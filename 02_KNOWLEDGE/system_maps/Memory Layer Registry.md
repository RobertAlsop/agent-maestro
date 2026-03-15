---
schema_version: 2
title: "Memory Layer Registry"
tags:
  - memory
  - registry
  - architecture
  - system-map
relationships:
  part_of: "[[Memory Architecture Map]]"
  implements: "[[Memory Model]]"
  governs: []
  uses:
    - "[[Knowledge Graph Layer]]"
    - "[[Structured Data Layer]]"
    - "[[Vector Memory Layer]]"
  defines: []
  inherits_from: []
  applies_to: []
  produces: []
authority_weight: 70
created_date: 2026-03-15
last_modified: 2026-03-15
status: active
review_status: approved
version: 1
canonical: true
source_type: ai_authored
id: MAP.memory_layer_registry
type: map
note_class: architecture
layer: knowledge
---

# Memory Layer Registry

This document consolidates all memory types, their purpose, canonical locations, and access patterns in the Agent Maestro vault. It is the single reference for understanding where and how knowledge is stored and retrieved.

---

## Three-Layer Memory Model

Agent Maestro uses a three-layer memory architecture. Each layer serves a different purpose and has different access patterns.

| Layer | Purpose | Storage Format | Canonical Location | Architecture Doc |
|-------|---------|---------------|-------------------|-----------------|
| Knowledge Graph Layer | Semantic relationships between concepts, notes, and entities | Markdown notes with wiki-links + YAML frontmatter | `02_KNOWLEDGE/` (all subdirectories) | `05_SYSTEMS/memory_architecture/Knowledge Graph Layer.md` |
| Structured Data Layer | Tabular operational data, registries, logs, and indexes | CSV files | `05_SYSTEMS/` (registries) + `06_EXECUTION/logs/` | `05_SYSTEMS/memory_architecture/Structured Data Layer.md` |
| Vector Memory Layer | Semantic search and similarity matching (future) | Vector embeddings (not yet implemented) | TBD | `05_SYSTEMS/memory_architecture/Vector Memory Layer.md` |

---

## Knowledge Graph Layer — Memory Types

The Knowledge Graph Layer stores knowledge as interconnected markdown notes. Each note belongs to a memory type based on its `note_class` and location.

| Memory Type | Purpose | Canonical Location | Examples |
|-------------|---------|-------------------|----------|
| Concepts | Core concept definitions and their relationships | `02_KNOWLEDGE/concepts/` | Authority Pack, GovernedAgent, Constellation |
| Patterns | Reusable design and operational patterns | `02_KNOWLEDGE/patterns/` | Three-Layer Memory Model, Governance Before Autonomy |
| Governance | Foundational principles, rules, and constraints (highest authority) | `02_KNOWLEDGE/governance/` | Principles, North Star, Modes, Scope |
| Domains | Domain-specific knowledge collections | `02_KNOWLEDGE/domains/` | Agent Maestro domain knowledge |
| References | External references, citations, and research | `02_KNOWLEDGE/references/` | External papers, tools, frameworks |
| System Maps | Navigational indexes that connect related notes | `02_KNOWLEDGE/system_maps/` | SYSTEM_MAP.md, all 21 system maps |
| System Architecture | Implementation-level architecture documentation | `05_SYSTEMS/` (various subdirectories) | Authority Architecture, Memory Model, Agent Runtime Architecture |
| Constellation Definitions | Agent role definitions within constellations | `05_SYSTEMS/agent_systems/constellations/` | Vault Curator, Vault Maintenance agent definitions |
| Pipeline Definitions | Workflow stage definitions with entry/exit conditions | `03_PIPELINES/` | Build Session Protocol, Maintenance Pipeline |
| Project Documentation | Project plans, briefs, and tracking | `04_PROJECTS/` | v0.3 Build Brief |
| Captured Input | Unprocessed raw input awaiting classification | `01_CAPTURE/` | Raw notes, observations, drafts |
| Archived Knowledge | Historical and superseded content (read-only) | `99_ARCHIVE/` | Previous versions, deprecated content |

### Access Patterns — Knowledge Graph

| Operation | Method | Governance |
|-----------|--------|-----------|
| Read any note | Direct file access | All agents may read from all layers |
| Follow relationships | Parse frontmatter `relationships` field → resolve wiki-links | Standard navigation |
| Query by tag | Search `tags` field in frontmatter | Standard navigation |
| Query by authority weight | Filter `authority_weight` field | Used for conflict resolution |
| Create new note | Write to appropriate folder with valid frontmatter | Must follow schema_version: 2 template |
| Modify existing note | Edit content or frontmatter | Escalate if authority_weight >= 90 |
| Promote note | Move from 01_CAPTURE to canonical location | Requires classification + frontmatter enrichment |
| Archive note | Move to 99_ARCHIVE | Must log in state_change_log.csv |

---

## Structured Data Layer — Registry Types

The Structured Data Layer stores operational data in CSV format for machine-readable access.

| Registry | Path | Fields | Update Frequency |
|----------|------|--------|-----------------|
| Knowledge Graph Index | `02_KNOWLEDGE/indexes/knowledge_graph_index.csv` | All note metadata (title, path, tags, relationships, authority_weight) | Regenerated on demand |
| Authority Pack Registry | `05_SYSTEMS/authority_architecture/authority_pack_registry.csv` | pack_id, name, type, version, status, parent, constellation | Updated when packs change |
| Agent Registry | `05_SYSTEMS/agent_systems/agent_registry.csv` | agent_id, name, role, constellation, purpose, actions, pack_id | Updated when agents change |
| Constellation Registry | `05_SYSTEMS/agent_systems/constellation_registry.csv` | constellation_id, name, executive_agent, status | Updated when constellations change |
| Compiler Artifacts Registry | `05_SYSTEMS/authority_architecture/compiler/compiler_artifacts_registry.csv` | artifact_id, pack_id, version, compilation metadata | Updated by compiler (upsert) |
| Task Execution Log | `06_EXECUTION/logs/task_execution_log.csv` | Every attempt_action() call with result | Appended per action |
| Escalation Log | `06_EXECUTION/logs/escalation_log.csv` | All escalations raised by agents | Appended per escalation |
| State Change Log | `06_EXECUTION/logs/state_change_log.csv` | All vault modifications (create/modify/move/archive/delete/promote/repair) | Appended per change |
| Session Index | `06_EXECUTION/logs/sessions/session_index.csv` | Build session metadata | Appended per session |

### Access Patterns — Structured Data

| Operation | Method | Governance |
|-----------|--------|-----------|
| Read registry | Parse CSV with standard CSV reader | All agents may read |
| Query by field | Filter CSV rows by column value | Standard access |
| Append log entry | Append row to CSV | Agents write to 06_EXECUTION logs |
| Update registry | Upsert by primary key (pack_id, agent_id, etc.) | Must use defined update methods |
| Regenerate index | Run `generate_master_index.py` | Infrastructure tool |

---

## Vector Memory Layer (Future)

Not yet implemented. Planned for Wave 5+ as part of the execution architecture.

| Aspect | Design |
|--------|--------|
| Purpose | Enable semantic similarity search across vault content |
| Storage | Vector embeddings stored alongside or linked to source notes |
| Embedding Model | TBD (likely per-host configuration) |
| Access Pattern | Query by semantic similarity, retrieve ranked results |
| Governance | Read-only for agents; embedding generation requires approval |

---

## Context Pack Architecture

Context Packs are curated bundles of knowledge that agents load before executing tasks. They combine items from all three memory layers into a single coherent context.

| Aspect | Detail |
|--------|--------|
| Architecture Doc | `05_SYSTEMS/memory_architecture/Context Pack Architecture.md` |
| Purpose | Pre-assembled knowledge context for agent operations |
| Contents | Selected notes + registry data + relevant logs |
| Memory Governance | `05_SYSTEMS/memory_architecture/Memory Governance.md` |

---

## Related Documents

- [[Memory Architecture Map]] — Navigation map for all memory system notes
- [[Memory Model]] — Top-level architecture definition
- [[Memory Governance]] — Rules governing memory operations
- [[Structured Data Registry]] — `05_SYSTEMS/memory_architecture/Structured Data Registry.md`
- [[SYSTEM_MAP]] — Complete vault navigation index
