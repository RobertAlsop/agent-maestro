---
id: EXE.workflow.maint.audit_cross_folder_links
type: process
note_class: execution
layer: pipes
canonical: false
authority_weight: 60
resolution_basis: canonical
schema_version: 2
status: active
review_status: approved
version: 1
source_type: human_authored
domain: execution
scope: null
created: null
updated: null
last_reviewed: null
review_cycle: quarterly
owner: AgentMaestro
map: null
related: []
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
maps: []
related_maps: []
related_pipes: []
supersedes: []
superseded_by: []
---

Audit the Agent-Maestro folder for unintended cross-folder links.

Check for:

1. Duplicate note names that also exist in the Bartram folder.
2. Links from Agent-Maestro notes to Bartram notes that are likely accidental.
3. Maps that reference notes outside Agent-Maestro.

Produce a report listing:

• duplicate note names
• cross-folder links detected
• whether each link appears intentional or accidental
• recommended fixes

Do not modify files.