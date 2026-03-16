# Templates System — Governance

**Foundations Alignment**: The template system implements the Structure seed by defining canonical structural contracts for every note type, ensuring consistency and verifiability across the knowledge graph.

## Purpose
This directory contains the canonical template system for the Agent Maestro vault. Templates define structural contracts — not suggestions — for every note type in the vault.

## Structure
- **frontmatter/**: The Frontmatter Schema v1 — the master schema all templates inherit from
- **core_knowledge/**: Templates for knowledge-layer notes (concepts, references, governance docs, principles, modes, scope, decisions, north star)
- **architecture_and_navigation/**: Templates for maps, indexes, registries, taxonomies, systems, authority packs
- **execution_and_planning/**: Templates for pipelines, processes, projects, roadmaps, strategies, authority pack sections
- **governance/**: Template system governance (Design Doctrine, Governance Rules, Mapping, Registry, Ruleset)

## Authority Hierarchy
Frontmatter Schema > Note Templates > Template Mapping > Template Registry > Template Ruleset > Design Doctrine

## Agent Rules
- Agents MUST use the appropriate template when creating new notes
- Agents MUST NOT modify templates without governance escalation
- Agents MAY read templates to understand required structure for any note type
- Template compliance can be validated using the Vault Template Compliance Scan prompt

## Template-to-Folder Mapping
See governance/Template Mapping.md for the canonical assignment of which templates apply to which vault folders.

## Integration Note
These templates were originally developed in v0.0.1 and stored in 01_CAPTURE/unprocessed/88_TEMPLATES. They were formally integrated into 05_SYSTEMS/templates during Session 2 (2026-03-14) as part of the v0.2 Evolution Roadmap, Wave 1.