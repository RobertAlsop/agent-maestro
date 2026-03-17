# Agent Maestro — Scheduled Execution Runtime

Wave 7 deliverable. Runs the vault-maintenance integrity suite on a daily schedule via macOS launchd, optionally summarises findings with a local LLM, and sends a notification when issues are detected.

## Architecture

```
run_maintenance.sh          ← Entry point (called by launchd)
  ├─ orchestrate.sh         ← Mechanical integrity (Wave 6 tools)
  ├─ summarise_report.py    ← Semantic summary via Ollama (optional)
  └─ notify.sh              ← macOS notification on findings (optional)
```

Each phase degrades gracefully. If the summary script or notification script is missing or fails, the pipeline continues. The mechanical report is always produced.

## Installation

### Prerequisites

- macOS (launchd is macOS-specific)
- The vault-maintenance tool suite in `../tools/vault-maintenance/`
- Python 3 (for the summary script)
- Ollama with `llama3.2` installed (for the summary script): `ollama pull llama3.2`

### Install the launchd agent

```bash
cd 04_EXECUTE/runtime/launchd
./install.sh
```

This:
1. Validates the plist and required scripts
2. Copies the plist to `~/Library/LaunchAgents/`
3. Loads the agent via `launchctl`

The agent runs daily at 06:00 local time.

### Configure the LLM summary (optional)

```bash
cd 04_EXECUTE/runtime
cp config.example.yaml config.yaml
# Edit config.yaml if using a different model or Ollama endpoint
```

### Uninstall

```bash
cd 04_EXECUTE/runtime/launchd
./uninstall.sh
```

## Manual execution

Run the full maintenance sequence manually:

```bash
./04_EXECUTE/runtime/run_maintenance.sh
```

Run just the summary on an existing report:

```bash
python3 04_EXECUTE/runtime/summarise_report.py 05_RECORD/reports/vault_health_report_2026-03-17.md
```

Test the launchd agent immediately (must be installed first):

```bash
launchctl start com.agentmaestro.vault-maintenance
```

## Output

- **Reports:** `05_RECORD/reports/vault_health_report_YYYY-MM-DD.md` — one per day
- **LLM Summary:** Appended to the report under `## LLM Summary` heading
- **Operational logs:** `04_EXECUTE/tools/vault-maintenance/logs/run_maintenance.log`
- **launchd logs:** `04_EXECUTE/tools/vault-maintenance/logs/launchd_stdout.log` / `launchd_stderr.log`

## Configuration

| Setting | File | Default |
|---------|------|---------|
| Schedule | `launchd/com.agentmaestro.vault-maintenance.plist` | Daily at 06:00 |
| Ollama endpoint | `config.yaml` | `http://localhost:11434` |
| LLM model | `config.yaml` | `llama3.2` |
| Vault-specific rules | `../tools/vault-maintenance/config/am.conf` | AM defaults |

## Exit codes

All scripts follow the vault-maintenance convention:

| Code | Meaning |
|------|---------|
| 0 | Clean — no findings |
| 1 | Findings — issues detected |
| 2 | Error — script or dependency failure |

## Troubleshooting

**Agent not running:**
```bash
launchctl list | grep agentmaestro
```

**Check logs:**
```bash
tail -50 04_EXECUTE/tools/vault-maintenance/logs/run_maintenance.log
```

**Plist validation:**
```bash
plutil -lint 04_EXECUTE/runtime/launchd/com.agentmaestro.vault-maintenance.plist
```

**Ollama not responding:**
```bash
ollama list              # Is it running?
curl localhost:11434     # Is the API up?
```
