# DocOS folder map

Quick reference for where documents live. Full details per section are in
[standard-fa.md](standard-fa.md) (section numbers noted below).

```text
docs/
├── README.md            # entry point: what the project is, start-here links
├── INDEX.md             # human index of all docs
├── AI_INDEX.md          # AI-agent map: domains, key paths, build/test commands, change rules
├── OWNERS.md            # area → owner table (align with CODEOWNERS)
├── GLOSSARY.md          # one official definition per term
├── ROADMAP.md
├── CHANGELOG.md         # keep-a-changelog style (Unreleased/Added/Changed/Deprecated)
│
├── 00-governance/       # §12 — documentation-standard, naming-conventions,
│                        #        review-process, versioning, deprecation-policy,
│                        #        developer-workflow, markdown-style, ownership
├── 01-product/          # §13 — vision, mission, goals, roadmap, personas,
│                        #        user-journeys, success-metrics, constraints
├── 02-business/         # §14 — business-model, pricing, stakeholders,
│                        #        business-rules, compliance, risks, assumptions
├── 03-requirements/     # §15 — epics/, features/, stories/, acceptance-criteria/,
│                        #        non-functional/, traceability/
├── 04-domain/           # §16 — domain-overview, bounded-contexts/, entities/,
│                        #        aggregates/, value-objects/, domain-services/,
│                        #        domain-events/, invariants/, diagrams/
├── 05-architecture/     # §17 — overview, system-context, container-view,
│                        #        component-view, deployment-view, data-flow,
│                        #        network, dependencies, constraints,
│                        #        quality-attributes, diagrams/ (C4 model)
├── 06-api/              # §18 — openapi.yaml (SOURCE OF TRUTH), authentication,
│                        #        authorization, conventions, errors, pagination,
│                        #        filtering, sorting, idempotency, versioning,
│                        #        rate-limiting, examples/, contracts/
├── 07-services/         # §19 — one folder per service: README, responsibilities,
│                        #        architecture, api, data, events, dependencies,
│                        #        flows, configuration, failure-modes, operations
├── 08-database/         # §20 — architecture, erd/, schemas/, tables/, indexes/,
│                        #        migrations/, constraints/, queries/, performance/,
│                        #        retention, backup-policy
├── 09-events/           # §21 — event-catalog, conventions, schemas/, publishers/,
│                        #        subscribers/, sagas/, retries, dead-letter, ordering
├── 10-security/         # §22 — security-model, authn/authz, roles-permissions,
│                        #        threat-model, secrets (references only!), encryption,
│                        #        data-classification, audit, incident-response
├── 11-frontend/         # §23 — architecture, routing, state-management,
│                        #        design-system, components, forms, error-handling,
│                        #        accessibility, performance, testing, analytics
├── 12-mobile/           # §24 — omit when the project has no mobile app
├── 13-ai/               # §25 — ai-guidelines, agents/, prompts/, workflows/,
│                        #        tools/, models/, evaluation/, guardrails/,
│                        #        memory/, context/, datasets/, observability/
├── 14-testing/          # §26 — strategy, test-pyramid, unit/, integration/,
│                        #        contract/, e2e/, performance/, security/,
│                        #        fixtures/, test-data, coverage, quality-gates
├── 15-devops/           # §27 — environments, docker, kubernetes, helm, terraform,
│                        #        ci-cd, branching, deployment-pipeline,
│                        #        configuration, secrets-management
├── 16-observability/    # §28 — logging, metrics, tracing, dashboards, alerts,
│                        #        slo, sla, error-handling, correlation
├── 17-operations/       # §29 — deployment, rollback, backup, restore, maintenance,
│                        #        scaling, access-management, disaster-recovery
├── 18-playbooks/        # §30 — incident response per situation
│                        #        (database-down.md, high-latency.md, ...)
├── 19-decisions/        # §31 — ADR-NNNN-<slug>.md
├── 20-features/         # §32 — one folder per feature: README, requirements,
│                        #        business-rules, architecture, flow, api, database,
│                        #        events, security, testing, observability,
│                        #        deployment, known-issues, open-questions
├── 21-releases/         # §33 — unreleased.md, vX.Y.Z.md
├── 22-scenarios/        # §34 — real user/system flows: <actor>-<action>.md
├── 23-runbooks/         # §35 — step-by-step operational procedures
├── 24-reference/        # §36 — commands, env vars, external services, links, rfcs
└── templates/           # §37 — copied from this skill's templates/
```

## Minimal structure (small projects, §35 of intro / section 35)

```text
docs/
├── README.md  INDEX.md  AI_INDEX.md
├── architecture/  api/  domain/  features/  testing/
├── operations/  decisions/  runbooks/  templates/
```

Grow into the numbered structure as the project grows; principles stay the same.

## Monorepo note (§36)

Global docs live in the root `docs/`. Per-service/app docs folders should stay
thin and link back to the root — never copy content (single source of truth).

## Review cadence (§47)

- security docs: every 3 months
- runbooks: 3–6 months
- architecture: 6 months
- product vision: 6–12 months
- API contract: with every change
