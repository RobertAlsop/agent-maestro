---
schema_version: 2
title: "Agent Maestro — Foundations"
type: foundations
note_class: doctrine
domain: governance
layer: governance
authority_weight: 95
resolution_basis: canonical
canonical: true
status: active
review_status: approved
version: 3
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Foundational Kernel]]"
    - "[[Derived Principles]]"
    - "[[Audit Taxonomy]]"
  part_of: []
  implements:
    - "[[Agent Maestro — North Star]]"
  governs:
    - "[[Agent Maestro — Principles]]"
    - "[[Agent Maestro — Vault Rules]]"
    - "[[Agent Maestro — Modes]]"
    - "[[Agent Maestro — Scope]]"
    - "[[Agent Maestro — Strategy]]"
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - governance
  - foundations
  - kernel
  - principles
  - canonical
hash: ""
---

# Agent Maestro — Foundations

Agent Maestro is the discipline of designing, governing, and evolving operational intelligence systems. This document defines its irreducible kernel — the foundational elements from which all other governance, architecture, and operational decisions are derived.

For extended rationale and framework reconciliation, see [[AM — Wave 5 — Treatise on Core Principles]].

---

## The Kernel

### Three Seeds

Seeds are the mechanics of any operational intelligence system.

**Seed 1 — Process**

Every operation follows the Irreducible Loop:

```
perception → interpretation → decision → action → memory → feedback
```

Between interpretation and decision, there is always a validation gate: no decision proceeds without checking against the Constraint hierarchy. The loop runs at every level of abstraction — a build session, an agent execution, a governance review, a single document's lifecycle.

**Seed 2 — Structure**

Every system component must have or serve seven primitives:

| Primitive | Question it answers |
|-----------|-------------------|
| State | What is true right now? |
| Goal | What is this trying to achieve? |
| Policy | What is allowed, forbidden, or preferred? |
| Memory | What from the past informs the present? |
| Tools | What actions can be taken? |
| Control | Who decides, who checks, who can stop? |
| Feedback | How do we know if the action worked? |

**Seed 3 — Constraint**

Every action must pass through an authority hierarchy. No level may bypass the one above it:

| Level | What it defines |
|-------|----------------|
| 1. Design intent | Why does this system exist? |
| 2. Definition | What are the named things? |
| 3. Schema | What shape must they take? |
| 4. Validation | Does this instance conform? |
| 5. Routing | Where does this action go? |
| 6. Execution | The action itself |

Stated as a chain: no execution without routing. No routing without validation. No validation without schema. No schema without definition. No definition without design intent.

### One Meta-Principle

**Fractal Design**

Every layer of Agent Maestro is built from the same fundamental principles, applied at different levels of abstraction. The audit that checks a single note is the same audit (parameterized) that checks an entire vault. The build session protocol used by a human and Claude is the same protocol an autonomous constellation follows.

Fractal Design implies composability (same parts recombine at each level), reflexivity (the system can apply its patterns to itself), and portability (patterns proven at one level transfer to others).

### Three Laws

Laws are universal constraints. Violating a law means the system is broken.

**Law 1 — Direction of Authority**
Purpose descends; accountability ascends. Every component's purpose is defined by and in service to the layer above it. At the top, the North Star declares the human's intent. Accountability — reporting, logging, escalation — flows upward to the human.

**Law 2 — Action Properties**
All actions must be verifiable, reversible, and accountable. No invisible mutations. No permanent changes without authorization. No anonymous modifications.

**Law 3 — Economy**
Only what is necessary. Every component must earn its place. If it can be removed without loss of function or understanding, it should be removed.

---

## Derived Principles

Six principles operationalize the kernel for Agent Maestro. Each is explicitly traced to the foundational element it derives from.

**D1. Deterministic Control Surfaces**
*Derives from: Seed 2 (Control) + Law 2 (verifiable)*
Agent actions must be reproducible, traceable, and explainable. Control is implemented through deterministic interfaces.

**D2. Three-Layer Memory Model**
*Derives from: Seed 2 (Memory)*
Knowledge is organized in three layers: Knowledge Graph (structured relationships), Vector Memory (semantic search), Structured Data (CSV, registry). Each layer has distinct responsibilities.

**D3. Controlled Evolution**
*Derives from: Seed 1 (feedback) + Seed 3 (Constraint)*
System changes proceed through graduated experiments within governance. Evolution is a governed process, not an uncontrolled mutation.

**D4. Human Sovereignty**
*Derives from: Law 1 (purpose descends)*
Humans hold final authority at the top of every authority chain. No autonomous action may be irreversible without human approval. Escalation to human is always available.

**D5. Governance Before Autonomy**
*Derives from: Seed 3 (Constraint) + Seed 1 (validation gate)*
No capability is deployed without governance in place first. Govern, then operate, then scale. Never the reverse.

**D6. Separation of Powers**
*Derives from: Seed 3 (Constraint) + Law 1 (Direction of Authority)*
Different functions within the authority hierarchy must be held by different actors. The entity that proposes a change must not be the entity that approves it. The entity that executes must not be the entity that audits. This prevents self-referential governance loops and ensures that accountability (Law 1) has somewhere to ascend to.

---

## The Hierarchy

```
Kernel (7 elements)          → What is always true
  ↓
Derived Principles (6)       → How the kernel applies to Agent Maestro
  ↓
Operational Patterns (many)  → Templates, authority packs, pipelines, audits
```

Purpose descends through the levels. Each level is the minimum viable expression of the one above it. The same structure appears at every abstraction level in the vault.

---

## Audit Taxonomy

Three audit types check any system component at any level of abstraction:

| Audit | Direction | Question |
|-------|-----------|----------|
| **Alignment** | Top-down | Does this serve what's above it? |
| **Integrity** | Horizontal | Is this internally sound and correctly connected? |
| **Viability** | Bottom-up | Is this earning its place? |

The adversarial method (assume it's wrong, try to prove it) is a lens applied within any of the three types, not a separate type.

---

## Relationship to Other Governance Documents

This document is the highest-authority governance document in Agent Maestro (authority_weight: 95). All other governance documents — Principles, Vault Rules, Modes, Scope, Strategy — derive from and must align with these foundations. The existing [[Agent Maestro — Principles]] document is superseded in authority but retained as a historical reference until the derived principles above are fully integrated across the vault.
