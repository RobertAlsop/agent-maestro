---
type: reference
note_class: reference
domain: ai_governance
layer: knowledge

canonical: false
authority_weight: 90
resolution_basis: authority_weight
schema_version: 2
title: "Governance Schemas Reference"

status: draft
review_status: draft
version: 1

created_date: 2026-03-12
last_modified: 2026-03-12

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to: []
  uses: []
  produces: []



source_type: imported
supersedes: []
superseded_by: []

tags:
  - reference
  - schemas
  - governance

hash: ""
---

# Governance Schemas Reference

## Purpose

Formal schema definitions for all design-time governance artifacts in Agent Maestro — specifically [[Authority Pack|Authority Packs]] and [[Pack Manifest|Pack Manifests]]. This reference governs what valid governance artifacts must contain.

## Context

Schemas are the structural contracts that make governance machine-verifiable. The [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] validates input packs against these schemas before processing. This reference is the authoritative source for pack schema definitions.

## Authority Pack Section Schemas

Following the [[Authority Pack Grammar]] (sections 00–13):

| Section | Required Fields |
|---|---|
| 00_identity | `pack_id`, `pack_name`, `version`, `inherits_from`, `overrides` |
| 01_scope | `domain`, `applies_to`, `exclusions` |
| 02_authority_domain | `decision_types`, `execution_types`, `escalation_types` |
| 03_governed_entities | `agent_classes`, `agent_instances` |
| 04_governed_actions | `allowed_actions`, `restricted_actions`, `prohibited_actions` |
| 05_rules | `rules[]` with `id`, `text`, `overridable` |
| 06_control_gates | `gates[]` with `id`, `condition`, `action`, `escalation_class` |
| 07_evidence_requirements | `required_evidence[]`, `retention_period` |
| 08–13 | (interaction and extension sections — context-dependent) |

## Pack Manifest Schema

Required fields:
- `manifest_id`, `manifest_version`
- `components[]` — list of pack sections included
- `grammar_sections[]` — which grammar sections this manifest activates
- `dependencies[]` — other packs this manifest depends on
- `runtime_requirements[]` — runtime conditions needed
- `validation_rules[]` — additional validation rules

## Related Concepts

- [[Authority Pack Grammar]] — the structural standard these schemas formalise
- [[Pack Manifest]] — the artifact whose schema is defined here
- [[Compiler Artifact Schemas Reference]] — runtime artifact schemas
- [[Agent Maestro — Governance Map]]
