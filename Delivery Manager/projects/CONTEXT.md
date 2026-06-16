# projects/ — Context (Room Template)

## What this room is for

`projects/` holds one subdirectory per active initiative. Each subdirectory is its own room with its own `CONTEXT.md`. This file doubles as the **template** for any new project room — when a room is minted, copy this structure and adapt.

Only two rooms are pre-built: `homelab/` and `hermes/`. All other projects stay in `intake/` until the heavyweight scheduled task proposes a room and Cincinnatus approves it.

## How a project room works

Each room is a contained workspace for one initiative. It holds:
- A `CONTEXT.md` (this template, adapted) describing the project's scope, current state, and working norms
- Work products produced during sessions in that room (or links to corpus items)
- Notes, decisions, and sub-threads relevant only to that initiative

Work products worth keeping cross the wall into `corpus/`. Signal-bearing interactions become traces in `traces/`. The project room itself holds working material — living, rough-edged, not necessarily stamped.

## Room creation checklist (when a new room is minted)

- [ ] Create `projects/[room-name]/` directory
- [ ] Copy this file to `projects/[room-name]/CONTEXT.md` and adapt it
- [ ] Add a card to `review/board.md` for the new initiative
- [ ] Route the relevant intake items into the new room

## Room template — adapt when copying

```
# projects/[room-name]/ — Context

## What this project is
[One paragraph: what the initiative is, why it exists, what done looks like.]

## Current state
[Two or three sentences: where things stand right now. Update this as the project moves.]

## Process
[How work flows in this room: how sessions start, how decisions get made, what gets promoted.]

## What lives here
[Working files, session notes, sub-threads specific to this project.]

## What gets promoted
- Finished artifacts → corpus/
- Signal-bearing interactions → traces/
- Status changes → review/board.md

## Skills
[Which skills are wired for this room.]

## Open threads
[Named blockers, pending decisions, next actions not yet on the board.]
```

## Skills

`ecosystemic-thinking-partner` is the default for genuine thinking work in any project room. `homelab-architect` is additionally available for homelab project rooms. `torres-rna` handles connection-wiring when artifacts are stamped.
