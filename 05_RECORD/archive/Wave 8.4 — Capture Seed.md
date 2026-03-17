---
title: "Wave 8.4 — Capture Seed"
type: log
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 8.3 — Reflection]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Git Conventions]]"
    - "[[AM — Future Waves Register]]"
tags: [capture-seed, wave-8, git-ops, automation]
---

# Wave 8.4 — Capture Seed

From [[Wave 8.3 — Reflection]].

## The Question

Wave 8.3 proved AM can detect when its git conventions are not being followed. Wave 8.4's question: **can AM prevent violations and automate the correct workflow?**

Detection without action requires human follow-up on every finding. Automation closes the loop: correct workflow happens automatically, violations are blocked at the point of action, not discovered after the fact.

## What Wave 8.3 Surfaced

The first run of `git_hygiene.py` produced 11 findings and 23 warnings, all real:

- All historical master commits are direct (no merge commits). The full history predates the branching convention. This is the primary behavioural gap — branches exist but the workflow hasn't been using them for master integration.
- Five branches use pre-convention naming schemes. Historical drift.
- Five completed waves have no pre-wave checkpoint tags. Historical gap — tags were not part of the workflow when those waves were built.

The detection tool is now producing real signal. The next question is what to do with it.

## Two Candidate Directions

**Direction 1 — Pre-commit hooks (prevention):**
Block non-conforming commits at write time. Enforce branch naming before a commit lands. Enforce commit message format before the commit is recorded. Lives in `.git/hooks/` (not tracked). Different trust boundary from detection — a false positive blocks workflow rather than appearing in a report.

**Direction 2 — Git workflow automation (action-taking tools):**
Automate the correct wave git sequence: `pre-wave-X.Y` tag creation, branch creation and naming, `orchestrate.sh` invocation at merge gate, version tag creation after wave completion. Requires "Action Tool Conventions" governance extension — the existing Tool Conventions cover read-only detection tools; action-taking tools need their own safety rules.

## What Needs to Be Decided

1. **Scope for Wave 8.4**: prevention hooks, workflow automation, or both? The proposal should define scope against available bandwidth and value.
2. **Action Tool Conventions**: before building any action-taking tool, the governance layer needs to specify what safeguards an action tool must have (undo path, confirmation model, dry-run mode, escalation triggers). This may be the most important output of a Wave 8.4 design session.
3. **Historical debt resolution**: the 11 findings from Wave 8.3's first run are not urgent, but they need a human decision. Branch renames/deletes (Level 2), tag deletion (Level 3), documentation of historical-state findings.

## Stage 1 Exit Assessment

Wave 8.3 was the last planned Stage 1 wave. Before designing Wave 8.4, evaluate Stage 1 exit criteria against [[AM — Strategy]]:
- Structural integrity: ✓ (Wave 6)
- Process compliance: ✓ (Wave 8.2)
- Git hygiene: ✓ (Wave 8.3)

If Stage 1 exit criteria are met, Wave 9 (Self-Observation) is the correct next wave — not 8.4. Wave 8.4 can remain in the register and follow after Wave 9 if the evidence base from self-observation confirms the need.
