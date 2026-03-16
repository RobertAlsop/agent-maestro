# Agent Maestro — Script Build Harness Integration Brief v1

## Purpose

Define the next design step for integrating a **local script build harness** into the **Build Session Protocol** so that session administration becomes:

- more deterministic
    
- less token-expensive
    
- more auditable
    
- easier to execute repeatedly
    

This brief does **not** build the harness yet.

It formalises:

1. what the harness is
    
2. why it exists
    
3. what the protocol must change
    
4. what needs to be built next
    

---

# 1. Problem Statement

The current Build Session Protocol v2 is structurally strong, but too much of the protocol still depends on frontier-model participation for tasks that are:

- repetitive
    
- mechanical
    
- deterministic
    
- low-judgment
    

This creates two problems:

## A. Frontier model token waste

Claude Opus is being used for steps that should be handled by scripts, such as:

- session setup
    
- repo state capture
    
- manifest creation
    
- pre-build Git checkpointing
    
- post-build commit flow
    
- release administration
    
- verification ritual
    

## B. Execution friction

If every session requires the model to manually re-establish state and repeat protocol mechanics, builds become:

- slower
    
- more expensive
    
- more fragile under rate limits
    

---

# 2. Design Goal

Refactor the Build Session Protocol so that:

- **the model handles reasoning**
    
- **scripts handle mechanics**
    
- **Git handles lineage**
    
- **artifacts handle auditability**
    

This preserves the protocol while reducing model overhead.

---

# 3. Strategic Principle

The correct move is:

> **Do not script the thinking. Script the ritual around the thinking.**

The model should remain responsible for:

- brief creation
    
- roadmap thinking
    
- proposal / contract generation
    
- design logic
    
- controlled build reasoning
    
- exception handling
    
- review of verification results
    
- post-build interpretation
    

The script harness should take over:

- session start mechanics
    
- repo snapshot capture
    
- manifest generation
    
- deterministic file inventory
    
- cheap verification checks
    
- post-build Git actions
    
- optional tagging / release mechanics
    

This approach is directly aligned with the AI OS principles of determinism, contracts, auditability, and no hidden state.

---

# 4. What the Script Build Harness Is

The **Script Build Harness** is a small local command layer that performs the deterministic administrative steps surrounding each build session.

It is not a new agent system.  
It is not a build brain.  
It is not an automation platform.

It is a **local execution harness** that prepares, records, verifies, and closes sessions consistently.

## Working definition

The harness is a set of local scripts that:

- initialise a build session
    
- capture canonical repo context
    
- verify session invariants
    
- close the session cleanly in Git
    

---

# 5. Proposed Harness Scope

The initial harness should contain four commands.

## 5.1 `session_start`

Purpose:

- start a deterministic build session
    

Responsibilities:

- generate `session_id`
    
- generate `run_id`
    
- create session folder
    
- check repo status
    
- optionally commit a pre-build checkpoint
    
- write initial `session_manifest.json`
    
- capture basic repo metadata
    

## 5.2 `context_capture`

Purpose:

- produce the canonical build context artifact
    

Responsibilities:

- record branch
    
- record HEAD commit
    
- record clean/dirty state
    
- enumerate tracked files
    
- hash tracked files deterministically
    
- write `repo_snapshot.json`
    
- optionally produce a compact folder/file manifest
    

This is the high-leverage upgrade used by strong AI engineering teams: instead of letting the model “peek” vaguely at repo state, planning consumes an explicit context artifact. That matches the `context_capture` direction already present in your roadmap.

## 5.3 `session_verify`

Purpose:

- run deterministic post-build checks
    

Responsibilities:

- confirm required artifacts exist
    
- confirm session folder is complete
    
- confirm no forbidden structural violations
    
- run cheap vault integrity checks
    
- write `verification_report.md` or `.json`
    

## 5.4 `session_close`

Purpose:

- close the build session in a disciplined way
    

Responsibilities:

- `git add -A`
    
- commit with standard session message
    
- optionally tag
    
- optionally create GitHub release via `gh`
    
- update manifest with end state
    

---

# 6. Redraft Required for the Build Session Protocol

The protocol should now explicitly distinguish between:

## A. Cognitive stages

Handled by human + model.

These are:

- input
    
- brief
    
- proposal
    
- build reasoning
    
- output interpretation
    

## B. Mechanical stages

Handled by local scripts.

These are:

- session initialisation
    
- repo freeze
    
- context capture
    
- verification execution
    
- Git closeout
    
- optional release administration
    

---

# 7. Recommended Protocol Redraft Direction

The Build Session Protocol should be revised from a purely conversational lifecycle into a **hybrid run lifecycle**.

## Current implicit model

Human → Claude → Build → Summary → Log

## New explicit model

Human → Scripted session start → Claude brief/contract → Claude-guided build → Scripted verify/close → Claude final interpretation

That is the more mature form.

---

# 8. Proposed Protocol v2.1 Structure

I would redraft the protocol around these stages:

## Stage 0 — Session Initialisation

Handled by `session_start`

Outputs:

- `session_id`
    
- `run_id`
    
- session folder
    
- initial manifest
    
- optional pre-build checkpoint
    

## Stage 0.5 — Context Capture

Handled by `context_capture`

Outputs:

- `repo_snapshot.json`
    
- deterministic repo truth artifact
    

## Stage 1 — Input

Human provides task context.

## Stage 2 — Brief / Roadmap

Model produces brief using the context artifact rather than informal repo scanning.

## Stage 3 — Proposal / Build Contract

Model produces scoped contract.

## Stage 4 — Build

Model guides execution against the contract.

## Stage 5 — Verification

Handled by `session_verify`

## Stage 6 — Output Summary

Model interprets results and summarises.

## Stage 7 — Session Closeout

Handled by `session_close`

## Stage 8 — Session Log Finalisation

Model or script finalises human-readable session record.

---

# 9. Key New Rule to Add

Add this rule to the protocol:

> **All deterministic session-administration steps should be executed by the local build harness where possible. Frontier models should be reserved for scoped reasoning, contract generation, controlled execution, and exception handling.**

That one sentence is the core doctrinal upgrade.

---

# 10. What Needs to Be Built

The next build should produce a **Build Harness v1**.

## Deliverables

### A. Script files

Likely under something like:

tools/build/

or

scripts/build/

with four scripts:

- `session_start`
    
- `context_capture`
    
- `session_verify`
    
- `session_close`
    

## B. Session artifact schema

Define exact schema for:

- `session_manifest.json`
    
- `repo_snapshot.json`
    
- `verification_report.json` or `.md`
    

## C. Protocol redraft

Produce **Build Session Protocol v2.1** reflecting the harness.

## D. Operator usage note

A short note explaining:

- when to run each script
    
- what to paste back into chat
    
- what the model should consume
    

## E. Optional wrapper

Potentially a single orchestrator command later, but **not in v1**

For v1, separate commands are better because they remain auditable and composable.

---

# 11. Recommended Build Order

This is the sensible order:

## Build 1

Design artifacts only:

- Build Harness Brief
    
- Build Session Protocol v2.1
    
- artifact schemas
    
- script specification
    

## Build 2

Implement:

- `session_start`
    
- `context_capture`
    

## Build 3

Implement:

- `session_verify`
    
- `session_close`
    

That sequencing is strong because the first two scripts give the biggest leverage fastest.

---

# 12. Why This Is the Right Next Step

Because it gives you:

- immediate token savings
    
- cleaner session discipline
    
- better replayability
    
- stronger audit trails
    
- less dependence on frontier-model administrative work
    

And it does so without overbuilding, which matches your “start simple, harden over time” principle.

---

# 13. Recommended Immediate Next Artifact

The next artifact to create should be:

**Agent Maestro — Build Harness Implementation Brief v1**

That artifact should define:

- folder location
    
- exact scripts
    
- exact outputs
    
- artifact schemas
    
- command conventions
    
- failure rules
    
- boundaries
    
- what is deferred from v1
    

That gives you a clean contract before implementation.