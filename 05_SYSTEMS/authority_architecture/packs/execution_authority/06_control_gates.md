---
id: SYS.pack.execution_authority.control_gates
type: authority_pack_section
note_class: governance
domain: system_architecture
layer: systems
scope: null

canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-10
updated: 2026-03-10
last_reviewed: null
review_cycle: quarterly

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

map: "[[Authority Architecture Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags: []

hash: ""
---
# Execution Authority — Control Gates

## Gates
Enforcement checkpoints that must be passed before an action proceeds.

- To be defined during pack authoring.

## Gate Failure Behaviour
What happens when a gate is not passed.

- See [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/execution_authority/12_failure_semantics]]

## Related
- [[Governance Before Autonomy]]
- [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/packs/execution_authority/05_rules]]
- [[Authority Architecture Map]]
