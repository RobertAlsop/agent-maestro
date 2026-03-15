---
id: MAP.agent_maestro.agent_taxonomy
type: system_map
note_class: architecture
domain: agent_architecture
layer: maps
scope:
canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: approved
version: 1
created: 2026-03-12
updated: 2026-03-12
last_reviewed:
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
map: "[[Agent Maestro — Navigation Map]]"
maps: []
related: []
related_maps:
  - "[[Agent Maestro — Concepts Map]]"
  - "[[Agent Maestro — Systems Map]]"
  - "[[Agent Maestro — Constellation Architecture Map]]"
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - map
  - taxonomy
  - agents
hash: ""
---

# Agent Maestro — Agent Taxonomy Map

## Purpose

Canonical taxonomy of all agent types recognised by Agent Maestro, organised by role and governance layer.

---

## Foundational Agent Type

- [[Agent]] — the base concept; all other types are specialisations

---

## By Governance Layer

### Executive Layer
- [[Executive Agent]] — sets direction, allocates authority, owns outcomes at the constellation level

### Supervisor Layer
- [[Supervisor Agent]] — manages workflows, coordinates specialists, enforces authority contracts

### Specialist Layer
- [[Specialist Agent]] — executes well-defined tasks within a bounded authority scope

---

## By Structural Role

| Role | Type | Authority Source |
|---|---|---|
| Constellation head | [[Executive Agent]] | Assigned by [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] governance |
| Workflow coordinator | [[Supervisor Agent]] | Delegated by Executive |
| Task executor | [[Specialist Agent]] | Delegated by Supervisor |

---

## Agent Grouping Concepts

- [[Agent System]] — a bounded collection of agents delivering a function
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — a governed cluster of agents with shared authority architecture
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] — the full organisational deployment of agent systems

---

## Governance Relationship

Every agent in the taxonomy operates under an [[Authority Pack]]. The [[Executive-Supervisor-Specialist Pattern]] defines the structural rules for composing these types into a [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation|constellation]].

---

## Related Maps

- [[Agent Maestro — Concepts Map]]
- [[Agent Maestro — Constellation Architecture Map]]
- [[Agent Maestro — Systems Map]]
- [[Agent Maestro — Navigation Map]]
