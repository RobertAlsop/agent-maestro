---
schema_version: 2
title: "Agent Maestro v0.3 — Build Brief"
type: brief
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 75
status: draft
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
source_type: ai_authored
defines: []
part_of:
  - "[[Agent Maestro — Evolution Roadmap v0.2]]"
implements:
  - "[[Build Session Protocol]]"
governs: []
applies_to: []
uses: []
produces: []
tags:
  - brief
  - roadmap
  - v0.3
  - build-contract
supersedes:
  - "[[Agent Maestro v0.3 — Next Moves Proposal]]"
superseded_by: []
hash: null
owner: null
resolution_basis: authority_weight
---

# Agent Maestro v0.3 — Build Brief

**Date**: 2026-03-15
**Status**: DRAFT — Awaiting Approval
**Sources**: Claude Adversarial Audit + Claude Next Moves Proposal + ChatGPT 5.2 Improvement Proposal
**Build Environment**: Claude Code (Opus), all sessions
**Protocol**: Build Session Protocol (Input → Brief → Approval → Build → Output Summary → Session Log → Git Commit)

---

## Executive Summary

Two independent analyses of Agent Maestro were conducted: an adversarial code audit plus strategic proposal (Claude/Opus) and an architectural improvement proposal (ChatGPT 5.2). This brief synthesizes both into a single prioritized build plan.

Both analyses converge on the same core insight: Agent Maestro has exceptional governance and knowledge architecture, but the gap between "defined" and "executable" is the primary bottleneck. The system needs to become machine-operable — agents should be able to boot, navigate, execute workflows, and report results without human hand-holding at every step.

The proposals also agree on what NOT to do yet: domain deployment (TBP business agents), model routing/benchmarking, and multi-vault networking are future horizons that depend on the core system working end-to-end first.

---

## Where The Two Proposals Agree

| Theme | Claude Proposal | ChatGPT Proposal | Verdict |
|-------|----------------|-------------------|---------|
| Safety hardening is urgent | 5 critical findings (permission bypass, control gates advisory, evidence not validated) | "Never allow agents with overlapping authority" | **Do first** |
| Agents need a single entry point | Fix stale paths, sync registries | "System Kernel" + "System Map" — agents read one file first | **Do first** |
| Workflow execution is the bridge | Move 3: workflow_engine.py | Phase 3: Runtime Infrastructure / Model Router | **Do second** |
| Agent boundaries must be explicit | Audit found vault_curator/vault_maintenance overlap | "Agent Responsibility Registry" — biggest failure mode in multi-agent | **Do second** |
| Escalation needs a resolution loop | Move 4: escalation_processor.py | Phase 2: Governance Constellation | **Do third** |
| Git/versioning is infrastructure | Move 2: Git/GitHub + release protocol | Not addressed (assumed) | **Do first** |
| Self-observation/evolution | Not explicitly proposed (future wave) | Phase 2: Evolution Constellation (System Observer, Performance Analyzer) | **Later** |
| Model routing/benchmarking | Not proposed (future) | Phase 3: Model Router + Benchmark Constellation | **Later** |
| Domain deployment (TBP) | Move 7: Host Binding Strategy | Phase 4: Domain Adapter → Birth Pool Business Vault | **Later** |
| Tool Interface / Execution Adapters | Implicit in workflow engine | Detailed tool layer design (tool registry, execution adapters, approved tools only) | **Design now, build later** |

## Where They Disagree (And Resolution)

**1. System Kernel vs. CLAUDE.md**

ChatGPT proposes creating `AGENT_MAESTRO_KERNEL.md` as a new "bootloader" file agents read first. However, the vault already has a root `CLAUDE.md` that serves this exact purpose — it defines the vault structure, four-layer model, agent permissions, and escalation rules. It also has 21 system maps, governance indexes, and navigation documents.

**Resolution**: Don't create a separate kernel file. Instead, upgrade the existing `CLAUDE.md` to be more machine-operable (add explicit file paths, registry locations, and a decision tree for "what to read first"). Create a single consolidated `SYSTEM_MAP.md` that indexes all 21 maps with a hierarchical navigation tree. This gives agents the "instant navigability" ChatGPT calls for without duplicating what exists.

**2. Agent Registry — New File vs. Existing CSVs**

ChatGPT proposes `AGENT_REGISTRY.md` as a markdown file. We already have `constellation_registry.csv` and `authority_pack_registry.csv` which together serve this purpose.

**Resolution**: Create a unified `agent_registry.csv` that combines agent identity, role, constellation, allowed/forbidden actions, and authority pack reference. This is more machine-readable than markdown and consistent with our existing CSV-based registries.

**3. Memory Layer Registry**

ChatGPT proposes `MEMORY_REGISTRY.md` documenting memory types (Concepts, Patterns, Domains, References, etc.). This is a good idea that doesn't currently exist in a consolidated form.

**Resolution**: Create as a vault note in `02_KNOWLEDGE/system_maps/`. Low effort, high clarity.

**4. Governance Constellation (New) vs. Governance Executive (Existing)**

ChatGPT proposes a new Governance Constellation with Contract Validator, Architecture Compliance Auditor, and Pipeline Validator agents. We already have a Governance Executive in the Executive Layer.

**Resolution**: Defer full Governance Constellation to Wave 5+. For now, the Governance Executive + vault_maintenance constellation cover the essential compliance functions. Flag this as a future build once the workflow engine can actually execute constellations.

**5. Tool Interface Layer**

ChatGPT provides detailed design for a tool registry + execution adapters pattern (agents call approved tools, never run arbitrary code). Claude's proposal has this implicit in the workflow engine but doesn't formalize it.

**Resolution**: Design the Tool Interface specification as part of the workflow engine build. Agents interact with the vault through a defined set of tool functions (read_note, write_note, move_note, run_audit, etc.) rather than arbitrary file operations. This aligns with both proposals and the existing GovernedAgent pattern.

---

## Build Plan

### Phase A: Foundation Hardening (Sessions 4-5)

Everything in this phase fixes things that are broken or missing. No new features — just making what exists trustworthy and navigable.

#### Session 4: Safety + Git Setup

| # | Item | Source | Effort |
|---|------|--------|--------|
| A1 | **Fix permission substring bypass** — Replace partial match in `check_permission()` with exact match + explicit alias support | Claude audit C1 | Small |
| A2 | **Implement control gate enforcement** — Evaluate gate conditions before action execution; block or escalate per `on_fail` directive | Claude audit C2 | Medium |
| A3 | **Add evidence requirement validation** — Check evidence file existence before `attempt_action()` | Claude audit C3 | Medium |
| A4 | **Fix compiler registry sync** — Compiler appends instead of resetting; back-fill 15 missing artifact entries | Claude audit C4 | Small |
| A5 | **Fix 17 stale path references** — Find-and-replace old session paths across vault | Claude audit C5 | Small |
| A6 | **Initialize Git repo + .gitignore** — Set up version control for the vault | Claude Move 2 | Small |
| A7 | **Create GitHub repo (private)** — Push as v0.2.0 with release notes | Claude Move 2 | Small |
| A8 | **Add Git/Release step to Build Session Protocol** — Standardize commit + tag + push at end of every build | Claude Move 2 | Small |

**Exit criteria**: All 26 tests pass. Permission bypass is impossible. Control gates block when they should. Git history begins.

#### Session 5: Agent Navigability

| # | Item | Source | Effort |
|---|------|--------|--------|
| B1 | **Create consolidated SYSTEM_MAP.md** — Single hierarchical index of all 21 system maps, all registries, all constellations, all pipelines. Agents read this first. | ChatGPT #1 | Medium |
| B2 | **Upgrade root CLAUDE.md** — Add explicit file paths, decision tree ("if you need X, read Y"), registry locations. Make it a proper machine-operable bootloader. | ChatGPT Kernel idea, adapted | Medium |
| B3 | **Create agent_registry.csv** — Unified registry: agent_id, name, role, constellation, purpose, allowed_actions (summary), forbidden_actions (summary), authority_pack_id, status | ChatGPT #2 + Claude Move 5 | Medium |
| B4 | **Create Memory Layer Registry** — Document memory types, their purpose, canonical locations, and access patterns | ChatGPT #3 | Small |
| B5 | **Resolve vault_curator / vault_maintenance overlap** — Define clear domain boundaries, deprecate or merge vault_curator | Claude audit H3 + ChatGPT "single responsibility" | Medium |
| B6 | **Add vault_maintenance executive authority pack** — Complete the three-level hierarchy (executive → supervisor → specialist) | Claude audit H4 | Small |

**Exit criteria**: An agent can read SYSTEM_MAP.md + CLAUDE.md and know exactly where everything is. No overlapping constellation authority. All agents registered in one place.

### Phase B: Executable System (Sessions 6-8)

This phase transforms Agent Maestro from "well-governed definitions" into "agents that actually do things."

#### Session 6: Workflow Engine Core

| #   | Item                                                                                                                                                                  | Source             | Effort |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------ |
| C1  | **Design Tool Interface specification** — Define the approved tool set (read_note, write_note, move_note, run_audit, generate_report, etc.) with input/output schemas | ChatGPT Tool Layer | Medium |
| C2  | **Create workflow_engine.py** — Loads pipeline definitions from 03_PIPELINES, maps stages to agent actions via tool interface                                         | Claude Move 3      | Large  |
| C3  | **Implement stage-to-agent mapping** — Translate workflow stages into `attempt_action()` calls through the tool interface                                             | Claude Move 3      | Medium |
| C4  | **Add result aggregation** — Collect outputs between stages, handle conditional branching, pass context forward                                                       | Claude Move 3      | Medium |

**Exit criteria**: Workflow engine can load a pipeline definition and execute it against real agents with tool-mediated actions.

#### Session 7: Workflow Integration + First Real Run

| # | Item | Source | Effort |
|---|------|--------|--------|
| D1 | **Integrate workflow engine into orchestrator** — New `orchestrator.py run --execute` mode | Claude Move 3 | Medium |
| D2 | **End-to-end integration test** — Run vault_maintenance audit cycle against real vault notes, produce real CSV reports | Claude Move 3 | Large |
| D3 | **Make state change logger mandatory** — Call `log_state_change()` automatically from all modification paths | Claude audit M1 | Small |
| D4 | **Add compiled artifact format documentation** — JSON Schema for compiled packs | Claude audit M2 | Small |

**Exit criteria**: `python orchestrator.py run vault_maintenance --execute` runs a full audit cycle and produces reports. State changes logged. First real output from the system.

#### Session 8: Escalation Handler + Human Review

| # | Item | Source | Effort |
|---|------|--------|--------|
| E1 | **Create escalation_processor.py** — Monitor escalation_log.csv, group by recipient, present for review | Claude Move 4 | Medium |
| E2 | **Human review queue** — Markdown-based approval queue in 06_EXECUTION/ (simple, practical, vault-native) | Claude Move 4 | Medium |
| E3 | **Approval → Resume pipeline** — Mechanism for approved escalations to unblock paused workflows | Claude Move 4 | Large |
| E4 | **Escalation dashboard** — Summary view of pending/approved/rejected escalations | Claude Move 4 | Small |

**Exit criteria**: When an agent hits an escalation, a human can review it in the vault and approve/reject. Approved escalations resume the workflow.

### Phase C: First Real Workload (Session 9)

#### Session 9: Process 45 Unprocessed Notes

| #   | Item                                                                                                 | Source        | Effort |
| --- | ---------------------------------------------------------------------------------------------------- | ------------- | ------ |
| F1  | **Run Note Processor specialist against 01_CAPTURE** — Classify all captures by note type and domain | Claude Move 6 | Medium |
| F2  | **Enrich with schema v2 frontmatter** — Apply templates based on classification                      | Claude Move 6 | Medium |
| F3  | **Promote or archive** — Move to canonical locations or 99_ARCHIVE with full audit trail             | Claude Move 6 | Medium |
| F4  | **Full state change log** — Every promotion, archive, and modification tracked                       | Claude Move 6 | Small  |

**Exit criteria**: 01_CAPTURE inbox is empty (or contains only items that were escalated for human decision). Full audit trail in state_change_log.csv. This is the first real proof that the system works end-to-end.

### Phase D: Architecture Design (Session 10)

#### Session 10: Execution Architecture + Host Binding

| #   | Item                                                                                                                                                                    | Source                           | Effort   |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | -------- |
| G1  | **Document execution architecture** — Formalize the three-layer model: Reasoning (LLM) → Tool Interface → Execution Adapters → External World                           | ChatGPT Execution Layer          | Medium   |
| G2  | **Design Tool Registry** — Vault-native registry of all approved tools with schemas, permissions, and adapter bindings                                                  | ChatGPT Tool Layer               | Medium   |
| G3  | Prototype one external integration — E.g., Slack DM via MCP through a GovernedAgent with tool interface                                                                 | Claude Move 7                    | Medium   |
| G4  | **Evaluate host options** — Claude sessions vs. Python daemon vs. n8n vs. hybrid. Document trade-offs and recommend.                                                    | Claude Move 7 + ChatGPT addendum | Research |
| G5  | **Design Self-Observation specification** — Define what agents should log about their own performance (errors, latency, confidence distributions, pipeline bottlenecks) | ChatGPT Evolution Constellation  | Medium   |

**Exit criteria**: Execution architecture documented. Tool registry designed. One working external integration. Host binding recommendation made. Self-observation spec ready for future implementation.

---

## Explicitly Deferred (Wave 5+)

These items are valuable but depend on Phases A-D being solid first:

| Item | Source | Why Deferred |
|------|--------|-------------|
| Governance Constellation (Contract Validator, Architecture Compliance Auditor) | ChatGPT Phase 2 | Governance Executive + vault_maintenance cover essentials; full constellation after workflow engine works |
| Evolution Constellation (System Observer, Performance Analyzer, Improvement Recommender) | ChatGPT Phase 2 | Requires self-observation data which requires the system to be running first |
| Model Router + Benchmark Constellation | ChatGPT Phase 3 | Interesting but premature; current system uses one model (Opus) effectively |
| Domain Deployment / TBP Business Agents | ChatGPT Phase 4 + Claude Move 7 | Agent Maestro must work end-to-end on its own vault before deploying elsewhere |
| Multi-Vault Agent Networks | ChatGPT Future #1 | Requires domain deployment to work first |
| AI System Replication (generate agent systems from domain descriptions) | ChatGPT Future #3 | Aspirational; requires everything else to be proven |
| Portable Agent OS | ChatGPT Phase 5 | Interesting long-term goal; premature to engineer for portability before the system runs reliably in one place |

---

## Versioning Plan

| Version | After Session | Milestone |
|---------|---------------|-----------|
| v0.2.0 | Session 4 | First Git release — Waves 1-3 complete |
| v0.2.1 | Session 5 | Safety hardened + agent navigability |
| v0.3.0 | Session 7 | Workflow engine works end-to-end |
| v0.3.1 | Session 8 | Escalation handler + human review loop |
| v0.3.2 | Session 9 | First real workload processed (45 notes) |
| v0.4.0 | Session 10 | Execution architecture + first external integration |

---

## Session Sequence Summary

```
Session 4:  Safety hardening + Git/GitHub setup              [Phase A]
Session 5:  Agent navigability + constellation consolidation  [Phase A]
Session 6:  Workflow engine core + tool interface design      [Phase B]
Session 7:  Workflow integration + first real E2E run         [Phase B]
Session 8:  Escalation handler + human review loop            [Phase B]
Session 9:  Process 45 unprocessed notes (real workload)      [Phase C]
Session 10: Execution architecture + host binding strategy    [Phase D]
```

**Total sessions**: 7
**Current session count**: SES-003
**Target completion**: SES-010

---

## What Success Looks Like After v0.4.0

At the end of this brief, Agent Maestro will be:

1. **Safe** — Permission checking is airtight. Control gates enforce. Evidence is validated. No bypass possible.
2. **Navigable** — Any agent (or human) can read two files (SYSTEM_MAP.md + CLAUDE.md) and know exactly where everything is and how to proceed.
3. **Executable** — `python orchestrator.py run vault_maintenance --execute` runs a real audit cycle. Workflows execute. Results are produced.
4. **Auditable** — Git history from day one. State change logs. Escalation trails. Release notes for every version.
5. **Human-in-the-loop** — Escalations reach humans. Approvals flow back. The system pauses safely when uncertain.
6. **Proven** — 45 real notes processed end-to-end through the full pipeline. Not theoretical — demonstrated.
7. **Ready for growth** — Tool interface designed. Execution architecture documented. First external integration working. Self-observation specification ready. The path to domain deployment (TBP) and model routing is clear.

The system will have crossed the threshold from *knowledge architecture* to *operational intelligence system* — which is the whole point of Agent Maestro.

---

**Awaiting approval before any build work begins.**
