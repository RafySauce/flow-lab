---
id: fp-accomplishments-digest-m365-servicenow
title: "Flow Primer Brief — Accomplishments Digest 2.0: Microsoft 365 & ServiceNow Gather"
type: flow-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[accomplishments-docx-finisher]]"
  - "[[doc-evidence-gatherer]]"
  - "[[servicenow-ticket-ingest]]"
  - "[[accomplishments-drafter]]"
---

# Flow Primer Brief — Accomplishments Digest 2.0: Microsoft 365 & ServiceNow Gather

> Revision intake for an existing, promoted flowspace (`icp-flows/accomplishments-digest`,
> 1.3), not a new flow. It arrived as conversation (`foundry-spec.md` §1 case 4) and
> is written down here so the revision has an intake record before any stage is
> touched. The operator made the four structural calls listed under
> "Decided" on 2026-10-27. Everything else below is the agent's proposal, still
> open for the operator to amend.

## Purpose

Make the performance-review flow show the work that never lands in Jira or
Confluence. That means recognition and resolution evidence from Microsoft 365
(thank-you mail, Teams meeting recaps naming the engineer's actions, resolution
threads), and operational volume from ServiceNow (incidents, change tasks,
catalog tasks, and problem tasks the engineer resolved or closed). It recurs on
the same cadence as the base flow: once per review cycle per engineer.

## Decided (operator, 2026-10-27)

| # | Question | Call | Consequence for the design |
|---|---|---|---|
| D1 | How the new sources fit | **Two new gather stages**, one per source | Microsoft 365 and ServiceNow each get their own stage contract, parallel to the existing Jira and Confluence gathers. One source per stage keeps each stage's data boundary and engine clean. |
| D2 | Which engine carries the run | **Decide at runtime** | The running engine probes what it can reach (the `START-HERE.md` capability-probe pattern, applied per stage) and runs each gather stage it can reach. A stage whose source it can't reach degrades and says so rather than failing. For the Word output, the engine offers to build the `.docx` itself or asks the engineer for a template to use (see "Word output" below). |
| D3 | Where cross-source correlation happens | **Its own Correlate stage** | A new stage between gather and draft merges evidence about the same piece of work into one accomplishment, and the engineer reviews the groups before any prose is written. |
| D4 | How ServiceNow volume shows up | **An "Operational load" section plus counts inside themes** | The document shape and drafter gain a short, contextualized load section. Counts also appear as supporting evidence under related outcome themes, never as a headline. |

## Trigger and cadence

Unchanged from the base flow: the engineer starts a run ahead of a scheduled
review. One run produces one document for one review cycle.

## Stage sketch

| # | Stage | What happens | Review intensity (est.) |
|---|---|---|---|
| 1 | Frame *(revised)* | As today, plus three things: which sources are in scope this run, the identifiers that tie the engineer to each source (ServiceNow user, mailbox, Teams identity), and an exclusion list applied as a search filter. Mail exclusions are mandatory (HR, medical, personal, compensation). Runs the runtime capability probe and records which gather stages this engine can reach. | heavy |
| 2 | Gather — Jira | Unchanged. | light |
| 3 | Gather — Confluence & Collaboration | Unchanged. | light |
| 4 | Gather — Microsoft 365 *(new)* | A targeted, read-only search of the engineer's own mail, Teams chats and meeting recaps, and SharePoint/OneDrive. It is scoped to the review period and keyed on Stage 1's themes and on ticket/INC numbers. It never sweeps a whole mailbox. It pulls recognition (thank-yous, kudos), resolution threads, and recap action items the engineer owned. Mail and chat get the strictest screen of any source. | light |
| 5 | Gather — ServiceNow *(new)* | A read-only pull of INCs, CTASKs, SCTASKs, and problem tasks the engineer resolved or closed in the period. Keeps "resolved by" separate from "assigned at some point". Adds context: priority mix, median time to resolve, problem tasks that led to a permanent fix, and reopened records flagged. | light |
| 6 | Correlate *(new)* | Matches evidence across all available digests on shared identifiers (INC/CHG/PRB numbers, Jira keys, page links) and on Stage 1 themes. One piece of work found in several sources becomes one accomplishment group with all its citations. Unmatched items stay visible as singletons. Nothing is dropped silently. | heavy (?) |
| 7 | Draft *(was 4)* | Synthesizes correlated groups into the revised house shape, including the Operational load section. | light |
| 8 | Align & Publish *(was 5)* | Unchanged in role. Its exclusion trace now also covers Microsoft 365 and ServiceNow content. | heavy |
| 9 | Word output *(was 6, revised)* | Optional. The engine checks whether it can produce a `.docx`. If it can, it offers the engineer two choices: build it from the minimal default style, or use a template the engineer provides. If it can't, it packages the handoff for an engine that can. | light |

**Correlate's review intensity is marked `(?)`.** It is a mid-flow stage, so
the U-curve default would be light. I've proposed heavy because grouping is
where a wrong merge (two different incidents treated as one) or an over-merge
(inflating one fix into a theme) gets locked in before drafting. That is a
judgment boundary, not mechanical execution. The operator decides; either
way, the reason gets logged.

## Data profile

The base flow runs at `internal`. The two new sources raise that:

- **ServiceNow records** routinely carry customer references, hostnames, and
  other people's names in work notes. Stage 5 reads structured fields
  (number, type, priority, state, opened/resolved timestamps,
  `resolved_by`/`closed_by`, short description). It does not read work-note
  or comment bodies by default. It halts and re-scopes if a record surfaces
  `confidential`/`restricted` content, using `doc-evidence-gatherer`'s halt rule.
- **Mail and Teams** can contain anything. Stage 4 distills to work facts and
  cites by reference, never by pasting. A thank-you is paraphrased by default
  ("recognized by the network team for…"). A named quote appears only if the
  engineer picks it at Stage 6 or 8. Threads on the Stage 1 exclusion list
  are filtered out before content is read, not after.
- **Peer non-evaluation** (the base flow's existing rule) is extended to both
  new stages. Colleagues appear only as thankers, collaborators, or
  requesters. Volume is never compared with peers or a team average.
- **Real runs stay inside the employer tenancy** on sanctioned engines.
  This public copy is a sanitized design, `data-class: public` by construction.

## Layer-3 inventory

**Unchanged pointers:** `jira-accomplishments-gatherer` (Stage 2),
`confluence-contribution-gatherer` (Stage 3).

**Existing skills deliberately *not* widened** (their patterns are reused, not
the skills themselves). This mirrors how `jira-accomplishments-gatherer`
sits beside `jira-portfolio-ingest`:

- `doc-evidence-gatherer`: it already does scoped Microsoft 365 sweeps with a
  strictest-screen rule for mail and chat, but its own boundary reads "Not an
  accomplishments gatherer." Its scoping, screening, and halt mechanics are
  the model for the new Microsoft 365 skill.
- `servicenow-ticket-ingest`: it reads the right tables and already handles
  numeric state labels, pagination, and reopen detection. But it is
  aggregate-only by design and names a group, never a person, which is what
  protects `statik-adoption`. Widening it to per-person would break that
  guarantee. Its binding and normalization mechanics are the model for the
  new ServiceNow skill.

**Suspected gaps: candidate skill-primer-briefs**, to be filed only after the
operator approves this brief:

| Candidate | Capability | Stage |
|---|---|---|
| `sp-m365-accomplishments-gatherer` | A scoped, screened, cited Microsoft 365 recognition and resolution digest for one engineer and one period | 4 |
| `sp-servicenow-accomplishments-gatherer` | A per-person, read-only ServiceNow resolution digest with load context (priority mix, time to resolve, problem fixes, reopen flags) | 5 |
| `sp-accomplishments-correlator` | Cross-source matching on shared IDs and themes into reviewed accomplishment groups | 6 (only if Correlate is a skill, not inline; see Open questions) |

**Revisions to verified artifacts.** Each one returns that artifact to
`to-review` until it passes the gate again:

- `accomplishments-drafter`: consumes correlated groups instead of two raw
  digests, and drafts the Operational load section.
- `reference/accomplishments-document-shape.md`: adds the Operational load
  section, and folds recognition into the collaboration evidence.
- `accomplishments-docx-finisher` and its stylizer skill: affected by D2's Word
  behavior (see below).

## Word output (D2, operator wording)

> "Decide at runtime. The engine running it can check what is available and
> produce the Word document. It should offer to build it or request a
> template to use for the output."

Agent's reading, for the operator to confirm:

1. The `.docx` is no longer tied to Copilot. Whichever engine is running
   checks whether it can produce Word output. If it can, it produces the
   document itself rather than always handing off.
2. Before stylizing, it asks one question: build from the minimal default
   (`accomplishments-docx-finisher/reference/docx-minimal-default-style.md`)
   or use a template the engineer provides. Today the finisher picks the house
   template silently when one exists and falls back with a flag when one
   doesn't.
3. The finisher's enrichment step (adding repo and file evidence) stays
   evidence-only, per its existing J1 assumption. The finisher's heavy
   final review stays. Only the engine lock and the template choice change.

What this implies structurally is an open question below.

## Source-repo

- **Source-repo:** unchanged. It is the instance's internal GitLab repo,
  `flows/accomplishments-digest/`.
- **External systems read:** Jira, Confluence (as today), plus Microsoft 365
  via Microsoft Graph (mail, Teams chat and meeting recaps,
  SharePoint/OneDrive) and ServiceNow (incident, change task, catalog task,
  and problem task tables). All are read-only.
- **External systems written:** unchanged. Only the Stage 8 publish writes
  (Confluence page tree).

## Intended outputs of the build (once approved)

1. `accomplishments-digest` HUB 1.3 → 2.0: diagram, stage table, Known gaps,
   and renumbered stage folders 01–09, with new `CONTEXT.md` contracts for
   Stages 4, 5, and 6, and revised contracts for Stages 1, 7, 8, and 9.
2. A revised `reference/accomplishments-document-shape.md`.
3. Two (or three) skill-primer-briefs in `skill-foundry/backlog-skill-starters/`,
   plus a revision note for `accomplishments-drafter`.
4. Whatever the Word-output decision requires in
   `accomplishments-docx-finisher` (see Open question 1).
5. A decision-log entry in `icp-flows/accomplishments-digest/decision-log/`
   recording D1 through D4 and the version bump.
6. Staged to `flow-foundry/review-flowspaces/` at `to-review`. Promotion stays
   the operator's.

**Non-goals:** no peer comparison or ranking; no evaluation of colleagues; no
whole-mailbox or all-chats sweep; no writes to ServiceNow or Microsoft 365; no
new accomplishments invented at the Word step; no employer content in this repo.

## Open questions

Surfaced for the operator, not decided here:

1. **Word output structure.** Should a) the finisher stay a separate companion
   flow that loses its Copilot lock and gains the build-or-template question,
   or b) be folded into this flow's Stage 9, retiring the companion? The
   agent recommends (a). It is the smaller change, and it keeps the
   finisher's heavy final review intact.
2. **Correlate review intensity.** Heavy, as proposed, or light with the
   check moved to Stage 8?
3. **Correlate as skill or inline.** Matching on shared IDs is reusable,
   which argues for a skill (and brief 3 above). If it's inline, there's one
   less artifact to verify. The agent leans toward a skill.
4. **ServiceNow identity field.** Is `resolved_by`, `closed_by`, or
   `assigned_to` at closure the right "this was the engineer's work" signal
   in the target instance? This varies by tenant, so it should be decided at
   instantiation with a probe, like the Confluence activity-history check.
5. **Mail scope default.** Does the search cover only mail the engineer sent
   and received, or also shared and team mailboxes they monitor? The agent
   recommends personal only by default, with shared mailboxes opted in by
   name at Stage 1.
6. **Stage renumbering.** Renumbering 4–6 → 7–9 touches every cross-reference
   in both flowspaces and in skill specs. That is mechanical, but it is a
   wide diff. The alternative is non-sequential numbering, which breaks the
   house convention. The agent recommends renumbering.
