---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Executive Agent"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  implements:
    - "[[Executive-Supervisor-Specialist Pattern]]"
  governs:
    - "[[Supervisor Agent]]"
  inherits_from:
    - "[[Agent]]"
  applies_to: []
  uses:
    - "[[Decision Authority]]"
    - "[[Authority Pack]]"
  produces: []
  - "[[Agent Maestro — Concepts Map]]"
  - "[[Agent Maestro — Constellation Architecture Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - agent_type
hash: ""
---

# Executive Agent

## Definition

An agent operating at the top governance layer of an [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — responsible for setting direction, allocating authority to supervisors, managing constellation-level outcomes, and escalating to human operators when required. The Executive Agent is the authority anchor of a constellation.

## Boundaries

An Executive Agent is not a general-purpose orchestrator or a simple routing agent. It has explicitly bounded authority defined by its [[Authority Pack]], including specific rules about what it may decide autonomously, what must be delegated to [[Supervisor Agent|Supervisor Agents]], and what must be escalated via [[Human Escalation]]. Not every agent system requires an Executive Agent — only governed constellations.

## Purpose

The Executive Agent brings accountability to multi-agent systems. By designating one agent as the governance head of a constellation, Agent Maestro creates a single point of authority accountability — a bounded, auditable decision-maker whose scope is explicitly defined.

## Responsibilities

- Holds and enforces the constellation's top-level authority pack
- Allocates sub-authority to Supervisor Agents via delegated authority
- Owns escalation decisions — when to escalate to humans
- Monitors and reports on constellation-level outcomes
- Cannot directly execute specialist tasks — maintains separation of decision and execution

## Relationships

- [[Supervisor Agent]] — receives authority delegation from Executive Agent
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — the structural context the Executive Agent heads
- [[Decision Authority]] — the core authority type the Executive Agent exercises
- [[Executive-Supervisor-Specialist Pattern]] — the pattern that defines this role
- [[Human Escalation]] — the escalation mechanism the Executive Agent manages
- [[Agent Maestro — Agent Taxonomy Map]]
- [[Agent Maestro — Concepts Map]]
