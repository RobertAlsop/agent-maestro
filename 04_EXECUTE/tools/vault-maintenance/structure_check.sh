#!/usr/bin/env bash
# structure_check.sh — Verify vault skeleton: required folders, root files, pipeline CLAUDE.md files.
# Enforces Vault Rules 1–4, 57.
#
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Structure Check"

# Check required folders
for folder in "${REQUIRED_FOLDERS[@]}"; do
    mark_checked
    if [[ -d "${VAULT_ROOT}/${folder}" ]]; then
        mark_passed
    else
        add_finding "Missing required folder: ${folder}"
    fi
done

# Check required root files
for file in "${REQUIRED_ROOT_FILES[@]}"; do
    mark_checked
    if [[ -f "${VAULT_ROOT}/${file}" ]]; then
        mark_passed
    else
        add_finding "Missing required root file: ${file}"
    fi
done

# Check required pipeline CLAUDE.md files
for claude_md in "${REQUIRED_CLAUDE_MD[@]}"; do
    mark_checked
    local_path="${VAULT_ROOT}/${claude_md}"
    if [[ ! -f "$local_path" ]]; then
        add_finding "Missing pipeline CLAUDE.md: ${claude_md}"
    elif [[ ! -s "$local_path" ]]; then
        add_finding "Empty pipeline CLAUDE.md: ${claude_md}"
    else
        mark_passed
    fi
done

write_report
exit $?
