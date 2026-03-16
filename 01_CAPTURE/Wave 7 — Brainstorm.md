# Wave 7 — Brainstorm

**Source:** Design conversation during Wave 6 proposal session (2026-03-16), between Rob and Claude (Cowork/Opus).

**Context:** This brainstorm happened *before* Wave 6 was built. It captures thinking about Wave 7 that should be refined by Wave 6's reflection. It is not a capture seed — it is a loose brainstorm note per Vault Rule 56.

---

## The Core Question

Wave 7 asks: "Can AM actually *run* things?"

The Roadmap says: bring `04_EXECUTE/` to life, build a runtime provider layer, implement scheduled execution, establish the memory/persistence approach.

But when we examined this against AM principles, the answer was simpler than expected.

## Key Insight: What Problem Are We Actually Solving?

Right now, an LLM connects to AM by reading files. Cowork mounts the vault. Claude Code reads `CLAUDE.md`. There is no middleware, no API layer, no runtime provider. Just an LLM with file access and a well-structured vault that tells it how to behave.

The problem Wave 7 solves is not "how do we connect LLMs to AM?" — that's already solved. The problem is: **how does AM do things when no human starts a session?** That's the autonomy gap. Someone has to open the tool, point it at the vault, and give it a task.

## The Minimum Viable Wave 7

Applying Law 3 (Economy) and D3 (Controlled Evolution), the simplest thing that answers the question:

**launchd runs `orchestrate.sh` on a schedule. Reports land in `05_RECORD/reports/`. Next time a session starts, the reports are waiting.**

That's it. No daemon. No runtime provider framework. No database. No model routing. Just: schedule → run → report → done. The loop closes without a human turning the crank.

Optionally: a thin Python script that can invoke an LLM to read a report and produce a summary. This would be the first instance of an agent operating autonomously on the vault — reading mechanical integrity reports and producing a semantic summary. Minimal, but it proves the concept.

## What We Decided NOT to Build (and Why)

### Runtime Provider Layer (deferred)

The v1 RPL was an abstraction over LLM APIs — provider-agnostic access to inference. The concern: this is framework-building. Frameworks are expensive to maintain, they couple you to API shapes, and they become the thing you work on instead of the thing the framework enables. Law 3 asks: does it earn its place?

If the only consumer is "run a script that calls an LLM," the Anthropic SDK or a direct API call is sufficient. An abstraction layer earns its place when there are *multiple consumers with different needs* — and AM doesn't have those yet.

**Revisit when:** Multiple tools need LLM access with different model requirements, or when provider-switching becomes a real operational need.

### Python Daemon (deferred)

A daemon is a long-running background process. It's needed when tasks must be chained with judgment — when the output of one step determines the next, and that determination requires intelligence (e.g., run scan → if critical findings → invoke LLM to triage → send notification).

Simple scheduled execution doesn't need a daemon. launchd/cron handles the scheduling. The scripts handle the execution. A daemon adds complexity (process management, crash recovery, logging) for no benefit when the tasks are independent script runs.

**Revisit when:** Wave 8 introduces intelligent chaining — where the output of one step determines the next and that determination requires an LLM.

### Memory Architecture Decisions (deferred)

Current memory: markdown files with YAML frontmatter, linked together, version-controlled in git. It works. You can search it, an LLM can read it, it's human-readable, portable.

The vault is ~60 files. Everything fits in context. There is no retrieval problem to solve.

**SQLite** is the right first step *if* a concrete need emerges — most likely when integrity reports need to be compared across time ("trend of broken links over last 10 runs"). A single file, no server, Python-native, queryable. But only introduce it when markdown reports prove insufficient.

**Vector databases** are a Stage 2 concern at the earliest. Needed when the vault is large enough that an LLM can't read everything relevant in one context window. The AM vault is nowhere near that threshold.

**RAG** follows the same logic — it's a retrieval strategy for when you can't fit everything in context. Not needed yet.

**Revisit when:** The vault grows large enough that context window limits become a real constraint, or when cross-run data comparison becomes a proven need.

### Model Routing System (deferred as system; simplified approach adopted)

Building a model routing system before having data about which models work for which tasks is premature optimisation.

**Simple approach for Wave 7:** Three tiers mapped to the existing escalation model.

| Tier | Model class | AM escalation level | Use case |
|------|------------|---------------------|----------|
| Cheap/fast | Haiku-class | Level 1 (Automatic) | Triage, classification, report parsing |
| Mid-tier | Sonnet-class | Level 2 (Agent judgment) | Validation, review, drafting |
| Frontier | Opus-class | Level 3 (Important work) | Adversarial audit, governance, architecture |

Pick one model per tier. Use them. Measure later.

**Revisit when:** Wave 8 instruments the pipeline — at that point, track which model was used, what the outcome was, whether it was satisfactory. Then optimise from data, not assumptions.

## Scheduling: launchd (confirmed)

Rob is on macOS and has already installed launchd. launchd is the native macOS scheduler, handles sleep/wake properly (cron jobs during sleep just don't run), can watch for file changes (not just time triggers), and is Apple's intended approach. No reason to switch to cron.

## What Wave 7 Might Look Like (speculative, pending Wave 6 reflection)

1. **launchd configuration** — schedule `orchestrate.sh` to run daily (or on a configurable interval)
2. **Report delivery** — integrity reports land in `05_RECORD/reports/` automatically
3. **Optional: LLM summary script** — thin Python script that reads the latest integrity report, invokes an LLM (Haiku-tier), and produces a one-paragraph summary appended to the report
4. **Optional: notification** — Slack message or other alert when findings are detected
5. **Documentation** — how to install, configure, and monitor the scheduled execution

This is deliberately minimal. It proves autonomous operation without building infrastructure for problems that don't exist yet.

---

*This note should be triaged after Wave 6 reflects. The reflection may change these conclusions.*
