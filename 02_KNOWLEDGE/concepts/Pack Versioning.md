---
id: CON.pack_versioning
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
scope:
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: draft
version: 1
created: 2026-03-12
updated: 2026-03-14
last_reviewed:
review_cycle: none
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements:
    - "[[Pack Versioning Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Authority Pack]]"
  uses:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]"
  produces: []
map: "[[Agent Maestro — Concepts Map]]"
maps:
  - "[[Agent Maestro — Pack Inheritance Map]]"
related: []
related_maps: []
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - governance
  - versioning
hash: ""
---

# Pack Versioning

## Definition

The practice of assigning, tracking, and managing version identifiers for [[Authority Pack|Authority Packs]] across their lifecycle — ensuring that changes to governance rules are recorded, traceable, and controllable, and that dependent systems maintain compatibility.

## Boundaries

Pack Versioning is not just incrementing a number. It is a governance discipline that requires: declaring what changed and why, specifying compatibility with parent pack versions, and registering each new version in the [[Pack Version Registry]]. Informal changes to pack files without versioning are a governance violation.

## Purpose

Governance without versioning is ungovernable. Pack Versioning ensures that the governance state of any agent at any point in time can be reconstructed from the pack version record. It enables safe evolution of authority rules, compatibility management across dependent systems, and auditable governance history.

## Key Properties

- **Semver-aligned** — major/minor/patch version scheme aligned with change type
- **Lineage-tracked** — every version records its parent version and delta
- **Compatibility-declared** — which parent versions a child pack is compatible with
- **Registry-anchored** — all versions are registered in [[Pack Version Registry]]

## Change Types

| Change Type | Version Bump | Example |
|---|---|---|
| Breaking governance change | Major | Remove a governed action class |
| Backwards-compatible addition | Minor | Add a new control gate |
| Non-functional / doc update | Patch | Clarify an evidence requirement |

## Relationships

- [[Authority Pack]] — what is being versioned
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] — inheritance chains must declare version compatibility
- [[Pack Versioning Pattern]] — design pattern for implementing versioning
- [[Pack Version Registry]] — authoritative registry of all pack versions
- [[Pack Lineage Index]] — navigation index for version lineage
- [[Agent Maestro — Pack Inheritance Map]]
- [[Agent Maestro — Concepts Map]]
