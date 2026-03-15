---
type: index
note_class: navigation
domain: agent_architecture
layer: maps

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2
title: "Constellation Index"

status: active
review_status: approved
version: 1

created_date: 2026-03-12
last_modified: 2026-03-12

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []


  - "[[Agent Maestro — Systems Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - index
  - constellation

hash: ""
---

# Constellation Index

## Purpose

Navigation index of all [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation|Agent Constellations]] instantiated in the Agent Maestro system. Constellations must be registered in [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]] and listed here for human navigation.

## Context

Constellations are the primary structural units of governed agent deployment. This index provides a human-readable directory of all constellations, their status, and their location in the vault.

## Relationships

Each constellation is a governed cluster following the [[Constellation Architecture Pattern]] with folder structure defined in [[Agent Maestro — Constellation Architecture Map]].

## Index

### Active Constellations

*(No constellation instances yet — folder structure and governance pattern defined. Add entries as constellations are instantiated.)*

| Constellation | Folder | Status | Executive | Registered |
|---|---|---|---|---|
| *(example)* | `05_SYSTEMS/agent_systems/constellations/<name>/` | draft | TBD | — |

## Entry Rules

1. A constellation must have a system note and 00_map before being listed as active
2. Every constellation must be registered in [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]
3. Authority packs must be applied before status becomes active

## Related

- [[Agent Maestro — Constellation Architecture Map]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] (concept)
