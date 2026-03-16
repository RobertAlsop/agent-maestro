---
title: "AM — Roadmap"
type: governance
status: active
authority_weight: 75
schema_version: 3
created: "2026-03-16"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Strategy]]"
    - "[[Agent Maestro — North Star]]"
  governs: []
  related:
    - "[[AM — Future Waves Register]]"
    - "[[Agent Maestro — Scope]]"
tags: [roadmap, strategy, governance]
---

# AM — Roadmap

## Purpose

Define the strategic arc of Agent Maestro's evolution — where we are, where we're going, and what each milestone proves. This roadmap is the committed plan. It derives from the [[Agent Maestro — Strategy|Strategy]] document's four stages and is the authoritative reference for what AM is working toward.

## Principle

The roadmap follows D3 (Controlled Evolution) — each wave proves the one before it. Stages cannot be skipped. The roadmap is deliberately high-level; detailed wave plans live in proposals (see [[AM — Future Waves Register]] for the backlog of uncommitted ideas).

## Current Position

**Stage 1 — Self-Governance.** AM governs its own vault. The pipeline works. Governance is solid. The patterns are being discovered and codified through practice. Wave 6 (Mechanical Integrity) is complete. Wave 7 (Scheduled Execution) is next.

---

## Stage 1 — Self-Governance

*Proof: AM can govern itself reliably.*

AM's vault must be a working demonstration of the principles it teaches. This means the governance is sound, the pipeline flows, and the system can detect and maintain its own integrity — not just as a static knowledge architecture, but as an operational system.

### Wave 5 — Consolidation (v0.5.0) ✓

**Question:** Does AM carry anything it doesn't need?

Delivered the v1.0.0 structural redesign. Vault consolidated from 100+ files to ~30 active. Schema v3 adopted. Governance hierarchy established. 7 skills and 2 roles defined. Archive organized. Pipeline folders operational.

### Wave 5.1 — Design Session ✓

**Question:** What does v1.0.0 look like?

Produced the Design Blueprint. Collaborative human-AI design process proved effective. Fractal insight validated. Law 3 (Economy) confirmed as the sharpest design tool.

### Wave 5.2 — Pipeline Hardening ✓

**Question:** Is every joint finished?

Governance documents reviewed and tightened. Pipeline folders audited. Concepts consolidated (39→5). Proposal lifecycle codified. Roadmap and register created. Universal Workflow documented. See [[Proposal — Wave 5.2 Pipeline Hardening]] for the full contract.

### Wave 6 — Mechanical Integrity ✓

**Question:** Can AM detect its own structural problems?

Delivered the vault-maintenance tool suite: seven detection tools (structure, YAML, broken links, orphans, stubs, naming, inventory) plus orchestrator. Config-driven, portable, read-only. First health report ran and found real issues — confirming the tools work. Established [[AM — Integrity Layers]] (mechanical/semantic boundary) and [[AM — Tool Conventions]] as governance. See [[Proposal — Wave 6 Mechanical Integrity]] for the full contract.

### Wave 7 — Scheduled Execution (current)

**Question:** Can AM actually *run* things?

Give AM autonomous operation via launchd scheduling of the integrity suite. Date-stamped reports land in `05_RECORD/reports/` daily without human initiation. Optionally, a local LLM (Ollama/llama3.2) summarises findings and macOS notifications alert on problems. Local-first stack — no external API dependencies. See [[Proposal — Wave 7 Scheduled Execution]] for the full contract.

### Wave 8 — Self-Observation & Autonomy

**Question:** Can AM run on itself without a human starting every session?

Instrument the pipeline with observation data. Implement scheduled maintenance that runs autonomously. Build the self-assessment loop: observe → identify issues → propose fixes → gate → execute (within authority) or escalate. Define the agent responsibility architecture to prevent collision.

**Stage 1 Exit Criteria:**
- The vault detects its own structural problems automatically
- A task can flow through all 6 pipeline stages with appropriate automation and gates
- AM runs scheduled maintenance between human sessions
- Someone new (human or LLM) can pick up CLAUDE.md and operate effectively
- SOPs document how the system works

---

## Stage 2 — First External Application

*Proof: AM's patterns work on a real system.*

Apply AM's methodology to Rob's business — the first stress test against real-world messiness. This is where the fractal insight is proven or broken.

**Dual-instance model:** When Stage 2 begins, AM forks. One instance continues self-evolving (Stage 1 ongoing). A second instance is created to learn by working on the external system. Both instances share the same foundational governance but evolve independently. Learnings cross-pollinate during reflections.

### Wave 9 — Generalized Audit Protocol

**Question:** Can AM assess a system it didn't build?

Extract the self-audit capability into a protocol that works on any folder structure or vault. Scan, assess, map relationships, produce findings and recommendations. This is AM's first outward-facing capability.

### Wave 10 — External Application & Discovery

**Question:** Can AM organize Rob's business?

Apply the audit protocol to Rob's business files. Build the discovery workflow — understand what the business needs, map existing structure, propose governance. Implement and iterate. Maintain ongoing.

**Stage 2 Exit Criteria:**
- AM has successfully audited and organized an external system
- The methodology survived contact with real-world complexity
- Learnings are documented and fed back into AM's governance

---

## Stage 3 — Replication

*Proof: AM's patterns transfer to other contexts.*

Apply AM to other businesses and domains. Discover what's universal methodology vs. what's context-specific. Refine the approach.

**Stage 3 Exit Criteria:**
- AM has been applied to multiple distinct contexts
- The universal vs. context-specific boundary is understood
- The methodology is stable and documented for replication

---

## Stage 4 — Product

*Proof: AM scales.*

The proven, refined methodology becomes a sellable offering. The exact form — product, consulting framework, educational package, starter pack, or combination — emerges from the experience of Stages 2 and 3. This does not need to be decided now.

---

## How This Document Is Maintained

- The roadmap is reviewed during every wave reflection (Phase 6 / Reflect stage)
- Reflections consult both this roadmap and the [[AM — Future Waves Register]] to decide what comes next
- New waves are promoted from the register to the roadmap through a proposal in `03_DECIDE/proposals/`
- Completed waves are marked with ✓ and their outcomes summarized
- The roadmap's scope aligns with [[Agent Maestro — Strategy]] — if the strategic stages change, the roadmap must be updated to match
- Changes to the strategic arc (adding/removing/reordering stages) are Level 3 decisions requiring human approval

## Related

- [[Agent Maestro — Strategy]]
- [[Agent Maestro — North Star]]
- [[AM — Future Waves Register]]
- [[Proposal — Wave 5.2 Pipeline Hardening]]
- [[Proposal — Wave 6 Mechanical Integrity]]
- [[Proposal — Wave 7 Scheduled Execution]]
