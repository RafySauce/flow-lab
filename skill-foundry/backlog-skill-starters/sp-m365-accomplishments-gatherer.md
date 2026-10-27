---
id: sp-m365-accomplishments-gatherer
title: "Skill Primer Brief — Microsoft 365 Accomplishments Gatherer"
type: skill-primer-brief
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: flow-foundry
data-class: public
related: ["[[accomplishments-digest]]", "[[doc-evidence-gatherer]]"]
---

# Skill Primer Brief — Microsoft 365 Accomplishments Gatherer

> Filed from a Layer-3 gap in `accomplishments-digest` 2.0, Stage 4 (Gather —
> Microsoft 365). Intake record:
> `flow-foundry/backlog-flow-starters/fp-accomplishments-digest-m365-servicenow.md`.

## Purpose

Find the evidence of one engineer's work that lives in Microsoft 365 and never
reaches a tracker: thank-yous, resolution threads, and meeting-recap action
items they owned. Return it as a screened, cited, theme-grouped digest for
one review period. This replaces hand-searching mail and Teams before a
review.

## Triggering intent

- `accomplishments-digest` Stage 4, with a framing brief in hand.
- "Find the thank-yous and resolution emails for my review period."
- "What did I own in Teams meetings this half?"

**Near-misses that should not trigger it:** documentation evidence for an SOP
or runbook (`doc-evidence-gatherer`); team-level or service-level analysis;
anything about another person's work; a general mailbox search not tied to a
review period.

## Method sketch

- Take the period, themes, top items, identities, opt-ins, and exclusion
  filters from the framing brief. Apply the exclusion filters **before**
  reading content.
- Run a targeted search per theme and per work identifier across Outlook (own
  mailbox plus named opt-ins), Teams (recaps and transcripts where the engineer
  owned an action, plus matching chats), and SharePoint/OneDrive (files they authored). Never sweep a whole
  mailbox.
- Classify each hit as recognition, resolution, or ownership. Distill each
  to a work fact, cite it by reference, and paraphrase other people's words.
  Keep the verbatim wording only in the citation so the engineer can choose
  to quote it.
- Use the strictest screen for mail and chat. Halt and re-scope on
  `confidential` or `restricted` content, using `doc-evidence-gatherer`'s halt rule.
- **Failure modes to guard against:** pulling HR or personal threads; treating
  a CC as ownership; quoting a colleague in a way that evaluates them;
  presenting a thin result as complete.

## Inputs and data boundary

- **Inputs:** the Stage 1 framing brief, plus optional work identifiers from
  other digests.
- **Max data-class:** `internal` after screening. Raw sources may be higher,
  which is why the screen runs first.
- **Engine:** any engine the employer matrix sanctions for Microsoft Graph
  reads, decided at runtime (Copilot with a Graph connector today).
  Read-only.

## Demand source

`accomplishments-digest` 2.0, Stage 4. The pattern is borrowed from
`doc-evidence-gatherer` (scoped Microsoft 365 sweep, strictest screen, halt
rule) without widening it, because its own boundary says "not an
accomplishments gatherer."

## Definition of done

- Every hit carries its kind, source surface, citation, and paraphrase.
- The applied filters match the framing brief's exclusion list
  one-for-one.
- Every Stage 1 top item is found or flagged "not found in Microsoft 365."
- A simulated run on synthetic mail and Teams data shows that excluded
  threads are never read and that recognition is paraphrased.
- "Graph unreachable" produces a declared skip, not an error.
