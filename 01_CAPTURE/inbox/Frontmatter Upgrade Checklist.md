Here’s a **very quick 5-check validation checklist** after Claude finishes the migration:

### 1️⃣ YAML validity

Open a few edited notes and confirm:

- frontmatter begins and ends with `---`
    
- indentation is consistent (2 spaces)
    
- no tabs or mixed indentation
    

### 2️⃣ Field placement rule

Check that the new fields appear in the correct location:

status  
version (if present)  
  
canonical  
authority_weight  
relationships  
  
created / updated

### 3️⃣ Relationship structure

Confirm every note contains:

relationships:  
  defines:  
  part_of:  
  implements:  
  governs:  
  inherits_from:  
  applies_to:  
  uses:  
  produces:

No wiki-links inside these lists — **IDs only**.

### 4️⃣ Required sections in body

Verify each note contains:

- **Purpose**
    
- **Relationships**
    
- **Definition OR Responsibilities**
    

(no template missing these).

### 5️⃣ Obsidian loads the vault cleanly

Open the vault and quickly check:

- no YAML parsing warnings
    
- graph view still renders normally
    
- internal links still resolve.
    

If all five pass, the **migration is structurally safe**.