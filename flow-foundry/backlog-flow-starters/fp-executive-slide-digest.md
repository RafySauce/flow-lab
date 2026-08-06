---
id: fp-executive-slide-digest
title: "Flow Primer Brief — Executive Slide Digest"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
data-class: public
related:
  - "[[executive-slide-digest]]"
---

# Flow Primer Brief — Executive Slide Digest

> Intake path 4 for the flow-foundry, backfilled: this arrived as a bare
> conversation (a manager wanting exec-ready slide content pulled from Rovo
> without manual rewriting), not as a formal starter. Per `foundry-spec.md`
> §1 case 4 that is workable — the setup questionnaire is answered here
> rather than skipped, so the scaffold has a real intake record behind it.

## Purpose

Turn a management user's request about one or more in-flight initiatives into
content that is already shaped for an executive slide — status, outcome-framed
accomplishments, risks, next milestones — and a finished `.pptx`, so the
manager never has to hand-rewrite a ticket dump into slide language. It
recurs on whatever cadence the manager's own steering/review meetings run on
(commonly weekly or monthly per initiative, or ahead of a portfolio review).

Unlike `accomplishments-digest` (its closest analog — Jira/Confluence gather,
draft, human review), this flow is a **single pipeline**, not a digest-plus-
companion-finisher pair: it goes end-to-end to the finished deck in one
flowspace. That was an explicit operator call during brainstorming, made to
keep one thing to maintain rather than two flows that always run together in
practice.

## Trigger and cadence

**Trigger:** a manager asks Rovo for exec-ready status on a named initiative
(single-initiative scope) or a set of initiatives (portfolio-rollup scope),
ahead of a review, steering meeting, or ad hoc executive ask.

**Cadence:** run-on-demand, not fixed — a manager may run this weekly for a
program in active steering, or once ahead of a single meeting. The flow is
cadence-neutral; nothing in it assumes a specific interval.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Frame | Manager states scope (single initiative vs. portfolio rollup), which initiative(s)/keywords/epics, audience, time period, and any explicit ask/decision needed from the exec | heavy |
| 2 | Gather | Rovo's native Jira (and Confluence, where relevant) search, keyed off Stage 1's keywords/epic names — status, recent activity, open blockers, upcoming due dates. Deliberately not a structured ingest pipeline (see Layer-3 inventory) | light |
| 3 | Draft | Synthesize gathered material into the house exec-slide content shape — one slide's content for single-initiative scope, a deck outline for portfolio scope | light |
| 4 | Align & Publish | Manager's own edit/approval pass against Stage 1's framing — the content-correctness gate (RAG call, framing, asks) before any file is generated | heavy |
| 5 | Stylize to .pptx | Apply house PPT template/branding to the approved content and produce the `.pptx`; fall back to a clean minimal deck and flag the gap if no house template exists | light |
| 6 | Final Review & Share | Manager checks the generated deck reads correctly and shares it. Terminal artifact | heavy |

This stage sketch deliberately carries **two** heavy gates rather than the
strict U-curve's single first/last pair: Stage 4 checks content correctness,
Stage 6 checks that stylizing didn't distort or drop anything from the
approved content. `accomplishments-digest` gets the same two checks by
splitting them across two flowspaces (digest's Stage 5, finisher's Stage 3);
this flow keeps both checks but folds them into one pipeline instead.

## Data profile

Jira/Confluence work-item content (summaries, descriptions, statuses, due
dates) and, in Stage 1, the manager's own framing of what the exec needs to
hear. No customer or credential-bearing content is expected by default, but
nothing in this design assumes a specific tenant's field configuration, so
the whole flow runs at `data-class: internal` in an instance. This public
design copy is `public` by construction — method only, no real work-item
content.

Stage-specific boundaries:

- **Stage 2** is a read-only search; assignee names may surface incidentally
  in returned work items but are not the point of the query and should not be
  carried into slide content unless the manager's framing calls for them.
- **No stage writes to Jira or Confluence.** Read-only for the whole flow.

## Layer-3 inventory

**Existing skills to reference:** none directly reused as a Layer-3 pointer
— see the deliberate non-reuse note below for why.

**Existing skills deliberately *not* reused:**

- `jira-portfolio-ingest` — considered for Stage 2. Rejected: it is
  portfolio-shaped (field-availability reports, completion denominators,
  ART-board connected-space discovery) built for a rationalization cycle
  across a whole project/space. A keyword-scoped status pull for one or a
  few named initiatives doesn't need that machinery, and narrowing its JQL
  filter to fit would mean carrying reporting overhead this flow has no use
  for.
- `jira-accomplishments-gatherer` — considered for Stage 2. Rejected:
  person-scoped (one engineer's own closed work for a review period), not
  initiative-scoped. Wrong unit of analysis.
- `confluence-contribution-gatherer` — considered for Stage 3/2. Rejected:
  scoped to one person's authored contributions, not an initiative's
  supporting docs.

Stage 2 instead uses the invoking engine's own native Jira/Confluence search
capability directly, keyed off Stage 1's keywords/epic names — inline logic,
not a dedicated skill. Building a purpose-specific gatherer skill here would
over-fit a search that native Rovo search already does; if a real recurring
gap in that native search surfaces at instantiation (e.g., a specific query
shape a manager always has to repeat by hand), that is a candidate for a
*future*, narrowly-scoped skill-primer-brief — not assumed here.

**Suspected gaps — two candidate skill-primer-briefs** (filed alongside this
brief):

| Candidate | Capability |
|---|---|
| `sp-executive-slide-drafter` | Synthesize Stage 2's gathered material plus Stage 1's framing into the house exec-slide content shape, including the RAG call |
| `sp-executive-slide-pptx-stylizer` | Apply house PPT branding to Stage 4's approved content and produce the `.pptx`, falling back to a minimal default and flagging a missing template |

**Reference material this flowspace must carry** (Layer-3 stable rule, not a
skill — authored when this flowspace is scaffolded):

An `executive-slide-shape.md` house content-shape template, modeled on
`accomplishments-digest/reference/accomplishments-document-shape.md`, defining
per-initiative slide content:

- **Title** — initiative name
- **Status** — RAG (Red/Amber/Green) + one-line why
- **Headline** — one sentence, business-outcome framed, never ticket-framed
- **Key accomplishments this period** — 2–4 outcome-first bullets
- **Risks / Blockers** — 0–3 bullets; omit the section entirely if none (a
  visible empty section reads worse than no section — same rule the
  accomplishments shape uses)
- **Upcoming milestones** — 1–3 bullets with dates
- **Ask** (optional) — what the exec needs to know, decide, or unblock

For portfolio-rollup scope: a title/agenda slide, one section per initiative
in the shape above, and an optional closing slide rolling up risks/asks
across initiatives.

## Source-repo

- **Source-repo:** the operator's internal GitLab instance repo,
  `flowspaces/executive-slide-digest/` — set at instantiation, sole source of
  truth for the instance.
- **External systems read:** Jira (primary), Confluence (secondary, where
  relevant) — read-only, via the engine's native search capability. No writes
  to any external system at any stage.

## Open questions

Surfaced for the operator rather than silently decided during setup:

1. **Whether Stage 2's native search needs any structure at all**, or should
   stay fully ad hoc per run. If managers repeatedly need the same query
   shape across runs, that recurring pattern — not this brief — is the
   trigger for a future dedicated gatherer skill.
2. **Whether a house PPT template exists yet.** Stage 5's stylizer skill
   (`sp-executive-slide-pptx-stylizer`) is designed to fall back to a clean
   minimal deck and flag the gap if not; sourcing a real house template is an
   instantiation-time task, not assumed here.
3. **Portfolio-rollup slide count ceiling.** Nothing in this design caps how
   many initiatives one portfolio-rollup run can cover; a very large rollup
   may need a stated ceiling (with overflow handled as a second deck) —
   deferred until a real instance hits the case.
4. **Whether Confluence gather is worth keeping as a first-class Stage 2
   input or should be dropped to a documented future extension** if it turns
   out most initiatives' exec-relevant status lives entirely in Jira.
