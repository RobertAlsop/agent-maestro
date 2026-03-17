# Wave 8.2 — Capture Seed

Source: [[Wave 8.2 — Reflection]]
Created: 2026-03-17

---

## Immediate Debt

The Wave 8.2 tools surfaced real gaps on first run. These need to be resolved before or during Wave 8.3:

1. **Wave 8.1 reflection is missing.** Wave 8.1 is ✓ in the Roadmap but no reflection exists in `06_REFLECT/`. Write it.
2. **Wave 7 proposal not archived.** Still in `active/` after wave completion. Move to `05_RECORD/archive/` with `status: archived`.
3. **`AM — Future Waves Register` authority_weight is 60.** Below governance floor of 70. Raise to 70 with a note explaining why.
4. **`Git Best Practices for AI-Assisted Builds.md` type mismatch.** Lives in `02_KNOWLEDGE/protocols/` but has type: concept. Either move to concepts/ or correct the type. Needs human decision.
5. **Old reflections (5.1, 5.2, 6) have no capture seeds.** Pre-governance gaps. Create retroactive seeds or document why they're exempt.

## Wave 8.3 — Git-Ops

The next registered wave. Needs its own design conversation. Key questions:

- What does AM-aware git enforcement look like? What are the minimum viable checks?
- Branch naming convention — current informal practice: `wave-X.Y-description`. Codify?
- Commit format — current: descriptive messages. Do we need `SES-XXX:` prefixes enforced?
- Tag management — `pre-<description>` before major changes. Currently manual. Automate?
- Uncommitted changes detection — should the health check flag dirty working tree?
- Where does git-ops tooling live? `04_EXECUTE/tools/vault-maintenance/` or a separate `git-ops/` suite?

## Reflections on the Process

**The governance-first approach paid off.** Wave 8.1 wrote [[AM — Artifact Lifecycles]] before Wave 8.2 built the tools. The result: the tools were almost a direct translation of the spec. Each check mapped to an explicit "Mechanical checks" section in the lifecycle document. This is the right order of operations.

**The type vocabulary needs a `reflection` type.** Currently reflections use type: `report`. This causes false positives in type/folder consistency checks (reports expected in `05_RECORD/reports/`, reflections live in `06_REFLECT/`). Workaround: excluded `report` from `type_folder_map`. Long-term: add `reflection` to the controlled vocabulary in [[Agent Maestro — Vault Rules]]. Stage 1 debt item.

**The two-bug pattern.** Both bugs found during testing were variations of the same root cause: too-greedy matching without explicit boundary constraints. `[^✓]*` crossing lines; content search finding adjacent waves. The pattern is: when matching structured text (file contents, identifiers), always constrain by explicit boundary, not by "doesn't contain X." This is a reusable heuristic for future tool development.

## Future Tooling Ideas

- **Wave 8.3 Git-Ops tools** — branch check, commit format, dirty tree detection
- **Retroactive seed generator** — for old reflections that predate the seed requirement, a simple template to create minimal seeds
- **Wave 8.1 reflection** — separate from tooling: the governance wave's reflection needs to be written
- **Authority weight audit** — a focused review of all authority_weight values across the vault to ensure consistency and correct the Future Waves Register gap
