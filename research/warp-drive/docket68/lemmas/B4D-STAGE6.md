# B4d stage 6: the two planes together (computed and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage6.py`, selftest 7/7, about 2 minutes.

## What you said

- **Item 165:** *"Of course. Continue"*. That was your answer to the board's next step: the negative-tension plane and a
  positive-tension plane together, as one object.
- **Item 139 (1):** *"yes"*. Position 2's plane is negative, a quarter of ours in size, and ours is positive: +4/3 and
  −1/3 of the one-plane value.
- **Item 127 (1):** *"yes"*. The planes coincide, the extra dimension included.
- **Item 141:** the planes are static.
- **Items 117/120:** *"the NEC only ever appears to break, but never does"*.
- **Clause (B):** the plane carries no matter.
- **Item 138:** the bulk is multi-universal, each universe under its own laws.

## Where stage 5 left it

With eq. (17) on a plane, the bulk turns singular within 8–16 clocks on any side where the warp decays away from the
plane. On a side where the warp grows, it is regular on the evidence. This stage asks which of the two your rulings
allow.

## What follows

**J1. What a plane can be, carrying eq. (17) and no matter** (computed, exact).
- **The constraint on each side.** The bulk's extrinsic curvature is K = a·h + Π, with Π the part that differs by
  direction. Eq. (17)'s plane has zero scalar curvature. So the bulk's constraint on each side is 12a² − Π·Π = 12/ℓ²,
  and **|a| ≥ 1/ℓ**, with equality only when Π = 0.
- **No matter on the plane** means the jump across it is pure tension, so the Π on the two sides cancel.
- **The tensions that result** (in units of the one-plane value λ_RS):

  **σ/λ_RS is 0, or ±√(1 + Π·Π ℓ²/12): never strictly between 0 and 1 in size.**

- **Control.** With Π = 0 and the warp decaying on both sides, this is Randall–Sundrum's plane, σ = +λ_RS.
- **What a means.** If a < 0 the warp decays away from the plane: stage 5 F2, singular. If a > 0 it grows: stage 5 F6,
  regular on the evidence.

**J2. Your coincident pair acts as a positive plane, and the warp decays on both its sides** (computed).
- **What the junction sees.** By your 127 the two planes are in one place, so the junction sees only their summed
  tension: +4/3 − 1/3 = **+1** λ_RS (your 139; `b5_positive.py` B5a).
- **What that forces.** By J1, +1 forces Π = 0, with the warp decaying on both sides.
- **So both sides are stage 5 F2's bulk,** singular within 8–16 clocks.

**J3. Neither sheet can stand alone as the regular side** (computed).
- **Position 2's sheet alone, at −1/3, is not in J1's set.** No matter-free plane carrying eq. (17) can have that tension.
- **Stage 5 F6's regular plane** (warp growing on both sides) has tension exactly −1 λ_RS, three times your 139's.

**J4. Pulling the sheets apart costs matter that breaks the NEC** (computed; exact at small separation).
- **The setup.** To keep the regular side, put eq. (17) on a negative plane at y = 0 and close the slab with a positive
  plane at y = d. This is Randall–Sundrum I's arrangement.
- **What that closing plane must carry:**
  - **Exactly:** ρ + p_r = R⁽⁴⁾_kk·(d − 3d²/ℓ) + O(d³), with R⁽⁴⁾_kk < 0. This is stage 5 F5 under the exact symmetry
    y → −y, e → −e.
  - **Numerically:** negative at r = 2.15m and 3m for every d from 0.1m to 4m, at ℓ = 2m and m. Both Padé orders agree,
    it shrinks with d, and the plane's tension tends to +λ_RS.
- **So, however far it is placed, the closing plane carries real matter breaking the NEC.** Your 117/120 rule that out.
- **The separation is a problem too.**
  - It runs against your 127.
  - It is a free separation, the radion. `b5_positive.py` B5c rules the radion out only because the separation is zero
    (standard, not READ).

**J5. Giving each universe its own ℓ (your 138) does not change the sign** (computed; STRUCTURAL).
- **The result.** With different ℓ on the two sides and any anisotropy, a plane whose warp grows on both sides has
  tension −(√(1/ℓ_L² + Π·Π/12) + √(1/ℓ_R² + Π·Π/12))/2 < 0.
- **So your 139's positive composite has a decaying side somewhere.**

## Verdict

- **On your rulings as they stand, the corridor's bulk is not regular through the write.**
  - Your coincident pair (127, 139) acts as a positive plane, with the warp decaying on both sides. Stage 5 F2 makes that
    bulk singular within 8–16 clocks.
  - The regular side needs a negative total tension (J1, J5), which your 139 does not give.
  - The other way to reach it is to pull the sheets apart, which your 127 rules out, and that puts NEC-breaking matter on
    the closing plane, which your 117/120 rule out.
- **The conjunction:**
  - **yours:** 127, 139, 117/120, clause (B);
  - **the board's:** eq. (17) on the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD), a vacuum bulk, B4b's
    locally analytic class, the column r = 2.15m and the ℓ values tested, and stage 5's readings.
- **Your inclination 161 does not hold on that conjunction.**
- **Each of these would still let it hold:**
  1. **Anisotropic junction data with each universe's own ℓ** (your 138). J5 forces a decaying side somewhere but leaves
     Π free, and whether a bulk built from data with Π ≠ 0 is regular has not been computed.
  2. **A bulk that is not vacuum** (your 158 (4)). `b5_positive.py` B5b's smooth wall is one: it carries a field in the
     bulk.
  3. **The plane's geometry not being eq. (17) while the README passes.**
  4. **A bulk outside the analytic class.**
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## Named hypotheses

- **Yours:** 117/120, 127, 138, 139, 141, 165; clause (B).
- **The board's:**
  - H-EQ17-ON-PLANE-THROUGH-HOLD;
  - a vacuum bulk;
  - B4b's locally analytic class;
  - the readings of `b4d_stage5.py`;
  - `b5_positive.py` B5a's summed tension at the coincidence (Israel; standard, not READ).
