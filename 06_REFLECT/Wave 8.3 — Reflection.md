---
title: "Wave 8.3 — Reflection"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Proposal — Wave 8.3 Git Hygiene Detection]]"
    - "[[AM — Git Conventions]]"
    - "[[AM — Tool Conventions]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Integrity Layers]]"
    - "[[Wave 8.2 — Reflection]]"
tags: [reflection, wave-8, git-ops, git-hygiene, detection]
---

# Wave 8.3 — Reflection

## What Happened

Wave 8.3 built `git_hygiene.py`: a single Python tool that detects violations of [[AM — Git Conventions]] across seven independent checks. It integrates into the existing vault-maintenance orchestrator, runs after the pipeline enforcement tools, and produces a Markdown report with findings and warnings.

**The tool — seven checks:**
1. **Branch naming** — local branches match configured patterns (`^wave-\d+\.\d+-[a-z0-9-]+$`, `^fix-[a-z0-9-]+$`, `^housekeeping-[a-z0-9-]+$`)
2. **Stale branches** — unmerged branches whose last commit exceeds the configured threshold (30 days)
3. **Direct master commits** — non-merge commits on `master` (warnings, not findings — the housekeeping exception is mechanically unenforceable)
4. **Pre-wave tag presence** — completed waves from the Roadmap have a corresponding `pre-wave-X.Y` tag
5. **Tag naming consistency** — all tags match configured patterns
6. **Commit message format** — recent non-merge commits meet quality criteria (format pattern match OR minimum length; reject patterns are hard failures)
7. **Uncommitted changes** — dirty working tree (warning, suppressed via `check_uncommitted_changes: false` during active sessions)

**Design decisions implemented:**
- Best-effort error isolation: each check runs independently, errors reported as warnings, exit code 2 only if no checks complete
- `subprocess` with no library dependencies — git CLI provides all needed data
- `vault_model.py` reused for config loading, Roadmap parsing (Check 4), and report writing
- `master_branch` and all patterns configurable — no hardcoded AM assumptions
- Merge commits exempt from Check 6 message validation — git generates those messages

**Supporting deliverables:**
- `config/am.conf` extended with git hygiene configuration keys
- `orchestrate.sh` updated with `git_hygiene.py` entry (after pipeline enforcement tools)
- `README.md` updated with Wave 8.3 tool documentation, config schema, and architecture note
- `SYSTEM_MAP.md` updated

## What Was Learned

**The tool worked on the first run.** 11 findings, 23 warnings, no false positives. This continued the pattern from Wave 8.2 — when the spec is mechanically precise, the implementation follows directly and the first test produces real signal immediately.

**The findings confirm the pre-wave history:**
- Five branches use pre-convention naming schemes (`phase-c-capture-processing`, `phase-d-execution-architecture`, `wave-5.1-v1.0.0-migration`, `wave-6-mechanical-integrity`, `wave-7-scheduled-execution`). These are real naming drift, correctly detected.
- Five completed waves lack pre-wave checkpoint tags (Waves 5, 5.1, 5.2, 7, 8.1). These tags were not part of the convention when those waves were built. Real findings.
- `pre-v1.0.0-migration` tag doesn't match any pattern. Historical naming, correctly flagged.

**The Check 3 warnings surface real debt.** All master commits are direct (no merge commits in the history). The repository has been worked on master-first throughout its history. This was before the branching convention was established. The warnings are real and informative — the human needs to see this. This is exactly the drift detection the wave was built to provide.

**Stale branches are not a problem here.** The old pre-convention branches (`phase-c`, `phase-d`, `wave-5.1`, etc.) show as clean in Check 2 because all their commits are reachable from `master` (their work was committed directly to master). Git correctly identifies them as "merged" even though they were never merged via a merge commit. This is expected — the stale check rightly skips already-reachable branches.

**IN-1 (regex escaping) resolved by a simpler approach.** The audit finding noted a regex escaping bug for the wave ID in Check 4. The implementation avoided this entirely by using exact string construction (`f"pre-wave-{wave_id}"`) and set membership testing rather than regex matching. The simpler approach is also the correct one — Law 3 vindicated.

**Wave 8.3 was faster than Wave 8.2.** One tool, no new library, proven patterns from Wave 8.2. The estimate was accurate: smaller scope, simpler implementation, faster execution. The scope degradation plan was never needed.

## Was the Wave's Question Answered?

Wave 8.3 asked: **Can AM detect when its own git conventions are not being followed?**

Yes. The seven checks cover the full surface of [[AM — Git Conventions]] that is mechanically detectable. Branch naming, stale branches, direct master commits, pre-wave tags, tag naming, commit message quality, and uncommitted state — all of these now produce findings or warnings in the vault health report on every orchestrator run.

## Concept Promotion Check

No new concepts emerged from Wave 8.3. The wave produced tooling against an existing governance spec. The existing concepts (Mechanical Integrity, Self-Observation) already frame the layer this tool operates in. No concept promotion needed.

## What Comes Next

**Immediate debt surfaced by Wave 8.3:**
1. Five branches with pre-convention names — human decision: leave (historical) or rename/delete
2. Five completed waves with no pre-wave checkpoint tags — cannot be retroactively added (tags would misrepresent when the checkpoint existed). Document as known historical gap.
3. All master commits are direct — the full history predates the branching convention. Document as known historical state; going forward the convention applies.
4. `pre-v1.0.0-migration` tag — evaluate whether to keep or delete (deletion requires Level 3 human approval per Git Conventions)

**Stage 1 completion assessment:**
Wave 8.3 was the last Stage 1 wave in the roadmap. The mechanical integrity stack is now complete:
- **Structural** (Wave 6): vault shape, YAML validity, link integrity, naming
- **Process** (Wave 8.2): lifecycle rules, pipeline gate compliance
- **Git** (Wave 8.3): version control convention compliance

Stage 1 exit criteria should now be evaluated. See [[AM — Strategy]] and [[AM — Roadmap]].

**Wave 9 — Self-Observation** is next. AM measures its own operational behaviour — session frequency, finding trends, wave velocity. This requires the mechanical integrity stack to be stable (it now is).

**Wave 8.4 — Git Workflow Automation** remains in the register. Detection is proven; prevention and automation are the next step. Pre-commit hooks (prevention) and workflow automation (branch creation, checkpoint tagging, merge orchestration) need their own design conversation. Wave 8.3's detection findings provide the evidence base for what automation is most needed.
