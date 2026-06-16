# Output Templates — Travel Planner v0.2

Eight output formats. In Plan mode, present Outputs 1–3 and 5 first (Phase A choices), then
build Outputs 4, 6, 7, and 8 after user selects flight and accommodation. Fill every section;
don't ship scaffolding prompts in the output.

---

## Output 1 — Flights & Lounge Brief

```
# Flight Options — [Origin] → [Destination] · [Dates]
*Prices pulled [date] — verify before booking; fares change.*

## Flight Options

| Option | Airline | Type | Depart | Arrive | Duration | Price (M1+F1 RT) |
|--------|---------|------|--------|--------|----------|-----------------|
| Cheapest direct | [Airline] | Nonstop | [time] | [time] | [Xh Ym] | $[X] |
| Best value w/ stop | [Airline] | 1 stop ([city]) | [time] | [time] | [Xh Ym] | $[X] |
| Premium / lie-flat | [Airline] | [type] | [time] | [time] | [Xh Ym] | $[X] |

## Priority Pass Lounge Alignment — [Departure Airport]

Available Priority Pass lounges at [airport code]:
- **[Lounge Name]** — Terminal [X], Gate area [X–XX] — [notes: food, showers, hours]
- **[Lounge Name]** — Terminal [X], Gate area [X–XX] — [notes]

**Lounge alignment check:**
- Cheapest direct ([Airline]) departs Terminal [X] → [lounge IS / IS NOT] in that terminal
- [If misaligned:] Lounge access requires Terminal [X]. Fare delta between lounge-aligned
  and cheapest option: $[X]. Worth it? Your call.
- [If aligned:] Cheapest direct and Priority Pass lounge are in the same terminal. ✓

## Recommendation
[One clear sentence: which flight gives the best combination of price, lounge access,
and duration. Flag any tradeoff plainly.]
```

---

## Output 2 — Accommodation Options

```
# Accommodation Options — [Destination] · [N nights]

## Option A — IHG (Platinum Elite)
**[Property Name]** · [Brand] · [Neighborhood]
- Rate: $[X]/night · Total: $[X] for [N] nights
- Platinum Elite perks: room upgrade (when available) · welcome amenity · guaranteed availability
- Location: [proximity to itinerary center — walkable to X, Y mins from Z]
- Standout: [one line on what makes it the right IHG choice here]
- Book at: ihg.com — confirm loyalty number is attached

## Option B — Boutique Hotel
**[Property Name]** · [Neighborhood]
- Rate: $[X]/night · Total: $[X] for [N] nights
- [Dog-friendly: yes/no — if dogs are traveling, only list if dog-friendly]
- Location: [proximity notes]
- Standout: [what makes it distinctive — local ownership, design, history, etc.]
- Book at: [platform or direct]

**[Second boutique option if available]**
- Rate: $[X]/night · Total: $[X] for [N] nights
- [Dog-friendly: yes/no]
- Standout: [one line]
- Book at: [platform]

## Option C — Unique Airbnb
**[Listing title or description]** · [Neighborhood]
- Rate: $[X]/night · Cleaning fee: $[X] · Total: $[X] for [N] nights
- [Dog-friendly: yes/no — dogs allowed flag]
- Location: [proximity notes]
- Standout: [what makes it unusual — historic building, exceptional host, unique setting, etc.]
- Host background: [any notable host credentials or reviews]
- Book at: airbnb.com — [listing link or search description]

**[Second Airbnb option if available]**
- Rate: $[X]/night · Total w/ fees: $[X]
- [Dog-friendly: yes/no]
- Standout: [one line]

## Notes
[Any caveats — cancellation policy differences, pet fees, deposit requirements, IHG
availability gaps if the property doesn't have strong inventory for these dates]
```

---

## Output 3 — Local Guide Discovery

```
# Local Guide Options — [Destination]

*Preference: degree holders, working artists, researchers, academics, longtime locals with
documented expertise. Not generic tour operators.*

## Guide 1 — [Name or Handle]
- **Background:** [degree / field / profession — e.g., "PhD in local history, University of X"]
- **Specialty:** [what they do — architectural walking tours, culinary deep dives, nature/ecology, art scene access, etc.]
- **Experience type:** [what a session with them looks like — 3-hour walking tour, private market visit, half-day, etc.]
- **Price:** $[X] per person · $[X] for two
- **Platform:** [Airbnb Experiences / Viator / direct booking / institution]
- **Why they fit:** [one sentence tying their background to what M1 + F1 are looking for on this trip]

## Guide 2 — [Name or Handle]
- **Background:** [credentials]
- **Specialty:** [focus area]
- **Experience type:** [format]
- **Price:** $[X]/person
- **Platform:** [booking source]
- **Why they fit:** [one sentence]

## Guide 3 — [Name or Handle, if strong third option exists]
- [same structure]

## Notes
[If no strong local guide options were found, say so plainly — "Guide discovery for [destination]
didn't surface strong expert-led options. Consider reaching out directly to [local university
department / cultural institution / food market] before departure."]
```

---

## Output 4 — Day-by-Day Itinerary

```
# [Destination] — [Date Range]
[M1 + F1] (+ [guests if any]) · [trip type] · Staying at: [chosen accommodation]

---

## Day 1 — [Day, Date]: [Theme or leg]

**Morning**
[Activity / transit / arrival logistics]

**Afternoon**
[Activity — favor cultural immersion and local food per profile. Note guide session here if booked.]

**Evening**
[Dinner: restaurant name, why it fits, allergy note if relevant]
[Accommodation: check-in note, Platinum Elite reminder if IHG]

---

[Repeat for each day]

---

## Transit & Logistics Summary
- Departure: [airport, chosen flight, Priority Pass lounge at departure]
- Return: [same]
- Getting around: [rental car / train / rideshare / driving own vehicle]
- Chosen accommodation: [property + confirmation approach]

## Pre-Departure Booking Checklist
- [ ] [High-demand reservation 1 — book before departure]
- [ ] [High-demand reservation 2]
- [ ] Chosen flight booked
- [ ] Accommodation booked (loyalty number attached if IHG)
- [ ] Guide session booked if desired
```

---

## Output 5 — Weather & Route Brief

```
# Weather Brief — [Destination] · [Dates]

## Destination Weather
[If near-term (<8 weeks):]
*Live forecast as of [date] — source: [weather service]*
- [Day-by-day or range summary: highs, lows, precipitation probability]
- What this means for packing: [specific additions or removals from standard list]

[If longer-term:]
*Historical climate estimate — not a forecast. Source: [climate data / Farmers Almanac]*
- [Month] in [Destination]: average high [X]°F / low [X]°F · average precipitation [X] days
- Farmers Almanac seasonal outlook: [brief note if available]
- Packing guidance based on historical norms: [specific additions]

## Route Weather (driving trips only)
*Major waypoints along [Origin] → [Destination] route:*

| Waypoint | Forecast / Historical Avg | Notes |
|----------|--------------------------|-------|
| [City/region 1] | [conditions] | [anything notable — mountain pass, flood risk, etc.] |
| [City/region 2] | [conditions] | |
| [Destination] | [conditions] | |

**Route weather impact on packing:**
- [Specific items to add based on route conditions — e.g., "rain gear for the Appalachian
  stretch," "extra layers for overnight mountain temps," "sunscreen for the desert section"]

## Packing List Adjustments
Based on weather above, add or flag the following items in the packing list:
- ADD: [item — reason]
- ADD: [item — reason]
- REMOVE or downgrade: [item — reason if conditions make it unnecessary]
```

---

## Output 6 — Packing List (weather-informed)

```
# Packing List — [Destination] · [Dates]
[Trip type] · [Travelers] · [Dogs: yes/no]
*Weather-adjusted for [conditions summary]*

---

## ⚠️ F1 Allergy Kit — Pack First
- [ ] EpiPen (2 if possible) — on F1's person at all times
- [ ] EpiPen not expired (check date)
- [ ] Allergy translation card [international: printed in destination language]
- [ ] Benadryl (backup antihistamine)

## M1 Medication Kit
- [ ] Tirzepatide pen — carry-on; dose date: [X]; extra pen packed
- [ ] Dupixent pen — carry-on; next dose falls [on/before/after] trip
- [ ] Prescription printout / doctor's note for injectables
- [ ] Sharps disposal container
- [ ] Gel/ice packs if cold storage needed (frozen solid at TSA)
- [ ] Zyrtec, ibuprofen, lidocaine patches, Tums/probiotics

## F1 Medication Kit
- [ ] EpiPen (listed above)
- [ ] Albuterol inhaler — carry-on; sufficient doses
- [ ] Lexapro — trip supply + 2 buffer days; carry-on [time zone note if applicable]
- [ ] B12

## Documents
- [ ] IDs / passports [international: 6-month validity check]
- [ ] Health insurance cards
- [ ] Chase Sapphire Preferred + backup card
- [ ] Cash (small bills)
- [ ] Emergency contacts written down
[International only:]
- [ ] Visa / ETIAS documentation (verify requirement before departure)
- [ ] Passport copies (cloud + physical)

## Tech & Entertainment
- [ ] Phones + chargers (M1 + F1)
- [ ] Tablets + chargers (M1 + F1)
- [ ] Media downloaded: podcasts, audiobooks, TV shows, movies
- [ ] Travel Roku
- [ ] GL.iNet Flint 1800 router (firmware current, WireGuard + Tailscale tested)
- [ ] Travel security camera
- [ ] Travel battery / power bank
- [ ] Travel solar panel [road trips]
- [ ] Universal travel adapter [international]
- [ ] Headphones / earbuds (M1 + F1)

## Clothing & Comfort — Weather-Adjusted
[Standard base:]
- [ ] [N] days of outfits + 1 extra day
- [ ] Change of clothes in carry-on [flights]
- [ ] Comfortable walking shoes

[Add based on weather output:]
- [ ] [Weather-specific item 1 — e.g., "insulated layer (overnight lows: 38°F along route)"]
- [ ] [Weather-specific item 2]

[Long-haul flights:]
- [ ] Neck pillow, eye mask, ear plugs

## Health & Hygiene
- [ ] Sanitary wipes, masks, gloves [flights]
- [ ] Hand sanitizer
- [ ] Sunscreen [adjust SPF for destination climate]
- [ ] Personal toiletries
- [ ] Band-aids / blister care

## Luggage
- [ ] Packing cubes
- [ ] Luggage locks [checked bags]
- [ ] Laundry bag
- [ ] Foldable tote for souvenirs

[Road Trip section:]
## Road Trip Kit
- [ ] Plug-in cooler
- [ ] Solar panel
- [ ] Car phone mount
- [ ] Roadside emergency kit
- [ ] Toll tag charged
- [ ] Offline maps downloaded (full route)

## Safety Kit [domestic road trips]
- [ ] Medical kit
- [ ] Bleed kit
- [ ] Mace
- [ ] Bully stick
- [ ] Pistol + ammo — ⚠️ verify transport laws for all states on route

[Dogs section:]
## Dog Kit
- [ ] Leashes + backup
- [ ] Travel water bottle
- [ ] Food: [N] days + 1 buffer day
- [ ] Collapsible bowls
- [ ] Toys + comfort item / bedding
- [ ] Dog medications (from cloud drive records)
- [ ] Dog medkit
- [ ] Dog carrying sling
- [ ] Waste bags (overpack)
- [ ] Vaccination records (digital)
- [ ] Car crate or seatbelt harness
- [ ] High-value treats
- [ ] Paper towels + wipes
- [ ] Pet insurance card / policy number
```

---

## Output 7 — Logistics & Safety Brief

```
# Logistics & Safety Brief — [Destination] · [Dates]

## Dog Care
[If dogs are home:]
- Care arrangement: [confirmed arrangement — daycare / friends / family]
- [ ] Caretaker briefed: itinerary · emergency contacts · feeding schedule · vet contact · pet insurance info
- [ ] Vaccination records current
- [ ] Dog tags + microchip current

[If dogs are traveling:]
- 24/7 emergency vet near [destination]: [Name, address, phone] — verified open 24/7
- Pet-friendly accommodation confirmed: [property name] ✓
- [ ] Pet deposit / fee confirmed at booking

## F1 Allergy Protocol
- EpiPen: on F1's person at all times — every departure, every day
- Flights: notify flight attendant at boarding every leg
- Restaurants: flag at reservation + at table, every meal
[International:] Translation card (text in Logistics section) — print multiple copies
[International:] High-risk dishes at destination: [list]

## Medication Logistics
**M1:** Tirzepatide next dose [date] · Dupixent next dose [date] · both carry-on · declared at TSA
**F1:** Lexapro daily · Albuterol carry-on · [time zone note if international]

## Loyalty & Financial
- IHG Platinum Elite perks: confirm at check-in (upgrade + welcome amenity)
- Priority Pass lounge at departure: [name, terminal, hours]
[Connection airport:] Priority Pass lounge: [name, terminal]
- All charges: Chase Sapphire Preferred
- Notify Chase of international travel before departure
- CSP travel insurance active: review limits for this trip cost

## Safety & Legal
[Domestic road trips:]
- Firearm transport: verify concealed carry reciprocity + transport rules for [states on route] before departure
[International:]
- Entry requirements: [visa status / ETIAS status]
- U.S. Embassy: [location + phone]
- Emergency services: [local number]
- English-speaking hospital near [destination]: [name + address + phone]
- Passport copies: cloud + physical (packed separately)

## Emergency Contacts
| Contact | Details |
|---------|---------|
| Each other | [M1 phone] / [F1 phone] — written down |
| Trusted home contact | [designate before departure] |
| Dog caretaker | [name + number] |
| [Embassy if international] | [number] |
| Local emergency | [number] |
| Chase Sapphire benefit line | on back of card |
| Prescribing doctors | [from records] |
```

---

## Output 8 — Cost Summary

```
# Cost Summary — [Destination] · [Dates]
*Prices as of [date]. Verify before booking — fares and rates fluctuate.*

## By Section

| Category | Details | Estimated Cost |
|----------|---------|---------------|
| Flights | [Airline], [type], M1 + F1 RT | $[X] |
| Accommodation | [Property], [N] nights @ $[X]/night | $[X] |
| Activities & Experiences | [Guide session + top bookings] | $[X] |
| Food & Dining | [N] days est. at $[X]/day for two | $[X] |
| Local transport | [Rideshare / train / rental car est.] | $[X] |
| Misc / buffer (10%) | | $[X] |
| **Subtotal (flights + hotel)** | | **$[X]** |

[Driving trips — add fuel section:]
## Fuel Cost Estimate

| Vehicle scenario | MPG | Distance | Gas price est. | Fuel cost |
|-----------------|-----|----------|---------------|-----------|
| Larger vehicle (truck/SUV) | 15 MPG | [X] miles | $[X]/gal | **$[X]** |
| Efficient vehicle (sedan/hybrid) | 32 MPG | [X] miles | $[X]/gal | **$[X]** |

*Distance: [X] miles total (round trip). Gas price: regional average as of [date] — source: [GasBuddy or AAA].*

## Total Trip Cost Estimate

[Flights only:]
| | Estimated Total |
|-|----------------|
| **Full trip** | **$[X]** |

[Driving trips:]
| | With 15 MPG vehicle | With 32 MPG vehicle |
|-|--------------------|--------------------|
| **Full trip** | **$[X]** | **$[X]** |
| **Difference** | | $[X] savings with efficient vehicle |

## Notes
- Accommodation total [includes / excludes] taxes and fees — add ~12–18% for final cost
- Guide session price: $[X] for both (confirm group pricing at booking)
- Food estimate is conservative for [luxury / mid-range] dining — actual may be higher at top restaurants
- Chase Sapphire Preferred travel insurance covers trip cancellation up to $[CSP limit] per person
```

---

## Output 9 — Trip Document (Combined)

Assemble all outputs into one mobile-readable document. Structure:

```
# [Destination] Trip — [Dates]
[Travelers] · [Trip type] · Staying: [property]
Generated: [date]

---

⚠️ ALLERGY ALERT [if F1 is traveling — always first]
[F1 allergy alert block]

---

## Quick Reference
- Flight: [airline, depart time, price]
- Accommodation: [property, address]
- Priority Pass lounge: [name, terminal]
- Emergency: [local number] · US Embassy: [if international]
- F1 allergy translation: [key phrase in local language, if international]

---

## Itinerary
[Output 4 content]

## Packing List
[Output 6 content]

## Logistics & Safety
[Output 7 content]

## Cost Summary
[Output 8 content]
```

Format for mobile: short paragraphs, bold the must-confirm items, checkboxes for packing
and pre-departure tasks.
