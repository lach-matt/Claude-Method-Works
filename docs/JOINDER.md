# `tools/joinder.py` — Title III: can Title II return Title I's winter?

**Why it exists.** `hourly3.py` found that a sun-following plant sized on the annual energy
serves 84 % of the load: a third of December goes unserved while a quarter of June's field is
defocused, and sixteen hours of store cannot move June into December. The author (2026-09-11):
water stores across seasons and electricity does not — desalinate on the summer surplus, hold
the water, *"and the offset is returned from the desalination plants from their turbines."*
There are two turbines that sentence can mean. This file prices both, at mid and at critical,
against the winter `hourly3.py` measured, and says which one returns a winter.

**Run it.** `python3 tools/joinder.py` (it runs `hourly3.py`'s base year at both cases, about
a minute), `--selftest` for the checks. Stdlib only; imports the winter and the surplus from
`hourly3.py`, the cycle and cost lines from `cspchain.py` and `firmpower.py`, and restates none.

## The winter and the surplus, from the hour-by-hour

| | mid | critical |
|---|---|---|
| winter (Nov–Feb) unserved, TWh_e | 1.88 | 1.89 |
| summer surplus thrown away, TWh_e (defocused field at the cycle efficiency + curtailed PV) | 3.20 | 3.29 |

## A. Steam-topping turbines at the desalination plant

Title II's own architecture: solar-thermal skids, steam through a back-pressure turbine, the
exhaust heat into LT-MED. Per m³ of water the turbine must take in 105 kWh_th to leave the
70 kWh_th LT-MED needs, and returns 34.5 kWh_e (mid) — but the same heat in a condensing cycle
makes 52.2 kWh_e with no water, so **the water costs 19.3 kWh_e per m³, 6.4× reverse osmosis**
(18.0 and 5.0× at critical). The topping turbine returns electricity it was given as heat, less
what the water took. And in winter it returns only what heat is there in winter, and F-13 and
F-27 found a coastal brownfield has no heat source at a module's scale. **This turbine does not
return a winter; it makes water dear in summer.**

## B. Hydraulic turbines on the water itself

Summer surplus electricity desalinates *and* lifts the product water to an elevated off-stream
reservoir; in winter the water is delivered downhill through pump-turbines to the aqueduct and
to groundwater recharge, and the head comes back as electricity. Pumped storage whose working
fluid is the state's own water supply, on the pattern of San Luis and Gianelli, seasonal because
the reservoir is. Energy per m³ is ρ·g·H·η: at 500 m and 0.90 turbine efficiency, 1.23 kWh_e
returned per m³ against 1.51 to lift it (round trip 0.81); at critical, 300 m and 0.85, 0.69
against 0.96 (0.72).

**The requirement** — to return the whole winter — is 1.5 km³ of water at mid (25 Title II
module-years) and 2.7 at critical, needing 6.9 / 12.4 TWh_e of summer electricity to desalinate
and lift, against a surplus of 3.2 / 3.3. The surplus cannot make that much water. So the honest
figure is the other bound:

| surplus-bounded | mid | critical |
|---|---|---|
| water made and lifted, km³ (M acre-feet) | 0.71 (0.58) | 0.72 (0.59) |
| = Title II modules' annual output | 11.5 | 11.7 |
| winter returned, TWh_e | **0.87** | **0.50** |
| = share of the winter unserved | **0.46** | **0.27** |
| pump-generation plant, MW | 302 | 174 |
| reservoir + pump-generation, $B | 1.77 + 0.45 = **2.23** | 2.89 + 0.44 = **3.32** |
| + $/MWh on Title I | 13.2 | 19.7 |
| $B per TWh of winter returned | 2.56 | 6.62 |
| `hourly3` field oversizing, whole winter: $B / $B per TWh | 10.15 / 5.39 | 16.95 / 8.95 |

**Per TWh of winter returned the water is cheaper than the mirrors at both cases**, by 2.1× at
mid and 1.35× at critical, and it is bounded by the surplus: the scheme returns about half the
winter at mid and a quarter at critical, and makes 0.7 km³ of water a year as its product. The
water is not consumed by the return; it is delivered, to the aqueduct and to SGMA winter
recharge, which is where winter water goes in California anyway. What it needs is **head** and
a **reservoir where the water is wanted below it** — a siting question, and the reason San Luis
exists. The rest of the winter still needs the field, or the grid.

## C. More modules, not more storage

The author (2026-09-11): not more storage on the power side — can hydro output at the
desalination plants be raised, or should more modules make more water? Two things settle it.
Hydro output at a plant is volume × head, and a coastal plant is at sea level: **the head is
where the water comes down**, a property of the reservoir site, not of the plant. So the levers
are exactly the author's two, volume (modules) and head (site), and head is worth more: each
doubling halves the water. And if the water is on **Title II's own account** — its cost model
already carries its energy line — then Title I's surplus is spent on the *lift alone*, and the
winter closes when enough water comes down:

| | head, m | modules | M acre-feet/yr | km³ | lift, TWh_e (surplus 3.2 / 3.3) | capex, $B | + $/MWh |
|---|---|---|---|---|---|---|---|
| mid | 300 | 41.5 | 2.08 | 2.56 | 2.33 | 7.38 | 43.7 |
| mid | 500 | **24.9** | **1.25** | 1.54 | 2.33 | **4.82** | **28.6** |
| mid | 800 | 15.6 | 0.78 | 0.96 | 2.33 | 3.38 | 20.0 |
| critical | 300 | 44.2 | 2.21 | 2.73 | 2.62 | 12.54 | 74.3 |
| critical | 500 | **26.5** | **1.33** | 1.64 | 2.62 | **8.18** | **48.5** |
| critical | 800 | 16.6 | 0.83 | 1.02 | 2.62 | 5.73 | 33.9 |
| field oversizing, whole winter | | | | | | 10.15 / 16.95 | 60 / 100 |

The lift fits inside the surplus at every head at both cases; the selftest asserts it. At 500 m
the whole winter closes for **$4.8 B at mid and $8.2 B at critical**, against $10.2 / $16.9 B
for the mirrors, and it makes **1.25 to 1.33 million acre-feet a year** of water doing it — 25
to 27 modules, roughly half of Carlsbad's output each. What the modules cost is Title II's to
price (F-16 says their capex is understated three- to four-fold), and what they need is
**takers for a million acre-feet or more a year, delivered in winter** — which is what SGMA
groundwater recharge in the San Joaquin is short of by about that much.

## What it does not do

It does not find the reservoir; head (500 / 300 m) and the reservoir and pump-turbine costs are
ASSUMED bands and say so. It does not net the evening peak, which `hourly3.py` closes with the
block, not the winter. It says which turbine the author's sentence can mean and returns a winter:
the hydraulic one, at a capex per TWh under the field oversizing at both cases, conditional on
head, and bounded by the summer the plant throws away.
