---
title: "Proposal — Wave 8.3 Git Hygiene Detection"
type: proposal
status: active
approved: "2026-03-17"
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Git Conventions]]"
    - "[[AM — Tool Conventions]]"
    - "[[AM — Integrity Layers]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Proposal — Wave 8.2 Pipeline Enforcement Tooling]]"
    - "[[Wave 8.3 — Git-Ops Brainstorm]]"
    - "[[Wave 8.2 — Reflection]]"
tags: [proposal, wave-8, git-ops, git-hygiene, detection, mechanical-integrity]
---

# Proposal — Wave 8.3 Git Hygiene Detection

## Problem Statement

AM can now detect structural problems in its vault (Wave 6) and verify that its pipeline process is being followed (Wave 8.2). Both operate on vault content — files, frontmatter, relationships, lifecycles. Neither touches git. Git is where every change is actually recorded, where branches scope work, where tags mark checkpoints, and where merges integrate validated output. If git conventions drift, the version control layer stops serving its purpose as AM's memory of change.

The drift is already visible. The git history shows inconsistencies that accumulated before [[AM — Git Conventions]] was formalised:

- **Branch naming drift.** `phase-c-capture-processing` vs `wave-7-scheduled-execution` — two different naming schemes for the same kind of work.
- **Tag naming drift.** `pre-wave-6` vs `pre-wave7` — inconsistent hyphenation, missing dot separators.
- **Commit format mixing.** `SES-XXX:` vs `Wave X:` vs plain descriptive — all valid, but some commits are single-word throwaways.
- **Stale unmerged branches.** Working branches that were never merged or cleaned up.
- **Direct master commits.** Occasional substantive work committed directly to `master` rather than through a branch.

None of these are detected by any existing tool. The structural tools check files. The pipeline tools check lifecycles. Nothing checks git. [[AM — Git Conventions]] defines the spec; nothing enforces it mechanically.

**Wave 8.3's question:** Can AM detect when its own git conventions are not being followed?

## Proposed Change

**Wave 8.3: Git Hygiene Detection** — build a single Python tool that detects violations of [[AM — Git Conventions]], integrated into the existing vault-maintenance orchestrator.

This is a single-phase wave. No new library is needed — `vault_model.py` (Wave 8.2) already provides config loading and Roadmap parsing. The tool uses Python's `subprocess` module to call git commands; no git library dependency is introduced.

### The Tool: `git_hygiene.py`

**Location:** `04_EXECUTE/tools/vault-maintenance/`

A single Python tool following the read-check-report pattern from [[AM — Tool Conventions]]. It reads git state (branches, tags, log, working tree status), checks it against conventions declared in `am.conf`, and produces a Markdown report with findings and warnings. Exit codes: 0 (clean), 1 (findings), 2 (error).

**Error isolation:** Each check runs independently within the tool. If a check encounters an error (e.g., Check 4's Roadmap parsing fails), that check's error is reported in the report and the remaining checks continue. The tool's exit code is determined by the aggregate result: 0 if all checks passed, 1 if any check produced findings (even if other checks errored), 2 only if *no* checks completed successfully. This best-effort strategy preserves the value of healthy checks when one check fails, while still surfacing the error. It follows Tool Conventions Safety Rule 5 — fail safe, but with explicit best-effort behaviour rather than silent partial results.

### Seven Checks

#### Check 1: Branch Naming

**Detects:** Branches whose names do not match any configured naming pattern.

**Source:** AM — Git Conventions §Branch Naming.

**Implementation:** The tool retrieves all local branches via `git branch --list`. Each branch name is tested against the configured patterns. Branches that match no pattern are reported as findings. The `master` branch is always exempt.

**Config:**

```
git_branch_patterns:
  - "^wave-\\d+\\.\\d+-[a-z0-9-]+$"
  - "^fix-[a-z0-9-]+$"
  - "^housekeeping-[a-z0-9-]+$"
```

**Design note:** Patterns are regexes, not globs. This allows precise validation of the naming structure (mandatory dot separator in wave branches, lowercase-only, etc.) while keeping patterns configurable for non-AM vaults.

#### Check 2: Stale Branches

**Detects:** Branches whose most recent commit is older than a configured threshold and that have not been merged into `master`.

**Source:** AM — Git Conventions §Stale Branches.

**Implementation:** For each local branch, the tool retrieves the date of the most recent commit via `git log -1 --format=%ci <branch>`. Branches whose last commit is older than `stale_branch_threshold_days` and that are not fully merged into `master` (checked via `git branch --merged master`) are reported as findings. The `master` branch is exempt.

**Config:**

```
stale_branch_threshold_days: 30
```

#### Check 3: Direct Commits to Master

**Detects:** Non-merge commits on `master`.

**Source:** AM — Git Conventions §The Protected Baseline.

**Implementation:** The tool retrieves the last N commits on `master` (configurable window) via `git log --first-parent master`. Commits with more than one parent are merge commits and are exempt. Commits with a single parent are direct commits and are reported as **warnings** (not findings).

**Why warnings, not findings:** AM — Git Conventions explicitly allows "trivial housekeeping" directly on `master`. The tool cannot mechanically distinguish trivial from non-trivial. Reporting these as warnings preserves the signal (direct commits happened) without producing false positives on legitimate housekeeping. The human evaluates. This follows Convention 7 (Conservative) and is explicitly specified in the Git Conventions detection note.

The warning section of the report is structurally distinct from the findings section, following the pattern established by `reflection_completeness.py` in Wave 8.2 (which uses "Warnings (uncertain)" for the same purpose).

**Config:**

```
master_commit_window: 50
```

#### Check 4: Pre-Wave Tag Presence

**Detects:** Completed waves (from the Roadmap) that have no corresponding `pre-wave-X.Y` tag.

**Source:** AM — Git Conventions §Checkpoint Tags.

**Implementation:** The tool uses `vault_model.py`'s `parse_completed_waves()` to identify completed waves from the [[AM — Roadmap]]. For each completed wave, it checks whether a tag matching the `pre-wave-X.Y` pattern exists (via `git tag --list`). Missing tags are reported as findings.

**Design note:** This reuses the same Roadmap parsing logic that Wave 8.2 tools use, with the same conservative fallback (skip unparseable entries, report warnings rather than false findings). The fragility concern was resolved in the Wave 8.2 proposal (AL-2): the tools consume Roadmap data as input with graceful degradation, they do not validate the Roadmap's own format.

**Config:**

```
pre_wave_tag_pattern: "^pre-wave-{wave_id}$"
```

Where `{wave_id}` is substituted with the wave identifier (e.g., `8.2`). The pattern allows for the historical inconsistencies in tag naming (`pre-wave-6` vs `pre-wave7`) to be detected rather than silently accepted.

#### Check 5: Tag Naming Consistency

**Detects:** Tags that do not match any configured naming pattern.

**Source:** AM — Git Conventions §Tag Conventions.

**Implementation:** The tool retrieves all tags via `git tag --list`. Each tag is tested against the configured patterns. Tags that match no pattern are reported as findings.

**Config:**

```
git_tag_patterns:
  - "^pre-wave-\\d+\\.\\d+$"
  - "^pre-[a-z0-9-]+$"
  - "^v\\d+\\.\\d+\\.\\d+$"
```

**Design note:** The historical tags that predate the conventions (`pre-wave7`, `pre-wave-6`) will likely be flagged as findings. This is correct — they are real naming inconsistencies. The findings are informational: the tags already exist and should not be renamed (tags are immutable per convention), but the report documents the drift for awareness.

#### Check 6: Commit Message Format

**Detects:** Recent commits whose messages do not match any accepted format and are below the configured minimum quality threshold.

**Source:** AM — Git Conventions §Commit Conventions.

**Implementation:** The tool retrieves the last N commits (configurable window) on the current branch via `git log --format=%H|%s`. Each commit's subject line is tested against three criteria:

1. **Format match.** Does the message match one of the accepted patterns (session-scoped, wave-scoped, or descriptive)?
2. **Minimum length.** Is the message at least `commit_min_length` characters?
3. **Not a known bad pattern.** Single-word messages, empty messages, and messages matching a configurable reject list (e.g., `^(wip|stuff|updates|fixes|test)$`) are flagged.

A commit is reported as a finding only if it fails **both** the format match and the minimum length check, **or** matches a known bad pattern. This layered approach avoids false positives: a commit that doesn't match `SES-XXX:` or `Wave X.Y:` but is a reasonable descriptive sentence passes the length check and is not flagged.

**Config:**

```
commit_message_window: 50
commit_min_length: 5
commit_format_patterns:
  - "^SES-\\d{3}:"
  - "^Wave \\d+\\.\\d+:"
commit_reject_patterns:
  - "^(wip|stuff|updates|fixes|test|tmp|asdf)$"
```

**Design note:** This is the most conservative check in the suite. The Git Conventions allow "descriptive message" as a format, which is inherently subjective. The tool operationalises "descriptive" as: at least 5 characters, not a single throwaway word. Anything that looks like a reasonable sentence passes. Convention 7 (Conservative) — no false positives on judgment calls.

Merge commits are exempt from commit message validation. Their messages are generated by git and follow git's own conventions, not AM's.

#### Check 7: Uncommitted Changes

**Detects:** Dirty working tree — staged or unstaged changes.

**Source:** AM — Git Conventions §Safety Rules (Rule 3).

**Implementation:** The tool runs `git status --porcelain`. If the output is non-empty, the tool reports a warning listing the number of staged and unstaged files.

**Why a warning, not a finding:** A dirty working tree is normal during active development. It only becomes a problem if work is left uncommitted at session close. The tool cannot determine whether the current state is "mid-session work in progress" or "forgotten uncommitted changes." Reporting as a warning preserves the signal without false-positive penalising active work.

**Config:**

```
check_uncommitted_changes: true
```

The check is enabled by default but can be disabled via config for active-session runs where uncommitted changes are expected. This prevents warning fatigue — a warning that fires every time becomes invisible and desensitises the reader to other, more meaningful warnings (such as Check 3's direct-master-commit warnings). For end-of-session or CI runs, the check should remain enabled.

### Orchestrator Integration

`git_hygiene.py` is added to the TOOLS array in `orchestrate.sh`, after the Wave 8.2 pipeline enforcement tools:

```bash
TOOLS=(
    # Wave 6 — Structural integrity
    "structure_check.sh:Structure Check"
    "yaml_validation.sh:YAML Validation"
    "broken_links.sh:Broken Links"
    "orphan_detection.sh:Orphan Detection"
    "stub_detection.sh:Stub Detection"
    "naming_validation.sh:Naming Validation"
    "inventory.sh:Inventory"
    # Wave 8.2 — Pipeline enforcement
    "capture_triage.py:Capture Triage"
    "proposal_lifecycle.py:Proposal Lifecycle"
    "reflection_completeness.py:Reflection Completeness"
    "concept_lifecycle.py:Concept Lifecycle"
    "governance_compliance.py:Governance Compliance"
    # Wave 8.3 — Git hygiene
    "git_hygiene.py:Git Hygiene"
)
```

**Ordering rationale:** Git hygiene runs after vault-content checks. The git checks are independent of vault state — they operate on git metadata, not file content — so the ordering is a convention for report readability (structural → process → git), not a dependency. The tool can run standalone with no dependency on prior tools.

**Git availability check:** The tool must verify that the vault root is inside a git repository (`git rev-parse --git-dir`) before running any checks. If the vault is not a git repo, the tool exits with code 2 (error) and a clear message. This handles the portability case: a non-git vault simply skips the tool.

### Config Additions Summary

All new config keys added to `am.conf`:

```
# Git hygiene (git_hygiene.py)
git_branch_patterns:
  - "^wave-\\d+\\.\\d+-[a-z0-9-]+$"
  - "^fix-[a-z0-9-]+$"
  - "^housekeeping-[a-z0-9-]+$"
stale_branch_threshold_days: 30
master_branch: "master"
master_commit_window: 50
pre_wave_tag_pattern: "^pre-wave-{wave_id}$"
git_tag_patterns:
  - "^pre-wave-\\d+\\.\\d+$"
  - "^pre-[a-z0-9-]+$"
  - "^v\\d+\\.\\d+\\.\\d+$"
commit_message_window: 50
commit_min_length: 5
commit_format_patterns:
  - "^SES-\\d{3}:"
  - "^Wave \\d+\\.\\d+:"
commit_reject_patterns:
  - "^(wip|stuff|updates|fixes|test|tmp|asdf)$"
check_uncommitted_changes: true
```

**Design note:** `master_branch` is configurable rather than hardcoded. If the repository ever renames to `main`, only the config changes — the tool code is unaffected. Convention 2 (Config-Driven).

### Modifications to Existing Artifacts

| Artifact | Change |
|----------|--------|
| `am.conf` | Extended with git hygiene config keys |
| `orchestrate.sh` | One new entry in TOOLS array |
| `README.md` | Updated with Wave 8.3 tool documentation |
| `SYSTEM_MAP.md` | Updated to reflect new tool |

No changes to governance documents. No changes to existing tools. No changes to `vault_model.py` — the existing `parse_completed_waves()` and config loading functions are sufficient.

## Scope Degradation Plan

If time pressure or unexpected complexity builds:

**Minimum viable Wave 8.3** (Checks 1, 2, 5 only — naming and staleness):
- Branch naming, stale branches, tag naming. These are the simplest checks (pattern matching against a list), require no Roadmap parsing, and catch the most visible drift. They answer the wave's question with the smallest scope.

**Standard Wave 8.3** (Checks 1–5 — all naming, staleness, and tag presence):
- Adds direct-master detection and pre-wave tag verification. Covers all structural git conventions. Check 4 introduces the Roadmap dependency (proven in Wave 8.2).

**Full Wave 8.3** (all seven checks):
- Adds commit message validation and uncommitted changes detection. These are the most nuanced checks and produce warnings rather than hard findings in several cases.

## What Is NOT in Scope

| Item | Why deferred | Revisit when |
|------|-------------|--------------|
| Pre-commit hooks | Prevention, not detection. Different trust boundary — false positives block workflow rather than appearing in a report. Lives in `.git/hooks/` (not tracked). Needs separate governance for intervention tools. | After detection is proven and Wave 8.4 governance extension addresses action-taking tools |
| Git workflow automation | Action-taking (branch creation, tagging, merging). Crosses the report-don't-repair boundary. Needs "Action Tool Conventions" governance extension. | Wave 8.4 — depends on 8.3 detection and governance extension |
| Remote branch analysis | `git branch -r` adds complexity (fetch requirements, remote availability). Local branches are sufficient for convention enforcement. | If remote drift becomes a problem |
| Commit body analysis | The tool checks the subject line only. Multi-line commit body analysis (e.g., verifying co-author tags, checking for issue references) adds complexity with low current value. | If commit body conventions are formalised |
| Historical remediation | The tool will flag historical naming drift (old tags, old branches). It does not fix them. Tags are immutable per convention; branches may need manual evaluation. | Human housekeeping session |

## Traceability

| Decision | Foundation |
|----------|-----------|
| Build a detection tool for git conventions | [[AM — Git Conventions]] is the spec; this tool mechanically enforces it. [[AM — Integrity Layers]] — git hygiene is Mechanical Integrity |
| Single tool, not multiple | Law 3 (Economy) — all seven checks operate on git metadata from the same repository. Splitting into multiple tools would mean multiple subprocess calls to the same git commands. One tool, one report. Convention 4 (Independence) is satisfied: the tool is independently runnable and self-contained |
| Python with subprocess for git | Law 3 (Economy) — reuses `vault_model.py` for config loading and Roadmap parsing. Python's subprocess provides clean capture of git command output. No new dependency (no gitpython, no pygit2) |
| Direct-master commits as warnings, not findings | Convention 7 (Conservative) — the housekeeping exception in Git Conventions is mechanically unenforceable. Warnings preserve signal without false positives. Explicitly specified in Git Conventions detection note (IN-2 resolution) |
| Uncommitted changes as warnings, not findings | Convention 7 (Conservative) — dirty tree is normal during active work. Cannot distinguish "in progress" from "forgotten" |
| Conservative commit message validation | Convention 7 (Conservative) — "descriptive message" is subjective. Tool operationalises it as minimum length + reject list. Anything resembling a reasonable sentence passes |
| Config-driven patterns and thresholds | Convention 2 (Config-Driven) — branch patterns, tag patterns, commit patterns, stale threshold, commit window all configurable. No hardcoded AM assumptions |
| Git availability check at startup | Convention 5 (Meaningful Exit Codes) — non-git vault exits with code 2, not a cryptic error |
| Merge commits exempt from message validation | Git generates merge commit messages. They follow git's conventions, not AM's. Enforcing AM format on auto-generated messages would produce false positives |

## Impact Assessment

**What this affects:**
- `04_EXECUTE/tools/vault-maintenance/` — receives `git_hygiene.py`
- `04_EXECUTE/tools/vault-maintenance/config/am.conf` — extended with git hygiene configuration
- `04_EXECUTE/tools/vault-maintenance/orchestrate.sh` — one new entry in TOOLS array
- `04_EXECUTE/tools/vault-maintenance/reports/` — receives `Git_Hygiene_report.md` per run
- `04_EXECUTE/tools/vault-maintenance/README.md` — updated with Wave 8.3 documentation
- `SYSTEM_MAP.md` — updated to reflect new tool

**What this does NOT affect:**
- Governance documents — no changes
- Existing Wave 6 tools — unchanged
- Existing Wave 8.2 tools — unchanged
- `vault_model.py` — unchanged, consumed as-is
- Wave 7 runtime (launchd, summarise_report.py, notify.sh) — unchanged; the orchestrator automatically picks up the new tool
- Vault structure — no new folders

**What could go wrong:**

- **Git not available.** The tool is the first in the suite that depends on git. If the vault is not a git repo (possible for a portable vault copy), the tool must handle this gracefully — exit code 2, clear message, not a stack trace. The git availability check at startup addresses this.
- **Subprocess failures.** Git commands can fail for unexpected reasons (corrupt repo, missing reflog, permissions). Each subprocess call must be wrapped in error handling that produces a clear error message and exits with code 2 rather than propagating a Python traceback.
- **Historical findings volume.** The first run will likely produce many findings — old branches with non-conforming names, old tags with inconsistent naming, old commits with informal messages. This is expected (Wave 8.2 had the same experience — six findings on first run). The findings are real drift that existed before the conventions were formalised. The report documents them; the human decides what to address.
- **Commit window size.** If `commit_message_window` is too large, the tool checks ancient commits that predate any convention. This produces noise. The default of 50 is a reasonable starting point — recent enough to catch current drift, not so deep that every historical commit is audited. The window is configurable.
- **Branch/tag patterns too strict or too loose.** The default patterns are derived directly from Git Conventions. If the patterns are wrong, the tool produces false positives (too strict) or misses drift (too loose). Mitigation: test against the actual repository during development. Adjust patterns in config before declaring the wave complete.

## Alternatives Considered

**Alternative 1: Shell script instead of Python**
Rejected. The tool needs config loading from `am.conf` (YAML), Roadmap parsing for Check 4, and structured report generation. These are all already implemented in `vault_model.py`. A shell script would need to reimplement config parsing or shell out to Python for it — adding complexity rather than reducing it. The Wave 8.2 precedent established Python as the right choice for tools that need data-structure access. The Wave 6 shell tools remain appropriate for their simpler structural checks.

**Alternative 2: Multiple tools (one per check category)**
Rejected. All seven checks operate on git metadata from the same repository. Splitting into separate tools would mean separate subprocess invocations of the same git commands, separate config loading, and separate report generation — duplicating the read phase for no independence benefit. Unlike Wave 8.2, where each tool covers a different artifact family with different data access patterns, the git checks all share one data source (git). One tool is the Law 3 choice.

**Alternative 3: Use gitpython or pygit2 library**
Rejected. Adding a library dependency for seven subprocess calls violates Law 3 (Economy). The git CLI is universally available, well-documented, and produces parseable output. `subprocess` is already used by the test infrastructure. A library adds installation requirements, version management, and API surface area for no measurable benefit at this scale.

**Alternative 4: Integrate git checks into existing pipeline tools**
Rejected. Git conventions and vault content lifecycles are different integrity domains — one checks version control metadata, the other checks file content and frontmatter. Mixing them in one tool muddies the concern boundary. A git finding should be clearly a git problem, not mixed into a proposal lifecycle report. Separation of concerns serves the human reading the report.

**Alternative 5: Build pre-commit hooks instead of (or alongside) detection**
Rejected for this wave. Pre-commit hooks are prevention, not detection. They introduce a different trust boundary: a false positive blocks the developer's workflow rather than appearing in a report they can evaluate. Hooks also live in `.git/hooks/` (not tracked by git), which means they need a separate installation and distribution mechanism. Detection proves the checks work. Prevention can follow in a future wave if the detection tool demonstrates value without false positives. D3 (Controlled Evolution) — prove then enforce.

## Gate Criteria

**This proposal is ready to execute when:**

- [x] Proposal drafted with all required elements
- [x] Adversarial audit completed (alignment, integrity, viability)
- [x] Human (Rob) approves the proposal (2026-03-17)

**Wave 8.3 is complete when:**

- [ ] `git_hygiene.py` implements all seven checks per the specifications above
- [ ] Each check traces to its source convention in [[AM — Git Conventions]]
- [ ] The tool follows [[AM — Tool Conventions]]: config-driven, read-only, exit codes 0/1/2, Markdown report, conservative (no false positives)
- [ ] Checks 3 (direct master commits) and 7 (uncommitted changes) produce warnings, not findings
- [ ] The tool handles non-git vaults gracefully (exit code 2, clear message)
- [ ] The tool handles subprocess failures gracefully (exit code 2, clear message, no tracebacks)
- [ ] `am.conf` extended with all git hygiene configuration keys
- [ ] `orchestrate.sh` updated with `git_hygiene.py` entry
- [ ] Tool tested against the actual repository — all findings are real, no false positives
- [ ] README.md updated with Wave 8.3 documentation
- [ ] SYSTEM_MAP.md updated
- [ ] Wave 8.3 reflection written and filed in `06_REFLECT/`
- [ ] Capture seed for Wave 8.4 created in `01_CAPTURE/`

## Audit

**Auditor context:** This audit is performed by the same agent that drafted the proposal, in the same session. This violates the spirit of D6 (Separation of Powers). The adversarial lens is applied with extra rigour to compensate, but the finding should be noted: a second-session review by a fresh agent would provide stronger separation. The human's review at approval time is the definitive gate.

### Alignment

**Question:** Does this proposal serve what's above it?

**Finding AL-1: Check 4 creates a cross-domain dependency.** The tool is framed as operating on git metadata — branches, tags, commits, working tree status. Six of the seven checks are pure git operations. Check 4 (pre-wave tag presence) breaks this model: it imports `vault_model.py` and calls `parse_completed_waves()`, which reads the Roadmap markdown file — a vault content artifact, not git metadata. This creates a coupling between the git hygiene tool and the vault content layer. If the Roadmap format changes or `vault_model.py`'s parser is updated, the git tool is affected — even though it should notionally operate only on git state.

This is not wrong — the check needs completed wave data, and the Roadmap is the only source of truth. But the proposal should acknowledge the dependency explicitly rather than framing the tool as purely git-scoped. The "no changes to vault_model.py" claim is accurate (the existing API suffices), but the runtime dependency exists and should be visible in the impact assessment.

**Severity: Low.** The dependency is well-understood (same pattern as Wave 8.2) and the vault model API is stable. The coupling is narrow — one function call for one check. If Check 4 is dropped in scope degradation, the dependency disappears entirely. The issue is transparency of framing, not architectural risk.

**Finding AL-2: The proposal claims git hygiene is Mechanical Integrity, but the Integrity Layers document describes Mechanical Integrity's domain as "Structure, syntax, and filesystem state."** Git metadata (branches, tags, commit log) is none of these — it's version control state, which is distinct from filesystem state. The Integrity Layers document was written before git enforcement was contemplated. The proposal correctly identifies that all seven checks are deterministic (same input → same output), which satisfies the Integrity Layers boundary test. But the domain description in the source document doesn't explicitly include git.

**Severity: Low.** The boundary test ("Can the check be expressed as a deterministic rule?") is the authoritative criterion per Integrity Layers, and all seven checks pass it. The domain description is illustrative, not exhaustive. However, the Integrity Layers document may benefit from a note acknowledging git metadata as a Mechanical Integrity domain — a future governance update, not a blocker for this wave.

**Overall alignment: PASS.** The proposal faithfully implements [[AM — Git Conventions]] through the [[AM — Tool Conventions]] pattern. Every check traces to a specific section in Git Conventions. The two findings are about transparency and domain categorisation, not alignment failures.

### Integrity

**Question:** Is this internally sound?

**Finding IN-1: Check 4's `pre_wave_tag_pattern` has a regex escaping bug.** The pattern `^pre-wave-{wave_id}$` substitutes `{wave_id}` with the wave identifier (e.g., `8.2`). But the dot in `8.2` is a regex metacharacter that matches any character. The substituted pattern `^pre-wave-8.2$` would match both `pre-wave-8.2` and `pre-wave-8X2`. In practice this is unlikely to cause a false match (nobody creates tags like `pre-wave-8X2`), but it is technically incorrect. The implementation must escape the wave ID before substitution (e.g., Python's `re.escape(wave_id)`) to produce the correct pattern `^pre-wave-8\.2$`.

**Severity: Low.** Trivial implementation fix. Zero practical risk at current scale. But correctness matters in a tool that claims deterministic results (D1).

**Finding IN-2: Error isolation within the single tool is unspecified.** The proposal defines exit code 2 as "the tool itself failed" but doesn't specify what happens when one check fails while others could succeed. Scenario: Check 4 fails because the Roadmap file is unreadable. Do the remaining six checks still run and produce their findings, or does the entire tool exit 2 with a partial report?

This matters because the "single tool" decision (justified by Law 3) consolidates seven independent concerns. In Wave 8.2, a failure in `proposal_lifecycle.py` didn't affect `governance_compliance.py` — they were separate processes. Here, a failure in any check could suppress findings from all other checks.

**Severity: Medium.** The proposal should specify the error isolation strategy. Two options: (a) **Fail-fast** — any check error causes exit 2, partial report. Simple, conservative, but loses findings from healthy checks. (b) **Best-effort** — each check runs independently, errors are reported per-check in the report, the exit code is 2 only if no checks completed, 1 if any findings exist alongside errors. This preserves the value of the checks that succeeded while surfacing the error. Option (b) is recommended — it aligns with the Tool Conventions Safety Rule 5 ("Fail safe... It must not guess, skip, or continue with partial results *unless explicitly configured to do so*"). The proposal should specify best-effort as the default and note the design explicitly.

**Finding IN-3: Check 6 runs on "the current branch" while Check 3 runs on `master`.** If the tool is run while on `master`, both checks examine master commits. A commit directly on master with a bad message could appear as both a Check 3 warning (direct master commit) and a Check 6 finding (bad commit message). This isn't wrong — they're different concerns about the same commit (one about location, one about format). But the proposal should note that findings and warnings can reference the same commit from different checks, so the human reading the report isn't confused by apparent duplication.

**Severity: Low.** This is an expected property of independent checks (same rationale as Wave 8.2's deliberate overlap between `proposal_lifecycle.py` and `reflection_completeness.py`). A sentence in the report format specification or a design note would resolve it.

**Finding IN-4: Check 7 (uncommitted changes) will produce a warning on virtually every run during active development.** The tool is designed to be run during development — it's in the orchestrator alongside other health checks. During active work, uncommitted changes are the normal state, not an exception. A warning that fires every time becomes invisible. This doesn't make the check incorrect, but it affects the report's signal-to-noise ratio. If every report includes "Warning: 12 uncommitted files," the reader stops noticing warnings — including the Check 3 warnings about direct master commits, which are the more meaningful signal.

**Severity: Medium.** The check is conceptually sound (AM — Git Conventions §Safety Rules does say agents should commit frequently and not accumulate uncommitted state). But the operational reality is that the tool runs mid-session when uncommitted work is expected. Two mitigations: (a) Make Check 7 suppressible via a config flag (e.g., `check_uncommitted_changes: true/false`), so it can be disabled during active sessions and enabled for end-of-session or CI runs. (b) Separate the warning section into "transient warnings" (Check 7) and "persistent warnings" (Check 3), so the reader can distinguish always-firing from meaningful warnings. Either approach preserves the check's value while preventing warning fatigue.

**Overall integrity: CONDITIONAL PASS.** IN-2 requires resolution — the error isolation strategy must be specified. IN-4 is a meaningful operational concern that should be addressed before or during implementation. IN-1 and IN-3 are straightforward implementation notes.

### Viability

**Question:** Is every component earning its place?

**Finding VI-1: The scope degradation plan correctly prioritises but doesn't account for the Check 4 dependency cost.** Check 4 (pre-wave tag presence) is the only check that requires `vault_model.py` and Roadmap parsing. All other checks use pure git commands. The scope degradation plan places Check 4 in the "Standard" tier alongside Checks 3 and 5. But Check 4 carries disproportionate complexity relative to Checks 3 and 5 — it introduces the cross-domain dependency (AL-1) and the Roadmap parsing fragility (proven manageable in Wave 8.2, but still the only fragile component in this tool). Consider: if the minimum viable scope is expanded, Check 3 and Check 5 should be added before Check 4, not alongside it.

**Severity: Low.** The current ordering (1, 2, 5 → 1–5 → all) already separates the simplest checks from Check 4. The suggestion is to make the ordering within the "Standard" tier explicit: 1, 2, 5 first, then 3, then 4. This is a refinement, not a restructuring.

**Finding VI-2: D6 process note.** As stated above, this audit was performed by the drafting agent in the same session. The findings are presented in good faith with adversarial rigour, but the D6 separation is imperfect. The human's review at approval time provides the definitive gate.

**Overall viability: PASS.** All seven checks earn their place. The single-tool design is justified. The scope degradation plan is well-ordered. The config-driven approach ensures portability. The wave is appropriately scoped — smaller than Wave 8.2 (one tool vs five + library), with no new architectural patterns to establish.

### Summary of Findings

| ID | Finding | Severity | Resolution |
|----|---------|----------|------------|
| AL-1 | Check 4 creates cross-domain dependency (vault content → git check) | Low | Acknowledge in impact assessment; note that scope degradation eliminates it |
| AL-2 | Git metadata not explicitly in Integrity Layers domain description | Low | Accept — boundary test is authoritative; governance update is future work |
| IN-1 | Regex escaping bug in pre_wave_tag_pattern substitution | Low | Implementation must use `re.escape()` on wave ID before substitution |
| IN-2 | Error isolation within single tool is unspecified | Medium | **RESOLVED.** Best-effort strategy added to tool specification: each check runs independently, errors reported per-check, exit code 2 only if no checks complete |
| IN-3 | Same commit can appear in Check 3 and Check 6 output | Low | Add design note acknowledging expected overlap |
| IN-4 | Check 7 produces warnings on every run during active development | Medium | **RESOLVED.** Config flag `check_uncommitted_changes` added (default true, suppressible for active-session runs) |
| VI-1 | Scope degradation could be more granular within Standard tier | Low | Refine Standard tier ordering: 1, 2, 5 → 3 → 4 |
| VI-2 | D6 process — same-session audit | Noted | Human review is the definitive gate |

### Audit Verdict

**Conditional pass.** The proposal is well-structured, correctly scoped, and faithfully implements [[AM — Git Conventions]] through the [[AM — Tool Conventions]] pattern. The single-tool design is justified by the shared data source. The scope degradation plan is sound. The conservative approach to Checks 3, 6, and 7 correctly applies Convention 7.

Two findings required resolution before approval:

1. **IN-2 (Medium): RESOLVED.** Best-effort error isolation strategy added to the tool specification. Each check runs independently within the tool; errors are reported per-check in the report; the tool's exit code is 2 only if no checks completed successfully, otherwise 1 if any findings exist (even alongside errors in other checks).

2. **IN-4 (Medium): RESOLVED.** Config flag `check_uncommitted_changes` added (default true, suppressible for active-session runs). This prevents warning fatigue without removing the check's capability.

The remaining findings (AL-1, AL-2, IN-1, IN-3, VI-1) are improvements that can be addressed during implementation or left as-is without compromising the proposal's soundness.

**Post-resolution verdict: PASS.** The proposal is ready for human approval.

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal creates a new executable artifact in `04_EXECUTE/tools/vault-maintenance/` and extends the existing tool suite. It does not modify governance documents. The Git Conventions and Tool Conventions governance applies unchanged.
