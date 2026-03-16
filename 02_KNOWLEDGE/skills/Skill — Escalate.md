---
title: "Skill — Escalate"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Gate", "Skill — Propose", "Skill — Audit"]
tags: [skill, escalate, human, governance, authority]
---

## Purpose

Escalate packages a decision for human review. It answers: **this is beyond my authority — here is everything you need to decide.** Escalation is not failure. It is Law 1 in action: accountability ascending to the human.

## Pipeline Stages Served

Any stage. Triggered whenever Gate returns Level 3, or whenever an agent encounters a decision it cannot resolve with available rules and principles.

## When to Apply

Mandatory escalation triggers:
- Any deletion of content (irreversible)
- Changes to documents with authority_weight ≥ 80
- Structural vault changes (new top-level folders, renaming pipeline stages)
- Governance conflicts the agent cannot resolve via authority hierarchy
- Any action the agent judges "I am not certain this is mine to decide"

## Escalation Package (what the human receives)

1. **What needs to be decided** — One clear question or choice.
2. **Why agent cannot resolve it** — Which rule or principle is insufficient, ambiguous, or absent.
3. **What was considered** — Options evaluated, with tradeoffs.
4. **What happens if approved** — Precise scope of the action to be taken.
5. **What happens if denied** — Alternative path or deferral plan.
6. **Recommended action** — Agent's best judgment, clearly labeled as a recommendation (not a decision).

## Halt Protocol

When Escalate is triggered, the agent HALTS the current action. No partial execution. The system returns to a stable state before pausing. The escalation package is presented to the human. Execution resumes only after human decision is received.

## Escalation Log

Every escalation is logged to `05_RECORD/logs/escalation_log.csv` with:
- Date, session ID
- What was escalated
- Human decision received
- Resolved by (human or deferred)

## Process

1. Identify the trigger (Level 3 gate, unresolvable conflict, or agent judgment).
2. Halt current action.
3. Compose the escalation package using the six elements above.
4. Present to human.
5. Log to `05_RECORD/logs/escalation_log.csv`.
6. Await decision before proceeding.

## Output

An escalation package (presented to human) + a log entry. Never a unilateral action.
