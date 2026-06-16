# Claude Code Primer Pass — Teach the Producers to Emit Skill-Primer-Briefs

> **Status: COMPLETE** — Edits ran against `torres-core-lab`. Both `ecosystemic-thinking-partner` and `homelab-architect` now emit skill-primer-briefs. Filed here as a record of the pipeline-wiring decision.

**Purpose:** close the producer side of the skill-foundry handshake. The foundry can
*consume* a skill-primer-brief, but right now nothing *produces* one. This pass teaches
both the **ecosystemic-thinking-partner** and the **homelab-architect** to (a) notice
when a conversation is surfacing a skill-shaped opportunity, and (b) emit a
skill-primer-brief as one of their output options — to be dropped into the foundry's
`backlog-skill-starters/` or handed off directly.

**Run this in Claude Code** at the `torres-core-lab` repo (or wherever the user skills
live). It edits two skills and adds one shared reference. Review each diff before
committing.

---

## Context for the editing session (paste this first)

```
You're editing two sibling skills in the Torres-Core skill pipeline to teach them a new
output: the skill-primer-brief — a structured handoff that the skill-foundry (the fourth
pipeline skill) consumes to build a skill.

Background you need:
- The skill-foundry is the toolmaker of the pipeline. It builds skills from two intake
  types: skill-primer-briefs (clean intent) and foreign-skill-starters (messy external
  material). It already exists and can consume primer-briefs. The canonical contract for
  what a primer-brief contains lives in the foundry skill at
  references/skill-primer-brief-contract.md.
- Both the thinking-partner and the architect are well-placed to PRODUCE primer-briefs:
  the thinking-partner when an exploratory session surfaces a reusable behavior worth
  packaging; the architect when a design conversation reveals the same.
- This is the producer side of a handshake. The consumer (foundry) is built; you are
  wiring the producers.

Do NOT duplicate the full contract into each skill — both should POINT to the canonical
contract in the foundry (the same references-point-to-canonical discipline the skills
already use). Each skill gets: a short new output-mode section, a triggering cue for when
to offer it, and a pointer to the canonical contract.

Make the edits surgical. Match each skill's existing voice and section structure. Show me
each diff before committing.
```

---

## Edit 1 — ecosystemic-thinking-partner

**Add a new output mode.** The thinking-partner already produces architect briefs,
decision briefs, brainstorm recaps, and designed prompts. Add the **skill-primer-brief**
as a peer output.

```
In the ecosystemic-thinking-partner SKILL.md:

1. Find the section that lists the skill's output artifacts (architect brief, decision
   brief, brainstorm recap, designed prompt). Add the skill-primer-brief as a new output
   type in the same format the others use:

   "**Skill-primer-brief** — when a session surfaces a reusable BEHAVIOR worth packaging
   as a skill (not just a one-off answer), offer to emit a skill-primer-brief: a
   structured handoff the skill-foundry consumes to build the skill. Carries Purpose,
   Triggering Intent (when it should fire AND when it should NOT), Stance/Voice notes,
   What-it-is-NOT, and execution character. The foundry does the structural work; this
   brief carries the intent. Canonical contract:
   skill-foundry/references/skill-primer-brief-contract.md."

2. Add a triggering cue to whatever section governs WHEN the skill offers each output.
   The cue for noticing a skill-shaped opportunity:

   "When the conversation keeps returning to the same KIND of task, or the user describes
   a process they'll repeat, or you find yourself wishing a reusable tool existed for what
   you're working through — that's a skill-shaped opportunity. Name it: 'this sounds like
   it wants to be a skill — want me to draft a skill-primer-brief the foundry can build
   from?' Offer; don't impose. Generating skill IDEAS is in scope — the thinking-partner
   is well-placed to spot what tools the system is missing."

3. If the SKILL.md carries a type enum or output-artifact frontmatter list, ensure the
   primer-brief's output is represented consistently. The primer-brief itself is informal
   (it's exploratory output, doesn't need to be schema-perfect — the foundry formalizes).

Match the existing voice. Keep the addition proportional — a new output mode, not a rewrite.
```

---

## Edit 2 — homelab-architect

**Add the same output mode, framed for design conversations.**

```
In the homelab-architect SKILL.md:

1. Find where the skill describes its outputs (stack designs, deployment guides). Add the
   skill-primer-brief as an additional output the architect can produce when a design
   conversation surfaces a reusable behavior:

   "**Skill-primer-brief** — sometimes a design conversation reveals not a service to
   deploy but a reusable BEHAVIOR worth packaging as a skill (a recurring build pattern, a
   validation step done by hand repeatedly, a normalization the system keeps needing). When
   that happens, offer to emit a skill-primer-brief: a structured handoff the skill-foundry
   consumes. Carries Purpose, Triggering Intent, Stance/Voice, What-it-is-NOT, execution
   character. Canonical contract: skill-foundry/references/skill-primer-brief-contract.md."

2. Add the triggering cue, framed for the architect's context:

   "When a design keeps re-deriving the same procedure, or you spot a step that should be a
   reusable tool rather than re-explained each build, that's a skill-shaped opportunity.
   Name it: 'this build step sounds like it wants to be a skill — want a skill-primer-brief
   for the foundry?' Generating skill ideas from recurring build patterns is in scope."

3. The architect already knows the foundry exists (they're siblings). Make sure the
   pointer to the foundry's contract is consistent with how the architect references other
   canonical sources.

Match the existing voice and structure. Surgical addition, not a rewrite.
```

---

## Edit 3 — shared reference pointer (optional but recommended)

Both skills now point to `skill-foundry/references/skill-primer-brief-contract.md` as
canonical. That's correct — the contract has one home, in the consumer. No copy is made.

**Verify the path resolves.** If the skills are installed such that the foundry's
references aren't reachable by relative path, add a one-line note in each skill's
references section giving the absolute install path to the contract, so the pointer isn't
dead. Don't vendor the contract — just make the pointer findable.

---

## Verification

- [ ] thinking-partner SKILL.md lists skill-primer-brief as an output with a triggering cue
- [ ] architect SKILL.md does the same, framed for design conversations
- [ ] Both POINT to the canonical contract; neither duplicates it
- [ ] Both frame idea-generation (noticing skill-shaped opportunities) as in scope
- [ ] Each addition matches its skill's existing voice; no rewrites
- [ ] The contract pointer path resolves from where the skills are installed
- [ ] Diffs reviewed before commit

## Commit

```
git add -A && git commit -m "skills: teach thinking-partner + architect to emit skill-primer-briefs (foundry producer side)"
```

Don't push until the diffs are reviewed.

---

## Why this completes the handshake

The foundry was built consumer-first: it knows how to *receive* a primer-brief but nothing
*sent* one. After this pass, the explore→build seam for skill-making is whole — a
thinking-partner or architect session can notice "this wants to be a skill," emit the
brief, drop it in `backlog-skill-starters/`, and the foundry picks it up at triage. The
producers learn to *notice*; the consumer already knows how to *build*.
