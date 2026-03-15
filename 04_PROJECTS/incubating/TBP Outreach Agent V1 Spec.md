---
schema_version: 2
title: "TBP Outreach Agent V1 Spec"
type: project
note_class: planning
domain: agent_maestro
layer: projects
authority_weight: 55
status: incubating
review_status: draft
version: 1
created_date: 2026-03-15
last_modified: 2026-03-15
source_type: ai_authored
relationships:
  defines: []
  part_of:
    - "[[Agent Maestro — Evolution Roadmap v0.2]]"
  implements: []
  governs: []
  inherits_from: []
  applies_to:
    - "[[Agent Constellation]]"
  uses:
    - "[[Authority Pack]]"
  produces: []
tags:
  - project
  - incubating
  - tbp
  - outreach
  - agent_deployment
project_status: incubating
deferred_until: "v0.4.0"
deferred_reason: "Domain deployment deferred per Build Brief: Agent Maestro must work end-to-end on its own vault before deploying elsewhere. See Phase D (Session 10+)."
---

# TBP Outreach Agent V1 Spec

## Status

**INCUBATING — Deferred to Phase D (v0.4.0+)**

Per [[Agent Maestro v0.3 — Build Brief]], TBP domain deployment is explicitly deferred until Agent Maestro works end-to-end on its own vault. This spec is preserved here for future activation.

## Purpose

Process a referral/outreach contact, generate the correct outreach email, validate it, present it for approval, then update system state and log the outcome.

## V1 Scope

**Includes:**
- One outreach workflow
- One contact at a time
- First outreach email only
- Human approval before send
- State update after send
- Event logging for every step

**Excludes:**
- Autonomous sending
- Reply handling
- Multi-agent handoffs
- Self-improving prompts
- Complex vector retrieval

## Core Flow

```
Trigger
→ Load contact/state
→ Build context pack
→ Generate decision + draft
→ Validate
→ Human approve / reject
→ Send email
→ Update state
→ Log outcome
```

## System Components

### A. Input Gateway
Receives the task (manual trigger from outreach table, or "ready_to_process" row in database). Output artifact: `task_packet`.

### B. State Store
Authoritative live truth: contacts, organizations, outreach status, sent dates, next action date, assigned language, notes.

### C. Context Builder
Inputs: contact row, organization row, prior outreach status, approved email template/components, tone/policy instructions. Output artifact: `context_pack`.

### D. Decision + Draft Engine (LLM)
Produces: outreach classification, language choice, draft subject, draft body, recommended next action, confidence/review flag. Output artifact: `draft_proposal`.

### E. Validation Layer
Checks: required fields present, no duplicate send, valid contact status, approved template family, language present, placeholders resolved, email safe to review. Output artifact: `validation_report`.

### F. Human Control Point
Operator chooses: approve / reject / edit externally and re-run / defer. Output artifact: `approval_decision`.

### G. Tool Executor (if approved)
Send email, update outreach status, create follow-up date/task, store sent timestamp. Output artifact: `execution_result`.

### H. Event Log (append-only)
Records: task created, context built, draft generated, validation passed/failed, approved/rejected, sent/not sent, state updated. Output artifact: `event_record`.

## Five Control Points

1. **Trigger eligibility** — only process contacts where: contact exists, email exists, status = ready, not already sent first outreach
2. **Validation gate** — no approval step unless validation passes
3. **Human approval** — no send without explicit approval
4. **Post-send state update** — mark first outreach sent, save sent date, assign follow-up date, log event
5. **Failure halt** — if send fails: do not advance status, log failure, flag for manual review

## Authority Model

| Authority Type | Location | Purpose |
|----------------|----------|---------|
| Conceptual | Obsidian / design docs | Outreach logic, tone, categories |
| Operational | Database | What is true now |
| Decision | LLM | Classification and draft proposal |
| Execution | Python tools / API | Actually sends and updates |
| Governance | Validation rules + approval gate + event logging | Determines what is allowed |

## Canonical Artifacts

**Declarative:** `outreach_policy.md`, `email_template_spec.md`, `draft_rules.json`, `status_transition_rules.json`

**Executable:** `build_context_pack.py`, `generate_outreach_draft.py`, `validate_outreach_draft.py`, `send_outreach_email.py`, `log_outreach_event.py`

**Runtime (per run):** `task_packet.json`, `context_pack.json`, `draft_proposal.json`, `validation_report.json`, `approval_decision.json`, `execution_result.json`, `event_log.jsonl`

## V1 Success Criteria

V1 is successful when it can reliably:
- Process a valid contact
- Generate a usable outreach draft
- Block invalid drafts
- Require approval before send
- Send successfully after approval
- Update status correctly
- Produce a complete event trail

## One-Sentence Definition

**TBP Outreach Agent V1 is a human-approved outreach workflow that turns a valid contact record into a validated sent email plus a fully logged state transition.**

## Relationships

- [[Agent Maestro v0.3 — Build Brief]] — governs the deferral decision
- [[Agent Constellation]] — the constellation pattern this implements
- [[Authority Pack]] — the governance mechanism to be applied
