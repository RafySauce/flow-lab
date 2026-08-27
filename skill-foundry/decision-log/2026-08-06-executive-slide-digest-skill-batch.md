---
id: decision-2026-08-06-executive-slide-digest-skill-batch
title: "Decision Log — Executive Slide Digest Skill Batch Build"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
data-class: public
related:
  - "[[sp-executive-slide-drafter]]"
  - "[[sp-executive-slide-pptx-stylizer]]"
  - "[[executive-slide-digest]]"
---

# Decision Log — 2026-08-06 — Executive Slide Digest Skill Batch Build

**What was decided:** author both backlog starters filed from the
`executive-slide-digest` flowspace's Layer-3 scaffold triage —
`executive-slide-drafter` and `executive-slide-pptx-stylizer` — each as an
engine-neutral `SKILL.md` plus adapters, staged in `review-skills/` at
`truth-level: to-review`. **By whom:** agent, on direct operator instruction
("let's complete the build out of the flowspace designed to take jira
information and put it into .ppt"). **What it affects:** two new folders
under `review-skills/`; the two `sp-*` primer briefs stay unchanged in the
backlog as intake records; the flowspace's `HUB.md` Known-gaps table updated
to reflect built (not promoted) status. Nothing promoted, nothing moved to
`../../produced-skills/`, nothing deployed to an engine.

**Intake path:** clean for both — each arrives from an `sp-*` primer brief
already sitting `to-review` in the backlog, filed in the same prior session
that backfilled `fp-executive-slide-digest.md` (per that brief's own
intake-path note, case 4 of `foundry-spec.md` §1). No foreign material, no
vetting checklist run.

**Both adapters for the drafter; Copilot only for the stylizer — the
`accomplishments-digest` precedent applies unchanged.** `executive-slide-
drafter` is pure synthesis from two already-gathered inputs, so no
Atlassian-native-access constraint narrows its engine assignment — both
adapters built, matching `accomplishments-drafter`'s own reasoning.
`executive-slide-pptx-stylizer` produces a `.pptx` file, which — like
`.docx` generation in `accomplishments-docx-stylizer` — has no Rovo-native
point of use; Copilot only, no Rovo adapter, for the same reason.

## Notable calls

- **Two content-shape reference docs authored alongside the skills, not
  deferred to instantiation.** `executive-slide-shape.md` (the drafter's
  target shape) already existed as a scaffold-time deliverable per the
  primer brief's own instruction. `pptx-minimal-default-style.md` (the
  stylizer's fallback when no house template exists) is new this session —
  directly modeled on `accomplishments-docx-finisher/reference/docx-
  minimal-default-style.md`, adapted for slide-shaped content: RAG-colored
  status chips instead of prose status, 16:9 layout rules instead of page
  margins. Both are `reference/` material inside the flowspace, not
  something either `SKILL.md` invents inline, so a future instance can swap
  the fallback for real house branding without touching either skill's spec.
- **Boundary/collision first pass** against the twenty-seven produced
  skills, plus the two other skills currently staged in `review-skills/`
  (`export-log`, `process-decomposition` — no overlap, different domains
  entirely): the closest pairs are `executive-slide-drafter` ↔
  `accomplishments-drafter` (both synthesize a framing brief plus gathered
  material into a house document shape) and `executive-slide-pptx-stylizer`
  ↔ `accomplishments-docx-stylizer` (both apply house branding to
  already-approved content and fall back to a documented minimal default).
  Both pairs are disjoint on the same two axes every time: **audience**
  (executive status vs. individual performance-review record) and **unit of
  analysis** (an initiative vs. one person's work). Each new spec's own
  "What this skill is not" section names its closest-pair sibling by id, and
  each existing sibling's spec was checked and needs no edit — neither
  existing spec claims territory broad enough to already cover initiative-
  status drafting or `.pptx` output. No merge, split, or redraw needed.
  Formal collision check re-runs at the promotion gate; pre-run evidence in
  the companion entry,
  `2026-08-06-executive-slide-digest-skill-gate-prerun.md`.
- **No write path in either skill** — `executive-slide-drafter` is
  read/compose only (drafts text, does not publish); `executive-slide-pptx-
  stylizer` produces a file but writes to no external system. Neither
  skill's Rovo or Copilot adapter carries any permitted write action.

## What is still needed before an end-to-end run

1. **A house PowerPoint template asset**, if the operator wants branded
   output rather than the minimal default — an instantiation-time,
   employer-specific asset per the primer brief's open question 2.
   `pptx-minimal-default-style.md` makes this optional, not blocking.
2. **Stage 2's native-search behavior** is inline logic, not a skill; no
   build artifact resolves the primer brief's remaining open questions
   (search-shape structure, portfolio slide-count ceiling, Confluence
   first-class status) — all three stay deferred, per the flowspace's own
   Known gaps.
3. **Published Rovo agent(s) and Copilot file(s)** from the `adapters/`
   copies of record, plus synthetic/`public` content to test against.
   Promotion and deployment are the operator's, per `foundry-spec.md` §5.

**Next:** operator review per `foundry-spec.md` §5 — see the companion
gate-pre-run entry for what is already checked agent-side and what remains
open.
