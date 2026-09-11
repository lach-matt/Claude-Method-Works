# `tools/studies.py` — provenance for Helios-3, listed rather than asserted

**Why it exists.** `helios3.py` R-12 says no plant of this kind exists at any commercial scale
and grades that MAJOR / HOURS. The author's requirement on it (2026-09-11): *"we must provide a
complete list of all studies that cover any technology being used in this system, and then
provide a recommendation of further study, with a note that delay increases cost of start up
at the rate of inflation."* This file is that list, that recommendation and that note.

**Run it.** `python3 tools/studies.py` for the full register, `--recommend` for the
recommendations and the delay cost only, `--selftest` for the checks. Stdlib only; imports the
priced plant from `helios3.py` and the escalation rate from `heliocost.py`, never restating
either.

## What "complete" means here, exactly

The register is **complete over technologies and a floor over studies**. Twelve technologies
are the ones the design uses — field, receiver, aperture, particles, storage, lift, exchanger,
sCO₂ block, alloys, PV and heaters, dry cooling, the hybrid architecture — and the selftest
asserts every one has at least one study row and exactly one recommendation. The **49 study
rows** were compiled from the published record as known to the session that wrote them, and
**reviewed against the web on 2026-09-11** where the search proxy reached (Sandia, OSTI, ASME,
SolarPACES, GTI, ACWA, DLR, CSIRO, SASAC, ORNL): rows marked *reviewed 2026-09-11* in their
source were checked and corrected in place — Noor III's 2024 outage was the hot-salt tank, not
the receiver; Crescent Dunes has had four hot-tank leaks and runs derated at half its design;
STEP reached 4 MWe in a simple cycle at ~500 °C and the 715 °C recompression phase has not run;
CentRec is 2.5 MW_th, not 0.5; G3P3-USA's 2 MW_th receiver measured 80–90 %; Sandia's curtain
was measured at 0.3–0.7 MW/m² average with 50–200 °C per metre of drop; the particles' absorptance
after 200 h is statistically unchanged, not 0.93; Haynes 282's code case is 3024 of 2021; and
Midelt I, the only plant designed to heat storage from PV, has not started construction. Rows
not so marked stand as compiled. Every row names its source so it can be checked, and a technology may have more
studies than are listed, never fewer. A row found wrong is corrected in place with its source.

Every row carries a status from a closed set: **OPERATED** (a plant that has run at the stated
scale), **TESTED** (a prototype or loop below plant scale), **DESIGNED** (a published design,
TEA or code case), **AUTHOR** (this repository's own design; no study exists). Two structural
checks keep the register honest: no technology may rest on AUTHOR rows alone, and the four
HOURS technologies — receiver, exchanger, sCO₂ block, aperture — have **no OPERATED row at plant
scale**, which is the gap R-12 names.

## The recommendation, by rung of the ladder

Studies are placed on the rungs of R-12's ladder — now → field → pilot aperture → first module
→ fleet — and studies on one rung run in parallel:

| rung | longest study | what is settled there |
|---|---|---|
| now | 0.5 y | Helios-3 hour by hour in `helios.py` at both cases: winter under-supply and heater sizing at critical |
| field | 1.0 y | measured annual optical efficiency against the 0.58–0.64 band; sets the mirror count at critical |
| pilot | 3.0 y | the ~30 MW_th pilot aperture (receiver threshold 0.690, edge loss vs size); the dome against an open aperture on one tower; particle ageing sampled quarterly (R-08); a full-size cold-shell silo cycled daily; the exchanger at 800 °C / 25 MPa; alloy coupons in the real CO₂ loop; a PV-fed particle heater at MW scale |
| module | 3.0 y | STEP's 715 °C phase then one 10–50 MWe unit; compressor inlet at 45 °C, whether a CO₂ blend is needed |

Critical path **7.5 years of study**, run *against* the build rather than before it: the field
is built while the pilot runs, the pilot runs while the module is ordered. Lift needs no further study and the file says so rather than inventing one; PV's heater path
does, because the review found Midelt I unbuilt.

## The cost of delay

`heliocost.py` escalates construction cost at **3 %/yr** (ASSUMED band 2–4 %, a
construction-cost index — the rate of inflation for what this plant is made of). Because the
debt service is proportional to the capex, the required price drifts at exactly the same rate,
and the selftest asserts that. Each year the start is delayed adds, before a dollar is spent:

| | capex net, $B | + per year, $B | $/MWh | + per year | $/household/yr | + per year |
|---|---|---|---|---|---|---|
| mid | 32.3 | 0.97 | 125 | 3.8 | 756 | 23 |
| critical | 54.6 | 1.64 | 202 | 6.1 | 1,218 | 37 |

A study that takes a year and is not run against the build costs that year's escalation on the
whole plant; a study run beside the build costs only itself. That is why the rungs overlap.
The escalation rate is ASSUMED and the delay cost is exactly as uncertain as it is.

## What it does not do

It does not make any of it have run. R-12 stays MAJOR / HOURS in `helios3.py`; what this file
adds is the list the author asked for and the order in which the hours are bought.
