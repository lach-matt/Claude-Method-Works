# B4d stage 5: the corridor of fixed size through the write (computed and deduced; not verified; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage5.py`, selftest 9/9, about 2½ minutes.

## What you said

- **Item 163:** *"All together, one whole"*. The README is carried in and held as one whole, and the gas bound stands.
- **Item 162:** *"The throat doesn't change size"*.
- **Item 161:** *"my inclination is yes"*: the corridor stays regular while the README passes.
- **Item 160:** the corridor and the opening are the same object.
- **Items 115 (c) and 136 G:** the inflow is the README, and the README is the energy.
- **Clause (B):** the plane carries no matter.
- **Items 117/120:** *"the NEC only ever appears to break, but never does"*.

## What follows

**F1. A fixed size with an inflow is a through-flow** (STRUCTURAL, deduced).
- **The size.** On the plane, in the Vaidya form `opening.py` already uses, the trapping radius is r = 2m(v). So your
  fixed size means dm/dv = 0: no net flux.
- **The inflow.** By 115 (c) and 136 G the README's energy flows in, for at least the gas bound's 2.0×10⁵ clocks.
- **So an equal flux leaves.** The corridor is a steady through-flow from position 1 to position 2. This is the board's
  reading of 160, 162 and 163, named H-THROUGH-FLOW.
- **How strong.** Its flux is at most E/T, which is 5.0×10⁻⁶ of the corridor's mass per clock.

**F2. At every ℓ tested the static bulk still has a singular surface, and it sits nearer the plane as ℓ falls**
(computed; numerical evidence, not a bound).
- **How it was computed.** `b4_static.py`'s exact series at r = 2.15m, order 32 in y, with the Randall–Sundrum tension
  at finite ℓ.
- **One step that made the difference.** The warp factor is divided out first (X̃ = X·e^{2y/ℓ}, constant for the black
  string). A bare Padé in y shows spurious poles that wander from order to order. With the warp removed they settle.
- **The results** (y in units of m):

  | ℓ | singular surface y_s | three Padé orders | depth where K = 30 × black string | hold to reach it | hold to 0.95 y_s | K at 0.95 y_s |
  |---|---|---|---|---|---|---|
  | ∞ (control) | 2.58 | 0.05% apart | 2.00 | 16.6 clocks | 21.7 clocks | ~10⁴ |
  | 2m | 1.43 | 0.1% | 1.08 | 11.7 | 18.0 | ~10⁵ |
  | m | 1.0 | 6% | 0.81 | 10.2 | 14.9 | ≥ 4×10⁵ |
  | m/2 | 0.69 | 0.01% | 0.56 | 8.6 | 13.1 | ~10⁸ |

- **Three independent signs that it is real.**
  - The Padé orders agree, and the singularity appears as a near-real cluster of poles and zeros: the same cut
    `b4_static.py` found in the flat limit.
  - **Pringsheim** (standard, not READ): C̃'s coefficients keep one sign from order 24 to 32. A power series with
    coefficients of one sign is singular at the positive real point of its radius, and the root test agrees with y_s
    from above, within 12%.
  - **K climbs far above the black string's.** The comparison is K_bs = 40/ℓ⁴ + 48m²e^{4y/ℓ}/r⁶ (Chamblin–Hawking–Reall's
    form, standard, not READ). By 0.8 y_s, K is 13–67 times K_bs, and by 0.95 y_s 10⁴ times or more.
- **Controls.**
  - ℓ = ∞ reproduces `b4_static.py`'s surface, 2.50m at order 80. Order 32 sits 3% high.
  - Schwarzschild data at ℓ = m give the black string. The warp-divided series terminates, so there is no singular
    surface, and the instrument's K equals K_bs to 2×10⁻¹⁶.
- **Why it moves inward.** This is KSCALE's closure (stage 2) seen in the bulk. With r₀ ≫ ℓ the plane's geometry is 4D
  general relativity to O(ℓ²/r₀²) (Figueras–Wiseman). Eq. (17)'s deficit is an O(1) Weyl datum, and the bulk cannot
  carry it far.

**F3. The hold that reaches it** (computed).
- **What is measured.** Light from the plane down the r = 2.15m column, in far time: T = 2∫dy/√A, the double cone of
  `b4_static.py` S3 along one path. Any one path gives an upper bound on the earliest hold whose cone contains the point.
- **The result.** At every ℓ, the cone reaches curvature of 10⁵ or more within **13–22 clocks** (table above). The
  three orders agree within 1% (2% at ℓ = m/2), and the lapse A stays positive all the way.
- **What is not resolved.** The last 5% to the surface itself: the orders part there. A shows no sign of closing to a
  horizon, so there is no infinite-time escape on the evidence.
- **Control.** At ℓ = ∞ the column reaches K = 100 at 19.2 clocks. That is no earlier than `b4_static.py`'s 14.9 clocks,
  which is the minimum over all paths, as an upper bound must be.
- **Against the write.** 2.0×10⁵ clocks.

**F4. Over that hold the through-flow is quasi-static** (deduced; H-QUASI-STATIC-CORRIDOR, the board's).
- **How much changes.** Over 20 clocks the through-flow moves at most about 10⁻⁴ of the mass past any point.
- **What that gives.** The plane's data are eq. (17) to that order, so the bulk in the cone is the static bulk to that
  order.
- **The caution.** The y-problem is elliptic and Hadamard-ill-posed. Continuity in the data is a reading inside the
  locally analytic class, not a theorem.

**F5. A second plane below the surface would carry NEC-breaking matter, at finite ℓ too** (computed; STRUCTURAL at
small height).
- **The setup.** A mirrored plane at y = y_w closing the bulk: stage 1's D3, now at finite ℓ.
- **What it must carry.** ρ + p_r = −A_y/(2A) + B_y/(2B). The warp cancels, and so does any tension, your 139's negative
  one included.
- **Exactly:** ρ + p_r = R⁽⁴⁾_kk·(y_w + 3y_w²/ℓ) + O(y_w³), with R⁽⁴⁾_kk = −2(r − 2m)/(r²(2r − 3m)²) < 0. This is checked
  rationally at r = 3m for ℓ = 2m, m and m/2.
- **Numerically** it is negative at every r from 2.15m to 32m, for y_w up to y_s/2, at every finite ℓ.
- **So the plane would carry real matter that breaks the NEC.** Your 117/120 rule that out, and clause (B) already
  forbids matter on the plane.

## Verdict

- **On the board's readings, the corridor of 161–163 does not stay regular through the write.** Its bulk reaches
  curvature of 10⁵ or more, rising to a singular surface, within about 20 clocks at every ℓ tested. The write takes
  2.0×10⁵ clocks.
- **This refutes a conjunction, not your inclination by itself.** The conjunction:
  - eq. (17) on the plane through the write (H-EQ17-ON-PLANE-THROUGH-HOLD);
  - one mirrored plane with the Randall–Sundrum tension and no matter (clause (B), H-RS2-ONE-PLANE);
  - B4b's locally analytic class (Holmgren at linear order);
  - Padé and Pringsheim as evidence;
  - H-QUASI-STATIC-CORRIDOR and H-THROUGH-FLOW.
- **F5 closes one way round it:** a closing plane, under your 117/120.
- **What stays open** (each is a way your "yes" could still hold):
  1. **H-TWO-SIDED:** a plane with bulk on both sides.
  2. **A curved closing wall** y_w(r), whose bending terms might outweigh R⁽⁴⁾_kk.
  3. **A through-flowing plane whose geometry is not eq. (17).** A throat that carries a flux need not be the static
     extremal one. This is a change to the theorem's corridor, not to the bulk.
  4. **A bulk outside the analytic class.** Holmgren closes this only at linear order.
  5. **ℓ below m/2.** Not computed; the trend is for the surface to come nearer.
- **No status moves on this stage's account.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## Named hypotheses

- **Yours:** 115 (c), 117/120, 136 G, 139, 160, 161 (an inclination), 162, 163; clause (B).
- **The board's:**
  - H-THROUGH-FLOW;
  - H-QUASI-STATIC-CORRIDOR;
  - H-EQ17-ON-PLANE-THROUGH-HOLD;
  - H-RS2-ONE-PLANE;
  - B4b's locally analytic class;
  - the hypotheses of `o3_write.py`'s gas bound.
