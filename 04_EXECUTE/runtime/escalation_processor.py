"""
Escalation Processor — Monitors, groups, and resolves escalations.

Part of Agent Maestro v0.3 Runtime Engine (Phase B — E1/E3).

Reads the escalation_log.csv, groups pending escalations by recipient,
generates human-readable review queues, and supports approve/reject
resolution that can resume paused workflows.

Usage:
    processor = EscalationProcessor(vault_path)

    # Get pending escalations grouped by recipient
    grouped = processor.get_pending_grouped()

    # Review a specific escalation
    detail = processor.get_escalation_detail(escalation_id)

    # Approve or reject
    processor.resolve(escalation_id, "approved", reviewer="human_operator", notes="Looks good")
    processor.resolve(escalation_id, "rejected", reviewer="human_operator", notes="Too risky")

    # Generate review queue markdown
    processor.generate_review_queue()

    # Get dashboard summary
    summary = processor.get_dashboard_summary()
"""

import csv
import json
import os
from collections import defaultdict
from datetime import datetime, timezone
from typing import Optional


class EscalationProcessor:
    """
    Processes, groups, and resolves escalations from the governance system.

    Reads from escalation_log.csv (written by GovernedAgent._log_escalation)
    and manages the full lifecycle: pending → approved/rejected.
    """

    def __init__(self, vault_path: str):
        self.vault_path = vault_path
        self.log_path = os.path.join(vault_path, "06_EXECUTION", "logs", "escalation_log.csv")
        self.review_queue_dir = os.path.join(vault_path, "06_EXECUTION", "review_queue")
        self.resolution_log_path = os.path.join(vault_path, "06_EXECUTION", "logs", "escalation_resolution_log.csv")

    def _read_log(self) -> list[dict]:
        """Read all entries from escalation_log.csv."""
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def _write_log(self, entries: list[dict]):
        """Rewrite the full escalation_log.csv."""
        if not entries:
            return
        headers = list(entries[0].keys())
        with open(self.log_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(entries)

    def get_all(self) -> list[dict]:
        """Return all escalation entries with generated IDs."""
        entries = self._read_log()
        for i, entry in enumerate(entries):
            entry["escalation_id"] = f"ESC-{i+1:04d}"
        return entries

    def get_pending(self) -> list[dict]:
        """Return only pending escalations."""
        return [e for e in self.get_all() if e.get("status") == "pending"]

    def get_pending_grouped(self) -> dict[str, list[dict]]:
        """Group pending escalations by escalates_to recipient."""
        grouped = defaultdict(list)
        for entry in self.get_pending():
            recipient = entry.get("escalates_to", "unknown")
            grouped[recipient].append(entry)
        return dict(grouped)

    def get_escalation_detail(self, escalation_id: str) -> Optional[dict]:
        """Get full details of a specific escalation by ID."""
        for entry in self.get_all():
            if entry.get("escalation_id") == escalation_id:
                return entry
        return None

    def resolve(self, escalation_id: str, resolution: str,
                reviewer: str = "human_operator", notes: str = "") -> bool:
        """
        Resolve a pending escalation.

        Args:
            escalation_id: The ESC-XXXX ID
            resolution: One of "approved", "rejected"
            reviewer: Who is resolving this
            notes: Review notes

        Returns:
            True if resolved, False if not found or already resolved
        """
        entries = self.get_all()
        resolved = False

        for entry in entries:
            if entry.get("escalation_id") == escalation_id:
                if entry.get("status") != "pending":
                    return False  # Already resolved
                entry["status"] = resolution
                resolved = True
                break

        if not resolved:
            return False

        # Remove the escalation_id field before writing back
        write_entries = []
        for entry in entries:
            e = dict(entry)
            e.pop("escalation_id", None)
            write_entries.append(e)
        self._write_log(write_entries)

        # Log the resolution
        self._log_resolution(escalation_id, resolution, reviewer, notes)

        return True

    def _log_resolution(self, escalation_id: str, resolution: str,
                        reviewer: str, notes: str):
        """Append a resolution entry to the resolution log."""
        os.makedirs(os.path.dirname(self.resolution_log_path), exist_ok=True)
        file_exists = os.path.exists(self.resolution_log_path)
        file_has_content = file_exists and os.path.getsize(self.resolution_log_path) > 0

        headers = ["timestamp", "escalation_id", "resolution", "reviewer", "notes"]

        with open(self.resolution_log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            if not file_has_content:
                writer.writeheader()
            writer.writerow({
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "escalation_id": escalation_id,
                "resolution": resolution,
                "reviewer": reviewer,
                "notes": notes,
            })

    def generate_review_queue(self) -> str:
        """
        Generate a markdown review queue file and return its path.

        Creates a human-readable document in 06_EXECUTION/review_queue/
        with pending escalations grouped by recipient, ready for review.
        """
        os.makedirs(self.review_queue_dir, exist_ok=True)
        grouped = self.get_pending_grouped()
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        queue_path = os.path.join(self.review_queue_dir, f"review_queue_{timestamp}.md")

        pending_count = sum(len(v) for v in grouped.values())

        lines = [
            "---",
            "schema_version: 2",
            f"title: Escalation Review Queue — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')}",
            "status: active",
            f"created_date: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            f"last_modified: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            "tags:",
            "  - escalation",
            "  - review-queue",
            "  - execution",
            "---",
            "",
            "# Escalation Review Queue",
            "",
            f"**Generated:** {datetime.now(timezone.utc).isoformat()}",
            f"**Pending Escalations:** {pending_count}",
            f"**Recipients:** {len(grouped)}",
            "",
        ]

        if not grouped:
            lines.append("No pending escalations.")
        else:
            for recipient, escalations in sorted(grouped.items()):
                lines.append(f"## Escalated To: {recipient}")
                lines.append(f"")
                lines.append(f"**Count:** {len(escalations)}")
                lines.append("")

                for esc in escalations:
                    esc_id = esc.get("escalation_id", "unknown")
                    lines.append(f"### {esc_id}")
                    lines.append("")
                    lines.append(f"- **Agent:** {esc.get('agent_id', 'unknown')}")
                    lines.append(f"- **Role:** {esc.get('agent_role', 'unknown')}")
                    lines.append(f"- **Constellation:** {esc.get('constellation', 'unknown')}")
                    lines.append(f"- **Action:** {esc.get('action', 'unknown')}")
                    lines.append(f"- **Reason:** {esc.get('reason', 'unknown')}")
                    lines.append(f"- **Timestamp:** {esc.get('timestamp', 'unknown')}")
                    lines.append("")
                    lines.append(f"**Decision:** [ ] Approve  [ ] Reject")
                    lines.append(f"**Notes:** ")
                    lines.append("")
                    lines.append("---")
                    lines.append("")

        with open(queue_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

        return queue_path

    def get_dashboard_summary(self) -> dict:
        """
        Generate a dashboard summary of all escalations.

        Returns a dict suitable for JSON report or display.
        """
        all_entries = self.get_all()
        pending = [e for e in all_entries if e.get("status") == "pending"]
        approved = [e for e in all_entries if e.get("status") == "approved"]
        rejected = [e for e in all_entries if e.get("status") == "rejected"]

        # Group by constellation
        by_constellation = defaultdict(int)
        for e in pending:
            by_constellation[e.get("constellation", "unknown")] += 1

        # Group by recipient
        by_recipient = defaultdict(int)
        for e in pending:
            by_recipient[e.get("escalates_to", "unknown")] += 1

        # Group by action (top 10)
        by_action = defaultdict(int)
        for e in pending:
            by_action[e.get("action", "unknown")] += 1
        top_actions = sorted(by_action.items(), key=lambda x: x[1], reverse=True)[:10]

        # Recent escalations (last 10)
        recent = sorted(pending, key=lambda e: e.get("timestamp", ""), reverse=True)[:10]

        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_escalations": len(all_entries),
            "pending": len(pending),
            "approved": len(approved),
            "rejected": len(rejected),
            "by_constellation": dict(by_constellation),
            "by_recipient": dict(by_recipient),
            "top_actions": top_actions,
            "recent_pending": [
                {
                    "escalation_id": e.get("escalation_id"),
                    "agent_id": e.get("agent_id"),
                    "action": e.get("action"),
                    "reason": e.get("reason", "")[:80],
                    "timestamp": e.get("timestamp"),
                }
                for e in recent
            ],
        }

    def generate_dashboard_report(self) -> str:
        """Generate a JSON dashboard report and return its path."""
        summary = self.get_dashboard_summary()
        report_dir = os.path.join(self.vault_path, "06_EXECUTION", "reports")
        os.makedirs(report_dir, exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(report_dir, f"escalation_dashboard_{timestamp}.json")

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, default=str)

        return report_path
