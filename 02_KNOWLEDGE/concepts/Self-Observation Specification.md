---
schema_version: 2
title: "Self-Observation Specification"
type: concept
note_class: specification
domain: agent_maestro
layer: knowledge
scope: runtime
canonical: true
authority_weight: 75
resolution_basis: authority_weight
status: active
review_status: approved
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: ai_authored
relationships:
  defines:
    - "[[Self-Observation Framework]]"
    - "[[Agent Performance Metrics]]"
  part_of:
    - "[[Execution Architecture]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  uses:
    - "[[GovernedAgent]]"
    - "[[Workflow Engine]]"
    - "[[State Change Logger]]"
  produces:
    - "[[Observation Log]]"
supersedes: []
superseded_by: []
tags:
  - concept
  - specification
  - self-observation
  - evolution
  - phase-d
  - v0.4
hash: ""
---

# Self-Observation Specification

## Purpose

This specification defines what agents should observe and log about their own performance, the format of observation data, and how that data feeds into future improvement. Self-observation is the foundation for the Evolution Constellation (deferred to Wave 5+) — without systematic performance data, the system cannot identify bottlenecks, measure improvement, or evolve.

Self-observation answers: **How well is the system working, and where should it improve?**

## Design Principles

1. **Observation is passive** — Self-observation collects data; it does not change behavior. Analysis and improvement are separate concerns (Evolution Constellation).
2. **Minimal overhead** — Observation logging must not measurably slow tool execution. All observation writes are non-blocking.
3. **Vault-native storage** — Observation data lives in the vault as CSV/JSON files, consistent with all other operational data.
4. **Built on existing logs** — Self-observation extends (does not replace) the task execution log, escalation log, and state change log.
5. **Privacy-aware** — Observation data logs actions and metrics, never content. A self-observation log entry records *that* an agent read a note and how long it took, not *what* the note contained.

## What Agents Should Observe

### Category 1: Action Metrics

These metrics are captured per `attempt_action()` call. They extend the existing task_execution_log.csv with timing and classification data.

| Metric | Type | Captured At | Description |
|--------|------|------------|-------------|
| `action_duration_ms` | int | attempt_action() | Wall-clock time from permission check through execution |
| `permission_check_ms` | int | check_permission() | Time spent in permission lookup |
| `gate_check_ms` | int | check_control_gates() | Time spent evaluating control gates |
| `evidence_check_ms` | int | check_evidence_requirements() | Time spent validating evidence |
| `tool_execution_ms` | int | execute_fn() | Time spent in the actual tool call |
| `action_category` | str | attempt_action() | Classification: read / write / scan / validate / report / move / external |
| `result_size_bytes` | int | tool result | Size of the ToolResult.data payload |

### Category 2: Workflow Metrics

These metrics are captured per workflow execution. They extend the workflow report JSON with performance data.

| Metric | Type | Captured At | Description |
|--------|------|------------|-------------|
| `workflow_duration_ms` | int | WorkflowEngine.execute() | Total wall-clock time for the entire workflow |
| `stages_completed` | int | WorkflowContext | Number of stages that completed successfully |
| `stages_skipped` | int | WorkflowContext | Number of stages skipped due to conditions |
| `stages_escalated` | int | WorkflowContext | Number of stages that triggered escalation |
| `stages_failed` | int | WorkflowContext | Number of stages that failed |
| `escalation_rate` | float | computed | stages_escalated / stages_total |
| `success_rate` | float | computed | stages_completed / (stages_total - stages_skipped) |
| `bottleneck_stage` | str | computed | Stage with the longest tool_execution_ms |
| `data_volume_bytes` | int | WorkflowContext | Total size of all shared_data accumulated |

### Category 3: Error Patterns

These metrics track error frequency and patterns to identify systemic issues.

| Metric | Type | Captured At | Description |
|--------|------|------------|-------------|
| `error_type` | str | attempt_action() on failure | Classification: permission_denied / gate_blocked / evidence_missing / tool_error / unknown_action |
| `error_action` | str | attempt_action() | The action string that caused the error |
| `error_agent` | str | GovernedAgent | Which agent encountered the error |
| `error_recoverable` | bool | failure_semantics | Whether the error was handled by retry or escalation |
| `consecutive_errors` | int | session tracking | Number of consecutive errors by the same agent |

### Category 4: Escalation Patterns

These metrics analyze escalation behavior to distinguish healthy governance from systemic misconfiguration.

| Metric | Type | Captured At | Description |
|--------|------|------------|-------------|
| `escalation_reason_category` | str | escalation_log | Classification: unknown_action / gate_failure / evidence_missing / execution_failure |
| `escalation_resolution_time` | int (hours) | escalation_processor | Time from escalation raised to resolution |
| `escalation_resolution` | str | escalation_processor | approved / rejected |
| `repeat_escalation` | bool | computed | Same agent + same action escalated more than once |
| `escalation_density` | float | computed | escalations per workflow execution |

### Category 5: Vault Health Indicators

These metrics are derived from periodic vault scans rather than real-time execution.

| Metric | Type | Captured By | Description |
|--------|------|------------|-------------|
| `total_notes` | int | scan_directory | Total vault note count |
| `broken_links_count` | int | scan_links | Number of broken wiki-links |
| `frontmatter_compliance_rate` | float | validate_frontmatter | Percentage of notes with valid schema v2 frontmatter |
| `capture_inbox_count` | int | scan_directory | Notes remaining in 01_CAPTURE |
| `orphan_notes_count` | int | link analysis | Notes with no incoming wiki-links |
| `average_authority_weight` | float | frontmatter scan | Mean authority_weight across all notes |

## Observation Log Format

### observation_log.csv

The primary observation log is a CSV file at `06_EXECUTION/logs/observation_log.csv`.

**Schema:**

```csv
timestamp,session_id,agent_id,constellation,observation_type,metric_name,metric_value,metric_unit,context
```

| Field | Type | Description |
|-------|------|-------------|
| `timestamp` | ISO 8601 | When the observation was recorded |
| `session_id` | string | Build session or daemon run ID (e.g., SES-010) |
| `agent_id` | string | Agent that produced the observation |
| `constellation` | string | Agent's constellation |
| `observation_type` | string | Category: action / workflow / error / escalation / vault_health |
| `metric_name` | string | Specific metric (e.g., action_duration_ms, escalation_rate) |
| `metric_value` | string | The observed value (stored as string, typed by metric_name) |
| `metric_unit` | string | Unit: ms, bytes, count, rate, boolean |
| `context` | string | Additional context (workflow_id, stage_id, action_name) |

### Example Entries

```csv
2026-03-15T14:30:00Z,SES-010,CONST.vault_maintenance.specialist.definition_alignment,vault_maintenance,action,action_duration_ms,1247,ms,scan_directory:02_KNOWLEDGE
2026-03-15T14:30:01Z,SES-010,CONST.vault_maintenance.specialist.definition_alignment,vault_maintenance,action,tool_execution_ms,1198,ms,scan_directory
2026-03-15T14:35:00Z,SES-010,CONST.vault_maintenance.supervisor,vault_maintenance,workflow,workflow_duration_ms,300000,ms,scheduled_audit_cycle
2026-03-15T14:35:00Z,SES-010,CONST.vault_maintenance.supervisor,vault_maintenance,workflow,escalation_rate,0.167,rate,scheduled_audit_cycle
2026-03-15T14:35:01Z,SES-010,system,system,vault_health,broken_links_count,3,count,weekly_scan
```

## Implementation Plan

### Phase 1: Instrument GovernedAgent (v0.5.0)

Add timing instrumentation to `attempt_action()` in `governed_agent.py`:

```python
def attempt_action(self, action, execute_fn=None, context=None):
    start = time.monotonic()

    # Existing permission check
    perm_start = time.monotonic()
    permission, conditions = self.check_permission(action)
    perm_ms = int((time.monotonic() - perm_start) * 1000)

    # ... existing logic ...

    # After execution
    total_ms = int((time.monotonic() - start) * 1000)

    # Log observation (non-blocking)
    self._observe("action", "action_duration_ms", total_ms, "ms", action)
    self._observe("action", "permission_check_ms", perm_ms, "ms", action)
```

The `_observe()` method appends to `observation_log.csv` with try/except (non-blocking, same pattern as state change logging).

### Phase 2: Instrument WorkflowEngine (v0.5.0)

Add timing to `WorkflowEngine.execute()` and per-stage tracking:

```python
def execute(self, workflow_id, ...):
    start = time.monotonic()
    # ... existing logic ...
    total_ms = int((time.monotonic() - start) * 1000)
    self._observe_workflow(workflow_id, context, total_ms)
```

### Phase 3: Vault Health Scanner (v0.5.0)

Add a new tool `observe_vault_health` to tool_interface.py that runs a comprehensive vault scan and writes observations:

```python
@register_tool("observe_vault_health", "scan directory", "Run vault health metrics scan")
def tool_observe_vault_health(vault_path, **kwargs):
    # Count notes, broken links, frontmatter compliance, etc.
    # Write results to observation_log.csv
```

### Phase 4: Observation Dashboard (v0.6.0)

Create a dashboard in `06_EXECUTION/dashboards/` that reads observation_log.csv and produces a summary report. This would be consumed by the future Evolution Constellation to identify improvement opportunities.

## How Self-Observation Feeds Evolution

The self-observation data is designed to answer specific questions that the Evolution Constellation (Wave 5+) will need:

| Question | Observation Data Source | Expected Action |
|----------|----------------------|-----------------|
| Which stages are slowest? | action_duration_ms, bottleneck_stage | Optimize tool implementations |
| Which actions escalate most? | escalation_density, repeat_escalation | Adjust authority packs or add new governed_actions |
| Are agents failing repeatedly? | consecutive_errors, error_type | Fix bugs or retrain workflows |
| Is vault health improving? | broken_links_count, frontmatter_compliance_rate | Adjust maintenance frequency |
| Are escalations being resolved? | escalation_resolution_time | Improve human review workflow |

The Evolution Constellation would read observation_log.csv, identify patterns, and propose improvements — which would themselves go through the governance pipeline (escalation for changes to authority packs or system architecture).

## Non-Goals

This specification explicitly does NOT cover:

- **Content logging** — What a note contains is not observed; only that it was read/written and how long it took
- **Automated improvement** — Self-observation collects data; automated improvement is a separate system (Evolution Constellation)
- **Real-time alerting** — Observations are logged for batch analysis, not streamed to alert systems
- **User behavior tracking** — Only agent behavior is observed; human session activity is not logged
- **Model performance benchmarking** — Comparing LLM models is a separate concern (Model Router, deferred)

## Related Documents

- [[Execution Architecture]] — `02_KNOWLEDGE/concepts/Execution Architecture.md`
- [[GovernedAgent]] — `05_SYSTEMS/runtime/governed_agent.py`
- [[Workflow Engine]] — `05_SYSTEMS/runtime/workflow_engine.py`
- [[State Change Logger]] — `05_SYSTEMS/runtime/state_change_logger.py`
- [[Agent Maestro — Principles]] — `02_KNOWLEDGE/governance/Agent Maestro — Principles.md`
