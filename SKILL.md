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
  Definition of Done that every significant change must satisfy.
---

# dokit — Documentation Operating System (DocOS)

DocOS treats documentation as part of the product: it lives next to the code,
is reviewed like code, has a single source of truth per topic, an owner per
document, and is usable by both humans and AI agents. The full normative
standard (in Persian) is in [references/standard-fa.md](references/standard-fa.md) —
read the relevant section when you need details beyond this file.

## Core rules (always apply)

1. **Single source of truth.** API contract lives in `docs/06-api/openapi.yaml`,
   architecture decisions in ADRs, domain shape in `04-domain/`, deployment in
   runbooks, feature behavior in `20-features/`. Never duplicate the same
   information into a second file — link to it.
2. **Every document has an owner** (in front matter and `OWNERS.md`).
3. **Docs change with the code, in the same merge request** — never "later".
4. **Naming:** English, lowercase, `kebab-case`, short and descriptive.
   ADRs: `ADR-0001-use-postgresql.md`. Releases: `v1.2.0.md`.
   Incidents: `INC-2026-001-database-outage.md`. Never `notes.md`, `final-v2.md`.
5. **No secrets in docs.** Reference the secret store, never the value.
6. **Deprecate, don't delete.** Old docs get `status: deprecated` +
   `deprecated_by: <path>` before removal; decision history is never erased.

## Initializing docs in a project

Run the bundled scaffolder instead of creating folders by hand:

```bash
python scripts/init_docs.py <target-project-root>          # full structure
python scripts/init_docs.py <target> --minimal             # small projects
python scripts/init_docs.py <target> --with-mobile         # include 12-mobile
```

It creates `docs/` with root files (`README.md`, `INDEX.md`, `AI_INDEX.md`,
`OWNERS.md`, `GLOSSARY.md`, `ROADMAP.md`, `CHANGELOG.md`), the numbered
sections `00-governance` … `24-reference`, the `templates/` folder (copied
from this skill), and a starter `README.md` in each section. After running it,
fill in `AI_INDEX.md` and `01-product/vision.md` first — they anchor
everything else.

The full folder map and per-section file lists are in
[references/structure.md](references/structure.md); consult it when deciding
where a new document belongs.

## Creating a document

Copy the matching file from `templates/` and fill it in — do not invent your
own layout:

| Need | Template | Destination |
|---|---|---|
| Architecture decision | `adr-template.md` | `19-decisions/ADR-NNNN-<slug>.md` |
| Feature | `feature-template.md` | `20-features/<slug>/README.md` (+ sibling files) |
| Entity | `entity-template.md` | `04-domain/entities/<slug>.md` |
| Service | `service-template.md` | `07-services/<slug>/README.md` |
| API topic | `api-template.md` | `06-api/` |
| Runbook (how to do an op) | `runbook-template.md` | `23-runbooks/<slug>.md` |
| Playbook (incident response) | `playbook-template.md` | `18-playbooks/<slug>.md` |
| Scenario (user flow) | `scenario-template.md` | `22-scenarios/<slug>.md` |
| Release notes | `release-template.md` | `21-releases/vX.Y.Z.md` |
| Incident report | `incident-template.md` | `INC-YYYY-NNN-<slug>.md` |
| Architecture view | `architecture-template.md` | `05-architecture/` |

ADR numbers are sequential — check the highest existing number first.
ADR statuses: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded`.

Every important document starts with YAML front matter:

```yaml
---
title: Media Upload
status: active        # draft | proposed | active | deprecated | archived | superseded
owner: backend-team
version: 1.0
last_reviewed: 2026-08-04
related_features: []
related_adrs: []
---
```

After adding a document, add it to `docs/INDEX.md` (and to `AI_INDEX.md` if an
agent would need it).

## Definition of Done (enforce on every significant change)

A feature or change is NOT complete until, where applicable:

- feature doc in `20-features/` created or updated
- OpenAPI contract updated (any API change)
- new/changed entities documented in `04-domain/`
- migration documented in `08-database/`
- ADR recorded (any architecture change)
- runbook added/updated (any new operational procedure)
- release note added to `21-releases/`
- tests and scenarios updated

Changes that ALWAYS require a doc update: new/changed API, new entity, new
migration, new service, new event, architecture change, business-rule change,
deployment/configuration change, security-model or permission change, and any
significant user-flow change. When you finish such a change without touching
docs, that is a defect — fix it before reporting the work done.

## Changelog and release notes

Two files record change history, with different jobs — keep both current:

**`docs/CHANGELOG.md`** — the running log. Every significant merged change
adds one line under `## Unreleased`, grouped by category
(keep-a-changelog style):

```md
## Unreleased

### Added
- Cross-site job sharing rules

### Changed
- Publication approval flow now requires site-admin confirmation

### Deprecated
- Legacy /v1/jobs endpoint (use /v2/jobs; removal in v2.0.0)
```

Allowed categories: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`,
`Security`. Write entries for the reader, not the diff: name the behavior
that changed, not the files touched. A `Deprecated` entry names the
replacement and, when known, the removal version.

**`docs/21-releases/vX.Y.Z.md`** — one file per release, from
`release-template.md`. At release time, move the `Unreleased` items into a
new `## vX.Y.Z — <date>` heading in CHANGELOG.md, and write the release file
with what the changelog line can't carry: breaking changes with migration
paths, database migrations, configuration changes, a rollback plan, and
known issues. `21-releases/unreleased.md` may hold in-progress notes for the
next release.

Adding the changelog line is part of finishing the change — not a separate
task for later. If a merge is worth reviewing, it is worth a changelog line.

## Validating

```bash
python scripts/validate_docs.py <target-project-root>
```

Checks required root files, naming conventions, ADR filename format, front
matter status values, and broken relative links. Run it after any large docs
edit and in CI (`docs-lint` stage). Fix what it reports.

## Writing style

- Write documentation content in the project's working language (this
  standard's reference text is Persian; the docs themselves may be Persian,
  English, or German as the project dictates) — but file names, front matter
  keys, and statuses are always English.
- Explain *why*, not just *what* — especially in ADRs and business rules.
- Link related docs liberally; an unlinked document is invisible.
- Keep each document focused; if it covers two topics, split it.
