---
id: accomplishments-digest-stage-01
title: "Stage 01 — Frame"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "2.0"
status: living
truth-level: to-review
created: 2026-07-08
updated: 2026-10-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
---

# Stage 1 — Frame (`CONTEXT.md`)

## Inputs

The engineer's verbal statement of: the review period (start/end dates, or a
named cycle e.g. "H1 2026 self-assessment"), the audience (manager only, promo
committee, skip-level), and — if known — a short list of what they personally
consider their top 3–5 contributions this period. No prior stage; this is the
flow's entry point.

## Process

Ask, don't assume: confirm the period as concrete dates (not "this year"),
confirm the audience (it changes tone and detail level in Stage 7), and
elicit the engineer's own read on impact before any data is pulled. This
ordering matters, because framing set *after* seeing the gathered evidence
tends to anchor on whatever the tools happened to surface rather than
what the engineer actually thinks mattered. Also ask what to explicitly
exclude (a project that got cancelled, a sensitive reorg, anything not meant
for this audience).

Then scope the sources (new in 2.0):

1. **Capability probe.** Check which sources this engine can reach: Jira,
   Confluence, Microsoft Graph (Outlook, Teams, SharePoint/OneDrive), and
   ServiceNow (live, or export). Use the `START-HERE.md` probe pattern, and
   record the result per stage. A source the engine can't reach becomes a
   declared skip for its gather stage, not a failure.
2. **Sources in scope.** Confirm with the engineer which reachable sources
   to use this run. Any of them may be left out by choice.
3. **Identities.** Get the identifier that ties the engineer to each source in
   scope: Jira account, Microsoft 365 identity, ServiceNow user. Also get any
   shared mailboxes or Teams channels to include, which must be opted in by
   name. The personal mailbox is the default.
4. **Identifier types (optional).** Ask which work identifiers Stage 6
   should match evidence on: INC/CHG/PRB/PTASK numbers, Jira keys,
   Confluence page links, SharePoint file references. The answer can be all
   of them (the default), a subset, or none (theme matching only). Skip this
   step if the engineer has no preference; Stage 6 offers the same choice,
   with counts by type, once the digests exist, and restates whatever was
   chosen here.
5. **Exclusions as filters.** Turn the exclusion list into search filters
   that the gather stages apply before reading content. For mail and chat,
   these exclusions are always added, whatever the engineer names:
   HR, medical, personal, and compensation threads.

`Layer-3: inline (one-off, described above)`.

## Outputs

A **framing brief**: period (start date, end date), audience, a 3–5 item list
of self-identified top contributions (one sentence each, in the engineer's own
words), the exclusion list (including the mandatory mail and chat
exclusions), the capability-probe result per gather stage, the sources in
scope, the per-source identities and opt-ins, and the identifier types
chosen for Stage 6 (or "not set"). Lands in the run's working
folder as `work/01-framing-brief.md` (Layer-4, transient).

## Verify

A specific cross-stage trace check: Stage 7's draft must be able to point back
to every item in Stage 1's exclusion list and confirm none of it appears in
the synthesized document. Also, every gather stage's digest must
list the exclusion filters it applied, matching this brief's list. If either
check fails, the exclusion list wasn't carried forward. Stop and re-run the
carry-through before drafting continues. Result recorded as a one-line entry
in the run's decision log.

## Review

- **Reviewer:** the engineer (this is their own review — no delegate).
- **Intensity:** `heavy` — direction-setting judgment; nothing downstream can
  correct a wrong period, audience, or exclusion list without redoing the
  gather stages.
- **Evidence:** the framing brief itself, confirmed back to the engineer in
  plain language before any gather stage starts ("here's the period,
  audience, your top items, the sources we'll search and the ones we can't
  reach, and what's excluded — correct?").

## Data boundary

- **Max data-class this stage handles:** `internal` (the engineer's own
  self-assessment framing; may reference sensitive exclusions).
- **Sanctioned engines for this stage:** per the employer's sanctioned-tool
  matrix, whichever engine the engineer is using (Rovo or Copilot). The
  capability probe checks reachability only. No content is read at this stage.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
