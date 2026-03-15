---
id: CON.compiled_governance_artifact
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
scope: null

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-12
updated: 2026-03-14
last_reviewed: null
review_cycle: none

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements:
    - "[[Governance Compilation Pattern]]"
  governs: []
  inherits_from:
    - "[[Authority Pack]]"
  applies_to: []
  uses:
    - "[[Host Binding]]"
  produces: []

map: "[[Agent Maestro — Concepts Map]]"
maps:
  - "[[Agent Maestro — Governance Artifacts Map]]"
  - "[[Authority Pack Compiler — Map]]"

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
  - compiler

hash: ""
---

# Compiled Governance Artifact

## Definition

A deterministic, runtime-ready governance object produced by the [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] from one or more [[Authority Pack|Authority Packs]]. A Compiled Governance Artifact represents the resolved, inheritance-flattened, and host-bound form of an authority contract — the form that can be loaded by an agent runtime environment.

## Boundaries

A Compiled Governance Artifact is the *output* of compilation, not the input. The input is the source authority pack or pack set. A compiled artifact is tied to a specific compilation run, a specific set of input packs at specific versions, and a specific host binding. Changing any of these requires recompilation.

## Purpose

Compilation produces deterministic governance. When an agent loads a compiled governance artifact, there is no ambiguity about what rules apply — inheritance has been resolved, overrides have been applied, and the result is a flat, validated governance contract. This makes runtime governance fast, auditable, and reproducible.

## Key Properties

- **Deterministic** — same inputs always produce the same artifact
- **Versioned** — each artifact is associated with the pack versions that produced it
- **Host-bound** — an artifact is bound to a specific runtime via [[Host Bindings]]
- **Auditable** — traceable back to source packs through [[Pack Lineage Index]]

## Registry

All compiled governance artifacts are registered in the [[Compiler Artifacts Registry]].

## Relationships

- [[Authority Pack]] — the source packs consumed during compilation
- [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] — the system that produces compiled artifacts
- [[Host Binding]] — the mechanism that binds artifacts to a runtime
- [[Governance Artifact]] — the broader class of which this is a specialisation
- [[Governance Compilation Pattern]] — the design pattern governing the compilation process
- [[Authority Pack Compiler — Map]]
- [[Agent Maestro — Concepts Map]]
