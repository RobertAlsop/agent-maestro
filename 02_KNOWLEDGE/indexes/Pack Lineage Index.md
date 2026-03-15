---
id: IDX.pack_lineage_index
type: index
note_class: navigation
domain: ai_governance
layer: maps
scope: null

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: approved
version: 1

created: 2026-03-12
updated: 2026-03-12
last_reviewed: null
review_cycle: annual

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

map: "[[Agent Maestro — Pack Inheritance Map]]"
maps: []

related: []
related_maps:
  - "[[Authority Architecture Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - index
  - lineage
  - authority

hash: ""
---

# Pack Lineage Index

## Purpose

Navigation index for the inheritance lineage of all [[Authority Pack|Authority Packs]] — showing parent-child relationships, version chains, and override declarations across the pack hierarchy.

## Context

This index helps practitioners navigate the pack inheritance graph without needing to inspect individual pack files. It answers: where does a pack sit in the hierarchy, what does it inherit from, and what does it override?

## Relationships

- Registries resolve: [[Authority Pack Registry]] · [[Pack Version Registry]]
- Maps navigate: this index navigates lineage relationships

## Base Pack Layer

All packs in `05_SYSTEMS/authority_architecture/packs/` current packs (01_scope through 13_extension_points):

| Pack | ID | Inherits From | Version |
|---|---|---|---|
| Conceptual Authority | PACK.conceptual_authority | *(base)* | 1.0.0 |
| Decision Authority | PACK.decision_authority | *(base)* | 1.0.0 |
| Execution Authority | PACK.execution_authority | *(base)* | 1.0.0 |
| Governance Authority | PACK.governance_authority | *(base)* | 1.0.0 |
| Interface Authority | PACK.interface_authority | *(base)* | 1.0.0 |
| Memory Authority | PACK.memory_authority | *(base)* | 1.0.0 |
| Operational Authority | PACK.operational_authority | *(base)* | 1.0.0 |
| Orchestration Authority | PACK.orchestration_authority | *(base)* | 1.0.0 |

## Role Pack Layer

*(Add entries as role packs are created in `packs/role_packs/`)*

## Domain Pack Layer

*(Add entries as domain packs are created in `packs/domain_packs/`)*

## Constellation Pack Layer

*(Add entries as constellation packs are created in `packs/constellation_packs/`)*

## Related

- [[Authority Pack Registry]] — authoritative registry
- [[Pack Version Registry]] — version records
- [[Agent Maestro — Pack Inheritance Map]]
