---
schema_version: 2
title: Agent Maestro — Evolution Roadmap v0.5.0
type: roadmap
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 75
resolution_basis: authority_weight
status: active
review_status: approved
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: human_authored
relationships:
  defines:
    - "[[Wave 5]]"
    - "[[Wave 6]]"
    - "[[Wave 7]]"
    - "[[Wave 8]]"
  part_of:
    - "[[Agent Maestro — Strategy]]"
  implements:
    - "[[Agent Maestro — North Star]]"
  supersedes:
    - "[[Agent Maestro — Evolution Roadmap v0.2]]"
  superseded_by: []
tags:
  - roadmap
  - strategy
  - v0.4
  - evolution
hash: ""
---

# Agent Maestro — Evolution Roadmap v0.5.0

**Date**: 2026-03-15
**Status**: APPROVED
**Starting version**: v0.4.0 (Build Brief complete — Phases A–D delivered)
**Principle**: Fractal architecture — every capability Agent Maestro builds for itself becomes a capability it can offer to other vaults.

---

## Strategic Target

Agent Maestro becomes a platform capable of auditing, optimizing, and building governed agent systems for external vaults (businesses, teams, domains). It achieves this by first mastering self-governance — using itself as the training ground. The path from internal ecosystem to external vault architect is a single continuous trajectory, not a pivot.

---

## Architectural Principles

### Fractal Design

Every layer of Agent Maestro is built from the same fundamental principles, applied at different levels of abstraction. The governance model that constrains a single specialist agent is the same model that will govern a multi-vault network. The audit workflow that checks Agent Maestro's own notes is the same workflow (generalized) that will check a business vault. Building inward *is* building outward.

### LLM / Script Separation

Two complementary execution paths, each doing what it does best:

- **Shell scripts** — Deterministic, fast, repeatable. File counts, link integrity checks, frontmatter validation, CSV operations, git workflows. The shell script vault maintenance layer complements the LLM constellation.
- **LLMs** — Judgment, classification, design. Is this note high quality? What constellation does this business need? Should we escalate? What's the best way to restructure this vault?

The tool registry's `adapter` field already models this: `vault_io` (script-like), `mcp_client` (LLM-mediated). Future adapters extend this separation cleanly.

### Minimum Viable Everything

At every stage, ask: what is the minimum we need? Minimum viable pipelines. Minimum viable governance documents. Minimum viable constellation for a given task. Bloat is the enemy of a system that needs to be legible to both humans and agents.

---

## Wave 5: Consolidation

**Question this wave answers:** *Does Agent Maestro carry anything it doesn't need?*

**Target version:** v0.5.0

### 5.1 — Vault Quality Audit

Systematic review of every vault note, starting with the highest authority weight and working down. For each note:

- Is the content accurate and current?
- Can it be simplified or distilled?
- Does it duplicate knowledge held elsewhere?
- Is the authority weight appropriate?
- Are relationships correct and complete?

Goal: a leaner, higher-quality knowledge base where every note earns its place.

### 5.2 — Governance Body Review

Specific focus on the 6 core governance documents (authority_weight 80–90). Questions:

- Are 12 principles the right number, or can some be merged?
- Are Modes, Scope, Strategy, and Vault Rules all pulling their weight?
- Is there redundancy between governance docs and CLAUDE.md?
- Can the governance body be expressed more concisely without losing precision?

### 5.3 — Pipeline Rationalization

Review all 7 pipeline definitions. Determine the minimum viable set:

- Which pipelines are actually used by workflows?
- Which are aspirational but not yet operational?
- Can any be merged or retired?
- What is the smallest set that supports: build sessions, vault maintenance, note processing, and deployment?

### 5.4 — Shell Script Maintenance Layer

Integrate the shell script vault maintenance tools alongside the LLM constellation. Define the boundary: scripts handle deterministic checks, LLMs handle judgment calls. Both report through the same observation and state change logging infrastructure.

**Exit criteria:** Every note justified. Governance body simplified if needed. Pipeline count reduced to minimum viable. Script/LLM boundary defined and operational.

---

## Wave 6: Living System

**Question this wave answers:** *Can Agent Maestro run on itself without a human starting every session?*

**Target version:** v0.6.0

### 6.1 — Runtime Provider Layer v2

Connect the governed inference infrastructure service to Agent Maestro. This transforms the runtime from "human opens Claude" to "inference service invokes governed agents on schedule or on demand." The runtime provider layer becomes the daemon from the G4 Host Options Evaluation, but backed by a proper inference service rather than direct API calls.

### 6.2 — Self-Observation Instrumentation

Implement the Self-Observation Specification (G5). Instrument GovernedAgent and WorkflowEngine with timing and metrics. Begin writing to `observation_log.csv`. This is the data foundation that Wave 7 depends on.

### 6.3 — Scheduled Task Execution

Define `daemon_safe` workflows and run them on a schedule from the host. Vault maintenance audits run daily/weekly without human intervention. Results appear in Slack DMs or observation dashboards. Escalations queue up for the next human session.

### 6.4 — Constellation Self-Assessment

The vault maintenance constellation runs regularly against the vault, finds issues, and either fixes them (within its authority) or escalates. This is Agent Maestro's first "living" behavior — ongoing self-care, not just build-session-driven work.

**Exit criteria:** Agent Maestro runs scheduled maintenance autonomously. Observation data accumulates. Escalations reach humans via Slack. The system is alive between sessions.

---

## Wave 7: Self-Improving System

**Question this wave answers:** *Can Agent Maestro improve itself safely?*

**Target version:** v0.7.0

### 7.1 — Evolution Constellation

Build the Evolution Constellation:

- **System Observer** — reads observation_log.csv, identifies patterns (slow stages, repeated escalations, declining vault health)
- **Performance Analyzer** — computes trends, ranks improvement opportunities by impact
- **Improvement Recommender** — proposes specific changes (adjust authority pack, optimize workflow, retire unused note)

All proposals go through governance — the Evolution Constellation cannot change the system directly. It recommends; the Governance Constellation (or a human) approves.

### 7.2 — Governance Constellation

Build the Governance Constellation:

- **Contract Validator** — checks that authority packs, compiled artifacts, and workflow definitions are internally consistent
- **Architecture Compliance Auditor** — verifies that changes align with the principles and architectural patterns
- **Pipeline Validator** — ensures workflow YAML matches the pipeline contracts

This constellation can validate proposed changes from the Evolution Constellation before they're applied.

### 7.3 — Self-Improvement Loop

Connect Evolution → Governance → Execution into a closed loop:

1. Evolution Constellation observes and proposes improvements
2. Governance Constellation validates proposals against principles
3. Approved proposals are executed (within authority) or escalated to human
4. Results are observed → feeds back to step 1

This is the fractal seed: the same loop that improves Agent Maestro will later improve external vaults.

### 7.4 — Model Router + Benchmark Constellation

Route different tasks to appropriate models (Opus for design, Sonnet for execution, Haiku for monitoring). Benchmark constellation measures model performance on Agent Maestro tasks and recommends routing adjustments.

**Exit criteria:** Agent Maestro proposes and validates its own improvements. Self-improvement loop operational. Model routing optimized.

---

## Wave 8: Vault Architect

**Question this wave answers:** *Can Agent Maestro do for others what it does for itself?*

**Target version:** v0.8.0 / v1.0.0

### 8.1 — Generalized Vault Audit Protocol

Extract the self-audit capability into a protocol that works on any vault (or folder structure). The protocol:

- Scans folder structure and file types
- Identifies organizational patterns (or lack thereof)
- Assesses content quality and consistency
- Maps relationships and dependencies
- Produces an audit report with findings and recommendations

This is the vault maintenance constellation's capabilities, generalized beyond the Agent Maestro schema.

### 8.2 — User Interview Workflow

Build a structured interaction workflow where Agent Maestro:

- Asks clarifying questions to understand a business/domain
- Identifies the user's goals, pain points, and existing structure
- Maps their needs to vault patterns and constellation types
- Produces a design proposal

This is a new pipeline type — consultative, human-in-the-loop at every stage.

### 8.3 — Vault Design Engine

Given an audit report and user interview data, Agent Maestro:

- Proposes an optimal vault structure
- Designs the constellation(s) needed to maintain and operate it
- Generates authority packs for those constellations
- Compiles governance artifacts
- Produces a deployment plan

This is the compiler + constellation builder, operating at a higher level of abstraction.

### 8.4 — First External Vault Audit

Apply the complete pipeline to a real external vault. Agent Maestro audits, interviews, designs, and proposes — using the same governance model it uses internally. The fractal completes.

**Exit criteria:** Agent Maestro can audit an external vault, interview a user, design a governance structure, and build the constellations to run it. The platform is proven.

---

## Explicitly Deferred

| Item | Why Deferred |
|------|-------------|
| Domain Deployment (TBP business agents) | Depends on Wave 8 being proven |
| Multi-Vault Agent Networks | Depends on single external vault working first |
| AI System Replication | Aspirational; requires Wave 8 at minimum |
| Portable Agent OS | Premature; focus on one runtime first |

---

## Wave Summary

| Wave | Name | Core Question | Key Deliverable |
|------|------|--------------|-----------------|
| 5 | Consolidation | Carrying anything we don't need? | Lean, justified vault + minimum viable pipelines |
| 6 | Living System | Can it run without a human starting it? | Scheduled autonomous maintenance + observation data |
| 7 | Self-Improving | Can it improve itself safely? | Evolution + Governance constellations + closed loop |
| 8 | Vault Architect | Can it do for others what it does for itself? | External vault audit + design + constellation builder |

---

**The fractal:** Wave 5 cleans the house. Wave 6 keeps it clean autonomously. Wave 7 improves the cleaning. Wave 8 cleans other houses.
