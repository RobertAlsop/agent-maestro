# Vault Maintenance Tool Suite

Mechanical integrity tools for Obsidian vaults. Validates structural health against configurable rules — detects broken links, invalid YAML, orphaned files, naming issues, and structural gaps.

Built as part of Agent Maestro Wave 6. Governed by [[AM — Tool Conventions]] and [[AM — Integrity Layers]].

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

| Tool | What it checks | Rules enforced |
|------|---------------|----------------|
| `structure_check.sh` | Required folders, root files, pipeline CLAUDE.md files exist and are non-empty | Vault Rules 1–4, 57 |
| `yaml_validation.sh` | YAML frontmatter parses, required fields present, controlled vocabulary valid, dates well-formed | Vault Rules 5, 9–14 |
| `broken_links.sh` | All `[[wiki-links]]` in body and frontmatter resolve to existing files. Flags concept/governance notes with zero body links | Vault Rules 15–19 |
| `orphan_detection.sh` | Every file is reachable via at least one inbound link. Structural files (CLAUDE.md, SYSTEM_MAP.md, README.md) are exempt | Vault Rule 20 |
| `stub_detection.sh` | No empty files, no frontmatter-only notes, no heading-only notes | Vault Rule 7 |
| `naming_validation.sh` | No duplicate filenames, no duplicate titles, frontmatter `title` matches filename | Vault Rule 34 |
| `inventory.sh` | Generates a manifest of all files with type, status, authority weight, and link counts | Vault Rules 21–23 |
| `orchestrate.sh` | Runs all tools in sequence, produces aggregate health report | — |

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
- **Python 3** with **PyYAML** — `yaml_validation.sh` only

Install PyYAML: `pip install pyyaml` or `pip3 install pyyaml`

## Architecture

```
vault-maintenance/
├── config/
│   ├── defaults.conf        # Generic vault defaults
│   └── am.conf              # Agent Maestro config
├── lib/
│   ├── config.sh            # Shared bash library (config parsing, report helpers)
│   └── yaml_validator.py    # Python YAML validation core
├── reports/                  # Generated reports (gitignored)
├── logs/                     # Operational logs (gitignored)
├── structure_check.sh
├── yaml_validation.sh       # Shell wrapper → lib/yaml_validator.py
├── broken_links.sh
├── orphan_detection.sh
├── stub_detection.sh
├── naming_validation.sh
├── inventory.sh
├── orchestrate.sh
└── README.md
```

## Design Principles

Per [[AM — Tool Conventions]]:

1. **Stateless read-check-report** — tools read vault state, check against rules, report findings
2. **Config-driven** — no hardcoded vault assumptions
3. **Read-only** — tools never modify vault content
4. **Independently useful** — each tool runs standalone
5. **Composable** — orchestrator coordinates without duplicating work
6. **Conservative** — no false positives; ambiguous cases go to warnings
7. **Machine-readable and human-readable** — Markdown reports with consistent structure
