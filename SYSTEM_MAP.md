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

The Inventory. A compact index of what currently exists in the vault and where to find it. Updated with every structural change.

---

## Vault Root

| File | Role |
|------|------|
| `CLAUDE.md` | The Charter — entry point for any agent |
| `SYSTEM_MAP.md` | This file — the Inventory |

---

## 01_CAPTURE — Input

Raw material waiting to be processed. Flat structure — no subfolders. Capture seeds and loose ideas land here. See `CLAUDE.md` in folder for conventions.

| File | Contents |
|------|----------|
| `Wave 8 — Capture Seed.md` | Seed from Wave 7 reflection — pipeline enforcement, git-ops, self-observation |

---

## 02_KNOWLEDGE — Interpret

Governance, concepts, skills, roles, templates, protocols.

### governance/

Constitutional and operational governance documents.

| File | Authority | Role |
|------|-----------|------|
| `Agent Maestro — North Star.md` | 97 | Mission and strategic intent — highest authority |
| `Agent Maestro — Foundations.md` | 95 | The kernel — 3 seeds, 1 meta-principle, 3 laws, 6 derived principles |
| `Agent Maestro — Vault Rules.md` | 85 | Vault structure, schema, conventions (72 rules) |
| `Agent Maestro — Scope.md` | 80 | What AM does and does not cover |
| `Agent Maestro — Strategy.md` | 80 | How AM evolves through 4 capability stages |
| `AM — Roadmap.md` | 75 | Strategic arc — committed waves and milestones |
| `AM — Universal Workflow.md` | 70 | How work happens at every scale (draft) |
| `AM — Integrity Layers.md` | 75 | Architectural separation: Mechanical vs Semantic integrity |
| `AM — Tool Conventions.md` | 70 | How tools are designed, built, and operated |
| `AM — Future Waves Register.md` | 60 | Backlog of validated ideas grouped by Strategy stage |

### governance/roles/

| File | Contents |
|------|----------|
| `Role — Worker.md` | Worker role definition (Level 1–2 authority) |
| `Role — Reviewer.md` | Reviewer role definition (Level 2 authority) |

### concepts/

Foundational domain knowledge — the minimum viable concept set.

| File | Authority | Contents |
|------|-----------|----------|
| `Agent.md` | 55 | What an agent is in AM's framework |
| `Authority Architecture.md` | 55 | How authority flows through the system |
| `Memory Architecture.md` | 55 | How AM stores and retrieves knowledge |
| `Operational Intelligence.md` | 55 | The discipline AM embodies |
| `Self-Observation.md` | 55 | How systems observe and improve themselves |
| `AM — Treatise on Core Principles.md` | 55 | Extended derivation behind the Foundations — 7 Primitives, fractal instances |

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

### templates/

| File | For creating |
|------|-------------|
| `Template — Governance.md` | Governance documents |
| `Template — Concept.md` | Concept notes |
| `Template — Skill.md` | Skill definitions |
| `Template — Role.md` | Role definitions |
| `Template — Session Log.md` | Session logs |
| `Template — Proposal.md` | Change proposals |
| `Template — Reflection.md` | Wave reflections |
| `Template — Audit Report.md` | Audit reports |

### protocols/

| File | Contents |
|------|----------|
| `Git Best Practices for AI-Assisted Builds.md` | Git conventions for AI-assisted development |

---

## 03_DECIDE — Decide

Active projects and approved decisions. Change proposals under review.

| Subfolder | Contents |
|-----------|----------|
| `active/` | Currently active, approved proposals |
| `proposals/` | Draft proposals awaiting gate review (currently empty) |

### Current Active Items

| File | Status |
|------|--------|
| `Proposal — Wave 5.2 Pipeline Hardening.md` | Complete |
| `Proposal — Wave 6 Mechanical Integrity.md` | Complete |
| `Proposal — Wave 7 Scheduled Execution.md` | Approved, executing |

---

## 04_EXECUTE — Act

### tools/vault-maintenance/

Mechanical integrity tool suite (Wave 6). Validates vault structural health against configurable rules.

| File | Role |
|------|------|
| `structure_check.sh` | Verify required folders, root files, pipeline CLAUDE.md |
| `yaml_validation.sh` | Validate YAML frontmatter (schema v3 compliance) |
| `broken_links.sh` | Check all wiki-links and relationship entries resolve |
| `orphan_detection.sh` | Detect files with no inbound links |
| `stub_detection.sh` | Detect empty/placeholder files |
| `naming_validation.sh` | Check filename/title uniqueness and matching |
| `inventory.sh` | Generate full vault manifest |
| `orchestrate.sh` | Run all tools, produce aggregate health report |
| `README.md` | Suite documentation, config schema, usage |

| Subfolder | Contents |
|-----------|----------|
| `config/` | `defaults.conf` (generic), `am.conf` (AM-specific) |
| `lib/` | `config.sh` (shared bash library), `yaml_validator.py` (Python core) |
| `reports/` | Generated reports (per-tool + aggregate) |
| `logs/` | Operational logs |

### runtime/

Scheduled execution runtime (Wave 7). Coordinates autonomous vault maintenance — scheduling, LLM summarisation, and notification.

| File | Role |
|------|------|
| `run_maintenance.sh` | Wrapper script — coordinates orchestrate.sh, summary, notification |
| `summarise_report.py` | Reads health report, invokes local LLM, appends summary |
| `notify.sh` | Sends macOS notification on findings |
| `config.example.yaml` | Configuration template (Ollama endpoint, model) |
| `README.md` | Runtime documentation |

| Subfolder | Contents |
|-----------|----------|
| `launchd/` | `com.agentmaestro.vault-maintenance.plist`, `install.sh`, `uninstall.sh` |

---

## 05_RECORD — Record

Logs, session history, and archive.

| Subfolder | Contents |
|-----------|----------|
| `logs/sessions/` | 17 session logs (SES-002 through SES-018) + session_index.csv |
| `reports/` | `Wave 6 — First Vault Health Report.md` |
| `sessions/` | Legacy session logs (pre-Wave 5.2 format) |
| `archive/` | Historical items organized by wave |

### archive/ subfolders

| Subfolder | Contents |
|-----------|----------|
| `pre_wave5/` | Pre-Wave 5 historical items |
| `wave_5_*` | Wave 5 archived items (agent_systems, authority_architecture, indexes, infrastructure, knowledge, memory_architecture, operational_intelligence, projects, reports, templates) |
| `wave_5.2_captures/` | 17 triaged capture notes |
| `wave_5.2_concepts/` | 39 archived concept files |
| `wave_5.2_execute/` | Archived runtime code and tools |
| `wave_5.2_governance/` | Archived Modes and Principles documents |
| `wave_5.2_logs/` | Archived CSV logs |
| `wave_5.2_reports/` | Archived runtime reports |
| `wave_5.2_roadmap/` | Archived old roadmap + Design Blueprint |

Also at `05_RECORD/` root level: session logs SES-002 through SES-006 and consumed capture seed (`Wave 5.2 — Phase 4 Capture Seed.md`).

---

## 06_REFLECT — Reflect

Reflections live directly in this folder — one per wave, flat structure. Each covers what happened, what we learned, and what comes next. Produces capture seeds that close the loop back to `01_CAPTURE/`.

| File | Wave |
|------|------|
| `Wave 5.1 — Design Session Reflection.md` | Wave 5.1 |
| `Wave 5.2 — Phases 1–3 Reflection.md` | Wave 5.2 (mid-wave) |
| `Wave 5.2 — Final Reflection.md` | Wave 5.2 (final) |
| `Wave 6 — Reflection.md` | Wave 6 |
| `Wave 7 — Reflection.md` | Wave 7 |

---

*Updated: 2026-03-17 — Wave 7 Scheduled Execution runtime built.*
