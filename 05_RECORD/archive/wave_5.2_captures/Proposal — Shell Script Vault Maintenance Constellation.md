# Proposal — Shell Script Vault Maintenance Constellation

## Purpose

Build a reusable **Shell Script Vault Maintenance Constellation** that serves as the **mechanical integrity layer** for Obsidian-style knowledge vaults.

This constellation should be portable across:

- Agent Maestro
    
- Trust Birth Pools
    
- future vaults
    

Its job is to perform all **deterministic, syntax-level, and filesystem-level maintenance** that can be handled safely by scripts, so that LLM-based vault agents can focus only on **semantic interpretation, classification, and repair**.

---

## Core Principle

**Shell scripts enforce mechanical integrity.  
Agents enforce semantic integrity.**

The shell constellation must never interpret meaning.

It must not decide:

- what a note means
    
- whether two concepts are semantically duplicates
    
- whether a note belongs to ontology vs workflow vs governance when that requires judgment
    
- whether a concept definition has drifted
    
- whether a note should be promoted into canonical knowledge based on meaning
    

It should only detect and report **mechanical drift**.

---

## Role in the Full Maintenance Stack

The shell constellation sits below the agent constellation.

Vault  
  ↓  
Shell Script Vault Maintenance Constellation  
  ↓  
Agent Maestro Vault Maintenance Constellation  
  ↓  
Self-Healing Repair Execution

The shell layer is the **first-pass integrity filter**.

It detects structural anomalies and produces reports.

It does not make semantic decisions.

---

## Scope

### In scope

The shell constellation may:

- scan folder and file structure
    
- validate existence of required files
    
- validate syntax and formatting at a mechanical level
    
- detect broken links
    
- detect duplicate IDs
    
- detect missing required routing surfaces
    
- detect empty stubs
    
- generate inventories and health reports
    
- create missing stubs if explicitly configured
    
- run scheduled maintenance
    
- create Git commits for maintenance outputs
    
- run CI validation
    

### Out of scope

The shell constellation must not:

- semantically classify notes
    
- decide canonical note meaning
    
- merge notes
    
- split notes based on content
    
- rewrite definitions
    
- determine ontology alignment
    
- validate conceptual completeness of registries
    
- enforce template meaning beyond syntax-level checks
    
- move notes based on inferred semantics
    
- repair knowledge content
    

---

## Required Capabilities

## 1. Vault integrity scanning

Primary script:

- `vault_integrity_scan.sh`
    

Purpose:

Perform master scan of mechanical vault health.

Checks may include:

- missing required maps
    
- missing required registries
    
- missing required `CLAUDE.md` files
    
- missing required folders
    
- broken wikilinks
    
- broken relative links
    
- missing YAML block where required by rules
    
- malformed YAML
    
- duplicate IDs
    
- duplicate filenames
    
- unresolved stub files
    
- missing scaffold artifacts
    
- empty required files
    
- invalid file extensions in controlled regions
    

Primary output:

- `vault_health_report.md`
    

This is the core script of the constellation.

---

## 2. Inventory reporting

Primary script:

- `vault_inventory.sh`
    

Purpose:

Generate structural inventories.

Outputs may include:

- folder inventory
    
- file inventory
    
- markdown inventory
    
- note counts by folder
    
- required artifact coverage
    
- routing surface counts
    
- report timestamps
    

This supports audits, refactors, and downstream agent maintenance.

---

## 3. Broken link detection

Primary script:

- `broken_link_detector.sh`
    

Purpose:

Detect:

- broken wikilinks
    
- broken relative markdown links
    
- links to missing files
    

Output:

- `broken_links.txt`
    

---

## 4. YAML validation

Primary script:

- `yaml_validator.sh`
    

Purpose:

Perform syntax-only YAML checks.

Checks:

- YAML block present where configured as required
    
- YAML parses
    
- malformed YAML
    
- duplicate keys where detectable
    

Important:

This script checks **syntax only**, not semantic schema compliance.

Output:

- `yaml_errors.txt`
    

---

## 5. Duplicate ID detection

Primary script:

- `duplicate_id_detector.sh`
    

Purpose:

Detect duplicate note IDs mechanically.

Checks:

- repeated `id` values
    
- missing `id` in regions where required
    

Output:

- `duplicate_ids.txt`
    

---

## 6. Orphan file detection

Primary script:

- `orphan_file_detector.sh`
    

Purpose:

Detect files that are structurally detached according to configured routing rules.

This must remain conservative.

It may detect:

- no inbound links
    
- absent from known routing surfaces if rules explicitly define the expected surface
    
- unreferenced scaffold artifacts
    

Important:

This is a **structural orphan detector**, not a semantic orphan detector.

Output:

- `orphan_files.txt`
    

---

## 7. Stub detection

Primary script:

- `stub_detector.sh`
    

Purpose:

Detect unresolved scaffold placeholders.

Checks:

- `status: stub`
    
- empty maps
    
- empty registries
    
- empty `CLAUDE.md`
    
- unresolved placeholder templates
    

Output:

- `stub_report.txt`
    

---

## 8. Auto-commit

Primary script:

- `auto_commit.sh`
    

Purpose:

Commit maintenance outputs and optionally push them.

Behavior:

- detect changed files
    
- stage configured maintenance artifacts
    
- commit with timestamp
    
- optionally push
    
- optionally skip if nothing meaningful changed
    

Example commit message:

- `vault maintenance pass: 2026-03-14 18:10`
    

This should be configurable per vault.

---

## 9. Scheduled maintenance runner

Primary script:

- `run_scheduled_maintenance.sh`
    

Purpose:

Run the maintenance suite in unattended mode.

Supports:

- `cron`
    
- `launchd`
    

Behavior:

- run configured scripts
    
- write logs
    
- timestamp reports
    
- optionally trigger auto-commit
    
- optionally hand off reports to agent workflows
    

---

## 10. CI validation

Purpose:

Provide non-destructive validation in CI.

CI should run only validation scripts, not write actions.

Suggested CI checks:

- vault integrity scan
    
- broken link check
    
- YAML validation
    
- duplicate ID detection
    
- stub detection
    

Failure should return non-zero exit in strict CI mode.

---

## Architecture

Recommended structure:

vault-maintenance/  
  README.md  
  config/  
    vault.conf  
    rules.conf  
  scripts/  
    vault_integrity_scan.sh  
    vault_inventory.sh  
    broken_link_detector.sh  
    yaml_validator.sh  
    duplicate_id_detector.sh  
    orphan_file_detector.sh  
    stub_detector.sh  
    auto_commit.sh  
    run_scheduled_maintenance.sh  
    install_launchd.sh  
    install_cron.sh  
  reports/  
  logs/

---

## Configuration Model

The shell constellation must be config-driven.

Config should define:

- vault root path
    
- required folders
    
- required maps
    
- required registries
    
- required `CLAUDE.md` locations
    
- regions requiring YAML
    
- regions requiring IDs
    
- orphan detection rules
    
- stub markers
    
- auto-commit behavior
    
- push behavior
    
- scheduler mode
    
- CI strictness
    

This keeps the system portable across vaults.

---

## Operating Modes

### Audit mode

Read-only. Generates reports only.

### Maintenance mode

Runs scans, writes reports, optionally commits.

### CI mode

Strict non-destructive validation with non-zero exit on failure.

### Scheduled mode

Quiet unattended execution with logs and timestamps.

---

## Safety Rules

The shell constellation must be conservative.

Allowed write actions:

- generate reports
    
- generate logs
    
- create missing required stub files if explicitly enabled
    
- create maintenance commits
    
- push commits if explicitly enabled
    

Disallowed actions:

- semantic rewrites
    
- semantic moves
    
- note merging
    
- note splitting
    
- definition repair
    
- ontology repair
    
- template-content rewrites
    
- semantic archival decisions
    

---

## Definition of Done

The Shell Script Vault Maintenance Constellation is complete when it functions as:

- a reusable mechanical integrity layer
    
- a drift detection system
    
- a scheduled maintenance runner
    
- a Git-aware audit recorder
    
- a CI validation surface
    
- a clean upstream provider of reports to vault agents