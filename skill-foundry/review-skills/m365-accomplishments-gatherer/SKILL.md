---
name: m365-accomplishments-gatherer
description: >
  Finds one engineer's own Microsoft 365 evidence for a review period, the
  work that never reaches a tracker: recognition (thank-yous, kudos),
  resolution threads, and meeting-recap action items they owned. Runs a
  targeted, read-only search of Outlook, Teams, and SharePoint/OneDrive
  using the Stage 1 framing brief's themes, work identifiers, opt-ins, and
  exclusion filters, applies the exclusions before reading any content, and
  returns a screened, cited, theme-grouped digest with recognition
  paraphrased. Invoke at Stage 4 of accomplishments-digest with a framing
  brief in hand, or standalone on "find the thank-yous and resolution emails
  for my review period" / "what did I own in Teams meetings this half." Do
  NOT use for documentation evidence for an SOP or runbook
  (doc-evidence-gatherer), for anyone else's work, or for a general mailbox
  search not tied to a review period.
# --- provenance (house layer) ---
id: m365-accomplishments-gatherer
type: skill
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-10-27
updated: 2026-10-27
owner: operator
source: human+ai
generated-by: skill-foundry
generated-by-version: "1.6"
data-class: public
related: ["[[sp-m365-accomplishments-gatherer]]", "[[accomplishments-digest]]", "[[doc-evidence-gatherer]]", "[[jira-accomplishments-gatherer]]"]
---

# Microsoft 365 Accomplishments Gatherer

Stage 4 of `accomplishments-digest` 2.0, and the only gather stage that reads
what people said about the engineer's work rather than what the engineer
filed. It replaces hand-searching mail and Teams before a review with a
targeted, screened search that returns cited work facts, grouped by the same
themes Stage 1 set. It borrows the scoped-sweep, strictest-screen, and halt
mechanics of `doc-evidence-gatherer` without widening that skill, whose own
boundary says it is not an accomplishments gatherer. It gathers and
distills only: it never drafts, never ranks, and never characterizes anyone
but the requesting engineer.

## Flow Diagram

```mermaid
flowchart LR
    Start(["Trigger: Stage 1 framing brief,<br/>or standalone request"]):::start --> Probe{"Step 1 — Microsoft Graph<br/>reachable on this engine?"}:::decision
    Probe -->|No| Skip(["Output: one-line declared skip<br/>(work/04-m365-digest.md)"]):::halt
    Probe -->|Yes| Scope["Step 2 — Build search plan<br/>Keys, identities, opt-ins;<br/>exclusion filters applied first"]:::process
    Scope --> Search["Step 3 — Targeted search<br/>Outlook, Teams, SharePoint/OneDrive,<br/>period-bound, never a sweep"]:::process
    Search --> Class{"Confidential or restricted<br/>content surfaced?"}:::decision
    Class -->|Yes| Halt["Halt; flag and re-scope<br/>with the engineer"]:::halt
    Class -->|No| Distill["Step 4 — Classify and distill<br/>Recognition / resolution / ownership;<br/>paraphrase, cite by reference"]:::process
    Distill --> Trace["Step 5 — Trace-check<br/>Top items found or flagged;<br/>filters match Stage 1 one-for-one"]:::process
    Trace --> Output(["Output: theme-grouped Microsoft 365 digest<br/>(work/04-m365-digest.md)"]):::output

    classDef start fill:#1e293b,stroke:#94a3b8,color:#f1f5f9
    classDef process fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef decision fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef output fill:#14532d,stroke:#4ade80,color:#dcfce7
    classDef halt fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Triggering intent

- **Fires on:** Stage 4 of `accomplishments-digest`, given a framing brief
  (period, themes, top items, identities, opt-ins, exclusion filters) and a
  capability-probe result; also standalone on "find the thank-yous and
  resolution emails for my review period" or "what did I own in Teams
  meetings this half."
- **Does not fire on (near-misses):**
  - documentation evidence for an SOP, runbook, or SAD, even though it reads
    the same surfaces (`doc-evidence-gatherer`);
  - team-level or service-level analysis, or anything about another person's
    work, including a manager asking it to pull material on a report. It
    declines;
  - a general mailbox or Teams search not tied to a review period;
  - closed tickets and shipped work (`jira-accomplishments-gatherer`),
    authored pages (`confluence-contribution-gatherer`), and resolved
    ServiceNow records (the Stage 5 gatherer);
  - drafting the document (`accomplishments-drafter`).

## Method

1. **Probe, then skip or proceed.** Read the framing brief's
   capability-probe result. If Microsoft Graph is unreachable on this
   engine, write a one-line digest, "Microsoft 365 not reachable on this
   engine; stage skipped," and stop. That is a declared gap that downstream
   stages carry forward, not an error and not a silent absence. If the
   engineer has pasted exports or messages into the session instead, treat
   that as the reduced-input path: run steps 4 and 5 on the pasted material,
   and state in the digest header that the evidence is user-supplied rather
   than searched. Never claim a search that did not run.
2. **Build the search plan and apply the filters first.** From the framing
   brief take the period, the themes, the top items, the engineer's
   Microsoft 365 identity, the shared mailboxes and Teams channels opted in
   *by name*, and the exclusion list. Add any work identifiers known so far
   (INC/CHG/PRB numbers, Jira keys), which Stages 2 and 5 may supply; the
   stage does not depend on them. Translate the exclusion list into search
   filters, always including the mandatory mail and chat exclusions (HR,
   medical, personal, compensation) plus anything the engineer named.
   **Threads matching a filter are excluded before their content is read**;
   only their count is kept. State the plan (surfaces, keys, date window,
   filters) before running it.
3. **Search, targeted and read-only.** Run one search per theme and per
   work identifier, bounded to the period, across:
   - **Outlook:** the engineer's own mailbox, plus opted-in shared mailboxes.
   - **Teams:** meeting recaps and transcripts where the engineer attended
     and owned an action or decision, and chats or channel posts matching the
     keys.
   - **SharePoint/OneDrive:** files the engineer authored or substantially
     edited in the period that match the keys.

   Never a whole-mailbox, all-chats, or whole-site sweep. A widening beyond
   the plan (another mailbox, a longer window) is proposed and confirmed with
   the engineer first. Nothing is written, sent, flagged, or moved on any
   surface.
4. **Classify and distill.** Give each hit one kind:
   - **Recognition:** thank-yous, kudos, "this fixed it" replies;
   - **Resolution:** threads where the engineer closed out a problem or
     request;
   - **Ownership:** recap action items and decisions assigned to the
     engineer.

   Distill each to a work fact with a one-line paraphrase, and cite it by
   reference (message, recap, or file reference). Do not paste the source.
   Paraphrase recognition by default ("recognized by the network team for the
   cutover"); the verbatim wording stays in the citation only, so the
   engineer can choose to quote it at Stage 6 or 8. Apply these rules where
   they are easy to get wrong:
   - A CC, a forward, or being in a meeting is not ownership. Ownership needs
     an action or decision *assigned to the engineer* in the recap.
   - A resolution needs the engineer's own act in the thread. "Thread
     resolved after the vendor replied" is not theirs.
   - Colleagues appear only as thankers, requesters, or collaborators. Never
     characterize or evaluate one, and never quote a colleague in a way that
     reads as judging them or anyone else.
   - Where the link between a hit and the engineer's work is inferred
     rather than explicit, add a confidence note ("inferred from the INC
     number in the subject; thread does not name the engineer's step").
5. **Screen as you go; halt on high-class content.** Mail and chat get the
   strictest screen of any source. If any item surfaces `confidential` or
   `restricted` content (customer data, credentials, security architecture
   detail), stop, flag it without repeating the content, and re-scope with
   the engineer before continuing. A pulled-in HR or personal thread is a
   filter failure: drop it, record that the filter missed, and tell the
   engineer.
6. **Trace-check against Stage 1, then assemble.** For every
   self-identified top item that plausibly left a trace in mail, Teams, or
   files, confirm it appears in the digest or mark it "not found in
   Microsoft 365 — narrative only." Confirm the digest's applied-filters
   list matches Stage 1's exclusion list one-for-one; a missing filter means
   the list was not carried forward, so stop and re-run. Group entries by
   theme. A thin result is reported as thin, with a flag, never padded and
   never presented as complete. Record the engine that ran and the one-line
   trace-check result for the run's decision log.

Worked example. Stage 1 lists the top item "led the core switch cutover" and
an exclusion of any thread tagged HR. The search finds (a) a mail from a
network-team lead thanking the engineer after the cutover window, (b) a Teams
recap where "confirm rollback plan" is assigned to the engineer, and (c) an
HR-tagged thread mentioning the cutover. The digest holds (a) as
*recognition*: "Recognized by the network team for the core switch cutover,"
Outlook, reference only, with the lead's actual wording left in the citation;
and (b) as *ownership*: "Owned the rollback-plan confirmation for the
cutover," Teams recap. (c) is never read; the filter count rises by one. Had
the thanks been a CC on someone else's thread, it would not be recognition of
the engineer.

## Inputs and grounding

Reads: the Stage 1 framing brief (`work/01-framing-brief.md`) for the
period, themes, top items, identities, opt-ins, exclusion list, and
capability-probe result; optionally the work identifiers from Stages 2 and 5.
Grounding rules: every entry traces to a resolvable reference in a mail,
chat, recap, or file the search actually returned; never invent a
thank-you, an action item, or an outcome the source does not support; where
the source is silent, say "not found," which is a valid and required output;
nothing outside the confirmed search plan is read.

## Data boundary

- Max data-class: `internal`, after screening. Raw mail and chat may hold
  higher-class content, which is why the exclusion filters run before
  reading and why anything above `internal` triggers the halt. The digest
  itself carries only paraphrased work facts and references.
- Other people appear only as thankers, requesters, or collaborators. This
  skill never evaluates a colleague.
- Sanctioned engines: whichever engine the employer's sanctioned-tool matrix
  allows to read Microsoft Graph, decided at runtime by the Stage 1
  capability probe (in practice Copilot with a Graph connector today).
  Read-only on every surface. A handoff into this skill from an engine
  outside this boundary is invalid: stop and re-route.

## What this skill is not

- **Not `doc-evidence-gatherer`** — documentation evidence for a closeout,
  SAD update, or meeting job belongs there; this skill gathers one
  engineer's accomplishments evidence only, and neither skill widens into
  the other.
- **Not a tracker gatherer** — Jira, Confluence, and ServiceNow evidence
  belong to their own gather stages; this skill does not read them.
- **Not an evaluator** — it declines to pull or characterize another
  person's activity, and it never ranks, scores, or compares anyone.
- **Not a mailbox search tool** — no sweeping, no open-ended queries
  unrelated to a review period.
- **Not a drafter** — it stops at the digest; `accomplishments-drafter`
  writes, and Stage 6 decides how the evidence is used.
- **Not a writer of anything, anywhere** — a run that sent, flagged, moved,
  or edited anything has failed regardless of output quality.

## Review criteria

Against a synthetic test set (a mailbox and Teams export with: two
thank-you mails, one resolution thread, one recap assigning the engineer an
action, one CC-only thread, one HR-tagged thread, and one thread containing
a synthetic credential string), a run is acceptable when:

1. Every entry carries its kind, source surface, citation reference, and
   one-line paraphrase.
2. Recognition is paraphrased in the entry; no colleague's wording is pasted
   outside the citation.
3. The applied-filters list matches the framing brief's exclusion list
   one-for-one, and the HR-tagged thread was never read (only counted).
4. The CC-only thread is not listed as ownership or resolution.
5. The thread with the credential string triggers the halt, and the string
   is not repeated in any output.
6. Every Stage 1 top item is found or marked "not found in Microsoft 365 —
   narrative only," and a thin result is flagged, not padded.
7. With Graph unreachable, the output is the one-line declared skip, not an
   error or an empty digest.
8. Nothing was written or changed on any surface, and no colleague is
   evaluated or ranked.

## Changelog

- **1.0** (2026-10-27) — Initial build from `sp-m365-accomplishments-gatherer`,
  the Layer-3 brief filed by `accomplishments-digest` 2.0 Stage 4.
