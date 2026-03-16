
## System-wide frontmatter upgrade rule

Apply this to **all templates already in sources** and to the six templates created in this chat.

### New fields added

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

### Placement rule

Insert these fields **after `version` when present**, or **after `status` if there is no `version`**, and before `created` / `updated`.

### Relationship rule

Keep all existing `related`, `related_maps`, `related_pipes`, `maps`, and `map` fields exactly as they are for human navigation and backward compatibility.

The new `relationships` block is the **machine-readable layer**.  
The old link fields remain the **human-readable / Obsidian-native layer**.

### Authority rule

Recommended defaults:

- `canonical: true` for maps, registries, references, taxonomies, principle sets, north stars, official indexes
    
- `canonical: false` for sections, drafts, exploratory notes, non-root implementation notes
    

Suggested `authority_weight` defaults:

- `100` system registries / operating control notes
    
- `95` canonical registries
    
- `90` core references / base doctrine
    
- `85` maps / taxonomies / indexes
    
- `80` authority packs
    
- `70` authority pack sections
    
- `60` standard systems / processes
    
- `<60` experiments / temporary overrides
    

## The six templates re-output in full with upgraded frontmatter

Below, the **body remains verbatim** from the templates I output earlier in this chat. Only the frontmatter has been upgraded.


___
# How This Applies to Existing Vault Templates

All templates in the sources now gain **three additional sections**:

### Added fields

canonical:  
authority_weight:  
relationships:

They appear **after `version` or `status`** and before timestamps.

Example applied to an existing template:

status: active  
version: 1  
  
canonical: true  
authority_weight: 90  
  
relationships:  
  
  defines:  
  
  part_of:  
  
  governs:

Everything else remains unchanged.

---

# 9. Short Summary of the Frontmatter Upgrade

You can store this as a **vault migration note**.

### Upgrade Name

**Frontmatter v2 — Authority + Graph Relationships**

### Changes Introduced

1️⃣ **Authority Metadata**

canonical  
authority_weight

Purpose:

- deterministic authority resolution
    
- pack compilation
    
- schema validation
    

---

2️⃣ **Structured Knowledge Graph**

relationships:

With typed edges:

defines  
part_of  
implements  
governs  
inherits_from  
applies_to  
uses  
produces

---

3️⃣ **Machine-Readable Graph**

Notes now function as:

Obsidian documents  
+  
explicit knowledge graph

This enables AI agents to:

- traverse system architecture
    
- trace authority inheritance
    
- map systems → packs → agents
    
- reason deterministically over the vault.