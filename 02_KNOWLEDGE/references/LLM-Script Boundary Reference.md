---
schema_version: 2
title: "LLM-Script Boundary Reference"
type: reference
note_class: reference
domain: agent_maestro
layer: knowledge
authority_weight: 65
resolution_basis: authority_weight
canonical: true
status: active
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[LLM-Script Boundary]]"
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Vault Maintenance Constellation]]"
  uses:
    - "[[AM — Wave 5 — Audit Framework Rubric]]"
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - reference
  - scripts
  - llm
  - boundary
  - governance
hash: ""
---

# LLM-Script Boundary Reference

## Purpose

Define which vault maintenance tasks should be performed by deterministic scripts vs. LLM judgment, and why. This boundary implements D1 (Deterministic Control Surfaces): use scripts for verifiable, repeatable checks; use LLMs for tasks requiring interpretation, context, or judgment.

## The Boundary Principle

**Scripts** handle tasks where the answer is binary (pass/fail) and the rules are fully specified. **LLMs** handle tasks where the answer requires interpretation, context awareness, or nuanced judgment. The boundary is not about complexity — it's about whether the correct answer can be determined by rule alone.

## Current Script Inventory

| Script | Purpose | Executor | Foundations Alignment |
|--------|---------|----------|-----------------------|
| `validate_frontmatter.sh` | Check required fields, valid values, YAML structure | Script (deterministic) | Law 2: verifiable |
| `check_link_integrity.sh` | Verify wiki-links resolve to existing notes | Script (deterministic) | Law 2: verifiable |
| `detect_orphan_notes.sh` | Find notes with zero incoming links | Script (deterministic) | Structure seed: connectivity |
| `migrate_frontmatter.sh` | Batch rename/remove legacy fields | Script (deterministic) | D3: controlled evolution |

## Script Territory (Deterministic)

Tasks where scripts should be the executor:

- **YAML structure validation**: Does frontmatter begin/end with `---`? Are fields present? Are values from allowed sets?
- **Link resolution**: Does `[[Note Title]]` resolve to a file in the vault?
- **Orphan detection**: Does a note have zero incoming links?
- **Field migration**: Rename `created:` → `created_date:`, remove `id:`, etc.
- **Registry consistency**: Do CSV registries have expected columns? Are referenced files present?
- **Duplicate detection**: Do two notes have the same title?
- **File counting and inventory**: How many files per folder, per type, per status?

## LLM Territory (Judgment)

Tasks where LLM judgment is required:

- **Content alignment**: Does a note's body content actually implement what its frontmatter claims?
- **Relationship accuracy**: Are the typed relationships (defines, implements, governs) semantically correct?
- **Quality assessment**: Is a note substantive or placeholder? Does it "earn its place"?
- **Consolidation decisions**: Should two similar notes be merged? Which is the better version?
- **Authority weight calibration**: Is 65 the right weight for this note given its role?
- **Naming judgment**: Is this title clear, unique, and following convention?
- **Archive decisions**: Should this note be archived, rewritten, or retained?
- **Cross-reference verification**: Does the set of relationships form a coherent graph?

## Hybrid Territory (Script + LLM)

Some tasks require both:

| Task | Script Phase | LLM Phase |
|------|-------------|-----------|
| **Three-audit pass** | Frontmatter validation, link checking, orphan detection | Alignment audit, integrity review, viability assessment |
| **Note upgrade** | Migrate frontmatter fields | Assess content quality, populate relationships |
| **Pipeline rationalization** | Count pipeline files, check frontmatter | Classify as operational vs aspirational, decide on merge/archive |
| **Template compliance** | Check frontmatter against template schema | Assess body structure, evaluate section completeness |

## Priority 2 Script Candidates

Scripts that could be built next (beyond the Priority 1 set already delivered):

| Script | Purpose | Difficulty | Value |
|--------|---------|-----------|-------|
| `check_registry_consistency.sh` | Verify CSV registries match actual files | Medium | High — catches drift between registries and vault |
| `detect_duplicates.sh` | Find notes with identical or near-identical titles | Small | Medium — catches naming collisions |
| `count_inventory.sh` | Produce vault inventory by folder/type/status | Small | High — replaces manual counting |
| `validate_relationships.sh` | Check that relationship targets exist as notes | Medium | High — structural integrity |

## Integration with Logging

Scripts should integrate with the vault's logging infrastructure:

1. **Output format**: Scripts produce summary statistics suitable for inclusion in session logs
2. **CSV output option**: Add `--csv` flag to output machine-readable results for `06_EXECUTION/logs/`
3. **Exit codes**: 0 = pass, 1 = failures found, 2 = script error
4. **Timestamp**: All output includes ISO 8601 timestamp
5. **Vault root parameter**: All scripts accept vault root as first argument, defaulting to current directory

## Related

- [[AM — Wave 5 — Audit Framework Rubric]] — classifies checks by executor type
- [[Execution Architecture]] — three-layer model (Reasoning → Governance Mediation → Tool Execution)
- [[Tool Registry Design]] — tool registry architecture
