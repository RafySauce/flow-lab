---
id: decision-2026-08-01-portfolio-and-statik-validation-checklist-run
title: "Decision Log — Validation Checklist Run: portfolio-rationalization and statik-adoption (Both Stay to-review)"
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
  - "[[portfolio-rationalization]]"
  - "[[statik-adoption]]"
  - "[[decision-2026-08-01-portfolio-rationalization-gap-ratifications]]"
  - "[[decision-2026-08-01-statik-adoption-gap-ratifications]]"
---

# Decision Log — 2026-08-01 — Validation Checklist Run

**What was checked:** `flow-foundry/templates/validation-checklist.md`'s
three gates, run against both flowspaces after this session's gap-closing
work (label-rename ratification and denominator redesign for
`portfolio-rationalization`; history-delta resolution and the
`servicenow-ticket-ingest` build for `statik-adoption`). **By whom:** agent,
checking Gates 1–2 directly (objective, checkable facts); Gate 3 is scoped to
what an agent can respond to — it is not a substitute for the operator's own
dry-run judgment call.

**Result for both flowspaces: stay `to-review`.** Neither is promoted by
this entry. Per `foundry-spec.md` §7, promotion is the operator's call, every
time — and both flows carry real, named, unresolved gaps in their own
`HUB.md` Known Gaps sections that a genuine dry-run would surface as
blocking, independent of who runs the checklist.

## portfolio-rationalization

**Gate 1 — structural completeness — pass.** `HUB.md` frontmatter valid
(`type: flowspace`, `owner: operator`, `data-class: public`); stage table
(7 rows, including the `03p` branch) matches the 7 stage folders one-for-one;
Stage Flow Diagram present, matches the stage table, uses the house palette
including the documented `03p` branch. Every stage `CONTEXT.md` populated —
no placeholder or template-remnant text found in this pass. Review intensity
set per stage. Data boundary set per stage (`internal` throughout, consistent
with the sanctioned-tool matrix as described). Source-repo section present
(`## Source-repo` — already on the current heading, no drift here).
*Not independently confirmed this pass:* Mermaid rendering on live GitLab —
this repo copy renders correctly in a standard Markdown/Mermaid preview, but
"confirmed on GitLab" per the checklist's own wording means the actual
instance, which only exists in employer tenancy.

**Gate 2 — Layer-3 status declared — pass.** All 7 stages declare Layer-3
status explicitly (5 promoted skills covering Stages 01–05, `03p` and
Stage 06 inline). `HUB.md` Known Gaps lists every flagged item.

**Gate 3 — human dry-run — return with findings, not promotable yet.** Two
gaps in Known Gaps are not something this session's gap-closing pass could
resolve, because both need inputs an agent session cannot manufacture:

1. **Score calibration** (`close-score-model.md` §7) — the five ramps and
   three band thresholds are inferred from five data points, never run
   against a real cycle. A dry-run walking Stage 04's contract would hit
   this immediately: "Process is actionable" is true, but the numbers it
   acts on are explicitly stated as proposals.
2. **Objective dictionary** — no instance dictionary exists yet; Stage 03's
   inference-and-confirm fork handles the "nothing supplied" case
   procedurally but still needs either operator authorship or a confirmed
   inference to produce a governance-grade Stage 04–06 run.

Both are named, not hidden, in `HUB.md` — this checklist run doesn't discover
anything new, it confirms the existing Known Gaps entries are still the
actual blockers and that this session's two closed gaps (label rename,
denominator) are no longer among them.

## statik-adoption

**Gate 1 — structural completeness — pass.** `HUB.md` frontmatter valid;
stage table (8 rows) matches the 8 stage folders one-for-one; Stage Flow
Diagram present and matches the stage table. Every stage `CONTEXT.md`
populated. Review intensity and data boundary set per stage. Source-repo
section present (`## Source-repo` — already current, no drift). Same GitLab-
rendering caveat as above.

**Gate 2 — Layer-3 status declared — pass.** All 8 stages declare Layer-3
status; Stage 01 now names both `jira-portfolio-ingest` and
`servicenow-ticket-ingest` as verified alternatives (this session's build
closed the "backlog-staged" state the stage table carried). `HUB.md` Known
Gaps lists every flagged item, now three instead of the five it opened this
session with (ServiceNow ingest and the history delta both resolved today).

**Gate 3 — human dry-run — return with findings, not promotable yet.** Three
gaps remain, none closeable by this session:

1. **Evidence-sufficiency floors are reasoned, not calibrated** — the 30-item
   and one-full-arrival-cycle floors are defensible defaults, not validated
   against this operator's actual boards. Same category of gap as
   portfolio-rationalization's score calibration: needs real board data.
2. **The two unreachable source articles** (`aktiasolutions.com`,
   `hjavixcs.medium.com`) — HTTP 403 at the egress proxy, an organization
   policy denial an agent session cannot route around. Residual risk
   (rollout-emphasis framing this build may not reflect) stays open until the
   operator supplies the text directly.
3. **`servicenow-ticket-ingest` has no on-engine test** — built and gated
   this session on synthetic data only; the sanctioned ServiceNow read
   connector isn't confirmed against a specific engine yet.

## What this entry does not do

It does not re-open or re-decide anything already ratified today (the label
rename, the denominator redesign, the history-delta resolution, or the
ServiceNow-ingest build) — those stand as recorded in their own entries. It
does not promote either flowspace's `truth-level`, and it does not move
either folder — both already live in `icp-flows/` (not
`review-flowspaces/`), consistent with how this repo has staged in-place
flowspace work rather than round-tripping through the foundry's staging
queue for revisions to an already-scaffolded flow.
