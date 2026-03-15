---
schema_version: 2
title: "AM — Wave 5 — Baseline Inventory"
type: reference
note_class: execution
domain: agent_maestro
layer: execution
authority_weight: 60
resolution_basis: authority_weight
status: active
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[AM — Wave 5 — Contract]]"
  implements:
    - "[[Law 2 — Action Properties]]"
  governs: []
  applies_to: []
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - wave-5
  - baseline
  - inventory
  - phase-1
hash: ""
---

# AM — Wave 5 — Baseline Inventory

**Date**: 2026-03-15
**Session**: SES-012 (Wave 5, Phase 1)
**Purpose**: "Before" snapshot for Wave 5 alignment pass. All metrics measured pre-build.
**Starting version**: v0.4.0 (commit 9070f69)

---

## 1. File Counts by Folder

| Folder | .md | .csv | .py | .json | .yaml | Total |
|--------|-----|------|-----|-------|-------|-------|
| 01_CAPTURE | 1 | 0 | 0 | 0 | 0 | 1 |
| 02_KNOWLEDGE | 123 | 1 | 0 | 0 | 0 | 124 |
| 03_PIPELINES | 13 | 0 | 0 | 0 | 0 | 13 |
| 04_PROJECTS | 29 | 0 | 0 | 0 | 0 | 29 |
| 05_SYSTEMS | 215 | 5 | 16 | 19 | 24 | 279 |
| 06_EXECUTION | 34 | 8 | 0 | 28 | 0 | 70 |
| 88_TEMPLATES | 28 | 0 | 0 | 0 | 0 | 28 |
| 99_ARCHIVE | 56 | 0 | 0 | 0 | 0 | 56 |
| Root | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **500** | **14** | **16** | **47** | **24** | **601** |

**Note**: 01_CAPTURE contains 1 CLAUDE.md (infrastructure). N1 from audit notes confirmed: 0 unprocessed notes.

---

## 2. Authority Weight Distribution

| Weight | Count | Tier |
|--------|-------|------|
| 95 | 11 | Canonical / Foundational |
| 92 | 4 | Near-canonical |
| 90 | 18 | Governance |
| 85 | 40 | High governance |
| 80 | 5 | Governance |
| 75 | 10 | Operational governance |
| 70 | 129 | Standard operational |
| 65 | 26 | Operational |
| 60 | 147 | Standard |
| 55 | 1 | Below standard |
| 50 | 6 | Low |
| 40 | 9 | Low |
| 30 | 1 | Very low |
| 20 | 3 | Minimal |
| Malformed/missing | ~5 | Template placeholders |

**Total notes with authority_weight**: ~416

---

## 3. Note Types (top 15)

| Type | Count |
|------|-------|
| authority_pack_section | 114 |
| concept | 57 |
| system | 42 |
| process | 22 |
| system_map | 19 |
| agent_definition | 17 |
| pipeline | 13 |
| project | 12 |
| pattern | 10 |
| map | 10 |
| index | 9 |
| reference | 8 |
| roadmap | 7 |
| registry | 6 |
| strategy | 5 |

---

## 4. Note Status

| Status | Count |
|--------|-------|
| active | 393 |
| draft | 15 |
| completed | 10 |
| archived | 3 |
| incubating | 2 |
| deprecated | 1 |

---

## 5. Note Classes

| Class | Count |
|-------|-------|
| governance | 130 |
| architecture | 81 |
| knowledge | 70 |
| execution | 53 |
| navigation | 18 |
| planning | 11 |
| doctrine | 10 |
| registry | 9 |
| reference | 7 |
| classification | 3 |
| specification | 1 |
| evaluation | 1 |

---

## 6. Structural Observations

- **02_KNOWLEDGE** is the largest knowledge folder (123 md), with heavy concentrations in concepts (37), system_maps (23), and patterns (20)
- **05_SYSTEMS** is by far the largest folder (279 files), dominated by authority_architecture (171 files — mostly authority pack sections and compiled JSON artifacts)
- **03_PIPELINES** has 13 files across 4 categories (deployment, development, exploration/learning, maintenance)
- **88_TEMPLATES** has 28 files inherited from 01_CAPTURE, organized into 4 template categories plus docs
- **99_ARCHIVE** has 56 read-only reference items
- **01_CAPTURE** is clear (confirmed N1 from audit notes)

---

## 7. Key Ratios

- Authority pack sections (114) represent 23% of all notes — largest single type
- 05_SYSTEMS alone holds 46% of all vault files
- Governance-class notes (130) are the most common class — expected for a governance-first vault
- 93% of notes are status: active — suggesting few have been through lifecycle management

---

**This inventory serves as the "before" measurement for the Wave 5 final audit report (Phase 6, item 6e).**
