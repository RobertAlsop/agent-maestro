---
id: CONST.vault_curator.map
type: map
note_class: navigation
domain: vault_governance
layer: systems
scope:
canonical: false
authority_weight: 75
resolution_basis: authority_weight
schema_version: 2
status: deprecated
review_status: approved
version: 1
created: 2026-03-14
updated: 2026-03-14
last_reviewed:
review_cycle: quarterly
owner: AgentMaestro
relationships:
  defines:
    - "[[CONST.vault_curator.agent.executive]]"
    - "[[CONST.vault_curator.agent.supervisor]]"
    - "[[CONST.vault_curator.agent.specialist.link_auditor]]"
    - "[[CONST.vault_curator.agent.specialist.schema_validator]]"
    - "[[CONST.vault_curator.agent.specialist.orphan_detector]]"
  part_of:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[authority_packs]]"
  produces:
    - "[[maintenance_cycle]]"
map: "[[Agent Maestro — Constellation Architecture Map]]"
maps:
  - "[[Agent Maestro — Systems Map]]"
related: []
related_maps:
  - "[[Agent Maestro — Constellation Architecture Map]]"
  - "[[Authority Architecture Map]]"
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by:
  - "[[Vault Maintenance Constellation]]"
tags:
  - constellation
  - vault_governance
  - reference_implementation
hash: ""
---

# Vault Curator Constellation

> **DEPRECATED**: This constellation has been superseded by the **Vault Maintenance Constellation** (CONST.vault_maintenance). vault_maintenance provides broader coverage (definition alignment, ontology integrity, template compliance, note processing, self-healing) and proper authority inheritance from the Knowledge Executive. The unique capabilities of vault_curator (link auditing, orphan detection) are planned for absorption into vault_maintenance in a future session. Schema validation is covered by vault_maintenance's Template Compliance Scanner.

## Purpose

The Vault Curator constellation is a reference implementation for automated vault maintenance and integrity verification. It orchestrates a team of specialist agents that audit vault links, validate schemas, detect orphaned content, and apply safe fixes under human-supervised authority.

## Constellation Architecture

### Executive Layer
- **[[vault_governance_director]]** (Vault Governance Director)
  - Authority Type: Decision
  - Responsibilities: Prioritize maintenance tasks, approve non-destructive fixes, escalate destructive actions
  - Escalation: → human_operator

### Supervisor Layer
- **[[integrity_coordinator]]** (Integrity Coordinator)
  - Authority Type: Coordination
  - Responsibilities: Receive priorities from Executive, delegate to Specialists, aggregate results, apply safe fixes
  - Reports to: Vault Governance Director

### Specialist Layer
- **[[link_auditor]]** (Link Auditor)
  - Authority Type: Execution
  - Task: Audit all vault links, detect broken references, generate report
  - Produces: CSV audit report

- **[[schema_validator]]** (Schema Validator)
  - Authority Type: Execution
  - Task: Validate frontmatter against schema, check all required fields
  - Produces: CSV validation report

- **[[orphan_detector]]** (Orphan Detector)
  - Authority Type: Execution
  - Task: Detect notes without incoming links or orphaned content
  - Produces: CSV orphan detection report

## Workflows

### Main Workflow: [[maintenance_cycle]]

1. Executive reviews current audit report freshness
2. Executive prioritizes which audits to run
3. Supervisor receives priorities, delegates to specialists
4. Specialists execute in parallel (link audit, schema validation, orphan detection)
5. Specialists write CSV reports to workspace artifacts
6. Supervisor aggregates results, applies safe fixes (backlinks, schema corrections)
7. Supervisor escalates destructive actions to Executive
8. Executive reviews escalations, escalates to human if needed
9. Execution log updated with results

## Authority Links

All authority packs registered in: **[[authority_packs]]**

- `vault_curator_executive.yaml` — Executive authority (decision)
- `vault_curator_supervisor.yaml` — Supervisor authority (coordination)
- `vault_curator_link_auditor.yaml` — Link Auditor authority (execution)
- `vault_curator_schema_validator.yaml` — Schema Validator authority (execution)
- `vault_curator_orphan_detector.yaml` — Orphan Detector authority (execution)

Compiled artifacts stored in workspace authority directories at runtime.

## Workspace Organization

**MWP Workspace**: `workspaces/link_auditor/`

Reference implementation showing how specialist workspaces organize:
- `authority/` — Compiled authority artifact (populated at runtime)
- `agents/` — Agent definition (populated at runtime)
- `stages/` — Stage contract (populated at runtime)
- `references/` — Vault file index (populated at runtime)
- `artifacts/` — Output directory (logs/, escalations/)

See: [[workspace_readme]]

## Execution Context

**Constellation ID**: CONST.vault_curator
**Status**: Deprecated — superseded by CONST.vault_maintenance
**Created**: 2026-03-14
**Last Executed**: (pending first execution)
**Workspace Path**: `05_SYSTEMS/agent_systems/constellations/vault_curator/workspaces/`

## Related Maps

- [[Agent Maestro — Constellation Architecture Map]]
- [[Authority Architecture Map]]
- [[Agent Maestro — Agent Taxonomy Map]]
