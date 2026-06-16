# review/ — Context

## What this room is for

The cockpit surface. `review/` is where Cincinnatus checks what's happening, what's next, and what's blocked. It holds the canonical status board and the rolling pulse log. This is the room to open when starting a session without a specific task in mind.

## Files in this room

### `board.md` — the canonical Kanban (source of truth)
A markdown Kanban with four columns:
- **Backlog** — not started; no active next action
- **Active** — in motion now; has a stated next action
- **Blocked** — waiting on a named dependency; the dependency must be named on the card
- **Done** — steady state; no next action

Cards belong to one of two swim lanes: **HOMELAB** and **HERMES / AI COUNCIL**. New swim lanes are added when a new project room is minted.

Card format:
```
- **[Service or initiative name]** ([location if relevant]) — one-line status. -> next: [next action or "nothing; steady state"].
```

Blocked cards must name what they are blocked on. A card with no named blocker is not a valid Blocked card — it belongs in Backlog.

`board.md` is permanently canonical. The eventual visual surface (Planka, self-hosted) is a presentation skin — it reads from and pushes to `board.md`, never the reverse. No commercial cloud PM connector is wired here.

### `pulse.md` — the rolling tally log (one-liner per tally run)
The lightweight scheduled task appends a single dated line here on each run. Format:
```
YYYY-MM-DD: [intake count] intake | [corpus count] corpus | [traces count] traces | [flags if any]
```
This makes trends in what Cincinnatus is capturing visible over time without proliferating files. `pulse.md` is appended, never rewritten. It is signal, not noise — keep the lines short.

## Process

**Starting a session:** read `board.md` first. Find the Active card for the work you're about to do. Confirm the next action is still accurate. If the board is stale, update it before starting work.

**Ending a session:** update the relevant card(s). Move cards that have changed state. Add any new cards that emerged. One commit covers the board update and the session work.

**Board hygiene:** a card in Active with no next action, or a card in Blocked with no named dependency, is a bug. Fix it when you see it.

## What good work looks like

The board reflects reality, not aspiration. Cards say where things actually are, not where they were supposed to be. Blocked cards name their blocker. Done cards say "steady state" only when they genuinely are.
