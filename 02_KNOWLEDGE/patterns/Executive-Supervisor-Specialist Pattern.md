---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Executive-Supervisor-Specialist Pattern"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  uses:
    - "[[Executive Agent]]"
    - "[[Supervisor Agent]]"
    - "[[Specialist Agent]]"
  produces: []
  - "[[Agent Maestro — Agent Taxonomy Map]]"
  - "[[Agent Maestro — Constellation Architecture Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - constellation
hash: ""
---

# Executive-Supervisor-Specialist Pattern

## Summary

Structure governed agent constellations as three explicit layers: an Executive Agent that owns authority and outcomes, Supervisor Agents that coordinate workflows and delegate tasks, and Specialist Agents that execute bounded tasks. Each layer has a distinct authority profile and escalation path.

## Problem

Without a defined authority hierarchy, multi-agent systems produce authority ambiguity — it is unclear who decides, who executes, and who is accountable.

## Solution

Apply three fixed governance layers:

| Layer | Role | Primary Authority | Escalates To |
|---|---|---|---|
| Executive | Direction + outcomes | Decision authority | Human operator |
| Supervisor | Coordination + delegation | Bounded decision + delegation | Executive |
| Specialist | Task execution | Execution authority | Supervisor |

## Rules

1. Every constellation must implement all three layers
2. No agent may exercise authority above its layer without explicit delegation
3. Delegation must flow downward only (Executive → Supervisor → Specialist)
4. Escalation must flow upward only (Specialist → Supervisor → Executive → Human)
5. Each layer's authority is defined by a separate authority pack section

## Relationships

- [[Executive Agent]] · [[Supervisor Agent]] · [[Specialist Agent]] — the three types
- [[Constellation Architecture Pattern]] — the broader pattern this is part of
- [[Decision Authority]] · [[Execution Authority]] — the authority types by layer
- [[Human Escalation]] — the top-of-chain escalation mechanism
- [[Agent Maestro — Agent Taxonomy Map]]
