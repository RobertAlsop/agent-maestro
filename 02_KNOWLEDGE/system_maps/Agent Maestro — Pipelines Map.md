---
id: MAP.agent_maestro.pipelines
type: system_map
note_class: architecture
domain: execution
layer: maps
scope: null

canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-10
updated: 2026-03-10
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

map: "[[Agent Maestro — Domain Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - map
  - navigation
  - pipelines

hash: ""
---

# Agent Maestro — Pipelines Map

## Purpose

Navigation layer for all operational pipelines.

---

# Pipelines

- [[Exploration Pipeline]]
- [[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]
- [[System Design Pipeline]]
- [[Agent Deployment Pipeline]]
- [[02_Systems/Bartram/03_PIPELINES/learning_pipeline/Learning Pipeline]]
- [[02_Systems/Bartram/03_PIPELINES/maintenance_pipeline/Maintenance Pipeline]]

---

# Mode Alignment

Each pipeline corresponds to a [[Agent Maestro — Modes|mode]]:

| Pipeline | Mode |
|---|---|
| Exploration | Exploration |
| Development + System Design | Architecture |
| Agent Deployment | Execution |
| Learning | Evolution |
| Maintenance | Deterministic |

---

# Related Maps

- [[Agent Maestro — Domain Map]]
- [[Agent Maestro — Projects & Experiments Map]]
