# Agent Maestro — Build Session Protocol v2

## Purpose

Defines the **deterministic lifecycle for all Agent Maestro build sessions**.

The protocol ensures that every build session is:

- reproducible
    
- auditable
    
- version-controlled
    
- governed by an explicit contract
    

Every session becomes a **traceable engineering run** with:

- identity
    
- artifacts
    
- logs
    
- Git history
    

---

# Core Principles

The protocol enforces the following system principles:

1. **Determinism First**  
    Every build must start from a frozen repository state.
    
2. **Contracts Over Prompts**  
    No build may execute without a formal proposal acting as the build contract.
    
3. **Auditability by Default**  
    All sessions produce logs and artifacts.
    
4. **No Bypass Rule**  
    No build may bypass validation, logging, or version control.
    
5. **Traceable Identity**  
    Every session is assigned unique identifiers.
    

---

# Session Identity

Every build session generates the following identifiers:

session_id  
run_id  
correlation_id (optional)

These identifiers appear in:

- session logs
    
- artifacts
    
- commit messages
    
- release manifests
    

---

# Session Artifacts

Each session creates a directory:

06_EXECUTION/logs/sessions/<SESSION_ID>/

Artifacts stored here include:

session_manifest.json  
proposal.md  
output_summary.md  
verification_report.md  
session_log.md  
repo_snapshot.json

---

# Session Lifecycle

## Stage 0 — Repository Freeze

Freeze repository state before the session begins.

Purpose:

- establish deterministic starting point
    
- ensure reproducibility
    

### Steps

1. Verify repository cleanliness
    

git status --porcelain

If output is not empty:

git add -A  
git commit -m "Pre-build checkpoint — Session <SESSION_ID>"

2. Capture repository snapshot
    

Record:

branch  
commit_hash  
timestamp

Store snapshot as:

repo_snapshot.json

3. Create session artifact directory
    

06_EXECUTION/logs/sessions/<SESSION_ID>/

4. Create initial session manifest
    

session_manifest.json

This records:

session_id  
run_id  
start_commit  
branch  
timestamp

---

## Stage 1 — Session Input

The human provides:

- context
    
- intent
    
- constraints
    

Claude records:

session_id  
run_id  
session_start_time

The session log is created immediately.

---

## Stage 2 — Brief / Roadmap

Claude produces a structured brief describing:

- problem scope
    
- constraints
    
- expected outputs
    
- dependencies
    

Purpose:

- clarify objectives
    
- prevent premature execution
    

Exit condition:

Human confirms understanding and approves direction.

---

## Stage 3 — Proposal (Build Contract)

Claude produces a deterministic **build proposal**.

The proposal functions as the **Build Contract**.

The proposal must define:

files_to_create  
files_to_modify  
files_to_delete (if any)  
execution sequence  
success criteria  
verification steps  
risks

The proposal is saved as:

sessions/<SESSION_ID>/proposal.md

Human approval is mandatory.

No build may begin before approval.

---

## Stage 4 — Execution (Build)

Claude executes the approved proposal.

Rules:

- Only files listed in the proposal may be modified
    
- All changes must follow vault conventions
    
- Scope changes require a revised proposal
    

Execution progress should be documented.

---

## Stage 5 — Verification

After execution, the system performs verification.

Typical checks include:

vault integrity check  
registry rebuild  
link validation  
markdown structure validation

Results are recorded in:

verification_report.md

If verification fails:

- build must pause
    
- fixes must be proposed
    
- verification must re-run
    

---

## Stage 6 — Output Summary

Claude produces a complete summary of the build.

The summary includes:

files_created  
files_modified  
files_deleted  
registries_updated  
design decisions  
deferred tasks  
verification results

Saved as:

output_summary.md

---

## Stage 7 — Repository Commit

The completed build is committed to Git.

git add -A  
git commit -m "Agent Maestro build — Session <SESSION_ID>"

Commit message should include:

session_id  
run_id  
build scope

---

## Stage 8 — Optional Release

If the build represents a meaningful milestone:

git tag vX.Y

Optional GitHub release:

gh release create vX.Y

Release artifacts may include:

- changelog
    
- build summary
    
- relevant documentation
    

---

## Stage 9 — Session Log Finalisation

A formal session log is written.

Location:

06_EXECUTION/logs/sessions/<SESSION_ID>/session_log.md

The log captures:

session metadata  
context  
proposal  
execution results  
verification outcome  
next actions

The session index CSV is updated.

---

# Session Variations

## Exploration Session

Used for research or planning.

Lifecycle:

0 → 1 → 2 → 9

No proposal or build.

---

## Minor Fix Session

For tightly scoped changes.

Lifecycle:

0 → 1 → 3 → 4 → 6 → 7 → 9

A proposal is still required.

---

## Multi-Build Session

Allows multiple contract-execution cycles within a single session.

Lifecycle:

0 → 1 → 2 → 3 → 4 → 6  
               ↺  
             3 → 4 → 6  
                 → 7 → 9

---

# Hard Rules

1. **Clean Repository Required**  
    Builds must begin from a known repository state.
    
2. **Contract Enforcement**  
    Builds may only modify files defined in the proposal.
    
3. **Mandatory Verification**  
    Every build must run integrity checks.
    
4. **Mandatory Logging**  
    Every session must produce artifacts and logs.
    
5. **Explicit Scope Changes**  
    Scope changes require a revised proposal.
    
6. **Git Discipline**  
    Every build session must end with a commit.
    
7. **Session Traceability**
    

Every session must record:

session_id  
run_id  
start_commit  
end_commit  
proposal_reference

---

# Session Manifest

Each session includes a machine-readable manifest.

Location:

sessions/<SESSION_ID>/session_manifest.json

Example structure:

{  
  "session_id": "",  
  "run_id": "",  
  "branch": "",  
  "start_commit": "",  
  "end_commit": "",  
  "proposal_file": "",  
  "output_summary": "",  
  "verification_report": "",  
  "tag": ""  
}

Purpose:

- enables automated analysis
    
- supports future AI supervision
    
- enables deterministic replay of sessions
    

---

# Outcome

The Build Session Protocol ensures that every Agent Maestro build session is:

- deterministic
    
- auditable
    
- reproducible
    
- contract-driven
    

Each session becomes a **fully traceable engineering run**, forming a reliable history of the system’s evolution.