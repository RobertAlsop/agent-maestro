---
id: SYS.context_pack_architecture
type: system
note_class: architecture
domain: system_architecture
layer: systems
scope: null

canonical: false
authority_weight: 60
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

map: "[[Memory Architecture Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags: []

hash: ""
---

# Context Pack Architecture

## Purpose

Defines how task-scoped context packs are assembled from the three memory layers and delivered to agents.

## Responsibilities

- Assemble relevant memory across all three layers for a given task
- Scope retrieval to task authority
- Deliver a well-formed context pack to the agent runtime

## Core Components

- Task scope definition
- Layer query orchestration
- Context assembly and formatting

## Invariants

- Context packs must be scoped to task authority
- No layer may be queried without an approved scope

## Related Concepts

- [[Context Pack]]
- [[Memory Architecture]]
