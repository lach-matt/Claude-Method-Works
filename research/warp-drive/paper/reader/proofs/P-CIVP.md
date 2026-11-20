### Block A. Additions to the section on exact localisation on the cones

The text of this block goes into [[sec:loc-cones]] after the proof of [[prop:loc-cones]]; the Placement section below
gives the exact position and the paragraph it replaces.

**Lemma {#lem:loc-cone-in}** (Exact localisation on the ingoing cone.) On the ingoing cone 𝒞_in = {v = 0} take b = 0,
write γ_ϑ = e^(2ϕ + 2ℓ_1), A_c = ϕ + ℓ_2, A_s = ϕ + ℓ_3 with ℓ_1 + ℓ_2 + ℓ_3 = 0, keep Ω the background's, and let the
free data (ℓ_1, ℓ_2, ℓ_3) and the outgoing density q_out on 𝒞_in equal the background's outside a compact subset of a
band {ϑ_a < ϑ < ϑ_b} × [0, u_1], the values of ϕ and ∂_uϕ at u = 0 being the background's. Then on 𝒞_in

    Ric(∂_u, ∂_u) = Σ_(i=1)^3 (−∂_u²ϰ_i − (∂_uϰ_i)² + 2 ∂_u ln Ω ∂_uϰ_i),                       {#eq:loc-cone-in}

so the constraint Ric(∂_u, ∂_u) = T(∂_u, ∂_u) on 𝒞_in determines ϕ on every generator on which e^ϕ stays positive,
and the resulting data equal the background's on every generator with ϑ ∉ [ϑ_a, ϑ_b]. No smallness is used for the
localisation; for small perturbations e^ϕ stays positive on [0, u_1]. The component Ric(∂_u, ∂_ϑ) = T(∂_u, ∂_ϑ) = 0
on 𝒞_in contains the derivative ∂_v b across 𝒞_in: it is a linear transport equation for ∂_v b along the generators,
and it places no condition on these data ([[lem:loc-cone-ricci]] (a)).

*Proof.* On 𝒞_in, b = 0, so ∂_u b = ∂_ϑ b = 0 there, and g(∂_u, ∂_u) = γ_ϑ b² and g(∂_u, ∂_ϑ) = −γ_ϑ b vanish there. So
∂_u is null and orthogonal to ∂_u, ∂_ϑ, ∂_(φ1), ∂_(φ2) along 𝒞_in: it is the null normal of 𝒞_in, and the sections {u =
const} of 𝒞_in carry γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2². With the inverse metric of the proof of
[[lem:loc-cone-equations]], Γ^u_(uu) = ½ g^(uv)(2∂_u g_(uv) − ∂_v g_(uu)) = 2∂_u ln Ω + ∂_v(γ_ϑ b²)/(4Ω²), and ∂_v(γ_ϑ
b²) = b (2γ_ϑ ∂_v b + b ∂_vγ_ϑ) = 0 on 𝒞_in; Γ^v_(uu) = ½ g^(vu) ∂_u(γ_ϑ b²) + ½ g^(vϑ)(2∂_u g_(ϑu) − ∂_ϑ g_(uu)) and
Γ^ϑ_(uu) = ½ g^(ϑv)(2∂_u g_(vu) − ∂_v g_(uu)) + ½ γ_ϑ⁻¹(−2∂_u(γ_ϑ b) − ∂_ϑ(γ_ϑ b²)) vanish there, since g^(vϑ) =
−b/(2Ω²); and Γ^(φi)_(uu) = 0. So ∇_(∂_u)∂_u = 2∂_u ln Ω ∂_u on 𝒞_in. The field ∂_u commutes with ∂_ϑ, ∂_(φ1), ∂_(φ2), so
for X, Y among these g(∇_X ∂_u, Y) = −g(∂_u, ∇_X Y) on 𝒞_in is symmetric in X and Y, and the null second fundamental form
of the sections along ∂_u is half the u-derivative of their metric, with eigenvalues ∂_uϰ_i. The Raychaudhuri equation
along ∂_u is [[eq:loc-cone-in]], as in the proof of [[lem:loc-cone-equations]]. With y := e^ϕ, T(∂_u, ∂_u) = q_out and
(ln Ω)′ = 0 on 𝒞_in (there e^(2σ) = 1/2), it reads y″ + (1/3)(Σ_i (ℓ_i′)² + q_out) y = 0, ′ = ∂_u, and the proof of
[[prop:loc-cones]] applies with u in place of v. ∎

On the corner sphere S = 𝒞_out ∩ 𝒞_in the two cones carry one metric, γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2² with the
background's ϕ, so the free data of [[prop:loc-cones]] at v = 0 and those of [[lem:loc-cone-in]] at u = 0 agree; nothing
else is required at S, the density q_in being free on 𝒞_out and q_out on 𝒞_in. Near the background's data, and with the
band away from the axes, these cone data have a development.

**Theorem {#thm:loc-cone-development}** (Development of cone data localised in angle.) Let u_1, v_1 > 0 be such that
R > a on the segments 𝒞_out ∩ {v ≤ v_1} and 𝒞_in ∩ {u ≤ u_1}, a = 0.70 the inner radius of [[sec:loc-setting]], let
R_min be the least value of R on them and C_0 := 2√2/R_min. Let 0 < ϑ_a < ϑ_b < π/2, η := (1/4) min(ϑ_a, π/2 − ϑ_b),
k ≥ 6 an integer and m := 6k + 21. Take free data (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0 on 𝒞_out ∩ {v ≤ v_1} as in
[[prop:loc-cones]], and (ℓ_1, ℓ_2, ℓ_3) and q_out ≥ 0 on 𝒞_in ∩ {u ≤ u_1} as in [[lem:loc-cone-in]], the two sets of
free data agreeing on S. Let them be smooth and equal to the background's outside compact sets K_out ⊂ [0, v_1) ×
(ϑ_a, ϑ_b) and K_in ⊂ [0, u_1) × (ϑ_a, ϑ_b) of the coordinates (v, ϑ) and (u, ϑ), and let ε be the largest absolute
value of a derivative of order at most m of their differences from the background's. Let [ϑ_a′, ϑ_b′] be the least
interval that contains the angles of the points of K_out ∪ K_in, u_K the least u on K_in and v_K the least v on K_out
(u_K := u_1 if K_in is empty, v_K := v_1 if K_out is). There is δ_* > 0, depending only on the background, u_1, v_1
and the band, and there are ε_0, C, ε_2 > 0, depending also on k, such that for ε ≤ ε_0, with

    G_* := {(u, v) : 0 ≤ u ≤ u_1, 0 ≤ v ≤ v_1, uv ≤ δ_*²},                                          {#eq:loc-cone-domain}

the following hold.

(a) *Existence.* The factors e^ϕ of [[prop:loc-cones]] and [[lem:loc-cone-in]] stay positive, and there is a smooth class
solution of [[eq:class-system]] on G_* × S³ with two families, an ingoing one with phase v and density q_in and an
outgoing one with phase u and density q_out, so that Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, whose metric has the form
[[eq:loc-double-null]] in the coordinates (u, v, ϑ, φ1, φ2), and which induces on 𝒞_out the functions Ω, γ_ϑ, b, A_c,
A_s and q_in of [[prop:loc-cones]] and on 𝒞_in those of [[lem:loc-cone-in]], with b = 0. G_* contains the strips
{u ≤ δ_*²/v_1} and {v ≤ δ_*²/u_1} of the rectangle [0, u_1] × [0, v_1], a future neighbourhood of both cones.

(b) *Localisation.* The solution equals the background at the points of G_* × S³ with ϑ < ϑ_a′ − 2C_0 (uv)^(1/2) or
ϑ > ϑ_b′ + 2C_0 (uv)^(1/2), and at those with u < u_K and v < v_K. In particular it equals the background where
ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η.

(c) *Estimate.* At the points of G_* × S³ with η ≤ ϑ ≤ π/2 − η the functions ln Ω, ½ ln γ_ϑ, b, A_c, A_s, q_in and
q_out differ from the background's by at most Cε, together with their derivatives of order at most k − 4.

(d) *Uniqueness.* Let a second smooth class solution of the same kind be given on G_* × S³, with the metric in the form
[[eq:loc-double-null]] in its coordinates (u, v, ϑ, φ1, φ2), inducing the same data, whose functions of (c) differ from
the background's by at most ε_2, together with their derivatives of order at most k, at the points with 2η ≤ ϑ ≤
π/2 − 2η. Then it equals the solution of (a) at the points with 3η ≤ ϑ ≤ π/2 − 3η. If moreover it equals the
background at the points of G_* × S³ with ϑ < 3η or ϑ > π/2 − 3η, it equals the solution of (a) on G_* × S³.

Data with q_in = 0 and q_out = 0 are vacuum data, and their development is vacuum, the densities being transported. The
theorem is proved in [[sec:loc-cone-proof]]. For the background of [[sec:bg-data]], R ≥ 5 on 𝒞_out and R > 1.5 on
𝒞_in ∩ {u ≤ 7.2} ([[lem:loc-cone-strips]] (c)); so u_1 = 7.2 and every v_1 > 0 are admissible, and with v_1 = 4.5 the
data may perturb the shell on 𝒞_out ∩ {3 < v < 4.5} and the packet on 𝒞_in ∩ {5.7 < u < 7.2} at once.

**Remark {#rem:loc-cone-scope}** (What [[thm:loc-cone-development]] does not give.) (i) *Smallness.* The data must be
near the background's. For cone data that carry dust and are not small nothing is asserted. For vacuum data of any
size [CTG23, Theorem 1.1] ([[thm:std-ctg-neighbourhood]]) gives a development near the two cones, with neither
uniqueness in the gauge nor localisation. (ii) *The axes.* The band avoids the axes, and by (b) so does the
perturbation in the development. The proof uses the augmented system of [[sec:class-augmented]] only where it is local,
off the axes; the dusts of the background, which reach the axes, are carried there by the background itself. For data
whose perturbation reaches an axis this fails: at an axis the augmented system is not local, its Cauchy theory
([[thm:class-stability]]) needs lateral boundaries adapted to the dust, and no domain-of-dependence statement with null
boundaries near an axis is proved in this paper. No development is asserted for such data, and (d) gives uniqueness
near the axes only among solutions that equal the background there. (iii) *Regularity.* The data are smooth and near
the background's in C^m, m = 6k + 21. Densities that are only bounded, or measures (shells), are not covered. For the
3 + 1 problem with two families of null dust, possibly measure-valued, [LR20, Theorem 4.6, p. 29] states: "Given a
strongly angularly regular reduced characteristic initial data set … there exists ε > 0 sufficiently small such that
whenever u_∗ ∈ (0, I] and u̲_∗ ∈ (0, ε], there exists a unique angularly regular weak solution to the Einstein–null
dust system … in the domain [0, u_∗] × [0, u̲_∗] × S² which achieves the prescribed initial data." (iv) *The domain.*
The development is asserted on G_*, a neighbourhood of the two cones, and not on the whole rectangle [0, u_1] ×
[0, v_1]; in particular not where the two dusts cross away from the cones.

### Block B. The development of the cone data {#sec:loc-cone-proof}

This section proves [[thm:loc-cone-development]], and, with the same proof, a development near any corner sphere for
cone data of any size on a small rectangle ([[prop:loc-cone-local]]). The method is Rendall's reduction of the
characteristic problem to the Cauchy problem ([Ren90, p. 221]: "A method is described by means of which the
characteristic initial value problem can be reduced to the Cauchy problem"), carried out for the augmented system of
[[sec:class-augmented]] off the axes. First, the double-null equations determine every derivative of the metric
functions and the densities across the two cones by linear ordinary differential equations along the generators, and the
derivatives so found agree at the corner sphere ([[lem:loc-cone-jets]]). A smooth extension with these derivatives is a
formal solution: its residual in every equation vanishes to infinite order on the cones ([[prop:loc-cone-formal]]); the
constraints that the data satisfy on the cones propagate to all orders by the contracted Bianchi identity. In a
wave-map gauge whose reference metric is that extension, the gauge condition holds identically for the extension. The
Cauchy problem for the augmented system, with the formal solution's residual as a forcing term to the past of the cones
and a cut-off near the axes, where the solution is the background, is solved by [[thm:class-kato-stability]] (a)
([[lem:loc-cone-cauchy]]). To the past of the cones the solution is the formal solution ([[lem:loc-cone-past]]); so it
takes the data, and the gauge condition and the constraints hold to infinite order on the cones, and then everywhere to
their future ([[lem:loc-cone-constraints]]). The two phases and an angle transported along the outgoing generators are
double-null coordinates in which the solution takes the given data ([[lem:loc-cone-gauge]]), and two solutions in the
gauge are compared through a wave map ([[lem:loc-cone-unique]]).

#### The setting {#sec:loc-cone-setting}

*Corners and edges.* Let l_u, l_v > 0 and δ_1 ∈ (0, min(l_u, l_v)/2], and translate u and v so that the corner is
(0, 0). Put N_o := {0} × [0, l_v + δ_1], N_i := [0, l_u + δ_1] × {0}, N := N_o ∪ N_i, the corner sphere S_c := {(0, 0)} ×
S³, F := {u ≥ 0, v ≥ 0}, P := {u < 0} ∪ {v < 0} and

    𝒮 := {(u, v) : −δ_1 ≤ u ≤ l_u + δ_1, −δ_1 ≤ v ≤ l_v + δ_1, min(u, v) ≤ δ_1}.                {#eq:loc-cone-collar}

Points of the (u, v)-plane stand for the corresponding spheres; a set of points is identified with its product with S³. A
*background* on 𝒮 is a round metric g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with σ_e, R_e > 0 smooth on 𝒮, together with
smooth profiles 𝒜(v), ℬ(u) ≥ 0, such that on 𝒮 ∩ F it solves the two-null-dust equations [[eq:two-dust-limit]],
Ric(g_e) = (𝒜/R_e³) dv ⊗ dv + (ℬ/R_e³) du ⊗ du. Its double-null functions are Ω_e² = e^(2σ_e)/2, γ_ϑ = R_e², A_c = ln(R_e
cos ϑ), A_s = ln(R_e sin ϑ), b = 0, and its densities are q̊_in := 𝒜/R_e³ and q̊_out := ℬ/R_e³; so ρ̊_in := 𝒱q̊_in = 𝒜(v)
sin ϑ cos ϑ and ρ̊_out := ℬ(u) sin ϑ cos ϑ, with 𝒱 of [[sec:loc-cone-equations-frame]]. A *class solution in the gauge*
on a set D × S³, D ⊂ F, is a smooth class solution of [[eq:class-system]] with two families, phases v and u and densities
q_in and q_out, so that Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, whose metric has the form [[eq:loc-double-null]] with Ω,
γ_ϑ, b, A_c, A_s smooth functions of (u, v, ϑ), equal to the background's near the axes.

**Definition {#def:loc-cone-data}** (Cone data at a corner.) Let a background on 𝒮 be given and k ≥ 6. *Cone data* are
smooth functions ln Ω, ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, b and q_in ≥ 0 of (v, ϑ) on N_o and ln Ω, ϰ_1, ϰ_2, ϰ_3, b
and q_out ≥ 0 of (u, ϑ) on N_i, such that: (i) ln Ω, the ϰ_i and b of the two edges agree on S_c; (ii) Ric(∂_v, ∂_v) =
q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o, the left sides being given by [[eq:loc-cone]] in terms of the functions on N_o, and
Ric(L̲, L̲) = q_out on N_i, L̲ := ∂_u + b∂_ϑ, the left side being given by the last line of [[eq:loc-cone-frame-ricci]]
in terms of the functions on N_i, L̲ being tangent to N_i; (iii) for some numbers 0 < ϑ_a′ < ϑ_b′ < π/2 they equal the
background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′]. Their *size* is the largest absolute value of a derivative of order at
most m_0 := 6k + 18 of their differences from the background's. They are in the *normalised gauge* if b = 0 on N_i; then
Ric(L̲, L̲) on N_i is [[eq:loc-cone-in]]. The data consist of the gauge functions ln Ω on both edges and b on N_i, which
are free, of the conformal data and densities, which are free, and of the functions that (ii) determines; the corner
values are arbitrary, subject to (i).

The data of [[thm:loc-cone-development]] are cone data at the corner S, with l_u = u_1, l_v = v_1: on 𝒞_out the
functions of [[prop:loc-cones]], extended to v ≤ v_1 + δ_1 by the background's, and on 𝒞_in those of
[[lem:loc-cone-in]], extended likewise; the extensions are smooth, as K_out ⊂ [0, v_1) × (ϑ_a, ϑ_b) and K_in ⊂
[0, u_1) × (ϑ_a, ϑ_b). The background on 𝒮 is provided by the next lemma.

**Lemma {#lem:loc-cone-strips}** (The background near the cones.) Let u_1, v_1, R_min and C_0 be as in
[[thm:loc-cone-development]].

(a) There is δ_1 ∈ (0, min(u_1, v_1)/2] such that the background of [[sec:bg-data]] is defined and smooth on the strips
S_out := [0, δ_1] × [0, v_1 + δ_1] and S_in := [0, u_1 + δ_1] × [0, δ_1], with R > a and 2e^σ/R ≤ C_0 there.

(b) Decreasing δ_1, there are smooth functions σ_e, R_e on the set 𝒮 of [[eq:loc-cone-collar]] (with l_u = u_1, l_v =
v_1) equal to σ, R on S_out ∪ S_in = 𝒮 ∩ F, with R_e > a/2 and e^(σ_e)/R_e ≤ C_0 on 𝒮. So g_e := −2e^(2σ_e) du dv +
R_e² dΩ₃², with the profiles 𝒜 and ℬ of [[eq:bg-profiles]], is a background on 𝒮.

(c) R ≥ 5 on 𝒞_out, and R > 1.5 on 𝒞_in ∩ {u ≤ 7.2}.

*Proof.* (a) By [[lem:two-dust-reparametrisation]] (b), [[prop:two-dust-background]] holds in the coordinates of
[[sec:bg-data]]: the set G of its part (d) is closed in Q = [0, ∞) × [0, V1′] (V1′ the image of V1), its boundary in Q
lies in {R = a}, and the background is smooth on G. A point p of the segment 𝒞_in ∩ {u ≤ u_1} lies in G, since
J⁻(p) is the part of 𝒞_in with u ≤ u(p), where R ≥ R_min > a, and it is not on the boundary of G in Q, since R(p) > a.
So p is an interior point of G relative to Q; the same holds on 𝒞_out ∩ {v ≤ v_1}, and by continuity on the slightly
longer segments, R > a there. By compactness a strip of some width δ_1 along each segment lies in G. On the cones
e^(2σ) = 1/2, so 2e^σ/R = √2/R ≤ √2/R_min = C_0/2 on the segments, and 2e^σ/R ≤ C_0 on the strips once δ_1 is small.

(b) Apply [[lem:loc-cone-borel]] below, with r := 0, to the derivatives ∂_u^j σ, ∂_u^j R on {u = 0} and ∂_v^k σ, ∂_v^k R
on {v = 0}, one-sided where the strips end; they agree at the corner, being derivatives of functions smooth on
S_out ∪ S_in. The function equal to σ on S_out ∪ S_in and to the extension on 𝒮 ∖ F has, from both sides, the same
derivatives of every order on N, so it is smooth; likewise for R. By continuity R_e > a/2 and e^(σ_e)/R_e ≤ C_0 on 𝒮
after decreasing δ_1, since 2e^σ/R ≤ C_0 on S_out ∪ S_in.

(c) On 𝒞_out, e^(2σ) = 1/2 is constant, so [[eq:bg-field]] gives R_vv = −𝒜/(3R²), with R = 5 and R_v = 1/2 at v = 0
and 0 ≤ 𝒜 ≤ 3.6 supported in [3, 4.5] (the bump β is at most 1). While R ≥ 5 on [0, v], R_v(v) ≥ 1/2 − (3.6 × 1.5)/
(3 × 25) = 0.428 > 0; so R increases, and R ≥ 5 on all of 𝒞_out. On 𝒞_in, R = 5 − 0.47u ≥ 2.321 for u ≤ u1 = 5.7
([[lem:bg-reduction]] (a)), and R > 1.5 for 5.7 ≤ u ≤ 7.2 ([[sec:loc-setting]], from [[prop:bg-nprime]]). ∎

For [[prop:loc-cone-local]] the background is the one of this chapter or any other background on 𝒮 in the sense
above; the proofs below use of it only the properties listed there and the bound C_* := sup over 𝒮 of e^(σ_e)/R_e,
which for [[thm:loc-cone-development]] is at most C_0.

#### The equations in the double-null gauge {#sec:loc-cone-equations-frame}

Let g have the form [[eq:loc-double-null]] off the axes, with ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, and put

    L̲ := ∂_u + b ∂_ϑ,   𝒱 := e^(ϰ_1 + ϰ_2 + ϰ_3),   η := ∂_ϑ ln Ω,   ζ := (γ_ϑ/(4Ω²)) ∂_v b,
    χ_i := ∂_vϰ_i,   χ̲_1 := L̲ϰ_1 + ∂_ϑ b,   χ̲_2 := L̲ϰ_2,   χ̲_3 := L̲ϰ_3,   tr χ := Σ_i χ_i,   tr χ̲ := Σ_i χ̲_i.
                                                                                                {#eq:loc-cone-quantities}

The χ_i are the eigenvalues of the null second fundamental form of the sections {u, v = const} along ∂_v, the χ̲_i
those along L̲, which is the null normal field of the hypersurfaces {v = const}: g(L̲, L̲) = g_(uu) + 2b g_(uϑ) +
b² g_(ϑϑ) = 0 and g(L̲, ∂_ϑ) = g_(uϑ) + b g_(ϑϑ) = 0. With K_i := ∂_(φi), the fields (L̲, ∂_v, ∂_ϑ, K_1, K_2) form a
frame with

    g(L̲, ∂_v) = −2Ω²,   g(∂_ϑ, ∂_ϑ) = γ_ϑ = e^(2ϰ_1),   g(K_i, K_i) = e^(2ϰ_(i+1)),   all other products 0,
    [∂_v, L̲] = (∂_v b) ∂_ϑ,   [∂_ϑ, L̲] = (∂_ϑ b) ∂_ϑ,   all other brackets of the frame 0.

**Lemma {#lem:loc-cone-frame}** (The connection.) The covariant derivatives of the frame are

    ∇_L̲ L̲ = 2 (L̲ ln Ω) L̲,      ∇_(∂_v) ∂_v = 2 (∂_v ln Ω) ∂_v,
    ∇_L̲ ∂_v = (2Ω²/γ_ϑ)(η − ζ) ∂_ϑ,      ∇_(∂_v) L̲ = (2Ω²/γ_ϑ)(η + ζ) ∂_ϑ,
    ∇_L̲ ∂_ϑ = (η − ζ) L̲ + (L̲ϰ_1) ∂_ϑ,      ∇_(∂_ϑ) L̲ = (η − ζ) L̲ + χ̲_1 ∂_ϑ,
    ∇_(∂_v) ∂_ϑ = ∇_(∂_ϑ) ∂_v = (η + ζ) ∂_v + χ_1 ∂_ϑ,
    ∇_(∂_ϑ) ∂_ϑ = (γ_ϑ/(2Ω²))(χ_1 L̲ + χ̲_1 ∂_v) + (∂_ϑϰ_1) ∂_ϑ,
    ∇_X K_i = ∇_(K_i) X = (Xϰ_(i+1)) K_i  (X = L̲, ∂_v, ∂_ϑ),      ∇_(K_1) K_2 = ∇_(K_2) K_1 = 0,
    ∇_(K_i) K_i = e^(2ϰ_(i+1)) ((2Ω²)⁻¹ (χ_(i+1) L̲ + χ̲_(i+1) ∂_v) − γ_ϑ⁻¹ (∂_ϑϰ_(i+1)) ∂_ϑ),

where L̲ϰ_(i+1) = χ̲_(i+1) and ∂_vϰ_(i+1) = χ_(i+1).

*Proof.* Each entry is Koszul's formula 2g(∇_X Y, Z) = X g(Y, Z) + Y g(Z, X) − Z g(X, Y) + g([X, Y], Z) − g([Y, Z], X) +
g([Z, X], Y), with X, Y, Z in the frame, the products and brackets above, and the fact that the products depend on (u, v,
ϑ) only. For instance 2g(∇_L̲ L̲, ∂_v) = 2L̲ g(L̲, ∂_v) + 2g([∂_v, L̲], L̲) = −4L̲Ω², while g(∇_L̲ L̲, Z) = 0 for Z = L̲,
∂_ϑ, K_i, which gives the first entry; and 2g(∇_L̲ ∂_v, ∂_ϑ) = L̲ g(∂_v, ∂_ϑ) + ∂_v g(∂_ϑ, L̲) − ∂_ϑ g(L̲, ∂_v) + g([L̲,
∂_v], ∂_ϑ) − g([∂_v, ∂_ϑ], L̲) + g([∂_ϑ, L̲], ∂_v) = 4Ω²η − γ_ϑ ∂_v b, while 2g(∇_L̲ ∂_v, Z) = 0 for the other frame
fields, which gives the third. The others follow in the same way. The derivatives of the frame have no K_i-component
unless the K_i enters, because the reflection φ_i ↦ −φ_i is an isometry that fixes L̲, ∂_v, ∂_ϑ and reverses K_i. As a
check, ∇_(∂_v) L̲ − ∇_L̲ ∂_v = (4Ω²ζ/γ_ϑ) ∂_ϑ = (∂_v b) ∂_ϑ and ∇_(∂_ϑ) L̲ − ∇_L̲ ∂_ϑ = (χ̲_1 − L̲ϰ_1) ∂_ϑ = (∂_ϑ b) ∂_ϑ,
the brackets. ∎

**Lemma {#lem:loc-cone-ricci}** (The equations.) Off the axes let g have the form [[eq:loc-double-null]], let q_in and
q_out be functions, T := q_in dv ⊗ dv + q_out du ⊗ du, E := Ric(g) − T, ρ_in := 𝒱q_in and ρ_out := 𝒱q_out.

(a) The frame components of E are E(K_1, K_2) = E(K_i, X) = 0 for X = L̲, ∂_v, ∂_ϑ, the components E(∂_v, ∂_v) =
Ric(∂_v, ∂_v) − q_in and E(∂_v, ∂_ϑ) = Ric(∂_v, ∂_ϑ) of [[eq:loc-cone]], and, with □_g the wave operator of g,

    E(K_i, K_i) = −e^(2ϰ_(i+1)) □_g ϰ_(i+1),
    □_g f = −Ω⁻² (∂_v L̲f + ½ (tr χ̲ ∂_v f + tr χ L̲f − ∂_v b ∂_ϑ f)) + (Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 γ_ϑ⁻¹ ∂_ϑ f),
    E(∂_ϑ, ∂_ϑ) = (γ_ϑ/Ω²) (∂_v χ̲_1 + ½ (tr χ χ̲_1 + χ_1 tr χ̲) − ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b)) − (γ_ϑ²/(8Ω⁴)) (∂_v b)²
                 − Σ_(i=2,3) (∂_ϑ²ϰ_i + (∂_ϑϰ_i)² − ∂_ϑϰ_1 ∂_ϑϰ_i) − 2 (∂_ϑη + η² − ∂_ϑϰ_1 η),
    E(L̲, ∂_v) = −2 ∂_v L̲ ln Ω − ∂_v tr χ̲ − Σ_i χ_i χ̲_i + (2Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 ∂_v b) − (γ_ϑ/(4Ω²)) (∂_v b)²
                 + 𝒱⁻¹ ∂_ϑ(𝒱 γ_ϑ⁻¹ ∂_ϑ Ω²),
    E(L̲, ∂_ϑ) = −(γ_ϑ/(4Ω²)) (L̲∂_v b + (L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) + 2∂_ϑ b) ∂_v b) + r̲,
    r̲ := (η + ∂_ϑϰ_2 + ∂_ϑϰ_3) χ̲_1 + (χ̲_2 + χ̲_3) η − ∂_ϑ L̲ ln Ω − Σ_(i=2,3) (∂_ϑϰ_i χ̲_i + ∂_ϑχ̲_i),
    E(L̲, L̲) = Σ_i (−L̲χ̲_i − χ̲_i² + 2 L̲ ln Ω χ̲_i) − q_out.                                {#eq:loc-cone-frame-ricci}

(b) √|det g| = 2Ω²𝒱, div_g(q_in g⁻¹dv) = −(2Ω²𝒱)⁻¹ (∂_u ρ_in + ∂_ϑ(b ρ_in)) and div_g(q_out g⁻¹du) =
−(2Ω²𝒱)⁻¹ ∂_v ρ_out; tr_g T = 0, and div_g T = div_g(q_in g⁻¹dv) dv + div_g(q_out g⁻¹du) du.

(c) Let E′ := (E(L̲, ∂_v), E(∂_ϑ, ∂_ϑ), E(L̲, ∂_ϑ), E(K_1, K_1), E(K_2, K_2)) and a := E(∂_v, ∂_v), β := E(∂_v, ∂_ϑ),
c := E(L̲, L̲). Then tr_g E = ℓ_0(E′) and

    (div_g E)(L̲) = −(2Ω²)⁻¹ (∂_v c + tr χ c) + ℓ_1(E′),
    (div_g E)(∂_ϑ) = −(2Ω²)⁻¹ (L̲β + (tr χ̲ + ∂_ϑ b) β) + ℓ_2(E′),
    (div_g E)(∂_v) = −(2Ω²)⁻¹ (L̲a + tr χ̲ a + ∂_v b β) + γ_ϑ⁻¹ (∂_ϑβ + ∂_ϑ(2 ln Ω + ϰ_2 + ϰ_3 − ϰ_1) β) + ℓ_3(E′),
                                                                                                  {#eq:loc-cone-bianchi}

with ℓ_0 linear and ℓ_1, ℓ_2, ℓ_3 linear differential operators of first order, all with coefficients that are smooth
functions of the metric functions and their first derivatives. Moreover div_g E = ½ d(tr_g E) − div_g T.

*Proof.* (a) The reflection φ_i ↦ −φ_i is an isometry that preserves T and reverses K_i, which gives the components with
one index K_i; T(K_i, ·) = T(L̲, ∂_v) = T(·, ∂_ϑ) = 0 because du and dv vanish on K_i and ∂_ϑ and dv(L̲) = du(∂_v) = 0,
while T(∂_v, ∂_v) = q_in and T(L̲, L̲) = q_out. By [[lem:warped-ricci]], E(K_1, K_1) = −e^(2A_c)(□_(g3) A_c + |dA_c|² +
⟨dA_c, dA_s⟩), with g3 the orbit metric, and □_g f = □_(g3) f + ⟨d(A_c + A_s), df⟩ for invariant f, since √|det g| =
√|det g3| e^(A_c + A_s); so E(K_1, K_1) = −e^(2A_c) □_g A_c, and likewise for K_2. With the inverse metric of the proof
of [[lem:loc-cone-equations]] and det g = −4Ω⁴γ_ϑ e^(2A_c + 2A_s), √|det g| g^(uv) = −𝒱, √|det g| g^(vϑ) = −b𝒱 and
√|det g| g^(ϑϑ) = 2Ω²𝒱/γ_ϑ, so 2Ω²𝒱 □_g f = −∂_u(𝒱∂_v f) − ∂_v(𝒱 ∂_u f + b𝒱 ∂_ϑ f) + ∂_ϑ(−b𝒱 ∂_v f + 2Ω²𝒱γ_ϑ⁻¹
∂_ϑ f); expanding, with ∂_v L̲f = ∂_u∂_v f + b∂_ϑ∂_v f + ∂_v b ∂_ϑ f, L̲ ln 𝒱 + ∂_ϑ b = tr χ̲ and ∂_v ln 𝒱 = tr χ, gives
the formula for □_g.

The components E(∂_v, ∂_v) and E(∂_v, ∂_ϑ) are [[lem:loc-cone-equations]]. For E(L̲, L̲) and E(L̲, ∂_ϑ), near a point
let ϑ̃ solve L̲ϑ̃ = 0 with ∂_ϑϑ̃ > 0, and use the coordinates (u, v, ϑ̃, φ1, φ2). In them ∂_u = L̲; with J := ∂ϑ/∂ϑ̃ and
w := ∂ϑ/∂v at fixed (u, ϑ̃), ∂_(ϑ̃) = J∂_ϑ and the new ∂_v is ∂_v + w∂_ϑ, so

    g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ J² (dϑ̃ − b̃ dv)² + e^(2A_c) dφ1² + e^(2A_s) dφ2²,      b̃ := −w/J,

which is [[eq:loc-double-null]] with u and v exchanged and (γ_ϑJ², b̃) in place of (γ_ϑ, b). [[lem:loc-cone-equations]]
applies to it, with the hypersurfaces {v = const} ruled by ∂_u = L̲. Since L̲ = ∂_u at fixed (v, ϑ̃) and L̲ϑ = b,
L̲J = ∂_(ϑ̃)b = J∂_ϑ b and L̲w = ∂_v b + w∂_ϑ b (the new ∂_v applied to b), so L̲(½ ln(γ_ϑJ²)) = χ̲_1 and L̲b̃ =
−J⁻¹ ∂_v b; and L̲(J∂_ϑ f) = J∂_ϑ L̲f, as [L̲, ∂_ϑ] = −(∂_ϑ b) ∂_ϑ. Substituting these in the two lines of
[[eq:loc-cone]] gives Ric(L̲, L̲) as stated and Ric(L̲, ∂_(ϑ̃)) = J Ric(L̲, ∂_ϑ) with Ric(L̲, ∂_ϑ) as stated: the
first term of the second line becomes (γ_ϑJ²/(4Ω²))(L̲(−J⁻¹∂_v b) + L̲ ln(γ_ϑ^(3/2)J³e^(A_c + A_s)Ω⁻²)(−J⁻¹∂_v b)),
and L̲ ln J = ∂_ϑ b; the term r of [[eq:loc-cone-r]] becomes J r̲.

For E(∂_ϑ, ∂_ϑ) and E(L̲, ∂_v) we use R(X, Y)Z := ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_([X,Y]) Z and

    Ric(Y, Z) = −(2Ω²)⁻¹ (g(R(L̲, Y)Z, ∂_v) + g(R(∂_v, Y)Z, L̲)) + γ_ϑ⁻¹ g(R(∂_ϑ, Y)Z, ∂_ϑ)
                + Σ_i e^(−2ϰ_(i+1)) g(R(K_i, Y)Z, K_i),

the trace in the frame. Lemma [[lem:loc-cone-frame]] gives, by a direct calculation,

    e^(−2ϰ_(i+1)) g(R(K_i, ∂_ϑ)∂_ϑ, K_i) = −(∂_ϑ²ϰ_(i+1) + (∂_ϑϰ_(i+1))² − ∂_ϑϰ_1 ∂_ϑϰ_(i+1)) + (γ_ϑ/(2Ω²))(χ_1χ̲_(i+1)
                                         + χ̲_1χ_(i+1)),
    g(R(L̲, ∂_ϑ)∂_ϑ, ∂_v) + g(R(∂_v, ∂_ϑ)∂_ϑ, L̲) = 4Ω² (∂_ϑη + η² − ∂_ϑϰ_1 η) + (γ_ϑ²/(4Ω²)) (∂_v b)²
                                         − 2γ_ϑ (∂_v χ̲_1 + χ_1 χ̲_1 − ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b)),

and R(∂_ϑ, ∂_ϑ) = 0; summing gives E(∂_ϑ, ∂_ϑ), since χ_1χ̲_1 + ½ Σ_(i=2,3) (χ_1χ̲_i + χ̲_1χ_i) = ½(tr χ χ̲_1 + χ_1 tr
χ̲). Likewise R(L̲, L̲) = 0 and

    g(R(∂_v, L̲)∂_v, L̲) = 4Ω² ∂_v L̲ ln Ω − 4Ω⁴γ_ϑ⁻¹ η² − 2Ω² η ∂_v b + ¾ γ_ϑ (∂_v b)²,
    γ_ϑ⁻¹ g(R(∂_ϑ, L̲)∂_v, ∂_ϑ) = −(∂_v χ̲_1 + χ_1 χ̲_1) + ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b) + (γ_ϑ/(8Ω²)) (∂_v b)²
                                + 2Ω²γ_ϑ⁻¹ (∂_ϑη + η² − ∂_ϑϰ_1 η),
    e^(−2ϰ_(i+1)) g(R(K_i, L̲)∂_v, K_i) = −(∂_v χ̲_(i+1) + χ_(i+1) χ̲_(i+1)) + 2Ω²γ_ϑ⁻¹ η ∂_ϑϰ_(i+1)
                                         + ½ ∂_ϑϰ_(i+1) ∂_v b;

summing gives E(L̲, ∂_v), since 2Ω²γ_ϑ⁻¹(∂_ϑη + 2η² + η ∂_ϑ(ϰ_2 + ϰ_3 − ϰ_1)) = 𝒱⁻¹∂_ϑ(𝒱γ_ϑ⁻¹∂_ϑΩ²) and
½ ∂_ϑ∂_v b + ½ ∂_v b ∂_ϑ ln 𝒱 + η ∂_v b = (2Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 ∂_v b).

(b) The determinant is that of the proof of [[lem:loc-cone-equations]]. div(q P) = |det g|^(−1/2) ∂_μ(|det g|^(1/2) q
P^μ) with P = g⁻¹dv, P^u = g^(uv), P^ϑ = g^(ϑv), and with P = g⁻¹du = g^(uv) ∂_v. tr_g T = q_in g^(vv) + q_out
g^(uu) = 0. By [[prop:class-augmented]] (c), div_g T is the stated sum plus q_in ∇_(g⁻¹dv) dv + q_out ∇_(g⁻¹du) du, and
∇_(g⁻¹dv) dv = ½ d(g⁻¹(dv, dv)) = 0, likewise for du.

(c) In the frame, g⁻¹ = −(2Ω²)⁻¹ (L̲ ⊗ ∂_v + ∂_v ⊗ L̲) + γ_ϑ⁻¹ ∂_ϑ ⊗ ∂_ϑ + Σ_i e^(−2ϰ_(i+1)) K_i ⊗ K_i, so tr_g E = −Ω⁻²
E(L̲, ∂_v) + γ_ϑ⁻¹ E(∂_ϑ, ∂_ϑ) + Σ_i e^(−2ϰ_(i+1)) E(K_i, K_i) is linear in E′, and (div_g E)(Y) = −(2Ω²)⁻¹ ((∇_L̲
E)(∂_v, Y) + (∇_(∂_v) E)(L̲, Y)) + γ_ϑ⁻¹ (∇_(∂_ϑ) E)(∂_ϑ, Y) + Σ_i e^(−2ϰ_(i+1)) (∇_(K_i) E)(K_i, Y), with (∇_X E)(Z,
Y) = X(E(Z, Y)) − E(∇_X Z, Y) − E(Z, ∇_X Y). The terms in E′ and its first derivatives make up the ℓ_j. The rest has only
a, β, c, and the table of [[lem:loc-cone-frame]] gives, for Y = L̲: (∇_(∂_v) E)(L̲, L̲) = ∂_v c − 2E(∇_(∂_v) L̲, L̲) =
∂_v c, (∇_L̲ E)(∂_v, L̲) = 0, (∇_(∂_ϑ) E)(∂_ϑ, L̲) = −(γ_ϑ/(2Ω²)) χ_1 c and (∇_(K_i) E)(K_i, L̲) = −(e^(2ϰ_(i+1))/(2Ω²))
χ_(i+1) c; for Y = ∂_ϑ: (∇_L̲ E)(∂_v, ∂_ϑ) = L̲β − (L̲ϰ_1) β, (∇_(∂_v) E)(L̲, ∂_ϑ) = 0, (∇_(∂_ϑ) E)(∂_ϑ, ∂_ϑ) = −(γ_ϑ/Ω²)
χ̲_1 β and (∇_(K_i) E)(K_i, ∂_ϑ) = −(e^(2ϰ_(i+1))/(2Ω²)) χ̲_(i+1) β, and 2χ̲_1 − L̲ϰ_1 = χ̲_1 + ∂_ϑ b; for Y = ∂_v: (∇_L̲
E)(∂_v, ∂_v) = L̲a − (4Ω²/γ_ϑ)(η − ζ) β, (∇_(∂_v) E)(L̲, ∂_v) = −(2Ω²/γ_ϑ)(η + ζ) β, (∇_(∂_ϑ) E)(∂_ϑ, ∂_v) = ∂_ϑβ −
(γ_ϑ/(2Ω²)) χ̲_1 a − (∂_ϑϰ_1 + η + ζ) β and (∇_(K_i) E)(K_i, ∂_v) = −(e^(2ϰ_(i+1))/(2Ω²)) χ̲_(i+1) a + e^(2ϰ_(i+1))γ_ϑ⁻¹
∂_ϑϰ_(i+1) β, and 2γ_ϑ⁻¹ζ = (2Ω²)⁻¹ ∂_v b. Summing gives [[eq:loc-cone-bianchi]]. The last identity is the contracted
Bianchi identity div Ric = ½ d(tr_g Ric), with tr_g Ric = tr_g E + tr_g T = tr_g E. ∎

#### The formal solution {#sec:loc-cone-formal}

**Lemma {#lem:loc-cone-borel}** (Extension of derivatives given on two edges.) Let λ_u, λ_v > 0, Y ⊂ ℝ a closed interval,
a_j (j ≥ 0) smooth functions of (v, ϑ) on [0, λ_v] × Y and b_k (k ≥ 0) smooth functions of (u, ϑ) on [0, λ_u] × Y, with
∂_v^k a_j(0, ϑ) = ∂_u^j b_k(0, ϑ) =: c_(jk)(ϑ) for all j, k. Let r ≥ 0 be an integer and γ_0, ε_0 ∈ (0, 1]. There is a
smooth function f on (−∞, λ_u] × (−∞, λ_v] × Y with ∂_u^j f(0, v, ϑ) = a_j(v, ϑ) for 0 ≤ v ≤ λ_v and ∂_v^k f(u, 0, ϑ) =
b_k(u, ϑ) for 0 ≤ u ≤ λ_u, for all j and k, such that:

(a) f vanishes outside {|u| ≤ 2ε_0, v ≥ −2ε_0} ∪ {|v| ≤ 2ε_0, u ≥ 0}, and at every ϑ at which all a_j and b_k vanish
identically; if all a_j vanish for v < v_K and all b_k for u < u_K, where u_K, v_K > 0, then f = 0 where u < u_K and
v < v_K;

(b) with C^r norms over the sets named, ‖f‖_(C^r) ≤ C (max_(j≤r) ‖a_j‖_(C^(2r)) + max_(k≤r) ‖b_k‖_(C^(2r))) + γ_0, C
depending only on r and ε_0.

*Proof.* Fix χ ∈ C^∞(ℝ) with 0 ≤ χ ≤ 1, χ = 1 on [−1, 1] and supp χ ⊂ (−2, 2). For 0 < ε ≤ 1 and integers i, j ≥
0, |∂_x^i(χ(x/ε) x^j)| ≤ C(i, j) ε^(j−i) when i ≤ j, since the derivatives of χ(x/ε) are ε^(−l) χ^(l)(x/ε) and vanish
for |x| ≥ 2ε. So for a smooth function h(z) of further variables z, the term χ(x/ε) x^j h(z)/j! has C^(j−1) norm at most
C(j) ε ‖h‖_(C^(j−1)) and C^r norm at most C(r, j) ‖h‖_(C^r). Given smooth h_j, choose ε_j := ε_0 for j ≤ r and, for j >
r, ε_j ≤ ε_0 so small that the C^(j−1) norm of the j-th term is at most 2^(−j) γ_0. Then the series Σ_j χ(x/ε_j) x^j
h_j(z)/j! converges in every C^p, its terms of index above p + 1 having C^p norms at most 2^(−j) γ_0; its sum B is
smooth, may be differentiated termwise, and ∂_x^j B(0, z) = h_j(z), as χ = 1 near 0. Call B the Borel sum of (h_j).

*Step 1.* For each j let ã_j := a_j on [0, λ_v] × Y and, for v < 0, ã_j := the Borel sum in v of (c_(jk))_k. All
one-sided v-derivatives of the two pieces at v = 0 are the c_(jk), so ã_j is smooth on (−∞, λ_v] × Y. *Step 2.* Let f_1
be the Borel sum in u of (ã_j)_j; then ∂_u^j f_1(0, v, ϑ) = ã_j(v, ϑ). *Step 3.* Termwise, ∂_v^k f_1(u, 0, ϑ) = Σ_j
χ(u/ε_j) u^j c_(jk)(ϑ)/j!, whose u-derivatives at u = 0 are the c_(jk). So d_k := b_k − ∂_v^k f_1(·, 0, ·) on [0, λ_u] ×
Y has all its u-derivatives zero at u = 0, and extended by 0 to u < 0 it is smooth. Let f := f_1 + the Borel sum in v of
(d_k)_k. Its u-derivatives at u = 0 are those of f_1, since every d_k vanishes for u ≤ 0, and ∂_v^k f(u, 0, ϑ) = ∂_v^k
f_1(u, 0, ϑ) + d_k(u, ϑ) = b_k(u, ϑ).

(a) f_1 vanishes for |u| ≥ 2ε_0 and, ã_j vanishing for v ≤ −2ε_0, for v ≤ −2ε_0; the second sum vanishes for |v| ≥ 2ε_0
and for u < 0. The cut-offs depend on u and v only. If all a_j vanish for v < v_K, then all c_(jk) = 0, so ã_j = 0 for
v < v_K and f_1 = 0 there; and d_k = b_k vanishes for u < u_K.

(b) The terms of index at most r have the cut-off scale ε_0 and C^r norms at most C(r, ε_0) times the C^r norms of ã_j,
respectively d_k; ‖ã_j‖_(C^r) ≤ ‖a_j‖_(C^r) + C max_(k≤r) ‖c_(jk)‖_(C^r) + (the sum of the terms of index above r),
‖d_k‖_(C^r) ≤ ‖b_k‖_(C^r) + C max_(j≤r) ‖c_(jk)‖_(C^r) + (the like), and ‖c_(jk)‖_(C^r) ≤ ‖a_j‖_(C^(r+k)) ≤
‖a_j‖_(C^(2r)) for k ≤ r. Choosing every ε of index above r also so small that the C^r norms of the terms it multiplies
sum, over all three sums, to at most γ_0/2 in total, (b) follows. ∎

In the rest of the section a background on 𝒮 and cone data are fixed, X denotes the list of functions
(ln Ω, ϰ_1, ϰ_2, ϰ_3, b, ρ_in, ρ_out) of (u, v, ϑ), and X̊ the background's. On N_o let a_0 be the cone data, with
ρ_in := 𝒱q_in and with ρ_out equal on each generator to the value of 𝒱q_out at the corner; on N_i let b_0 be the cone
data, with ρ_out := 𝒱q_out and with ρ_in the solution of ∂_u ρ_in + ∂_ϑ(b ρ_in) = 0 along N_i equal to 𝒱q_in at the
corner (in the normalised gauge, ρ_in is constant along each generator). Then a_0 = b_0 on S_c. On N_i the integral
curves of L̲ = ∂_u + b∂_ϑ, the generators of N_i, start on S_c and cover N_i: b vanishes outside the band, so dϑ/du = b
keeps them in [0, π/2].

**Lemma {#lem:loc-cone-jets}** (The derivatives across the edges.) There are unique sequences of functions a_j (j ≥ 0)
on [0, l_v + δ_1] × [0, π/2] and b_k (k ≥ 0) on [0, l_u + δ_1] × [0, π/2], with values in ℝ⁷ and with a_0, b_0 as above,
such that a_j − å_j and b_k − b̊_k are smooth (å_j, b̊_k the derivatives of X̊) and, for every smooth X on a
neighbourhood of N in 𝒮 × [0, π/2] equal to X̊ near the axes and with ∂_u^j X(0, v, ϑ) = a_j(v, ϑ) and ∂_v^k X(u, 0, ϑ) =
b_k(u, ϑ) for all j and k, the metric g of the form [[eq:loc-double-null]] with the functions X and the densities
q_A := ρ_A/𝒱 satisfy: E′ of [[lem:loc-cone-ricci]] (c), ∂_u ρ_in + ∂_ϑ(b ρ_in) and ∂_v ρ_out vanish to infinite order
on N. Moreover:

(i) ∂_v^k a_j(0, ϑ) = ∂_u^j b_k(0, ϑ) for all j and k;

(ii) if the cone data equal the background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], so do all a_j and b_k; if they equal
the background's on N_o ∩ {v < v_K} and on N_i ∩ {u < u_K}, with u_K, v_K > 0, then a_j = å_j for v < v_K and b_k = b̊_k
for u < u_K;

(iii) if the size of the cone data is at most Λ, then ‖a_j − å_j‖_(C^(m_0−4j)) + ‖b_j − b̊_j‖_(C^(m_0−4j)) is at most C_j
times the size, for 4j ≤ m_0, C_j depending only on j, Λ and the background;

(iv) every class solution in the gauge on D × S³, D ⊂ F containing a neighbourhood of N in F, smooth up to N, whose
functions on N_o and N_i are the cone data, has ∂_u^j X = a_j on N_o and ∂_v^k X = b_k on N_i; in particular å_j and
b̊_k are the derivatives of X̊ across N.

No smallness enters, and a_j, b_k depend on the cone data only on N_o ∩ {v′ ≤ v} and N_i ∩ {u′ ≤ u} respectively.

*Proof.* *The equations solved for the mixed derivatives.* In [[eq:loc-cone-frame-ricci]] the second derivatives of
ln Ω and of the ϰ_i other than ∂_ϑ² enter only through ∂_v L̲ ln Ω and the ∂_v χ̲_i, with ∂_v χ̲_1 = ∂_v L̲ϰ_1 +
∂_v∂_ϑ b and ∂_v χ̲_i = ∂_v L̲ϰ_i (i = 2, 3), and the second derivatives of b other than ∂_ϑ² b and ∂_v∂_ϑ b only
through L̲∂_v b in E(L̲, ∂_ϑ). The equations E(∂_ϑ, ∂_ϑ) = E(K_1, K_1) = E(K_2, K_2) = 0 contain ∂_v L̲ϰ_1, ∂_v L̲ϰ_2,
∂_v L̲ϰ_3 with the factors γ_ϑ/Ω², Ω⁻² and Ω⁻², E(L̲, ∂_v) = 0 contains −2∂_v L̲ ln Ω − Σ_i ∂_v L̲ϰ_i, and
E(L̲, ∂_ϑ) = 0 contains −(γ_ϑ/(4Ω²)) L̲∂_v b. Solving the first three for ∂_v L̲ϰ_i and then the fourth for
∂_v L̲ ln Ω, the five equations E′ = 0 are equivalent, off the axes, to

    ∂_v(L̲ Y_l) = Ψ_l  (l = 0, 1, 2, 3),      L̲(∂_v b) = Ψ_4,      (Y_0, …, Y_3) := (ln Ω, ϰ_1, ϰ_2, ϰ_3),
                                                                                                  {#eq:loc-cone-goursat}

where each Ψ_l is a polynomial in e^(±2 ln Ω), e^(±2ϰ_1), e^(±2ϰ_2), e^(±2ϰ_3), b and derivatives of ln Ω, the ϰ_i and
b of the kinds below, read off from [[eq:loc-cone-frame-ricci]]:

(Ψ1) the derivatives of ln Ω and the ϰ_i in the Ψ_l are of the forms ∂_ϑ^p, ∂_v, L̲ and ∂_ϑ L̲ (p ≤ 2), those of b of
the forms ∂_ϑ^p, ∂_v and ∂_ϑ∂_v (p ≤ 2); there is no ∂_u b;
(Ψ2) each monomial of Ψ_0, …, Ψ_3 contains at most one factor among L̲ ln Ω, the L̲ϰ_i and the ∂_ϑL̲ of these (in fact
no ∂_ϑ L̲), and at most one among ∂_v ln Ω and the ∂_vϰ_i, besides factors ∂_v b and ∂_ϑ∂_v b;
(Ψ3) Ψ_4 contains no ∂_v of ln Ω or the ϰ_i and no ∂_ϑ∂_v b, and each of its monomials contains at most one factor among
L̲ ln Ω, the L̲ϰ_i, ∂_ϑ L̲ ln Ω, ∂_ϑ L̲ϰ_2, ∂_ϑ L̲ϰ_3, and at most one factor ∂_v b.

For instance □_g ϰ_2 = 0 reads ∂_v L̲ϰ_2 = −½(tr χ̲ ∂_vϰ_2 + tr χ χ̲_2 − ∂_v b ∂_ϑϰ_2) + 𝒱⁻¹Ω⁻²∂_ϑ(Ω²𝒱γ_ϑ⁻¹∂_ϑϰ_2), and
E(L̲, ∂_ϑ) = 0 reads L̲∂_v b = −(L̲ ln(γ_ϑ^(3/2)e^(A_c+A_s)Ω⁻²) + 2∂_ϑ b) ∂_v b + 4Ω²γ_ϑ⁻¹ r̲. With L̲ = ∂_u + b∂_ϑ,
[[eq:loc-cone-goursat]] is also ∂_u∂_v Y_l = Ψ_l − ∂_v(b ∂_ϑ Y_l) and ∂_u∂_v b = Ψ_4 − b ∂_ϑ∂_v b: every right side holds
at most first derivatives in u and in v of each factor. The conservation laws are ∂_u ρ_in = −∂_ϑ(b ρ_in) and
∂_v ρ_out = 0.

*N_o.* Let j ≥ 1 and a_0, …, a_(j−1) be found. Apply ∂_u^(j−1) to [[eq:loc-cone-goursat]] and set u = 0, replacing
∂_u^i X by a_i. As L̲X = ∂_u X + b ∂_ϑ X, ∂_u^(j−1) ∂_v L̲Y_l = ∂_v ∂_u^j Y_l + ∂_v ∂_u^(j−1)(b ∂_ϑ Y_l), whose second
part holds u-derivatives of order at most j − 1; likewise ∂_u^(j−1) L̲∂_v b = ∂_v ∂_u^j b + ∂_u^(j−1)(b ∂_ϑ∂_v b). By
(Ψ1)–(Ψ3) the u-derivatives of order j enter the right sides only through ∂_u^(j−1) of L̲ Y_l and of ∂_ϑ L̲ Y_l, once in
each monomial, so

    ∂_v a_j^(ϰ_i) = Σ_l M_(il) a_j^(ϰ_l) + h_i,   ∂_v a_j^(ln Ω) = Σ_l M_(0l) a_j^(ϰ_l) + h_0,
    ∂_v a_j^b = M_4 · (a_j^(ln Ω), a_j^(ϰ_l), ∂_ϑ a_j^(ln Ω), ∂_ϑ a_j^(ϰ_2), ∂_ϑ a_j^(ϰ_3)) + h_4,

after substituting the first lines in the second; the coefficients M are smooth functions of a_0 and of its first
derivatives in v and ϑ, and the h are polynomials in a_0, …, a_(j−1) and their derivatives in v and ϑ of order at most
two. This is a system of linear ordinary differential equations in v along each generator, which we solve with the
initial values a_j(0, ϑ) := ∂_u^j b_0(0, ϑ) for the components ln Ω, ϰ_l, b: first the three ϰ-components, then ln Ω,
then b. For the densities put a_j^(ρ_in) := −(∂_u^(j−1)∂_ϑ(b ρ_in)) at u = 0, a polynomial in a_0, …, a_(j−1) and
their ϑ-derivatives, and a_j^(ρ_out)(v, ϑ) := ∂_u^j b_0^(ρ_out)(0, ϑ) for all v.

*N_i.* Let k ≥ 1 and b_0, …, b_(k−1) be found. Apply ∂_v^(k−1) to [[eq:loc-cone-goursat]] and set v = 0. Since ∂_v^k
(L̲ Y_l) = L̲ ∂_v^k Y_l + Σ_(1≤i≤k) (k choose i) ∂_v^i b ∂_ϑ∂_v^(k−i) Y_l and ∂_v^(k−1)(L̲ ∂_v b) = L̲ ∂_v^k b +
Σ_(1≤i≤k−1) (k−1 choose i) ∂_v^i b ∂_ϑ∂_v^(k−i) b, the left sides are L̲ applied to the unknowns of order k, plus terms
with v-derivatives of order at most k − 1 and the term ∂_v^k b ∂_ϑ Y_l. By (Ψ3), the right side for b holds v-derivatives
of order k only through ∂_v^k b, once in each monomial: a linear equation L̲ b_k^b = M_4′ b_k^b + h_4′ along the
generators of N_i. By (Ψ2), the other right sides hold them through ∂_v^k(ln Ω, ϰ_l), once in each monomial, and
through ∂_v^k b and ∂_ϑ∂_v^k b. So, with b_k^b known, these are linear equations along the generators for the
ϰ-components and then for ln Ω. We solve them with the initial values b_k(0, ϑ) := ∂_v^k a_0(0, ϑ). For the densities
put b_k^(ρ_out) := 0, and let b_k^(ρ_in) solve L̲ b_k^(ρ_in) = −(∂_ϑ b) b_k^(ρ_in) − ∂_ϑ Σ_(1≤i≤k) (k choose i)
b_i^b b_(k−i)^(ρ_in), the derivative ∂_v^k of the conservation law, with the initial value ∂_v^k a_0^(ρ_in)(0, ϑ).

*Vanishing to infinite order.* For X as in the statement, ∂_u^(j−1) of the differences of the two sides of
[[eq:loc-cone-goursat]] vanishes at u = 0 for every j ≥ 1, by the construction on N_o, and ∂_v^(k−1) of them vanishes at
v = 0 for every k ≥ 1; the derivatives along N of these restrictions vanish too. So the differences vanish to infinite
order on N, and so does E′, which is obtained from them by multiplying with smooth functions and adding. The
conservation laws are the same: at order 0 on N_o, ∂_v ρ_out = 0 is the constancy of a_0^(ρ_out) along the generators,
and on N_i the conservation law for ρ_in is the equation that defines b_0^(ρ_in).

(i) For j = 0 or k = 0 the equality holds by the choice of the initial values and of a_0, b_0, which agree on S_c. For j,
k ≥ 1 we use induction on n := j + k. Let c^o_(jk) := ∂_v^k a_j(0, ·) and c^i_(jk) := ∂_u^j b_k(0, ·). For the components
Y_l, c^o_(jk) = ∂_v^(k−1) of the right side of the equation for ∂_v a_j at v = 0, which is the formal mixed derivative
∂_u^(j−1)∂_v^(k−1) of the right side of the form ∂_u∂_v Y_l = Ψ_l − ∂_v(b ∂_ϑ Y_l) (respectively ∂_u∂_v b = Ψ_4 − b
∂_ϑ∂_v b) at the corner, expanded by the chain rule into the numbers ∂_ϑ^p c^o_(j′k′); and c^i_(jk) = ∂_u^(j−1) of the
right side of the equation for ∂_u b_k at u = 0, written in the same form, which is the same expansion in the numbers
∂_ϑ^p c^i_(j′k′). These right sides hold at most first derivatives in u and in v of each factor, so only pairs with j′ +
k′ ≤ n − 1 occur, and these agree by induction. For ρ_in and j ≥ 1 both are ∂_u^(j−1)∂_v^k of −∂_ϑ(b ρ_in), expanded in
the same way with j′ ≤ j − 1, k′ ≤ k; for ρ_out both vanish when k ≥ 1.

(ii) The coefficients, the inhomogeneous terms and the initial values of all the equations at an angle ϑ are built from
the cone data and their derivatives at ϑ. Where the data equal the background's on a neighbourhood of ϑ, the
background's derivatives solve the same equations with the same initial values, by (iv) for the background, and by
uniqueness they are the solutions. Likewise on N_o ∩ {v < v_K}: the equations there use the data on N_o ∩ {v′ ≤ v} and
the derivatives of b_0 at u = 0, which are the background's since u_K > 0; and on N_i ∩ {u < u_K}.

(iii) For a linear system ∂_v Z = MZ + h in v with Z(0) = Z_0, ‖Z‖_(C^r) ≤ C(r, ‖M‖_(C^r))(‖Z_0‖_(C^r) + ‖h‖_(C^r)),
by differentiating in ϑ, the v-derivatives being given by the equation; and the difference Z − Z̊ from the background's
solution solves ∂_v(Z − Z̊) = M(Z − Z̊) + (M − M̊) Z̊ + h − h̊. Suppose the bound for all orders below j. On N_o the
inhomogeneous terms of the ϰ- and ln Ω-equations hold derivatives of order at most two of a_0, …, a_(j−1), so their
differences are bounded in C^(m_0−4j+2); M − M̊ is bounded in C^(m_0−1) and the initial values ∂_u^j(b_0 − b̊_0)(0, ·) in
C^(m_0−j), all by C times the size. So these components of a_j − å_j are bounded in C^(m_0−4j+2); the b-component, whose
equation holds ∂_ϑ a_j^(ln Ω) and ∂_ϑ a_j^(ϰ_l), in C^(m_0−4j+1), and the densities likewise. On N_i the equations are
transport equations along L̲, whose flow from u = 0 has derivatives of order r bounded in terms of the C^r norm of b on
N_i; the same bounds hold for them. The equation for b_k^b holds derivatives of order at most two along N_i of
b_0, …, b_(k−1) and the initial value ∂_v^k a_0^b(0, ·), so b_k^b − b̊_k^b is bounded in C^(m_0−4k+2); the other
equations hold ∂_ϑ b_k^b, so the other components are bounded in C^(m_0−4k+1).

(iv) Such a solution satisfies E = 0 and the conservation laws on D, hence, by continuity, their derivatives of every
order on N; so its derivatives across N solve the equations above with the same initial values. ∎

**Proposition {#prop:loc-cone-formal}** (The formal solution.) Let the cone data have size at most Λ, equal the
background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], on N_o ∩ {v < v_K} and on N_i ∩ {u < u_K}, where u_K, v_K ∈ (0, ∞],
and let 0 < δ_e ≤ δ_1/4. There are smooth functions Δ = (Δ_l) of (u, v, ϑ) on 𝒮 × [0, π/2] such that, with X̂ := X̊ + Δ,
the metric Ĝ of the form [[eq:loc-double-null]] with the functions X̂, and q̂_A := ρ̂_A/𝒱̂:

(a) Δ vanishes outside {ϑ_a′ ≤ ϑ ≤ ϑ_b′} ∩ ({|u| ≤ 2δ_e, v ≥ −2δ_e} ∪ {|v| ≤ 2δ_e, u ≥ 0}) and where u < u_K and
v < v_K, and ‖Δ‖_(C^(k+3)) ≤ C times the size, C depending only on Λ, δ_e, k and the background;

(b) the derivatives of X̂ across N are the a_j and b_k of [[lem:loc-cone-jets]]; so Ĝ and q̂_A induce the cone data on N,
and Ĝ is a smooth G-invariant Lorentzian metric on 𝒮 × S³, equal to g_e near the axes, for which u and v are null;

(c) E := Ric(Ĝ) − q̂_in dv ⊗ dv − q̂_out du ⊗ du, ∂_u ρ̂_in + ∂_ϑ(b̂ ρ̂_in) and ∂_v ρ̂_out vanish to infinite order on N.

*Proof.* Apply [[lem:loc-cone-borel]] to each component of (a_j − å_j) and (b_k − b̊_k), with Y = [0, π/2], λ_u = l_u +
δ_1, λ_v = l_v + δ_1, r := k + 3, ε_0 := δ_e and γ_0 the size (Δ := 0 if the size is 0); the compatibility at the corner
holds for the data and for the background by [[lem:loc-cone-jets]] (i). (a) follows from parts (a) and (b) there and
[[lem:loc-cone-jets]] (ii), (iii), since m_0 − 4(k + 3) = 2(k + 3). (b) The double-null form with Ω̂ > 0 and γ̂_ϑ > 0 is
Lorentzian, with g^(uu) = g^(vv) = 0. (c) E′ and the conservation laws vanish to infinite order on N by
[[lem:loc-cone-jets]]. On N_o, E(∂_v, ∂_v) = E(∂_v, ∂_ϑ) = 0, and on N_i, E(L̲, L̲) = 0, by (ii) of
[[def:loc-cone-data]], these components being expressions in the functions on the edges, L̲ being tangent to N_i. By
[[lem:loc-cone-ricci]] (b), div T̂ vanishes to infinite order on N, and by (c) there tr E does; so div E does, and by
[[eq:loc-cone-bianchi]] the three expressions on its right sides, without the terms ℓ_j(E′), vanish to infinite order on
N. With a := E(∂_v, ∂_v), β := E(∂_v, ∂_ϑ), c := E(L̲, L̲):

*On N_o.* We show by induction on j that ∂_u^i a = ∂_u^i β = 0 on N_o for i ≤ j and ∂_u^i c = 0 on N_o for i ≤ j − 1;
this holds for j = 0. Given it for j, apply ∂_u^j to the first identity: on N_o, ∂_v(∂_u^j c) + tr χ ∂_u^j c = 0, the
terms with lower u-derivatives of c vanishing; and ∂_u^j c = 0 at v = 0, since c = 0 on N_i and ∂_u is tangent to N_i. So
∂_u^j c = 0 on N_o. Applying ∂_u^j to the second identity, all terms other than ∂_u^(j+1) β hold ∂_u^i β with i ≤ j or
∂_u^j c, so ∂_u^(j+1) β = 0 on N_o; then the third gives ∂_u^(j+1) a = 0.

*On N_i.* We show by induction on k that ∂_v^i c = 0 on N_i for i ≤ k and ∂_v^i a = ∂_v^i β = 0 on N_i for i ≤ k − 1;
this holds for k = 0. Given it for k, apply ∂_v^k to the second identity: on N_i, ∂_v^k L̲β = L̲ ∂_v^k β plus terms with
∂_v^i β, i ≤ k − 1, so L̲(∂_v^k β) + (tr χ̲ + ∂_ϑ b) ∂_v^k β = 0 along the generators of N_i, and ∂_v^k β = 0 at u = 0,
as β = 0 on N_o; so ∂_v^k β = 0 on N_i. Then ∂_v^k of the third gives L̲(∂_v^k a) + tr χ̲ ∂_v^k a = 0 along the
generators, with ∂_v^k a = 0 at u = 0, so ∂_v^k a = 0. Finally ∂_v^k of the first gives ∂_v^(k+1) c = 0 on N_i.

So a, β and c, with all their derivatives, vanish on N, and E vanishes to infinite order on N. ∎

#### The reduced problem {#sec:loc-cone-reduced}

The cone data, of size at most Λ, now equal the background's at the points with ϑ ∉ [2η, π/2 − 2η], for a number
η ∈ (0, π/8]; for [[thm:loc-cone-development]], η is the number there, and [ϑ_a′, ϑ_b′] ⊂ (ϑ_a, ϑ_b) ⊂ [4η, π/2 − 4η].
Two cases are treated together: (I) small data, the size at most ε ≤ ε_0, and (II) data of any size Λ on a small
rectangle at the corner. In case (II) we truncate the edges, l_u = l_v := 2δ_1: by [[lem:loc-cone-jets]] the derivatives
across N near the corner do not depend on the data farther out.

*Constants, coordinates and regions.* Put C_* := sup_𝒮 e^(σ_e)/R_e (in case (I), C_* := C_0, which is at least
that by [[lem:loc-cone-strips]] (b)), c_+ := (min(δ_1, η/C_*)/4)²,
κ := δ_1/(4(l_u + l_v + 1)), and fix δ_c ∈ (0, √c_+/8]. On {u > −δ_c, v > −δ_c} put

    τ := ln((u + δ_c)(v + δ_c)),      y := ((v + δ_c)/(u + δ_c)) ω(ϑ, φ1, φ2),                     {#eq:loc-cone-time}

ω ∈ S³ ⊂ ℝ⁴ the point with angles (ϑ, φ1, φ2). (τ, y) is a G-equivariant chart onto ℝ × (ℝ⁴ ∖ {0}), in which class
metrics equal to the background's near the axes are smooth; dτ = du/(u + δ_c) + dv/(v + δ_c), and the coordinate
field ∂_τ = ½((u + δ_c)∂_u + (v + δ_c)∂_v) is future timelike for g_e and for the metrics C⁰-close to it. Let
τ_init := ln(δ_c²/4), τ_+ := ln c_+, Σ_init := {τ = τ_init} and

    𝒰 := {(u, v) : u, v > −δ_c, τ_init ≤ τ ≤ τ_+, u + κv ≤ l_u + δ_1/2, v + κu ≤ l_v + δ_1/2}.      {#eq:loc-cone-region}

On 𝒰, min(u + δ_c, v + δ_c) ≤ √c_+ ≤ δ_1/4 and u + δ_c ≥ δ_c²/(4(l_v + 2δ_1)), so 𝒰 is a compact subset of the interior
of 𝒮 inside the chart. Its boundary consists of Σ_init ∩ 𝒰, of a piece of {τ = τ_+} and of pieces of the two far cuts,
with conormals dτ, du + κdv and dv + κdu; g_e⁻¹ of each with itself is negative (g_e^(uv) = −e^(−2σ_e) is the only entry
of g_e⁻¹ pairing du, dv), uniformly on 𝒰, so these pieces are spacelike, with 𝒰 to their past, for g_e and for every
Lorentzian metric close enough to g_e in C⁰. On 𝒰, 2C_* e^(τ/2) ≤ 2C_*√c_+ ≤ η/2, and the corner sphere S_c, where τ = 2
ln δ_c, lies in 𝒰, with F ∩ 𝒰 ⊂ {τ ≥ 2 ln δ_c}.

In case (I) put δ_* := √c_+/2 and take δ_c so small also that δ_c(l_u + l_v + 1) ≤ c_+/2; then the set G_* of
[[eq:loc-cone-domain]] lies in F ∩ 𝒰, since there (u + δ_c)(v + δ_c) ≤ δ_*² + c_+/2 < c_+ and u + κv ≤ l_u + δ_1/4.
In case (II), for 0 < σ ≤ σ_1 := δ_c/8, put 𝒰_σ := 𝒰 ∩ {τ ≤ ln((δ_c + 2σ)²)}; then [0, σ]² ⊂ F ∩ 𝒰_σ ⊂ [0, 6σ]², and
(−2σ, 10σ)² ⊂ 𝒰. In case (I) put 𝒰_σ := 𝒰.

*Cut-offs.* Let χ_ϑ be smooth on [0, π/2], equal to 1 on [η, π/2 − η] and to 0 on [0, η/2] ∪ [π/2 − η/2, π/2]; χ_𝒰 a
smooth function of (u, v), equal to 1 on a neighbourhood 𝒰_1 of 𝒰 and supported in the chart and in the interior of 𝒮;
χ := χ_ϑ χ_𝒰. In case (I), θ is a smooth function of (u, v) equal to 1 on a neighbourhood of 𝒰 and supported in 𝒰_1; in
case (II), θ := θ_1(u/σ) θ_1(v/σ), with θ_1 smooth, 0 ≤ θ_1 ≤ 1, θ_1 = 1 on [−1, 9] and supp θ_1 ⊂ (−2, 10), so that
supp θ ⊂ 𝒰 and θ = 1 on F ∩ 𝒰_σ.

*The reference states.* Take Δ of [[prop:loc-cone-formal]] with δ_e := δ_c/8, so that Δ vanishes where (u + δ_c)(v + δ_c)
≤ (3δ_c/4)², in particular near Σ_init. Let Ů := (g_e, p̊_in, p̊_out, Θ̊_in, Θ̊_out, q̊_in, q̊_out) with p̊_in := −dv,
p̊_out := −du, P̊_A := g_e⁻¹p̊_A, Θ̊_A := div_(g_e) P̊_A and q̊_A of [[sec:loc-cone-setting]]; and Û := (Ĝ, −dv, −du,
Θ̂_A, q̂_A) with Ĝ of the form [[eq:loc-double-null]] with the functions X̊ + χ_𝒰Δ, Θ̂_A := div_Ĝ P̂_A, P̂_A := Ĝ⁻¹p̂_A,
and q̂_A := (ρ̊_A + χ_𝒰Δ_(ρ_A))/𝒱̂. The fields P̊_A, P̂_A are future directed: P̂_out = (2Ω̂²)⁻¹ ∂_v and P̂_in = (2Ω̂²)⁻¹
L̲. On {χ_𝒰 = 1}, Û is the formal solution of [[prop:loc-cone-formal]]. Put K := supp(χ_𝒰 Δ); it lies in {ϑ_a′ ≤ ϑ ≤
ϑ_b′}, outside {u < u_K, v < v_K}, and in {(u + δ_c)(v + δ_c) ≥ (3δ_c/4)²}, and Ĝ = g_e and Û = Ů outside K.

*The modified system.* Let 𝒜(U) = 0 denote the augmented system (Aug1)–(Aug4) of [[sec:class-augmented]] for the
unknowns U = (g, p_A, Θ_A, q_A), A ∈ {in, out}, with ζ_A := 1 and with the reduced Ricci tensor and the gauge vector
relative to Ĝ, D(g) := g^(ab)(Γ[g] − Γ[Ĝ])_(ab), in place of g̊; it is defined where g(K_i, K_i) > 0, in particular on
supp χ. In the first-order form of Step 9 of the proof of [[thm:class-stability-off-axes]], in the chart (τ, y), with the
variables 𝐔 := (g, g_τ, g_a, p_A, Θ_A, q_A) for (g, ∂_τ g, ∂_(y^a) g, …), it reads A^μ(x, 𝐔) ∂_μ𝐔 = F_0(x, 𝐔): the wave
block is ∂_τ g − g_τ = 0, a row with −g^(ττ) ∂_τ g_τ − 2g^(τa) ∂_a g_τ − g^(ab) ∂_a g_b, and g^(ab)(∂_τ g_b − ∂_b g_τ) =
0, so that A^0 = diag(1, −g^(ττ), g^(ab)) there and P_A^τ on the transports. The coefficients are smooth functions of x
and 𝐔 on the states with g Lorentzian, dτ and ∂_τ timelike and P_A^τ > 0, x entering through Ĝ and its derivatives
of order at most two ([[eq:gauge]] with Ĝ in place of g0).

In case (I) let 𝐔_c := 𝐔̊, in case (II) 𝐔_c := 𝐔̂ (the centre). Let c_0, r_0 > 0 be such that A^0(x, 𝐔_c + w) ≥ 2c_0 I
for x ∈ supp χ and |w| ≤ 2r_0, and ϒ smooth with ϒ(w) = w for |w| ≤ r_0 and |ϒ| ≤ 2r_0. Let A^μ_♭ be the first-order
form, in the same variables, of the linear operator −½ h^(ab) ∂_a∂_b on the wave block and of the transports P̄_A·∂,
where h⁻¹ := χ_♭ g_e⁻¹ + (1 − χ_♭)(−∂_τ ⊗ ∂_τ + Σ_a ∂_(y^a) ⊗ ∂_(y^a)) and P̄_A := χ_♭ P̊_A + (1 − χ_♭) ∂_τ, χ_♭ a smooth
function of (u, v) equal to 1 on supp χ_𝒰 and supported in the chart and in 𝒮; on supp χ_𝒰, A^μ_♭ = A^μ(x, 𝐔̊). For
Z := 𝐔 − 𝐔̊ put

    𝔄_χ(𝐔) := χ (A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) ∂_μ𝐔 − F_0(x, 𝐔_c + ϒ(𝐔 − 𝐔_c))) + (1 − χ) A^μ_♭ ∂_μ Z,
    F̃ := (1 − θ 1_F) 𝔄_χ(Û),                                                                    {#eq:loc-cone-modified}

1_F the indicator function of F. 𝔄_χ(𝐔) involves 𝐔̊ only where χ ≠ 0, so 𝔄_χ(𝐔) = F̃ is a system for Z on
[τ_init, τ_+] × ℝ⁴.

**Lemma {#lem:loc-cone-system}** (The modified system.) In case (I) let ε be small, in case (II) σ ≤ σ_1.

(a) 𝔄_χ(𝐔) = F̃ has the form A^μ_χ(x, Z) ∂_μ Z = Φ(x, Z) of [[eq:class-kato-system]] on [τ_init, τ_+] × ℝ⁴, with
A^μ_χ := χ A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) + (1 − χ) A^μ_♭ symmetric, A^0_χ ≥ c_1 I with c_1 > 0, and Φ a local forcing term in
the sense of [[rem:class-kato-local]]. The bounds of every order of the A^μ_χ and of Φ, and c_1, depend only on Λ, η, k,
δ_c and the background.

(b) Where χ = 1 and |𝐔 − 𝐔_c| ≤ r_0, 𝔄_χ(𝐔) = 𝒜(𝐔); at the points of 𝒰 where χ = 0, 𝔄_χ(𝐔) = A^μ(x, 𝐔̊) ∂_μ(𝐔 − 𝐔̊).

(c) The first and the third row of the wave block of 𝔄_χ(𝐔) = F̃ are ∂_τ g − g_τ = 0 and h_χ^(ab)(∂_τ g_b − ∂_b g_τ) = 0,
with h_χ^(ab) positive definite; so g_τ = ∂_τ g and g_a = ∂_a g hold on [τ_init, τ_+] × ℝ⁴ if they hold at τ_init.

(d) 𝔄_χ(Û) = F̃ on P; F̃ is smooth and supported in supp χ_𝒰.

(e) R_I := 𝔄_χ(Ů) − F̃ and R_II := 𝔄_χ(Û) − F̃ are smooth, supported in supp χ_𝒰, and sup_τ ‖R_I(τ)‖_(H^k) ≤ C ε in case
(I), sup_τ ‖R_II(τ)‖_(H^k) ≤ C σ in case (II), with C depending on Λ in case (II). On 𝒰, F̃ − 𝔄_χ(Ů) vanishes outside K.

*Proof.* (a) A^μ_χ is a convex combination of the matrices of two systems of the form of Step 9, both symmetric; A^0 of
the first is at least 2c_0 I on supp χ for all Z, by the choice of ϒ, and A^0_♭ = diag(1, −h^(ττ), h^(ab), P̄_A^τ) is
positive definite, with a lower bound c_♭ > 0 on bounded sets of x and equal to the identity far out; so c_1 :=
min(2c_0, c_♭) serves. Φ(x, Z) := χ (F_0(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) − A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) ∂_μ𝐔̊) + F̃(x) is smooth in
(x, Z), with every derivative bounded on bounded sets of Z, and Φ(x, 0) vanishes for x outside the compact set
supp χ_𝒰, by (d); so [[rem:class-kato-local]] applies. Its bounds involve Ĝ in C^(k+3), and ‖Δ‖_(C^(k+3)) ≤ C(Λ) by
[[prop:loc-cone-formal]] (a). (b) is read off, as A^μ_♭ = A^μ(x, 𝐔̊) on supp χ_𝒰. (c) Both systems have these two rows,
with the matrices g^(ab) of 𝐔_c + ϒ(𝐔 − 𝐔_c) and h^(ab), and F̃ has no component in them, since those of 𝔄_χ(Û) vanish
(𝐔̂ has ĝ_τ = ∂_τ ĝ, ĝ_a = ∂_a ĝ); so ∂_τ(g_a − ∂_a g) = ∂_a(g_τ − ∂_τ g) = 0.

(d) On P, θ 1_F = 0. F̃ = 𝔄_χ(Û) − θ 1_F 𝔄_χ(Û), and 𝔄_χ(Û) is smooth. On supp θ ⊂ {χ_𝒰 = 1}, 𝐔̂ − 𝐔̊ vanishes where χ_ϑ
≠ 1 (Δ vanishes for ϑ ∉ [2η, π/2 − 2η]), so the frozen part of 𝔄_χ(Û) vanishes there, and |𝐔̂ − 𝐔_c| ≤ r_0 (in case (I)
since ‖Δ‖_(C^(k+3)) ≤ Cε); so 𝔄_χ(Û) = χ 𝒜(Û) on supp θ. 𝒜(Û) vanishes to infinite order on N ∩ {χ_𝒰 = 1}: in (Aug1),
Ric^H_Ĝ(Ĝ) = Ric(Ĝ) since D(Ĝ) = 0, so its residual is E of [[prop:loc-cone-formal]] (c); (Aug2) holds exactly, ∇_(P̂_A)
p̂_A = ½ d Ĝ⁻¹(p̂_A, p̂_A) = 0 as u and v are null for Ĝ; in (Aug3), off the axes, [[eq:class-raychaudhuri]] for the
eikonals −v and −u of Ĝ gives P̂_A(Θ̂_A) − S_A(Û) = −E(P̂_A, P̂_A); and (Aug4) is the conservation law, P̂_A(q̂_A) + Θ̂_A
q̂_A = div_Ĝ(q̂_A P̂_A), which [[lem:loc-cone-ricci]] (b) expresses through the conservation expressions of
[[prop:loc-cone-formal]] (c). A smooth function that vanishes to infinite order on N, times 1_F, is smooth; so θ 1_F
𝔄_χ(Û) is smooth.

(e) R_I = 𝔄_χ(Ů) − 𝔄_χ(Û) + θ 1_F 𝔄_χ(Û). 𝔄_χ is a smooth function of (x, 𝐔, ∂𝐔), so the first difference is bounded
in C^k by C‖𝐔̂ − 𝐔̊‖_(C^(k+1)) ≤ C‖Δ‖_(C^(k+2)) ≤ Cε. On F ∩ supp θ, 𝔄_χ(Û) = χ(𝒜(Û) − 𝒜(Ů)) + χ𝒜(Ů); there 𝒜(Ů) has
only the residual of (Aug1), Ric^H_Ĝ(g_e) − Ric^H_(g_e)(g_e), Ů solving the background's system on F ∩ 𝒮 (with
[[eq:class-raychaudhuri]] for (Aug3)); so it is bounded in C^k by C‖Ĝ − g_e‖_(C^(k+2)) ≤ Cε, and as θ 1_F 𝔄_χ(Û) is
smooth its C^k norm is at most Cε. In case (II), R_II = θ 1_F χ 𝒜(Û). Let x ∈ F ∩ supp θ, with u ≤ v say, so that
u ≤ 10σ; all derivatives of 𝒜(Û) vanish at (0, v, ϑ) ∈ N_o, so by Taylor's formula in u each derivative of 𝒜(Û) of order
at most k − p is at most C(Λ) u^(p+1) ≤ C(Λ)(10σ)^(p+1) at x, C(Λ) bounding the derivatives of order k + 1 of 𝒜(Û),
hence those of order k + 3 of Ĝ. The derivatives of order p of θ are at most Cσ^(−p). By Leibniz's rule each derivative
of order at most k of R_II is at most C(Λ)σ, and R_II is supported in the bounded set (−2σ, 10σ)² × S³; the chart
(τ, y) has bounded derivatives there. Finally, on 𝒰 ∖ K: on P, F̃ − 𝔄_χ(Ů) = 𝔄_χ(Û) − 𝔄_χ(Ů) = 0; on F, it is
−θ 𝔄_χ(Ů), and 𝔄_χ(Ů) = 0 on a neighbourhood of each point of F ∩ 𝒰 ∖ K, where Ĝ = g_e and Ů solves its own system. ∎

**Lemma {#lem:loc-cone-energy}** (Energy on a region.) Let 𝒟 be a compact subset of the slab [τ_init, τ_+] × ℝ⁴ such that
every 𝒟_s := 𝒟 ∩ {τ ≤ s} is empty or a Lipschitz domain whose boundary is the union of 𝒟 ∩ {τ = s}, of a closed set
B_0 and of a set B_1 that is a finite union of smooth hypersurfaces, meeting one another and the slices transversally.
Let 𝐀^μ be C¹ symmetric matrices on 𝒟 with 𝐀^0 ≥ cI, c > 0, M a bounded matrix function and z ∈ C¹(𝒟) with
𝐀^μ ∂_μ z = Mz on 𝒟, z = 0 on B_0 and ν_μ 𝐀^μ ≥ 0 at the points of B_1, ν the outward conormal. Then z = 0 on 𝒟.

*Proof.* The field V^μ := ⟨𝐀^μ z, z⟩ is C¹ in the slab coordinates, with ∂_μ V^μ = ⟨(∂_μ 𝐀^μ) z, z⟩ + 2⟨Mz, z⟩ ≤ C|z|²,
by the symmetry of the 𝐀^μ. Let e(s) := ∫_(𝒟∩{τ=s}) ⟨𝐀^0 z, z⟩ dy. The divergence theorem on the Lipschitz domain 𝒟_s,
as in the proof of [[thm:class-kato]] (b) (i), gives e(s) + ∫_(B_1∩{τ≤s}) ⟨ν_μ 𝐀^μ z, z⟩ |ν|⁻¹ dS = ∫_(𝒟_s) ∂_μ V^μ, the
integral over B_0 vanishing with z. The boundary integral over B_1 is nonnegative, so e(s) ≤ C ∫_(𝒟_s) |z|² ≤ (C/c)
∫_(τ_init)^s e, and e = 0 by Gronwall's inequality. ∎

For a system of the form of Step 9 with inverse metric h on its wave block and transport fields P, the matrix ν_μ 𝐀^μ is
nonnegative exactly when ν(∂_τ) ≥ 0, h⁻¹(ν, ν) ≤ 0 and ν(P) ≥ 0 for each transport field P (Step 9 of the proof of
[[thm:class-stability-off-axes]]); for a convex combination of two such systems it is nonnegative where it is for both.
In particular it is nonnegative on every piece of boundary whose conormal is future causal for both inverse metrics and
nonnegative on the transport fields.

**Lemma {#lem:loc-cone-cauchy}** (The Cauchy problem.) In case (I) for ε ≤ ε_0, and in case (II) for σ ≤ σ_0, where
σ_0 ∈ (0, σ_1] depends only on Λ, η, k, δ_c and the background, the system 𝔄_χ(𝐔) = F̃ has a smooth solution on
[τ_init, τ_+] × ℝ⁴ with 𝐔 = 𝐔̊ at τ_init, g_τ = ∂_τ g, g_a = ∂_a g, and |𝐔 − 𝐔_c| ≤ r_0. In case (I), sup_τ
‖𝐔 − 𝐔̊‖_(H^k) ≤ Cε; in case (II), sup |𝐔 − 𝐔̂| + sup |∂(𝐔 − 𝐔̂)| ≤ C(Λ) σ^(1/(4k)).

*Proof.* After the shift t := τ − τ_init the time interval is [0, T], T := ln(4c_+/δ_c²). In case (I) apply
[[thm:class-kato-stability]] (a), with d = 4, s = k and ρ = ∞, to the system for Z of [[lem:loc-cone-system]] (a), with
ū := 0 and u0 := 0: ū satisfies [[eq:class-kato-approximate]] with R := −Φ(x, 0) = 𝔄_χ(Ů) − F̃ = R_I, since 𝔄_χ(Ů) =
χ𝒜(Ů). (F1)–(F3) and (F1′) hold by [[rem:class-kato-local]]; ‖R_I(t)‖_(H^k) ≤ Cε ≤ 1 and sup_t ‖R_I‖ ≤ ε_0′ for ε small;
and the constants depend only on bounds of order k for the coefficients and on sup_t ‖Φ(t, ·, 0)‖_(H^k)
([[rem:class-kato-local]], the paragraph after it), which are uniform. So Z exists on [0, T], with sup_t ‖Z‖ ≤ Cε and
sup_t ‖Z‖_(H^(s′)) ≤ C ε^(1/(4k)) for s′ := k − 1/4 > 3; so sup |Z| ≤ C ε^(1/(4k)) ≤ r_0 for ε small, and the cut-off ϒ
is not active. For the bound in H^k, Z solves the linear problem of [[lem:class-kato-linear]] with v := Z and f :=
Φ(x, Z) − Φ(x, 0) − R_I, and ‖Φ(·, Z) − Φ(·, 0)‖_(H^k) ≤ C‖Z‖_(H^k) by [[lem:class-composition]] (b); by part (a) of that
lemma Z is the solution of its part (b), whose bound and Gronwall's inequality give sup_t ‖Z‖_(H^k) ≤ C sup_t
‖R_I‖_(H^k) ≤ Cε. In case (II) write the system for Z̃ := 𝐔 − 𝐔̂ and apply the same theorem with ū := 0, u0 := 0 (𝐔̂ =
𝐔̊ near Σ_init) and R := R_II, whose H^k norm is at most C(Λ)σ by [[lem:loc-cone-system]] (e); the constants depend
on Λ through the bounds of the coefficients near 𝐔̂, and not on σ, the system and T being fixed apart from F̃. For σ
small this gives the solution with ‖Z̃‖_(H^(s′)) ≤ C(Λ)σ^(1/(4k)), and ‖Z̃‖_(W^(1,∞)) ≤ C‖Z̃‖_(H^(s′)). The solution is
smooth by the argument of step (4) of the proof of [[cor:class-kato-sphere]] ([[thm:class-kato]] (a) at every order and
[[lem:class-kato-linear]] (c)), F̃ being smooth with compact support. The rows of (c) of [[lem:loc-cone-system]] hold at
τ_init, where 𝐔 = 𝐔̊. ∎

Below U denotes this solution, (g, p_A, Θ_A, q_A) its components and P_A := g⁻¹p_A.

**Lemma {#lem:loc-cone-past}** (The past of the edges.) U = Û on P ∩ 𝒰. So U − Û vanishes, with all its derivatives, on
N ∩ 𝒰, and g and the densities induce the cone data on N ∩ 𝒰.

*Proof.* On P, 𝔄_χ(𝐔) = F̃ = 𝔄_χ(Û) ([[lem:loc-cone-system]] (d)). 𝔄_χ(𝐔) = A^μ_χ(x, Z) ∂_μ𝐔 − Φ_0(x, Z) with Φ_0 smooth,
so z := 𝐔 − 𝐔̂ satisfies A^μ_χ(x, Ẑ) ∂_μ z = Mz on P, with Ẑ := 𝐔̂ − 𝐔̊ and M bounded on 𝒰, 𝐔 being C¹. Apply
[[lem:loc-cone-energy]] on the closure of P ∩ 𝒰, a Lipschitz domain (near S_c it lies below the graph of a Lipschitz
function in the coordinates u + v, u − v), with B_0 := Σ_init ∩ 𝒰, where z = 0 as 𝐔 = 𝐔̊ = 𝐔̂ there, and B_1 the rest of
its boundary: N ∩ 𝒰 and pieces of the far cuts. On N the outward conormal is du on {u = 0} and dv on {v = 0}. At Û the
wave blocks of A^μ_χ have the inverse metrics Ĝ⁻¹ and g_e⁻¹ (convexly combined), for which du and dv are null, with
du(∂_τ), dv(∂_τ) > 0; the transport fields are P̂_A and P̊_A, with du(P̂_out) = dv(P̂_in) = 0 and du(P̂_in), dv(P̂_out) >
0, likewise for P̊_A. On the far cuts the conormals du + κdv and dv + κdu are future timelike for every metric of the
form [[eq:loc-double-null]], since such metrics have g^(uu) = g^(vv) = 0 and g^(uv) < 0, and positive on future causal
vectors. So ν_μ 𝐀^μ ≥ 0 on B_1, and z = 0. ∎

**Lemma {#lem:loc-cone-support}** (Localisation.) U = Ů at the points of 𝒰 with ϑ < ϑ_a′ − 2C_* e^(τ/2), at those with
ϑ > ϑ_b′ + 2C_* e^(τ/2), and at those with u < u_K and v < v_K. In particular U = Ů on 𝒰 where ϑ < 3η/2 or
ϑ > π/2 − 3η/2.

*Proof.* On 𝒰, 𝔄_χ(𝐔) − 𝔄_χ(Ů) = F̃ − 𝔄_χ(Ů) vanishes outside K ([[lem:loc-cone-system]] (e)), so z := 𝐔 − 𝐔̊
satisfies A^μ_χ(x, 0) ∂_μ z = Mz on 𝒰 ∖ K, with M bounded. For ι > 0 let 𝒲 := {p ∈ 𝒰 : ϑ ≤ ϑ_a′ − ι − 2C_* e^(τ/2)};
it does not meet K, and on it 𝐔_c = 𝐔̊, so A^μ_χ(x, 0) = A^μ(x, 𝐔̊), with the inverse metric g_e on its wave block
and the transport fields P̊_A. Apply [[lem:loc-cone-energy]] on 𝒲 with B_0 := Σ_init ∩ 𝒲 and B_1 the angular face and
pieces of the far cuts. The angular face lies off the axes, as ϑ_a′ − 2C_* e^(τ/2) ≥ 2η − η/2, and its outward
conormal is ν := dϑ + C_* e^(τ/2) dτ. Since g_e⁻¹(dϑ, dτ) = 0, g_e⁻¹(dϑ, dϑ) = R_e⁻² and g_e⁻¹(dτ, dτ) = 2g_e^(uv)
e^(−τ) = −2e^(−2σ_e) e^(−τ),

    g_e⁻¹(ν, ν) = R_e⁻² − 2C_*² e^(−2σ_e) ≤ R_e⁻² − 2R_e⁻² < 0,

as C_* ≥ e^(σ_e)/R_e; ν(∂_τ) = C_* e^(τ/2) > 0, and ν(P̊_A) = C_* e^(τ/2) dτ(P̊_A) > 0, P̊_A having no ∂_ϑ-component. So
z = 0 on 𝒲 for every ι > 0. The set where ϑ > ϑ_b′ + 2C_* e^(τ/2) is treated in the same way with π/2 − ϑ in place of
ϑ. For {u ≤ u_K − ι, v ≤ v_K − ι} ∩ 𝒰, which does not meet K, the faces {u = u_K − ι} and {v = v_K − ι} have the
conormals du and dv, null for g_e with du(P̊_out) = dv(P̊_in) = 0 and du(P̊_in), dv(P̊_out) > 0. Finally ϑ_a′ − 2C_*
e^(τ/2) ≥ 2η − η/2 on 𝒰. ∎

**Lemma {#lem:loc-cone-constraints}** (The constraints.) On F ∩ 𝒰_σ, g⁻¹(p_A, p_A) = 0, dp_A = 0, D(g) = 0 and Θ_A =
div_g P_A. There are smooth functions u_in, u_out on 𝒰′ := (P ∩ 𝒰) ∪ (F ∩ 𝒰_σ) with p_in = −du_in, p_out = −du_out,
u_in = v and u_out = u on P ∩ 𝒰; and (g, u_in, u_out, q_in, q_out) solves [[eq:class-system]] on F ∩ 𝒰_σ, with
Ric(g) = q_in du_in ⊗ du_in + q_out du_out ⊗ du_out and q_A ≥ 0, in the gauge D(g) = 0 relative to Ĝ.

*Proof.* On F ∩ 𝒰_σ, θ = 1 and F̃ = 0. Let 𝒪_1 be the set of its points with η < ϑ < π/2 − η and 𝒪_2 that of its points
with ϑ < 3η/2 or ϑ > π/2 − 3η/2; both are open in F ∩ 𝒰_σ and cover it. On 𝒪_1, χ = 1 and |𝐔 − 𝐔_c| ≤ r_0, so 𝒜(U) = 0
([[lem:loc-cone-system]] (b)). On 𝒪_2, U = Ů ([[lem:loc-cone-support]]) and Ĝ = g_e, so there ν_A := g⁻¹(p_A, p_A),
dp_A, D := D(g) and Δ_A := Θ_A − div_g P_A vanish identically. By [[lem:loc-cone-past]] all four, with their
derivatives, vanish on N ∩ 𝒰: on P ∩ 𝒰, U = Û, and for Û they vanish identically.

*The phases.* On 𝒪_1, P_A(ν_A) = 0 by [[prop:class-augmented]] (b), and on 𝒪_2, ν_A = 0; so P_A(ν_A) = 0 on F ∩ 𝒰_σ.
Through a point of F ∩ 𝒰_σ the integral curve of P_A, followed to the past, cannot leave 𝒰_σ through {τ = ln((δ_c +
2σ)²)} or the far cuts, which are spacelike for g with 𝒰_σ to their past, and τ decreases along it at a rate bounded
below; as F ∩ 𝒰_σ ⊂ {τ ≥ 2 ln δ_c}, it reaches N, where ν_A = 0. So ν_A = 0 on F ∩ 𝒰_σ. Then ℒ_(P_A) dp_A = 0 on 𝒪_1
([[prop:class-augmented]] (b)) and dp_A = 0 on 𝒪_2, so dp_A, transported along the same curves from N, vanishes on
F ∩ 𝒰_σ. On P ∩ 𝒰, p_A = p̂_A is −dv or −du. So dp_A = 0 on 𝒰′, a simply connected planar set times S³, and p_A =
−du_A with u_A fixed by its values on the connected set P ∩ 𝒰; g⁻¹(du_A, du_A) = ν_A = 0.

*The gauge and the expansions.* On 𝒪_1, with p_A = −du_A an eikonal and ζ_A = 1, [[prop:class-augmented]] (d) and (e)
give

    P_A(Δ_A) = −Δ_A (Θ_A + div_g P_A − 2κ_A1 − 2κ_A2) + g(∇_(P_A) D, P_A) + L(P_A, P_A),

and D solves [[eq:class-gauge-wave]] with B_g T = Σ_A Δ_A q_A p_A, the tensor L being built with Γ[g] − Γ[Ĝ]; on 𝒪_2
all these quantities vanish. In the first-order variables z := (D, ∂_τ D, ∂_y D, Δ_in, Δ_out) this is a linear system
𝐀^μ ∂_μ z = Mz on F ∩ 𝒰_σ, of the form of Step 9 with the inverse metric g and the transport fields P_A, with C¹
coefficients. Apply [[lem:loc-cone-energy]] on the closure of F ∩ 𝒰_σ with B_0 := N ∩ 𝒰_σ, where z = 0, and B_1 the
future face and the far cuts, spacelike for g with future conormals positive on the P_A. So D = 0 and Δ_A = 0 on
F ∩ 𝒰_σ. Then (Aug1) is Ric(g) = Σ_A q_A p_A ⊗ p_A, by the identity of the proof of [[lem:gauge-propagation]] with Ĝ in
place of g0, and (Aug4) with Θ_A = div_g P_A is div_g(q_A P_A) = 0; on 𝒪_2 this is the background. The densities are
transported along the P_A from N, where they are those of the data or, on N_i for q_in and on N_o for q_out, determined
from their corner values by the conservation law, and so nonnegative. ∎

**Lemma {#lem:loc-cone-gauge}** (The double-null gauge.) Let ϑ′ be the function on 𝒰′ with P_out(ϑ′) = 0 and ϑ′ = ϑ on
P ∩ 𝒰, and Ψ := (u_out, u_in, ϑ′), acting on the orbit space and fixing φ1, φ2. Then Ψ is a diffeomorphism from F ∩ 𝒰_σ
onto a set that contains G_* in case (I) and [0, σ]² in case (II) (times the angles), equal to the identity, with its
differential, on N ∩ 𝒰_σ and on the sets of [[lem:loc-cone-support]]. In the coordinates (u′, v′, ϑ′, φ1, φ2) :=
(u_out, u_in, ϑ′, φ1, φ2) the metric g has the form [[eq:loc-double-null]], and (g, v′, u′, q_in, q_out) is a class
solution in the gauge on Ψ(F ∩ 𝒰_σ) × S³ that induces the cone data on the two edges. In case (I) its functions ln Ω,
½ ln γ_ϑ, b, A_c, A_s, q_in, q_out differ from the background's by at most Cε, with their derivatives of order at most
k − 4, at the points with η ≤ ϑ ≤ π/2 − η, and equal them elsewhere.

*Proof.* On P ∩ 𝒰, P_out = P̂_out = (2Ω̂²)⁻¹ ∂_v, and the past integral curves of ∂_v from P ∩ 𝒰 stay in P ∩ 𝒰; so
ϑ′ := ϑ ∘ Φ, Φ following the integral curves of P_out to the past to the set P ∩ 𝒰 ∩ {τ ≤ τ_init + 1}, is well
defined, smooth and G-invariant, and ϑ′ = ϑ on P ∩ 𝒰. By smoothness, u_out − u, u_in − v and ϑ′ − ϑ vanish with all
their derivatives on N ∩ 𝒰. Where U = Ů ([[lem:loc-cone-support]]), p_A = p̊_A and P_out = P̊_out ∝ ∂_v on a set that
contains, with each point, its past integral curves of P_out and meets P ∩ 𝒰; there Ψ is the identity.

*Ψ is near the identity.* In case (I), sup |𝐔 − 𝐔̊| + |∂(𝐔 − 𝐔̊)| ≤ Cε, and the derivatives of order at most k − 3 of
𝐔 − 𝐔̊ are at most Cε, by [[lem:loc-cone-cauchy]] and the Sobolev inequality on the slices; in case (II) the same
holds for 𝐔 − 𝐔̂ with C(Λ)σ^(1/(4k)) in place of Cε, at the order one. As d(u_out − u) = −(p_out − p̊_out) and
d(u_in − v) = −(p_in − p̊_in), and ϑ′ − ϑ solves P_out(ϑ′ − ϑ) = −(P_out − P̊_out)(ϑ) with zero values on P (in case
(II) with P̂ in place of P̊), Ψ − id is small in C¹ on F ∩ 𝒰_σ, in case (I) at most Cε in C^(k−3). The set F ∩ 𝒰_σ is a
down-set in (u, v): with (u, v) it contains [0, u] × [0, v]; so two of its points are joined in it by a path of length at
most 3 times their distance, through the point of least coordinates, and the bound on d(Ψ − id) makes Ψ injective. Ψ is
the identity on N and moves every point by at most sup |Ψ − id|, smaller than the distance from G_* (or from [0, σ]²)
to the rest of the boundary of F ∩ 𝒰_σ; by the homotopy invariance of the degree of id + t(Ψ − id), 0 ≤ t ≤ 1, the image
of Ψ contains these sets.

*The form of the metric.* In the new coordinates g⁻¹(du′, du′) = g⁻¹(dv′, dv′) = 0, and g⁻¹du′ = −P_out annihilates
du′ and dϑ′ and, by the reflections, dφ1 and dφ2, so g⁻¹du′ = c ∂_(v′) with c ≠ 0. So g^(u′u′) = g^(v′v′) = g^(u′ϑ′) = 0,
and the inverse of the (u′, v′, ϑ′)-block [[0, c, 0], [c, 0, e], [0, e, f]] is [[e²/(c²f), 1/c, −e/(cf)], [1/c, 0, 0],
[−e/(cf), 0, 1/f]]: g_(v′v′) = g_(v′ϑ′) = 0, g_(u′v′) = 1/c, g_(ϑ′ϑ′) = 1/f, g_(u′ϑ′) = −e/(cf) and g_(u′u′) = e²/(c²f).
This is [[eq:loc-double-null]] with −2Ω² = 1/c, γ_ϑ = 1/f and b = e/c. By [[lem:loc-cone-constraints]], v′ = u_in and
u′ = u_out are the phases of the two families. On N, Ψ and its differential are the identity and g agrees with Ĝ to all
orders, so the functions of g in the new coordinates and the densities are on N those of Ĝ, the cone data. In case (I)
the functions involve g ∈ C^(k−2), the densities ∈ C^(k−3), and Ψ⁻¹ with its first derivatives, ∈ C^(k−4); this gives the
estimate. ∎

**Lemma {#lem:loc-cone-unique}** (Uniqueness.) In case (I), let (g′, q′_in, q′_out) be a class solution in the gauge on
G_* × S³ that induces the cone data, whose functions differ from the background's by at most ε_2 with their derivatives
of order at most k at the points with 2η ≤ ϑ ≤ π/2 − 2η. For ε and ε_2 small it equals the solution of
[[lem:loc-cone-gauge]], in their coordinates, at the points of G_* with 3η ≤ ϑ ≤ π/2 − 3η.

*Proof.* (1) *Derivatives on N.* By [[lem:loc-cone-jets]] (iv) the functions of g′ and of the solution of
[[lem:loc-cone-gauge]] have the derivatives a_j, b_k across N. So g″ := g′ on G_* and Ĝ on P ∩ 𝒰 is smooth, and so is
g_e′ := g on F ∩ 𝒰 and Ĝ on P ∩ 𝒰 (here g is the solution in the coordinates (u, v, ϑ) of the construction, in which
D(g) = 0 relative to Ĝ).

(2) *A wave map.* Fix a point p of G_* with 3η ≤ ϑ(p) ≤ π/2 − 3η, u(p) < u_1 and v(p) < v_1; the remaining points follow
by continuity. Take δ′ ∈ (0, δ_c/2] and κ′ > 0 so small that p lies in 𝒟′ := {(u, v) : u, v ≥ 0, (u + δ′)(v + δ′) ≤
δ_*², u + κ′v ≤ u_1, v + κ′u ≤ v_1} × {9η/4 + 2C_*((u + δ′)(v + δ′))^(1/2) ≤ ϑ ≤ π/2 − 9η/4 − 2C_*((u + δ′)(v +
δ′))^(1/2)}; 𝒟′ lies in G_* ∩ {2η ≤ ϑ ≤ π/2 − 2η}, and 2C_*δ_* ≤ η/4. With τ′ := ln((u + δ′)(v + δ′)) in place of τ,
the faces of 𝒟′ other than N are spacelike for g_e, with 𝒟′ to their past, as in [[lem:loc-cone-support]], and so for
every metric close enough to g_e in C⁰ on 𝒟′. Seek Φ = id + φ with id: (𝒟′, (Φ⁻¹)^*g″) → Ĝ a wave map, that is

    g″^(μν) (∂_μ∂_ν Φ^λ − Γ[g″]^ρ_(μν) ∂_ρ Φ^λ + Γ[Ĝ]^λ_(αβ)(Φ) ∂_μΦ^α ∂_νΦ^β) = 0,

a semilinear wave system for φ whose principal part is that of g″. As in [[lem:loc-cone-system]] and
[[lem:loc-cone-cauchy]], case (I), with the time τ′, the initial slice {τ′ = ln(δ′²/4)} in P, a cut-off in ϑ equal to 1
on [9η/4, π/2 − 9η/4] and supported in (2η, π/2 − 2η) and a cut-off in (u, v) equal to 1 near 𝒟′, and the frozen part
taken with the wave operator of g_e: φ := 0 satisfies the cut-off system on P exactly, as g″ = Ĝ there, and on F up to
the residual 1_F g″^(μν)(Γ[Ĝ] − Γ[g″])^λ_(μν), which vanishes to infinite order on N and is at most C(ε + ε_2) in
C^(k−1). [[thm:class-kato-stability]] (a) with s = k − 1 > 3 gives a smooth solution φ on the slab with φ small in
W^(1,∞); φ = 0 on P, by the argument of [[lem:loc-cone-past]] with g″ = Ĝ on N; and on 𝒟′ ∩ F it solves the wave map
system, the cut-offs being 1 there.

(3) *Comparison.* For ε, ε_2 small, Φ is a diffeomorphism near the identity, equal to it on P and so, with all
derivatives, on N. Put g̃ := (Φ⁻¹)^*g″, ũ_A := u′_A ∘ Φ⁻¹ with u′_in := v, u′_out := u the phases of g′, p̃_A := −dũ_A,
Θ̃_A := div_(g̃) P̃_A, q̃_A := q′_A ∘ Φ⁻¹. Then D(g̃) = 0 relative to Ĝ, so (g̃, p̃_A, Θ̃_A, q̃_A) solves 𝒜 = 0 on
Φ(𝒟′ ∩ F) (off the axes, with [[eq:class-raychaudhuri]] for (Aug3)), and so does U on F ∩ 𝒰 ∩ {η < ϑ < π/2 − η}
([[lem:loc-cone-constraints]]). Both equal Û, with all derivatives, on N. On a set 𝒟″ ⊂ Φ(𝒟′) ∩ 𝒟′ of the same kind,
slightly smaller and still containing p, the difference z of their first-order variables satisfies A^μ(x, 𝐔) ∂_μ z =
Mz, and [[lem:loc-cone-energy]] with B_0 := N ∩ 𝒟″ and B_1 its other faces gives z = 0.

(4) *Conclusion.* So g = (Φ⁻¹)^*g″, p_A = p̃_A, and u_A = ũ_A, both being u or v on P. Hence Φ is an isometry from
(g′, u, v) to (g, u_out, u_in) on 𝒟′ ∩ F: u = u_out ∘ Φ and v = u_in ∘ Φ. It carries g′⁻¹du to g⁻¹du_out, so ϑ′ ∘ Φ is
constant along the integral curves of g′⁻¹du and equals ϑ on N_i, where Φ is the identity; as the angle of g′ has the
same two properties, ϑ′ ∘ Φ = ϑ. So Ψ ∘ Φ is the identity near p, and the functions of g′ at p are those of the
solution of [[lem:loc-cone-gauge]] at p. ∎

**Proposition {#prop:loc-cone-local}** (Developments near a corner sphere, of any size.) Let a background be given on
the set 𝒮 of [[eq:loc-cone-collar]] about a corner, and cone data at that corner ([[def:loc-cone-data]]), in any gauge,
that is with any ln Ω on both edges and any b on the ingoing edge N_i, and with any corner values, equal to the
background's at the points with ϑ ∉ [2η, π/2 − 2η] for some η ∈ (0, π/8], whose differences from the background's,
with ln Ω and ½ ln γ_ϑ in place of Ω and γ_ϑ, have C^(m_0) norms at most Λ on N_o ∩ {v ≤ 3δ_1} and N_i ∩ {u ≤ 3δ_1},
where k ≥ 6 and m_0 = 6k + 18. There is σ > 0, depending only on Λ, η, k, δ_1 and on bounds for σ_e, R_e, 1/R_e and
their derivatives of order at most m_0 + 2 on 𝒮 ∩ {|u|, |v| ≤ 3δ_1}, and not on l_u, l_v or on the data at distance more
than 3δ_1 from the corner, such that on [0, σ] × [0, σ] × S³ there is a class solution in the gauge that induces the
cone data on the two edges and equals the background at the points with ϑ ∉ [η, π/2 − η].

*Proof.* Case (II), with l_u = l_v = 2δ_1: by [[lem:loc-cone-jets]] the derivatives across N on N ∩ {u, v ≤ 3δ_1} use
only the data there. [[lem:loc-cone-cauchy]] for σ ≤ σ_0, then [[lem:loc-cone-past]], [[lem:loc-cone-support]],
[[lem:loc-cone-constraints]] and [[lem:loc-cone-gauge]], give the solution on Ψ(F ∩ 𝒰_σ) ⊃ [0, σ]², equal to the
background where ϑ < 3η/2 or ϑ > π/2 − 3η/2. The constants of these lemmas depend only on the quantities named, once δ_c
is fixed as a function of δ_1, η and C_*. ∎

The same argument as in [[lem:loc-cone-unique]], with the residual of the wave map localised by the cut-off θ of case
(II), shows that the development of [[prop:loc-cone-local]] is unique on [0, σ′]² among class solutions in the gauge that
equal the background where ϑ ∉ [η, π/2 − η] and whose functions have C^(k+1) norms at most Λ′ there, σ′ ≤ σ depending
also on Λ′; no result here uses this.

**Remark {#rem:loc-cone-local-scope}** (What the size of the rectangle depends on.) The number σ of [[prop:loc-cone-local]] depends on the data only through their C^(m_0) norms on the two edges within 3δ_1 of the corner, in any gauge and with any corner values, and not on l_u, l_v or on any smallness of the data. It depends on the background through δ_1, the width of the collar of 𝒮 on which the background is given, and through the bounds named there, for three reasons, which are the only places where the proof uses the background: near the axes the solution is the background, since off the band the augmented system is used only through the background's own solution and is not local at an axis ([[rem:loc-cone-scope]] (ii)); the modified system [[eq:loc-cone-modified]] takes the background's coefficients where its cut-off vanishes; and the time function [[eq:loc-cone-time]] and the faces of 𝒰 are spacelike for the metrics C⁰-close to g_e, with the constant C_*. A statement with no background, the data being prescribed up to the axes and the rectangle depending on their norms alone, needs a local theory of the augmented system at the axes, with domain of dependence for null boundaries there, and is not given in this paper.

*Proof of [[thm:loc-cone-development]].* Take the background of [[lem:loc-cone-strips]] (b) on 𝒮, with l_u = u_1, l_v = v_1, and C_* = C_0. The free data are ε-close to the background's in C^m, m = m_0 + 3 = 6k + 21. The equations of [[prop:loc-cones]] and [[lem:loc-cone-in]] are linear
ordinary differential equations along the generators whose coefficients differ from the background's by at most Cε in
C^(m−1); so for ε small e^ϕ stays within Cε of the background's, positive, on [0, v_1 + δ_1] and [0, u_1 + δ_1], ϕ is
within Cε of the background's in C^(m−1), and b in C^(m−3), r of [[eq:loc-cone-r]] holding two derivatives of the data.
So the cone data have size at most Cε, are in the normalised gauge, and equal the background's at the points with
ϑ ∉ [ϑ_a′, ϑ_b′], on 𝒞_out ∩ {v < v_K} and on 𝒞_in ∩ {u < u_K} (the constraints there have the background's coefficients
and corner values). [[lem:loc-cone-cauchy]], case (I), [[lem:loc-cone-past]], [[lem:loc-cone-support]],
[[lem:loc-cone-constraints]] and [[lem:loc-cone-gauge]] give a solution with (a) and (c) on G_*; and (d) is
[[lem:loc-cone-unique]] together with (b) for the solution of (a), which equals the background where ϑ < ϑ_a′ − η/4 or
ϑ > ϑ_b′ + η/4, so where ϑ < 3η or ϑ > π/2 − 3η. For (b): [[lem:loc-cone-support]] and the last part of
[[lem:loc-cone-gauge]] give the background at the points of G_* with ϑ < ϑ_a′ − 2C_* ((u + δ_c)(v + δ_c))^(1/2), with
ϑ > ϑ_b′ + 2C_* ((u + δ_c)(v + δ_c))^(1/2), or with u < u_K and v < v_K. The construction may be made with every smaller
δ_c, and by (d) the solutions coincide on G_*, all of them equalling the background where ϑ < 3η or ϑ > π/2 − 3η; letting
δ_c → 0 gives (b). Finally 2C_0 (uv)^(1/2) ≤ 2C_* δ_* ≤ η/4 on G_*, and ϑ_a′ > ϑ_a, ϑ_b′ < ϑ_b. ∎

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:". Line numbers
are those of the current chapter sources and serve only to find the place. The texts of items 3 and 4 are also replaced
by the Tier 2 section on large data, which follows the section of item 2 and cites [[thm:loc-cone-development]],
[[lem:loc-cone-in]] and [[prop:loc-cone-local]]; where both change a text, the coordinator merges the two new texts.

*1. Block A.* The text of Block A, from the statement of [[lem:loc-cone-in]] through the end of [[rem:loc-cone-scope]]
(without the heading "Block A" and its first paragraph), is inserted in [[sec:loc-cones]] immediately after the proof of
[[prop:loc-cones]], whose last line ends with "background's by uniqueness." and the end mark (line 591), with one blank
line before and one after; the paragraph of item 4 follows it. It defines lem:loc-cone-in, eq:loc-cone-in,
thm:loc-cone-development, eq:loc-cone-domain and rem:loc-cone-scope.

*2. Block B.* The section of Block B, from its heading through the end of the proof of [[thm:loc-cone-development]], is
inserted in [[ch:localised-data]] as a new section immediately after [[sec:loc-cones]], that is before the heading
of [[sec:loc-kid]] (line 602), and before the Tier 2 section if that is placed
there too, with one blank line before and one after. Its heading line is the heading of Block B
without the words "Block B.". It defines sec:loc-cone-proof, sec:loc-cone-setting,
eq:loc-cone-collar, def:loc-cone-data, lem:loc-cone-strips, sec:loc-cone-equations-frame, eq:loc-cone-quantities,
lem:loc-cone-frame, lem:loc-cone-ricci, eq:loc-cone-frame-ricci, eq:loc-cone-bianchi, sec:loc-cone-formal,
lem:loc-cone-borel, lem:loc-cone-jets, eq:loc-cone-goursat, prop:loc-cone-formal, sec:loc-cone-reduced, eq:loc-cone-time,
eq:loc-cone-region, eq:loc-cone-modified, lem:loc-cone-system, lem:loc-cone-energy, lem:loc-cone-cauchy,
lem:loc-cone-past, lem:loc-cone-support, lem:loc-cone-constraints, lem:loc-cone-gauge, lem:loc-cone-unique,
prop:loc-cone-local and rem:loc-cone-local-scope, none of which is defined elsewhere. Numbers are resolved at assembly.

*3. [[ch:localised-data]], its opening paragraph (lines 8–9).* Old:

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]]). On Σ_τ0 the constraints split, after Rácz

New:

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]], [[lem:loc-cone-in]]); near the background's
data, with the band away from the axes, they have a development on a neighbourhood of the two cones, with or without
dust, equal to the background outside the domain of influence of the band and unique in the gauge off the axes
([[thm:loc-cone-development]]). On Σ_τ0 the constraints split, after Rácz

*4. [[ch:localised-data]], the paragraph after [[prop:loc-cones]] (lines 593–600).* Old:

When these cone data carry no dust, their vacuum development near the two cones exists by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]): this is the case when v_1 < 3, so that 𝒞_out ∩ {v ≤ v_1} lies before the shell, the
dust densities are left zero there, and 𝒞_in is taken only on u < 5.7, before the packet; both cones then carry
vacuum data of Tangherlini's metric of mass 3/2 outside the band, and the two cones meet transversally in the corner
sphere. [CTG23, Theorem 1.1] concerns vacuum data only. For cone data that carry dust, among them every perturbation
of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} and every density added in the band,
no development is asserted here: [[prop:loc-cones]] gives the cone data only, and no result of this paper uses their
development.

New (after Block A):

[[thm:loc-cone-development]] develops these cone data when they are near the background's and their band avoids the
axes, with or without dust: on the neighbourhood G_* of the two cones there is a class solution in the gauge
[[eq:loc-double-null]] that induces them, equal to the background outside the domain of influence of the band and
unique in the gauge off the axes. Every small perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on
𝒞_in ∩ {5.7 < u < 7.2}, and every small density added in the band, supported away from the axes, is of this kind, with
v_1 = 4.5 and u_1 = 7.2 ([[lem:loc-cone-strips]] (c)). For vacuum data of any size, before the shell (v_1 < 3) and on
𝒞_in before the packet (u_1 < 5.7), a development near the two cones exists by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]); that theorem gives neither uniqueness in the gauge nor localisation. For cone data that
carry dust and are not small, and for data whose perturbation reaches an axis, no development is asserted by
[[thm:loc-cone-development]] ([[rem:loc-cone-scope]]). No result of the other chapters uses these developments.

*5. [[ch:introduction]], the paragraph on [[part:further]] (lines 189–191).* Old:

[[part:further]] treats two crossing dusts ([[ch:two-dusts]]), the class Einstein–null-dust system
([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data and the sign of the charge
([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]], [[ch:equality-edge]]), the threshold λ0 at a

New:

[[part:further]] treats two crossing dusts ([[ch:two-dusts]]), the class Einstein–null-dust system
([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data, their development from two
null cones and the sign of the charge ([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]],
[[ch:equality-edge]]), the threshold λ0 at a

*6. [[ch:theorems]], the bullet "More families", its last lines (lines 373–374).* Old:

  data exist for small amplitude, while on vacuum bands outside it the sign of their charge at second order excludes
  them for small amplitude when the first-order part is T² × Z2 × Z2-invariant ([[thm:charge-sign]]).

New:

  data exist for small amplitude, while on vacuum bands outside it the sign of their charge at second order excludes
  them for small amplitude when the first-order part is T² × Z2 × Z2-invariant ([[thm:charge-sign]]). Data localised
  in angle on two null cones of that background exist exactly, and near the background's data, with the band away from
  the axes, they develop, dust included, on a neighbourhood of the cones, equal to the background outside the domain
  of influence of the band and unique in the gauge off the axes ([[thm:loc-cone-development]]).

*7. [[ch:scope]], the paragraph on localised data, its last line (line 200).* Old:

small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]).

New:

small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]). Data localised
in angle on the two null cones exist exactly, and near the background's data, with the band away from the axes, they
develop, dust included, on a neighbourhood of the cones, equal to the background outside the domain of influence of the
band and unique in the gauge off the axes; developments of dust-carrying cone data that are not small, or whose
perturbation reaches an axis, are not established ([[prop:loc-cones]], [[thm:loc-cone-development]],
[[rem:loc-cone-scope]]).

*8. Unchanged.* [[ch:ten-l5]] and the sentences of [[ch:scope]] on the characteristic problem at 10 l5 stand: that
problem is vacuum, not near an explicit background, needs the regions D_s that contain the axes and uniqueness in the
gauge on them, and has data that are C³; [[thm:loc-cone-development]] gives none of these. [[ch:class-system]] and
[[ch:two-dusts]] are unchanged.

*9. Appendix A.* No new entry: the proofs use no published result as a black box beyond those already stated there.
[LR20, Theorem 4.6, p. 29] is quoted only for comparison in [[rem:loc-cone-scope]] (iii); its wording there was checked
against the arXiv text (version 1, p. 29).

*10. References.* New entry, in alphabetical place (after [Rac16]):

- [Ren90] A. D. Rendall, *Reduction of the characteristic initial value problem to the Cauchy problem and its
  applications to the Einstein equations*, Proc. Roy. Soc. London Ser. A 427 (1990), no. 1872, 221–239.
  doi:10.1098/rspa.1990.0009

### Crosswalk rows

New rows for the crosswalk table of [[ch:localised-data]], one per label, each given as its four fields (label; source;
source_name; note), to be written with tab separators. The second field is "P-CIVP" with the line of the label in this
file.

Row 1. lem:loc-cone-in; P-CIVP:6; P-CIVP Block A, Lemma (Exact localisation on the ingoing cone); new: the analogue of
prop:loc-cones on 𝒞_in in the gauge b = 0, Raychaudhuri along ∂_u, ∂_v b a transverse derivative.
Row 2. eq:loc-cone-in; P-CIVP:11; P-CIVP Block A, display; Ric(∂_u, ∂_u) on 𝒞_in.
Row 3. thm:loc-cone-development; P-CIVP:37; P-CIVP Block A, Theorem (Development of cone data localised in angle);
new: Tier 1 of the scoping report, existence on G_*, localisation, estimate, uniqueness off the axes.
Row 4. eq:loc-cone-domain; P-CIVP:49; P-CIVP Block A, display; the set G_*.
Row 5. rem:loc-cone-scope; P-CIVP:78; P-CIVP Block A, Remark; smallness, axes, regularity ([LR20, Theorem 4.6]),
domain.
Row 6. sec:loc-cone-proof; P-CIVP:96; P-CIVP Block B, section heading; Rendall's reduction for the augmented system.
Row 7. sec:loc-cone-setting; P-CIVP:116; P-CIVP Block B; corners, edges, backgrounds on 𝒮.
Row 8. eq:loc-cone-collar; P-CIVP:122; P-CIVP Block B, display; the set 𝒮.
Row 9. def:loc-cone-data; P-CIVP:134; P-CIVP Block B, Definition (Cone data at a corner); any gauge on both edges.
Row 10. lem:loc-cone-strips; P-CIVP:151; P-CIVP Block B, Lemma (The background near the cones); strips in G, smooth
extension across the cones, R ≥ 5 on 𝒞_out and R > 1.5 on 𝒞_in ∩ {u ≤ 7.2}.
Row 11. sec:loc-cone-equations-frame; P-CIVP:186; P-CIVP Block B, subsection; the double-null frame.
Row 12. eq:loc-cone-quantities; P-CIVP:192; P-CIVP Block B, display; χ, χ̲, η, ζ, 𝒱.
Row 13. lem:loc-cone-frame; P-CIVP:202; P-CIVP Block B, Lemma (The connection); Koszul table.
Row 14. lem:loc-cone-ricci; P-CIVP:224; P-CIVP Block B, Lemma (The equations); Ricci in the frame, dust, Bianchi;
(L̲, L̲) and (L̲, ∂_ϑ) from lem:loc-cone-equations by exchanging u and v.
Row 15. eq:loc-cone-frame-ricci; P-CIVP:238; P-CIVP Block B, display; the frame components of E.
Row 16. eq:loc-cone-bianchi; P-CIVP:249; P-CIVP Block B, display; div E for the constraint components.
Row 17. sec:loc-cone-formal; P-CIVP:320; P-CIVP Block B, subsection; the formal solution.
Row 18. lem:loc-cone-borel; P-CIVP:322; P-CIVP Block B, Lemma (Extension of derivatives given on two edges); Borel
with a corner, C^r bound.
Row 19. lem:loc-cone-jets; P-CIVP:369; P-CIVP Block B, Lemma (The derivatives across the edges); linear ODEs along
the generators, corner compatibility, no smallness; loss 4 derivatives per order.
Row 20. eq:loc-cone-goursat; P-CIVP:401; P-CIVP Block B, display; the five equations solved for the mixed derivatives.
Row 21. prop:loc-cone-formal; P-CIVP:484; P-CIVP Block B, Proposition (The formal solution); constraints propagated to
all orders by the contracted Bianchi identity.
Row 22. sec:loc-cone-reduced; P-CIVP:522; P-CIVP Block B, subsection; cases (I) small data, (II) small rectangle.
Row 23. eq:loc-cone-time; P-CIVP:534; P-CIVP Block B, display; the time τ and the chart (τ, y).
Row 24. eq:loc-cone-region; P-CIVP:541; P-CIVP Block B, display; the region 𝒰.
Row 25. eq:loc-cone-modified; P-CIVP:587; P-CIVP Block B, display; the modified system and the forcing term F̃.
Row 26. lem:loc-cone-system; P-CIVP:592; P-CIVP Block B, Lemma (The modified system); reference metric Ĝ in the gauge,
cut-offs, residuals.
Row 27. lem:loc-cone-energy; P-CIVP:641; P-CIVP Block B, Lemma (Energy on a region).
Row 28. lem:loc-cone-cauchy; P-CIVP:659; P-CIVP Block B, Lemma (The Cauchy problem); thm:class-kato-stability (a).
Row 29. lem:loc-cone-past; P-CIVP:684; P-CIVP Block B, Lemma (The past of the edges).
Row 30. lem:loc-cone-support; P-CIVP:698; P-CIVP Block B, Lemma (Localisation).
Row 31. lem:loc-cone-constraints; P-CIVP:718; P-CIVP Block B, Lemma (The constraints); Step 10 of
thm:class-stability-off-axes with zero data on the cones.
Row 32. lem:loc-cone-gauge; P-CIVP:752; P-CIVP Block B, Lemma (The double-null gauge).
Row 33. lem:loc-cone-unique; P-CIVP:788; P-CIVP Block B, Lemma (Uniqueness); comparison through a wave map.
Row 34. prop:loc-cone-local; P-CIVP:830; P-CIVP Block B, Proposition (Developments near a corner sphere, of any size);
cited by the Tier 2 section for its corner developments.

Notes for existing rows: sec:loc-cones and prop:loc-cones (the closing paragraph now states the development,
[[thm:loc-cone-development]], and names what is not covered; the loss "no development is asserted" for cone data with
dust remains only for data that are not small or that reach an axis); ch:localised-data (opening, text 3); in
[[ch:introduction]], the paragraph on Part further (text 5); in [[ch:theorems]], the bullet "More families" (text 6); in
[[ch:scope]], the paragraph on localised data (text 7).
