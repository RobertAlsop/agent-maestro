---
title: "AM — Git Conventions"
type: governance
status: active
authority_weight: 70
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  related:
    - "[[AM — Tool Conventions]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[AM — Roadmap]]"
    - "[[Wave 8.3 — Reflection]]"
tags:
  - governance
  - git
  - version-control
  - conventions
  - safety
  - historical-exceptions
---

# AM — Git Conventions

## Purpose

Define the git workflow, conventions, and safety rules for all work within the Agent Maestro vault. This document is the authoritative reference for how version control operates in AM. It governs both human and AI-assisted git operations, and is the specification that `git_hygiene.py` (Wave 8.3) enforces mechanically and that future workflow automation (Wave 8.4) implements.

This document replaces [[Git Best Practices for AI-Assisted Builds]] (`05_RECORD/archive/`), which served as the initial reference and has been archived. The principles from that document are preserved and extended here with AM-specific conventions, pipeline integration, and Foundations traceability.

## Principle

Git is AM's memory of change. Every commit is a record. Every branch is a workspace boundary. Every tag is a checkpoint. Every merge is a gate. Version control is not a development convenience — it is the implementation of Law 2 (all actions must be verifiable, reversible, and accountable) for everything that enters the repository.

Because AM uses AI agents for implementation work, the conventions carry additional weight. An AI agent can produce large, sweeping changes in a single pass. Without disciplined version control, those changes are neither bounded nor reversible. The conventions in this document exist to make every change — regardless of who or what produced it — auditable, reversible, bounded, and traceable to the work it belongs to.

---

## The Protected Baseline

`master` is the protected baseline branch.

It must remain:

- **Stable** — `master` always represents a known-good state of the vault.
- **Reversible** — any state of `master` can be rolled back to a previous tagged checkpoint.
- **Recoverable** — if an AI-assisted build produces bad output, `master` is the safe ground to return to.

No implementation work occurs directly on `master`. All substantive changes reach `master` through a merge from a working branch, after validation passes. The only commits permitted directly on `master` are:

- Merge commits from validated working branches.
- Trivial housekeeping (typo fixes, whitespace) where branching would violate Law 3 (Economy). These should be rare and clearly marked in the commit message. **Detection note:** `git_hygiene.py` cannot mechanically distinguish trivial from non-trivial commits. It flags all non-merge commits on `master` as **warnings** (not findings). The human evaluates whether the housekeeping exception applies. This follows Convention 7 (Conservative) — no false positives on legitimate exceptions.

**Note on branch naming:** The repository uses `master` as its default branch. Vault Rule 67 delegates all git conventions to this document, making it the single source of truth. `master` is the canonical name for the protected baseline in the AM repository. If the repository is ever renamed to `main`, this document should be updated accordingly.

---

## Branch Conventions

### When to Branch

Create a dedicated working branch before beginning any implementation work. "Implementation work" means anything that changes vault content, tools, or configuration beyond a trivial correction. The threshold is judgment — but when in doubt, branch.

### Branch Naming

Branch names follow the pattern:

```
<context>-<description>
```

Where `<context>` identifies the unit of work and `<description>` summarises the scope in lowercase hyphenated words.

**AM-specific patterns:**

| Context | Pattern | Example |
|---------|---------|---------|
| Wave work | `wave-X.Y-description` | `wave-8.2-pipeline-enforcement` |
| Hotfix | `fix-description` | `fix-yaml-parser-edge-case` |
| Housekeeping | `housekeeping-description` | `housekeeping-archive-cleanup` |

Branch names must be:

- Lowercase with hyphens (no underscores, no spaces, no camelCase).
- Descriptive enough that someone reading `git branch` can understand the purpose without checking the commit log.
- Scoped to a single unit of work. Do not reuse a branch for unrelated work.

### Branch Lifecycle

| Stage | What happens |
|-------|-------------|
| **Created** | Branch created from `master` at a known-good state. A pre-branch checkpoint tag should exist (see Tags below). |
| **Active** | Implementation work happens. Commits are frequent, scoped, and descriptive. |
| **Validated** | `orchestrate.sh` (or the relevant validation suite) runs and passes. Findings are addressed. |
| **Merged** | Branch is merged to `master` after validation passes and any required human approval is obtained. |
| **Cleaned up** | After merge, the branch is deleted locally and remotely. Stale branches (not merged within 30 days of last commit) should be evaluated: merge, rebase, or delete. |

### Stale Branches

A branch is considered stale if its most recent commit is older than 30 days and it has not been merged to `master`. Stale branches are not automatically deleted — they are flagged by `git_hygiene.py` for human review. The human decides: merge, rebase, or delete.

---

## Tag Conventions

Tags serve two purposes in AM: **checkpoint tags** mark known-good states before risky operations, and **version tags** mark completed waves.

### Checkpoint Tags

Create a checkpoint tag before any major build pass — before branching for a wave, before a large refactor, before any operation that could produce changes you might want to undo.

**Naming pattern:** `pre-<context>`

| Context | Pattern | Example |
|---------|---------|---------|
| Before a wave | `pre-wave-X.Y` | `pre-wave-8.2` |
| Before a refactor | `pre-<description>` | `pre-archive-cleanup` |

Checkpoint tags are the rollback anchors. If an AI-assisted build pass produces bad output:

```
git checkout master
git reset --hard pre-wave-8.2
```

### Version Tags

Version tags mark completed, validated states — typically at wave completion after all gate criteria pass.

**Naming pattern:** `vX.Y.Z` (semantic versioning)

| Component | Meaning in AM |
|-----------|--------------|
| Major (X) | Strategy stage change or architectural restructure |
| Minor (Y) | Wave completion |
| Patch (Z) | Housekeeping, hotfixes, minor corrections |

### Tag Rules

- Tags must be pushed to the remote: `git push origin <tag-name>`.
- Tags are immutable. Do not move or delete tags unless correcting an error (Level 3 — human approval required).
- Every completed wave should have both a checkpoint tag (created before the wave started) and a version tag (created when the wave is complete).

---

## Commit Conventions

### Commit Message Format

Commit messages follow one of three accepted formats:

**Format 1 — Session-scoped:**
```
SES-XXX: Summary of what was done
```
Used when work is tracked by session ID. The session log provides the detailed context.

**Format 2 — Wave-scoped:**
```
Wave X.Y: Summary of what was done
```
Used for commits that correspond to a specific wave's work, especially when a single session spans multiple commits within the same wave.

**Format 3 — Descriptive:**
```
Summary of what was done in imperative mood
```
Used for housekeeping, hotfixes, and work that doesn't map to a specific session or wave. The message must be descriptive enough to understand without external context.

### Commit Quality Rules

- **Small and scoped.** Each commit should address a single implementation objective. A commit that touches unrelated files or mixes concerns is too large.
- **Descriptive.** The message must convey what was done and (briefly) why. No single-word messages, no `stuff`, no `updates`, no `fixes`.
- **Frequent.** Commit at meaningful checkpoints during implementation — after completing a logical unit of work, after passing a validation, before switching focus. More commits is safer than fewer.
- **Minimum message length.** Commit messages should be at least 5 characters. This floor eliminates single-word throwaway messages (`fix`, `wip`) without penalising legitimate short descriptions (`Fix typo`, `Add tag`).

---

## Merge Conventions

### Merge to Master

Working branches are merged to `master` only after:

1. **Validation passes.** `orchestrate.sh` (the full integrity suite) runs against the branch and produces no unaddressed findings. At minimum, structural integrity (Wave 6 tools) must pass. Pipeline enforcement (Wave 8.2 tools) should pass where applicable.
2. **Wave gate criteria are met.** If the branch corresponds to a wave, all completion criteria in the wave's proposal are satisfied.
3. **Human approval** for changes that touch governance (authority_weight ≥ 70), vault structure, or architectural decisions. This is Level 3 — the human reviews the diff and approves the merge.

### Merge Strategy

Use standard merge commits (not fast-forward, not squash) for wave branches. Merge commits preserve the branch history and create a visible record of when work was integrated. The merge commit message should reference the wave:

```
Merge wave-8.2-pipeline-enforcement: Pipeline enforcement tooling complete
```

Fast-forward merges are acceptable for trivial branches (hotfixes, single-commit housekeeping) where preserving branch structure adds no informational value.

Squash merges are not used. They destroy the granular commit history that Law 2 (accountability) requires.

---

## Recovery Procedures

### Bad Build on a Working Branch

If an AI-assisted build pass produces bad output and the work is confined to a working branch:

```
git checkout master
git branch -D <branch-name>
```

The branch is discarded. `master` is untouched. Start over from the checkpoint tag if needed.

### Bad Merge to Master

If a merge to `master` introduced problems:

```
git revert -m 1 <merge-commit-hash>
```

This creates a new commit that undoes the merge, preserving history. Prefer revert over reset for `master` — revert is additive (adds a correction) while reset is destructive (rewrites history).

### Hard Rollback (Emergency)

If `master` is in a bad state and revert is insufficient:

```
git reset --hard <checkpoint-tag>
```

This is a destructive operation that discards all commits after the tag. It requires Level 3 human approval. Only use when you intentionally want to discard committed state.

---

## Safety Rules for AI Agents

AI agents (LLMs operating via Claude Code, Cowork, or any other interface) are bound by the same git conventions as human operators, plus additional constraints. These rules are a quick-reference checklist; the Escalation Levels table below provides the comprehensive reference for which operations require which approval level.

### Agents MUST:

1. Confirm the current branch is not `master` before beginning implementation work.
2. Create or verify a checkpoint tag exists before starting a major build pass.
3. Commit frequently at meaningful checkpoints — do not accumulate an entire wave's work in uncommitted state.
4. Run validation before declaring work complete.
5. Stop before merge if validation fails — do not merge unvalidated work.

### Agents MUST NOT:

6. Work directly on `master` for implementation work.
7. Rewrite git history (`rebase`, `commit --amend` on pushed commits, `filter-branch`) without explicit human instruction.
8. Force-push (`push --force`, `push --force-with-lease`) without explicit human permission.
9. Delete branches or tags without explicit human authorisation.
10. Bypass validation steps silently. If the human explicitly instructs skipping validation for speed, the agent should note the risk, comply if the human confirms, and log the override in the commit message or session log. Accountability (Law 2) is preserved even when the human exercises sovereignty (D4).

### Agents MAY:

11. Create working branches.
12. Make small, scoped commits on working branches.
13. Recommend checkpoint tags.
14. Stop before merge if validation fails (this is preferred over proceeding).
15. Push branches and tags to the remote.

---

## The Wave Git Workflow

Git operations map to AM's pipeline stages. A typical wave follows this sequence:

```
DECIDE (proposal approved)
  │
  ├─ git tag pre-wave-X.Y          ← Checkpoint from master
  ├─ git checkout -b wave-X.Y-desc ← Working branch created
  │
EXECUTE (implementation)
  │
  ├─ git commit (frequent, scoped) ← Work happens on the branch
  ├─ ./orchestrate.sh              ← Validation at checkpoints
  │
RECORD (completion)
  │
  ├─ All gate criteria verified
  ├─ Reflection written
  ├─ Capture seed created
  │
  ├─ git checkout master
  ├─ git merge wave-X.Y-desc       ← Merge after validation
  ├─ git tag vX.Y.Z                ← Version tag
  ├─ git push origin master --tags ← Push to remote
  ├─ git branch -d wave-X.Y-desc   ← Branch cleanup
  │
REFLECT (loop closes)
```

This workflow is the operational spec for Wave 8.4 (Git Workflow Automation). Each step that can be automated is a candidate for the automation tool. Steps that require human judgment (merge approval for governance changes, recovery decisions) are escalation points.

---

## Escalation Levels for Git Operations

Git operations have varying risk profiles. The escalation level determines whether an operation can be performed automatically, requires agent judgment, or requires human approval. The Safety Rules for AI Agents above provide a quick-reference checklist derived from these levels.

| Operation | Level | Rationale |
|-----------|-------|-----------|
| Create working branch | 1 — Automatic | Low risk, fully reversible (delete the branch). |
| Create checkpoint tag | 1 — Automatic | Additive, no state change. |
| Commit on working branch | 1 — Automatic | Scoped to working branch, reversible (revert). |
| Push branch to remote | 1 — Automatic | Sharing work, fully reversible (delete remote branch). |
| Push tags to remote | 1 — Automatic | Additive, reversible (delete remote tag). |
| Merge to `master` (non-governance) | 2 — Agent judgment | Changes the protected baseline. Agent verifies validation passed and gate criteria met. |
| Merge to `master` (governance changes) | 3 — Human approval | Governance changes are irreversible in effect. Human reviews the diff. |
| Create version tag | 2 — Agent judgment | Marks a milestone. Agent verifies wave completion criteria. |
| Delete branch (local or remote) | 2 — Agent judgment | Destructive but recoverable (reflog). Agent confirms branch is merged or abandoned. |
| Revert a merge on `master` | 2 — Agent judgment | Corrective action. Agent assesses impact and documents reasoning. |
| Hard reset on `master` | 3 — Human approval | Destructive, rewrites history. Emergency only. |
| Force-push | 3 — Human approval | Destructive, rewrites remote history. Explicit human instruction required. |
| Rewrite history (rebase, amend, filter-branch) | 3 — Human approval | Destructive. Explicit human instruction required. |
| Delete tags | 3 — Human approval | Tags are immutable anchors. Deletion requires explicit justification. |

---

## Convention Adoption and Historical Exceptions

### Effective Dates

Git conventions apply *going forward from their adoption date*, not retroactively to the entire repository history. A convention cannot meaningfully govern commits, branches, or tags that were created before the convention existed.

Each convention section in this document has an implicit effective date — the date the convention was approved and merged to `master`. For the initial version of this document (Wave 8.3, merged 2026-03-17), all conventions take effect from that date. Future additions to this document should note their effective date if it differs from the document's original adoption.

The `git_hygiene.py` detection tool respects effective dates through configuration. The `master_commit_convention_start` config key tells Check 3 (direct master commits) to skip commits before the branching convention existed. The `pre_wave_tag_exceptions` config key tells Check 4 (pre-wave tags) to skip waves that predate the checkpoint tag convention. This is not suppression of findings — it is honest scoping of what the convention governs.

**Principle:** Conventions govern future behaviour. Historical non-compliance is documented, not falsified. Creating retroactive tags or renaming historical branches to match current patterns would misrepresent when the convention was followed. The correct response to pre-convention history is: acknowledge it, document the exceptions in the tool config with rationale, and ensure the convention is followed going forward.

### Managing Historical Exceptions

When a convention is adopted and the detection tool surfaces pre-convention debt:

1. **Items that can be fixed without falsifying the record** — fix them. Example: deleting merged branches with pre-convention names. The branches are dead pointers; deleting them removes clutter without misrepresenting history.
2. **Items that cannot be fixed without falsifying the record** — document them as known exceptions. Example: missing pre-wave checkpoint tags for waves completed before the tagging convention existed. Creating those tags now would misrepresent when the checkpoint was taken.
3. **Exception documentation lives in the tool config** (`am.conf`), not in this governance document. The config is the operational layer; this document is the policy layer. The config entries must include comments explaining *why* the exception exists, tracing back to this section.

### Branch Cleanup Timing

Branch cleanup is part of the merge ritual, not a deferred task. When a working branch is merged to `master`:

1. Delete the branch locally: `git branch -d <branch-name>`
2. Delete the branch remotely: `git push origin --delete <branch-name>`
3. Both steps happen in the same session as the merge.

If cleanup is missed, `git_hygiene.py` Check 1 (branch naming) and Check 2 (stale branches) serve as the safety net. But the safety net is not the workflow — the workflow is immediate cleanup at merge time. Stale merged branches are noise that obscures the branch list and generates unnecessary findings.

---

## Derivation from Foundations

**Law 2 — Action Properties.** All actions must be verifiable, reversible, and accountable. This is the primary foundation for the entire document. Git provides all three properties natively: every action is logged (verifiable), most are reversible (revert, reset, branch deletion), and `git log` provides full accountability. The conventions ensure these properties are preserved — squash merges are forbidden because they destroy accountability, force-push is Level 3 because it destroys verifiability.

**Law 3 — Economy.** Branch when needed, not always. Commit messages follow accepted formats rather than requiring rigid templates. The escalation levels scale effort with risk. Trivial operations are Level 1; only destructive operations require Level 3.

**D1 — Deterministic Control Surfaces.** Git conventions are deterministic rules — branch naming is a pattern match, commit format is a pattern match, merge prerequisites are checkable conditions. This makes them suitable for mechanical enforcement (`git_hygiene.py`) and automation (Wave 8.4).

**D3 — Controlled Evolution.** The wave git workflow follows the pipeline stages in order. Checkpoint tags before branching ensure rollback is always possible. Validation before merging ensures quality gates are passed. Each step builds on the previous one.

**D4 — Human Sovereignty.** Destructive operations (force-push, hard reset, history rewrite) require human approval. The human is always at the top of the authority chain for irreversible actions.

**D6 — Separation of Powers.** The entity that builds (Worker on the working branch) is not the entity that validates (orchestrator tools), and the entity that validates is not the entity that approves the merge (human for governance, Reviewer for standard work).

---

## Relationship to Other Governance

**Authority chain:** [[Agent Maestro — Foundations]] → [[Agent Maestro — Vault Rules]] (Rule 67 delegates to this document) → **AM — Git Conventions** (the single authoritative reference for git operations) → `git_hygiene.py` (mechanical detection) → future automation tools.

Vault Rule 67 establishes the principle (Law 2 for version control) and delegates all git conventions to this document. This eliminates the duplication that previously existed across Rules 67–72, which were consolidated into a single pointer rule when this document was promoted to governance. [[AM — Tool Conventions]] governs *how* the detection tool (`git_hygiene.py`) is built. [[AM — Artifact Lifecycles]] governs the pipeline process that the wave git workflow implements.

## When It Applies

When performing any git operation in the AM repository. When building `git_hygiene.py` (Wave 8.3) — this document is the spec for what the tool checks. When designing git workflow automation (Wave 8.4) — this document is the spec for what the automation implements. When onboarding a new contributor (human or AI) to the vault.

## Audit

**Auditor context:** Same-session audit by the drafting agent. D6 tension acknowledged. Adversarial lens applied with extra rigour. Human review is the definitive gate.

### Alignment

**Question:** Does this document serve what's above it?

**Finding AL-1: A weight-70 document cannot resolve a discrepancy in a weight-85 document.** The document states that `master` "resolves the discrepancy" with Vault Rule 67, which says `main`. But [[Agent Maestro — Vault Rules]] has authority_weight 85; this document has 70. A lower-authority document cannot override a higher-authority document — that violates the governance hierarchy itself. The document should *recommend* that Vault Rule 67 be updated to say `master` (with human approval, since Vault Rules are governance), not *declare* the resolution. **Severity: Medium.** The resolution is correct (the repo uses `master`), but the authority chain must be respected. The fix is to reframe: this document adopts `master` as the convention and notes that Vault Rule 67 should be updated to match.

**Finding AL-2: "Supersedes" requires process, not declaration.** The Purpose section states this document "supersedes [[Git Best Practices for AI-Assisted Builds]]." But supersession of an existing document requires archiving the old document and updating any references to it. The document declares intent but doesn't specify the archival process. **Severity: Low.** The archival is a procedural step that happens at approval time, not a content flaw. But the language should be softened from "supersedes" to "replaces, upon approval" to acknowledge the process hasn't happened yet.

**Overall alignment: PASS.** The document faithfully extends Vault Rules 67–72 with operational detail. Every convention traces to the Foundations. The two findings are about governance process, not content alignment.

### Integrity

**Question:** Is this internally sound?

**Finding IN-1: Safety Rule 10 conflicts with D4 (Human Sovereignty).** Rule 10 states agents must not "bypass validation steps — even if the human requests speed." But D4 says the human is always at the top of the authority chain. If a human explicitly instructs an agent to skip validation, does the agent obey D4 (follow the human) or Rule 10 (refuse)? This is a genuine tension. The Foundations resolve it: D4 says "human sovereignty means the human can override" — but it also says the agent should escalate concerns. The rule as written is too absolute. **Severity: Medium.** The fix is to reframe Rule 10: agents must not *silently* bypass validation. If the human explicitly instructs skipping, the agent should note the risk and comply — but log the override. This preserves accountability (Law 2) while respecting sovereignty (D4).

**Finding IN-2: The "trivial housekeeping" exception for direct master commits is mechanically unenforceable.** The document allows "trivial housekeeping (typo fixes, whitespace)" directly on `master`. But `git_hygiene.py` cannot distinguish a trivial commit from a non-trivial one — it can only detect that a non-merge commit landed on `master`. This exception makes the detection tool's job ambiguous: should it flag all non-merge commits on master (producing false positives on legitimate trivial commits) or try to assess triviality (crossing into semantic territory)? **Severity: Medium.** Two options: (a) remove the exception entirely — all work branches, no exceptions, which is stricter but mechanically clean; or (b) keep the exception but specify that `git_hygiene.py` flags all non-merge master commits as *warnings* rather than findings, and the human evaluates whether the exception applies. Option (b) is more practical and aligns with Convention 7 (Conservative).

**Finding IN-3: Minimum commit message length of 10 characters is too restrictive.** "Fix typo" is 8 characters and is a perfectly descriptive commit message. "Add tag" is 7 characters and is clear. The 10-character floor would produce false positives on legitimate short-but-descriptive messages, violating Convention 7. **Severity: Low.** Either lower the threshold (e.g., 5 characters, which eliminates single-word messages without penalising short descriptive ones) or drop the length check entirely and rely on the pattern-match checks (commit must match one of the three accepted formats or be clearly descriptive).

**Finding IN-4: AI agent safety rules partially duplicate the escalation levels table.** The "Agents MUST NOT" rules (6–9) largely overlap with the Level 3 entries in the Escalation Levels table. Both say agents must not force-push, rewrite history, delete tags, or work on master — expressed differently in two places. **Severity: Low.** The duplication is intentional: the safety rules are a quick-reference checklist for agents loading this document; the escalation table is the comprehensive reference. But the document should cross-reference them explicitly to avoid the impression of inconsistency.

**Overall integrity: CONDITIONAL PASS.** IN-1 and IN-2 require resolution. IN-3 and IN-4 are improvements.

### Viability

**Question:** Is every section earning its place?

**Finding VI-1: Recovery Procedures reads more like a runbook than governance.** The section provides specific `git` commands for each recovery scenario. This is operationally useful but is implementation detail rather than governance principle. The governance-level statement is: "recovery must be immediate and mechanical, preferring revert over reset" — the specific commands could live in a README or operational guide. **Severity: Low.** The section is short and useful. Including the commands makes the document self-contained — an operator doesn't need to look elsewhere. Law 3 argues for keeping it here rather than creating a separate reference. Leave it, but note that it serves a dual purpose (governance principle + operational reference).

**Overall viability: PASS.** Every section earns its place. The document covers conventions (what the rules are), workflows (how they integrate with the pipeline), escalation (who can do what), safety (what agents must and must not do), and recovery (what to do when things go wrong). The Recovery Procedures finding is a style note, not a viability concern.

### Summary of Findings

| ID | Finding | Severity | Resolution |
|----|---------|----------|------------|
| AL-1 | Weight-70 doc cannot resolve weight-85 discrepancy | Medium | **RESOLVED.** Vault Rules 67–72 consolidated into single Rule 67 pointer (with human approval). This document is now the delegated authority — no upward override. |
| AL-2 | "Supersedes" requires archival process | Low | **RESOLVED.** Purpose section now says "replaces, upon approval" and notes the archival will happen at approval time. |
| IN-1 | Safety Rule 10 conflicts with D4 (Human Sovereignty) | Medium | **RESOLVED.** Rule 10 reframed: agents must not *silently* bypass validation. If the human explicitly overrides, the agent notes the risk, complies, and logs the override. Law 2 preserved, D4 respected. |
| IN-2 | Trivial housekeeping exception is mechanically unenforceable | Medium | **RESOLVED.** Detection note added to the Protected Baseline section: `git_hygiene.py` flags all non-merge master commits as warnings (not findings). Human evaluates the exception. Convention 7 honoured. |
| IN-3 | 10-character minimum is too restrictive | Low | **RESOLVED.** Lowered to 5 characters. Eliminates throwaway messages without penalising legitimate short descriptions. |
| IN-4 | Safety rules duplicate escalation table | Low | **RESOLVED.** Cross-references added between Safety Rules and Escalation Levels sections. Duplication is intentional (quick-reference vs comprehensive), now explicitly stated. |
| VI-1 | Recovery section is runbook-level detail | Low | **Accepted.** Self-contained is preferable to creating a separate reference. |

### Audit Verdict

**PASS.** All findings resolved. The document is well-structured, comprehensive, and faithfully extends the governance it derives from. The Foundations traceability is thorough and accurate. The escalation levels table and wave git workflow are the strongest sections — they provide the governance foundation for both Wave 8.3 and 8.4.

AL-1 was resolved structurally (Vault Rules consolidation, approved by human). IN-1 was resolved by reframing Safety Rule 10 to balance Law 2 and D4. IN-2, IN-3, and IN-4 were resolved as improvements. VI-1 was accepted. The document is ready for human approval.

## Related

- [[Agent Maestro — Foundations]] — the kernel (Law 2, Law 3, D1, D3, D4, D6)
- [[Agent Maestro — Vault Rules]] — Rule 67 delegates git conventions to this document
- [[AM — Tool Conventions]] — governs how detection tools are built
- [[AM — Artifact Lifecycles]] — governs the pipeline process the wave workflow implements
- [[AM — Roadmap]] — Wave 8.3 (detection), Wave 8.4 (automation)
