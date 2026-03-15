---
type: concept
note_class: knowledge
domain: agent_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Constellation Architecture Pattern"
status: active
review_status: draft
version: 1
created_date: 2026-03-12
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  uses:
    - "[[Executive Agent]]"
    - "[[Supervisor Agent]]"
    - "[[Specialist Agent]]"
  produces: []
  - "[[Agent Maestro — Constellation Architecture Map]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - pattern
  - agent_maestro
  - constellation
hash: ""
---

# Constellation Architecture Pattern

## Summary

Design every multi-agent capability as a governed constellation — a bounded, layered cluster of agents with explicit authority architecture, standard folder structure, and registry registration.

## Problem

Ad hoc multi-agent deployments produce unpredictable authority boundaries, untracked agent relationships, and ungovernable escalation paths.

## Solution

Every significant multi-agent capability should be instantiated as a constellation with: a defined executive agent, one or more supervisor agents, specialist agents, and authority packs at each layer. Constellations follow the standard folder structure and are registered in the [[Constellation Index]].

## Standard Structure

```
00_map/             — navigation entry point
01_executive_links/ — executive agent links
02_supervisors/     — supervisor definitions
03_specialists/     — specialist definitions
04_workflows/       — workflow definitions
05_memory/          — memory architecture
06_authority_links/ — authority pack links
07_metrics/         — observability
```

## Rules

1. Every constellation must have exactly one executive agent
2. Authority packs must be applied at every layer
3. The constellation must be registered in [[Constellation Index]]
4. Escalation paths must be defined before deployment

## Relationships

- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]] — the concept this pattern produces
- [[Executive-Supervisor-Specialist Pattern]] — the layering pattern used
- [[Authority Pack Grammar]] — governs the pack structure applied
- [[Agent Maestro — Constellation Architecture Map]]
