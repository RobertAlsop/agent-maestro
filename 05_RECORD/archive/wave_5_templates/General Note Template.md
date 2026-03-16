---
title: "General Note Template"
type: concept
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  related:
    - "[[Skill Definition Template]]"
    - "[[Role Definition Template]]"
tags:
  - template
---

# General Note Template

## Purpose

Default template for vault notes that don't fit a specialized type (skill, role, governance). Use for concepts, references, reports, proposals, and general knowledge.

## Template

```yaml
---
title: ""
type: ""               # concept | reference | report | proposal | log | pipeline
status: draft           # draft | active | archived
authority_weight: 0     # 0-100 (set based on significance; ≥80 = canonical)
schema_version: 3
created: ""             # YYYY-MM-DD
updated: ""             # YYYY-MM-DD
relationships:
  derives_from: []      # what this traces to
  governs: []           # what this controls
  related: []           # other connections
tags: []
---
```

### Required Sections

**Purpose** — What this note is for. Every note must have this.

### Optional Sections (as appropriate)

**Principle** — For governance/conceptual notes: the core idea.

**Content** — The main body. Structure as needed for the subject matter.

**Implications** — What follows from this content.

**When It Applies** — Context for when this note is relevant.

**Related** — Wiki-links to connected documents.
