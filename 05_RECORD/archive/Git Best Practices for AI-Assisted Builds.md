---
title: "Git Best Practices for AI-Assisted Builds"
type: concept
status: archived
authority_weight: 40
archived_date: "2026-03-17"
archived_reason: "Replaced by [[AM — Git Conventions]] (governance, authority_weight 70). All principles preserved and extended."
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Vault Rules]]"
    - "[[Agent Maestro — Foundations]]"
  governs: []
  related: []
tags: [git, best-practices, safety, reference]
---

# Git Best Practices for AI-Assisted Builds

## Purpose

Define the full git workflow and safety rules for AI-assisted implementation within Agent Maestro. The key principles from this document are codified as vault rules; this reference provides the complete operational detail.

This document operationalizes Law 2 (all actions must be verifiable, reversible, and accountable) for version control.

---

## 1. Core Rule

Never perform AI-assisted build work directly on `main`.

All implementation work must occur on a dedicated working branch.

---

## 2. Protected Baseline Rule

`main` is the protected baseline branch.

It must remain:

- stable
- reversible
- recoverable
- suitable for rollback at all times

Claude must treat `main` as protected.

---

## 3. Branch Rule

Before beginning any meaningful implementation step, create a dedicated branch.

Example:

```
git checkout -b slice-04-content-layer
```

Branch names should reflect the specific build phase or slice.

Examples:
- `slice-04-content-layer`
- `slice-05-seo-layer`
- `slice-06-commerce`
- `slice-09-static-routes`

Do not reuse a stale branch for unrelated work.

---

## 4. Checkpoint Tag Rule

Before any major AI-assisted build pass, create a checkpoint tag from the current known-good state.

Example:

```
git tag pre-slice-04
git push origin pre-slice-04
```

Checkpoint tags create an exact rollback anchor.

They should be used:
- before large Claude coding passes
- before major refactors
- before multi-file semantic implementation
- before contract-sensitive edits

---

## 5. Recovery Rule

If an AI-assisted build pass produces bad output, rollback must be immediate and mechanical.

If the bad work is confined to a working branch, discard the branch:

```
git checkout main
git branch -D slice-04-content-layer
```

If a hard rollback is needed to a tagged state:

```
git reset --hard pre-slice-04
```

Only perform hard reset when you intentionally want to discard current uncommitted or unwanted committed state.

---

## 6. Merge Rule

Only merge a working branch back into `main` when all relevant validations pass.

Typical merge flow:

```
git checkout main
git merge slice-04-content-layer
```

Never merge unvalidated AI output into `main`.

---

## 7. Commit Rule

Commit frequently at meaningful checkpoints.

Good commits are:
- small enough to understand
- reversible
- tied to a single implementation objective

Examples:
- `Implement content query layer scaffold completion`
- `Implement hreflang builder and metadata wiring`
- `Wire static routes to content loaders`

Avoid vague commit messages.

Bad examples:
- `stuff`
- `updates`
- `fixes`

---

## 8. Validation Rule

Before committing or merging, run the relevant validation commands.

Examples may include:

```
./scripts/validate_structure.sh
./scripts/validate_content_parity.sh
./scripts/validate_placeholders.sh
astro check
astro build
```

Claude must not treat code generation as complete until validations pass.

---

## 9. Safety Rule for Claude

Claude must not:
- delete the repository
- rewrite Git history unless explicitly instructed
- force-push without explicit permission
- work directly on `main`
- remove contract-governed files without explicit authorization
- bypass validation steps

Claude may:
- create or use a working branch
- make small, scoped commits
- recommend checkpoint tags
- stop before merge if validation fails

---

## 10. Preferred AI Build Workflow

1. Confirm current branch is not `main` for implementation work.
2. Create a checkpoint tag from the last known-good state.
3. Create a dedicated working branch for the slice or task.
4. Perform implementation work.
5. Run validation.
6. Commit scoped changes.
7. Merge to `main` only after validation passes.
8. Push branch and tags as needed.

---

## 11. Minimal Safe Example

```
git checkout main
git pull
git tag pre-slice-04
git push origin pre-slice-04
git checkout -b slice-04-content-layer
```

Claude performs the build work on the branch.

If successful:

```
git add .
git commit -m "Implement slice 04 content query and relation layer"
git checkout main
git merge slice-04-content-layer
git push origin main
```

If unsuccessful:

```
git checkout main
git branch -D slice-04-content-layer
```

---

## 12. Operating Principle

The goal is not merely to build quickly.

The goal is to make every AI-assisted build step:
- auditable
- reversible
- bounded
- contract-safe

## Related

- [[Agent Maestro — Vault Rules]]
- [[Agent Maestro — Foundations]]
