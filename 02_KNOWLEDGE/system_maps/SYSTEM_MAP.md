---
schema_version: 2
title: "SYSTEM_MAP"
tags:
  - system-map
  - navigation
  - index
  - bootloader
relationships:
  part_of: "[[Agent Maestro — Navigation Map]]"
  implements: "[[Agent Maestro — Principles]]"
  governs: []
  uses: []
  defines: []
  inherits_from: []
  applies_to: []
  produces: []
authority_weight: 85
created_date: 2026-03-15
last_modified: 2026-03-15
status: active
review_status: approved
version: 1
canonical: true
source_type: ai_authored
type: map
note_class: navigation
layer: knowledge
---

# SYSTEM_MAP — Agent Maestro Master Navigation Index

This is the single entry point for navigating the entire Agent Maestro vault. Every system map, registry, constellation, pipeline, runtime module, and governance document is indexed here with its exact file path. Agents should read this file first (after CLAUDE.md) to orient themselves.

---

## Quick Decision Tree

**If you need to...**

- **Understand what Agent Maestro is** → Read `CLAUDE.md` (vault root) then `02_KNOWLEDGE/governance/Agent Maestro — North Star.md`
- **Find a specific system map** → See §1 below
- **Check what an agent is allowed to do** → See §3 (Authority Packs) or §4 (Registries)
- **Run or operate the system** → See §5 (Runtime) and §6 (Pipelines)
- **Find operational logs and reports** → See §7 (Execution Layer)
- **Look up a concept or pattern** → See §8 (Knowledge Base)
- **Find a constellation or agent definition** → See §3 (Agent Systems)

---

## §1 — System Maps (21)

All maps live in `02_KNOWLEDGE/system_maps/`. They provide high-level visual and conceptual navigation of different aspects of the system.

### Architecture & Structure Maps
| Map                                 | Path                                                          | Purpose                                                           |
| ----------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [[Agent Maestro — Layer Model Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Layer Model Map.md` | The Four-Layer Model (Authority → Runtime → Workflow → Workspace) |
| [[Agent Maestro — Stack Map]]       | `02_KNOWLEDGE/system_maps/Agent Maestro — Stack Map.md`       | Full technology and architecture stack                            |
| [[Agent Maestro — Systems Map]]     | `02_KNOWLEDGE/system_maps/Agent Maestro — Systems Map.md`     | All systems and their relationships                               |
| [[Memory Architecture Map]]         | `02_KNOWLEDGE/system_maps/Memory Architecture Map.md`         | Three memory layers (Knowledge Graph, Structured Data, Vector)    |

### Governance & Authority Maps
| Map | Path | Purpose |
|-----|------|---------|
| [[Agent Maestro — Governance Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Governance Map.md` | Governance principles, rules, and constraints |
| [[Agent Maestro — Governance Artifacts Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Governance Artifacts Map.md` | All governance artifacts and their locations |
| [[Authority Architecture Map]] | `02_KNOWLEDGE/system_maps/Authority Architecture Map.md` | Authority pack system architecture |
| [[Agent Maestro — Pack Inheritance Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Pack Inheritance Map.md` | How authority packs inherit from each other |
| [[Authority Pack Compiler — Map]] | `02_KNOWLEDGE/system_maps/Authority Pack Compiler — Map.md` | 8-stage compiler pipeline |
| [[Project Governance Map]] | `02_KNOWLEDGE/system_maps/Project Governance Map.md` | Project lifecycle governance |

### Agent & Constellation Maps
| Map | Path | Purpose |
|-----|------|---------|
| [[Agent Maestro — Agent Taxonomy Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Agent Taxonomy Map.md` | Agent types and classification |
| [[Agent Maestro — Constellation Architecture Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Constellation Architecture Map.md` | Executive → Supervisor → Specialist constellation model |
| [[Agent Maestro — Executive Layer Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Executive Layer Map.md` | The five executive agents and their domains |

### Domain & Knowledge Maps
| Map | Path | Purpose |
|-----|------|---------|
| [[Agent Maestro — Concepts Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Concepts Map.md` | Core concepts and their relationships |
| [[Agent Maestro — Domain Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Domain Map.md` | Knowledge domains covered by the vault |
| [[Agent Maestro — Practice Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Practice Map.md` | Operational practices and methodologies |
| [[Operational Intelligence Map]] | `02_KNOWLEDGE/system_maps/Operational Intelligence Map.md` | The broader OI discipline |

### Operational & Navigation Maps
| Map | Path | Purpose |
|-----|------|---------|
| [[Agent Maestro — Navigation Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Navigation Map.md` | How to navigate the vault |
| [[Agent Maestro — Pipelines Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Pipelines Map.md` | All operational pipelines |
| [[Agent Maestro — Projects & Experiments Map]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Projects & Experiments Map.md` | Active and completed projects |
| [[Agent Maestro — Quickstart]] | `02_KNOWLEDGE/system_maps/Agent Maestro — Quickstart.md` | Quick orientation guide |

---

## §2 — Governance Documents

Core governance documents that define the principles, rules, and boundaries of the entire system. These have the highest authority weights.

| Document | Path | Authority Weight |
|----------|------|-----------------|
| [[Agent Maestro — Principles]] | `02_KNOWLEDGE/governance/Agent Maestro — Principles.md` | 90 |
| [[Agent Maestro — North Star]] | `02_KNOWLEDGE/governance/Agent Maestro — North Star.md` | 90 |
| [[Agent Maestro — Modes]] | `02_KNOWLEDGE/governance/Agent Maestro — Modes.md` | 80 |
| [[Agent Maestro — Scope]] | `02_KNOWLEDGE/governance/Agent Maestro — Scope.md` | 80 |
| [[Agent Maestro — Strategy]] | `02_KNOWLEDGE/governance/Agent Maestro — Strategy.md` | 80 |
| [[Agent Maestro — Vault Rules]] | `02_KNOWLEDGE/governance/Agent Maestro — Vault Rules.md` | 80 |

---

## §3 — Agent Systems

### Constellations

| Constellation | ID | Executive Agent | Status | Definition Path |
|---------------|----|-----------------|--------|----------------|
| Vault Curator | CONST.vault_curator | CONST.vault_curator.agent.executive | **deprecated** | `05_SYSTEMS/agent_systems/constellations/vault_curator/` |
| Vault Maintenance | CONST.vault_maintenance | EXEC.pack.knowledge_executive | active | `05_SYSTEMS/agent_systems/constellations/vault_maintenance/` |

**Registry**: `05_SYSTEMS/agent_systems/constellation_registry.csv`

### Vault Curator Constellation

| Role       | Agent                     | Definition                                                                     | Authority Pack                                                             |
| ---------- | ------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Executive  | Vault Governance Director | `constellations/vault_curator/01_executive_links/vault_governance_director.md` | `packs/constellation_packs/vault_curator/executive.yaml`                   |
| Supervisor | Integrity Coordinator     | `constellations/vault_curator/02_supervisors/integrity_coordinator.md`         | `packs/constellation_packs/vault_curator/supervisor.yaml`                  |
| Specialist | Link Auditor              | `constellations/vault_curator/03_specialists/link_auditor.md`                  | `packs/constellation_packs/vault_curator/specialist_link_auditor.yaml`     |
| Specialist | Orphan Detector           | `constellations/vault_curator/03_specialists/orphan_detector.md`               | `packs/constellation_packs/vault_curator/specialist_orphan_detector.yaml`  |
| Specialist | Schema Validator          | `constellations/vault_curator/03_specialists/schema_validator.md`              | `packs/constellation_packs/vault_curator/specialist_schema_validator.yaml` |

All paths relative to `05_SYSTEMS/agent_systems/`.

### Vault Maintenance Constellation

| Role       | Agent                        | Definition                                                                        | Authority Pack                                                                     |
| ---------- | ---------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Executive  | Knowledge Executive (shared) | `packs/executive/knowledge_executive.yaml`                                        | `packs/executive/knowledge_executive.yaml`                                         |
| Supervisor | Maintenance Coordinator      | `constellations/vault_maintenance/02_supervisors/maintenance_coordinator.md`      | `packs/constellation_packs/vault_maintenance/supervisor.yaml`                      |
| Specialist | Definition Alignment Auditor | `constellations/vault_maintenance/03_specialists/definition_alignment_auditor.md` | `packs/constellation_packs/vault_maintenance/specialist_definition_alignment.yaml` |
| Specialist | Ontology Integrity Auditor   | `constellations/vault_maintenance/03_specialists/ontology_integrity_auditor.md`   | `packs/constellation_packs/vault_maintenance/specialist_ontology_integrity.yaml`   |
| Specialist | Template Compliance Scanner  | `constellations/vault_maintenance/03_specialists/template_compliance_scanner.md`  | `packs/constellation_packs/vault_maintenance/specialist_template_compliance.yaml`  |
| Specialist | Note Processor               | `constellations/vault_maintenance/03_specialists/note_processor.md`               | `packs/constellation_packs/vault_maintenance/specialist_note_processor.yaml`       |
| Specialist | Self-Healing Repairer        | `constellations/vault_maintenance/03_specialists/self_healing_repairer.md`        | `packs/constellation_packs/vault_maintenance/specialist_self_healing.yaml`         |

All definition paths relative to `05_SYSTEMS/agent_systems/`. All pack paths relative to `05_SYSTEMS/authority_architecture/`.

### Executive Authority Packs (5)

| Executive | Pack ID | Path |
|-----------|---------|------|
| Executive Orchestrator | EXEC.pack.executive_orchestrator | `05_SYSTEMS/authority_architecture/packs/executive/executive_orchestrator.yaml` |
| Knowledge Executive | EXEC.pack.knowledge_executive | `05_SYSTEMS/authority_architecture/packs/executive/knowledge_executive.yaml` |
| Governance Executive | EXEC.pack.governance_executive | `05_SYSTEMS/authority_architecture/packs/executive/governance_executive.yaml` |
| Operations Executive | EXEC.pack.operations_executive | `05_SYSTEMS/authority_architecture/packs/executive/operations_executive.yaml` |
| Evolution Executive | EXEC.pack.evolution_executive | `05_SYSTEMS/authority_architecture/packs/executive/evolution_executive.yaml` |

### Conceptual Authority Pack Types (8)

These are the foundational authority domain definitions (not compilable YAML packs — reference documentation):

| Authority Type | Path |
|---------------|------|
| Conceptual Authority | `05_SYSTEMS/authority_architecture/packs/conceptual_authority/` |
| Decision Authority | `05_SYSTEMS/authority_architecture/packs/decision_authority/` |
| Execution Authority | `05_SYSTEMS/authority_architecture/packs/execution_authority/` |
| Governance Authority | `05_SYSTEMS/authority_architecture/packs/governance_authority/` |
| Interface Authority | `05_SYSTEMS/authority_architecture/packs/interface_authority/` |
| Memory Authority | `05_SYSTEMS/authority_architecture/packs/memory_authority/` |
| Operational Authority | `05_SYSTEMS/authority_architecture/packs/operational_authority/` |
| Orchestration Authority | `05_SYSTEMS/authority_architecture/packs/orchestration_authority/` |

### Pack Templates

| Template | Path |
|----------|------|
| Executive Pack Template | `05_SYSTEMS/authority_architecture/packs/templates/executive_pack_template.yaml` |
| Supervisor Pack Template | `05_SYSTEMS/authority_architecture/packs/templates/supervisor_pack_template.yaml` |
| Specialist Pack Template | `05_SYSTEMS/authority_architecture/packs/templates/specialist_pack_template.yaml` |

---

## §4 — Registries (All CSV)

| Registry | Path | Contents |
|----------|------|----------|
| Authority Pack Registry | `05_SYSTEMS/authority_architecture/authority_pack_registry.csv` | All authority packs (executive + constellation), 29 entries |
| Agent Registry | `05_SYSTEMS/agent_systems/agent_registry.csv` | All agents with roles, permissions, and pack references, 18 entries |
| Constellation Registry | `05_SYSTEMS/agent_systems/constellation_registry.csv` | All constellations (1 active, 1 deprecated), 2 entries |
| Compiler Artifacts Registry | `05_SYSTEMS/authority_architecture/compiler/compiler_artifacts_registry.csv` | All compiled JSON artifacts, 17 entries |
| Knowledge Graph Index | `02_KNOWLEDGE/indexes/knowledge_graph_index.csv` | All vault notes with metadata |
| Session Index | `06_EXECUTION/logs/sessions/session_index.csv` | All build sessions |

---

## §5 — Runtime System

### Python Modules

| Module | Path | Purpose |
|--------|------|---------|
| GovernedAgent | `05_SYSTEMS/runtime/governed_agent.py` | Base class — loads compiled packs, checks permissions, enforces control gates, validates evidence |
| AgentRuntime | `05_SYSTEMS/runtime/agent_runtime.py` | Runtime environment (logging, escalation, agent lifecycle) |
| Orchestrator | `05_SYSTEMS/runtime/orchestrator.py` | CLI for running constellation cycles (`list`, `status`, `run`, `run-agent`, `compile`) |
| State Change Logger | `05_SYSTEMS/runtime/state_change_logger.py` | Tracks all vault modifications (create, modify, move, archive, delete, promote, repair) |
| Authority Pack Compiler | `05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py` | 8-stage YAML → JSON compiler |

### Test Suites

| Suite | Path | Tests |
|-------|------|-------|
| Runtime Tests | `05_SYSTEMS/runtime/test_runtime.py` | 21 tests (GovernedAgent, permissions, gates, evidence) |
| State Change Logger Tests | `05_SYSTEMS/runtime/test_state_change_logger.py` | 11 tests |

### Compiled Artifacts

All compiled JSON governance artifacts are stored in:
`05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/`

17 compiled artifacts across three constellations (executive, vault_curator, vault_maintenance).

### Infrastructure Tools

| Tool | Path | Purpose |
|------|------|---------|
| Master Index Generator | `05_SYSTEMS/infrastructure/tools/generate_master_index.py` | Generates knowledge_graph_index.csv |
| Knowledge Graph Export | `05_SYSTEMS/infrastructure/tools/knowledge_graph_export.py` | Exports knowledge graph data |
| Link Auditor | `05_SYSTEMS/infrastructure/tools/link_auditor.py` | Audits wiki-link integrity |
| Schema Validator | `05_SYSTEMS/infrastructure/tools/schema_validator.py` | Validates frontmatter schemas |

---

## §6 — Pipelines

All pipeline definitions live in `03_PIPELINES/`.

| Pipeline | Path | Purpose |
|----------|------|---------|
| [[Build Session Protocol]] | `03_PIPELINES/development/Build Session Protocol.md` | 7-stage lifecycle for every build session |
| [[Development Pipeline]] | `03_PIPELINES/development/Development Pipeline.md` | Software development workflow |
| [[System Design Pipeline]] | `03_PIPELINES/development/System Design Pipeline.md` | System architecture design process |
| [[Exploration Pipeline]] | `03_PIPELINES/exploration/Exploration Pipeline.md` | Research and exploration workflow |
| [[Learning Pipeline]] | `03_PIPELINES/learning/Learning Pipeline.md` | Knowledge acquisition pipeline |
| [[Maintenance Pipeline]] | `03_PIPELINES/maintenance/Maintenance Pipeline.md` | Vault maintenance operations |
| [[Agent Deployment Pipeline]] | `03_PIPELINES/deployment/Agent Deployment Pipeline.md` | Agent deployment lifecycle |

---

## §7 — Execution Layer

### Logs

| Log | Path | Purpose |
|-----|------|---------|
| Task Execution Log | `06_EXECUTION/logs/task_execution_log.csv` | Every `attempt_action()` result |
| Escalation Log | `06_EXECUTION/logs/escalation_log.csv` | All escalations raised by agents |
| State Change Log | `06_EXECUTION/logs/state_change_log.csv` | All vault modifications |
| Session Index | `06_EXECUTION/logs/sessions/session_index.csv` | Build session metadata |

### Session Logs

Located in `06_EXECUTION/logs/sessions/`:
- Session Log Template
- SES-002 (2026-03-14)
- SES-003 (2026-03-14)

### Reports

| Report | Path |
|--------|------|
| Link Audit Report | `06_EXECUTION/reports/link_audit_report.csv` |
| Schema Validation Report | `06_EXECUTION/reports/schema_validation_report.csv` |

### Dashboards & Planning

| Item | Path |
|------|------|
| Agent Maestro Dashboard | `06_EXECUTION/dashboards/Agent Maestro Dashboard.md` |
| Build Roadmap | `06_EXECUTION/roadmaps/Agent Maestro Build Roadmap.md` |
| Tasks Hub | `06_EXECUTION/tasks/Hub/Tasks Hub.md` |
| To Do | `06_EXECUTION/tasks/To Do/To Do.md` |
| Next Steps | `06_EXECUTION/tasks/Next Steps/Next Steps.md` |
| Open Questions | `06_EXECUTION/tasks/Questions/Open Questions.md` |
| Weekly Reset Template | `06_EXECUTION/weekly_planning/Weekly Reset Template.md` |

### Workflow Prompts

Located in `06_EXECUTION/workflows/prompts/`:
- Knowledge Upgrade Prompt v2
- Note Knowledge Upgrade v1
- Vault Build
- Vault Structure and Knowledge Upgrade v2

Vault maintenance prompts in `06_EXECUTION/workflows/prompts/vault_maintenance/`:
- 01 Definition Alignment Audit v2
- 02 Ontology Integrity Audit
- 03 Reasoning Path Audit
- Audit Folder For Unintended Cross-Folder Links
- Controlled Vault Repair Operation v2
- Filename Refactor
- Process Unprocessed Notes Into The Vault
- Template Architecture Audit
- Vault Integrity & Self-Healing Audit v2
- Vault Template Compliance Scan

---

## §8 — Knowledge Base

### Folder Structure

| Folder | Path | Contents |
|--------|------|----------|
| Concepts | `02_KNOWLEDGE/concepts/` | Core concept definitions |
| Patterns | `02_KNOWLEDGE/patterns/` | Reusable design and operational patterns |
| Governance | `02_KNOWLEDGE/governance/` | Governance principles and rules |
| Domains | `02_KNOWLEDGE/domains/` | Domain-specific knowledge |
| References | `02_KNOWLEDGE/references/` | External references and citations |
| System Maps | `02_KNOWLEDGE/system_maps/` | Navigational maps (this section) |
| Indexes | `02_KNOWLEDGE/indexes/` | Generated indexes (knowledge_graph_index.csv) |

---

## §9 — Authority Architecture Documents

Core architecture documents defining how authority works in the system.

| Document | Path |
|----------|------|
| [[Authority Architecture]] | `05_SYSTEMS/authority_architecture/Authority Architecture.md` |
| [[Authority Model]] | `05_SYSTEMS/authority_architecture/Authority Model.md` |
| [[Authority Inheritance]] | `05_SYSTEMS/authority_architecture/Authority Inheritance.md` |
| [[Pack Manifest]] | `05_SYSTEMS/authority_architecture/Pack Manifest.md` |
| [[Pack Versioning]] | `05_SYSTEMS/authority_architecture/Pack Versioning.md` |

### Compiler Documentation

| Document | Path |
|----------|------|
| 01_CAPTURE/inbox/Authority Pack Compiler]] | `05_SYSTEMS/authority_architecture/compiler/Authority Pack Compiler.md` |
| [[Compiler Pipeline]] | `05_SYSTEMS/authority_architecture/compiler/Compiler Pipeline.md` |
| [[Compiler Inputs]] | `05_SYSTEMS/authority_architecture/compiler/Compiler Inputs.md` |
| [[Compiler Outputs]] | `05_SYSTEMS/authority_architecture/compiler/Compiler Outputs.md` |
| [[Compiled Governance Artifacts]] | `05_SYSTEMS/authority_architecture/compiler/Compiled Governance Artifacts.md` |
| [[Compile Failure Semantics]] | `05_SYSTEMS/authority_architecture/compiler/Compile Failure Semantics.md` |
| [[Host Bindings]] | `05_SYSTEMS/authority_architecture/compiler/Host Bindings.md` |
| [[Integration Manifest]] | `05_SYSTEMS/authority_architecture/compiler/Integration Manifest.md` |

---

## §10 — Vault Structure Overview

```
Agent Maestro/
├── CLAUDE.md                          ← Root governance contract (read first)
├── .gitignore
├── 01_CAPTURE/                        ← Inbox (unsorted input, ~45 unprocessed notes)
├── 02_KNOWLEDGE/                      ← Authoritative knowledge base
│   ├── concepts/
│   ├── patterns/
│   ├── governance/                    ← 6 core governance documents
│   ├── domains/
│   ├── references/
│   ├── system_maps/                   ← 21 system maps + this file
│   └── indexes/                       ← knowledge_graph_index.csv
├── 03_PIPELINES/                      ← 7 operational pipeline definitions
│   ├── deployment/
│   ├── development/                   ← Build Session Protocol lives here
│   ├── exploration/
│   ├── learning/
│   └── maintenance/
├── 04_PROJECTS/                       ← Project tracking
│   ├── active/                        ← v0.3 Build Brief lives here
│   ├── incubating/
│   └── completed/
├── 05_SYSTEMS/                        ← Implementation (most sensitive)
│   ├── agent_systems/                 ← Constellation definitions + registry
│   ├── authority_architecture/        ← Packs, compiler, registries
│   ├── memory_architecture/           ← Memory layer documentation
│   ├── runtime/                       ← Python runtime (GovernedAgent, orchestrator, etc.)
│   ├── infrastructure/                ← Tools (validators, auditors, generators)
│   ├── operational_intelligence/      ← OI methodology docs
│   ├── organizational_integration/    ← Org integration patterns
│   └── templates/                     ← Frontmatter templates
├── 06_EXECUTION/                      ← Operational workspace
│   ├── dashboards/
│   ├── logs/                          ← Task, escalation, state change, session logs
│   ├── reports/                       ← Audit reports
│   ├── roadmaps/
│   ├── tasks/
│   ├── weekly_planning/
│   └── workflows/prompts/            ← Execution prompts for agents
└── 99_ARCHIVE/                        ← Historical/archived (read-only)
```

---

## §11 — Projects

| Project | Path | Status |
|---------|------|--------|
| Agent Maestro Development | `04_PROJECTS/active/agent_maestro_development/` | Active |
| v0.3 Build Brief | `04_PROJECTS/active/agent_maestro_development/Agent Maestro v0.3 — Build Brief.md` | Approved |

---

## Version

- **Created**: 2026-03-15
- **Last Updated**: 2026-03-15
- **Vault Version**: v0.2.1 (Phase A in progress)
