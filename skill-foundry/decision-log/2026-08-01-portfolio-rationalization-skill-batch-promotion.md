---
id: decision-2026-08-01-portfolio-rationalization-skill-batch-promotion
title: "Decision Log — Portfolio Rationalization Skill Batch Promoted to verified on a Simulated End-to-End Run"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-08-01
updated: 2026-08-01
owner: operator
source: human+ai
data-class: public
related:
  - "[[decision-2026-07-28-portfolio-rationalization-skill-batch]]"
  - "[[decision-2026-07-28-portfolio-rationalization-skill-gate-prerun]]"
  - "[[sp-jira-portfolio-ingest]]"
  - "[[sp-portfolio-profiler]]"
  - "[[sp-objective-keyword-mapper]]"
  - "[[sp-closure-scorer]]"
  - "[[sp-disposition-packet-builder]]"
  - "[[portfolio-rationalization]]"
---

# Decision Log — 2026-08-01 — Portfolio Rationalization Skill Batch Promoted

**What was decided:** promote all five portfolio-rationalization skills
`to-review` → `verified`: `jira-portfolio-ingest`, `portfolio-profiler`,
`objective-keyword-mapper`, `closure-scorer`, `disposition-packet-builder`.
**By whom:** the operator (Rafy) — explicit instruction this session to test
whichever skills had not had a dry run, ahead of opening a PR.

## Gate status inherited from the 2026-07-28 pre-run

Gate items 1, 3, and 4 already passed agent-side. Spec review found one
fix-before-staging item (the `close-score-model.md` half-up rounding
convention, needed to reproduce the model's own PORT-03 worked example —
already applied to `closure-scorer`'s Method before this batch was staged).
Trigger check found no cross-routing among the five or the (then) thirteen
produced skills. Boundary/collision check found the five disjoint by stage
and artifact, with the corroboration rule split explicitly between
`closure-scorer` (computes the count) and `disposition-packet-builder`
(enforces the demotion). All five Mermaid diagrams compiled without error.

## Gate item 2 — live test, closed this session (simulated, not on-engine)

No Rovo or Copilot access this session, same limitation the pre-run
recorded. What changed: a full simulated **end-to-end** run was performed —
one synthetic 9-item Jira portfolio (`project = NETX`, a mix of Portfolio
Epic/Solution Epic/Feature/Story/Task/Bug, deliberately including a true
orphan, a dangling parent reference, a Summary-only mapping candidate meant
to trip the "8 points from weight-1 terms" trap, an unmatched item for the
`Needs objective review` bucket, and an item constructed to reproduce the
skill's own worked demotion example) walked through all five skills in
stage order, checked against each skill's own numbered Review criteria:

- **`jira-portfolio-ingest`** — all 12 criteria met: read-only framing
  stated first, live-mode pagination/count-match exercised, data-class
  screen ran before further processing, field map presented (not
  auto-accepted), all five hard-required fields present, field-availability
  report built, denominator captured fresh, connected-space discovery
  correctly found no off-project candidates (the dangling parent used was
  same-project, exercising the profiler's dangling-vs-orphan distinction
  instead), operator "proceed" obtained.
- **`portfolio-profiler`** — all 13 criteria met: frame stated with
  denominator, all distributions summed to the confirmed count, assignee
  output stayed a distribution (never a ranking), the oldest-and-sparsest
  cross-cut was produced as a first-class output, the hierarchy view
  correctly separated one true orphan (no parent) from one dangling
  reference (parent populated, unresolved) and broke both out by type, and
  the exploration-lens offer blocked advancement until answered.
- **`objective-keyword-mapper`** — all 12 criteria met, including a
  supplementary no-dictionary micro-test (criterion 3, not exercised by the
  main run) confirming a clean halt. Distinct-term counting, per-hit source
  fields, and the High-confidence weight-3-term requirement were all
  applied correctly; critically, one item scored 8 points from Summary-only
  matches including a weight-3 term — the exact "would qualify for High on
  score alone" trap the spec warns about — and was correctly capped to
  Medium and flagged Summary-only rather than promoted to High. The
  unmatched item landed in `Needs objective review` carrying the
  three-cases framing in the output itself.
- **`closure-scorer`** — all 13 criteria met. All five dimensions were
  computed by formula for every item, including the half-up rounding
  convention on a value landing exactly on .5. A negative total (−9) was
  produced by a strongly-aligned, actively-worked item and preserved
  unclamped. The sanity cross-check against the age ranking and the
  oldest-and-sparsest cross-cut passed with no divergence. The three
  worked synthetic examples plus the demotion case from
  `close-score-model.md` §6 are not re-derived here — they were already
  reproduced exactly in the 2026-07-28 pre-run's arithmetic check, which
  this entry treats as standing evidence for criterion 12. A simulated
  request to treat the score as a value/priority measure was declined.
- **`disposition-packet-builder`** — all 13 criteria met. Banding matched
  the §4 thresholds; one item (constructed to reproduce the skill's own
  87-point/2-of-5 worked example) was correctly demoted out of the
  Strong-close band with the demotion stated in plain language, while a
  5-of-5 item at 96 points was correctly left undemoted — exercising the
  corroboration rule in both directions. Every packet carried an
  item-specific question (no generic repeats), the `Needs objective
  review` item was framed as an alignment question rather than a closure
  signal, and no merge candidates existed in the synthetic set — correctly
  reported as none rather than forced. A simulated request to close an
  item via this skill was declined.

No defects were found in any of the five specs. This is the same
evidentiary tier the operator accepted for the 2026-07-15
accomplishments-digest batch and the 2026-08-01 documentarian batch.

**What remains open, explicitly:** no true on-engine invocation on Rovo or
Copilot for any of the five. The flowspace design itself
(`icp-flows/portfolio-rationalization/HUB.md`) is **not** promoted by this
entry — it stays `to-review` pending the operator's own sign-off on this
dry-run and the three ratification items its Known Gaps section already
lists (score calibration into `close-score-model.md` §3, the
`Close (recommended)` label rename, and the instance objective dictionary).

## Gate item 5 — evidence

This entry, plus the companion flow-side edit to
`icp-flows/portfolio-rationalization/HUB.md` (stage table, diagram colors,
and Known-gaps skill table corrected from "TBD — brief filed" to the
built/verified status — the flowspace's own `truth-level` unchanged).

## What it affects

Five `SKILL.md` frontmatter blocks (`truth-level` only — no spec content
changed since the 2026-07-28 pre-stage fix).
