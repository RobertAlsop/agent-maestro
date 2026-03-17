#!/usr/bin/env bash
# orphan_detection.sh — Detect files with no inbound links from any other file.
# Enforces Vault Rule 20.
#
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Orphan Detection"

init_tmp_dir
INBOUND_FILE="${TOOL_TMPDIR}/inbound_targets.txt"
NOTES_FILE="${TOOL_TMPDIR}/all_notes.txt"

# Collect all non-exempt note basenames and their paths
> "$NOTES_FILE"
while IFS= read -r file; do
    if ! is_structural_exemption "$file"; then
        rel_path="${file#$VAULT_ROOT/}"
        basename_noext="$(basename "$file" .md)"
        echo "${basename_noext}	${rel_path}" >> "$NOTES_FILE"
    fi
done < <(get_vault_files)

# Scan ALL files (incl. archive, templates) for outbound links.
# Uses get_index_files() so that links FROM excluded content still count
# as inbound links for their targets.
> "$INBOUND_FILE"
while IFS= read -r file; do
    # Extract all [[wiki-links]] from entire file
    grep -oE '\[\[[^]]+\]\]' "$file" 2>/dev/null | sed 's/^\[\[//;s/\]\]$//' | while IFS= read -r link; do
        target="${link%%|*}"
        target="${target%%#*}"
        target="$(echo "$target" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        [[ -n "$target" ]] && echo "$target"
    done || true

    # Also extract bare string entries from frontmatter relationships
    in_fm=false
    in_rels=false
    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [[ "$in_fm" == true ]]; then break; fi
            in_fm=true
            continue
        fi
        if [[ "$in_fm" == true ]]; then
            if [[ "$line" =~ ^relationships: ]]; then in_rels=true; continue; fi
            if [[ "$in_rels" == true ]] && echo "$line" | grep -qE '^[a-z]'; then break; fi
            if [[ "$in_rels" == true ]]; then
                if echo "$line" | grep -qE '^\s+-\s+"[^"]*"'; then
                    val="$(echo "$line" | sed -n 's/.*- *"\([^"]*\)".*/\1/p')"
                    if [[ -n "$val" ]]; then
                        val="${val#\[\[}"
                        val="${val%\]\]}"
                        echo "$val"
                    fi
                fi
            fi
        fi
    done < "$file"
done < <(get_index_files) | sort -u > "$INBOUND_FILE"

# Check each note for inbound links
while IFS=$'\t' read -r basename rel_path; do
    mark_checked
    # Skip files in orphan-exempt folders (leaf artifacts like logs and reports)
    if is_orphan_exempt "${VAULT_ROOT}/${rel_path}"; then
        mark_passed
        continue
    fi
    if grep -qFx "$basename" "$INBOUND_FILE" 2>/dev/null; then
        mark_passed
    else
        add_finding "${rel_path}: orphan — no inbound links from any other file"
    fi
done < "$NOTES_FILE"

write_report
exit $?
