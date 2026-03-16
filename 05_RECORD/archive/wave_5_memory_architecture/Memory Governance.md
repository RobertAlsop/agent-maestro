---
type: system
note_class: architecture
domain: system_architecture
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Memory Governance"

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

# Memory Governance

## Purpose

Defines the rules, access controls, and audit requirements that govern how agent memory is read, written, and managed.

## Responsibilities

- Define read/write authority for each memory layer
- Enforce memory access controls via memory authority pack
- Govern retention and deletion policies

## Invariants

- Memory writes must be authorised by the memory authority pack
- All memory access must produce an audit event

## Related Systems

- Authority Architecture]]

## Related Concepts

- [[Memory Architecture]]
- Authority Architecture]]
