---
id: confluence-activity-history-capability-check
title: "Confluence Activity-History Capability Check — Accomplishments Digest"
type: specification
artifact-version: "1.0"
status: living
truth-level: verified
created: 2026-07-14
updated: 2026-07-15
owner: operator
source: human+ai
data-class: public
related: ["[[accomplishments-digest]]", "[[confluence-contribution-gatherer]]"]
---

# Confluence Activity-History Capability Check — Accomplishments Digest

**Status: prepared, not executed.** This resolves the open question in
`../../../backlog-flow-starters/fp-accomplishments-digest.md` ("does the
target org's Jira/Confluence instance expose enough activity history to
make the collaboration-signal slice reliable?") into a concrete, one-time
probe an operator runs once per Confluence tenant at instantiation, rather
than leaving it a standing unknown. Stage 3's `CONTEXT.md` and the
`confluence-contribution-gatherer` skill both already handle an unusable
result gracefully at run time (narrow to authored-pages-only, flag it
explicitly) — this checklist is what tells the operator, once, which mode a
given tenant is actually in, so every run afterward doesn't have to
rediscover it live.

## How to use this

Run once per Confluence tenant, before the first real `accomplishments-
digest` run in that tenant (or after a Confluence version upgrade — activity-
history retention is a platform-level setting that can change). Record the
result as a decision-log entry in the instantiated flowspace's own
`decision-log/` (not this public repo) and reference it from Stage 3's
`CONTEXT.md` Layer-3 line so every subsequent run reads the answer instead of
re-probing.

## Probe steps

1. **Pick a page with known recent activity** — one with comments, at least
   one `@mention`, and a review/approval cycle in the last 90 days, ideally
   spanning both a short window (last 7 days) and a longer one (60–90 days).
2. **Query comment history** via the same interface `confluence-contribution-
   gatherer`'s Rovo/Copilot adapter would use (native Confluence action or
   the sanctioned connector). Confirm: are comments from the full 90-day
   window returned, or does the result silently truncate to a shorter
   retention window?
3. **Query mention/notification history** the same way. Some instances
   surface `@mentions` only through personal notification feeds (not
   queryable for another timeframe after the fact) rather than a searchable
   page-activity log — confirm which is true here.
4. **Query cross-team page contribution signal** (co-authorship, page
   history "contributors" list) — this is usually reliable even where
   comment/mention depth is not; confirm it separately rather than assuming
   it fails alongside the other two.
5. **Classify the tenant** against the decision table below and record the
   result.

## Decision table

| Finding | Classification | What Stage 3 / the skill should do |
|---|---|---|
| Comments, mentions, and contributor history all return reliably for ≥ 90 days | **Full depth** | Run the full collaboration-signal slice as designed; no fallback needed. |
| Contributor history reliable; comments/mentions truncated or unqueryable | **Partial depth** | Gather co-authorship/contribution signal normally; explicitly omit the comment/mention slice and say so — this is the "collaboration signal unavailable" fallback path already built into the skill's Method step 2, not a new behavior to design. |
| Nothing beyond page authorship is reliably queryable | **Authored-pages-only** | Skip collaboration-signal gathering entirely; the skill's fallback note becomes the default behavior for this tenant, not an occasional edge case. |

## What this does not resolve

This checklist tells you *which* fallback mode a tenant is in — it does not
change the skill's behavior in any mode; the skill's spec already implements
all three rows correctly by design (per its Review criterion 2). It also
does not need re-running per review cycle, only per tenant (and after a
platform upgrade that could change retention settings) — treat a stale
classification as a bigger risk than not having run this at all, since a
tenant that quietly upgraded from Partial to Full depth would otherwise keep
under-reporting collaboration evidence indefinitely.
