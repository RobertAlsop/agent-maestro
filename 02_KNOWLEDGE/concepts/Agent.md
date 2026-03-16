---
title: "Agent"
type: concept
status: active
authority_weight: 55
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related:
    - "[[Role — Worker]]"
    - "[[Role — Reviewer]]"
tags: [concept, agent, foundational]
---

# Agent

## Purpose

Define what an agent is in Agent Maestro — the fundamental unit of execution within the system.

## Definition

An agent is an on-demand instantiation of a model (or human) operating within a defined role, equipped with a set of skills, and scoped to a specific context. Agents are not permanent entities. They are created when a task requires execution and dissolved when the task is complete.

## Composition

Every agent instantiation has four components:

1. **Model** — The LLM or human performing the work
2. **Role** — The authority boundary ([[Role — Worker]] or [[Role — Reviewer]]) that defines what the agent may and must not do
3. **Skills** — The capabilities loaded for this instantiation (subset of the 7 core skills, determined by role)
4. **Context** — The current pipeline stage, task, and relevant artifacts

## Lifecycle

```
Instantiate → Execute → Record → Dissolve
```

An agent is instantiated with a role, skills, and context. It executes its task within the authority boundaries of its role. It records what it did (or hands off to the [[Skill — Summarize|Summarize]] skill). It dissolves — there is no persistent agent state between instantiations.

## Key Properties

- **Agents are not permanent.** There is no standing "Triage Agent" or "Audit Agent." There is a model instantiated with the Triage skill when triage is needed.
- **The same model can play different roles** — but never for the same work in the same context (D6, Separation of Powers).
- **A human is an agent** when operating within the system. When Rob builds, he is a Worker. When Rob approves, he is a Reviewer (Level 3).
- **Authority derives from the role, not the model.** A more capable model in a Worker role has less authority than a less capable model in a Reviewer role.

## Traceability

This concept operationalizes Seed 2 (Structure) — specifically the Control primitive ("who decides, who checks, who can stop?") and the Tools primitive ("what actions can be taken?"). The agent is how these primitives are instantiated at runtime.

## Related

- [[Agent Maestro — Foundations]]
- [[Role — Worker]]
- [[Role — Reviewer]]
