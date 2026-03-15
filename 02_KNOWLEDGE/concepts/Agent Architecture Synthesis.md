---
id: CON.agent_architecture_synthesis
type: concept
note_class: knowledge
domain: agent_maestro
layer: knowledge
schema_version: 2
status: active
review_status: reviewed
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
authority_weight: 60
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Agent Maestro — Concepts Map]]"
    - "[[Agent Maestro — Constellation Architecture Map]]"
  implements:
    - "[[Constellation Architecture Pattern]]"
    - "[[Executive-Supervisor-Specialist Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent System]]"
  uses:
    - "[[Authority Pack]]"
    - "[[Agent Constellation]]"
  produces: []
tags:
  - concept
  - agent_maestro
  - synthesis
  - constellation
  - vault_architecture
---

# Agent Architecture Synthesis

## Purpose

A synthesis reference documenting the core architectural vocabulary of Agent Maestro: the relationships between agents, authority packs, constellations, and the vault structure. This note integrates definitions from early vault conception.

## The Three Vault Layers

The vault has three major layers:

1. **Knowledge (discipline)** — the concepts, maps, and governance that define what Agent Maestro is
2. **Authority architecture** — how authority works everywhere; the governance substrate
3. **Agent systems** — the actual operational constellations

## Core Vocabulary

| Term | Definition |
|------|-----------|
| **Agent** | An entity that operates within defined authority boundaries to perceive, decide, and act |
| **Authority Pack** | A modular, versioned governance contract defining what an agent class may decide, execute, and escalate |
| **Constellation** | An operational grouping of agents, supervisors, workflows, memory, and authority links organized around a domain or capability |
| **Executive** | A meta-agent that coordinates, governs, or directs — not a frontline worker |
| **Supervisor** | An agent that manages a domain or workflow end-to-end, sitting below executives and above specialists |
| **Specialist** | A task-performing agent operating within a specific function (writing, email, data, etc.) |

## The Mental Model

```
Executives define direction
Supervisors run domains
Specialists do tasks
Authority packs govern all of them
Constellations group them into operational systems
Obsidian vault makes them all visible
```

## Constellation Structure

Each constellation contains all three triangle dimensions:

```
marketing_constellation/
  00_map/             MAP.marketing_constellation
  01_executive_links/ EXEC.marketing.executive_interface
  02_supervisors/     SUP.marketing.supervisor
  03_specialists/     AGENT.writer, AGENT.editor, AGENT.email
  04_workflows/       WF.campaign_build, WF.content_pipeline
  05_memory/          MEM.marketing.sources
  06_authority_links/ PACK.marketing.supervisor, PACK.content.specialists
  07_metrics/         MET.marketing.scorecard
```

## Vault Structure That Supports This

```
05_SYSTEMS/
  authority_architecture/
    maps/
    templates/
    packs/
      conceptual_authority/
      executive/
      supervisor/
      specialist/
      domain/
  agent_systems/
    constellations/
      marketing_constellation/
      customer_support_constellation/
    shared_services/
      memory_services/
      audit_services/
      governance_services/
      orchestration_services/
```

## The Network, Not the Hierarchy

When mapped in Obsidian graphs, Agent Maestro doesn't appear as a hierarchy — it appears as **clusters** (constellations). Each constellation connects to others like a network. This is by design:

- Authority packs are reusable governance modules
- Constellations are operational groupings
- New constellations can reuse existing packs

This aligns with the principle of **composable architecture**.

## The Big Picture

Agent Maestro is essentially an operating system for AI organizations, where:

- **Authority packs** = governance modules
- **Agent systems** = operational constellations
- **Vault** = architecture knowledge base

```
Human CEO
     │
AI Executive Layer
     │
Triangular Infrastructure
(Governance / Operations / Intelligence)
     │
Operational Agent Ecosystem
(Supervisors + Specialists)
```

## Relationships

- [[Agent Constellation]] — the operational grouping concept
- [[Authority Pack]] — the governance mechanism
- [[Executive Agent]] — the executive layer
- [[Supervisor Agent]] — the supervisor layer
- [[Specialist Agent]] — the specialist layer
- [[Constellation Architecture Pattern]] — the architectural pattern
- [[Executive-Supervisor-Specialist Pattern]] — the hierarchy pattern
- [[Agent Organization Architecture]] — more detailed treatment of organization structure
- [[Agent Maestro — Constellation Architecture Map]] — the system map
