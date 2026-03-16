---
title: "Skill — Validate"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations", "Agent Maestro — Vault Rules"]
  governs: []
  related: ["Skill — Gate", "Skill — Audit"]
tags: [skill, validate, governance, schema]
---

## Purpose

Validate checks any artifact against the vault's governance rules. It answers: **does this conform?** Validate is a fast, rule-based check — it does not require judgment. Either the artifact meets the criteria or it doesn't.

## Pipeline Stages Served

All stages. Called by Gate at every stage transition.

## What Validate Checks

### Schema compliance (all vault notes)
- Frontmatter present and well-formed
- All required schema v3 fields present: `title`, `type`, `status`, `authority_weight`, `schema_version`, `created`, `updated`, `relationships`, `tags`
- `type` is a valid value: `governance | concept | skill | role | pipeline | log | report | proposal`
- `status` is a valid value: `draft | active | archived`
- `authority_weight` is 0–100 (integer)
- `schema_version` is 3
- All dates in ISO 8601 (`YYYY-MM-DD`)

### Structural compliance
- Note has a `## Purpose` section
- All wiki-links (`[[...]]`) resolve to existing notes
- Note is not orphaned (has at least one inbound or outbound link, or is an index)

### Authority compliance
- `derives_from` is populated for notes with authority_weight ≥ 40
- Notes claiming authority_weight ≥ 80 are in `02_KNOWLEDGE/governance/`

## Process

1. Load the artifact to check.
2. Run each check. Record pass/fail for each.
3. If all pass: **VALID** — proceed.
4. If any fail: **INVALID** — list failures, block stage transition, return to author for repair.

## Escalation

Validate does not escalate — it passes or fails. Failures are returned to the Worker for repair before Gate re-evaluates. If a failure involves a potential governance conflict, the repair must go through Gate before proceeding.

## Output

A validation result: `VALID` or `INVALID [list of failures]`.
