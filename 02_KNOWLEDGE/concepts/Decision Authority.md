---
type: concept
note_class: knowledge
domain: ai_governance
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Decision Authority"
status: active
review_status: draft
version: 1
created_date: 2026-03-10
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
    - "Authority Architecture]]"
  implements:
    - "[[Decision-Execution Separation]]"
    - "[[Evidence Over Assumptions]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent]]"
  uses: []
  produces: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
hash: ""
---

# Decision Authority

## Definition

The bounded permission granted to an [[Agent|agent]] to select among options and commit to a course of action, within parameters defined by its [[Authority Pack]]. Decision authority governs what an agent may *choose* — which path to take, which classification to assign, which recommendation to surface — but not what it may *do* to external systems. That is [[Execution Authority]].

## Boundaries

Decision authority is explicitly separated from [[Execution Authority]]. An agent may hold broad decision authority (e.g., triage all incoming support tickets) while holding narrow execution authority (e.g., may only update ticket metadata, not issue refunds). This separation is formalised in [[Decision-Execution Separation]] and is a core safety principle of Authority Architecture]].

## Purpose

Constraining what an agent may decide — not just what it may do — prevents agents from committing the organisation to courses of action outside their competence or governance scope. Decision authority makes the commitment boundary explicit: beyond this scope, the agent must escalate. See [[Human Escalation Pattern]].

## Key Components

- **Permitted decision scope** — the classes of choices the agent may make (e.g., classify, prioritise, route, recommend)
- **Escalation thresholds** — conditions under which the agent must defer to a human or higher-authority agent (e.g., ambiguous inputs, high-stakes outcomes, novel situations)
- **Evidence requirements** — what rationale and context must be recorded for each decision to maintain auditability. See [[Evidence Over Assumptions]]

## Example

A triage agent may decide which support tier a ticket belongs to (permitted scope), but must escalate to a human when the ticket involves a legal complaint (escalation threshold), and must log the classification rationale for every ticket processed (evidence requirement).

## Relationships

- [[Execution Authority]] — the complementary permission governing agent actions
- [[Authority Pack]] — the governance contract that specifies an agent's decision authority
- [[Authority Architecture Map]]
- [[Agent Maestro — Concepts Map]]
