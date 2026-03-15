---
id: REG.pack_version_registry
type: registry
note_class: registry
domain: ai_governance
layer: registry
scope: null

canonical: true
authority_weight: 95
resolution_basis: canonical
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
  - registry
  - versioning
  - authority

hash: ""
---

# Pack Version Registry

## Purpose

Authoritative registry of all versions of all [[Authority Pack|Authority Packs]]. Every pack version must be registered here before it can be used as a compiler input.

## Context

Pack versioning is a governance requirement. This registry ensures that the governance state of any compiled artifact can be reconstructed by looking up the pack versions that were used as inputs.

## Structure

Each entry records:

| Field | Description |
|---|---|
| `pack_id` | Parent pack stable ID |
| `version` | Semver version string |
| `parent_version` | Version this was derived from |
| `change_summary` | What changed in this version |
| `change_type` | major / minor / patch |
| `compatibility` | Compatible parent pack versions |
| `registered` | Date registered |
| `status` | active / deprecated |

## Registry Entries

### PACK.conceptual_authority

| Version | Parent | Change | Type | Date |
|---|---|---|---|---|
| 1.0.0 | *(origin)* | Initial version | major | 2026-03-10 |

### PACK.decision_authority

| Version | Parent | Change | Type | Date |
|---|---|---|---|---|
| 1.0.0 | *(origin)* | Initial version | major | 2026-03-10 |

*(Additional packs follow same pattern.)*

## Entry Rules

1. Every pack version must be registered before first use in compilation
2. Version strings must be valid semver
3. Parent version must be an existing registered version
4. Versions are never deleted

## Related

- [[Authority Pack Registry]] — the pack-level registry
- [[Pack Lineage Index]] — navigation through lineage
- [[Pack Versioning Pattern]] — the implementation pattern
- [[Agent Maestro — Pack Inheritance Map]]
