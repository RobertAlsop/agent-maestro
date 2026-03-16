# Canonical Artifact Taxonomy for AI-Native Systems

We’ll map artifacts across six storage domains:

1. **Concept Layer (Obsidian / knowledge system)**
    
2. **Design Layer (repo markdown)**
    
3. **Executable Layer (Python / code)**
    
4. **State Layer (database)**
    
5. **Memory Layer (vector + documents)**
    
6. **Governance Layer (AIOS substrate)**
    

These layers correspond closely to the authority model we discussed.

---

# 1. Concept Layer — System Knowledge

**Best home:** Obsidian vault

This layer defines **meaning and understanding**.

Artifacts here change slowly and guide system design.

### Artifact types

- domain ontology
    
- concept definitions
    
- system maps
    
- maps of content
    
- architecture narratives
    
- design doctrine
    
- heuristics
    
- operational philosophy
    
- decision frameworks
    
- role definitions
    
- agent archetypes
    
- workflow explanations
    

### Example artifacts

agent-orchestration-principles.md  
customer-lifecycle-map.md  
ai-governance-philosophy.md  
birthpool-referral-ecosystem.md

### Key properties

- human-readable
    
- linkable knowledge graph
    
- conceptual authority
    
- rarely machine-executed directly
    

This is **knowledge**, not state.

---

# 2. Design Layer — Declarative System Artifacts

**Best home:** repository markdown / JSON / YAML

This layer defines **machine-operable declarations**.

These artifacts are often read by programs.

### Artifact types

- contracts
    
- specifications
    
- manifests
    
- schemas
    
- run definitions
    
- policy profiles
    
- agent role definitions
    
- workflow specifications
    
- interface definitions
    
- config declarations
    

### Example artifacts

contracts/by_id/send_email.contract.md  
policy_profiles/default_policy.yaml  
workflow_specs/outreach_pipeline.md  
release_manifest.json

### Key properties

- declarative
    
- version controlled
    
- inspectable
    
- diffable
    
- deterministic inputs for code
    

This layer answers:

> What should exist and how should it behave?

---

# 3. Executable Layer — Operational Machinery

**Best home:** Python or other code

This layer **implements the system mechanics**.

### Artifact types

- operators
    
- compilers
    
- validators
    
- planners
    
- orchestrators
    
- context builders
    
- tool adapters
    
- event processors
    
- queue workers
    
- API integrations
    

### Example artifacts

build_contract_compiler.py  
context_capture.py  
bundle_context_generator.py  
email_send_tool.py  
workflow_orchestrator.py

### Key properties

- deterministic execution
    
- side effects allowed
    
- integrates tools
    
- interprets declarative artifacts
    

This layer answers:

> How does the system actually run?

---

# 4. State Layer — Operational Truth

**Best home:** SQL database

This layer stores **authoritative current state**.

### Artifact types

- entities
    
- records
    
- statuses
    
- queues
    
- workflow states
    
- ownership data
    
- timestamps
    
- task lists
    
- transactional logs
    

### Example tables

customers  
orders  
tasks  
workflow_runs  
email_outreach  
agent_jobs

### Key properties

- authoritative truth
    
- structured schema
    
- transactional
    
- frequently updated
    

This layer answers:

> What is true right now?

---

# 5. Memory Layer — Retrievable Past Experience

**Best home:** vector database + document store

This layer stores **past information useful for reasoning**.

### Artifact types

- conversations
    
- historical cases
    
- summaries
    
- research notes
    
- past workflows
    
- incident reports
    
- decision explanations
    
- knowledge fragments
    

### Example memory objects

memory_objects/  
  outreach_success_patterns.md  
  customer_support_resolution_patterns.md

### Key properties

- approximate retrieval
    
- similarity search
    
- non-authoritative
    
- augment reasoning
    

This layer answers:

> What from the past might be relevant?

---

# 6. Governance Layer — System Integrity

**Best home:** AIOS substrate

This layer enforces **system safety and discipline**.

### Artifact types

- invariants
    
- validators
    
- contract enforcement
    
- evidence logs
    
- event ledger
    
- run identity
    
- audit records
    
- halt conditions
    
- provenance records
    

### Example artifacts

event_ledger.json  
snapshot_records.json  
release_manifest.json  
run_identity.json

### Key properties

- append-only evidence
    
- deterministic validation
    
- system oversight
    
- replayable execution
    

This layer answers:

> Was this action valid?

---

# Visual Map of the Artifact Taxonomy

Concept Layer  
(Obsidian)  
    ↓ defines meaning  
  
Design Layer  
(Repo markdown / JSON)  
    ↓ declares system structure  
  
Executable Layer  
(Python code)  
    ↓ runs workflows  
  
State Layer  
(SQL database)  
    ↓ stores operational truth  
  
Memory Layer  
(Vector + documents)  
    ↓ stores retrievable experience  
  
Governance Layer  
(AIOS substrate)  
    ↓ enforces system integrity

---

# Example Flow Through the Layers

Let's take a simple example: **sending a referral outreach email**.

### Concept layer

midwife-referral-relationship.md

Defines the conceptual model of the referral network.

---

### Design layer

contracts/send_referral_email.contract.md

Defines allowed behavior.

---

### Executable layer

send_referral_email_operator.py

Implements the operation.

---

### State layer

contacts table  
outreach_status table

Tracks which contacts have been emailed.

---

### Memory layer

past outreach emails  
successful message patterns

Provides context to the drafting agent.

---

### Governance layer

run ledger  
contract validation  
event log

Records and verifies the execution.

---

# The Golden Rule of AI System Architecture

Each artifact must answer **one question**:

|Question|Layer|
|---|---|
|What does this concept mean?|Concept|
|What should exist or be allowed?|Design|
|How does the system execute it?|Execution|
|What is true right now?|State|
|What past information is relevant?|Memory|
|Was the system allowed to do this?|Governance|

When artifacts mix these roles, systems become chaotic.

---

# The Architectural Insight That Matters

Once this taxonomy exists, **AI systems stop being mysterious**.

They become a structured stack of artifact types.

Which means an **AI Systems Architect** is really someone who:

- designs artifact boundaries
    
- defines authority layers
    
- orchestrates interactions between them
    

This is exactly why the role you described — **Agent Maestro / AI Systems Architect** — is emerging.