---
id: PROJ.improvement_proposal_v0.1
type: project
note_class: execution
domain: governance
layer: execution
scope:
canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: draft
version: 1
created: 2026-03-14
updated: 2026-03-14
last_reviewed:
review_cycle: quarterly
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
map: "[[Agent Maestro — Navigation Map]]"
maps: []
related:
  - "[[Agent Maestro — North Star]]"
  - "[[Agent Maestro — Principles]]"
  - "[[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]]"
  - "[[Memory Model]]"
related_maps: []
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - project
  - proposal
  - improvement
hash: ""
---

# Agent Maestro v0.1 — Improvement Proposal

## Summary

This proposal defines eight concrete improvements to bring Agent Maestro from a conceptual governance framework to an operational, buildable system. Each improvement addresses a specific gap identified during a full audit of the v0.0.1 vault.

Improvement #9 (testing against existing orchestration frameworks like CrewAI, AutoGen, LangGraph) is deferred to a later phase.

---

## Improvement 1 — Reference Implementation

### Problem

Agent Maestro defines 26 concepts, 14 patterns, and a full compilation pipeline, but contains no working example of a governed agent constellation. Without a reference implementation, the framework remains theoretical.

### Proposal

Build a complete, end-to-end reference constellation called **"Vault Curator"** — a three-layer agent system that governs and maintains the Agent Maestro vault itself. This use case is ideal because it exercises the most framework features while being immediately useful.

### Why Vault Curator

The Vault Curator constellation would handle tasks the vault already needs: validating that notes conform to schema, checking wiki-link integrity, enforcing frontmatter standards, and flagging orphaned notes. This means the reference implementation is not a toy example — it is the first real deployment of Agent Maestro governance, applied to Agent Maestro itself.

### Constellation Structure

**Executive Agent — Vault Governance Director**

- Owns the top-level authority pack for vault operations
- Decides which maintenance tasks to prioritise
- Escalates destructive actions (file deletion, schema migration) to the human operator
- Authority type: Decision authority

**Supervisor Agent — Integrity Coordinator**

- Receives task priorities from the Executive
- Delegates specific checks to Specialist agents
- Aggregates results and reports back
- Authority type: Bounded decision + delegation authority

**Specialist Agents (three):**

| Specialist | Responsibility | Authority Type |
|---|---|---|
| Schema Validator | Checks YAML frontmatter against governance schemas | Execution authority |
| Link Auditor | Validates wiki-links resolve to existing notes | Execution authority |
| Orphan Detector | Identifies notes with no inbound links | Execution authority |

### What Gets Built

| Deliverable | Location |
|---|---|
| Executive authority pack | `05_SYSTEMS/authority_architecture/packs/constellation_packs/vault_curator/` |
| Supervisor authority pack | Same directory |
| Three specialist authority packs | Same directory |
| Compiled governance artifacts (one per agent) | `05_SYSTEMS/authority_architecture/compiler/artifacts/vault_curator/` |
| Constellation map | `05_SYSTEMS/agent_systems/constellations/vault_curator/` |
| Execution log template | `06_EXECUTION/workflows/vault_curator/` |
| Walkthrough document | `04_PROJECTS/active/vault_curator/` |

### Escalation Path Demonstrated

```
Specialist (Link Auditor) finds 12 broken links
  → Reports to Supervisor (Integrity Coordinator)
    → Supervisor classifies: 10 are safe renames, 2 require file deletion
      → Supervisor fixes 10 renames (within execution authority)
      → Supervisor escalates 2 deletions to Executive
        → Executive evaluates impact, escalates to Human Operator
          → Human approves or rejects
```

This single example exercises authority packs, escalation, decision-execution separation, the human escalation pattern, and audit trails.

---

## Improvement 2 — Authority Pack Compiler Prototype

### Problem

The compiler pipeline is documented across six notes ([[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]], [[Compiler Pipeline]], [[Compiler Inputs]], [[Compiler Outputs]], [[Host Bindings]], [[Compile Failure Semantics]]) but no implementation exists. Until the compiler can actually process a pack, the governance model cannot be validated.

### Proposal

Build a working prototype compiler as a Python script that processes authority packs written in YAML and outputs compiled governance artifacts as JSON. The compiler will implement all 8 pipeline stages defined in [[Compiler Pipeline]].

### Design Decisions

**Input format: YAML.** Authority packs are currently markdown notes with YAML frontmatter. The compiler will read the frontmatter as the machine-processable governance contract. The markdown body remains human documentation.

**Output format: JSON.** Compiled artifacts are JSON files with a strict schema, suitable for consumption by any runtime host.

**Host: Filesystem.** The first host binding targets "filesystem" — meaning the compiled artifact is written to a known directory and can be loaded by any agent process that reads JSON.

### Pipeline Stages (Implemented)

| Stage | Implementation |
|---|---|
| 1. Input Validation | Validate YAML frontmatter against a JSON Schema for authority packs |
| 2. Inheritance Resolution | Traverse `inherits_from` fields, flatten into a single merged pack |
| 3. Override Application | Apply child pack fields that explicitly override parent fields |
| 4. Policy Resolution | Detect conflicting rules; fail with a conflict report if unresolvable |
| 5. Completeness Validation | Check all required sections present per the 14-section grammar |
| 6. Artifact Generation | Produce the compiled JSON artifact |
| 7. Host Binding | Write artifact to the target host directory with a binding manifest |
| 8. Output Registration | Append entry to a `compiler_artifacts_registry.csv` (structured data layer) |

### File Structure

```
05_SYSTEMS/authority_architecture/compiler/
├── prototype/
│   ├── compiler.py              # Main compiler script
│   ├── schema/
│   │   ├── authority_pack.schema.json    # Input validation schema
│   │   └── compiled_artifact.schema.json # Output validation schema
│   ├── artifacts/               # Compiled output directory
│   └── README.md                # Usage instructions
```

### First Compilation Target

The Vault Curator constellation packs from Improvement 1, producing five compiled governance artifacts (one per agent).

---

## Improvement 3 — Vault Navigation Hardening

### Problem

The vault contains 15 system maps and multiple indexes that rely on Obsidian wiki-links. If a note is renamed or a link target doesn't exist, navigation silently breaks. There is no way to detect this without manually clicking every link.

### Proposal

Build a link integrity checker (one of the Vault Curator specialists from Improvement 1) and a generated master index.

### Deliverables

**A. Link Auditor Script**

A Python script (`05_SYSTEMS/infrastructure/tools/link_auditor.py`) that:

- Scans all `.md` files in the vault
- Extracts all `[[wiki-links]]` (including aliased links like `[[target|display]]`)
- Checks each link resolves to an existing file
- Outputs a report as CSV: `source_file, link_text, target_file, status (valid/broken/ambiguous)`
- Report saved to `06_EXECUTION/reports/link_audit_report.csv`

**B. Generated Master Index**

A script that generates `02_KNOWLEDGE/indexes/Master Index — Generated.md` by crawling the vault and producing a categorised list of all notes, grouped by `note_class` from frontmatter. This index regenerates on demand and never goes stale.

**C. Frontmatter Schema Validator**

A script that validates every note's YAML frontmatter against the governance schema, reporting missing required fields, invalid values, and schema version mismatches. Output as CSV to `06_EXECUTION/reports/schema_validation_report.csv`.

---

## Improvement 4 — Memory Architecture: Concrete Implementation

### Problem

The three-layer memory model ([[Knowledge Graph Layer]], [[Vector Memory Layer]], [[Structured Data Layer]]) defines responsibilities and invariants but provides no concrete technology bindings or implementation guidance.

### Current Constraints and the Two-vs-Three Layer Question

- No vector database is connected — the Vector Memory Layer is deferred
- The Knowledge Graph Layer should be implemented within the vault using markdown
- The Structured Data Layer should use CSV files compatible with Google Sheets

**Architectural principle vs. operational reality:** The Three-Layer Memory Model remains the correct architectural principle. It describes the complete design — the system Agent Maestro is building toward. However, the current operational state is a **two-layer implementation** (Knowledge Graph + Structured Data), with the Vector Memory Layer architecturally reserved. The principle name should not change, but all documentation should clearly distinguish between the architectural target (three layers) and the current implementation (two active layers, one planned). The Memory Model note will be updated to include an "Implementation Status" section reflecting this.

### 4A. Knowledge Graph Layer — Obsidian-Native with Generated Index

**Approach: Hybrid.** Each knowledge entity is an Obsidian note (browsable, linkable, human-readable). A generated index provides programmatic access.

**How it works:**

Every entity in the knowledge graph is already a note in the vault — concepts like [[Agent]], [[Authority Pack]], [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] are nodes. The wiki-links between them (`relationships` in frontmatter, inline `[[links]]` in the body) are edges. This means the knowledge graph already exists implicitly. The improvement is to make it explicit and queryable.

**Deliverables:**

1. **Standardise the `relationships` frontmatter block** across all concept, system, and pattern notes. Currently the relationships field exists but arrays are mostly empty. Populate them with actual relationships by auditing each note's wiki-links and backfilling the frontmatter. The relationship types already defined in the schema (`defines`, `part_of`, `implements`, `governs`, `inherits_from`, `applies_to`, `uses`, `produces`) become the edge types.

2. **Generate a Knowledge Graph Index** (`02_KNOWLEDGE/indexes/Knowledge Graph Index.csv`) — a CSV file listing every edge in the graph:

   | source_id | source_name | relationship_type | target_id | target_name |
   |---|---|---|---|---|
   | CON.agent | Agent | part_of | CON.agent_constellation | Agent Constellation |
   | CON.authority_pack | Authority Pack | governs | CON.agent | Agent |

   This CSV is the machine-readable knowledge graph. It is importable into Google Sheets for querying, filtering, and visualization. It can also be loaded by any script that needs to traverse the graph.

3. **Graph Statistics Dashboard** — a generated note (`06_EXECUTION/dashboards/Knowledge Graph Dashboard.md`) showing node count by type, edge count by relationship type, most-connected nodes, and orphaned nodes.

**Why this approach is best:**

- Zero new tooling dependencies — works within Obsidian today
- The vault IS the knowledge graph; no sync problem between a database and the notes
- The CSV export makes it queryable outside Obsidian and compatible with Google Sheets
- Obsidian's graph view already visualises it natively
- When a vector database is added later, embeddings can be generated from these same notes

### 4B. Structured Data Layer — CSV with Google Sheets Compatibility

**Yes, CSV works well for this.** Google Sheets imports and exports CSV natively. As long as the files follow standard conventions, they are fully compatible.

**Conventions for Google Sheets compatibility:**

- UTF-8 encoding (Google Sheets default)
- Comma delimiter (not semicolons or tabs)
- First row is always headers
- No merged cells or multi-line cell values (keep values atomic)
- Date format: `YYYY-MM-DD` (ISO 8601, which Google Sheets parses correctly)
- Filenames use underscores, no spaces (e.g., `compiler_artifacts_registry.csv`)
- One CSV per operational concern (not one giant file)

**Structured Data Registry — defined CSV files:**

| CSV File | Purpose | Location |
|---|---|---|
| `compiler_artifacts_registry.csv` | Tracks all compiled governance artifacts | `05_SYSTEMS/authority_architecture/compiler/` |
| `link_audit_report.csv` | Output of the link auditor | `06_EXECUTION/reports/` |
| `schema_validation_report.csv` | Output of the schema validator | `06_EXECUTION/reports/` |
| `knowledge_graph_index.csv` | Exported knowledge graph edges | `02_KNOWLEDGE/indexes/` |
| `constellation_registry.csv` | Tracks deployed constellations and their status | `05_SYSTEMS/agent_systems/` |
| `authority_pack_registry.csv` | Index of all authority packs with version and status | `05_SYSTEMS/authority_architecture/` |
| `escalation_log.csv` | Records all escalation events across constellations | `06_EXECUTION/logs/` |
| `task_execution_log.csv` | Records agent task executions with outcomes | `06_EXECUTION/logs/` |

Each CSV file will have a companion schema note (markdown) documenting its columns, data types, and update rules.

### 4C. Vector Memory Layer — Deferred

The Vector Memory Layer is acknowledged but not implemented in this phase. When a vector database is connected, embeddings will be generated from the markdown notes in the Knowledge Graph Layer. The architecture is designed so this layer can be added without restructuring the other two layers.

**Preparation for future integration:** Each note's `id` field in frontmatter serves as the stable identifier that will link a vector embedding back to its source note. This ID stability is already an invariant of the Knowledge Graph Layer.

---

## Improvement 5 — Quickstart Guide

### Problem

Understanding Agent Maestro currently requires reading across governance docs, concept definitions, pattern descriptions, system maps, and pipeline definitions spread across dozens of files. There is no single entry point for a new reader.

### Proposal

Create a single "Quickstart" document that walks a reader through building their first constellation in under 30 minutes, using the Vault Curator as the example.

### Document Structure

```
02_KNOWLEDGE/system_maps/Agent Maestro — Quickstart.md
```

**Contents:**

1. **What is Agent Maestro?** — 3 sentences from the North Star, no jargon
2. **The three things you need to know** — Authority Packs, Constellations, The Compiler. One paragraph each.
3. **Build your first constellation (Vault Curator):**
   - Step 1: Read the Executive authority pack (link to file, explain each section)
   - Step 2: Read the Specialist authority pack (show how it inherits from Executive)
   - Step 3: Run the compiler (command line, show input and output)
   - Step 4: Read the compiled artifact (explain what changed)
   - Step 5: Trace an escalation path (walk through the Link Auditor example)
4. **Where to go next** — Links to the Navigation Map, Principles, and the full constellation docs
5. **Glossary** — 10 key terms with one-line definitions and links to full concept notes

### Design Principles for the Quickstart

- No term is used before it is defined
- Every section links to the deeper vault note for readers who want more
- The entire document can be read in 10 minutes
- It uses a single concrete example throughout (no abstract descriptions)

---

## Improvement 6 — Principles Prioritisation

### Problem

The 12 principles are presented as a flat list of equal weight. A practitioner starting from scratch doesn't know which ones to apply first.

### Proposal

Add a tiered structure to [[Agent Maestro — Principles]] without changing the principles themselves.

### Tier Structure

**Tier 1 — Foundation (apply these first, they are non-negotiable)**

| # | Principle | Why it's foundational |
|---|---|---|
| 1 | [[Governance Before Autonomy]] | Without this, nothing else in the framework applies |
| 2 | Authority Over Intelligence | This is the core thesis of Agent Maestro |
| 7 | [[Human Escalation Pattern]] | Safety boundary — humans must retain final authority |
| 4 | Transparency by Design | You cannot govern what you cannot observe |

**Tier 2 — Architecture (apply these when designing systems)**

| # | Principle | When it applies |
|---|---|---|
| 3 | [[Deterministic Control Surfaces]] | When defining agent actions and outputs |
| 5 | Intelligence Through Constraints | When scoping agent authority |
| 6 | [[Three-Layer Memory Model]] | When designing memory and knowledge systems. Note: the architectural principle remains three layers (Knowledge Graph, Vector Memory, Structured Data) even though the current implementation operates two active layers, with the Vector Memory Layer architecturally planned. See Improvement 4C. |
| 8 | Composable Architecture | When structuring multi-agent systems |

**Tier 3 — Evolution (apply these when operating and scaling)**

| # | Principle | When it applies |
|---|---|---|
| 9 | [[Evidence Over Assumptions]] | When evaluating system behaviour |
| 10 | Real Systems First | When validating designs |
| 11 | [[Controlled Evolution Pattern]] | When upgrading or expanding systems |
| 12 | [[Anti-Agent-Sprawl Pattern]] | When scaling the number of agents |

**Implementation:** Add the tier structure as a new section in [[Agent Maestro — Principles]], above the existing flat index. The flat index remains for reference. The tiered view becomes the primary reading path.

---

## Improvement 7 — CLAUDE.md Governance Files

### Problem

When an AI agent (Claude or any future agent) works inside the Agent Maestro vault, it has no structured guidance about what each folder contains, what conventions to follow, or what operations are permitted. The agent must infer context from file contents, which is slow, error-prone, and ungoverned.

### Proposal

Place a `CLAUDE.md` file in the most critical directories. A `CLAUDE.md` file is a lightweight governance contract for AI agents working in that directory — it tells the agent what the folder is for, what files belong here, what naming and formatting conventions to follow, and what the agent should and should not do.

This is Agent Maestro's own governance philosophy applied to itself: governance before autonomy. Before an agent touches a folder, a contract exists defining the rules.

### Where CLAUDE.md Files Will Be Placed

**Root level:**

| Location | Purpose |
|---|---|
| `CLAUDE.md` (vault root) | Top-level orientation: what Agent Maestro is, vault structure overview, global conventions (frontmatter schema, naming, linking), and pointers to key governance docs |

**Top-level numbered folders:**

| Location | Purpose |
|---|---|
| `01_CAPTURE/CLAUDE.md` | Explains this is the inbox for raw input; notes here are unsorted and unvalidated; agent should not modify existing captures without escalation |
| `02_KNOWLEDGE/CLAUDE.md` | Explains this is the authoritative knowledge base; notes must conform to governance schema; changes to canonical notes require review |
| `03_PIPELINES/CLAUDE.md` | Explains these are operational workflows; pipelines define stage sequences; agents should follow pipeline contracts |
| `04_PROJECTS/CLAUDE.md` | Explains project lifecycle (incubating → active → completed); project notes track deliverables |
| `05_SYSTEMS/CLAUDE.md` | Explains this contains implementation-level architecture; the most governance-sensitive area; changes here affect system behaviour |
| `06_EXECUTION/CLAUDE.md` | Explains this contains dashboards, logs, reports, and task tracking; agents write operational data here |
| `99_ARCHIVE/CLAUDE.md` | Explains archived items are read-only; agents should not modify archived notes |

**Critical subdirectories:**

| Location | Purpose |
|---|---|
| `05_SYSTEMS/authority_architecture/CLAUDE.md` | Authority pack conventions, compiler usage, pack versioning rules |
| `05_SYSTEMS/authority_architecture/compiler/CLAUDE.md` | Compiler inputs/outputs, how to run the compiler, artifact registration |
| `05_SYSTEMS/memory_architecture/CLAUDE.md` | Memory layer responsibilities, CSV conventions, knowledge graph conventions |
| `02_KNOWLEDGE/governance/CLAUDE.md` | These are the highest-authority documents in the vault; changes require explicit human approval |

### CLAUDE.md Template Structure

Each `CLAUDE.md` follows a consistent structure:

```markdown
# {Folder Name}

## Purpose
What this folder contains and why it exists.

## Conventions
- Naming conventions for files in this folder
- Required frontmatter fields
- Linking conventions

## Agent Rules
- What an agent MAY do in this folder
- What an agent MUST NOT do without escalation
- What outputs belong here vs. elsewhere

## Key Files
Links to the most important files in this directory.
```

### Relationship to Authority Packs

`CLAUDE.md` files are not authority packs — they are simpler and more immediately actionable. Think of them as the "quick briefing" an agent gets before entering a room, while authority packs are the full legal contract governing what happens inside. When the Vault Curator constellation is running, agents will have both: the CLAUDE.md for orientation and the compiled authority pack for enforcement.

---

## Improvement 8 — Agent Maestro Layer Model and Model Workspace Protocol

### Problem

Agent Maestro defines what agents are governed by (authority packs) and what they conceptually do (constellations, roles), but does not define how they actually run. There is no runtime model connecting governance intent to execution mechanics.

### Proposal

Introduce the **Agent Maestro Layer Model** — a four-layer runtime architecture — and the **Model Workspace Protocol (MWP)** — a standardised workspace structure that every agent execution operates within.

### The Four-Layer Model

```
Authority Layer      →  What may happen
     ↓
Agent Runtime        →  Who does it
     ↓
Workflow Layer       →  In what order
     ↓
Workspace Layer      →  Where it happens
```

**Authority Layer:** The governance surface. Contains authority packs (design-time) and compiled governance artifacts (runtime). This layer already exists in the vault under `05_SYSTEMS/authority_architecture/`. The Authority Layer answers: what is this agent permitted to decide? What is it permitted to execute? Under what conditions? With what evidence?

**Agent Runtime:** The execution surface. Contains agent definitions, constellation structures, and the Executive-Supervisor-Specialist hierarchy. This layer already exists conceptually in `05_SYSTEMS/agent_systems/`. The Agent Runtime answers: which agent is active? What role does it hold? Who does it report to? Who does it delegate to?

**Workflow Layer:** The orchestration surface. Contains stage definitions, pipeline sequences, and task contracts. This layer already exists in `03_PIPELINES/`. The Workflow Layer answers: what stage is this execution in? What comes next? What are the entry and exit conditions?

**Workspace Layer:** The operational surface. This is the new layer. It defines the physical file structure an agent works within during execution. The Workspace Layer answers: what files does this agent have access to? Where does it read authority? Where does it write artifacts?

### Model Workspace Protocol (MWP)

Every agent execution operates within a workspace that follows the MWP structure:

```
workspace/
   authority/       # Compiled authority pack for this agent
   agents/          # Agent definition and role contract
   stages/          # Current workflow stage contract
   references/      # Reference knowledge the agent needs
   artifacts/       # Working outputs produced by the agent
```

**At execution start, the agent loads:**

| What | From | Purpose |
|---|---|---|
| Authority pack | `authority/` | Defines what the agent may do |
| Stage contract | `stages/` | Defines what the agent should do right now |
| Reference knowledge | `references/` | Context the agent needs to reason |
| Working artifacts | `artifacts/` | Previous outputs or inputs to work with |

**At execution end, the agent produces:**

| What | To | Purpose |
|---|---|---|
| Output artifacts | `artifacts/` | The work product |
| Execution log | `artifacts/logs/` | Audit trail of what happened |
| Escalation requests | `artifacts/escalations/` | Decisions that exceeded authority |

### Why MWP Matters

MWP makes every agent execution **self-contained and auditable**. After an agent runs, you can inspect its workspace to see exactly what authority it operated under, what knowledge it had, what stage it was in, and what it produced. This is Principle 4 (Transparency by Design) made concrete at the filesystem level.

MWP also makes agent executions **reproducible**. Given the same workspace inputs (authority pack, stage contract, references), the same agent should produce the same outputs. This is Principle 3 (Deterministic Control Surfaces) made concrete.

### Implementation in the Vault

**New documentation:**

| Deliverable | Location |
|---|---|
| Layer Model concept note | `02_KNOWLEDGE/concepts/Agent Maestro Layer Model.md` |
| MWP concept note | `02_KNOWLEDGE/concepts/Model Workspace Protocol.md` |
| MWP pattern note | `02_KNOWLEDGE/patterns/Model Workspace Protocol Pattern.md` |
| Layer Model system map | `02_KNOWLEDGE/system_maps/Agent Maestro — Layer Model Map.md` |
| Workspace Layer architecture | `05_SYSTEMS/infrastructure/Workspace Layer.md` |

**Reference implementation:** The Vault Curator constellation (Improvement 1) will use MWP. Each specialist agent's execution will follow the workspace structure, creating a concrete example of the protocol in action.

**Example: Link Auditor workspace**

```
vault_curator/workspaces/link_auditor/
   authority/
      link_auditor_compiled.json     # Compiled authority pack
   agents/
      link_auditor.md                # Agent definition
   stages/
      audit_stage.md                 # Current stage contract
   references/
      vault_file_index.csv           # List of all vault files
   artifacts/
      link_audit_report.csv          # Output report
      logs/
         execution_log.csv           # What the agent did
      escalations/
         broken_links_requiring_deletion.md   # Escalated to Supervisor
```

### Relationship to Existing Architecture

The Layer Model does not replace existing concepts — it organises them into a runtime stack:

| Existing Concept | Layer Model Position |
|---|---|
| Authority Packs, Compiler, Governance | Authority Layer |
| Constellations, Agent Roles, Escalation | Agent Runtime |
| Pipelines, Stages | Workflow Layer |
| **MWP (new)** | **Workspace Layer** |

---

## Implementation Order

The improvements have dependencies. The recommended build order is:

```
Phase 1: Foundation
  ├── Improvement 6 — Principles Prioritisation (no dependencies, quick win)
  ├── Improvement 8 — Layer Model + MWP concept notes (establishes runtime model)
  ├── Improvement 4B — Structured Data CSV conventions (establishes data layer)
  └── Improvement 4A — Knowledge Graph population (establishes knowledge layer)

Phase 2: Governance + Tooling
  ├── Improvement 7 — CLAUDE.md files (governs the workspace before agents run)
  ├── Improvement 3 — Link Auditor + Schema Validator scripts
  └── Improvement 2 — Authority Pack Compiler prototype

Phase 3: Integration
  ├── Improvement 1 — Vault Curator reference constellation (with MWP workspaces)
  │     (uses the compiler from Phase 2, produces data in the CSVs from Phase 1,
  │      operates within CLAUDE.md-governed folders, follows MWP workspace structure)
  └── Improvement 5 — Quickstart Guide
        (references the working Vault Curator example from this phase)
```

**Estimated effort:**

| Phase | Improvements | Estimated Effort |
|---|---|---|
| Phase 1 | 6, 8, 4B, 4A | Foundation — establishes all conceptual and data infrastructure |
| Phase 2 | 7, 3, 2 | Governance + Tooling — CLAUDE.md files and Python scripts |
| Phase 3 | 1, 5 | Integration — brings everything together into a working system |

---

## Success Criteria

The improvements are complete when:

1. A reader can follow the Quickstart guide from zero to a compiled constellation without external help
2. The compiler successfully processes the Vault Curator authority packs and produces valid JSON artifacts
3. The link auditor reports zero broken links in the vault
4. The knowledge graph CSV contains every relationship defined in frontmatter across all notes
5. All structured data CSVs open correctly in Google Sheets with no formatting issues
6. The principles document has a clear tiered reading path
7. CLAUDE.md files exist in all top-level folders and critical subdirectories
8. The Vault Curator specialists run as Python scripts within MWP-structured workspaces
9. The Layer Model concept note accurately maps all existing vault concepts to the four layers

---

## Design Decisions (Resolved)

The following questions were raised during proposal drafting and have been resolved:

**1. Compiler dependencies: Use `pyyaml` and `jsonschema`.**

The compiler's job is to validate governance — it should use proven validation tools. Reimplementing YAML parsing and JSON Schema validation in pure Python introduces bugs into the governance layer itself, violating Principle 3 (Deterministic Control Surfaces). Both libraries are standard, well-maintained, and pip-installable.

**2. Knowledge Graph CSV: Generated by script on demand.**

A committed CSV drifts from actual frontmatter the moment someone edits a note and forgets to regenerate. A script that produces a fresh index guarantees accuracy every time. The script becomes one of the Vault Curator specialist tools — the knowledge graph export is itself a governed operation.

**3. Vault Curator specialists: Implemented as runnable Python scripts with authority packs.**

The authority packs define what the agents *may* do. The scripts implement what they *actually* do. Without scripts, the reference implementation is more documentation describing documentation — it would not prove the framework works. With scripts, you can run `python link_auditor.py`, see it check its authority pack, execute within its bounds, and produce a CSV report. That is the difference between a theoretical framework and an operational one.
