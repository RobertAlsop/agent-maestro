---
type: process
note_class: execution
layer: pipes
canonical: false
authority_weight: 60
resolution_basis: canonical
schema_version: 2
title: "Vault Integrity & Self-Healing Audit v2"
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

# Vault Integrity & Self-Healing Audit

You are performing a structural and ontological integrity audit of the Agent Maestro Obsidian vault.

Goal:  
Ensure the vault remains a coherent operational knowledge system over time.

The vault should function as a stable ontology for the Agent Maestro discipline, where concepts, systems, patterns, pipelines, and projects remain clearly defined and correctly linked.

You will scan the entire `Agent-Maestro/` folder and generate a structured repair report.

IMPORTANT:  
You are auditing the system, not rewriting it.

Do NOT modify files.  
Do NOT rename notes.  
Do NOT change frontmatter.  
Do NOT invent new concepts.

Only detect problems and propose improvements.

---

# AREAS TO AUDIT

---

## 1. ORPHAN NOTES

Detect notes that are not reachable from any canonical map.

Definition:  
A note is considered orphaned if it has no incoming links from maps or other core notes.

For each orphan note report:

- note name
    
- folder
    
- suggested map where it should appear
    

---

## 2. WEAKLY CONNECTED NOTES

Detect notes with poor connectivity.

Heuristic:

- fewer than 2 meaningful internal links
    
- no links to concepts, patterns, or systems
    

For each weak note report:

- note name
    
- number of links
    
- suggested link improvements
    

---

## 3. MAP COVERAGE

Verify that every core note appears in at least one canonical map.

Maps include:

MAP.agent_maestro.domain  
MAP.agent_maestro.governance  
MAP.agent_maestro.concepts  
MAP.agent_maestro.systems  
MAP.agent_maestro.pipelines  
MAP.agent_maestro.projects

MAP.authority.architecture  
MAP.memory.architecture  
MAP.operational.intelligence

Report:

- notes missing from maps
    
- maps that appear incomplete
    
- notes that should be added to maps
    

---

## 4. ONTOLOGY COLLISIONS

Detect overlapping concepts.

Example signals:

- two notes defining the same concept
    
- definitions that significantly overlap
    
- competing terminology for the same idea
    

For each collision report:

- note A
    
- note B
    
- nature of overlap
    
- recommended resolution
    

Possible resolutions:

- merge
    
- redefine boundaries
    
- convert one to pattern or example
    

---

## 5. DEFINITION WEAKNESS

Identify notes where the opening definition is unclear.

Symptoms:

- definition missing
    
- definition longer than necessary
    
- vague language
    
- circular definitions
    

Report:

- note
    
- problem
    
- improved definition suggestion
    

---

## 6. LINK ARCHITECTURE

Evaluate link quality across the vault.

Look for:

- missing links between related concepts
    
- concept notes not linking to systems
    
- system notes not linking to concepts
    
- patterns not linked to systems
    

Suggest improvements.

Do NOT add links automatically — only recommend.

---

## 7. NOTE SIZE HEALTH

Detect notes that are either:

Too small

- less than ~80 words
    
- definition incomplete
    

Too large

- over ~600 words
    
- multiple concepts inside one note
    

Suggest whether to:

- expand
    
- split
    
- leave unchanged
    

---

## 8. MAP STRUCTURE

Evaluate map hierarchy.

Look for:

- maps with too many items
    
- maps missing key notes
    
- maps that should reference other maps
    

Recommend improvements if necessary.

---

## 9. AUTHORITY PACK ISOLATION

Authority pack grammar files are implementation artifacts.

Location:

05_SYSTEMS/authority_architecture/packs/

Rules:

Do NOT recommend renaming them.  
Do NOT recommend restructuring them.

Only check whether the authority architecture maps correctly reference the packs.

---

## 10. FRONTMATTER INTEGRITY

Verify that each note contains the required frontmatter fields defined by the vault schema.

Required fields include:

- id
    
- type
    
- canonical
    
- authority_weight
    
- resolution_basis
    
- relationships
    
- map
    
- status
    
- version
    

Detect:

- notes missing required fields
    
- malformed YAML
    
- fields with invalid structure
    

Report:

- note name
    
- missing or malformed fields
    
- recommended correction
    

Do NOT modify the note.

---

## 11. TEMPLATE COMPLIANCE

Verify that each note follows the correct template structure according to its `type`.

Example expectations:

Concept notes should contain:

- Purpose
    
- Context
    
- Relationships
    
- Definition
    

System notes should contain:

- Purpose
    
- Context
    
- Relationships
    
- Responsibilities
    

Pipeline notes should contain:

- Purpose
    
- Context
    
- Relationships
    
- Stages
    

Detect:

- notes missing required sections
    
- notes using the wrong structural template
    

Report:

- note name
    
- detected template mismatch
    
- missing sections
    

---

## 12. STRUCTURAL PARENT RULE

The vault enforces a single structural parent rule.

Each note must have exactly one structural parent defined in frontmatter:


Detect:

- notes missing a map field
    
- notes referencing multiple structural parents
    
- notes referencing non-existent maps
    

Report:

- note name
    
- detected issue
    
- suggested parent map
    

---

# OUTPUT FORMAT

Produce a structured report:

---

AGENT MAESTRO VAULT HEALTH REPORT

---

1. Structural Issues
    

- orphan notes
    
- weak connectivity
    

2. Ontology Issues
    

- duplicate concepts
    
- conflicting definitions
    

3. Link Improvements
    

- recommended new links
    

4. Map Coverage
    

- missing map references
    

5. Definition Improvements
    

- notes needing definition strengthening
    

6. Note Size Issues
    

- overly large notes
    
- underdeveloped notes
    

7. Map Structure Suggestions
    
8. Frontmatter Integrity Issues
    
9. Template Compliance Issues
    
10. Structural Parent Violations
    

---

IMPORTANT

The goal is to keep the vault healthy over time.

Only propose improvements that strengthen the existing ontology.

Do not introduce new conceptual layers unless absolutely necessary.

This audit should help maintain the vault as a coherent operational intelligence knowledge system.