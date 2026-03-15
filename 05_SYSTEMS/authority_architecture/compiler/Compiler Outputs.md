---
type: system
note_class: architecture
domain: ai_governance
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Compiler Outputs"

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



source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - system
  - compiler

hash: ""
---

# Compiler Outputs

## Purpose

Defines what the Authority Pack Compiler]] produces — the artifact types, schemas, and registration requirements for all outputs of a compilation run.

## Output Types

### Primary Output: Compiled Governance Artifact
- Schema: [[Compiler Artifact Schemas Reference]] (Compiled Governance Artifact Schema)
- Registration: [[Compiler Artifacts Registry]]
- Contains: resolved rules, inheritance graph, source pack references, checksum

### Secondary Output: Integration Manifest
- Schema: [[Compiler Artifact Schemas Reference]] (Integration Manifest Schema)
- Produced by: [[Host Bindings]] stage
- Contains: host binding declarations, enforcement point map, binding conditions

### Tertiary Output: Compilation Report
- Not registered — used for operational review
- Contains: stage-by-stage log, override decisions, policy resolution outcomes, any warnings

## Quality Requirements

1. All outputs must conform to their declared schemas
2. Compiled artifacts must include a valid checksum
3. Integration manifests must reference a valid host identifier
4. All outputs must be registered before the compilation run is marked successful

## Relationships

- [[Compiled Governance Artifact]] — the primary output concept
- [[Integration Manifest]] — the secondary output concept
- [[Compiler Artifacts Registry]] — registration target
- [[Authority Pack Compiler — Map]]
