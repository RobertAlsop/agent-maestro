---
schema_version: 2
title: Build Session Protocol
tags:
  - pipeline
  - protocol
  - session
  - governance
relationships:
  part_of: []
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs:
    - "[[Agent Maestro — Evolution Roadmap v0.2]]"
  uses:
    - "[[Agent Maestro — Modes]]"
    - "[[Governance Before Autonomy]]"
  defines: []
  inherits_from: []
  applies_to: []
  produces: []
authority_weight: 75
created_date: 2026-03-14
last_modified: 2026-03-15
status: active
supersedes: []
superseded_by: []
review_status: draft
version: 2
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
type: log
note_class: execution
layer: pipes
---

# Build Session Protocol

## Purpose

Defines the formalised lifecycle for every Agent Maestro build session. This protocol ensures that work is scoped before execution, audited before building, governed during execution, extracted into reusable patterns after execution, and documented throughout. It emerged organically during Session 1 (v0.1 build), was formalised during Session 2 (v0.2 planning), and extended with Adversarial Audit and Workflow Extraction stages in v0.5.

## Context

Every time a human and Claude work together on Agent Maestro, the interaction follows a natural rhythm that maximises quality and minimises waste. This protocol captures that rhythm as a repeatable pipeline.

## Relationships

- Implements: [[Governance Before Autonomy]] — scope and contract before execution
- Produces: Session logs in 06_EXECUTION/logs/sessions/
- Uses: [[Agent Maestro — Modes]] — sessions operate in Design, Governance, or Execution mode

---

# Stages

## Stage 0 — Brainstorm (v0.5+)
Before formal session input, the human and/or Claude may engage in open-ended exploration of the problem space. Brainstorming generates raw material — observations, hypotheses, design sketches, analogies, "what if" questions — that inform the subsequent stages. Brainstorm artifacts are stored in `04_PROJECTS/active/agent_maestro_development/brainstorms/`.

Entry condition: A problem, opportunity, or direction exists but is not yet well-defined.
Exit condition: Brainstorm artifacts captured. Enough clarity to formulate session input (Stage 1).

### Brainstorm Guidelines

1. **Diverge before converging**: Generate many ideas before evaluating any.
2. **Capture everything**: Even fragments and half-formed thoughts have value. Write them down.
3. **Name artifacts clearly**: Use `AM — Wave [N] — [Topic] Brainstorm.md` naming convention.
4. **Link to session**: Reference the brainstorm from the session log's Input Summary.
5. **No governance required**: Brainstorms are exploratory. They do not require approval, audit, or frontmatter compliance. They become governed when promoted to proposals.

### Relationship to Other Stages

Brainstorm → Input → Brief → Proposal. The brainstorm feeds Stage 1 but does not replace it. Stage 1 still requires structured input; the brainstorm provides the raw material from which structured input is distilled.

## Stage 1 — Input
The human provides context, requirements, and direction.
Entry condition: Human initiates session with intent (optionally informed by Stage 0 brainstorm).
Exit condition: Claude has enough context to produce a brief.

## Stage 2 — Brief / Roadmap
Claude analyses the input and produces a structured brief or roadmap.
Entry condition: Sufficient input from Stage 1.
Exit condition: Brief/roadmap shared with human for review.

## Stage 3 — Proposal (Build Contract)
Claude produces a detailed proposal that serves as the build contract with specific deliverables, sequence, success criteria, and risks.
The human reviews and either approves, requests changes, or redirects.
Entry condition: Brief/roadmap approved.
Exit condition: Human confirms approval.

## Stage 4 — Adversarial Audit (v0.5+)
Before building, the proposal undergoes an adversarial audit — a structured attempt to find flaws, gaps, contradictions, unstated assumptions, and downstream risks. The auditor role is adversarial by design: it assumes the proposal is wrong and tries to prove it.

Entry condition: Proposal produced (Stage 3 complete).
Exit condition: Audit findings documented. Proposal either confirmed, amended, or rejected.

### Audit Checklist

**Structural integrity:**
- Does the proposal contradict any governance document (authority_weight ≥ 80)?
- Are there internal contradictions between deliverables, sequence, or success criteria?
- Does the build order have unacknowledged dependencies?

**Completeness:**
- Are there unstated assumptions that would cause the build to fail?
- Are success criteria measurable and verifiable?
- Are risks identified for every high-impact deliverable?
- Does the proposal account for rollback if a deliverable fails?

**Scope discipline:**
- Does the proposal try to do too much for one wave/session?
- Could any deliverable be deferred without undermining the wave's core question?
- Is there scope creep disguised as "nice to have"?

**Fractal alignment (v0.5+):**
- Does the work produce a reusable pattern, or is it a one-off?
- If this process will be repeated on other vaults/systems, does the proposal build toward that generalization?

**Downstream impact:**
- Will any deliverable break existing vault content, references, or registries?
- Are there second-order effects the proposal doesn't address?

### Audit Outcomes

| Outcome | Meaning | Next Step |
|---------|---------|-----------|
| CONFIRMED | No material findings. Proposal is sound | Proceed to Stage 5 (Build) |
| AMENDED | Findings require proposal changes | Return to Stage 3, amend proposal, human re-approves |
| REJECTED | Fundamental problems discovered | Return to Stage 2, re-brief |

### Audit Severity Scale

| Severity | Definition | Effect |
|----------|-----------|--------|
| Critical | Would cause build failure, governance violation, or data loss | AMENDED or REJECTED — must be resolved |
| High | Significant gap or risk that undermines a deliverable | AMENDED — should be resolved |
| Medium | Missing detail or unstated assumption, workaround exists | Note in proposal, proceed |
| Low | Observation or improvement suggestion | Log for future reference |

## Stage 5 — Build
Claude executes against the approved (and audited) proposal. Follows vault conventions. Logs progress. Escalates decisions that exceed the proposal scope.
Entry condition: Proposal approved and adversarial audit outcome is CONFIRMED or AMENDED-and-re-approved.
Exit condition: All deliverables complete or explicitly deferred.

## Stage 6 — Output Summary
Claude produces a summary of everything built: files created/modified, registries updated, decisions made, deferred items, verification results.
Entry condition: Build complete.
Exit condition: Summary shared with human.

## Stage 7 — Workflow Extraction (v0.5+)
After the build, assess whether the work performed constitutes a repeatable process. If so, extract the abstract pipeline from the specific instance.

Entry condition: Output summary complete.
Exit condition: Either a new pipeline definition is created in 03_PIPELINES/, or a documented "no new pipeline" decision is recorded.

### Extraction Checklist

1. **Repeatability test**: Would this same sequence of work be useful again — on this vault, on another vault, or on a different system?
2. **Abstraction test**: Can the specific instance (names, paths, counts) be replaced with parameters while preserving the logic?
3. **Stage identification**: What are the natural stages? What are the entry/exit conditions for each?
4. **Input/output contracts**: What does each stage consume and produce?
5. **Executor classification**: For each stage, is the executor a script (deterministic), an LLM (judgment), or a human (decision)?

### Extraction Outcomes

| Outcome | Action |
|---------|--------|
| New pipeline identified | Write pipeline definition to 03_PIPELINES/ with correct frontmatter. Reference the originating session |
| Existing pipeline extended | Amend the existing pipeline definition. Log the extension in the session log |
| No pipeline needed | Record the decision and brief rationale in the session log |

### Fractal Principle

This stage exists because of the fractal design principle: every capability Agent Maestro builds for itself becomes a capability it can offer to others. A one-off build is a missed opportunity. A pipeline is a reusable asset.

## Stage 8 — Session Log
A formal session log is written to 06_EXECUTION/logs/sessions/ capturing all metadata, decisions, deliverables, and next actions. The session index CSV is updated.
Entry condition: Workflow extraction complete (or output summary complete if extraction is skipped).
Exit condition: Session log written, index updated.

## Stage 9 — Git Commit + Release (v0.3+)
All changes are committed to version control. The commit message references the session ID and upgrades addressed. For milestone versions, a Git tag and GitHub release are created with release notes.
Entry condition: Session log complete.
Exit condition: Changes committed and pushed.

Standard steps:
1. `git add` — stage all changed files (review before staging)
2. `git commit` — message format: "SES-XXX: [summary of changes]"
3. `git push` — push to remote
4. (Milestone only) `git tag vX.Y.Z` + `gh release create` with release notes

Versioning convention:
- Major (v1.0): Production-ready milestone
- Minor (v0.3.0): Significant new capability (e.g., workflow engine works)
- Patch (v0.2.1): Bugfix, hardening, or incremental improvement

---

# Variations

## Exploration Session
Stages 1 → 2 (roadmap) → 8 (log). No build, no proposal.

## Quick Fix Session
Stages 1 → 5 (build) → 6 (summary) → 8 (log). Skip brief, proposal, and audit when the task is small and well-defined. Workflow extraction (Stage 7) is still recommended — quick fixes sometimes reveal repeatable patterns.

## Multi-Build Session
Stages 1 → 2 → 3 → 4 → 5 → 6 → 7 → 3 → 4 → 5 → 6 → 7 → 8. Multiple proposal-audit-build cycles within one session. Each cycle includes its own adversarial audit and workflow extraction.

## Audit-Only Session
Stages 1 → 3 (proposal to review) → 4 (adversarial audit) → 8 (log). Used when reviewing existing proposals or plans without building. The audit findings are the deliverable.

---

# Rules

1. Never build without a brief (unless Quick Fix variation).
2. Never build without human approval of the proposal.
3. Always run an adversarial audit on the proposal before building (unless Quick Fix variation).
4. Always produce an output summary after building.
5. Always assess workflow extraction after building.
6. Always log the session.
7. If scope changes during build, pause and re-propose (which triggers a new audit).
8. The proposal is the contract — deviations require explicit acknowledgement.
9. Each session should reference which roadmap wave/upgrade it addresses.
10. If a build session produces a repeatable process, extract it as a pipeline. One-off work is a missed fractal opportunity.