"""
AgentRuntime — Manages the lifecycle of GovernedAgents.

Part of Agent Maestro v0.2 Runtime Engine.
Handles init → run → log → shutdown for individual agents and constellation cycles.
"""

import json
import os
from datetime import datetime, timezone
from typing import Optional, Callable

from governed_agent import GovernedAgent, ActionResult


class AgentRuntime:
    """
    Manages the lifecycle of GovernedAgents.

    Responsibilities:
    - Load and instantiate agents from compiled packs
    - Run agent workflows (sequences of actions)
    - Collect and aggregate results
    - Generate cycle reports
    """

    def __init__(self, vault_path: str):
        """
        Initialize the runtime.

        Args:
            vault_path: Root path of the Agent Maestro vault
        """
        self.vault_path = vault_path
        self.agents = {}
        self.cycle_log = []
        self.cycle_start = None
        self.cycle_end = None

    def load_agent(self, compiled_pack_path: str) -> GovernedAgent:
        """
        Load a GovernedAgent from a compiled authority pack.

        Args:
            compiled_pack_path: Path to the compiled pack JSON

        Returns:
            The loaded GovernedAgent instance
        """
        agent = GovernedAgent(compiled_pack_path, self.vault_path)
        self.agents[agent.agent_id] = agent
        return agent

    def load_constellation(self, constellation_name: str) -> list[GovernedAgent]:
        """
        Load all agents for a constellation from the artifacts directory.

        Args:
            constellation_name: Name of the constellation (e.g., 'vault_curator')

        Returns:
            List of loaded GovernedAgent instances
        """
        artifacts_dir = os.path.join(
            self.vault_path,
            "05_SYSTEMS/authority_architecture/compiler/prototype/artifacts"
        )

        agents = []
        prefix = f"CONST_{constellation_name}_"

        for filename in sorted(os.listdir(artifacts_dir)):
            if filename.startswith(prefix) and filename.endswith("_compiled.json"):
                path = os.path.join(artifacts_dir, filename)
                agent = self.load_agent(path)
                agents.append(agent)

        return agents

    def run_action(self, agent_id: str, action: str,
                   execute_fn: Optional[Callable] = None,
                   context: Optional[dict] = None) -> ActionResult:
        """
        Run a single action for a specific agent.

        Args:
            agent_id: The agent's artifact_id
            action: Description of the action
            execute_fn: Optional callable to execute
            context: Optional context dict

        Returns:
            ActionResult
        """
        if agent_id not in self.agents:
            raise ValueError(f"Agent not loaded: {agent_id}")

        agent = self.agents[agent_id]
        result = agent.attempt_action(action, execute_fn, context)
        self.cycle_log.append({
            "agent_id": agent_id,
            "result": result.to_dict(),
        })
        return result

    def run_workflow(self, agent_id: str, actions: list[dict]) -> list[ActionResult]:
        """
        Run a sequence of actions for an agent.

        Each action in the list should be a dict with:
            - 'action': str (description)
            - 'execute_fn': Optional[Callable]
            - 'context': Optional[dict]

        Stops on denied or escalated actions (fail-safe).

        Returns:
            List of ActionResult objects
        """
        results = []
        for action_spec in actions:
            result = self.run_action(
                agent_id,
                action_spec["action"],
                action_spec.get("execute_fn"),
                action_spec.get("context"),
            )
            results.append(result)

            # Stop workflow on denied or escalated actions
            if result.permission.value in ("denied", "requires_escalation"):
                break

        return results

    def start_cycle(self):
        """Mark the start of an execution cycle."""
        self.cycle_start = datetime.now(timezone.utc)
        self.cycle_log = []

    def end_cycle(self) -> dict:
        """
        Mark the end of an execution cycle and generate a report.

        Returns:
            Cycle report dict
        """
        self.cycle_end = datetime.now(timezone.utc)

        # Aggregate results across all agents
        total_actions = 0
        total_allowed = 0
        total_denied = 0
        total_escalated = 0
        total_executed = 0
        agent_summaries = {}

        for agent_id, agent in self.agents.items():
            summary = agent.get_session_summary()
            agent_summaries[agent_id] = summary
            total_actions += summary["total_actions"]
            total_allowed += summary["allowed"]
            total_denied += summary["denied"]
            total_escalated += summary["escalated"]
            total_executed += summary["executed"]

        report = {
            "cycle_start": self.cycle_start.isoformat() if self.cycle_start else None,
            "cycle_end": self.cycle_end.isoformat(),
            "duration_seconds": (self.cycle_end - self.cycle_start).total_seconds() if self.cycle_start else None,
            "agents_loaded": len(self.agents),
            "total_actions": total_actions,
            "total_allowed": total_allowed,
            "total_denied": total_denied,
            "total_escalated": total_escalated,
            "total_executed": total_executed,
            "agent_summaries": agent_summaries,
            "cycle_log": self.cycle_log,
        }

        return report

    def save_cycle_report(self, report: dict, filename: Optional[str] = None):
        """
        Save a cycle report to the execution reports directory.

        Args:
            report: The cycle report dict from end_cycle()
            filename: Optional filename override
        """
        reports_dir = os.path.join(self.vault_path, "06_EXECUTION/reports")
        os.makedirs(reports_dir, exist_ok=True)

        if filename is None:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            filename = f"cycle_report_{timestamp}.json"

        path = os.path.join(reports_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)

        return path

    def shutdown(self):
        """Clean up the runtime."""
        self.agents.clear()
        self.cycle_log.clear()
        self.cycle_start = None
        self.cycle_end = None
