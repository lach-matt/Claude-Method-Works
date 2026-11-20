### Developments of cone data without smallness {#sec:civp-large}

This section develops the cone data of [[prop:loc-cones]] without smallness; for data near the background's the
development is [[pending:civp-tier1-theorem]]. For cone data of any size that equal the background's outside a band
away from the axes, with or without dust, a development in the gauge [[eq:loc-double-null]] exists on a neighbourhood
{min(u, v) ≤ δ} of the two cones, which contains {uv ≤ δ²}; it equals the background outside a slightly wider band, and
it is unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]). The number δ
depends on the data. The route is that of Cabet, Chruściel and Tagne Wafo [CCTW16]. Off the axes, [[prop:reduction]]
turns the class system into a three-dimensional one for the conformal orbit metric h, two waves ψ and ω and the two
densities. In three dimensions the curvature is determined by the Ricci tensor, and the reduction expresses the Ricci
tensor through the densities and the first derivatives of ψ and ω. So in a double-null frame of h the connection
coefficients obey transport equations along the two null directions with no angular derivative of an unknown on the
right, and the waves become first-order systems of the same kind ([[lem:civp-large-frame]]). The resulting evolution
system has the doubly-null form of [CCTW16, (2.7)–(2.8)] ([[prop:civp-large-system]]), and once it is localised in
angle their theorem ([[thm:std-cctw-existence]], [[thm:std-cctw-strips]]) gives a solution on two strips along the
cones. That this solution solves the Einstein equations is shown as in the proof of [CCTW16, Theorem 5.3]: the
development is built up in the time u + v from local developments near corner spheres ([[prop:civp-large-corner]]),
each of which coincides with the strip solution by an energy estimate ([[lem:civp-large-energy]]).

*Notation.* The background g0, the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the corner sphere S = 𝒞_out ∩ 𝒞_in and
the gauge [[eq:loc-double-null]] are those of [[sec:loc-cones]]. We fix u1, v1 > 0 such that the background is defined,
in the gauge [[eq:loc-double-null]], on a neighbourhood of Q1 × S³, Q1 := [0, u1] × [0, v1]; there b = 0, γ_ϑ = R²,
A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ), Ω is a function of (u, v), and Ric(g0) = q̊_in dv ⊗ dv + q̊_out du ⊗ du
([[eq:two-dust-limit]]). We fix a band 0 < ϑ_a < ϑ_b < π/2 and put

    η0 := (1/3) min(ϑ_a, π/2 − ϑ_b),      J0 := [ϑ_a − 2η0, ϑ_b + 2η0] ⊂ [η0, π/2 − η0].  {#eq:civp-large-band}

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
    ζ = −(1/4) e^(β−2α) ∂_vb,   η = ζ + e1α,   η̲ = −ζ + e1α.  {#eq:civp-large-coefficients}

(b) The following hold for every metric of the form [[eq:civp-large-h]], together with their images (F1′)–(F5′) under
the exchange:

    (F1)  e4χ = −χ² − 2ϖχ − Ric_44,
    (F2)  e4η = −Ric_41 − χ(η − η̲),
    (F3)  e3ϖ = 2ϖϖ̲ + (1/2)η̲² − ηη̲ + (1/4)(Ric_34 + Ric_11),
    (F4)  e3χ = 2 e1η + 2η² + 2ϖ̲χ − χχ̲ + Ric_11,
    (F5)  e3η = Ric_31 − 2χ̲η − 4 e1ϖ̲ − 2ϖ̲(η + η̲).  {#eq:civp-large-null}

(c) For every function F,

    □_h F = −e3e4F + e1e1F + (2ϖ̲ − (1/2)χ̲) e4F − (1/2)χ e3F + 2η e1F,                              {#eq:civp-large-box}

and the image of the right side under the exchange is also □_h F. For every function q,

    div_h(q h⁻¹dv) = −(1/2) e^(−α) (e3q + χ̲ q),      div_h(q h⁻¹du) = −(1/2) e^(−α) (e4q + χ q).  {#eq:civp-large-dust}

(d) Let g be a metric of the form [[eq:loc-double-null]] off the axes and q a function of (u, v, ϑ). Then
div_g(q g⁻¹du) = e^(2ψ) div_h(q h⁻¹du) and div_g(q g⁻¹dv) = e^(2ψ) div_h(q h⁻¹dv).

In (F1)–(F5) only (F4), (F5) and their images contain an e1-derivative of a connection coefficient; (F1)–(F3) and
(F1′)–(F3′) contain none, and the only curvature in them is the Ricci tensor of h.

*Proof.* *The connection table.* Since u is a null coordinate, h⁻¹du = −(1/2) e^(−α) e4 is the gradient of a solution
of h⁻¹(du, du) = 0, so ∇_(h⁻¹du) h⁻¹du = (1/2) ∇(h⁻¹(du, du)) = 0, and ∇_4 e4 is a multiple of e4; likewise h⁻¹dv =
−(1/2) e^(−α) e3, and ∇_3 e3 is a multiple of e3. (The formulas for h⁻¹du and h⁻¹dv follow from du(e3) = dv(e4) =
e^(−α), du(e4) = dv(e3) = du(e1) = dv(e1) = 0 and h(e3, e4) = −2.) A vector V is −(1/2)h(V, e4) e3 − (1/2)h(V, e3) e4 +
h(V, e1) e1. With the definitions, h(∇_X e_i, e_j) = −h(e_i, ∇_X e_j), h(∇_X e3, e3) = h(∇_X e4, e4) = h(∇_X e1, e1) =
0, and the two geodesic facts, this gives

    ∇_4e4 = −2ϖ e4,   ∇_4e3 = 2ϖ e3 + 2η̲ e1,   ∇_4e1 = η̲ e4,   ∇_3e3 = −2ϖ̲ e3,   ∇_3e4 = 2ϖ̲ e4 + 2η e1,
    ∇_3e1 = η e3,   ∇_1e4 = χ e1 − ζ e4,   ∇_1e3 = χ̲ e1 + ζ e3,   ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4.
                                                                                                   {#eq:civp-large-table}

For instance h(∇_4e3, e4) = −h(e3, ∇_4e4) = −4ϖ, h(∇_4e3, e3) = 0 and h(∇_4e3, e1) = 2η̲, so ∇_4e3 = 2ϖ e3 + 2η̲ e1;
and h(∇_1e1, e4) = −χ, h(∇_1e1, e3) = −χ̲, h(∇_1e1, e1) = 0, so ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4. The table is invariant
under the exchange.

(a) Since ∇ has no torsion, the table gives

    [e4, e3] = 2ϖ e3 − 2ϖ̲ e4 + 2(η̲ − η) e1,   [e4, e1] = (η̲ + ζ) e4 − χ e1,   [e3, e1] = (η − ζ) e3 − χ̲ e1.

From the coordinate expressions, with ∂_v and ∂_u + b∂_ϑ and ∂_ϑ commuting up to [∂_v, ∂_u + b∂_ϑ] = (∂_vb)∂_ϑ and
[∂_u + b∂_ϑ, ∂_ϑ] = −(∂_ϑb)∂_ϑ,

    [e4, e3] = −(e4α) e3 + (e3α) e4 + e^(β−2α)(∂_vb) e1,   [e4, e1] = (e1α) e4 − (e4β) e1,
    [e3, e1] = (e1α) e3 − (e3β + e^(−α)∂_ϑb) e1.

Comparing coefficients gives ϖ, ϖ̲, χ, χ̲, η̲ + ζ = e1α = η − ζ, and 2(η̲ − η) = e^(β−2α) ∂_vb; since η − η̲ = 2ζ by
the previous relation, ζ = −(1/4) e^(β−2α) ∂_vb. This is [[eq:civp-large-coefficients]]. We use below

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
h(∇_4e3, ∇_3e4) = −4e4ϖ̲ + 8ϖϖ̲ − 4ηη̲, since h(e3, ∇_3e4) = −h(∇_3e3, e4) = −4ϖ̲; and with [e3, e4] = −2ϖ e3 + 2ϖ̲
e4 + 4ζ e1, the e4-coefficient of ∇_[e3,e4] e4 = −2ϖ∇_3e4 + 2ϖ̲∇_4e4 + 4ζ∇_1e4 is −8ϖϖ̲ − 4ζ², so that h(e3, ∇_[e3,e4]
e4) = 16ϖϖ̲ + 8ζ². Hence

    e3ϖ + e4ϖ̲ = (1/4) K + 4ϖϖ̲ + 2ζ² − ηη̲.

On the other hand ϖ = −(1/2)e4α and ϖ̲ = −(1/2)e3α give e3ϖ − e4ϖ̲ = −(1/2)[e3, e4]α = −(1/2)(4ϖϖ̲ − 4ϖ̲ϖ + 4ζ e1α) =
−2ζ e1α = −(1/2)(η² − η̲²). Half the sum of the two relations, with ζ = (η − η̲)/2 and K = 2(Ric_34 + Ric_11), is (F3).

(F4) e3χ = h(∇_3∇_1e4, e1) + h(∇_1e4, ∇_3e1) = h(∇_3∇_1e4, e1) + 2ζη, since h(χ e1 − ζ e4, η e3) = 2ζη. Here
∇_3∇_1e4 = R(e3, e1)e4 + ∇_1∇_3e4 + ∇_[e3,e1] e4. The e1-component of ∇_1∇_3e4 = ∇_1(2ϖ̲ e4 + 2η e1) is 2ϖ̲χ + 2e1η,
and that of ∇_[e3,e1] e4 = (η − ζ)∇_3e4 − χ̲∇_1e4 is 2η(η − ζ) − χχ̲. With h(R(e3, e1)e4, e1) = Ric_11 this is (F4).

(F5) By (a), e3η + e3η̲ = 2e3e1α = 2e1e3α + 2[e3, e1]α = −4e1ϖ̲ + 2(e1α)(e3α) − 2χ̲ e1α = −4e1ϖ̲ − (2ϖ̲ + χ̲)(η + η̲).
Subtracting (F2′), e3η̲ = −Ric_31 − χ̲(η̲ − η), gives (F5).

The images under the exchange hold by the same derivations with the roles of e3 and e4 exchanged, since the table and
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
    e3q_in = −χ̲ q_in,      e4q_out = −χ q_out.  {#eq:civp-large-reduced}

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

    A^u = diag(I₁₀, 0),      A^v = diag(0, I₁₃),      A^ϑ = (b I₁₀, Q; Qᵀ, 0),  {#eq:civp-large-form}

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

q_in as given, and χ̲ the solution of the linear equation (F4′), e4χ̲ = 2e1η̲ + 2η̲² + 2ϖχ̲ − χχ̲ + M_11 with χ := e4β
and M_11 := (3/2)(e1ψ)² + 2(e1ω)², whose value at v = 0 is e^(−α)∂_uβ computed on 𝒞_in. Define on 𝒞_in, where b = 0 and
e3 = e^(−α)∂_u,

    ϖ̲ := −(1/2) e3α,   Ψ_3 := e3Ψ,   Ψ′_1 := e1Ψ,

α, β, b = 0, Ψ and q_out as given, η the solution of the linear equation (F5), e3η = M_31 − 2χ̲η − 4e1ϖ̲ − 4ϖ̲ e1α with
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
the data, with χ := e4β, η := ζ + e1α, ζ := −(1/4)e^(β−2α)∂_vb and Ψ′_1 := e1Ψ. They solve the corresponding equations
of [[eq:civp-large-system]]: those for α, β, b, Ψ by [[eq:civp-large-coefficients]]; that for χ by (F1) and the
constraint Ric(∂_v, ∂_v) = q_in, which by [[prop:reduction]] (the term with R11, R22 being multiplied by g3(∂_v, ∂_v) =
0) reads Ric[h](∂_v, ∂_v) = q_in + (3/2)(∂_vψ)² + 2(∂_vω)², that is Ric_44 = M_44; that for η by (F2) and the
constraint Ric(∂_v, ∂_ϑ) = 0, which reads Ric_41 = M_41 (g3(∂_v, ∂_ϑ) = 0); and that for Ψ′_1 by the commutator [e4,
e1]. The remaining equations, for Ψ_3, then ϖ̲, then q_out, are linear in these unknowns with coefficients defined on
all of 𝒞_out, so they have solutions there. On 𝒞_in, take χ̲ := e3β, η̲ := 2e1α − η, Ψ° := Ψ and Ψ_1 := e1Ψ. The
equation for χ̲ holds by (F1′) and the constraint Ric(∂_u, ∂_u) = q_out (g3(∂_u, ∂_u) = γ_ϑ b² = 0 on 𝒞_in), that for
Ψ°, Ψ_1 by the definitions and [e3, e1]; that for η̲ holds because, by the equation defining η and 2e3e1α = −4e1ϖ̲ −
(2ϖ̲ + χ̲)(η + η̲) (proof of (F5)), D_3η̲ = e^α(2e3e1α − e3η) = −e^α(M_31 + χ̲(η̲ − η)). The equations for Ψ_4, then ϖ,
then q_in are linear and have solutions on all of 𝒞_in. In each case the initial values at S are those of f̄, so these
are the solutions of (i).

(ii) Every formula and every coefficient of the equations above at an angle ϑ is built from the functions of the data
and their derivatives at ϑ, and so are the initial values at S; the equations are ordinary differential equations along
the lines {ϑ = const}, since b = 0 on 𝒞_in and the f₄-equations contain no ∂_ϑ of an f₄-unknown. At ϑ ∉ (ϑ_a, ϑ_b) the
data are the background's on a neighbourhood of ϑ, the background's reduced fields solve all the equations used
([[prop:civp-large-system]] (a)), and by uniqueness for these equations f̄ and the solutions of (i) are the
background's there. ∎

#### An energy identity {#sec:civp-large-energy}

**Lemma {#lem:civp-large-energy}** (Energy for systems in doubly-null form.) Let R := [u_c, u_c + l_u] × [v_c, v_c +
l_v], let J = [ϑ₋, ϑ₊] be an interval, or an arc of a circle with a coordinate ϑ on it, and let z = (z₃, z₄), of class
C¹ on R × J with values in ℝ^(N₃) × ℝ^(N₄), solve

    ∂_u z₃ + P ∂_ϑ z₃ + Q ∂_ϑ z₄ = B₃ z,      ∂_v z₄ + Qᵀ ∂_ϑ z₃ = B₄ z,  {#eq:civp-large-linear}

with P symmetric, P and Q of class C¹ and B₃, B₄ continuous on R × J. Assume z₃ = 0 on {u_c} × [v_c, v_c + l_v] × J
and z₄ = 0 on [u_c, u_c + l_u] × {v_c} × J.

(a) Let |P| ≤ p and |Q| ≤ q on R × J (operator norms), let t > 0, c1 := p + t, c2 := q²/t and k(u, v) := c1(u − u_c) +
c2(v − v_c). Then z = 0 at every point of R × J with ϑ₋ + k(u, v) ≤ ϑ ≤ ϑ₊ − k(u, v).

(b) If z = 0 on R × ([ϑ₋, ϑ₋ + ε] ∪ [ϑ₊ − ε, ϑ₊]) for some ε > 0, then z = 0 on R × J.

*Proof.* Put A^u := diag(I, 0), A^v := diag(0, I) and A^ϑ := (P, Q; Qᵀ, 0), so that [[eq:civp-large-linear]] reads
A^μ∂_μz = Bz with B := (B₃; B₄), and for λ ≥ 0 let X^μ := e^(−λ(u+v)) ⟨z, A^μz⟩, μ ∈ {u, v, ϑ}, a C¹ vector field in
the coordinates (u, v, ϑ). Since the A^μ are symmetric and A^u, A^v are constant,

    ∂_μX^μ = e^(−λ(u+v)) (−λ ⟨z, (A^u + A^v)z⟩ + ⟨z, (∂_ϑA^ϑ)z⟩ + 2⟨z, Bz⟩) ≤ e^(−λ(u+v)) (C₁ − λ) |z|²,

with C₁ := sup_(R×J) (|∂_ϑA^ϑ| + 2|B|), finite since R × J is compact, and A^u + A^v = I. Fix λ > C₁.

(a) Fix (u′, v′) ∈ R with ϑ₋ + k(u′, v′) ≤ ϑ₊ − k(u′, v′), and let W be the set of (u, v, ϑ) with u_c ≤ u ≤ u′,
v_c ≤ v ≤ v′ and ϑ₋ + k(u, v) ≤ ϑ ≤ ϑ₊ − k(u, v); since k increases in u and v, its sections are nonempty intervals,
and W is compact with a piecewise smooth boundary. By the divergence theorem ∫_W ∂_μX^μ = ∫_(∂W) X^μ ν_μ dS, with ν the
outer unit conormal. On the face u = u′, X^μν_μ = e^(−λ(u+v)) |z₃|² ≥ 0; on v = v′ it is e^(−λ(u+v)) |z₄|² ≥ 0; on
u = u_c and v = v_c it vanishes, since these faces lie in the sets where z₃, respectively z₄, vanish. On the face
ϑ = ϑ₊ − k the conormal is a positive multiple of dϑ + c1 du + c2 dv, and on ϑ = ϑ₋ + k one of −dϑ + c1 du + c2 dv, so
X^μν_μ is a positive multiple of e^(−λ(u+v)) ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩, and

    ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩ ≥ (c1 − p)|z₃|² − 2q|z₃||z₄| + c2|z₄|² = (t^(1/2)|z₃| − q t^(−1/2)|z₄|)² ≥ 0.

Hence 0 ≤ ∫_(∂W) X^μν_μ dS = ∫_W ∂_μX^μ ≤ (C₁ − λ) ∫_W e^(−λ(u+v)) |z|², so z = 0 on W, and in particular at (u′, v′)
for every ϑ with ϑ₋ + k ≤ ϑ ≤ ϑ₊ − k.

(b) Take W := [u_c, u′] × [v_c, v′] × J. The faces u = u′, v = v′, u = u_c, v = v_c contribute as in (a), and on the
faces ϑ = ϑ± the field X vanishes, since z does. The same inequality gives z = 0 on W. ∎

#### Local developments {#sec:civp-large-local}

**Proposition {#prop:civp-large-corner}** (Developments near a corner sphere, without smallness.) Let m be the
regularity index of [[pending:civp-tier1-local]] and η ∈ (0, π/8]. For every Λ > 0 there is σ > 0 with the following
property. Let R = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ Q1, N_o := {u_c} × [v_c, v_c + l_v] and N_i := [u_c, u_c + l_u]
× {v_c}. Let smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of (v, ϑ) on N_o × S³, and Ω > 0, γ_ϑ > 0, A_c,
A_s and q_out ≥ 0 of (u, ϑ) on N_i × S³, with b = 0 on N_i, be given that agree on the corner sphere, satisfy
Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(∂_u, ∂_u) = q_out on N_i, equal the background's at the
points with ϑ ∉ [2η, π/2 − 2η], and whose differences from the background's, with ln Ω, ln γ_ϑ in place of Ω, γ_ϑ,
have C^m norms at most Λ. Then there is a class solution in the gauge on [u_c, u_c + min(l_u, σ)] × [v_c, v_c +
min(l_v, σ)] × S³ that induces these functions on the two edges and equals (g0, q̊_in, q̊_out) at the points with
ϑ ∉ [η, π/2 − η].

*Proof.* This is the development theorem of [[pending:civp-tier1-theorem]] with its smallness hypothesis replaced by
smallness of the rectangle, and its proof is the one given there ([[pending:civp-tier1-local]]), with 𝒞_out, 𝒞_in
and S replaced by N_o, N_i and the corner sphere. Three steps of that proof use the smallness of the data. (i) The
Cauchy problem for the augmented system with Rendall's forcing term is solved there on the whole time interval by
[[thm:class-kato-stability]] (a) around the background; here it is solved by [[thm:class-kato]] (a), with
[[rem:class-kato-local]] for the forcing term, on a time interval of length T > 0 that depends only on bounds for the
coefficients and for the norm of the extended data, hence only on Λ, η, m and the background on a neighbourhood of
Q1 × S³, and not on the corner. (ii) Finite speed of propagation and the localisation away from the axes are used
there with a cone field close to g0's; here the cone field of the solution is bounded in terms of Λ on the time
interval, the perturbation spreads in ϑ by at most a constant depending on Λ times the size of the rectangle, and the
solution equals the background at the points with ϑ ∉ [η, π/2 − η] once σ is small in terms of Λ and η. (iii) The
double-null coordinates are built there from the two phases and the transported angle near the background's; here
they are built in the same way on the rectangle of side σ, and they are close to the data's coordinates once σ is
small in terms of Λ. With σ chosen so that the initial slice of the Cauchy problem lies to the past of the corner
sphere and its development contains the rectangle of side σ, the remaining steps of that proof apply unchanged. ∎

#### The theorem {#sec:civp-large-theorem}

**Theorem {#thm:civp-large}** (Developments of cone data without smallness.) Let cone data be given
([[def:civp-large-data]]), with η0 and J0 as in [[eq:civp-large-band]]; no smallness is assumed. There is δ > 0 such
that, with 𝒮_δ := {(u, v) ∈ Q1 : min(u, v) ≤ δ}, the following hold.

(a) *Existence.* There is a class solution (g, v, u, q_in, q_out) in the gauge on 𝒮_δ × S³ that induces the cone data.
So v and u are the phases of the ingoing and the outgoing family of [[eq:class-system]] with N_f = 2, and the
development contains the strips {u ≤ δ} along 𝒞_out and {v ≤ δ} along 𝒞_in, a future neighbourhood of both cones.

(b) *Localisation.* g = g0, q_in = q̊_in and q_out = q̊_out at the points of 𝒮_δ × S³ with ϑ ∉ [ϑ_a − η0, ϑ_b + η0].

(c) *Uniqueness in the gauge.* Let D′ ⊂ Q1 be a past set and (g′, v, u, q′_in, q′_out) a class solution in the gauge
on D′ × S³ that induces the cone data on 𝒞_out ∩ D′ and 𝒞_in ∩ D′ and equals (g0, q̊_in, q̊_out) at the points with
ϑ ∉ [η′, π/2 − η′], for some η′ > 0. Then it equals (g, q_in, q_out) on (D′ ∩ 𝒮_δ) × S³.

(d) *The neighbourhood.* 𝒮_δ ⊃ {(u, v) ∈ Q1 : uv ≤ δ²}, and δ = min(s1, s2) with s1, s2 of [[eq:civp-large-delta]]:
they are given by the constants a*, b* of [[thm:std-cctw-strips]] for the localised system [[eq:civp-large-localised]]
with the data of [[lem:civp-large-data]] and by three suprema of its solution, and they depend on the cone data through
these. No lower bound for δ in terms of norms of the cone data is asserted.

The proof of (a) uses [[prop:civp-large-corner]]; (b), (c) and (d) do not.

*Proof.* Since uv ≤ δ² implies u ≤ δ or v ≤ δ, 𝒮_δ contains {uv ≤ δ²}.

*Step 1: the localised system.* Let Y := ℝ/πℤ, which contains J0 ⊂ (0, π/2) as an arc. Fix ϱ ∈ C^∞(Y) with 0 ≤ ϱ ≤ 1,
ϱ = 1 on [ϑ_a − η0, ϑ_b + η0] and supp ϱ ⊂ (ϑ_a − 2η0, ϑ_b + 2η0). Let f̊ be the reduced fields of the background on
Q1 × (0, π/2), and f̊_e ∈ C^∞(Q1 × Y; ℝ²³) a function that equals f̊ on Q1 × J0 and whose b-component vanishes (b̊ = 0).
With A^u, A^v, A^ϑ and G of [[prop:civp-large-system]], the *localised system* is

    A^u∂_uf + A^v∂_vf + ϱ A^ϑ(f) ∂_ϑf = ϱ G(f) + (1 − ϱ)(A^u∂_u + A^v∂_v) f̊_e      on Q1 × Y.
                                                                                               {#eq:civp-large-localised}

It has the form (2.7)–(2.8) of [CCTW16]: A^u = diag(I₁₀, 0) and A^v = diag(0, I₁₃) are unchanged, ϱA^ϑ(f) is symmetric,
and the coefficients and the right side are smooth functions of f and of (u, v, ϑ). It coincides with
[[eq:civp-large-system]] where ϱ = 1. The function f̊_e solves it: where ϱ = 0 trivially, and on supp ϱ ⊂ J0 because
there f̊_e = f̊ solves [[eq:civp-large-system]] ([[prop:civp-large-system]] (a) for g0), so that both sides equal
A^u∂_uf̊ + A^v∂_vf̊ + ϱA^ϑ(f̊)∂_ϑf̊. Its data are ϕ̄ := f̄₃ on {u = 0} × J0 and f̊_e,₃ on the rest of {u = 0} × Y, and
ψ̄ := f̄₄ on {v = 0} × J0 and f̊_e,₄ on the rest, with f̄ of [[lem:civp-large-data]] (b); they are smooth, because f̄ =
f̊ at the points of J0 with ϑ ∉ (ϑ_a, ϑ_b) ([[lem:civp-large-data]] (b) (ii)). The transport equations [CCTW16,
(3.100)–(3.101)] of [[thm:std-cctw-existence]] for this system are the restrictions of [[eq:civp-large-localised]] to
{v = 0} and {u = 0}. They have global solutions: on J0 take the solutions of [[lem:civp-large-data]] (b) (i), and on
the rest of Y the restrictions of f̊_e. Where ϱ = 1 these are the equations of [[lem:civp-large-data]] (b) (i); at the
other points of J0 those solutions equal f̊ ([[lem:civp-large-data]] (b) (ii)), which solves the localised system; and
the two pieces agree near the ends of J0.

*Step 2: the strip solution.* [[thm:std-cctw-existence]] and [[thm:std-cctw-strips]] apply with n = 2, a0 := u1,
b0 := v1 and any integer ℓ ≥ 6 (ℓ > (n + 9)/2): Y is a compact one-dimensional manifold without boundary, the system has
the form (2.7)–(2.8) with the scalar product and the flat connection preserving the splitting, the data are smooth, and
the transport equations have global solutions. They give a* ∈ (0, u1], b* ∈ (0, v1] and a solution f of
[[eq:civp-large-localised]] with these data on 𝒰 := ([0, a*] × [0, v1] ∪ [0, u1] × [0, b*]) × Y, unique among C¹
solutions and smooth, the data being smooth.

*Step 3: localisation and δ.* Put z := f − f̊_e on 𝒰. Subtracting the equations for f and f̊_e,

    A^u∂_uz + A^v∂_vz + ϱA^ϑ(f)∂_ϑz = ϱ(G(f) − G(f̊_e)) − ϱ(A^ϑ(f) − A^ϑ(f̊_e))∂_ϑf̊_e,

whose right side is B z with B := ϱ∫_0^1 (dG − (dA^ϑ)∂_ϑf̊_e)(f̊_e + s z) ds continuous. This is [[eq:civp-large-linear]]
with P := ϱb I₁₀ and Q := ϱQ(f), b and Q(f) evaluated on f. Its data vanish on the arc I := Y ∖ (ϑ_a, ϑ_b). Let

    p1 := sup |b| over [0, a*] × [0, v1] × Y,      β1 := sup |∂_vb| over [0, u1] × [0, b*] × Y,
    q1 := sup e^(α−β) over 𝒰,      s1 := min(a*, η0²/(2p1η0 + 4q1²v1)),
    s2 := min(b*, η0/(4u1β1), η0²/(8q1²u1)),      δ := min(s1, s2),
                                                                                             {#eq:civp-large-delta}

with the middle term of s2 omitted if β1 = 0, the components b, α, β being those of f. On [0, s1] × [0, v1] apply
[[lem:civp-large-energy]] (a) with J := I, p := p1, q := q1 and t := 2q1²v1/η0: then c2 = η0/(2v1), c1 = p1 + t, and
k = c1u + c2v ≤ c1s1 + η0/2 ≤ η0. On [0, u1] × [0, s2] the b-component of f vanishes at v = 0, both on J0 (b = 0 on
𝒞_in) and elsewhere (f̊_e has b = 0), so |b| ≤ β1 v ≤ β1 s2 ≤ η0/(4u1) =: p there; with t := η0/(4u1), c1 = p + t ≤
η0/(2u1) and c2 = 4q1²u1/η0, so k ≤ η0/2 + c2s2 ≤ η0. On both strips, therefore, z = 0 at the points of I at distance
at least η0 from its ends, that is

    f = f̊_e  at the points of 𝒮 × Y with ϑ ∉ (ϑ_a − η0, ϑ_b + η0),   𝒮 := [0, s1] × [0, v1] ∪ [0, u1] × [0, s2] ⊃ 𝒮_δ.

Define F on 𝒮_δ × (0, π/2) by F := f on J0 and F := f̊ off J0. It is smooth, since f = f̊_e = f̊ near the ends of J0;
it equals f̊ at the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0]; and it solves [[eq:civp-large-system]], since ϱ = 1 on
[ϑ_a − η0, ϑ_b + η0] and f̊ solves [[eq:civp-large-system]]. On 𝒞_out its f₃-components are f̄₃, and its f₄-components
solve the restriction of Step 1 with the same initial values at S; that restriction is a system of ordinary
differential equations in v along the lines {ϑ = const} (A^ϑ has no f₄f₄-block), so they are the solution of
[[lem:civp-large-data]] (b) (i), whose components α, β, b, ψ, ω are the functions of the data. Likewise on 𝒞_in its
f₄-components are f̄₄ and its f₃-components the solution of [[lem:civp-large-data]] (b) (i), b vanishing there.

*Step 4: F is geometric.* Let h_F and g_F be the metrics built from the components α, β, b, ψ, ω of F as in
[[prop:civp-large-system]] (b); they are defined on all of 𝒮_δ × (0, π/2), times T² for g_F. F is geometric on a set
when the identities of [[prop:civp-large-system]] (b) hold at its points; on the closure of a set where they hold they
hold too, F being smooth. Where F is geometric, (g_F, v, u, q_in, q_out) is a class solution in the gauge, by that
proposition. We say that F is *geometric to first order* at a point if there its components χ, χ̲, η, η̲, ϖ, ϖ̲ are the
connection coefficients of h_F and Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}. We show that F is
geometric on 𝒮_δ × (0, π/2). As 𝒮_δ = 𝒯₁ ∪ 𝒯₂, 𝒯₁ := [0, δ] × [0, v1], 𝒯₂ := [0, u1] × [0, δ], it suffices to treat one
of them, 𝒯 = [0, l1] × [0, l2].

*Constants.* F is smooth on 𝒮_δ × (0, π/2) and equals f̊ off [ϑ_a − η0, ϑ_b + η0] ⊂ [2η0, π/2 − 2η0]. So the functions
Ω = e^(α−ψ), γ_ϑ = e^(2β−2ψ), b, A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2, q_in, q_out formed from F on segments {u_c} ×
[v_c, v_c + l_v] and [u_c, u_c + l_u] × {v_c} in 𝒯, transformed by the change of angle described below, have
differences from the background's whose C^m norms are bounded by one Λ, for all such segments, because F and its
derivatives are bounded on 𝒯 × [η0, π/2 − η0] and the change of angle has derivatives bounded by those of b. Let σ be
given by [[prop:civp-large-corner]] for this Λ and η := η0, and L := σ/2.

*The corner step.* Let R = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ 𝒯 with l_u, l_v ≤ σ and edges N_o, N_i, and assume: F
is geometric to first order at the points of the corner circle {(u_c, v_c)} × (0, π/2); N_o × (0, π/2) is contained in
a set on which F is geometric, or u_c = 0; and N_i × (0, π/2) is contained in a set on which F is geometric, or v_c =
0. We show that F is geometric on R × (0, π/2). On N_o take the functions Ω, γ_ϑ, b, A_c, A_s, q_in formed from F, and
on N_i the functions Ω, γ_ϑ, b, A_c, A_s, q_out. Where an edge lies in 𝒞_out or 𝒞_in these are the cone data (Step 3),
and they satisfy the constraints by [[def:civp-large-data]] (ii); where F is geometric they are induced by the class
solution g_F, and the constraints are components of Ric(g_F) = q_in dv² + q_out du². They agree at the corner and equal
the background's off [2η0, π/2 − 2η0]. If b does not vanish on N_i, let Φ(u, ϑ) solve (∂_u + b(u, v_c, ϑ)∂_ϑ)Φ = 0 with
Φ(u_c, ϑ) = ϑ; for each u it is a diffeomorphism of (0, π/2) equal to the identity off [ϑ_a − η0, ϑ_b + η0], where b =
0. The change of angle (u, v, ϑ) ↦ (u, v, Φ(u, ϑ)) maps a metric of the form [[eq:loc-double-null]] to one of the same
form, with γ_ϑ replaced by γ_ϑ/(∂_ϑΦ)², b by ∂_uΦ + b∂_ϑΦ, and Ω, A_c, A_s unchanged, since Φ does not depend on v and
dϑ − b du = (dΦ − (∂_uΦ + b∂_ϑΦ) du)/∂_ϑΦ; it commutes with the T² action and the reflections, it is the identity on
N_o, and after it b = 0 on N_i. [[prop:civp-large-corner]] applies to the transformed functions and gives a class
solution in the gauge on R × S³; changing the angle back gives a class solution g_c in the gauge on R × S³ that induces
the functions above on N_o and N_i and equals (g0, q̊_in, q̊_out) off [η0, π/2 − η0]. Let f_c be its reduced fields, a
solution of [[eq:civp-large-system]] on R × (0, π/2) ([[prop:civp-large-system]] (a)). By [[lem:civp-large-data]] (a),
the f₃-components of f_c on N_o and its f₄-components on N_i are given by the functions on the edges, through
[[eq:civp-large-coefficients]] and the equations (F4′) on N_o and (F5), (F4) on N_i, with the values of f_c at the
corner, which are given by [[eq:civp-large-coefficients]] in the functions near the corner. The same holds for F. At
the corner F is geometric to first order, and h_F, ψ, ω induce the same functions on the edges as g_c, so F has the
same values there as f_c. On an edge on which F is geometric, the proof of [[lem:civp-large-data]] (a) applies to F,
since it uses only identities that hold at the points of the edge. On an edge in 𝒞_out or 𝒞_in it holds by the
definition of f̄ in [[lem:civp-large-data]] (b), the linear equations there being those used here, with the same
coefficients, and the values at the corner being those of F. By uniqueness for these linear equations, z := f_c − F has
z₃ = 0 on N_o and z₄ = 0 on N_i. It solves the linear system A^μ(F)∂_μz = G(f_c) − G(F) − (A^ϑ(f_c) − A^ϑ(F))∂_ϑf_c, of
the form [[eq:civp-large-linear]] on R × [η0/2, π/2 − η0/2], and z = 0 at the points with ϑ ≤ η0 or ϑ ≥ π/2 − η0, where
f_c = f̊ = F. By [[lem:civp-large-energy]] (b), z = 0 on R × (0, π/2). So F is the reduced fields of g_c on R × (0,
π/2) and is geometric there.

*Continuation in u + v.* For t > 0 let D_t := {(u, v) ∈ 𝒯 : u + v < t}, and let t* be the supremum of the t ∈ (0, l1 +
l2] such that F is geometric on D_t × (0, π/2), with t* := 0 if there is none. The corner step with R = [0, min(L, l1)]
× [0, min(L, l2)] applies: its corner is S, where F is geometric to first order, because the values of f̄ at S are
those of [[eq:civp-large-coefficients]] in the cone data, and its edges lie in 𝒞_out and 𝒞_in. So t* ≥ min(L, l1, l2) >
0. Suppose t* < l1 + l2. F is geometric on the closure of D_t* × (0, π/2). Let Γ := {(u, v) ∈ 𝒯 : u + v = t*}, and for
p = (u_p, v_p) ∈ Γ let u_c := max(u_p − L/2, 0), v_c := max(v_p − L/2, 0) and R_p := [u_c, min(u_p + L/2, l1)] × [v_c,
min(v_p + L/2, l2)], whose sides are at most L < σ. Its corner satisfies u_c + v_c ≤ t*. If v_c > 0, the edge N_i =
[u_c, min(u_p + L/2, l1)] × {v_c} satisfies u + v ≤ u_p + L/2 + v_p − L/2 = t*, so it lies in the closure of D_t*;
likewise N_o if u_c > 0. So the corner step applies, and F is geometric on R_p × (0, π/2). Every (u, v) ∈ 𝒯 with t* ≤
u + v < t* + L/4 lies in some R_p: with s := (u + v − t*)/2 < L/8, take p := (u − s, v − s) if this point lies in 𝒯, and
otherwise the end point of Γ on the side of 𝒯 that it leaves; in both cases u_p − L/4 ≤ u ≤ u_p + L/4 and v_p − L/4 ≤ v
≤ v_p + L/4. Hence F is geometric on D_(t*+L/4) × (0, π/2), contrary to the choice of t*. So t* = l1 + l2, and F is
geometric on 𝒯 × (0, π/2).

*Step 5: the solution.* By Step 4 and [[prop:civp-large-system]] (b), g_F with v, u, q_in, q_out is a class solution in
the gauge on 𝒮_δ × (0, π/2) × T². At the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0] it equals (g0, q̊_in, q̊_out), since
F = f̊ there; extended by (g0, q̊_in, q̊_out) to the axes it is a class solution in the gauge on 𝒮_δ × S³, which gives
(a) and (b). It induces the cone data: on 𝒞_out the components α, β, b, ψ, ω of F are the functions of the data and its
q_in is the data's (Step 3), and on 𝒞_in its f₄-components are f̄₄. By [[eq:civp-large-h]] the functions Ω, γ_ϑ, b, A_c,
A_s are therefore the data's on both cones.

*Step 6: uniqueness.* Let (g′, q′_in, q′_out) be as in (c) and f′ its reduced fields on D′ × (0, π/2), a solution of
[[eq:civp-large-system]] ([[prop:civp-large-system]] (a)) with f′₃ = f̄₃ on 𝒞_out ∩ D′ and f′₄ = f̄₄ on 𝒞_in ∩ D′
([[lem:civp-large-data]] (b) (iii)), and equal to f̊ off [η′, π/2 − η′]. Put η″ := min(η′, η0). D′ ∩ 𝒮_δ is a past
set; for (u, v) in it, z := f′ − F solves on [0, u] × [0, v] × [η″/2, π/2 − η″/2] a linear system of the form
[[eq:civp-large-linear]] as in Step 4, with z₃ = 0 at u = 0, z₄ = 0 at v = 0 (Step 3), and z = 0 at ϑ ≤ η″ and at
ϑ ≥ π/2 − η″, where f′ = f̊ = F. By [[lem:civp-large-energy]] (b), f′ = F on (D′ ∩ 𝒮_δ) × (0, π/2). The metric and the
densities are determined by α, β, b, ψ, ω, q_in, q_out through [[prop:civp-large-system]] (b), so (g′, q′_in, q′_out) =
(g, q_in, q_out) there, and both equal (g0, q̊_in, q̊_out) near the axes.

(d) is [[eq:civp-large-delta]] with Steps 2 and 3. ∎

**Remark {#rem:civp-large-domain}** (How the neighbourhood depends on the data.) In [[eq:civp-large-delta]], a* and b*
are the constants of [[thm:std-cctw-strips]] for the localised system with the data of [[lem:civp-large-data]]; that
theorem asserts their existence, independent of ℓ, and gives no bound for them. p1, q1 and β1 are suprema of the strip
solution, the shift, the ratio e^(α−β) = Ω γ_ϑ^(−1/2) and ∂_vb, and are not bounded here in terms of the data. So δ
depends on the data, on the band through η0 and on u1, v1, and no lower bound for it in terms of norms of the data is
asserted. For data near the background's, [[pending:civp-tier1-theorem]] gives a development on the explicit set
{uv ≤ δ_*²}; it equals g0 near the axes, so by [[thm:civp-large]] (c) the two developments agree where both are
defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ from
the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded or
measure-valued.

**Remark {#rem:civp-large-beyond}** (What the theorem adds.) With [[thm:civp-large]], the cone data of
[[sec:loc-cones]] that are localised in a band away from the axes have developments without any smallness: among them
every perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} and of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, of any amplitude,
and every density added in the band, when v1 > 4.5 and u1 > 7.2. The development contains the strip {u ≤ δ} along all
of 𝒞_out^(v1) and the strip {v ≤ δ} along all of 𝒞_in^(u1), so the dust on the cones lies in it; it is in the
double-null gauge of the class, with u and v the phases of the two families; it is localised, equal to the background
outside {ϑ_a − η0 ≤ ϑ ≤ ϑ_b + η0}, so that localisation on the cones is localisation of a spacetime; and it is unique
in the gauge among solutions that equal the background near the axes. For vacuum cone data (v1 < 3 and u1 < 5.7, the
densities zero), [CTG23, Theorem 1.1] ([[thm:std-ctg-neighbourhood]]) gives a vacuum development of any size; the
theorem adds the double-null gauge, uniqueness in it, and localisation. Compared with [[pending:civp-tier1-theorem]],
smallness is dropped and uniqueness holds among all solutions that equal the background near the axes, not only near
the background; the neighbourhood is not explicit and no estimate of the solution is given.

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:". Line numbers
are those of the current chapter sources and serve only to find the place. The section above follows the section of
[[pending:civp-tier1-theorem]] and uses it at three places, each marked: the analogue of [[prop:loc-cones]] on 𝒞_in
with the gauge b = 0 there ([[pending:civp-tier1-cin-cones]]), the theorem itself, for comparison, and its proof, for
[[prop:civp-large-corner]] ([[pending:civp-tier1-local]]). Where that section also changes a text listed below, the new
text below replaces both.

*1. Where the section goes.* The section above, from its heading through [[rem:civp-large-beyond]], is inserted in
[[ch:localised-data]] after the section of [[pending:civp-tier1-theorem]], which follows [[sec:loc-cones]], and before
the heading "### The static Killing field and the charge {#sec:loc-kid}", with one blank line before and one after. It
defines sec:civp-large, eq:civp-large-band, def:civp-large-data, sec:civp-large-frame, eq:civp-large-h,
lem:civp-large-frame, eq:civp-large-coefficients, eq:civp-large-null, eq:civp-large-box, eq:civp-large-dust,
eq:civp-large-table, lem:civp-large-reduction, eq:civp-large-reduced, eq:civp-large-m, eq:civp-large-system,
prop:civp-large-system, eq:civp-large-form, sec:civp-large-data, lem:civp-large-data, sec:civp-large-energy,
lem:civp-large-energy, eq:civp-large-linear, sec:civp-large-local, prop:civp-large-corner, sec:civp-large-theorem,
thm:civp-large, eq:civp-large-localised, eq:civp-large-delta, rem:civp-large-domain and rem:civp-large-beyond, none of
which is defined elsewhere; the prefix may be changed to the chapter's prefix loc- without other changes. Numbers are
resolved at assembly.

*2. [[ch:localised-data]], its opening paragraph (lines 8–9).* Old:

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]]). On Σ_τ0 the constraints split, after Rácz

New:

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]]); when the band avoids the axes they have a
development in the double-null gauge on a neighbourhood of the two cones, with or without dust and without smallness,
equal to the background outside a slightly wider band and unique in the gauge among solutions that equal the background
near the axes, the neighbourhood depending on the data ([[thm:civp-large]]; for data near the background's on an
explicit neighbourhood, [[pending:civp-tier1-theorem]]). On Σ_τ0 the constraints split, after Rácz

*3. [[ch:localised-data]], the paragraph after [[prop:loc-cones]] (lines 593–600).* Old:

When these cone data carry no dust, their vacuum development near the two cones exists by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]): this is the case when v_1 < 3, so that 𝒞_out ∩ {v ≤ v_1} lies before the shell, the
dust densities are left zero there, and 𝒞_in is taken only on u < 5.7, before the packet; both cones then carry
vacuum data of Tangherlini's metric of mass 3/2 outside the band, and the two cones meet transversally in the corner
sphere. [CTG23, Theorem 1.1] concerns vacuum data only. For cone data that carry dust, among them every perturbation
of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} and every density added in the band,
no development is asserted here: [[prop:loc-cones]] gives the cone data only, and no result of this paper uses their
development.

New:

When these cone data carry no dust, their vacuum development near the two cones exists by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]): this is the case when v_1 < 3, so that 𝒞_out ∩ {v ≤ v_1} lies before the shell, the
dust densities are left zero there, and 𝒞_in is taken only on u < 5.7, before the packet; both cones then carry vacuum
data of Tangherlini's metric of mass 3/2 outside the band, and the two cones meet transversally in the corner sphere.
With or without dust, the cone data of [[def:civp-large-data]], completed on 𝒞_in with b = 0 there, among them every
perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} of any amplitude and
every density added in the band, have a development in the gauge [[eq:loc-double-null]] on a neighbourhood {min(u, v) ≤
δ} of the two cones; it equals the background outside a slightly wider band and is unique in the gauge among solutions
that equal the background near the axes ([[thm:civp-large]]). The number δ depends on the data; for data near the
background's [[pending:civp-tier1-theorem]] gives an explicit neighbourhood and an estimate of the solution. No
development is asserted for cone data that differ from the background's near an axis, for data of finite regularity or
for densities that are not smooth, and no other result of this paper uses these developments.

*4. [[ch:scope]], the paragraph on localised data (line 200).* Old:

small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]).

New:

small amplitude when the first-order part perturbs the extrinsic curvature alone ([[thm:charge-sign]]). On the two null
cones through the corner sphere, data localised in an angular band exist exactly, with or without dust
([[prop:loc-cones]]); when the band avoids the axes they have a development in the double-null gauge on a neighbourhood
{min(u, v) ≤ δ} of the cones, without smallness, equal to the background outside a slightly wider band and unique in
the gauge among solutions that equal the background near the axes; δ depends on the data and is explicit only for data
near the background's ([[thm:civp-large]], [[pending:civp-tier1-theorem]]). Developments of cone data that differ from
the background's near an axis are not established.

*5. [[ch:introduction]], the paragraph on [[part:further]] (lines 190–191).* Old:

([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data and the sign of the charge
([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]], [[ch:equality-edge]]), the threshold λ0 at a

New:

([[ch:class-system]]), restricted massless Vlasov limits ([[ch:vlasov]]), localised data, their development from two
null cones, and the sign of the charge ([[ch:localised-data]]), the boundary at equality ([[ch:equality-layer]],
[[ch:equality-edge]]), the threshold λ0 at a

*6. [[ch:theorems]], the item *More families* (line 367).* Old:

  construction of that background does not decide ([[cor:vlasov-two-dust]]); and exactly localised vacuum data

New:

  construction of that background does not decide ([[cor:vlasov-two-dust]]); developments in the double-null gauge
  of cone data localised in an angular band away from the axes, with or without dust and without smallness, on a
  neighbourhood of the two cones that depends on the data, localised and unique in the gauge among solutions equal to
  the background near the axes ([[thm:civp-large]]); and exactly localised vacuum data

*7. [[app:standard-results]], [[sec:std-characteristic]].* Insert before [[thm:std-ctg-neighbourhood]], with one blank
line after each item; this defines thm:std-cctw-existence and thm:std-cctw-strips. New:

**Theorem {#thm:std-cctw-existence}** ([CCTW16, (2.1)–(2.2), p. 6; (2.7)–(2.9), p. 7; (3.2), p. 11; Theorem 3.9, pp.
32–33].) The authors consider "quasi-linear first order symmetric hyperbolic systems of the form Lf = G, (2.1) on
subsets of M̃ := {u ∈ [0, ∞), v ∈ [0, ∞), y ∈ Y}. (2.2) In (2.1), f is assumed to be a section of a real vector bundle
over M̃, equipped with a scalar product, similarly for G. … Both the scalar product and the connection coefficients are
allowed to depend upon f, and we assume that ∇ is compatible with ⟨·, ·⟩. … L is a first order operator of the form L =
A^μ∇_μ, where the A^μ's are self-adjoint, and are smooth functions of f and of the space-time coordinates" (p. 6), with
G = G(f, ·) (p. 11); here Y is "a (n − 1)-dimensional compact manifold without boundary" and ∇̊ "a fixed, arbitrarily
chosen, smooth connection which is f, u, and v–independent" (p. 6). They "specialise to f's which are of the form f =
(ϕ, ψ), (2.7) with A^v and A^u satisfying A^u = (A^u_ϕϕ, 0; 0, 0), A^v = (0, 0; 0, A^v_ψψ), and A^v_ψψ > 0, A^u_ϕϕ > 0.
(2.8) It is further assumed that the connections ∇ and ∇̊ preserve the splitting (2.7). We will write G = (G_ϕ, G_ψ).
(2.9)" (p. 7). With N₋ = {0} × [0, b0] × Y and N₊ = [0, a0] × {0} × Y (p. 32), a bar denoting restriction to N₋ ∪ N₊
(p. 11), Theorem 3.9 reads: "Let Y be a (n − 1)−dimensional compact manifold without boundary, let a0 and b0 two
positive real numbers and set Ω0 = [0, a0] × [0, b0] × Y. Consider the symmetric hyperbolic system (2.1) on Ω0 with the
splitting (2.7) and assume that (2.8) holds. Let ϕ̄ and ψ̄ be defined respectively on N₋ and N₊, providing Cauchy data
for (2.1): ϕ = ϕ̄ on N₋, ψ = ψ̄ on N₊. (3.98) Let ℓ ∈ ℕ, ℓ > (n + 9)/2 and suppose that ϕ̄ ∈ ∩_(0≤j≤ℓ) C^j([0, b0];
H^(ℓ−j)(Y)) and ψ̄ ∈ ∩_(0≤j≤ℓ) C^j([0, a0]; H^(ℓ−j)(Y)). (3.99) Assume that the transport equations A^μ_ϕϕ|_(v=0)
∂_μϕ|_(v=0) = (−A^μ_ϕψ ∂_μψ + G_ϕ)|_(v=0), (3.100) A^μ_ψψ|_(u=0) ∂_μψ|_(u=0) = (−A^μ_ψϕ ∂_μϕ + G_ψ)|_(u=0), (3.101)
with initial data ϕ|_(u=v=0) = ϕ̄|_(v=0) and ψ|_(u=v=0) = ψ̄|_(u=0), have a global solution on ([0, a0] × Y) ∪ ([0, b0]
× Y). Then there exists an ℓ-independent constant a* ∈ (0, a0] such that the Cauchy problem (2.1), (3.98) has a
solution f defined on [0, a*] × [0, b0] × Y satisfying (3.88)-(3.90) with k = ℓ − 1. … The solution f is unique within
the class of C¹ solutions, and is smooth if ϕ̄ and ψ̄ are." The omitted sentence states further regularity for ℓ > (n +
12)/2.

**Theorem {#thm:std-cctw-strips}** ([CCTW16, Corollary 3.11, p. 35].) "Under the hypotheses of Theorem 3.9, there
exists two constants 0 < a* ≤ a0 and 0 < b* ≤ b0 and a unique solution f of the Cauchy problem (2.1), (3.98) defined on
the neighborhood ([0, a*] × [0, b0] × Y) ∪ ([0, a0] × [0, b*] × Y) of N = N₊ ∪ N₋ such that f ∈ L^∞([0, a*] × [0, b0];
H^(ℓ−2)(Y)) ∩ ⋂_(0<3i≤ℓ−(n+9)/2) W^(i,∞)([0, a*] × [0, b0]; H^(ℓ−1−3i)(Y)) similarly on [0, a0] × [0, b*]." The
corollary follows from Theorem 3.9 by "the symmetry of the problem under the interchange of u and v" (p. 35). Theorem
3.9 applied to the system with u and v exchanged therefore also gives that f is smooth on [0, a0] × [0, b*] × Y when ϕ̄
and ψ̄ are smooth; on the overlap of the two strips the two solutions agree, by the uniqueness in Theorem 3.9.

*8. The references, [CCTW16] (lines 26–28).* The publisher's page gives volume 515 and pages 1–67; the page numbers
cited in the edition are those of arXiv:1406.3009v2, as the appendix states for all arXiv versions. Old:

- [CCTW16] A. Cabet, P. T. Chruściel, R. Tagne Wafo, *On the characteristic initial value problem for nonlinear
  symmetric hyperbolic systems, including Einstein equations*, Dissertationes Math. (2016), 1–72.
  doi:10.4064/dm732-7-2015 arXiv:1406.3009v2

New:

- [CCTW16] A. Cabet, P. T. Chruściel, R. Tagne Wafo, *On the characteristic initial value problem for nonlinear
  symmetric hyperbolic systems, including Einstein equations*, Dissertationes Math. 515 (2016), 1–67.
  doi:10.4064/dm732-7-2015 arXiv:1406.3009v2

*9. No change.* [[ch:two-dusts]], [[ch:class-system]], [[ch:vlasov]] and [[ch:ten-l5]] need no change: no result there
uses the cone developments, and the section uses only results those chapters state. The crosswalk of
[[ch:localised-data]] receives one row for each label listed in item 1.
