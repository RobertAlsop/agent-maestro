---
type: registry
note_class: registry
domain: ai_governance
layer: registry

canonical: true
authority_weight: 95
resolution_basis: canonical
schema_version: 2
title: "Authority Pack Registry"

status: active
review_status: approved
version: 1

created_date: 2026-03-12
last_modified: 2026-03-12

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []


  - "[[Agent Maestro — Pack Inheritance Map]]"
  - "[[Agent Maestro — Governance Artifacts Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - registry
  - authority
  - governance

hash: ""
---

# Authority Pack Registry

## Purpose

Authoritative registry of all [[Authority Pack|Authority Packs]] in the Agent Maestro system. Every pack must be registered here before it can be used in compilation or deployed to agents.

## Context

The registry is the resolution anchor for authority pack objects. When a compiler, system, or agent needs to reference a pack by ID, this registry provides the authoritative record.

## Structure

Each entry records:

| Field | Description |
|---|---|
| `pack_id` | Stable unique identifier (never changes) |
| `pack_name` | Human display name |
| `pack_type` | conceptual / base / role / domain / constellation |
| `status` | active / deprecated / experimental |
| `current_version` | Current canonical version |
| `parent_pack` | Parent pack ID (if inherited) |
| `pack_folder` | Vault folder path |
| `registered` | Date registered |

## Registered Packs

| Pack ID | Name | Type | Status | Version | Folder |
|---|---|---|---|---|---|
| PACK.conceptual_authority | Conceptual Authority | base | active | 1.0.0 | `packs/conceptual_authority/` |
| PACK.decision_authority | Decision Authority | base | active | 1.0.0 | `packs/decision_authority/` |
| PACK.execution_authority | Execution Authority | base | active | 1.0.0 | `packs/execution_authority/` |
| PACK.governance_authority | Governance Authority | base | active | 1.0.0 | `packs/governance_authority/` |
| PACK.interface_authority | Interface Authority | base | active | 1.0.0 | `packs/interface_authority/` |
| PACK.memory_authority | Memory Authority | base | active | 1.0.0 | `packs/memory_authority/` |
| PACK.operational_authority | Operational Authority | base | active | 1.0.0 | `packs/operational_authority/` |
| PACK.orchestration_authority | Orchestration Authority | base | active | 1.0.0 | `packs/orchestration_authority/` |

## Entry Rules

1. Every pack must be registered before first use
2. Pack IDs are stable and never reused
3. When a pack is deprecated, status changes to `deprecated` — the record is never deleted
4. Version changes are recorded in [[Pack Version Registry]]

## Related

- [[Authority Packs Index]] — navigational index for human browsing
- [[Pack Version Registry]] — version tracking
- [[Pack Lineage Index]] — lineage navigation
- [[Authority Architecture Map]]
