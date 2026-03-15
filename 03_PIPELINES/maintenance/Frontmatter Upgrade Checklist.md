---
id: PIPE.frontmatter_upgrade_checklist
type: pipeline
note_class: execution
domain: agent_maestro
layer: pipes
schema_version: 2
status: active
review_status: reviewed
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
authority_weight: 60
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Maintenance Pipeline]]"
  implements:
    - "[[Agent Maestro — Note Quality Rules]]"
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
  uses: []
  produces: []
tags:
  - pipeline
  - maintenance
  - frontmatter
  - checklist
  - agent_maestro
---

# Frontmatter Upgrade Checklist

## Purpose

A 5-check validation checklist to run after any frontmatter migration or upgrade operation. Ensures structural integrity before accepting note changes as complete.

## When to Use

Run this checklist after:
- Any batch frontmatter upgrade
- Any schema migration (e.g., schema_version: 1 → 2)
- Any automated note enrichment operation
- Any bulk promotion of capture notes

## The Five Checks

### Check 1 — YAML Validity

Open a sample of edited notes and confirm:
- Frontmatter begins and ends with `---`
- Indentation is consistent (2 spaces)
- No tabs or mixed indentation

### Check 2 — Field Placement Rule

Fields must appear in the correct location order:

```
status
version (if present)

canonical
authority_weight
relationships

created_date / last_modified
```

### Check 3 — Relationship Structure

Confirm every note contains all relationship keys:

```yaml
relationships:
  defines:
  part_of:
  implements:
  governs:
  inherits_from:
  applies_to:
  uses:
  produces:
```

No wiki-links inside these lists — IDs or canonical names only.

### Check 4 — Required Body Sections

Verify each note contains:
- **Purpose**
- **Relationships** (body section)
- **Definition OR Responsibilities**

No template should be missing these three sections.

### Check 5 — Obsidian Loads Cleanly

Open the vault and verify:
- No YAML parsing warnings
- Graph view still renders normally
- Internal links still resolve

If all five checks pass, the migration or upgrade is structurally safe.

## Related Pipeline

This checklist is part of [[Maintenance Pipeline]]. It is typically run as the final validation stage of any Note Upgrade Workflow execution.

## Relationships

- [[Maintenance Pipeline]] — parent pipeline
- [[Agent Maestro — Note Quality Rules]] — the rules this validates against
- [[Agent Maestro — Vault Rules]] — vault-level rules this enforces
- [[Note Upgrade Workflow]] — the workflow that precedes this checklist
