---
type: system
note_class: architecture
domain: ai_governance
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Compiled Governance Artifacts"

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
  - governance

hash: ""
---

# Compiled Governance Artifacts

## Purpose

System note for the compiled governance artifacts layer — the set of all [[Compiled Governance Artifact|Compiled Governance Artifacts]] produced by the Authority Pack Compiler]] and deployed to agent runtime environments.

## Context

This is the system-level view of compiled artifacts as a managed collection. Individual artifacts are registered in [[Compiler Artifacts Registry]] and bound to hosts via [[Integration Manifest|Integration Manifests]].

## Responsibilities

### Outputs
- Valid, deployed governance artifacts in runtime environments
- Audit trail of all compilation events

### Internal Components
- Active compiled artifacts (registered in [[Compiler Artifacts Registry]])
- Superseded artifacts (retained for auditability)
- Compilation history

### Lifecycle

```
Source Packs → Compilation → Compiled Artifact (draft)
→ Host Binding → Compiled Artifact (bound)
→ Deployment → Compiled Artifact (active)
→ Supersession → Compiled Artifact (superseded, retained)
```

### Failure Modes
- Deployed artifact fails runtime validation → halt affected agents; trigger [[Human Escalation]]
- Artifact checksum mismatch → treat as governance integrity failure; halt immediately

## Relationships

- [[Compiled Governance Artifact]] (concept)
- [[Compiler Artifacts Registry]] — the registry tracking all artifacts
- [[Integration Manifest]] — the binding contracts associated with artifacts
- [[Authority Pack Compiler — Map]]
