---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Specialist Agent"
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
  governs: []
  inherits_from:
    - "[[Agent]]"
  applies_to: []
  uses:
    - "[[Execution Authority]]"
  produces: []
  - "[[Agent Maestro — Concepts Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - agent_type
hash: ""
---

# Specialist Agent

## Definition

An agent operating at the task-execution layer of an [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — focused on performing well-defined, bounded tasks within a narrow authority scope delegated by a [[Supervisor Agent]]. Specialist Agents are the workhorses of the constellation; they execute, not decide.

## Boundaries

A Specialist Agent should not make decisions outside its defined authority scope. If a decision is required that exceeds its authority, it must escalate to its [[Supervisor Agent]], not act autonomously. Specialist Agents are optimised for depth in a specific capability, not breadth.

## Purpose

Specialist Agents enable deep capability within a governed constraint. By keeping execution authority narrow and clearly bounded, they make agent behaviour predictable, testable, and auditable. Their narrow scope also makes them the easiest agents to evaluate for reliability.

## Responsibilities

- Executes well-defined tasks within its authority pack scope
- Uses only the tools and data sources declared in its authority pack
- Produces outputs that meet the evidence requirements of its pack
- Escalates immediately when a task requires out-of-scope authority
- Cannot delegate to other agents — delegation is the supervisor's role

## Relationships

- [[Supervisor Agent]] — the agent that assigns tasks and receives outputs
- [[Execution Authority]] — the core authority type the Specialist Agent exercises
- [[Executive-Supervisor-Specialist Pattern]] — the pattern that defines this role
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — the constellation context in which specialists operate
- [[Agent Maestro — Agent Taxonomy Map]]
- [[Agent Maestro — Concepts Map]]
