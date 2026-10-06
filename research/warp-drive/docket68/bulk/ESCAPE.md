# The four routes, and the shape that does not move (M-RULINGS items 80–82; READ, deduced and computed; not verified; not seated; 2026-10-06)

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

Every number is printed by `escape.py` (`--selftest` coarse grid; `--full` resolution study).
- **Selftest:** 13/13 checks, 4 of them controls, with 7 STRUCTURAL lines printed and not counted.
- **Verification:** not yet verified.

## How it was tested

**By hand, where a deduction closes:** routes A, C, D, and the identities of route S.

**By an exact numerical test, where it does not.** On a mirror-symmetric plane, the plane's matter must meet three
conditions from the plane's Gauss and Codazzi equations (READ, SMS), on the *exact* warp metric at any strength:
- it is conserved;
- its trace is fixed by the plane's curvature R;
- it keeps the null energy condition in every direction.

These are linear, so whether such matter exists is a **linear program**. It is solved on an (X, s) grid in the bubble's
own frame, with the null condition checked on 14–26 sampled directions. The measure is the least total violation V of
the null condition: V = 0 means such matter exists, V > 0 means it does not. Sampling the condition makes V a lower
bound on the true violation.

## What follows the work

- **1. A shape that does not move needs no matter on either plane, ours included (route S).**
  - Bronnikov and Kim's static throats join two positions. Computed: both have **R = 0**, and the plane reads them as
    matter that breaks the null condition (example 1: ρ + p_r = −r₀/(8πr³) < 0).
  - With **no matter on the plane at all**, every condition is met exactly, for either sign of the tension: the Gauss
    trace (R = 0), conservation, and the null condition. The bulk holds only its vacuum energy, and its Weyl term
    carries the whole reading.
  - No speed enters. In the board's terms this is a candidate counterpart of H-HIGHER-CORRIDOR (position 1, then
    position 2) and of H-NO-SPEED (nothing travels the shape). Its exotic reading on our plane is the bulk's, which is
    H-SIGN-BY-DIMENSION under its named reading. Signals still cross it at light speed locally.
  - Locally the bulk exists (analytic theorems, weakly protected). Globally, "a complete model requires knowledge of
    the full 5-dimensional space-time" (BK p.6), which is OPEN.
- **2. What decides a moving shape is its vorticity, not its speed (route S).**
  - Computed, exactly, for every warp of Alcubierre's and Natário's kind (unit lapse, flat slices, any shift N, any
    time dependence): **R = ½|∇×N|² + total derivatives**. So ∫R d³x = ½∫|∇×N|² ≥ 0.
  - That is the whole content of the energy test. Light speed does not enter, which answers item 81 within this class.
  - An irrotational shape has ∫R = 0. Matter keeping the null condition would then have to vanish, so the shape needs
    R = 0 at every point. Whether a moving irrotational shape with R = 0 exists is OPEN.
- **3. A field in the bulk can carry any shape on any plane (route A).**
  - The null energy condition does not fix the sign of the field's normal stress (computed: a scalar with a gradient
    along the plane keeps the null condition everywhere, with T_nn < 0).
  - **A field with a potential** carries the shape with no plane matter at all, at every strength. Its normal stress
    takes the whole trace point by point, and its net amount is positive (∫Ψ = ∫R).
  - **A field without a potential** (gradient energy only) rescues the negative plane at low strength. On the coarse
    grid, ∫Ψ is 2.2–2.4 × ∫R at v = 0.1 and 0.5. It rescues the positive plane above light strength, with ∫Ψ ≈ 0.6 ×
    ∫R at v = 1.5 and 0.3 × at v = 3.
  - **In every case the field holds net positive energy of the order of the warp's negative energy.** The demand is
    relocated into positive energy in the bulk, not reduced.
  - The stabilising field (Goldberger–Wise) couples to the planes, which adds freedom. Whether its own profile could
    supply this is OPEN; its authors neglected its back-reaction (p.5).
- **4. A thick plane must be a positive one (route D).** Computed: the bulk keeps the null energy condition only where
  the warp factor bends down (A'' ≤ 0). DeWolfe et al. READ the same: "A'' ≤ 0 using only the weakest of positive energy
  conditions" and "Only positive tension brane configurations can be smoothed". Thickening our negative plane moves the
  violation into the bulk. A thick positive plane returns the question to the positive plane.

## What is ruled out, as the boundary

- **Matter keeping the null condition cannot carry a vortical shape on our plane in a bulk of vacuum energy alone,** at
  any strength tried on the exact metric:

  | strength v | positive plane V | negative plane V | scale N·∫R |
  |---|---|---|---|
  | 0.1 (grids 20, 28, 40) | 0.169 → 0.092 → 0.083 | 0.917 → 0.894 → 0.879 | 0.80 |
  | 0.5 (grids 20, 28, 40) | 6.47 → 4.11 → 3.66 | 19.6 → 17.9 | 18.8–20.1 |
  | 0.9 | 19.8 | 40.1 | 60.9 |
  | 1.5 (grids 20, 28) | 1.11 → 0.36 | 82.8 → 76.9 | 169–181 |
  | 3.0 | 4.15 | 535 | 676 |

  - At v = 0.1 the negative plane's violation sits at or above the deficit bulkwarp.py's Laue argument predicts. Above
    light strength nothing changes: the reversal a flat-space identity suggested does not happen on the real metric.
  - **Below light strength the positive plane fails point by point too, though far more weakly; above it, it passes.**
    At v = 1.5 its residue falls fast with resolution (1.11 → 0.36, 0.2% of the scale), as discretisation error does. Its residue does not fall to zero: it
    extrapolates to about 0.082 at v = 0.1 (10% of the scale) and about 3.5 at v = 0.5 (18%). It is the same with 26
    directions (12%) and with a larger box (13%). In a vacuum bulk, bulkwarp.py's open sufficiency question gets a
    provisional answer of no, subject to the grid.
- **Radiation does not get round the test (route C).**
  - Computed: the trace fixes everything that leaves the wall to be traceless. Only massless radiation can escape, and
    massive ejecta cannot.
  - Computed for any emission history: radiation's moments obey I″ = 2E, so the massive part keeps the ordinary virial.
  - Sustained radiation needs an unlimited energy supply, which on a vacuum-bulk plane nothing provides, so route C
    reduces to route A.

## For M

- **Your corridor, as a shape that does not move, passes on our plane with nothing on the plane at all.** A static
  throat between two positions has zero curvature scalar. Our plane reads its exotic energy, and the bulk supplies it
  through its Weyl curvature, holding only its vacuum energy. No speed enters anywhere.
- **For shapes that do move, speed is not what matters; vorticity is.** The energy test depends only on how much the
  shape swirls (½∫|∇×N|²), exactly and at every strength.
- **A field in the bulk carries any shape,** with positive field energy of the warp's size, so the bulk pays in
  positive energy.
- **What is ruled out shapes this:** on a plane with nothing but vacuum in the bulk, well-behaved matter cannot carry a
  swirling shape. That is decisive on our plane, and holds more weakly on the other. The two clean routes are a shape
  with zero curvature scalar (the throat) and a field in the bulk.

## Named hypotheses and premises

- **P-VACUUM-BULK and its relaxations; P-LEADING (matter far below the tension); H-LOCALISED; H-BOUNDED.**
- **H-ESC-ILLUSTRATIVE:** σ = 4, R = 1.
- **H-GRID:** the finite-volume discretisation; the resolution, direction and box studies are its controls.
- **P-SCIPY:** scipy's HiGHS solver.
- **Carried:** H-RS1; the reading of H-SIGN-BY-DIMENSION as the tension's sign.
- **M's:** H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR and H-NO-SPEED.

## OPEN

1. A global bulk for the static throat (BK p.6).
2. A moving irrotational shape with R = 0 everywhere (irrotational warps in the literature, unread).
3. A bulk field realising the needed normal stress globally: the stabilising field's own profile and back-reaction.
4. The positive plane's residue at finer grids (H-GRID).
5. Not yet READ: induced gravity, Gauss–Bonnet, asymmetric embedding, plane density near the tension (from
   bulkwarp.py).
