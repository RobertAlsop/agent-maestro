---
title: "Skill — Triage"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Validate", "Skill — Gate"]
tags: [skill, triage, pipeline, capture]
---

## Purpose

Triage classifies incoming material and routes it to the correct pipeline stage. It answers the question: **what is this, and where does it belong?**

## Pipeline Stages Served

CAPTURE → KNOWLEDGE (primary handoff)

## When to Apply

Apply Triage to anything arriving in `01_CAPTURE/` or arriving unclassified — ideas, observations, links, drafts, tasks, or requests.

## Process

1. **Identify type** — What category does this input fall into?
   - Governance material (affects rules, principles, authority) → `02_KNOWLEDGE/governance/`
   - Concept or reference → `02_KNOWLEDGE/concepts/` or `02_KNOWLEDGE/references/`
   - Active decision or proposal → `03_DECIDE/`
   - Executable artifact or build → `04_EXECUTE/`
   - Record or log → `05_RECORD/`
   - Reflection or brainstorm → `06_REFLECT/`
   - Noise / not vault-relevant → discard

2. **Check completeness** — Is this ready to move, or does it need more context? If incomplete: leave in `01_CAPTURE/inbox/` with a note.

3. **Route** — Move or recommend moving to the identified destination.

4. **Log** — Note the routing decision if non-obvious.

## Escalation

- If classification is ambiguous between two stages: prefer the earlier stage (err toward CAPTURE or KNOWLEDGE rather than DECIDE or EXECUTE).
- If the item may be governance-level: escalate to Reviewer before routing.
- If genuinely unresolvable: Level 3 — escalate to human.

## Output

A routing decision: folder destination + reason. No document is created by Triage — it moves material, it doesn't transform it.
