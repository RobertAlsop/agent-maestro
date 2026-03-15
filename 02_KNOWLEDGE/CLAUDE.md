# 02_KNOWLEDGE

## Purpose

The KNOWLEDGE layer is the authoritative knowledge base for Agent Maestro. It contains the concepts, patterns, governance principles, system maps, and reference materials that define how the system is designed and operated. Knowledge notes form a semantic graph via wiki-links and typed relationships, enabling agents and humans to understand both individual concepts and how they fit into larger architectural patterns.

The layer has two critical properties:
- **Canonical**: Notes here are the single source of truth
- **Governed**: Changes to canonical notes follow escalation procedures based on authority_weight

## Structure

- **concepts/**: Core concepts and definitions (e.g., Agent, Authority Model, Agent Constellation)
- **patterns/**: Design patterns and architectural approaches (e.g., Authority Pack Grammar, Host Binding Pattern, Governance Compilation Pattern)
- **governance/**: Highest-authority governance documents (North Star, Principles, Modes, Strategy, Scope, Vault Rules) — authority_weight ≥ 90
- **domains/**: Thematic knowledge domains (e.g., Authority Systems, Human-Agent Collaboration, Operational Transformation)
- **system_maps/**: System diagrams and relationship maps (e.g., Navigation Map, Stack Map, Agent Taxonomy Map, Governance Artifacts Map)
- **references/**: Reference materials and schemas (e.g., Governance Schemas Reference, Tool and Action Class Reference, Compiler Artifact Schemas Reference)
- **indexes/**: Navigational indexes and category listings (e.g., All Concepts Index, All Patterns Index, All Domains Index)

## Conventions

### Frontmatter Requirements
All notes in KNOWLEDGE must include YAML frontmatter with:
- `title`: Note title (matches filename)
- `schema_version`: 2
- `type`: concept | pattern | governance | domain | system_map | reference | index
- `tags`: Comma-separated list of tags
- `authority_weight`: 0-100 (see below)
- `relationships`: Dictionary of typed links to other notes
- `created_date`: YYYY-MM-DD
- `last_modified`: YYYY-MM-DD

### Authority Weight Scale
- **90-100**: Canonical governance (North Star, Principles, Scope, Strategy) — human approval required for changes
- **70-89**: High-authority patterns and concepts — human review recommended for changes
- **50-69**: Standard knowledge and reference material — agent updates acceptable with relationship management
- **0-49**: Exploratory or draft knowledge — agent updates acceptable

### Wiki-Links & Relationships
- Links use `[[Note Name]]` format
- Frontmatter relationships use typed edges:
  - `defines`: This concept defines another
  - `part_of`: This is part of a larger concept
  - `implements`: This pattern implements a principle
  - `governs`: This document governs how something works
  - `inherits_from`: This inherits properties or rules from another
  - `applies_to`: This applies to a specific system or domain
  - `uses`: This uses or depends on another
  - `produces`: This produces or creates another

## Agent Rules

**Agents MAY**:
- Read all knowledge notes for guidance
- Create new knowledge notes following the frontmatter schema
- Update relationships in frontmatter of notes with authority_weight < 90
- Add or refine wiki-links between related concepts

**Agents MUST NOT**:
- Modify the content of notes with authority_weight ≥ 90 (escalate to human)
- Delete knowledge notes without escalation
- Change the `type` field of existing notes without escalation
- Create notes that violate the schema or lack required frontmatter

**Escalation Required**:
- Any modification to governance documents (Principles, North Star, Scope, Strategy, Modes, Vault Rules)
- Significant rewrites of high-authority patterns (authority_weight ≥ 70)
- Deletion of any canonical knowledge note

## Key Files

### Governance (authority_weight ≥ 90)
- **Agent Maestro — North Star**: Core vision and strategic intent
- **Agent Maestro — Principles**: 12 foundational principles (read daily)
- **Agent Maestro — Modes**: Three operational modes (Design, Governance, Execution)
- **Agent Maestro — Scope**: What Agent Maestro does and does not cover
- **Agent Maestro — Strategy**: Strategic approach and key initiatives
- **Agent Maestro — Vault Rules**: Vault organization and content management rules

Location: `02_KNOWLEDGE/governance/`

### Core Concepts
- Agent, Authority Model, Execution Authority, Memory Architecture, Supervisor Agent
- Operational Outcome, Authority Inheritance, Authority Pack, Authority Architecture
- Agent Constellation, Host Binding, Human Escalation, Executive Agent, Context Pack
- Agent System, Agent Workflow, Compiled Governance Artifact, Agent Orchestration
- Agent Systems, Agent Ecosystem, Operational Intelligence, Model Workspace Protocol
- Specialist Agent, Pack Versioning, Decision Authority

Location: `02_KNOWLEDGE/concepts/`

### Key Patterns
- Authority Pack Grammar, Deterministic Control Surfaces, Thin-Edge Thick-Core Pattern
- Pack Versioning Pattern, Authority Inheritance Pattern, Evidence Over Assumptions
- Executive-Supervisor-Specialist Pattern, Decision-Execution Separation
- Constellation Architecture Pattern, Host Binding Pattern, Model Workspace Protocol Pattern
- Three-Layer Memory Model, Pack Override Rules, Human Escalation Pattern
- Anti-Agent-Sprawl Pattern, Controlled Evolution Pattern, Governance Before Autonomy
- Governance Compilation Pattern, Policy Resolution Pattern

Location: `02_KNOWLEDGE/patterns/`

### System Maps
Maps that show relationships between major system components:
- Agent Maestro — Navigation Map, Concepts Map, Constellation Architecture Map
- Pipelines Map, Governance Artifacts Map, Project Governance Map
- Projects & Experiments Map, Authority Architecture Map, Governance Map
- Stack Map, Systems Map, Agent Taxonomy Map, Domain Map
- Pack Inheritance Map, Practice Map, Layer Model Map, Operational Intelligence Map

Location: `02_KNOWLEDGE/system_maps/`

### Domains
Thematic knowledge domains for different aspects of Agent Maestro:
- Operational Transformation, Authority Systems, Human-Agent Collaboration
- AI Executive Systems, Multi-Agent Coordination, Governance Infrastructure
- Operational Governance, Organizational Intelligence, Workflow Intelligence
- Governance Systems, AI-Native Organizations, Platformization, Agent Organizations

Location: `02_KNOWLEDGE/domains/`

### References
- Governance Schemas Reference, Tool and Action Class Reference
- Compiler Artifact Schemas Reference, Escalation Classes Reference, Host Runtime Reference

Location: `02_KNOWLEDGE/references/`

## Relationship to Authority Layer

KNOWLEDGE serves as the blueprint for the Authority Layer (05_SYSTEMS/authority_architecture). Authority packs are compiled from patterns and governance documents in KNOWLEDGE. Changes to KNOWLEDGE may require recompilation of authority packs in 05_SYSTEMS.

See CLAUDE]] in 05_SYSTEMS/authority_architecture/ for details on how knowledge is transformed into compiled governance artifacts.
