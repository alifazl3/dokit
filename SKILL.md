---
name: dokit
description: >-
  Apply DocOS — a comprehensive documentation operating system for software
  projects. Use this skill whenever the user asks to create, structure,
  update, review, or validate project documentation of any kind: setting up a
  docs/ folder, writing an ADR (architecture decision record), documenting a
  feature, entity, service, API, database table, or event, writing runbooks,
  playbooks, scenarios, release notes, glossaries, onboarding docs, or an
  AI_INDEX for AI agents. Also use it when the user mentions "dokit" or
  "DocOS" by name, when scaffolding a new project that needs documentation,
  and when finishing a feature or change — DocOS defines the documentation
  Definition of Done that every significant change must satisfy. When the
  user runs "/dokit upgrade" or asks to re-check, migrate, or upgrade
  existing docs after a skill/standard update, follow the "Upgrading
  existing docs" workflow.
---

# dokit — compatibility shim

The skill now lives in [skills/dokit/SKILL.md](skills/dokit/SKILL.md) (the
repository doubles as a Claude Code plugin marketplace). Read that file and
follow it exactly; every relative path in it — `references/`, `templates/`,
`scripts/`, `hooks/` — resolves next to that file, i.e. inside
`skills/dokit/`.

For new installs prefer the plugin route:

```
/plugin marketplace add alifazl3/dokit
/plugin install dokit@dokit
```
