# Template Ruleset

This is the ruleset I recommend using to generate and validate the 22 templates.

---

## Global Rules

### 1. All templates must use the locked master schema

Every template must use the same frontmatter field order and field names.

No template may:

- invent alternate field names
    
- omit core schema fields
    
- reorder fields arbitrarily
    

---

### 2. Relationships values must use stable note IDs

Inside `relationships`, values must always be stable IDs, not wiki links.

Correct:

relationships:  
  part_of:  
    - SYS.agent_ecosystem

Incorrect:

relationships:  
  part_of:  
    - "Agent Ecosystem]]"

---

### 3. Human navigation fields use wiki links

These fields remain human-facing and should use Obsidian links:

- `map`
    
- `maps`
    
- `related`
    
- `related_maps`
    
- `related_pipes`
    

Example:

map: "[[MAP.agent_ecosystem]]"  
maps:  
  - "[[MAP.agent_governance]]"

---

### 4. `map` / `maps` rule

This must be explicit across all templates:

- `map` = the **primary navigation map**
    
- `maps` = **additional associated maps**
    

If a note has only one map, use `map` and leave `maps: []`.

If it belongs to multiple maps, use:

- `map` for the primary one
    
- `maps` for the additional ones
    

---

### 5. Empty collections must always be explicit

Use empty lists, not nulls, for list-shaped fields.

Correct:

maps: []  
related: []  
supersedes: []  
superseded_by: []

This makes parsing predictable.

---

### 6. Required body structure rule

Every template must include:

- `# Purpose`
    
- `# Relationships`
    

And then the appropriate type-specific required section.

This is mandatory across the template set.

---

### 7. ID grammar rule

All IDs must follow:

PREFIX.identifier_name

Recommended prefixes:

- `CON.` concept
    
- `SYS.` system
    
- `MAP.` map
    
- `GOV.` governance
    
- `REG.` registry
    
- `DEC.` decision
    
- `PROJ.` project
    
- `PIPE.` pipeline
    
- `PROC.` process
    
- `PACK.` authority pack
    
- `PACKSEC.` authority pack section
    
- `REF.` reference
    
- `NS.` north star
    
- `PRN.` principles
    
- `MODE.` mode
    
- `SCOPE.` scope
    
- `STRAT.` strategy
    
- `ROAD.` roadmap
    
- `TAX.` taxonomy
    
- `IDX.` index
    

---

### 8. Schema version rule

All templates in this set use:

schema_version: 2

---

### 9. `canonical` and `authority_weight` are both required

These fields are never omitted.

Reason:

- `canonical` = resolution status
    
- `authority_weight` = authority strength
    

Both are needed.

---

### 10. `owner` is optional in meaning, but present in schema

The field should appear in every template, even if blank.

This keeps the schema shape stable.

---

# Controlled Vocabulary Rules

## `note_class`

Allowed values:

doctrine
governance
architecture
navigation
execution
registry
reference
knowledge
classification

## `layer`

Allowed values:

knowledge  
governance  
maps  
systems  
pipes  
execution  
registry

## `status`

Allowed values:

draft  
active  
paused  
deprecated  
archived

## `review_status`

Allowed values:

draft  
in_review  
approved  
superseded  
archived

## `resolution_basis`

Allowed values:

canonical  
authority_weight  
registry_reference  
recency  
manual_override

## `source_type`

Allowed values:

human_authored  
ai_authored  
ai_transformed  
imported  
generated  
compiled

## `review_cycle`

Allowed values:

none  
monthly  
quarterly  
biannual  
annual  
event_driven

---

# Template-by-Template Rules

## 1. Concept Template

- `type`: `concept`

- `note_class`: `knowledge`

- `layer`: `knowledge`
    
- required section: `# Definition`
    
- typical authority: `60`
    
- default resolution: `authority_weight`
    

---

## 2. Reference Template

- `type`: `reference`
    
- `note_class`: `reference`
    
- `layer`: `knowledge`
    
- required section: `# Summary`
    
- authority: `90`
    
- default resolution: `authority_weight`
    

---

## 3. Principles Template

- `type`: `principles`
    
- `note_class`: `doctrine`
    
- `layer`: `governance`
    
- required section: `# Principles`
    
- authority: `90`
    
- default resolution: `canonical`
    

---

## 4. North Star Template

- `type`: `north_star`
    
- `note_class`: `doctrine`
    
- `layer`: `governance`
    
- required section: `# Definition`
    
- authority: `90`
    
- default resolution: `canonical`
    

---

## 5. Modes Template

- `type`: `modes`
    
- `note_class`: `doctrine`
    
- `layer`: `governance`
    
- required section: `# Modes`
    
- authority: `90`
    
- default resolution: `canonical`
    

---

## 6. Governance Template

- `type`: `governance`
    
- `note_class`: `governance`
    
- `layer`: `governance`
    
- required section: `# Policy`
    
- authority: `92`
    
- default resolution: `canonical`
    

Use for:

- policies
    
- charters
    
- governance models
    
- escalation rules
    
- access rules
    
- control documents
    

Not for:

- north stars
    
- principles
    
- modes
    

---

## 7. Decision Template

- `type`: `decision`
    
- `note_class`: `governance`
    
- `layer`: `governance`
    
- required section: `# Decision`
    
- authority: `65`
    
- default resolution: `authority_weight`
    

---

## 8. Map Template

- `type`: `map`

- `note_class`: `navigation`

- `layer`: `maps`

- required section: `# Map`

- authority: `85`

- default resolution: `authority_weight`
    

---

## 9. System Map Template

- `type`: `system_map`

- `note_class`: `architecture`

- `layer`: `maps`

- required section: `# System Map`

- authority: `85`

- default resolution: `authority_weight`
    

Use specifically for:

- architecture maps
    
- component maps
    
- relationship maps
    
- inheritance maps
    

---

## 10. Taxonomy Template

- `type`: `taxonomy`

- `note_class`: `classification`

- `layer`: `maps`
    
- required section: `# Structure`
    
- authority: `85`
    
- default resolution: `authority_weight`
    

---

## 11. Index Template

- `type`: `index`
    
- `note_class`: `navigation`
    
- `layer`: `maps`
    
- required section: `# Index`
    
- authority: `85`
    
- default resolution: `authority_weight`
    

---

## 12. System Template

- `type`: `system`
    
- `note_class`: `architecture`
    
- `layer`: `systems`
    
- required section: `# Responsibilities`
    
- authority: `60`
    
- default resolution: `authority_weight`
    

---

## 13. System Registry Template

- `type`: `system_registry`

- `note_class`: `registry`

- `layer`: `registry`

- required section: `# Entries`

- authority: `95`

- default resolution: `canonical`
    

---

## 14. Registry Template

- `type`: `registry`

- `note_class`: `registry`

- `layer`: `registry`

- required section: `# Entries`

- authority: `95`

- default resolution: `canonical`
    

---

## 15. Pipeline Template

- `type`: `pipeline`

- `note_class`: `execution`

- `layer`: `pipes`
    
- required section: `# Stages`
    
- authority: `60`
    
- default resolution: `authority_weight`
    

---

## 16. Process Template

- `type`: `process`
    
- `note_class`: `execution`
    
- `layer`: `pipes`
    
- required section: `# Steps`
    
- authority: `60`
    
- default resolution: `authority_weight`
    

---

## 17. Project Template

- `type`: `project`
    
- `note_class`: `execution`
    
- `layer`: `execution`
    
- required section: `# Scope`
    
- authority: `60`
    
- default resolution: `authority_weight`
    

---

## 18. Authority Pack Template

- `type`: `authority_pack`

- `note_class`: `governance`

- `layer`: `systems`
    
- required section: `# Pack Definition`
    
- authority: `80`
    
- default resolution: `authority_weight`
    

---

## 19. Authority Pack Section Template

- `type`: `authority_pack_section`

- `note_class`: `governance`

- `layer`: `systems`
    
- required section: `# Section Definition`
    
- authority: `70`
    
- default resolution: `authority_weight`
    

---

## 20. Scope Template

- `type`: `scope`
    
- `note_class`: `governance`
    
- `layer`: `governance`
    
- required section: `# Scope Definition`
    
- authority: `65`
    
- default resolution: `authority_weight`
    

---

## 21. Strategy Template

- `type`: `strategy`
    
- `note_class`: `governance`
    
- `layer`: `governance`
    
- required section: `# Strategic Direction`
    
- authority: `65`
    
- default resolution: `authority_weight`
    

---

## 22. Roadmap Template

- `type`: `roadmap`
    
- `note_class`: `execution`
    
- `layer`: `execution`
    
- required section: `# Roadmap`
    
- authority: `65`
    
- default resolution: `authority_weight`
    

---

# Optional field guidance by template type

## Strongly recommended to populate

### Governance, registry, roadmap, strategy, map, system_map

- `last_reviewed`
    
- `review_cycle`
    
- `owner`
    

## Often useful

### Decision, project, pipeline, process, authority pack

- `owner`
    
- `last_reviewed`
    

## Usually optional

### Concept, reference, taxonomy, index

- `owner`
    
- `review_cycle`
    

---

# Required body skeleton rule

Every template must contain these headings in this order:

# Purpose  
  
# Relationships  
  
# [Type-Specific Section]

Optional extra sections may follow, but these required sections must appear first and in this order.