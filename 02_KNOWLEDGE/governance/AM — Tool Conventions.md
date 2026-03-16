---
title: "AM — Tool Conventions"
type: governance
status: draft
authority_weight: 70
schema_version: 3
created: "2026-03-16"
updated: "2026-03-16"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[AM — Integrity Layers]]"
  governs: []
  related:
    - "[[Agent Maestro — Vault Rules]]"
    - "[[AM — Roadmap]]"
tags:
  - governance
  - tools
  - conventions
  - scripts
  - mechanical
---

# AM — Tool Conventions

## Purpose

Define how tools are designed, built, and operated within the Agent Maestro ecosystem. Any executable artifact that lives in `04_EXECUTE/tools/` — shell scripts, Python utilities, validators, or future tooling — is governed by this document.

## Principle

Tools are the mechanical arm of AM's integrity system. They implement [[AM — Integrity Layers|Mechanical Integrity]]. Because they operate without judgment, they must be built with extreme clarity about what they do, what they don't do, and how they behave in every operating condition. A tool that is ambiguous in its scope is a tool that cannot be trusted.

---

## Core Conventions

### 1. Tools Are Stateless Read-Check-Report Executors

A tool reads vault state, checks it against rules, and reports what it finds. That is the entire scope of what a tool does. Each invocation is self-contained — a tool does not remember previous runs, does not maintain internal state between executions, and does not depend on having been run before.

This means every tool has three internal phases:

| Phase | What happens |
|-------|-------------|
| **Read** | Load configuration, accept arguments, scan the vault. Build an internal model of what exists. |
| **Check** | Compare the model against configured rules. Determine what passes, what fails, and what is ambiguous. |
| **Report** | Produce output — write findings to a report file, return an exit code, optionally print a summary to stdout. |

A tool that skips a phase — for example, one that reports without checking, or checks without fully reading — will eventually produce wrong results. The three phases are a completeness checklist for tool design.

### 2. Tools Are Config-Driven

No tool may hardcode assumptions about vault structure, required files, naming conventions, or output locations. Every vault-specific expectation must be declared in configuration.

**Why:** Portability. The same tool suite must work on Agent Maestro, Trust Birth Pools, and any future vault. Configuration is the contract between the tool and the vault it operates on.

**Configuration model:**

- **Vault configuration** — a per-vault config file that declares vault-specific expectations (vault root path, required folders, required files, controlled vocabulary values, regions requiring YAML, output paths, etc.). This is the primary contract.
- **Invocation arguments** — command-line flags that override config for specific runs (e.g., `--output-dir`, `--strict`, `--quiet`). Invocation arguments take precedence over vault config.

Tools should use sensible defaults where config is silent — for example, checking all `.md` files for valid YAML unless config restricts the scope. But no tool may assume the presence of AM-specific structures (pipeline folders, governance hierarchy, schema v3) without those being declared in config.

### 3. Tools Report, They Don't Repair

Tools produce findings. They do not fix what they find. Detection and remediation are different responsibilities held by different actors (D6 — Separation of Powers).

**Allowed write actions:**
- Generate report files
- Generate log files

**Forbidden actions:**
- Creating, modifying, or deleting vault content (notes, frontmatter, body text, stubs)
- Moving or renaming files
- Rewriting links or references
- Creating git commits
- Any action that changes the vault's state

This convention is absolute. If remediation capability is needed in the future (stub creation, auto-commit, etc.), it belongs in a separate tool category with its own governance, not mixed into detection tools. Detection tools are read-only. No exceptions, no config flags.

**Why this is stricter than a "config-gated exception" model:** A tool that *can* write — even optionally — is a tool that must be audited for write safety. Keeping detection tools purely read-only means they can be run with zero risk in any context: CI, audit, unattended maintenance, unfamiliar vaults. The trust model is simpler when the guarantee is absolute.

### 4. Tools Are Independently Useful and Composable

Each tool must be runnable on its own and produce a complete, self-contained result. No tool may depend on another tool having been run first (though it may consume another tool's output if available).

At the same time, tools must be composable. An orchestrator can run multiple tools in sequence and aggregate their outputs. The orchestrator does not duplicate the work of individual tools — it coordinates them.

Independence means any single check can be run in isolation for debugging or targeted validation. Composability means the full suite can run as a single operation. Both are required.

### 5. Tools Use Meaningful Exit Codes

Every tool must return structured exit codes that downstream consumers (CI pipelines, orchestrators, agents) can act on without parsing output:

| Exit Code | Meaning |
|-----------|---------|
| `0` | Clean — no issues found |
| `1` | Findings — issues detected, reported |
| `2` | Error — the tool itself failed (couldn't read config, vault path invalid, etc.) |

This three-state model maps cleanly to pipeline gates: `0` means the gate passed, `1` means the gate found issues to address, `2` means the gate couldn't run. A consumer that sees `1` knows to read the report. A consumer that sees `2` knows to investigate the tool, not the vault.

### 6. Output Is Machine-Readable and Human-Readable

Tool output must serve two audiences: humans reading reports and agents consuming findings as structured input.

**Report format:** Each tool produces a report file in its configured output directory. Reports must include: a header identifying the tool, vault path, and timestamp; a summary count (items checked, passed, failed); and the detailed findings. The format should be Markdown for human readability with consistent structure that agents can parse.

**Stdout:** Tools should output a concise summary to stdout (suitable for terminal and CI use). Detailed findings go to the report file, not stdout. Quiet mode (`--quiet`) suppresses stdout entirely and only writes the report.

### 7. Tools Are Conservative

When the result of a check is ambiguous, the tool must not report it as a failure. Mechanical integrity checks must be provably correct — a reported issue must be a real issue, not a guess.

**Why:** False positives erode trust. If a tool cries wolf, operators stop reading its reports. A conservative tool that catches 80% of real problems and flags zero false problems is more valuable than an aggressive tool that catches 95% but includes 10% false positives. Trust is the tool's most important output.

Ambiguous findings may be reported in a separate "warnings" or "uncertain" section of the report, clearly distinguished from confirmed findings.

---

## Safety Rules

Tools operate under the same authority model as the rest of AM. The following constraints are absolute:

1. **No semantic interpretation.** Tools must never reason about meaning. If a check requires understanding what a note *means*, it belongs in [[AM — Integrity Layers|Semantic Integrity]], not in a tool.

2. **Read-only by default and by design.** Detection tools do not write to the vault. This is not a configurable behaviour — it is an architectural constraint. Reports and logs are the only write outputs, and they are written to the tool's own output directory, not into the vault content tree.

3. **No silent mutations.** If a tool writes anything (reports, logs), it must log exactly what it wrote and where. Law 2 (Action Properties): all actions must be verifiable, reversible, and accountable.

4. **No unbounded scope.** Every tool operates on explicitly configured paths. No tool may scan outside the declared vault root. No tool may follow symlinks outside the vault without explicit configuration.

5. **Fail safe.** If a tool encounters an unexpected condition (missing config, unreadable file, ambiguous state), it must exit with code `2` and a clear error message. It must not guess, skip, or continue with partial results unless explicitly configured to do so (e.g., a `--best-effort` flag).

---

## Relationship to Other Governance

This document governs implementation principles. It does not define *what* to check — that is determined by [[Agent Maestro — Vault Rules]] (which defines the structural rules tools enforce) and by the specific Wave proposal that scopes each build. It does not define *what the layers are* — that is established by [[AM — Integrity Layers]]. This document defines *how* to build the tools that do the checking.

**Authority chain:** [[Agent Maestro — Foundations]] → [[AM — Integrity Layers]] → **AM — Tool Conventions** → individual tool implementations.

Implementation-specific decisions — folder structure, naming conventions for scripts, orchestrator design, operating modes, config file format — belong in the Wave proposal or in the tool suite's own documentation (e.g., a `README.md` in the tool directory). This document provides the principles those decisions must satisfy, not the decisions themselves.

## When It Applies

When designing, building, reviewing, or extending any tool in `04_EXECUTE/tools/`. When evaluating whether a proposed tool meets AM's standards. When onboarding a new contributor to the tool suite.

## Related

- [[Agent Maestro — Foundations]] — the kernel (Law 2, Law 3, D1, D6)
- [[AM — Integrity Layers]] — the architectural separation this implements
- [[Agent Maestro — Vault Rules]] — the rules tools enforce mechanically
- [[AM — Roadmap]] — Wave 6 is the first implementation governed by this document
