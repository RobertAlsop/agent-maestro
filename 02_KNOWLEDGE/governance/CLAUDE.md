# 02_KNOWLEDGE/governance

## Purpose

The governance subdirectory contains the **highest-authority documents** in the entire Agent Maestro vault. These are canonical documents that define the principles, vision, scope, and strategic direction for all agent systems, governance approaches, and operational modes. They represent the immutable foundation upon which all other systems are built.

Every note in this directory has `authority_weight: 90` (or higher) and requires explicit human approval for any modifications.

## Documents (All canonical, authority_weight ≥ 90)

- **Agent Maestro — North Star**: The core vision and strategic intent. Defines why Agent Maestro exists and what success looks like.
- **Agent Maestro — Principles**: The 12 foundational principles that govern all design decisions, governance approaches, and operational practices. This is the most-referenced document in the system.
- **Agent Maestro — Modes**: The three operational modes: Design Mode (building systems), Governance Mode (defining rules), and Execution Mode (running operations). These modes sequence how the system evolves.
- **Agent Maestro — Scope**: Explicitly defines what Agent Maestro does and does not cover. Essential for boundary-setting.
- **Agent Maestro — Strategy**: The strategic approach, key initiatives, and how Agent Maestro is being deployed.
- **Agent Maestro — Vault Rules**: Rules and conventions for vault organization, note structure, and content management.

All files located in `/sessions/loving-busy-bohr/mnt/Agent Maestro/02_KNOWLEDGE/governance/`

## Conventions

- **No frontmatter variations**: All governance notes must follow the standard schema
- **Read-before-building**: Before starting work in any layer, read the relevant sections of Principles
- **Citation required**: When referencing governance documents, use full wiki-link format: `[[Agent Maestro — Principles]]`
- **Immutability principle**: These documents change infrequently and only through deliberate governance processes

## Agent Rules

**Agents MAY**:
- Read all governance documents (mandatory before starting work)
- Reference these documents when explaining decisions
- Create new notes in 02_KNOWLEDGE that cite and implement these principles
- Suggest improvements or modifications (via escalation)

**Agents MUST NOT**:
- Modify the content of any governance document
- Reinterpret or override these principles
- Create new "authority_weight: 90+" documents without explicit approval
- Delete or archive governance documents

**Escalation Required**:
- ANY modification to ANY governance document
- Proposals to add new canonical principles or scope statements
- Requests to change the Three-Mode model (Design, Governance, Execution)

## Critical Documents to Know

When working in Agent Maestro, these documents guide every decision:

1. **[[Agent Maestro — Principles]]**: Read the relevant principle before making design decisions
2. **[[Agent Maestro — North Star]]**: Understand the vision before proposing changes to scope or strategy
3. **[[Agent Maestro — Modes]]**: Know which mode you're operating in (Design/Governance/Execution)
4. **[[Agent Maestro — Scope]]**: Understand boundaries before suggesting new capabilities
5. **[[Agent Maestro — Vault Rules]]**: Follow naming, frontmatter, and structural conventions

## Relationship to Authority Architecture

These governance documents are the source material for the **Authority Pack Compiler** in 05_SYSTEMS/authority_architecture/compiler/. The compiler transforms these principles and scope statements into executable authority packs, compiled governance artifacts, and host bindings.

Changes to governance documents may trigger recompilation of authority packs. See [[02_Systems/Agent Maestro/02_KNOWLEDGE/governance/CLAUDE]] in 05_SYSTEMS/authority_architecture/compiler/ for the compilation pipeline.
