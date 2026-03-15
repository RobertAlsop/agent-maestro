# 02_KNOWLEDGE/indexes

## Purpose

The indexes subdirectory provides navigational aids and cross-references for the knowledge base. Indexes help agents and humans find relevant information by category, enabling discovery of related concepts, registries of canonical documents, and searchable catalogs of system components.

Indexes are generated and maintained to keep the knowledge graph organized and discoverable. Most indexes are updated automatically or semi-automatically as knowledge notes are created and modified.

## Index Files

- **Master Index — Generated.md**: Comprehensive auto-generated index of all concepts, patterns, domains, and system maps with brief descriptions
- **Glossary.md**: Alphabetical glossary of Agent Maestro terminology with definitions
- **Canonical Notes Index.md**: Index of high-authority (authority_weight ≥ 70) documents
- **Canonical Notes Registry.md**: Detailed registry of all canonical notes with metadata
- **Authority Packs Index.md**: Searchable index of all authority packs
- **Authority Pack Registry.md**: Detailed registry of packs with versions and status
- **Pack Version Registry.md**: Version history for all authority packs
- **Pack Lineage Index.md**: Inheritance relationships between packs (who inherits from whom)
- **Compiler Artifacts Registry.md**: Registry of all compiled governance artifacts
- **Constellation Index.md**: Index of all agent constellations and their members
- **Shared Services Index.md**: Catalog of all shared services available to agents
- **System Registry.md**: Master registry of all system components (packs, artifacts, services, agents)
- **Artifact Taxonomy.md**: Taxonomy of compiler output artifacts by type and purpose
- **knowledge_graph_index.csv**: Machine-readable index of all notes in the knowledge base (CSV format)

All files located in `/sessions/loving-busy-bohr/mnt/Agent Maestro/02_KNOWLEDGE/indexes/`

## Index Types

### Navigation Indexes
- **Master Index — Generated**: Start here for comprehensive overview of knowledge base
- **Glossary**: Alphabetical lookup of terms and concepts

### Canonical Document Registries
- **Canonical Notes Index**: Quick reference to high-authority documents
- **Canonical Notes Registry**: Detailed metadata on all canonical notes

### Authority & Governance Indexes
- **Authority Packs Index**: Browse available authority packs
- **Authority Pack Registry**: Detailed pack metadata and versions
- **Pack Version Registry**: Historical versions of packs
- **Pack Lineage Index**: Inheritance relationships between packs
- **Compiler Artifacts Registry**: Compiled artifacts generated from packs

### Organization Indexes
- **Constellation Index**: Agent constellations and composition
- **Shared Services Index**: Available services
- **System Registry**: Master registry of all components
- **Artifact Taxonomy**: Classification of compiler artifacts

### Machine-Readable Indexes
- **knowledge_graph_index.csv**: CSV export of knowledge graph structure

## Conventions

### Index Formatting
- Indexes use markdown with wiki-links to referenced items
- Indexes include brief (1-2 sentence) descriptions of items
- Indexes are organized hierarchically (headings) for browsability
- Links use full wiki-link format: `[[Item Name]]`

### Auto-Generated Indexes
Some indexes are auto-generated (indicated in filename):
- Master Index — Generated is created by a process that scans all notes
- Canonical Notes Registry is regenerated when authority_weight values change
- Authority Pack Registry is auto-updated when packs are versioned

Auto-generated indexes should not be manually edited; re-run the generation process instead.

### CSV Indexes
Machine-readable indexes (*.csv) use standard CSV format:
- UTF-8 encoding
- Comma delimiter
- Headers on first row
- ISO 8601 dates

## Agent Rules

**Agents MAY**:
- Consult indexes to find relevant knowledge and system components
- Use Master Index to orient to the knowledge base
- Use registries to look up current versions of packs and artifacts
- Reference indexes when explaining how to find information

**Agents MUST NOT**:
- Manually edit auto-generated indexes (regenerate instead)
- Delete index files without escalation
- Treat indexes as canonical (they are guides; the actual items are canonical)
- Create conflicting indexes without coordination

**Escalation Required**:
- Changes to manual index structure (if any exist)
- Decisions to add new permanent index types
- Requests to delete or archive indexes
- Conflicts between index versions

## Using Indexes Effectively

**Finding a Concept**:
1. Consult Master Index — Generated for overview
2. Search Glossary for definition
3. Follow wiki-links to related concepts

**Finding an Authority Pack**:
1. Check Authority Packs Index for browse view
2. Check Authority Pack Registry for detailed metadata and versions
3. Check Pack Lineage Index to understand inheritance

**Finding a Compiled Artifact**:
1. Check Compiler Artifacts Registry for what exists
2. Look up source pack and version
3. Find artifact file in artifacts/ directory

**Finding a System Component**:
1. Search System Registry for component name
2. Check Artifact Taxonomy for what type of artifact it is
3. Follow links to detailed component documentation

## Index Maintenance

Indexes should be:

- **Current**: Updated when major changes occur (new packs, new concepts)
- **Consistent**: Aligned with actual items they reference
- **Discoverable**: Linked from main vault entry point and navigation docs
- **Organized**: Hierarchical and categorized for browsing

Most indexes can be regenerated from the vault contents. A maintenance process should:

1. Scan all notes in 02_KNOWLEDGE
2. Identify canonical notes (authority_weight ≥ 90)
3. Extract pack information from 05_SYSTEMS
4. Generate updated index documents
5. Commit changes to vault

## Relationship to Navigation

Indexes work together with system maps to help users navigate the vault:

- **Indexes** are categorical lists (by type, by registry, etc.)
- **System Maps** are relational diagrams (how concepts relate)
- **Both together** provide comprehensive navigation

See system_maps/ for relational navigation aids.

## Relationship to Authority & Governance

Canonical Notes Index and Registry focus specifically on high-authority documents (from 02_KNOWLEDGE/governance/). These are the documents agents and humans should read first when understanding the system.

Authority-related indexes (packs, artifacts, constellations) are the source of truth for the Authority Layer and should be consulted before making decisions about agent permissions or system architecture.
