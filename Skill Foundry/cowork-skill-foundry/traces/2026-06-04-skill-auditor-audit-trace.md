---
date: 2026-06-04
skill: skill-auditor
auditor-version: "0.1"
mode: gate
independence: inline-self-audit
verdict: CLEAR
blocking-failures: 0
flags: 2
---

# Audit — skill-auditor

## Verdict: CLEAR

The auditor's first run was on itself. After one blocking failure was found and
fixed mid-audit (the over-limit description), the battery is clean: no blocking
failures remain. Promotion is **unlocked, not performed** — the skill stays at
`truth-level: to-review` awaiting Cincinnatus's release. Confidence is lowered one
notch: this was an **inline self-audit** (no fresh subagent), the exact dependency
the skill warns against. A second-pass audit by an independent agent is recommended
before release.

## Battery results

| Check | Severity | Result | Note |
|---|---|---|---|
| Schema / DNA validity | blocking | pass* | vault-doc has all `type: skill` fields; *validated against `dna-spec-extract.md`, not canonical (unreachable) — RNA to re-check |
| Install limits | blocking | pass | name 13 / desc 982 / compat 313 — all under limit (desc was 1127, fixed) |
| Security / safety | blocking | pass | one helper script (`measure_frontmatter.py`): read-only, stdlib only, no network/subprocess/egress |
| Boundary collision | blocking/flag | FLAG | proximity to skill-foundry on "foreign material"; distinct verbs + auditor names foundry → not a duplicate |
| Triggering accuracy | flag | deferred | full eval (`run_loop`) deferred to the human-reviewed description pass per foundry guidance |
| Behavioral quality | flag | n/a | no end-to-end run yet; verdict format dogfooded by writing this trace |
| Voice coherence | flag | pass | identity/stance, What This Skill Is Not, references-point-to-canonical, explains why — reads as a sibling |

## Blocks (resolved during audit)

- **Install limit — description over 1024 chars (was 1127).** `SKILL.md` frontmatter.
  Fix applied: trimmed the battery enumeration and orchestration clause to 982 chars;
  re-measured to pass. (Recorded because the block was real even though same-session
  fixed — the gate caught it.)

## Flags — notes for Cincinnatus, not blockers

- **Boundary proximity to skill-foundry.** Both descriptions reference foreign
  material. Mitigated by distinct verbs (build/normalize vs. audit/vet/gate) and the
  auditor naming the foundry. Mutual fix available: add a "for safety vetting, use
  skill-auditor" pointer to the foundry's description when there's headroom (it's at
  1000/1024). Low urgency.
- **Inline self-audit.** This verdict was produced without an independent subagent.
  Treat as provisional; re-audit independently before release to `verified`.

## Consequence

CLEAR → promotion unlocked, not performed. Skill stays at `to-review` with this
verdict attached. Cincinnatus releases to `verified` and moves the pair to
`completed-skills/`.

## Capability this audit embodies

**The gate caught its own gate.** The first thing the install-limit check did was
block the skill that contains it — concrete evidence the objective checks fail
loudly and the fix path is actionable. The boundary-collision check also surfaced a
real-but-minor sibling proximity that no single-skill triggering eval would have
seen, validating the corpus-diff as a distinct muscle.
