---
type: pattern
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Evidence Over Assumptions"

status: active
review_status: draft
version: 1

created_date: 2026-03-10
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
    - "[[Decision Authority]]"
    - "[[Execution Authority]]"
  uses:
    - "[[Operational Outcome]]"
  produces: []



source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - concept
  - pattern
  - agent_maestro

hash: ""
---

# Evidence Over Assumptions

## Definition

The operational principle that system behaviour must be validated through events and measured outcomes, not theoretical reasoning or assumed correctness.

## Purpose

Assumptions about system behaviour are fragile. Principle 9 of [[Agent Maestro — Principles]] requires evidence. The [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]] pipeline exists to collect it.

## Key Components

- Event logging
- Outcome measurement
- Feedback loop to system design
- [[Operational Outcome]] as the evidence unit

## Relationships

- [[Operational Outcome]]
- [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- [[Controlled Evolution Pattern]]
