---
id: PAT.deterministic_authority_resolution
type: pattern
note_class: knowledge
domain: agent_maestro
layer: knowledge
schema_version: 2
status: active
review_status: reviewed
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
authority_weight: 65
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Authority Architecture]]"
    - "[[Governance Compilation Pattern]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs:
    - "[[Authority Pack Compiler]]"
  inherits_from:
    - "[[Governance Compilation Pattern]]"
  applies_to:
    - "[[Authority Pack]]"
  uses:
    - "[[Authority Pack]]"
  produces:
    - "[[Compiled Governance Artifact]]"
tags:
  - pattern
  - agent_maestro
  - authority_pack
  - compiler
  - determinism
---

# Deterministic Authority Resolution Pattern

## Purpose

Defines the algorithm by which authority packs are resolved into compiled governance artifacts. This pattern makes authority packs truly machine-compilable by specifying a deterministic resolution sequence.

## The Pattern

Once canonical flags and authority weights are set on notes, a deterministic compilation rule applies:

**Authority Resolution Algorithm:**

```
1. Collect candidate notes
2. Filter canonical=true
3. Sort by authority_weight
4. Apply inheritance chain
5. Produce compiled pack
```

This means: authority packs become machine-compilable without human intervention, and resolution is predictable and auditable.

## Preconditions

For this pattern to function, every authority pack note must have:
- `canonical: true/false` — marks whether this is the authoritative form
- `authority_weight: 0–100` — determines priority when multiple candidates conflict
- `inherits_from: [...]` — defines the inheritance chain

## Why This Matters

Without deterministic resolution:
- Conflicting notes produce ambiguous governance
- Agents may interpret different versions as authoritative
- Compilation is a manual, error-prone process

With deterministic resolution:
- Any agent can resolve the correct authority pack given a class and context
- The compiler produces identical results on every run
- Conflicts surface as explicit ambiguities rather than silent drift

## Relationship to the Compiler

This pattern is the core algorithm inside the [[Authority Pack Compiler]]. The compiler's 8-stage pipeline implements this pattern as its authority resolution step.

See: `05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py`

## Relationships

- [[Authority Pack Compiler]] — the system that implements this pattern
- [[Compiled Governance Artifact]] — the output of this algorithm
- [[Governance Compilation Pattern]] — the broader pattern this is part of
- [[Authority Pack]] — the input artifact
- [[Pack Versioning Pattern]] — how versioning interacts with resolution
