---
title: "Agent Maestro — Vault Rules"
type: governance
status: active
authority_weight: 85
schema_version: 3
created: "2026-03-10"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs:
    - "[[01_CAPTURE]]"
    - "[[02_KNOWLEDGE]]"
    - "[[03_DECIDE]]"
    - "[[04_EXECUTE]]"
    - "[[05_RECORD]]"
    - "[[06_REFLECT]]"
  related:
    - "[[Agent Maestro — North Star]]"
tags:
  - governance
  - vault
  - rules
---

# Agent Maestro — Vault Rules

## Purpose

Define the structural rules that keep the Agent Maestro vault consistent, navigable, and trustworthy. These rules operationalize the Structure seed (every component must serve the seven primitives) and Law 2 (all actions must be verifiable, reversible, and accountable).

## Principle

Structure is governance. A vault without rules becomes an unnavigable knowledge dump. The vault IS the pipeline — its structure directly mirrors the universal 6-stage workflow.

## Vault Structure Rules

1. The vault has exactly six pipeline folders: `01_CAPTURE`, `02_KNOWLEDGE`, `03_DECIDE`, `04_EXECUTE`, `05_RECORD`, `06_REFLECT`.
2. Each folder corresponds to a pipeline stage. Content belongs in the folder that matches its function, not its format.
3. `CLAUDE.md` at the vault root is the Charter — the entry point for any agent. It is not a vault note and does not use frontmatter.
4. The Design Blueprint at the vault root is the architectural specification for the current version.

## Note Creation Rules

5. Every note must have YAML frontmatter conforming to schema_version: 3.
6. Every note must have a **Purpose** section explaining why it exists.
7. Notes must contain meaningful content — no empty placeholders (Law 3: only what is necessary).
8. If no template fits the content type, the agent should create a minimal note with correct frontmatter and flag it for review.

## Schema v3 Requirements

9. All frontmatter must include at minimum: `title`, `type`, `status`, `authority_weight`, `schema_version`, `created`, `updated`, `relationships`, `tags`.
10. The `type` field must use one of the controlled values: governance, concept, skill, role, pipeline, log, report, proposal.
11. The `status` field must use one of: draft, active, archived.
12. The `relationships` field must include three sub-fields: `derives_from`, `governs`, `related`.
13. All dates use ISO 8601 format: `YYYY-MM-DD`.
14. Empty list fields use `[]`, never null.

## Linking and Navigation

15. Wiki-links use the canonical format: `[[Note Title]]`.
16. Every note (except the North Star) must have at least one entry in `derives_from`. This is the formal parent link — it traces authority upward and prevents orphans.
17. Every concept or governance note must include at least one wiki-link in its body content, connecting it to related knowledge.
18. All wiki-links must resolve to existing notes. Orphan links indicate missing knowledge and must be flagged.
19. No orphan notes — every note must be reachable from at least one other note via `derives_from`, `governs`, or `related`.

## Navigation

20. The vault maintains a single master map: `02_KNOWLEDGE/indexes/SYSTEM_MAP.md`. This is the inventory — a compact index of what currently exists in the vault.
21. SYSTEM_MAP must be updated as part of any build that changes vault structure, adds or removes documents, or reorganizes content.
22. CLAUDE.md is the Charter (what AM is). SYSTEM_MAP is the Inventory (what exists). Both are required.

## Authority and Governance

23. Documents with `authority_weight` ≥ 80 are canonical. Changes to canonical documents require human approval (Level 3 escalation).
24. When two documents conflict, higher `authority_weight` wins. When weights are equal, defer to the Foundations.
25. The Foundations document (authority_weight: 95) is the highest authority in the vault. It cannot be modified without explicit human approval and a full pipeline cycle (proposal → audit → approval → implementation → record → reflect).

## Pipeline Integrity

26. `01_CAPTURE` is the inbox — unsorted input arrives here and should be processed through triage promptly. The inbox should be kept lean.
27. Content moves through the pipeline in order: Capture → Knowledge → Decide → Execute → Record → Reflect. Skipping stages requires explicit justification traceable to the Foundations.
28. Every stage transition passes through a gate. Gate intensity scales with the stakes of the transition.
29. `06_REFLECT` feeds back into `01_CAPTURE` — evolution proposals and brainstorms become input for the next cycle.

## Validation Checklist

Before accepting any note as complete, verify:

**Frontmatter:**
- Begins and ends with `---`
- Indentation is consistent (2 spaces)
- All required fields present (see rule 9)
- `type` and `status` use controlled vocabulary values

**Content:**
- Has a Purpose section
- Contains substantive content (not a placeholder)
- Wiki-links use canonical format

**Relationships:**
- `derives_from` traces upward to at least one parent (for non-root documents)
- Links resolve to existing notes

## When It Applies

Always. These rules apply to every note created in this vault.

## Related

- [[Agent Maestro — Foundations]]
- [[Agent Maestro — North Star]]
