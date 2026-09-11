# `tools/receiver.py` — the particle receiver, scaled rather than asserted about

**Why it exists.** `helios3.py` R-11 says the largest particle receiver that has run is about
1 MW_t and a Helios-3 tower needs hundreds of MW_th, grades that MAJOR after mitigation, and the
author flagged the row for simulation on 2026-09-11. A MAJOR that rests on one large number is
worth asking what the number is made of. This is the first simulation; it computes what
physically scales in a falling-particle receiver and what does not, on the material the design
intends to use (sintered bauxite in a falling curtain), fixtured on Sandia's 1 MW_t receiver on
that material.

**Run it.** `python3 tools/receiver.py` for the report, `--selftest` for the checks. Stdlib
only; imports the fleet tower duty from `cspchain.py`'s Helios-3 design and never restates it.

## Three results

1. **The curtain is a per-metre machine.** Flux it can take, mass it can carry and the
   temperature rise across one drop are all per metre of width and per metre of drop. Power is
   width × drop × flux: at 1 MW/m² a 1 m drop carries 1 MW per metre of width at 4.2 kg/s per
   metre for 600 → 800 °C, and Sandia ran 1–7 kg/s through its 1 m curtain. The law reproduces
   the machine. Scale is therefore bought in **width** and in **aperture count**, neither of
   which is a 700× step.

2. **The thermal loss fraction at fixed flux does not change with aperture size.** Radiation
   and convection both scale with aperture area, as the power does, so the model's efficiency
   (0.88 calm, 0.87 windy, 0.84 domed) is the same at 1 m² and at 30 m². What does change with
   size is the **edge** — spillage, curtain-driven air escape, non-uniform feed — and those are
   perimeter effects that shrink as perimeter/area. Sandia measured 0.50–0.80 where the model
   says 0.88; the gap is the edge, and it is the one thing scale reduces for free.

   The R-02 dome is priced beside the open aperture. It costs 70 kW/m² of transmission going in
   and saves convection and a quarter of the radiation coming out, so **on the model alone it
   loses** (break-even 59 kW/m² of open loss beyond radiation, against 23 kW/m² of modelled
   windy convection) and **on the measured record it pays everywhere** (200–500 kW/m² of
   measured loss). Both are printed; the file does not choose, because which is right is what
   the hours measure.

3. **The staging plan did not stage the receiver.** The first 100 MWe module's field charges the
   night, so its receiver is about 2.3× its turbine's thermal — **434 MW_th, 0.55 of a fleet
   tower's 794**. The ladder as planned was 1 → 434 → 794: one step of 434× and then 1.8×. A
   **pilot aperture at fleet-aperture size** belongs between: 1 → 30 → 434 → 794, factors 30,
   14.5 and 1.8. At a 3 m mesh-slowed drop a 30 MW_th aperture is a **10 m wide slot** carrying
   125 kg/s, and a fleet tower is some 26 of them around a polygonal cavity — comparable in
   aperture to Crescent Dunes' 1,100 m² external receiver. The module is then copies of the
   pilot and the tower is copies of the module.

## What it does not do

It does not make the receiver have run, and the grade stays with `helios3.py`: R-11 is still
MAJOR / HOURS. What it moves is the question — from "700×" to "a 10 m curtain fed uniformly,
thirty times, on one tower" — and it names the pilot that answers it. The selftest asserts the
per-metre law against Sandia's mass flow, the Planck fraction against the Wien-peak identity,
that the dome loses on the model and pays on the record, that the ladder factors multiply to the
whole step, and that the staging gap is real (the module between 0.4 and 0.7 of a tower).

**Status of the constants.** The demonstrated unit (1 MW_t, 1 m², 1–7 kg/s, 0.50–0.80 measured),
particle cp, peak flux and absorptance are SOURCED; the drop height band (1–3 m), cavity
emittance, convection band, ambient and the dome's infrared return fraction are ASSUMED and say
so. Every constant line carries a status and the selftest fails one that does not.
