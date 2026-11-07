---
id: comms-types-and-lanes
title: "Comms Types and Lanes"
type: specification
artifact-version: "1.0"
status: living
truth-level: to-review
created: 2026-11-07
updated: 2026-11-07
owner: operator
source: human+ai
generated-by: flow-foundry
generated-by-version: "1.5"
data-class: public
related:
  - "[[comms-builder]]"
---

# Comms Types and Lanes

Stage 1 reads this file to propose a comms type and a lane. Stage 4 reads
the touchpoint sets. The user always has the last word on both.

## Comms types

| Type | Use when | Example subjects |
|---|---|---|
| Awareness | People should know; nobody has to do anything | A shared service gains a feature; a project milestone lands |
| Action required | Some segment must do something by a date | Re-register a client certificate; update a connection string |
| Change implementation | A scheduled change affects services, often with validation and an implementation event | Platform upgrade in a weekend window; shared-service migration |
| Response plan | A CVE or incident needs a coordinated response | Patch rollout for a critical vulnerability; incident status and recovery steps |

## Lane rule

The flow **suggests a campaign** when any of these is true, and names which
fired:

1. **Many stakeholders.** A large-scale change touching three or more
   segments, or more than one business area.
2. **Validation needed.** Application teams must confirm their services
   before, during, or after the change.
3. **Multi-stakeholder project.** A project whose stakeholders need
   different content at different times.

Otherwise it suggests a **one-off**. A response plan defaults to campaign
when it runs longer than one business day (initial notice, updates,
resolved).

## Default touchpoint sets (campaign)

Offsets are relative to the key date (T). The user adjusts all of them.

| Type | Touchpoints |
|---|---|
| Awareness | T-7 announce · T day-of note (optional) |
| Action required | T-14 announce with the ask · T-5 reminder to those not done · T deadline-day note · T+1 confirmation |
| Change implementation | T-14 announce · T-7 validation request to validating teams · T-2 reminder and bridge invite · T day-of start notice · T all-clear (or delay notice, held in reserve) · T+1 validation summary |
| Response plan | T initial notice (what, who is affected, what to do now) · updates at an agreed cadence · resolved notice · follow-up with any remaining actions |

## Response-plan data rule

CVE and incident comms carry **impact, timing, and the actions people must
take**. They never carry exploit details, configurations, IP addresses,
hostnames beyond service names, or descriptions of security controls. Those
stay in the security or incident record and are referenced by number only.
Stages 2, 5, and 8 each re-check this rule.

## Non-goals

- Sending anything. Every message leaves as a draft a person sends.
- External customer communications (regulated; owned by the employer's
  marketing and compliance functions).
- Organization or HR announcements about named people.
- Executive status decks (use `executive-slide-digest`).
