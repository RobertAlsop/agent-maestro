# 05_SYSTEMS/authority_architecture

## Foundations Alignment

This directory implements the **Constraint seed** (Authority Hierarchy) from [[Agent Maestro — Foundations]]. Authority packs define the six-level hierarchy from design intent through execution. All changes require human approval per D4 (Human Sovereignty).

## Purpose

The Authority Architecture subdirectory is the source of truth for what agents can and cannot do. It contains authority pack definitions (versioned blueprints of agent permissions), pack inheritance chains, versioning metadata, compiler configuration, templates for creating new packs, and reference maps showing how packs are organized.

This is the highest-stakes subdirectory in SYSTEMS. Changes here directly affect agent autonomy and escalation constraints across the entire system.

## Structure

- **packs/**: Authority pack definitions organized by pack type (base_packs/, constellation_packs/, role_packs/, domain_packs/, etc.)
- **compiler/**: The Authority Pack Compiler system that transforms packs into compiled governance artifacts
- **templates/**: Templates for creating new authority packs following the 14-section Authority Pack Grammar
- **maps/**: Reference maps showing pack inheritance and organizational relationships
- **Authority Architecture.md**: Core documentation for how authority is modeled and inherited
- **Authority Inheritance.md**: Rules for how packs inherit from parent packs
- **Authority Model.md**: Conceptual model of authority and delegation
- **Pack Manifest.md**: Manifest of all authority packs in the system
- **Pack Versioning.md**: Versioning rules and evolution procedures
- **authority_pack_registry.csv**: Registry of all packs with versions and status

All files located in `05_SYSTEMS/authority_architecture/`

## Pack Types

Authority packs are organized by type, each serving a specific purpose:

- **base_packs/**: Foundational authority definitions (e.g., Base Pack — Supervisor Authority)
- **constellation_packs/**: Authority for multi-agent constellations
- **role_packs/**: Authority tied to specific agent roles (Executive, Supervisor, Specialist)
- **domain_packs/**: Authority for specific domains or business areas
- **context_packs/**: Temporary context-specific authority modifications

Each pack type uses the 14-section Authority Pack Grammar defined in [[Authority Pack Grammar]] pattern.

## Authority Pack Grammar (14 Sections)

Every authority pack follows a consistent grammar with 14 sections:

1. **Pack Metadata**: Name, version, type, created_date, owner
2. **Purpose**: What this pack authorizes
3. **Applies To**: Which agents or roles this pack applies to
4. **Inherits From**: Parent packs (if any)
5. **Overrides**: Which rules from parent packs are overridden
6. **Decision Authority**: What decisions this agent can make
7. **Execution Authority**: What actions this agent can execute
8. **Resource Access**: What resources and data this agent can access
9. **Escalation Rules**: When decisions must be escalated to a human
10. **Policy Constraints**: Hard constraints that cannot be violated
11. **Action Classes**: Which action classes are permitted
12. **Tool Access**: Which tools and APIs this agent can use
13. **Relationships**: Links to other packs and referenced concepts
14. **Versioning**: Version number, change log, deprecation status

## Conventions

### Pack Naming
- Format: "[Domain] Pack — [Type] Authority"
- Example: "Base Pack — Supervisor Authority" or "Constellation Pack — Executive System"
- All packs must have a version: "v1.0.0", "v1.1.0", etc.

### Versioning Requirements
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **MAJOR**: Breaking changes to pack structure or compatibility (requires human approval and system-wide update)
- **MINOR**: Non-breaking additions (e.g., new action classes permitted)
- **PATCH**: Bug fixes and clarifications (no permission changes)

### Frontmatter Required Fields
- `title`: Pack name
- `pack_type`: base_pack | constellation_pack | role_pack | domain_pack | context_pack
- `version`: Semantic version (e.g., "1.2.0")
- `authority_weight`: 80-100 (these are high-authority documents)
- `schema_version`: 2
- `inherits_from`: Parent pack names (if applicable)
- `applies_to`: Agent roles or constellation names
- `created_date`: YYYY-MM-DD
- `last_modified`: YYYY-MM-DD
- `owner`: Who maintains this pack

## Agent Rules

**Agents MAY**:
- Read all authority pack definitions (mandatory before executing tasks)
- Consult packs to understand their own permissions and constraints
- Reference packs when explaining why an action requires escalation
- Use the templates to propose new packs (with escalation)

**Agents MUST NOT**:
- Modify any existing authority pack without escalation
- Change version numbers (only humans increment versions)
- Create new packs without escalation (use templates to propose)
- Delete or archive packs without escalation
- Ignore pack inheritance chains or override rules
- Reinterpret pack permissions (unclear cases require escalation)

**Escalation Required**:
- ANY modification to ANY authority pack
- Proposals to create new packs
- Requests to increase agent authority
- Conflicts between authority pack requirements and other constraints
- Interpretation disputes about pack permissions

## Key Documents

- **Authority Architecture.md**: Core documentation for how authority works
- **Authority Inheritance.md**: Rules for inheriting permissions from parent packs
- **Authority Model.md**: Conceptual model of authority delegation
- **Pack Manifest.md**: Master list of all packs in the system
- **Pack Versioning.md**: Rules for versioning and evolving packs
- **authority_pack_registry.csv**: Machine-readable registry of pack versions and statuses

## Pack Registry

The file `authority_pack_registry.csv` contains:
- Pack name
- Pack type
- Current version
- Status (active | deprecated | experimental)
- Applies to (agent roles or constellations)
- Last modified date

This registry is the single source of truth for which pack versions are active in the system.

## Compiler Subsystem

The compiler (in compiler/) transforms authority packs into compiled governance artifacts. See CLAUDE]] in compiler/ for details on the compilation pipeline.

## Related Patterns

Authority packs implement several core patterns:
- **[[Authority Pack Grammar]]**: The 14-section structure all packs must follow
- **[[Authority Inheritance Pattern]]**: How packs inherit and override parent permissions
- **[[Pack Versioning Pattern]]**: How packs evolve over time
- **[[Pack Override Rules]]**: How child packs override parent pack permissions
- **[[Governance Compilation Pattern]]**: How packs are compiled into executable artifacts

## Modification Workflow

To modify an authority pack:

1. **Analyze Current Pack**: Read the existing pack and understand its 14 sections
2. **Propose Change**: Document what needs to change and why
3. **Version Increment**: Determine if this is MAJOR, MINOR, or PATCH
4. **Create New Version**: Create a new pack file with incremented version
5. **Document Changes**: Include changelog in pack frontmatter
6. **Escalate**: Submit to human for approval
7. **Recompile**: If approved, trigger compiler to generate new compiled artifacts
8. **Update Registry**: Update authority_pack_registry.csv
9. **Notify Agents**: Communicate the change to affected agents

Authority packs are never modified in place; new versions are created instead.
