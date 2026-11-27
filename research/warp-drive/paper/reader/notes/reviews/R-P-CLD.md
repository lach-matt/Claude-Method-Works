# R-P-CLD — reading of proofs/P-CLD.md

File read: research/warp-drive/paper/reader/proofs/P-CLD.md, md5 67d1d46d29bf60540d4414971c6e34f4, 797 lines, every
line, every proof. Branch ccr-66909215-gi0qa5, HEAD ea33ac6a (chapters 81, 82, 83 identical to the 9d133b0c the file
cites; every line number below is at HEAD). Also read: notes/reports/P-CLD.md, notes/reviews/R-P-CIVP4.md (Major 5,
minor 2 and the closing verdict), chapters 81 (whole of sec:class-axes to the end), 82 (the leaf and shear sites),
83 (every site that cites the lemmas or the shear), the standard results cited (95-standard-results.md), and
proofs/P-CIVP5.md for compatibility.

Summary. The mathematics of the block is sound: lem:class-leaf-states (a)–(c) is proved as stated with only C² of g, and
the seven-step proof of (a) and (c) of lem:class-leaf-differences is loss-free and correct in substance (the σ²-form via
the Cartesian 𝔗, the radial Volterra form for transverse derivatives, the flat Laplacian of the radial potential along
the disc). Nothing in the chapters after the merge needs an H^k bound of σ itself. But the new explicit restriction
δ ≤ δ_0 (≤ ρ1(p)/128) breaks one site that the use list classifies as unaffected (Major 1), and there are six minor
gaps: two in the ordering and bookkeeping of Steps 5 and 6 and in eq:class-leaf-compose, one in the comparison of norms
of Step 2, and three in the text around lem:class-leaf-reference and in Tier 3's paragraph that the placement leaves
stale or unproved. Every replacement below was applied in a scratch merge (all 11 replacements of the file first, then
these texts) and passes lint.py --chapters (0 hits), assemble.py --check (0 problems) and the assembled check (prints
`[] 0`), all lines ≤ 121 characters after resolution, no bad wrapped-line starts.

-----------------------------------------------------------------------------------------------------------------------

## Major

### Major 1 — lem:loc-lens-dependence fixes δ := 1/2, which the new statement does not allow (83:447–450, 83:508–509)

Step (4) of the proof of lem:loc-lens-dependence reads "Fix δ := 1/2 and the points p_i of axis 2 in a slice with
ρ1(p_i) = 3.4, 3.8, …, 5.8; then δ ≤ ρ1(p_i)/4, and [[lem:class-leaf-differences]] … holds near each p_i", and step (6)
then applies (b) of that lemma on the sets 𝒰_δ(p_i), which are to cover {ρ2 ≤ 1/4} ∩ 𝒟_s, to prove eq:loc-lens-shear.
The old statement had no quantifier on δ beyond the definition of 𝒰_δ (δ ≤ ρ1(p)/4), and chapter 83 read it so. The
new statement gives (a)–(c) only for 0 < δ ≤ δ_0, with δ_0 ≤ r_1/4, r_1 ≤ r_*/8 and r_* ≤ ρ1(p)/4, so δ_0 ≤ ρ1(p)/128
≤ 5.8/128 < 0.05. After the merge the proof of eq:loc-lens-shear cites (b) at δ = 1/2, outside its range, and the
covering of {ρ2 ≤ 1/4} by the 𝒰_δ(p_i) is not available at any admissible δ. No other tool of the block covers it:
lem:class-leaf-states (c) also needs δ ≤ r_1/2. The file's use list puts 83:509–511 among the L² uses "not affected";
it is affected through δ, and no placement item touches it. (83:2890–2891, "By compactness, as in step (4) of the proof
of [[lem:loc-lens-dependence]], there are δ ∈ (0, ρ_-/4] and balls …", is consistent with the repair below.)

Repair (a new placement item for chapter 83; two old texts). The background is the one the old text already uses on
𝒰_1(p_i), so the radius r_* := 1/2 stays where it is defined; δ_0, the balls and the constants of the lemma depend only
on ρ1(p), r_* and bounds of the background state there, uniform over the compact set of axis points and times; the cut-off
χ_Z moves inside {ρ2 < δ}, where it is still 1 near the axis, and S_loc is smooth where χ_Z ≠ 1 with c depending on δ.
The leaf argument of step (6) ("Let y ∈ 𝒟_s with ρ2(y) ≤ 1/4") is unchanged and covers ρ2 < δ ≤ 1/8.

First old (83:447–450), first new:

Old:

```
where σ is the planar shear of the level sets of u_in in the slices {t = s}. Fix δ := 1/2 and the points p_i of axis 2
in a slice with ρ1(p_i) = 3.4, 3.8, …, 5.8; then δ ≤ ρ1(p_i)/4, and [[lem:class-leaf-differences]], for the background
and the ingoing family, holds near each p_i, with balls 𝔅, 𝔅′ and a constant C common to these points and to
0 ≤ s ≤ t1. Let χ_Z be a G-invariant function of ρ2 equal to 1 for ρ2 ≤ 1/8 and to 0 for ρ2 ≥ 1/4. Then on 𝒟,
```

New:

```
where σ is the planar shear of the level sets of u_in in the slices {t = s}. At the points p of axis 2 in these slices
with 3.39 ≤ ρ1(p) ≤ 5.86, 0 ≤ s ≤ t1, take the radius r_* := 1/2 ≤ ρ1(p)/4 in [[lem:class-leaf-differences]], for the
background and the ingoing family; its number δ_0, its balls and its constants depend only on ρ1(p), r_* and bounds of
the background on the sets 𝒰_(r_*)(p), which are uniform over these points and times. Fix δ ∈ (0, 1/8], at most δ_0 at
all of them, and finitely many such points p_i whose intervals (ρ1(p_i) − δ, ρ1(p_i) + δ) cover [3.39, 5.86]; then
[[lem:class-leaf-differences]] holds near each p_i, with balls 𝔅, 𝔅′ and a constant C common to these points and to
0 ≤ s ≤ t1. Let χ_Z be a G-invariant function of ρ2 equal to 1 for ρ2 ≤ δ/2 and to 0 for ρ2 ≥ δ. Then on 𝒟,
```

Second old (83:508–509), second new:

Old:

```
([[eq:class-shear-leaf]]); so σ[Ŭ](y) = σ(y), and likewise σ[ů] = σ̊. The sets 𝒰_δ(p_i) cover {ρ2 ≤ 1/4} ∩ 𝒟_s, where
3.39 ≤ ρ1 ≤ 5.86, and [[lem:class-leaf-differences]] (b) gives
```

New:

```
([[eq:class-shear-leaf]]); so σ[Ŭ](y) = σ(y), and likewise σ[ů] = σ̊. The sets 𝒰_δ(p_i) cover {ρ2 < δ} ∩ 𝒟_s, where
3.39 ≤ ρ1 ≤ 5.86 and outside which χ_Z = 0, and [[lem:class-leaf-differences]] (b) gives
```

The crosswalk row of lem:loc-lens-dependence in crosswalk/83-localised-data.tsv should record the change (δ from
lem:class-leaf-differences, χ_Z at the scale δ).

-----------------------------------------------------------------------------------------------------------------------

## minor

### minor 1 — Steps 5 and 6 are one induction, and R_j holds top-order terms that must be absorbed (P-CLD 351–354)

Two points in Step 5 of the proof of (a) and (c).

(i) Ordering. Step 5 is completed for all j ≤ k (or m) before Step 6 begins, and its bound of R_j is "By (P), and by
induction on j". For j ≥ 4, (P) bounds the factor with fewer derivatives through H¹(Q̂) ⊂ L⁴ (j = 4) or H²(Q̂) ⊂ L^∞
(j ≥ 5), that is by mixed norms T^a ∂_y^β with |β| ≤ 2 — for instance ‖T² δs‖_(H¹(Q̂)) in (T² a_2)(T² δs) at j = 4.
Step 5's induction controls only the pure T^j; the mixed norms come from eq:class-leaf-elliptic, which is Step 6 and
itself uses eq:class-leaf-transverse. The induction closes when the two steps are run together: at the order j, Step 5
needs mixed norms of order below j, given by eq:class-leaf-elliptic at j − 1, and Step 6 at the order n uses Step 5 at
orders at most n. Since eq:class-leaf-elliptic at j − 1 holds on Q̂_(j−1), so does the bound of Step 5 at the order j;
the radial operators act disc by disc, so nothing else changes.

(ii) Top-order terms of R_j. R_j collects the Leibniz terms in which δs, η or ω ∘ Λ_U carry fewer than j derivatives,
so it contains the terms in which all j derivatives fall on a_1, a_2, a_3 — and these coefficients contain s_U, h_U,
W_U ∘ Λ_U, W_ů ∘ Λ_U, so T^j of them holds T^j δs, T^j η and T^j(ω ∘ Λ_U) at top order. The sentence "the factors of R_j
other than δs, η and ω ∘ Λ_U being bounded in the norms of order j by Step 4 and (Q)" is therefore not right as it
stands: they are bounded by C (1 + ‖T^j δs‖ + ‖T^j η‖ + ‖T^j(ω ∘ Λ_U)‖), and the term is closed only because the other
factor (δs, η or ω ∘ Λ_U undifferentiated) is at most C 𝒩_k(U) ≤ 2C r″, so that it is absorbed for r″ small. The text
absorbs the analogous term in Step 6 (iii) explicitly, but not here; r″ must then also be fixed in Step 5.

Old (P-CLD 351–354):

```
with 3C_2 (1 + C_0) δ_1 + 9C δ_1² ≤ 1/2. By (P), and by induction on j, ‖R_j‖ ≤ C (Ω_j + 𝒩_k(U)) for j ≤ k, the factors
of R_j other than δs, η and ω ∘ Λ_U being bounded in the norms of order j by Step 4 and (Q), and ‖R_j‖ ≤ C_m (Ω_j +
𝒩_k(U)) for k < j ≤ m. By (Q), ‖T^j(ω ∘ Λ_U)‖ ≤ C (Ω_j + 𝒩_k(U) ‖T^j η‖) plus terms bounded by (P) and the derivatives
of η of order below j. With ∂_y η = δs y and Ω_j ≤ C 𝒩_j(U), induction on j gives, on Q̂,
```

New:

```
with 3C_2 (1 + C_0) δ_1 + 9C δ_1² ≤ 1/2. Steps 5 and 6 are one induction on the order: at the order j this step uses
[[eq:class-leaf-elliptic]] at j − 1, and Step 6 at the order n uses this step at orders at most n. The operator bounds
above hold on every disc 𝔻_ρ, ρ ≤ 3δ, so the bounds of this step hold on the set Q̂_(j−1) of Step 6, Q̂_(−1) := Q̂.
In R_j the coefficients a_1, a_2, a_3 carry the derivatives that δs, η and ω ∘ Λ_U do not. A term in which all j fall
on a coefficient has δs, η or ω ∘ Λ_U as a factor without derivatives, at most C 𝒩_k(U) ≤ 2C r″, times at most C (1 +
‖T^j δs‖ + ‖T^j η‖ + ‖T^j(ω ∘ Λ_U)‖), by (Q) for the coefficients; the other terms are covered by (P), whose norms of
order below j are bounded by [[eq:class-leaf-elliptic]] at j − 1 and by Step 4. So ‖R_j‖ ≤ C (Ω_j + 𝒩_k(U)) + C r″
(‖T^j δs‖ + ‖T^j η‖ + ‖T^j(ω ∘ Λ_U)‖) for j ≤ k, and the same with C_m in place of C for k < j ≤ m. By (Q),
‖T^j(ω ∘ Λ_U)‖ ≤ C (Ω_j + 𝒩_k(U) ‖T^j η‖) plus terms bounded by (P) and the derivatives of η of order below j. With
∂_y η = δs y and Ω_j ≤ C 𝒩_j(U), the terms in r″ being absorbed for r″ small, induction on j gives, on Q̂_(j−1),
```

and, in *The balls* (P-CLD 240):

Old:

```
and ů, and 𝔅 := {𝒩_k ≤ r″}, with r″ ∈ (0, r′/2] fixed in Steps 4 and 6 below; let 0 < δ ≤ δ_0.
```

New:

```
and ů, and 𝔅 := {𝒩_k ≤ r″}, with r″ ∈ (0, r′/2] fixed in Steps 4, 5 and 6 below; let 0 < δ ≤ δ_0.
```

### minor 2 — eq:class-leaf-compose overstates the bound for ω_g at the order n + 1 (P-CLD 330–333)

In (Q) with F := ω_g and |α| = n + 1, the term with |β| = 1 is (∂_z ω_g) ∘ Λ_U · D^α h_U. If D^α has a derivative in y,
D^α h_U is a derivative of order n of ∂_y h_U = ∂_y h_ů + ∂_y η, covered by ‖∂_y η‖_n. If D^α = T^(n+1) (only
transverse derivatives), it is T^(n+1) h_ů + T^(n+1) η, and ‖T^(n+1) η‖ is in neither ‖η‖_n nor ‖∂_y η‖_n. So the
display is not proved for ‖ω_g ∘ Λ_U‖_(n+1). The only use at the order n + 1 is Step 6 (iii), with T^j ∂_y^β, j ≤ n,
which is covered; the ω-part at the order n is fine. Restrict the norm:

Old (P-CLD 330–333):

```
with Jacobian at least 1/2, gives ‖(D^β F) ∘ Λ_U‖ ≤ √2 ‖D^β F‖ on Q_(4δ). With F := ω, and F := ω_g at the order n + 1,
the term in which all of D^α falls on h_U being multiplied by sup |Dω| ≤ C 𝒩_k(U),

    ‖ω ∘ Λ_U‖_n + ‖ω_g ∘ Λ_U‖_(n+1) ≤ C (Ω_n + 𝒩_k(U) (‖η‖_n + ‖∂_y η‖_n)).                      {#eq:class-leaf-compose}
```

New:

```
with Jacobian at least 1/2, gives ‖(D^β F) ∘ Λ_U‖ ≤ √2 ‖D^β F‖ on Q_(4δ). With F := ω, and F := ω_g at the order n + 1,
the term in which all of D^α falls on h_U being multiplied by sup |Dω| ≤ C 𝒩_k(U), and with ‖·‖′_(n+1) the sum of the
norms of the derivatives of order at most n + 1 other than the T^(n+1), for which that term would hold T^(n+1) η,

    ‖ω ∘ Λ_U‖_n + ‖ω_g ∘ Λ_U‖′_(n+1) ≤ C (Ω_n + 𝒩_k(U) (‖η‖_n + ‖∂_y η‖_n)).                     {#eq:class-leaf-compose}
```

Step 6 (iii) reads correctly with it ("those of ω_g ∘ Λ_U by [[eq:class-leaf-compose]]" concerns T^j ∂_y^β, j ≤ n).

### minor 3 — Step 2 compares norms for invariant functions but applies the comparison to tensor components (P-CLD 266–273)

"For a G-invariant function f on 𝒰_ρ … the H^m norms of f on Σ ∩ 𝒰_ρ and of f(z, y) on Q_ρ agree" is then used for
Ω_n ≤ C 𝒩_n(U), where ω = W_U − W_ů and ω_g are components, in the chart x, of invariant tensor fields — not invariant
functions (g_11 is not constant along the orbits of K1). A restriction to the 3-dimensional M3 does not in general
control or follow from 4-dimensional norms; here it does because of the invariance, through the frame adapted to the
(x1, x2)-plane. Add it:

Old (P-CLD 270):

```
ρ1(p)/2. Below, D denotes the derivatives in (z0, y), or in (z, y), and, for a family, also in τ; T denotes ∂_(z0) and,
```

New:

```
ρ1(p)/2. The same holds for each component in the chart x of a G-invariant tensor field: its components in the frame
(∂_z, ρ1⁻¹K1, ∂_(x3), ∂_(x4)) are functions of (ρ1, x3, x4), equal to its components in the chart x at the points of M3,
and they are obtained from those by a change of frame with bounded derivatives of every order where ρ1 ≥ ρ1(p)/2.
Below, D denotes the derivatives in (z0, y), or in (z, y), and, for a family, also in τ; T denotes ∂_(z0) and,
```

### minor 4 — lem:class-leaf-reference keeps a second definition of *state*, and its V is not assumed smooth up to the closure (81:1371–1376; widens Placement 2)

(i) After the merge the section defines *state* twice in italics: in the paragraph before lem:class-leaf-states (W_U =
(g, ∂g, p_A, Θ_A) of class C¹ on Σ ∩ 𝒰) and again at 81:1371–1372 ("A *state* is … with g of class C², p_A and Θ_A
of class C¹"), with its own reading of σ[U] (81:1374–1375). The two are compatible, but item 4 now applies
lem:class-leaf-differences, whose states are those of the new paragraph; one definition should stand.

(ii) Item 4 applies lem:class-leaf-differences with ů := V; its hypothesis is "a smooth state on a neighbourhood of the
closure of 𝒰". lem:class-leaf-reference assumes only "Let V be a smooth state with |p_V(∂_z)| ≥ c > 0 on the axis near
p", a state on 𝒰_(r_*). The use in chapter 83 (83:3654–3656, 𝒰_(r_*) in the interior of 𝒮′ for r_* small) satisfies the
stronger hypothesis, so stating it costs nothing. Replace Placement 2 (81:1373–1374) by this item (81:1371–1376, the
old text being HEAD's):

Old (81:1371–1376 at HEAD; the third to fifth lines are those of Placement 2's new text after it is applied, so the item below replaces Placement 2):

```
ρ1(p)/4]; norms and bounds below are taken on 𝒰_(r_*). A *state* is a G-invariant U = (g, p_A, Θ_A, q_A) on 𝒰_(r_*), with
g of class C², p_A and Θ_A of class C¹, g Lorentzian, Σ_τ spacelike for g and p_A(∂_z) ≠ 0 on the axis. Its function
H_L[U] is that defined before [[lem:class-leaf-states]], its *leaves* are the solutions h(·; z0) of
[[eq:class-leaf-volterra]] with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its planar shear σ[U] at a point is
[[eq:class-shear-leaf]] for the leaf
through that point, with |p_A^Σ| in place of |∇_M3 u| and p_A(n) in place of n(u), and for a state V, 𝒩_k^V(U) is
[[eq:class-energy]] with V in place of ů. Let V be a smooth state with |p_V(∂_z)| ≥ c > 0 on the axis near p.
```

New:

```
ρ1(p)/4]; norms and bounds below are taken on 𝒰_(r_*). States, their functions H_L[U], their *leaves* h(·; z0) and their
planar shear σ[U] are those defined before [[lem:class-leaf-states]] for this radius; for a state V, 𝒩_k^V(U) is
[[eq:class-energy]] with V in place of ů. Let V be a smooth state on a neighbourhood of the closure of 𝒰_(r_*) such
that |p_V(∂_z)| ≥ c > 0 on the axis near p.
```

At HEAD the same old text reads, in its third and fourth lines, "H_L[U] is that of [[lem:class-leaf-differences]], its
*leaves* are the solutions h(·; z0) of [[eq:class-leaf-volterra]]" / "with H_L(ρ) := H_L[U](h(ρ), ρ) and h(0) = z0, its
planar shear σ[U] at a point is [[eq:class-shear-leaf]] for the leaf" (two lines, not three); the new text is the same.
This also removes the short line "[[eq:class-shear-leaf]] for the leaf" that Placement 2 leaves.

### minor 5 — (o) and (b′) still omit the lower bounds their proofs use; Placement 4 should carry them (81:1378–1379, 81:1393–1395)

The file's note on Tier 4 says: "(o) Step 1 and (b′) bound n, K_Σ and κ_A1 by C² norms of g, which needs also lower
bounds for −g⁻¹(dτ, dτ) and for g on TΣ_τ; the bounds (M, c) of this file include them, and Placement 3 names them for
(a), (b)." The task asks whether (o) and (b′) still hold with the bounds of the new definitions. Their proofs do, but
their statements, which stay, claim constants "depending only on r_*, c, lower bounds for A3, B3 and det₂ … and bounds
for the C² norms of g_V and the C¹ norms of p_V and Θ_V" ((o)) and an 𝔐 that bounds C³ of g, C¹ of p_A, Θ_A and the
inverses of lower bounds for A3, B3, det₂ and |p_A^Σ| ((b′)). n = g⁻¹dτ/(−g⁻¹(dτ, dτ))^(1/2) needs the lower bound for
−g⁻¹(dτ, dτ); κ_A1 = g⁻¹(p_A, dψ1) needs g⁻¹ bounded and g(K1, K1) ≥ ρ1²/M, that is the lower bound for g on TΣ_τ in the
K1 direction, which A3, B3, det₂ (the metric γ3 of M3) do not give. So, as stated, (o) and (b′) are not proved, and
Placement 4's "so U has the bounds of (b′) for 2𝔐_V and c/2" inherits it. Since Placement 4 rewrites that sentence
anyway, the three texts below repair it. Placement 4 also says "its norm 𝒩_k at most 𝒩_k^V": the lemma itself says
𝒩_m is at most twice eq:class-energy (the ‖∂^j w‖, j ≥ 1, are counted again as ‖∂^(j−1) ∂w‖); "at most twice 𝒩_k^V".

Old (81:1378–1379):

```
(o) (Foliation.) There are r_V ∈ (0, r_*/2] and C_V, depending only on r_*, c, lower bounds for A3, B3 and det₂ of the
metric γ3 of V and bounds for the C² norms of g_V and the C¹ norms of p_V and Θ_V, such that for |z0 − z(p)| ≤ r_V the
```

New:

```
(o) (Foliation.) There are r_V ∈ (0, r_*/2] and C_V, depending only on r_*, c, lower bounds for A3, B3 and det₂ of the
metric γ3 of V, for −g_V⁻¹(dτ, dτ) and for g_V on TΣ_τ, and bounds for the C² norms of g_V and the C¹ norms of p_V
and Θ_V, such that for |z0 − z(p)| ≤ r_V the
```

Old (81:1393–1395):

```
(b′) (Leaf by leaf.) Let 𝔐 ≥ 1 bound the C³ norms of g and the C¹ norms of p_A and Θ_A of two states U and U′, the
inverses of lower bounds for A3, B3, det₂ of their metrics γ3 and the inverse of a lower bound for |p_A^Σ|, and
let |p_A(∂_z)| ≥ c on the axis for both. There are δ_𝔐 ∈ (0, r_*/16] and C, depending only on r_*, 𝔐 and c, such that for
```

New:

```
(b′) (Leaf by leaf.) Let 𝔐 ≥ 1 bound the C³ norms of g and the C¹ norms of p_A and Θ_A of two states U and U′, the
inverses of lower bounds for A3, B3, det₂ of their metrics γ3, for −g⁻¹(dτ, dτ) and for g on TΣ_τ, and the inverse of
a lower bound for |p_A^Σ|, and let |p_A(∂_z)| ≥ c on the axis for both. There are δ_𝔐 ∈ (0, r_*/16] and C, depending
only on r_*, 𝔐 and c, such that for
```

Placement 4, its new text, the last four lines (P-CLD 525–528):

Old:

```
being balls about V and its norm 𝒩_k at most 𝒩_k^V. For U in its ball 𝔅′, decreased if necessary, the C³ norms of g and
the C¹ norms of p_A and Θ_A are within C 𝒩_(k−1)^V(U) of those of V, by Sobolev's embedding ([[thm:std-bh-embedding]])
and k − 1 ≥ 5, and so are |p_A^Σ|, |p_A(∂_z)| and the lower bounds for A3, B3 and det₂; so U has the bounds of (b′) for
2𝔐_V and c/2.
```

New:

```
being balls about V and its norm 𝒩_k at most twice 𝒩_k^V. For U in its ball 𝔅′, decreased if necessary, the C³ norms of
g and the C¹ norms of p_A and Θ_A are within C 𝒩_(k−1)^V(U) of those of V, by Sobolev's embedding
([[thm:std-bh-embedding]]) and k − 1 ≥ 5, and so are |p_A^Σ|, |p_A(∂_z)| and the lower bounds for A3, B3, det₂,
−g⁻¹(dτ, dτ) and g on TΣ_τ; so U has the bounds of (b′) for 2𝔐_V and c/2.
```

With these, the uses in chapter 83 read correctly: 83:3763–3764 ("U and U′ have the bounds of (b′) for 2𝔐_Û and c_Û/2
… by ‖Z‖_(H^k) ≤ ρ, k ≥ 6, for ρ small") and 83:3866–3867, 3885 (𝔐_U, and W close to U) — the added lower bounds
are open conditions, held by the reference states and inherited by close states. Item 3's list "lower bounds for
−g_V⁻¹(dτ, dτ) and for g_V on TΣ_τ" then duplicates part of 𝔐_V; harmless.

### minor 6 — Tier 3's paragraph points to an H_L[Θ_A] that lem:class-leaf-differences no longer contains (83:2714–2715)

sec:loc-axis-leaves (Tier 3, merged) says "This is how H_L[Θ_A] of [[lem:class-leaf-differences]] is read: a function of
the point …". After Placement 1 the reading is the definition of H_L[U] in the paragraph before lem:class-leaf-states,
and lem:class-leaf-differences contains no H_L[Θ_A]. The file says Tier 3's item 8 is absorbed with "no statement
changes", and its use list does not include 83:2713–2716. A reader sent to the lemma does not find the object.

Old (83:2714–2715):

```
p_A(n) in place of Θ, ∇_Σu and n(u), and with the plane Π fixed by p_A. This is how H_L[Θ_A] of
[[lem:class-leaf-differences]] is read: a function of the point, as [[lem:class-volterra]] requires, which for a
```

New:

```
p_A(n) in place of Θ, ∇_Σu and n(u), and with the plane Π fixed by p_A. This is H_L[V] as defined before
[[lem:class-leaf-states]]: a function of the point, as [[lem:class-volterra]] requires, which for a
```

-----------------------------------------------------------------------------------------------------------------------

## nits

1. 81:1137, "The next section carries the recovery of (b) over to curved metrics." After the change of (a) the section
   recovers σ in L² (lem:class-leaf-states (c)) and σ² in every H^k, not σ in every H^k as (b) of prop:class-flat-model
   does in the flat case. The sentence is qualitative, but under the author's condition it is safer to say so.

Old:

```
perturbation perturbs. The next section carries the recovery of (b) over to curved metrics.
```

New:

```
perturbation perturbs. The next section carries the recovery of (b) over to curved metrics, for σ in L² and for σ² in
every H^k.
```

2. Placement 7's new text: "(a) about Ů, which bounds σ_A[𝐔]² − σ_A[Ů]² = σ_A[𝐔]² in H^k, bounds it by C ‖Z‖_(H^k)"
   is circular in wording, and the old clause "sup |σ_A| bounded on 𝔅" that served the product with the bounded factors
   of the first-order form is dropped (the bound still holds: sup |σ_A|² ≤ C ‖σ_A[𝐔]²‖_(H^k) by Sobolev).

Old:

```
so [[lem:class-leaf-differences]] (a) about Ů, which bounds σ_A[𝐔]² − σ_A[Ů]² = σ_A[𝐔]² in H^k, bounds it by C ‖Z‖_(H^k),
which gives (F1) and the linear bound; [[lem:class-leaf-differences]] (b), with
```

New:

```
so [[lem:class-leaf-differences]] (a) about Ů bounds σ_A[𝐔]² = σ_A[𝐔]² − σ_A[Ů]² in H^k by C ‖Z‖_(H^k), with Moser's
estimate for the bounded factors, which gives (F1) and the linear bound; [[lem:class-leaf-differences]] (b), with
```

3. lem:class-leaf-differences, statement, "Θ_A := □ů_A": the chapter writes □_g̊ ů_A (eq:class-energy).

Old (P-CLD 201):

```
Θ_A := □ů_A; its leaves h̊ and its planar shear σ[ů] are those defined before [[lem:class-leaf-states]], as are the
```

New:

```
Θ_A := □_g̊ ů_A; its leaves h̊ and its planar shear σ[ů] are those defined before [[lem:class-leaf-states]], as are the
```

4. lem:class-leaf-states, Step 1: "|p_A^Σ| ≥ c M^(−1/2)/2 on 𝒰_(4r_2), where p_A(∂_z) then has the constant sign ε" —
   |p_A^Σ| > 0 off the axis does not give p_A(∂_z) ≠ 0; the same Lipschitz argument applied to p_A(∂_z) does.

Old (P-CLD 67–68):

```
constant at most C, so there is r_2 ∈ (0, r_*/4] with |p_A^Σ| ≥ c M^(−1/2)/2 on 𝒰_(4r_2), where p_A(∂_z) then has the
constant sign ε. There H_L[U](x) = ℋ(x, W_U(x)), with ℋ a smooth function, the same for all states, on the set of (x,
```

New:

```
constant at most C, and so has p_A(∂_z); so there is r_2 ∈ (0, r_*/4] with |p_A^Σ| ≥ c M^(−1/2)/2 and |p_A(∂_z)| ≥ c/2
on 𝒰_(4r_2), where p_A(∂_z) has the constant sign ε. There H_L[U](x) = ℋ(x, W_U(x)), with ℋ a smooth function, the
same for all states, on the set of (x,
```

5. lem:class-leaf-states, Steps 2 and 6: "|G_U − G_(U′)| ≤ C (r + |q|) |U − U′|" and the like bound for 𝔖 are
   claimed from smoothness; the segment between W_U and W_(U′) need not lie where ℋ is smooth (the lower bounds and
   the sign ε are not convex conditions). It holds — by the mean value theorem for |U − U′| small, and trivially
   otherwise since |G| ≤ C (r + |q|) and |𝔖| ≤ C — but one clause says so.

Old (P-CLD 96):

```
(r, 0)), G_U and G_(U′) the functions [[eq:class-leaf-g]] of the two states.
```

New:

```
(r, 0)), G_U and G_(U′) the functions [[eq:class-leaf-g]] of the two states: by the mean value theorem where |U − U′| is
so small that the segment between W_U and W_(U′) lies in the set of Step 1, and elsewhere as both |G_U| and |G_(U′)| are
at most C (r + |q|); the same holds for the function 𝔖 of Step 6, which is bounded by C.
```

6. Steps 4 and 5 of the proof of (a): ℋ depends on the point through K1 (dψ1 = dz/z + ½ d log g_22 on M3), so 𝔤̂ needs
   the argument h; "For X ∈ {U, ů}" opening Step 5 is idle; and a_3 is a function also of ∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ,
   not only of the listed arguments. Harmless (a_3 η absorbs it).

Old (P-CLD 309):

```
[[eq:class-leaf-s]] is 𝔤̂(r t, s, W_X(h, (r t, 0))) with 𝔤̂ smooth, the same for all states. Differentiating
```

New:

```
[[eq:class-leaf-s]] is 𝔤̂(r t, h, s, W_X(h, (r t, 0))) with 𝔤̂ smooth, the same for all states. Differentiating
```

Old (P-CLD 339–341):

```
*Step 5 (Transverse derivatives).* For X ∈ {U, ů}, 𝔤̂(r t, s_U, W_U(h_U, ·)) − 𝔤̂(r t, s_ů, W_ů(h_ů, ·)) = a_1 · (ω ∘
Λ_U) + a_2 δs + a_3 η at the point (r t, 0) of the leaves, with a_1, a_2, a_3 smooth functions of r t, s_U, s_ů, W_U ∘
Λ_U, W_ů ∘ Λ_U and W_ů ∘ Λ_ů, the last difference being (∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ) η; and |a_2| = |∂_s 𝔤̂| ≤ C_2
```

New:

```
*Step 5 (Transverse derivatives).* 𝔤̂(r t, h_U, s_U, W_U(h_U, ·)) − 𝔤̂(r t, h_ů, s_ů, W_ů(h_ů, ·)) = a_1 · (ω ∘
Λ_U) + a_2 δs + a_3 η at the point (r t, 0) of the leaves, with a_1, a_2, a_3 smooth functions of r t, h_U, h_ů, s_U,
s_ů, W_U ∘ Λ_U, W_ů ∘ Λ_U, W_ů ∘ Λ_ů and ∫_0^1 ∂_z W_ů(h_ů + θη, ·) dθ, the factor of η in W_ů ∘ Λ_U − W_ů ∘ Λ_ů;
and |a_2| = |∂_s 𝔤̂| ≤ C_2
```

7. (P), P-CLD 325–326: "𝒩_(a+3) ≤ 𝒩_(m−1) for n ≤ m + 1, m ≥ 7" fails at m = 7, n = 8, a = 4 (a + 3 = 7). The first
   route of the same sentence (H²(Q̂) ⊂ L^∞ and the norm of order a + 2 = 6 ≤ m − 1, through eq:class-leaf-compose for
   ω ∘ Λ_U) covers it, so nothing is lost.

Old (P-CLD 326):

```
6, and 𝒩_(a+3) ≤ 𝒩_(m−1) for n ≤ m + 1, m ≥ 7. So the L² norm of such a product is at most C, or C_m, times the L² norm
```

New:

```
6, and 𝒩_(a+3) ≤ 𝒩_(m−1) for n ≤ m + 1 if a ≤ m − 4, the first bound serving if not. So the L² norm of such a
product is at most C, or C_m, times the L² norm
```

8. Step 1 of the proof of (a), for families: convergence of 𝒩_m(U_n − U) at the time considered after mollifying in τ
   needs ∂^j W continuous in τ into L² (true for the solutions used, which are in C([τ0, τ1]; H^k) with the τ-derivatives
   given by the equations). One clause would close it; no replacement offered.

9. The last statement is stated "for a solution of the class system with p_A = du_A and Θ_A = □_g u_A", but its proof
   uses only g⁻¹(du_A, du_A) = 0, p_A = du_A, Θ_A = □_g u_A and ∂_z u_A ≠ 0, and four sites cite it that way (83:2722,
   83:3078, 83:3650 "whose proof uses no field equation", 83:3863 for U := (g_e, −dv, …)). Stating it for a state with
   those properties ("for instance a solution …") would make these sites read the statement rather than the proof.
   Optional.

10. Placement 3's dependence list, and (o)/(b′), omit ρ1(p) (the weight 2π z, z ≤ 5ρ1(p)/4, and ℋ's x-dependence),
    as HEAD did. 83:3654–3657 lists the constants for V := Û as "C^(k+3) bounds of Û, … c_Û, … r_* and … r_Û"; after
    Placement 3 the lower bounds for Ĝ also enter; its conclusion "so only on k, Λ, κ, l" stands.

-----------------------------------------------------------------------------------------------------------------------

## The uses of the lemmas and of the shear at HEAD, rechecked

Grepped all 62 chapter sources for lem:class-leaf-differences, lem:class-leaf-reference, lem:class-planar-shear and the
shear (σ_A, σ[·], "planar shear", ‖σ). Only chapters 81, 82, 83 contain any. Each site:

- Through σ², or reworded by an item: 81:17–18 (item 9), 81:1286 and 1318–1319 (item 8), 81:1675 and 1704 (Steps 6, 9:
  S_A^ax holds −½ σ_A²), 81:1745–1757 (item 6), 82:2198–2199 and 2229 (balls and leaves of the lemma, checked as Step 6,
  9), 83:2933–2934 (item 7), 83:2975 (*Smoothness*), 83:3697–3698 and 3714–3716 (lem:class-leaf-reference (a), the
  difference of squares; "σ_A bounded in L^∞ on 𝒟_ρ by (a)" holds, σ² − σ̊² ∈ H^k ⊂ L^∞).
- Only the leaves bound (c): 81:1590–1591, 1605–1606 (item 5; I = {|z0 − z̊_B| ≤ δ_B} ⊂ [z(p) − δ, z(p) + δ] and D_B ⊂
  𝔻_δ, as δ_B ≤ δ/4; the H² argument in (z0, y) then gives W^(k,∞) as before).
- L²/L^∞ only: 81:1717, 1732–1734, 1785–1787; 83:509–511 (but see Major 1), 2781, 2934–2935, 2991, 3095, 3738–3740,
  3759–3761, 3891–3893.
- The leaves, the balls, δ or the constants, no bound of σ: 81:1540, 1547, 1583, 1587, 1638, 1659, 1673, 1700; 83:448
  (Major 1), 501, 2436–2443, 2774–2777, 2787, 2892, 3078, 3242, 3248, 3269, 3650–3661, 3668, 3692, 3708, 3735, 3757,
  3798, 3860–3867. Of these only 83:447–450 conflicts (Major 1); 83:2713–2715 is the stale pointer of minor 6.
- Qualitative: 81:1102–1103 (the flat model, proved there), 81:1137 (nit 1), 82:1802 and 1957 (smoothness of σ2/ρ2² for
  a smooth eikonal, own proof).
- The uses of lem:class-planar-shear's statement are its steps (1), (3), (4) and its constants (81:1437, 1445, 1659,
  1757; 83:503; the new block's definitions and last statement); none uses an H^k bound of σ.

No site after the merge needs an H^k bound of σ itself, so the Rellich-type question for angular mode 2 does not arise
in the paper (I did not settle it). The note's arguments for the change are right: σ involves the mode-2 coefficient
α = T(K2, K2)/|y|² of K_Σ and ∂γ3, while σ² = 2|χ̸ − ½(tr χ̸)γ̸|² is a smooth function of Cartesian quantities.

## Placement 1–9 checked

- Item 1: the old text is 81:1324–1357 exactly once as whole lines; it contains Tier 3's clause (81:1325–1331), which the
  new definitions carry (p_A(n), the sign of p_A(∂_z), Π the γ3-orthogonal complement of p_A^Σ). The block sits between
  the paragraph after lem:class-planar-shear and rem:class-leaf-numerics.
- Items 2–4: apply once each. With item 4, lem:class-leaf-reference (a), (b) follow from lem:class-leaf-differences with
  ů := V for δ ≤ δ_V = min(δ_0, r_V/8, δ_𝔐), with fixed balls, as Tier 4's corner and uniqueness proofs need — subject to
  minor 4 (ii) (V up to the closure) and minor 5 (the bounds of (o), (b′)). (o) and (b′) keep their proofs; with the
  lower bounds of minor 5 added, both hold, and (b′)'s C³ of g is more than (c) of lem:class-leaf-states needs.
- Item 5: reads correctly ("The / bounds of [[lem:class-leaf-differences]] (c), at the axis point z̊_B(τ), bound …").
- Item 6: closes. For σ = k the first part of (a) gives C_k constant; for σ > k, C_σ depends on sup_τ ‖U(τ)‖_(H^(σ−1)),
  bounded on each interval by the previous step (and for the iterates of the short-time scheme by its *Boundedness* at
  the order σ − 1), so Gronwall at the order σ is linear. The leaves are smooth by lem:class-leaf-states (a).
- Item 7: correct (nit 2 on wording).
- Item 8: step (5) proved for σ² from the Cartesian form k_L(X_i, X_j) = −(∂_i∂_j h + Γ[γ3]^c_ab X_i^a X_j^b ∂_c F)/|∇F|,
  lem:class-gauss (b) and Moser's estimate, with sup bounds from step (3), the C² norms of g and the C¹ norms of u; the
  statement's constants are unchanged. Correct.
- Item 9: correct.
- Scratch merge (git archive of HEAD in scratchpad/rpcld/): the 11 replacements each match exactly once as whole lines;
  lint.py --chapters: 62 files, 5056 labels, 0 hits; assemble.py --check: problems 0; the assembled check prints `[] 0`;
  no assembled line over 121 characters. The new lemmas assemble as Lemma 51.28 (lem:class-leaf-states) and 51.29
  (lem:class-leaf-differences); lem:class-leaf-reference becomes 51.31. With every replacement of this review applied
  on top (scratchpad/rpcld2 and rpcld3), the same three checks pass ([] 0, max line 121).
- Crosswalk: the 16 new rows are complete (lem:class-leaf-states and all 15 eq: labels of the block) and in the order of
  the labels in the merged chapter; rows 1–8 go between lem:class-planar-shear (row 61) and lem:class-leaf-differences
  (row 62), rows 9–16 between row 62 and rem:class-leaf-numerics (row 63); each PENDING:N is the line of its label in the
  file. Changed rows as listed; add lem:loc-lens-dependence (Major 1), and the rows of lem:class-leaf-reference and of
  sec:loc-axis-leaves (or lem:loc-axis-leaf) for minors 4–6 if adopted.

## Compatibility with Tier 5 (proofs/P-CIVP5.md, not merged)

- No label collision: P-CIVP5's labels (lem:class-leaf-arc, eq:class-leaf-arc, lem:class-leaf-tame, eq:class-leaf-tame,
  lem:class-kato-history, lem:class-mixed-product, thm:class-kato-memory, the loc-t5 family, …) are disjoint from the 17
  of this file. Its placement items replace no text that this file replaces.
- Text that becomes wrong if P-CLD lands first: Block A1, lines 11–12, "Its H_L is H_L[Θ_A] of
  [[lem:class-leaf-differences]], with TΣ_L there the γ3-orthogonal complement …" — no such object remains there; read
  "H_L[V] defined before [[lem:class-leaf-states]]".
- Block A1 defines *state*, *bounds (M, c)* and *arc* again, in the same section, with different content (bounds: C² of g
  and C¹ of p_A, Θ_A on 𝒰_(2δ), A3, B3, det₂ ≥ 1/M, |p_A^Σ| ≥ c and p_A(∂_z) ≥ c on 𝒰_(2δ); states with a free field 𝔤
  for ∂g). After P-CLD the section would carry conflicting definitions of these terms. lem:class-leaf-arc (a)–(c) is
  lem:class-leaf-states (a)–(c) with the roles of the two states exchanged, as the file says; it could be cited instead,
  except for the 𝔤-variant, which lem:class-leaf-states does not cover.
- lem:class-leaf-tame (eq:class-leaf-tame) is an H^n bound of σ_A[W] − σ_A[W̊] itself, used at P-CIVP5 704 through
  σ² − σ̊² = (σ − σ̊)² + 2σ̊(σ − σ̊). Under the author's condition for this file (no H^k bound of σ itself unproved
  anywhere) it would, after P-CIVP5 lands, be the one such bound in the paper; its reader should check its step (2)
  against the coefficient question of the file's note 5, and its step (6) against the logarithmic loss of note 1, or
  P-CIVP5 should state it for σ².

## What I checked and found correct

- Definitions: H_L[U] and σ[U] agree with step (1) of lem:class-planar-shear and eq:class-shear-leaf (ν_L = εν, k for
  ν_L = ε k for ν); |p_A^Σ| = |∇_M3 u_A| for p_A = du_A; the arc; 𝒰_δ ∩ M3.
- lem:class-leaf-states, Step 2: γ_z1 = C3 r, C3 = ∂_(y2) γ3(∂_z, ∂_(y2)) at (z, (r, 0)) by equivariance (an O(2)-
  equivariant field on the plane is a(|y|) y), so C3 and B̃ are first derivatives of g and ∂_z of them second; det₂ ≥ M⁻²,
  N_L² ≥ (1 + q²)/M; E_L = ν^r/a_L − q + rB̃/a_L; det₂ − γ_zz N_L² = −(γ_z1 + γ_zz q)²; eq:class-leaf-g; G(0, z, q) =
  −γ_zz q³/γ_22; eq:class-leaf-g-bounds including |∂_z G| ≤ C_1 (r + |q|) with only C² of g; |G_U − G_U′| ≤ C (r + |q|)|U −
  U′| (nit 5). Step 3: self-map (C_0 r_0/2 + C_2 (r_0 + δ_p) δ_p ≤ δ_p), contraction ≤ 1/2, |h′| ≤ (2/3) C_0 r, the leaf
  stays in R. Step 4: C_4 = (C_1 + C_2)(1 + C_0), r³/3 + r²/2 ≤ r² for r ≤ 1, eq:class-leaf-quotient. Step 5: r_1 ≤
  r_*/8, C_4 r_1² ≤ 1/2, the image contains [z(p) − 3r_1/4, z(p) + 3r_1/4], arcs of 𝒰_δ in 𝒰_(5δ/4). Step 6: mean
  curvature H_L[U] on the leaf, 𝔖 smooth, s has a limit at 0 (G/ρ continuous), r s′ → 0. Step 7: 𝔤 even, 𝒦 a self-map
  (|𝒦s| ≤ C_0/2 + C_4 r_1 C_0/3 ≤ C_0) and a contraction (≤ C_4 r_1/3 + C_4 r_1²/8 ≤ 1/2), C^j bounds of the iterates,
  Arzelà–Ascoli, the implicit function theorem, the Taylor argument for smoothness in y, z0[U] smooth. (b): the four-term
  split, |ζ − z0| ≤ 2|δh(r)|, the Volterra difference, D(r) ≤ C(∫ t f² dt)^(1/2), eq:class-leaf-pointwise. (c): the weight
  2πz, the absolutely continuous change of variables with Jacobian in [1/2, 3/2], R(z0) and G-invariance, ‖𝒜f‖ ≤ ‖f‖ on
  discs by Minkowski, (R²/2) ≤ 1, eq:class-leaf-sets with C independent of D and δ.
- lem:class-volterra's proof uses of G only G(0, z, p), the three bounds and continuity, as the file says; Step 3
  re-derives the contraction with |∂_z G| ≤ 2C_1 on R.
- lem:class-leaf-differences: 𝒩_m ≤ 2 eq:class-energy; eq:class-leaf-sup (H³ ⊂ L^∞ on the Lipschitz Σ ∩ 𝒰, product of
  an annulus and a disc); the balls, 𝔅 ⊂ 𝔅′, 4δ_0 ≤ r_1; (b) from lem:class-leaf-states (c) with D := Σ; the last
  statement (lem:class-leaf (b), lem:class-gauss (b), ν_L = εν, Π = TΣ_L, uniqueness); Step 1 density (Stein, mollify,
  G-average, (b) for L² convergence, |σ| ≤ C, weak limits); Step 3: the divergence identity along graphs, Φ_X a function
  of W_X, 𝔙 = y𝔰_X, ∂_P𝔙 = −√γ |dF|⁻¹(γ3^(ij) − ν^iν^j) negative definite and symmetric, 𝔓, k_L in the frame X_i, χ̸
  diagonal, σ² = 2|χ̸ − ½(tr χ̸)γ̸|², 𝔗 smooth with no division by r; Step 4; (Q) by Faà di Bruno, the Jacobians; Step 5:
  |a_2| ≤ C_2(1 + C_0) r t, the radial operators bounded by 1 and 9δ² on L²(𝔻_ρ) (minor 1 apart); Step 6: ρ_n, Q̂_n,
  lem:class-interior-regularity for Δ on 𝔻_(ρ_n) ⊂ 𝔻_(ρ_(n−1)), ‖T^j δu‖ ≤ 9δ² ‖T^j δΦ‖, the inverse 𝔓 with absorption;
  Step 7: S, S̊ ∘ Λ_U⁻¹ − S̊ ∘ Λ_ů⁻¹ by the mean value theorem in z, Λ_U(Q̂_k) ⊃ Q_δ, (c) from eq:class-leaf-elliptic at
  n = k and H²(Q̂_k) ⊂ L^∞. The scheme is loss-free: δΦ ∈ H^n needs W ∈ H^n, ∇δu ∈ H^(n+1), ∂_y η ∈ H^(n+1) needs g ∈
  H^(n+1), so ∂²_y η ∈ H^n.
- The two claims of the note on the transverse derivatives: the radial form gives ‖T^j η‖ ≤ 9δ² ‖T^j δs‖ with T^j δs
  from the Volterra contraction; the Cartesian F ↦ ∫_0^1 F(ty)·y dt is unbounded on L²(𝔻_R) — Minkowski gives ∫ t⁻¹ dt,
  and F = f(|y|) y/|y|, f(ρ) = 1/(ρ log(e/ρ)) on 𝔻_1, has F ∈ L² while ∫_0^r f diverges (truncations give ratios → ∞).
- Cited results say what is used: lem:class-leaf (b), (c), lem:class-gauss (b), (c), step (1) of lem:class-planar-shear,
  lem:class-interior-regularity (its proof applies to any two concentric discs), eq:class-leaf-volterra,
  eq:class-shear-leaf, prop:class-flat-model (b) (the Minkowski argument, "as in"), thm:std-bh-embedding (H³ ⊂ L^∞ in
  four variables, H² ⊂ L^∞ in three), thm:std-bh17-embedding (H¹ ⊂ L⁴ in three: 1 − 3/2 ≥ −3/4), thm:std-sy-extension
  (Stein on the Lipschitz Σ ∩ 𝒰 and on I × (Σ ∩ 𝒰)).
- Format of the merged text: self-contained, no file or program names, no process language in the block or the new
  texts, labels lowercase, lines ≤ 121, no bad wrapped-line starts.

Verdict: NOT CONFIRMED
