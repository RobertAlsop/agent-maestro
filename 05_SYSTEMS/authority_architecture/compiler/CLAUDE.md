# 05_SYSTEMS/authority_architecture/compiler

## Purpose

The Authority Pack Compiler is the system that transforms human-written authority packs into executable compiled governance artifacts. The compiler takes authority pack definitions (from the packs/ directory), validates them against schemas, resolves inheritance chains, applies overrides, performs policy resolution, and generates machine-readable compiled artifacts that can be bound to specific agent hosts.

The compiler is the critical bridge between Authority Architecture design (in KNOWLEDGE) and executable agent constraints (in the runtime).

## Compiler Pipeline

The compiler executes a deterministic pipeline:

1. **Input Validation**: Verify input packs conform to Authority Pack Grammar and required schemas
2. **Inheritance Resolution**: Resolve pack inheritance chains, verify no circular dependencies
3. **Override Application**: Apply child pack overrides to parent pack rules
4. **Policy Resolution**: Resolve policy conflicts, check for contradictions
5. **Completeness Validation**: Ensure all 14 sections are populated, no gaps in permission matrix
6. **Artifact Generation**: Generate compiled governance artifact for each pack
7. **Host Binding**: Bind compiled artifacts to specific host/agent combinations
8. **Output Registration**: Register generated artifacts in compiler_artifacts_registry.csv

Output artifacts are placed in `artifacts/` subdirectory and registered in the registry.

## Structure

- **prototype/**: Reference compiler implementation in Python
- **compiler.py**: Main compiler script with full pipeline implementation
- **artifacts/**: Output directory for compiled governance artifacts
- **Authority Pack Compiler.md**: Overview and architecture documentation
- **Compiler Pipeline.md**: Detailed description of each pipeline stage
- **Compiler Inputs.md**: Input specification and validation rules
- **Compiler Outputs.md**: Output artifact schemas and formats
- **Compiled Governance Artifacts.md**: Reference for compiled artifact structure
- **Compile Failure Semantics.md**: Error conditions and failure handling
- **Host Bindings.md**: How compiled artifacts are bound to host systems
- **Integration Manifest.md**: Integration points with agent runtime
- **compiler_artifacts_registry.csv**: Registry of all compiled artifacts with versions

All files located in `05_SYSTEMS/authority_architecture/compiler/`

## Compiler Inputs

The compiler accepts:

- **Authority packs** (from packs/ directory): Each pack follows the 14-section grammar
- **Pack version specifications**: Which pack versions to compile
- **Host specifications**: Target hosts and agent roles for binding
- **Policy constraints** (from KNOWLEDGE/governance/): Policy precedence rules
- **Inheritance maps** (from authority_architecture/maps/): Pack dependency information

Inputs are validated against schemas in Compiler Inputs.md.

## Compiler Outputs

The compiler generates:

- **Compiled Governance Artifacts** (CSVs and JSON): Machine-readable specifications of agent permissions
- **Host Bindings**: Mappings of artifacts to specific hosts/agents
- **Compilation Report**: Summary of compilation results, warnings, and errors
- **Artifact Registry**: compiler_artifacts_registry.csv with all generated artifacts and versions

Artifacts are stored in `artifacts/` subdirectory with clear version numbering.

## Agent Rules

**Agents MAY**:
- Read compiler documentation to understand the compilation process
- Run the compiler on new/modified authority packs (with escalation approval)
- Review compilation reports and artifacts
- Query the compiler_artifacts_registry.csv to find compiled artifacts

**Agents MUST NOT**:
- Modify the compiler source code without escalation
- Bypass compiler validation or skip pipeline stages
- Directly edit compiled artifacts (regenerate via compiler instead)
- Delete compilation outputs without escalation
- Manually edit the compiler_artifacts_registry.csv

**Escalation Required**:
- Modifications to compiler.py or pipeline logic
- Decisions to skip compiler stages or validation
- Changes to artifact output format or schemas
- Requests to regenerate all artifacts (full recompilation)

## Compilation Workflow

To compile an updated authority pack:

1. **Prepare Pack**: Ensure the modified pack is in packs/ directory with new version number
2. **Run Compiler**: Execute `python compiler.py --pack <pack_name> --version <new_version>`
3. **Review Output**: Check compilation report for errors or warnings
4. **Validate Artifacts**: Verify generated artifacts match pack specifications
5. **Update Registry**: Compiler automatically updates compiler_artifacts_registry.csv
6. **Bind to Hosts**: Use host binding specification to bind artifacts to agents
7. **Communicate**: Notify affected agents of the new compiled artifact versions

## Key Documents

- **Authority Pack Compiler.md**: Overview of compiler architecture and principles
- **Compiler Pipeline.md**: Detailed pipeline stages and validation rules
- **Compiler Inputs.md**: Input schema and validation specifications
- **Compiler Outputs.md**: Output artifact formats and specifications
- **Compiled Governance Artifacts.md**: Structure of compiled artifacts
- **Compile Failure Semantics.md**: Failure conditions and error handling
- **Host Bindings.md**: Host binding specification and mapping
- **Integration Manifest.md**: Integration with agent runtime

## Artifact Registry

The file `compiler_artifacts_registry.csv` contains:
- Artifact name
- Source pack name
- Source pack version
- Artifact version
- Compilation date
- Target host/agent role
- Status (active | deprecated | experimental)
- Artifact file path

This registry is the single source of truth for which compiled artifacts are active in the system.

## Error Handling

Compilation failures are classified by severity:

- **Fatal**: Validation failed, no artifact generated (e.g., invalid pack structure, circular inheritance)
- **Major**: Artifact generated but with warnings (e.g., policy conflicts, missing optional sections)
- **Minor**: Artifact generated with informational notes (e.g., deprecated pack dependency, unused sections)

See Compile Failure Semantics.md for detailed error classifications and recovery procedures.

## Performance Notes

- The compiler is deterministic: same inputs always produce identical outputs
- Compilation is idempotent: compiling the same pack twice produces the same artifacts
- Compiler execution is reasonably fast (typical compilation < 1 second)
- All compilation results are logged for auditability

## Relationship to Authority Architecture

The compiler executes the Authority Pack Grammar. Each authority pack's 14 sections are validated, inherited, overridden, and resolved by the compiler. The compiler is the enforcement mechanism for the Authority Inheritance Pattern and the Pack Override Rules.

See the authority_architecture CLAUDE.md for details on pack structure and versioning.

## Relationship to Agent Runtime

Compiled artifacts are bound to specific agent hosts via host bindings. At runtime, agents execute according to the permissions and constraints specified in their bound compiled artifacts. Changes to compiled artifacts require rebinding agents to new artifact versions.

See Host Bindings.md for details on how artifacts are bound to agent hosts.
