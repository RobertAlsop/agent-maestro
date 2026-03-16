---
type: system
note_class: architecture
domain: system_architecture
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Operational Agent Design"

status: active
review_status: draft
version: 1

created_date: 2026-03-10
last_modified: 2026-03-10

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



source_type: ai_authored
supersedes: []
superseded_by: []

tags: []

hash: ""
---

# Operational Agent Design

## Purpose

Defines the design principles and patterns for building agents that are reliable, governable, and effective in production.

## Responsibilities

- Define agent role and responsibility clearly
- Specify authority boundaries before building
- Design for observability from the start

## Core Components

- Role definition framework
- Authority scope specification
- Observability design requirements

## Invariants

- No agent may be built without a defined authority scope
- All agents must expose performance metrics

## Related Concepts

- [[Agent]]
- [[Anti-Agent-Sprawl Pattern]]
