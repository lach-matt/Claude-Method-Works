# DECK.md — the transport calculation, written out so it can be run

`python3 tools/deck.py` · `--provenance` · `--write` · `--selftest` · stdlib only

## Why it exists

The project has one uncertainty left. `fuelchoice.py`'s one-group model places the fissile fraction;
`criticality.py`'s **always-subcritical property** rests on where that model puts `k_inf = 1`; and the
whole hazard-class argument — and with it the adopted `k = 0.900` — rests on that. The model's own
error is **asserted** at fifteen percent and has never been measured **on this material**, because
there is no critical benchmark for a fast chloride salt: the first one is being built and has not run.

What settles it is a transport calculation, and a transport calculation is a **computation** rather
than an experiment. So this writes the decks for it, from the design's own numbers, and **states the
prediction before the run.**

## Why k_inf and not k_eff

An infinite medium has no geometry, no leakage, no blanket and no reflector — every one of which is a
place two calculations differ for reasons that are not the question. The previous attempt at this
compared a k_inf against a whole system's k_eff and had to open a seven-point error band to cover the
difference. **This cannot.**

## The material, imported from the design and not restated

| | |
|---|---|
| salt | NaCl–UCl₃, **18.91 mol %** UCl₃ |
| uranium by mass | 40 % |
| density | 3.3000 g/cm³ |
| temperature | 900 K |
| chlorine | Cl-37 enriched to 99.0 % |

## The decks, and the prediction each one carries

| fissile fraction | Pu-239 | U-238 | Cl (atoms/b·cm) | one-group k_inf |
|---:|---:|---:|---:|---:|
| 6.00 % | 1.9677e-04 | 3.0828e-03 | 2.3902e-02 | 0.8524 |
| 7.00 % | 2.2956e-04 | 3.0499e-03 | 2.3902e-02 | 0.9187 |
| 7.93 % | 2.6006e-04 | 3.0194e-03 | 2.3901e-02 | 0.9758 |
| **8.35 %** | 2.7370e-04 | 3.0057e-03 | 2.3901e-02 | **1.0000** ← the always-subcritical threshold |
| 9.00 % | 2.9514e-04 | 2.9842e-03 | 2.3901e-02 | 1.0367 |
| 10.00 % | 3.2793e-04 | 2.9514e-03 | 2.3901e-02 | 1.0894 |
| 12.00 % | 3.9351e-04 | 2.8857e-03 | 2.3900e-02 | 1.1845 |

**Every deck is derived, not typed.** The atom densities come from the design's own density and
stoichiometry, and the selftest sums them back into a mass density and requires the input back. *A deck
whose densities do not reproduce the density they came from is a deck that computes a different
material.*

## Writing a deck for the real material bought a finding before it bought an answer

| | |
|---|---:|
| `criticality.py` publishes the threshold at | **7.93 %** |
| at the composition the design actually holds | **8.35 %** |

**The published figure is computed at the eutectic, 34 mol % UCl₃.** The design's salt is 18.9 mol % —
a fact `fuelchoice.py` had already recorded and not repaired — and a more dilute salt carries more
sodium and more chlorine per heavy atom to absorb, so it needs **more** fissile to reach `k_inf = 1`,
not less. **The safety property was published for a material the design does not use** — the same
error the fluoride benchmark was withdrawn for, found one level further down.

It runs the safe way, and that is luck rather than design: the always-subcritical band is *wider* than
published. And `k = 0.900` survives untouched, because it is `k_inf = 1` carried through the leakage
allowance and not a fissile fraction at all.

## `--provenance` — what is published on this material, and what it says

Two figures exist and both are on the right material:

- **MCRE fuel** — the Molten Chloride Reactor Experiment uses the NaCl–UCl₃ binary **eutectic** with
  uranium enriched to **93.2 wt % U-235**; it needs 72–75 batches of salt to go critical, and it has
  not yet run.
- **MCFR start-up** — the commercial TerraPower / Southern Company Molten Chloride Fast Reactor states
  that **first plants start with 12 % enrichment**, and the fuel cycle needs no enrichment after
  start-up.

**The second one tests the deck, and it does not agree.** A commercial power reactor is *critical*:
k_eff = 1, so its k_inf exceeds one by whatever it leaks, and the `k_inf = 1` crossing lies **below**
the enrichment it starts at.

| | |
|---|---:|
| this model, U-235 in the eutectic salt | **14.66 %** |
| what a 12 % start-up implies, leaking 3–10 % | **10.80 – 11.64 %** |

**So the model demands 1.26 to 1.36 times more fissile than published practice does.** That is the
*safe* direction for a reactor and the **unsafe** direction for a criticality-safety **threshold** —
because a threshold is the fraction below which nothing can be critical, and over-stating it puts the
line in the wrong place.

| | |
|---|---:|
| this model's threshold, Pu-239, design salt | 8.35 % |
| the same, scaled by the conservatism above | **6.15 – 6.63 %** |
| the design's own operating fissile fraction | **8.35 %** |

**The design would sit above its own threshold**, and `criticality.py`'s central claim — that below it
the hazard class stops existing rather than being managed — is what justified `k = 0.900`.

**And the two claims may not be simultaneously satisfiable:**

| fissile | k_eff at the favourable leakage | beam MW |
|---:|---:|---|
| 6.15 % | 0.7763 | **does not close** |
| 6.63 % | 0.8051 | 2,010 |
| 8.35 % | 0.9000 | 240 |

Hold the always-subcritical property and the plant needs a beam it cannot have, or does not close at
all. Hold the plant and the salt is not always subcritical. **On this evidence the design is asked to
choose, and it has not been told it must.**

### The cautions, and they are load-bearing

This is a **flag**, not a result:

1. The MCFR's own salt composition is **not stated** in what is available. The comparison is made at
   the eutectic because that is what MCRE uses; if the MCFR is elsewhere, the conservatism factor
   moves.
2. 12 % is a **start-up** enrichment for a breeder. Its core geometry and leakage are not published
   here, which is why the leakage band is wide and the conclusion is required to survive all of it.
3. Scaling the Pu-239 threshold by the U-235 conservatism **assumes the model errs by the same
   multiple on both nuclides.** That is an assumption and not a result, and it is the weakest link.

**What the flag is worth is not its number but its direction.** It is drawn from published practice on
a *chloride fast salt* — the material the design uses — and it says the transport calculation is not a
formality: it decides whether the design as it stands is internally consistent. The prediction is
registered so the answer cannot be argued with after the fact.

### The studies that would settle it

- Idaho National Laboratory, *"Criticality Safety S/U based USL Calculation for UCl₃-NaCl Fuel Salt
  Operations"* — the same question, on the same salt, by the discipline's own method.
- The MCRE nuclear-data uncertainty analysis, which puts the data term at **2,161 pcm** and names
  **Cl-35** as its driver.
- Any MCFR neutronics paper stating a **composition and a k in the same table** — which is the one
  thing none of the available sources does.

## What is not done here

The decks are **not run in this environment**: it holds neither a transport code nor an evaluated
cross-section library, and OpenMC is not installable from the package index here. What is needed is
one of them plus ENDF/B-VIII.0 — a day's work for anyone who has both, and **the prediction above is
registered so that whoever runs it is not marking their own homework.**
