# Frontmatter Schema v1

This is the canonical frontmatter schema for all notes in the Agent Maestro vault.

All templates must conform to this schema. No template may add, remove, or rename fields.

Schema version: 2

---

## Field Reference

### Identity

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique note identifier using PREFIX.name format |
| type | string | yes | Note type — determines which template governs the note |
| note_class | string | yes | Semantic classification of the note |
| domain | string | no | Domain the note belongs to |
| layer | string | yes | Architectural layer the note operates in |
| scope | string | no | Scope boundary the note belongs to |

### Authority

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| canonical | boolean | yes | Whether this note is the authoritative source for its subject |
| authority_weight | integer | yes | Numeric authority strength (0–100) |
| resolution_basis | string | yes | How conflicts with other notes are resolved |
| schema_version | integer | yes | Schema version — currently 2 |

### Lifecycle

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| status | string | yes | Current operational status |
| review_status | string | yes | Current review state |
| version | integer | yes | Note version number |
| created | date | no | Date note was created |
| updated | date | no | Date note was last modified |
| last_reviewed | date | no | Date note was last reviewed |
| review_cycle | string | no | How often the note should be reviewed |

### Ownership

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| owner | string | no | Person or agent responsible for this note |

### Relationships (object)

| Sub-field | Type | Description |
|-----------|------|-------------|
| defines | list of IDs | What this note defines |
| part_of | list of IDs | What this note is part of |
| implements | list of IDs | What this note implements |
| governs | list of IDs | What this note governs |
| inherits_from | list of IDs | What this note inherits from |
| applies_to | list of IDs | What this note applies to |
| uses | list of IDs | What this note uses |
| produces | list of IDs | What this note produces |

Relationship values must be stable note IDs (e.g., `SYS.agent_ecosystem`), not wiki links.

### Navigation

| Field | Type | Description |
|-------|------|-------------|
| map | wiki link | Primary structural parent map |
| maps | list of wiki links | Additional associated maps |
| related | list of wiki links | Related notes |
| related_maps | list of wiki links | Related maps |
| related_pipes | list of wiki links | Related pipelines |

Navigation values use Obsidian wiki links (e.g., `"[[MAP.agent_ecosystem]]"`).

### Provenance

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_type | string | yes | How the note was created |
| supersedes | list of IDs | no | Notes this note replaces |
| superseded_by | list of IDs | no | Notes that replace this note |

### Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| tags | list of strings | no | Obsidian tags |
| hash | string | no | Content hash for integrity checking |

---

## Controlled Vocabularies

### note_class

doctrine, governance, architecture, navigation, execution, registry, reference, knowledge, classification

### layer

knowledge, governance, maps, systems, pipes, execution, registry

### status

draft, active, paused, deprecated, archived

### review_status

draft, in_review, approved, superseded, archived

### resolution_basis

canonical, authority_weight, registry_reference, recency, manual_override

### source_type

human_authored, ai_authored, ai_transformed, imported, generated, compiled

### review_cycle

none, monthly, quarterly, biannual, annual, event_driven

---

## Structural Template

All templates must use this exact field structure:

```yaml
id:
type:
note_class:
domain:
layer:
scope:

canonical:
authority_weight:
resolution_basis:
schema_version:

status:
review_status:
version:

created:
updated:
last_reviewed:
review_cycle:

owner:

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []

map:
maps: []

related: []
related_maps: []
related_pipes: []

source_type:
supersedes: []
superseded_by: []

tags: []

hash:
```

Empty list-shaped fields must always use `[]`, never null.