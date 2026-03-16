# 04_EXECUTE — Execute Stage

## Pipeline Position

Stage 4 of 6. Receives approved plans from `03_DECIDE/`. Outputs are recorded in `05_RECORD/`.

## Purpose

This is where approved work gets built. Code, tools, configurations, and any other artifacts that require active construction live here during their build lifecycle.

## Current State

Empty. All previous tools and runtime code were archived during Wave 5.2 (Pipeline Hardening) because they were built against schema v2 and the old constellation architecture. Rebuilding vault tools aligned to v1.0.0 architecture is registered as a future wave item.

## Gate: Entry from Decide

Nothing enters Execute without an approved proposal or explicit human delegation. The proposal is the contract.

## Gate: Exit to Record

Completed work must be recorded. Every build session ends with a log entry in `05_RECORD/logs/`.

## Conventions

- Feature branches only — never commit directly to master
- Tag current state before major changes: `git tag pre-<description>`
- Follow Git Best Practices protocol (see `02_KNOWLEDGE/protocols/`)
- Build as Worker, review as Reviewer (D6 — Separation of Powers)
