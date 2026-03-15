---
type: workflow_definition
note_class: execution
domain: vault_governance
layer: systems
canonical: false
authority_weight: 75
resolution_basis: authority_weight
schema_version: 2
title: "maintenance_cycle"
status: active
review_status: approved
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of:
  - '[[CONST.vault_curator.map]]'
  implements: []
  governs: []
  inherits_from: []
  applies_to:
  - '[[Vault Curator constellation]]'
  uses:
  - '[[CONST.vault_curator.agent.executive]]'
  - '[[CONST.vault_curator.agent.supervisor]]'
  - '[[CONST.vault_curator.agent.specialist.link_auditor]]'
  - '[[CONST.vault_curator.agent.specialist.schema_validator]]'
  - '[[CONST.vault_curator.agent.specialist.orphan_detector]]'
  produces:
  - '[[Audit Report]]'
  - '[[Execution Log]]'
- '[[Agent Maestro — Constellation Architecture Map]]'
- '[[CONST.vault_curator.agent.executive]]'
- '[[CONST.vault_curator.agent.supervisor]]'
- '[[Agent Maestro — Systems Map]]'
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
- workflow
- vault_governance
- maintenance
- constellation
hash: ''
---

# Vault Curator Maintenance Cycle

## Purpose

Full end-to-end workflow for [[Vault Curator constellation]] vault maintenance and integrity verification, orchestrating executive decision-making, supervisor coordination, specialist execution, and human escalation.

## Workflow Overview

The maintenance cycle is a repeating process executed by the [[Vault Curator constellation]]:

1. Executive reviews audit freshness and sets priorities
2. Supervisor orchestrates specialist execution
3. Specialists audit vault (links, schema, orphans)
4. Supervisor aggregates and applies safe fixes
5. Executive reviews escalations and escalates to human if needed
6. Human makes destructive action decisions
7. Results recorded in execution log

## Phase 1: Executive Review & Prioritization

**Agent**: [[CONST.vault_curator.agent.executive]] (Vault Governance Director)

**Activities**:
1. Review current audit reports (timestamps, freshness)
2. Assess which audits are stale (older than 30 days, e.g.)
3. Decide priority level for next maintenance cycle:
   - `CRITICAL`: Run all audits immediately
   - `HIGH`: Run audits, focus on broken links
   - `MEDIUM`: Run audits, review schema violations
   - `LOW`: Run audits, routine orphan detection
4. Generate priority directive with selected audits
5. Delegate to Integrity Coordinator (Supervisor)

**Authority**: Decision (approved by Executive)

**Escalation**: None at this phase

**Output**: Priority directive sent to Supervisor

## Phase 2: Supervisor Delegation

**Agent**: [[CONST.vault_curator.agent.supervisor]] (Integrity Coordinator)

**Activities**:
1. Receive priority directive from Executive
2. Decompose into specialist tasks:
   - Task 1: Link audit (→ Link Auditor)
   - Task 2: Schema validation (→ Schema Validator)
   - Task 3: Orphan detection (→ Orphan Detector)
3. Send execution instructions to each specialist
4. Distribute workspace contexts (vault file index, references)
5. Begin monitoring specialist progress

**Authority**: Coordination (delegates execution tasks)

**Escalation**: → Executive if specialist fails

**Output**: Specialist task assignments

## Phase 3: Specialist Execution (Parallel)

Three specialists execute in parallel, each independently:

### Link Auditor Execution
**Agent**: [[CONST.vault_curator.agent.specialist.link_auditor]]

**Activities**:
1. Receive task: "Run link audit"
2. Scan all vault files
3. Extract all `[[link]]` references
4. Verify each link destination exists
5. Classify broken links by severity
6. Write CSV report: `link_audit_report.csv`
7. Write execution log: `artifacts/logs/execution.log`
8. Report completion to Supervisor

**Output**: `workspaces/link_auditor/artifacts/link_audit_report.csv`

### Schema Validator Execution
**Agent**: [[CONST.vault_curator.agent.specialist.schema_validator]]

**Activities**:
1. Receive task: "Run schema validation"
2. Parse frontmatter from all files
3. Validate against Agent Maestro schema standard
4. Check required fields: id, type, note_class, schema_version
5. Identify violations (missing, invalid, malformed)
6. Classify by severity (CRITICAL, HIGH, MEDIUM, LOW)
7. Write CSV report: `schema_validation_report.csv`
8. Write execution log: `artifacts/logs/execution.log`
9. Report completion to Supervisor

**Output**: `workspaces/link_auditor/artifacts/schema_validation_report.csv`

### Orphan Detector Execution
**Agent**: [[CONST.vault_curator.agent.specialist.orphan_detector]]

**Activities**:
1. Receive task: "Run orphan detection"
2. Build complete link graph of vault
3. Analyze connectivity for all notes
4. Identify orphaned nodes (no incoming links)
5. Classify orphans: TRUE_ORPHAN, WEAKLY_CONNECTED, UNMAPPED, DEAD_END
6. Calculate connectivity scores
7. Write CSV report: `orphan_detection_report.csv`
8. Write execution log: `artifacts/logs/execution.log`
9. Report completion to Supervisor

**Output**: `workspaces/link_auditor/artifacts/orphan_detection_report.csv`

**Execution Model**: Parallel (all three specialists run simultaneously)

## Phase 4: Result Aggregation

**Agent**: [[CONST.vault_curator.agent.supervisor]]

**Activities**:
1. Receive completion notices from all specialists
2. Collect all three CSV reports
3. Merge findings into unified audit summary:
   - High-priority link breakages
   - Critical schema violations
   - True orphans detected
4. Identify patterns:
   - Which content areas have most issues
   - Which file categories have high violation rates
   - Which schema fields are most commonly missing
5. Generate aggregated audit report
6. Timestamp all reports with execution metadata

**Output**: Aggregated audit report + evidence package

## Phase 5: Safe Fix Execution

**Agent**: [[CONST.vault_curator.agent.supervisor]]

**Activities**:
1. Identify safe, non-destructive fixes from audit results:
   - **Link fixes**: Correct broken links where destination is known (e.g., file was renamed)
   - **Schema fixes**: Add missing required fields with default values
   - **Backlink fixes**: Add standard backlinks to isolated notes
2. For each proposed fix:
   - Validate that fix preserves content integrity
   - Confirm destination exists (for link fixes)
   - Check that fix aligns with standards
3. Execute all safe fixes
4. Log each fix with: file_path, fix_type, before_state, after_state

**Authority**: Execution (Supervisor can execute safe, non-destructive fixes)

**Fixes Allowed**:
- Repairing broken links to confirmed destinations
- Adding missing required frontmatter fields
- Correcting schema format violations
- Adding backlinks for integration

**Fixes NOT Allowed** (escalate to Executive):
- Deleting files or links
- Removing content
- Restructuring vault organization
- Changing metadata standards retroactively

**Output**: Execution log of all fixes applied

## Phase 6: Escalation Queue

**Agent**: [[CONST.vault_curator.agent.supervisor]]

**Activities**:
1. Identify all proposed actions that require approval:
   - Deletions (orphaned notes)
   - Link removals (broken links with no recovery option)
   - Structural changes
   - Unusual patterns requiring human judgment
2. For each escalation item, gather evidence:
   - Why action is needed
   - What would happen if not taken
   - Alternative approaches considered
   - Risk assessment
3. Create escalation queue with all evidence attached
4. Report to Executive for review and decision

**Output**: Escalation queue with evidence + risk assessment

## Phase 7: Executive Review & Decision

**Agent**: [[CONST.vault_curator.agent.executive]]

**Activities**:
1. Review Supervisor's aggregated audit report
2. Review safe fixes already applied
3. Review escalation queue (destructive actions)
4. For each escalation item:
   - Assess risk and impact
   - Review evidence from Supervisor
   - Make decision: APPROVE / REJECT / INVESTIGATE_FURTHER
5. If APPROVE: Send execution instructions to Supervisor
6. If REJECT: Request alternative approach
7. If INVESTIGATE_FURTHER: Escalate to human operator
8. Document all decisions in execution log

**Authority**: Decision (approves/rejects actions, escalates to human)

**Escalation Path**: → human_operator (if Executive cannot decide or if destructive action needed)

**Output**: Executive decision log

## Phase 8: Human Escalation (If Needed)

**Agent**: human_operator

**Activities** (if Executive escalates):
1. Review Executive's escalation report
2. Review all evidence collected by Supervisor
3. Review Executive's assessment
4. Make final decision on destructive actions
5. If APPROVE: Authorize Supervisor to proceed
6. If REJECT: Provide reasoning

**Authority**: Final decision authority on destructive actions

**Output**: Human authorization (or rejection)

## Phase 9: Execution of Approved Actions

**Agent**: [[CONST.vault_curator.agent.supervisor]]

**Activities** (if escalation approved):
1. Receive approval from Executive (or human if escalated)
2. Execute approved destructive actions:
   - Delete orphaned notes (if human approved)
   - Remove broken links (if human approved)
   - Restructure vault (if human approved)
3. For each action: log before state, action taken, after state
4. Verify vault integrity after each action

**Authority**: Execution (only for approved actions)

**Output**: Execution log of all destructive actions

## Phase 10: Final Log Update

**Agent**: [[CONST.vault_curator.agent.supervisor]]

**Activities**:
1. Compile final execution log from all phases
2. Record:
   - Audit reports (3 specialists)
   - Safe fixes executed
   - Escalations to Executive (and outcomes)
   - Escalations to human (and outcomes)
   - Final vault state
3. Timestamp everything
4. Write to `artifacts/logs/maintenance_cycle_<timestamp>.log`
5. Archive previous logs
6. Report cycle complete

**Output**: Final maintenance cycle log

## Complete Workflow Diagram

```
START
  ↓
[Phase 1] Executive: Review & Prioritize
  ↓
[Phase 2] Supervisor: Delegate to Specialists
  ↓
┌──[Phase 3] Parallel Specialist Execution
│  ├→ Link Auditor: audit links → report
│  ├→ Schema Validator: validate schema → report
│  └→ Orphan Detector: detect orphans → report
└──(all complete)
  ↓
[Phase 4] Supervisor: Aggregate Results
  ↓
[Phase 5] Supervisor: Execute Safe Fixes
  ↓
[Phase 6] Supervisor: Create Escalation Queue
  ↓
[Phase 7] Executive: Review & Decide
  ├→ APPROVE safe fixes: continue
  ├→ APPROVE destructive action: continue
  └→ ESCALATE: → Phase 8
  ↓
[Phase 8] Human (if escalated): Make Final Decision
  ├→ APPROVE: → Phase 9
  └→ REJECT: → Phase 10 (log rejection)
  ↓
[Phase 9] Supervisor: Execute Approved Actions (if any)
  ↓
[Phase 10] Supervisor: Final Log Update
  ↓
END (Maintenance Cycle Complete)
```

## Failure & Recovery

**If Specialist Fails**:
- Supervisor receives failure notice
- Escalates immediately to Executive
- Executive decides: RETRY / SKIP / INVESTIGATE
- If INVESTIGATE: escalates to human

**If Executive Cannot Decide**:
- Executive escalates to human immediately
- Provides: evidence, Supervisor recommendation, risk assessment
- Waits for human decision
- Implements human decision

**If Vault Modified During Cycle**:
- Supervisor detects integrity issue
- Pauses cycle
- Escalates to Executive
- Executive decides: ABORT_CYCLE / RESTART / INVESTIGATE

## Cycle Frequency

Default maintenance cycle runs on schedule:
- Weekly: Full audit (all three specialists)
- Post-Migration: Full audit (after vault restructuring)
- On-Demand: Triggered by human or Executive decision

Can be adjusted via Executive authority settings.

## Related Concepts

- [[Vault Curator constellation]]
- [[Executive-Supervisor-Specialist Pattern]]
- [[CONST.vault_curator.agent.executive]]
- [[CONST.vault_curator.agent.supervisor]]
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]]
