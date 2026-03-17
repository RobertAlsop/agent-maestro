#!/usr/bin/env python3
"""summarise_report.py — Append an LLM-generated summary to a vault health report.

Reads the specified health report, sends it to a local LLM via Ollama,
and appends a one-paragraph natural language summary under a
'## LLM Summary' heading.

Exit codes:
    0 — Summary appended successfully
    2 — Error (Ollama unavailable, model missing, API failure)

Usage:
    python3 summarise_report.py <report_path> [--config <config_path>]
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# Defaults — overridden by config file if provided
DEFAULT_OLLAMA_HOST = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"

SUMMARY_HEADING = "## LLM Summary"

SYSTEM_PROMPT = (
    "You are a vault maintenance assistant. You will receive a structured "
    "health report from an Obsidian vault integrity scan. Produce a single "
    "paragraph summarising the key findings: what passed, what has issues, "
    "and what needs attention. Be concise and specific — cite tool names "
    "and counts. If everything is clean, say so in one sentence."
)


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


def check_model_available(host, model):
    """Verify the configured model is available in Ollama."""
    try:
        url = f"{host}/api/tags"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            models = [m.get("name", "") for m in data.get("models", [])]
            # Match both "llama3.2" and "llama3.2:latest"
            return any(model == m or m.startswith(f"{model}:") for m in models)
    except (urllib.error.URLError, OSError, json.JSONDecodeError):
        return False


def generate_summary(host, model, report_content):
    """Call Ollama's generate API and return the summary text."""
    url = f"{host}/api/generate"
    payload = json.dumps({
        "model": model,
        "system": SYSTEM_PROMPT,
        "prompt": report_content,
        "stream": False,
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode())
        return data.get("response", "").strip()


def main():
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage: summarise_report.py <report_path> [--config <config_path>]", file=sys.stderr)
        sys.exit(2)

    report_path = sys.argv[1]
    config_path = None

    if "--config" in sys.argv:
        idx = sys.argv.index("--config")
        if idx + 1 < len(sys.argv):
            config_path = sys.argv[idx + 1]

    # Default config location: config.yaml next to this script
    if not config_path:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        default_config = os.path.join(script_dir, "config.yaml")
        if os.path.isfile(default_config):
            config_path = default_config

    config = load_config(config_path)
    host = config["ollama_host"]
    model = config["model"]

    # Validate report exists
    if not os.path.isfile(report_path):
        print(f"ERROR: Report not found: {report_path}", file=sys.stderr)
        sys.exit(2)

    # Read report
    with open(report_path, "r") as f:
        report_content = f.read()

    # Check for existing summary (idempotency)
    if SUMMARY_HEADING in report_content:
        print("Summary already exists — skipping.", file=sys.stderr)
        sys.exit(0)

    # Check Ollama and model availability
    if not check_model_available(host, model):
        print(f"ERROR: Model '{model}' not available at {host}", file=sys.stderr)
        print("Is Ollama running? Is the model installed?", file=sys.stderr)
        sys.exit(2)

    # Generate summary
    try:
        summary = generate_summary(host, model, report_content)
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as e:
        print(f"ERROR: LLM call failed: {e}", file=sys.stderr)
        sys.exit(2)

    if not summary:
        print("ERROR: LLM returned empty response", file=sys.stderr)
        sys.exit(2)

    # Append summary to report
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    summary_block = (
        f"\n{SUMMARY_HEADING}\n\n"
        f"**Generated:** {timestamp}  \n"
        f"**Model:** {model}\n\n"
        f"{summary}\n"
    )

    with open(report_path, "a") as f:
        f.write(summary_block)

    print(f"Summary appended to {report_path}")
    sys.exit(0)


if __name__ == "__main__":
    main()
