---
type: system_registry
note_class: registry
domain: agent_maestro
layer: registry

canonical: true
authority_weight: 95
resolution_basis: canonical
schema_version: 2
title: "System Registry"

status: active
review_status: approved
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


  - "[[Agent Maestro — Constellation Architecture Map]]"

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - registry
  - systems

hash: ""
---

# System Registry

## Purpose

Vault-wide authoritative registry for all systems in the Agent Maestro architecture. Every system-level note must be registered here. Systems are discoverable by ID without needing to navigate folders.

## Context

Registries resolve. The System Registry is the canonical resolution anchor for any object with system status — agent systems, shared service systems, authority architecture systems, compiler systems, and constellation systems.

## Structure

Each entry records, where relevant:

| Field | Description |
|---|---|
| `system_id` | Stable unique identifier |
| `display_name` | Human display name |
| `system_type` | agent_system / shared_service / authority / compiler / constellation |
| `lifecycle_status` | active / draft / deprecated |
| `owner` | Responsible owner |
| `canonical_note` | Link to the system's primary note |
| `parent_system` | Parent system if applicable |
| `applied_packs` | Authority packs applied |
| `maps` | Related maps |
| `operational_scope` | Brief scope description |

## Entries

### Agent Systems

| ID | Name | Type | Status | Note |
|---|---|---|---|---|
| SYS.agent_runtime_architecture | Agent Runtime Architecture | agent_system | active | [[Agent Runtime Architecture]] |
| SYS.agent_system_architecture | Agent System Architecture | agent_system | active | [[Agent System Architecture]] |
| SYS.agent_workflow_architecture | Agent Workflow Architecture | agent_system | active | [[Agent Workflow Architecture]] |
| SYS.multi_agent_systems | Multi-Agent Systems | agent_system | active | [[Multi-Agent Systems]] |
| SYS.executive_layer | Executive Layer | agent_system | active | [[Executive Layer]] |
| SYS.shared_services | Shared Services | shared_service | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]] |
| SYS.agent_constellation | Agent Constellation | constellation | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] |
| SYS.agent_ecosystem | Agent Ecosystem | agent_system | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Ecosystem]] |

### Authority Architecture Systems

| ID | Name | Type | Status | Note |
|---|---|---|---|---|
| SYS.authority_architecture | Authority Architecture System | authority | active | [[02_Systems/Agent Maestro/05_SYSTEMS/authority_architecture/Authority Architecture]] |
| SYS.authority_model | Authority Model | authority | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Model]] |
| SYS.authority_inheritance | Authority Inheritance | authority | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Inheritance]] |
| SYS.pack_versioning | Pack Versioning | authority | active | [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Pack Versioning]] |

### Compiler Systems

| ID | Name | Type | Status | Note |
|---|---|---|---|---|
| SYS.authority_pack_compiler | Authority Pack Compiler | compiler | active | [[02_Systems/Agent Maestro/01_CAPTURE/inbox/Authority Pack Compiler]] |
| SYS.compiler_pipeline | Compiler Pipeline | compiler | active | [[Compiler Pipeline]] |
| SYS.compiler_inputs | Compiler Inputs | compiler | active | [[Compiler Inputs]] |
| SYS.compiler_outputs | Compiler Outputs | compiler | active | [[Compiler Outputs]] |
| SYS.host_bindings | Host Bindings | compiler | active | [[Host Bindings]] |
| SYS.compile_failure_semantics | Compile Failure Semantics | compiler | active | [[Compile Failure Semantics]] |
| SYS.compiled_governance_artifacts | Compiled Governance Artifacts | compiler | active | [[Compiled Governance Artifacts]] |
| SYS.integration_manifest | Integration Manifest | compiler | active | [[Integration Manifest]] |

### Other Systems

| ID | Name | Type | Status | Note |
|---|---|---|---|---|
| SYS.memory_architecture | Memory Architecture | shared_service | active | `05_SYSTEMS/memory_architecture/` |
| SYS.operational_intelligence | Operational Intelligence | shared_service | active | `05_SYSTEMS/operational_intelligence/` |
| SYS.infrastructure | Infrastructure | infrastructure | active | `05_SYSTEMS/infrastructure/` |
| SYS.organizational_integration | Organizational Integration | agent_system | active | `05_SYSTEMS/organizational_integration/` |

## Governance Rules

1. Every system note must be registered before it can be referenced as a system dependency
2. System IDs are stable and never reused
3. Deprecated systems remain in registry with `lifecycle_status: deprecated`
4. All applied packs must be valid entries in [[Authority Pack Registry]]

## Related

- [[Agent Maestro — Systems Map]] — navigation layer above this registry
- [[Canonical Notes Registry]] — the note-level registry
