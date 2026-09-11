# Title I — Helios-3, re-based (v0.2)

**What this document is.** Title I of the California Sovereign Infrastructure program as it
stands after the second pass: the Helios-1M salt towers of v0.1 replaced by Helios-3 (Gen3
particles, sCO₂, PV-direct daytime, night-sized field), the author's mitigation register adopted
row by row, and the plant run hour by hour. It is **rendered by `tools/rebase.py` from the
instruments** and carries no number they did not compute; every number is labelled **mid** or
**critical**, under the author's standing rule that a number quoted without its case is misquoted.
v0.1 is the as-submitted merge and is unchanged; this is the diff, stated as a document.

## 1. The requirement

Three million households at EIA's 6,036 kWh a year is **18.1 TWh** of firm supply, the
program's minimum, growing to 1.35–1.81× over the 30-year bond term. The criterion is the
author's: the plant pays for itself after the build bonds. Inverted, that is a required price per
MWh, set beside the $80–120 California's load-serving entities pay for firm clean
energy under contract, and beside what a household pays the utility today for generation: **$1,177 a
year**.

## 2. The plant

Helios-3: a Noor III-class surround heliostat field sized for the night; a multi-aperture
falling-particle receiver behind the author's compound quartz aperture; sintered-bauxite particles
as medium and store in cold-shell silos; a moving packed-bed exchanger into a 715 °C sCO₂
recompression block, dry-cooled; PV serving the daytime load directly and feeding particle heaters
in winter. The energy chain, link by link:

| link | mid | critical |
|---|---|---|
| field optical efficiency, annual | 0.640 | 0.580 |
| receiver thermal efficiency | 0.900 | 0.690 |
| power cycle, gross | 0.500 | 0.450 |
| 1 − parasitic share | 0.920 | 0.900 |
| availability | 0.960 | 0.920 |

The critical receiver figure is `receiver.py`'s, handed up the chain rather than the chain's own
best: 0.690 open, which alone grows the field by 1.30. Sized to the requirement:

| | mid | critical |
|---|---|---|
| mirror aperture, M m² | 18.1 | 30.9 |
| towers, Noor III class | 14 | 24 |
| sCO₂ block, MWe | 2,620 | 2,620 |
| particle store, GWh_th (16 h) | 83.8 | 93.2 |
| PV, MW_AC | 2,894 | 3,101 |
| electric heaters, MW_th | 3,493 | 3,882 |

## 3. What it serves, hour by hour

The chain sizes the plant on annual energy. Run through 8,760 hours across the three nodes,
PV serving the load first, the block serving the residual from the store, the plant as sized
serves:

| | mid | critical |
|---|---|---|
| share of the load served | 0.839 | 0.835 |
| unserved, TWh | 2.92 | 2.99 |
| unserved in July, share of month | 0.053 | 0.058 |
| unserved in December, share of month | 0.357 | 0.358 |
| field defocused in summer, TWh_th | 5.99 | 6.86 |

Two shortfalls the annual chain could not see. The block is sized to the average night and a
residential load peaks after sunset, so the block cannot carry the evening in any month. And
sixteen hours of store cannot move June into December: the store empties from October to April
while a quarter of June's field is defocused. The load and PV shapes are reconstructed and pinned
to sourced levels; a measured CAISO profile and an NSRDB hourly file replace them when reachable.

## 4. Closing the load: two routes

Both keep the block at **×1.5**, because nothing but the block serves a July evening. They differ
in how the October-to-April season is closed.

| route | what grows | mid, $B | + $/MWh | critical, $B | + $/MWh | leaves to the grid |
|---|---|---|---|---|---|---|
| mirrors | field ×2, store 2 days | 10.2 | 60 | 16.9 | 100 | 0.0% / 0.0% |
| water (Title III) | 33 / 35 desalination modules, a 2.0 / 2.2 km³ reservoir at 500 m, 2,500 MW of pump-turbines | 11.3 | 67 | 18.2 | 108 | 0.6% / 0.6% |

On the power side the two are at parity. The water route makes **1.64 to 1.76 million
acre-feet a year** of water the mirrors do not, delivered October to April; at critical the summer
surplus lifts 0.95 of the season and the rest is the plant's own output. Which route is a decision about
water, and it is Title III's.

## 5. Price and the household

| $/MWh | mid | critical |
|---|---|---|
| Helios-3 as chained | 117 | 187 |
| with the mitigation register (§6) | 125 | 202 |
| serving the whole load, mirrors route | 185 | 302 |
| serving the whole load, water route | 192 | 310 |

| $ per household per year (today 1,177) | mid | critical |
|---|---|---|
| with the mitigation register | 756 | 1,218 |
| serving the whole load, mirrors route | 1,119 | 1,824 |
| serving the whole load, water route | 1,161 | 1,868 |

**The criterion, stated exactly.** At mid, Helios-3 with its register needs $125/MWh, $5
above the top of the contract band, and a household pays $756 against $1,177 today. Serving
the whole load from the plant alone costs $185, at which a household pays about what it pays now. At
critical the register price is $202 and the whole load $302: **above today's bill**. The plant pays
for itself after the bonds only at a price above the band, and the critical case is the threshold
the design is held to. A plant designed to mid has no margin; this document does not offer one.

## 6. The risks and their mitigation

Sixteen rows, graded before and after, each carried by a named part of the build, each DESIGN
(retired by specification), HOURS (retired only by operating time) or BENEFIT. Adopted row by
row with the author on 2026-09-11.

| id | risk | before | after | kind |
|---|---|---|---|---|
| R-01 | Particle attrition: grains break, make dust, and the medium is lost | MODERATE | NEGLIGIBLE | DESIGN |
| R-02 | Receiver wind and convective loss: a falling curtain is open to the air | MAJOR | MODERATE | HOURS |
| R-03 | Particle-to-sCO2 heat exchanger: 800 C particles against 250 bar CO2 | MAJOR | MODERATE | HOURS |
| R-04 | sCO2 turbomachinery at 715 C and 250 bar | MAJOR | MODERATE | HOURS |
| R-05 | CO2 inventory release: heavier than air, 4 % is IDLH, cold on release | MODERATE | MINOR | DESIGN |
| R-06 | High-pressure, high-temperature containment (250 bar / 715 C) | MODERATE | MINOR | DESIGN |
| R-07 | Silo heat loss and thermal ratcheting at 800 C over forty years | MODERATE | MINOR | DESIGN |
| R-08 | Particle chemistry: bauxite oxides transform in air at 700-1000 C | MODERATE | MODERATE | HOURS |
| R-09 | Particle lift: erosion and temperature on the elevator | MODERATE | MINOR | DESIGN |
| R-10 | Dust as PM10 in non-attainment counties | MODERATE | MINOR | DESIGN |
| R-11 | Receiver scale: no particle receiver has run above ~2.5 MW_t | DOMINANT | MAJOR | HOURS |
| R-12 | Provenance: no plant of this kind exists at any commercial scale | DOMINANT | MAJOR | HOURS |
| R-13 | No freezing point: no heat tracing, no drain-down, no hot-tank failure | BENEFIT | BENEFIT | BENEFIT |
| R-14 | No decomposition ceiling: stable past 1000 C | BENEFIT | BENEFIT | BENEFIT |
| R-15 | No oxidiser and no toxic medium: the author's hazard rule, met cleanly | BENEFIT | BENEFIT | BENEFIT |
| R-16 | Dry cooling at a sixth of the airflow | BENEFIT | BENEFIT | BENEFIT |

After: 4 BENEFIT, 1 NEGLIGIBLE, 5 MINOR, 4 MODERATE, 2 MAJOR. R-08 is managed without moving and says so.

## 7. Provenance, the ladder and the cost of delay

`studies.py` lists 49 studies over the 12 technologies in the system, each with a status and a
source, complete over technologies and a floor over studies, reviewed against the web where the
proxy reached. No falling-particle receiver has run above 2 MW_th and no 715 °C sCO₂ recompression
cycle has run at all; those are HOURS, and the ladder buys them in order:

- G3P3-USA 2 MW_th falling receiver (has run): 2 MW_th
- pilot aperture, 30 MW_th (proposed): 30 MW_th (×15.0)
- first module, 100 MWe: 434 MW_th (×14.5)
- fleet tower: 794 MW_th (×1.8)

Each rung is passed at its critical figure and handed up the chain before the next is ordered.
The studies on the critical path take 7.5 years, run against the build rather than before
it. Delay escalates the whole plant at 3 % a year before a dollar is spent:

| per year of delay | mid | critical |
|---|---|---|
| capex, $B | 0.97 | 1.64 |
| price, $/MWh | 3.8 | 6.1 |
| household, $/yr | 23 | 37 |

## 8. What v0.2 does not settle

- The route for the season — mirrors or water — is Title III's decision, and the water side has
  its own flaw register to survive (F-16 on module capital, F-14 on the price of water).
- The evening peak is closed by a block ×1.5 and by nothing else; a measured load profile may
  move that factor either way.
- The receiver's critical figure and the dome's verdict are what the pilot aperture measures;
  until it has run, the critical column is the design basis.
- Transmission, the tariff, the bond rate and the schedule (F-09, F-10, F-19, F-24) are open in
  `FLAWS.tsv` and are not changed by anything above.

*Rendered by `tools/rebase.py`; do not edit by hand. Re-render after any change to the instruments.*
