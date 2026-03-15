---
id: SYS.compiler_inputs
type: system
note_class: architecture
domain: ai_governance
layer: systems
scope: null

canonical: false
authority_weight: 60
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

map: "[[Authority Pack Compiler — Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - system
  - compiler

hash: ""
---

# Compiler Inputs

## Purpose

Defines what the [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/compiler/Authority Pack Compiler]] accepts as inputs — the format, validation requirements, and resolution rules for all inputs to a compilation run.

## Required Inputs

| Input Type | Description | Source |
|---|---|---|
| Primary Pack | The root pack being compiled | [[Authority Pack Registry]] |
| Inheritance Graph | Resolved inheritance chain | [[Pack Lineage Index]] |
| Version Declarations | Declared versions for all packs | [[Pack Version Registry]] |
| Pack Manifest | Composition declaration | [[Pack Manifest]] |
| Host Identifier | Target runtime identifier | [[Host Runtime Reference]] |

## Validation Rules

1. All declared pack IDs must be resolvable in [[Authority Pack Registry]]
2. All declared versions must exist in [[Pack Version Registry]]
3. The inheritance graph must be acyclic
4. The pack manifest must conform to the manifest schema in [[Governance Schemas Reference]]
5. The host identifier must be a recognised runtime in [[Host Runtime Reference]]

## Failure Conditions

Any input validation failure is handled per [[Compile Failure Semantics]].

## Relationships

- [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/compiler/Authority Pack Compiler]] — the system consuming these inputs
- [[Compiler Pipeline]] — the pipeline stage that processes inputs
- [[Authority Pack Compiler — Map]]
