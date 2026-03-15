# Template Governance Rules

## Purpose

Define how templates are created, modified, and applied within the vault.

Templates ensure structural consistency and machine readability across the knowledge system.


## Template Authority

Templates define the structural contract for notes.

Each note type must use its designated template.

### Authority Hierarchy

When documents conflict, the following precedence applies:

1. **Frontmatter Schema** — canonical field definitions and allowed values
2. **Note Templates** — canonical structural contracts
3. **Template Mapping** — folder-to-template assignment guide
4. **Template Registry** — canonical type-to-template mapping
5. **Template Ruleset** — validation rules and per-template specifications
6. **Template Design Doctrine** — design principles and philosophy

The Frontmatter Schema and Note Templates are the highest-authority sources. If the Ruleset, Registry, or Doctrine contradicts them, those documents must be corrected.

### Mapping Authority

The Template Registry is the canonical source for type-to-template assignment. The Template Mapping is a supplementary guide that maps vault folder paths to templates. Both should agree; if they conflict, the Registry takes precedence.


## Template Creation

A new template may only be introduced when:

1. A new note type requires a fundamentally different reasoning structure.
2. The structure cannot be represented by an existing template.
3. The change is approved through governance review.


## Template Modification

Template changes should be rare.

When a template changes:

1. Update the template definition.
2. Document the change.
3. Evaluate whether existing notes require migration.


## Template Compliance

All notes must conform to the template associated with their `type`.

Validation is performed through the Vault Integrity Audit.


## Template Registry

The mapping between note types and templates is defined in the Template Registry document.


## Structural Parent Rule

Every note must belong to exactly one structural parent map.

Frontmatter rule:

map: [[Parent Map]]

Secondary appearances may use:

maps:
  - [[Secondary Map]]


## Goal

Maintain a stable, machine-readable knowledge architecture as the vault grows.