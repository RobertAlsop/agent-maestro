---
id: MAP.authority.architecture
type: system_map
note_class: architecture
domain: system_architecture
layer: maps
scope: null

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 2

created: 2026-03-10
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

map: "[[Agent Maestro — Systems Map]]"
maps: []

related: []
related_maps:
  - "[[Authority Pack Compiler — Map]]"
  - "[[Agent Maestro — Pack Inheritance Map]]"
  - "[[Agent Maestro — Governance Artifacts Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - map
  - navigation
  - authority

hash: ""
---

# Authority Architecture Map

## Purpose

Navigation layer for all authority architecture systems, packs, inheritance, versioning, compiler, and governance artifacts.

---

## Core Systems

- [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/Authority Architecture]] — system overview
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]] — system implementation of the authority model

---

## Concepts

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] — system overview concept
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]] — conceptual framework
- [[Authority Pack]] — atomic governance contract
- [[Decision Authority]] · [[Execution Authority]] — primary authority types
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] (concept) — inheritance mechanics
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]] (concept) — version management

---

## Patterns

- [[Authority Pack Grammar]] — the 00–13 structural standard
- [[Decision-Execution Separation]]
- [[Deterministic Control Surfaces]]
- [[Governance Before Autonomy]]
- [[Authority Inheritance Pattern]]
- [[Pack Override Rules]]
- [[Pack Versioning Pattern]]
- [[Governance Compilation Pattern]]
- [[Policy Resolution Pattern]]

---

## Authority Pack Index and Registry

- [[Authority Packs Index]] — navigation index
- [[Authority Pack Registry]] — authoritative registry

### Base Packs

| Pack | Folder |
|---|---|
| Governance Authority | `packs/governance_authority/` |
| Decision Authority | `packs/decision_authority/` |
| Execution Authority | `packs/execution_authority/` |
| Operational Authority | `packs/operational_authority/` |
| Interface Authority | `packs/interface_authority/` |
| Orchestration Authority | `packs/orchestration_authority/` |
| Conceptual Authority | `packs/conceptual_authority/` |
| Memory Authority | `packs/memory_authority/` |

### Extended Pack Families (future)
- `packs/role_packs/` · `packs/domain_packs/` · `packs/constellation_packs/`

---

## Inheritance & Versioning

- [[Agent Maestro — Pack Inheritance Map]] — full inheritance navigation
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] (system) — inheritance resolution
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]] (system) — version tracking
- [[Pack Lineage Index]] — lineage navigation
- [[Pack Version Registry]] — version registry

---

## Compiler

- [[Authority Pack Compiler — Map]] — full compiler navigation
- [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] (system)
- [[Pack Manifest]] — pack composition governance artifact

---

## Governance Artifacts

- [[Agent Maestro — Governance Artifacts Map]] — full artifacts navigation
- [[Compiler Artifacts Registry]] — compiled artifact registry

---

## Related Maps

- [[Agent Maestro — Systems Map]]
- [[Agent Maestro — Governance Map]]
- [[Agent Maestro — Navigation Map]]
