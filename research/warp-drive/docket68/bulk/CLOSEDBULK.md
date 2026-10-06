# Building the bulk as a closed index (M-RULINGS items 120–121; deduced, computed and READ; not verified; not seated; 2026-10-06)

## What M said

- **Item 120:** *"yes. Science has already taught us that matter is neither created nor destroyed, it only changes
  geometric state."* A complete bulk exists on your path (H-COMPLETE-BULK).
- **Item 121:** *"yes. And we build it under closed index criteria, self referencing and self defending"*
  (H-BULK-CLOSED-INDEX).

Every number is printed by `closedbulk.py`.
- **Selftest:** 11/11 checks, 3 genuine controls and 1 contrast, with 6 STRUCTURAL lines printed and not counted. The
  series runs through y³ by default (under a minute); `--order 5` runs through y⁵.
- **Imported, not rebuilt:**
  - `pairing.py`, for the five-dimensional Einstein tensor;
  - `coin.py`, for the plane's ANEC integral in closed form;
  - `escape.py`, for S3's K = −a q.

## The criteria, as The Method states them (READ)

From `method/members/The_Method_1_6-2.md`:

| | The Method | where |
|---|---|---|
| P1 | *"a complete index is self-referencing"*, ℛ(Λ) = Λ | principles table; §15.5 *"ℛ(X) = X recovers alphabet and bounds for any closed index"* |
| P2 | *"a complete index is self-defending"*, ⅅ = dim q − rank ∂Φ/∂p ≥ 1 | principles table; §16.1 *"Each is a test the index must pass"* |
| | the defence is two disjoint paths | §16.4 *"ⅅ_def is realised iff a quantity is reachable by two disjoint paths, and the defence is the DISAGREEMENT between them"* |
| | surplus is needed | *"Without surplus there is no check"* |

The board read "self-defending" earlier as the contracted Bianchi identity (paper/CLAIMS.md H20).

## How the board translates them to a five-dimensional spacetime (named, the board's)

- **H-SELFREF-AS-DETERMINED.** Self-referencing means the bulk is rebuilt from the plane's own data alone, with no input
  from outside it, and reads back to the plane. The data are the plane's metric, and its extrinsic curvature
  K = −a q, which τ = 0 and the tension fix (escape.py S3).
- **H-SELFDEF-AS-CONSTRAINTS.** Self-defending means the bulk's field equations outnumber its unknowns.
  - At each order in the distance y off the plane, three evolution equations fix the three new coefficients.
  - The two constraint equations are then a second, disjoint path that must agree.
  - So ⅅ = 5 − 3 = 2 per order. The contracted Bianchi identity is why the two paths can agree.
- **H-CLOSED-AS-COMPACT.** Closed means the extra dimension closes on itself with no boundary: Randall–Sundrum's S¹/Z₂
  (H-RS1), with a second plane at y = y_c and no outside to supply data. Only B3 uses this reading.

## What passes

**The construction.** Coordinates run straight out from the plane: ds² = −A dt² + B dr² + C dΩ² + dy².
- The bulk holds vacuum energy only (H-VACUUM-BULK, with the Randall–Sundrum tuning, so the plane's own Λ is zero).
- A, B and C are each a power series in y.
  - The y⁰ term is Bronnikov–Kim's eq. 17 (gr-qc/0212112v1 p.4).
  - The y¹ term is −2a times it (K = ½∂_y g = −a q).

- **B1. The bulk is self-referencing.**
  - Every coefficient through y³ (through y⁵ with `--order 5`) is fixed uniquely by the plane's m and r₀ and by a. No
    free function and no outside datum enters (sympy).
  - **The bulk reads the plane's own violation back.** Every term beyond the warp e^{−2ay} carries the factor
    (2r₀ − 3m). That is the factor of the plane's G_kk (coin.py C1); for an ordinary black hole every such term vanishes.
  - **The bulk's null extrinsic curvature starts as the plane's reading: K_kk = G_kk·(y + 5a y²) + O(y³).** Its first
    y-derivative is exactly coin.py's G_kk.
  - Restricted to y = 0, the bulk returns the plane (STRUCTURAL: by construction).
- **B2. The bulk is self-defending.**
  - Both constraint equations vanish at every order computed: y⁰ and y¹ by default, through y³ with `--order 5`. The
    evolution path and the constraint path agree.
  - The defence catches a wrong index (controls):

    | wrong input | what the constraint returns |
    |---|---|
    | a plane with R ≠ 0 (Schwarzschild–de Sitter) | yy at y⁰: −2Λ |
    | a wrong tension (K = −2a q) | yy at y⁰: 18a² |
    | a mis-stated y² coefficient (A₂ + δA₀) | yy at y¹: −3aδ; ry at y¹: −δm/(r(r − 2m)) |

    The last row is The Method's *"The check caught the check"* (§16.4).
  - Contrast: a Schwarzschild plane builds the pure warp, with every correction zero and both constraints zero. This is
    the black string, computed here, not READ.

## What the closed reading forces: the price moves to the other plane

- **B3. Under H-CLOSED-AS-COMPACT, with flat planes, the second plane's tension is exactly minus the first's.** K = −a h
  at every y (computed).
- **With the corridor on our plane, the second plane's matter breaks the averaged NEC.**
  - The junction with the Z₂ mirror gives the second plane's null matter: **τ₂_kk = (2/κ²) K_kk(y_c) = (2/κ²)·G_kk·
    (y_c + 5a y_c²) + O(y_c³)**.
  - Along a whole null geodesic its ANEC integral is **(2/κ²)·y_c·(−1.914712 E/m)** at leading order (m = 1, r₀ = 1.8):
    negative.
  - The second-order term has the same sign, so it does not reverse the reading locally.
  - **Bending the second plane cannot remove it.** A bend y_c → y_c + ε(x) adds −d²ε/dλ² along each null geodesic,
    to first order. That is a total derivative, so the integral is unchanged (STRUCTURAL, a standard identity).
- **Matter in the bulk that keeps the NEC makes it worse, not better (derived; for the verifier).**
  - The null-contracted Gauss equation at the plane gives ∂_y K_kk = R⁽⁴⁾_kk − R⁽⁵⁾_kk. The quadratic terms vanish
    there because K = −a q and q_kk = 0.
  - In vacuum R⁽⁵⁾_kk = 0. This is the computed K_kk = y G_kk.
  - Bulk matter keeping the NEC has R⁽⁵⁾_kk ≥ 0, so it pushes the second plane's reading further negative.
  - **So, given our plane's geometry, a closed bulk that keeps the NEC everywhere puts matter breaking the averaged NEC
    on the other plane**, at leading order in y_c.
- **The same move appears elsewhere on the board.** pairing.py's reading of Chung–Freese (H-ORIENTATION) found that
  junction conditions *"may move the price onto the hidden brane"*.

**Against your coin, as the board read it, in this reading (item 82: this is the boundary).**
- Your item 117 puts the two positions on separate sides. If the two planes of a closed bulk are the two sides, then
  side 1 shows the violation as geometry (an appearance), and side 2 carries it as matter (a real violation).
- **Escapes, each named:**
  1. **"Closed" does not mean compact.** With one plane and an open bulk (Randall–Sundrum's second model) there is no
     second plane to pay. Then BK p.6's *"full 5-dimensional space-time"* problem returns, with an outside.
  2. **The bulk breaks the NEC between the planes** (R⁽⁵⁾_kk < 0 somewhere). Then the condition is broken in the bulk,
     which is against H-NEC-COIN in another place.
  3. **Our plane carries matter** (τ₁ ≠ 0). That changes the corridor, which BK's vacuum plane does not supply.
  4. **Beyond leading order.** For y_c not small against r₀, the global bulk decides, and it is OPEN.
  5. **The second plane is position 2's.** Your words *"each position sits on a separate side"* would then name the
     planes. Whether position 2's plane may carry that matter is your call. Not asked before this.

## Scope

- **The series is local.** A's first term beyond the warp is m(2r₀ − 3m)y²/(r²(2r − 3m)²), of order (y/r₀)² near the
  throat.
  - It reaches y ≈ 1.67, 2.58 and 11.6 (units of m) at r = 1.85, 2 and 3 (m = 1, r₀ = 1.8).
  - So it is trusted only for y ≪ r₀ (H-NEAR-PLANE).
- **For the README's corridor**, r₀ is of order 10⁻²⁷ m, far inside any Randall–Sundrum y_c.
  - B1 and B2 hold order by order wherever the series converges.
  - B3's sign is shown only for y_c ≪ r₀.
- **The global bulk is still the construction.** What this instrument builds is the bulk's germ at the plane, with
  every order the plane's own and every order defended.

## Named hypotheses

- **Yours:** H-COMPLETE-BULK and H-CONSERVATION-AS-GEOMETRY (120); H-BULK-CLOSED-INDEX (121); H-NEC-COIN (117; a
  metaphor, 120).
- **The board's:**
  - H-SELFREF-AS-DETERMINED, H-SELFDEF-AS-CONSTRAINTS, H-CLOSED-AS-COMPACT: the translations above;
  - H-BK-CORRIDOR; H-RS1;
  - H-VACUUM-BULK: G_AB = 6a² g_AB;
  - H-Z2: the orbifold mirror at each plane;
  - H-NEAR-PLANE: the series' scope;
  - H-PLANE-READING.

## Sources READ

| source | route | used |
|---|---|---|
| The Method 1.6, `method/members/The_Method_1_6-2.md` | the store of record (md5-verified) | principles table P1, P2, P18; §15.5; §16.1; §16.4; the P2 hypothesis |
| paper/CLAIMS.md H20 | the board's own | "self-defending … is the contracted Bianchi identity" |
| Bronnikov & Kim, gr-qc/0212112v1 | plane.py, escape.py (READ there) | eq. 17 p.4; p.6 |
| Chung & Freese, hep-ph/9910235v2 | pairing.py (READ there) | the junction moves the price to the hidden brane |

## OPEN

1. The global bulk (BULK5-O1): whether the series continues to a second plane, or to a regular open bulk.
2. Which reading of "closed" is yours: compact with a second plane, or another.
3. B3 beyond leading order in y_c.
4. Whether the second plane is position 2's, and whether its matter may break the averaged NEC (escape 5).
5. Carried from COIN.md: a five-dimensional censorship theorem; H-UMBILIC-GEODESIC; your two sides.
