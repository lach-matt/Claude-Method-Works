# B4d stage 7: the corridor across both planes (computed and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage7.py`, selftest 5/5, about 1 minute.

## What you said

- **Item 166:** *"Both planes at once"*. The corridor is one object across both planes, ours and position 2's, with the
  bulk between them as its throat.
- **Item 139 (1):** *"yes"*: ours is positive (+4/3), position 2's negative (−1/3).
- **Item 152 (1):** *"two separate positions connected by/reached through a dimension"*.
- **Item 127 (1):** *"yes"*: the planes coincide.
- **Item 138:** each universe has its own laws.
- **Clause (B):** the planes are free of matter.

## The arrangement

- **Our plane** (y = 0) carries eq. (17).
- **The slab** between the two planes is the throat, the dimension your 152 describes. It has its own ℓ_s.
- **Position 2's plane** sits at y = d.
- **Beyond each plane** lies that plane's own universe's bulk: ours beyond y = 0 (with ℓ₁), position 2's beyond y = d
  (with ℓ₂).

From stage 5: a side where the warp decays is singular within 8–16 clocks; a side where it grows is regular on the
evidence. From stage 6: a plane's tension is −3(a_L + a_R)/κ², where a is each side's trace part (a < 0 means the
warp decays).

## What follows

**K1. The slab, seen from position 2's plane** (computed, exact).
- **The formula.** Carrying eq. (17)'s data across the slab gives, at position 2's plane,

  **a_s(d, r) = 1/ℓ_s + (R_ab R^ab/12)·d³·(1 + 5d/ℓ_s) + O(d⁵).**

  Here R_ab is eq. (17)'s Ricci tensor. Computed: R = 0, and R_ab R^ab = 2/729 at r = 3m.
- **Checked.** It is exact at r = 3m for ℓ_s = 2m, m and m/2, and matches at 2.15m and 5m.
- **What matters.** It depends on r, and the correction is never negative.

**K2. A flat position-2 plane cannot carry your 139's tension without matter** (computed, exact).
- **One relation, pointwise.** Both sides of position 2's plane share its induced metric. So the constraint on each
  side, with no matter on the plane, gives at each point a₂² = a_s² + 1/ℓ₂² − 1/ℓ_s².
- **What that does to the tension.** The tension then changes whenever a_s changes. The one exception is ℓ₂ = ℓ_s with
  a₂ = −a_s, and that is zero tension.
- **So a flat plane cannot hold −1/3.** By K1, a_s changes with r at every separation d > 0. A flat position-2 plane at
  −1/3 must therefore carry matter, or curve.

**K3. The two outer bulks cannot both grow** (computed, an exact identity).
- **The identity.** With both planes' tensions fixed,

  **a₁ + a₂ = −κ²(σ₁ + σ₂)/3 − (a_s(d) − 1/ℓ_s).**

- **What it gives.** Your 139's total is +1, and a_s − 1/ℓ_s ≥ 0 (K1). So a₁ + a₂ < 0 at every separation: at least
  one outer bulk decays. At d = 0 (127 read as one place) this is stage 6's J2.
- **Which one.** a₁ = 1/ℓ_s − 8/(3ℓ), so our outer bulk grows exactly when ℓ_s < 3ℓ/8.
  - **If ours grows,** position 2's must decay in its trace. Its data differ by direction (Π₂ = −Π_slab), and that bulk
    has not been computed.
  - **If ours decays,** its data are pure trace, so it is stage 5 F2's case and singular.

## Verdict

- **With flat, matter-free planes at your 139's tensions, the corridor across both planes cannot be regular on every
  side.**
  - The outer bulks' trace parts sum negative at every separation (K3).
  - Our side, if it is the one that decays, is singular (stage 5 F2).
- **Only one arrangement is left:**
  - our outer bulk grows (ℓ_s < 3ℓ/8);
  - position 2's plane is curved, since K2 forbids it flat;
  - position 2's outer bulk decays in its trace but is built from direction-dependent data. Stage 5's evidence does not
    cover that case.
- **That bulk, and the curved plane that carries it, are B4d's next computation.**
- **The conjunction:**
  - **yours:** 139, 152/127, 138, clause (B), 166;
  - **the board's:** diagonal K, a negative cosmological constant on every side, a vacuum bulk, eq. (17) on our plane,
    B4b's analytic class, and stage 5's link between decay and singularity (at Π = 0).
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## Named hypotheses

- **Yours:** 127, 138, 139, 152, 166; clause (B).
- **The board's:**
  - diagonal K;
  - a negative cosmological constant on every side;
  - a vacuum bulk;
  - eq. (17) on our plane;
  - B4b's locally analytic class;
  - the readings of stages 5 and 6.
