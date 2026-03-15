---
id: SYS.memory_model
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
updated: 2026-03-14
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

# Memory Model

## Purpose

The top-level architecture of the three-layer agent memory system.

## Responsibilities

- Define how each memory layer stores and retrieves knowledge
- Manage layer boundaries and handoffs
- Govern context pack assembly

## Core Components

- [[Knowledge Graph Layer]]
- [[Vector Memory Layer]]
- [[Structured Data Layer]]
- [[Context Pack Architecture]]

## Invariants

- Each layer has distinct read/write contracts
- Context packs may only be assembled from authorised layers
- Memory writes must be auditable

## Implementation Status

The architectural principle is a three-layer model. The current operational state is:

| Layer | Status | Implementation |
|---|---|---|
| [[Knowledge Graph Layer]] | **Active** | Obsidian-native notes as graph nodes; wiki-links and frontmatter `relationships` as edges; CSV index for programmatic access |
| [[Structured Data Layer]] | **Active** | CSV files with Google Sheets compatibility; one CSV per operational concern; UTF-8, comma-delimited, ISO 8601 dates |
| [[Vector Memory Layer]] | **Planned** | Architecturally reserved. When connected, embeddings will be generated from Knowledge Graph Layer notes. Each note's `id` field serves as the stable anchor linking vectors to source notes. |

The principle name remains "Three-Layer Memory Model" because it describes the complete architectural design. Documentation distinguishes between the target architecture (three layers) and current implementation (two active layers, one planned).

## Related Concepts

- [[Memory Architecture]]
- [[Three-Layer Memory Model]]
- [[Agent Maestro Layer Model]]
