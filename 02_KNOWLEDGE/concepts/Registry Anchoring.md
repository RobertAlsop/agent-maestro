---
type: concept
note_class: knowledge
domain: agent_maestro
layer: knowledge
schema_version: 2
title: "Registry Anchoring"
status: active
review_status: reviewed
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
authority_weight: 65
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Authority Architecture]]"
    - "[[Agent Maestro — Concepts Map]]"
  implements:
    - "[[Agent Maestro — Principles]]"
  governs:
    - "[[Canonical Notes Registry]]"
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]]"
    - "[[Authority Pack Registry]]"
  inherits_from: []
  applies_to:
    - "[[02_KNOWLEDGE]]"
  uses: []
  produces: []
tags:
  - concept
  - agent_maestro
  - registry
  - governance
  - authority
---

# Registry Anchoring

## Purpose

Defines the principle that every class of governed object must be resolvable through an authoritative registry. Registry anchoring is what distinguishes a well-governed vault from one that appears organized but cannot resolve authority at scale.

## Core Principle

**Maps navigate. Registries resolve.**

| Type | Purpose |
|------|---------|
| **Map** | Helps humans and agents move through the vault |
| **Index** | Groups related items for lookup |
| **Registry** | Resolves ambiguity — which object is canonical, which version is active |

Use **Map** for navigation, **Index** for grouped lookup, **Registry** for authority and membership.

## The Rule

**If an object class matters operationally, it must be registry-addressable.**

An object should have a true registry (not just an index) if it answers one of these questions:
- Does this object officially exist?
- Which note is authoritative?
- Which version is active?
- Which system does this belong to?
- Which objects are valid members of this class?

## Required Registries for Agent Maestro

### 1. Canonical Notes Registry
Anchors the highest-authority note for core concepts and doctrine.
Examples: `CON.agent`, `CON.authority_pack`, `PRN.agent_maestro_principles`

### 2. System Registry
Anchors all major systems.
Examples: `SYS.agent_runtime_architecture`, `SYS.authority_pack_compiler`, `SYS.memory_model`

### 3. Authority Pack Registry
Makes packs operationally addressable.
Examples: `PACK.conceptual_authority`, `PACK.domain.marketing`, `PACK.role.supervisor`

### 4. Pack Version Registry
Tracks version drift — the fastest way AI systems become unreliable.
Must record: current version, superseded versions, canonical active version.

### 5. Compiler Artifacts Registry
Anchors compiled outputs so agents cannot confuse source packs with compiled forms.

## What Breaks Without Registry Anchoring

At around 3k–5k notes, without anchoring:
- Duplicate canonical concepts appear
- Notes compete without resolution
- Inheritance becomes ambiguous
- Pack/version confusion arises
- Maps look good but don't resolve authority

At that point the vault still appears organized, but AI makes subtle mistakes because it cannot determine the governed source of truth. That is the dangerous failure mode.

## The Governance Rule

**Any object used for authority, inheritance, compilation, or execution must be resolvable through a registry.**

That one rule makes Agent Maestro dramatically more robust.

## Relationships

- [[Canonical Notes Registry]] — implements this concept
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/indexes/System Registry]] — implements this concept
- [[Authority Pack Registry]] — implements this concept
- [[Pack Version Registry]] — implements this concept
- [[Compiler Artifacts Registry]] — implements this concept
- [[Agent Maestro — Vault Rules]] — the governance document this principle feeds into
