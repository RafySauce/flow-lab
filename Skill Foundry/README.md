# Cowork Project — Skill Foundry

The workshop for building, normalizing, and reviewing Torres-Core skills. Instantiated
from the Cowork Project Template (Van Clief three-layer routing = Hermes agent
containment), `instrumented: true`.

## Why instrumented

Hermes will inherit this responsibility and process. That makes the instrument module
load-bearing rather than decorative: the foundry's triage -> vet -> normalize -> review
workflow is a Hermes agent spec being written in slow motion. Every build, every drop,
every execution-tier call is a trace the future skill-foundry-agent learns from. The
synthesis task's migration targets are concrete (a specific Hermes agent behavior, a
gateway rule, an MCP-skill) because the destination is known.

## Layout

```
cowork-skill-foundry/
├── CLAUDE.md              # the map: identity, routing, rules, instrumented: true
├── 00-intake/            # unsorted thought-catcher (upstream of the queue)
├── _template/            # copy-me room
│   ── work rooms ──
├── intake-triage/        # classify + vet every starter
├── forge/                # build / normalize to house standard
├── review-bench/         # the human verified gate
│   ── instrument module ──
├── corpus/               # finished-skill records accumulate
├── traces/               # flagged foundry decisions, capability-stamped
├── synthesis/            # scheduled findings -> Hermes targets (source: ai)
├── tasks/                # the two scheduled tasks (tally + synthesis)
├── harness/              # the emergent Hermes skill-foundry-agent design
│   ── queue + skills ──
├── backlog-skill-starters/  # inbox queue (truth-level: claimed)
├── completed-skills/        # done queue (truth-level: verified)
└── skills/                  # the skill-foundry skill wires in here
```

## Two adaptations from the base template (worth noting)

1. **Queue folders alongside rooms.** Rooms are *modes of work*; the queue folders
   (`backlog-skill-starters/`, `completed-skills/`) are *where the work-product
   physically sits as it moves*. The base template doesn't have this second axis —
   the foundry does, because skills are durable artifacts that flow through states,
   not just conversations that happen in rooms. They compose: a starter sits in the
   backlog queue while the triage and forge rooms act on it.

2. **The capability enum is foundry-specific.** The trace scaffold's `capability`
   field is refined from the template's generic enum to this project's actual modes:
   `triage | vet | normalize | author | route | review | decide`. This is the
   intended evolution path — the template says to refine the enum as use reveals gaps.

## The verified gate is deliberately human

Hermes can eventually triage, vet, and normalize. But "is this skill good enough to be
verified" stays a human (or council) judgment — `/review-bench` and the `harness/` open
seam both preserve this. It mirrors the foundry skill's own "never self-promote to
verified" rule. Automate the toil; keep the judgment.

## To instantiate

This project is already scaffolded and drop-in ready. If rebuilding from scratch in a
fresh Cowork chat, the template's Part 3 setup-prompt walks the guided build — but the
answers are already decided: instrumented true (Hermes inherits), three work rooms
(intake-triage, forge, review-bench), queue folders alongside.

## Connection Notes

*Un-verified hints for the vault-side connection skill.*

- Built from: [[cowork-project-template]] — the standard of record this instantiates
- Houses: the skill-foundry skill (the HOW; this project is the WHERE)
- Carries across to: the Hermes skill-foundry-agent (the harness room is its larval spec)
- Stamps against: [[dna-spec]] — every artifact's frontmatter
- Entities likely in play: hermes, obsidian, skill-foundry
