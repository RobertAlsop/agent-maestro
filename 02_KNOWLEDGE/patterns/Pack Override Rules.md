---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Pack Override Rules"
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
  - "[[Agent Maestro — Pack Inheritance Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - governance
hash: ""
---

# Pack Override Rules

## Summary

Override rules define the conditions under which a child pack may modify a parent pack's governance rules — and the documentation requirements for doing so. Overrides are not optional — if a child diverges from a parent rule, it must declare it explicitly.

## Problem

Without explicit override rules, inheritance chains produce silent divergence — child packs that contradict parent rules without traceability, making governance auditing impossible.

## Rules

1. **Explicit declaration** — every override must be named in section 00 (identity) of the child pack
2. **Justification** — every override must include a brief rationale
3. **Scope constraint** — a child pack may not override a rule marked `non_overridable` in the parent
4. **Version lock** — overrides must declare the parent version they override against
5. **Compiler validation** — overrides are validated during compilation; undeclared divergences cause compilation failure
6. **Traceability** — overrides are recorded in [[Pack Lineage Index]]

## Override Classes

| Class | Description |
|---|---|
| `restrict` | Narrows a parent rule (tighter constraints) |
| `extend` | Adds conditions to a parent rule |
| `replace` | Replaces a parent rule entirely (requires justification) |

## Relationships

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] — the context in which overrides operate
- [[Authority Inheritance Pattern]] — the pattern that declares overrides
- [[Compile Failure Semantics]] — what happens when override validation fails
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]] — overrides must be version-tracked
- [[Agent Maestro — Pack Inheritance Map]]
