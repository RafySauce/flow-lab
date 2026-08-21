---
id: ai-refinement-stage-06
title: "Stage 06 — Jira Commit & Close"
type: stage-context
stage: 6
review-intensity: heavy
artifact-version: "1.12"
status: living
truth-level: to-review
created: 2026-07-03
updated: 2026-08-21
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.1"
data-class: public
related:
  - "[[ai-refinement]]"
  - "[[jira-commit]]"
  - "[[bulk-child-creation]]"
---

# Stage 06 — Jira Commit & Close

## Inputs

| Input | Source | Required |
|---|---|---|
| Validated + formatted work item payload | Stage 05 | Yes |
| User sign-off confirmation | Stage 05 | Yes |
| Work item type + hierarchy position | Stage 01 | Yes |
| Classified dependency list | Stage 03 | Yes |
| Stakeholder tags + coalition / conflict-axis annotations | Stages 02, 03 | Yes |
| Candidate parent items (queried live from the target instance) | Jira (via native lookup) | If applicable |
| Confirmed parent choice (confirm / skip / create-new) | User | If applicable |
| Resolved team_code + session planning quarter (+ any Stage 05 label bypass) | Stage 01 (+ Stage 05) | Yes |
| Selected creation mode (bulk / single-item) + bulk acknowledgment record | Stage 01 | Yes |
| Per-item validation table + fallout list | Stage 05 | If bulk |
| Batch-scope answers (intended parent, due-date anchor) | Stage 01 | If bulk |

## Process

`Layer-3: jira-commit` (skill spec in
`produced-skills/jira-commit/`, `to-review` as of 1.11 — content change
2026-08-05, re-gate owed; previously re-gated and promoted 2026-08-01 on a
confirmed Rovo live test)

0. **API preflight — before the first write call of the session.** Read the
   actual function signature or stub for every write API this run will call
   (create issue, update issue, transition issue, create issue link, add
   comment) before calling it for the first time. Parameter naming for the
   same underlying Jira REST operation varies by platform and engine
   integration; a name guessed from convention is a wasted round-trip, not a
   reasonable default. This is the flowspace's `commit_boundary_hardening`
   house amendment (`../reference/ai-refinement-hybrid.md`).
1. **Field mapping, registry-driven, format-translated, capability-tested** —
   translate the refined field key-value pairs into Jira field IDs, the field
   set read from the selected type's schema in
   `../reference/work-item-schemas.md`:
   - Standard fields: summary, description, due date, issue type — for `bug`,
     `description` carries steps to reproduce, expected result, actual
     result, and (where known) severity and environment as prose, per the
     registry's Extension field definitions
   - Custom fields (per the type's registry schema): problem_statement, business_outcomes, customer_business_value, in_scope, out_of_scope, type_of_work, work_category, acceptance_criteria, question_to_answer, timebox (spike — map or create at instantiation per the registry), app_code, root_cause (bug — map or create at instantiation per the registry)
   - **Field-capability test** (`commit_boundary_hardening`): for each custom
     field, test its actual accepted format in a defined fallback order —
     rich ADF payload first, then plain text, then folding the content into
     `description` with the gap explicitly named — instead of defaulting
     straight to the `description` fallback because a field's metadata
     looked ambiguous (e.g. typed `string` rather than `doc`). Folding
     structured content into `description` as a blanket "safe" choice
     without testing the field first is the defect this replaces; the
     fallback is a last-resort, per-field outcome, not a default.
   - Format-translation gate: convert the payload's Markdown structure
     (headings, bullet lists, code blocks) into the target platform's native
     markup — Atlassian Document Format (ADF) for Jira Cloud — before mapping
     any rich-text field. Raw Markdown syntax landing in a Jira field is a
     defect; Stage 05's "no bold, no emojis" pass does not translate
     structural markup, so this stage owns the translation. This is the
     flowspace's `format_translation_gate` house amendment
     (`../reference/ai-refinement-hybrid.md`).
2. **Hierarchy linkage — hard carve-out, never skipped; batch-scoped in bulk
   mode only.** Resolve parent-child relationships. Parent mapping is default
   behavior for every type this stage commits except `portfolio_epic` (top of
   the refinable set — no parent within scope). This step is never compressed
   or skipped by fast-track mode — the mode selected at Stage 01 governs how
   many Stages 02–05 fields were extracted versus elicited; it has no bearing
   here.

   **Hierarchy validation, before any parent-link write** — validate the
   proposed parent-child relationship against the target project's actual,
   live-queried issue-type hierarchy levels: `parent.hierarchyLevel ==
   child.hierarchyLevel + 1`. This registry's `children:` relationships
   (`../reference/work-item-schemas.md`) encode design intent; a real
   project's configured hierarchy can diverge from it, and attempting the
   write before checking turns a preventable mismatch into a failed API
   call. On a validation failure, halt before attempting the write and
   present structurally valid alternatives — create as top-level and link
   to the intended parent instead, change the item's type to one that fits
   the hierarchy, or ask the operator how to restructure — rather than
   surfacing only the raw API error. This is the flowspace's
   `commit_boundary_hardening` house amendment
   (`../reference/ai-refinement-hybrid.md`).

   **In bulk creation mode** the confirmation is taken once for the batch
   rather than once per item, and validated at the end of the pass rather than
   before each create — the narrowing the `bulk_creation_acknowledgment`
   amendment defines, applying in this mode and nowhere else. Candidate
   parents are queried and presented exactly as below; the user confirms
   **"all N items take parent X"** as one explicit act; and step 7a validates
   the created set against that parent once creation completes. This is
   sufficient here, and only here, because a parent link is editable after
   creation — an incorrect batch parent is a correction, not the irreversible
   mis-assignment the amendment was written to prevent. Two things do not
   relax: the confirmation is still explicit (never a silently carried-forward
   Stage 01 hierarchy position), and a row whose content names a **different**
   parent falls out of the batch default and gets its own confirmation rather
   than being absorbed.
   - Query the target instance for existing candidates of the appropriate
     parent type (portfolio epics for a solution epic; solution epics for a
     feature; the epic's existing features for a story/task/spike/bug).
   - Present the candidates to the user (key, summary, status) and obtain
     one of: confirm a specific parent, skip (no parent yet), or request a
     new parent be created (spawns a new Band 2 run for that type; this
     commit resumes once the new parent exists).
   - If creating a solution epic under a portfolio epic: set parent link (or
     the instance's epic-of-epic mechanism, per its configuration). If
     creating a feature under a solution epic: set epic link. If creating a
     story/task/spike/bug under a feature: set parent link. Set the link only
     after the user's explicit confirmation — never from an unconfirmed
     Stage 01 hierarchy position. This is the flowspace's
     `parent_mapping_confirmation` house amendment
     (`../reference/ai-refinement-hybrid.md`).
   - Validate that the parent exists in Jira.
3. **Dependency linkage** — create Jira issue links for blocking dependencies identified in Stage 03.
4. **Labeling** — apply the Stage 02 stakeholder tags and Stage 03 coalition /
   conflict-axis annotations as Jira labels (or the instance's designated
   fields), so the item is taggable per the stakeholder register's usage
   rules. Additionally apply the flowspace's `mandatory_labels` house
   amendment (`../reference/ai-refinement-hybrid.md`): `refine-ai-flow-v
   <version>` (this flowspace's own `artifact-version`, stated by Stage 01
   at session start — no query) on every item, and — for `feature`, `story`,
   `task`, `spike`, `bug` only — the session's resolved
   `<team_code>-<yyyy>-q<n>` planning label from Stage 01 (`portfolio_epic`/
   `solution_epic` are exempt from the second label). If Stage 05 recorded an
   explicit user bypass of a missing or malformed label, carry that exception
   forward rather than fabricating a value — it gets surfaced, not silently
   resolved, in step 5's preview.
5. **Dry-run preview** — present the full payload to the user in its
   translated, rendered form (native markup, not raw Markdown source) before
   committing. Surface the provenance label (`refine-ai-flow-v<version>`)
   alongside its purpose — a pending-review flag the team removes once their
   review is complete — so the preview, not just Stage 01's earlier notice,
   is where the user last sees why it's there. For a gated type, also surface
   the resolved planning label (and, if Stage 05 recorded a bypass, that
   exception plainly) and offer a per-item quarter override — the rare item
   that targets a different quarter than the session default — before commit.

   **In bulk creation mode this becomes one batch preview covering the whole
   approved set**, and it is the second of the mode's two acknowledgment
   points. Present: the items to be created with their key fields in rendered
   form; the labels every item will carry; the confirmed batch parent; the
   fallout list from Stage 05 (validation failures and underspecified items,
   with their defects) so the user sees what is *not* being created; and the
   suggested-item set kept visibly separate from the grounded set. **Restate
   the bulk caution here with the concrete final count** — that this single
   approval creates all N items, that they are AI-drafted and need team review
   before work starts, and that creation is not reversible by this flow. One
   approval covers the set; there is no per-item approval in this mode, which
   is precisely what the Stage 01 acknowledgment covered.
6. **Commit** — execute through the engine's native Jira capabilities first
   (Rovo built-in create/update issue and issue-link actions); the sanctioned
   Jira integration is the fallback for engines without them (Copilot).

   **In bulk mode, create sequentially and halt on failure.** Maintain a
   running result table — item, key, URL, status — visible as creation
   proceeds. On any failure, stop the batch rather than continuing into the
   remaining items; report precisely what was created and what was not; then
   offer resume-from-failure or abort. There is no rollback: items already
   created stay created, which the Stage 01 acknowledgment and the step 5
   preview both stated before approval. The user must never be left uncertain
   about what landed in Jira.

   **No write path available at all** (neither a native engine action nor a
   sanctioned connector — the same condition Stage 06 already handles for
   single items): in bulk mode, offer to produce a **Markdown handoff
   document** carrying the full drafted set — one section per item with every
   field under its schema name, the labels that would have been applied, the
   intended parent, the underspecified rows with their named gaps, and the
   suggested set kept separate — structured so a fresh session can pick it up
   and finish the job without re-deriving anything, and stating plainly at the
   top that nothing was created and why. This is a valid terminal output of
   the stage, not a failure state.
7. **Confirm success** — return the created issue key and URL to the user; in
   bulk mode, the completed result table for the whole set.

   7a. **Post-creation parent validation (bulk mode).** Validate the created
   set against the batch parent confirmed at step 2 — the end-of-pass check
   that the batch-scoped narrowing relies on. Report any item whose parent did
   not attach, and correct it directly rather than leaving it silent; parent
   links are editable, which is what makes end-of-pass validation sufficient
   in this mode. Close by restating that every created item carries
   `refine-ai-flow-v<version>` as a pending-review flag and needs team review
   before work starts.

   7b. **Post-commit field audit (both modes).** Re-fetch every issue this
   pass created — the single item in single-item mode, every created item in
   bulk mode — and verify each schema-required field for its type, per
   `../reference/work-item-schemas.md`, is actually populated, alongside the
   mandatory labels and the due date. This catches exactly the gap between
   "the field was built" and "the field was included in the create call" —
   content the agent constructed upstream but never mapped in step 1 (e.g.
   folded into `description` by an untested fallback, or dropped from the
   payload silently). Report any gap to the operator before declaring the
   commit complete; a gap found here is a defect to fix (a follow-up update
   call), not a note for later. This is the flowspace's
   `commit_boundary_hardening` house amendment
   (`../reference/ai-refinement-hybrid.md`).
8. **Offer status transition** — ask whether to move the item to In Progress
   (or the board's equivalent active status); execute via the engine's native
   Jira capabilities on confirmation, leave the default status on decline.
   This is the flowspace's `post_commit_transition_offer` house amendment
   (`../reference/ai-refinement-hybrid.md`). In bulk mode the offer is made
   once for the batch, not once per item — still offered once, still no
   transition without an explicit "yes," and a set whose items should start in
   different states is transitioned individually in Jira rather than here.
9. **Session loop decision**:
   - "Refine another" → loop back to Stage 02 with session context retained
   - "Done" → close session, produce session summary

   After a bulk pass, the loop offers the same choices plus routing any
   underspecified or fallout item into its own Band ② run, since those are the
   items most likely to need real refinement rather than another batch.
10. **Context-budget marker** — per the `session_budget_checkpoint` house
    amendment (`../reference/ai-refinement-hybrid.md`), self-query and state
    context-window usage at this stage's exit (and after every bulk-creation
    sub-batch, per `bulk-child-creation` step 10): "Stage 06 — context
    remaining: ~<percent>%." Informational only at 50%; an escalating
    quality-degradation advisory at 60% and 70%; past 80%, and if the loop
    decision (step 9) was "refine another," stop and produce the handoff
    defined in `../reference/session-continuation-handoff.md` instead of
    looping back to Stage 02.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Created Jira issue key + URL | User | Link |
| API response confirmation | Run decision log | JSON |
| Session summary (if closing) | User / audit | Structured summary |
| Batch result table (item, key, URL, status) + not-created list | User; run decision log | Structured per-item table |
| Markdown handoff document (bulk mode, no write path) | User / a fresh session | Markdown file |
| Post-commit field audit result (per created item) | User; run decision log | Structured pass/gap list |

## Verify

Cross-stage trace: the committed payload must match Stage 05's signed-off
payload field-for-field, aside from format translation (nothing of substance
altered between sign-off and commit), and every blocking dependency from
Stage 03's classified list must appear as a Jira issue link — the failures
these catch are post-sign-off content mutation and dropped dependency links.
Running these checks leaves a one-line result in the run's decision log.

- [ ] Function stubs for every write API used this session were read before
      the first write call — no parameter name was guessed from convention
- [ ] All required Jira fields are mapped (no unmapped required fields);
      each custom field's capability was tested in the ADF → plain-text →
      description-with-gap-named order, not defaulted straight to
      `description`
- [ ] Committed payload matches the Stage 05 signed-off payload (content
      unchanged; only markup was translated to the platform's native format)
- [ ] No raw Markdown syntax (heading markers, list markers, code fences)
      remains in any committed field
- [ ] For applicable types, candidate parents were presented and the user
      explicitly confirmed, skipped, or requested a new parent — never a
      silently-carried-forward hierarchy position
- [ ] Before any parent-link write, the relationship was validated against
      the target project's live-queried hierarchy levels
      (`parent.hierarchyLevel == child.hierarchyLevel + 1`); a mismatch
      halted before the write and presented structurally valid alternatives
      rather than surfacing a raw API error
- [ ] Parent item exists in Jira (if hierarchy linkage applies)
- [ ] Every Stage 03 blocking dependency has a Jira issue link
- [ ] Stakeholder tags / annotations applied as labels
- [ ] `refine-ai-flow-v<version>` label present on the committed item, and the
      dry-run preview surfaced its purpose (pending-review flag, removed by
      the team once reviewed)
- [ ] For `feature`/`story`/`task`/`spike`/`bug`, the
      `<team_code>-<yyyy>-q<n>` planning label is present and well-formed —
      or an explicit Stage 05 bypass is recorded and was shown plainly in the
      dry-run preview, never fabricated
- [ ] Dry-run preview was shown in rendered (native-markup) form and user approved
- [ ] Jira API returned success (issue key received)
- [ ] User was offered the post-commit status transition (accept or decline
      recorded)
- [ ] User was offered loop/close decision
- [ ] In bulk mode, the batch preview restated the caution with the concrete
      final count, showed the fallout list (what is *not* being created), and
      kept suggested items visibly separate from grounded ones
- [ ] In bulk mode, the parent was confirmed once as an explicit act ("all N
      items take parent X"), any differently-parented row was surfaced
      individually, and step 7a validated the created set against that parent
- [ ] In bulk mode, creation was sequential with a running result table, and
      any failure halted the batch with a precise account of what was and was
      not created plus a resume-or-abort offer — no silent continuation
- [ ] In bulk mode with no write path, the Markdown handoff document was
      produced, stated plainly that nothing was created and why, and carried
      the full set structured for a fresh session to finish
- [ ] Every created item (single item, or each item in a bulk set) was
      re-fetched and its schema-required fields, labels, and due date were
      confirmed actually populated before the commit was declared complete;
      any gap found was reported and fixed, not left for later discovery
- [ ] Context-remaining marker was stated at stage exit, with the correct
      threshold advisory (or handoff, past 80%) attached if usage warranted it

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy, unconditionally — this is the commit boundary. An
  incorrect API payload creates real Jira artifacts that require manual
  cleanup. Fast-track mode never compresses this stage's review, same as
  Stage 01 — the Stage 03–05 consolidation (Stage 05's Review section) stops
  at Stage 05 and never reaches into Stage 06. Bulk mode does not compress it
  either: the batch preview is a heavy review of the whole set, and the
  stakes are higher here than in a single-item run, not lower — N artifacts
  requiring manual cleanup instead of one, with no rollback.
- **Evidence:** the approved dry-run preview, the API response captured in the
  run's decision log, and the returned issue key.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- Jira API payloads contain `internal` data — transmitted over authenticated, encrypted channels only.
- Issue keys and URLs are `internal` — shareable within the organization.
- API credentials are handled by the platform (Rovo/Copilot) — never included in flowspace artifacts.
- The hierarchy-validation query (target project's issue-type hierarchy
  levels) and the post-commit field-audit re-fetch are additional read-only
  calls, the same access class as the existing parent-candidate query —
  neither is a write action.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
