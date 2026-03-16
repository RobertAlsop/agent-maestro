---
title: "AM — Future Waves Register"
type: governance
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Strategy]]"
    - "[[AM — Roadmap]]"
  governs: []
  related:
    - "[[Agent Maestro — North Star]]"
tags: [register, strategy, backlog]
---

# AM — Future Waves Register

## Purpose

A living backlog of validated ideas that could become future waves. This register is the menu from which the [[AM — Roadmap|Roadmap]] selects. Ideas live here until they are promoted to the roadmap as a committed wave, or archived if they become irrelevant.

## Principle

The register is inclusive — every plausible idea gets a place. The roadmap is selective — only committed work appears there. The register feeds the roadmap; the roadmap does not feed the register. Ideas are grouped by the [[Agent Maestro — Strategy|Strategy]] stage they most naturally belong to, but may shift as understanding evolves.

---

## Stage 1 — Self-Governance

### Mechanical Integrity Layer (Wave 6 candidate)

**Source:** Capture — "Proposal — Shell Script Vault Maintenance Constellation," "The 6 shell scripts every large knowledge-vault builder eventually creates"

Build the shell script layer for deterministic vault validation. Core capabilities: vault integrity scanning, inventory reporting, broken link detection, YAML validation, duplicate ID detection, orphan file detection, stub detection, auto-commit, scheduled maintenance runner, CI validation. Config-driven and portable across vaults.

Key design principle: shell scripts enforce mechanical integrity, LLMs enforce semantic integrity. Scripts detect and report; they never interpret meaning.

**Related ideas:**
- "Potential rule" capture note — codify which tasks belong to scripts vs. LLMs
- "Agent responsibility collision" capture note — layered architecture preventing agents from stepping on each other (Layer 0: vault, Layer 1: mechanical scripts, Layer 2: triage/routing, Layer 3: specialist auditors, Layer 4: controlled repair, Layer 5: validation/change control)

### Runtime & Execution Layer (Wave 7 candidate)

**Source:** Capture — "Runtime Provider Layer Proposal v2," "AM Python Daemon for scheduled automations"

Bring 04_EXECUTE to life. The Runtime Provider Layer (RPL) is a substrate service providing governed access to LLM inference. Provider-agnostic (local via Ollama, cloud via Anthropic/OpenAI). Strict separation: RPL handles inference only; runtime engines handle all side effects.

The Python daemon enables scheduled, unattended execution — vault maintenance runs on a cron/launchd schedule without human intervention.

**Related ideas:**
- "Memory Options" / "RAG vs QMD" capture notes — persistence and retrieval strategy (CSV, SQLite, vector, page index DB). Decision needed: what's the right memory architecture for AM's operational data?
- "Toon" capture note — use TOON with JSON for lower API fees during routine operations
- Model routing — different models for different tasks (Opus for design, Sonnet for execution, Haiku for monitoring)

### Self-Observation & Autonomy (Wave 8 candidate)

**Source:** Old roadmap Waves 6-7

Instrument the pipeline with timing and metrics. Implement observation logging. Build the self-assessment loop: observe → identify patterns → propose improvements → governance gate → execute or escalate. The evolution loop that allows AM to improve itself safely.

**Sub-capabilities:**
- Self-observation instrumentation (timing, metrics, observation_log.csv)
- Evolution capability (system observer, performance analyzer, improvement recommender)
- Governance validation of proposed changes (contract validator, architecture compliance, pipeline validator)
- Closed self-improvement loop with human escalation for high-stakes changes

### Operational Improvements (any wave)

**Source:** Various capture notes

- **Slack notifications** — message sent when new capture seeds, proposals, or reports are filed. Same function pattern for each. (Capture: "Message sent on new capture sees")
- **Capture seed → brief pipeline** — should every capture seed automatically produce a brief? Or is that overkill? (Capture: "Breifs")
- **Terminology refinement** — ✓ Resolved in Wave 5.2: "reflections" adopted, replacing "retrospectives." Folder, template, and all references updated.
- **Roles placement** — question whether roles should live in governance. Currently they do. (Capture: "Roles") — resolved in Wave 5.2: roles confirmed in `governance/roles/`.
- **Skills acquisition model** — building skills vs. acquiring from external marketplace. (Capture: "Skills")
- **Archived treatise rescue** — ✓ Resolved in Wave 5.2: treatise rescued to `02_KNOWLEDGE/concepts/AM — Treatise on Core Principles.md`, updated to schema v3.

---

## Stage 2 — First External Application

### Generalized Audit Protocol (Wave 9 candidate)

**Source:** Old roadmap Wave 8.1

Extract AM's self-audit capability into a protocol for any vault or folder structure. Scan structure, identify patterns, assess quality and consistency, map relationships, produce findings and recommendations. This is the mechanical integrity layer plus semantic audit, generalized beyond AM's own schema.

### Discovery & Interview Workflow (Wave 10 candidate)

**Source:** Old roadmap Wave 8.2

Build a structured interaction workflow: ask clarifying questions, understand business/domain goals, identify pain points and existing structure, map needs to vault patterns, produce a design proposal. This is a consultative, human-in-the-loop pipeline type.

### External Vault Design & Implementation

**Source:** Old roadmap Wave 8.3

Given an audit report and discovery data: propose optimal structure, design governance, generate role and skill definitions, produce a deployment plan. Apply to Rob's business as the first real test case.

### Dual-Instance Evolution Model

**Source:** Rob, Wave 5.2 Phase 4 discussion

When Stage 2 begins, fork AM. One instance continues self-evolution (Stage 1 ongoing). A second instance is created for external application work. Both share foundational governance but evolve independently. Learnings cross-pollinate during reflections.

---

## Stage 3 — Replication

### Multi-Context Application

**Source:** Strategy Stage 3

Apply AM to multiple distinct businesses/domains. Discover what's universal methodology vs. context-specific. Refine and stabilize the approach.

### AM Starter Pack

**Source:** Capture — "Am basically starter pack"

A stripped-down, empty AM instance that guides an LLM to create the first agent, run the first instance, and start the evolution. A bootstrapping kit for new vaults. This could be the seed of a product offering.

---

## Stage 4 — Product

### Productization (form TBD)

**Source:** Strategy Stage 4

The exact form emerges from Stages 2-3. Possibilities include: consulting framework, educational package, starter pack product, SaaS platform, or some combination. Explicitly deferred until proven through replication.

---

## Explicitly Deferred

| Item | Why Deferred |
|------|-------------|
| Domain deployment (specific business agents) | Depends on Stage 2 being proven |
| Multi-vault agent networks | Depends on single external vault working first |
| AI system replication | Aspirational; requires Stage 3 at minimum |
| Portable agent OS | Premature; focus on one runtime first |

---

## How This Document Is Maintained

- **Adding items:** Capture notes that survive triage are added here, grouped by the Strategy stage they belong to. Items include source attribution (which capture note or discussion they came from).
- **Promoting items:** When a reflection identifies the next wave, the relevant register item is used to draft a proposal in `03_DECIDE/proposals/`. The register item is marked as promoted (not removed — it preserves the provenance).
- **Archiving items:** If an idea becomes irrelevant after two waves without promotion, it is a candidate for removal. Removed items are noted in the "Explicitly Deferred" table with a reason.
- **Reflection consultation:** Every wave reflection (Phase 6) reviews this register alongside the [[AM — Roadmap]] to inform what comes next.

## Related

- [[AM — Roadmap]]
- [[Agent Maestro — Strategy]]
- [[Agent Maestro — North Star]]
