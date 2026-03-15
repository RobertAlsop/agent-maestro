---
schema_version: 2
title: "AM — Wave 5 — Proposal v3"
type: proposal
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 70
resolution_basis: authority_weight
status: draft
review_status: draft
version: 3
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Wave 5]]"
  part_of:
    - "[[Agent Maestro — Evolution Roadmap v0.5.0]]"
  implements:
    - "[[Build Session Protocol]]"
    - "[[Consolidation Pipeline]]"
    - "[[Agent Maestro — Foundations]]"
  governs: []
  applies_to: []
  uses:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Wave 5 — Treatise on Core Principles]]"
    - "[[AM — Wave 5 — Foundational Brainstorm]]"
  produces:
    - "[[v0.5.0 Release]]"
  supersedes:
    - "[[AM — Wave 5 — Proposal v1]]"
  superseded_by: []
tags:
  - proposal
  - wave-5
  - consolidation
  - alignment
  - v0.5
hash: ""
---

# AM — Wave 5 — Proposal v3

**Date**: 2026-03-15
**Authors**: Rob + Claude (Opus)
**Status**: DRAFT — Awaiting Approval
**Starting version**: v0.4.0
**Target version**: v0.5.0
**Supersedes**: AM — Wave 5 — Proposal v1 (operational-first), v2 (audited but pre-foundations)

---

## 1. Perception — Where Are We?

### The Question This Wave Answers

*Is every part of Agent Maestro in alignment with its core principles?*

The original Wave 5 question was "does Agent Maestro carry anything it doesn't need?" — an operational question. This revised proposal elevates the question to the conceptual level. Operational leanness follows from conceptual alignment. If everything in the vault serves the foundations, nothing unnecessary survives.

### What Changed Since v2

The Foundational Brainstorm and Treatise on Core Principles established a new kernel for Agent Maestro: three seeds (Process, Structure, Constraint), one meta-principle (Fractal Design), and three laws (Direction of Authority, Action Properties, Economy). Five derived principles replace the original twelve. A Foundations document (authority_weight: 95) now sits at the top of the governance hierarchy.

This changes the nature of Wave 5. Instead of an operational consolidation (audit notes, retire pipelines, build scripts), Wave 5 becomes a **systematic alignment pass** — walking through every folder, every level, every document in the vault and checking it against the new foundations. Operational work (scripts, pipeline rationalization, template creation) happens as a consequence of that alignment pass, not as a separate concern.

### Current State

| Dimension | Count | Note |
|-----------|-------|------|
| Governance documents | 8 | 6 original + Foundations (new, authority_weight 95) + Note Quality Rules |
| Knowledge docs (02_KNOWLEDGE) | ~40+ | System maps, concepts, references, indexes — need alignment check |
| Pipelines (03_PIPELINES) | 8 | 7 original + Consolidation Pipeline (new) |
| Projects (04_PROJECTS) | 1 active | agent_maestro_development — needs subfolder standardization |
| Systems (05_SYSTEMS) | Runtime, authority architecture, agent systems | Most complex layer — needs deep alignment check |
| Execution (06_EXECUTION) | Logs, reports, dashboards, workflows | Operational layer — needs alignment check |
| Templates (88_TEMPLATES) | ~20+ | Recently added note templates used to build AM — need alignment check against Foundations |
| Capture (01_CAPTURE) | 0 | Cleared — templates were the last items |
| Archive (99_ARCHIVE) | Read-only reference | Needs inventory but no alignment changes |

---

## 2. Interpretation — What Must Be Done?

### The Alignment Pass

Wave 5 is a single, systematic pass through the entire vault, checking every component against the foundations. The pass visits every canonical folder in order, applying the three audit types (Alignment, Integrity, Viability) at each stop.

The pass proceeds top-down through the vault's authority hierarchy — highest authority first, lowest last — because purpose descends (Law 1). You establish the standard before measuring against it.

### Vault Walk Order

```
Layer 1 — Governance (02_KNOWLEDGE/governance/)
  Foundations.md is the new apex. Do the remaining governance docs
  align with it? Are any redundant with each other or with Foundations?

Layer 2 — Knowledge (02_KNOWLEDGE/ — all subfolders)
  System maps, concepts, references, indexes.
  Does every document serve a declared purpose?
  Are relationships correct? Is anything duplicated or stale?

Layer 3 — Pipelines (03_PIPELINES/ — all subfolders)
  Is every pipeline operational or explicitly planned?
  Does each pipeline follow the Process seed (Irreducible Loop)?
  Can any be merged or retired?

Layer 4 — Projects (04_PROJECTS/)
  Standardize subfolder structure (briefs, proposals, audits,
  contracts, summaries, brainstorms).
  Move roadmaps to 02_KNOWLEDGE/strategy/.

Layer 5 — Systems (05_SYSTEMS/ — all subfolders)
  Runtime, authority architecture, agent systems, templates.
  Does each component address the Structure seed's seven primitives?
  Is the authority architecture consistent with the Constraint seed?
  Are templates aligned with the foundations?

Layer 6 — Execution (06_EXECUTION/)
  Logs, reports, dashboards, workflows.
  Is the logging infrastructure consistent with Law 2 (verifiable,
  reversible, accountable)?

Layer 7 — Infrastructure files
  Root CLAUDE.md, subdirectory CLAUDE.md files, .gitignore,
  runtime configuration.
  Does CLAUDE.md accurately reflect the current system?

Layer 8 — Templates (88_TEMPLATES/)
  The recently added note templates that were used to build Agent Maestro.
  Do templates embed the Structure seed's seven primitives?
  Are templates aligned with Foundations?
  Is the template set minimum viable? Any gaps? Any redundancy?
  This layer is critical — templates are how Fractal Design becomes operational.

Layer 9 — Archive (99_ARCHIVE/)
  Quick inventory. No changes — read-only by convention.
```

### What the Pass Produces at Each Layer

At every layer, the alignment pass produces:

1. **Alignment verdict** — Does each component serve what's above it? (Law 1)
2. **Integrity verdict** — Is each component internally sound? References valid, relationships correct, no contradictions? (Seed 2)
3. **Viability verdict** — Is each component earning its place? Minimum viable? (Law 3)
4. **Action list** — What changes are needed? (keep / simplify / merge / archive / create)
5. **State change log entries** — Every modification logged (Law 2)

### Concurrent Workstreams

Three workstreams run alongside the alignment pass:

**W1 — Shell Script Toolkit**
Priority 1 scripts (frontmatter validator, link integrity checker, orphan note detector) are built in the first session. They serve as deterministic tools during the alignment pass itself. Priority 2 scripts and the LLM/script boundary document come after the pass.

**W2 — Template Formalization**
As the pass reveals what templates are needed, they are created. The priority order from the Treatise: note template, pipeline template, project template, audit template, agent template, brainstorm template, authority pack template.

**W3 — Structural Changes**
Project subfolder standardization, roadmap relocation, naming convention migration, Build Session Protocol updates (brainstorm stage, foundation references). These happen when the pass reaches the relevant layer.

---

## 3. Decision — The Deliverables

### Phase 1: Foundation Lock + Tooling (Session N)

| Item | Description | Effort |
|------|-------------|--------|
| 1a. Baseline inventory | Complete vault inventory: note count by folder, by authority weight tier, by type. The "before" snapshot | Small |
| 1b. Foundation integration | Add D6 (Separation of Powers) to Foundations.md. Ensure Foundations.md is cross-referenced from root CLAUDE.md and all governance-adjacent files | Small |
| 1c. Priority 1 shell scripts | Build frontmatter validator, link integrity checker, orphan note detector. Accept vault root as argument, produce structured output | Large |
| 1d. Audit framework | Define the alignment pass rubric: for each of the three audit types, what specific checks apply at each vault layer? Produce as a reference checklist | Medium |
| 1e. Naming convention migration | Rename existing Wave 5 artifacts to `AM — Wave 5 — [Type].md` pattern. Establish convention for all future artifacts | Small |

**Exit**: Foundations locked, tools built, rubric defined, naming standardized. Ready to walk the vault.

### Phase 2: Governance Alignment (Session N+1)

| Item | Description | Effort |
|------|-------------|--------|
| 2a. Alignment pass — Layer 1 (Governance) | Apply three audits to every governance doc: Principles, Vault Rules, Modes, Scope, Strategy, Note Quality Rules. Each doc checked against Foundations.md. Produce verdicts + action list | Large |
| 2b. Governance reconciliation proposal | Based on 2a: which docs merge, simplify, keep, archive? How do the 5 derived principles replace the 12? Concrete proposal. **Human approval required** | Medium |
| 2c. Execute approved reconciliation | Apply changes. Update all references. Run frontmatter validator + link integrity checker to verify | Medium |

**Exit**: Governance layer fully aligned with Foundations. All governance docs earn their place. No redundancy between docs or with CLAUDE.md files.

### Phase 3: Knowledge + Pipeline Alignment (Session N+2)

| Item | Description | Effort |
|------|-------------|--------|
| 3a. Alignment pass — Layer 2 (Knowledge) | Walk every subfolder of 02_KNOWLEDGE: system maps, concepts, references, indexes. Three audits per document. Archive or simplify as needed | Large |
| 3b. Alignment pass — Layer 3 (Pipelines) | Classify all 8 pipelines: operational, planned, aspirational. Retire aspirational. Validate surviving pipelines against Process seed (do they follow the Irreducible Loop?) | Medium |
| 3c. Create strategy subfolder + relocate roadmaps | Create 02_KNOWLEDGE/strategy/, move roadmaps, update all references | Small |
| 3d. Pipeline template creation | Formalize a pipeline template based on the Process seed and the Consolidation Pipeline as exemplar | Small |

**Exit**: Knowledge base lean and aligned. Pipeline set minimized. Roadmaps relocated. Pipeline template established.

### Phase 4: Systems Alignment (Session N+3)

| Item | Description | Effort |
|------|-------------|--------|
| 4a. Alignment pass — Layer 5 (Systems: runtime) | Review 8 Python runtime modules against Constraint seed and Structure seed. Do they implement the authority hierarchy correctly? Do they address all seven primitives? | Large |
| 4b. Alignment pass — Layer 5 (Systems: authority architecture) | Review all 29 authority packs and compiler artifacts. Are they consistent with Foundations? Is the Constraint seed's chain rule enforced? | Large |
| 4c. Alignment pass — Layer 5 (Systems: agent systems) | Review constellations and agent registry. Archive vault_curator. Assess: what is the minimum viable constellation set? (Treatise suggests 3: Maintenance, Governance, Evolution) | Medium |
| 4d. Alignment pass — Layer 8 (Templates: 88_TEMPLATES/) | Review existing note templates. Do they embed the Structure seed's seven primitives? Are any redundant or missing? Align with Foundations | Medium |
| 4e. Template reconciliation | Reconcile existing 88_TEMPLATES/ with the new template needs identified by the Treatise. Update, merge, or create templates as needed. Formalize note template, agent template, authority pack template | Medium |

**Exit**: Systems layer and templates fully audited. Runtime, authority architecture, and agent systems aligned with Foundations. Templates reconciled with Foundations and formalized.

### Phase 5: Execution + Infrastructure Alignment (Session N+4)

| Item | Description | Effort |
|------|-------------|--------|
| 5a. Alignment pass — Layer 6 (Execution) | Review logs, reports, dashboards, workflows. Is logging consistent with Law 2? Are dashboards serving their declared purpose? | Medium |
| 5b. Alignment pass — Layer 4 (Projects) | Standardize project subfolder structure (6 folders). Create project template. Apply to active project | Medium |
| 5c. Alignment pass — Layer 7 (Infrastructure) | Update root CLAUDE.md and all subdirectory CLAUDE.md files to reflect Foundations, new stage count, naming conventions | Medium |
| 5d. Archive inventory — Layer 8 | Quick inventory of 99_ARCHIVE. No changes. Record what's there | Small |
| 5e. Build Session Protocol update | Add Brainstorm stage (Stage 10). Add explicit Irreducible Loop mapping. Reference Foundations | Small |

**Exit**: All vault layers visited. Infrastructure files current. Project structure standardized.

### Phase 6: Completion (Session N+5)

| Item | Description | Effort |
|------|-------------|--------|
| 6a. Priority 2 shell scripts | Authority weight distribution report, relationship completeness check (if time permits) | Medium |
| 6b. LLM/script boundary document | Reference doc in 02_KNOWLEDGE mapping every maintenance operation to its executor with rationale | Small |
| 6c. Script integration with logging | Both script and LLM execution paths report through same infrastructure | Medium |
| 6d. Consolidation Pipeline validation | Compare the abstract pipeline against the actual work performed. Update pipeline with lessons learned | Medium |
| 6e. Final audit report | Before/after metrics against baseline. Every layer's verdicts. Changes made, items archived, templates created | Medium |
| 6f. Foundations.md review | Final check: after walking the entire vault, does Foundations.md still feel right? Any refinements? | Small |

**Exit**: Wave 5 complete. v0.5.0 ready.

---

## 4. Validation — Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Over-pruning during alignment pass | Medium | Archive over delete (Law 2 — reversible). Tag archived items with `archive_reason`. Git checkpoint before each phase |
| Governance reconciliation breaks downstream references | High | Run link integrity checker immediately after changes (Phase 2c). Git checkpoint tag before reconciliation |
| Alignment pass takes longer than estimated | Medium | Each phase is independently valuable. If a phase runs long, it can spill into a follow-up session without blocking later phases (except Phase 2 must complete before Phase 3) |
| Templates formalized prematurely before full alignment pass reveals what's needed | Medium | Templates are created at the phase where they're needed. Note template in Phase 4 (after seeing all note types). Pipeline template in Phase 3 (after pipeline rationalization) |
| Shell scripts don't cover edge cases in vault | Low | Scripts are validation tools, not enforcement. LLM judgment handles edge cases. Scripts flag; humans decide |
| Alignment pass produces too many changes to track | Medium | State change log captures every modification (Law 2). Each phase produces a summary. Final audit report aggregates everything |

---

## 5. Design Decisions

**D1. Alignment before operations.** The systematic alignment pass (conceptual audit) comes before any operational work. You cannot optimize what isn't aligned.

**D2. Top-down vault walk.** The alignment pass proceeds from highest authority (governance) to lowest (execution, infrastructure). Purpose descends (Law 1) — establish the standard before measuring against it.

**D3. Three audits at every stop.** Every component gets all three checks: Alignment (serves what's above), Integrity (internally sound), Viability (earns its place). No exceptions, no shortcuts.

**D4. Archive over delete.** Default action for content that fails the Viability audit is archive, not delete. Reversible (Law 2). Items tagged with `archive_reason`.

**D5. Human gate on governance changes.** Phase 2 produces a reconciliation proposal (2b) requiring human approval before execution (2c). Governance changes at authority_weight ≥ 80 must be human-authorized.

**D6. Front-load deterministic tools.** Priority 1 scripts built in Phase 1, used throughout the alignment pass. The tools serve the process that creates them.

**D7. Templates emerge from the pass.** Templates are created at the phase where they're most informed — after the alignment pass reveals the actual needs, not before.

**D8. Validate the fractal.** Phase 6d compares the Consolidation Pipeline against actual work. The pipeline is updated with lessons learned to ensure genuine reusability.

**D9. Separation of Powers noted.** To be added as D6 to Foundations.md during Phase 1 (item 1b). Derived from Seed 3 + Law 1: different functions within the authority hierarchy must be held by different actors.

---

## 6. Exit Criteria

Wave 5 is complete when:

1. **Every vault layer visited** — The alignment pass has walked through all 9 layers (Governance, Knowledge, Pipelines, Projects, Systems, Execution, Infrastructure, Templates, Archive). Every component has received Alignment, Integrity, and Viability verdicts.

2. **Governance aligned** — All governance documents reconciled with Foundations.md. The 5 derived principles replace the 12. No redundancy between governance docs or with CLAUDE.md files. Documented rationale for every keep/merge/simplify/archive decision.

3. **Knowledge base lean** — Every knowledge document earns its place. Stale, duplicated, or orphaned content archived with rationale. System maps accurate.

4. **Pipelines minimized** — Only operational and explicitly planned pipelines survive. Each follows the Process seed. Pipeline template established.

5. **Systems aligned** — Runtime, authority architecture, and agent systems consistent with Foundations. vault_curator archived. Minimum viable constellation set identified.

6. **Execution layer consistent** — Logging infrastructure conforms to Law 2. Project subfolder structure standardized.

7. **Infrastructure current** — All CLAUDE.md files reflect Foundations, current protocols, and naming conventions.

8. **Shell script layer operational** — At least 3 deterministic maintenance scripts implemented, tested, and integrated with logging. LLM/script boundary documented.

9. **Templates created** — Minimum viable template set formalized: note, pipeline, project, audit (at least).

10. **Consolidation Pipeline validated** — Abstract pipeline compared against actual work and updated with lessons learned.

11. **Audit report published** — Before/after metrics, layer-by-layer verdicts, changes made, items archived, templates created.

12. **Git release** — All changes committed, tagged as v0.5.0.

---

## 7. Build Order Summary

```
Phase 1 (Session N):     Foundation lock + tooling + baseline
Phase 2 (Session N+1):   Governance alignment (human approval gate)
Phase 3 (Session N+2):   Knowledge + pipelines alignment
Phase 4 (Session N+3):   Systems alignment (deepest layer)
Phase 5 (Session N+4):   Execution + infrastructure + projects
Phase 6 (Session N+5):   Completion — scripts, boundary doc, pipeline validation, report
```

**Total estimated sessions**: 6
**Version target**: v0.5.0 after Phase 6

Each session follows the Build Session Protocol (all 10 stages when applicable) and includes a workflow extraction checkpoint.

---

## 8. What This Unlocks

A vault in full alignment with its foundations is the prerequisite for everything that follows. Wave 6 (Living System) depends on a clean, consistent vault — autonomous maintenance on misaligned content amplifies problems. Wave 7 (Self-Improving) depends on the Evolution Constellation having clean signals to analyze. Wave 8 (Vault Architect) depends on Agent Maestro's own vault being the exemplar it offers to others.

The alignment pass itself is a fractal capability: the same process (parameterized through the Consolidation Pipeline) will be used on external vaults in Wave 8. The templates formalized during this wave become the templates offered to external vault users. The audit methodology becomes the audit service.

Building inward is building outward.

---

**Awaiting approval before any build work begins.**
