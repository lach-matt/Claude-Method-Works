# The two-plane balance in a bulk that carries the corridor (item 181; models A, B, C; computed and deduced; each model re-derived by a separate checker, then verified once, findings applied; not seated; 2026-10-09)

*First headed* "The two-plane balance … (findings applied; not seated)". The scripts and outputs of the workflow
`k-equality-bulk-balance` are archived in `lemmas/kequality_scratch/`. They are scratch instruments, reproduced by
the checkers and the refute verifier, and not yet an owned instrument with its own selftest. The checkers were
separate AI sessions inside this project, not an outside review.

## What you said

- **181** (verbatim): *"this bears directly on B4d, and requires priority"*. The mechanism tested, that each plane
  balances where its tension meets the corridor's geometry so that the two conditions pin ℓ, is **the board's
  account**, which you prioritised. So is the control: with no corridor, a flat plane balances anywhere.
- **179/180, 182, 184:** the corridor in the bulk; your guess C; no matter-free planes.
- **162** (verbatim): *"I submit that it may be more like a black hole, containing both mouths and throat at once"*.
  "One black-hole-like object" is the board's H-ONE-OBJECT.

## Plain words first

1. **The board's account behind 181 is refuted for bare planes in these models.** In a corridor of this kind, a flat
   plane cannot stay still anywhere. The corridor does not pin the planes; it removes every place they could rest.
   With no corridor, a flat plane stays still anywhere, as the control predicted.
2. **With matter on the planes (your 184), a flat plane can stay still beside the corridor.** Its matter must then
   break the null energy condition at each point (ρ + p < 0). Whether your 183, "never violated as a pair", covers
   that, by pairing it with the bulk's projected Weyl term, is OPEN and goes to the matter round (185).
3. **k's scale still has no value.** Any equality of this kind would tie ℓ to the corridor's size, which the README
   sets, so ℓ would grow as √N and change with every trip. With no corridor, which is our current state (129), it is
   undefined.

## Results

**Which model fits (deduced).** Model C, the two-sided bridge, fits your 179/180 best, together with the board's
H-ONE-OBJECT reading of your hedged 162 and your 166 as re-read under 179. It is also your guess (182). It is not
ruled.
- Model A's two-exterior orientation is the same geometry as C: the two checkers found the identical solution
  separately.
- Model A's connected orientations have no horizon between the planes, so they are not 162's object, on the board's
  reading that 162 needs a horizon between them.
- Model B is excluded as yours under the board's reading of 179, where "sits on a plane" means the plane's induced
  geometry. Its throat is our plane's own eq. (17).

**1. Flat planes: no static position (computed; checked).**
- **Where this holds:** flat planes at r = const (H-SYMMETRIC-PLANES), in a static Schwarzschild-AdS5 corridor whose
  outer bulks carry no mass or charge (H-CORRIDOR-ONLY-BETWEEN), with 141 read as R = const (H-STATIC-SCALE).
- Under those readings no static position exists, under any tension convention. Each bridge side's balance
  B = −2μℓ/(R√(R⁴ − ℓ²μ)) is never zero for μ > 0, and identically zero for μ = 0.
- The charged flat case was checked over the reals on the listed rows only.
- **Two limits on what this shows:**
  - **A flat black brane has no size.** Rescaling (r, t, x, μ) → (λr, t/λ, x/λ, λ⁴μ) is a symmetry, so a flat-plane
    model cannot return an equality between ℓ and a corridor size at all. It tests where planes can rest, not k's
    scale.
  - **A negative-mass outer bulk can hold a flat plane**, which these readings exclude.

**2. Model B, the throat column: no equality (computed; checked).**
- **Our plane gives no condition.** Its Randall–Sundrum balance holds at every ℓ, because R₄ = 0 on eq. (17).
- **No matter-free mirrored or pure-trace position-2 plane exists** at any depth: the umbilic defect D = q − p > 0
  throughout.
- **With a free far side**, the balance is met only at coincidence (C-SHEET-M4, C-S6), or along a curve y₂(ℓ) (C-S7):
  moduli, not equalities.
- **With README matter on position 2**, every depth balances, and positive energy gives only lower bounds, in
  corridor mass lengths m: ℓ > 8.54m (−1/4), 7.30m (−1/3), 9.78m (−1/6), 10.40m (−1/8), 27.07m (ours, reproducing
  SIM2). That is 5.38×10⁻²⁷ metres at the example README for the last, and these bounds grow with the README. They
  belong to the board's configuration.
- **An AdS₂ × S² vacuum column holds at most one matter-free umbilic slice.**

**3. Closed planes: equalities in form, physically excluded (computed by two checkers; reproduced to 60 digits).**
- **What they need.** Isolated solutions that pin the bridge's size against ℓ exist only when three things hold
  together:
  - the slab's ℓ is free, or ℓ is read as ℓ₁;
  - our plane is at 6/(κ²ℓ₁), which is above the flat-balance tension of its own two sides (by 36%, 40% and 15% in
    the three cases);
  - the slicing is closed.
- **Where they exist.** This depends on both the slab-ℓ reading and the statement of the quarter:

  | quarter, ℓ₂ | form-equality? |
  |---|---|
  | −1/8, 4ℓ₁/3 | yes |
  | −1/8, ℓ₁ | yes |
  | −1/4, ℓ₁ | yes |
  | −1/4, 4ℓ/3 | no |
  | −1/3, 3ℓ | no |
  | −1/6, 6ℓ | no |

- **Why they are excluded:**
  - our plane would be a closed three-dimensional sphere of radius about 1.1ℓ, against observed flatness and every
    bound on ℓ (standard-not-READ);
  - our tension would be above its flat-balance value, failing the control;
  - they are matter-free, against 184.
- **Model A's checker also lists k = −1 free-slab solutions,** with position 2 within 10⁻⁴ ℓ of two horizons
  (numerical, not re-checked). These are hyperbolic, against observed flatness, and OPEN as to numerics.

**4. The matter sign (computed; checked).**
- On a static flat plane whose corridor side is r < R (both of Model C's planes, and mirrored planes), beside a
  corridor of positive mass: κ²(ρ_m + p_m) = −4μℓ/(R⁴√(1 − μℓ²/R⁴)) < 0. Its matter must break the NEC at each point.
- For a plane with the corridor on its r > R side, the sign is positive. In general, at least one plane breaks it.

**5. Motion (computed).**
- A mirrored flat plane at exactly the RS tension is never at rest: Ṙ² = μ/R², R̈ = −μ/R³.
- A plane momentarily at rest needs a tension below RS, and then R̈ = −2μ/R³.
- The bulk corridor reaches a flat plane through the projected Weyl term, as radiation-like energy μ/R⁴. READ, Kraus
  hep-th/9910149 p.6: "For large R the wall metric is that of a spatially flat radiation dominated cosmology".

**6. Settled along the way: the per-sheet count (computed in A, B and C; checked).**
- Under the board's 174 (2) rule (keep M4's geometry, k_R = 3k_L/4), position 2's single sheet is −1/8 of ours, and
  PRZ's −1/4 is the count over both copies of the space.
- Your 139 quarter is kept as that doubled count. Read literally per sheet, the flat control forces k_R = k_L/2
  instead.
- Stage 6's −1/3 at ℓ₂ = 3ℓ, the board's reading of your 138, has no two-plane balance with a corridor in any model.

**7. Model C as a B4d corridor (standard-not-READ; deduced; refute verifier).**
- Model C is the eternal two-sided black hole. The corridor between the two exteriors passes through the bifurcation
  surface, whose causal past contains the white-hole region and its past singularity. There is a future singularity
  too, and the bridge between the horizons is not static.
- So under 174 (1)'s strict regularity rule, Model C as it stands is not an admissible B4d corridor. What fits your
  words is its topology, a bridge with a plane on each side, not this eternal solution.
- A non-extremal two-sided bridge is not traversable without negative null energy (standard-not-READ). So E-PASS's
  crossing runs through E-Q, your 177 and 183. Maldacena–Qi is READ; Gao–Jafferis–Wall is READ as of item 178's
  answer.
- Lemma S applies to the bridge's horizon (standard-not-READ).
- No pure-tension Model C solution realises 127 / 172 (2)'s endless approach. Its horizons are non-degenerate, and the
  neutral extremal member is hyperbolic and fails. That remains OPEN.

**8. The structural point (deduced; extended to C by the synthesis).** Any balance equality reads ℓ = c × (corridor
size), and the size is set by the README (131, 162). So ℓ ∝ √N per trip, and in the corridor-free current state
(129) no length is fixed. A matter-round equality would carry the same caveat. It would be admissible only under
127's H-COEFF-FROM-CURRENT read as allowing a value per trip, which the board does not read it as (ITEM179 note).

## What it does to B4d (no status moves; nothing seated)

- **The gate for a static configuration.** Static planes beside a bulk corridor need matter on the planes (184
  supplies it), and that matter breaks the NEC at each point. Whether 183 admits it, paired with the projected Weyl
  term (H-PLANE-MATTER-PAIRS-WITH-WEYL, the board's), is OPEN and goes to 185's matter round.
- **E-PASS** is re-read on the bridge's horizon, through E-Q.
- **The look-ahead** is re-run after 185.
- **OPEN:**
  - planes that break the bridge's symmetry, for example a flat plane cutting a spherical hole: no model covers it;
  - outer bulks with their own mass, and charged bridges;
  - an extremal, endless-throat bridge.

## History

- **2026-10-09, workflow `k-equality-bulk-balance`.**
  - **Run:** three models, each with a separate checker, then a synthesis, then refute and overclaim verifiers.
  - **Refute verifier:** one blocker. The flat-plane no-go was presented as refuting any corridor, when it holds
    under four readings and a flat brane has no size. Also several majors:
    - the closed-plane equalities need a super-critical tension;
    - the convention dependence was misstated;
    - Model C's past singularity was omitted.
  - **Overclaim verifier:** majors on attribution (the board's account presented as yours; 162 misquoted; stage 6's
    ℓ₂ = 3ℓ quoted as 138's), on scope, and on independence.
  - **Applied:** all of the above, and the minors, including the R̈ factor, units (m versus metres), the ρ + p sign
    restricted to planes with the corridor on their inner side, Model B's "no solution" refined to "no equality",
    the per-sheet count's grounds named as the board's 174 (2) rule, and the excluded metre value of k removed.
