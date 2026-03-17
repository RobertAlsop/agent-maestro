---
title: "Wave 8 — Capture Seed"
type: pipeline
status: draft
authority_weight: 10
schema_version: 3
created: "2026-03-17"
updated: "2026-03-17"
relationships:
  derives_from:
    - "[[Wave 7 — Reflection]]"
  governs: []
  related:
    - "[[AM — Roadmap]]"
    - "[[AM — Future Waves Register]]"
tags: [capture, seed, wave-8]
---

# Wave 8 — Capture Seed

**Source:** [[Wave 7 — Reflection]]

## Context

Wave 7 proved AM can run things autonomously. The vault is now checked daily via launchd, findings are summarised by a local LLM, and a notification fires when issues are detected.

The question shifts: **Can AM enforce its own rules?**

## Seeds

1. **Pipeline enforcement.** AM has rules (72 Vault Rules, Tool Conventions, Integrity Layers). The integrity tools detect violations after the fact. Can AM prevent violations at the point of action — pre-commit hooks, gate checks that block rather than report?

2. **Git-ops integration.** AM's build protocol requires feature branches, tags, and commit conventions. These are currently human-enforced. Can they be automated — pre-commit hooks that enforce branch naming, commit message format, or frontmatter validation before a commit lands?

3. **Self-observation.** AM now produces daily health reports. Can it observe trends across reports — are findings increasing or decreasing? Which tools consistently find issues? This requires cross-run comparison, which the current one-report-per-day model doesn't directly support.

4. **Orchestrator enhancement.** The `--quiet` mode suppresses per-tool report paths from stdout, which leaves the aggregate report's "Combined Findings" section empty. A small fix to pass report paths through a mechanism other than stdout parsing.

## Priority Signal

The [[AM — Roadmap]] identifies Wave 8 as "pipeline-enforcement + git-ops + self-observation." The first two are high-value (prevention > detection). Self-observation is the more ambitious item and may warrant its own wave if scope expands.

---

*This seed closes the Wave 7 loop. Process it through a brainstorm and proposal before committing to scope.*
