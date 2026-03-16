---
title: "SYSTEM_MAP"
type: governance
status: active
authority_weight: 50
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Vault Rules"]
  governs: []
  related: []
tags: [index, navigation, system-map]
---

## Purpose

The Inventory. A compact index of what currently exists in the vault and where to find it. Updated with every structural change. Replaces all prior system maps.

---

## Vault Root

| File | Role |
|------|------|
| `CLAUDE.md` | The Charter — entry point for any agent |
| `AM v1.0.0 — Design Blueprint.md` | The build contract for v1.0.0 |

---

## 01_CAPTURE — Input

Raw material waiting to be processed. Anything unclassified lands here.

| Subfolder | Contents |
|-----------|----------|
| `inbox/` | Unprocessed captures awaiting triage |
| `unprocessed/` | Items acknowledged but not yet routed |

---

## 02_KNOWLEDGE — Interpret

Governance, concepts, skills, roles, templates, references, indexes.

### governance/
Constitutional documents (authority_weight ≥ 80).

| File | Authority | Role |
|------|-----------|------|
| `Agent Maestro — Foundations.md` | 95 | The kernel — 3 seeds, 1 meta-principle, 3 laws, 6 derived principles |
| `Agent Maestro — North Star.md` | 90 | Mission and strategic intent |
| `Agent Maestro — Vault Rules.md` | 85 | Vault structure, schema, conventions |
| `Agent Maestro — Scope.md` | 80 | What AM does and does not cover |
| `Agent Maestro — Strategy.md` | 80 | How AM evolves through capability stages |
| `Agent Maestro — Modes.md` | 75 | The 6 operational modes |
| `Agent Maestro — Principles.md` | 75 | Derived principles reference |

### governance/roles/
| File | Contents |
|------|----------|
| `Role — Worker.md` | Worker role definition (Level 1–2 authority) |
| `Role — Reviewer.md` | Reviewer role definition (Level 2 authority) |

### skills/
The 7 core capability definitions.

| File | Pipeline stage(s) |
|------|------------------|
| `Skill — Triage.md` | CAPTURE → KNOWLEDGE |
| `Skill — Validate.md` | All stages |
| `Skill — Audit.md` | REFLECT + high-stakes gates |
| `Skill — Propose.md` | DECIDE |
| `Skill — Gate.md` | Between all stages |
| `Skill — Summarize.md` | RECORD |
| `Skill — Escalate.md` | Any stage (Level 3 trigger) |

### concepts/
Domain knowledge, patterns, and workflows.

| File | Contents |
|------|----------|
| `Build Session Protocol.md` | Protocol for build sessions |
| `Git Best Practices for AI-Assisted Builds v1.md` | Git conventions |
| `Consolidation Pipeline.md` | Pattern: consolidation workflow |
| `Maintenance Pipeline.md` | Pattern: maintenance workflow |
| `Note Upgrade Workflow.md` | Pattern: note upgrade process |

### templates/
Minimal v1.0.0 template set.

| File | For creating |
|------|-------------|
| `Template — Governance.md` | Governance documents |
| `Template — Concept.md` | Concept notes |
| `Template — Skill.md` | Skill definitions |
| `Template — Role.md` | Role definitions |
| `Template — Session Log.md` | Session logs |
| `Template — Proposal.md` | Change proposals |

### references/
External references and research (contents vary).

### indexes/
| File | Contents |
|------|----------|
| `SYSTEM_MAP.md` | This file — the master inventory |

---

## 03_DECIDE — Decide

Active projects and approved decisions awaiting execution. Change proposals under review.

| Subfolder | Contents |
|-----------|----------|
| `active/` | Currently active projects and decisions |
| `proposals/` | Proposals awaiting gate review |

### Current Active Items
| File | Status |
|------|--------|
| `Agent Maestro Vault Build.md` | v1.0.0 build in progress |
| `AM — Evolution Roadmap — Waves 5-8.md` | Active roadmap |

---

## 04_EXECUTE — Act

Runtime code, tools, and active builds.

| Subfolder | Contents |
|-----------|----------|
| `runtime/` | Python runtime (governed_agent, orchestrator, workflow_engine, etc.) |
| `tools/` | Utility scripts (link_auditor, schema_validator, shell scripts) |
| `builds/` | Active build work in progress |

### runtime/ key files
`governed_agent.py`, `orchestrator.py`, `workflow_engine.py`, `agent_runtime.py`, `mcp_adapter.py`, `state_change_logger.py`, `escalation_processor.py`, `tool_interface.py`

### tools/ key files
`link_auditor.py`, `schema_validator.py`, `generate_master_index.py`, `knowledge_graph_export.py`, `check_link_integrity.sh`, `detect_orphan_notes.sh`, `validate_frontmatter.sh`, `migrate_frontmatter.sh`

---

## 05_RECORD — Record

Logs, reports, summaries, session history, archive.

| Subfolder | Contents |
|-----------|----------|
| `logs/` | Operational logs (CSVs + session narratives) |
| `logs/sessions/` | Session logs (SES-XXX narrative summaries) |
| `reports/` | Audit reports, workflow execution reports |
| `archive/` | Historical items from pre-v1.0.0 |

### logs/ key files
`escalation_log.csv`, `escalation_resolution_log.csv`, `state_change_log.csv`, `task_execution_log.csv`

---

## 06_REFLECT — Reflect

Retrospectives, evolution proposals, brainstorms. The feedback loop back into CAPTURE.

| Subfolder | Contents |
|-----------|----------|
| `retrospectives/` | Session retrospectives and learnings |
| `evolution/` | Proposed improvements and experiments |
| `brainstorms/` | Ideas for future work |

---

*Updated: 2026-03-16 — v1.0.0 migration complete.*
