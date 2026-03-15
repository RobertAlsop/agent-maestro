---
schema_version: 2
title: "AM — Wave 5 — Contract"
type: contract
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 75
resolution_basis: authority_weight
status: active
review_status: approved
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Wave 5]]"
  part_of:
    - "[[Agent Maestro — Evolution Roadmap v0.5.0]]"
  implements:
    - "[[Build Session Protocol]]"
    - "[[Consolidation Pipeline]]"
    - "[[Agent Maestro — Foundations]]"
  governs: []
  applies_to: []
  uses:
    - "[[AM — Wave 5 — Proposal v3]]"
    - "[[AM — Wave 5 — Audit of Proposal v3]]"
    - "[[AM — Wave 5 — Treatise on Core Principles]]"
  produces:
    - "[[v0.5.0 Release]]"
  supersedes: []
  superseded_by: []
tags:
  - contract
  - wave-5
  - alignment
  - v0.5
hash: ""
---

# AM — Wave 5 — Contract

**Date**: 2026-03-15
**Parties**: Rob (human authority) + Claude (Opus, execution)
**Status**: APPROVED (2026-03-15)
**Source**: Proposal v3 (confirmed by audit — 0 findings requiring amendment)
**Starting version**: v0.4.0
**Target version**: v0.5.0

---

## Mission

*Walk every layer of the Agent Maestro vault and bring it into alignment with the Foundations.*

---

## What We Build

### Phase 1 — Foundation Lock + Tooling (Session N)

| # | Deliverable | Effort |
|---|-------------|--------|
| 1a | Baseline vault inventory (note count by folder, authority weight, type) | Small |
| 1b | Add D6 (Separation of Powers) to Foundations.md; cross-reference from CLAUDE.md | Small |
| 1c | Priority 1 shell scripts: frontmatter validator, link integrity checker, orphan note detector | Large |
| 1d | Audit framework rubric (three audit types × vault layers = specific checks) | Medium |
| 1e | Naming convention migration to `AM — Wave [N] — [Type].md` | Small |

**Exit**: Tools built, rubric defined, foundations locked. Ready to walk.

### Phase 2 — Governance Alignment (Session N+1)

| # | Deliverable | Effort |
|---|-------------|--------|
| 2a | Three-audit pass on all governance docs against Foundations.md | Large |
| 2b | Governance reconciliation proposal (human approval required) | Medium |
| 2c | Execute reconciliation + verify with scripts | Medium |

**Exit**: Governance layer aligned. 5 derived principles replace the 12.

### Phase 3 — Knowledge + Pipeline Alignment (Session N+2)

| # | Deliverable | Effort |
|---|-------------|--------|
| 3a | Three-audit pass on all 02_KNOWLEDGE subfolders | Large |
| 3b | Classify and rationalize all 8 pipelines | Medium |
| 3c | Create 02_KNOWLEDGE/strategy/, relocate roadmaps | Small |
| 3d | Pipeline template | Small |

**Exit**: Knowledge lean. Pipelines minimized. Roadmaps relocated.

### Phase 4 — Systems + Templates Alignment (Session N+3, possibly N+3b)

| # | Deliverable | Effort |
|---|-------------|--------|
| 4a | Three-audit pass on runtime modules | Large |
| 4b | Three-audit pass on authority packs + compiler artifacts | Large |
| 4c | Constellation review; archive vault_curator; identify minimum viable set | Medium |
| 4d | Three-audit pass on 88_TEMPLATES/ | Medium |
| 4e | Template reconciliation + formalize note, agent, authority pack templates | Medium |

**Exit**: Systems aligned. Templates formalized. May require two sessions.

### Phase 5 — Execution + Infrastructure + Projects (Session N+4)

| # | Deliverable | Effort |
|---|-------------|--------|
| 5a | Three-audit pass on 06_EXECUTION/ | Medium |
| 5b | Standardize project subfolders (6 folders) + project template | Medium |
| 5c | Update all CLAUDE.md files | Medium |
| 5d | Archive inventory (99_ARCHIVE) | Small |
| 5e | Add Brainstorm stage (Stage 10) to Build Session Protocol | Small |

**Exit**: All layers visited. Infrastructure current.

### Phase 6 — Completion (Session N+5)

| # | Deliverable | Effort |
|---|-------------|--------|
| 6a | Priority 2 shell scripts (if time permits) | Medium |
| 6b | LLM/script boundary document | Small |
| 6c | Script integration with logging infrastructure | Medium |
| 6d | Consolidation Pipeline validation + update | Medium |
| 6e | Final audit report (before/after metrics, all verdicts) | Medium |
| 6f | Foundations.md final review | Small |

**Exit**: Wave 5 complete. Tag v0.5.0.

---

## Rules of Engagement

1. **Top-down**: Governance first, then knowledge, then systems, then execution. Purpose descends.
2. **Three audits at every stop**: Alignment, Integrity, Viability. No exceptions.
3. **Archive over delete**: All removals are reversible. Tag with `archive_reason`.
4. **Human gate on governance**: Phase 2b requires Rob's approval before execution.
5. **Git checkpoint before each phase**: Rollback point if something breaks.
6. **Scripts serve the process**: Priority 1 scripts are built first and used throughout.
7. **Templates emerge from the pass**: Created when informed by actual findings, not before.
8. **Workflow extraction at each session end**: Per Build Session Protocol Stage 7.
9. **Phase 4 may split**: If it runs long, Systems and Templates can become separate sessions without blocking Phase 5.

---

## Exit Criteria

The wave is done when:

1. Every vault layer (9 of 9) visited with three-audit verdicts
2. Governance reconciled with Foundations; 5 principles replace 12
3. Knowledge base lean; all docs earn their place
4. Pipelines minimized; each follows the Process seed
5. Systems aligned with Foundations; vault_curator archived; minimum viable constellations identified
6. Execution layer conforms to Law 2; project structure standardized
7. All CLAUDE.md files current
8. At least 3 shell scripts operational + LLM/script boundary documented
9. Minimum viable template set formalized (note, pipeline, project, audit)
10. Consolidation Pipeline validated against actual work
11. Final audit report published with before/after metrics
12. All changes committed and tagged v0.5.0

---

## Estimated Effort

6 sessions (Phase 4 may become 7 if it splits).

---

## Audit Notes (from light audit of Proposal v3)

Carried forward for awareness during build:

- **N1**: Confirm 01_CAPTURE = 0 during baseline inventory
- **N2**: Phase 4 is heavy (two Large items) — be prepared to split
- **N3**: Stage 10 (Brainstorm) referenced but added in Phase 5 — forward reference is fine
- **N4**: Clean up old-convention filenames during Phase 1 naming migration

---

**This contract is binding upon human approval. Deviations require explicit acknowledgement per Build Session Protocol Rule 8.**

**Approved by Rob on 2026-03-15. Phase 1 execution began same session (SES-012).**
