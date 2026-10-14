# Lemma B4c on an ellipsoidal far surface (computed, READ and deduced; not verified; not seated; 2026-10-09)

The instrument is `b4c_far.py`: `--selftest` 13 of 13, and `--mutants` 35 of 35 caught (the run figures are under
"Re-run" below). It imports `b4_global.py`, `o3_write.py`, `ledger.py`, `bulk/kscale.py`, `../cosmo.py` and
`../address.py` by path, and reads the bank `b4_static.json`. It writes nothing into any other file. Folding it into
`warptheorem.py`, `WARPTHEOREM.md` and the cypher audit is left for later.

**Revised the same day.** Two separate AI sessions inside this project reviewed the first version. These were
in-project checks, not an outside review. One tried to refute it and one looked for overclaims. Every finding they
made was reproduced here and applied (list at the end). This revision has not had a separate-session check of its own.

## What you said (verbatim)

- **139 (1):** to the board's question whether position 2's plane is the negative-tension one, a quarter of ours, with
  ours positive, you answered *"1 - yes"*.
- **152 (1):** *"two separate positions connected by/reached through a dimension."*
- **152 (2):** *"I had not considered this yet. It could very well be possible, so let's consider this an option and
  check it."*
- **157:** *"we already have at least half the model, our current universe."*
- **158 (2):** *"Exactly as long as the write needs  I should think"*
- **160:** *"the corridor and the opening are the same object"*
- **162:** *"... The throat doesn't change size because the whole chain object only every takes on the size that
  contains the README upon opening. It is and always will be only the size that is needed to hold the object once and
  at once"*
- **163:** you chose *"All together, one whole"*.
- **166:** you chose *"Both planes at once"*.
- **179/180:** *"Let's approach this from a different angle. We know the corridor \*does not sit on either position's
  plane, it only bridges them. So one could surmise that the corridor is exclusive to the bulk."*
- **183:** you chose *"Yes: never violated as a pair"*. **187 (3):** you chose *"Seat both"*, which seated clauses
  (G) and (Z) as the board worded them. (G): *"the corridor sits in the bulk, on neither plane (179/180), with
  eq. (17) kept only as a plane's possible reading of the corridor's mouth"*. (Z): *""null energy never violated"
  holds net along each light ray (183)"*.
- **184:** *"There are no matter free planes"*
- **192:** *"this appears to be a question to put to the math language hierarchy cypher"*
- **194:** *"Disregard that last ruling. I want that question put to the cypher"*. Item 193 is withdrawn by 194, so the
  pair axiom is not carried here and input F5 is OPEN. Nothing in this lemma uses the withdrawn item.
- **195:** *"The README is not a pair"*
- **196:** *"Review all tasks running. Stop any that are no longer relevant. All questions get works through the
  cypher"*

## Plain words first

1. **Inside the board's far model, the shape problem is solved exactly.** Take an egg-shaped surface around the
   corridor: half-width U along our plane, depth W into the bulk, meeting the plane square-on. If W ≥ √3·U, it is
   strictly untrapped at every ℓ. That is proved (exact algebra, one inequality checked by z3), not scanned. The shape
   is a pure ratio, so it does not change with ℓ or with the README's size. **The surface's size does change:** U grows
   with the README.
2. **√3 is the exact line.** Below it the tip is trapped whenever ℓ is small enough. The item-186 checker's bracket,
   1.70 trapped and 1.74 untrapped, sits on either side of 1.7320508.
3. **The time part is not proved.** That the surface stays untrapped through the write needs global hyperbolicity (W2,
   not green) and a standard theorem the board has not read, and the model itself breaks that theorem's energy premise.
   After the closing there is only an estimate, and for very large ℓ it needs ℓ to be bounded after all.
4. **The far model is not yours, and seated (Z) excludes its key part.** The model puts the corridor's throat on our
   plane and gives both positions one positive-tension plane. Your (G), 139 (1) and 166 say otherwise. The column that
   joins the two positions through the bulk carries net negative null energy along every light ray through it, for
   every depth profile the instrument covers. Seated (Z) forbids that. So no column of that kind can be supplied later
   to turn B4c green.
5. **B4c stays a READING and is not green.** On this model it cannot turn green. What B4c needs is a far boundary in a
   bulk consistent with (Z), (G), 139 (1) and 166, and that is OPEN.

## The result

Units are m = 1 and c = ℓ/m. T_E is the surface {(u/U)² + (w/W)² = 1} × S², mirrored across the plane, with k = W/U.
The far model is `b4_global.py`'s H-FAR-MODEL (the board's): g = (ℓ/z)²(−dt² + du² + dw² + ρ(u)² dΩ²), with
z = ℓ + |w| and ρ² = u² + a², a = 2 (the throat radius r₀ = 2m, G3).

**The cover** (the board's, revised). U = 1.05·R_reach with R_reach = R_core + 2T. The reason for 2T: `o3_write.py` W3
says *"Moving at most at c, all of it then lay, when the write began, inside the ball of radius (2 + T) m"*. The
README's own matter, carried in by the inflow (115 (c), 163), can therefore influence the region out to (2 + 2T) m by
the closing (deduced, the model's cones). At the example README (N = 2.74×10¹⁵ bits), T = 199,702.187 clocks,
R_reach = 399,406.4 and U = 419,376.7.

**X0. Agreement with the owner** (computed). The expansion here is `b4_global.py`'s own recipe, generalized to any
level set and any static diagonal metric: div n over √|g| with the lapse, minus a_n. On the round surface it equals
`far_boundary()`'s closed form exactly (sympy). On the owner's parabola it equals `tipped_far_boundary()`'s minimum on
the owner's own grid, to a relative 3×10⁻¹⁵.

**X1. The ellipse in closed form** (computed, exact). On T_E, with D = √(u²/U⁴ + w²/W⁴):

> P = 1/(U²W²D²) + 2u²/(U²(u² + a²)),  **θ₊ = −θ₋ = ((ℓ + w)P − 3w/W²)/(ℓD)**

- At the tip, θ₊ = (W² + Wℓ − 3U²)/(U²ℓ), the checker's form. (Reproduced in the apply step by a different method, the
  first variation of the area.)
- W = U gives the owner's round formula.
- T_E meets the plane square-on (∂F/∂w = 0 at w = 0; the parabola does not), so the mirror and the warp's kink add
  nothing there.

**X2. The theorem, within H-FAR-MODEL** (deduced from X1; its inequality machine-checked by z3, with vacuity and
encoding guards).
- **Notation.** K = k², x = (u/U)², b = (a/U)², and Q = W²P = K/(1 + (K − 1)x) + 2Kx/(x + b).
- **The inequality.** If K ≥ 3 and (K − 1)b ≤ 2, then Q ≥ 3 everywhere on T_E (z3: the negation is unsat).
- **What follows:**
  > θ₊ = (ℓP + (w/W²)(Q − 3))/(ℓD) ≥ P/D ≥ U/W² > 0, at every point and for **every ℓ > 0**.
- **The side condition** reads a ≤ U at W = √3·U, which every surface considered here meets.
- **At W = √3·U exactly,** the tip reads √3/U for every ℓ.

**X3. The threshold is exact** (computed, exact). For W < √3·U the tip is trapped whenever ℓ < (3U² − W²)/W.

**X4. The scan** (computed, 30 digits). It uses the general code, which is independent of X1's algebra. At the example
README:

| W/U | c = 10⁻⁶ … 27.07 | c = 4×10⁵ | c = 10⁹ |
|---|---|---|---|
| 1.70 | trapped (−1.1×10⁵ … −4.1×10⁻³) | +3.78×10⁻⁶ | +4.05×10⁻⁶ |
| √3 | +4.130×10⁻⁶ = √3/U | +4.130×10⁻⁶ | +4.130×10⁻⁶ |
| 1.74 | +5.557×10⁻⁶ | +4.22×10⁻⁶ | +4.15×10⁻⁶ |
| 2 | +5.365×10⁻⁶ | +5.365×10⁻⁶ | +4.77×10⁻⁶ |

- 1.70 is trapped exactly for the c below X3's switch, ℓ* = 27,136.
- Every untrapped minimum lies above X2's floor, U/W² = 7.95×10⁻⁷ at √3.

**X5. The shape is free of N and ℓ; the size is not** (deduced; computed).
- **The threshold is a pure ratio.** U(N) enters only through b, and U > a at every N.
- **The size grows with the README.** U = 27.9 at N = 10³, 419,377 at the example and 3.0×10¹⁰ at N = 10³⁰. The depth at
  which H-FAR-MODEL must hold (X9 (a)) grows with it.
- **Checked at those three N:** 1.74 is untrapped and 1.70 is trapped.
- **Control.** The owner's parabola has an exact foot condition, and the W/U it needs at c = 1 itself grows with N:
  21.0, then 3.15×10⁵, then 2.25×10¹⁰.

**X6. Through the write** (deduced, conditional on W2 and on causal propagation; the cones STRUCTURAL; **not proved**).
- **The model's cones** (STRUCTURAL, checked from the model's metric itself). Every causal vector has
  du² + dw² ≤ dt², because the S² coefficient u² + a² is non-negative. A mutant that makes it negative fails the check.
- **T_E's distance from the origin** (computed on the grid) is never less than U. An oblate mutant fails the check.
- **Reach.** No signal from the corridor (R_core = 2, fixed by your 162) or from the README's own matter reaches T_E
  before the closing. At the example README there are 19,970 clocks to spare.
- **Under 179** the corridor sits in the bulk, so U must also cover its depth w_c: U ≥ 1.05·(R_core + w_c + 2T). No
  ruling and no computation here bounds w_c, so this is OPEN. If the corridor reached down the column to depth W, T's
  tip would sit inside the corridor itself.
- **Why the geometry there stays put** is the step that is not proved. It needs the region outside the reach to keep
  its prior state. That takes global hyperbolicity (W2, not green) and an evolution whose sources propagate causally
  (domain of dependence, standard-not-READ). CGS Theorem 3.1's premises include *"the null energy condition (NEC)"*
  (READ, CGS pp. 3–4, recorded in `bulk/CENSOR5D.md`), and that note records Theorem 3.5 (p. 5) as resting on the same
  premises. The model's own column violates the NEC at every point (X9 (c)).
- **Any finite hold works,** because X2 does not depend on U. The hold is finite by your 158 (2) and by E2's closing
  (DERIVED).

**X7. After the closing** (deduced, an estimate, **not green**; Raychaudhuri and the area law standard-not-READ).
- **4D form.** The radiation focuses by about 2E_rad/U², with E_rad ≤ (5/4)m (`ledger.py` E4, computed on eq. (17)).
  Margin against X2's floor: U/(2.5k²) = 5.59×10⁴ at the example README, or 2.91×10⁵ with the computed floor √3/U. The
  exact-floor margin falls below 1 only for READMEs under about 33 bits.
- **5D form, for ℓ ≫ U** (deduced, an order of magnitude; G5 ≈ G4·ℓ is standard-not-READ). Focusing is about
  8πG5·E_rad/(2π²U³), and the margin is about πU²/(15c). That is 37 at c = 10⁹, and it reaches 1 at c ≈ 3.7×10¹⁰.
- **So a condition on ℓ comes back after the closing.** "No condition on ℓ" holds only up to the closing.

**X8. A far field at T_E, in the board's configuration** (computed in the model with its throat on our plane, **not**
in the configuration 179 asks; deduced).
- **The field.** `bulk/kscale.py` gives eq. (17)'s γ = 5/4 at r₀ = 2m, so the plane's spatial field is
  g_rr = 1 + (5/2)m/r, conformally flat to O(m).
- **The lapse drops out of θ₊ exactly.**
- **Exact tip as ℓ → 0** (computed; reproduced in the apply step by the first-variation method):
  > ℓ·θ₊(tip) → (positive factor) × (k² − 3 − 3γm/(kU + 2γm)).
- **So 1.74 suffices only for large enough READMEs.** With γ = 5/4, 1.74 holds at the tip only for U above 76.65, that
  is N above about 1.8×10⁴ bits. At N = 10³ (U = 27.9) the tip is trapped: −4.48×10⁴ at c = 10⁻⁶. There the tip
  alone needs k above 1.753 (from the exact tip form), and the sufficient bound below asks 1.862. (The refuting
  session found the threshold near 1.3×10⁵ bits with the old cover R_core + T; the revised cover moves it to 1.8×10⁴.)
- **A sufficient condition for any conformal field** of strength γm is k²(1 − 3γm/U) > 3 (deduced). At the example
  README that is k > 1.7320586, and by that bound 1.74 survives a field at least 1,019 times eq. (17)'s.
- **The field is real at the line itself.** In the isotropic extension E1 the tip at exactly √3 is trapped for small c
  (−5.16 at c = 10⁻⁶).
- **The non-conformal extension E2** (g_uu alone) keeps 1.74 untrapped at the seven values of c tested (10⁻⁶ to 10⁹),
  and that is all: scan evidence only. E1 and E2 are the board's test extensions (H-FAR-FIELD-EXTENSION), not
  solutions.
- **Scope.** By X6, a field that arises at the opening (160, 162) cannot reach T_E before the closing. X8 therefore
  bears only on a far field already present before the opening, such as the README's own energy on our plane before it
  is carried in (163, 184). That field's bulk form is not computed.

**X9. H-FAR-MODEL is not derived here, and seated (Z) excludes its column** (computed; STRUCTURAL; deduced).
- **(a) The tip crosses the join** (STRUCTURAL). In the model, a column joining the two positions runs to every depth.
  Every far surface enclosing the reach crosses it (u = 0) at a depth of at least R_reach, about 4.0×10⁵ at the example
  README, whatever its shape. The join is B4a's one end: the board's reading of your 152 (1), not your words.
- **(b) No computed bulk supplies that column** (computed from the bank; READ from the board's notes).
  - `b4_static.py`'s banked bulk is built on eq. (17) as the plane's own metric (F1) and reaches r ≤ 32, y ≤ 16, more
    than 10³ times short of the tip.
  - The board's other bulks do not supply it either (READ from `BULK-BALANCE.md` and `warptheorem.py`'s B4d row).
    Model B is a throat column whose plane balance has no equality. Model C, your guess in 182, is the eternal two-sided
    black hole: as it stands it is not an admissible B4d corridor (BULK-BALANCE §7), and its bridge is not a static
    traversable column. B4d stages 5–7 took eq. (17) as a plane's metric.
- **(c) Every column of the family breaks (Z)** (computed; deduced). Let the column's conformal radius A(w) be any
  profile in depth (the model's constant a included).
  - **Curvature.** Along k = ∂_t + ∂_u, R(k,k) = −2A²/(u² + A²)². This is computed from the full 5D Ricci tensor. The
    apply step reproduced it independently from the warped-product formula R(k,k) = −(2/r)∂²_u r with r = √(u² + A²).
  - **The rays.** k is an affine null geodesic of the model, R(k,k) is the same in the model and its flat conformal
    partner, and Raychaudhuri's identity holds exactly with the cross-section's expansion 2u/ρ² (all computed).
  - **The net per ray.** Along each radial light ray through the column the integral is −π/A in the affine parameter u
    (computed). It is negative, never zero.
  - **What that means.** Under Einstein's equations (standard-not-READ), that is net negative null energy along each
    such ray, against seated (Z) as worded. Your 183's pairs net to zero, so they do not cover a net below zero. It is
    also negative null energy at every point, against the NEC premise of CGS's theorems.
- **Beyond the family** (deduced; Raychaudhuri standard-not-READ). Any static throat that complete light rays pass
  through needs the cross-section's expansion to change sign along them. That forces a net negative ∫R(k,k), so (Z)
  excludes every static traversable join, not just this family. A join consistent with (Z) would have to be of another
  type, for example non-traversable or carrying a horizon. What T's tip does then is OPEN, and this instrument does not
  cover it.
- **(d) The tip formula, for excluded columns only** (computed, exact). For any profile:
  > θ₊(tip) = ((ℓ + W)/ℓ)(W/U² + 2A′(W)/A(W)) − 3/ℓ.

  Power-law columns A = a(z/ℓ)^p move the threshold to k² ≥ 3 − 2p. Scanned: for p = −1, √5 is untrapped and 2 is
  trapped at small c; for p = +1, √3 is untrapped and even k = 1 has minimum +2.38×10⁻⁶. **These are statements about
  columns (Z) excludes. They are not a route to green.**
- **(e) The model against (G), 139 (1) and 166** (STRUCTURAL, checked).
  - On our plane (w = 0) the S² radius² is u² + a², least at u = 0 with a² > 0: a throat on our plane. Seated (G) puts
    the corridor on neither plane.
  - The warp's jump across the plane, ∂_w ln Ω at w = 0⁺, is −1/ℓ on position 1's sheet (u > 0) and on position 2's
    (u < 0): one positive tension for both positions. Your 139 (1) has position 2's plane negative. A mutant that puts
    position 2's sheet on a negative-tension plane makes the check fail.
  - There is one plane, not the two of your 166 with the bulk between them.
  - So "eq. (17) on our plane is not an input", which the first version claimed, is withdrawn. The model keeps the
    corridor's throat on our plane in another metric.

**X10. Under 184** (computed; deduced, an estimate).
- **H-FAR-MODEL's plane is matter-free,** which your 184 rules out.
- **The mean.** Our plane's mean energy density over its Randall–Sundrum tension is exactly ρ_crit c²/λ_RS =
  (H₀ℓ/c)²/2, which is 2.65×10⁻⁶¹ at ℓ = 10⁻⁴ m (`cosmo.py`'s H₀, `kscale.tension`). That is a mean, not a bound.
- **A local bound.** At nuclear density (`address.py`'s RHO_NUCLEAR = 2.676×10¹⁷ kg/m³) the ratio is 8.3×10⁻¹⁸.
  `f1_audit.py` bounds a plane's matter the same generous way (2.3×10¹⁷) under the board's H-OWN-MATTER-ONLY. The ratio
  is still negligible, but it is no longer 10⁻⁶¹.

**X11. Without the column** (computed: z3, and a scan in the board's test extension; deduced).
- **No column, no threshold.** At a = 0 our plane is throat-free and the model is Poincaré AdS₅ with the RS plane.
  Then Q = K/(1 + (K − 1)x) + 2K ≥ 3 for every K ≥ 1 (z3, with guards), so every W ≥ U is untrapped at every ℓ. The √3
  threshold belongs to the on-plane throat alone.
- **With a field centred in the bulk** (the board's test extension E1, centred at depth w_c = U/2 inside T_E): at both
  README sizes tested, k = √3 stays untrapped (+0.0775 at N = 10³; +5.56×10⁻⁶ at the example), while the round
  surface k = 1 is trapped at small c (−4.2×10⁵ and −35.8).
- **A sufficient condition at every ℓ** (deduced; both parts checked at both sizes):
  2/U ≥ 3γm/d_min² and 2(K − 1)/(KU) ≥ 3γm/d_min², where d_min is the least distance from the field's centre to
  T_E (0.935·U on the grid). The apply step found the first version checked only the second part, and added the first.
- **Not computed here:** a negative-tension position-2 plane (139 (1)), the two planes of 166, and whether T in 179's
  configuration must cross a join or can enclose it (B4a's topology). All OPEN.

## What B4c earns

| part | status | on what |
|---|---|---|
| untrapped at every ℓ and every N, static | **PROVED within H-FAR-MODEL** (exact; z3) | X1–X5, for W ≥ √3·U |
| through the write | **deduced, conditional; not proved** | X6: W2 (not green) and causal propagation (standard-not-READ); the model's column violates the NEC those theorems assume |
| after the closing | **an estimate, not green** | X7: Raychaudhuri and the area law (standard-not-READ); in 5D it needs c ≲ πU²/15 |
| with a far field | computed in the board's configuration only | X8, X11: H-FAR-FIELD-EXTENSION; small READMEs need k above 1.74 |
| **B4c as a lemma** | **READING. Not green. On this model it cannot turn green.** | H-FAR-MODEL, whose join column seated (Z) excludes and whose plane conflicts with (G), 139 (1) and 166 as worded |

**What it rests on, not green:**
- H-FAR-MODEL (the board's reading). It carries five things, each used somewhere above:
  1. a throat on our plane, joining both positions' sheets under one positive-tension warp (against (G), 139 (1) and
     166 as worded);
  2. the join column at every depth, crossed by T's tip at depth ≥ R_reach, and excluded by (Z) in every profile the
     instrument covers;
  3. the RS-II warp and a matter-free plane on all of T;
  4. the model's causal structure everywhere inside T, the column included, as a well-posed prior state;
  5. under 179, a corridor depth w_c inside the cover, which nothing bounds (OPEN).
- W2 (B4b READING, B4d OPEN), for the step through the write.
- Causal propagation and the domain-of-dependence theorem (standard-not-READ), for the same step.
- The after-closing estimate.
- H-FAR-FIELD-EXTENSION (the board's), for the far-field clause only.

**What it rests on, green:** E2 (DERIVED): the closing exists, so the hold is finite. Your 162 (H-FIXED-SIZE): the core
size is fixed at R_core = 2m.

**What it no longer needs:** a condition on ℓ up to the closing (the round surface needed ℓ > 2R_reach); a condition
on the shape that grows with N (the round surface grew as N^(1/3), the parabola as N^(2/3)/c); eq. (17)'s own metric on
our plane. The model still keeps an on-plane throat, though, as X9 (e) shows.

**What turning it green would take.** First, a join consistent with (Z), (G), 139 (1) and 166 has to replace the model's
column and plane. That join is OPEN. Then W2 has to turn green, and the after-closing step has to become more than an
estimate. Supplying a column of the model's family would not do it, because (Z) excludes every one of them.

## Before the opening (B4b′)

The topology before the opening is fixed by B4b′, given W2. Its source is a **READ of the abstract only**, with no page
(Ake Hau, Flores and Sánchez, arXiv:1808.04412, quoted in `b4_global.py`): *"the splitting of any globally hyperbolic
(M-bar, g) as an orthogonal product R x Sigma-bar with Cauchy slices with boundary {t} x Sigma-bar is proved"*. The
theorem itself has not been read with its page.

## The cypher (192, 194, 196)

The question this lemma raises has **not** been put to the cypher: "is H-FAR-MODEL derivable, and is a join consistent
with (Z) possible here?" Under your 196 it goes there, through §33's procedure (`tools/cypher.py`, roster 1173, logic
as the mechanism), with the index encoding named as the board's and a control that can fail. The cypher would classify
the question. It would not be a physical derivation, and nothing here was run through it.

## Controls and mutants

There are 35 named mutations, and each one makes its check fail:

- **The expansion's recipe:** the lapse dropped from √|g|; a_n added instead of subtracted; the S² factor taken as ρ
  instead of ρ²; the normal pointed inward.
- **The closed form:** the warp's 3 written as 2; the S²'s 2 written as 1.
- **The theorem:** K ≥ 2.9, and the side condition loosened to 3. z3 finds a counterexample to each.
- **The scan:** the warp inverted; the floor claimed as 3/U.
- **The shape free of N:** the parabola in place of the ellipse.
- **The reach:** an oblate surface; a cover of 0.95; the model's S² coefficient made negative; the README's initial
  support left out of the cover.
- **After the closing:** E_rad inflated 10⁵-fold; G5 taken without its factor ℓ.
- **The far field:** inflated 10⁴-fold; switched off.
- **The column:** removed (a = 0); its depth power's sign flipped; the general R(k,k) claimed positive; position 2's
  sheet put on a negative-tension plane.
- **The density:** a mass density used as an energy density; the local bound taken as the cosmic mean.
- **Without the column:** K ≥ 9/10 (z3 finds a counterexample); the column put back; the bulk-centred field inflated
  100-fold.
- **The guards:** a row labelled "positive"; the status row claiming green; the non-green inputs dropped while the
  status stays READING; a line of the code's docstring citing the withdrawn item as standing; a line of this note doing
  the same.

The status guard applies your green rule: GREEN only if PROVED, DERIVED or an axiom of yours, with no non-green input.

## Named hypotheses

- **Yours:** H-P2-NEGATIVE-PLANE (139 (1)); H-SEPARATE-JOINED-THROUGH-DIMENSION (152 (1)); H-BRIEF-EVOLUTION, an
  option to check (152 (2)); H-HALF-IS-OURS (157); H-HOLD-AT-BOUND (158 (2)); H-CORRIDOR-IS-OPENING (160); H-FIXED-SIZE
  (162); H-AT-ONCE-IS-WHOLE (163); H-CORRIDOR-SPANS-BOTH (166); H-CORRIDOR-IN-BULK (179/180); seated (G) and (Z) (183,
  187 (3)); H-NO-MATTER-FREE-PLANES (184); H-README-NOT-A-PAIR (195); M-ALL-QUESTIONS-THROUGH-THE-CYPHER (196). The
  pair axiom was withdrawn by 194 and is not carried.
- **The board's:**
  - H-FAR-MODEL, with its five load-bearing parts listed above;
  - H-FAR-FIELD-EXTENSION, the test extensions in X8 and X11;
  - the cover U = 1.05·(R_core + 2T).

## Proposed change to the theorem's B4c row (not made here)

> **B4c** the far boundary T strictly untrapped, uniformly in time. Within the board's far model H-FAR-MODEL, an
> ellipsoidal T with W ≥ √3·U is untrapped at every ℓ and every N (exact; z3). U = 1.05·(R_core + 2T_hold) grows with
> N. Through the write: deduced, conditional on W2 and causal propagation. After the closing: an estimate, needing
> c ≲ πU²/15 in 5D. With a far field present before the opening, the ratio must exceed k_tip(U), and 1.74 suffices
> only above about 1.8×10⁴ bits. — **READING, not green.** The model's join column is excluded by seated (Z) for every
> depth profile covered, and its on-plane throat and single positive tension conflict with (G), 139 (1) and 166. A
> (Z)-consistent join is OPEN.

That would remove, from the current row: the "ℓ > 2R_reach" condition; the "~23 m in corridor units" figure (already
stale against o3_write's write); eq. (17) as the source of the reach; and "margin ~5".

## Findings applied in the revision

Both reviews were separate AI sessions inside this project. Every finding was reproduced before it was applied, and
none was rejected.

- **Refuting session.**
  - F1: the far-field claim fails for small READMEs. Reproduced independently: −9.90×10⁴ at the old cover's U = 15.0
    and −4.48×10⁴ at the revised cover's U = 27.9, with the tip formula exact. Applied in X8.
  - F2: (Z) excludes every column of the family. Reproduced by the warped-product formula. Applied in X9 (c) and (d),
    and extended beyond the family by Raychaudhuri.
  - F3: the "one thing" narrowing was overstated. Applied: the five parts of H-FAR-MODEL, and the cover now includes
    the README's support.
  - F4: the withdrawn item had been cited as standing. Applied, and guarded in both files.
  - F5: X10's number was a mean, not a bound. Reproduced: 8.3×10⁻¹⁸ at nuclear density. Applied.
  - F6: two of C7's sub-checks could not fail. Applied: the cones are now read from the model's metric, the distance
    is taken on the grid, and the table row is split.
- **Overclaim session.**
  - Applied in the same places: R1 (as F4), R2 (all non-green inputs), R3 (X9 (e) and X11), R4 (X6 not proved),
    R5 (cover 2T; 19,970 clocks), R6 (X7's 5D form), R7 (estimate, not DERIVED), R8 (shape, not size), R9 (E2 at seven
    values only), R10 (the other bulks named), R11 ("not derived here"; cypher not run), R12 (as F5), R13 (sessions
    labelled), R14 (B4b′ is an abstract-only READ), R15 (152 (1)'s join is the board's reading), R16 (as F6).
- **Found while reproducing.** X11's sufficient bound covered only one of its two parts. The ℓ part was added, with a
  mutant that breaks it.

## Re-run

```
python3 lemmas/b4c_far.py               # the report, every row labelled
python3 lemmas/b4c_far.py --selftest    # 13 checks, about 40 s
python3 lemmas/b4c_far.py --mutants     # 35 mutations, each must make its check fail, about 2 min
python3 lemmas/b4c_far.py --json PATH
```

## History

- **First written 2026-10-09.** It started from the item-186 window checker's ellipse (its check discrepancy 2,
  scanned at W/U = 1.70 and 1.74). That checker was a separate AI session inside this project. The exact threshold √3,
  the proof, the far-field note and the column analysis were new.
- **Revised 2026-10-09** on two reviews by separate AI sessions inside this project.
  - All findings were applied (listed above), and nothing was rejected.
  - The cover became R_core + 2T.
  - The far-field claim was narrowed to large READMEs and to the board's configuration.
  - (Z) was shown to exclude the model's column in every depth profile covered.
  - The model was set against (G), 139 (1) and 166.
  - B4c stays a READING. It is not green, and on this model it cannot turn green.
  - Not verified since. Nothing is seated.
