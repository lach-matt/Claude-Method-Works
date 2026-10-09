# B4d simulation, phase 2: two pieces of our plane, facing across the extra dimension (computed, READ and deduced; not verified; not seated; 2026-10-09)

*First headed* "(… not verified; not seated …)". The instrument is `sim2_facing.py`, selftest 14/14, about 100 seconds.
The map of the bulk is banked in `sim2_bank.json` (0.9 MB; about 22 minutes to regenerate on three CPUs, 40 CPU-minutes),
and the READ sources, verbatim with pages, are in `sim2_reads.json`.

**In plain words.**
- **Decided, with no simulation needed.** Two pieces of our own plane that carry no matter, at our tension, cannot face
  each other across a static bulk. That holds at every ℓ and at every depth. Within one universe under the theorem's
  clause (B), the question is settled.
- **The one way that is left.** Suppose position 2's piece carries the README's stress, and that stress obeys the NEC
  (your 117/120). Then the point where it comes nearest to our piece can only lie inside the corridor object's own
  throat, in a band of depths: from a depth y\* down to the depth y_s where the bulk becomes singular. No other part of
  the bulk the board could compute allows it, at any ℓ tested.
- **What the band is, and what it is not.** It is a necessary condition at that one nearest point. It does not say that
  such a piece exists. Positive energy there needs ℓ ≥ 49.86m. At ℓ ≤ 4m the band lies where the bulk's curvature is
  more than 100 times the black string's.
- **What only you can settle.** That one way rests on a reading of the board's, H-README-ON-P2. As worded, your 130 (1)
  (*"no added matter"*) and 136 (2) (*"released at position two at the closing of the horizon"*) read against it.
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## What you said

- **Item 168:** *"My sense: positions, one universe"*. The option text that went with it is the board's.
- **Item 152:** (1) *"two separate positions connected by/reached through a dimension."* (2) *"It could very well be
  possible, so let's consider this an option and check it."*
- **Item 126:** *"The corridor will always entangle separate plane position using the shortest distance needed. The
  second position isn't built far away, it is realized in the same place the position 1 occupies while the corridor
  exists"*.
- **Item 127 (1):** *"1 - yes"* (the planes coincide).
- **Item 116:** (a) *"No, separate"* (the address is not a trajectory). (b) *"Some trajectories are confined within
  specific dimensions, some pass through dimensions. The length of the corridor is dependent on the trajectories  needed
  to reach position 2."*
- **Item 117:** *"Trajectory does not change size in width, but rather length."* and *"The NEC appears broken, but is
  not"*.
- **Item 120:** *"the NEC only ever appears to break, but never does"*.
- **Item 123:** *"forget the coin metaphor."*
- **Item 118:** *"Yes: law and history"*.
- **Item 119:** *"The address is always precise to the input."*
- **Item 129 (1):** *"the corridor is a bridge, so it adds nothing to either position."*
- **Item 130 (1):** *"no added matter. And in my model a black hole is not matter, it is what the mouth at position 1
  looks like."*
- **Item 136:** (2) *"released at position two at the closing of the horizon"*. (3) *"It is a bridge, not a physical
  place."*
- **Item 138:** *"I keep saying, it is multi-universal."* and *"The difference is the relative laws of physics to that
  universe"*.
- **Item 139:** (1) *"1 - yes"* (ours positive, position 2's plane negative). (2) *"positive, and you have to prove
  it."* (4) *"why are you still chasing distance/speed? This was ruled out"*.
- **Item 140:** *"Our math is not dependent on k, k is dependent on our work."*
- **Item 141:** *"I suggest the planes are static"*.
- **Item 143 A:** *"the only thing that can cross is that which can cross the horizon of a black hole."*
- **Item 155 (2):** *"Yes, in bits"* (the corridor's length is in bits).
- **Item 157:** *"we already have at least half the model, our current universe."*
- **Item 158 (4):** *"This too is a question for the math."*
- **Item 161:** *"my inclination is yes"* (the corridor stays regular through the write).
- **Item 162:** *"containing both mouths and throat at once. The throat doesn't change size"*.
- **Item 166:** *"Both planes at once"*.
- **Item 101 (7):** *"distance is irrelevant. The device only sees the two positions as one, never the distance between
  the two."*
- **Items 169–171, since this phase was designed:**
  - 169: *"One does not travel through time alone. One can only warp travel through spacetime."*
  - 170: *"Position 1's clock gets absorbed into position 2's clock. However, time according to the object transported,
    because memory is part of the reconstruction, will always be relative to the clock of position 1, like an astronaut
    taking relative time with him"*.
  - 171: *"might we be able to derive a basic teleportation from it, not time, just space?"*
- **The theorem's clause (B)** (the theorem's words, not yours): *"A vacuum five-dimensional bulk carries the corridor.
  The plane is free of matter, at the Randall–Sundrum tension."*

## Why this phase is static, at one moment

- **Your 141 is the reason:** the planes are static.
- **Items 169 and 170 are consistent with it.** A static bulk compares the two pieces at one moment, with no time offset
  between them. That fits 169 (no travel through time alone) and 170 (the world arrives on position 2's clock). This
  phase computes no clock, so it neither tests 170 nor uses it.
- **Item 171.** The board offered, for discussion, that the corridor within one universe already is space-only
  teleportation. This phase is that corridor's geometry, read at one moment.

## The setup

- **Position 1's piece, P1,** sits at depth y = 0 and carries eq. (17) at the Randall–Sundrum tension (clause (B), 157).
  The bulk grown from it is the owner's: `b4_static.py`'s exact series, vacuum, Λ₅ = −6/ℓ², static and spherical.
- **Position 2's piece, P2,** is a second piece of the same mirrored plane (H-Z2-PIECES).
  - Each piece is one-sided toward the bulk between them, which this note calls the slab. The other side of each is its
    mirror image.
  - How the two pieces join far away is the address's business (116 (a)), and is OPEN G. Nothing here is a crease on P1.
  - Your 166's *"Both planes at once"* is read, within one universe, as both pieces present at once inside the one
    object (H-BOTH-PIECES-AT-ONCE).
- **Facing** (H-NEAREST-APPROACH). P2 faces P1 when the bulk's nearest approach from P1 to P2 is attained at a point p₂
  of the static region. The case where it is only approached, down the throat, is treated separately (S7).
  - **The depth of p₂ is a property of the bulk,** like y_s. It is never the corridor's length (155 (2): bits), and no
    distance is ever an output (101 (7), 139 (4)).
- **Two numbers at each point of the bulk** decide everything below:
  - **w_r = κ_r − κ_t:** how much faster the radial direction stretches than time, going into the bulk;
  - **w_θ = κ_θ − κ_t:** the same for the angular directions.
  - Here κ_X = ½ ∂_y ln X, for X = A (time), B (radial) and C (angular). The warp cancels from both.
- **The slab is regular in the strict sense** when the piece sits above the singular depth y_s (H-REGULAR-SLAB). The
  curvature against the black string's, K/K_bs, is reported at 10, 30 and 100 alongside it.
- **Units:** m = 1; ν = 2/κ₅², the one-sided Israel factor; σ_RS = 3ν/ℓ, the Randall–Sundrum tension.
- **The ℓ scanned:** ∞, 32m, 16m, 8m, 4m, 2m, m, m/2, m/4. Our plane stays at our tension (s = 1). There is no tension
  scan: that is phase 3's direction Δs.

## What follows

**S1. Lemma T: the trap** (deduced; its first step computed exactly).
- **T1.** Going into the bulk, the mean stretching rate a = (κ_t + κ_r + 2κ_θ)/4 obeys a′ = 1/ℓ² − a² − Π·Π/4, where Π is
  the part that differs by direction.
  - On the owner's exact series at r = 2.15m this holds with residual exactly zero through y¹², at ℓ = ∞ and ℓ = m.
  - With the bulk curvature's sign flipped, the residual is 2/ℓ² at y⁰ (selftest C3).
- **T2.** In a static bulk K is diagonal, so Π·Π ≥ 0.
- **T3.** At P1, a = −1/ℓ (Gauss, with eq. (17)'s R⁽⁴⁾ = 0).
- **T4.** So a ≤ −1/ℓ at every depth the chart reaches: ã ≡ a + 1/ℓ ≤ 0. The comparison solution e·tanh(ey − artanh s₁)
  has the fixed point −1/ℓ at s₁ = 1 (sympy).
- **An exact anchor:** at r = 3m, ã = −(1/4374)(y³ + 5ey⁴) + O(y⁵), that is −(R_abR^ab/12)(y³ + 5ey⁴).
- **On the map:** ã < 0 at every one of the 4,406 verified points (the largest is −6×10⁻¹³).
- **Precedents (READ):** Witten–Yau's Riemannian Riccati, eqs. (2.28)–(2.29), PDF pp.9–10; FGPW's *"The one general
  restriction … is A''(r) ≤ 0. This rules out a second anti-de Sitter boundary"*, PDF p.14. Stage 7 K1 held this for
  parallel sheets; T holds it for every column.

**S2. Lemma C: what a facing piece sees at its nearest point** (deduced; the comparison step is standard, not READ).
- **The statement.** At p₂ the facing piece bends at least as much as the level surface through p₂: k_t(P2) = −κ_t
  exactly, and k_spatial(P2) ≥ −κ_spatial.
- **What it needs.** A static region (lapse > 0) and no focal point of P1 before p₂. At a focal point, Calabi's barrier
  trick (standard, not READ).
- **Where it is not used:** where the nearest approach is not attained (S7's approach down the throat).

**S3. Corollary T5c: two matter-free pieces cannot face each other** (deduced; decided).
- **The bound.** A matter-free mirrored P2 reads tension s₂ ≤ ℓ·a(depth) ≤ −1, at every depth and every ℓ. It reaches −1
  only if Π ≡ 0 all the way, which is the black string, not eq. (17).
- **The general form,** for the controls: s₂ ≤ tanh(depth/ℓ − artanh s₁). At our s₁ = 1 the depth drops out.
- **The equality control.** The AdS₄-sliced wedge, dρ² + cosh²(ρ/ℓ)g₄ (Witten–Yau's eq. (1.2), PDF p.4, is its
  Riemannian form, READ). It solves Einstein's equations, and a facing sheet there reads s₂ = s₁ exactly. A sinh warp
  fails Einstein's equations (selftest C11).
- **What follows within one universe.** Under clause (B) on both pieces, two positions cannot face each other. This is
  decided now.
- **What the facing piece reads instead** (H-LAW-READ-BY-TRACE, a reading: the trace part reads a law, the part that
  carries the NEC is history). Its tension is −1 or below. Your 139's negative plane is between universes, so that
  reading points to phase 3.

**S4. Lemma W: where a facing piece can obey the NEC** (deduced).
- **Statement.** Suppose P2 is static and mirrored, its total stress obeys the NEC, and its nearest point p₂ is in the
  static region. Then **w_r ≥ 0 and w_θ ≥ 0 at p₂.** That holds for any tension and any split into tension and matter.
- **Proof.** The NEC on P2 is k_t·I ≥ k_spatial, from the local Israel lemma ρ + p_i = ν(k_t − k_i). Lemma C gives
  k_t = −κ_t and k_spatial ≥ −κ_spatial. Together: κ_i ≥ κ_t in every spatial direction.
- **Checked (selftest C2):**
  - the identity k_t·I − k_spatial = diag(w) − H holds exactly;
  - of 20,000 random samples, 1,427 obey the NEC and none has a negative w;
  - with the comparison reversed, 1,999 counterexamples appear.
- **What it does not use:** any bulk field equation. So it survives matter in the bulk (158 (4)). Only the map (S9)
  assumes a vacuum bulk.
- **Stage 5's F5 and stage 6's J4** are its level-surface member, the best case for the energy density.

**S5. Near our plane, its own apparent NEC shortfall forbids facing** (computed, exact).
- **The leading orders:** w_r = R̂_rad(y + 3ey²) + O(y³) and w_θ = R̂_tan(y + 3ey²) + O(y³), with
  - R̂_rad = −2m(r − 2m)/(r²(2r − 3m)²), negative at every r > 2m;
  - R̂_tan = m/(r(2r − 3m)²), positive.
- **Exact values:** −2/81 and 1/27 at r = 3m, with y² terms −1/27 and 1/18 at ℓ = 2m; −12000/312481 and 2000/7267 at
  r = 2.15m. Checked against `b4d_stage5.wall_exact`, `sim1_transition.eq17_rkk` and `b4d_stage7.slab_trace` (selftest C4).
- **What this is.** R̂_rad is exactly phase 1's radial NEC shortfall of eq. (17) (SIM1 S4/S5): the appearance of your
  117/120. Here it is what forbids facing near our plane (H-APPEARANCE-IS-THE-OBSTRUCTION). It vanishes only at the
  object, r = 2m.
- **A picture (S11):** bulk light sent along a level surface bends back toward our plane wherever w_r < 0. No ray is
  identified with any of your trajectories (118).

**S6. The throat is the one place the shortfall vanishes** (STRUCTURAL, with the near-horizon geometry computed).
- **At r = 2m** eq. (17) is AdS₂ × S², both of radius 2m: R^a_b = diag(−¼, −¼, ¼, ¼)/m² (selftest C6).
- **Over it the bulk is homogeneous,** so w_r ≡ 0 there: AdS₂'s boost symmetry makes the radial and time equations
  identical (sympy, selftest C7). This rests on uniqueness in the analytic class (standard, not READ).
- **The horizon over the throat** is AdS₂'s horizon × S² at every depth. It is vertical, and one horizon spans the slab
  (H-ONE-OBJECT-IN-GAP; your 162's one object).

**S7. The bulk over the throat** (computed by ODE; the constraint held to 3×10⁻¹² relative).
- **It ends at a depth y_s^th(ℓ),** where the AdS₂ factor shrinks to zero. That is a curvature singularity: K rises
  without bound.
- **Along the way:** ã ≤ 0 (T4), and w_θ > 0 everywhere.
- **A facing level surface there carries** ρ = ν(p + 2q), ρ + p_r = 0 and ρ + p_θ = ν(q − p). Its matter, once our
  tension is subtracted, is ρ_m = ν(p + 2q − 3/ℓ).
- **The approach down the throat** (deduced, at first order in x = r − 2m). A piece whose nearest approach is only
  reached as r → 2m must bend no more than x·W₁ allows along the way. Where W₁ < 0 that is impossible, so this case also
  needs depth ≥ y\*.

**S8. The band** (computed).
- **One step off the throat,** w_r = x·W₁(y) + O(x²). W₁ starts as −y/2 at our plane and turns positive deep in. Its
  first zero is y\*, and the admissible band is [y\*, y_s^th).

| ℓ | y_s^th | y\* | y\*/y_s | y_K at 10 / 30 / 100 K_bs | K(y\*)/K_bs | ρ_m(y\*), ν/m (σ_RS) |
|---|---|---|---|---|---|---|
| ∞ | 2.5536m | 1.7901m | 0.701 | 1.633 / 1.895 / 2.087m | 18.3 | +0.1215 |
| 32m | 2.3744m | 1.7286m | 0.728 | 1.511 / 1.760 / 1.941m | 25.4 | −0.0686 (−0.731) |
| 16m | 2.2247m | 1.6720m | 0.752 | 1.407 / 1.646 / 1.818m | 34.9 | −0.263 (−1.403) |
| 8m | 1.9868m | 1.5709m | 0.791 | 1.239 / 1.464 / 1.621m | 64.5 | −0.668 (−1.782) |
| 4m | 1.6591m | 1.4053m | 0.847 | 1.010 / 1.214 / 1.350m | 199 | −1.562 (−2.083) |
| 2m | 1.2803m | 1.1673m | 0.912 | 0.800 / 0.947 / 1.048m | 1.35×10³ | −3.861 (−2.574) |
| m | 0.9139m | 0.8812m | 0.964 | 0.643 / 0.718 / 0.773m | 2.69×10⁴ | −12.10 (−4.032) |
| m/2 | 0.6101m | 0.6042m | 0.990 | 0.474 / 0.509 / 0.536m | 2.14×10⁶ | −58.61 (−9.769) |
| m/4 | 0.3864m | 0.3856m | 0.998 | 0.319 / 0.336 / 0.349m | 5.91×10⁸ | −438.1 (−36.51) |

- **Positive energy in the band** (ρ_m ≥ 0 at y\*, the band's best point): **ℓ ≥ ℓ_W = 49.86m** (e ≤ 0.020057). The
  maximum over the whole band gives the same 49.86m.
- **The band's shallow edge lies below 30 K_bs** for ℓ > 21.05m, and below 100 K_bs for ℓ > 5.82m. It never lies below
  10 K_bs: in the flat limit it is 18.3 times K_bs, and y\* sits 0.157m deeper than y_K(10).
- **ρ_m is given in ν/m,** since σ_RS → 0 in the flat limit.

**S9. The map on the owner's bulk** (computed; raw Padé as evidence).
- **The columns:** 13 radii from 2.005m to 10m, at each of the 9 ℓ, order 32: raw Padé of Ã, B̃ and C̃. Stage 5's
  doublet-removing `_clean` is not used; selftest C5 shows it moves w_r by 36% at y = 0.02m.
- **A point counts as verified** when:
  - two Padé orders agree on A, B, C to 10⁻⁴ and all three are positive (`b4_static.py` S3's rule);
  - no real pole or zero of those orders, other than a Froissart doublet, lies above it;
  - the two orders agree on w_r and w_θ (to 10⁻⁶ plus 0.1%). This last rule only removes points; it removed 62.
- **Off the throat, never:** at every one of the 3,861 verified points at r ≥ 2.05m, or at ℓ ≤ 2m: w_r < 0, w_θ > 0 and
  ã < 0. Over all 4,406 verified points, w_θ ≥ 9×10⁻⁶.
- **Near the throat, past a depth:** w_r ≥ 0 appears only at r = 2.005, 2.01 and 2.02m, only at ℓ ≥ 4m, and only past
  the depth where it changes sign:

| ℓ | r = 2.005m | r = 2.01m | r = 2.02m | the throat's y\* |
|---|---|---|---|---|
| ∞ | 1.821m | 1.854m | 1.924m | 1.790m |
| 32m | 1.758m | 1.790m | 1.857m | 1.729m |
| 16m | 1.700m | 1.730m | 1.795m | 1.672m |
| 8m | 1.597m | 1.625m | 1.687m | 1.571m |
| 4m | 1.428m | none above its verified top, 1.438m | not reached (top 1.365m) | 1.405m |

- **The curvature there,** K/K_bs at the shallowest admissible point (two Padé orders agree): 23.5, 32.4 and 47.3 at
  ℓ = ∞ (r = 2.005, 2.01, 2.02m); 31.9, 45.3, 68.7 at 32m; 44.8, 66.1, 105 at 16m; 101, 102, 311 at 8m; 294 at 4m.
- **Not reached at ℓ ≤ 2m.** There the r = 2.005m column is verified only to depths below y\*: to 1.139, 0.858, 0.544
  and 0.328m, against y\* = 1.167, 0.881, 0.604 and 0.386m. Such columns count neither way. The one near-throat column
  verified past y\* at ℓ ≤ 2m (r = 2.01m at ℓ = 2m, to 1.174m) still has w_r < 0 there, as expected: at larger x the
  sign change lies deeper (the table above).

**S10. The throat and the owner agree** (computed).
- **The sign change, extrapolated to x → 0** (2y₀(2.005m) − y₀(2.01m)): 1.7888, 1.7273, 1.6706 and 1.5693m at ℓ = ∞,
  32m, 16m, 8m, against y\* = 1.7901, 1.7286, 1.6720, 1.5709m. All within 0.1%.
- **W₁ against the owner:** W₁(1.088m) = −0.3810, against w_r(2.005m)/0.005 = −0.3830 (flat, order 24): 0.5%.
- **w_θ and ã at ℓ = 2m,** y = 0.13 and 0.26m: within 3.9% of the throat ODE at r = 2.005m and 7.6% at 2.01m. The gap
  doubles with x (ratio 1.95–1.97), and the extrapolation to x → 0 meets the ODE to 0.19% (selftest C9).
- **The singular depth:** y_s^th sits 1–3% below the r = 2.005m column's Padé singularity: 0.9139 against 0.926m at
  ℓ = m, and 1.2803 against 1.296m at ℓ = 2m. Order 32 runs high, as stage 5 found.

**S11. Lemma N** (deduced; sympy).
- Γ^y_ab = −½∂_y g_ab, so bulk light sent along a level surface has ÿ = w_r·B·ṙ² (selftest C12).
- **Corollary W.** In any warped product w ≡ 0, so W is marginal everywhere: the black-string and RS2 control.
  Schwarzschild data give w_r = w_θ = ã = 0 exactly, the series terminating (selftest C11).

**S12. The decision, per ℓ** (deduced from S7–S9).

| ℓ | decision | on the owner's bulk | regular at 10 / 30 / 100 K_bs | y\* < y_s | positive energy |
|---|---|---|---|---|---|
| ∞ | THROAT-BAND | CONFIRMED (1.8% from y\*) | no / yes / yes | yes | yes |
| 32m | THROAT-BAND | CONFIRMED (1.7%) | no / yes / yes | yes | no |
| 16m | THROAT-BAND | CONFIRMED (1.7%) | no / no / yes | yes | no |
| 8m | THROAT-BAND | CONFIRMED (1.7%) | no / no / yes | yes | no |
| 4m | THROAT-BAND | CONFIRMED (1.6%) | no / no / no | yes | no |
| 2m, m, m/2, m/4 | THROAT-BAND | EXPANSION-ONLY (not reached) | no / no / no | yes | no |

- **No ℓ is WIDE, and none is NONE.**
- **Regularity is settled** (all three thresholds agree) only at ℓ ≤ 4m, and there the band lies in the singular layer.
  At ℓ ≥ 8m the answer depends on the threshold, so it is not settled. In the strict sense (y\* < y_s) the band is
  regular at every ℓ.
- **CONFIRMED** means an owner column at r ≤ 2.02m turns admissible within 5% of the throat's y\*.

**S13. The hand-off to phase 3** (deduced).
- **What the slab side reads.** At any nearest point, the slab side of a facing piece reads s_slab = ℓ·a(depth) ≤ −1.
  That holds for curved pieces too; stage 7's K1 and K3 went only to parallel planes.
- **What phase 3 must supply.** Two-sided, σ₂/λ_RS = (s_slab + s_outer)/2.
  - For your 139's −1/3 the outer side needs s_outer ≥ +1/3; for stage 7 K5's −1/6, s_outer ≥ +2/3.
  - Either way the outer side decays, which is stage 7 K4's finding. The unit (K4) and the image count (K5) stay put to
    you.
- **Where W stops.** W binds only the slab side. The outer bulk's own law is phase 3's first direction (Δℓ).
- **The within-universe rows (Δs, Δℓ | stress):**

| row | result |
|---|---|
| (0, 0 \| no matter) | EMPTY (S3) |
| (0, 0 \| NEC) | the throat band (S12) |
| (0, 0 \| NEC and positive energy) | ℓ ≥ 49.86m only |

- **What phase 3 can show.** If its rows admit facing outside the throat, the within-universe row is the narrower one:
  an ordering, measured. If they do not, there is no ordering in this form. Your 116 (b)'s *"likely smaller"* is tested,
  never assumed.
- **No length is computed.** Your corridor's length is in bits (155 (2)); within one universe it is the history bits
  only.

**S14. The escapes left** (STRUCTURAL / OPEN; none hidden).

| Escape | Status |
|---|---|
| E-NS: non-static (your 152 (2)) | scheduled as phase 2b-ii, the brief evolution |
| E-ROT: K not diagonal (your 141's internal motion) | open |
| E-BULK: bulk matter with Ric(n,n) < −4/ℓ² | T fails; W stands |
| E-ASYM: P2 not mirrored, with its own outer side | phase 3 |
| E-PASS: no second sheet; the far end of our own plane reached through the horizon | the next instrument, `sim2_passage` |
| E-G: how P2 closes globally | phase 2b-i |
| Outside the analytic class | open |

## Where the computation differs from the design

The design's expected values came from a scratch pilot, which is not board evidence. The instrument computes everything
itself, and where the two differ the computed value stands.

1. **y_s^th, fourth decimal.** The instrument follows the throat bulk until α = 10⁻⁹; the pilot stopped at α = 10⁻³. The
   singular depth comes out 3–6×10⁻⁵m deeper: 2.5536 (not 2.5535) at ℓ = ∞, 1.9868 (1.9867) at 8m, 0.9139 (0.9138) at m,
   0.6101 (0.6100) at m/2, 0.3864 (0.3863) at m/4. Every other table entry, ℓ_W and ℓ_c agree to the digits given.
2. **CONFIRMED reaches down to ℓ = 4m,** not only ℓ ≥ 8m. At 4m the r = 2.005m column turns admissible at 1.428m, 1.6%
   from y\* = 1.405m.
3. **The sign-change depths,** found by root-finding rather than read off a grid: 1.821, 1.854 and 1.924m in the flat
   limit (pilot ≈ 1.80, 1.88, 1.93); 1.758, 1.700 and 1.597m at r = 2.005m for 32m, 16m, 8m (pilot ≈ 1.75, 1.69, 1.58).
4. **Verified tops at r = 2.005m for ℓ ≤ 2m:** 1.139, 0.858, 0.544 and 0.328m (pilot 1.115, 0.833, 0.557, 0.323). All
   still lie below y\*, so "not reached" stands. The difference is the verification rule (items 5 and 6).
5. **The real-pole guard.** Applied to every real pole, as specified, it would cut the r = 2.005m column at ℓ = 8m at
   1.432m, below y\* = 1.571m, on a Froissart doublet of C̃ at Padé order (16, 16), a pole and a zero that coincide to
   three decimals. Doublets are exempted by stage 5's own rule (a zero within 2×10⁻³), and the two-order agreement on
   w_r and w_θ is added instead. That removed 62 points.
6. **Padé honesty (C5).** The raw Padé matches the converged partial sums to 4×10⁻¹⁵ (y ≤ 0.4m), and the order-24 sums to
   4×10⁻⁸ at 0.5m. At 0.6m the specified 10⁻⁷ fails (1.9×10⁻⁶), because the order-24 partial sums have not converged
   there: they are 2.5×10⁻⁶ from the order-32 sums, and the raw Padé is nearer (5.6×10⁻⁷). Through `_clean`, w_r at
   0.02m moves by 2.9×10⁻⁴, which is 36% (the pilot's 40% is reproduced, its 2×10⁻³ is not).
7. **Throat against owner (C9).** At ℓ = 2m, ã at r = 2.005m is 3.9% from the ODE, not within 3%; at 2.01m, w_θ and ã are
   4.4% and 7.6% off. The gap is the O(x) correction: it doubles with x, R_abR^ab itself falls 3.9% between r = 2m and
   2.005m, and the extrapolation to x → 0 meets the ODE to 0.19%. The check now tests that.
8. **The throat constraint (C7)** holds to 3×10⁻¹² relative at ℓ = m/4 (4×10⁻¹⁴ or better at ℓ ≥ 2m), not 10⁻¹²; the
   check uses 10⁻¹¹.
9. **The local Israel lemma cannot fail through the trace,** which drops out of ρ + p_i. C2's mutation is the one-sided
   factor instead; a trace error is caught by C1's calibration, where it gives s = 2/3.
10. **A page.** Witten–Yau's eq. (2.28) is on PDF p.9; eq. (2.29) and *"we can replace the Einstein equation …"* are on
    p.10.
11. **Run costs.** The selftest takes about 100 s, not 3 minutes (the O(x) derivation takes 6 s, not 35 s). The
    regeneration took 22 minutes on three CPUs of a shared machine. The bank is 0.9 MB.

## Verdict

- **Decided (S3).** Within one universe, under clause (B) on both pieces, two positions cannot face each other across a
  static bulk.
  - **For B4d:** the within-universe member under clause (B) is refuted under M-IRREFUTABLE, on this conjunction:
    static (your 141); mirrored pieces at the Randall–Sundrum tension with one ℓ (clause (B); H-ONE-UNIVERSE-ONE-LAW,
    the board's reading of your 138); a vacuum Λ₅ bulk with diagonal K; the nearest approach in the static region or down
    the throat; eq. (17) on P1 (your 157).
  - **For O3:** unchanged.
- **Computed, on H-README-ON-P2 only (S12).** THROAT-BAND at every ℓ.
  - Position 2's piece can face ours only inside the object's throat, at depths from y\* to y_s: y\*/y_s = 0.70 in the
    flat limit, 0.998 at ℓ = m/4.
  - Confirmed on the owner's bulk at ℓ ≥ 4m (S10: to 0.1% after extrapolation).
  - It is necessary, not sufficient. It is not a configuration that exists, and it is not B4d green.
- **What it would mean for B4d.** One candidate class, located inside the one object (your 162). Below y_s the slab is
  regular in the strict sense, and stage 5 F2's singular surface is cut away; your 161 would then be met statically, for
  any length of hold.
- **What does not move.**
  - At ℓ ≤ 4m the band lies in the singular layer under all three thresholds, so it is closed there in practice.
  - At ℓ ≥ 8m the regularity verdict depends on the threshold, so it is not settled.
  - Positive energy needs ℓ ≥ 49.86m.
  - Whether a whole piece P2 exists over the band is phase 2b-i, a free-boundary problem.
  - For O3: for this member, stage 5's 8–16 clocks no longer bind O3's write of at least 2.0×10⁵ clocks (`o3_write.py`
    W3), since the band is static. O3 moves to READING only together with 2b-i.
- **A finding recorded, not repaired.** Your 127's coincidence, read as the depth going to zero (the board's
  H-COINCIDE-AS-LIMIT), is excluded: the depth is at least y\* > 0. Your 152 (1), two separate positions reached through a
  dimension, is consistent with it.
- **On k:** ℓ_W and ℓ_c are consequences of this work in the sense of your 140, conditional on its readings. They are not
  hypotheses about k.
- **No status moves.** B4d stays OPEN, and O3 stays OPEN as B4d's.

## Questions for you

1. **H-README-ON-P2.** While the corridor holds, may position 2's piece carry the README's stress, a stress that obeys
   the NEC? The computed band (S8, S12) exists only if it may. As worded, your 130 (1) (*"no added matter"*) and 136 (2)
   (*"released at position two at the closing of the horizon"*) read against it. If it may not, the within-universe
   facing route is closed by S3 alone, and the live route stays stage 6's H-EQ17-ON-P2, which is phase 3.
2. **For correction, the board's other new readings:**
   - H-Z2-PIECES: positions 1 and 2 are two pieces of our one mirrored plane, each one-sided toward the slab;
   - H-NEAREST-APPROACH: facing means the nearest approach is attained;
   - H-POSITIVE-ON-P2: your 139 (2)'s *"positive"* applied to position 2's matter once the tension is subtracted, which
     is what sets the bound ℓ ≥ 49.86m.

## Named hypotheses

- **Yours:** 168 (H-PHASES-BY-TRAJECTORY), 123 (H-NEC-NEVER-VIOLATED), 155 (H-LENGTH-IN-BITS), 116 (a)
  (H-ADDRESS-SEPARATE), 141 (H-STATIC-PLANES), 162 (H-ONE-OBJECT, H-FIXED-SIZE), 152
  (H-SEPARATE-JOINED-THROUGH-DIMENSION). 169 and 170 are consistent with a static, one-moment analysis and are not used.
- **The theorem's:** clause (B).
- **The board's:**
  - H-ONE-UNIVERSE-ONE-LAW (one universe, one ℓ, one tension: the fold design's reading of 138);
  - H-Z2-PIECES, H-NEAREST-APPROACH, H-README-ON-P2 (the computed branch only), H-POSITIVE-ON-P2,
    H-LAW-READ-BY-TRACE, H-APPEARANCE-IS-THE-OBSTRUCTION, H-BOTH-PIECES-AT-ONCE, H-REGULAR-SLAB;
  - H-COINCIDE-AS-LIMIT (excluded here, recorded);
  - a static bulk with diagonal K; a vacuum bulk with Λ₅ = −6/ℓ² (the map only; W needs none);
  - B4b's locally analytic class, and uniqueness in it (S6);
  - Padé as evidence, the verification rule of S9, and the radii (2.005m to 10m) and ℓ (∞ to m/4) tested.
