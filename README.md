# dokit

**DocOS — Documentation Operating System** packaged as a Claude Code skill.

DocOS is a comprehensive standard for software project documentation: a
numbered `docs/` taxonomy (governance, product, business, domain,
architecture, API, database, events, security, testing, DevOps,
observability, operations, playbooks, ADRs, features, releases, scenarios,
runbooks, reference), templates for every document type, naming conventions,
front matter metadata, lifecycle rules, and a documentation Definition of
Done that ties docs to code changes.

The full normative standard (Persian) lives in
[`references/standard-fa.md`](references/standard-fa.md).

## What's inside

```
dokit/
├── SKILL.md                  # the skill: rules Claude applies + workflow
├── references/
│   ├── standard-fa.md        # full DocOS standard (fa)
│   └── structure.md          # folder map quick reference
├── templates/                # ADR, feature, entity, service, api, runbook,
│                             # playbook, scenario, incident, release, architecture
└── scripts/
    ├── init_docs.py          # scaffold docs/ in a project
    └── validate_docs.py      # lint the docs/ tree (CI-friendly)
```

## Install as a Claude Code skill

```bash
# per project
git clone git@github.com:alifazl3/dokit.git .claude/skills/dokit

# or globally
git clone git@github.com:alifazl3/dokit.git ~/.claude/skills/dokit
```

Then in any session: ask Claude to document something, or invoke `/dokit`.

## Use the scripts directly (no Claude needed)

```bash
python scripts/init_docs.py /path/to/project            # full structure
python scripts/init_docs.py /path/to/project --minimal  # small projects
python scripts/validate_docs.py /path/to/project        # lint (exit 1 on errors)
```

`validate_docs.py` is CI-friendly — add it as a `docs-lint` job.
