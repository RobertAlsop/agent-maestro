#!/usr/bin/env bash
# notify.sh — Send a macOS notification when vault maintenance finds issues.
#
# Called by run_maintenance.sh only when orchestrate.sh exits with code 1 (findings).
# Reads the report to extract the LLM summary if present; falls back to a
# generic findings message.
#
# Usage: notify.sh <report_path>

set -uo pipefail

REPORT_PATH="${1:-}"

if [[ -z "$REPORT_PATH" || ! -f "$REPORT_PATH" ]]; then
    echo "ERROR: Report path required and must exist" >&2
    exit 2
fi

TITLE="Agent Maestro — Vault Findings"

# Try to extract the LLM summary paragraph (text between ## LLM Summary and next ## or EOF)
SUMMARY=""
if grep -q "^## LLM Summary" "$REPORT_PATH" 2>/dev/null; then
    SUMMARY=$(sed -n '/^## LLM Summary$/,/^## /{
        /^## /d
        /^\*\*/d
        /^$/d
        p
    }' "$REPORT_PATH" | head -5 | tr '\n' ' ' | sed 's/  */ /g' | head -c 500)
fi

# Fallback: count tools with findings from the Tool Summary table
if [[ -z "$SUMMARY" ]]; then
    FINDINGS_COUNT=$(grep -c "| FINDINGS |" "$REPORT_PATH" 2>/dev/null || echo "0")
    SUMMARY="Vault health check found issues in ${FINDINGS_COUNT} tool(s). Review the report for details."
fi

# Send macOS notification
osascript -e "display notification \"${SUMMARY}\" with title \"${TITLE}\""

echo "Notification sent."
