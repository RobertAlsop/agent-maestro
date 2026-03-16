# 02_KNOWLEDGE/governance

## Purpose

The governance subdirectory contains the **highest-authority documents** in the Agent Maestro vault. These documents define the foundational kernel, vision, scope, strategy, operational modes, and structural rules from which all other vault content is derived.

## Document Hierarchy

| Document | Authority Weight | Role |
|----------|-----------------|------|
| **Agent Maestro — Foundations** | 95 | Apex governance. Foundational kernel (3 seeds, 1 meta-principle, 3 laws) + 6 derived principles. All other governance docs must align with this. |
| **Agent Maestro — North Star** | 90 | Core vision: why Agent Maestro exists and what success looks like. |
| **Agent Maestro — Vault Rules** | 85 | Structural rules for vault consistency, navigation, and trustworthiness. Defines schema v3. |
| **Agent Maestro — Scope** | 80 | What Agent Maestro does and does not cover. |
| **Agent Maestro — Strategy** | 80 | Five capability stages from experimentation to intelligence platforms. |
| **Agent Maestro — Modes** | 75 | Six operational modes aligned with the universal pipeline stages. |
| **Agent Maestro — Principles** | 70 | Historical reference. The original 12 principles, superseded by Foundations. |

### Subdirectories

- `roles/` — Worker and Reviewer role definitions (authority boundaries for agents)

## Conventions

- **Foundations is the apex**: When governance documents conflict, Foundations wins.
- **Read before building**: Before starting work in any layer, read the Foundations.
- **Citation required**: Use wiki-link format: `[[Agent Maestro — Foundations]]`
- **Immutability principle**: These documents change infrequently and only through full pipeline cycles with human approval.

## Agent Rules

**Agents MAY:**
- Read all governance documents (mandatory before starting work)
- Reference these documents when explaining decisions
- Create new notes that cite and implement these foundations
- Suggest improvements or modifications (via escalation)

**Agents MUST NOT:**
- Modify governance document content without human approval
- Reinterpret or override the foundational kernel
- Create new canonical governance documents without explicit approval
- Delete or archive governance documents
