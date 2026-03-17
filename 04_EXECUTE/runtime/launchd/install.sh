#!/usr/bin/env bash
# install.sh — Install the vault-maintenance launchd agent.
#
# Validates the plist, copies it to ~/Library/LaunchAgents/, and loads it.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_NAME="com.agentmaestro.vault-maintenance.plist"
PLIST_SRC="${SCRIPT_DIR}/${PLIST_NAME}"
PLIST_DST="${HOME}/Library/LaunchAgents/${PLIST_NAME}"
LAUNCH_AGENTS_DIR="${HOME}/Library/LaunchAgents"

# Validate source plist exists
if [[ ! -f "$PLIST_SRC" ]]; then
    echo "ERROR: plist not found at ${PLIST_SRC}"
    exit 1
fi

# Validate plist XML
if ! plutil -lint "$PLIST_SRC" > /dev/null 2>&1; then
    echo "ERROR: plist validation failed"
    plutil -lint "$PLIST_SRC"
    exit 1
fi

# Validate that run_maintenance.sh exists and is executable
RUN_SCRIPT="${SCRIPT_DIR}/../run_maintenance.sh"
if [[ ! -x "$RUN_SCRIPT" ]]; then
    echo "ERROR: run_maintenance.sh not found or not executable at ${RUN_SCRIPT}"
    exit 1
fi

# Validate that orchestrate.sh exists
VAULT_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
ORCHESTRATOR="${VAULT_ROOT}/04_EXECUTE/tools/vault-maintenance/orchestrate.sh"
if [[ ! -x "$ORCHESTRATOR" ]]; then
    echo "ERROR: orchestrate.sh not found or not executable at ${ORCHESTRATOR}"
    exit 1
fi

# Ensure LaunchAgents directory exists
mkdir -p "$LAUNCH_AGENTS_DIR"

# Unload existing agent if present
if launchctl list | grep -q "com.agentmaestro.vault-maintenance"; then
    echo "Unloading existing agent..."
    launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# Copy plist
cp "$PLIST_SRC" "$PLIST_DST"
echo "Installed plist to ${PLIST_DST}"

# Load agent
launchctl load "$PLIST_DST"
echo "Loaded agent: com.agentmaestro.vault-maintenance"

# Verify
if launchctl list | grep -q "com.agentmaestro.vault-maintenance"; then
    echo "SUCCESS: Agent is loaded and scheduled."
    echo "Schedule: Daily at 06:00"
    echo "To test now: launchctl start com.agentmaestro.vault-maintenance"
else
    echo "WARNING: Agent may not have loaded correctly. Check with:"
    echo "  launchctl list | grep agentmaestro"
    exit 1
fi
