# Agent Maestro Vault

## Purpose

This vault is the operational center for Agent Maestro—the discipline of designing, governing, and evolving operational intelligence systems. Agent Maestro provides a comprehensive framework for building AI agents that are reliable, controllable, and capable of complex autonomous work within human-defined boundaries.

The vault is organized into seven major functional areas (01_CAPTURE through 06_EXECUTION + 99_ARCHIVE) that implement the Four-Layer Model: Authority Layer → Agent Runtime → Workflow Layer → Workspace Layer.

## Start Here — Agent Bootloader

**Read order for agents entering this vault:**

1. **This file** (CLAUDE.md) — Understand vault structure, conventions, and permissions
2. **SYSTEM_MAP.md** → `02_KNOWLEDGE/system_maps/SYSTEM_MAP.md` — Find anything in the vault by exact path
3. **Your authority pack** → Check `05_SYSTEMS/agent_systems/constellation_registry.csv` to find your constellation, then load your compiled pack from `05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/`

**Decision tree — "Where do I look?"**

| If you need... | Go to... |
|----------------|----------|
| What Agent Maestro IS and WHY it exists | `02_KNOWLEDGE/governance/Agent Maestro — North Star.md` |
| What principles govern all decisions | `02_KNOWLEDGE/governance/Agent Maestro — Principles.md` |
| What an agent is ALLOWED to do | Your compiled authority pack JSON in `05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/` |
| Which agents exist and what they do | `05_SYSTEMS/agent_systems/constellation_registry.csv` + constellation folders in `05_SYSTEMS/agent_systems/constellations/` |
| All authority packs registered | `05_SYSTEMS/authority_architecture/authority_pack_registry.csv` |
| How to run an agent or constellation | `05_SYSTEMS/runtime/orchestrator.py` (CLI: `list`, `status`, `run`, `run-agent`, `compile`, `review`, `approve`, `reject`, `dashboard`) |
| Pipeline definitions (how work flows) | `03_PIPELINES/` — one subfolder per pipeline type |
| Build session lifecycle | `03_PIPELINES/development/Build Session Protocol.md` |
| Operational logs and reports | `06_EXECUTION/logs/` (task, escalation, state change, session logs) |
| Current project status / build plan | `04_PROJECTS/active/agent_maestro_development/` |
| Complete vault index with all paths | `02_KNOWLEDGE/system_maps/SYSTEM_MAP.md` |

## Structure Overview

| Folder | Purpose | Key Files |
|--------|---------|-----------|
| `01_CAPTURE/` | Inbox for unsorted input (raw observations, drafts, captured context) | ~45 unprocessed notes |
| `02_KNOWLEDGE/` | Authoritative knowledge base | `governance/` (6 core docs), `system_maps/` (21 maps + SYSTEM_MAP.md), `indexes/knowledge_graph_index.csv` |
| `03_PIPELINES/` | Operational workflow definitions and pipeline contracts | 7 pipeline definitions across 4 categories |
| `04_PROJECTS/` | Project tracking with lifecycle management | `active/`, `incubating/`, `completed/` |
| `05_SYSTEMS/` | Implementation-level architecture and governance (most sensitive) | `runtime/` (Python), `authority_architecture/` (packs + compiler), `agent_systems/` (constellations) |
| `06_EXECUTION/` | Operational dashboards, logs, reports, tasks, planning | `logs/` (4 CSV logs), `reports/`, `dashboards/`, `workflows/prompts/` |
| `99_ARCHIVE/` | Historical and archived items (read-only reference) | — |

## Global Conventions

All notes in this vault follow these conventions:

### Frontmatter & Metadata
- All vault notes use YAML frontmatter with `schema_version: 2`
- Required frontmatter fields depend on note type (see Governance Schemas Reference)
- Common fields: `title`, `tags`, `relationships`, `authority_weight`, `created_date`, `last_modified`
- **Exception:** `CLAUDE.md` files are infrastructure files, not vault notes. They do not use YAML frontmatter and are excluded from schema validation and knowledge graph indexing. They serve as lightweight governance contracts for AI agents working in each directory.

### Wiki-Links & Relationships
- Wiki-links use double-bracket format: `[[Note Name]]`
- Relationships in frontmatter use typed links: `defines`, `part_of`, `implements`, `governs`, `inherits_from`, `applies_to`, `uses`, `produces`

### Dates & Data
- All dates use ISO 8601 format: `YYYY-MM-DD`
- CSV files use UTF-8 encoding with comma delimiters and ISO 8601 date format

### Naming Conventions
- Note titles use Title Case with em-dashes for subtitles (e.g., "Agent Maestro — North Star")
- Folders use UPPER_CASE_WITH_UNDERSCORES
- Files in 05_SYSTEMS use Title Case for governance documents

## The Four-Layer Model

The Agent Maestro architecture is organized in four layers:

1. **Authority Layer** (`05_SYSTEMS/authority_architecture/`): Defines what agents can and cannot do through authority packs, inheritance rules, and policy resolution
2. **Agent Runtime** (`05_SYSTEMS/runtime/` + `05_SYSTEMS/agent_systems/`): The systems and agents themselves — GovernedAgent base class, orchestrator, state change logging
3. **Workflow Layer** (`03_PIPELINES/`): Operational workflows and pipeline contracts that guide agent execution
4. **Workspace Layer** (`06_EXECUTION/`): Dashboards, logs, reports, and task management where agents record outcomes

## Key Governance Documents (Authority Layer)

These documents define the fundamental principles and constraints for the entire system. Located in `02_KNOWLEDGE/governance/`:

| Document | Authority Weight | Purpose |
|----------|-----------------|---------|
| [[Agent Maestro — Principles]] | 90 | The 12 principles governing all decisions |
| [[Agent Maestro — North Star]] | 90 | Core vision and strategic intent |
| [[Agent Maestro — Modes]] | 80 | Three operational modes (Design, Governance, Execution) |
| [[Agent Maestro — Scope]] | 80 | What Agent Maestro does and does not cover |
| [[Agent Maestro — Strategy]] | 80 | Strategic approach and key initiatives |
| [[Agent Maestro — Vault Rules]] | 80 | Rules for vault organization and content management |

## Key Registries

| Registry | Path | What it tracks |
|----------|------|---------------|
| Authority Pack Registry | `05_SYSTEMS/authority_architecture/authority_pack_registry.csv` | All 29 authority packs |
| Constellation Registry | `05_SYSTEMS/agent_systems/constellation_registry.csv` | 2 constellations (1 active, 1 deprecated) |
| Agent Registry | `05_SYSTEMS/agent_systems/agent_registry.csv` | All 18 agents with roles and permissions |
| Compiler Artifacts Registry | `05_SYSTEMS/authority_architecture/compiler/compiler_artifacts_registry.csv` | All 17 compiled JSON artifacts |
| Knowledge Graph Index | `02_KNOWLEDGE/indexes/knowledge_graph_index.csv` | All vault notes with metadata |
| Session Index | `06_EXECUTION/logs/sessions/session_index.csv` | All build sessions |
| State Change Log | `06_EXECUTION/logs/state_change_log.csv` | All vault modifications |
| Task Execution Log | `06_EXECUTION/logs/task_execution_log.csv` | All agent action results |
| Escalation Log | `06_EXECUTION/logs/escalation_log.csv` | All escalations |

## Runtime System

The runtime is implemented in Python at `05_SYSTEMS/runtime/`:

| Module | Purpose |
|--------|---------|
| `governed_agent.py` | Base class: loads compiled packs, checks permissions (exact match), enforces control gates, validates evidence requirements |
| `agent_runtime.py` | Runtime environment: logging, escalation, agent lifecycle |
| `orchestrator.py` | CLI: `python orchestrator.py list/status/run/run-agent/compile --vault-root <path>` |
| `state_change_logger.py` | Tracks CREATE/MODIFY/MOVE/ARCHIVE/DELETE/PROMOTE/REPAIR operations |

The compiler at `05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py` transforms YAML authority packs into compiled JSON governance artifacts via an 8-stage pipeline.

## Agent Permissions & Escalation

- **Agents MAY**: Read from all layers, follow pipeline contracts, update relationships in frontmatter, write operational data to 06_EXECUTION
- **Agents MUST escalate**: Changes to canonical knowledge (authority_weight >= 90), modifications to authority packs, system architecture changes, permanent deletions
- **Agents MUST NOT**: Modify archived items in 99_ARCHIVE, ignore escalation requirements, deviate from established patterns without governance approval

**Permission checking** uses exact string matching only. Unknown actions fail-safe to REQUIRES_ESCALATION. Control gates evaluate via context-provided evaluator functions. Evidence requirements check file existence before action execution.

## Build Protocol

> **⚠ MANDATORY: Read both documents below before starting any build session.**

Before beginning any build work, agents MUST read:

1. **Build Session Protocol** → `03_PIPELINES/development/Build Session Protocol.md`
   — Defines the 7-stage lifecycle: Input → Brief → Proposal → Build → Output Summary → Session Log → Git Commit
2. **Git Best Practices for AI-Assisted Builds** → `03_PIPELINES/development/Git Best Practices for AI-Assisted Builds v1.md`
   — Branch rules, checkpoint tags, commit conventions, safety rules for Claude

**Session stages (summary):**

1. Input → 2. Brief/Roadmap → 3. Proposal (Build Contract) → 4. Build → 5. Output Summary → 6. Session Log → 7. Git Commit + Release

**Critical rules:**
- Never build without human approval of the proposal. The proposal is the contract.
- Never work directly on `main`. Always create a dedicated branch (e.g., `phase-b-workflow-engine`).
- Create a checkpoint tag before each major build pass: `git tag pre-phase-X`
- Commit format: `SES-XXX: [summary of changes]`
- For milestone versions: `git tag vX.Y.Z` + release notes

**Project document locations:**

| Document type | Location |
|---------------|----------|
| Evolution roadmaps | `04_PROJECTS/active/agent_maestro_development/roadmaps/` |
| Build briefs | `04_PROJECTS/active/agent_maestro_development/briefs/` |
| Proposals | `04_PROJECTS/active/agent_maestro_development/proposals/` |
| Session logs | `06_EXECUTION/logs/sessions/` |
| Output summaries | `04_PROJECTS/active/agent_maestro_development/summaries/` |

## Related Documents

- See `CLAUDE.md` files in each subdirectory for layer-specific governance
- See `02_KNOWLEDGE/system_maps/SYSTEM_MAP.md` for the complete vault index
- Consult Governance Schemas Reference and Tool and Action Class Reference for detailed taxonomies
