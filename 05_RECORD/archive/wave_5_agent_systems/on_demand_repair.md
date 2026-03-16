---
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
  - CONST.vault_maintenance.specialist.self_healing
produces: []
  - MAP.vault_maintenance
  - CONST.vault_maintenance.supervisor
  - CONST.vault_maintenance.specialist.self_healing
  - MAP.vault_maintenance
tags:
  - constellation
  - workflow
  - vault_maintenance
  - repair
  - on_demand
supersedes: []
superseded_by: []
hash: ""
owner: ""
resolution_basis: authority_weight
title: On-Demand Repair Workflow
---

# On-Demand Repair Workflow

## Purpose

The On-Demand Repair Workflow executes targeted repairs to specific vault issues identified by audit specialists or requested by the Knowledge Executive. It invokes the Self-Healing Repairer to attempt repairs within authority boundaries, handles escalations for complex changes, and validates that repairs were successful. This workflow enables rapid response to critical issues while maintaining governance compliance.

## Stages

### Stage 1: Repair Request Reception
**Agent**: Maintenance Coordinator
**Action**: Receive repair request from audit findings or manual trigger

- Receive repair request with context (which notes, what issues, why)
- Validate that request is within constellation's authority
- Check if repair is already in flight or would conflict with other changes
- Analyze repair complexity and risk level
- Determine if repair can be handled autonomously or requires escalation
- Create repair ticket with ID, priority, context
- Proceed to Stage 2 (Repair Analysis)

**Inputs**:
- Repair request (from audit specialist or Knowledge Executive)
- Audit finding evidence and justification
- Current state of notes to be repaired

**Outputs**:
- Repair ticket ID and metadata
- Risk assessment (low/medium/high)
- Execution plan (which specialist does what)
- Initial escalation determination

### Stage 2: Repair Analysis and Planning
**Agent**: Maintenance Coordinator
**Action**: Analyze repair request and plan execution

- Examine specific notes that need repairs
- Identify all relationships that might be affected
- Check for dependencies or cascading implications
- Assess risk level (confidence of successful repair)
- Determine if repairs can be done independently or need ordering
- Classify repair type (template fix, relationship repair, content clarification)
- If low-risk: approve for autonomous execution (Stage 3a)
- If medium-risk: prepare for supervised execution (Stage 3b)
- If high-risk: prepare for escalation (Stage 4)

**Inputs**:
- Repair ticket from Stage 1
- Full note content and metadata
- Relationship graphs and dependencies

**Outputs**:
- Detailed repair plan
- Risk classification
- Execution path (autonomous, supervised, or escalation)
- Before-state snapshot for audit trail

### Stage 3a: Autonomous Repair Execution (Low-Risk)
**Agent**: Self-Healing Repairer
**Action**: Execute repairs within authority without approval

Applicable to:
- Template formatting fixes (YAML syntax, field ordering)
- Simple relationship repairs (adding missing unambiguous links)
- Metadata normalization (date formatting, version numbers)
- Tag standardization using canonical glossary
- Optional field population with defaults

Process:
- Receive repair plan from Maintenance Coordinator
- Load notes to be repaired
- Apply repairs as planned
- Validate repairs resolve issues
- Create audit trail documenting changes
- Report completion to Coordinator

**Outputs**:
- Repaired notes with updated timestamps
- Audit trail with before/after state
- Validation results confirming issue resolution
- Completion report to Coordinator

### Stage 3b: Supervised Repair Execution (Medium-Risk)
**Agent**: Maintenance Coordinator (supervisor), Self-Healing Repairer (executor)
**Action**: Execute repairs with supervisor validation

Applicable to:
- Confidence level 60-79% repairs
- Relationship changes on notes with authority_weight 70-79
- Content clarifications with semantic significance
- Repairs affecting 2-5 notes in dependent way
- Archive decisions with existing relationships

Process:
- Coordinator reviews proposed repairs with Self-Healing Repairer
- Coordinator approves or requests modifications
- Self-Healing Repairer executes approved repairs
- Coordinator validates outcomes
- Create audit trail documenting approval and execution

**Inputs**:
- Repair plan from Stage 2
- Specific repairs proposed
- Risk assessment and justification

**Outputs**:
- Approval documentation
- Executed repairs with audit trail
- Validation confirmation
- Completion report

### Stage 4: High-Risk Escalation
**Agent**: Maintenance Coordinator
**Action**: Escalate high-risk repairs to Knowledge Executive

Applicable to:
- Any modification to authority_weight >= 80 notes
- Confidence level < 60% repairs
- Structural ontology changes
- Relationship type inversions or category shifts
- Permanent deletions or content removal
- Changes to governance documents

Process:
- Coordinator analyzes repair and documents risk factors
- Coordinator prepares escalation package with full context
- Submit escalation to Knowledge Executive with:
  - Specific changes proposed
  - Risk assessment and reasoning
  - Evidence of issues needing repair
  - Alternative approaches if any
- Wait for Knowledge Executive decision
- Execute approved repairs or hold for clarification

**Outputs**:
- Escalation documentation
- Risk analysis package
- Knowledge Executive decision
- Pending repair status

### Stage 5: Validation and Verification
**Agent**: Self-Healing Repairer or Maintenance Coordinator
**Action**: Validate that repairs actually resolved issues

- Re-run relevant audit check to confirm issues are resolved
- Check for side effects or unintended consequences
- Verify related notes still have consistency
- Sample-check downstream relationships
- Confirm no new issues were introduced by repairs

**Inputs**:
- Repairs executed in Stage 3 or Knowledge Executive approval from Stage 4
- Original issue description and evidence

**Outputs**:
- Validation results (pass/fail)
- Evidence that issues are resolved
- Any new issues discovered during validation

### Stage 6: Repair Completion and Reporting
**Agent**: Maintenance Coordinator
**Action**: Complete repair workflow and report results

- Log all repairs executed with full audit trail
- Generate repair completion report for Knowledge Executive
- Update vault metrics reflecting repairs
- Close repair ticket
- Store audit trail in 06_EXECUTION/logs/vault_maintenance_log.md
- Trigger any necessary follow-up actions

**Outputs**:
- Repair completion report
- Full audit trail for governance
- Closure of repair ticket
- Updated vault health metrics

## Entry Conditions

- **Trigger 1**: Audit specialist finds issue, recommends repair
- **Trigger 2**: Knowledge Executive requests specific repair
- **Trigger 3**: Automated alert from system detects critical issue
- **Prerequisite**: Repair is within constellation's authority OR can be escalated

## Exit Conditions

- **Success**: Issue resolved, repairs validated, audit trail complete
- **Escalation**: Repair escalated to Knowledge Executive pending decision
- **Partial**: Low-risk repairs completed, high-risk items escalated
- **Deferred**: Repair held pending additional information or context
- **Rejected**: Repair found infeasible or conflicting with other work

## Risk Categories and Escalation Paths

### Low-Risk → Autonomous (Stages 1, 2, 3a, 5, 6)
- Template fixes, simple relationship repairs
- Execution: Repairer executes autonomously
- Duration: 1-5 minutes
- Approval: None required

### Medium-Risk → Supervised (Stages 1, 2, 3b, 5, 6)
- Relationship changes on lower-authority notes
- Repairs with 60-79% confidence
- Execution: Coordinator approves, Repairer executes
- Duration: 5-15 minutes
- Approval: Coordinator approval required

### High-Risk → Escalation (Stages 1, 2, 4, 5, 6)
- Changes to authority_weight >= 80 notes
- Structural ontology changes
- Permanent deletions
- Execution: Pending Knowledge Executive approval
- Duration: 15+ minutes (plus approval wait time)
- Approval: Knowledge Executive approval required

## Configuration

- **Parallel repairs**: Can handle multiple concurrent low-risk repairs
- **Priority ordering**: High-risk repairs take precedence in escalation queue
- **Timeout**: Escalations await response for up to 48 hours
- **Retry policy**: Failed repairs logged and reported, not retried autonomously
- **Audit retention**: All repair records retained indefinitely

## Related Processes

- [[scheduled_audit_cycle.md]]: Identifies issues for repair
- [[note_processing.md]]: Parallel inbox processing
- [[executive_link.md]]: Escalation point for high-risk repairs

---

**Trigger**: As needed from audit findings or manual request | **SLA**: Low-risk 15 min, Medium-risk 30 min, High-risk escalated same hour
