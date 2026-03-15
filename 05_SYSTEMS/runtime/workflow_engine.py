"""
Workflow Engine — Executes pipeline definitions through governed agents.

Part of Agent Maestro v0.3 Runtime Engine (Phase B — C2/C3/C4).

Loads YAML workflow definitions from 05_SYSTEMS/runtime/workflows/,
maps stages to agent actions via the tool interface, executes them
in sequence with result aggregation and conditional branching.

Architecture:
    WorkflowDefinition  — Parsed YAML with stages, agents, and branching rules
    WorkflowStage       — Single stage: agent + tool + parameters + next
    WorkflowContext      — Accumulates results across stages, provides context
    WorkflowEngine       — Loads definitions, maps agents, executes stages
    WorkflowResult       — Final outcome of a workflow execution

Usage:
    engine = WorkflowEngine(vault_path)
    engine.load_agents("vault_maintenance")
    result = engine.execute("scheduled_audit_cycle")
"""

import json
import os
import sys
import yaml
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable, Optional

# Ensure sibling imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from governed_agent import GovernedAgent, Permission, ActionResult
from agent_runtime import AgentRuntime
from tool_interface import get_tool, ToolResult, TOOL_REGISTRY


class StageStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    SKIPPED = "skipped"
    FAILED = "failed"
    ESCALATED = "escalated"
    BLOCKED = "blocked"
    PAUSED = "paused"  # Waiting for escalation resolution


class WorkflowStatus(Enum):
    NOT_STARTED = "not_started"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"  # Waiting for escalation resolution
    ABORTED = "aborted"


class StageResult:
    """Result of executing a single workflow stage."""

    def __init__(self, stage_id: str, stage_name: str, agent_id: str,
                 status: StageStatus, tool_result: ToolResult = None,
                 action_result: ActionResult = None,
                 data: Any = None, error: str = None):
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.agent_id = agent_id
        self.status = status
        self.tool_result = tool_result
        self.action_result = action_result
        self.data = data
        self.error = error
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "stage_id": self.stage_id,
            "stage_name": self.stage_name,
            "agent_id": self.agent_id,
            "status": self.status.value,
            "data": self.data,
            "error": self.error,
            "tool_result": self.tool_result.to_dict() if self.tool_result else None,
            "action_result": self.action_result.to_dict() if self.action_result else None,
            "timestamp": self.timestamp,
        }


class WorkflowContext:
    """
    Execution context that accumulates results across workflow stages.

    Stages can read outputs from previous stages via this context.
    Supports conditional branching by evaluating conditions against
    accumulated data.
    """

    def __init__(self, workflow_id: str, vault_path: str):
        self.workflow_id = workflow_id
        self.vault_path = vault_path
        self.stage_results: dict[str, StageResult] = {}
        self.shared_data: dict[str, Any] = {}
        self.escalations: list[dict] = []
        self.started_at = datetime.now(timezone.utc).isoformat()
        self.ended_at = None

    def record_stage(self, result: StageResult):
        """Record the result of a stage execution."""
        self.stage_results[result.stage_id] = result
        if result.data:
            self.shared_data[result.stage_id] = result.data

    def get_stage_data(self, stage_id: str) -> Any:
        """Get the output data from a previous stage."""
        return self.shared_data.get(stage_id)

    def get_stage_result(self, stage_id: str) -> Optional[StageResult]:
        """Get the full result from a previous stage."""
        return self.stage_results.get(stage_id)

    def add_escalation(self, stage_id: str, agent_id: str, reason: str,
                       escalates_to: str):
        """Record an escalation raised during workflow execution."""
        self.escalations.append({
            "stage_id": stage_id,
            "agent_id": agent_id,
            "reason": reason,
            "escalates_to": escalates_to,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "pending",
        })

    def evaluate_condition(self, condition: dict) -> bool:
        """
        Evaluate a branching condition against accumulated context.

        Condition format:
            {"field": "stage_id.data_key", "operator": "eq|ne|gt|lt|contains|exists", "value": ...}
            {"field": "stage_id.status", "operator": "eq", "value": "completed"}
            {"any_escalations": true}  — True if any escalations have been raised
        """
        if not condition:
            return True

        # Special conditions
        if condition.get("any_escalations"):
            return len(self.escalations) > 0
        if condition.get("no_escalations"):
            return len(self.escalations) == 0

        field = condition.get("field", "")
        operator = condition.get("operator", "eq")
        expected = condition.get("value")

        # Parse field: "stage_id.data_key" or "stage_id.status"
        parts = field.split(".", 1)
        if len(parts) != 2:
            return False

        stage_id, key = parts

        if key == "status":
            result = self.stage_results.get(stage_id)
            actual = result.status.value if result else None
        elif key == "success":
            result = self.stage_results.get(stage_id)
            actual = result.tool_result.success if result and result.tool_result else None
        else:
            data = self.shared_data.get(stage_id)
            if isinstance(data, dict):
                actual = data.get(key)
            else:
                actual = None

        # Evaluate operator
        if operator == "eq":
            return actual == expected
        elif operator == "ne":
            return actual != expected
        elif operator == "gt":
            return actual is not None and actual > expected
        elif operator == "lt":
            return actual is not None and actual < expected
        elif operator == "gte":
            return actual is not None and actual >= expected
        elif operator == "contains":
            return expected in actual if actual else False
        elif operator == "exists":
            return actual is not None
        else:
            return False

    def to_dict(self) -> dict:
        return {
            "workflow_id": self.workflow_id,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "stages_completed": sum(1 for r in self.stage_results.values()
                                    if r.status == StageStatus.COMPLETED),
            "stages_total": len(self.stage_results),
            "escalations": self.escalations,
            "stage_results": {k: v.to_dict() for k, v in self.stage_results.items()},
        }


class WorkflowDefinition:
    """
    A parsed workflow definition loaded from YAML.

    YAML format:
        workflow_id: str
        workflow_name: str
        constellation: str
        description: str
        stages:
          - stage_id: str
            name: str
            agent_pack: str  (pack_id fragment, e.g., "supervisor" or "specialist.definition_alignment")
            action: str  (the governed action to attempt)
            tool: str  (tool_interface tool name)
            tool_params: dict  (parameters passed to the tool)
            on_success: str  (next stage_id, or "end")
            on_failure: str  (stage_id to jump to, or "escalate", or "abort")
            on_escalation: str  (stage_id or "pause")
            condition: dict  (optional — only run this stage if condition is met)
            collect_as: str  (optional — key under which to store this stage's output in context)
    """

    def __init__(self, data: dict):
        self.workflow_id = data["workflow_id"]
        self.workflow_name = data.get("workflow_name", self.workflow_id)
        self.constellation = data["constellation"]
        self.description = data.get("description", "")
        self.entry_stage = data.get("entry_stage")

        self.stages: dict[str, dict] = {}
        for stage_def in data.get("stages", []):
            sid = stage_def["stage_id"]
            self.stages[sid] = stage_def
            if self.entry_stage is None:
                self.entry_stage = sid  # First stage is entry by default

    @classmethod
    def from_file(cls, path: str) -> "WorkflowDefinition":
        """Load a workflow definition from a YAML file."""
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls(data)

    def get_stage(self, stage_id: str) -> Optional[dict]:
        return self.stages.get(stage_id)

    def get_stage_ids(self) -> list[str]:
        return list(self.stages.keys())


class WorkflowEngine:
    """
    Executes workflow definitions through governed agents using the tool interface.

    The engine:
    1. Loads a workflow definition (YAML)
    2. Resolves agent_pack references to loaded GovernedAgent instances
    3. Executes stages in order, using attempt_action() for governance
    4. Calls the appropriate tool for each stage
    5. Aggregates results in a WorkflowContext
    6. Handles conditional branching and escalation pauses
    """

    def __init__(self, vault_path: str, runtime: AgentRuntime = None):
        self.vault_path = vault_path
        self.runtime = runtime or AgentRuntime(vault_path)
        self.workflows_dir = os.path.join(vault_path, "05_SYSTEMS", "runtime", "workflows")
        self.definitions: dict[str, WorkflowDefinition] = {}
        self.agents_by_pack_fragment: dict[str, GovernedAgent] = {}

    def bootstrap_evidence(self):
        """
        Bootstrap evidence infrastructure for all loaded agents.

        Creates empty evidence files (CSVs with headers, empty JSON reports)
        that are required by evidence_requirements in compiled packs.
        This resolves the chicken-and-egg problem on first run: agents need
        evidence files to exist, but evidence comes from running agents.

        Safe to call multiple times — only creates files that don't exist.
        """
        bootstrapped = []
        for agent in self.agents_by_pack_fragment.values():
            evidence_reqs = agent.governance.get("evidence_requirements", [])
            for req in evidence_reqs:
                fmt = req.get("format", "")
                if not fmt:
                    continue
                # Extract vault-relative file paths from format string
                for token in fmt.replace(",", " ").split():
                    if "/" in token and ("." in token.split("/")[-1]):
                        full_path = os.path.join(self.vault_path, token)
                        if not os.path.exists(full_path):
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)
                            if token.endswith(".csv"):
                                # Create empty CSV with a minimal header
                                with open(full_path, 'w', encoding='utf-8') as f:
                                    f.write("timestamp,agent_id,status,details\n")
                            elif token.endswith(".json"):
                                # Create empty JSON report skeleton
                                with open(full_path, 'w', encoding='utf-8') as f:
                                    json.dump({
                                        "report_type": "bootstrap",
                                        "created_at": datetime.now(timezone.utc).isoformat(),
                                        "note": "Bootstrapped empty evidence file for first run",
                                        "data": {}
                                    }, f, indent=2)
                            bootstrapped.append(token)
                        break  # Only first path per requirement
        return bootstrapped

    def load_agents(self, constellation_name: str):
        """Load all agents for a constellation and index them by pack_id fragment."""
        agents = self.runtime.load_constellation(constellation_name)
        for agent in agents:
            pack_id = agent.pack["compiled_from"]["pack_id"]
            # Index by full pack_id and by useful fragments
            self.agents_by_pack_fragment[pack_id] = agent

            # Also index by the last segment(s) for convenience
            # e.g., "CONST.vault_maintenance.specialist.definition_alignment" →
            #   "specialist.definition_alignment", "definition_alignment"
            parts = pack_id.split(".")
            for i in range(1, len(parts)):
                fragment = ".".join(parts[i:])
                if fragment not in self.agents_by_pack_fragment:
                    self.agents_by_pack_fragment[fragment] = agent
        return agents

    def _resolve_agent(self, agent_pack: str) -> Optional[GovernedAgent]:
        """Resolve an agent_pack reference to a loaded GovernedAgent."""
        if agent_pack in self.agents_by_pack_fragment:
            return self.agents_by_pack_fragment[agent_pack]

        # Try case-insensitive partial match
        agent_pack_lower = agent_pack.lower()
        for key, agent in self.agents_by_pack_fragment.items():
            if agent_pack_lower in key.lower():
                return agent

        return None

    def load_workflow(self, workflow_id: str) -> WorkflowDefinition:
        """Load a workflow definition from the workflows directory."""
        path = os.path.join(self.workflows_dir, f"{workflow_id}.yaml")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Workflow definition not found: {path}")
        defn = WorkflowDefinition.from_file(path)
        self.definitions[defn.workflow_id] = defn
        return defn

    def load_all_workflows(self) -> list[WorkflowDefinition]:
        """Load all workflow definitions from the workflows directory."""
        loaded = []
        if not os.path.isdir(self.workflows_dir):
            return loaded
        for fn in sorted(os.listdir(self.workflows_dir)):
            if fn.endswith(".yaml"):
                try:
                    defn = WorkflowDefinition.from_file(os.path.join(self.workflows_dir, fn))
                    self.definitions[defn.workflow_id] = defn
                    loaded.append(defn)
                except Exception:
                    pass
        return loaded

    def execute(self, workflow_id: str, initial_params: dict = None,
                max_stages: int = 50) -> tuple[WorkflowStatus, WorkflowContext]:
        """
        Execute a loaded workflow definition.

        Args:
            workflow_id: The workflow to execute
            initial_params: Optional initial parameters merged into tool_params
            max_stages: Safety limit on number of stages to prevent infinite loops

        Returns:
            (WorkflowStatus, WorkflowContext)
        """
        if workflow_id not in self.definitions:
            self.load_workflow(workflow_id)

        defn = self.definitions[workflow_id]
        context = WorkflowContext(workflow_id, self.vault_path)
        current_stage_id = defn.entry_stage
        stages_executed = 0

        while current_stage_id and current_stage_id != "end" and stages_executed < max_stages:
            stage_def = defn.get_stage(current_stage_id)
            if stage_def is None:
                return WorkflowStatus.FAILED, context

            stages_executed += 1

            # Check stage condition
            condition = stage_def.get("condition")
            if condition and not context.evaluate_condition(condition):
                # Skip this stage
                skip_result = StageResult(
                    stage_id=current_stage_id,
                    stage_name=stage_def.get("name", current_stage_id),
                    agent_id="",
                    status=StageStatus.SKIPPED,
                    data={"reason": "condition_not_met"},
                )
                context.record_stage(skip_result)
                # Move to next stage (on_success path since skip is not failure)
                current_stage_id = stage_def.get("on_success", "end")
                continue

            # Execute the stage
            stage_result = self._execute_stage(stage_def, context, initial_params)
            context.record_stage(stage_result)

            # Determine next stage based on result
            if stage_result.status == StageStatus.COMPLETED:
                current_stage_id = stage_def.get("on_success", "end")
            elif stage_result.status == StageStatus.ESCALATED:
                context.add_escalation(
                    stage_id=current_stage_id,
                    agent_id=stage_result.agent_id,
                    reason=stage_result.error or "Action requires escalation",
                    escalates_to=stage_def.get("escalates_to", "unknown"),
                )
                on_esc = stage_def.get("on_escalation", "pause")
                if on_esc == "pause":
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.PAUSED, context
                elif on_esc == "abort":
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.ABORTED, context
                else:
                    current_stage_id = on_esc
            elif stage_result.status == StageStatus.BLOCKED:
                on_fail = stage_def.get("on_failure", "abort")
                if on_fail == "abort":
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.FAILED, context
                elif on_fail == "escalate":
                    context.add_escalation(
                        stage_id=current_stage_id,
                        agent_id=stage_result.agent_id,
                        reason=stage_result.error or "Stage blocked",
                        escalates_to=stage_def.get("escalates_to", "unknown"),
                    )
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.PAUSED, context
                else:
                    current_stage_id = on_fail
            elif stage_result.status == StageStatus.FAILED:
                on_fail = stage_def.get("on_failure", "abort")
                if on_fail == "abort":
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.FAILED, context
                elif on_fail == "escalate":
                    context.add_escalation(
                        stage_id=current_stage_id,
                        agent_id=stage_result.agent_id,
                        reason=stage_result.error or "Stage execution failed",
                        escalates_to=stage_def.get("escalates_to", "unknown"),
                    )
                    context.ended_at = datetime.now(timezone.utc).isoformat()
                    return WorkflowStatus.PAUSED, context
                else:
                    current_stage_id = on_fail
            else:
                # Unexpected status
                context.ended_at = datetime.now(timezone.utc).isoformat()
                return WorkflowStatus.FAILED, context

        context.ended_at = datetime.now(timezone.utc).isoformat()

        if stages_executed >= max_stages:
            return WorkflowStatus.ABORTED, context

        return WorkflowStatus.COMPLETED, context

    def _execute_stage(self, stage_def: dict, context: WorkflowContext,
                       initial_params: dict = None) -> StageResult:
        """
        Execute a single workflow stage.

        Steps:
        1. Resolve the agent from agent_pack reference
        2. Build tool parameters (merge stage params + context + initial params)
        3. Call attempt_action() on the agent with a tool-executing function
        4. Return StageResult
        """
        stage_id = stage_def["stage_id"]
        stage_name = stage_def.get("name", stage_id)
        agent_pack = stage_def.get("agent_pack", "")
        action = stage_def.get("action", stage_name)
        tool_name = stage_def.get("tool")

        # Resolve agent
        agent = self._resolve_agent(agent_pack)
        if agent is None:
            return StageResult(
                stage_id=stage_id,
                stage_name=stage_name,
                agent_id=f"unresolved:{agent_pack}",
                status=StageStatus.FAILED,
                error=f"Could not resolve agent for pack: {agent_pack}",
            )

        # Build tool parameters
        tool_params = dict(stage_def.get("tool_params", {}))

        # Merge initial_params (from workflow execution call)
        if initial_params:
            for k, v in initial_params.items():
                if k not in tool_params:
                    tool_params[k] = v

        # Inject context data references: values like "${stage_id.key}" get resolved
        tool_params = self._resolve_param_refs(tool_params, context)

        # Always provide vault_path
        tool_params["vault_path"] = self.vault_path

        # Build the tool execution function
        if tool_name and tool_name in TOOL_REGISTRY:
            tool_entry = TOOL_REGISTRY[tool_name]
            tool_fn = tool_entry["function"]

            def execute_fn(ctx):
                result = tool_fn(**tool_params)
                return result.to_dict() if result else None
        else:
            # No tool — just a governance check (useful for approval stages)
            execute_fn = None

        # Execute through governance
        action_result = agent.attempt_action(action, execute_fn, context=None)

        # Determine stage status from action result
        if action_result.permission == Permission.ALLOWED and action_result.executed:
            status = StageStatus.COMPLETED
            # Extract tool result data
            data = None
            tool_result_obj = None
            if action_result.outcome and action_result.outcome != "action_permitted_no_fn":
                try:
                    parsed = json.loads(action_result.outcome.replace("'", '"')) if isinstance(action_result.outcome, str) else action_result.outcome
                    if isinstance(parsed, dict):
                        data = parsed.get("data")
                        tool_result_obj = ToolResult(
                            tool_name=tool_name or "",
                            success=parsed.get("success", True),
                            data=data,
                        )
                except (json.JSONDecodeError, AttributeError):
                    data = action_result.outcome

            # If the tool was executed directly and returned a ToolResult
            if execute_fn and not tool_result_obj:
                # The outcome is the string repr of the ToolResult dict
                try:
                    if isinstance(action_result.outcome, str):
                        outcome_dict = eval(action_result.outcome)  # Safe: we control the content
                        if isinstance(outcome_dict, dict):
                            data = outcome_dict.get("data")
                            tool_result_obj = ToolResult(
                                tool_name=outcome_dict.get("tool_name", ""),
                                success=outcome_dict.get("success", True),
                                data=data,
                            )
                            if not outcome_dict.get("success"):
                                status = StageStatus.FAILED
                except Exception:
                    data = action_result.outcome

            return StageResult(
                stage_id=stage_id,
                stage_name=stage_name,
                agent_id=agent.agent_id,
                status=status,
                tool_result=tool_result_obj,
                action_result=action_result,
                data=data,
            )

        elif action_result.permission == Permission.DENIED:
            return StageResult(
                stage_id=stage_id,
                stage_name=stage_name,
                agent_id=agent.agent_id,
                status=StageStatus.BLOCKED,
                action_result=action_result,
                error=f"Action denied: {action_result.conditions}",
            )

        elif action_result.permission == Permission.REQUIRES_ESCALATION:
            return StageResult(
                stage_id=stage_id,
                stage_name=stage_name,
                agent_id=agent.agent_id,
                status=StageStatus.ESCALATED,
                action_result=action_result,
                error=f"Escalation required: {action_result.conditions}",
            )

        else:
            # Execution failure (permission was allowed but execution raised an exception)
            return StageResult(
                stage_id=stage_id,
                stage_name=stage_name,
                agent_id=agent.agent_id,
                status=StageStatus.FAILED,
                action_result=action_result,
                error=action_result.error or action_result.outcome,
            )

    def _resolve_param_refs(self, params: dict, context: WorkflowContext) -> dict:
        """
        Resolve parameter references like "${stage_id.key}" against context.

        Example:
            tool_params:
              dir_path: "${audit_init.scope}"

        Would look up context.shared_data["audit_init"]["scope"].
        """
        resolved = {}
        for key, value in params.items():
            if isinstance(value, str) and value.startswith("${") and value.endswith("}"):
                ref = value[2:-1]
                parts = ref.split(".", 1)
                if len(parts) == 2:
                    stage_data = context.get_stage_data(parts[0])
                    if isinstance(stage_data, dict):
                        resolved[key] = stage_data.get(parts[1], value)
                    else:
                        resolved[key] = value
                else:
                    resolved[key] = value
            elif isinstance(value, dict):
                resolved[key] = self._resolve_param_refs(value, context)
            else:
                resolved[key] = value
        return resolved

    def get_workflow_report(self, status: WorkflowStatus,
                           context: WorkflowContext) -> dict:
        """Generate a comprehensive workflow execution report."""
        return {
            "workflow_id": context.workflow_id,
            "status": status.value,
            "started_at": context.started_at,
            "ended_at": context.ended_at,
            "stages_completed": sum(1 for r in context.stage_results.values()
                                    if r.status == StageStatus.COMPLETED),
            "stages_skipped": sum(1 for r in context.stage_results.values()
                                  if r.status == StageStatus.SKIPPED),
            "stages_failed": sum(1 for r in context.stage_results.values()
                                 if r.status in (StageStatus.FAILED, StageStatus.BLOCKED)),
            "stages_escalated": sum(1 for r in context.stage_results.values()
                                    if r.status == StageStatus.ESCALATED),
            "escalations": context.escalations,
            "stage_results": {k: v.to_dict() for k, v in context.stage_results.items()},
        }
