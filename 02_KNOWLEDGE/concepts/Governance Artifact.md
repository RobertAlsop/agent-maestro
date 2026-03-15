---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Governance Artifact"

status: active
review_status: draft
version: 1

created_date: 2026-03-12
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[Authority Pack]]"
    - "[[Context Pack]]"
    - "[[Compiled Governance Artifact]]"
  produces: []

  - "[[Agent Maestro — Governance Artifacts Map]]"


source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - concept
  - agent_maestro
  - governance

hash: ""
---

# Governance Artifact

## Definition

Any formally defined object in an Agent Maestro system that encodes, declares, or enforces governance rules, authority boundaries, or operational constraints. Governance Artifacts are the material expression of the [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] — they give governance physical form in the vault and in runtime environments.

## Boundaries

A Governance Artifact is a *formal governance object*, not just any document or note. A meeting note is not a governance artifact. A note containing governance rules is a governance artifact only if it follows a formal schema and is resolvable through the appropriate registry. Informal records do not qualify.

## Purpose

The concept of a Governance Artifact unifies the different types of governance objects across Agent Maestro — from source pack definitions through to compiled runtime contracts. Naming and classifying them enables consistent management, versioning, and audit.

## Classification

Key governance artifact types:

- **[[Authority Pack]]** — source governance contract (design-time)
- **[[Pack Manifest]]** — pack composition declaration
- **[[Compiled Governance Artifact]]** — resolved runtime governance contract (runtime)
- **[[Integration Manifest]]** — host binding declaration
- **[[Context Pack]]** — contextual configuration artifact

## Relationships

- [[Compiled Governance Artifact]] — runtime specialisation
- [[Authority Pack]] — primary source governance artifact
- [[Artifact Taxonomy]] — classification system for all artifact types
- [[Agent Maestro — Governance Artifacts Map]]
- [[Agent Maestro — Concepts Map]]
