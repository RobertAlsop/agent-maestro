---
type: system
note_class: architecture
domain: system_architecture
layer: systems
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Workspace Layer"
status: active
review_status: draft
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "[[Agent Maestro Layer Model]]"
  implements:
    - "[[Model Workspace Protocol]]"
    - "[[Model Workspace Protocol Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "Agent Constellation]]"
  uses:
    - "[[Compiled Governance Artifact]]"
    - "[[Knowledge Graph Layer]]"
    - "[[Structured Data Layer]]"
  produces: []
  - "[[Agent Infrastructure]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - system
  - workspace
  - infrastructure
hash: ""
---

# Workspace Layer

## Purpose

The Workspace Layer is the operational surface of the [[Agent Maestro Layer Model]]. It defines the physical file structure within which every agent execution operates, following the [[Model Workspace Protocol]].

## Responsibilities

- Provide a standardised directory structure for every agent execution
- Ensure agents have access to their compiled authority pack before execution begins
- Capture all agent outputs, logs, and escalation requests in inspectable locations
- Enable post-execution auditing by preserving workspace state

## Structure

Every agent workspace follows the MWP standard:

```
workspace/
   authority/       # Compiled authority pack for this agent
   agents/          # Agent definition and role contract
   stages/          # Current workflow stage contract
   references/      # Reference knowledge the agent needs
   artifacts/       # Working outputs produced by the agent
      logs/         # Execution audit trail
      escalations/  # Decisions exceeding agent authority
```

## Invariants

- Every workspace must contain a valid compiled governance artifact in `authority/` before the agent starts
- Agents must not access files outside their workspace unless explicitly permitted by their authority pack
- All outputs must be written to `artifacts/`
- Workspace state must be preserved after execution for audit purposes
- Execution logs must include: agent ID, start time, end time, actions taken, and outcome

## Integration Points

**From Authority Layer:** Compiled governance artifacts are copied into `authority/` during workspace setup.

**From Agent Runtime:** Agent definitions are copied into `agents/` during workspace setup.

**From Workflow Layer:** Stage contracts are copied into `stages/` during workspace setup.

**From Memory Architecture:** Reference knowledge may be drawn from the [[Knowledge Graph Layer]] or [[Structured Data Layer]] and placed in `references/`.

**To Structured Data Layer:** Execution logs and reports written to `artifacts/` feed back into the [[Structured Data Layer]] as operational records.

## Related Concepts

- [[Model Workspace Protocol]] — the protocol this layer implements
- [[Model Workspace Protocol Pattern]] — the design pattern
- [[Agent Maestro Layer Model]] — the four-layer architecture this belongs to
- [[Agent Infrastructure]] — broader infrastructure context
