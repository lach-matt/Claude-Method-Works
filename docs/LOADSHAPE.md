# The load-shape correction (2026-09-11)

**What was wrong.** `hourly3.py`'s reconstructed California load shape carried its seasonal term with
the wrong sign: `− ½(S−W)·cos(2π(doy−200)/365)` troughs at day 200. The comment said *peaks late July*;
the series peaked in January at 1.15× the annual mean and troughed in July at 0.85×, the opposite of
California's load. It was found by `profiles.py`'s shape statistics — the summer/winter ratio printed
0.75 where the constants say 1.36 — the first time the reconstruction was compared against itself.
The sign is corrected; the annual energy was pinned throughout and never moved.

**Why it mattered.** With winter load high and summer low, the December shortfall was overstated
(36 %), a seven-month *season* appeared where the corrected shape has a year-round, evening-led
shortfall, and the water route — which returns only October to April — looked at parity with the
mirrors. It is not.

## Before and after (mid / critical)

| | inverted shape | corrected shape |
|---|---|---|
| share of load served, as sized | 0.839 / 0.835 | **0.874 / 0.869** |
| unserved in July, share of month | 0.05 | **0.14 / 0.15** |
| unserved in December | 0.36 | **0.20 / 0.20** |
| mirrors route (cheapest closing to 1 %) | block ×1.5, field ×2, store 2 d | **block ×1.25, field ×1.5, store 2 d** |
| mirrors route, Title I $B (+$/MWh) | 10.2 / 16.9 (+60 / +100) | **5.7 / 9.5 (+34 / +56)** |
| whole-load price by mirrors, $/MWh | 185 / 302 | **159 / 258** |
| season (Oct–Apr) unserved, TWh | 2.48 / 2.55 | **1.20 / 1.25** |
| water route: modules at 500 m | 33 / 35 | **16 / 17** |
| water route: block, Title I $B | ×1.5, 11.3 / 18.2 | **×2.0, 11.2 / 17.0** |
| water against mirrors, power side | parity | **about 2×** |
| lift inside the surplus at critical | no (0.94 of the season) | **yes** |
| Title II capital, water route, $B | 62 / 102 | **30 / 50** |
| both (adopted): sizing | field ×1.25, store 1.5 d, 2,500 MW, 16–18 modules | **block ×1.25, field ×1.25, store 2 d, 1,500 MW, 8–9 modules** |
| both (adopted): Title I $B (+$/MWh) | 11.2 / 18.0 (+66 / +107) | **7.7 / 12.7 (+46 / +75)** |
| both: with water withheld / field at design | 7 % / 6 % | **1.5–1.7 % / 5.6–5.9 %** |
| program at the adopted route, $B | — | **55 / 93** |
| in-state RA, MW | 3,616 / 3,537 | **3,013 / 2,948** |
| mirror washing, AFY | 1,394 / 2,378 | **1,046 / 1,783** |
| land, acres (Westside covers a node) | 62,160 / 94,980 (4.8× / 1.9×) | **50,961 / 75,886 (5.9× / 2.4×)** |
| CO₂ avoided as sized, MMT/yr | 6.08 / 5.29 | **6.33 / 5.51** |
| permanent jobs, Title I (construction peak) | 1,901 / 1,214 (21,054) | **1,632 / 1,063 (17,545)** |
| gen-tie per node, MW | 1,196 / 1,179 | **1,194 / 1,190** |

Unchanged: the chain, the register and its price ($125 / $202), the receiver, the studies, the pilot
protocol, Title II's module and water price, the minors that do not read the hourly run.

## What changed in the instruments

- `hourly3.py`: the sign; `MIRRORS_ROUTE = (1.25, 1.5, 2.0)` now holds the mirrors sizing in one
  place, derived from `close()` at the 1 % target, and every instrument reads it rather than typing
  `1.5, 2.0, 2.0`. The selftest asserts the shape peaks in summer and that December is the worst
  month with no month under 5 %.
- `joinder.py`: the block scan runs to ×2.5; the selftest now asserts the water route costs 1.5–2.5×
  the mirrors on the power side and that the lift fits at both cases.
- `both.py`: the block is scanned (×1.25 / 1.5 / 2.0) rather than held at ×1.5, since the two routes
  no longer share a block.
- `majors.py`, `minors.py`, `titleone.py`, `rebase.py`, `rebase3.py`: read `MIRRORS_ROUTE`; the
  gen-tie is stated at the adopted route's block.

## What did not change in kind

The water route still returns a winter and still makes water the mirrors do not; the author's decision
— both — stands, at the even split, with the ladder printed. What moved is the price of the water
route on the power side and the size of everything downstream of the season. Documents rendered from
the instruments carry the corrected figures; the docs listed with a correction banner carry the
superseded ones in their prose and this file is the record of both.

## Year-round delivery (the author's decision, 2026-09-11)

Put to the author after the correction: the water route had returned only October to April, and on the
corrected shape the shortfall is year-round. **Decided: the water comes down year-round** (summer
irrigation and winter recharge), the even split kept. `hourly3.HYDRO_MONTHS` is all twelve, the
reservoir holds **30 / 60 days** of delivery (ASSUMED) rather than a season, and every closing point
must **lift its water inside its own run's surplus** — a lift bought from the grid is not this route.

| | Oct–Apr delivery | year-round delivery |
|---|---|---|
| water alone (field and store at design) | block ×2.0, $11.2 / $17.0 B | **no feasible point**: the block that closes the evening eats the spill the lift runs on |
| both (adopted, even split) | block ×1.25, field ×1.25, store 2 d, 8–9 modules, $7.7 / $12.7 B (+$46 / +$75) | **block ×1.5, field ×1.25, store 1 d, 1,500 MW, 15 / 17 modules, $6.4 / $10.3 B (+$38 / +$61)** |
| both against mirrors alone | 1.35× / 1.34× | **1.12× / 1.15×** |
| with the water withheld / field at design | 1.5–1.7 % / 5.6–5.9 % | **3.6–4.0 % / 1.3–1.4 %** |
| water, MAF/yr | 0.40 / 0.44 | **0.75 / 0.83** |
| Title II capital, $B | 15 / 25 | **28 / 48** |
| whole-load price on the adopted route, $/MWh | 171 / 277 | **163 / 263** |
| program at the adopted route, $B | 55 / 93 | **67 / 113** |

Year-round delivery makes the water a real lever again — each route carries a share the other cannot —
and the adopted route lands within fifteen percent of the mirrors on Title I's account while making
three quarters of a million acre-feet a year. `aquacost.py`'s water route is now the adopted route's water.
