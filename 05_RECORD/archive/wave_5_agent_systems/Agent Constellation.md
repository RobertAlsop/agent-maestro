---
type: system
note_class: architecture
domain: agent_architecture
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Agent Constellation"

status: active
review_status: approved
version: 1

created_date: 2026-03-12
last_modified: 2026-03-12

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

  - "[[Agent Maestro — Systems Map]]"


source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - system
  - agent_maestro
  - constellation

hash: ""
---

# Agent Constellation

## Purpose

System reference for governed agent constellations — defining the standard structure, governance requirements, and registration rules for all constellation instances in the vault.

## Context

A constellation is a governed cluster of agents: one [[Executive Agent]], one or more [[Supervisor Agent|Supervisor Agents]], and multiple [[Specialist Agent|Specialist Agents]], all operating under a shared Authority Architecture]]. This note defines the structural standard; individual constellation instances live in subdirectories of `05_SYSTEMS/agent_systems/constellations/`.

## Responsibilities

### Standard Folder Structure

Every constellation instance must follow this layout:

```
<constellation_name>/
  00_map/             — navigation map for this constellation
  01_executive_links/ — links to executive agent definitions
  02_supervisors/     — supervisor agent definitions
  03_specialists/     — specialist agent definitions
  04_workflows/       — workflow definitions
  05_memory/          — memory architecture for this constellation
  06_authority_links/ — links to applicable authority packs
  07_metrics/         — observability and metrics definitions
```

### Internal Components
- Executive Layer (→ `01_executive_links/`)
- Supervisor Layer (→ `02_supervisors/`)
- Specialist Layer (→ `03_specialists/`)
- Constellation Map (→ `00_map/`)
- Authority Links (→ `06_authority_links/`)

### Dependencies
- [[Executive Layer]] (system) — for executive agent definition
- Shared Services]] (system) — for shared operational capabilities
- Authority Architecture]] — for authority pack governance

### Failure Modes
- Authority pack missing or invalid → constellation cannot be activated
- Executive agent fails → constellation must halt and escalate to human

## Registry

All constellations must be registered in:
- [[Constellation Index]] — navigation index
- indexes/System Registry]] — authoritative system registry

## Relationships

- constellations/Agent Constellation]] (concept)
- [[Constellation Architecture Pattern]] — the design pattern
- [[Executive-Supervisor-Specialist Pattern]] — the layering pattern
- [[Agent Maestro — Constellation Architecture Map]]
