"""
StateChangeLogger — Tracks all vault artifact state changes.

Part of Agent Maestro v0.2 Runtime Engine (Upgrade 3.3).
Records create, modify, move, archive, and delete operations
on vault artifacts with before/after state for full auditability.
"""

import csv
import json
import os
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class ChangeType(Enum):
    CREATE = "create"
    MODIFY = "modify"
    MOVE = "move"
    ARCHIVE = "archive"
    DELETE = "delete"
    PROMOTE = "promote"
    REPAIR = "repair"


class StateChangeLogger:
    """
    Logs all state changes to vault artifacts.

    Every change records: what changed, who changed it, what the before/after
    states were, and whether the change was autonomous or escalated.
    """

    HEADERS = [
        "timestamp", "change_id", "change_type", "agent_id", "agent_role",
        "constellation", "artifact_path", "artifact_type", "field_changed",
        "before_state", "after_state", "justification", "confidence",
        "authority_check", "cycle_id"
    ]

    def __init__(self, vault_path: str, log_filename: str = "state_change_log.csv"):
        self.vault_path = vault_path
        self.log_path = os.path.join(vault_path, "06_EXECUTION", "logs", log_filename)
        self._change_counter = 0
        self._cycle_id = None
        self._ensure_log_exists()

    def _ensure_log_exists(self):
        """Create log file with headers if it doesn't exist or is empty."""
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        file_exists = os.path.exists(self.log_path)
        file_has_content = file_exists and os.path.getsize(self.log_path) > 0

        if not file_has_content:
            with open(self.log_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADERS)

    def start_cycle(self, cycle_id: str):
        """Begin a new logging cycle (e.g., maintenance run, session)."""
        self._cycle_id = cycle_id
        self._change_counter = 0

    def end_cycle(self) -> dict:
        """End the current cycle and return a summary."""
        summary = {
            "cycle_id": self._cycle_id,
            "total_changes": self._change_counter,
        }
        self._cycle_id = None
        return summary

    def log_change(
        self,
        change_type: ChangeType,
        agent_id: str,
        agent_role: str,
        constellation: str,
        artifact_path: str,
        artifact_type: str = "note",
        field_changed: str = "",
        before_state: str = "",
        after_state: str = "",
        justification: str = "",
        confidence: Optional[int] = None,
        authority_check: str = "passed",
    ) -> str:
        """
        Log a single state change.

        Args:
            change_type: Type of change (create, modify, move, etc.)
            agent_id: ID of the agent making the change
            agent_role: Role of the agent (executive, supervisor, specialist)
            constellation: Constellation the agent belongs to
            artifact_path: Vault-relative path to the artifact
            artifact_type: Type of artifact (note, csv, yaml, json)
            field_changed: Specific field that changed (for modify operations)
            before_state: Value before the change
            after_state: Value after the change
            justification: Why this change was made
            confidence: Confidence level 0-100 (for automated repairs)
            authority_check: Whether authority was checked (passed, escalated, overridden)

        Returns:
            The change_id for this entry
        """
        self._change_counter += 1
        timestamp = datetime.now(timezone.utc).isoformat()
        change_id = f"CHG-{timestamp[:10].replace('-', '')}-{self._change_counter:04d}"

        row = [
            timestamp,
            change_id,
            change_type.value,
            agent_id,
            agent_role,
            constellation,
            artifact_path,
            artifact_type,
            field_changed,
            before_state,
            after_state,
            justification,
            str(confidence) if confidence is not None else "",
            authority_check,
            self._cycle_id or "",
        ]

        with open(self.log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(row)

        return change_id

    def log_create(self, agent_id: str, agent_role: str, constellation: str,
                   artifact_path: str, artifact_type: str = "note",
                   justification: str = "", **kwargs) -> str:
        """Convenience method for logging artifact creation."""
        return self.log_change(
            change_type=ChangeType.CREATE,
            agent_id=agent_id, agent_role=agent_role,
            constellation=constellation, artifact_path=artifact_path,
            artifact_type=artifact_type, after_state="created",
            justification=justification, **kwargs,
        )

    def log_modify(self, agent_id: str, agent_role: str, constellation: str,
                   artifact_path: str, field_changed: str,
                   before_state: str, after_state: str,
                   justification: str = "", **kwargs) -> str:
        """Convenience method for logging artifact modification."""
        return self.log_change(
            change_type=ChangeType.MODIFY,
            agent_id=agent_id, agent_role=agent_role,
            constellation=constellation, artifact_path=artifact_path,
            field_changed=field_changed, before_state=before_state,
            after_state=after_state, justification=justification, **kwargs,
        )

    def log_move(self, agent_id: str, agent_role: str, constellation: str,
                 artifact_path: str, before_state: str, after_state: str,
                 justification: str = "", **kwargs) -> str:
        """Convenience method for logging artifact move/promote."""
        return self.log_change(
            change_type=ChangeType.MOVE,
            agent_id=agent_id, agent_role=agent_role,
            constellation=constellation, artifact_path=artifact_path,
            field_changed="location", before_state=before_state,
            after_state=after_state, justification=justification, **kwargs,
        )

    def log_repair(self, agent_id: str, agent_role: str, constellation: str,
                   artifact_path: str, field_changed: str,
                   before_state: str, after_state: str,
                   justification: str = "", confidence: int = 100,
                   **kwargs) -> str:
        """Convenience method for logging automated repairs."""
        return self.log_change(
            change_type=ChangeType.REPAIR,
            agent_id=agent_id, agent_role=agent_role,
            constellation=constellation, artifact_path=artifact_path,
            field_changed=field_changed, before_state=before_state,
            after_state=after_state, justification=justification,
            confidence=confidence, **kwargs,
        )

    def get_changes_for_artifact(self, artifact_path: str) -> list[dict]:
        """Retrieve all state changes for a given artifact."""
        changes = []
        if not os.path.exists(self.log_path):
            return changes

        with open(self.log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("artifact_path") == artifact_path:
                    changes.append(dict(row))
        return changes

    def get_changes_for_cycle(self, cycle_id: str) -> list[dict]:
        """Retrieve all state changes for a given cycle."""
        changes = []
        if not os.path.exists(self.log_path):
            return changes

        with open(self.log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("cycle_id") == cycle_id:
                    changes.append(dict(row))
        return changes

    def get_summary(self) -> dict:
        """Get a summary of all logged changes."""
        if not os.path.exists(self.log_path):
            return {"total": 0, "by_type": {}}

        counts = {}
        total = 0
        with open(self.log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total += 1
                ct = row.get("change_type", "unknown")
                counts[ct] = counts.get(ct, 0) + 1

        return {"total": total, "by_type": counts}
