#!/usr/bin/env python3
"""vault_model.py — Shared vault model library for pipeline enforcement tools.

Parses all vault markdown files, extracts YAML frontmatter, and builds an
in-memory model of artifacts with their types, statuses, relationships,
locations, and creation dates.

Each pipeline enforcement tool imports this library and calls build_vault_model()
to get a dict of VaultArtifact objects keyed by relative path.

Design: each tool rebuilds the model per invocation (tools run as separate
processes). Economy value is code reuse (DRY) — one implementation of YAML
parsing, date resolution, config loading, and relationship traversal.
"""

import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------------------
# Config loading (mirrors yaml_validator.py approach)
# ---------------------------------------------------------------------------

def parse_config(config_path: str) -> dict:
    """Parse a YAML config file. Returns empty dict on missing/invalid."""
    if not config_path or not os.path.exists(config_path):
        return {}
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def load_merged_config(config_path: str, defaults_path: str) -> dict:
    """Load defaults then override with vault-specific config."""
    config = {}
    if defaults_path and os.path.exists(defaults_path):
        config = parse_config(defaults_path)
    if config_path and os.path.exists(config_path):
        override = parse_config(config_path)
        config.update(override)
    return config


# ---------------------------------------------------------------------------
# Exclusion and folder classification
# ---------------------------------------------------------------------------

def is_excluded(rel_path: str, exclude_patterns: list) -> bool:
    """Check if a relative path matches any exclude pattern."""
    for pattern in exclude_patterns:
        if rel_path.startswith(pattern) or rel_path.startswith(pattern + '/'):
            return True
        if ('/' + pattern + '/') in ('/' + rel_path + '/'):
            return True
        if os.path.basename(rel_path) == pattern:
            return True
    return False


def is_frontmatter_optional(rel_path: str, optional_folders: list) -> bool:
    """Check if file is in a folder where frontmatter is optional."""
    for folder in optional_folders:
        if rel_path.startswith(folder + '/') or rel_path.startswith(folder + os.sep):
            return True
    return False


def is_structural_file(filename: str) -> bool:
    """Check if file is a structural file that never has frontmatter."""
    return filename in ('CLAUDE.md', 'SYSTEM_MAP.md', 'README.md')


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def extract_frontmatter(content: str) -> tuple:
    """Extract YAML frontmatter from markdown content.

    Returns (frontmatter_dict, body_content, error_string).
    frontmatter_dict is None if no frontmatter; body_content is the text after ---
    """
    if not content.startswith('---'):
        return None, content, None

    lines = content.split('\n')
    end_idx = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return None, content, "frontmatter not closed (missing closing ---)"

    fm_text = '\n'.join(lines[1:end_idx])
    body = '\n'.join(lines[end_idx + 1:])

    try:
        fm = yaml.safe_load(fm_text)
        if fm is None:
            return None, body, "frontmatter is empty"
        if not isinstance(fm, dict):
            return None, body, "frontmatter is not a YAML mapping"
        return fm, body, None
    except yaml.YAMLError as e:
        return None, body, f"YAML parse error: {e}"


# ---------------------------------------------------------------------------
# Date resolution
# ---------------------------------------------------------------------------

def resolve_creation_date(filepath: str, frontmatter: Optional[dict]) -> Optional[date]:
    """Resolve creation date from frontmatter 'created' field or filesystem.

    Conservative: when date is ambiguous, uses the most recent available
    date to bias toward "not yet stale" rather than false positives.
    """
    # Try frontmatter first
    if frontmatter and 'created' in frontmatter:
        val = str(frontmatter['created'])
        try:
            return datetime.strptime(val, '%Y-%m-%d').date()
        except ValueError:
            pass

    # Fall back to filesystem modification time (most recent available)
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime).date()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Wiki-link parsing and normalization
# ---------------------------------------------------------------------------

# Matches [[Note Title]] and [[Note Title|Alias]]
WIKI_LINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:\|[^\]]*?)?\]\]')


def parse_wiki_links(text: str) -> list:
    """Extract all wiki-link targets from text. Returns list of normalized titles."""
    return [normalize_title(m.group(1).strip()) for m in WIKI_LINK_RE.finditer(text)]


def normalize_title(title: str) -> str:
    """Normalize a wiki-link target or filename for comparison.

    Strips path components, .md extension, and lowercases.
    """
    # Remove any path prefix (Obsidian links can include folder paths)
    title = title.split('/')[-1]
    # Remove .md extension if present
    if title.endswith('.md'):
        title = title[:-3]
    return title.strip().lower()


def file_title(rel_path: str) -> str:
    """Get normalized title from a relative file path."""
    basename = os.path.basename(rel_path)
    if basename.endswith('.md'):
        basename = basename[:-3]
    return basename.strip().lower()


# ---------------------------------------------------------------------------
# VaultArtifact dataclass
# ---------------------------------------------------------------------------

class VaultArtifact:
    """Represents a single markdown file in the vault."""

    __slots__ = (
        'filepath', 'rel_path', 'filename', 'frontmatter', 'content',
        'body', 'frontmatter_optional', 'frontmatter_error',
        'has_frontmatter', 'artifact_type', 'status', 'authority_weight',
        'created_date', 'derives_from', 'governs', 'related',
        'all_wiki_links', 'title',
    )

    def __init__(self, filepath: str, rel_path: str, vault_root: str,
                 frontmatter_optional: bool):
        self.filepath = filepath
        self.rel_path = rel_path
        self.filename = os.path.basename(filepath)

        # Read content
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.content = f.read()
        except Exception as e:
            self.content = ''
            self.frontmatter = None
            self.body = ''
            self.frontmatter_error = str(e)
            self.has_frontmatter = False
            self._set_defaults()
            self.frontmatter_optional = frontmatter_optional
            self.created_date = resolve_creation_date(filepath, None)
            self.all_wiki_links = []
            return

        fm, body, error = extract_frontmatter(self.content)

        self.frontmatter = fm
        self.body = body
        self.frontmatter_error = error
        self.has_frontmatter = fm is not None
        self.frontmatter_optional = frontmatter_optional
        self.created_date = resolve_creation_date(filepath, fm)

        if fm:
            self.artifact_type = fm.get('type')
            self.status = fm.get('status')
            self.authority_weight = fm.get('authority_weight')
            self.title = fm.get('title', '')
            rels = fm.get('relationships', {}) or {}
            if isinstance(rels, dict):
                self.derives_from = rels.get('derives_from') or []
                self.governs = rels.get('governs') or []
                self.related = rels.get('related') or []
            else:
                self.derives_from = []
                self.governs = []
                self.related = []
        else:
            self._set_defaults()

        # Parse all wiki-links from entire content (frontmatter + body)
        self.all_wiki_links = parse_wiki_links(self.content)

    def _set_defaults(self):
        self.artifact_type = None
        self.status = None
        self.authority_weight = None
        self.title = ''
        self.derives_from = []
        self.governs = []
        self.related = []

    def references_title(self, target_title: str) -> bool:
        """Check if this artifact wiki-links to target_title (normalized)."""
        normalized = normalize_title(target_title)
        return normalized in self.all_wiki_links

    def has_section(self, heading: str) -> bool:
        """Check if body contains a markdown heading with the given text (case-insensitive)."""
        pattern = re.compile(
            r'^#{1,6}\s+' + re.escape(heading) + r'\s*$',
            re.MULTILINE | re.IGNORECASE
        )
        return bool(pattern.search(self.body))

    def has_section_with_content(self, heading: str) -> bool:
        """Check if body contains a heading followed by non-empty content."""
        pattern = re.compile(
            r'^(#{1,6})\s+' + re.escape(heading) + r'\s*\n(.*?)(?=^#{1,6}\s|\Z)',
            re.MULTILINE | re.IGNORECASE | re.DOTALL
        )
        m = pattern.search(self.body)
        if not m:
            return False
        section_content = m.group(2).strip()
        return bool(section_content)

    def __repr__(self):
        return f"VaultArtifact({self.rel_path!r}, type={self.artifact_type!r}, status={self.status!r})"


# ---------------------------------------------------------------------------
# Vault model builder
# ---------------------------------------------------------------------------

def build_vault_model(vault_root: str, config: dict) -> dict:
    """Parse all vault markdown files and return dict keyed by rel_path.

    Keys are relative paths (using os.sep). Values are VaultArtifact objects.
    Respects exclude_patterns and frontmatter_optional_folders from config.
    Skips structural files (CLAUDE.md, SYSTEM_MAP.md, README.md).
    """
    exclude_patterns = config.get('exclude_patterns', [])
    optional_folders = config.get('frontmatter_optional_folders', [])

    artifacts = {}

    for root, dirs, files in os.walk(vault_root):
        rel_root = os.path.relpath(root, vault_root)
        if rel_root == '.':
            rel_root = ''

        # Prune excluded directories in-place
        dirs[:] = [
            d for d in sorted(dirs)
            if not is_excluded(
                os.path.join(rel_root, d).lstrip('/') if rel_root else d,
                exclude_patterns
            )
        ]

        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue

            rel_path = os.path.join(rel_root, fname).lstrip('/')
            if not rel_root:
                rel_path = fname

            if is_excluded(rel_path, exclude_patterns):
                continue
            if is_structural_file(fname):
                continue

            frontmatter_optional = is_frontmatter_optional(rel_path, optional_folders)
            filepath = os.path.join(root, fname)

            artifact = VaultArtifact(filepath, rel_path, vault_root, frontmatter_optional)
            artifacts[rel_path] = artifact

    return artifacts


# ---------------------------------------------------------------------------
# Roadmap parsing
# ---------------------------------------------------------------------------

def parse_completed_waves(roadmap_content: str) -> list:
    """Parse the Roadmap for completed waves (lines with ✓ marker).

    Returns list of dicts: {
        'identifier': e.g. 'Wave 5', 'Wave 8.1',
        'heading': full heading text e.g. 'Wave 5 — Consolidation (v0.5.0)',
        'level': heading depth (number of #)
    }

    Conservative: skips lines it cannot parse rather than producing false findings.
    """
    completed = []
    # Match headings ending with ✓ (with optional whitespace)
    # e.g. "### Wave 6 — Mechanical Integrity ✓"
    # e.g. "#### Wave 8.1 — Governance ✓"
    # Use .*? (non-greedy, no DOTALL so . does not match newlines) to prevent
    # cross-line matching. $ with MULTILINE anchors to end of line.
    heading_re = re.compile(r'^(#{2,6})\s+(Wave\s+[\d.]+\b.*?)\s*✓\s*$', re.MULTILINE)

    for m in heading_re.finditer(roadmap_content):
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        # Extract wave identifier: "Wave X" or "Wave X.Y"
        id_match = re.match(r'(Wave\s+[\d.]+)', heading_text)
        if id_match:
            identifier = id_match.group(1)
            completed.append({
                'identifier': identifier,
                'heading': heading_text,
                'level': level,
            })
        # else: skip unparseable entry (conservative)

    return completed


# ---------------------------------------------------------------------------
# Reference checking helpers
# ---------------------------------------------------------------------------

def any_artifact_references(title: str, artifacts: dict,
                            folder_filter: Optional[str] = None) -> bool:
    """Check if any artifact (optionally in folder_filter) references title via wiki-link."""
    normalized = normalize_title(title)
    for rel_path, artifact in artifacts.items():
        if folder_filter and not rel_path.startswith(folder_filter):
            continue
        if normalized in artifact.all_wiki_links:
            return True
    return False


def find_artifacts_in_folder(folder: str, artifacts: dict) -> list:
    """Return list of VaultArtifact objects whose rel_path starts with folder."""
    return [a for rel, a in artifacts.items() if rel.startswith(folder + '/') or rel.startswith(folder + os.sep)]


def find_artifact_by_title(title: str, artifacts: dict) -> Optional['VaultArtifact']:
    """Find first artifact whose title or filename matches (normalized)."""
    normalized = normalize_title(title)
    for rel_path, artifact in artifacts.items():
        if file_title(rel_path) == normalized:
            return artifact
        if artifact.title and normalize_title(artifact.title) == normalized:
            return artifact
    return None


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------

def write_report(output_dir: str, report_filename: str, tool_name: str,
                 vault_root: str, result: str,
                 checked: int, passed: int,
                 findings: list, warnings: list) -> str:
    """Write a standardized Markdown report. Returns the report file path."""
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, report_filename)
    failed = checked - passed

    with open(report_path, 'w') as f:
        f.write(f"# {tool_name} Report\n\n")
        f.write(f"**Vault:** {vault_root}\n")
        f.write(f"**Date:** {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')}\n")
        f.write(f"**Result:** {result}\n\n")
        f.write("## Summary\n\n")
        f.write("| Checked | Passed | Failed | Warnings |\n")
        f.write("|---------|--------|--------|----------|\n")
        f.write(f"| {checked} | {passed} | {failed} | {len(warnings)} |\n\n")

        if findings:
            f.write("## Findings\n\n")
            for finding in findings:
                f.write(f"- {finding}\n")
            f.write("\n")

        if warnings:
            f.write("## Warnings (uncertain)\n\n")
            for warning in warnings:
                f.write(f"- {warning}\n")
            f.write("\n")

    return report_path


def standard_arg_parser(description: str):
    """Return a pre-configured argparse.ArgumentParser matching tool conventions."""
    import argparse
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--vault-root', required=True,
                        help='Vault root directory')
    parser.add_argument('--config', default='',
                        help='Path to vault-specific config file')
    parser.add_argument('--output-dir', default='',
                        help='Report output directory')
    parser.add_argument('--quiet', action='store_true',
                        help='Suppress stdout, write report only')
    return parser


def resolve_tool_paths(args, script_file: str) -> tuple:
    """Resolve vault_root, config, output_dir from args and script location.

    Returns (vault_root, config, output_dir, tool_dir).
    """
    vault_root = os.path.abspath(args.vault_root)
    if not os.path.isdir(vault_root):
        print(f"ERROR: vault root does not exist: {vault_root}", file=sys.stderr)
        sys.exit(2)

    script_dir = os.path.dirname(os.path.abspath(script_file))
    # script_dir is vault-maintenance/ (tools live there directly)
    tool_dir = script_dir
    defaults_path = os.path.join(tool_dir, 'config', 'defaults.conf')
    config = load_merged_config(args.config, defaults_path)
    config['vault_root'] = vault_root

    output_dir = args.output_dir or config.get('output_dir', 'reports')
    if not os.path.isabs(output_dir):
        output_dir = os.path.join(tool_dir, output_dir)

    return vault_root, config, output_dir, tool_dir
