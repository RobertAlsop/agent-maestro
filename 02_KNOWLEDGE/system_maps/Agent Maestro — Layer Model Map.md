---
id: MAP.layer_model_map
type: map
note_class: navigation
domain: system_architecture
layer: knowledge
scope: null

canonical: false
authority_weight: 50
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-14
updated: 2026-03-14
last_reviewed: null
review_cycle: annual

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[Agent Maestro — Navigation Map]]"
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
  - "[[Agent Maestro — Stack Map]]"
  - "[[Agent Maestro — Systems Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - map
  - layer_model

hash: ""
---

# Agent Maestro — Layer Model Map

## Overview

This map navigates the Agent Maestro Layer Model — the four-layer runtime architecture that organises how agent systems execute.

## Core Concept

- [[Agent Maestro Layer Model]] — the four-layer runtime architecture

## The Four Layers

### Authority Layer — What may happen

| Component | Location |
|---|---|
| [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] | `05_SYSTEMS/authority_architecture/` |
| [[Authority Pack]] | `02_KNOWLEDGE/concepts/` |
| [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] | `05_SYSTEMS/authority_architecture/compiler/` |
| [[Compiled Governance Artifact]] | `05_SYSTEMS/authority_architecture/compiler/` |
| [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]] | `05_SYSTEMS/authority_architecture/` |

### Agent Runtime — Who does it

| Component | Location |
|---|---|
| [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] | `02_KNOWLEDGE/concepts/` |
| [[Executive Agent]] | `02_KNOWLEDGE/concepts/` |
| [[Supervisor Agent]] | `02_KNOWLEDGE/concepts/` |
| [[Specialist Agent]] | `02_KNOWLEDGE/concepts/` |
| [[Executive-Supervisor-Specialist Pattern]] | `02_KNOWLEDGE/patterns/` |

### Workflow Layer — In what order

| Component | Location |
|---|---|
| [[Exploration Pipeline]] | `03_PIPELINES/` |
| [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]] | `03_PIPELINES/` |
| [[System Design Pipeline]] | `03_PIPELINES/` |
| [[Agent Deployment Pipeline]] | `03_PIPELINES/` |
| [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]] | `03_PIPELINES/` |

### Workspace Layer — Where it happens

| Component | Location |
|---|---|
| [[Model Workspace Protocol]] | `02_KNOWLEDGE/concepts/` |
| [[Model Workspace Protocol Pattern]] | `02_KNOWLEDGE/patterns/` |
| [[Workspace Layer]] | `05_SYSTEMS/infrastructure/` |

## Design Pattern

- [[Model Workspace Protocol Pattern]] — how to build MWP workspaces

## Related Maps

- [[Agent Maestro — Stack Map]] — the technology stack view
- [[Agent Maestro — Systems Map]] — the system-level architecture view
- [[Agent Maestro — Navigation Map]] — the top-level vault navigation
