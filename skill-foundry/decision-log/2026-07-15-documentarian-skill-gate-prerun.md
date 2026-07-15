---
id: decision-2026-07-15-documentarian-skill-gate-prerun
title: "Decision Log — Documentarian Skill Batch: Five-Point Gate Pre-Run"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-15
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related:
  - "[[decision-2026-07-15-documentarian-skill-batch]]"
  - "[[sp-doc-evidence-gatherer]]"
  - "[[sp-doc-planner]]"
  - "[[sp-doc-drafter]]"
  - "[[sp-sad-diagram-maintainer]]"
  - "[[sp-doc-standards-validator]]"
  - "[[sp-confluence-page-commit]]"
  - "[[sp-doc-custodian]]"
---

# Decision Log — 2026-07-15 — Documentarian Skill Batch: Five-Point Gate Pre-Run

**What was decided:** run the skill-foundry §5 review gate agent-side
across the seven-skill batch and record the evidence here (gate item 5).
**By whom:** agent, same instruction as the batch-build entry. **What it
affects:** two specs received a pre-stage fix during the diagram-discipline
check (below); nothing is promoted, nothing moved to
`../../produced-skills/`, nothing deployed — those calls stay with the
operator.

## Scope limitation — read first

Gate item 2 demands a live test **on the target engine**. This session has
no Rovo or Copilot access, and — unlike the 2026-07-14 batch — no simulated
adapter invocations were run either: several of these skills' review
criteria hinge on interactive per-item human confirmations and platform
write responses (commit conflicts, partial link failures) that a synthetic
transcript exercises poorly. Gate item 2 therefore remains **fully open**
for the operator: at minimum one invocation per adapter on
`public`/synthetic data, judged against each spec's review criteria — the
seeded scenarios are already written into each spec's Review criteria
section. Diagram compilation was run for real: all seven Mermaid
`flowchart LR` diagrams were extracted and compiled locally with
`@mermaid-js/mermaid-cli` (headless Chromium, `--no-sandbox`); all seven
rendered to SVG without error. Confluence-macro rendering remains
unconfirmed (no tenant access), per the guide's fallback note.

## 1. Spec review — pass, two fixes applied before staging

All seven: purpose sharp; triggering intent names misfires; boundaries
explicit and mutually naming (drafter ↔ diagram-maintainer; evidence
gatherer ↔ accomplishments gatherers; validator ↔ workitem-validation;
commit ↔ jira-commit/custodian); review criteria transcribed from each
brief's Definition of done, checkable as written; frontmatter valid per
`provenance-spec.md` (rule 3 — `generated-by`/`generated-by-version`
paired; rule 6 — spec frontmatter `data-class: public` with the runtime
max of `internal` in each body's Data boundary section). Diagram-discipline
check (every node/edge ↔ a Method sentence) surfaced two mismatches, fixed
before staging: `doc-evidence-gatherer`'s confidential-content halt diamond
had its prose only in the Data boundary section — a guard sentence was
added to Method; `confluence-page-commit`'s declined-approval halt edge
lacked an explicit "no approval, no write" sentence in Method step 2 — added.

## 2. Live test on the target engine — OPEN (see scope limitation)

Not run, on-engine or simulated. The operator decides whether to require
on-engine runs before promotion or to accept a simulated pass first.

## 3. Trigger check — pass (static)

Each spec's fires-on was walked against its six siblings' and the thirteen
produced skills' fires-on lists: no phrase routes to two skills. The
closest pairs — "gather evidence" (engineer-accomplishments vs. doc-job
scope), "validate this" (work item vs. governed document), "commit this"
(Jira item vs. Confluence page), and Stage 04 `sad-update` lines (prose vs.
diagram sources) — are each disambiguated in both directions by the
respective near-miss lists. Live trigger behavior is part of the open gate
item 2.

## 4. Boundary/collision check — pass

Recorded in the batch entry's notable calls: disjoint among the seven by
stage and artifact; no overlap with the thirteen produced skills' declared
territories; the one shared surface (Stage 04 `sad-update`) is explicitly
split. No merge, split, or redraw needed beyond the already-decided
standalone call on `sad-diagram-maintainer`.

## 5. Evidence — this entry

Reviewer at the gate itself: the operator, pending. This pre-run is
agent-side preparation, not the human review.
