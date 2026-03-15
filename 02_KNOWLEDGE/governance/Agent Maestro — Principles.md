---
id: GOV.agent_maestro.principles
type: principles
note_class: doctrine
domain: governance
layer: governance
scope: null

canonical: true
authority_weight: 90
resolution_basis: canonical
schema_version: 2

status: active
review_status: draft
version: 2

created: 2026-03-10
updated: 2026-03-14
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

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - governance
  - principles

hash: ""
---

# Agent Maestro — Principles

## Purpose

Twelve principles that govern every Agent Maestro system design decision.

## Principle

These principles are constraints, not suggestions. They define the shape of reliable intelligent systems.

## Implications

- Systems that violate these principles are fragile by design.
- Each principle has a corresponding [[02_KNOWLEDGE/patterns/|pattern note]] that operationalises it.

## Principles by Tier

The twelve principles are organised into three tiers. Tier 1 is non-negotiable — apply these before anything else. Tier 2 guides system design. Tier 3 governs operational evolution and scaling.

### Tier 1 — Foundation

Apply these first. They are non-negotiable prerequisites for any Agent Maestro system.

| # | Principle | Why it's foundational |
|---|---|---|
| 1 | [[Governance Before Autonomy]] | Without this, nothing else in the framework applies. Govern before you scale. |
| 2 | **Authority Over Intelligence** | The core thesis of Agent Maestro. [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] matters more than the model. |
| 7 | [[Human Escalation Pattern]] | Safety boundary. Humans must always hold final authority on irreversible actions. |
| 4 | **Transparency by Design** | You cannot govern what you cannot observe. All system actions must be observable and auditable. |

### Tier 2 — Architecture

Apply these when designing agent systems, memory layers, and authority structures.

| # | Principle | When it applies |
|---|---|---|
| 3 | [[Deterministic Control Surfaces]] | When defining agent actions and outputs. Actions must be reproducible, traceable, explainable. |
| 5 | **Intelligence Through Constraints** | When scoping agent authority. Constraints create reliability, not freedom. |
| 6 | [[Three-Layer Memory Model]] | When designing memory and knowledge systems. Three distinct layers, each with clear responsibilities. The architectural principle is three layers (Knowledge Graph, Vector Memory, Structured Data) even when fewer are currently active. See [[Memory Model]] for implementation status. |
| 8 | **Composable Architecture** | When structuring multi-agent systems. Systems must remain modular and reusable. |

### Tier 3 — Evolution

Apply these when operating, evaluating, and scaling existing systems.

| # | Principle | When it applies |
|---|---|---|
| 9 | [[Evidence Over Assumptions]] | When evaluating system behaviour. Behaviour validated through events and outcomes. |
| 10 | **Real Systems First** | When validating designs. Theory validated in real operational environments only. |
| 11 | [[Controlled Evolution Pattern]] | When upgrading or expanding systems. Evolution through graduated experiments, never jumps. |
| 12 | [[Anti-Agent-Sprawl Pattern]] | When scaling the number of agents. Every agent must have defined purpose, authority, and outcomes. |

## Principles Index (Flat Reference)

1. [[Governance Before Autonomy]] — Govern before you scale.
2. **Authority Over Intelligence** — [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] matters more than the model.
3. [[Deterministic Control Surfaces]] — Actions must be reproducible, traceable, explainable.
4. **Transparency by Design** — All system actions must be observable and auditable.
5. **Intelligence Through Constraints** — Constraints create reliability, not freedom.
6. [[Three-Layer Memory Model]] — Three distinct knowledge layers, each with clear responsibilities.
7. [[Human Escalation Pattern]] — Humans must always hold final authority on irreversible actions.
8. **Composable Architecture** — Systems must remain modular and reusable.
9. [[Evidence Over Assumptions]] — Behaviour validated through events and outcomes.
10. **Real Systems First** — Theory validated in real operational environments only.
11. [[Controlled Evolution Pattern]] — Evolution through graduated experiments, never jumps.
12. [[Anti-Agent-Sprawl Pattern]] — Every agent must have defined purpose, authority, and outcomes.

## When It Applies

All system design, architecture reviews, and agent deployment decisions.

## Related

- [[Agent Maestro — North Star]]
- [[Agent Maestro — Modes]]
- [[Agent Maestro — Strategy]]
- [[Agent Maestro — Governance Map]]
