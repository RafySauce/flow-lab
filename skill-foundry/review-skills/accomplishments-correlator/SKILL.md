---
name: accomplishments-correlator
description: >
  Takes an engineer's own evidence (gather digests or pasted/attached lists from
  Jira, Confluence, Microsoft 365, ServiceNow), plus optional context (period,
  themes, top items), and builds accomplishment groups:
  one piece of work with all of its evidence. Matches first on the hard
  identifier types the engineer chooses (INC/CHG/PRB/PTASK numbers, Jira keys,
  page links, file references; a by-type count of what the digests contain is
  offered first, and the step is optional), then on supplied themes labeled `inferred`; everything else
  stays a visible singleton, and look-alikes with no shared identifier are
  flagged "possible duplicate", never merged. Then presents the groups for the
  engineer's heavy confirmation and records every merge, split, drop, and
  quote choice as a confirmed correlation map. Works the same
  whether fed by Stage 6 of accomplishments-digest or called standalone with
  context handed in. Invoke on "tie my tickets, emails, and incidents together
  into accomplishments." Do
  NOT use to draft prose (accomplishments-drafter), to deduplicate a backlog
  (portfolio-rationalization), or to correlate anyone's evidence but the
  engineer's own.
# --- provenance (house layer) ---
id: accomplishments-correlator
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
related: ["[[sp-accomplishments-correlator]]", "[[accomplishments-digest]]"]
---

# Accomplishments Correlator

The correlation skill used at Stage 6 of `accomplishments-digest`, and equally usable standalone. It behaves identically either way: it works from whatever evidence and context it is handed and never depends on the flow's folders or earlier stages. The gather stages each report
one source, so a single fix can appear as a ticket, an incident, a Teams recap
decision, and a thank-you email: four bullets for one accomplishment, or worse,
a thank-you with no link to the work it praised. This skill joins that evidence
into accomplishment groups and puts the groups in front of the engineer to
confirm before any prose is written. It correlates and presents only; it never
drafts, and it never decides what counts as one accomplishment without the
engineer.

## Flow Diagram

```mermaid
flowchart LR
    Start(["Trigger: evidence handed in<br/>(from the flow or standalone)"]):::start --> I["Step 1 — Inventory and count<br/>Every digest present or declared skipped;<br/>count every entry"]:::process
    I --> X["Step 2 — Choose identifiers<br/>Callout: items seen, by type;<br/>engineer opts in, optional"]:::process
    X --> M["Step 3 — Match on identifiers<br/>INC/CHG/PRB/PTASK, Jira keys,<br/>page and file links"]:::process
    M --> T["Step 4 — Match on themes<br/>supplied themes only; labeled inferred"]:::process
    T --> S["Step 5 — Singletons and duplicates<br/>Unmatched stays visible; look-alikes<br/>flagged, never merged"]:::process
    S --> L["Step 6 — Attach load context<br/>ServiceNow load as evidence; summary<br/>carried whole"]:::process
    L --> G{"Step 7 — Engineer confirms<br/>Merge, split, re-theme, drop,<br/>promote; quote choices"}:::decision
    G -.->|"changes requested"| M
    G --> V["Step 8 — Verify<br/>Count in = count out;<br/>top items mapped"]:::process
    V --> Output(["Output: confirmed correlation map<br/>(correlation map)"]):::output

    classDef start fill:#1e293b,stroke:#94a3b8,color:#f1f5f9
    classDef process fill:#1e3a8a,stroke:#60a5fa,color:#dbeafe
    classDef decision fill:#78350f,stroke:#fbbf24,color:#fef3c7
    classDef output fill:#14532d,stroke:#4ade80,color:#dcfce7
    classDef halt fill:#7f1d1d,stroke:#f87171,color:#fee2e2
```

## Triggering intent

- **Fires on:** Stage 6 of `accomplishments-digest` with its digests and
  framing brief handed in, or a standalone request with evidence pasted or
  attached; the same behavior in both, on "tie my tickets,
  emails, and incidents together into accomplishments," "which of these
  records are the same piece of work," or "group my evidence by accomplishment."
- **Does not fire on (near-misses):** drafting accomplishment prose
  (`accomplishments-drafter`); deduplicating or rationalizing a Jira backlog
  (`portfolio-rationalization`); gathering from any source (the four gatherer
  skills); correlating anyone's evidence but the engineer's own, including a
  manager assembling material about a report.

## Method

1. **Inventory and count.** Establish what was handed in and what context
   came with it. *Evidence:* any of the four sources (Jira, Confluence,
   Microsoft 365, ServiceNow) as digests or plain lists of records. Ask which
   of the four are included and whether each absent one was skipped or simply
   not supplied; either way record it as a gap carried forward, never as
   silently complete. *Context (all optional):* period, themes, top items,
   exclusion list. Use what was supplied; ask once for anything missing that
   a later step needs; if the engineer has none, proceed without it and say
   which steps are reduced (no themes: step 4 is skipped; no top items: the
   top-item check is skipped; no period: state the span the entries cover).
   Give every entry in every supplied source a stable working ref
   (`J-1`, `C-1`, `M-1`, `S-1`, in digest order) and record the per-digest
   entry counts. These counts are the baseline for step 8. The ServiceNow
   digest's assigned-but-not-resolved list is carried separately as context
   (see step 6), not counted as evidence entries.
2. **Choose identifiers (optional, engineer's call).** Do not assume which
   identifiers to match on. First scan the digests for identifiers already
   present and report, from those digests only (no new query), what was seen
   over the period (supplied, or the span the entries cover), by type, for example: "Over <period>
   I see 31 ServiceNow records (INC 22, CTASK 6, PRB 3), 14 Jira keys, 5
   Confluence page links, and 3 SharePoint file references across your
   digests." Then ask which types to match on. Offer: all types seen, a
   chosen subset, or none (skip identifier matching and group by themes and
   singletons only). Match only on the types chosen. If the engineer already
   made this choice in the context handed in (for example the flow's
   per-source opt-ins), restate it and ask only to confirm. An unchosen type still keeps
   its entries visible as ordinary entries; it just forms no identifier link.
   The counts describe what is in the digests, never a claim about the
   engineer's total work.
3. **Match on chosen identifiers.** Pull each chosen-type identifier from every entry:
   INC/CHG/PRB/PTASK/CTASK/SCTASK numbers, Jira keys, Confluence page links
   or IDs, SharePoint/OneDrive file references. Entries sharing an identifier
   join one group, including transitively (A shares a key with B, B shares an
   incident number with C: one group, with the chain shown). Match basis:
   `identifier`, naming the identifier. Match on the exact identifier string
   only; "similar number" or "same prefix" is not a match.
4. **Match on themes.** For groups and entries still unattached, place them
   under a supplied theme or top item only when the link is clear in the
   entries' own content. Match basis: `inferred`, with a one-line reason.
   An `inferred` link must read as visibly weaker than an `identifier`
   link everywhere it is shown (label, ordering, and a "confirm this link"
   prompt in step 7). An inferred match never overrides or splits an
   identifier match.
5. **Keep singletons; flag look-alikes.** Anything unmatched stays as its own
   group, match basis `singleton`. Never merge on similarity alone: two
   entries with similar descriptions but no shared identifier and no clear
   theme link stay separate and carry "possible duplicate: engineer to
   decide" pointing at each other. Nothing is dropped here; only the engineer
   drops.
6. **Attach load context.** ServiceNow records attach to the groups they
   support as evidence entries, and counts may appear against a theme as
   supporting detail. The ServiceNow load summary (counts by type, priority
   mix, median time to resolve, problem-led fixes, reopens) is carried whole
   and unaltered into the output for the Operational load section. The
   assigned-but-not-resolved list is carried whole as its own section. Load
   figures are evidence, never a headline, and are never compared with peers
   or a team average.
7. **Present for confirmation (heavy gate).** Show the groups ordered with
   top items first (when supplied), then other themes, then singletons. For each group:
   working title, theme, match basis, every evidence entry with source and
   citation, and any flags. Ask the engineer to: confirm, merge, split,
   re-theme, drop, or promote each group; resolve each "possible duplicate"
   flag; confirm each `inferred` link; choose any verbatim recognition quote
   they want used (default is paraphrase, no named quote unless picked); and
   confirm that each supplied top item has a group or accept a "narrative only" flag.
   Apply the changes and re-present the changed groups until the engineer says
   plainly that the map is right. Do not treat silence, a skim, or "looks
   fine" on a partial view as confirmation, and do not proceed to output
   without an explicit confirmation of the full map.
8. **Verify and write the map.** Run two checks and show the results.
   *Coverage:* every entry counted in step 1 appears in exactly one group or
   is listed as dropped by the engineer; count in equals count out, per
   digest and in total. *Top items (when supplied):* every top item maps to at least
   one confirmed group or carries a "narrative only" flag the engineer
   accepted. A failed check goes back to step 7, never forward. Then write
   the confirmed correlation map where the caller asks (in the flow,
   `work/06-correlation-map.md`; standalone, in the conversation or a file
   the engineer names) and a one-line log entry naming the result and the
   engineer's merges, splits, and drops.

**Worked example A: one incident, three sources.** `INC0012345` appears in
the ServiceNow digest (resolved, P2), in a Teams recap entry ("agreed the
root-cause fix for INC0012345 ships Thursday"), and in a thank-you email
entry that names the same incident. With INC numbers chosen in step 2, step 3 produces one group, basis
`identifier: INC0012345`, three entries. The engineer is asked only to
confirm it and, if they want, pick a quote from the email.

**Worked example B: two look-alikes.** Two ServiceNow entries read "Core
switch port flapping, site A" and "Core switch port flapping, site B" with
different INC numbers, and neither is linked to anything else. Step 5 keeps
two singleton groups, each flagged "possible duplicate: engineer to decide."
The skill does not merge them, and does not pick which is real.

**Worked example C: weak versus strong.** A Confluence page on "firewall
rule cleanup" and a Jira epic on the same theme share no key or link. Step 4
may place both under the supplied theme "network hygiene," labeled `inferred`
with its reason, as two entries in one theme group. It is never presented
as the same strength as an incident-number match.

## Inputs and grounding

Reads only what is handed in, by whatever route: pasted text, attached
files, or the flow's working files (in `accomplishments-digest`, the framing
brief `work/01-framing-brief.md` and digests `work/02` to `work/05`). The skill
does not care which route; it never requires the flow's folders and never
fetches from a source itself. Paste or attach is a fully valid path. Context
that is not supplied is asked for once, then treated as absent (step 1).

Grounding rules: every group, link, and flag traces to entries actually in the
digests. Never invent an identifier, a source, or an outcome. Never infer a
person's involvement or a link from similarity of wording alone. Group titles
are working labels built from the entries' own content, not new claims. State
"no match found" rather than manufacturing a connection. No external queries:
this skill works only on material already gathered.

## Data boundary

- Max data-class: `internal`, carried from the digests. No external queries.
- Digests may contain work-fact paraphrases of mail, chat, and ServiceNow
  records. The skill adds no new content beyond working titles. It does not
  expand a paraphrase into a direct quote, and it names colleagues only as
  they appear in the digests (as thankers, collaborators, or requesters).
  If an entry looks like `confidential` or `restricted` content, or matches
  the exclusion list, if one was supplied, stop, flag it, and ask the engineer before
  grouping it.
- Sanctioned engines: any engine sanctioned for `internal` content, per the
  employer matrix. This is pure synthesis; no source connector is needed.

## What this skill is not

- **Not a drafter.** It produces a map of evidence groups, not prose.
  `accomplishments-drafter` writes from the confirmed map.
- **Not a backlog deduplicator.** It correlates one engineer's evidence
  across sources; `portfolio-rationalization` owns backlog hygiene.
- **Not a gatherer.** It does not query Jira, Confluence, Microsoft 365, or
  ServiceNow; the gatherer skills do.
- **Not an evaluator of anyone.** It correlates the requesting engineer's own
  record only, declines to correlate another person's evidence, and never
  compares volume with peers or averages.
- **Not an auto-merger.** It never merges on similarity alone, never lets an
  inferred match look as strong as an identifier match, and never drops an
  entry. Only the engineer drops.
- **Not self-confirming.** The confirmation in step 7 is the engineer's;
  the skill cannot supply, assume, or imply it.

## Review criteria

A single output of this skill is acceptable when:

1. Count in equals count out: each entry in each digest appears in exactly
   one group or in the engineer's dropped list, with per-digest counts shown.
2. Every group carries a match basis (`identifier` naming the identifier,
   `inferred` with its reason, or `singleton`), and `inferred` is visibly
   distinguishable from `identifier` wherever shown.
3. No merge exists on similarity alone; look-alike entries without a shared
   identifier or clear theme link are separate and flagged "possible
   duplicate."
4. When top items were supplied, every one maps to a confirmed group or an accepted
   "narrative only" flag.
5. The ServiceNow load summary and assigned-but-not-resolved list are carried
   whole and unaltered, with no peer comparison and no volume as headline.
6. Digest gaps (skipped or unreachable stages) are carried forward by name,
   not silently omitted.
7. Every disposition (keep, merged, split, dropped), every approved quote, and
   the engineer's explicit confirmation of the full map are recorded; no
   recognition quote is named that the engineer did not pick.
8. Identifier types were offered with a by-type count callout drawn from the
   digests and matched only on the types the engineer chose (or none); the
   choice is recorded in the map.
9. Simulated run 1: one incident present in three sources yields exactly one
   group. Simulated run 2: two look-alike incidents with different numbers
   yield two groups plus a duplicate flag.

## Changelog

- **1.0** (2026-10-27) — Initial build, context-agnostic (same behavior fed by the flow or called standalone); identifier types are operator-selectable (step 2) per review feedback.
