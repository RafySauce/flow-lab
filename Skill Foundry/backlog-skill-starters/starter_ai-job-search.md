---
type: skill-starter
truth-level: claimed
status: living
generated-by: skill-foundry
source: external
captured: 2026-06-10
---

# Starter: ai-job-search (foreign material)

## Source
- Repo: https://github.com/MadsLorentzen/ai-job-search (MIT, master @ 2026-04-29, "refactor: fold /setup_docs into /setup as third onboarding path (#9)")
- Context article: https://www.linkedin.com/pulse/i-automated-my-job-search-made-process-more-human-mads-lorentzen-phd-38bje — **not fetched** (LinkedIn blocks automated access); README appears to summarize the same philosophy.
- Author: Mads Lorentzen (PhD), lone account; job-portal CLI tools credited to Mikkel Krogholm (mikkelkrogsholm/skills).
- Ingested by Cincinnatus, 2026-06-10, with directive: customize to house spec; consider sub-agent enhancements (e.g. nimble-driven job-link search).

## As-ingested intent (hypothesis)
A full job-application *framework* (not a single skill): profile-grounded job-fit
evaluation, drafter→reviewer CV/cover-letter pipeline (LaTeX), job-portal scraping
with dedupe + tracker, interview prep, salary benchmarking. The portal layer is
Danish-market-specific and explicitly designed to be swapped.

## What's actually in it (vetted read, full clone)
- 2 Claude skills: `job-application-assistant` (7 numbered reference files:
  candidate profile, behavioral profile, writing style, evaluation framework,
  CV templates, cover-letter templates, interview prep) and `job-scraper`
  (search → dedupe via seen_jobs.json + tracker CSV → quick-fit table).
- 4 slash commands: /setup (onboarding interview), /apply (drafter-reviewer,
  token-efficiency rules, mandatory compiled-PDF inspection), /expand, /reset.
- 4 Bun/TypeScript CLI scrapers for Danish portals (jobindex, jobnet, jobbank,
  jobdanmark) — pattern-demonstrators, not house-relevant as-is.
- LaTeX assets (moderncv CV, custom cover.cls + fonts), salary_lookup.py (BYO data).

## Vetting
- **Maintenance:** young repo (~6 wk since last commit), small footprint (1 star),
  but coherent and actively shaped via PRs. Acceptable for pattern-harvest;
  wouldn't take a runtime dependency on it.
- **Provenance:** clear, MIT, attribution chain intact (Krogholm CLIs credited).
- **Security read:** no malicious behavior; permissions allow bash(python/curl/bun)
  — normal for its design. **The real flag is privacy, not malice:** the framework
  centralizes deep PII (full CV, behavioral/PI assessment, motivations,
  deal-breakers) in plaintext and routes it through cloud LLM calls + web search.
  House normalization must take a deliberate data-sovereignty stance on the
  candidate-profile layer.
- **Quality:** good bones — drafter-reviewer separation, no-fabrication rules,
  verification checklist, dedupe discipline. Worth normalizing.

## Triage verdict
Foreign-skill-starter, **skill-worthy**, normalize path. Scoping decisions
(single skill vs. split, discovery engine, output format, profile residency)
confirmed with Cincinnatus 2026-06-10.

## Normalization status
Normalized 2026-06-10 as `job-search-partner` (one skill, two modes) — see
`cowork-skill-foundry/forge/job-search-partner/` (+ vault doc + .skill package)
at `truth-level: to-review`. Trace:
`cowork-skill-foundry/traces/2026-06-10-job-search-partner-trace.md`.
Awaiting review-bench.
