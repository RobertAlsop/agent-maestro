#!/usr/bin/env bash
# stub_detection.sh — Detect empty files, placeholder-only content, and stubs.
# Enforces Vault Rule 7.
#
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Stub Detection"

# Placeholder patterns that indicate non-content
PLACEHOLDER_PATTERNS=(
    "^---$"       # Only frontmatter delimiters
    "TODO"
    "TBD"
    "PLACEHOLDER"
    "^\s*$"       # All whitespace
)

while IFS= read -r file; do
    mark_checked
    rel_path="${file#$VAULT_ROOT/}"

    # Skip structural files and stub-exempt folders (e.g. 01_CAPTURE)
    if is_structural_exemption "$file" || is_stub_exempt "$file"; then
        mark_passed
        continue
    fi

    # Check for empty files
    if [[ ! -s "$file" ]]; then
        add_finding "${rel_path}: empty file"
        continue
    fi

    # Read content, strip frontmatter
    content=$(sed -n '/^---$/,/^---$/!p' "$file" | sed '/^$/d')

    # If only frontmatter exists (no body content)
    if [[ -z "$content" ]]; then
        # Check if file has frontmatter at all
        if head -1 "$file" | grep -q '^---$'; then
            add_finding "${rel_path}: frontmatter only, no body content"
        else
            add_finding "${rel_path}: no meaningful content"
        fi
        continue
    fi

    # Check body length — if fewer than 2 non-empty lines after frontmatter, likely a stub
    line_count=$(echo "$content" | wc -l | tr -d ' ')
    if [[ "$line_count" -lt 2 ]]; then
        # Check if the content is just a heading
        if echo "$content" | grep -qE '^#+ ' && [[ "$line_count" -eq 1 ]]; then
            add_finding "${rel_path}: heading only, no substantive content"
            continue
        fi
    fi

    mark_passed
done < <(get_vault_files)

write_report
exit $?
