---
id: PAT.authority_inheritance_pattern
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
scope:
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: draft
version: 1
created: 2026-03-12
updated: 2026-03-14
last_reviewed:
review_cycle: none
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Authority Pack]]"
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]]"
  uses: []
  produces: []
map: "[[Agent Maestro — Concepts Map]]"
maps:
  - "[[Agent Maestro — Pack Inheritance Map]]"
related: []
related_maps: []
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - governance
hash: ""
---

# Authority Inheritance Pattern

## Summary

Structure pack inheritance as a layered chain — base, role, domain, constellation — where each layer declares what it inherits, adds, and overrides. Never allow silent inheritance; every derivation must be explicit.

## Problem

Governance rules need to be specialised for different roles, domains, and contexts without duplicating base rules or creating inconsistency between derived packs.

## Solution

Define a four-layer pack hierarchy: base packs (foundational rules), role packs (role-specific additions), domain packs (domain-scoped rules), constellation packs (context-specific rules). Each pack declares its parent via stable ID and version.

## Rules

1. Every non-base pack must declare `inherits_from` in its identity section (00_identity)
2. Every pack must declare what it adds beyond its parent
3. Every override must be named and justified
4. Inheritance depth should not exceed four layers without architectural review
5. Parent pack version compatibility must be declared

## Relationships

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] — the concept this pattern implements
- [[Pack Override Rules]] — the rules governing overrides within this pattern
- [[Authority Pack Grammar]] — the structural standard that makes inheritance possible
- [[Controlled Evolution Pattern]] — the higher-level pattern governing governance evolution
- [[Agent Maestro — Pack Inheritance Map]]
