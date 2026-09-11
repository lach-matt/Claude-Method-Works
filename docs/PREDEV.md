# `tools/predev.py` — the studies and surveys, priced as the first line

**Why it exists.** The author's instruction of 2026-09-11: *all studies and surveys are built into
the upfront cost as their own line item, preceding most of the others by first priority.* Before
this the program carried them as a ladder of HOURS (`studies.py`), a pilot tranche (`titleone.py`)
and a ranked list of site studies (`sites.py`), and none of the resource, site, environmental,
permit, interconnection or reservoir work was priced at all: the price began at the field.

**Run it.** `python3 tools/predev.py` (`--selftest`). Stdlib only; it imports `helios.py` for the
node count and nothing else, so `helios3.py`, `titleone.py` and `aquacost.py` can import it lazily.

## What it prices

**Title I, gating** (must finish before the field rung): one year of on-site DNI at each node, a
measured load profile, title and fallowing agreements, geotechnical and ASCE 7 seismic hazard,
biological and cultural surveys, a CEQA EIR per node, a NEPA EIS on the Mojave node, a CAISO
interconnection study per node, and the reservoir siting and head study the water route needs.

**Title I, on the ladder** (run against the build): the field optical measurement, the quartz dome
beside an open aperture, particle ageing, silo cycling, the particle-to-sCO₂ exchanger module, the
STEP recompression phase and first unit, alloy exposure, the PV-fed heater and the dry-cooler test —
`studies.py`'s recommendations, each with a cost band. **The 30 MW_th pilot aperture is not repeated
here**: `titleone.py` already prices it as a tranche from `cspchain.py`'s own lines.

**Title II, per selected coastal site**: outfall diffuser hydraulics, a two-year entrainment study,
site survey and remediation scope, the seismic and tsunami basis, and the Coastal Development Permit
pre-application with its EIR, plus a screening pass over the eight candidates in `sites.py`.

Every cost and duration is an **ASSUMED band from the class of study, not a quote**, and the file
says so. An owner's engineer on the study phase is carried at 10 / 15 %.

| | mid | critical |
|---|---|---|
| Title I gating studies, $M | 106 | 228 |
| Title I technology studies on the ladder, $M | 88 | 175 |
| owner's engineer, $M | 19 | 60 |
| **Title I total, first in the capital, $M** | **213** | **463** |
| longest gating study, years | 2.0 | 4.0 |
| studies start / field rung starts | 2027 / 2029 | 2027 / 2031 |
| Title II per selected site, $M | 18 (+4 screening) | 43 (+8 screening) |
| Title II per module, $M | 4.3 | 17.8 |

## Where it lands

- `helios3.priced()` adds the Title I total to the capital **before every plant line**, with
  contingency and without EPC margin or sales tax. The register price moves from $125 / $202 to
  **$126 / $205 per MWh**.
- `titleone.tranches()` opens with **tranche zero, "studies and surveys (gating)", 2027 to the field
  start**; the field rung waits on the longest gating study, so at critical the whole schedule slides
  two years (field 2031, fleet to 2043), and `studies.py`'s escalation prices what that costs. The
  ladder's technology studies ride with the pilot tranche.
- `aquacost.module()` carries the Title II studies per module, $4.3 / $17.8 M, so the water price
  moves from $3,034 / $4,790 to **$3,044 / $4,830 per acre-foot**.
- Title I §7 now opens with the studies table and the schedule shows tranche zero; Title II §1 shows
  the per-module line.

## What it does not do

It does not quote. The gating durations at critical (a four-year NEPA EIS, a five-year coastal
permit) are the record's, and they are what makes the critical schedule two years later than the
mid. A study that comes in under its band returns the difference; one that runs over its years
costs the plant its escalation, which is the number `studies.py` prints.
