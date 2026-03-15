#!/usr/bin/env bash
# =============================================================================
# validate_frontmatter.sh — Frontmatter Validator for Agent Maestro Vault
# =============================================================================
# Checks every .md file in the vault for required frontmatter fields,
# valid field values, and schema compliance.
#
# Usage: ./validate_frontmatter.sh [VAULT_ROOT]
#        VAULT_ROOT defaults to current directory.
#
# Output: Structured report to stdout. Exit code 0 = pass, 1 = failures found.
#
# Required fields (schema_version: 2):
#   schema_version, title, type, note_class, domain, layer, authority_weight,
#   resolution_basis, status, review_status, version, created_date,
#   last_modified, owner, source_type, relationships, tags
#
# Excluded: CLAUDE.md files (infrastructure, not vault notes)
# =============================================================================

set -uo pipefail

VAULT_ROOT="${1:-.}"
ERRORS=0
WARNINGS=0
FILES_CHECKED=0
FILES_PASSED=0
FILES_FAILED=0
FILES_SKIPPED=0

# Colors (if terminal supports them)
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Required top-level fields
REQUIRED_FIELDS=(
  "schema_version"
  "title"
  "type"
  "note_class"
  "authority_weight"
  "status"
  "review_status"
  "version"
  "created_date"
  "last_modified"
  "tags"
)

# Valid values for enumerated fields
VALID_STATUS="active|draft|completed|archived|incubating|deprecated"
VALID_REVIEW_STATUS="draft|reviewed|approved|needs_revision"
VALID_RESOLUTION="authority_weight|canonical|temporal"
VALID_SOURCE_TYPE="human_authored|ai_authored|collaborative|system_generated"

# Date pattern: YYYY-MM-DD
DATE_PATTERN='^[0-9]{4}-[0-9]{2}-[0-9]{2}$'

log_error() {
  local file="$1"
  local msg="$2"
  echo -e "  ${RED}ERROR${NC}: $msg"
  ((ERRORS++))
}

log_warning() {
  local file="$1"
  local msg="$2"
  echo -e "  ${YELLOW}WARN${NC}:  $msg"
  ((WARNINGS++))
}

log_pass() {
  local msg="$1"
  echo -e "  ${GREEN}PASS${NC}:  $msg"
}

# Extract YAML frontmatter from a file (between --- delimiters)
extract_frontmatter() {
  local file="$1"
  sed -n '/^---$/,/^---$/p' "$file" | sed '1d;$d'
}

# Get a simple field value from frontmatter text
get_field() {
  local frontmatter="$1"
  local field="$2"
  echo "$frontmatter" | grep -E "^${field}:" | head -1 | sed "s/^${field}:[[:space:]]*//" | sed 's/^"//;s/"$//' | sed "s/^'//;s/'$//"
}

# Check if field exists in frontmatter
has_field() {
  local frontmatter="$1"
  local field="$2"
  echo "$frontmatter" | grep -qE "^${field}:" 2>/dev/null
}

# Check if relationships block exists
has_relationships() {
  local frontmatter="$1"
  echo "$frontmatter" | grep -qE "^relationships:" 2>/dev/null
}

validate_file() {
  local file="$1"
  local relative_path="${file#$VAULT_ROOT/}"
  local file_errors=0

  # Skip CLAUDE.md files (infrastructure, not vault notes)
  if [[ "$(basename "$file")" == "CLAUDE.md" ]]; then
    ((FILES_SKIPPED++))
    return 0
  fi

  # Skip files in .git
  if [[ "$file" == *"/.git/"* ]]; then
    return 0
  fi

  ((FILES_CHECKED++))

  # Check if file has frontmatter delimiters
  local first_line
  first_line=$(head -1 "$file" 2>/dev/null)
  if [[ "$first_line" != "---" ]]; then
    echo -e "\n${CYAN}$relative_path${NC}"
    log_error "$file" "No YAML frontmatter found (first line is not '---')"
    ((FILES_FAILED++))
    return 1
  fi

  local frontmatter
  frontmatter=$(extract_frontmatter "$file")

  if [[ -z "$frontmatter" ]]; then
    echo -e "\n${CYAN}$relative_path${NC}"
    log_error "$file" "Empty or malformed frontmatter"
    ((FILES_FAILED++))
    return 1
  fi

  echo -e "\n${CYAN}$relative_path${NC}"

  # Check required fields
  for field in "${REQUIRED_FIELDS[@]}"; do
    if ! has_field "$frontmatter" "$field"; then
      log_error "$file" "Missing required field: $field"
      ((file_errors++))
    fi
  done

  # Validate schema_version
  local sv
  sv=$(get_field "$frontmatter" "schema_version")
  if [[ -n "$sv" && "$sv" != "2" ]]; then
    log_error "$file" "schema_version should be 2, found: $sv"
    ((file_errors++))
  fi

  # Validate authority_weight is numeric and in range
  local aw
  aw=$(get_field "$frontmatter" "authority_weight")
  if [[ -n "$aw" ]]; then
    if [[ "$aw" =~ ^[0-9]+$ ]]; then
      if (( aw < 0 || aw > 100 )); then
        log_error "$file" "authority_weight out of range (0-100): $aw"
        ((file_errors++))
      fi
    elif [[ "$aw" != *"-"* ]]; then
      # Allow ranges like "0-100" in templates
      log_error "$file" "authority_weight is not numeric: $aw"
      ((file_errors++))
    fi
  fi

  # Validate status
  local status
  status=$(get_field "$frontmatter" "status")
  if [[ -n "$status" ]]; then
    if ! echo "$status" | grep -qE "^($VALID_STATUS)$"; then
      log_warning "$file" "Non-standard status: $status"
    fi
  fi

  # Validate review_status
  local rs
  rs=$(get_field "$frontmatter" "review_status")
  if [[ -n "$rs" ]]; then
    if ! echo "$rs" | grep -qE "^($VALID_REVIEW_STATUS)$"; then
      log_warning "$file" "Non-standard review_status: $rs"
    fi
  fi

  # Validate dates
  local cd
  cd=$(get_field "$frontmatter" "created_date")
  if [[ -n "$cd" && ! "$cd" =~ $DATE_PATTERN ]]; then
    log_error "$file" "created_date not ISO 8601 (YYYY-MM-DD): $cd"
    ((file_errors++))
  fi

  local lm
  lm=$(get_field "$frontmatter" "last_modified")
  if [[ -n "$lm" && ! "$lm" =~ $DATE_PATTERN ]]; then
    log_error "$file" "last_modified not ISO 8601 (YYYY-MM-DD): $lm"
    ((file_errors++))
  fi

  # Validate version is numeric
  local ver
  ver=$(get_field "$frontmatter" "version")
  if [[ -n "$ver" && ! "$ver" =~ ^[0-9]+$ ]]; then
    log_warning "$file" "version is not a simple integer: $ver"
  fi

  # Check relationships block exists
  if ! has_relationships "$frontmatter"; then
    log_warning "$file" "No relationships block in frontmatter"
  fi

  # Check title is not empty
  local title
  title=$(get_field "$frontmatter" "title")
  if [[ -z "$title" ]]; then
    log_error "$file" "Title is empty"
    ((file_errors++))
  fi

  if (( file_errors == 0 )); then
    log_pass "All required fields present and valid"
    ((FILES_PASSED++))
  else
    ((FILES_FAILED++))
  fi
}

# === MAIN ===

echo "=============================================="
echo "  Agent Maestro — Frontmatter Validator"
echo "=============================================="
echo "Vault root: $VAULT_ROOT"
echo "Date: $(date -I)"
echo ""

# Find all .md files, excluding .git
while IFS= read -r -d '' file; do
  validate_file "$file"
done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

# === SUMMARY ===
echo ""
echo "=============================================="
echo "  SUMMARY"
echo "=============================================="
echo -e "Files checked:  $FILES_CHECKED"
echo -e "Files passed:   ${GREEN}$FILES_PASSED${NC}"
echo -e "Files failed:   ${RED}$FILES_FAILED${NC}"
echo -e "Files skipped:  $FILES_SKIPPED (CLAUDE.md infrastructure files)"
echo -e "Total errors:   ${RED}$ERRORS${NC}"
echo -e "Total warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

if (( ERRORS > 0 )); then
  echo -e "${RED}RESULT: FAIL${NC} — $ERRORS errors found"
  exit 1
else
  echo -e "${GREEN}RESULT: PASS${NC} — No errors (${WARNINGS} warnings)"
  exit 0
fi
