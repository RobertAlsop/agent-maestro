---
schema_version: 2
title: "Note Upgrade Workflow"
type: pipeline
note_class: execution
domain: agent_maestro
layer: pipes
authority_weight: 65
resolution_basis: authority_weight
status: active
review_status: approved
version: 2
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Note Upgrade Process]]"
  part_of:
    - "[[Maintenance Pipeline]]"
    - "[[Consolidation Pipeline]]"
  implements:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
    - "[[05_SYSTEMS]]"
  uses: []
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - pipeline
  - maintenance
  - note_upgrade
  - knowledge
hash: ""
---

# Note Upgrade Workflow

## Purpose

Defines the three-stage workflow for upgrading vault notes to meet current schema and quality standards. Used during vault maintenance cycles, batch note promotions, and as Stage 3 of the [[Consolidation Pipeline]].

This workflow is an instance of the Process seed: perception (assess current state) → interpretation (identify gaps) → decision (plan upgrades) → action (execute upgrades) → memory (validate) → feedback (update maps).

---

## The Three-Stage Workflow

```
1. Knowledge Upgrade (content + frontmatter)
       ↓
2. Definition Alignment (cross-note consistency)
       ↓
3. Ontology Integrity Pass (structural coherence)
```

### Stage 1 — Knowledge Upgrade

Enrich notes with deeper, more accurate content aligned to current vault doctrine.

**Processing order** (upgrade what others depend on first):

| Priority | Layer | Folder | Rationale |
|----------|-------|--------|-----------|
| 1 | Governance doctrine | `02_KNOWLEDGE/governance/` | Everything aligns to this |
| 2 | Keystone concepts | `02_KNOWLEDGE/concepts/` | Core ontology |
| 3 | Domains | `02_KNOWLEDGE/domains/` | Application context |
| 4 | Patterns | `02_KNOWLEDGE/patterns/` | Design mechanisms |
| 5 | Indexes and registries | `02_KNOWLEDGE/indexes/` | Navigation anchors |
| 6 | System maps | `02_KNOWLEDGE/system_maps/` | Navigation layer |
| 7 | Agent systems | `05_SYSTEMS/agent_systems/` | Implementation |
| 8 | Authority architecture | `05_SYSTEMS/authority_architecture/` | Governance encoding |
| 9 | Pipelines | `03_PIPELINES/` | Workflow definitions |

**Per-note checklist**:
- Purpose section present and meaningful
- Frontmatter schema_version: 2 with all required fields
- At least two internal wiki-links
- Relationships block populated with correct typed links

**Exit condition**: All targeted notes have complete content and valid frontmatter.

### Stage 2 — Definition Alignment

Audit for consistency across the knowledge graph:
- Do linked notes use the same definition of shared concepts?
- Are relationship types correct (defines, implements, governs, etc.)?
- Are titles canonical and consistent?

**Exit condition**: No definitional contradictions between linked notes.

### Stage 3 — Ontology Integrity Pass

Verify structural coherence:
- Do all wiki-links resolve? (Run `check_link_integrity.sh`)
- Are there orphan notes? (Run `detect_orphan_notes.sh`)
- Does the concept hierarchy make sense?
- Are all maps current?

**Exit condition**: Link checker clean, orphan detector clean, graph navigable.

---

## Validation Checklist (Post-Upgrade)

Run after any batch upgrade or schema migration:

1. **YAML validity** — Frontmatter begins/ends with `---`, consistent 2-space indentation, no tabs
2. **Required fields present** — `schema_version`, `title`, `type`, `note_class`, `authority_weight`, `status`, `review_status`, `version`, `created_date`, `last_modified`, `tags`, `relationships`
3. **Relationship structure** — All typed relationship keys present (`defines`, `part_of`, `implements`, `governs`, `inherits_from`, `applies_to`, `uses`, `produces`)
4. **Body sections** — Purpose section + substantive content
5. **Link integrity** — Run `validate_frontmatter.sh` and `check_link_integrity.sh`

---

## Cadence Guidance

| Trigger | Stages to run |
|---------|---------------|
| After batch note promotion (e.g., capture processing) | All three stages |
| Weekly vault integrity audit | Stages 2–3 |
| After new concept notes added | Stage 2 |
| After schema changes | All three stages + validation checklist |

---

## Relationships

- [[Maintenance Pipeline]] — parent pipeline
- [[Consolidation Pipeline]] — uses this as Stage 3
- [[Agent Maestro — Foundations]] — kernel that defines upgrade standards
- [[Agent Maestro — Vault Rules]] — operational rules this enforces
