---
title: "Skill — Gate"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Validate", "Skill — Audit", "Skill — Escalate"]
tags: [skill, gate, pipeline, transition, governance]
---

## Purpose

Gate evaluates pipeline stage transitions. It answers: **is this ready to move forward?** Every transition between pipeline stages passes through a gate. Gate intensity scales with what's at stake.

## Pipeline Stages Served

Between ALL stages. Gate is the mechanism that keeps the pipeline honest.

## The Three Gate Levels

### Level 1 — Automatic
**Trigger:** Rules cover it completely.
**Resolution:** Run Validate. Pass or fail against defined criteria. No judgment needed.
**Examples:** Note moving from CAPTURE to KNOWLEDGE; log entry being written to RECORD.

### Level 2 — Agent judgment
**Trigger:** Rules are insufficient, but principles apply.
**Resolution:** Agent traces the decision back to the Foundations. If a traceable justification exists, proceed. Document the reasoning.
**Examples:** Classifying an ambiguous input; deciding whether to archive or keep a borderline artifact.

### Level 3 — Human approval
**Trigger:** Action is irreversible, architectural, or governance-level.
**Resolution:** Apply Escalate skill. Do not proceed until human decides.
**Examples:** Deleting content, changing vault structure, modifying governance documents.

## Gate Process

1. **Identify the transition** — What stage is this artifact moving from/to?
2. **Determine gate level** — Level 1 if rules cover it; Level 2 if judgment needed; Level 3 if irreversible or governance.
3. **Apply the resolution:**
   - L1: Run Validate. Pass → proceed. Fail → return for repair.
   - L2: Apply Foundations principles. Proceed with documented justification. Flag any uncertainty.
   - L3: Package context, apply Escalate, halt until human decides.
4. **Record the gate decision** — Log outcome in `05_RECORD/logs/`.

## Adversarial Gate

For governance-level transitions (highest stakes), Gate applies the adversarial mode: actively seek reasons to block. The artifact must survive challenge before advancing.

## D6 Compliance

The entity that executed a stage must not gate its own work. A Worker builds; a Reviewer gates.

## Output

A gate decision: PASS / FAIL / ESCALATE, with reason. Logged to `05_RECORD/logs/`.
