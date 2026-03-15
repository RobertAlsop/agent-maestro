---
schema_version: 2
title: Build Session Protocol
tags:
  - pipeline
  - protocol
  - session
  - governance
relationships:
  part_of: "[[02_Systems/Agent Maestro/03_PIPELINES/development/Development Pipeline]]"
  implements: "[[Agent Maestro — Principles]]"
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
last_modified: 2026-03-14
status: active
maps: []
related: []
related_maps: []
related_pipes: []
supersedes: []
superseded_by: []
review_status: draft
version: 1
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
id: PIPE.build_session_protocol
type: log
note_class: execution
layer: pipes
---

# Build Session Protocol

## Purpose

Defines the formalised lifecycle for every Agent Maestro build session. This protocol ensures that work is scoped before execution, governed during execution, and documented after execution. It emerged organically during Session 1 (v0.1 build) and was formalised during Session 2 (v0.2 planning).

## Context

Every time a human and Claude work together on Agent Maestro, the interaction follows a natural rhythm that maximises quality and minimises waste. This protocol captures that rhythm as a repeatable pipeline.

## Relationships

- Implements: [[Governance Before Autonomy]] — scope and contract before execution
- Produces: Session logs in 06_EXECUTION/logs/sessions/
- Uses: [[Agent Maestro — Modes]] — sessions operate in Design, Governance, or Execution mode

---

# Stages

## Stage 1 — Input
The human provides context, requirements, and direction.
Entry condition: Human initiates session with intent.
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

## Stage 4 — Build
Claude executes against the approved proposal. Follows vault conventions. Logs progress. Escalates decisions that exceed the proposal scope.
Entry condition: Proposal approved.
Exit condition: All deliverables complete or explicitly deferred.

## Stage 5 — Output Summary
Claude produces a summary of everything built: files created/modified, registries updated, decisions made, deferred items, verification results.
Entry condition: Build complete.
Exit condition: Summary shared with human.

## Stage 6 — Session Log
A formal session log is written to 06_EXECUTION/logs/sessions/ capturing all metadata, decisions, deliverables, and next actions. The session index CSV is updated.
Entry condition: Output summary complete.
Exit condition: Session log written, index updated.

## Stage 7 — Git Commit + Release (v0.3+)
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
Stages 1 → 2 (roadmap) → 6 (log). No build, no proposal.

## Quick Fix Session
Stages 1 → 4 → 5 → 6. Skip brief and proposal when the task is small and well-defined.

## Multi-Build Session
Stages 1 → 2 → 3 → 4 → 5 → 3 → 4 → 5 → 6. Multiple proposal-build cycles within one session.

---

# Rules

1. Never build without a brief (unless Quick Fix variation).
2. Never build without human approval of the proposal.
3. Always produce an output summary after building.
4. Always log the session.
5. If scope changes during build, pause and re-propose.
6. The proposal is the contract — deviations require explicit acknowledgement.
7. Each session should reference which roadmap wave/upgrade it addresses.