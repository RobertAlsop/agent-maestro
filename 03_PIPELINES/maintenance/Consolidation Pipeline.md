---
schema_version: 2
title: Consolidation Pipeline
type: pipeline
note_class: execution
domain: agent_maestro
layer: pipes
authority_weight: 70
resolution_basis: authority_weight
status: active
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: ai_authored
relationships:
  defines:
    - "[[Consolidation Process]]"
  part_of:
    - "[[Maintenance Pipeline]]"
  implements:
    - "[[Agent Maestro — Foundations]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses:
    - "[[Build Session Protocol]]"
    - "[[State Change Logger]]"
  produces:
    - "[[Consolidation Audit Report]]"
  supersedes: []
  superseded_by: []
tags:
  - pipeline
  - consolidation
  - audit
  - maintenance
  - fractal
hash: ""
---

# Consolidation Pipeline

## Purpose

A reusable pipeline for systematically auditing, simplifying, and rationalizing a governed knowledge system. Consolidation answers one question: *Does this system carry anything it doesn't need?*

This pipeline was first instantiated as Wave 5 of the Agent Maestro Evolution Roadmap (v0.5.0), where it was applied to the Agent Maestro vault itself. It is designed to be reused — on this vault at future checkpoints, or on any external vault that Agent Maestro governs.

## Fractal Design Note

This pipeline embodies the fractal principle: the same consolidation process Agent Maestro applies to itself is the process it will offer to external vaults (Wave 8). The stages below are parameterized — they operate on a `target_vault` and use configurable quality criteria, not hardcoded paths or thresholds.

---

## Parameters

| Parameter | Type | Description | Example (Wave 5) |
|-----------|------|-------------|-------------------|
| `target_vault` | path | Root path of the vault or knowledge system to consolidate | Agent Maestro vault root |
| `quality_rubric` | document | Scoring criteria for content quality assessment | Accuracy, currency, necessity, duplication, authority weight correctness, relationship completeness |
| `governance_docs` | list | Documents that define the system's governance body | The 6 core governance docs (authority_weight 80-90) |
| `pipeline_registry` | path | Location of pipeline/workflow definitions | `03_PIPELINES/` |
| `capture_inbox` | path | Location of unprocessed input notes | `01_CAPTURE/` |
| `archive_location` | path | Where retired content is moved | `99_ARCHIVE/` |
| `log_output` | path | Where audit results and state changes are logged | `06_EXECUTION/logs/`, `06_EXECUTION/reports/` |
| `executor_boundary` | document | Reference for script-vs-LLM classification | LLM/Script Boundary Document |

---

## Stages

### Stage 1 — Audit Framework Setup

**Executor**: LLM (judgment required to design rubric) + Human (approval)

Define the quality rubric and scoring criteria that will be applied across all subsequent stages. The rubric must be explicit enough that two independent auditors would reach similar conclusions.

**Inputs**: Target vault structure, governance documents, existing quality standards
**Outputs**: Approved quality rubric document, audit scope definition, tier classification of content by priority

**Entry condition**: Target vault is accessible and its governance structure is understood.
**Exit condition**: Quality rubric approved by human. Tiers defined.

### Stage 2 — Governance Body Review

**Executor**: LLM (analysis and recommendation) + Human (approval for changes)

Examine the governance documents that define the system's rules and constraints. Assess each for necessity, clarity, redundancy, and appropriate authority. Produce a simplification proposal if warranted.

**Inputs**: Quality rubric (Stage 1), governance documents, any governance-adjacent files (e.g., CLAUDE.md, README)
**Outputs**: Governance review report, simplification proposal (if needed), approved simplifications applied

**Entry condition**: Quality rubric established.
**Exit condition**: Governance body reviewed. Changes (if any) approved and applied. All references updated.

**Sub-steps**:
1. Review each governance document against the rubric
2. Identify overlaps, redundancies, and gaps between governance docs
3. Identify overlaps between governance docs and implementation files (e.g., CLAUDE.md)
4. Produce simplification proposal (requires human approval before execution)
5. Execute approved simplifications and update all downstream references

### Stage 3 — Content Audit

**Executor**: Script (deterministic checks) + LLM (quality judgment) + Human (decisions on borderline cases)

Systematic review of every content item in the target system, working from highest authority/priority to lowest. For each item: assess accuracy, currency, necessity, duplication, metadata correctness, and relationship completeness.

**Inputs**: Quality rubric (Stage 1), tier classifications, target vault content
**Outputs**: Per-item audit verdicts (keep/simplify/merge/archive/delete), state change log entries, updated content

**Entry condition**: Governance body review complete (Stage 2) — governance documents set the standard that content is audited against.
**Exit condition**: Every content item has an audit verdict. Verdicts applied (archive/simplify/merge executed). Capture inbox at zero.

**Sub-steps**:
1. Tier-1 audit: highest authority/priority content (sets quality standard)
2. Tier-2 audit: mid-level content (references, concepts, maps)
3. Tier-3 audit: low-priority content (aggressive pruning)
4. Capture inbox processing: classify, enrich, promote, or archive every unprocessed item

**Audit verdicts**:

| Verdict | Meaning | Action |
|---------|---------|--------|
| KEEP | Content earns its place as-is | No change (may update metadata) |
| SIMPLIFY | Content is valuable but verbose or unclear | Rewrite/distill in place |
| MERGE | Content duplicates or overlaps another item | Combine into single authoritative note, archive duplicate |
| ARCHIVE | Content is not currently needed but has historical value | Move to archive location with `archive_reason` |
| DELETE | Content has no current or historical value | Remove (requires human approval for authority_weight > 50) |

### Stage 4 — Pipeline Rationalization

**Executor**: LLM (analysis) + Human (decisions on retire/keep)

Review all workflow/pipeline definitions. Classify each as operational (actively used), planned (needed for a defined future wave), or aspirational (no concrete consumer). Retire aspirational pipelines. Consolidate overlapping operational ones.

**Inputs**: Pipeline registry, workflow definitions, constellation/agent configurations that consume pipelines
**Outputs**: Classified pipeline inventory, retired pipelines moved to archive, consolidated pipeline definitions, validated surviving pipelines

**Entry condition**: Content audit complete — we know what agents and constellations exist and what they reference.
**Exit condition**: Only operational and explicitly-planned pipelines remain. Each surviving pipeline has complete metadata and valid contracts.

**Classification criteria**:

| Classification | Test | Action |
|----------------|------|--------|
| Operational | Referenced by active workflow or constellation AND has been executed | Keep, validate |
| Planned | Not yet operational but explicitly required by a defined future wave | Keep, tag with target wave |
| Aspirational | No active consumer and no concrete future plan | Archive with rationale |

### Stage 5 — Executor Boundary Definition

**Executor**: LLM (classification) + Script (validation of script candidates) + Human (approval)

For every recurring maintenance operation in the target system, determine whether the executor should be a deterministic script or an LLM agent. Implement the highest-value scripts. Document the boundary.

**Inputs**: Maintenance operations inventory (derived from pipeline definitions, constellation task lists, common operations), target vault structure
**Outputs**: Executor boundary document, implemented scripts, integration with logging infrastructure

**Entry condition**: Pipeline rationalization complete — we know which maintenance operations survive.
**Exit condition**: At least 3 deterministic scripts operational. Boundary document published. Both execution paths (script and LLM) feed the same logging infrastructure.

**Classification heuristic**:

| If the operation... | Then executor is... |
|---------------------|---------------------|
| Has a deterministic correct answer (yes/no, present/absent, count) | Script |
| Requires understanding meaning, context, or quality | LLM |
| Involves pattern matching against a known schema | Script |
| Involves judgment against a subjective rubric | LLM |
| Can be fully specified with regex, file-system queries, or CSV operations | Script |
| Requires reading and interpreting natural language content | LLM |

### Stage 6 — Consolidation Report + Exit Criteria

**Executor**: LLM (synthesis) + Human (sign-off)

Produce the final consolidation report: what was reviewed, what changed, what was archived, what was built. Verify all exit criteria are met. This stage is the formal close of the consolidation process.

**Inputs**: All outputs from Stages 1-5, state change log, audit verdicts
**Outputs**: Consolidation audit report, before/after metrics, exit criteria verification

**Entry condition**: All prior stages complete.
**Exit condition**: Report published to log output location. Human signs off that exit criteria are met.

**Report structure**:
1. Scope and parameters (what vault, what rubric, when)
2. Governance body: changes made, rationale
3. Content audit: items reviewed, verdicts, before/after counts
4. Pipeline rationalization: classified inventory, retirements, consolidations
5. Executor boundary: script/LLM map, scripts implemented
6. Metrics: note count before/after, pipeline count before/after, capture inbox before/after
7. Unresolved items and recommendations for future consolidation cycles

---

## Reuse Guide

To run this pipeline on a new target:

1. **Instantiate parameters**: Set `target_vault`, define or adapt the `quality_rubric`, locate the governance docs, pipeline registry, capture inbox, and archive location for the target system.
2. **Create a proposal**: Write a proposal (per [[Build Session Protocol]]) that references this pipeline and specifies the parameter values. The proposal is the specific instance; this pipeline is the abstract process.
3. **Run adversarial audit**: Audit the proposal per Build Session Protocol Stage 4.
4. **Execute stages in order**: Stages 1-6 have strict dependencies — each builds on the outputs of the previous. In particular, Stage 2 (Governance Body Review) must fully complete before Stage 3 (Content Audit) begins, because content is audited against governance standards that must be stable. Do not run governance review and content audit in parallel.
5. **Log everything**: All state changes flow through the same logging infrastructure regardless of target vault.

---

## Relationship to Other Pipelines

| Pipeline | Relationship |
|----------|-------------|
| [[Maintenance Pipeline]] | Parent — Consolidation is a type of maintenance, run periodically rather than continuously |
| [[Build Session Protocol]] | Consumer — Each consolidation instance is a build session governed by the protocol |
| [[Note Upgrade Workflow]] | Consumed by Stage 3 — Note upgrade is a sub-process of content audit |
| [[LLM-Script Boundary Reference]] | Produced by Stage 5 — Documents script vs LLM executor classification |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1 | 2026-03-15 | Initial pipeline definition, extracted from Wave 5 proposal |
| 2 | 2026-03-15 | Validated against Wave 5 execution (SES-012 through SES-017). Implements reference updated to Foundations. Frontmatter Upgrade Checklist ref replaced with LLM-Script Boundary Reference. All 6 stages confirmed operational. |
