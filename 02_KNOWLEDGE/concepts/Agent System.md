---
id: CON.agent_system
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
scope:
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: draft
version: 1
created: 2026-03-12
updated: 2026-03-14
last_reviewed:
review_cycle: none
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]]"
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[Agent]]"
    - "[[Authority Pack]]"
  produces:
    - "[[Operational Outcome]]"
map: "[[Agent Maestro — Concepts Map]]"
maps:
  - "[[Agent Maestro — Systems Map]]"
related: []
related_maps: []
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
hash: ""
---

# Agent System

## Definition

A bounded collection of one or more [[Agent|agents]] organised to deliver a specific operational capability. An Agent System has defined inputs, outputs, and an authority scope. It is the smallest unit of organised multi-agent work.

## Boundaries

An Agent System is not the same as a single agent (too small) or an [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] (which implies a specific three-layer governed structure). A system may be as simple as two agents working in sequence or as complex as a layered workflow, as long as it has defined scope and delivers a coherent output.

## Purpose

The Agent System concept provides a bounded unit of analysis for designing, deploying, and governing agent-based capabilities. Every system should be addressable in the [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]] and governed by at least one [[Authority Pack]].

## Key Properties

- **Bounded** — has defined inputs, outputs, and scope
- **Governed** — operates under an authority pack or pack set
- **Deployable** — can be instantiated and run in a runtime environment
- **Registrable** — resolvable via the [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]

## Relationships

- [[Agent]] — the individual agents that make up a system
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — a governed layered structure containing systems
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] — the organisational context containing systems
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]] — authoritative registry for all systems
- [[Agent Maestro — Systems Map]] — navigation for the systems layer
- [[Agent Maestro — Concepts Map]]
