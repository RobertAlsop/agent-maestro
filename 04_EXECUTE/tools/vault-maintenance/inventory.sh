#!/usr/bin/env bash
# inventory.sh — Generate a machine-readable manifest of all vault files.
# Reports: file path, folder, type, status, authority_weight, inbound/outbound link counts.
# Enforces Vault Rules 21–23 (SYSTEM_MAP support).
#
# Exit codes: 0 = clean (always — this is a reporting tool), 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Inventory"

init_tmp_dir
OUTBOUND_FILE="${TOOL_TMPDIR}/outbound.txt"
INBOUND_FILE="${TOOL_TMPDIR}/inbound.txt"

# First pass: count outbound and register inbound targets
> "$OUTBOUND_FILE"
> "$INBOUND_FILE"

while IFS= read -r file; do
    basename_noext="$(basename "$file" .md)"
    outbound=0

    # Count all [[wiki-links]]
    links="$(grep -oE '\[\[[^]]+\]\]' "$file" 2>/dev/null || true)"
    if [[ -n "$links" ]]; then
        while IFS= read -r match; do
            target="$(echo "$match" | sed 's/^\[\[//;s/\]\]$//')"
            target="${target%%|*}"
            target="${target%%#*}"
            target="$(echo "$target" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
            if [[ -n "$target" ]]; then
                outbound=$((outbound + 1))
                echo "$target" >> "$INBOUND_FILE"
            fi
        done <<< "$links"
    fi

    echo "${basename_noext}	${outbound}" >> "$OUTBOUND_FILE"
done < <(get_vault_files)

# Sort and count inbound links
INBOUND_COUNTED="${TOOL_TMPDIR}/inbound_counted.txt"
sort "$INBOUND_FILE" | uniq -c | awk '{print $2"\t"$1}' > "$INBOUND_COUNTED"

# Generate inventory report
report_file="${OUTPUT_DIR}/Inventory_report.md"
total_files=0
TYPE_COUNTS_FILE="${TOOL_TMPDIR}/type_counts.txt"
> "$TYPE_COUNTS_FILE"

{
    echo "# Inventory Report"
    echo ""
    echo "**Vault:** ${VAULT_ROOT}"
    echo "**Date:** $(date -u +%Y-%m-%dT%H:%M:%S)"
    echo "**Result:** CLEAN"
    echo ""
    echo "## Manifest"
    echo ""
    echo "| File | Folder | Type | Status | AW | Inbound | Outbound |"
    echo "|------|--------|------|--------|----|---------|----------|"

    while IFS= read -r file; do
        total_files=$((total_files + 1))
        rel_path="${file#$VAULT_ROOT/}"
        folder="$(dirname "$rel_path")"
        [[ "$folder" == "." ]] && folder="(root)"
        basename_noext="$(basename "$file" .md)"

        # Extract frontmatter fields
        note_type=""
        note_status=""
        note_aw=""
        in_frontmatter=false
        while IFS= read -r line; do
            if [[ "$line" == "---" ]]; then
                if [[ "$in_frontmatter" == true ]]; then break; fi
                in_frontmatter=true
                continue
            fi
            if [[ "$in_frontmatter" == true ]]; then
                if [[ "$line" =~ ^type:[[:space:]]*\"?([^\"]*)\"? ]]; then
                    note_type="${BASH_REMATCH[1]}"
                    note_type="${note_type%\"}"
                fi
                if [[ "$line" =~ ^status:[[:space:]]*\"?([^\"]*)\"? ]]; then
                    note_status="${BASH_REMATCH[1]}"
                    note_status="${note_status%\"}"
                fi
                if [[ "$line" =~ ^authority_weight:[[:space:]]*([0-9]+) ]]; then
                    note_aw="${BASH_REMATCH[1]}"
                fi
            fi
        done < "$file"

        [[ -z "$note_type" ]] && note_type="—"
        [[ -z "$note_status" ]] && note_status="—"
        [[ -z "$note_aw" ]] && note_aw="—"

        # Look up link counts
        inbound="$(grep -F "${basename_noext}	" "$INBOUND_COUNTED" 2>/dev/null | head -1 | cut -f2 || true)"
        [[ -z "$inbound" ]] && inbound="0"
        outbound="$(grep -F "${basename_noext}	" "$OUTBOUND_FILE" 2>/dev/null | head -1 | cut -f2 || true)"
        [[ -z "$outbound" ]] && outbound="0"

        echo "| ${rel_path} | ${folder} | ${note_type} | ${note_status} | ${note_aw} | ${inbound} | ${outbound} |"

        if [[ "$note_type" != "—" ]]; then
            echo "$note_type" >> "$TYPE_COUNTS_FILE"
        fi

        mark_checked
        mark_passed
    done < <(get_vault_files)

    echo ""
    echo "## Summary"
    echo ""
    echo "**Total files:** ${total_files}"
    echo ""
    echo "| Type | Count |"
    echo "|------|-------|"
    if [[ -s "$TYPE_COUNTS_FILE" ]]; then
        sort "$TYPE_COUNTS_FILE" | uniq -c | sort -rn | awk '{print "| "$2" | "$1" |"}'
    fi
    echo ""

} > "$report_file"

if [[ "$QUIET" != true ]]; then
    echo "Inventory: CLEAN (${REPORT_CHECKED} files inventoried)"
    echo "Report: ${report_file}"
fi

exit 0
