---
id: REF.host_runtime
type: reference
note_class: reference
domain: ai_governance
layer: knowledge
scope: null

canonical: false
authority_weight: 90
resolution_basis: authority_weight
schema_version: 2

status: draft
review_status: draft
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

source_type: imported
supersedes: []
superseded_by: []

tags:
  - reference
  - runtime
  - host

hash: ""
---

# Host Runtime Reference

## Purpose

Reference catalogue of supported host runtime environments for compiled governance artifact binding. Used during the [[Host Binding Pattern|host binding]] stage of compilation.

## Context

A [[Host Binding]] associates a [[Compiled Governance Artifact]] with a specific runtime environment. This reference defines what runtime environments exist, their identifiers, and their capability requirements for loading compiled governance artifacts.

## Runtime Categories

### Conversational Agent Runtimes
Environments where agents operate through conversational interfaces.
- Must support: rule loading, escalation routing, evidence capture
- Identifier prefix: `RT.CONV.*`

### Workflow Agent Runtimes
Environments where agents execute structured workflows.
- Must support: state management, task delegation, timeout handling
- Identifier prefix: `RT.WF.*`

### Autonomous Agent Runtimes
Long-running environments with persistent agent state.
- Must support: full governance artifact loading, memory integration, audit logging
- Identifier prefix: `RT.AUTO.*`

## Runtime Capability Matrix

| Capability | Conversational | Workflow | Autonomous |
|---|---|---|---|
| Rule enforcement | Required | Required | Required |
| Escalation routing | Required | Required | Required |
| Evidence capture | Required | Required | Required |
| State persistence | Optional | Required | Required |
| Memory integration | Optional | Optional | Required |

## Related Concepts

- [[Host Binding]] — the concept of binding governance to a runtime
- [[Host Bindings]] (system) — the system managing bindings
- [[Integration Manifest]] — the binding contract produced
- [[Host Binding Pattern]] — the implementation pattern
- [[Authority Pack Compiler — Map]]
