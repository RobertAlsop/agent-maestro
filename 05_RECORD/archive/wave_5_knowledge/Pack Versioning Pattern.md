---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Pack Versioning Pattern"
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
    - "Pack Versioning]]"
  uses: []
  produces: []
  - "[[Agent Maestro — Pack Inheritance Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - versioning
hash: ""
---

# Pack Versioning Pattern

## Summary

Version every authority pack using semantic versioning, register every version in the [[Pack Version Registry]], declare compatibility with parent versions, and never mutate a pack in place — always increment the version and record the change.

## Problem

Unversioned packs cannot be audited, compared, or safely evolved. Governance changes become invisible.

## Solution

Apply semantic versioning (MAJOR.MINOR.PATCH) to every pack, with change type determining the bump level. Every new version is registered in [[Pack Version Registry]] before it can be used in a compilation.

## Versioning Rules

| Change Type | Bump | Example |
|---|---|---|
| Breaking governance change | MAJOR | Remove or restrict a governed action |
| Backwards-compatible extension | MINOR | Add a new control gate |
| Non-functional change | PATCH | Update documentation or examples |

## Required Version Record Fields

- `version` — semver identifier
- `parent_version` — version this was derived from
- `change_summary` — brief description of changes
- `compatibility` — compatible parent pack versions
- `compiled_artifacts` — artifacts compiled from this version

## Relationships

- Pack Versioning]] — the concept this pattern implements
- [[Pack Version Registry]] — the registry where versions are recorded
- [[Pack Lineage Index]] — the navigation index for version history
- [[Authority Inheritance Pattern]] — version compatibility declarations live here
- [[Controlled Evolution Pattern]] — the broader safe-evolution pattern
- [[Agent Maestro — Pack Inheritance Map]]
