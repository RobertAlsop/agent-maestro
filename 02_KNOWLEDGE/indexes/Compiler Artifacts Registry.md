---
type: registry
note_class: registry
domain: ai_governance
layer: registry

canonical: true
authority_weight: 95
resolution_basis: canonical
schema_version: 2
title: "Compiler Artifacts Registry"

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


  - "[[Agent Maestro — Governance Artifacts Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - registry
  - compiler
  - governance

hash: ""
---

# Compiler Artifacts Registry

## Purpose

Authoritative registry of all [[Compiled Governance Artifact|Compiled Governance Artifacts]] produced by the 01_CAPTURE/inbox/Authority Pack Compiler]]. Every compiled artifact must be registered here before it can be deployed to a runtime.

## Context

Registries resolve. This registry enables any system to look up a compiled artifact by ID and retrieve its source packs, compilation metadata, and host binding.

## Structure

Each entry records:

| Field | Description |
|---|---|
| `artifact_id` | Stable unique identifier |
| `artifact_name` | Human display name |
| `source_packs` | List of input pack IDs and versions |
| `compiled_at` | ISO 8601 timestamp |
| `compiler_version` | Compiler version used |
| `host_binding` | Bound host runtime identifier |
| `manifest_id` | Associated [[Integration Manifest]] ID |
| `status` | active / superseded / failed |
| `checksum` | Deterministic hash |

## Registered Artifacts

*(No artifacts compiled yet — registry is initialised and ready.)*

## Entry Rules

1. Only the compiler writes to this registry
2. Artifacts are never deleted — superseded artifacts are marked `superseded`
3. Every artifact must have a valid host binding before status becomes `active`
4. Checksum must be validated on every deployment

## Related

- [[Authority Pack Compiler — Map]]
- [[Pack Version Registry]] — versions of source packs used in compilation
- [[Authority Pack Registry]] — the source packs
- [[Agent Maestro — Governance Artifacts Map]]
