#!/usr/bin/env bash
# =============================================================================
# migrate_frontmatter.sh — Batch Frontmatter Migration for Agent Maestro Vault
# =============================================================================
# Migrates legacy frontmatter fields to schema_version: 2 format.
#
# Usage: ./migrate_frontmatter.sh [VAULT_ROOT] [--dry-run]
#        VAULT_ROOT defaults to current directory.
#        --dry-run shows what would change without modifying files.
#
# Migrations performed:
#   1. Rename created: → created_date: (if created_date not already present)
#   2. Rename updated: → last_modified: (if last_modified not already present)
#   3. Add title: from filename (if missing)
#   4. Remove legacy fields: id:, scope:, last_reviewed:, review_cycle:,
#      map:, maps:, related:, related_maps:, related_pipes:
#
# Excluded: CLAUDE.md files, .git directory, 99_ARCHIVE/
# =============================================================================

set -uo pipefail

VAULT_ROOT="${1:-.}"
DRY_RUN=false
if [[ "${2:-}" == "--dry-run" ]]; then
  DRY_RUN=true
fi

MIGRATED=0
SKIPPED=0
ERRORS=0

RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

# Legacy fields to remove (top-level only)
LEGACY_FIELDS=(
  "^id:"
  "^scope:"
  "^last_reviewed:"
  "^review_cycle:"
  "^map:"
  "^maps:"
  "^related:"
  "^related_maps:"
  "^related_pipes:"
)

migrate_file() {
  local file="$1"
  local relative_path="${file#$VAULT_ROOT/}"
  local basename_noext
  basename_noext=$(basename "$file" .md)

  # Skip CLAUDE.md
  if [[ "$basename_noext" == "CLAUDE" ]]; then
    return 0
  fi

  # Skip archive
  if [[ "$relative_path" == 99_ARCHIVE/* ]]; then
    return 0
  fi

  # Check for frontmatter
  local first_line
  first_line=$(head -1 "$file" 2>/dev/null)
  if [[ "$first_line" != "---" ]]; then
    return 0
  fi

  local changes=0
  local tmpfile
  tmpfile=$(mktemp)

  cp "$file" "$tmpfile"

  # 1. Add title if missing
  if ! grep -q "^title:" "$tmpfile" 2>/dev/null; then
    # Insert title after schema_version line, or after first ---
    if grep -q "^schema_version:" "$tmpfile"; then
      sed -i "/^schema_version:/a title: \"$basename_noext\"" "$tmpfile"
    else
      sed -i "0,/^---$/!{0,/^---$/!b; s/^---$/---\ntitle: \"$basename_noext\"/}" "$tmpfile"
      # Simpler: just add after first line
      sed -i "2i title: \"$basename_noext\"" "$tmpfile"
    fi
    ((changes++))
    if $DRY_RUN; then
      echo -e "  ${GREEN}+title${NC}: \"$basename_noext\""
    fi
  fi

  # 2. Rename created: → created_date:
  if grep -q "^created:" "$tmpfile" && ! grep -q "^created_date:" "$tmpfile"; then
    sed -i 's/^created:/created_date:/' "$tmpfile"
    ((changes++))
    if $DRY_RUN; then
      echo -e "  ${GREEN}rename${NC}: created: → created_date:"
    fi
  fi

  # 3. Rename updated: → last_modified:
  if grep -q "^updated:" "$tmpfile" && ! grep -q "^last_modified:" "$tmpfile"; then
    sed -i 's/^updated:/last_modified:/' "$tmpfile"
    ((changes++))
    if $DRY_RUN; then
      echo -e "  ${GREEN}rename${NC}: updated: → last_modified:"
    fi
  fi

  # 4. Remove legacy fields
  for pattern in "${LEGACY_FIELDS[@]}"; do
    if grep -q "$pattern" "$tmpfile" 2>/dev/null; then
      # For array fields (maps:, related:, etc.), also remove following indented lines
      local field_name
      field_name=$(echo "$pattern" | sed 's/\^//' | sed 's/://')

      # Simple removal for single-line fields
      sed -i "/$pattern/d" "$tmpfile"
      ((changes++))
      if $DRY_RUN; then
        echo -e "  ${RED}-remove${NC}: $field_name"
      fi
    fi
  done

  # 5. Clean up null values → empty or remove
  sed -i 's/: null$/: ""/' "$tmpfile"

  if (( changes > 0 )); then
    if $DRY_RUN; then
      echo -e "${CYAN}$relative_path${NC}: $changes changes (dry run)"
    else
      cp "$tmpfile" "$file"
      echo -e "${CYAN}$relative_path${NC}: $changes changes applied"
    fi
    ((MIGRATED++))
  fi

  rm -f "$tmpfile"
}

# === MAIN ===

echo "=============================================="
echo "  Agent Maestro — Frontmatter Migration"
echo "=============================================="
echo "Vault root: $VAULT_ROOT"
echo "Mode: $( $DRY_RUN && echo 'DRY RUN' || echo 'LIVE' )"
echo "Date: $(date -I)"
echo ""

while IFS= read -r -d '' file; do
  migrate_file "$file"
done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

echo ""
echo "=============================================="
echo "  SUMMARY"
echo "=============================================="
echo -e "Files migrated: ${GREEN}$MIGRATED${NC}"
echo -e "Mode: $( $DRY_RUN && echo 'DRY RUN — no files were modified' || echo 'LIVE — changes applied' )"
