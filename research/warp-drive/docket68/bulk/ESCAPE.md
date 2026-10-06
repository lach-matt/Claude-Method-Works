# The four routes, and the shapes with zero curvature scalar (M-RULINGS items 80–82; READ, deduced and computed; verified once; not seated; 2026-10-06)

*First headed* "The four routes, and the shape that does not move (M-RULINGS items 80–82; READ, deduced and computed;
not verified; not seated; 2026-10-06)".

## What M asked

- **Item 80:** *"What the test does not cover: a field in the bulk (the field that would stabilise the distance between
  our planes is one), a faster-than-light bubble, matter that radiates, and a thick brane. Each stays OPEN. -
  exhaustively test these"*.
- **Item 81:** *"Why does light speed matter if speed is not part of the warp process?"*
- **Item 82:** *"Yes. We need to be pursuing that which follows our work. That which is ruled out or ruled against
  only exists to shape the current argument's strength"*. So this file leads with what follows the work, and keeps what
  is ruled out as the boundary that gives it strength. The warp's v is read as the shape's **strength**: Alcubierre's
  v_s sets how strongly space is curved (R ∝ v_s²). *First written* "speed".

M's hypotheses are carried as hypotheses, never as results. O9 stays OPEN.

Every number is printed by `escape.py`:
- `--selftest`, on the coarse grid;
- `--study table | controls | field | all`, which prints every number in the table and in §3, one JSON line per run.
  *First written* "(`--selftest` coarse grid; `--full` resolution study)". `--full` did not print the finer-grid,
  direction, box or field numbers; they had been run outside the file.

Status:
- **Selftest:** 14/14 checks: 3 genuine controls, 3 contrasts, and 8 STRUCTURAL lines printed and not counted. *First
  written* "13/13 checks, 4 of them controls". Two of those "controls" were contrasts (History).
- **Verification:** verified once, with its findings applied (History).

## How it was tested

**By hand, where a deduction closes:** routes A, C and D, and the identities of route S.

**By an exact numerical test, where it does not.** On a mirror-symmetric plane, the plane's matter must meet three
conditions from the plane's Gauss and Codazzi equations (READ, SMS), on the *exact* warp metric at any strength:
- it is conserved;
- its trace is fixed by the plane's curvature R;
- it keeps the null energy condition in every direction.

These conditions are linear, so whether such matter exists is a **linear program**:
- It is solved on an (X, s) grid in the bubble's own frame, with the null condition checked on 14–26 sampled directions.
- The measure is the least total violation V of the null condition. V = 0 means such matter exists; V > 0 means it does
  not.
- Sampling the condition makes V a lower bound on the true violation.
- Restricting to matter that is steady, symmetric about the axis and without swirl about it loses nothing. The metric
  has those symmetries and the measure is convex, so averaging any solution over them gives one at least as good.

**Control.** The engine finds conserved, localised matter that keeps the null condition and has positive energy (its
own witness). Imposing that matter's trace as the target must give V = 0, and it does on both planes (V = 0.0). So a
positive V is not built into the problem by the edge or the grid. This control does not settle the grid's continuum
limit (H-GRID).

**Checks that cannot fail on their own** (a formula evaluated on another case) are labelled CONTRAST, not CONTROL.

## What follows the work

- **1. A shape with zero curvature scalar needs no matter on either plane, ours included (route S; "ours" under
  H-RS1).** *First written* "A shape that does not move".
  - Bronnikov and Kim's static throats: computed, both have **R = 0**. The plane reads them as matter breaking the null
    condition (G_kk < 0, a geometric statement; example 1: ρ + p_r = −r₀/(8πr³)).
  - With **no matter on the plane at all**, every condition is met exactly, for either sign of the tension: the Gauss
    trace (R = 0), conservation, and the null condition. The bulk holds only its vacuum energy, and its Weyl term
    carries the whole reading.
  - **Here the demand is removed, not relocated.** For these shapes this answers, locally, the question SIGNDIM S7 left
    OPEN (whether the bulk needs anything beyond its vacuum energy): it does not.
  - A throat joins two asymptotic regions with no motion of the shape. *First written* "joins two positions". They are
    two places in one universe only if identified, and the static solution does not supply that.
  - In the board's terms this is a candidate counterpart of H-HIGHER-CORRIDOR (position 1, then position 2) and of
    H-NO-SPEED. For H-NO-SPEED the sharper statement is that **what passes is R = 0**, not the absence of motion. A static
    shape with R ≠ 0 still needs plane matter, while a moving irrotational shape with R = 0 everywhere would pass too
    (OPEN).
  - Its exotic reading on our plane is the bulk's: H-SIGN-BY-DIMENSION, under its named reading. Signals still cross it
    at light speed locally.
  - Locally the bulk exists (analytic theorems, weakly protected: Anderson). Globally, "a complete model requires
    knowledge of the full 5-dimensional space-time" (BK p.6), which is OPEN.
- **2. A moving shape's total is decided by its vorticity (route S).** *First written* "What decides a moving shape is
  its vorticity, not its speed".
  - Computed, exactly, for every warp of Alcubierre's and Natário's kind (unit lapse, flat slices, any shift N falling
    off faster than 1/r², any time dependence): **R = ½|∇×N|² + total derivatives**, so ∫R d³x = ½∫|∇×N|² ≥ 0 at every
    strength.
  - **Prior art:** the integral statement is Santiago, Schuster and Visser's eq. 7.17 (2105.03079, p.23,
    verifier-READ): ∫ρ d³x = −(1/32π)∫ω·ω ≤ 0, with ∫R = −16π∫ρ. Their eq. 4.6 (p.11) is the same structure for the
    density. The pointwise identity for R is the board's own.
  - **What it answers, and how far.**
    - The identity holds at every strength.
    - Reading ∫R as the plane matter's total energy uses bulkwarp's W3 (P-LEADING, H-BOUNDED, H-LOCALISED,
      P-VACUUM-BULK), so it holds at leading order in v.
    - Above light strength the negative-plane result rests on the engine, not on the identity.
    - Point by point, strength does appear: the positive plane's residue changes near v = 1 (provisional, H-GRID).
  - So item 81 is answered at the level of totals: strength enters only through the vorticity it carries. *First
    written* "That is the whole content of the energy test. Light speed does not enter".
  - An irrotational shape has ∫R = 0. Matter keeping the null condition would then have to vanish (W3's premises), so the
    shape needs R = 0 at every point. Irrotational warps exist in the literature: Lentz, and Fell–Heisenberg, with a
    shift that is a gradient. SSV show they break the null condition in 4D (p.28). That binds the plane's *reading*, not
    the plane's matter. *First written* "irrotational warps in the literature, unread".
  - Whether a localised, moving, irrotational shape with R = 0 everywhere exists is OPEN.
- **3. A field in the bulk can carry a shape on either plane, locally (route A; Anderson's objection carries).** *First
  written* "can carry any shape on any plane".
  - The null energy condition does not fix the sign of the field's normal stress. Computed: a scalar with a gradient
    along the plane keeps the null condition everywhere, with T_nn < 0.
  - **A field with a potential** carries the shape with no plane matter at all, at every strength. Its normal stress Ψ
    takes the whole trace point by point, and its net amount is positive (∫Ψ = ∫R).
  - **A field without a potential** (gradient energy only):
    - Below light strength it rescues the negative plane, needing ℓ∫ψ on the plane of at least |E_Alc| at leading
      order. *First written* "within about one bulk curvature length ℓ of the plane", which was an assumed profile.
    - It never rescues the positive plane below light strength (infeasible).
    - **Above light strength its Ψ can take either sign.** In the bubble's frame (d_∥φ)² = (1 − β²)φ_X² + φ_s², and
      β > 1 outside the bubble. A field pattern moving faster than light, made of a field that keeps the null condition,
      has a timelike gradient there.
    - *First written* "above light speed a gradient-only field does not rescue the negative plane (infeasible at
      v = 1.5)". That run imposed Ψ ≥ 0 where the physics does not.
    - With Ψ left free where β > 1, both planes are feasible at v = 1.5 and 3. This is a pointwise relaxation: whether a
      field φ realises that Ψ is OPEN. **It is a candidate place where light strength enters** (item 81).

    | strength v | negative plane: least ∫Ψ (∫R) | positive plane |
    |---|---|---|
    | 0.1 | 0.119 (0.054): 2.2× | infeasible |
    | 0.5 | 3.18 (1.34): 2.4× | infeasible |
    | 0.9 | 11.75 (4.35): 2.7× | infeasible |
    | 1.5, Ψ ≥ 0 imposed | infeasible | 6.84 (12.08): 0.57× |
    | 1.5, Ψ free where β > 1 | net 11.54 (0.96×), ∫\|Ψ\| = 73.3 | net −0.94, ∫\|Ψ\| = 5.50 |
    | 3.0, Ψ ≥ 0 imposed | infeasible | 14.28 (48.32): 0.30× |
    | 3.0, Ψ free where β > 1 | net 47.4 (0.98×), ∫\|Ψ\| = 293.7 | net 0.67, ∫\|Ψ\| = 9.84 |

    Coarse grid, `--study field`. With Ψ free, the program minimises ∫|Ψ|; "net" is ∫Ψ.
  - **Below light strength the field holds net positive Ψ of the order of the warp's negative energy,** positive energy
    located in the bulk. The demand is relocated, not reduced.
    - **This is a literal instance of item 74's form:** positive energy in the higher dimension, read on the plane as
      the warp's negative energy.
    - **H-SIGN-BY-DIMENSION is a candidate under this second reading.** Unlike bulkwarp's W4, where the positive energy
      was the plane's matter, here it is genuinely the bulk's.
    - Above light strength the net amount is no longer of one sign on the positive plane.
  - The stabilising field (Goldberger–Wise) couples to the planes, which adds freedom. Whether its own profile could
    supply this is OPEN. Its authors set its back-reaction aside "for the computation of V(r_c)" (p.5). *First quoted*
    without those words, which carry its scope.
- **4. A thick plane must be a positive one (route D).**
  - Computed: the bulk keeps the null energy condition only where the warp factor bends down (A'' ≤ 0).
  - DeWolfe et al. READ the same: "A'' ≤ 0 using only the weakest of positive energy conditions" (p.23) and "Only
    positive tension brane configurations can be smoothed" (p.3).
  - They also hold the *thin* negative plane consistent. The sentence continues "Nevertheless a negative tension brane is
    consistent with micro-" (p.3; it runs onto p.4, not READ). With an orientifold it "does not introduce difficulties
    with negative kinetic terms or unboundedness of energy because it is just part of a background, not something which
    can be dynamically created anywhere in space" (p.7).
  - Thickening our negative plane moves the violation into the bulk. A thick positive plane returns the question to the
    positive plane.

## What is ruled out, as the boundary

- **Matter keeping the null condition cannot carry a vortical shape on a negative-tension plane in a bulk of vacuum
  energy alone,** at any strength tried on the exact metric. On the positive plane a residue remains below light
  strength:

  | strength v | positive plane V (grids 20, 28, 40) | negative plane V | scale N·∫R (grid) |
  |---|---|---|---|
  | 0.1 | 0.169 → 0.092 → 0.083 | 0.917 → 0.894 → 0.879 | 0.75 → 0.80 → 0.80 |
  | 0.5 | 6.47 → 4.11 → 3.66 | 19.6 → 17.9 → 17.3 | 18.8 → 20.1 → 20.0 |
  | 0.9 | 19.8 | 40.1 | 60.9 |
  | 1.5 | 1.11 → 0.36 | 82.8 → 76.9 | 169 → 181 |
  | 3.0 | 4.15 | 535 | 677 |

  The scale is N_dir times the grid's own ∫R, so it moves with the grid. The Simpson value at v = 0.1 is 0.80 (B1).
  *First written* with the scale column mixing the two. The box bound on the matter is reached in none of these runs.

  - **The negative plane.**
    - At v = 0.1 its violation sits at or above the deficit bulkwarp.py's Laue argument predicts.
    - Above light strength it still fails, and the flat-space reversal does not occur. V/(N∫R) falls from about 1.1 at
      v = 0.1 to about 0.43 at v = 1.5 and 0.79 at v = 3.
    - *First written* "Above light strength nothing changes".
    - Under H-RS1 and P-VACUUM-BULK this plane is ours.
  - **The positive plane.**
    - Below light strength it shows a residue that does not fall to zero across three grids: provisional, H-GRID.
    - At v = 1.5 its residue falls with resolution, 1.11 → 0.36 (two grids).
    - Extrapolating gives floors of about 0.08 at v = 0.1 and 3.5 at v = 0.5. The implied orders are about 5–6, so the
      data are not in the asymptotic regime. A power law at order 1 or 2 gives 0.062–0.075 and 2.6–3.2. A nonzero floor
      is plausible, not shown.
    - The residue is the same with 26 directions (0.180 at grid 28, against 0.092 with 14; 12% of its scale) and with a
      larger box (box 4, grid 37: 0.103, 13%).
    - *First written* "Below light strength the positive plane fails point by point too … above it, it passes". In a
      vacuum bulk, bulkwarp.py's open sufficiency question stays OPEN, leaning no below light strength, subject to the
      grid.
- **Sustained radiation does not get round the test (route C).**
  - Computed: the trace fixes everything that leaves the wall to be traceless. Massless radiation, and traceless
    mixtures that keep the null condition (dust with stiff matter, for example), can escape. Single-kind massive ejecta
    cannot. *First written* "Only massless radiation can escape".
  - For the total stress the general virial holds: d²I/dt² = 2∫τ_ii.
    - Traceless, separately conserved escaping matter has I'' = 2E.
    - Radiation emitted from the origin with any history has I'' = 2E.
    - Emitted from the wall at R_b: I'' = 2E + 2R_bP + R_b²P′ (computed). The extra terms are its exchange with the
      massive part.
    - *First written* "the massive part keeps the ordinary virial", which holds only for emission from the origin.
  - Sustained radiation drains the massive part without limit. On a vacuum-bulk plane nothing resupplies it, so route C
    reduces to route A.

## For M

- **A static throat, a candidate counterpart of your corridor (H-HIGHER-CORRIDOR), passes locally on either plane, ours
  under H-RS1, with nothing on the plane.**
  - Its curvature scalar is zero. Our plane reads its exotic energy, and the bulk supplies it through its Weyl
    curvature, holding only its vacuum energy.
  - The demand is removed, not relocated.
  - What passes is R = 0. Whether a global bulk exists is OPEN (BK p.6), and so is whether the throat's two regions are
    one universe.
  - *First written* "Your corridor, as a shape that does not move, passes on our plane with nothing on the plane at all".
- **For shapes that move, the total is set by vorticity.** The identity ∫R = ½∫|∇×N|² holds at every strength (prior
  art: SSV eq. 7.17).
  - Reading it as the plane's energy is leading order.
  - Above light strength the engine decides.
  - Point by point, strength appears.
  - *First written* "speed is not what matters … exactly and at every strength".
- **A field in the bulk carries a shape locally.**
  - Below light strength it carries the shape with positive field energy of the warp's size, located in the bulk. That
    is item 74's form, and H-SIGN-BY-DIMENSION is a candidate under that reading.
  - Above light strength a gradient-only field's normal stress takes either sign. That is a candidate place where light
    strength enters your question (item 81). OPEN, as a relaxation.
- **What is ruled out shapes this.** On a negative-tension plane with nothing but vacuum in the bulk, well-behaved
  matter cannot carry a swirling shape at any strength tried.
  - That is decisive on our plane under H-RS1 and P-VACUUM-BULK.
  - On the positive plane the question stays open, leaning no below light strength.
  - The clean routes are a shape with zero curvature scalar (the throat) and a field in the bulk.
  - *First written* "decisive on our plane, and holds more weakly on the other".

## Named hypotheses and premises

- **Premises:** P-VACUUM-BULK and its relaxations; P-LEADING (matter far below the tension); H-LOCALISED; H-BOUNDED.
- **H-ESC-ILLUSTRATIVE:** σ = 4, R = 1.
- **H-GRID:** the finite-volume discretisation. The resolution, direction and box studies are its tests; the witness is
  its control.
- **P-SCIPY:** scipy's HiGHS solver.
- **The box bound M** on each matter component is named and reported. It is reached in none of the main runs.
- **Carried:** H-RS1; H-SIGN-BY-DIMENSION's two named readings (the tension's sign; positive energy located in the bulk).
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR and H-NO-SPEED.

## OPEN

1. A global bulk for the static throat (BK p.6), and whether its two asymptotic regions are one universe.
2. A moving irrotational shape with R = 0 everywhere. Irrotational warps exist (Lentz; Fell–Heisenberg; SSV); none is
   yet shown to have R = 0.
3. A bulk field realising the needed normal stress globally: the stabilising field's own profile and back-reaction.
4. Above light strength, a gradient-only field realising the relaxed Ψ (a φ with that mixed-sign stress).
5. The positive plane's residue at finer grids (H-GRID).
6. Not yet READ: induced gravity, Gauss–Bonnet, asymmetric embedding, plane density near the tension (from
   bulkwarp.py).

## History (verifier, 2026-10-06; first-written claims kept above, each where it stood)

- **Reproducibility.** The finer-grid, 26-direction, larger-box and field numbers were run outside `escape.py`.
  `--study` now prints every one.
- **Ψ ≥ 0 at v > 1.** It was imposed where a gradient-only field's stress takes either sign, so the "infeasible at
  v = 1.5" result is withdrawn as a result. It was replaced by the relaxation, which is feasible.
- **"The whole content … light speed does not enter".** Too strong: the identity is exact, but reading it as energy is
  leading order.
- **"A shape that does not move" and "joins two positions".** Replaced by R = 0, and by two asymptotic regions.
- **"Your corridor … passes".** H-HIGHER-CORRIDOR was treated as identified, and "ours" lacked H-RS1.
- **The positive plane's pointwise failure and pass were stated as findings.** They are provisional. A feasibility
  control was added.
- **"Above light speed nothing changes"** is corrected in B2.
- **Route C.** "Only massless radiation", and the massive part's virial with emission from the wall.
- **Quotes.** GW p.5 was cut before "for the computation of V(r_c)". DFGK's p.3 continuation and p.7 are now carried.
- **Premises named** for S2, for A2's condition (stated without a profile), for "decisive on our plane", and for
  "carries any shape" (locally).
- **Prior art.** SSV 2105.03079 had not been cited. Irrotational warps moved from unread to READ (verifier-READ).
- **Selftest labels.** Two "controls" were contrasts. B1's v² ratio was an identity and is now STRUCTURAL. The label
  "CONTROL: ENGINE CONTROL:" was doubled.
