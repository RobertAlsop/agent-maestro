#!/usr/bin/env bash
# naming_validation.sh — Check for duplicate filenames, duplicate titles, and title-filename mismatches.
# Enforces Vault Rule 34 and implied uniqueness.
#
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Naming Validation"

init_tmp_dir
FILENAMES_FILE="${TOOL_TMPDIR}/filenames.txt"
TITLES_FILE="${TOOL_TMPDIR}/titles.txt"

> "$FILENAMES_FILE"
> "$TITLES_FILE"

while IFS= read -r file; do
    mark_checked
    rel_path="${file#$VAULT_ROOT/}"
    basename_full="$(basename "$file")"
    basename_noext="$(basename "$file" .md)"

    skip_title=false
    if is_structural_exemption "$file"; then
        skip_title=true
    fi

    # Check duplicate filenames (skip structural exemptions like CLAUDE.md)
    existing="$(grep -F "	${basename_full}	" "$FILENAMES_FILE" 2>/dev/null | head -1 || true)"
    if [[ -n "$existing" && "$skip_title" == false ]]; then
        prev_path="$(echo "$existing" | cut -f1)"
        add_finding "${rel_path}: duplicate filename (also at ${prev_path})"
    fi
    printf '%s\t%s\t\n' "$rel_path" "$basename_full" >> "$FILENAMES_FILE"

    # Extract and check title
    if [[ "$skip_title" == false ]]; then
        title=""
        in_frontmatter=false
        while IFS= read -r line; do
            if [[ "$line" == "---" ]]; then
                if [[ "$in_frontmatter" == true ]]; then break; fi
                in_frontmatter=true
                continue
            fi
            if [[ "$in_frontmatter" == true ]]; then
                if [[ "$line" =~ ^title:[[:space:]]*\"(.*)\" ]]; then
                    title="${BASH_REMATCH[1]}"
                    break
                elif [[ "$line" =~ ^title:[[:space:]]*(.+) ]]; then
                    title="${BASH_REMATCH[1]}"
                    break
                fi
            fi
        done < "$file"

        if [[ -n "$title" ]]; then
            # Check duplicate titles
            existing_title="$(grep -F "	${title}	" "$TITLES_FILE" 2>/dev/null | head -1 || true)"
            if [[ -n "$existing_title" ]]; then
                prev_path="$(echo "$existing_title" | cut -f1)"
                add_finding "${rel_path}: duplicate title '${title}' (also in ${prev_path})"
            fi
            printf '%s\t%s\t\n' "$rel_path" "$title" >> "$TITLES_FILE"

            # Check title matches filename
            if [[ "$title" != "$basename_noext" ]]; then
                add_finding "${rel_path}: title '${title}' does not match filename '${basename_noext}'"
            else
                mark_passed
            fi
        else
            if is_frontmatter_optional "$file"; then
                mark_passed
            else
                mark_passed
            fi
        fi
    else
        mark_passed
    fi

done < <(get_vault_files)

write_report
exit $?
