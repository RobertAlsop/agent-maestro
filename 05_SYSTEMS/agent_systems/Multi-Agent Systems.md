---
id: SYS.multi_agent_systems
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

map: "[[Agent Maestro — Systems Map]]"
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

# Multi-Agent Systems

## Purpose

Defines the architecture and coordination patterns for systems where multiple agents collaborate to complete complex tasks.

## Responsibilities

- Define inter-agent communication protocols
- Manage task routing and delegation
- Enforce authority boundaries across agent interactions
- Prevent agent sprawl — see [[Anti-Agent-Sprawl Pattern]]

## Core Components

- Orchestration layer
- Agent registry
- Task routing engine
- Conflict resolution rules

## Interfaces

- [[Agent Runtime Architecture]] — per-agent execution
- Orchestration authority pack

## Invariants

- Every agent has a unique, registered identity
- Inter-agent handoffs must preserve authority context

## Related Concepts

- [[Agent Orchestration]]
- [[Agent Systems]]
