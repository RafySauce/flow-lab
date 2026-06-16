# Career Profile Contract

The standing-context files this skill reads at first move:
`career-profile-M1.md` and `career-profile-F1.md`, in the Skill Foundry workspace
(same pattern as `traveler-profile.md`). One file per person — two careers, two
profiles, no merging.

## Privacy rules for these files

- The files live in the user's own workspace (local/Proton Drive), not inside the
  skill package. The skill reads them; it never embeds their contents into another
  artifact except the output documents the user reviews.
- **Deep profile authoring is local-first.** The full interview below is best run
  against local models. In a cloud session, offer the flag once: "this interview
  covers your complete career history — want to run it locally and hand me the
  file instead?" Then respect the call.
- Profile content never enters a web query (see SKILL.md Privacy Stance).

## Profile shape

```markdown
# Career Profile — <M1|F1>
updated: YYYY-MM-DD

## Identity & logistics
Name and contact block (used ONLY in output documents), location, commute/remote
constraints, languages, current employment status.

## Experience (depth is the whole game)
Per role: title, org, dates — then what was ACTUALLY done: specific projects,
tools, responsibilities, measurable outcomes. Not a title list. "Built X with Y,
which produced Z" beats "managed projects."

## Skills in context
Each skill anchored to where it was applied. "Python" is thin;
"built ML pipelines for churn prediction in Python/scikit-learn" is usable.

## Education, certifications, publications, awards
Standard list, most recent first.

## What energizes / what drains
Free-form. Feeds culture-fit scoring and latent-opportunity discovery.

## Target roles & sectors
Explicit targets, plus "open to adjacent" if true. Feeds Scout queries.

## Deal-breakers (hard constraints — these are pass/fail gates)
Relocation, travel ceilings, salary floor, sector exclusions, schedule
constraints, values lines. The evaluation framework fails a posting on any of
these without negotiation.

## Self-assessment (OPTIONAL)
A few honest lines on working style, strengths, growth areas, environments where
this person thrives or struggles. A formal instrument (PI/DISC) can slot in if
one exists, but is not required and not solicited.
```

## The profile interview (when a file is missing or thin)

Two entry paths, same principle — richer input, sharper output:
1. **Import**: read an existing CV/resume the user provides, populate the shape,
   then ask only the gaps (energize/drain, deal-breakers, targets).
2. **Interview**: walk the sections conversationally, one at a time. Push for
   specifics on experience — projects, tools, outcomes — and for honesty on
   deal-breakers. What's written here gates every future evaluation.

## Latent-opportunity discovery (harvested from source, worth keeping)

The profile supports two search postures: **explicit targeting** (known roles,
refine and prioritize) and **latent discovery** — mining the actual work history,
not the titles, for transferable patterns: skills that map to unexpected sectors,
threads in what energized them, emerging roles combining their domain with new
tech. When a profile is rich enough, Scout may propose one "you didn't ask for
this, but look" category per run. Label it as such.
