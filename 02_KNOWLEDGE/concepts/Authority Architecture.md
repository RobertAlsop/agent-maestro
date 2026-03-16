---
title: "Authority Architecture"
type: concept
status: active
authority_weight: 55
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — North Star]]"
  governs: []
  related:
    - "[[Role — Worker]]"
    - "[[Role — Reviewer]]"
    - "[[Skill — Gate]]"
    - "[[Skill — Escalate]]"
tags: [concept, authority, governance, foundational]
---

# Authority Architecture

## Purpose

Define how authority flows through Agent Maestro — the connective tissue between governance principles and operational execution.

## Definition

Authority Architecture is the system by which purpose descends and accountability ascends through every layer of Agent Maestro. It is the operational expression of Law 1 (Direction of Authority), Seed 3 (Constraint), and D4 (Human Sovereignty).

## The Authority Chain

Purpose descends from the human through governance to execution:

```
Human Intent
  → North Star (authority_weight: 97) — mission and intent
    → Foundations (authority_weight: 95) — kernel mechanics
      → Governance docs (80-94) — rules, scope, strategy
        → Roles (70) — authority boundaries
          → Skills (60) — capabilities
            → Agent instantiation — runtime execution
```

Accountability ascends in the reverse direction: every action is traceable upward through the chain to the human who authorized the system's purpose.

## Three-Level Escalation

Not every decision needs to travel the full chain. The escalation model routes decisions to the appropriate level:

| Level | When | Resolution |
|-------|------|------------|
| 1 — Automatic | Rules cover it | Pass/fail against criteria. [[Role — Worker\|Worker]] executes. |
| 2 — Agent Judgment | Principles apply | Trace decision to [[Agent Maestro — Foundations\|Foundations]]. [[Role — Reviewer\|Reviewer]] evaluates. |
| 3 — Human Approval | Irreversible, architectural, or governance-level | Escalate with full context. Human decides. |

## Authority Weights

Authority weight is a numeric signal (0-100) that determines precedence when documents conflict. Higher weight wins. The ranges are defined in [[Agent Maestro — Vault Rules|Vault Rule 48]].

The weight doesn't measure importance — it measures *authority to override*. A concept at weight 40 might be deeply important, but it yields to a governance doc at weight 85 when they conflict.

## Key Principles

- **No level may bypass the one above it** (Seed 3, Constraint). No execution without routing. No routing without validation. No validation without schema.
- **Human sovereignty is non-negotiable** (D4). The human sits at the top of every authority chain. No autonomous action may be irreversible without human approval.
- **Separation of powers** (D6). The entity that proposes must not approve. The entity that executes must not audit.

## Traceability

This concept ties together Law 1 (Direction of Authority), Seed 3 (Constraint), D4 (Human Sovereignty), and D6 (Separation of Powers) into a single operational model. It is the architecture that the [[Skill — Gate|Gate]] and [[Skill — Escalate|Escalate]] skills implement at runtime.

## Related

- [[Agent Maestro — Foundations]]
- [[Agent Maestro — Vault Rules]]
- [[Skill — Gate]]
- [[Skill — Escalate]]
