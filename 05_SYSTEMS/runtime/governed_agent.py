"""
GovernedAgent — Base class for authority-governed agent execution.

Part of Agent Maestro v0.2 Runtime Engine.
All agents load a compiled authority pack at init and check permissions before every action.
"""

import json
import csv
import os
import sys
from datetime import datetime, timezone
from enum import Enum
from typing import Optional

# Allow importing sibling modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from state_change_logger import StateChangeLogger, ChangeType
    HAS_STATE_CHANGE_LOGGER = True
except ImportError:
    HAS_STATE_CHANGE_LOGGER = False


class Permission(Enum):
    ALLOWED = "allowed"
    DENIED = "denied"
    REQUIRES_ESCALATION = "requires_escalation"


class ActionResult:
    """Result of attempting an agent action."""

    def __init__(self, action: str, permission: Permission, executed: bool,
                 outcome: Optional[str] = None, conditions: Optional[str] = None,
                 error: Optional[str] = None):
        self.action = action
        self.permission = permission
        self.executed = executed
        self.outcome = outcome
        self.conditions = conditions
        self.error = error
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        return {
            "action": self.action,
            "permission": self.permission.value,
            "executed": self.executed,
            "outcome": self.outcome,
            "conditions": self.conditions,
            "error": self.error,
            "timestamp": self.timestamp,
        }


class GovernedAgent:
    """
    Base class for all governed agents in Agent Maestro.

    Loads a compiled authority pack JSON at init.
    Before every action, checks permissions against the pack.
    Logs all actions and escalations to CSV.
    """

    def __init__(self, compiled_pack_path: str, vault_path: str):
        """
        Initialize a GovernedAgent.

        Args:
            compiled_pack_path: Path to the compiled authority pack JSON
            vault_path: Root path of the Agent Maestro vault
        """
        self.vault_path = vault_path
        self.compiled_pack_path = compiled_pack_path
        self.pack = self._load_pack(compiled_pack_path)

        # Extract identity from pack
        self.agent_id = self.pack["artifact_id"]
        self.agent_name = self.pack["compiled_from"]["pack_name"]
        self.agent_role = self.pack["compiled_from"]["agent_role"]
        self.constellation = self.pack["compiled_from"]["constellation"]

        # Extract governance
        self.governance = self.pack["governance"]
        self.governed_actions = self._index_actions(self.governance.get("governed_actions", []))
        self.rules = self.governance.get("rules", [])
        self.control_gates = self.governance.get("control_gates", [])
        self.escalation = self.governance.get("escalation", {})
        self.failure_semantics = self.governance.get("failure_semantics", {})

        # Logging paths
        self.task_log_path = os.path.join(vault_path, "06_EXECUTION/logs/task_execution_log.csv")
        self.escalation_log_path = os.path.join(vault_path, "06_EXECUTION/logs/escalation_log.csv")

        # State change logger (Upgrade 3.3)
        if HAS_STATE_CHANGE_LOGGER:
            self.state_logger = StateChangeLogger(vault_path)
        else:
            self.state_logger = None

        # Action history for this session
        self.action_history = []

    def _load_pack(self, path: str) -> dict:
        """Load and validate a compiled authority pack."""
        with open(path, 'r', encoding='utf-8') as f:
            pack = json.load(f)

        required_keys = ["artifact_id", "compiled_from", "governance"]
        for key in required_keys:
            if key not in pack:
                raise ValueError(f"Compiled pack missing required key: {key}")

        return pack

    def _index_actions(self, actions: list) -> dict:
        """Build a lookup index from governed_actions list."""
        index = {}
        for action_def in actions:
            action_name = action_def["action"].lower().strip()
            index[action_name] = {
                "permission": Permission(action_def["permission"]),
                "conditions": action_def.get("conditions", ""),
            }
        return index

    def check_permission(self, action: str) -> tuple[Permission, str]:
        """
        Check if an action is permitted by this agent's authority pack.

        Returns (Permission, conditions_string).

        Matching strategy (v0.3 — hardened):
        1. Exact match against governed_actions index
        2. Fail-safe: unknown actions → REQUIRES_ESCALATION

        The previous substring matching (v0.2) was removed because it allowed
        compound actions like "read note and delete files" to match against
        "read note" and bypass governance. Exact match only is safer.
        """
        action_lower = action.lower().strip()

        # Exact match only — no substring matching
        if action_lower in self.governed_actions:
            entry = self.governed_actions[action_lower]
            return entry["permission"], entry["conditions"]

        # Unknown action — fail-safe to escalation
        return Permission.REQUIRES_ESCALATION, "Action not defined in authority pack — escalating"

    def check_control_gates(self, context: dict = None) -> tuple[bool, list[dict]]:
        """
        Evaluate control gates against the provided context.

        Control gates are conditions that must be satisfied before execution.
        Each gate has an on_fail policy: 'block', 'escalate', or 'log_and_continue'.

        Context dict can contain gate evaluators — functions keyed by gate_id
        that return True (pass) or False (fail). Gates without evaluators
        default to 'pass' (open-world assumption for unevaluable gates).

        Args:
            context: Dict with optional gate evaluator functions keyed by gate_id.
                     Each evaluator is a callable returning bool.

        Returns:
            (all_passed: bool, gate_results: list[dict])
            all_passed is False if any gate with on_fail='block' or 'escalate' failed.
        """
        context = context or {}
        gate_results = []
        all_passed = True

        for gate in self.control_gates:
            gate_id = gate["gate_id"]
            on_fail = gate.get("on_fail", "escalate")

            # Check if context provides an evaluator for this gate
            evaluator = context.get(gate_id)
            if evaluator and callable(evaluator):
                passed = evaluator()
            elif evaluator is not None:
                # Non-callable truthy/falsy value
                passed = bool(evaluator)
            else:
                # No evaluator provided — gate passes by default
                # (cannot evaluate declarative conditions without context)
                passed = True

            status = "passed" if passed else "failed"

            if not passed:
                if on_fail in ("block", "escalate"):
                    all_passed = False
                if on_fail == "escalate":
                    self._log_escalation(
                        f"Control gate {gate_id}",
                        f"Gate failed: {gate['condition']}"
                    )

            gate_results.append({
                "gate_id": gate_id,
                "condition": gate["condition"],
                "on_fail": on_fail,
                "status": status,
            })

        return all_passed, gate_results

    def check_evidence_requirements(self) -> tuple[bool, list[dict]]:
        """
        Validate that all required evidence files exist.

        Evidence requirements are defined in the authority pack and specify
        files that must be present (e.g., audit reports, CSVs) before the
        agent can operate.

        Returns:
            (all_satisfied: bool, evidence_results: list[dict])
        """
        evidence_reqs = self.governance.get("evidence_requirements", [])
        results = []
        all_satisfied = True

        for req in evidence_reqs:
            evidence_type = req.get("evidence_type", "unknown")
            required = req.get("required", False)
            fmt = req.get("format", "")

            # Try to extract a file path from the format string
            # Common patterns: "CSV at 06_EXECUTION/logs/task_execution_log.csv"
            # or "CSV entry in task_execution_log.csv"
            file_path = None
            satisfied = True

            if fmt:
                # Look for vault-relative paths in the format string
                for token in fmt.replace(",", " ").split():
                    if "/" in token and ("." in token.split("/")[-1]):
                        # Looks like a file path
                        candidate = os.path.join(self.vault_path, token)
                        file_path = token
                        if required and not os.path.exists(candidate):
                            satisfied = False
                            all_satisfied = False
                        break

            results.append({
                "evidence_type": evidence_type,
                "required": required,
                "format": fmt,
                "file_path": file_path,
                "satisfied": satisfied,
            })

        return all_satisfied, results

    def attempt_action(self, action: str, execute_fn=None, context: dict = None) -> ActionResult:
        """
        Attempt to perform an action under governance.

        Pipeline (v0.3 — hardened):
        1. Check permission against authority pack
        2. If allowed, check control gates (block/escalate on failure)
        3. If gates pass, check evidence requirements
        4. If all checks pass and execute_fn provided, execute it
        5. Log the result
        6. If requires_escalation, log to escalation log

        Args:
            action: Description of the action to attempt
            execute_fn: Optional callable that performs the actual work. Returns outcome string.
            context: Optional context dict for the action. May include gate evaluator
                     functions keyed by gate_id for control gate enforcement.

        Returns:
            ActionResult
        """
        permission, conditions = self.check_permission(action)

        result = None

        if permission == Permission.ALLOWED:
            # Gate check — enforce control gates before execution
            gates_passed, gate_results = self.check_control_gates(context)
            if not gates_passed:
                failed_gates = [g for g in gate_results if g["status"] == "failed"]
                gate_msg = "; ".join(f"{g['gate_id']}: {g['condition']}" for g in failed_gates)
                block_gates = [g for g in failed_gates if g["on_fail"] == "block"]
                if block_gates:
                    result = ActionResult(action, Permission.DENIED, False,
                                          outcome=f"blocked_by_control_gate: {gate_msg}",
                                          conditions=conditions)
                else:
                    # Escalate gates — treat as escalation
                    result = ActionResult(action, Permission.REQUIRES_ESCALATION, False,
                                          outcome=f"gate_escalation: {gate_msg}",
                                          conditions=conditions)

            # Evidence check — verify required evidence exists
            if result is None:
                evidence_ok, evidence_results = self.check_evidence_requirements()
                if not evidence_ok:
                    missing = [e for e in evidence_results if not e["satisfied"]]
                    missing_msg = "; ".join(f"{e['evidence_type']}: {e['file_path']}" for e in missing)
                    result = ActionResult(action, Permission.REQUIRES_ESCALATION, False,
                                          outcome=f"missing_evidence: {missing_msg}",
                                          conditions=conditions)
                    self._log_escalation(action, f"Missing required evidence: {missing_msg}")

            # Execute if all checks passed
            if result is None:
                if execute_fn:
                    try:
                        outcome = execute_fn(context or {})
                        result = ActionResult(action, permission, True, outcome=str(outcome), conditions=conditions)
                    except Exception as e:
                        result = ActionResult(action, permission, False, error=str(e), conditions=conditions)
                        # On execution failure, check failure semantics
                        if self.failure_semantics.get("on_execution_failure") == "escalate":
                            self._log_escalation(action, f"Execution failed: {e}")
                else:
                    result = ActionResult(action, permission, True, outcome="action_permitted_no_fn", conditions=conditions)

        elif permission == Permission.DENIED:
            result = ActionResult(action, permission, False,
                                  outcome="blocked_by_authority", conditions=conditions)

        elif permission == Permission.REQUIRES_ESCALATION:
            result = ActionResult(action, permission, False,
                                  outcome="escalation_required", conditions=conditions)
            self._log_escalation(action, conditions)

        self.action_history.append(result)
        self._log_task_execution(result)
        return result

    def _log_task_execution(self, result: ActionResult):
        """Append an entry to the task execution log CSV."""
        file_exists = os.path.exists(self.task_log_path)
        file_has_content = file_exists and os.path.getsize(self.task_log_path) > 0

        # Only write header if file is empty or doesn't exist
        needs_header = not file_has_content

        with open(self.task_log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if needs_header:
                writer.writerow([
                    "timestamp", "agent_id", "agent_role", "constellation",
                    "action", "permission", "executed", "outcome", "conditions", "error"
                ])
            writer.writerow([
                result.timestamp,
                self.agent_id,
                self.agent_role,
                self.constellation,
                result.action,
                result.permission.value,
                result.executed,
                result.outcome or "",
                result.conditions or "",
                result.error or "",
            ])

    def _log_escalation(self, action: str, reason: str):
        """Append an entry to the escalation log CSV."""
        file_exists = os.path.exists(self.escalation_log_path)
        file_has_content = file_exists and os.path.getsize(self.escalation_log_path) > 0

        needs_header = not file_has_content

        escalates_to = self.escalation.get("escalates_to", "unknown")

        with open(self.escalation_log_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if needs_header:
                writer.writerow([
                    "timestamp", "agent_id", "agent_role", "constellation",
                    "action", "reason", "escalates_to", "status"
                ])
            writer.writerow([
                datetime.now(timezone.utc).isoformat(),
                self.agent_id,
                self.agent_role,
                self.constellation,
                action,
                reason,
                escalates_to,
                "pending",
            ])

    def log_state_change(self, change_type: str, artifact_path: str,
                         field_changed: str = "", before_state: str = "",
                         after_state: str = "", justification: str = "",
                         confidence: int = None, artifact_type: str = "note") -> Optional[str]:
        """
        Log a state change to the state_change_log.csv via StateChangeLogger.

        Args:
            change_type: One of: create, modify, move, archive, delete, promote, repair
            artifact_path: Vault-relative path to the artifact
            field_changed: Specific field that changed
            before_state: Value before the change
            after_state: Value after the change
            justification: Why this change was made
            confidence: Confidence level 0-100 (for automated repairs)
            artifact_type: Type of artifact (note, csv, yaml, json)

        Returns:
            The change_id, or None if state logger is not available
        """
        if not self.state_logger:
            return None

        ct = ChangeType(change_type)
        return self.state_logger.log_change(
            change_type=ct,
            agent_id=self.agent_id,
            agent_role=self.agent_role,
            constellation=self.constellation,
            artifact_path=artifact_path,
            artifact_type=artifact_type,
            field_changed=field_changed,
            before_state=before_state,
            after_state=after_state,
            justification=justification,
            confidence=confidence,
        )

    def get_session_summary(self) -> dict:
        """Return a summary of all actions in this session."""
        total = len(self.action_history)
        allowed = sum(1 for r in self.action_history if r.permission == Permission.ALLOWED)
        denied = sum(1 for r in self.action_history if r.permission == Permission.DENIED)
        escalated = sum(1 for r in self.action_history if r.permission == Permission.REQUIRES_ESCALATION)
        executed = sum(1 for r in self.action_history if r.executed)
        failed = sum(1 for r in self.action_history if r.permission == Permission.ALLOWED and not r.executed)

        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "total_actions": total,
            "allowed": allowed,
            "denied": denied,
            "escalated": escalated,
            "executed": executed,
            "failed": failed,
            "actions": [r.to_dict() for r in self.action_history],
        }
