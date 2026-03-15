---
id: EXE.prompt.note_quality_rules
type: pipeline
layer: execution
domain: execution
status: active
version: 1
created: 2026-03-10
owner: AgentMaestro
maps: "[[Agent Maestro — Domain Map]]"
hash: TBD
---

# Claude Note Quality Rules

## Purpose

Rules that govern note quality when Claude authors or edits Agent Maestro notes.

## Rules

1. Every note must use an approved template structure.
2. Every note must have a correctly formatted frontmatter block with a stable ID.
3. Every note must link to at least one canonical map.
4. Concept notes must contain at least two internal links.
5. No note may be empty or a placeholder.
6. Links must use the canonical ID format: `[[Authority Architecture]]`
7. Prefer short, well-linked notes over long, isolated notes.
8. Never invent IDs. Use the canonical prefix system from [[Artifact Taxonomy]].

## Related

- [[Agent Maestro — Vault Rules]]
- [[Artifact Taxonomy]]
