# `tools/receiver.py` — the particle receiver, scaled rather than asserted about

**Why it exists.** `helios3.py` R-11 says the largest particle receiver that has run is about
1 MW_t and a Helios-3 tower needs hundreds of MW_th, grades that MAJOR after mitigation, and the
author flagged the row for simulation on 2026-09-11. A MAJOR that rests on one large number is
worth asking what the number is made of. This is the first simulation; it computes what
physically scales in a falling-particle receiver and what does not, on the material the design
intends to use (sintered bauxite in a falling curtain), fixtured on Sandia's 1 MW_t receiver on
that material. **Reviewed against the record on 2026-09-11** (`studies.py`): the flux the design
assumes, the measured temperature rise per metre of drop, G3P3-USA's 2 MW_th receiver and its
80–90 % measured efficiency, and DLR's 2.5 MW_th CentRec were all brought in, and two results
changed — the critical receiver fell from 0.795 to **0.690**, and the dome's verdict split.

**Run it.** `python3 tools/receiver.py` for the report, `--selftest` for the checks. Stdlib
only; imports the fleet tower duty from `cspchain.py`'s Helios-3 design and never restates it.

**The rule it runs under (author, 2026-09-11): simulate critical, not optimal.** Every banded
constant carries a NOMINAL value and a CRITICAL value, the critical being the adverse end of its
band — 45 °C ambient, windy convection, aged absorptance 0.90, a hot back wall at 850 °C, a 1 m
free-fall drop, low-end cp, standard soiled quartz at 0.85 with a short rod, and an
aperture-average flux of **0.5 MW/m²** against the Gen3 design point of 1.0 (Sandia measured its
curtain at averages of 0.3–0.7). Every result prints
in both columns, the design is held to the critical column, and the nominal column is margin.
A number quoted from this file without its case is misquoted. The selftest asserts critical ≤
nominal on every efficiency and every loss term, and critical ≥ nominal on every width and
mass flow.

## Four results, stated at the critical case

1. **The curtain is a per-metre machine.** Flux it can take, mass it can carry and the
   temperature rise across one drop are all per metre of width and per metre of drop. Power is
   width × drop × flux. At the critical 0.5 MW/m², 1 m free-fall drop and low-end cp, a metre of
   curtain carries 0.5 MW at 2.5 kg/s for 600 → 800 °C (3 MW at 12.5 kg/s at the nominal 3 m
   mesh-slowed drop and 1 MW/m²). Sandia measured **50–200 °C per metre of drop at 1–7 kg/s per
   metre and averages up to 0.7 MW/m²**, and the law spans that range; the selftest asserts it. Scale is therefore bought in **width** and in **aperture count**, neither of which is
   a 700× step.

2. **The thermal loss fraction at fixed flux does not change with aperture size.** Radiation
   and convection both scale with aperture area, as the power does, so the efficiency is the
   same at 1 m² and at 30 m²: **0.690 critical open** (0.882 nominal), **0.592 critical domed**
   (0.835 nominal). The critical figure fell from 0.795 when the review halved the critical flux:
   the losses per m² are the same and the power they are set against is half. What does change with size is the **edge** — spillage, curtain-driven air
   escape, non-uniform feed — perimeter effects that shrink as perimeter/area. The record spans
   0.50 (the 1 MW_th free-fall curtain) to 0.90 (G3P3-USA, 2 MW_th) where the model says
   0.69–0.88; the gap is the edge. The critical column assumes scale does not reduce it, which
   is the threshold.

   The R-02 dome is priced beside the open aperture in both columns. It costs 70 (nominal) to 75
   (critical) kW/m² of transmission going in and saves convection and part of the radiation
   coming out, so **on the model alone it loses** at both cases (break-even 59 / 81 kW/m² of open
   loss beyond radiation against 8 / 24 kW/m² of modelled convection). **The review split the
   verdict on the record**: against the best measured receiver, G3P3-USA at 80–90 %, the dome
   **loses** at nominal (40 kW/m² of loss beyond radiation, under the 59 break-even); against the
   worst, the free-fall curtain at 50 % and critical flux, it **pays** (169 against 81). Both are
   pinned in the selftest. Which record the fleet receiver resembles is what the pilot aperture
   measures, and the file does not choose.

3. **The staging plan did not stage the receiver.** The first 100 MWe module's field charges the
   night, so its receiver is about 2.3× its turbine's thermal — **434 MW_th, 0.55 of a fleet
   tower's 794**. The ladder as planned was 2 → 434 → 794: one step of 217× and then 1.8×. A
   **pilot aperture at fleet-aperture size** belongs between: 2 → 30 → 434 → 794, factors 15,
   14.5 and 1.8, starting from G3P3-USA's 2 MW_th, the largest falling curtain that has run
   (CentRec, a centrifugal receiver, has run at 2.5). At the critical 0.5 MW/m² and 1 m drop a
   30 MW_th aperture is a **60 m wide, 1 m tall slot** carrying 150 kg/s (10 m × 3 m at 125 kg/s
   nominal), and a fleet tower is some 26 of them around a polygonal cavity — comparable in aperture to Crescent Dunes' 1,100 m² external
   receiver. The tower is designed to the critical slot; the nominal one is margin, not a plan.
   The module is then copies of the pilot and the tower is copies of the module.

4. **The threshold handed upstream.** `cspchain.py` carries one receiver efficiency, rec = 0.90.
   If the receiver returns this file's critical open figure instead, the field must grow by
   **1.30** (1.52 domed) to hold 18.1 TWh — and the towers and the price with it. That is the
   front-end threshold band the author asked for: the downstream instrument hands its critical
   figure to the one above it rather than the hoped-for one. `cspchain.py` is not changed here;
   it is told.

## What it does not do

It does not make the receiver have run, and the grade stays with `helios3.py`: R-11 is still
MAJOR / HOURS. What it moves is the question — from "700×" to "a 10 m curtain fed uniformly,
thirty times, on one tower" — and it names the pilot that answers it. The selftest asserts the
per-metre law against Sandia's mass flow, the Planck fraction against the Wien-peak identity,
that the dome loses on the model and pays on the record, that the ladder factors multiply to the
whole step, and that the staging gap is real (the module between 0.4 and 0.7 of a tower).

**Status of the constants.** The demonstrated unit (1 MW_t, ~1 m², 1–7 kg/s per m, 50–200 °C/m,
0.3–0.7 MW/m² average, 0.50–0.90 measured across the two Sandia receivers), G3P3-USA's 2 MW_th,
CentRec's 2.5 MW_th, the particle cp band, the design flux and the absorptance after 200 h are
SOURCED; the critical flux, the drop height band (1–3 m),
aged absorptance, cavity emittance, convection band, radiating temperature, ambient, the
soiled-quartz transmission and the dome's infrared return fraction are ASSUMED and say so.
Every constant line carries a status and the selftest fails one that does not.
