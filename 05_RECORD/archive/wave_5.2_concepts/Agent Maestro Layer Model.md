---
type: concept
note_class: knowledge
domain: system_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Agent Maestro Layer Model"
status: active
review_status: draft
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent System]]"
    - "Agent Constellation]]"
    - "[[Memory Architecture]]"
    - "Authority Architecture]]"
  uses:
    - "[[Agent]]"
    - "[[Authority Pack]]"
    - "[[Memory Model]]"
    - "[[Model Workspace Protocol]]"
  produces: []
  - "[[Agent Maestro — Stack Map]]"
  - "[[Agent Maestro — Systems Map]]"
  - "[[Authority Pack]]"
  - "Agent Constellation]]"
  - "[[Model Workspace Protocol]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - layer_model
  - architecture
hash: ""
---

# Agent Maestro Layer Model

## Definition

The Agent Maestro Layer Model is a four-layer runtime architecture that organises every component of an Agent Maestro system into a clear execution stack. Each layer has a distinct responsibility, and layers communicate only through defined contracts.

## The Four Layers

```
Authority Layer      →  What may happen
     ↓
Agent Runtime        →  Who does it
     ↓
Workflow Layer       →  In what order
     ↓
Workspace Layer      →  Where it happens
```

### Authority Layer

The governance surface. Contains authority packs (design-time) and compiled governance artifacts (runtime). This layer exists in the vault under `05_SYSTEMS/authority_architecture/`.

The Authority Layer answers: what is this agent permitted to decide? What is it permitted to execute? Under what conditions? With what evidence?

### Agent Runtime

The execution surface. Contains agent definitions, constellation structures, and the [[Executive-Supervisor-Specialist Pattern]] hierarchy. This layer exists in `05_SYSTEMS/agent_systems/`.

The Agent Runtime answers: which agent is active? What role does it hold? Who does it report to? Who does it delegate to?

### Workflow Layer

The orchestration surface. Contains stage definitions, pipeline sequences, and task contracts. This layer exists in `03_PIPELINES/`.

The Workflow Layer answers: what stage is this execution in? What comes next? What are the entry and exit conditions?

### Workspace Layer

The operational surface. Defines the physical file structure an agent works within during execution. Governed by the [[Model Workspace Protocol]].

The Workspace Layer answers: what files does this agent have access to? Where does it read authority? Where does it write artifacts?

## Boundaries

The Layer Model is not a deployment topology — it does not prescribe servers, containers, or cloud services. It is a logical architecture that applies whether agents run locally, in the cloud, or within an Obsidian vault.

The Layer Model is also not a replacement for existing concepts. It organises them:

| Existing Concept | Layer Model Position |
|---|---|
| Authority Packs, Compiler, Governance | Authority Layer |
| Constellations, Agent Roles, Escalation | Agent Runtime |
| Pipelines, Stages | Workflow Layer |
| [[Model Workspace Protocol]] | Workspace Layer |

## Key Properties

- **Separation of concerns** — each layer has one job and a clear contract
- **Top-down authority** — governance flows downward from Authority Layer to Workspace Layer
- **Bottom-up evidence** — audit trails, execution logs, and artifacts flow upward
- **Layer independence** — changes to one layer do not require changes to others if contracts are preserved

## Relationships

- [[Model Workspace Protocol]] — defines the structure of the Workspace Layer
- Authority Architecture]] — the system that implements the Authority Layer
- Agent Constellation]] — the primary unit that operates across all four layers
- [[Agent Maestro — Layer Model Map]]
- [[Agent Maestro — Stack Map]]
