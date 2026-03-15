---
schema_version: 2
title: "Execution Architecture"
type: concept
note_class: architecture
domain: agent_maestro
layer: knowledge
scope: runtime
canonical: true
authority_weight: 80
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
    - "[[Execution Layer Model]]"
    - "[[Execution Adapter Pattern]]"
  part_of:
    - "[[Agent Maestro — Layer Model Map]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs:
    - "[[Tool Interface]]"
    - "[[Workflow Engine]]"
  uses:
    - "[[GovernedAgent]]"
    - "[[Authority Pack]]"
  produces:
    - "[[Tool Registry]]"
    - "[[Self-Observation Specification]]"
supersedes: []
superseded_by: []
tags:
  - concept
  - architecture
  - execution
  - phase-d
  - v0.4
hash: ""
---

# Execution Architecture

## Purpose

This document formalizes the execution architecture of Agent Maestro — the layered model that governs how agent reasoning translates into real-world effects. It defines the complete path from an LLM's decision to act, through governance mediation and tool execution, to observable changes in the vault or external systems.

The execution architecture answers the fundamental question: **How does a governed agent safely do things?**

## The Three-Layer Execution Model

Agent Maestro's execution follows a strict three-layer model. Each layer has a single responsibility and a defined interface to the layers above and below it.

```
┌─────────────────────────────────────────────────────┐
│                  REASONING LAYER                     │
│                                                      │
│  LLM (Claude/GPT/etc.) decides what to do based on  │
│  authority pack, workflow stage, and vault context.   │
│                                                      │
│  Output: action intent + parameters                  │
└───────────────┬─────────────────────────────────────┘
                │  action intent
                ▼
┌─────────────────────────────────────────────────────┐
│              GOVERNANCE MEDIATION LAYER               │
│                                                      │
│  GovernedAgent.attempt_action() pipeline:             │
│    1. Permission check (exact match)                 │
│    2. Control gate enforcement                       │
│    3. Evidence requirement validation                │
│    4. Execute (if all pass) or escalate/block        │
│                                                      │
│  Output: ActionResult (executed / denied / escalated)│
└───────────────┬─────────────────────────────────────┘
                │  governed tool call
                ▼
┌─────────────────────────────────────────────────────┐
│              TOOL EXECUTION LAYER                     │
│                                                      │
│  Tool Interface → Execution Adapter → External World │
│                                                      │
│  Tool Interface: 9 registered tools with schemas     │
│  Execution Adapters: vault I/O, CSV, JSON, future    │
│  External World: files, APIs, MCP servers, etc.      │
│                                                      │
│  Output: ToolResult (success/failure + data)         │
└─────────────────────────────────────────────────────┘
```

### Layer 1: Reasoning Layer

The Reasoning Layer is where intelligence lives. This is the LLM (or any reasoning system) that decides *what* to do based on its authority pack, the current workflow stage, and accumulated context.

The Reasoning Layer does not interact with the external world directly. It produces **action intents** — structured declarations of what it wants to do and with what parameters. These intents are expressed as calls to `attempt_action()` with a governed action string and a tool-executing function.

**Inputs to the Reasoning Layer:**

| Input | Source | Purpose |
|-------|--------|---------|
| Compiled authority pack | `05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/` | Defines what the agent is allowed to do |
| Workflow stage definition | YAML in `05_SYSTEMS/runtime/workflows/` | Defines what the agent should do now |
| WorkflowContext | Previous stage results, shared_data | Accumulated context from prior stages |
| Vault state | Read via tool_interface.read_note, scan_directory | Current state of the vault |

**Outputs from the Reasoning Layer:**

| Output | Type | Consumed By |
|--------|------|-------------|
| Action string | `str` — exact governed action name | GovernedAgent.check_permission() |
| Execute function | `callable` — wraps a tool call | GovernedAgent.attempt_action() |
| Tool parameters | `dict` — tool_params from YAML or dynamic | Tool Interface functions |

**Key constraint:** The Reasoning Layer never bypasses governance. There is no code path from reasoning to external effect that does not pass through `attempt_action()`.

### Layer 2: Governance Mediation Layer

The Governance Mediation Layer is the enforcement boundary. Every action intent from Layer 1 must pass through the four-stage governance pipeline in `GovernedAgent.attempt_action()`:

1. **Permission check** — Exact string match against the `governed_actions` index from the compiled authority pack. Unknown actions fail-safe to `REQUIRES_ESCALATION`.

2. **Control gate enforcement** — Evaluates pre-conditions defined in the authority pack. Each gate has an `on_fail` policy: `block` (hard stop), `escalate` (pause for human review), or `log_and_continue` (proceed with audit trail).

3. **Evidence requirement validation** — Checks that required evidence files exist before execution. Missing evidence triggers escalation. The `bootstrap_evidence()` method in WorkflowEngine handles first-run initialization.

4. **Execute or route** — If all checks pass and an `execute_fn` is provided, the function is called. Results are captured as `ActionResult`. If any check fails, the action is routed to denial, escalation, or blocking.

**Mediation outcomes:**

| Outcome | Permission | Executed | Next Step |
|---------|-----------|----------|-----------|
| COMPLETED | ALLOWED | True | Tool ran, result captured |
| BLOCKED | DENIED | False | Action forbidden by authority pack |
| ESCALATED | REQUIRES_ESCALATION | False | Logged to escalation_log.csv, workflow paused |
| GATE_BLOCKED | DENIED | False | Control gate failed with on_fail=block |
| GATE_ESCALATED | REQUIRES_ESCALATION | False | Control gate failed with on_fail=escalate |
| EVIDENCE_MISSING | REQUIRES_ESCALATION | False | Required evidence file not found |
| EXECUTION_FAILED | ALLOWED | False | Tool raised an exception |

### Layer 3: Tool Execution Layer

The Tool Execution Layer contains the actual implementations that interact with the vault and, in the future, the external world. It is subdivided into three tiers:

#### Tier 3a: Tool Interface

The Tool Interface (`05_SYSTEMS/runtime/tool_interface.py`) provides the approved set of operations. Each tool is a Python function registered via the `@register_tool` decorator with a name, a required permission string, and a description.

Current registered tools (v0.3.2):

| Tool | Required Permission | Purpose |
|------|-------------------|---------|
| `read_note` | "read note" | Read vault note content + frontmatter |
| `write_note` | "write note" | Write/update vault notes |
| `scan_directory` | "scan directory" | List files in a vault directory |
| `validate_frontmatter` | "validate frontmatter" | Check frontmatter against schema v2 |
| `scan_links` | "scan links" | Audit wiki-links for broken targets |
| `generate_report` | "write execution reports" | Write CSV/JSON reports to 06_EXECUTION |
| `move_note` | "move note" | Move notes between vault locations |
| `read_registry` | "read registry" | Read CSV registry files |
| `append_registry` | "write to registry" | Append rows to CSV registries |

Each tool returns a `ToolResult` with `success`, `data`, `error`, and `artifacts` fields. Tools are stateless — they receive all context as parameters.

#### Tier 3b: Execution Adapters

Execution Adapters are the bridge between the Tool Interface and the actual substrate — the systems that tools operate on. Currently, the only adapter is the **Vault I/O Adapter** (implicit in tool implementations), which translates tool calls into file system operations within the vault.

The adapter pattern exists to support future expansion to external systems without changing the Tool Interface contract:

| Adapter | Status | Substrate | Used By |
|---------|--------|-----------|---------|
| Vault I/O | **Active** (implicit) | Local file system | All 9 current tools |
| MCP Client | **Planned** | Model Context Protocol servers | External integrations (Slack, APIs) |
| HTTP Client | **Planned** | REST/GraphQL APIs | External service calls |
| Database | **Planned** | SQLite / PostgreSQL | Structured data beyond CSV |

When an external integration tool is added (e.g., `send_slack_message`), it will be registered in the Tool Interface with its own required permission, but its implementation will call through an MCP Client Adapter rather than performing vault I/O.

#### Tier 3c: External World

The External World is everything outside Agent Maestro's governance boundary. This includes the local file system (where the vault lives), MCP servers, REST APIs, databases, and any other system an agent might need to interact with.

**Key principle:** Agents never interact with the External World directly. Every interaction passes through Tool Interface → Execution Adapter → External World, with governance mediation above. This creates a single, auditable path for all side effects.

## Data Flow

The complete data flow for a governed tool execution:

```
WorkflowEngine.execute()
  │
  ├─ load stage definition from YAML
  ├─ resolve agent from agent_pack reference
  ├─ build tool_params (merge stage params + context refs + initial params)
  │
  └─ agent.attempt_action(action_string, execute_fn)
       │
       ├─ check_permission(action) → exact match against governed_actions
       ├─ check_control_gates(context) → evaluate gate conditions
       ├─ check_evidence_requirements() → verify evidence files exist
       │
       └─ execute_fn(context)
            │
            └─ tool_fn(**tool_params)
                 │
                 ├─ Vault I/O: os.path / open() / csv / json / yaml
                 ├─ _log_state_change() → state_change_log.csv
                 │
                 └─ return ToolResult(success, data, error, artifacts)
```

## Execution Boundaries

### What Agents Can Execute

Agents can only execute actions that satisfy ALL of the following:

1. The action string exactly matches a `governed_action` in the agent's compiled pack with permission `ALLOWED`
2. All control gates in the agent's pack pass (or have `on_fail: log_and_continue`)
3. All required evidence files exist
4. The action maps to a registered tool in the Tool Interface
5. The tool's `required_permission` matches the action being attempted

### What Agents Cannot Execute

1. Arbitrary code — there is no `exec()` or `eval()` path from agent reasoning to execution (the `eval()` in `_execute_stage` operates only on tool result strings generated internally)
2. Unregistered tools — only tools in `TOOL_REGISTRY` can be called
3. Direct file I/O — agents access the vault only through tool functions
4. External API calls — no adapter exists yet (planned for G3)
5. Actions not in their authority pack — fail-safe to REQUIRES_ESCALATION

## State and Observability

Every execution produces observable side effects that are logged:

| Log | Path | What It Captures |
|-----|------|-----------------|
| Task Execution Log | `06_EXECUTION/logs/task_execution_log.csv` | Every `attempt_action()` call: agent, action, permission, outcome |
| Escalation Log | `06_EXECUTION/logs/escalation_log.csv` | Every escalation: agent, action, reason, recipient, status |
| State Change Log | `06_EXECUTION/logs/state_change_log.csv` | Every vault modification: type, path, before/after, justification |
| Workflow Reports | `06_EXECUTION/reports/` | Stage-by-stage workflow execution results (JSON) |

The `tool_interface.py` module-level `_log_state_change()` function ensures that all tool operations that modify the vault are automatically logged. This is mandatory — state change logging cannot be bypassed by tools.

## Integration Points

### Current Integration (v0.3.2)

The execution architecture currently operates as a closed system within the vault:

```
Orchestrator CLI → WorkflowEngine → GovernedAgent → Tool Interface → Vault I/O → File System
```

### Future Integration (v0.4.0+)

The execution adapter pattern enables future integration without changing the governance model:

```
Orchestrator CLI ─┬→ WorkflowEngine → GovernedAgent → Tool Interface ─┬→ Vault I/O → File System
                  │                                                    ├→ MCP Client → Slack/APIs
                  │                                                    ├→ HTTP Client → REST APIs
                  │                                                    └→ DB Adapter → SQLite/PG
                  │
                  └→ Host Binding Layer → Claude Code / Python daemon / n8n / hybrid
```

The Host Binding Layer (see [[Host Bindings]]) manages the association between compiled governance artifacts and the runtime environment where agents actually execute. This is where the "how does the LLM get invoked?" question is answered — see the Host Options Evaluation (G4) for the analysis.

## Design Decisions

### Why Three Layers (Not Two or Four)?

Two layers (reasoning + execution) would collapse governance into either the reasoning layer (LLM decides its own permissions — unsafe) or the execution layer (every tool checks permissions — redundant, inconsistent). Three layers cleanly separate concerns: intelligence (Layer 1), safety (Layer 2), capability (Layer 3).

Four layers would split the Tool Execution Layer into separate "tool selection" and "tool execution" layers. This adds complexity without benefit — tool selection is already handled by the workflow YAML stage definitions, and the `@register_tool` pattern handles the mapping.

### Why Exact Permission Matching?

The v0.2 runtime used substring matching for permissions, which created a security vulnerability: a compound action string like "read note and delete files" would match against "read note" and bypass the denial on "delete files." v0.3 hardened this to exact string matching only. Unknown actions fail-safe to REQUIRES_ESCALATION.

### Why Stateless Tools?

Tools receive all context as parameters and return all results as `ToolResult` objects. They hold no state between calls. This makes tools testable in isolation, composable in workflows, and safe to retry — a failed tool call has no side effects beyond what the state change logger captured.

### Why Module-Level State Logging?

State change logging is implemented at the module level in `tool_interface.py` rather than injected per-agent. This ensures that ALL tool operations are logged regardless of which agent called them. The logger is initialized on first use and shared across all tool calls. Logging failures are silently caught — state logging never blocks tool execution.

## Related Documents

- [[GovernedAgent]] — `05_SYSTEMS/runtime/governed_agent.py`
- [[Tool Interface]] — `05_SYSTEMS/runtime/tool_interface.py`
- [[Workflow Engine]] — `05_SYSTEMS/runtime/workflow_engine.py`
- [[Host Bindings]] — `05_SYSTEMS/authority_architecture/compiler/Host Bindings.md`
- [[Agent Maestro — Principles]] — `02_KNOWLEDGE/governance/Agent Maestro — Principles.md`
- [[Tool Registry]] — `05_SYSTEMS/runtime/tool_registry.csv` (created in G2)
- [[Self-Observation Specification]] — `02_KNOWLEDGE/concepts/Self-Observation Specification.md` (created in G5)
- [[Host Options Evaluation]] — `02_KNOWLEDGE/references/Host Options Evaluation.md` (created in G4)
