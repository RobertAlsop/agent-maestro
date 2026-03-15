---
id: WF.vault_maintenance.audit_cycle
type: process
note_class: execution
domain: vault_maintenance
layer: pipes
authority_weight: 60
status: active
review_status: draft
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
source_type: ai_authored
schema_version: 2
defines: []
part_of:
  - CONST.vault_maintenance
implements: []
governs: []
inherits_from: []
applies_to: []
uses:
  - CONST.vault_maintenance.supervisor
  - CONST.vault_maintenance.specialist.definition_alignment
  - CONST.vault_maintenance.specialist.ontology_integrity
  - CONST.vault_maintenance.specialist.template_compliance
produces: []
map: MAP.vault_maintenance
maps:
  - MAP.vault_maintenance
related:
  - CONST.vault_maintenance.supervisor
  - CONST.vault_maintenance.specialist.definition_alignment
  - CONST.vault_maintenance.specialist.ontology_integrity
  - CONST.vault_maintenance.specialist.template_compliance
related_maps:
  - MAP.vault_maintenance
related_pipes: []
tags:
  - constellation
  - workflow
  - vault_maintenance
  - audit
  - scheduled
supersedes: []
superseded_by: []
hash: null
owner: null
resolution_basis: authority_weight
title: Scheduled Audit Cycle — Workflow
---

# Scheduled Audit Cycle Workflow

## Purpose

The Scheduled Audit Cycle is the primary maintenance workflow that runs on a regular schedule (daily or weekly) to audit the entire vault for consistency, integrity, and compliance. It coordinates execution across all three audit specialists, aggregates findings, and reports results to the Maintenance Coordinator. This workflow ensures continuous vault health monitoring and early detection of issues.

## Stages

### Stage 1: Audit Initiation
**Agent**: Maintenance Coordinator
**Action**: Receive trigger signal (scheduled time) and begin audit cycle

- Determine audit scope (full vault, specific domain, specific layer)
- Check if previous audit cycle has completed
- Prepare execution context (configuration, audit parameters)
- Initialize audit report aggregator
- Log audit cycle start with timestamp
- Invoke Stage 2 (Definition Alignment Audit)

**Outputs**:
- Audit cycle ID for tracking
- Audit scope and parameters
- Start timestamp in log

### Stage 2: Definition Alignment Audit
**Agent**: Definition Alignment Auditor
**Action**: Analyze definitions across scope for consistency and alignment

- Discover all definitions in audit scope
- Compare definitions of same concepts across notes
- Check for definitional drift in notes since last audit
- Validate authority alignment (lower-authority notes not redefining higher-authority concepts)
- Generate audit report with findings

**Inputs**:
- Audit scope parameters
- Reference definitions from canonical notes

**Outputs**:
- Definition audit report with identified issues
- List of problematic notes with specific issues
- Severity classification for each finding
- Evidence links to conflicting definitions

**Escalation triggers**:
- Contradictions in authority_weight >= 80 definitions
- Drift in core governance documents
- Issues affecting > 20% of audited notes

### Stage 3: Ontology Integrity Audit
**Agent**: Ontology Integrity Auditor
**Action**: Validate knowledge graph structure and relationships

- Check all wiki-links in scope for validity
- Validate relationship types and directions
- Detect orphaned or disconnected notes
- Find circular dependencies
- Validate cross-references and IDs
- Generate graph integrity report

**Inputs**:
- Audit scope
- Graph schema and relationship rules

**Outputs**:
- Ontology integrity report
- Broken links list with sources
- Relationship errors with context
- Orphan analysis
- Circular dependency detection
- Graph metrics and statistics

**Escalation triggers**:
- Broken links to authority_weight >= 80 documents
- Circular dependencies in authority/inheritance chains
- Relationship errors in governance documents
- Issues preventing system operation

### Stage 4: Template Compliance Check
**Agent**: Template Compliance Scanner
**Action**: Verify all notes conform to schema and templates

- Check schema_version and frontmatter completeness
- Validate field types, formats, and values
- Verify required sections are present
- Check relationship field completeness
- Validate tags match canonical glossary
- Generate compliance report

**Inputs**:
- Audit scope
- Template library for each note class
- Schema_version: 2 requirements

**Outputs**:
- Compliance audit report
- Detailed violations by note
- Missing fields and content sections
- Format errors and type violations
- Inconsistencies in metadata
- Severity classification

**Escalation triggers**:
- Missing required frontmatter in authority_weight >= 80 notes
- Invalid schema_version or core fields
- Type/domain mismatches affecting operations
- Template violations in governance documents

### Stage 5: Findings Aggregation and Analysis
**Agent**: Maintenance Coordinator
**Action**: Collect all specialist reports and analyze aggregate findings

- Aggregate findings across all three specialists
- Identify overlapping issues reported by multiple specialists
- Categorize issues by severity (critical, high, medium, low)
- Detect systemic patterns (e.g., single domain with high issue density)
- Prioritize repairs based on severity and dependencies
- Generate executive summary report

**Inputs**:
- Definition Alignment report
- Ontology Integrity report
- Template Compliance report

**Outputs**:
- Unified audit report
- Issues categorized by severity and type
- Prioritized repair queue
- Systemic issue analysis
- Metrics: total issues, by type, by domain, by layer

### Stage 6: Supervisor Reporting
**Agent**: Maintenance Coordinator
**Action**: Generate and submit report to Knowledge Executive

- Format findings for executive audience
- Highlight critical issues requiring immediate attention
- Summarize metrics and trends
- Provide recommendations for repairs or escalations
- Submit report to Knowledge Executive
- Log audit cycle completion
- Trigger Stage 1 of on-demand repair if critical issues found

**Outputs**:
- Executive summary report
- Detailed findings document
- Metrics dashboard
- Recommendations for Knowledge Executive
- Audit cycle completion timestamp

## Entry Conditions

- **Scheduled trigger**: Daily or weekly at configured time
- **OR manual trigger**: Knowledge Executive requests audit cycle
- **Prerequisite**: No concurrent audit or repair cycle in progress

## Exit Conditions

- **Success**: All three audit specialists complete without errors
- **Partial**: Some specialists complete; report generated with incomplete data
- **Failure**: Critical error in audit process; escalation to Knowledge Executive
- **Escalation**: Critical issues found requiring immediate Knowledge Executive action

## Configuration

- **Audit frequency**: Daily (full vault) or weekly (by domain rotation)
- **Scope rotation**: Option to audit single domain per day, full vault weekly
- **Parallel execution**: Audit specialists can run in parallel for efficiency
- **Report retention**: All audit reports logged to 06_EXECUTION/logs/vault_maintenance_log.md
- **Alert threshold**: Critical issues trigger immediate notification to Knowledge Executive

## Related Processes

- [[on_demand_repair.md]]: Triggered for critical findings
- [[note_processing.md]]: Runs continuously alongside audit cycles
- [[executive_link.md]]: Reports to Knowledge Executive

---

**Frequency**: Daily or weekly (configurable) | **Estimated duration**: 15-30 minutes per cycle | **Last run**: Pending first execution
