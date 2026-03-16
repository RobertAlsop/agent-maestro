---
title: "AM — Universal Workflow"
type: governance
status: draft
authority_weight: 70
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Agent Maestro — Vault Rules]]"
  governs: []
  related:
    - "[[AM — Treatise on Core Principles]]"
    - "[[AM — Roadmap]]"
tags: [workflow, sop, protocol, pipeline, fractal]
---

# AM — Universal Workflow

## Purpose

Define how work happens in Agent Maestro. One pattern, applied at every scale. This document is the connective tissue between the pipeline structure (folders), the governance framework (rules), and the actual practice of doing work.

## Principle

There is one workflow: the Irreducible Loop (Seed 1). Everything in AM — from a single triage decision to a multi-session wave — is an instance of this loop. What changes between instances is scale, entry point, and intensity. The pattern itself never changes.

The extended derivation of why this is true lives in [[AM — Treatise on Core Principles]]. This document is operational — it tells you *how to work*, not why the pattern works.

---

## The Pattern

Every unit of work in AM follows six stages:

| Stage | Question | Pipeline Folder | What Happens |
|-------|----------|----------------|--------------|
| **Capture** | What arrived? | `01_CAPTURE` | Receive input — an idea, a problem, a request, an observation. |
| **Interpret** | What does it mean? | `02_KNOWLEDGE` | Understand the input against existing knowledge. Classify, contextualize, assess. |
| **Decide** | What are we going to do? | `03_DECIDE` | Commit to an action. Every decision passes through a gate — the intensity of the gate scales with the stakes. |
| **Execute** | Do it. | `04_EXECUTE` | Perform the action within the authority granted. |
| **Record** | What happened? | `05_RECORD` | Log the outcome — what was done, what changed, what was decided and why. |
| **Reflect** | What did we learn? | `06_REFLECT` | Evaluate the outcome. Identify what worked, what didn't, what's next. Feed forward into the next Capture. |

Between every stage: a **gate**. The gate checks whether the work is ready to move forward. Gate intensity scales with escalation level (see Intensity below).

The loop closes: Reflect feeds back into Capture. The reflection becomes the next seed.

---

## The Structural Checklist

Every workflow instance — at any scale — should address seven primitives (Seed 2: Structure). These are not stages; they are *what must be present* for the workflow to function:

| Primitive | Question | How It Shows Up |
|-----------|----------|----------------|
| **State** | What is true right now? | Current vault state, session context, the input itself. |
| **Goal** | What is this trying to achieve? | The purpose of the wave, the session objective, the task at hand. |
| **Policy** | What is allowed or forbidden? | Governance rules, authority limits, escalation thresholds. |
| **Memory** | What from the past informs the present? | Session logs, previous decisions, related knowledge, the roadmap. |
| **Tools** | What actions can be taken? | Available skills, shell scripts, LLM capabilities, the vault itself. |
| **Control** | Who decides and who can stop? | Role definitions, escalation levels, human sovereignty. |
| **Feedback** | How do we know if it worked? | Audit criteria, gate checks, reflection questions. |

You don't need to explicitly address all seven for every small task. But if something feels incomplete or stuck, checking the primitives will reveal what's missing.

---

## Scale

The same pattern operates at three scales. What changes is the artifacts produced, the duration, and the formality.

### Wave (largest)

A complete pipeline cycle with a proposal, build phases, and reflection. Produces a version increment.

| Stage | Wave Artifact |
|-------|--------------|
| Capture | Capture seed from previous wave's reflection |
| Interpret | Review seed, consult roadmap and register, assess context |
| Decide | Draft proposal → adversarial audit → human approval → promote to active |
| Execute | Work through phases, each with its own deliverables |
| Record | Session logs, state change logs, updated SYSTEM_MAP |
| Reflect | Reflection → capture seed for next wave |

### Session (medium)

A working conversation between participants. Produces a session log.

| Stage | Session Artifact |
|-------|-----------------|
| Capture | Read charter, load role, pick up where we left off |
| Interpret | Review current state — what's done, what's next, any new inputs |
| Decide | Agree on session scope — what we'll work on today |
| Execute | Do the work — build, review, triage, discuss |
| Record | Session log (SES-XXX) with decisions, changes, deferrals |
| Reflect | Quick check — did we achieve the session goal? What's next? |

### Task (smallest)

A single action or decision. May not produce a formal artifact — but the pattern still applies.

| Stage | Task Expression |
|-------|----------------|
| Capture | Notice or receive the input (an idea, a file to triage, a question) |
| Interpret | Understand it — what kind of thing is this? What's relevant? |
| Decide | Choose the action — route it, edit it, escalate it, archive it |
| Execute | Do it |
| Record | Note the outcome (may be a log entry, a git commit, or just conversation context) |
| Reflect | Was that right? Anything to flag? Move on. |

Not every task needs all six stages explicitly. A quick triage might compress Capture→Decide into a single moment. That's fine — the pattern is a guide, not a straitjacket. But when something goes wrong, expanding back to all six stages will reveal where the gap is.

**Note on terminology:** Wave/Session/Task is the *operational* hierarchy — how work is actually done. [[Agent Maestro — Vault Rules|Vault Rules 36–38]] define the *planning* hierarchy: Wave > Phase > Step. The two are orthogonal in the middle: a Phase (scope-bound, has a deliverable) may span multiple Sessions (time-bound, one sitting). Step and Task are the same thing viewed from different angles. Both hierarchies share Wave at the top.

---

## Named Entry Patterns

Common types of work enter the pipeline at different points and emphasize different stages. These are recipes, not separate workflows.

| Pattern           | Entry Point | Emphasis                             | Example                                                                           |
| ----------------- | ----------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| **Triage**        | Capture     | Capture → Interpret → Decide (route) | A new note lands in 01_CAPTURE. Classify it, decide where it goes.                |
| **Proposal**      | Decide      | Decide → gate (audit + approval)     | An idea is mature enough for a formal proposal. Draft, audit, seek approval.      |
| **Build**         | Execute     | Execute → Record                     | An approved proposal is being implemented. Do the work, log the results.          |
| **Review**        | Interpret   | Interpret → Decide (pass/fail)       | Examine an artifact against governance. Does it comply?                           |
| **Archive**       | Decide      | Decide → Execute (move) → Record     | Something is complete or obsolete. Confirm, move to archive, preserve provenance. |
| **Reflection** | Reflect     | Reflect → Capture (seed)             | A wave or phase is complete. What happened? What's next? Produce the seed.        |

Every named pattern is still the full loop — it just starts at a different point and may move through some stages quickly.

---

## Intensity

Not all work requires the same level of rigor. Intensity maps to the existing escalation levels:

| Level | Intensity | Gate Behavior | Artifacts | Who Decides |
|-------|-----------|--------------|-----------|-------------|
| **Level 1 — Automatic** | Light | Rules cover it. Pass/fail against criteria. Fast. | Minimal — a commit message, a log line. | The rules themselves. |
| **Level 2 — Agent Judgment** | Standard | Principles apply. Agent traces decision to Foundations. | Session log entry, documented rationale. | Agent (Worker or Reviewer). |
| **Level 3 — Human Approval** | Deep | Irreversible, architectural, or governance-level. Full audit. | Proposal, adversarial audit, explicit approval. | Human (Rob). |

How to determine intensity: check the **authority_weight** of what you're touching. Ephemeral content (0–29) is usually Level 1. Working documents (30–59) are Level 2. Canonical governance (≥80) is always Level 3.

When in doubt, escalate. The cost of asking is always lower than the cost of unauthorized action.

---

## Participants

### Human-AI Collaborative (current mode)

Rob and Claude working together. The pattern that Wave 5.1 proved effective:

- **Rob** holds ultimate authority (Level 3). Sets direction, approves proposals, makes governance decisions, provides domain judgment.
- **Claude** operates as Worker and/or Reviewer. Proposes, builds, audits, presents options. Never approves its own work.
- **The conversation is the workflow.** Each exchange is a micro-instance of the loop: Rob provides input (Capture), Claude interprets and proposes (Interpret → Decide), they agree on action (gate), Claude executes (Execute), the result is recorded (Record), and both reflect on whether it's right (Reflect).
- **Checkpoints are frequent.** Claude presents findings and asks targeted questions rather than executing large blocks autonomously. This is D4 (Human Sovereignty) in practice.

### LLM Autonomous (future mode)

An LLM agent entering the vault without a human present:

1. **Read the Charter** (`CLAUDE.md` at vault root) — understand the architecture and your role.
2. **Load your role** (`02_KNOWLEDGE/governance/roles/`) — understand your authority level.
3. **Read the stage CLAUDE.md** for wherever you're working — understand the local conventions.
4. **Operate within your authority.** Level 1 actions: execute. Level 2 actions: execute with documented rationale. Level 3 actions: do not execute — package the decision for human review using the Escalate skill.
5. **Record everything.** Session log, state changes, decisions and their rationale.
6. **When the task is complete, reflect.** Did the work achieve its goal? Are there loose ends? File findings for the next session.

The autonomous mode follows the exact same pipeline pattern. The only difference is that Level 3 gates become queues rather than live conversations — the agent packages the decision and waits for human review.

---

## The Fractal Summary

| Scale | Duration | Key Artifact | Gate Type |
|-------|----------|-------------|-----------|
| **Wave** | Days to weeks | Proposal + Reflection | Human approval |
| **Session** | Hours | Session log | Session goal check |
| **Task** | Minutes | Log entry or commit | Authority level check |

One pattern. Three scales. The same loop at every level. The same primitives present at every level. The same escalation model governing every level.

When something goes wrong: expand to all six stages, check all seven primitives, verify the escalation level. The answer is always in the pattern.

---

## Related

- [[Agent Maestro — Foundations]] — the kernel this workflow derives from
- [[AM — Treatise on Core Principles]] — the extended proof, including the fractal instances table
- [[Agent Maestro — Vault Rules]] — the conventions that constrain how work flows
- [[Role — Worker]] — Level 1–2 participant definition
- [[Role — Reviewer]] — Level 2 participant definition
