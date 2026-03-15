---
schema_version: 2
title: "Host Options Evaluation"
type: reference
note_class: evaluation
domain: agent_maestro
layer: knowledge
canonical: true
authority_weight: 70
resolution_basis: authority_weight
status: active
review_status: approved
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
owner: AgentMaestro
source_type: ai_authored
relationships:
  defines:
    - "[[Host Binding Strategy]]"
  part_of:
    - "[[Execution Architecture]]"
  implements:
    - "[[Agent Maestro — Strategy]]"
  uses:
    - "[[Host Bindings]]"
  produces: []
supersedes: []
superseded_by: []
tags:
  - reference
  - evaluation
  - host-options
  - phase-d
  - v0.4
hash: ""
---

# Host Options Evaluation

## Purpose

This document evaluates the viable options for hosting Agent Maestro's runtime — the environment where the Reasoning Layer (LLM) is invoked, the governance pipeline runs, and tools execute. The goal is to recommend the best hosting strategy for taking Agent Maestro from prototype to operational system.

## The Hosting Problem

Agent Maestro's runtime currently consists of Python modules (`governed_agent.py`, `workflow_engine.py`, `tool_interface.py`, `orchestrator.py`) that execute locally. But these modules need an LLM to drive the Reasoning Layer — something must decide *what actions to take* within the governance boundaries.

The hosting question is: **Where and how does the LLM-powered reasoning happen, and how does it connect to the Python governance runtime?**

## Options Evaluated

### Option 1: Claude Code / Claude Desktop Sessions

**How it works:** A human opens Claude Code (or Claude Desktop with Cowork mode), which has access to the vault directory. Claude reads the vault, understands the governance structure, and executes commands through the orchestrator CLI or directly through Python.

**Architecture:**
```
Human → Claude Code/Desktop → reads vault → calls orchestrator.py → GovernedAgent → Tools → Vault
```

**Strengths:**
- Already working — this is how all builds (SES-001 through SES-010) have been executed
- Claude has full context of the vault through CLAUDE.md, SYSTEM_MAP.md, and authority packs
- MCP integration is native — Claude Code already supports MCP servers
- Human-in-the-loop is natural — the human is right there
- No infrastructure to maintain — Anthropic hosts the LLM
- Rich reasoning capabilities — Claude can handle complex decisions, not just rule-following

**Weaknesses:**
- Session-based — no persistent daemon; agent work requires a human to start a session
- Context window limits — very large vaults may exceed context
- No scheduling — cannot run automated workflows on a timer
- Cost scales with usage — each session uses API tokens
- No parallel execution — one session at a time (unless multiple windows)

**Best for:** Design work, complex governance decisions, build sessions, ad-hoc analysis — anything that benefits from human oversight and rich reasoning.

### Option 2: Python Daemon

**How it works:** A long-running Python process that monitors the vault, runs scheduled workflows, and calls an LLM API for reasoning when needed. The daemon uses the existing runtime modules directly.

**Architecture:**
```
Cron/systemd → Python daemon → LLM API call → GovernedAgent → Tools → Vault
                    ↑
              watches vault for triggers
```

**Strengths:**
- Autonomous — can run scheduled workflows (audit cycles, maintenance) without human presence
- Uses existing Python runtime directly — no translation layer
- Can implement event triggers (file change → run workflow)
- Full control over execution — retries, queuing, parallelism
- Can aggregate results over time (self-observation, metrics)

**Weaknesses:**
- Requires infrastructure — server/VM to run, process management, monitoring
- LLM reasoning is thinner — API calls are stateless; no persistent context window
- Security surface — a daemon with vault access needs careful sandboxing
- Error handling complexity — unattended failures need alerting
- Custom code for scheduling, queuing, retry logic

**Best for:** Scheduled maintenance, automated audits, background monitoring — anything repetitive that doesn't need human judgment for each decision.

### Option 3: n8n (or Similar Workflow Platform)

**How it works:** n8n (or Zapier, Make, Temporal, etc.) orchestrates workflows visually. Each workflow stage maps to an n8n node that calls the Python runtime or an LLM API. The governance layer runs within custom nodes.

**Architecture:**
```
n8n trigger → n8n workflow → custom node (Python) → GovernedAgent → Tools → Vault
                                ↑
                          LLM API node for reasoning
```

**Strengths:**
- Visual workflow editor — non-developers can inspect and modify workflows
- Built-in scheduling, retry, and error handling
- Pre-built integrations — Slack, GitHub, email, databases
- Event-driven triggers (webhooks, file watchers, cron)
- Execution history and monitoring out of the box

**Weaknesses:**
- Translation overhead — YAML workflow definitions must be re-expressed as n8n flows
- Governance split — some governance runs in n8n nodes, some in Python; hard to keep consistent
- Dependency on external platform — n8n needs hosting and maintenance
- Limited reasoning — n8n nodes are procedural; complex LLM reasoning requires workarounds
- Double governance risk — n8n has its own permission model that may conflict with Agent Maestro's
- Vendor lock-in on workflow definitions

**Best for:** Teams that want a visual interface for workflow management and need pre-built external integrations. Less ideal for Agent Maestro's governance-first architecture.

### Option 4: Hybrid (Recommended)

**How it works:** Combine Claude sessions for complex reasoning work with a lightweight Python daemon for scheduled/automated tasks. The vault is the shared state between both modes.

**Architecture:**
```
Interactive mode:
  Human → Claude Code/Desktop → vault → orchestrator.py → full reasoning

Autonomous mode:
  Scheduler → Python daemon → vault → orchestrator.py → LLM API (for reasoning)
                                                        → or rule-based (for simple tasks)
```

**Strengths:**
- Best of both worlds — rich reasoning for complex work, automation for routine tasks
- Graceful degradation — if the daemon encounters something complex, it escalates to the next Claude session
- Vault is the single source of truth — both modes read/write the same vault
- Incremental adoption — start with Claude sessions (already working), add daemon later
- Matches the escalation model — daemon handles ALLOWED actions; complex decisions get REQUIRES_ESCALATION → human reviews in next Claude session

**Weaknesses:**
- Two systems to maintain (though they share the same Python runtime)
- Coordination via vault state (not real-time) — daemon and Claude sessions communicate through escalation_log.csv and state_change_log.csv
- Need to define which workflows are "daemon-safe" vs "session-required"

**Best for:** Agent Maestro's actual use case — a system that needs both complex reasoning (design, governance, architecture) and routine automation (audits, maintenance, monitoring).

## Evaluation Matrix

| Criterion | Claude Sessions | Python Daemon | n8n | Hybrid |
|-----------|:-:|:-:|:-:|:-:|
| Already working | **Yes** | No | No | Partially |
| Rich LLM reasoning | **Excellent** | Limited | Limited | **Excellent** (interactive) |
| Autonomous scheduling | No | **Yes** | **Yes** | **Yes** (daemon mode) |
| Governance consistency | **Native** | **Native** | Risky | **Native** |
| Infrastructure overhead | None | Medium | High | Low-Medium |
| Human-in-the-loop | **Natural** | Manual | Manual | **Natural** (interactive) |
| External integrations | Via MCP | Custom | **Built-in** | Via MCP + custom |
| Scalability | Session-bound | Good | Good | Good |
| Time to production | **Now** | 2-3 sessions | 4-5 sessions | **1-2 sessions** |

## Recommendation

**Primary recommendation: Hybrid (Option 4)**, implemented in two phases:

**Phase 1 (Current — v0.4.0):** Continue using Claude sessions (Code/Desktop/Cowork) as the primary execution host. This is already working and provides the richest reasoning capabilities. The MCP adapter (G3) enables external integrations within this mode.

**Phase 2 (Future — v0.5.0+):** Add a lightweight Python daemon for scheduled workflows. The daemon should:

1. Run on a schedule (cron or systemd timer)
2. Execute only workflows tagged as `daemon_safe: true` in their YAML definitions
3. Use rule-based execution for simple stages (no LLM needed for "scan directory" or "validate frontmatter")
4. Call an LLM API only when a stage requires actual reasoning (classification, analysis)
5. Escalate anything complex to the escalation queue for the next human session
6. Log all actions through the existing governance pipeline

**Key principle:** The daemon is a supplement, not a replacement. Complex work (design, architecture, governance changes, novel decisions) stays in interactive Claude sessions. The daemon handles the "boring but important" work — scheduled audits, compliance scans, routine maintenance.

### Implementation Guidance for the Daemon

When building the daemon (v0.5.0+), the recommended approach is:

```python
# Conceptual daemon structure
class AgentMaestroDaemon:
    def __init__(self, vault_path, config_path):
        self.engine = WorkflowEngine(vault_path)
        self.engine.load_agents("vault_maintenance")
        self.engine.load_all_workflows()

    def run_scheduled(self):
        """Run all daemon-safe workflows."""
        for wf_id, defn in self.engine.definitions.items():
            if defn.metadata.get("daemon_safe"):
                status, context = self.engine.execute(wf_id)
                if status == WorkflowStatus.PAUSED:
                    # Escalation raised — leave for human review
                    self.log_escalation_summary(context)

    def run_once(self, workflow_id):
        """Run a single workflow."""
        return self.engine.execute(workflow_id)
```

This daemon would reuse the entire existing runtime — `GovernedAgent`, `WorkflowEngine`, `tool_interface`, state change logging — with no new governance code.

## Host Binding Integration

The Host Bindings system (`05_SYSTEMS/authority_architecture/compiler/Host Bindings.md`) was designed to associate compiled governance artifacts with specific runtime environments. The hybrid approach maps to host bindings as follows:

| Host Binding | Runtime | Governance Source |
|-------------|---------|------------------|
| `host.claude_session` | Claude Code/Desktop/Cowork | Compiled JSON pack loaded by GovernedAgent |
| `host.python_daemon` | Python daemon process | Same compiled JSON pack |
| `host.mcp_bridge` | MCP adapter within either host | Same governance; MCP config from mcp_servers.yaml |

The key insight is that the governance model is host-agnostic. The same compiled authority pack governs an agent whether it's running in a Claude session or a Python daemon. Only the Reasoning Layer differs — Claude provides rich reasoning; the daemon uses simpler rule-based or API-call reasoning.

## Related Documents

- [[Execution Architecture]] — `02_KNOWLEDGE/concepts/Execution Architecture.md`
- [[Host Bindings]] — `05_SYSTEMS/authority_architecture/compiler/Host Bindings.md`
- [[Agent Maestro — Strategy]] — `02_KNOWLEDGE/governance/Agent Maestro — Strategy.md`
- [[Integration Manifest]] — `05_SYSTEMS/authority_architecture/compiler/Integration Manifest.md`
