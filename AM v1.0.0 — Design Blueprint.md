# Agent Maestro v1.0.0 — Design Blueprint

**Status:** DRAFT — Proposal for review
**Created:** 2026-03-16
**Authors:** Rob + Claude (Wave 5.1 collaborative design session)
**Derives from:** Agent Maestro — Foundations (authority_weight: 95)

---

## 1. What Agent Maestro Is

Agent Maestro is the discipline of designing, governing, and evolving operational intelligence systems. Its mission is not to create smarter AI — it is to create **more reliable intelligent systems**.

This blueprint defines the minimum viable architecture for AM v1.0.0 — the first version where the system can govern itself, run real workflows, and begin to self-improve.

## 2. Design Principles Applied

Every decision in this blueprint traces back to the Foundations:

- **Law 3 (Economy):** Only what is necessary. Every component earns its place.
- **Fractal Design (Meta-Principle):** The same pattern applies at every level of abstraction. The vault IS the pipeline. The pipeline IS the workflow.
- **Seed 3 (Constraint):** Every action passes through an authority hierarchy. No stage transitions without gates.
- **Law 1 (Direction of Authority):** Purpose descends from the human. Accountability ascends to the human.
- **D6 (Separation of Powers):** The entity that proposes must not approve. The entity that executes must not audit.

## 3. Goals — Three Capability Layers

AM v1.0.0 must demonstrate three capabilities, in order. Each layer proves the one before it.

| Layer | Capability | What it proves |
|-------|-----------|----------------|
| 1 | **Govern itself** | AM can maintain its own vault, enforce its own rules, validate its own integrity |
| 2 | **Run real workflows** | AM can execute actual agent pipelines against real tasks — not just describe how they would work |
| 3 | **Self-improve** | AM can audit itself, propose improvements, and implement them with human approval |

**Audience:** Rob + Claude now. Local LLMs very soon. Others eventually.

## 4. The Universal Pipeline

The core insight: Agent Maestro IS a pipeline. The vault structure mirrors the workflow. The same 6-stage pattern appears at every level of abstraction.

### 4.1 The Six Stages

| Stage | Function | Question it answers |
|-------|----------|-------------------|
| **Input** | Receive | What arrived? |
| **Interpret** | Understand | What does it mean? |
| **Decide** | Commit | What are we going to do? |
| **Act** | Execute | Do it. |
| **Record** | Remember | What happened? |
| **Reflect** | Learn | What did we learn? What's next? |

Between every stage: a **gate**. Nothing moves forward without a check. Gate intensity scales with what's at stake.

The loop closes: Reflect feeds back into Input. The brainstorm becomes the next brief. Evolution generates new captures.

### 4.2 Fractal Instantiation

The same pipeline at three scales:

| Stage | Irreducible Loop (Seed 1) | Build Session | AM Vault |
|-------|--------------------------|---------------|----------|
| Input | Perception | Idea / Brief | 01_CAPTURE |
| Interpret | Interpretation | Proposal | 02_KNOWLEDGE |
| Decide | Decision | Contract | 03_DECIDE |
| Act | Action | Build | 04_EXECUTE |
| Record | Memory | Summary | 05_RECORD |
| Reflect | Feedback | Brainstorm | 06_REFLECT |

### 4.3 Gate System

Gates are validation checks between pipeline stages. They use the three-level escalation model:

| Level | Trigger | Resolution |
|-------|---------|------------|
| **Level 1 — Automatic** | Rules cover it | Pass/fail against defined criteria. No judgment needed. |
| **Level 2 — Agent judgment** | Rules insufficient, but principles apply | Agent traces decision back to Foundations. Proceeds if traceable. |
| **Level 3 — Human approval** | Irreversible, architectural, or governance-level | Agent packages context and escalates. Human decides. |

The **adversarial audit** is a special form of gate — the highest-intensity validation, applied at the most critical transitions (e.g., proposal → contract for governance changes).

## 5. Vault Structure

The vault folders directly mirror the pipeline stages. **The vault IS the workflow.**

```
CLAUDE.md                      ← The Charter (entry point for any agent)

01_CAPTURE/                    ← INPUT: Raw ideas, observations, drafts, unsorted material
02_KNOWLEDGE/                  ← INTERPRET: Governance, concepts, references, patterns, skills, templates
    governance/                   Constitutional documents (canonical: true, authority_weight ≥ 80)
    concepts/                     Domain knowledge and frameworks
    references/                   External references and research
    skills/                       Skill definitions (the 7 core skills)
    templates/                    Patterns for creating artifacts
    indexes/                      Knowledge graph, registries, SYSTEM_MAP.md
03_DECIDE/                     ← DECIDE: Active projects, proposals, contracts, roadmaps
    active/                       Currently active projects and decisions
    proposals/                    Change proposals awaiting review
04_EXECUTE/                    ← ACT: Runtime, tools, active builds, working artifacts
    runtime/                      Python runtime code (governed_agent, orchestrator, etc.)
    tools/                        Utility scripts and infrastructure tools
    builds/                       Active build work in progress
05_RECORD/                     ← RECORD: Logs, reports, summaries, session history
    logs/                         Operational logs (task, escalation, state change, sessions)
    reports/                      Audit reports, summaries
    archive/                      Historical items (former 99_ARCHIVE)
06_REFLECT/                    ← REFLECT: Retrospectives, evolution proposals, brainstorms
    retrospectives/               Session retrospectives and learnings
    evolution/                    Proposed improvements and experiments
    brainstorms/                  Ideas for future work
```

**What was removed:**
- `03_PIPELINES/` → Pipeline definitions are KNOWLEDGE (patterns for how workflows work)
- `04_PROJECTS/` → Active projects move to DECIDE; completed projects move to RECORD
- `05_SYSTEMS/` → Dissolved entirely. Runtime code → EXECUTE. Concepts → KNOWLEDGE. Authority packs (130+ files) → replaced by simplified role definitions in KNOWLEDGE.
- `88_TEMPLATES/` → Absorbed into KNOWLEDGE/templates/
- `99_ARCHIVE/` → Absorbed into RECORD/archive/

**What was gained:**
- `06_REFLECT/` — a dedicated space for the feedback loop, which didn't previously exist as a vault concept

**Navigation:**
- `CLAUDE.md` is the **Charter** — what AM is, how it works, what the rules are. Stable.
- `02_KNOWLEDGE/indexes/SYSTEM_MAP.md` is the **Inventory** — a compact index of what currently exists in the vault. Updated with every structural change.
- The old 21 separate system maps are replaced by this single master map. The vault is now simple enough (6 folders) that one map suffices.

## 6. Authority Architecture

### 6.1 The Simplification

The current authority system (130+ files, 14-section packs, a compiler, inheritance trees) is replaced by three components:

1. **The Foundations** — Constitutional authority. Already exists. Already good. (authority_weight: 95)
2. **Role definitions** — One clear document per role in `02_KNOWLEDGE/governance/roles/`
3. **The escalation chain** — Three levels (see §4.3). Human at top. Always.

No compiler. No 14-section packs. No inheritance trees. These can be added later if they prove necessary — but they are not built until they earn their place (Law 3).

### 6.2 Decision-Making Model

| Decision type | Example | Resolution |
|---------------|---------|------------|
| Routine operational | Format a note, write a log | **Level 1** — rules cover it |
| Classification | Is this capture item knowledge or noise? | **Level 2** — agent applies Foundations |
| Architectural | Change vault structure, add a skill | **Level 3** — agent proposes, human decides |
| Governance | Change a principle, modify authority model | **Level 3 + full pipeline** — proposal → audit → human approval |
| Conflict resolution | Two principles seem to conflict | **Authority hierarchy** — higher-weight principle wins; if ambiguous → human |

## 7. Agent Architecture — Skills, Roles, Agents

### 7.1 Three-Layer Model

| Layer | What it is | How many | Where defined |
|-------|-----------|----------|---------------|
| **Skills** | Concrete capabilities — "how to do X" | 7 core skills | `02_KNOWLEDGE/skills/` |
| **Roles** | Authority boundaries — "what you're allowed to do" | 2 roles + Human | `02_KNOWLEDGE/governance/roles/` |
| **Agents** | Runtime instantiations — a model + a role + loaded skills | Created on demand | `04_EXECUTE/runtime/` |

**Key principle:** Agents are not pre-built permanent entities. They are instantiated when needed: pick a model, assign a role, load relevant skills, execute, dissolve. No elaborate hierarchies, no constellation maps, no executive layers.

### 7.2 The Seven Core Skills

| Skill | Purpose | Pipeline stages served |
|-------|---------|----------------------|
| **Triage** | Classify input and route through the pipeline | CAPTURE → KNOWLEDGE |
| **Validate** | Check any artifact against governance rules (schema, links, alignment) | All stages (used by Gate) |
| **Audit** | Deep evaluation — alignment (top-down), integrity (horizontal), viability (bottom-up). Parameterized: same skill, three lenses. | REFLECT + high-stakes gates |
| **Propose** | Formulate a change proposal with evidence and traceability to Foundations | DECIDE |
| **Gate** | Evaluate pipeline stage transitions: pass automatically, pass with judgment, or escalate | Between ALL stages |
| **Summarize** | Synthesize outcomes — session summaries, reports, decision records | RECORD |
| **Escalate** | Package a decision for human review with full context | Any stage (Level 3 trigger) |

Skills map to capability layers:
- **Layer 1 (Govern):** Validate + Gate + basic tools
- **Layer 2 (Workflows):** Triage + Gate + Summarize
- **Layer 3 (Self-improve):** Audit + Propose + Escalate

The **core questions library** is the Audit skill's question bank:
- Alignment: "Does this serve what's above it?"
- Integrity: "Is this internally sound and correctly connected?"
- Viability: "Is this earning its place? Could it be simplified?"

### 7.3 The Two Roles

```
HUMAN (ultimate authority — Level 3)
  │
  ├─ Reviewer (Level 2 authority)
  │    Purpose: Operate gates, audit, propose changes
  │    Skills: Audit, Gate, Validate, Propose, Escalate
  │    Cannot: Execute builds, modify artifacts directly
  │
  └─ Worker (Level 1-2 authority)
       Purpose: Execute pipeline stages, build artifacts
       Skills: Triage, Validate, Summarize, Gate (basic)
       Cannot: Approve own work, modify governance
```

**D6 compliance:** The same model can play both roles — but not for the same work in the same context. Build as Worker → review as Reviewer. Different role = different authority = separation of powers.

## 8. Document Schema v3

### 8.1 The Simplification

The current frontmatter schema (v2) has ~30 fields across 7 categories. Schema v3 reduces this to 9 fields. The key insight: **the folder structure now carries information that frontmatter used to carry.** A skill definition in `02_KNOWLEDGE/skills/` doesn't need a `layer: knowledge` field — its location tells you that.

### 8.2 Schema v3 — Canonical Template

```yaml
---
title: ""
type: ""               # governance | concept | skill | role | pipeline | log | report | proposal
status: ""             # draft | active | archived
authority_weight: 0    # 0-100 (the core governance mechanism; ≥80 = canonical)
schema_version: 3
created: ""            # ISO 8601
updated: ""            # ISO 8601
relationships:
  derives_from: []     # upward authority trace (what this implements/inherits)
  governs: []          # downward authority (what this controls)
  related: []          # everything else
tags: []
---
```

### 8.3 What Was Removed

| Removed field(s) | Reason |
|-------------------|--------|
| `id` | Filename IS the identifier |
| `note_class`, `domain`, `layer`, `scope` | Folder structure carries this information |
| `canonical` | Derived from authority_weight (≥80 = canonical) |
| `resolution_basis` | Always authority_weight; exceptions noted inline |
| `review_status`, `review_cycle`, `last_reviewed` | Over-engineered for current scale |
| `owner` | 2 roles, not a department structure |
| 5 navigation fields | Collapsed into `relationships.related` |
| 8 relationship types | Collapsed into 3 (`derives_from`, `governs`, `related`) |
| `hash` | Nobody was computing it |
| `source_type`, `supersedes`, `superseded_by` | Noted in document body when relevant |

### 8.4 Vault Rules Update

The Vault Rules document must be updated for v1.0.0 to reflect:
- New 6-folder structure (replacing references to old folders)
- Schema v3 (replacing schema v2 requirements)
- Removal of authority pack grammar rules (00-13 sections)
- Simplified template requirements (no longer 30+ templates)

Rules that survive unchanged:
- Every note must have frontmatter conforming to the schema
- Every note must have a Purpose section
- All wiki-links must resolve
- No orphan notes
- All dates in ISO 8601

## 9. What Gets Cut

Applying Law 3 (Economy) — components from the current vault that do not survive into v1.0.0:

| Current component | File count | Verdict | Reason |
|-------------------|-----------|---------|--------|
| Conceptual authority packs (14 sections × 8 domains) | ~112 | **Remove** | Replaced by simple role definitions |
| Authority pack compiler | ~15 | **Remove** | No packs to compile |
| Agent hierarchy (executive, supervisor, specialist definitions) | ~20 | **Remove** | Replaced by 2 roles + on-demand instantiation |
| Constellation system (maps, links, workflows per constellation) | ~15 | **Remove** | Unnecessary complexity for current scale |
| Memory architecture concepts (7 files) | 7 | **Evaluate** | Keep what's actionable, move to KNOWLEDGE/concepts |
| Infrastructure concepts (5 files) | 5 | **Evaluate** | Keep what's actionable, move to KNOWLEDGE/concepts |
| Organizational integration (4 files) | 4 | **Remove** | Future concern, not v1.0.0 |
| Operational intelligence (3 files) | 3 | **Evaluate** | May inform self-improvement skills |
| 30+ templates | ~35 | **Consolidate** | Keep only templates actually needed for v1.0.0 artifacts |

**Estimated reduction:** From ~284 files in 05_SYSTEMS alone to approximately 20-30 files across the entire vault's operational layer.

## 10. Migration Path

This blueprint does not describe a big-bang rebuild. It describes a target architecture. Migration happens in stages:

1. **Create new structure** — Set up the 6 pipeline folders alongside the existing structure
2. **Migrate governance first** — Move Foundations and governance docs to `02_KNOWLEDGE/governance/` (minimal change — they're already close)
3. **Write the skill definitions** — Create the 7 core skill documents in `02_KNOWLEDGE/skills/`
4. **Write role definitions** — Create Worker and Reviewer role docs in `02_KNOWLEDGE/governance/roles/`
5. **Migrate runtime** — Move functioning Python code to `04_EXECUTE/runtime/`
6. **Migrate records** — Move logs, reports, session history to `05_RECORD/`
7. **Audit remaining content** — Everything left goes through a viability audit: keep, move, or delete
8. **Clean up** — Remove empty old folders, update CLAUDE.md to reflect new structure

Each step is a gated pipeline stage: propose → validate → execute → record.

## 11. What Agent Maestro Defines (Refined)

From the original brainstorm note: "AM should define three things." Refined to:

1. **Workflow Architecture** — The universal 6-stage pipeline with gates. How work flows.
2. **Authority Architecture** — Roles, escalation levels, decision-making. Who decides what.
3. **Skill Architecture** — The capability library. What the system can do.

These three, plus the Foundations that govern all of them, constitute Agent Maestro.

## 12. Open Questions for Future Waves

These are important but deliberately deferred — they haven't earned their place in v1.0.0:

- **How should the skill library grow?** What's the process for proposing, testing, and approving new skills?
- **LLM-specific challenges:** Should AM's design account for hallucination, context window limits, inconsistency? (Yes, but as an extension to the Foundations, not a v1.0.0 requirement.)
- **Multi-model coordination:** When local LLMs join, how do they divide work? (The role system supports this, but the coordination protocol isn't needed until there are multiple models.)
- **Laws vs Rules boundary:** Where does the "constitution" end and the "law book" begin? (The current Foundations + role definitions may be sufficient. Revisit if the system grows.)
- **Self-improvement protocol:** The detailed process by which AM audits and improves itself. (Layer 3 capability — built after Layers 1 and 2 are proven.)

---

*This blueprint was produced through the collaborative design process that AM should eventually be able to perform autonomously: Input (Rob's brief) → Interpret (reading the vault together) → Decide (design choices through questions) → Act (this document) → Record (session log) → Reflect (next steps).*

*The process itself demonstrated the fractal principle: we used the pipeline to design the pipeline.*
