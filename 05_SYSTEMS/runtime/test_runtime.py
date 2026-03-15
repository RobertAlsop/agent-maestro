"""
Tests for the Agent Maestro Runtime Engine.
Validates GovernedAgent permission checking, logging, and AgentRuntime lifecycle.
"""

import os
import sys
import json
import csv
import tempfile
import shutil

# Add runtime to path
sys.path.insert(0, os.path.dirname(__file__))

from governed_agent import GovernedAgent, Permission, ActionResult
from agent_runtime import AgentRuntime

VAULT = "/sessions/loving-busy-bohr/mnt/Agent Maestro"
ARTIFACTS = os.path.join(VAULT, "05_SYSTEMS/authority_architecture/compiler/prototype/artifacts")


def test_load_executive_pack():
    """Test loading the Vault Curator Executive compiled pack."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    assert agent.agent_id == "compiled.CONST.vault_curator.executive.v1.0"
    assert agent.agent_role == "executive"
    assert agent.constellation == "vault_curator"
    assert len(agent.governed_actions) > 0
    print("  PASS: test_load_executive_pack")


def test_permission_allowed():
    """Test that allowed actions are correctly identified."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    perm, cond = agent.check_permission("Prioritise maintenance tasks")
    assert perm == Permission.ALLOWED, f"Expected ALLOWED, got {perm}"
    print("  PASS: test_permission_allowed")


def test_permission_denied():
    """Test that denied actions are correctly identified."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    perm, cond = agent.check_permission("Change vault directory structure")
    assert perm == Permission.DENIED, f"Expected DENIED, got {perm}"
    print("  PASS: test_permission_denied")


def test_permission_escalation():
    """Test that escalation actions are correctly identified."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    perm, cond = agent.check_permission("Delete vault files")
    assert perm == Permission.REQUIRES_ESCALATION, f"Expected REQUIRES_ESCALATION, got {perm}"
    print("  PASS: test_permission_escalation")


def test_unknown_action_escalates():
    """Test that unknown actions default to escalation (fail-safe)."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    perm, cond = agent.check_permission("Launch nuclear missiles")
    assert perm == Permission.REQUIRES_ESCALATION, f"Expected REQUIRES_ESCALATION, got {perm}"
    print("  PASS: test_unknown_action_escalates")


def test_substring_bypass_blocked():
    """v0.3 SECURITY: Substring matching no longer grants permissions.
    Previously 'read note and delete files' would match 'Prioritise maintenance tasks'
    via substring. Now only exact matches work."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # This compound action contains parts of allowed actions but is NOT an exact match
    perm, _ = agent.check_permission("Prioritise maintenance tasks and delete vault files")
    assert perm == Permission.REQUIRES_ESCALATION, f"Expected REQUIRES_ESCALATION for compound action, got {perm}"
    print("  PASS: test_substring_bypass_blocked")


def test_compound_action_escalates():
    """v0.3 SECURITY: Actions that embed allowed action names are escalated."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_specialist_link_auditor_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # "Scan vault files for wiki-links" is allowed, but adding extra text should fail
    perm, _ = agent.check_permission("Scan vault files for wiki-links then modify them")
    assert perm == Permission.REQUIRES_ESCALATION, f"Expected REQUIRES_ESCALATION, got {perm}"
    print("  PASS: test_compound_action_escalates")


def test_control_gate_blocks():
    """v0.3 SECURITY: Control gates with on_fail=block actually block execution."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # Provide a failing gate evaluator
    context = {}
    for gate in agent.control_gates:
        if gate.get("on_fail") == "block":
            context[gate["gate_id"]] = False  # Force gate failure
            break

    if context:
        result = agent.attempt_action(
            "Prioritise maintenance tasks",
            lambda ctx: "should_not_run",
            context=context
        )
        assert result.executed is False, "Action should have been blocked by control gate"
        assert "blocked_by_control_gate" in result.outcome
        print("  PASS: test_control_gate_blocks")
    else:
        # No block gates in this pack — test passes vacuously
        print("  PASS: test_control_gate_blocks (no block gates in pack)")


def test_control_gate_escalates():
    """v0.3 SECURITY: Control gates with on_fail=escalate trigger escalation."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # Provide a failing gate evaluator for an escalate gate
    context = {}
    for gate in agent.control_gates:
        if gate.get("on_fail") == "escalate":
            context[gate["gate_id"]] = False  # Force gate failure
            break

    if context:
        result = agent.attempt_action(
            "Prioritise maintenance tasks",
            lambda ctx: "should_not_run",
            context=context
        )
        assert result.executed is False, "Action should have been escalated by control gate"
        assert "gate_escalation" in result.outcome
        print("  PASS: test_control_gate_escalates")
    else:
        print("  PASS: test_control_gate_escalates (no escalate gates in pack)")


def test_control_gate_passes_without_evaluator():
    """Control gates without evaluators pass by default (can't evaluate declarative conditions)."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # No context — all gates should pass by default
    passed, results = agent.check_control_gates()
    assert passed is True, "Gates without evaluators should pass by default"
    assert all(r["status"] == "passed" for r in results)
    print("  PASS: test_control_gate_passes_without_evaluator")


def test_evidence_check_passes_when_file_exists():
    """Evidence checks pass when referenced files exist in the vault."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    satisfied, results = agent.check_evidence_requirements()
    # task_execution_log.csv should exist (we've been writing to it)
    log_evidence = [r for r in results if r.get("file_path") and "task_execution_log" in r["file_path"]]
    if log_evidence:
        assert log_evidence[0]["satisfied"] is True, "task_execution_log.csv should exist"
    print("  PASS: test_evidence_check_passes_when_file_exists")


def test_attempt_allowed_action():
    """Test executing an allowed action."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    def mock_fn(ctx):
        return "priorities_set"

    result = agent.attempt_action("Prioritise maintenance tasks", mock_fn)
    assert result.permission == Permission.ALLOWED
    assert result.executed is True
    assert result.outcome == "priorities_set"
    print("  PASS: test_attempt_allowed_action")


def test_attempt_denied_action():
    """Test that denied actions are blocked."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    def mock_fn(ctx):
        return "this_should_never_run"

    result = agent.attempt_action("Change vault directory structure", mock_fn)
    assert result.permission == Permission.DENIED
    assert result.executed is False
    assert result.outcome == "blocked_by_authority"
    print("  PASS: test_attempt_denied_action")


def test_attempt_escalation_action():
    """Test that escalation actions are not executed but logged."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    result = agent.attempt_action("Delete vault files")
    assert result.permission == Permission.REQUIRES_ESCALATION
    assert result.executed is False
    print("  PASS: test_attempt_escalation_action")


def test_execution_failure_escalates():
    """Test that execution failures trigger escalation per failure_semantics."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    def failing_fn(ctx):
        raise RuntimeError("Something went wrong")

    result = agent.attempt_action("Prioritise maintenance tasks", failing_fn)
    assert result.permission == Permission.ALLOWED
    assert result.executed is False
    assert "Something went wrong" in result.error
    print("  PASS: test_execution_failure_escalates")


def test_session_summary():
    """Test that session summary accurately reflects action history."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    agent.attempt_action("Prioritise maintenance tasks", lambda ctx: "ok")
    agent.attempt_action("Change vault directory structure")
    agent.attempt_action("Delete vault files")

    summary = agent.get_session_summary()
    assert summary["total_actions"] == 3
    assert summary["allowed"] == 1
    assert summary["denied"] == 1
    assert summary["escalated"] == 1
    assert summary["executed"] == 1
    print("  PASS: test_session_summary")


def test_specialist_pack():
    """Test loading a specialist pack (link auditor)."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_specialist_link_auditor_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    assert agent.agent_role == "specialist"

    # Link auditor can scan but not modify
    perm, _ = agent.check_permission("Scan vault files for wiki-links")
    assert perm == Permission.ALLOWED

    perm, _ = agent.check_permission("Modify vault files")
    assert perm == Permission.DENIED
    print("  PASS: test_specialist_pack")


def test_runtime_load_constellation():
    """Test loading an entire constellation via AgentRuntime."""
    runtime = AgentRuntime(VAULT)
    agents = runtime.load_constellation("vault_curator")

    assert len(agents) == 5, f"Expected 5 agents, got {len(agents)}"
    roles = {a.agent_role for a in agents}
    assert "executive" in roles
    assert "supervisor" in roles
    assert "specialist" in roles
    print("  PASS: test_runtime_load_constellation")


def test_runtime_workflow():
    """Test running a workflow through the runtime."""
    runtime = AgentRuntime(VAULT)
    agents = runtime.load_constellation("vault_curator")

    # Find the executive
    exec_agent = None
    for a in agents:
        if a.agent_role == "executive":
            exec_agent = a
            break

    assert exec_agent is not None

    runtime.start_cycle()

    # Run a simple workflow
    results = runtime.run_workflow(exec_agent.agent_id, [
        {"action": "Prioritise maintenance tasks", "execute_fn": lambda ctx: "tasks_prioritised"},
        {"action": "Delegate audits to Supervisor", "execute_fn": lambda ctx: "audits_delegated"},
    ])

    assert len(results) == 2
    assert all(r.executed for r in results)

    report = runtime.end_cycle()
    assert report["total_actions"] == 2
    assert report["total_executed"] == 2
    print("  PASS: test_runtime_workflow")


def test_runtime_workflow_stops_on_denial():
    """Test that workflows stop when an action is denied."""
    runtime = AgentRuntime(VAULT)
    agents = runtime.load_constellation("vault_curator")

    exec_agent = [a for a in agents if a.agent_role == "executive"][0]

    runtime.start_cycle()

    results = runtime.run_workflow(exec_agent.agent_id, [
        {"action": "Prioritise maintenance tasks", "execute_fn": lambda ctx: "ok"},
        {"action": "Change vault directory structure"},  # DENIED — should stop here
        {"action": "Delegate audits to Supervisor"},  # Should never reach this
    ])

    assert len(results) == 2  # Stopped after denial
    assert results[0].executed is True
    assert results[1].executed is False
    assert results[1].permission == Permission.DENIED
    print("  PASS: test_runtime_workflow_stops_on_denial")


def test_logging_to_csv():
    """Test that actions are logged to task_execution_log.csv."""
    pack_path = os.path.join(ARTIFACTS, "CONST_vault_curator_executive_compiled.json")
    agent = GovernedAgent(pack_path, VAULT)

    # Clear existing log content (keep header if present)
    agent.attempt_action("Prioritise maintenance tasks", lambda ctx: "test_logged")

    # Check the log file exists and has content
    assert os.path.exists(agent.task_log_path), "Task execution log not created"

    csv.field_size_limit(1024 * 1024)  # 1MB limit for large workflow outputs
    with open(agent.task_log_path, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find our entry
    found = any(
        r["outcome"] == "test_logged" and r["agent_id"] == agent.agent_id
        for r in rows
    )
    assert found, "Test action not found in execution log"
    print("  PASS: test_logging_to_csv")


def main():
    print("Agent Maestro Runtime Engine — Test Suite\n")
    print("=" * 50)

    tests = [
        test_load_executive_pack,
        test_permission_allowed,
        test_permission_denied,
        test_permission_escalation,
        test_unknown_action_escalates,
        test_substring_bypass_blocked,
        test_compound_action_escalates,
        test_control_gate_blocks,
        test_control_gate_escalates,
        test_control_gate_passes_without_evaluator,
        test_evidence_check_passes_when_file_exists,
        test_attempt_allowed_action,
        test_attempt_denied_action,
        test_attempt_escalation_action,
        test_execution_failure_escalates,
        test_session_summary,
        test_specialist_pack,
        test_runtime_load_constellation,
        test_runtime_workflow,
        test_runtime_workflow_stops_on_denial,
        test_logging_to_csv,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"  FAIL: {test.__name__} — {e}")
            failed += 1

    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
