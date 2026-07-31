---
id: decision-2026-07-31-bulk-creation-mode
title: "Decision Log — Bulk Creation Mode"
type: decision-log
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-07-31
updated: 2026-07-31
owner: operator
source: human+ai
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[ai-refinement-hybrid]]"
  - "[[work-item-schemas]]"
  - "[[bulk-child-creation]]"
  - "[[value-decomposition]]"
  - "[[jira-commit]]"
---

# Decision Log — 2026-07-31 — Bulk Creation Mode

**What was decided:** add **bulk creation mode** to the `ai-refinement`
flowspace — a path for the user who already holds the item set and needs it
drafted to house standard and created, rather than refined one item at a time.
It is gated behind an explicit acknowledgment, separate from every other
confirmation in the flow, that bulk creation is to be used carefully and that
AI-generated items may be wrong and must be reviewed. **By whom:** agent, on
direct operator instruction. **What it affects:** an eighth house amendment in
`reference/ai-refinement-hybrid.md` (1.4 → 1.5), `HUB.md` (1.17 → 1.18), all
six stage contracts, `reference/work-item-schemas.md` (1.5 → 1.6), a new skill
staged for review (`bulk-child-creation` 1.0), and two promoted skills
(`jira-commit` 1.9 → 1.10; `value-decomposition` 1.0 → 1.1, `verified` →
`to-review`).

## The gap this closes

The pipeline's founding premise — `HUB.md`'s "one run = one fully refined work
item committed to Jira" — is correct for what it was designed for: a rough
idea, a vague request, a document with a problem buried in it. It is wrong for
a case the operator actually hits, and hits often: a spreadsheet of tasks, an
exported work breakdown, a solution epic whose child features are already
known, a decomposition that just produced fourteen accepted stories. The work
of *deciding what the items are* is finished before the flow starts.

Two things blocked that case, and both were deliberate rather than
accidental — which is why this needed a decision rather than a fix:

1. **`jira-commit` refused bulk by contract.** `SKILL.md` boundary: "Not a
   bulk-import or migration tool — one signed-off item per commit," with the
   description declining bulk explicitly.
2. **There was no list-ingest path.** All nine source-input taxonomy rows were
   prose "pasted or summarized into the session." Nothing read a spreadsheet,
   and nothing distinguished *a list of items* from *one item's description*.

The user's options were therefore N full Band ② runs, or abandoning the flow
and hand-creating in Jira — which loses the schema enforcement, the mandatory
labels, the persona, and the audit trail that are the pipeline's entire
purpose. The second option is what actually happens under time pressure, so
the flow was losing exactly the work it most wanted to govern.

## Design decisions

1. **A separate axis, not a widening of fast-track.** Fast-track already
   exists and already means something precise: *compressed review for one
   item*, folding Stages 03–05 into one checkpoint. Bulk answers a different
   question — *how many items does one pass produce*. Overloading "fast-track"
   would have drifted six stage contracts, three skills, and the 2026-07-03
   fast-track decision log, all of which use the term in its existing sense.
   The two modes compose: a bulk pass over richly-specified rows is also
   fast-track-shaped, and Stage 01 assesses them as two independent questions
   at steps 10a and 10b.

2. **A mode inferred and *proposed*, never selected.** Per operator
   instruction, the agent infers bulk applicability from the shape of the
   input rather than waiting for a command. But inference drives a proposal
   with a stated item count, per-row type reading, and reasoning — never an
   action. This matches how fast-track and work-item type selection already
   behave, and keeps the mode from being something that happens *to* a user
   who pasted a long document.

3. **The set-versus-item test, written as the mode's primary near-miss.** The
   most likely and most damaging misfire is reading one complex item's twelve
   scope bullets as twelve work items. The test — *would each row stand alone
   as a work item with its own acceptance criteria?* — is stated in the house
   amendment, Stage 01, the skill spec, both adapters, and the HUB taxonomy
   row, with a worked example in each of the longer ones (three switch
   upgrades with their own site lists are three items; "update firmware /
   validate routing / confirm monitoring / roll back if BGP fails" under one
   upgrade is one item). Where the reading is genuinely ambiguous, the agent
   states which reading it took before drafting anything.

4. **The acknowledgment is a separate act, not a bundled one.** The operator's
   requirement was a clear confirmation that bulk creation should be used
   carefully and that AI-generated items may not be correct. Implemented as:
   distinct from Stage 01's general responsibility notice, *and* distinct from
   the mode-selection question itself — the user answers the mode question,
   then acknowledges, as two acts, because a single "yes" covering both is
   exactly the shape that lets a consequential confirmation slide past
   unnoticed. Taken per bulk pass, never carried forward. It states five
   things: the count, that one approval creates all of them, that the items
   are AI-drafted and may be wrong (and *more* likely wrong than in
   single-item mode, since drafting is shallower per item — stated in that
   direction deliberately), that team review is required before work starts
   with the provenance label as the pending-review flag, and that creation is
   not reversible. Stage 06 restates the caution at the batch preview with the
   concrete final count, so the user meets it again at the moment of approval
   rather than only at intake.

5. **Anti-fabrication is the mode's load-bearing rule, not a quality
   aspiration.** Per operator instruction: the agent drafts from provided
   context and **stops when the detail runs out**, reporting the item as
   underspecified with its specific missing fields named. It never pads a thin
   row into a full-looking work item. The reasoning recorded here because it
   drove the design: at batch volume, a fabricated item is indistinguishable
   from a grounded one at review time — forty plausible items where fifteen
   were invented is a worse output than twenty-five with fifteen honestly
   flagged, because the reviewer has no signal telling them where to look.
   This is why bulk creation is a distinct skill with its own review criteria
   rather than a flag on the existing pipeline: the behavior that makes it
   safe has no analogue in single-item refinement, where an unfillable field
   simply enters the elicitation queue.

6. **Suggested next items: opt-in, separated, warned.** Per operator
   instruction, having stopped at the edge of the evidence the agent may offer
   to suggest further likely items, drawing on the value-delivery model,
   general domain knowledge, and internet sources. Three constraints, all
   non-optional: offered as a question and never produced unasked; kept a
   structurally separate labelled set through review, validation, and creation
   so a reviewer can always tell which items came from their own material; and
   carrying an explicit warning that these are inferred and need close
   attention on relevance and accuracy — a stronger caution than the batch
   acknowledgment, because these items have no grounding in anything the user
   supplied. Internet sources are read-only, cited, and vetted as third-party
   material on the same terms as vendor documentation; anything that cannot be
   cited is not used. This also introduces the flowspace's first outbound
   research surface beyond Confluence/Jira, noted below as an operator item.

7. **Two carve-outs narrow to batch scope — explicitly, and only here.** Both
   were previously absolute, and both are recorded as narrowings rather than
   left to erode silently:
   - **`parent_mapping_confirmation`.** Bulk confirms the parent once for the
     batch ("all N items take parent X") as one explicit act, and validates
     the created set against it at the **end of the pass** rather than before
     each create. The operator's reasoning, adopted here: a parent link is
     editable after creation, so an incorrect batch parent is a correction,
     not the irreversible mis-assignment the amendment (NEADD-1827, defect 2)
     was written to prevent. What does not relax: the confirmation is still
     explicit rather than a silently carried-forward Stage 01 position, and a
     row naming a *different* parent falls out of the batch default and gets
     its own confirmation.
   - **`due_date_elicitation`.** Per operator instruction, the **parent's due
     date is the focus first** — where the set sits beneath a parent carrying
     one, that date is the batch's reference point and is stated as such,
     since the parent's commitment is what the children serve. A user-supplied
     sheet's per-row due-date column is treated as user-committed and used as
     given: the user authored the sheet, so this is not the agent inferring a
     date. Absent both, one date is elicited explicitly for the batch. The
     part that does not narrow: a date the agent derives from prose remains a
     reference point only, never a commitment.

8. **No new stages; the mode changes the shape of existing ones.** Following
   the fast-track precedent rather than inventing a parallel pipeline. Band ③
   is a named alternative path through the same stage contracts: Stages 02–04
   fold into the skill's batch-draft pass, Stage 05 validates per item across
   the batch, Stage 06 commits behind one preview and one approval. This kept
   the change to edits within existing contracts instead of a new stage
   hierarchy, and means an underspecified item can be routed into an ordinary
   Band ② run without crossing a structural boundary.

9. **A failing item falls out of the batch; it does not fail the batch.**
   Stage 05 pulls halt-level items and lets the rest proceed, reporting each
   defect specifically. The alternative — failing the whole set on one bad
   row — would push users toward accepting whatever the agent produced rather
   than flagging problems.

10. **Halt on failure during creation, with no rollback and no pretence of
    one.** Sequential creation with a running result table; on any failure the
    batch stops rather than continuing into the remaining items, reports
    precisely what was and was not created, and offers resume-or-abort. There
    is no rollback mechanism, and rather than build a fragile one, the
    acknowledgment and the batch preview both state plainly that creation is
    irreversible. The failure mode being designed against is a user left
    uncertain about what landed in Jira.

11. **A Markdown handoff document as the degrade path.** Per operator
    instruction: where the native tooling cannot create the items — no write
    path, insufficient permissions, repeated failures — the pass offers a
    human-readable Markdown file carrying the full drafted set, structured so
    a fresh session can pick it up and finish without re-deriving anything.
    This extends the existing degrade-path pattern (`jira-commit` 1.8's
    preview-only terminal output, `START-HERE.md`'s capability probe) rather
    than inventing one, and is explicitly a valid terminal output rather than
    a failure state.

12. **Native Rovo tooling first.** Per operator instruction, and consistent
    with `jira-commit` 1.2's engine-native-first commit path: Rovo's built-in
    Jira MCP actions are the primary path, the sanctioned connector the
    fallback for Copilot. Nothing in the method is Rovo-specific.

13. **`jira-commit`'s bulk boundary split rather than dropped.** The skill
    keeps refusing bulk import, migration, and edits of issues that **already
    exist** — bulk-closing, bulk-labeling, bulk-transitioning, loading a
    backlog into existing records — at any volume. What it now accepts is the
    per-item commits of a **newly drafted** set that passed validation and one
    batch approval. The test is whether the items exist yet. Each commit in a
    batch remains a full commit, answerable to the same review criteria — not
    a reduced import path. This preserves the boundary's original intent (this
    skill is not a migration tool) while removing the blanket refusal that
    made bulk creation impossible.

14. **`value-decomposition` offers the bulk destination rather than assuming
    it.** Its step 8 previously sent every accepted child into its own Band 2
    run. It now offers a bulk pass for a set large enough that N runs would be
    disproportionate — offered, never selected — and its boundary list gains
    "not the bulk creator," since a set arriving already decided should reach
    `bulk-child-creation` directly without passing through decomposition at
    all. Its one-level-per-pass, vertical-slice, MVP, and value-statement
    rules are untouched.

## Truth-level movements

- `value-decomposition` drops `verified` → `to-review`. Its first behavior
  change since promotion, logged rather than assumed clean.
- Stages 02, 03, and 04 drop `verified` → `to-review` for the same reason.
- `jira-commit`, Stages 01/05/06, `HUB.md`, `ai-refinement-hybrid.md`, and
  `work-item-schemas.md` were already `to-review`; they stay there with the
  gate re-run obligation growing.
- `bulk-child-creation` is staged in `skill-foundry/review-skills/` at
  `to-review`. It is **not** promoted, not placed in `produced-skills/`, and
  not gated — that is the operator's act (AGENTS.md rule 5).

## Incidental fix

The provenance label's illustrative value read `refine-ai-flow-v1.14` in
`ai-refinement-hybrid.md`, `work-item-schemas.md`, and Stage 01 while `HUB.md`
had advanced to 1.17. The *rule* was always correct — the label carries the
flowspace's own `artifact-version` — so this was drift in the examples, not in
the behavior. All three now read `refine-ai-flow-v1.18`, matching this
change's `HUB.md` bump. This is also why `jira-commit`'s adapters needed
regenerating independently of its own spec change, per the maintenance
coupling that skill's 1.9 changelog flagged.

## Remaining for the operator (the human gate)

1. **Run the five-point gate on `bulk-child-creation`** and decide on
   promotion. The spec review, per-adapter live test, trigger check (the
   set-versus-item near-miss especially), and collision check against
   `value-decomposition`, `jira-commit`, and `jira-portfolio-ingest` are all
   owed. Nothing here has run on-engine.
2. **Confirm the two carve-out narrowings** (design decision 7) are
   acceptable. This is the most consequential call in the change: both rules
   were previously absolute, and fast-track was explicitly forbidden from
   touching either.
3. **Decide whether bulk-created items need a batch-identifying label.**
   Deliberately not minted here — it would touch `mandatory_labels`, and the
   run result table plus this log already record the batch. Raised as an open
   question rather than answered.
4. **Confirm the proposal threshold.** The skill proposes bulk for a set of
   three or more discrete items. The number is a starting point, not a
   derived value.
5. **Scope the new internet-research surface.** Design decision 6 introduces
   the flowspace's first outbound research beyond Confluence/Jira, in the
   optional suggested-items step only. The instantiation guide (REC-02's
   knowledge scoping) and the on-engine validation checklist (REC-09's matrix)
   do not cover it, alongside the existing gap for the Confluence read
   surface added 2026-07-21.
6. **Decide whether the spreadsheet ingest contract should move.** The
   parsing rules are cited from
   `flow-foundry/review-flowspaces/portfolio-rationalization/reference/export-and-field-requirements.md`
   §6 and `skill-foundry/review-skills/jira-portfolio-ingest/SKILL.md` — both
   unpromoted `to-review` artifacts in review queues. Citing a design rather
   than duplicating it was the right call for this change, but if
   `portfolio-rationalization` is never promoted, these rules need a permanent
   home.
