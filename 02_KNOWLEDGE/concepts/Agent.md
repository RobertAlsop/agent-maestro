---
id: CON.agent
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
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
review_cycle: none

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[Agent Systems]]"
    - "[[Agent Workflow]]"
  implements:
    - "[[Anti-Agent-Sprawl Pattern]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[Context Pack]]"
    - "[[Decision Authority]]"
    - "[[Execution Authority]]"
  produces:
    - "[[Operational Outcome]]"

map: "[[Agent Maestro — Concepts Map]]"
maps: []

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

# Agent

## Definition

An autonomous software process that perceives context, reasons over it, and executes actions within defined authority boundaries. An agent is the fundamental execution unit of [[Agent Systems]] — the smallest entity capable of producing an [[Operational Outcome]] independently.

An agent is not a model. A model provides reasoning capability; an agent combines that capability with perception, authority constraints, and action within a governed environment.

## Purpose

Agents exist to translate organizational intent into measurable operational results. Every agent must operate under an [[Authority Pack]] that defines its decision scope, permitted actions, and escalation triggers. Without this governance binding, a software process is an automation script, not an agent. See [[Anti-Agent-Sprawl Pattern]].

## Key Components

- **Perception** — intake of task context via a [[Context Pack]], scoped to what the agent needs for the current operation
- **Reasoning** — selection among options within the agent's [[Decision Authority]]
- **Execution** — action on external systems within the agent's [[Execution Authority]]
- **Escalation** — handoff to a human or higher-authority agent when the current authority boundary is reached. See [[Human Escalation Pattern]]

## Example

A document-review agent perceives an incoming contract (perception), evaluates it against stored compliance rules (reasoning), flags non-compliant clauses (execution), and escalates ambiguous terms to a human reviewer (escalation).

## Relationships

- [[Agent Workflow]] — the structured sequence an agent operates within
- [[Agent Orchestration]] — the coordination layer that routes tasks to agents
- [[Agent Runtime Architecture]] — the infrastructure that hosts agent execution
- [[Agent Maestro — Concepts Map]]
