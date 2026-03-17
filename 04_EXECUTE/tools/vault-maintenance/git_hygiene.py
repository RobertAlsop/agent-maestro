#!/usr/bin/env python3
"""git_hygiene.py — Git convention compliance detection.

Checks git state against AM — Git Conventions:
  1. Branch naming — local branches match configured patterns
  2. Stale branches — unmerged branches with last commit older than threshold
  3. Direct commits to master — non-merge commits on master (warnings, not findings)
  4. Pre-wave tag presence — completed waves have corresponding pre-wave-X.Y tags
  5. Tag naming consistency — all tags match configured naming patterns
  6. Commit message format — recent non-merge commits meet quality criteria
  7. Uncommitted changes — dirty working tree (warning, configurable)

Error isolation: each check runs independently. If a check errors, its error is
reported as a warning and the remaining checks continue. Exit code 2 only when no
checks complete successfully. This best-effort strategy follows Tool Conventions
Safety Rule 5 — fail safe, but with explicit best-effort behaviour.

Exit codes: 0 = clean, 1 = findings, 2 = error
"""

import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.vault_model import (
    standard_arg_parser, resolve_tool_paths, write_report,
    parse_completed_waves,
)

TOOL_NAME = "Git Hygiene"
REPORT_FILENAME = "Git_Hygiene_report.md"

DEFAULT_BRANCH_PATTERNS = [
    r"^wave-\d+\.\d+-[a-z0-9-]+$",
    r"^fix-[a-z0-9-]+$",
    r"^housekeeping-[a-z0-9-]+$",
]

DEFAULT_TAG_PATTERNS = [
    r"^pre-wave-\d+\.\d+$",
    r"^pre-[a-z0-9-]+$",
    r"^v\d+\.\d+\.\d+$",
]

DEFAULT_COMMIT_FORMAT_PATTERNS = [
    r"^SES-\d{3}:",
    r"^Wave \d+\.\d+:",
]

DEFAULT_COMMIT_REJECT_PATTERNS = [
    r"^(wip|stuff|updates|fixes|test|tmp|asdf)$",
]


# ---------------------------------------------------------------------------
# Git subprocess wrapper
# ---------------------------------------------------------------------------

def run_git(args: list, cwd: str) -> tuple:
    """Run a git command. Returns (stdout, stderr, returncode).

    All git interaction goes through this function so subprocess errors
    are caught in one place and callers get a consistent (str, str, int) tuple.
    """
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except FileNotFoundError:
        return "", "git not found in PATH", 1
    except subprocess.TimeoutExpired:
        return "", "git command timed out", 1
    except Exception as e:
        return "", str(e), 1


def parse_branches(output: str, master_branch: str) -> list:
    """Parse `git branch --list` output into a list of branch names.

    Handles the leading '  ' (inactive) and '* ' (current) markers.
    Skips detached HEAD entries.
    """
    branches = []
    for line in output.splitlines():
        if "(HEAD detached" in line:
            continue
        branch = line.strip().lstrip("* ").strip()
        if branch and branch != master_branch:
            branches.append(branch)
    return branches


def check_git_available(vault_root: str) -> tuple:
    """Verify vault is inside a git repository. Returns (ok, error_message)."""
    stdout, stderr, code = run_git(["rev-parse", "--git-dir"], vault_root)
    if code != 0:
        return False, (
            f"vault is not a git repository (or git is not available): {stderr}"
        )
    return True, None


# ---------------------------------------------------------------------------
# Check 1: Branch naming
# Source: AM — Git Conventions §Branch Naming
# ---------------------------------------------------------------------------

def check1_branch_naming(vault_root: str, config: dict) -> tuple:
    """Check that all local branches (except master) match a configured pattern."""
    patterns = [
        re.compile(p)
        for p in config.get("git_branch_patterns", DEFAULT_BRANCH_PATTERNS)
    ]
    master_branch = config.get("master_branch", "master")

    stdout, stderr, code = run_git(["branch", "--list"], vault_root)
    if code != 0:
        return [], [], 0, 0, f"Check 1 (branch naming): git branch failed: {stderr}"

    branches = parse_branches(stdout, master_branch)
    findings = []
    checked = len(branches)
    passed = 0

    for branch in branches:
        if any(p.match(branch) for p in patterns):
            passed += 1
        else:
            findings.append(
                f"Branch `{branch}`: does not match any configured naming pattern"
            )

    return findings, [], checked, passed, None


# ---------------------------------------------------------------------------
# Check 2: Stale branches
# Source: AM — Git Conventions §Stale Branches
# ---------------------------------------------------------------------------

def check2_stale_branches(vault_root: str, config: dict) -> tuple:
    """Check for unmerged branches whose last commit exceeds the stale threshold."""
    threshold_days = int(config.get("stale_branch_threshold_days", 30))
    master_branch = config.get("master_branch", "master")
    cutoff = datetime.now(timezone.utc) - timedelta(days=threshold_days)

    stdout, stderr, code = run_git(["branch", "--list"], vault_root)
    if code != 0:
        return [], [], 0, 0, f"Check 2 (stale branches): git branch failed: {stderr}"

    branches = parse_branches(stdout, master_branch)

    # Branches already merged into master are exempt
    merged_out, _, _ = run_git(["branch", "--merged", master_branch], vault_root)
    merged = set(parse_branches(merged_out, master_branch))

    findings = []
    checked = len(branches)
    passed = 0

    for branch in branches:
        if branch in merged:
            passed += 1
            continue

        date_out, date_err, date_code = run_git(
            ["log", "-1", "--format=%ci", branch], vault_root
        )
        if date_code != 0 or not date_out:
            findings.append(
                f"Branch `{branch}`: could not determine last commit date"
            )
            continue

        try:
            # git --format=%ci: "2026-03-17 14:30:00 +0000"
            last_commit = datetime.strptime(date_out[:19], "%Y-%m-%d %H:%M:%S")
            last_commit = last_commit.replace(tzinfo=timezone.utc)
        except ValueError:
            findings.append(
                f"Branch `{branch}`: could not parse last commit date: {date_out!r}"
            )
            continue

        if last_commit < cutoff:
            days_old = (datetime.now(timezone.utc) - last_commit).days
            findings.append(
                f"Branch `{branch}`: stale — last commit {days_old} days ago "
                f"(threshold: {threshold_days} days), not merged to {master_branch}"
            )
        else:
            passed += 1

    return findings, [], checked, passed, None


# ---------------------------------------------------------------------------
# Check 3: Direct commits to master (warnings, not findings)
# Source: AM — Git Conventions §The Protected Baseline
# ---------------------------------------------------------------------------

def check3_direct_master_commits(vault_root: str, config: dict) -> tuple:
    """Flag non-merge commits on master as warnings for human evaluation.

    The tool cannot mechanically distinguish trivial housekeeping from
    substantive work. Reports as warnings so the human evaluates whether
    the housekeeping exception applies. Convention 7 (Conservative).
    """
    master_branch = config.get("master_branch", "master")
    window = int(config.get("master_commit_window", 50))

    stdout, stderr, code = run_git(
        ["log", f"--max-count={window}", "--first-parent", master_branch,
         "--format=%H|%P|%s"],
        vault_root,
    )
    if code != 0:
        return [], [], 0, 0, (
            f"Check 3 (direct master commits): git log failed: {stderr}"
        )

    commits = [line for line in stdout.splitlines() if line.strip()]
    warnings = []
    checked = len(commits)
    passed = 0

    for line in commits:
        parts = line.split("|", 2)
        if len(parts) < 2:
            passed += 1
            continue
        commit_hash = parts[0][:8]
        parents = parts[1].split() if parts[1] else []
        subject = parts[2] if len(parts) > 2 else ""

        if len(parents) > 1:
            # Merge commit — exempt and clean
            passed += 1
        else:
            warnings.append(
                f"Commit `{commit_hash}` on {master_branch}: direct commit (not a merge)"
                f" — subject: {subject!r} — verify this is trivial housekeeping"
            )

    return [], warnings, checked, passed, None


# ---------------------------------------------------------------------------
# Check 4: Pre-wave tag presence
# Source: AM — Git Conventions §Checkpoint Tags
# ---------------------------------------------------------------------------

def check4_pre_wave_tags(vault_root: str, config: dict) -> tuple:
    """Check that each completed wave (from Roadmap) has a pre-wave-X.Y tag.

    Uses parse_completed_waves() from vault_model — same cross-domain dependency
    as Wave 8.2 tools. If the Roadmap is unreadable, this check fails gracefully
    (error reported, other checks continue). The wave_id string is used for exact
    tag name construction, not as a regex, so no escaping is needed.
    """
    roadmap_file = config.get("roadmap_file", "02_KNOWLEDGE/governance/AM — Roadmap.md")

    if not os.path.isabs(roadmap_file):
        roadmap_path = os.path.join(vault_root, roadmap_file)
    else:
        roadmap_path = roadmap_file

    if not os.path.exists(roadmap_path):
        return (
            [], [f"Check 4 (pre-wave tags): roadmap not found at {roadmap_path} — skipped"],
            0, 0, None,
        )

    try:
        with open(roadmap_path, "r", encoding="utf-8") as f:
            roadmap_content = f.read()
    except Exception as e:
        return [], [], 0, 0, f"Check 4 (pre-wave tags): could not read roadmap: {e}"

    completed_waves = parse_completed_waves(roadmap_content)
    if not completed_waves:
        # No completed waves found — nothing to check, not an error
        return [], [], 0, 0, None

    tags_out, tags_err, tags_code = run_git(["tag", "--list"], vault_root)
    if tags_code != 0:
        return [], [], 0, 0, f"Check 4 (pre-wave tags): git tag failed: {tags_err}"

    existing_tags = set(tags_out.splitlines())
    findings = []
    checked = len(completed_waves)
    passed = 0

    for wave in completed_waves:
        identifier = wave["identifier"]
        # Extract numeric wave ID: "Wave 8.2" → "8.2"
        wave_id_match = re.match(r"Wave\s+([\d.]+)", identifier)
        if not wave_id_match:
            findings.append(
                f"Wave `{identifier}`: could not extract wave ID for tag check"
            )
            continue

        wave_id = wave_id_match.group(1)
        expected_tag = f"pre-wave-{wave_id}"

        if expected_tag in existing_tags:
            passed += 1
        else:
            findings.append(
                f"Wave `{identifier}`: no `{expected_tag}` tag found — "
                f"checkpoint tag required before wave work begins"
            )

    return findings, [], checked, passed, None


# ---------------------------------------------------------------------------
# Check 5: Tag naming consistency
# Source: AM — Git Conventions §Tag Conventions
# ---------------------------------------------------------------------------

def check5_tag_naming(vault_root: str, config: dict) -> tuple:
    """Check that all repository tags match a configured naming pattern.

    Historical tags that predate the conventions will be flagged — this is
    correct. They are real naming drift, documented for awareness.
    """
    patterns = [
        re.compile(p)
        for p in config.get("git_tag_patterns", DEFAULT_TAG_PATTERNS)
    ]

    stdout, stderr, code = run_git(["tag", "--list"], vault_root)
    if code != 0:
        return [], [], 0, 0, f"Check 5 (tag naming): git tag failed: {stderr}"

    tags = [t for t in stdout.splitlines() if t]
    findings = []
    checked = len(tags)
    passed = 0

    for tag in tags:
        if any(p.match(tag) for p in patterns):
            passed += 1
        else:
            findings.append(
                f"Tag `{tag}`: does not match any configured naming pattern"
            )

    return findings, [], checked, passed, None


# ---------------------------------------------------------------------------
# Check 6: Commit message format
# Source: AM — Git Conventions §Commit Conventions
# ---------------------------------------------------------------------------

def check6_commit_messages(vault_root: str, config: dict) -> tuple:
    """Check recent non-merge commit messages meet quality criteria.

    Conservative: a commit passes if it matches a format pattern OR meets
    minimum length. Only fails if it matches a reject pattern, or fails
    both the format check AND the length check. Merge commits are exempt —
    git generates their messages, not AM conventions.
    """
    window = int(config.get("commit_message_window", 50))
    min_length = int(config.get("commit_min_length", 5))
    format_patterns = [
        re.compile(p)
        for p in config.get("commit_format_patterns", DEFAULT_COMMIT_FORMAT_PATTERNS)
    ]
    reject_patterns = [
        re.compile(p, re.IGNORECASE)
        for p in config.get("commit_reject_patterns", DEFAULT_COMMIT_REJECT_PATTERNS)
    ]

    stdout, stderr, code = run_git(
        ["log", f"--max-count={window}", "--format=%H|%P|%s"],
        vault_root,
    )
    if code != 0:
        return [], [], 0, 0, f"Check 6 (commit messages): git log failed: {stderr}"

    commits = [line for line in stdout.splitlines() if line.strip()]
    findings = []
    checked = 0
    passed = 0

    for line in commits:
        parts = line.split("|", 2)
        if len(parts) < 3:
            continue
        commit_hash = parts[0][:8]
        parents = parts[1].split() if parts[1] else []
        subject = parts[2]

        # Merge commits exempt — git generates their messages
        if len(parents) > 1:
            continue

        checked += 1

        # Reject patterns: hard fail regardless of length
        if any(p.match(subject.strip()) for p in reject_patterns):
            findings.append(
                f"Commit `{commit_hash}`: message {subject!r} matches a known bad pattern"
            )
            continue

        # Pass if format matches OR message meets minimum length
        format_ok = any(p.match(subject) for p in format_patterns)
        length_ok = len(subject.strip()) >= min_length

        if format_ok or length_ok:
            passed += 1
        else:
            findings.append(
                f"Commit `{commit_hash}`: message {subject!r} does not match any "
                f"accepted format and is below minimum length ({min_length} characters)"
            )

    return findings, [], checked, passed, None


# ---------------------------------------------------------------------------
# Check 7: Uncommitted changes (warning, not finding)
# Source: AM — Git Conventions §Safety Rules (Rule 3)
# ---------------------------------------------------------------------------

def check7_uncommitted_changes(vault_root: str, config: dict) -> tuple:
    """Warn if the working tree has uncommitted changes.

    Reports as a warning, not a finding. A dirty working tree is normal
    during active development; the tool cannot distinguish in-progress work
    from forgotten uncommitted changes. Convention 7 (Conservative).
    Suppressible via check_uncommitted_changes: false to prevent warning
    fatigue during active-session runs.
    """
    if not config.get("check_uncommitted_changes", True):
        return [], [], 0, 0, None

    stdout, stderr, code = run_git(["status", "--porcelain"], vault_root)
    if code != 0:
        return [], [], 0, 0, (
            f"Check 7 (uncommitted changes): git status failed: {stderr}"
        )

    if not stdout:
        return [], [], 1, 1, None

    lines = [line for line in stdout.splitlines() if line.strip()]
    staged = sum(
        1 for line in lines
        if len(line) >= 2 and line[0] not in (" ", "?")
    )
    untracked = sum(1 for line in lines if line[:2] == "??")
    unstaged = sum(
        1 for line in lines
        if len(line) >= 2 and line[1] not in (" ", "?") and line[0] == " "
    )

    warnings = [
        f"Working tree has uncommitted changes: "
        f"{staged} staged, {unstaged} unstaged, {untracked} untracked files — "
        f"consider committing before session close"
    ]
    return [], warnings, 1, 0, None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = standard_arg_parser(
        "Detect git convention violations per AM — Git Conventions."
    )
    args = parser.parse_args()
    vault_root, config, output_dir, tool_dir = resolve_tool_paths(args, __file__)

    # Git availability check — non-git vault exits with code 2, not a traceback
    git_ok, git_err = check_git_available(vault_root)
    if not git_ok:
        print(f"ERROR: {git_err}", file=sys.stderr)
        sys.exit(2)

    # Best-effort error isolation: each check runs independently.
    # If a check returns an error string, it is reported as a warning and
    # the remaining checks continue. Exit code 2 only if no checks complete.
    checks = [
        ("Check 1 (branch naming)",       lambda: check1_branch_naming(vault_root, config)),
        ("Check 2 (stale branches)",       lambda: check2_stale_branches(vault_root, config)),
        ("Check 3 (direct master commits)", lambda: check3_direct_master_commits(vault_root, config)),
        ("Check 4 (pre-wave tags)",        lambda: check4_pre_wave_tags(vault_root, config)),
        ("Check 5 (tag naming)",           lambda: check5_tag_naming(vault_root, config)),
        ("Check 6 (commit messages)",      lambda: check6_commit_messages(vault_root, config)),
        ("Check 7 (uncommitted changes)",  lambda: check7_uncommitted_changes(vault_root, config)),
    ]

    all_findings = []
    all_warnings = []
    total_checked = 0
    total_passed = 0
    completed_checks = 0

    for check_name, check_fn in checks:
        try:
            findings, warnings, checked, passed, error = check_fn()
            if error:
                # Check encountered a problem — report and continue
                all_warnings.append(f"[ERROR] {error}")
            else:
                completed_checks += 1
            all_findings.extend(findings)
            all_warnings.extend(warnings)
            total_checked += checked
            total_passed += passed
        except Exception as e:
            all_warnings.append(
                f"[ERROR] {check_name}: unexpected exception: {e}"
            )

    # Determine exit code per best-effort strategy
    if all_findings:
        result = "FINDINGS"
        exit_code = 1
    elif completed_checks == 0:
        result = "ERROR"
        exit_code = 2
    else:
        result = "CLEAN"
        exit_code = 0

    report_path = write_report(
        output_dir, REPORT_FILENAME, TOOL_NAME, vault_root,
        result, total_checked, total_passed, all_findings, all_warnings,
    )

    if not args.quiet:
        print(
            f"{TOOL_NAME}: {result} "
            f"({total_checked} checked, {len(all_findings)} findings, "
            f"{len(all_warnings)} warnings)"
        )
        print(f"Report: {report_path}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
