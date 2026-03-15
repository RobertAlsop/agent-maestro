---
type: process
note_class: execution
layer: pipes
canonical: false
authority_weight: 60
resolution_basis: canonical
schema_version: 2
title: "Process Unprocessed Notes Into The Vault"
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

You are processing notes located in:

01_CAPTURE/unprocessed/

These notes are ready to enter the Agent Maestro vault but are currently unstructured.

Your job is to transform them into properly formatted vault notes and prepare them for placement in the correct location within the vault.

--------------------------------------------------

GOAL

Convert each note in `01_CAPTURE/unprocessed/` into a valid vault note that:

• uses the correct master template  
• contains proper frontmatter  
• fits the Agent Maestro ontology  
• is ready to move into the correct folder

The notes should become first-class citizens of the vault.

--------------------------------------------------

TEMPLATES

Templates are located here:

99_templates/notes/master_notes/

Select the appropriate template based on the type of note.

Typical template types include:

Concept  
Domain  
Pattern  
System  
Process  
Project  
Governance  

Do NOT invent new template structures.

If a note does not clearly match an existing template, flag it in the report instead of forcing it into a template.

--------------------------------------------------

PROCESS

For each note in `01_CAPTURE/unprocessed/`:

1. Read the note carefully.

2. Determine the correct note type:
   - Concept
   - Domain
   - Pattern
   - System
   - Pipeline / Process
   - Project
   - Governance
   - Reference

3. Select the corresponding template.

4. Reformat the note to match the template structure.

This includes:

• adding correct frontmatter  
• assigning a canonical ID  
• adding a clean H1 title  
• structuring sections according to the template

5. Perform a light knowledge upgrade.

This includes:

• strengthening the definition  
• clarifying scope  
• removing vague language  
• keeping the note concise

Do NOT expand excessively.

Target note size:
150–400 words.

--------------------------------------------------

ONTOLOGY ALIGNMENT

Ensure the note aligns with the existing ontology.

Check:

• definitions do not contradict existing concepts  
• terminology matches the vault vocabulary  
• concept boundaries remain clear

Add internal links where appropriate.

Prefer linking to:

• concept notes  
• pattern notes  
• system notes  
• maps

Do NOT over-link.

--------------------------------------------------

MAP INTEGRATION

Ensure the note links to at least one canonical map.

Possible maps include:

MAP.agent_maestro.domain  
MAP.agent_maestro.concepts  
MAP.agent_maestro.systems  
MAP.agent_maestro.pipelines  
MAP.agent_maestro.projects  

Or subsystem maps such as:

MAP.authority.architecture  
MAP.memory.architecture  
MAP.operational.intelligence  

--------------------------------------------------

PLACEMENT

Determine the correct destination folder for the note.

Possible locations include:

02_KNOWLEDGE/concepts  
02_KNOWLEDGE/domains  
02_KNOWLEDGE/patterns  
05_SYSTEMS  
03_PIPELINES  
04_PROJECTS  

Do NOT move files automatically.

Instead, report the recommended location.

--------------------------------------------------

OUTPUT PROCESS

Step 1

Scan the `01_CAPTURE/unprocessed/` folder and produce a report listing:

• number of notes detected  
• proposed note type for each note  
• template to apply  
• suggested destination folder

Wait for approval.

--------------------------------------------------

Step 2

After approval, produce the upgraded and templated versions of the notes.

For each note include:

• the full rewritten note  
• the applied template  
• the assigned ID  
• the recommended destination folder

--------------------------------------------------

IMPORTANT RULES

Do NOT modify files in the vault yet.

Do NOT invent new ontology layers.

Do NOT rename core concepts.

Only prepare the notes so they can safely enter the vault.

--------------------------------------------------

QUALITY STANDARD

Write like an editor of a technical discipline.

Definitions should be precise and operational.

Notes should feel like entries in a structured knowledge system, not essays.