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

*Proof.* On 𝒞_in, b = 0, so ∂_u b = ∂_ϑ b = 0 there, and g(∂_u, ∂_u) = γ_ϑ b² and g(∂_u, ∂_ϑ) = −γ_ϑ b vanish there.
So ∂_u is null and orthogonal to ∂_u, ∂_ϑ, ∂_(φ1), ∂_(φ2) along 𝒞_in: it is the null normal of 𝒞_in, and the
sections {u = const} of 𝒞_in carry γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2². With the inverse metric of the proof of
[[lem:loc-cone-equations]], Γ^u_(uu) = ½ g^(uv)(2∂_u g_(uv) − ∂_v g_(uu)) = 2∂_u ln Ω + ∂_v(γ_ϑ b²)/(4Ω²), and
∂_v(γ_ϑ b²) = b (2γ_ϑ ∂_v b + b ∂_vγ_ϑ) = 0 on 𝒞_in; Γ^v_(uu) = ½ g^(vu) ∂_u(γ_ϑ b²) + ½ g^(vϑ)(2∂_u g_(ϑu) − ∂_ϑ
g_(uu)) and Γ^ϑ_(uu) = ½ g^(ϑv)(2∂_u g_(vu) − ∂_v g_(uu)) + ½ γ_ϑ⁻¹(−2∂_u(γ_ϑ b) − ∂_ϑ(γ_ϑ b²)) vanish there, since
g^(vϑ) = −b/(2Ω²); and Γ^(φi)_(uu) = 0. So ∇_(∂_u)∂_u = 2∂_u ln Ω ∂_u on 𝒞_in. The field ∂_u commutes with ∂_ϑ,
∂_(φ1), ∂_(φ2), so for X, Y among these g(∇_X ∂_u, Y) = −g(∂_u, ∇_X Y) on 𝒞_in is symmetric in X and Y, and the null
second fundamental form of the sections along ∂_u is half the u-derivative of their metric, with eigenvalues ∂_uϰ_i.
The Raychaudhuri equation along ∂_u is [[eq:loc-cone-in]], as in the proof of [[lem:loc-cone-equations]]. With
y := e^ϕ, T(∂_u, ∂_u) = q_out and (ln Ω)′ = 0 on 𝒞_in (there e^(2σ) = 1/2), it reads y″ + (1/3)(Σ_i (ℓ_i′)² + q_out) y
= 0, ′ = ∂_u, and the proof of [[prop:loc-cones]] applies with u in place of v. ∎

On the corner sphere S = 𝒞_out ∩ 𝒞_in the two cones carry one metric, γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2² with the
background's ϕ, so the free data of [[prop:loc-cones]] at v = 0 and those of [[lem:loc-cone-in]] at u = 0 agree; nothing
else is required at S, the density q_in being free on 𝒞_out and q_out on 𝒞_in. Near the background's data, and with the
band away from the axes, these cone data have a development.

**Theorem {#thm:loc-cone-development}** (Development of cone data localised in angle.) Let u_1, v_1 > 0 be such that
R > a on the segments 𝒞_out ∩ {v ≤ v_1} and 𝒞_in ∩ {u ≤ u_1}, a = 0.70 the inner radius of [[sec:loc-setting]], let
R_min be the least value of R on them and C_0 := 2√2/R_min. Let 0 < ϑ_a < ϑ_b < π/2, η := (1/4) min(ϑ_a, π/2 − ϑ_b),
k ≥ 6 an integer and m := 6k + 15. Take free data (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0 on 𝒞_out ∩ {v ≤ v_1} as in
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
the background's in C^m, m = 6k + 15. Densities that are only bounded, or measures (shells), are not covered. For the
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

Points of the (u, v)-plane stand for the corresponding spheres; a set of points is identified with its product with S³.
A *background* on 𝒮 is a round metric g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with σ_e, R_e > 0 smooth on 𝒮, together with
smooth profiles 𝒜(v), ℬ(u) ≥ 0, such that on 𝒮 ∩ F it solves the two-null-dust equations [[eq:two-dust-limit]],
Ric(g_e) = (𝒜/R_e³) dv ⊗ dv + (ℬ/R_e³) du ⊗ du. Its double-null functions are Ω_e² = e^(2σ_e)/2, γ_ϑ = R_e²,
A_c = ln(R_e cos ϑ), A_s = ln(R_e sin ϑ), b = 0, and its densities are q̊_in := 𝒜/R_e³ and q̊_out := ℬ/R_e³; so
ρ̊_in := 𝒱q̊_in = 𝒜(v) sin ϑ cos ϑ and ρ̊_out := ℬ(u) sin ϑ cos ϑ, with 𝒱 of [[sec:loc-cone-equations-frame]]. A *class
solution in the gauge* on a set D × S³, D ⊂ F, is a smooth class solution of [[eq:class-system]] with two families, phases
v and u and densities q_in and q_out, so that Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, whose metric has the form
[[eq:loc-double-null]] with Ω, γ_ϑ, b, A_c, A_s smooth functions of (u, v, ϑ), equal to the background's near the axes.

**Definition {#def:loc-cone-data}** (Cone data at a corner.) Let a background on 𝒮 be given and k ≥ 6. *Cone data* are
smooth functions ln Ω, ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, b and q_in ≥ 0 of (v, ϑ) on N_o and ln Ω, ϰ_1, ϰ_2, ϰ_3 and
q_out ≥ 0 of (u, ϑ) on N_i, with b := 0 on N_i, such that: (i) ln Ω and the ϰ_i of the two edges agree on S_c; (ii)
Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o, the left sides being given by [[eq:loc-cone]] in terms of the functions
on N_o, and Ric(∂_u, ∂_u) = q_out on N_i, the left side being given by [[eq:loc-cone-in]]; (iii) for some numbers
0 < ϑ_a′ < ϑ_b′ < π/2 they equal the background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′]. Their *size* is the largest
absolute value of a derivative of order at most m_0 := 6k + 12 of their differences from the background's.

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

For [[prop:loc-cone-local]] the background is that of [[thm:civp-large]]'s setting or any background on 𝒮 in the sense
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

*Proof.* Each entry is Koszul's formula 2g(∇_X Y, Z) = X g(Y, Z) + Y g(Z, X) − Z g(X, Y) + g([X, Y], Z) − g([Y, Z], X)
+ g([Z, X], Y), with X, Y, Z in the frame, the products and brackets above, and the fact that the products depend on
(u, v, ϑ) only. For instance 2g(∇_L̲ L̲, ∂_v) = 2L̲ g(L̲, ∂_v) + 2g([∂_v, L̲], L̲) = −4L̲Ω², while g(∇_L̲ L̲, Z) = 0 for
Z = L̲, ∂_ϑ, K_i, which gives the first entry; and 2g(∇_L̲ ∂_v, ∂_ϑ) = L̲ g(∂_v, ∂_ϑ) + ∂_v g(∂_ϑ, L̲) − ∂_ϑ g(L̲, ∂_v) +
g([L̲, ∂_v], ∂_ϑ) − g([∂_v, ∂_ϑ], L̲) + g([∂_ϑ, L̲], ∂_v) = 4Ω²η − γ_ϑ ∂_v b, while 2g(∇_L̲ ∂_v, Z) = 0 for the other
frame fields, which gives the third. The others follow in the same way. The derivatives of the frame have no
K_i-component unless the K_i enters, because the reflection φ_i ↦ −φ_i is an isometry that fixes L̲, ∂_v, ∂_ϑ and
reverses K_i. As a check, ∇_(∂_v) L̲ − ∇_L̲ ∂_v = (4Ω²ζ/γ_ϑ) ∂_ϑ = (∂_v b) ∂_ϑ and ∇_(∂_ϑ) L̲ − ∇_L̲ ∂_ϑ = (χ̲_1 −
L̲ϰ_1) ∂_ϑ = (∂_ϑ b) ∂_ϑ, the brackets. ∎

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
    E(L̲, L̲) = Σ_i (−L̲χ̲_i − χ̲_i² + 2 L̲ ln Ω χ̲_i) − q_out.                                  {#eq:loc-cone-frame-ricci}

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

and R(∂_ϑ, ∂_ϑ) = 0; summing gives E(∂_ϑ, ∂_ϑ), since χ_1χ̲_1 + ½ Σ_(i=2,3) (χ_1χ̲_i + χ̲_1χ_i) = ½(tr χ χ̲_1 + χ_1 tr χ̲).
Likewise R(L̲, L̲) = 0 and

    g(R(∂_v, L̲)∂_v, L̲) = 4Ω² ∂_v L̲ ln Ω − 4Ω⁴γ_ϑ⁻¹ η² − 2Ω² η ∂_v b + ¾ γ_ϑ (∂_v b)²,
    γ_ϑ⁻¹ g(R(∂_ϑ, L̲)∂_v, ∂_ϑ) = −(∂_v χ̲_1 + χ_1 χ̲_1) + ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b) + (γ_ϑ/(8Ω²)) (∂_v b)²
                                + 2Ω²γ_ϑ⁻¹ (∂_ϑη + η² − ∂_ϑϰ_1 η),
    e^(−2ϰ_(i+1)) g(R(K_i, L̲)∂_v, K_i) = −(∂_v χ̲_(i+1) + χ_(i+1) χ̲_(i+1)) + 2Ω²γ_ϑ⁻¹ η ∂_ϑϰ_(i+1) + ½ ∂_ϑϰ_(i+1) ∂_v b;

summing gives E(L̲, ∂_v), since 2Ω²γ_ϑ⁻¹(∂_ϑη + 2η² + η ∂_ϑ(ϰ_2 + ϰ_3 − ϰ_1)) = 𝒱⁻¹∂_ϑ(𝒱γ_ϑ⁻¹∂_ϑΩ²) and
½ ∂_ϑ∂_v b + ½ ∂_v b ∂_ϑ ln 𝒱 + η ∂_v b = (2Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 ∂_v b).

(b) The determinant is that of the proof of [[lem:loc-cone-equations]]. div(q P) = |det g|^(−1/2) ∂_μ(|det g|^(1/2)
q P^μ) with P = g⁻¹dv, P^u = g^(uv), P^ϑ = g^(ϑv), and with P = g⁻¹du = g^(uv) ∂_v. tr_g T = q_in g^(vv) + q_out g^(uu)
= 0. By [[prop:class-augmented]] (c), div_g T is the stated sum plus q_in ∇_(g⁻¹dv) dv + q_out ∇_(g⁻¹du) du, and
∇_(g⁻¹dv) dv = ½ d(g⁻¹(dv, dv)) = 0, likewise for du.

(c) In the frame, g⁻¹ = −(2Ω²)⁻¹ (L̲ ⊗ ∂_v + ∂_v ⊗ L̲) + γ_ϑ⁻¹ ∂_ϑ ⊗ ∂_ϑ + Σ_i e^(−2ϰ_(i+1)) K_i ⊗ K_i, so tr_g E =
−Ω⁻² E(L̲, ∂_v) + γ_ϑ⁻¹ E(∂_ϑ, ∂_ϑ) + Σ_i e^(−2ϰ_(i+1)) E(K_i, K_i) is linear in E′, and (div_g E)(Y) =
−(2Ω²)⁻¹ ((∇_L̲ E)(∂_v, Y) + (∇_(∂_v) E)(L̲, Y)) + γ_ϑ⁻¹ (∇_(∂_ϑ) E)(∂_ϑ, Y) + Σ_i e^(−2ϰ_(i+1)) (∇_(K_i) E)(K_i, Y),
with (∇_X E)(Z, Y) = X(E(Z, Y)) − E(∇_X Z, Y) − E(Z, ∇_X Y). The terms in E′ and its first derivatives make up the ℓ_j.
The rest has only a, β, c, and the table of [[lem:loc-cone-frame]] gives, for Y = L̲: (∇_(∂_v) E)(L̲, L̲) = ∂_v c −
2E(∇_(∂_v) L̲, L̲) = ∂_v c, (∇_L̲ E)(∂_v, L̲) = 0, (∇_(∂_ϑ) E)(∂_ϑ, L̲) = −(γ_ϑ/(2Ω²)) χ_1 c and (∇_(K_i) E)(K_i, L̲) =
−(e^(2ϰ_(i+1))/(2Ω²)) χ_(i+1) c; for Y = ∂_ϑ: (∇_L̲ E)(∂_v, ∂_ϑ) = L̲β − (L̲ϰ_1) β, (∇_(∂_v) E)(L̲, ∂_ϑ) = 0,
(∇_(∂_ϑ) E)(∂_ϑ, ∂_ϑ) = −(γ_ϑ/Ω²) χ̲_1 β and (∇_(K_i) E)(K_i, ∂_ϑ) = −(e^(2ϰ_(i+1))/(2Ω²)) χ̲_(i+1) β, and 2χ̲_1 − L̲ϰ_1 =
χ̲_1 + ∂_ϑ b; for Y = ∂_v: (∇_L̲ E)(∂_v, ∂_v) = L̲a − (4Ω²/γ_ϑ)(η − ζ) β, (∇_(∂_v) E)(L̲, ∂_v) = −(2Ω²/γ_ϑ)(η + ζ) β,
(∇_(∂_ϑ) E)(∂_ϑ, ∂_v) = ∂_ϑβ − (γ_ϑ/(2Ω²)) χ̲_1 a − (∂_ϑϰ_1 + η + ζ) β and (∇_(K_i) E)(K_i, ∂_v) =
−(e^(2ϰ_(i+1))/(2Ω²)) χ̲_(i+1) a + e^(2ϰ_(i+1))γ_ϑ⁻¹ ∂_ϑϰ_(i+1) β, and 2γ_ϑ⁻¹ζ = (2Ω²)⁻¹ ∂_v b. Summing gives
[[eq:loc-cone-bianchi]]. The last identity is the contracted Bianchi identity div Ric = ½ d(tr_g Ric), with
tr_g Ric = tr_g E + tr_g T = tr_g E. ∎

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

*Proof.* Fix χ ∈ C^∞(ℝ) with 0 ≤ χ ≤ 1, χ = 1 on [−1, 1] and supp χ ⊂ (−2, 2). For 0 < ε ≤ 1 and integers i, j ≥ 0,
|∂_x^i(χ(x/ε) x^j)| ≤ C(i, j) ε^(j−i) when i ≤ j, since the derivatives of χ(x/ε) are ε^(−l) χ^(l)(x/ε) and vanish for
|x| ≥ 2ε. So for a smooth function h(z) of further variables z, the term χ(x/ε) x^j h(z)/j! has C^(j−1) norm at most
C(j) ε ‖h‖_(C^(j−1)) and C^r norm at most C(r, j) ‖h‖_(C^r). Given smooth h_j, choose ε_j := ε_0 for j ≤ r and, for
j > r, ε_j ≤ ε_0 so small that the C^(j−1) norm of the j-th term is at most 2^(−j) γ_0. Then the series Σ_j χ(x/ε_j)
x^j h_j(z)/j! converges in every C^p, its terms of index above p + 1 having C^p norms at most 2^(−j) γ_0; its sum B is
smooth, may be differentiated termwise, and ∂_x^j B(0, z) = h_j(z), as χ = 1 near 0. Call B the Borel sum of (h_j).

*Step 1.* For each j let ã_j := a_j on [0, λ_v] × Y and, for v < 0, ã_j := the Borel sum in v of (c_(jk))_k. All one-sided
v-derivatives of the two pieces at v = 0 are the c_(jk), so ã_j is smooth on (−∞, λ_v] × Y. *Step 2.* Let f_1 be the Borel
sum in u of (ã_j)_j; then ∂_u^j f_1(0, v, ϑ) = ã_j(v, ϑ). *Step 3.* Termwise, ∂_v^k f_1(u, 0, ϑ) = Σ_j χ(u/ε_j) u^j
c_(jk)(ϑ)/j!, whose u-derivatives at u = 0 are the c_(jk). So d_k := b_k − ∂_v^k f_1(·, 0, ·) on [0, λ_u] × Y has all its
u-derivatives zero at u = 0, and extended by 0 to u < 0 it is smooth. Let f := f_1 + the Borel sum in v of (d_k)_k. Its
u-derivatives at u = 0 are those of f_1, since every d_k vanishes for u ≤ 0, and ∂_v^k f(u, 0, ϑ) = ∂_v^k f_1(u, 0, ϑ) +
d_k(u, ϑ) = b_k(u, ϑ).

(a) f_1 vanishes for |u| ≥ 2ε_0 and, ã_j vanishing for v ≤ −2ε_0, for v ≤ −2ε_0; the second sum vanishes for |v| ≥ 2ε_0
and for u < 0. The cut-offs depend on u and v only. If all a_j vanish for v < v_K, then all c_(jk) = 0, so ã_j = 0 for
v < v_K and f_1 = 0 there; and d_k = b_k vanishes for u < u_K.

(b) The terms of index at most r have the cut-off scale ε_0 and C^r norms at most C(r, ε_0) times the C^r norms of ã_j,
respectively d_k; ‖ã_j‖_(C^r) ≤ ‖a_j‖_(C^r) + C max_(k≤r) ‖c_(jk)‖_(C^r) + (the sum of the terms of index above r),
‖d_k‖_(C^r) ≤ ‖b_k‖_(C^r) + C max_(j≤r) ‖c_(jk)‖_(C^r) + (the like), and ‖c_(jk)‖_(C^r) ≤ ‖a_j‖_(C^(r+k)) ≤ ‖a_j‖_(C^(2r))
for k ≤ r. Choosing every ε of index above r also so small that the C^r norms of the terms it multiplies sum, over all
three sums, to at most γ_0/2 in total, (b) follows. ∎

In the rest of the section a background on 𝒮 and cone data are fixed, X denotes the list of functions
(ln Ω, ϰ_1, ϰ_2, ϰ_3, b, ρ_in, ρ_out) of (u, v, ϑ), and X̊ the background's. On N_o let a_0 be the cone data, with
ρ_in := 𝒱q_in and with ρ_out equal on each generator to the value of 𝒱q_out at the corner; on N_i let b_0 be the cone
data, with b := 0, ρ_out := 𝒱q_out and ρ_in equal on each generator to the value of 𝒱q_in at the corner. We assume, as
the corner condition (i) of [[def:loc-cone-data]] together with b = 0 on N_i requires for continuity, that b = 0 at the
corner on N_o; then a_0 = b_0 on S_c.

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

*Proof.* *The equations solved for the mixed derivatives.* In [[eq:loc-cone-frame-ricci]] write ∂_v L̲f = ∂_u∂_v f +
∂_v b ∂_ϑ f + b ∂_v∂_ϑ f, χ̲_1 = ∂_uϰ_1 + b ∂_ϑϰ_1 + ∂_ϑ b, χ̲_i = ∂_uϰ_i + b ∂_ϑϰ_i (i = 2, 3). The equations
E(∂_ϑ, ∂_ϑ) = E(K_1, K_1) = E(K_2, K_2) = 0 contain ∂_u∂_vϰ_1, ∂_u∂_vϰ_2, ∂_u∂_vϰ_3 with the factors γ_ϑ/Ω², Ω⁻²
and Ω⁻², and E(L̲, ∂_v) = 0 contains −2∂_u∂_v ln Ω − Σ_i ∂_u∂_vϰ_i; E(L̲, ∂_ϑ) = 0 contains −(γ_ϑ/(4Ω²)) ∂_u∂_v b.
Solving the first three for ∂_u∂_vϰ_i and then the fourth for ∂_u∂_v ln Ω, the five equations E′ = 0 are equivalent,
off the axes, to

    ∂_u∂_v Y_l = Ψ_l,      Y := (ln Ω, ϰ_1, ϰ_2, ϰ_3, b),      l = 0, …, 4,                     {#eq:loc-cone-goursat}

where each Ψ_l is a polynomial in e^(±2 ln Ω), e^(±2ϰ_1), e^(±2ϰ_2), e^(±2ϰ_3), b and the derivatives of the Y_l of the
kinds listed below, and, read off from [[eq:loc-cone-frame-ricci]]:

(Ψ1) no Ψ_l contains ∂_u², ∂_v², ∂_u∂_v of any Y_l, or ∂_u b;
(Ψ2) Ψ_0, …, Ψ_3 contain u-derivatives only as ∂_uϰ_1, ∂_uϰ_2, ∂_uϰ_3, each monomial at most one of them, and contain
∂_v∂_ϑ of ln Ω and of the ϰ_i only in monomials with the factor b;
(Ψ3) Ψ_4 contains no v-derivative of ln Ω or of the ϰ_i, contains u-derivatives only as ∂_u and ∂_u∂_ϑ of ln Ω,
ϰ_2, ϰ_3 and ∂_uϰ_1, each monomial at most one of them, contains ∂_v∂_ϑ b only with the factor b, and contains ∂_v b
only in monomials (∂_v b) × (terms with ∂_u ln Ω, ∂_uϰ_i, b, ∂_ϑ b and the ϰ_i);
(Ψ4) each monomial of Ψ_0, …, Ψ_3 contains at most one of ∂_vϰ_1, ∂_vϰ_2, ∂_vϰ_3, ∂_v ln Ω, besides factors ∂_v b,
∂_v∂_ϑ b.

For instance □_g ϰ_2 = 0 reads ∂_u∂_vϰ_2 = −∂_v b ∂_ϑϰ_2 − b ∂_v∂_ϑϰ_2 − ½(tr χ̲ ∂_vϰ_2 + tr χ χ̲_2 − ∂_v b ∂_ϑϰ_2) +
(Ω²/𝒱) ∂_ϑ(𝒱Ω²γ_ϑ⁻¹∂_ϑϰ_2)/Ω², and E(L̲, ∂_ϑ) = 0 reads ∂_u∂_v b = −b ∂_ϑ∂_v b − (L̲ ln(γ_ϑ^(3/2)e^(A_c+A_s)Ω⁻²) +
2∂_ϑ b) ∂_v b + 4Ω²γ_ϑ⁻¹ r̲. The conservation laws are ∂_u ρ_in = −∂_ϑ(b ρ_in) and ∂_v ρ_out = 0.

*N_o.* Let j ≥ 1 and a_0, …, a_(j−1) be found. Apply ∂_u^(j−1) to [[eq:loc-cone-goursat]] and set u = 0, replacing
∂_u^i X by a_i. By (Ψ1)–(Ψ3), u-derivatives of order j enter only through ∂_u^(j−1) of the factors listed there, once
in each monomial, so

    ∂_v a_j^(ϰ_i) = Σ_l M_(il) a_j^(ϰ_l) + h_i,   ∂_v a_j^(ln Ω) = Σ_l M_(0l) a_j^(ϰ_l) + h_0,
    ∂_v a_j^b = M_4 · (a_j^(ln Ω), a_j^(ϰ_l), ∂_ϑ a_j^(ln Ω), ∂_ϑ a_j^(ϰ_2), ∂_ϑ a_j^(ϰ_3)) + h_4,

after substituting the first lines in the second; the coefficients M are smooth functions of a_0 and of its first
derivatives in v and ϑ, and the h are polynomials in a_0, …, a_(j−1) and their derivatives in v and ϑ of order at most
two. This is a system of linear ordinary differential equations in v along each generator, which we solve with the
initial values a_j(0, ϑ) := ∂_u^j b_0(0, ϑ) for the components ln Ω, ϰ_l, b (for b this value is 0): first the
three ϰ-components, then ln Ω, then b. For the densities put a_j^(ρ_in) := −(∂_u^(j−1)∂_ϑ(b ρ_in)) at u = 0, a
polynomial in a_0, …, a_(j−1) and their ϑ-derivatives, and a_j^(ρ_out)(v, ϑ) := ∂_u^j b_0^(ρ_out)(0, ϑ) for all v.

*N_i.* Let k ≥ 1 and b_0, …, b_(k−1) be found. Apply ∂_v^(k−1) to [[eq:loc-cone-goursat]] and set v = 0, where b = ∂_u b
= ∂_ϑ b = 0. By (Ψ3), in the equation for b the v-derivatives of order k enter only through ∂_u∂_v^k b, through
b ∂_ϑ∂_v^k b and 2∂_ϑ b ∂_v^k b, which vanish at v = 0, and through ∂_v^k b times a function of b_0: a linear equation
∂_u b_k^b = M_4′ b_k^b + h_4′. By (Ψ2) and (Ψ4), in the other four the v-derivatives of order k enter through
∂_u∂_v^k(ln Ω, ϰ_l), through ∂_v^k(ln Ω, ϰ_l) once in each monomial, and through ∂_v^k b and ∂_ϑ∂_v^k b; the terms
b ∂_v∂_ϑ(ln Ω, ϰ_l) give no ∂_ϑ∂_v^k(ln Ω, ϰ_l) at v = 0. So with b_k^b known these are linear equations in u for the
ϰ-components and then for ln Ω. We solve them with the initial values b_k(0, ϑ) := ∂_v^k a_0(0, ϑ). For the densities
put b_k^(ρ_out) := 0, and let b_k^(ρ_in) solve ∂_u b_k^(ρ_in) = −(∂_v^k ∂_ϑ(b ρ_in)) at v = 0, whose right side is
−∂_ϑ Σ_(1≤i≤k) (k choose i) b_i^b b_(k−i)^(ρ_in), with the initial value ∂_v^k a_0^(ρ_in)(0, ϑ).

*Vanishing to infinite order.* For X as in the statement, ∂_u^(j−1) of ∂_u∂_v Y − Ψ vanishes at u = 0 for every j ≥ 1,
by the construction on N_o, and ∂_v^(k−1) of it vanishes at v = 0 for every k ≥ 1; the derivatives along N of these
restrictions vanish too. So ∂_u∂_v Y − Ψ vanishes to infinite order on N, and so does E′, which is obtained from it by
multiplying with smooth functions and adding. The conservation laws are the same: at order 0 on N_o, ∂_v ρ_out = 0 is
the constancy of a_0^(ρ_out) along the generators, and on N_i, where b = ∂_ϑ b = 0, ∂_u ρ_in = 0 is that of
b_0^(ρ_in).

(i) For j = 0 or k = 0 the equality holds by the choice of the initial values and of a_0, b_0, which agree on S_c. For
j, k ≥ 1 we use induction on n := j + k. Let c^o_(jk) := ∂_v^k a_j(0, ·) and c^i_(jk) := ∂_u^j b_k(0, ·). For the
components Y_l, c^o_(jk) = ∂_v^(k−1) of the right side of the equation for ∂_v a_j at v = 0, which is the formal mixed
derivative ∂_u^(j−1)∂_v^(k−1)Ψ_l at the corner, expanded by the chain rule into the numbers ∂_ϑ^p c^o_(j′k′); and
c^i_(jk) = ∂_u^(j−1) of the right side of the equation for ∂_u b_k at u = 0, which is the same expansion in the numbers
∂_ϑ^p c^i_(j′k′). By (Ψ1) every Ψ_l holds at most first derivatives in u and in v, so only pairs with j′ + k′ ≤ n − 1
occur, and these agree by induction. For ρ_in and j ≥ 1 both are ∂_u^(j−1)∂_v^k of −∂_ϑ(b ρ_in), expanded in the
same way with j′ ≤ j − 1, k′ ≤ k; for ρ_out both vanish when k ≥ 1.

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
equation holds ∂_ϑ a_j^(ln Ω) and ∂_ϑ a_j^(ϰ_l), in C^(m_0−4j+1), and the densities likewise. On N_i, the equation for
b_k^b holds ∂_ϑ∂_u of b_0, …, b_(k−1) and the initial value ∂_v^k a_0^b(0, ·), so b_k^b − b̊_k^b is bounded in
C^(m_0−4k+2); the other equations hold ∂_ϑ b_k^b, so the other components are bounded in C^(m_0−4k+1).

(iv) Such a solution satisfies E = 0 and the conservation laws on D, hence, by continuity, their derivatives of every
order on N; so its derivatives across N solve the equations above with the same initial values. ∎

**Proposition {#prop:loc-cone-formal}** (The formal solution.) Let the cone data have size at most Λ, equal the
background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], on N_o ∩ {v < v_K} and on N_i ∩ {u < u_K}, where u_K, v_K ∈ (0, ∞],
and let 0 < δ_e ≤ δ_1/4. There are smooth functions Δ = (Δ_l) of (u, v, ϑ) on 𝒮 × [0, π/2] such that, with X̂ := X̊ + Δ,
the metric Ĝ of the form [[eq:loc-double-null]] with the functions X̂, and q̂_A := ρ̂_A/𝒱̂:

(a) Δ vanishes outside {ϑ_a′ ≤ ϑ ≤ ϑ_b′} ∩ ({|u| ≤ 2δ_e, v ≥ −2δ_e} ∪ {|v| ≤ 2δ_e, u ≥ 0}) and where u < u_K and
v < v_K, and ‖Δ‖_(C^(k+2)) ≤ C times the size, C depending only on Λ, δ_e, k and the background;

(b) the derivatives of X̂ across N are the a_j and b_k of [[lem:loc-cone-jets]]; so Ĝ and q̂_A induce the cone data on N,
and Ĝ is a smooth G-invariant Lorentzian metric on 𝒮 × S³, equal to g_e near the axes, for which u and v are null;

(c) E := Ric(Ĝ) − q̂_in dv ⊗ dv − q̂_out du ⊗ du, ∂_u ρ̂_in + ∂_ϑ(b̂ ρ̂_in) and ∂_v ρ̂_out vanish to infinite order on N.

*Proof.* Apply [[lem:loc-cone-borel]] to each component of (a_j − å_j) and (b_k − b̊_k), with Y = [0, π/2], λ_u = l_u +
δ_1, λ_v = l_v + δ_1, r := k + 2, ε_0 := δ_e and γ_0 the size (Δ := 0 if the size is 0); the compatibility at the corner
holds for the data and for the background by [[lem:loc-cone-jets]] (i). (a) follows from parts (a) and (b) there and
[[lem:loc-cone-jets]] (ii), (iii), since m_0 − 4(k + 2) = 2k + 4. (b) The double-null form with Ω̂ > 0 and γ̂_ϑ > 0 is
Lorentzian, with g^(uu) = g^(vv) = 0. (c) E′ and the conservation laws vanish to infinite order on N by
[[lem:loc-cone-jets]]. On N_o, E(∂_v, ∂_v) = E(∂_v, ∂_ϑ) = 0, and on N_i, E(L̲, L̲) = 0, by (ii) of [[def:loc-cone-data]],
these components being expressions in the functions on the edges (on N_i, b̂ = 0 with its derivatives along N_i, so
E(L̲, L̲) there is [[eq:loc-cone-in]] minus q_out). By [[lem:loc-cone-ricci]] (b), div T̂ vanishes to infinite order on N,
and by (c) there tr E does; so div E does, and by [[eq:loc-cone-bianchi]] the three expressions on its right sides, without
the terms ℓ_j(E′), vanish to infinite order on N. With a := E(∂_v, ∂_v), β := E(∂_v, ∂_ϑ), c := E(L̲, L̲):

*On N_o.* We show by induction on j that ∂_u^i a = ∂_u^i β = 0 on N_o for i ≤ j and ∂_u^i c = 0 on N_o for i ≤ j − 1;
this holds for j = 0. Given it for j, apply ∂_u^j to the first identity: on N_o, ∂_v(∂_u^j c) + tr χ ∂_u^j c = 0, the
terms with lower u-derivatives of c vanishing; and ∂_u^j c = 0 at v = 0, since c = 0 on N_i and ∂_u is tangent to N_i. So
∂_u^j c = 0 on N_o. Applying ∂_u^j to the second identity, all terms other than ∂_u^(j+1) β hold ∂_u^i β with i ≤ j or
∂_u^j c, so ∂_u^(j+1) β = 0 on N_o; then the third gives ∂_u^(j+1) a = 0.

*On N_i.* We show by induction on k that ∂_v^i c = 0 on N_i for i ≤ k and ∂_v^i a = ∂_v^i β = 0 on N_i for i ≤ k − 1;
this holds for k = 0. Given it for k, apply ∂_v^k to the second identity: on N_i, where b = 0, ∂_u(∂_v^k β) + (tr χ̲ +
∂_ϑ b) ∂_v^k β = 0, and ∂_v^k β = 0 at u = 0, as β = 0 on N_o; so ∂_v^k β = 0 on N_i. Then ∂_v^k of the third gives
∂_u(∂_v^k a) + tr χ̲ ∂_v^k a = 0 on N_i, with ∂_v^k a = 0 at u = 0, so ∂_v^k a = 0. Finally ∂_v^k of the first gives
∂_v^(k+1) c = 0 on N_i.

So a, β and c, with all their derivatives, vanish on N, and E vanishes to infinite order on N. ∎

