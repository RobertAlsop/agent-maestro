---
type: concept
note_class: knowledge
domain: system_architecture
layer: knowledge
canonical: false
authority_weight: 60
resolution_basis: authority_weight
schema_version: 2
title: "Model Workspace Protocol"
status: active
review_status: draft
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements:
    - "[[Model Workspace Protocol Pattern]]"
  governs: []
  inherits_from: []
  applies_to:
    - "[[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Agent Constellation]]"
  uses:
    - "[[Authority Pack]]"
    - "[[Compiled Governance Artifact]]"
    - "[[Specialist Agent]]"
    - "[[Executive Agent]]"
    - "[[Supervisor Agent]]"
  produces: []
  - "[[Agent Maestro — Systems Map]]"
  - "[[Agent Maestro Layer Model]]"
  - "[[Model Workspace Protocol Pattern]]"
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
  - concept
  - agent_maestro
  - workspace
  - protocol
hash: ""
---

# Model Workspace Protocol

## Definition

The Model Workspace Protocol (MWP) is a standardised file structure that defines the operational environment for every agent execution. When an agent begins work, it operates within an MWP workspace — a self-contained directory that provides everything the agent needs and captures everything it produces.

## Workspace Structure

```
workspace/
   authority/       # Compiled authority pack for this agent
   agents/          # Agent definition and role contract
   stages/          # Current workflow stage contract
   references/      # Reference knowledge the agent needs
   artifacts/       # Working outputs produced by the agent
```

### Directory Responsibilities

**`authority/`** — Contains the compiled governance artifact for this agent. The agent reads its authority pack from here before taking any action. This is the enforcement boundary.

**`agents/`** — Contains the agent's own definition: its role, capabilities, escalation path, and the constellation it belongs to.

**`stages/`** — Contains the current workflow stage contract. Defines what the agent should do in this specific execution, what the entry conditions were, and what the exit conditions are.

**`references/`** — Contains reference knowledge the agent needs to reason about its task. This may include indexes, registries, or knowledge graph extracts from the [[Knowledge Graph Layer]].

**`artifacts/`** — The agent's working directory. All outputs go here. Subdivided into:

- `artifacts/` (root) — primary output artifacts
- `artifacts/logs/` — execution logs and audit trail
- `artifacts/escalations/` — decisions that exceeded the agent's authority, forwarded to supervisor or executive

## Execution Lifecycle

**At execution start, the agent loads:**

| What | From | Purpose |
|---|---|---|
| Authority pack | `authority/` | Defines what the agent may do |
| Stage contract | `stages/` | Defines what the agent should do right now |
| Reference knowledge | `references/` | Context the agent needs to reason |
| Working artifacts | `artifacts/` | Previous outputs or inputs to work with |

**At execution end, the agent produces:**

| What | To | Purpose |
|---|---|---|
| Output artifacts | `artifacts/` | The work product |
| Execution log | `artifacts/logs/` | Audit trail of what happened |
| Escalation requests | `artifacts/escalations/` | Decisions that exceeded authority |

## Boundaries

MWP governs the Workspace Layer only. It does not define agent behaviour (Agent Runtime), workflow sequencing (Workflow Layer), or governance rules (Authority Layer). It defines *where* things happen, not *what* happens or *who* does it.

MWP workspaces are ephemeral per execution. A new execution may create a new workspace or reuse an existing one, but the workspace state at any point in time must be a complete, inspectable record of that execution.

## Key Properties

- **Self-contained** — everything an agent needs is in its workspace
- **Auditable** — after execution, the workspace is a complete audit record
- **Reproducible** — given the same inputs (authority, stage, references), the same agent should produce the same outputs
- **Portable** — workspaces are plain directories; no database or special tooling required

## Relationships

- [[Agent Maestro Layer Model]] — MWP implements the Workspace Layer
- [[Model Workspace Protocol Pattern]] — the design pattern for building MWP workspaces
- [[Authority Pack]] — loaded from the `authority/` directory
- [[Compiled Governance Artifact]] — the runtime form of the authority pack
