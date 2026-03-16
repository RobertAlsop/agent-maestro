"""
Tool Interface — Approved tool set for governed agent operations.

Part of Agent Maestro v0.3 Runtime Engine (Phase B — C1).

Agents interact with the vault exclusively through this tool interface.
Every tool call is mediated by the governance layer via attempt_action().
Tools have defined input/output contracts and required permissions.

Available tools:
    - read_note: Read a vault note's content and frontmatter
    - write_note: Write or update a vault note
    - scan_directory: List notes in a vault directory with metadata
    - validate_frontmatter: Check a note's frontmatter against schema
    - scan_links: Audit wiki-links in a note or directory
    - generate_report: Write a CSV or JSON report to 06_EXECUTION
    - move_note: Move a note between vault locations
    - read_registry: Read a CSV registry file
    - append_registry: Append a row to a CSV registry
"""

import csv
import json
import os
import re
import sys
import yaml
from datetime import datetime, timezone
from typing import Any, Optional

# Allow importing sibling modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from state_change_logger import StateChangeLogger, ChangeType
    HAS_STATE_LOGGER = True
except ImportError:
    HAS_STATE_LOGGER = False

# Module-level state change logger (initialized on first use)
_state_logger: Optional["StateChangeLogger"] = None


def _get_state_logger(vault_path: str):
    """Get or create the module-level state change logger."""
    global _state_logger
    if _state_logger is None and HAS_STATE_LOGGER:
        _state_logger = StateChangeLogger(vault_path)
    return _state_logger


def _log_state_change(vault_path: str, change_type: str, artifact_path: str,
                      agent_id: str = "tool_interface", agent_role: str = "tool",
                      constellation: str = "runtime", field_changed: str = "",
                      before_state: str = "", after_state: str = "",
                      justification: str = "", artifact_type: str = "note"):
    """Log a state change from a tool operation."""
    logger = _get_state_logger(vault_path)
    if logger:
        try:
            ct = ChangeType(change_type)
            logger.log_change(
                change_type=ct,
                agent_id=agent_id,
                agent_role=agent_role,
                constellation=constellation,
                artifact_path=artifact_path,
                artifact_type=artifact_type,
                field_changed=field_changed,
                before_state=before_state,
                after_state=after_state,
                justification=justification,
            )
        except Exception:
            pass  # State logging should never block tool execution


class ToolResult:
    """Result of a tool execution."""

    def __init__(self, tool_name: str, success: bool, data: Any = None,
                 error: str = None, artifacts: list = None):
        self.tool_name = tool_name
        self.success = success
        self.data = data
        self.error = error
        self.artifacts = artifacts or []
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "tool_name": self.tool_name,
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "artifacts": self.artifacts,
            "timestamp": self.timestamp,
        }


# ── Tool Registry ──────────────────────────────────────────────


TOOL_REGISTRY = {}


def register_tool(name: str, required_permission: str, description: str):
    """Decorator to register a tool function in the tool registry."""
    def decorator(fn):
        TOOL_REGISTRY[name] = {
            "function": fn,
            "required_permission": required_permission,
            "description": description,
            "name": name,
        }
        fn.tool_name = name
        fn.required_permission = required_permission
        return fn
    return decorator


def get_tool(name: str) -> dict:
    """Look up a registered tool by name."""
    if name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {name}. Available: {list(TOOL_REGISTRY.keys())}")
    return TOOL_REGISTRY[name]


def list_tools() -> list[dict]:
    """List all registered tools with their metadata."""
    return [
        {"name": t["name"], "permission": t["required_permission"], "description": t["description"]}
        for t in TOOL_REGISTRY.values()
    ]


# ── Tool Implementations ──────────────────────────────────────


@register_tool("read_note", "read note", "Read a vault note's content and parse its YAML frontmatter")
def tool_read_note(vault_path: str, note_path: str, **kwargs) -> ToolResult:
    """
    Read a vault note and return its content and parsed frontmatter.

    Args:
        vault_path: Root path of the vault
        note_path: Vault-relative path to the note

    Returns:
        ToolResult with data = {"content": str, "frontmatter": dict, "body": str}
    """
    full_path = os.path.join(vault_path, note_path)

    if not os.path.exists(full_path):
        return ToolResult("read_note", False, error=f"Note not found: {note_path}")

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = {}
        body = content

        # Parse YAML frontmatter (between --- delimiters)
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                except yaml.YAMLError:
                    frontmatter = {"_parse_error": "Invalid YAML frontmatter"}
                body = parts[2].strip()

        return ToolResult("read_note", True, data={
            "path": note_path,
            "content": content,
            "frontmatter": frontmatter,
            "body": body,
            "size_bytes": len(content.encode('utf-8')),
        })

    except Exception as e:
        return ToolResult("read_note", False, error=str(e))


@register_tool("write_note", "write note", "Write or update a vault note with content and frontmatter")
def tool_write_note(vault_path: str, note_path: str, content: str = None,
                    frontmatter: dict = None, body: str = None, **kwargs) -> ToolResult:
    """
    Write a vault note. Can provide full content, or frontmatter + body separately.

    Args:
        vault_path: Root path of the vault
        note_path: Vault-relative path to the note
        content: Full note content (takes precedence over frontmatter+body)
        frontmatter: YAML frontmatter dict (combined with body if content not provided)
        body: Note body text (combined with frontmatter if content not provided)

    Returns:
        ToolResult with data = {"path": str, "size_bytes": int}
    """
    full_path = os.path.join(vault_path, note_path)

    try:
        if content is None and frontmatter is not None:
            # Build content from frontmatter + body
            fm_str = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
            content = f"---\n{fm_str}---\n\n{body or ''}"
        elif content is None:
            return ToolResult("write_note", False, error="Must provide content or frontmatter")

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # Detect create vs modify
        is_new = not os.path.exists(full_path)
        change_type = "create" if is_new else "modify"

        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Log state change
        _log_state_change(
            vault_path, change_type, note_path,
            justification=f"{'Created' if is_new else 'Updated'} via write_note tool",
            artifact_type="note",
        )

        return ToolResult("write_note", True, data={
            "path": note_path,
            "size_bytes": len(content.encode('utf-8')),
        }, artifacts=[note_path])

    except Exception as e:
        return ToolResult("write_note", False, error=str(e))


@register_tool("scan_directory", "scan directory", "List notes in a vault directory with basic metadata")
def tool_scan_directory(vault_path: str, dir_path: str, pattern: str = "*.md",
                        recursive: bool = False, **kwargs) -> ToolResult:
    """
    Scan a vault directory and return file listing with basic metadata.

    Args:
        vault_path: Root path of the vault
        dir_path: Vault-relative directory path
        pattern: Glob pattern to match (default: *.md)
        recursive: Whether to scan subdirectories

    Returns:
        ToolResult with data = {"files": [{"path": str, "size": int, "modified": str}], "count": int}
    """
    full_dir = os.path.join(vault_path, dir_path)

    if not os.path.isdir(full_dir):
        return ToolResult("scan_directory", False, error=f"Directory not found: {dir_path}")

    try:
        import fnmatch
        files = []

        if recursive:
            for root, dirs, filenames in os.walk(full_dir):
                for fn in filenames:
                    if fnmatch.fnmatch(fn, pattern):
                        full = os.path.join(root, fn)
                        rel = os.path.relpath(full, vault_path)
                        stat = os.stat(full)
                        files.append({
                            "path": rel,
                            "name": fn,
                            "size_bytes": stat.st_size,
                            "modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                        })
        else:
            for fn in sorted(os.listdir(full_dir)):
                if fnmatch.fnmatch(fn, pattern):
                    full = os.path.join(full_dir, fn)
                    if os.path.isfile(full):
                        stat = os.stat(full)
                        rel = os.path.relpath(full, vault_path)
                        files.append({
                            "path": rel,
                            "name": fn,
                            "size_bytes": stat.st_size,
                            "modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                        })

        return ToolResult("scan_directory", True, data={
            "directory": dir_path,
            "pattern": pattern,
            "files": files,
            "count": len(files),
        })

    except Exception as e:
        return ToolResult("scan_directory", False, error=str(e))


@register_tool("validate_frontmatter", "validate frontmatter", "Check a note's frontmatter against schema_version 2 requirements")
def tool_validate_frontmatter(vault_path: str, note_path: str, **kwargs) -> ToolResult:
    """
    Validate a note's YAML frontmatter against schema_version 2 requirements.

    Returns:
        ToolResult with data = {"valid": bool, "errors": list, "warnings": list}
    """
    # First read the note
    read_result = tool_read_note(vault_path, note_path)
    if not read_result.success:
        return ToolResult("validate_frontmatter", False, error=read_result.error)

    fm = read_result.data["frontmatter"]
    errors = []
    warnings = []

    # Required fields for schema_version 2
    if not fm:
        errors.append("No frontmatter found")
        return ToolResult("validate_frontmatter", True, data={
            "path": note_path, "valid": False, "errors": errors, "warnings": warnings
        })

    # Check schema_version
    sv = fm.get("schema_version")
    if sv is None:
        errors.append("Missing schema_version")
    elif sv != 2:
        warnings.append(f"schema_version is {sv}, expected 2")

    # Check common required fields
    for field in ["status", "created_date", "last_modified"]:
        alt_field = field.replace("_date", "").replace("last_", "")
        if field not in fm and alt_field not in fm and f"{field}d" not in fm:
            # Be flexible about field naming (created vs created_date vs created)
            if field == "created_date" and "created" not in fm:
                warnings.append(f"Missing {field} (or 'created')")
            elif field == "last_modified" and "updated" not in fm:
                warnings.append(f"Missing {field} (or 'updated')")
            elif field == "status":
                warnings.append(f"Missing {field}")

    # Check relationships structure
    rels = fm.get("relationships", fm)
    rel_types = ["defines", "part_of", "implements", "governs", "inherits_from",
                 "applies_to", "uses", "produces"]
    has_any_rel = False
    for rt in rel_types:
        if rt in rels or rt in fm:
            has_any_rel = True
            break
    if not has_any_rel:
        warnings.append("No relationship fields found in frontmatter")

    # Check tags
    if "tags" not in fm:
        warnings.append("Missing tags field")
    elif not isinstance(fm.get("tags"), list):
        warnings.append("tags should be a list")

    valid = len(errors) == 0

    return ToolResult("validate_frontmatter", True, data={
        "path": note_path,
        "valid": valid,
        "errors": errors,
        "warnings": warnings,
        "frontmatter_keys": list(fm.keys()) if fm else [],
    })


@register_tool("scan_links", "scan links", "Audit wiki-links in a note or set of notes")
def tool_scan_links(vault_path: str, note_path: str = None, dir_path: str = None,
                    **kwargs) -> ToolResult:
    """
    Scan for wiki-links ([[...]] format) and check if targets exist.

    Args:
        vault_path: Root path of the vault
        note_path: Vault-relative path to a single note (or)
        dir_path: Vault-relative path to scan a directory

    Returns:
        ToolResult with data = {"links": [...], "broken": [...], "total": int, "broken_count": int}
    """
    try:
        notes_to_scan = []
        if note_path:
            notes_to_scan.append(os.path.join(vault_path, note_path))
        elif dir_path:
            full_dir = os.path.join(vault_path, dir_path)
            for root, _, files in os.walk(full_dir):
                for fn in files:
                    if fn.endswith('.md'):
                        notes_to_scan.append(os.path.join(root, fn))
        else:
            return ToolResult("scan_links", False, error="Must provide note_path or dir_path")

        # Build index of existing note names
        all_notes = set()
        for root, _, files in os.walk(vault_path):
            for fn in files:
                if fn.endswith('.md'):
                    name_no_ext = fn[:-3]
                    all_notes.add(name_no_ext.lower())

        link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
        all_links = []
        broken_links = []

        for note_file in notes_to_scan:
            try:
                with open(note_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue

            rel_path = os.path.relpath(note_file, vault_path)
            matches = link_pattern.findall(content)
            for target in matches:
                target_clean = target.strip()
                # Extract just the note name (strip path prefixes)
                target_name = target_clean.split('/')[-1].lower()
                exists = target_name in all_notes
                link_info = {
                    "source": rel_path,
                    "target": target_clean,
                    "exists": exists,
                }
                all_links.append(link_info)
                if not exists:
                    broken_links.append(link_info)

        return ToolResult("scan_links", True, data={
            "links": all_links,
            "broken": broken_links,
            "total": len(all_links),
            "broken_count": len(broken_links),
        })

    except Exception as e:
        return ToolResult("scan_links", False, error=str(e))


@register_tool("generate_report", "write execution reports", "Write a CSV or JSON report to 06_EXECUTION")
def tool_generate_report(vault_path: str, report_name: str, report_type: str = "csv",
                         headers: list = None, rows: list = None,
                         data: dict = None, subdir: str = "reports", **kwargs) -> ToolResult:
    """
    Generate a report file in 06_EXECUTION.

    Args:
        vault_path: Root path of the vault
        report_name: Filename for the report
        report_type: "csv" or "json"
        headers: CSV headers (for csv type)
        rows: List of row lists (for csv type)
        data: Dict data (for json type)
        subdir: Subdirectory within 06_EXECUTION (default: "reports")

    Returns:
        ToolResult with data = {"path": str}
    """
    try:
        report_dir = os.path.join(vault_path, "06_EXECUTION", subdir)
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, report_name)
        rel_path = os.path.relpath(report_path, vault_path)

        if report_type == "csv":
            with open(report_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if headers:
                    writer.writerow(headers)
                if rows:
                    writer.writerows(rows)
        elif report_type == "json":
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(data or {}, f, indent=2, default=str)
        else:
            return ToolResult("generate_report", False, error=f"Unknown report type: {report_type}")

        return ToolResult("generate_report", True, data={
            "path": rel_path,
            "report_type": report_type,
        }, artifacts=[rel_path])

    except Exception as e:
        return ToolResult("generate_report", False, error=str(e))


@register_tool("move_note", "move note", "Move a note between vault locations")
def tool_move_note(vault_path: str, source_path: str, dest_path: str, **kwargs) -> ToolResult:
    """
    Move a vault note from one location to another.

    Args:
        vault_path: Root path of the vault
        source_path: Vault-relative source path
        dest_path: Vault-relative destination path

    Returns:
        ToolResult with data = {"source": str, "destination": str}
    """
    full_source = os.path.join(vault_path, source_path)
    full_dest = os.path.join(vault_path, dest_path)

    if not os.path.exists(full_source):
        return ToolResult("move_note", False, error=f"Source not found: {source_path}")

    try:
        os.makedirs(os.path.dirname(full_dest), exist_ok=True)
        os.rename(full_source, full_dest)

        # Determine if this is an archive operation or a promotion
        change_type = "archive" if "99_ARCHIVE" in dest_path else "move"
        if "02_KNOWLEDGE" in dest_path or "03_PIPELINES" in dest_path or "04_PROJECTS" in dest_path:
            change_type = "promote"

        _log_state_change(
            vault_path, change_type, dest_path,
            before_state=source_path,
            after_state=dest_path,
            justification=f"Moved from {source_path} to {dest_path}",
            artifact_type="note",
        )

        return ToolResult("move_note", True, data={
            "source": source_path,
            "destination": dest_path,
        }, artifacts=[dest_path])

    except Exception as e:
        return ToolResult("move_note", False, error=str(e))


@register_tool("read_registry", "read registry", "Read a CSV registry file and return its contents")
def tool_read_registry(vault_path: str, registry_path: str, filter_field: str = None,
                       filter_value: str = None, **kwargs) -> ToolResult:
    """
    Read a CSV registry file.

    Args:
        vault_path: Root path of the vault
        registry_path: Vault-relative path to the CSV
        filter_field: Optional field name to filter by
        filter_value: Optional value to filter on

    Returns:
        ToolResult with data = {"rows": list[dict], "count": int, "headers": list}
    """
    full_path = os.path.join(vault_path, registry_path)

    if not os.path.exists(full_path):
        return ToolResult("read_registry", False, error=f"Registry not found: {registry_path}")

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            rows = []
            for row in reader:
                if filter_field and filter_value:
                    if row.get(filter_field) == filter_value:
                        rows.append(dict(row))
                else:
                    rows.append(dict(row))

        return ToolResult("read_registry", True, data={
            "path": registry_path,
            "headers": headers,
            "rows": rows,
            "count": len(rows),
        })

    except Exception as e:
        return ToolResult("read_registry", False, error=str(e))


@register_tool("append_registry", "write to registry", "Append a row to a CSV registry")
def tool_append_registry(vault_path: str, registry_path: str, row: dict, **kwargs) -> ToolResult:
    """
    Append a row to a CSV registry file.

    Args:
        vault_path: Root path of the vault
        registry_path: Vault-relative path to the CSV
        row: Dict of field_name: value

    Returns:
        ToolResult with data = {"path": str}
    """
    full_path = os.path.join(vault_path, registry_path)

    if not os.path.exists(full_path):
        return ToolResult("append_registry", False, error=f"Registry not found: {registry_path}")

    try:
        # Read existing headers
        with open(full_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []

        # Append the row
        with open(full_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers, extrasaction='ignore')
            writer.writerow(row)

        # Log state change
        _log_state_change(
            vault_path, "modify", registry_path,
            field_changed="row_appended",
            after_state=str(row),
            justification="Row appended via append_registry tool",
            artifact_type="csv",
        )

        return ToolResult("append_registry", True, data={
            "path": registry_path,
        }, artifacts=[registry_path])

    except Exception as e:
        return ToolResult("append_registry", False, error=str(e))
