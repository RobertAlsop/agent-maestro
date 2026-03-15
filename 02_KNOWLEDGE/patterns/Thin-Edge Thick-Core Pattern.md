---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Thin-Edge Thick-Core Pattern"

status: active
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

Design agents as thin executors that consume Shared Services]] for all shared capabilities — memory, orchestration, governance checking. The governance core (Authority Architecture]], [[Compiled Governance Artifact|compiled artifacts]], [[Memory Architecture]]) is centralised and shared. Agents are interchangeable at the edge.

## Rules

1. Agents should not implement their own memory management — use Shared Services]]
2. Agents should not implement governance logic internally — load from compiled artifacts
3. State that crosses agent boundaries must go through the shared core
4. The thinner the edge agent, the easier it is to replace, upgrade, or audit

## Relationships

- Shared Services]] — the thick core service layer
- Agent Constellation]] — the structural context where this pattern applies
- [[Compiled Governance Artifact]] — the governance object loaded from core
- [[Anti-Agent-Sprawl Pattern]] — complementary pattern preventing capability sprawl
- [[Agent Maestro — Concepts Map]]
