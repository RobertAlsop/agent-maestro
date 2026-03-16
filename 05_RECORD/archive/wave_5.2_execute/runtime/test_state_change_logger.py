"""
Tests for StateChangeLogger — Upgrade 3.3 State Change Logging.
"""

import csv
import os
import sys
import tempfile
import unittest

# Ensure the runtime directory is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from state_change_logger import StateChangeLogger, ChangeType


class TestStateChangeLogger(unittest.TestCase):

    def setUp(self):
        """Create a temporary vault structure for each test."""
        self.temp_dir = tempfile.mkdtemp()
        self.vault_path = self.temp_dir
        os.makedirs(os.path.join(self.vault_path, "06_EXECUTION", "logs"), exist_ok=True)
        self.logger = StateChangeLogger(self.vault_path)

    def tearDown(self):
        """Clean up temp files."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def _read_log(self):
        """Read the log CSV and return rows as list of dicts."""
        with open(self.logger.log_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def test_creates_log_file_on_init(self):
        """Logger creates CSV with headers on init."""
        self.assertTrue(os.path.exists(self.logger.log_path))
        rows = self._read_log()
        self.assertEqual(len(rows), 0)

    def test_log_create(self):
        """log_create writes a create entry."""
        change_id = self.logger.log_create(
            agent_id="test.agent",
            agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="02_KNOWLEDGE/concepts/test_note.md",
            justification="New concept note created",
        )
        self.assertTrue(change_id.startswith("CHG-"))
        rows = self._read_log()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["change_type"], "create")
        self.assertEqual(rows[0]["artifact_path"], "02_KNOWLEDGE/concepts/test_note.md")

    def test_log_modify(self):
        """log_modify writes a modify entry with before/after."""
        self.logger.log_modify(
            agent_id="test.agent",
            agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="02_KNOWLEDGE/concepts/test_note.md",
            field_changed="status",
            before_state="draft",
            after_state="active",
            justification="Note reviewed and activated",
        )
        rows = self._read_log()
        self.assertEqual(rows[0]["change_type"], "modify")
        self.assertEqual(rows[0]["field_changed"], "status")
        self.assertEqual(rows[0]["before_state"], "draft")
        self.assertEqual(rows[0]["after_state"], "active")

    def test_log_repair_with_confidence(self):
        """log_repair records confidence score."""
        self.logger.log_repair(
            agent_id="self_healing.agent",
            agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="02_KNOWLEDGE/concepts/test_note.md",
            field_changed="note_class",
            before_state="index",
            after_state="reference",
            justification="Invalid controlled vocabulary value corrected",
            confidence=95,
        )
        rows = self._read_log()
        self.assertEqual(rows[0]["change_type"], "repair")
        self.assertEqual(rows[0]["confidence"], "95")

    def test_log_move(self):
        """log_move records location changes."""
        self.logger.log_move(
            agent_id="note_processor.agent",
            agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="01_CAPTURE/raw_idea.md",
            before_state="01_CAPTURE/raw_idea.md",
            after_state="02_KNOWLEDGE/concepts/raw_idea.md",
            justification="Capture promoted to knowledge base",
        )
        rows = self._read_log()
        self.assertEqual(rows[0]["change_type"], "move")
        self.assertEqual(rows[0]["field_changed"], "location")

    def test_cycle_tracking(self):
        """start_cycle and end_cycle track changes within a cycle."""
        self.logger.start_cycle("CYCLE-2026-03-14-001")
        self.logger.log_create(
            agent_id="test.agent", agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="test1.md",
        )
        self.logger.log_create(
            agent_id="test.agent", agent_role="specialist",
            constellation="vault_maintenance",
            artifact_path="test2.md",
        )
        summary = self.logger.end_cycle()
        self.assertEqual(summary["cycle_id"], "CYCLE-2026-03-14-001")
        self.assertEqual(summary["total_changes"], 2)

        rows = self._read_log()
        for row in rows:
            self.assertEqual(row["cycle_id"], "CYCLE-2026-03-14-001")

    def test_get_changes_for_artifact(self):
        """Retrieves changes filtered by artifact path."""
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="note_a.md",
        )
        self.logger.log_modify(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="note_a.md",
            field_changed="status", before_state="draft", after_state="active",
        )
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="note_b.md",
        )

        changes = self.logger.get_changes_for_artifact("note_a.md")
        self.assertEqual(len(changes), 2)

        changes_b = self.logger.get_changes_for_artifact("note_b.md")
        self.assertEqual(len(changes_b), 1)

    def test_get_changes_for_cycle(self):
        """Retrieves changes filtered by cycle ID."""
        self.logger.start_cycle("C1")
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="note1.md",
        )
        self.logger.end_cycle()

        self.logger.start_cycle("C2")
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="note2.md",
        )
        self.logger.end_cycle()

        c1_changes = self.logger.get_changes_for_cycle("C1")
        self.assertEqual(len(c1_changes), 1)
        self.assertEqual(c1_changes[0]["artifact_path"], "note1.md")

    def test_get_summary(self):
        """Summary counts changes by type."""
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="n1.md",
        )
        self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="n2.md",
        )
        self.logger.log_repair(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="n3.md",
            field_changed="status", before_state="x", after_state="y",
            confidence=90,
        )

        summary = self.logger.get_summary()
        self.assertEqual(summary["total"], 3)
        self.assertEqual(summary["by_type"]["create"], 2)
        self.assertEqual(summary["by_type"]["repair"], 1)

    def test_change_id_increments(self):
        """Change IDs increment within a session."""
        id1 = self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="n1.md",
        )
        id2 = self.logger.log_create(
            agent_id="a1", agent_role="specialist",
            constellation="vm", artifact_path="n2.md",
        )
        # IDs should be different
        self.assertNotEqual(id1, id2)
        # Second should have higher counter
        self.assertTrue(id2 > id1)

    def test_all_change_types(self):
        """All ChangeType enum values are valid."""
        for ct in ChangeType:
            change_id = self.logger.log_change(
                change_type=ct,
                agent_id="test", agent_role="specialist",
                constellation="vm", artifact_path=f"test_{ct.value}.md",
            )
            self.assertTrue(change_id.startswith("CHG-"))


if __name__ == "__main__":
    unittest.main()
