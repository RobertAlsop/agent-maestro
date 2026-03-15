# 02_KNOWLEDGE/governance

## Purpose

The governance subdirectory contains the **highest-authority documents** in the Agent Maestro vault. These documents define the foundational kernel, vision, scope, strategy, operational modes, and structural rules from which all other systems are derived.

## Document Hierarchy

| Document | Authority Weight | Role |
|----------|-----------------|------|
| **Agent Maestro — Foundations** | 95 | Apex governance. Foundational kernel (3 seeds, 1 meta-principle, 3 laws) + 6 derived principles. All other governance docs must align with this. |
| **Agent Maestro — North Star** | 90 | Core vision: why Agent Maestro exists and what success looks like. |
| **Agent Maestro — Vault Rules** | 85 | Structural rules for vault consistency, navigation, and trustworthiness. Includes the validation checklist (merged from Note Quality Rules). |
| **Agent Maestro — Scope** | 80 | What Agent Maestro does and does not cover. |
| **Agent Maestro — Strategy** | 80 | Five capability stages from experimentation to intelligence platforms. |
| **Agent Maestro — Modes** | 75 | Five operational modes (Exploration, Architecture, Deterministic, Execution, Evolution) mapped to the Process seed. |
| **Agent Maestro — Principles** | 70 | Historical reference. The original 12 principles, now superseded by Foundations. Retained for traceability. |

## Conventions

- **Foundations is the apex**: When governance documents conflict, Foundations wins.
- **Read before building**: Before starting work in any layer, read the relevant sections of Foundations.
- **Citation required**: Use full wiki-link format: `[[Agent Maestro — Foundations]]`
- **Immutability principle**: These documents change infrequently and only through deliberate governance processes with human approval.

## Agent Rules

**Agents MAY**:
- Read all governance documents (mandatory before starting work)
- Reference these documents when explaining decisions
- Create new notes that cite and implement these foundations
- Suggest improvements or modifications (via escalation)

**Agents MUST NOT**:
- Modify the content of any governance document without human approval
- Reinterpret or override the foundational kernel
- Create new canonical governance documents without explicit approval
- Delete or archive governance documents

**Escalation Required**:
- ANY modification to ANY governance document
- Proposals to add new derived principles or modify the kernel
- Requests to change authority weights in this directory

## Relationship to Authority Architecture

These governance documents are the source material for the **Authority Pack Compiler** in `05_SYSTEMS/authority_architecture/compiler/`. The compiler transforms these principles and scope statements into executable authority packs and compiled governance artifacts.

Changes to governance documents may trigger recompilation of authority packs. See `05_SYSTEMS/authority_architecture/compiler/` for the compilation pipeline.
