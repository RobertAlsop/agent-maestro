---
type: map
note_class: navigation
domain: governance
layer: knowledge
schema_version: 2
title: "Agent Maestro — Quickstart"
created_date: 2026-03-14
last_modified: 2026-03-14
status: active
audience: all
authority_weight: 30
tags:
- agent_maestro
- governance
- quickstart
- getting_started
supersedes: []
superseded_by: []
review_status: draft
version: 1
canonical: false
resolution_basis: authority_weight
source_type: ai_authored
---

# Agent Maestro — Quickstart Guide

Get from zero to a compiled constellation in under 30 minutes.

## 1. What is Agent Maestro?

Agent Maestro is the discipline of designing, governing, and evolving operational intelligence systems composed of networks of intelligent agents. Its mission is not to create smarter AI. It is to create more reliable intelligent systems. You accomplish this by writing modular governance contracts that define exactly what each agent may decide and execute—and then compiling those contracts into runtime-enforceable governance artifacts.

## 2. The Three Things You Need to Know

### Authority Packs: Modular Governance Contracts

An authority pack is a YAML file that defines what an agent may decide and execute. Think of it as a job description with teeth. It specifies: the agent's role (Executive, Supervisor, or Specialist), the domain it operates in, the actions it's allowed to take, the conditions that must be met, the rules it must follow, and the escalation path when it encounters a decision outside its authority. Authority packs are composable: a Specialist pack can inherit from a Supervisor pack, which inherits from an Executive pack. Each child narrows the scope and overrides the parent's rules to fit its narrower responsibility. The result is a clear, auditable chain of decision-making authority.

### Constellations: Governed Clusters of Agents

A constellation is a governed cluster of agents organized in a three-level hierarchy: Executive → Supervisor → Specialist. The Executive sets policy and makes the strategic decisions. The Supervisor delegates tasks to specialists, aggregates their results, and applies fixes that fall within authority. Each Specialist executes a narrow, well-defined job (auditing links, validating schemas, detecting orphaned notes) and reports back. When any agent encounters a decision outside its authority, it escalates to the next level up. This hierarchy creates a feedback loop: specialists report problems, supervisors classify and attempt fixes, executives make judgment calls, and unresolvable issues escalate to human operators.

### The Compiler: Transform Authority Packs into Governance Artifacts

The compiler is a Python tool that reads authority packs and outputs JSON governance artifacts. It performs 8 stages of transformation: input validation, inheritance resolution, rule flattening, escalation binding, control gate compilation, evidence validation setup, and output formatting. The result is a compiled JSON artifact that can be loaded at runtime and enforced by your agents. The compiled artifact contains the full inheritance chain resolved and merged into one document, with all overrides tracked and all escalation paths bound to their targets.

## 3. Explore the Vault Curator Constellation

The Vault Curator is a working constellation already built into this vault. In the next five steps, you'll walk through it — reading the authority packs, running the compiler yourself, and tracing the full governance chain. The Vault Curator is a three-agent system that audits and maintains this knowledge vault: the Executive sets policy, the Supervisor coordinates specialist tasks and applies fixes, and specialists (Link Auditor, Schema Validator, Orphan Detector) perform focused audits.

### Step 1: Read the Executive Authority Pack

Navigate to the executive pack:

```
05_SYSTEMS/authority_architecture/packs/constellation_packs/vault_curator/executive.yaml
```

Scan the key sections:

- **pack_id**: `CONST.vault_curator.executive` — unique identifier for the Executive agent
- **authority_type**: `decision` — this agent makes decisions, not just executes
- **scope**: The boundaries of what this agent may touch. For the Vault Curator Executive, it's "vault governance" (schema compliance, link integrity, knowledge graph consistency)
- **governed_actions**: A list of actions the agent may take. Most are `allowed`, some require `requires_escalation` (file deletion, modifying canonical documents)
- **rules**: Mandatory rules that the agent must follow. For example, "All maintenance decisions must be traceable to audit report data" and "Destructive operations always escalate to human"
- **escalation**: Where this agent escalates unresolved issues. The Executive escalates to `human_operator`

Notice that the Executive has wide authority: it can approve non-destructive fixes and delegate audits. But destructive operations (file deletion) and changes to high-authority documents are blocked and escalated.

### Step 2: Read a Specialist Authority Pack

Navigate to the Link Auditor specialist pack:

```
05_SYSTEMS/authority_architecture/packs/constellation_packs/vault_curator/specialist_link_auditor.yaml
```

The key insight here is inheritance. Look at line 6:

```yaml
inherits_from: CONST.vault_curator.supervisor
```

The Link Auditor doesn't inherit from the Executive directly. It inherits from the Supervisor. This creates a chain: **Executive → Supervisor → Specialist**. The specialist inherits the rules and constraints of the Supervisor, which inherits the rules of the Executive.

Now look at the specialist's scope and actions. It's much narrower than the Executive:

- **scope**: Only "Wiki-link validation"
- **governed_actions**: Only four actions, all read-only. Notice `"Modify vault files": permission: denied` — the specialist is read-only by design. It finds broken links but doesn't fix them. That's the Supervisor's job.

When you compile this pack, the compiler will resolve the inheritance chain, merge all rules from the Executive and Supervisor, and flatten them into a single JSON document. The specialist's narrower scope will override the parent's broader rules.

### Step 3: Run the Compiler

Open a terminal in the vault root and run:

```bash
cd /sessions/loving-busy-bohr/mnt/Agent Maestro

# Install dependencies (one time only)
pip install pyyaml jsonschema

# Compile all Vault Curator packs
python 05_SYSTEMS/authority_architecture/compiler/prototype/compiler.py \
  05_SYSTEMS/authority_architecture/packs/constellation_packs/vault_curator/ \
  --vault-root . \
  --output-dir 05_SYSTEMS/authority_architecture/compiler/prototype/artifacts
```

Watch the output. You'll see something like:

```
✓ Stage 1: Input Validation (8/8 passes)
✓ Stage 2: Inheritance Resolution
✓ Stage 3: Rule Flattening
✓ Stage 4: Escalation Binding
✓ Stage 5: Control Gate Compilation
✓ Stage 6: Evidence Validation Setup
✓ Stage 7: Host Binding
✓ Stage 8: Output Formatting
```

The compiler processes each pack through all eight stages. When it encounters the Link Auditor pack, it resolves the inheritance chain (Executive → Supervisor → Link Auditor), merges the rules, and flattens everything into a single document.

### Step 4: Read the Compiled Artifact

Navigate to the artifacts directory:

```
05_SYSTEMS/authority_architecture/compiler/prototype/artifacts/
```

Open the compiled Link Auditor artifact:

```
CONST_vault_curator_specialist_link_auditor_compiled.json
```

Compare it to the original YAML. You'll see several changes:

1. **Inheritance flattened**: The `inherits_from` field is gone. All rules from the Executive and Supervisor are now merged into this document.

2. **All governance merged**: Fields from all three packs are combined. For example, the specialist inherits the Executive's `evidence_requirements` (audit reports must exist) and the Supervisor's control gates (audit must complete before fixes).

3. **Escalation paths bound**: The escalation chain is now explicit. When the Link Auditor escalates, it points to the full path: `CONST.vault_curator.supervisor`, which in turn escalates to `CONST.vault_curator.executive`, which escalates to `human_operator`.

4. **Host binding added**: The compiler adds metadata about where the artifact was compiled, when, and which schema version it conforms to.

This JSON file is what your agents load at runtime. It's the source of truth for what the agent may or may not do.

### Step 5: Trace an Escalation Path

Now walk through a concrete example of how the hierarchy works when a problem arises.

**Scenario**: The Link Auditor finds 15 broken wiki-links while auditing vault notes.

1. **Link Auditor executes**: It scans all markdown files, classifies each link as valid, broken, or ambiguous, and writes a CSV report to `06_EXECUTION/reports/link_audit_report.csv`. Its authority pack says `"Modify vault files": permission: denied`, so it stops here. It cannot fix anything.

2. **Report escalates to Supervisor**: The Supervisor receives the audit report. Its authority pack says it can `"Apply safe renames (broken link fixes)"` but only `"when link target is unambiguous"`. It scans the report:
   - 10 links have unambiguous targets (the target file exists, only one match). The Supervisor fixes these by renaming the links in the vault files.
   - 5 links are ambiguous (the target is unclear or the file doesn't exist). The Supervisor cannot resolve these within its authority.

3. **Ambiguous cases escalate to Executive**: The Supervisor escalates the 5 ambiguous cases to the Executive. The Executive's rules say it can `"Approve non-destructive fixes"` and `"Delete vault files"` but only with `requires_escalation`. The Executive reviews the ambiguous cases and decides: three links should be updated to point to a different file (non-destructive fix, within authority), and two links point to deleted files and should be removed (destructive, requires escalation).

4. **Final escalation to human operator**: The Executive escalates the file deletions to the human operator via email or a task queue. A human reviews the context, confirms the files are truly orphaned, and approves deletion. The human operator then executes the deletions or signals back to the Executive to proceed.

This cascading escalation ensures that no decision is made outside the scope of the agent that makes it, and every unresolvable issue bubbles up the chain until it reaches a human.

## 4. Where to Go Next

- [[Agent Maestro — Navigation Map]] — Explore the full knowledge base
- [[Agent Maestro — Principles]] — Learn the foundational design philosophy
- [[Agent Maestro Layer Model]] — Understand the five layers of the system
- [[Model Workspace Protocol]] — Learn how agents collaborate within workspaces
- [[Compiler Pipeline]] — Dive deep into the 8-stage compilation process

## 5. Glossary

**Agent**: An autonomous entity in the constellation that makes decisions and executes actions within a defined authority. Agents are organized in three roles: Executive, Supervisor, and Specialist.

**Authority Pack**: A YAML file that defines what an agent may decide and execute. It specifies the agent's role, scope, governed actions, rules, control gates, escalation path, and evidence requirements.

**Constellation**: A governed cluster of agents organized in an Executive → Supervisor → Specialist hierarchy. Each constellation is a complete governance system for a domain (e.g., vault maintenance, incident response).

**Compiled Governance Artifact**: A JSON file produced by the compiler that contains the fully resolved and flattened authority pack, ready for runtime enforcement. It resolves inheritance chains, merges rules, binds escalation paths, and adds host metadata.

**Executive Agent**: The top-level agent in a constellation that sets policy, makes strategic decisions, and escalates unresolvable issues to human operators.

**Supervisor Agent**: The middle-level agent that coordinates specialist tasks, aggregates their results, applies non-destructive fixes, and escalates decisions outside its authority to the Executive.

**Specialist Agent**: The bottom-level agent that executes focused, well-defined tasks (auditing, validation, detection) and reports results to the Supervisor.

**Escalation**: The act of passing a decision up the hierarchy when an agent lacks authority to resolve it. Escalation is mandatory in Agent Maestro and creates a feedback loop that ensures no decision is made outside its proper scope.

**Model Workspace Protocol**: A communication protocol that allows agents to collaborate within shared workspaces, sharing audit reports, fix logs, and escalation requests.

**Knowledge Graph Layer**: The semantic layer of the Agent Maestro system that tracks entities, relationships, and metadata across the vault. Specialists enrich this graph as they audit.
