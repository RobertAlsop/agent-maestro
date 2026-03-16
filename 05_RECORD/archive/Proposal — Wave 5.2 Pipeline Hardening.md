---
title: "Proposal — Wave 5.2 Pipeline Hardening"
type: proposal
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
approved: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM v1.0.0 — Design Blueprint]]"
    - "[[Wave 5.1 — Design Session Reflection]]"
  governs: []
  related:
    - "[[Agent Maestro — North Star]]"
    - "[[Agent Maestro — Vault Rules]]"
    - "[[AM — Evolution Roadmap — Waves 5-8]]"
tags: [proposal, wave-5.2, pipeline, governance, hardening]
---

# Proposal — Wave 5.2 Pipeline Hardening

## Problem Statement

Wave 5.1 delivered the architectural redesign — the Design Blueprint, simplified schema, governance migration, and new folder structure. But the vault is in a transitional state. Specific evidence:

1. **The reflection sits at root**, not in the pipeline. The loop from Wave 5.1 hasn't formally closed (Reflect → Capture).
2. **39 concept files in 02_KNOWLEDGE/concepts/** — most are leftovers from the authority pack and agent constellation era (e.g., Authority Pack Compiler, Agent Constellation, Compiled Governance Artifact). They predate the v1.0.0 redesign and haven't been evaluated against Law 3.
3. **Governance documents were migrated to schema v3** but haven't been reviewed for internal consistency, alignment with the Blueprint, or mutual coherence post-restructure.
4. **No top-level roadmap exists.** The Waves 5-8 evolution roadmap in 03_DECIDE describes the old architecture in places and doesn't reflect the post-5.1 reality.
5. **No standard operating procedures (SOPs) exist** for how Rob + Claude work through the pipeline, or how an LLM agent works through it autonomously.
6. **No workflow documentation** for the human-AI collaborative process that Wave 5.1 proved effective.
7. **06_REFLECT is empty.** 01_CAPTURE has no active seeds. The pipeline isn't flowing.

The vault has good bones but unfinished joints. If we start building capabilities (Wave 6) on top of this, we'll compound the inconsistencies.

## Proposed Change

**Wave 5.2: Pipeline Hardening** — a systematic walkthrough of every pipeline stage, every folder, and every file, conducted collaboratively by Rob and Claude. The wave has six phases.

**Operating principle: Human-in-the-loop by default.** Every phase is carried out as a question-and-answer session between Claude and Rob. Claude presents findings, asks targeted questions, and proposes changes — Rob confirms, corrects, or redirects. No phase is executed autonomously unless Rob explicitly delegates a specific task. This is not a reporting exercise; it is a working conversation. This principle derives from D4 (Human Sovereignty), the Wave 5.1 reflection (Learning 6: "collaborative design with frequent checkpoints works"), and the fact that the semantic judgments required in this wave — "is this governance doc saying what we mean?" — cannot be made by an LLM alone.

### Phase 1 — Close the 5.1 Loop
- Move the reflection to `06_REFLECT/`
- Create a derivative capture document in `01_CAPTURE/inbox/` that seeds Wave 5.2
- This formally closes Wave 5.1 and opens 5.2 through the pipeline itself

### Phase 2 — Governance Review
- Walk through each governance document individually (Foundations → North Star → Vault Rules → Scope → Strategy → Modes → Principles → Worker Role → Reviewer Role)
- For each document: Claude asks targeted questions, Rob confirms or corrects, we tighten language and resolve any inconsistencies
- Verify all governance docs are mutually coherent and aligned with the Design Blueprint
- Confirm authority_weight hierarchy is correct and earned
- **Escalation rule:** Any change that alters the meaning or intent of a governance document (authority_weight ≥ 80) is a Level 3 decision requiring explicit human approval on that specific change. Language tightening that preserves meaning is Level 2. When in doubt, escalate.

### Phase 3 — Pipeline Walkthrough (folder by folder)
- Starting at 01_CAPTURE, move through each pipeline folder
- At each stage: check contents against governance, apply Law 3 (does this earn its place?), note what needs to be created, cleaned, or archived. Capture SOP observations as working notes for formalization in Phase 5.
- **02_KNOWLEDGE/concepts/ cleanup**: Apply viability audit to all 39 concept files. Identify the minimum viable concept set — the concepts that are actually referenced by governance, skills, or operational documents. Archive the rest.
- **02_KNOWLEDGE/references/**: Same viability check
- **04_EXECUTE/runtime/**: Verify code aligns with v1.0.0 architecture decisions
- **05_RECORD/archive/**: Confirm archive is organized and complete

### Phase 4 — Roadmap Consolidation
- Create one **top-level AM roadmap** (strategic direction, current version, target milestones)
- Create one **future waves register** — a living document listing all potential future builds/upgrades, updated after each wave
- Review the existing Waves 5-8 evolution roadmap: evaluate relevance of 5.4–8.4 items post-refactor
- Archive or integrate the old roadmap as appropriate

### Phase 5 — SOPs and Workflow Documentation
- Formalize the SOP observations captured as working notes during Phase 3 into proper documents
- Document the **human-AI collaborative workflow** (the process Rob + Claude used in 5.1, formalized as a repeatable SOP)
- Document the **LLM autonomous workflow** (how an agent enters the vault, reads CLAUDE.md, and works through a task)
- Document **per-stage SOPs** — what happens at each pipeline stage, what the gate criteria are, what artifacts are produced
- These become operational knowledge in `02_KNOWLEDGE/` (patterns or a new `workflows/` subfolder)

### Phase 6 — Wave 5.2 Reflection
- Document what happened, what we learned
- Feed forward into 01_CAPTURE as seeds for Wave 5.3
- Update SYSTEM_MAP to reflect current vault state

## Traceability

| Decision | Foundation |
|----------|-----------|
| Walk the pipeline systematically | Seed 1 (Process) — every operation follows the Irreducible Loop |
| Review governance first, before touching anything downstream | D5 (Governance Before Autonomy) — govern before you operate |
| Apply Law 3 to concepts folder | Law 3 (Economy) — only what is necessary |
| Collaborative human-AI process | D4 (Human Sovereignty) + Learning 6 from reflection |
| Close the loop before starting new work | Seed 1 (Process) — the loop must close; Reflect feeds Capture |
| Separate proposal from approval | D6 (Separation of Powers) — proposer ≠ approver |
| Document SOPs as we discover them | Law 2 (Action Properties) — verifiable, accountable; D1 (Deterministic Control Surfaces) |
| Human-in-the-loop by default for every phase | D4 (Human Sovereignty) + Learning 6 from reflection — semantic judgments require human confirmation |
| Create roadmap hierarchy | D3 (Controlled Evolution) — changes proceed through graduated stages |

## Impact Assessment

**What this affects:**
- Every folder in the vault will be reviewed and potentially modified
- Governance documents may receive language tightening (content changes, not structural)
- 20-30 concept files may be archived
- New documents will be created (roadmap, SOPs, workflow docs)
- SYSTEM_MAP will need updating at the end

**What could go wrong:**
- **Scope creep.** The walkthrough could expand into rebuilding things rather than reviewing them. Mitigation: strict discipline — review and document only. If we find something that needs a build, we note it as a future wave item, not an in-session fix.
- **Over-archiving concepts.** Some concepts that look irrelevant may contain seeds for future waves. Mitigation: archive, don't delete. Everything remains accessible in 05_RECORD/archive/.
- **Governance changes cascading.** If we tighten a governance doc and it changes meaning, downstream documents may need updating. Mitigation: review governance as a complete set before touching anything downstream.
- **Session length.** This is a substantial walkthrough. Mitigation: we can split across multiple sessions if needed. Each phase has a natural stopping point.

**Scope protection — Minimum Viable 5.2 vs. Full 5.2:**
If scope pressure builds, the wave has a graceful degradation path. Phases 1-3 (close the loop, governance review, pipeline walkthrough) constitute the **minimum viable wave** — the vault is hardened and consistent. Phases 4-5 (roadmap, SOPs) are high-value but can be deferred to a 5.3 if needed without compromising the foundation. Phase 6 (reflection) always happens regardless. This honors Law 3 applied to the wave itself.

## Alternatives Considered

**Alternative 1: Skip straight to Wave 6 (Living System — autonomous execution)**
Rejected. The reflection explicitly noted that "governance documents need to be updated BEFORE the build, not during it." Starting autonomy on top of an inconsistent vault would compound problems. D5 (Governance Before Autonomy) supports this rejection.

**Alternative 2: Automated audit only (run validators, fix what fails)**
Rejected. Schema validation catches structural issues but not semantic ones. The governance review needs human judgment — are these documents actually saying what we mean? Automated tools are Wave 6 territory.

**Alternative 3: Do phases 1-3 only, defer roadmap and SOPs**
Considered viable but rejected. The SOPs are the bridge between "vault that exists" and "vault that operates." Without them, we'd complete another wave with no documented process, repeating the pattern Wave 5.1 identified. The roadmap prevents us from losing the strategic thread.

## Gate Criteria

This proposal is ready to execute when:

- [x] Proposal drafted with all six required elements
- [x] Adversarial audit completed (all three lenses) — 3 findings, all resolved via refinements
- [x] Human (Rob) approves the proposal
- [x] Audit findings resolved (governance escalation rule added, Phase 3/5 overlap clarified, scope protection defined)

Wave 5.2 is complete when:

- [x] Wave 5.1 reflection is in 06_REFLECT and derivative in 01_CAPTURE
- [x] All 9 governance documents reviewed and confirmed solid
- [x] Every pipeline folder reviewed, contents justified or archived
- [x] Concepts reduced to minimum viable set
- [x] Top-level roadmap created
- [x] Future waves register created
- [x] Workflow documentation consolidated into Universal Workflow (one document replacing 3+ SOPs — Law 3 applied)
- [x] SYSTEM_MAP updated to reflect final vault state
- [x] Wave 5.2 reflection written and filed

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal modifies vault contents across all pipeline stages and creates new document types (SOPs, roadmaps). It does not change governance definitions (those changes would be Level 3 and escalated individually during Phase 2 if needed).
