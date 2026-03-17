#!/usr/bin/env bash
# run_maintenance.sh — Wrapper script for scheduled vault maintenance.
#
# Coordinates the full maintenance sequence:
#   1. Run orchestrate.sh (mechanical integrity)
#   2. Run extract_metrics.py (temporal metric extraction, if available)
#   3. Run summarise_report.py (semantic summary, if available)
#   4. Run notify.sh (notification on findings, if available)
#
# Called by launchd plist. Each phase degrades gracefully if its
# script is not present or fails.
#
# Exit codes mirror orchestrate.sh: 0 = clean, 1 = findings, 2 = error

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VAULT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
TOOLS_DIR="${VAULT_ROOT}/04_EXECUTE/tools/vault-maintenance"
CONFIG_FILE="${TOOLS_DIR}/config/am.conf"
REPORT_DIR="${VAULT_ROOT}/05_RECORD/reports"
LOG_DIR="${TOOLS_DIR}/logs"
DATE_STAMP="$(date +%Y-%m-%d)"
REPORT_FILE="${REPORT_DIR}/vault_health_report_${DATE_STAMP}.md"

mkdir -p "$REPORT_DIR" "$LOG_DIR"

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%S)] $*" >> "${LOG_DIR}/run_maintenance.log"
}

log "=== Maintenance run started ==="

# --- Phase 1: Mechanical Integrity ---

ORCHESTRATOR="${TOOLS_DIR}/orchestrate.sh"

if [[ ! -x "$ORCHESTRATOR" ]]; then
    log "ERROR: orchestrate.sh not found or not executable at ${ORCHESTRATOR}"
    exit 2
fi

log "Running orchestrate.sh..."
set +e
"$ORCHESTRATOR" \
    --config "$CONFIG_FILE" \
    --vault-root "$VAULT_ROOT" \
    --output-dir "$REPORT_DIR" \
    --quiet \
    2>&1 | while IFS= read -r line; do log "  orchestrate: $line"; done

orchestrator_exit=${PIPESTATUS[0]}
set -e

log "orchestrate.sh exited with code ${orchestrator_exit}"

# Rename the generic report to date-stamped version
GENERIC_REPORT="${REPORT_DIR}/vault_health_report.md"
if [[ -f "$GENERIC_REPORT" ]]; then
    mv "$GENERIC_REPORT" "$REPORT_FILE"
    log "Report saved: ${REPORT_FILE}"
fi

# --- Phase 2: Metric Extraction (optional) ---

EXTRACTOR="${TOOLS_DIR}/extract_metrics.py"
OBSERVATION_CSV="${VAULT_ROOT}/05_RECORD/logs/observation_metrics.csv"

if [[ -x "$EXTRACTOR" ]]; then
    log "Running extract_metrics.py..."
    set +e
    python3 "$EXTRACTOR" \
        --config "$CONFIG_FILE" \
        --vault-root "$VAULT_ROOT" \
        --output-dir "${TOOLS_DIR}/reports" \
        --csv-path "$OBSERVATION_CSV" \
        --quiet \
        2>&1 | while IFS= read -r line; do log "  extract: $line"; done
    extract_exit=${PIPESTATUS[0]}
    set -e
    log "extract_metrics.py exited with code ${extract_exit}"
    if [[ $extract_exit -eq 2 ]]; then
        log "WARNING: Metric extraction failed (exit 2) — continuing"
    fi
else
    log "Skipping metric extraction (extract_metrics.py not available)"
fi

# --- Phase 3: LLM Summary (optional) ---

SUMMARISER="${SCRIPT_DIR}/summarise_report.py"

if [[ -x "$SUMMARISER" && -f "$REPORT_FILE" ]]; then
    log "Running summarise_report.py..."
    set +e
    python3 "$SUMMARISER" "$REPORT_FILE" 2>&1 | while IFS= read -r line; do log "  summarise: $line"; done
    summarise_exit=${PIPESTATUS[0]}
    set -e
    log "summarise_report.py exited with code ${summarise_exit}"
    if [[ $summarise_exit -eq 2 ]]; then
        log "WARNING: Summary failed (exit 2) — report unchanged"
    fi
else
    log "Skipping summary (script not available or no report)"
fi

# --- Phase 4: Notification (optional) ---

NOTIFIER="${SCRIPT_DIR}/notify.sh"

if [[ -x "$NOTIFIER" ]]; then
    if [[ $orchestrator_exit -eq 1 ]]; then
        log "Running notify.sh (findings detected)..."
        set +e
        "$NOTIFIER" "$REPORT_FILE" 2>&1 | while IFS= read -r line; do log "  notify: $line"; done
        notify_exit=${PIPESTATUS[0]}
        set -e
        log "notify.sh exited with code ${notify_exit}"
    else
        log "Skipping notification (no findings — exit code ${orchestrator_exit})"
    fi
else
    log "Skipping notification (notify.sh not available)"
fi

log "=== Maintenance run finished (overall exit: ${orchestrator_exit}) ==="

exit $orchestrator_exit
