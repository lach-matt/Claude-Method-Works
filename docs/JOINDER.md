# `tools/joinder.py` — Title III: can Title II return Title I's winter?

> **Corrected 2026-09-11.** Figures in this file computed before the load-shape correction (`docs/LOADSHAPE.md`)
> are superseded: the reconstructed load had its seasonal term inverted. The instrument's current output is
> authoritative; the corrected headline figures are in `docs/LOADSHAPE.md` and `CLAUDE.md`.

**Why it exists.** `hourly3.py` found that a sun-following plant sized on the annual energy
serves 84 % of the load: a third of December goes unserved while a quarter of June's field is
defocused, and sixteen hours of store cannot move June into December. The author (2026-09-11):
water stores across seasons and electricity does not — desalinate on the summer surplus, hold
the water, *"and the offset is returned from the desalination plants from their turbines"*; then,
*not more storage on the power side* — more hydro at the plants, or more modules? This file
prices all of it, at mid and at critical, against the shortfall `hourly3.py` measured, and says
what closes and what it costs.

**Run it.** `python3 tools/joinder.py` (it runs `hourly3.py` some dozens of times, several
minutes), `--selftest` for the checks. Stdlib only; imports the shortfall and the surplus from
`hourly3.py`, the cycle and cost lines from `cspchain.py` and `firmpower.py`, and restates none.

## The season and the surplus, from the hour-by-hour

The shortfall is not a winter: hour by hour it runs **October to April**, seven months, and
the evening in every month.

| | mid | critical |
|---|---|---|
| season (Oct–Apr) unserved, TWh_e | 2.48 | 2.52 |
| summer surplus thrown away, TWh_e (defocused field at the cycle efficiency + curtailed PV) | 3.20 | 3.29 |

## A. Steam-topping turbines at the desalination plant

Title II's own architecture: solar-thermal skids, steam through a back-pressure turbine, the
exhaust heat into LT-MED. Per m³ the turbine takes in 105 kWh_th to leave the 70 kWh_th LT-MED
needs and returns 34.5 kWh_e (mid) — but the same heat condensing makes 52.2 kWh_e with no
water, so **the water costs 19.3 kWh_e per m³, 6.4× reverse osmosis** (18.0 and 5.0× at
critical). The topping turbine returns electricity it was given as heat, less what the water
took, and in winter only what heat is there in winter — which F-13 and F-27 found is none at a
module's scale on a coastal brownfield. **This turbine does not return a winter; it makes water
dear in summer.**

## B. Hydraulic turbines on the water itself

Summer surplus desalinates *and* lifts the product water to an elevated off-stream reservoir;
in the short season it is delivered downhill through pump-turbines to the aqueduct and to
groundwater recharge, and the head comes back. Pumped storage whose working fluid is the state's
own water supply, on the pattern of San Luis and Gianelli. Energy per m³ is ρ·g·H·η: at 500 m
and 0.90, 1.23 kWh_e returned per m³ against 1.51 to lift it (round trip 0.81); at critical,
300 m and 0.85, 0.69 against 0.96 (0.72).

If the surplus must both desalinate and lift, it makes **0.7 km³ a year** (11.5 modules' output)
and returns **35 % of the season at mid, 20 % at critical**, for $2.0 / $3.1 B. Bounded by the
surplus, cheaper per TWh than the mirrors, and not a closure.

## C. More modules, not more storage

Hydro output at a plant is volume × head, and a coastal plant is at sea level: **the head is
where the water comes down**, a property of the reservoir site, not of the plant. So the
levers are the author's two, volume (modules) and head (site), and head is worth more: each
doubling halves the water. Put the water on **Title II's own account** — its cost model already
carries its energy line — and Title I's surplus is spent on the *lift alone*:

| | head, m | modules | M acre-feet/yr | km³ | lift, TWh_e | surplus, TWh_e |
|---|---|---|---|---|---|---|
| mid | 300 | 54.7 | 2.73 | 3.37 | 3.06 | 3.20 fits |
| mid | 500 | **32.8** | **1.64** | 2.02 | 3.06 | 3.20 fits |
| mid | 800 | 20.5 | 1.03 | 1.26 | 3.06 | 3.20 fits |
| critical | 300 | 58.8 | 2.94 | 3.62 | 3.49 | 3.29 **does not fit** |
| critical | 500 | **35.3** | **1.76** | 2.17 | 3.49 | 3.29 does not fit |
| critical | 800 | 22.0 | 1.10 | 1.36 | 3.49 | 3.29 does not fit |

Two things the table shows. **The lift does not depend on head** — it is the returned energy
over the round trip — so whether the surplus can lift the season is a fixed fact per case: at
mid it fits; **at critical it does not**, the surplus returning 0.94 of the season, and the
selftest pins that as a finding rather than repairing it. And the water is a lot: 1.6 to 1.8
million acre-feet a year at 500 m, 33 to 35 modules of 50,000 acre-feet, delivered October to
April — which is what SGMA groundwater recharge in the San Joaquin is short of by about that
much. What the modules cost is Title II's to price (F-16 says their capex is understated three-
to four-fold); what this file prices is the reservoir and the pump-generation.

## D. The evening, with the season closed by water

The hydro plant must be sized to the **evening** shortfall, not the season's average, and the
block must still carry a July evening, which no water can. At 500 m of head, block and hydro
plant scanned, field and store at design, cheapest point under 1 % unserved (the residue is the
grid's):

| | block × | hydro plant, MW | unserved | water, km³ | modules | block, $B | water, $B | total, $B | + $/MWh |
|---|---|---|---|---|---|---|---|---|---|
| mid | **1.5** | 2,500 | 0.006 | 2.02 | 32.8 | 2.49 | 8.81 | **11.30** | **67** |
| critical | **1.5** | 2,500 | 0.006 | 2.17 | 35.3 | 3.23 | 14.95 | **18.18** | **108** |
| mirrors-only closure (`hourly3.py`) | 1.5 | — | 0.000 | — | — | | | 10.15 / 16.95 | 60 / 100 |

**Sized honestly, the water route costs about what the mirrors cost on the power side** — 1.11×
at mid, 1.07× at critical — and it leaves 0.6 % to the grid where the mirrors leave nothing.
What it adds is the water: **1.6 to 1.8 million acre-feet a year the mirrors do not make**,
against a reservoir of 2.0 to 2.2 km³ (San Luis is 2.5). The field and the store stay at their
design size, as the author asked; the block does not, because nothing but the block serves a
July evening.

## What it does not do

It does not find the reservoir; head (500 / 300 m), the reservoir cost and the pump-turbine cost
are ASSUMED bands and say so. It does not price the modules, which are Title II's. It does not
choose between the water route and the mirrors: on the power side they are at parity, and the
choice is whether California wants the water — which is the joinder's whole question, now with
a number on it.
