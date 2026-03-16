---
type: process
note_class: execution
layer: pipes
canonical: false
authority_weight: 60
resolution_basis: canonical
schema_version: 2
title: "Filename Refactor"
status: active
review_status: approved
version: 1
source_type: human_authored
domain: execution
created_date: ""
last_modified: ""
owner: AgentMaestro
tags: []
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []
hash: ''
supersedes: []
superseded_by: []
---

We need to perform a filename refactor only within the Agent Maestro folder.

Scope:
This refactor applies only to the `Agent-Maestro/` folder and its subfolders.

The following folders must NOT be refactored:
- `01_CAPTURE/`
- `99_ARCHIVE/`

Current situation:
The body title inside each note is already correct and human-readable.
The problem is only that many filenames were generated from the canonical ID instead of the human-facing title.

Desired convention:
- The canonical ID remains in frontmatter and must NEVER change.
- The existing human-readable body title should become the filename.
- The body content itself should remain unchanged.

Example:

Before:
filename:
CON.agent.md

frontmatter:

body:
# Agent

After:
filename:
Agent.md

frontmatter:

body:
# Agent

Rules:

1. Do NOT change the `id` field in frontmatter.
2. Do NOT change the body title / H1 if it is already correct.
3. Rename each file to match the existing human-readable title in the body.
4. Update internal links across the vault so that all links remain valid after renaming.
5. Do NOT change folder structure.
6. Do NOT modify authority pack grammar filenames (`00_identity.md`, `01_scope.md`, etc.) — those filenames must remain unchanged.
7. Do NOT rewrite note content unless needed only to preserve valid internal links after rename.

Goal:
After the refactor:
- filenames are human-readable
- IDs remain stable in frontmatter
- body titles remain unchanged
- all links still resolve correctly

Before making any changes, output a short refactor plan listing:
- number of files to rename
- 10 example filename transformations
- confirmation that authority pack grammar files will be excluded

Wait for approval before executing.