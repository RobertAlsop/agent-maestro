---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Execution Authority"
status: active
review_status: draft
version: 1
created_date: 2026-03-10
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]"
  implements:
    - "[[Decision-Execution Separation]]"
    - "[[Evidence Over Assumptions]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
  uses:
    - "[[Context Pack]]"
    - "[[Decision Authority]]"
  produces: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
hash: ""
---

# Execution Authority

## Definition

The bounded permission granted to an [[Agent|agent]] to take actions in the world — writing, sending, modifying, or triggering external systems. Execution authority governs what an agent may *do*, as distinct from what it may *decide* (see [[Decision Authority]]). It defines the blast radius of an agent: the set of real-world effects the agent is permitted to cause.

## Boundaries

Execution authority does not include the permission to choose a course of action — that is [[Decision Authority]]. An agent may decide to recommend a refund (decision) but lack the authority to issue it (execution). This separation is formalised in [[Decision-Execution Separation]].

Execution authority also does not cover internal computation or reasoning. An agent may reason freely within its [[Context Pack]]; execution authority applies only to actions with observable effects on external systems.

## Purpose

Constraining execution authority is the primary mechanism for making [[Agent Systems]] safe to scale. The narrower the execution boundary, the smaller the damage from any single agent failure. Per [[Agent Maestro — Principles]], irreversible actions require the tightest constraints and the strongest evidence requirements.

## Key Components

- **Permitted action classes** — the specific operations an agent may perform (e.g., read a database, update a record, send a notification, trigger a downstream system)
- **Irreversibility thresholds** — actions above a defined impact level that require human approval before execution. See [[Human Escalation Pattern]]
- **Evidence requirements** — the audit trail that must be recorded for each executed action, per [[Evidence Over Assumptions]]

## Example

A data-enrichment agent may read from a CRM and write updated contact fields (permitted actions), but may not delete records or modify billing information (outside execution scope), and must log every field change with a timestamp and source reference (evidence requirement).

## Relationships

- [[Decision Authority]] — the complementary permission governing agent choices
- [[Authority Pack]] — the governance contract that specifies an agent's execution authority
- [[Human Escalation Pattern]] — the pattern invoked when execution authority is insufficient
- [[Authority Architecture Map]]
- [[Agent Maestro — Concepts Map]]
