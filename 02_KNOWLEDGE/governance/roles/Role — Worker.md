---
title: "Role — Worker"
type: role
status: active
authority_weight: 70
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related:
    - "[[Role — Reviewer]]"
    - "[[Skill — Triage]]"
    - "[[Skill — Validate]]"
    - "[[Skill — Summarize]]"
    - "[[Skill — Gate]]"
tags: [role, worker, execution, pipeline]
---

## Purpose

The Worker executes pipeline stages and builds artifacts. Workers operate at Level 1–2 authority. They do the work of the system — processing, building, classifying, recording. A Worker can be a human or an LLM — the role defines the authority boundaries, not the entity. When Rob is building and Claude is reviewing, Rob is the Worker.

## Authority Level

**Level 1–2.** Workers can:
- Execute routine operational actions without approval
- Apply agent judgment for Level 2 decisions (with documented reasoning)
- Cannot approve their own work
- Cannot modify documents in `02_KNOWLEDGE/governance/` with authority_weight ≥ 80
- Cannot take irreversible structural actions without escalation

## Skills Available

| Skill | Use |
|-------|-----|
| [[Skill — Triage|Triage]] | Classify and route incoming material |
| [[Skill — Validate|Validate]] | Check artifacts against schema and rules |
| [[Skill — Summarize|Summarize]] | Create records, logs, session summaries |
| [[Skill — Gate|Gate]] | Apply Level 1 gates (rule-based only); escalate Level 2–3 to [[Role — Reviewer|Reviewer]] |

Workers do not hold [[Skill — Audit|Audit]], [[Skill — Propose|Propose]], or [[Skill — Escalate|Escalate]] as primary skills. They may recognize escalation triggers and hand off to a Reviewer, but the escalation package is composed by the Reviewer.

## What Workers MAY Do

- Read all vault folders
- Write to `01_CAPTURE/`, `04_EXECUTE/`, `05_RECORD/`
- Write to `02_KNOWLEDGE/` (concepts, references, indexes — not governance)
- Draft proposals in `03_DECIDE/proposals/` (drafting is Worker work; approval is not)
- Move artifacts between stages after Level 1 gate passes
- Execute build instructions from approved contracts in `03_DECIDE/active/`
- Run runtime code and tools in `04_EXECUTE/`
- Write session logs and operational records

## What Workers MUST NOT Do

- Approve their own work
- Modify documents in `02_KNOWLEDGE/governance/` directly
- Take Level 3 actions (deletions, structural changes) without escalation
- Proceed past a gate that returns Level 3
- Skip a gate

## D6 Compliance

Per D6 (Separation of Powers) in [[Agent Maestro — Foundations]], a Worker must not review the same work it built. If a model builds as Worker, it must switch to [[Role — Reviewer|Reviewer]] role in a distinct context to review that work. The same entity (human or LLM) can play both roles — never for the same work in the same context.

## Instantiation

Workers are instantiated on demand:
```
Model: [chosen model]
Role: Worker
Skills loaded: Triage, Validate, Summarize, Gate
Context: [current pipeline stage and task]
```

Agents are not permanent entities. They are dissolved when the task is complete.
