---
id: executive-slide-shape
title: "Executive Slide Shape — House Content Template"
type: template
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-08-06
updated: 2026-08-06
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related: ["[[executive-slide-digest]]"]
---

# Executive Slide Shape — House Content Template

The output shape Stage 3 (Draft) synthesizes into and Stage 4 (Align &
Publish) edits against. One initiative = one slide's worth of content. This
is the content-shape mold named in `fp-executive-slide-digest.md`'s Layer-3
inventory, authored here per the flow-foundry scaffold rule that reference
material "must be carried" alongside the flowspace, not deferred to
instantiation.

```markdown
## <Initiative Name>

**Status:** 🔴/🟡/🟢 <RAG> — <one-line why, naming the signal that drove the call>

**Headline:** <one sentence, business-outcome framed, never ticket-framed>

**Key accomplishments this period**

- <outcome-framed bullet>
- <outcome-framed bullet>
(2–4 bullets)

**Risks / Blockers** (omit this section entirely if none — see Authoring rules)

- <bullet, 0–3>

**Upcoming milestones**

- <bullet with date>
(1–3 bullets)

**Ask** (optional — omit if there is none)

<what the exec needs to know, decide, or unblock>
```

## Portfolio-rollup variant

For portfolio-rollup scope, the deck outline is:

1. **Title/agenda slide** — portfolio name, period, the initiatives covered in
   run order.
2. **One section per initiative**, each in the shape above.
3. **Closing rollup slide (optional)** — risks and asks pulled across all
   initiatives in the run, grouped by initiative name; omit if no initiative
   in the run carries a risk or ask worth escalating.

## Authoring rules

- **Outcome first, ticket second.** "Shipped X, which unblocks Y" beats
  "Closed 12 tickets in the Foo epic." Ticket counts are supporting evidence,
  never the headline — the same discipline
  `accomplishments-document-shape.md` states for its own audience, applied
  here for an executive one.
- **The RAG call must be defensible from Stage 2's gathered material.** Name
  the signal (a blocked dependency, a slipped due date, an open critical bug)
  that drove Amber or Red — never assert a status the source material doesn't
  support.
- **Risks/Blockers: a visible empty section reads worse than no section.**
  Omit it outright when there are none; do not write "No risks at this time."
- **Gaps stay visible.** If Stage 2's material is thin for an initiative, say
  so in that initiative's content (e.g., "no recent activity found in the
  gather window") rather than padding it to look complete. A fabricated
  accomplishment or invented milestone date is a worse failure than a
  visibly thin slide.
- **No milestone date or metric may appear that Stage 2's gathered material
  did not state.** This mirrors the accomplishments-drafter's exclusion-list
  discipline: nothing invented, ever, regardless of how thin the section
  looks without it.
