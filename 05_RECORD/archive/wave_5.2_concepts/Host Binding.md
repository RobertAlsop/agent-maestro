---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Host Binding"

status: active
review_status: draft
version: 1

created_date: 2026-03-12
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements:
    - "[[Host Binding Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Compiled Governance Artifact]]"
  uses: []
  produces: []

  - "[[Authority Pack Compiler — Map]]"


source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - concept
  - agent_maestro
  - runtime

hash: ""
---

# Host Binding

## Definition

The resolved association between a [[Compiled Governance Artifact]] and a specific host runtime environment. Host Binding is the final stage of the compilation process — it produces the binding contract that tells a runtime how to load, apply, and enforce a compiled governance artifact.

## Boundaries

Host Binding is not the same as deployment (which is an operational process) or configuration (which is environment-specific). A host binding is a *governance-level declaration* that specifies which compiled artifact applies to which runtime, under what conditions. It is a formal artifact with its own schema.

## Purpose

Host Binding ensures that compiled governance is not just produced but successfully applied to a real runtime. Without binding, a compiled artifact has no connection to an operational agent environment. Binding closes the loop from design-time governance intent to runtime enforcement.

## Key Components

- **Host identifier** — the unique identifier for the target runtime
- **Artifact reference** — the compiled governance artifact being bound
- **Binding conditions** — conditions under which the binding is active
- **Integration contract** — the interface between the artifact and the runtime (see [[Integration Manifest]])

## Relationships

- [[Compiled Governance Artifact]] — what is being bound
- [[Integration Manifest]] — the contract produced by binding
- [[Host Bindings]] (system) — system note for the bindings layer
- [[Host Runtime Reference]] — reference for supported runtime environments
- [[Host Binding Pattern]] — the design pattern for implementing host bindings
- [[Authority Pack Compiler — Map]]
- [[Agent Maestro — Concepts Map]]
