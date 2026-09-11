# helios.py — Program Helios-1M at the scale proposed, hour by hour

`tools/helios.py` resolves `proposals/FLAWS.tsv` **F-01** and **F-02**: the
as-submitted Title I sells 1,515 MW × 8,760 h of export at an evening-peak
price — a 100 % capacity factor priced at a four-hour-a-day price. The
instrument takes the plant **exactly as specified** (45.6 M m² aperture,
5,250 MWe gross, 197,184 MWh_th of salt, three nodes, 735 MW parasitic), runs
it through a year one hour at a time, and prices what it made at what the
hours pay. It corrects the mathematics to the proposed scale and changes
nothing else: no larger field, no PV charging, no re-siting. Those are
redesigns and belong to later passes.

    python3 tools/helios.py
    python3 tools/helios.py --selftest

## The result

| | as written (Title I) | as modelled |
|---|---|---|
| net generation | 39.6 TWh sold (26.3 in-state + 13.3 export) | **19.2 TWh** |
| net capacity factor | 1.00 (implied) | **0.486** |
| left for export after the 3,000 MW in-state promise | 13.3 TWh | **−7.0 TWh** |
| energy in the 4 h peak window | 100 % (priced so) | **33 %** |
| December average net | — | 1,497 MW (33 % of net nameplate) |
| revenue, all energy at 2024 wholesale | $2,522–4,645 M (export only) | **$693 M** |
| revenue, $190 peak / 2024 off-peak | $2,972 M with RA | $1,439 M |
| revenue, $350 peak / 2024 off-peak | $5,125 M with RA | $2,467 M |
| carrying cost (Title I §4.1, unchanged here) | $1,933 M | $1,933 M |

**The plant as specified has no export.** After the in-state promise it is
7 TWh short, so the export line — the one that funds the program — is not
overstated, it is empty. F-01 is not a percentage; it is the sign.

**Only the $350 case clears the proposal's own carrying cost** (1.28×), and it
does so by selling every megawatt-hour, including the ones promised to
households, at 2.4× the highest monthly hour-ending-20 average of 2024. The
"conservative" $190 case reaches 0.74. At the 2024 shape the whole plant earns
0.36 of carrying cost.

**And the model still flatters the plant.** No commercial salt tower has
delivered its design output: Gemasolar 80 of 110 GWh after a decade (0.73),
Crescent Dunes 196 of 500 (0.39), Cerro Dominador 115 of 950 (0.12, hot-tank
damage), Noor III a 14-month hot-tank leak from 2024. At the best sustained
record the network makes 14.0 TWh; at Crescent Dunes' 7.5.

## What the proposal's own numbers say about each other

The instrument first checks Title I against itself, before any model:

- 197,184 MWh_th ÷ (5,250 MWe ÷ 0.43) = **16.2 h** — the 16-hour claim holds.
- 1.665 Mt of solar salt × 1.5 kJ/kg·K × 275 K = **190,781 MWh_th** — 0.968 of
  the claim, consistent.
- 45.6 M m² at 950 W/m² and design-point field efficiency delivers ~26 GW_th
  against a 12.2 GW_th turbine: **SM = 2.06, not 5.0**. SM 5 needs 111 M m².
  This is F-06's evidence, produced here for free; F-06 stays open until the
  author decides which figure to keep.

## What is sourced, what is reconstructed

No hourly irradiance or price series was reachable — NREL, CAISO and CPUC are
blocked at this environment's egress proxy. So:

- **SOURCED**: Daggett annual DNI 7.67 kWh/m²/day (NREL TMY3) for the Mojave
  node; the Westlands 5.5–6.5 kWh/m²/day band for the Central Valley node;
  CAISO 2024 hour-ending-20 day-ahead prices by month (Q1 $64, July $146,
  August $97, October $63); the WEIM 2024 average of about $40/MWh and its
  35 % fall from 2023; 1,180 negative-price hours in 2024; the Palo Verde
  2024 on-peak strip at $81.80; and the built record above.
- **RECONSTRUCTED**: the hourly *shape* of both. DNI is clear-sky from exact
  solar geometry (declination, hour angle, Kasten–Young air mass, Meinel
  attenuation), with a seasonal clearness 0.88 in December to 1.12 in June
  and every seventh day overcast at a quarter of clear-sky, then scaled
  **exactly** to the sourced annual total — so the shape cannot change the
  energy, only its timing. The price shape is pinned to the anchors above.
- **ASSUMED**: Desert Center's annual DNI (2,740 kWh/m²/yr, from the NSRDB map
  class, with a band); the field efficiency curve (0.66 at high sun falling
  as sin(h)^0.3, ~0.58 annual, inside the SolarPACES/SAM band); receiver
  0.88; availability 0.95.

The selftest asserts the distinction: re-running with no overcast days and a
flat season moves the annual energy by **under 5 %**. What the shape decides is
December and the peak-window share, and the report gives those as what they
are.

## Dispatch

Two strategies, both reported. **Max-energy** runs the turbine whenever the
store can feed it. **Peak-first** — the honest version of "evening peak
dispatch" — runs at full through 17:00–21:00 whenever the store can, and
outside the window runs only to keep the tank from spilling and to burn down
what the next window will not need. They differ by under 1 % in annual energy,
because a 16 h store rarely has to choose; they differ in *when*, and
peak-first puts 33 % of the year's energy into the 4 h window against
max-energy's ~17 %.

## What this pass does not do

It does not size the field to the promise (that is a redesign: SM 5 would
need 111 M m² and 620,000 Noor III heliostats), add electric charging from
curtailed CAISO solar, re-site the Central Valley node, price the in-state
energy as a bill credit, or correct the carrying cost (F-05, F-19). Each is a
later flaw. What it does is replace two impossible numbers with real ones:
**19.2 TWh a year at the scale proposed, worth about $0.7 B at 2024
wholesale**, against a carrying cost the proposal puts at $1.93 B.

## Selftest

Forty checks: exact solar geometry (equinox, solstice, noon elevation);
every node's series sums to its sourced annual DNI and a different cloud
pattern keeps the total; the proposal's storage-hours and salt-inventory
claims agree with each other and its solar multiple does not; the hourly
plant conserves energy to within one tank, never exceeds nameplate, and has
a capacity factor between 0.35 and 0.75; peak-first never out-produces
max-energy and never falls under 90 % of it; the network makes less than
Title I sells, by more than a third, and less than the in-state promise
alone; the price shape hits its anchors; the $190 case is under carrying
cost and only the $350 case clears it; no built plant reached design; and the
report says "has no export", names what it does not do, and carries the RA
exclusion.

## The criterion, as the author stated it

*The plant pays for itself after the build bonds.* Revenue must cover debt
service plus O&M every year of the term, at the coverage a bond buyer
requires (~1.25×); after the term, everything above O&M is the household
dividend. **The free tariff is therefore an output of the balance, not an
input to it** — the proposal put it first and the export second.

Inverted, the question is *at what realised $/MWh does 19.2 TWh pay for
itself?*

| case | capex $B | rate | carrying $M | $/MWh at 1.00× | at 1.25× |
|---|---|---|---|---|---|
| Title I as written | 27.2 | 3.85 % | 1,954 | **101.6** | 127.0 |
| F-05 low capex | 42.0 | 3.85 % | 2,795 | 145.3 | 181.6 |
| F-05 high capex | 63.0 | 3.85 % | 3,987 | 207.2 | 259.0 |
| F-05 low, F-19 low rate | 42.0 | 5.50 % | 3,300 | 171.5 | 214.4 |
| F-05 high, F-19 high rate | 63.0 | 7.00 % | 5,487 | 285.2 | 356.5 |

California's load-serving entities pay **$80–120/MWh** for firm clean energy
under long-term contract; 2024 wholesale paid this plant $35.

**At Title I's own capex the plant needs $102/MWh — inside the band the
state already pays.** At the proposed scale and cost, self-funding is a
contract question, not an export gamble: a 30-year firm-energy agreement
with California's own LSEs, which a state authority can write, closes it
where WEIM cannot. **At F-05 and F-19's realistic cost it needs $285/MWh,
which nothing pays.** The criterion does not fail on the physics or on the
market; it turns on the capital cost, and F-05 is the flaw that decides
whether the program exists.

## F-17: the size is a requirement, not a lever

The author restated the requirement: **3 million households is a minimum and
must grow with population; one facility or a hundred, the equipment is the
same.** So the plant is sized by the requirement, and the requirement has to
be stated at California's actual consumption rather than the three figures
Title I implies (12,000 kWh/yr in the bill example, 8,760 implied by 3,000 MW
at 100 % CF, and the truth):

| | kWh/yr per household | 3 M households | plant as specified |
|---|---|---|---|
| EIA 2024, California actual (SOURCED, 503 kWh/month) | 6,036 | **18.1 TWh** | **19.2 TWh → 3.19 M households, zero export** |
| growth 1 %/yr over the 30-year term | | 24.4 TWh | 1.27× the plant |
| growth 2 %/yr | | 32.8 TWh | 1.70× the plant |

**The plant as specified serves the minimum today with nothing to spare.** The
size was never wrong; the export promised on top of it was. And because the
three largest cost lines scale with the plant, growing it does not change the
price per MWh — which is why the size cannot be the lever.

What a household would actually pay for generation, at the required price:

| case | $/MWh | $/household/yr | vs today |
|---|---|---|---|
| today, IOU generation charge (Title I's own $0.195/kWh) | 195 | 1,177 | — |
| Title I as written ($27.2 B) | 102 | 613 | −48 % |
| heliocost.py low | 171 | 1,033 | −12 % |
| heliocost.py mid | 206 | 1,244 | **+6 %** |
| heliocost.py high | 253 | 1,528 | +30 % |

**At the built cost, the sovereign plant charges a household more for
generation than the IOU does today.** No size answers that. Only the
equipment does — what makes a firm megawatt-hour, and what that equipment
costs per megawatt-hour it makes — and that is the second pass's first
question. The built prices are computed by importing `heliocost.py`, not
quoted, and the selftest asserts it.
