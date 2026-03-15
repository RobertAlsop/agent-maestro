---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Host Binding Pattern"

status: active
review_status: draft
version: 1

created_date: 2026-03-12
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Host Binding]]"
  uses: []
  produces: []

  - "[[Authority Pack Compiler — Map]]"


source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - pattern
  - agent_maestro
  - runtime

hash: ""
---

# Host Binding Pattern

## Summary

Every [[Compiled Governance Artifact]] must be explicitly bound to a specific target host runtime before it can be enforced. Binding produces an [[Integration Manifest]] that declares the contract between the artifact and the runtime. Governance without binding is undeployed governance.

## Problem

A compiled governance artifact is generic until it is bound to a specific runtime environment. Without binding, the artifact cannot be loaded, enforced, or monitored by a runtime host.

## Solution

After compilation, run a binding step that: identifies the target runtime from the [[Host Runtime Reference]], maps artifact sections to runtime enforcement points, declares any runtime-specific conditions, and produces an [[Integration Manifest]] as the binding contract.

## Rules

1. Every compiled artifact must have exactly one primary host binding
2. Binding declarations must include the host identifier and artifact version
3. If a runtime changes, rebinding is required
4. Integration manifests must be registered alongside their compiled artifacts

## Relationships

- [[Host Binding]] (concept) — the concept this pattern implements
- [[Host Bindings]] (system) — the system layer for binding management
- [[Integration Manifest]] — the artifact produced by binding
- [[Compiled Governance Artifact]] — the input being bound
- [[Host Runtime Reference]] — the reference for supported runtimes
- [[Governance Compilation Pattern]] — the broader compilation pattern this is part of
- [[Authority Pack Compiler — Map]]
