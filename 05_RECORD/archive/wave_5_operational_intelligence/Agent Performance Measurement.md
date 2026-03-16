---
type: system
note_class: architecture
domain: system_architecture
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Agent Performance Measurement"

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

# Agent Performance Measurement

## Purpose

Defines how agent and workflow performance is measured, tracked, and used for system improvement.

## Responsibilities

- Define performance metrics per agent and workflow
- Collect [[Operational Outcome|operational outcomes]]
- Surface performance data for review
- Feed [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]] with evidence

## Invariants

- All metrics must be attributable to a specific agent and workflow
- Performance data must be available for review within 24 hours of an event

## Related Concepts

- [[Operational Outcome]]
- [[Evidence Over Assumptions]]
