---
id: comms-builder-stage-08
title: "Stage 08 — Publish & Hand Off"
type: stage-context
stage: 8
review-intensity: heavy
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[comms-builder]]"
  - "[[comms-builder-commit-packet]]"
  - "[[confluence-page-commit]]"
---

# Stage 8 — Publish & Hand Off (`CONTEXT.md`)

## Inputs

`work/07-approval.md` and the approved pack it names. The target surfaces
chosen at Stage 1 (chat, Confluence page, Jira comment). The Step 1
capability probe result. `reference/commit-packet.md` for packet Parts B–E.

## Process

1. Deliver the pack in chat: a header (subject, comms type, lane, key
   date), then drafts ready to paste into Outlook or Teams, the plan with
   the timeline image and raw Mermaid, and the meeting pack files.
2. For each Rovo-bound item (the Confluence plan page; the Jira
   plan-summary comment), emit a commit packet per
   `methodology/engine-handoff-contract.md` and `reference/commit-packet.md`
   as a `.md` file the requester pastes into Rovo. Copilot never writes to
   Confluence or Jira itself.
3. Tell the requester plainly what happens next: which drafts to send on
   which dates, which packet to paste where, and that nothing has been sent.
4. Store the run's work folder and the packet in `handoffs/` in the
   source-repo.

`Layer-3: inline (one-off, described above)` for delivery and packet
emission. The Rovo executor runs `confluence-page-commit` for the page and
an engine-native Jira comment action for the comment, per the packet.

## Outputs

The delivered pack in chat; zero to two commit packets
(`handoffs/comms-builder-commit-packet-<YYYY-MM-DD>-<n>.md`); a next-steps
list (send date, channel, draft id) for the requester. Return slips from the
executor, when they come back, land beside their packet.

## Verify

Stage 8 → Stage 7 trace: every item in the delivered pack and every packet
payload matches the version recorded in `work/07-approval.md` — no content
added or changed after approval. One-line result in the run's decision log.

## Review

- **Reviewer:** the requester.
- **Intensity:** `heavy` — the last check before anything reaches people.
- **Evidence:** the requester's confirmation that the pack is complete; the
  executor's return slip for each packet.

## Data boundary

- **Max data-class this stage handles:** `internal`.
- **Sanctioned engines for this stage:** Copilot produces; Rovo executes
  packets only.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
