#!/usr/bin/env python3
"""Validate a project's docs/ tree against the DocOS standard.

Usage:
    python validate_docs.py <project-root>

Checks (exit code 1 if any error):
- required root files exist (README.md, INDEX.md, AI_INDEX.md)
- file/folder names are lowercase kebab-case (ADR/INC/vX.Y.Z patterns allowed)
- ADR files match ADR-NNNN-<slug>.md and contain a Status section
- front matter `status:` values are from the allowed set
- relative markdown links resolve to existing files
- no obviously secret-looking content (very rough heuristic)
"""
import re
import sys
from pathlib import Path

REQUIRED_ROOT = ["README.md", "INDEX.md", "AI_INDEX.md"]
ALLOWED_STATUS = {"draft", "proposed", "active", "deprecated", "archived", "superseded"}

KEBAB = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*(?:\.[a-z0-9]+)?$")
SPECIAL = re.compile(
    r"^(README|INDEX|AI_INDEX|OWNERS|GLOSSARY|ROADMAP|CHANGELOG|SKILL)\.md$"
    r"|^ADR-\d{4}-[a-z0-9-]+\.md$"
    r"|^INC-\d{4}-\d{3}-[a-z0-9-]+\.md$"
    r"|^v\d+\.\d+\.\d+\.md$"
    r"|^unreleased\.md$"
    r"|^openapi\.(yaml|yml|json)$"
)
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
SECRET = re.compile(
    r"(?i)(api[_-]?key|password|secret|token)\s*[:=]\s*['\"]?[A-Za-z0-9+/_-]{16,}")


def check_front_matter(text: str, rel: str, errors: list) -> None:
    if not text.startswith("---\n"):
        return
    end = text.find("\n---", 4)
    if end == -1:
        errors.append(f"{rel}: unterminated front matter")
        return
    fm = text[4:end]
    m = re.search(r"^status:\s*(\S+)", fm, re.MULTILINE)
    if m and m.group(1).strip("'\"") not in ALLOWED_STATUS:
        errors.append(f"{rel}: invalid status '{m.group(1)}' "
                      f"(allowed: {', '.join(sorted(ALLOWED_STATUS))})")
    if m and m.group(1).strip("'\"") == "deprecated" and "deprecated_by:" not in fm:
        errors.append(f"{rel}: status is deprecated but no deprecated_by given")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    docs = Path(sys.argv[1]).resolve() / "docs"
    if not docs.is_dir():
        print(f"error: {docs} not found")
        return 1

    errors: list = []
    warnings: list = []

    for name in REQUIRED_ROOT:
        if not (docs / name).exists():
            errors.append(f"missing required file: docs/{name}")

    for path in sorted(docs.rglob("*")):
        rel = str(path.relative_to(docs.parent))
        name = path.name
        # Directories starting with "_" hold vendored or generated assets
        # (e.g. an exported design-system bundle) — not authored docs, so
        # naming and content rules don't apply inside them.
        parts = path.relative_to(docs).parts
        if any(p.startswith("_") for p in parts[:-1]) or (path.is_dir() and name.startswith("_")):
            continue
        if path.is_dir():
            if not KEBAB.match(name) and not re.match(r"^\d{2}-[a-z-]+$", name):
                errors.append(f"{rel}: folder name is not kebab-case")
            continue
        if not (SPECIAL.match(name) or KEBAB.match(name)):
            errors.append(f"{rel}: file name violates naming convention")
        if path.suffix != ".md":
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        check_front_matter(text, rel, errors)

        if re.match(r"^ADR-\d{4}-", name) and "## Status" not in text:
            errors.append(f"{rel}: ADR without a '## Status' section")

        if SECRET.search(text):
            errors.append(f"{rel}: possible secret committed to docs")

        # Links inside fenced code blocks are examples, not real references.
        prose = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for target in LINK.findall(prose):
            if re.match(r"^[a-z]+://|^mailto:", target):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                warnings.append(f"{rel}: broken link -> {target}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
