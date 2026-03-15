# 01_CAPTURE

**Foundations Alignment**: This directory supports Law 2 (all actions must be verifiable) by serving as the capture point for raw observations and untrusted input before validation.

## Purpose

The CAPTURE layer is the vault's inbox for raw, unsorted input. This is where observations, drafts, rough notes, and captured context live before they are processed, validated, and promoted to canonical knowledge or operational records.

CAPTURE contains two subdirectories:
- **inbox**: Primary capture space for incoming observations and contexts
- **unprocessed**: Items that have been triaged but not yet moved to their canonical locations

This layer prioritizes capture speed and flexibility over formal structure. Governance constraints are minimal here.

## Conventions

- Naming: Use descriptive titles that capture the essence of the input
- Frontmatter: Not required (this is a drafting space), but titles should be clear
- Organization: Group related captures by theme or context, but avoid deep hierarchies
- Linking: Loose wiki-links are acceptable; full relationship frontmatter is not required

## Agent Rules

**Agents MAY**:
- Add new capture notes freely without approval
- Create subdirectories within inbox/ and unprocessed/ as needed
- Use this space to draft observations, questions, and preliminary ideas
- Link between captures and to 02_KNOWLEDGE notes

**Agents MUST NOT**:
- Delete or modify existing captures without explicit escalation to a human
- Assume captures are validated or canonical (they are working drafts)
- Move items between 01_CAPTURE and other layers without escalation (this is promotion, not capture)

**Escalation Required**:
- Deletion or modification of captures
- Decisions about what should be captured vs. what should be archived

## Key Files & Folders

- **inbox/**: Primary capture space for incoming observations and contexts
- **unprocessed/**: Triaged but not yet processed items awaiting promotion or archival

## Relationship to Other Layers

Items in CAPTURE flow "downstream" to other layers:
- Validated captures → 02_KNOWLEDGE
- Operational observations → 06_EXECUTION
- Project-related items → 04_PROJECTS
- System-related items → 05_SYSTEMS

The key principle: **Always capture first, validate second.** Do not let governance constraints prevent capture.
