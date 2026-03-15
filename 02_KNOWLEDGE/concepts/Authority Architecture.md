---
id: CON.authority_architecture
type: concept
note_class: knowledge
domain: ai_governance
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
  defines:
    - "[[Authority Pack]]"
    - "[[Decision Authority]]"
    - "[[Execution Authority]]"
  part_of: []
  implements:
    - "[[Governance Before Autonomy]]"
  governs:
    - "[[Agent]]"
  inherits_from: []
  applies_to: []
  uses: []
  produces: []

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

# Authority Architecture

## Definition

The governance layer that defines what [[Agent|agents]] are permitted to decide, do, and escalate within an [[Agent Systems|agent system]]. Authority architecture is the structural answer to the question: *who is allowed to do what, under what conditions, with what evidence?*

## Boundaries

Authority architecture governs agent behaviour, not agent capability. It does not determine what an agent *can* do (that is model capability and tooling); it determines what an agent *may* do. The distinction is critical — capability without authority constraint is uncontrolled automation.

## Purpose

Per [[Agent Maestro — Principles]], the authority architecture matters more than the model. A weak model operating under strong authority constraints produces auditable, predictable results. A powerful model operating without authority constraints produces unaccountable risk. The pattern [[Governance Before Autonomy]] formalises this priority.

## Key Components

- [[Authority Pack]] — the modular, versioned governance contract assigned to each agent class
- [[Decision Authority]] — the bounded permission to select among options and commit to a course of action
- [[Execution Authority]] — the bounded permission to act on external systems
- [[Governance Before Autonomy]] — the foundational constraint requiring authority structures before agent deployment

## Relationships

- [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/Authority Architecture]] — the system-level implementation of authority architecture
- [[Authority Architecture Map]]
- [[Authority Packs Index]]
- [[Agent Maestro — Concepts Map]]
