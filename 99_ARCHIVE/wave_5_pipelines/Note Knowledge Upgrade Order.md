---
id: PIPE.note_knowledge_upgrade_order
type: pipeline
note_class: execution
domain: agent_maestro
layer: pipes
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
    - "[[Note Upgrade Workflow]]"
    - "[[Maintenance Pipeline]]"
  implements:
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
  uses: []
  produces: []
tags:
  - pipeline
  - maintenance
  - note_upgrade
  - knowledge_order
  - agent_maestro
---

# Note Knowledge Upgrade Order

## Purpose

Defines the recommended processing order for upgrading vault notes. The order ensures that notes which others depend on are upgraded first, producing consistent, well-linked knowledge.

## The Recommended Order

```
1.  Governance doctrine
2.  Keystone concepts
3.  Domains
4.  Patterns
5.  Indexes / registries
6.  System maps
7.  Agent systems
8.  Authority architecture (concept layer)
9.  Compiler subsystem
10. Memory architecture
11. Infrastructure
12. Operational intelligence
13. Organizational integration
14. Authority architecture / templates
15. Authority packs
```

## Rationale by Layer

### 1. Governance Doctrine First (`02_KNOWLEDGE/governance/`)
Notes: North Star, Scope, Principles, Modes, Strategy

Everything else in the vault should align with governance documents. Upgrading these first ensures all subsequent notes are written consistently.

### 2. Keystone Concepts (`02_KNOWLEDGE/concepts/`)
Notes: Agent, Agent Systems, Authority Architecture, Memory Architecture, Operational Intelligence, Agent Workflow, Agent Orchestration, Authority Pack, Decision Authority, Execution Authority, Context Pack, Operational Outcome

Goal: strong definitions, internal links, clear concept boundaries. These form the core ontology of the discipline.

### 3. Domain Layer (`02_KNOWLEDGE/domains/`)
Notes: AI-Native Organizations, Operational Transformation, Human-Agent Collaboration, Workflow Intelligence, Governance Systems

Goal: contextualize concepts for where Agent Maestro applies in the world.

### 4. Pattern Library (`02_KNOWLEDGE/patterns/`)
Notes: Governance Before Autonomy, Three-Layer Memory Model, Decision-Execution Separation, Anti-Agent-Sprawl Pattern, Deterministic Control Surfaces

Goal: translate concepts into reusable mechanisms.

### 5. System Architecture Layer (`05_SYSTEMS/`)
Notes: Agent System Architecture, Agent Runtime Architecture, Memory Model, Context Pack Architecture, AI Operations, Operational Agent Design, Observability, Governance Integration

Goal: describe how the discipline is implemented.

### 6. Maps (refinement pass) (`02_KNOWLEDGE/system_maps/`)
After concepts are richer, update map connections, hierarchy, and navigation.

### 7. Pipelines (`03_PIPELINES/`)
Notes: Exploration Pipeline, Development Pipeline, Agent Deployment Pipeline, Learning Pipeline

Goal: explain how systems are built and evolved.

### 8. Authority Packs Last (`05_SYSTEMS/authority_architecture/packs/`)
Reason: authority packs encode operational governance. They should be written after concepts, patterns, and systems are established — otherwise structure will be invented prematurely.

## The Development Order Summary

```
1 Governance
2 Concepts
3 Domains
4 Patterns
5 Systems
6 Maps refinement
7 Pipelines
8 Authority packs
```

This builds the vault top-down conceptually, not just structurally.

## Post-Upgrade Audit Sequence

After each upgrade pass:

```
knowledge upgrade complete
        ↓
definition alignment audit
        ↓
ontology integrity audit
        ↓
reasoning path audit
```

## Audit Cadence

| Audit | Frequency |
|-------|-----------|
| Vault Integrity & Self-Healing | Weekly |
| Definition Alignment | During upgrades |
| Ontology Integrity | After upgrades |
| Reasoning Path | After upgrades |

## Relationships

- [[Note Upgrade Workflow]] — the parent workflow this sequence serves
- [[Maintenance Pipeline]] — the pipeline this is part of
- [[Agent Maestro — Vault Rules]] — the governance this implements
