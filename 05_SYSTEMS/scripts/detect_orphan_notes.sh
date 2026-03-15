#!/usr/bin/env bash
# =============================================================================
# detect_orphan_notes.sh — Orphan Note Detector for Agent Maestro Vault
# =============================================================================
# Identifies notes that are not linked to by any other note in the vault.
# An orphan note has no incoming wiki-links from any other file.
#
# Usage: ./detect_orphan_notes.sh [VAULT_ROOT]
#        VAULT_ROOT defaults to current directory.
#
# Output: Structured report to stdout. Exit code 0 = no orphans, 1 = orphans found.
#
# What it checks:
#   1. For every .md file, checks if any OTHER file contains a [[link]] to it
#   2. Reports notes with zero incoming links as orphans
#   3. Reports notes with only self-references
#
# Known exceptions (not flagged as orphans):
#   - CLAUDE.md files (infrastructure, not vault notes)
#   - Root-level files
#   - Files in 99_ARCHIVE/ (archived items may naturally be unlinked)
#
# Viability signal: Orphan notes are candidates for the Viability audit (Law 3).
# =============================================================================

set -uo pipefail

VAULT_ROOT="${1:-.}"
ORPHAN_COUNT=0
TOTAL_NOTES=0
LOW_LINK_COUNT=0

# Colors
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

# Build a reverse index: for each note, count how many OTHER files link to it
declare -A INCOMING_LINKS
declare -A NOTE_FILES
declare -A NOTE_AUTHORITY

# Index all notes
build_note_index() {
  while IFS= read -r -d '' file; do
    local basename
    basename=$(basename "$file" .md)

    # Skip CLAUDE.md
    if [[ "$basename" == "CLAUDE" ]]; then
      continue
    fi

    NOTE_FILES["$basename"]="$file"
    INCOMING_LINKS["$basename"]=0

    # Extract authority_weight for context
    local aw
    aw=$(grep -E "^authority_weight:" "$file" 2>/dev/null | head -1 | sed 's/authority_weight:[[:space:]]*//' | sed 's/"//g' | tr -d ' ')
    NOTE_AUTHORITY["$basename"]="${aw:-unknown}"

    ((TOTAL_NOTES++))
  done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -not -name "CLAUDE.md" -print0)
}

# Scan all files and count incoming links for each note
count_incoming_links() {
  while IFS= read -r -d '' file; do
    local source_basename
    source_basename=$(basename "$file" .md)

    # Extract all wiki-link targets from this file
    local targets
    targets=$(grep -oP '\[\[([^\]|#]+)' "$file" 2>/dev/null | sed 's/\[\[//' | sort -u)

    while IFS= read -r target; do
      [[ -z "$target" ]] && continue
      target=$(echo "$target" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

      # Only count links from OTHER files (not self-references)
      if [[ "$target" != "$source_basename" && -n "${INCOMING_LINKS[$target]+x}" ]]; then
        INCOMING_LINKS["$target"]=$(( ${INCOMING_LINKS[$target]} + 1 ))
      fi
    done <<< "$targets"
  done < <(find "$VAULT_ROOT" -type f -name "*.md" -not -path "*/.git/*" -print0)
}

# === MAIN ===

echo "=============================================="
echo "  Agent Maestro — Orphan Note Detector"
echo "=============================================="
echo "Vault root: $VAULT_ROOT"
echo "Date: $(date -I)"
echo ""
echo "Building note index..."

build_note_index

echo "Indexed: $TOTAL_NOTES notes (excluding CLAUDE.md files)"
echo ""
echo "Counting incoming links..."

count_incoming_links

echo "Link scan complete."
echo ""

# === REPORT ORPHANS ===
echo "=============================================="
echo "  ORPHAN NOTES (0 incoming links)"
echo "=============================================="

report_notes() {
  local note
  for note in "${!INCOMING_LINKS[@]}"; do
    local count="${INCOMING_LINKS[$note]:-0}"
    local file="${NOTE_FILES[$note]:-}"
    [[ -z "$file" ]] && continue
    local relative_path="${file#$VAULT_ROOT/}"

    # Skip 99_ARCHIVE
    if [[ "$relative_path" == 99_ARCHIVE/* ]]; then
      continue
    fi

    local aw="${NOTE_AUTHORITY[$note]:-unknown}"

    if (( count == 0 )); then
      echo -e "  ${RED}ORPHAN${NC}: $relative_path (authority_weight: $aw)"
      ((ORPHAN_COUNT++)) || true
    elif (( count == 1 )); then
      ((LOW_LINK_COUNT++)) || true
    fi
  done
}

report_notes

if (( ORPHAN_COUNT == 0 )); then
  echo -e "  ${GREEN}None found.${NC}"
fi

# === LOW-LINK NOTES ===
echo ""
echo "=============================================="
echo "  LOW-LINK NOTES (only 1 incoming link)"
echo "=============================================="

report_low_link() {
  local note
  for note in "${!INCOMING_LINKS[@]}"; do
    local count="${INCOMING_LINKS[$note]:-0}"
    local file="${NOTE_FILES[$note]:-}"
    [[ -z "$file" ]] && continue
    local relative_path="${file#$VAULT_ROOT/}"

    if [[ "$relative_path" == 99_ARCHIVE/* ]]; then
      continue
    fi

    if (( count == 1 )); then
      local aw="${NOTE_AUTHORITY[$note]:-unknown}"
      echo -e "  ${YELLOW}LOW${NC}:    $relative_path (authority_weight: $aw, 1 incoming link)"
    fi
  done
}

report_low_link

if (( LOW_LINK_COUNT == 0 )); then
  echo -e "  ${GREEN}None found.${NC}"
fi

# === SUMMARY ===
echo ""
echo "=============================================="
echo "  SUMMARY"
echo "=============================================="
echo -e "Total notes scanned: $TOTAL_NOTES"
echo -e "Orphan notes:        ${RED}$ORPHAN_COUNT${NC}"
echo -e "Low-link notes:      ${YELLOW}$LOW_LINK_COUNT${NC}"
echo -e "Well-linked notes:   ${GREEN}$(( TOTAL_NOTES - ORPHAN_COUNT - LOW_LINK_COUNT ))${NC}"
echo ""

if (( ORPHAN_COUNT > 0 )); then
  echo -e "${YELLOW}RESULT: ${ORPHAN_COUNT} orphan notes found.${NC}"
  echo "These are candidates for the Viability audit (Law 3 — Economy)."
  echo "Review each: does it earn its place? If not, archive with rationale."
  exit 1
else
  echo -e "${GREEN}RESULT: PASS${NC} — No orphan notes (excluding 99_ARCHIVE)"
  exit 0
fi
