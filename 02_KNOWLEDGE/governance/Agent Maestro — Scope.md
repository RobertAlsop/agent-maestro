---
schema_version: 2
title: "Agent Maestro — Scope"
type: scope
note_class: governance
domain: governance
layer: governance
authority_weight: 80
resolution_basis: authority_weight
canonical: true
status: active
review_status: approved
version: 2
created_date: 2026-03-10
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Agent Maestro Scope Boundaries]]"
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — North Star]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
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

Agent Maestro is bounded. Clear scope prevents drift and keeps the discipline operationally focused. This boundary enforcement is an expression of Law 3 (Economy) — only what is necessary.

## In Scope

- [[Agent Systems]] architecture
- [[Authority Architecture]] governance
- Operational workflows
- [[Memory Architecture]]
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

- [[Agent Maestro — Foundations]]
- [[Agent Maestro — North Star]]
- [[Agent Maestro — Strategy]]
