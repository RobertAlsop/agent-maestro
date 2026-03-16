# 06_EXECUTION

**Foundations Alignment**: This layer implements Law 2 (verifiable, reversible, accountable actions) from [[Agent Maestro — Foundations]], providing complete observability and audit trails for all operational work.

## Purpose

The EXECUTION layer is where operational intelligence systems do their work. It contains dashboards, logs, reports, task tracking, weekly planning artifacts, and workflow execution records. This is the layer where agents record what they did, what happened, and what the outcomes were.

The EXECUTION layer is write-heavy (agents constantly record operational state) but read-sparse (except for supervisors reviewing results). It provides the observability and accountability for the system.

## Structure

- **dashboards/**: Dashboards summarizing system health, agent activity, and key metrics
- **logs/**: Structured execution logs, operation records, and audit trails
- **reports/**: CSV reports on agent activity, outcomes, and metrics
- **tasks/**: Task tracking, status updates, and task-specific execution records
- **workflows/**: Workflow execution records and pipeline run logs
- **roadmaps/**: Strategic roadmaps and execution plans
- **weekly_planning/**: Weekly planning artifacts, progress reviews, and retrospectives

## Conventions

### Log Files
- Format: Plain text or CSV with timestamps
- Naming: Descriptive + date (e.g., "agent_execution_2026-03-14.log")
- Timestamps: ISO 8601 format with timezone (e.g., "2026-03-14T10:30:00Z")
- Content: One record per line for machine readability

### Report Files
- Format: CSV with headers
- Naming: Descriptive + report type (e.g., "agent_activity_report.csv", "escalation_report.csv")
- Dates: ISO 8601 format in all date columns
- Follow Structured Data Registry conventions

### Task Records
- Format: Markdown with YAML frontmatter (status tracking) or CSV (bulk listing)
- Status values: pending | in_progress | completed | blocked | escalated
- Include: Owner, created_date, target_date, actual_completion_date

### Workflow Execution Records
- Format: JSON or CSV with execution details
- Include: Pipeline name, start_time, end_time, stages_completed, outcome (success/failure/partial)
- Link to related tasks and projects

## Agent Rules

**Agents MAY**:
- Write to logs/ subdirectory freely (operation logs and audit trails)
- Write to reports/ subdirectory (CSV reports, metrics, activity summaries)
- Update task status and notes in tasks/ subdirectory
- Record workflow execution details in workflows/ subdirectory
- Create new weekly planning artifacts following conventions
- Update dashboard data (if system permits write access)

**Agents MUST NOT**:
- Delete or modify historical logs without escalation (audit trail integrity)
- Fabricate or misrepresent operational data in reports
- Modify task records from other agents without escalation
- Delete workflow execution records without escalation
- Claim task completion without actual completion

**Escalation Required**:
- Deletion or modification of historical logs
- Requests to retract or amend operational reports
- Changes to completed or escalated task status
- Deletion of workflow execution records
- Decisions about system-wide operational changes

## Key Subdirectories

### logs/
Structured execution logs recording agent operations, decisions, and outcomes. Machine-readable format (CSV or line-delimited JSON) for analysis.

Typical content:
- Agent execution logs: What agents did and when
- Decision logs: What decisions were made and rationale
- Error logs: System errors and failures
- Escalation logs: Escalations to humans
- Audit trails: Changes to system state

### reports/
CSV reports summarizing operational data. Generated from logs, task data, and execution records.

Typical content:
- Agent activity report: Hours worked, tasks completed, escalations per agent
- Escalation report: What was escalated, why, outcomes
- Metric report: System-level KPIs (uptime, throughput, accuracy)
- Outcome report: Results of operational work vs. planned objectives

### tasks/
Task tracking and management. Subdirectories by owner, status, or project.

Typical content:
- Task lists: Individual task tracking
- Status updates: Progress on ongoing tasks
- Completion records: Finished tasks with outcomes

### workflows/
Pipeline and workflow execution records. Records what workflows were run, their outcome, and what was produced.

Typical content:
- Workflow execution logs: Each pipeline run with stages, timing, outcome
- Workflow failure analysis: Why workflows failed and what was learned

### dashboards/
Dashboards summarizing system state. May be CSV snapshots, JSON data, or formatted markdown.

Typical content:
- Health dashboard: System health metrics
- Activity dashboard: Agent activity and throughput
- KPI dashboard: Key performance indicators vs. targets

### weekly_planning/
Weekly planning artifacts and progress reviews. Typically markdown with dates.

Typical content:
- Weekly plans: What will be done in the coming week
- Progress reviews: What was actually accomplished
- Retrospectives: What went well, what didn't, lessons learned
- Risk tracking: Identified risks and mitigation status

## CSV Conventions for Reports & Logs

All CSV files in EXECUTION must follow:

- **Encoding**: UTF-8
- **Delimiter**: Comma
- **Dates**: ISO 8601 format (YYYY-MM-DD for dates, YYYY-MM-DDTHH:MM:SSZ for timestamps)
- **Nulls**: Empty cells or "NULL"
- **Headers**: Descriptive names on first row
- **Consistency**: Related CSV files must use aligned schemas

See **Structured Data Registry** in 05_SYSTEMS/memory_architecture/ for detailed CSV conventions.

## Data Flow: Authority → Execution

1. **Authority Layer** (05_SYSTEMS): Defines what agents can do
2. **Workflow Layer** (03_PIPELINES): Defines how work is structured
3. **Execution** (06_EXECUTION): Agents execute within authority and workflow constraints, record results here
4. **Feedback**: Execution results inform future authority changes (improvements via 02_KNOWLEDGE and 05_SYSTEMS)

## Relationship to Other Layers

- **02_KNOWLEDGE**: Execution records may prompt updates to knowledge or patterns
- **03_PIPELINES**: Agents follow pipeline contracts when recording execution details
- **04_PROJECTS**: Project outcomes are recorded from execution logs/reports
- **05_SYSTEMS**: Agents must operate within system constraints defined in SYSTEMS layer
- **01_CAPTURE**: Operational observations captured here may become insights (promote to 02_KNOWLEDGE)

## Agent Execution Cycle

Each agent execution iteration:

1. **Query Memory**: Read authority constraints, pipeline definitions, current operational state
2. **Execute Work**: Perform operations according to constraints and pipeline stages
3. **Log Operations**: Record what was done, decisions made, outcomes achieved
4. **Report Results**: Update task status, write reports, update dashboards
5. **Escalate if Needed**: Escalate decisions that exceed authority

All of steps 1-5 must be auditable and traceable in logs and reports.

## Monitoring & Observability

The EXECUTION layer provides observability through:

- **Logs**: Detailed audit trail of what agents did
- **Reports**: Summarized operational metrics and outcomes
- **Dashboards**: Real-time or near-real-time system state
- **Task Tracking**: Individual task progress and status

Humans monitor these artifacts to supervise agent activity and identify issues needing escalation.

## Historical Retention

Execution records should be retained indefinitely (unless company retention policies require deletion). Historical logs enable:

- Audit trails for compliance
- Analysis of agent performance and behavior over time
- Root cause analysis of failures
- Learning from past experiences

Archive old logs to 99_ARCHIVE when they are no longer needed for active operations.
