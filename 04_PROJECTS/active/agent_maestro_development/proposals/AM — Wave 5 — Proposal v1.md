---
schema_version: 2
title: "AM — Wave 5 — Proposal v1"
type: proposal
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 70
resolution_basis: authority_weight
status: draft
review_status: draft
version: 2
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: ai_authored
relationships:
  defines:
    - "[[Wave 5]]"
  part_of:
    - "[[Agent Maestro — Evolution Roadmap v0.5.0]]"
  implements:
    - "[[Build Session Protocol]]"
    - "[[Consolidation Pipeline]]"
  governs: []
  applies_to: []
  uses:
    - "[[Agent Maestro — Principles]]"
    - "[[Agent Maestro — Vault Rules]]"
  produces:
    - "[[v0.5.0 Release]]"
  supersedes: []
  superseded_by: []
tags:
  - proposal
  - roadmap
  - wave-5
  - consolidation
  - v0.5
hash: ""
---

# Agent Maestro v0.5 — Wave 5 Consolidation Proposal

**Date**: 2026-03-15
**Author**: Claude (Opus) + Rob
**Status**: DRAFT — Awaiting Approval
**Scope**: Wave 5 implementation — systematic consolidation of the Agent Maestro vault
**Starting version**: v0.4.0 (Phases A–D delivered)
**Target version**: v0.5.0

---

## Part 1: Strategic Context

### The Question This Wave Answers

*Does Agent Maestro carry anything it doesn't need?*

Wave 5 is the consolidation wave. Before the system becomes autonomous (Wave 6), self-improving (Wave 7), and externally capable (Wave 8), it must be lean. Every note must earn its place. Every governance document must pull its weight. Every pipeline must be operational or retired. The boundary between what scripts do and what LLMs do must be drawn clearly.

### Current State (v0.4.0)

| Dimension | Count | Observation |
|-----------|-------|-------------|
| Capture notes (01_CAPTURE) | 36 | Unprocessed; carried since early builds |
| Governance documents | 7 | 6 core (authority_weight 80–90) + Note Quality Rules |
| Pipelines | 7 definitions across 5 categories | Several aspirational, not yet invoked by workflows |
| Constellations | 2 (1 active, 1 deprecated) | vault_curator deprecated but not archived |
| Compiled authority packs | 17 artifacts | Registry previously fixed in v0.3 safety hardening |
| Runtime modules | 8 Python files | Functional but untested against a lean vault |

### This Proposal as Fractal Seed

This proposal is the first instantiation of the [[Consolidation Pipeline]] — the abstract, reusable process for systematically auditing and rationalizing any governed knowledge system. The specific work described below (vault paths, note counts, governance doc names) are parameters of that pipeline. The pipeline itself is designed to be re-run on this vault at future checkpoints, or on external vaults in Wave 8. A design constraint of this wave is that the abstract pipeline must be validated and updated based on lessons learned during execution (see Design Decision D6).

### Why Consolidation Before Autonomy

Principle 1 (Minimum Viable Everything) demands that we strip the vault to its essential weight before adding new capabilities. A system that runs autonomously on bloated, inconsistent, or duplicated content will propagate those problems at machine speed. Consolidation is the foundation Wave 6–8 stand on.

---

## Part 2: Deliverables

Wave 5 is organized into four workstreams matching the roadmap sections 5.1–5.4. Each workstream produces concrete, verifiable outputs.

### Pipeline-to-Workstream Mapping

This proposal is an instance of the [[Consolidation Pipeline]]. The pipeline's six abstract stages map to the proposal's workstreams as follows:

| Consolidation Pipeline Stage | Proposal Workstream(s) | Session(s) |
|------------------------------|----------------------|------------|
| Stage 1 — Audit Framework Setup | 5.1a (Baseline inventory) + 5.1a-1 (Audit framework) | N |
| Stage 2 — Governance Body Review | 5.2 (Governance Body Review) | N+1, N+2 |
| Stage 3 — Content Audit | 5.1b–5.1e (Tier audits + capture processing) | N+3, N+4 |
| Stage 4 — Pipeline Rationalization | 5.3 (Pipeline Rationalization) | N, N+2 |
| Stage 5 — Executor Boundary Definition | 5.4 (Shell Script Maintenance Layer) | N, N+5 |
| Stage 6 — Consolidation Report + Exit Criteria | 5.1f (Audit report) + Session N+6 (pipeline validation + close-out) | N+6 |

### Workstream 5.1 — Vault Quality Audit

**Goal**: Every vault note is reviewed, justified, and either improved or removed.

| Item | Description | Effort |
|------|-------------|--------|
| 5.1a. Baseline inventory | Establish complete vault inventory: total note count, distribution by folder, distribution by authority weight tier. This is the "before" baseline for the final audit report | Small |
| 5.1a-1. Audit framework | Define scoring rubric: accuracy, currency, necessity, duplication, authority weight correctness, relationship completeness | Small |
| 5.1b. Tier-1 audit (authority_weight ≥ 80) | Review the 6 core governance docs + any other high-authority notes. These set the standard for everything below | Medium |
| 5.1c. Tier-2 audit (authority_weight 50–79) | Review system maps, concepts, references, pipeline contracts. Flag duplicates and stale content | Large |
| 5.1d. Tier-3 audit (authority_weight < 50) | Review remaining notes. Aggressive pruning — archive or delete anything that doesn't earn its place | Medium |
| 5.1e. Process 36 capture notes | Classify, enrich, promote, or archive every note in 01_CAPTURE. This backlog predates v0.2 and must be resolved | Large |
| 5.1f. Audit report | Produce a formal audit report: notes reviewed, actions taken (kept/simplified/merged/archived/deleted), before/after metrics | Small |

**Success criteria**: Zero notes in 01_CAPTURE. Every surviving note has accurate frontmatter, correct relationships, and justified authority weight. Audit report written to 06_EXECUTION/reports/.

### Workstream 5.2 — Governance Body Review

**Goal**: The governance body is as concise as possible without losing precision.

| Item                                             | Description                                                                                                                                                                              | Effort |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 5.2a. Principles review                          | Evaluate whether 12 principles is the right number. Identify candidates for merging (e.g., do any overlap with each other or with Vault Rules?)                                          | Medium |
| 5.2b. Modes / Scope / Strategy review            | Do all three documents carry distinct, necessary content? Could any be folded into another?                                                                                              | Medium |
| 5.2c. Vault Rules vs. CLAUDE.md overlap analysis | Map every rule in Vault Rules against CLAUDE.md files. Identify redundancy. Recommend single-source-of-truth for each rule                                                               | Medium |
| 5.2d. Note Quality Rules assessment              | This 7th governance document was added later. Does it belong at governance level or should it be a pipeline reference?                                                                   | Small  |
| 5.2e. Governance simplification proposal         | Based on 5.2a–d, produce a concrete recommendation: which docs to merge, which to simplify, which to keep as-is. Human approval required before execution                                | Small  |
| 5.2f. Execute approved simplifications           | Apply the approved changes. Update all references and relationships                                                                                                                      | Medium |
| 5.2g. Post-simplification validation             | Run frontmatter validator and link integrity checker against all surviving governance docs and their references. This deterministic check catches breakage before downstream work begins | Small  |

**Success criteria**: Governance body reviewed with documented rationale for every decision (keep/merge/simplify). No redundancy between governance docs and CLAUDE.md. Human approves simplification proposal before any changes.

### Workstream 5.3 — Pipeline Rationalization

**Goal**: The minimum viable set of pipelines that supports actual operational needs.

| Item | Description | Effort |
|------|-------------|--------|
| 5.3a. Pipeline usage audit | For each of the 7 pipeline definitions: Is it referenced by any workflow YAML? Has it ever been executed? Is it needed by any current constellation? | Medium |
| 5.3b. Classify pipelines | Tag each as: operational (used now), planned (needed for Wave 6+), or aspirational (no concrete use case) | Small |
| 5.3c. Retire aspirational pipelines | Move to 99_ARCHIVE with clear archive rationale. They can be restored if needed | Small |
| 5.3d. Consolidate operational pipelines | If any operational pipelines overlap (e.g., Maintenance Pipeline vs. Note Upgrade Workflow), merge into a single authoritative definition | Medium |
| 5.3e. Validate surviving pipelines | Ensure each remaining pipeline has: correct frontmatter, valid stage definitions, clear input/output contracts, and a consuming workflow or constellation | Medium |

**Note**: The pipeline rationalization operates on the inventory as it exists at the start of this workstream's session, including any pipelines created by prior Wave 5 sessions (e.g., the Consolidation Pipeline). The Consolidation Pipeline itself is exempt from rationalization since it is the process being executed.

**Current pipeline inventory** (8 definitions as of v0.5 proposal, including Consolidation Pipeline):

| Pipeline | Category | Likely Classification |
|----------|----------|----------------------|
| Build Session Protocol | development | Operational — core build lifecycle |
| Development Pipeline | development | Needs assessment — overlaps with Build Session Protocol? |
| System Design Pipeline | development | Needs assessment — when was it last used? |
| Exploration Pipeline | exploration | Needs assessment — aspirational? |
| Learning Pipeline | learning | Needs assessment — aspirational? |
| Maintenance Pipeline | maintenance | Operational — vault maintenance constellation uses this |
| Agent Deployment Pipeline | deployment | Planned — needed for Wave 6+ |
| Consolidation Pipeline | maintenance | Operational — this wave is an instance of it (exempt from rationalization) |

**Success criteria**: Pipeline count reduced. Every surviving pipeline is either operational or explicitly tagged as planned-for-Wave-N. No orphan pipelines.

### Workstream 5.4 — Shell Script Maintenance Layer

**Goal**: Define and implement the boundary between deterministic script operations and LLM judgment calls.

| Item | Description | Effort |
|------|-------------|--------|
| 5.4a. Identify script-suitable operations | Survey current vault maintenance tasks. Classify each as deterministic (scriptable) or judgment-required (LLM) | Medium |
| 5.4b. Design shell script toolkit | Define the scripts needed: frontmatter validator, link integrity checker, orphan note detector, file counter, CSV operations, relationship graph builder | Medium |
| 5.4c. Implement Priority 1 scripts (front-loaded) | Build the 3 scripts that serve the consolidation itself: (1) frontmatter validator, (2) link integrity checker, (3) orphan note detector. Each must: accept vault root as argument, produce structured output (CSV or JSON), exit with meaningful codes. These are front-loaded to Session N because they are the audit framework's deterministic backbone | Large |
| 5.4c-1. Implement Priority 2 scripts (post-audit) | Build remaining scripts as time permits: authority weight distribution report, relationship completeness check. Desirable but not required for v0.5.0 exit criteria | Medium |
| 5.4d. Integrate with observation infrastructure | Scripts report through the same state_change_log.csv and observation channels as LLM agents | Medium |
| 5.4e. Define LLM/script boundary document | A reference document in 02_KNOWLEDGE that maps every maintenance operation to its executor (script vs. LLM) with rationale | Small |
| 5.4f. Deprecate vault_curator constellation | The deprecated vault_curator constellation should be formally archived as part of consolidation cleanup | Small |

**Candidate script operations**:

| Operation | Type | Why Script |
|-----------|------|-----------|
| Frontmatter schema validation | Script | Deterministic YAML parsing against known schema |
| Wiki-link integrity check | Script | File existence check — no judgment needed |
| Orphan note detection | Script | Notes with no inbound links — pure graph query |
| Authority weight distribution report | Script | CSV aggregation |
| Relationship completeness check | Script | Frontmatter field presence — deterministic |
| Duplicate content detection | LLM | Requires semantic understanding |
| Note quality assessment | LLM | Requires judgment against quality rubric |
| Content simplification | LLM | Requires language understanding and rewriting |

**Success criteria**: At least 3 shell scripts operational and tested. LLM/script boundary documented. Both execution paths log to the same infrastructure. vault_curator archived.

---

## Part 3: Build Order

The workstreams have dependencies that dictate sequencing. The build order below reflects amendments from the adversarial audit (Part 8), particularly: governance review completes before content is audited against governance standards (S1), critical scripts are front-loaded (SC2, S3), the overloaded bulk session is split (SC1), and each session includes a workflow extraction checkpoint (F2).

```
Session N:    5.1a (Baseline inventory) + 5.1a-1 (Audit framework)
              + 5.4a (Identify script-suitable operations)
              + 5.4c front-load (Implement Priority 1 scripts: frontmatter validator,
                link integrity checker, orphan note detector)
              + 5.3a–5.3b (Pipeline usage audit + classify)
              + Update root CLAUDE.md (Build Session Protocol now has 9 stages)
              → Workflow extraction checkpoint
              → Establishes rubric, baseline, deterministic tools, and pipeline landscape

Session N+1:  5.2a–5.2d (Governance body review — full analysis phase)
              → Governance review runs independently, without content audit in parallel.
                The governance standard must be stable before content is audited against it
              → Workflow extraction checkpoint

Session N+2:  5.2e (Governance simplification proposal — human approval gate)
              + 5.2f (Execute approved simplifications)
              + 5.2g (Post-simplification validation — run frontmatter validator + link
                integrity checker against all governance docs and references)
              + 5.3c–5.3e (Pipeline retire/consolidate/validate)
              → Workflow extraction checkpoint
              → Structural changes to governance and pipelines, validated by scripts

Session N+3:  5.1b (Tier-1 audit — governance docs now stable)
              + 5.1c (Tier-2 audit — system maps, concepts, references)
              + 5.1d (Tier-3 audit — aggressive pruning)
              → Workflow extraction checkpoint
              → Content audit across all tiers, measured against stable governance

Session N+4:  5.1e (Process 36 capture notes)
              → Workflow extraction checkpoint (capture processing is a strong candidate
                for pipeline extraction — the Note Processor specialist's workflow)
              → Dedicated session for the capture backlog to avoid scope overload

Session N+5:  5.4b (Design remaining script toolkit)
              + 5.4c-1 (Implement Priority 2 scripts)
              + 5.4d (Integrate scripts with observation infrastructure)
              + 5.4e (LLM/script boundary document)
              + 5.4f (Archive vault_curator constellation)
              → Workflow extraction checkpoint

Session N+6:  5.1f (Final audit report — before/after metrics against baseline)
              + Validate Consolidation Pipeline against actual work performed (D6)
              + Update Consolidation Pipeline with lessons learned
              → Final workflow extraction
              → Close out the wave
```

**Total estimated sessions**: 6–7
**Version target**: v0.5.0 after Session N+6

---

## Part 4: Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Over-pruning: removing notes that turn out to be needed later | Medium | Archive rather than delete. 99_ARCHIVE is always available for restoration. Tag archived items with `archive_reason` |
| Governance simplification breaks downstream references | High | Map all references before changing any governance doc. Update relationships in a single atomic session. Git checkpoint tag before changes |
| Shell scripts introduce a second maintenance surface | Medium | Scripts must pass through the same logging infrastructure. Include scripts in the standard build session review |
| 36 capture notes take longer than expected to process | Low | Process in priority order (most likely to contain unique knowledge first). Accept that some may be quick archives |
| Governance simplification introduces undetected breakage | High | Post-simplification validation step (5.2g) runs frontmatter validator and link integrity checker immediately after changes. Git checkpoint tag before changes enables rollback |
| Disagreement on which pipelines to retire | Low | Human approval required for all retire/archive decisions. Keep anything uncertain as "planned" rather than archiving prematurely |

---

## Part 5: Design Decisions

**D1. Audit before simplify.** The vault quality audit (5.1) runs before governance simplification (5.2) executes changes. This ensures we understand the full picture before restructuring.

**D2. Archive over delete.** The default action for content that doesn't earn its place is archive (move to 99_ARCHIVE), not delete. This is reversible and preserves institutional memory.

**D3. Human gate on governance changes.** Workstream 5.2 produces a simplification *proposal* (5.2e) that requires human approval before execution (5.2f). Governance documents carry authority_weight 80–90 and changes at this level must be human-authorized per the escalation rules.

**D4. Scripts complement, not replace.** Shell scripts handle deterministic operations. They do not replace the LLM constellation — they run alongside it. Both paths feed the same logging infrastructure.

**D5. One wave, one version.** Wave 5 produces v0.5.0. No intermediate version bumps. The vault is either consolidated or it isn't.

**D6. Validate the fractal.** At the end of Wave 5 (Session N+6), the Consolidation Pipeline is compared against the actual work performed. Any discrepancies — stages that didn't work as designed, missing parameters, timing insights — are incorporated into the pipeline definition. The pipeline must be genuinely reusable, not aspirational.

**D7. Front-load deterministic tools.** The three Priority 1 shell scripts (frontmatter validator, link integrity checker, orphan note detector) are built in Session N rather than Session N+4. This means the consolidation process itself benefits from deterministic validation at every stage. The scripts are both a deliverable of Wave 5 and a tool used during Wave 5.

---

## Part 6: Exit Criteria (Wave 5 Complete When...)

1. **Every note justified** — All vault notes have been reviewed. Each either earns its place (with accurate frontmatter, correct relationships, appropriate authority weight) or has been archived with documented rationale.

2. **Zero capture backlog** — 01_CAPTURE contains zero unprocessed notes. All 36 current captures have been classified, enriched, promoted, or archived.

9. **Consolidation Pipeline validated** — The abstract Consolidation Pipeline has been compared against the actual work performed and updated with lessons learned. It is genuinely reusable for future consolidation cycles and external vault audits.

3. **Governance body simplified** — Core governance documents reviewed with documented rationale for every keep/merge/simplify decision. No redundancy between governance docs and CLAUDE.md files.

4. **Pipeline count reduced** — Only operational and explicitly planned pipelines survive. Aspirational pipelines archived. Every surviving pipeline has complete frontmatter and valid contracts.

5. **Shell script layer operational** — At least 3 deterministic maintenance scripts implemented, tested, and integrated with the observation/logging infrastructure.

6. **LLM/script boundary defined** — A reference document maps every maintenance operation to its executor with rationale.

7. **Audit report published** — Formal audit report in 06_EXECUTION/reports/ documenting all changes, before/after metrics, and decisions made.

8. **Git release** — All changes committed, tagged as v0.5.0, with release notes summarizing the consolidation.

---

## Part 7: What This Unlocks

A consolidated vault is the prerequisite for everything that follows:

- **Wave 6 (Living System)** depends on a lean, consistent vault. Autonomous maintenance on bloated content propagates problems at machine speed.
- **Wave 7 (Self-Improving)** depends on clean observation data. A consolidated vault produces cleaner signals for the Evolution Constellation to analyze.
- **Wave 8 (Vault Architect)** depends on Agent Maestro's own vault being an exemplar. You cannot credibly audit and design external vaults if your own house is cluttered.

The fractal principle applies: the audit methodology developed in 5.1 becomes the foundation for the Generalized Vault Audit Protocol in Wave 8. The shell scripts built in 5.4 become the deterministic layer of the external audit toolkit. Consolidation is not just cleanup — it is capability building.

---

---

## Part 8: Adversarial Audit

**Audit date**: 2026-03-15
**Auditor**: Claude (Opus) — adversarial role per Build Session Protocol Stage 4
**Audit outcome**: **AMENDED** — findings require proposal changes before build

### Structural Integrity

**Finding S1 — Circular dependency between 5.1 and 5.2 (Severity: High)**

The build order puts governance review (5.2a–d) in Session N+1 alongside Tier-1 audit (5.1b). But Tier-1 audit reviews the same governance docs that 5.2 is analyzing. If the governance review recommends merging two documents, the Tier-1 audit of those documents was wasted effort. The proposal says "Governance review informs Tier-1 audit" but doesn't specify what happens if the governance review changes the documents the Tier-1 audit just reviewed.

**Resolution**: Governance body review (5.2) should fully complete its analysis phase before any content is audited against governance standards. Reorder so that 5.2a–d runs first, 5.2e produces the simplification proposal, and only after human approval of simplifications does Tier-1 audit begin — because at that point the governance standard is stable.

**Finding S2 — Pipeline inventory is stale before it starts (Severity: Medium)**

The pipeline inventory in Workstream 5.3 lists 7 pipelines. But this session has just created an 8th (Consolidation Pipeline) and amended the Build Session Protocol (adding two stages). The proposal doesn't account for the fact that the consolidation work itself is producing new pipelines while also rationalizing existing ones.

**Resolution**: Add a note that the pipeline rationalization (5.3) operates on the pipeline inventory as it exists at the start of that workstream's session, including any pipelines created by prior Wave 5 sessions. The Consolidation Pipeline itself is exempt from rationalization since it is the process being executed.

**Finding S3 — No rollback strategy for governance simplification (Severity: High)**

Risk R2 mentions "Git checkpoint tag before changes" but the proposal doesn't define what triggers a rollback or who decides. If governance simplification breaks something in Session N+2, how do we know? The downstream Tier-2/3 audits don't happen until Session N+3. The breakage could go undetected.

**Resolution**: Add an explicit validation step after 5.2f (execute simplifications): run the frontmatter validator and link integrity checker against all surviving governance docs and their references. This is a script-suitable operation (deterministic check) and could be the first shell script built in 5.4 — pulled forward as a dependency.

### Completeness

**Finding C1 — No total note count baseline (Severity: Medium)**

The proposal states 36 capture notes and 7 governance docs, but never establishes the total note count across the vault. Exit criteria say "every note justified" — but how many notes is that? Without a baseline count, the audit report can't produce meaningful before/after metrics.

**Resolution**: Add item 5.1a-0 (or fold into 5.1a): establish a complete vault inventory — total note count, distribution by folder, distribution by authority weight tier. This becomes the "before" baseline for the audit report.

**Finding C2 — Success criteria for 5.4 don't specify which 3 scripts (Severity: Low)**

"At least 3 deterministic maintenance scripts" is measurable, but the proposal lists 5 script candidates without prioritizing. Which 3 are the minimum? This matters because some scripts (frontmatter validator, link integrity) would be useful during the consolidation itself, while others (orphan detection, authority weight report) are purely observational.

**Resolution**: Prioritize the scripts that serve the consolidation process: (1) frontmatter validator, (2) link integrity checker, (3) orphan note detector. These three directly support Stages 5.1 and 5.2. The remaining scripts (authority weight distribution, relationship completeness) are desirable but not required for v0.5.0.

**Finding C3 — Proposal doesn't reference the Consolidation Pipeline (Severity: Medium)**

The proposal is an instance of the Consolidation Pipeline, but it doesn't say so. The `relationships` frontmatter doesn't reference it. This breaks the fractal traceability — the specific instance should explicitly link to its abstract process.

**Resolution**: Add `[[Consolidation Pipeline]]` to the proposal's `implements` relationship. Add a note in Part 1 or Part 2 stating that this proposal is the first instantiation of the Consolidation Pipeline.

### Scope Discipline

**Finding SC1 — Session N+3 is overloaded (Severity: High)**

Session N+3 combines Tier-2 audit + Tier-3 audit + processing 36 capture notes. The proposal labels Tier-2 as "Large" effort and capture processing as "Large" effort. Two large items plus a medium in one session is a scope risk. Previous proposals estimated 1–2 sessions just for processing the 45 (now 36) capture notes.

**Resolution**: Split Session N+3 into two sessions. Session N+3a: Tier-2 and Tier-3 vault audit. Session N+3b: Process capture notes. This increases the estimate to 6–7 sessions but is more realistic. Alternatively, accept that Session N+3 may spill into a second session and plan accordingly.

**Finding SC2 — Shell script implementation could be partially front-loaded (Severity: Medium)**

Workstream 5.4 is scheduled for Sessions N+4 and N+5, but Findings S3 and C2 above show that the frontmatter validator and link integrity checker would be useful during earlier stages. Building them only at the end means the consolidation itself can't benefit from them.

**Resolution**: Pull forward the implementation of the frontmatter validator and link integrity checker to Session N (alongside audit framework setup). These scripts are the audit framework's deterministic backbone. The remaining 5.4 items (boundary document, observation integration, vault_curator archive) stay in their current position.

### Fractal Alignment

**Finding F1 — Proposal doesn't explicitly state it is the fractal seed (Severity: Medium)**

The roadmap says "every capability Agent Maestro builds for itself becomes a capability it can offer to other vaults." The proposal mentions this in Part 7 but treats it as a consequence rather than a design constraint. The Consolidation Pipeline has been created, but the proposal doesn't reference it or commit to validating that the pipeline's abstract stages match the specific work being done.

**Resolution**: Add a design decision (D6) committing to validate the Consolidation Pipeline against the actual work performed. At the end of Wave 5, the Consolidation Pipeline should be updated with any lessons learned — stage adjustments, parameter additions, timing insights — so it is truly reusable, not aspirational.

**Finding F2 — Workflow Extraction not accounted for (Severity: Medium)**

The Build Session Protocol now includes a Workflow Extraction stage (Stage 7), but the proposal's build order doesn't include workflow extraction checkpoints at the end of each session. This is the first wave operating under the amended protocol — it should model compliance.

**Resolution**: Each session in the build order should include a workflow extraction checkpoint. Most sessions will produce a "no new pipeline" outcome, but some (particularly the capture processing session) may reveal sub-processes worth extracting.

### Downstream Impact

**Finding D1 — CLAUDE.md references to Build Session Protocol will need updating (Severity: Low)**

The root CLAUDE.md references the Build Session Protocol's 7-stage lifecycle. The protocol now has 9 stages. This reference will be stale until updated.

**Resolution**: Add updating root CLAUDE.md as a task in the first build session, or accept that it will be caught during the Tier-1 audit (which reviews CLAUDE.md as part of governance-adjacent files).

### Audit Summary

| ID | Severity | Category | Status |
|----|----------|----------|--------|
| S1 | High | Structural | Requires amendment — reorder 5.1/5.2 dependency |
| S2 | Medium | Structural | Requires note — pipeline inventory is dynamic |
| S3 | High | Structural | Requires amendment — add validation step + front-load scripts |
| C1 | Medium | Completeness | Requires amendment — add baseline inventory |
| C2 | Low | Completeness | Requires amendment — prioritize scripts |
| C3 | Medium | Completeness | Requires amendment — add pipeline reference |
| SC1 | High | Scope | Requires amendment — split overloaded session |
| SC2 | Medium | Scope | Requires amendment — front-load critical scripts |
| F1 | Medium | Fractal | Requires amendment — add D6 design decision |
| F2 | Medium | Fractal | Requires amendment — add extraction checkpoints |
| D1 | Low | Downstream | Note — will be caught during audit |

**High-severity findings**: 3 (S1, S3, SC1)
**Total findings requiring amendment**: 10 of 11

---

**Awaiting approval of audit findings and amended proposal before any build work begins.**
