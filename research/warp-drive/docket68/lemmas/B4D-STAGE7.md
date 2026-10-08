# B4d stage 7: the corridor across both planes (computed and deduced; verified once; not seated; 2026-10-08)

*First headed* "(… not verified; not seated …)". The instrument is `b4d_stage7.py`, selftest 7/7, about 15 seconds.

The first draft left one arrangement open: our outer bulk growing and position 2's plane curved. Its verifier showed
three problems with that:
- the arrangement rested on an undefined unit;
- it left out that the slab is itself stage 5's singular case;
- it applied an identity where the stage's own K2 forbids it.

The stage now enumerates every branch, and finds a decaying outer bulk in each. All findings are applied (History).

## What you said

- **Item 166:** *"Both planes at once"*.
- **Item 139 (1):** *"yes"*: ours is +4/3, position 2's −1/3. These are `multiplane.py` M4's figures.
- **Item 152 (1):** *"two separate positions connected by/reached through a dimension"*.
- **Item 127 (1):** *"yes"*: the planes coincide.
- **Item 138:** each universe has its own laws.
- **Item 141:** the planes are static.
- **Clause (B):** the planes are free of matter.

## The arrangement

- **Eq. (17) sits on one plane.** K4 shows it makes no difference which, at small separation.
- **The slab** between the planes (AdS radius ℓ_s) is your 152's dimension and the corridor's throat.
- **Position 2's plane** sits at y = d.
- **Beyond each plane** lies its own universe's bulk: ℓ₁ for ours, ℓ₂ for position 2's.

## What follows

**K1. The slab** (computed, exact; a bound deduced).
- **It is singular itself, at a depth y_s.** The slab is the decaying side of the plane carrying eq. (17), so it is
  stage 5 F2's case. Its singular surface is at y_s ≈ 1.0m, 0.67m and 0.43m at ℓ_s = m, m/2 and m/4 (r = 2.15m).
  **So every arrangement needs d < y_s.**
- **Below that depth, the formula.** At position 2's plane, a_s = 1/ℓ_s + (R_ab R^ab/12)·d³·(1 + 5d/ℓ_s) + O(d⁵).
  Eq. (17)'s Ricci-squared is 2(3r² − 8r + 6)/(r⁴(2r − 3)⁴), which is positive at every r.
- **A bound at every depth.** Raychaudhuri gives a_s ≥ 1/ℓ_s for every d < y_s (deduced; it needs diagonal K).
- **a_s depends on r.** That is shown for all small d, and is generic for every d < y_s.

**K2. No parallel, matter-free position-2 plane exists at any nonzero tension** (computed, exact).
- **One relation, pointwise.** Both sides share the plane's induced metric, so at each point
  a₂² = a_s² + 1/ℓ₂² − 1/ℓ_s².
- **Why the tension can't stay fixed.** A pure tension is constant, so a_s + a₂ must be constant, and that forces a_s
  constant. K1 says it is not. The one exception has zero tension.
- **So position 2's plane must curve, or carry matter.**

**K3. The outer bulks' trace parts sum negative** (an exact identity; its sign deduced).
- **The identity:** a₁ + a₂ = −κ²(σ₁ + σ₂)/3 − (a_s − 1/ℓ_s).
- **The sign.** It is negative at every d < y_s for your 139's positive total, on the parallel surface.
- **On a curved plane** the sign is not derived.

**K4. Every small-separation branch has a decaying outer bulk** (computed, exact arithmetic).
- **The setup.** At small d the outer data are nearly pure trace, so a₁ = ±1/ℓ₁ and a₂ = ±1/ℓ₂, and the tensions fix
  the rest.
- **Whose ℓ is the unit is a choice.** `multiplane.py` M4 measures your 139's tensions against the curvature beyond
  position 2 (ℓ₂): its code says "the one-plane (Z2) value at the outer curvature".

  | unit | position 2's tension | result |
  |---|---|---|
  | ℓ₂ (M4's) | −1/3 | ℓ_s = 3ℓ₂/5; **both outer bulks decay** |
  | ℓ₂ (M4's) | −1/6 | ℓ_s = ℓ₁ = 3ℓ₂/4; both decay. **This is M4's own geometry, the control** |
  | ℓ₁ | −1/3 | ours grows (ℓ_s = 3ℓ₁/11) and position 2's decays (ℓ₂ = ℓ₁/3); or both decay |
  | ℓ₁ | −1/6 | ours grows (ℓ_s = 3ℓ₁/11) and position 2's decays (ℓ₂ = 3ℓ₁/10); or both decay |

- **Where eq. (17) sits makes no difference:** ours, position 2's, or both give the same system at small d.
- **So every branch has an outer bulk that decays.**
  - **Ours** has pure-trace data, so it is stage 5 F2's case: singular.
  - **Position 2's** has data that differ from pure trace by an amount of order d, so it is F2 slightly perturbed:
    singular by continuity. That is a reading, H-F2-STABLE.

**K5. Your 139's −1/3 counts position 2's plane twice** (deduced; recorded, not repaired).
- **What the source gives.** By its verifier's reading of PRZ's jump condition (hep-th/0004028, p.3), a single sheet
  carries 12M³(k_R − k_L). PRZ print 24M³(k_R − k_L), which counts the plane's two images on the doubled space; the
  rule that the tensions sum to the one-plane value needs that count.
- **What one sheet carries.** Under stage 6's per-plane formula, M4's geometry gives one sheet **−1/6**, and K4's
  unit-ℓ₂ branch with −1/6 reproduces M4 exactly.
- **What it changes.** Stage 6's live route then reads ℓ₂ = 6ℓ, not 3ℓ. "A quarter of ours" is the doubled-space count.

## Verdict

- **With the corridor across both planes, and eq. (17) on either, every small-separation branch has an outer bulk that
  decays.** Its data are pure trace or nearly so, so it is singular: directly on our side (stage 5 F2), or by
  continuity on position 2's.
- **What is robust:**
  - no parallel, matter-free position-2 plane exists (K2);
  - our outer side decays unless ℓ_s < 3ℓ/8 (a₁ = 1/ℓ_s − 8/(3ℓ));
  - the slab is itself stage 5's singular case, so d < y_s.
- **What is still open:**
  1. **d close to the slab's own singular surface.** There a_s departs from 1/ℓ_s by an amount of order one, but the
     slab's curvature is 10³–10⁴ times the black string's.
  2. **Data that differ by direction** on the plane carrying eq. (17).
  3. **Curved planes,** beyond leading order.
  4. **Outer bulks that are not anti-de Sitter** (your 138).
- **Two questions for you, about your 139:** which universe's ℓ its figures are measured in (K4), and whether its
  −1/3 counts position 2's plane once or twice (K5).
- **The conjunction:**
  - **yours:** 139, 152/127, 138, 141, clause (B), 166;
  - **the board's:** diagonal K, a negative cosmological constant on every side, a vacuum bulk, pure-trace data on the
    plane carrying eq. (17), B4b's analytic class, H-F2-STABLE, and stage 5's tested ℓ range and column.
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## History (verifier, 2026-10-08)

**What the verifier confirmed independently.**
- Eq. (17)'s Ricci-squared in closed form, positive at every r.
- K1, derived analytically from the trace and traceless evolution.
- Both orientations.
- K2's pointwise relation.
- K3's identity.
- Your quotes.
- Selftest 5/5 at the time, in 14 s.

**Its findings, all applied:**

**MUST-FIX**
1. **The slab is F2's case.** So d < y_s; now in K1, K3 and the verdict.
2. **The unit ℓ was undefined, and the surviving branch depends on it.** M4 normalises to ℓ₂, and in that unit ours
   decays. Now K4 enumerates both units, and the unit is put to you.
3. **The verdict's premise was empty** (it described flat planes, which K2 forbids), **and K3 was applied on a curved
   plane.** The verdict is restated on what is robust.
4. **Missing escapes.** Data differing by direction at the plane carrying eq. (17), and the other placements of
   eq. (17). K4 now shows those placements give the same system at small d.

**SHOULD-FIX**
5. **139's −1/3 is a doubled-space count.** Now K5, recorded and put to you. Stage 6's J3 is noted.
6. **a_s ≥ 1/ℓ_s** now rests on Raychaudhuri at every d < y_s, with diagonal K named.
7. **"At every d"** is now "all small d; generically every d < y_s".
8. **"Flat" is defined** (parallel). K2 is strengthened to any nonzero tension, and a₂ cannot change sign.
9. **Selftest coverage.** K3's check is relabelled as an identity, and K4 tests the branches, including the control.
10. **Unnamed hypotheses** are now named: your 141, the slab's own ℓ_s, pure-trace data.
11. **F2's tested range** (ℓ = 2m to m/4, r = 2.15m) is stated.
12. **Position 2's outer bulk at small d** is F2 slightly perturbed: singular by continuity (H-F2-STABLE), not
    "uncovered".

**NOTE**
- **Stage 6's J2** carries over only through the summed tension. Its decay on both sides needs one ℓ.
- **The 2.15m and 5m checks** are at ℓ_s = m.
- **The selftest time** is about 15 s.

## Named hypotheses

- **Yours:** 127, 138, 139, 141, 152, 166; clause (B).
- **The board's:**
  - diagonal K;
  - a negative cosmological constant on every side;
  - a vacuum bulk;
  - pure-trace data on the plane carrying eq. (17);
  - B4b's locally analytic class;
  - H-F2-STABLE;
  - the unit of 139's figures (K4) and its image count (K5), both put to you;
  - the readings of stages 5 and 6.
