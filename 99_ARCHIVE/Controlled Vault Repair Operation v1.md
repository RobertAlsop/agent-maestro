# Controlled Vault Repair Operation

You are performing a **controlled structural repair operation** on the AGENT_MAESTRO vault.

A **Vault Template Compliance Scan has already been completed**, and a **Template Compliance Report** has been generated.

Your task is to **repair structural violations safely and deterministically** so that every note conforms to:

- the **canonical frontmatter schema**
    
- the **governing note templates**
	
- **the template registry**
    
- the **template mapping system**
    

---

# Scope

Repair notes within:

AGENT_MAESTRO/

Process all markdown notes recursively.

Exclude:

99_ARCHIVE/ and 01_CAPTURE/

if present.

---

# Canonical Sources

The following documents are authoritative:

OBSIDIAN/88_templates/notes

Specifically:

- Frontmatter Schema
    
- Note Templates
	
- Template Registry
    
- Template Mapping
    

These define the **structural grammar of the vault**.

If a note conflicts with these sources, **the canonical sources always win**.

---

# Repair Goals

Ensure every note:

- uses the **correct template**
    
- conforms to the **frontmatter schema**
    
- contains **all required fields**
    
- contains **no unknown fields**
    
- uses **correct field nesting**
    
- uses **valid YAML structure**
    

---

# Repair Procedure

For each non-compliant note identified in the **Template Compliance Report**:

### 1. Identify Governing Template

Determine the correct template using:

type  
note_class

and the **Template Mapping**.

---

### 2. Repair Frontmatter

Modify the frontmatter to match the canonical template:

#### Add Missing Fields

Insert any required fields that are absent.

Use default values if defined in the template.

---

#### Remove Unknown Fields

Remove fields that do not exist in the canonical schema.

---

#### Correct Field Structure

Fix:

- incorrect nesting
    
- wrong field placement
    
- malformed YAML
    

---

#### Correct Classification

If `type` or `note_class` are invalid:

- correct them if obvious
    
- otherwise flag the note for manual review
    

---

### 3. Preserve Note Content

You must **never modify the body content of the note** unless the template explicitly requires structural headings.

Focus on **frontmatter repair only**.

---

### 4. Preserve Existing Valid Data

If a field exists and:

- matches the schema
    
- has valid data
    

then **retain the existing value**.

Do not overwrite valid metadata.

---

### 5. Schema Version

Ensure:

schema_version

matches the canonical schema version.

Update if necessary.

---

# Edge Cases

If a note cannot be safely repaired because:

- its classification is ambiguous
    
- the governing template cannot be determined
    

then:

- **do not modify the note**
    
- add it to the **Manual Review List**
    

---

# Output Requirements

Produce a **Vault Repair Report** containing:

---

## 1. Repair Summary

- total notes processed
    
- notes repaired
    
- notes already compliant
    
- notes requiring manual review
    

---

## 2. Repaired Notes

For each repaired note list:

- file path
    
- fields added
    
- fields removed
    
- fields corrected
    

---

## 3. Manual Review List

List notes that could not be safely repaired.

Include the reason.

---

## 4. Structural Integrity Assessment

Provide a short assessment of:

- vault structural health
    
- template compliance status
    
- remaining risks
    

---

# Safety Constraints

You must **not**:

- rename files
    
- move files
    
- change note content
    
- rewrite notes
    

Only repair **frontmatter structure and template alignment**.

---

# Final Goal

At the end of this repair operation, the Agent Maestro vault should function as a **fully deterministic knowledge system** where:

- every note conforms to the canonical schema
    
- every note follows a valid template
    
- the vault structure remains stable and machine-readable.