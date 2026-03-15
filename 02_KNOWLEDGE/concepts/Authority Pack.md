---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Authority Pack"
status: active
review_status: draft
version: 1
created_date: 2026-03-10
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines:
    - "[[Decision Authority]]"
    - "[[Execution Authority]]"
  part_of:
    - "Authority Architecture]]"
  implements: []
  governs:
    - "[[Agent]]"
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
hash: ""
---

# Authority Pack

## Definition

A modular, versioned governance contract that defines what a specific class of [[Agent|agent]] is permitted to decide, execute, and escalate. An authority pack is the atomic unit of Authority Architecture]] — the smallest self-contained governance specification that can be assigned to an agent or agent class.

## Boundaries

An authority pack governs a *class* of agent, not a single agent instance. Multiple agents of the same class share the same authority pack. An authority pack does not define agent logic or tooling — it defines the constraints within which any agent of that class must operate.

## Purpose

Authority packs make governance composable and auditable. Because they follow a standardised structure (the [[Authority Pack Grammar]]), they can be versioned, compared, and composed without ambiguity. Per [[Governance Before Autonomy]], no agent may be deployed without a corresponding authority pack.

## Key Components

Structured using the [[Authority Pack Grammar]] (sections 00–13):

- **Identity and scope** — what this pack governs and where it applies
- **Governed entities and actions** — which agents and which action classes fall under this contract
- **Rules and control gates** — the constraints and checkpoints agents must respect
- **Evidence requirements** — what must be recorded for auditability
- **Interaction contracts** — how this pack's agents interact with agents under other packs
- **Failure semantics** — what happens when an agent violates a constraint or encounters an unhandled condition

## Example

A Customer Support Agent may operate under an authority pack that specifies: which backend systems the agent may query (governed actions), which actions — such as issuing refunds above a threshold — require escalation to a human (control gates), and which evidence — such as conversation logs and decision rationale — must be recorded for every interaction (evidence requirements).

## Relationships

- [[Decision Authority]] — the bounded permission to decide, which this pack specifies
- [[Execution Authority]] — the bounded permission to act, which this pack specifies
- [[Authority Packs Index]] — the registry of all authority packs in the system
- Authority Model]] — the formal model within which packs are defined
- [[Authority Architecture Map]]
- [[Agent Maestro — Concepts Map]]
