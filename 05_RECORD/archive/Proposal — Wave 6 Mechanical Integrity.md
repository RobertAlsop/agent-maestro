---
title: "Proposal — Wave 6 Mechanical Integrity"
type: proposal
status: archived
authority_weight: 30
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
approved: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Wave 5.2 — Final Reflection]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Agent Maestro — Vault Rules]]"
    - "[[Wave 6 — Capture Seed]]"
tags: [proposal, wave-6, mechanical-integrity, tools, scripts]
---

# Proposal — Wave 6 Mechanical Integrity

## Problem Statement

AM cannot detect its own structural problems. Every integrity check currently requires a human and an LLM to read through the vault manually. This creates three specific problems:

1. **Broken links accumulate silently.** Wiki-links that point to renamed, moved, or deleted notes produce no error until someone happens to click one. The vault's navigational integrity degrades invisibly.
2. **YAML frontmatter drift is undetectable.** A note with a misspelled `type` value, a missing `derives_from`, or a malformed date passes no gate — because no gate exists. Schema v3 defines rules that nothing enforces.
3. **Orphaned and stub files persist.** Law 3 (Economy) says every component must earn its place. Without automated detection, dead-weight files survive indefinitely — they're invisible unless someone audits every file manually.
4. **No baseline inventory exists.** SYSTEM_MAP is manually maintained. If it falls out of date, there is no way to regenerate it mechanically. We don't know what we have unless we count by hand.

The [[AM — Roadmap]] identifies this as the next committed wave: "Can AM detect its own structural problems?" The [[AM — Integrity Layers]] document establishes that these are Mechanical Integrity problems — deterministic, structural, and enforceable by tools. The [[AM — Tool Conventions]] document defines how those tools must be built.

The foundation is laid. The tools don't exist yet.

## Proposed Change

**Wave 6: Mechanical Integrity** — build the first tool suite in `04_EXECUTE/tools/vault-maintenance/` that validates vault structural health against the rules defined in [[Agent Maestro — Vault Rules]].

The wave has two phases.

### Phase 1 — Individual Tools and Config Model

Build seven detection tools and the configuration model that makes them portable across vaults.

**Tools:**

| Tool | What it checks | Vault Rules enforced |
|------|---------------|---------------------|
| `yaml_validation.sh` | YAML frontmatter parses, required fields present, controlled vocabulary values valid, dates well-formed. Skips files in folders where frontmatter is optional (configured per vault). | Rules 5, 9–14 |
| `broken_links.sh` | All `[[wiki-links]]` in body text resolve to existing files. All `derives_from`, `governs`, and `related` entries in frontmatter resolve to existing files. Additionally flags concept and governance notes that contain zero body wiki-links. | Rules 15–19 |
| `orphan_detection.sh` | Every file is reachable via at least one inbound `derives_from`, `governs`, or `related` link from another file. Files with a known structural role (CLAUDE.md, SYSTEM_MAP.md, README.md) are exempt. | Rule 20 |
| `stub_detection.sh` | No empty files, no placeholder-only content, no `status: stub` notes in folders where content is required | Rule 7 |
| `naming_validation.sh` | No duplicate filenames across the vault. No duplicate `title` values in frontmatter. The `title` field in frontmatter matches the filename (minus `.md` extension) for every note. | Rule 34, implied uniqueness |
| `inventory.sh` | Generate a machine-readable manifest: every file, its folder, type, status, authority_weight, inbound link count, outbound link count. This is a reporting tool — it produces a snapshot, not a replacement for SYSTEM_MAP. SYSTEM_MAP remains human-curated; the inventory report supports cross-checking it for staleness. | Rules 21–23 (SYSTEM_MAP support) |
| `structure_check.sh` | Required folders exist. Required root files exist (`CLAUDE.md`, `SYSTEM_MAP.md`). Pipeline folder `CLAUDE.md` files present and non-empty. | Rules 1–4, 57 |

**Vault Rules intentionally out of scope for Wave 6:**

| Rule | Why out of scope |
|------|-----------------|
| Rule 6 (Purpose section required) | Detecting a `## Purpose` heading is mechanical, but verifying the section contains meaningful content is semantic. Deferred to Semantic Integrity. |
| Rule 18 (body wiki-links in concepts/governance) | Partially covered: `broken_links.sh` flags concept/governance notes with zero body wiki-links. Full compliance (links are contextually appropriate) is semantic. |
| Rule 42 (`updated` field changes on modification) | Requires git history analysis to compare file modification dates against frontmatter dates. Feasible but complex; deferred to a future wave. |
| Rule 58 (significant subfolders SHOULD have CLAUDE.md) | Uses "SHOULD" — requires judgment about which subfolders are "significant." Semantic. |
| Rules 24–26 (authority and governance cascade) | Require semantic judgment about whether authority weights are "earned" and whether documents "conflict." |
| Rules 27–30 (pipeline integrity — content flow) | Require semantic judgment about whether content is in the right pipeline stage. |
| Rules 36–38, 44–56 (work units, proposals, ideas, captures) | Lifecycle and process rules — enforced by the workflow, not by a filesystem scanner. |
| Rules 60–72 (templates, concepts, scope, governance cascade, git) | Mix of semantic judgment (concept viability, governance alignment) and repo-level concerns (git workflow). Outside vault-maintenance scope. |

**Config model:**

Configuration uses YAML format. Two files in `config/`:

- `defaults.conf` — generic Obsidian vault defaults (conservative baseline)
- `am.conf` — Agent Maestro-specific configuration (overrides defaults)

Invocation arguments (e.g., `--output-dir`, `--quiet`, `--strict`) override both files for specific runs.

**Example `am.conf`:**

```yaml
# AM vault configuration for vault-maintenance tools
vault_root: "/path/to/agent-maestro"
output_dir: "reports"

# Structure expectations (structure_check.sh)
required_folders:
  - "01_CAPTURE"
  - "02_KNOWLEDGE"
  - "03_DECIDE"
  - "04_EXECUTE"
  - "05_RECORD"
  - "06_REFLECT"

required_root_files:
  - "CLAUDE.md"
  - "SYSTEM_MAP.md"

required_claude_md:
  - "01_CAPTURE/CLAUDE.md"
  - "02_KNOWLEDGE/CLAUDE.md"
  - "03_DECIDE/CLAUDE.md"
  - "04_EXECUTE/CLAUDE.md"
  - "05_RECORD/CLAUDE.md"
  - "06_REFLECT/CLAUDE.md"

# YAML validation (yaml_validation.sh)
frontmatter_optional_folders:
  - "01_CAPTURE"

required_fields:
  - "title"
  - "type"
  - "status"
  - "authority_weight"
  - "schema_version"
  - "created"
  - "updated"
  - "relationships"
  - "tags"

controlled_vocabulary:
  type:
    - "governance"
    - "concept"
    - "skill"
    - "role"
    - "pipeline"
    - "log"
    - "report"
    - "proposal"
  status:
    - "draft"
    - "active"
    - "archived"

authority_weight_range:
  min: 0
  max: 100

# Orphan detection (orphan_detection.sh)
structural_exemptions:
  - "CLAUDE.md"
  - "SYSTEM_MAP.md"
  - "README.md"

# Link validation (broken_links.sh)
wiki_link_required_types:
  - "governance"
  - "concept"

# Files and folders to exclude from all scans
exclude_patterns:
  - ".git"
  - "04_EXECUTE/tools/vault-maintenance/reports"
  - "04_EXECUTE/tools/vault-maintenance/logs"
```

The full config schema will be documented in the suite's `README.md`. Each field corresponds to a specific tool's needs. Tools ignore fields they don't use.

**Exit codes per [[AM — Tool Conventions]]:**

| Code | Meaning |
|------|---------|
| `0` | Clean — no issues |
| `1` | Findings — issues detected, report written |
| `2` | Error — tool failed (bad config, missing vault path, etc.) |

**Report format:** Each tool writes a Markdown report to the configured output directory. Every report follows this structure:

```markdown
# [Tool Name] Report

**Vault:** /path/to/vault
**Date:** 2026-03-16T14:30:00
**Result:** CLEAN | FINDINGS | ERROR

## Summary

| Checked | Passed | Failed | Warnings |
|---------|--------|--------|----------|
| N       | N      | N      | N        |

## Findings

- [file path]: [description of issue]
- ...

## Warnings (uncertain)

- [file path]: [description of ambiguous finding]
- ...
```

Findings are confirmed issues. Warnings are ambiguous cases reported separately per Tool Convention 7 (conservative — don't report ambiguity as failure).

### Phase 2 — Orchestrator and First Health Report

Build the orchestrator and run the full suite against the AM vault.

**Orchestrator** (`orchestrate.sh`):
- Reads config to determine which tools to run
- Executes each tool in sequence
- Collects exit codes and report paths
- Produces an aggregate `vault_health_report.md` with: overall status, per-tool summary (tool name, exit code, finding count), combined findings, timestamp
- Returns exit code: `0` if all tools return `0`; `1` if any tool returns `1`; `2` if any tool returns `2`

**First health report:**
- Run the full suite against the AM vault using `am.conf`
- The report becomes the first artifact in `05_RECORD/reports/` — the pipeline's Record stage
- Findings are reviewed by Rob and categorised as: **critical** (blocks future work), **important** (should be fixed), or **acceptable** (known context, no action needed). This categorisation becomes input for remediation work in a subsequent session or wave. Remediation is out of scope for Wave 6.

**Secondary deliverables:**
- `README.md` in `vault-maintenance/` — what the suite does, how to configure it, how to run it, config schema reference, invocation examples, output format
- Updated `SYSTEM_MAP.md` reflecting the new contents of `04_EXECUTE/`

## Scope Degradation Plan

If time pressure or unexpected complexity builds, the wave has a graceful degradation path. This honors Law 3 (Economy) applied to the wave itself.

**Minimum viable Wave 6** (four core tools + config):
- `yaml_validation.sh` — enforces the schema
- `broken_links.sh` — enforces navigational integrity
- `orphan_detection.sh` — enforces structural connectedness
- `structure_check.sh` — enforces vault skeleton
- Config model (`defaults.conf` + `am.conf`)
- `README.md`

These four cover the highest-value checks. A vault with valid YAML, no broken links, no orphans, and the right folder structure is a vault with solid mechanical integrity.

**Full Wave 6** (adds three tools + orchestrator):
- `stub_detection.sh`
- `naming_validation.sh`
- `inventory.sh`
- `orchestrate.sh` + first health report

If the minimum viable set is delivered and the remaining tools require a second session, they can be completed as Wave 6.1 without a new proposal — the scope is already approved, the phasing just extends.

## Language Strategy

Most tools will be shell scripts — they're the natural fit for filesystem operations, link resolution, and structure checks. `yaml_validation.sh` will use Python (via a thin shell wrapper for exit code consistency) because robust YAML parsing in pure shell is unreliable.

All tools — regardless of language — read config in the same way, produce reports in the same Markdown format, and return the same exit codes. The interface contract is uniform; the implementation language is a per-tool decision.

## Traceability

| Decision | Foundation |
|----------|-----------|
| Build mechanical detection tools | [[AM — Integrity Layers]] — Mechanical Integrity layer; [[AM — Roadmap]] — Wave 6 |
| Tools are read-only, report-only | [[AM — Tool Conventions]] Convention 3 — tools report, they don't repair |
| Config-driven, portable across vaults | [[AM — Tool Conventions]] Convention 2 — no hardcoded assumptions |
| Conservative detection (no false positives) | [[AM — Tool Conventions]] Convention 7 — trust is the most important output |
| Meaningful exit codes | [[AM — Tool Conventions]] Convention 5 — 0/1/2 model |
| Each tool independently useful | [[AM — Tool Conventions]] Convention 4 — independently useful and composable |
| Enforce Vault Rules mechanically | [[AM — Integrity Layers]] — deterministic rules with one correct answer belong in Mechanical Integrity |
| Phase the work (tools first, orchestrator second) | D3 (Controlled Evolution) — graduated steps |
| Don't remediate findings in this wave | D6 (Separation of Powers) — detection and remediation are separate responsibilities |
| Scope degradation path | Law 3 (Economy) — deliver the minimum that proves the concept if full scope is at risk |

## Impact Assessment

**What this affects:**
- `04_EXECUTE/tools/` — currently empty; this wave populates it with the vault-maintenance suite
- `05_RECORD/reports/` — currently empty; receives the first health report
- `SYSTEM_MAP.md` — updated to reflect new vault contents
- Future waves — the health report may reveal structural issues that need remediation (separate wave or session work). Wave 7 (Runtime & Execution) will add code to `04_EXECUTE/runtime/`; the mechanical integrity tools built here provide the baseline for detecting issues in that code.

**What could go wrong:**

- **Over-engineering the config model.** Portability is a goal, but AM is the only vault using these tools right now. Mitigation: build config for AM first, extract generalisation only where it's trivially cheap. Don't solve portability problems we haven't encountered yet.
- **Script complexity.** Shell scripts have limits — particularly for YAML parsing and relationship graph traversal. Mitigation: use Python where shell is insufficient (see Language Strategy). The convention governs behaviour, not language choice.
- **False positives in orphan detection.** Orphan detection depends on parsing all links in all files. If the parser misses a link format, it will falsely flag files as orphaned. Mitigation: Convention 7 (conservative). Start with `[[wiki-links]]` and frontmatter `relationships` only — the formats the vault actually uses. Expand later if needed.
- **The health report reveals a lot of issues.** Wave 5.2 hardened the vault, but mechanical checks may find things human review missed. Mitigation: this is a feature, not a bug. The whole point is to find what we can't see. Findings are triaged by Rob; remediation is scoped separately.

## Alternatives Considered

**Alternative 1: Build a single monolithic validation script**
Rejected. A single script that does everything violates Convention 4 (independently useful and composable). Individual tools can be run in isolation, debugged independently, and composed flexibly. A monolith can't.

**Alternative 2: Use Python exclusively (no shell scripts)**
Considered viable. Python handles YAML natively and is better for complex checks. But shell scripts are simpler for filesystem operations (file existence, link resolution, structure checks). Decision: use the right language for each tool with a uniform interface contract. See Language Strategy.

**Alternative 3: Build the orchestrator first, then the individual tools**
Rejected. The orchestrator is a composition layer — it has nothing to compose until the individual tools exist. Phase 1 before Phase 2 follows the natural dependency order.

**Alternative 4: Include remediation capability (auto-fix broken links, create missing stubs)**
Rejected. [[AM — Tool Conventions]] Convention 3 is absolute: tools report, they don't repair. Remediation requires judgment about *how* to fix, which is a Semantic Integrity responsibility. If automated remediation is needed in the future, it belongs in a separate tool category with its own governance.

## Gate Criteria

**This proposal is ready to execute when:**

- [x] Proposal drafted with all required elements
- [x] Adversarial audit completed (alignment, integrity, viability)
- [x] Human (Rob) approves the proposal
- [x] Audit findings resolved

**Wave 6 is complete when:**

- [ ] All seven detection tools implemented and individually runnable (or minimum viable four — see Scope Degradation)
- [ ] Config model implemented: `defaults.conf` with generic defaults, `am.conf` with AM-specific configuration, both parseable by all tools
- [ ] Each tool's exit codes validated individually: exit 0 on a clean vault, exit 1 when given a vault with at least one issue in the tool's domain, exit 2 when given invalid config or a missing vault path
- [ ] Each tool produces a Markdown report matching the defined report format (header with tool/vault/timestamp, summary table, findings list, warnings list)
- [ ] Orchestrator runs all tools in sequence and produces an aggregate health report with: per-tool summary (name, exit code, finding count), combined findings, overall exit code
- [ ] First health report generated against AM vault, reviewed by Rob, findings categorised, report filed in `05_RECORD/reports/`
- [ ] `README.md` documents all tools, config schema, invocation examples, and output format
- [ ] `SYSTEM_MAP.md` updated to list `04_EXECUTE/tools/vault-maintenance/` and its contents
- [ ] Wave 6 reflection written and filed in `06_REFLECT/`
- [ ] Capture seed for Wave 7 created in `01_CAPTURE/`

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal creates new executable artifacts in `04_EXECUTE/tools/` and new report artifacts in `05_RECORD/reports/`. It does not modify governance documents. The two governance documents created during design (Integrity Layers, Tool Conventions) were approved separately prior to this proposal.
