---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Policy Resolution Pattern"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]"
  uses: []
  produces: []
  - "[[Authority Pack Compiler — Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - governance
hash: ""
---

# Policy Resolution Pattern

## Summary

When multiple authority pack rules apply to the same situation and conflict, resolve them using a deterministic priority order: more specific beats more general, explicit overrides beat inherited defaults, and unresolvable conflicts fail compilation rather than silently choosing.

## Problem

In an inheritance chain, multiple rules from different pack levels can apply to the same action. Without a resolution algorithm, the compiler cannot determine which rule wins.

## Resolution Order

1. **Explicit override** — a child pack's declared override always wins against the parent rule it names
2. **Specificity** — the rule with the narrower scope wins (constellation > domain > role > base)
3. **Restriction wins** — when two rules conflict and neither explicitly overrides the other, the more restrictive rule wins (default safe behaviour)
4. **Escalation on tie** — if restriction cannot determine a winner, the compilation fails and flags the conflict for human resolution

## Rules

1. Resolution is deterministic — same inputs always produce the same result
2. Conflicts that cannot be resolved deterministically cause compilation failure
3. Resolution outcomes are logged in the compiled artifact for auditability

## Relationships

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] — the context where policy conflicts arise
- [[Governance Compilation Pattern]] — the broader compilation process this is part of
- [[Compile Failure Semantics]] — what happens when resolution fails
- [[Pack Override Rules]] — explicit overrides are the highest-priority resolution
- [[Authority Pack Compiler — Map]]
