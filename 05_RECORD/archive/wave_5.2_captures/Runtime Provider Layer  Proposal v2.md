# Runtime Provider Layer (RPL)

## Controlled Revision Proposal v2

Note: RPL v1 is already built.

---

# 1. System Role

The **Runtime Provider Layer (RPL)** is a **substrate service** that provides governed access to language model inference for runtime systems.

It allows runtime engines to request model inference **without binding to a specific provider**.

The RPL enables:

- local inference providers
    
- cloud inference providers
    
- provider routing
    
- deterministic request logging
    
- controlled inference execution
    

The RPL **does not implement runtime logic** and **does not implement application behavior**.

It provides **inference capability only**.

---

# 2. Architectural Layer Placement

The Runtime Provider Layer belongs to the **System Services layer of the AI-OS ecosystem**.

It sits **below runtime engines** and **above model providers**.

AI-OS Ecosystem  
  
Applications  
    Agent Maestro Runtime  
    Trust Birth Pools Runtime  
  
System Services  
    Runtime Provider Layer (RPL)  
  
Provider Drivers  
    Local Model Providers  
    Cloud Model Providers  
  
External Providers  
    Ollama  
    OpenAI  
    Anthropic  
    Future providers

Responsibilities are strictly separated.

**Applications must never interact directly with model providers.**

All inference must pass through the RPL.

---

# 3. Scope Boundaries

The Runtime Provider Layer **only performs inference operations**.

It does **not**:

- edit files
    
- execute commands
    
- mutate runtime state
    
- manage scheduling
    
- interpret business logic
    
- execute constellations
    
- authorize system mutations
    

All side effects remain the responsibility of **runtime engines**.

---

# 4. Provider Abstraction Contract

All model providers must implement the **RPL Provider Contract**.

This ensures swappable providers.

## Provider Interface

Example Python contract:

class Provider:  
    def generate(request: GenerationRequest) -> GenerationResponse  
    def classify(request: ClassificationRequest) -> ClassificationResponse  
    def summarize(request: SummaryRequest) -> SummaryResponse  
    def propose_patch(request: PatchRequest) -> PatchResponse

Providers may support only a subset of capabilities.

Capabilities must be declared in provider metadata.

---

# 5. Request Contract

Every inference request must include a complete structured request object.

GenerationRequest  
{  
  request_id  
  provider_id  
  model_id  
  task_type  
  input_context  
  system_prompt  
  parameters  
  context_hash  
  prompt_template_version  
}

Required parameters:

temperature  
max_tokens  
top_p  
stop_sequences  
seed

This ensures deterministic configuration.

---

# 6. Response Contract

Every provider response must return a structured response object.

GenerationResponse  
{  
  request_id  
  provider_id  
  model_id  
  model_version  
  output  
  token_usage  
  latency_ms  
  seed  
  response_hash  
}

All responses must be serializable.

Free-form text without structure is prohibited.

---

# 7. Determinism Contract

Each inference call must record deterministic inputs.

Captured data must include:

- model identifier
    
- model version
    
- provider identifier
    
- temperature
    
- seed
    
- prompt template version
    
- context hash
    
- request parameters
    

These values become part of the **run artifact record**.

Exact replay may not be guaranteed for all providers, but replay inputs must always be captured.

---

# 8. Mutation Pathway Rules

The RPL is **never permitted to mutate system state**.

Mutation must follow the runtime governance pipeline.

Required pathway:

Model inference  
        ↓  
Proposal artifact generated  
        ↓  
Validation stage  
        ↓  
Authorization stage  
        ↓  
Mutation execution  
        ↓  
Event emission

The RPL participates **only in the inference stage**.

---

# 9. Scheduling Separation

Scheduling is not part of the Runtime Provider Layer.

Scheduling occurs at the runtime level.

Example:

launchd  
    ↓  
runtime orchestrator  
    ↓  
constellation execution  
    ↓  
RPL inference call

Scheduled execution must default to **dry-run mode**.

Apply-mode requires explicit runtime authorization.

---

# 10. Run Artifact Requirements

Each runtime execution cycle must create a run directory.

runs/<run_id>/

Required artifacts:

context.json  
events.jsonl  
outcomes.json  
requests/  
responses/  
proposals/  
summary.md

Inference calls must produce request and response artifacts.

requests/<request_id>.json  
responses/<request_id>.json

This ensures full inference traceability.

---

# 11. Provider Drivers

The RPL supports multiple provider drivers.

### Local Provider Driver

Example:

OllamaProvider

Responsibilities:

- local model inference
    
- model selection
    
- request forwarding
    
- response formatting
    

Local providers must default to **network-disabled mode**.

---

### Cloud Provider Drivers

Example:

OpenAIProvider  
AnthropicProvider

Responsibilities:

- API request execution
    
- response normalization
    
- cost tracking
    

---

# 12. Provider Selection

Provider routing must occur explicitly.

Routing strategies may include:

explicit provider selection  
capability matching  
fallback routing

Example routing rules:

maintenance tasks → local provider  
complex reasoning → cloud provider  
fallback on failure → secondary provider

Routing decisions must be logged.

---

# 13. Failure Handling

Provider failures must produce structured errors.

Error contract:

ProviderError  
{  
  request_id  
  provider_id  
  error_type  
  error_message  
  retryable  
}

Runtime engines decide retry behavior.

The RPL does not retry automatically.

---

# 14. Security Rules

The Runtime Provider Layer must enforce strict security constraints.

### File Access

The RPL must have **no filesystem write permissions**.

### Network Access

Local providers default to **network disabled**.

### Secret Handling

Cloud provider API keys must be stored outside runtime artifacts.

---

# 15. Constellation Compatibility

Runtime engines may use the RPL during constellation execution.

Example constellation flow:

Constellation cycle  
      ↓  
analysis stage  
      ↓  
RPL inference  
      ↓  
proposal generation  
      ↓  
validation  
      ↓  
optional mutation

The RPL does not know about constellations.

---

# 16. Supported Use Cases

Examples:

### Vault Maintenance

- schema validation suggestions
    
- front matter normalization proposals
    
- broken link detection suggestions
    

### Knowledge Curation

- summarization
    
- classification
    
- deduplication suggestions
    

### Business Runtime Tasks

- draft generation
    
- classification
    
- analysis
    

All outputs must remain **proposals** until validated.

---

# 17. Initial Provider Implementation

The first provider driver will be:

OllamaProvider

Responsibilities:

- run local coding models
    
- perform offline inference
    
- support scheduled runtime cycles
    

---

# 18. Implementation Phases

### Phase 1 — Provider Interface

Create canonical provider interface.

rpl/provider_interface.py

---

### Phase 2 — Ollama Driver

Implement local provider driver.

rpl/providers/ollama_provider.py

---

### Phase 3 — Runtime Integration

Modify runtime engines to call RPL instead of direct providers.

---

### Phase 4 — Artifact Logging

Implement request/response artifact generation.

---

### Phase 5 — Provider Routing

Add provider selection rules.

---

# 19. Expected Outcomes

Once implemented, the Runtime Provider Layer will allow:

- runtime systems to run constellations using local models
    
- provider-agnostic inference
    
- deterministic inference logging
    
- safe integration with runtime governance
    
- reduced reliance on rate-limited cloud models
    

---

# 20. Long-Term Role

The Runtime Provider Layer becomes a **core system service** supporting all AI-OS runtimes.

It will enable:

- hybrid inference architectures
    
- local-first runtime execution
    
- cloud augmentation when required
    
- long-term provider independence
    

---

# Audit Compliance Result

This revision resolves the failures identified in the adversarial audit:

|Audit Issue|Status|
|---|---|
|Layer ambiguity|Resolved|
|Provider abstraction|Resolved|
|Determinism gap|Resolved|
|Mutation pathway|Resolved|
|Scheduling separation|Resolved|
|Scope creep|Resolved|