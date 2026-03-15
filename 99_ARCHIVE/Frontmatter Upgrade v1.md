# Prompt for Claude Co-Work — Agent Maestro Frontmatter Upgrade

We are now going to perform a **vault-wide frontmatter upgrade** across the notes in the **Agent Maestro** folder inside my Obsidian vault.

Target scope:

`/Users/robertalsop/obsidian/`

Focus only on the **Agent Maestro folder and all notes within it**.

The templates have already been updated.  
Your role is **not** to update templates.  
Your role is to update the **frontmatter of the existing notes** in Agent Maestro.

This is a **frontmatter migration only** unless a note requires a minimal YAML repair.

Do not rewrite note bodies.  
Do not change note meaning.  
Do not introduce structural drift.

---

## Objective

Upgrade the Agent Maestro notes to the new standard:

**Frontmatter v2 — Authority + Graph Relationships**

The purpose of this upgrade is to make the vault function as:

- Obsidian notes
    
- plus explicit machine-readable knowledge graph
    
- plus deterministic authority layer
    

This should improve AI reasoning, graph traversal, inheritance tracing, registry logic, and pack compilation.

---

## Step 1 — Output the migration plan

First, output:

# Agent Maestro Frontmatter Upgrade Plan

The plan must include:

- which folders inside Agent Maestro will be touched
    
- which note families or note types are present
    
- which frontmatter patterns currently exist
    
- what upgrade actions will be applied to each note family
    
- any likely YAML inconsistencies or edge cases
    
- any notes that may require manual review
    
- how canonical defaults and authority weights will be assigned
    
- how relationship fields will be handled when targets are unknown
    

For the plan, also include the migration rules you intend to follow for:

- field placement
    
- canonical assignment
    
- authority weight defaults
    
- relationships block insertion
    
- preservation of existing `related`, `map`, `maps`, `related_maps`, and `related_pipes` fields
    
- ID-only relationship values
    
- non-destructive editing
    

Do **not** modify any files in Step 1.

---

## Step 2 — Wait for approval

After outputting the plan, stop and wait for approval.

Do not begin editing notes until the plan is approved.

---

## Step 3 — Execute the migration exactly according to the approved plan

Once approved, update the notes directly in the Agent Maestro folder.

Work carefully and conservatively.

No structural changes are allowed during the migration unless explicitly approved.

---

## New Frontmatter Standard

Add the following fields to relevant notes:

canonical: true | false  
authority_weight: 0-100  
relationships:  
  defines:  
  part_of:  
  implements:  
  governs:  
  inherits_from:  
  applies_to:  
  uses:  
  produces:

---

## Placement Rule

Insert the new fields:

- **after `version` if `version` exists**
    
- otherwise **after `status`**
    
- and always **before `created` / `updated`**
    

Preserve all other frontmatter fields.

Do not reorder unrelated fields unless needed to apply this rule cleanly.

---

## Relationship Rule

Keep all existing human-readable navigation fields exactly as they are, including:

- `related`
    
- `related_maps`
    
- `related_pipes`
    
- `map`
    
- `maps`
    

These remain the **human-readable / Obsidian-native layer**.

The new `relationships` block is the **machine-readable layer**.

Both layers must coexist.

---

## Critical ID Rule

All values inside `relationships` must use **stable note IDs only**.

Use IDs such as:

relationships:  
  part_of:  
    - SYS.agent_ecosystem

Do not use:

- wiki-links
    
- note titles
    
- filenames
    

If the correct target ID is unknown, leave the relationship empty rather than guessing.

Be conservative.

---

## Authority Rule

Use these defaults unless a note clearly requires a different value.

### Set `canonical: true` for:

- maps
    
- registries
    
- references
    
- taxonomies
    
- principle sets
    
- north stars
    
- official indexes
    
- canonical root architecture notes
    
- operating control notes
    

### Set `canonical: false` for:

- sections
    
- drafts
    
- exploratory notes
    
- non-root implementation notes
    
- temporary notes
    
- ordinary projects unless clearly canonical
    
- decision notes unless they define canonical policy
    

### Suggested `authority_weight` defaults

- `100` system registries / operating control notes
    
- `95` canonical registries
    
- `90` core references / base doctrine
    
- `85` maps / taxonomies / indexes / canonical architecture notes
    
- `80` authority packs
    
- `70` authority pack sections
    
- `60` standard systems / processes / decisions / projects
    
- `<60` experiments / temporary overrides / exploratory material
    

Use consistent judgment across the folder.

---

## Non-Destructive Editing Rule

This is a **non-destructive migration**.

Preserve:

- note titles
    
- note bodies
    
- existing prose
    
- current meaning
    
- existing human-facing link fields
    
- existing tags
    
- existing IDs
    
- existing timestamps unless updating `updated` is appropriate within the vault standard
    
- existing domain / type / layer semantics
    

Do not rewrite notes for style.

Do not expand notes.

Do not compress notes.

Do not “improve” the body text.

Only upgrade frontmatter.

---

## YAML Cleanliness Rule

Ensure all edited frontmatter is valid YAML.

That means:

- correct indentation
    
- clean list formatting
    
- no malformed mixed syntax
    
- no guessed values when confidence is low
    

Preferred empty structure:

relationships:  
  defines:  
  part_of:  
  implements:  
  governs:  
  inherits_from:  
  applies_to:  
  uses:  
  produces:

If a relationship is confidently known, populate it using IDs only.

Otherwise leave it blank.

---

## Handling Existing Fields

If a note already contains fields such as `inherits_from`, preserve them exactly as they are.

Do not collapse existing fields into `relationships`.

The existing fields remain note-specific metadata.  
The new `relationships` block is the general graph layer.

---

## Editing Philosophy

Short, precise, and safe changes are better than ambitious edits.

When uncertain:

- preserve existing data
    
- add the new structure conservatively
    
- leave relationship values blank rather than speculating
    

The goal is to make the vault more machine-readable **without destabilizing it**.

---

## Final Goal

After this migration, the Agent Maestro folder should behave less like a collection of markdown notes and more like a:

- governed knowledge graph
    
- deterministic authority system
    
- AI-operable architecture layer
    

Follow the approved plan strictly.