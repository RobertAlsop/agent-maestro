---
id: MAP.agent_maestro_practice
type: map
note_class: navigation
domain: agent_maestro
layer: maps
scope: practice
canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: approved
version: 1
created: 2026-03-12
updated: 2026-03-12
last_reviewed:
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
map: "[[Agent Maestro — Navigation Map]]"
maps: []
related: []
related_maps:
  - "[[Agent Maestro — Governance Map]]"
  - "[[Agent Maestro — Pipelines Map]]"
  - "[[Project Governance Map]]"
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - map
  - navigation
  - practice
hash: ""
---

# MAP.agent_maestro_practice

> Operational guide for working within Agent Maestro day-to-day.

---

## Purpose

This map guides practitioners through the operational workflows of Agent Maestro — how to design agents, define authority, deploy constellations, and maintain governance integrity over time.

---

## How to Design an Agent

1. Identify the agent's role — executive, supervisor, or specialist (see [[Executive-Supervisor-Specialist Pattern]])
2. Determine the agent's authority scope — consult [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] and [[Decision Authority]]
3. Assign or create an [[Authority Pack]] using the [[Authority Pack Grammar]]
4. Link to the appropriate [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] or constellation definition
5. Register the agent in the [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]

---

## How to Define Authority

- Start from the [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]] — understand the conceptual framework
- Apply [[Authority Pack Grammar]] — sections 00–13
- Use [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] to inherit from a base pack where applicable
- Apply [[Pack Override Rules]] to manage deviations
- Version the pack using [[Pack Versioning Pattern]]
- Register in [[Authority Pack Registry]] and [[Pack Version Registry]]

---

## How to Deploy a Constellation

- Define the constellation structure (see [[Constellation Architecture Pattern]])
- Link executive, supervisors, and specialists (see [[Executive-Supervisor-Specialist Pattern]])
- Apply authority packs to each layer
- Run the [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] to produce [[Compiled Governance Artifact|compiled governance artifacts]]
- Bind outputs using [[Host Binding Pattern]]
- Register in [[Constellation Index]]

---

## How to Maintain the Vault

- Consult [[Agent Maestro — Vault Rules]] before structural changes
- New notes must conform to the template schema in `OBSIDIAN/88_templates/notes`
- All new objects must be registered in the appropriate registry
- Use [[Pack Lineage Index]] to track authority lineage

---

## Key Patterns for Daily Practice

- [[Governance Before Autonomy]]
- [[Evidence Over Assumptions]]
- [[Deterministic Control Surfaces]]
- [[Decision-Execution Separation]]
- [[Anti-Agent-Sprawl Pattern]]
- [[Human Escalation Pattern]]
- [[Controlled Evolution Pattern]]

---

## Related

- [[Agent Maestro — Pipelines Map]]
- [[Agent Maestro — Governance Map]]
- [[Project Governance Map]]
- [[Agent Maestro — Navigation Map]]
