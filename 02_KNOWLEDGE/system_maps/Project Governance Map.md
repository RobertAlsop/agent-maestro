---
type: map
note_class: navigation
domain: agent_maestro
layer: maps
canonical: true
authority_weight: 85
resolution_basis: authority_weight
schema_version: 2
title: "Project Governance Map"
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
  - "[[Agent Maestro — Governance Map]]"
  - "[[Authority Architecture Map]]"
  - "[[Agent Maestro — Governance Artifacts Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - map
  - navigation
  - governance
  - project
hash: ""
---

# MAP.project.governance

> Governance reference map for use inside project contexts. Shows governance boundaries, applicable authority packs, escalation paths, and operational constraints.

---

## Purpose

This map is embedded in project notes to make governance boundaries explicit. It answers: what rules apply here, who has authority, what can be escalated, and what constraints are in force.

---

## Governance Boundaries

Projects operate within governance boundaries defined by:

- [[Agent Maestro — Scope]] — what Agent Maestro covers
- [[Agent Maestro — Principles]] — the non-negotiable principles
- [[Agent Maestro — Vault Rules]] — vault-level structural rules
- [[Governance Before Autonomy]] — no agent operates without governance

---

## Applicable Authority Packs

Each project that deploys or involves agents must identify its applicable authority packs. See:

- [[Authority Packs Index]] — full list of available packs
- [[Authority Pack Registry]] — registry-resolvable pack objects
- [[Pack Manifest]] — canonical governance artifact defining pack composition

---

## Escalation Paths

Escalation is governed by:

- [[Human Escalation Pattern]] — when and how to escalate to humans
- [[Escalation Classes Reference]] — escalation class taxonomy
- [[Decision Authority]] — what decisions are within scope vs. require escalation

---

## Operational Constraints

- [[Deterministic Control Surfaces]] — control points must be explicit
- [[Evidence Over Assumptions]] — decisions require logged evidence
- [[Decision-Execution Separation]] — deciding and acting are separate authorities
- [[Pack Override Rules]] — override rules must be declared and versioned

---

## Compiled Governance in Force

For projects using compiled governance:

- [[Compiled Governance Artifact]] — what compilation produces
- [[Compiler Artifacts Registry]] — registry of active compiled artifacts
- [[Compile Failure Semantics]] — what happens when compilation fails

---

## Related

- [[Agent Maestro — Governance Map]]
- [[Agent Maestro — Governance Artifacts Map]]
- [[Agent Maestro — Practice Map]]
- [[Agent Maestro — Navigation Map]]
