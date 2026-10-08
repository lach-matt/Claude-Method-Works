# B4d simulation, phase 1: a transition in one spacetime, as the board reads it (computed, READ and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `sim1_transition.py`, selftest 9/9, about 1 minute.
The heavy runs are banked in `sim1_bank.json` (about 45 minutes to regenerate). An independent fourth-order code's
numbers are in `sim1_repro.json`, and the READ sources, verbatim with pages, are in `sim_reads.json`.

Three verifiers checked this phase: numerics, claims and labels, and adversarial physics. They confirmed the solver.
An independent solver agrees to 0.08%, and a mutation test breaks the controls when the physics is broken. But they
did not let four first claims stand:
- that the collapse end point was computed;
- that one number decides every inflow;
- that the ordering of outcomes is your hierarchy of trajectories;
- that two outside papers corroborate stage 5.

All findings are applied (History).

## What you said

- **Item 167:** *"I think I understand now. You are technically running a simulation. Run it in phases. Start small, a
  transition in the same spacetime. Then build on it, with independent directions one at a time. This incidently will
  also likely give you a hierarchy of trajectories I would think. HOWEVER, if my interpretation of you task is
  incorrect, do not run these simulations unless you think they are the way to move forward"*.
- **Items 116 (b) and 117,** your own use of the words. *"The trajectory between two positions in the same direction
  are different and likely smaller than trajectories between positions in separate universes"*, and *"Consider travel
  between two positions within one universe vs travel between two counterfactual universes."*
- **Item 118:** trajectories are of two kinds, *"law and history"*.
- **Items 115 (c) and 136 G:** the inflow is the README, and the README is the energy.
- **Item 162:** the fixed size.
- **Item 163:** *"All together, one whole"*.
- **Item 157:** our current universe.

## Is your reading of the task right?

**Yes.**
- **B4d is a time evolution by its own statement:** the opening and closing "evolve regularly in five dimensions".
- **No stage so far was a numerical time evolution.** Stages 1–7 continued the static bulk off the plane along the
  extra dimension. Stages 3–4 and `opening.py` built exact dynamical pieces, but only on the plane.
- **A simulation makes the plane's geometry an output** instead of an input, so it tests the readings those stages
  rested on.

## Which transition? Two readings, put to you

- **The board's reading, which this phase ran (H-PHASE1-IS-4D).** One four-dimensional spacetime, no bulk, spherical:
  - the start flat (H-FLAT-START, the board's gloss on your 157's "our current universe");
  - the README's energy carried in by a massless scalar field (H-SCALAR-CARRIER), one initial-data family
    (H-GAUSSIAN-FAMILY).
- **Your own usage, items 116–118.** "A transition in the same spacetime" is the corridor's passage between two
  positions within one universe, the smaller trajectory, as against a passage between universes. The "hierarchy of
  trajectories" is then your law and history trajectories, ordered from within-universe to between-universe.
- **On either reading this phase stands as the validated time-evolution tool** the later phases build on. What changes
  is phase 2.

## The simulation

- **The equations are READ.** Polar-areal coordinates, G = 1: Gundlach & Martín-García, arXiv:0711.4620, eqs. (21)–(25),
  p.13. The lapse is normalised at the outer boundary as in Olabarrieta et al., arXiv:0708.0513, eq. (27), p.3; that only
  relabels time.
- **The constraint each step.** It is solved from its closed integral form by trapezoidal quadrature, which is second
  order.
- **One family of initial data:** φ = p·exp(−((r − 20)/3)²), moving inward.
- **A built-in check.** The momentum constraint is never imposed, and is used as the check.
- **What this code cannot do: follow a black hole.** Polar-areal slicing does not penetrate apparent horizons
  (0708.0513, p.3, READ). So every collapsing run is read at 2m/r = 0.95 (H-READOUT-095) and stopped. Continued past that
  point, the hole drains away numerically, which the verifier showed directly.

## What follows

**S1. Controls below the threshold** (computed; each can fail).
- **Flat space** against the exact solution: errors fall 4.2× and 4.0× per halving.
- **Strong field at p = 0.8 p*:**
  - convergence factor 3.99;
  - the unimposed momentum constraint's residual is 1.6×10⁻³, 4.1×10⁻⁴ and 1.0×10⁻⁴ of its scale;
  - total mass conserved to 1.7×10⁻⁵.
- **Near the threshold** the code is checked only by the two-grid masses and by γ (S2). The echoing period itself is not
  measured.

**S2. The threshold and the mass scaling** (computed; checked against READ values).
- **The outcomes, classified so they can't be faked.** Collapse means 2m/r reaches 0.95 at least 20 grid points from the
  centre. Dispersal is counted only when the total mass is conserved and the centre empties.
  - On the finest grid: 0.01686, 0.01687 and 0.016875 disperse, and 0.016885 collapses.
  - 0.01688 is a floor event: it crosses 0.8 at a few grid points, then drains away. Undecided.
- **An independent code agrees.** A separate fourth-order code (`sim1_repro.json`) puts p* = 0.01688 to four figures,
  inside the bracket.
- **The exponent depends on p* unless the wiggle is fitted.** Over masses 0.059–0.44, a plain power law gives γ anywhere
  from 0.43 (p* = 0.016875) to about 0.31 (p* near 0.016884); the best fit is 0.40. Fitting in the known wiggle, period
  Δ/(2γ) = 4.61 in ln(p − p*) (gr-qc/9604019, p.13, READ), gives **γ = 0.37** at p* = 0.01688, with a residual ten times
  smaller.
- **The READ value is γ = 0.374 ± 0.001** (gr-qc/9604019, abstract p.1).
- **How well the two grids agree.**
  - The 0.8-readout masses agree to 0.35%.
  - The 0.95-readout masses differ by 2–6% between dr = 0.01 and 0.005. Both are banked; the readout jumps between echoes
    in places.

**S3. What the outcome depends on** (computed within the family; deduced beyond it).
- **Within a family of fixed shape, one number decides.** Below the threshold the inflow disperses; above it, it
  collapses with M ∝ (p − p*)^γ; one critical solution sits between. That is an **ordering of solutions**, the board's
  analogy (H-HIERARCHY-IS-OUTCOME-ORDER), **not your trajectories**.
- **Across shapes it is not one number.** A supercritical burst followed by a tail of any length still collapses. That
  follows from the domain of dependence.
- **For a long write, the inflow rate decides.** At threshold this family carries its mass (0.59) in about 2δ: a rate of
  about **0.1 per mass unit**.
- **Where the README's write falls.** `o3_write.py` W3's gas bound puts the write at ≥ 2.0×10⁵ clocks, computed there at
  the example README and carried in the option you chose in 163. Spread evenly over that, the README's energy arrives at
  a rate of about 5×10⁻⁶: **2×10⁴ times below the threshold.** In this family that is an amplitude of about 1.2×10⁻⁴,
  between the computed dispersals at 10⁻⁶ and 0.01686.
- **So a README written evenly over the write disperses** (deduced for evenly spread writes). A write with any stretch
  above about 0.1 m per clock collapses, and is then held by a hole that grows.

**S3b. A horizon that keeps its size absorbs nothing, in one spacetime** (deduced; Raychaudhuri, standard, not READ).
- **The argument.** Along a horizon's generators, dθ/dλ = −θ²/2 − σ² − R_kk. Your 162's fixed size means θ = 0 throughout,
  so R_kk = −σ² ≤ 0.
- **With ordinary matter that forces zero flux.** Matter that obeys the null energy condition gives R_kk = 0 = σ: nothing
  crosses.
- **It is stage 5's F1 again.** That stage's dm/dv = 0 at r = 2m is the same statement.
- **So in one spacetime the README cannot be carried into a horizon that keeps its size.** The negative R_kk that would
  allow it is S4's.

**S4. Eq. (17) is out of reach of one spacetime** (computed; STRUCTURAL; the pointwise part restates `opening.py` O3).
- **The criterion is exact.** For any static metric, radial R_kk = (H/r)·d ln(F/H)/dr. So the null energy condition is
  exactly "F/H never decreases outward".
- **Eq. (17) fails it everywhere.** Its d ln(F/H)/dr = −m/((2r − 3m)(r − 2m)) < 0: F/H falls from infinity at the horizon.
  Its zero surface gravity comes precisely from F/H → ∞ there.
- **So no static end state reached with ordinary matter is eq. (17),** or close to it in F/H.
- **Pointwise:** a scalar has R_kk ≥ 0, while eq. (17) has R_kk < 0, the shortfall largest (0.0443/m²) at r = 2.295m.
- **What is not computed here.** The collapse end state, Schwarzschild outside, comes from Birkhoff's theorem (standard,
  not READ).

**S5. What the next direction must supply** (computed).
- **Read as an effective fluid on the plane,** eq. (17)'s Weyl term has:
  - energy density ρ = m²/(8πr²(2r − 3m)²) > 0, which integrates to **m/4 outside 2m**: `ledger.py` E4's 5m/4 − m, the
    control;
  - radial pressure p_r = −m/(8πr²(2r − 3m));
  - tangential pressure p_t = m(r − m)/(8πr²(2r − 3m)²).
- **So radially the null energy condition fails and tangentially it holds:** the term is **anisotropic**.
- **A plane-uniform phase 2 cannot carry it.** A Weyl term uniform along the plane is isotropic (dark radiation). The
  bulk must supply an anisotropic Weyl stress, and along a trajectory that also holds the README.

## Outside the board (READ, from `sim_reads.json`)

- **Eq. (17) is a published metric.** It is Casadio–Fabbri–Mazzacurati's Case I at its zero-temperature member: deduced
  from their eqs. (8) and (13), gr-qc/0111072, p.2. They call it *"completely regular"* and leave its bulk open (p.4).
- **An analogue of stage 5 F2, for a different metric.** Chamblin–Reall–Shinkai–Shiromizu (hep-th/0008177, p.7) studied
  the tidal Reissner–Nordström brane metric. That has F = H, which excludes eq. (17). They found *"the trace of the
  extrinsic curvature diverges at a finite distance from the brane"*.
- **A caution, not a check.** Casadio–Mazzacurati (gr-qc/0205129, p.9) are qualitative only at eq. (17)'s η = 3/4.
  - They find the area growing into the bulk, *"as one would indeed expect on a negative tension brane"*.
  - They also find caustics: Gaussian coordinates that do not cover the bulk. That is a caution on the coordinates stage 5
    used, not a check of F6.
- **Phase 3's template.** Wang & Choptuik (arXiv:1604.04832, pp.1–3) evolved collapse on an RS2 brane in (t, r, y): a
  hole of finite extent settles to an *"apparently stationary"* state, though *"the evolution inevitably departs from this
  configuration"* (p.3).

## Verdict

- **Phase 1 gives a validated time-evolution tool, and three statements about one spacetime:**
  - a README written evenly over the write disperses;
  - a horizon that keeps its size absorbs nothing;
  - eq. (17) cannot be an end state.
- **All three point at the extra dimension,** which must supply an anisotropic Weyl stress (S5).
- **No status moves.** B4d stays OPEN.

## Phase 2, depending on your answer

- **On the board's reading:** add y with the plane uniform along r.
  - **Its limits.** S5 shows such a plane cannot carry eq. (17)'s anisotropy, and its sign question already has a
    closed-form answer: with f = R²/ℓ² − μ/R², μ < 0 gives a naked singularity on the decaying side and none on the
    growing side.
  - **Its value.** Validating the code against exact solutions, and following how the plane moves. Energy flowing into
    the bulk (the question your 158 (4) left to the math) needs matter in the bulk.
  - **It should use your 166's arrangement:** the slab between the planes plus the bulk beyond each.
- **On your reading (items 116–118):** add the extra direction the corridor's trajectory passes through, between two
  positions in one universe.
  - **In one spacetime alone,** such a shortcut is ruled out for matter obeying the averaged null energy condition
    (topological censorship, the board's walls D/`censor.py`).
  - **So phase 2 adds the dimension that lifts that.** The hierarchy is then your law and history trajectories, from
    within one universe to between universes.

## History (three verifiers, 2026-10-08)

**What they confirmed.**
- Every number in S1 and S2.
- The metric solve, the treatment at the centre, the dissipation and the exact flat control, all re-derived.
- The controls are not trivially satisfied: a mutation test with the constraint coupling or the lapse perturbed breaks
  the momentum check.
- An independent solver agrees to 0.08% at p = 0.0176.
- M_ADM(p*) = 0.5916.
- Phase 2's side assignment (μ < 0 is singular on the decaying side).
- Your quotes.
- CLOSEDBULK.md's "NAMED, NOT READ".

**Their findings, all applied:**

**MUST-FIX**
1. **The code cannot follow a hole.** The end state is relabelled Birkhoff (not computed), and runs are read at 0.95 and
   stopped.
2. **The 0.374 attribution.** It is gr-qc/9604019; the Living Review gives only ≈ 0.37.
3. **Chamblin et al. is for a different metric (F = H)**, so it is an analogue, deduced.
4. **Casadio–Mazzacurati is a caution about the coordinates,** not support for F6.
5. **"The first rung of your hierarchy" was the board's analogy.** It is now H-HIERARCHY-IS-OUTCOME-ORDER, and your
   usage in 116–118 is put to you.
6. **157 is H-FLAT-START,** the board's gloss.
7. **"One number decides" is false across shapes.** For a long write the rate decides, and the conclusion is restricted
   to evenly spread writes.
8. **"Hierarchy of trajectories" is your defined term** (116–118). It is not claimed.

**SHOULD-FIX**
- **A robust dispersal test.** Total mass conserved; the 0.8 floor events are now undecided.
- **γ depends on p*.** The range across the bracket is reported, and the wiggle-aware fit gives 0.37.
- **A sub-range fit put p* above banked collapses.** p* is now bounded by the bracket.
- **The 0.95 masses** are now banked at a second resolution: 2–6%.
- **Labels:** 4.2× and 4.0×; 0.35% agreement at the 0.8 readout; the 0.05 floor claim dropped.
- **"Why 7% is acceptable"** is now answered by the wiggle fit, not argued.
- **The 2×10⁵ clocks** are attributed to `o3_write.py` W3, not to you.
- **"Not even approximately"** is replaced by the static F/H criterion and the size of the shortfall.
- **The CFM identification** is deduced.
- **Wang–Choptuik** is cited at p.3, with "inevitably departs".
- **The board's readings are named.**
- **"Avoiding"** is now "had not done", and "stages 1–7" is corrected.
- **The lapse normalisation** is cited.
- **Item 167** is quoted in full.
- **The timings** are corrected.
- **S3b (fixed size, Raychaudhuri)** is added.
- **S5 (the anisotropic Weyl fluid)** is added, and phase 2 redesigned around it.
- **Missing carriers:** null dust never disperses (Vaidya, standard). A radiation fluid has its own threshold (Evans &
  Coleman, gr-qc/9402041, named, not READ).

## Named hypotheses

- **Yours:** 115 (c), 116 (b), 117, 118, 136 G, 157, 162 (H-FIXED-SIZE), 163 (H-AT-ONCE-IS-WHOLE), 167
  (H-PHASED-SIMULATION, H-TRAJECTORY-HIERARCHY).
- **The board's:**
  - H-PHASE1-IS-4D;
  - H-FLAT-START;
  - H-SCALAR-CARRIER;
  - H-GAUSSIAN-FAMILY;
  - H-READOUT-095;
  - H-HIERARCHY-IS-OUTCOME-ORDER.
