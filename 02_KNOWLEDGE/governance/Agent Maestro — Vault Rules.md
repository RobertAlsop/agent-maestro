---
schema_version: 2
title: "Agent Maestro — Vault Rules"
type: governance
note_class: governance
domain: governance
layer: governance
authority_weight: 85
resolution_basis: authority_weight
canonical: true
status: active
review_status: approved
version: 2
created_date: 2026-03-10
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Vault Structure Rules]]"
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs:
    - "[[02_KNOWLEDGE]]"
    - "[[03_PIPELINES]]"
    - "[[04_PROJECTS]]"
    - "[[05_SYSTEMS]]"
    - "[[06_EXECUTION]]"
    - "[[88_TEMPLATES]]"
    - "[[99_ARCHIVE]]"
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - governance
  - vault
  - rules
hash: ""
---

# Agent Maestro — Vault Rules

## Purpose

Define the structural rules that keep the Agent Maestro vault consistent, navigable, and trustworthy. These rules operationalize the Structure seed (every component must have the seven primitives) and Law 2 (all actions must be verifiable, reversible, and accountable).

## Principle

Structure is governance. A vault without rules becomes an unnavigable knowledge dump.

## Rules

### Note Creation

1. Every note must be created from one of the approved templates in `88_TEMPLATES/`.
2. No note may invent its own structure. If no template fits, stop and request one.
3. Every note must populate its frontmatter fields correctly per schema_version: 2.
4. Every note must have a stable, unique title that serves as its identifier. Titles do not change once a note is established.
5. Notes contain light but meaningful initial content. No empty placeholders.

### Linking and Navigation

6. Every concept note must include a minimum of two internal wiki-links.
7. Every note must link to at least one related document.
8. Every concept, system, and pipeline must appear in at least one map.
9. Maps link downward to contents and upward to parent maps.
10. No orphan notes are allowed.

### Authority Packs

11. Authority pack folders follow the canonical `00–13` grammar. No deviations.
12. Each authority pack file represents exactly one grammar section.

### Vault Structure

13. `01_CAPTURE` is the inbox — unsorted input arrives here and should be processed promptly. The inbox should be kept empty.
14. `02_KNOWLEDGE` (including governance) and `99_ARCHIVE` are canonical directory structures. Do not redesign them.
15. Canonical note titles must be unique across the vault.
16. No concept may link directly to more than one layer above itself. (Prevents conceptual short-circuiting and preserves layered integrity.)
17. All note templates are stored canonically in `88_TEMPLATES/`. Templates in `05_SYSTEMS/templates/` are the compiled/runtime versions.

## Validation Checklist

Before accepting any note as complete, verify:

### YAML Validity
- Frontmatter begins and ends with `---`
- Indentation is consistent (2 spaces)
- No tabs or mixed indentation

### Field Presence
Fields must include at minimum: `schema_version`, `title`, `type`, `note_class`, `authority_weight`, `status`, `review_status`, `version`, `created_date`, `last_modified`, `tags`, `relationships`

### Relationship Structure
Every note contains typed relationships:
```yaml
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
```

### Required Body Sections
Each note contains at minimum:
- **Purpose** — what this note is for
- One or more sections of substantive content

### Link Integrity
- All wiki-links use the canonical format: `[[Note Title]]`
- No full-path links (`...]]`)
- Internal links resolve to existing notes

## When It Applies

Always. These rules apply to every note created in this vault.

## Related

- [[Agent Maestro — Foundations]]
- [[Agent Maestro — North Star]]
