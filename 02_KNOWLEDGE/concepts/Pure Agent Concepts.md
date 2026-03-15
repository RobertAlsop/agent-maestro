---
id: CON.pure_agent_concepts
type: concept
note_class: knowledge
domain: agent_maestro
layer: knowledge
schema_version: 2
status: active
review_status: reviewed
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
authority_weight: 65
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines:
    - "[[Agent]]"
  part_of:
    - "[[Agent Maestro — Concepts Map]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent System]]"
  uses:
    - "[[Memory Architecture]]"
    - "[[Three-Layer Memory Model]]"
  produces: []
tags:
  - concept
  - agent_maestro
  - agent_loop
  - memory_architecture
  - primitives
---

# Pure Agent Concepts

## Purpose

Defines the irreducible primitives underneath all agent systems, independent of implementation. These concepts form the conceptual substrate from which all Agent Maestro architecture derives.

## The Irreducible Loop

If all hype is stripped away, an agent system is:

**perception → interpretation → decision → action → memory → feedback**

That is the irreducible loop. Everything else is an implementation detail.

## The Seven Essential Primitives

From that loop, the essential primitives are:

**1. State** — What is true right now?

**2. Goal** — What is the system trying to achieve?

**3. Policy** — What is allowed, forbidden, or preferred?

**4. Memory** — What from the past can influence the present?

**5. Tools** — What actions can the system take?

**6. Control** — Who decides, who checks, who can stop execution?

**7. Feedback** — How does the system learn whether the action worked?

A lot of "agent" talk skips straight to prompting, but prompting is only a small piece of the interpretation/decision layer. The real architecture is about how those seven primitives are designed and constrained.

## The First Principle: Where Does Authority Live?

The foundational question to return to in every AI system:

**Where does authority live?**

- Where does truth live?
- Where does memory live?
- Where do goals live?
- Where do permissions live?
- Where do actions get approved?
- Where do failures get recorded?

That one question exposes almost every weak system design.

## The Three-Layer Memory Architecture

**Knowledge** = relatively stable understanding
**Memory** = retrievable past experience
**State** = what is true now

These three must not be collapsed:

| Layer | Store | Purpose |
|-------|-------|---------|
| Knowledge | Obsidian | Conceptual memory — meaning, architecture, relationships |
| Memory | Vector DB | Associative recall — past experience, patterns |
| State | Database | Operational truth — what is true now |

This maps to the [[Three-Layer Memory Model]] pattern and the [[Memory Architecture]] concept.

## Real System Design Work

The real work is not "make an agent." It is:

- define memory layers
- define truth layers
- define action boundaries
- define control boundaries
- define feedback loops
- define human oversight points

This is systems architecture, not prompt engineering.

## Relationships

- [[Agent]] — the entity that operates this loop
- [[Memory Architecture]] — detailed treatment of the three memory layers
- [[Three-Layer Memory Model]] — the pattern form of this distinction
- [[Authority Pack]] — the mechanism that encodes Policy and Control
- [[Agent Maestro — Principles]] — the governance principles derived from these foundations
