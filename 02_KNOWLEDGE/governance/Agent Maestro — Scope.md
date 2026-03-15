---
id: GOV.agent_maestro.scope
type: scope
note_class: governance
domain: governance
layer: governance
scope: null

canonical: false
authority_weight: 65
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-10
updated: 2026-03-10
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
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - governance
  - scope

hash: ""
---

# Agent Maestro — Scope

## Purpose

Define what Agent Maestro does and does not cover.

## Principle

Agent Maestro is bounded. Clear scope prevents drift and keeps the discipline operationally focused.

## In Scope

- [[Agent Systems|Agent system architecture]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture|Authority governance]]
- Operational workflows
- [[Memory Architecture|Memory architecture]]
- Orchestration systems
- Monitoring and observability
- Operational intelligence infrastructure

## Out of Scope

- Model training
- LLM research
- Low-level AI algorithm development
- Isolated automation scripts without governance

## Implications

- Agent Maestro assumes agents operate inside **real organizations** with real accountability structures.
- Work that falls outside scope should not be filed under Agent Maestro.

## When It Applies

When evaluating whether a project, concept, or system belongs inside Agent Maestro.

## Related

- [[Agent Maestro — North Star]]
- [[Agent Maestro — Strategy]]
- [[Agent Maestro — Governance Map]]
