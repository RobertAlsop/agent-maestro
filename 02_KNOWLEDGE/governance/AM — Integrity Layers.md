---
title: "AM — Integrity Layers"
type: governance
status: draft
authority_weight: 75
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — Scope]]"
  governs: []
  related:
    - "[[AM — Tool Conventions]]"
    - "[[AM — Roadmap]]"
tags:
  - governance
  - integrity
  - architecture
  - mechanical
  - semantic
---

# AM — Integrity Layers

## Purpose

Establish the architectural separation between the two integrity layers that maintain vault health: Mechanical Integrity and Semantic Integrity. Define the boundary between them and govern how they interact.

## Principle

A system's integrity depends on checks that are appropriate to the thing being checked. Mechanical problems — broken links, malformed YAML, missing files — have deterministic answers. Semantic problems — whether a concept has drifted, whether two notes are duplicates in meaning, whether a definition serves its purpose — require judgment.

Using judgment where determinism suffices is waste (Law 3 — Economy). Using determinism where judgment is required is dangerous — it creates false confidence. The separation is not a preference; it is a constraint derived from the nature of the problems themselves.

**Note on terminology:** The two layers described here — Mechanical Integrity and Semantic Integrity — describe *how* a check is enforced (deterministic tool vs. judgment-based agent). They are orthogonal to the six Constraint levels in Seed 3, which describe *what level of authority* a check operates at. A mechanical check can enforce any Constraint level (e.g., schema validation enforces Level 3; link resolution enforces Level 5). A semantic check can also operate at any Constraint level. The dimensions are independent.

---

## The Two Layers

### Mechanical Integrity

**Enforced by:** Deterministic tools (shell scripts, linters, validators).

**Domain:** Structure, syntax, and filesystem state. Things that have exactly one correct answer or can be checked against explicit rules.

**What it checks:**

- File existence — do required files and folders exist?
- Link resolution — do all internal references resolve to real targets?
- Syntax validity — does YAML parse? Are frontmatter fields present and within allowed values?
- Uniqueness constraints — are IDs unique? Are filenames unique where required?
- Structural orphans — are there files with no inbound links and no known structural role?
- Completeness — are there stubs, empty required files, or missing scaffold artifacts?
- Inventory — what exists, where, and in what state?

**What it produces:** Reports. Structured, machine-readable, timestamped findings. Never fixes. Never interpretations. Never recommendations.

**What it must never do:**

- Interpret what a note *means*
- Decide whether two concepts are semantically equivalent
- Judge whether content is correct, complete, or well-written
- Classify notes by meaning rather than by declared metadata
- Move, merge, split, or rewrite content based on inferred intent
- Make decisions that require reading comprehension beyond pattern matching

### Semantic Integrity

**Enforced by:** LLM agents operating within the role and authority framework.

**Domain:** Meaning, alignment, quality, and governance compliance. Things that require interpretation, judgment, or reasoning about intent.

**What it checks:**

- Alignment — does this artifact serve the purpose defined by the layer above it? (Foundations Audit Taxonomy: top-down)
- Conceptual integrity — has a definition drifted from its intended meaning? Are concepts coherent?
- Governance compliance — does this document follow the *spirit* of the rules, not just the letter?
- Viability — is this artifact earning its place? Would removing it create a real gap? (Foundations Audit Taxonomy: bottom-up)
- Completeness of thought — is the content substantive, or does it merely satisfy a template?
- Relationship correctness — are the `derives_from` and `governs` relationships semantically accurate, not just syntactically present?

**What it produces:** Audit findings with reasoning, proposals for change, escalation packages for human review.

**What it must never do:**

- Approve its own work (D6 — Separation of Powers)
- Make irreversible changes without human approval (D4 — Human Sovereignty)
- Skip the gate process for changes to canonical documents (Vault Rule 24)

---

## The Boundary

The boundary between layers is defined by a single test: **Can the check be expressed as a deterministic rule that produces the same result every time, regardless of who or what runs it?**

If yes → Mechanical Integrity. Build a tool.
If no → Semantic Integrity. Use an agent.

When the answer is ambiguous, the check belongs in the semantic layer. Mechanical integrity must be conservative — it flags only what it can prove. False negatives (missed problems) are acceptable at the mechanical layer because semantic checks will catch them. False positives (incorrect flags) erode trust in the entire system and must be avoided.

---

## How the Layers Interact

The layers operate in sequence, not in parallel. Mechanical integrity runs first. Its output feeds into semantic integrity as structured input.

```
Vault state
  ↓
Mechanical Integrity scan (scripts)
  ↓ produces: structured reports
Semantic Integrity assessment (agents)
  ↓ produces: findings, proposals, escalations
Human review (Level 3 decisions)
```

This reflects D5 (Governance Before Autonomy) applied to integrity: ground the semantic layer in verified structural reality before asking it to reason about meaning. An agent performing a semantic audit should consume the most recent mechanical integrity report as part of its input — it should not re-derive mechanical facts that scripts have already established. This prevents duplication and ensures the agent's judgment starts from a trustworthy foundation.

---

## Derivation from Foundations

This separation traces to three foundational elements:

**Law 3 — Economy.** Deterministic checks are cheaper, faster, and more reliable than LLM inference. Using an LLM to check whether YAML parses is waste. Every component must earn its place — and an LLM checking syntax is a component that hasn't earned its place when a script would suffice.

**D6 — Separation of Powers.** D6 requires that the entity proposing a change must not be the entity approving it, and the entity executing must not be the entity auditing. This document applies a stricter interpretation: detection, interpretation, and approval are held by three different actor types — tools, agents, and humans respectively. This stricter separation is not required by D6 alone, but it follows naturally when combined with Law 3 (tools are more economical for detection) and D1 (tools provide more deterministic control surfaces). The three principles together produce the two-layer model.

**D1 — Deterministic Control Surfaces.** Agent actions must be reproducible, traceable, and explainable. Mechanical integrity checks are the most deterministic control surface possible — same input always produces same output. This forms the trustworthy foundation on which less deterministic (but more capable) semantic checks can operate.

---

## When It Applies

When designing, building, or evaluating any integrity check, audit, validation tool, or maintenance process within the AM ecosystem. When deciding whether a check should be implemented as a tool or delegated to an agent. When scoping the responsibilities of tools vs. agents in any maintenance workflow.

## Related

- [[Agent Maestro — Foundations]] — the kernel this derives from (Law 3, D1, D6)
- [[Agent Maestro — Scope]] — AM's boundary definitions
- [[AM — Tool Conventions]] — how tools implementing Mechanical Integrity must be built
- [[AM — Roadmap]] — Wave 6 implements the first Mechanical Integrity tool suite
