#!/usr/bin/env bash
# yaml_validation.sh — Validate YAML frontmatter against schema v3 rules.
# Enforces Vault Rules 5, 9–14.
#
# Thin shell wrapper around lib/yaml_validator.py for exit code consistency.
# Exit codes: 0 = clean, 1 = findings, 2 = error

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Build Python args from shell args
PYTHON_ARGS=()
CONFIG_FILE=""
VAULT_ROOT_ARG=""
OUTPUT_DIR_ARG=""
QUIET=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --config)    CONFIG_FILE="$2"; shift 2 ;;
        --vault-root) VAULT_ROOT_ARG="$2"; shift 2 ;;
        --output-dir) OUTPUT_DIR_ARG="$2"; shift 2 ;;
        --quiet)     QUIET="--quiet"; shift ;;
        *)           shift ;;
    esac
done

# If no vault root from CLI, try to parse from config
if [[ -z "$VAULT_ROOT_ARG" && -n "$CONFIG_FILE" ]]; then
    VAULT_ROOT_ARG=$(grep '^vault_root:' "$CONFIG_FILE" 2>/dev/null | sed 's/vault_root:[[:space:]]*"\?\([^"]*\)"\?/\1/' || true)
fi

if [[ -z "$VAULT_ROOT_ARG" ]]; then
    echo "ERROR: vault_root not set. Use --vault-root or set in config." >&2
    exit 2
fi

PYTHON_ARGS+=(--vault-root "$VAULT_ROOT_ARG")
[[ -n "$CONFIG_FILE" ]] && PYTHON_ARGS+=(--config "$CONFIG_FILE")
[[ -n "$OUTPUT_DIR_ARG" ]] && PYTHON_ARGS+=(--output-dir "$OUTPUT_DIR_ARG")
[[ -n "$QUIET" ]] && PYTHON_ARGS+=("$QUIET")

# Find Python
PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON="$cmd"
        break
    fi
done

if [[ -z "$PYTHON" ]]; then
    echo "ERROR: Python not found. yaml_validation requires Python 3 with PyYAML." >&2
    exit 2
fi

exec "$PYTHON" "${SCRIPT_DIR}/lib/yaml_validator.py" "${PYTHON_ARGS[@]}"
