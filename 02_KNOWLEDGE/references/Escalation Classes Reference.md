---
id: REF.escalation_classes
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

map: "[[Agent Maestro — Governance Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: imported
supersedes: []
superseded_by: []

tags:
  - reference
  - escalation
  - governance

hash: ""
---

# Escalation Classes Reference

## Purpose

Canonical classification of escalation types in Agent Maestro. Used by authority packs to declare escalation conditions and by runtime systems to route escalations to the correct recipient.

## Context

Every escalation event in a governed agent system must belong to a declared escalation class. Classes determine routing, response requirements, and SLA expectations.

## Escalation Classes

| Class | Code | Trigger | Default Routing |
|---|---|---|---|
| Authority Exceeded | `ESC.AUTH` | Decision requires out-of-scope authority | Supervisor → Executive |
| Evidence Gap | `ESC.EVID` | Required evidence cannot be obtained | Supervisor |
| Policy Conflict | `ESC.POL` | Conflicting rules without resolution path | Executive |
| Human Approval Required | `ESC.HAR` | Pack explicitly requires human sign-off | Designated human |
| Unhandled Condition | `ESC.UHC` | Situation not covered by any rule | Executive → Human |
| Safety Threshold | `ESC.SAFE` | Action would breach a safety constraint | Human (immediate) |
| Timeout | `ESC.TIME` | Agent exceeded time limit without resolution | Supervisor |

## Usage in Authority Packs

Escalation classes are declared in section `06_control_gates` and `12_failure_semantics` of an [[Authority Pack]] using the `escalation_class` field.

## Related Concepts

- [[Human Escalation]] — the concept these classes classify
- [[Human Escalation Pattern]] — implementation pattern
- [[Decision Authority]] — the authority boundary that triggers escalation
- [[Agent Maestro — Governance Map]]
