---
id: accomplishments-digest-stage-04
title: "Stage 04 — Gather — Microsoft 365"
type: stage-context
stage: 4
review-intensity: light
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-28
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[accomplishments-digest]]"
  - "[[sp-m365-accomplishments-gatherer]]"
  - "[[doc-evidence-gatherer]]"
---

# Stage 4 — Gather — Microsoft 365 (`CONTEXT.md`)

## Inputs

Stage 1's framing brief (`work/01-framing-brief.md`): the period, the
self-identified top items and their themes, the exclusion list, the
engineer's Microsoft 365 identity, any shared mailboxes or Teams channels
the engineer opted in by name, and the capability-probe result saying this
engine can reach Microsoft Graph. Optionally, the ticket and INC numbers
from Stages 2 and 5 if they have already run, used as extra search keys. This
stage does not depend on them; it runs in parallel with Stages 2, 3, and 5.

## Process

If the capability probe says Microsoft Graph is unreachable on this engine,
skip the search. Write a one-line "Microsoft 365 not reachable on this
engine; stage skipped" digest and stop. Downstream stages treat it as a
declared gap, not a silent absence.

Otherwise, run a **targeted, read-only** search scoped to the period. The
search keys are Stage 1's themes and top items, plus any work identifiers
(INC/CHG/PRB numbers, Jira keys) known so far. The surfaces searched:

- **Outlook:** the engineer's own mailbox, plus any shared mailboxes opted
  in by name at Stage 1. Never a whole-mailbox sweep. Threads matching
  the exclusion list (HR, medical, personal, compensation, plus anything the
  engineer named) are filtered out *before* their content is read.
- **Teams:** meeting recaps and transcripts where the engineer attended and
  owned an action or decision; chats and channel posts matching the search
  keys.
- **SharePoint/OneDrive:** documents the engineer authored or substantially
  edited in the period that match the search keys.

Pull three kinds of evidence. **Recognition** means thank-yous, kudos, and
"this fixed it" replies. **Resolution** means threads where the engineer
closed out a problem or request. **Ownership** means recap action items and
decisions assigned to the engineer. Distill each one to a work fact and cite it
by reference (message, recap, or file reference). Don't paste the original. Paraphrase
recognition by default, for example "recognized by the network team for the
cutover." Keep the verbatim wording only in the digest's citation, so the
engineer can choose to quote it at Stage 6 or 8. Mail and chat get the
strictest screen of any source. If an item surfaces `confidential` or
`restricted` content (customer data, credentials, security architecture),
halt, flag it, and re-scope with the engineer before continuing.
`Layer-3: m365-accomplishments-gatherer` (1.0, `to-review`, staged in
`skill-foundry/review-skills/m365-accomplishments-gatherer/`; until it passes the gate,
this stage runs inline as described above).

## Outputs

A **Microsoft 365 digest**: evidence entries grouped by theme. Each entry
carries its kind (recognition / resolution / ownership), a one-line work-fact
paraphrase, its source surface (Outlook / Teams / SharePoint / OneDrive), a
citation reference, any work identifiers it mentions, and a confidence note
where the link to the engineer's work is inferred rather than explicit. It
also carries a list of exclusion filters applied and a count of threads
filtered. Lands as `work/04-m365-digest.md`.

## Verify

A specific cross-stage trace check against Stage 1. Every self-identified top
item that plausibly left a trace in mail, Teams, or files appears in this
digest, either explicitly or flagged "not found in Microsoft 365 — narrative
only." Also, the digest's applied-filters list matches Stage 1's exclusion
list one-for-one. A missing filter means the exclusion list was not carried
forward: stop and re-run. Result recorded as a one-line entry in the run's
decision log.

## Review

- **Reviewer:** the engineer.
- **Intensity:** `light`. This is constrained execution against defined search
  keys and a defined screen, with no framing judgment. The heavy check on how
  this evidence is used sits at Stage 6.
- **Evidence:** the digest, available for the engineer to skim before
  Stage 6 correlates it.

## Data boundary

- **Max data-class this stage handles:** `internal`, after screening. Raw
  mail and chat may contain higher-class content, which is why the screen
  runs before distillation and anything above `internal` triggers the halt.
  Other people appear only as thankers, requesters, or collaborators. Never
  evaluate a colleague, and never quote a colleague's words in a way that
  reads as judging them.
- **Sanctioned engines for this stage:** whichever engine the employer's
  sanctioned-tool matrix allows to read Microsoft Graph, decided at runtime
  by the Stage 1 capability probe. In practice that is Copilot with a Graph
  connector today. Record the engine that ran in the run's decision log.
- A handoff into this stage from an engine outside this boundary is invalid —
  stop and re-route.
