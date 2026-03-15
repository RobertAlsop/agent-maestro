---
id: EXE.prompt.vault_build
type: pipeline
layer: execution
domain: execution
status: active
version: 1
created: 2026-03-10
owner: AgentMaestro
maps: "[[Agent Maestro — Domain Map]]"
hash: TBD
---

# Claude Vault Build Prompt

## Purpose

The prompt template used to instruct Claude to build or extend the Agent Maestro vault.

## When It Is Used

Whenever the vault requires structural additions, bulk note creation, or build phases.

## Prompt Template

```
You are building the Agent Maestro Obsidian vault at /Users/robertalsop/obsidian/Agent-Maestro/

Vault rules: [[Agent Maestro — Vault Rules]]
Templates: Use only the approved master templates.
Build plan: Follow the approved plan exactly. No structural changes during build.
Priority: Internal linking quality over writing length. Short, well-linked notes.

Task: [DESCRIBE TASK HERE]
```

## Related

- [[Agent Maestro — Vault Rules]]
- [[Claude Note Quality Rules]]
