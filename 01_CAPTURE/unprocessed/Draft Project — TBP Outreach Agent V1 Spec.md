# TBP Outreach Agent V1 — Canonical One-Page Architecture Spec

## 1. Purpose

Process a referral/outreach contact, generate the correct outreach email, validate it, present it for approval, then update system state and log the outcome.

## 2. Scope

V1 handles:

- one outreach workflow
    
- one contact at a time
    
- first outreach email only
    
- human approval before send
    
- state update after send
    
- event logging for every step
    

V1 does **not** include:

- autonomous sending
    
- reply handling
    
- multi-agent handoffs
    
- self-improving prompts
    
- complex vector retrieval
    

## 3. Core Flow

Trigger  
→ Load contact/state  
→ Build context pack  
→ Generate decision + draft  
→ Validate  
→ Human approve / reject  
→ Send email  
→ Update state  
→ Log outcome

## 4. System Components

### A. Input Gateway

Receives the task.

Examples:

- manual trigger from outreach table
    
- “ready_to_process” row in database
    

Output artifact:

- `task_packet`
    

### B. State Store

Authoritative live truth.

Stores:

- contacts
    
- organizations
    
- outreach status
    
- sent dates
    
- next action date
    
- assigned language
    
- notes
    

### C. Context Builder

Builds the exact context for the model.

Inputs:

- contact row
    
- organization row
    
- prior outreach status
    
- approved email template/components
    
- tone/policy instructions
    

Output artifact:

- `context_pack`
    

### D. Decision + Draft Engine

LLM produces:

- outreach classification
    
- language choice
    
- draft subject
    
- draft body
    
- recommended next action
    
- confidence / review flag
    

Output artifact:

- `draft_proposal`
    

### E. Validation Layer

Checks:

- required fields present
    
- no duplicate send
    
- valid contact status
    
- approved template family
    
- language present
    
- placeholders resolved
    
- email safe to review
    

Output artifact:

- `validation_report`
    

### F. Human Control Point

Operator chooses:

- approve
    
- reject
    
- edit externally and re-run
    
- defer
    

Output artifact:

- `approval_decision`
    

### G. Tool Executor

If approved:

- send email
    
- update outreach status
    
- create follow-up date/task
    
- store sent timestamp
    

Output artifact:

- `execution_result`
    

### H. Event Log

Append-only record of:

- task created
    
- context built
    
- draft generated
    
- validation passed/failed
    
- approved/rejected
    
- sent/not sent
    
- state updated
    

Output artifact:

- `event_record`
    

## 5. Canonical Artifacts

### Declarative artifacts

Best in markdown / JSON:

- `outreach_policy.md`
    
- `email_template_spec.md`
    
- `draft_rules.json`
    
- `status_transition_rules.json`
    

### Executable artifacts

Best in Python:

- `build_context_pack.py`
    
- `generate_outreach_draft.py`
    
- `validate_outreach_draft.py`
    
- `send_outreach_email.py`
    
- `log_outreach_event.py`
    

### Runtime artifacts

Produced per run:

- `task_packet.json`
    
- `context_pack.json`
    
- `draft_proposal.json`
    
- `validation_report.json`
    
- `approval_decision.json`
    
- `execution_result.json`
    
- `event_log.jsonl`
    

## 6. Data Stores

### Operational truth store

Airtable or Postgres.

Minimum tables:

- `contacts`
    
- `organizations`
    
- `outreach_tasks`
    
- `outreach_events`
    
- `sent_emails`
    

### Document/design store

Obsidian or repo docs.

Stores:

- outreach doctrine
    
- tone rules
    
- contact category definitions
    
- approved template structures
    

### Optional memory store later

Vector layer for:

- similar successful outreach examples
    
- past message patterns
    
- categorized reply outcomes
    

Not required for V1.

## 7. Control Points

### Control Point 1 — Trigger eligibility

Only process contacts where:

- contact exists
    
- email exists
    
- status = ready
    
- not already sent first outreach
    

### Control Point 2 — Validation gate

No approval step unless validation passes.

### Control Point 3 — Human approval

No send without explicit approval.

### Control Point 4 — Post-send state update

After successful send:

- mark first outreach sent
    
- save sent date
    
- assign follow-up date
    
- log event
    

### Control Point 5 — Failure halt

If send fails:

- do not advance status
    
- log failure
    
- flag for manual review
    

## 8. Authority Model

### Conceptual authority

Obsidian / design docs  
Defines outreach logic, tone, categories.

### Operational authority

Database  
Defines what is true now.

### Decision authority

LLM  
Proposes classification and draft.

### Execution authority

Python tools / API layer  
Actually sends and updates.

### Governance authority

Validation rules + approval gate + event logging  
Determines what is allowed.

## 9. V1 Success Criteria

V1 is successful when it can reliably:

- process a valid contact
    
- generate a usable outreach draft
    
- block invalid drafts
    
- require approval before send
    
- send successfully after approval
    
- update status correctly
    
- produce a complete event trail
    

## 10. One-Sentence Definition

**TBP Outreach Agent V1 is a human-approved outreach workflow that turns a valid contact record into a validated sent email plus a fully logged state transition.**