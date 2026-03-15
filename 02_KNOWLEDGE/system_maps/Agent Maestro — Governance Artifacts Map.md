---
id: MAP.agent_maestro.governance_artifacts
type: system_map
note_class: architecture
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

map: "[[Agent Maestro — Governance Map]]"
maps: []

related: []
related_maps:
  - "[[Authority Architecture Map]]"
  - "[[Authority Pack Compiler — Map]]"
  - "[[Agent Maestro — Governance Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - map
  - governance
  - artifacts

hash: ""
---

# Agent Maestro — Governance Artifacts Map

## Purpose

Navigation map for all governance artifacts produced by the Agent Maestro authority architecture — from design-time pack definitions through to compiled runtime artifacts.

---

## Concepts

- [[Governance Artifact]] — any formally defined governance object
- [[Compiled Governance Artifact]] — a governance artifact produced by the compiler

---

## Design-Time Artifacts

These artifacts define governance intent before compilation:

- [[Authority Pack]] — modular governance contract (atomic)
- [[Pack Manifest]] — canonical governance artifact declaring pack composition, dependencies, and runtime requirements
- [[Context Pack]] — contextual configuration artifact

---

## Inheritance and Versioning Artifacts

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] — how packs inherit from parent packs
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]] — how packs are versioned and evolved
- [[Pack Override Rules]] — how overrides are declared and tracked

---

## Compiler Artifacts

Produced by the [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]]:

- [[Compiled Governance Artifacts]] (system) — the full compiled output set
- [[Integration Manifest]] — binding contracts for runtime hosts
- [[Host Bindings]] — resolved bindings to specific runtime environments

---

## Schemas and References

- [[Governance Schemas Reference]] — formal schemas for governance artifacts
- [[Compiler Artifact Schemas Reference]] — schemas for compiled artifact formats
- [[Artifact Taxonomy]] — taxonomy of all artifact types

---

## Registries

- [[Authority Pack Registry]] — all authority packs, registry-resolvable
- [[Pack Version Registry]] — versioned pack snapshots
- [[Pack Lineage Index]] — lineage navigation index
- [[Compiler Artifacts Registry]] — compiled artifacts, registry-resolvable

---

## Related Maps

- [[Authority Architecture Map]]
- [[Authority Pack Compiler — Map]]
- [[Agent Maestro — Governance Map]]
- [[Agent Maestro — Navigation Map]]
