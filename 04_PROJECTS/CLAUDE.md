# 04_PROJECTS

## Purpose

The PROJECTS layer provides project tracking and lifecycle management. Projects move through defined lifecycle stages (incubating → active → completed) and are recorded with status updates, deliverables, and relationships to other system components.

Projects connect strategy (from 02_KNOWLEDGE governance documents) to execution (in 06_EXECUTION) and are tracked against the overall Agent Maestro roadmap.

## Structure

Projects are organized by lifecycle stage:
- **active/**: Currently active projects with ongoing work
- **incubating/**: New ideas and proposals under evaluation
- **completed/**: Finished projects and their outcomes

Each project typically has a project note (markdown file) containing metadata, status, milestones, and deliverables.

## Conventions

### Project Note Frontmatter
Each project note should include:
- `title`: Project name
- `project_status`: one of [incubating, active, completed]
- `project_owner`: Name or role of the project owner/sponsor
- `created_date`: YYYY-MM-DD
- `expected_completion`: YYYY-MM-DD (if active/incubating)
- `completed_date`: YYYY-MM-DD (if completed)
- `relationships`: Links to related projects, pipelines, and systems
- `tags`: Categorization tags

### Project Note Content
- **Summary**: One-sentence description of what the project achieves
- **Objectives**: Why this project matters and what it delivers
- **Milestones**: Key dates and deliverables
- **Status**: Current state and recent progress
- **Blockers**: Any issues preventing progress
- **Owner**: Who is responsible for moving this project forward
- **Related**: Links to pipelines, systems, and other projects

## Agent Rules

**Agents MAY**:
- Update project status notes with progress information
- Create new project notes in the incubating/ directory
- Update milestones and deliverables in active/ projects
- Move projects from incubating/ to active/ (with owner approval)
- Record completed deliverables in project notes

**Agents MUST NOT**:
- Delete project notes without escalation
- Change project_status from active back to incubating without escalation
- Move projects to completed/ without human sign-off
- Modify project_owner or historical project records without escalation

**Escalation Required**:
- Decisions to archive or delete projects
- Major scope changes to active projects
- Changes to project ownership
- Requests to extend project completion dates significantly

## Key Directories

- **active/**: Projects currently in progress with active work
- **incubating/**: New ideas and proposals under evaluation
- **completed/**: Archived and historical projects

Location: `/sessions/loving-busy-bohr/mnt/Agent Maestro/04_PROJECTS/`

## Project Lifecycle

```
incubating → active → completed
```

1. **Incubating**: New project idea, under evaluation, not yet committed
2. **Active**: Approved and in progress, with milestones and assigned owner
3. **Completed**: Finished, with results documented and archived

Projects should move through this lifecycle in order. Backward movements (e.g., active → incubating) require escalation and justification.

## Relationship to Execution Layer

Projects use pipelines from 03_PIPELINES to execute work. Project status updates reference execution logs and task outcomes from 06_EXECUTION. The relationship is:

Projects (Strategy) → Pipelines (Workflow) → Execution (Operations)

See [[02_Systems/Agent Maestro/04_PROJECTS/CLAUDE]] in 06_EXECUTION/ for how project work is recorded and tracked operationally.
