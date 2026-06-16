# Audit Battery — the master checklist

The full set of checks the auditor runs, the instrument each one wraps, its
severity, and how the three modes weight them. Read this at the start of every
audit. The SKILL.md carries the summary table; this file carries the *how*.

The governing rule (from the SKILL.md): **block only on the objective, flag on the
subjective.** "Fail" is reserved for things that are deterministically, checkably
wrong. Everything that needs human judgment *flags* — it reaches Cincinnatus as a
note, not a locked door.

---

## The three modes

| Mode | Called by | Question it answers | Battery weight |
|---|---|---|---|
| **Intake** | foundry, during triage of foreign material | "Should this enter the corpus at all?" | Foreign-source vetting + security run first and hard; the rest is preliminary (the skill isn't house-shaped yet) |
| **Gate** | foundry, after emit, before promotion | "Is this safe and correct to promote?" | Full battery, all checks, binding verdict |
| **Standalone** | Cincinnatus, on any candidate | "Tell me the truth about this skill." | Full battery; report, no folder move expected |

In **intake mode** the skill is still foreign — it won't have a DNA vault-doc, may
not be in agentskills.io shape, and shouldn't be graded as if it were house-built.
Run foreign-source vetting and the security read; note schema/voice as "N/A —
pre-normalization." The output is a go/no-go on *bringing it in to be normalized*,
not a promotion verdict.

In **gate** and **standalone** modes the skill is house-shaped (a SKILL.md + DNA
vault-doc), so the full battery applies.

---

## The checks, in severity order

Run blocking checks first. If one fails hard, the verdict is already BLOCKED — but
finish the battery anyway when cheap, so the report is complete and the user fixes
everything in one pass rather than discovering blocks one at a time.

### 1. Schema / DNA validity — BLOCKING

Wrap **torres-rna**. Validate the companion vault-doc's frontmatter against the
canonical `dna-spec.md`:
- Required fields present and well-formed for `type: skill`.
- `truth-level` is `to-review` (a skill arriving at the gate should not already
  claim `verified` — if it does, that's a self-promotion flag, escalate).
- `generated-by` + `skill-version` both present (they travel together).
- No unrecognized fields (the foundry never extends the schema; an unknown field is
  a defect).

If canonical `dna-spec.md` is unreachable in the current environment, say so and
validate against the foundry's `dna-spec-extract.md` as a fallback — and **lower the
confidence** of this check in the verdict (extract-validated, not canonical-validated).

### 2. Install-limit compliance — BLOCKING

Measure the SKILL.md frontmatter, don't eyeball it. The loader rejects on:
- `name` ≤ 64 chars
- `description` ≤ 1024 chars
- `compatibility` ≤ 500 chars

A simple measurement (the `scripts/measure_frontmatter.py` helper, or
skill-creator's `quick_validate.py` if present). Over-limit = un-installable =
hard block. If `compatibility` is over, the fix is almost always "move body-content
out of the field," not "trim words."

### 3. Security / safety — BLOCKING

The auditor's first original muscle. Wrap the **`security-review` command** for the
general pass, then apply `references/security-read.md` for the skill-specific
patterns the general review doesn't center: script egress/subprocess behavior,
prompt-injection planted in references, over-broad tool grants, and
sovereignty/phone-home. A *confirmed* finding in any of these blocks. A *suspicion*
that needs human eyes flags (and says exactly what to look at). Never wave a skill
through on "probably fine"; never block on a vibe — confirm against the file.

### 4. Boundary collision — BLOCKING (duplicate) / FLAG (proximity)

The auditor's second original muscle. Diff the candidate's `description` and trigger
phrasing against the sibling corpus (see `references/boundary-collision.md`). A
**true duplicate trigger** — two skills that will both fire on the same phrasing with
no disambiguating boundary — is blocking: it corrupts routing for the whole family.
Mere **proximity** (adjacent domains, shared keywords, but distinct boundaries that
each skill names) is a flag with a suggested wording tweak-spot.

### 5. Triggering accuracy — FLAG

Wrap skill-creator's eval (`run_eval` / `run_loop`). Low should-trigger /
should-not-trigger scores are *iteration fuel*, not a safety gate — a skill that
under-triggers is improvable, not dangerous. Report the score and the worst
misfires; never block on it. (Environment note: `run_loop` needs `claude -p`; in
claude.ai it's unavailable — assess the description manually against the corpus
instead, and say so.)

### 6. Behavioral quality — FLAG

Wrap skill-creator's eval loop on a few realistic prompts. Quality is *improved*
through the foundry's iteration loop, not *gated* by the auditor. Surface concrete
weaknesses; leave the block to the objective checks.

### 7. Voice coherence — FLAG

Does it read as a sibling? Check against the house-voice rubric below. You can't
deterministically "fail" voice, so this always flags, never blocks.

**House-voice rubric (quick):**
- Has an identity/stance paragraph and a "What This Skill Is Not" section.
- References point to canonical sources, not frozen copies.
- Explains *why*, not just *what* (few or no all-caps MUSTs).
- Boundary discipline is explicit — the skill names its edges.
- Tone matches the siblings: warm, precise, teaching by layers.

---

## Foreign-source vetting (intake mode)

This is the auditor's third original muscle, and it **points to the foundry's
canonical contract rather than copying it.** Read
`skill-foundry-v1/references/foreign-skill-starter-contract.md` for the foundry's
source-vetting spec (maintenance, provenance, license, security read). The auditor
adds only the *verdict layer* on top of that contract:

- **Maintenance** — is the source alive (recent commits, open issues addressed) or
  abandoned? Abandoned ≠ automatic block, but it flags and shifts the burden: the
  lab now owns it.
- **Provenance** — who wrote it, can it be trusted, is the license compatible with
  bringing it in-house? A license trap (copyleft that would infect the corpus, or no
  license at all) blocks until resolved.
- **Security** — run check #3 on the foreign material *before* normalization, when
  the hostile code (if any) is still in its original form. This is the cheapest
  place to catch a launderable skill.
- **Verdict** — go (normalize it), no-go (drop it, with the reason), or
  conditional (bring it in only after the named fix).

The division of labor: the **foundry's** contract says *how to vet*; the
**auditor** renders the *go/no-go verdict* from that vetting. No duplication — the
auditor reads the foundry's contract and decides.

---

## What this reference is NOT

- Not the schema (that's `dna-spec.md`), not the security-review command's own
  rules, not skill-creator's eval docs. It's the *orchestration map* — which
  instrument to play for which check, and how loud each one gets to be in the
  verdict.
