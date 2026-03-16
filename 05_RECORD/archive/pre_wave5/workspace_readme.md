# Vault Curator MWP Workspaces

## Overview

MWP (Modular Workspace Protocol) workspaces provide isolated, sandboxed execution environments for specialist agents in the [[Vault Curator constellation]]. Each workspace is a self-contained directory structure that stages inputs, receives compiled authority, executes tasks, and produces outputs.

## Why Workspaces?

**Isolation**: Each specialist operates in its own sandbox, preventing cross-contamination of authority, artifacts, or execution context.

**Auditability**: All inputs and outputs are stored in the workspace, creating a complete audit trail of what happened and when.

**Parallelization**: Multiple specialists can execute simultaneously without interfering with each other's work.

**Reusability**: Workspace structure is standardized across all specialists, making it easy to extend with new audit tasks.

**Recovery**: If a specialist fails, its workspace provides complete context for investigation and retry.

## Directory Structure

### Reference Implementation: link_auditor

```
workspaces/link_auditor/
  ├── authority/          # Compiled authority artifacts (populated at runtime)
  │   └── vault_curator_link_auditor.compiled.json
  │
  ├── agents/             # Agent definition (populated at runtime)
  │   └── link_auditor_agent.json
  │
  ├── stages/             # Stage contract (populated at runtime)
  │   └── execution_stage.yaml
  │
  ├── references/         # Vault file index (populated at runtime)
  │   ├── vault_file_index.json
  │   ├── vault_links_graph.json
  │   └── vault_metadata_index.json
  │
  └── artifacts/          # Output directory (workspace produces outputs here)
      ├── link_audit_report.csv
      ├── logs/
      │   └── execution.log
      └── escalations/
          └── escalation_queue.json
```

### Runtime Population

When the constellation executes, the Supervisor populates each workspace directory:

1. **authority/**: Copy compiled authority artifact
2. **agents/**: Copy agent definition JSON
3. **stages/**: Copy execution stage contract
4. **references/**: Copy vault file index and link graph snapshots

Specialists then execute in their workspace and write outputs to **artifacts/**.

## Workspace Lifecycle

### Initialization (by Supervisor)

1. Create or reset workspace directories
2. Populate `authority/` with compiled authority artifact
3. Populate `agents/` with agent definition
4. Populate `stages/` with execution contract
5. Populate `references/` with vault context snapshots
6. Verify all inputs present and valid
7. Mark workspace READY_FOR_EXECUTION

### Execution (by Specialist)

1. Specialist reads authority from `authority/`
2. Specialist reads agent context from `agents/`
3. Specialist reads execution contract from `stages/`
4. Specialist reads vault references from `references/`
5. Specialist performs task (e.g., link audit)
6. Specialist writes results to `artifacts/`
7. Specialist logs execution to `artifacts/logs/`
8. Specialist writes completion signal
9. Workspace marked EXECUTION_COMPLETE

### Collection (by Supervisor)

1. Supervisor detects workspace completion
2. Supervisor reads all artifacts from `artifacts/`
3. Supervisor validates output format (CSV, JSON, etc.)
4. Supervisor aggregates results from all workspaces
5. Supervisor may clean up old workspace for next cycle

## File Specifications

### authority/ — Compiled Authority Artifacts

**Format**: JSON (compiled from YAML authority pack)

**Example**: `vault_curator_link_auditor.compiled.json`

Contains:
- Role definition
- Authority type and scope
- Decision contracts
- Constraints and validation rules
- Escalation paths

Specialist reads this to understand its decision authority and execution bounds.

### agents/ — Agent Definitions

**Format**: JSON (compiled from markdown agent definition)

**Contains**:
- Agent ID (e.g., CONST.vault_curator.agent.specialist.link_auditor)
- Role name
- Authority pack reference
- Configuration parameters
- Task instructions

Specialist reads this to understand its role and configuration.

### stages/ — Execution Stage Contracts

**Format**: YAML (execution contract)

**Contains**:
- Task specification
- Input requirements
- Output expectations
- Success criteria
- Timeout and resource limits

Specialist reads this to understand what it must accomplish.

### references/ — Vault Context Snapshots

**Format**: JSON

**Files**:
- `vault_file_index.json` — list of all files, paths, metadata
- `vault_links_graph.json` — complete link graph (for orphan detection)
- `vault_metadata_index.json` — all frontmatter metadata snapshot

Created by Supervisor before delegating task. Specialists use these as read-only references.

### artifacts/ — Output Directory

**Subdirectories**:

```
artifacts/
  ├── <primary_output>.csv     # Main task result (e.g., link_audit_report.csv)
  ├── logs/
  │   ├── execution.log        # Execution transcript
  │   └── timing.log           # Timing data
  └── escalations/
      └── escalation_queue.json # Items requiring Executive/human decision
```

**CSV Format** (all task outputs):

```
column1,column2,column3,...
value1,value2,value3,...
```

Example (link audit):
```
source_file,broken_link_text,target,backlink_count,severity
02_KNOWLEDGE/concepts/Agent.md,[[Missing Concept]],Missing Concept,3,HIGH
```

**Execution Log** (log format):

```
[2026-03-14T14:32:15Z] STARTED: Link Auditor task
[2026-03-14T14:32:16Z] READ_CONFIG: vault_curator_link_auditor.compiled.json
[2026-03-14T14:32:20Z] SCAN_VAULT: Processing 250 files
[2026-03-14T14:32:45Z] AUDIT_LINKS: Found 1250 references, 23 broken
[2026-03-14T14:32:50Z] GENERATE_REPORT: Writing link_audit_report.csv
[2026-03-14T14:32:51Z] COMPLETED: SUCCESS (23 broken links found)
```

**Escalation Queue** (JSON format):

```json
{
  "escalations": [
    {
      "escalation_id": "ESC-001",
      "source_file": "file.md",
      "action_type": "DELETE",
      "reason": "True orphan detected",
      "priority": "MEDIUM",
      "evidence": { ... },
      "recommended_action": "Review for archival"
    }
  ]
}
```

## Workspace Standards

### Naming Conventions

- Workspace directory named after specialist: `link_auditor`, `schema_validator`, `orphan_detector`
- Agent IDs use format: `CONST.vault_curator.agent.specialist.<role>`
- Authority packs named: `vault_curator_<role>.yaml`
- Compiled artifacts named: `vault_curator_<role>.compiled.json`

### File Permissions

- Read-only: `authority/`, `agents/`, `stages/`, `references/`
- Read-write: `artifacts/`, `logs/`, `escalations/`

### Cleanup Policy

- Old workspace runs are archived to `workspaces/<specialist>/archive/<timestamp>/`
- Current run stored in `workspaces/<specialist>/` (overwritten each cycle)
- Execution logs permanently retained in archive

## Using Workspaces in Practice

### For Supervisors

**Initialize Workspace**:
```
supervisor.populate_workspace(
  workspace="link_auditor",
  authority=compiled_authority,
  agent_definition=agent_def,
  vault_snapshot=current_vault_state
)
```

**Delegate Task**:
```
supervisor.delegate_task(
  specialist="link_auditor",
  task="RUN_AUDIT",
  workspace="workspaces/link_auditor/",
  expected_output="link_audit_report.csv"
)
```

**Collect Results**:
```
results = supervisor.collect_results(
  workspace="workspaces/link_auditor/",
  expected_files=["link_audit_report.csv"]
)
```

### For Specialists

**Initialize**:
```
workspace = load_workspace("workspaces/link_auditor/")
authority = read_authority(workspace.authority_path)
agent = read_agent_definition(workspace.agents_path)
vault_index = read_vault_index(workspace.references_path)
```

**Execute**:
```
execute_task(agent, authority, vault_index)
```

**Output**:
```
write_report(workspace.artifacts_path, results)
write_log(workspace.artifacts_path + "/logs/", execution_log)
```

## Testing Workspaces

Workspaces are independent, so you can test a specialist in isolation:

```bash
# Initialize test workspace
mkdir -p workspaces/link_auditor/authority
mkdir -p workspaces/link_auditor/agents
mkdir -p workspaces/link_auditor/artifacts/logs

# Copy test authority and agent definitions
cp test_authority.json workspaces/link_auditor/authority/
cp test_agent.json workspaces/link_auditor/agents/

# Run specialist
python link_auditor.py workspaces/link_auditor/

# Check outputs
ls -la workspaces/link_auditor/artifacts/
```

## Related Documentation

- [[Vault Curator constellation]] — overview
- [[CONST.vault_curator.agent.specialist.link_auditor]] — reference specialist
- [[02_Systems/Agent Maestro/02_KNOWLEDGE/concepts/Authority Architecture]] — how authority works
- [[Modular Workspace Protocol]] — MWP specification
