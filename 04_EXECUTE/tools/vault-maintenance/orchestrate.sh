#!/usr/bin/env bash
# orchestrate.sh — Run all vault-maintenance tools in sequence and produce
# an aggregate health report.
#
# Reads config, executes each tool, collects exit codes and finding counts,
# produces vault_health_report.md.
#
# Exit codes: 0 = all clean, 1 = any findings, 2 = any errors

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Parse arguments
CONFIG_FILE=""
VAULT_ROOT_ARG=""
OUTPUT_DIR_ARG=""
QUIET=""
TOOL_ARGS=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)    CONFIG_FILE="$2"; TOOL_ARGS+=(--config "$2"); shift 2 ;;
        --vault-root) VAULT_ROOT_ARG="$2"; TOOL_ARGS+=(--vault-root "$2"); shift 2 ;;
        --output-dir) OUTPUT_DIR_ARG="$2"; TOOL_ARGS+=(--output-dir "$2"); shift 2 ;;
        --quiet)     QUIET="true"; TOOL_ARGS+=(--quiet); shift ;;
        *)           shift ;;
    esac
done

# Determine output dir
if [[ -n "$OUTPUT_DIR_ARG" ]]; then
    OUT_DIR="$OUTPUT_DIR_ARG"
else
    OUT_DIR="${SCRIPT_DIR}/reports"
fi
[[ "$OUT_DIR" != /* ]] && OUT_DIR="${SCRIPT_DIR}/${OUT_DIR}"
mkdir -p "$OUT_DIR"

# Tools to run, in order
TOOLS=(
    "structure_check.sh:Structure Check"
    "yaml_validation.sh:YAML Validation"
    "broken_links.sh:Broken Links"
    "orphan_detection.sh:Orphan Detection"
    "stub_detection.sh:Stub Detection"
    "naming_validation.sh:Naming Validation"
    "inventory.sh:Inventory"
)

# Run each tool and collect results
declare -a TOOL_NAMES=()
declare -a TOOL_EXITS=()
declare -a TOOL_REPORTS=()
overall_exit=0

echo "════════════════════════════════════════════════════════"
echo " Vault Health Check — $(date -u +%Y-%m-%dT%H:%M:%S)"
echo "════════════════════════════════════════════════════════"
echo ""

for tool_entry in "${TOOLS[@]}"; do
    tool_script="${tool_entry%%:*}"
    tool_name="${tool_entry##*:}"
    tool_path="${SCRIPT_DIR}/${tool_script}"

    TOOL_NAMES+=("$tool_name")

    if [[ ! -x "$tool_path" ]]; then
        echo "  ✗ ${tool_name}: script not executable or missing (${tool_script})"
        TOOL_EXITS+=(2)
        TOOL_REPORTS+=("—")
        overall_exit=2
        continue
    fi

    echo "  Running: ${tool_name}..."

    # Capture output
    set +e
    output=$("$tool_path" "${TOOL_ARGS[@]}" 2>&1)
    tool_exit=$?
    set -e

    TOOL_EXITS+=($tool_exit)

    # Extract report path from output
    report_path=$(echo "$output" | grep "^Report:" | sed 's/^Report: //' || true)
    TOOL_REPORTS+=("${report_path:-—}")

    # Update overall exit
    if [[ $tool_exit -eq 2 && $overall_exit -ne 2 ]]; then
        overall_exit=2
    elif [[ $tool_exit -eq 1 && $overall_exit -eq 0 ]]; then
        overall_exit=1
    fi

    # Show tool output (unless quiet)
    if [[ "$QUIET" != "true" && -n "$output" ]]; then
        echo "$output" | sed 's/^/    /'
        echo ""
    fi
done

# Produce aggregate health report
health_report="${OUT_DIR}/vault_health_report.md"
overall_result="CLEAN"
[[ $overall_exit -eq 1 ]] && overall_result="FINDINGS"
[[ $overall_exit -eq 2 ]] && overall_result="ERROR"

# Determine vault root for report header
vault_display="$VAULT_ROOT_ARG"
if [[ -z "$vault_display" && -n "$CONFIG_FILE" ]]; then
    vault_display=$(grep '^vault_root:' "$CONFIG_FILE" 2>/dev/null | sed 's/vault_root:[[:space:]]*"\?\([^"]*\)"\?/\1/' || true)
fi

{
    echo "# Vault Health Report"
    echo ""
    echo "**Vault:** ${vault_display}"
    echo "**Date:** $(date -u +%Y-%m-%dT%H:%M:%S)"
    echo "**Result:** ${overall_result}"
    echo ""
    echo "## Tool Summary"
    echo ""
    echo "| Tool | Exit Code | Result | Report |"
    echo "|------|-----------|--------|--------|"

    for i in "${!TOOL_NAMES[@]}"; do
        exit_code="${TOOL_EXITS[$i]}"
        case $exit_code in
            0) result="CLEAN" ;;
            1) result="FINDINGS" ;;
            2) result="ERROR" ;;
            *) result="UNKNOWN" ;;
        esac
        report="${TOOL_REPORTS[$i]}"
        [[ "$report" != "—" ]] && report="$(basename "$report")"
        echo "| ${TOOL_NAMES[$i]} | ${exit_code} | ${result} | ${report} |"
    done

    echo ""
    echo "## Combined Findings"
    echo ""

    any_findings=false
    for i in "${!TOOL_NAMES[@]}"; do
        report="${TOOL_REPORTS[$i]}"
        if [[ "$report" != "—" && -f "$report" ]]; then
            # Extract findings section
            findings=$(sed -n '/^## Findings$/,/^## /{ /^## Findings$/d; /^## /d; p; }' "$report" 2>/dev/null || true)
            if [[ -n "$findings" ]]; then
                any_findings=true
                echo "### ${TOOL_NAMES[$i]}"
                echo ""
                echo "$findings"
                echo ""
            fi
        fi
    done

    if [[ "$any_findings" == false ]]; then
        echo "No findings across all tools."
        echo ""
    fi

    echo "## Combined Warnings"
    echo ""

    any_warnings=false
    for i in "${!TOOL_NAMES[@]}"; do
        report="${TOOL_REPORTS[$i]}"
        if [[ "$report" != "—" && -f "$report" ]]; then
            warnings=$(sed -n '/^## Warnings/,/^## /{ /^## Warnings/d; /^## /d; p; }' "$report" 2>/dev/null || true)
            if [[ -n "$warnings" ]]; then
                any_warnings=true
                echo "### ${TOOL_NAMES[$i]}"
                echo ""
                echo "$warnings"
                echo ""
            fi
        fi
    done

    if [[ "$any_warnings" == false ]]; then
        echo "No warnings across all tools."
        echo ""
    fi

} > "$health_report"

echo "════════════════════════════════════════════════════════"
echo " Overall: ${overall_result}"
echo " Report: ${health_report}"
echo "════════════════════════════════════════════════════════"

exit $overall_exit
