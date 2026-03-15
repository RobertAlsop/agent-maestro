# 05_SYSTEMS/memory_architecture

## Purpose

The Memory Architecture subdirectory defines and implements the three-layer memory model that enables agents to access, maintain, and reason about knowledge. The architecture describes how agents know things (through graphs, structured data, and vector embeddings) and provides governance for how memory is accessed and evolved.

Memory is critical infrastructure: agents execute according to what they know. The memory architecture determines the shape and accessibility of that knowledge.

## Three-Layer Model

The memory architecture has three layers (two currently active, one architecturally planned):

### 1. Knowledge Graph Layer (Active)
Obsidian vault notes form a semantic graph via wiki-links and typed relationships. Nodes are concepts, patterns, governance documents, and system maps. Edges are wiki-links and frontmatter relationships. This layer provides rich semantic context and explicit conceptual relationships.

Files in this layer:
- **Knowledge Graph Layer.md**: Architecture documentation
- All markdown files throughout the vault (02_KNOWLEDGE is the primary graph)

### 2. Structured Data Layer (Active)
CSV and JSON files with clear schemas provide structured, queryable data. Used for registries, measurements, execution logs, and operational state. Enables consistent, machine-readable data exchange.

Key structured data files:
- **authority_pack_registry.csv**: Registry of authority packs
- **compiler_artifacts_registry.csv**: Registry of compiled governance artifacts
- **Structured Data Registry.md**: Master reference for CSV schemas and conventions
- CSV files throughout 05_SYSTEMS and 06_EXECUTION

### 3. Vector Memory Layer (Architecturally Planned)
Planned for future implementation. Will enable semantic search and similarity-based retrieval across unstructured content. Not yet active.

File:
- **Vector Memory Layer.md**: Architecture and future implementation plan

## Structure

- **Knowledge Graph Layer.md**: Documentation for how Obsidian notes form a semantic graph
- **Structured Data Layer.md**: Documentation for CSV/JSON structured data files
- **Vector Memory Layer.md**: Architecture for future vector embeddings (not yet active)
- **Memory Model.md**: Overall memory architecture and layer interactions
- **Memory Governance.md**: Governance rules for memory access and modification
- **Structured Data Registry.md**: Master reference for all CSV file schemas, naming conventions, and validation rules
- **Context Pack Architecture.md**: How context packs encapsulate temporary memory modifications

All files located in `05_SYSTEMS/memory_architecture/`

## Conventions

### Knowledge Graph Layer
- Wiki-links: `[[Note Name]]` format
- Relationships in frontmatter using typed edges (defines, part_of, implements, etc.)
- All notes should have proper YAML frontmatter with relationships
- Schema version 2 required

### Structured Data Layer
- CSV files must follow Structured Data Registry conventions
- UTF-8 encoding, comma delimiters
- ISO 8601 dates
- Headers on first row
- Consistency across related files (e.g., pack_registry.csv and compiler_artifacts_registry.csv must align)

### Naming Conventions
- Layer documentation files use Title Case
- Registry files end with _registry.csv
- Schema reference files are in Structured Data Registry.md

## Agent Rules

**Agents MAY**:
- Read all memory layer documentation
- Query the Knowledge Graph Layer (via wiki-links)
- Read structured data from CSV registries
- Update relationships in Knowledge Graph frontmatter (maintaining graph consistency)
- Write new CSV data following Structured Data Registry conventions
- Generate CSV exports from operational data

**Agents MUST NOT**:
- Modify Knowledge Graph Layer structure without escalation (graph integrity is critical)
- Delete or rename wiki-linked notes without updating all references
- Violate CSV schema conventions in the Structured Data Layer
- Manually edit registries when systems could generate consistent data instead
- Create new structured data formats without documenting them in Structured Data Registry

**Escalation Required**:
- Changes to the three-layer model architecture
- Modifications to Knowledge Graph structure (node/edge semantics)
- New CSV schemas or changes to existing schemas
- Decisions to archive or delete large portions of the knowledge graph
- Integration of vector embeddings (when Vector Memory Layer becomes active)

## Key Documents

- **Memory Model.md**: Overall architecture, how three layers interact, access patterns
- **Knowledge Graph Layer.md**: How Obsidian notes form a semantic graph (most agents use this layer)
- **Structured Data Layer.md**: CSV/JSON structured data (operational state, registries)
- **Vector Memory Layer.md**: Future vector embeddings (not yet active)
- **Memory Governance.md**: Governance rules for memory access and evolution
- **Structured Data Registry.md**: Master reference for all CSV file formats and schemas
- **Context Pack Architecture.md**: Temporary memory modifications via context packs

## Structured Data Registry

The **Structured Data Registry.md** document is the master reference for all structured data in the system. It specifies:

- CSV file naming conventions
- Required and optional columns for each file type
- Data types and validation rules
- Relationships between registry files
- Tools for generating and validating CSV files

Key registry files the system depends on:
- **authority_pack_registry.csv**: Packs and versions
- **compiler_artifacts_registry.csv**: Compiled artifacts and versions
- Various CSV files in 06_EXECUTION (logs, reports, task tracking)

## Context Packs

Context Packs are temporary memory modifications that apply constraints or provide additional information for specific execution contexts. They are layered over the base memory architecture without modifying it permanently.

See **Context Pack Architecture.md** for details on how context packs work and when they should be used.

## Memory Access Patterns

Agents access memory through:

1. **Graph Traversal**: Start from a concept, follow wiki-links to related concepts
2. **Relationship Queries**: Ask for all notes that have a specific relationship type
3. **Structured Data Queries**: Look up values in CSV registries
4. **Full-Text Search**: Search all markdown for keyword matches (in Obsidian UI)

Different access patterns are appropriate for different query types. The Knowledge Graph is best for conceptual relationships; structured data is best for operational state.

## Governance Principles

Memory governance is guided by:

- **Authoritative Source**: Each piece of information has a single authoritative source
- **Consistency**: Related data (e.g., registry files) must remain consistent
- **Auditability**: Who made what change to memory (via git or change logs)
- **Accessibility**: Agents should be able to access needed information efficiently
- **Integrity**: Graph structure, CSV schemas, relationships must be maintained

See **Memory Governance.md** for detailed governance rules.

## Relationship to Agent Execution

What agents know (from memory architecture) determines what they can do (in execution layer). Agents in 06_EXECUTION query memory via:

- Reading KNOWLEDGE concepts and patterns
- Looking up their own authority constraints in authority_pack_registry.csv
- Querying compiled artifacts in compiler_artifacts_registry.csv
- Reading operational state from structured data CSV files

Memory consistency directly affects agent behavior. Inconsistent or corrupted memory can cause agents to violate constraints.

See CLAUDE]] in 06_EXECUTION/ to understand how agents query and use memory during execution.
