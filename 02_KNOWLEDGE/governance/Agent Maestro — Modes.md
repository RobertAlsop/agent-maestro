---
schema_version: 2
title: "Agent Maestro — Modes"
type: modes
note_class: governance
domain: governance
layer: governance
authority_weight: 75
resolution_basis: authority_weight
canonical: true
status: active
review_status: approved
version: 2
created_date: 2026-03-10
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Operational Modes]]"
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - governance
  - modes
hash: ""
---

# Agent Maestro — Modes

## Purpose

Define the five operational modes that structure Agent Maestro work.

## Principle

Every Agent Maestro activity belongs to one of five modes. Modes prevent context-mixing and keep work purposeful. They are an instantiation of the Process seed (Irreducible Loop) applied to project lifecycle.

## Modes

| Mode | Focus | Loop Stage |
|---|---|---|
| **Exploration** | Discover opportunities for operational intelligence | Perception + Interpretation |
| **Architecture** | Design the structure of agent systems | Decision |
| **Deterministic** | Define contracts, validation rules, and authority boundaries | Validation gate |
| **Execution** | Deploy and operate systems | Action |
| **Evolution** | Improve systems through feedback loops and operational learning | Memory + Feedback |

## Traceability to Foundations

The five modes are a fractal instance of the Process seed. Each mode corresponds to one or more stages of the Irreducible Loop:

```
perception → interpretation → [validation] → decision → action → memory → feedback
    |              |               |             |          |        |          |
 Exploration   Exploration   Deterministic   Architecture  Execution  Evolution  Evolution
```

This means the modes are not arbitrary categories — they emerge naturally from the fundamental mechanics of any operational intelligence system. Moving through modes in order follows the loop; skipping modes means skipping loop stages.

## Implications

- Work must be tagged to a mode.
- Mixing modes in a single session leads to architectural drift.
- [[Controlled Evolution Pattern]] depends on moving through modes in order.
- The validation gate (Deterministic mode) must be visited before Execution — per the Constraint seed.

## When It Applies

Use to orient every working session and every project phase.

## Related

- [[Agent Maestro — Foundations]]
- [[Agent Maestro — Strategy]]
