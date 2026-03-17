---
title: "Wave 7 — Reflection"
type: report
status: active
authority_weight: 30
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Agent Maestro — Foundations]]"
    - "[[Proposal — Wave 7 Scheduled Execution]]"
  governs: []
  related:
    - "[[Wave 6 — Reflection]]"
    - "[[AM — Roadmap]]"
    - "[[AM — Integrity Layers]]"
    - "[[AM — Tool Conventions]]"
tags: [reflection, reflect, wave-7]
---

# Wave 7 — Reflection

## Purpose

Close the loop on Wave 7 (Scheduled Execution). This wave asked one question: "Can AM run things?" The answer is yes.

## What Happened

### Starting State

Wave 6 delivered a mechanical integrity tool suite — seven shell scripts that detect structural problems in the vault. But those tools only ran when a human opened a terminal, navigated to the vault, and typed `./orchestrate.sh`. Every check required someone to sit down and do it. AM had detection capability but no operational cadence.

The [[AM — Roadmap]] identified this as the next committed wave. The [[Wave 7 — Brainstorm]] proposed the simplest possible answer: schedule the existing tools via macOS launchd, add an LLM summary, add a notification.

### Key Decisions

1. **Full scope executed — all three phases.** The proposal's degradation plan allowed Phase 1 only (minimum viable) or Phases 1+2. All three phases were built because each was small and independent, and Ollama with llama3.2 was confirmed available on the target machine before building Phase 2.

2. **Wrapper script as the extension point.** `run_maintenance.sh` coordinates the three phases. The launchd plist calls the wrapper, never the individual scripts. Adding or removing phases means editing one file — the plist never changes. This proved its value during testing: each phase could be verified independently.

3. **Runtime artifacts in `04_EXECUTE/runtime/`, tools untouched.** Per [[AM — Integrity Layers]], the mechanical detection tools (`04_EXECUTE/tools/`) were not modified. The runtime layer (`04_EXECUTE/runtime/`) consumes their output and acts on it. The only change to the tools directory was adding `04_EXECUTE/runtime` to the exclude patterns in `am.conf` — so the integrity tools don't scan runtime artifacts (plist XML, Python scripts, shell wrappers) as vault content.

4. **Direct Ollama API call, no abstraction.** The summary script makes a single HTTP call to `localhost:11434`. No provider abstraction layer, no retry logic, no configuration framework. One consumer, one endpoint. The Runtime Provider Layer remains deferred in the Future Waves Register until multiple consumers justify it.

5. **Date-stamped reports preserve history.** Each run produces `vault_health_report_YYYY-MM-DD.md` in `05_RECORD/reports/`. Reports accumulate. No retention policy yet — at one per day, this isn't a problem for years.

### Artifacts Produced

| Artifact | Location | Phase |
|----------|----------|-------|
| `run_maintenance.sh` | `04_EXECUTE/runtime/` | 1 |
| `com.agentmaestro.vault-maintenance.plist` | `04_EXECUTE/runtime/launchd/` | 1 |
| `install.sh` | `04_EXECUTE/runtime/launchd/` | 1 |
| `uninstall.sh` | `04_EXECUTE/runtime/launchd/` | 1 |
| `summarise_report.py` | `04_EXECUTE/runtime/` | 2 |
| `config.example.yaml` | `04_EXECUTE/runtime/` | 2 |
| `notify.sh` | `04_EXECUTE/runtime/` | 3 |
| `README.md` | `04_EXECUTE/runtime/` | — |

### Test Results

Full end-to-end pipeline test completed:

- **Phase 1:** orchestrate.sh ran all 7 tools, detected findings in 5, produced date-stamped report in `05_RECORD/reports/`
- **Phase 2:** summarise_report.py invoked llama3.2 via Ollama, appended `## LLM Summary` section to the report. Idempotency verified — re-running skips the append.
- **Phase 3:** notify.sh fired a macOS notification with the LLM summary text.
- **Plist validation:** `plutil -lint` passed.
- **All scripts:** bash syntax check and Python compile check passed.

## What We Learned

### About Agent Maestro

**The Integrity Layers architecture proved itself.** Wave 6 built the mechanical layer. Wave 7 built the first semantic actor (the summary script) and the first operational actor (the scheduler). The layer separation meant Wave 7 never touched Wave 6 code — it only consumed its output. This is exactly what the architecture predicted: mechanical integrity as a stable foundation that semantic and operational layers build on independently.

**AM now has autonomous operation.** This is the Stage 1 exit criterion from the [[Agent Maestro — Strategy]]: "AM runs scheduled maintenance between human sessions." With launchd installed, the vault is checked daily whether anyone opens it or not. Problems accumulate for at most 24 hours before being detected and reported.

**Local LLM is viable for Level 1 work.** llama3.2 running locally via Ollama produced a useful, accurate summary of the health report. It correctly identified which tools had findings and characterised the nature of the issues. For daily automated maintenance — pattern recognition on structured output — a local model is sufficient and costs nothing.

### About the Process

**The three-phase structure with graceful degradation worked well.** Each phase was independently testable and independently deployable. The wrapper script pattern meant Phase 1 was complete and working before Phase 2 was started.

**The proposal's specificity reduced build decisions to near zero.** The proposal specified every artifact, every location, every design decision with traceability. Building was almost mechanical — translate the specification into code. This is what a good proposal should do: move all the judgment into the proposal phase, so the execution phase is deterministic.

## What Comes Next

Seeds for future work (not commitments):

1. **Report accumulation policy.** Daily reports will eventually need a retention strategy — archive after N days, or compress into weekly/monthly summaries. Not urgent at current scale.

2. **Combined Findings extraction.** The orchestrator's `--quiet` mode prevents per-tool report paths from appearing in stdout, which means the aggregate health report's "Combined Findings" section is empty even when individual tools find issues. This is a Wave 6 orchestrator enhancement, not a Wave 7 concern.

3. **Runtime Provider Layer.** Still deferred. When a second consumer needs LLM access (e.g., a semantic validation tool, or an auto-remediation actor), the abstraction earns its place.

4. **Wave 8 scope.** The [[AM — Future Waves Register]] and [[AM — Roadmap]] identify pipeline enforcement, git-ops, and self-observation as the next capability cluster. With scheduling solved, the question shifts from "can AM run things?" to "can AM enforce its own rules?"

## Process Reflection

This wave followed the universal pipeline cleanly:

- **Capture:** The [[Wave 7 — Brainstorm]] captured the idea. The [[Wave 6 — Reflection]] validated it.
- **Interpret:** The brainstorm was interpreted through the lens of [[AM — Integrity Layers]] and [[AM — Tool Conventions]] — runtime vs. tools, mechanical vs. semantic.
- **Decide:** The [[Proposal — Wave 7 Scheduled Execution]] specified three phases with a degradation plan. Adversarial audit completed. Human approved.
- **Execute:** All three phases built and tested. Feature branch used. Pre-wave tag created.
- **Record:** Date-stamped health report produced automatically. Session documented.
- **Reflect:** This document.

The loop closes with a capture seed in `01_CAPTURE/`.

---

*Filed in `06_REFLECT/`. Capture seed: [[Wave 8 — Capture Seed]]*
