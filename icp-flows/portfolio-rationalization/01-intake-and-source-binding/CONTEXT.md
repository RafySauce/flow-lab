---
id: portfolio-rationalization-stage-01
title: "Stage 01 — Intake & Source Binding"
type: stage-context
stage: 1
review-intensity: heavy
artifact-version: "1.2"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-08-01
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[export-and-field-requirements]]"
  - "[[work-item-schemas]]"
---

# Stage 01 — Intake & Source Binding

## Inputs

| Input | Source | Required |
|---|---|---|
| Trigger phrase ("Run Portfolio Rationalization", "Start a portfolio review", "Rationalize the backlog") | Operator | Yes |
| Target Jira project or space name | Operator | Yes |
| Source mode declaration — live Jira or export | Operator | Yes |
| Optional JQL narrowing filter | Operator | No |
| Expected item count (for the parse/pagination check) | Operator | Yes |
| Export file (CSV/XLSX), when source mode is export | Operator | Conditional — required in export mode |
| Live Jira read access to the named project/space | Engine-native Jira capability | Conditional — required in live mode |
| Field requirements, parity contract, degraded-signal table, denominator rule | `../reference/export-and-field-requirements.md` | Yes |
| Session capability-probe result (Jira connector present or absent) | `START-HERE.md` Step 1, carried in as session context | Yes |
| Prior cycle's field-availability report and denominator, if this is not the first cycle | Instance `decision-log/` | No |

## Process

`Layer-3: TBD — skill-primer-brief filed (sp-jira-portfolio-ingest)`

1. **Trigger and scope declaration.** Recognize the trigger phrase. Ask the
   operator for the target project or space, the source mode, any JQL
   narrowing, and the expected item count. Record the scope verbatim — a scope
   change between cycles invalidates cycle-over-cycle comparison, and the
   record is what lets a later reviewer see that it changed.
2. **Announce what this cycle will and will not do.** State plainly, before any
   data moves: this flow reads Jira and writes nothing; its output is a triage
   recommendation for human review, not a closure decision. Say it here so no
   participant downstream is surprised by a packet labeled `Close
   (recommended)`.
3. **Bind the source.**
   - **Live mode:** query the named project/space read-only via the engine's
     native Jira capability, applying the JQL filter if given. Page through to
     completion and confirm the returned count matches the query's reported
     total. A silent truncation corrupts every distribution downstream — halt
     on mismatch.
   - **Export mode:** parse the file with a real CSV/XLSX reader honoring
     quoted fields (embedded newlines in descriptions and comments are routine
     — a naive line-split produces phantom rows). Capture the header row before
     parsing bodies. Collapse repeated same-header columns (labels, comments,
     links) into one canonical field each.
   - **Degrade path** (`START-HERE.md`): the capability probe found no Jira
     connector and the operator has no export → ask the operator to paste the
     item set directly, in whatever shape they have it, and normalize from
     that. State plainly which fields the pasted shape lacks; a pasted set
     typically carries Summary and Status and little else, which degrades
     Stage 03 heavily. Record the degradation, run anyway.
4. **Data-class screen — before typing the data any further.** Run the intake
   screen per `../reference/export-and-field-requirements.md` §7. Exports are
   the higher-risk carrier: every column comes along, and comments and custom
   fields routinely carry personal names, customer references, hostnames, and
   occasionally credentials. Content above the instance's sanctioned ceiling
   (`internal` by default) **halts the run** — it is not redacted and carried
   forward, because redaction at portfolio volume is not reliably verifiable.
   Assignee names are expected and permitted at `internal`.
5. **Confirm the item count** against the operator's stated expectation. A
   mismatch halts: it means the scope, the filter, or the parse is wrong, and
   every count in Stage 02 would be wrong with it.
6. **Map the source's fields onto the canonical field set** in
   `../reference/export-and-field-requirements.md` §2. Jira field names vary by
   configuration; this mapping is what makes live and export modes produce
   identical downstream shapes. Present the mapping to the operator for
   confirmation — an auto-mapped field that is subtly wrong (a custom
   "Outcome" field mapped to Business Outcome when it means something else)
   poisons Stage 03 invisibly.
7. **Check the hard requirements.** Issue key, Summary, Status, Created, and
   Updated must all be present. Any absent → halt, naming which.
8. **Build the field-availability report.** For every canonical field: present
   or absent, and for present fields, how many items actually populate it. This
   is what tells Stage 03 whether it is mapping on rich text or on summaries
   alone, and what tells Stage 04 whether staleness can use comment timestamps.
9. **Capture the completion denominator** — the count of §2's canonical fields
   that resolved in this cycle's field map (step 6), per §4 of the
   requirements file. Not the source's raw column count: a raw export or live
   project routinely carries fields this flow never reads, and those don't
   belong in the denominator. Do not carry forward a prior cycle's
   denominator, and do not hardcode one. Record it, and which canonical fields
   (if any) were unavailable this cycle, alongside the item count.
10. **Emit the normalized item set.** One record per work item, canonical field
    names, values normalized (dates to ISO, empty-equivalents like `None` and
    `-` and empty rich-text containers resolved to genuinely empty).
11. **Discover connected spaces — the ART-board pattern.** A backlog's
    portfolio and solution epics often do not live in the project or space
    just bound: an overarching ART (Agile Release Train) board commonly holds
    the portfolio/solution epics that drive strategic goals across several
    feature-delivery team projects, each with its own board. Before this
    cycle's scope is treated as complete, check whether this backlog's own
    hierarchy reaches outside it.
    - Group every populated `Parent key` value in the normalized set by its
      issue-key project prefix. Any prefix that differs from the primary
      scope's own project/space is a **candidate connected space**.
    - If no `Parent key` values are populated, or every one resolves to the
      primary project's own prefix, say so plainly and move to step 12 —
      there is nothing to discover this cycle.
    - Otherwise, present the candidate list to the operator: each distinct
      external prefix, how many in-scope items reference it, and (where
      `Issue Type` is available) what level those referencing items sit at.
      Offer the choice explicitly — **resolve** the specific referenced
      parent keys to complete the hierarchy for Stage 02, or **decline** and
      leave those references unresolved this cycle. Either answer is valid;
      this is the same offer-and-wait discipline Stage 02 uses for its
      exploration lenses, not a default to talk the operator out of.
    - **If the operator elects to resolve:** look up the named parent keys
      only — read-only, through the engine's native Jira capability, or by
      asking the operator to paste the resolved items if no such capability
      exists. This is a **targeted lookup of specific keys, never a second
      whole-project or JQL query** — the one-project-per-cycle discipline
      (`../reference/export-and-field-requirements.md` §5) still governs the
      *primary* scope; a connected space is read only far enough to complete
      the hierarchy, nothing more. Walk each resolved item's own `Parent key`
      upward the same way, deduping keys already resolved, until an item
      carries no `Parent key` (top of the hierarchy) or a lookup fails. The
      hierarchy `../../ai-refinement/reference/work-item-schemas.md` defines
      is four levels deep at most, so this walk always terminates. A key that
      fails to resolve is recorded **unresolved**, not retried, and discovery
      continues.
    - Run the same data-class screen (step 4) against anything resolved this
      way before it joins the cycle. A connected space earns no lower-trust
      exemption for being "just parent context."
    - Record what resolves as a **connected-space hierarchy context** —
      Issue key, Issue Type, Summary, Parent key, and Status only, the
      minimum Stage 02 needs to draw a parent chain. **These items never join
      the primary normalized item set or its count.** They carry no
      status/assignee/priority/due-date distribution, no objective mapping,
      no close score, no disposition packet — their sole purpose is
      completing parent chains in Stage 02's hierarchy view.
    - Record the discovery outcome — no candidates found; candidates found
      and resolved; candidates found and declined — in the cycle scope
      record, along with the connected-space list and item count when
      resolved.
12. **Confirm setup with the operator** — scope, source mode, item count,
    denominator, field map, degraded-signal list, and the connected-space
    discovery outcome — and obtain explicit "proceed" before advancing.

## Outputs

| Output | Consumed by | Format |
|---|---|---|
| Normalized item set | Stages 02, 03, 04, 05 | One record per item, canonical field names, ISO dates, empties resolved |
| Field-availability report | Stages 02, 03, 04 | Per canonical field: present/absent + populated-item count |
| Completion denominator (count of §2 canonical fields resolved this cycle) | Stage 02 | Integer (≤19), with which canonical fields (if any) were unavailable |
| Confirmed item count | Stage 02 | Integer |
| Cycle scope record (project/space, JQL filter verbatim, source mode, run date) | Stages 05, 06; instance decision log | Text |
| Degraded-signal list (which fields are missing and what each degrades) | Stages 02, 03, 04, 05 | Field → consequence table |
| Data-class screen result | Instance decision log | Pass, or halt with cause |
| Connected-space discovery outcome (no candidates / resolved / declined) | Stage 02, instance decision log | Text, plus the connected-space list when resolved |
| Connected-space hierarchy context (conditional — present only when discovery resolved candidates) | Stage 02 (hierarchy view only) | Key, Issue Type, Summary, Parent key, Status — never added to the primary item set or its count |

## Verify

Cross-stage trace: the item count and canonical field names Stage 01 emits are
the item count and field names Stage 02 profiles. Check that the normalized
item set's record count equals both the operator's stated expectation and the
source's own reported total, and that every canonical field Stage 02's
distributions reference appears in the field-availability report as either
present or explicitly absent. The failure this catches is Stage 02 profiling a
silently truncated item set — a paginated query that stopped early, or an
export whose embedded newlines split rows — and reporting distributions over a
portfolio that is not the portfolio. Running this check leaves a one-line
result in the cycle's decision log. Connected-space hierarchy context, when
resolved, is checked separately and does not participate in this trace: it is
never counted into the primary item count, so its presence or absence cannot
by itself explain a mismatch here.

- [ ] Trigger phrase matched and target project/space named
- [ ] The read-only, recommendation-not-decision framing was stated before any
      data moved
- [ ] Source mode declared; JQL filter (if any) recorded verbatim
- [ ] Live mode: pagination ran to completion and the returned count matches
      the query's reported total
- [ ] Export mode: parsed with quote-honoring reader; repeated same-header
      columns collapsed; header row captured before body parse
- [ ] Degrade path taken explicitly (not silently) if no Jira and no export,
      with the resulting field gaps stated
- [ ] Data-class screen ran **before** any further processing, and its result
      is recorded
- [ ] Item count confirmed against the operator's stated expectation
- [ ] Field map presented to and confirmed by the operator — not auto-accepted
- [ ] Hard requirements (Issue key, Summary, Status, Created, Updated) all
      present
- [ ] Field-availability report lists every canonical field with its populated
      count
- [ ] Denominator captured from this cycle's source, not carried forward or
      hardcoded, and recorded with the item count
- [ ] Normalized set uses canonical field names and ISO dates, with
      empty-equivalents resolved
- [ ] Connected-space discovery ran against `Parent key`/`Issue Type`;
      candidates (if any) were presented with reference counts, and the
      resolve/decline choice — or the no-candidates finding — is recorded
- [ ] Any resolved connected-space items passed the same data-class screen as
      the primary source and were kept out of the primary item set and its
      count
- [ ] Operator confirmed "proceed"

## Review

- **Reviewer:** operator (or delegate)
- **Intensity:** heavy — this is the cycle's trust boundary. Every distribution,
  mapping, and score downstream inherits whatever this stage got wrong, and
  none of them can detect it: a truncated item set profiles cleanly, a
  mis-mapped Business Outcome field maps cleanly, and a carried-forward
  denominator produces plausible completion percentages that mean nothing.
- **Evidence:** the setup confirmation echoed in the session, plus a
  decision-log entry recording scope, source mode, item count, denominator,
  field map, degraded signals, the data-class screen result, and the
  connected-space discovery outcome.

## Data boundary

- **Max data-class this stage handles:** internal
- **Sanctioned engines for this stage:** Rovo, Copilot
- This is the flow's classification gate. Content above `internal` halts the
  run rather than being redacted and carried forward.
- Live binding is **read-only** via the engine's native Jira capability — the
  same access class `ai-refinement` Stage 01 uses for its label query. No write
  scope is requested or needed at any point in this flow.
- Assignee names enter here and persist through Stage 06. They are permitted at
  `internal` and are the flow's only sustained personal-data surface.
- Real portfolio content never enters this public design repo — it lives only in
  the instance, per `methodology/mirroring-protocol.md`.
- **Connected-space discovery is the one narrow exception to the single-project
  scope above.** It may read specific named issues in a different project or
  space than the one bound at step 3 — but only the exact parent keys the
  primary set already references, never a second whole-project or JQL query,
  and only after the operator explicitly elects to resolve. Everything
  resolved this way is read-only and passes the same step-4 data-class screen
  before it joins the cycle.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
