---
schema_version: 2
title: "Agent Maestro v0.3 — Next Moves Proposal"
type: proposal
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 70
status: draft
review_status: draft
version: 1
created_date: 2026-03-14
last_modified: 2026-03-14
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
  - proposal
  - roadmap
  - wave-4
  - adversarial-audit
supersedes: []
superseded_by: []
hash: null
owner: null
resolution_basis: authority_weight
---

# Agent Maestro v0.3 — Next Moves Proposal

**Date**: 2026-03-14
**Author**: Claude (Opus) + Rob
**Status**: DRAFT — Awaiting Approval
**Scope**: Post-Wave 3 priorities based on adversarial audit + strategic direction

---

## Part 1: Adversarial Audit Summary

Before proposing next moves, a full adversarial audit was conducted across the vault. The findings inform the priorities below.

### Critical Findings (Must Fix)

**C1. Partial Match Bypass in Permission Checking** — The `check_permission()` method in `governed_agent.py` uses substring matching that can accidentally grant permissions. An agent attempting "read note and delete related files" would match against "read note" and be allowed. The fail-safe (unknown → escalate) is bypassed.

**C2. Control Gates Are Advisory Only** — All control gates defined in authority packs (e.g., "no more than 50 changes per cycle") are loaded but never enforced. The `check_control_gates()` method marks everything "advisory" regardless of the `on_fail` directive (block/escalate).

**C3. Evidence Requirements Never Validated** — Authority packs define required evidence (audit reports, CSVs) but the runtime never checks whether evidence exists before allowing actions.

**C4. Compiler Artifacts Registry Out of Sync** — Only 1 of 16 compiled artifacts is registered. The compiler resets the registry on each run instead of appending. Historical compilation data is lost.

**C5. 17 Files Reference Stale Vault Path** — Root CLAUDE.md and 16 other files still reference `/sessions/loving-busy-bohr/mnt/Agent Maestro/` from the original session.

### High-Priority Findings

**H1. No End-to-End Workflow Execution** — The orchestrator performs dry-run authority checks but has no mechanism to actually execute workflows. Pipeline definitions in 03_PIPELINES are never invoked.

**H2. Escalation Logging Without Resolution** — Escalations write to CSV with status "pending" but nothing reads, processes, or resolves them. No human notification. No approval mechanism.

**H3. Vault Curator / Vault Maintenance Overlap** — Both constellations claim authority over schema validation and relationship auditing. No coordination mechanism exists. Concurrent execution could produce conflicting repairs.

**H4. No Constellation-Level Executive for Vault Maintenance** — The supervisor inherits directly from Knowledge Executive, skipping the constellation executive layer that vault_curator has.

### Medium-Priority Findings

**M1. State change logger integration is optional** — GovernedAgent works without it; `log_state_change()` is never called automatically from `attempt_action()`.

**M2. No compiled artifact format documentation** — No JSON Schema for compiled packs. Tooling that reads artifacts has no spec to validate against.

**M3. Scalability** — Orchestrator loads all artifact JSON files to display a list. Works fine now with 16 artifacts but will degrade at 250+.

---

## Part 2: Strategic Context

Based on the interview with Rob:

- **Goal**: All of the above — working system for personal AI workflows, potential product/service, AND reference architecture
- **Host system**: Undecided — open to suggestions (Claude sessions, Python runtime, or automation tools)
- **Integrations**: Multiple external systems (Apollo, Google Workspace, Airtable, Slack, etc.)
- **Build philosophy**: Governance foundation first, executable capability introduced step by step
- **New requirement**: Git/GitHub baked into every build session as standard practice

---

## Part 3: Proposed Next Moves (Prioritized)

The moves are ordered by leverage — each one multiplies the value of everything built so far.

### Move 1: Safety & Integrity Hardening

**Why highest leverage**: Everything downstream depends on the governance engine being trustworthy. If agents can accidentally bypass permissions, the entire authority architecture is undermined.

| Item | Description | Effort |
|------|-------------|--------|
| 1a. Fix permission substring bypass | Replace partial matching with exact match + explicit aliases | Small |
| 1b. Implement control gate enforcement | Evaluate gate conditions before action execution; block or escalate per on_fail | Medium |
| 1c. Add evidence requirement validation | Check evidence file existence before attempt_action() | Medium |
| 1d. Fix compiler registry sync | Compiler appends instead of resetting; back-fill 15 missing entries | Small |
| 1e. Fix stale path references | Find-and-replace across 17 files | Small |

**Estimated sessions**: 1

### Move 2: Git/GitHub Integration + Release Protocol

**Why high leverage**: Version control is foundational infrastructure. Every future build benefits from it. Enables collaboration, rollback, and release tracking.

| Item | Description | Effort |
|------|-------------|--------|
| 2a. Initialize repo, .gitignore, first commit | Set up repo structure with proper ignores | Small |
| 2b. Create GitHub repo (private) | Push initial codebase as v0.2.0 | Small |
| 2c. Define release protocol | Semantic versioning, release notes template, tag conventions | Small |
| 2d. Add Git/Release section to Build Session Protocol | Commit + tag + push as standard build session step | Small |
| 2e. Create v0.2.0 release with notes | First formal release covering Waves 1-3 | Small |

**Estimated sessions**: 1 (can combine with Move 1)

### Move 3: Workflow Execution Engine

**Why high leverage**: This is the bridge between "agents that are defined" and "agents that do things." Without it, the entire constellation + authority pack + pipeline infrastructure is theoretical.

| Item | Description | Effort |
|------|-------------|--------|
| 3a. Create workflow_engine.py | Loads pipeline definitions, maps stages to agent actions | Large |
| 3b. Implement stage-to-agent mapping | Translate workflow stages into attempt_action() calls | Medium |
| 3c. Add result aggregation | Collect outputs, pass between stages, handle conditional branching | Medium |
| 3d. Integrate with orchestrator | New `orchestrator.py run --execute` mode that uses workflow engine | Medium |
| 3e. End-to-end integration test | Orchestrator → Workflow → Agent → CSV output for one real audit | Large |

**Estimated sessions**: 2-3

### Move 4: Escalation Handler + Human Review Loop

**Why high leverage**: Closes the governance feedback loop. Without this, escalations are a dead end. With it, the system can safely operate with human-in-the-loop for high-risk decisions.

| Item | Description | Effort |
|------|-------------|--------|
| 4a. Create escalation_processor.py | Monitor escalation_log.csv, group by recipient | Medium |
| 4b. Human review interface | Markdown-based approval queue in 06_EXECUTION/ (start simple) | Medium |
| 4c. Approval → Resume pipeline | Mechanism for approved escalations to unblock agents | Large |
| 4d. Escalation dashboard | Summary view of pending, approved, rejected escalations | Small |

**Estimated sessions**: 2

### Move 5: Constellation Consolidation

**Why important**: vault_curator and vault_maintenance overlap creates confusion and potential conflicts. Consolidating or clearly separating their domains is necessary before deploying either.

| Item | Description | Effort |
|------|-------------|--------|
| 5a. Define domain separation rules | Clear boundaries: who owns schema, who owns relationships, who owns content | Medium |
| 5b. Create coordination authority pack | Cross-constellation coordination rules and mutex | Medium |
| 5c. Merge or deprecate vault_curator | Evaluate whether vault_curator should fold into vault_maintenance | Decision |
| 5d. Add vault_maintenance executive pack | Complete the three-level authority hierarchy | Small |

**Estimated sessions**: 1-2

### Move 6: Process the 45 Unprocessed Notes

**Why it matters now**: With a working workflow engine (Move 3), this becomes the first real test of the system. The Note Processor specialist was designed for exactly this.

| Item | Description | Effort |
|------|-------------|--------|
| 6a. Classify all 45 captures | Run Note Processor specialist against 01_CAPTURE | Medium |
| 6b. Enrich with schema v2 frontmatter | Apply templates based on classification | Medium |
| 6c. Promote or archive each item | Move to canonical locations or 99_ARCHIVE | Medium |
| 6d. Log all state changes | Full audit trail via state_change_logger | Small |

**Estimated sessions**: 1-2

### Move 7: Host Binding Strategy

**Why strategic**: Rob hasn't decided on the execution host yet. This move explores the options and makes a recommendation.

| Item | Description | Effort |
|------|-------------|--------|
| 7a. Document host binding options | Claude sessions, Python daemon, n8n, hybrid | Research |
| 7b. Prototype one external integration | E.g., Apollo contact lookup via MCP → GovernedAgent | Medium |
| 7c. Define host binding specification | How compiled packs bind to different host types | Medium |
| 7d. Recommend execution architecture | Based on prototyping results | Decision |

**Estimated sessions**: 2-3

---

## Part 4: Recommended Sequence

```
Session 4:  Move 1 (Safety Hardening) + Move 2 (Git/GitHub Setup)
Session 5:  Move 3a-3c (Workflow Engine Core)
Session 6:  Move 3d-3e (Workflow Integration + E2E Test)
Session 7:  Move 4 (Escalation Handler)
Session 8:  Move 5 (Constellation Consolidation)
Session 9:  Move 6 (Process 45 Notes — first real system test)
Session 10: Move 7 (Host Binding Strategy + Prototype)
```

**Total estimated sessions**: 7-10
**Version target**: v0.3.0 after Move 3, v0.4.0 after Move 7

---

## Part 5: What This Unlocks

After completing these moves, Agent Maestro will be:

1. **Safe** — Permission checking is airtight, control gates enforce, evidence is validated
2. **Executable** — Workflows actually run agents against the vault and produce real outputs
3. **Auditable** — Git history, state change logs, escalation trails, release notes
4. **Human-in-the-loop** — Escalations reach humans and approvals flow back to agents
5. **Tested** — First real workload (45 notes) processed end-to-end through the system
6. **Ready for external integration** — Host binding strategy chosen, first MCP integration prototyped

This transforms Agent Maestro from a governance framework into a working operational intelligence system.

---

**Awaiting approval before any build work begins.**
