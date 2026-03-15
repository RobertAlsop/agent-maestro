---
id: GOV.agent_maestro.vault_rules
type: governance
note_class: governance
domain: governance
layer: governance
scope: null

canonical: true
authority_weight: 92
resolution_basis: canonical
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-10
updated: 2026-03-14
last_reviewed: null
review_cycle: quarterly

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []

map: "[[Agent Maestro — Governance Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - governance
  - vault

hash: ""
---

# Agent Maestro — Vault Rules

## Purpose

Define the structural rules that keep the Agent Maestro vault consistent, navigable, and trustworthy.

## Principle

Structure is governance. A vault without rules becomes an unnavigable knowledge dump.

## Rules

1. Every note must be created from one of the approved master templates.
2. No note may invent its own structure. If no template fits, stop and request one.
3. Every note must populate its frontmatter fields correctly.
4. Every note must have a stable unique ID. IDs never change once created.
5. Every concept note must include a minimum of two internal links.
6. Every note must link to at least one canonical map.
7. Every concept, system, and pipeline must appear in at least one map.
8. Maps link downward to contents and upward to parent maps.
9. Authority pack folders follow the canonical `00–13` grammar. No deviations.
10. Each authority pack file represents exactly one grammar section.
11. No orphan notes are allowed.
12. Maps are for navigation. Folders are for storage only.
13. Notes contain light but meaningful initial content. No empty placeholders.
14. `01_CAPTURE`, `02_KNOWLEDGE` (including governance), and `99_ARCHIVE` are canonical. Do not redesign them.
15. Canonical note titles must be unique across the vault.
16. No concept may link directly to more than one layer above itself. (Prevents conceptual short-circuiting and preserves layered integrity.)
17. All note templates are stored canonically in `05_SYSTEMS/templates/`. The source template system in `01_CAPTURE/unprocessed/88_TEMPLATES/` is the historical origin and should not be used for new note creation.

## When It Applies

Always. These rules apply to every note created in this vault.

## Related

- [[Canonical Notes Registry]]
- [[Canonical Notes Index]]
- [[Agent Maestro — Governance Map]]
