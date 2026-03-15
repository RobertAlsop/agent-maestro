---
type: pattern
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Human Escalation Pattern"

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
  uses: []
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

# Human Escalation Pattern

## Definition

The structural requirement that agents must route irreversible, financial, policy, and system-modifying actions to human review before execution.

## Purpose

Humans must never be removed as the final authority on consequential actions. This is Principle 7 of [[Agent Maestro — Principles]].

## Key Components

- Irreversibility threshold definition
- Escalation trigger conditions
- Human review interface
- Audit trail of escalation decisions

## Relationships

- [[Execution Authority]]
- [[Decision-Execution Separation]]
- [[Escalation Models]]
