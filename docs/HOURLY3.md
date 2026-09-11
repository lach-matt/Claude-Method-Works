# `tools/hourly3.py` — Helios-3 hour by hour, at mid and at critical

**Why it exists.** `cspchain.py` sized Helios-3 on three static assumptions — a direct-PV share of
0.35 of the annual energy, winter heaters at 0.25 of the night block's thermal input, and a
dispatch link near unity — and named running the plant hour by hour as its next step.
`studies.py` put that study first, because it is the one only this repository can run. This is
it, and it runs under the author's standing rule: every result at mid and at critical, the
design held to critical.

**Run it.** `python3 tools/hourly3.py` (about five minutes; the closure scan is 288 plant-years
per case), `--no-close` for the base run only, `--selftest` for the checks. Stdlib only; imports
the design from `cspchain.py`, the solar geometry and DNI series from `helios.py`, and the cost
bands from `firmpower.py`, and restates none of them.

## What it does

One year at one hour per step across the three nodes. PV serves the load first; PV surplus
charges the store through the heaters; the field charges the store; the sCO₂ block serves the
residual load from the store, net of its own parasitics, within its minimum load; what nothing
serves is **unserved** and is counted by month. Two shapes are RECONSTRUCTED and say so — the
hourly load (California residential: evening peak at 19:00, summer amplification, pinned exactly
to the annual energy so the shape cannot change the energy, only its timing) and the PV output
(a single-axis tracker following the same DNI series `helios.py` reconstructs, pinned exactly to
the case's sourced capacity factor). The optical curve is `helios.py`'s shape pinned to the
case's annual link. The selftest asserts each pin exactly and that the store's energy balance
closes over the year.

## What it found

**As sized, the plant serves 84 % of the load** — 2.9 TWh unserved at mid, 3.0 at critical —
and the static shares were not the problem. The direct-PV share comes out at 0.346 against the
assumed 0.35 and the heater peaks at exactly its sizing. Two things the static chain could not
see are:

| | mid | critical |
|---|---|---|
| served, share of load | 0.839 | 0.835 |
| unserved, TWh | 2.92 | 2.99 |
| unserved in July / December, share of month | 0.053 / 0.357 | 0.058 / 0.358 |
| field spilled (defocus), TWh_th | 5.99 of 24.98 | 6.86 of 28.37 |
| dispatch link (static ~0.996) | 0.800 | 0.793 |
| hours the store is empty / full | 1,209 / 589 | 1,189 / 592 |

1. **The evening peak.** The block is sized to the average night × 1.3 (`NIGHT_PEAK`, ASSUMED).
   A residential load peaks at about 1.7× its mean, at 19:00, after the sun has set, and the
   block cannot carry it in any month — unserved is 5 % even in July.
2. **The winter.** The night block is sized for the *average* night; December has the longest
   nights and the least sun, so the store empties and a third of December's load goes
   unserved, while in June the store fills by early afternoon and a quarter of the field's
   energy is defocused. Sixteen hours of storage cannot move June into December. That is F-06,
   quantified.

**What closes it.** A scan over block size (with its 16 h store), store days, field size, PV
overbuild and heater size, priced on `cspchain.py`'s own lines through its overheads and
`firmpower.py`'s financing, cheapest point at each target:

| | block × | store, days | field × | PV × | heater × | extra direct, $M | + $/MWh | unserved |
|---|---|---|---|---|---|---|---|---|
| mid | 1.5 | 2 | 2.0 | 1.0 | 1.0 | 10,153 | **+60** | 0.0000 |
| critical | 1.5 | 2 | 2.0 | 1.0 | 1.0 | 16,947 | **+100** | 0.0002 |

The block closes the evening; the field and a second day of store close the winter. **The
heater and the PV overbuild were never the lever**: the scan never chose more of either,
because December's PV is as short as December's sun. Stated on top of `helios3.py`'s mitigated
price, Helios-3 serving its whole load hour by hour is about **$185/MWh at mid and $302 at
critical** ($1,117 and $1,822 per household against $1,177 today). The scan is coarse (steps
of 0.5 on the block and field); a finer one would shave the figure and not change its kind.

## What it does not do

The load and PV shapes are reconstructed; a measured CAISO residential profile and an NSRDB
hourly file replace them when this environment can reach one, and `studies.py` names that as
the next step of this study. `cspchain.py` is not changed here — it is told what its static
shares are worth hour by hour, and re-basing Title I on the closed sizing is a decision for the
author, priced above. The seasonal alternative the scan does not price — serving December from
something other than December's sun — is the question `firmpower.py`'s geothermal row and the
grid already pose.
