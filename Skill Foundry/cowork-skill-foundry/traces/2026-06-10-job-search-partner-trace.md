---
type: trace
created: 2026-06-10
capability: foreign-intake-normalization
artifact: job-search-partner
---

# Trace: ai-job-search → job-search-partner (foreign intake, full pass)

## Input
Foreign-skill-starter: github.com/MadsLorentzen/ai-job-search (MIT) + LinkedIn
article pointer (unfetchable — LinkedIn blocks automation; proceeded on the repo,
which is self-documenting; noted in starter). Directive from Cincinnatus:
customize to house spec, consider sub-agent enhancements (nimble).

## Triage & vetting decisions
1. **Classified foreign, skill-worthy.** Not one skill but a framework: 2 skills,
   4 commands, 4 portal CLIs, LaTeX chain. Vetting: MIT, clean attribution chain,
   no malicious behavior, young-but-coherent repo. Verdict: harvest patterns,
   take no runtime dependency.
2. **The vetting flag was privacy, not security.** Source centralizes deep PII
   (CV, PI/DISC profile, deal-breakers) in plaintext through cloud calls. Surfaced
   to Cincinnatus as a scoping question rather than silently inherited.

## Scoping (4 branches put to Cincinnatus via multiple-choice; all answered)
- **Scope:** one skill, two modes (Scout/Apply) — collapsed source's 2 skills +
  4 commands. Rationale: single triggering surface, one voice, references carry depth.
- **Discovery:** Danish portal CLIs (useless here) → Nimble researcher sub-agent,
  WebSearch fallback. Portal-CLI pattern preserved as appendix, not wired.
- **Documents:** LaTeX → house docx/pdf skills. Kept the source's real insight
  (inspect the *rendered* output) translated out of TeX specifics.
- **Profile/PII:** rebuilt as two-person household contract (M1/F1, mirroring
  travel-planner). CV substance kept, deal-breakers kept (promoted to hard
  pass/fail gates), behavioral assessment demoted to optional self-assessment
  per Cincinnatus ("unsure about behavioral assessment"). Added privacy stance:
  PII never in web queries; deep profile authoring local-first.

## Harvested nearly intact (best of the foreign material)
Writing-style rules incl. the **interview backtrack test** (OK/flag/never
reframing taxonomy — the single best idea in the repo), five-dimension evaluation
framework, drafter-reviewer pattern with token-efficiency rules, verification
checklist discipline, no-fabrication rules, interview-prep framework,
latent-opportunity discovery concept.

## Dropped
LaTeX assets, salary_lookup.py (BYO-data, low value vs. live search), /expand and
/reset commands (workspace-management, not skill behavior), Danish portal CLIs.

## Lessons for Hermes
- Foreign frameworks ≠ foreign skills: intake may need a *decomposition* step
  before normalization; the four-branch scoping question-set (scope / engine /
  output / data residency) generalized well and could template.
- Second use of the M1/F1 standing-profile pattern — formalize as house contract
  when a third appears.
- Privacy-as-workflow (not just storage) entered the house style here.

## Status
Emitted at `truth-level: to-review`, execution-tier frontier, limits measured
(name 18, description 926, compatibility 263 — all under). Eval not yet run.
Awaiting Cincinnatus review at the bench.
