# Boundary Collision — the corpus diff

A skill's `description` is what a routing model reads to decide whether to fire. When
two skills' descriptions claim the same trigger space, the router can't tell them
apart — and *both* skills get less reliable, not just the new one. Boundary collision
is the one quality problem that's contagious across the family, which is why it's the
only subjective-feeling check that can rise to **blocking**.

This check is the auditor's second original muscle: nothing else in the pipeline
looks at a candidate skill *against the existing corpus*.

---

## How to run it

1. **Gather the corpus.** Read the `description` (and `name`) of every sibling skill
   currently in the family — the installed skills plus anything in
   `completed-skills/`. These are the live triggers the router is already choosing
   among.
2. **Extract the candidate's trigger surface.** From its `description`: the explicit
   trigger phrases, the domain, and the boundary it claims ("use for X," "do NOT use
   for Y").
3. **Diff against each sibling** on three axes:
   - **Trigger-phrase overlap** — do they share literal phrases a user would type?
     (e.g. two skills both claiming "extract providers from".)
   - **Domain overlap** — same subject area?
   - **Boundary clarity** — does each skill *name* the other (or the distinction) so
     the router has a tiebreaker?
4. **Classify** each overlap (below) and fold the worst into the verdict.

---

## Classifying an overlap

| Situation | Severity | Why |
|---|---|---|
| Shared trigger phrase **and** no disambiguating boundary in either skill | **BLOCK** | The router has no way to choose; both skills degrade |
| Shared domain, but each skill names the boundary that separates them | **Flag** (or pass) | Adjacent-but-distinct is normal and healthy; the boundary does the routing work |
| Shared keywords, clearly different intent, boundaries explicit | **Pass** | Surface similarity only |
| Candidate is a genuine superset/replacement of a sibling | **Flag — escalate** | May warrant `status: replaced` + `superseded-by` on the older skill — but that's a human call, not an auto-block |

The Nimble healthcare skills are the worked example of *healthy* proximity: extract,
enrich, and verify all touch "providers," but each description ends with explicit
"Do NOT use for… — use [sibling] instead" lines. That mutual naming is what keeps
adjacent skills from colliding. A candidate that shares their space but *omits* those
lines is the blocking case — the fix is to add the boundary, not to kill the skill.

---

## The fix path (always name it)

A boundary block is the most fixable block in the battery — it's almost never "this
skill shouldn't exist," it's "this skill hasn't named its edge." So the verdict
should say exactly where:

- Which sibling it collides with.
- Which phrase or domain overlaps.
- The specific "Do NOT use for X — use [sibling]" line to add to *both*
  descriptions (collisions are mutual; fixing one side is half a fix).

---

## What this reference is NOT

- Not a triggering-accuracy test — that's skill-creator's eval (a *flag* check).
  Boundary collision is structural (does the trigger space overlap a sibling),
  not statistical (how often does it fire correctly).
- Not the schema's concern — `related` / `superseded-by` are DNA fields the human
  sets on a replacement decision; the auditor flags the candidate, it doesn't
  rewrite sibling frontmatter.
