---
title: "Skill — Propose"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Audit", "Skill — Gate", "Skill — Escalate"]
tags: [skill, propose, change, decision]
---

## Purpose

Propose formulates a change proposal with evidence and traceability. It answers: **what should change, and why?** A proposal is the bridge between an audit finding and a decision. Nothing changes without a proposal. No proposal advances without a gate.

## Pipeline Stages Served

DECIDE (primary). Triggered by Audit findings, Reflect outputs, or direct human briefs.

## When to Apply

- An audit has produced findings that require action
- A new capability, document, or structural change is being proposed
- The human has requested a change that needs to be formalized before execution

## A Proposal Must Contain

1. **Problem statement** — What is the issue or opportunity? Cite evidence.
2. **Proposed change** — What specifically will change? Be precise about scope.
3. **Traceability** — Which Foundations principle(s) support this change? (Derive_from chain)
4. **Impact assessment** — What else does this affect? What could go wrong?
5. **Alternative considered** — What else was evaluated and why it was rejected.
6. **Gate criteria** — How will we know if this proposal is ready to execute? What does success look like?

## Proposal Types

| Type | When | Who approves |
|------|------|-------------|
| Operational | Routine vault maintenance, note repairs | Level 1 — automatic (Worker executes) |
| Structural | New folders, new templates, new skills | Level 2 — Reviewer gate |
| Governance | Changes to authority_weight ≥ 80 docs | Level 3 — Human approval |

## Process

1. Draft the proposal using the six required elements above.
2. Place in `03_DECIDE/proposals/` with status: draft.
3. Trigger Gate to evaluate.
4. If Gate passes: status → active; move to `03_DECIDE/active/` for execution.
5. If Gate requires escalation: apply Escalate skill.

## D6 Compliance

The entity that proposes must not approve. A Worker may draft a proposal; a Reviewer must gate it. The same model may do both only if they are operating in different role contexts (Worker session → Reviewer session).

## Output

A proposal document in `03_DECIDE/proposals/` conforming to schema v3 with type: proposal.
