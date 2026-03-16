---
title: "Memory Architecture"
type: concept
status: active
authority_weight: 55
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related:
    - "[[Skill — Summarize]]"
tags: [concept, memory, foundational]
---

# Memory Architecture

## Purpose

Define the three-layer memory model that organizes knowledge within Agent Maestro. This concept expands on D2 (Three-Layer Memory Model) from [[Agent Maestro — Foundations]].

## Definition

Agent Maestro organizes knowledge in three distinct layers, each with different responsibilities and access patterns. Together they ensure that the system can remember what it needs to — structured relationships, semantic meaning, and operational data.

## The Three Layers

### 1. Knowledge Graph (Relationships)

The network of wiki-links and `relationships` frontmatter that connects every document in the vault. This layer answers: *how are things related?*

- **Current implementation:** Wiki-links in note bodies (navigational), `derives_from` / `governs` / `related` fields in frontmatter (structural)
- **Access pattern:** Graph traversal — follow links to discover connections
- **Maintained by:** Authors when creating/editing notes, validated by [[Skill — Validate]]

### 2. Structured Data (Registries and Logs)

CSV files, registries, and structured records that track operational data. This layer answers: *what happened, and what exists?*

- **Current implementation:** `tool_registry.csv`, escalation logs, state change logs, task execution logs in `05_RECORD/`
- **Access pattern:** Query/filter — search by field values
- **Maintained by:** Runtime tools and the [[Skill — Summarize]] skill

### 3. Vector Memory (Semantic Search)

Semantic embeddings that enable similarity-based retrieval. This layer answers: *what is this similar to?*

- **Current implementation:** Not yet implemented. This is a future capability (Stage 1 → Stage 2 transition).
- **Access pattern:** Similarity search — find conceptually related content regardless of explicit links
- **Planned use:** Enabling agents to find relevant knowledge without knowing exact note titles

## How the Layers Interact

The knowledge graph provides structure (what connects to what). Structured data provides facts (what happened when). Vector memory will provide discovery (what else is relevant). A well-functioning system uses all three: the graph for navigation, the data for accountability, and the vectors for serendipity.

## Current State

Layers 1 and 2 are operational. Layer 3 is planned. The system functions without vector memory — explicit links and structured logs cover current needs. Vector memory becomes important when the vault grows large enough that explicit linking can't capture all relevant connections.

## Traceability

Directly implements D2 (Three-Layer Memory Model) from [[Agent Maestro — Foundations]], which derives from Seed 2 (Structure) — specifically the Memory primitive ("what from the past informs the present?").

## Related

- [[Agent Maestro — Foundations]]
- [[Skill — Summarize]]
