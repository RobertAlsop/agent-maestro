---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Supervisor Agent"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "Agent Constellation]]"
  implements:
    - "[[Executive-Supervisor-Specialist Pattern]]"
  governs:
    - "[[Specialist Agent]]"
  inherits_from:
    - "[[Agent]]"
  applies_to: []
  uses:
    - "[[Decision Authority]]"
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

# Supervisor Agent

## Definition

An agent operating at the coordination layer of an Agent Constellation]] — responsible for managing workflows, delegating tasks to [[Specialist Agent|Specialist Agents]], enforcing the authority contracts of its team, and escalating to the [[Executive Agent]] when decisions exceed its scope.

## Boundaries

A Supervisor Agent coordinates and delegates — it does not directly execute specialist tasks, nor does it make constellation-level strategic decisions. The Supervisor layer is specifically the middle tier of the [[Executive-Supervisor-Specialist Pattern]]: below executive-level authority, above task execution.

## Purpose

Supervisor Agents provide the coordination layer that makes constellations scalable. Without supervisors, an executive agent would need to manage every specialist directly — which does not scale. Supervisors handle workflow orchestration and task allocation within a bounded domain, allowing the executive to focus on strategic authority and escalation.

## Responsibilities

- Receives task assignments and authority delegation from the [[Executive Agent]]
- Decomposes tasks and delegates to appropriate [[Specialist Agent|Specialist Agents]]
- Monitors specialist execution and enforces evidence requirements
- Escalates decisions that exceed its authority scope to the Executive Agent
- Does not execute specialist tasks directly

## Relationships

- [[Executive Agent]] — receives authority delegation from; escalates to
- [[Specialist Agent]] — delegates tasks to; monitors
- [[Decision Authority]] — exercises bounded decision authority within its domain
- [[Executive-Supervisor-Specialist Pattern]] — the pattern that defines this role
- Agent Constellation]] — the constellation context in which supervisors operate
- [[Agent Maestro — Agent Taxonomy Map]]
- [[Agent Maestro — Concepts Map]]
