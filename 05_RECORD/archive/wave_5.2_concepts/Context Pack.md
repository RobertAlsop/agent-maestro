---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Context Pack"

status: active
review_status: draft
version: 1

created_date: 2026-03-10
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[Memory Architecture]]"
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
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
  - agent_maestro

hash: ""
---

# Context Pack

## Definition

A structured, task-scoped assembly of memory drawn from the three layers of [[Memory Architecture]], prepared for [[Agent|agent]] consumption at the start of a task. A context pack is the delivery mechanism between stored knowledge and active agent reasoning — it determines *what the agent knows* when it begins work.

## Boundaries

A context pack is not a knowledge base. It is a curated, task-specific extract assembled on demand. It includes only what the agent needs for the current operation and excludes everything else. A context pack is also not an [[Authority Pack]] — it provides knowledge context, not governance constraints. Both are loaded before task execution, but they serve distinct functions.

## Purpose

Context packs ensure agents operate with the right knowledge for the right task, without polluting working memory with irrelevant information. The quality of an agent's output is bounded by the quality of its context pack — an agent with correct authority but incorrect context will produce governed but wrong results.

## Key Components

- **Knowledge graph nodes** — relevant entity relationships from the [[Knowledge Graph Layer]]
- **Semantically retrieved documents** — similar past decisions, reference materials, or policies from the [[Vector Memory Layer]]
- **Structured operational records** — task history, metrics, and audit data from the [[Structured Data Layer]]
- **Task-specific instructions** — operational parameters for the current workflow step

## Example

Before processing a vendor invoice, an accounts-payable agent receives a context pack containing: the vendor's contract terms (knowledge graph), similar past invoices and their resolution history (vector memory), and the current purchase order record (structured data).

## Relationships

- [[Memory Architecture]] — the three-layer system from which context packs are assembled
- [[Context Pack Architecture]] — the system-level design of context pack assembly and delivery
- [[Memory Architecture Map]]
- [[Agent Maestro — Concepts Map]]
