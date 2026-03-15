---
type: system
note_class: architecture
domain: system_architecture
layer: systems

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Structured Data Registry"

status: active
review_status: draft
version: 1

created_date: 2026-03-14
last_modified: 2026-03-14

owner: AgentMaestro

relationships:
  defines: []
  part_of:
    - "[[Structured Data Layer]]"
  implements:
    - "[[Memory Model]]"
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []


  - "[[Structured Data Layer]]"
  - "[[Memory Model]]"


source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - system
  - structured_data
  - registry

hash: ""
---

# Structured Data Registry

## Purpose

Documents all CSV files in the Structured Data Layer — their location, schema, update rules, and purpose.

## CSV Conventions (Google Sheets Compatible)

All CSV files in Agent Maestro follow these conventions to ensure compatibility with Google Sheets:

- **Encoding:** UTF-8
- **Delimiter:** Comma (not semicolons or tabs)
- **Header row:** Always present as the first row
- **Cell values:** Atomic (no multi-line values, no merged cells)
- **Date format:** `YYYY-MM-DD` (ISO 8601)
- **Filenames:** Underscores, no spaces (e.g., `compiler_artifacts_registry.csv`)
- **One CSV per concern:** Each file serves a single operational purpose

## Registry of CSV Files

### Compiler Artifacts Registry

- **File:** `05_SYSTEMS/authority_architecture/compiler/compiler_artifacts_registry.csv`
- **Purpose:** Tracks all compiled governance artifacts
- **Columns:** `artifact_id`, `pack_id`, `pack_version`, `constellation`, `agent_role`, `compiled_date`, `compiler_version`, `host_type`, `host_path`, `status`
- **Updated by:** 01_CAPTURE/inbox/Authority Pack Compiler]] (Stage 8: Output Registration)

### Link Audit Report

- **File:** `06_EXECUTION/reports/link_audit_report.csv`
- **Purpose:** Output of the link auditor specialist
- **Columns:** `source_file`, `link_text`, `target_file`, `status`, `audit_date`
- **Updated by:** Link Auditor specialist agent
- **Status values:** `valid`, `broken`, `ambiguous`

### Schema Validation Report

- **File:** `06_EXECUTION/reports/schema_validation_report.csv`
- **Purpose:** Output of the schema validator specialist
- **Columns:** `file_path`, `field_name`, `issue_type`, `expected_value`, `actual_value`, `validation_date`
- **Updated by:** Schema Validator specialist agent
- **Issue types:** `missing_field`, `invalid_value`, `schema_version_mismatch`, `invalid_type`

### Knowledge Graph Index

- **File:** `02_KNOWLEDGE/indexes/knowledge_graph_index.csv`
- **Purpose:** Machine-readable export of the knowledge graph (all edges)
- **Columns:** `source_id`, `source_name`, `relationship_type`, `target_id`, `target_name`
- **Updated by:** Knowledge Graph export script (generated on demand)

### Constellation Registry

- **File:** `05_SYSTEMS/agent_systems/constellation_registry.csv`
- **Purpose:** Tracks deployed constellations and their status
- **Columns:** `constellation_id`, `constellation_name`, `executive_agent`, `status`, `created_date`, `last_executed`, `workspace_path`
- **Updated by:** Constellation deployment process

### Authority Pack Registry

- **File:** `05_SYSTEMS/authority_architecture/authority_pack_registry.csv`
- **Purpose:** Index of all authority packs with version and status
- **Columns:** `pack_id`, `pack_name`, `pack_type`, `version`, `status`, `parent_pack_id`, `constellation`, `created_date`, `updated_date`
- **Updated by:** Authority pack authoring process

### Escalation Log

- **File:** `06_EXECUTION/logs/escalation_log.csv`
- **Purpose:** Records all escalation events across constellations
- **Columns:** `escalation_id`, `constellation`, `source_agent`, `target_agent`, `escalation_type`, `reason`, `status`, `created_date`, `resolved_date`, `resolution`
- **Updated by:** Any agent raising or resolving an escalation

### Task Execution Log

- **File:** `06_EXECUTION/logs/task_execution_log.csv`
- **Purpose:** Records agent task executions with outcomes
- **Columns:** `execution_id`, `constellation`, `agent_id`, `agent_role`, `task_description`, `start_time`, `end_time`, `status`, `artifacts_produced`, `escalations_raised`
- **Updated by:** Any agent completing a task execution

## Related Concepts

- [[Structured Data Layer]] — the memory layer these files implement
- [[Memory Model]] — the top-level memory architecture
