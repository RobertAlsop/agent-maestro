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
  - CONST.vault_maintenance.specialist.note_processor
produces: []
  - MAP.vault_maintenance
  - CONST.vault_maintenance.specialist.note_processor
  - MAP.vault_maintenance
tags:
  - constellation
  - workflow
  - vault_maintenance
  - ingestion
  - note_processing
supersedes: []
superseded_by: []
hash: ""
owner: ""
resolution_basis: authority_weight
title: Note Processing Workflow
---

# Note Processing Workflow

## Purpose

The Note Processing Workflow continuously ingests and processes new captures from the 01_CAPTURE inbox. It evaluates captures for quality and relevance, enriches them with proper governance metadata and frontmatter, promotes qualified captures into the canonical knowledge base (02_KNOWLEDGE through 05_SYSTEMS), archives stale or duplicate captures, and requests clarification for ambiguous items. This workflow ensures that the vault grows in an organized, governance-compliant manner.

## Stages

### Stage 1: Capture Monitoring and Discovery
**Agent**: Note Processor
**Action**: Monitor 01_CAPTURE directory and discover new items

- Scan 01_CAPTURE directory for new items
- Filter out system files and temporary items
- Identify captures that have been waiting for long periods (stale)
- Check for obvious duplicates against existing notes
- Prioritize items by freshness and apparent importance
- Report discovered items to Maintenance Coordinator

**Inputs**:
- 01_CAPTURE directory contents
- Existing vault index for duplicate detection
- Processing history (which captures have been seen before)

**Outputs**:
- List of new captures to process
- Stale capture flags
- Potential duplicates identified

### Stage 2: Capture Triage and Classification
**Agent**: Note Processor
**Action**: Analyze captures and determine classification

- Read capture content and metadata
- Classify by note type:
  - Agent definition (agent, constellation, etc.)
  - Governance document (principle, policy, rule, scope, etc.)
  - Process/workflow definition
  - Pattern or practice
  - Project or initiative
  - Concept or reference material
  - Other/unclear
- Assess content quality:
  - Clarity of purpose
  - Completeness
  - Coherence and internal consistency
  - Relationship to existing notes
- Determine target domain (vault_maintenance, agent_systems, authority_architecture, etc.)
- Identify target layer (02_KNOWLEDGE, 03_PIPELINES, 04_PROJECTS, 05_SYSTEMS)
- Flag quality concerns or gaps

**Inputs**:
- Capture content and structure
- Domain taxonomy
- Layer definitions and purposes
- Quality standards

**Outputs**:
- Classification (type, domain, layer)
- Quality assessment
- Identified gaps or concerns
- Classification confidence level

### Stage 3: Governance Validation
**Agent**: Note Processor
**Action**: Check that capture complies with governance standards

- Verify capture doesn't contradict existing governance
- Check for conflicts with core principles or policies
- Assess appropriateness of proposed authority_weight
- Verify domain assignment is correct
- Check for relationships to governance documents
- Ensure capture respects documented scope boundaries
- Flag any governance violations or concerns

**Inputs**:
- Classified capture
- Governance documents
- Authority policies
- Scope definitions

**Outputs**:
- Governance validation pass/fail
- Issues identified if any
- Recommended authority_weight
- Required relationships to governance documents

### Stage 4: Frontmatter Enrichment
**Agent**: Note Processor
**Action**: Generate proper YAML frontmatter for capture

For captures passing governance validation:

- Generate unique ID based on type and domain:
  - Authority docs: AUTH.domain.shortname
  - Agent definitions: CONST.domain.component
  - Workflows: WF.domain.workflowname
  - Governance: GOV.domain.docname
  - Knowledge: KNOW.domain.concept
  - Projects: PROJ.shortname
- Set type field from classification
- Set domain field from triage
- Set layer field from triage
- Assign authority_weight:
  - Governance documents: 75-90
  - Agent definitions: 60-75
  - Workflows/processes: 50-65
  - Knowledge/patterns: 40-60
  - Projects: 30-50
- Set status: "active"
- Set review_status: "draft" (requires human review before approval)
- Initialize relationships fields (may be empty, will be filled during canonical placement)
- Add created_date: today's ISO 8601 date
- Set source_type: "capture_promoted" or "user_submitted"
- Add schema_version: 2
- Generate tags from content analysis:
  - Core topic tags
  - Domain tags
  - Layer tags
  - Status tags

**Inputs**:
- Classification from Stage 2
- Governance validation from Stage 3
- Authority weight guidelines

**Outputs**:
- Complete YAML frontmatter
- Structured metadata ready for vault insertion

### Stage 5: Relationship Discovery
**Agent**: Note Processor
**Action**: Identify relationships between capture and existing notes

- Scan capture content for references to existing notes
- Extract wiki-links and explicit references
- Infer semantic relationships based on content:
  - Does it implement an existing governance document?
  - Does it define a concept used elsewhere?
  - Does it build on or extend an existing pattern?
  - Is it part of a larger system or initiative?
- Identify required relationships:
  - To governance documents (if applicable)
  - To related concepts (if applicable)
  - To authority documents (if agent/constellation)
- Mark relationships as candidates for bidirectional linking
- Prepare relationship metadata for frontmatter

**Inputs**:
- Enriched capture with frontmatter
- Vault index of existing notes
- Relationship taxonomy

**Outputs**:
- Identified relationships (defines, part_of, implements, uses, produces, etc.)
- Required bidirectional links
- Relationship metadata for frontmatter

### Stage 6: Promotion Decision
**Agent**: Note Processor
**Action**: Decide whether to promote, request clarification, or archive

**Decision Tree**:

1. **Quality and completeness check**
   - If missing required sections or critical information → Request Clarification (Stage 7)
   - If quality is insufficient → Request Clarification

2. **Governance validation check**
   - If conflicts with governance or scope → Flag for Escalation (Stage 8)
   - If violates principles or policies → Flag for Escalation

3. **Duplicate check**
   - If exact duplicate of existing note → Archive (Stage 9)
   - If near-duplicate → Request merging or clarification (Stage 7)

4. **Staleness check**
   - If capture is > 30 days old and stale → Archive (Stage 9)
   - If inactive capture with no activity → Consider archiving (Stage 9)

5. **Relationship validation**
   - If references broken or missing notes → Request clarification (Stage 7)
   - If relationships to critical notes unclear → Request clarification (Stage 7)

6. **Clear promotion criteria met**
   - If passes all checks → Proceed to Stage 10 (Canonical Placement)

**Outputs**:
- Promotion decision (promote, clarify, escalate, or archive)
- Justification for decision
- Any required actions

### Stage 7: Clarification Request
**Agent**: Note Processor
**Action**: Request additional information from capture source

For captures needing clarification before promotion:

- Generate clarification request with:
  - Specific gaps or issues identified
  - Questions for the source
  - Guidance on required improvements
  - Timeline for response
- Move capture to holding area (or mark with clarification tag)
- Update processing record with pending status
- Return capture to inbox for source response
- Report to Maintenance Coordinator

**Outputs**:
- Clarification request with specific feedback
- Pending clarification status
- Follow-up timeline

### Stage 8: Escalation to Knowledge Executive
**Agent**: Note Processor → Maintenance Coordinator
**Action**: Escalate items with governance conflicts or policy implications

For captures with governance violations or policy questions:

- Escalate to Maintenance Coordinator
- Document specific conflicts or concerns
- Provide capture content and analysis
- Request Knowledge Executive decision:
  - Promote with documented exception?
  - Reject and return to source?
  - Request source modifications?
- Wait for decision before proceeding

**Outputs**:
- Escalation documentation
- Knowledge Executive decision
- Path forward for capture

### Stage 9: Archive Decision
**Agent**: Note Processor
**Action**: Archive duplicates, stale, or rejected captures

For captures not promoted:

- Move capture to 99_ARCHIVE
- Document reason for archiving:
  - Duplicate of existing note
  - Stale or outdated
  - Rejected due to governance conflict
  - Superseded by newer version
- Maintain reference link from original to archive if needed
- Report archival to Maintenance Coordinator

**Outputs**:
- Archived captures in 99_ARCHIVE
- Archive justification documented
- Archive completion report

### Stage 10: Canonical Placement and Integration
**Agent**: Note Processor
**Action**: Place promoted capture in correct location in canonical layers

- Create note file in target layer directory:
  - 02_KNOWLEDGE for concepts and reference material
  - 03_PIPELINES for workflows and processes
  - 04_PROJECTS for project-specific items
  - 05_SYSTEMS for agent definitions and system architecture
- Write complete note with enriched frontmatter
- Create initial relationship entries (part_of, uses, etc.)
- Add bidirectional links to related notes
- Validate note against template compliance
- Register note in constellation or system map if applicable

**Inputs**:
- Enriched capture with complete frontmatter
- Discovered relationships
- Target location and domain

**Outputs**:
- New note in canonical layers
- Updated related notes (bidirectional links)
- Updated system maps if applicable
- Placement confirmation

### Stage 11: Processing Completion and Reporting
**Agent**: Maintenance Coordinator
**Action**: Complete processing workflow and report results

- Aggregate processing results:
  - Notes promoted to canonical
  - Clarifications requested
  - Escalations raised
  - Captures archived
- Generate processing report
- Log outcomes to processing journal (06_EXECUTION/logs/vault_maintenance_log.md)
- Report metrics to Knowledge Executive (if significant items escalated)
- Close processing cycle

**Outputs**:
- Processing completion report
- Metrics (promoted, clarified, escalated, archived)
- Status update to Knowledge Executive if escalations raised

## Entry Conditions

- **Continuous**: Note Processing runs continuously or on regular schedule (e.g., every 2 hours)
- **Trigger**: New items detected in 01_CAPTURE directory
- **Prerequisite**: 01_CAPTURE directory is accessible and monitored

## Exit Conditions

- **Complete**: All discovered captures processed and placed or escalated
- **Partial**: Some captures processed, others pending clarification or escalation
- **Deferred**: No new captures found; cycle waits for next trigger
- **Hold**: Unclear item held pending external information or decision

## Configuration

- **Monitoring frequency**: Every 2 hours or continuous
- **Staleness threshold**: 30 days without activity
- **Quality gates**: Template compliance, required sections, clarity standards
- **Default authority_weight**: Varies by type (see Stage 4)
- **Escalation triggers**: Governance conflicts, unclear scope, policy violations
- **Batch size**: Process captures as discovered, or batch by time period

## Related Processes

- [[scheduled_audit_cycle.md]]: Runs in parallel with note processing
- [[on_demand_repair.md]]: Called if newly promoted notes need repair validation
- [[executive_link.md]]: Escalation point for governance conflicts

---

**Frequency**: Continuous or every 2 hours | **Estimated per-capture time**: 5-15 minutes | **Escalation SLA**: Same day
