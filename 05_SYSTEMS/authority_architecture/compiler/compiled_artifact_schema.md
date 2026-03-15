---
schema_version: 2
title: "Compiled Authority Pack — Artifact Format"
status: active
created_date: 2026-03-15
last_modified: 2026-03-15
tags:
  - schema
  - authority-architecture
  - compiler
  - reference
relationships:
  defines: "Compiled authority pack JSON format"
  part_of: "[[Agent Maestro — Authority Architecture]]"
  applies_to: "All compiled JSON artifacts in compiler/prototype/artifacts/"
authority_weight: 70
---

# Compiled Authority Pack — Artifact Format

This document defines the JSON format of compiled authority pack artifacts produced by the 8-stage compiler pipeline. Every JSON file in `05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/` conforms to this schema.

## Top-Level Structure

```json
{
  "artifact_id": "string — Unique identifier: compiled.{pack_id}.v{version}",
  "compiled_from": { ... },
  "compiled_at": "string — ISO 8601 timestamp",
  "compiler_version": "string — Semantic version of the compiler",
  "compilation_report": { ... },
  "governance": { ... }
}
```

## `compiled_from` — Source Pack Metadata

```json
{
  "pack_id": "string — Authority pack identifier (e.g., CONST.vault_maintenance.supervisor)",
  "pack_name": "string — Human-readable pack name",
  "pack_version": "string — Semantic version",
  "parent_pack_id": "string — Pack this inherits from (empty string if root)",
  "constellation": "string — Constellation name (e.g., vault_maintenance)",
  "agent_role": "string — One of: executive, supervisor, specialist"
}
```

## `compilation_report` — Build Provenance

```json
{
  "stages_passed": ["string — Names of compiler stages that passed"],
  "inheritance_chain": ["string — Pack IDs from root to this pack"],
  "overrides_applied": ["string — Human-readable override descriptions"],
  "warnings": ["string — Compiler warnings (if any)"]
}
```

The eight compiler stages are:

1. `input_validation` — Validates YAML structure and required fields
2. `inheritance_resolution` — Resolves the full inheritance chain
3. `override_application` — Merges parent governance with child overrides
4. `policy_resolution` — Resolves permission conflicts (child wins)
5. `completeness_validation` — Ensures all required governance sections exist
6. `artifact_generation` — Generates the compiled JSON artifact
7. `host_binding` — Binds the artifact to its host constellation
8. `output_registration` — Registers the artifact in `compiler_artifacts_registry.csv`

## `governance` — The Runtime Governance Contract

This is the section loaded by `GovernedAgent` at runtime.

### `governance.authority_type`

String. One of: `root`, `delegation`, `operational`. Defines the level of authority granted to this agent.

### `governance.scope`

```json
{
  "domain": "string — Primary domain (e.g., vault_maintenance)",
  "boundaries": ["string — Human-readable boundary descriptions"]
}
```

### `governance.governed_entities`

Array of strings describing what this agent is authorized to manage.

### `governance.governed_actions`

Array of action definitions. This is the core permission set checked by `GovernedAgent.check_permission()`.

```json
[
  {
    "action": "string — The exact action name (case-insensitive match at runtime)",
    "permission": "string — One of: allowed, denied, requires_escalation",
    "conditions": "string — Human-readable conditions for this permission"
  }
]
```

**Permission matching** at runtime uses exact, case-insensitive string comparison. Unknown actions (not in this list) fail-safe to `requires_escalation`.

### `governance.rules`

Array of governance rules the agent must follow.

```json
[
  {
    "rule_id": "string — Unique rule identifier (e.g., R1, R2)",
    "description": "string — Human-readable rule description"
  }
]
```

### `governance.control_gates`

Array of pre-execution gates that must pass before action execution.

```json
[
  {
    "gate_id": "string — Unique gate identifier",
    "condition": "string — Human-readable gate condition",
    "on_fail": "string — One of: block, escalate, log_and_continue"
  }
]
```

At runtime, gates are evaluated via context-provided evaluator functions keyed by `gate_id`. Gates without evaluators pass by default (open-world assumption).

### `governance.evidence_requirements`

Array of evidence that must exist before the agent can operate.

```json
[
  {
    "evidence_type": "string — Description of the evidence",
    "required": "boolean — Whether this evidence is mandatory",
    "format": "string — Expected format, may include vault-relative file paths"
  }
]
```

At runtime, the system extracts vault-relative file paths from the `format` field and checks file existence. Missing required evidence triggers `requires_escalation`.

### `governance.escalation`

Defines the escalation path for this agent.

```json
{
  "escalates_to": "string — Pack ID of the agent to escalate to",
  "escalation_conditions": ["string — Conditions that trigger escalation"]
}
```

### `governance.failure_semantics`

Defines behavior on execution failures.

```json
{
  "on_execution_failure": "string — One of: escalate, retry, log_and_continue",
  "max_retries": "integer (optional) — Maximum retry count"
}
```

## Naming Convention

Compiled artifact files follow this pattern:

```
{TIER}_{constellation}_{role}_compiled.json
```

Where `TIER` is `EXEC` for executive-layer packs and `CONST` for constellation packs. Specialist packs include the specialist name:

```
CONST_vault_maintenance_specialist_definition_alignment_compiled.json
```

## Registry

All compiled artifacts are tracked in `compiler_artifacts_registry.csv` with columns: `pack_id`, `artifact_id`, `artifact_file`, `compiled_date`, `compiler_version`, `stages_passed`, `status`.
