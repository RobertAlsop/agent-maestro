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
  governs: []
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
4. `SYSTEM_MAP.md` at the vault root is the Inventory — a compact index of what currently exists in the vault. Both `CLAUDE.md` and `SYSTEM_MAP.md` are required root documents.

## Note Creation Rules

5. Every note must have YAML frontmatter conforming to schema_version: 3. **Exception:** Notes in `01_CAPTURE/` may omit frontmatter — Capture prioritizes low-friction input. The [[Skill — Triage|Triage]] skill is responsible for adding frontmatter when routing a note out of Capture.
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

15. The vault uses two linking systems that serve different purposes. Frontmatter `relationships` provide structural, machine-readable connections (authority chains, governance scope, formal associations). Wiki-links in the body provide navigational, human-readable connections for Obsidian. Both are required and are not redundant — frontmatter says "these are my formal relationships," body links say "this concept is relevant here."
16. Wiki-links use the canonical format: `[[Note Title]]`.
17. Every note (except the North Star) must have at least one entry in `derives_from`. This is the formal parent link — it traces authority upward and prevents orphans.
18. Every concept or governance note must include at least one wiki-link in its body content, connecting it to related knowledge.
19. All wiki-links must resolve to existing notes. Orphan links indicate missing knowledge and must be flagged.
20. No orphan notes — every note must be reachable from at least one other note via `derives_from`, `governs`, or `related`.
21. The vault maintains a single master map: `SYSTEM_MAP.md` at the vault root. This is the inventory — a compact index of what currently exists in the vault.
22. SYSTEM_MAP must be updated as part of any build that changes vault structure, adds or removes documents, or reorganizes content.
23. CLAUDE.md is the Charter (what AM is). SYSTEM_MAP is the Inventory (what exists). Both live at the vault root. Both are required.

## Authority and Governance

24. Documents with `authority_weight` ≥ 80 are canonical. Changes to canonical documents require human approval (Level 3 escalation).
25. When two documents conflict, higher `authority_weight` wins. When weights are equal, defer to the Foundations.
26. The [[Agent Maestro — North Star]] (authority_weight: 97) is the highest authority in the vault, defining mission and intent. The [[Agent Maestro — Foundations]] (authority_weight: 95) is the highest operational authority, defining the kernel mechanics. Neither can be modified without explicit human approval and a full pipeline cycle (proposal → audit → approval → implementation → record → reflect).

## Pipeline Integrity

27. `01_CAPTURE` is the inbox — unsorted input arrives here and should be processed through triage promptly. The inbox should be kept lean.
28. Content moves through the pipeline in order: Capture → Knowledge → Decide → Execute → Record → Reflect. Skipping stages requires explicit justification traceable to the Foundations.
29. Every stage transition passes through a gate. Gate intensity scales with the stakes of the transition.
30. `06_REFLECT` feeds back into `01_CAPTURE` — reflections produce capture seeds that start the next cycle.

## Naming Conventions

31. Governance documents use the full project prefix: "Agent Maestro — [Title]". All other notes use their type or project abbreviation as prefix (e.g., "Proposal — [Title]", "Skill — [Title]", "SES-001 — [Title]").
32. For multi-project work, use short project codes as prefixes (e.g., "DP — Proposal v0.1.0"). Project codes should be defined in SYSTEM_MAP when introduced.
33. Note titles use Title Case with em-dashes ( — ) for subtitles and type separation.
34. File names must match the `title` field in frontmatter exactly.
35. Folder names follow the established pattern: pipeline folders use `NN_UPPER_CASE`, subfolders use `lowercase`.

## Work Unit Hierarchy

36. Work is organized in three planning units. A **Wave** is the largest — a complete pipeline cycle with a proposal, build, and reflection, producing a version increment (e.g., Wave 5.2). A **Phase** is a major division within a wave, with a clear deliverable and natural stopping point (e.g., Phase 2 — Governance Review). A **Step** is the smallest unit — a single action or decision within a phase.
37. A **Stage** refers to a pipeline stage (Capture, Knowledge, Decide, Execute, Record, Reflect) and is structural, not temporal. Phases move *through* stages; they are not contained within them. Stage and the planning units are orthogonal dimensions.
38. Wave naming uses the format `Wave X.Y` where X is the major wave and Y is the sub-wave.

## Archiving and Deletion

39. Notes are never deleted from the vault. They are archived to `05_RECORD/archive/` with `status: archived`. Git history preserves the full record.
40. When archiving, the original `derives_from` chain is preserved in frontmatter so the archive remains traceable.
41. Archive subfolders follow the pattern `wave_N_[domain]/` to group historical items by the wave that produced or retired them.

## Change Tracking

42. The `updated` field must be changed whenever a note's content is modified.
43. Every build wave must begin with an approved proposal in `03_DECIDE/` and end with a reflection in `06_REFLECT/`, plus a capture seed in `01_CAPTURE/` that closes the loop and seeds the next cycle.

## Proposal Lifecycle

44. Proposals follow a three-stage lifecycle within `03_DECIDE/`: **draft** in `proposals/`, **active** in `active/`, **archived** in `05_RECORD/archive/`. Each transition corresponds to a pipeline gate.
45. A new proposal is created in `03_DECIDE/proposals/` with `status: draft`. It remains there until it passes its gate criteria — including human approval for any proposal that touches governance or structure. If the proposal derives from a capture seed, the seed is consumed (moved to `05_RECORD/archive/` with `status: archived`) when the proposal is created — this is the moment the work the seed describes has formally begun.
46. When a proposal is approved, its `status` is changed to `active`, an `approved` date field is added to frontmatter, and the file is moved to `03_DECIDE/active/`. This is the formal commitment to execute.
47. When a proposal's work is complete (all completion criteria checked, reflection filed), the proposal is moved to `05_RECORD/archive/` with `status: archived` and a `completed` date field added. This closes the loop.
48. A rejected proposal is moved directly to `05_RECORD/archive/` with `status: archived` and a `rejected` date field. The archive preserves the reasoning for future reference.

## Idea Lifecycle

49. Capture notes that are not seeds follow a triage lifecycle: they are **reviewed**, then either **promoted** to the [[AM — Future Waves Register]] or **archived** to `05_RECORD/archive/`. The goal is to keep `01_CAPTURE/` lean — ideas should not accumulate indefinitely.
50. To promote a capture note to the register, its core idea is added to the appropriate Strategy stage section in the register with source attribution. The original capture note is then archived. The register entry replaces the capture note as the canonical record of the idea.
51. To promote a register item to the [[AM — Roadmap]], a formal proposal is drafted in `03_DECIDE/proposals/` referencing the register item. The register item is marked as promoted (not removed) to preserve provenance.
52. Every wave reflection (Phase 6 / Reflect stage) must consult both the Roadmap and the Future Waves Register when deciding what comes next. This ensures strategic continuity and prevents good ideas from being lost between waves.

## Capture Folder Rules

53. `01_CAPTURE/` is flat — no subfolders. Everything drops in at the top level. Triage happens later, not at the point of capture.
54. `01_CAPTURE/` holds at most one **capture seed** at a time. A capture seed is a structured handoff produced by the pipeline (Reflect → seed → Capture) that starts the next unit of work. Seeds follow the naming convention "Wave X.Y — Capture Seed.md" and carry the `seed` tag.
55. When the work a capture seed describes begins, the seed is **consumed** — it moves to `05_RECORD/archive/` as a historical record. Capture should only ever contain the *next* seed, not completed ones.
56. Loose brainstorm notes, ideas, and observations can be added to `01_CAPTURE/` at any time alongside an active seed. They are raw input waiting for triage, not structured handoffs. The seed is always distinguishable by its template format, naming convention, and `seed` tag.

## CLAUDE.md Files

57. Each of the six pipeline folders MUST contain a `CLAUDE.md` that provides stage-specific guidance for agents entering that folder. These are infrastructure files and do not use vault note frontmatter.
58. Significant subfolders (e.g., `governance/`, `skills/`, `concepts/`, `runtime/`, `archive/`) SHOULD have a `CLAUDE.md` if the folder has conventions, constraints, or workflows that aren't obvious from its name and parent context. The test: would an agent entering this folder for the first time make a mistake without guidance?
59. CLAUDE.md files serve as micro-SOPs — they define what belongs in this space, what the conventions are, and what to do next.

## Templates

60. When creating a new note of a type that has a template in `02_KNOWLEDGE/templates/`, the template must be used as the starting point.

## Authority Weight Ranges

61. Authority weight conventions: 95-100 = constitutional (North Star, Foundations); 80-94 = canonical governance (Vault Rules, Scope, Strategy); 60-79 = operational governance (Principles, roles, skills); 30-59 = working documents (proposals, concepts, reports); 0-29 = ephemeral (captures, logs, seeds).

## Concept Lifecycle

62. New concepts are introduced through the wave lifecycle. During the reflection phase, the Reviewer audits for concepts that were used but never defined. A concept earns its place in `02_KNOWLEDGE/concepts/` if it is referenced by governance, skills, or operational documents and is not already adequately defined within those documents.
63. Concept authority weights are tiered. **Foundational concepts (50-59)** are the minimum viable set — referenced by governance or skills, load-bearing, removing one would create a gap. **Operational concepts (30-49)** are introduced during waves to describe patterns or ideas that earned their place through use — valuable but not load-bearing.
64. If an operational concept (30-49) is not referenced by any active document after two waves, it is a candidate for archiving under Law 3.

## Scope Protection

65. The vault governs itself. No external systems are tracked or managed within this vault unless a formal proposal extends the scope.

## Governance Cascade

66. When a governance document is modified, all documents that list it in `derives_from` should be checked for continued alignment. This is a check, not an automatic rewrite.

## Git and Version Control

67. All implementation work occurs on dedicated working branches. The `main` branch is the protected baseline — it must remain stable, reversible, and suitable for rollback at all times.
68. Before any major build pass, create a checkpoint tag from the current known-good state (e.g., `pre-wave-5.2`).
69. Commits must be small, scoped, and tied to a single implementation objective. Commit messages must be descriptive — no vague messages.
70. Working branches are only merged to `main` after relevant validations pass.
71. Agents must not: rewrite git history without explicit instruction, force-push without permission, work directly on `main`, or bypass validation steps.
72. The full git workflow reference is maintained in [[Git Best Practices for AI-Assisted Builds]] (`02_KNOWLEDGE/protocols/`).

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
- [[Git Best Practices for AI-Assisted Builds]]
