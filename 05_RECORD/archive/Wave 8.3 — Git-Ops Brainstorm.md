---
title: "Wave 8.3 — Git-Ops Brainstorm"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 8 — Capture Seed]]"
    - "[[AM — Future Waves Register]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Tool Conventions]]"
    - "[[AM — Git Conventions]]"
    - "[[Proposal — Wave 8.2 Pipeline Enforcement Tooling]]"
tags: [capture, brainstorm, wave-8, git-ops, git-hygiene]
---

# Wave 8.3 — Git-Ops Brainstorm

**Source:** Design conversation during Wave 8.2 proposal session (2026-03-17), [[Wave 8 — Capture Seed]], [[AM — Future Waves Register]] Wave 8.3 entry.

## Context

Wave 8.2 builds pipeline enforcement tooling — mechanical checks that verify AM's process is followed. Wave 8.3 extends the same principle to git: are AM's git conventions being followed?

The Charter's Build Protocol defines git conventions (feature branches, pre-wave tags, commit format). [[AM — Git Conventions]] (governance, authority_weight 70, approved 2026-03-17) is now the authoritative reference, replacing the earlier [[Git Best Practices for AI-Assisted Builds]] (archived). AM — Git Conventions defines branch naming, tag naming, commit formats, merge strategy, recovery procedures, AI safety rules, and escalation levels — and is the spec that `git_hygiene.py` enforces mechanically. The git history shows inconsistency: branch naming drift (`phase-c-capture-processing` vs `wave-7-scheduled-execution`), tag naming drift (`pre-wave-6` vs `pre-wave7`), commit format mixing (`SES-XXX:` vs `Wave X:` vs plain), stale unmerged branches, and occasional work committed directly to `master`.

## Wave 8.3 Question

**Can AM detect when its own git conventions are not being followed?**

## Proposed Scope: One Detection Tool

**`git_hygiene.py`** — a single Python tool integrated into the vault-maintenance orchestrator, following the same read-check-report pattern as the Wave 6 and 8.2 tools.

### Candidate Checks

| # | Check | What it detects | Source convention |
|---|-------|----------------|-------------------|
| 1 | **Branch naming** | Branches that don't match the configured naming convention (e.g., `wave-X.Y-description` or `fix-description`). | AM — Git Conventions §Branch Naming |
| 2 | **Stale branches** | Branches older than a configured threshold (e.g., 30 days) that haven't been merged. | AM — Git Conventions §Stale Branches |
| 3 | **Direct commits to master** | Non-merge commits on `master` — flagged as **warnings** (not findings) per the trivial housekeeping exception. Human evaluates. | AM — Git Conventions §Protected Baseline |
| 4 | **Pre-wave tag presence** | Completed waves (from Roadmap ✓) that don't have a corresponding `pre-wave-X.Y` tag. | AM — Git Conventions §Checkpoint Tags |
| 5 | **Tag naming consistency** | Tags that don't match the configured naming convention (e.g., `pre-wave-X.Y` or `vX.Y.Z`). | AM — Git Conventions §Tag Conventions |
| 6 | **Commit message format** | Recent commits (configurable window) whose messages don't match any of the accepted formats (`SES-XXX: summary`, `Wave X.Y: summary`, or meaningful descriptive text ≥5 characters). | AM — Git Conventions §Commit Conventions |
| 7 | **Uncommitted changes** | Dirty working tree — staged or unstaged changes that haven't been committed. | AM — Git Conventions §Safety Rules (Rule 3) |

### Design Decisions from the Conversation

- **Detection only, not prevention.** Wave 8.3 builds a detection tool that runs through the orchestrator and reports findings. It does not build pre-commit hooks or any intervention mechanism. Detection proves the checks work; prevention (hooks) can follow later if needed. This follows D3 (Controlled Evolution) — prove then enforce.
- **Python, shared vault model.** The tool imports `vault_model.py` (from Wave 8.2) for config loading and Roadmap parsing (Check 4 needs completed wave data). Git-specific operations use Python's `subprocess` to call git commands — no git library dependency.
- **Config-driven conventions.** Branch naming patterns, tag naming patterns, commit format patterns, stale branch threshold, and commit history window are all configurable in `am.conf`. No hardcoded AM-specific assumptions.
- **Conservative on commit message validation.** Check 6 is the most ambiguous — the Charter allows "descriptive message" which is inherently subjective. The tool should only flag clearly bad commits (single-word messages, empty messages, messages below a configurable minimum length). Anything that looks like a reasonable sentence passes. Convention 7 (Conservative) — no false positives on judgment calls.

### What Is Explicitly NOT in Scope for 8.3

**Pre-commit hooks** are a different category of tool — prevention, not detection. They introduce a new trust boundary: a false positive blocks workflow rather than appearing in a report. They live in `.git/hooks/` (not tracked by git, requires separate installation), and they need governance that the Tool Conventions don't currently cover. If hooks earn their place, they can reuse the checks from `git_hygiene.py` — but they belong in a separate effort after detection is proven.

**Git workflow automation** is a fundamentally different concern — see Wave 8.4 below.

---

## Wave 8.4 — Git Workflow Automation (Future)

The design conversation identified a second concern that is distinct from git hygiene detection: **can AM automate the repetitive git workflow steps?**

[[AM — Git Conventions]] now defines the authoritative workflow (§The Wave Git Workflow), including escalation levels for every git operation. The mechanical steps — branch creation, checkpoint tagging, merge after validation, branch cleanup — are currently performed manually. The Capture Seed notes this friction: "manual git operations in Cowork are irritating."

### Why This Is a Separate Wave

Git workflow automation is **action-taking**, not detection. It crosses the Report-Don't-Repair boundary (Convention 3) in a fundamental way:

- A tool that creates a git branch is **writing state**.
- A tool that creates a commit is **writing state**.
- A tool that merges branches is **writing state and potentially destroying state**.

This is a different trust level from anything in the current tool suite. Convention 3 governs detection tools in `04_EXECUTE/tools/`. Workflow automation isn't detection — it's a new category that needs its own governance.

### What It Would Automate

The [[AM — Git Conventions]] §The Wave Git Workflow maps directly to automatable steps, with escalation levels already defined in §Escalation Levels for Git Operations:

| Step | Current (manual) | Automated | Escalation Level |
|------|-----------------|-----------|-----------------|
| 1. Confirm not on `master` | Human checks | Script checks and warns/blocks | 1 — Automatic |
| 2. Create checkpoint tag | `git tag pre-wave-X.Y` | Script creates tag with standardised name | 1 — Automatic |
| 3. Create working branch | `git checkout -b wave-X.Y-description` | Script creates branch with standardised name from wave context | 1 — Automatic |
| 4. Perform implementation | Human/AI builds | Unchanged — this is the work itself | N/A |
| 5. Run validation | Human runs `orchestrate.sh` | Script runs validation automatically | 1 — Automatic |
| 6. Commit scoped changes | Human commits | Script commits with formatted message | 1 — Automatic |
| 7. Merge to `master` after validation | Human merges | Script merges (Level 2 for non-governance, Level 3 for governance) | 2–3 |
| 8. Push branch and tags | Human pushes | Script pushes | 1 — Automatic |

### Governance It Needs

An "Action Tool Conventions" extension (or section within [[AM — Tool Conventions]]) that defines the trust model for tools that write state. Note: [[AM — Git Conventions]] §Escalation Levels for Git Operations already defines escalation levels for all 14 git operations. The governance extension needs to generalise this pattern for action-taking tools beyond git:

- **Escalation levels per action type.** Already defined for git operations in AM — Git Conventions. The extension generalises the pattern to non-git action tools.
- **Reversibility requirements.** Every automated action must have a documented undo path. Git provides this natively (reflog, branch deletion, tag deletion, revert), but the automation must surface the undo command in its output.
- **Logging requirements.** Every automated action must be logged — what was done, when, by whom/what. Git log provides most of this, but the automation should produce its own operational log entry.
- **Human confirmation for destructive operations.** Merge to `master`, force-push, branch deletion, history rewrite — all require explicit human confirmation (Level 3 per AM — Git Conventions). The automation must pause and ask, not proceed silently.

### What It Depends On

- **Wave 8.3** — the detection checks must exist before automating alongside them.
- **[[AM — Git Conventions]]** — the workflow definition and escalation levels are already written. The automation implements them.
- **A governance extension** — Action Tool Conventions, defining the trust model for state-writing tools (generalising the escalation pattern from AM — Git Conventions).

### The Key Design Question

Does the automation live in `04_EXECUTE/tools/` alongside detection tools (with the Tool Conventions extended), or does it get a separate location that reflects its different trust level? The conversation leaned toward extending the existing conventions rather than creating a parallel structure, but this needs resolution during the 8.4 design conversation.

### Existing Asset

[[AM — Git Conventions]] in `02_KNOWLEDGE/governance/` defines the authoritative workflow, escalation levels, and safety rules. This document is the spec for what 8.4 would automate. The conventions are AM-specific but the automation patterns should be portable (config-driven, not AM-hardcoded), consistent with Convention 2.

---

## Priority Signal

Wave 8.3 (detection) is the natural next step after 8.2. Wave 8.4 (automation) depends on 8.3 and on a governance extension. Both are high-value — detection catches drift, automation eliminates the friction that causes drift in the first place.

---

*This brainstorm captures the design conversation from 2026-03-17. Process through a proposal when Wave 8.2 is complete.*
