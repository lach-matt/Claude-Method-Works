# helios3.py — Helios-3's risks, mitigated upfront where design can, and named where only hours can

`tools/helios3.py` tests the author's claim on the chosen path — *"Helios-3 is
actually better, and I think each cost can be fully mitigated upfront"* — by
the objective's own rule that mitigations are addressed before design, and
by the method `environment.py` used on the fission plant: a register in which
every risk is graded **before and after** its mitigation, every mitigation is
**carried by a named part of the build** (a mitigation that lives only in a
register is prose), and every row says which **kind** of mitigation it is:

- **DESIGN** — retired upfront, by a specification: what the author means.
- **HOURS** — retired only by operating time on a plant that does not yet
  exist, which no specification can supply.
- **BENEFIT** — a risk the salt plant carried that this one does not.

Then the mitigations are **priced back into Helios-3** (`cspchain.py`'s own
design, imported) so the $117/MWh is tested rather than kept.

    python3 tools/helios3.py
    python3 tools/helios3.py --selftest

## The register

| id | risk | before | after | kind | carrier |
|---|---|---|---|---|---|
| R-01 | particle attrition, dust, medium loss | MODERATE → NEGLIGIBLE | DESIGN | particle geometry (spherical, tight cut) + system geometry (short drops, few transfer points, particle-on-particle landing, mass-flow hoppers, one cold lift); enclosed conveyance; O&M makeup. Adopted by the author 2026-09-11; fixed-bed/air fallback noted |
| R-02 | receiver wind and convective loss | MAJOR | MODERATE | HOURS | receiver spec; aperture element spec (compound quartz aperture: hex low-OH rod-lens dome, adopted 2026-09-11); aperture cooling loop (hollow-web frame manifold at the cold ends, preheat tie-in); tower count |
| R-03 | particle-to-sCO₂ heat exchanger, 800 °C / 250 bar | MAJOR | MODERATE | HOURS | power block; N+1 spares; working-fluid fill (CO₂ stays, blend optional for hot-ambient dry cooling; adopted 2026-09-11) |
| R-04 | sCO₂ turbomachinery at 715 °C | MAJOR | MODERATE | HOURS | 740H hot path; many small units; materials spec: 740H boundary at 110 °C margin, single-crystal rotor, no ceramic in the CO₂ path (adopted 2026-09-11) |
| R-05 | CO₂ inventory release | MODERATE | MINOR | DESIGN | site layout; sensors, dump tanks, per-module inventory (adopted as it stands 2026-09-11; the desalination brine is a carbonate sink for maintenance vents only, tonnes a year against a release of tonnes a minute, and is noted for Title III, not here) |
| R-06 | 250 bar / 715 °C containment | MODERATE | MINOR | DESIGN | 740H under ASME code; alloy ladder 740H / Haynes 282 / Inconel 617 fallback to 950 °C, no single-crystal or ODS in pressure parts (adopted 2026-09-11) |
| R-07 | silo heat loss, ratcheting at 800 °C | MODERATE | MINOR | DESIGN | refractory-lined large silos; cold-shell lining, replaceable inner liner, berm and cold-silo pit; hot silos not buried (adopted 2026-09-11) |
| R-08 | bauxite chemistry in air over decades | MODERATE | MODERATE | HOURS | rejuvenation; silo atmosphere (adopted as it stands 2026-09-11; UNMOVED by agreement, the rate over decades is measured by decades) |
| R-09 | particle lift erosion and temperature | MODERATE | MINOR | DESIGN | lift cold, fall hot (G3P3's arrangement) (adopted as it stands 2026-09-11) |
| R-10 | dust as PM₁₀ in non-attainment counties | MODERATE | MINOR | DESIGN | enclosed negative-pressure handling (adopted as it stands 2026-09-11; R-01 geometry is the first layer) |
| R-11 | receiver scale: nothing above ~1 MW_t has run | DOMINANT | MAJOR | HOURS | multi-aperture; more towers; first module; FLAGGED FOR SIMULATION 2026-09-11, first in `tools/receiver.py` (per-metre curtain law, loss fraction size-invariant, pilot aperture at ~30 MW_th before the module) |
| R-12 | provenance: no plant of this kind exists | DOMINANT | MAJOR | HOURS | programme staging |
| R-13–16 | no freezing; no decomposition ceiling; no oxidiser or toxic medium; dry cooling at ⅙ the airflow | BENEFIT | | | |

**Before: 4 BENEFIT / 7 MODERATE / 3 MAJOR / 2 DOMINANT. After: 4 BENEFIT /
1 NEGLIGIBLE / 5 MINOR / 4 MODERATE / 2 MAJOR / 0 DOMINANT.**

## What design retires

Six rows reach MINOR by specification and stay there — CO₂ inventory,
pressure parts, silos, lift, dust, attrition — each ordinary practice in an
industry that exists (bulk solids, pressure plant, CCUS). Sourced where a
source reached: CARBO particles after ~200 h on-sun in Sandia's 1 MW_t
receiver at 0.946 absorptance against 0.945 unused; Inconel 740H
ASME-qualified 650–825 °C, the only age-hardened superalloy approved for
welded creep-limited pressure parts; G3P3's own lift-cold-fall-hot
arrangement; silo loss falling as surface over volume.

## What design cannot retire, and the file says so

Six rows are HOURS: the receiver in the wind and at scale, the exchanger at
its design point (prototype tested to 500 °C / 17 MPa against a design point
of 800 °C / 25 MPa; 4–6× any known particle/sCO₂ exchanger), the turbine at
715 °C (STEP's recompression phase, next), the particle chemistry over decades
(XRD shows transformations after heating in air; absorptance is restorable
by reduction; the rate over forty years is unknown), and provenance. **Each
has a design mitigation and all but one move a grade — R-08, the chemistry over
decades, is recorded as UNMOVED: rejuvenation manages it and does not reduce it,
and the fission register's rule that an unmoving mitigation is not a mitigation
is honoured by saying so rather than by promoting the row — and none reaches MINOR,
because a specification cannot make a machine have run.** What *is* upfront
for these is the plan: the field, towers and PV are common to Helios-2 and
Helios-3 and are built once; one Helios-3 module of 100 MWe is built first at
a first-of-a-kind premium; modules convert as its hours accumulate. The salt
block is the fallback, not the plan.

## The mitigations, priced

| adder | on | $M |
|---|---|---|
| R-01 enclosed conveyance, baghouse, +10 % | thermal storage | 126 |
| R-02 quartz covers, multi-aperture, +15 % | receivers | 321 |
| R-03 N+1 exchanger modules, +10 % | power block | 275 |
| R-04 small-unit premium, spares, +8 % | power block | 220 |
| R-05 CO₂ safety, +2 % | power block | 55 |
| R-06 740H over lesser alloys, +3 % | power block | 83 |
| R-07 refractory, expansion, +8 % | thermal storage | 101 |
| R-10 negative pressure, +3 % | thermal storage | 38 |
| first module at 1.5× on its thermal share | | 135 |
| particle makeup 1 %/yr + rejuvenation | O&M | 21 /yr |

| | Helios-3 as chained | **mitigated** | Helios-2 |
|---|---|---|---|
| capex net, $B | 30.0 | **32.3** | 37.0 |
| O&M, $M/yr | 412 | 434 | 447 |
| **$/MWh** | 117 | **125** | 141 |
| $/household/yr (today 1,177) | 706 | **756** | 849 |

**At critical (the author's standing rule, 2026-09-11: simulate critical, not optimal).** Every
band at its adverse end — optics 0.58, cycle 0.45, parasitics 0.90, availability 0.92, PV at its
low capacity factor, every cost band at its top, contingency and EPC at their tops, a 2.0
first-of-a-kind premium, 2 %/yr makeup — and the receiver at `receiver.py`'s critical open
figure of **0.795** rather than the chain's 0.90:

| | mid | critical | factor |
|---|---|---|---|
| mirror aperture, M m² | 18.1 | 26.8 | 1.48 |
| towers | 14.3 | 21.2 | 1.48 |
| capex net, $B | 32.3 | 51.4 | 1.59 |
| $/MWh | 125 | **191** | 1.52 |
| $/household/yr (today 1,177) | 756 | **1,153** | 1.52 |

**At critical Helios-3 needs $191/MWh, $71 above the band's top, and a household pays $1,153
against $1,177 today.** That is the front-end threshold: a plant designed to it carries the mid
figure as margin, and a plant designed to mid has none. What moves it is the chain, not the
mitigation — the receiver's 0.795 and the field's 0.58 grow the mirror by 1.48 before any adder
is applied. The critical case is printed beside mid and never in its place; `priced()` defaults
to mid and the selftest asserts that.

**Mitigated, Helios-3 needs $125/MWh — still under Helios-2's $141, and $5
above the top of the $80–120 band.** The chained figure was inside the band;
the mitigated one is not, by the price of the mitigation itself. That is the
answer to the author's claim, stated exactly: every cost a design can carry
is carried and priced, and it costs a few dollars a megawatt-hour, not the
plant; what remains is not a cost but a clock, and the staging plan is how
the clock is run.

## Status

The adders are ASSUMED bands and the file says so — a receiver vendor prices
a quartz cover, not this file. The first module's schedule is not modelled.
HOURS is never flattened into DESIGN: the author's rule is mitigations before
design, and a row only time can settle is owed to the record as such.

The selftest asserts every row carries a grade both sides, a kind and a
carrier; every mitigation moves its grade; every DESIGN row reaches MINOR and
no HOURS row does; both DOMINANT rows are HOURS and none survives; every
priced adder names a row and a line that exist; the mitigated price is above
the chained, by under 20 %, still below Helios-2, and within 10 % of the
band's top; the credit lands on the storage lines and adders only; and the
report says what design cannot retire, states the band position exactly, and
names the salt block as the fallback.
