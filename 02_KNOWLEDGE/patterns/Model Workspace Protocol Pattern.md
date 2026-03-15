---
id: PAT.model_workspace_protocol_pattern
type: concept
note_class: knowledge
domain: system_architecture
layer: knowledge
scope: null

canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2

status: active
review_status: draft
version: 1

created: 2026-03-14
updated: 2026-03-14
last_reviewed: null
review_cycle: annual

owner: AgentMaestro

relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Model Workspace Protocol]]"
  uses: []
  produces: []

map: "[[Agent Maestro — Layer Model Map]]"
maps:
  - "[[Agent Maestro — Concepts Map]]"

related:
  - "[[Constellation Architecture Pattern]]"
  - "[[Agent Maestro Layer Model]]"

related_maps: []
related_pipes: []

source_type: ai_authored
supersedes: []
superseded_by: []

tags:
  - pattern
  - agent_maestro
  - workspace

hash: ""
---

# Model Workspace Protocol Pattern

## Summary

Structure every agent execution as a self-contained workspace with five standard directories — authority, agents, stages, references, artifacts — so that executions are auditable, reproducible, and governed.

## Problem

When agents execute without a standardised workspace structure, it becomes impossible to determine after the fact what authority the agent operated under, what knowledge it had access to, what stage of a workflow it was in, or what it produced. This makes auditing impractical and reproduction impossible.

## Solution

Every agent execution operates within a workspace that follows the [[Model Workspace Protocol]] structure:

```
workspace/
   authority/       # Compiled authority pack
   agents/          # Agent definition
   stages/          # Stage contract
   references/      # Reference knowledge
   artifacts/       # Outputs, logs, escalations
```

Before an agent begins work, its workspace is populated with the compiled authority pack, the agent definition, the current stage contract, and any reference knowledge needed. As the agent works, it writes output artifacts, execution logs, and escalation requests to the artifacts directory.

## Rules

1. Every agent execution must have a workspace that conforms to MWP structure
2. The `authority/` directory must contain a valid [[Compiled Governance Artifact]] before the agent starts
3. The agent must not access files outside its workspace unless explicitly permitted by its authority pack
4. All outputs must be written to `artifacts/`
5. All escalation requests must be written to `artifacts/escalations/`
6. Execution logs must be written to `artifacts/logs/` and must include: agent ID, start time, end time, actions taken, and outcome
7. Workspaces must be inspectable after execution — do not delete workspace contents on completion

## Example

A Link Auditor specialist agent in the Vault Curator constellation:

```
vault_curator/workspaces/link_auditor/
   authority/
      link_auditor_compiled.json
   agents/
      link_auditor.md
   stages/
      audit_stage.md
   references/
      vault_file_index.csv
   artifacts/
      link_audit_report.csv
      logs/
         execution_log.csv
      escalations/
         broken_links_requiring_deletion.md
```

## Relationships

- [[Model Workspace Protocol]] — the concept this pattern operationalises
- [[Agent Maestro Layer Model]] — MWP implements the Workspace Layer
- [[Constellation Architecture Pattern]] — constellations use MWP for agent execution
- [[Deterministic Control Surfaces]] — MWP makes control surfaces inspectable
