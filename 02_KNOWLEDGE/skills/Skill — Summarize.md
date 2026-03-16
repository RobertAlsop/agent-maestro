---
title: "Skill — Summarize"
type: skill
status: active
authority_weight: 60
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from: ["Agent Maestro — Foundations"]
  governs: []
  related: ["Skill — Gate", "Skill — Escalate"]
tags: [skill, summarize, record, session, log]
---

## Purpose

Summarize synthesizes outcomes and creates records. It answers: **what happened, and what matters?** Every significant pipeline action produces a record. Records are how the system remembers.

## Pipeline Stages Served

RECORD (primary). Also used at the end of any significant action that needs to be remembered.

## When to Apply

- End of a build session
- Completion of a gate decision
- Conclusion of an audit
- Completion of a workflow
- Any decision that future agents will need to understand

## What to Capture

A good summary captures:

1. **What was done** — The actions taken. Concrete and specific.
2. **What was decided** — Any decisions made, with the reasoning that led to them.
3. **What changed** — Files created, moved, modified, or deleted.
4. **What was deferred** — Anything that came up but was not acted on. Why.
5. **What's next** — The logical next action, if apparent.

The summary is NOT an exhaustive transcript. Apply Law 3: minimum viable record.

## Record Types

| Type | Content | Location |
|------|---------|----------|
| Session log | What happened in a build session | `05_RECORD/logs/sessions/` |
| Gate log | Gate decision + reasoning | `05_RECORD/logs/` |
| Audit report | Audit findings and recommendations | `05_RECORD/reports/` |
| State change log | Structural vault changes | `05_RECORD/logs/` |
| Workflow report | Runtime workflow execution results | `05_RECORD/reports/` |

## Naming Convention

- Session logs: `Session Log — SES-XXX — YYYY-MM-DD.md`
- Reports: `[type]_report_[session/date].md` or `.json` for machine-readable output
- Gate logs: appended to `05_RECORD/logs/state_change_log.csv` (structured) or session log (narrative)

## Process

1. Collect the inputs: actions taken, decisions made, artifacts changed.
2. Draft the summary using the five capture elements above.
3. Write to the appropriate record location.
4. Update `05_RECORD/logs/state_change_log.csv` if structural changes were made.

## Output

A record document in `05_RECORD/` conforming to schema v3 with type: log or report.
