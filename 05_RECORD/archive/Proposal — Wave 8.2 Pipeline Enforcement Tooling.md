---
title: "Proposal — Wave 8.2 Pipeline Enforcement Tooling"
type: proposal
status: archived
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
approved: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Artifact Lifecycles]]"
    - "[[AM — Tool Conventions]]"
    - "[[AM — Integrity Layers]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[AM — LLM Conventions]]"
    - "[[Proposal — Wave 6 Mechanical Integrity]]"
    - "[[Proposal — Wave 7 Scheduled Execution]]"
    - "[[Wave 8 — Capture Seed]]"
tags: [proposal, wave-8, pipeline-enforcement, tooling, mechanical-integrity]
---

# Proposal — Wave 8.2 Pipeline Enforcement Tooling

## Problem Statement

AM can detect structural problems in its vault (Wave 6) and run those checks autonomously on a schedule (Wave 7). But structure and process are different things. The existing seven tools check whether files are well-formed, links resolve, orphans exist, and names follow conventions. They answer: "Is the vault structurally sound?" They do not answer: "Is the AM pipeline being followed?"

This creates a specific, proven problem. During Wave 6, the reflection was skipped and nothing detected it. Proposals have appeared in `active/` without audit. Capture items can sit indefinitely without being triaged. These are process failures, not structural ones — every file involved was valid YAML with correct links. The structural tools passed. The pipeline was still broken.

Wave 8.1 produced the governance specification for this gap: [[AM — Artifact Lifecycles]] defines the lifecycle rules for seven artifact types, the gates between stages, and — critically — the mechanical checks that can enforce those gates. [[AM — LLM Conventions]] governs the semantic side. The governance is written. What's missing is the tooling that enforces the mechanical checks.

**Wave 8.2's question:** Can AM mechanically verify that its own process is being followed — not just that its files are well-formed?

## Proposed Change

**Wave 8.2: Pipeline Enforcement Tooling** — build the mechanical tools that verify lifecycle rules from [[AM — Artifact Lifecycles]] are followed. These tools extend the existing vault-maintenance suite with process-level checks.

The wave has two phases: a shared foundation (vault model library), then the enforcement tools themselves.

### Phase 1 — Vault Model Library

Build a shared Python library that parses all vault frontmatter and builds an in-memory model of the vault's artifacts and their relationships. This library is consumed by every pipeline enforcement tool.

**Deliverables:**

| Artifact | Location | What it does |
|----------|----------|-------------|
| `vault_model.py` | `04_EXECUTE/tools/vault-maintenance/lib/` | Parses all markdown files in the vault, extracts YAML frontmatter, builds an in-memory model of artifacts with their types, statuses, relationships, locations, and creation dates. Respects exclude_patterns and frontmatter_optional_folders from config. |

**Design decisions:**

- **Shared library, not duplicated code.** Every pipeline check needs the same data: frontmatter fields, file locations, relationship links, dates. Without a shared library, each tool would independently implement its own YAML parsing, config loading, date resolution, and relationship traversal — five copies of the same logic, maintained in five places. The library provides a single implementation that each tool imports. This satisfies Law 3 (Economy) — one implementation maintained in one place — while preserving Convention 4 (Independence) — each tool remains independently invocable because each tool imports the library itself. Note: because each tool runs as a separate process through the orchestrator, each invocation rebuilds the in-memory model from scratch. The library's Economy value is code reuse (DRY), not parse-count reduction. At ~60 files, the rebuild cost is negligible.
- **Python, not shell.** The Wave 6 tools are shell scripts, and that was the right choice for structural checks — file existence, grep patterns, basic validation. The pipeline enforcement checks are fundamentally different: they require YAML field-level access, date arithmetic, and cross-artifact relationship traversal. Shell can do these things, but at the cost of fragile string parsing and external tool dependencies (yq, jq, date gymnastics). Python has native YAML parsing (the `yaml_validator.py` precedent already exists in `lib/`), datetime handling, and data structures that make relationship traversal natural. The Tool Conventions prescribe the pattern (read-check-report), the behaviour (config-driven, conservative, stateless), and the interface (exit codes, report format) — not the language. Python satisfies all conventions.
- **In-memory model, not a database.** The vault is ~60 active files. An in-memory dictionary of frontmatter data is sufficient. SQLite or any persistence layer would violate Law 3 — it solves a problem that doesn't exist at this scale. If the vault grows to hundreds of files and cross-run comparison becomes necessary, the vault model can be serialized then. Not now.
- **Respects existing config.** The library reads the same `am.conf` and `defaults.conf` files that the shell tools use. It honours `exclude_patterns` (so archive, tool reports, runtime, and templates are not scanned), `frontmatter_optional_folders` (so capture items and session logs are not penalised for missing frontmatter), and `vault_root`. No new config format — the existing format is extended with pipeline-specific keys.
- **Captures and archive are handled correctly.** Capture items (`01_CAPTURE/`) are loaded into the model but flagged as frontmatter-optional — their presence is tracked for triage and routing checks, but missing frontmatter is never a finding. Archive (`05_RECORD/archive/`) is excluded from scans entirely via `exclude_patterns` — archived artifacts are not subject to active-document checks. This matches the Artifact Lifecycles specification: captures are "deliberately unstructured" and archive is a terminal state.

### Phase 2 — Pipeline Enforcement Tools

Build five Python tools, each covering one artifact-type family. Each tool follows the read-check-report pattern from [[AM — Tool Conventions]], produces a Markdown report, and returns structured exit codes (0 = clean, 1 = findings, 2 = error).

**Deliverables:**

| Artifact | Location | What it does |
|----------|----------|-------------|
| `capture_triage.py` | `04_EXECUTE/tools/vault-maintenance/` | Checks capture item lifecycle rules |
| `proposal_lifecycle.py` | `04_EXECUTE/tools/vault-maintenance/` | Checks proposal lifecycle rules |
| `reflection_completeness.py` | `04_EXECUTE/tools/vault-maintenance/` | Checks reflection and capture seed lifecycle rules |
| `concept_lifecycle.py` | `04_EXECUTE/tools/vault-maintenance/` | Checks concept lifecycle rules |
| `governance_compliance.py` | `04_EXECUTE/tools/vault-maintenance/` | Checks governance document structural rules |
| Updated `am.conf` | `04_EXECUTE/tools/vault-maintenance/config/` | Extended with pipeline-specific configuration |
| Updated `orchestrate.sh` | `04_EXECUTE/tools/vault-maintenance/` | Adds the five new tools to the orchestration sequence |

#### Tool 1: `capture_triage.py`

**Checks:**

1. **Triage deadline.** Capture items older than the configured triage deadline (default: 14 days) that are not referenced by any Future Waves Register entry, concept, reflection, or archive record. The tool checks file creation date (from `created` frontmatter if present, otherwise filesystem creation date) against the current date. If the item is referenced anywhere in the vault (by wiki-link to its title or filename), it is considered triaged.

2. **Routing provenance.** Capture items that appear to have been routed (referenced by another artifact) but whose destination artifact does not link back. This is a bidirectional link check scoped to capture items and their expected destinations.

**Exemptions:**

- Capture items without frontmatter are still checked for triage deadline using filesystem dates. Missing frontmatter is never a finding for capture items — this is inherited from `frontmatter_optional_folders` in config.
- `CLAUDE.md` files within `01_CAPTURE/` are excluded (structural files, not capture items).

**Config additions:**

```
# Pipeline enforcement — capture triage
capture_triage_deadline_days: 14
```

#### Tool 2: `proposal_lifecycle.py`

**Checks:**

3. **Status/location consistency.** No proposal exists in `active/` with `status: draft`. Conversely, no proposal exists in `proposals/` with `status: active`. Status must match location.

4. **Audit gate.** No proposal exists in `active/` without a non-empty `## Audit` section. The tool checks for the presence of a `## Audit` heading with content following it (not just the heading).

5. **Completion gate.** Every active proposal whose wave is marked complete in the [[AM — Roadmap]] (contains ✓) has a corresponding reflection in `06_REFLECT/`. The tool identifies the wave from the proposal filename or title, then checks for a reflection referencing that wave.

6. **Archive gate.** No proposal remains in `active/` after its wave is marked complete in the Roadmap. Completed waves' proposals should be in `05_RECORD/archive/`.

**Config additions:**

```
# Pipeline enforcement — proposal lifecycle
proposal_draft_folder: "03_DECIDE/proposals"
proposal_active_folder: "03_DECIDE/active"
roadmap_file: "02_KNOWLEDGE/governance/AM — Roadmap.md"
```

#### Tool 3: `reflection_completeness.py`

**Checks:**

7. **Reflection existence.** Every wave marked complete (✓) in the Roadmap has a corresponding reflection in `06_REFLECT/`. The tool parses the Roadmap for completed waves, then checks for a reflection file whose title or `derives_from` references that wave.

8. **Capture seed existence.** Every reflection in `06_REFLECT/` has a corresponding capture seed in `01_CAPTURE/`. The tool checks whether any file in `01_CAPTURE/` references the reflection (by wiki-link or relationship).

9. **Reflection provenance.** The reflection's `derives_from` includes the wave's proposal. The tool checks the reflection's frontmatter relationships against the corresponding proposal.

10. **Capture seed provenance.** The capture seed references the reflection. The tool checks whether the seed's content or frontmatter references the reflection it came from.

**Design note:** Checks 7 and 5 (from `proposal_lifecycle.py`) overlap — both verify that completed waves have reflections. This is intentional. Convention 4 (Independence) means each tool must produce a complete result on its own. The orchestrator's aggregate report will show the same finding from both tools, which is correct — it's the same underlying problem detected from two angles. This is preferable to making one tool depend on the other's output.

#### Tool 4: `concept_lifecycle.py`

**Checks:**

11. **Draft stagnation.** No concept in `status: draft` for more than the configured review deadline (default: 30 days). The tool checks the `created` date in frontmatter against the current date.

12. **Authority chain.** Every active concept has a non-empty `derives_from` relationship. The tool checks that the `derives_from` field exists and contains at least one entry.

13. **Reflection reference.** Every active concept in `02_KNOWLEDGE/concepts/` is referenced by at least one reflection in `06_REFLECT/`. The tool scans all reflections for wiki-links or mentions matching each concept's title. This is a reference-existence check, not a temporal mapping — it verifies that the concept has been acknowledged in a reflection, without attempting to determine *which* wave produced it. (The stronger temporal check — "referenced in the wave's reflection that created it" — requires date-range data that the Roadmap does not currently provide. See audit finding IN-2. The simplified check is conservative and mechanically clean; the temporal variant can be revisited if wave date ranges are added to the Roadmap or proposals.)

**Config additions:**

```
# Pipeline enforcement — concept lifecycle
concept_review_deadline_days: 30
```

**Exemptions:**

- Concepts in `05_RECORD/archive/` are excluded (already handled by `exclude_patterns`).

#### Tool 5: `governance_compliance.py`

**Checks:**

14. **Authority floor.** All documents in `02_KNOWLEDGE/governance/` with type `governance` have `authority_weight` ≥ 70.

15. **Location enforcement.** All documents anywhere in the vault with `type: governance` are located in `02_KNOWLEDGE/governance/` (or a subfolder thereof, e.g., `governance/roles/`).

16. **Schema compliance.** All governance documents have complete schema v3 frontmatter — all required fields present, `schema_version: 3`, valid controlled vocabulary values.

17. **Type/folder consistency.** The `type` field in frontmatter matches the expected type for the folder the artifact lives in. Governance folder → `type: governance`; concepts folder → `type: concept`; proposals → `type: proposal`. This check extends beyond governance documents to catch misplaced artifacts vault-wide.

**Config additions:**

```
# Pipeline enforcement — governance compliance
governance_folder: "02_KNOWLEDGE/governance"
governance_min_authority_weight: 70

# Type/folder mapping for consistency check
type_folder_map:
  governance: "02_KNOWLEDGE/governance"
  concept: "02_KNOWLEDGE/concepts"
  skill: "02_KNOWLEDGE/skills"
  role: "02_KNOWLEDGE/governance/roles"
  proposal: "03_DECIDE"
  log: "05_RECORD/logs"
  report: "05_RECORD/reports"
```

**Exemptions:**

- `CLAUDE.md` and `README.md` files are excluded from all governance compliance checks (infrastructure files, not vault notes — as stated in the Charter).
- Archive is excluded via `exclude_patterns`.
- Files in `frontmatter_optional_folders` are excluded from schema compliance checks.

### Modifications to Existing Tools

Two exemption rules from [[AM — Artifact Lifecycles]] require changes to the existing Wave 6 tools, not new tools:

**18. Session logs exempt from orphan detection.** The config already exempts `05_RECORD/logs` via `orphan_exempt_folders`. No code change needed — configuration already handles this.

**19. Reports exempt from orphan detection.** The config already exempts `05_RECORD/reports` via `orphan_exempt_folders`. No code change needed.

Both exemptions are already implemented. No Wave 6 tool modifications are needed.

### Orchestrator Integration

The existing `orchestrate.sh` is extended to include the five new Python tools. They run after the existing seven shell tools, in order:

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
)
```

The orchestrator already handles arbitrary executables — it calls the tool, captures the exit code, and collects the report path. Python scripts work identically to shell scripts from the orchestrator's perspective, provided they are executable and follow the same interface (exit codes 0/1/2, `Report: <path>` on stdout).

**Ordering rationale:** Structural tools run first because pipeline tools assume structurally valid input. If YAML doesn't parse, the vault model can't be built. If links are broken, relationship checks are meaningless. The structural layer is the foundation; the pipeline layer is built on top of it. This mirrors [[AM — Integrity Layers]]: mechanical checks proceed from low-level (syntax) to high-level (process).

## Scope Degradation Plan

If time pressure or unexpected complexity builds:

**Minimum viable Wave 8.2** (Phase 1 + Tools 2 and 3 only):
- Vault model library, `proposal_lifecycle.py`, `reflection_completeness.py`
- These two tools cover the highest-value checks: the ones that have already failed in practice (skipped reflection, unapproved proposals in `active/`). They answer the wave's question with the smallest possible scope.

**Standard Wave 8.2** (Phase 1 + Tools 1–4):
- Adds capture triage and concept lifecycle. These cover all four process-active artifact types.

**Full Wave 8.2** (all deliverables):
- Adds governance compliance and type/folder consistency. These are structural-process hybrids — useful but lower urgency since governance documents change infrequently.

## What Is NOT in Scope

| Item | Why deferred | Revisit when |
|------|-------------|--------------|
| Finishing ritual automation | Finishing rituals require sequential multi-step actions (archive proposal, update roadmap, create seed). This is orchestration of *actions*, not detection of *state*. It crosses the report-don't-repair boundary. | Wave 8.3 or a future automation wave considers action-taking tools with their own governance |
| Standalone Roadmap format validation | A dedicated tool that verifies the Roadmap's own formatting and completeness is mechanically checkable but fragile — depends on Roadmap formatting staying consistent, and a formatting change produces false positives, violating Convention 7 (Conservative). Note: this is distinct from *consuming* Roadmap data as input to other checks (Checks 5, 6, 7), which use a conservative parser that skips unparseable entries and reports warnings rather than false findings. The distinction: "is the Roadmap well-formed?" (deferred) vs. "what does the Roadmap say about wave completion?" (consumed as input, with graceful degradation). See audit finding AL-2. | Roadmap format is stabilised and codified in config |
| SYSTEM_MAP staleness detection | Requires determining "what counts as updated" — a timestamp comparison is brittle and a content comparison is semantic. | Self-observation wave introduces content-aware change detection |
| Semantic assessments | All semantic gates (alignment, integrity, viability audits) are [[AM — LLM Conventions]] territory, not mechanical tooling. Wave 8.1 governs them. | Already governed — LLMs follow [[AM — LLM Conventions]] and [[AM — Artifact Lifecycles]] |
| Git-ops enforcement | Branch naming, commit format, tag management. Needs its own design conversation. | Wave 8.3 |
| Auto-remediation | Tools that fix what they find (create missing reflections, archive stale proposals). Violates Convention 3 (Report, Don't Repair). | If ever — under separate governance with explicit human authorization model |

## Traceability

| Decision | Foundation |
|----------|-----------|
| Build tools that detect process violations, not structural ones | [[AM — Artifact Lifecycles]] — the mechanical checks listed per artifact type are the spec |
| Shared vault model library | Law 3 (Economy) — single implementation of YAML parsing, date resolution, config loading, and relationship traversal maintained in one place (code reuse), rather than duplicated across five tools. Each tool rebuilds the model independently (separate processes), so this is maintenance economy, not parse-count reduction. See audit finding IN-1. |
| Python for pipeline tools | Law 3 (Economy) — natural fit for YAML parsing, date math, relationship traversal; D1 (Deterministic Control Surfaces) — Python produces same result every time |
| Five independent tools, one per artifact family | Convention 4 (Independent and Composable) — each tool is self-contained; Convention 1 (Read-Check-Report) — each follows the same pattern |
| Tools report, they don't repair | Convention 3 (Report, Don't Repair) — detection and remediation are different responsibilities (D6) |
| Conservative: flag only provable violations | Convention 7 (Conservative) — false positives erode trust |
| Config-driven deadlines and folder mappings | Convention 2 (Config-Driven) — no hardcoded vault-specific assumptions |
| Pipeline tools run after structural tools | [[AM — Integrity Layers]] — mechanical checks proceed from low-level (syntax) to high-level (process) |
| Capture items exempt from frontmatter requirements | [[AM — Artifact Lifecycles]] — "captures are deliberately unstructured" |
| Archive excluded from all pipeline checks | Existing `exclude_patterns` convention — archive is a terminal state |
| Deliberate overlap between tools (reflection check in both proposal and reflection tools) | Convention 4 (Independence) — each tool produces a complete result on its own |

## Impact Assessment

**What this affects:**
- `04_EXECUTE/tools/vault-maintenance/lib/` — receives `vault_model.py`
- `04_EXECUTE/tools/vault-maintenance/` — receives five new Python tools
- `04_EXECUTE/tools/vault-maintenance/config/am.conf` — extended with pipeline-specific configuration
- `04_EXECUTE/tools/vault-maintenance/orchestrate.sh` — extended with five new entries in the TOOLS array
- `04_EXECUTE/tools/vault-maintenance/reports/` — receives five new report files per run
- `05_RECORD/reports/` — daily health reports now include pipeline enforcement findings

**What this does NOT affect:**
- Governance documents — no changes
- Existing Wave 6 tools — unchanged; the exemptions they need are already in config
- Wave 7 runtime (launchd, summarise_report.py, notify.sh) — unchanged; the wrapper script calls `orchestrate.sh`, which automatically picks up the new tools
- Vault structure — no new folders

**What could go wrong:**

- **YAML parsing edge cases.** Some vault files may have frontmatter that Python's YAML parser handles differently than the existing `yaml_validator.py`. Mitigation: the vault model library reuses the same YAML parsing approach as the existing validator. Tests against the actual vault during development.
- **Date resolution ambiguity.** Capture items without frontmatter rely on filesystem dates, which may differ from logical creation dates (e.g., a file copied from another location). Mitigation: Convention 7 (Conservative) — when the date is ambiguous, the tool uses the most recent date available, which biases toward "not yet stale" rather than false positives.
- **Roadmap parsing fragility.** Two tools (`proposal_lifecycle.py` and `reflection_completeness.py`) parse the Roadmap to identify completed waves. If the Roadmap's format changes, these tools may break. Mitigation: the Roadmap parsing logic is in the shared vault model library, not duplicated across tools. A format change requires one fix. The parser is conservative — if it can't parse a wave entry, it skips it and reports a warning rather than a false finding.
- **Performance.** Parsing every markdown file's frontmatter adds time to the health check. Mitigation: the vault is ~60 files. YAML parsing is fast. Even if the vault grows to 200 files, the total parse time would be under a second. This is not a concern at current scale.
- **Report volume.** Five new tools produce five new reports per run. The daily health report grows. Mitigation: the orchestrator's aggregate report already handles this — it collects findings from all tools into one combined view. Individual reports exist for debugging. The aggregate report is what humans and the LLM summary read.

## Alternatives Considered

**Alternative 1: Shell scripts for pipeline checks**
Rejected. Shell can parse YAML via external tools (yq, python -c), but the result is fragile string processing for what are fundamentally data-structure operations. Cross-artifact relationship traversal in shell requires nested loops with grep — possible but unmaintainable. The existing `yaml_validator.py` in `lib/` already established the precedent: when the check requires data structure access, use Python.

**Alternative 2: One monolithic Python tool for all pipeline checks**
Rejected. Violates Convention 4 (Independent and Composable). A single `pipeline_check.py` with sub-commands could share the vault model efficiently, but it cannot be run selectively by the orchestrator, cannot produce independent reports, and cannot return independent exit codes. The orchestrator's design assumes one tool = one concern = one exit code. Five independent tools that share a library preserve both independence and efficiency.

**Alternative 3: Enhance existing shell tools instead of building new ones**
Partially viable. The governance compliance checks (authority floor, schema compliance) could extend `yaml_validation.sh`. But mixing structural validation with process enforcement in the same tool muddies the concern boundary. Wave 6 tools check "is this file well-formed?" Wave 8.2 tools check "is this process being followed?" These are different questions with different failure modes. Keeping them separate means a structural finding is clearly a structural problem, and a process finding is clearly a process problem. The distinction serves the human reading the report.

**Alternative 4: Skip the vault model library, let each tool implement parsing independently**
Rejected. Five tools each implementing their own YAML parsing, config loading, date resolution, and relationship traversal means five copies of the same logic to maintain, debug, and evolve. Law 3 (Economy) — the shared library provides a single implementation maintained in one place. (Note: each tool still rebuilds the model per invocation since tools run as separate processes. The Economy benefit is code reuse, not parse-count reduction — but code reuse is the more valuable property for long-term maintenance.)

**Alternative 5: Database-backed vault model (SQLite)**
Rejected for current scale. The vault model is an in-memory dictionary rebuilt on each run. At ~60 files, this takes milliseconds. SQLite would add schema management, migration, and persistence concerns for no measurable benefit. Deferred to the [[AM — Future Waves Register]] — revisit when cross-run comparison or vault growth justifies it.

## Gate Criteria

**This proposal is ready to execute when:**

- [x] Proposal drafted with all required elements
- [x] Adversarial audit completed (alignment, integrity, viability)
- [x] Human (Rob) approves the proposal (2026-03-17)
- [x] Audit findings resolved (IN-2, AL-2, IN-1 — see Audit section)

**Wave 8.2 is complete when:**

- [ ] `vault_model.py` library parses all vault frontmatter, builds in-memory model, respects config exclusions and exemptions
- [ ] `capture_triage.py` detects untriaged captures past deadline and broken routing provenance
- [ ] `proposal_lifecycle.py` detects status/location mismatches, missing audits, missing reflections for complete waves, and unarchived complete proposals
- [ ] `reflection_completeness.py` detects missing reflections, missing capture seeds, broken provenance chains in both directions
- [ ] `concept_lifecycle.py` detects stale drafts, missing authority chains, unreferenced concepts
- [ ] `governance_compliance.py` detects authority floor violations, location violations, schema gaps, and type/folder mismatches
- [ ] All five tools follow Tool Conventions: config-driven, read-only, exit codes 0/1/2, Markdown reports, conservative (no false positives)
- [ ] All five tools are integrated into `orchestrate.sh` and produce reports that appear in the aggregate health report
- [ ] `am.conf` extended with pipeline-specific configuration
- [ ] Tools tested against the actual vault — all findings are real findings, no false positives
- [ ] README.md in `04_EXECUTE/tools/vault-maintenance/` updated to document the new tools
- [ ] SYSTEM_MAP.md updated to reflect new tool suite contents
- [ ] Wave 8.2 reflection written and filed in `06_REFLECT/`
- [ ] Capture seed for Wave 8.3 created in `01_CAPTURE/`

## Audit

**Auditor context:** This audit is performed by the same agent that drafted the proposal, in the same session. This violates the spirit of D6 (Separation of Powers). The adversarial lens is applied with extra rigour to compensate, but the finding should be noted: a second-session review by a fresh agent would provide stronger separation. The human's review at approval time is the definitive gate.

### Alignment

**Question:** Does this proposal serve what's above it?

**Finding AL-1: Check 17 is not specified in Artifact Lifecycles.** The proposal claims to implement "the mechanical checks specified in [[AM — Artifact Lifecycles]]." Checks 1–16 trace directly to specific mechanical checks listed in that document. Check 17 (type/folder consistency) does not — it was identified during the pre-proposal conversation as "implied but not explicitly listed." The [[AM — Future Waves Register]] entry for Wave 8.2 explicitly notes the list is "not exhaustive," so the addition is legitimate. But the proposal should be transparent about which checks come from the spec and which are additions. **Severity: Low.** The check is sound and config-driven. The issue is provenance transparency, not alignment.

**Finding AL-2: Three checks depend on Roadmap parsing, but Roadmap verification is explicitly deferred as fragile.** Checks 5, 6, and 7 parse the [[AM — Roadmap]] for ✓ markers to identify completed waves. The "What Is NOT in Scope" table defers "Roadmap ✓ verification" because it's "fragile — depends on Roadmap formatting staying consistent. A formatting change produces false positives, violating Convention 7." This is an internal contradiction: the proposal defers Roadmap verification as a standalone check because of fragility, then depends on Roadmap parsing as input to three other checks. The "What could go wrong" section acknowledges the fragility and proposes a mitigation (conservative parser, warnings on unparseable entries, shared logic in vault model). The mitigation is reasonable, but the contradiction should be resolved explicitly. **Severity: Medium.** The three checks that depend on Roadmap parsing are among the highest-value checks in the suite (completion gate, archive gate, reflection existence). If the Roadmap parser fails, these checks silently degrade. The proposal needs to decide: either Roadmap parsing is reliable enough to depend on (in which case the "Not in Scope" entry is misleading), or it's too fragile (in which case Checks 5, 6, and 7 need an alternative source of truth for wave completion status).

**Recommendation for AL-2:** Reframe the "Not in Scope" entry. The deferred item is not "Roadmap ✓ verification" generally — it's "standalone Roadmap format validation as its own tool." The three checks that consume Roadmap data are not verifying the Roadmap's correctness; they are using it as input. The distinction is: "is the Roadmap well-formed?" (deferred) vs. "what does the Roadmap say about wave completion?" (used as input, with conservative fallback). This resolves the contradiction without changing any checks.

**Overall alignment: PASS.** The proposal faithfully implements the Artifact Lifecycles specification. The additions (Check 17) and dependencies (Roadmap parsing) are justifiable but need clearer provenance and framing.

### Integrity

**Question:** Is this internally sound?

**Finding IN-1: "Parse once, check many times" is factually incorrect.** The traceability table claims the vault model library satisfies "Law 3 (Economy) — parse once, check many times." This is misleading. Each tool is an independent process invoked by the orchestrator. Each process imports `vault_model.py` and builds the model from scratch — parsing every YAML file in the vault. With five tools and ~60 files, the actual parse count is ~300, not 60. The library does not persist its model between invocations because each tool runs as a separate process.

The library's actual Economy value is code reuse: one implementation of YAML parsing, date resolution, config loading, and relationship traversal, maintained in one place. That's a genuine Law 3 benefit — but it's DRY (Don't Repeat Yourself), not parse reduction. The traceability claim should be corrected. **Severity: Medium.** The architecture is sound; the justification is wrong. Correcting the traceability entry is a one-line fix. Alternatively, if parse reduction matters, the proposal could specify a model-caching mechanism (serialize the model to a temp file on first build; subsequent tools load the cached model instead of re-parsing). But at ~60 files, the performance difference is negligible — this would be premature optimisation.

**Finding IN-2: Check 13 (concept reflection reference) is underspecified and may be unimplementable.** The check says it "maps [concepts] to the wave that was active at that time (by checking the Roadmap's wave timeline)." The Roadmap has ✓ markers for completed waves but no explicit date ranges. There is no mechanical way to determine "which wave was active on 2026-03-17" from the current Roadmap format. Implementing this check requires either: (a) adding date ranges to the Roadmap (a governance change, out of scope for Wave 8.2), (b) inferring wave dates from reflection or proposal creation dates (fragile, depends on artifacts existing), or (c) a heuristic mapping that could produce incorrect associations, violating Convention 7 (Conservative). **Severity: High.** As specified, this check cannot be built without either changing governance or accepting fragility. It should be redesigned or deferred.

**Recommendation for IN-2:** Simplify the check. Instead of "every concept created during a wave is referenced in that wave's reflection," check: "every active concept in `02_KNOWLEDGE/concepts/` is referenced by at least one reflection in `06_REFLECT/`." This is mechanically clean — it's a reference check, not a temporal mapping. It's weaker (it doesn't verify the *correct* reflection references the concept), but it's provably correct and conservative. The stronger temporal check can be revisited if wave date ranges are ever added to the Roadmap or proposals.

**Finding IN-3: Check 2 (routing provenance) risks false positives.** The check looks for capture items "that appear to have been routed (referenced by another artifact) but whose destination artifact does not link back." In practice, captures are often absorbed informally — someone reads a capture, incorporates the idea into a conversation or proposal, and the capture is effectively triaged without formal bidirectional wiki-linking. The Artifact Lifecycles document says routing evidence can be "A wiki-link or relationship entry traces back to the capture item, or (for archive routing) the capture's archived status in `05_RECORD/archive/`." But many current captures were triaged through conversation, not through formal wiki-links. This check would retroactively flag captures that were legitimately processed, violating Convention 7 (Conservative — no false positives). **Severity: Medium.** The check is conceptually sound but practically dangerous at current scale, where most routing is informal.

**Recommendation for IN-3:** Make Check 2 a warning, not a finding. Report it in the "Warnings" section of the tool's report, clearly distinguished from confirmed findings. This preserves the signal (bidirectional provenance is the goal) without producing false positives on historically informal routing. Alternatively, only apply Check 2 to captures created after the Artifact Lifecycles document was approved (2026-03-17), since that's when the bidirectional linking expectation was formalised.

**Overall integrity: CONDITIONAL PASS.** IN-1 is a documentation fix. IN-3 is a severity adjustment. IN-2 requires redesign — the check as specified cannot be built conservatively.

### Viability

**Question:** Is every component earning its place?

**Finding VI-1: governance_compliance.py partially overlaps with yaml_validation.sh.** Check 16 (schema compliance for governance documents) verifies "all required fields present, `schema_version: 3`, valid controlled vocabulary values." This is exactly what `yaml_validation.sh` already does for all vault documents, including governance documents. The unique value of `governance_compliance.py` is Check 14 (authority floor ≥ 70), Check 15 (location enforcement), and Check 17 (type/folder consistency, which extends vault-wide). Check 16 is redundant with the existing tool. **Severity: Low.** The scope degradation plan already places this tool last. Removing Check 16 from governance_compliance.py would sharpen the tool's purpose: it checks governance-specific and location-specific rules that yaml_validation.sh cannot, rather than repeating what yaml_validation.sh already covers. The remaining three checks are unique and earn their place.

**Finding VI-2: Check 13 will almost never fire.** There are currently ~6 concepts in the vault. They change perhaps once every 3–4 waves. The development cost of the temporal mapping logic (which IN-2 already identified as problematic) is fixed; its runtime value approaches zero at current scale. If simplified per the IN-2 recommendation (check that concepts are referenced by any reflection), the implementation cost drops and the check becomes viable — but it will still fire rarely. **Severity: Low.** The check is conceptually correct (the Artifact Lifecycles spec requires it). Its low firing rate is a property of the vault's current maturity, not a flaw in the check. It costs little to include.

**Finding VI-3: D6 process note.** As stated above, this audit was performed by the drafting agent in the same session. The findings are presented in good faith with adversarial rigour, but the D6 separation is imperfect. The human's review at approval time provides the definitive gate.

**Overall viability: PASS.** All five tools earn their place. The scope degradation plan correctly prioritises the highest-value tools first. VI-1 is a sharpening suggestion, not a viability concern.

### Summary of Findings

| ID | Finding | Severity | Resolution |
|----|---------|----------|------------|
| AL-1 | Check 17 not in Artifact Lifecycles spec | Low | Note provenance transparently in the check description |
| AL-2 | Roadmap parsing contradicts "Not in Scope" framing | Medium | Reframe the deferred item to distinguish Roadmap validation from Roadmap consumption |
| IN-1 | "Parse once" claim is factually incorrect | Medium | Correct traceability to "code reuse" not "parse reduction" |
| IN-2 | Check 13 is underspecified and unimplementable as written | High | Simplify to reference-existence check (any reflection, not temporal mapping) |
| IN-3 | Check 2 risks false positives on informally triaged captures | Medium | Demote to warning, or apply only to captures created after 2026-03-17 |
| VI-1 | Check 16 redundant with yaml_validation.sh | Low | Remove Check 16 from governance_compliance.py |
| VI-2 | Check 13 fires rarely at current scale | Low | Accept — cost is low if simplified per IN-2 |
| VI-3 | D6 process — same-session audit | Noted | Human review is the definitive gate |

### Audit Verdict

**Conditional pass.** The proposal is well-structured, correctly scoped, and faithfully implements the Artifact Lifecycles specification. The architecture is sound. The scope degradation plan is well-ordered.

Three findings required resolution before approval:

1. **IN-2 (High): RESOLVED.** Check 13 redesigned. The temporal mapping ("concept referenced in the wave's reflection that created it") replaced with a reference-existence check ("every active concept is referenced by at least one reflection"). Conservative, mechanically clean, buildable. The stronger temporal variant is noted as a future enhancement if wave date ranges are added.
2. **AL-2 (Medium): RESOLVED.** The "Not in Scope" entry reframed from "Roadmap ✓ verification" to "Standalone Roadmap format validation." The entry now explicitly distinguishes between validating the Roadmap's own format (deferred) and consuming Roadmap data as input to other checks (used, with conservative fallback). The contradiction is resolved.
3. **IN-1 (Medium): RESOLVED.** The traceability entry, the Phase 1 design decision, and Alternative 4 all corrected from "parse once, check many times" to "code reuse — single implementation maintained in one place." The text now accurately states that each tool rebuilds the model per invocation (separate processes) and that the Economy benefit is maintenance, not parse-count reduction.

The remaining findings (AL-1, IN-3, VI-1, VI-2) are improvements that can be addressed during implementation or left as-is without compromising the proposal's soundness.

**Post-resolution verdict: PASS.** The proposal is ready for human approval.

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal creates new executable artifacts in `04_EXECUTE/tools/vault-maintenance/` and extends the existing tool suite. It does not modify governance documents. The Artifact Lifecycles and Tool Conventions governance established during Waves 6 and 8.1 apply unchanged.
