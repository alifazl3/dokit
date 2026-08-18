#!/usr/bin/env python3
"""Scaffold a DocOS docs/ structure in a target project.

Usage:
    python init_docs.py <project-root> [--minimal] [--with-mobile]
                        [--no-changelog] [--force]

Creates docs/ with the DocOS root files, numbered section folders, a
changelog/ folder for per-change entries (on by default, skip with
--no-changelog), and a templates/ folder copied from this skill. Existing
files are never overwritten unless --force is given.
"""
import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent

FULL_SECTIONS = [
    "00-governance", "01-product", "02-business", "03-requirements",
    "04-domain", "05-architecture", "06-api", "07-services", "08-database",
    "09-events", "10-security", "11-frontend", "12-mobile", "13-ai",
    "14-testing", "15-devops", "16-observability", "17-operations",
    "18-playbooks", "19-decisions", "20-features", "21-releases",
    "22-scenarios", "23-runbooks", "24-reference",
]

MINIMAL_SECTIONS = [
    "architecture", "api", "domain", "features", "testing",
    "operations", "decisions", "runbooks",
]

SECTION_TITLES = {
    "00-governance": "Governance — documentation and development rules",
    "01-product": "Product — vision, personas, roadmap",
    "02-business": "Business — model, rules, stakeholders",
    "03-requirements": "Requirements — functional and non-functional",
    "04-domain": "Domain — entities, aggregates, invariants",
    "05-architecture": "Architecture — C4 views, data flow, constraints",
    "06-api": "API — OpenAPI contract (source of truth) and conventions",
    "07-services": "Services — one folder per service",
    "08-database": "Database — schemas, tables, migrations, performance",
    "09-events": "Events — catalog, schemas, publishers, subscribers",
    "10-security": "Security — model, roles, threat model (no real secrets!)",
    "11-frontend": "Frontend — architecture, routing, design system",
    "12-mobile": "Mobile — architecture, releases, store deployment",
    "13-ai": "AI — agents, prompts, guardrails, evaluation",
    "14-testing": "Testing — strategy, pyramid, quality gates",
    "15-devops": "DevOps — environments, CI/CD, kubernetes, helm",
    "16-observability": "Observability — logging, metrics, tracing, alerts",
    "17-operations": "Operations — deployment, rollback, backup, scaling",
    "18-playbooks": "Playbooks — incident response per situation",
    "19-decisions": "Decisions — ADRs (ADR-NNNN-slug.md)",
    "20-features": "Features — one folder per feature",
    "21-releases": "Releases — vX.Y.Z.md release notes",
    "22-scenarios": "Scenarios — real user and system flows",
    "23-runbooks": "Runbooks — step-by-step operational procedures",
    "24-reference": "Reference — commands, env vars, links, standards",
}

ROOT_FILES = {
    "README.md": """# Project Documentation

This folder is the single source of truth for project knowledge (DocOS).

## Start Here

- [Documentation Index](./INDEX.md)
- [AI Agent Index](./AI_INDEX.md)
- [Glossary](./GLOSSARY.md)
- [Owners](./OWNERS.md)
""",
    "INDEX.md": """# Documentation Index

<!-- Keep this current: every new document gets a line here. -->
""",
    "AI_INDEX.md": """# AI Project Index

## Project Context

<!-- One paragraph: what this project is. -->

## Main Domains

-

## Important Paths

- API Contract: `docs/06-api/openapi.yaml`
- Domain Docs: `docs/04-domain/`
- Feature Docs: `docs/20-features/`
- Decisions (ADRs): `docs/19-decisions/`
- Runbooks: `docs/23-runbooks/`

## Build & Test Commands

<!-- Exact commands an agent should run. -->

## Required Checks

Before completing a change:

1. Update related feature documentation.
2. Update OpenAPI when API behavior changes.
3. Add or update tests.
4. Add an ADR when architecture changes.
""",
    "OWNERS.md": """# Documentation Owners

| Area | Owner | Backup |
|---|---|---|
""",
    "GLOSSARY.md": """# Glossary

<!-- One official definition per term. -->
""",
    "ROADMAP.md": """# Roadmap
""",
    "changelog/README.md": """# Changelog entries

One document per finished change, named `{date}_{title}.md`:

    2026-08-05_internal-api-proxy.md

Copy `../templates/changelog-entry-template.md` and fill in Summary,
Files Changed, Tests Run, and Follow-ups / Risks. This complements the
one-line entry in `../CHANGELOG.md` — both are written when the change is
finished, in the same commit.
""",
    "CHANGELOG.md": """# Changelog

## Unreleased

### Added
""",
}


def write(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="project root (docs/ is created inside it)")
    parser.add_argument("--minimal", action="store_true",
                        help="lighter structure for small projects")
    parser.add_argument("--with-mobile", action="store_true",
                        help="include 12-mobile (skipped by default)")
    parser.add_argument("--no-changelog", action="store_true",
                        help="skip docs/changelog/ per-change entries folder")
    parser.add_argument("--force", action="store_true",
                        help="overwrite existing files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        print(f"error: target {target} does not exist", file=sys.stderr)
        return 1

    docs = target / "docs"
    created = 0

    for name, content in ROOT_FILES.items():
        if args.no_changelog and name.startswith("changelog/"):
            continue
        if write(docs / name, content, args.force):
            created += 1

    if args.minimal:
        sections = MINIMAL_SECTIONS
    else:
        sections = [s for s in FULL_SECTIONS
                    if s != "12-mobile" or args.with_mobile]

    for section in sections:
        title = SECTION_TITLES.get(section, section)
        readme = f"# {title.split(' — ')[0]}\n\n{title}\n"
        if write(docs / section / "README.md", readme, args.force):
            created += 1

    templates_src = SKILL_ROOT / "templates"
    templates_dst = docs / "templates"
    templates_dst.mkdir(parents=True, exist_ok=True)
    for tpl in sorted(templates_src.glob("*.md")):
        dst = templates_dst / tpl.name
        if not dst.exists() or args.force:
            shutil.copy2(tpl, dst)
            created += 1

    print(f"DocOS structure ready at {docs} ({created} files created)")
    print("Next: fill in AI_INDEX.md and 01-product/vision.md"
          if not args.minimal else "Next: fill in AI_INDEX.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
