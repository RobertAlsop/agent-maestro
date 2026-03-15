---
id: MAP.agent_maestro.constellation_architecture
type: system_map
note_class: architecture
domain: agent_architecture
layer: maps
scope: null

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: approved
version: 1

created: 2026-03-12
updated: 2026-03-12
last_reviewed: null
review_cycle: annual

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

map: "[[Agent Maestro — Systems Map]]"
maps: []

related: []
related_maps:
  - "[[Agent Maestro — Agent Taxonomy Map]]"
  - "[[Authority Architecture Map]]"
  - "[[Agent Maestro — Systems Map]]"
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - map
  - constellation
  - architecture

hash: ""
---

# Agent Maestro — Constellation Architecture Map

## Purpose

Architecture reference for governed agent constellations — how they are structured, governed, and instantiated.

---

## Core Concept

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — the concept: a governed cluster of agents sharing authority architecture
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] — the broader deployment context containing constellations

---

## Structural Pattern

- [[Executive-Supervisor-Specialist Pattern]] — the canonical three-layer structure
- [[Constellation Architecture Pattern]] — full design pattern for constellation composition

---

## System Implementation

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] (system) — implementation reference in `05_SYSTEMS/agent_systems/constellations/`
- [[Executive Layer]] — system note for the executive layer
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]] (system) — services shared across agents in a constellation

---

## Standard Constellation Folder Structure

Each constellation instance follows this layout:

```
<constellation_name>/
  00_map/             — navigation map for this constellation
  01_executive_links/ — links to executive agent definitions
  02_supervisors/     — supervisor agent definitions
  03_specialists/     — specialist agent definitions
  04_workflows/       — workflow definitions
  05_memory/          — memory architecture for this constellation
  06_authority_links/ — links to applicable authority packs
  07_metrics/         — metrics and observability definitions
```

---

## Authority Governance

Constellations are governed by authority packs applied at each layer. See:

- [[Authority Pack]] — atomic governance contract
- [[Authority Architecture Map]] — full authority architecture
- [[Agent Maestro — Pack Inheritance Map]] — inheritance and versioning

---

## Registry

- [[Constellation Index]] — navigational index of all constellations
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]] — registry-resolvable system entries

---

## Related Maps

- [[Agent Maestro — Agent Taxonomy Map]]
- [[Agent Maestro — Systems Map]]
- [[Authority Architecture Map]]
- [[Agent Maestro — Navigation Map]]
