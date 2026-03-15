#!/usr/bin/env bash
# =============================================================================
# check_link_integrity.sh — Wiki-Link Integrity Checker for Agent Maestro Vault
# =============================================================================
# Scans all .md files for [[wiki-links]] and verifies that each link resolves
# to an existing note in the vault.
#
# Usage: ./check_link_integrity.sh [VAULT_ROOT]
#        VAULT_ROOT defaults to current directory.
#
# Output: Structured report to stdout. Exit code 0 = pass, 1 = broken links.
#
# What it checks:
#   1. Every [[Target]] in body text resolves to a file named "Target.md"
#   2. Every [[Target]] in frontmatter relationships resolves similarly
#   3. Reports orphan links (links TO notes that don't exist)
#
# Excluded: CLAUDE.md files, .git directory
# =============================================================================

set -uo pipefail

VAULT_ROOT="${1:-.}"
BROKEN_LINKS=0
TOTAL_LINKS=0
FILES_WITH_BROKEN=0
FILES_CHECKED=0

# Colors
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

# Build an index of all note titles (filename without .md extension)
declare -A NOTE_INDEX

build_index() {
  while IFS= read -r -d '' file; do
    local basename
    basename=$(basename "$file" .md)
    NOTE_INDEX["$basename"]=1
  done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -print0)
}

# Extract all [[wiki-links]] from a file
extract_links() {
  local file="$1"
  # Match [[anything]] patterns, extracting the content between brackets
  grep -oP '\[\[([^\]]+)\]\]' "$file" 2>/dev/null | sed 's/\[\[//;s/\]\]//' | sort -u
}

check_file() {
  local file="$1"
  local relative_path="${file#$VAULT_ROOT/}"

  # Skip CLAUDE.md and .git
  if [[ "$(basename "$file")" == "CLAUDE.md" ]]; then
    return 0
  fi

  ((FILES_CHECKED++))

  local links
  links=$(extract_links "$file")

  if [[ -z "$links" ]]; then
    return 0
  fi

  local file_broken=0
  local file_header_printed=0

  while IFS= read -r link; do
    [[ -z "$link" ]] && continue
    ((TOTAL_LINKS++))

    # Handle links with aliases: [[Target|Display Text]] → check Target
    local target
    target=$(echo "$link" | cut -d'|' -f1)

    # Handle links with headings: [[Target#heading]] → check Target
    target=$(echo "$target" | cut -d'#' -f1)

    # Trim whitespace
    target=$(echo "$target" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

    if [[ -z "$target" ]]; then
      continue
    fi

    # Check if target exists in note index
    if [[ -z "${NOTE_INDEX[$target]+x}" ]]; then
      if (( file_header_printed == 0 )); then
        echo -e "\n${CYAN}$relative_path${NC}"
        file_header_printed=1
      fi
      echo -e "  ${RED}BROKEN${NC}: [[$link]] → no file named '$target.md'"
      ((BROKEN_LINKS++))
      ((file_broken++))
    fi
  done <<< "$links"

  if (( file_broken > 0 )); then
    ((FILES_WITH_BROKEN++))
  fi
}

# === MAIN ===

echo "=============================================="
echo "  Agent Maestro — Link Integrity Checker"
echo "=============================================="
echo "Vault root: $VAULT_ROOT"
echo "Date: $(date -I)"
echo ""
echo "Building note index..."

build_index

echo "Index built: ${#NOTE_INDEX[@]} notes indexed"
echo ""
echo "Scanning for wiki-links..."

while IFS= read -r -d '' file; do
  check_file "$file"
done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

# === SUMMARY ===
echo ""
echo "=============================================="
echo "  SUMMARY"
echo "=============================================="
echo -e "Files checked:       $FILES_CHECKED"
echo -e "Total wiki-links:    $TOTAL_LINKS"
echo -e "Broken links:        ${RED}$BROKEN_LINKS${NC}"
echo -e "Files with broken:   ${RED}$FILES_WITH_BROKEN${NC}"
echo ""

if (( BROKEN_LINKS > 0 )); then
  echo -e "${RED}RESULT: FAIL${NC} — $BROKEN_LINKS broken links in $FILES_WITH_BROKEN files"
  exit 1
else
  echo -e "${GREEN}RESULT: PASS${NC} — All $TOTAL_LINKS links resolve"
  exit 0
fi
