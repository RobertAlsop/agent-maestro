# 05_RECORD — Record Stage

## Pipeline Position

Stage 5 of 6. Receives completed work from `04_EXECUTE/` and outcomes from any pipeline stage. Feeds into `06_REFLECT/`.

## Purpose

Record what happened. Every session, every decision, every structural change gets documented here. This is Layer 2 of the memory architecture — structured data that makes the vault's history queryable and traceable.

## Subfolders

### logs/

Operational logs. Currently contains:

- **sessions/** — One session log per build session (see `Template — Session Log` in `02_KNOWLEDGE/templates/`). Also contains `session_index.csv` for quick lookup.

Future logs (escalation, state change, task execution) will be recreated here when new vault tools are built.

### reports/

Audit reports, validation reports, and any other formal assessment outputs. Currently empty — ready for future use.

### archive/

Historical items preserved but no longer active. Organized by wave:

- `wave_5_reports/` — Wave 5 baseline inventory and final audit
- `wave_5.2_reports/` — Old runtime JSON outputs and tool-generated CSVs
- `wave_5.2_logs/` — Old runtime CSV logs (schema v2)
- `wave_5.2_execute/` — Archived runtime and tools from 04_EXECUTE
- `wave_5.2_governance/` — Archived governance documents (Modes, Principles)
- `wave_5.2_concepts/` — Archived old concept files and references
- Various other `wave_5_*` archives from earlier cleanup

## Gate: Entry to Record

Any pipeline stage can write to Record. The gate is format compliance — use the session log template, follow CSV conventions (UTF-8, comma-delimited, ISO 8601 dates).

## Conventions

- Session logs follow the template in `02_KNOWLEDGE/templates/Template — Session Log.md`
- CSV files: UTF-8, comma-delimited, ISO 8601 dates
- Archive folders are named by wave and content type
- Nothing is ever deleted — items move to archive with their `derives_from` relationships preserved
