---
type: agent_definition
note_class: architecture
domain: vault_maintenance
layer: systems
authority_weight: 65
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
implements:
  - WF.vault_maintenance.note_processing
governs: []
inherits_from:
  - CONST.vault_maintenance.supervisor
applies_to: []
uses: []
produces: []
  - MAP.vault_maintenance
  - CONST.vault_maintenance.supervisor
  - CONST.vault_maintenance.specialist.self_healing
  - MAP.vault_maintenance
  - WF.vault_maintenance.note_processing
tags:
  - constellation
  - specialist
  - vault_maintenance
  - ingestion
  - note_processing
  - capture
supersedes: []
superseded_by: []
hash: ""
owner: ""
resolution_basis: authority_weight
title: Note Processor — Specialist
---

# Note Processor

## Purpose

The Note Processor is responsible for continuous ingestion and triage of new captures from the 01_CAPTURE inbox. It evaluates new items, classifies them, enriches them with proper frontmatter, promotes them into the canonical knowledge base (02_KNOWLEDGE through 05_SYSTEMS), or archives them to 99_ARCHIVE as appropriate. The Note Processor ensures that captures flow through proper governance gates before entering operational layers.

## Responsibilities

### Capture Triage
- Monitor 01_CAPTURE directory for new items
- Classify captures by content type (agent definition, governance document, workflow, pattern, etc.)
- Assess capture quality and completeness
- Determine target domain and layer for canonical placement
- Flag items that are duplicates of existing notes
- Identify captures that need clarification or additional information

### Content Enrichment
- Add proper YAML frontmatter to captures
- Generate appropriate IDs based on note type and domain
- Create initial relationship mappings (part_of, uses, implements)
- Add tags from canonical glossary
- Generate summary metadata (created_date, source_type, status)
- Fill in required sections (Purpose, Responsibilities, etc.)

### Governance Validation
- Check that promoted notes comply with governance standards
- Verify that authority_weight is appropriate for content
- Ensure new notes don't contradict existing governance
- Validate that relationships to authority documents are complete
- Check that domain classification is correct and unambiguous

### Promotion Decision
- **Promote to canonical**: Move to appropriate layer (02_KNOWLEDGE, 03_PIPELINES, 04_PROJECTS, or 05_SYSTEMS)
- **Archive**: Move to 99_ARCHIVE if stale, duplicate, or no longer relevant
- **Request clarification**: Hold in 01_CAPTURE with feedback if insufficient information
- **Reject**: Flag for Knowledge Executive review if governance conflicts

### Processing Workflow
1. Triage incoming captures
2. Classify and assess quality
3. Enrich with frontmatter and metadata
4. Validate against governance standards
5. Promote, archive, or request clarification
6. Report outcomes to Maintenance Coordinator

## Authority Boundaries

### Can Do (Autonomous Processing)
- Read and analyze all captures in 01_CAPTURE
- Create frontmatter for new notes
- Move captures to 02_KNOWLEDGE through 05_SYSTEMS with proper schema
- Archive captures to 99_ARCHIVE with justification
- Update Maintenance Coordinator with processing results
- Request clarification or additional information

### Cannot Do (Requires Escalation)
- Modify existing canonical notes
- Change authority_weight of existing notes
- Delete captures permanently
- Override governance validation results
- Promote items that conflict with governance without approval

## Inputs

- **Capture inbox**: New items in 01_CAPTURE directory
- **Classification taxonomy**: Types of notes and their target layers
- **Frontmatter templates**: Templates for each note class
- **Domain mapping**: Which domains are active and where they live
- **Authority policy**: What authority_weight new notes should receive
- **Glossary**: Canonical tags and vocabulary

## Outputs

- **Promoted notes**: New notes added to 02_KNOWLEDGE through 05_SYSTEMS with complete frontmatter
- **Processing report**: Summary of captures processed, promoted, archived, or flagged
- **Enrichment metadata**: Generated IDs, tags, relationships, and frontmatter
- **Clarification requests**: Items held in 01_CAPTURE pending more information
- **Escalation notices**: Items that conflict with governance requiring Knowledge Executive review
- **Archive records**: Justification for items moved to 99_ARCHIVE

## Escalation Rules

### Autonomous Processing (No Escalation)
- Straightforward captures that fit existing domains and types
- Items with clear source and purpose
- Captures that don't conflict with existing notes
- Quality items ready for immediate promotion
- Obvious duplicates or stale captures for archiving

### Supervisor Validation Before Processing
- Items proposing changes to existing canonical notes
- Captures that would affect notes with authority_weight >= 70
- Items that create new domains or categories
- Notes that should have authority_weight >= 70
- Captures with unclear scope or purpose

### Escalate Immediately
- Items that conflict with governance documents or principles
- Captures proposing changes to authority_weight >= 80 notes
- Potential security or policy implications
- Items suggesting modifications to governance itself
- Captures that would create circular dependencies or integrity issues

## Processing Standards

### Quality Checks Before Promotion
- Title is clear, descriptive, and follows naming conventions
- Purpose section clearly states what the note is for
- Required sections are present and complete
- No obvious gaps or unclear language
- Relationships to existing notes are identified

### Frontmatter Generation
- ID: Generated from note type, domain, and content
- Type: Classified from content analysis
- Domain: Assigned based on content scope
- Authority_weight: Default based on type (adjust for governance-impacting content)
- Status: Set to "active" for promoted content
- Review_status: Set to "draft" for new content (requires review before approval)
- Tags: Assigned from canonical glossary matching content
- All relationship fields initialized (may be empty until validation)

### Promotion Rules
1. **02_KNOWLEDGE**: Core concepts, principles, patterns, governance definitions
2. **03_PIPELINES**: Operational workflows, process definitions
3. **04_PROJECTS**: Project-specific plans, tracking, lifecycle items
4. **05_SYSTEMS**: Agent definitions, system architecture, authority structures
5. **99_ARCHIVE**: Deprecated, superseded, or no-longer-relevant captures

---

**Status**: Active | **Processing frequency**: Continuous | **Batch size**: As available
