---
schema_version: 2
title: Agent Maestro v0.2 — Wave 2+3 Proposal
tags:
- proposal
- build-contract
- wave-2
- wave-3
relationships:
  part_of: '[[Agent Maestro — Evolution Roadmap v0.2]]'
  implements: '[[Build Session Protocol]]'
  uses:
  - '[[Agent Maestro — Principles]]'
  - '[[Governance Before Autonomy]]'
  defines: []
  governs: []
  inherits_from: []
  applies_to: []
  produces: []
authority_weight: 65
created_date: 2026-03-14
last_modified: 2026-03-14
status: active
maps: []
related: []
related_maps: []
related_pipes: []
supersedes: []
superseded_by: []
review_status: draft
version: 1
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
id: PROJ.agent_maestro_v0_2_wave_2_3_proposal
type: project
note_class: execution
layer: execution
---

# Agent Maestro v0.2 — Wave 2+3 Proposal

## Overview

This proposal covers Foundation (Wave 2) and First Operational Agents (Wave 3). Together they take Agent Maestro from "architecture with operational infrastructure" to "architecture with running agents."

Platform: All sessions in Claude Code. Model: All sessions with Opus. Estimated total: ~9 sessions.

---

## Wave 2 — Foundation (~5 sessions)

### 2.1 — Frontmatter Compliance Pass (Upgrade 1.4)
What: Systematically visit every note. Ensure all conform to Frontmatter Schema v1. Fix missing fields, incorrect types, inconsistent values.
Deliverables: Every note checked and corrected, updated schema_validation_report.csv.
Success criteria: 100% compliance for all canonical notes.
Sessions: 1-2

### 2.2 — Agent Runtime Engine (Upgrade 3.1)
What: Build Python runtime for governed agent execution.
Deliverables: GovernedAgent base class, permission checking, logging integration, AgentRuntime class, unit tests, CLAUDE.md.
Success criteria: GovernedAgent loaded with Vault Curator Executive pack can be instantiated, actions checked against authority pack, results logged to CSV.
Sessions: 2-3

### 2.3 — Authority Pack Templates for Agent Layers (Upgrade 2.4)
What: Create YAML templates for Executive, Supervisor, Specialist layers.
Deliverables: 3 template YAML files, updated registry.
Success criteria: Templates can be copied and customised to create any new pack within 15 minutes.
Sessions: 1

### 2.4 — Process Unprocessed Notes (Upgrade 1.5)
What: Triage and integrate 45 notes from inbox and unprocessed.
Deliverables: Each note triaged, new canonical notes created, existing notes enriched, processing log.
Success criteria: Zero notes remaining that should be in canonical knowledge base.
Sessions: 2-3

### Wave 2 Session Plan

| Session | Tasks |
|---------|-------|
| SES-003 | Frontmatter Compliance Pass |
| SES-004 | Agent Runtime Engine (part 1) |
| SES-005 | Agent Runtime Engine (part 2) + Authority Pack Templates |
| SES-006 | Process Unprocessed Notes (part 1) |
| SES-007 | Process Unprocessed Notes (part 2) |

---

## Wave 3 — First Operational Agents (~4 sessions)

### 3.1 — Executive Agent Layer (Upgrade 2.1)
What: Create 5 executive agents with authority packs: Executive Orchestrator, Governance Executive, Operations Executive, Knowledge Executive, Evolution Executive.
Deliverables: 5 agent definitions, 5 authority packs, compiled artifacts, Executive Layer Map, updated registries.
Success criteria: Each executive has definition, pack, and compiled artifact.
Sessions: 1-2

### 3.2 — Vault Maintenance Constellation (Upgrade 2.5)
What: Build second constellation for vault maintenance. Supervisor + 5 specialists (Definition Alignment Auditor, Ontology Integrity Auditor, Template Compliance Scanner, Note Processor, Self-Healing Repairer).
Deliverables: Full constellation folder structure, all agent definitions + packs, workflows, compiled artifacts, updated registries.
Success criteria: Fully defined, all packs compile, mirrors Vault Curator pattern.
Sessions: 2-3

### 3.3 — State Change Logging (Upgrade 3.2)
What: Wire up CSV log schemas for automatic agent action recording.
Deliverables: Logging module, automatic log writing, test coverage.
Success criteria: Test workflow produces complete log entries.
Sessions: 1

### 3.4 — Orchestrator Script (Upgrade 3.5)
What: Build orchestrator.py for running constellation cycles.
Deliverables: orchestrator.py with CLI, test run against Vault Curator.
Success criteria: python orchestrator.py --constellation vault_curator completes full cycle.
Sessions: 1-2

### Wave 3 Session Plan

| Session | Tasks |
|---------|-------|
| SES-008 | Executive Agent Layer |
| SES-009 | Vault Maintenance Constellation (part 1) |
| SES-010 | Vault Maintenance Constellation (part 2) |
| SES-011 | State Change Logging + Orchestrator Script |

---

## End State After Waves 2+3

- Fully compliant vault
- All intellectual assets integrated
- Working Python runtime engine
- Five executive agents (AI C-Suite)
- Two constellations (Vault Curator + Vault Maintenance)
- Complete state change logging
- Orchestrator for command-line constellation runs
- Authority pack templates for all agent layers

## Risks

1. Runtime engine scope creep — mitigate with minimum viable build
2. Unprocessed note volume (45 notes) — mitigate by splitting across sessions
3. Authority pack overlap between executives — mitigate using existing conceptual definitions
4. Compilation failures — budget time for compiler fixes

## Approval

Approved 2026-03-14. Build begins with SES-003 (Frontmatter Compliance Pass).
