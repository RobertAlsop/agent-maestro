---
id: PROJ.next_phase_proposal_v0.2
type: project
note_class: execution
domain: governance
layer: execution
scope: null
canonical: false
authority_weight: 70
resolution_basis: authority_weight
schema_version: 2
status: active
review_status: draft
version: 1
created: 2026-03-14
updated: 2026-03-14
last_reviewed: null
review_cycle: quarterly
owner: AgentMaestro
relationships:
  defines: []
  part_of: []
  implements: []
  governs: []
  inherits_from:
  - '[[Agent Maestro v0.1 — Improvement Proposal]]'
  applies_to: []
  uses: []
  produces: []
map: '[[Agent Maestro — Navigation Map]]'
maps: []
related:
- '[[Agent Maestro v0.1 — Improvement Proposal]]'
- '[[Agent Maestro v0.1 — Session Log 2026-03-14]]'
related_maps: []
related_pipes: []
source_type: ai_authored
supersedes: []
superseded_by: []
tags:
- project
- proposal
- next_phase
hash: ''
---

# Agent Maestro v0.2 — Next Phase Proposal

## Context

v0.1 delivered the foundation: a working compiler, the Vault Curator constellation, MWP workspaces, CLAUDE.md governance files, knowledge graph population, structured data CSVs, and a Quickstart Guide. All eight improvements passed verification.

What v0.1 did not deliver is a working runtime. The compiler produces compiled governance artifacts (JSON), the authority packs define what agents may do, and the MWP workspaces define where agents work — but no agent actually loads its authority pack at runtime, checks permissions before acting, or writes structured execution logs. The framework is complete at design time but has no runtime enforcement.

v0.2 makes Agent Maestro operational.

## Goals

- Personal operational tool: Claude can govern its own work inside the vault using Agent Maestro
- Product foundation: The runtime engine becomes the reusable core for future constellations
- Research: Prove that governance-first agent systems work in practice, not just in theory

## Three Phases

### Phase 1 — Agent Runtime Engine

Build a lightweight Python runtime that any specialist script can use to operate under governance.

**What it does:**

1. Loads the compiled governance artifact from the MWP workspace `authority/` directory
2. Provides a `GovernedAgent` class that wraps any specialist's logic
3. Before each action, checks the `governed_actions` list in the compiled artifact — if the action is `allowed`, proceed; if `requires_escalation`, write to `artifacts/escalations/`; if `denied`, block and log
4. Writes structured execution logs to `artifacts/logs/execution_log.csv`
5. Populates the MWP workspace at startup (copies compiled artifact, agent definition, stage contract, references)

**What gets built:**

| Deliverable | Location |
|---|---|
| `runtime.py` — GovernedAgent class and workspace manager | `05_SYSTEMS/infrastructure/tools/runtime.py` |
| Updated `link_auditor.py` — uses GovernedAgent | `05_SYSTEMS/infrastructure/tools/link_auditor.py` |
| Updated `schema_validator.py` — uses GovernedAgent | `05_SYSTEMS/infrastructure/tools/schema_validator.py` |
| `orchestrator.py` — runs the full Vault Curator maintenance cycle | `05_SYSTEMS/infrastructure/tools/orchestrator.py` |

**The runtime contract:**

```python
from runtime import GovernedAgent

agent = GovernedAgent(
    compiled_artifact_path="authority/link_auditor_compiled.json",
    workspace_path="workspaces/link_auditor/"
)

# This checks the authority pack before executing
agent.request_action("Scan vault files for wiki-links")  # → allowed
agent.request_action("Modify vault files")                # → denied, logged

# Write results
agent.write_artifact("link_audit_report.csv", report_data)
agent.complete()  # Writes execution log, closes workspace
```

**Success criteria:** Run `python orchestrator.py` from the vault root and get a complete maintenance cycle: specialists audit, reports are written, execution logs are recorded, escalations are captured — all governed by compiled authority packs.

### Phase 2 — Claude Host Binding

Bind compiled governance artifacts to Claude itself as the runtime host. This means Claude, when working inside the Agent Maestro vault, can load a compiled artifact and enforce it on its own behaviour.

**What it does:**

1. Defines a "claude" host type for the compiler (in addition to "filesystem")
2. Produces a CLAUDE.md-compatible governance injection — a compiled artifact translated into Claude-readable instructions
3. Creates a `claude_host_binding.py` script that reads a compiled artifact and outputs a CLAUDE.md section containing the governance rules in natural language

**Why this matters:**

Right now, the root CLAUDE.md contains manually written governance rules. With Claude host binding, those rules would be generated from compiled authority packs — meaning the governance that applies to Claude when it works in the vault is the same governance that applies to any other agent. Same source of truth, same compiler, same audit trail.

**What gets built:**

| Deliverable | Location |
|---|---|
| Updated compiler with `claude` host type | `05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py` |
| `claude_host_binding.py` — artifact-to-CLAUDE.md translator | `05_SYSTEMS/infrastructure/tools/claude_host_binding.py` |
| Host Binding specification for Claude | `05_SYSTEMS/authority_architecture/compiler/Host Bindings.md` (updated) |
| Generated CLAUDE.md governance section | Appended to folder-level CLAUDE.md files |

**Success criteria:** Compile the Vault Curator Executive pack with `--host claude`, get a CLAUDE.md section that accurately represents the governance rules, and verify that Claude follows those rules when working in the vault.

### Phase 3 — Second Constellation

Build a second constellation to prove the framework is composable. The specific domain should be chosen based on what's most useful at that point — possibilities include:

**Option A: Research Pipeline Constellation** — A constellation that manages research workflows: an Executive that decides what to research, a Supervisor that coordinates source gathering and analysis, and specialists for web search, document summarisation, and synthesis. Useful for the "personal operational tool" goal.

**Option B: Content Pipeline Constellation** — A constellation that manages content creation: an Executive that sets editorial priorities, a Supervisor that coordinates drafting and review, and specialists for outlining, writing, and fact-checking. Useful for the "foundation for a product" goal.

**Option C: Authority Auditor Constellation** — A constellation that audits the authority architecture itself: checking that all packs compile, that inheritance chains are valid, that compiled artifacts match their source packs, and that the registry is consistent. This is Agent Maestro governing Agent Maestro's governance — the most architecturally interesting option.

**What gets built (regardless of choice):**

- New authority packs (YAML) for all agents in the constellation
- Compiled artifacts (JSON) via the compiler
- Constellation directory with standard structure
- MWP workspaces for each agent
- Specialist Python scripts using GovernedAgent from Phase 1
- Claude host binding for the constellation's governance
- Registry entries in all structured data CSVs

**Success criteria:** The second constellation runs end-to-end, governed by compiled authority packs, using the same runtime engine and Claude host binding from Phases 1 and 2.

## Build Order

```
Phase 1: Agent Runtime Engine
  ├── GovernedAgent class (runtime.py)
  ├── Workspace manager (populates MWP directories)
  ├── Update link_auditor.py and schema_validator.py to use GovernedAgent
  ├── Build orchestrator.py for full maintenance cycle
  └── Run and verify Vault Curator end-to-end

Phase 2: Claude Host Binding
  ├── Add 'claude' host type to compiler
  ├── Build artifact-to-CLAUDE.md translator
  ├── Recompile Vault Curator packs with claude host binding
  └── Verify Claude follows generated governance rules

Phase 3: Second Constellation
  ├── Choose domain (decide at Phase 2 completion)
  ├── Author authority packs
  ├── Compile and bind
  ├── Build specialist scripts with GovernedAgent
  └── Run and verify end-to-end
```

## What This Achieves

After v0.2, Agent Maestro will have:

- A **working runtime engine** that enforces governance at execution time
- **Claude as a governed agent host** — the first real host binding
- **Two working constellations** proving the framework is composable
- **Self-hosting capability** — Agent Maestro governs Claude, which governs Agent Maestro

This transforms Agent Maestro from a governance framework with documentation and a compiler into an operational intelligence system with runtime enforcement. It crosses the line from "designed" to "deployed."

## Recommended Model

Use Opus for Phases 1 and 2 (runtime engine and host binding require careful cross-file reasoning). Phase 3 can use Sonnet if the runtime engine is solid, since it's applying an established pattern to a new domain.

## Session Handoff Notes

This proposal was produced at the end of the v0.1 build session (2026-03-14). The builder should:

1. Read this proposal first
2. Read the v0.1 session log for design rationale context
3. Read the Quickstart Guide to understand the current system state
4. Start with Phase 1 — the GovernedAgent class is the foundation for everything else

Key files to start with:
- This proposal: `04_PROJECTS/active/Agent Maestro v0.2 — Next Phase Proposal.md`
- Session log: `04_PROJECTS/active/Agent Maestro v0.1 — Session Log 2026-03-14.md`
- Quickstart: `02_KNOWLEDGE/system_maps/Agent Maestro — Quickstart.md`
- Root CLAUDE.md: `CLAUDE.md`
- Compiler: `05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py`
- Existing specialist scripts: `05_SYSTEMS/infrastructure/tools/`
- Vault Curator constellation: `05_SYSTEMS/agent_systems/constellations/vault_curator/`
