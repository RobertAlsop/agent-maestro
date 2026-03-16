# Agent Maestro Vault

## Purpose

Agent Maestro is the discipline of designing, governing, and evolving operational intelligence systems. Its mission is to create **more reliable intelligent systems** — not smarter AI.

This vault IS Agent Maestro. The folder structure mirrors the universal pipeline. Every folder is a stage. Every stage has gates. The same pattern operates at every level of abstraction.

## Start Here — Agent Bootloader

**Read order for agents entering this vault:**

1. **This file** (CLAUDE.md) — The Charter. Understand the architecture, conventions, and your role.
2. **Foundations** → `02_KNOWLEDGE/governance/Agent Maestro — Foundations.md` — The constitutional authority. All decisions trace back here.
3. **Universal Workflow** → `02_KNOWLEDGE/governance/AM — Universal Workflow.md` — How work happens at every scale.
4. **Your role** → `02_KNOWLEDGE/governance/roles/` — Load your role definition (Worker or Reviewer).
5. **System Map** → `SYSTEM_MAP.md` — The Inventory. What currently exists in the vault and where to find it.

## The Universal Pipeline

Agent Maestro is a 6-stage pipeline. The vault folders ARE the pipeline stages.

| Stage | Folder | Function | Question it answers |
|-------|--------|----------|-------------------|
| Input | `01_CAPTURE/` | Receive | What arrived? |
| Interpret | `02_KNOWLEDGE/` | Understand | What does it mean? |
| Decide | `03_DECIDE/` | Commit | What are we going to do? |
| Act | `04_EXECUTE/` | Execute | Do it. |
| Record | `05_RECORD/` | Remember | What happened? |
| Reflect | `06_REFLECT/` | Learn | What did we learn? What's next? |

Between every stage: a **gate**. Nothing moves forward without a check.

The loop closes: Reflect feeds back into Input. The brainstorm becomes the next brief.

## Vault Structure

```
CLAUDE.md                      ← You are here (The Charter)
AM v1.0.0 — Design Blueprint.md  ← Full architectural specification

01_CAPTURE/                    ← Raw ideas, observations, drafts, unsorted input
02_KNOWLEDGE/                  ← Governance, concepts, skills, templates, references
    governance/                   Constitutional documents (authority_weight ≥ 80)
    governance/roles/             Worker and Reviewer role definitions
    concepts/                     Domain knowledge and frameworks
    skills/                       The 7 core skill definitions
    templates/                    Patterns for creating artifacts
    references/                   External references
    indexes/                      Knowledge graph, registries
03_DECIDE/                     ← Active projects, proposals, contracts, roadmaps
04_EXECUTE/                    ← Runtime code, tools, active builds
    runtime/                      Python runtime (governed_agent, orchestrator, etc.)
    tools/                        Utility scripts
05_RECORD/                     ← Logs, reports, summaries, session history, archive
    logs/                         Operational logs (sessions, state changes, tasks)
    reports/                      Audit reports and summaries
    archive/                      Historical items
06_REFLECT/                    ← Reflections, evolution proposals, brainstorms
```

## Governance Hierarchy

The highest-authority documents, in order:

| Document | Authority Weight | What it governs |
|----------|-----------------|-----------------|
| [[Agent Maestro — Foundations]] | 95 | Everything — the kernel (3 seeds, 1 meta-principle, 3 laws, 6 derived principles) |
| [[Agent Maestro — North Star]] | 90 | Mission and strategic intent |
| [[Agent Maestro — Vault Rules]] | 85 | Vault structure, schema, and conventions |
| [[Agent Maestro — Scope]] | 80 | What AM does and does not cover |
| [[Agent Maestro — Strategy]] | 80 | How AM evolves through capability stages |
| [[Agent Maestro — Modes]] | 75 | The 6 operational modes (aligned with pipeline stages) |

When documents conflict, higher authority_weight wins. When weights are equal, defer to the Foundations. When the Foundations are ambiguous, escalate to the human.

## Agent Architecture

### Skills (7 core capabilities)

| Skill | What it does |
|-------|-------------|
| **Triage** | Classify input and route through the pipeline |
| **Validate** | Check artifacts against governance rules |
| **Audit** | Deep evaluation — alignment, integrity, viability |
| **Propose** | Formulate change proposals with evidence |
| **Gate** | Evaluate pipeline stage transitions |
| **Summarize** | Synthesize outcomes and create records |
| **Escalate** | Package decisions for human review |

Skill definitions live in `02_KNOWLEDGE/skills/`.

### Roles (2 + Human)

```
HUMAN (ultimate authority — Level 3)
  │
  ├─ Reviewer (Level 2 — audits, gates, proposes)
  └─ Worker (Level 1-2 — executes, processes, builds)
```

Role definitions live in `02_KNOWLEDGE/governance/roles/`.

**D6 rule:** The same model can play both roles, but not for the same work in the same context. Build as Worker, review as Reviewer.

### Escalation Levels

| Level | When | Resolution |
|-------|------|------------|
| 1 — Automatic | Rules cover it | Pass/fail against criteria |
| 2 — Agent judgment | Principles apply | Trace decision to Foundations |
| 3 — Human approval | Irreversible, architectural, or governance-level | Escalate with full context |

## Document Schema (v3)

All vault notes use YAML frontmatter:

```yaml
---
title: ""
type: ""               # governance | concept | skill | role | pipeline | log | report | proposal
status: ""             # draft | active | archived
authority_weight: 0    # 0-100 (≥80 = canonical)
schema_version: 3
created: ""            # ISO 8601
updated: ""            # ISO 8601
relationships:
  derives_from: []     # upward authority trace
  governs: []          # downward authority
  related: []          # everything else
tags: []
---
```

**Exception:** CLAUDE.md files are infrastructure, not vault notes. They do not use YAML frontmatter.

## Conventions

- Dates: ISO 8601 (`YYYY-MM-DD`)
- Note titles: Title Case with em-dashes for subtitles ("Agent Maestro — Foundations")
- Wiki-links: `[[Note Title]]`
- Folder names: UPPER_CASE or lowercase (pipeline folders use numbers + UPPER_CASE)
- CSV files: UTF-8, comma-delimited, ISO 8601 dates

## Build Protocol

Before any build session:

1. Read the **Design Blueprint** → `AM v1.0.0 — Design Blueprint.md`
2. Create a feature branch — never commit directly to `master`
3. Tag current state before major changes: `git tag pre-<description>`
4. Commit format: `SES-XXX: [summary]` or descriptive message
5. The proposal is the contract — never build without human approval

**Repository:** `https://github.com/robertalsop/agent-maestro`
**Current version:** v0.5.0 (Wave 5 complete)
**Target version:** v1.0.0 (Wave 5.1 — structural redesign)

## Permissions & Escalation

- **Agents MAY:** Read all folders, execute skills within their role, write to RECORD
- **Agents MUST escalate:** Changes to governance docs (authority_weight ≥ 80), structural changes, permanent deletions
- **Agents MUST NOT:** Approve their own work, modify Foundations without human approval, skip gates

When in doubt: escalate. The cost of asking is always lower than the cost of unauthorized action.
