# 05_SYSTEMS

## Purpose

The SYSTEMS layer is the implementation-level architecture for Agent Maestro. This is the most governance-sensitive layer because changes here directly affect system behavior, agent capabilities, and escalation constraints. The layer contains the Authority Architecture (the source of truth for what agents can and cannot do), Memory Architecture (how agents know things), Agent Systems (the agents themselves), and organizational integration.

The SYSTEMS layer is the bridge between Authority (what is allowed) and Execution (what actually happens).

## Structure

- **authority_architecture/**: Authority pack definitions, versioning, compiler, templates
- **agent_systems/**: Agent constellation definitions, role assignments, supervisor/specialist relationships
- **agent_instances/**: Running instances of agents and their configurations
- **memory_architecture/**: Knowledge graph, structured data, vector memory infrastructure
- **infrastructure/**: Tools, scripts, and runtime systems that support agents
- **operational_intelligence/**: Metrics, monitoring, and observability for the system
- **organizational_integration/**: How Agent Maestro integrates with human organizations

## Conventions

All files in SYSTEMS must follow strict naming and versioning conventions:

### Governance Documents
- Use Title Case for document names
- Include `authority_weight` in frontmatter (70-100 range)
- Include `version` field for any pack or template document
- Include `schema_version: 2` in all frontmatter

### Authority Packs
- Named consistently with pack type suffix (e.g., "Base Pack — Supervisor Authority")
- Versioned using semantic versioning (MAJOR.MINOR.PATCH)
- Include `pack_type` in frontmatter (base_pack, constellation_pack, role_pack, domain_pack, etc.)
- Include inheritance chain in relationships

### CSV Files
- Follow Structured Data Registry conventions
- Use ISO 8601 dates and UTF-8 encoding
- Include headers on first row
- Maintain consistency with register files (*_registry.csv)

## Agent Rules

**Agents MAY**:
- Read all system documentation and architecture files
- Update agent instance configurations and status
- Write to logs and metrics in operational_intelligence/
- Generate CSV reports following the Structured Data Registry format
- Update memory architecture relationship graphs

**Agents MUST NOT**:
- Modify authority pack definitions without escalation
- Change version numbers on packs or templates (only humans increment versions)
- Delete or rename infrastructure tools without escalation
- Modify organizational_integration documents without escalation
- Ignore agent role or responsibility definitions

**Escalation Required**:
- Any change to authority pack definitions (these affect agent permissions)
- Modifications to agent constellation definitions
- Changes to agent system architecture or role assignments
- Additions or removals of agent instances
- Modifications to Memory Architecture (though relationship updates are OK)
- Changes to infrastructure tools that affect multiple agents

## Critical Subdirectories

### authority_architecture/
The most critical subdirectory. Contains authority packs (versioned), templates, maps, and the compiler. Changes here have system-wide impact.
See the respective CLAUDE.md in authority_architecture/ for detailed rules.

### memory_architecture/
Defines the three-layer memory model (Knowledge Graph, Structured Data, Vector). Changes here affect all agent knowledge access.
See the respective CLAUDE.md in memory_architecture/ for detailed rules.

### agent_systems/
Defines agent roles, constellation structure, and supervisor/specialist relationships. Changes here affect agent organizational structure.
See the respective CLAUDE.md in agent_systems/ for detailed rules.

### infrastructure/
Tools, scripts, and runtime support. Read-mostly, written by system administrators.

### operational_intelligence/
Metrics, logs, and monitoring. Write-mostly by agents, read by supervisors and humans.

### organizational_integration/
How agents integrate with human organizations. Changes require human coordination.

## The Authority Stack

The SYSTEMS layer implements the full authority stack:

1. **Governance Documents** (authority_weight: 70+): Governance Schemas, Authority Architecture, Authority Inheritance, Pack Versioning, Pack Manifest
2. **Authority Packs** (versioned): Base packs, constellation packs, role packs, domain packs
3. **Authority Pack Compiler**: Transforms packs into compiled governance artifacts
4. **Compiled Governance Artifacts**: Executable authority specifications
5. **Host Bindings**: Bindings of artifacts to specific agent hosts
6. **Agent Runtime**: Agents executing according to compiled artifacts

Each layer depends on the layers above it. Changes must propagate through the entire stack.

## Versioning & Evolution

Authority packs and system architecture documents use semantic versioning:
- **MAJOR**: Breaking changes to pack structure or compatibility
- **MINOR**: Non-breaking additions or enhancements
- **PATCH**: Bug fixes and clarifications

When you need to change an authority pack, you must:
1. Create a new version with incremented version number
2. Document the change (what changed, why, impact analysis)
3. Escalate to human for approval of the new version
4. Update host bindings to use the new pack version
5. Communicate the change to all affected agents

## Relationship to Knowledge Layer

SYSTEMS documents should cite and implement the principles from 02_KNOWLEDGE/governance/. Authority packs are grounded in [[Agent Maestro — Foundations]] (the foundational kernel: 3 seeds, 1 meta-principle, 3 laws, 6 derived principles). System architecture should follow the patterns in 02_KNOWLEDGE/patterns/.

Before making changes to SYSTEMS, verify they are consistent with:
- The Foundations (kernel + derived principles)
- The Governance Before Autonomy pattern (D5)
- The Authority Architecture pattern
- The Memory Architecture concepts

## Relationship to Execution Layer

Agents in 06_EXECUTION operate according to the rules and authority structures defined in 05_SYSTEMS. The compiled governance artifacts from the authority_architecture/ compiler are the executable specifications that guide all agent action.

See the respective CLAUDE.md in 06_EXECUTION/ to understand how SYSTEMS rules are enforced during execution.
