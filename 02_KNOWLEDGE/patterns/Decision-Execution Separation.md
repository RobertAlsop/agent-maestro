---
id: PAT.decision_execution_separation
type: pattern
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

created: 2026-03-10
updated: 2026-03-14
last_reviewed: null
review_cycle: none

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
  uses:
    - "[[Decision Authority]]"
    - "[[Execution Authority]]"
  produces: []

map: "[[Authority Architecture Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - concept
  - pattern
  - agent_maestro

hash: ""
---

# Decision-Execution Separation

## Definition

The architectural pattern of maintaining distinct authority layers for deciding and executing, preventing agents from both selecting and acting without review.

## Purpose

Conflating decision and execution authority removes human oversight opportunities. Separation creates natural control gates.

## Key Components

- [[Decision Authority]] — selection layer
- [[Execution Authority]] — action layer
- Explicit handoff protocol between layers
- Escalation triggers at the boundary

## Relationships

- [[Authority Pack]]
- [[Human Escalation Pattern]]
- [[Authority Architecture Map]]
