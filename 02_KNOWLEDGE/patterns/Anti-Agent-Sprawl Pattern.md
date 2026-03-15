---
type: pattern
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Anti-Agent-Sprawl Pattern"

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
  uses:
    - "[[Authority Pack]]"
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

# Anti-Agent-Sprawl Pattern

## Definition

The discipline of preventing agents from multiplying without clear purpose, defined authority, and measurable outcomes.

## Purpose

Agent sprawl creates unauditable, unmanageable systems. This pattern enforces Principle 12 of [[Agent Maestro — Principles]]: every agent must justify its existence.

## Key Components

- Agent registry with owner and purpose
- Authority boundary definition before creation
- Measurable outcome requirement
- Regular pruning review

## Relationships

- [[Agent]]
- [[Governance Before Autonomy]]
- [[Agent Maestro — Governance Map]]
