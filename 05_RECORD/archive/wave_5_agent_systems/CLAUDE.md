# 05_SYSTEMS/agent_systems

## Foundations Alignment

This directory implements the **Process seed** (Irreducible Loop) and **Structure seed** (7 Primitives) from [[Agent Maestro — Foundations]]. The Executive-Supervisor-Specialist pattern reflects D6 (Separation of Powers). Escalation paths enforce D4 (Human Sovereignty).

## Purpose

The Agent Systems subdirectory defines the constellation of agents that operate in the Agent Maestro environment, including their roles, responsibilities, relationships, and runtime characteristics. It contains the architecture for the Executive-Supervisor-Specialist pattern, shared services, constellation definitions, and the registry mapping which agents are active in the system.

This is the most critical subdirectory for understanding who the agents are and how they work together.

## Structure

- **Agent Ecosystem.md**: Overview of the agent ecosystem (all agents, their categories, relationships)
- **Agent Runtime Architecture.md**: How agents are instantiated, initialized, and execute at runtime
- **Agent System Architecture.md**: Architecture of multi-agent systems and how individual agents coordinate
- **Agent Workflow Architecture.md**: How agents execute workflows and respect pipeline contracts
- **Multi-Agent Systems.md**: Patterns for coordinating multiple agents working together
- **constellations/**: Agent constellation definitions (groups of agents working toward shared goals)
- **executive_layer/**: Executive agent definitions and their authority/responsibilities
- **shared_services/**: Shared services that all agents depend on (logging, memory access, escalation)
- **constellation_registry.csv**: Registry of all active agent constellations and their status

All files located in `05_SYSTEMS/agent_systems/`

## Agent Roles

The system implements the Executive-Supervisor-Specialist pattern with three roles:

### Executive Agents
- **Authority**: High (can make strategic decisions, approve escalations)
- **Responsibilities**: Overall system coordination, human escalation, major decisions
- **Constraints**: Must justify all decisions, visible decision-making
- **Location**: executive_layer/ subdirectory

### Supervisor Agents
- **Authority**: Medium (can supervise specialists, handle local coordination)
- **Responsibilities**: Oversee specialist agents, coordinate work, escalate to executives
- **Constraints**: Must follow executive decisions, report regularly
- **Location**: constellation-specific

### Specialist Agents
- **Authority**: Low (task execution, limited decision-making)
- **Responsibilities**: Execute specific tasks, follow pipelines, report outcomes
- **Constraints**: Must follow supervisor direction, respect authority constraints
- **Location**: constellation-specific

## Agent Constellations

An agent constellation is a group of agents (typically Executive + Supervisors + Specialists) organized around a shared business domain or function. Each constellation has:

- **Name**: Unique identifier for the constellation
- **Purpose**: What this constellation achieves
- **Executive Agent**: The agent responsible to humans
- **Supervisor Agents**: Agents overseeing specialist work
- **Specialist Agents**: Task execution agents
- **Authority Pack**: The compiled authority artifact governing this constellation
- **Shared Services**: What services this constellation depends on

See constellation/ subdirectory for specific constellation definitions.

## Conventions

### Agent Names
- Format: "[Domain] — [Role]"
- Example: "Customer Service — Executive" or "Content Analysis — Supervisor"
- Agent names must be unique within the system

### Constellation Registry
The file `constellation_registry.csv` contains:
- Constellation name
- Purpose
- Executive agent name
- Number of supervisor agents
- Number of specialist agents
- Authority pack version
- Status (active | paused | experimental)
- Created date

### Frontmatter Requirements
All agent definition documents must include:
- `title`: Agent name
- `agent_role`: executive | supervisor | specialist
- `constellation`: Which constellation(s) this agent belongs to
- `authority_pack_version`: Version of authority pack governing this agent
- `shared_services`: Which services this agent depends on
- `created_date`: YYYY-MM-DD
- `status`: active | paused | archived

## Agent Rules

**Agents MAY**:
- Read other agents' architecture and role definitions
- Query constellation_registry.csv to understand the system structure
- Reference their own role and authority definitions when explaining constraints
- Collaborate with other agents as defined in their constellation

**Agents MUST NOT**:
- Modify agent definitions without escalation
- Change their own role or authority constraints
- Delete constellation definitions
- Misrepresent their role or authority to other agents
- Act outside their defined constellation

**Escalation Required**:
- Changes to agent role definitions
- Additions or removals of agents from system
- Changes to constellation structure or composition
- Modifications to executive agent assignments
- Decisions to pause or archive agents

## Key Documents

- **Agent Ecosystem.md**: Who are all the agents? Categories and relationships
- **Agent Runtime Architecture.md**: How are agents instantiated and initialized?
- **Agent System Architecture.md**: How do multi-agent systems work?
- **Agent Workflow Architecture.md**: How do agents execute workflows?
- **Multi-Agent Systems.md**: Patterns for multi-agent coordination

## Shared Services

All agents depend on shared services including:

- **Logging Service**: Recording agent operations and decisions
- **Memory Service**: Accessing knowledge graphs and structured data
- **Escalation Service**: Escalating decisions to humans
- **Pipeline Service**: Consulting pipeline definitions
- **Authority Service**: Checking permission constraints
- **Reporting Service**: Writing operational reports

See shared_services/ for service specifications.

## Executive Layer

Executive agents are special: they represent the system to humans and have authority to make system-level decisions. Executive agents:

- Are the point of contact with human supervisors
- Make strategic decisions and authorize major actions
- Escalate difficult decisions to humans
- Are responsible for constellation outcomes

Executive agents must be transparent about their reasoning and decisions. All Executive decisions are logged and auditable.

See executive_layer/ for Executive agent definitions.

## Constellation Examples

A typical constellation might include:

- 1 Executive agent (Customer Service — Executive)
- 2-3 Supervisor agents (Support Quality Supervisor, Support Operations Supervisor)
- 5-10 Specialist agents (Ticket Handler, Email Responder, Knowledge Base Assistant, etc.)

Constellations can be specialized (all agents in a domain) or functional (agents performing specific functions across domains).

## Registry Management

The constellation_registry.csv is the single source of truth for what agents are active. It should be:

- Updated whenever agents are added/removed
- Reviewed regularly to ensure accuracy
- Kept in sync with actual agent configurations
- Used by humans to monitor system composition

## Relationship to Authority Architecture

Each constellation is governed by a compiled authority artifact from 05_SYSTEMS/authority_architecture/compiler/. Agent actions are constrained by the constellation's authority pack.

See the authority_architecture CLAUDE.md for how authority packs govern agent behavior.

## Relationship to Execution Layer

Agent systems execute according to rules defined here. Agents in active constellations record their work in 06_EXECUTION. Execution logs should show constellation membership and role of the executing agent.
