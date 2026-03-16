#!/usr/bin/env python3
"""
Agent Maestro Orchestrator — CLI for running constellation cycles.

Part of Agent Maestro v0.2 Runtime Engine (Upgrade 3.4).
Provides a command-line interface for loading constellations,
running audit/maintenance cycles, and generating reports.

Usage:
    # List available constellations
    python orchestrator.py list --vault-root /path/to/vault

    # Run a full cycle for a constellation
    python orchestrator.py run vault_maintenance --vault-root /path/to/vault

    # Run a single agent from a constellation
    python orchestrator.py run-agent vault_maintenance supervisor --vault-root /path/to/vault

    # Show status of compiled packs
    python orchestrator.py status --vault-root /path/to/vault
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure runtime modules are importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_runtime import AgentRuntime
from governed_agent import GovernedAgent, Permission
from state_change_logger import StateChangeLogger
from workflow_engine import WorkflowEngine, WorkflowStatus
from escalation_processor import EscalationProcessor


def find_vault_root(start_path: str = None) -> Path:
    """Walk up directories to find vault root (has 01_CAPTURE)."""
    if start_path:
        path = Path(start_path).resolve()
        if (path / "01_CAPTURE").exists():
            return path

    path = Path.cwd()
    while path != path.parent:
        if (path / "01_CAPTURE").exists():
            return path
        path = path.parent

    return None


def get_artifacts_dir(vault_root: Path) -> Path:
    """Return the compiled artifacts directory."""
    return vault_root / "05_SYSTEMS" / "authority_architecture" / "compiler" / "prototype" / "artifacts"


def get_available_constellations(vault_root: Path) -> dict:
    """Scan compiled artifacts to find available constellations."""
    artifacts_dir = get_artifacts_dir(vault_root)
    constellations = {}

    if not artifacts_dir.exists():
        return constellations

    for f in sorted(artifacts_dir.glob("CONST_*_compiled.json")):
        with open(f, 'r', encoding='utf-8') as fh:
            pack = json.load(fh)
        constellation = pack["compiled_from"]["constellation"]
        role = pack["compiled_from"]["agent_role"]
        pack_id = pack["compiled_from"]["pack_id"]

        if constellation not in constellations:
            constellations[constellation] = {"agents": []}

        constellations[constellation]["agents"].append({
            "pack_id": pack_id,
            "role": role,
            "artifact_file": f.name,
            "compiled_at": pack.get("compiled_at", "unknown"),
        })

    return constellations


def get_executive_packs(vault_root: Path) -> list:
    """Scan compiled artifacts to find executive-layer packs."""
    artifacts_dir = get_artifacts_dir(vault_root)
    executives = []

    if not artifacts_dir.exists():
        return executives

    for f in sorted(artifacts_dir.glob("EXEC_*_compiled.json")):
        with open(f, 'r', encoding='utf-8') as fh:
            pack = json.load(fh)
        executives.append({
            "pack_id": pack["compiled_from"]["pack_id"],
            "pack_name": pack["compiled_from"]["pack_name"],
            "role": pack["compiled_from"]["agent_role"],
            "artifact_file": f.name,
        })

    return executives


# ── Commands ──────────────────────────────────────────────────


def cmd_list(args):
    """List available constellations and executive agents."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    print(f"Agent Maestro Orchestrator")
    print(f"Vault: {vault_root}")
    print()

    # Executive Layer
    executives = get_executive_packs(vault_root)
    if executives:
        print("Executive Layer:")
        print("-" * 60)
        for ex in executives:
            print(f"  {ex['pack_id']:<45} {ex['role']}")
        print()

    # Constellations
    constellations = get_available_constellations(vault_root)
    if constellations:
        print("Constellations:")
        print("-" * 60)
        for name, data in constellations.items():
            agent_count = len(data["agents"])
            roles = [a["role"] for a in data["agents"]]
            role_summary = ", ".join(sorted(set(roles)))
            print(f"  {name:<30} {agent_count} agents ({role_summary})")
        print()
    else:
        print("No compiled constellations found.")
        print("Run the compiler first to produce artifacts.")


def cmd_status(args):
    """Show detailed status of all compiled packs."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    artifacts_dir = get_artifacts_dir(vault_root)

    # Read compiler registry
    registry_path = vault_root / "05_SYSTEMS" / "authority_architecture" / "compiler" / "compiler_artifacts_registry.csv"

    print(f"Agent Maestro Orchestrator — Status")
    print(f"Vault: {vault_root}")
    print()

    if registry_path.exists():
        print("Compiler Artifacts Registry:")
        print("-" * 80)
        with open(registry_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"  {row.get('pack_id', 'unknown'):<50} {row.get('status', 'unknown'):<10} {row.get('compiled_date', 'unknown')}")
    else:
        print("No compiler registry found.")

    print()

    # Count artifacts
    if artifacts_dir.exists():
        json_files = list(artifacts_dir.glob("*_compiled.json"))
        print(f"Compiled Artifacts: {len(json_files)}")
        for f in sorted(json_files):
            size = f.stat().st_size
            print(f"  {f.name:<65} {size:>6} bytes")
    else:
        print("No artifacts directory found.")

    # Check log files
    print()
    print("Execution Logs:")
    print("-" * 60)
    log_dir = vault_root / "06_EXECUTION" / "logs"
    if log_dir.exists():
        for log_file in sorted(log_dir.glob("*.csv")):
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = sum(1 for _ in f) - 1  # subtract header
            print(f"  {log_file.name:<45} {max(0, lines):>5} entries")


def cmd_run(args):
    """Run a full cycle for a constellation."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    constellation_name = args.constellation
    dry_run = args.dry_run

    print(f"Agent Maestro Orchestrator — Run Cycle")
    print(f"Vault:         {vault_root}")
    print(f"Constellation: {constellation_name}")
    print(f"Mode:          {'DRY RUN' if dry_run else 'LIVE'}")
    print()

    # Initialize runtime
    runtime = AgentRuntime(str(vault_root))
    runtime.start_cycle()

    # Load constellation agents
    agents = runtime.load_constellation(constellation_name)
    if not agents:
        print(f"Error: No compiled packs found for constellation '{constellation_name}'.")
        print("Run the compiler first.")
        sys.exit(1)

    print(f"Loaded {len(agents)} agents:")
    for agent in agents:
        print(f"  {agent.agent_id:<55} ({agent.agent_role})")
    print()

    # Sort agents by role hierarchy: executive > supervisor > specialist
    role_order = {"executive": 0, "supervisor": 1, "specialist": 2}
    agents_sorted = sorted(agents, key=lambda a: role_order.get(a.agent_role, 99))

    # Run health check — each agent checks their own permissions
    print("Running authority health check...")
    print("-" * 60)
    for agent in agents_sorted:
        # Each agent verifies their key actions
        actions = list(agent.governed_actions.keys())[:3]  # Check first 3 actions
        for action_name in actions:
            permission, conditions = agent.check_permission(action_name)
            status = "OK" if permission == Permission.ALLOWED else permission.value.upper()
            print(f"  [{status:<22}] {agent.agent_role:<12} | {action_name[:50]}")
    print()

    if dry_run:
        print("DRY RUN complete. No actions executed.")
    elif args.execute:
        # Execute workflows via the workflow engine
        print("Executing workflows via Workflow Engine...")
        print("=" * 60)
        engine = WorkflowEngine(str(vault_root), runtime)
        engine.agents_by_pack_fragment = {}
        # Re-index agents for the engine
        for agent in agents:
            pack_id = agent.pack["compiled_from"]["pack_id"]
            engine.agents_by_pack_fragment[pack_id] = agent
            parts = pack_id.split(".")
            for i in range(1, len(parts)):
                fragment = ".".join(parts[i:])
                if fragment not in engine.agents_by_pack_fragment:
                    engine.agents_by_pack_fragment[fragment] = agent

        # Bootstrap evidence files for first run
        bootstrapped = engine.bootstrap_evidence()
        if bootstrapped:
            print(f"Bootstrapped {len(bootstrapped)} evidence files:")
            for path in bootstrapped:
                print(f"    + {path}")
            print()

        # Load and execute all workflows for this constellation
        workflows = engine.load_all_workflows()
        constellation_workflows = [w for w in workflows if w.constellation == constellation_name]

        if not constellation_workflows:
            print(f"No workflow definitions found for {constellation_name}.")
            print(f"Add YAML files to 05_SYSTEMS/runtime/workflows/")
        else:
            for wf_def in constellation_workflows:
                print(f"\n  Workflow: {wf_def.workflow_name}")
                print(f"  Stages:   {len(wf_def.stages)}")
                print(f"  {'-' * 50}")

                status, context = engine.execute(wf_def.workflow_id)
                report = engine.get_workflow_report(status, context)

                # Print stage results
                for sid, sresult in context.stage_results.items():
                    icon = {"completed": "✓", "skipped": "→", "failed": "✗",
                            "escalated": "⚠", "blocked": "⊘"}.get(sresult.status.value, "?")
                    print(f"    {icon} {sresult.stage_name:<40} [{sresult.status.value}]")

                print(f"\n  Result:  {status.value.upper()}")
                print(f"  Stages:  {report['stages_completed']} completed, "
                      f"{report['stages_skipped']} skipped, "
                      f"{report['stages_failed']} failed, "
                      f"{report['stages_escalated']} escalated")

                if context.escalations:
                    print(f"  Escalations: {len(context.escalations)}")
                    for esc in context.escalations:
                        print(f"    → {esc['reason'][:60]}")

                # Save workflow report
                report_name = f"workflow_{wf_def.workflow_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                report_dir = os.path.join(str(vault_root), "06_EXECUTION", "reports")
                os.makedirs(report_dir, exist_ok=True)
                report_path = os.path.join(report_dir, report_name)
                with open(report_path, 'w', encoding='utf-8') as rf:
                    json.dump(report, rf, indent=2, default=str)
                print(f"  Report:  {report_path}")
    else:
        print("Authority checks passed. Agents are ready for workflow execution.")
        print("Use --execute to run workflows, or --dry-run for authority check only.")

    # End cycle and generate report
    report = runtime.end_cycle()
    report_path = runtime.save_cycle_report(
        report, f"cycle_{constellation_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    print(f"\nCycle report saved: {report_path}")

    runtime.shutdown()


def cmd_run_agent(args):
    """Run a specific agent from a constellation."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    constellation_name = args.constellation
    agent_role = args.agent_role

    print(f"Agent Maestro Orchestrator — Run Agent")
    print(f"Vault:         {vault_root}")
    print(f"Constellation: {constellation_name}")
    print(f"Agent Role:    {agent_role}")
    print()

    # Find the matching compiled artifact
    artifacts_dir = get_artifacts_dir(vault_root)
    prefix = f"CONST_{constellation_name}_"

    matching_file = None
    for f in sorted(artifacts_dir.glob(f"{prefix}*_compiled.json")):
        with open(f, 'r', encoding='utf-8') as fh:
            pack = json.load(fh)
        if pack["compiled_from"]["agent_role"] == agent_role:
            matching_file = f
            break
        # Also match by partial pack_id
        if agent_role in pack["compiled_from"]["pack_id"]:
            matching_file = f
            break

    if not matching_file:
        print(f"Error: No compiled pack found for {constellation_name}/{agent_role}")
        sys.exit(1)

    # Load and inspect
    runtime = AgentRuntime(str(vault_root))
    agent = runtime.load_agent(str(matching_file))

    print(f"Agent:     {agent.agent_name}")
    print(f"Agent ID:  {agent.agent_id}")
    print(f"Role:      {agent.agent_role}")
    print()

    print("Governed Actions:")
    print("-" * 60)
    for action_name, action_def in agent.governed_actions.items():
        perm = action_def["permission"].value
        print(f"  [{perm:<22}] {action_name}")

    print()
    print("Rules:")
    for rule in agent.rules:
        print(f"  {rule['rule_id']}: {rule['description']}")

    print()
    print("Escalation Path:")
    escalates_to = agent.escalation.get("escalates_to", "unknown")
    print(f"  Escalates to: {escalates_to}")
    for condition in agent.escalation.get("escalation_conditions", []):
        print(f"  - {condition}")

    runtime.shutdown()


def cmd_compile(args):
    """Compile all packs for a constellation (convenience wrapper)."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    constellation_name = args.constellation
    packs_dir = vault_root / "05_SYSTEMS" / "authority_architecture" / "packs" / "constellation_packs" / constellation_name
    compiler_path = vault_root / "05_SYSTEMS" / "authority_architecture" / "compiler" / "prototype" / "compiler.py"

    if not packs_dir.exists():
        print(f"Error: Packs directory not found: {packs_dir}")
        sys.exit(1)

    if not compiler_path.exists():
        print(f"Error: Compiler not found: {compiler_path}")
        sys.exit(1)

    print(f"Compiling packs for {constellation_name}...")
    os.system(f"python3 {compiler_path} {packs_dir} --vault-root {vault_root}")


def cmd_review(args):
    """Show pending escalations and optionally generate a review queue."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    proc = EscalationProcessor(str(vault_root))

    print(f"Agent Maestro Orchestrator — Escalation Review")
    print(f"Vault: {vault_root}")
    print()

    if args.generate_queue:
        queue_path = proc.generate_review_queue()
        print(f"Review queue generated: {queue_path}")
        print()

    grouped = proc.get_pending_grouped()
    pending_total = sum(len(v) for v in grouped.values())

    if not grouped:
        print("No pending escalations.")
        return

    print(f"Pending Escalations: {pending_total}")
    print("=" * 70)

    for recipient, escalations in sorted(grouped.items()):
        print(f"\n  Escalated To: {recipient} ({len(escalations)} pending)")
        print(f"  {'-' * 60}")
        for esc in escalations:
            esc_id = esc.get("escalation_id", "?")
            action = esc.get("action", "unknown")[:45]
            agent = esc.get("agent_id", "unknown").split(".")[-2] if "." in esc.get("agent_id", "") else esc.get("agent_role", "?")
            reason = esc.get("reason", "")[:50]
            print(f"    {esc_id}  {agent:<15} {action}")
            if reason:
                print(f"              Reason: {reason}")


def cmd_approve(args):
    """Approve a pending escalation."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    proc = EscalationProcessor(str(vault_root))
    escalation_id = args.escalation_id.upper()
    notes = args.notes or ""

    detail = proc.get_escalation_detail(escalation_id)
    if not detail:
        print(f"Error: Escalation {escalation_id} not found.")
        sys.exit(1)

    if detail.get("status") != "pending":
        print(f"Error: Escalation {escalation_id} is already {detail['status']}.")
        sys.exit(1)

    print(f"Approving: {escalation_id}")
    print(f"  Action:  {detail.get('action', 'unknown')}")
    print(f"  Agent:   {detail.get('agent_id', 'unknown')}")
    print(f"  Reason:  {detail.get('reason', 'unknown')}")

    result = proc.resolve(escalation_id, "approved", reviewer="human_operator", notes=notes)
    if result:
        print(f"\n  ✓ {escalation_id} approved.")
    else:
        print(f"\n  ✗ Failed to approve {escalation_id}.")


def cmd_reject(args):
    """Reject a pending escalation."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    proc = EscalationProcessor(str(vault_root))
    escalation_id = args.escalation_id.upper()
    notes = args.notes or ""

    detail = proc.get_escalation_detail(escalation_id)
    if not detail:
        print(f"Error: Escalation {escalation_id} not found.")
        sys.exit(1)

    if detail.get("status") != "pending":
        print(f"Error: Escalation {escalation_id} is already {detail['status']}.")
        sys.exit(1)

    print(f"Rejecting: {escalation_id}")
    print(f"  Action:  {detail.get('action', 'unknown')}")
    print(f"  Agent:   {detail.get('agent_id', 'unknown')}")
    print(f"  Reason:  {detail.get('reason', 'unknown')}")

    result = proc.resolve(escalation_id, "rejected", reviewer="human_operator", notes=notes)
    if result:
        print(f"\n  ✗ {escalation_id} rejected.")
    else:
        print(f"\n  ✗ Failed to reject {escalation_id}.")


def cmd_dashboard(args):
    """Show escalation dashboard summary."""
    vault_root = find_vault_root(args.vault_root)
    if not vault_root:
        print("Error: Could not find vault root. Use --vault-root.")
        sys.exit(1)

    proc = EscalationProcessor(str(vault_root))
    summary = proc.get_dashboard_summary()

    print(f"Agent Maestro Orchestrator — Escalation Dashboard")
    print(f"Vault: {vault_root}")
    print(f"Generated: {summary['generated_at']}")
    print()

    print(f"  Total Escalations:  {summary['total_escalations']}")
    print(f"  Pending:            {summary['pending']}")
    print(f"  Approved:           {summary['approved']}")
    print(f"  Rejected:           {summary['rejected']}")
    print()

    if summary["by_constellation"]:
        print("  By Constellation:")
        for const, count in sorted(summary["by_constellation"].items()):
            print(f"    {const:<30} {count}")
        print()

    if summary["by_recipient"]:
        print("  By Recipient:")
        for recipient, count in sorted(summary["by_recipient"].items()):
            print(f"    {recipient:<40} {count}")
        print()

    if summary["top_actions"]:
        print("  Top Escalated Actions:")
        for action, count in summary["top_actions"]:
            print(f"    {count:>3}x  {action[:55]}")
        print()

    if summary["recent_pending"]:
        print("  Recent Pending:")
        for esc in summary["recent_pending"][:5]:
            print(f"    {esc['escalation_id']}  {esc['action'][:45]}")
    print()

    if args.save_report:
        report_path = proc.generate_dashboard_report()
        print(f"  Dashboard report saved: {report_path}")


# ── Main ──────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Agent Maestro Orchestrator — CLI for running constellation cycles",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--vault-root", default=None,
        help="Root directory of the Agent Maestro vault (auto-detected if not set)"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Common argument for all subparsers
    vault_root_kwargs = {"--vault-root": {"default": None, "help": "Root directory of the Agent Maestro vault"}}

    # list
    sub_list = subparsers.add_parser("list", help="List available constellations and executives")
    sub_list.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_list.set_defaults(func=cmd_list)

    # status
    sub_status = subparsers.add_parser("status", help="Show detailed status of compiled packs and logs")
    sub_status.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_status.set_defaults(func=cmd_status)

    # run
    sub_run = subparsers.add_parser("run", help="Run a full cycle for a constellation")
    sub_run.add_argument("constellation", help="Constellation name (e.g., vault_maintenance)")
    sub_run.add_argument("--dry-run", action="store_true", help="Check authority only, don't execute")
    sub_run.add_argument("--execute", action="store_true", help="Execute workflows via the workflow engine")
    sub_run.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_run.set_defaults(func=cmd_run)

    # run-agent
    sub_agent = subparsers.add_parser("run-agent", help="Inspect/run a specific agent")
    sub_agent.add_argument("constellation", help="Constellation name")
    sub_agent.add_argument("agent_role", help="Agent role or pack_id fragment")
    sub_agent.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_agent.set_defaults(func=cmd_run_agent)

    # compile
    sub_compile = subparsers.add_parser("compile", help="Compile all packs for a constellation")
    sub_compile.add_argument("constellation", help="Constellation name")
    sub_compile.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_compile.set_defaults(func=cmd_compile)

    # review
    sub_review = subparsers.add_parser("review", help="Show pending escalations")
    sub_review.add_argument("--generate-queue", action="store_true", help="Generate markdown review queue")
    sub_review.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_review.set_defaults(func=cmd_review)

    # approve
    sub_approve = subparsers.add_parser("approve", help="Approve a pending escalation")
    sub_approve.add_argument("escalation_id", help="Escalation ID (e.g., ESC-0001)")
    sub_approve.add_argument("--notes", default="", help="Approval notes")
    sub_approve.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_approve.set_defaults(func=cmd_approve)

    # reject
    sub_reject = subparsers.add_parser("reject", help="Reject a pending escalation")
    sub_reject.add_argument("escalation_id", help="Escalation ID (e.g., ESC-0001)")
    sub_reject.add_argument("--notes", default="", help="Rejection notes")
    sub_reject.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_reject.set_defaults(func=cmd_reject)

    # dashboard
    sub_dashboard = subparsers.add_parser("dashboard", help="Show escalation dashboard")
    sub_dashboard.add_argument("--save-report", action="store_true", help="Save dashboard as JSON report")
    sub_dashboard.add_argument("--vault-root", **vault_root_kwargs["--vault-root"])
    sub_dashboard.set_defaults(func=cmd_dashboard)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
