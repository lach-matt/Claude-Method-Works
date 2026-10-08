# B4d simulation, phase 1: a transition in one spacetime (computed, READ and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `sim1_transition.py`, selftest 8/8, about 3 minutes.
The heavy runs are banked in `sim1_bank.json` (about 45 minutes to regenerate). The READ sources, with verbatim quotes
and pages, are in `sim_reads.json`.

## What you said

- **Item 167:** *"You are technically running a simulation. Run it in phases. Start small, a transition in the same
  spacetime. Then build on it, with independent directions one at a time. This incidently will also likely give you a
  hierarchy of trajectories I would think. HOWEVER, if my interpretation of you task is incorrect, do not run these
  simulations unless you think they are the way to move forward"*.
- **Items 115 (c) and 136 G:** the inflow is the README, and the README is the energy.
- **Items 162 and 163:** a fixed size, held as one whole; the write lasts at least 2.0×10⁵ clocks.
- **Item 157:** our universe, before the opening.

## Is your reading of the task right?

**Yes, and it names what the board had been avoiding.**
- **B4d is a time evolution by its own statement:** the opening and closing "evolve regularly in five dimensions".
- **The board had not run one.** Stages 1–7 continued the static bulk off the plane along the extra dimension.
- **That is why several of their conclusions rested on readings** (quasi-staticity, eq. (17) imposed on the plane, the
  analytic class).
- **A simulation makes the plane's geometry an output,** so it tests those readings directly.
- **The outside literature confirms the distinction.** Chamblin–Reall–Shinkai–Shiromizu (hep-th/0008177, p.2, READ)
  contrast evolving "in the spacelike direction transverse to the brane" with evolving from "a spacelike hypersurface …
  in a timelike direction". The board had done the first; your phases do the second.

## The board's reading of "a transition in the same spacetime" (H-PHASE1-IS-4D-COLLAPSE; correct it if wrong)

- **One spacetime:** one four-dimensional spacetime, no bulk, spherical symmetry. The directions are (t, r).
- **Its starting point is our universe:** flat space (your 157).
- **The README's energy is carried in** by the simplest carrier that obeys the null energy condition and has real
  dynamics: a massless scalar field.
- **The question:** what the inflow becomes.
- **The phases that follow:**
  - Phase 2 adds the extra dimension y on its own, with the plane uniform along r.
  - Phase 3 has r and y together: the corridor.

## The simulation

- **The setup is Choptuik's** (G = 1, G_ab = 8πT_ab), in polar-areal coordinates.
- **The equations are READ.** They are Gundlach & Martín-García's eqs. (21)–(25), Living Rev. Rel., arXiv:0711.4620, p.13.
- **Every step is consistent.** The Hamiltonian constraint is solved exactly at each step, in closed integral form.
- **The numerics:** second-order differences, RK4, fourth-order dissipation, and an outgoing boundary at r = 50.
- **One family of initial data:** φ = p·exp(−((r − 20)/3)²), moving inward.
- **A built-in check.** The momentum constraint is never imposed, and is used as a check.

## What follows

**S1. The machine is validated** (computed; every control could fail).

| control | result |
|---|---|
| a weak pulse in flat space (p = 10⁻⁶) against the exact solution [f(t+r) − f(t−r)]/r | error falls 4.0× per halving of the step, at t = 20 and t = 40 (second order) |
| a strong field (p = 0.8 p*), three resolutions | convergence factor 3.99 (second order expects 4) |
| the momentum constraint, never imposed | residual 1.6×10⁻³, 4.1×10⁻⁴, 1.0×10⁻⁴ of its scale: 4× per halving |
| total mass, before radiation reaches the edge | conserved to 1.7×10⁻⁵ on the finest grid |

**S2. The family has a threshold** (computed; checked against a READ value).
- **Below it the inflow disperses.** The peak of 2m/r stays below about 0.5.
- **Above it, it collapses.** 2m/r → 1 and the lapse → 0.
- **Bracketed on the finest grid:** 0.01686 and 0.01687 disperse, 0.016885 collapses; the fitted p* = 0.016878.
- **Above threshold M ∝ (p − p*)^γ.** Read at 2m/r = 0.95, closest to the horizon, over masses 0.059–0.44, the fit
  gives **γ = 0.40**, with sub-ranges 0.35–0.43. The READ value is **0.374 ± 0.001** (Gundlach, gr-qc/9604019, abstract
  p.1; "γ ≃ 0.37" in the Living Review, p.19).
- **Why 7% high is acceptable.**
  - The mass range spans about one period of the known wiggle, Δ/(2γ) ≈ 4.61 in ln(p − p*) (gr-qc/9604019, p.13).
  - A code like this one measures the first apparent horizon's mass, which depends on the slicing (Living Review,
    pp.16–17, page not pinned).
- **What could not be used.** Readouts at 2m/r = 0.8 and 0.9 jump between echoes, so they are recorded and not fitted.
- **The two finest grids agree** on the masses to 0.5% for p ≥ 0.0169. Masses below about 0.05 are a resolution floor
  (a few grid points across), and the note records them as such.

**S3. The hierarchy of trajectories** (computed; the ordering deduced).
- **One number decides the outcome.** The theory has no length scale, so what happens depends only on the inflow's
  compactness: how long the inflow lasts, measured in units of its own mass.
- **The trajectories order along that number:**
  - dispersal below the threshold;
  - collapse above it, with M ∝ (p − p*)^γ;
  - one critical member between them.

  That is the first rung of the hierarchy you expected.
- **Where the threshold sits.** The inflow lasts about 2δ/M_ADM ≈ **10 of its own mass units** (M_ADM(p*) = 0.59). That
  is this family's profile, an order of magnitude.
- **Where your 163 puts the README.** Its write lasts at least 2.0×10⁵ clocks, a clock being the README's own mass:
  **2×10⁴ times longer than the threshold.** So a wave inflow carrying the README's own energy over the write disperses.
  It cannot hold itself.
- **The limits of that statement.** Pressureless matter would not disperse (Oppenheimer–Snyder; standard, not READ). A radiation gas, `o3_write.py`'s carrier,
  behaves as the wave does; that is a reading, not computed here.

**S4. The end point is not eq. (17), and cannot be, in one spacetime** (computed; STRUCTURAL).
- **What a collapse ends in.** 2m/r → 1, with m(r) constant outside the matter. That is Schwarzschild outside (by
  Birkhoff, standard, not READ): H = F, surface gravity 1/(4M), not extremal.
- **Why eq. (17) is out of reach.**
  - For this carrier R_kk = 8πT_kk = 8π(k·∂φ)² ≥ 0 for every null k, at every point of every trajectory (exact).
  - Eq. (17) has radial R_kk = −2m(r − 2m)/(r²(2r − 3m)²) < 0 at every r > 2m (computed from its metric).
  - So **no trajectory in one spacetime, with a carrier that obeys the null energy condition, reaches eq. (17), even
    approximately.**
- **What the next direction must supply.** Exactly that negative R_kk: the bulk's Weyl term, −E_kk = R_kk(eq. 17)
  < 0 on the plane. And it must do so along a trajectory that also holds the README (S3).

## Outside the board (READ, from `sim_reads.json`)

- **Eq. (17) is a known metric.** It is Casadio–Fabbri–Mazzacurati's Case I (gr-qc/0111072, p.2, eq. (8)) at its
  zero-temperature member (p.4).
  - **On the plane** it is *"completely regular"* (p.4).
  - **Its extension into the bulk** they leave open: *"it will be important to investigate the extension of our
    solutions into the bulk"* (p.4).
  - **The board had named it but not READ it** (CLOSEDBULK.md). It is now READ.
- **Stage 5 F2's finding was found independently, in 2001.** Chamblin–Reall–Shinkai–Shiromizu (hep-th/0008177)
  carried brane metrics with a Weyl term into the bulk along y. They found that *"the trace of the extrinsic curvature
  diverges at a finite distance from the brane"* (p.7), and *"suspect that our solutions will generically have a
  curvature singularity"* there (p.7).
- **Stage 5 F6's side as well.** Casadio–Mazzacurati (gr-qc/0205129, p.9) find caustics for eq. (17)'s sign of the
  term. They also note it behaves *"as one would indeed expect on a negative tension brane"*: the side stage 5 found
  regular.
- **Phase 3 has a template.** Wang & Choptuik (PRL 117, 011102, 2016; arXiv:1604.04832, pp.1–2) ran the full (t, r, y)
  problem for collapse on an RS2 brane.
  - **Their method:** a well-posed generalized-harmonic evolution, with the brane's constraints enforced as boundary
    conditions.
  - **Their result:** a black hole of finite extent in the bulk, settling to an *"apparently stationary"* state.
  - **Their scale:** they used a uniform grid on one processor (Wang's thesis, arXiv:1505.00093, PDF p.130).

## Verdict

- **Phase 1 builds and validates the evolution,** and gives the first rung of the hierarchy of trajectories.
- **In one spacetime, the README's inflow has two fates.** It disperses, which is what any write as long as your
  163's does, or it collapses to a Schwarzschild hole. It never reaches the corridor's extremal eq. (17).
- **Both point at the next direction.** The hold over 2×10⁵ clocks (162, 163), and the corridor's geometry, must come
  from the bulk.
- **No status moves.** B4d stays OPEN.

## Next: phase 2, the extra dimension on its own

- **What it adds.** The direction y, with the plane uniform along r: one independent direction at a time, as you
  asked.
- **What it checks against.** There, Birkhoff's theorem makes the bulk anti-de Sitter–Schwarzschild with a constant
  μ, and the plane's own equations follow from the junction. That gives exact controls.
- **What it tests.** It is the plane-uniform analogue of the corridor. The question is which sign of the bulk's Weyl
  term (the parameter μ) a regular bulk allows on each side of a plane:
  - eq. (17)'s sign is μ < 0;
  - it should leave a naked singularity on the decaying side (R → 0);
  - it should leave none on the growing side.

  That is stage 5's F2 and F6 in dynamical form, to be computed and not assumed.
- **What it adds beyond that.** Energy moving into the bulk (your 158 (4)) as a genuine time evolution.

## Named hypotheses

- **Yours:** 115 (c), 136 G, 157, 162, 163, 167 (H-PHASED-SIMULATION, H-TRAJECTORY-HIERARCHY).
- **The board's:**
  - H-PHASE1-IS-4D-COLLAPSE (the reading of "a transition in the same spacetime");
  - the massless scalar as the README's carrier;
  - this initial-data family;
  - the mass readout at 2m/r = 0.95.
