# استاندارد جامع مستندسازی پروژه‌ها

## 1. مقدمه

این سند یک چارچوب جامع برای مستندسازی پروژه‌های نرم‌افزاری ارائه می‌دهد. هدف آن ایجاد یک ساختار یکپارچه، قابل نگهداری و قابل استفاده برای توسعه‌دهندگان، تیم محصول، تیم عملیات، مدیران فنی و عامل‌های هوش مصنوعی است.

این چارچوب صرفاً یک ساختار پوشه‌بندی نیست، بلکه یک سیستم عملیاتی برای تولید، نگهداری، مرور، اعتبارسنجی و استفاده از مستندات پروژه محسوب می‌شود.

در این سند، از عنوان زیر برای اشاره به این سیستم استفاده می‌شود:

**Documentation Operating System — DocOS**

هر پروژه باید DocOS را به‌عنوان مرجع اصلی دانش پروژه در کنار کد منبع نگهداری کند.

---

## 2. اهداف سیستم

اهداف اصلی این استاندارد عبارت‌اند از:

* ایجاد یک ساختار مستندات یکسان در تمام پروژه‌ها
* جلوگیری از پراکندگی اطلاعات در Issueها، پیام‌ها، فایل‌ها و ابزارهای مختلف
* کاهش وابستگی دانش پروژه به افراد
* ساده‌سازی ورود توسعه‌دهندگان جدید
* ثبت تصمیمات فنی و معماری
* نگهداری مستندات محصول و کسب‌وکار در کنار مستندات فنی
* ایجاد ارتباط میان Featureها، APIها، Entityها، تست‌ها و عملیات
* فراهم‌کردن Context دقیق برای AI Agentها
* امکان اعتبارسنجی مستندات در CI/CD
* حفظ تاریخچه تغییرات پروژه
* کاهش زمان تحلیل، توسعه، تست و رفع خطا

---

## 3. اصول بنیادین

### 3.1 مستندات بخشی از محصول هستند

مستندات نباید خروجی جانبی یا اختیاری توسعه در نظر گرفته شوند. هر تغییر مهم در سیستم باید همراه با تغییر مستندات مربوطه انجام شود.

### 3.2 مستندات در کنار کد نگهداری می‌شوند

مستندات فنی پروژه باید در همان Repository کد قرار داشته باشند تا:

* همراه کد Version شوند
* در Code Review بررسی شوند
* با Branch و Release هماهنگ باشند
* در CI اعتبارسنجی شوند

### 3.3 یک منبع حقیقت وجود دارد

برای هر موضوع باید یک مرجع اصلی یا **Single Source of Truth** مشخص باشد.

برای مثال:

* قرارداد API در OpenAPI
* تصمیمات معماری در ADR
* ساختار دامنه در Domain Documentation
* فرآیند استقرار در Runbook
* رفتار Feature در Feature Documentation

اطلاعات نباید به‌صورت ناسازگار در چند محل تکرار شوند.

### 3.4 هر مستند باید مالک داشته باشد

هر بخش از مستندات باید دارای Owner مشخص باشد. مالک مسئول موارد زیر است:

* صحت محتوا
* به‌روزرسانی
* پاسخ‌گویی به ابهامات
* تأیید تغییرات مهم

### 3.5 هر مستند باید قابل ردیابی باشد

مستندات باید تا حد امکان به عناصر مرتبط لینک شوند:

* Issue
* Epic
* Merge Request
* Commit
* API
* Entity
* Test
* Dashboard
* Runbook
* ADR
* Release

### 3.6 مستندات باید برای انسان و AI قابل استفاده باشند

ساختار فایل‌ها، عنوان‌ها، لینک‌ها و Metadata باید به‌گونه‌ای باشد که هم انسان و هم AI Agent بتوانند مسیر درست اطلاعات را پیدا کنند.

---

## 4. محدوده استفاده

این استاندارد برای پروژه‌های زیر قابل استفاده است:

* Backend
* Frontend
* Mobile
* Monorepo
* Microservice
* API Platform
* Infrastructure
* DevOps
* AI System
* Internal Tool
* SaaS
* Marketplace
* E-commerce
* Data Platform

پروژه‌های کوچک می‌توانند نسخه سبک‌تر ساختار را پیاده‌سازی کنند، اما اصول اصلی باید حفظ شوند.

---

## 5. ساختار اصلی مستندات

ساختار پیشنهادی برای هر پروژه:

```text
docs/
├── README.md
├── INDEX.md
├── AI_INDEX.md
├── OWNERS.md
├── GLOSSARY.md
├── ROADMAP.md
├── CHANGELOG.md
│
├── 00-governance/
├── 01-product/
├── 02-business/
├── 03-requirements/
├── 04-domain/
├── 05-architecture/
├── 06-api/
├── 07-services/
├── 08-database/
├── 09-events/
├── 10-security/
├── 11-frontend/
├── 12-mobile/
├── 13-ai/
├── 14-testing/
├── 15-devops/
├── 16-observability/
├── 17-operations/
├── 18-playbooks/
├── 19-decisions/
├── 20-features/
├── 21-releases/
├── 22-scenarios/
├── 23-runbooks/
├── 24-reference/
└── templates/
```

شماره‌گذاری پوشه‌ها باعث می‌شود ترتیب منطقی مستندات در File Explorer، GitLab و ابزارهای مستندسازی حفظ شود.

---

# بخش اول: فایل‌های اصلی

## 6. فایل `README.md`

این فایل نقطه شروع مستندات پروژه است.

محتوای پیشنهادی:

* معرفی کوتاه پروژه
* هدف پروژه
* معماری کلی
* لینک به فهرست مستندات
* نحوه شروع توسعه
* لینک به API
* لینک به Runbookهای مهم
* لینک به محیط‌ها
* مالک پروژه

نمونه:

```md
# Project Documentation

این پوشه مرجع اصلی مستندات پروژه است.

## Start Here

- [Documentation Index](./INDEX.md)
- [Architecture Overview](./05-architecture/overview.md)
- [Developer Workflow](./00-governance/developer-workflow.md)
- [API Documentation](./06-api/README.md)
- [Operations](./17-operations/README.md)
```

---

## 7. فایل `INDEX.md`

این فایل فهرست کامل مستندات است و باید مسیر ورود انسان به سیستم باشد.

وظایف آن:

* معرفی بخش‌های اصلی
* لینک به اسناد مهم
* مشخص‌کردن وضعیت بخش‌ها
* هدایت اعضای جدید تیم
* جلوگیری از گم‌شدن فایل‌ها

نمونه:

```md
# Documentation Index

## Product
- Vision
- Roadmap
- Personas

## Architecture
- System Overview
- Deployment Architecture
- Data Flow

## Development
- Developer Workflow
- Coding Standards
- Testing Strategy

## Operations
- Deployment
- Rollback
- Backup and Restore
```

---

## 8. فایل `AI_INDEX.md`

این فایل مخصوص AI Agentها و ابزارهای اتوماسیون است.

هدف آن ارائه یک نقشه کوتاه و دقیق از پروژه است تا Agent مجبور نباشد همه فایل‌ها را از ابتدا بررسی کند.

محتوای پیشنهادی:

* Context کلی پروژه
* Domainهای اصلی
* Serviceها
* مسیر فایل‌های مهم
* Dependencyهای اصلی
* قوانین تغییر کد
* قوانین تغییر مستندات
* محل تست‌ها
* دستورات Build و Test
* محدودیت‌های پروژه

نمونه:

```md
# AI Project Index

## Project Context

این پروژه یک پلتفرم Marketplace است.

## Main Domains

- Product
- Seller
- Channel
- Media
- Payment

## Important Paths

- API Contract: `docs/06-api/openapi.yaml`
- Domain Docs: `docs/04-domain/`
- Feature Docs: `docs/20-features/`
- Runbooks: `docs/23-runbooks/`
- Tests: `tests/`

## Required Checks

Before completing a change:

1. Update related feature documentation.
2. Update OpenAPI when API behavior changes.
3. Add or update tests.
4. Add an ADR when architecture changes.
```

---

## 9. فایل `OWNERS.md`

این فایل مالکیت مستندات را مشخص می‌کند.

نمونه:

```md
# Documentation Owners

| Area | Owner | Backup |
|---|---|---|
| Architecture | Platform Team | CTO |
| API | Backend Team | Tech Lead |
| Frontend | Frontend Team | Product Team |
| Operations | DevOps Team | Backend Team |
| Security | Security Lead | CTO |
```

در صورت استفاده از GitLab یا GitHub، این ساختار می‌تواند با `CODEOWNERS` هماهنگ شود.

---

## 10. فایل `GLOSSARY.md`

این فایل واژه‌ها، اصطلاحات و نام‌های داخلی پروژه را تعریف می‌کند.

نمونه:

```md
# Glossary

## Seller

کاربری که محصولات خود را در پلتفرم مدیریت و منتشر می‌کند.

## Channel

یک مسیر یا ویترین فروش که محصولات Seller در آن نمایش داده می‌شوند.

## Provider Product

محصول اصلی ثبت‌شده توسط Provider که Seller می‌تواند از آن Draft ایجاد کند.
```

هر واژه باید فقط یک تعریف رسمی داشته باشد.

---

## 11. فایل `CHANGELOG.md`

این فایل تغییرات مهم مستندات و سیستم را ثبت می‌کند.

نمونه:

```md
# Changelog

## Unreleased

### Added
- Media local storage documentation

### Changed
- Product creation flow

### Deprecated
- Legacy upload API
```

برای تغییرات Featureمحور می‌توان علاوه بر این فایل از پوشه `21-releases` نیز استفاده کرد.

---

# بخش دوم: حاکمیت مستندات

## 12. پوشه `00-governance`

این پوشه قوانین مدیریت مستندات و توسعه پروژه را نگهداری می‌کند.

```text
00-governance/
├── README.md
├── documentation-standard.md
├── naming-conventions.md
├── folder-conventions.md
├── markdown-style.md
├── ownership.md
├── review-process.md
├── versioning.md
├── deprecation-policy.md
└── developer-workflow.md
```

### محتوای اصلی

#### `documentation-standard.md`

قوانین کلی نوشتن و نگهداری مستندات.

#### `naming-conventions.md`

قواعد نام‌گذاری:

* فایل‌ها
* پوشه‌ها
* APIها
* Eventها
* Entityها
* Featureها
* ADRها

#### `review-process.md`

توضیح می‌دهد چه تغییراتی نیاز به Review دارند و چه کسانی باید آن‌ها را تأیید کنند.

#### `deprecation-policy.md`

قوانین Deprecatedکردن API، Feature، Event یا مستند.

---

# بخش سوم: محصول و کسب‌وکار

## 13. پوشه `01-product`

این بخش Context محصول را نگهداری می‌کند.

```text
01-product/
├── README.md
├── vision.md
├── mission.md
├── goals.md
├── roadmap.md
├── personas.md
├── user-journeys.md
├── success-metrics.md
├── constraints.md
└── product-principles.md
```

### `vision.md`

باید پاسخ دهد:

* پروژه چه مشکلی را حل می‌کند؟
* مخاطب اصلی چه کسی است؟
* ارزش اصلی محصول چیست؟
* محصول در آینده به چه سمتی می‌رود؟

### `personas.md`

برای هر Persona:

* نقش
* هدف
* نیاز
* مشکل
* محدودیت
* رفتار مورد انتظار

### `success-metrics.md`

معیارهای موفقیت محصول:

* نرخ تبدیل
* نرخ نگهداری
* زمان انجام فرآیند
* خطای کاربر
* رضایت کاربر

---

## 14. پوشه `02-business`

```text
02-business/
├── README.md
├── business-model.md
├── pricing.md
├── stakeholders.md
├── business-rules.md
├── compliance.md
├── risks.md
└── assumptions.md
```

### `business-rules.md`

قواعدی که رفتار سیستم را از نظر کسب‌وکار تعیین می‌کنند.

مثال:

* Seller تنها می‌تواند محصولات متعلق به خود را ویرایش کند.
* سفارش پرداخت‌شده قابل حذف نیست.
* موجودی هنگام رزرو کاهش می‌یابد.
* Refund پس از تأیید مالی انجام می‌شود.

---

# بخش چهارم: نیازمندی‌ها

## 15. پوشه `03-requirements`

```text
03-requirements/
├── README.md
├── epics/
├── features/
├── stories/
├── acceptance-criteria/
├── non-functional/
└── traceability/
```

### نیازمندی‌های عملکردی

رفتارهایی که سیستم باید اجرا کند.

### نیازمندی‌های غیرعملکردی

شامل:

* Performance
* Security
* Availability
* Scalability
* Accessibility
* Maintainability
* Observability

### Traceability

هر Requirement باید به عناصر زیر قابل اتصال باشد:

* Feature
* Issue
* Test
* API
* Release

---

# بخش پنجم: دامنه

## 16. پوشه `04-domain`

این بخش برای مستندسازی Domain Model استفاده می‌شود.

```text
04-domain/
├── README.md
├── domain-overview.md
├── bounded-contexts/
├── entities/
├── aggregates/
├── value-objects/
├── domain-services/
├── domain-events/
├── invariants/
└── diagrams/
```

### Entity Documentation

برای هر Entity:

```text
entities/
└── product.md
```

ساختار پیشنهادی:

```md
# Product

## Purpose

نمایش یک محصول قابل فروش در سیستم.

## Fields

| Field | Type | Required | Description |
|---|---|---:|---|
| id | UUID | Yes | شناسه محصول |
| title | String | Yes | عنوان محصول |
| status | Enum | Yes | وضعیت محصول |

## Invariants

- عنوان نمی‌تواند خالی باشد.
- محصول حذف‌شده قابل انتشار نیست.

## Related Entities

- Seller
- Media
- Category
```

---

# بخش ششم: معماری

## 17. پوشه `05-architecture`

```text
05-architecture/
├── README.md
├── overview.md
├── system-context.md
├── container-view.md
├── component-view.md
├── deployment-view.md
├── data-flow.md
├── network.md
├── dependencies.md
├── constraints.md
├── quality-attributes.md
└── diagrams/
```

پیشنهاد می‌شود از مدل C4 برای دیاگرام‌ها استفاده شود:

* Context
* Container
* Component
* Code

### `overview.md`

باید شامل موارد زیر باشد:

* سبک معماری
* Componentهای اصلی
* Databaseها
* Queueها
* Serviceها
* ارتباطات خارجی
* نقاط حساس سیستم

---

# بخش هفتم: API

## 18. پوشه `06-api`

```text
06-api/
├── README.md
├── openapi.yaml
├── openapi.json
├── authentication.md
├── authorization.md
├── conventions.md
├── errors.md
├── pagination.md
├── filtering.md
├── sorting.md
├── idempotency.md
├── versioning.md
├── rate-limiting.md
├── examples/
└── contracts/
```

قرارداد OpenAPI باید مرجع اصلی API باشد.

مستندات API باید مشخص کنند:

* Request
* Response
* Error
* Authentication
* Authorization
* Validation
* Side Effect
* Idempotency
* Eventهای تولیدشده

---

# بخش هشتم: سرویس‌ها

## 19. پوشه `07-services`

برای هر Service یک پوشه مستقل ایجاد می‌شود.

```text
07-services/
├── auth/
├── product/
├── media/
├── payment/
└── notification/
```

ساختار هر سرویس:

```text
product/
├── README.md
├── responsibilities.md
├── architecture.md
├── api.md
├── data.md
├── events.md
├── dependencies.md
├── flows.md
├── configuration.md
├── failure-modes.md
└── operations.md
```

هر Service باید مسئولیت مشخص و مرز روشن داشته باشد.

---

# بخش نهم: داده و Database

## 20. پوشه `08-database`

```text
08-database/
├── README.md
├── architecture.md
├── erd/
├── schemas/
├── tables/
├── indexes/
├── migrations/
├── constraints/
├── queries/
├── performance/
├── retention.md
└── backup-policy.md
```

برای هر جدول:

* هدف
* ستون‌ها
* Constraintها
* Indexها
* Relationها
* حجم تقریبی
* Queryهای مهم
* Retention Policy

---

# بخش دهم: Eventها

## 21. پوشه `09-events`

```text
09-events/
├── README.md
├── event-catalog.md
├── conventions.md
├── schemas/
├── publishers/
├── subscribers/
├── sagas/
├── retries.md
├── dead-letter.md
└── ordering.md
```

برای هر Event باید ثبت شود:

* نام
* هدف
* Producer
* Consumer
* Schema
* Version
* Retry Policy
* Ordering Guarantee
* Idempotency Behavior

---

# بخش یازدهم: امنیت

## 22. پوشه `10-security`

```text
10-security/
├── README.md
├── security-model.md
├── authentication.md
├── authorization.md
├── roles-permissions.md
├── threat-model.md
├── secrets.md
├── encryption.md
├── data-classification.md
├── audit.md
├── vulnerability-management.md
└── incident-response.md
```

این بخش نباید شامل Secret واقعی باشد.

اطلاعات حساس باید فقط به محل امن نگهداری Secret ارجاع داده شوند.

---

# بخش دوازدهم: Frontend و Mobile

## 23. پوشه `11-frontend`

```text
11-frontend/
├── README.md
├── architecture.md
├── routing.md
├── state-management.md
├── design-system.md
├── components.md
├── forms.md
├── error-handling.md
├── accessibility.md
├── performance.md
├── testing.md
└── analytics.md
```

## 24. پوشه `12-mobile`

```text
12-mobile/
├── README.md
├── architecture.md
├── navigation.md
├── state-management.md
├── offline-mode.md
├── notifications.md
├── permissions.md
├── deep-links.md
├── releases.md
└── store-deployment.md
```

در صورت نبود Mobile، این پوشه می‌تواند حذف شود.

---

# بخش سیزدهم: هوش مصنوعی

## 25. پوشه `13-ai`

```text
13-ai/
├── README.md
├── ai-guidelines.md
├── agents/
├── prompts/
├── workflows/
├── tools/
├── models/
├── evaluation/
├── guardrails/
├── memory/
├── context/
├── datasets/
└── observability/
```

### Agent Documentation

برای هر Agent:

```text
agents/
└── backend-agent.md
```

ساختار:

```md
# Backend Agent

## Purpose

پیاده‌سازی تغییرات Backend بر اساس قراردادهای پروژه.

## Allowed Actions

- Read backend code
- Modify service layer
- Add tests
- Update API documentation

## Restricted Actions

- Modify production credentials
- Change architecture without ADR
- Remove tests without approval

## Required Context

- AI_INDEX.md
- Developer Workflow
- API Standards
- Testing Strategy
```

### Prompt Documentation

هر Prompt مهم باید شامل موارد زیر باشد:

* هدف
* Input
* Output
* Model
* Version
* Example
* Failure Modes
* Evaluation Criteria

---

# بخش چهاردهم: تست

## 26. پوشه `14-testing`

```text
14-testing/
├── README.md
├── strategy.md
├── test-pyramid.md
├── unit/
├── integration/
├── contract/
├── e2e/
├── performance/
├── security/
├── fixtures/
├── test-data.md
├── coverage.md
└── quality-gates.md
```

### `strategy.md`

باید مشخص کند:

* چه چیزی Unit Test می‌شود؟
* چه چیزی Integration Test می‌شود؟
* چه چیزی E2E Test می‌شود؟
* Mock کجا مجاز است؟
* حداقل Coverage چقدر است؟
* تست‌ها در چه مرحله‌ای اجرا می‌شوند؟

---

# بخش پانزدهم: DevOps

## 27. پوشه `15-devops`

```text
15-devops/
├── README.md
├── environments.md
├── docker.md
├── kubernetes.md
├── helm.md
├── terraform.md
├── ci-cd.md
├── branching.md
├── deployment-pipeline.md
├── configuration.md
└── secrets-management.md
```

---

# بخش شانزدهم: Observability

## 28. پوشه `16-observability`

```text
16-observability/
├── README.md
├── logging.md
├── metrics.md
├── tracing.md
├── dashboards.md
├── alerts.md
├── slo.md
├── sla.md
├── error-handling.md
└── correlation.md
```

باید مشخص شود:

* Logها کجا ذخیره می‌شوند؟
* Traceها چگونه تولید می‌شوند؟
* Metricهای اصلی چیست؟
* Alertها چه زمانی فعال می‌شوند؟
* Owner هر Alert چه کسی است؟

---

# بخش هفدهم: عملیات

## 29. پوشه `17-operations`

```text
17-operations/
├── README.md
├── deployment.md
├── rollback.md
├── backup.md
├── restore.md
├── maintenance.md
├── scaling.md
├── access-management.md
├── disaster-recovery.md
└── environment-management.md
```

این اسناد فرآیندهای عادی عملیاتی را توضیح می‌دهند.

---

# بخش هجدهم: Playbookها

## 30. پوشه `18-playbooks`

Playbook برای پاسخ به وضعیت‌های خاص استفاده می‌شود.

```text
18-playbooks/
├── database-down.md
├── redis-down.md
├── queue-backlog.md
├── payment-failure.md
├── media-storage-failure.md
├── high-latency.md
└── security-incident.md
```

ساختار Playbook:

```md
# Database Down

## Symptoms

- Connection errors
- Increased API failures
- Database health check is failing

## Immediate Actions

1. Check database instance.
2. Check connection pool.
3. Check disk usage.
4. Review recent deployments.

## Escalation

Contact Platform Team if outage exceeds 10 minutes.

## Recovery Validation

- Health checks pass
- Error rate returns to normal
- Write operations succeed
```

---

# بخش نوزدهم: تصمیمات معماری

## 31. پوشه `19-decisions`

تمام تصمیمات معماری مهم باید به‌صورت ADR ثبت شوند.

```text
19-decisions/
├── README.md
├── ADR-0001-use-postgresql.md
├── ADR-0002-use-kafka.md
└── ADR-0003-store-media-locally.md
```

ساختار ADR:

```md
# ADR-0001: Use PostgreSQL

## Status

Accepted

## Context

سیستم به یک Database رابطه‌ای با Transaction قوی نیاز دارد.

## Decision

PostgreSQL به‌عنوان Database اصلی انتخاب شد.

## Consequences

### Positive

- Transaction support
- Strong consistency
- Mature ecosystem

### Negative

- Horizontal scaling complexity
- Operational overhead
```

وضعیت‌های مجاز:

* Proposed
* Accepted
* Rejected
* Deprecated
* Superseded

---

# بخش بیستم: مستندات Feature

## 32. پوشه `20-features`

این پوشه مرکز اصلی مستندسازی قابلیت‌های سیستم است.

```text
20-features/
├── product-creation/
├── media-upload/
├── checkout/
├── stock-reservation/
└── refund/
```

ساختار هر Feature:

```text
feature-name/
├── README.md
├── requirements.md
├── business-rules.md
├── architecture.md
├── flow.md
├── api.md
├── database.md
├── events.md
├── security.md
├── testing.md
├── observability.md
├── deployment.md
├── known-issues.md
└── open-questions.md
```

### فایل `README.md` هر Feature

باید خلاصه کامل Feature را ارائه دهد:

```md
# Media Upload

## Purpose

امکان آپلود، پردازش و ذخیره فایل‌های رسانه‌ای.

## Actors

- Seller
- Admin
- Media Worker

## Main Flow

1. Client uploads a file.
2. API validates the file.
3. File is converted to WebP.
4. File is stored.
5. Media record is created.

## Related Documentation

- API
- Database
- Events
- Runbook
```

این ساختار باعث می‌شود تمام اطلاعات یک Feature در یک محل قابل دسترسی باشند.

---

# بخش بیست‌ویکم: Releaseها

## 33. پوشه `21-releases`

```text
21-releases/
├── unreleased.md
├── v1.0.0.md
├── v1.1.0.md
└── v2.0.0.md
```

هر Release باید شامل موارد زیر باشد:

* Featureهای جدید
* Bug Fixها
* Breaking Changeها
* Migrationها
* تغییرات Configuration
* Rollback Plan
* Known Issues

---

# بخش بیست‌ودوم: سناریوها

## 34. پوشه `22-scenarios`

سناریوها رفتار واقعی کاربران و سیستم را ثبت می‌کنند.

```text
22-scenarios/
├── seller-creates-product.md
├── customer-completes-checkout.md
├── admin-refunds-order.md
└── worker-processes-media.md
```

ساختار Scenario:

```md
# Seller Creates Product

## Actor

Seller

## Preconditions

- Seller is authenticated.
- Seller account is active.

## Main Flow

1. Seller opens product creation page.
2. Seller enters product information.
3. Seller uploads media.
4. Seller submits the form.
5. System validates and stores the product.

## Alternative Flows

- Invalid media
- Duplicate SKU
- Missing category

## Expected Result

A product draft is created.
```

---

# بخش بیست‌وسوم: Runbookها

## 35. پوشه `23-runbooks`

Runbook دستورالعمل دقیق انجام یک کار عملیاتی است.

```text
23-runbooks/
├── deploy-application.md
├── rollback-release.md
├── restore-database.md
├── rotate-api-key.md
├── add-kubernetes-node.md
└── migrate-media-storage.md
```

ساختار استاندارد:

```md
# Restore Database

## Purpose

بازیابی Database از Backup.

## Preconditions

- Backup file is available.
- Maintenance mode is enabled.
- Required permissions are granted.

## Procedure

1. Stop write traffic.
2. Verify backup integrity.
3. Restore database.
4. Run migrations.
5. Validate critical queries.
6. Re-enable traffic.

## Rollback

Restore the previous database snapshot.

## Validation

- Health check succeeds.
- Critical APIs respond correctly.
- Data consistency checks pass.
```

---

# بخش بیست‌وچهارم: مرجع

## 36. پوشه `24-reference`

```text
24-reference/
├── README.md
├── glossary.md
├── commands.md
├── http-status-codes.md
├── configuration-reference.md
├── environment-variables.md
├── useful-links.md
├── external-services.md
├── standards.md
└── rfcs.md
```

این بخش برای اطلاعات مرجعی استفاده می‌شود که ماهیت توضیحی یا عملیاتی دارند ولی متعلق به Feature خاصی نیستند.

---

# بخش بیست‌وپنجم: Templateها

## 37. پوشه `templates`

```text
templates/
├── feature-template.md
├── entity-template.md
├── service-template.md
├── api-template.md
├── adr-template.md
├── runbook-template.md
├── playbook-template.md
├── scenario-template.md
├── incident-template.md
├── release-template.md
└── architecture-template.md
```

Templateها باید استفاده از استاندارد را برای تیم ساده کنند.

---

# بخش بیست‌وششم: Metadata استاندارد

## 38. Front Matter

پیشنهاد می‌شود هر مستند مهم دارای Metadata باشد.

نمونه:

```yaml
---
title: Media Upload
status: active
owner: backend-team
reviewers:
  - platform-team
version: 1.2
last_reviewed: 2026-07-27
related_features:
  - product-management
related_services:
  - media-service
related_adrs:
  - ADR-0003
---
```

فیلدهای پیشنهادی:

* `title`
* `status`
* `owner`
* `reviewers`
* `version`
* `last_reviewed`
* `related_features`
* `related_services`
* `related_adrs`
* `related_issues`
* `deprecated_by`

---

# بخش بیست‌وهفتم: وضعیت مستندات

## 39. وضعیت‌های مجاز

هر مستند می‌تواند یکی از وضعیت‌های زیر را داشته باشد:

* `draft`
* `proposed`
* `active`
* `deprecated`
* `archived`
* `superseded`

مستند Deprecated باید جایگزین خود را مشخص کند.

نمونه:

```yaml
status: deprecated
deprecated_by: docs/20-features/new-checkout/
```

---

# بخش بیست‌وهشتم: قواعد نام‌گذاری

## 40. فایل‌ها و پوشه‌ها

نام‌ها باید:

* انگلیسی باشند
* با حروف کوچک نوشته شوند
* از `kebab-case` استفاده کنند
* کوتاه و توصیفی باشند
* بدون فاصله باشند

درست:

```text
media-upload.md
stock-reservation/
developer-workflow.md
```

نادرست:

```text
Media Upload.md
media_upload.md
new-doc-final-v2.md
```

---

## 41. ADRها

```text
ADR-0001-use-postgresql.md
ADR-0002-add-event-bus.md
```

## 42. Releaseها

```text
v1.0.0.md
v1.2.0.md
```

## 43. Incidentها

```text
INC-2026-001-database-outage.md
```

---

# بخش بیست‌ونهم: چرخه عمر مستندات

## 44. ایجاد

مستند هنگام ایجاد Feature، Service، API یا تصمیم معماری ساخته می‌شود.

## 45. Review

مستند باید مانند کد Review شود.

Reviewer باید بررسی کند:

* صحت فنی
* سازگاری با سیستم
* کامل‌بودن لینک‌ها
* هم‌خوانی با کد
* رعایت Template

## 46. انتشار

مستند پس از Merge بخشی از نسخه رسمی پروژه محسوب می‌شود.

## 47. بازبینی دوره‌ای

مستندات مهم باید به‌صورت دوره‌ای بررسی شوند.

پیشنهاد:

* مستندات امنیتی: هر سه ماه
* Runbookها: هر سه تا شش ماه
* Architecture: هر شش ماه
* Product Vision: هر شش تا دوازده ماه
* API Contract: همراه هر تغییر

## 48. منسوخ‌سازی

مستند قدیمی نباید بدون توضیح حذف شود. ابتدا باید Deprecated شود و جایگزین آن مشخص گردد.

## 49. آرشیو

مستنداتی که دیگر در جریان فعلی پروژه کاربرد ندارند باید به بخش Archive منتقل شوند یا وضعیت `archived` دریافت کنند.

---

# بخش سی‌ام: ارتباط مستندات با توسعه

## 50. Definition of Done

هیچ Feature مهمی کامل محسوب نمی‌شود مگر اینکه موارد زیر انجام شده باشند:

* کد پیاده‌سازی شده باشد
* تست‌ها اضافه یا به‌روزرسانی شده باشند
* مستند Feature به‌روزرسانی شده باشد
* API Contract به‌روزرسانی شده باشد
* Migration مستند شده باشد
* Observability در نظر گرفته شده باشد
* Runbook لازم ایجاد شده باشد
* ADR لازم ثبت شده باشد
* Release Note نوشته شده باشد

---

## 51. تغییراتی که الزاماً نیاز به مستند دارند

موارد زیر باید همیشه همراه با تغییر مستندات باشند:

* API جدید
* تغییر API
* Entity جدید
* Migration جدید
* Service جدید
* Event جدید
* تغییر معماری
* تغییر Business Rule
* تغییر Deployment
* تغییر Configuration
* تغییر Security Model
* تغییر Permission
* تغییر مهم در User Flow

---

# بخش سی‌ویکم: اعتبارسنجی در CI/CD

## 52. بررسی‌های پیشنهادی

CI می‌تواند موارد زیر را بررسی کند:

* وجود `docs/README.md`
* وجود `docs/INDEX.md`
* وجود `docs/AI_INDEX.md`
* اعتبار لینک‌های داخلی
* فرمت صحیح Markdown
* فرمت صحیح Front Matter
* وجود Owner
* معتبر بودن Status
* همگام‌بودن OpenAPI
* وجود Release Note
* وجود ADR برای تغییرات معماری
* وجود Feature Doc برای Featureهای جدید

نمونه مراحل:

```text
docs-lint
docs-links-check
docs-schema-validation
openapi-validation
documentation-coverage
```

---

## 53. Documentation Coverage

می‌توان پوشش مستندات را مانند Test Coverage اندازه‌گیری کرد.

نمونه معیارها:

* درصد APIهای مستندشده
* درصد Entityهای مستندشده
* درصد Featureهای دارای سناریو
* درصد Serviceهای دارای Runbook
* درصد ADRهای دارای Status
* درصد مستندات دارای Owner
* درصد مستندات بازبینی‌شده در شش ماه اخیر

---

# بخش سی‌ودوم: Repository گلوبال استاندارد

## 54. ساخت Repository مرکزی

برای استفاده در تمام پروژه‌ها، یک Repository مستقل ایجاد می‌شود:

```text
project-documentation-standard/
├── README.md
├── standard/
├── templates/
├── schemas/
├── scripts/
├── examples/
├── ci/
└── changelog/
```

این Repository شامل موارد زیر است:

* ساختار استاندارد
* Templateها
* قوانین
* Validatorها
* نمونه پروژه
* CI Jobها
* Schemaهای Metadata
* Documentation Linter

---

## 55. روش استفاده در پروژه‌ها

### روش اول: Template Repository

هر پروژه جدید از Template اصلی ساخته شود.

مزیت:

* ساده
* مستقل
* بدون Dependency خارجی

عیب:

* به‌روزرسانی استاندارد در پروژه‌های قدیمی دستی است

### روش دوم: Package یا CLI

یک CLI مانند زیر ساخته شود:

```bash
docos init
docos validate
docos add feature media-upload
docos add adr use-postgresql
docos add runbook restore-database
docos sync
```

این روش برای استفاده سازمانی مناسب‌تر است.

### روش سوم: Git Submodule

```bash
git submodule add git@gitlab.com:company/project-documentation-standard.git .docos
```

این روش برای Templateها و Validatorها مناسب است، ولی مستندات اختصاصی پروژه باید داخل خود پروژه باقی بمانند.

---

# بخش سی‌وسوم: CLI پیشنهادی

## 56. دستورات

```bash
docos init
```

ساخت ساختار اولیه.

```bash
docos add feature checkout
```

ایجاد مستند Feature از Template.

```bash
docos add adr use-redis
```

ایجاد ADR جدید با شماره خودکار.

```bash
docos validate
```

اعتبارسنجی ساختار و Metadata.

```bash
docos index
```

تولید خودکار `INDEX.md`.

```bash
docos ai-index
```

تولید یا به‌روزرسانی `AI_INDEX.md`.

```bash
docos stale
```

نمایش مستندات قدیمی.

```bash
docos coverage
```

محاسبه Documentation Coverage.

---

# بخش سی‌وچهارم: نقش‌ها و مسئولیت‌ها

## 57. توسعه‌دهنده

* به‌روزرسانی مستندات مرتبط با تغییر
* ایجاد ADR در صورت نیاز
* اضافه‌کردن تست و سناریو
* اصلاح لینک‌های شکسته

## 58. Tech Lead

* Review مستندات فنی
* تأیید ADRها
* تعیین Owner
* کنترل سازگاری معماری

## 59. Product Manager

* نگهداری Vision، Roadmap و Requirements
* تأیید Business Ruleها
* به‌روزرسانی Acceptance Criteria

## 60. DevOps یا Platform Team

* نگهداری Runbookها
* مستندسازی Deployment
* مستندسازی Backup و Recovery
* نگهداری Observability Documentation

## 61. Security Owner

* نگهداری Threat Model
* بازبینی Permissionها
* مستندسازی Incident Response
* کنترل Data Classification

## 62. AI Agent

* مطالعه `AI_INDEX.md`
* رعایت AI Guidelines
* به‌روزرسانی مستندات مرتبط
* خودداری از تغییر معماری بدون ADR
* ارائه لینک به فایل‌های تغییرکرده

---

# بخش سی‌وپنجم: حداقل ساختار برای پروژه‌های کوچک

برای پروژه‌های کوچک می‌توان از نسخه ساده‌تر استفاده کرد:

```text
docs/
├── README.md
├── INDEX.md
├── AI_INDEX.md
├── architecture/
├── api/
├── domain/
├── features/
├── testing/
├── operations/
├── decisions/
├── runbooks/
└── templates/
```

با رشد پروژه، پوشه‌های بیشتر به‌تدریج اضافه می‌شوند.

---

# بخش سی‌وششم: ساختار پیشنهادی برای Monorepo

در Monorepo:

```text
docs/
├── README.md
├── INDEX.md
├── AI_INDEX.md
├── architecture/
├── product/
├── shared/
├── services/
│   ├── auth/
│   ├── product/
│   └── payment/
├── apps/
│   ├── web/
│   ├── admin/
│   └── mobile/
├── features/
├── operations/
└── decisions/
```

مستندات سراسری در ریشه قرار می‌گیرند و مستندات هر Service یا App در پوشه اختصاصی آن نگهداری می‌شوند.

---

# بخش سی‌وهفتم: ضدالگوها

## 63. فایل‌های بدون Owner

مستندی که Owner ندارد معمولاً به‌سرعت قدیمی می‌شود.

## 64. تکرار اطلاعات

کپی‌کردن قرارداد API در چند فایل باعث ناسازگاری می‌شود.

## 65. مستندات بدون لینک

مستندات جدا از Issue، Code و Test قابلیت ردیابی ندارند.

## 66. فایل‌های مبهم

نام‌هایی مانند موارد زیر نباید استفاده شوند:

```text
notes.md
new.md
final.md
final-v2.md
misc.md
```

## 67. مستندات فقط پس از اتمام پروژه

مستندات باید هم‌زمان با توسعه نوشته شوند، نه چند هفته بعد.

## 68. حذف تاریخچه تصمیمات

حتی تصمیم ردشده نیز می‌تواند ارزشمند باشد و نباید بدون دلیل حذف شود.

## 69. ذخیره Secret در مستندات

هیچ Token، Password، Private Key یا Credential نباید در Repository قرار گیرد.

---

# بخش سی‌وهشتم: خروجی نهایی سیستم

با اجرای این استاندارد، هر پروژه دارای موارد زیر خواهد بود:

* نقشه روشن محصول
* معماری قابل فهم
* مدل دامنه مستند
* قرارداد API معتبر
* مستندات Featureمحور
* تصمیمات معماری قابل ردیابی
* سناریوهای کاربری
* استراتژی تست
* Runbookهای عملیاتی
* Playbookهای Incident
* مستندات Observability
* راهنمای توسعه‌دهندگان
* Context استاندارد برای AI Agentها
* کنترل کیفیت مستندات در CI/CD

---

# 70. جمع‌بندی

DocOS یک استاندارد جامع برای مدیریت دانش پروژه است. این سیستم مستندات فنی، محصول، کسب‌وکار، امنیت، عملیات، تست، معماری و هوش مصنوعی را در یک ساختار یکپارچه قرار می‌دهد.

هدف DocOS تولید تعداد زیادی فایل نیست. هدف آن ایجاد مستنداتی است که:

* قابل اعتماد باشند
* مالک مشخص داشته باشند
* همراه کد تغییر کنند
* قابل جستجو باشند
* قابل اعتبارسنجی باشند
* برای انسان و AI قابل استفاده باشند
* تصمیمات و رفتار سیستم را دقیق توضیح دهند

در این مدل، مستندات از یک پوشه جانبی به یکی از اجزای اصلی مهندسی نرم‌افزار تبدیل می‌شوند.
