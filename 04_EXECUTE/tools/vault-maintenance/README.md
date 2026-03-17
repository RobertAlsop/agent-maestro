# Vault Maintenance Tool Suite

Mechanical integrity, pipeline enforcement, and git hygiene tools for Obsidian vaults. Validates structural health, process compliance, and version control conventions — detects broken links, invalid YAML, orphaned files, naming issues, structural gaps, lifecycle rule violations, and git convention drift.

Built across Agent Maestro Waves 6, 8.2, and 8.3. Governed by [[AM — Tool Conventions]], [[AM — Integrity Layers]], [[AM — Artifact Lifecycles]], and [[AM — Git Conventions]].

## Quick Start

```bash
# Run a single tool
./structure_check.sh --config config/am.conf --vault-root /path/to/vault

# Run all tools
./orchestrate.sh --config config/am.conf --vault-root /path/to/vault

# Quiet mode (reports only, no stdout)
./orchestrate.sh --config config/am.conf --vault-root /path/to/vault --quiet
```

## Tools

### Wave 6 — Structural Integrity

| Tool | What it checks | Rules enforced |
|------|---------------|----------------|
| `structure_check.sh` | Required folders, root files, pipeline CLAUDE.md files exist and are non-empty | Vault Rules 1–4, 57 |
| `yaml_validation.sh` | YAML frontmatter parses, required fields present, controlled vocabulary valid, dates well-formed | Vault Rules 5, 9–14 |
| `broken_links.sh` | All `[[wiki-links]]` in body and frontmatter resolve to existing files. Flags concept/governance notes with zero body links | Vault Rules 15–19 |
| `orphan_detection.sh` | Every file is reachable via at least one inbound link. Structural files (CLAUDE.md, SYSTEM_MAP.md, README.md) are exempt | Vault Rule 20 |
| `stub_detection.sh` | No empty files, no frontmatter-only notes, no heading-only notes | Vault Rule 7 |
| `naming_validation.sh` | No duplicate filenames, no duplicate titles, frontmatter `title` matches filename | Vault Rule 34 |
| `inventory.sh` | Generates a manifest of all files with type, status, authority weight, and link counts | Vault Rules 21–23 |

### Wave 8.2 — Pipeline Enforcement

| Tool | What it checks | Lifecycle spec |
|------|---------------|----------------|
| `capture_triage.py` | Capture items untriaged past deadline (14 days); routing provenance (bidirectional link check, warnings only) | Capture Item lifecycle |
| `proposal_lifecycle.py` | Status/location consistency; audit gate (non-empty `## Audit`); reflection existence for complete waves; archive gate for complete waves | Proposal lifecycle |
| `reflection_completeness.py` | Reflection existence per completed wave; capture seed existence per reflection; `derives_from` provenance in both directions | Reflection lifecycle |
| `concept_lifecycle.py` | Draft stagnation (>30 days); authority chain (`derives_from` non-empty); reflection reference (active concepts) | Concept lifecycle |
| `governance_compliance.py` | Authority floor (`authority_weight` ≥ 70 for governance docs); location enforcement (type: governance in governance folder); type/folder consistency vault-wide | Governance Document lifecycle |

### Wave 8.3 — Git Hygiene

| Tool | What it checks | Convention source |
|------|---------------|-------------------|
| `git_hygiene.py` | Branch naming (Check 1), stale branches (Check 2), direct master commits as warnings (Check 3), pre-wave tag presence (Check 4), tag naming (Check 5), commit message format (Check 6), uncommitted changes as warning (Check 7) | AM — Git Conventions |

### Orchestrator

| Tool | What it does |
|------|-------------|
| `orchestrate.sh` | Runs all tools in sequence (structural → pipeline → git), produces aggregate health report |

Each tool is independently runnable and produces a self-contained report.

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Clean — no issues found |
| `1` | Findings — issues detected, report written |
| `2` | Error — tool failed (bad config, missing vault path, etc.) |

## Configuration

Configuration uses YAML format. Two files in `config/`:

- **`defaults.conf`** — Generic Obsidian vault defaults (conservative baseline)
- **`am.conf`** — Agent Maestro-specific configuration (overrides defaults)

CLI arguments override both files for specific runs.

### Config Schema Reference

```yaml
# Path to the vault root directory (required)
vault_root: "/path/to/vault"

# Output directory for reports (relative to tool suite root, or absolute)
output_dir: "reports"

# structure_check.sh
required_folders: []          # Folders that must exist
required_root_files: []       # Files that must exist at vault root
required_claude_md: []        # CLAUDE.md files that must exist and be non-empty

# yaml_validation.sh
frontmatter_optional_folders: []   # Folders where YAML frontmatter is not required
required_fields: []                # Fields that must be present in frontmatter
controlled_vocabulary:             # Allowed values for specific fields
  type: []
  status: []
authority_weight_range:            # Valid range for authority_weight
  min: 0
  max: 100

# orphan_detection.sh
structural_exemptions: []     # Filenames exempt from orphan detection

# broken_links.sh
wiki_link_required_types: []  # Note types that must have body wiki-links

# All tools
exclude_patterns: []          # Paths/patterns excluded from all scans

# git_hygiene.py (Wave 8.3)
git_branch_patterns: []       # Regexes for valid branch names (master always exempt)
stale_branch_threshold_days: 30   # Days before an unmerged branch is flagged stale
master_branch: "master"       # Protected baseline branch name
master_commit_window: 50      # How many master commits to inspect for direct-commit check
git_tag_patterns: []          # Regexes for valid tag names
commit_message_window: 50     # How many recent commits to inspect for message quality
commit_min_length: 5          # Minimum subject line length (eliminates throwaway messages)
commit_format_patterns: []    # Regexes for accepted commit message formats
commit_reject_patterns: []    # Regexes for known-bad commit messages (hard fail)
check_uncommitted_changes: true   # Set false during active-session runs to suppress warning fatigue
```

### CLI Arguments

All tools accept:

| Argument | Description |
|----------|-------------|
| `--config FILE` | Path to vault-specific config file |
| `--vault-root DIR` | Vault root directory (overrides config) |
| `--output-dir DIR` | Report output directory (overrides config) |
| `--quiet` | Suppress stdout, write reports only |

## Report Format

Each tool produces a Markdown report in the configured output directory:

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

## Warnings (uncertain)

- [file path]: [description of ambiguous finding]
```

The orchestrator produces `vault_health_report.md` with per-tool summaries and combined findings.

## Requirements

- **Bash 3.2+** (macOS default) — all shell tools
- **Python 3** with **PyYAML** — `yaml_validation.sh` and all Wave 8.2 pipeline tools

Install PyYAML: `pip install pyyaml` or `pip3 install pyyaml`

## Architecture

```
vault-maintenance/
├── config/
│   ├── defaults.conf        # Generic vault defaults
│   └── am.conf              # Agent Maestro config (structural + pipeline + git hygiene)
├── lib/
│   ├── config.sh            # Shared bash library (config parsing, report helpers)
│   ├── yaml_validator.py    # Python YAML validation core (Wave 6)
│   └── vault_model.py       # Shared Python vault model (Wave 8.2) — imported by pipeline + git tools
├── reports/                  # Generated reports (gitignored)
├── logs/                     # Operational logs (gitignored)
├── structure_check.sh        # Wave 6
├── yaml_validation.sh        # Wave 6 — shell wrapper → lib/yaml_validator.py
├── broken_links.sh           # Wave 6
├── orphan_detection.sh       # Wave 6
├── stub_detection.sh         # Wave 6
├── naming_validation.sh      # Wave 6
├── inventory.sh              # Wave 6
├── capture_triage.py         # Wave 8.2 — pipeline enforcement
├── proposal_lifecycle.py     # Wave 8.2 — pipeline enforcement
├── reflection_completeness.py # Wave 8.2 — pipeline enforcement
├── concept_lifecycle.py      # Wave 8.2 — pipeline enforcement
├── governance_compliance.py  # Wave 8.2 — pipeline enforcement
├── git_hygiene.py            # Wave 8.3 — git convention detection
├── orchestrate.sh
└── README.md
```

### Library architecture

`lib/vault_model.py` is shared by all pipeline enforcement and git hygiene tools. It provides:
- `build_vault_model(vault_root, config)` — parse all vault frontmatter into VaultArtifact objects
- `parse_completed_waves(roadmap_content)` — extract completed wave identifiers from the Roadmap
- `write_report(...)` — standardized Markdown report writer
- Helper functions for exclusion, wiki-link parsing, date resolution, and reference checking

Each tool rebuilds the vault model per invocation (tools run as separate processes). The library's Economy value is code reuse — one implementation of YAML parsing, date resolution, config loading, and relationship traversal maintained in one place.

`git_hygiene.py` uses `subprocess` to call git CLI commands directly. No git library dependency is introduced — the git CLI is universally available and produces parseable output. Each of the seven checks runs independently with best-effort error isolation: if one check fails (e.g., Roadmap unavailable for Check 4), the remaining checks continue and the failure is reported as a warning in the output.

## Design Principles

Per [[AM — Tool Conventions]]:

1. **Stateless read-check-report** — tools read vault state, check against rules, report findings
2. **Config-driven** — no hardcoded vault assumptions
3. **Read-only** — tools never modify vault content
4. **Independently useful** — each tool runs standalone
5. **Composable** — orchestrator coordinates without duplicating work
6. **Conservative** — no false positives; ambiguous cases go to warnings
7. **Machine-readable and human-readable** — Markdown reports with consistent structure
