#!/usr/bin/env bash
# broken_links.sh — Validate all wiki-links resolve to existing files.
# Checks body [[wiki-links]] and frontmatter relationship entries.
# Flags concept/governance notes with zero body wiki-links.
# Enforces Vault Rules 15–19.
#
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "${SCRIPT_DIR}/lib/config.sh"

load_config "$@" || exit 2
init_report "Broken Links"

# Build a lookup file of all note titles (filename without .md).
# Uses get_index_files() to include ALL vault content (incl. archive, templates)
# so that links to excluded-from-scanning files still resolve correctly.
init_tmp_dir
NOTE_INDEX="${TOOL_TMPDIR}/note_index.txt"
while IFS= read -r file; do
    basename "$file" .md
done < <(get_index_files) > "$NOTE_INDEX"

resolve_link() {
    local target="$1"
    # Handle Obsidian escaped pipe in tables: \| is a display-text separator
    target="${target%%\\|*}"
    target="${target%%|*}"
    target="${target%%#*}"
    target="$(echo "$target" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    [[ -z "$target" ]] && return 1
    grep -qFx "$target" "$NOTE_INDEX" 2>/dev/null
}

extract_body_links() {
    local file="$1"
    local past_frontmatter=false
    local in_frontmatter=false

    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [[ "$in_frontmatter" == true ]]; then
                past_frontmatter=true
                continue
            fi
            in_frontmatter=true
            continue
        fi
        if [[ "$past_frontmatter" == true || "$in_frontmatter" == false ]]; then
            # Strip backtick-quoted content before extracting wiki-links
            local cleaned_line
            cleaned_line="$(echo "$line" | sed 's/`[^`]*`//g')"
            # Use grep to extract [[...]] patterns
            echo "$cleaned_line" | grep -oE '\[\[[^]]+\]\]' | sed 's/^\[\[//;s/\]\]$//' || true
        fi
    done < "$file"
}

extract_frontmatter_links() {
    local file="$1"
    local in_frontmatter=false
    local in_relationships=false

    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [[ "$in_frontmatter" == true ]]; then break; fi
            in_frontmatter=true
            continue
        fi
        if [[ "$in_frontmatter" == true ]]; then
            if [[ "$line" =~ ^relationships: ]]; then
                in_relationships=true
                continue
            fi
            if [[ "$in_relationships" == true ]] && echo "$line" | grep -qE '^[a-z]'; then
                in_relationships=false
                continue
            fi
            if [[ "$in_relationships" == true ]]; then
                # Extract [[...]] links
                echo "$line" | grep -oE '\[\[[^]]+\]\]' | sed 's/^\[\[//;s/\]\]$//' || true
                # Extract bare string entries
                if echo "$line" | grep -qE '^\s+-\s+"[^"]*"'; then
                    local val
                    val="$(echo "$line" | sed -n 's/.*- *"\([^"]*\)".*/\1/p')"
                    if [[ -n "$val" ]] && ! echo "$val" | grep -q '\[\['; then
                        echo "$val"
                    fi
                fi
            fi
        fi
    done < "$file"
}

get_note_type() {
    local file="$1"
    local in_frontmatter=false
    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [[ "$in_frontmatter" == true ]]; then break; fi
            in_frontmatter=true
            continue
        fi
        if [[ "$in_frontmatter" == true ]]; then
            if [[ "$line" =~ ^type:[[:space:]]*\"?([^\"]*)\"? ]]; then
                local val="${BASH_REMATCH[1]}"
                echo "${val%\"}"
                return
            fi
        fi
    done < "$file"
}

while IFS= read -r file; do
    mark_checked
    rel_path="${file#$VAULT_ROOT/}"

    if is_structural_exemption "$file"; then
        mark_passed
        continue
    fi

    local_findings=0

    # Check body wiki-links
    body_link_count=0
    while IFS= read -r link; do
        [[ -z "$link" ]] && continue
        body_link_count=$((body_link_count + 1))
        if ! resolve_link "$link"; then
            target="${link%%|*}"
            target="${target%%#*}"
            add_finding "${rel_path}: broken wiki-link [[${target}]]"
            local_findings=$((local_findings + 1))
        fi
    done < <(extract_body_links "$file")

    # Check frontmatter relationship links
    while IFS= read -r link; do
        [[ -z "$link" ]] && continue
        link="${link#\[\[}"
        link="${link%\]\]}"
        if ! resolve_link "$link"; then
            add_finding "${rel_path}: broken relationship link '${link}'"
            local_findings=$((local_findings + 1))
        fi
    done < <(extract_frontmatter_links "$file")

    # Check if concept/governance notes have at least one body wiki-link
    note_type="$(get_note_type "$file")"
    if [[ "$body_link_count" -eq 0 ]]; then
        for req_type in "${WIKI_LINK_REQUIRED_TYPES[@]}"; do
            if [[ "$note_type" == "$req_type" ]]; then
                add_finding "${rel_path}: ${note_type} note has zero body wiki-links"
                local_findings=$((local_findings + 1))
                break
            fi
        done
    fi

    [[ "$local_findings" -eq 0 ]] && mark_passed

done < <(get_vault_files)

write_report
exit $?
