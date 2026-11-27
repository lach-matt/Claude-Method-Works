# R-P-CIVP5: independent line-by-line reading of proofs/P-CIVP5.md (Tier 5, further families at the axes)

File read: `research/warp-drive/paper/reader/proofs/P-CIVP5.md`, md5 226d1eae5f915d229723114e4b63121b, 1,227 lines.
Every line was read and every proof was followed in full. Also read: STYLE.md, READER-BRIEF.md, the writer's report
(notes/reports/P-CIVP5.md, round 2), R-P-CIVP4.md for the standard, chapter 81 lines 381–876 (sec:class-kato) and
1038–1368 (sec:class-axes, sec:class-planar-shear), chapter 83 lines 1171–1440 (sec:loc-cone-reduced and its lemmas)
and all of sec:loc-axis (2424–3247 before Tier 4), Appendix A entries thm:std-sy-extension, thm:std-bh-embedding,
thm:std-bh17-embedding, thm:std-gn-moser, chapter 90 sec:scope-families and the characteristic-problem paragraph.
Nothing under method/, drive/, extracted/ or recovered/ was read; no repository file was edited.

Bases (as the coordinator directed): "without Tier 4" = `git archive dd28a9b7~1` (= e6ec1d96); "with Tier 4" = `git
archive edafc288` (HEAD; chapters 81 and 83 and their crosswalks are byte-identical to dd28a9b7). Scratch:
`scratchpad/rpcivp5/` — `head/`, `t4h/` (archives), `m1/`, `m2/` (the file merged as written), `fix/P-CIVP5-fix.md`
and `fix/fix.diff` (the file with the replacement texts of this report applied), `m2f/` (the fixed file merged on the
Tier 4 base), merge script `tools/merge.py`.

Coordinator's relayed input from the writer of P-CLD (five claims) is checked and recorded at the end (section
"P-CLD claims"); claims (1), (2) and (4) are confirmed and appear below as Major 1, Major 3 and Major 2.

## Verdict: NOT CONFIRMED — 3 Major, 15 minor, 8 nits

The three Major findings are all in the proof of lem:class-leaf-tame (Block A1), on which the smoothness of the
development rests (thm:class-kato-memory (c) through (M1_σ), and (M1′) through lem:loc-t5-forcing). Each is a step that
is false or unproved as written; none has a repair I could write out and check in full, and the routes are indicated.
Everything else in the mathematics checked out up to the minor findings, in particular: lem:class-leaf-arc (b) (the
pointwise bound, including the claim that E_L's difference is O(r + |q|) times the jet difference, which is right
because C3 and D3 r are components of the Cartesian first derivatives of γ3 at the point); the composition estimate (C)
of step (5), which is correct; the whole of Block A2 (lem:class-mixed-product, lem:class-kato-history,
thm:class-kato-memory (a)–(c)) up to minor 7 and 8; the order of the constants (no circularity; minor 15 is about
presentation and data dependence); the slab/triangle argument of lem:loc-t5-uniqueness (sound, up to minors 4–6);
prop:loc-t5-grazing (b) (sound); the derivative counts; the Tier 3 citations; and the outside results (only Stein's
extension, the embeddings of [BH17] and the Moser estimates of Appendix A are used).

---------------------------------------------------------------------------------------------------------------------

## Major findings

### Major 1 — step (6) of lem:class-leaf-tame: D^α η for derivatives without a y-component is not bounded by (H) (line 179)

"D^α η is ∫_0^1 D^α[π(s y) · y] ds, at most C δ ‖D^α π‖ + C 𝒩_(m−1) by (H)." For α = ∂_t^a ∂_(z0)^b (no derivative in
y), D^α η(y) = ∫_0^1 (D^α π)(s y) · y ds, which carries the weight s⁰, not s^(1+j) with j ≥ 0; (H) does not apply.
The operator T F(y) := ∫_0^1 F(s y) · y ds is not bounded on L²(𝔻): for a radial field F = f(|y|) ŷ, T F(y) =
∫_0^|y| f, and f_n := 1_(1/n < ρ < 1/e) / (ρ log(1/ρ)) has ∫ f_n² ρ dρ ≤ 1 while T F_n ≥ log log n − 1 on
{1/e > |y| > ... } of fixed measure, so ‖T F_n‖/‖F_n‖ → ∞ (smooth truncations give the same). Invariance does not help:
D^α π = y q̂_α with q̂_α radial, and ‖|y|² 𝒜 q̂_α‖ ≤ C ‖y q̂_α‖ fails for the same f.

The pointwise part of π does have this profile. In (V), P = 𝔓(y, h, y 𝒜Φ) holds 𝔓(y, h, 0) = (γ3^(ij))⁻¹ γ3^(jz), a
pointwise function of the metric at (h(y), y), so ∂_t^m π contains ∂_t^m of the difference of γ3^(jz) at the point, with
no factor y and no average. Taking W − W̊ = φ(t) G(y) with ‖φ^(m)‖ = 1, ‖φ‖ = λ^(−m), λ ≫ n, and G with the profile f_n
in its γ3^(rz) component, ‖W − W̊‖_(H^m) stays bounded while the line integral in ∂_t^m η grows like log log n. So the
claimed inequality 𝒩_m ≤ C (‖W − W̊‖_(H^m) + 𝒩_(m−1)) is not proved, and (C), which uses ‖η‖_(H^m) with all its pure
(t, z0)-derivatives, and step (7) inherit the gap.

Why the bound may still hold: for invariant states γ3^(rz) = r C3 with C3 = ∂_(y2) γ3_(z y2) at (r, 0), a Cartesian
first derivative of g at the point; so the line integral is ∫_0^r ρ C3-difference, bounded by (H) with j = 0 by the
first derivatives of g — provided those are among the components of W and equal ∂g (see Major 2), and provided the
extraction of such coefficients is bounded in H^m (see Major 3).

Repair route (not written out here; it is new mathematics): bound the pure (t, z0)-derivatives of η through the radial
form, η = |y|² 𝒜(q̂ − q̂̊) with q̂ := P · y/|y|² = h′/r, by (H) with j = 0, which needs ‖D^α(q̂ − q̂̊)‖ ≤ C (‖W − W̊‖_(H^m)
+ 𝒩_(m−1)) + small · 𝒩_m. The P-CLD writer offers P-CLD's Step 5 (the radial Volterra form in s = h′/r) for this; I
have not read P-CLD and do not confirm it.

### Major 2 — step (1) of lem:class-leaf-tame identifies the fixed point of (V) with the leaf only when 𝔤 = ∂g (lines 107–129)

The lemma is stated for state paths W = (g, 𝔤, p_A, Θ_A) with 𝔤 "in place of ∂g", and by the convention of Block A1
"H_L, the leaves and σ are then computed with 𝔤 in place of ∂g". Step (1) derives (D) from the true divergence formula
H_L = (√γ)⁻¹ ∂_a(√γ ν^a): div_y V = d/dy_i[𝔙^i(y, h, ∂h)] holds the actual y- and z-derivatives of g, while Φ holds
∂_z(√γ ν^z) and ∂_z(√γ ν^i), "values of W", i.e. 𝔤. "The graph has mean curvature H_L[W] exactly when div_y V = Φ"
and "so it is the leaf, by lem:class-volterra" (line 127) are then true only when the parts of 𝔤 involved are the
actual derivatives of g. For 𝔤 ≠ ∂g, the solution of (V) and the leaf of lem:class-leaf-arc and of the system (the
solution of eq:class-leaf-volterra with E_L computed with 𝔤) solve different equations: their difference is ∂_g𝔙 ·
((∂_y + ∂h ∂_z) g − (𝔤_y + ∂h 𝔤_z)) inside the divergence.

This matters: lem:loc-t5-forcing applies the lemma to W := 𝐔̊ + Z_e for every path Z ∈ 𝒫_t̄, with 𝔤 = (g_τ, g_a) of Z,
and thm:class-kato-memory (a) and (c) apply (M1) and (M1_σ) to its iterates, for which g_τ = ∂_τ g and g_a = ∂_a g
fail in general (the first row of u^(n+1) is ∂_τ g^(n+1) = g_τ^n). Defining σ_A for such states through (V) instead
does not work either: then δP holds the pointwise term Δγ3^(rz) = r ΔC3 with C3 read from g, and ‖δh‖_(L²) is not
bounded by ‖U − V‖_(L²) uniformly on the C^5-ball (take Δγ3^(rz) = δ/(ρ log(1/ρ)) on [μ, 1/e] with δ ≤ r μ⁶: the ratio
grows like log log(1/μ)), so (M2) would fail.

Repair route: keep the definition of the leaves of lem:class-leaf-arc (eq:class-leaf-volterra with E_L, C3 and D3 r read
from 𝔤, so that every coefficient is a pointwise function of (g, 𝔤, p_A, Θ_A)), and prove the space-time tame bound for
those leaves — for instance by the per-slice elliptic route of lem:class-leaf-differences (a), differentiated in t_A
and in the transverse direction, with the zero-order term of the radial form (R-P-CIVP4's Major 5 repair) — or show
that only states with 𝔤 = ∂g enter (not true for the paths of 𝒫_t̄ as the hypotheses are formulated).

### Major 3 — step (2) of lem:class-leaf-tame: "𝔖 smooth; no division by |y| occurs" is false as a function of the components (lines 130–136, used in step (7))

σ_A[W] = |p_A^Σ|(H_L − 2k_φ) − p_A(n)(K_Σ(e_r, e_r) − K_Σ(e2, e2)) holds K_Σ(e2, e2) = K_Σ(K2, K2)/|K2|² and, in k_φ,
½ ν(log B3) with B3 = γ3(K2, K2)/|y|², and e_r ∝ ŷ + (ŷ · P) ∂_z. Each is the coefficient α of an invariant tensor αδ +
β y⊗y, a quotient by |y|²: a smooth function of y for each smooth invariant tensor (the argument "as a_⊥ in
eq:class-axis-metric is" shows that), but not a smooth function of the pointwise Cartesian components and of y jointly,
which is what the chain rule of step (7) ("by (C), lem:class-composition (b) and (c)") needs. A loss-free bound ‖α‖_(H^m)
≤ C ‖T‖_(H^m) for invariant T is a Rellich-type inequality for angular mode 2, which the paper does not prove (this is
P-CLD's claim (2); I agree that the step as written needs it). k_φ is written through 𝒜Φ only for ν(log r); ν(log B3) is
an α-derivative.

Uses of eq:class-leaf-tame: lem:loc-t5-forcing (through σ − σ̊, after writing σ² − σ̊² = (σ − σ̊)² + 2σ̊(σ − σ̊), lines
704–706), lem:loc-t5-residual (b) (the σ² terms), rem:class-kato-memory and rem:loc-t5-scope (iv). The system holds σ_A
only through σ_A², and σ² = 2|χ̸ − ½(tr χ̸)γ̸|² is a smooth function of the components and of the leaf's second
fundamental form, without α; so stating the tame bound for σ_A² (or for the closure term) would serve every use, but
lem:loc-t5-forcing does not go through σ² as written, and the σ² route needs its own proof (the second fundamental form
holds ∂P, one order above 𝒩_m in step (6)). I have not verified P-CLD's statement that the σ² version holds.

---------------------------------------------------------------------------------------------------------------------

## minor findings

All replacement texts below were applied to a copy of the file (scratchpad/rpcivp5/fix/P-CIVP5-fix.md; diff in
fix/fix.diff) and merged on the Tier 4 base (m2f/): `lint.py --chapters` "62 file(s), 4961 label(s) defined, 0 hit(s)";
`assemble.py --check` "labels 4961, computations cited 0, problems 0"; the in-memory check prints `[] 0`; no assembled
line exceeds 121 characters; no wrapped line has a forbidden start.

### minor 1 — lem:class-leaf-arc (a): the stated |∂_z G_X| ≤ C_1 does not give |π| ≤ C r (lines 40–45)

From |∂_z G_X| ≤ C_1 the π-equation gives only sup |π| ≤ C_1 (1 + r S/2) + S/4, a bounded π, not the displayed
"C_1 r/2 (1 + r sup|π|)". |∂_(z0) h′| ≤ C r is needed in (b) ("|∂_(z̄) h_U′|/r ≤ C by (a)"). The stronger bound is
true (lem:loc-axis-shear (1) states it). Old (line 40):

```
(M, c), |G_X(r, z, 0)| ≤ C_0 r, |∂_z G_X| ≤ C_1 and |∂_q G_X| ≤ C_2 (r + |q|), and the map 𝒯 of that proof, with the
```

New:

```
(M, c), |G_X(r, z, 0)| ≤ C_0 r, |∂_z G_X| ≤ C_1 (r + |q|) and |∂_q G_X| ≤ C_2 (r + |q|), the bound of ∂_z G_X because
E_L^X(0, z, q) = A3 q³/B3 and E_L^X − E_L^X(0, ·) is r times a smooth function; and the map 𝒯 of that proof, with the
```

Old (lines 43–45, from ":= ∂_(z0) h′ solves" to "≤ ½. So"):

```
:= ∂_(z0) h′ solves r π(r) = ∫_0^r (∂_z G_X (1 + ∫_0^ρ π) + ∂_q G_X π) dρ. Hence sup_[0,r] |π| ≤ C_1 r/2 (1 + r
sup_[0,r] |π|) + ¼ sup_[0,r] |π|, which gives |π| ≤ C r for r ≤ r_1 small, and |∂_(z0) h − 1| ≤ ∫_0^r |π| ≤ C r² ≤ ½. So
```

New:

```
:= ∂_(z0) h′ solves r π(r) = ∫_0^r (∂_z G_X (1 + ∫_0^ρ π) + ∂_q G_X π) dρ. Hence, as |q| ≤ C_0 ρ, sup_[0,r] |π| ≤ C_1
(1 + C_0) r/2 (1 + r sup_[0,r] |π|) + ¼ sup_[0,r] |π|, which gives |π| ≤ C r for r ≤ r_1 small, and |∂_(z0) h − 1| ≤
∫_0^r |π| ≤ C r² ≤ ½. So
```

(In (b), "C_1 ρ D(ρ)" stays valid with the stronger bound.)

### minor 2 — lem:class-leaf-arc (c): the set of y is not always a disc (lines 77–78)

For z0 near the edge of the range, |z0 − z(p)| ≥ δ/2, the condition x ∈ 𝒰_(δ/2) holds only for |y| in an interval away
from 0, so the set can be an annulus. The estimate stands with the disc of the supremum radius, whose points are arc
points of points of the set. Old:

```
D is G-invariant and closed under the arcs of V, for each z0 the set of y with x ∈ D ∩ 𝒰_(δ/2) is a disc {|y| < R(z0)}
or {|y| ≤ R(z0)}; the arc points of its points lie in D, and in 𝒰_δ, since they are within C δ² of x in z. For the
```

New:

```
D is G-invariant and closed under the arcs of V, for each z0 the set of y with x ∈ D ∩ 𝒰_(δ/2) lies in the disc {|y| ≤
R(z0)}, R(z0) the supremum of its |y|, and every point (h_V(|y|; z0), y) with |y| < R(z0) is an arc point of one of its
points, so it lies in D, and in 𝒰_δ, being within C δ² of that point in z. For the
```

### minor 3 — lem:class-leaf-tame, statement: the radii (lines 86–96, 101–103)

- 𝒰_δ(p) is defined for δ ≤ ρ1(p)/4; with δ0 ≤ ρ1(p)/4, 𝒰̄_(4δ0)(p) reaches ρ1 = 0 (axis 1), where the coordinates
  (z, y) fail. Line 87: "0 < δ0 ≤ ρ1(p)/4" → "0 < δ0 ≤ ρ1(p)/16" (applied in fix/; the application has δ′ ≤ ρ_-/32).
- Lines 101–103 obtain the leaves through |z0 − z(p)| < 3δ over 𝔻_(3δ) from lem:class-leaf-arc (a), which, as stated,
  needs the state on 𝒰_(6δ); W is given on 𝒰_(4δ) only. It follows from the proof of (a), the leaves staying within
  C(3δ)² < δ of their axis points. Read "by the proof of [[lem:class-leaf-arc]] (a), the leaves staying within C (3δ)² ≤
  δ of their axis points, the leaves of W through …".
- The statement gives one δ; the application (closure radius, line 655: "δ ≥ δ′"; lem:loc-t5-forcing:
  "𝒰_(4δ′)(p)") uses it at δ′. Every condition on δ in the proof is a smallness condition, so state: "There are δ_1 ∈
  (0, δ0] and r > 0 such that for every δ ∈ (0, δ_1] and every integer n ≥ 0 there is C_n (depending also on δ) …", and
  in the closure radius read "… holds … with δ := δ′ and r ≥ ρ′" with δ′ ≤ δ_1.

### minor 4 — lem:loc-t5-past, lem:loc-t5-constraints, lem:loc-t5-uniqueness: arc-closure is needed on the whole set where lem:class-leaf-arc (c) is applied (lines 785–793, 835–836, 943–947 and 967)

lem:class-leaf-arc (c) requires the arc of V through every point of D ∩ 𝒰_(δ/2) to lie in D. The proofs apply it with δ′
and D a whole slice of the region, but establish arc-closure only for points within δ_♮/2 ≤ δ′/2 of the axis and, for a
further family, at points where ξ_A ≠ 0: at points of the slice near a tangency set the edge section is not a leaf
(prop:loc-t5-grazing), and those points lie in D. Only the points where the closure is used matter, so take D to be the
union of their arcs and δ := δ_♮. In lem:loc-t5-past, old (lines 786–787 from "ρ_i(x) < δ_♮/2" and the first half of 788):

```
ρ_i(x) < δ_♮/2 for an axis i and, for a further family, ξ_A(x) ≠ 0, and let D := (𝒟 ∪ {τ ≤ τ_init}) ∩ {t_A = t_A(x)} ∩
{τ ≤ s}. Every point y of D near the axis has its arc of Û in D: in {τ ≤ τ(y)} by [[lem:loc-t5-times]] (c); in the
```

New:

```
ρ_i(x) < δ_♮/2 for an axis i and, for a further family, ξ_A(x) ≠ 0, and let D be the union of the arcs of Û, in the
slice {t_A = t_A(x)}, through the points y of (𝒟 ∪ {τ ≤ τ_init}) ∩ {τ ≤ s} in that slice at which the closure of A is
used. D is G-invariant and closed under the arcs of Û, and it lies in (𝒟 ∪ {τ ≤ τ_init}) ∩ {τ ≤ s}: the arc of such a
point y lies in {τ ≤ τ(y)} by [[lem:loc-t5-times]] (c); in the
```

and old (lines 792–793):

```
[[lem:class-leaf-arc]] (c), with V := Û and U := U, gives ‖σ_A[U] − σ_A[Û]‖_(L²(D∩𝒰_(δ′/2)(p))) ≤ C
‖z‖_(L²(D∩𝒰_(δ′)(p))) at every point p of the axis; squaring and integrating over t_A(x), by Fubini's theorem in the
```

New:

```
[[lem:class-leaf-arc]] (c), with δ := δ_♮, V := Û and U := U, gives ‖σ_A[U] − σ_A[Û]‖_(L²(D∩𝒰_(δ_♮/2)(p))) ≤ C
‖z‖_(L²(D∩𝒰_(δ_♮)(p))) at every point p of the axis; squaring and integrating over t_A(x), by Fubini's theorem in the
```

The same two changes in lem:loc-t5-constraints ("bounds the term in σ_A in L²(D_(A,t,s) ∩ 𝒰_(δ′/2)(p))": take the
union of the arcs of U′ through the points of D_(A,t,s) within δ_♮/2 of an axis, and δ := δ_♮) and in
lem:loc-t5-uniqueness (the sets D_(A,t,s) with δ := δ_♮(N)). lem:class-leaf-arc allows any δ ≤ r_1 with a constant
independent of δ, and δ_♮ ≤ δ′ ≤ r_1/4.

### minor 5 — the lateral boundary of 𝒯_A is not shown to be admissible for lem:loc-t5-energy (lem:loc-t5-constraints, lem:loc-t5-uniqueness)

lem:loc-t5-energy takes 𝒟, B_0, B_1 "as in lem:loc-cone-energy": every 𝒟_s a Lipschitz domain and B_1 a finite union of
smooth hypersurfaces. The proofs estimate Δ_A (and z for family A) "on 𝒯_A only", with no flux through "the lateral
boundary of 𝒯_A, ruled by integral curves of P_A". That boundary is the flow-out of ∂𝒦_A″, of which nothing is
assumed (𝒦_A″ is a union of 𝒦_A′ and caps). Fix without boundaries: multiply the rows of family A by a smooth function
κ_A with P_A(κ_A) = 0 (P_1^A in the uniqueness lemma), equal to 1 on 𝒯_A and supported where the phase is defined (κ_A
:= κ̄_A on N transported along P_A, κ̄_A a cut-off equal to 1 on 𝒦_A″ and supported in the interior of 𝒦_A′): for the
transport rows ∂_μ(κ_A V^μ) = κ_A ∂_μ V^μ, as V^μ ∂_μ κ_A = |z_A|² P_A(κ_A) = 0, and family A enters the other rows only
through q_A, which vanishes off 𝒯_A.

### minor 6 — lem:loc-t5-uniqueness: the hypothesis on the further families' components is too strong to be checked (lines 922–923; used in thm:loc-t5 (c), (d))

"If U_2 and U_1 agree, with all their derivatives, on the past faces" includes the components of the further families
everywhere on the faces, in particular at their tangency sets, where their transverse jets are not determined by the
data (prop:loc-t5-grazing (a)). The proof uses agreement of family A only on 𝒦_A″. thm (c) checks agreement only on the
crossing sets, and thm (d) applies the lemma with U_1 := Ů and 𝒦_A″ := ∅ although U's further phases need not be ů_A on
{u < u_K, v < v_K} (the data U_A are not assumed to be ů_A there, and (d)'s proof says "Û = Ů there", which is not true
for the further phases). Old (line 923, with the end of 922):

```
derivatives, on the past faces, then U_2 = U_1 on R′. No smallness of U_1, of U_2 or of U_2 − U_1 is assumed.
```

New:

```
derivatives, on the past faces, the components of each further family A only on 𝒦_A″, then U_2 = U_1 on R′, the
components of each further family A on 𝒯_A. No smallness of U_1, of U_2 or of U_2 − U_1 is assumed.
```

and in (d), old (lines 1034–1035):

```
[0, u′] × {0} are the background's ([[lem:loc-axis-jets]] (b), [[lem:loc-t5-jets]] (b)), so Δ and the further Borel sums
vanish at the points with u < u_K and v < v_K, Δ being supported within 2δ_e of N, and Ĝ = g_e and Û = Ů there. The
```

New:

```
[0, u′] × {0} are the background's ([[lem:loc-axis-jets]] (b), [[lem:loc-t5-jets]] (b)), so Δ and the Borel sums of
the further densities vanish at the points with u < u_K and v < v_K, Δ being supported within 2δ_e of N, and Ĝ = g_e
there and Û = Ů there except in the phases of the further families. The
```

### minor 7 — Block A2: the coefficients are given on [0, T0] only (line 201)

The setting of sec:class-kato gives A^μ on [0, T0] × R^d × R^m, while lem:class-kato-history and thm:class-kato-memory
use them on [t1 − m, t2] and [−m, T0] ([−2m, T0] for the paths), and "bounds of order s for the A^μ" must be taken
there. Old (line 201): "*Space-time norms.* Keep the setting of this section, and let J = [a, b] be an interval. H^σ(J)
is the space of". New:

```
*Space-time norms.* Keep the setting of this section, with the A^μ given, with the properties stated there, for t in an
interval containing every interval of times used below ([−2m, T0] in [[thm:class-kato-memory]]), the bounds of order σ
taken over it, and let J = [a, b] be an interval. H^σ(J) is the space of
```

### minor 8 — thm:class-kato-memory (a): the choice of η and T* gives ηρ + ρ, not ρ (lines 340–341)

⟦·⟧ over [−2m, t1 + T] is a sum over j of ess sups over the union, so it is at most ⟦h − u_*⟧_(s,[−2m,t1]) + ⟦w⟧_(s,J) ≤
ηρ + Bηρ + B T^(1/2)(T + m)^(1/2), which the stated choice bounds by ηρ + ρ. Old:

```
B depending only on the quantities of (a). Choose η ≤ 1/(2B) and then T* so small that B T*^(1/2) (T* + m)^(1/2) ≤ ρ/2:
then ⟦u^(n+1) − u_*⟧_(s,[−2m,t1+T]) ≤ ρ, and u^(n+1) ∈ 𝒫_(t1+T). *Contraction.* For n ≥ 1, δ^(n+1) := u^(n+1) − u^n
```

New:

```
B ≥ 1 depending only on the quantities of (a). Choose η ≤ 1/(4B) and then T* so small that B T*^(1/2) (T* + m)^(1/2) ≤
ρ/4: then ⟦u^(n+1) − u_*⟧_(s,[−2m,t1+T]) ≤ ⟦h − u_*⟧_(s,[−2m,t1]) + ⟦w⟧_(s,J) ≤ η ρ + ρ/2 ≤ ρ, and u^(n+1) ∈
𝒫_(t1+T). *Contraction.* For n ≥ 1, δ^(n+1) := u^(n+1) − u^n
```

(η ≤ 1/(2C_E) from the line before is kept.)

### minor 9 — lem:loc-t5-forcing: the extension's C^5 constant depends on σ, and Stein's operator is used on an unbounded slab (lines 684–686, 691–692, 696)

ρ is fixed with C_E of E_b for N := k + 1 (line 685), but the proof extends with N := σ + 1 for every σ ≥ k and claims
‖Z_e‖_(C^5) ≤ C_E C_5 ρ; C_E = Σ_l |c_l| grows with N, so for σ > k the C^5-smallness the tame lemma needs is not
ensured. Line 696 applies "Stein's extension from the slab", but thm:std-sy-extension states Stein's operator (bounded
on L^∞, which lem:class-composition needs) for bounded Lipschitz domains. One operator in t, independent of σ, fixes the
first. Old (lines 684–685):

```
− τ_init, s := k, u_* := 0, the memory m := 2m_* + 2 and a radius ρ ≤ ρ′/(C_E C_5), where C_E is the constant of the
extension E_b with N := k + 1 and C_5 is such that ‖Z‖_(C^5) ≤ C_5 ⟦Z⟧_(k,J) for Z ∈ 𝒳^k(J) on intervals J of length at
```

New:

```
− τ_init, s := k, u_* := 0, the memory m := 2m_* + 2 and a radius ρ ≤ ρ′/(C_X C_5), where C_X bounds on W^(5,∞) the
operator X_b defined in the proof of [[lem:loc-t5-forcing]] and C_5 is such that ‖Z‖_(C^5) ≤ C_5 ⟦Z⟧_(k,J) for Z ∈
𝒳^k(J) on intervals J of length at
```

Old (lines 691–692):

```
*Proof.* Let Z be a path in 𝒫_t̄, and for t̄′ ≤ t̄ let Z_e := E_(t̄′) Z be its extension beyond t̄′ by the operator of
[[sec:class-kato]] with N := σ + 1, σ ≥ k the order considered, and with the length m_* + 1; ‖Z_e‖_(C^5) ≤ C_E C_5 ρ.
```

New:

```
*Proof.* For a time b let X_b extend functions of (t, x) from [b − m_* − 1, b] × ℝ⁴ to [b − m_* − 1, b + m_* + 1] × ℝ⁴ by
Stein's extension operator of the interval [b − m_* − 1, b] in t at each x ([[thm:std-sy-extension]]), translated so that
it does not depend on b; it commutes with ∂_x, so it is bounded on every H^σ and on every W^(j,∞), with constants
independent of b. Let Z be a path in 𝒫_t̄, and for t̄′ ≤ t̄ let Z_e be Z on [−2m, t̄′] and X_(t̄′) Z on the interval
[t̄′, t̄′ + m_* + 1]; ‖Z_e‖_(C^5) ≤ C_X C_5 ρ, and the norms of Z_e of order σ on [t̄′, t̄′ + m_* + 1] are at most C_σ
times those of Z on [t̄′ − m_* − 1, t̄′].
```

and read E_(t2) as X_(t2) in the rest of the proof (four places), and at line 696 extend in t by X_(t1) reflected and
X_(t2) (or say "after the extension X_b at both ends, bounded on H^σ and on L^∞") in place of "Stein's extension from
the slab".

### minor 10 — lem:loc-t5-residual (b) states a fixed-time bound; lem:loc-t5-existence uses a space-time one (line 718)

(b) states sup_τ ‖R(τ)‖_(H^k) ≤ Cε; thm:class-kato-memory (b) needs δ := ‖R‖_(H^k([τ_init − m, s*])), the space-time
norm with time derivatives, which lem:loc-t5-existence takes from (b). The proof of (b) in fact bounds the space-time
norm (C^k bounds and lem:class-leaf-tame, which is space-time). Old:

```
(b) R := 𝔄_χ(Ů) − F̃ is smooth, supported in supp χ, zero on {τ0 ≤ τ_0′}, and sup_τ ‖R(τ)‖_(H^k) ≤ C ε.
```

New:

```
(b) R := 𝔄_χ(Ů) − F̃ is smooth, supported in supp χ, zero on {τ0 ≤ τ_0′}, and ‖R‖_(H^k(J)) ≤ C ε for every interval J
of times of length at most s* − τ_init + 2m_* + 2, H^k(J) the space-time norm of [[sec:class-kato]].
```

### minor 11 — overclaims about the grazing families, (F-a) and (F1)–(F2)

prop:loc-t5-grazing proves: finite-order vanishing ⇒ the section is not a leaf and arcs cross the edge; all sections
leaves ⇒ the edge is characteristic; the infinite-order case is not analysed (the paragraph after the proposition and
rem:loc-t5-scope (i) say so). Several sentences claim more. Replacements (all applied and checked in fix/):

(a) Block B introduction (lines 431–434). Old:

```
([[thm:loc-t5]]). A family that carries density where it is tangent to an edge at an axis is excluded, and the
reason is proved: no section of that edge by the slice of a time function is a leaf of the family there, while the
energy estimates of the construction need these sections to be leaves ([[prop:loc-t5-grazing]]). Such families are
developed on regions that avoid the axes near the points concerned ([[prop:loc-t5-cut]]).
```

New:

```
([[thm:loc-t5]]). A family that carries density where it is tangent to an edge at an axis is excluded. Where the
restriction of its phase to a section of that edge by the slice of a time function vanishes to finite order at the
axis, the section is not a leaf of the family and points arbitrarily near the axis have arcs that cross the edge, while
the energy estimates of the construction need the arcs of the points of a region to stay in it; where all these
sections are leaves, the edge is characteristic for the family; the remaining case is not analysed
([[prop:loc-t5-grazing]]). Such families are developed on regions that avoid the axes near the points concerned
([[prop:loc-t5-cut]]).
```

(b) thm:loc-t5 statement (lines 980–981). Old:

```
(F-b) excludes the families that carry density where they are tangent to an edge along an axis generator, as the
construction cannot treat them there ([[prop:loc-t5-grazing]]); (F-a) excludes density near the circles in which the
```

New:

```
(F-b) excludes the families that carry density where they are tangent to an edge along an axis generator, where the
construction does not apply ([[prop:loc-t5-grazing]]); (F-a) excludes density near the circles in which the
```

(c) The paragraph after prop:loc-t5-grazing (lines 900–901). Old:

```
So (F-b) excludes the families that carry density near a point x_0 of a tangency set because the construction of this
section, in any slicing, cannot treat them there. At every point x′ of the tangency set near x_0 at which, for the slice
```

New:

```
So (F-b) excludes the families that carry density near a point x_0 of a tangency set because the construction of this
section, in any slicing, does not apply to them there, except possibly in a case not analysed. At every point x′ of the
tangency set near x_0 at which, for the slice
```

(d) Line 512 (proved: the tubes come near the tangency set; not proved: no other construction). Old: "(F-a) cannot be
weakened to the vanishing of the density on the corner circles alone: by the proof above, a family of". New:

```
For this construction (F-a) cannot be weakened to the vanishing of the density on the corner circles alone: by the
proof above, a family of
```

(e) Block A2 introduction (lines 198–199): "then fail" is not proved; rem:class-kato-memory says only that the estimates
do not give them. Old:

```
computed on the leaves of hypersurfaces that are not the slices of the time: the fixed-time hypotheses (F1)–(F2) then
fail, while their integrated forms hold ([[rem:class-kato-memory]]).
```

New:

```
computed on the leaves of hypersurfaces that are not the slices of the time: the estimates of the leaves then give the
integrated forms of the fixed-time hypotheses (F1)–(F2), and not those hypotheses ([[rem:class-kato-memory]]).
```

(f) Placement items 4 and 5 ("the construction failing there", "cannot treat"): see minor 12 for item 4; item 5's new
text, old (its last three lines):

```
in which the corner sphere meets the axes ([[thm:loc-t5]]), and shows that this construction cannot treat a family
with density where it is tangent to a cone at an axis ([[prop:loc-t5-grazing]]). (iii) *Regularity.* The data are smooth
and small in C^(m_1); densities that
```

New:

```
in which the corner sphere meets the axes ([[thm:loc-t5]]), and shows that this construction does not apply to a family
with density where it is tangent to a cone at an axis, except possibly in a case it does not analyse
([[prop:loc-t5-grazing]]). (iii) *Regularity.* The data are smooth and small in C^(m_1); densities that
```

The regularity claims of the Block B introduction, of thm:loc-t5 (a) and of items 4 and 5 ("smooth") stand only once
Majors 1–3 are repaired.

### minor 12 — placement item 4 does not apply at the Tier 4 base (lines 1130–1145)

Its old line "([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. No
development is" occurs once at dd28a9b7~1 (83:728) but 0 times at dd28a9b7 / edafc288, where Tier 4 rewrote that
paragraph (83:729–739). Rebased (the sentence goes after Tier 4's, before "No development is asserted"); old (83:734 at
edafc288), exactly once:

```
[[rem:civp-axes-scope]]). No development is asserted for data of finite regularity or for densities that are not smooth,
```

New:

```
[[rem:civp-axes-scope]]). Near the background's, further null dusts, of phases that are not functions of u or of v, may
be added to the cone data through the axes, any number of them, when at the points where a cone meets an axis each
carries density only where it crosses that cone and none near the circles in which the corner sphere meets the axes; the
development on the whole rectangle is then smooth, with an estimate, and unique in the gauge among nearby solutions
([[thm:loc-t5]]). A family that carries density where it is tangent to a cone along an axis generator is not treated,
the construction not applying there ([[prop:loc-t5-grazing]]); such data are developed on regions that avoid that axis
near those points ([[prop:loc-t5-cut]]). No development is asserted for data of finite regularity or for densities that
are not smooth,
```

The item's sentence "Only this line is replaced, so that the item composes with placements that rewrite the sentence
beginning "No development is" on the lines after it" should then read that the line is Tier 4's last line before that
sentence. All other anchors apply exactly once at both bases (item 5 at 83:3251, item 6 at 81:1674 / 1839; A1 before
sec:class-axes-stability, after lem:class-leaf-reference at the Tier 4 base; A2 before sec:class-off-axes; B before
sec:civp-axes / sec:loc-shells).

### minor 13 — prop:loc-t5-cut: (F-c) for the cut data, and ε depends on χ_c (lines 1043–1077)

- "The new data … satisfy (F-a)–(F-c) by (N1) and (N3)": multiplying q_A by χ_c changes the transverse jets of q_A at
  the points of S_c where χ_c is not locally constant, and (F-c) at such points (where A crosses both edges — near but
  off the corner circles, inside N_c ∖ N_0, this happens) does not follow from (N3), which concerns q_A. χ_c cannot be
  taken constant near S_c (S_c is connected and χ_c = 0 near the corner circles). Add a hypothesis: "(N4) no family of
  𝒢 crosses both edges at a point of S_c ∩ (N_c ∖ int N_0)", or require χ_c near S_c to be the restriction of a function
  constant along the integral curves of P̊_A, and say which.
- The size of the cut data in C^(m_1) is at most C(χ_c) ε, so ε must be small depending on the C^(m_1) norm of χ_c, not
  only on N_0, N_c and λ; and (b) compares two admissible cut-offs. Read "For ε small, depending also on N_0, N_c, λ and
  a bound for the C^(m_1) norms of the cut-offs χ_c considered".

### minor 14 — lem:loc-t5-jets (b) gives no bound, but ‖Û − Ů‖_(C^(k+3)) ≤ Cε is asserted for the further families (lines 531–578)

(b) determines ∂_u^j u_A and ∂_u^j q_A but states no estimate, and the field jets now carry the further stress as an
inhomogeneous term; the bound of lem:loc-axis-jets (iii) is cited only for fields. The recursion loses one derivative
along N per order for u_A (the eikonal equation holds ∂_a ∂_u^(j−1) u_A) and two for q_A (□_g holds angular second
derivatives), within the count m_0 = 6k + 18, but this must be said. Add to (b): "and their C^r norms on the crossing
sets are at most C ε, C depending on r and j, for data of size ε in C^(r + 2j + c), c fixed", with the count checked
against m_0 for j ≤ k + 3 (I did not fix c).

### minor 15 — order of choice and data dependence of 𝒦_A″, ξ_A, t_A and δ_♮ (lines 516–529, 579–597, 648–656, 803–808)

No circularity, but as written: (i) 𝒦_A″ is defined in the proof of lem:loc-t5-constraints from the caps of the
A-sections of the data, and "we choose 𝒦_A′ and ξ_A for 𝒦_A″ from the start" — 𝒦_A′ is a hypothesis of the theorem and
the constants depend on it; and ξ_A then depends on the data, as do Ĝ_A, K and t_A (through U_A). Define 𝒦_A″ in the
paragraph *Carrying a family near its tube*, with the caps of the background's sections (ů_A) of a fixed width 2δ_2,
which contain the data's caps of width δ_2 for ε small, build ξ_A from it, and define K from the background's Ĝ_A plus
1. (ii) Further smallness conditions on δ_♮ appear after it is fixed: lem:loc-t5-past ("for δ_♮ small"),
lem:loc-t5-constraints (δ_♮ e^(L(s*−τ_c)) ≤ δ_2, L a Lipschitz constant of the flow of P_A — take L for P̊_A plus 1),
prop:loc-t5-cut (δ_♮ ≤ w/4), and the condition that the caps of the edge sections from points within δ_♮ of the axis
lie in {ζ_A = 1}. All are geometric; collect them where δ_♮ is fixed. (iii) lem:loc-t5-faces assumes only "(b) of
lem:loc-t5-times holds", but its proof uses that û_A is null to infinite order on S, which holds where ζ_A = 1: add "and
ζ_A = 1 on the cap of S" to the hypothesis.

---------------------------------------------------------------------------------------------------------------------

## nits

1. Step (6) of lem:class-leaf-tame (lines 175–177): the display of D^α π omits the term ∂_z𝔓 · D^α η from the second
   argument of 𝔓 (it is bounded by C ‖D^α η‖ and is absorbed like the others), and the Leibniz sum Σ_e should carry the
   multiplicity β_e.
2. Lines 103–105: the approximants must be G-invariant (average Stein's extension over G and mollify with a G-invariant
   kernel), and their C^5 distance from W̊ is C r (the extension's W^(5,∞) bound), so treat smooth W with radius C r.
3. Crosswalk: the 18 rows from sec:loc-t5-times to rem:loc-t5-scope give a line one too small (577 for 578, …, 1078 for
   1079). The other 15 rows are right; all 33 have four tab-separated fields and their labels are those the blocks
   define, in chapter order (checked in m1/ and m2/: label order of chapters 81 and 83 equals row order).
4. Lines 492–493: "So the tangency sets are where a family meets an edge with the edge's own orientation, the case in
   which two families are not angularly separated" suggests that non-separation is special to the tangency sets; family
   A of ingoing type is not separated from the ingoing family on the whole axis, crossing points included. Read "…
   where a family has the orientation of the adapted family whose phase defines that edge, from which it is then not
   angularly separated ([[prop:class-separation]] (c)); at the crossing points it is not separated from the other
   adapted family."
5. thm:class-kato-memory (c), *Higher norms*: θ (and the partition τ_i) must be taken anew for each σ (C_* and C
   depend on σ); say "fix, for this σ, a partition with τ_(i+1) − τ_i ≤ θ".
6. Lines 509–510: the short line "𝒦′, by" — rewrap.
7. Line 101: "By [[lem:class-leaf-arc]], with M and c replaced by 2M and c/2, for r small every slice … has bounds" — the
   bounds come from ‖W − W̊‖_(C^5) ≤ r, not from the lemma; reorder.
8. rem:loc-t5-scope (i): "where they are leaves the edge is characteristic for the family on an open set" — (c) needs
   all the sections through the axis points near x_0; read "where all of them near a point are leaves".

---------------------------------------------------------------------------------------------------------------------

## The writer's questions

- Steps 5 and 6 of lem:class-leaf-tame. (C) is correct: the Faà di Bruno terms, k′ ≤ m − 1, the Hölder exponents with
  reciprocals summing to ½, the change of variables (Jacobian ≥ ½) and the weighted AM–GM all check, the C^1 smallness
  of F being unnecessary. Step 6 has Major 1; step 1 has Major 2; step 2 has Major 3.
- Order of constants: K (from Ĝ_A on supp ψ_A) → δ_* (by (a) and (d), needing C¹ of Ĝ_A, ψ_A and K) → charts (t_A, y),
  (τ, y) → M, c, δ′, ρ′, C_L (compactness in the bent charts) → r_L(C_L, δ_*) → δ_♮ ≤ min(δ′, r_L) → ψ_♮ and the system
  → ρ ≤ ρ′/(C_X C_5) → ε. No step uses a later constant; the issues are those of minor 15.
- lem:loc-t5-uniqueness: the triangles T_N = {ũ, ṽ ≥ 0} ∩ {τ^N ≤ 1} lie in R′ and exhaust {ũ < a, ṽ < b} (Φ_N → 0 and
  τ^N − Φ_N ≤ 1/(4N)); their slices are bounded by the past faces and {τ^N = s} only, so arcs never leave through a
  future null face; the cap condition puts the arcs in 𝒯_A; the Taylor bound on 𝒩_θ needs no convexity (each D^β of
  U_2 − U_1 is expanded along the segment to the nearest point); the slab lies in 𝒩_(θ/8) and the leaves of W there are
  those of U_2. It replaces Tier 3's Lemma R correctly. Open: minors 4, 5, 6.
- prop:loc-t5-grazing (b): correct (L transverse to the axis, h_S − h_L of sign b_j/∂_z u_A with |h_S − h_L| ≥ c_1
  |y|^(2j), the level set through z_0 = z(x_0) + d crossing S at radius about (2d/c_1)^(1/(2j))).
- Tier 3 citations: each cited statement says what is used (sec:loc-axis-reduced and its paragraphs *The chart*, *The
  system*, eq:loc-axis-time/region, lem:loc-axis-leaf (i)–(iii), lem:loc-axis-jets (a)–(c), lem:loc-axis-constraints
  (a)–(c), lem:loc-axis-system (a)–(e), lem:loc-axis-energy, lem:loc-axis-past, lem:loc-axis-propagation (*The
  phases*), lem:loc-axis-gauge (and its last statement), lem:loc-axis-dependence (*The chart*, *The equations*,
  *Continuity in t*), lem:loc-axis-unique steps (1)–(4), def:loc-axis-data, thm:loc-axis; and from Tier 1
  eq:loc-cone-modified, lem:loc-cone-energy and the paragraph after it, lem:loc-cone-system (c), lem:loc-cone-jets).
  "τ_0′ := ln(9δ_c²/16)" is right with Tier 3's τ0, whose β-terms are nonnegative. No pending marker remains.
- Derivative counts: k ≥ 9 gives the C^5 control (H^(k−j) ⊂ C^(5−j) on the slices for j ≤ 5 needs k > 7), the C^(k−3)
  bounds of 𝐔 − 𝐔̊ and Ψ − id, hence C^(k−4) for the fields, as in Tier 3; uniqueness in C^(k−4) uses only C^5-type
  bounds of the second solution for the leaves and the wave map of lem:loc-axis-unique (k − 5 > 3). m_1 = 2p with p =
  m_0 + 3. The further jets need minor 14.
- Smoothness: thm:class-kato-memory (c) is proved correctly from (M1_σ) (global iteration from u_*, the M_i and M′_i
  inductions, the matching at t = 0); (M1_σ) rests on lem:class-leaf-tame, hence on Majors 1–3 (and minor 9).
- Scope of the exclusions: stated exactly in rem:loc-t5-scope (i)–(iii) and the paragraph after prop:loc-t5-grazing,
  the unanalysed subcase included; the overclaims elsewhere are minor 11 (a)–(f).
- prop:loc-t5-cut: existence on D′ from thm:loc-t5 for the cut data and independence of χ_c by the energy argument on
  D′ with the face {λ = 0} are correct (jets outside N_c see only data outside N_c by (N2), the corner point of each
  generator included; past causal curves from D′ stay in D′); minor 13. rem:loc-t5-scope (i) correctly says that no
  uniqueness among other solutions on D′ is given.
- Outside results: thm:std-sy-extension (Stein: bounded Lipschitz domains, all W^(k,p), 1 ≤ p ≤ ∞, used on the boxes
  𝒟̂, 𝒱_4 and an interval; minor 9 for the slab), thm:std-bh-embedding and thm:std-bh17-embedding (on unit cubes, in
  lem:class-mixed-product (a), with the exponents checked), thm:std-gn-moser (1), cor:std-moser-product (1), and the
  interpolation inequality of the proof of lem:class-composition (a). Nothing else.
- Placement: item 7 is right (chapter 90's sentence at line 183 concerns the Cauchy problem; ch:theorems and ch:scope
  make no claim about further families in the characteristic problem). Item 8 (no new Appendix A entry) is right.

## P-CLD claims (relayed by the coordinator; P-CLD itself not read)

1. Step (6), D^α η with weight s⁻¹ and a logarithmic loss at the axis: confirmed independently, Major 1 (counterexample
   given there). P-CLD's Step 5 as the repair: not checked.
2. σ = 𝔖(…, 𝒜Φ) needs a loss-free bound for α = T(K2, K2)/|y|²: confirmed as a gap in step (2), Major 3. Not every use
   goes through σ²: lem:loc-t5-forcing uses σ − σ̊; the system needs only σ², so a σ² version would serve all uses if
   proved.
3. lem:class-leaf-arc (a)–(c) = P-CLD's lem:class-leaf-states (a)–(c) with the states swapped: for the coordinator.
   If P-CLD is merged first, Block A1 should cite it instead of defining lem:class-leaf-arc (and minors 1–2 then apply
   to whichever text is merged), and the crosswalk rows change.
4. The free field 𝔤 not covered by P-CLD's divergence-form part: consistent with Major 2, which shows that the
   divergence form with 𝔤 ≠ ∂g does not define the leaves of the system.
5. "Its H_L is H_L[Θ_A] of [[lem:class-leaf-differences]]" (line 10) would need to read "defined before
   [[lem:class-leaf-states]]" if P-CLD lands first: agreed; a merge-order item, not a finding against this file.

Verdict: NOT CONFIRMED
