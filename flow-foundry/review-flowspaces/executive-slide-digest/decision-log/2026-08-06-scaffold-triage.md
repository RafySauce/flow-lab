---
id: decision-2026-08-06-executive-slide-digest-scaffold-triage
title: "Decision Log — Executive Slide Digest Scaffold"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
data-class: public
related: ["[[fp-executive-slide-digest]]", "[[executive-slide-digest]]"]
---

# Decision Log — 2026-08-06 — Executive Slide Digest Scaffold

**What was decided:** scaffold the flowspace from `fp-executive-slide-digest.md`
— a flow-primer-brief already filed and crystallized in a prior session (its
own intake-path note records it as "Intake path 4 … backfilled" per
`foundry-spec.md` §1 case 4) — into the standard six-field-contract structure,
staged in `review-flowspaces/` at `truth-level: to-review`. **By whom:** agent,
on direct operator instruction naming this exact starter ("the flowspace
designed to take jira information and put it into .ppt"). **What it affects:**
new `HUB.md`, six stage `CONTEXT.md` files, and
`reference/executive-slide-shape.md`, all staged here; the primer brief itself
is untouched (it stays in `backlog-flow-starters/` as the intake record, per
`foundry-spec.md` §5).

## Scaffold decisions

1. **Stage count and names transcribed as-is from the brief's stage sketch** —
   Frame, Gather, Draft, Align & Publish, Stylize to .pptx, Final Review &
   Share — no restructuring. The brief's stage sketch was already a settled
   design call (including the operator's explicit choice to keep this a
   single pipeline rather than splitting a digest/finisher pair, unlike its
   closest analog `accomplishments-digest`); re-opening that shape here would
   violate the clean-path rule (§1 case 1 — "transcribe the decided intent
   into structure, don't re-open it").
2. **Two heavy gates, not one.** Stage 4 (content correctness) and Stage 6
   (post-stylize final check) both carry `heavy`, per the brief's explicit
   rationale — `accomplishments-digest` gets the same two checks by splitting
   them across two flowspaces; this one folds both into a single pipeline
   instead. Stated in `HUB.md`'s Run procedure so a future reviewer doesn't
   read it as an arbitrary U-curve deviation.
3. **Stage 2 (Gather) stays `Layer-3: inline`, not a skill reference.** The
   brief explicitly considered and rejected reusing `jira-portfolio-ingest`
   and `jira-accomplishments-gatherer` (wrong shape / wrong unit of analysis)
   and declined to draft a new gatherer skill, reasoning that a
   purpose-specific skill here would over-fit what native engine search
   already does. Carried into Stage 2's `CONTEXT.md` unchanged.
4. **Two Layer-3 gaps flagged at Stages 3 and 5 — briefs already existed.**
   `sp-executive-slide-drafter` and `sp-executive-slide-pptx-stylizer` were
   filed in the same prior session as the flow-primer-brief. This scaffold
   references both by id in the Stage table and `CONTEXT.md` Layer-3 lines,
   marked `to-review` because — per this session's own follow-on work — both
   were built and staged to `skill-foundry/review-skills/` immediately after
   this scaffold; see `skill-foundry/decision-log/2026-08-06-executive-slide-
   digest-skill-batch.md`. The diagram nodes for Stages 3 and 5 carry `gap`
   coloring per `references/flow-diagram-guide.md` (a stage's skill exists
   but isn't yet `verified`) — see `HUB.md`'s diagram note.
5. **`executive-slide-shape.md` authored now, per the brief's own Layer-3
   inventory instruction** ("reference material this flowspace must carry
   … authored when this flowspace is scaffolded"). Modeled directly on
   `accomplishments-digest/reference/accomplishments-document-shape.md`,
   adapted for the RAG-status/headline/risks/milestones/ask shape the brief
   specifies, with a portfolio-rollup variant folded in as its own section
   rather than a second file.

## Assumption (operator to confirm or amend)

- **Data-class stays `public` for this design copy**, per the brief's own
  data profile section — no real work-item content enters this repo; an
  instantiated copy runs at `internal` per `governance-and-audit.md` §2.
