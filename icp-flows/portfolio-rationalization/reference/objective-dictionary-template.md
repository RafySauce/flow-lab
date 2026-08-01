---
id: objective-dictionary-template
title: "Objective Dictionary — Template"
type: template
artifact-version: "1.1"
status: living
truth-level: to-review
created: 2026-07-28
updated: 2026-07-29
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[portfolio-rationalization]]"
  - "[[close-score-model]]"
---

# Objective Dictionary — Template

The domain-neutral mold for Stage 03's objective dictionary. Instantiate it in
the source-repo with the organization's real objective areas; **this public
copy carries only the structure.**

> `truth-level: to-review` rather than the `template` type's usual `verified`
> default: this mold has never produced a real dictionary, and its confidence
> thresholds are proposals pending the same calibration gate as
> `close-score-model.md`.

**Why the real dictionary never lives here:** objective area names and their
keyword sets are organizational strategy content (`AGENTS.md` rule 8). They
belong in the instance, in employer tenancy, at whatever `data-class` the
employer's scheme assigns them. A dictionary in this repo would be an
employer-content leak, and this file exists specifically so that leak is
unnecessary. When no dictionary exists at all, §9 documents a way to propose
a starting one from the portfolio's own vocabulary — read the caveat there
before relying on it.

---

## 1. What a dictionary is

A dictionary is the mapping between the organization's strategic objective
areas and the vocabulary its work actually uses. Stage 03 reads it, matches
each Jira item's text fields against it, and emits a mapped area with a
confidence, a score, and the keywords that matched.

Two properties make it work:

- **Transparent.** Every mapping decision is explainable by pointing at the
  keywords that fired. An item's stakeholders can argue with a mapping, which
  is the point — an opaque classifier they cannot argue with will not survive
  its first governance meeting.
- **Owned and versioned.** Someone is accountable for the dictionary, and it
  carries a version. When objective areas change between planning cycles, the
  dictionary changes with them and the change is recorded.

## 2. Structure

One instantiated dictionary is one file in the instance's `reference/` folder,
carrying provenance frontmatter and this shape:

```markdown
## <Objective Area Name>

- **Area id:** `<kebab-case-id>`
- **Owner:** <accountable human for this area's keyword set>
- **Statement:** <the objective as the organization states it, one sentence>

| Keyword / phrase | Weight | Notes |
|---|---|---|
| <term> | 3 | Strong — near-unambiguous for this area |
| <term> | 2 | Moderate — indicative, appears elsewhere occasionally |
| <term> | 1 | Weak — supporting signal only |
```

Repeat per objective area. Then one closing section:

```markdown
## Needs objective review

The residual bucket. No keyword set — an item lands here by failing every
area's minimum threshold (§4).
```

### Weight guidance

| Weight | Use for |
|---|---|
| 3 | Terms that only this area's work would use — product names, platform names, the objective's own distinctive nouns |
| 2 | Terms strongly associated with this area but appearing occasionally elsewhere |
| 1 | Generic terms that support a match but never carry one alone |

**Keep weight-3 terms scarce.** A dictionary where everything is a 3 produces
high-confidence matches for everything and tells you nothing. As a working
rule, no more than a quarter of an area's terms should be weight 3.

## 3. Which fields get searched

Stage 03 matches against the item's text fields in this order, and records
which field each keyword hit came from:

| Field | Why it counts |
|---|---|
| Summary | Highest-signal, but shortest — a hit here is worth recording as such |
| Description | The main body of intent |
| Business Outcome | Written in objective language by construction — the highest-value field to match on when populated |
| Scope | What the work actually covers |
| Acceptance Criteria | Concrete, often names systems and platforms |
| Dependencies | Names adjacent systems — useful for secondary matches |
| Risks | Weakest signal; a risk mentions things the work is *avoiding* |

A match in Business Outcome or Summary is stronger evidence than the same match
in Risks. Instances may weight by field; the default is not to, and to record
the source field so the reviewer can judge.

**Missing fields degrade the match, they do not fail it.** An item with only a
Summary can still map — at correspondingly lower confidence, flagged in the
output. Stage 01's field-availability report tells Stage 03 which fields exist
at all in this cycle's source.

## 4. Scoring, confidence, and thresholds

An item's score for an area is the **sum of the weights of the distinct terms
that matched** in that area. Distinct: a term appearing six times counts once.
Repetition is a writing style, not evidence.

Proposed default thresholds — instance-tunable, and they must agree with
`close-score-model.md` §3.2:

| Confidence | Score | Meaning |
|---|---|---|
| High | ≥ 8 | Multiple distinct terms, including at least one weight-3 |
| Medium | 4 – 7 | Several terms, or one strong term with support |
| Low / weak | 1 – 3 | A single term or a few weak ones — flag, don't trust |
| Needs objective review | 0 | No term in any area matched |

**High confidence additionally requires at least one weight-3 term.** A score
of 8 assembled entirely from weight-1 generic terms is a coincidence, not a
match; it caps at Medium.

## 5. Tie-break and secondary matches

Score every area for every item. Then:

1. **Primary** = the highest-scoring area.
2. **Secondary possible match** = recorded when the runner-up area scores
   **≥ 60% of the primary's score**. Below that, the primary stands alone.
3. **True tie** (two areas equal and both above the Low threshold): the item is
   flagged for human assignment, not auto-assigned. Stage 03 carries heavy
   review precisely so these get looked at.

Secondary matches are a feature, not an inconvenience. Not every item belongs
cleanly to one objective, and forcing a false binary loses real information —
the item that legitimately supports two areas is different from the item that
matches one weakly, and the model treats it as such (`close-score-model.md`
§3.2 applies a 5-point unrelatedness reduction for a recorded secondary).

## 6. What `Needs objective review` means

An item lands here when nothing matched anywhere. It means one of:

- The item is **poorly worded** — real work, described in vocabulary the
  dictionary does not carry.
- The **dictionary has a gap** — vocabulary the organization uses that nobody
  wrote down.
- The item is **genuinely unaligned** — it does not support any stated
  objective.

These are three very different situations and the mapping cannot tell them
apart. `Needs objective review` therefore means "a human must look at this,"
never "this is unaligned" and certainly never "close this." Stage 06 captures
which of the three it turned out to be, and case two feeds back as a dictionary
revision for the next cycle.

## 7. Maintenance

- **Author or review the dictionary at the start of every cycle**, before
  Stage 03 runs. Objective areas change; vocabulary drifts.
- **Bump `artifact-version` on any keyword or weight change**, and record the
  change in the instance's `decision-log/`. Scores are not comparable across
  dictionary versions, and a cycle-over-cycle comparison that ignores this will
  mislead.
- **Feed Stage 06's dictionary-revision notes forward.** Every `Needs objective
  review` item a human resolves as "the dictionary was missing a term" is a
  concrete improvement for the next cycle. This feedback path is the main
  reason the dictionary gets better rather than staler.
- **Mid-cycle revisions:** decide, and record, whether a mid-cycle change
  invalidates that cycle's scores or applies forward only. The intake brief
  flags this as unresolved; the default recommendation is forward-only, with a
  re-run of Stage 03 if the change is material.

## 8. Worked fragment (synthetic)

An illustrative area from an invented dictionary — structure only, no real
objective areas:

```markdown
## Reduce Unplanned Outage Exposure

- **Area id:** `reduce-outage-exposure`
- **Owner:** <name>
- **Statement:** Cut customer-visible unplanned downtime by removing single
  points of failure in tier-1 services.

| Keyword / phrase | Weight | Notes |
|---|---|---|
| redundancy | 3 | Near-unambiguous for this area |
| failover | 3 | " |
| single point of failure | 3 | Also matches the abbreviation SPOF |
| resiliency | 2 | Also appears in platform-modernization work |
| disaster recovery | 2 | " |
| high availability | 2 | " |
| uptime | 1 | Generic — supporting signal only |
| monitoring | 1 | Weak here; strong in an observability area |
```

An item scoring 3 (`failover`) + 2 (`resiliency`) + 1 (`uptime`) = 6 maps
Medium. With `redundancy` also present it reaches 9 with a weight-3 term
included, and maps High.

## 9. Inferring a candidate dictionary (no operator dictionary available)

This section documents a **method**, not content. An inferred dictionary
produced by applying it to a real portfolio is built from that portfolio's
real vocabulary and real Component/Label/Epic-Link structure — once
instantiated it is organizational content exactly as an authored dictionary
is, and it lives in the instance's `reference/` folder, never in this public
repo (`AGENTS.md` rule 8), regardless of whether a human or an inference pass
wrote its first draft. Everything below is technique; the worked fragment
(§9.6) stays synthetic, in the same `PORT-nn` / "Reduce Unplanned Outage
Exposure" convention as §8, precisely so the method can be shown here without
leaking anything real.

**What this method cannot do.** It recovers, at best, how the backlog is
already organized and worded — not what leadership has actually stated the
objectives are. That is a materially weaker claim than an authored dictionary
makes, which is exactly why Stage 03 routes it through an explicit human
confirmation gate rather than treating it as equivalent on arrival.

### 9.1 Evidence floor

Inference requires the portfolio to already carry some categorical
structure. Proposed default (instance-tunable): at least 15% of items
populate at least one of Component, Labels, or Epic Link. Below that floor,
say so and do not attempt inference — there is too little to cluster on, and
a dictionary built from noise is worse than no dictionary.

### 9.2 Cluster

Group items by Component, then by Label, then by Epic Link — whichever the
field-availability report shows populated. A cluster earns consideration as
a candidate area at a proposed floor of at least 5 items *or* 5% of the
portfolio, whichever is larger; below that, it's noise, not an objective.

### 9.3 Extract terms

Within each qualifying cluster, compute term frequency across Summary and
Description, relative to that term's frequency across the rest of the
portfolio. A term common inside the cluster and rare outside it is a real
candidate; a term common everywhere (generic Jira vocabulary) is not.

### 9.4 Cap the weights

A term appearing in ≥50% of the cluster's items, materially rarer outside
it → weight 2 (the ceiling for inference). 25–49% → weight 1. Below 25%,
discard. **No inferred term is ever weight 3** — that designation is
reserved for organizational vocabulary a human wrote down (§2), never for a
statistically frequent word.

### 9.5 Name from the tag, never from strategy

The candidate area's name is the cluster's dominant categorical value itself
(the Component/Label/Epic name, title-cased) — never a strategic-sounding
phrase invented for the occasion. The name describes what the backlog
already calls this work, not what it claims to be for.

### 9.6 Residual and provenance

Items in no qualifying cluster land in the same `Needs objective review`
bucket a confirmed run would use — inference narrows that bucket, it doesn't
eliminate it. Every area produced this way, and the dictionary file as a
whole, carries `provenance: inferred` (as against `provenance:
operator-authored`) in its metadata — this travels downstream as a caveat,
never as a silent equivalence.

**Worked fragment (synthetic).** A cluster tagged `Component:
Outage-Response`, 14 items, with `failover` in 9 of 14 (64%, rare
elsewhere) and `redundancy` in 6 of 14 (43%): candidate area
**"Outage-Response"** (`provenance: inferred`) — `failover` weight 2,
`redundancy` weight 1. An item scoring `2 + 1 = 3` maps Low; nothing in this
dictionary can ever reach High, by construction.
