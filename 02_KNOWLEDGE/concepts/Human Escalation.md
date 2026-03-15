---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Human Escalation"

status: active
review_status: draft
version: 1

created_date: 2026-03-12
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements:
    - "[[Human Escalation Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
  uses:
    - "[[Decision Authority]]"
  produces: []



source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - concept
  - agent_maestro
  - governance

hash: ""
---

# Human Escalation

## Definition

The structured mechanism by which an agent transfers authority and decision-making to a human operator when a situation exceeds the agent's defined authority scope, evidence requirements are not met, or an authority pack explicitly requires human review.

## Boundaries

Human Escalation is not a fallback for agent failure — it is a designed, governed transfer of authority. An escalation must follow a declared escalation class and must be traceable. Unstructured agent failures that result in stopping work are *not* escalations. Escalation is a deliberate, rule-governed handoff.

## Purpose

Human Escalation is the mechanism that keeps humans in control of AI-native systems. By defining escalation rules explicitly in authority packs, Agent Maestro ensures that agents never operate beyond their sanction — and that humans receive well-structured, contextualised handoffs rather than raw failures.

## Key Properties

- **Declared** — escalation conditions must be specified in the agent's authority pack
- **Classified** — escalations belong to defined classes (see [[Escalation Classes Reference]])
- **Evidence-bearing** — the escalating agent must pass context and evidence to the human recipient
- **Traceable** — every escalation event must be logged

## Escalation Triggers

Common triggers defined in authority packs:
- Decision exceeds the agent's authority threshold
- Evidence requirements cannot be met
- Conflicting rules without a resolution path
- Explicit human approval required by policy

## Relationships

- [[Human Escalation Pattern]] — design pattern for implementing escalation
- [[Executive Agent]] — the governance layer that manages constellation-level escalation
- [[Decision Authority]] — the authority boundary that determines when escalation is needed
- [[Escalation Classes Reference]] — classification system for escalation types
- [[Agent Maestro — Concepts Map]]
