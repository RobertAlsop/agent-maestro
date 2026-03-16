# 88_TEMPLATES

## Foundations Alignment

Templates implement the **Structure seed** (7 Primitives) from [[Agent Maestro — Foundations]]. Every template enforces the same structural pattern (frontmatter + required body sections), realizing the Fractal Design meta-principle. The Pipeline Template explicitly maps to the Process seed (Irreducible Loop).

## Purpose

The canonical source for all note templates in the Agent Maestro vault. Every note must be created from an approved template (Vault Rule 1). Templates enforce schema_version: 2 frontmatter, typed relationships, and required body sections.

## Structure

- **Pipeline Template.md**: Pipeline template mapped to the Irreducible Loop (root-level, authoritative)
- **notes/core_knowledge_templates/**: Concept, Decision, Governance, Modes, North Star, Principles, Reference, Scope
- **notes/architecture_and_navigation_templates/**: Authority Pack, Index, Map, Registry, System, System Map, System Registry, Taxonomy
- **notes/execution_and_planning_template/**: Authority Pack Section, Process, Project, Roadmap, Strategy
- **notes/frontmatter/**: Frontmatter Schema v1 (field definitions)
- **notes/docs/**: Template governance documentation (Design Doctrine, Governance Rules, Mapping, Registry, Ruleset)

## Relationship to 05_SYSTEMS/templates/

`88_TEMPLATES/` is the **source** location for templates. `05_SYSTEMS/templates/` contains **compiled/runtime** copies. When templates are updated here, the runtime copies should be regenerated.

## Agent Rules

**Agents MAY**:
- Read all templates to understand expected note structure
- Use templates when creating new notes
- Propose new templates via escalation

**Agents MUST NOT**:
- Modify templates without escalation
- Create notes that deviate from template structure
- Delete templates without human approval

**Escalation Required**:
- Any template modification
- Proposals for new templates
- Changes to template governance docs
