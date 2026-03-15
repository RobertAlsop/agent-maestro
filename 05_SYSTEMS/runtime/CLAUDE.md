# Runtime Engine — Governance

**Foundations Alignment**: The runtime engine implements the Authority seed and Law 3 (control over all agent actions), providing the governance mediation layer that enforces authority constraints at execution time.

## Purpose
This directory contains the Agent Maestro runtime engine — the Python system that allows governed agents to execute operations.

## Components
- **governed_agent.py**: GovernedAgent base class — loads compiled authority packs, checks permissions, logs actions
- **agent_runtime.py**: AgentRuntime class — manages agent lifecycle, runs workflows, generates cycle reports
- **test_runtime.py**: Test suite (15 tests covering permission checking, logging, workflows)

## How It Works
1. A compiled authority pack JSON is loaded at agent init
2. Before every action, permissions are checked: allowed → execute, denied → block, requires_escalation → log and block
3. All actions are logged to 06_EXECUTION/logs/task_execution_log.csv
4. All escalations are logged to 06_EXECUTION/logs/escalation_log.csv
5. Unknown actions default to REQUIRES_ESCALATION (fail-safe)

## Agent Rules
- Agents MUST load a compiled authority pack before executing any actions
- Agents MUST NOT bypass permission checking
- Agents MUST log all actions and escalations
- Agents MAY extend GovernedAgent with domain-specific methods
- Agents MUST NOT modify their own authority packs at runtime

## Created
Session SES-004, 2026-03-14, Wave 2 (Upgrade 2.2)
