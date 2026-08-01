---
id: sp-jira-portfolio-ingest
title: "Skill Primer Brief — Jira Portfolio Ingest"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[export-and-field-requirements]]"
---

# Skill Primer Brief — Jira Portfolio Ingest

## Purpose

Bind a portfolio review cycle to its data source — a live Jira project/space or
an export of the same — and emit one canonical, normalized item set plus a
field-availability report, so every downstream stage reads the same shape
regardless of where the data came from. Replaces the manual export-and-clean
step that currently starts each analysis by hand and produces a different
column layout every time.

## Triggering intent

**Fires on:** Stage 01 of `portfolio-rationalization`. Also standalone on
"pull the whole NE project into a normalized set," "normalize this Jira
export," "bind this export for portfolio analysis," or a portfolio-wide
export/CSV arriving with an analysis intent attached.

**Does not fire on:**

- Refining or creating a single work item — that is `ai-refinement`'s pipeline
  and `jira-commit`'s job. This skill is portfolio-scoped and read-only.
- Querying one engineer's own closed work for a review period — that is
  `jira-accomplishments-gatherer`. Different unit of analysis (person, not
  portfolio), different intent (evidence, not triage). This skill borrows its
  live-query-with-paste-degrade *pattern*; the scope is unrelated.
- Any request that implies writing to Jira. This skill has no write path and
  should decline rather than route.

## Method sketch

1. Take scope: project/space, optional JQL, source mode, expected item count.
2. **Live mode** — read-only query via the engine's native Jira capability;
   page to completion; confirm the returned count matches the query's reported
   total. Halt on truncation.
3. **Export mode** — parse CSV/XLSX with a quote-honoring reader (embedded
   newlines in descriptions and comments are routine); capture the header row
   before parsing bodies; collapse repeated same-header columns (labels,
   comments, links) into one canonical field each.
4. **Degrade path** — no Jira connector and no export file: ask the operator to
   paste the item set directly and normalize from that, stating plainly which
   fields the pasted shape lacks and what that degrades. Never silently.
5. Run the data-class screen **before** typing the data further. Halt above the
   sanctioned ceiling; do not redact and continue.
6. Confirm the parsed item count against the operator's expectation.
7. Map source fields onto the canonical set and **present the map for
   confirmation** — never auto-accept.
8. Check hard requirements: Issue key, Summary, Status, Created, Updated.
9. Emit the normalized set (ISO dates, empty-equivalents resolved), the
   field-availability report, and this cycle's completion denominator.

**Quality bar:** a live-bound cycle and an export-bound cycle over the same
portfolio must produce identical normalized sets. That is checkable, and it is
the skill's definition of correct.

**Failure modes to guard against:**

- Silent pagination truncation — profiles cleanly, describes the wrong
  portfolio.
- Naive line-splitting on export parse — phantom rows from embedded newlines.
- Auto-accepting a plausible-but-wrong field map (a custom "Outcome" field
  mapped to Business Outcome when it means something else) — poisons objective
  mapping invisibly.
- Carrying forward a prior cycle's denominator — produces plausible completion
  percentages that mean nothing.
- Treating a missing field as a zero rather than as unavailable.

## Inputs and data boundary

**Needs:** read-only access to one Jira project/space (live mode), or an export
file (export mode), or pasted content (degrade path). Field names and hierarchy
per `icp-flows/ai-refinement/reference/work-item-schemas.md`; requirements and
parity contract per the flowspace's
`reference/export-and-field-requirements.md`.

**Max data-class:** `internal`. This is the flow's classification gate — it
screens before anything else touches the data. Exports are the higher-risk
carrier: every column comes along, and comments and custom fields routinely
carry personal names, customer references, hostnames, and occasionally
credentials.

**Engines:** Rovo and Copilot both. Not a constraint — Rovo's native Jira
actions suit live mode, Copilot suits export mode, and the degrade path needs
neither.

## Demand source

Layer-3 gap at Stage 01 of the `portfolio-rationalization` flowspace, filed
during its scaffold (`flow-foundry/decision-log/2026-07-28-portfolio-rationalization-triage-and-scaffold.md`).
The stage contract carries this brief's id.

## Definition of done

- Round-trips a real portfolio through both modes and produces identical
  normalized sets.
- Halts — not warns — on count mismatch, pagination truncation, a missing hard
  requirement, or content above the sanctioned ceiling.
- The field-availability report is complete enough that Stage 03 can decide
  whether it is mapping on rich text or summaries alone without asking.
- The degrade path has been exercised at least once and states its gaps
  plainly.
- Never writes to Jira, and declines rather than routing when asked to.
