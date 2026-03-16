---
title: "Self-Observation"
type: concept
status: active
authority_weight: 50
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related:
    - "[[Skill — Audit]]"
    - "[[Agent Maestro — Strategy]]"
tags: [concept, self-observation, foundational]
---

# Self-Observation

## Purpose

Define how Agent Maestro monitors its own health and identifies opportunities for improvement. This concept is the foundation for the system's eventual self-improvement capability.

## Definition

Self-observation is the system's ability to assess its own state — the quality of its governance, the integrity of its knowledge, the effectiveness of its pipeline, and the alignment of its components with the [[Agent Maestro — North Star]]. It is the Reflect stage made systematic.

## What Self-Observation Checks

Self-observation applies the three audit lenses (from [[Skill — Audit]]) to the system as a whole:

### Alignment (top-down)
Is the vault serving its stated purpose? Do the governance documents still reflect the human's intent? Has the system drifted from the North Star?

### Integrity (horizontal)
Are all parts consistent with each other? Do wiki-links resolve? Does frontmatter conform to schema? Are there contradictions between governance documents?

### Viability (bottom-up)
Is everything earning its place? Are there documents nobody references? Skills that never get used? Folders that accumulate without being processed? Law 3 applied to the whole vault.

## Current Implementation

Self-observation is currently **manual and collaborative** — Rob and Claude walk through the vault together, asking questions and checking alignment. This is exactly what Wave 5.2 is doing.

The tools in `04_EXECUTE/tools/` provide some automated support: `schema_validator.py` checks frontmatter, `link_auditor.py` checks wiki-links, `detect_orphan_notes.sh` finds orphans. But semantic assessment (is this document *good*?) requires human-AI collaboration.

## Future Direction

Per [[Agent Maestro — Strategy]], the path from Stage 1 (Self-Governance) toward Stage 2 (First External Application) requires self-observation to become more systematic and eventually more autonomous. The progression:

1. **Manual** (current) — Human + AI walk the vault together
2. **Scheduled** — Automated integrity checks run on a cycle, surfacing issues for human review
3. **Proposing** — The system identifies issues and drafts proposals for improvement, subject to human approval
4. **Self-improving** — The full Reflect → Capture → Decide → Execute loop runs with human gate at Level 3 only

Each step increases autonomy while maintaining governance. D5 (Governance Before Autonomy) applies — the governance for each step must exist before the capability is deployed.

## Traceability

Self-observation is the operational expression of Seed 1 (Process) — specifically the feedback stage of the Irreducible Loop. It also implements Seed 2 (Structure) — the Feedback primitive ("how do we know if the action worked?"). The three audit lenses come directly from the Audit Taxonomy in [[Agent Maestro — Foundations]].

## Related

- [[Agent Maestro — Foundations]]
- [[Skill — Audit]]
- [[Agent Maestro — Strategy]]
