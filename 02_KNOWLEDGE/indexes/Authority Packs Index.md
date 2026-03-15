---
type: index
note_class: navigation
domain: ai_governance
layer: maps

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2
title: "Authority Packs Index"

status: active
review_status: approved
version: 2

created_date: 2026-03-10
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


  - "[[Authority Architecture Map]]"
  - "[[Agent Maestro — Pack Inheritance Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - index
  - authority

hash: ""
---

# Authority Packs Index

All authority packs follow the [[Authority Pack Grammar]] (sections 00–13).

Pack files are classified as **System Artifacts**, not canonical notes. For version and lineage data use the registries below.

## Registries

- [[Authority Pack Registry]] — canonical registry of all packs; resolves pack IDs to current versions
- [[Pack Version Registry]] — records all registered versions per pack
- [[Pack Lineage Index]] — tracks pack ancestry and parent-child relationships

## Base Packs

Base packs define foundational authority that all other packs may inherit from.

| Pack | Folder | Status |
|---|---|---|
| Governance Authority | `05_SYSTEMS/authority_architecture/packs/governance_authority/` | active |
| Decision Authority | `05_SYSTEMS/authority_architecture/packs/decision_authority/` | active |
| Execution Authority | `05_SYSTEMS/authority_architecture/packs/execution_authority/` | active |
| Operational Authority | `05_SYSTEMS/authority_architecture/packs/operational_authority/` | active |
| Interface Authority | `05_SYSTEMS/authority_architecture/packs/interface_authority/` | active |
| Orchestration Authority | `05_SYSTEMS/authority_architecture/packs/orchestration_authority/` | active |
| Conceptual Authority | `05_SYSTEMS/authority_architecture/packs/conceptual_authority/` | active |
| Memory Authority | `05_SYSTEMS/authority_architecture/packs/memory_authority/` | active |

Additional base packs: `05_SYSTEMS/authority_architecture/packs/base_packs/`

## Role Packs

Role packs extend base packs with authority specific to agent roles (executive, supervisor, specialist).

| Pack | Folder | Status |
|---|---|---|
| *(none registered)* | `05_SYSTEMS/authority_architecture/packs/role_packs/` | — |

## Domain Packs

Domain packs extend base or role packs with authority specific to a business or operational domain.

| Pack | Folder | Status |
|---|---|---|
| *(none registered)* | `05_SYSTEMS/authority_architecture/packs/domain_packs/` | — |

## Constellation Packs

Constellation packs define the composed authority architecture for a full [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]].

| Pack | Folder | Status |
|---|---|---|
| *(none registered)* | `05_SYSTEMS/authority_architecture/packs/constellation_packs/` | — |

## Related

- [[Authority Pack]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]]
- [[Authority Architecture Map]]
- [[Agent Maestro — Pack Inheritance Map]]
