---
schema_version: 2
title: "Tool Registry Design"
type: concept
note_class: architecture
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
    - "[[Tool Registry]]"
    - "[[Execution Adapter Pattern]]"
  part_of:
    - "[[Execution Architecture]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs:
    - "[[Tool Interface]]"
  uses:
    - "[[GovernedAgent]]"
  produces: []
supersedes: []
superseded_by: []
tags:
  - concept
  - architecture
  - tool-registry
  - phase-d
  - v0.4
hash: ""
---

# Tool Registry Design

## Purpose

The Tool Registry is the vault-native, machine-readable catalog of all approved tools in Agent Maestro. It serves as the single source of truth for what tools exist, what permissions they require, what adapters they use, and what their input/output contracts look like.

The registry answers: **What can agents do, through what mechanism, and with what governance?**

## Registry Location

**CSV Registry**: `05_SYSTEMS/runtime/tool_registry.csv`
**Runtime Registry**: `tool_interface.py` → `TOOL_REGISTRY` dict (populated at import via `@register_tool`)

The CSV registry is the authoritative record. The Python `TOOL_REGISTRY` is the runtime implementation. These must stay in sync — any tool added to `tool_interface.py` must also be registered in the CSV.

## Registry Schema

Each tool entry contains:

| Field | Type | Description |
|-------|------|-------------|
| `tool_id` | string | Unique identifier (format: `TOOL.<name>`) |
| `tool_name` | string | Function name in `tool_interface.py` (matches `TOOL_REGISTRY` key) |
| `required_permission` | string | Exact governed action string required in authority pack |
| `description` | string | Human-readable description of what the tool does |
| `adapter` | string | Execution adapter used: `vault_io`, `mcp_client`, `http_client`, `database` |
| `input_schema` | string | Simplified schema of required/optional parameters |
| `output_schema` | string | Simplified schema of ToolResult.data fields |
| `state_change_logged` | boolean | Whether this tool automatically logs state changes |
| `status` | string | `active`, `prototype`, `deprecated` |
| `added_version` | string | Version when the tool was added |

## How the Registry Connects to Governance

The Tool Registry is the bridge between the governance system (authority packs) and the execution system (tool implementations). The connection works through the `required_permission` field:

```
Authority Pack (governed_actions)     Tool Registry              Tool Interface
─────────────────────────────────     ──────────────             ──────────────
"read note" → ALLOWED          ──→   required_permission:       @register_tool(
                                      "read note"          ←──    "read_note",
                                                                   "read note", ...)
```

When a workflow stage executes:

1. The YAML stage defines an `action` string (e.g., "read note") and a `tool` name (e.g., "read_note")
2. `GovernedAgent.attempt_action("read note", execute_fn)` checks if "read note" is in the agent's governed_actions
3. If ALLOWED, `execute_fn` calls `tool_fn(**params)` from the `TOOL_REGISTRY`
4. The tool's `required_permission` in the registry documents this mapping for auditing

This means the Tool Registry serves as an auditable map between governance permissions and runtime capabilities. An authority pack auditor can verify that every tool an agent might call has a corresponding governed_action in the agent's pack.

## Adapter Architecture

Each tool uses an execution adapter — a pattern that abstracts the underlying substrate:

### vault_io (Active)

The Vault I/O adapter is currently implicit in tool implementations. Each tool directly uses Python's `os`, `csv`, `json`, and `yaml` modules to read/write vault files. This works because the vault is a local file system.

### mcp_client (Prototype — v0.4.0)

The MCP Client adapter wraps the Model Context Protocol for communication with external services. An MCP tool implementation:

1. Receives parameters from the Tool Interface (like any other tool)
2. Connects to a configured MCP server (Slack, GitHub, etc.)
3. Calls the appropriate MCP tool with mapped arguments
4. Returns a `ToolResult` with the response data

The MCP adapter adds governance to what would otherwise be ungoverned external calls. The agent cannot call an MCP server directly — it must go through a registered tool with a required permission that its authority pack allows.

### http_client (Planned)

For REST/GraphQL APIs that don't have MCP servers. Same pattern: tool function wraps an HTTP call, returns a `ToolResult`.

### database (Planned)

For structured data queries beyond CSV. Same pattern: tool function wraps a database query, returns rows as `ToolResult.data`.

## Adding a New Tool

To add a new tool to Agent Maestro:

**Step 1: Register in tool_interface.py**

```python
@register_tool("new_tool_name", "required permission string", "Description")
def tool_new_tool_name(vault_path: str, param1: str, **kwargs) -> ToolResult:
    # Implementation
    return ToolResult("new_tool_name", True, data={...})
```

**Step 2: Add to tool_registry.csv**

```csv
TOOL.new_tool_name,new_tool_name,required permission string,Description,vault_io,"{vault_path: str, param1: str}","{...}",false,active,vX.Y.Z
```

**Step 3: Add governed_action to relevant authority packs**

Any agent that needs to use this tool must have the permission string in its `governed_actions` list with `permission: allowed`.

**Step 4: Update workflow YAML if needed**

If the tool is used in a workflow, add a stage that references it:

```yaml
- stage_id: my_stage
  agent_pack: specialist.something
  action: "required permission string"
  tool: new_tool_name
  tool_params:
    param1: "value"
```

## Validation Rules

The following invariants must hold for the Tool Registry to be valid:

1. Every entry in `TOOL_REGISTRY` (Python) has a corresponding row in `tool_registry.csv`
2. Every `required_permission` in the registry corresponds to at least one `governed_action` in at least one authority pack
3. No two tools share the same `tool_id`
4. No two tools share the same `tool_name`
5. Every tool with `state_change_logged: true` actually calls `_log_state_change()` in its implementation
6. Every tool with adapter `mcp_client` has a corresponding MCP server configuration

## Future: Tool Capability Discovery

In future versions, the Tool Registry could support capability discovery — agents could query "what tools are available for adapter X?" or "what tools require permission Y?" This would enable dynamic workflow construction where the Reasoning Layer selects tools based on available capabilities rather than hard-coded YAML stage definitions.

This is explicitly deferred to post-v0.4.0 as it requires the self-observation and evolution constellations to be operational.

## Related Documents

- [[Execution Architecture]] — `02_KNOWLEDGE/concepts/Execution Architecture.md`
- [[Tool Interface]] — `05_SYSTEMS/runtime/tool_interface.py`
- [[GovernedAgent]] — `05_SYSTEMS/runtime/governed_agent.py`
- [[Authority Architecture]] — `05_SYSTEMS/authority_architecture/Authority Architecture.md`
