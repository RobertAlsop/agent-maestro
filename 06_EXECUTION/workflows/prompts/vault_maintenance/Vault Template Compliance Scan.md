---
id: EXE.workflow.maint.vault_template_compliance
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

## Agent Maestro — Vault Template Compliance Scan

You are performing a **Template Compliance Scan** of the AGENT_MAESTRO vault.

The purpose of this scan is to ensure that **every note in the vault conforms to the canonical frontmatter schema and the governing note templates.**

This scan acts as a **structural grammar check** for the vault.

---

# Scope

Scan the entire folder:

AGENT_MAESTRO/

This includes all subfolders and all markdown notes.

Exclude:

99_ARCHIVE/ and 01_CAPTURE/

---

# Canonical Sources

The following are the authoritative references:

1. **Frontmatter Schema**
    
2. **Template Registry**
	
3. **Note Templates**
    
4. **Template Mapping**
    

These are located in:

OBSIDIAN/88_templates/notes/

Treat these as **canonical definitions of vault structure**.

---

# Goal

Ensure that every note in the Agent Maestro system:

- Uses the **correct template**
    
- Conforms to the **frontmatter schema**
    
- Uses **valid field names**
    
- Contains **required fields**
    
- Uses **correct structural nesting**
    
- Does not contain **unknown fields**
    

---

# Compliance Rules

For each note:

1. Parse the **frontmatter block**.
    
2. Identify the note’s **type / note_class**.
    
3. Determine the **governing template** using the Template Mapping.
    
4. Compare the note’s frontmatter against:
    

- the **frontmatter schema**
    
- the **canonical template structure**
    

---

# Detect the Following Violations

### Schema Violations

- Missing required fields
    
- Unknown fields not defined in the schema
    
- Incorrect nesting structures
    
- Invalid data types
    

---

### Template Violations

- Missing template fields
    
- Incorrect template layout
    
- Incorrect template for the note type
    
- Fields appearing in the wrong sections
    

---

### Structural Violations

- Missing frontmatter block
    
- Duplicate frontmatter keys
    
- Improper YAML formatting
    

---

### Governance Violations

- Invalid `type`
    
- Invalid `note_class`
    
- Conflicting classification values
    

---

# Special Checks

Also detect:

### Schema Version Drift

If `schema_version` exists:

- Ensure it matches the canonical schema version.
    

---

### Authority Violations

Ensure that fields intended only for certain note classes are **not used in inappropriate note types**.

---

# Output Format

Produce a **Template Compliance Report** with the following sections.

---

# 1. Scan Summary

- Total notes scanned
    
- Total compliant notes
    
- Total non-compliant notes
    
- Compliance percentage
    

---

# 2. Schema Violations

List notes that violate the frontmatter schema.

For each note include:

- file path
    
- violation type
    
- incorrect field
    
- recommended correction
    

---

# 3. Template Violations

List notes that do not match their governing template.

Include:

- note path
    
- expected template
    
- detected issue
    

---

# 4. Structural Violations

List notes with:

- malformed frontmatter
    
- duplicate keys
    
- YAML errors
    

---

# 5. Classification Violations

List notes with:

- invalid `type`
    
- invalid `note_class`
    
- inconsistent classification fields
    

---

# 6. Schema Version Drift

List notes using incorrect schema versions.

---

# 7. Unknown Fields

List all fields present in notes that **do not exist in the canonical schema**.

---

# 8. System Integrity Assessment

Provide a brief evaluation of:

- vault structural health
    
- template compliance quality
    
- systemic structural risks
    

---

# Important Constraints

You are **scanning and reporting only**.

Do **NOT**:

- modify notes
    
- change frontmatter
    
- rewrite files
    
- rename files
    

This scan is **diagnostic only**.

---

# Final Output

Produce:

1. **Template Compliance Report**
    
2. **List of notes requiring repair**
    
3. **Summary of systemic issues**
    

This report will later be used to perform a **controlled vault repair operation**.