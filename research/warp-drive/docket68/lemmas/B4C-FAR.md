# Lemma B4c on an ellipsoidal far surface (computed, READ and deduced; not verified; not seated; 2026-10-09)

The instrument is `b4c_far.py`: selftest 12/12 in about 30 s, and `--mutants` 22 of 22 caught in about 80 s. It imports
`b4_global.py`, `o3_write.py`, `ledger.py`, `bulk/kscale.py` and `../cosmo.py` by path and reads the bank
`b4_static.json`. It writes nothing into any other file. Folding it into `warptheorem.py`, `WARPTHEOREM.md` and the
cypher audit is done afterwards.

## What you said

- **152 (1):** *"two separate positions connected by/reached through a dimension."*
- **152 (2):** *"I had not considered this yet. It could very well be possible, so let's consider this an option and
  check it."*
- **157:** *"we already have at least half the model, our current universe."*
- **158 (2):** *"Exactly as long as the write needs  I should think"*
- **162:** *"... The throat doesn't change size because the whole chain object only every takes on the size that
  contains the README upon opening. ..."*
- **179/180:** *"We know the corridor \*does not sit on either position's plane, it only bridges them. So one could
  surmise that the corridor is exclusive to the bulk."*
- **183:** you chose *"Yes: never violated as a pair"*. **187 (3):** you chose *"Seat both"*.
- **184:** *"There are no matter free planes"*
- **192:** *"this appears to be a question to put to the math language hierarchy cypher"*. **193:** you chose *"An axiom
  of my theory"*.
- The round's request, as relayed: get the chain to full green, *"even if it means new or edited lemmas"*.

## Plain words first

1. **The far boundary no longer asks anything of ℓ or of the README's size.** Take an egg-shaped surface around the
   corridor: half-width U along our plane and depth W into the bulk, meeting the plane square-on. If W ≥ √3·U, it is
   strictly untrapped at every ℓ, every time before the closing, and at every README. That is an exact proof, not a scan.
2. **√3 is the exact line.** Below it the tip is trapped whenever ℓ is small enough. The item-186 checker's bracket,
   1.70 trapped and 1.74 untrapped, sits on either side of 1.7320508.
3. **Eq. (17) on our plane is not needed (179).** With the corridor in the bulk and our plane carrying only eq. (17)'s
   far field, W = 1.74·U still holds at every ℓ.
4. **B4c is still not green.** It rests on the board's far model, and what it rests on is now one thing: the geometry
   of the column joining the two positions, deep in the bulk. Every admissible far surface must cross that column at a
   depth of at least R_reach, about 2×10⁵ corridor lengths at the example README. No ruling of yours and no source
   read gives that geometry. The model's own column is not a solution, and taken literally it would break clause (Z).
   So B4c can turn green only when the complete bulk (B3, through B4d) supplies that column.

## The result

Units are m = 1 and c = ℓ/m. T_E is the surface {(u/U)² + (w/W)² = 1} × S², mirrored across the plane, with k = W/U.
The far model is `b4_global.py`'s H-FAR-MODEL: g = (ℓ/z)²(−dt² + du² + dw² + ρ(u)² dΩ²), with z = ℓ + |w| and
ρ² = u² + a².

**X0. Agreement with the owner** (computed). The expansion here is `b4_global.py`'s own recipe, generalized to any
level set and any static diagonal metric: div n over √|g| with the lapse, minus a_n. On the round surface it equals
`far_boundary()`'s closed form exactly (sympy). On the owner's parabola it equals `tipped_far_boundary()`'s minimum on
the owner's own grid, to a relative 3×10⁻¹⁵.

**X1. The ellipse in closed form** (computed, exact). On T_E, with D = √(u²/U⁴ + w²/W⁴):

> P = 1/(U²W²D²) + 2u²/(U²(u² + a²)),  **θ₊ = −θ₋ = ((ℓ + w)P − 3w/W²)/(ℓD)**

- At the tip, θ₊ = (W² + Wℓ − 3U²)/(U²ℓ), the checker's form.
- W = U gives the owner's round formula.
- T_E meets the plane square-on (∂F/∂w = 0 at w = 0; the parabola does not), so the mirror and the warp's kink add
  nothing there.

**X2. The theorem** (deduced from X1; its inequality machine-checked by z3, with vacuity and encoding guards).
- **Notation.** K = k², x = (u/U)², b = (a/U)², and Q = W²P = K/(1 + (K − 1)x) + 2Kx/(x + b).
- **The inequality.** If K ≥ 3 and (K − 1)b ≤ 2, then Q ≥ 3 everywhere on T_E (z3: the negation is unsat).
- **What follows:**
  > θ₊ = (ℓP + (w/W²)(Q − 3))/(ℓD) ≥ P/D ≥ κ ≥ U/W² > 0, at every point and for **every ℓ > 0**.
- **The side condition** reads a ≤ U at W = √3·U, which any surface enclosing the throat meets. It allows any W/U up
  to √(1 + 2U²/a²), about 1.5×10⁵ at the example README.
- **It holds for any column radius 0 < a ≤ U.** So B7's widening, from a smaller pre-existing bridge to the throat
  size, changes nothing (deduced).
- **At W = √3·U exactly,** the tip reads √3/U for every ℓ.

**X3. The threshold is exact** (computed, exact). For W < √3·U the tip is trapped whenever ℓ < (3U² − W²)/W.

**X4. The scan** (computed, 30 digits). It uses the general code, which is independent of X1's algebra. At the example
README, T = 199,702.187 clocks (`o3_write.py`), R_reach = 2 + T and U = 1.05·R_reach = 209,689.4:

| W/U | c = 10⁻⁶ … 27.07 | c = 4×10⁵ | c = 10⁹ |
|---|---|---|---|
| 1.70 | trapped (−1.1×10⁵ … −4.1×10⁻³) | +7.8×10⁻⁶ | +8.1×10⁻⁶ |
| √3 | +8.260×10⁻⁶ = √3/U at every c | | |
| 1.74 | +1.111×10⁻⁵ | +8.37×10⁻⁶ | +8.30×10⁻⁶ |
| 2 | +1.073×10⁻⁵ | +1.073×10⁻⁵ | +9.54×10⁻⁶ |

- 1.70 is trapped exactly for the c below X3's switch, ℓ* = 13,568.
- Every untrapped minimum lies above X2's floor, U/W² = 1.59×10⁻⁶ at √3.

**X5. Free of N** (deduced; computed).
- **The threshold is a pure ratio.** U(N) enters only through b, and U ≥ 1.05 × 2 > a at every N.
- **Checked at three N.** At N = 10³ (U = 15.0), at the example, and at 10³⁰ (U = 1.5×10¹⁰), 1.74 is untrapped and
  1.70 is trapped.
- **Control.** The owner's parabola has an exact foot condition, and the W/U it needs at c = 1 grows with N: 11.4,
  then 1.57×10⁵, then 1.12×10¹⁰.

**X6. Uniformly in time, through the write** (STRUCTURAL, deduced; the domain-of-dependence step is
standard-not-READ).
- **The model's cones** (STRUCTURAL). Every causal vector has du² + dw² ≤ dt²: the S² adds only squares.
- **T_E's distance from the origin.** On T_E, u² + w² = U² + (W² − U²)sin², which is never less than U².
- **So T_E is outside the corridor's influence through the write.** Take U = 1.05·(R_core + T_hold), with R_core = 2,
  G3's r₀, held fixed by your 162. Then no signal from the corridor reaches T_E before the closing; at the example
  README 9,985 clocks are still to spare.
- **Why the geometry there stays put.** The region outside the reach keeps its prior, static state by domain of
  dependence. That step needs global hyperbolicity (W2), as CGS Theorem 3.5 itself does.
- **Before the opening** the model is static, and B4b′ (READ and deduced, given W2) fixes the topology.
- **Any finite hold works,** because X2 does not depend on U. The hold is finite by your 158 (2) and by E2's closing
  (DERIVED). `o3_write.py`'s figure of at least 2.0×10⁵ clocks is an illustration, not an input.
- **Under 179** the corridor sits in the bulk, so U must also cover its depth: U ≥ 1.05·(R_core + w_c + T_hold). The
  ratio does not change (deduced).

**X7. After the closing** (deduced, an estimate; Raychaudhuri, standard-not-READ). This is `b4_global.py`'s radiation
step, with X2's floor.
- **The estimate.** The radiation focuses by about 2E_rad/U², with E_rad ≤ (5/4)m (`ledger.py` E4).
- **Margin with the exact floor:** U/(2.5k²) = 2.80×10⁴ at the example README.
- **Margin with the computed floor** (√3/U): 1.45×10⁵.
- **Where it fails.** The exact-floor margin falls below 1 only for READMEs under about 126 bits.
- **Its weak point** is the four-dimensional area law used for a five-dimensional surface. The margin is large enough
  that factors of order one do not matter.
- **E4's 5/4 was computed on eq. (17).** With E alone (G1) the cap is m, which only raises the margin.

## What B4c earns

| part | status | on what |
|---|---|---|
| untrapped at every ℓ and every N, before the opening and through the write | **PROVED within H-FAR-MODEL** (exact) | X1–X6; the domain-of-dependence step rests on W2, as CGS's own hypothesis |
| after the closing | **derived, an estimate** | X7 |
| **B4c as a lemma** | **READING. Not green.** | H-FAR-MODEL, narrowed to one thing: the join column's geometry at depth ≥ R_reach (X9). That geometry is B3's (OPEN), through B4d |

- **What B4c no longer needs:**
  - a condition on ℓ (the round surface needed ℓ > 2R_reach);
  - a condition that grows with N (the round surface grew as N^(1/3), the parabola as N^(2/3)/c);
  - eq. (17) on our plane, F1 (X8);
  - `o3_write.py`'s numbers.
- **What it still rests on:**
  - H-FAR-MODEL (the board's reading);
  - W2, for the domain-of-dependence step;
  - E2 (DERIVED): the closing exists, so the hold is finite;
  - your 162: the corridor's size is fixed;
  - Raychaudhuri (standard-not-READ), for the step after the closing.

## Why H-FAR-MODEL is not derived (X9)

- **(a) Every admissible far surface crosses the join column deep in the bulk** (STRUCTURAL).
  - A far surface must enclose the reach and join both positions through the bulk; that join is B4a's one end, your
    152 (1).
  - So its tip crosses u = 0 at a depth of at least R_reach: about 2.0×10⁵ at the example README, whatever the shape.
- **(b) The only bulk the board has derived does not reach that depth** (computed from the bank).
  - That bulk is `b4_static.py`'s, and it is built on eq. (17) as the plane's own metric (F1).
  - Its verified grid stops at r ≤ 32 and y ≤ 16, more than 10³ times short of the tip.
- **(c) The model's own column is not a solution.**
  - **Its curvature** (computed: the full 5D Ricci tensor in sympy). R_ab + (4/ℓ²)g_ab vanishes except in R_uu. Along
    k = ∂_t + ∂_u, R(k,k) = −2a²/ρ⁴. At a = 0 the metric is exactly AdS₅.
  - **Along each radial ray through the column.** The integral is −π/a in the flat metric's affine parameter
    (computed). In the physical metric it is −(z/ℓ)²π/a (deduced: null affine parameters rescale by Ω²,
    standard-not-READ).
  - **What that means for (Z).** Taken as an exact geometry, Einstein's equations would give the column net negative
    null energy along every one of those rays. That is against seated clause (Z), "never violated" net along each light
    ray, your 183 (deduced).
  - **Your 193 does not cover it.** Its axiom, H-PAIR-AXIOM, is for the README crossing the corridor's horizon. It is
    not stretched to this column.
  - **Why X2 survives anyway.** X2 does not use the column's stress: the column's S² term is zero at the tip and
    positive elsewhere. It does use the column's metric.
- **(d) The verdict turns on the column's profile with depth** (computed, exact).
  - Keep the rest of the model, and let the column's conformal radius A(w) vary with depth. Then the tip reads:
    > θ₊(tip) = ((ℓ + W)/ℓ)(W/U² + 2A′(W)/A(W)) − 3/ℓ.
  - **Power-law columns,** A = a(z/ℓ)^p, move the tip threshold to k² ≥ 3 − 2p.
  - **Scanned** (computed):
    - p = −1: √5 is untrapped at every c tested, while 2 is trapped at small c;
    - p = +1: √3 is untrapped; even k = 1 has a minimum of +4.8×10⁻⁶.
  - **A column that thins faster than any power of the warp** would need a depth growing with N. That is deduced from
    the tip formula and not computed.
- **Your 157 does not supply it.** It makes the prior state our current universe, but it does not give the metric of
  B7's bridge column 2×10⁵ corridor lengths down. Reading it that way would stretch it.

**So H-FAR-MODEL cannot be derived from the rulings or from any source read.** B4c stays a READING, and the reason is
exactly the column. Once B4d produces a column, the tip formula and the general level-set code here decide at once
whether an ellipse works on it.

## Under 179: eq. (17) on our plane is not an input (X8)

- **Nothing in X1–X6 uses eq. (17).** The old B4c took its reach from eq. (17) (1 − FH > 0). That step is replaced by
  the model's own cones.
- **With only eq. (17)'s far field on our plane** (computed):
  - **The field itself.** `bulk/kscale.py` gives γ = 5/4 at r₀ = 2m, so the plane's spatial field is
    g_rr = 1 + (5/2)m/r. That is conformally flat to O(m), with r = ρ + γm.
  - **The lapse drops out of θ₊ exactly,** so the 1/r tail of g_tt plays no part.
  - **Any conformal far field** whose gradient is no larger than this one keeps T_E untrapped at every ℓ if
    k²(1 − 3γm/U) > 3 (deduced from X2 and the exact conformal identity). At the example README that is k > 1.7320663.
    By that bound, 1.74 survives a field at least 509 times eq. (17)'s.
  - **The scans.** Two test extensions into the bulk were tried (H-FAR-FIELD-EXTENSION, the board's): E1, isotropic in
    the coordinate distance; and E2, in g_uu alone. Both keep W/U = 1.74 untrapped at every c from 10⁻⁶ to 10⁹; the
    minimum is +8.30×10⁻⁶.
  - **The field is not negligible at the line itself.** E1 traps the tip at exactly √3 for small c (−10.3 at
    c = 10⁻⁶). The far field moves the threshold up by about 10⁻⁵, and the surface to carry is **W = 1.74·U**.
- **What eq. (17) still touches.** Only E4's cap in X7, which it does not need.

## Under 184 (X10)

- **H-FAR-MODEL's plane is matter-free.**
- **How much our plane's matter could change that** (computed, exact). Our plane's mean energy density over its
  Randall–Sundrum tension is ρ_crit c²/λ_RS = (H₀ℓ/c)²/2. It uses `cosmo.py`'s H₀ and `kscale.tension`.
- **Its size.** At most 2.7×10⁻⁶¹ for ℓ ≤ 10⁻⁴ m.
- **What it does.** The plane's matter enters the far bulk at that relative order (deduced, an estimate).

## Controls and mutants

The 22 mutations, each of which makes its check fail:

- **The expansion's recipe:** the lapse dropped from √|g|; a_n added instead of subtracted; the S² factor taken as ρ
  instead of ρ²; the normal pointed inward.
- **The closed form:** the warp's 3 written as 2; the S²'s 2 written as 1.
- **The theorem:** K ≥ 2.9, and the side condition loosened to 3. z3 finds a counterexample to each.
- **The scan:** the warp inverted; the floor claimed as 3/U.
- **N-independence:** the parabola in place of the ellipse.
- **The reach:** an oblate surface; a cover of 0.95.
- **The radiation step:** E_rad inflated 10⁵-fold.
- **The far field:** inflated 10⁴-fold.
- **The column:** removed (a = 0); its depth power's sign flipped.
- **The density:** a mass density used as an energy density.
- **The guards:** a row labelled "positive"; the status row claiming green.

The 1.70 control fails exactly where X3 says it should.

## Named hypotheses

- **Yours:** H-SEPARATE-JOINED-THROUGH-DIMENSION (152 (1)); H-BRIEF-EVOLUTION, an option to check (152 (2));
  H-HALF-IS-OURS (157); H-HOLD-AT-BOUND (158 (2)); H-FIXED-SIZE (162); H-CORRIDOR-IN-BULK (179/180); seated (Z) (183,
  187 (3)); H-NO-MATTER-FREE-PLANES (184); H-PAIR-AXIOM (193), not used here.
- **The board's:**
  - H-FAR-MODEL, now load-bearing only through the join column's geometry at depth ≥ R_reach;
  - H-FAR-FIELD-EXTENSION, the two test extensions in X8;
  - the cover U = 1.05·R_reach.

## Proposed change to the theorem's B4c row (not made here)

> **B4c** the far boundary T strictly untrapped, uniformly in time: an ellipsoidal T, W ≥ √3·U (1.74·U with eq. (17)'s
> far field), U = 1.05·(R_core + hold), is untrapped at every ℓ and every N before the closing (exact, within
> H-FAR-MODEL; z3); radiation after the closing cannot trap it (margin 2.8×10⁴ at the example README; an estimate). —
> **READING**: H-FAR-MODEL, narrowed to the join column's geometry at depth ≥ R_reach, which B3/B4d must supply.

That would remove, from the current row: the "ℓ > 2R_reach" condition; the "~23 m in corridor units" figure (already
stale against o3_write's write); eq. (17) as the source of the reach; and "margin ~5".

## Re-run

```
python3 lemmas/b4c_far.py               # the report, every row labelled
python3 lemmas/b4c_far.py --selftest    # 12 checks, ~30 s
python3 lemmas/b4c_far.py --mutants     # 22 mutations, each must make its check fail, ~80 s
python3 lemmas/b4c_far.py --json PATH
```

## History

- **First written 2026-10-09.** It has not been verified and nothing is seated.
- The item-186 window checker's ellipse (its check discrepancy 2, scanned at W/U = 1.70 and 1.74) is the starting point.
  The exact threshold √3, the proof, the far-field note and the column analysis are new here.
