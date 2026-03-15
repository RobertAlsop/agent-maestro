---
type: system
note_class: architecture
domain: ai_governance
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Integration Manifest"

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
  - runtime

hash: ""
---

# Integration Manifest

## Purpose

The Integration Manifest is the binding contract produced by the [[Host Bindings]] stage of compilation. It declares exactly how a [[Compiled Governance Artifact]] should be loaded, enforced, and monitored by a specific host runtime environment.

## Context

An Integration Manifest closes the loop between compiled governance and runtime enforcement. Without it, a compiled artifact is a governance document; with it, the artifact becomes a deployed governance contract.

## Structure

Each Integration Manifest contains:

| Field | Description |
|---|---|
| `manifest_id` | Stable unique identifier |
| `artifact_ref` | ID and version of the compiled artifact being bound |
| `host_id` | Target runtime identifier (from [[Host Runtime Reference]]) |
| `binding_version` | Version of this binding |
| `enforcement_points` | Map of rule sections to runtime enforcement points |
| `conditions` | Activation conditions (e.g. agent class, context) |
| `monitoring_hooks` | Runtime monitoring integration points |
| `escalation_routing` | Escalation endpoint configuration |

## Lifecycle

1. Produced by [[Host Bindings]] during compilation
2. Registered alongside the compiled artifact in [[Compiler Artifacts Registry]]
3. Loaded by the runtime host during agent initialisation
4. Remains active until the compiled artifact is superseded

## Failure Modes
- Runtime cannot parse the manifest → deployment blocked; flag for review
- Enforcement point not available in target runtime → binding failure; see [[Compile Failure Semantics]]

## Relationships

- [[Host Binding]] (concept) — the concept this artifact implements
- [[Compiled Governance Artifact]] — the artifact this manifest binds
- [[Host Bindings]] (system) — the system that produces manifests
- [[Compiler Artifact Schemas Reference]] — the schema this manifest must conform to
- [[Authority Pack Compiler — Map]]
