---
id: SYS.host_bindings
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
  - runtime

hash: ""
---

# Host Bindings

## Purpose

The Host Bindings system manages the association between [[Compiled Governance Artifact|Compiled Governance Artifacts]] and their target host runtime environments — producing [[Integration Manifest|Integration Manifests]] that declare how compiled governance is loaded and enforced in a specific runtime.

## Context

Binding is the final stage of compilation. Without a host binding, a compiled artifact cannot be deployed. The binding step resolves the abstract compiled artifact into a runtime-specific governance contract.

## Responsibilities

### Inputs
- Compiled governance artifact (from [[Compiler Outputs]])
- Target host identifier (from [[Host Runtime Reference]])
- Runtime capability declarations

### Outputs
- [[Integration Manifest]] — binding contract for the target runtime

### Internal Components
- Host resolution — mapping host identifiers to runtime capability profiles
- Enforcement point mapping — mapping artifact rule sections to runtime enforcement points
- Condition declaration — runtime-specific activation conditions

### Failure Modes
- Unknown host identifier → binding fails; halt compilation
- Runtime does not support required capability → binding fails with capability mismatch report
- Artifact schema not compatible with runtime version → binding fails

## Relationships

- [[Host Binding]] (concept)
- [[Host Binding Pattern]] — the design pattern implemented here
- [[Integration Manifest]] — the artifact produced
- [[Host Runtime Reference]] — the reference for supported runtimes
- [[Authority Pack Compiler — Map]]
