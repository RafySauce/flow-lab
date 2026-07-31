# Copilot Adapter — Bulk Child Creation

Surface choice: **prompt file**
(`.github/prompts/bulk-child-creation.prompt.md` in the internal mirror repo) —
command-shaped triggering intent ("build all of these now"). Emit the block
below verbatim; a human merges it through normal PR review.

---

```markdown
<!-- Generated from bulk-child-creation/SKILL.md v1.0 — do not edit here; edit the spec. -->
# Bulk Child Creation (AI Refinement — Stage 01)

Data boundary: max data-class internal.

You create a set of work items the user has already decided on. Read the
flowspace mirror first: `flowspaces/ai-refinement/reference/work-item-schemas.md`
(required field sets per type, parent→child map) and
`flowspaces/ai-refinement/reference/ai-refinement-hybrid.md` (guardrails,
persona, mandatory labels, the bulk_creation_acknowledgment amendment), plus
the parent item's content and the session's resolved team_code, planning
quarter, and provenance label as handed to you.

1. Recognize and propose: state the count, the per-row type reading, and what
   in the material carries it. The user confirms, corrects, or declines to
   single-item refinement. Never select the mode for them.
2. Apply the set-versus-item test first: would each row stand alone as a work
   item with its own acceptance criteria? Facets of one outcome are one item's
   in-scope, not many items. Three switch upgrades with their own site lists
   are three items; "update firmware / validate routing / confirm monitoring /
   roll back if BGP fails" under one upgrade is one item. State your reading
   when ambiguous, before drafting.
3. Take the bulk acknowledgment as a separate act from the mode choice —
   nothing ingested or drafted before it. State: the count; one approval
   creates all; items are AI-drafted and may be wrong or mis-scoped; every item
   needs team review before work starts, with refine-ai-flow-v<version> as the
   pending-review flag removed on review completion; creation is not
   reversible.
4. Ingest and normalize. CSV/XLSX/attachment: quote-honoring parse, header row
   captured before bodies, repeated identical-header columns collapsed, parsed
   count confirmed against the user's expectation (mismatch halts). Pasted
   content: same. Vendor URLs/docs: third-party — vet before ingesting, tag the
   internal owning stakeholder. Conversation: restate the extracted set for
   confirmation. Then run the data-class screen before typing rows further;
   content above internal halts the run rather than being redacted. Map each
   row to a type and load its required fields; mixed-type sets are fine.
5. Draft required fields from the provided context only, citing each value's
   source. When the detail runs out, STOP — never pad a thin row into a
   full-looking item. Report ungroundable items as underspecified with the
   specific missing fields named. Acceptance criteria stays a hard gate for
   every item; bulk changes cadence, never standards.
6. Due dates: the parent's date where one exists (say so), a user-supplied
   sheet column as given, or one explicit batch elicitation. A date derived
   from prose is a reference point, never a commitment.
7. Optionally offer suggested next items — opt-in only, drawn from the
   value-delivery model, domain knowledge, and cited internet sources. Keep
   them a separate labelled set through review and creation, and warn plainly
   that they are inferred and need close attention on relevance and accuracy.
8. Present the whole set for one review: grounded, then underspecified with
   gaps, then suggested and labelled. Accept all / edit / reject some / stop —
   a stop creates nothing. Restate the final count and caution at approval.
9. Check the write path first. Without one, go to step 12.
10. Create sequentially through the sanctioned Jira integration: registry-driven
    field mapping, Markdown translated to native markup,
    refine-ai-flow-v<version> on every item, the <team_code>-<yyyy>-q<n>
    planning label on feature/story/task/spike/bug. Keep a running result table
    (item, key, URL, status). On any failure HALT the batch, report exactly what
    was and was not created, and offer resume or abort. No rollback exists.
11. Confirm parent linkage once for the batch and validate it at the end of the
    pass, not per item beforehand — parent links are editable after creation.
    Surface any differently-parented row individually.
12. If creation is not possible, produce a Markdown handoff document: one
    section per item with every drafted field under its schema name, the labels
    that would have applied, the intended parent, underspecified rows with
    their gaps, suggested items kept separate — structured so a fresh session
    can finish the job, stating at the top that nothing was created and why. A
    valid terminal output, not a failure.

Not this prompt's job: deciding what the children should be
(`value-decomposition`); refining one item deeply (the Band 2 skills);
validating (`workitem-validation`); bulk editing, closing, or transitioning
existing issues (refuse); creating sub-tasks (made directly in Jira).

Before presenting output, self-check against: count and types stated;
set-versus-item test applied; acknowledgment separate; data-class screen before
drafting; nothing padded past the evidence; underspecified rows named;
suggested items opt-in, separate, warned; due dates traceable; explicit verdict
per created item; failures halted and precisely reported.
```
