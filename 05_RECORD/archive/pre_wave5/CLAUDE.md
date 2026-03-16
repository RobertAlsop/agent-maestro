# 99_ARCHIVE

## Purpose

The ARCHIVE layer contains historical items, completed projects, deprecated patterns, archived concepts, and superseded governance documents. ARCHIVE is read-only and serves as a reference library for understanding how the system evolved and what was tried in the past.

Items move to ARCHIVE when they are no longer actively used but retain historical or reference value. ARCHIVE enables learning from past experiments and decisions without cluttering active operational areas.

## Principles

- **Read-Only**: Archive contents should never be modified
- **Reference Value**: Archive contains items worth keeping for historical context
- **Auditability**: Archive enables auditing of past decisions and experiments
- **Searchability**: Archive items should be findable but not prominently linked from active layers

## Organization

Archives are typically organized by type and date:

- **archived_projects/**: Completed or cancelled projects (moved from 04_PROJECTS)
- **deprecated_patterns/**: Patterns that have been superseded or are no longer recommended
- **superseded_governance/**: Old versions of governance documents (new versions are in 02_KNOWLEDGE/governance/)
- **experimental_notes/**: Results of experiments and prototypes
- **historical_logs/**: Old execution logs (for retention but not active use)

Location: `/sessions/loving-busy-bohr/mnt/Agent Maestro/99_ARCHIVE/`

## Conventions

- Add a frontmatter field: `archived_date: YYYY-MM-DD` to all archived items
- Include: `archive_reason`: Why this was archived (e.g., "Project completed", "Pattern superseded", "Experiment concluded")
- If superseded: Include `replaced_by: [[New Item Name]]` linking to the replacement
- Keep original content unchanged (archive preserves history exactly)

## Agent Rules

**Agents MAY**:
- Read archived items for historical context and learning
- Reference archived items when explaining past decisions
- Search archive to understand how previous decisions were made

**Agents MUST NOT**:
- Modify any archived items
- Delete archived items
- Treat archived items as current authority (they're historical only)
- Resurrect archived patterns or processes without escalation

**Escalation Required**:
- Decisions to delete archived items permanently
- Requests to un-archive and re-activate archived processes
- Modifications to archived items (even to fix errors)

## Archive Dates and Retention

- Items archived 1-2 years ago: Active reference value, still frequently consulted
- Items archived 2-5 years ago: Historical value for understanding system evolution
- Items archived 5+ years ago: Long-term archival, rarely consulted but kept for completeness

Retention policies should balance storage cost against reference value. In general:
- Keep archived items indefinitely unless company retention policies require deletion
- Archive entire directories when a project or initiative completes

## Archiving Workflow

To archive an item:

1. **Identify**: Determine the item is no longer active
2. **Document**: Add `archived_date` and `archive_reason` to frontmatter
3. **Link Replacement**: If superseded, add `replaced_by` link to new item
4. **Move to Archive**: Move item from active location to 99_ARCHIVE
5. **Update References**: Remove links from active items pointing to archived item (or update to archive location)
6. **Communicate**: Notify stakeholders that item has been archived

## Example Archive Categories

Items typically archived:

- **Completed Projects**: From 04_PROJECTS/active/ → 99_ARCHIVE/archived_projects/
- **Superseded Patterns**: Old versions → 99_ARCHIVE/deprecated_patterns/
- **Deprecated Processes**: Old workflows → 99_ARCHIVE/deprecated_workflows/
- **Old Governance**: Previous versions → 99_ARCHIVE/superseded_governance/
- **Experiment Results**: Concluded experiments → 99_ARCHIVE/experimental_notes/
- **Historical Logs**: Old execution logs (1+ year old) → 99_ARCHIVE/historical_logs/

## Distinguishing Archived vs. Deleted

- **Archived**: Item is no longer active but has reference/historical value, stays in vault
- **Deleted**: Item has no value and is removed entirely (rare, requires escalation)

Most items should be archived, not deleted. Deletion is only appropriate for:
- Duplicate or erroneous captures
- Items created by mistake
- Temporary working notes of no lasting value

## Accessing Archived Items

Archived items are findable through:

- **Full-text search**: Obsidian search can find archived items (they're still in the vault)
- **Archive index**: An index file in 99_ARCHIVE lists all archived items
- **Dated subdirectories**: Items organized by archive date
- **Related links**: From active items referencing archived work

Archive is less discoverable than active layers by design—archived items should be consulted when needed for reference, not as primary sources.

## Learning from Archive

The archive is a learning resource. Periodically review archived items to:

- Understand why past patterns were retired
- Learn from past experiments (what worked, what didn't)
- Trace the evolution of governance and system design
- Inform future decisions with historical context

ARCHIVE preserves institutional knowledge that would otherwise be lost.
