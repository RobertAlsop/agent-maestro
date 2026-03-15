---
id: PAT.thin_edge_thick_core
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
scope: null

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-12
updated: 2026-03-12
last_reviewed: null
review_cycle: none

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

map: "[[Agent Maestro — Concepts Map]]"
maps: []

related: []
related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - pattern
  - agent_maestro
  - architecture

hash: ""
---

# Thin-Edge Thick-Core Pattern

## Summary

Keep agents at the execution edge as thin and focused as possible — minimal logic, minimal state, minimal authority. Push shared intelligence, governance, memory, and orchestration capability into a thick, shared core. Agents call the core; the core does not live inside the agent.

## Problem

Agents that accumulate logic, state, and authority beyond their scope become ungovernable and hard to replace. Distributing governance logic across many agents makes it inconsistent and untestable.

## Solution

Design agents as thin executors that consume [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]] for all shared capabilities — memory, orchestration, governance checking. The governance core ([[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]], [[Compiled Governance Artifact|compiled artifacts]], [[Memory Architecture]]) is centralised and shared. Agents are interchangeable at the edge.

## Rules

1. Agents should not implement their own memory management — use [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]]
2. Agents should not implement governance logic internally — load from compiled artifacts
3. State that crosses agent boundaries must go through the shared core
4. The thinner the edge agent, the easier it is to replace, upgrade, or audit

## Relationships

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Shared Services]] — the thick core service layer
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — the structural context where this pattern applies
- [[Compiled Governance Artifact]] — the governance object loaded from core
- [[Anti-Agent-Sprawl Pattern]] — complementary pattern preventing capability sprawl
- [[Agent Maestro — Concepts Map]]
