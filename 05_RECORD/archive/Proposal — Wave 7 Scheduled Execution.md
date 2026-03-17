---
title: "Proposal — Wave 7 Scheduled Execution"
type: proposal
status: archived
authority_weight: 30
schema_version: 3
created: "2026-03-16"
updated: "2026-03-17"
approved: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Wave 6 — Reflection]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
    - "[[Wave 7 — Brainstorm]]"
    - "[[Proposal — Wave 6 Mechanical Integrity]]"
tags: [proposal, wave-7, scheduled-execution, runtime, launchd]
---

# Proposal — Wave 7 Scheduled Execution

## Problem Statement

AM can detect its own structural problems (Wave 6). It cannot act on that capability without a human starting a session, navigating to the vault, and running the tools manually. Every integrity check currently requires someone to sit down, open a tool, and type `./orchestrate.sh`.

This creates two specific problems:

1. **The integrity suite has no cadence.** Problems accumulate between sessions. A broken link introduced on Monday isn't detected until someone happens to run the tools — which might be days or weeks later. The tools exist; the habit of running them does not.
2. **AM has no autonomous operation.** The roadmap's Stage 1 exit criteria include: "AM runs scheduled maintenance between human sessions." Currently, AM does nothing between sessions. It is entirely passive — a knowledge architecture that waits to be read.

The [[AM — Roadmap]] identifies this as the next committed wave: "Can AM actually run things?" The [[Wave 6 — Reflection]] validates the [[Wave 7 — Brainstorm]]'s conclusion: the simplest thing that answers this question is scheduled script execution via launchd.

## Proposed Change

**Wave 7: Scheduled Execution** — give AM the ability to run its integrity suite autonomously on a schedule, produce reports without human initiation, and optionally summarise findings using an LLM.

The wave has three phases, ordered by dependency. All runtime artifacts live in `04_EXECUTE/runtime/` — the execution folder for scheduling, orchestration, and semantic processing. This is distinct from `04_EXECUTE/tools/` which holds Mechanical Integrity detection tools governed by [[AM — Tool Conventions]]. The `runtime/` folder holds code that *consumes* tool output and *operates* the system — scheduling, summarisation, notification. The distinction maps to [[AM — Integrity Layers]]: `tools/` implements mechanical detection; `runtime/` implements everything that acts on detection output.

### Phase 1 — Scheduled Execution via launchd

Build the launchd configuration that runs `orchestrate.sh` on a daily schedule.

**Deliverables:**

| Artifact | Location | What it does |
|----------|----------|-------------|
| `com.agentmaestro.vault-maintenance.plist` | `04_EXECUTE/runtime/launchd/` | launchd job definition — runs orchestrate.sh daily |
| `run_maintenance.sh` | `04_EXECUTE/runtime/` | Wrapper script — coordinates orchestrate.sh, optional summary, optional notification in sequence |
| `install.sh` | `04_EXECUTE/runtime/launchd/` | Installs the plist to `~/Library/LaunchAgents/`, validates paths, sets permissions |
| `uninstall.sh` | `04_EXECUTE/runtime/launchd/` | Removes the plist cleanly |
| Updated `am.conf` | `04_EXECUTE/tools/vault-maintenance/config/` | Any config changes needed for unattended operation (e.g., absolute paths, quiet mode default) |

**Design decisions:**

- **launchd, not cron.** Rob is on macOS. launchd is the native scheduler, handles sleep/wake correctly (cron jobs during sleep simply don't run), and is Apple's intended approach. Already installed and proven on the target machine.
- **Daily schedule, configurable.** Default to once daily (early morning). The plist is a text file — changing the interval is editing one XML value. No config abstraction needed for something this simple.
- **User-level agent, not system daemon.** The plist installs to `~/Library/LaunchAgents/`, runs as the current user, requires no elevated privileges. This is maintenance, not infrastructure.
- **Quiet mode by default for scheduled runs.** When running unattended, stdout is irrelevant. The plist passes `--quiet` to orchestrate.sh. All output goes to reports.
- **Date-stamped reports.** Each scheduled run produces a date-stamped report file (e.g., `vault_health_report_2026-03-17.md`) rather than overwriting a single file. This preserves history for trend comparison and ensures each day's findings are a distinct artifact. The orchestrator's `--output-dir` already supports this — the wrapper script (or plist) passes a date-stamped filename. Previous reports are not deleted; accumulation is addressed under "What could go wrong."
- **Log file for operational visibility.** launchd's `StandardOutPath` and `StandardErrorPath` capture any unexpected output or errors. Logs land in `04_EXECUTE/tools/vault-maintenance/logs/`.

### Phase 2 — LLM Summary Script (optional)

Build a thin Python script that reads the latest integrity report and produces a one-paragraph natural language summary using an LLM.

**Deliverables:**

| Artifact | Location | What it does |
|----------|----------|-------------|
| `summarise_report.py` | `04_EXECUTE/runtime/` | Reads latest vault_health_report.md, invokes LLM, appends summary |
| `config.example.yaml` | `04_EXECUTE/runtime/` | Documents configuration (Ollama endpoint, model name) |

**Design decisions:**

- **This is a Semantic Integrity actor, not a Mechanical Integrity tool.** Per [[AM — Integrity Layers]], mechanical integrity runs first and produces structured reports; semantic integrity follows and interprets them. The summary script is the first instance of this sequence being automated. It lives in `04_EXECUTE/runtime/`, not in `04_EXECUTE/tools/vault-maintenance/`, because it is not a detection tool — it is a consumer of detection output.
- **Local LLM via Ollama (llama3.2).** Rob has Ollama installed locally with `llama3.2`. Daily automated maintenance should not incur API costs or depend on an external service. A local model handles Level 1 work (summarising a structured report — pattern recognition, not judgment) without cost, latency, or availability concerns. The brainstorm's three-tier model (Haiku-class for Level 1, Sonnet-class for Level 2, Opus-class for Level 3) still holds — the tier defines the capability needed, not the provider. The model name is configured in the runtime config file (default: `llama3.2`). Before invoking the model, the script verifies availability via `ollama list` or the Ollama API's model endpoint — if the configured model is not installed, the script logs the error and exits cleanly (same as if Ollama is not running).
- **Direct API call to Ollama, not an abstraction layer.** The Runtime Provider Layer was considered and deferred (see Future Waves Register). A single HTTP call to Ollama's local API (`localhost:11434`) is sufficient when there is one consumer. The RPL abstraction earns its place when there are multiple consumers with different provider needs — not before. Swapping Ollama for another provider later means changing one endpoint, not rebuilding a framework.
- **Appends to the existing report, does not create a separate file.** The summary is most useful when it appears at the bottom of the report it summarises. The human opening the health report sees the mechanical findings first, then the LLM's read of those findings. One file, one artifact. The summary is written under a `## LLM Summary` heading with a timestamp. The script checks for an existing `## LLM Summary` section before appending — if one already exists (e.g., from a manual re-run), it skips rather than duplicates. This makes the append operation idempotent.
- **Graceful degradation.** If Ollama is not running, the configured model is not available, or the call fails, the script logs the error to `04_EXECUTE/tools/vault-maintenance/logs/` and exits with code 2 (error — script itself failed) without modifying the report. The mechanical report is never corrupted by a semantic failure. This honours the layer separation: mechanical output is the foundation; semantic output is additive. Exit codes for the summary script follow the same convention as tools: 0 = summary appended successfully, 1 = not used (reserved), 2 = error (Ollama unavailable, model missing, API failure).

**Integration with Phase 1:** A wrapper script (`run_maintenance.sh` in `04_EXECUTE/runtime/`) coordinates the full sequence. The launchd plist calls this wrapper, not `orchestrate.sh` directly. The wrapper:

1. Runs `orchestrate.sh` with date-stamped output
2. If Phase 2 is built: runs `summarise_report.py` on the new report
3. If Phase 3 is built: runs `notify.sh` based on the orchestrator's exit code

This design means Phase 1's launchd plist never changes when Phases 2 or 3 are added — the wrapper script is the extension point. Each phase can be deployed and removed independently by editing the wrapper.

### Phase 3 — Notification (optional)

Send a notification when the integrity suite produces findings.

**Deliverables:**

| Artifact | Location | What it does |
|----------|----------|-------------|
| `notify.sh` (or equivalent) | `04_EXECUTE/runtime/` | Sends a macOS notification when orchestrate.sh exits with code 1 (findings) |

**Design decisions:**

- **macOS native notification via `osascript`.** The stack is local — Ollama runs locally, launchd runs locally, the vault is local. Sending a Slack message to tell yourself something happened on your own machine goes out to the internet and back for no reason. `osascript -e 'display notification'` is zero-dependency, immediate, and appropriate for a local-first setup. If remote notification is needed later (AM running on a server, or notifications when away from the machine), Slack integration is a future concern, not a Wave 7 concern.
- **Only notify on findings, not on clean runs.** A daily "everything is fine" message becomes noise. Notification should be signal — something needs attention.
- **No notification on error (exit code 2).** Errors in the tool suite itself should be caught by log monitoring, not by the notification system. Mixing operational errors with vault findings muddies the signal.
- **Notification text includes the summary if available.** If Phase 2 ran successfully, the notification includes the LLM's one-paragraph summary rather than a generic "findings detected" message. This means the notification carries information, not just urgency. If Phase 2 didn't run (or failed gracefully), the notification falls back to reporting the number of tools with findings.

## Scope Degradation Plan

If time pressure or unexpected complexity builds:

**Minimum viable Wave 7** (Phase 1 only):
- launchd plist, install/uninstall scripts, documentation
- This alone answers the wave's question: "Can AM run things?" The answer is yes — it runs the integrity suite daily without human initiation.

**Standard Wave 7** (Phases 1 + 2):
- Adds LLM summary. This is the first instance of automated semantic integrity — a meaningful capability step.

**Full Wave 7** (all three phases):
- Adds notification. Nice to have but not load-bearing. The reports exist whether or not anyone is notified about them.

## What Is NOT in Scope

These items were considered during the Wave 7 brainstorm, validated as useful, and explicitly deferred. They are documented in the [[AM — Future Waves Register]] with revisit criteria.

| Item | Why deferred | Revisit when |
|------|-------------|--------------|
| Runtime Provider Layer | Framework-building for one consumer. A direct API call suffices. | Multiple tools need LLM access with different requirements |
| Python daemon | launchd handles scheduling without process management overhead | Wave 8 introduces chained workflows requiring intelligent task routing |
| Memory architecture (SQLite, vector DB) | The vault (~60 files) fits in context. Markdown + YAML + git is sufficient. | Cross-run data comparison becomes necessary, or vault outgrows context window |
| Model routing system | No data on which models work for which tasks. Premature optimisation. | Wave 8 instruments the pipeline with model performance data |
| TOML with JSON for API cost reduction | Unproven benefit vs. added complexity | Investigated and cost savings demonstrated |

## Traceability

| Decision | Foundation |
|----------|-----------|
| Schedule existing tools rather than build new infrastructure | Law 3 (Economy) — simplest thing that answers the question |
| launchd for scheduling | D1 (Deterministic Control Surfaces) — native OS scheduler, predictable behaviour |
| Separate mechanical scan from semantic summary | [[AM — Integrity Layers]] — layers run in sequence, mechanical first |
| Summary script uses direct Ollama API call, no abstraction | Law 3 (Economy) — one consumer doesn't justify a framework |
| Local LLM via Ollama for report summarisation | Law 3 (Economy) — no cost, no external dependency for Level 1 daily maintenance work |
| macOS native notification, not Slack | Law 3 (Economy) — local stack uses local notification; don't go to the internet to talk to yourself |
| Phase the work (schedule → summary → notify) | D3 (Controlled Evolution) — graduated steps, each independently useful |
| Runtime artifacts in `04_EXECUTE/runtime/`, not in `tools/` | [[AM — Integrity Layers]] — semantic actors are distinct from mechanical tools |
| Graceful degradation when LLM unavailable | [[AM — Tool Conventions]] Safety Rule 5 — fail safe |
| Notification only on findings | Law 3 (Economy) — signal, not noise |

## Impact Assessment

**What this affects:**
- `04_EXECUTE/runtime/` — currently empty; receives launchd config and summary script
- `04_EXECUTE/tools/vault-maintenance/config/am.conf` — may need updates for unattended operation
- `04_EXECUTE/tools/vault-maintenance/logs/` — receives launchd operational logs
- `05_RECORD/reports/` — receives daily integrity reports automatically (currently receives them only on manual runs)
- SYSTEM_MAP.md — updated to reflect new runtime contents

**What this does NOT affect:**
- Governance documents — no changes
- Tool suite — orchestrate.sh and individual tools are unchanged; Wave 7 schedules them, it does not modify them
- Vault structure — no new folders beyond `runtime/launchd/`

**What could go wrong:**

- **launchd configuration complexity.** plist XML is notoriously finicky. Mitigation: keep the plist minimal (program, arguments, schedule, log paths), test with `launchctl load` and verify with `launchctl list`. The install script validates before installing.
- **Ollama availability.** The summary script depends on Ollama running locally. If Ollama isn't running when the scheduled job fires, the summary fails. Mitigation: graceful degradation — the mechanical report is produced regardless; the summary is additive. The script logs the failure and moves on. Optionally, the launchd plist could ensure Ollama is running before invoking the summary, but that adds coupling. Simpler to let it fail gracefully.
- **Report accumulation.** Daily reports will accumulate in `05_RECORD/reports/`. At one report per day, this is ~365 files per year. Mitigation: not an immediate problem. If it becomes one, a retention policy (archive reports older than N days) is trivial to add. Don't solve it now.
- **The summary script is the first code that invokes an LLM autonomously.** This is a trust boundary. The script must be read-only with respect to the vault — it reads a report file and appends to it, nothing else. It must not write to vault content, create notes, or modify frontmatter. The same principle as Tool Convention 3 applies, extended to semantic actors: report and summarise, don't repair.

## Alternatives Considered

**Alternative 1: cron instead of launchd**
Rejected. cron jobs that fire during sleep simply don't run on macOS. launchd is the native scheduler, handles sleep/wake, and is already available. No advantage to cron.

**Alternative 2: Build a Python daemon that manages scheduling internally**
Rejected. A daemon adds process management, crash recovery, and logging complexity. launchd already provides all of this at the OS level. A daemon would duplicate OS-level scheduling in application code — a Law 3 violation. Deferred to Wave 8 if intelligent task chaining proves necessary.

**Alternative 3: Use Anthropic API (Haiku) instead of Ollama**
Considered. Haiku is proven, high-quality, and already familiar. But it adds per-call cost, requires an internet connection, and introduces an external dependency for daily local maintenance. Ollama is already installed, runs locally, costs nothing, and handles Level 1 summarisation adequately. The three-tier model defines capability needs, not providers — a local model that meets Level 1 requirements is the right choice for daily unattended work. If quality proves insufficient, swapping the endpoint to Anthropic is a one-line change.

**Alternative 4: Skip the LLM summary, just schedule the scripts**
Viable — this is the minimum viable scope (Phase 1 only). The LLM summary is included because it proves a meaningful capability: automated semantic interpretation of mechanical output. It's the first instance of the Integrity Layers sequence running end-to-end without human initiation. But if the wave needs to degrade, Phase 1 alone answers the question.

**Alternative 5: Build notification first, summary later**
Rejected. Notification without summary is "something happened, go read the report." Summary without notification is "the report has a readable conclusion, find it when you're ready." Summary is more valuable because it adds information; notification only adds urgency. Urgency without information is noise.

## Gate Criteria

**This proposal is ready to execute when:**

- [x] Proposal drafted with all required elements
- [x] Adversarial audit completed (alignment, integrity, viability)
- [x] Human (Rob) approves the proposal (2026-03-17)
- [x] Audit findings resolved

**Wave 7 is complete when:**

- [ ] launchd plist created and tested — `launchctl load` succeeds, `run_maintenance.sh` runs on schedule, date-stamped reports land in `05_RECORD/reports/`
- [ ] `run_maintenance.sh` wrapper script coordinates the full sequence and is extensible for Phases 2 and 3
- [ ] Install and uninstall scripts created and tested
- [ ] am.conf updated for unattended operation if needed
- [ ] (If Phase 2) Summary script reads latest health report, invokes llama3.2 via Ollama, appends `## LLM Summary` section with timestamp
- [ ] (If Phase 2) Summary script verifies model availability before invocation and degrades gracefully when Ollama is not running, model is missing, or call fails (exit code 2)
- [ ] (If Phase 2) Summary append is idempotent — re-running does not duplicate the summary
- [ ] (If Phase 3) Notification fires on findings (exit code 1), silent on clean (exit code 0), includes summary text if available
- [ ] README.md in `04_EXECUTE/runtime/` documents installation, configuration, scheduling, and monitoring
- [ ] SYSTEM_MAP.md updated to reflect new runtime contents
- [ ] Wave 7 reflection written and filed in `06_REFLECT/`
- [ ] Capture seed for Wave 8 created in `01_CAPTURE/`

## Proposal Type

[x] Structural — Level 2 (Reviewer gate required)

This proposal creates new executable artifacts in `04_EXECUTE/runtime/` and establishes AM's first autonomous operation. It does not modify governance documents. The integrity layers and tool conventions governance established during Wave 6 design apply unchanged.
