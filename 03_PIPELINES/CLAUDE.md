# 03_PIPELINES

## Purpose

The PIPELINES layer defines operational workflows and pipeline contracts that guide agent execution. A pipeline is a series of stages with clear entry conditions, processing rules, exit conditions, and success criteria. Pipelines implement the Workflow Layer of the Four-Layer Model.

Agents consult pipelines before executing workflows to understand:
- What stages must be completed in sequence
- What conditions must be met to enter or exit each stage
- What outputs are produced at each stage
- When escalation to a human supervisor is required

## Structure

Pipelines are organized by operational context:
- **deployment/**: Pipelines for deploying systems to production
- **development/**: Pipelines for building and developing new features
- **exploration/**: Pipelines for research and experimentation
- **learning/**: Pipelines for training and knowledge acquisition
- **maintenance/**: Pipelines for system maintenance and updates

Each pipeline directory may contain multiple pipeline definitions (typically one per file).

## Conventions

### Pipeline Document Structure
Each pipeline should define:
- **Name**: Identifier for the pipeline
- **Purpose**: What this pipeline achieves
- **Stages**: Ordered list of processing stages
- **Entry Conditions**: Requirements to begin the pipeline
- **Exit Conditions**: Requirements to complete the pipeline
- **Stage Transitions**: Rules for moving between stages
- **Escalation Points**: Where human approval is required
- **Success Criteria**: How to know the pipeline succeeded
- **Failure Modes**: Common failure patterns and recovery

### Naming Convention
- Pipeline files use descriptive titles in Title Case
- Pipeline stage names use ALL_CAPS (e.g., VALIDATION, EXECUTION, REVIEW)

## Agent Rules

**Agents MAY**:
- Read pipeline contracts to understand workflow requirements
- Execute pipelines according to their stage definitions
- Record outputs at each stage following the pipeline's schema
- Request clarification on pipeline requirements

**Agents MUST NOT**:
- Skip stages or modify the sequence without escalation
- Proceed to the next stage without meeting exit conditions
- Ignore escalation points that require human approval
- Modify pipeline definitions without escalation

**Escalation Required**:
- Changes to pipeline definitions (stages, conditions, or success criteria)
- Requests to bypass stages or modify the pipeline sequence
- Decisions about whether to abort a pipeline run
- Conflicts between pipeline requirements and other constraints

## Key Pipelines

The following pipeline categories exist:

- **deployment/**: Pipelines for deploying systems to production environments
- **development/**: Pipelines for building, testing, and integrating new features
- **exploration/**: Pipelines for research, prototyping, and experimentation
- **learning/**: Pipelines for knowledge acquisition and skill development
- **maintenance/**: Pipelines for system maintenance, updates, and upgrades

Location: `/sessions/loving-busy-bohr/mnt/Agent Maestro/03_PIPELINES/`

## Pipeline Execution Model

When an agent executes a pipeline:

1. **Entry**: Verify entry conditions are met
2. **Stage Loop**: For each stage:
   - Execute stage processing
   - Collect outputs
   - Verify exit conditions
   - Handle escalation points
3. **Exit**: Verify pipeline exit conditions are met
4. **Reporting**: Record pipeline outcome (success/failure/partial)

Pipelines are deterministic and repeatable. The same input to the same pipeline should produce consistent results.

## Relationship to Authority Layer

Pipelines are subject to authority constraints defined in 05_SYSTEMS/authority_architecture. Some stages may require specific authority permissions (e.g., only Executive Agents can approve production deployments). The compiled governance artifacts in 05_SYSTEMS define which agents can execute which pipeline stages.

See [[02_Systems/Agent Maestro/03_PIPELINES/CLAUDE]] in 05_SYSTEMS/agent_systems/ for how agent roles are mapped to pipeline execution rights.
