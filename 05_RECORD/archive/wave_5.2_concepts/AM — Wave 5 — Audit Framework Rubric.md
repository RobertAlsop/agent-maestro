---
schema_version: 2
title: "AM — Wave 5 — Audit Framework Rubric"
type: reference
note_class: governance
domain: agent_maestro
layer: knowledge
authority_weight: 70
resolution_basis: authority_weight
status: active
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: collaborative
relationships:
  defines:
    - "[[Audit Framework]]"
  part_of:
    - "[[AM — Wave 5 — Contract]]"
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
    - "[[03_PIPELINES]]"
    - "[[04_PROJECTS]]"
    - "[[05_SYSTEMS]]"
    - "[[06_EXECUTION]]"
    - "[[88_TEMPLATES]]"
    - "[[99_ARCHIVE]]"
  uses:
    - "[[Audit Taxonomy]]"
  produces: []
  supersedes: []
  superseded_by: []
tags:
  - wave-5
  - audit
  - rubric
  - phase-1
  - governance
hash: ""
---

# AM — Wave 5 — Audit Framework Rubric

**Purpose**: Defines the specific checks applied at each vault layer for each of the three audit types. This rubric is used throughout the Wave 5 alignment pass (Phases 2–5) to ensure consistent evaluation.

**Foundation**: Derived from the Audit Taxonomy in [[Agent Maestro — Foundations]].

---

## Audit Types (Review)

| Audit | Direction | Core Question | Kernel Basis |
|-------|-----------|---------------|-------------|
| **Alignment** | Top-down | Does this serve what's above it? | Law 1 (Direction of Authority) |
| **Integrity** | Horizontal | Is this internally sound and correctly connected? | Seed 2 (Structure) |
| **Viability** | Bottom-up | Is this earning its place? | Law 3 (Economy) |

---

## Rubric by Vault Layer

### Layer 1 — Governance (02_KNOWLEDGE/governance/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| G-A1 | Alignment | Does this doc serve the North Star? | LLM judgment |
| G-A2 | Alignment | Is it consistent with Foundations.md? | LLM judgment |
| G-A3 | Alignment | Does its authority_weight correctly reflect its position in the hierarchy? | Frontmatter validator |
| G-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| G-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| G-I3 | Integrity | Are relationships reciprocal (if A governs B, does B reference A)? | LLM judgment |
| G-I4 | Integrity | Are there internal contradictions between governance docs? | LLM judgment |
| G-V1 | Viability | Is this doc redundant with another governance doc? | LLM judgment |
| G-V2 | Viability | Is this doc redundant with Foundations.md? | LLM judgment |
| G-V3 | Viability | Could this doc be merged with another without loss? | LLM judgment |

### Layer 2 — Knowledge (02_KNOWLEDGE/ — all non-governance subfolders)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| K-A1 | Alignment | Does this doc serve a declared purpose traceable to governance? | LLM judgment |
| K-A2 | Alignment | Is authority_weight appropriate for this content? | Frontmatter validator + LLM |
| K-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| K-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| K-I3 | Integrity | Is the content current (not stale or outdated)? | LLM judgment |
| K-I4 | Integrity | Are typed relationships correct (defines, implements, etc.)? | LLM judgment |
| K-V1 | Viability | Is this doc an orphan (no incoming links)? | `detect_orphan_notes.sh` |
| K-V2 | Viability | Does this doc duplicate knowledge held elsewhere? | LLM judgment |
| K-V3 | Viability | Would removing this doc cause any loss of function or understanding? | LLM judgment |

### Layer 3 — Pipelines (03_PIPELINES/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| P-A1 | Alignment | Does this pipeline serve a declared operational need? | LLM judgment |
| P-A2 | Alignment | Does it follow the Process seed (Irreducible Loop)? | LLM judgment |
| P-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| P-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| P-I3 | Integrity | Does each stage have clear entry/exit conditions? | LLM judgment |
| P-I4 | Integrity | Is the executor classification clear (script/LLM/human)? | LLM judgment |
| P-V1 | Viability | Has this pipeline ever been executed? | LLM judgment (check logs) |
| P-V2 | Viability | Is this pipeline operational, planned, or aspirational? | LLM judgment |
| P-V3 | Viability | Could this merge with another pipeline without loss? | LLM judgment |

### Layer 4 — Projects (04_PROJECTS/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| PR-A1 | Alignment | Does this project serve the evolution roadmap or North Star? | LLM judgment |
| PR-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| PR-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| PR-I3 | Integrity | Does the project subfolder structure follow the standard? | LLM judgment |
| PR-V1 | Viability | Is the project active, completed, or stale? | LLM judgment |
| PR-V2 | Viability | Are there duplicate or overlapping projects? | LLM judgment |

### Layer 5 — Systems (05_SYSTEMS/)

**5a. Runtime modules (Python)**

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| SR-A1 | Alignment | Does this module implement the Constraint seed correctly? | LLM judgment |
| SR-A2 | Alignment | Does it address the Structure seed's seven primitives? | LLM judgment |
| SR-I1 | Integrity | Does the code execute without errors? | Script (`python -c "import module"`) |
| SR-I2 | Integrity | Is the module consistent with its documented interface? | LLM judgment |
| SR-V1 | Viability | Is this module used by any other component? | LLM judgment (import analysis) |

**5b. Authority packs + compiler artifacts**

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| SA-A1 | Alignment | Is the authority pack consistent with Foundations? | LLM judgment |
| SA-A2 | Alignment | Does the Constraint seed's chain rule hold? | LLM judgment |
| SA-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| SA-I2 | Integrity | Do compiled JSON artifacts match their YAML sources? | LLM judgment |
| SA-I3 | Integrity | Is the authority_pack_registry.csv consistent with actual files? | LLM judgment |
| SA-V1 | Viability | Is this authority pack assigned to an active agent? | Registry cross-check |

**5c. Agent systems (constellations)**

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| SC-A1 | Alignment | Does each constellation serve a foundational concern? | LLM judgment |
| SC-I1 | Integrity | Is the constellation_registry.csv consistent with actual files? | LLM judgment |
| SC-I2 | Integrity | Does each agent have a valid authority pack reference? | Registry cross-check |
| SC-V1 | Viability | Does this constellation have work to do? | LLM judgment |
| SC-V2 | Viability | Is this the minimum viable constellation set? | LLM judgment |

### Layer 6 — Execution (06_EXECUTION/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| E-A1 | Alignment | Does the logging infrastructure conform to Law 2? | LLM judgment |
| E-A2 | Alignment | Do dashboards serve their declared purpose? | LLM judgment |
| E-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| E-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| E-I3 | Integrity | Are CSV logs well-formed (headers, encoding, dates)? | LLM judgment |
| E-V1 | Viability | Are there stale or unused reports/dashboards? | LLM judgment |

### Layer 7 — Infrastructure (CLAUDE.md files)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| INF-A1 | Alignment | Does root CLAUDE.md reference Foundations? | LLM judgment |
| INF-A2 | Alignment | Do subdirectory CLAUDE.md files reflect current layer purpose? | LLM judgment |
| INF-I1 | Integrity | Are file paths and counts current? | Cross-check with inventory |
| INF-I2 | Integrity | Are naming conventions documented correctly? | LLM judgment |
| INF-V1 | Viability | Is every CLAUDE.md earning its place? | LLM judgment |

### Layer 8 — Templates (88_TEMPLATES/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| T-A1 | Alignment | Does this template embed the Structure seed's seven primitives? | LLM judgment |
| T-A2 | Alignment | Is it consistent with Foundations? | LLM judgment |
| T-I1 | Integrity | Are all frontmatter fields present and valid? | `validate_frontmatter.sh` |
| T-I2 | Integrity | Do all wiki-links resolve? | `check_link_integrity.sh` |
| T-I3 | Integrity | Is the template internally consistent (no conflicting guidance)? | LLM judgment |
| T-V1 | Viability | Is there a duplicate template serving the same purpose? | LLM judgment |
| T-V2 | Viability | Is this template in the minimum viable set? | LLM judgment |
| T-V3 | Viability | Has this template been used to create at least one instance? | LLM judgment |

### Layer 9 — Archive (99_ARCHIVE/)

| Check | Audit Type | What to Verify | Tool Support |
|-------|-----------|----------------|-------------|
| AR-A1 | Alignment | N/A — archived items are not expected to align with current governance | — |
| AR-I1 | Integrity | Quick inventory only — confirm contents exist | `ls` / count |
| AR-V1 | Viability | N/A — archived items are retained for reference | — |

---

## Verdicts

Each audit check produces one of:

| Verdict | Meaning | Action |
|---------|---------|--------|
| **PASS** | Component meets the check | No action needed |
| **FAIL** | Component does not meet the check | Remediation required |
| **N/A** | Check does not apply to this component | Document why |
| **DEFERRED** | Cannot be checked now (dependency or tooling gap) | Track for later |

Each component receives an overall verdict per audit type (PASS / FAIL / PARTIAL).

---

## Executor Classification

Each check has an executor:

| Executor | Meaning |
|----------|---------|
| **Script** | Deterministic check via shell script. Repeatable, no judgment. |
| **LLM** | Requires semantic understanding. Claude performs the check. |
| **Human** | Requires human authority (governance decisions, approval gates). |

The LLM/script boundary will be formally documented in Phase 6 (deliverable 6b).

---

**This rubric is used at every layer stop during the Wave 5 alignment pass. Results are recorded in the layer's audit verdict section of the session log.**
