---
id: PIPE.note_upgrade_workflow
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
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
  uses:
    - "[[Note Knowledge Upgrade Order]]"
    - "[[Frontmatter Upgrade Checklist]]"
  produces: []
tags:
  - pipeline
  - maintenance
  - note_upgrade
  - knowledge
  - agent_maestro
---

# Note Upgrade Workflow

## Purpose

Defines the three-stage workflow for upgrading vault notes to meet current schema and quality standards. Used during vault maintenance cycles and after batch note promotions.

## The Three-Stage Workflow

```
1. Knowledge Upgrade
       ↓
2. Definition Alignment
       ↓
3. Ontology Integrity Pass
```

### Stage 1 — Knowledge Upgrade

Enrich notes with deeper, more accurate content aligned to current vault doctrine. Follow [[Note Knowledge Upgrade Order]] for the recommended processing sequence.

- Upgrade governance notes first, then concepts, then patterns, then domains, then systems, then maps, then pipelines, then authority packs
- Ensure each note has Purpose, Definition/Responsibilities, and Relationships sections
- Apply schema v2 frontmatter

**Exit condition:** All targeted notes have complete content and valid frontmatter.

### Stage 2 — Definition Alignment

Audit for consistency across the knowledge graph:
- Do linked notes use the same definition of shared concepts?
- Are relationship types correct (defines, implements, governs, etc.)?
- Are IDs canonical and consistent?

**Exit condition:** No definitional contradictions between linked notes.

### Stage 3 — Ontology Integrity Pass

Verify structural coherence:
- Does the graph render cleanly in Obsidian?
- Are all wiki-links resolving?
- Does the concept hierarchy make sense?
- Are all maps current?

**Exit condition:** Graph view clean, all links resolve, no orphaned concepts.

## Cadence Guidance

| Trigger | Stages |
|---------|--------|
| After batch note promotion (e.g., Phase C) | All three stages |
| Weekly vault integrity audit | Stages 2–3 |
| After new concept notes added | Stage 2 |
| After schema changes | All three stages |

## Relationships

- [[Maintenance Pipeline]] — parent pipeline
- [[Note Knowledge Upgrade Order]] — the recommended processing sequence for Stage 1
- [[Frontmatter Upgrade Checklist]] — the validation checklist for Stage 1
- [[Agent Maestro — Vault Rules]] — the governance document this implements
