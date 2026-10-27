---
id: decision-2026-07-08-accomplishments-digest-scaffold-triage
title: "Decision Log — Accomplishments Digest Triage and Scaffold"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-08
updated: 2026-07-08
owner: operator
source: human+ai
data-class: public
related: ["[[fp-accomplishments-digest]]", "[[accomplishments-digest]]"]
---

# Decision Log — 2026-07-08 — Accomplishments Digest Triage and Scaffold

**What was decided:** the operator's request ("a skill (or flowspace) that
collects and collates Jira/Confluence information into a performance-review
accomplishments document") was triaged as a **flow-primer-brief** (clean-path
intake, crystallized in the same session) and routed to the **flow-foundry**,
not the skill-foundry. **By whom:** agent, on direct operator instruction,
after confirming three setup-questionnaire items (cadence, document emphasis,
build scope) via clarifying questions. **What it affects:** new flow-primer-
brief `fp-accomplishments-digest` filed to `backlog-flow-starters/`, new
flowspace scaffold staged here at `to-review`, three skill-primer-briefs
filed to `skill-foundry/backlog-skill-starters/` for the flagged Layer-3 gaps.

## Why this is a flowspace and not a single skill

The request's shape — gather from two systems, synthesize, and get it in
front of a manager — carries genuine human-judgment boundaries at both ends
(what to frame as important before seeing tool output; what to actually
publish after seeing the draft) that a single skill invocation can't hold.
The existing `fp-weekly-status-report` exemplar established the same pattern
for a structurally similar recurring Jira+Confluence-to-document workflow;
this flowspace follows its stage shape (frame → gather → gather → draft →
align & publish) rather than inventing a new one. A skill alone would need to
either skip the framing/align judgment stages (producing a tracker-flavored
document, the exact failure mode the flow is designed to avoid) or smuggle
multi-turn human review into a single skill's contract, which the skill-
foundry's own boundary discipline (skills are discrete, reusable capability
definitions) argues against.

## Decisions and alternatives

1. **Split Jira and Confluence gather into two stages, not one.** The
   operator's answer to the doc-shape question named both delivered work
   (Jira) and initiatives/docs/collaboration signal (Confluence) as wanted
   emphasis, each with a distinct query shape and distinct data source.
   *Alternative considered:* one combined "gather" stage — rejected, since
   the two sources have no dependency on each other and combining them would
   blur the Layer-3 skill boundary (one gatherer skill trying to do two
   platforms' native queries).
2. **Collaboration signal folded into the Confluence stage, not its own
   stage.** The operator selected it as a desired emphasis but it's a thin
   signal (comments/mentions) layered on top of the Confluence query, not a
   separate data-gathering operation with its own contract. *Alternative
   considered:* a fourth gather stage — rejected as premature structure for
   a slice this thin; revisit if collaboration signal turns out to need its
   own query surface at instantiation.
3. **Self-framed narrative handled as part of Stage 1 (Frame), not a
   separate stage.** The operator's fourth doc-shape selection ("self-framed
   narrative") is the reason Stage 1 elicits the engineer's own top-items
   list *before* any tool data is gathered, rather than being bolted on
   after drafting. This is stated explicitly in Stage 1's Process field
   (ordering rationale) so a future reviewer doesn't mistake it for an
   arbitrary stage-count choice.
4. **Full scaffold built now, staged to `review-flowspaces/`, not promoted.**
   Per the operator's explicit build-scope answer. The foundry's own rule —
   never self-promote — applies unchanged: this stays `to-review` until the
   operator runs the three-gate validation checklist.

## Assumption (operator to confirm or amend)

- **J1 — per-tenant activity-history depth is unknown until instantiation.**
  Stage 3's contract and the primer brief both flag that Confluence's
  comment/mention visibility varies by instance and can't be assumed at
  design time. Amendment path: if instantiation reveals the signal is
  reliably available (or reliably absent) across the target org, fold that
  into Stage 3's contract as a stated fact rather than a per-run check.
