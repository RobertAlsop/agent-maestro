---
type: pattern
note_class: knowledge
domain: agent_architecture
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Three-Layer Memory Model"

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
    - "[[Memory Architecture]]"
  uses:
    - "[[Knowledge Graph Layer]]"
    - "[[Vector Memory Layer]]"
    - "[[Structured Data Layer]]"
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

# Three-Layer Memory Model

## Definition

The pattern of structuring agent memory across three distinct layers — knowledge graph, vector memory, and structured data — each with separate responsibilities.

## Purpose

Mixed or unstructured memory leads to unpredictable retrieval and reasoning. Separation of layers enforces clarity and reliability. This operationalises Principle 6 from [[Agent Maestro — Principles]].

## Key Components

- [[Knowledge Graph Layer]] — structured relationships and facts
- [[Vector Memory Layer]] — semantic similarity retrieval
- [[Structured Data Layer]] — operational records and state

## Relationships

- [[Memory Architecture]]
- [[Context Pack]]
- [[Memory Architecture Map]]
