---
type: reference
note_class: reference
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 90
resolution_basis: authority_weight
schema_version: 2
title: "Compiler Artifact Schemas Reference"

status: draft
review_status: draft
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



source_type: imported
supersedes: []
superseded_by: []

tags:
  - reference
  - schemas
  - compiler

hash: ""
---

# Compiler Artifact Schemas Reference

## Purpose

Formal schema definitions for all artifact types produced by the [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]]. This reference is the authoritative source for what a valid [[Compiled Governance Artifact]] must contain.

## Context

The compiler validates its outputs against these schemas. If an output does not conform to the appropriate schema, compilation fails. This reference must be updated when new artifact types are introduced.

## Schemas

### Compiled Governance Artifact Schema

Required fields:
- `artifact_id` — unique identifier (stable, never reused)
- `source_packs` — list of input packs with versions
- `compiled_at` — ISO 8601 timestamp
- `compiler_version` — version of compiler used
- `inheritance_graph` — resolved inheritance structure
- `resolved_rules` — flattened rule set after override resolution
- `host_binding` — reference to [[Integration Manifest]]
- `checksum` — deterministic hash of resolved_rules

### Integration Manifest Schema

Required fields:
- `manifest_id` — unique identifier
- `artifact_ref` — compiled artifact this manifest binds
- `host_id` — target runtime identifier
- `binding_version` — version of this binding
- `enforcement_points` — runtime enforcement map
- `conditions` — activation conditions

## Related Concepts

- [[Compiled Governance Artifact]] — the output type described by these schemas
- [[Integration Manifest]] — the binding artifact schema
- [[Governance Schemas Reference]] — governance artifact schemas (broader)
- [[Authority Pack Compiler — Map]]
