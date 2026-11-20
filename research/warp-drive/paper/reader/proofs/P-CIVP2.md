### Developments of cone data without smallness {#sec:civp-large}

This section removes the smallness from the development of the cone data of [[prop:loc-cones]]
([[pending:civp-tier1-theorem]] proves it for data near the background's). For cone data of any size that equal the
background's outside a band away from the axes, with or without dust, a development in the gauge [[eq:loc-double-null]]
exists on a neighbourhood {min(u, v) ≤ δ} of the two cones, which contains {uv ≤ δ²}; it equals the background outside a
slightly wider band, and it is unique in the gauge among solutions that equal the background near the axes
([[thm:civp-large]]). The number δ depends on the data. The route is that of Cabet, Chruściel and Tagne Wafo [CCTW16].
Off the axes, [[prop:reduction]] turns the class system into a three-dimensional one for the conformal orbit metric h,
two waves ψ and ω and the two densities. In three dimensions the curvature is determined by the Ricci tensor, and the
reduction expresses the Ricci tensor through the densities and the first derivatives of ψ and ω. So in a double-null
frame of h the connection coefficients obey transport equations along the two null directions with no angular
derivative of an unknown on the right, and the waves become first-order systems of the same kind
([[lem:civp-large-frame]]). The resulting evolution system has the doubly-null form of [CCTW16, (2.7)–(2.8)]
([[prop:civp-large-system]]), and once it is localised in angle their theorem ([[thm:std-cctw-existence]],
[[thm:std-cctw-strips]]) gives a solution on two strips along the cones. That this solution solves the Einstein
equations is shown as in the proof of [CCTW16, Theorem 5.3]: the development is built up in the time u + v from local
developments near corner spheres ([[prop:civp-large-corner]]), each of which coincides with the strip solution by an
energy estimate ([[lem:civp-large-energy]]).

*Notation.* The background g0, the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the corner sphere S = 𝒞_out ∩ 𝒞_in and
the gauge [[eq:loc-double-null]] are those of [[sec:loc-cones]]. We fix u1, v1 > 0 such that the background is defined,
in the gauge [[eq:loc-double-null]], on a neighbourhood of Q1 × S³, Q1 := [0, u1] × [0, v1]; there b = 0, γ_ϑ = R²,
A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ), Ω is a function of (u, v), and Ric(g0) = q̊_in dv ⊗ dv + q̊_out du ⊗ du
([[eq:two-dust-limit]]). We fix a band 0 < ϑ_a < ϑ_b < π/2 and put

    η0 := (1/3) min(ϑ_a, π/2 − ϑ_b),      J0 := [ϑ_a − 2η0, ϑ_b + 2η0] ⊂ [η0, π/2 − η0].              {#eq:civp-large-band}

A set D ⊂ Q1 is a *past set* if [0, u] × [0, v] ⊂ D for every (u, v) ∈ D. A *class solution in the gauge* on D × S³ is a
smooth class solution (g, v, u, q_in, q_out) of [[eq:class-system]] with N_f = 2, phases u_1 = v and u_2 = u and
densities q_1 = q_in and q_2 = q_out, whose metric has the form [[eq:loc-double-null]] with Ω, γ_ϑ, b, A_c, A_s smooth
functions of (u, v, ϑ) on D × [0, π/2] (the axes being regular points of the metric, as for g0).

**Definition {#def:civp-large-data}** (Cone data.) *Cone data* consist of smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s
and q_in ≥ 0 of (v, ϑ) on 𝒞_out ∩ (Q1 × S³), and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) on 𝒞_in ∩ (Q1 × S³),
with b = 0 on 𝒞_in, such that:

(i) the two sets of functions agree on S;

(ii) for the metric [[eq:loc-double-null]] that they define, Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on 𝒞_out, and
Ric(∂_u, ∂_u) = q_out on 𝒞_in (each side involves only the functions given on that cone: on 𝒞_out by
[[lem:loc-cone-equations]], on 𝒞_in by (F1′) of [[lem:civp-large-frame]] and [[prop:reduction]], since b vanishes
there);

(iii) they equal the background's outside compact sets K_out ⊂ [0, v1] × (ϑ_a, ϑ_b) and K_in ⊂ [0, u1] × (ϑ_a, ϑ_b).

[[prop:loc-cones]] and its analogue on 𝒞_in with b = 0 there ([[pending:civp-tier1-cin-cones]]) produce cone data from
free data (ℓ_1, ℓ_2, ℓ_3, q_in) on 𝒞_out and (ℓ_1, ℓ_2, ℓ_3, q_out) on 𝒞_in whenever the conformal factor e^ϕ that
they determine stays positive on [0, v1] and on [0, u1]; no smallness is needed for that. Data with q_in = q_out = 0 are
vacuum data.

#### The reduced system in a double-null frame {#sec:civp-large-frame}

Off the axes write a metric of the form [[eq:loc-double-null]] as g = g3 + e^(2A_c) dφ1² + e^(2A_s) dφ2², with
g3 := −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ (dϑ − b du)². With ψ := A_c + A_s, ω := (A_s − A_c)/2 and h := e^(2ψ) g3 as in
[[prop:reduction]],

    h = −2e^(2α) (du ⊗ dv + dv ⊗ du) + e^(2β) (dϑ − b du)²,      α := ψ + ln Ω,      β := ψ + (1/2) ln γ_ϑ.
                                                                                                 {#eq:civp-large-h}

We use the frame

    e3 := e^(−α) (∂_u + b ∂_ϑ),      e4 := e^(−α) ∂_v,      e1 := e^(−β) ∂_ϑ,

for which h(e3, e4) = −2, h(e1, e1) = 1 and all other products vanish: h(e3, e3) = e^(−2α)(e^(2β) b² − 2b e^(2β) b +
b² e^(2β)) = 0, h(e1, e3) = e^(−α−β)(−e^(2β) b + b e^(2β)) = 0, and h(e4, e4) = h(e1, e4) = 0 because h_vv = h_vϑ = 0.
Its *connection coefficients* are

    χ := h(∇_1 e4, e1),   χ̲ := h(∇_1 e3, e1),   η := (1/2) h(e1, ∇_3 e4),   η̲ := (1/2) h(e1, ∇_4 e3),
    ϖ := (1/4) h(e3, ∇_4 e4),   ϖ̲ := (1/4) h(e4, ∇_3 e3),   ζ := (1/2) h(∇_1 e4, e3),

with ∇ the connection of h and ∇_i := ∇_(e_i). We write Ric_ij := Ric[h](e_i, e_j) and, for a function F, e_iF for
its derivative. The *exchange* is the map e3 ↔ e4, χ ↔ χ̲, η ↔ η̲, ϖ ↔ ϖ̲, ζ ↔ −ζ; it maps each definition above to
another one.

**Lemma {#lem:civp-large-frame}** (The double-null frame of h.) (a) The coefficients are

    χ = e4β,   χ̲ = e3β + e^(−α) ∂_ϑb,   ϖ = −(1/2) e4α,   ϖ̲ = −(1/2) e3α,
    ζ = −(1/4) e^(β−2α) ∂_vb,   η = ζ + e1α,   η̲ = −ζ + e1α.                                       {#eq:civp-large-coefficients}

(b) The following hold for every metric of the form [[eq:civp-large-h]], together with their images (F1′)–(F5′) under
the exchange:

    (F1)  e4χ = −χ² − 2ϖχ − Ric_44,
    (F2)  e4η = −Ric_41 − χ(η − η̲),
    (F3)  e3ϖ = 2ϖϖ̲ + (1/2)η̲² − ηη̲ + (1/4)(Ric_34 + Ric_11),
    (F4)  e3χ = 2 e1η + 2η² + 2ϖ̲χ − χχ̲ + Ric_11,
    (F5)  e3η = Ric_31 − 2χ̲η − 4 e1ϖ̲ − 2ϖ̲(η + η̲).                                                {#eq:civp-large-null}

(c) For every function F,

    □_h F = −e3e4F + e1e1F + (2ϖ̲ − (1/2)χ̲) e4F − (1/2)χ e3F + 2η e1F,                              {#eq:civp-large-box}

and the image of the right side under the exchange is also □_h F. For every function q,

    div_h(q h⁻¹dv) = −(1/2) e^(−α) (e3q + χ̲ q),      div_h(q h⁻¹du) = −(1/2) e^(−α) (e4q + χ q).     {#eq:civp-large-dust}

(d) Let g be a metric of the form [[eq:loc-double-null]] off the axes and q a function of (u, v, ϑ). Then
div_g(q g⁻¹du) = e^(2ψ) div_h(q h⁻¹du) and div_g(q g⁻¹dv) = e^(2ψ) div_h(q h⁻¹dv).

In (F1)–(F5) only (F4), (F5) and their images contain an e1-derivative of a connection coefficient; (F1)–(F3) and
(F1′)–(F3′) contain none, and the only curvature in them is the Ricci tensor of h.

*Proof.* *The connection table.* Since u is a null coordinate, h⁻¹du = −(1/2) e^(−α) e4 is the gradient of a solution
of h⁻¹(du, du) = 0, so ∇_(h⁻¹du) h⁻¹du = (1/2) ∇(h⁻¹(du, du)) = 0, and ∇_4 e4 is a multiple of e4; likewise
h⁻¹dv = −(1/2) e^(−α) e3, and ∇_3 e3 is a multiple of e3. (The formulas for h⁻¹du and h⁻¹dv follow from
du(e3) = dv(e4) = e^(−α), du(e4) = dv(e3) = du(e1) = dv(e1) = 0 and h(e3, e4) = −2.) A vector V is −(1/2)h(V, e4) e3 − (1/2)h(V, e3) e4 + h(V, e1) e1. With the
definitions, h(∇_X e_i, e_j) = −h(e_i, ∇_X e_j), h(∇_X e3, e3) = h(∇_X e4, e4) = h(∇_X e1, e1) = 0, and the two
geodesic facts, this gives

    ∇_4e4 = −2ϖ e4,   ∇_4e3 = 2ϖ e3 + 2η̲ e1,   ∇_4e1 = η̲ e4,   ∇_3e3 = −2ϖ̲ e3,   ∇_3e4 = 2ϖ̲ e4 + 2η e1,
    ∇_3e1 = η e3,   ∇_1e4 = χ e1 − ζ e4,   ∇_1e3 = χ̲ e1 + ζ e3,   ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4.   {#eq:civp-large-table}

For instance h(∇_4e3, e4) = −h(e3, ∇_4e4) = −4ϖ, h(∇_4e3, e3) = 0 and h(∇_4e3, e1) = 2η̲, so ∇_4e3 = 2ϖ e3 + 2η̲ e1;
and h(∇_1e1, e4) = −χ, h(∇_1e1, e3) = −χ̲, h(∇_1e1, e1) = 0, so ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4. The table is invariant
under the exchange.

(a) Since ∇ has no torsion, the table gives

    [e4, e3] = 2ϖ e3 − 2ϖ̲ e4 + 2(η̲ − η) e1,   [e4, e1] = (η̲ + ζ) e4 − χ e1,   [e3, e1] = (η − ζ) e3 − χ̲ e1.

From the coordinate expressions, with ∂_v and ∂_u + b∂_ϑ and ∂_ϑ commuting up to [∂_v, ∂_u + b∂_ϑ] = (∂_vb)∂_ϑ and
[∂_u + b∂_ϑ, ∂_ϑ] = −(∂_ϑb)∂_ϑ,

    [e4, e3] = −(e4α) e3 + (e3α) e4 + e^(β−2α)(∂_vb) e1,   [e4, e1] = (e1α) e4 − (e4β) e1,
    [e3, e1] = (e1α) e3 − (e3β + e^(−α)∂_ϑb) e1.

Comparing coefficients gives ϖ, ϖ̲, χ, χ̲, η̲ + ζ = e1α = η − ζ, and η − η̲ = −(1/2) e^(β−2α) ∂_vb, which is ζ by the
two previous relations. This is [[eq:civp-large-coefficients]]. We use below

    [e4, e3] = 2ϖ e3 − 2ϖ̲ e4 − 4ζ e1,   [e4, e1] = (e1α) e4 − χ e1,   [e3, e1] = (e1α) e3 − χ̲ e1,   e1α = (η + η̲)/2.

*The Ricci tensor in the frame.* With the dual frame, Ric(X, Y) = h(R(e1, X)Y, e1) − (1/2)h(R(e3, X)Y, e4) −
(1/2)h(R(e4, X)Y, e3), where R(X, Y) = ∇_X∇_Y − ∇_Y∇_X − ∇_[X,Y]. By the antisymmetries of h(R(X, Y)Z, W) in (X, Y)
and in (Z, W), the pair symmetry and the first Bianchi identity, this gives

    Ric_44 = h(R(e1, e4)e4, e1),   Ric_41 = −(1/2) h(R(e4, e3)e4, e1),   Ric_11 = h(R(e3, e1)e4, e1),
    Ric_34 + Ric_11 = (1/2) K,   K := h(R(e3, e4)e4, e3).

Indeed Ric_11 = −(1/2)(h(R(e3, e1)e1, e4) + h(R(e4, e1)e1, e3)), and by the pair symmetry and the Bianchi identity both
terms equal L := h(R(e1, e3)e4, e1), so Ric_11 = −L = h(R(e3, e1)e4, e1); and Ric_34 = h(R(e1, e3)e4, e1) −
(1/2)h(R(e4, e3)e4, e3) = L + (1/2)K. For Ric_41 the terms h(R(e1, e4)e1, e1) and h(R(e4, e4)e1, e3) vanish and
h(R(e3, e4)e1, e4) = −h(R(e3, e4)e4, e1) = h(R(e4, e3)e4, e1).

(F1) By the table, ∇_4∇_1e4 = (e4χ) e1 + χη̲ e4 − (e4ζ) e4 + 2ζϖ e4, ∇_1∇_4e4 = −2(e1ϖ) e4 − 2ϖ(χ e1 − ζ e4) and
∇_[e4,e1] e4 = −2ϖ(η̲ + ζ) e4 − χ(χ e1 − ζ e4). The e1-component of R(e4, e1)e4 is therefore e4χ + 2ϖχ + χ², and
Ric_44 = −h(R(e4, e1)e4, e1).

(F2) 2e4η = e4 h(∇_3e4, e1) = h(∇_4∇_3e4, e1) + h(∇_3e4, ∇_4e1), and the last term vanishes since ∇_4e1 = η̲ e4 and
h(e4, e1) = h(e4, e4) = 0. Here ∇_4∇_3e4 = R(e4, e3)e4 + ∇_3∇_4e4 + ∇_[e4,e3] e4; the e1-component of ∇_3∇_4e4 =
∇_3(−2ϖ e4) is −4ϖη, and that of ∇_[e4,e3] e4 = 2ϖ∇_3e4 − 2ϖ̲∇_4e4 − 4ζ∇_1e4 is 4ϖη − 4ζχ. So
2e4η = h(R(e4, e3)e4, e1) − 4ζχ = −2Ric_41 − 2χ(η − η̲).

(F3) 4e3ϖ = e3 h(e3, ∇_4e4) = h(∇_3e3, ∇_4e4) + h(e3, ∇_3∇_4e4), and h(∇_3e3, ∇_4e4) = 4ϖϖ̲ h(e3, e4) = −8ϖϖ̲. Write
∇_3∇_4e4 = R(e3, e4)e4 + ∇_4∇_3e4 + ∇_[e3,e4] e4. Then h(e3, R(e3, e4)e4) = K; h(e3, ∇_4∇_3e4) = e4 h(e3, ∇_3e4) −
h(∇_4e3, ∇_3e4) = −4e4ϖ̲ + 8ϖϖ̲ − 4ηη̲, since h(e3, ∇_3e4) = −h(∇_3e3, e4) = −4ϖ̲; and with [e3, e4] = −2ϖ e3 + 2ϖ̲ e4
+ 4ζ e1, the e4-coefficient of ∇_[e3,e4] e4 = −2ϖ∇_3e4 + 2ϖ̲∇_4e4 + 4ζ∇_1e4 is −8ϖϖ̲ − 4ζ², so that
h(e3, ∇_[e3,e4] e4) = 16ϖϖ̲ + 8ζ². Hence

    e3ϖ + e4ϖ̲ = (1/4) K + 4ϖϖ̲ + 2ζ² − ηη̲.

On the other hand ϖ = −(1/2)e4α and ϖ̲ = −(1/2)e3α give e3ϖ − e4ϖ̲ = −(1/2)[e3, e4]α = −(1/2)(4ϖϖ̲ − 4ϖ̲ϖ + 4ζ e1α)
= −2ζ e1α = −(1/2)(η² − η̲²). Half the sum of the two relations, with ζ = (η − η̲)/2 and K = 2(Ric_34 + Ric_11), is
(F3).

(F4) e3χ = h(∇_3∇_1e4, e1) + h(∇_1e4, ∇_3e1) = h(∇_3∇_1e4, e1) + 2ζη, since h(χ e1 − ζ e4, η e3) = 2ζη. Here
∇_3∇_1e4 = R(e3, e1)e4 + ∇_1∇_3e4 + ∇_[e3,e1] e4. The e1-component of ∇_1∇_3e4 = ∇_1(2ϖ̲ e4 + 2η e1) is 2ϖ̲χ + 2e1η,
and that of ∇_[e3,e1] e4 = (η − ζ)∇_3e4 − χ̲∇_1e4 is 2η(η − ζ) − χχ̲. With h(R(e3, e1)e4, e1) = Ric_11 this is (F4).

(F5) By (a), e3η + e3η̲ = 2e3e1α = 2e1e3α + 2[e3, e1]α = −4e1ϖ̲ + 2(e1α)(e3α) − 2χ̲ e1α = −4e1ϖ̲ − (2ϖ̲ + χ̲)(η + η̲).
Subtracting (F2′), e3η̲ = −Ric_31 − χ̲(η̲ − η), gives (F5).

The images under the exchange hold by the same computations with the roles of e3 and e4 exchanged, since the table and
the formula for Ric are invariant; for (F3′) and (F5′) one uses ϖ = −(1/2)e4α, ϖ̲ = −(1/2)e3α and e1α = (η + η̲)/2,
which are also invariant.

(c) □_h F = h^(ab)∇_a∇_bF = −(1/2)(∇²F(e3, e4) + ∇²F(e4, e3)) + ∇²F(e1, e1), with ∇²F(X, Y) = X(YF) − (∇_XY)F. By the
table, ∇²F(e3, e4) = e3e4F − 2ϖ̲ e4F − 2η e1F, ∇²F(e4, e3) = e4e3F − 2ϖ e3F − 2η̲ e1F and ∇²F(e1, e1) = e1e1F −
(1/2)χ e3F − (1/2)χ̲ e4F. Replacing e4e3F by e3e4F + [e4, e3]F = e3e4F + 2ϖ e3F − 2ϖ̲ e4F + 2(η̲ − η) e1F gives
[[eq:civp-large-box]]; replacing instead e3e4F by e4e3F − [e4, e3]F gives its image. For the densities, h⁻¹dv =
−(1/2)e^(−α) e3, so div_h(q h⁻¹dv) = −(1/2)(e3(e^(−α) q) + e^(−α) q div_h e3), and div_h e3 = −(1/2)h(∇_3e3, e4) −
(1/2)h(∇_4e3, e3) + h(∇_1e3, e1) = −2ϖ̲ + χ̲; with e3(e^(−α)) = 2ϖ̲ e^(−α) this is the first formula, and the second is
its image.

(d) In coordinates (u, v, ϑ, φ1, φ2), √|det g| = e^ψ √|det g3| and √|det h| = e^(3ψ) √|det g3|, and since q and u do
not depend on φ1, φ2, g⁻¹du = g3⁻¹du = e^(2ψ) h⁻¹du has no φ-components. Hence div_g(q g⁻¹du) = e^(−ψ) |det g3|^(−1/2)
∂_a(e^ψ |det g3|^(1/2) q e^(2ψ) (h⁻¹du)^a) = e^(−ψ) |det g3|^(−1/2) ∂_a(|det h|^(1/2) q (h⁻¹du)^a) = e^(2ψ)
div_h(q h⁻¹du), and the same for dv. ∎

**Lemma {#lem:civp-large-reduction}** (The class system off the axes.) Let g be a metric of the form
[[eq:loc-double-null]] on an open set of D × (0, π/2) × T², D ⊂ Q1, and q_in, q_out ≥ 0 functions of (u, v, ϑ), and let
h, ψ, ω be as in [[eq:civp-large-h]]. Then (g, v, u, q_in, q_out) solves [[eq:class-system]] if and only if

    Ric[h] = q_in dv ⊗ dv + q_out du ⊗ du + (3/2) dψ ⊗ dψ + 2 dω ⊗ dω,      □_hψ = □_hω = 0,
    e3q_in = −χ̲ q_in,      e4q_out = −χ q_out.                                                    {#eq:civp-large-reduced}

*Proof.* g⁻¹(du, du) = g⁻¹(dv, dv) = 0 holds for every metric of the form [[eq:loc-double-null]]. T := q_in dv ⊗ dv +
q_out du ⊗ du has no φ-components, so in the notation of [[prop:reduction]] the equations Ric(g) = T are R11 = R22 = 0,
vanishing mixed components and Ric[g]_ab = T_ab on the orbit space; the mixed components vanish for every class metric
([[lem:warped-ricci]]). By [[prop:reduction]], R11 = R22 = 0 is equivalent to □_hψ = □_hω = 0, and then
Ric[h]_ab = Ric[g]_ab + (3/2)∂_aψ∂_bψ + 2∂_aω∂_bω, so Ric[g] = T on the orbit space is the first equation. The dust
equations are div_g(q_in g⁻¹dv) = 0 and div_g(q_out g⁻¹du) = 0, equivalent by [[lem:civp-large-frame]] (d) and
[[eq:civp-large-dust]] to the last two. ∎

In the frame, T(e4, e4) = e^(−2α) q_in, T(e3, e3) = e^(−2α) q_out and the other components of T vanish, since
dv(e4) = du(e3) = e^(−α) and dv(e3) = du(e4) = dv(e1) = du(e1) = 0. Only Ric_44 and Ric_33 carry a density.

*The evolution system.* Its unknown is f = (f₃, f₄), in the notation of [CCTW16] f = (ϕ, ψ) with ϕ = f₃ and ψ = f₄
(the letters f₃, f₄ avoid a clash with the function ψ), with

    f₃ := (χ̲, η̲, ϖ, q_in, ψ°, ψ_4, ψ_1, ω°, ω_4, ω_1),
    f₄ := (α, β, b, χ, η, ϖ̲, q_out, ψ, ψ_3, ψ′_1, ω, ω_3, ω′_1),

twenty-three real functions of (u, v, ϑ). For Ψ ∈ {ψ, ω}, the unknowns Ψ°, Ψ_4, Ψ_1, Ψ_3, Ψ′_1 stand for Ψ, e4Ψ, e1Ψ, e3Ψ
and e1Ψ; the others for the quantities of the same name. We put D_3 := ∂_u + b∂_ϑ, k := e^(α−β) and

    M_44 := e^(−2α) q_in + (3/2)ψ_4² + 2ω_4²,      M_33 := e^(−2α) q_out + (3/2)ψ_3² + 2ω_3²,
    M_34 := (3/2)ψ_3ψ_4 + 2ω_3ω_4,   M_41 := (3/2)ψ_4ψ′_1 + 2ω_4ω′_1,   M_31 := (3/2)ψ_3ψ_1 + 2ω_3ω_1,
    M_11 := (3/2)ψ′_1² + 2ω′_1²,                                                                  {#eq:civp-large-m}

the frame components of q_in dv² + q_out du² + (3/2)dψ² + 2dω² written with the unknowns. The *evolution system*,
each equation multiplied by e^α, is, for Ψ ∈ {ψ, ω},

    ∂_vα = −2e^α ϖ,   ∂_vβ = e^α χ,   ∂_vb = −2e^(2α−β) (η − η̲),
    ∂_vχ = −e^α (χ² + 2ϖχ + M_44),   ∂_vη = −e^α (M_41 + χ(η − η̲)),
    ∂_vϖ̲ = e^α (2ϖϖ̲ + (1/2)η² − ηη̲ + (1/4)(M_34 + M_11)),   ∂_vq_out = −e^α χ q_out,   ∂_vΨ = e^α Ψ_4,
    ∂_vΨ_3 − k ∂_ϑΨ_1 = e^α ((2ϖ − (1/2)χ)Ψ_3 − (1/2)χ̲Ψ_4 + 2η̲Ψ_1),
    ∂_vΨ′_1 − k ∂_ϑΨ_4 = e^α ((1/2)(η + η̲)Ψ_4 − χΨ′_1),
    D_3χ̲ = −e^α (χ̲² + 2ϖ̲χ̲ + M_33),   D_3η̲ = −e^α (M_31 + χ̲(η̲ − η)),
    D_3ϖ = e^α (2ϖϖ̲ + (1/2)η̲² − ηη̲ + (1/4)(M_34 + M_11)),   D_3q_in = −e^α χ̲ q_in,   D_3Ψ° = e^α Ψ_3,
    D_3Ψ_4 − k ∂_ϑΨ′_1 = e^α ((2ϖ̲ − (1/2)χ̲)Ψ_4 − (1/2)χΨ_3 + 2ηΨ′_1),
    D_3Ψ_1 − k ∂_ϑΨ_3 = e^α ((1/2)(η + η̲)Ψ_3 − χ̲Ψ_1).                                           {#eq:civp-large-system}

The first ten lines have ∂_v and govern f₄, the last seven have D_3 and govern f₃.

**Proposition {#prop:civp-large-system}** (The doubly-null form.) Write [[eq:civp-large-system]] as A^u∂_uf + A^v∂_vf +
A^ϑ∂_ϑf = G(f) on R² × Y, Y an interval or a circle, with the Euclidean scalar product on ℝ²³ and the flat connection
∂. Then A^u, A^v, A^ϑ are symmetric and smooth functions of f, G is a smooth function of f, and

    A^u = diag(I₁₀, 0),      A^v = diag(0, I₁₃),      A^ϑ = (b I₁₀, Q; Qᵀ, 0),                           {#eq:civp-large-form}

in the splitting f = (f₃, f₄), where the 10 × 13 matrix Q has exactly four nonzero entries, each equal to −k = −e^(α−β),
at the pairs (ψ_4, ψ′_1), (ψ_1, ψ_3), (ω_4, ω′_1), (ω_1, ω_3), so that |Q| = e^(α−β) in the operator norm. In
particular the system has the form (2.7)–(2.8) of [CCTW16] ([[thm:std-cctw-existence]]), with A^u_ϕϕ = I₁₀ > 0 and
A^v_ψψ = I₁₃ > 0, the scalar product and the connection preserving the splitting. Moreover:

(a) if (g, v, u, q_in, q_out) is a class solution in the gauge on D × S³, its *reduced fields* (the connection
coefficients of h, the densities, α, β, b, and Ψ° = Ψ, Ψ_4 = e4Ψ, Ψ_3 = e3Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}) solve
[[eq:civp-large-system]] on D × (0, π/2);

(b) conversely, let f be a smooth solution of [[eq:civp-large-system]] on an open set U ⊂ D × (0, π/2) that is
*geometric* there: χ, χ̲, η, η̲, ϖ, ϖ̲ are the connection coefficients of the metric h of [[eq:civp-large-h]] built from
(α, β, b), Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ, and Ric[h] equals the tensor with the frame components
[[eq:civp-large-m]]. Then g := e^(−2ψ) h + e^(ψ−2ω) dφ1² + e^(ψ+2ω) dφ2², with v, u, q_in, q_out, is a solution of
[[eq:class-system]] on U × T², of the form [[eq:loc-double-null]] with Ω = e^(α−ψ), γ_ϑ = e^(2β−2ψ), A_c = (ψ − 2ω)/2,
A_s = (ψ + 2ω)/2.

*Proof.* The coefficients of the derivatives are read off [[eq:civp-large-system]]: each f₃-equation has the operator
D_3 = ∂_u + b∂_ϑ on its own unknown and no ∂_v, each f₄-equation has ∂_v on its own unknown and no ∂_u, and the only
other derivatives are −k∂_ϑΨ_1 in the Ψ_3-equation and −k∂_ϑΨ_3 in the Ψ_1-equation, −k∂_ϑΨ_4 in the Ψ′_1-equation and
−k∂_ϑΨ′_1 in the Ψ_4-equation. So A^ϑ is symmetric with the stated blocks, and A^u, A^v are as stated. The coefficients
and G are polynomials in f, e^(±α), e^(±β), hence smooth for all values of f; positivity of A^u_ϕϕ, A^v_ψψ needs no
restriction on f.

(a) Multiplied by e^(−α), the equations are, line by line: [[eq:civp-large-coefficients]] for ϖ, χ and ζ = (η − η̲)/2;
(F1), (F2), (F3′) and the second formula of [[eq:civp-large-dust]] with [[lem:civp-large-reduction]]; e4Ψ = Ψ_4;
[[eq:civp-large-box]] (image) with □_hΨ = 0; the commutator [e4, e1]Ψ = (e1α) e4Ψ − χ e1Ψ with e1α = (η + η̲)/2; then
(F1′), (F2′), (F3) and the first formula of [[eq:civp-large-dust]]; e3Ψ = Ψ_3; [[eq:civp-large-box]] with □_hΨ = 0;
and [e3, e1]Ψ = (e1α) e3Ψ − χ̲ e1Ψ. In each, Ric[h] is replaced by the tensor of [[eq:civp-large-m]], which is the right
side of the first equation of [[eq:civp-large-reduced]] in the frame.

(b) By hypothesis the first equation of [[eq:civp-large-reduced]] holds; the equations of [[eq:civp-large-system]] for
Ψ_3 and Ψ_4, with the geometric identifications and [[eq:civp-large-box]], give □_hψ = □_hω = 0; those for q_in and
q_out give the dust equations. [[lem:civp-large-reduction]] concludes, and [[eq:civp-large-h]] gives the form. ∎

The equations for χ, η, ϖ̲, χ̲, η̲, ϖ are (F1), (F2), (F3′), (F1′), (F2′), (F3): each connection coefficient is
transported along e3 or e4, with no angular derivative of an unknown, and the densities enter only the two Raychaudhuri
equations, through M_44 and M_33. The wave block is the first-order form of [CCTW16, (4.47)–(4.50), p. 47], with their
ℓ and ω in the roles of e3 and e4. The equations (F4), (F5), their images and the relations of
[[eq:civp-large-coefficients]] for χ̲, ϖ̲ and η + η̲ are not part of the system; they hold for the reduced fields of a
solution, and they determine the data on the cones.

#### Data on the two cones {#sec:civp-large-data}

**Lemma {#lem:civp-large-data}** (The data of the evolution system.) (a) Let R = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ Q1
and let g, g′ be class solutions in the gauge on neighbourhoods of the two edges N_o := {u_c} × [v_c, v_c + l_v] and
N_i := [u_c, u_c + l_u] × {v_c} (times S³) that induce the same functions Ω, γ_ϑ, b, A_c, A_s, q_in on N_o and the same
Ω, γ_ϑ, b, A_c, A_s, q_out on N_i. Then their reduced fields have the same f₃-components on N_o and the same
f₄-components on N_i. More precisely, for the reduced fields of a class solution in the gauge: the values at the corner
sphere of all reduced fields are given by [[eq:civp-large-coefficients]] in the functions on N_o and N_i near it; on
N_o the f₃-components other than χ̲ are given by [[eq:civp-large-coefficients]] in the functions on N_o, and χ̲ solves
(F4′) along N_o with M_11 in place of Ric_11; on N_i the f₄-components other than η and χ are given by
[[eq:civp-large-coefficients]] in the functions on N_i, and η and χ solve (F5) and (F4) along the integral curves of e3
in N_i with M_31, M_11 in place of Ric_31, Ric_11.

(b) Let cone data be given. Define on 𝒞_out, from its functions and with α, β, ψ, ω as in [[eq:civp-large-h]],

    ϖ := −(1/2) e4α,   η̲ := (1/4) e^(β−2α) ∂_vb + e1α,   Ψ° := Ψ,   Ψ_4 := e4Ψ,   Ψ_1 := e1Ψ,

q_in as given, and χ̲ the solution of the linear equation (F4′), e4χ̲ = 2e1η̲ + 2η̲² + 2ϖχ̲ − χχ̲ + M_11 with χ := e4β and
M_11 := (3/2)(e1ψ)² + 2(e1ω)², whose value at v = 0 is e^(−α)∂_uβ computed on 𝒞_in. Define on 𝒞_in, where b = 0 and
e3 = e^(−α)∂_u,

    ϖ̲ := −(1/2) e3α,   Ψ := Ψ,   Ψ_3 := e3Ψ,   Ψ′_1 := e1Ψ,

α, β, b = 0 and q_out as given, η the solution of the linear equation (F5), e3η = M_31 − 2χ̲η − 4e1ϖ̲ − 4ϖ̲ e1α with
χ̲ := e3β and M_31 := (3/2)e3ψ e1ψ + 2e3ω e1ω, whose value at u = 0 is (−1/4) e^(β−2α)∂_vb + e1α computed on 𝒞_out, and
χ the solution of the linear equation (F4), e3χ = 2e1η + 2η² + 2ϖ̲χ − χχ̲ + M_11, whose value at u = 0 is e4β computed
on 𝒞_out. Let f̄₃ be the first list on 𝒞_out and f̄₄ the second on 𝒞_in. Then:

(i) the restriction of [[eq:civp-large-system]] to 𝒞_out, the f₄-equations with f₃ = f̄₃, with the values of f̄₄ at S
as initial values, has a solution on all of 𝒞_out ∩ (Q1 × (0, π/2)), and the restriction to 𝒞_in, the f₃-equations
with f₄ = f̄₄, with the values of f̄₃ at S, has one on all of 𝒞_in ∩ (Q1 × (0, π/2));

(ii) f̄ and the two solutions of (i) equal the background's reduced fields at every point with ϑ ∉ (ϑ_a, ϑ_b);

(iii) the reduced fields of every class solution in the gauge on D × S³, D ⊂ Q1 a past set, that induces the cone data
have f₃ = f̄₃ on 𝒞_out ∩ D and f₄ = f̄₄ on 𝒞_in ∩ D, and solve the two restricted problems of (i) there.

*Proof.* (a) On N_o the fields e4 and e1 are tangent, and on N_i the fields e3 and e1 are. So on N_o the components ϖ,
η̲ = −ζ + e1α (by [[eq:civp-large-coefficients]], ζ holding ∂_vb), q_in, Ψ°, Ψ_4, Ψ_1 of either solution are given by
the induced functions, and χ̲ solves (F4′) along the generators of N_o, with Ric_11 = M_11 by
[[lem:civp-large-reduction]], a linear equation whose coefficients are given by the induced functions; its value at
the corner is e3β + e^(−α)∂_ϑb, given by the functions on N_i. On N_i, α, β, b, ϖ̲, q_out, Ψ, Ψ_3, Ψ′_1 are given by
the induced functions, and η and χ solve (F5) and (F4) along the integral curves of e3, with Ric_31 = M_31 and
Ric_11 = M_11, linear transport equations with initial values at u = u_c given by the functions on N_o (η = ζ + e1α
and χ = e4β there). Each integral curve of D_3 = ∂_u + b∂_ϑ in N_i starts on the corner circle, so these values are
determined.

(b) (iii) is (a) for g and the data, together with [[prop:civp-large-system]] (a); the values at u = 0 or v = 0 used in
(b) are those of the reduced fields at S. For (i) on 𝒞_out, take for (α, β, b, χ, η, Ψ, Ψ′_1) the functions given by
the data, with χ := e4β, η := ζ + e1α, ζ := −(1/4)e^(β−2α)∂_vb and Ψ′_1 := e1Ψ. They solve the corresponding equations of [[eq:civp-large-system]]: those for α, β, b, Ψ by [[eq:civp-large-coefficients]];
that for χ by (F1) and the constraint Ric(∂_v, ∂_v) = q_in, which by [[prop:reduction]] (the term with R11, R22 being
multiplied by g3(∂_v, ∂_v) = 0) reads Ric[h](∂_v, ∂_v) = q_in + (3/2)(∂_vψ)² + 2(∂_vω)², that is Ric_44 = M_44; that
for η by (F2) and the constraint Ric(∂_v, ∂_ϑ) = 0, which reads Ric_41 = M_41 (g3(∂_v, ∂_ϑ) = 0); and that for Ψ′_1 by
the commutator [e4, e1]. The remaining equations, for Ψ_3, then ϖ̲, then q_out, are linear in these unknowns with
coefficients defined on all of 𝒞_out, so they have solutions there. On 𝒞_in, take χ̲ := e3β, η̲ := 2e1α − η, Ψ° := Ψ and
Ψ_1 := e1Ψ. The equation for χ̲ holds by (F1′) and the constraint Ric(∂_u, ∂_u) = q_out (g3(∂_u, ∂_u) = γ_ϑ b² = 0 on
𝒞_in), that for Ψ°, Ψ_1 by the definitions and [e3, e1]; that for η̲ holds because, by the equation defining η and
2e3e1α = −4e1ϖ̲ − (2ϖ̲ + χ̲)(η + η̲) (proof of (F5)), D_3η̲ = e^α(2e3e1α − e3η) = −e^α(M_31 + χ̲(η̲ − η)). The equations
for Ψ_4, then ϖ, then q_in are linear and have solutions on all of 𝒞_in. In each case the initial values at S are those
of f̄, so these are the solutions of (i).

(ii) Every formula and every coefficient of the equations above at an angle ϑ is built from the functions of the data
and their derivatives at ϑ, and so are the initial values at S; the equations are ordinary differential equations
along the lines {ϑ = const}, since b = 0 on 𝒞_in and the f₄-equations contain no ∂_ϑ of an f₄-unknown. At ϑ ∉ (ϑ_a,
ϑ_b) the data are the background's on a neighbourhood of ϑ, the background's reduced fields solve all the equations
used ([[prop:civp-large-system]] (a)), and by uniqueness for these equations f̄ and the solutions of (i) are the
background's there.

(a) also gives the form in which it is used below: the f₃-components on N_o are the formulas above in the functions on
N_o together with the solution of (F4′) along N_o, and the f₄-components on N_i are the formulas in the functions on
N_i together with the solutions of (F5) and (F4) along N_i; the only further input is the value at the corner sphere
of all reduced fields, which [[eq:civp-large-coefficients]] gives from the functions on N_o and N_i near the corner. ∎
