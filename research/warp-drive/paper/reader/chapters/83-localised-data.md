## Localised data and the sign of the charge {#ch:localised-data}

This chapter asks which perturbations of the data of [[ch:two-dusts]] can be localised: equal to the background's data
outside a compact set, in angle or in angle and radius at once. Throughout, the background is the two-dust background
of [[sec:two-dust-background]] with the explicit characteristic data of [[sec:bg-data]], and data are taken on its
slice Σ_τ0, τ0 = −0.68, or on a slice bent from it.

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]]). On Σ_τ0 the constraints split, after Rácz
[Rac16], into a hyperbolic system with the radius as time wherever κK^l_l < 0; this holds on all of Σ_τ0 except one
band inside the shell, where no foliation of Σ_τ0 is hyperbolic, and on a slice bent from Σ_τ0 by at most 0.0012 it
holds everywhere, so that data localised in an angle exist on the whole slice ([[thm:loc-bent-slice]]). Localisation
in angle and radius at once is decided, near the background's data and at second order in the amplitude, by the sign
of a charge Q: the pairing of the constraints with the static Killing field. Q is negative for every perturbation of
the extrinsic curvature alone; for perturbations of the metric it takes both signs where the round spheres are
trapped, f < 0, and is negative where they are not, f > 0 ([[thm:charge-sign]]).

The inequalities on the background that these results use are proved at the end of the chapter, in
[[sec:bg-below]] and [[sec:margins]], from the tables of [[sec:tab-bg]] and [[sec:table-margins]].

### The setting {#sec:loc-setting}

*The background.* The background g0 is the solution of the two-null-dust equations [[eq:two-dust-limit]] with the
characteristic data of [[sec:bg-data]]: e^(2σ) = 1/2 on the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the ingoing
shell 𝒜(v) = 3.6 b(v; 3, 4.5) on 𝒞_out, the outgoing packet ℬ(u) = 1.7 b(u;
5.7, 7.2) on 𝒞_in, and at the corner R = 5, R_u = −0.47, R_v = 1/2 and mass 3/2. In the chart (v̂, R) of
[[eq:bg-chart]] it reads g0 = −q² f dv̂² + 2q dv̂ dR + R² dΩ₃², q := e^ψ, f = 1 − μ/R². Region I is {u ≤ u1}, u1 =
5.7, where ψ = 0 and g0 is ingoing Vaidya ([[lem:margins-region-one]]); region III is {u ≥ u2}, u2 = 7.2, past the
outgoing packet, where ψ = ψ_III(v̂) and μ = μ3 ∈ [0.8220998, 0.8221253] ([[lem:bg-reduction]] (e),
[[thm:bg-margins]] (a)). The slice is Σ_τ0 = {v̂ − R = τ0} ∩ Ω₂, which is {a ≤ R ≤ b(τ0)} with a = 0.70
([[lem:two-dust-domain]]). Its *seed region* is {0.70 ≤ R ≤ 1.861}; it lies in region III ([[prop:bg-seed]] (a)), and
there f < 0 exactly where R < √μ3, and √μ3 ∈ (0.9066, 0.9068). The radius R_* ∈ [3.43718006, 3.43718007] of
[[lem:bg-rstar]] is where the ray u = u1 meets Σ_τ0; the points of Σ_τ0 with R ≥ R_* lie in region I
([[lem:margins-region-one]] (c)). At every point of Σ_τ0, qf < 1 ([[cor:margins-lens]], proof).

*The angles and the class.* On S³ we use the angles (ϑ, φ1, φ2) of [[sec:background]], with the round metric dΩ₃² =
dϑ² + cos²ϑ dφ1² + sin²ϑ dφ2², and write sc := sin ϑ cos ϑ. Data on a slice are *invariant* if they are invariant
under the T² action and the two reflections φ_i ↦ −φ_i. A *band* is a set U = {R1 < R < R2} of a slice, all angles
included. On a round slice γ = G dR² + R² dΩ₃² we use the orthonormal frame e_R := G^(−1/2) ∂_R, e_ϑ := R⁻¹∂_ϑ,
e_s := (R sin ϑ)⁻¹∂_(φ2), e_c := (R cos ϑ)⁻¹∂_(φ1).

*The constraints.* For data (γ, K) on a four-dimensional slice put

    Φ(γ, K) := (ℋ, ℳ),      ℋ := Scal(γ) + (tr K)² − |K|²,      ℳ_i := D_j K^j_i − D_i tr K,  {#eq:loc-constraints}

D the connection of γ. For data induced on a spacelike hypersurface by a Lorentzian metric g, with future unit normal n
and K(X, Y) = g(∇_X n, Y), the Gauss and Codazzi equations give ℋ = 2Ein(n, n) and ℳ_i = Ein(n, e_i), Ein the
Einstein tensor; for Einstein–matter data we write ρ := ℋ/2 and J := ℳ. In the notation of [[thm:std-cd-constraints]],
(J, ρ) there equals (−2ℳ, ℋ) here.

### Rácz's split on round slices {#sec:loc-racz}

**Lemma {#lem:racz-split-formulas}** (Round slices of the chart.) Let g = −q² f dv̂² + 2q dv̂ dR + R² dΩ₃², with q =
e^ψ > 0 and f functions of (v̂, R), on a region where qf < 2, and let Σ = {v̂ − R = τ} for a constant τ, parametrised
by (R, ϑ, φ1, φ2). Time-orient g so that v̂ − R increases to the future.

(a) Σ is spacelike, with γ = G dR² + R² dΩ₃², G := q(2 − qf). The lapse of v̂ − R is N := (2/q − f)^(−1/2), and the
future unit normal is n = (N/q)(∂_v̂ + (qf − 1)∂_R), with n_♭ = −N(dv̂ − dR).

(b) The second fundamental form K is round: K = κ0 G dR² + Y0 R² dΩ₃². Its radial part κ := K(e_R, e_R) = κ0 and its
trace on the spheres K^l_l := 3Y0 are

    κ = −N_κ/(q (2 − qf) √(2/q − f)),      K^l_l = 3(qf − 1)/(qR √(2/q − f)),
    N_κ := q²f²ψ_R + ½ q²f f_R − 3qfψ_R − ½ q f_v̂ − (3/2) q f_R − ψ_v̂ + ψ_R.  {#eq:racz-kappa}

So K^l_l < 0 where qf < 1, and there κK^l_l < 0 exactly where N_κ < 0.

(c) The vector field ξ := e^(−ψ) ∂_v̂ decomposes on Σ as ξ = N_s n + Y_s with

    N_s = N/q = q⁻¹ (2/q − f)^(−1/2) > 0,      Y_s = ((1 − qf)/G) ∂_R,      N_s √G = 1,      N_s² − G (Y_s^R)² = f,
                                                                                                    {#eq:racz-kid}

∂_R being the coordinate field of Σ, which is ∂_v̂ + ∂_R in the chart.

(d) On a vacuum region of the two-dust background, f = 1 − μ/R² with μ constant and ψ = ψ(v̂) ([[lem:bg-identities]]),
v := ∫ e^ψ dv̂ turns g into Tangherlini's metric −f dv² + 2 dv dR + R² dΩ₃², and ξ = ∂_v is its static Killing field.
On Σ there, with ψ, ψ′ evaluated at v̂ = τ + R and f′ := 2μ/R³,

    N_κ = (q f′/2)(qf − 3) − ψ′.                                                                       {#eq:racz-vacuum}

Every round slice v = V(R) of Tangherlini with V′ > 0 and fV′ < 2 is of the form Σ for the chart with e^(ψ(v̂)) :=
V′(v̂ − τ).

*Proof.* (a) The inverse of the (v̂, R) block has g^(v̂v̂) = 0, g^(v̂R) = 1/q and g^(RR) = f. The tangent field T :=
∂_v̂ + ∂_R of Σ has g(T, T) = −q²f + 2q = G > 0, and g⁻¹(dv̂ − dR, dv̂ − dR) = −2/q + f = −N⁻² < 0. Raising n_♭ gives
n^v̂ = N/q and n^R = N(qf − 1)/q.

(b) The spheres are orbits of SO(4) acting isometrically, so K is round. With the Christoffel symbols of g on the
spheres, Γ^a_(AB) = −R ∇^aR γ̂_AB for a ∈ {v̂, R}, K(∂_A, ∂_B) = R n(R) γ̂_AB, so K^l_l = 3n^R/R, which is the stated
value. For κ: κ = K(T, T)/G = −g(∇_T T, n)/G, since g(n, T) = 0. The (v̂, R) block h has the lowered symbols
Γ_(v̂,v̂v̂) = ½∂_v̂ h_v̂v̂, Γ_(R,v̂v̂) = ∂_v̂ q − ½∂_R h_v̂v̂, Γ_(v̂,v̂R) = ½∂_R h_v̂v̂, Γ_(v̂,RR) = ∂_R q and
Γ_(R,v̂R) = Γ_(R,RR) = 0, with h_v̂v̂ = −q²f. Hence (∇_T T)_v̂ = ½∂_v̂h_v̂v̂ + ∂_Rh_v̂v̂ + ∂_Rq and (∇_T T)_R = ∂_v̂q −
½∂_Rh_v̂v̂. Contracting with n^v̂ = N/q, n^R = N(qf − 1)/q and inserting ∂q = q∂ψ, ∂h_v̂v̂ = −2q²f∂ψ − q²∂f, the terms
in f ψ_v̂ cancel and

    g(∇_T T, n) = (N/q) · q N_κ = N N_κ,

so κ = −N N_κ/G, which is the stated formula. Where qf < 1, K^l_l < 0, and since q(2 − qf)√(2/q − f) > 0, κ > 0
exactly where N_κ < 0.

(c) g(ξ, n) = e^(−ψ) n_v̂ = −N/q, so N_s = −g(ξ, n) = N/q. Then Y_s = ξ − N_s n = q⁻¹(1 − N²/q)∂_v̂ − (N²/q²)(qf − 1)∂_R,
and N²/q = 1/(2 − qf), so Y_s = ((1 − qf)/(q(2 − qf)))(∂_v̂ + ∂_R). Next N_s²G = (N²/q²) q(2 − qf) = 1, and N_s² − G
(Y_s^R)² = (1 − (1 − qf)²)/G = qf(2 − qf)/(q(2 − qf)) = f.

(d) By [[lem:bg-identities]], μ_u = 0 and ψ_u = 0 where ℬ = 0, and μ_v = 0 where 𝒜 = 0; so on a vacuum region μ is
constant and ψ depends on v̂ alone (both being constant along the generators of either family). With dv = e^ψ dv̂ the
chart becomes −f dv² + 2 dv dR + R² dΩ₃². In [[eq:racz-kappa]], ψ_R = 0, f_v̂ = 0 and f_R = f′, which gives
[[eq:racz-vacuum]]. For the last claim, the slice v̂ = τ + R is v = Λ(τ + R) with Λ′ = e^ψ, and Λ := V(· − τ) has this
form. ∎

On Σ_τ0 every point has qf < 1, so K^l_l < 0 there and Rácz's split ([[thm:std-racz-hyperbolic]]) is hyperbolic
exactly where N_κ < 0. In region I, q = 1 and [[eq:racz-kappa]] reduces to the formulas of [[lem:margins-racz]].

**Proposition {#prop:loc-band}** (The band.) Rácz's split, for the foliation of Σ_τ0 by the round spheres, is
hyperbolic on Σ_τ0 ∩ {R ∉ [4.2882, 4.5310]} and not hyperbolic on Σ_τ0 ∩ {4.2955 ≤ R ≤ 4.5258}. At every point of
Σ_τ0 with 4.2955 ≤ R ≤ 4.5258, K is negative definite, and for every foliation of a neighbourhood of the point in Σ_τ0
by hypersurfaces the split is not hyperbolic there.

*Proof.* The first sentence is [[thm:margins-hyperbolic]] (b) for R ≥ R_* and [[thm:bg-margins]] (c) for R ≤ R_*. At a
point with 4.2955 ≤ R ≤ 4.5258, which lies in region I, N_κ > 0, so κ < 0, and K^l_l < 0 since f < 1. K being round,
K = κ e_R ⊗ e_R + (K^l_l/3)(γ − e_R ⊗ e_R), whose eigenvalues κ and K^l_l/3 are negative. Let n̂′ be the unit normal
of the leaves of another foliation at the point. Then κ′ = K(n̂′, n̂′) < 0, and K′^l_l = tr K − κ′ is the trace of K on
the three-dimensional orthogonal complement of n̂′, which is negative. So κ′K′^l_l > 0, and by the argument at the start
of [[sec:margins]], which uses only κ′K′^l_l > 0 and the three-dimensionality of the leaves, the split has no common
symmetrizer and is not hyperbolic. ∎

**Theorem {#thm:loc-bent-slice}** (Data localised in angle, on a bent slice.) Let φ be the bend of
[[prop:margins-bend]] and Σ′ := {v̂ − R − φ(R) = τ0} ∩ Ω₂.

(a) Σ′ equals Σ_τ0 outside 3.5 ≤ R ≤ 5.75, lies to the past of Σ_τ0 where they differ, at τ-distance at most
0.0011596, and is spacelike. Rácz's split for its round spheres is hyperbolic at every point of Σ′: κ′K′^l_l < 0, with
κ′K′^l_l ≤ −2.96 × 10⁻⁴ for R_* ≤ R ≤ 5.75 and κ′K′^l_l ≤ −4.76 × 10⁻³ for R ≤ R_*.

(b) Let 0 < ϑ1 < π/4 and a < R1 < R2 ≤ b(τ0). Take invariant free data ([Rac16, (4.28)], quoted in
[[thm:std-racz-hyperbolic]]) on Σ′ equal to the background's outside a compact subset of {R1 < R < R2, ϑ1 < ϑ < π/2 −
ϑ1} and ε-close to them in C^∞; the free data e, p_i may carry any number of further dust families supported there.
Take (k_i, K^l_l) at R = R2 equal to the background's. For ε small the system (4.16), (3.2) of [Rac16] has a unique
solution on a ≤ R ≤ R2. The data it determines, extended by the background's data for R ≥ R2, satisfy the constraints
on Σ′, and equal the background's outside the domain of influence, for that system, of the support of the
perturbation.

(c) The development of these data across the lens between Σ′ and Σ_τ0 induces on Σ_τ0 constraint data equal to the
background's outside the domain of influence of the support; on Σ_τ0 the angular support is wider than on Σ′ by at
most 3.3 × 10⁻⁴ rad.

So data localised in an angle exist near the background's data on all of Σ_τ0, the band of [[prop:loc-band]]
included; for perturbations whose radial support avoids [4.2882, 4.5310] the same construction works on Σ_τ0 itself.

*Proof.* (a) The first two statements are [[cor:margins-lens]]. Σ′ is spacelike: below R = 3.5 it is Σ_τ0, spacelike
by [[lem:two-dust-domain]] (a); for R ≥ R_* it lies in region I ([[lem:margins-region-one]] (c)), where d(τ − φ) is
timelike (proof of [[cor:margins-lens]]). The margin for R_* ≤ R is [[thm:margins-hyperbolic]] (a), and for R ≤ R_*,
where Σ′ = Σ_τ0, it is [[thm:bg-margins]] (c).

(b) The background's data solve the system on [a, R2] and the system is symmetrizable hyperbolic there, by (a) and
[[thm:std-racz-hyperbolic]]. A perturbation of the data of a symmetrizable hyperbolic system that is small in C^∞
has a solution on the whole compact interval of the background's solution, by the Cauchy stability theorem for such
systems [[pending:thm-class-kato-stability]]; by uniqueness the solution is invariant. The leaves are three-spheres, so
the axes are interior points of the leaves and need no condition. By [[thm:std-racz-hyperbolic]] the fields built from
the solution and the free data satisfy the constraints in the domain of dependence of the initial sphere, which here
is all of {a ≤ R ≤ R2}, and outside the domain of influence of the perturbation's support the solution is the
background's.

(c) The lens is a compact region of region I with no lateral boundary, and by [[cor:margins-lens]] every causal curve
joining Σ′ to Σ_τ0 runs in it. The development exists near the smooth background by the Cauchy stability of the class
Einstein–null-dust system ([[thm:class-stability]]), and the angular widening is that of [[cor:margins-lens]]. ∎

### Exact localisation on the cones {#sec:loc-cones}

In the double-null gauge of the class,

    g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ (dϑ − b du)² + e^(2A_c) dφ1² + e^(2A_s) dφ2²,  {#eq:loc-double-null}

with Ω, γ_ϑ, b, A_c, A_s functions of (u, v, ϑ), the cone 𝒞 := {u = u_c} is ruled by the null generators ∂_v. Put
λ_1 := ½ ln γ_ϑ, λ_2 := A_c, λ_3 := A_s.

**Lemma {#lem:loc-cone-equations}** (The constraints on a cone.) On 𝒞,

    Ric(∂_v, ∂_v) = Σ_(i=1)^3 (−∂_v²λ_i − (∂_vλ_i)² + 2 ∂_v ln Ω ∂_vλ_i),
    Ric(∂_v, ∂_ϑ) = (γ_ϑ/(4Ω²)) (∂_v²b + ∂_v ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) ∂_v b) + r,  {#eq:loc-cone}

where r is a polynomial in the first and mixed derivatives ∂_v, ∂_ϑ, ∂_v∂_ϑ of ln Ω, λ_1, λ_2, λ_3. Neither contains a
u-derivative, and b enters only through ∂_v b and ∂_v² b.

*Proof.* The inverse metric has g^(uv) = −1/(2Ω²), g^(vϑ) = −b/(2Ω²), g^(ϑϑ) = γ_ϑ⁻¹, g^(φ1φ1) = e^(−2A_c),
g^(φ2φ2) = e^(−2A_s), and g^(uu) = g^(vv) = g^(uϑ) = 0. Hence ∇_(∂_v)∂_v = Γ^v_(vv)∂_v = k ∂_v with k := 2∂_v ln Ω,
since g_vv = g_vϑ = 0. The sections {u, v constant} carry the metric γ_ϑ dϑ² + e^(2A_c)dφ1² + e^(2A_s)dφ2², b not
entering because du = 0 on them; ∂_v is orthogonal to them and commutes with ∂_ϑ and ∂_(φi), so their null second
fundamental form along ∂_v is half the v-derivative of that metric, with eigenvalues ∂_vλ_i, expansion θ_v = Σ∂_vλ_i and
|χ|² = Σ(∂_vλ_i)². The Raychaudhuri equation ∂_vθ_v = kθ_v − |χ|² − Ric(∂_v, ∂_v) is the first line. The second
line follows by a direct calculation of the Christoffel symbols of [[eq:loc-double-null]] in the coordinates (u, v,
ϑ, φ1, φ2), in which b enters only through g_uu = γ_ϑb², g_uϑ = −γ_ϑb and g^(vϑ) = −b/(2Ω²); in R_vϑ the terms in
b that carry no v-derivative cancel, and no u-derivative survives. ∎

**Proposition {#prop:loc-cones}** (Exact localisation on cones.) On the outgoing cone 𝒞_out = {u = 0} write γ_ϑ =
e^(2ϕ + 2ℓ_1), A_c = ϕ + ℓ_2, A_s = ϕ + ℓ_3 with ℓ_1 + ℓ_2 + ℓ_3 = 0, keep Ω the background's, and let the free data
(ℓ_1, ℓ_2, ℓ_3) and the null dust densities on 𝒞_out equal the background's outside a compact subset of a band {ϑ_a <
ϑ < ϑ_b} × [0, v_1], the corner sphere's data (ϕ, ∂_vϕ, b, ∂_v b at v = 0) being the background's. Then the constraints
Ric(∂_v, ∂_v) = T(∂_v, ∂_v), Ric(∂_v, ∂_ϑ) = T(∂_v, ∂_ϑ) on 𝒞_out determine ϕ and b on every generator on which e^ϕ
stays positive, and the resulting cone data equal the background's on every generator with ϑ ∉ [ϑ_a, ϑ_b]. No
smallness is used for the localisation; for small perturbations e^ϕ stays positive on [0, v_1].

*Proof.* With y := e^ϕ, the first line of [[eq:loc-cone]] reads −3y″/y + 6(ln Ω)′y′/y − Σ_i(ℓ_i′)² = T(∂_v, ∂_v),
′ = ∂_v, that is

    y″ − 2(ln Ω)′ y′ + (1/3)(Σ_i (ℓ_i′)² + T(∂_v, ∂_v)) y = 0,

a linear ordinary differential equation along each generator whose coefficients at the angle ϑ are the free data at ϑ.
With the background's corner values it has a unique solution, positive near v = 0. The second line of [[eq:loc-cone]] is
then a linear first-order equation for ∂_v b along each generator, with the nonzero leading coefficient γ_ϑ/(4Ω²) and
with the other coefficients and the inhomogeneous term built from the data and their ϑ-derivatives at ϑ. On a generator
with ϑ ∉ [ϑ_a, ϑ_b] all free data agree with the background's on a neighbourhood of ϑ, so the coefficients of both
equations are the background's there, and with the same initial values at the corner sphere both solutions are the
background's by uniqueness. ∎

The vacuum development of such cone data, near the two cones, exists by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]).

### The static Killing field and the charge {#sec:loc-kid}

**Lemma {#lem:loc-kid}** (The pairing with the static Killing field.) (a) For every lapse and shift (N, Y) and every
data induced by a Lorentzian metric g̃ with unit normal ñ, Nℋ + 2Y·ℳ = 2Ein(Nñ + Y, ñ); for Einstein–matter data,
Nℋ + 2Y·ℳ = 2(Nρ + Y·J).

(b) Let U be a band of Σ_τ0 whose closure lies in the interior of a vacuum region of the background, and (N_s, Y_s)
as in [[eq:racz-kid]]. For every smooth variation δ = (δγ, δK) of the data with compact support in U,

    ∫_U (N_s Dℋ[δ] + 2Y_s·Dℳ[δ]) dvol = 0.

(c) The invariant Killing fields of the development of such a band are the constant multiples of ξ.

*Proof.* (a) By the Gauss and Codazzi equations ([[eq:loc-constraints]]), Nℋ + 2Y^iℳ_i = 2N Ein(ñ, ñ) + 2Ein(Y, ñ).

(b) Let (t, x) be Gaussian normal coordinates of g0 near supp δ, g0 = −dt² + γ_t, defined on (−t_0, t_0) × U′ with supp δ
⊂ U′ and U′ in the vacuum region. Put h := χ(t)(δγ + 2t δK) in these coordinates (h_tt = h_ti = 0), with χ smooth,
compactly supported in (−t_0, t_0), χ = 1 near 0. Then g0 + εh has, on Σ_τ0, the lapse 1, the normal ∂_t and the data (γ
+ εδγ, K + εδK), so the data's first variation is δ. Since Ein(g0) = 0 near supp h, the first variation of the
constraints is DΦ[δ] = (2Ein¹[h](n, n), Ein¹[h](n, ·)), Ein¹[h] the linearised Einstein tensor, because the variation of
the normal enters multiplied by Ein(g0). By (a), N_sDℋ[δ] + 2Y_s·Dℳ[δ] = 2Ein¹[h](ξ, n). The vector field J^a :=
Ein¹[h]^(ab) ξ_b is compactly supported, and ∇_aJ^a = (∇_a Ein¹[h]^(ab)) ξ_b + Ein¹[h]^(ab)∇_(a ξ_b) = 0: the first term
vanishes by the linearised contracted Bianchi identity at a vacuum metric, obtained by differentiating ∇^(g0+εh)_a Ein(g0
+ εh)^(ab) = 0 at ε = 0, and the second because ξ is Killing. By the divergence theorem on [0, t_1] × U′, supp χ ⊂ (−t_1,
t_1), t_1 < t_0, the flux of J through Σ_τ0 equals that through {t = t_1}, which is 0.

(c) In the Tangherlini chart of [[lem:racz-split-formulas]] (d), let X = X^v∂_v + X^R∂_R + X^ϑ∂_ϑ + X^1∂_(φ1) +
X^2∂_(φ2) be an invariant Killing field; its components do not depend on φ1, φ2. The reflection φ_i ↦ −φ_i changes
the sign of X^i, so X^1 = X^2 = 0. The φ1φ1 and φ2φ2 components of L_X g are 2R cos²ϑ X^R − 2R² sc X^ϑ and 2R sin²ϑ
X^R + 2R² sc X^ϑ; their sum 2R X^R vanishes, so X^R = 0 and then X^ϑ = 0. With X = X^v∂_v, the RR, Rϑ and vR
components are 2∂_RX^v, ∂_ϑX^v and ∂_vX^v − f∂_RX^v, so X^v is constant. ∎

By [CD03, p. 33] ([[thm:std-cd-compact]]) the Killing initial data of a vacuum band generate Killing fields of its
development, so by (c) the invariant Killing initial data on U are the constant multiples of (N_s, Y_s).

**Definition {#def:loc-charge}** (Seeds and the charge.) Let U be a band as in [[lem:loc-kid]] (b). A *seed* on U is a
smooth invariant pair δ = (δγ, δK) with compact support in U and DΦ[δ] = 0. Its *charge* is

    Q(δ) := ½ ∫_U (N_s D²ℋ[δ, δ] + 2Y_s·D²ℳ[δ, δ]) dvol.                                               {#eq:loc-charge}

A seed is a *momentum seed* if δγ = 0. It is a *gauge seed* if it is the first variation of the data induced on the
slice by the pull-backs of g0 under a family of diffeomorphisms whose generator is compactly supported near U, or
equals a constant multiple of ξ on the inner side of U; otherwise it is *non-gauge*. Gauge seeds have Q = 0, since the
data they generate are the background's data on a deformed slice.

**Proposition {#prop:loc-projection}** (The charge decides localisation at second order.) Let U be a band as in
[[lem:loc-kid]] (b) and δ a seed on U.

(a) For every family D_ε = bg + εδ + c_ε of data on Σ_τ0, equal to the background's outside a fixed compact subset of
U, with ‖c_ε‖_(C²) ≤ Cε²,

    ∫_U (N_s ℋ + 2Y_s·ℳ)(D_ε) dvol = ε² Q(δ) + O(ε³).                                                {#eq:loc-pairing}

So if Q(δ) ≠ 0, no such D_ε satisfies the vacuum constraints for ε small.

(b) There are invariant corrections c_ε, supported in U, with ‖c_ε‖ ≤ Cε² in the norms of [[thm:std-cd-compact]], such
that Φ(bg + εδ + c_ε) is m(ε) times one fixed invariant element of the weighted image of the static Killing initial
data, whose pairing with (N_s, 2Y_s) is positive; then m(ε) has the sign of ε²Q(δ) + O(ε³). For a family of seeds
δ_s, s ∈ [0, 1], continuous in s, the corrections can be chosen continuous in s [[pending:issue-1]], with the O(ε³)
uniform in s. Hence, if Q(δ_0) < 0 < Q(δ_1), then for ε small there is s(ε) ∈ (0, 1) such that bg + εδ_(s(ε)) +
c_ε satisfies the vacuum constraints exactly and equals the background's data outside a compact subset of U.

*Proof.* (a) By Taylor's formula, Φ(D_ε) = Φ(bg) + DΦ[εδ + c_ε] + ½ε² D²Φ[δ, δ] + O(ε³), with Φ(bg) = 0 and DΦ[δ] =
0. Pairing with (N_s, 2Y_s), the term DΦ[c_ε] drops out by [[lem:loc-kid]] (b), and the quadratic term gives ε²Q(δ).
Vacuum data have Φ(D_ε) = 0.

(b) Apply [[thm:std-cd-compact]] on the closure M of a band U′ ⋐ U containing supp δ, with x a defining function of
∂M, at the data bg + εδ, which are close to the background's, with the right side (δJ, δρ) := −(J, ρ)(bg + εδ). This
right side is O(ε²), since DΦ[δ] = 0, and supported in U′. The theorem gives a correction c_ε of the form
x^(2s−n)Φ²P*(Y, N), close to zero and extending smoothly by zero across ∂M, such that the projection of
x^(−2s+n)(J, ρ)(bg + εδ + c_ε) onto the orthogonal complement of the space 𝒦0 of Killing initial data of the
background on M vanishes. The problem is invariant under the isometries T² × Z2 × Z2 and the solution near zero is
unique, so c_ε is invariant, and x^(−2s+n)(J, ρ)(bg + εδ + c_ε) lies in the invariant part of 𝒦0. By [[lem:loc-kid]]
(b) the pair (Y, N) := (−Y_s, N_s) pairs to zero with every compactly supported variation of (J, ρ) = (−2ℳ, ℋ), and by
[[lem:loc-kid]] (c) it spans the invariant part of 𝒦0; so (J, ρ)(bg + εδ + c_ε) = m(ε) x^(2s−n)(−Y_s^♭, N_s). Pairing
with (N_s, 2Y_s) gives m(ε) ∫ x^(2s−n)(N_s² + |Y_s|²) dvol = ε²Q(δ) + O(ε³), as in (a). The last statement follows
from the intermediate value theorem applied to m(ε, ·) on [0, 1]. ∎

### Momentum seeds {#sec:loc-momentum}

On a round slice γ = G dR² + R² dΩ₃² with round second fundamental form K0 = κ0 G dR² + Y0 R² dΩ₃², write an
invariant δK by its components in the frame of [[sec:loc-setting]]:

    δK(e_R, e_R) = κ,   δK(e_R, e_ϑ) = p̂,   δK(e_ϑ, e_ϑ) = Kt/3 + s1,   δK(e_s, e_s) = Kt/3 + s2,
    δK(e_c, e_c) = Kt/3 − s1 − s2,                                                                    {#eq:loc-dk}

the other components vanishing. Put c := −(κ0 + 2Y0)/(3Y0), β := −κ0/(3Y0), a := −3(1 − β)/R, so that 3c − 1 = Ra.

**Lemma {#lem:loc-momentum-constraints}** (The linearised constraints at δγ = 0.) Let Y0 ≠ 0. For δ = (0, δK),

    Dℋ[δ] = 2(3Y0 κ + (κ0 + 2Y0) Kt),
    √G Dℳ[δ](e_R) = −∂_R Kt + (3κ − Kt)/R + (√G/R)(1/sc) ∂_ϑ(sc p̂),
    R Dℳ[δ](e_ϑ) = (1/(√G R³)) ∂_R(R⁴ p̂) − (2/3)∂_ϑ Kt − ∂_ϑκ + ∂_ϑ s1 + (cot ϑ − 2 tan ϑ) s1 − s2/sc,  {#eq:loc-dm}

and the other components of Dℳ[δ] vanish. So δ is a momentum seed exactly when κ = c Kt,
∂_R Kt = a Kt + (√G/R)(1/sc)∂_ϑ(sc p̂), and

    s2 = sc ((1/(√G R³)) ∂_R(R⁴ p̂) − β ∂_ϑ Kt + ∂_ϑ s1 + (cot ϑ − 2 tan ϑ) s1).                          {#eq:loc-s2}

*Proof.* At δγ = 0, Dℋ[δ] = 2 tr K0 tr δK − 2⟨K0, δK⟩ with tr K0 = κ0 + 3Y0, tr δK = κ + Kt and ⟨K0, δK⟩ = κ0κ + Y0Kt.
Dℳ[δ] = div δK − d tr δK, with the Christoffel symbols of γ in (R, ϑ, φ1, φ2): Γ^R_RR = G′/(2G), Γ^R_ϑϑ = −R/G,
Γ^R_(φ1φ1) = −R cos²ϑ/G, Γ^R_(φ2φ2) = −R sin²ϑ/G, Γ^ϑ_(Rϑ) = Γ^(φi)_(Rφi) = 1/R, Γ^ϑ_(φ1φ1) = sc, Γ^ϑ_(φ2φ2) = −sc,
Γ^(φ1)_(ϑφ1) = −tan ϑ, Γ^(φ2)_(ϑφ2) = cot ϑ. Inserting the coordinate components of [[eq:loc-dk]] (δK_RR = Gκ,
δK_Rϑ = √G R p̂, δK_ϑϑ = R²(Kt/3 + s1), δK_(φ2φ2) = R² sin²ϑ (Kt/3 + s2), δK_(φ1φ1) = R² cos²ϑ (Kt/3 − s1 − s2)) gives
[[eq:loc-dm]]; the φ components vanish because nothing depends on φ_i and δK has no mixed φ components. With κ = cKt,
the combination −(2/3)∂_ϑKt − ∂_ϑκ is −β∂_ϑKt. ∎

**Theorem {#thm:charge-identity}** (The charge of a momentum seed.) Let U be a band of a round slice on which Y0 ≠ 0,
let N > 0 be a function of R, and for a momentum seed δ supported in U put

    Q_N(δ) := ∫_U N((tr δK)² − |δK|²) dvol,      ν := N √G R³,      E := e^(∫a dR),
    P := 8νE²R/G − (2νER/√G)′ RE/√G,      Γ := 4νE² − P′,  {#eq:charge-identity-defs}

′ = d/dR. Then there is a function η(R, ϑ), compactly supported in R, with

    Kt = E ∂_ϑη/sc,      p̂ = (R/√G) E ∂_Rη/sc,      η = O(sc²),   ∂_ϑη = O(sc),  {#eq:charge-stream}

and, with Z := s2 + s1/2 and X := ∂_ϑη − (3/2)(cos 2ϑ/sc) η,

    Q_N(δ) = −(2π)² ∫∫ [ 2ν sc (Z − Eη/(2sc²))² + (3/2) ν sc (s1 − 2EX/(3sc))²
                         + Γ η²/sin 2ϑ ] dϑ dR.                                                  {#eq:charge-identity}

For N = N_s, Q_N(δ) = Q(δ).

*Proof.* *The stream function.* Since E′ = aE, the second condition of [[lem:loc-momentum-constraints]] reads
∂_R(sc Kt/E) = ∂_ϑ(√G sc p̂/(RE)). Put η(R, ϑ) := ∫_(R1)^R √G sc p̂/(RE) dR′. Then ∂_Rη is as stated, and
∂_R(∂_ϑη − sc Kt/E) = 0 with both terms vanishing for R near R1, so ∂_ϑη = sc Kt/E. Near the axis ϑ = 0 the
component p̂ = δK(e_R, e_ϑ) is O(sin ϑ): in the plane (x3, x4) of [[sec:background]], e_ϑ is the unit radial
direction, and the rotation by π in that plane, an isometry preserving δK, reverses it, so p̂ at the point with polar
radius ϱ in that plane is an odd smooth function of ϱ = R sin ϑ. Likewise p̂ = O(cos ϑ) at ϑ = π/2. Hence ∂_Rη = O(sc²),
so η = O(sc²); and ∂_ϑη = sc Kt/E = O(sc), Kt being bounded. For R ≥ R2, ∂_ϑη = 0, so η is constant on each sphere
there, and η = 0 on the axis; so η is compactly supported in R.

*The quadratic form.* Since δγ = 0 and ℳ is linear in K at fixed γ, D²ℳ[δ, δ] = 0 and D²ℋ[δ, δ] = 2((tr δK)² −
|δK|²). From [[eq:loc-dk]] and κ = cKt, (tr δK)² − |δK|² = (2β − 2/3)Kt² − 2p̂² − s1² − s2² − (s1 + s2)², and dvol =
√G R³ sc dR dϑ dφ1 dφ2. So Q_N(δ) = (2π)² ∫∫ 𝔮 dϑ dR with 𝔮 := ν sc [(2β − 2/3)Kt² − 2p̂² − s1² − s2² − (s1 + s2)²],
and Q_(N_s) = Q by [[eq:loc-charge]].

*The identity.* Substitute Kt and p̂ from [[eq:charge-stream]] and s2 from [[eq:loc-s2]] into 𝔮 and into the integrand
𝔡 of [[eq:charge-identity]] (with its sign). Then, pointwise,

    𝔮 = 𝔡 + ∂_ϑ 𝔄 + ∂_R 𝔅,
    𝔄 := 2νβE² η ∂_ϑη/sc − 2νE η s1 − νE² (cos 2ϑ/sc²) η²,
    𝔅 := −(P/2) η²/sc − 2νE² (R²/G) η ∂_Rη/sc.                                                      {#eq:charge-flux}

This is an identity between polynomials in η, s1 and their derivatives, with coefficients in R and ϑ, and it is
checked by expanding both sides, using E′ = aE, a = −3(1 − β)/R and the definitions of P and Γ, with ν, G and β
arbitrary functions of R. It is found by writing s2 = Z − s1/2, integrating by parts the cross terms of η with s2 (in
R) and with s1 and ∂_ϑη (in ϑ), and completing the squares in Z and in s1; 𝔄 and 𝔅 record the integrations by parts.

*The boundary terms.* 𝔅 vanishes for R near R1 and R2. At ϑ → 0 and ϑ → π/2, by [[eq:charge-stream]] and the
boundedness of s1, each term of 𝔄 is O(sc²), so 𝔄 → 0; the integrand of [[eq:charge-identity]] is bounded, since
η/sc², X/sc and s2 are bounded and Γη²/sin 2ϑ = O(sc³). Integrating [[eq:charge-flux]] over (R1, R2) × (0, π/2) gives
[[eq:charge-identity]]. ∎

**Corollary {#cor:loc-charge-momentum}** (The sign for momentum seeds.) If Γ > 0 on U, then Q(δ) < 0 for every nonzero
momentum seed δ on U; precisely, Q(δ) ≤ −(2π)²∫∫ Γη²/sin 2ϑ if η ≠ 0, and Q(δ) = −(2π)²∫∫ ν sc (s1² + s2² + (s1 +
s2)²) < 0 if η = 0.

*Proof.* ν = N_s√G R³ > 0. If η ≠ 0 the first two terms of [[eq:charge-identity]] are nonnegative. If η = 0, then Kt
= p̂ = κ = 0, and 𝔮 = −ν sc (s1² + s2² + (s1 + s2)²); this vanishes identically only if s1 = s2 = 0, that is δ = 0. ∎

The positivity of Γ does not depend on the normalisation of E, since Γ scales with E². On a vacuum region of the
background, N_s√G = 1 ([[eq:racz-kid]]), so ν = R³, and [[lem:margins-gamma-form]] gives Γ/E² in closed form; where
ψ = 0 it gives Γ = 4μ/R for the normalisation E = √G/R.

**Corollary {#cor:loc-charge-seed}** (Momentum seeds on Σ_τ0.) Let U be a band of Σ_τ0 on which the background is
vacuum, contained in the seed region {0.70 ≤ R ≤ 1.861} or in {R ≥ R_*}. Then Γ > 0 on U, so Q(δ) < 0 for every
nonzero momentum seed δ on U, and for ε small no vacuum data on Σ_τ0 of the form bg + εδ + O(ε²), equal to the
background's outside a compact subset of U, exist.

*Proof.* On Σ_τ0, qf < 1, so Y0 = K^l_l/3 < 0 ([[lem:racz-split-formulas]] (b)). On the seed region Γ > 0 by
[[prop:bg-seed]] (c), which places the background in the tube of [[prop:margins-seed]] (b). On {R ≥ R_*} the points
lie in region I ([[lem:margins-region-one]] (c)), where ψ = 0 and Γ/E² = 4R³μ/(R² + μ) > 0
([[lem:margins-gamma-form]]). Then [[cor:loc-charge-momentum]] and [[prop:loc-projection]] (a) apply; a band of Σ_τ0
on which the background is vacuum has closure in a vacuum region after shrinking it slightly around the compact
support. ∎

The momentum seeds reach the axes: [[thm:charge-identity]] uses only the smoothness of δK on S³, and the boundary terms
at ϑ = 0 and ϑ = π/2 vanish. The charge is minus a sum of squares minus the term in Γ, which carries the mass: on flat
space, μ = 0, Γ = 0 where ψ = 0, and the identity degenerates to Q ≤ 0.

### Matter {#sec:loc-matter}

**Theorem {#thm:loc-matter}** (Momentum seeds with matter.) Let U be a band as in [[cor:loc-charge-seed]] and δ a
nonzero momentum seed on U.

(a) If f ≥ 0 on U, then for ε small there are no invariant Einstein–matter data D_ε = bg + εδ + c_ε, ‖c_ε‖_(C²) ≤
Cε², equal to the background's outside a fixed compact subset of U, whose matter satisfies the dominant energy
condition ρ ≥ |J|_γ.

(b) If U meets {f < 0}, there are exactly localised Einstein–null-dust data of this form, with outgoing radial null
dust of density ≥ 0 supported in U ∩ {f < 0}, for every small ε > 0.

*Proof.* (a) By [[lem:loc-kid]] (a) and [[eq:loc-pairing]], ε²Q(δ) + O(ε³) = 2∫_U (N_sρ + Y_s·J) dvol. Since
DΦ[δ] = 0, ρ and J are O(ε²). By [[eq:racz-kid]], N_s² − |Y_s|²_γ = f ≥ 0 for the background's γ, so N_s − |Y_s|_(γ_D)
≥ −Cε for the metric γ_D of D_ε, and N_sρ + Y_s·J ≥ (N_s − |Y_s|_(γ_D))ρ ≥ −Cερ. So the right side is at least
−C′ε³, while the left side is ε²Q(δ) + O(ε³) with Q(δ) < 0 by [[cor:loc-charge-seed]]: a contradiction for ε small.

(b) On a vacuum region of the chart, let ℓ_out := ∂_v̂ + (qf/2)∂_R, the future-directed outgoing null direction
(g(ℓ_out, ℓ_out) = 0, and d(v̂ − R)(ℓ_out) = 1 − qf/2 > 0), and T := ϖ ℓ_out^♭ ⊗ ℓ_out^♭ with density ϖ ≥ 0, which
satisfies the dominant energy condition. Since ℓ_out^♭ = −(q²f/2) dv̂ + q dR, ℓ_out^♭(ξ) = −qf/2 and ℓ_out^♭(n) =
−N(2 − qf)/2, so

    T(ξ, n) = ϖ qf (2 − qf)/(4√(2/q − f)),

which has the sign of f. Fix a nonzero dust density ϖ_1 ≥ 0 supported in U ∩ {f < 0}, with stress T_1; then ∫T_1(ξ, n)
dvol < 0. Put s* := Q(δ)/(2∫T_1(ξ, n) dvol) > 0. Solve, as in [[prop:loc-projection]] (b), for data bg + εδ + c whose
constraints equal ε²s times those of the dust of density ϖ_1 (the matter term computed with the unit normal of the
unknown data, which depends smoothly on them and is O(ε²)) up to the static Killing initial data, for s ∈ [0, 2s*]
[[pending:issue-1]]. Pairing as in (a), the coefficient of the Killing data has the sign of m(ε, s) = ε²(Q(δ) − 2s∫T_1(ξ,
n)) + O(ε³), uniformly in s and continuous in s. Then m(ε, 0) < 0 < m(ε, 2s*) for ε small, and m(ε, s(ε)) = 0 for some
s(ε): exact Einstein–null-dust data, equal to the background's outside U, with dust density ε²s(ε)ϖ_1 ≥ 0. ∎

Where f > 0 the vector ξ is future timelike and its charge is an energy, which the dominant energy condition makes
nonnegative; where f < 0 it is spacelike, its charge is a momentum, and outgoing dust carries it with the sign
opposite to that of the momentum seeds.

### Seeds that perturb the metric {#sec:loc-metric}

**Lemma {#lem:loc-harmonics}** (The class harmonics.) (a) Class functions on S³ are the expansions in P_j(cos 2ϑ), with
Δ̂ = −l(l + 2), l = 2j; class 1-forms are exact; a class symmetric 2-tensor on S³ is the orthogonal sum of a trace part,
a part (D̂D̂ − (1/3)γ̂Δ̂)𝓉 and a transverse trace-free part ([[lem:gd-1-2]]).

(b) The rough Laplacian Δ̂ of the unit S³ maps transverse trace-free class tensors to such tensors, and these are an
orthogonal sum of eigentensors Δ̂T = −k_T² T with k_T² ≥ 0.

(c) The tensor

    T_0 := dϑ² + ((3 cos 2ϑ − 1)/2) sin²ϑ dφ2² − ((3 cos 2ϑ + 1)/2) cos²ϑ dφ1²

is a smooth transverse trace-free class tensor with Δ̂T_0 = −6T_0.

*Proof.* (a) is [[lem:gd-1-2]] (a)–(c). (b) The round metric has constant curvature, so Δ̂ commutes with the trace and
maps divergence-free trace-free symmetric tensors to such tensors; it commutes with the isometries, so it preserves
the class. It is elliptic and self-adjoint on the compact S³, and ⟨T, −Δ̂T⟩ = ‖D̂T‖² ≥ 0. (c) The trace is 1 + (3 cos 2ϑ
− 1)/2 − (3 cos 2ϑ + 1)/2 = 0. The divergence and Δ̂T_0 + 6T_0 vanish by a direct calculation with the Christoffel
symbols of dΩ₃² listed in the proof of [[lem:loc-momentum-constraints]] (at R = 1, G = 1). Near ϑ = 0, T_0 = B_0
(dϑ² + sin²ϑ dφ2²) + 3 sin²ϑ dϑ² + C_0 cos²ϑ dφ1², with B_0 := (3 cos 2ϑ − 1)/2 and C_0 := −(3 cos 2ϑ + 1)/2 smooth
functions of cos 2ϑ, and dϑ² + sin²ϑ dφ2² = dΩ₃² − cos²ϑ dφ1² and sin²ϑ dϑ² are smooth near the axis ϑ = 0
(sin ϑ d(sin ϑ) = cos ϑ sin ϑ dϑ); here 1 − B_0 = 3 sin²ϑ. Near ϑ = π/2 the same holds with φ1, cos ϑ and
1 − C_0 = 3 cos²ϑ. So T_0 is smooth. ∎

**Theorem {#thm:loc-tensor}** (The tensor sector.) Let Σ be a round slice of a Tangherlini region as in
[[lem:racz-split-formulas]] (d), γ = G dR² + R² dΩ₃² its metric, (N_s, Y_s) as in [[eq:racz-kid]], n^R the radial
component of its normal, T a transverse trace-free class eigentensor, Δ̂T = −k_T²T, |T|² := ∫ |T|²_(γ̂) sc dϑ, and H,
Π smooth functions of R with compact support in (R1, R2). Let δ := (2R²H T, (R²Π + 2R n^R H) T). Then:

(i) DΦ[δ] = 0, so δ is a seed;

(ii) N_s√G = 1 and N_s² − G (Y_s^R)² = f;

(iii) with ξ(H) := N_sΠ + Y_s^R ∂_RH, |dH|² := −Π² + (∂_RH)²/G and g(ξ, n) = −N_s,

    Q(δ) = −2(2π)²|T|² ∫ T_m(ξ, n) √G dR,
    T_m(ξ, n) := R³ (ξ(H) Π − ½ g(ξ, n) |dH|²) − ½ g(ξ, n)(k_T² + 2) R H²;  {#eq:loc-tensor-charge}

(iv) T_m's quadratic form in (Π, ∂_RH) is R³ [[N_s/2, Y_s^R/2], [Y_s^R/2, N_s/(2G)]], of determinant R⁶ f/(4G):
positive definite exactly where f > 0.

*Proof.* (i) Here δγ and δK are purely angular, with angular parts radial functions times T. Since T is trace-free,
tr δγ = tr δK = 0; since T is divergence-free on S³ and δγ, δK have no radial components, div δγ = div δK = 0 (the
radial component of the divergence of a purely angular tensor is a multiple of its angular trace). K0 and Ric(γ) are
round, so ⟨δγ, Ric(γ)⟩, ⟨δγ, K0⟩, ⟨δK, K0⟩ and K0^(pl)K0^q_l δγ_pq are multiples of angular traces and vanish. In the
linearisation [[thm:std-cd-constraints]] (2.2) the terms −Δ tr h, div div h, ⟨h, Ric⟩, 2K^(pl)K^q_l h_pq, ⟨K, Q⟩, tr Q
and ⟨h, K⟩ therefore vanish, and so do K^(pq)∇_i h_pq, K^q_i(2∇^jh_qj − ∇_q tr h), ∇^jQ_ij, ∇_i tr Q and
(∇_iK^(pq) − ∇^qK^p_i)h_pq: each is a contraction of h or Q, or of their divergence, with tensors built from γ, K0,
dR and the second fundamental form of the spheres, all of which are round. (ii) is [[eq:racz-kid]].

(iii) [[pending:computational-1]]

(iv) With g(ξ, n) = −N_s, T_m = R³(½N_sΠ² + Y_s^RΠ ∂_RH + (N_s/(2G))(∂_RH)²) + ½N_s(k_T² + 2)RH², and the
determinant is R⁶(N_s² − G(Y_s^R)²)/(4G) = R⁶f/(4G) by (ii). ∎

The quantity T_m is the flux through Σ of J^a = T^a_b ξ^b for T_ab := R³(∂_aH ∂_bH − ½g_ab|dH|²) − ½g_ab(k_T² +
2)RH², the canonical stress of the tensor master equation D_a(R³D^aH) − (k_T² + 2)RH = 0 of the orbit space
([[thm:std-ki-master]] (1), with n = 3, K = 1).

**Lemma {#lem:loc-tensor-sign}** (Tensor seeds of either sign.) In the setting of [[thm:loc-tensor]]:

(a) if Π = −(Y_s^R/N_s) ∂_RH, then Q(δ) = −(2π)²|T|² ∫ (R³ f (∂_RH)² + (k_T² + 2) R H²) dR;

(b) if H = 0, then Q(δ) = −(2π)²|T|² ∫ R³ Π² dR < 0 unless Π = 0;

(c) if f < 0 on an interval I ⊂ (R1, R2) and H_ω := β_I(R) sin(ωR) for a smooth bump β_I ≥ 0 supported in I, then
in (a) Q(δ) = ½(2π)²|T|²ω² ∫ R³|f|β_I² dR + O(ω) > 0 for ω large.

*Proof.* (a) ξ(H) = N_sΠ + Y_s^R∂_RH = 0, and |dH|² = (∂_RH)²(1/G − (Y_s^R)²/N_s²) = (∂_RH)² f/(N_s²G) by
[[thm:loc-tensor]] (ii). So T_m = ½N_s(R³f(∂_RH)²/(N_s²G) + (k_T² + 2)RH²), and with N_s√G = 1, 2T_m√G = R³f(∂_RH)²
+ (k_T² + 2)RH². (b) ξ(H) = N_sΠ and |dH|² = −Π², so 2T_m√G = R³Π². (c) (∂_RH_ω)² = ω²β_I² cos²(ωR) + O(ω), cos² =
(1 + cos 2ωR)/2, and ∫R³fβ_I² cos 2ωR dR → 0 by the Riemann–Lebesgue lemma. ∎

**Theorem {#thm:loc-inside}** (Inside the apparent horizon.) Let U be a band of Σ_τ0 on which the background is vacuum
and which meets {f < 0}. Then:

(a) there are non-gauge seeds of tensor type on U with Q > 0 and with Q < 0;

(b) for every small ε > 0 there are exact invariant vacuum data on Σ_τ0, equal to the background's outside a compact
subset of U, of the form bg + εδ_ε + O(ε²) with δ_ε a non-gauge seed; δ_ε tends to a nonzero tensor seed as ε → 0.

*Proof.* Let T := T_0 of [[lem:loc-harmonics]] (c) and I ⊂ U ∩ {f < 0} an interval. (a) [[lem:loc-tensor-sign]] (c) gives
Q > 0 and (b) gives Q < 0. A gauge seed has a vanishing transverse trace-free part: its data are the variation of (γ, K0)
along a vector field Z = N_Z n + X_Z, (2N_Z K0 + L_(X_Z)γ, L_(X_Z)K0 + D²N_Z + N_Z 𝔯) with 𝔯 a round tensor built from
Ric(γ) and K0, and for invariant Z the angular trace-free parts of these are (D̂D̂ − (1/3)γ̂Δ̂) of scalars, the class
1-forms being exact ([[lem:loc-harmonics]] (a)), and so orthogonal to T. A seed of [[thm:loc-tensor]] with (H, Π) ≠ 0 has
a nonzero transverse trace-free part, so it is non-gauge.

(b) Let H := H_ω of [[lem:loc-tensor-sign]] (c) with ω so large that the seed δ_1 with Π = −(Y_s^R/N_s)∂_RH has Q(δ_1)
> 0, let Π_0 ≠ 0 be a bump in I, δ_0 the seed with (0, Π_0), and δ_s := (sH, −s(Y_s^R/N_s)∂_RH + (1 − s)Π_0) for s ∈
[0, 1]. Every δ_s is a nonzero tensor seed, hence non-gauge, and Q(δ_s) is a quadratic polynomial in s with
Q(δ_0) < 0 < Q(δ_1). [[prop:loc-projection]] (b) gives s(ε) and the data; since the root s_* of Q(δ_s) in (0, 1) is
simple, s(ε) = s_* + O(ε), and δ_ε := δ_(s(ε)) → δ_(s_*) ≠ 0. ∎

The charge Q vanishes on a whole cone of non-gauge seeds inside the apparent horizon. For a seed δ_0 on that cone whose
bilinear form 𝔟(δ_0, ·) := ½(Q(δ_0 + ·) − Q(δ_0) − Q(·)) is not identically zero, take δ′ with 𝔟(δ_0, δ′) ≠ 0;
then Q(δ_0 + sδ′) = 2s𝔟(δ_0, δ′) + s²Q(δ′) changes sign between s = ±Kε for a large K, and [[prop:loc-projection]] (b)
gives data bg + εδ_0 + O(ε²). Seeds in the radical of Q are not treated.

### Outside the apparent horizon {#sec:loc-outside}

**Lemma {#lem:loc-transfer}** (From the slice to a static slice.) Let U ⊂ {f > 0} be a band of Σ_τ0 on which the
background is vacuum, of mass μ, with the radial extent of supp δ equal to [R1′, R2′], and let δ be a seed on U.
Extend the slice to a Cauchy surface of the maximally extended Tangherlini spacetime M_μ, and let h be the linearised
vacuum solution with data δ in a harmonic gauge with compactly supported gauge data, so that supp h ⊂ J(supp δ). Then:

(1) Q(δ) = 2∫_Σ Ein²[h](ξ, n) dvol, Ein²[h] the ε² coefficient of Ein(g + εh);

(2) J^a := Ein²[h]^(ab) ξ_b is divergence-free;

(3) for a suitable static slice {t = t_1} of the exterior, h's data there are compactly supported, Q(δ) =
Q_static(h|_(t = t_1)), the charge [[eq:loc-charge]] on that slice, and δ is a gauge seed exactly when h|_(t = t_1) is.

*Proof.* (1) For g_ε := g + εh with data (γ_ε, K_ε), normal n_ε and ξ = N_ε n_ε + Y_ε, [[lem:loc-kid]] (a) gives
N_sℋ + 2Y_s·ℳ = 2Ein_ε(ξ, n_ε) + (N_s − N_ε)ℋ + 2(Y_s − Y_ε)·ℳ, and the last two terms are O(ε³), since Ein_ε =
O(ε²) (Ein(g) = 0 and Ein¹[h] = 0). The ε² coefficient of the left side is ½(N_sD²ℋ + 2Y_s·D²ℳ)[δ, δ] + N_sDℋ[δ_2] +
2Y_s·Dℳ[δ_2], δ_2 the compactly supported second variation of the data, which pairs to zero by [[lem:loc-kid]] (b).
(2) The ε² coefficient of ∇^(ε)_a Ein_ε^(ab) = 0, with Ein¹[h] = 0, is ∇_a Ein²[h]^(ab) = 0, and ∇_(a ξ_b) = 0.
(3) In Kruskal coordinates (U_K, V_K) of the exterior, both increasing to the future, the slice is a curve along which
U_K decreases and V_K increases with R. The support K := supp δ lies in U_K ∈ [U_K(R2′), U_K(R1′)], V_K ∈
[V_K(R1′), V_K(R2′)], and J^±(K) lie in {U_K ≥ U_K(R2′), V_K ≥ V_K(R1′)} and {U_K ≤ U_K(R1′), V_K ≤ V_K(R2′)},
causal curves projecting to causal curves of the orbit space. The rectangles S_in := {U_K(R1′) < U_K < 0, 0 < V_K <
V_K(R1′)} and S_out := {U_K < U_K(R2′), V_K > V_K(R2′)} meet neither. A static slice is a ray V_K = c|U_K|. Take R_a ∈
(√μ, R1′) on the slice and c ∈ (V_K(R_a)/|U_K(R1′)|, V_K(R1′)/|U_K(R1′)|); the ray meets S_in at a point U_K = U_s
slightly above U_K(R1′) with c|U_s| ∈ (V_K(R_a), V_K(R1′)), and S_out at every U_s′ with |U_s′| > max(|U_K(R2′)|,
V_K(R2′)/c); take R_b on the slice with |U_K(R_b)| > |U_s′| and V_K(R_b) > c|U_s′|. Let Σ″ consist of the slice up to
R_a, the segment to (U_s, c|U_s|), which lies in S_in with ΔU_K < 0 < ΔV_K and is spacelike, the ray to U_s′, the
segment to the slice at R_b, in S_out and spacelike, and the slice beyond R_b. Σ″ is spacelike and equals the slice
outside a compact set, so by (2) and the divergence theorem its J-flux is Q(δ). h vanishes on the two segments, and
J(K) meets the ray only inside the part used; near the bifurcation sphere and beyond, the static slice does not meet
J(K). So the flux is that through the whole static slice, which is Q_static of h's data there by (1). Uniqueness up to
gauge of the linearised solution gives the last clause. ∎

On a static slice, γ = dR²/f + R² dΩ₃², N_s = √f, K0 = 0 and Y_s = 0, D²ℋ[(h, k), (h, k)] = D²Scal[h, h] + 2((tr k)² −
|k|²), the mixed terms carrying K0, and the linearised constraints decouple into DScal[h] = 0 and D^i(k_ij − tr k γ_ij)
= 0. So Q = −𝔈_V(h) − 𝔈_K(k), with

    𝔈_V(h) := −½ ∫ N_s D²Scal[h, h] dvol,      𝔈_K(k) := ∫ N_s (|k|² − (tr k)²) dvol.  {#eq:loc-static-energies}

**Lemma {#lem:loc-gauge-invariance}** (Gauge invariance.) For a vector field X and a function ψ_g of compact support,
𝔈_V(h + L_Xγ) = 𝔈_V(h) when DScal[h] = 0, and 𝔈_K(k + k_ψ) = 𝔈_K(k) when D^i(k_ij − tr k γ_ij) = 0, where k_ψ :=
D²ψ_g − ψ_g Ric(γ).

*Proof.* Differentiating Scal(φ_t*(γ + sh)) = φ_t* Scal(γ + sh), φ_t the flow of X, at s = t = 0 gives DScal[L_Xγ] =
X(Scal) = 0 and D²Scal[h, L_Xγ] = X(DScal[h]) − DScal[L_Xh]. So the cross term of 𝔈_V is ½∫N_s X(DScal[h]) −
½∫N_s DScal[L_Xh] = −½∫ div(N_sX) DScal[h] − ½∫⟨(DScal)*N_s, L_Xh⟩ = 0, using DScal[h] = 0 and (DScal)*N_s = D²N_s
− ΔN_s γ − N_s Ric(γ) = 0, the static vacuum equation; the quadratic term vanishes in the same way. For 𝔈_K, the
bilinear form B(k, k_ψ) = ∫N_s(⟨k, k_ψ⟩ − tr k tr k_ψ) dvol is, after two integrations by parts, ∫ψ_g (2dN_s·ℳ[k] +
N_s div ℳ[k]) dvol with ℳ[k] := D^jk_ji − D_i tr k, which vanishes when ℳ[k] = 0; and ℳ[k_ψ] = D^j(D_jD_iψ_g −
ψ_g Ric_ij) − D_i(Δψ_g − ψ_g Scal) = 0 by the contracted Bianchi identity and Scal = 0, so B(k_ψ, k_ψ) = 0. ∎

**Lemma {#lem:loc-scalar-reduction}** (The scalar modes.) On the static slice, a class seed is a sum of scalar modes,
tensor modes and an l = 0 part, and 𝔈_V, 𝔈_K and the constraints split mode by mode. Write a scalar mode of degree l =
2j ≥ 2 as h_RR = aS, h_Rϑ = R b ∂_ϑS, h|_(S³) = R²(cSγ̂ + eŜ), with S := P_j(cos 2ϑ), k² := l(l + 2), Ŝ := D̂D̂S +
(k²/3)γ̂S, and k likewise with (p, q_k, w, z) in place of (a, b, c, e); put x := μ/R², m := k² − 3 and H_KI := m + 6x.

(a) The vector field X = αS∂_R + β̃ ∂_ϑS ∂_ϑ shifts (a, b, c, e) by ((1/f)′α + 2α′/f, α/(Rf) + Rβ̃′, 2α/R −
(2k²/3)β̃, 2β̃), so that b = e = 0 is reached by β̃ = −e/2 and α = −Rf(b − Re′/2); the quantities A := a + (1/f)′α +
2α′/f and F := c/2 − fb + k²e/6 + fRe′/2 are gauge invariant. The direction k_ψ with ψ_g = ψS has trace-free angular
part ψŜ^TF, so z = 0 is reached by ψ = −R²z. Both gauges are local in R.

(b) On the momentum constraint, with Z := R³(w − fq_k), the map Z ↦ (q_k, w, p) = (−3Z′/(R²H_KI), Z/R³ + fq_k, ((4 −
3x)q_k + Rf q_k′ − 2w)/f) solves the constraint and is onto, and per ∫S² sc dϑ,

    𝔈_K = ∫ 6k²m Z²/(R³H_KI²) dR.                                                                       {#eq:loc-ek}

(c) On the Hamiltonian constraint, with the variable ℓ := A − (2R/f)F′ + (2H_KI/(3f²))F, the map ℓ ↦ (A, F), F =
9Rf³(ℓ′ + κ_Mℓ)/(2k²H_KI), A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F, κ_M := (k² + 6 + 6x)/(3Rf), solves the constraint and is
onto; with Φ_M := R^(3/2)f²ℓ/H_KI, per ∫S² sc dϑ,

    𝔈_V = (27m/(2k²)) ∫ (f Φ_M′² + Qp Φ_M²/(16R²H_KI²)) dR,
    Qp := 1296x³ + (624m − 144)x² + 36m(m − 12)x + 16m³ + 60m².                                          {#eq:loc-ev}

(d) The l = 0 part of a seed is a gauge seed: on the constraint, h_(l=0) = L_(RF∂_R)γ for a compactly supported F, and
k_(l=0) = k_ψ with ψ_g = N_s(c_0 + ∫Rw/(fN_s) dR), a constant multiple of N_s on the inner side of the support.

*Proof.* [[pending:computational-2]] ∎

The potential in [[eq:loc-ev]] is Kodama and Ishibashi's scalar potential: fQp/(16R²H_KI²) = V_S, with V_S/f the
function W_S of [[lem:rw-potentials]] at ς = x.

**Lemma {#lem:loc-positivity}** (Positivity.) For class modes, m ∈ {5, 21, 45, …}, and for every x ∈ [0, 1], Qp > 0.

*Proof.* Class modes have l = 2j, so m = 4j(j + 1) − 3. At m = 5, Qp = 1296x³ + 2976x² − 1260x + 3500, and the
quadratic 2976x² − 1260x + 3500 has discriminant 1260² − 4 · 2976 · 3500 = −40076400 < 0, so Qp > 0 for x ≥ 0. For
m = 12 + t with t ≥ 0, every coefficient of Qp as a polynomial in (x, t) is nonnegative (624m − 144 = 7344 + 624t,
36m(m − 12) = 36(12 + t)t) and Qp(0, 0) = 16 · 12³ + 60 · 12² > 0. ∎

**Theorem {#thm:loc-outside}** (Outside the apparent horizon.) Let U ⊂ {f > 0} be a band of Σ_τ0 on which the
background is vacuum. Then Q(δ) ≤ 0 for every seed δ on U, with equality exactly when δ is a gauge seed.

*Proof.* By [[lem:loc-transfer]], Q(δ) = Q_static of a compactly supported seed on a static slice, and δ is gauge
exactly when that seed is. There Q = −𝔈_V − 𝔈_K, unchanged by the compactly supported gauges of
[[lem:loc-scalar-reduction]] (a) ([[lem:loc-gauge-invariance]]), and the modes separate (orthogonality of the class
harmonics of different type and degree, [[lem:loc-harmonics]], the mode sums converging for smooth data). For a scalar
mode, H_KI > 0, f > 0, 27m/(2k²) > 0 and 6k²m/(R³H_KI²) > 0, and Qp > 0 ([[lem:loc-positivity]]), so by
[[eq:loc-ek]] and [[eq:loc-ev]] 𝔈_K ≥ 0 with equality exactly when Z = 0, that is (q_k, w, p) = 0, and 𝔈_V ≥ 0 with
equality exactly when Φ_M = 0, that is ℓ = 0 and (A, F) = 0: the mode is gauge. A tensor mode on the static slice is
[[thm:loc-tensor]] with G = 1/f and Y_s = 0, where −Q = (2π)²|T|²∫(R³Π² + R³f(∂_RH)² + (k_T² + 2)RH²) dR > 0 unless H
= Π = 0. The l = 0 part is gauge and contributes 0 ([[lem:loc-scalar-reduction]] (d)). So Q ≤ 0, and Q = 0 exactly
when every mode is gauge, that is when δ is gauge. ∎

### The sign of the charge {#sec:loc-sign}

**Theorem {#thm:charge-sign}** (The sign of the charge of exactly localised data.) Let U be a band of Σ_τ0 on which the
background is vacuum, and consider invariant data on Σ_τ0 equal to the background's outside a compact subset of U and
of the form bg + εδ + O(ε²), δ a seed on U, ε > 0 small.

(a) *Momentum seeds.* If U lies in the seed region {0.70 ≤ R ≤ 1.861} or in {R ≥ R_*} and δ ≠ 0 has δγ = 0, then
Q(δ) < 0 and no such vacuum data exist for ε small. With matter obeying the dominant energy condition none exist if
f ≥ 0 on U; if U meets {f < 0}, such data exist with outgoing radial null dust.

(b) *Inside the apparent horizon.* If U meets {f < 0}, Q takes both signs on non-gauge seeds of tensor type, and for
every small ε > 0 there are exact vacuum data of this form with δ non-gauge.

(c) *Outside the apparent horizon.* If f > 0 on U, then Q(δ) < 0 for every non-gauge seed δ, and no such vacuum data
with δ non-gauge exist for ε small.

On Σ_τ0, {f < 0} is the part {0.70 ≤ R < √μ3} of the seed region, √μ3 ∈ (0.9066, 0.9068).

*Proof.* (a) is [[cor:loc-charge-seed]] and [[thm:loc-matter]]; (b) is [[thm:loc-inside]]; (c) is [[thm:loc-outside]]
with [[prop:loc-projection]] (a). The last statement: on the seed region, in region III, f = 1 − μ3/R², and √μ3 lies
in the stated interval by [[thm:bg-margins]] (a). ∎

The sets {f < 0} and {f > 0} are where the round spheres are trapped and where they are not; nothing above uses the
event horizon. In the class, −Q on a static slice is the sum over the even harmonics of the energies of Kodama and
Ishibashi's master equations, scalar and tensor, whose potentials are positive in five dimensions for every l ≥ 2:
for the scalar potential, Qp > 0 on x ∈ [0, 1] holds for m = 5 and for every m ≥ 12 by the proof of
[[lem:loc-positivity]], which covers m = l(l + 2) − 3 for every l ≥ 2.

### The background below R_* {#sec:bg-below}

This section proves the properties of the background of the angle-localised families that the margins of the bent slice
and of the seed region use below R_*: the data on 𝒞_in and the mass μ3 of region III ([[prop:bg-nprime]]); that the
background's ψ_III lies in the tube of [[prop:margins-seed]] (b) around the explicit quintic ψ_s
([[prop:bg-seed]]); and the hyperbolicity margin κK^l_l on Σ_τ0 for 0.68 ≤ R ≤ R_* ([[prop:bg-slice]]). The results
are collected in [[thm:bg-margins]]. Below R_* the background reduces exactly to ordinary differential equations along
null rays ([[lem:bg-reduction]]). Their solutions are enclosed by explicit approximants with a posteriori bounds
([[prop:bg-nprime]], [[prop:bg-rays]]). The approximants and every row of the bounds are printed in [[sec:tab-bg]].

#### The data and the reduction {#sec:bg-data}

Put u1 := 5.7, u2 := 7.2 and τ0 := −0.68. With the bump β(w) = exp(1 − 1/(1 − w²)) for |w| < 1, β(w) = 0 otherwise,
and b(x; a, c) = β((2x − a − c)/(c − a)), both as in [[sec:table-bump]], put

    ℬ(u) := 1.7 b(u; 5.7, 7.2),        𝒜(v) := 3.6 b(v; 3, 4.5).                                       {#eq:bg-profiles}

The background is the spherically symmetric metric g0 = −2e^(2σ) du dv + R² dΩ₃² of
[[sec:two-dust-background]]
with an outgoing null dust of profile ℬ(u) and an ingoing one of profile 𝒜(v), so that ([[ch:two-dusts]])

    R_uu − 2σ_u R_u = −ℬ/(3R²),     R_vv − 2σ_v R_v = −𝒜/(3R²),     R R_uv = −e^(2σ) − 2R_u R_v,       {#eq:bg-field}

with the characteristic data e^(2σ) = 1/2 on 𝒞_out = {u = 0} and on 𝒞_in = {v = 0}, and R = 5, R_u = −0.47, R_v = 1/2 at
the corner. The mass function is μ := R²(1 + 2e^(−2σ) R_u R_v), and f := 1 − μ/R² = −2e^(−2σ) R_u R_v. Let v̂(v) be
the ingoing coordinate with v̂(0) = 0 and ψ = 0 on 𝒞_out, where

    ψ := ln(−e^(2σ)/(R_u v̂′(v))),      g0 = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃²   where R_u ≠ 0,     {#eq:bg-chart}

the second identity following from du = (dR − R_v dv)/R_u. The slice is Σ_τ0 := {v̂ − R = τ0}. Put

    F(R) := 2R + √(3/2) ln((R − √(3/2))/(R + √(3/2))),      F′(R) = 2/(1 − 3/(2R²)),  {#eq:bg-tangherlini}

the null function of Tangherlini's metric of mass 3/2, and for ρ > √(3/2)

    v̂(ρ) := F(ρ) − F(2.321),    f1(ρ) := 1 − 3/(2ρ²),    a(ρ) := f1(ρ)/2,    a′(ρ) = 3/(2ρ³).           {#eq:bg-label}

**Lemma {#lem:bg-identities}** (Identities.) A solution of [[eq:bg-field]] satisfies

    μ_u = −(2/3) ℬ e^(−2σ) R_v,    μ_v = −(2/3) 𝒜 e^(−2σ) R_u,    ψ_u = ℬ/(3R² R_u),
    (e^(−2σ) R_v)_v = −𝒜 e^(−2σ)/(3R²),    (e^(−2σ) R_u)_u = −ℬ e^(−2σ)/(3R²).

Proof. Differentiating, μ_u = 2RR_u + 4Re^(−2σ)R_u²R_v + 2R²e^(−2σ)R_v(R_uu − 2σ_uR_u) + 2R²e^(−2σ)R_uR_uv. By the
third equation of [[eq:bg-field]] the last term is −2RR_u − 4Re^(−2σ)R_u²R_v, and by the first the third term is
−(2/3)Be^(−2σ)R_v. The identity for μ_v follows in the same way with u and v exchanged. The two others are e^(−2σ)
times the first two equations of [[eq:bg-field]], and ψ_u = 2σ_u − R_uu/R_u = ℬ/(3R²R_u) by the first. ∎

**Lemma {#lem:bg-reduction}** (Reduction to rays.) Let ℛ := {v < 3}.

(a) *The data on 𝒞_in.* R(u) := R(u, 0) solves R″ = −ℬ/(3R²) with R(u1) = 2.321, R′(u1) = −0.47, and S(u) := R²R_v(u,
0) solves S′ = −R/2 with S(u1) = 2.067575. The functions μ(u) := μ(u, 0) and λ(u) := 2R_v(u, 0) are

    μ = R² + 4R′S,     λ = 2S/R²,     μ′ = −(2/3) ℬ λ,     λ′ = −μ/R³.                                   {#eq:bg-nprime}

(b) *Region I.* On {u ≤ u1} ∩ ℛ, μ = 3/2 and ψ = 0, so g0 is Tangherlini's metric of mass 3/2 in ingoing
coordinates; along the outgoing ray u = u1, v̂ = F(R) − F(2.321). The ingoing ray of label v̂ meets u = u1 at R = ρ,
where v̂ = v̂(ρ) in the notation [[eq:bg-label]]; we label rays by ρ.

(c) *The rays.* On ℛ, μ(u, v) = μ(u) and e^(−2σ)R_v(u, v) = λ(u), and R_u < 0. Where λ(u) > 0, along every ingoing ray

    R_u = G(u, R),        G(u, X) := −(1 − μ(u)/X²)/(2λ(u)).                                              {#eq:bg-ray}

Write Ψ(u, ρ) for the solution of [[eq:bg-ray]] with Ψ(u1, ρ) = ρ, and J := ∂_ρΨ, K := ∂_ρ²Ψ, L := ∂_ρ³Ψ.

(d) *The packet.* At a point of ℛ with u1 ≤ u ≤ u2 and f > 0, on the ray ρ, in the chart [[eq:bg-chart]],

    q := e^ψ = 2aJ/f,    ψ_R = ℬ/(3R²G²),    f_R = 2μ/R³ − μ′/(R²G),    f_v̂ = μ′ J a/(R²G),
    ψ_v̂ = aK/J + a′ − 2μJa/(R³f) − (Ja/G) ℬ/(3R²G),                                                    {#eq:bg-inputs}

with R = Ψ(u, ρ), G = G(u, R), a = a(ρ), μ = μ(u), μ′ = μ′(u), ℬ = ℬ(u).

(e) *Region III.* On {u ≥ u2} ∩ ℛ, μ = μ3 := μ(u2) and ψ = ψ_III(v̂), where for the ray ρ, with Φ(ρ) := Ψ(u2, ρ)
and f3(X) := 1 − μ3/X²,

    ψ_III(v̂(ρ)) = ln Φ′(ρ) + ln f1(ρ) − ln f3(Φ(ρ)),  {#eq:bg-psi3-def}

provided f3(Φ(ρ)) > 0. There g0 = −e^(2ψ_III) f3 dv̂² + 2e^(ψ_III) dv̂ dR + R² dΩ₃².

(f) *The slice.* Every point of Σ_τ0 with 0.68 ≤ R ≤ R_*, R_* as in [[lem:bg-rstar]], lies in ℛ, on the ray ρ with
v̂(ρ) − R = τ0 and 2.321 ≤ ρ ≤ R_*.

Proof. (a) On 𝒞_in, σ is constant, so [[eq:bg-field]] gives R″ = −ℬ/(3R²) and R R_uv = −1/2 − 2R′R_v; hence S′ = 2RR′R_v
+ R²R_uv = −R/2. Since ℬ = 0 on [0, u1], R = 5 − 0.47u there, so R(u1) = 2.321, and S(u1) = 25/2 − (1/2)∫_0^(u1) (5 −
0.47u) du = 2.067575. With e^(−2σ) = 2, μ = R²(1 + 4R′R_v) = R² + 4R′S and λ = 2S/R². Then μ′ = −(2/3)ℬλ by
[[lem:bg-identities]], and λ′ = 2R_uv = −(1 + 4R′R_v)/R = −μ/R³.

(b) On {u ≤ u1}, ℬ = 0, and on ℛ, 𝒜 = 0. By [[lem:bg-identities]] μ_u = μ_v = 0, so μ equals its corner value
25(1 − 0.94) = 3/2, and ψ_u = 0, so ψ = 0 as on 𝒞_out. In [[eq:bg-chart]] the outgoing null directions satisfy dv̂/dR =
2/f = F′(R); the ray u = u1 meets 𝒞_in at v̂ = 0, R = 5 − 0.47 u1 = 2.321.

(c) On ℛ, 𝒜 = 0, so [[lem:bg-identities]] gives μ_v = 0 and (e^(−2σ)R_v)_v = 0; hence μ and e^(−2σ)R_v take their
values on 𝒞_in. On 𝒞_out, R_u = (3/(2R²) − 1)/2 < 0 for v ≤ 3 (there μ = 3/2, R = 5 + v/2, e^(−2σ) = 2), and
(e^(−2σ)R_u)_u ≤ 0, so R_u < 0 on ℛ. Finally f = −2e^(−2σ)R_uR_v = −2λR_u.

(d) On ℛ, e^(2σ) = R_v/λ and λR_u = −f/2, so e^ψ = −R_v/(λR_u v̂′) = (2/f) ∂_v̂R|_u, and ∂_v̂R|_u = J dρ/dv̂ = Ja.
The derivatives in the chart [[eq:bg-chart]] follow from ∂_R|_v̂ = G⁻¹∂_u and ∂_v̂|_R = ∂_v̂|_u − (Ja/G)∂_u: f_R =
2μ/R³ − μ′/(R²G), f_v̂ = μ′Ja/(R²G), ψ_R = ψ_u/G = ℬ/(3R²G²) by [[lem:bg-identities]], and ψ_v̂ = ∂_v̂ ln(2Ja/f)|_u −
(Ja/G)ψ_u, where ∂_v̂ J|_u = Ka, ∂_v̂ a = aa′ and ∂_v̂ f|_u = 2μJa/R³.

(e) On {u ≥ u2}, ℬ = 0, so μ_u = ψ_u = 0 ([[lem:bg-identities]]; R_u ≠ 0 by (c)): μ and ψ take their values on u =
u2. There (d) gives e^ψ = 2aΦ′/f3(Φ) = f1Φ′/f3(Φ).

(f) On Σ_τ0, v̂ = R + τ0 ≤ R_* − 0.68 < 2.7572, while v̂(3) = F(6.5) − F(5) > 3.1453 (on 𝒞_out before the shell R = 5 +
v/2 and dv̂/dR = F′(R)); v̂ is increasing in v, so the point lies in ℛ. Its ray meets u = u1 at the ρ with v̂(ρ) = v̂ ≤
R_* − 0.68, so ρ ≤ R_* by the definition of R_*; and v̂ ≥ 0 gives ρ ≥ 2.321. ∎

**Lemma {#lem:bg-rstar}** (The radius R_*.) Let R_* be the radius at which the ray u = u1 meets Σ_τ0, that is the
zero of τ(R) := F(R) − F(2.321) − R + 0.68 on R > 2.321. Then R_* is unique and 3.43718006 ≤ R_* ≤ 3.43718007.

Proof. τ′(R) = 2/f1(R) − 1 > 0, τ(3.43718006) ≤ −8.4 × 10⁻⁹ and τ(3.43718007) ≥ 4.4 × 10⁻⁹, by direct evaluation of
[[eq:bg-tangherlini]] at these two decimals. ∎

**Lemma {#lem:bg-slice-forms}** (The margin on Σ_τ0.) At a point of Σ_τ0 in ℛ, in the chart [[eq:bg-chart]] with q :=
e^ψ > 0 and qf < 2 (f of either sign), the radial extrinsic curvature κ and the sphere trace K^l_l of
[[lem:racz-split-formulas]] satisfy

    κ K^l_l = 3 N_κ (1 − qf)/(q R (2 − qf)²),
    N_κ := q²f²ψ_R + q²f f_R/2 − 3qfψ_R − qf_v̂/2 − 3qf_R/2 − ψ_v̂ + ψ_R,                                 {#eq:bg-kk}

and κ > 0, K^l_l < 0 exactly when N_κ < 0 and qf < 1. In the packet (u1 ≤ u ≤ u2, f > 0, inputs [[eq:bg-inputs]]),

    N_κ = −(μq/R³)(2 − qf) − aK/J − a′ + ℬ λ² (2 − qf)²/(3R²f²),        q f = 2aJ,  {#eq:bg-nk-packet}

and in region III, N_κ = (μ3q/R³)(qf − 3) − ψ_III′(v̂).

Proof. Since q > 0 and qf < 2, 2/q − f = (2 − qf)/q > 0. By [[lem:racz-split-formulas]],
κ = −N_κ/(q√(2/q − f)(2 − qf)) and K^l_l = 3(qf − 1)/(qR√(2/q − f)), and q²(2/q − f) = q(2 − qf); this gives the
product, and since q, R, √(2/q − f) and 2 − qf are positive, κ > 0 exactly when N_κ < 0 and K^l_l < 0 exactly when
qf < 1. In the packet substitute [[eq:bg-inputs]] with qf = 2aJ and μ′ = −(2/3)ℬλ: the terms without ℬ give
(μq/R³)(qf − 3) − (aK/J + a′ − μq/R³), using 2μJa/(R³f) = μq/R³; the terms in ℬ are ℬ times
(4λ²/(3R²f²))[(qf)² − (5/2)qf + 1 − qf((3/4)qf − 3/2)] = ℬλ²(2 − qf)²/(3R²f²). In region III, ψ_R = f_v̂ = 0 and
f_R = 2μ3/R³. ∎

#### Elementary bounds {#sec:bg-tools}

**Lemma {#lem:bg-tools}** (Elementary bounds.)

(a) *Chebyshev sums.* If p(x, y) = Σ c_(ij) T_i(x)T_j(y) is a polynomial, T_i the Chebyshev polynomials, then on
[−1, 1]² it lies in [c_00 − ς′, c_00 + ς′], ς′ := Σ_((i,j)≠(0,0)) |c_(ij)|; in particular |p| ≤ Σ |c_(ij)|. On a box
[a, b] × [c, d] the same holds for the coefficients in the variables x = (u − (a + b)/2)/((b − a)/2), y likewise; a
polynomial written in powers of x has Chebyshev coefficients given by x^n = 2^(1−n) Σ′_(k ≤ n/2) C(n, k) T_(n−2k)(x),
the prime halving the term T_0.

(b) *Cauchy.* If g is holomorphic on a neighbourhood of {|z − c| ≤ r}, |g| ≤ M there, and g_n are its Taylor
coefficients at c, then for real x with |x − c| ≤ h < r and every N, |g(x)| ≤ Σ_(n<N) |g_n|hⁿ + M(h/r)^N/(1 − h/r).

(c) *Taylor.* If g ∈ C^(N+1)[c − h, c + h], then |g(x)| ≤ Σ_(n≤N) |g^(n)(c)|hⁿ/n! + h^(N+1) sup |g^(N+1)|/(N + 1)!.

(d) *Enclosures.* If x ∈ X and y ∈ Y for closed intervals X, Y, then x + y, x − y, xy and (if 0 ∉ Y) x/y lie in the
intervals spanned by the corresponding combinations of the endpoints, and φ(x) ∈ φ(X) for φ = exp, ln, √ (monotone).
Replacing each operation of an explicit expression by this rule encloses the expression's range on a box.

(e) *The bump.* β is increasing on (−1, 0] and decreasing on [0, 1). For real w0 and complex w with |w − w0| ≤ ϱ <
1 − |w0|,

    |β(w)| ≤ exp(1 − (1/2)(1/(1 − w0 + ϱ) + 1/(1 + w0 + ϱ))),  {#eq:bg-bump-disc}

and β(w0 + t) = exp(Σ_n g_n tⁿ) with g_0 = 1 − 1/(1 − w0²) and g_n = −(1/2)((1 − w0)^(−n−1) + (−1)ⁿ(1 + w0)^(−n−1))
for n ≥ 1; its Taylor coefficients are e_0 = e^(g_0), n e_n = Σ_(k=1)^n k g_k e_(n−k).

(f) *Power series.* Let p = Σ p_n tⁿ and q = Σ q_n tⁿ be the Taylor series at a point of two smooth functions. The
Taylor coefficients there of p + q, pq, r := p/q (q_0 ≠ 0), e := exp p, ℓ := ln p (p_0 > 0) and the derivative p′ are
p_n + q_n, Σ_(k≤n) p_k q_(n−k), and, with e_0 = exp p_0 and ℓ_0 = ln p_0,

    q_0 r_n = p_n − Σ_(k=1)^n q_k r_(n−k),     (p′)_n = (n + 1) p_(n+1),
    n e_n = Σ_(k=1)^n k p_k e_(n−k),     n p_0 ℓ_n = n p_n − Σ_(k=1)^(n−1) k ℓ_k p_(n−k)   (n ≥ 1).  {#eq:bg-series}

Proof. (a) |T_i| ≤ 1 on [−1, 1], and the expansion of xⁿ is the binomial expansion of ((e^(iθ) + e^(−iθ))/2)ⁿ. (b)
Cauchy's estimate |g_n| ≤ M/rⁿ bounds the terms n ≥ N. (c) Taylor's formula with Lagrange's remainder. (d) is
elementary. (e) 1/(1 − w²) = (1/2)(1/(1 − w) + 1/(1 + w)). The disc 1 − w ∈ {|ζ − (1 − w0)| ≤ ϱ} does not contain 0,
and ζ ↦ 1/ζ maps it onto the disc with real diameter [1/(1 − w0 + ϱ), 1/(1 − w0 − ϱ)], so Re 1/(1 − w) ≥ 1/(1 − w0 +
ϱ); likewise for 1 + w; and |e^(1−Z)| = e^(1−Re Z). The series of ln β = 1 − 1/(1 − w²) follows from the two
geometric series, and n e_n = Σ k g_k e_(n−k) from (exp g)′ = g′ exp g. (f) Compare the coefficients of tⁿ in
rq = p, and of tⁿ⁻¹ in e′ = p′e and in pℓ′ = p′. ∎

**Lemma {#lem:bg-comparison}** (Comparison.)

(a) If e ∈ C²[a, b], |e″| ≤ Λ|e| + δ with Λ > 0, δ ≥ 0, |e(a)| ≤ E₀ and |e′(a)| ≤ E₁, then with k := √Λ and t := u −
a,

    |e(u)| ≤ E₀ cosh kt + E₁ (sinh kt)/k + δ (cosh kt − 1)/Λ,
    |e′(u)| ≤ E₀ k sinh kt + E₁ cosh kt + δ (sinh kt)/k.  {#eq:bg-comparison-2}

(b) If e is absolutely continuous on [a, b] and e′ = −p e + r with p ≥ 0 continuous and r integrable, then |e(u)| ≤
|e(a)| + ∫_a^u |r|.

Proof. (a) By Taylor's formula, m(t) := |e(a)| + |e′(a)| t + ∫_0^t (t − s)(Λ|e(a + s)| + δ) ds satisfies |e(a + t)| ≤
m(t), m″ = Λ|e| + δ ≤ Λm + δ, m(0) ≤ E₀, m′(0) ≤ E₁. The right side of the first line of [[eq:bg-comparison-2]], call it
𝓔(t), solves 𝓔″ = Λ𝓔 + δ with 𝓔(0) = E₀, 𝓔′(0) = E₁. Then z := 𝓔 − m has z″ − Λz = 𝓆 ≥ 0 and z(0), z′(0) ≥ 0, so z(t)
= z(0) cosh kt + z′(0)(sinh kt)/k + ∫_0^t (sinh k(t − s)/k) 𝓆(s) ds ≥ 0. Then |e′(a + t)| ≤ E₁ + ∫_0^t (Λ𝓔 + δ) =
𝓔′(t). (b) e(u) = e^(−P(u)) e(a) + ∫_a^u e^(P(s)−P(u)) r(s) ds with P(u) := ∫_a^u p, and P is nondecreasing. ∎

#### The data on 𝒞_in {#sec:bg-nprime}

The approximant R̂ is the piecewise polynomial of [[sec:tab-bg-nprime]] on twelve segments of [u1, u2]: affine on
[5.7, 5.73] (the data line) and on [7.17, 7.2], and a polynomial of degree 12 to 17 on each of the ten middle segments,
which are graded towards the ends of the packet. Put

    Ŝ(u) := 2.067575 − (1/2)∫_(u1)^u R̂,     μ̃ := R̂² + 4R̂′Ŝ,     λ̃ := 2Ŝ/R̂²,  {#eq:bg-nprime-approx}

so that Ŝ and μ̃ are polynomials and λ̃ is a rational function on each segment, and μ̃3 := R̂(u2)² + 4R̂′(u2)Ŝ(u2) =
0.82211255682735… (an explicit rational).

**Proposition {#prop:bg-nprime}** (The data on 𝒞_in.) On each segment [a, b] of [[sec:tab-bg-nprime-chain]], |R − R̂| ≤
E₀ and |R′ − R̂′| ≤ E₁ with E₀, E₁ of that row, and |S − Ŝ| ≤ I/2. In particular |R − R̂| ≤ 4.53 × 10⁻⁸, |R′ − R̂′| ≤
9.20 × 10⁻⁸ and |S − Ŝ| ≤ 1.82 × 10⁻⁸ on [u1, u2], and

(i) R(u2) ∈ [1.5193579, 1.5193581] ⊂ [1.519357, 1.519359];

(ii) |μ3 − μ̃3| ≤ 4.07 × 10⁻⁷, so μ3 ∈ [0.82211214, 0.82211297] ⊂ [0.8220998, 0.8221253], and R(u2)² > μ3;

(iii) μ is nonincreasing, 3/2 ≥ μ ≥ μ3, and λ is decreasing with λ ≥ λ(u2) ≥ 0.529533 > 0.529 on [u1, u2];

(iv) at every u ∈ [u1, u2], with E₀, E₁, I of a segment containing u and R̂, R̂′, Ŝ at u,

    |μ − μ̃| ≤ (2R̂ + E₀)E₀ + 4(|R̂′| I/2 + ŜE₁ + E₁I/2),      |λ − λ̃| ≤ (I + 2Ŝ(2R̂ + E₀)E₀/R̂²)/(R̂ − E₀)²;

in particular |μ − μ̃| ≤ 4.2 × 10⁻⁷ and |λ − λ̃| ≤ 5 × 10⁻⁸ on [u1, u2].

Proof. Let δ(u) := R̂″ + ℬ/(3R̂²) on a segment. On the ten middle segments δ is holomorphic on the disc |u − c| ≤ r, r =
(4/5)min(c − u1, u2 − c), since ℬ is holomorphic off u1 and u2 ([[lem:bg-tools]] (e)) and |R̂| > 0 there; on the
disc, |R̂″| ≤ Σ n(n − 1)|q_n|(r/h)^(n−2)/h², |R̂| ≥ q_0 − Σ_(n≥1)|q_n|(r/h)ⁿ and |ℬ| is bounded by [[eq:bg-bump-disc]]
with w0 = (c − 6.45)/0.75, ϱ = r/0.75. This gives M. The Taylor coefficients δ_n of δ at c follow from those of ℬ
([[lem:bg-tools]] (e)) by multiplication and division of power series, and [[lem:bg-tools]] (b) with N = 60 gives the
bound δ of [[sec:tab-bg-nprime-defects]]. On the outer segments R̂″ = 0 and |δ| = ℬ/(3R̂²) ≤ ℬ_max/(3R̂_min²), ℬ being
monotone there.

The error e := R − R̂ satisfies e″ = −(ℬ/3)(1/R² − 1/R̂²) − δ, and |1/R² − 1/R̂²| = |e|(R + R̂)/(R²R̂²). While |e| ≤
10⁻⁶ this gives |e″| ≤ Λ|e| + δ with the Λ of [[sec:tab-bg-nprime-chain]]. On the first segment e(u1) = e′(u1) = 0;
on each later one the initial bounds are the previous segment's E₀, E₁ plus the jumps j₀, j₁ of R̂ and R̂′ (exact
differences of the two polynomials at the common end). [[lem:bg-comparison]] (a) gives E₀, E₁ row by row; since
[[eq:bg-comparison-2]] is increasing in t they bound |e|, |e′| on the whole segment. They stay below 4.53 × 10⁻⁸ <
10⁻⁶, so by continuity the hypothesis |e| ≤ 10⁻⁶ holds on every segment. Then S − Ŝ = −(1/2)∫_(u1)^u e by
[[lem:bg-reduction]] (a), and I accumulates the segment lengths times E₀.

Since R̂ ≥ R̂_min > 1.5 on every segment ([[sec:tab-bg-nprime-chain]]), Ŝ′ = −R̂/2 < 0, so Ŝ decreases from 2.067575
to Ŝ(u2) = 0.61120057465952… ([[sec:tab-bg-nprime]]) and is positive on [u1, u2]; and R ≥ R̂ − E₀ > 1.5. The column
I does not decrease down the rows, so |S − Ŝ| ≤ I/2 ≤ (3.63 × 10⁻⁸)/2 < 1.82 × 10⁻⁸ on [u1, u2], by the last row.

(iv) At u, μ − μ̃ = (R² − R̂²) + 4(R̂′(S − Ŝ) + (R′ − R̂′)Ŝ + (R′ − R̂′)(S − Ŝ)) and λ − λ̃ = 2(S − Ŝ)/R² + 2Ŝ(R̂² −
R²)/(R²R̂²), where |R² − R̂²| = |e|(R + R̂) ≤ (2R̂ + E₀)E₀, |S − Ŝ| ≤ I/2, Ŝ > 0 and R ≥ R̂ − E₀ > 0; this gives the two
bounds. On each segment they are at most 4.17 × 10⁻⁷ and 4.89 × 10⁻⁸ when R̂ is replaced by R̂_max in the numerators
and by R̂_min in the denominators, |R̂′| by R̂′_max of [[sec:tab-bg-ray-chain]] and Ŝ by its value at the left end;
both largest values occur on [7.17, 7.2].

(i) R̂(u2) = 1.5193579823987569 exactly. (ii) The bound (iv) at u = u2, with the exact values R̂(u2), R̂′(u2) =
−0.60795759341336… and Ŝ(u2) and the last row's E₀, E₁, I, gives |μ3 − μ̃3| ≤ 4.068 × 10⁻⁷; and R(u2)² ≥ 2.308 > 0.823.

(iii) Since Ŝ ≥ Ŝ(u2) and |S − Ŝ| ≤ 1.82 × 10⁻⁸, S ≥ Ŝ(u2) − 1.82 × 10⁻⁸ > 0.6111 on [u1, u2], so λ = 2S/R² > 0 there.
Since ℬ ≥ 0, [[eq:bg-nprime]] gives μ′ = −(2/3)ℬλ ≤ 0, so μ is nonincreasing and 3/2 = μ(u1) ≥ μ ≥ μ3 > 0 by (ii), where
μ(u1) = 2.321² − 4(0.47)(2.067575) = 3/2. Hence λ′ = −μ/R³ < 0, so λ is decreasing on [u1, u2] and λ ≥ λ(u2) =
2S(u2)/R(u2)² ≥ 2(Ŝ(u2) − I/2)/(R̂(u2) + E₀)² ≥ 0.529533. ∎

#### The rays {#sec:bg-rays}

The ray approximant Ψ̃ is the polynomial of [[sec:tab-bg-ray]] on [u1, u2] × [2.32, 3.44], of degree 24 in u and 12 in
ρ; put J̃ := ∂_ρΨ̃, K̃ := ∂_ρ²Ψ̃, L̃ := ∂_ρ³Ψ̃. On each segment of R̂ let

    G̃(u, X) := R̂²(μ̃ − X²)/(4ŜX²),     D := ∂_uΨ̃ − G̃(u, Ψ̃),     D_m := ∂_ρ^m D  (m ≤ 3),  {#eq:bg-ray-approx}

so that G̃ is [[eq:bg-ray]] with μ, λ replaced by μ̃, λ̃, and D_1, D_2, D_3 are the defects of J̃, K̃, L̃ in the
variational equations of [[eq:bg-ray]] (for G̃). The polynomial

    P := 4ŜΨ̃² ∂_uΨ̃ − R̂²(μ̃ − Ψ̃²) = 4ŜΨ̃² D  {#eq:bg-ray-numerator}

has Chebyshev sums ς_m of ∂_ρ^m P on each box [a, b] × [2.32, 3.44]. Since Ŝ does not depend on ρ, D = (P/(4Ŝ)) Ψ̃^(−2)
and Leibniz's rule give

    |D_m| ≤ Σ_(j≤m) C(m, j) (ς_(m−j)/(4Ŝ_min)) g_j,    g_0 = Ψ̃_min^(−2),  g_1 = 2J̄Ψ̃_min^(−3),
    g_2 = 6J̄²Ψ̃_min^(−4) + 2K̄Ψ̃_min^(−3),
    g_3 = 24J̄³Ψ̃_min^(−5) + 18J̄K̄Ψ̃_min^(−4) + 2L̄Ψ̃_min^(−3),  {#eq:bg-ray-defects}

J̄, K̄, L̄ the bounds of |J̃|, |K̃|, |L̃| on the box ([[sec:tab-bg-ray-defects]]).

The fields G and G̃ differ through the data. Write G = Q/(2X²) − V/2 with Q := μ/λ = R⁴/(2S) + 2R′R² and V := 1/λ =
R²/(2S), and Q̃, Ṽ likewise from R̂, Ŝ. On a segment, with R̄ := R̂_max + E₀, R̄′ := R̂′_max + E₁ (R̂′_max ≥ |R̂′|
is the bound of [[sec:tab-bg-ray-chain]]), S̲ := Ŝ_min − I/2 and X̲ := Ψ̃_min − 10⁻⁵, the mean value theorem in (R,
R′, S) gives |Q − Q̃| ≤ Δ₁, |V − Ṽ| ≤ Δ₂ with

    Δ₁ := (2R̄³/S̲ + 4R̄′R̄) E₀ + 2R̄² E₁ + (R̄⁴/(2S̲²)) I/2,      Δ₂ := (R̄/S̲) E₀ + (R̄²/(2S̲²)) I/2,
    γ_0 := Δ₁/(2X̲²) + Δ₂/2,   γ_1 := Δ₁/X̲³,   γ_2 := 3Δ₁/X̲⁴,   γ_3 := 12Δ₁/X̲⁵,  {#eq:bg-gamma}

and |∂_X^m(G − G̃)| ≤ γ_m (m ≤ 3) on the tube

    {(u, X): |X − Ψ̃(u, ρ)| ≤ 10⁻⁵ for some ρ ∈ [2.32, 3.44]},                                             {#eq:bg-tube}

where also |∂_X^m G| ≤ H_m := c_m (3/2)/(0.529533 X̲^(m+2)), (c_2, c_3, c_4) = (3, 12, 60), by
[[prop:bg-nprime]] (iii) and ∂_X^m G = (−1)^m (m + 1)! μ/(2λX^(m+2)) for m ≥ 1.

**Proposition {#prop:bg-rays}** (The rays.) For u ∈ [a, b], a segment of [[sec:tab-bg-ray-chain]], and ρ ∈ [2.32, 3.44],

    |Ψ − Ψ̃| ≤ ε₀,   |J − J̃| ≤ ε₁,   |K − K̃| ≤ ε₂,   |L − L̃| ≤ ε₃,

with the ε of that row. At u = u2: ε₀ = 8.69 × 10⁻⁷, ε₁ = 1.68 × 10⁻⁶, ε₂ = 6.10 × 10⁻⁶, ε₃ = 3.65 × 10⁻⁵. Moreover 0
< J ≤ 1, and the rays satisfy Ψ(u, ρ) > √μ(u) on [u1, u2] × [2.32, 3.44].

Proof. Fix ρ. By [[prop:bg-nprime]] (iii), λ > 0 on [u1, u2], so [[eq:bg-ray]] holds along the ray, and ∂_XG = −μ/(λX³)
< 0 for X > 0. Let e₀ := Ψ − Ψ̃. Then e₀′ = −p e₀ + r with p := −∫_0^1 ∂_XG(u, Ψ̃ + θe₀) dθ ≥ 0 and r := (G −
G̃)(u, Ψ̃) − D. While |e₀| ≤ 10⁻⁵, [[lem:bg-comparison]] (b) gives |e₀(u)| ≤ |e₀(a)| + (u − a)(γ_0 + D₀). For e₁ := J
− J̃, differentiating [[eq:bg-ray]] in ρ, e₁′ = ∂_XG(u, Ψ)e₁ + (∂_XG(u, Ψ) − ∂_XG(u, Ψ̃))J̃ + (∂_XG − ∂_XG̃)(u, Ψ̃)J̃ −
D_1, whose last three terms are at most H_2ε₀J̄ + γ_1J̄ + D₁; the same lemma applies with p = −∂_XG(u, Ψ) ≥ 0. For
e₂ and e₃ the variational equations K′ = ∂_XG K + ∂_X²G J² and L′ = ∂_XG L + 3∂_X²G JK + ∂_X³G J³ give in the same
way

    ε₀(b) = ε₀(a) + (b − a)(γ_0 + D₀),
    ε₁(b) = ε₁(a) + (b − a)(H_2ε₀J̄ + γ_1J̄ + D₁),
    ε₂(b) = ε₂(a) + (b − a)((H_2ε₀ + γ_1)K̄ + H_2ε₁(2J̄ + ε₁) + (H_3ε₀ + γ_2)J̄² + D₂),
    ε₃(b) = ε₃(a) + (b − a)((H_2ε₀ + γ_1)L̄ + 3(H_2(ε₁K̄ + J̄ε₂ + ε₁ε₂) + (H_3ε₀ + γ_2)J̄K̄)
                   + H_3ε₁(3J̄² + 3J̄ε₁ + ε₁²) + (H_4ε₀ + γ_3)J̄³ + D₃),  {#eq:bg-ray-chain}

the ε on the right without argument being those at b, taken in the order m = 0, 1, 2, 3. The bounds |J² − J̃²| ≤
ε₁(2J̄ + ε₁), |JK − J̃K̃| ≤ ε₁K̄ + J̄ε₂ + ε₁ε₂ and |J³ − J̃³| ≤ ε₁(3J̄² + 3J̄ε₁ + ε₁²) enter here. The initial values
at u1 are the sums of [[sec:tab-bg-ray-chain]] ([[lem:bg-tools]] (a)), the defects are bounded by [[eq:bg-ray-defects]]
and the rows of [[sec:tab-bg-ray-defects]], the γ_m by [[eq:bg-gamma]] and the H_m by the bound after [[eq:bg-tube]].
Since ε₀ ≤ 8.69 × 10⁻⁷ < 10⁻⁵ everywhere,
the hypothesis |e₀| ≤ 10⁻⁵ holds throughout by continuity.

J = exp(∫_(u1)^u ∂_XG(s, Ψ) ds) ∈ (0, 1]. Finally Ψ ≥ Ψ̃_min − ε₀ ≥ 1.4832 on every segment
([[sec:tab-bg-ray-defects]]), while μ ≤ 3/2 < 1.4832²: so f > 0 along every ray of the box. ∎

#### Region III and the seed region {#sec:bg-seed}

Let Φ := Ψ(u2, ·), Φ̃ := Ψ̃(u2, ·), a polynomial of degree 12 in ρ (its Chebyshev coefficients C_k are the column sums
of [[sec:tab-bg-ray]]). By [[eq:bg-psi3-def]] and d/dv̂ = a(ρ) d/dρ, the derivatives of ψ_III are ψ_III^(k)(v̂(ρ)) =
Ψ_k(ρ, Φ(ρ), Φ′(ρ), Φ″(ρ), Φ‴(ρ), μ3), where

    Ψ_0 := ln Φ′ + ln f1(ρ) − ln f3(Φ),    Ψ_1 := a(ρ) 𝒟Ψ_0,    Ψ_2 := a(ρ) 𝒟Ψ_1,                       {#eq:bg-psi3}

𝒟 the total derivative in ρ (Φ^(j) ↦ Φ^(j+1)). Explicitly, with h3(X) := 1/(X³ − μ3X),

    Ψ_1 = a(Φ″/Φ′) + a′ − 2μ3 a Φ′ h3(Φ),     Ψ_2 = a 𝒟Ψ_1,

that is Ψ_1 = aΦ″/Φ′ + a′ − μ3q/Φ³ with q = f1Φ′/f3(Φ), which is ψ_v̂ of [[eq:bg-inputs]] at u = u2, where ℬ = 0.

**Proposition {#prop:bg-seed}** (Region III and the seed region.) Let ψ_s and μ_s be the reference quintic and mass of
[[sec:table-seed-profile]].

(a) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in the points with 0.68 ≤ R ≤ R_u2, where 1.8614098 ≤ R_u2 ≤ 1.8614596;
in particular the seed region 0.70 ≤ R ≤ 1.861 (0.02 ≤ v̂ ≤ 1.181) lies in region III, and f3(Φ(ρ)) > 0 for every
ρ ∈ [2.32, 3.44].

(b) For every v̂ ∈ [0.02, 1.181],

    |ψ_s(v̂) − ψ_III(v̂)| ≤ 3.03 × 10⁻⁵,  |ψ_s′(v̂) − ψ_III′(v̂)| ≤ 2.40 × 10⁻⁴,  |ψ_s″(v̂) − ψ_III″(v̂)| ≤ 8.56 × 10⁻⁴,

and |μ3 − μ_s| ≤ 1.79 × 10⁻⁶. In particular the bounds 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ (k = 0, 1, 2) and 1.4 ×
10⁻⁵ hold at every point of the seed region.

(c) Consequently (ψ_III, ψ_III′, ψ_III″) lies within (10⁻³, 10⁻³, 3 × 10⁻²) of (ψ_s, ψ_s′, ψ_s″) on the seed region and
|μ3 − μ_s| ≤ 10⁻⁴: the background lies in the tube of [[prop:margins-seed]] (b), and Γ > 0 on the seed region.

Proof. (a) On Σ_τ0, R = v̂ + 0.68 ≥ 0.68 since v̂ ≥ 0, and by [[lem:bg-reduction]] (f) a point of Σ_τ0 with R ≤ R_* lies
on a ray ρ ∈ [2.321, R_*] ⊂ [2.32, 3.44]. Let g(ρ) := Φ(ρ) − v̂(ρ) − 0.68 for ρ ∈ [2.32, 3.44]. Its derivative is J(u2,
ρ) − 1/a(ρ) < 1 − 2 < 0 since J ≤ 1 ([[prop:bg-rays]]) and a < 1/2. By [[prop:bg-rays]], g(2.77362) ≥ Φ̃(2.77362) −
v̂(2.77362) − 0.68 − ε₀ ≥ 1.89 × 10⁻⁵ > 0 and g(2.77364) ≤ −1.27 × 10⁻⁵ < 0; so g has one zero ρ_u2 ∈ (2.77362, 2.77364).
A point of Σ_τ0 on the ray ρ has R = v̂(ρ) + 0.68; since R decreases along the ray ([[lem:bg-reduction]] (c)) it lies in
{u ≥ u2} exactly when R ≤ Φ(ρ), that is g(ρ) ≥ 0, that is ρ ≤ ρ_u2. Hence R_u2 = v̂(ρ_u2) + 0.68 ∈ [v̂(2.77362) + 0.68,
v̂(2.77364) + 0.68] ⊂ [1.8614098, 1.8614596]. The seed region has ρ ≤ v̂⁻¹(1.181) < 2.7735 < ρ_u2 (v̂(2.7735) ≥ 1.18111).
And f3(Φ) ≥ 1 − 0.8222/1.4832² > 0 by [[prop:bg-rays]] and [[prop:bg-nprime]].

(b) Since v̂(2.3282) ≤ 0.0199332 < 0.02 and v̂(2.7735) ≥ 1.18111 > 1.181, it suffices to bound, for ρ ∈ [2.3282,
2.7735] and k = 0, 1, 2, the function e_k(ρ) := ψ_s^(k)(v̂(ρ)) − Ψ_k(ρ, Φ, …, μ3). Split

    e_k = ẽ_k + (Ψ_k(ρ, Φ̃, …, μ̃3) − Ψ_k(ρ, Φ, …, μ3)),
    ẽ_k(ρ) := ψ_s^(k)(v̂(ρ)) − Ψ_k(ρ, Φ̃, …, μ̃3).  {#eq:bg-seed-split}

On each interval of [[sec:tab-bg-seed]], consider the box

    ρ in the interval,   Φ^(j) in the enclosure of Φ̃^(j) on it widened by ε_j (j ≤ 3),
    |μ3 − μ̃3| ≤ 4.07 × 10⁻⁷.  {#eq:bg-seed-box}

It contains (Φ, …, μ3) and (Φ̃, …, μ̃3) ([[prop:bg-rays]] at u2, [[prop:bg-nprime]] (ii)), and the partial derivatives
of Ψ_k are bounded there as in [[sec:tab-bg-seed]] ([[lem:bg-tools]] (d)). By the mean value theorem the second term
of [[eq:bg-seed-split]] is at most

    Δ_k := Σ_(j≤3) sup|∂Ψ_k/∂Φ^(j)| ε_j + sup|∂Ψ_k/∂μ3| · 4.07 × 10⁻⁷,  {#eq:bg-seed-delta}

that is Δ_0 = 3.34 × 10⁻⁶, Δ_1 = 5.20 × 10⁻⁶, Δ_2 = 1.50 × 10⁻⁵.

The function ẽ_k is bounded by [[lem:bg-tools]] (c) with N = 5 at the midpoint ρ_m of each interval: |ẽ_k| ≤ Σ_(n≤5)
|c_n| hⁿ + h⁶ sup |c_6(ξ)|, where c_n is the n-th Taylor coefficient of ẽ_k at ρ_m, c_6(ξ) := ẽ_k^(6)(ξ)/6! for ξ in
the interval, and h is the half-width. These coefficients are obtained as follows. The function ẽ_k is built from ρ by
sums, products, quotients, logarithms and 𝒟: Φ̃ = Σ C_j T_j(y) with y = (ρ − 2.88)/0.56 and T_(j+1) = 2yT_j − T_(j−1);
f1 = 1 − 3/(2ρ²), a = f1/2 and f3(Φ̃) = 1 − μ̃3/Φ̃²; Ψ_0 = ln Φ̃′ + ln f1 − ln f3(Φ̃), Ψ_1 = a𝒟Ψ_0 and Ψ_2 = a𝒟Ψ_1
([[eq:bg-psi3]]); v̂ = F(ρ) − F(2.321) with F of [[eq:bg-tangherlini]]; and ψ_s^(k)(v̂), where the k-th derivative
ψ_s^(k) of the quintic is a polynomial. Starting from the Taylor series ρ_0 + t of ρ at a point ρ_0, the rules
[[eq:bg-series]] give the Taylor coefficients at ρ_0 of each of these functions in turn, up to order 9 (Φ̃ is a
polynomial, so its series is exact; Φ̃′ and each 𝒟 lower the order by one), and so those of ẽ_k up to order 6; every
operation on numbers is replaced by [[lem:bg-tools]] (d), with √(3/2) enclosed by it. With ρ_0 = ρ_m this encloses c_0,
…, c_5. With ρ_0 replaced by each of twenty equal parts P of the interval, the same steps enclose, at every ξ ∈ P, the
coefficients at ξ, since each is the same finite combination of ξ; the sixth one encloses c_6(ξ). This gives the column
"Taylor" of [[sec:tab-bg-seed]] and the rest, at most 2 × 10⁻¹⁰ in every row, and the totals Taylor + rest + Δ_k
bound |e_k| on each interval. The largest totals are 3.020 × 10⁻⁵, 2.394 × 10⁻⁴ and 8.558 × 10⁻⁴, all on the first
interval. Finally |μ3 − μ_s| ≤ |μ̃3 − μ_s| + 4.07 × 10⁻⁷ ≤ 1.3809 × 10⁻⁶ + 4.07 × 10⁻⁷.

(c) The bounds of (b) are below (10⁻³, 10⁻³, 3 × 10⁻²) and 10⁻⁴; [[prop:margins-seed]] (b) states Γ > 0 for every
background of the tube. ∎

#### The slice below R_* {#sec:bg-slice}

**Proposition {#prop:bg-slice}** (Hyperbolicity below R_*.) At every point of Σ_τ0 with 0.68 ≤ R ≤ R_*, κ > 0, K^l_l <
0, e^ψ f < 1 and κK^l_l ≤ −6.00 × 10⁻³; in particular κK^l_l ≤ −4.76 × 10⁻³.

Proof. By [[lem:bg-reduction]] (f) the point lies on a ray ρ ∈ [2.321, R_*] with R = v̂(ρ) + 0.68 =: T(ρ). By
[[prop:bg-seed]] (a) it lies in region III if ρ ≤ ρ_u2 ≤ 2.77364, and otherwise in the packet u1 ≤ u ≤ u2.

*Region III.* On each interval of [[sec:tab-bg-slice-iii]], ψ_III and ψ_III′ are enclosed by [[eq:bg-psi3]] with Φ
in Φ̃ ± ε₀, Φ′ in Φ̃′ ± ε₁, Φ″ in Φ̃″ ± ε₂ ([[prop:bg-rays]]), and R by T on the interval. [[lem:bg-slice-forms]] and
[[lem:bg-tools]] (d) give qf < 1, N_κ < 0 and κK^l_l ≤ −0.093 on every row (q = e^(ψ_III) > 0, qf < 2).

*The packet.* For ρ ∈ [ρ_u2, R_*] the slice point is at the unique u_s(ρ) ∈ [u1, u2] with Ψ(u_s, ρ) = T(ρ): the
difference Ψ(u, ρ) − T(ρ) is ≥ 0 at u1 (ρ ≥ T(ρ) for ρ ≤ R_*, by [[lem:bg-rstar]]), ≤ 0 at u2 (g(ρ) ≤ 0), and decreasing
in u (∂_uΨ = G < 0 since f > 0, [[prop:bg-rays]]). It is also decreasing in ρ, since ∂_ρ(Ψ − T) = J − 1/a < 0; hence u_s
is decreasing in ρ, and so is the inverse ρ_s(u). For each row [u_a, u_b] of [[sec:tab-bg-slice-packet]], Ψ̃(u_a, ρ_hi) +
ε₀ < T(ρ_hi) and Ψ̃(u_b, ρ_lo) − ε₀ > T(ρ_lo) (by direct evaluation; at u_a = u1 take ρ_hi ≥ R_* from [[lem:bg-rstar]],
at u_b = u2 take ρ_lo ≤ ρ_u2 from [[prop:bg-seed]] (a)), so the slice points with u_s ∈ [u_a, u_b] have ρ ∈ [ρ_lo, ρ_hi].
On the box [u_a, u_b] × [ρ_lo, ρ_hi]: μ and λ lie between their values at u_a and u_b (monotone, [[prop:bg-nprime]]
(iii)), which are μ̃, λ̃ there up to the errors 4.2 × 10⁻⁷ and 5 × 10⁻⁸ of [[prop:bg-nprime]] (iv); ℬ lies between its
end values, or between the smaller one and 17/10 when 6.45 is inside, by [[lem:bg-tools]] (e); J and K lie in the
Chebyshev enclosures of J̃, K̃ on the box widened by ε₁, ε₂, with J ≤ 1; and R ∈ [T(ρ_lo), T(ρ_hi)]. Then
[[eq:bg-nk-packet]] and [[lem:bg-tools]] (d) give the enclosures of qf and N_κ in the second table: qf < 1 and N_κ < 0 on
every row, and the largest upper bound of κK^l_l is −6.00 × 10⁻³, on the row u ∈ [6.05, 6.1]. ∎

Near R = R_* the packet's slice points approach region I, where q = 1 and N_κ = (μ/R³)(f − 3) exactly, and κK^l_l =
3(3/2)R_*⁻³(f − 3)(1 − f)/(R_*(2 − f)²) = −6.86 × 10⁻³ at R_*, f = 1 − 3/(2R_*²); the first rows' bounds are close to it.

#### The theorem {#sec:bg-theorem}

**Theorem {#thm:bg-margins}** (The background below R_*.) For the background of [[sec:two-dust-background]]:

(a) On 𝒞_in, λ ≥ 0.529 on [u1, u2]; R(u2) ∈ [1.519357, 1.519359]; the mass of region III satisfies μ3 ∈ [0.8220998,
0.8221253] and R(u2)² > μ3.

(b) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in 0.68 ≤ R ≤ R_u2, where 1.861394 ≤ R_u2 ≤ 1.861466, and contains the
seed region. On the seed region, |ψ_s^(k) − ψ_III^(k)| ≤ 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ for k = 0, 1, 2, and |μ3 −
μ_s| ≤ 1.4 × 10⁻⁵; so the background lies in the tube of [[prop:margins-seed]] (b) and Γ > 0 on the seed region.

(c) On Σ_τ0 for 0.68 ≤ R ≤ R_*: κ > 0, K^l_l < 0, e^ψ f < 1 and κK^l_l ≤ −4.76 × 10⁻³.

Proof. (a) is [[prop:bg-nprime]], (b) is [[prop:bg-seed]], (c) is [[prop:bg-slice]]. ∎

**Remark {#rem:bg-grid}** (Numerical observation.) The reference quintic ψ_s of [[sec:table-seed-profile]] is the first
piece of a degree-5 smoothing spline fitted to the values of ψ_III on a second-order finite-difference solution of the
characteristic problem on a double-null grid with 160 steps per unit, and μ_s is that solution's mass in region III.
The same grid solution reproduces the six inputs [[eq:bg-inputs]] at 40 points of the packet on Σ_τ0 to within
2.0 × 10⁻³ (q), 1.1 × 10⁻³ (f), 2.7 × 10⁻³ (ψ_R, of size 0.20), 2.0 × 10⁻³ (ψ_v̂, of size 0.06), 2.8 × 10⁻³ (f_R) and
7.7 × 10⁻⁴ (f_v̂), up to 3 % of the smaller inputs. No proof uses this remark: [[prop:bg-seed]] uses only the printed
coefficients of ψ_s and the number μ_s.

### The margins of the angle-localised families {#sec:margins}

This section proves the inequalities on which [[thm:loc-bent-slice]] and [[cor:loc-charge-seed]] rest, for the
two-dust background of [[sec:two-dust-background]] with the characteristic data of [[sec:bg-data]], at those data's own
parameters. Three results are proved. [[prop:margins-bend]] and [[cor:margins-lens]] describe the bend of the slice Σ′
and the lens between Σ′ and Σ_τ0. [[thm:margins-hyperbolic]] proves that Rácz's split is hyperbolic on Σ′ ∩ {R ≥ R_*}
with an explicit margin, and locates the band of Σ_τ0 where it fails. [[prop:margins-seed]] bounds Γ/E² from below on
the seed region, for a reference profile and for every profile in a tube around it. Each inequality is reduced to a
finite list of rows, printed in [[sec:table-margins]], and each row is checked by a rule stated here.

*The background.* We recall what is used. The metric is g = −2e^(2σ) du dv + R² dΩ₃² on the quotient by the T² action,
the ingoing dust has profile 𝒜(v) := 3.6 b(v; 3, 4.5) on 𝒞_out := {u = 0}, the outgoing dust has profile ℬ(u) := 1.7 b(u;
5.7, 7.2) on 𝒞_in := {v = 0}, e^(2σ) = 1/2 on both cones, and at the corner R = 5, R_u = −0.47, R_v = 1/2, with mass 3/2.
Here b(x; a, c) := β((2x − a − c)/(c − a)) with the bump β of [[sec:table-bump]]. The mass function is μ := R²(1 +
2e^(−2σ) R_u R_v). The time v̂ on 𝒞_out is fixed by v̂ = 0 at the corner and dv̂/dv = −e^(2σ)/R_u on 𝒞_out, and ψ :=
ln(−e^(2σ)/(R_u dv̂/dv)). Then τ := v̂ − R, τ0 := −0.68 and Σ_τ0 := {τ = τ0}. Region I is {u ≤ 5.7}. The proofs use four
identities of the background ([[lem:bg-identities]], [[eq:bg-field]] and the definition of μ):

    (S1)  μ_u = −(2/3) ℬ e^(−2σ) R_v,   μ_v = −(2/3) 𝒜 e^(−2σ) R_u;      (S2)  R_uv = −e^(2σ) μ/R³;
    (S3)  R_vv = −𝒜/(3R²) on 𝒞_out and R_uu = −ℬ/(3R²) on 𝒞_in;                (S4)  ψ_u = ℬ/(3R² R_u),

and R_u < 0 on the domain. We use the time orientation in which u and v increase to the future. Rácz's quantities on a
round slice are κ (the radial extrinsic curvature) and K^l_l (the trace on the spheres), with the sign conventions of
[[lem:racz-split-formulas]]. Hyperbolic means first-order symmetrizable hyperbolic, as in
[[thm:std-racz-hyperbolic]], by which the split is hyperbolic where κK^l_l < 0. It is not hyperbolic where κK^l_l > 0.
To see this, use the notation of [[rem:std-racz-characteristic]]: for a real leaf covector ξ_S = (ξ_K) ≠ 0 put
B(ξ_S) := ξ_K B^(K), k·ξ_S := γ̂^(KL) k_K ξ_L and |ξ_S|² := γ̂^(KL) ξ_K ξ_L > 0, where k is the mixed part of the
extrinsic curvature, and write ξ_n for n̂^i ξ_i. The characteristic polynomial of the split at ξ = (ξ_ρ, ξ_S) is
det(ξ_ρ I + B(ξ_S)), the determinant of its principal symbol, and its essential part, a factor, is the quadratic
[Rac16, (4.22)]

    K^l_l ξ_n² − 2ξ_n (k·ξ_S) + κ|ξ_S|² = 0,   with roots   ξ_n = (k·ξ_S ± √((k·ξ_S)² − κK^l_l|ξ_S|²))/K^l_l.

By [Rac16, (4.23)] a root ξ_n gives the root ξ_ρ = N̂^K ξ_K + N̂ ξ_n of the characteristic polynomial, so −ξ_ρ is an
eigenvalue of B(ξ_S); and since N̂ ≠ 0 (n̂_i = N̂(dρ)_i is a unit covector) and N̂^K ξ_K are real, ξ_ρ is real exactly
when ξ_n is. The leaves are three-dimensional, so we may choose ξ_S with k·ξ_S = 0. Then the discriminant is
−4κK^l_l|ξ_S|² < 0, and the roots ξ_n = ±i|ξ_S|√(κK^l_l)/K^l_l are not real, so B(ξ_S) has an eigenvalue that is not
real. If H were a common symmetrizer, symmetric positive definite with H B^(K) symmetric for every K, then H B(ξ_S) would
be symmetric, so B(ξ_S) would be self-adjoint for the inner product (x, y) ↦ xᵀHy and its eigenvalues would be real. So
the split has no common symmetrizer, and is not hyperbolic, where κK^l_l > 0.

#### Enclosures and quadrature {#sec:margins-tools}

**Lemma {#lem:margins-enclosure}** (Enclosures and quadrature.)

(a) Let e be an expression in real variables x_1, …, x_n built from constants, +, −, ×, ÷, positive integer powers, exp
and √, and let I_1, …, I_n be closed bounded intervals. Evaluate e with each x_i replaced by I_i and each operation by
its form on intervals: [a, b] + [c, d] = [a + c, b + d]; [a, b] − [c, d] = [a − d, b − c]; [a, b]·[c, d] is the interval
between the least and the greatest of ac, ad, bc, bd; [a, b]/[c, d] = [a, b]·[1/d, 1/c] when 0 ∉ [c, d]; a power [a, b]ⁿ
is the range of t ↦ tⁿ on [a, b]; exp and √ act on the endpoints. If every step is defined, the resulting interval
contains e(x) for every x ∈ I_1 × ⋯ × I_n. This remains true when the lower end of any intermediate interval is
decreased and its upper end increased.

(b) If f ∈ C²[a, b], h := b − a and 0 ≤ s ≤ 1, then |f(a + sh) − (1 − s) f(a) − s f(b)| ≤ (h²/8) sup|f″|. In particular
f ≥ min(f(a), f(b)) − (h²/8) sup|f″| and f ≤ max(f(a), f(b)) + (h²/8) sup|f″| on [a, b].

(c) If f ∈ C²[a, b], then |∫_a^b f − (h/2)(f(a) + f(b))| ≤ (h³/12) sup|f″|. If f ∈ C⁴[a, b], then

    |∫_a^b f − (h/2)(f(a) + f(b)) + (h²/12)(f′(b) − f′(a))| ≤ (h⁴/384) ∫_a^b |f⁗|.   {#eq:margins-hermite}

(d) If ω ≥ 0 is continuous, w ∈ C²[a, b], A0 := ∫_a^b ω and A1 := ∫_a^b (x − a) ω, then

    |∫_a^b ω w − w(a) A0 − (w(b) − w(a)) A1/h| ≤ (h²/8) sup|w″| A0.

*Proof.* (a) By induction on e. Each rule returns exactly the set of values of its operation on the product of its
arguments' intervals: a product is bilinear, so its extreme values on a rectangle are at corners; t ↦ 1/t, exp and √ are
monotone on the intervals where they are applied; the power rule is the definition. Enlarging an intermediate interval
keeps the inclusion. (b) Let L be the linear interpolant of f at a and b. For x ∈ (a, b) choose c with F := f − L − c(t
− a)(t − b) vanishing at x; F vanishes at a, x, b, so F″(ξ) = 0 for some ξ, that is f(x) − L(x) = (f″(ξ)/2)(x − a)(x −
b), and (x − a)(b − x) ≤ h²/4. (c) Two integrations by parts give ∫_a^b f − (h/2)(f(a) + f(b)) = −(1/2) ∫_a^b (x − a)(b
− x) f″(x) dx, and ∫_a^b (x − a)(b − x) dx = h³/6. Four integrations by parts give the left side of
[[eq:margins-hermite]] without modulus as (1/24) ∫_a^b (x − a)²(b − x)² f⁗(x) dx, and (x − a)²(b − x)² ≤ h⁴/16. (d) The
function w(a) + (w(b) − w(a))(x − a)/h is the linear interpolant of w; integrate (b) against ω ≥ 0. ∎

#### The bump {#sec:margins-bump}

**Lemma {#lem:margins-bump}** (The bump.) Let z := 1/(1 − y²) for |y| < 1, and

    q3(z) := z³ − 7z² + (21/2) z − 3,     q4(z) := 4z⁵ − 56z⁴ + 232z³ − 348z² + 195z − 30.

(a) On (−1, 1), β′ = −2yz²β, β″ = 2z²(2z² − 6z + 3)β, β‴ = −8yz³ q3(z) β and β⁗ = 4z³ q4(z) β. Every derivative of β
tends to 0 at ±1, so β ∈ C^∞(ℝ). β is even, 0 ≤ β ≤ 1, and β is increasing on [−1, 0].

(b) β″ vanishes on (−1, 1) exactly at ±y_1, y_1 := 3^(−1/4). So β′ is monotone on [−1, −y_1], [−y_1, y_1] and [y_1, 1],
sup|β′| = |β′(y_1)| ≤ 2.17036, and ∫_(−1)^1 |β″| = 4 sup|β′| ≤ 8.6815.

(c) β‴ vanishes on (−1, 1) exactly at 0, ±y_2 and ±y_3, where z(y_2) ∈ (1.594, 1.595) and z(y_3) ∈ (5.031, 5.032), and
β″ is monotone between consecutive points of −1, −y_3, −y_2, 0, y_2, y_3, 1. Further β″(0) = −2, β″(±y_2) ∈ [−4.181,
−4.136] and β″(±y_3) ∈ [21.039, 21.093]; so sup|β″| ≤ 21.093 and ∫_(−1)^1 |β‴| ≤ 97.1.

(d) β⁗ vanishes on (−1, 1) exactly at ±y_4, ±y_5 and ±y_6, where z(y_4) ∈ (1.300, 1.301), z(y_5) ∈ (3.597, 3.598) and
z(y_6) ∈ (8.039, 8.040), and β‴ is monotone between consecutive points of −1, −y_6, −y_5, −y_4, y_4, y_5, y_6, 1. Its
values satisfy β‴(y_4) ∈ [−6.49, −6.24], β‴(y_5) ∈ [216.8, 219.7] and β‴(y_6) ∈ [−507.6, −505.7]; so sup|β‴| ≤ 507.6 and
∫_(−1)^1 |β⁗| ≤ 2936.

*Proof.* (a) Differentiate β = e^(1−z) with z′ = 2yz² and remove even powers of y by y² = 1 − 1/z; for instance β″ =
(4y²z⁴ − 2z² − 8y²z³)β = 2z²(2z² − 6z + 3)β, and the third and fourth derivatives follow in the same way. Each
derivative is a polynomial in y and z times e^(1−z), and z^m e^(1−z) → 0 as z → ∞. Evenness, the bounds and the
monotonicity follow from β = e^(1−z) with z increasing in |y|.

(b) 2z² − 6z + 3 has the roots (3 ± √3)/2, and only (3 + √3)/2 exceeds 1; it gives y² = 1 − 2/(3 + √3) = 3^(−1/2).
There |β′| = 2·3^(−1/4)·((3 + √3)/2)²·e^(−(1+√3)/2) = 2.170357…. On the three pieces β′ runs from 0 to its maximum, from
its maximum to its minimum −sup|β′|, and back to 0; its total variation, which is ∫|β″|, is 4 sup|β′|.

(c) q3(0) = −3, q3(1/2) = 5/8, q3(1.594) = 0.0012406 > 0, q3(1.595) = −0.0029551 < 0, q3(5.031) = −0.0117822 < 0 and
q3(5.032) = 0.0042248 > 0, so the cubic q3 has exactly one root in each of (0, 1/2), (1.594, 1.595) and (5.031, 5.032);
only the last two exceed 1. With y = 0 (the factor y of β‴) these give the zeros. On z ∈ [1.594, 1.595] and z ∈ [5.031,
5.032], [[lem:margins-enclosure]] (a) applied to 2z²(2z² − 6z + 3)e^(1−z) gives the stated intervals. As β″ is even and
monotone on the pieces, its total variation on [−1, 1] is 2(|β″(y_2) − β″(0)| + |β″(y_3) − β″(y_2)| + |β″(y_3)|) ≤
2(2.181 + 25.274 + 21.093) ≤ 97.1.

(d) q4(0) = −30, q4(1/2) = 49/8, q4(1) = −3, q4(1.300) = −0.00588, q4(1.301) = 0.025631, q4(3.597) = 0.052921,
q4(3.598) = −0.327578, q4(8.039) = −5.84132 and q4(8.040) = 0.897867: five sign changes of a quintic, so exactly one
root in each interval and no other. On the three z-intervals [[lem:margins-enclosure]] (a) applied to −8yz³q3(z)e^(1−z),
y = (1 − 1/z)^(1/2), gives the stated values. They alternate in sign, and β‴ is odd with β‴(0) = β‴(±1) = 0, so its
total variation on [0, 1] is |e_4| + (|e_4| + |e_5|) + (|e_5| + |e_6|) + |e_6| with e_i := β‴(y_i), at most 2(6.49 +
219.7 + 507.6) ≤ 1467.6, and on [−1, 1] at most 2936. ∎

**Lemma {#lem:margins-bump-table}** (The bump table.) Let C, D, C̃_j and D̃_j be as in [[sec:table-bump]], δ = 1/20, and
K := ∫_(−1)^1 β.

(a) |C(y_j) − C̃_j| ≤ 5 × 10⁻⁵ and |D(y_j) − D̃_j| ≤ 10⁻⁴ for 0 ≤ j ≤ 40; in particular |K − 1.2069048544| ≤ 5 × 10⁻⁵.

(b) For y_j ≤ y ≤ y_(j+1),

    |C(y) − C̃_j − (y − y_j)(β(y_j) + β(y))/2| ≤ 2.7 × 10⁻⁴,
    |D(y) − D̃_j − (y − y_j) C̃_j − (y − y_j)² β(y_j)/2| ≤ 1.5 × 10⁻⁴,

and for y ≥ 1, C(y) = K and D(y) = yK.

(c) Let φ be the bend of [[prop:margins-bend]] and, for its three lobes X with half-width h_X, centre c_X and weight ε_X
(ε = 1 for the central lobe, −l1 and −l2 for the others), y_X := (R − c_X)/h_X. Then φ′(R) = 0.01 Σ_X ε_X h_X C(y_X) and
φ(R) = 0.01 Σ_X ε_X h_X² D(y_X). Evaluating C and D by (b) gives φ′(R) to within 1.7 × 10⁻⁶ and φ(R) to within 10⁻⁶.

*Proof.* (a) The recursion for C̃ applies [[eq:margins-hermite]] to f = β on each [y_j, y_(j+1)]. Summing, |C(y_j) −
C̃_j| ≤ (δ⁴/384) ∫|β⁗| + 40 × 5 × 10⁻¹¹ ≤ 2936/(384 × 20⁴) + 2 × 10⁻⁹ ≤ 4.8 × 10⁻⁵ by [[lem:margins-bump]] (d), the
second term accounting for the rounding of the printed values. The recursion for D̃ applies [[eq:margins-hermite]] to
f = C, with f′ = β and f⁗ = β‴, but with C̃ in place of C. So |D(y_j) − D̃_j| is at most (δ⁴/384) ∫|β‴| plus δ times the
sum over i < j of the larger error of C̃ at y_i and y_(i+1), that is at most 1.6 × 10⁻⁶ + 40δ × 4.8 × 10⁻⁵ ≤ 10⁻⁴, using
[[lem:margins-bump]] (c).

(b) By [[lem:margins-enclosure]] (c), |∫_(y_j)^y β − (y − y_j)(β(y_j) + β(y))/2| ≤ (δ³/12) × 21.093 ≤ 2.2 × 10⁻⁴; add
(a). Next D(y) = D(y_j) + (y − y_j) C(y_j) + ∫_(y_j)^y (y − s) β(s) ds, and |∫_(y_j)^y (y − s)(β(s) − β(y_j)) ds| ≤
sup|β′| ∫_(y_j)^y (y − s)(s − y_j) ds ≤ 2.1704 δ³/6 ≤ 4.6 × 10⁻⁵; add (a) and δ × 5 × 10⁻⁵. For y ≥ 1, C(y) = K, and
D(y) = yK − ∫ sβ(s) ds = yK because β is even. (c) The formulas follow from φ(R) = ∫_(3.5)^R (R − t) φ″(t) dt and the
substitution t = c_X + h_X s. The error in φ′ is at most 0.01 (h_P + l1 h_L + l2 h_R) × 2.7 × 10⁻⁴ ≤ 1.7 × 10⁻⁶. For φ,
a lobe in progress contributes at most 0.01 h_X² × 1.5 × 10⁻⁴ and a completed lobe, where D = y_X K with |y_X| ≤ 7.2, at
most 0.01 h_X² × 7.2 × 5 × 10⁻⁵; in all at most 0.01 (0.09 × 2.3 × 10⁻⁴ + 0.0487 × 3.6 × 10⁻⁴ + 0.05533 × 1.5 × 10⁻⁴) ≤
10⁻⁶. ∎

#### The bend {#sec:margins-bend}

**Proposition {#prop:margins-bend}** (The bend.) Let l1 := 432/671, l2 := 50/183, and let φ be the function with φ(R) =
0 for R ≤ 3.5 and

    φ″(R) = 0.01 (b(R; 4.1, 4.7) − l1 b(R; 3.5, 4.05) − l2 b(R; 4.85, 5.75)).   {#eq:margins-bend}

(a) The three lobes have half-widths h_L = 11/40, h_P = 3/10, h_R = 9/20 and centres c_L = 151/40, c_P = 22/5, c_R =
53/10. The numbers l1, l2 are the unique ones for which ∫φ″ = ∫ R φ″ dR = 0, namely

    l1 = (h_P/h_L)(c_R − c_P)/(c_R − c_L) = 0.6438152011922503…,
    l2 = (h_P/h_R)(c_P − c_L)/(c_R − c_L) = 0.27322404371584699….

Hence φ = φ′ = 0 outside [3.5, 5.75].

(b) φ ≤ 0. There is x* ∈ (4.415, 4.445) with φ′ < 0 on (3.5, x*) and φ′ > 0 on (x*, 5.75), and

    0.0011590 ≤ max|φ| = −φ(x*) ≤ 0.0011596;

so max|φ| = 0.00116 to three significant figures.

(c) |φ′| ≤ 0.0021370, |φ″| ≤ 0.01, |φ‴| ≤ 0.072346 and |φ⁗| ≤ 2.3437.

*Proof.* (a) Each lobe is a translate and dilate of the even bump β, so ∫ b(R; a, c) dR = hK and ∫ R b(R; a, c) dR =
c′hK for the lobe of half-width h and centre c′. The two conditions read l1 h_L + l2 h_R = h_P and l1 c_L h_L + l2 c_R
h_R = c_P h_P; K cancels. The determinant is h_L h_R (c_R − c_L) ≠ 0, and Cramer's rule gives the formulas: l1 = (12/11)
(9/10)(40/61) = 432/671 and l2 = (2/3)(5/8)(40/61) = 50/183. For R ≥ 5.75, φ′(R) = ∫φ″ = 0 and φ(R) = ∫ (R − t) φ″(t)
dt = R ∫φ″ − ∫ t φ″ = 0.

(b) The lobes have disjoint supports, so φ″ < 0 on (3.5, 4.05) and on (4.85, 5.75), φ″ > 0 on (4.1, 4.7), and φ″ = 0
elsewhere. Hence φ′ falls from 0 to −0.01 l1 h_L K < 0 on [3.5, 4.05], is constant up to 4.1, rises on [4.1, 4.7] to
0.01(h_P − l1 h_L)K = 0.01 h_P (25/61) K > 0, is constant up to 4.85, and falls to φ′(5.75) = 0. So φ′ has a single zero
x* ∈ (4.1, 4.7), φ falls from 0 to φ(x*) and rises back to φ(5.75) = 0, and φ ≤ 0. On [4.1, 4.7] the left lobe is
complete, so

    φ(R) = 0.01 (h_P² D(y_P) − l1 h_L K (R − c_L)),     y_P := (R − c_P)/h_P,

with l1 h_L = 54/305. At R = 4.415, 4.43 and 4.445 (y_P = y_21, y_22, y_23) the table gives, with K̃ := C̃_40 and
rounded to ten decimals,

    0.01 (0.09 D̃_j − (54/305) K̃ (R − c_L)) ≈ −0.0011576361,  −0.0011591651,  −0.0011584676,

and by [[lem:margins-bump-table]] (a) the true values differ from these printed decimals by at most 0.01(0.09 × 10⁻⁴ +
(54/305) × 0.67 × 5 × 10⁻⁵) + 5 × 10⁻¹¹ ≤ 1.5 × 10⁻⁷. So φ(4.43) < min(φ(4.415), φ(4.445)), and as φ is convex on [4.1,
4.7] its minimum point x* lies in (4.415, 4.445). There [[lem:margins-enclosure]] (b), with h = 0.015 and sup|φ″| ≤ 0.01,
so that (h²/8) sup|φ″| ≤ 2.82 × 10⁻⁷, gives φ ≥ −0.0011591651 − 1.5 × 10⁻⁷ − 2.82 × 10⁻⁷ = −0.0011595971 ≥ −0.0011596,
while φ(4.43) ≤ −0.0011591651 + 1.5 × 10⁻⁷ ≤ −0.0011590.

(c) By the description of φ′ in (b), |φ′| ≤ 0.01 (54/305) K ≤ 0.0021370 by [[lem:margins-bump-table]] (a). Since the
lobes are disjoint, |φ^(k)| on the lobe of half-width h and weight c ∈ {1, l1, l2} is at most 0.01 c
sup|β^(k−2)|/h^(k−2); by [[lem:margins-bump]] the largest of these is 0.01 × 2.17036 × (10/3) for k = 3 and 0.01 ×
21.093 × (100/9) for k = 4. ∎

#### Region I and the data on the shell {#sec:margins-region-one}

**Lemma {#lem:margins-region-one}** (Region I.)

(a) On region I the background is ingoing Vaidya in the chart (v̂, R):

    g = −f dv̂² + 2 dv̂ dR + R² dΩ₃²,     f := 1 − μ(v̂)/R²,   {#eq:margins-vaidya}

where μ(v̂) is the mass at the point of 𝒞_out with time v̂. The function μ is nondecreasing; μ = 3/2 for v ≤ 3, μ is
constant for v ≥ 4.5, and μ ≤ 3.6059 everywhere.

(b) Let F(r) := 2r + √(3/2) ln((r − √(3/2))/(r + √(3/2))) and τ_ray(R) := F(R) − F(2.321) − R. Where v̂ ≤ v̂(v = 3) the
null ray u = 5.7 is {τ = τ_ray(R)}. Since τ_ray(3.43718) = −0.68000009 and τ_ray(3.43719) = −0.67998718, it crosses Σ_τ0
at a single radius R_* ∈ (3.43718, 3.43719), with v̂ = τ0 + R_* < 2.7572 < v̂(v = 3) = 3.14533. This R_* is the radius
of [[lem:bg-rstar]], which encloses it in [3.43718006, 3.43718007].

(c) Every point with R ≥ R_* and τ ≤ τ0 lies in region I. In particular Σ_τ0 ∩ {R ≥ R_*}, Σ′ ∩ {R ≥ R_*} and every point
with R ≥ R_* between Σ′ and Σ_τ0 do.

*Proof.* (a) In region I, ℬ = 0, so μ_u = 0 by (S1) and ψ_u = 0 by (S4). Thus μ is constant along ingoing rays, equal to
its value on 𝒞_out, and ψ = 0, its value on 𝒞_out. With dv̂ = −(e^(2σ)/R_u) dv (which is ψ = 0) and du = (dR − R_v
dv)/R_u, the quotient metric is −2e^(2σ) du dv = 2 dv̂ dR + 2e^(−2σ) R_u R_v dv̂², and 2e^(−2σ) R_u R_v = μ/R² − 1 by the
definition of μ. On 𝒞_out, μ_v = −(2/3)𝒜 e^(−2σ) R_u ≥ 0 with 𝒜 = 0 outside (3, 4.5); the bound μ ≤ 3.6059 is
[[lem:margins-shell-data]] (c) at v = 4.5.

(b) For v̂ ≤ v̂(v = 3), μ = 3/2. The ray u = 5.7 starts on 𝒞_in, where v̂ = 0 and, by (S3) with ℬ = 0 for u ≤ 5.7, R = 5
− 0.47 u, so R = 2.321. Outgoing null rays of [[eq:margins-vaidya]] satisfy dv̂/dR = 2/f, and F′(r) = 2r²/(r² − 3/2) is
2/f for μ = 3/2; so v̂ = F(R) − F(2.321) on the ray. The values of τ_ray are direct evaluations, and τ_ray is increasing
by (c) below. Finally v̂(v = 3) is v̂_0 of [[sec:table-shell]].

(c) Along an outgoing null ray of [[eq:margins-vaidya]], dτ/dR = 2/f − 1 > 0 where 0 < f < 2. On the ray u = 5.7 at R ≥
R_*, f ≥ 1 − 3.6059/R_*² > 0 since R_*² > 11.81. So the ray's τ, as a function of R, is increasing on [R_*, ∞) and at
least τ0 there; equivalently its time v̂_ray(R) satisfies v̂_ray(R) ≥ τ0 + R. Let p have R_p ≥ R_* and τ_p ≤ τ0. Then
v̂_ray(R_p) ≥ τ0 + R_p ≥ v̂_p, so the ingoing ray v̂ = v̂_p meets u = 5.7 at a radius R_1 ≤ R_p. Along an ingoing ray u
decreases as R increases (R_u < 0), so u(p) ≤ 5.7. Points of Σ′ have τ = τ0 + φ(R) ≤ τ0 by [[prop:margins-bend]] (b),
and points between the two slices have τ0 + φ(R) ≤ τ ≤ τ0. ∎

**Corollary {#cor:margins-lens}** (The lens.) Let Σ′ := {v̂ − R − φ(R) = τ0}. Then Σ′ = Σ_τ0 outside R ∈ [3.5, 5.75],
and Σ′ lies to the past of Σ_τ0 where they differ, at τ-distance at most max|φ| ≤ 0.0011596. Let γ be a causal curve
joining a point p of Σ′ with R_p ≥ R_* to a point q of Σ_τ0. Then γ lies in region I. If γ is not constant, it runs to
the future from p to q, every point of γ other than q has R ∈ (3.5, 5.75), and the angular displacement of γ on the
unit sphere S³ is at most 3.25 × 10⁻⁴. The slice Σ_τ0 is acausal; so a causal curve joining a point p of Σ′ with
R_p < R_*, which lies on Σ_τ0, to a point q of Σ_τ0 is constant, and R_q = R_p < R_*. Hence carrying a domain of
influence from one slice to the other widens its angular support by at most 3.3 × 10⁻⁴ rad.

*Proof.* On Σ′, τ = τ0 + φ(R). By [[prop:margins-bend]], φ = 0 outside [3.5, 5.75], and φ < 0 on (3.5, 5.75), since φ
strictly decreases from φ(3.5) = 0 on [3.5, x*] and strictly increases to φ(5.75) = 0 on [x*, 5.75]. This gives the
first two statements.

*Time functions in region I.* With τ = v̂ − R, [[eq:margins-vaidya]] reads g = −f dτ² + 2(1 − f) dτ dR + (2 − f) dR² +
R² dΩ₃², whose inverse on the (τ, R) plane has g^(ττ) = −(2 − f), g^(τR) = 1 − f and g^(RR) = f. So g⁻¹(dτ, dτ) = −(2 −
f) < 0, since f < 1. Where φ′ ≠ 0, R ∈ (3.5, 5.75) and 0 < f < 1 (μ ≤ 3.6059 < 3.5²), so with |φ′| ≤ 0.0022,
g⁻¹(d(τ − φ), d(τ − φ)) = −(2 − f) − 2(1 − f)φ′ + fφ′² ≤ −1 + 2 × 0.0022 + 0.0022² < 0; where φ′ = 0 it is −(2 − f).
So dτ and d(τ − φ) are timelike on region I. The vector −∂_R of the chart (v̂, R) is null and future directed: it is
tangent to an ingoing ray, along which u increases as R decreases, because R_u < 0. On it dτ and d(τ − φ) take the
values 1 and 1 + φ′, both positive. A timelike covector does not vanish on a nonzero causal vector, so it has one sign
on the future causal vectors; hence τ and τ − φ(R) increase strictly along every future causal curve in region I that
is not constant.

*Where γ lies.* Along a future causal curve u and v do not decrease, and v̂ is an increasing function of v (dv̂/dv =
−e^(2σ)/R_u > 0); so v̂ does not decrease. Let γ join p ∈ Σ′, R_p ≥ R_*, to q ∈ Σ_τ0. The point p lies in region I by
[[lem:margins-region-one]] (c), which settles a constant γ; suppose γ is not constant. If γ runs to the future from q to
p, then u ≤ u(p) ≤ 5.7 along γ, so γ lies in region I; there τ increases strictly from τ(q) = τ0 to τ(p) = τ0 +
φ(R_p) ≤ τ0, which is impossible. So γ runs to the future from p to q. Then τ0 + R_q = v̂(q) ≥ v̂(p) = τ0 + R_p +
φ(R_p). If R_p ≥ 3.5, this gives R_q ≥ 3.5 − 0.0011596 > R_*; if R_* ≤ R_p < 3.5, then φ(R_p) = 0 and R_q ≥ R_p ≥ R_*.
In either case q lies in region I by [[lem:margins-region-one]] (c), so u(q) ≤ 5.7, and u ≤ u(q) along γ: γ lies in
region I. There τ − φ(R) increases strictly from τ0 at p, and τ increases strictly to τ0 at q. So at every point of γ
other than q, φ(R) ≤ τ − τ0 < 0, which forces R ∈ (3.5, 5.75).

*The angular displacement.* A causal vector (τ̇, Ṙ, Ω̇) satisfies

    R²|Ω̇|² ≤ f τ̇² − 2(1 − f) τ̇ Ṙ − (2 − f) Ṙ² ≤ τ̇²/(2 − f),

the right-hand bound being the maximum over Ṙ. At the points of γ other than q, μ ≥ 3/2 and 3.5 < R < 5.75, so 2 − f
= 1 + μ/R² ≥ 1 + 1.5/5.75² ≥ 1.045368 and √(2 − f) ≥ 1.02243. Hence |Ω̇| ≤ τ̇/(3.5 × 1.02243) ≤ τ̇/3.5785, and the
angular displacement is at most (τ0 − τ(p))/3.5785 = −φ(R_p)/3.5785 ≤ 0.0011596/3.5785 ≤ 3.25 × 10⁻⁴.

*Σ_τ0 is acausal.* In the chart [[eq:bg-chart]], g = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃², so the induced metric of
Σ_τ0 = {v̂ = τ0 + R} is e^ψ(2 − e^ψ f) dR² + R² dΩ₃²; on the domain v̂ ≥ 0, so R ≥ 0.68 on Σ_τ0. Here e^ψ f < 1 at
every point of Σ_τ0: for R ≥ R_* the point lies in region I by [[lem:margins-region-one]] (c), where ψ = 0 and f = 1 −
μ/R² < 1; for 0.68 ≤ R ≤ R_*, e^ψ f < 1 by [[prop:bg-slice]]. Parametrise
the quotient curve of Σ_τ0 by R. Along it v̂ = τ0 + R increases, so v increases strictly, and −2e^(2σ)(du/dR)(dv/dR)
= e^ψ(2 − e^ψ f) > 0, so u decreases strictly. Let a future causal curve run from p1 ∈ Σ_τ0 to p2 ∈ Σ_τ0. Then
v(p2) ≥ v(p1) and u(p2) ≥ u(p1), which give R(p2) ≥ R(p1) and R(p2) ≤ R(p1); so u and v take the same values at both
ends, and as they do not decrease along the curve they are constant on it. Its tangent then has u̇ = v̇ = 0 and
R²|Ω̇|² ≤ 2e^(2σ) u̇ v̇ = 0, so the curve is constant. Finally, a point p of Σ′ with R_p < R_* has φ(R_p) = 0 and lies
on Σ_τ0, so a causal curve joining it to a point q of Σ_τ0 is constant, and R_q = R_p < R_*. ∎

**Lemma {#lem:margins-shell-data}** (The data on the shell.) On 𝒞_out put P := R_v, write ′ for d/dv, and let f_N := 1 −
μ/R², w := f_N/(3P) and g := 2P/f_N along 𝒞_out. For 3 ≤ v ≤ 4.5,

    R′ = P,    P′ = −𝒜/(3R²),    μ′ = 𝒜 w,    v̂′ = g,   {#eq:margins-ode}

with R = 13/2, P = 1/2, μ = 3/2 and v̂ = v̂_0 at v = 3 (v̂_0 as in [[sec:table-shell]]). Moreover

    w′ = 2μ/(3R³),    g′ = −4μP²/(f_N² R³),    dμ/dv̂ = (3/2) 𝒜 w².   {#eq:margins-rates}

(a) For 3 ≤ v ≤ 4.5: 0.47428 ≤ P ≤ 1/2, 13/2 ≤ R ≤ 29/4, 3/2 ≤ μ ≤ 3.79034, 0.91028 ≤ f_N ≤ 0.97147 and 0.60685 ≤ w ≤
0.70282.

(b) Let h := 1/80, v_k := 3 + kh, 𝒜_k := 𝒜(v_k), 𝒜′_k := 𝒜′(v_k), and

    Ã0_k := (h/2)(𝒜_k + 𝒜_(k+1)) − (h²/12)(𝒜′_(k+1) − 𝒜′_k),
    Ã1_k := (h²/2) 𝒜_(k+1) − (h²/12)(𝒜_(k+1) − 𝒜_k + h 𝒜′_(k+1)).

The rows (R_k, P_k, μ_k, v̂_k) of [[sec:table-shell]] satisfy

    R_(k+1) = R_k + (h/2)(P_k + P_(k+1)),
    P_(k+1) = P_k − (1/3)(Ã0_k/R_k² + (1/R_(k+1)² − 1/R_k²) Ã1_k/h),
    μ_(k+1) = μ_k + w_k Ã0_k + (w_(k+1) − w_k) Ã1_k/h,   {#eq:margins-scheme}
    v̂_(k+1) = v̂_k + (h/2)(g_k + g_(k+1)),

with w_k, g_k evaluated on row k, up to residuals r_k of modulus at most 10⁻⁸ in each line, whose sums over k = 0, …,
119 are at most 5 × 10⁻⁷ in each line.

(c) For every k, |R(v_k) − R_k| ≤ 4 × 10⁻⁶, |P(v_k) − P_k| ≤ 6 × 10⁻⁷, |μ(v_k) − μ_k| ≤ 10⁻⁵ and |v̂(v_k) − v̂_k| ≤ 4 ×
10⁻⁶.

*Proof.* Put Q := R_u on 𝒞_out, where e^(2σ) = 1/2. Then (S3) gives P′ = −𝒜/(3R²); the definition of μ gives μ = R²(1 +
4QP), so Q = −f_N/(4P); (S1) gives μ′ = −(4/3)𝒜Q = 𝒜w; and dv̂/dv = −e^(2σ)/R_u = −1/(2Q) = g. Before the shell 𝒜 = 0,
so R = 5 + v/2, P = 1/2 and μ = 3/2, and v̂(3) = ∫_5^(13/2) 2/f_N dR = F(13/2) − F(5) = v̂_0. Next, f_N′ = −𝒜w/R² +
2μP/R³ gives w′ = (f_N′ P − f_N P′)/(3P²) = −𝒜w/(3PR²) + 2μ/(3R³) + f_N 𝒜/(9P²R²), and the first and last terms cancel
because f_N/(3P) = w. Likewise g′ = 2P′/f_N − 2P f_N′/f_N² = −2𝒜/(3R² f_N) + 2P𝒜w/(R² f_N²) − 4μP²/(R³ f_N²), and
2Pw/f_N² = 2/(3f_N) cancels the first term. Finally dμ/dv̂ = μ′/g = 𝒜w f_N/(2P) = (3/2)𝒜w².

(a) P′ ≤ 0, so P ≤ 1/2, and while P > 0, R ≥ 13/2. Then P ≥ 1/2 − (1/3) ∫𝒜/R² ≥ 1/2 − 2.7K/126.75 ≥ 0.47428, because
∫𝒜 = 3.6 × 0.75 K and K ≤ 1.2069549 by [[lem:margins-bump-table]] (a). So R ≤ 13/2 + (3/2)(1/2) = 29/4. While f_N > 0,
μ′ ≥ 0 and w ≤ 1/(3 × 0.47428) ≤ 0.70282, so μ ≤ 3/2 + 0.70282 × 3.25878 ≤ 3.79034 and f_N ≥ 1 − 3.79034/42.25 ≥
0.91028 > 0; this closes the argument. The remaining bounds follow from f_N ≤ 1 − 1.5/R² ≤ 1 − 1.5/(29/4)².

(b) is a row-by-row check of [[sec:table-shell]], with 𝒜_k and 𝒜′_k from [[lem:margins-bump]] (a).

(c) For the true solution, let A0_k := ∫ 𝒜 and A1_k := ∫ (v − v_k) 𝒜 over [v_k, v_(k+1)]. By [[lem:margins-enclosure]]
(c) and (d), the true values satisfy the four lines of [[eq:margins-scheme]] with A0_k, A1_k in place of Ã0_k, Ã1_k, up
to errors τ^R_k, τ^P_k, τ^μ_k, τ^v_k with

    |τ^R_k| ≤ (h³/12) sup|P″|,   |τ^P_k| ≤ (h²/24) sup|(R⁻²)″| A0_k,
    |τ^μ_k| ≤ (h²/8) sup|w″| A0_k,   |τ^v_k| ≤ (h³/12) sup|g″|.

On the box (a), P″ = −𝒜′/(3R²) + 2𝒜P/(3R³) gives |P″| ≤ 10.4178/126.75 + 3.6/823.875 ≤ 0.0866 (sup|𝒜′| = 4.8 sup|β′| ≤
10.4178); (R⁻²)″ = 6P²/R⁴ + 2𝒜/(3R⁵) ≤ 0.00105; w″ = 2𝒜w/(3R³) − 2μP/R⁴ gives |w″| ≤ 0.00827; and differentiating g′
with [[eq:margins-ode]] gives |g″| ≤ 4(0.6326 + 0.1077 + 0.1535 + 0.2187)/(0.9102² × 274.625) ≤ 0.0196, the four terms
bounding μ′P², 2μP|P′|, 2μP²|f_N′|/f_N and 3μP³/R. By [[eq:margins-hermite]] applied to 𝒜 and to (v − v_k)𝒜, |A0_k −
Ã0_k| ≤ (h⁴/384) ∫|𝒜⁗| and |A1_k − Ã1_k| ≤ (h⁴/384)(4 ∫|𝒜‴| + h ∫|𝒜⁗|), integrals over the cell; summed over k, with
∫|𝒜⁗| = 3.6 (4/3)³ ∫|β⁗| ≤ 25054 and ∫|𝒜‴| = 3.6 (4/3)² ∫|β‴| ≤ 622, these are at most 1.6 × 10⁻⁶ and 1.8 × 10⁻⁷. Let
e^X_k be the true value minus the row value, for X = R, P, μ, v̂, so e_0 = 0. On the box (a), which contains the rows,
the Lipschitz bounds are |Δ(R⁻²)| ≤ 0.0072827|ΔR|, |Δw| ≤ 0.016635|Δμ| + 0.019401|ΔR| + 1.43959|ΔP| and |Δg| ≤
2.19713|ΔP| + 0.028565|Δμ| + 0.033314|ΔR|; also R⁻² ≤ 1/42.25, |(R⁻²)′| ≤ 0.0036414 and |w′| ≤ 0.00921. Subtracting the
row relations from the true ones,

    |e^R_(k+1)| ≤ |e^R_k| + (h/2)(|e^P_k| + |e^P_(k+1)|) + |τ^R_k| + |r^R_k|,
    |e^P_(k+1)| ≤ |e^P_k| + 0.0024276 ((|Ã0_k| + |Ã1_k|/h)|e^R_k| + (|Ã1_k|/h)|e^R_(k+1)|) + m^P_k + |τ^P_k| + |r^P_k|,
    |e^μ_(k+1)| ≤ |e^μ_k| + (|Ã0_k| + |Ã1_k|/h)|Δw_k| + (|Ã1_k|/h)|Δw_(k+1)| + m^μ_k + |τ^μ_k| + |r^μ_k|,
    |e^v_(k+1)| ≤ |e^v_k| + (h/2)(|Δg_k| + |Δg_(k+1)|) + |τ^v_k| + |r^v_k|,

where m^P_k := (1/3)(|A0_k − Ã0_k|/42.25 + 0.0036414 |A1_k − Ã1_k|) and m^μ_k := 0.70282 |A0_k − Ã0_k| + 0.00921 |A1_k −
Ã1_k|. Let E^X be the largest |e^X_k|. Summing from 0 and using Σ_k (|Ã0_k| + 2|Ã1_k|/h) ≤ 6.52 (from the table) and Σ_k
h = 3/2, the sources are S^R ≤ 1.70 × 10⁻⁶ + 5 × 10⁻⁷, S^P ≤ 3.6 × 10⁻⁸ + 5 × 10⁻⁷, S^μ ≤ 1.66 × 10⁻⁶ + 5 × 10⁻⁷ and
S^v ≤ 3.9 × 10⁻⁷ + 5 × 10⁻⁷, and

    E^R ≤ S^R + 1.5 E^P,   E^P ≤ S^P + 0.015828 E^R,   E^μ ≤ S^μ + 6.52 (0.016635 E^μ + 0.019401 E^R + 1.43959 E^P),
    E^v ≤ S^v + 1.5 (2.19713 E^P + 0.028565 E^μ + 0.033314 E^R).

The first two give E^P ≤ (S^P + 0.015828 S^R)/(1 − 0.023742) ≤ 5.9 × 10⁻⁷ and E^R ≤ 3.1 × 10⁻⁶; then E^μ ≤ (S^μ +
6.52(0.019401 E^R + 1.43959 E^P))/(1 − 0.108461) ≤ 9.1 × 10⁻⁶ and E^v ≤ 3.4 × 10⁻⁶. ∎

#### Rácz's quantities in region I {#sec:margins-racz}

**Lemma {#lem:margins-racz}** (Round slices of region I.) In the chart [[eq:margins-vaidya]], let v̂ = V(R) be a round
slice with V′ > 0 and fV′ < 2, write μ̇ := dμ/dv̂, and put

    Ξ := V″ + (μ/R³) V′²(3 − fV′) − μ̇ V′³/(2R²).   {#eq:margins-xi}

Then κ′ = Ξ/(V′(2 − fV′))^(3/2) and K′^l_l = 3(fV′ − 1)/(R (V′(2 − fV′))^(1/2)), so

    κ′ K′^l_l = −c Ξ,     c := 3(1 − fV′)/(R V′² (2 − fV′)²).

On Σ_τ0 (V′ = 1, V″ = 0) this is κ = −N_κ/(2 − f)^(3/2) and K^l_l = 3(f − 1)/(R(2 − f)^(1/2)), with

    N_κ := (μ/R³)(f − 3) + μ̇/(2R²) = −2μ/R³ − μ²/R⁵ + μ̇/(2R²).

*Proof.* With T := V′∂_v̂ + ∂_R tangent to the slice, g(T, T) = V′(2 − fV′) > 0 and the normal covector dv̂ − V′dR has
g⁻¹-norm −V′(2 − fV′); let n be the unit normal with n_♭ = −(dv̂ − V′dR)/(V′(2 − fV′))^(1/2). The Christoffel symbols of
the (v̂, R) part are Γ_(v̂,v̂v̂) = −f_v̂/2, Γ_(v̂,v̂R) = −f_R/2, Γ_(R,v̂v̂) = f_R/2 and zero otherwise (first index
lowered), with f_v̂ = −μ̇/R² and f_R = 2μ/R³. With n^v̂ = V′/(V′(2 − fV′))^(1/2) and n^R = (fV′ − 1)/(V′(2 −
fV′))^(1/2), κ′ := −g(∇_T T, n)/g(T, T) has numerator V″ + f_v̂ V′³/2 + f_R V′² − (fV′ − 1) f_R V′²/2 = Ξ, divided by
(V′(2 − fV′))^(1/2) g(T, T). The trace on the spheres is K′^l_l = 3n^R/R. At V′ = 1, V″ = 0 these are the formulas of
[[lem:racz-split-formulas]] with ψ = 0, which fixes the signs. ∎

On Σ′ the slice is V(R) = τ0 + R + φ(R), so V′ = 1 + φ′ ∈ [0.99786, 1.00149] and V″ = φ″ by [[prop:margins-bend]], and Ξ
= φ″ + (μ/R³)V′²(3 − fV′) − μ̇V′³/(2R²). On Σ′ ∩ {R ≥ R_*}, which lies in region I by [[lem:margins-region-one]] (c), μ
≥ 3/2, so f ≤ 1 − 3/(2R²); with V′ ≤ 1.00149, and V′ = 1 for R ≥ 5.75, this gives fV′ < 1 on Σ′ ∩ {R ≥ R_*}, so K′^l_l <
0 there, and κ′ > 0 exactly where Ξ > 0.

#### Hyperbolicity on R ≥ R_* {#sec:margins-hyperbolic}

For 3 ≤ v ≤ 4.5, the ingoing ray v meets Σ_τ0 at R0(v) := v̂(v) − τ0 and Σ′ at the radius R′(v) with R′ + φ(R′) = R0(v);
both are increasing in v. Write N_κ(v) and Ξ(v) for N_κ and Ξ at these points, with μ = μ(v) and μ̇ = (3/2)𝒜 w² by
[[eq:margins-rates]].

**Lemma {#lem:margins-curvature}** (Second derivatives along the slices.) On a cell [v_k, v_(k+1)] let S_i be the
supremum of |𝒜^(i)| (i = 0, 1, 2) and Φ4 the supremum of |φ⁗| over [R′(v_k), R′(v_(k+1))]. Then on the cell

    (a)  |d²N_κ/dv²| ≤ M := 0.024 S_2 + 0.059 S_1 + 0.072 S_0 + 0.0013 S_0² + 0.17,
    (b)  |d²Ξ/dv²| ≤ M′ := 1.21 Φ4 + 0.024 S_2 + 0.061 S_1 + 0.075 S_0 + 0.0013 S_0² + 0.23.

*Proof.* By [[lem:margins-shell-data]] (c) and the monotonicity of R, P and μ in v, along 𝒞_out the true values satisfy
0.4769 ≤ P ≤ 1/2, 13/2 ≤ R ≤ 7.2325 and 3/2 ≤ μ ≤ 3.6059; hence 0.91465 ≤ f_N ≤ 0.97133, 0.60976 ≤ w ≤ 0.67892, μ/R³ ≤
0.013131 and 0 ≤ μ̇ ≤ (3/2)(0.67892)² S_0 ≤ 0.6914 S_0 ≤ 2.49. By [[eq:margins-ode]] and [[eq:margins-rates]],

    μ′ = 𝒜w,   μ″ = 𝒜′w + 2𝒜μ/(3R³),   μ̇′ = (3/2)𝒜′w² + 2𝒜wμ/R³,
    μ̇″ = (3/2)𝒜″w² + 4𝒜′wμ/R³ + (4/3)𝒜μ²/R⁶ + 2𝒜²w²/R³ − 6𝒜wμP/R⁴,

with R the radius on 𝒞_out, so |μ′| ≤ 0.67892 S_0, |μ″| ≤ 0.67892 S_1 + 0.008754 S_0, |μ̇′| ≤ 0.6914 S_1 + 0.01783 S_0
and |μ̇″| ≤ 0.6914 S_2 + 0.03566 S_1 + 0.004345 S_0 + 0.003357 S_0². Also R0′ = g ≤ 1.09332 and |R0″| = |g′| ≤
0.015696.

(a) N_κ = H(μ, μ̇, R0) with H := −2μR⁻³ − μ²R⁻⁵ + (1/2)μ̇R⁻², linear in μ̇. For R ≥ 3.825, μ ≤ 3.6059 and μ̇ ≤ 2.49,
the partial derivatives obey |H_μ| ≤ 0.044547, H_μ̇ ≤ 0.034175, |H_R| ≤ 0.12184 + 0.01787μ̇, |H_μμ| ≤
0.0024428, |H_μR| ≤ 0.039545, |H_μ̇R| ≤ 0.01787 and |H_RR| ≤ 0.13827 + 0.014016μ̇, each a sum of the moduli of its terms
at R = 3.825 and the largest μ. The chain rule,

    N_κ″ = H_μ μ″ + H_μ̇ μ̇″ + H_R R0″ + H_μμ μ′² + 2H_μR μ′ R0′ + 2H_μ̇R μ̇′ R0′ + H_RR R0′²,

and the bounds above give |N_κ″| ≤ 0.02363 S_2 + 0.05848 S_1 + 0.07172 S_0 + 0.00125 S_0² + 0.1672 ≤ M.

(b) Ξ = φ″(R′) + Y(μ, μ̇, R′, V) with Y := μR⁻³V²(3 − V) + μ²R⁻⁵V³ − (1/2)μ̇R⁻²V³ and V := 1 + φ′(R′). Differentiating
R′ + φ(R′) = R0 gives R′_v = g/V, R′_vv = g′/V − g²φ″/V³, V_v = φ″R′_v and V_vv = φ‴R′_v² + φ″R′_vv, so with
[[prop:margins-bend]] (c), by which V ≥ 0.99786, R′_v ≤ 1.09332/0.99786 ≤ 1.09567, R′_v² ≤ (1.09332/0.99786)² ≤
1.20049, |R′_vv| ≤ 0.027761, |V_v| ≤ 0.010957 and |V_vv| ≤ 0.08713; and (φ″(R′))_vv = φ⁗R′_v² + φ‴R′_vv. For 3.825 ≤
R ≤ 5.373, μ ≤ 3.6059, μ̇ ≤ 2.49 and V ∈ [0.99786, 1.00149],

    |Y_μ| ≤ 0.044666,  Y_μ̇ ≤ 0.034328,  |Y_R| ≤ 0.12216 + 0.01795μ̇,  |Y_V| ≤ 0.24109 + 0.10284μ̇,  |Y_μμ| ≤ 0.0024537,
    |Y_μR| ≤ 0.039659,  |Y_μV| ≤ 0.080112,  |Y_μ̇R| ≤ 0.01795,  |Y_μ̇V| ≤ 0.10284,  |Y_RR| ≤ 0.13865 + 0.014078μ̇,
    |Y_RV| ≤ 0.21408 + 0.053768μ̇,  |Y_VV| ≤ 0.096254 + 0.20536μ̇,

each again a sum of the moduli of its terms (using V²(3 − V) ≤ 2.00447, V³ ≤ 1.00448 and 3V(2 − V) ≤ 3). The chain rule
for Y in the four variables (Y is linear in μ̇) and the bounds above give |Ξ_vv| ≤ 1.2005 Φ4 + 0.02374 S_2 + 0.06031
S_1 + 0.08062 S_0 + 0.00125 S_0² + 0.19801, and 0.08062 S_0 + 0.19801 ≤ 0.075 S_0 + 0.23 because S_0 ≤ 3.6. ∎

**Theorem {#thm:margins-hyperbolic}** (Hyperbolicity margins on R ≥ R_*.) Let R_* ∈ (3.43718, 3.43719) be as in
[[lem:margins-region-one]] (b). For the background:

(a) on Σ′, κ′ > 0, K′^l_l < 0 and κ′K′^l_l ≤ −2.96 × 10⁻⁴ for R_* ≤ R ≤ 5.75, and κ′K′^l_l < 0 for R ≥ 5.75;

(b) on Σ_τ0, N_κ < 0 for R ∈ [R_*, 4.2882] ∪ [4.5310, ∞), and N_κ > 0 for R ∈ [4.2955, 4.5258].

So Rácz's split is hyperbolic on all of Σ′ ∩ {R ≥ R_*}; on Σ_τ0 ∩ {R ≥ R_*} it is hyperbolic outside [4.2882, 4.5310]
and is not hyperbolic on [4.2955, 4.5258], and each of the two remaining intervals, of widths 0.0073 and 0.0052,
contains a point where N_κ = 0.

*Proof.* By [[lem:margins-region-one]] every point concerned lies in region I, so [[lem:margins-racz]] applies, with μ
and μ̇ those of 𝒞_out at the point's time v̂.

*Σ′ before the shell.* The points of Σ′ with R ≤ R′(3) have v̂ ≤ v̂(3), so μ = 3/2 and μ̇ = 0. Here R′(3) ≈ R′_0 =
3.8254920; by the next paragraph |R′(3) − R′_0| ≤ 5.3 × 10⁻⁶, so R′(3) < 3.82550. On [R_*, 3.5], φ = 0 and Ξ = (1.5/R³)(2
+ 1.5/R²) ≥ 0.074254, while c ≥ 3(1.5/3.5²)/(3.5 (1 + 1.5/R_*²)²) ≥ 0.082639, so κ′K′^l_l ≤ −6.1 × 10⁻³. On [3.5,
3.82550], φ″ ≥ −0.01 l1 ≥ −0.0064382, V′ ∈ [0.99786, 1] (φ′ ≤ 0 there) and f ∈ [0.877551, 0.897504], so Ξ ≥ −0.0064382 +
0.026793 × 0.995724 × 2.102496 ≥ 0.049653 and c ≥ 0.307488/(3.8255 × 1.124327²) ≥ 0.063585, so κ′K′^l_l ≤ −3.1 × 10⁻³.

*Σ′ over the shell.* For v ∈ [3, 4.5] use [[sec:table-sigma-bent]]. The map R ↦ R + φ(R) has derivative 1 + φ′ ≥
0.9978; it sends R′(v_k) to v̂(v_k) + 0.68, which is within 4 × 10⁻⁶ of v̂_k + 0.68 by [[lem:margins-shell-data]] (c),
and it sends R′_k to within 2 × 10⁻⁷ of v̂_k + 0.68 (the residual 10⁻⁷ of the table and the roundings of R0_k and φ_k).
So |R′(v_k) − R′_k| ≤ (4 × 10⁻⁶ + 2 × 10⁻⁷)/0.9978 ≤ 5.3 × 10⁻⁶. The true value Ξ(v_k) then differs from Ξ_k by at most

    0.0447 × 10⁻⁵ + 0.0344 × 8.4 × 10⁻⁶ + 0.24 × 5.3 × 10⁻⁶ + 0.50 × 0.01 × 5.3 × 10⁻⁶ + 5 × 10⁻⁸ ≤ 5 × 10⁻⁶.

The terms come from μ (|Δμ| ≤ 10⁻⁵), from μ̇ (|Δμ̇| ≤ 3𝒜w|Δw| ≤ 7.34 (0.016635 × 10⁻⁵ + 0.019401 × 4 × 10⁻⁶ + 1.43959
× 6 × 10⁻⁷) ≤ 8.4 × 10⁻⁶, by [[lem:margins-shell-data]] (c)), from the radius R′, from V′ = 1 + φ′(R′) (|φ″| ≤ 0.01
times the change of radius) and from the rounding of Ξ_k. The coefficients bound the partial derivatives of Ξ by the
bounds of the proof of [[lem:margins-curvature]]: |Y_μ| ≤ 0.0447, Y_μ̇ ≤ 0.0344, |Y_R| + |φ‴| ≤ 0.12216 + 0.01795 ×
2.49 + 0.072346 ≤ 0.24 and |Y_V| ≤ 0.24109 + 0.10284 × 2.49 ≤ 0.50. By [[lem:margins-enclosure]] (b) and
[[lem:margins-curvature]] (b), on the cell [v_k, v_(k+1)], Ξ ≥ L_k := min(Ξ_k, Ξ_(k+1)) − 5 × 10⁻⁶ − M′_k/51200, where
h²/8 = 1/51200; here Φ4_k bounds |φ⁗| on the cell, because R′ increases with v and so the cell's radii lie in [R′_k −
5.3 × 10⁻⁶, R′_(k+1) + 5.3 × 10⁻⁶]. On the cell, R lies in that interval, μ in [μ_k − 10⁻⁵, μ_(k+1) + 10⁻⁵] (μ
increases with v), and V′ in [min(V_k, V_(k+1)) − 2 × 10⁻⁴, max(V_k, V_(k+1)) + 2 × 10⁻⁴] with V_k := 1 + φ′_k, since
φ′_k is within 5 × 10⁻⁷ of φ′(R′_k), |φ″| ≤ 0.01 and R′_(k+1) − R′_k ≤ 0.013. So f lies between 1 − (μ_(k+1) +
10⁻⁵)/(R′_k − 5.3 × 10⁻⁶)² and 1 − (μ_k − 10⁻⁵)/(R′_(k+1) + 5.3 × 10⁻⁶)², and c ≥ c_k, the value of c with the largest
f and V′ in the numerator and the largest R, V′ and smallest fV′ in the denominator. Every row has L_k > 0, and the
bound column gives κ′K′^l_l ≤ −c_k L_k ≤ −3.041 × 10⁻⁴ on every cell.

*Σ′ after the shell.* For R ∈ [R′(4.5), 5.75], R′(4.5) ≥ 5.372519, μ = μ(4.5) ∈ [3.60579, 3.60582] and μ̇ = 0; φ″ ≥
−0.01 l2 ≥ −0.0027323 and V′ ∈ [1, 1.0014840] (φ′ ≥ 0 there), and f ∈ [0.875075, 0.890941]. So Ξ ≥ −0.0027323 +
(3.60579/5.75³)(3 − 0.890941 × 1.0014840) ≥ 0.037244 and c ≥ 0.32321/(5.75 × 1.0014840² × 1.124925²) ≥ 0.044287, so
κ′K′^l_l ≤ −1.6 × 10⁻³. For R ≥ 5.75, Σ′ = Σ_τ0, μ is constant and μ̇ = 0, so N_κ = −2μ/R³ − μ²/R⁵ < 0; hence κ > 0,
K^l_l < 0 and κK^l_l < 0. This proves (a).

*The band on Σ_τ0.* Where v̂ ≤ v̂(3) or v̂ ≥ v̂(4.5), that is R ≤ R0(3) ≈ R0_0 = 3.8253316 or R ≥ R0(4.5) ≈ R0_120 =
5.3724596, μ̇ = 0 and N_κ < 0. For v ∈ [3, 4.5] use [[sec:table-sigma0]]. The true N_κ(v_k) differs from N_k by at most

    0.044547 × 10⁻⁵ + 0.034175 × 8.4 × 10⁻⁶ + 0.16634 × 4 × 10⁻⁶ + 5 × 10⁻⁹ ≤ 1.5 × 10⁻⁶ ≤ 5 × 10⁻⁶,

the terms coming from μ, μ̇ and the radius v̂ + 0.68 (as above, by [[lem:margins-shell-data]] (c)) and from the
rounding of N_k, with |H_μ| ≤ 0.044547, H_μ̇ ≤ 0.034175 and |H_R| ≤ 0.12184 + 0.01787 × 2.49 ≤ 0.16634 from the proof
of [[lem:margins-curvature]]. On each cell [[lem:margins-enclosure]] (b) and [[lem:margins-curvature]] (a) give the
sign column. Cells 0–34 and 55–119 are negative, cells 37–53 positive. On the remaining cells write v = v_k + s/80. By
[[lem:margins-enclosure]] (b), with |g′| ≤ 0.0157 and [[lem:margins-shell-data]] (c), R0(v) is within 4.5 × 10⁻⁶ of (1 −
s)R0_k + sR0_(k+1), and N_κ(v) is within 5 × 10⁻⁶ + M_k/51200 of (1 − s)N_k + sN_(k+1). Hence:

- cell 35, s ∈ [0, 0.762]: N_κ ≤ max(−0.00049105, 0.238 × (−0.00049105) + 0.762 × 0.00000012) + 5 × 10⁻⁶ + 1.17/51200 ≤
  −8.8 × 10⁻⁵, and at s = 0.762, R0 ≥ 4.2783783 + 0.762 × 0.0129271 − 4.5 × 10⁻⁶ ≥ 4.288224;
- cell 36, s ∈ [0.323, 1]: N_κ ≥ min(0.323 × 0.00042441 + 0.677 × 0.00000012, 0.00042441) − 5 × 10⁻⁶ − 1.14/51200 ≥
  1.09 × 10⁻⁴, and at s = 0.323, R0 ≤ 4.2913054 + 0.323 × 0.0129260 + 4.5 × 10⁻⁶ ≤ 4.295486;
- cell 54, s ∈ [0, 0.156]: N_κ ≥ min(0.00012015, 0.844 × 0.00012015 − 0.156 × 0.00021986) − 5 × 10⁻⁶ − 0.82/51200 ≥
  4.6 × 10⁻⁵, and at s = 0.156, R0 ≥ 4.5238047 + 0.156 × 0.0129054 − 4.5 × 10⁻⁶ ≥ 4.525813;
- cell 54, s ∈ [0.556, 1]: N_κ ≤ max(0.444 × 0.00012015 − 0.556 × 0.00021986, −0.00021986) + 5 × 10⁻⁶ + 0.82/51200 ≤
  −4.7 × 10⁻⁵, and at s = 0.556, R0 ≤ 4.5238047 + 0.556 × 0.0129054 + 4.5 × 10⁻⁶ ≤ 4.530985.

Since R0 is increasing, N_κ < 0 on R ∈ [R_*, 4.288224] ⊃ [R_*, 4.2882] and on [4.530985, ∞) ⊃ [4.5310, ∞), and N_κ > 0
on [4.295486, 4.525813] ⊃ [4.2955, 4.5258]. On Σ_τ0, K^l_l < 0 and κ = −N_κ/(2 − f)^(3/2), so the split is hyperbolic
where N_κ < 0 and not hyperbolic where N_κ > 0. By continuity N_κ vanishes in each of the two intervals left over. ∎

The rows give more than the statement: κ′K′^l_l ≤ −3.04 × 10⁻⁴ on Σ′ ∩ {R_* ≤ R ≤ 5.75}. The largest cell bounds occur
on the cells around R = 4.66, where the bend's central lobe is on its falling side. For 0.68 ≤ R ≤ R_*, where Σ′ =
Σ_τ0, the margin is that of [[thm:bg-margins]] (c).

#### Γ on the seed region {#sec:margins-seed}

On a vacuum region of the background, in the chart (v̂, R), g = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃² with f = 1 −
μ/R², μ constant and ψ = ψ(v̂), the slice Σ_τ0 (v̂ = τ0 + R) has γ = G dR² + R² dΩ₃² with G = e^ψ(2 − e^ψ f), and
N_s√G = 1. Along it write ψ, ψ′ and ψ″ for ψ(τ0 + R) and its derivatives, q := e^ψ, u := 1 − q, m := μ/R² and w := qf =
q(1 − m). The quantities ν, β, a, E, P and Γ of [[thm:charge-identity]] are then ν = R³, β = R N_κ/(3(2 − w)(w −
1)) with N_κ = (q f′/2)(w − 3) − ψ′ and f′ = 2μ/R³ (from κ0 and Y0 of [[lem:racz-split-formulas]]; N_κ is the
quantity of [[lem:margins-racz]], here with ψ ≠ 0 and μ̇ = 0), a = −3(1 − β)/R, E = e^(∫a), P = 8νE²R/G − (2νER/√G)′
RE/√G and Γ = 4νE² − P′.

**Lemma {#lem:margins-gamma-form}** (Γ/E² in closed form.) On such a region, wherever w < 1,

    Γ/E² = A0 + A1 ψ′ + A2 ψ′² + A3 ψ″,   {#eq:margins-gamma-form}

    A0 := 4R³ n0/(q(2 − w)(1 − w)²),
    n0 := m³ − 2m(2m² − m + 1)u + (2m + 1)(3m² − 5m + 4)u² − 4m(m − 1)²u³ + (m − 1)³u⁴,
    A1 := 2R⁴ (m(5 − m) − (1 − m)(7 + m)u)/((2 − w)(1 − w)²),
    A2 := 2R⁵ (1 − m)(1 + 2w)/((2 − w)(1 − w)²),     A3 := 2R⁵ (1 − m)/((2 − w)(1 − w)).

Where ψ = 0 this is Γ/E² = 4R³μ/(R² + μ), that is Γ = 4μ/R for the normalisation E = √G/R.

*Proof.* Since E′ = aE and ν = R³, (2νER/√G)′ = E((2R⁴/√G)′ + 2aR⁴/√G), so P = E²p with p := 8R⁴/G − R(2R⁴/√G)′/√G −
2aR⁵/G = (R⁵/G)(G′/G − 2a), and Γ/E² = 4R³ − 2ap − p′. Here G′/G = ψ′ − w′/(2 − w) with w′ = q(ψ′f + f′), and a =
−3/R + N_κ/((2 − w)(w − 1)). Substituting, p′ contains ψ″ linearly through ψ″ in (G′/G)′ and in N_κ′ = (q/2)(ψ′f′ +
f″)(w − 3) + (qf′/2)w′ − ψ″, f″ = −6μ/R⁴. Clearing the common denominator qR⁶(2 − w)(1 − w)² and collecting the
coefficients of 1, ψ′, ψ′² and ψ″, the numerator of the ψ′⁰ term becomes 4R⁹n0 after the substitution q = 1 − u, m =
μ/R², which gives the stated A0, A1, A2, A3. At ψ = 0, u = 0 and ψ′ = ψ″ = 0, so Γ/E² = A0 = 4R³m³/((1 + m)m²) =
4R³μ/(R² + μ). Since E′ = aE fixes E only up to a constant factor, and Γ scales with E², the last statement is for
the normalisation E = √G/R, which solves E′ = aE where ψ = 0; there E² = (R² + μ)/R⁴, and Γ = 4μ/R. ∎

**Lemma {#lem:margins-profile-monotone}** (The reference profile.) On [0.02, 1.181], ψ_s is increasing, ψ_s′ is positive
and decreasing, and ψ_s″ is negative and increasing.

*Proof.* ψ_s‴(v̂) = 60c_5 v̂² + 24c_4 v̂ + 6c_3 has positive leading coefficient and discriminant (24c_4)² − 4(60c_5)
(6c_3) = 2.6861 × 10⁻⁴ − 3.1207 × 10⁻⁴ < 0, so ψ_s‴ > 0. Hence ψ_s″ increases, and ψ_s″(1.181) = −0.0325045 < 0. So ψ_s′
decreases, and ψ_s′(1.181) = 0.0617566 > 0. So ψ_s increases. ∎

**Proposition {#prop:margins-seed}** (Γ on the seed region.) Let (ψ_s, μ_s) be the reference profile of
[[sec:table-seed-profile]] and let Γ/E² be given by [[eq:margins-gamma-form]] on R ∈ [0.70, 1.861].

(a) For ψ = ψ_s, ψ′ = ψ_s′, ψ″ = ψ_s″ (at τ0 + R) and μ = μ_s, Γ/E² ≥ 0.4475.

(b) For every μ with |μ − μ_s| ≤ 10⁻⁴ and every (ψ, ψ′, ψ″) with |ψ − ψ_s| ≤ 10⁻³, |ψ′ − ψ_s′| ≤ 10⁻³ and |ψ″ − ψ_s″| ≤
3 × 10⁻² at τ0 + R, Γ/E² ≥ 0.048. In particular Γ > 0 on the seed region for every background whose profile ψ past the
outgoing packet is within (10⁻³, 10⁻³, 3 × 10⁻²) of ψ_s in C² there and whose mass there is within 10⁻⁴ of μ_s.

*Proof.* Cover [0.70, 1.861] by the thirty-two cells of [[sec:table-seed-cells]]. On a cell, by
[[lem:margins-profile-monotone]], ψ_s, ψ_s′ and ψ_s″ range over the intervals between their values at the ends of the
cell, which lie within 5 × 10⁻⁸ of the printed end values. For (a) take the intervals between the printed end values,
each end moved outward by 5 × 10⁻⁸, and μ = μ_s; for (b) widen these intervals further by 10⁻³, 10⁻³ and 3 × 10⁻², and
take μ ∈ [μ_s − 10⁻⁴, μ_s + 10⁻⁴]. Evaluate [[eq:margins-gamma-form]] in the written form by [[lem:margins-enclosure]]
(a), with R the cell, q = e^ψ, u = 1 − q, m = μ/R², w = q(1 − m) and 2 − w, 1 − w positive on every cell. The resulting
lower ends are columns (a) and (b); their least values are 0.456 and 0.438, which exceed 0.4475 and 0.048. ∎

By [[prop:bg-seed]] (c), the background itself lies in the tube of (b), which gives Γ > 0 on its seed region
and so [[cor:loc-charge-seed]] there.

### Tables for the background below R_* {#sec:tab-bg}

These tables carry the objects and the finite lists of inequalities used in [[sec:bg-below]]; the reference quintic
ψ_s and the mass μ_s are those of [[sec:table-seed-profile]]. A number written with a decimal point and no exponent in
the definition of an object (the approximants R̂ and Ψ̃) is an exact decimal. In the rows, the segment ends, the radii
r of [[sec:tab-bg-nprime-defects]], the u- and ρ-ranges of the seed and slice tables and the entries 0 are exact
decimals. Every other number in a row is a bound rounded outward: an upper bound, or a lower bound when it is the left
entry of a range [x, y] or is named a minimum (Ŝ_min). Each row is checked from the rows above it and from the
objects, by the rule named in its table; later rows use the rounded values as printed, and an entry obtained from
other entries of its own row uses their unrounded values.

#### The approximant R̂ on 𝒞_in {#sec:tab-bg-nprime}

Used in [[prop:bg-nprime]]. On each segment [a, b] with centre c = (a + b)/2 and half-width h = (b − a)/2,
R̂(u) = Σ_n q_n x^n with x = (u − c)/h. On [5.7, 5.73], R̂(u) = 2.321 − 0.47 (u − 5.7) exactly; on [7.17, 7.2]
and on the ten middle segments the coefficients q_0, q_1, … are listed in order.

    [5.73, 5.76], degree 13:
       2.2998499990950535  −0.0070500035890575  −0.0000000060858802  −0.0000000056421213  −0.0000000029838424
      −0.0000000008027414  −0.0000000000389979   0.0000000000246103  −0.0000000000001755  −0.0000000000011116
       0.0000000000002192   0.0000000000000118  −0.0000000000000164   0.0000000000000042
    [5.76, 5.82], degree 15:
       2.2786993577610023  −0.0141016088531818   −0.000001586340491  −0.0000007379693574   −0.000000135054667
       0.0000000061654714    0.000000002299025  −0.0000000006150883   0.0000000000589794   0.0000000000112707
      −0.0000000000067499   0.0000000000017849  −0.0000000000002774  −0.0000000000000017   0.0000000000000193
      −0.0000000000000084
    [5.82, 5.94], degree 16:
       2.2363516271359387  −0.0282837186015477  −0.0000519583306435  −0.0000122418284956  −0.0000001553492355
       0.0000001448806995  −0.0000000282960554   0.0000000034633536  −0.0000000000233548  −0.0000000001515256
       0.0000000000614766  −0.0000000000173817   0.0000000000039655  −0.0000000000007088     0.00000000000007
       0.0000000000000154  −0.0000000000000127
    [5.94, 6.18], degree 16:
       2.1507106159236233  −0.0578222878944627  −0.0006088924305476  −0.0000743592803576   0.0000051739934834
       −0.000000196256404  −0.0000000375600006   0.0000000218908869  −0.0000000064354619   0.0000000016268568
      −0.0000000003684261   0.0000000000752613  −0.0000000000131408   0.0000000000015668   0.0000000000001006
      −0.0000000000001608   0.0000000000000764
    [6.18, 6.45], degree 12:
       2.0244713027588781  −0.0688957272089234  −0.0012184273694516  −0.0000557533006197   0.0000055757675211
      −0.0000000531698062   0.0000000490093513   0.0000000006653872   0.0000000001590086   0.0000000000536128
      −0.0000000000097832   0.0000000000024203  −0.0000000000004742
    [6.45, 6.72], degree 13:
         1.88145090674259  −0.0742543422751787  −0.0014107079525908   −0.000004571052586   0.0000084964203915
       0.0000007324548516   0.0000000981891648   0.0000000074893653   0.0000000005653132  −0.0000000000216173
      −0.0000000000165583  −0.0000000000045627  −0.0000000000010113  −0.0000000000002002
    [6.72, 6.96], degree 17:
       1.7362595722650483  −0.0705245743098549  −0.0009342760728852   0.0000720510034886   0.0000139979568905
       0.0000012393137233   0.0000000173638379  −0.0000000355003694  −0.0000000134826554  −0.0000000037602767
      −0.0000000009124067  −0.0000000001991244  −0.0000000000382667   −0.000000000005813  −0.0000000000003305
       0.0000000000002365   0.0000000000001464   0.0000000000000597
    [6.96, 7.08], degree 17:
       1.6286930628775715  −0.0363129947398262  −0.0000979618268921    0.000020798590445    0.000000467032891
      −0.0000002664969984  −0.0000000660309664  −0.0000000095694054  −0.0000000004759122   0.0000000002706222
       0.0000000001315469   0.0000000000399254   0.0000000000096217   0.0000000000018496   0.0000000000002291
      −0.0000000000000178  −0.0000000000000254  −0.0000000000000116
    [7.08, 7.14], degree 16:
       1.5740727877810153  −0.0182353077784798  −0.0000033244579763   0.0000015071548069  −0.0000002559486535
      −0.0000000186220094   0.0000000044324424   0.0000000014060415   0.0000000001597877  −0.0000000000196339
      −0.0000000000147541  −0.0000000000041624  −0.0000000000006994   −0.000000000000016   0.0000000000000403
       0.0000000000000189   0.0000000000000057
    [7.14, 7.17], degree 14:
       1.5467160721518957  −0.0091193559889629  −0.0000000134555429   0.0000000123940299   −0.000000006485739
       0.0000000017045675  −0.0000000000655028  −0.0000000000553616  −0.0000000000011271   0.0000000000024463
       0.0000000000005198  −0.0000000000000188  −0.0000000000000367  −0.0000000000000098  −0.0000000000000007
    [7.17, 7.2], degree 1:
       1.5284773462999573  −0.0091193639012004

The function Ŝ(u) := 2.067575 − (1/2) ∫ from 5.7 to u of R̂ is a polynomial on each segment. Its values at the
segment ends, rounded to 10 digits (only the exact values enter the rows), are:

    Ŝ(5.7) = 2.0675750000   Ŝ(5.73) = 2.0328657500   Ŝ(5.76) = 1.9983680001   Ŝ(5.82) = 1.9300070360
    Ŝ(5.94) = 1.7958269796   Ŝ(6.18) = 1.5377659380   Ŝ(6.45) = 1.2645169898   Ŝ(6.72) = 1.0105843680
    Ŝ(6.96) = 0.8022702543   Ŝ(7.08) = 0.7045506247   Ŝ(7.14) = 0.6573284758   Ŝ(7.17) = 0.6341277349
    Ŝ(7.2) = 0.6112005747

#### The data on 𝒞_in: the defects {#sec:tab-bg-nprime-defects}

Used in [[prop:bg-nprime]]. For the ten middle segments, δ bounds |R̂″ + ℬ/(3R̂²)| on [a, b] by [[lem:bg-tools]]
(b): r = (4/5) min(c − 5.7, 7.2 − c) is the radius of the disc, M bounds |R̂″| + |ℬ|/(3|R̂|²) on it (with
|ℬ| bounded by [[eq:bg-bump-disc]]), "tail" is Σ_(n<60) |δ_n| h^n for the Taylor coefficients δ_n of R̂″ + ℬ/(3R̂²)
at c, and "rest" is M (h/r)⁶⁰/(1 − h/r). On the two outer segments R̂ is affine and δ := ℬ_max/(3 R̂_min²).

| segment | r | M | tail | rest | δ |
|---|---|---|---|---|---|
| [5.7, 5.73] | — | — | — | — | 8.40·10⁻⁷ |
| [5.73, 5.76] | 0.036 | 5.49·10⁻³ | 6.26·10⁻¹⁰ | 1.5·10⁻²⁵ | 6.27·10⁻¹⁰ |
| [5.76, 5.82] | 0.072 | 0.0589 | 8.62·10⁻¹⁰ | 1.6·10⁻²⁴ | 8.63·10⁻¹⁰ |
| [5.82, 5.94] | 0.144 | 0.190 | 6.29·10⁻¹⁰ | 5.0·10⁻²⁴ | 6.30·10⁻¹⁰ |
| [5.94, 6.18] | 0.288 | 0.375 | 8.41·10⁻¹⁰ | 9.9·10⁻²⁴ | 8.42·10⁻¹⁰ |
| [6.18, 6.45] | 0.492 | 0.547 | 9.51·10⁻¹⁰ | 1.6·10⁻³⁴ | 9.52·10⁻¹⁰ |
| [6.45, 6.72] | 0.492 | 0.661 | 4.80·10⁻¹⁰ | 1.9·10⁻³⁴ | 4.81·10⁻¹⁰ |
| [6.72, 6.96] | 0.288 | 0.609 | 6.78·10⁻¹⁰ | 1.7·10⁻²³ | 6.79·10⁻¹⁰ |
| [6.96, 7.08] | 0.144 | 0.368 | 5.15·10⁻¹⁰ | 9.7·10⁻²⁴ | 5.16·10⁻¹⁰ |
| [7.08, 7.14] | 0.072 | 0.125 | 4.96·10⁻¹⁰ | 3.3·10⁻²⁴ | 4.97·10⁻¹⁰ |
| [7.14, 7.17] | 0.036 | 0.0121 | 8.20·10⁻¹⁰ | 3.2·10⁻²⁵ | 8.21·10⁻¹⁰ |
| [7.17, 7.2] | — | — | — | — | 1.94·10⁻⁶ |

#### The data on 𝒞_in: the comparison {#sec:tab-bg-nprime-chain}

Used in [[prop:bg-nprime]]. On each segment, [R̂_min, R̂_max] encloses R̂ (by q_0 ∓ Σ_(n≥1) |q_n|); ℬ_max is the
largest value of ℬ there; Λ := ℬ_max (R̂_max + 10⁻⁶ + R̂_max)/(3 (R̂_min − 10⁻⁶)² R̂_min²) is the constant of
[[lem:bg-comparison]] (a); j₀, j₁ are the jumps of R̂ and R̂′ at the left end; E₀, E₁ bound |R − R̂| and |R′ − R̂′|
on the segment (they are the values of [[eq:bg-comparison-2]] at its right end); I bounds ∫ from 5.7 to b of
|R − R̂|. Entries 0 are exact.

| segment | [R̂_min, R̂_max] | ℬ_max | Λ | j₀, j₁ | E₀ | E₁ | I |
|---|---|---|---|---|---|---|---|
| [5.7, 5.73] | [2.30689, 2.32101] | 1.34·10⁻⁵ | 7.33·10⁻⁷ | 0, 0 | 3.79·10⁻¹⁰ | 2.53·10⁻⁸ | 1.14·10⁻¹¹ |
| [5.73, 5.76] | [2.29279, 2.30691] | 6.88·10⁻³ | 3.83·10⁻⁴ | 3.3·10⁻¹², 1.8·10⁻⁹ | 1.20·10⁻⁹ | 2.72·10⁻⁸ | 4.75·10⁻¹¹ |
| [5.76, 5.82] | [2.26459, 2.29281] | 0.155 | 9.01·10⁻³ | 3.5·10⁻¹⁵, 1.2·10⁻¹² | 2.84·10⁻⁹ | 2.73·10⁻⁸ | 2.18·10⁻¹⁰ |
| [5.82, 5.94] | [2.20800, 2.26470] | 0.720 | 0.0458 | 9.7·10⁻¹⁵, 1.3·10⁻¹² | 6.13·10⁻⁹ | 2.75·10⁻⁸ | 9.54·10⁻¹⁰ |
| [5.94, 6.18] | [2.09219, 2.20923] | 1.47 | 0.113 | 3.8·10⁻¹⁴, 7.3·10⁻¹² | 1.28·10⁻⁸ | 2.80·10⁻⁸ | 4.03·10⁻⁹ |
| [6.18, 6.45] | [1.95429, 2.09465] | 1.71 | 0.164 | 8.6·10⁻¹⁴, 1.4·10⁻¹¹ | 2.05·10⁻⁸ | 2.91·10⁻⁸ | 9.57·10⁻⁹ |
| [6.45, 6.72] | [1.80577, 1.95713] | 1.71 | 0.210 | 1.1·10⁻¹³, 3.7·10⁻¹² | 2.86·10⁻⁸ | 3.07·10⁻⁸ | 1.73·10⁻⁸ |
| [6.72, 6.96] | [1.66471, 1.80781] | 1.47 | 0.231 | 6.3·10⁻¹⁴, 2.6·10⁻¹² | 3.62·10⁻⁸ | 3.27·10⁻⁸ | 2.60·10⁻⁸ |
| [6.96, 7.08] | [1.59226, 1.66513] | 0.720 | 0.125 | 3.3·10⁻¹⁴, 3.8·10⁻¹² | 4.02·10⁻⁸ | 3.34·10⁻⁸ | 3.09·10⁻⁸ |
| [7.08, 7.14] | [1.55583, 1.59232] | 0.155 | 0.0281 | 4.6·10⁻¹⁵, 2.4·10⁻¹² | 4.23·10⁻⁸ | 3.36·10⁻⁸ | 3.35·10⁻⁸ |
| [7.14, 7.17] | [1.53759, 1.55584] | 6.88·10⁻³ | 1.28·10⁻³ | 1.8·10⁻¹⁵, 2.4·10⁻¹³ | 4.34·10⁻⁸ | 3.37·10⁻⁸ | 3.49·10⁻⁸ |
| [7.17, 7.2] | [1.51935, 1.53760] | 1.34·10⁻⁵ | 2.58·10⁻⁶ | 8.0·10⁻¹⁶, 7.8·10⁻¹³ | 4.53·10⁻⁸ | 9.20·10⁻⁸ | 3.63·10⁻⁸ |

#### The ray approximant Ψ̃ {#sec:tab-bg-ray}

Used in [[prop:bg-rays]]. For 5.7 ≤ u ≤ 7.2 and 2.32 ≤ ρ ≤ 3.44,

    Ψ̃(u, ρ) = Σ_(j=0)^(24) Σ_(k=0)^(12) c_(jk) T_j((u − 6.45)/0.75) T_k((ρ − 2.88)/0.56),

T_j the Chebyshev polynomials. The table lists 10¹⁴ c_(jk), an integer, row by row: for each j, the thirteen
values k = 0, …, 12 (a row continues on the next line when it is long).

    j =  0: 244176616978007 51400021862843 671645233012 −78974944331 7420935757 −484787420 4338070 4564758 −796053 73258
            −1320 −894 181
    j =  1: −45699475162490 −4897720259727 713958831794 −80737788821 6673110559 −238128747 −42332061 11013228 −1440062
            106771 1746 −2007 343
    j =  2: −2075143227302 −320844165164 45719533864 −1583293384 −930255437 289780173 −52390770 6663225 −532273 −3129
            10008 −2048 244
    j =  3: −146521686402 −58127732860 8528288407 −313820324 −166767407 47249585 −6394172 177590 147672 −45039 8043 −966
            60
    j =  4: 56737618666 −42087652968 6015022739 −515897661 −2783126 9182790 −1428471 22673 38232 −9862 1284 −20 −31
    j =  5: 4323029756 −8405479500 1042555013 −15371100 −24817740 6378740 −887131 53245 7794 −2660 333 5 −10
    j =  6: 966394828 −1983981123 229082323 3847547 −7280779 1528163 −137381 −13607 7604 −1525 171 −2 −4
    j =  7: −228677984 −265838381 18069334 6117289 −2231302 345646 −10306 −9063 2667 −396 18 8 −2
    j =  8: −1060053129 388823196 −64198387 9513062 −1198536 92201 7333 −4408 888 −89 −5 4 −1
    j =  9: −213158599 116609501 −18345428 1785094 7127 −52822 15118 −2798 347 −15 −6 2 0
    j = 10: −285058764 132360948 −19502032 2007652 −93106 −16335 5208 −752 36 14 −5 1 0
    j = 11: −44263760 29815889 −4078136 198146 58572 −19813 3480 −374 7 7 −2 0 0
    j = 12: −16192382 9909126 −1261487 43154 21568 −5961 795 −21 −18 6 −1 0 0
    j = 13: 2525529 −294014 141162 −44033 9159 −1152 6 39 −11 2 0 0 0
    j = 14: 21286491 −9016567 1358668 −159671 13637 −396 −145 39 −6 0 0 0 0
    j = 15: 5943312 −3229500 473158 −34977 −2938 1571 −324 45 −4 0 0 0 0
    j = 16: 11812749 −5282380 767282 −78180 3936 430 −139 17 0 0 0 0 0
    j = 17: 2537380 −1464081 203762 −11424 −2322 836 −146 16 −1 0 0 0 0
    j = 18: 3034515 −1406261 199167 −18039 318 232 −46 4 0 0 0 0 0
    j = 19: 428361 −272776 35282 −1019 −681 187 −27 2 0 0 0 0 0
    j = 20: −287304 102205 −17104 2799 −422 49 −2 −1 0 0 0 0 0
    j = 21: −234497 117001 −17714 1501 52 −49 11 −2 0 0 0 0 0
    j = 22: −903957 396067 −57831 6074 −359 −20 9 −1 0 0 0 0 0
    j = 23: −327046 177840 −25268 1593 234 −94 17 −2 0 0 0 0 0
    j = 24: −448856 199469 −28849 2902 −139 −17 5 −1 0 0 0 0 0

At u = 7.2 every T_j equals 1, so Φ̃(ρ) := Ψ̃(7.2, ρ) = Σ_k C_k T_k((ρ − 2.88)/0.56) with C_k = Σ_j c_(jk).

#### The rays: the defects {#sec:tab-bg-ray-defects}

Used in [[prop:bg-rays]]. The box is [a, b] × [2.32, 3.44]. Ŝ_min = Ŝ(b) (rounded down); [Ψ̃_min, Ψ̃_max] and the
bounds on the absolute values of J̃ = ∂_ρΨ̃, K̃ = ∂_ρ²Ψ̃, L̃ = ∂_ρ³Ψ̃ are given by [[lem:bg-tools]] (a) from the
Chebyshev coefficients of these polynomials on the box; ς_m is the sum of the absolute values of the Chebyshev
coefficients on the box of
∂_ρ^m P, P the polynomial [[eq:bg-ray-numerator]]; D_m bounds the defect of order m by [[eq:bg-ray-defects]].

| segment | Ŝ_min | [Ψ̃_min, Ψ̃_max] | J̃ bound | K̃ bound | L̃ bound |
|---|---|---|---|---|---|
| [5.7, 5.73] | 2.0328657 | [2.30393, 3.44026] | 1.002 | 6.12·10⁻³ | 0.0105 |
| [5.73, 5.76] | 1.998368 | [2.28930, 3.42323] | 1.002 | 0.0124 | 0.0211 |
| [5.76, 5.82] | 1.930007 | [2.25847, 3.40643] | 1.003 | 0.0251 | 0.0423 |
| [5.82, 5.94] | 1.7958269 | [2.19628, 3.37277] | 1.006 | 0.0514 | 0.0850 |
| [5.94, 6.18] | 1.5377659 | [2.06833, 3.30519] | 1.012 | 0.106 | 0.167 |
| [6.18, 6.45] | 1.2645169 | [1.92225, 3.16253] | 1.007 | 0.168 | 0.246 |
| [6.45, 6.72] | 1.0105843 | [1.76700, 2.99167] | 0.9972 | 0.229 | 0.309 |
| [6.72, 6.96] | 0.80227025 | [1.62083, 2.80758] | 0.9856 | 0.284 | 0.353 |
| [6.96, 7.08] | 0.70455062 | [1.55270, 2.62984] | 0.9649 | 0.313 | 0.368 |
| [7.08, 7.14] | 0.65732847 | [1.51904, 2.53658] | 0.9528 | 0.328 | 0.372 |
| [7.14, 7.17] | 0.63412773 | [1.50249, 2.48877] | 0.9460 | 0.336 | 0.373 |
| [7.17, 7.2] | 0.61120057 | [1.48321, 2.46481] | 0.9442 | 0.344 | 0.376 |

| segment | ς₀ | ς₁ | ς₂ | ς₃ | D₀ | D₁ | D₂ | D₃ |
|---|---|---|---|---|---|---|---|---|
| [5.7, 5.73] | 2.23·10⁻⁵ | 2.79·10⁻⁶ | 6.36·10⁻⁶ | 1.31·10⁻⁴ | 5.17·10⁻⁷ | 5.15·10⁻⁷ | 8.49·10⁻⁷ | 4.68·10⁻⁶ |
| [5.73, 5.76] | 6.60·10⁻⁶ | 1.61·10⁻⁶ | 3.58·10⁻⁶ | 7.83·10⁻⁵ | 1.58·10⁻⁷ | 1.77·10⁻⁷ | 3.36·10⁻⁷ | 2.56·10⁻⁶ |
| [5.76, 5.82] | 1.11·10⁻⁵ | 1.79·10⁻⁶ | 3.54·10⁻⁶ | 3.99·10⁻⁵ | 2.82·10⁻⁷ | 2.96·10⁻⁷ | 5.11·10⁻⁷ | 2.05·10⁻⁶ |
| [5.82, 5.94] | 8.41·10⁻⁶ | 1.72·10⁻⁶ | 3.65·10⁻⁶ | 4.88·10⁻⁵ | 2.43·10⁻⁷ | 2.72·10⁻⁷ | 5.14·10⁻⁷ | 2.52·10⁻⁶ |
| [5.94, 6.18] | 3.55·10⁻⁶ | 1.80·10⁻⁶ | 3.78·10⁻⁶ | 4.19·10⁻⁵ | 1.35·10⁻⁷ | 2.01·10⁻⁷ | 4.86·10⁻⁷ | 2.80·10⁻⁶ |
| [6.18, 6.45] | 2.91·10⁻⁶ | 1.30·10⁻⁶ | 2.73·10⁻⁶ | 3.15·10⁻⁵ | 1.56·10⁻⁷ | 2.33·10⁻⁷ | 5.76·10⁻⁷ | 3.24·10⁻⁶ |
| [6.45, 6.72] | 4.33·10⁻⁶ | 1.14·10⁻⁶ | 2.42·10⁻⁶ | 4.23·10⁻⁵ | 3.44·10⁻⁷ | 4.78·10⁻⁷ | 1.15·10⁻⁶ | 6.65·10⁻⁶ |
| [6.72, 6.96] | 6.22·10⁻⁶ | 1.04·10⁻⁶ | 2.17·10⁻⁶ | 4.92·10⁻⁵ | 7.38·10⁻⁷ | 1.03·10⁻⁶ | 2.46·10⁻⁶ | 1.35·10⁻⁵ |
| [6.96, 7.08] | 6.45·10⁻⁶ | 7.41·10⁻⁷ | 1.66·10⁻⁶ | 3.76·10⁻⁵ | 9.50·10⁻⁷ | 1.29·10⁻⁶ | 3.10·10⁻⁶ | 1.54·10⁻⁵ |
| [7.08, 7.14] | 6.26·10⁻⁶ | 7.21·10⁻⁷ | 1.27·10⁻⁶ | 2.18·10⁻⁵ | 1.04·10⁻⁶ | 1.42·10⁻⁶ | 3.39·10⁻⁶ | 1.46·10⁻⁵ |
| [7.14, 7.17] | 3.60·10⁻⁶ | 6.40·10⁻⁷ | 1.23·10⁻⁶ | 2.77·10⁻⁵ | 6.29·10⁻⁷ | 9.04·10⁻⁷ | 2.28·10⁻⁶ | 1.23·10⁻⁵ |
| [7.17, 7.2] | 4.18·10⁻⁶ | 1.01·10⁻⁶ | 1.94·10⁻⁶ | 4.18·10⁻⁵ | 7.78·10⁻⁷ | 1.18·10⁻⁶ | 3.09·10⁻⁶ | 1.81·10⁻⁵ |

#### The rays: the comparison {#sec:tab-bg-ray-chain}

Used in [[prop:bg-rays]]. At u = 5.7 the errors of orders 0 to 3 are at most 1.6·10⁻¹³, 6.1·10⁻¹², 4.5·10⁻¹⁰, 2.2·10⁻⁸:
the sums of the absolute values of the Chebyshev coefficients of Ψ̃(5.7, ρ) − ρ, J̃(5.7, ρ) − 1, K̃(5.7, ρ) and
L̃(5.7, ρ).
On each segment, R̂′_max bounds |R̂′| (by Σ n|q_n|/h); Δ₁, Δ₂ and γ_m are [[eq:bg-gamma]]; H₂, H₃, H₄ bound
|∂_X^m G| on the tube [[eq:bg-tube]]; ε_m bounds the error of order m on the segment. In each row ε₀, ε₁, ε₂, ε₃ are
the values of [[eq:bg-ray-chain]] at b, taken in this order from the printed ε of the row above and the unrounded
values of the lower orders in the same row, and then rounded up.

| segment | R̂′_max | Δ₁ | Δ₂ | H₂ | H₃ | H₄ |
|---|---|---|---|---|---|---|
| [5.7, 5.73] | 0.4701 | 2.79·10⁻⁷ | 4.37·10⁻¹⁰ | 0.302 | 0.524 | 1.14 |
| [5.73, 5.76] | 0.4701 | 3.10·10⁻⁷ | 1.41·10⁻⁹ | 0.310 | 0.541 | 1.19 |
| [5.76, 5.82] | 0.4703 | 3.36·10⁻⁷ | 3.46·10⁻⁹ | 0.327 | 0.579 | 1.29 |
| [5.82, 5.94] | 0.4738 | 3.90·10⁻⁷ | 8.11·10⁻⁹ | 0.366 | 0.666 | 1.52 |
| [5.94, 6.18] | 0.4941 | 5.19·10⁻⁷ | 2.05·10⁻⁸ | 0.465 | 0.899 | 2.18 |
| [6.18, 6.45] | 0.5298 | 6.74·10⁻⁷ | 4.06·10⁻⁸ | 0.623 | 1.30 | 3.37 |
| [6.45, 6.72] | 0.5714 | 8.50·10⁻⁷ | 7.17·10⁻⁸ | 0.872 | 1.98 | 5.59 |
| [6.72, 6.96] | 0.6056 | 1.02·10⁻⁶ | 1.15·10⁻⁷ | 1.24 | 3.04 | 9.38 |
| [6.96, 7.08] | 0.6096 | 9.95·10⁻⁷ | 1.39·10⁻⁷ | 1.47 | 3.77 | 12.2 |
| [7.08, 7.14] | 0.6083 | 9.79·10⁻⁷ | 1.52·10⁻⁷ | 1.60 | 4.21 | 13.9 |
| [7.14, 7.17] | 0.6080 | 9.71·10⁻⁷ | 1.60·10⁻⁷ | 1.67 | 4.44 | 14.8 |
| [7.17, 7.2] | 0.6080 | 1.28·10⁻⁶ | 1.72·10⁻⁷ | 1.76 | 4.74 | 16.0 |

| segment | γ₀ | γ₁ | γ₂ | γ₃ | ε₀ | ε₁ | ε₂ | ε₃ |
|---|---|---|---|---|---|---|---|---|
| [5.7, 5.73] | 2.65·10⁻⁸ | 2.29·10⁻⁸ | 2.98·10⁻⁸ | 5.16·10⁻⁸ | 1.65·10⁻⁸ | 1.64·10⁻⁸ | 2.75·10⁻⁸ | 1.68·10⁻⁷ |
| [5.73, 5.76] | 3.03·10⁻⁸ | 2.59·10⁻⁸ | 3.39·10⁻⁸ | 5.92·10⁻⁸ | 2.22·10⁻⁸ | 2.27·10⁻⁸ | 3.94·10⁻⁸ | 2.50·10⁻⁷ |
| [5.76, 5.82] | 3.47·10⁻⁸ | 2.92·10⁻⁸ | 3.88·10⁻⁸ | 6.87·10⁻⁸ | 4.13·10⁻⁸ | 4.31·10⁻⁸ | 7.56·10⁻⁸ | 3.90·10⁻⁷ |
| [5.82, 5.94] | 4.45·10⁻⁸ | 3.69·10⁻⁸ | 5.03·10⁻⁸ | 9.16·10⁻⁸ | 7.59·10⁻⁸ | 8.36·10⁻⁸ | 1.59·10⁻⁷ | 7.62·10⁻⁷ |
| [5.94, 6.18] | 7.10·10⁻⁸ | 5.87·10⁻⁸ | 8.51·10⁻⁸ | 1.65·10⁻⁷ | 1.27·10⁻⁷ | 1.62·10⁻⁷ | 3.64·10⁻⁷ | 1.81·10⁻⁶ |
| [6.18, 6.45] | 1.12·10⁻⁷ | 9.49·10⁻⁸ | 1.49·10⁻⁷ | 3.09·10⁻⁷ | 2.00·10⁻⁷ | 2.85·10⁻⁷ | 7.38·10⁻⁷ | 3.73·10⁻⁶ |
| [6.45, 6.72] | 1.72·10⁻⁷ | 1.55·10⁻⁷ | 2.62·10⁻⁷ | 5.93·10⁻⁷ | 3.40·10⁻⁷ | 5.36·10⁻⁷ | 1.59·10⁻⁶ | 8.46·10⁻⁶ |
| [6.72, 6.96] | 2.52·10⁻⁷ | 2.40·10⁻⁷ | 4.44·10⁻⁷ | 1.10·10⁻⁶ | 5.78·10⁻⁷ | 1.02·10⁻⁶ | 3.36·10⁻⁶ | 1.92·10⁻⁵ |
| [6.96, 7.08] | 2.76·10⁻⁷ | 2.66·10⁻⁷ | 5.14·10⁻⁷ | 1.33·10⁻⁶ | 7.26·10⁻⁷ | 1.33·10⁻⁶ | 4.60·10⁻⁶ | 2.681·10⁻⁵ |
| [7.08, 7.14] | 2.89·10⁻⁷ | 2.80·10⁻⁷ | 5.52·10⁻⁷ | 1.46·10⁻⁶ | 8.06·10⁻⁷ | 1.51·10⁻⁶ | 5.33·10⁻⁶ | 3.13·10⁻⁵ |
| [7.14, 7.17] | 2.96·10⁻⁷ | 2.87·10⁻⁷ | 5.72·10⁻⁷ | 1.53·10⁻⁶ | 8.34·10⁻⁷ | 1.59·10⁻⁶ | 5.681·10⁻⁶ | 3.37·10⁻⁵ |
| [7.17, 7.2] | 3.77·10⁻⁷ | 3.93·10⁻⁷ | 7.94·10⁻⁷ | 2.14·10⁻⁶ | 8.69·10⁻⁷ | 1.68·10⁻⁶ | 6.10·10⁻⁶ | 3.65·10⁻⁵ |

#### The seed region {#sec:tab-bg-seed}

Used in [[prop:bg-seed]]. The bounds on the partial derivatives of ψ^(k) := Ψ_k in its arguments (Φ, Φ′, Φ″, Φ‴,
μ3), on the box of [[eq:bg-seed-box]], and the resulting Δ_k of [[eq:bg-seed-delta]]:

|  | ∂/∂Φ | ∂/∂Φ′ | ∂/∂Φ″ | ∂/∂Φ‴ | ∂/∂μ3 | Δ_k |
|---|---|---|---|---|---|---|
| k = 0 | 0.720 | 1.45 | 0 | 0 | 0.667 | 3.34·10⁻⁶ |
| k = 1 | 0.696 | 0.633 | 0.551 | 0 | 0.415 | 5.20·10⁻⁶ |
| k = 2 | 1.66 | 1.37 | 0.514 | 0.216 | 0.580 | 1.50·10⁻⁵ |

On each interval [ρ_a, ρ_b] of ρ, "Taylor" is Σ_(n≤5) |c_n| h^n for the Taylor coefficients c_n of ẽ_k at the
midpoint, h = (ρ_b − ρ_a)/2, "rest" bounds |c_6(ξ)| h⁶ for ξ in the interval (both enclosed as in the proof of
[[prop:bg-seed]] (b), c_6 on twenty equal parts), and "total" = Taylor + rest + Δ_k bounds |e_k| on the interval
([[eq:bg-seed-split]]). Rest is at most 2·10⁻¹⁰ in every row, and every total is at least the printed Taylor entry
plus 2·10⁻¹⁰ plus Δ_k.

| ρ | Taylor, k = 0 | k = 1 | k = 2 | total, k = 0 | k = 1 | k = 2 |
|---|---|---|---|---|---|---|
| [2.3282, 2.3727] | 2.685·10⁻⁵ | 2.341·10⁻⁴ | 8.407·10⁻⁴ | 3.020·10⁻⁵ | 2.394·10⁻⁴ | 8.558·10⁻⁴ |
| [2.3727, 2.4172] | 1.088·10⁻⁵ | 1.426·10⁻⁴ | 6.588·10⁻⁴ | 1.423·10⁻⁵ | 1.479·10⁻⁴ | 6.739·10⁻⁴ |
| [2.4172, 2.4617] | 1.587·10⁻⁵ | 7.349·10⁻⁵ | 4.911·10⁻⁴ | 1.922·10⁻⁵ | 7.870·10⁻⁵ | 5.062·10⁻⁴ |
| [2.4617, 2.5062] | 1.611·10⁻⁵ | 2.405·10⁻⁵ | 3.435·10⁻⁴ | 1.946·10⁻⁵ | 2.926·10⁻⁵ | 3.586·10⁻⁴ |
| [2.5062, 2.5507] | 1.576·10⁻⁵ | 3.113·10⁻⁵ | 2.188·10⁻⁴ | 1.911·10⁻⁵ | 3.634·10⁻⁵ | 2.339·10⁻⁴ |
| [2.5507, 2.5952] | 1.317·10⁻⁵ | 3.924·10⁻⁵ | 1.177·10⁻⁴ | 1.652·10⁻⁵ | 4.445·10⁻⁵ | 1.328·10⁻⁴ |
| [2.5952, 2.6397] | 9.092·10⁻⁶ | 3.962·10⁻⁵ | 3.927·10⁻⁵ | 1.244·10⁻⁵ | 4.483·10⁻⁵ | 5.428·10⁻⁵ |
| [2.6397, 2.6842] | 4.734·10⁻⁶ | 3.915·10⁻⁵ | 6.142·10⁻⁵ | 8.075·10⁻⁶ | 4.436·10⁻⁵ | 7.643·10⁻⁵ |
| [2.6842, 2.7287] | 2.950·10⁻⁶ | 3.427·10⁻⁵ | 8.383·10⁻⁵ | 6.291·10⁻⁶ | 3.948·10⁻⁵ | 9.884·10⁻⁵ |
| [2.7287, 2.7735] | 5.340·10⁻⁶ | 2.607·10⁻⁵ | 9.330·10⁻⁵ | 8.681·10⁻⁶ | 3.128·10⁻⁵ | 1.084·10⁻⁴ |

#### The slice in region III {#sec:tab-bg-slice-iii}

Used in [[prop:bg-slice]]. For ρ in [ρ_a, ρ_b], R = v̂(ρ) + 0.68 and the enclosures of ψ_III, ψ_III′ (from
[[prop:bg-rays]] and [[eq:bg-psi3]]) give, by [[lem:bg-tools]] (d) with μ3 in [0.82211214, 0.82211297], the
enclosures of qf and N_κ = (μ3 q/R³)(qf − 3) − ψ_III′ and the upper bound of κK^l_l in the second table.

| ρ | R | ψ_III | ψ_III′ |
|---|---|---|---|
| [2.321,2.3663] | [0.680000,0.804644] | [−0.2796,−0.2206] | [0.07193,0.1627] |
| [2.3663,2.4116] | [0.804643,0.927553] | [−0.2641,−0.2090] | [0.06752,0.1512] |
| [2.4116,2.4569] | [0.927552,1.048866] | [−0.2498,−0.1982] | [0.06349,0.1407] |
| [2.4569,2.5022] | [1.048865,1.168708] | [−0.2366,−0.1883] | [0.05979,0.1310] |
| [2.5022,2.5475] | [1.168707,1.287190] | [−0.2244,−0.1792] | [0.05640,0.1222] |
| [2.5475,2.5928] | [1.287189,1.404411] | [−0.2131,−0.1707] | [0.05327,0.1140] |
| [2.5928,2.6381] | [1.404410,1.520461] | [−0.2026,−0.1628] | [0.05038,0.1065] |
| [2.6381,2.6834] | [1.520460,1.635420] | [−0.1928,−0.1555] | [0.04770,0.09950] |
| [2.6834,2.7287] | [1.635419,1.749363] | [−0.1837,−0.1487] | [0.04522,0.09312] |
| [2.7287,2.77364] | [1.749362,1.861460] | [−0.1751,−0.1425] | [0.04309,0.08704] |

| ρ | qf | N_κ | κK^l_l ≤ |
|---|---|---|---|
| [2.321,2.3663] | [−0.649,−0.191] | [−8.26,−3.64] | −2.18 |
| [2.3663,2.4116] | [−0.232,0.0414] | [−4.46,−2.33] | −1.56 |
| [2.4116,2.4569] | [0.0237,0.208] | [−2.73,−1.58] | −1.02 |
| [2.4569,2.5022] | [0.192,0.330] | [−1.83,−1.13] | −0.674 |
| [2.5022,2.5475] | [0.313,0.422] | [−1.30,−0.843] | −0.454 |
| [2.5475,2.5928] | [0.403,0.492] | [−0.970,−0.650] | −0.315 |
| [2.5928,2.6381] | [0.474,0.548] | [−0.751,−0.516] | −0.224 |
| [2.6381,2.6834] | [0.529,0.593] | [−0.599,−0.419] | −0.163 |
| [2.6834,2.7287] | [0.575,0.631] | [−0.489,−0.347] | −0.121 |
| [2.7287,2.77364] | [0.612,0.662] | [−0.407,−0.292] | −0.0930 |

#### The slice in the packet {#sec:tab-bg-slice-packet}

Used in [[prop:bg-slice]]. For u in [u_a, u_b] the slice point lies on a ray with ρ in [ρ_lo, ρ_hi] (the first
table); μ, λ, ℬ are enclosed on [u_a, u_b], J = ∂_ρΨ and K = ∂_ρ²Ψ on the box, and R = v̂(ρ) + 0.68; the second
table gives the enclosures of qf and of N_κ by [[eq:bg-nk-packet]] and the upper bound of κK^l_l.

| u | ρ | R | μ | λ | ℬ |
|---|---|---|---|---|---|
| [5.7, 5.75] | [3.41516, 3.43718007] | [3.3866, 3.4372] | [1.4999, 1.5001] | [0.7615, 0.7677] | [0, 1.98·10⁻³] |
| [5.75, 5.8] | [3.39319, 3.41519] | [3.3362, 3.3868] | [1.4992, 1.5000] | [0.7552, 0.7616] | [1.97·10⁻³, 0.0832] |
| [5.8, 5.85] | [3.37125, 3.39322] | [3.2857, 3.3363] | [1.4947, 1.4993] | [0.7487, 0.7553] | [0.0831, 0.288] |
| [5.85, 5.9] | [3.34934, 3.37128] | [3.2351, 3.2858] | [1.4846, 1.4948] | [0.7421, 0.7488] | [0.287, 0.532] |
| [5.9, 5.95] | [3.32743, 3.34937] | [3.1845, 3.2353] | [1.4686, 1.4847] | [0.7353, 0.7422] | [0.531, 0.764] |
| [5.95, 6] | [3.30553, 3.32746] | [3.1338, 3.1847] | [1.4474, 1.4687] | [0.7284, 0.7354] | [0.763, 0.969] |
| [6, 6.05] | [3.28362, 3.30556] | [3.0829, 3.1339] | [1.4218, 1.4475] | [0.7213, 0.7285] | [0.968, 1.15] |
| [6.05, 6.1] | [3.26169, 3.28365] | [3.0319, 3.0831] | [1.3927, 1.4219] | [0.7142, 0.7214] | [1.14, 1.29] |
| [6.1, 6.15] | [3.23973, 3.26172] | [2.9807, 3.0321] | [1.3608, 1.3928] | [0.7069, 0.7143] | [1.28, 1.41] |
| [6.15, 6.2] | [3.21774, 3.23976] | [2.9294, 2.9809] | [1.3267, 1.3609] | [0.6996, 0.7070] | [1.40, 1.51] |
| [6.2, 6.25] | [3.19571, 3.21777] | [2.8778, 2.9295] | [1.2910, 1.3268] | [0.6922, 0.6997] | [1.50, 1.58] |
| [6.25, 6.3] | [3.17363, 3.19574] | [2.8260, 2.8780] | [1.2542, 1.2911] | [0.6848, 0.6923] | [1.57, 1.64] |
| [6.3, 6.35] | [3.15151, 3.17366] | [2.7739, 2.8261] | [1.2167, 1.2543] | [0.6773, 0.6849] | [1.63, 1.67] |
| [6.35, 6.4] | [3.12934, 3.15154] | [2.7216, 2.7741] | [1.1789, 1.2168] | [0.6697, 0.6774] | [1.66, 1.70] |
| [6.4, 6.45] | [3.10713, 3.12937] | [2.6691, 2.7218] | [1.1412, 1.1790] | [0.6621, 0.6698] | [1.69, 1.71] |
| [6.45, 6.5] | [3.08487, 3.10716] | [2.6163, 2.6693] | [1.1040, 1.1413] | [0.6544, 0.6622] | [1.69, 1.71] |
| [6.5, 6.55] | [3.06257, 3.0849] | [2.5633, 2.6165] | [1.0675, 1.1041] | [0.6467, 0.6545] | [1.66, 1.70] |
| [6.55, 6.6] | [3.04023, 3.0626] | [2.5100, 2.5635] | [1.0321, 1.0676] | [0.6389, 0.6468] | [1.63, 1.67] |
| [6.6, 6.65] | [3.01785, 3.04026] | [2.4565, 2.5102] | [0.99817, 1.0322] | [0.6310, 0.6390] | [1.57, 1.64] |
| [6.65, 6.7] | [2.99545, 3.01788] | [2.4028, 2.4567] | [0.96600, 0.99818] | [0.6230, 0.6311] | [1.50, 1.58] |
| [6.7, 6.75] | [2.97304, 2.99548] | [2.3489, 2.4030] | [0.93598, 0.96601] | [0.6149, 0.6231] | [1.40, 1.51] |
| [6.75, 6.8] | [2.95061, 2.97307] | [2.2948, 2.3491] | [0.90853, 0.93600] | [0.6066, 0.6150] | [1.28, 1.41] |
| [6.8, 6.85] | [2.9282, 2.95064] | [2.2406, 2.2950] | [0.88409, 0.90855] | [0.5982, 0.6067] | [1.14, 1.29] |
| [6.85, 6.9] | [2.90581, 2.92823] | [2.1862, 2.2407] | [0.86314, 0.88410] | [0.5896, 0.5983] | [0.968, 1.15] |
| [6.9, 6.95] | [2.88347, 2.90584] | [2.1318, 2.1864] | [0.84619, 0.86315] | [0.5806, 0.5897] | [0.763, 0.969] |
| [6.95, 7] | [2.86122, 2.8835] | [2.0774, 2.1320] | [0.83371, 0.84620] | [0.5714, 0.5807] | [0.531, 0.764] |
| [7, 7.05] | [2.83907, 2.86125] | [2.0231, 2.0776] | [0.82598, 0.83372] | [0.5617, 0.5715] | [0.287, 0.532] |
| [7.05, 7.1] | [2.81706, 2.8391] | [1.9689, 2.0232] | [0.82266, 0.82599] | [0.5516, 0.5618] | [0.0831, 0.288] |
| [7.1, 7.15] | [2.79524, 2.81709] | [1.9150, 1.9691] | [0.82211, 0.82268] | [0.5409, 0.5517] | [1.97·10⁻³, 0.0832] |
| [7.15, 7.2] | [2.77362, 2.79527] | [1.8614, 1.9151] | [0.82211, 0.82212] | [0.5295, 0.5410] | [0, 1.98·10⁻³] |

| u | J | K | qf | N_κ | κK^l_l ≤ |
|---|---|---|---|---|---|
| [5.7, 5.75] | [0.9975, 1.000] | [−4.33·10⁻⁵, 2.20·10⁻³] | [0.865, 0.877] | [−0.0827, −0.0781] | −6.47·10⁻³ |
| [5.75, 5.8] | [0.9948, 0.9976] | [2.14·10⁻³, 4.59·10⁻³] | [0.861, 0.874] | [−0.0867, −0.0793] | −6.79·10⁻³ |
| [5.8, 5.85] | [0.9919, 0.9949] | [4.52·10⁻³, 7.18·10⁻³] | [0.856, 0.870] | [−0.0887, −0.0766] | −6.76·10⁻³ |
| [5.85, 5.9] | [0.9889, 0.9921] | [7.11·10⁻³, 9.98·10⁻³] | [0.851, 0.867] | [−0.0871, −0.0722] | −6.56·10⁻³ |
| [5.9, 5.95] | [0.9857, 0.9890] | [9.91·10⁻³, 0.0130] | [0.846, 0.863] | [−0.0839, −0.0678] | −6.35·10⁻³ |
| [5.95, 6] | [0.9822, 0.9858] | [0.0129, 0.0163] | [0.840, 0.860] | [−0.0808, −0.0637] | −6.17·10⁻³ |
| [6, 6.05] | [0.9786, 0.9824] | [0.0161, 0.0198] | [0.834, 0.856] | [−0.0783, −0.0601] | −6.02·10⁻³ |
| [6.05, 6.1] | [0.9748, 0.9787] | [0.0196, 0.0235] | [0.829, 0.851] | [−0.0764, −0.0577] | −6.00·10⁻³ |
| [6.1, 6.15] | [0.9708, 0.9749] | [0.0233, 0.0274] | [0.823, 0.847] | [−0.0754, −0.0558] | −6.02·10⁻³ |
| [6.15, 6.2] | [0.9665, 0.9709] | [0.0273, 0.0317] | [0.817, 0.842] | [−0.0750, −0.0544] | −6.11·10⁻³ |
| [6.2, 6.25] | [0.9621, 0.9667] | [0.0315, 0.0361] | [0.811, 0.837] | [−0.0750, −0.0541] | −6.33·10⁻³ |
| [6.25, 6.3] | [0.9574, 0.9622] | [0.0360, 0.0409] | [0.804, 0.831] | [−0.0761, −0.0541] | −6.60·10⁻³ |
| [6.3, 6.35] | [0.9525, 0.9576] | [0.0407, 0.0459] | [0.798, 0.826] | [−0.0775, −0.0552] | −7.05·10⁻³ |
| [6.35, 6.4] | [0.9473, 0.9527] | [0.0458, 0.0513] | [0.791, 0.820] | [−0.0801, −0.0564] | −7.53·10⁻³ |
| [6.4, 6.45] | [0.9419, 0.9475] | [0.0511, 0.0570] | [0.784, 0.814] | [−0.0827, −0.0585] | −8.20·10⁻³ |
| [6.45, 6.5] | [0.9363, 0.9421] | [0.0568, 0.0630] | [0.777, 0.808] | [−0.0866, −0.0612] | −9.01·10⁻³ |
| [6.5, 6.55] | [0.9303, 0.9364] | [0.0628, 0.0694] | [0.770, 0.801] | [−0.0920, −0.0645] | −9.96·10⁻³ |
| [6.55, 6.6] | [0.9240, 0.9305] | [0.0692, 0.0762] | [0.762, 0.794] | [−0.0978, −0.0689] | −0.0112 |
| [6.6, 6.65] | [0.9175, 0.9242] | [0.0760, 0.0834] | [0.754, 0.787] | [−0.106, −0.0737] | −0.0126 |
| [6.65, 6.7] | [0.9105, 0.9176] | [0.0832, 0.0910] | [0.746, 0.779] | [−0.114, −0.0804] | −0.0145 |
| [6.7, 6.75] | [0.9032, 0.9107] | [0.0908, 0.0992] | [0.738, 0.771] | [−0.124, −0.0882] | −0.0167 |
| [6.75, 6.8] | [0.8955, 0.9034] | [0.0989, 0.108] | [0.729, 0.763] | [−0.137, −0.0984] | −0.0197 |
| [6.8, 6.85] | [0.8873, 0.8957] | [0.107, 0.117] | [0.720, 0.754] | [−0.151, −0.110] | −0.0234 |
| [6.85, 6.9] | [0.8785, 0.8875] | [0.116, 0.127] | [0.710, 0.745] | [−0.168, −0.125] | −0.0281 |
| [6.9, 6.95] | [0.8693, 0.8788] | [0.126, 0.138] | [0.701, 0.735] | [−0.190, −0.144] | −0.0343 |
| [6.95, 7] | [0.8593, 0.8695] | [0.137, 0.149] | [0.690, 0.724] | [−0.215, −0.168] | −0.0422 |
| [7, 7.05] | [0.8486, 0.8596] | [0.148, 0.161] | [0.679, 0.714] | [−0.244, −0.196] | −0.0521 |
| [7.05, 7.1] | [0.8371, 0.8489] | [0.160, 0.174] | [0.668, 0.702] | [−0.274, −0.228] | −0.0643 |
| [7.1, 7.15] | [0.8246, 0.8374] | [0.173, 0.188] | [0.655, 0.690] | [−0.300, −0.262] | −0.0777 |
| [7.15, 7.2] | [0.8111, 0.8249] | [0.187, 0.203] | [0.641, 0.679] | [−0.323, −0.289] | −0.0899 |

### Tables for the margins of the angle-localised families {#sec:table-margins}

These tables carry the objects and the rows that the proofs of [[sec:margins]] use. Every number is a terminating
decimal. Where a printed number is a rounding of a real number, the proof that uses it states the rounding and absorbs
it into its error bounds.

#### The bump and its integrals {#sec:table-bump}

The bump is β(y) := exp(1 − 1/(1 − y²)) for |y| < 1 and β(y) := 0 otherwise, and b(x; a, c) := β((2x − a − c)/(c − a)).
Its integrals are C(y) := ∫_(−1)^y β and D(y) := ∫_(−1)^y C = ∫_(−1)^y (y − s) β(s) ds. With δ := 1/20 and y_j := −1 +
jδ (j = 0, …, 40) the table lists β(y_j) and β′(y_j), rounded to ten decimals, and the numbers C̃_j, D̃_j defined by
C̃_0 = D̃_0 = 0 and

    C̃_(j+1) = C̃_j + (δ/2)(β(y_j) + β(y_(j+1))) − (δ²/12)(β′(y_(j+1)) − β′(y_j)),
    D̃_(j+1) = D̃_j + (δ/2)(C̃_j + C̃_(j+1)) − (δ²/12)(β(y_(j+1)) − β(y_j)),

evaluated with the exact values β(y_j) and β′(y_j), not their printed roundings, and with C̃ unrounded, and then
rounded to ten decimals. [[lem:margins-bump-table]] shows |C(y_j) − C̃_j| ≤ 5 × 10⁻⁵ and |D(y_j) − D̃_j| ≤ 10⁻⁴.
The table is used in [[prop:margins-bend]] and, through the values of the bend, in [[thm:margins-hyperbolic]].

| j | y_j | β(y_j) | β′(y_j) | C̃_j | D̃_j |
|---|---|---|---|---|---|
| 0 | −1.00 | 0.0000000000 | 0.0000000000 | 0.0000000000 | 0.0000000000 |
| 1 | −0.95 | 0.0000954975 | 0.0190869472 | −0.0000015890 | −0.0000000596 |
| 2 | −0.90 | 0.0140777760 | 0.7019389699 | 0.0002104820 | 0.0000022497 |
| 3 | −0.85 | 0.0740064074 | 1.6337750833 | 0.0022184541 | 0.0000504880 |
| 4 | −0.80 | 0.1690133154 | 2.0865841408 | 0.0081996119 | 0.0002911465 |
| 5 | −0.75 | 0.2764530466 | 2.1664891818 | 0.0193196241 | 0.0009567442 |
| 6 | −0.70 | 0.3825926956 | 2.0593224675 | 0.0358180940 | 0.0023130747 |
| 7 | −0.65 | 0.4811377191 | 1.8754642074 | 0.0574496582 | 0.0046242383 |
| 8 | −0.60 | 0.5697828247 | 1.6692856193 | 0.0837656257 | 0.0081361526 |
| 9 | −0.55 | 0.6481120012 | 1.4653937154 | 0.1142554738 | 0.0130703616 |
| 10 | −0.50 | 0.7165313106 | 1.2738334410 | 0.1484114650 | 0.0196227810 |
| 11 | −0.45 | 0.7757550272 | 1.0977557602 | 0.1857553063 | 0.0279646120 |
| 12 | −0.40 | 0.8265654376 | 0.9371490222 | 0.2258467776 | 0.0382440786 |
| 13 | −0.35 | 0.8697050571 | 0.7906345435 | 0.2682840638 | 0.0505883622 |
| 14 | −0.30 | 0.9058322914 | 0.6563209453 | 0.3127004796 | 0.0651054493 |
| 15 | −0.25 | 0.9355069850 | 0.5321995293 | 0.3587598201 | 0.0818857746 |
| 16 | −0.20 | 0.9591894571 | 0.4163148685 | 0.4061513738 | 0.1010036206 |
| 17 | −0.15 | 0.9772449882 | 0.3068253049 | 0.4545850452 | 0.1225182695 |
| 18 | −0.10 | 0.9899498338 | 0.2020099651 | 0.5037867523 | 0.1464749176 |
| 19 | −0.05 | 0.9974968724 | 0.1002503122 | 0.5534941199 | 0.1729053671 |
| 20 | 0.00 | 1.0000000000 | 0.0000000000 | 0.6034524272 | 0.2018285093 |
| 21 | 0.05 | 0.9974968724 | −0.1002503122 | 0.6534107345 | 0.2332506098 |
| 22 | 0.10 | 0.9899498338 | −0.2020099651 | 0.7031181021 | 0.2671654030 |
| 23 | 0.15 | 0.9772449882 | −0.3068253049 | 0.7523198091 | 0.3035539976 |
| 24 | 0.20 | 0.9591894571 | −0.4163148685 | 0.8007534806 | 0.3423845914 |
| 25 | 0.25 | 0.9355069850 | −0.5321995293 | 0.8481450343 | 0.3836119882 |
| 26 | 0.30 | 0.9058322914 | −0.6563209453 | 0.8942043748 | 0.4271769056 |
| 27 | 0.35 | 0.8697050571 | −0.7906345435 | 0.9386207905 | 0.4730050613 |
| 28 | 0.40 | 0.8265654376 | −0.9371490222 | 0.9810580768 | 0.5210060204 |
| 29 | 0.45 | 0.7757550272 | −1.0977557602 | 1.0211495481 | 0.5710717965 |
| 30 | 0.50 | 0.7165313106 | −1.2738334410 | 1.0584933894 | 0.6230752082 |
| 31 | 0.55 | 0.6481120012 | −1.4653937154 | 1.0926493806 | 0.6768680315 |
| 32 | 0.60 | 0.5697828247 | −1.6692856193 | 1.1231392287 | 0.7322790653 |
| 33 | 0.65 | 0.4811377191 | −1.8754642074 | 1.1494551962 | 0.7891123936 |
| 34 | 0.70 | 0.3825926956 | −2.0593224675 | 1.1710867604 | 0.8471464728 |
| 35 | 0.75 | 0.2764530466 | −2.1664891818 | 1.1875852303 | 0.9061353850 |
| 36 | 0.80 | 0.1690133154 | −2.0865841408 | 1.1987052425 | 0.9658150300 |
| 37 | 0.85 | 0.0740064074 | −1.6337750833 | 1.2046864003 | 1.0259196142 |
| 38 | 0.90 | 0.0140777760 | −0.7019389699 | 1.2066943724 | 1.0862166187 |
| 39 | 0.95 | 0.0000954975 | −0.0190869472 | 1.2069064434 | 1.1465595520 |
| 40 | 1.00 | 0.0000000000 | 0.0000000000 | 1.2069048544 | 1.2069048544 |

#### The reference profile on the seed region {#sec:table-seed-profile}

The reference profile is the pair (ψ_s, μ_s) with μ_s := 0.8221111759474543 and, for 0 ≤ v̂ ≤ 2.626161920655184,

    ψ_s(v̂) := c_5 v̂⁵ + c_4 v̂⁴ + c_3 v̂³ + c_2 v̂² + c_1 v̂ + c_0,

    c_5 =  0.000036266230280898565,      c_4 = −0.0006828865263100425,     c_3 =  0.005975740440748802,
    c_2 = −0.032306921548756716,         c_1 =  0.11720807953605501,       c_0 = −0.25734075580969945.

We call ψ_s the reference quintic; [[rem:bg-grid]] relates it to a numerical solution, and no proof uses that relation.
The seed region R ∈ [0.70, 1.861] of Σ_τ0 has v̂ = τ0 + R ∈ [0.02, 1.181], inside the interval of definition.
[[prop:margins-seed]] uses the pair, and [[prop:bg-seed]] compares the background with it.

#### Cells of the seed region {#sec:table-seed-cells}

Thirty-two cells [R_a, R_b] cover [0.70, 1.861]. For each, the columns give the values of ψ_s, ψ_s′ and ψ_s″ at v̂ =
τ0 + R_a and τ0 + R_b (τ0 = −0.68), rounded to seven decimals; by [[lem:margins-profile-monotone]] the exact values are
the ends of the ranges of ψ_s, ψ_s′ and ψ_s″ on the cell. Each pair of columns lists the smaller value first. Column (a)
is a lower bound for Γ/E² on the cell for the reference profile, column (b) a lower bound over the tube of
[[prop:margins-seed]] (b). Both are rounded down to three decimals. They come from [[eq:margins-gamma-form]] evaluated
by the enclosure rule of [[lem:margins-enclosure]] (a), in the form written there, with q = e^ψ, u = 1 − q and m =
μ/R², and with each printed end value moved outward by 5 × 10⁻⁸ to cover its rounding.

| R_a | R_b | ψ_s(a) | ψ_s(b) | ψ_s′(b) | ψ_s′(a) | ψ_s″(a) | ψ_s″(b) | (a) | (b) |
|---|---|---|---|---|---|---|---|---|---|
| 0.70 | 0.7091 | −0.2550095 | −0.2539572 | 0.1153429 | 0.1159230 | −0.0639000 | −0.0635774 | 0.470 | 0.460 |
| 0.7091 | 0.7182 | −0.2539572 | −0.2529102 | 0.1147658 | 0.1153429 | −0.0635774 | −0.0632561 | 0.486 | 0.475 |
| 0.7182 | 0.7272 | −0.2529102 | −0.2518799 | 0.1141980 | 0.1147658 | −0.0632561 | −0.0629397 | 0.503 | 0.493 |
| 0.7272 | 0.7363 | −0.2518799 | −0.2508433 | 0.1136267 | 0.1141980 | −0.0629397 | −0.0626211 | 0.518 | 0.507 |
| 0.7363 | 0.7454 | −0.2508433 | −0.2498119 | 0.1130583 | 0.1136267 | −0.0626211 | −0.0623038 | 0.534 | 0.523 |
| 0.7454 | 0.7544 | −0.2498119 | −0.2487969 | 0.1124989 | 0.1130583 | −0.0623038 | −0.0619913 | 0.553 | 0.542 |
| 0.7544 | 0.7635 | −0.2487969 | −0.2477757 | 0.1119362 | 0.1124989 | −0.0619913 | −0.0616767 | 0.568 | 0.557 |
| 0.7635 | 0.7726 | −0.2477757 | −0.2467596 | 0.1113764 | 0.1119362 | −0.0616767 | −0.0613634 | 0.586 | 0.574 |
| 0.7726 | 0.7907 | −0.2467596 | −0.2447537 | 0.1102713 | 0.1113764 | −0.0613634 | −0.0607442 | 0.456 | 0.445 |
| 0.7907 | 0.8088 | −0.2447537 | −0.2427677 | 0.1091774 | 0.1102713 | −0.0607442 | −0.0601302 | 0.491 | 0.479 |
| 0.8088 | 0.8270 | −0.2427677 | −0.2407906 | 0.1080886 | 0.1091774 | −0.0601302 | −0.0595180 | 0.525 | 0.513 |
| 0.8270 | 0.8451 | −0.2407906 | −0.2388439 | 0.1070168 | 0.1080886 | −0.0595180 | −0.0589144 | 0.565 | 0.553 |
| 0.8451 | 0.8632 | −0.2388439 | −0.2369165 | 0.1059559 | 0.1070168 | −0.0589144 | −0.0583159 | 0.604 | 0.592 |
| 0.8632 | 0.8814 | −0.2369165 | −0.2349978 | 0.1049000 | 0.1059559 | −0.0583159 | −0.0577192 | 0.644 | 0.631 |
| 0.8814 | 0.8995 | −0.2349978 | −0.2331085 | 0.1038606 | 0.1049000 | −0.0577192 | −0.0571309 | 0.689 | 0.675 |
| 0.8995 | 0.9176 | −0.2331085 | −0.2312380 | 0.1028318 | 0.1038606 | −0.0571309 | −0.0565477 | 0.733 | 0.719 |
| 0.9176 | 0.9539 | −0.2312380 | −0.2275422 | 0.1008002 | 0.1028318 | −0.0565477 | −0.0553932 | 0.483 | 0.466 |
| 0.9539 | 0.9902 | −0.2275422 | −0.2239194 | 0.0988100 | 0.1008002 | −0.0553932 | −0.0542587 | 0.573 | 0.551 |
| 0.9902 | 1.0265 | −0.2239194 | −0.2203681 | 0.0968607 | 0.0988100 | −0.0542587 | −0.0531440 | 0.673 | 0.644 |
| 1.0265 | 1.0628 | −0.2203681 | −0.2168868 | 0.0949516 | 0.0968607 | −0.0531440 | −0.0520489 | 0.783 | 0.745 |
| 1.0628 | 1.0991 | −0.2168868 | −0.2134741 | 0.0930818 | 0.0949516 | −0.0520489 | −0.0509732 | 0.904 | 0.855 |
| 1.0991 | 1.1354 | −0.2134741 | −0.2101286 | 0.0912507 | 0.0930818 | −0.0509732 | −0.0499167 | 1.037 | 0.973 |
| 1.1354 | 1.2080 | −0.2101286 | −0.2036335 | 0.0877018 | 0.0912507 | −0.0499167 | −0.0478605 | 0.543 | 0.438 |
| 1.2080 | 1.2805 | −0.2036335 | −0.1973992 | 0.0843041 | 0.0877018 | −0.0478605 | −0.0458812 | 0.817 | 0.663 |
| 1.2805 | 1.3530 | −0.1973992 | −0.1914060 | 0.0810473 | 0.0843041 | −0.0458812 | −0.0439743 | 1.145 | 0.906 |
| 1.3530 | 1.4256 | −0.1914060 | −0.1856362 | 0.0779219 | 0.0810473 | −0.0439743 | −0.0421357 | 1.532 | 1.174 |
| 1.4256 | 1.4982 | −0.1856362 | −0.1800886 | 0.0749275 | 0.0779219 | −0.0421357 | −0.0403664 | 1.990 | 1.466 |
| 1.4982 | 1.5708 | −0.1800886 | −0.1747537 | 0.0720591 | 0.0749275 | −0.0403664 | −0.0386646 | 2.521 | 1.775 |
| 1.5708 | 1.6434 | −0.1747537 | −0.1696227 | 0.0693118 | 0.0720591 | −0.0386646 | −0.0370289 | 3.131 | 2.089 |
| 1.6434 | 1.7159 | −0.1696227 | −0.1646935 | 0.0666845 | 0.0693118 | −0.0370289 | −0.0354595 | 3.828 | 2.399 |
| 1.7159 | 1.7884 | −0.1646935 | −0.1599507 | 0.0641687 | 0.0666845 | −0.0354595 | −0.0339526 | 4.606 | 2.681 |
| 1.7884 | 1.861 | −0.1599507 | −0.1553803 | 0.0617566 | 0.0641687 | −0.0339526 | −0.0325045 | 5.469 | 2.910 |

#### The data on the shell {#sec:table-shell}

Along the cone 𝒞_out = {u = 0}, at v_k := 3 + k/80 (k = 0, …, 120), the table lists the shell profile 𝒜_k := 𝒜(v_k) = 3.6
b(v_k; 3, 4.5) with its first two derivatives (rounded to nine, eight and six decimals), and the numbers R_k, P_k, μ_k,
v̂_k (rounded to eight decimals) that satisfy the scheme [[eq:margins-scheme]] of [[lem:margins-shell-data]] to within
10⁻⁸ in each component, the residuals summing to at most 5 × 10⁻⁷ in each component. By that lemma the true radius, its
v-derivative, the mass and the time v̂ on 𝒞_out at v_k are within 4 × 10⁻⁶, 6 × 10⁻⁷, 10⁻⁵ and 4 × 10⁻⁶ of R_k, P_k, μ_k
and v̂_k. For k = 0 the values are exact: R_0 = 13/2, P_0 = 1/2, μ_0 = 3/2 and v̂_0 = 3 + √(3/2) ln[(13/2 − √(3/2))(5 +
√(3/2))/((13/2 + √(3/2))(5 − √(3/2)))].

| k | v_k | 𝒜_k | 𝒜′_k | 𝒜″_k | R_k | P_k | μ_k | v̂_k |
|---|---|---|---|---|---|---|---|---|
| 0 | 3.00000 | 0.000000000 | 0.00000000 | 0.000000 | 6.50000000 | 0.50000000 | 1.50000000 | 3.14533158 |
| 1 | 3.01250 | 0.000000000 | 0.00000000 | 0.000004 | 6.50625000 | 0.50000000 | 1.50000000 | 3.15829125 |
| 2 | 3.02500 | 0.000002321 | 0.00139249 | 0.723823 | 6.51250000 | 0.50000000 | 1.50000000 | 3.17125000 |
| 3 | 3.03750 | 0.000343791 | 0.09161735 | 19.525674 | 6.51875000 | 0.49999999 | 1.50000063 | 3.18420784 |
| 4 | 3.05000 | 0.004178985 | 0.62610242 | 68.728752 | 6.52500000 | 0.49999983 | 1.50001434 | 3.19716477 |
| 5 | 3.06250 | 0.018686840 | 1.79054550 | 114.156738 | 6.53124999 | 0.49999883 | 1.50009651 | 3.21012079 |
| 6 | 3.07500 | 0.050679994 | 3.36930706 | 133.887351 | 6.53749996 | 0.49999560 | 1.50036216 | 3.22307591 |
| 7 | 3.08750 | 0.103284582 | 5.03942381 | 130.223695 | 6.54374985 | 0.49998828 | 1.50096720 | 3.23603012 |
| 8 | 3.10000 | 0.176061256 | 6.56861192 | 112.972133 | 6.54999962 | 0.49997485 | 1.50207760 | 3.24898344 |
| 9 | 3.11250 | 0.266423066 | 7.84212040 | 90.418679 | 6.55624918 | 0.49995352 | 1.50384622 | 3.26193586 |
| 10 | 3.12500 | 0.370910892 | 8.82829232 | 67.591157 | 6.56249840 | 0.49992276 | 1.50640094 | 3.27488739 |
| 11 | 3.13750 | 0.485989510 | 9.54128992 | 46.966903 | 6.56874718 | 0.49988142 | 1.50984115 | 3.28783802 |
| 12 | 3.15000 | 0.608447935 | 10.01560388 | 29.469781 | 6.57499537 | 0.49982868 | 1.51423897 | 3.30078776 |
| 13 | 3.16250 | 0.735553285 | 10.29153655 | 15.201271 | 6.58124282 | 0.49976400 | 1.51964256 | 3.31373661 |
| 14 | 3.17500 | 0.865072323 | 10.40794361 | 3.882485 | 6.58748939 | 0.49968709 | 1.52608013 | 3.32668456 |
| 15 | 3.18750 | 0.995230968 | 10.39914807 | −4.904814 | 6.59373492 | 0.49959787 | 1.53356382 | 3.33963162 |
| 16 | 3.20000 | 1.124650485 | 10.29404567 | −11.597414 | 6.59997926 | 0.49949638 | 1.54209315 | 3.35257778 |
| 17 | 3.21250 | 1.252279922 | 10.11626190 | −16.596299 | 6.60622226 | 0.49938279 | 1.55165787 | 3.36552304 |
| 18 | 3.22500 | 1.377333704 | 9.88474784 | −20.246894 | 6.61246376 | 0.49925736 | 1.56224041 | 3.37846740 |
| 19 | 3.23750 | 1.499237693 | 9.61450397 | −22.836229 | 6.61870362 | 0.49912040 | 1.57381776 | 3.39141085 |
| 20 | 3.25000 | 1.617584271 | 9.31728540 | −24.597633 | 6.62494170 | 0.49897229 | 1.58636296 | 3.40435339 |
| 21 | 3.26250 | 1.732095789 | 9.00222820 | −25.718143 | 6.63117786 | 0.49881341 | 1.59984632 | 3.41729502 |
| 22 | 3.27500 | 1.842595237 | 8.67637893 | −26.346307 | 6.63741197 | 0.49864417 | 1.61423636 | 3.43023574 |
| 23 | 3.28750 | 1.948982943 | 8.34512998 | −26.599370 | 6.64364390 | 0.49846501 | 1.62950044 | 3.44317552 |
| 24 | 3.30000 | 2.051218169 | 8.01257097 | −26.569463 | 6.64987353 | 0.49827634 | 1.64560542 | 3.45611438 |
| 25 | 3.31250 | 2.149304651 | 7.68176962 | −26.328741 | 6.65610075 | 0.49807860 | 1.66251797 | 3.46905230 |
| 26 | 3.32500 | 2.243279271 | 7.35499430 | −25.933562 | 6.66232544 | 0.49787221 | 1.68020494 | 3.48198927 |
| 27 | 3.33750 | 2.333203204 | 7.03388983 | −25.427835 | 6.66854751 | 0.49765758 | 1.69863358 | 3.49492530 |
| 28 | 3.35000 | 2.419155029 | 6.71961584 | −24.845677 | 6.67476683 | 0.49743511 | 1.71777170 | 3.50786036 |
| 29 | 3.36250 | 2.501225363 | 6.41295542 | −24.213520 | 6.68098334 | 0.49720521 | 1.73758778 | 3.52079446 |
| 30 | 3.37500 | 2.579512718 | 6.11440052 | −23.551765 | 6.68719692 | 0.49696827 | 1.75805106 | 3.53372759 |
| 31 | 3.38750 | 2.654120288 | 5.82421880 | −22.876085 | 6.69340750 | 0.49672464 | 1.77913160 | 3.54665973 |
| 32 | 3.40000 | 2.725153494 | 5.54250614 | −22.198449 | 6.69961500 | 0.49647471 | 1.80080030 | 3.55959088 |
| 33 | 3.41250 | 2.792718098 | 5.26922765 | −21.527922 | 6.70581933 | 0.49621881 | 1.82302888 | 3.57252103 |
| 34 | 3.42500 | 2.856918782 | 5.00424990 | −20.871302 | 6.71202043 | 0.49595728 | 1.84578993 | 3.58545017 |
| 35 | 3.43750 | 2.917858077 | 4.74736601 | −20.233615 | 6.71821823 | 0.49569045 | 1.86905685 | 3.59837828 |
| 36 | 3.45000 | 2.975635575 | 4.49831531 | −19.618503 | 6.72441266 | 0.49541865 | 1.89280388 | 3.61130537 |
| 37 | 3.46250 | 3.030347355 | 4.25679856 | −19.028534 | 6.73060367 | 0.49514216 | 1.91700601 | 3.62423142 |
| 38 | 3.47500 | 3.082085575 | 4.02248987 | −18.465445 | 6.73679119 | 0.49486130 | 1.94163900 | 3.63715641 |
| 39 | 3.48750 | 3.130938206 | 3.79504581 | −17.930331 | 6.74297517 | 0.49457633 | 1.96667934 | 3.65008035 |
| 40 | 3.50000 | 3.176988849 | 3.57411246 | −17.423798 | 6.74915557 | 0.49428755 | 1.99210419 | 3.66300321 |
| 41 | 3.51250 | 3.220316649 | 3.35933075 | −16.946080 | 6.75533234 | 0.49399521 | 2.01789137 | 3.67592500 |
| 42 | 3.52500 | 3.260996249 | 3.15034054 | −16.497134 | 6.76150543 | 0.49369957 | 2.04401931 | 3.68884569 |
| 43 | 3.53750 | 3.299097800 | 2.94678353 | −16.076713 | 6.76767481 | 0.49340088 | 2.07046704 | 3.70176527 |
| 44 | 3.55000 | 3.334686999 | 2.74830549 | −15.684424 | 6.77384044 | 0.49309940 | 2.09721411 | 3.71468374 |
| 45 | 3.56250 | 3.367825146 | 2.55455774 | −15.319777 | 6.78000228 | 0.49279534 | 2.12424058 | 3.72760109 |
| 46 | 3.57500 | 3.398569225 | 2.36519818 | −14.982218 | 6.78616031 | 0.49248894 | 2.15152699 | 3.74051729 |
| 47 | 3.58750 | 3.426971988 | 2.17989188 | −14.671157 | 6.79231449 | 0.49218042 | 2.17905432 | 3.75343235 |
| 48 | 3.60000 | 3.453082046 | 1.99831137 | −14.385992 | 6.79846481 | 0.49187000 | 2.20680394 | 3.76634625 |
| 49 | 3.61250 | 3.476943962 | 1.82013668 | −14.126126 | 6.80461123 | 0.49155790 | 2.23475762 | 3.77925898 |
| 50 | 3.62500 | 3.498598350 | 1.64505522 | −13.890981 | 6.81075374 | 0.49124431 | 2.26289743 | 3.79217053 |
| 51 | 3.63750 | 3.518081957 | 1.47276146 | −13.680005 | 6.81689233 | 0.49092944 | 2.29120579 | 3.80508088 |
| 52 | 3.65000 | 3.535427756 | 1.30295652 | −13.492687 | 6.82302697 | 0.49061349 | 2.31966536 | 3.81799002 |
| 53 | 3.66250 | 3.550665020 | 1.13534769 | −13.328554 | 6.82915766 | 0.49029665 | 2.34825906 | 3.83089795 |
| 54 | 3.67500 | 3.563819402 | 0.96964783 | −13.187184 | 6.83528438 | 0.48997910 | 2.37697005 | 3.84380465 |
| 55 | 3.68750 | 3.574912994 | 0.80557480 | −13.068205 | 6.84140714 | 0.48966105 | 2.40578163 | 3.85671011 |
| 56 | 3.70000 | 3.583964392 | 0.64285076 | −12.971297 | 6.84752591 | 0.48934267 | 2.43467731 | 3.86961432 |
| 57 | 3.71250 | 3.590988741 | 0.48120150 | −12.896200 | 6.85364070 | 0.48902415 | 2.46364069 | 3.88251727 |
| 58 | 3.72500 | 3.595997777 | 0.32035575 | −12.842706 | 6.85975151 | 0.48870566 | 2.49265551 | 3.89541895 |
| 59 | 3.73750 | 3.598999861 | 0.16004445 | −12.810669 | 6.86585834 | 0.48838738 | 2.52170555 | 3.90831933 |
| 60 | 3.75000 | 3.600000000 | 0.00000000 | −12.800000 | 6.87196120 | 0.48806949 | 2.55077467 | 3.92121843 |
| 61 | 3.76250 | 3.598999861 | −0.16004445 | −12.810669 | 6.87806009 | 0.48775217 | 2.57984674 | 3.93411621 |
| 62 | 3.77500 | 3.595997777 | −0.32035575 | −12.842706 | 6.88415501 | 0.48743558 | 2.60890562 | 3.94701267 |
| 63 | 3.78750 | 3.590988741 | −0.48120150 | −12.896200 | 6.89024598 | 0.48711990 | 2.63793515 | 3.95990781 |
| 64 | 3.80000 | 3.583964392 | −0.64285076 | −12.971297 | 6.89633301 | 0.48680531 | 2.66691909 | 3.97280160 |
| 65 | 3.81250 | 3.574912994 | −0.80557480 | −13.068205 | 6.90241612 | 0.48649198 | 2.69584114 | 3.98569405 |
| 66 | 3.82500 | 3.563819402 | −0.96964783 | −13.187184 | 6.90849532 | 0.48618008 | 2.72468487 | 3.99858513 |
| 67 | 3.83750 | 3.550665020 | −1.13534769 | −13.328554 | 6.91457063 | 0.48586978 | 2.75343370 | 4.01147484 |
| 68 | 3.85000 | 3.535427756 | −1.30295652 | −13.492687 | 6.92064208 | 0.48556127 | 2.78207090 | 4.02436316 |
| 69 | 3.86250 | 3.518081957 | −1.47276146 | −13.680005 | 6.92670968 | 0.48525471 | 2.81057953 | 4.03725009 |
| 70 | 3.87500 | 3.498598350 | −1.64505522 | −13.890981 | 6.93277346 | 0.48495029 | 2.83894242 | 4.05013561 |
| 71 | 3.88750 | 3.476943962 | −1.82013668 | −14.126126 | 6.93883345 | 0.48464818 | 2.86714215 | 4.06301973 |
| 72 | 3.90000 | 3.453082046 | −1.99831137 | −14.385992 | 6.94488968 | 0.48434856 | 2.89516101 | 4.07590241 |
| 73 | 3.91250 | 3.426971988 | −2.17989188 | −14.671157 | 6.95094218 | 0.48405162 | 2.92298096 | 4.08878366 |
| 74 | 3.92500 | 3.398569225 | −2.36519818 | −14.982218 | 6.95699099 | 0.48375755 | 2.95058363 | 4.10166347 |
| 75 | 3.93750 | 3.367825146 | −2.55455774 | −15.319777 | 6.96303614 | 0.48346653 | 2.97795023 | 4.11454183 |
| 76 | 3.95000 | 3.334686999 | −2.74830549 | −15.684424 | 6.96907767 | 0.48317876 | 3.00506160 | 4.12741872 |
| 77 | 3.96250 | 3.299097800 | −2.94678353 | −16.076713 | 6.97511563 | 0.48289443 | 3.03189810 | 4.14029414 |
| 78 | 3.97500 | 3.260996249 | −3.15034054 | −16.497134 | 6.98115005 | 0.48261374 | 3.05843959 | 4.15316808 |
| 79 | 3.98750 | 3.220316649 | −3.35933075 | −16.946080 | 6.98718100 | 0.48233691 | 3.08466545 | 4.16604053 |
| 80 | 4.00000 | 3.176988849 | −3.57411246 | −17.423798 | 6.99320850 | 0.48206413 | 3.11055446 | 4.17891148 |
| 81 | 4.01250 | 3.130938206 | −3.79504581 | −17.930331 | 6.99923263 | 0.48179562 | 3.13608484 | 4.19178092 |
| 82 | 4.02500 | 3.082085575 | −4.02248987 | −18.465445 | 7.00525342 | 0.48153161 | 3.16123416 | 4.20464886 |
| 83 | 4.03750 | 3.030347355 | −4.25679856 | −19.028534 | 7.01127094 | 0.48127232 | 3.18597931 | 4.21751526 |
| 84 | 4.05000 | 2.975635575 | −4.49831531 | −19.618503 | 7.01728526 | 0.48101798 | 3.21029651 | 4.23038014 |
| 85 | 4.06250 | 2.917858077 | −4.74736601 | −20.233615 | 7.02329643 | 0.48076883 | 3.23416121 | 4.24324348 |
| 86 | 4.07500 | 2.856918782 | −5.00424990 | −20.871302 | 7.02930451 | 0.48052512 | 3.25754810 | 4.25610528 |
| 87 | 4.08750 | 2.792718098 | −5.26922765 | −21.527922 | 7.03530959 | 0.48028709 | 3.28043107 | 4.26896552 |
| 88 | 4.10000 | 2.725153494 | −5.54250614 | −22.198449 | 7.04131173 | 0.48005501 | 3.30278318 | 4.28182421 |
| 89 | 4.11250 | 2.654120288 | −5.82421880 | −22.876085 | 7.04731100 | 0.47982914 | 3.32457662 | 4.29468133 |
| 90 | 4.12500 | 2.579512718 | −6.11440052 | −23.551765 | 7.05330750 | 0.47960976 | 3.34578275 | 4.30753688 |
| 91 | 4.13750 | 2.501225363 | −6.41295542 | −24.213520 | 7.05930129 | 0.47939715 | 3.36637202 | 4.32039086 |
| 92 | 4.15000 | 2.419155029 | −6.71961584 | −24.845677 | 7.06529247 | 0.47919159 | 3.38631406 | 4.33324326 |
| 93 | 4.16250 | 2.333203204 | −7.03388983 | −25.427835 | 7.07128113 | 0.47899339 | 3.40557765 | 4.34609407 |
| 94 | 4.17500 | 2.243279271 | −7.35499430 | −25.933562 | 7.07726735 | 0.47880285 | 3.42413077 | 4.35894329 |
| 95 | 4.18750 | 2.149304651 | −7.68176962 | −26.328741 | 7.08325125 | 0.47862027 | 3.44194074 | 4.37179092 |
| 96 | 4.20000 | 2.051218169 | −8.01257097 | −26.569463 | 7.08923291 | 0.47844597 | 3.45897425 | 4.38463694 |
| 97 | 4.21250 | 1.948982943 | −8.34512998 | −26.599370 | 7.09521245 | 0.47828026 | 3.47519762 | 4.39748137 |
| 98 | 4.22500 | 1.842595237 | −8.67637893 | −26.346307 | 7.10118997 | 0.47812345 | 3.49057694 | 4.41032419 |
| 99 | 4.23750 | 1.732095789 | −9.00222820 | −25.718143 | 7.10716559 | 0.47797586 | 3.50507845 | 4.42316540 |
| 100 | 4.25000 | 1.617584271 | −9.31728540 | −24.597633 | 7.11313943 | 0.47783779 | 3.51866895 | 4.43600501 |
| 101 | 4.26250 | 1.499237693 | −9.61450397 | −22.836229 | 7.11911160 | 0.47770954 | 3.53131630 | 4.44884300 |
| 102 | 4.27500 | 1.377333704 | −9.88474784 | −20.246894 | 7.12508223 | 0.47759137 | 3.54299020 | 4.46167938 |
| 103 | 4.28750 | 1.252279922 | −10.11626190 | −16.596299 | 7.13105145 | 0.47748352 | 3.55366309 | 4.47451414 |
| 104 | 4.30000 | 1.124650485 | −10.29404567 | −11.597414 | 7.13701939 | 0.47738621 | 3.56331135 | 4.48734729 |
| 105 | 4.31250 | 0.995230968 | −10.39914807 | −4.904814 | 7.14298617 | 0.47729957 | 3.57191685 | 4.50017883 |
| 106 | 4.32500 | 0.865072323 | −10.40794361 | 3.882485 | 7.14895194 | 0.47722367 | 3.57946885 | 4.51300876 |
| 107 | 4.33750 | 0.735553285 | −10.29153655 | 15.201271 | 7.15491683 | 0.47715848 | 3.58596644 | 4.52583707 |
| 108 | 4.35000 | 0.608447935 | −10.01560388 | 29.469781 | 7.16088097 | 0.47710386 | 3.59142147 | 4.53866377 |
| 109 | 4.36250 | 0.485989510 | −9.54128992 | 46.966903 | 7.16684449 | 0.47705947 | 3.59586201 | 4.55148886 |
| 110 | 4.37500 | 0.370910892 | −8.82829232 | 67.591157 | 7.17280752 | 0.47702480 | 3.59933632 | 4.56431235 |
| 111 | 4.38750 | 0.266423066 | −7.84212040 | 90.418679 | 7.17877017 | 0.47699910 | 3.60191686 | 4.57713423 |
| 112 | 4.40000 | 0.176061256 | −6.56861192 | 112.972133 | 7.18473254 | 0.47698133 | 3.60370370 | 4.58995451 |
| 113 | 4.41250 | 0.103284582 | −5.03942381 | 130.223695 | 7.19069474 | 0.47697019 | 3.60482575 | 4.60277320 |
| 114 | 4.42500 | 0.050679994 | −3.36930706 | 133.887351 | 7.19665683 | 0.47696413 | 3.60543725 | 4.61559029 |
| 115 | 4.43750 | 0.018686840 | −1.79054550 | 114.156738 | 7.20261887 | 0.47696148 | 3.60570580 | 4.62840579 |
| 116 | 4.45000 | 0.004178985 | −0.62610242 | 68.728752 | 7.20858088 | 0.47696066 | 3.60578888 | 4.64121971 |
| 117 | 4.46250 | 0.000343791 | −0.09161735 | 19.525674 | 7.21454289 | 0.47696052 | 3.60580273 | 4.65403205 |
| 118 | 4.47500 | 0.000002321 | −0.00139249 | 0.723823 | 7.22050489 | 0.47696051 | 3.60580338 | 4.66684281 |
| 119 | 4.48750 | 0.000000000 | 0.00000000 | 0.000004 | 7.22646690 | 0.47696051 | 3.60580338 | 4.67965200 |
| 120 | 4.50000 | 0.000000000 | 0.00000000 | 0.000000 | 7.23242891 | 0.47696051 | 3.60580338 | 4.69245962 |

#### The slice Σ_τ0 over the shell {#sec:table-sigma0}

Row k is the point of Σ_τ0 on the ingoing ray v = v_k: R0_k := v̂_k + 0.68 (seven decimals), a_k := (3/2) 𝒜_k w_k² with
w_k := (1 − μ_k/R_k²)/(3P_k) (six decimals), and N_k := −2μ_k ρ⁻³ − μ_k² ρ⁻⁵ + (1/2) a ρ⁻² (eight decimals), from the
shell table, where ρ := v̂_k + 0.68 and a := (3/2) 𝒜_k w_k² are taken before rounding. By the proof of
[[thm:margins-hyperbolic]] the true value of N_κ at the point is within 5 × 10⁻⁶ of N_k. On the cell v ∈ [v_k, v_(k+1)],
M_k (rounded up to two decimals) is the bound of [[lem:margins-curvature]] (a) for the second v-derivative of N_κ along
Σ_τ0, built from S_0, S_1 and S_2 := sup|𝒜″|, for which the printed column S2_k (rounded up to one decimal) is used. By
the monotone pieces of [[lem:margins-bump]], S_0 and S_1 are the larger end values of 𝒜 and |𝒜′| on the cell, taken from
the shell table with 5 × 10⁻¹⁰ and 5 × 10⁻⁹ added for its rounding, except that S_1 = 4.8 × 2.17036 on the cells k = 14
and 105, which contain v = 3.75 ∓ 0.75 × 3^(−1/4); and S_2 is the larger end value of |𝒜″|, except on the cells k = 6,
23, 96 and 113, which contain a zero of β‴ in the variable y = (4v − 15)/3, where the extremal value of
[[lem:margins-bump]] (c) times 6.4 is used. The sign column is − when max(N_k, N_(k+1)) + 5 × 10⁻⁶ + M_k/51200 < 0, +
when min(N_k, N_(k+1)) − 5 × 10⁻⁶ − M_k/51200 > 0, and 0 otherwise. The bound column prints that maximum (rounded up) or
minimum (rounded down). The three cells marked 0 are treated in the proof of [[thm:margins-hyperbolic]].

| k | R0_k | a_k | N_k | S2_k | M_k | sign | bound |
|---|---|---|---|---|---|---|---|
| 0 | 3.8253316 | 0.000000 | −0.05634060 | 0.1 | 0.18 | − | −0.055744 |
| 1 | 3.8382912 | 0.000000 | −0.05575350 | 0.8 | 0.19 | − | −0.055165 |
| 2 | 3.8512500 | 0.000001 | −0.05517458 | 19.6 | 0.65 | − | −0.054579 |
| 3 | 3.8642078 | 0.000213 | −0.05459672 | 68.8 | 1.86 | − | −0.053913 |
| 4 | 3.8771648 | 0.002593 | −0.05395527 | 114.2 | 3.02 | − | −0.053042 |
| 5 | 3.8901208 | 0.011597 | −0.05310635 | 133.9 | 3.59 | − | −0.051844 |
| 6 | 3.9030759 | 0.031457 | −0.05191945 | 135.0 | 3.72 | − | −0.050265 |
| 7 | 3.9160301 | 0.064117 | −0.05034351 | 130.3 | 3.70 | − | −0.048323 |
| 8 | 3.9289834 | 0.109310 | −0.04840080 | 113.0 | 3.37 | − | −0.046084 |
| 9 | 3.9419359 | 0.165435 | −0.04615542 | 90.5 | 2.89 | − | −0.043624 |
| 10 | 3.9548874 | 0.230349 | −0.04368620 | 67.6 | 2.40 | − | −0.041018 |
| 11 | 3.9678380 | 0.301859 | −0.04107046 | 47.0 | 1.94 | − | −0.038333 |
| 12 | 3.9807878 | 0.377972 | −0.03837623 | 29.5 | 1.54 | − | −0.035624 |
| 13 | 3.9937366 | 0.456994 | −0.03565964 | 15.3 | 1.22 | − | −0.032936 |
| 14 | 4.0066846 | 0.537538 | −0.03296508 | 5.0 | 0.98 | − | −0.030302 |
| 15 | 4.0196316 | 0.618501 | −0.03032645 | 11.6 | 1.15 | − | −0.027741 |
| 16 | 4.0325778 | 0.699028 | −0.02776880 | 16.6 | 1.27 | − | −0.025280 |
| 17 | 4.0455230 | 0.778464 | −0.02531002 | 20.3 | 1.36 | − | −0.022930 |
| 18 | 4.0584674 | 0.856322 | −0.02296232 | 22.9 | 1.42 | − | −0.020700 |
| 19 | 4.0714109 | 0.932243 | −0.02073345 | 24.6 | 1.45 | − | −0.018594 |
| 20 | 4.0843534 | 1.005974 | −0.01862778 | 25.8 | 1.47 | − | −0.016613 |
| 21 | 4.0972950 | 1.077342 | −0.01664704 | 26.4 | 1.48 | − | −0.014757 |
| 22 | 4.1102357 | 1.146234 | −0.01479105 | 26.6 | 1.47 | − | −0.013024 |
| 23 | 4.1231755 | 1.212589 | −0.01305815 | 26.8 | 1.46 | − | −0.011412 |
| 24 | 4.1361144 | 1.276381 | −0.01144568 | 26.6 | 1.45 | − | −0.009916 |
| 25 | 4.1490523 | 1.337610 | −0.00995022 | 26.4 | 1.43 | − | −0.008534 |
| 26 | 4.1619893 | 1.396299 | −0.00856784 | 26.0 | 1.41 | − | −0.007261 |
| 27 | 4.1749253 | 1.452485 | −0.00729430 | 25.5 | 1.38 | − | −0.006093 |
| 28 | 4.1878604 | 1.506217 | −0.00612516 | 24.9 | 1.36 | − | −0.005024 |
| 29 | 4.2007945 | 1.557549 | −0.00505592 | 24.3 | 1.33 | − | −0.004051 |
| 30 | 4.2137276 | 1.606543 | −0.00408207 | 23.6 | 1.30 | − | −0.003168 |
| 31 | 4.2266597 | 1.653262 | −0.00319912 | 22.9 | 1.27 | − | −0.002372 |
| 32 | 4.2395909 | 1.697770 | −0.00240272 | 22.2 | 1.25 | − | −0.001659 |
| 33 | 4.2525210 | 1.740134 | −0.00168861 | 21.6 | 1.22 | − | −0.001023 |
| 34 | 4.2654502 | 1.780417 | −0.00105271 | 20.9 | 1.19 | − | −0.000462 |
| 35 | 4.2783783 | 1.818682 | −0.00049105 | 20.3 | 1.17 | 0 | · |
| 36 | 4.2913054 | 1.854992 | 0.00000012 | 19.7 | 1.14 | 0 | · |
| 37 | 4.3042314 | 1.889404 | 0.00042441 | 19.1 | 1.12 | + | 0.000397 |
| 38 | 4.3171564 | 1.921976 | 0.00078526 | 18.5 | 1.09 | + | 0.000758 |
| 39 | 4.3300804 | 1.952763 | 0.00108592 | 18.0 | 1.07 | + | 0.001060 |
| 40 | 4.3430032 | 1.981815 | 0.00132949 | 17.5 | 1.05 | + | 0.001303 |
| 41 | 4.3559250 | 2.009181 | 0.00151889 | 17.0 | 1.03 | + | 0.001493 |
| 42 | 4.3688457 | 2.034907 | 0.00165689 | 16.5 | 1.01 | + | 0.001632 |
| 43 | 4.3817653 | 2.059037 | 0.00174612 | 16.1 | 0.99 | + | 0.001721 |
| 44 | 4.3946837 | 2.081610 | 0.00178903 | 15.7 | 0.97 | + | 0.001764 |
| 45 | 4.4076011 | 2.102664 | 0.00178795 | 15.4 | 0.96 | + | 0.001721 |
| 46 | 4.4205173 | 2.122234 | 0.00174508 | 15.0 | 0.94 | + | 0.001639 |
| 47 | 4.4334324 | 2.140353 | 0.00166247 | 14.7 | 0.92 | + | 0.001519 |
| 48 | 4.4463463 | 2.157049 | 0.00154207 | 14.4 | 0.90 | + | 0.001363 |
| 49 | 4.4592590 | 2.172351 | 0.00138568 | 14.2 | 0.89 | + | 0.001172 |
| 50 | 4.4721705 | 2.186283 | 0.00119503 | 13.9 | 0.88 | + | 0.000949 |
| 51 | 4.4850809 | 2.198867 | 0.00097170 | 13.7 | 0.86 | + | 0.000695 |
| 52 | 4.4979900 | 2.210123 | 0.00071719 | 13.5 | 0.85 | + | 0.000411 |
| 53 | 4.5108979 | 2.220069 | 0.00043291 | 13.4 | 0.84 | + | 0.000098 |
| 54 | 4.5238047 | 2.228720 | 0.00012015 | 13.2 | 0.82 | 0 | · |
| 55 | 4.5367101 | 2.236089 | −0.00021986 | 13.1 | 0.81 | − | −0.000199 |
| 56 | 4.5496143 | 2.242187 | −0.00058599 | 13.0 | 0.80 | − | −0.000565 |
| 57 | 4.5625173 | 2.247024 | −0.00097721 | 12.9 | 0.79 | − | −0.000956 |
| 58 | 4.5754189 | 2.250604 | −0.00139252 | 12.9 | 0.78 | − | −0.001372 |
| 59 | 4.5883193 | 2.252934 | −0.00183104 | 12.9 | 0.77 | − | −0.001811 |
| 60 | 4.6012184 | 2.254015 | −0.00229195 | 12.9 | 0.77 | − | −0.002271 |
| 61 | 4.6141162 | 2.253848 | −0.00277448 | 12.9 | 0.78 | − | −0.002754 |
| 62 | 4.6270127 | 2.252430 | −0.00327796 | 12.9 | 0.79 | − | −0.003257 |
| 63 | 4.6399078 | 2.249759 | −0.00380175 | 13.0 | 0.80 | − | −0.003781 |
| 64 | 4.6528016 | 2.245827 | −0.00434529 | 13.1 | 0.81 | − | −0.004324 |
| 65 | 4.6656941 | 2.240627 | −0.00490810 | 13.2 | 0.82 | − | −0.004887 |
| 66 | 4.6785851 | 2.234148 | −0.00548972 | 13.4 | 0.84 | − | −0.005468 |
| 67 | 4.6914748 | 2.226377 | −0.00608977 | 13.5 | 0.85 | − | −0.006068 |
| 68 | 4.7043632 | 2.217301 | −0.00670793 | 13.7 | 0.86 | − | −0.006686 |
| 69 | 4.7172501 | 2.206902 | −0.00734392 | 13.9 | 0.88 | − | −0.007321 |
| 70 | 4.7301356 | 2.195160 | −0.00799753 | 14.2 | 0.89 | − | −0.007975 |
| 71 | 4.7430197 | 2.182053 | −0.00866860 | 14.4 | 0.90 | − | −0.008646 |
| 72 | 4.7559024 | 2.167559 | −0.00935700 | 14.7 | 0.92 | − | −0.009334 |
| 73 | 4.7687837 | 2.151650 | −0.01006268 | 15.0 | 0.94 | − | −0.010039 |
| 74 | 4.7816635 | 2.134297 | −0.01078563 | 15.4 | 0.96 | − | −0.010761 |
| 75 | 4.7945418 | 2.115469 | −0.01152590 | 15.7 | 0.97 | − | −0.011501 |
| 76 | 4.8074187 | 2.095131 | −0.01228356 | 16.1 | 0.99 | − | −0.012259 |
| 77 | 4.8202941 | 2.073246 | −0.01305877 | 16.5 | 1.01 | − | −0.013034 |
| 78 | 4.8331681 | 2.049775 | −0.01385170 | 17.0 | 1.03 | − | −0.013826 |
| 79 | 4.8460405 | 2.024675 | −0.01466260 | 17.5 | 1.05 | − | −0.014637 |
| 80 | 4.8589115 | 1.997900 | −0.01549175 | 18.0 | 1.07 | − | −0.015465 |
| 81 | 4.8717809 | 1.969403 | −0.01633947 | 18.5 | 1.09 | − | −0.016313 |
| 82 | 4.8846489 | 1.939132 | −0.01720613 | 19.1 | 1.12 | − | −0.017179 |
| 83 | 4.8975153 | 1.907032 | −0.01809215 | 19.7 | 1.14 | − | −0.018064 |
| 84 | 4.9103801 | 1.873048 | −0.01899799 | 20.3 | 1.17 | − | −0.018970 |
| 85 | 4.9232435 | 1.837120 | −0.01992412 | 20.9 | 1.19 | − | −0.019895 |
| 86 | 4.9361053 | 1.799184 | −0.02087106 | 21.6 | 1.22 | − | −0.020842 |
| 87 | 4.9489655 | 1.759178 | −0.02183936 | 22.2 | 1.25 | − | −0.021809 |
| 88 | 4.9618242 | 1.717035 | −0.02282956 | 22.9 | 1.27 | − | −0.022799 |
| 89 | 4.9746813 | 1.672687 | −0.02384224 | 23.6 | 1.30 | − | −0.023811 |
| 90 | 4.9875369 | 1.626066 | −0.02487794 | 24.3 | 1.33 | − | −0.024846 |
| 91 | 5.0003909 | 1.577102 | −0.02593718 | 24.9 | 1.36 | − | −0.025905 |
| 92 | 5.0132433 | 1.525730 | −0.02702044 | 25.5 | 1.38 | − | −0.026988 |
| 93 | 5.0260941 | 1.471885 | −0.02812813 | 26.0 | 1.41 | − | −0.028095 |
| 94 | 5.0389433 | 1.415508 | −0.02926052 | 26.4 | 1.43 | − | −0.029227 |
| 95 | 5.0517909 | 1.356547 | −0.03041773 | 26.6 | 1.45 | − | −0.030384 |
| 96 | 5.0646369 | 1.294962 | −0.03159966 | 26.8 | 1.46 | − | −0.031566 |
| 97 | 5.0774814 | 1.230727 | −0.03280592 | 26.6 | 1.47 | − | −0.032772 |
| 98 | 5.0903242 | 1.163837 | −0.03403571 | 26.4 | 1.48 | − | −0.034001 |
| 99 | 5.1031654 | 1.094317 | −0.03528772 | 25.8 | 1.47 | − | −0.035254 |
| 100 | 5.1160050 | 1.022226 | −0.03655996 | 24.6 | 1.45 | − | −0.036526 |
| 101 | 5.1288430 | 0.947675 | −0.03784960 | 22.9 | 1.42 | − | −0.037816 |
| 102 | 5.1416794 | 0.870838 | −0.03915265 | 20.3 | 1.36 | − | −0.039121 |
| 103 | 5.1545141 | 0.791970 | −0.04046375 | 16.6 | 1.27 | − | −0.040433 |
| 104 | 5.1673473 | 0.711434 | −0.04177569 | 11.6 | 1.15 | − | −0.041748 |
| 105 | 5.1801788 | 0.629723 | −0.04307903 | 5.0 | 0.98 | − | −0.043054 |
| 106 | 5.1930088 | 0.547504 | −0.04436149 | 15.3 | 1.22 | − | −0.044332 |
| 107 | 5.2058371 | 0.465649 | −0.04560738 | 29.5 | 1.54 | − | −0.045572 |
| 108 | 5.2186638 | 0.385280 | −0.04679688 | 47.0 | 1.94 | − | −0.046753 |
| 109 | 5.2314889 | 0.307815 | −0.04790551 | 67.6 | 2.40 | − | −0.047853 |
| 110 | 5.2443124 | 0.234985 | −0.04890378 | 90.5 | 2.89 | − | −0.048842 |
| 111 | 5.2571342 | 0.168831 | −0.04975765 | 113.0 | 3.37 | − | −0.049686 |
| 112 | 5.2699545 | 0.111597 | −0.05043040 | 130.3 | 3.70 | − | −0.050353 |
| 113 | 5.2827732 | 0.065483 | −0.05088732 | 135.0 | 3.72 | − | −0.050809 |
| 114 | 5.2955903 | 0.032140 | −0.05110454 | 133.9 | 3.59 | − | −0.051007 |
| 115 | 5.3084058 | 0.011854 | −0.05108298 | 114.2 | 3.02 | − | −0.050799 |
| 116 | 5.3212197 | 0.002651 | −0.05086333 | 68.8 | 1.86 | − | −0.050484 |
| 117 | 5.3340320 | 0.000218 | −0.05052603 | 19.6 | 0.65 | − | −0.050135 |
| 118 | 5.3468428 | 0.000001 | −0.05015321 | 0.8 | 0.19 | − | −0.049771 |
| 119 | 5.3596520 | 0.000000 | −0.04978040 | 0.1 | 0.18 | − | −0.049402 |
| 120 | 5.3724596 | 0.000000 | −0.04941133 |  |  |  |  |

#### The bent slice over the shell {#sec:table-sigma-bent}

Row k is the point of Σ′ = {v̂ − R − φ(R) = τ0} on the ingoing ray v = v_k. Its radius R′_k (seven decimals)
satisfies |R′_k + φ_k − R0_k| ≤ 10⁻⁷. The numbers φ_k, φ′_k and φ″_k are the bend of [[prop:margins-bend]] and its
derivatives at R′_k, rounded to seven, six and seven decimals ([[lem:margins-bump-table]] (c) reproduces φ_k and φ′_k
from the bump table to within 10⁻⁶ and 1.7 × 10⁻⁶). Ξ_k (seven decimals) is the numerator [[eq:margins-xi]] at the
printed radius R = R′_k, with μ = μ_k and with μ̇ = (3/2) 𝒜_k w_k², V′ = 1 + φ′(R′_k) and V″ = φ″(R′_k) taken before
rounding. On the cell v ∈ [v_k, v_(k+1)], Φ4_k (rounded up to three decimals) is an upper bound for the supremum of |φ⁗|
over R ∈ [R′_k − 5.3 × 10⁻⁶, R′_(k+1) + 5.3 × 10⁻⁶], an interval that contains the true radii of the cell's points of
Σ′; it is found from the monotone pieces of β″ ([[lem:margins-bump]] (c)) in the variable of each lobe that meets the
interval, with the extremal values of [[lem:margins-bump]] (c) at interior extremal points. M′_k (rounded up to two
decimals) is the bound of [[lem:margins-curvature]] (b), built from the printed Φ4_k and S2_k and from S_0 and S_1 as in
[[sec:table-sigma0]]. And c_k (rounded down to five decimals) is the lower bound for c := 3(1 − fV)/(R V²(2 − fV)²) on
the cell of the proof of [[thm:margins-hyperbolic]], with R ∈ [R′_k − 5.3 × 10⁻⁶, R′_(k+1) + 5.3 × 10⁻⁶], μ ∈ [μ_k −
10⁻⁵, μ_(k+1) + 10⁻⁵] and V in the interval given there. The bound column (rounded up to seven decimals) is −c_k
(min(Ξ_k, Ξ_(k+1)) − 5 × 10⁻⁶ − M′_k/51200), an upper bound for κ′K′^l_l on the cell.

| k | R′_k | φ_k | φ′_k | φ″_k | Ξ_k | Φ4_k | M′_k | c_k | bound |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 3.8254920 | −0.0001604 | −0.001390 | −0.0062174 | 0.0499927 | 0.199 | 0.48 | 0.06612 | −0.0032740 |
| 1 | 3.8384702 | −0.0001789 | −0.001470 | −0.0060859 | 0.0495307 | 0.213 | 0.51 | 0.06559 | −0.0032201 |
| 2 | 3.8514485 | −0.0001985 | −0.001548 | −0.0059209 | 0.0491107 | 0.229 | 0.99 | 0.06506 | −0.0031686 |
| 3 | 3.8644269 | −0.0002191 | −0.001623 | −0.0057201 | 0.0487278 | 0.249 | 2.23 | 0.06454 | −0.0031154 |
| 4 | 3.8774054 | −0.0002406 | −0.001696 | −0.0054808 | 0.0483206 | 0.271 | 3.41 | 0.06403 | −0.0030528 |
| 5 | 3.8903839 | −0.0002631 | −0.001765 | −0.0051996 | 0.0477494 | 0.296 | 4.02 | 0.06352 | −0.0029730 |
| 6 | 3.9033623 | −0.0002864 | −0.001831 | −0.0048728 | 0.0468883 | 0.321 | 4.18 | 0.06301 | −0.0028735 |
| 7 | 3.9163407 | −0.0003106 | −0.001892 | −0.0044963 | 0.0456909 | 0.343 | 4.19 | 0.06253 | −0.0027573 |
| 8 | 3.9293190 | −0.0003355 | −0.001947 | −0.0040658 | 0.0441839 | 0.355 | 3.87 | 0.06206 | −0.0026285 |
| 9 | 3.9422970 | −0.0003611 | −0.001997 | −0.0035776 | 0.0424348 | 0.356 | 3.40 | 0.06161 | −0.0024922 |
| 10 | 3.9552747 | −0.0003873 | −0.002040 | −0.0030303 | 0.0405236 | 0.338 | 2.89 | 0.06119 | −0.0023535 |
| 11 | 3.9682520 | −0.0004140 | −0.002075 | −0.0024269 | 0.0385240 | 0.263 | 2.34 | 0.06079 | −0.0022151 |
| 12 | 3.9812289 | −0.0004411 | −0.002103 | −0.0017809 | 0.0364900 | 0.357 | 2.06 | 0.06043 | −0.0020786 |
| 13 | 3.9942052 | −0.0004686 | −0.002121 | −0.0011271 | 0.0344426 | 1.098 | 2.63 | 0.06010 | −0.0019410 |
| 14 | 4.0071807 | −0.0004962 | −0.002132 | −0.0005379 | 0.0323530 | 1.788 | 3.23 | 0.05980 | −0.0017979 |
| 15 | 4.0201555 | −0.0005239 | −0.002136 | −0.0001341 | 0.0301342 | 1.796 | 3.41 | 0.05953 | −0.0016460 |
| 16 | 4.0331294 | −0.0005516 | −0.002137 | −0.0000039 | 0.0277225 | 0.687 | 2.19 | 0.05929 | −0.0014961 |
| 17 | 4.0461023 | −0.0005793 | −0.002137 | 0.0000000 | 0.0252828 | 0.001 | 1.45 | 0.05908 | −0.0013539 |
| 18 | 4.0590744 | −0.0006070 | −0.002137 | 0.0000000 | 0.0229498 | 0.000 | 1.50 | 0.05891 | −0.0012194 |
| 19 | 4.0720456 | −0.0006347 | −0.002137 | 0.0000000 | 0.0207349 | 0.000 | 1.54 | 0.05876 | −0.0010933 |
| 20 | 4.0850158 | −0.0006624 | −0.002137 | 0.0000000 | 0.0186426 | 0.000 | 1.56 | 0.05865 | −0.0009758 |
| 21 | 4.0979852 | −0.0006902 | −0.002137 | 0.0000000 | 0.0166745 | 0.032 | 1.60 | 0.05856 | −0.0008663 |
| 22 | 4.1109536 | −0.0007179 | −0.002137 | 0.0000000 | 0.0148304 | 1.846 | 3.79 | 0.05850 | −0.0007645 |
| 23 | 4.1239211 | −0.0007456 | −0.002137 | 0.0000396 | 0.0131483 | 2.344 | 4.38 | 0.05845 | −0.0006881 |
| 24 | 4.1368877 | −0.0007733 | −0.002135 | 0.0003569 | 0.0118636 | 2.167 | 4.15 | 0.05843 | −0.0006401 |
| 25 | 4.1498532 | −0.0008009 | −0.002126 | 0.0010213 | 0.0110419 | 1.186 | 2.95 | 0.05842 | −0.0006117 |
| 26 | 4.1628176 | −0.0008284 | −0.002107 | 0.0018879 | 0.0105344 | 0.366 | 1.93 | 0.05842 | −0.0005934 |
| 27 | 4.1757808 | −0.0008555 | −0.002077 | 0.0028209 | 0.0102007 | 0.338 | 1.87 | 0.05843 | −0.0005792 |
| 28 | 4.1887425 | −0.0008821 | −0.002034 | 0.0037393 | 0.0099555 | 0.435 | 1.96 | 0.05845 | −0.0005675 |
| 29 | 4.2017026 | −0.0009082 | −0.001980 | 0.0046028 | 0.0097536 | 0.462 | 1.97 | 0.05848 | −0.0005573 |
| 30 | 4.2146610 | −0.0009334 | −0.001915 | 0.0053942 | 0.0095736 | 0.465 | 1.95 | 0.05852 | −0.0005479 |
| 31 | 4.2276175 | −0.0009578 | −0.001841 | 0.0061084 | 0.0094057 | 0.454 | 1.90 | 0.05857 | −0.0005391 |
| 32 | 4.2405719 | −0.0009811 | −0.001757 | 0.0067465 | 0.0092470 | 0.431 | 1.85 | 0.05862 | −0.0005308 |
| 33 | 4.2535243 | −0.0010032 | −0.001666 | 0.0073124 | 0.0090970 | 0.401 | 1.78 | 0.05868 | −0.0005232 |
| 34 | 4.2664744 | −0.0010242 | −0.001568 | 0.0078111 | 0.0089567 | 0.371 | 1.72 | 0.05874 | −0.0005162 |
| 35 | 4.2794221 | −0.0010438 | −0.001464 | 0.0082475 | 0.0088273 | 0.342 | 1.66 | 0.05881 | −0.0005100 |
| 36 | 4.2923674 | −0.0010621 | −0.001355 | 0.0086266 | 0.0087099 | 0.317 | 1.60 | 0.05888 | −0.0005045 |
| 37 | 4.3053103 | −0.0010789 | −0.001241 | 0.0089525 | 0.0086053 | 0.294 | 1.55 | 0.05896 | −0.0004999 |
| 38 | 4.3182506 | −0.0010942 | −0.001123 | 0.0092292 | 0.0085140 | 0.275 | 1.50 | 0.05903 | −0.0004959 |
| 39 | 4.3311883 | −0.0011079 | −0.001002 | 0.0094598 | 0.0084360 | 0.259 | 1.46 | 0.05912 | −0.0004929 |
| 40 | 4.3441233 | −0.0011201 | −0.000879 | 0.0096470 | 0.0083712 | 0.247 | 1.43 | 0.05920 | −0.0004905 |
| 41 | 4.3570557 | −0.0011307 | −0.000753 | 0.0097930 | 0.0083187 | 0.237 | 1.39 | 0.05929 | −0.0004888 |
| 42 | 4.3699853 | −0.0011396 | −0.000626 | 0.0098994 | 0.0082776 | 0.229 | 1.36 | 0.05938 | −0.0004878 |
| 43 | 4.3829121 | −0.0011468 | −0.000497 | 0.0099675 | 0.0082466 | 0.225 | 1.34 | 0.05947 | −0.0004872 |
| 44 | 4.3958362 | −0.0011524 | −0.000368 | 0.0099981 | 0.0082242 | 0.223 | 1.32 | 0.05956 | −0.0004870 |
| 45 | 4.4087574 | −0.0011563 | −0.000239 | 0.0099915 | 0.0082084 | 0.226 | 1.30 | 0.05965 | −0.0004871 |
| 46 | 4.4216759 | −0.0011586 | −0.000110 | 0.0099477 | 0.0081971 | 0.232 | 1.29 | 0.05975 | −0.0004874 |
| 47 | 4.4345915 | −0.0011592 | 0.000018 | 0.0098662 | 0.0081879 | 0.240 | 1.29 | 0.05984 | −0.0004875 |
| 48 | 4.4475044 | −0.0011581 | 0.000145 | 0.0097461 | 0.0081780 | 0.251 | 1.28 | 0.05993 | −0.0004874 |
| 49 | 4.4604144 | −0.0011555 | 0.000269 | 0.0095861 | 0.0081644 | 0.264 | 1.28 | 0.06003 | −0.0004870 |
| 50 | 4.4733217 | −0.0011512 | 0.000392 | 0.0093845 | 0.0081437 | 0.281 | 1.29 | 0.06012 | −0.0004858 |
| 51 | 4.4862262 | −0.0011454 | 0.000511 | 0.0091389 | 0.0081120 | 0.302 | 1.30 | 0.06021 | −0.0004837 |
| 52 | 4.4991280 | −0.0011380 | 0.000628 | 0.0088465 | 0.0080652 | 0.325 | 1.31 | 0.06030 | −0.0004804 |
| 53 | 4.5120271 | −0.0011292 | 0.000739 | 0.0085041 | 0.0079986 | 0.352 | 1.34 | 0.06040 | −0.0004757 |
| 54 | 4.5249236 | −0.0011189 | 0.000847 | 0.0081077 | 0.0079071 | 0.381 | 1.36 | 0.06049 | −0.0004690 |
| 55 | 4.5378175 | −0.0011074 | 0.000948 | 0.0076530 | 0.0077851 | 0.411 | 1.38 | 0.06058 | −0.0004601 |
| 56 | 4.5507088 | −0.0010945 | 0.001044 | 0.0071351 | 0.0076269 | 0.439 | 1.40 | 0.06067 | −0.0004486 |
| 57 | 4.5635978 | −0.0010805 | 0.001132 | 0.0065492 | 0.0074265 | 0.459 | 1.42 | 0.06077 | −0.0004342 |
| 58 | 4.5764843 | −0.0010654 | 0.001212 | 0.0058906 | 0.0071784 | 0.465 | 1.41 | 0.06086 | −0.0004166 |
| 59 | 4.5893686 | −0.0010493 | 0.001283 | 0.0051563 | 0.0068787 | 0.459 | 1.40 | 0.06095 | −0.0003958 |
| 60 | 4.6022508 | −0.0010324 | 0.001345 | 0.0043466 | 0.0065270 | 0.415 | 1.34 | 0.06104 | −0.0003722 |
| 61 | 4.6151309 | −0.0010147 | 0.001395 | 0.0034694 | 0.0061304 | 0.287 | 1.20 | 0.06114 | −0.0003474 |
| 62 | 4.6280091 | −0.0009965 | 0.001434 | 0.0025470 | 0.0057106 | 0.562 | 1.54 | 0.06123 | −0.0003233 |
| 63 | 4.6408856 | −0.0009778 | 0.001461 | 0.0016287 | 0.0053163 | 1.471 | 2.65 | 0.06133 | −0.0003056 |
| 64 | 4.6537605 | −0.0009589 | 0.001476 | 0.0008087 | 0.0050410 | 2.317 | 3.69 | 0.06142 | −0.0003041 |
| 65 | 4.6666339 | −0.0009398 | 0.001483 | 0.0002328 | 0.0050297 | 2.344 | 3.73 | 0.06151 | −0.0003045 |
| 66 | 4.6795059 | −0.0009207 | 0.001484 | 0.0000139 | 0.0053947 | 1.286 | 2.47 | 0.06159 | −0.0003289 |
| 67 | 4.6923765 | −0.0009016 | 0.001484 | 0.0000000 | 0.0059834 | 0.001 | 0.92 | 0.06167 | −0.0003675 |
| 68 | 4.7052457 | −0.0008826 | 0.001484 | 0.0000000 | 0.0066041 | 0.000 | 0.94 | 0.06174 | −0.0004062 |
| 69 | 4.7181135 | −0.0008635 | 0.001484 | 0.0000000 | 0.0072428 | 0.000 | 0.95 | 0.06181 | −0.0004462 |
| 70 | 4.7309800 | −0.0008444 | 0.001484 | 0.0000000 | 0.0078992 | 0.000 | 0.97 | 0.06187 | −0.0004872 |
| 71 | 4.7438450 | −0.0008253 | 0.001484 | 0.0000000 | 0.0085731 | 0.000 | 0.98 | 0.06192 | −0.0005293 |
| 72 | 4.7567086 | −0.0008062 | 0.001484 | 0.0000000 | 0.0092645 | 0.000 | 1.00 | 0.06196 | −0.0005725 |
| 73 | 4.7695708 | −0.0007871 | 0.001484 | 0.0000000 | 0.0099733 | 0.000 | 1.01 | 0.06200 | −0.0006168 |
| 74 | 4.7824315 | −0.0007680 | 0.001484 | 0.0000000 | 0.0106994 | 0.000 | 1.03 | 0.06203 | −0.0006621 |
| 75 | 4.7952908 | −0.0007489 | 0.001484 | 0.0000000 | 0.0114430 | 0.000 | 1.05 | 0.06206 | −0.0007085 |
| 76 | 4.8081486 | −0.0007299 | 0.001484 | 0.0000000 | 0.0122040 | 0.000 | 1.07 | 0.06208 | −0.0007560 |
| 77 | 4.8210049 | −0.0007108 | 0.001484 | 0.0000000 | 0.0129827 | 0.000 | 1.08 | 0.06209 | −0.0008044 |
| 78 | 4.8338598 | −0.0006917 | 0.001484 | 0.0000000 | 0.0137793 | 0.000 | 1.11 | 0.06209 | −0.0008539 |
| 79 | 4.8467132 | −0.0006726 | 0.001484 | 0.0000000 | 0.0145939 | 0.001 | 1.13 | 0.06208 | −0.0009043 |
| 80 | 4.8595650 | −0.0006536 | 0.001484 | 0.0000000 | 0.0154268 | 0.041 | 1.20 | 0.06207 | −0.0009557 |
| 81 | 4.8724154 | −0.0006345 | 0.001484 | −0.0000003 | 0.0162782 | 0.218 | 1.44 | 0.06205 | −0.0010080 |
| 82 | 4.8852643 | −0.0006154 | 0.001484 | −0.0000097 | 0.0171395 | 0.285 | 1.54 | 0.06202 | −0.0010608 |
| 83 | 4.8981116 | −0.0005964 | 0.001483 | −0.0000531 | 0.0179863 | 0.284 | 1.57 | 0.06199 | −0.0011127 |
| 84 | 4.9109575 | −0.0005773 | 0.001482 | −0.0001417 | 0.0188079 | 0.233 | 1.53 | 0.06194 | −0.0011628 |
| 85 | 4.9238018 | −0.0005583 | 0.001480 | −0.0002682 | 0.0196119 | 0.150 | 1.45 | 0.06189 | −0.0012117 |
| 86 | 4.9366446 | −0.0005393 | 0.001475 | −0.0004197 | 0.0204120 | 0.078 | 1.39 | 0.06183 | −0.0012600 |
| 87 | 4.9494859 | −0.0005204 | 0.001469 | −0.0005842 | 0.0212205 | 0.026 | 1.36 | 0.06177 | −0.0013088 |
| 88 | 4.9623258 | −0.0005016 | 0.001460 | −0.0007530 | 0.0220467 | 0.033 | 1.39 | 0.06169 | −0.0013580 |
| 89 | 4.9751642 | −0.0004829 | 0.001450 | −0.0009204 | 0.0228969 | 0.046 | 1.44 | 0.06161 | −0.0014086 |
| 90 | 4.9880013 | −0.0004644 | 0.001437 | −0.0010827 | 0.0237754 | 0.053 | 1.48 | 0.06152 | −0.0014605 |
| 91 | 5.0008369 | −0.0004460 | 0.001422 | −0.0012375 | 0.0246849 | 0.056 | 1.51 | 0.06142 | −0.0015140 |
| 92 | 5.0136712 | −0.0004279 | 0.001405 | −0.0013838 | 0.0256269 | 0.057 | 1.53 | 0.06131 | −0.0015690 |
| 93 | 5.0265041 | −0.0004100 | 0.001386 | −0.0015210 | 0.0266025 | 0.057 | 1.56 | 0.06119 | −0.0016256 |
| 94 | 5.0393356 | −0.0003923 | 0.001366 | −0.0016490 | 0.0276121 | 0.056 | 1.58 | 0.06106 | −0.0016838 |
| 95 | 5.0521659 | −0.0003749 | 0.001344 | −0.0017678 | 0.0286555 | 0.054 | 1.59 | 0.06093 | −0.0017437 |
| 96 | 5.0649948 | −0.0003579 | 0.001321 | −0.0018778 | 0.0297324 | 0.052 | 1.61 | 0.06078 | −0.0018049 |
| 97 | 5.0778224 | −0.0003411 | 0.001296 | −0.0019794 | 0.0308421 | 0.050 | 1.61 | 0.06063 | −0.0018677 |
| 98 | 5.0906488 | −0.0003246 | 0.001270 | −0.0020728 | 0.0319832 | 0.047 | 1.62 | 0.06046 | −0.0019314 |
| 99 | 5.1034739 | −0.0003085 | 0.001243 | −0.0021586 | 0.0331542 | 0.045 | 1.61 | 0.06028 | −0.0019963 |
| 100 | 5.1162978 | −0.0002927 | 0.001215 | −0.0022370 | 0.0343525 | 0.042 | 1.59 | 0.06010 | −0.0020624 |
| 101 | 5.1291204 | −0.0002774 | 0.001185 | −0.0023086 | 0.0355750 | 0.040 | 1.55 | 0.05990 | −0.0021288 |
| 102 | 5.1419417 | −0.0002623 | 0.001155 | −0.0023736 | 0.0368172 | 0.038 | 1.49 | 0.05969 | −0.0021955 |
| 103 | 5.1547619 | −0.0002477 | 0.001125 | −0.0024323 | 0.0380735 | 0.037 | 1.40 | 0.05947 | −0.0022623 |
| 104 | 5.1675808 | −0.0002335 | 0.001093 | −0.0024851 | 0.0393362 | 0.035 | 1.28 | 0.05923 | −0.0023281 |
| 105 | 5.1803985 | −0.0002197 | 0.001061 | −0.0025323 | 0.0405958 | 0.034 | 1.11 | 0.05899 | −0.0023931 |
| 106 | 5.1932151 | −0.0002063 | 0.001028 | −0.0025740 | 0.0418395 | 0.032 | 1.34 | 0.05873 | −0.0024554 |
| 107 | 5.2060304 | −0.0001934 | 0.000995 | −0.0026105 | 0.0430515 | 0.031 | 1.66 | 0.05847 | −0.0025150 |
| 108 | 5.2188446 | −0.0001808 | 0.000961 | −0.0026419 | 0.0442117 | 0.030 | 2.06 | 0.05819 | −0.0025700 |
| 109 | 5.2316576 | −0.0001687 | 0.000927 | −0.0026685 | 0.0452954 | 0.029 | 2.51 | 0.05790 | −0.0026194 |
| 110 | 5.2444694 | −0.0001571 | 0.000893 | −0.0026903 | 0.0462729 | 0.029 | 3.01 | 0.05760 | −0.0026616 |
| 111 | 5.2572801 | −0.0001459 | 0.000858 | −0.0027075 | 0.0471100 | 0.028 | 3.48 | 0.05729 | −0.0026947 |
| 112 | 5.2700896 | −0.0001351 | 0.000824 | −0.0027201 | 0.0477699 | 0.028 | 3.81 | 0.05698 | −0.0027174 |
| 113 | 5.2828980 | −0.0001248 | 0.000789 | −0.0027283 | 0.0482178 | 0.028 | 3.82 | 0.05666 | −0.0027275 |
| 114 | 5.2957052 | −0.0001149 | 0.000754 | −0.0027320 | 0.0484297 | 0.028 | 3.69 | 0.05633 | −0.0027224 |
| 115 | 5.3085112 | −0.0001055 | 0.000719 | −0.0027313 | 0.0484067 | 0.028 | 3.12 | 0.05600 | −0.0026949 |
| 116 | 5.3213162 | −0.0000965 | 0.000684 | −0.0027261 | 0.0481896 | 0.028 | 1.96 | 0.05568 | −0.0026623 |
| 117 | 5.3341200 | −0.0000879 | 0.000649 | −0.0027165 | 0.0478591 | 0.028 | 0.74 | 0.05535 | −0.0026279 |
| 118 | 5.3469227 | −0.0000799 | 0.000614 | −0.0027024 | 0.0474974 | 0.029 | 0.29 | 0.05503 | −0.0025935 |
| 119 | 5.3597242 | −0.0000722 | 0.000580 | −0.0026837 | 0.0471405 | 0.030 | 0.27 | 0.05470 | −0.0025589 |
| 120 | 5.3725246 | −0.0000650 | 0.000546 | −0.0026603 | 0.0467919 |  |  |  |  |
