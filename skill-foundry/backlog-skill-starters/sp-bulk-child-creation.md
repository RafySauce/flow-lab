---
id: sp-bulk-child-creation
title: "Skill Primer Brief — Bulk Child Creation"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-31
updated: 2026-07-31
owner: operator
source: human+ai
data-class: public
related: ["[[ai-refinement]]", "[[value-decomposition]]", "[[jira-commit]]"]
---

# Skill Primer Brief — Bulk Child Creation

> Intake path 1 for the skill-foundry: crystallized intent, written before
> authoring starts. Filed in `skill-foundry/backlog-skill-starters/` as
> `sp-bulk-child-creation.md`.

## Purpose

Creates many child work items in one reviewed pass, for the case where the
user already knows what the items are and only needs them drafted to house
standard and created. Replaces two manual practices: hand-creating a set of
tasks or stories in Jira one at a time (losing the schema enforcement,
labels, persona, and audit trail that `ai-refinement` exists to provide), and
running the flowspace's Band ② pipeline N times for a set the user already
enumerated.

The two use cases that drove the request, both operator-stated: creating a
solution epic with its child features, and creating many tasks or stories
under one feature.

## Triggering intent

**Fires on** — the user's input indicates a set of items rather than one
item, and the deciding is already done:

- A spreadsheet, export, or attached file listing work items.
- A pasted table, numbered list, or bulleted list where each row is an item.
- Vendor documentation or a URL enumerating required actions.
- A conversation in which the user has described several discrete pieces of
  work in one turn.
- A `value-decomposition` pass that produced an accepted child set the user
  wants created rather than refined one at a time.
- Explicit phrasings: "build them all," "create all of these," "make these
  tasks," "go create the features for this epic."

The mode is **inferred from the input**, not waited for as a command — the
skill recognizes list-shaped material and proposes bulk creation with its
reasoning stated. The user always makes the final call.

**Does not fire on (near-misses):**

- **One complex item with many scope bullets.** The single most likely
  misfire. Twelve bullets describing facets of one outcome is one item with a
  populated `in_scope`, not twelve items. The test: would each row stand alone
  as a work item with its own acceptance criteria?
- Two or three items surfacing from meeting minutes — ordinary sequential
  Band ② runs, the existing behavior.
- A request to bulk-edit, bulk-close, bulk-label, or bulk-transition
  *existing* Jira issues. This skill creates; it never edits a portfolio.
  (`jira-portfolio-ingest` reads portfolios and writes nothing.)
- Decomposition itself — proposing *what* the children should be is
  `value-decomposition`'s job. This skill takes a set that already exists and
  creates it.
- A single item the user wants refined properly. The full Band ② pipeline is
  still the right and better path, and the flow should say so.
- Sub-tasks, which stay out of the pipeline per the schema registry.

## Method sketch

1. **Recognize and propose.** State why the input reads as a set, how many
   items were counted, and what type each appears to be. Propose bulk
   creation. The user confirms, corrects the count or types, or declines to
   single-item refinement.
2. **Take the bulk acknowledgment.** Separate from and additional to Stage
   01's general responsibility notice, and separate from the mode question
   itself — the user answers the mode question, then acknowledges, as two
   acts. Per the `bulk_creation_acknowledgment` house amendment.
3. **Ingest and normalize the set.** CSV/XLSX, attached files, pasted
   content, vendor URLs and documentation, and the conversation itself.
   Quote-honoring parse for tabular sources; capture the header row; collapse
   repeated columns; confirm the parsed item count against the user's stated
   expectation. Run the data-class screen before the rows are typed any
   further — a spreadsheet's columns come along wholesale.
4. **Draft required fields per item, from the provided context only.** Fill
   the selected type's required schema fields to the best of the available
   grounding.
5. **Stop at the edge of the evidence.** The quality bar this skill lives or
   dies on: when the provided detail runs out, **stop generating and say so**
   — never pad a thin row into a full-looking item. Items that cannot be
   grounded are reported as underspecified, with the specific missing fields
   named, and the user supplies detail or drops them.
6. **Offer suggested next items, clearly separated.** Having stopped, the
   skill may *offer* to suggest likely further work items — drawing on the
   value-delivery model, general domain knowledge, and internet sources where
   available. These are presented as a visually and structurally distinct
   set, never merged into the grounded set, and carry an explicit warning
   that their relevance and accuracy need close attention. Opt-in, never
   automatic.
7. **Present the whole set for one review.** Same verdict vocabulary as
   `value-decomposition`: accept all, edit some, reject some, or stop with
   nothing created.
8. **Create via native tooling first.** Rovo's native Jira MCP actions are
   the primary path, per house standards and the `jira-commit` precedent.
   Sequential creation, halting on failure, with a running result table of
   keys and URLs.
9. **Degrade to a handoff document.** If the tools cannot create the items —
   no write path, permissions, repeated failures — offer to produce a
   human-readable Markdown file carrying the full drafted set, structured so
   a fresh session can pick it up and finish the job. A valid terminal
   output, not a failure state.

### Known failure modes to guard against

- **Fabrication under batch pressure.** The most damaging failure: forty
  plausible-looking items where fifteen were invented. Step 5 is the guard.
- **Splitting one item into many.** See the near-miss above.
- **Silent partial creation.** The user must always know exactly what landed
  in Jira and what did not. No rollback exists; say so before approval.
- **Suggested items laundering into grounded ones.** Keep the two sets
  structurally separate through review and creation.
- **Scope creep into bulk editing.** Creation only.

## Inputs and data boundary

Reads: the user-supplied item set in any of its carriers (CSV/XLSX,
attachments, pasted content, vendor URLs and documentation, conversation);
the parent item's content where the set is being created beneath one; the
work-item schema registry for the required field set per type; the
flowspace's guardrails, persona, and label amendments. For the optional
suggested-items step, the value-delivery concepts and internet sources.

Max data-class: **internal**, matching the rest of the `ai-refinement`
pipeline. Exports are the higher-risk carrier — the data-class screen runs
before rows are typed further. Content above the ceiling halts the run rather
than being redacted and carried forward: redaction at batch volume is not
reliably verifiable.

Engines: Rovo and Copilot. Rovo is the primary target — the operator's stated
requirement is that the skill reach for Rovo's native MCP tooling first — but
nothing in the method is Rovo-specific, so Copilot runs it through the
sanctioned Jira integration on the same terms.

Internet sources are read-only and only reachable in the optional
suggested-items step; anything retrieved is third-party material and gets the
same vetting the source-input taxonomy already applies to vendor material.

## Demand source

Raised directly by the operator, 2026-07-31: the `ai-refinement` flow
"currently focuses on specific refinement and decomposition of work in a very
detailed manner" and should recognize and offer a fast path for creating many
child items when that is what the situation calls for — with a clear
confirmation that bulk creation is to be used carefully and that AI-generated
items may not be correct and should be reviewed.

Flowspace gap: `icp-flows/ai-refinement/` — the pipeline's founding premise
is "one run = one fully refined work item committed to Jira" (`HUB.md`), and
`jira-commit` refuses bulk by contract. Neither was wrong; both were
single-case.

## Definition of done

1. Given list-shaped input, the skill proposes bulk mode with a stated count,
   per-row type reading, and reasoning — and does not proceed without both a
   mode choice and a separate acknowledgment.
2. Given one complex item with many scope bullets, it does **not** propose
   bulk mode, and says why.
3. Given a set where some rows are richly specified and others are one-liners,
   it drafts the former, names the latter as underspecified with their missing
   fields, and invents nothing.
4. Suggested next items, if offered at all, are opt-in, structurally separate
   from the grounded set, and carry the accuracy warning.
5. A simulated mid-batch creation failure halts the run and reports precisely
   what was created and what was not.
6. With no write path available, the run produces the Markdown handoff
   document and says plainly that nothing was created.
7. Every created item carries the same labels, schema compliance, and
   formatting rules a single-item run would produce — bulk changes cadence,
   never standards.
