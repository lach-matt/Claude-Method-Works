# Wall C, first piece: a vacuum Randall–Sundrum bulk carrying the corridor is shown to exist near the plane (M-RULINGS item 149; derived and computed; verified once; not seated; 2026-10-07)

*First headed* "Wall C, first piece: a bulk carrying the corridor exists near the plane (… not verified; not seated;
2026-10-07)". The first draft said the bulk is "unique there" without qualification, said "near the plane, one now is"
known, skipped constraint propagation, stretched a long-range result to short range, and estimated the reach as the
throat's size alone. All five are corrected (History).

## Where this starts

- **Wall C asked for a five-dimensional bulk carrying your corridor.**
  - Maartens: one *"has not been found"* (gr-qc/0312059, quoted in SIGNDIM.md). That means an explicit bulk.
  - STATUS's wall C is the global bulk.
  - The board's record already implied that *some* local bulk exists for any analytic metric (Dahia–Romero, READ in
    BULKWARP.md). What it left uncontrolled was the plane's matter. Seahra–Wesson: *"we lose control of the jump in
    extrinsic curvature"*.
- **The question here:** one vacuum Randall–Sundrum plane whose own metric is your corridor.
  - The plane's metric is eq. (17) at r₀ = 2m.
  - Its extrinsic curvature is K_μν = −(1/ℓ)·g_μν. This comes from the junction condition with mirror symmetry and the
    Randall–Sundrum tension (Maartens–Koyama eq. 68 with T = 0, READ in throatbulk.py).
  - The bulk is vacuum with Λ₅ = −6/ℓ².
- **Why one plane, and the limit of that:** on static, face-to-face planes the pair is one RS II plane **at long range**
  (static.py S2b, zero modes only).
  - Here the construction is used within ~r₀ and ~ℓ of the plane, where the massive modes S2b did not read live.
  - So treating the pair as one plane at short range is the board's hypothesis, H-ONE-PLANE-NEAR. What is shown below is
    about a single vacuum RS plane carrying eq. (17).
- **The instrument:** `localbulk.py`, which imports throatbulk.py by path. Selftest 8/8.
  - **Genuine checks:** four (L1, L3 twice, L5).
  - **Controls:** two (L1b, L1c).
  - **Marked STRUCTURAL:** two (L1, L1d), plus L2, which has no check.

## What the mathematics gives

### 1. Your corridor satisfies the Gauss condition (L1)

- **The condition.** For a plane in this bulk, R⁽⁴⁾ = 2Λ₅ + K² − K·K.
  - When K = c·g, the right side is 2Λ₅ + 12c².
  - With c = −1/ℓ that is −12/ℓ² + 12/ℓ² = 0 (STRUCTURAL).
  - So the condition is that the plane's curvature scalar vanishes.
- **Eq. (17) at r₀ = 2m has R⁽⁴⁾ = 0 exactly** (computed). The condition holds.
- **Control L1b:** Schwarzschild–de Sitter (R = 12/L²) fails it.
- **Control L1c, which tests the formula itself:** the de Sitter slicing of AdS₅, dy² + ℓ²sinh²(y/ℓ)·dS₄.
  - Each slice has c = coth(y/ℓ)/ℓ and R⁽⁴⁾ = 12/(ℓ²sinh²(y/ℓ)). That equals 2Λ₅ + 12coth²(y/ℓ)/ℓ² (computed).
  - The same formula with the K-terms' sign reversed fails.
- **What the check does not see (L1d, STRUCTURAL).**
  - **The sign of K.** c = +1/ℓ passes too. The positive-tension reading, and which side the bulk lies on, rest on
    Maartens–Koyama's sign convention. The mirror-symmetric bulk keeps the y > 0 solution and reflects it.
  - **Mirror symmetry is not needed.** Each side passes on its own (2Λ_side + 12/ℓ_side² = 0). So two unequal sides,
    k_L ≠ k_R as in static.py, work too, provided each has K = −g/ℓ_side.

### 2. The Codazzi condition holds identically (L2, STRUCTURAL)

- D^μK_μν − D_νK = R_AB n^A e^B_ν. That is zero in this bulk, and the left side vanishes identically for K = c·g with c
  constant. No check is needed or given.

### 3. The corridor's data are analytic, through the horizon and beyond (L3)

- **The coordinate.** ρ is stability.py's chart, dρ = √(F/H) dr.
- **Through the horizon.** With r = 2m + u², the closed form is dρ/du = 2√(m/2 + u²) exactly (computed). It begins
  √(2m).
  - It is even in u. So ρ − ρ_H is odd and r(ρ) is even, with its minimum at the horizon.
  - Continuing through the horizon leads into a **second r > 2m exterior**, not into r < 2m. That is the corridor's
    throat (plane.py P1).
- **Where the series stops.** The u-series converges for |u| < √(m/2), up to the branch point at r = 3m/2.
  - **The strip 3m/2 < r < 2m is Riemannian** (computed at r = 7m/4: g_tt = 1/7, g_rr = 7, both positive). It is not part
    of the Lorentzian corridor, so the branch point is not in the domain.
- **Away from the horizon.** For r > 2m the data are rational in r, or the root of a positive analytic function. So they
  are analytic.
  - **H-ANALYTIC-DATA is therefore established, not assumed.** The first draft called it assumed.

### 4. So a local vacuum bulk exists, unique among analytic solutions (L4)

- **The data.** The plane's metric and extrinsic curvature are analytic data on a timelike surface, and they satisfy
  both conditions. A timelike surface is not characteristic; the characteristics are null.
- **Existence.** In Gaussian normal gauge, the Cauchy–Kovalevskaya theorem (standard, not READ) solves the evolution
  equations off the plane.
- **Constraint propagation.** The two constraints, Gauss (the yy part) and Codazzi (the yμ parts), then stay zero off the
  plane by the contracted Bianchi identities. That is the lemma in the Campbell–Magaard theorem with Λ, as Dahia and
  Romero use it (READ in BULKWARP.md). Without it the solution would not be a vacuum bulk.
- **Uniqueness, with its limits.**
  - The solution is unique among analytic solutions, up to diffeomorphism.
  - Uniqueness among merely smooth solutions is not established for this timelike problem. That is Anderson's point
    (below).
- **What the result says:**
  - Maartens–Koyama's formal series eq. (148) is this solution's Taylor series, and it converges near the plane.
  - By uniqueness, the bulk inherits the data's staticity and spherical symmetry.
- **What the board adds to Dahia–Romero** is K = −g/ℓ: the plane is a vacuum with Randall–Sundrum tension, because your
  corridor has R⁽⁴⁾ = 0. Dahia–Romero's theorem leaves the extrinsic curvature, and so the plane's matter, free.

### 5. How far it reaches (L5)

- **At the throat, Maartens–Koyama eq. (148) gives g̃_θθ = 4m² + y² + 2y³/ℓ** (imported from throatbulk.py T6). So the
  corrections are (y/r₀)² and (y/r₀)²·(2y/ℓ).
- **The reach is roughly min(r₀, ℓ).** That accounts for the warp factor e^(−2y/ℓ) and the O(y⁴) terms, which are not
  computed here. It is an estimate, not a bound, and it is conditional on ℓ against r₀:
  - throatbulk.py T4 puts them of one order;
  - under H-ONE-BIT-SCALE, r_min/ℓ = √N, and the reach is about ℓ.
- **"Near the plane" need not mean uniform thickness.** The neighbourhood may thin as r → ∞ along the non-compact plane.
  Maartens–Koyama's p.27 caution about Gaussian normal coordinates at a horizon also limits the chart.

## What this does and does not show

- **It shows that a local vacuum Randall–Sundrum bulk carrying your corridor exists, unique among analytic solutions.**
  - The corridor is an exact plane with no matter on it.
  - Existence is proved, but no metric is handed over: the bulk is not written down.
- **It does not show the global bulk.**
  - Whether the local solution continues, regular, to where the bulk ends is not settled.
  - Building a bulk outward from the plane is not stable to small changes in the data. Anderson (READ in BULKWARP.md):
    the embedding theorem *"offers no guarantee of continuous dependence on the data and … disregards causality"*.
  - The global bulk needs a boundary-value construction, the method Figueras and Wiseman used for static black holes on
    such a plane (READ in OUTSIDE.md).
- **The censorship question (wall D) turns on the global bulk.** It stays open with it.

## Named hypotheses

- **Yours:**
  - H-STATIC-PLANES (141);
  - eq. (17) as your corridor (H-BK-CORRIDOR, the board's identification);
  - M-WORK-THE-MATH (149).
- **The board's:**
  - H-FACE-TO-FACE;
  - H-COMPOSITE-SURFACE (one RS II plane at long range);
  - H-ONE-PLANE-NEAR (the same at short range, which S2b does not show);
  - mirror symmetry (Z2) in fixing K. It is not needed for existence (L1d).

## OPEN

1. The global bulk: a boundary-value construction (Figueras–Wiseman's method).
2. The O(y⁴) terms of eq. (148) at the throat, which would turn L5's estimate into a computed radius.
3. The short-range identification, H-ONE-PLANE-NEAR: the massive modes of the face-to-face pair.

## History (verifier, 2026-10-07)

Ten findings and four under-claims, all applied:

1. **The reach was order r₀ only.** Maartens–Koyama's ℓ-terms make it ~min(r₀, ℓ), conditional on ℓ against r₀. Now L5,
   computed from throatbulk T6.
2. **Uniqueness lacked its qualifier.** It holds among analytic solutions, up to diffeomorphism.
3. **Constraint propagation was missing.** Now named: the Bianchi identities, the Campbell–Magaard lemma, as used by
   Dahia–Romero.
4. **"Near the plane, one now is" over-stated.** Existence is shown and no metric is found. The docstring's "Dahia–Romero
   give the same" was wrong and is withdrawn.
5. **A long-range premise was used at short range.** Now H-ONE-PLANE-NEAR. Z2 is listed.
6. **The Gauss check is blind to the sign of K.** Now stated (L1d), with the mirrored solution.
7. **ρ and the domain were implicit.** Now ρ is defined, the second exterior is stated, the Riemannian strip is computed,
   and evenness is proved from the closed form.
8. **"Local" is not uniform.** Now stated.
9. **L2 is now tagged STRUCTURAL** in the note.
10. **The controls did not test the Gauss formula.** L1c (the dS slicing of AdS₅) now does, with a wrong-sign foil.

Under-claims taken up:

- Z2 is not needed.
- Eq. (148) converges.
- The bulk inherits staticity and spherical symmetry.
- H-ANALYTIC-DATA is established.
