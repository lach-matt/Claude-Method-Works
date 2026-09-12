# California Sovereign Infrastructure — the complete proposal (v0.2)

*Rendered 2026-09-12 by `tools/proposal.py` from the instruments in `tools/`. Do not edit by hand; re-render after any change to an instrument.*

**What this document is.** The whole of the California Sovereign Infrastructure program as it stands
after the second pass, in one document: Title I, the electricity (Helios-3); Title II, the water
(Aqua-Sovereign); Title III, the joinder; every location addressed term by term; every study that covers
a technology in the system, cited; every one of the forty flaws found in the as-submitted proposal, with
its resolution; the figures drawn from the instruments' own outputs. It carries **no number an instrument
did not compute**, and every number is labelled **mid** or **critical** under the author's standing rule
that a number quoted without its case is misquoted. Mid is the middle of each constant's band; critical is
the adverse end of every band at once, and the design is held to critical. The nominal column is margin.

**How to read a status.** SOURCED is a published figure with its source named. ASSUMED is a band the
record does not fix, stated as such. RECONSTRUCTED is a shape or split rebuilt from physics or from a
published model because the source is unreachable here. DERIVED is computed from the others. DECIDED is
a choice the author made and recorded. A status is never flattened: how a number was got is part of what it is.

**Contents.** A. Summary · B. The requirement · C. What was submitted and why it failed · D. The equipment
question · E. The energy chain · F. The plant · G. Hour by hour · H. Closing the load · I. The risk register ·
J. Provenance: the studies · K. The pilot aperture · L. Studies and surveys first · M. Price, household and
financing · N. Title II, the water · O. Title III, the joinder · P. The sites · Q. Environment, employment and
procurement · R. What is not settled · S. The flaws register · T. Sources · U. The instruments.

## A. Summary

One state-owned program under one Authority, two severable projects, funded once by bonds and never again
by the treasury. Title I builds Helios-3, concentrating solar on three desert nodes with falling-particle
receivers and supercritical-CO₂ turbines, photovoltaics serving the day directly and a night-sized mirror
field, to make **18.1 TWh** of firm electricity a year for three million households. Title II builds
**15 to 17** seawater reverse-osmosis modules of 50,000 acre-feet a year on retired coastal power plants,
lifting their product to an elevated reservoir with Title I's summer surplus and returning it year-round
through pump-turbines to Title I's evenings. Title III is the contract, the shared asset and the
severability that join them.

| | mid | critical |
|---|---|---|
| Title I plant with its register, $B | 32.7 | 55.4 |
| Title I closing the whole load on the adopted route, $B | 6.4 | 10.3 |
| Title II modules at the adopted route, $B | 28 | 48 |
| **program, $B** | **67** | **114** |
| of which studies and surveys, first in the capital, $M | 213 | 463 |
| Title I price serving the whole load, $/MWh | 172 | 279 |
| household generation charge during the bonds, $/yr (today 1,177) | 1,036 | 1,682 |
| household generation charge after the bonds retire, $/yr | 190 | 263 |
| water at cost recovery, $/acre-foot | 3,044 | 4,830 |
| share of the load left to the grid | 0.6% | 0.7% |
| studies begin / first electricity (PV) / first CSP module / fleet complete | 2027 / 2031 / 2036 / 2041 | 2027 / 2033 / 2038 / 2043 |
| CO₂ avoided with the load closed, million t/yr | 7.24 | 6.34 |
| permanent jobs, Title I / construction peak | 1,901 / 21,054 | 1,214 / 21,054 |

**The decision the document asks for.** Fund the studies and surveys now, at
$213 to 463 million, and know within 2 to 4 years whether the rest is worth
$67 to 114 billion. Nothing irreversible is bought before the pilot receiver has passed its test.

![Figure 1](figures/fig-10-capital.png)

*Figure 1. The program's capital at the adopted route, both cases, from Title III's single financial statement.*

## B. The requirement

**Households (F-17).** Three million households is the program's **minimum**, growing with population (the author,
2026-09-11). At EIA's California average of 6,036 kWh a year (503 kWh a month, 2024) that is **18.1 TWh** of firm
supply, growing to **1.35–1.81×** over the 30-year bond term at 1–2 % a year of residential
growth including electrification. v0.1's bill example used 12,000 kWh a year, twice the state average; California has
14,217,180 residential customers, so three million is a fifth of them.

**The criterion, as the author stated it.** *The plant pays for itself after the build bonds.* Revenue must cover
debt service plus O&M every year of the 30-year term, with the coverage a bond buyer requires; after the term,
everything above O&M is the household's dividend. So the free tariff v0.1 promised is an **output** of the balance,
not an input to it. Inverted, the criterion is a required price per MWh, set beside two references:

| reference | $/MWh | $ per household per year |
|---|---|---|
| what a household pays the utility for generation today (Title I §5's own IOU charge, 0.195 $/kWh) | 195 | 1,177 |
| what California's load-serving entities pay for firm clean energy under contract | 80–120 | 483–724 |

**Size is not a lever.** Because the households are a requirement, the plant cannot be shrunk to make the price
close; only the equipment and the ownership form move the price. v0.1's plant as specified makes 19.2 TWh net,
which serves 3.19 million households at the state average: the size was right and the export was wrong (§C).

## C. What was submitted, and why it failed

`California_Sovereign_Infrastructure_v0.1.md` is the as-submitted merge of the author's two documents with no figure
altered, so every repair is a diff against it. What it proposed:

- **Title I, Program Helios-1M.** 5,250 MWe gross of nitrate-salt tower CSP across three desert nodes, 45.6 million m²
  of heliostats, 197 GWh_th of salt storage (1.67 million tonnes of salt), a claimed solar multiple of 5.0,
  3,000 MW promised in-state and 1,515 MW exported at 13.27 TWh a year, sold at
  $190–350/MWh; capital $27.2 B at a 3.85 % bond rate, $410 M a year of O&M, a carrying
  cost of $1,933 M a year; a $0.00/kWh household tariff.
- **Title II, Aqua-Sovereign.** 50,000 acre-foot-a-year desalination modules on coastal brownfields by low-temperature
  multi-effect distillation with zero liquid discharge, minerals (lithium, magnesium) sold to offset the cost, water at
  $400 an acre-foot, $250–320 M a module, first water in 24 months.
- **Title III.** Reserved and never written.

**What the plant as specified actually makes (`helios.py`, F-01, F-02).** Run hour by hour on exact solar geometry at
each node's sourced annual DNI, with the salt tank, the turbine's part-load curve and the parasitics as Title I states them:

| | figure |
|---|---|
| net output, TWh/yr | 19.2 |
| net capacity factor | 0.486 |
| v0.1 sold, TWh/yr (in-state promise plus export at 100 % capacity factor) | 39.6 |
| shortfall against the in-state promise alone, TWh/yr | 7.0 |
| revenue selling everything at the 2024 CAISO shape, $M/yr | 677 |
| revenue with v0.1's $350/MWh on the four peak hours of every day, the rest at the 2024 shape, $M/yr | 2,451 |
| carrying cost, debt service at Title I's own rate and term plus its O&M, $M/yr (Title I stated 1,933) | 1,954 |
| required price at Title I's own $27.2 B, $/MWh | 102 |

The export that funds the program is not overstated; it is **negative**: after the in-state promise the plant is short.
Evening-peak pricing exists for about 1,500–2,000 hours a year, and 1,180 hours in 2024 cleared negative. At
Title I's own capital the required price is $102/MWh, inside the contract band, so at the stated cost self-funding
is a contract question. The stated cost is the question F-05 asks.

**What it would cost to build (`heliocost.py`, F-05).** Line by line at the class the author decided (Noor III-class
heliostats of 178 m² on 36 towers of 250 m), state-owned, groundbreaking 2028–2030: no developer margin,
bond-rate interest during construction, the federal storage credit with the public direct-pay and energy-community bonuses,
CalPERS on-cost, property tax out and a payment in lieu in. The level is calibrated to NREL ATB 2024's $7,912/kWe and
the split is RECONSTRUCTED from SAM / Turchi 2019, because NREL is unreachable from this environment.

| case | net capital, $B | $/W gross | required price, $/MWh | $ per household |
|---|---|---|---|---|
| low | 46.1 | 8.79 | 171 | 1,033 |
| mid | 57.0 | 10.85 | 206 | 1,244 |
| high | 71.5 | 13.62 | 253 | 1,528 |
| Title I as written | 27.2 | 5.18 | 102 | 613 |

Title I's $27.2 B is 1.70× below the low case. **The criterion does not close at the scale proposed in any case.** The built record:

| plant | $/W gross as built | year | storage, h |
|---|---|---|---|
| Gemasolar | 11.17 | 2011 | 15.0 |
| Ivanpah | 5.61 | 2014 | 0.0 |
| Crescent Dunes | 8.86 | 2015 | 10.0 |
| Noor II+III (blended) | 6.92 | 2018 | 7.5 |
| Cerro Dominador | 10.45 | 2021 | 17.5 |
| DEWA Noor Energy 1 (blended, incl. PV) | 4.77 | 2023 | 15.0 |

And what those plants delivered against their design, the fidelity band `helios.py` carries:

| plant | delivered / designed | the year, and why |
|---|---|---|
| Gemasolar, Spain, 2011 | 0.73 | mature; the best sustained record of any salt tower |
| Crescent Dunes, USA, 2015 | 0.39 | 2018, best full year before the 2019 shutdown |
| Cerro Dominador, Chile, 2021 | 0.12 | 2023; hot-tank damage, plant largely stopped |

No commercial salt tower has delivered its design output, and the hourly model still flatters that record. That is
why the critical column exists.

![Figure 2](figures/fig-01-built-record.png)

*Figure 2. Salt-tower CSP as built against Title I's own capital, in $ per watt gross (heliocost.py).*

## D. The equipment question

Every candidate that can make a firm MWh in California, sized to the same 18.1 TWh, state-owned, one criterion
(`firmpower.py`). Salt-tower CSP is priced from `heliocost.py`, never restated; the built-up candidates from their parts. The
instrument's bands are low / mid / high, so its high column stands where critical stands elsewhere.

| candidate | MW | mid: net capital $B / price $/MWh / $ per household | band top: net capital $B / price $/MWh | acres | legal status |
|---|---|---|---|---|---|
| Salton Sea geothermal, flash (conventional) | 2,297 | 11.9 / 62 / 375 | 14.3 / 70 | 4,594 | permitted class; CEQA + Imperial County; FAST-41 covered (capped: exceeds the developable resource) |
| Enhanced geothermal (Fervo class) | 2,297 | 11.1 / 57 / 343 | 14.3 / 68 | 3,445 | permitted class; SCE holds 320 MW / 15 yr, Google 396 MW |
| PV-charged nitrate salt (heaters into Helios tanks + turbines) | 13,040 | 49.9 / 193 / 1,168 | 55.2 / 210 | 78,240 | permitted class; PV on disturbed land; salt block as heliocost |
| Salt-tower CSP as proposed (heliocost mid) | 4,941 | 53.6 / 205 / 1,239 | mid only: heliocost's mid case, scaled | 212,453 | permitted class; F-09, F-21, F-25 open |
| PV + 100-hour iron-air storage | 13,609 | 52.8 / 199 / 1,203 | 56.3 / 209 | 81,651 | permitted class; first 15 MW units 2026 |
| Small modular reactor | 2,247 | 24.5 / 102 / 617 | 29.3 / 119 | 1,123 | BARRED: Cal. Pub. Res. Code §25524.2 moratorium on new nuclear |
| Floating offshore wind (Morro Bay / Humboldt) | — | — | — | — | two of three Morro Bay leases terminated; not firm; SOURCED LCOE+LCOT $95-121 (2035) |

Salton Sea geothermal, in the proposal's own Imperial node, has 2,250 MW developable, 0.98 of the requirement,
and prices at $62/MWh at mid; the small modular reactor is barred by Public Resources Code §25524.2. The
hypersaline capital band is ASSUMED and the file says so. **The instrument does not choose. The author chose CSP** —
*"learn enough about how it works to do it better: scale down in size while increasing output"* — and §E is that.

![Figure 3](figures/fig-02-candidates.png)

*Figure 3. Every firm candidate sized to the requirement, state-owned, required price at mid and critical (firmpower.py).*

## E. The energy chain

Sun to socket is a product of seven links, `E = A · DNI · opt · rec · tes · dispatch · cycle · (1 − par) · avail`, each
carried by Helios as proposed, each at the best achieved or designed, each at its physical bound (`cspchain.py`):

| link | Helios as proposed | best achieved / designed | bound | status of the best |
|---|---|---|---|---|
| field optical efficiency, annual | 0.536 | 0.640 | 0.700 | SOURCED: optimised surround fields 58-64 %; mono-tower upper limit ~70 % |
| receiver thermal efficiency, annual | 0.880 | 0.900 | 0.950 | SOURCED: 84.7 % annual / 87.4 % design at 336-650 C salt; particle 85-90 % |
| storage round trip | 0.995 | — | 1.000 | SOURCED: ~1 C/day on a 275 K span; no gain claimed |
| dispatch: spill, start-up, part load | 0.996 | — | 1.000 | DERIVED from helios.py's hourly run: SM 2.1 rarely fills the tank, so it barely spills; no gain claimed -- the loss is winter under-supply, F-06 |
| power cycle, gross | 0.430 | 0.500 | — | SOURCED: subcritical reheat steam 41-44 %; sCO2 RCBC ~50 % at 700-715 C (STEP) |
| 1 - parasitic share | 0.880 | 0.920 | 0.970 | SOURCED: sCO2 needs ~1/6 the cooling airflow of steam; ACC fans dominate |
| availability | 0.950 | 0.960 | 1.000 | SOURCED band: soiling, tracking, outage |

Helios's product is **0.168** sun to socket; the best chain is **0.252**, ×1.50. The three links that move are
the cycle (0.43 steam at 565 °C against 0.50 sCO₂ at 715 °C), the optics (0.536 against Noor III-class
0.64), and the one thing no link fixes: **a thermal plant serves daytime load at 43% where a panel serves it at
100 %.** So the daytime third never touches the mirrors, and the field is sized for the night. Two plants on that architecture:

| | Helios as proposed, scaled to 18.1 TWh | Helios-2 (nitrate salt, steam) | Helios-3 (particles, sCO₂), mid |
|---|---|---|---|
| mirror aperture, M m² | 42.9 | 22.5 | 18.1 |
| towers, Noor III class | 34 | 18 | 14 |
| thermal block, MWe | 4,941 | 2,620 | 2,620 |
| PV, MW_AC | — | 2,894 | 2,894 |
| price, $/MWh | 205 | 141 | 117 |
| $ per household per year (today 1,177) | 1,239 | 849 | 706 |
| status | built class | BUILT: Noor Energy 1 (700 MW CSP + 250 MW PV); Midelt adds PV-fed heaters | PILOT: G3P3 >1 MW_t at Sandia; STEP 10 MWe sCO2 at 715 C -- not a 2030 plant |

Helios-2 is **1.9× smaller in mirror** for the same energy, every part of it built (DEWA Phase IV, Midelt's design).
Helios-3 is a pilot (G3P3, STEP), priced and not offered as a 2030 plant. **The author chose Helios-3** and claimed each
cost could be mitigated upfront; §I tests that claim row by row.

![Figure 4](figures/fig-03-chain.png)

*Figure 4. The chain, link by link: Helios as proposed, Helios-3 at mid, Helios-3 at critical.*

## F. The plant: Helios-3

A Noor III-class surround heliostat field sized for the night; a multi-aperture falling-particle receiver behind the
author's compound quartz aperture (a hexagonal low-OH rod-lens dome on a cooled lattice frame); sintered-bauxite
particles as medium and store, in cold-shell refractory-lined silos with replaceable liners, not buried; a moving
packed-bed particle-to-sCO₂ exchanger into a 715 °C, 250 bar sCO₂ recompression Brayton block, dry-cooled at 45 °C
ambient, CO₂ kept as the fluid; Inconel 740H pressure parts with Haynes 282 and Inconel 617 on the alloy ladder; PV
serving the daytime load directly and feeding electric particle heaters in winter; one cold-side particle lift per
aperture, gravity everywhere else. The cycle is sCO₂ recompression Brayton, 715 °C at 0.50 gross; the nitrate-salt
fallback on the same field is subcritical reheat steam at ~540 °C live steam from 565 °C salt at 0.43 (F-32: v0.1's *supercritical Rankine* is withdrawn).

**The chain at both cases.** The critical receiver figure is `receiver.py`'s, handed up the chain rather than the
chain's own best (the standing rule: a downstream instrument hands its critical figure to the one above it):

| link | mid | critical |
|---|---|---|
| field optical efficiency, annual | 0.640 | 0.580 |
| receiver thermal efficiency | 0.900 | 0.690 |
| storage round trip | 0.995 | 0.995 |
| dispatch | 0.996 | 0.996 |
| power cycle, gross | 0.500 | 0.450 |
| 1 − parasitic share | 0.920 | 0.900 |
| availability | 0.960 | 0.920 |
| **sun to socket** | **0.252** | **0.148** |

**Sized to the requirement:**

| | mid | critical |
|---|---|---|
| mirror aperture, M m² | 18.1 | 30.9 |
| towers, Noor III class | 14 | 24 |
| sCO₂ block, MWe | 2,620 | 2,620 |
| particle store, GWh_th (16 h) | 83.8 | 93.2 |
| PV, MW_AC | 2,894 | 3,101 |
| electric heaters, MW_th | 3,493 | 3,882 |
| energy served by PV directly / by the block, TWh | 6.3 / 11.8 | 6.3 / 11.8 |
| land at design sizing, acres | 39,762 | 56,792 |
| **on the adopted route (§H)**: mirror aperture, M m² | 22.7 | 38.6 |
| on the adopted route: towers | 18 | 31 |
| on the adopted route: sCO₂ block, MWe | 3,930 | 3,930 |
| on the adopted route: land, acres | 45,361 | 66,339 |

**Direct cost by line, $M, before contingency, EPC, tax, escalation and interest** (`cspchain.py`, the same rates
as `heliocost.py` where the part is the same, particle and sCO₂ lines from the Gen3 and STEP record):

| line | mid | critical |
|---|---|---|
| site improvements | 373 | 636 |
| heliostat field | 2,330 | 4,768 |
| towers | 931 | 1,587 |
| receivers | 2,140 | 3,648 |
| thermal storage (particles) | 1,258 | 2,049 |
| power block (sCO2) | 2,751 | 3,275 |
| balance of plant | 977 | 1,145 |
| PV, direct + winter | 4,659 | 5,891 |
| electric heaters | 210 | 388 |
| 500 kV switchyards + gen-tie | 771 | 1,157 |
| **direct total** | **16,399** | **24,544** |

**The receiver (`receiver.py`, R-11).** A falling curtain is a per-metre machine: its power goes with its width, so
scale is bought in width and aperture count, the loss fraction at fixed flux does not change with size, and the edge
losses shrink as perimeter over area. Run under the standing rule with every banded constant at nominal and at
critical (the critical flux halved to 0.5 MW/m² after the 2026-09-11 review of the record, below the 0.3–0.7 Sandia
measured its curtain at):

| | nominal (mid) | critical |
|---|---|---|
| open-aperture thermal efficiency | 0.882 | 0.690 |
| with the compound quartz dome (R-02) | 0.835 | 0.592 |
| field factor handed upstream, against the chain's own receiver link | 1.02 | 1.30 |

The dome loses on the model and pays on the measured record, and both are printed. The critical open receiver, **0.690**
against the chain's 0.90, grows the field by **1.30** and is what the critical column above carries. The ladder of
scale, from what has run to a fleet tower:

| rung | MW_th | step |
|---|---|---|
| G3P3-USA 2 MW_th falling receiver (has run) | 2 | — |
| pilot aperture, 30 MW_th (proposed) | 30 | ×15.0 |
| first module, 100 MWe | 434 | ×14.5 |
| fleet tower | 794 | ×1.8 |

The first 100 MWe module is already 0.55 of a fleet tower's duty, so a pilot aperture at ~30 MW_th belongs before it (§K).

## G. Hour by hour

The chain sizes the plant on annual energy. `hourly3.py` runs it through 8,760 hours across the three nodes, PV
serving the load first, the block serving the residual from the store, the heaters charging the store from
surplus PV. The load shape is RECONSTRUCTED (residential, evening-peaked, summer-peaked; its seasonal sign was
found inverted and corrected on 2026-09-11, `docs/LOADSHAPE.md`) and pinned to the sourced annual; `profiles.py` is
the ingestion path for a measured CAISO profile and NSRDB hourly DNI, which replace it when reachable.

| | mid | critical |
|---|---|---|
| share of the load served, as sized | 0.874 | 0.869 |
| unserved, TWh | 2.27 | 2.37 |
| hours with any shortfall | 2,309 | 2,348 |
| field defocused in summer, TWh_th | 4.82 | 5.59 |
| PV curtailed beyond the heaters, TWh | 0.06 | 0.06 |
| hours the store is full / empty | 395 / 902 | 400 / 914 |

**By month, mid** (TWh; the critical column of the last row beside it):

| month | load | PV direct | block net | heaters (PV in) | unserved | share unserved, mid / critical |
|---|---|---|---|---|---|---|
| Jan | 1.31 | 0.39 | 0.78 | 0.14 | 0.15 | 11.3% / 11.8% |
| Feb | 1.20 | 0.39 | 0.72 | 0.13 | 0.11 | 8.8% / 9.4% |
| Mar | 1.41 | 0.51 | 0.79 | 0.14 | 0.12 | 8.4% / 8.9% |
| Apr | 1.48 | 0.56 | 0.77 | 0.10 | 0.17 | 11.4% / 11.9% |
| May | 1.64 | 0.66 | 0.82 | 0.07 | 0.18 | 10.8% / 11.3% |
| Jun | 1.68 | 0.67 | 0.81 | 0.05 | 0.20 | 11.9% / 12.4% |
| Jul | 1.77 | 0.68 | 0.85 | 0.05 | 0.25 | 14.2% / 14.7% |
| Aug | 1.74 | 0.66 | 0.86 | 0.07 | 0.23 | 13.1% / 13.6% |
| Sep | 1.61 | 0.56 | 0.83 | 0.08 | 0.22 | 13.9% / 14.5% |
| Oct | 1.55 | 0.50 | 0.86 | 0.11 | 0.20 | 13.0% / 13.6% |
| Nov | 1.38 | 0.41 | 0.78 | 0.11 | 0.19 | 14.0% / 14.4% |
| Dec | 1.34 | 0.38 | 0.71 | 0.12 | 0.26 | 19.6% / 20.0% |

**What the annual chain could not see.** The block is sized to the average night and a residential load peaks after
sunset, so the block cannot carry the evening in any month; the shortfall is year-round and evening-led, worst in
December at 20% (mid). Sixteen hours of store cannot move June into December: the store empties on winter
nights while a share of June's field is defocused. The heater and PV overbuild were never the lever; the block, the
field and the water are.

**The Central Valley node (F-22).** Its DNI is 0.78 of the Mojave's. Moving it to a desert site lifts the served share from
0.874 to 0.886 and December's shortfall from 19.6% to 14.5%, and does not change the closing sizing: the
node is kept for its land (§P), which the deserts do not have in fallowed, private, disturbed form.

![Figure 5](figures/fig-04-monthly.png)

*Figure 5. The load by month and what the plant as sized serves, both cases (hourly3.py).*

![Figure 6](figures/fig-05-load-shape.png)

*Figure 6. The residential load shape on a late-July and a late-December day, relative to the annual mean hour; the shaded band is the day PV serves directly.*

## H. Closing the load

**Three routes.** The **mirrors** route grows the block to ×1.25, the field to ×1.5 and the store to 2 days, the cheapest
point of `hourly3.py`'s scan that closes to 1 %. The **water** route lifts Title II's product to an elevated reservoir with
the summer surplus (the field it would otherwise defocus and the PV it would curtail) and returns it year-round through
pump-turbines to the evenings — the author's decision of 2026-09-11 that the water comes down year-round, summer
irrigation and winter recharge, so the reservoir holds 30 / 60 days rather than a season. The feasibility rule is that a
closing point must lift its water inside its own run's surplus: a lift bought from the grid is not this route, and the
scan refuses it. **Water alone has no feasible point on this load**: with the field and store at design, the block that
closes the evening eats the spill the lift runs on. **The author chose both** (`both.py`): the water returns half the
shortfall, the plant the other half, each point on a ladder over the water's share required to lift inside its own surplus.

| share of the shortfall returned by water | mid: block, field, store, MW; Title I $B; +$/MWh; left to grid | critical: the same |
|---|---|---|
| 0.00 (mirrors alone, on this scan's grid) | ×1.25, ×1.50, 2 d, 0 MW; 5.7; +42; 0.8% | ×1.50, ×1.25, 2 d, 0 MW; 9.0; +64; 0.8% |
| 0.25 | ×1.50, ×1.25, 1 d, 1,500 MW; 6.3; +45; 0.6% | ×1.50, ×1.25, 1 d, 1,500 MW; 10.0; +72; 0.7% |
| 0.50 **(adopted)** | ×1.50, ×1.25, 1 d, 1,500 MW; 6.4; +45; 0.6% | ×1.50, ×1.25, 1 d, 1,500 MW; 10.3; +74; 0.7% |
| 0.75 | ×1.50, ×1.25, 1 d, 1,500 MW; 6.5; +46; 0.6% | ×1.50, ×1.25, 1 d, 1,500 MW; 10.7; +77; 0.7% |
| 1.00 | ×1.50, ×1.25, 1 d, 1,500 MW; 6.6; +47; 0.6% | ×1.50, ×1.25, 1 d, 1,500 MW; 11.0; +79; 0.7% |

**The adopted point:**

| | mid | critical |
|---|---|---|
| block / field / store | ×1.50 / ×1.25 / 1 d | ×1.50 / ×1.25 / 1 d |
| pump-turbine plant, MW | 1,500 | 1,500 |
| Title II modules / million acre-feet a year | 15 / 0.75 | 17 / 0.83 |
| Title I capital: plant growth / water side (reservoir and pump-turbines) / total, $B | 3.9 / 2.4 / 6.4 | 5.9 / 4.4 / 10.3 |
| mirrors alone, for comparison, $B | 5.7 | 9.5 |
| both over mirrors | 1.12× | 1.09× |
| added to the price, $/MWh | +45 | +74 |
| left to the grid | 0.6% | 0.7% |
| with the water withheld | 3.6% | 4.0% |
| with the field at design | 1.3% | 1.4% |
| with neither (as sized) | 12.6% | 13.1% |
| water sized to return / dispatched in the run / lift for the sized water / surplus available, TWh | 1.14 / 0.54 / 1.40 / 3.37 | 1.19 / 0.58 / 1.64 / 3.47 |
| O&M the closing plant adds, plant / water side, $M/yr | 99 / 37 | 125 / 111 |

Two levers that fail differently, each carrying a real share. A cheapest-point search returns mirrors with a token
water plant, so the even split is adopted as the author's word and marked DECIDED, movable on the ladder.

**Two things a reader should see in that table.** The water is *sized* to return half the shortfall as sized (1.14 TWh at
mid) and the run *dispatches* 0.54, because the larger block serves the evening first and the pump-turbines take what
it leaves; the modules are sized on the shortfall, not on what is dispatched, so the water plant runs at about half its
evening sizing and all of its water is delivered as irrigation and recharge regardless. That is the conservative side
for Title II and the expensive side for Title I, and it is stated rather than hidden. And the mirrors-alone figure the
comparison uses is `hourly3.py`'s one fixed route (block ×1.25, field ×1.5, store 2 days at both cases, $5.7 / 9.5 B), which
is what Title III prints; the ladder's own scan, which lets the block and field vary per case, finds a cheaper
mirrors-only point at critical ($9.0 B). Both are the instruments' and neither is hidden.

**The hydraulics.** The adopted route is priced at one head, 500 m (ASSUMED; the Edmonston lift is 587 m, Gianelli about 100), at both cases.
There a cubic metre returns 1.226 / 1.158 kWh and costs 1.514 / 1.603 kWh to lift, a round trip of
0.81 / 0.72 (turbine and pump at 0.90 / 0.85 each); reverse osmosis itself takes 3.0–3.6 kWh/m³ on Title II's own account. The
lift is invariant in head (returned energy over the round trip), so feasibility does not depend on the site; the
volume, and so the modules and Title II's capital, go as one over head, and the sensitivity below runs the head band
from 300 to 800 m. The pump-turbine plant and reservoir carry O&M at 1.5 / 2.5 % of their capital a year (ASSUMED band).

**Sensitivity to the two site assumptions**, the hourly run held fixed:

| case | head, m | days held | modules | MAF/yr | reservoir, $B | Title I, $B | +$/MWh | Title II, $B |
|---|---|---|---|---|---|---|---|---|
| mid | 300 | 14 | 25.1 | 1.25 | 0.15 | 6.3 | +45 | 47 |
| mid | 300 | 30 | 25.1 | 1.25 | 0.32 | 6.5 | +46 | 47 |
| mid | 300 | 60 | 25.1 | 1.25 | 0.64 | 6.8 | +48 | 47 |
| mid | 300 | 90 | 25.1 | 1.25 | 0.95 | 7.1 | +50 | 47 |
| mid | 500 | 14 | 15.0 | 0.75 | 0.09 | 6.3 | +45 | 28 |
| mid | 500 | 30 | 15.0 | 0.75 | 0.19 | 6.4 | +45 | 28 |
| mid | 500 | 60 | 15.0 | 0.75 | 0.38 | 6.6 | +47 | 28 |
| mid | 500 | 90 | 15.0 | 0.75 | 0.57 | 6.8 | +48 | 28 |
| mid | 800 | 14 | 9.4 | 0.47 | 0.06 | 6.2 | +44 | 18 |
| mid | 800 | 30 | 9.4 | 0.47 | 0.12 | 6.3 | +45 | 18 |
| mid | 800 | 60 | 9.4 | 0.47 | 0.24 | 6.4 | +46 | 18 |
| mid | 800 | 90 | 9.4 | 0.47 | 0.36 | 6.5 | +46 | 18 |
| critical | 300 | 14 | 27.7 | 1.38 | 0.26 | 9.9 | +71 | 80 |
| critical | 300 | 30 | 27.7 | 1.38 | 0.56 | 10.2 | +73 | 80 |
| critical | 300 | 60 | 27.7 | 1.38 | 1.12 | 10.8 | +77 | 80 |
| critical | 300 | 90 | 27.7 | 1.38 | 1.68 | 11.3 | +81 | 80 |
| critical | 500 | 14 | 16.6 | 0.83 | 0.16 | 9.8 | +70 | 48 |
| critical | 500 | 30 | 16.6 | 0.83 | 0.34 | 10.0 | +72 | 48 |
| critical | 500 | 60 | 16.6 | 0.83 | 0.67 | 10.3 | +74 | 48 |
| critical | 500 | 90 | 16.6 | 0.83 | 1.01 | 10.7 | +77 | 48 |
| critical | 800 | 14 | 10.4 | 0.52 | 0.10 | 9.7 | +70 | 30 |
| critical | 800 | 30 | 10.4 | 0.52 | 0.21 | 9.9 | +71 | 30 |
| critical | 800 | 60 | 10.4 | 0.52 | 0.42 | 10.1 | +72 | 30 |
| critical | 800 | 90 | 10.4 | 0.52 | 0.63 | 10.3 | +74 | 30 |

The head is the site question that sizes Title II; the days of holding move Title I by under a billion.

![Figure 7](figures/fig-06-ladder.png)

*Figure 7. The ladder over the water's share: Title I's capital to close the load at each share, both cases, every point carrying the larger field; water alone with the field and store at design has no feasible point and is not on the ladder.*

![Figure 8](figures/fig-07-head.png)

*Figure 8. Title II modules the adopted route needs against the reservoir head, at each case's days of holding.*

## I. The risk register, mitigated upfront

The author's claim: *Helios-3 is actually better, and each cost can be fully mitigated upfront.* `helios3.py` tests
it the way an environmental register is tested: sixteen rows graded **before** and **after**, each carried by a
named part of the build, each marked DESIGN (retired by specification), HOURS (retired only by operating time) or
BENEFIT, and each with the source that grades it. The file refuses to flatten HOURS: *a specification cannot make a
machine have run.* Walked row by row with the author on 2026-09-11; the author's design is written into each row.

**R-01. Particle attrition: grains break, make dust, and the medium is lost** — MODERATE → **NEGLIGIBLE**, DESIGN.

- *Mitigation:* Particle geometry: spherical sintered bauxite (roundness ~0.9), tight size cut. SYSTEM geometry (author, 2026-09-11): short drops, few transfer points, particles land on particles (rock-box liners, dead beds), mass-flow hoppers, gravity flow everywhere but the one cold lift. Enclosed conveyance; makeup in O&M; dust to baghouse. Fallback noted: a fixed ceramic bed with air as the moving fluid (Julich class) wears nothing and is a different plant
- *Carried by:* particle specification; plant arrangement (drops, transfer points, liners, hopper flow); conveyance; O&M makeup line
- *Source:* SOURCED: after ~200 h on-sun in Sandia's 1 MW_t receiver, used-particle absorptance 0.946 vs 0.945 unused -- durability shown at hours scale, not decades; residual is HOURS
- *Priced:* $126 M at mid, $205 M at critical

**R-02. Receiver wind and convective loss: a falling curtain is open to the air** — MAJOR → **MODERATE**, HOURS.

- *Mitigation:* Compound quartz aperture (author, 2026-09-11): a dome lattice of long hexagonal-section low-OH fused-quartz rod lenses, each a two-surface thick lens placing its focus in the receiver, the dome acting as secondary concentrator and flux homogeniser aimed jointly with the field; hot face at cavity temperature, cold end in a cooled frame; single-element replacement. Aperture cooling loop (author, 2026-09-11): hollow hex webs carry a closed water or oil loop (latitude rings as headers, meridian webs as tubes); mushroom-head rods so entry faces tile 100 % and the webs run beneath, unshadowed; the loop touches the rods at the cold ends only and returns the rod leak and absorbed light to the sCO2 cycle after the main compressor, or to the winter heaters. Multi-aperture receivers on smaller towers
- *Carried by:* receiver specification; aperture element specification; aperture cooling loop (frame manifold, preheat tie-in); tower count
- *Source:* SOURCED: windowed receiver +11.9 % efficiency over aerowindow; quartz half-shell transmissivity 0.97 / 0.94; fused silica k 1.38 W/m K, CTE 0.55 ppm/K, devitrification above ~1,100 C. Rod length is cheap in light (low-OH quartz ~1.3 % from 1 to 30 cm) and buys a gentler gradient; what it cannot move is the hot-face temperature. No windowed receiver has run at commercial scale -- residual is HOURS
- *Priced:* $321 M at mid, $547 M at critical

**R-03. Particle-to-sCO2 heat exchanger: 800 C particles against 250 bar CO2** — MAJOR → **MODERATE**, HOURS.

- *Mitigation:* Moving packed-bed exchanger (Sandia / Solex / VPE lineage), low particle velocity for erosion, modular N+1 units so one can be out. Fluid decision (author, 2026-09-11): CO2 stays -- every efficient cycle at this temperature is a high-pressure cycle (steam 170-300 bar, CO2 250), and the low-pressure gases (helium, air) need a hotter source than a particle receiver makes; the fill may be a CO2 blend (SCARABEUS class) for the hot-ambient dry-cooling case, same machinery and pressure, decided later
- *Carried by:* power block; spares policy; working-fluid fill
- *Source:* SOURCED: prototype 4-6x any known particle/sCO2 exchanger, tested to 500 C at 17 MPa, U ~300-400 W/m2K; design point is 800 C / 25 MPa -- the gap is HOURS at the design point
- *Priced:* $275 M at mid, $328 M at critical

**R-04. sCO2 turbomachinery at 715 C and 250 bar** — MAJOR → **MODERATE**, HOURS.

- *Mitigation:* Inconel 740H for the hot path; many small units (10-50 MWe) rather than few large, so a unit is a spare; STEP's recompression configuration. Materials margin (author, 2026-09-11): pressure boundary 740H (rated 825 C, operating 715, margin 110 C), Haynes 282 alternate; rotor in single-crystal aero superalloy running ~300 C below its design point; no ceramic or refractory metal in the CO2 path. Residual is carburisation at 100,000 h, which temperature margin does not buy
- *Carried by:* power block specification; unit sizing; materials specification (boundary and rotor)
- *Source:* SOURCED: 740H is ASME-qualified 650-825 C, the only age-hardened superalloy approved for welded creep-limited pressure parts; STEP's RCBC at 715 C / 250 bar is its next phase, 16 MW turbine under 100 kg -- residual is HOURS
- *Priced:* $220 M at mid, $262 M at critical

**R-05. CO2 inventory release: heavier than air, 4 % is IDLH, cold on release** — MODERATE → **MINOR**, DESIGN.

- *Mitigation:* Open-air or forced-ventilated turbine yards; no occupied low ground; CO2 sensors and dump tanks; inventory held per module, not per plant
- *Carried by:* site layout; safety systems
- *Source:* SOURCED: hazard characterised in the CCUS literature; a power loop's inventory is tens of tonnes per module against tens of thousands in a CCUS pipeline; standard pressure-plant practice
- *Priced:* $55 M at mid, $66 M at critical

**R-06. High-pressure, high-temperature containment (250 bar / 715 C)** — MODERATE → **MINOR**, DESIGN.

- *Mitigation:* 740H piping and headers under ASME Section I/VIII; design by code, not novelty. Alloy ladder (author, 2026-09-11): 740H primary; Haynes 282 second source; Inconel 617 fallback for the hottest headers under its Section III Division 5 case to 950 C at about twice the wall. Single-crystal and ODS alloys excluded from pressure parts: neither can be made as welded pipe
- *Carried by:* pressure-part specification; alloy ladder
- *Source:* SOURCED: 740H is the code-approved material for exactly this duty; 617 carries the Division 5 case to 950 C at roughly half 740H's allowable stress at 715 C
- *Priced:* $83 M at mid, $98 M at critical

**R-07. Silo heat loss and thermal ratcheting at 800 C over forty years** — MODERATE → **MINOR**, DESIGN.

- *Mitigation:* Refractory-lined silos with expansion allowance; large silos, because loss goes as surface over volume. Cold-shell design (author, 2026-09-11): lining thick enough that the steel shell stays below ~100 C, unbonded lining with expansion joints so it walks without cracking, replaceable inner liner so liner life is a maintenance item and not a forty-year bet; earth berm and a cold-silo pit at the tower base for seismic and wind. Hot silos are NOT buried: earth conducts ten times worse than the lining, burial breaks the gravity chain of R-01, and 800 C against wet ground is a steam event
- *Carried by:* storage specification; liner replacement in O&M; site civil (berm, pit)
- *Source:* SOURCED: rock, sand and bauxite operate to >1000 C; loss falls with silo size; hot-blast stoves and cement preheaters run refractory linings for decades of daily cycling. Forty-year life of ONE liner would be HOURS; a replaceable liner makes it O&M, which is why the row stays DESIGN
- *Priced:* $101 M at mid, $164 M at critical

**R-08. Particle chemistry: bauxite oxides transform in air at 700-1000 C** — MODERATE → **MODERATE**, HOURS.

- *Mitigation:* Periodic reduction to rejuvenate absorptance; makeup; inert or lean atmosphere in the hot silo
- *Carried by:* O&M rejuvenation line; silo atmosphere
- *Source:* SOURCED: XRD shows transformations in sintered bauxite after heating in air; absorptance can be restored by reduction -- rate over decades unknown

**R-09. Particle lift: erosion and temperature on the elevator** — MODERATE → **MINOR**, DESIGN.

- *Mitigation:* Lift COLD particles only; everything after the receiver is gravity-driven, so the lift never sees 800 C
- *Carried by:* plant arrangement
- *Source:* SOURCED: G3P3's own architecture -- skip hoist to the receiver top, free-fall through receiver, storage and exchanger

**R-10. Dust as PM10 in non-attainment counties** — MODERATE → **MINOR**, DESIGN.

- *Mitigation:* Negative-pressure enclosed handling with baghouse; no open transfer points
- *Carried by:* conveyance; air permit
- *Source:* Kern, Imperial, San Bernardino are PM10 non-attainment; enclosed bulk handling is ordinary practice
- *Priced:* $38 M at mid, $61 M at critical

**R-11. Receiver scale: no particle receiver has run above ~2.5 MW_t** — DOMINANT → **MAJOR**, HOURS.

- *Mitigation:* Multi-aperture receivers; more, smaller towers; a first module built and run before the fleet. FLAGGED FOR SIMULATION (author, 2026-09-11): receiver.py is the first -- the curtain is a per-metre machine, so scale is bought in width and aperture count; the loss fraction at fixed flux does not change with size and the edge losses shrink as perimeter/area; and the 100 MWe module is already 0.55 of a fleet tower, so a pilot aperture at fleet-aperture size (~30 MW_th, a 10 m curtain) goes between, and every fleet aperture is a copy of it
- *Carried by:* tower count; programme staging (pilot aperture before the module); receiver.py
- *Source:* SOURCED: G3P3-USA falling receiver 2 MW_th (>250 h, 80-90 % measured, 2024); DLR CentRec centrifugal 2.5 MW_th (965 C, 2018); Helios-3 needs ~800 MW_th per tower. Design can split the receiver; only hours can prove it

**R-12. Provenance: no plant of this kind exists at any commercial scale** — DOMINANT → **MAJOR**, HOURS.

- *Mitigation:* Stage: build the common field, towers and PV for Helios-2 OR Helios-3; build one Helios-3 module first; convert modules as hours accumulate. Ladder (author, 2026-09-11): common field, towers and PV; a ~30 MW_th pilot aperture on one tower (receiver.py); the 100 MWe module as copies of the pilot; the fleet as copies of the module; each rung passed at its critical figure and handed up the chain before the next is ordered. Provenance is LISTED rather than asserted: studies.py holds every technology in the system, every study covering it (a floor, sourced), the further study recommended per rung, and the cost of delay at the construction escalation rate. Salt block as fallback
- *Carried by:* programme staging (ladder); studies.py (provenance register, recommendations, delay cost)
- *Source:* This row cannot be mitigated by a specification. What is upfront is the PLAN that buys the hours, and the LIST of what has and has not run

**R-13. No freezing point: no heat tracing, no drain-down, no hot-tank failure** — BENEFIT → **BENEFIT**, BENEFIT.

- *Mitigation:* -
- *Carried by:* -
- *Source:* SOURCED (reviewed 2026-09-11): Crescent Dunes has had FOUR hot-salt tank leaks (2016, 2022, 2023 ...), its hot tank is now derated from ~565 C to 455-480 C and its output constrained to ~55 MW, half of design; Noor III's hot tank leaked in March 2024, the plant was offline 14 months, and it leaked again on return. Two of the three largest salt towers built have lost more than a year each to the hot tank. A silo of sand at ambient is a silo of sand -- and the salt-block FALLBACK carries this failure mode

**R-14. No decomposition ceiling: stable past 1000 C** — BENEFIT → **BENEFIT**, BENEFIT.

- *Mitigation:* -
- *Carried by:* -
- *Source:* nitrate decomposes above ~600 C; this is the link that buys the cycle

**R-15. No oxidiser and no toxic medium: the author's hazard rule, met cleanly** — BENEFIT → **BENEFIT**, BENEFIT.

- *Mitigation:* -
- *Carried by:* -
- *Source:* nitrate is NFPA OX; bauxite and sand are inert

**R-16. Dry cooling at a sixth of the airflow** — BENEFIT → **BENEFIT**, BENEFIT.

- *Mitigation:* -
- *Carried by:* -
- *Source:* SOURCED: sCO2 cooling profiles are near-parallel; steam needs ~6x the air

Before: 4 BENEFIT, 7 MODERATE, 3 MAJOR, 2 DOMINANT. After: 4 BENEFIT, 1 NEGLIGIBLE, 5 MINOR, 4 MODERATE, 2 MAJOR.

| priced, $M | mid | critical |
|---|---|---|
| direct plant lines (§F) | 16,399 | 24,544 |
| mitigation adders, direct | 1,218 | 1,731 |
| contingency (15 / 30 %), EPC and owner's cost (13 / 15 %), sales tax on those | 6,060 | 13,505 |
| studies and surveys (§L), with contingency | 245 | 602 |
| first-module premium (1.5× / 2.0× on its share of the thermal block) | 135 | 403 |
| overnight, groundbreaking dollars | 24,057 | 40,786 |
| escalation to the build and interest during construction (4 years at the bond rate) | 9,749 | 16,528 |
| gross capital | 33,806 | 57,314 |
| federal storage credit, direct pay | -1,130 | -1,871 |
| **net capital with the register, $M** | **32,677** | **55,443** |
| O&M with particle makeup (1 / 2 %/yr) and rejuvenation, $M/yr | 434 | 555 |
| price with the register, $/MWh | 126 | 205 |

## J. Provenance: every study that covers a technology in the system

R-12 says no plant of this kind exists; `studies.py` lists rather than asserts. 49 rows over the 12 technologies
the design uses, each with a status from a closed set — OPERATED (a plant has run at the stated scale), TESTED (a
prototype has run, below plant scale), DESIGNED (a published design or code case; nothing has run), AUTHOR (this
repository's own design; no study exists) — and a source. The register is complete over technologies and a floor
over studies; it was reviewed against the web on 2026-09-11 where the proxy reached and corrected in place.

### J.1. Heliostat field, Noor III class, surround, night-sized

*What the design needs:* ~31 M m2 critical / 18 M m2 mid across 3 nodes at design; 14-24 towers.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Gemasolar (Torresol), Fuentes de Andalucia | 19.9 MWe, 15 h salt storage | 2011 | OPERATED | first commercial salt tower; 24 h operation demonstrated; CF ~0.73 of design | Torresol Energy; Burgaleta et al., SolarPACES 2011 |
| Crescent Dunes (SolarReserve; Cobra 2021; Vinci 2023), Nevada | 110 MWe, 10 h salt, 1.2 M m2 | 2015 | OPERATED | US utility-scale salt tower; four hot-salt tank leaks (2016, 2022, 2023, ...); hot tank derated to 455-480 C after a 2023 root-cause analysis, output constrained to ~55 MW (half of design); CF ~0.39 of design over its first years; night-only contract since 2023 | SolarPACES 'What happened with Crescent Dunes'; Wikipedia project page (reviewed 2026-09-11); DOE Loan Programs Office |
| Noor III (ACWA/SENER), Ouarzazate | 150 MWe, 7.5 h salt, 1.3 M m2, 178 m2 heliostats | 2018 | OPERATED | the heliostat class the design carries; HOT-SALT TANK leak March 2024, offline 14 months (~$47 M loss), leaked again after the April 2025 restart | ACWA Power Tadawul statement 2024-03; pv magazine 2024-03-25; Hespress 2025 (reviewed 2026-09-11) |
| Cerro Dominador (EIG), Atacama | 110 MWe tower + 100 MWe PV, 17.5 h salt | 2021 | OPERATED | CSP + PV hybrid at one site; $10.45/W built cost | Cerro Dominador; SolarPACES project database |
| DEWA Phase IV (ACWA/Shanghai Electric), Dubai | 100 MWe tower + 600 MWe trough + 250 MWe PV | 2023 | OPERATED | night-sized thermal block beside daytime PV -- the Helios-2/3 architecture | DEWA; ACWA Power; SolarPACES project database |
| Chinese tower fleet: Shouhang Dunhuang 100 MWe, Supcon Delingha 50 MWe, Luneng Haixi 50 MWe | 50-100 MWe each | 2018 | OPERATED | salt towers at 100 MWe with small heliostats; multiple operators | CSPPLAZA; SolarPACES project database |
| NREL HelioCon heliostat consortium | cost and performance roadmap | 2022 | DESIGNED | heliostat cost targets and failure modes; the $80-120/m2 band | NREL HelioCon (2022-) |
| Ivanpah (BrightSource), California | 392 MWe direct steam, 3 towers | 2014 | OPERATED | California desert siting, permitting, avian and dust record; no storage; contracts ending | NRG/BrightSource; CEC docket 07-AFC-5 |

*Further study recommended, on the field rung (1.0 years):* Field commissioning at the first node with measured annual optical efficiency against the 0.58-0.64 band. *It settles:* the largest chain link after the receiver; sets the mirror count at critical.

### J.2. Falling-particle cavity receiver, multi-aperture

*What the design needs:* ~800 MW_th per tower; 30 MW_th per aperture, 26 apertures.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Sandia NSTTF 1 MW_th falling-particle receiver | 1 MW_th, ~1 m2 aperture, chevron mesh option | 2015 | TESTED | outlet >700 C; efficiency 50-80 % (60-70 % free-fall, ~80 % obstructed); 50-200 C per metre of drop at 1-7 kg/s per m and average irradiance to ~0.7 MW/m2; the fixture in receiver.py | Ho et al., AIP Conf. Proc. 1734 (2016); J. Sol. Energy Eng. 141 (2019); OSTI 1364838, 1431441 (reviewed 2026-09-11) |
| G3P3-USA receiver, Sandia NSTTF | 2 MW_th, >250 h on-sun and ground | 2024 | TESTED | double the 1 MW_th unit; multistage release, reduced-volume cavity, automated flow control; 80-90 % efficiency in test campaigns -- the largest falling curtain that has run | Sandia LabNews 2024-08-22; Ho & Schroeder, AIP Conf. Proc. 2445 (2022) (reviewed 2026-09-11) |
| G3P3 Gen3 Particle Pilot Plant, integrated system, Sandia | 1 MW_th receiver + HX, 6 h storage, >700 C working fluid | 2025 | TESTED | receiver + silos + lift + heat exchanger as one system; particle loop assembled Dec 2024, commissioning from Jan 2025, on-sun from summer 2025; goal >2,000 h combined with G3P3-Saudi -- hours as published | Sandia LabNews 2025-02-06; OSTI 2999325 (cold commissioning); DOE Gen3 Phase 3 (reviewed 2026-09-11) |
| DLR CentRec centrifugal particle receiver, Julich | 2.5 MW_th prototype | 2018 | TESTED | rotating-drum alternative to a falling curtain; 965 C average outlet on sun; commercialised by HelioHeat -- the largest particle receiver of any type that has run | DLR Institute of Solar Research; Ebert et al., ASME ES2018; SolarPACES/HelioHeat (reviewed 2026-09-11) |
| CSIRO / ASTRI falling-particle receiver, Newcastle | ~1 MW-class system, 400-mirror field | 2023 | TESTED | second falling-particle receiver on sun, independent of Sandia; 803 C reached; spun off as FPR Energy | CSIRO 2023-10; SolarPACES (FPR Energy) (reviewed 2026-09-11) |
| King Saud University / Sandia multi-stage receiver, Riyadh | sub-MW | 2018 | TESTED | multi-stage (staggered) curtain to raise residence time | KSU / Sandia collaboration |
| Sandia Gen3 100 MWe particle plant design study | 100 MWe, multi-aperture | 2019 | DESIGNED | the multi-aperture layout and the $/kWe the design carries | Sandia Gen3 Roadmap / TEA (Ho et al. 2019-2021) |
| receiver.py (this repository) | scaling law, critical case | 2026 | AUTHOR | curtain as a per-metre machine; loss fraction size-invariant; pilot aperture rung | tools/receiver.py |

*Further study recommended, on the pilot rung (2.0 years):* A ~30 MW_th pilot aperture on one fleet tower: curtain fed uniformly across 60 m (critical) / 10 m (nominal); efficiency, edge loss vs aperture size, wind. *It settles:* receiver.py's threshold: 0.690 critical open (pilot.py's pass mark); whether the edge losses fall as perimeter/area.

### J.3. Compound quartz aperture: hex rod-lens dome with cooled lattice frame

*What the design needs:* one dome per aperture, hot face at cavity temperature.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| DLR REFOS / SOLGATE pressurised volumetric receivers, PSA | 250-400 kW_th, quartz window | 2003 | TESTED | domed quartz windows on cavity receivers at 800-1000 C air; window cooling and failure modes | Buck et al., J. Solar Energy Eng. 2002; SOLGATE final report 2005 |
| Sandia windowed falling-particle receiver study | modelled, 1 MW_th class | 2016 | DESIGNED | +11.9 % efficiency over an aerowindow; quartz half-shell transmissivity 0.97/0.94 | Ho / Yellowhair, Sandia SAND (Gen3 windowed receiver) |
| Author's compound quartz aperture (helios3.py R-02) | hex rod-lens dome, cooled lattice | 2026 | AUTHOR | no study exists; receiver.py prices it against the open aperture | tools/helios3.py R-02; tools/receiver.py |

*Further study recommended, on the pilot rung (1.0 years):* The compound quartz aperture on the pilot: one dome, open aperture beside it, both measured on one tower. *It settles:* whether the dome pays on the measured record as receiver.py says, or loses as the model says.

### J.4. Sintered bauxite particles as medium and store

*What the design needs:* hundreds of kt inventory, 600-800 C, forty years.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Sandia particle durability and optical studies (CARBO Accucast ID50, ~280 um) | lab + 1 MW_th on-sun | 2014 | TESTED | packed-bed absorptance 0.946 after ~200 h on-sun, statistically the same as 0.945 unused; 11 of 140 formulations held >0.90 after 500 h in air at 700 C; sintered bauxite chosen for absorptance, abrasion and sintering resistance and reducibility; oxide transformations on heating in air (R-08) | Siegel et al., J. Sol. Energy Eng. 137 (2015); Ho et al., OSTI 1431441; Sandia 2016 review (reviewed 2026-09-11) |
| CARBO Ceramics proppant production | industrial, Mt/yr | 2000 | OPERATED | the medium is a commodity with a supply chain | CARBO Ceramics product data |

*Further study recommended, on the pilot rung (3.0 years):* Long-duration particle ageing on the pilot: absorptance, attrition and oxide state sampled quarterly. *It settles:* R-08's rate over decades, the UNMOVED row; R-01's makeup rate.

### J.5. Cold-shell refractory-lined particle silos, replaceable liner

*What the design needs:* 84 GWh_th mid; 800 C hot silo; daily cycling.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| G3P3 hot and cold particle bins | 6 h at ~1 MW_th, refractory-lined | 2024 | TESTED | 800 C particle storage in a lined steel bin | Sandia G3P3 |
| Sandia / Bridgers & Paxton commercial-scale particle silo design | 100 MWe-class, 6-12 h | 2020 | DESIGNED | cold-shell lined silo design and cost; thermal ratcheting analysis | Sandia Gen3 storage design reports |
| Siemens Gamesa ETES rock-bed thermal store, Hamburg | 130 MWh_th, 750 C, electrically charged | 2019 | OPERATED | a hot solid store at scale, charged by resistance heaters -- the winter heater path | Siemens Gamesa ETES pilot (2019-2022) |
| Hot-blast stoves and cement preheaters (industrial precedent) | decades, daily cycling, >1,000 C | 1900 | OPERATED | refractory linings cycling daily for decades; replaceable liners as O&M | steel and cement industry practice |

*Further study recommended, on the pilot rung (3.0 years):* One full-size cold-shell silo on the pilot, cycled daily, liner inspected annually. *It settles:* thermal ratcheting and liner life as O&M.

### J.6. Cold-side particle lift (skip hoist / bucket elevator)

*What the design needs:* ~150 kg/s per aperture, ambient temperature.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| G3P3 skip hoist / bucket elevator | ~1 MW_th class, cold side | 2024 | TESTED | cold particle lift to receiver top | Sandia G3P3 |
| Mining skip hoists and bulk-solids bucket elevators | thousands of t/h, ambient | 1950 | OPERATED | cold abrasive bulk lift is an industry, not a development | bulk-solids handling practice |

*Further study recommended, on the pilot rung (0.0 years):* None beyond the pilot's own lift: cold abrasive lift is an industry. *It settles:* nothing open.

### J.7. Moving packed-bed particle-to-sCO2 heat exchanger

*What the design needs:* 800 C particles against 250 bar CO2, 2,620 MWe fleet.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Sandia / Solex / VPE moving packed-bed particle-to-sCO2 exchanger | 100 kW_th shell-and-plate prototype | 2020 | TESTED | ground tests with a 150 kW electric particle preheater to 500 C; overall U approaching 400 W/m2 K; 4-6x any other known particle/sCO2 exchanger; design point 800 C / 25 MPa untested | Albrecht & Ho, Sandia (AIP Conf. Proc. 2020; Sandia 2022 performance evaluation); Sandia LabNews 2021-06 (reviewed 2026-09-11) |
| G3P3 integrated particle-to-sCO2 exchanger | ~1 MW_th | 2024 | TESTED | exchanger in the loop with receiver and storage | Sandia G3P3 |
| NREL fluidised-bed particle heat exchanger (Ma et al.) | lab / design | 2017 | DESIGNED | the fluidised-bed alternative; particle-side heat transfer coefficients | Ma et al., NREL (2014-2020) |

*Further study recommended, on the pilot rung (2.0 years):* A particle-to-sCO2 exchanger module at its design point, 800 C / 25 MPa, on the pilot. *It settles:* R-03: the 4-6x scale-up and the design-point pressure-temperature pair.

### J.8. sCO2 recompression Brayton power block, 715 C / 250 bar, dry-cooled

*What the design needs:* 10-50 MWe units, 2,620 MWe fleet, 45 C ambient.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| STEP Demo (GTI / SwRI / GE), San Antonio | 10 MWe plant; 4 MWe grid-synchronised in simple recuperated cycle | 2024 | TESTED | first electricity May 2024; maximum simple-cycle power 4 MWe Sept 2024 at ~500 C (Phase 1 complete); Phase 2 reconfigures to recompression at 715 C from 2025 -- the 50 % RCBC has NOT yet run | GTI Energy STEP Demo Phase 1 milestone; POWER magazine; ASME GT2025 simple-cycle testing paper (reviewed 2026-09-11) |
| Sandia sCO2 recompression Brayton test loop | ~1 MWe class | 2012 | TESTED | recompression cycle operated; compressor near the critical point | Sandia SAND2012-9546 (Wright et al.) |
| Echogen EPS100 | 8 MWe sCO2 waste-heat | 2014 | TESTED | a commercial sCO2 turbine-generator at MW scale (simple recuperated, ~300 C) | Echogen Power Systems |
| China Huaneng / XTPRI 5 MWe sCO2 unit, Xi'an | 5 MWe, fossil-fired | 2021 | TESTED | put into service Dec 2021 after a 72 h trial; a 50 MWe demonstration planned -- second MW-class sCO2 unit, independent of the US programme | SASAC 2021-12-23; Energy (2023) startup study (reviewed 2026-09-11) |
| SCARABEUS CO2-blend cycle project (EU) | lab loops + design | 2019 | DESIGNED | CO2 + dopant blends to raise the critical point for hot-ambient dry cooling (R-03 note) | EU H2020 SCARABEUS (2019-2023) |
| NETL / SunShot sCO2 CSP system studies | design + TEA | 2015 | DESIGNED | sCO2 RCBC at ~50 % for 700 C CSP; the cycle value the chain carries | DOE SunShot sCO2 (2012-2018); NETL |

*Further study recommended, on the module rung (3.0 years):* STEP's 715 C recompression phase, then one 10-50 MWe unit on the first module. *It settles:* R-04: turbine, seals and bearings at 715 C; carburisation on the real loop.

### J.9. Inconel 740H / Haynes 282 / Inconel 617 pressure parts

*What the design needs:* 715 C / 250 bar, 100,000 h, CO2 carburisation.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| ASME Code Case 2702, Inconel 740H | 650-825 C pressure parts | 2011 | DESIGNED | the only age-hardened superalloy approved for welded creep-limited pressure parts | ASME BPVC Code Case 2702 (2011) |
| US DOE / EPRI A-USC ComTest programme | 700 C steam components, full scale | 2015 | TESTED | 740H headers, piping and valves fabricated and tested for 760 C steam | DOE/OCDO A-USC (2001-2021); EPRI |
| ASME Code Case 3024, Haynes 282 | pressure parts, same class | 2021 | DESIGNED | the second source; base, cross-weld and all-weld qualification for superheaters, reheaters and steam pipe | ASME BPVC Code Cases Supplement 2 (2021); ORNL Pub140621 (reviewed 2026-09-11) |
| ASME Section III Division 5, Inconel 617 | to 950 C, nuclear high-temperature | 2019 | DESIGNED | the fallback with the deepest temperature margin | ASME BPVC III-5 (2019 edition, Alloy 617) |
| sCO2 corrosion / carburisation testing of Ni alloys | coupons, 700-750 C, 20-25 MPa, to ~10,000 h | 2016 | TESTED | carburisation slow but present; 100,000 h is extrapolated -- the residual in R-04 | ORNL, NETL, Sandia coupon programmes |

*Further study recommended, on the pilot rung (3.0 years):* Coupon and component exposure in the pilot's CO2 loop to the longest hours the schedule allows. *It settles:* R-04/R-06 residual: carburisation at 100,000 h, by extrapolation from the longest real exposure.

### J.10. PV direct daytime supply with PV-fed electric heaters for winter

*What the design needs:* 2.9 GW_AC PV, 3.5 GW_th heaters.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Noor Midelt I (EDF/Masdar/Green of Africa), Morocco | 800 MW CSP + PV hybrid, PV-charged salt storage via electric heaters | 2019 | DESIGNED | the first plant designed to heat thermal storage from PV -- PPA 2019, construction NOT started as of 2025; Midelt II and III re-awarded in 2024 as PV + batteries | SolarPACES (Midelt PV-to-storage); REN21 GSR 2025; NS Energy (reviewed 2026-09-11) |
| California utility PV fleet | >20 GW installed, Mojave single-axis | 2020 | OPERATED | the PV capacity factor band the chain carries | CEC / EIA installed capacity data |
| Electric resistance heaters for high-temperature stores | MW-class, 750 C (ETES); salt heaters commercial | 2019 | OPERATED | resistance heating of a hot solid store at MW scale | Siemens Gamesa ETES; Kraftblock; Malta (design) |

*Further study recommended, on the pilot rung (0.5 years):* A PV-fed electric particle heater at MW scale on the pilot's cold-to-hot path (Midelt I, the only plant designed for PV-to-storage, has not been built). *It settles:* heater efficiency and control on particles rather than salt; winter dispatch is measured by helios.py's hourly run.

### J.11. Dry (air-cooled) heat rejection for sCO2

*What the design needs:* zero water, 45 C ambient.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| Air-cooled condensers at CSP plants (Ivanpah, Cerro Dominador, Noor III) | 100-400 MWe | 2014 | OPERATED | dry cooling in desert CSP is standard | plant records |
| sCO2 dry-cooling studies (Sandia / NREL) | design | 2016 | DESIGNED | sCO2 needs ~1/6 the cooling airflow of steam; hot-ambient compressor-inlet penalty | Sandia / NREL sCO2 CSP studies |

*Further study recommended, on the module rung (1.0 years):* Compressor-inlet performance at 45 C on the first module's dry cooler. *It settles:* the cycle's 0.45-0.50 critical band; whether a CO2 blend is needed (R-03 note).

### J.12. Hybrid CSP + PV, thermal block sized for the night

*What the design needs:* 18.1 TWh/yr firm to 3 M households.

| study or plant | scale | year | status | what it settled | source |
|---|---|---|---|---|---|
| DEWA Phase IV hybrid | CSP night + PV day, one site | 2023 | OPERATED | the architecture at 950 MW total | DEWA / ACWA Power |
| Cerro Dominador hybrid | 110 MWe tower + 100 MWe PV | 2021 | OPERATED | CSP + PV hybrid dispatch record | Cerro Dominador |
| cspchain.py / helios.py (this repository) | hourly model, mid and critical | 2026 | AUTHOR | night-sized field; PV direct; winter heaters; the critical case | tools/cspchain.py; tools/helios.py |

*Further study recommended, on the now rung (0.5 years):* RUN (hourly3.py, 2026-09-11, corrected load shape): Helios-3 hour by hour at both cases -- as sized it serves 87 % of the load, year-round and evening-led; the mirrors route closes at block x1.25, field x1.5, store 2 d at the price hourly3.mirrors_price_delta computes; the adopted route is both.py's. *It settles:* the evening peak in every month (F-06); the heater was never the lever, the block, the field and the water are.

**The critical path of study is 7.5 years**, run against the build rather than before it, the studies within a rung
in parallel. **Delay** escalates the whole plant at 3 % a year (ASSUMED band 2–4 %) before a dollar is spent:

| per year of delay | mid | critical |
|---|---|---|
| capital, $B | 0.98 | 1.66 |
| price, $/MWh | 3.8 | 6.1 |
| household, $/yr | 23 | 37 |

## K. The pilot aperture: an acceptance protocol

The receiver's real efficiency is the one open item no instrument can close, and a test graded after it runs is
not a test. `pilot.py` fixes the unit, the measurements and the pass mark before the pilot is built.

| the unit | nominal (mid) | critical |
|---|---|---|
| one aperture carrying 30 MW_th: curtain width, m | 10.0 | 60.0 |
| aperture area, m² | 30.0 | 60.0 |
| drop per stage, m | 3.0 | 1.0 |
| particle mass flow, kg/s | 125 | 150 |
| aperture-average flux, MW/m² / ambient, °C | 1.0 / 25 | 0.5 / 45 |

**Five measurements:**

- **M1 thermal efficiency.** particle mass flow (weigh-cell), inlet and outlet temperature, incident flux by calibrated heliostat field and flux gauge; eta = m cp dT / (q A). *Condition:* critical conditions: 0.5 MW/m2 aperture-average, 45 C ambient, 800 C outlet, hot back wall.
- **M2 edge losses.** M1 repeated at half and full curtain width on the same aperture. *Condition:* loss per m2 must fall from half to full width as perimeter/area (receiver.py's scaling law).
- **M3 dome against open.** one compound quartz dome (R-02) beside an open aperture on one tower, M1 on both. *Condition:* whether the dome pays on the record or loses on the model; both are printed by receiver.py.
- **M4 particle ageing.** absorptance, attrition and oxide state sampled quarterly from the pilot's own inventory. *Condition:* R-01 makeup rate and R-08's rate, the UNMOVED row.
- **M5 wind.** M1 across the site wind envelope, curtain stability by camera. *Condition:* the graded figure must hold across the envelope, not at calm.

**The pass mark**, M1 at critical conditions averaged over the last 500 of 1000 on-sun hours, with a calorimetric
uncertainty of **3.3 %** in quadrature (mass flow 1 %, temperatures 1 %, flux 3 %):

| grade | measured efficiency | what follows |
|---|---|---|
| PASS-CHAIN | ≥ 0.930 | the chain's own link is witnessed; mid is witnessed too |
| PASS-DESIGN | ≥ 0.713 | the critical design basis holds; the first module is ordered |
| UNDECIDED | 0.667 – 0.713 | not a pass and not a fail; the pilot runs on |
| FAIL | < 0.667 | the salt-block fallback is the recorded route; the first module is not ordered |

**What each result does upstream**, priced against each case's own receiver link, so a pass at the design basis
costs the critical design nothing:

| measured | grade | field factor, mid / critical | price, mid / critical, $/MWh |
|---|---|---|---|
| 0.600 | FAIL | 1.50 / 1.15 | +21 / +11 |
| 0.667 | FAIL | 1.35 / 1.03 | +15 / +3 |
| 0.690 | UNDECIDED | 1.30 / 1.00 | +13 / +0 |
| 0.713 | UNDECIDED | 1.26 / 0.97 | +11 / -2 |
| 0.800 | PASS-DESIGN | 1.12 / 0.86 | +5 / -10 |
| 0.900 | PASS-DESIGN | 1.00 / 0.77 | +0 / -18 |
| 0.930 | PASS-CHAIN | 0.97 / 0.74 | -1 / -19 |

Scheduled 2031–2033 (mid) / 2033–2035 (critical) at $159 / 246 M including the ladder's technology
studies. The protocol constants are ASSUMED and say so; the pass mark is not.

## L. Studies and surveys first

The author's instruction of 2026-09-11: every study and survey is its own upfront line item, preceding the others
by first priority. `predev.py` prices them from the class of study — ASSUMED bands, not quotes — and carries them
in the capital ahead of every plant line, with contingency and without EPC margin or sales tax.

**Title I.** Gating studies must finish before the field rung; the technology studies run on the ladder against the build.

| id | study or survey | what it settles | scope | mid: $M each × n = total, years | critical: the same |
|---|---|---|---|---|---|
| dni | one year of on-site DNI at each node (class-A pyrheliometer station) | the node's field size; profiles.py's replacement of the reconstructed series | node, GATE | 0.1 × 3 = 0.4, 1.0 | 0.3 × 3 = 0.9, 1.5 |
| load | measured residential load profile for the served territory (CAISO / CCA metered data) | the evening block factor; profiles.py's load series | program, GATE | 0.5 × 1 = 0.5, 0.5 | 1.0 × 1 = 1.0, 1.0 |
| title | title search, land survey and fallowing agreements | sites.py's land term | node, GATE | 3.0 × 3 = 9.0, 1.0 | 6.0 × 3 = 18.0, 2.0 |
| geotech | geotechnical investigation and ASCE 7 site-specific seismic hazard (mapped MCE_R) | minors.py's seismic margin; the tower foundation | node, GATE | 2.0 × 3 = 6.0, 1.0 | 4.0 × 3 = 12.0, 1.5 |
| bio | biological and cultural resource surveys (protocol-level, two seasons) | CEQA / NEPA baseline; desert tortoise and cultural sites | node, GATE | 3.0 × 3 = 9.0, 1.5 | 8.0 × 3 = 24.0, 2.0 |
| ceqa | CEQA environmental impact report per node | the state permit; majors.py F-25 | node, GATE | 15.0 × 3 = 45.0, 2.0 | 30.0 × 3 = 90.0, 3.0 |
| nepa | NEPA environmental impact statement on the Mojave node (BLM nexus) | majors.py F-25: 2 / 4 years | mojave, GATE | 15.0 × 1 = 15.0, 2.0 | 30.0 × 1 = 30.0, 4.0 |
| grid | CAISO interconnection cluster study per node (deposits refundable, excluded) | titleone.py F-09's gen-tie | node, GATE | 2.0 × 3 = 6.0, 2.0 | 4.0 × 3 = 12.0, 3.0 |
| reservoir | reservoir siting, head survey and geotechnical study for the water route | both.py's head: the site question that sizes Title II | program, GATE | 15.0 × 1 = 15.0, 2.0 | 40.0 × 1 = 40.0, 3.0 |
| field-meas | field commissioning measurement of annual optical efficiency at the first node | studies.py: the 0.58-0.64 band | program, ladder | 2.0 × 1 = 2.0, 1.0 | 4.0 × 1 = 4.0, 1.0 |
| dome | compound quartz aperture beside an open aperture on the pilot tower | studies.py / pilot.py M3 | program, ladder | 5.0 × 1 = 5.0, 1.0 | 10.0 × 1 = 10.0, 1.0 |
| ageing | long-duration particle ageing sampled quarterly on the pilot | studies.py / pilot.py M4; R-01, R-08 | program, ladder | 3.0 × 1 = 3.0, 3.0 | 6.0 × 1 = 6.0, 3.0 |
| silo | one full-size cold-shell silo cycled daily on the pilot | studies.py: liner life as O&M | program, ladder | 5.0 × 1 = 5.0, 3.0 | 10.0 × 1 = 10.0, 3.0 |
| hx | particle-to-sCO2 exchanger module at 800 C / 25 MPa on the pilot | studies.py: R-03's 4-6x scale-up | program, ladder | 20.0 × 1 = 20.0, 2.0 | 40.0 × 1 = 40.0, 2.0 |
| sco2 | STEP's 715 C recompression phase, then one 10-50 MWe unit on the first module | studies.py: R-04 turbine, seals, bearings | program, ladder | 40.0 × 1 = 40.0, 3.0 | 80.0 × 1 = 80.0, 3.0 |
| alloy | coupon and component exposure in the pilot's CO2 loop | studies.py: carburisation by extrapolation | program, ladder | 3.0 × 1 = 3.0, 3.0 | 6.0 × 1 = 6.0, 3.0 |
| heater | PV-fed electric particle heater at MW scale on the pilot | studies.py: heater efficiency on particles | program, ladder | 8.0 × 1 = 8.0, 0.5 | 15.0 × 1 = 15.0, 0.5 |
| cooler | compressor-inlet performance at 45 C on the first module's dry cooler | studies.py: the cycle's critical band | program, ladder | 2.0 × 1 = 2.0, 1.0 | 4.0 × 1 = 4.0, 1.0 |

The 30 MW_th pilot aperture is priced by titleone.py as its own tranche from cspchain's lines and is not repeated here.

| Title I | mid | critical |
|---|---|---|
| gating studies and surveys, $M | 106 | 228 |
| technology studies on the ladder, $M | 88 | 175 |
| owner's engineer on the study phase (10 / 15 %), $M | 19 | 60 |
| **total, first in the capital, $M** | **213** | **463** |
| longest gating study, years | 2.0 | 4.0 |
| studies start / field rung starts | 2027 / 2029 | 2027 / 2031 |

**Title II**, per selected coastal site, plus a screening pass over the 8 candidates of §P:

| id | study | what it settles | mid: $M, years | critical: $M, years |
|---|---|---|---|---|
| screen | screening of the candidate brownfields against sites.py's seven terms | which sites go to study | 4.0, 0.5 | 8.0, 0.5 |
| outfall | outfall diffuser hydraulic and dilution study (Ocean Plan 17:1) | titletwo.py's brine term | 2.0, 1.0 | 4.0, 1.5 |
| entrain | intake entrainment study, two years under the Ocean Plan | titletwo.py's intake decision | 3.0, 2.0 | 6.0, 2.0 |
| survey | site survey, remediation scope and acreage confirmation | sites.py's acreage term | 2.0, 1.0 | 5.0, 1.5 |
| hazard | seismic and tsunami basis for the site | sites.py's hazard term | 1.0, 1.0 | 3.0, 1.0 |
| coastal | Coastal Development Permit pre-application and CEQA EIR per site | sites.py's permit term; titletwo.py's schedule | 10.0, 3.0 | 25.0, 5.0 |

| Title II | mid | critical |
|---|---|---|
| per selected site, $M | 18.0 | 43.0 |
| screening of the candidates, $M | 4.0 | 8.0 |
| per module at 5 / 3 modules a site, $M | 4.3 | 17.8 |
| longest study (the coastal permit), years | 3.0 | 5.0 |

## M. Price, the household and the financing

| $/MWh | mid | critical |
|---|---|---|
| Helios-3 as chained | 117 | 187 |
| with the mitigation register (§I) and the studies (§L) | 126 | 205 |
| serving the whole load, mirrors route | 168 | 272 |
| **serving the whole load, both (adopted)** | **172** | **279** |
| after the bonds retire: O&M only, register plant and closing plant | 31 | 44 |

| $ per household per year (today 1,177) | mid | critical |
|---|---|---|
| with the register | 763 | 1,234 |
| serving the whole load, mirrors route | 1,015 | 1,641 |
| **serving the whole load, both (adopted)** | **1,036** | **1,682** |
| after the bonds retire | 190 | 263 |

**The criterion, stated exactly.** At mid, Helios-3 with its register needs $126/MWh, $6 above the top of the
contract band, and a household pays $763 against $1,177 today; serving the whole load on the adopted route
costs $172, at which a household pays $1,036. At critical the register price is $205 and the whole load
$279: **$1,682 a household, above today's bill**. The plant pays for itself after the bonds at a price
above the band, and the critical case is the threshold the design is held to. A plant designed to mid has no margin;
this document does not offer one.

**No further public money after the build.** The bill carries debt service and O&M; the treasury carries nothing
once the plant runs at capacity. That holds if the plant delivers its modelled output, if the HOURS rows of §I hold
(a mid-life replacement of a major component is new capital, not O&M), and if Title II stands on its own rate (§O).

| per year, Title I | mid | critical |
|---|---|---|
| debt service, 30-year bonds at 3.85 %, $M | 1,855 | 3,148 |
| O&M, register plant, $M | 434 | 555 |
| O&M the closing plant adds on the adopted route (§H), $M | 136 | 235 |
| share of the register plant's bill that is the bonds | 81% | 85% |

**The security behind the rate (F-19).** The 3.85 % is a general-obligation or contracted-revenue rate; the security is
contracted in-state offtake at the required price with a state GO backstop for the first-of-kind rungs. Priced to each
security, with the register:

| security | rate | mid, $/MWh ($/household) | critical, $/MWh ($/household) |
|---|---|---|---|
| GO-backed, state general obligation | 3.85 % | 126 (763) | 205 (1,234) |
| revenue bond, contracted in-state offtake | 5.00 % | 141 (853) | 230 (1,387) |
| unrated first-of-kind | 6.50 % | 162 (979) | 265 (1,600) |

**The mechanism behind the tariff (F-10).** v0.1's $0.00/kWh is replaced by the household bill above, an output of the
balance: the Authority registered as a load-serving entity in the community-choice form (PUC section 366.2), IOU delivery, generation sold at cost recovery. A free tariff is a subsidy paid by someone, and this program names no one to pay it.

**Contingency, reserve and the downside (F-29, F-30).**

| | mid | critical |
|---|---|---|
| contingency carried on direct cost | 15% | 30% |
| EPC and owner's cost | 13% | 15% |
| debt-service reserve, 1 year, $M | 1,855 | 3,148 |
| price at 1.25× coverage (a revenue bond's requirement), $/MWh | 152 | 248 |

The downside case is the critical column, by the author's standing rule.

**The schedule (F-24).** Tranche zero is the studies and surveys, from the first study year to the field start; the
field rung waits on the longest gating study; each later tranche follows a rung passed at its critical figure. Direct
cost by rung, with each case's own years:

| rung | mid: years, $B | critical: years, $B |
|---|---|---|
| studies and surveys (gating) | 2027–2029, 0.13 | 2027–2031, 0.29 |
| field, towers and PV at the first node | 2029–2031, 3.02 | 2031–2033, 4.68 |
| pilot aperture on one tower | 2031–2033, 0.16 | 2033–2035, 0.25 |
| first 100 MWe module | 2033–2036, 0.63 | 2035–2038, 0.95 |
| fleet, by tower group | 2036–2041, 12.67 | 2038–2043, 18.84 |

| milestone | mid | critical |
|---|---|---|
| studies and surveys begin | 2027 | 2027 |
| field, towers and PV at the first node complete: first electricity, from PV | 2031 | 2033 |
| pilot aperture on sun, graded | 2031–2033 | 2033–2035 |
| first 100 MWe Helios-3 module dispatching | 2036 | 2038 |
| fleet complete, the whole load served | 2041 | 2043 |

The realistic column is the critical one. The two-year slide comes from one item, the 4-year NEPA environmental
impact statement on the Mojave node, which is why the studies go first.

**Transmission (F-09).** The export is negative, so no firm export right is needed. The in-state gen-tie per node at the
adopted sizing peaks at 1,197 MW (mid) / 1,197 MW (critical) from the hour-by-hour — the same at both cases because the block is the
same size at both and sets the peak — 0.60 / 0.80 of one 500 kV circuit (rated 2,000 / 1,500 MW), priced in the design's
switchyard line at $771 / 1,157 M (§F). The interconnection study is the Authority's to file and no
authority shortens it.

![Figure 9](figures/fig-08-price.png)

*Figure 9. Title I's required price step by step, both cases, against the contract band and today's generation charge.*

![Figure 10](figures/fig-09-household.png)

*Figure 10. A household's annual generation charge: today, during the bond term on the adopted route, and after the bonds retire.*

![Figure 11](figures/fig-11-schedule.png)

*Figure 11. The schedule by tranche at mid and critical; tranche zero is the studies and surveys.*

## N. Title II: the water

**The module.** A 50,000 acre-foot-a-year seawater reverse-osmosis module on a retired coastal power-plant brownfield,
reusing its intake channel and permitted outfall, state-owned on Title I's form. The unit capital is the built record
escalated to the groundbreaking dollar — Carlsbad at $27,011 per AFY (mid) and Huntington Beach as designed at
$36,534 (critical) — against the $5,000–6,400 v0.1 submitted.

| | mid | critical |
|---|---|---|
| overnight, $M | 1,391 | 1,881 |
| of which site studies and surveys per module (§L), $M | 4.3 | 17.8 |
| financed (contingency, EPC, interest during construction), $M | 1,889 | 2,910 |
| against v0.1's $250–320 M | 6.6× | 10.2× |
| electricity, kWh/m³, bought from Title I at its register price | 3.0 at $126/MWh | 3.6 at $205/MWh |

**The water**, at cost recovery — debt service, energy and operations, no mineral revenue:

| | mid | critical |
|---|---|---|
| debt service / energy / non-energy O&M, $M/yr | 107 / 23 / 22 | 165 / 45 / 31 |
| **$ per acre-foot** | **3,044** | **4,830** |
| $ per m³ | 2.47 | 3.92 |
| of which energy | 15% | 19% |
| per household per year at 0.28 AF | 852 | 1,352 |

v0.1 said $400. Carlsbad delivers at $2,700–2,900 and a district pays about $1,300 wholesale today.
Desalinated water is firm water and is priced as such; capital dominates, not energy.

**The process decisions (`titletwo.py`).**

- **Reverse osmosis, not LT-MED (F-13).** A coastal brownfield has no heat source of the 500 MW_th a thermal module
  needs, and none is named; against a condensing cycle on the same heat the water would cost 19.3 / 18.0 kWh/m³ of
  electricity forgone, 6.4× / 5.0× reverse osmosis (`joinder.py`). RO at 3.0–3.6 kWh/m³ is what is priced.
- **No zero-liquid-discharge, no mineral train (F-03, F-04, F-11, F-12).** Seawater holds 0.18 mg/L of lithium: one module's
  feed contains 22.2 tonnes a year, three orders below v0.1's revenue. Its magnesium as hydroxide would be 382 kt a
  year, 0.76 of the US magnesium-compounds market (1.27 at critical) from one module. Crystallising the brine
  costs 20–30 kWh per m³ of brine, omitted from v0.1's energy line. Neither mineral is a revenue and neither is in the price.
- **Brine through the outfall at Ocean Plan concentration.** At 50% recovery the brine is 67 ppt, 33.5 above
  ambient, against a limit of 2 ppt at the 100 m edge — a diffuser dilution of 17 : 1, which a retired plant's
  outfall must achieve without cooling water. Chloride chemistry is excluded everywhere on hazard grounds (the author's
  standing decision), which rules out magnesium metal.
- **Intake (F-28).** screened open intake through the retired plant's channel, 1 mm wedge-wire at <= 0.5 ft/s (the Ocean Plan's alternative to subsurface intake), slant wells where per-site hydrogeology permits. Slant wells are site-specific and were Huntington Beach's failure; entrainment is
  non-zero and mitigated under the Ocean Plan, not eliminated.
- **On-site power covers a tenth, not all (F-27).** A module draws 21–25 MW on average; the 80 / 50 acre site's PV makes
  2.8–1.5 MW, 13%–6% of it. Islanding is a battery for the intake, pretreatment and controls (3.2 MW), so the plant
  rides through an outage without fouling; full-load islanding is not claimed.
- **Energy at the contract price, full-time (F-26).** Title I's surplus is 5% of hours, not half; a membrane plant runs
  steadily. The surplus is the water route's lift, an upside the water price does not count.
- **40 dBA at the boundary is bought, not assumed (F-40).** High-pressure pumps at 90–100 dBA at 1 m reach 40 dBA at
  316–1,000 m in the open; a full enclosure of 28–22 dB brings the boundary to 13–79 m, inside the brownfield, at
  $19–58 M a module, carried in the module's band.
- **Employment (F-38).** At Carlsbad's staffing per plant, the adopted route's modules employ 601–664 permanently.

**The schedule (F-15).** Carlsbad: proposed 1998, coastal permit 2006, water 2015 — 17 years. Huntington Beach:
1998 to a 2022 denial. Stated honestly, permitting 5 years (mid) to 8 (critical, assumed from the record) and a
3-year build put first water at **2034–2037** from a 2026 start, not 24 months. Each year of delay escalates a module by
$57–87 M.

**Title II's side of the adopted route:**

| | mid | critical |
|---|---|---|
| modules at 500 m of head (built as whole modules: 15 / 17) | 15.0 | 16.6 |
| water, million acre-feet a year | 0.75 | 0.83 |
| modules' capital, financed, $B | 28.4 | 48.3 |
| lift on the water's bill, kWh/m³ | 1.51 | 1.60 |
| water with the lift on its bill, $/acre-foot | 3,280 | 5,234 |
| per household per year | 918 | 1,466 |

## O. Title III: the joinder

**The relation (F-31).** One Authority, two projects, two revenue accounts. Title I sells electricity at cost recovery
to in-state load-serving entities and to Title II; Title II sells water at cost recovery to districts. Neither
subsidises the other: each carries its own capital, its own debt service and its own price, and the joinder is two
contracts and one asset. The author's four standing decisions govern it: one program, two projects, severable;
nitrate stays and chloride chemistry is excluded everywhere; Noor III-class heliostats; ZLD dropped and brine returned
through the existing outfall.

**The power-supply agreement.** Title II buys its electricity from Title I at Title I's required price, mid or critical, for the bond term of 30 years:

| | mid | critical |
|---|---|---|
| contract price, $/MWh (Title I with its register) | 126 | 205 |
| volume per module, GWh/yr | 185 | 222 |
| energy's share of the water's cost | 15% | 19% |

**The one shared asset.** Title I's summer surplus lifts Title II's product water to an elevated reservoir, and the
year-round delivery returns through pump-turbines to Title I's evenings. The reservoir and the pump-turbines are Title
I's (they close its load); the modules are Title II's (they make its water); the lift energy is the surplus, priced at
nothing because it was worth nothing.

**The decision table.** §H's three routes, side by side:

| | mirrors, mid | mirrors, critical | water alone, mid | water alone, critical | **both, mid** | **both, critical** |
|---|---|---|---|---|---|---|
| Title I additional capital, $B | 5.7 | 9.5 | no feasible point | no feasible point | **6.4** | **10.3** |
| Title I price, $/MWh | 168 | 272 | — | — | **172** | **279** |
| Title II modules / capital, $B | 0 / 0 | 0 / 0 | — | — | 15 / 28 | 17 / 48 |
| water, million acre-feet a year | 0 | 0 | — | — | 0.75 | 0.83 |
| left to the grid | 0.8% | 1.0% | — | — | 0.6% | 0.7% |

**The takers.** The adopted route delivers 0.75–0.83 million acre-feet a year, year-round: summer irrigation on the Westside
and winter recharge, where the San Joaquin Valley's groundwater overdraft under SGMA is about 1.8–2.5 million acre-feet a
year. That is the match of supply to demand the joinder rests on, and it is a contract question: irrigation and
recharge districts under contract for firm water at three to five thousand dollars an acre-foot, which is what firm
water costs. **The decision is the author's, and it is made: both.**

**The single financial statement:**

| | mid | critical |
|---|---|---|
| Title I capital with its register, $B | 32.7 | 55.4 |
| Title I closing the load, mirrors / both, $B | 5.7 / 6.4 | 9.5 / 10.3 |
| Title II modules at the adopted route, $B | 28 | 48 |
| **program at the adopted route (both), $B** | **67** | **114** |
| Title I debt service, $M/yr | 1,855 | 3,148 |
| Title I debt-service reserve, $M | 1,855 | 3,148 |
| contingency carried | 15% | 30% |
| Title I price at 1.25× coverage, $/MWh | 152 | 248 |

**Severability.**

- **Title I without Title II** stands: the field and store grow to the mirrors route's sizing, the load closes at that
  price, and no water is made.
- **Title II without Title I** stands: a module buys its electricity from the grid instead of the Authority, at the
  grid's price rather than the contract's, and makes the same water; the reservoir and pump-turbines are not built,
  and the water is delivered by the aqueduct.
- **What does not sever** is the water route itself: it exists only as the pair, because its lift is Title I's surplus
  and its evening is Title I's shortfall. It is the joinder, and it is optional.

## P. The sites, each addressed in full

None of the site terms can be computed without a site, and this document does not pretend to. `sites.py` takes the
three Title I nodes v0.1 named and the retired or retiring coastal plants a Title II module could stand on, states
the term each Title needs of a site, grades each site on each term from what is on the public record — MET,
CONDITIONAL (clears on an assumption the site study confirms), OPEN (not knowable here), FAIL — and ranks them.
MET 1, CONDITIONAL 0.5, OPEN 0, FAIL -1. Every site value is ASSUMED from the public record unless an instrument
holds it, and the note beside each grade says which. **The rank orders the site studies; it does not choose a site.**

### P.1. Title I: the three nodes

The terms a node must meet:

| term | requirement | what settles it |
|---|---|---|
| DNI | annual DNI at or above 2500 kWh/m2/yr, else the field grows | one year of on-site DNI (NSRDB then a pyrheliometer) |
| land | a contiguous disturbed parcel covering the node's field | title search and a fallowing agreement |
| nexus | no federal land or federal action, else NEPA on the node | BLM / USACE jurisdiction determination |
| seismic | design PGA over mapped MCE by 1.5x or the tower is re-based | ASCE 7 site-specific hazard study |
| grid | a 500 kV substation within one gen-tie of the node | CAISO interconnection study |
| head | an off-stream reservoir site with 500 m of head within reach | reservoir siting and geotechnical study |

#### Mojave (Kramer Junction)

35.01° N, 117.56° W. Annual DNI **2,799 kWh/m²/yr** (SOURCED: NREL TMY3 Daggett 7.67 kWh/m2/day; band 2,700–2,900). One third of the fleet:
6.0 / 10.3 million m² of mirror at design and 7.6 / 12.9 on the adopted route, 6 / 10 towers on the adopted route,
965 / 1,034 MW_AC of PV; land 15,120 / 22,113 acres on the adopted route; mirror washing 291 / 495 acre-feet a year
from the program's own water; one 500 kV circuit at 1,197 / 1,197 MW peak injection. Seismic: the 0.75 g design target over a mapped
MCE_R PGA of 0.45 / 0.50 g is 1.67× / 1.50× (a site study must confirm 1.5×).

| term | mid | critical | note |
|---|---|---|---|
| DNI | MET | MET | 2799 kWh/m2/yr (SOURCED) |
| land | CONDITIONAL | CONDITIONAL | private and BLM checkerboard; SEGS and Solar Star precedent |
| nexus | CONDITIONAL | CONDITIONAL | BLM parcels in the corridor; DRECP development focus area |
| seismic | MET | MET | 0.75 g over mapped 0.45 g = 1.67x / 0.75 g over mapped 0.50 g = 1.50x |
| grid | MET | MET | Kramer substation on the Kramer-Lugo 230/500 kV corridor |
| head | MET | MET | Tehachapi crest to the west (Edmonston lift 587 m) |

Score 5.0 (mid) / 5.0 (critical). *First study:* land — title search and a fallowing agreement.

#### Imperial (Desert Center)

33.71° N, 115.40° W. Annual DNI **2,740 kWh/m²/yr** (ASSUMED: NSRDB map class 7.3-7.8 kWh/m2/day, mid 7.5; band 2,660–2,850). One third of the fleet:
6.0 / 10.3 million m² of mirror at design and 7.6 / 12.9 on the adopted route, 6 / 10 towers on the adopted route,
965 / 1,034 MW_AC of PV; land 15,120 / 22,113 acres on the adopted route; mirror washing 291 / 495 acre-feet a year
from the program's own water; one 500 kV circuit at 1,197 / 1,197 MW peak injection. Seismic: the 0.75 g design target over a mapped
MCE_R PGA of 0.35 / 0.45 g is 2.14× / 1.67× (a site study must confirm 1.5×).

| term | mid | critical | note |
|---|---|---|---|
| DNI | MET | MET | 2740 kWh/m2/yr (ASSUMED) |
| land | CONDITIONAL | CONDITIONAL | Desert Sunlight / Desert Harvest on BLM; private parcels along I-10 |
| nexus | CONDITIONAL | CONDITIONAL | largely BLM; DRECP DFA |
| seismic | MET | MET | 0.75 g over mapped 0.35 g = 2.14x / 0.75 g over mapped 0.45 g = 1.67x |
| grid | MET | MET | Red Bluff 500 kV substation (built for Desert Sunlight) |
| head | CONDITIONAL | CONDITIONAL | Eagle Mountain pumped-storage site (licensed, unbuilt) nearby; head on a private pit |

Score 4.5 (mid) / 4.5 (critical). *First study:* land — title search and a fallowing agreement.

#### Central Valley (Westside)

36.01° N, 119.96° W. Annual DNI **2,190 kWh/m²/yr** (SOURCED band: Westlands 5.5-6.5 kWh/m2/day, mid 6.0; band 2,010–2,370). One third of the fleet:
6.0 / 10.3 million m² of mirror at design and 7.6 / 12.9 on the adopted route, 6 / 10 towers on the adopted route,
965 / 1,034 MW_AC of PV; land 15,120 / 22,113 acres on the adopted route; mirror washing 291 / 495 acre-feet a year
from the program's own water; one 500 kV circuit at 1,197 / 1,197 MW peak injection. Seismic: the 0.75 g design target over a mapped
MCE_R PGA of 0.40 / 0.55 g is 1.88× / 1.36× (a site study must confirm 1.5×).

| term | mid | critical | note |
|---|---|---|---|
| DNI | CONDITIONAL | CONDITIONAL | 2190 kWh/m2/yr (SOURCED band) |
| land | MET | MET | Westlands drainage-impaired fallowed land, 100,000 acres, private |
| nexus | MET | MET | no federal land; state and county permits (majors.py: first node) |
| seismic | MET | CONDITIONAL | 0.75 g over mapped 0.40 g = 1.88x / 0.75 g over mapped 0.55 g = 1.36x |
| grid | MET | MET | Gates 500 kV substation on the Path 15 corridor |
| head | CONDITIONAL | CONDITIONAL | Coast Range foothills west of I-5; San Luis / Gianelli precedent at ~100 m, 500 m needs a higher bench |

Score 5.0 (mid) / 4.5 (critical). *First study:* DNI — one year of on-site DNI (NSRDB then a pyrheliometer).

**Ranking.** Mid: Central Valley 5.0, Mojave 5.0, Imperial 4.5. Critical: Mojave 5.0, Central Valley 4.5, Imperial 4.5.
At mid the Westside ties the Mojave for first: it meets land, nexus and grid outright and is conditional on DNI and head,
so the node the record doubted for its sun has the fewest open terms. At critical the Mojave leads alone, because the
Westside's seismic margin falls under the 1.5× a site study must confirm. The Central Valley node's land is the
reason it is kept (F-22): 100,000 / 60,000 acres of fallowed, drainage-impaired Westside farmland cover a node 6.6× / 2.7× over.
Land across the program on the adopted route is 45,361 / 66,339 acres (184 / 268 km²), which v0.1 never stated (F-21).
NEPA on the Mojave node's federal nexus (F-25) is budgeted as 2 / 4 years of escalation on that node, $654 / 2,218 M.

### P.2. Title II: the coastal brownfields

The terms a coastal site must meet:

| term | requirement | what settles it |
|---|---|---|
| outfall | a permitted ocean outfall the brine can use at Ocean Plan dilution | outfall diffuser hydraulic study (titletwo.py 17:1) |
| intake | an intake channel a screened open intake can reuse | entrainment study under the Ocean Plan |
| acreage | 50-80 acres of brownfield for a module and its enclosure | site survey and remediation scope |
| takers | an overdrafted basin or an aqueduct within reach for the winter delivery | recharge district contract |
| head | an elevated reservoir site with 500 m of head within reach | reservoir siting study |
| permit | a Coastal Commission record that does not foreclose the site | Coastal Development Permit pre-application |
| hazard | outside the tsunami inundation zone or hardened; seismic basis stated | ASCE 7 and CGS tsunami mapping |

#### Mandalay (Oxnard)

| term | grade | note |
|---|---|---|
| outfall | MET | retired 2018; outfall via the Edison canal |
| intake | MET | canal intake |
| acreage | MET | retired footprint |
| takers | MET | Oxnard Plain / Fox Canyon |
| head | MET | as Ormond Beach |
| permit | CONDITIONAL | as Ormond Beach |
| hazard | CONDITIONAL | dune-backed; inundation zone |

Score 6.0. *First study:* permit — Coastal Development Permit pre-application.

#### Ormond Beach (Oxnard)

| term | grade | note |
|---|---|---|
| outfall | MET | OTC outfall, plant retiring |
| intake | MET | beach intake |
| acreage | MET | retiring OTC plant footprint |
| takers | MET | Oxnard Plain and Fox Canyon, overdrafted, seawater intrusion |
| head | MET | Santa Monica Mountains and Topatopa foothills |
| permit | CONDITIONAL | wetland restoration adjacent; environmental-justice record |
| hazard | CONDITIONAL | inundation zone; liquefaction |

Score 6.0. *First study:* permit — Coastal Development Permit pre-application.

#### Morro Bay

| term | grade | note |
|---|---|---|
| outfall | MET | retired plant outfall into Estero Bay |
| intake | MET | harbour intake |
| acreage | MET | retired 2014; battery project on part |
| takers | CONDITIONAL | no large overdrafted basin; Coastal Branch aqueduct connection |
| head | MET | Santa Lucia range immediately inland |
| permit | CONDITIONAL | sanctuary-adjacent; local opposition record |
| hazard | CONDITIONAL | inundation zone at the harbour |

Score 5.5. *First study:* takers — recharge district contract.

#### Moss Landing (Monterey)

| term | grade | note |
|---|---|---|
| outfall | MET | OTC outfall of the retired units into Monterey Bay |
| intake | MET | harbour intake channel |
| acreage | MET | large retired footprint; Vistra battery on part |
| takers | MET | Salinas Valley 180/400-ft aquifer, critically overdrafted under SGMA |
| head | CONDITIONAL | Gabilan / Santa Lucia ranges within 30 km; bench at 500 m unsurveyed |
| permit | CONDITIONAL | inside the Monterey Bay National Marine Sanctuary; the Cal Am / MPWSP record is a caution |
| hazard | CONDITIONAL | low-lying harbour, inundation zone; 1989 Loma Prieta record |

Score 5.5. *First study:* head — reservoir siting study.

#### Alamitos / Long Beach

| term | grade | note |
|---|---|---|
| outfall | MET | OTC outfall into San Pedro Bay |
| intake | MET | channel intake |
| acreage | CONDITIONAL | repowered with gas units in 2020; footprint shared |
| takers | MET | Central and West Coast basins (WRD recharge) |
| head | CONDITIONAL | San Gabriel foothills 40 km |
| permit | CONDITIONAL | industrial harbour; port air district |
| hazard | CONDITIONAL | inundation zone; Newport-Inglewood fault |

Score 5.0. *First study:* acreage — site survey and remediation scope.

#### Scattergood / El Segundo

| term | grade | note |
|---|---|---|
| outfall | MET | OTC outfalls into Santa Monica Bay |
| intake | MET | ocean intakes |
| acreage | CONDITIONAL | LADWP repowering on site; El Segundo repowered |
| takers | MET | West Coast basin; West Basin's existing recycled-water plant next door |
| head | CONDITIONAL | Santa Monica Mountains 20 km |
| permit | CONDITIONAL | West Basin's own ocean desalination EIR was withdrawn in 2022 |
| hazard | CONDITIONAL | dune-backed; inundation zone |

Score 5.0. *First study:* acreage — site survey and remediation scope.

#### South Bay (Chula Vista)

| term | grade | note |
|---|---|---|
| outfall | CONDITIONAL | plant demolished 2013; outfall into south San Diego Bay, a refuge |
| intake | CONDITIONAL | bay intake, not ocean |
| acreage | MET | cleared bayfront parcel |
| takers | MET | San Diego County Water Authority system |
| head | MET | Otay and Jamul mountains; San Vicente pumped-storage precedent |
| permit | CONDITIONAL | bayfront master plan; refuge adjacency |
| hazard | CONDITIONAL | bay margin; Rose Canyon fault |

Score 5.0. *First study:* outfall — outfall diffuser hydraulic study (titletwo.py 17:1).

#### Huntington Beach (AES)

| term | grade | note |
|---|---|---|
| outfall | MET | OTC outfall, the Poseidon site |
| intake | MET | the Poseidon intake |
| acreage | MET | the Poseidon footprint |
| takers | MET | Orange County basin (OCWD recharge) |
| head | CONDITIONAL | Santa Ana Mountains 40 km inland |
| permit | FAIL | Coastal Commission denied a desalination plant on this site in 2022 (titletwo.py schedule) |
| hazard | CONDITIONAL | inundation zone; Newport-Inglewood fault |

Score 4.0. *First study:* permit — Coastal Development Permit pre-application.

**Excluded: Encina (Carlsbad).** already hosts the 56,000 AFY Carlsbad plant; the record aquacost.py prices from, not a site.

**Ranking.** Mandalay 6.0, Ormond Beach 6.0, Morro Bay 5.5, Moss Landing 5.5, Alamitos / Long Beach 5.0, Scattergood / El Segundo 5.0, South Bay 5.0, Huntington Beach 4.0. The Oxnard plain
(Ormond Beach, Mandalay) and Moss Landing meet the taker and head terms the water route needs; Huntington Beach
carries its 2022 denial as a FAIL and is not a first site; no coastal site is MET on every term, so a site study is
always owed. The adopted route needs 15–17 modules and this list holds 8 sites: 3–5 modules a site, or sites this
list does not name. That is a finding, not a plan.

![Figure 12](figures/fig-12-sites.png)

*Figure 12. The sites scored: the three Title I nodes on six terms at both cases, and the eight coastal brownfields on seven terms.*

## Q. Environment, employment, land and procurement

**CO₂ avoided (F-34).** From the hour-by-hour at a CAISO marginal factor of 0.40 / 0.35 t/MWh (the critical case
credits less, because a cleaner grid displaces less):

| | mid | critical |
|---|---|---|
| served as sized, TWh | 15.83 | 15.74 |
| avoided as sized, million t/yr | 6.33 | 5.51 |
| avoided with the load closed, million t/yr | 7.24 | 6.34 |

v0.1 said 11.8 million tonnes, descended from the inflated energy.

**Employment (F-38).** From built plants per MW — Crescent Dunes and Ivanpah for the permanent staff, Ivanpah's peak for
construction — at the adopted route's block of 3,930 MWe and its 15 / 17 water modules:

| | mid | critical |
|---|---|---|
| permanent, Title I | 1,901 | 1,214 |
| construction peak, Title I | 21,054 | 21,054 |
| permanent, Title II's modules | 601 | 664 |

v0.1 said 22,500 construction and 1,350 permanent; the multiplier it quoted is unsourced and is not carried.

**Resource adequacy (F-18).** No RA is earned on exported energy and the export is negative; the in-state RA is the closed
block's net capacity on the adopted route, 3,616 / 3,537 MW, self-supplied by the Authority as load-serving entity. v0.1 counted $450–480 M a year of it.

**Water for the mirrors (F-20).** At Ivanpah's dry-cooled record (100 acre-feet a year on 2.6 million m²) the program's
field on the adopted route needs 872 / 1,486 acre-feet a year, from Title II desalinated water.

**Seismic (F-33).** Seismic zones left the code in 2001; the basis is ASCE 7, site class and mapped MCE_R. The 0.75 g target
is kept and clears the mapped PGA at every node (§P.1); the mapped values are assumed from the hazard record and the
site study fixes them.

**Nitrate (F-23).** No nitrate salt anywhere in Helios-3: the medium is sintered bauxite, with no freezing point, no
decomposition ceiling, no oxidiser and no toxic medium (R-13 to R-15). The nitrate register applies only to the salt-block
fallback, whose failure mode — the hot-salt tank leak that took Crescent Dunes and Noor III each offline for more than
a year — is on the record in §J.1.

**Procurement (F-39).** One EPC per node under an owner's engineer across the program; the pilot aperture and the first
module let as separate contracts. No contractor has delivered more than one commercial tower at a time in the US, and
the ladder buys the hours before the fleet.

**The Authority (F-37).** A statutory public entity created by the Act on the pattern of the California Consumer Power
and Conservation Financing Authority (SB 6X, 2001; defunded by 2004, a history the Act acknowledges), registered as the
load-serving entity of §M in the community-choice form. Government Code §8571 is cited only for what it does: suspend
regulatory statutes in a declared emergency. It issues no coastal permit and shortens no federal review.

**Dry cooling.** Zero water for heat rejection; sCO₂ needs about a sixth of steam's cooling airflow (R-16), at a
compressor-inlet penalty at 45 °C the critical cycle band carries.

## R. What is not settled, and what could stop it

- **No plant of this kind has run.** The largest falling-particle receiver is 2 MW_th; the 715 °C recompression cycle
  has not run. The pilot aperture (§K) and the ladder (§J) buy the hours before the fleet, and the salt block on the
  same field is the recorded fallback at a price this document prints.
- **The plant must deliver its modelled output.** Every dollar of the bill is per MWh; a plant at Crescent Dunes' 0.39
  of design does not pay its bonds from the bill. The critical column is the defence, and the mid column is margin.
- **The load and DNI shapes are reconstructed**, pinned to sourced levels; `profiles.py` ingests the measured series
  when reachable, and the evening block factor may move either way.
- **The coastal permits are the longest studies on the path** and set the critical schedule; a statutory consolidation
  shortens litigation, not the Coastal Commission.
- **The head is the site question that sizes Title II**; the reservoir's days of holding move Title I by under a billion.
- **The takers** are a contract question: irrigation and recharge districts under contract for firm water, year-round.
- **The split of the shortfall** between the two routes is adopted even and is movable on the ladder.
- **At the critical case a household pays more than today for one bond term**, and the document says so on every page.
- **The HOURS rows of the register** — receiver, exchanger, turbine, chemistry, scale, provenance — retire only by
  operating time; a specification cannot make a machine have run.
- **The brine as a carbonate sink** for the power block's maintenance vents is noted and not priced.

## S. The flaws register: forty found, forty resolved

`FLAWS.tsv` is the adversarial review of v0.1, graded FATAL, CRITICAL, MAJOR, MINOR, worked one at a time in register
order, each by an instrument where numerical. Every row, with its resolution **as recorded when it was closed**: a
resolution quotes the figure the instrument gave that day, and where a later pass moved a figure (the load-shape
correction, the studies line, the adopted route, the O&M on the closing plant) the current figure is the one in
§A–Q and the move is recorded in `docs/`. A status is never flattened, so the record stands beside the result.

**F-01 (FATAL, I §4.2). Export sold at a 100 % capacity factor.**

- *As written:* Annual Export Volume = 1,515 MW × 8,760 h = 13,271,400 MWh/yr
- *Why it fails:* A CSP plant with SM 2.1 and 16 h storage runs at a ~55 % net capacity factor, not 100 %. From the document's own field (45.6 M m², Mojave DNI ~2,750 kWh/m²/yr, 52 % annual field efficiency, 43 % cycle) the network makes ~65 TWh_th → ~28 TWh gross → ~22 TWh net of the stated 735 MW parasitic. The program sells 3,000 MW + 1,515 MW continuous = 39.6 TWh. Delivery is short of promise by ~45 %; the export line alone is overstated by 1.8× on volume before price is considered.
- *What settles it:* An hourly dispatch model over a TMY year for each node, with the sale sized to what the model delivers; sold energy may not exceed modelled net generation.
- *RESOLVED:* tools/helios.py (docs/HELIOS.md). Hourly model of the plant as specified: 19.2 TWh net (CF 0.486) against 39.6 TWh sold; -7.0 TWh after the in-state promise. The export is not overstated, it is negative.

**F-02 (FATAL, I §4.2). Peak price applied to every hour.**

- *As written:* Realized Evening Peak Price $190–350/MWh × 13,271,400 MWh
- *Why it fails:* Evening-peak pricing exists for roughly 1,500–2,000 h/yr; the other 6,800 h clear at $20–60/MWh, and midday often below zero. A 16 h store discharges through the peak and then through the off-peak. Even granting the volume, the price line is overstated ~4.8× on hours alone; compounded with F-01 the export revenue is overstated 5–9×. Every 'Net Cost Coverage' figure (153.7–265.1 %) and every 'Net Surplus to Treasury' figure descends from this line.
- *What settles it:* The same hourly model priced against a CAISO/WEIM historical price shape, with a stated share of energy dispatched into the peak window and the remainder at off-peak.
- *RESOLVED:* tools/helios.py. All net energy priced at the 2024 CAISO shape earns $693 M against $1,933 M carrying; peak-first dispatch puts 33 % of energy in the 4 h window; only the $350 case clears carrying, at 2.4x any 2024 monthly HE20 average. Inverted (helios.required_price): the plant needs $102/MWh at Title I's own capex -- inside the $80-120 firm-clean band -- so self-funding is a contract question at the stated cost, and F-05 decides it.

**F-03 (FATAL, II §2, §4, §5). Lithium revenue is three orders of magnitude too small.**

- *As written:* Battery-Grade Lithium (LiOH) as a revenue stream that 'fully offsets operational and capital amortization expenses'
- *Why it fails:* Seawater holds 0.18 mg/L Li. A 50,000 AFY module processes 61.7 M m³/yr and therefore contains ~11 t of lithium per year ≈ 67 t LiOH·H₂O ≈ $0.8 M/yr, against a $250–320 M facility and ~$50 M/yr operating cost. No one has extracted lithium from raw seawater economically; brine sources are ~1,000× more concentrated. The self-funding claim rests on this line and this line cannot carry it.
- *What settles it:* Delete the lithium line. The mineral case must be made on magnesium and gypsum alone (see F-11).
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): lithium is 22 t per module-year at 0.18 mg/L on the feed; deleted as a line. No mineral revenue is in the water's price (aquacost.py).

**F-04 (FATAL, II §3, §4). ZLD energy omitted from the cost model.**

- *As written:* Reject brine … transformed 100 % into pure water and dry solid minerals; Energy line $0.35/m³; total $0.85/m³
- *Why it fails:* Thermal/mechanical vapour-compression crystallisation costs 20–30 kWh per m³ of brine; at ~50 % recovery the brine volume equals the product volume, so ZLD adds ~25 kWh/m³ of product — ~176 MW continuous per module, ten times the electricity the desalination itself uses. At $0.05/kWh that is ~$1.25/m³ for ZLD alone, 3.6× the entire energy line and 1.5× the stated total operating cost. The cost model as written is off by more than 2× in total.
- *What settles it:* Either delete ZLD (return brine through the existing outfall at Ocean Plan concentration — the author's 2026-09-11 direction) or carry its full energy and capital.
- *RESOLVED:* RESOLVED 2026-09-11: ZLD dropped by the author's direction (F-12); brine returns through the retired plant's permitted outfall; no ZLD energy or capital is carried.

**F-05 (CRITICAL, I §4.1). Title I CapEx at best-in-world CSP price.**

- *As written:* Total Turnkey EPC & Switchyard CapEx: $27.2 Billion ('Audited Baseline')
- *Why it fails:* $27.2 B ÷ 5.25 GW = $5.18/W. Built tower-CSP: Crescent Dunes $9/W, Cerro Dominador $12.7/W, Noor III ~$6/W; DEWA Noor 1 (hybrid, one-off) ~$4.6/W. A 16 h store and 45.6 M m² field are at the upper end of field-per-MW. Realistic band $8–12/W → $42–63 B. Debt service at $60 B and 3.85 % is $3.4 B/yr, not $1.5 B; at a realistic revenue-bond rate of 5.5 % it is $4.1 B. 'Audited' is asserted; no audit is cited.
- *What settles it:* A bottom-up cost build: heliostats ($/m²), receivers, towers, salt, tanks, power block, ACC, switchyards, owner's cost, contingency, IDC — each with a sourced unit rate.
- *RESOLVED:* tools/heliocost.py (docs/HELIOCOST.md). Bottom-up build at the decided class, state-owned, 2028-2030 groundbreaking: $46.1 / 57.0 / 71.5 B net of the federal storage credit (low/mid/high), $8.79-13.62/W, against $27.2 B stated -- 1.70x below the low case. Required price $171 / 206 / 253 per MWh against a firm-clean band of $80-120: the criterion does not close at the scale proposed in any case. Level calibrated to NREL ATB 2024 ($7,912/kWe, SOURCED); split RECONSTRUCTED from SAM/Turchi 2019 and corroborated at 0.778 raw.

**F-06 (CRITICAL, I §2, §2.1). Solar Multiple 5.0 does not match the stated aperture.**

- *As written:* Micro-Heliostat Aperture: 45.6M m² Total (Solar Multiple = 5.0); Guaranteed 16-hr storage charge during winter DNI minimums
- *Why it fails:* The turbine needs 12,209 MW_th at nameplate. 45.6 M m² at 950 W/m² design DNI and 60 % design-point efficiency delivers ~26,000 MW_th: SM ≈ 2.1. SM 5.0 needs ~107 M m². SM 2.1 with 16 h storage is a sound, conventional design (Crescent Dunes 2.7/10 h, Cerro Dominador 2.6/17.5 h) but it does not fill 16 h in December, when DNI is ~60 % of summer; expect 8–10 h. Either the label or the guarantee must go.
- *What settles it:* State SM = 2.1, withdraw the winter guarantee, and let the hourly model (F-01) say what December delivers.
- *RESOLVED:* EVIDENCE (helios.py): at 950 W/m2 the stated aperture gives SM 2.06; SM 5.0 needs 111 M m2. RESOLVED 2026-09-11 by replacing the solar multiple with the hour-by-hour (hourly3.py): Helios-3 as chained serves 84 % of the load; the block cannot carry the evening in any month and the store empties Oct-Apr. Closed by block x1.5 with either field x2 + store 2 days (mirrors, +$60/MWh mid, +$100 critical) or 33-35 desalination modules lifting to a 2 km3 reservoir at 500 m (water, Title III, at parity, +1.6-1.8 MAF/yr of water). The winter guarantee is not a label on the field; it is a route, and the route is the author's decision.

**F-07 (CRITICAL, I §2, §2.1). 11.4 million heliostats.**

- *As written:* Dual-axis tracking 2 m × 2 m micro-heliostat arrays; 45.6M m²
- *Why it fails:* 45.6 M m² ÷ 4 m² = 11.4 million dual-axis drives. Ivanpah has 173,500; the world's installed heliostat population is of order one million. No factory, O&M model or field-control system exists within 50× of this count. The industry trend is the opposite — Crescent Dunes 116 m², Noor III 178 m² — because large units are cheapest per m².
- *What settles it:* Author's direction 2026-09-11: Noor III-class units → ~256,000 heliostats, a purpose-built line at ~100 k/yr over 30 months.
- *RESOLVED:* Author's decision 2026-09-11, carried into heliocost.py: Noor III-class 178 m2 units, 256,180 heliostats, priced at $80-127/m2 (SOURCED band).

**F-08 (CRITICAL, I §2.1). Receiver and field per tower are 2.9× the largest ever built.**

- *As written:* 12 Concrete Towers; 4 × 220 m towers per node
- *Why it fails:* 45.6 M m² ÷ 12 = 3.8 M m² and ~2,170 MW_th per receiver, against Noor III's ~1.3 M m² and ~750 MW_th. A field that size puts its far edge ~2.5 km from the tower, where atmospheric attenuation and spillage degrade optics. No receiver of this size has been designed, let alone operated.
- *What settles it:* Author's direction 2026-09-11: 36 towers of Noor III class (12 per node), same aperture, same salt, same turbines.
- *RESOLVED:* Author's decision 2026-09-11, carried into heliocost.py: 36 towers of 250 m, 1,700 m2 receivers at 722 MW_th each -- Noor III scale, priced per SAM's tower and receiver relations.

**F-09 (CRITICAL, I §3). No firm transmission exists for 1,515 MW of export.**

- *As written:* Export via existing 500 kV corridors: Path 26, Path 15, Pacific DC Intertie, Devers–Colorado River
- *Why it fails:* Path 15, Path 26 and the PDCI are fully subscribed; the document names no transmission rights, no interconnection queue position and no upgrade. CAISO's interconnection queue runs 5–7 years, and 5,250 MW across three 500 kV switchyards needs bay capacity that Lugo, Devers and Gates may not have. Without firm rights the export is curtailable, and curtailable export cannot back a revenue bond.
- *What settles it:* An interconnection study (or the CAISO cluster application) per node; firm transmission rights or a named upgrade; and the export re-sized to what rights exist.
- *RESOLVED:* RESOLVED 2026-09-11 (titleone.py): the export is negative (F-01), so the export need is zero. In-state gen-tie per node at the closed sizing peaks at 1,196 MW (mid) / 1,179 MW (critical), 0.60 / 0.79 of one 500 kV circuit, priced in heliocost's switchyard line ($600 / $900 M). The interconnection study is the Authority's to file.

**F-10 (CRITICAL, I §1, §5, §8). The $0.00/kWh tariff is not the Authority's to give.**

- *As written:* 3,000,000 households transition to $0.00/kWh generation supply tariffs
- *Why it fails:* Retail generation charges are set in IOU tariffs under CPUC. To zero them the CPA must become the load-serving entity for 3 M households (a ~10 GW-peak LSE, larger than SDG&E) or the Legislature must compel IOUs to pass through free power — either is a restructuring of the retail market. The document proposes neither. Selling scarcity-priced power out of state while giving in-state ratepayers $0 generation is also a dormant-Commerce-Clause exposure. (What does hold: a state instrumentality is exempt from FERC rate regulation under FPA §201(f), like LADWP and SMUD.)
- *What settles it:* Decide the retail mechanism: CPA as LSE (CCA-style, with IOU delivery), a statutory pass-through, or a bill credit; and price the export non-discriminatorily.
- *RESOLVED:* RESOLVED 2026-09-11 (titleone.py): the tariff is an output -- the household bill at cost recovery, $756 (mid) / $1,218 (critical) with the register against $1,177 today. Mechanism: the Authority registered as a load-serving entity in the community-choice form (PUC section 366.2), IOU delivery, generation sold at cost recovery. A free tariff is a subsidy someone pays and the program names no one.

**F-11 (CRITICAL, II §2, §4, §5). Magnesium is the only real mineral, and it is market-limited.**

- *As written:* High-Purity Magnesium … mineral sales cover 100 % of facility operational and capital costs
- *Why it fails:* Seawater Mg is 1,290 mg/L → ~79,600 t Mg/yr per module, which is real. As Mg(OH)₂ (~191,000 t/yr at ~$500/t) that is ~$95 M/yr — but one module is a few percent of the world Mg(OH)₂/MgO market and ten modules set the price. As magnesium metal the route is MgCl₂ electrolysis, evolving chlorine gas at ~38 MWh/t — 3 TWh/yr per module, more than the plant's whole energy budget, and the one genuinely toxic process in the document (author's chloride rule, 2026-09-11). Precipitating Mg(OH)₂ needs ~243,000 t/yr of lime, i.e. a kiln and ~144,000 t/yr of CO₂ per module, which is not 'zero impact'.
- *What settles it:* Carry Mg(OH)₂ as a slipstream product at a stated market share and a stated lime source; drop magnesium metal; delete 'battery-grade'.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): one module's magnesium is 382 kt/yr of Mg(OH)2, 0.76 / 1.27 of the US magnesium-compounds market (mid / critical); the brine carries the feed's Mg, twice F-11's product-based figure. A one-module slipstream is possible; it is not a program revenue and is not in the price.

**F-12 (CRITICAL, II §3, §5). Salt disposal at 127 truckloads a day per module.**

- *As written:* Industrial Salts (NaCl) as a revenue stream
- *Why it fails:* 61.7 M m³/yr × 27 g/L NaCl = 1.67 Mt/yr per module, 127 truckloads of 36 t every day. Bulk solar salt sells for $30–60/t (~$67 M/yr gross before haulage), California uses almost no road salt, and a handful of modules exceeds total US salt production (42 Mt/yr). The salt is a disposal cost, not a revenue line.
- *What settles it:* Author's direction 2026-09-11: drop ZLD, return brine through the retired plant's existing permitted outfall at Ocean Plan concentration (≤2 ppt above ambient at the mixing-zone edge). Resolves F-04 and F-12 together.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): brine at 50 % recovery is 67 ppt; the Ocean Plan's 2 ppt at the 100 m edge needs a diffuser dilution of 17:1 with no cooling water, a design requirement on the outfall retrofit priced in aquacost's outfall share.

**F-13 (CRITICAL, II §2). LT-MED has no heat source on a coastal brownfield.**

- *As written:* LT-MED … runs on low-grade thermal energy; on-site solar and steam-topping turbine array
- *Why it fails:* LT-MED needs ~70 kWh_th/m³ → ~490 MW_th continuous per module. A retired coastal plant has no such source; coastal DNI is ~30 % below the Mojave and fogged, and 'solar-thermal skids' on a ~50-acre brownfield deliver of order 10 MW. Making the heat from electricity via heat pump costs 17–23 kWh_e/m³; seawater RO does the same job at 3.2–3.6 kWh_e/m³. Thermal desalination is correct beside a thermal plant (the Gulf model; Diablo Canyon is California's one candidate) and RO is correct everywhere else.
- *What settles it:* Decide RO as the default process; keep LT-MED only where a named heat source of ≥500 MW_th per module exists.
- *RESOLVED:* RESOLVED 2026-09-11: seawater RO is the default process and is what aquacost.py prices; LT-MED only beside a named heat source of >= 500 MW_th per module, and none is named.

**F-14 (CRITICAL, II §4). $400 per acre-foot.**

- *As written:* wholesale water … under $400 per acre-foot
- *Why it fails:* $400/AF is $0.32/m³. The document's own operating cost is $0.85/m³ = $1,048/AF before capital. Carlsbad, the best comparable, delivers at ~$2,700–2,900/AF. The $400 depends entirely on the mineral offset (F-03, F-11, F-12).
- *What settles it:* Price water from the corrected cost build with energy at the Title I contract price; state the resulting $/AF.
- *RESOLVED:* RESOLVED 2026-09-11 (aquacost.py): at cost recovery with the energy at Title I's register price, water is $3,034/AF at mid and $4,790/AF at critical (no mineral revenue), 7.6x / 12.0x the $400 claimed; Carlsbad delivers $2,700-2,900. Energy is 15% of it; capital dominates.

**F-15 (CRITICAL, II §4). 24 months to first water against the Coastal Act.**

- *As written:* under 24 months from breaking ground to first water delivery … under state sovereign drought-emergency authority
- *Why it fails:* Carlsbad took 14 years from proposal to water; Huntington Beach was denied after 22. The binding constraint is not construction but the Coastal Commission CDP, the State Lands Commission lease, the Regional Board's Ocean Plan desalination amendment and CEQA. Gov. Code §8571 lets the Governor suspend statutes in a declared emergency, but it has never been used to site a permanent coastal industrial facility, would be enjoined immediately, and expires with the emergency. 'Sovereign authority' is asserted, not defined.
- *What settles it:* Name the legal instrument (a statutory permitting consolidation with fixed clocks, as in AB 900/SB 7), keep the Ocean Plan-compliant design (slant wells, diffuser outfall), and state an honest schedule.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): permitting 5-8 years (assumed from Carlsbad's 17 and Huntington Beach's 24-year denial) plus a 3-year build puts first water at 2034-2037 from 2026; each year of delay escalates a module by $57-87 M.

**F-16 (CRITICAL, II §4, §5). Title II CapEx 3–4× understated, and no capital source.**

- *As written:* CAPEX $250–320 million per 50,000 AFY module; zero municipal bond debt … self-funding from day one
- *Why it fails:* Carlsbad (56,000 AFY, RO, brownfield at Encina) cost ~$1.0 B in 2015 dollars — ~$18,000/AFY against the document's $5,700/AFY — and LT-MED + ZLD + crystallisers + a mineral train is more equipment than RO, not less. Separately: with 'zero bond debt' and 'zero taxpayer burden' the document names no source for the $250–320 M; a revenue allocation of 40/30/20/10 sums to 100 % with no line for debt service.
- *What settles it:* A bottom-up cost build per module and a stated financing structure (CPA revenue bonds under Title I's authority is the obvious one — which is the joinder).
- *RESOLVED:* RESOLVED 2026-09-11 (aquacost.py): unit capital derived from the record, Carlsbad $27,011/AFY (mid) and Huntington Beach $36,534/AFY (critical) in groundbreaking dollars; a module is $1,883 M / $2,886 M financed, 6.6x / 10.1x the $250-320 M submitted. Financing: Title I's form (municipal bonds at 3.85 %, 30 y, no developer margin, PILOT) -- the joinder, F-31.

**F-17 (MAJOR, I §1, §5). Households, consumption and the bill example use three different numbers.**

- *As written:* 3,000,000 households; 3,000 MW in-state; bill comparison at 1,000 kWh/mo
- *Why it fails:* 3,000 MW × 8,760 h = 26.3 TWh = 8,760 kWh per household at 100 % CF. The bill example assumes 12,000 kWh/yr. California's actual residential average is ~6,300 kWh/yr. At the honest ~22 TWh net with zero export, the plant serves ~3.4 M households at the state average, ~1.8 M at the document's 1,000 kWh/mo. The $2,880/yr saving halves at the state average.
- *What settles it:* Fix the household consumption figure at the CEC residential average and recompute households served, savings and the in-state MW from it.
- *RESOLVED:* tools/helios.py --households (F-17 block). Author 2026-09-11: 3 M households is a MINIMUM growing with population, so the size is a requirement, not a lever. At EIA 2024's 503 kWh/month (6,036 kWh/yr, SOURCED) 3 M households need 18.1 TWh; the plant as specified makes 19.2 -> 3.19 M households at zero export, so the size was right and only the export was wrong. Growth at 1-2 %/yr needs 1.3-1.7x the plant over the bond term. Per household at the required price: $613/yr at Title I's capex (-48 % vs today's $1,177 IOU generation charge), $1,033 / 1,244 / 1,528 at heliocost's built cases (-12 % / +6 % / +30 %): at the built cost the sovereign plant charges a household MORE than the IOU does today. No size answers that; only the equipment does.

**F-18 (MAJOR, I §4.2, §9). RA revenue cannot be earned on exported energy.**

- *As written:* CAISO Resource Adequacy (RA) Value $450 M on out-of-state export
- *Why it fails:* Resource Adequacy is a CAISO product sold to CAISO load-serving entities. Energy sold out of state to WEIM or bilateral buyers is not available to CAISO as RA; the same MW cannot be counted twice. Out-of-state capacity contracts exist but are not 'CAISO RA', and their price is not the CAISO RA price.
- *What settles it:* Split: RA on the in-state capacity (which the CPA may self-supply if it is the LSE), a separate capacity product on export if any.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): export is negative so no export RA; in-state RA is the closed block's net capacity, 3,616 / 3,537 MW (mid / critical), self-supplied by the Authority as LSE -- a requirement met, not a revenue line.

**F-19 (MAJOR, I §4.1). Bond rate assumes a credit the structure does not have.**

- *As written:* 30-Year Tax-Exempt Revenue Bonds @ 3.85 % Fixed
- *Why it fails:* 3.85 % is an investment-grade municipal rate on a take-or-pay contracted revenue stream. First-of-kind CSP at 13× the largest built, with merchant export revenue and no offtake contract, is not that credit; comparable project revenue bonds price at 5.5–7 %. A State GO guarantee would restore the rate — and contradict 'self-funding'.
- *What settles it:* State the security: contracted offtake (in-state LSE contract, water contract) or a stated GO backstop, and price the bonds to it.
- *RESOLVED:* RESOLVED 2026-09-11 (titleone.py): security is contracted in-state offtake at the required price with a state GO backstop for the first-of-kind rungs. Priced: GO 3.85 % $125 / $202 per MWh; revenue bond 5.0 % $140 / $227; unrated 6.5 % $161 / $262 (mid / critical).

**F-20 (MAJOR, I §2.1, §6, §9). Mirror-washing water understated ~4×.**

- *As written:* Water Consumption ~405 acre-ft/yr across 3 nodes; sourced via pre-secured non-potable agricultural water rights
- *Why it fails:* Ivanpah (dry-cooled, 2.6 M m²) uses ~100 AFY; scaled by aperture, 45.6 M m² is ~1,750 AFY. Kramer Junction has no agricultural water; the Mojave node's source is unnamed.
- *What settles it:* Scale from a built dry-cooled plant per m² and name the source per node.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): scaled per m2 from Ivanpah (100 AFY on 2.6 M m2): 1,394 / 2,378 AFY on the mirrors route, 697 / 1,189 on the water route; source is the program's own water (Title II desalinated / the water route's delivery).

**F-21 (MAJOR, I §2, §6, §9). Land footprint unstated.**

- *As written:* sites restricted strictly to state-owned or previously disturbed agricultural/industrial buffer lands
- *Why it fails:* At ~20 % ground-cover ratio, 45.6 M m² of mirror is ~230 km² (~56,000 acres), 3.5× Ivanpah, whose 14 km² produced a multi-year desert-tortoise fight. No contiguous state-owned or previously-disturbed parcel of ~75 km² exists in the Mojave; fallowed Westside San Joaquin farmland does, and is a strength the document does not claim.
- *What settles it:* State the footprint per node and name candidate parcels; move share toward the Central Valley node where disturbed land exists (see F-22).
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): 62,160 / 94,980 acres on the mirrors route (20,720 / 31,660 per node), 39,762 / 56,792 on the water route; fallowed Westside San Joaquin land covers a node 4.8x / 1.9x and is claimed; desert nodes are BLM-adjacent (F-25).

**F-22 (MAJOR, I §2, §3). Nodes treated as identical; Central Valley DNI is 15–25 % lower.**

- *As written:* three desert nodes … 1,750 MWe each
- *Why it fails:* Westside San Joaquin DNI is ~6.0–6.5 kWh/m²/day against 7.5–8 in the Mojave and Imperial, with winter tule fog. The Central Valley node's output is 15–25 % below the other two for the same field; it is not a 'desert node'.
- *What settles it:* Per-node TMY in the hourly model; either a larger field there or a smaller nameplate.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py, hourly3.py): the node runs on its own DNI, 0.78 of the Mojave's; moving it to the desert lifts service 0.839 -> 0.856 and does not change the closing sizing; kept at a larger field share for its land.

**F-23 (MAJOR, I §9). Nitrate risk register absent.**

- *As written:* Risk matrix lists supply chain for nitrate salt only
- *Why it fails:* Nitrate is the right medium (author's direction 2026-09-11) but its own hazards are missing: it is an oxidiser (no organics in the salt building), it decomposes above ~600 °C (flux control is a chemistry requirement), it freezes at ~238 °C (heat tracing and drain-down on every line), and the hot tank is the historical failure — Crescent Dunes lost eight months to a hot-tank leak in 2016. 1.665 Mt over 36 months is also of order 40–50 % of world solar-grade nitrate output.
- *What settles it:* Add four rows to §9 with a mitigation each; state the nitrate supply share against sourced world production.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): Helios-3 holds no nitrate -- sintered bauxite medium, helios3 R-13 to R-15 BENEFIT; the four hazards return only with the salt-block fallback, whose hot tank is the record's own failure (Crescent Dunes, Noor III).

**F-24 (MAJOR, I §8). Schedule: 5.25 GW in two construction years.**

- *As written:* Phase 3 (2028–2029) civil, towers, tanks, field; COD Q2 2030
- *Why it fails:* Ivanpah (392 MW) took four construction years; Crescent Dunes (110 MW) four. 5.25 GW in two years is ~13× Ivanpah's build rate across three sites, with a heliostat line, a salt tank programme and 36 receivers that do not yet exist. The 2030 COD is not credible as stated.
- *What settles it:* A resource-loaded schedule per node with a phased COD (first node, first tower group) and the finance sized to the phasing.
- *RESOLVED:* RESOLVED 2026-09-11 (titleone.py): the schedule is R-12's ladder dated from 2028-2030 -- first node's field and pilot aperture 2029-2033, first 100 MWe module 2033-2036, fleet by tower group 2036-2041 -- each bond tranche following a rung passed at critical; tranches $3.02 / 0.07 / 0.63 / 12.68 B at mid on $16.4 B direct.

**F-25 (MAJOR, I §9). Federal nexus defeats the CEQA-only permitting plan.**

- *As written:* statutory CEQA streamlining … capping judicial review windows at 180 days
- *Why it fails:* The Mojave node near Kramer Junction almost certainly touches BLM land or a federally permitted transmission line; any federal nexus triggers NEPA, which no state statute can shorten. The 180-day CEQA cap (AB 900 / SB 7) also requires certification and a $100 M+ threshold, and applies to judicial review only, not to the EIR itself.
- *What settles it:* Site on state or private land with no federal nexus, or budget NEPA; cite the actual statute the cap comes from.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): NEPA is not shortened by state statute; the first node is the one with no federal nexus (Westside); the Mojave node budgets NEPA on the fleet rung, 2 / 4 years, $647 / $2,184 M of escalation.

**F-26 (MAJOR, II §2, §4). '50 % of hours at cheap or negative price' and a thermal plant that cannot cycle.**

- *As written:* plant draws 50 % cheap or negative-price power from the CAISO grid
- *Why it fails:* Negative or near-zero prices occur in ~5–15 % of CAISO hours, concentrated in spring middays. An LT-MED train cannot follow that at 50 % duty without wrecking its thermal economics; an RO train can, which is another argument for F-13.
- *What settles it:* Price energy at the Title I contract, or at an hourly CAISO shape with the plant's actual flexibility.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py, aquacost.py): energy priced at Title I's contract price full-time; Title I's surplus is 589 h/yr (7%), not 50 %, and is the water route's lift, an upside not counted.

**F-27 (MAJOR, II §2). '100 % on-site power capacity' is 10–20× what a brownfield can host.**

- *As written:* dedicated on-site solar and steam-topping turbine array providing 100 % internal power capacity; full-load islanding
- *Why it fails:* A module as written needs ~25 MW_e for LT-MED, ~176 MW_e for ZLD (F-04) and ~490 MW_th of heat. A ~50-acre coastal brownfield hosts of order 10 MW of PV. Islanding a 200 MW load on 10 MW of solar is not a capability.
- *What settles it:* Delete ZLD (F-12), adopt RO (F-13), and state islanding as what on-site generation actually covers.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): a module draws 21-25 MW average; the whole brownfield as PV makes 2.8-1.5 MW, 13%-6%. Islanding is a battery for critical loads (3.2-3.8 MW); full-load islanding withdrawn.

**F-28 (MAJOR, II §2). Slant-well feasibility is site-specific and was the Huntington Beach failure.**

- *As written:* subsurface slant wells … eliminating 100 % of fish and plankton entrainment
- *Why it fails:* Slant wells are what the Ocean Plan prefers, and that is a strength — but their feasibility depends on coastal geology, and at Huntington Beach Poseidon's own studies found them infeasible, which is why the Ocean Plan has a feasibility test. The 'where geology dictates' hedge means the zero-entrainment claim is conditional at every site.
- *What settles it:* Per-site hydrogeology; where wells are infeasible, state the screened-intake alternative and its (non-zero) entrainment.
- *RESOLVED:* RESOLVED 2026-09-11 (titletwo.py): decision -- screened open intake through the retired plant's channel, 1 mm wedge-wire at <= 0.5 ft/s (the Ocean Plan's alternative to subsurface intake), slant wells where per-site hydrogeology permits; entrainment non-zero and mitigated under the Ocean Plan; 'eliminating 100 %' withdrawn.

**F-29 (MAJOR, I §4.2, §9; II §4, §5). No sensitivity or downside case in either Title.**

- *As written:* 'Conservative' scenario is the 100 % CF case; mineral prices stated as fixed
- *Why it fails:* Neither Title has a case in which a load-bearing input comes in worse than assumed. The Title I 'conservative' case is conservative in price only; the Title II model has no sensitivity to mineral prices, energy prices or capex at all. A revenue bond prospectus requires a downside case that still covers debt service.
- *What settles it:* A downside case per Title (CF −15 %, price −30 %, capex +50 %) that states its coverage ratio.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): the downside case is the critical case (standing rule); at 1.25x coverage the price is $151 / $245 per MWh (mid / critical).

**F-30 (MAJOR, I §4, §10; II §5). No contingency, reserve or overrun provision anywhere.**

- *As written:* 100 % of surplus distributed; 'Audited Baseline' capex; revenue split sums to 100 %
- *Why it fails:* First-of-kind CSP has run 30–100 % over budget (Ivanpah, Crescent Dunes). Neither Title carries a construction contingency, a debt-service reserve fund or an overrun mechanism; Title II distributes 100 % of surplus by formula.
- *What settles it:* A contingency line (25–35 % on first-of-kind), a DSRF, and a stated overrun backstop.
- *RESOLVED:* RESOLVED 2026-09-11 (majors.py): contingency 15% / 30% and EPC 13% / 15% carried (heliocost); DSRF one year's debt service, $1,836 / $3,100 M; overrun backstop the state GO (F-19).

**F-31 (MAJOR, III). The joinder does not exist.**

- *As written:* (no text)
- *Why it fails:* The merged document carries no power-supply agreement, no shared balance sheet, no severability clause and no institutional relation between the Authority and the water program. The author's decision (one program, two projects, severable) is stated in chat only.
- *What settles it:* Write Title III once F-01..F-16 are resolved: contract price, volume, term; single financial statement; severability.
- *RESOLVED:* RESOLVED 2026-09-11 (rebase3.py): Title_III_Joinder_v0.2.md -- power-supply agreement at Title I's price for the bond term, the shared asset (reservoir and pump-turbines Title I's, modules Title II's, lift energy the surplus), the decision table (mirrors vs water at both cases), the takers (SGMA recharge), a single financial statement (program $106 B mid at the water route), severability both ways. The decision is the author's.

**F-32 (MINOR, I §2.1). 'Supercritical Rankine' at 565 °C salt.**

- *As written:* Multi-module supercritical Rankine steam cycle
- *Why it fails:* Supercritical steam needs ≥ 600 °C live steam; 565 °C salt gives ~540 °C steam and a subcritical reheat cycle at ~42 %. The efficiency used is right; the label is wrong.
- *What settles it:* Relabel as subcritical reheat.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py cycle_label): Helios-3's cycle is sCO2 recompression Brayton at 715 C, 0.50 (cspchain); the nitrate-salt fallback (Helios-2) is subcritical reheat steam, ~540 C live steam from 565 C salt, 0.43. 'Supercritical Rankine' withdrawn; the efficiencies were right, the label was wrong.

**F-33 (MINOR, I §9). Seismic standard cited does not exist.**

- *As written:* CBC Title 24 Seismic Zone 4; PGA up to 0.75 g
- *Why it fails:* CBC has not used seismic zones since 2001; design is site-specific under ASCE 7. Kramer Junction's mapped PGA is ~0.4–0.5 g. The 0.75 g target is fine; the citation will be caught.
- *What settles it:* Cite ASCE 7 site class and the mapped MCE.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py seismic): seismic zones left the CBC in 2001; design is site-specific under ASCE 7 (site class, mapped MCE_R). The 0.75 g target is kept and lies above the mapped PGA at every node -- Mojave 0.45/0.50 g (target 1.67x/1.50x), Imperial 0.35/0.45 g (2.14x/1.67x), Central Valley 0.40/0.55 g (1.88x/1.36x), mid/critical. Mapped values are ASSUMED from the USGS hazard record; the site study fixes them.

**F-34 (MINOR, I §6). CO₂ figure descends from the inflated energy.**

- *As written:* eliminates 11.8 Million Metric Tons of CO₂ annually
- *Why it fails:* At ~0.4 t/MWh marginal gas, the honest ~22 TWh net avoids ~8.6 MMT; the promised 39.6 TWh would avoid ~15.8. 11.8 sits between and cites neither.
- *What settles it:* Recompute from the hourly model at CAISO marginal emissions.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py co2): recomputed from hourly3.py's served energy at a CAISO marginal factor of 0.40/0.35 t/MWh: 6.08/5.29 MMT a year as sized (15.2/15.1 TWh served), 7.24/6.34 MMT with the load closed (18.1 TWh), mid/critical, against 11.8 claimed. The honest figure is 5.3-7.2.

**F-35 (MINOR, II §2, §3). HPRO in the ZLD train contradicts 'no membranes in the water path'.**

- *As written:* eliminates fragile water-filtration membranes … routed through high-pressure reverse osmosis (HPRO)
- *Why it fails:* Internal contradiction; moot if F-12 is adopted.
- *What settles it:* Resolve with F-12/F-13.
- *RESOLVED:* RESOLVED 2026-09-11: moot -- ZLD and HPRO are gone with F-12.

**F-36 (MINOR, II §2). Spent citric-acid CIP routed into mineral recovery.**

- *As written:* Spent wash solutions route directly into the mineral recovery train
- *Why it fails:* Citrate chelates Ca and Mg and would suppress the Mg(OH)₂ precipitation it is being routed into.
- *What settles it:* Route CIP to neutralisation and the outfall, or to a separate evaporator.
- *RESOLVED:* RESOLVED 2026-09-11: moot -- the mineral train is gone; CIP waste is neutralised and returned with the brine under the NPDES permit.

**F-37 (MINOR, I passim; II §1, §4). 'Sovereign authority' is used as a mechanism and is not one.**

- *As written:* state sovereign authority; sovereign drought-emergency authority
- *Why it fails:* The mechanisms that exist are a statutory authority created by the Legislature (the original California Power Authority, SB 6X 2001, existed and was defunded by 2004 — a history the proposal should acknowledge) and Gov. Code §8571 emergency powers. 'Sovereign' names neither.
- *What settles it:* Define the Authority in the Act; cite §8571 only for what it can do.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py): the Authority is a statutory public entity created by the Act on the pattern of the California Consumer Power and Conservation Financing Authority (SB 6X, 2001, defunded by 2004 -- acknowledged), registered as a load-serving entity in CCA form (F-10). Gov. Code 8571 is cited only for what it does -- suspend regulatory statutes during a declared emergency -- and is not offered as a coastal permit or a NEPA shortcut (F-15, F-25). 'Sovereign' is a description, not a power.

**F-38 (MINOR, I §7). Permanent jobs and construction jobs unsupported.**

- *As written:* 22,500 construction jobs; 1,350 permanent; $4.2 B multiplier
- *Why it fails:* Plausible in magnitude (Crescent Dunes ~45 permanent per 110 MW scales to ~2,100; Ivanpah ~90 per 392 MW to ~1,200) but no basis stated; the multiplier is unsourced.
- *What settles it:* Cite the basis per MW from a built plant.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py jobs): from built plants per MW (Crescent Dunes 0.41, Ivanpah 0.23 permanent per MW; 2,100 / 392 MW construction peak): Title I at the x1.5 block (3,930 MW) 1,901/1,214 permanent, 21,054 construction peak; Title II water route 1,313/1,410 permanent, mid/critical. v0.1's 22,500 and 1,350 were the right order; the $4.2 B multiplier is unsourced and is not carried.

**F-39 (MINOR, I §4.1, §8). Turnkey EPC with no EPC.**

- *As written:* Total Turnkey EPC
- *Why it fails:* No EPC contractor has delivered more than one commercial salt tower at a time in the US; the document names none. 'Turnkey' at 36 towers is a procurement strategy, not a fact.
- *What settles it:* Name the procurement structure (multiple EPCs by node, owner's engineer).
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py): 'turnkey EPC' is replaced by a procurement structure -- one EPC per node under an owner's engineer across the program, with the pilot aperture and the first 100 MWe module let as separate contracts, because no contractor has delivered more than one commercial tower at a time in the US and the ladder (R-12) buys the hours before the fleet.

**F-40 (MINOR, II §3). 40 dBA at the boundary unsupported.**

- *As written:* boundary noise below 40 dBA (quieter than a library)
- *Why it fails:* RO high-pressure pumps and MVC crystallisers are 85–100 dBA at source. 40 dBA at a fence line is achievable with full enclosure and is a cost the document does not carry.
- *What settles it:* State the enclosure and its cost, or the boundary distance.
- *RESOLVED:* RESOLVED 2026-09-11 (minors.py noise): RO high-pressure pumps at 90/100 dBA at 1 m reach 40 dBA at 316/1,000 m open; a full enclosure of 28/22 dB brings the boundary to 13/79 m, inside the brownfield F-27 assumes, at $19/$58 M per module, mid/critical. The cost is carried in the Title II module's price band; 'quieter than a library' is withdrawn as a comparison.

## T. Sources

The published record the instruments cite, as the study register names it (§J), deduplicated; each row of §J carries
its own citation beside the finding it supports.

- Torresol Energy
- Burgaleta et al., SolarPACES 2011
- SolarPACES 'What happened with Crescent Dunes'
- Wikipedia project page (reviewed 2026-09-11)
- DOE Loan Programs Office
- ACWA Power Tadawul statement 2024-03
- pv magazine 2024-03-25
- Hespress 2025 (reviewed 2026-09-11)
- Cerro Dominador
- SolarPACES project database
- DEWA
- ACWA Power
- CSPPLAZA
- NREL HelioCon (2022-)
- NRG/BrightSource
- CEC docket 07-AFC-5
- Ho et al., AIP Conf. Proc. 1734 (2016)
- J. Sol. Energy Eng. 141 (2019)
- OSTI 1364838, 1431441 (reviewed 2026-09-11)
- Sandia LabNews 2024-08-22
- Ho & Schroeder, AIP Conf. Proc. 2445 (2022) (reviewed 2026-09-11)
- Sandia LabNews 2025-02-06
- OSTI 2999325 (cold commissioning)
- DOE Gen3 Phase 3 (reviewed 2026-09-11)
- DLR Institute of Solar Research
- Ebert et al., ASME ES2018
- SolarPACES/HelioHeat (reviewed 2026-09-11)
- CSIRO 2023-10
- SolarPACES (FPR Energy) (reviewed 2026-09-11)
- KSU / Sandia collaboration
- Sandia Gen3 Roadmap / TEA (Ho et al. 2019-2021)
- Buck et al., J. Solar Energy Eng. 2002
- SOLGATE final report 2005
- Ho / Yellowhair, Sandia SAND (Gen3 windowed receiver)
- Siegel et al., J. Sol. Energy Eng. 137 (2015)
- Ho et al., OSTI 1431441
- Sandia 2016 review (reviewed 2026-09-11)
- CARBO Ceramics product data
- Sandia G3P3
- Sandia Gen3 storage design reports
- Siemens Gamesa ETES pilot (2019-2022)
- steel and cement industry practice
- bulk-solids handling practice
- Albrecht & Ho, Sandia (AIP Conf. Proc. 2020; Sandia 2022 performance evaluation)
- Sandia LabNews 2021-06 (reviewed 2026-09-11)
- Ma et al., NREL (2014-2020)
- GTI Energy STEP Demo Phase 1 milestone
- POWER magazine
- ASME GT2025 simple-cycle testing paper (reviewed 2026-09-11)
- Sandia SAND2012-9546 (Wright et al.)
- Echogen Power Systems
- SASAC 2021-12-23
- Energy (2023) startup study (reviewed 2026-09-11)
- EU H2020 SCARABEUS (2019-2023)
- DOE SunShot sCO2 (2012-2018)
- NETL
- ASME BPVC Code Case 2702 (2011)
- DOE/OCDO A-USC (2001-2021)
- EPRI
- ASME BPVC Code Cases Supplement 2 (2021)
- ORNL Pub140621 (reviewed 2026-09-11)
- ASME BPVC III-5 (2019 edition, Alloy 617)
- ORNL, NETL, Sandia coupon programmes
- SolarPACES (Midelt PV-to-storage)
- REN21 GSR 2025
- NS Energy (reviewed 2026-09-11)
- CEC / EIA installed capacity data
- Siemens Gamesa ETES
- Kraftblock
- Malta (design)
- plant records
- Sandia / NREL sCO2 CSP studies
- DEWA / ACWA Power

An entry marked *reviewed 2026-09-11* was checked against the web where this environment's proxy reached; an
encyclopaedia entry in the list is a pointer to a plant's public record and to the primary items beside it, not the
source of a figure. Entries such as *plant records* and *industry practice* name a class of evidence, not a
document, and the row that cites them claims only what such a class can carry.

Further sources carried by the instruments as constants, each marked SOURCED beside its value: EIA 2024 (California
residential consumption and customers); NREL ATB 2024 (tower CSP, the calibration anchor); NREL TMY3 Daggett and the
NSRDB DNI classes; CAISO Department of Market Monitoring 2024 (prices, negative hours); Palo Verde on-peak strip 2024;
SAM / Turchi 2019 (the cost split, RECONSTRUCTED); the DOE Loan Programs Office and SolarPACES on Crescent Dunes; ACWA
Power on Noor III; NREL ATB and Fervo / Cape Station on geothermal; TVA Clinch River and Darlington on SMRs; California
Public Resources Code §25524.2; the Ocean Plan 2015 amendment (brine); Carlsbad and Huntington Beach records (capital,
price, schedule); PPIC on the San Joaquin Valley overdraft; ASCE 7 and the CGS hazard and tsunami maps; SB 6X (2001)
and PUC §366.2 (the Authority's form); Government Code §8571; Ivanpah and Crescent Dunes staffing; the Sites reservoir
record and the Edmonston and Gianelli lifts.

## U. The instruments

Every number in this document is computed by one of these, each with a `--selftest` fixtured on the record, each
stdlib-only (the renderer alone needs matplotlib for the figures and python-docx for the Word files), each importing
what it needs from its neighbours and restating nothing:

- `tools/helios.py` — the plant as submitted, run hour by hour; the criterion inverted; F-17's requirement.
- `tools/heliocost.py` — the capital line by line at the built record, state-owned.
- `tools/firmpower.py` — every firm candidate sized to the requirement.
- `tools/cspchain.py` — the seven-link chain; Helios-2 and Helios-3 designed on it.
- `tools/helios3.py` — the sixteen-row mitigation register, graded and priced.
- `tools/receiver.py` — the falling curtain as a per-metre machine; the critical receiver.
- `tools/studies.py` — the provenance register and the recommendations.
- `tools/hourly3.py` — Helios-3 hour by hour; the mirrors route.
- `tools/profiles.py` — the ingestion path for measured CAISO and NSRDB series.
- `tools/joinder.py` — the water route's hydraulics and its feasibility rule.
- `tools/both.py` — the ladder over the water's share; the adopted point; its sensitivity.
- `tools/pilot.py` — the pilot aperture's acceptance protocol.
- `tools/predev.py` — the studies and surveys, priced first.
- `tools/aquacost.py` — the module and its water.
- `tools/titletwo.py` — Title II's process rows.
- `tools/titleone.py` — the bond rate, the schedule, transmission, the tariff.
- `tools/majors.py` — RA, washing, land, the Central Valley node, NEPA, the reserve, the downside.
- `tools/minors.py` — the cycle label, seismic, CO₂, jobs, the Authority, procurement, noise.
- `tools/sites.py` — the site terms, graded and ranked.
- `tools/rebase.py, rebase2.py, rebase3.py` — the three Titles as documents.
- `tools/proposal.py` — this document and the pitch.

*Rendered by `tools/proposal.py`; do not edit by hand. Re-render after any change to the instruments.*
