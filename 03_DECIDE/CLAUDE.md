# 03_DECIDE

**Pipeline Stage:** Decide — Decision
**Foundations Alignment:** Seed 1 (Process) — the third stage of the Irreducible Loop. The validation gate between Interpret and Decide is the most critical in the pipeline.

## Purpose

DECIDE is where proposals are evaluated, contracts are formed, and commitments are made. Nothing is built without a decision here first. This folder contains the system's active commitments and pending proposals.

## Structure

- **proposals/** — Draft proposals awaiting review. Created by Workers using [[Skill — Propose]], gated by Reviewers.
- **active/** — Approved proposals and active contracts. These are the system's current commitments — what is being built, what roadmap governs planning.

## Flow

```
Proposal drafted (Worker) → Gate (Reviewer) → If passed: move to active/ → Execute in 04_EXECUTE/
                                             → If blocked: return to Worker for revision
                                             → If Level 3: escalate to Human
```

## Agent Rules

**Agents MAY:**
- Draft proposals in `proposals/` (Worker role)
- Review and gate proposals (Reviewer role)
- Read all active contracts

**Agents MUST NOT:**
- Move a proposal to `active/` without a gate pass (Vault Rule 29)
- Execute work that has no corresponding active contract
- Modify active contracts without a new proposal cycle

## Key Files

- `proposals/` — Pending proposals awaiting review
- `active/` — Current commitments and roadmaps
