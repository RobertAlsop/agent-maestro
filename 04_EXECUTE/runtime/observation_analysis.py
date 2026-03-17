#!/usr/bin/env python3
"""observation_analysis.py — Semantic trend analysis of vault observation metrics.

Reads observation_metrics.csv (produced by extract_metrics.py), identifies trends
and anomalies, and invokes a local LLM to interpret them. Produces an observation
analysis report in 05_RECORD/reports/.

Escalation-governed intensity (per Wave 9 proposal):
  Level 1 (no anomalies): Brief mechanical summary — "all metrics stable."
  Level 2 (anomalies/trends): Causal analysis, formulate recommendation.
  Level 3 (governance concern): Full analysis with proposal draft for human review.

This script lives in 04_EXECUTE/runtime/ (not tools/) because it performs semantic
interpretation via LLM, following the Wave 7 precedent set by summarise_report.py.

Exit codes:
    0 — Analysis produced successfully
    1 — Analysis produced with Level 2+ findings (threshold breaches or trends)
    2 — Error (insufficient data, config missing, LLM unavailable)

Usage:
    python3 observation_analysis.py [--csv-path PATH] [--config PATH]
           [--min-runs N] [--output-dir PATH] [--vault-root PATH] [--quiet]
"""

import csv
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
DEFAULT_OLLAMA_HOST = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"
DEFAULT_MIN_RUNS = 5
REPORT_HEADING = "# Observation Analysis Report"

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
def load_config(config_path):
    """Load config from a YAML-like file (simple key: value parsing)."""
    config = {
        "ollama_host": DEFAULT_OLLAMA_HOST,
        "model": DEFAULT_MODEL,
    }
    if config_path and os.path.isfile(config_path):
        with open(config_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key in config:
                        config[key] = value
    return config


# ---------------------------------------------------------------------------
# CSV loading and trend computation
# ---------------------------------------------------------------------------
def load_metrics(csv_path):
    """Load observation_metrics.csv. Returns list of row dicts."""
    rows = []
    if not os.path.isfile(csv_path):
        return rows
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def group_by_run(rows):
    """Group rows by run_id. Returns {run_id: [rows]} ordered by run_id."""
    groups = defaultdict(list)
    for row in rows:
        groups[row["run_id"]].append(row)
    return dict(sorted(groups.items()))


def compute_trends(rows):
    """Compute trend data for each (tool, metric_name) across all runs.

    Returns a dict: {(tool, metric_name): {
        "values": [(run_id, value), ...],
        "current": int,
        "previous": int or None,
        "delta": int or None,
        "direction": str,
        "polarity": str,
        "threshold": int,
        "escalation_level": int,
        "category": str,
        "sustained_direction": str,  # "improving", "degrading", "stable", "mixed"
        "sustained_count": int,      # consecutive runs in same direction
        "breach_runs": int,          # number of runs with threshold breach
        "total_runs": int,
    }}
    """
    # Collect time series for each metric
    series = defaultdict(list)
    meta = {}

    for row in rows:
        key = (row["tool"], row["metric_name"])
        try:
            value = int(row["metric_value"])
        except (ValueError, TypeError):
            continue
        series[key].append((row["run_id"], value))

        # Store latest metadata
        meta[key] = {
            "category": row.get("category", ""),
            "goal_trace": row.get("goal_trace", ""),
            "threshold": row.get("threshold", "0"),
            "escalation_level": row.get("escalation_level", "1"),
        }

    trends = {}
    for key, points in series.items():
        # Deduplicate by run_id (take last value per run)
        by_run = {}
        for run_id, val in points:
            by_run[run_id] = val
        ordered = sorted(by_run.items())

        values = [v for _, v in ordered]
        current = values[-1]
        previous = values[-2] if len(values) >= 2 else None
        delta = current - previous if previous is not None else None

        m = meta[key]
        try:
            threshold = int(m["threshold"])
        except (ValueError, TypeError):
            threshold = 0
        try:
            esc_level = int(m["escalation_level"])
        except (ValueError, TypeError):
            esc_level = 1

        # Determine polarity from registry data embedded in CSV
        # We infer from the direction field in the most recent row with a direction
        polarity = "lower_is_better"  # default for failed/warnings
        metric_name = key[1]
        if metric_name in ("checked", "passed", "tools_clean"):
            polarity = "higher_is_better"

        # Compute sustained direction (consecutive same-direction changes)
        if len(values) < 2:
            sustained_dir = "stable"
            sustained_count = len(values)
        else:
            deltas = [values[i] - values[i - 1] for i in range(1, len(values))]
            if not deltas:
                sustained_dir = "stable"
                sustained_count = len(values)
            else:
                # Check last N consecutive deltas for same sign
                last_sign = (1 if deltas[-1] > 0 else (-1 if deltas[-1] < 0 else 0))
                sustained_count = 0
                for d in reversed(deltas):
                    sign = 1 if d > 0 else (-1 if d < 0 else 0)
                    if sign == last_sign:
                        sustained_count += 1
                    else:
                        break

                if last_sign == 0:
                    sustained_dir = "stable"
                elif polarity == "lower_is_better":
                    sustained_dir = "improving" if last_sign < 0 else "degrading"
                else:
                    sustained_dir = "improving" if last_sign > 0 else "degrading"

        # Count breach runs
        breach_runs = 0
        for val in values:
            if polarity == "lower_is_better" and val > threshold:
                breach_runs += 1
            elif polarity == "higher_is_better" and val < threshold:
                breach_runs += 1

        trends[key] = {
            "values": ordered,
            "current": current,
            "previous": previous,
            "delta": delta,
            "direction": (
                "stable" if delta is None or delta == 0
                else ("improving" if (polarity == "lower_is_better" and delta < 0)
                      or (polarity == "higher_is_better" and delta > 0)
                      else "degrading")
            ),
            "polarity": polarity,
            "threshold": threshold,
            "escalation_level": esc_level,
            "category": m["category"],
            "goal_trace": m["goal_trace"],
            "sustained_direction": sustained_dir,
            "sustained_count": sustained_count,
            "breach_runs": breach_runs,
            "total_runs": len(ordered),
        }

    return trends


def classify_metrics(trends, min_runs):
    """Classify metrics into escalation groups.

    Returns (level_1_metrics, level_2_metrics, level_3_metrics).
    Level 2 = threshold breaches OR sustained degrading trends (>= min_runs/2 consecutive).
    Level 3 = governance-related metrics at Level 2 (category = 'process' with high breach rate).
    """
    level_1 = []
    level_2 = []
    level_3 = []

    for key, t in trends.items():
        is_breach = t["escalation_level"] >= 2
        is_sustained_degrading = (
            t["sustained_direction"] == "degrading"
            and t["sustained_count"] >= max(2, min_runs // 2)
        )
        is_persistent_breach = t["breach_runs"] > t["total_runs"] // 2

        if is_breach and is_persistent_breach and t["category"] == "process":
            level_3.append((key, t))
        elif is_breach or is_sustained_degrading:
            level_2.append((key, t))
        else:
            level_1.append((key, t))

    return level_1, level_2, level_3


# ---------------------------------------------------------------------------
# Mechanical summary (Level 1 — no LLM needed)
# ---------------------------------------------------------------------------
def build_mechanical_summary(trends, run_ids, level_1, level_2, level_3):
    """Build a brief mechanical summary for Level 1 output."""
    total = len(trends)
    stable = sum(1 for t in trends.values() if t["direction"] == "stable")
    improving = sum(1 for t in trends.values() if t["direction"] == "improving")
    degrading = sum(1 for t in trends.values() if t["direction"] == "degrading")
    breaches = sum(1 for t in trends.values() if t["escalation_level"] >= 2)

    categories = defaultdict(lambda: {"total": 0, "breaches": 0})
    for key, t in trends.items():
        cat = t["category"] or "uncategorised"
        categories[cat]["total"] += 1
        if t["escalation_level"] >= 2:
            categories[cat]["breaches"] += 1

    lines = []
    lines.append(f"**Runs analysed:** {len(run_ids)} (from {run_ids[0]} to {run_ids[-1]})")
    lines.append(f"**Metrics tracked:** {total}")
    lines.append(f"**Current direction:** {stable} stable, {improving} improving, {degrading} degrading")
    lines.append(f"**Threshold breaches:** {breaches}")
    lines.append("")
    lines.append("| Category | Metrics | Breaches |")
    lines.append("|----------|---------|----------|")
    for cat in sorted(categories):
        c = categories[cat]
        lines.append(f"| {cat} | {c['total']} | {c['breaches']} |")

    return "\n".join(lines)


def build_findings_table(level_2, level_3):
    """Build a findings table for Level 2+ metrics."""
    items = level_2 + level_3
    if not items:
        return "No anomalies detected."

    lines = []
    lines.append("| Tool | Metric | Current | Threshold | Direction | Sustained | Breach Rate |")
    lines.append("|------|--------|---------|-----------|-----------|-----------|-------------|")
    for key, t in sorted(items, key=lambda x: (-x[1]["escalation_level"], x[0])):
        tool, metric = key
        breach_rate = f"{t['breach_runs']}/{t['total_runs']}"
        lines.append(
            f"| {tool} | {metric} | {t['current']} | {t['threshold']} "
            f"| {t['direction']} | {t['sustained_direction']} ({t['sustained_count']} runs) "
            f"| {breach_rate} |"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# LLM interaction (Level 2+)
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are a vault observation analyst for Agent Maestro, an operational intelligence system. \
You will receive structured trend data from the system's self-observation metrics. \
Your task is to interpret the data and provide causal analysis.

Follow these conventions:
- Ground every claim in the data provided. Do not invent metrics or values.
- Express uncertainty qualitatively: "likely", "possibly", "insufficient evidence".
- When a trend could have multiple causes, present all plausible explanations.
- Short-term fluctuations in small-count metrics (e.g., failed going from 0 to 1 to 0) \
are noise, not trends. Require sustained directional change across multiple runs.
- State the sample size when reporting trends.
- Do not recommend changes to governance documents — escalate those to the human.
- Structure your response as: Summary paragraph, then Findings (one per anomaly), \
then Recommendations (concrete, actionable).
- Be concise. Cite tool names and metric names specifically.\
"""


def check_model_available(host, model):
    """Verify the configured model is available in Ollama."""
    try:
        url = f"{host}/api/tags"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            models = [m.get("name", "") for m in data.get("models", [])]
            return any(model == m or m.startswith(f"{model}:") for m in models)
    except (urllib.error.URLError, OSError, json.JSONDecodeError):
        return False


def generate_analysis(host, model, prompt_text):
    """Call Ollama's generate API and return the analysis text."""
    url = f"{host}/api/generate"
    payload = json.dumps({
        "model": model,
        "system": SYSTEM_PROMPT,
        "prompt": prompt_text,
        "stream": False,
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode())
        return data.get("response", "").strip()


def build_llm_prompt(trends, run_ids, level_2, level_3):
    """Build the prompt sent to the LLM for trend interpretation."""
    lines = []
    lines.append(f"Observation data covers {len(run_ids)} maintenance runs "
                 f"from {run_ids[0]} to {run_ids[-1]}.")
    lines.append("")

    # Level 2 findings
    if level_2:
        lines.append("## Anomalies (Level 2 — agent judgment required)")
        lines.append("")
        for key, t in level_2:
            tool, metric = key
            history = ", ".join(f"{rid}={v}" for rid, v in t["values"][-5:])
            lines.append(f"- **{tool}.{metric}**: current={t['current']}, "
                        f"threshold={t['threshold']}, "
                        f"direction={t['direction']}, "
                        f"sustained={t['sustained_direction']} for {t['sustained_count']} runs, "
                        f"breach rate={t['breach_runs']}/{t['total_runs']}. "
                        f"Recent history: [{history}]")
        lines.append("")

    # Level 3 findings
    if level_3:
        lines.append("## Governance Concerns (Level 3 — human review required)")
        lines.append("")
        for key, t in level_3:
            tool, metric = key
            history = ", ".join(f"{rid}={v}" for rid, v in t["values"][-5:])
            lines.append(f"- **{tool}.{metric}**: current={t['current']}, "
                        f"threshold={t['threshold']}, "
                        f"category={t['category']}, "
                        f"sustained={t['sustained_direction']} for {t['sustained_count']} runs, "
                        f"breach rate={t['breach_runs']}/{t['total_runs']}. "
                        f"Recent history: [{history}]")
        lines.append("")

    # Context: stable metrics summary
    stable_count = sum(1 for t in trends.values()
                      if t["escalation_level"] < 2 and t["sustained_direction"] != "degrading")
    lines.append(f"Context: {stable_count} other metrics are within threshold and stable/improving.")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Report writing
# ---------------------------------------------------------------------------
def write_report(output_dir, run_ids, mechanical_summary, findings_table,
                 llm_analysis, escalation_level, model_name):
    """Write the observation analysis report."""
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    date_stamp = now.strftime("%Y-%m-%d")

    level_label = {1: "STABLE", 2: "ANOMALIES", 3: "GOVERNANCE CONCERN"}
    result = level_label.get(escalation_level, "STABLE")

    lines = []
    lines.append(REPORT_HEADING)
    lines.append("")
    lines.append(f"**Date:** {timestamp}")
    lines.append(f"**Result:** {result}")
    lines.append(f"**Escalation Level:** {escalation_level}")
    lines.append(f"**Runs Covered:** {run_ids[0]} to {run_ids[-1]} ({len(run_ids)} runs)")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append(mechanical_summary)
    lines.append("")

    if findings_table and findings_table != "No anomalies detected.":
        lines.append("## Findings")
        lines.append("")
        lines.append(findings_table)
        lines.append("")

    if llm_analysis:
        lines.append("## Analysis")
        lines.append("")
        lines.append(f"**Model:** {model_name}")
        lines.append("")
        lines.append(llm_analysis)
        lines.append("")

    os.makedirs(output_dir, exist_ok=True)
    filename = f"observation_analysis_{date_stamp}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return filepath


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Semantic trend analysis of vault observation metrics."
    )
    parser.add_argument("--csv-path", help="Path to observation_metrics.csv")
    parser.add_argument("--config", help="Path to config file (ollama_host, model)")
    parser.add_argument("--min-runs", type=int, default=DEFAULT_MIN_RUNS,
                       help=f"Minimum runs required for analysis (default: {DEFAULT_MIN_RUNS})")
    parser.add_argument("--output-dir", help="Directory for analysis report "
                       "(default: 05_RECORD/reports/ in vault root)")
    parser.add_argument("--vault-root", help="Vault root directory")
    parser.add_argument("--quiet", action="store_true", help="Suppress stdout output")
    args = parser.parse_args()

    # Resolve vault root
    vault_root = args.vault_root
    if not vault_root:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        vault_root = os.path.abspath(os.path.join(script_dir, "..", ".."))
    vault_root = os.path.abspath(vault_root)

    # Resolve paths
    csv_path = args.csv_path or os.path.join(
        vault_root, "05_RECORD", "logs", "observation_metrics.csv"
    )
    output_dir = args.output_dir or os.path.join(vault_root, "05_RECORD", "reports")

    # Load config
    config_path = args.config
    if not config_path:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        default_config = os.path.join(script_dir, "config.yaml")
        if os.path.isfile(default_config):
            config_path = default_config
    config = load_config(config_path)
    host = config["ollama_host"]
    model = config["model"]

    # Load and validate data
    rows = load_metrics(csv_path)
    if not rows:
        if not args.quiet:
            print("Observation Analysis: no metric data found — nothing to analyse")
        sys.exit(2)

    runs = group_by_run(rows)
    run_ids = list(runs.keys())

    if len(run_ids) < args.min_runs:
        if not args.quiet:
            print(f"Observation Analysis: insufficient history — "
                  f"{len(run_ids)} runs found, {args.min_runs} required")
        sys.exit(2)

    # Compute trends
    trends = compute_trends(rows)
    level_1, level_2, level_3 = classify_metrics(trends, args.min_runs)

    # Determine overall escalation level
    if level_3:
        overall_level = 3
    elif level_2:
        overall_level = 2
    else:
        overall_level = 1

    # Build mechanical summary (always produced)
    mechanical_summary = build_mechanical_summary(trends, run_ids, level_1, level_2, level_3)
    findings_table = build_findings_table(level_2, level_3)

    # LLM analysis (Level 2+ only)
    llm_analysis = None
    if overall_level >= 2:
        if check_model_available(host, model):
            prompt = build_llm_prompt(trends, run_ids, level_2, level_3)
            try:
                llm_analysis = generate_analysis(host, model, prompt)
            except (urllib.error.URLError, OSError, json.JSONDecodeError) as e:
                if not args.quiet:
                    print(f"  WARNING: LLM call failed: {e}", file=sys.stderr)
                llm_analysis = (
                    "*LLM analysis unavailable — Ollama call failed. "
                    "Mechanical findings above are complete. "
                    "Review the findings table manually.*"
                )
        else:
            if not args.quiet:
                print(f"  WARNING: Model '{model}' not available at {host}", file=sys.stderr)
            llm_analysis = (
                "*LLM analysis unavailable — model not reachable. "
                "Mechanical findings above are complete. "
                "Review the findings table manually.*"
            )

    # Write report
    report_path = write_report(
        output_dir, run_ids, mechanical_summary, findings_table,
        llm_analysis, overall_level, model,
    )

    # Output
    if not args.quiet:
        level_label = {1: "STABLE", 2: "ANOMALIES", 3: "GOVERNANCE CONCERN"}
        result = level_label.get(overall_level, "STABLE")
        l2_count = len(level_2)
        l3_count = len(level_3)
        print(f"Observation Analysis: {result} "
              f"({len(run_ids)} runs, {len(trends)} metrics, "
              f"{l2_count} anomalies, {l3_count} governance concerns)")
        print(f"Report: {report_path}")

    sys.exit(1 if overall_level >= 2 else 0)


if __name__ == "__main__":
    main()
