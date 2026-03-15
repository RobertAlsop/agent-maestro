---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Agent Constellation"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]]"
  implements:
    - "[[Constellation Architecture Pattern]]"
    - "[[Executive-Supervisor-Specialist Pattern]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[Agent System]]"
    - "[[Executive Agent]]"
    - "[[Supervisor Agent]]"
    - "[[Specialist Agent]]"
    - "[[Authority Pack]]"
  produces:
    - "[[Operational Outcome]]"
  - "[[Agent Maestro — Constellation Architecture Map]]"
  - "[[Agent Maestro — Agent Taxonomy Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - constellation
hash: ""
---

# Agent Constellation

## Definition

A governed cluster of agents — typically comprising an [[Executive Agent]], one or more [[Supervisor Agent|Supervisor Agents]], and multiple [[Specialist Agent|Specialist Agents]] — that operates under a shared [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] and delivers a coherent operational capability.

## Boundaries

An Agent Constellation is not the same as an [[Agent System]] (a general collection of agents delivering a function) or an [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] (the full organisational deployment). A constellation is specifically a *governed, layered cluster* with defined authority contracts at each layer. A constellation must have explicit authority governance; an informal group of agents does not qualify.

## Purpose

Constellations make multi-agent coordination governable. By structuring agents into a three-layer hierarchy — executive, supervisor, specialist — and applying authority packs at each layer, constellations ensure that decision authority, execution authority, and escalation behaviour are all explicitly defined and traceable.

## Key Properties

- **Governed** — every agent in the constellation operates under an [[Authority Pack]]
- **Layered** — follows the [[Executive-Supervisor-Specialist Pattern]]
- **Bounded** — has a defined operational scope and clear external interfaces
- **Composable** — can be nested within an [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]]

## Standard Structure

```
00_map/             — navigation map for this constellation
01_executive_links/ — links to executive agent definitions
02_supervisors/     — supervisor agent definitions
03_specialists/     — specialist agent definitions
04_workflows/       — workflow definitions
05_memory/          — memory architecture
06_authority_links/ — applicable authority packs
07_metrics/         — observability and metrics
```

## Relationships

- [[Agent System]] — simpler, less formal grouping; constellations add explicit governance
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] — constellations are components of an ecosystem
- [[Executive Agent]] — heads the constellation
- [[Constellation Architecture Pattern]] — design rules for building constellations
- [[Agent Maestro — Constellation Architecture Map]]
- [[Agent Maestro — Concepts Map]]
