# `tools/both.py` — the season closed by both routes (the author's decision)

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why it exists.** Title III put two routes to the author for closing Title I's October-to-April
season: mirrors (block ×1.5, a second day of store, field ×2) or water (block ×1.5 and Title II's
product lifted on the summer surplus, returned through pump-turbines), at parity on the power side.
The author's answer, 2026-09-11: **both**. Both is a combination and not a sum — the field and store
sized smaller than the mirrors route, the water returning part of the season — and this file sizes
and prices it, at mid and at critical, under the standing rule that the design is held to critical.

**Run it.** `python3 tools/both.py` prints the ladder and the adopted point (`--selftest` pins them).
Stdlib only; it runs `hourly3.py` about two hundred times per case, a minute or two in all.

## What it scans

Block held at ×1.5 (nothing else serves a July evening). Free axes: the field factor
(1.0–2.0), the store in days (1.0–2.0), the pump-turbine plant (1,000 / 1,500 / 2,500 MW) and the
**water's share of the season** (0, ¼, ½, ¾, 1), where a share is that fraction of the full water
route's modules, reservoir and hydro budget. At each share the cheapest closing point (≤ 1 % left to
the grid) on Title I's account is the rung; the mirrors route is the share-0 rung and the water route
the share-1 rung.

## The ladder, mid (critical in the report)

| water share | field | store, d | hydro MW | Title I $B | + $/MWh | modules | MAF/yr | water out | field out |
|---|---|---|---|---|---|---|---|---|---|
| 0 (mirrors) | 1.75 | 2.0 | 0 | 8.7 | 52 | 0 | 0 | 0.9 % | 12.7 % |
| ¼ | 1.75 | 1.0 | 1,500 | 10.3 | 61 | 8.2 | 0.41 | 3.2 % | 9.3 % |
| **½ (adopted)** | **1.25** | **1.5** | **2,500** | **11.2** | **66** | **16.4** | **0.82** | **7.0 %** | **5.9 %** |
| ¾ | 1.25 | 1.0 | 2,500 | 11.5 | 68 | 24.6 | 1.23 | 8.0 % | 2.5 % |
| 1 (water) | 1.00 | 1.0 | 2,500 | 11.3 | 67 | 32.8 | 1.64 | 12.7 % | 0.6 % |

"Water out" and "field out" are the same plant with that route withheld, run hour by hour; as sized
with neither route, 12.7 % is left to the grid. At critical the adopted rung is the same sizing at
**$18.0 B, +$107/MWh**, 17.6 modules and 0.88 MAF/yr.

## What it found

- **Both costs more than mirrors alone on Title I's account** — $11.2 B against $8.7 B at mid —
  because the pump-turbine plant is bought whole whatever share of the season it returns. It is not
  the cheapest way to close the load and the file says so.
- **What it buys is resilience.** With either route out the adopted plant leaves 6–7 % to the grid
  against 13 % with neither: two levers that fail differently, neither at its full extent.
- **A cheapest-point search does not find "both".** Asked only for the cheapest closing point with
  both levers engaged, the scan returns field ×1.75 with a token 1,000–1,500 MW water plant returning
  a tenth of a terawatt-hour at critical — both in name. The even split is therefore adopted as the
  author's word read literally, `ADOPTED_SHARE = 0.5`, marked DECIDED, and the ladder is printed so
  the split can be moved.
- **The finer scan finds a cheaper mirrors point** than `hourly3.py`'s stated closing (field ×1.75,
  store 2 d at $8.7 B against field ×2 at $10.2 B). The Titles keep the stated mirrors sizing as the
  mirrors route; the difference is recorded here and does not change the decision.
- **Both in full** (field ×2, store 2 d, the whole water route) closes to 0.0 % at $19.0 / $31.9 B
  and throws away 12 TWh of surplus: the margin case, printed and not adopted.

## Where it lands

Title III §2 now records the decision as made, with a third column in the decision table and the
one-route-out rows; §3 adds the program total at the adopted route; §4's severability states that
Title I without Title II reverts to the mirrors sizing. Title I §4 carries the adopted route beside
the two it combines, and §5 prices the household at it. The Title II side is the water route at half
scale: 16–18 modules, $31 / $51 B, on Title II's own account.

## The two site assumptions, as a band (2026-09-11)

The adopted point rests on two site assumptions: 500 m of head and a reservoir holding 30 / 60 days of
delivery. Neither can be settled without a site, so `both.py`'s `sensitivity()` prices the adopted
point across them with the hourly run held fixed. At fixed share the returned energy is what the run
dispatched, so the water volume goes as 1/head, the modules and Title II capital with it, the lift is
invariant in head, and the reservoir is the only term the days touch.

| head, m | modules (mid / critical) | MAF/yr | Title II $B | Title I $B at 14 → 90 days |
|---|---|---|---|---|
| 300 | 25.1 / 27.7 | 1.25 / 1.38 | 47 / 80 | 6.3–7.1 / 9.9–11.3 |
| 500 | 15.0 / 16.6 | 0.75 / 0.83 | 28 / 48 | 6.3–6.8 / 9.8–10.7 |
| 800 | 9.4 / 10.4 | 0.47 / 0.52 | 18 / 30 | 6.2–6.5 / 9.7–10.3 |

The lift fits inside the surplus at every head, so the route's feasibility does not depend on the
site. **The head is the site question that sizes Title II** — a factor of 2.7 in modules and capital
across the band — and the days of holding move Title I by under a billion dollars. The selftest pins
the lift's invariance, the 1/head scaling, the monotone cost in days, and that 500 m at the design's
days reproduces the adopted point exactly.
