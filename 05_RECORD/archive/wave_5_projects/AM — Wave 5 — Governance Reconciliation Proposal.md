---
schema_version: 2
title: "AM — Wave 5 — Governance Reconciliation Proposal"
type: proposal
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 65
resolution_basis: authority_weight
status: active
review_status: approved
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines: []
  part_of:
    - "[[AM — Wave 5 — Contract]]"
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  applies_to:
    - "[[02_KNOWLEDGE/governance]]"
  uses:
    - "[[AM — Wave 5 — Governance Audit]]"
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - wave-5
  - phase-2
  - governance
  - reconciliation
  - proposal
hash: ""
---

# AM — Wave 5 — Governance Reconciliation Proposal

**Date**: 2026-03-15
**Status**: APPROVED (2026-03-15) (per Contract Rule 4)
**Source**: Governance Audit (AM — Wave 5 — Governance Audit.md)

---

## What This Proposal Addresses

The governance audit found 7 of 8 documents failing at least one audit type. This proposal defines the specific changes to bring all governance documents into alignment with Foundations.md. Changes are grouped by type to make approval efficient.

---

## Change Set A — Frontmatter Standardization (All 6 legacy docs)

**Applies to**: North Star, Principles, Modes, Scope, Strategy, Vault Rules

Replace the legacy frontmatter schema with the current schema_version: 2 format. For each document:

1. **Remove** legacy fields: `id:`, `scope: null`, `last_reviewed: null`, `review_cycle:`, `map:`, `maps:`, `related:`, `related_maps:`, `related_pipes:`
2. **Rename**: `created:` → `created_date:`, `updated:` → `last_modified:`
3. **Add** missing fields: `title:`, `domain:`, `layer:`, `resolution_basis:`, `source_type:`, `owner:`
4. **Populate** the relationships block with correct typed links (see per-doc sections below)

**Risk**: Low. Structural change only — no content modification.

---

## Change Set B — Authority Weight Adjustments

| Document | Current | Proposed | Rationale |
|----------|---------|----------|-----------|
| Foundations | 95 | 95 | No change — apex document |
| North Star | 90 | 90 | No change — correctly weighted |
| Principles | 90 | 70 | Reclassified as historical reference; superseded by Foundations |
| Modes | 90 | 75 | Operational pattern, not foundational doctrine |
| Scope | 65 | 80 | Governance boundary doc — per CLAUDE.md intent |
| Strategy | 65 | 80 | Governance strategy doc — per CLAUDE.md intent |
| Vault Rules | 92 | 85 | High governance, but below North Star and Foundations |
| Note Quality Rules | 70 | 70 | No change — correctly weighted as operational child |

**Risk**: Medium. Changes how conflicts resolve between these documents. The key shift is Principles dropping from 90 to 70, signaling Foundations as the authoritative source.

---

## Change Set C — Principles Reclassification

**Agent Maestro — Principles.md** changes from active governance to historical reference:

1. **Status**: `active` → `active` (retained for reference)
2. **Add frontmatter**: `superseded_by: ["[[Agent Maestro — Foundations]]"]`
3. **Add header notice**: Below the title, add: *"Historical reference. The 12 principles below are now superseded by the foundational kernel and 6 derived principles in [[Agent Maestro — Foundations]]. This document is retained for traceability — each original principle maps to a specific kernel element. See the [[AM — Wave 5 — Treatise on Core Principles]] for the full reconciliation."*
4. **authority_weight**: 90 → 70
5. **Remove**: `canonical: true` (no longer canonical — Foundations is)

**Risk**: Medium. This is the symbolic shift from 12 principles to the kernel. The content is preserved but the authority claim changes.

---

## Change Set D — Modes Conflict Resolution

The Modes document lists 5 modes (Exploration, Architecture, Deterministic, Execution, Evolution). The governance CLAUDE.md references 3 modes (Design, Governance, Execution). These are different mode sets.

**Proposed resolution**: Retain the 5-mode set from the Modes document as the authoritative version. The 3-mode reference in CLAUDE.md was a simplification that should be corrected. The 5 modes map cleanly to the Irreducible Loop:

| Mode | Loop Stage | What it governs |
|------|-----------|-----------------|
| Exploration | Perception + Interpretation | Discovering what exists and what it means |
| Architecture | Decision | Designing the structure of solutions |
| Deterministic | Validation gate | Defining contracts, rules, and constraints |
| Execution | Action | Building and deploying |
| Evolution | Memory + Feedback | Learning and improving |

Add this mapping to the Modes document and trace it to the Process seed.

**Risk**: Low. Corrects an inconsistency rather than changing actual practice.

---

## Change Set E — Broken Link Repair

Fix all broken wiki-links in governance documents:

| Document | Broken Link | Fix |
|----------|------------|-----|
| North Star | `Authority Architecture]]` | `[[Authority Architecture]]` |
| Principles | `Authority Architecture]]` (×2) | `[[Authority Architecture]]` |
| Principles | `[[02_KNOWLEDGE/patterns/\|pattern note]]` | `[[02_KNOWLEDGE/patterns]]` or remove |
| Scope | `[[Agent Systems\|Agent system architecture]]` | `[[Agent Systems]]` |
| Scope | `Authority Architecture\|Authority governance]]` | `[[Authority Architecture]]` |
| Scope | `[[Memory Architecture\|Memory architecture]]` | `[[Memory Architecture]]` |
| Strategy | `Authority Architecture]]` | `[[Authority Architecture]]` |
| Vault Rules | `[[Canonical Notes Registry]]` | Verify or remove |
| Vault Rules | `[[Canonical Notes Index]]` | Verify or remove |

**Risk**: Low. Link correction only.

---

## Change Set F — Vault Rules Content Fixes

1. **Rule 17**: Update template path from `01_CAPTURE/unprocessed/88_TEMPLATES/` to `88_TEMPLATES/`. Update the note to reflect that `88_TEMPLATES/` is the canonical template location.
2. **Rule 4**: Clarify "stable unique ID" — in current practice, the `title` field serves as the unique identifier. Reword to: "Every note must have a stable, unique title that serves as its identifier. Titles never change once a note is established."
3. **Rule 14**: Update `01_CAPTURE` description — it is now clear (0 unprocessed notes). Reword to reflect its role as an inbox that should be kept empty.
4. **Add**: `implements: [[Agent Maestro — Foundations]]` to relationships.

**Risk**: Low. Corrects outdated references.

---

## Change Set G — Note Quality Rules Disposition

Two options:

**Option 1 (Recommended)**: Merge Note Quality Rules into Vault Rules as a "Validation Checklist" section. This eliminates duplication and consolidates operational vault governance into a single document. Law 3 (Economy) supports this.

**Option 2**: Keep Note Quality Rules separate but update `implements` to reference Foundations and fix overlap with Vault Rules.

**Risk**: Low either way.

---

## Change Set H — Governance CLAUDE.md Update

Rewrite `02_KNOWLEDGE/governance/CLAUDE.md` to reflect:
1. Foundations as the apex document
2. Correct mode count (5, not 3)
3. Principles as historical reference
4. Correct file paths
5. Current agent permissions aligned with Foundations

**Risk**: Low. Infrastructure file, not a vault note.

---

## Execution Order

If approved:
1. Change Set A (frontmatter) — all docs simultaneously
2. Change Set B (weights) — applied during A
3. Change Set C (Principles reclassification) — applied during A
4. Change Set D (Modes fix) — content edit
5. Change Set E (links) — applied during A
6. Change Set F (Vault Rules fixes) — content edit
7. Change Set G (Note Quality Rules) — merge or update
8. Change Set H (CLAUDE.md) — rewrite

---

## Decision Required

Rob, please approve, modify, or reject:

1. **Change Sets A, B, E, F, H**: Structural fixes (frontmatter, weights, links, paths) — low risk
2. **Change Set C**: Principles reclassification (authority_weight 90 → 70, superseded by Foundations) — medium risk, symbolic
3. **Change Set D**: 5-mode resolution — low risk
4. **Change Set G**: Option 1 (merge Note Quality Rules into Vault Rules) or Option 2 (keep separate)?

---

**Approved by Rob on 2026-03-15. All change sets executed in SES-013.**
