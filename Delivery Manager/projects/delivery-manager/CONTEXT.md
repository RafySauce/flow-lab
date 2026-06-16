# projects/delivery-manager/ — Context

## What this project is

The meta-lane. This room holds work on the Delivery Manager itself — improving, automating, and streamlining the management process. It is also the Hermes prototype instrumentation layer: the folder-form version of the Homelab Manager agent that will eventually port to the self-hosted Hermes stack. Work here looks at the system, not through it.

## Current state

Harness build complete (2026-05-25): folder skeleton, CLAUDE.md, all CONTEXT files, board seeded, task definitions drafted. 4-lane board structure live. Next: board verification pass, first real capture end-to-end, register scheduled tasks, and eventually wire Planka when the self-hosted instance is ready.

## What this lane owns

- The harness itself: CLAUDE.md, CONTEXT files, routing model
- Scheduled task definitions and cadence tuning (`tasks/`)
- Planka wiring (when self-hosted instance is live)
- MCP-native board tools (future: read/write board.md via MCP gateway)
- DNA schema evolution as it affects this project
- Any improvement to the management process itself

## Process

When friction surfaces — a routing decision felt wrong, a CONTEXT.md didn't hold up, a scheduled task produced noise instead of signal — file a note in `harness/` first. If the friction is structural, propose a change here. Changes to CLAUDE.md or CONTEXT files are deliberate, not reactive; one session of friction does not warrant a rewrite.

## What gets promoted

- Design insights about the agent architecture → `harness/`
- Finished harness artifacts (designed prompts, task specs) → `corpus/`
- Signal-bearing management interactions → `traces/`
- Status changes → `review/board.md` (DELIVERY MANAGER lane)

## Skills

- `ecosystemic-thinking-partner` — for thinking through process improvements and agent architecture questions
- `schedule` — for wiring and adjusting scheduled task cadence
- `torres-rna` — for stamping artifacts when they go to corpus

## Open threads

- Board verification pass: drop all `[verify]` tags after confirming cards against reality
- First real capture end-to-end: intake → room → board card
- First trace promotion: flag a signal-bearing interaction and promote it
- Planka: wire when self-hosted instance is available (MCP connector, not cloud PM)
- Scheduled tasks: register tally (daily) and synthesis (weekly) via `schedule` skill
