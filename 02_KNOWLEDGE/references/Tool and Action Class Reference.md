---
id: REF.tool_action_class
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
  - tools
  - actions

hash: ""
---

# Tool and Action Class Reference

## Purpose

Canonical classification of tool types and action classes used in [[Authority Pack]] governance declarations. Authority packs reference these classes to specify which tools and actions are allowed, restricted, or prohibited for governed agents.

## Context

When an authority pack declares `governed_actions` in section 04, it uses these standardised classes rather than listing individual tools. This ensures that governance declarations remain stable even as specific tool implementations change.

## Tool Classes

| Class | Code | Description |
|---|---|---|
| Data Read | `TOOL.READ` | Reading from data sources (databases, files, APIs) |
| Data Write | `TOOL.WRITE` | Writing to data sources |
| Data Delete | `TOOL.DELETE` | Deleting records or files |
| External API | `TOOL.API.EXT` | Calls to external (third-party) APIs |
| Internal API | `TOOL.API.INT` | Calls to internal organisation APIs |
| Communication | `TOOL.COMM` | Sending messages, emails, notifications |
| Compute | `TOOL.COMPUTE` | Running computations, analysis, or inference |
| Code Execution | `TOOL.EXEC` | Executing code or scripts |
| Human Interface | `TOOL.HUMAN` | Presenting information to or requesting input from humans |

## Action Classes

| Class | Code | Description |
|---|---|---|
| Autonomous Decision | `ACT.DECIDE.AUTO` | Decision made without human review |
| Supervised Decision | `ACT.DECIDE.SUP` | Decision requiring supervisor review |
| Human-Approved Decision | `ACT.DECIDE.HAR` | Decision requiring explicit human approval |
| Execute Workflow | `ACT.WF` | Initiating or advancing a workflow |
| Delegate | `ACT.DELEGATE` | Assigning a task to another agent |
| Escalate | `ACT.ESCALATE` | Triggering an escalation event |
| Log Evidence | `ACT.LOG` | Recording evidence for auditability |

## Related Concepts

- [[Authority Pack Grammar]] — where these classes are used in section 04
- [[Execution Authority]] — the authority type governing action classes
- [[Governance Schemas Reference]] — the schema that formalises pack section 04
- [[Agent Maestro — Governance Map]]
