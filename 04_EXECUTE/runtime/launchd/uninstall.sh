#!/usr/bin/env bash
# uninstall.sh — Remove the vault-maintenance launchd agent.

set -euo pipefail

PLIST_NAME="com.agentmaestro.vault-maintenance.plist"
PLIST_DST="${HOME}/Library/LaunchAgents/${PLIST_NAME}"

# Unload if running
if launchctl list | grep -q "com.agentmaestro.vault-maintenance"; then
    echo "Unloading agent..."
    launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# Remove plist
if [[ -f "$PLIST_DST" ]]; then
    rm "$PLIST_DST"
    echo "Removed ${PLIST_DST}"
else
    echo "Plist not found at ${PLIST_DST} (already removed?)"
fi

# Verify
if launchctl list | grep -q "com.agentmaestro.vault-maintenance"; then
    echo "WARNING: Agent may still be loaded. Check with:"
    echo "  launchctl list | grep agentmaestro"
else
    echo "SUCCESS: Agent uninstalled."
fi
