#!/usr/bin/env bash
# config.sh — Shared config-parsing library for vault-maintenance tools.
# Compatible with bash 3.2+ (macOS default).
#
# Sources into each tool via: source "$(dirname "$0")/lib/config.sh"

set -euo pipefail

# --- Globals set by load_config ---
VAULT_ROOT=""
OUTPUT_DIR=""
EXCLUDE_PATTERNS=()
REQUIRED_FOLDERS=()
REQUIRED_ROOT_FILES=()
REQUIRED_CLAUDE_MD=()
FRONTMATTER_OPTIONAL_FOLDERS=()
REQUIRED_FIELDS=()
STRUCTURAL_EXEMPTIONS=()
WIKI_LINK_REQUIRED_TYPES=()
AW_MIN=0
AW_MAX=100
QUIET=false
STRICT=false

# Controlled vocabulary stored as pipe-delimited strings
# e.g., CV_type="governance|concept|skill|..."
# Checked via: echo "|${CV_type}|" | grep -q "|${value}|"

# --- Config Parsing ---

parse_config_file() {
    local file="$1"
    [[ -f "$file" ]] || return 0

    local current_list=""
    local in_nested_map=""
    local nested_map_key=""

    while IFS= read -r line || [[ -n "$line" ]]; do
        # Skip comments and blank lines
        [[ "$line" =~ ^[[:space:]]*# ]] && continue
        [[ "$line" =~ ^[[:space:]]*$ ]] && continue

        # Detect list item (  - "value" or   - value)
        if [[ "$line" =~ ^[[:space:]]+-[[:space:]]+\"?([^\"]*)\"?[[:space:]]*$ ]]; then
            local val="${BASH_REMATCH[1]}"
            if [[ -n "$in_nested_map" && -n "$nested_map_key" ]]; then
                local varname="CV_${nested_map_key}"
                local existing="${!varname:-}"
                if [[ -n "$existing" ]]; then
                    eval "${varname}=\"${existing}|${val}\""
                else
                    eval "${varname}=\"${val}\""
                fi
            elif [[ -n "$current_list" ]]; then
                eval "${current_list}+=(\"\$val\")"
            fi
            continue
        fi

        # Detect nested map key (e.g., "  type:" under controlled_vocabulary)
        if [[ -n "$in_nested_map" && "$line" =~ ^[[:space:]]+([a-z_]+):[[:space:]]*$ ]]; then
            nested_map_key="${BASH_REMATCH[1]}"
            continue
        fi

        # Detect top-level key
        if [[ "$line" =~ ^([a-z_]+):[[:space:]]*(.*) ]]; then
            local key="${BASH_REMATCH[1]}"
            local val="${BASH_REMATCH[2]}"
            in_nested_map=""
            nested_map_key=""
            current_list=""

            val="${val#\"}"
            val="${val%\"}"

            case "$key" in
                vault_root)       VAULT_ROOT="$val" ;;
                output_dir)       OUTPUT_DIR="$val" ;;
                required_folders) current_list="REQUIRED_FOLDERS" ;;
                required_root_files) current_list="REQUIRED_ROOT_FILES" ;;
                required_claude_md) current_list="REQUIRED_CLAUDE_MD" ;;
                frontmatter_optional_folders) current_list="FRONTMATTER_OPTIONAL_FOLDERS" ;;
                required_fields)  current_list="REQUIRED_FIELDS" ;;
                structural_exemptions) current_list="STRUCTURAL_EXEMPTIONS" ;;
                wiki_link_required_types) current_list="WIKI_LINK_REQUIRED_TYPES" ;;
                exclude_patterns) current_list="EXCLUDE_PATTERNS" ;;
                controlled_vocabulary) in_nested_map="controlled_vocabulary" ;;
                authority_weight_range) in_nested_map="aw_range" ;;
            esac

            if [[ "$val" == "{}" || "$val" == "[]" ]]; then
                current_list=""
                in_nested_map=""
            fi
        fi

        # Handle nested min/max under authority_weight_range
        if [[ "$in_nested_map" == "aw_range" && "$line" =~ ^[[:space:]]+(min|max):[[:space:]]*([0-9]+) ]]; then
            local subkey="${BASH_REMATCH[1]}"
            local subval="${BASH_REMATCH[2]}"
            [[ "$subkey" == "min" ]] && AW_MIN="$subval"
            [[ "$subkey" == "max" ]] && AW_MAX="$subval"
        fi

    done < "$file"
}

# Load config: defaults first, then vault-specific, then CLI overrides.
load_config() {
    local config_file=""
    local cli_vault_root=""
    local cli_output_dir=""

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --config)    config_file="$2"; shift 2 ;;
            --vault-root) cli_vault_root="$2"; shift 2 ;;
            --output-dir) cli_output_dir="$2"; shift 2 ;;
            --quiet)     QUIET=true; shift ;;
            --strict)    STRICT=true; shift ;;
            *)           shift ;;
        esac
    done

    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[1]}")" && pwd)"
    local defaults_file="${script_dir}/config/defaults.conf"

    if [[ -f "$defaults_file" ]]; then
        parse_config_file "$defaults_file"
    fi

    if [[ -n "$config_file" && -f "$config_file" ]]; then
        parse_config_file "$config_file"
    fi

    [[ -n "$cli_vault_root" ]] && VAULT_ROOT="$cli_vault_root"
    [[ -n "$cli_output_dir" ]] && OUTPUT_DIR="$cli_output_dir"

    if [[ -z "$VAULT_ROOT" ]]; then
        echo "ERROR: vault_root not set. Use --vault-root or set in config." >&2
        return 2
    fi
    if [[ ! -d "$VAULT_ROOT" ]]; then
        echo "ERROR: vault_root does not exist: $VAULT_ROOT" >&2
        return 2
    fi

    if [[ "$OUTPUT_DIR" != /* ]]; then
        OUTPUT_DIR="${script_dir}/${OUTPUT_DIR}"
    fi
    mkdir -p "$OUTPUT_DIR"
}

# --- Report Helpers ---

REPORT_TOOL_NAME=""
REPORT_FINDINGS=()
REPORT_WARNINGS=()
REPORT_CHECKED=0
REPORT_PASSED=0
REPORT_FAILED=0
REPORT_WARNED=0

init_report() {
    REPORT_TOOL_NAME="$1"
    REPORT_FINDINGS=()
    REPORT_WARNINGS=()
    REPORT_CHECKED=0
    REPORT_PASSED=0
    REPORT_FAILED=0
    REPORT_WARNED=0
}

add_finding() {
    REPORT_FINDINGS+=("$1")
    REPORT_FAILED=$((REPORT_FAILED + 1))
}

add_warning() {
    REPORT_WARNINGS+=("$1")
    REPORT_WARNED=$((REPORT_WARNED + 1))
}

mark_passed() {
    REPORT_CHECKED=$((REPORT_CHECKED + 1))
    REPORT_PASSED=$((REPORT_PASSED + 1))
}

mark_checked() {
    REPORT_CHECKED=$((REPORT_CHECKED + 1))
}

write_report() {
    local report_file="${OUTPUT_DIR}/${REPORT_TOOL_NAME// /_}_report.md"
    local result="CLEAN"
    local exit_code=0

    if [[ ${#REPORT_FINDINGS[@]} -gt 0 ]]; then
        result="FINDINGS"
        exit_code=1
    fi

    {
        echo "# ${REPORT_TOOL_NAME} Report"
        echo ""
        echo "**Vault:** ${VAULT_ROOT}"
        echo "**Date:** $(date -u +%Y-%m-%dT%H:%M:%S)"
        echo "**Result:** ${result}"
        echo ""
        echo "## Summary"
        echo ""
        echo "| Checked | Passed | Failed | Warnings |"
        echo "|---------|--------|--------|----------|"
        echo "| ${REPORT_CHECKED} | ${REPORT_PASSED} | ${REPORT_FAILED} | ${REPORT_WARNED} |"
        echo ""

        if [[ ${#REPORT_FINDINGS[@]} -gt 0 ]]; then
            echo "## Findings"
            echo ""
            local f
            for f in "${REPORT_FINDINGS[@]}"; do
                echo "- ${f}"
            done
            echo ""
        fi

        if [[ ${#REPORT_WARNINGS[@]} -gt 0 ]]; then
            echo "## Warnings (uncertain)"
            echo ""
            local w
            for w in "${REPORT_WARNINGS[@]}"; do
                echo "- ${w}"
            done
            echo ""
        fi
    } > "$report_file"

    if [[ "$QUIET" != true ]]; then
        echo "${REPORT_TOOL_NAME}: ${result} (${REPORT_CHECKED} checked, ${REPORT_FAILED} findings, ${REPORT_WARNED} warnings)"
        echo "Report: ${report_file}"
    fi

    return $exit_code
}

# --- File Discovery ---

get_vault_files() {
    local find_cmd="find \"$VAULT_ROOT\" -name '*.md' -type f"
    local pattern
    for pattern in "${EXCLUDE_PATTERNS[@]}"; do
        find_cmd="${find_cmd} -not -path '*/${pattern}/*' -not -path '*/${pattern}'"
    done
    eval "$find_cmd" | sort
}

is_frontmatter_optional() {
    local file="$1"
    local rel_path="${file#$VAULT_ROOT/}"
    local folder
    for folder in "${FRONTMATTER_OPTIONAL_FOLDERS[@]}"; do
        if [[ "$rel_path" == "${folder}/"* ]]; then
            return 0
        fi
    done
    return 1
}

is_structural_exemption() {
    local file="$1"
    local bn
    bn="$(basename "$file")"
    local exempt
    for exempt in "${STRUCTURAL_EXEMPTIONS[@]}"; do
        if [[ "$bn" == "$exempt" ]]; then
            return 0
        fi
    done
    return 1
}

# --- Temp file helpers (for tools that need lookup tables) ---
# Each tool should call init_tmp_dir early (before any subshells),
# then use $TOOL_TMPDIR. Cleanup is registered once.

TOOL_TMPDIR=""

init_tmp_dir() {
    if [[ -z "$TOOL_TMPDIR" ]]; then
        TOOL_TMPDIR="$(mktemp -d)"
        # Use SIGINT/SIGTERM traps instead of EXIT to avoid subshell cleanup issues
        trap '_cleanup_tmpdir' INT TERM
    fi
}

_cleanup_tmpdir() {
    [[ -n "$TOOL_TMPDIR" && -d "$TOOL_TMPDIR" ]] && rm -rf "$TOOL_TMPDIR"
}

# Cleanup at end of script — call explicitly before exit
cleanup() {
    _cleanup_tmpdir
}
