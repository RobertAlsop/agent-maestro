---
id: GOV.note_quality_rules
type: governance
note_class: knowledge
domain: agent_maestro
layer: knowledge
schema_version: 2
status: active
review_status: reviewed
version: 1
created_date: 2026-03-10
last_modified: 2026-03-15
authority_weight: 70
canonical: true
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Agent Maestro — Vault Rules]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs:
    - "[[02_KNOWLEDGE]]"
  inherits_from: []
  applies_to: []
  uses:
    - "[[Artifact Taxonomy]]"
  produces: []
tags:
  - governance
  - note_quality
  - vault_rules
  - agent_maestro
---

# Agent Maestro — Note Quality Rules

## Purpose

Rules that govern note quality when Claude authors or edits Agent Maestro notes. These rules are mandatory for all note creation and editing operations within the vault.

## Rules

1. Every note must use an approved template structure.
2. Every note must have a correctly formatted frontmatter block with a stable ID.
3. Every note must link to at least one canonical map.
4. Concept notes must contain at least two internal links.
5. No note may be empty or a placeholder.
6. Links must use the canonical ID format: `[[Authority Architecture]]`
7. Prefer short, well-linked notes over long, isolated notes.
8. Never invent IDs. Use the canonical prefix system from [[Artifact Taxonomy]].

## Validation Checklist

Before accepting any note as complete, verify:

### 1. YAML validity
- Frontmatter begins and ends with `---`
- Indentation is consistent (2 spaces)
- No tabs or mixed indentation

### 2. Field placement
Fields must appear in the correct order:
```
status / version
canonical / authority_weight / relationships
created_date / last_modified
```

### 3. Relationship structure
Every note contains:
```
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

### 4. Required sections in body
Verify each note contains:
- **Purpose**
- **Relationships** (body section)
- **Definition OR Responsibilities**

### 5. Obsidian loads cleanly
- No YAML parsing warnings
- Graph view renders normally
- Internal links resolve

## Relationships

- [[Agent Maestro — Vault Rules]] — parent governance document
- [[Artifact Taxonomy]] — canonical ID prefix system
- [[Agent Maestro — Principles]] — underlying principles this implements
