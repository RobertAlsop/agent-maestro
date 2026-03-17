#!/usr/bin/env python3
"""extract_metrics.py — Temporal metric extraction from vault maintenance reports.

Data transformation tool that reads per-tool reports produced by orchestrate.sh
and extracts standard metrics into CSV rows for temporal analysis.

This is NOT a detection tool. It does not check rules or produce findings.
It transforms report data into a temporal format (observation_metrics.csv).

Differences from standard Tool Conventions (acknowledged per Wave 9 proposal):
  - Stateful across runs: reads existing CSV to compute deltas.
    Degrades gracefully on first run (delta fields are empty).
  - Writes to vault content tree: appends to 05_RECORD/logs/observation_metrics.csv,
    not to the tool's own output directory. Temporal data belongs in the Record layer.

Borrows from Tool Conventions: config-driven, composable, meaningful exit codes,
conservative, dual-audience output.

Exit codes:
  0 — Metrics extracted successfully (all escalation levels are 1)
  1 — Metrics extracted but threshold breaches detected (escalation level >= 2)
  2 — Tool itself failed (config missing, vault path invalid, etc.)

Input:  Per-tool reports in the configured reports directory.
Output: Rows appended to observation_metrics.csv.
"""

import csv
import io
import os
import re
import sys
import tempfile
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Path setup — allow importing from lib/
# ---------------------------------------------------------------------------
TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOL_DIR)

from lib.vault_model import standard_arg_parser, resolve_tool_paths

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
TOOL_NAME = "Metric Extraction"
CSV_FILENAME = "observation_metrics.csv"
REGISTRY_FILENAME = "metric_registry.csv"

CSV_FIELDS = [
    "timestamp", "run_id", "tool", "metric_name", "metric_value",
    "previous_value", "delta", "direction", "category", "goal_trace",
    "threshold", "escalation_level", "source_report",
]

# Regex for the standard summary table row: | 28 | 14 | 0 | 0 |
SUMMARY_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
    re.MULTILINE,
)

# Regex for the tool name from report header: # Tool Name Report
HEADER_RE = re.compile(r"^#\s+(.+?)\s+Report\s*$", re.MULTILINE)

# Regex for the date line: **Date:** 2026-03-17T09:46:30
DATE_RE = re.compile(r"\*\*Date:\*\*\s*(\S+)")

# Health report tool summary row: | Tool Name | 0 | CLEAN | — |
HEALTH_ROW_RE = re.compile(
    r"^\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*(CLEAN|FINDINGS|ERROR)\s*\|",
    re.MULTILINE,
)

# Map result strings to numeric values for the overall_result metric
RESULT_MAP = {"CLEAN": 0, "FINDINGS": 1, "ERROR": 2}


# ---------------------------------------------------------------------------
# Registry loading
# ---------------------------------------------------------------------------
def load_registry(config_dir):
    """Load metric_registry.csv. Returns {(tool, metric_name): row_dict}."""
    path = os.path.join(config_dir, REGISTRY_FILENAME)
    registry = {}
    if not os.path.isfile(path):
        return registry
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["tool"], row["metric_name"])
            registry[key] = row
    return registry


def registry_lookup(registry, tool, metric_name):
    """Look up a metric in the registry. Returns dict or defaults."""
    key = (tool, metric_name)
    if key in registry:
        return registry[key]
    return {
        "enabled": "true",
        "polarity": "lower_is_better",
        "threshold": "0",
        "default_escalation": "1",
        "category": "",
        "goal_trace": "",
    }


# ---------------------------------------------------------------------------
# Previous value loading
# ---------------------------------------------------------------------------
def load_previous_values(csv_path):
    """Load the most recent value for each (tool, metric_name) from the CSV.

    Returns {(tool, metric_name): metric_value_str}.
    """
    previous = {}
    if not os.path.isfile(csv_path):
        return previous
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["tool"], row["metric_name"])
            previous[key] = row["metric_value"]
    return previous


# ---------------------------------------------------------------------------
# Report parsing
# ---------------------------------------------------------------------------
def parse_tool_report(report_path):
    """Parse a per-tool report. Returns (tool_name, date_str, metrics_dict) or None.

    metrics_dict has keys: checked, passed, failed, warnings (all ints).
    """
    try:
        with open(report_path, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    # Extract tool name from header
    header_match = HEADER_RE.search(content)
    if not header_match:
        return None
    tool_name = header_match.group(1).strip()

    # Extract date
    date_match = DATE_RE.search(content)
    date_str = date_match.group(1) if date_match else ""

    # Extract summary table
    summary_match = SUMMARY_RE.search(content)
    if not summary_match:
        return None  # No standard summary table (e.g., Inventory)

    metrics = {
        "checked": int(summary_match.group(1)),
        "passed": int(summary_match.group(2)),
        "failed": int(summary_match.group(3)),
        "warnings": int(summary_match.group(4)),
    }
    return tool_name, date_str, metrics


def parse_health_report(report_path):
    """Parse the aggregate health report. Returns (date_str, tool_results, overall_result).

    tool_results is a list of (tool_name, exit_code, result_str).
    overall_result is the **Result:** value.
    """
    try:
        with open(report_path, encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeDecodeError):
        return None

    # Extract date
    date_match = DATE_RE.search(content)
    date_str = date_match.group(1) if date_match else ""

    # Extract overall result
    result_match = re.search(r"\*\*Result:\*\*\s*(\w+)", content)
    overall_result = result_match.group(1) if result_match else ""

    # Extract tool summary rows
    tool_results = []
    for m in HEALTH_ROW_RE.finditer(content):
        tool_name = m.group(1).strip()
        if tool_name == "Tool":  # Skip header row
            continue
        exit_code = int(m.group(2))
        result_str = m.group(3)
        tool_results.append((tool_name, exit_code, result_str))

    return date_str, tool_results, overall_result


# ---------------------------------------------------------------------------
# Delta / direction computation
# ---------------------------------------------------------------------------
def compute_delta(current_value, previous_values, tool, metric_name, reg):
    """Compute previous_value, delta, and direction.

    Returns (previous_value_str, delta_str, direction_str).
    """
    key = (tool, metric_name)
    if key not in previous_values:
        return "", "", ""

    try:
        prev = int(previous_values[key])
    except (ValueError, TypeError):
        return "", "", ""

    delta = current_value - prev
    polarity = reg.get("polarity", "lower_is_better")

    if delta == 0:
        direction = "stable"
    elif polarity == "lower_is_better":
        direction = "improving" if delta < 0 else "degrading"
    else:  # higher_is_better
        direction = "improving" if delta > 0 else "degrading"

    return str(prev), str(delta), direction


# ---------------------------------------------------------------------------
# Escalation computation
# ---------------------------------------------------------------------------
def compute_escalation(value, reg):
    """Determine escalation level from threshold.

    Threshold-only rule (proposal IN-3 resolution):
      - If value breaches threshold → registry's default_escalation
      - Otherwise → 1
    Breach respects polarity:
      - lower_is_better: value > threshold = breach
      - higher_is_better: value < threshold = breach
    """
    try:
        threshold = int(reg.get("threshold", "0"))
        default_esc = int(reg.get("default_escalation", "1"))
    except (ValueError, TypeError):
        return 1

    polarity = reg.get("polarity", "lower_is_better")

    if polarity == "lower_is_better" and value > threshold:
        return default_esc
    elif polarity == "higher_is_better" and value < threshold:
        return default_esc
    return 1


# ---------------------------------------------------------------------------
# CSV writing (atomic)
# ---------------------------------------------------------------------------
def write_rows_atomic(csv_path, rows):
    """Append rows to CSV atomically. Creates the file with header if needed."""
    file_exists = os.path.isfile(csv_path) and os.path.getsize(csv_path) > 0

    # Write to a temp file in the same directory, then append
    csv_dir = os.path.dirname(csv_path)
    os.makedirs(csv_dir, exist_ok=True)

    # Build the new content
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_FIELDS)
    if not file_exists:
        writer.writeheader()
    for row in rows:
        writer.writerow(row)
    new_content = buf.getvalue()

    # Write to temp file, then append (or create)
    fd, tmp_path = tempfile.mkstemp(dir=csv_dir, suffix=".tmp")
    try:
        if file_exists:
            # Copy existing content
            with open(csv_path, "rb") as existing:
                os.write(fd, existing.read())
        os.write(fd, new_content.encode("utf-8"))
        os.close(fd)
        os.replace(tmp_path, csv_path)
    except Exception:
        os.close(fd) if not os.get_inheritable(fd) else None
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = standard_arg_parser(
        "Extract temporal metrics from vault maintenance reports into CSV."
    )
    parser.add_argument(
        "--csv-path",
        help="Path to observation_metrics.csv (default: 05_RECORD/logs/ in vault root)",
    )
    args = parser.parse_args()

    vault_root, config, output_dir, tool_dir = resolve_tool_paths(args, __file__)

    # Resolve paths
    config_dir = os.path.join(tool_dir, "config")

    # Per-tool reports live in tool_dir/reports/ (where orchestrate.sh writes them)
    tool_reports_dir = os.path.join(tool_dir, "reports")

    csv_path = args.csv_path or os.path.join(
        vault_root, "05_RECORD", "logs", CSV_FILENAME
    )

    # Validate
    if not os.path.isdir(vault_root):
        print(f"{TOOL_NAME}: ERROR — vault root not found: {vault_root}", file=sys.stderr)
        sys.exit(2)

    # Load registry
    registry = load_registry(config_dir)
    if not registry:
        print(f"{TOOL_NAME}: WARNING — metric registry not found at {config_dir}/{REGISTRY_FILENAME}, using defaults", file=sys.stderr)

    # Load previous values for delta computation
    previous_values = load_previous_values(csv_path)

    # Timestamp for this extraction
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Collect all rows to write
    rows = []
    warnings = []
    max_escalation = 1

    # --- Parse per-tool reports ---
    # Per-tool reports live in tool_dir/reports/ (orchestrate.sh writes them there)
    report_files = []
    if os.path.isdir(tool_reports_dir):
        for fname in sorted(os.listdir(tool_reports_dir)):
            if fname.endswith("_report.md") and fname != "vault_health_report.md":
                report_files.append((fname, os.path.join(tool_reports_dir, fname)))

    run_id = ""  # Will be set from the first report's date

    for fname, fpath in report_files:
        result = parse_tool_report(fpath)
        if result is None:
            warnings.append(f"Skipped {fname}: no standard summary table")
            continue

        tool_name, date_str, metrics = result

        # Set run_id from the first report's date (YYYY-MM-DD portion)
        if not run_id and date_str:
            run_id = date_str[:10]  # e.g., "2026-03-17" from "2026-03-17T09:46:30"

        for metric_name, value in metrics.items():
            reg = registry_lookup(registry, tool_name, metric_name)

            # Skip disabled metrics
            if reg.get("enabled", "true").lower() == "false":
                continue

            prev_str, delta_str, direction = compute_delta(
                value, previous_values, tool_name, metric_name, reg
            )
            esc_level = compute_escalation(value, reg)
            if esc_level > max_escalation:
                max_escalation = esc_level

            rows.append({
                "timestamp": timestamp,
                "run_id": run_id,
                "tool": tool_name,
                "metric_name": metric_name,
                "metric_value": str(value),
                "previous_value": prev_str,
                "delta": delta_str,
                "direction": direction,
                "category": reg.get("category", ""),
                "goal_trace": reg.get("goal_trace", ""),
                "threshold": reg.get("threshold", ""),
                "escalation_level": str(esc_level),
                "source_report": fname,
            })

    # --- Parse aggregate health report ---
    health_report_path = None
    candidate = os.path.join(tool_reports_dir, "vault_health_report.md")
    if os.path.isfile(candidate):
        health_report_path = candidate
    # Also check date-stamped version in 05_RECORD/reports/
    if not health_report_path:
        record_reports = os.path.join(vault_root, "05_RECORD", "reports")
        if os.path.isdir(record_reports):
            # Find most recent date-stamped health report
            candidates = sorted(
                [f for f in os.listdir(record_reports)
                 if f.startswith("vault_health_report_") and f.endswith(".md")],
                reverse=True,
            )
            if candidates:
                health_report_path = os.path.join(record_reports, candidates[0])

    if health_report_path:
        health_result = parse_health_report(health_report_path)
        if health_result:
            date_str, tool_results, overall_result = health_result

            if not run_id and date_str:
                run_id = date_str[:10]

            # Aggregate metrics
            tools_clean = sum(1 for _, ec, _ in tool_results if ec == 0)
            tools_findings = sum(1 for _, ec, _ in tool_results if ec == 1)
            tools_error = sum(1 for _, ec, _ in tool_results if ec == 2)
            overall_numeric = RESULT_MAP.get(overall_result, 2)

            health_fname = os.path.basename(health_report_path)
            aggregate_metrics = [
                ("tools_clean", tools_clean),
                ("tools_findings", tools_findings),
                ("tools_error", tools_error),
                ("overall_result", overall_numeric),
            ]

            for metric_name, value in aggregate_metrics:
                reg = registry_lookup(registry, "Health Report", metric_name)

                if reg.get("enabled", "true").lower() == "false":
                    continue

                prev_str, delta_str, direction = compute_delta(
                    value, previous_values, "Health Report", metric_name, reg
                )
                esc_level = compute_escalation(value, reg)
                if esc_level > max_escalation:
                    max_escalation = esc_level

                rows.append({
                    "timestamp": timestamp,
                    "run_id": run_id,
                    "tool": "Health Report",
                    "metric_name": metric_name,
                    "metric_value": str(value),
                    "previous_value": prev_str,
                    "delta": delta_str,
                    "direction": direction,
                    "category": reg.get("category", ""),
                    "goal_trace": reg.get("goal_trace", ""),
                    "threshold": reg.get("threshold", ""),
                    "escalation_level": str(esc_level),
                    "source_report": health_fname,
                })
        else:
            warnings.append("Skipped health report: could not parse")
    else:
        warnings.append("No health report found")

    # Fallback run_id if no date was extracted
    if not run_id:
        run_id = now.strftime("%Y-%m-%d")
        for row in rows:
            row["run_id"] = run_id

    # --- Write CSV ---
    if not rows:
        print(f"{TOOL_NAME}: WARNING — no metrics extracted", file=sys.stderr)
        sys.exit(2)

    write_rows_atomic(csv_path, rows)

    # --- Output ---
    escalation_summary = ""
    if max_escalation >= 2:
        breach_count = sum(1 for r in rows if int(r["escalation_level"]) >= 2)
        escalation_summary = f", {breach_count} threshold breaches"

    if not args.quiet:
        print(f"{TOOL_NAME}: {len(rows)} metrics extracted for run {run_id}{escalation_summary}")
        if warnings:
            for w in warnings:
                print(f"  WARNING: {w}")
        print(f"CSV: {csv_path}")

    # Exit code: 1 if any threshold breaches, 0 if all clean
    sys.exit(1 if max_escalation >= 2 else 0)


if __name__ == "__main__":
    main()
