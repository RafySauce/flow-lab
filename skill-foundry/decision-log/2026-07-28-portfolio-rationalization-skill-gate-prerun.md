---
id: decision-2026-07-28-portfolio-rationalization-skill-gate-prerun
title: "Decision Log — Portfolio Rationalization Skill Batch: Five-Point Gate Pre-Run"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
data-class: public
related:
  - "[[decision-2026-07-28-portfolio-rationalization-skill-batch]]"
  - "[[sp-jira-portfolio-ingest]]"
  - "[[sp-portfolio-profiler]]"
  - "[[sp-objective-keyword-mapper]]"
  - "[[sp-closure-scorer]]"
  - "[[sp-disposition-packet-builder]]"
  - "[[close-score-model]]"
---

# Decision Log — 2026-07-28 — Portfolio Rationalization Skill Batch: Five-Point Gate Pre-Run

**What was decided:** run the skill-foundry §5 review gate agent-side across
the five-skill batch and record the evidence here (gate item 5). **By whom:**
agent, same instruction as the batch-build entry. **What it affects:** one
spec received a pre-stage fix during the arithmetic check (§1 below); nothing
is promoted, nothing moved to `../../produced-skills/`, nothing deployed —
those calls stay with the operator.

## Scope limitation — read first

Gate item 2 demands a live test **on the target engine**. This session has no
Rovo or Copilot access, so no adapter has been invoked on-engine, and no
simulated adapter transcript was produced either: three of these five skills'
review criteria hinge on interactive operator confirmations (the field-map
confirmation, the lens offer, the dictionary currency confirmation) that a
synthetic transcript exercises poorly — it would show the agent asking, not the
gate holding. Gate item 2 is therefore **fully open**. What *was* run for real:
Mermaid compilation and the scoring model's arithmetic (both below).

## 1. Spec review — pass, one fix applied before staging

All five: purpose sharp; triggering intent names the misfires; boundaries
explicit and mutually naming (ingest ↔ accomplishments-gatherer and
↔ jira-commit; profiler ↔ scorer; mapper ↔ scorer and ↔ context-elicitation;
scorer ↔ packet-builder on both sides of the corroboration split); review
criteria transcribed from each brief's Definition of done and checkable as
written; frontmatter valid per `provenance-spec.md` (rule 3 —
`generated-by`/`generated-by-version` paired; rule 6 — spec frontmatter
`data-class: public`, with each body's Data boundary carrying the runtime max
of `internal`).

**Arithmetic reproduction — run, and it surfaced an unstated convention.** All
four synthetic cases in `close-score-model.md` §6 were recomputed from the
ramps: PORT-01 → 101 (5 of 5 firing), PORT-02 → 25 (1 of 5), PORT-03 → 41
(2 of 5), and the demotion example → 87 (2 of 5). All four reproduce exactly.
**But PORT-03 only reproduces under round-half-up:** its staleness
(`15 × 65 ÷ 150` = 6.5) and completion (`10 × 26 ÷ 40` = 6.5) both land on an
exact half and the model shows both as 7. A half-even (banker's) implementation
— the default in several standard libraries, including Python's `round()` —
returns 6 for both, reproduces PORT-01 and PORT-02 cleanly, and silently fails
PORT-03. The model's §3 says only "rounded to the nearest integer."

**Fix applied:** `closure-scorer`'s Method now states the half-up convention
explicitly, applies it across all three ramps, and flags it for ratification
into `close-score-model.md` §3 rather than leaving it implicit; both adapters
carry the same line. **This is a finding for the operator, not just a build
detail** — the model file is the flow-foundry's artifact, and a convention that
only exists in one skill's spec is drift waiting to happen. Ratifying it into
§3 (and bumping that file's `artifact-version`) is the clean resolution.

**Diagram discipline** (every node and edge ↔ a sentence in the Method prose)
was walked per spec: ingest's three-way mode diamond ↔ Method 3's three paths
and its screen halt ↔ Method 4; profiler's lens gate, its stop node, and the
dashed loop-back ↔ Method 9–10; mapper's dictionary halt ↔ Method 3; scorer's
sanity-check diamond and its divergence node ↔ Method 11; packet-builder's
corroboration diamond and demotion node ↔ Method 2. No unmatched node, no
unmatched sentence. **One judgment call for the reviewer:** packet-builder's
demotion node and scorer's divergence node use the `halt` role (rose) as
*exception paths that rejoin the main flow*, not as terminal stops. The guide's
definition covers exception paths; if the operator reads `halt` as
terminal-only, both should become `process` nodes.

**Mermaid compilation — run for real.** All five `flowchart LR` blocks were
extracted and compiled locally with `@mermaid-js/mermaid-cli` against the
pre-installed headless Chromium (`--no-sandbox`); all five rendered to SVG
without error. Rendering **on GitLab** is unconfirmed (no tenant access) and
remains part of the operator's spec-review item.

## 2. Live test on the target engine — OPEN (see scope limitation)

Not run, on-engine or simulated. Minimum for the gate: one invocation per
adapter on `public`/synthetic data, judged against each spec's review criteria.
Note the two dependencies that gate a *meaningful* Stage 03–05 test, recorded
in the batch entry: an instance objective dictionary must exist (the mapper
halts by design without one) and the instance status→adjustment mapping must be
recorded. A Stage 01–02 test needs neither and can run first.

## 3. Trigger check — pass (static)

Each spec's fires-on was walked against its four siblings' and the thirteen
produced skills' fires-on lists: no phrase routes to two skills. The closest
pairs — "pull the project into a normalized set" vs. "pull my closed work for
this quarter" (portfolio vs. one engineer's own record), "profile this
portfolio" vs. "score these for closure" (diagnosis vs. judgment), "map these
to objectives" vs. "should we close this" (alignment evidence vs. verdict), and
"score these" vs. "build the review pack" (numbers vs. banding) — are each
disambiguated in both directions by the respective near-miss lists. Live
trigger behavior is part of the open gate item 2.

## 4. Boundary/collision check — pass

Recorded in the batch entry's notable calls: the five are disjoint by stage and
by artifact (normalized set → profile → mapping record → scored ranking →
routed pack); no overlap with the thirteen produced skills' declared
territories; the one shared surface — the corroboration rule — is split
explicitly, with the scorer computing the count and the packet-builder
enforcing the demotion, and both specs naming the split. No merge, split, or
redraw needed.

Worth the operator's attention at the gate: **all five decline Jira writes and
none routes the request onward**, including away from `jira-commit`. That is
the flow's central guarantee ("it writes nothing to Jira at any stage") made
enforceable at the skill layer, and it is checkable in one pass across the five
`What this skill is not` sections and the Rovo adapters' permitted-action lists
(read-only Jira search on ingest; **no actions at all** on the other four).

## 5. Evidence — this entry

Reviewer at the gate itself: the operator, pending. This pre-run is agent-side
preparation, not the human review.
