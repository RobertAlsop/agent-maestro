# Template Registry

## Purpose

Define the canonical mapping between note types and templates used in the vault.

This is the authoritative source for type-to-template assignment.

This document ensures:

- consistent note structure
- deterministic machine parsing
- predictable knowledge graph architecture


## Template Mapping


### Knowledge Layer

| Note Type | Template | Notes |
|-----------|----------|-------|
| concept | Concept | |
| domain | Concept | Shares template with concept; distinguished by `type` field |
| pattern | Concept | Shares template with concept; distinguished by `type` field |
| reference | Reference | |
| glossary_entry | Reference | Shares template with reference; distinguished by `type` field |


### Governance Layer

| Note Type | Template |
|-----------|----------|
| principles | Principles |
| north_star | North Star |
| modes | Modes |
| governance | Governance |
| decision | Decision |
| scope | Scope |
| strategy | Strategy |


### Maps Layer

| Note Type | Template |
|-----------|----------|
| map | Map |
| system_map | System Map |
| taxonomy | Taxonomy |
| index | Index |


### Systems Layer

| Note Type | Template |
|-----------|----------|
| system | System |
| authority_pack | Authority Pack |
| authority_pack_section | Authority Pack Section |


### Registry Layer

| Note Type | Template |
|-----------|----------|
| registry | Registry |
| system_registry | System Registry |


### Pipes Layer

| Note Type | Template |
|-----------|----------|
| pipeline | Pipeline |
| process | Process |


### Execution Layer

| Note Type | Template |
|-----------|----------|
| project | Project |
| roadmap | Roadmap |


## Shared Templates

Some note types share a structural template while maintaining distinct `type` identifiers in frontmatter:

- **Concept template** serves types: `concept`, `domain`, `pattern`
- **Reference template** serves types: `reference`, `glossary_entry`

The `type` field — not the template — determines the note's semantic identity.


## Structural Rule

Every note must have exactly one structural parent.

Frontmatter rule:

map: [[Parent Map]]

Additional appearances may use:

maps:
  - [[Secondary Map]]


## Template Governance

New templates may only be introduced when:

1. A new note type requires a different reasoning structure
2. The structure cannot be represented by an existing template
3. The change is approved through the governance process