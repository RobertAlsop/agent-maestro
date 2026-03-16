# The 6 shell scripts every large knowledge-vault builder eventually creates

These become extremely useful once vaults reach **hundreds or thousands of notes**.

---

# 1️⃣ Vault scaffold script

Purpose:

Create the architecture of a vault.

Example tasks:

- create folder hierarchy
    
- create maps
    
- create registries
    
- create template system
    
- create CLAUDE.md files
    

This is the script you just ran.

Typical command:

./vault_scaffold.sh

---

# 2️⃣ Vault inventory script

Purpose:

Generate a full structural report of the vault.

Example outputs:

file_inventory.txt  
folder_inventory.txt  
note_inventory.md

Useful for:

- audits
    
- refactors
    
- AI analysis
    

Example command:

./vault_inventory.sh

Example inside:

find . -type f > file_inventory.txt

---

# 3️⃣ Orphan note detector

Purpose:

Find notes **not linked from maps or registries**.

This is one of the most important vault maintenance scripts.

Example result:

Orphan notes:  
- marketing_strategy.md  
- midwife_pipeline.md

These are notes that **no navigation surface points to**.

Example command:

./find_orphans.sh

---

# 4️⃣ Bulk frontmatter installer

Purpose:

Add or normalize frontmatter across hundreds of notes.

Example:

Add this block:

type: concept  
status: draft

to all concept notes.

Example command:

./apply_frontmatter.sh

Useful when introducing **new metadata standards**.

---

# 5️⃣ Link repair / rename script

Purpose:

When you rename files or restructure folders, this script updates links.

Example:

Replace:

[[old_name]]

with

[[new_name]]

Example command:

./repair_links.sh

Very useful during **large vault refactors**.

---

# 6️⃣ Archive / cleanup script

Purpose:

Move obsolete or inactive notes automatically.

Example:

Move old logs to archive:

mv logs/* archive/logs/

Or archive completed projects.

Example command:

./vault_cleanup.sh

---

# What advanced vault builders eventually add

When vaults get very large, people add:

### semantic audit scripts

Example:

workflow_without_registry.txt  
schema_without_registry.txt  
duplicate_authority_notes.txt

These help detect structural drift.