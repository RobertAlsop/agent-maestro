---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Authority Inheritance"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements:
    - "[[Authority Inheritance Pattern]]"
    - "[[Policy Resolution Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Authority Pack]]"
  uses:
    - "Pack Versioning]]"
  produces: []
  - "[[Agent Maestro — Pack Inheritance Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - governance
hash: ""
---

# Authority Inheritance

## Definition

The mechanism by which one [[Authority Pack]] derives its governance rules from a parent pack, adding to, restricting, or overriding specific rules while preserving the full lineage of the governance chain. Authority Inheritance enables modular, composable governance that can be specialised for specific roles, domains, or constellations without duplicating base rules.

## Boundaries

Authority Inheritance does not mean unrestricted extension. Child packs may only override rules within the bounds declared by the parent. Override rules that would violate parent constraints require explicit escalation or a new base pack. Inheritance is not the same as copying — the lineage must remain intact and traceable.

## Purpose

Inheritance allows governance to be defined once at the base level and specialised progressively. A base pack might define rules for all agents in a domain; a role pack inherits from it and adds role-specific constraints; a constellation pack inherits from the role pack and adds context-specific rules. This produces a coherent, traceable governance stack without redundancy.

## Key Properties

Every pack that inherits must declare:
- **Inherits from** — the parent pack (by stable ID and version)
- **Adds** — new rules or sections not present in the parent
- **Overrides** — parent rules being replaced (with justification)
- **Compatibility** — the parent versions this pack is compatible with

## Compilation

Inheritance chains are resolved by the 01_CAPTURE/inbox/Authority Pack Compiler]] during compilation. The compiler traverses the inheritance graph, applies overrides, and resolves conflicts per the [[Policy Resolution Pattern]].

## Relationships

- [[Authority Pack]] — the units that participate in inheritance
- Pack Versioning]] — versions must be tracked alongside inheritance
- [[Pack Override Rules]] — the rules governing what may be overridden
- [[Authority Inheritance Pattern]] — design pattern for structuring inheritance hierarchies
- [[Agent Maestro — Pack Inheritance Map]]
- [[Agent Maestro — Concepts Map]]
