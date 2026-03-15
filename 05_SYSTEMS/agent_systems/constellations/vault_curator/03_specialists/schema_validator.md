---
id: CONST.vault_curator.agent.specialist.schema_validator
type: agent_definition
note_class: architecture
domain: vault_governance
layer: systems
scope: null

canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: approved
version: 1

created: 2026-03-14
updated: 2026-03-14
last_reviewed: null
review_cycle: quarterly

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[CONST.vault_curator.map]]"
  implements:
    - "[[Specialist Agent]]"
  governs: []
  inherits_from:
    - "[[Agent]]"
  applies_to:
    - "[[Vault Curator constellation]]"
  uses:
    - "[[06_authority_links/vault_curator_schema_validator.yaml]]"
  produces:
    - "[[Schema Validation Report (CSV)]]"

map: "[[CONST.vault_curator.map]]"
maps:
  - "[[Agent Maestro — Constellation Architecture Map]]"

related:
  - "[[CONST.vault_curator.agent.supervisor]]"
  - "[[CONST.vault_curator.agent.specialist.link_auditor]]"
  - "[[CONST.vault_curator.agent.specialist.orphan_detector]]"
related_maps:
  - "[[Agent Maestro — Agent Taxonomy Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - agent
  - specialist
  - vault_governance
  - schema_validation

hash: ""
---

# Schema Validator

## Agent Role

**Specialist Agent** for the [[Vault Curator constellation]].

Responsible for validating frontmatter schema against standards, checking required fields, and generating validation reports.

## Authority Type

**Execution Authority**

- Scope: Schema validation, frontmatter analysis, report generation
- Level: Low (executes delegated tasks only)
- Escalation Path: → Integrity Coordinator (Supervisor)

## Responsibilities

### Primary Responsibilities

1. **Validate Frontmatter Against Schema**
   - Parse YAML frontmatter from all `.md` files
   - Check each note against Agent Maestro schema standard
   - Verify required fields present: `id`, `type`, `note_class`, `schema_version`
   - Validate field formats and value constraints

2. **Check Required Fields**
   - `id` — must be present and valid format (CON.*, MAP.*, CONST.*, etc.)
   - `type` — must match allowed types (concept, map, agent_definition, etc.)
   - `note_class` — must be valid class (knowledge, architecture, governance, etc.)
   - `schema_version` — must equal 2
   - `created` — must be valid ISO date
   - `owner` — must be non-empty

3. **Identify Schema Violations**
   - Missing required fields
   - Invalid field formats
   - Invalid enum values (type, note_class)
   - Malformed YAML
   - Wrong schema_version

4. **Generate Validation Report**
   - Output structured CSV report with columns:
     - `file_path` — path to validated file
     - `violation_type` — MISSING_FIELD / INVALID_FORMAT / INVALID_VALUE / MALFORMED_YAML
     - `field_name` — which field has the violation
     - `current_value` — what's actually in the field
     - `expected_value` — what should be there
     - `severity` — CRITICAL/HIGH/MEDIUM/LOW
   - Report location: `workspaces/link_auditor/artifacts/schema_validation_report.csv`

5. **Record Execution**
   - Log execution timestamp
   - Record files validated, violations found
   - Write to `artifacts/logs/execution.log`

## Execution Pattern

```
Receive Execution Task (from Supervisor)
    ↓
Parse All Frontmatter
    ├→ Extract YAML from each file
    ├→ Check required fields
    └→ Validate field formats
    ↓
Identify Schema Violations
    ├→ MISSING_FIELD
    ├→ INVALID_FORMAT
    ├→ INVALID_VALUE
    └→ MALFORMED_YAML
    ↓
Generate CSV Report
    ├→ file_path | violation_type | field_name | current_value | expected_value | severity
    └→ Write to artifacts/schema_validation_report.csv
    ↓
Write Execution Log
    └→ Write to artifacts/logs/execution.log
    ↓
Report Complete (to Supervisor)
```

## Output Artifacts

**Primary Output**: `workspaces/link_auditor/artifacts/schema_validation_report.csv`

Example format:
```
file_path,violation_type,field_name,current_value,expected_value,severity
02_KNOWLEDGE/concepts/Agent.md,MISSING_FIELD,schema_version,,2,CRITICAL
05_SYSTEMS/system_file.md,INVALID_FORMAT,created,2026-13-45,2026-03-14,HIGH
```

**Execution Log**: `workspaces/link_auditor/artifacts/logs/execution.log`

## Schema Standard Reference

Valid field values (examples):
- `type`: concept, map, system, agent_definition, authority_pack
- `note_class`: knowledge, architecture, governance, process
- `schema_version`: 2 (only valid value)
- `status`: active, deprecated, archived

## Authority Pack

Link to authority pack: **[[06_authority_links/vault_curator_schema_validator.yaml]]**

Compiled at runtime into workspace `authority/` directory.

## Python Script Reference

Implementation: `05_SYSTEMS/infrastructure/tools/schema_validator.py`

## Related Concepts

- [[Specialist Agent]]
- [[Execution Authority]]
- [[Frontmatter Schema]]
- [[CONST.vault_curator.agent.supervisor]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
