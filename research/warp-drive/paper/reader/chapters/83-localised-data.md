## Localised data and the sign of the charge {#ch:localised-data}

This chapter asks which perturbations of the data of [[ch:two-dusts]] can be localised: equal to the background's data
outside a compact set, in angle or in angle and radius at once. Throughout, the background is the two-dust background
of [[sec:two-dust-background]] with the explicit characteristic data of [[sec:bg-data]], and data are taken on its
slice Σ_τ0, τ0 = −0.68, or on a slice bent from it.

Three answers are proved. On the null cones the constraints are ordinary differential equations along the generators,
and data localised in an angular band exist exactly ([[prop:loc-cones]], [[lem:loc-cone-in]]); when the band avoids the
axes they have a development in the double-null gauge on a neighbourhood of the two cones, with or without dust, equal
to the background outside a slightly wider band: without smallness, on a neighbourhood that depends on the data and
unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]), and, for data near the
background's, on an explicit neighbourhood and with an estimate ([[thm:loc-cone-development]]). On Σ_τ0 the
constraints split, after Rácz
[Rac16], into a hyperbolic system with the radius as time wherever κK^l_l < 0; this holds on all of Σ_τ0 except one band
inside the shell, where no foliation of Σ_τ0 is hyperbolic, and on a slice bent from Σ_τ0 by at most 0.0012 it holds
everywhere, so that data equal to the background's outside the domain of influence of a compact set away from the axes
exist on the whole slice, that domain spreading in angle at most linearly as the radius decreases
([[thm:loc-bent-slice]]). Localisation in angle and radius at once is decided, near the background's data and at second
order in the amplitude, by the sign of a charge Q: the pairing of the constraints with the static Killing field. On
every band of Σ_τ0 on which the background is vacuum the mass term of the charge identity is positive, and Q is negative
for every perturbation of the extrinsic curvature alone. For perturbations of the metric, on every such band, Q takes
both signs where the round spheres are trapped, f < 0, and where they are not, f > 0, it is negative for every
perturbation that is not a gauge perturbation ([[thm:charge-sign]]).

The inequalities on the background that these results use are proved at the end of the chapter, in
[[sec:bg-below]] and [[sec:margins]], from the tables of [[sec:tab-bg]] and [[sec:table-margins]].

### The setting {#sec:loc-setting}

*The background.* The background g0 is the solution of the two-null-dust equations [[eq:two-dust-limit]] with the
characteristic data of [[sec:bg-data]]: e^(2σ) = 1/2 on the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the ingoing
shell 𝒜(v) = 3.6 b(v; 3, 4.5) on 𝒞_out, the outgoing packet ℬ(u) = 1.7 b(u; 5.7, 7.2) on 𝒞_in, and at the corner
R = 5, R_u = −0.47, R_v = 1/2 and mass 3/2. In the chart (v̂, R) of [[eq:bg-chart]] it reads g0 = −q² f dv̂² + 2q
dv̂ dR + R² dΩ₃², q := e^ψ, f = 1 − μ/R². Region I is {u ≤ u1}, u1 = 5.7, where ψ = 0 and g0 is ingoing Vaidya
([[lem:margins-region-one]]); region III is {u ≥ u2}, u2 = 7.2, past the outgoing packet, where ψ = ψ_III(v̂) and
μ = μ3 ∈ [0.8220998, 0.8221253] ([[lem:bg-reduction]] (e), [[thm:bg-margins]] (a)).

*The background as two-dust data.* g0 is the background of [[def:two-dust-data]], written in the normalisation
e^(2σ) = 1/2 of the cones, which [[lem:two-dust-reparametrisation]] (b) allows; its advanced time is v̂. The parameters
are the seed mass μ0 := μ3, with μ0 + E₂ = 3/2 the mass before the packet; [v_start, v_end] := [v̂(v = 3), v̂(v = 4.5)],
the support of the shell in v̂; T := 1; l5 fixed by q0 := (√72 μ3 l5²)^(1/4) = 0.75; and δ0 := 0.05, so that the inner
radius of [[sec:domain]] is q0 − δ0 = 0.70 and τ0 := −0.68 = −0.70 + 0.02. The square roots of the profiles 𝒜 and ℬ,
rewritten as in [[lem:two-dust-reparametrisation]], are smooth, the bump being the exponential of a function that tends
to −∞ with all its derivatives at the ends of its support. The conditions of [[def:two-dust-data]] hold: μ0 ≥ √72 l5²,
that is μ3² ≥ q0⁴ = 0.3164…; v_start − τ0 > 3.1453 + 0.68 > √μ3 + 1 (proof of [[lem:bg-reduction]] (f)); 𝒞_in = {v̂ = 0}
with 0 < τ0 + 0.70; and on [u1, u2] the cone 𝒞_in is untrapped, R² > 1.5² > 3/2 ≥ μ ([[prop:bg-nprime]] and its
proof). The slice is Σ_τ0 := {v̂ − R = τ0} ∩ Ω₂ = {0.70 ≤ R ≤ b(τ0)} ([[lem:two-dust-domain]]), and b(τ0) > 12:
by [[eq:two-dust-omega]], b(τ0) = V + 1 + τ_end − 2τ0 with V = v_end + T ≥ 4.6924 + 1 ([[lem:margins-shell-data]] (c)
and the last row of [[sec:table-shell]]), and τ_end ≥ V − r_q^♭(V) ≥ V − r_q(3.6059) ≥ V − 1.0854: the point p of the
ray v̂ = V on the outer cone of [[lem:two-dust-domain]] lies in region I, where μ(p) ≤ 3.6059
([[lem:margins-region-one]] (a)), and in D_T, its radius exceeding 5 > r_q(μ(p)); and r_q(3.6059) = 0.75
(3.6059/μ3)^(1/4) ≤ 1.0854.

Region III meets Σ_τ0 in {0.70 ≤ R ≤ R_u2}, 1.8614372 ≤ R_u2 ≤ 1.8614410 ([[prop:bg-seed]] (a),
[[prop:bg-region-three-end]] (a)); there f < 0 exactly where R < √μ3, and √μ3 ∈ (0.9066, 0.9068). Its part {0.70 ≤ R ≤
1.861} is the *seed region*. The radius R_* ∈ [3.43718006, 3.43718007] of [[lem:bg-rstar]] is where the ray u = u1 meets
Σ_τ0; the points of Σ_τ0 with R ≥ R_* lie in region I ([[lem:margins-region-one]] (c)), and no point of Σ_τ0 with R_u2 <
R < R_* is a vacuum point of the background ([[prop:bg-region-three-end]] (d)). At every point of Σ_τ0, qf < 1: for R ≤
R_* by [[thm:bg-margins]] (c), and for R ≥ R_* because there q = 1 and f = 1 − μ/R² < 1 ([[lem:margins-region-one]] (a),
(c)). Σ_τ0 denotes this slice throughout the chapter.

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

On Σ_τ0 every point has qf < 1 ([[sec:loc-setting]]), so K^l_l < 0 there and Rácz's split
([[thm:std-racz-hyperbolic]]) is hyperbolic exactly where N_κ < 0. In region I, q = 1 and [[eq:racz-kappa]] reduces to
the formulas of [[lem:margins-racz]].

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
[[prop:margins-bend]] and Σ′ := {v̂ − R − φ(R) = τ0, 0.70 ≤ R ≤ b(τ0)}.

(a) Σ′ equals Σ_τ0 outside 3.5 ≤ R ≤ 5.75, lies to the past of Σ_τ0 where they differ, at τ-distance at most
0.0011596, and is spacelike. Rácz's split for its round spheres is hyperbolic at every point of Σ′: κ′K′^l_l < 0, with
κ′K′^l_l ≤ −2.96 × 10⁻⁴ for R_* ≤ R ≤ 5.75 and κ′K′^l_l ≤ −4.76 × 10⁻³ for R ≤ R_*.

(b) Let 0 < ϑ1 < π/4 and 0.70 < R1 < R2 ≤ b(τ0), and let 𝒫 be a compact subset of {R1 < R < R2, ϑ1 < ϑ <
π/2 − ϑ1}. Take invariant free data ([Rac16, (4.28)], quoted in [[thm:std-racz-hyperbolic]]) on Σ′ equal to the
background's outside 𝒫 and ε-close to them in C^∞, whose matter part e, p_i is that of null dust: of the background's
two families, with their phases and with densities ≥ 0, and of any number of further families, each with an invariant
phase that is an eikonal of the background, smooth with nonzero differential on a neighbourhood of the part of
Σ′ ∪ Σ_τ0 with R ≤ 6, and with a density ≥ 0 supported in 𝒫. Take (k_i, K^l_l) at R = R2 equal to the background's.
For ε small the system (4.16), (3.2) of [Rac16] has a unique solution on 0.70 ≤ R ≤ R2. The data it determines, extended
by the background's data for R ≥ R2, satisfy the constraints on Σ′, and equal the background's outside the domain of
influence, for that system, of 𝒫. There is c_* > 0, depending only on R2, such that this domain lies in the set of
points with R ≤ R_𝒫 and ϑ1 − c_*(R_𝒫 − R) ≤ ϑ ≤ π/2 − ϑ1 + c_*(R_𝒫 − R), R_𝒫 the largest value of R on 𝒫.

(c) The development of these data across the lens between Σ′ and Σ_τ0 exists, and the constraint data it induces on
Σ_τ0 are those of (b) for R ∉ (3.5, 5.75), where Σ_τ0 = Σ′. Let 0 ≤ α ≤ β ≤ π/2, with α < π/2 and β > 0, be such
that every point of the domain of influence of 𝒫 in (b) with 3.44 ≤ R ≤ 5.85 has α ≤ ϑ ≤ β. Then for ε small,
depending also on α and β, the data induced on Σ_τ0 equal the background's at the points with 3.5 < R < 5.75 and
ϑ < α − 3.3 × 10⁻⁴ or ϑ > β + 3.3 × 10⁻⁴: across the lens the angular support widens by at most 3.3 × 10⁻⁴ rad on
each side.

So data near the background's exist on all of Σ_τ0, the band of [[prop:loc-band]] included, that equal the
background's outside the domain of influence of a compact set 𝒫 away from the axes for R ∉ (3.5, 5.75), and outside a
range of ϑ for 3.5 < R < 5.75. By (b) that domain lies in R ≤ R_𝒫, with ϑ within c_*(R_𝒫 − R) of [ϑ1, π/2 − ϑ1] at
radius R. With d := c_* max(0, R_𝒫 − 3.44), (c) applies with α := max(0, ϑ1 − d) and β := min(π/2, π/2 − ϑ1 + d), so
that for 3.5 < R < 5.75 the data equal the background's where ϑ < α − 3.3 × 10⁻⁴ or ϑ > β + 3.3 × 10⁻⁴. For
perturbations whose radial support avoids [4.2882, 4.5310] the
construction of (b) works on Σ_τ0 itself. If R2 < 4.2882, integrate from R2 inward as in (b): the split is hyperbolic on
Σ_τ0 ∩ {R < 4.2882} ([[prop:loc-band]]). If R1 > 4.5310, take (k_i, K^l_l) equal to the background's at a radius
R_0 ∈ (4.5310, R1) and integrate outward, on R_0 ≤ R ≤ b(τ0), where the split is hyperbolic; with the parameter −R in
place of R the system keeps the form (4.19) of [Rac16] ([[rem:std-racz-characteristic]]), with −B^(K) and −C in place of
B^(K) and C and the same symmetrizer, and the leaves are again closed, so the proof of (b) applies, the constraints
holding in the domain of dependence of the sphere R = R_0, which is all of {R_0 ≤ R ≤ b(τ0)}; the data are extended by
the background's for R ≤ R_0. A support on both sides is treated by both constructions at once, inward from an
R2 < 4.2882 and outward from an R_0 > 4.5310, the data between 4.2882 and 4.5310 being the background's; the
constraints, being local, hold for the data so combined.

*Proof.* (a) The first two statements are [[cor:margins-lens]]. Σ′ is spacelike: below R = 3.5 it is Σ_τ0, spacelike
by [[lem:two-dust-domain]] (a); for R ≥ R_* it lies in region I ([[lem:margins-region-one]] (c)), where d(τ − φ) is
timelike (proof of [[cor:margins-lens]]). The margin for R_* ≤ R is [[thm:margins-hyperbolic]] (a), and for R ≤ R_*,
where Σ′ = Σ_τ0, it is [[thm:bg-margins]] (c).

(b) Write (4.16), (3.2) of [Rac16] as (4.19) there ([[rem:std-racz-characteristic]]): ∂_ρu + B^(K)∂_Ku + C = 0, with
u = (k_B, K^E_E), ρ := R, on [0.70, R2] × S³, each leaf {R = const} identified with the unit sphere S³ by the angles.
*A global frame.* On the unit sphere S³ of the quaternions ℍ, X_1(x) := xi, X_2(x) := xj and X_3(x) := xk (quaternion
products) form an orthonormal frame of the round metric ⟨·, ·⟩. We take the mixed part k by its components k(X_1),
k(X_2), k(X_3), and each tensor among the free data by its components in this frame, so that u is ℝ⁴-valued and the free
data with their derivatives in R and along the frame, of the orders that enter, form an ℝ^(n_P)-valued function P
(the q of [[cor:class-kato-sphere]]). With
𝔉(ω) := diag((⟨∂_K, X_a⟩)_(K,a), 1), so that k(∂_K) = Σ_a ⟨∂_K, X_a⟩ k(X_a), the frame components ũ have u = 𝔉ũ, and the
system becomes

    ∂_ρũ + 𝔉⁻¹B^(K)𝔉 ∂_Kũ + 𝔉⁻¹(B^(K)(∂_K𝔉)ũ + C) = 0:

B^(K)∂_K becomes the matrix of vector fields 𝔉⁻¹B^(K)𝔉 ∂_K, terms of order zero in ũ are added to C, and a symmetrizer H
becomes 𝔉ᵀH𝔉, positive definite where H is, with 𝔉ᵀH𝔉 𝔉⁻¹B^(K)𝔉 = 𝔉ᵀHB^(K)𝔉 symmetric. The equations and H being
tensorial on the leaves, these frame forms are the same in every chart of leaf coordinates, so they are smooth on all of
S³. An isometry of S³ carries the frame to an orthonormal frame, so it acts on the frame components by an orthogonal
matrix at each point. Below, u, B^(K), C and H denote the frame forms.

Where K^E_E ≠ 0, B^(K) and C are smooth functions of (ρ, ω, u) and of P, κ being given algebraically by [Rac16, (4.17)].
The background's data give a smooth solution ū, for the background's free data P̄, and κK^l_l < 0 along it by (a). The
common symmetrizer H that Rácz exhibits for [Rac16, Lemma 4.1] ([[thm:std-racz-hyperbolic]]), [Rac16, (4.21), p. 12], is
a rational function of k, K^E_E, κ and γ̂ with only κ in its denominators; so near the graph of (ū, P̄) it is a smooth
function of (ρ, ω, u, P), symmetric, positive definite at ū, where κK^E_E < 0 ([[thm:std-racz-hyperbolic]]), and HB^(K)
is symmetric. With t := R2 − ρ the system reads ∂_tu − B^(K)∂_Ku − C = 0, which is [[eq:class-kato-sphere]] with n = 3,
A^0 := H, A^(ab) := −HB^(K)⟨∂_K, W_ab⟩ and F := HC (the remark after [[cor:class-kato-sphere]]), on [0, R2 − 0.70]. We
multiply these coefficients by a smooth cut-off supported in a neighbourhood of the graph of (ū, P̄) on which H, B^(K)
and C are smooth and HB^(K) is symmetric, and equal to 1 on a smaller neighbourhood 𝒪 of the graph, and we add I times
one minus the cut-off to A^0; this makes them smooth and symmetric everywhere and leaves them unchanged on 𝒪. Fix
r0 ∈ (0, r̄] in [[cor:class-kato-sphere]] so small that the points (t, ω, u, π) with |u − ū(t, ω)| ≤ r0
and |π − P̄(t, ω)| ≤ r0 lie in 𝒪 and H is positive definite at them, take ε0 ≤ r0, and fix an integer s ≥ 4, so that
s > (n + 1)/2 + 1 = 3. For ε small, ‖P − P̄‖_(C^s) ≤ ε0, and [[cor:class-kato-sphere]] (a), (b), with the datum ū(0) at
t = 0, gives a smooth solution on the whole interval with sup_t ‖u − ū‖_(L²(S³)) ≤ C ‖P − P̄‖_(C⁰), sup_t
‖u‖_(H^s(S³)) ≤ C and sup |u − ū| ≤ C ‖P − P̄‖_(C⁰)^(1/(4s)); so sup |u − ū| → 0 as ε → 0, the solution stays in 𝒪 and
solves (4.19). A solution of the class of [[cor:class-kato-sphere]] (a) has its states in 𝒪, where the system is (4.19);
the isometries T² × Z2 × Z2 preserve (4.19), P, P̄, ū and the pointwise norm of u − ū, so they carry such solutions with
the invariant datum ū(0) to such solutions, and by the uniqueness there the solution is invariant. The leaves are
three-spheres, so the axes are interior points of the leaves and need no condition. By [[cor:class-kato-sphere]] (c),
u = ū on every set Ω as there on which P = P̄; outside 𝒫 the free data are the background's, and the complement of the
union of these sets is the domain of influence of 𝒫 for the system (4.19), the condition of
[[cor:class-kato-sphere]] (c) being imposed at states in 𝒪, where the coefficients are unchanged. By
[[thm:std-racz-hyperbolic]] the fields built from the solution and the free data satisfy the constraints in the domain
of dependence of the initial sphere, which here is all of {0.70 ≤ R ≤ R2}.

*The domain of influence in angle.* For ξ ∈ T*_ωS³ put B(ξ) := B^(K)ξ(∂_K). At the points (t, ω, u, P̄(t, ω))
with |u − ū(t, ω)| ≤ r0, H is positive definite and HB(ξ) is symmetric, so the eigenvalues of B(ξ) are real. These
points, with ξ of length 1 for the round metric, form a compact set; so there is c_* > 0, depending only on R2 (the
background being fixed, and r0 fixed above in terms of R2 alone), such that the eigenvalues of B(ξ) are at most c_*|ξ|
in modulus there. Since Σ_(a<b) ⟨∂_K, W_ab⟩
W_ab = ∂_K (the remark after [[cor:class-kato-sphere]]), a covector ν = c dt + ξ gives ν(∂_t)A^0 + Σ_(a<b)
ν(W_ab)A^(ab) = H(c − B(ξ)), and for c ≥ c_*|ξ| this matrix is positive semidefinite at these points: it is congruent,
by H^(−1/2), to the symmetric matrix H^(1/2)(c − B(ξ))H^(−1/2), whose eigenvalues are c minus those of B(ξ), hence ≥ 0.
Let R_𝒫 < R2 be the largest value of R on 𝒫, and take R′ ∈ (R_𝒫, R2), ϑ_c ∈ (0, ϑ1) and R_b ∈ [0.70, R′) with
ϑ_c > c_*(R′ − R_b). The set

    Ω_* := {R′ ≤ R ≤ R2} ∪ {R_b ≤ R ≤ R′, ϑ ≤ ϑ_c − c_*(R′ − R)}

does not meet 𝒫, so P = P̄ on it. Its part with R ≥ R3, for R_b ≤ R3 ≤ R2, is {R ≥ max(R3, R′ − max(0, ϑ_c − ϑ)/c_*)},
the region beyond the graph of a Lipschitz function of ω (ϑ being the distance in S³ from the circle {ϑ = 0}), so a
Lipschitz domain. Its lateral part consists of pieces of {R = R′, ϑ ≥ ϑ_c}, with outward conormal dt, and of
{ϑ = ϑ_c − c_*(R′ − R)}, a smooth hypersurface off the axes, as 0 < ϑ_c − c_*(R′ − R) < π/4 there, with outward conormal
dϑ + c_* dt and |dϑ| = 1. Both satisfy the condition of [[cor:class-kato-sphere]] (c), by the above with (c, ξ) = (1, 0)
and (c, ξ) = (c_*, dϑ); so u = ū on Ω_*. Every point with R > R_𝒫 lies in such a set, with R′ < R, and so does every
point with R ≤ R_𝒫 and ϑ < ϑ1 − c_*(R_𝒫 − R), with R′ close to R_𝒫, ϑ_c close to ϑ1 and R_b = R. With π/2 − ϑ, the
distance from the circle {ϑ = π/2}, in place of ϑ, the same holds where ϑ > π/2 − ϑ1 + c_*(R_𝒫 − R). This is the bound
on the domain of influence stated in (b).

(c) *A domain containing the lens.* The lens is the set between Σ′ and Σ_τ0, {τ0 + φ(R) ≤ τ ≤ τ0, 3.5 ≤ R ≤ 5.75}, in
region I ([[lem:margins-region-one]] (c)). Fix δ1 ∈ (0, 0.01] and put t := (τ − τ0 − φ(R))/(δ1 − φ(R)), smooth since
δ1 − φ ≥ δ1. Its level set {t = s} is {τ = τ0 + (1 − s)φ(R) + sδ1}: Σ′ for s = 0, Σ_(τ0+δ1) for s = 1, and the lens
lies in {0 ≤ t < 1}. The differential dt is a positive multiple of dτ − (1 − t)φ′ dR. Where φ′ ≠ 0, R ∈ (3.5, 5.75)
and 0 < f < 1, and for c ∈ [0, 1], as in the proof of [[cor:margins-lens]],

    g⁻¹(dτ − cφ′ dR, dτ − cφ′ dR) = −(2 − f) − 2c(1 − f)φ′ + c²fφ′² ≤ −1 + 2 × 0.0022 + 0.0022² < 0;

where φ′ = 0 the covector is dτ, timelike by [[lem:two-dust-domain]] (a). So dt is timelike, in the cone of dτ, and t
is a time function; (t, x) is a chart, as ∂_τt > 0. Let

    Ω_L := {0 ≤ t ≤ 1, R ≥ 0.70, v̂ + τ ≤ 2τ0 + 6}.

Where φ = 0, in particular for R ≤ 3.5 and for R ≥ 5.75, Ω_L agrees with {τ0 ≤ τ ≤ τ0 + δ1, R ≥ 0.70, v̂ + τ ≤ 2τ0 +
6}, which lies in Ω₂, as b(τ) = b(τ0) − 2(τ − τ0) > 6 there ([[sec:loc-setting]]). So the lateral boundaries of Ω_L
are pieces of {R = 0.70} and of {v̂ + τ = 2τ0 + 6}, spacelike with Ω_L to their past by [[lem:two-dust-domain]] (b),
(c), and the slices {t = s} ∩ Ω_L are the annuli 0.70 ≤ R ≤ 6 − 2sδ1 of the coordinates (s, x). These conditions are
strict on the compact Ω_L, so they hold for every Lorentzian metric C⁰-close to g0, and Ω_L is admissible for g0
([[def:class-admissible]]) in the chart (t, x).

*The hypotheses of [[thm:class-stability]].* (H1) holds for the background's phases v̂ and u, double-null coordinates of
g0, smooth with nonzero differentials (proof of [[cor:class-two-dust]]), and for the further phases by (b), once δ1 is
small. Let 𝒫_G be the union of the images of 𝒫 under T² × Z2 × Z2, a compact invariant subset of {R1 < R < R2,
ϑ1 < ϑ < π/2 − ϑ1}; the invariant data of (b) equal the background's outside 𝒫_G. For a small η > 0, let S_in be the set
of points of Σ′ with v̂(v = 3) − η ≤ v̂ ≤ v̂(v = 4.5) + η, S_out the set with u1 − η ≤ u ≤ u2 + η, and take S_in ∪ 𝒫_G,
S_out ∪ 𝒫_G for the background's families and 𝒫_G for the further ones, each intersected with {R ≤ 6}, so that they
lie in the first slice Σ′ ∩ {R ≤ 6} of Ω_L. These are closed and invariant, and they contain
the supports on Σ′ of the background's densities, which lie where v̂(v = 3) ≤ v̂ ≤ v̂(v = 4.5) and where u1 ≤ u ≤ u2, 𝒜
and ℬ being supported in [3, 4.5] and [u1, u2]. On Σ′, v̂ − R ∈ [τ0 − 0.0012, τ0], so S_in lies in 3.7 < R < 5.5
([[sec:table-shell]]: v̂(v = 3) + 0.68 = 3.8253… and v̂(v = 4.5) + 0.68 = 5.3724…), and S_out, which is the part of Σ_τ0
with R_u2 ≤ R ≤ R_* when η = 0 ([[prop:bg-seed]] (a), [[lem:bg-rstar]]), lies in 1.8 < R < 3.5 for η small. In the
chart, g0 = −q²f(dτ + dR)² + 2q(dτ + dR) dR + R²dΩ₃², and qf < 1 on Ω_L for δ1 small (on Σ_τ0 by [[sec:loc-setting]], on
the lens as f < 1 in region I); so a future causal vector has Ṙ/τ̇ between the roots −1 and qf/(2 − qf) < 1 of
(2 − qf)x² + 2(1 − qf)x − qf, that is |Ṙ| ≤ τ̇, and R²|Ω̇|² ≤ Cτ̇². Along a dust curve in Ω_L, R therefore changes by at
most the τ-thickness of Ω_L, which is δ1 where φ = 0 and at most 0.0012 + δ1 ≤ 0.0122 elsewhere. Hence the tubes of S_in
and S_out stay in 1.7 < R < 5.6, away from the lateral boundaries. The background's families are radial, so their tubes
over 𝒫_G keep its angles, in [ϑ1, π/2 − ϑ1]. A tube of a further family near a lateral boundary runs where φ = 0, so its
angular displacement there is at most Cδ1, and for δ1 small it stays away from the axes. So no tube meets a
neighbourhood of a point where a lateral boundary meets an axis, and (H2′) puts no condition.

*The datum on the first slice.* The slice {t = 0} of Ω_L is Σ′_L := Σ′ ∩ {R ≤ 6}. Near the axes, where φ = 0, the
lateral components of Ω_L meet each slice {t = s} in the spheres R = 0.70 and R = 6 − 2sδ1, on which v̂ and u are
constant (u is constant on the spheres of each slice {v̂ − R = const}, proof of [[cor:class-two-dust]]); so each
component has the property of [[def:class-adapted]] for both background families. Whichever components are treated as
adapted there, and to whichever family, the datum's phase of every family is on Σ′ the background's phase of that
family, by (b), the background's phase ů_A of a further family being the eikonal that (b) gives it. So the constants of
the normalisation in [[def:class-adapted]] vanish, and at the points of B ∩ Σ′ in 𝒱_B, which contains the sets 𝒰_(2δ_B)
about the points of B on the axes, for a component B adapted to a family A, the datum's phase of A is ů_A, which equals
c_B(0) there. By the last paragraph of [[def:class-adapted]], T_(0,U) is the identity and a datum on Σ′_L suffices; the
constraints and the gauge condition are required on Σ′_L, and the condition on the supports in [[thm:class-stability]]
is supp q_A ∩ Σ′_L ⊂ S_A for every A. It holds: outside 𝒫_G the densities of the background's families are the
background's, and those of the further families vanish. The sets 𝒱_B may be taken in {R < 0.8} for the inner component
and in {R > 5.9} for the outer one, whose spheres have R ≥ 6 − 2δ1 ≥ 5.98. Each T_(s,U) is a diffeomorphism equal to the
identity outside them, so it maps their union onto itself, and the adapted domain Ω_U of the development agrees with Ω_L
on {0.8 ≤ R ≤ 5.9}; so it contains the lens and Σ_τ0 ∩ {3.5 ≤ R ≤ 5.75}, which lie in Ω_L there.

*The development.* Complete the constraint data of (b) on Σ′_L, with their dust phases and densities, to a datum of
[[thm:class-stability]] on Σ′_L: the metric on Σ′ with the background's lapse and shift, and the gauge condition
D(g) = 0 imposed through the transversal derivatives, as in [[thm:data]]. This datum is within Cε of the background's,
so for ε small [[thm:class-stability]] gives the development on its adapted domain Ω_U, within Cε of g0. Since Σ_τ0 ∩
{3.5 ≤ R ≤ 5.75} lies in Ω_U, and Σ_τ0 = Σ′ elsewhere, it induces constraint data on the whole of Σ_τ0; for R ∉
(3.5, 5.75) these are the data of (b), which the development attains on Σ′.

*Localisation across the lens.* At a point of Σ_τ0 the induced metric and second fundamental form, and the matter part
ℋ/2 and ℳ of [[eq:loc-constraints]], are computed from g and its first derivatives and from the differentials of the
phases and the densities at that point. Let α and β be as in (c). By (b), the data of (b) equal the background's outside
the domain of influence of 𝒫, so they equal the background's at the points of Σ′ with 3.44 ≤ R ≤ 5.85 and ϑ < α, and at
those with 3.44 ≤ R ≤ 5.85 and ϑ > β. If α > 3.3 × 10⁻⁴, [[lem:loc-lens-dependence]] below gives, for ε small, depending
also on α, that g with its first derivatives, the differential of the ingoing phase and every density equal the
background's at the points of the lens with ϑ < α − 3.3 × 10⁻⁴; if α ≤ 3.3 × 10⁻⁴ there are no such points. The same
holds for ϑ > β + 3.3 × 10⁻⁴. At these points of Σ_τ0 the induced data are therefore the background's. ∎

**Lemma {#lem:loc-lens-dependence}** (Dependence across the lens.) Let Ω_L, t and δ1 be as in the proof of
[[thm:loc-bent-slice]] (c), and let (g, u_A, q_A) be the development constructed there. Let 3.3 × 10⁻⁴ < α < π/2, and
let the data of [[thm:loc-bent-slice]] (b), the metric and second fundamental form and the densities of all families,
equal the background's at the points of Σ′ with 3.44 ≤ R ≤ 5.85 and ϑ < α. Then for ε small, depending also on α, at
every point of the lens with ϑ < α − 3.3 × 10⁻⁴ the metric g and its first derivatives equal those of g0, the
differential of the ingoing family's phase equals the background's, and every density equals the background's. The
same holds, for 0 < β < π/2 − 3.3 × 10⁻⁴, with ϑ > β and ϑ > β + 3.3 × 10⁻⁴ in place of ϑ < α and
ϑ < α − 3.3 × 10⁻⁴.

*Proof.* We prove the first statement; the second is proved in the same way, with axis 1 in place of axis 2.

*Notation.* By [[thm:class-stability]] the development solves [[eq:class-system]] on its adapted domain Ω_U, which
agrees with Ω_L on {0.8 ≤ R ≤ 5.9} (proof of [[thm:loc-bent-slice]] (c)), in the gauge D(g) = 0 relative to g0, and its
norm 𝒩_k of [[eq:class-energy]] is at most Cε. Fix k ≥ 6 and apply that theorem with k + 2 in place of k: the data are
ε-close in C^∞, and by its uniqueness the development is the same. Let u_in be the development's phase of the ingoing
family, with the sign of [[sec:class-augmented]], so that P := g⁻¹p, p := du_in, is future directed; put v_in := −u_in,
Θ := □_g u_in and let q_in be the ingoing density. Then v_in = v̂ on Σ′, by (b), and the derivatives of v_in − v̂ of
order at most k − 1 are at most Cε on Ω_U. For the background write ů_in := −v̂, p̊, P̊, Θ̊ and q̊_in. Put
τ_L := 0.0011596, the bound on the τ-depth of the lens in [[thm:loc-bent-slice]] (a), t1 := τ_L/(δ1 + τ_L), W := 1.015
(δ1 + τ_L)/3.5756 (3.5756 = 3.5 × 1.0216), α′ := α − 4 × 10⁻⁷, c_a := τ0 + 3.44, c_b := τ0 + 5.85, c_v := 0.05, and

    𝒟 := {y ∈ Ω_U : t ≤ t1, ϑ ≤ α′ − W t, c_a + c_v t ≤ v_in ≤ c_b − c_v t}.                   {#eq:loc-lens-region}

Then W t1 = 1.015 τ_L/3.5756 ≤ 3.2918 × 10⁻⁴, and on 𝒟, ϑ ≤ α′ < π/2 and on its angular face ϑ ≥ α − 3.2958 × 10⁻⁴ > 0.

(1) *Where 𝒟 lies.* By the definition of t, τ = τ0 + (1 − t)φ(R) + tδ1 and −τ_L ≤ φ ≤ 0 ([[prop:margins-bend]] (b)); so
on 𝒟, −τ_L ≤ τ − τ0 ≤ tδ1 ≤ t1δ1 < τ_L, and as |v_in − v̂| ≤ Cε, R = v̂ − τ satisfies

    3.44 + t(c_v − δ1) − Cε ≤ R ≤ 5.85 + τ_L + Cε < 5.86.

Every point of 𝒟 lies in region I. Where τ ≤ τ0 this is [[lem:margins-region-one]] (c), as R ≥ 3.4399 > R_*. Where
τ > τ0, the ray u = 5.7 is {τ = τ_ray(R)} with dτ_ray/dR = 2/f − 1 ≥ 1 ([[lem:margins-region-one]] (b), (c), its time
v̂ ≤ τ0 + τ_L + 3.4384 < v̂(v = 3) there), so it meets the slice {τ = const} at a radius at most R_* + (τ − τ0), which
is at most 3.43719 + tδ1 < 3.44 + t(c_v − δ1) − Cε, since c_v ≥ 2δ1; and u decreases strictly in R along that slice
(proof of [[cor:class-two-dust]]), so u < 5.7 at the points of 𝒟. Hence on 𝒟, by [[lem:margins-region-one]] (a),

    g0 = −f dτ² + 2(1 − f) dτ dR + (2 − f) dR² + R² dΩ₃²,      f = 1 − μ/R²,      3/2 ≤ μ ≤ 3.6059,

so 0.69 < f ≤ 1 − 1.5/5.86² ≤ 0.95632; the inverse has g0^(ττ) = −(2 − f), g0^(τR) = 1 − f, g0^(RR) = f, g0^(ϑϑ) = R⁻²
and no other entry pairing dϑ with dτ or dR. The background's outgoing density vanishes on 𝒟, as ℬ = 0 in region I. 𝒟
lies in the interior of Ω_L, since R > 0.70, v̂ + τ = 2τ + R < 2τ0 + 6 and t1 < 1, and so in the interior of Ω_U, as
0.8 < R < 5.9 on 𝒟. On 𝒟 the coordinate field ∂_t of the chart (t, x) is (δ1 − φ)∂_τ, with g0(∂_τ, ∂_τ) = −f < 0 and
dτ(∂_τ) = 1: it is future timelike, for g as well when ε is small.

A point y of the lens with ϑ(y) < α − 3.3 × 10⁻⁴ lies in 𝒟. Indeed τ(y) ≤ τ0 gives t(y) ≤ |φ|/(δ1 + |φ|) ≤ t1, so
ϑ(y) < α′ − 3.2958 × 10⁻⁴ ≤ α′ − W t(y); and v̂(y) = τ + R lies in [τ0 + 3.5 − τ_L, τ0 + 5.75], so c_a + c_v t(y) ≤ τ0 +
3.49 < v_in(y) < τ0 + 5.8 ≤ c_b − c_v t(y) for ε small.

(2) *The lateral faces.* 𝒟 = {y ∈ Ω_U : t ≤ t1, F_1 ≤ 0, F_2 ≤ 0, F_3 ≤ 0} with F_1 := ϑ + W t − α′, F_2 := c_a + c_v t −
v_in and F_3 := v_in + c_v t − c_b. We show that at the points of 𝒟 each dF_i is timelike for g and positive on the
nonzero future causal vectors of g. A covector positive on these is timelike: otherwise its kernel would contain a
nonzero causal vector. As in the proof of [[thm:loc-bent-slice]] (c), dt = η/(δ1 − φ) with η := dτ − κ_L dR,
κ_L := (1 − t)φ′, |κ_L| ≤ 0.0021370 ([[prop:margins-bend]] (c)), δ1 − φ ≤ δ1 + τ_L ≤ 0.0111596, and

    −g0⁻¹(η, η) = (2 − f) + 2κ_L(1 − f) − κ_L² f ≥ 1.0216²:

where φ′ ≠ 0, so 3.5 < R < 5.75, the left side is at least 1 + 1.5/5.75² − 2 × 0.002137 × 3.6059/3.5² − 0.002137² ≥
1.04410; elsewhere it is 2 − f = 1 + μ/R² ≥ 1 + 1.5/5.86² ≥ 1.04368; and 1.0216² ≤ 1.04367. A nonzero future causal
vector Y of g0 has τ̇ := dτ(Y) > 0 and x := dR(Y)/τ̇ between the roots −1 and f/(2 − f) of (2 − f)x² + 2(1 − f)x − f,
so that η(Y) = τ̇(1 − κ_L x) ≥ (1 − |κ_L|)τ̇ and dv̂(Y) = (1 + x)τ̇ ≤ 2τ̇/(2 − f).

For F_1: since g0⁻¹(dϑ, dϑ) = R⁻² and g0⁻¹(dϑ, η) = 0,

    g0⁻¹(dF_1, dF_1) = R⁻² + (W/(δ1 − φ))² g0⁻¹(η, η) ≤ R⁻² − (1.0216 W/(δ1 − φ))².

Where R ≥ 3.5, 1.0216 W/(δ1 − φ) ≥ 1.015/3.5 ≥ 1.015/R; where R < 3.5, φ = 0 and 1.0216 W/δ1 = 1.015
(1 + τ_L/δ1)/3.5 ≥ 0.3236 ≥ 1.1/R, as δ1 ≤ 0.01 and R ≥ 3.43. So g0⁻¹(dF_1, dF_1) ≤ −0.03 R⁻², and dF_1(∂_t) = W > 0.
For F_2: dv̂(Y) ≤ 1.9163 τ̇ ≤ 1.9205 η(Y), while c_v dt(Y) = c_v η(Y)/(δ1 − φ) ≥ 4.48 η(Y); so (c_v dt − dv̂)(Y) ≥ 2.5
η(Y) > 0. These bounds for F_1 and F_2 are strict, uniformly on the compact 𝒟, and g − g0 and dv_in − dv̂ are at most Cε
there; so for ε small they hold for g and v_in. For F_3: dF_3 = dv_in + c_v dt, where dv_in is null for g and
dv_in(Y) = −g(P, Y) ≥ 0 for future causal Y; so dF_3 is positive on the nonzero future causal vectors, dt being so.

Consequently a past directed causal curve γ of g that starts in 𝒟 stays in 𝒟 while t > 0. Let y = γ(s*) be its last
point with γ([0, s*]) ⊂ 𝒟, and suppose t(y) > 0. Along γ, t decreases, so t ≤ t1 continues to hold; the F_i negative
at y stay negative near s*; and each F_i with F_i(y) = 0 has derivative dF_i(γ̇) < 0 there, γ̇ being past directed.
So γ(s) ∈ 𝒟 for s a little beyond s* (𝒟 lying in the interior of Ω_U), against the choice of s*.

(3) *Only the ingoing family carries dust in 𝒟.* The background has no further families, and its outgoing density
vanishes on 𝒟 by (1). For the development, let A be the outgoing family or a further one and y ∈ 𝒟. The integral curve
of P_A through y, followed to the past, is a past directed causal curve of g along which t decreases at a rate bounded
below on the compact 𝒟; by (2) it stays in 𝒟 until it reaches a point y0 of 𝒟 ∩ Σ′. On Σ′, v̂ = τ0 + R + φ(R)
increases with R and equals c_a at R = 3.44 and c_b at R = 5.85, where φ = 0; so y0 has 3.44 ≤ R ≤ 5.85 and ϑ ≤ α′ < α,
and q_A(y0) is the background's, 0. The conservation law of [[eq:class-system]] reads P_A(q_A) = −(□_g u_A) q_A, a
linear ordinary differential equation along the curve; so q_A(y) = 0. On 𝒟 the stress of either solution is therefore
that of its ingoing family alone.

(4) *The equations compared.* On 𝒟 both (g, u_in, q_in) and (g0, ů_in, q̊_in) satisfy, by [[eq:class-system]], the gauge
condition and (3):

(i) Ric^H(g) = q_in p ⊗ p, Ric^H the reduced Ricci tensor relative to g0 ([[eq:gauge]]);
(ii) P^b ∂_b p_a = P^b Γ[g]^c_ba p_c, as ∇_P p = ½ d g⁻¹(p, p) = 0;
(iii) P(Θ) = −|∇²u_in|²_g, which is [[eq:class-raychaudhuri]] with Ric(P, P) = q_in g⁻¹(p, p)² = 0;
(iv) P(q_in) = −Θ q_in.

In (iii), by [[eq:class-identity]], |∇²u_in|² = S_loc := (Θ − κ1 − κ2)² + κ1² + κ2² off the axes, and by
[[eq:class-x]] and continuity ([[prop:class-axis]] (d)), |∇²u_in|² = S_ax := κ1² + ½(Θ − κ1)² + ½σ² near axis 2,
where σ is the planar shear of the level sets of u_in in the slices {t = s}. Fix δ := 1/2 and the points p_i of axis 2
in a slice with ρ1(p_i) = 3.4, 3.8, …, 5.8; then δ ≤ ρ1(p_i)/4, and [[lem:class-leaf-differences]], for the background
and the ingoing family, holds near each p_i, with balls 𝔅, 𝔅′ and a constant C common to these points and to
0 ≤ s ≤ t1. Let χ_Z be a G-invariant function of ρ2 equal to 1 for ρ2 ≤ 1/8 and to 0 for ρ2 ≥ 1/4. Then on 𝒟,
the square |∇²u_in|² is χ_Z S_ax + (1 − χ_Z) S_loc. Where χ_Z ≠ 1, S_loc is a smooth function of (g, ∂g, p, Θ),
since there g(K2, K2) ≥ c and, ϑ ≤ α′ < π/2 on 𝒟, g(K1, K1) ≥ c(α′) > 0 (proof of [[prop:class-augmented]] (a));
where χ_Z ≠ 0, S_ax is a smooth function of (g, ∂g, p, Θ, σ), κ1 being smooth near axis 2.

Put w := g − g0 and 𝔡 := (w, ∂_t w, ∂_x w, p − p̊, Θ − Θ̊, q_in − q̊_in). Write (i) in the first-order form of Step 9 of
the proof of [[thm:class-stability-off-axes]], in the chart (t, x), with the difference of the principal parts taken as
in Step 4 there, ½(g^(ab) − g0^(ab)) ∂_a ∂_b g0, and (ii)–(iv) as transports along P. Subtracting the background's
equations from the development's gives on 𝒟 a linear system 𝐀^0 ∂_t 𝔡 + 𝐀^j ∂_j 𝔡 = F_𝔡, with 𝐀^0 = diag(1, −g^(tt),
g^(ab)) on the wave block and P^t on the transports, 𝐀^j its other matrices, all symmetric and evaluated at the
development, and with F_𝔡 bounded at every point of 𝒟 by C |𝔡| + C χ_Z |σ − σ̊|, σ̊ the background's: C bounds the
derivatives of the smooth functions concerned on the compact 𝒟, where both solutions are smooth. On 𝒟, dt is timelike
and ∂_t future timelike for g; so −g^(tt) > 0, g^(ab), the restriction of g⁻¹ to the covectors vanishing on ∂_t, is
positive definite, P^t = dt(P) > 0, and 𝐀^0 ≥ c0 I with c0 > 0.

(5) *𝔡 vanishes on 𝒟 ∩ Σ′.* The development's datum on Σ′ is built at each point from the constraint data, the
background's lapse and shift and the gauge condition D(g) = 0 solved for the transversal derivatives ([[thm:data]]);
its ingoing phase on Σ′ is −v̂ by (b); p is fixed on Σ′ by its spatial part and g⁻¹(p, p) = 0; and Θ = □_g u_in on Σ′
is computed from g, ∂g, the derivatives of u_in along Σ′ and the transversal derivative of p that (ii) gives. All of
these equal the background's at the points of Σ′ with 3.44 < R < 5.85 and ϑ < α, by hypothesis, hence on the closure
of that set, which contains 𝒟 ∩ Σ′.

(6) *The planar shear.* Let 𝒟_s := 𝒟 ∩ {t = s}, a subset of the x-space. We show that, for 0 ≤ s ≤ t1,

    ‖χ_Z (σ − σ̊)‖_(L²(𝒟_s)) ≤ C ‖𝔡(s)‖_(L²(𝒟_s)).                                            {#eq:loc-lens-shear}

*The leaves stay in 𝒟_s.* Let y ∈ 𝒟_s with ρ2(y) ≤ 1/4. On M3 := {t = s, φ1 = 0} use the coordinates (z, y′) :=
(ρ1, x3, x4) of [[lem:class-leaf]] and r := |y′| = ρ2; there R = (z² + r²)^(1/2) and z ≥ 3.39. On the slice, v̂ is a
function V(R) := τ0 + (1 − s)φ(R) + sδ1 + R with 0.997 ≤ V′ ≤ 1.003 and |V″| ≤ 0.01, so ∂_z v̂ = V′z/R ≥ 0.98 and
∂_r² v̂ = V″r²/R² + V′z²/R³ ≤ 0.31 for r ≤ 1/2; v_in differs from v̂ by Cε in C². So, near the axis, the level set
{v_in = v_in(y)} of the slice meets M3 in a graph z = h(r), 0 ≤ r ≤ 1/4. As v_in is invariant, ∂_r v_in vanishes at
r = 0, so |h′(r)| = |∂_r v_in/∂_z v_in| ≤ r sup |∂_r² v_in|/0.97 ≤ r. Then tan ϑ = r/h(r) has the derivative
(h − rh′)/h² > 0, since rh′ ≤ r² < h. So along the leaf from the axis to y, ϑ increases and v_in is constant: the arc
{(h(r), r) : 0 ≤ r ≤ ρ2(y)}, with its images under G, lies in 𝒟_s.

*An extension.* The map Φ_s(x) := (v_in(s, x), x/|x|) is a G-equivariant diffeomorphism of a neighbourhood of 𝒟_s onto
its image in R × S³, under which 𝒟_s is [c_a + c_v s, c_b − c_v s] × {ϑ ≤ α′ − Ws}; at s = 0, v_in = v̂. Let A_s be the
affine map of [c_a, c_b] onto [c_a + c_v s, c_b − c_v s], and m_s the flow on S³, for the time Ws, of a G-invariant
vector field equal to −∂_ϑ on {α′ − W t1 ≤ ϑ ≤ α′} and to 0 near the axes. Then ψ_s := Φ_s⁻¹ ∘ (A_s × m_s) ∘ Φ_0 is a
G-equivariant diffeomorphism near 𝒟_0, C¹-close to the identity, with ψ_s(𝒟_0) = 𝒟_s, whose derivatives of order at most
k − 1, and those of its inverse, are bounded independently of s and of ε by the bound on v_in − v̂; we extend it to a
diffeomorphism of R⁴ equal to the identity outside a compact set. 𝒟_0 = Σ′ ∩ {3.44 ≤ R ≤ 5.85, ϑ ≤ α′} is a bounded
Lipschitz domain of the x-space. Let E be its extension operator of [[thm:std-sy-extension]] and 𝔼_s f the average over
G of (E(f ∘ ψ_s)) ∘ ψ_s⁻¹. By [[thm:std-sy-extension]] and [[thm:std-ly-extension]] (Lemma 27 there), 𝔼_s is bounded on
L² and on H^(k−1), the norms of the compositions depending only on bounds for the derivatives of ψ_s and ψ_s⁻¹ (chain
rule and change of variables, as in the proof of [[thm:class-kato]] (b) (ii)); so its bound C_E depends on α but not on
s or ε. And 𝔼_s f = f on 𝒟_s for invariant f, 𝒟_s being invariant.

*The bound.* Let U be the development's state (g, ∂g, p, Θ, q_in) on 𝒟_s, with Θ = □_g u_in, ů the background's state on
the slice, which the background defines on the sets 𝒰_2δ(p_i) as well, and Ŭ := ů + 𝔼_s 𝔡(s). Then Ŭ = U on 𝒟_s, and
the distance of Ŭ from ů in the norm 𝒩_(k−1) is at most C_E ‖𝔡(s)‖_(H^(k−1)(𝒟_s)) ≤ C_E C ε; so Ŭ lies in the ball 𝔅′
of [[lem:class-leaf-differences]] for ε small, depending also on α. Let y ∈ 𝒟_s with ρ2(y) ≤ 1/4 and let h be the
level set of u_in through y found above, issued from the axis point (h(0), 0). As Θ = □_g u_in, H_L[Θ] is the mean
curvature of the leaf (step (1) of the proof of [[lem:class-planar-shear]]), so h solves [[eq:class-leaf-volterra]]
for U on [0, ρ2(y)] ([[lem:class-leaf]] (c)). That equation uses U only along the arc of h, where Ŭ = U together with
∂g; so h solves it for Ŭ, and by the uniqueness in [[lem:class-volterra]] the leaf of Ŭ issued from (h(0), 0) is h on
[0, ρ2(y)]: it is the leaf of Ŭ through y. The planar shear at y is determined by h and h′ at ρ2(y), by H_L there,
which fixes h″ through the leaf equation, and by the values of Ŭ = U and the 1-jet of γ3 at y
([[eq:class-shear-leaf]]); so σ[Ŭ](y) = σ(y), and likewise σ[ů] = σ̊. The sets 𝒰_δ(p_i) cover {ρ2 ≤ 1/4} ∩ 𝒟_s, where
3.39 ≤ ρ1 ≤ 5.86, and [[lem:class-leaf-differences]] (b) gives

    ‖χ_Z (σ − σ̊)‖_(L²(𝒟_s)) ≤ Σ_i ‖σ[Ŭ] − σ[ů]‖_(L²(𝒰_δ(p_i))) ≤ C Σ_i ‖Ŭ − ů‖_(L²(𝒰_2δ(p_i)))
                              ≤ C C_E ‖𝔡(s)‖_(L²(𝒟_s)),

which is [[eq:loc-lens-shear]].

(7) *The energy.* For 0 ≤ s ≤ t1 put e(s) := ∫_(𝒟_s) ⟨𝐀^0 𝔡, 𝔡⟩ dx. On 𝒟 away from the axes, dt, dv_in and dϑ are
independent: in the coordinates (t, R) the differential of v̂ is (δ1 − φ) dt + (1 + (1 − t)φ′) dR. So the faces
{F_i = 0} meet one another and the slices transversally, and 𝒟 ∩ {t ≤ s} is a Lipschitz domain, bounded by 𝒟_0, 𝒟_s
and pieces of the faces. The field (⟨𝐀^μ 𝔡, 𝔡⟩)_μ is smooth, with divergence ⟨(∂_μ 𝐀^μ) 𝔡, 𝔡⟩ + 2⟨F_𝔡, 𝔡⟩ by the
symmetry of the 𝐀^μ, and the divergence theorem on 𝒟 ∩ {t ≤ s}, as in the proof of [[thm:class-kato]] (b) (i), gives

    e(s) + ∫ ⟨(ν_μ 𝐀^μ) 𝔡, 𝔡⟩ |ν|⁻¹ dS = e(0) + ∫_0^s ∫_(𝒟_s′) (⟨(∂_μ 𝐀^μ) 𝔡, 𝔡⟩ + 2⟨F_𝔡, 𝔡⟩) dx ds′,

the middle integral taken over the pieces of the faces, ν being a positive multiple of dF_i on {F_i = 0}. By (2) and
(1), ν_t = ν(∂_t) > 0, g⁻¹(ν, ν) < 0 and ν(P) > 0 there; so the boundary matrix is nonnegative, on the wave block by
Step 9 of the proof of [[thm:class-stability-off-axes]] and on the transports, where it is ν(P). We drop that
integral. e(0) = 0 by (5). By the bound on F_𝔡 in (4) and by [[eq:loc-lens-shear]], the right side is at most
C ∫_0^s ‖𝔡(s′)‖²_(L²(𝒟_s′)) ds′ ≤ (C/c0) ∫_0^s e. By Gronwall's inequality e = 0, so 𝔡 = 0 on 𝒟. With (1) and (3) this
is the first statement.

For the second, use 𝒟 := {y ∈ Ω_U : t ≤ t1, ϑ ≥ β + 4 × 10⁻⁷ + W t, c_a + c_v t ≤ v_in ≤ c_b − c_v t}, the face function
β + 4 × 10⁻⁷ + W t − ϑ, whose differential has the norm and the sign of dF_1, axis 1 in place of axis 2, the
coordinates (ρ2, x1, x2) of M3 := {t = s, φ2 = 0}, and the results of [[sec:class-planar-shear]] at axis 1, where they
hold with the two planes exchanged and the same proofs. ∎

**Remark {#rem:loc-band-grid}** (Numerical observation.) On the discretisation of [[rem:two-dust-example]] at 40, 80 and
160 steps per unit, N_κ evaluated on Σ_τ0 from the grid solution was negative except on R ∈ [4.2956, 4.5264] at 160
steps ([4.3017, 4.5204] at 80), with largest value 1.7925 × 10⁻³ at R = 4.3994, and qf ≤ 0.9052 throughout; with the
flux term −qf_v̂/2 dropped the largest value was −0.036, and with half the shell's amplitude it was −0.017. No proof
uses this remark; the band is that of [[prop:loc-band]].

### Exact localisation on the cones {#sec:loc-cones}

In the double-null gauge of the class,

    g = −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ (dϑ − b du)² + e^(2A_c) dφ1² + e^(2A_s) dφ2²,  {#eq:loc-double-null}

with Ω, γ_ϑ, b, A_c, A_s functions of (u, v, ϑ), the cone 𝒞 := {u = u_c} is ruled by the null generators ∂_v. Put
ϰ_1 := ½ ln γ_ϑ, ϰ_2 := A_c, ϰ_3 := A_s.

**Lemma {#lem:loc-cone-equations}** (The constraints on a cone.) On 𝒞,

    Ric(∂_v, ∂_v) = Σ_(i=1)^3 (−∂_v²ϰ_i − (∂_vϰ_i)² + 2 ∂_v ln Ω ∂_vϰ_i),
    Ric(∂_v, ∂_ϑ) = (γ_ϑ/(4Ω²)) (∂_v²b + ∂_v ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) ∂_v b) + r,  {#eq:loc-cone}

    r := (∂_ϑ ln Ω + ∂_ϑϰ_2 + ∂_ϑϰ_3) ∂_vϰ_1 + (∂_vϰ_2 + ∂_vϰ_3) ∂_ϑ ln Ω − ∂_v∂_ϑ ln Ω
         − Σ_(i=2,3) (∂_ϑϰ_i ∂_vϰ_i + ∂_v∂_ϑϰ_i).                                              {#eq:loc-cone-r}

Neither line contains a u-derivative, and b enters only through ∂_v b and ∂_v² b.

*Proof.* The inverse metric has g^(uv) = −1/(2Ω²), g^(vϑ) = −b/(2Ω²), g^(ϑϑ) = γ_ϑ⁻¹, g^(φ1φ1) = e^(−2A_c),
g^(φ2φ2) = e^(−2A_s), and g^(uu) = g^(vv) = g^(uϑ) = 0. Hence ∇_(∂_v)∂_v = Γ^v_(vv)∂_v = k ∂_v with k := 2∂_v ln Ω,
since g_vv = g_vϑ = 0. The sections {u, v constant} carry the metric γ_ϑ dϑ² + e^(2A_c)dφ1² + e^(2A_s)dφ2², b not
entering because du = 0 on them; ∂_v is orthogonal to them and commutes with ∂_ϑ and ∂_(φi), so their null second
fundamental form χ along ∂_v is half the v-derivative of that metric, with eigenvalues ∂_vϰ_i, trace tr χ = Σ∂_vϰ_i
and |χ|² = Σ(∂_vϰ_i)². The Raychaudhuri equation ∂_v tr χ = k tr χ − |χ|² − Ric(∂_v, ∂_v) is the first line.

For the second line we use Ric(∂_v, ∂_ϑ) = ∂_aΓ^a_(vϑ) − ∂_v∂_ϑ ln √|det g| + Γ^a_(ad)Γ^d_(vϑ) − Γ^a_(ϑd)Γ^d_(av),
with indices over (u, v, ϑ, φ1, φ2) and Γ^a_(ad) = ∂_d ln √|det g|, where det g = −4Ω⁴γ_ϑe^(2A_c + 2A_s). From the
inverse metric above and Γ^a_(bc) = ½g^(ad)(∂_bg_(dc) + ∂_cg_(db) − ∂_dg_(bc)), with β_v := (γ_ϑ/(4Ω²))∂_v b, the symbols
that enter are

    Γ^v_(vv) = 2∂_v ln Ω,   Γ^v_(vϑ) = ∂_ϑ ln Ω + β_v,   Γ^ϑ_(vϑ) = ∂_vϰ_1,   Γ^(φ1)_(vφ1) = ∂_vϰ_2,
    Γ^(φ2)_(vφ2) = ∂_vϰ_3,   Γ^(φi)_(ϑφi) = ∂_ϑϰ_(i+1),   Γ^u_(ϑϑ) = (γ_ϑ/(2Ω²))∂_vϰ_1,
    Γ^ϑ_(ϑϑ) = ∂_ϑϰ_1 + (γ_ϑb/(2Ω²))∂_vϰ_1,   Γ^ϑ_(uv) = (2Ω²/γ_ϑ)∂_ϑ ln Ω − ½∂_v b − b∂_vϰ_1,

and Γ^u_(vv) = Γ^u_(uv) = Γ^u_(vϑ) = Γ^ϑ_(vv) = Γ^(φi)_(vϑ) = 0; the only nonzero Γ^d_(vϑ) are Γ^v_(vϑ) and Γ^ϑ_(vϑ).
None of these contains a u-derivative, and Γ^u_(vϑ) = 0, so no u-derivative enters. Then ∂_aΓ^a_(vϑ) = ∂_v∂_ϑ ln Ω +
∂_vβ_v + ∂_v∂_ϑϰ_1; Γ^a_(ad)Γ^d_(vϑ) = ∂_v ln √|det g| (∂_ϑ ln Ω + β_v) + ∂_ϑ ln √|det g| ∂_vϰ_1; and the terms of
Γ^a_(ϑd)Γ^d_(av) are, for (a, d) = (v, v), (ϑ, v), (u, ϑ), (ϑ, ϑ), (φi, φi),

    2∂_v ln Ω (∂_ϑ ln Ω + β_v),   ∂_vϰ_1 (∂_ϑ ln Ω + β_v),   ∂_vϰ_1 ∂_ϑ ln Ω − ∂_vϰ_1β_v − (γ_ϑb/(2Ω²))(∂_vϰ_1)²,
    (∂_ϑϰ_1 + (γ_ϑb/(2Ω²))∂_vϰ_1)∂_vϰ_1,   ∂_ϑϰ_(i+1)∂_vϰ_(i+1),

all other products vanishing. The two terms in b without derivative cancel. With ln √|det g| = ln 2 + 2 ln Ω + ϰ_1 +
ϰ_2 + ϰ_3, the terms in β_v add up to ∂_vβ_v + (∂_vϰ_1 + ∂_vϰ_2 + ∂_vϰ_3)β_v, which is the first term of the second line
since ∂_vβ_v = β_v(2∂_vϰ_1 − 2∂_v ln Ω) + (γ_ϑ/(4Ω²))∂_v²b; and the remaining terms add up to r. ∎

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

On the corner sphere S = 𝒞_out ∩ 𝒞_in the two cones must induce one metric, γ_ϑ dϑ² + e^(2A_c) dφ1² + e^(2A_s) dφ2²; as ϕ
is the background's on S on both cones, this holds exactly when the free data of [[prop:loc-cones]] at v = 0 and those of
[[lem:loc-cone-in]] at u = 0 agree; nothing else is required at S, the density q_in being free on 𝒞_out and q_out on
𝒞_in. Near the background's data, and with the band away from the axes, these cone data have a development.

**Theorem {#thm:loc-cone-development}** (Development of cone data localised in angle.) Let u_1, v_1 > 0 be such that R >
a on the segments 𝒞_out ∩ {v ≤ v_1} and 𝒞_in ∩ {u ≤ u_1}, a = q0 − δ0 = 0.70 the inner radius of [[sec:domain]]
([[sec:loc-setting]]), let R_min be the least value of R on them and C_0 := 2√2/R_min. Let 0 < ϑ_a < ϑ_b < π/2, η :=
(1/4) min(ϑ_a, π/2 − ϑ_b), k ≥ 6 an integer and m := 6k + 21. Take free data (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0 on 𝒞_out ∩ {v ≤
v_1} as in [[prop:loc-cones]], and (ℓ_1, ℓ_2, ℓ_3) and q_out ≥ 0 on 𝒞_in ∩ {u ≤ u_1} as in [[lem:loc-cone-in]], the two
sets of free data agreeing on S. Let them be smooth and equal to the background's outside compact sets K_out ⊂ [0, v_1) ×
(ϑ_a, ϑ_b) and K_in ⊂ [0, u_1) × (ϑ_a, ϑ_b) of the coordinates (v, ϑ) and (u, ϑ), and let ε be the largest absolute value
of a derivative of order at most m of their differences from the background's. Let [ϑ_a′, ϑ_b′] be the least interval
that contains the angles of the points of K_out ∪ K_in, u_K the least u on K_in and v_K the least v on K_out (u_K := u_1
if K_in is empty, v_K := v_1 if K_out is). There is δ_* > 0, depending only on the background, u_1, v_1 and the band, and
there are ε_0, C, ε_2 > 0, depending also on k, such that for ε ≤ ε_0, with

    G_* := {(u, v) : 0 ≤ u ≤ u_1, 0 ≤ v ≤ v_1, uv ≤ δ_*²},                                          {#eq:loc-cone-domain}

the following hold.

(a) *Existence.* The factors e^ϕ of [[prop:loc-cones]] and [[lem:loc-cone-in]] stay positive, and there is a smooth class
solution of [[eq:class-system]] on G_* × S³ with two families, an ingoing one with phase v and density q_in and an
outgoing one with phase u and density q_out, so that Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, whose metric has the form
[[eq:loc-double-null]] in the coordinates (u, v, ϑ, φ1, φ2), and which induces on 𝒞_out the functions Ω, γ_ϑ, b, A_c,
A_s and q_in of [[prop:loc-cones]] and on 𝒞_in those of [[lem:loc-cone-in]], with b = 0. G_* contains the strips
{u ≤ δ_*²/v_1} and {v ≤ δ_*²/u_1} of the rectangle [0, u_1] × [0, v_1], a future neighbourhood of both cones.

(b) *Localisation.* The solution equals the background at the points of G_* × S³ with ϑ < ϑ_a′ − η/4 − 2C_0 (uv)^(1/2) or
ϑ > ϑ_b′ + η/4 + 2C_0 (uv)^(1/2), and at those with u < u_K and v < v_K (that clause being empty when u_K = 0 or v_K =
0). In particular it equals the background where ϑ ≤ ϑ_a − η or ϑ ≥ ϑ_b + η.

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
near the background's. For cone data that carry dust and are not small the theorem asserts nothing; [[thm:civp-large]]
develops them on a neighbourhood that depends on the data. For vacuum data of any size [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]) gives a development near the two cones, with neither uniqueness in the gauge nor
localisation. (ii) *The axes.* The band avoids the axes, and by (b) so does the perturbation in the development. The
proof uses the augmented system of [[sec:class-augmented]] only where it is local, off the axes; the dusts of the
background, which reach the axes, are carried there by the background itself. For data whose perturbation reaches an axis
this fails: at an axis the augmented system is not local, its Cauchy theory ([[thm:class-stability]]) needs lateral
boundaries adapted to the dust, and no domain-of-dependence statement with null boundaries near an axis is proved in this
paper. No development is asserted for such data, and (d) gives uniqueness near the axes only among solutions that equal
the background there. (iii) *Regularity.* The data are smooth and near the background's in C^m, m = 6k + 21. Densities
that are only bounded, or measures (shells), are not covered. For the 3 + 1 problem with two families of null dust,
possibly measure-valued, [LR20, Theorem 4.6, p. 29] states: "Given a strongly angularly regular reduced characteristic
initial data set … there exists ε > 0 sufficiently small such that whenever u_∗ ∈ (0, I] and u̲_∗ ∈ (0, ε], there exists
a unique angularly regular weak solution to the Einstein–null dust system … in the domain [0, u_∗] × [0, u̲_∗] × S² which
achieves the prescribed initial data." (iv) *The domain.* The development is asserted on G_*, a neighbourhood of the two
cones, and not on the whole rectangle [0, u_1] × [0, v_1]; in particular not where the two dusts cross away from the
cones.

[[thm:loc-cone-development]] develops these cone data, completed on 𝒞_in by [[lem:loc-cone-in]], when they are near the
background's and their band avoids the axes, with or without dust: on the explicit neighbourhood G_* of the two cones
there is a class solution in the gauge [[eq:loc-double-null]] that induces them, with an estimate, equal to the
background outside a slightly wider band and unique in the gauge near the background off the axes. Every small
perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2}, and every small density
added in the band, supported away from the axes, is of this kind, with v_1 = 4.5 and u_1 = 7.2 ([[lem:loc-cone-strips]]
(c)). Without smallness, these cone data, completed on 𝒞_in in the gauge b = 0 ([[def:civp-large-data]]), have a
development in the gauge [[eq:loc-double-null]] on a neighbourhood {min(u, v) ≤ δ} of the two cones whenever their band
avoids the axes; among them, with v_1 = 4.5 and u_1 = 7.2, are every perturbation of the shell or of the packet, or of
both, and every density added in the band, of any amplitude for which e^ϕ stays positive, and such perturbations exist
of every amplitude ([[lem:civp-large-free]], [[lem:civp-large-rectangle]]). That development equals the background
outside a slightly wider band and is unique in the gauge among solutions that equal the background near the axes
([[thm:civp-large]]); the number δ depends on the data. For vacuum data of any size, before the shell (v_1 < 3) and on
𝒞_in before the packet (u_1 < 5.7), a development near the two cones exists also by [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]), which gives neither uniqueness in the gauge nor localisation. No development is
asserted for cone data that differ from the background's near an axis, for data of finite regularity or for densities
that are not smooth, and no other result of this paper uses these developments.

### The development of the cone data {#sec:loc-cone-proof}

This section proves [[thm:loc-cone-development]], and, with the same proof, a development near any corner sphere for cone
data of any size on a small rectangle, the edges being first extended by a fixed length ([[lem:loc-cone-extension]],
[[prop:loc-cone-local]]). The method is Rendall's reduction of the characteristic problem to the Cauchy problem ([Ren90,
p. 221]: "A method is described by means of which the characteristic initial value problem can be reduced to the Cauchy
problem …"), carried out for the augmented system of [[sec:class-augmented]] off the axes. First, the double-null
equations determine every derivative of the metric functions and the densities across the two cones by linear ordinary
differential equations along the generators, and the derivatives so found agree at the corner sphere
([[lem:loc-cone-jets]]). A smooth extension with these derivatives is a formal solution: its residual in every equation
vanishes to infinite order on the cones ([[prop:loc-cone-formal]]); the constraints that the data satisfy on the cones
propagate to all orders by the contracted Bianchi identity. In a wave-map gauge whose reference metric is that extension,
the gauge condition holds identically for the extension. The Cauchy problem for the augmented system, with the formal
solution's residual as a forcing term to the past of the cones and a cut-off near the axes, where the solution is the
background, is solved by [[thm:class-kato-stability]] (a) ([[lem:loc-cone-cauchy]]). To the past of the cones the
solution is the formal solution ([[lem:loc-cone-past]]); so it takes the data, and the gauge condition and the
constraints hold to infinite order on the cones, and then everywhere to their future ([[lem:loc-cone-constraints]]). The
two phases and an angle transported along the outgoing generators are double-null coordinates in which the solution takes
the given data ([[lem:loc-cone-gauge]]), and two solutions in the gauge are compared through a wave map
([[lem:loc-cone-unique]]).

#### The setting {#sec:loc-cone-setting}

*Corners and edges.* Let l_u, l_v > 0 and δ_1 ∈ (0, min(l_u, l_v)/2], and translate u and v so that the corner is
(0, 0). Put N_o := {0} × [0, l_v + δ_1], N_i := [0, l_u + δ_1] × {0}, N := N_o ∪ N_i, the corner sphere S_c := {(0, 0)} ×
S³, F := {u ≥ 0, v ≥ 0}, P := {u < 0} ∪ {v < 0} and

    𝒮 := {(u, v) : −δ_1 ≤ u ≤ l_u + δ_1, −δ_1 ≤ v ≤ l_v + δ_1, min(u, v) ≤ δ_1}.                {#eq:loc-cone-collar}

Points of the (u, v)-plane stand for the corresponding spheres; a set of points is identified with its product with S³. A
*background* on 𝒮 is a round metric g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with σ_e and R_e smooth on 𝒮 and R_e > 0, together
with smooth profiles 𝒜(v), ℬ(u) ≥ 0, such that on 𝒮 ∩ F it solves the two-null-dust equations [[eq:two-dust-limit]],
Ric(g_e) = (𝒜/R_e³) dv ⊗ dv + (ℬ/R_e³) du ⊗ du. Its double-null functions are Ω_e² = e^(2σ_e)/2, γ_ϑ = R_e², A_c = ln(R_e
cos ϑ), A_s = ln(R_e sin ϑ), b = 0, and its densities are q̊_in := 𝒜/R_e³ and q̊_out := ℬ/R_e³; so ρ̊_in := 𝒱q̊_in = 𝒜(v)
sin ϑ cos ϑ and ρ̊_out := ℬ(u) sin ϑ cos ϑ, with 𝒱 of [[sec:loc-cone-equations-frame]]. A *class solution in the gauge*
on a set D × S³, D ⊂ F, is a smooth class solution of [[eq:class-system]] with two families, phases v and u and densities
q_in and q_out, so that Ric(g) = q_in dv ⊗ dv + q_out du ⊗ du, whose metric has the form [[eq:loc-double-null]] with Ω,
γ_ϑ, b, A_c, A_s smooth functions of (u, v, ϑ) ∈ D × (0, π/2), equal to the background's near ϑ = 0 and ϑ = π/2.

**Definition {#def:loc-cone-data}** (Cone data at a corner.) Let a background on 𝒮 be given and k ≥ 6. *Cone data* are
smooth functions ln Ω, ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, b and q_in ≥ 0 of (v, ϑ) ∈ [0, l_v + δ_1] × (0, π/2) on N_o
and ln Ω, ϰ_1, ϰ_2, ϰ_3, b and q_out ≥ 0 of (u, ϑ) ∈ [0, l_u + δ_1] × (0, π/2) on N_i, such that: (i) ln Ω, the ϰ_i and b
of the two edges agree on S_c; (ii) Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o, the left sides being given by
[[eq:loc-cone]] in terms of the functions on N_o, and Ric(L̲, L̲) = q_out on N_i, L̲ := ∂_u + b∂_ϑ, the left side being
given by the last line of [[eq:loc-cone-frame-ricci]] in terms of the functions on N_i, L̲ being tangent to N_i; (iii)
for some numbers 0 < ϑ_a′ < ϑ_b′ < π/2 they equal the background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′]. Their *size* is
the largest absolute value of a derivative of order at most m_0 := 6k + 18 of their differences from the background's.
They are in the *normalised gauge* if b = 0 on N_i; then Ric(L̲, L̲) on N_i is [[eq:loc-cone-in]]. The data consist of
the gauge functions ln Ω on both edges and b on N_i, which are free, of the conformal data and densities, which are free,
and of the functions that (ii) determines; the corner values are arbitrary, subject to (i). Cone data *of any sign* are
defined in the same way without the conditions q_in ≥ 0 and q_out ≥ 0. Every statement of this section holds for them, a
class solution being read as a G-invariant solution of [[eq:class-system]] whose densities may take either sign, except
the sign of the densities, which [[lem:loc-cone-constraints]] states separately; they arise when data are extended beyond
the ends of the edges ([[lem:loc-cone-extension]]).

The data of [[thm:loc-cone-development]] are cone data at the corner S, with l_u = u_1, l_v = v_1: on 𝒞_out the functions
that [[prop:loc-cones]] determines from the free data extended to v ≤ v_1 + δ_1 by the background's, and on 𝒞_in those
that [[lem:loc-cone-in]] determines from the free data extended likewise to u ≤ u_1 + δ_1; the extended free data are
smooth, as K_out ⊂ [0, v_1) × (ϑ_a, ϑ_b) and K_in ⊂ [0, u_1) × (ϑ_a, ϑ_b). The background on 𝒮 is provided by the next
lemma.

**Lemma {#lem:loc-cone-strips}** (The background near the cones.) Let u_1, v_1, R_min and C_0 be as in
[[thm:loc-cone-development]].

(a) There is δ_1 ∈ (0, min(u_1, v_1)/2] such that the background of [[sec:bg-data]] is defined and smooth on the strips
S_out := [0, δ_1] × [0, v_1 + δ_1] and S_in := [0, u_1 + δ_1] × [0, δ_1], with R > a and 2e^σ/R ≤ C_0 there.

(b) Decreasing δ_1, there are smooth functions σ_e, R_e on the set 𝒮 of [[eq:loc-cone-collar]] (with l_u = u_1, l_v =
v_1) equal to σ, R on S_out ∪ S_in = 𝒮 ∩ F, with R_e > a/2 and e^(σ_e)/R_e ≤ C_0 on 𝒮. So g_e := −2e^(2σ_e) du dv +
R_e² dΩ₃², with the profiles 𝒜 and ℬ of [[eq:bg-profiles]], is a background on 𝒮.

(c) R ≥ 5 on 𝒞_out, and R > 1.5 on 𝒞_in ∩ {u ≤ 7.2}.

*Proof.* (a) By [[lem:two-dust-reparametrisation]] (b), [[prop:two-dust-background]] holds in the coordinates of
[[sec:bg-data]]: the set G of its part (d) is closed in Q = [0, ∞) × [0, V1′] (V1′ the image of V1, with V1 chosen so
large that V1′ > v_1 + 1), its boundary in Q lies in {R = a}, and the background is smooth on G. A point p of the segment
𝒞_in ∩ {u ≤ u_1} lies in G, since J⁻(p) is the part of 𝒞_in with u ≤ u(p), where R ≥ R_min > a, and it is not on the
boundary of G in Q, since R(p) > a. So p is an interior point of G relative to Q; the same holds on 𝒞_out ∩ {v ≤ v_1},
and by continuity on the slightly longer segments, R > a there. By compactness a strip of some width δ_1 along each
segment lies in G. On the cones e^(2σ) = 1/2, so 2e^σ/R = √2/R ≤ √2/R_min = C_0/2 on the segments, and 2e^σ/R ≤ C_0 on
the strips once δ_1 is small.

(b) Apply [[lem:loc-cone-borel]] below, with r := 0, to the derivatives ∂_u^j σ, ∂_u^j R on {u = 0} and ∂_v^k σ, ∂_v^k R
on {v = 0}, one-sided where the strips end; they agree at the corner, being derivatives of functions smooth on
S_out ∪ S_in. The function equal to σ on S_out ∪ S_in and to the extension on 𝒮 ∖ F has, from both sides, the same
derivatives of every order on N, so it is smooth; likewise for R. By continuity R_e > a/2 and e^(σ_e)/R_e ≤ C_0 on 𝒮
after decreasing δ_1, since 2e^σ/R ≤ C_0 on S_out ∪ S_in.

(c) On 𝒞_out, e^(2σ) = 1/2 is constant, so [[eq:bg-field]] gives R_vv = −𝒜/(3R²), with R = 5 and R_v = 1/2 at v = 0 and 0
≤ 𝒜 ≤ 3.6 supported in [3, 4.5] (the bump β is at most 1). While R ≥ 5 on [0, v], R_v(v) ≥ 1/2 − (3.6 × 1.5)/(3 × 25) =
0.428 > 0; so R increases, and R ≥ 5 on all of 𝒞_out. On 𝒞_in, R = 5 − 0.47u ≥ 2.321 for u ≤ u1 = 5.7, as ℬ = 0 there
([[lem:bg-reduction]] (a)), and R > 1.5 for 5.7 ≤ u ≤ 7.2 ([[sec:loc-setting]], from [[prop:bg-nprime]]). ∎

For [[prop:loc-cone-local]] the background on 𝒮 is the restriction of a background on a larger open set, which need solve
the equations only to the future of the least corner; for instance that of this chapter where it is defined on a
rectangle with a corner at S, σ and R being extended across the two cones as in (b). The proofs below use of it only the
properties listed above and a number C_* ≥ sup over 𝒮 of e^(σ_e)/R_e, for which C_0 serves in
[[thm:loc-cone-development]].

#### The equations in the double-null gauge {#sec:loc-cone-equations-frame}

Let g have the form [[eq:loc-double-null]] off the axes, with ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, and put

    L̲ := ∂_u + b ∂_ϑ,   𝒱 := e^(ϰ_1 + ϰ_2 + ϰ_3),   ϖ := ∂_ϑ ln Ω,   ζ := (γ_ϑ/(4Ω²)) ∂_v b,
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
    ∇_L̲ ∂_v = (2Ω²/γ_ϑ)(ϖ − ζ) ∂_ϑ,      ∇_(∂_v) L̲ = (2Ω²/γ_ϑ)(ϖ + ζ) ∂_ϑ,
    ∇_L̲ ∂_ϑ = (ϖ − ζ) L̲ + (L̲ϰ_1) ∂_ϑ,      ∇_(∂_ϑ) L̲ = (ϖ − ζ) L̲ + χ̲_1 ∂_ϑ,
    ∇_(∂_v) ∂_ϑ = ∇_(∂_ϑ) ∂_v = (ϖ + ζ) ∂_v + χ_1 ∂_ϑ,
    ∇_(∂_ϑ) ∂_ϑ = (γ_ϑ/(2Ω²))(χ_1 L̲ + χ̲_1 ∂_v) + (∂_ϑϰ_1) ∂_ϑ,
    ∇_X K_i = ∇_(K_i) X = (Xϰ_(i+1)) K_i  (X = L̲, ∂_v, ∂_ϑ),      ∇_(K_1) K_2 = ∇_(K_2) K_1 = 0,
    ∇_(K_i) K_i = e^(2ϰ_(i+1)) ((2Ω²)⁻¹ (χ_(i+1) L̲ + χ̲_(i+1) ∂_v) − γ_ϑ⁻¹ (∂_ϑϰ_(i+1)) ∂_ϑ),

where L̲ϰ_(i+1) = χ̲_(i+1) and ∂_vϰ_(i+1) = χ_(i+1).

*Proof.* Each entry is Koszul's formula 2g(∇_X Y, Z) = X g(Y, Z) + Y g(Z, X) − Z g(X, Y) + g([X, Y], Z) − g([Y, Z], X) +
g([Z, X], Y), with X, Y, Z in the frame, the products and brackets above, and the fact that the products depend on (u, v,
ϑ) only. For instance 2g(∇_L̲ L̲, ∂_v) = 2L̲ g(L̲, ∂_v) + 2g([∂_v, L̲], L̲) = −4L̲Ω², while g(∇_L̲ L̲, Z) = 0 for Z = L̲,
∂_ϑ, K_i, which gives the first entry; and 2g(∇_L̲ ∂_v, ∂_ϑ) = L̲ g(∂_v, ∂_ϑ) + ∂_v g(∂_ϑ, L̲) − ∂_ϑ g(L̲, ∂_v) + g([L̲,
∂_v], ∂_ϑ) − g([∂_v, ∂_ϑ], L̲) + g([∂_ϑ, L̲], ∂_v) = 4Ω²ϖ − γ_ϑ ∂_v b, while 2g(∇_L̲ ∂_v, Z) = 0 for the other frame
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
                 − Σ_(i=2,3) (∂_ϑ²ϰ_i + (∂_ϑϰ_i)² − ∂_ϑϰ_1 ∂_ϑϰ_i) − 2 (∂_ϑϖ + ϖ² − ∂_ϑϰ_1 ϖ),
    E(L̲, ∂_v) = −2 ∂_v L̲ ln Ω − ∂_v tr χ̲ − Σ_i χ_i χ̲_i + (2Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 ∂_v b) − (γ_ϑ/(4Ω²)) (∂_v b)²
                 + 𝒱⁻¹ ∂_ϑ(𝒱 γ_ϑ⁻¹ ∂_ϑ Ω²),
    E(L̲, ∂_ϑ) = −(γ_ϑ/(4Ω²)) (L̲∂_v b + (L̲ ln(γ_ϑ^(3/2) e^(A_c + A_s) Ω⁻²) + 2∂_ϑ b) ∂_v b) + r̲,
    r̲ := (ϖ + ∂_ϑϰ_2 + ∂_ϑϰ_3) χ̲_1 + (χ̲_2 + χ̲_3) ϖ − ∂_ϑ L̲ ln Ω − Σ_(i=2,3) (∂_ϑϰ_i χ̲_i + ∂_ϑχ̲_i),
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
    g(R(L̲, ∂_ϑ)∂_ϑ, ∂_v) + g(R(∂_v, ∂_ϑ)∂_ϑ, L̲) = 4Ω² (∂_ϑϖ + ϖ² − ∂_ϑϰ_1 ϖ) + (γ_ϑ²/(4Ω²)) (∂_v b)²
                                         − 2γ_ϑ (∂_v χ̲_1 + χ_1 χ̲_1 − ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b)),

and R(∂_ϑ, ∂_ϑ) = 0; summing gives E(∂_ϑ, ∂_ϑ), since χ_1χ̲_1 + ½ Σ_(i=2,3) (χ_1χ̲_i + χ̲_1χ_i) = ½(tr χ χ̲_1 + χ_1 tr
χ̲). Likewise R(L̲, L̲) = 0 and

    g(R(∂_v, L̲)∂_v, L̲) = 4Ω² ∂_v L̲ ln Ω − 4Ω⁴γ_ϑ⁻¹ ϖ² − 2Ω² ϖ ∂_v b + ¾ γ_ϑ (∂_v b)²,
    γ_ϑ⁻¹ g(R(∂_ϑ, L̲)∂_v, ∂_ϑ) = −(∂_v χ̲_1 + χ_1 χ̲_1) + ½ e^(−ϰ_1) ∂_ϑ(e^(ϰ_1) ∂_v b) + (γ_ϑ/(8Ω²)) (∂_v b)²
                                + 2Ω²γ_ϑ⁻¹ (∂_ϑϖ + ϖ² − ∂_ϑϰ_1 ϖ),
    e^(−2ϰ_(i+1)) g(R(K_i, L̲)∂_v, K_i) = −(∂_v χ̲_(i+1) + χ_(i+1) χ̲_(i+1)) + 2Ω²γ_ϑ⁻¹ ϖ ∂_ϑϰ_(i+1)
                                         + ½ ∂_ϑϰ_(i+1) ∂_v b;

summing gives E(L̲, ∂_v), since 2Ω²γ_ϑ⁻¹(∂_ϑϖ + 2ϖ² + ϖ ∂_ϑ(ϰ_2 + ϰ_3 − ϰ_1)) = 𝒱⁻¹∂_ϑ(𝒱γ_ϑ⁻¹∂_ϑΩ²) and
½ ∂_ϑ∂_v b + ½ ∂_v b ∂_ϑ ln 𝒱 + ϖ ∂_v b = (2Ω²𝒱)⁻¹ ∂_ϑ(Ω²𝒱 ∂_v b).

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
E)(∂_v, ∂_v) = L̲a − (4Ω²/γ_ϑ)(ϖ − ζ) β, (∇_(∂_v) E)(L̲, ∂_v) = −(2Ω²/γ_ϑ)(ϖ + ζ) β, (∇_(∂_ϑ) E)(∂_ϑ, ∂_v) = ∂_ϑβ −
(γ_ϑ/(2Ω²)) χ̲_1 a − (∂_ϑϰ_1 + ϖ + ζ) β and (∇_(K_i) E)(K_i, ∂_v) = −(e^(2ϰ_(i+1))/(2Ω²)) χ̲_(i+1) a + e^(2ϰ_(i+1))γ_ϑ⁻¹
∂_ϑϰ_(i+1) β, and 2γ_ϑ⁻¹ζ = (2Ω²)⁻¹ ∂_v b. Summing gives [[eq:loc-cone-bianchi]]. The last identity is the contracted
Bianchi identity div Ric = ½ d(tr_g Ric), with tr_g Ric = tr_g E + tr_g T = tr_g E. ∎

#### The formal solution {#sec:loc-cone-formal}

**Lemma {#lem:loc-cone-borel}** (Extension of derivatives given on two edges.) Let λ_u, λ_v > 0, Y ⊂ ℝ a closed interval,
a_j (j ≥ 0) smooth functions of (v, ϑ) on [0, λ_v] × Y and b_k (k ≥ 0) smooth functions of (u, ϑ) on [0, λ_u] × Y, with
∂_v^k a_j(0, ϑ) = ∂_u^j b_k(0, ϑ) =: c_(jk)(ϑ) for all j, k. Let r ≥ 0 be an integer and γ_0, ε_B ∈ (0, 1]. There is a
smooth function f on (−∞, λ_u] × (−∞, λ_v] × Y with ∂_u^j f(0, v, ϑ) = a_j(v, ϑ) for 0 ≤ v ≤ λ_v and ∂_v^k f(u, 0, ϑ) =
b_k(u, ϑ) for 0 ≤ u ≤ λ_u, for all j and k, such that:

(a) f vanishes outside {|u| ≤ 2ε_B, v ≥ −2ε_B} ∪ {|v| ≤ 2ε_B, u ≥ 0}, and at every ϑ at which all a_j and b_k vanish
identically; if all a_j vanish for v < v_K and all b_k for u < u_K, where u_K, v_K > 0, then f = 0 where u < u_K and
v < v_K;

(b) with C^r norms over the sets named, ‖f‖_(C^r) ≤ C (max_(j≤r) ‖a_j‖_(C^(2r)) + max_(k≤r) ‖b_k‖_(C^(2r))) + γ_0, C
depending only on r and ε_B.

*Proof.* Fix χ ∈ C^∞(ℝ) with 0 ≤ χ ≤ 1, χ = 1 on [−1, 1] and supp χ ⊂ (−2, 2). For 0 < ε ≤ 1 and integers i, j ≥
0, |∂_x^i(χ(x/ε) x^j)| ≤ C(i, j) ε^(j−i) when i ≤ j, since the derivatives of χ(x/ε) are ε^(−l) χ^(l)(x/ε) and vanish
for |x| ≥ 2ε. So for a smooth function h(z) of further variables z, the term χ(x/ε) x^j h(z)/j! has C^(j−1) norm at most
C(j) ε ‖h‖_(C^(j−1)) and, for ε = ε_B or j ≥ r, C^r norm at most C(r, j, ε_B) ‖h‖_(C^r). Given smooth h_j, choose ε_j :=
ε_B for j ≤ r and, for j > r, ε_j ≤ ε_B so small that the C^(j−1) norm of the j-th term is at most 2^(−j) γ_0. Then the
series Σ_j χ(x/ε_j) x^j h_j(z)/j! converges in every C^p, its terms of index above p + 1 having C^p norms at most 2^(−j)
γ_0; its sum B is smooth, may be differentiated termwise, and ∂_x^j B(0, z) = h_j(z), as χ = 1 near 0. Call B the Borel
sum of (h_j).

*Step 1.* For each j let ã_j := a_j on [0, λ_v] × Y and, for v < 0, ã_j := the Borel sum in v of (c_(jk))_k. All
one-sided v-derivatives of the two pieces at v = 0 are the c_(jk), so ã_j is smooth on (−∞, λ_v] × Y. *Step 2.* Let f_1
be the Borel sum in u of (ã_j)_j; then ∂_u^j f_1(0, v, ϑ) = ã_j(v, ϑ). *Step 3.* Termwise, ∂_v^k f_1(u, 0, ϑ) = Σ_j
χ(u/ε_j) u^j c_(jk)(ϑ)/j!, whose u-derivatives at u = 0 are the c_(jk). So d_k := b_k − ∂_v^k f_1(·, 0, ·) on [0, λ_u] ×
Y has all its u-derivatives zero at u = 0, and extended by 0 to u < 0 it is smooth. Let f := f_1 + the Borel sum in v of
(d_k)_k. Its u-derivatives at u = 0 are those of f_1, since every d_k vanishes for u ≤ 0, and ∂_v^k f(u, 0, ϑ) = ∂_v^k
f_1(u, 0, ϑ) + d_k(u, ϑ) = b_k(u, ϑ).

(a) f_1 vanishes for |u| ≥ 2ε_B and, ã_j vanishing for v ≤ −2ε_B, for v ≤ −2ε_B; the second sum vanishes for |v| ≥ 2ε_B
and for u < 0. The cut-offs depend on u and v only. If all a_j vanish for v < v_K, then all c_(jk) = 0, so ã_j = 0 for
v < v_K and f_1 = 0 there; and d_k = b_k vanishes for u < u_K.

(b) The terms of index at most r have the cut-off scale ε_B and C^r norms at most C(r, ε_B) times the C^r norms of ã_j,
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
on [0, l_v + δ_1] × (0, π/2) and b_k (k ≥ 0) on [0, l_u + δ_1] × (0, π/2), with values in ℝ⁷ and with a_0, b_0 as above,
such that a_j − å_j and b_k − b̊_k are smooth (å_j, b̊_k the derivatives of X̊) and, for every smooth X on a
neighbourhood of N in 𝒮 × (0, π/2) equal to X̊ near the axes and with ∂_u^j X(0, v, ϑ) = a_j(v, ϑ) and ∂_v^k X(u, 0, ϑ) =
b_k(u, ϑ) for all j and k, the metric g of the form [[eq:loc-double-null]] with the functions X and the densities
q_A := ρ_A/𝒱 satisfy: E′ of [[lem:loc-cone-ricci]] (c), ∂_u ρ_in + ∂_ϑ(b ρ_in) and ∂_v ρ_out vanish to infinite order
on N. Moreover:

(i) ∂_v^k a_j(0, ϑ) = ∂_u^j b_k(0, ϑ) for all j and k;

(ii) if the cone data equal the background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], so do all a_j and b_k; if they equal
the background's on N_o ∩ {v < v_K} and on N_i ∩ {u < u_K}, with u_K, v_K > 0, then a_j = å_j for v < v_K and b_k = b̊_k
for u < u_K;

(iii) if the size of the cone data is at most Λ, then ‖a_j − å_j‖_(C^(m_0−4j)) + ‖b_j − b̊_j‖_(C^(m_0−4j)) is at most C_j
times the size, for 4j ≤ m_0, C_j depending only on j, Λ, the lengths of the edges and the background;

(iv) every class solution in the gauge on D × S³, where D ⊂ F is a past set (with each (u, v) it contains [0, u] × [0,
v]) whose interior is dense in it, smooth up to N ∩ D, whose functions on N_o ∩ D and N_i ∩ D are the cone data, has
∂_u^j X = a_j on N_o ∩ D and ∂_v^k X = b_k on N_i ∩ D; in particular å_j and b̊_k are the derivatives of X̊ across N.

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
order on N ∩ D; so its derivatives across N ∩ D solve the equations above with the same initial values. ∎

**Proposition {#prop:loc-cone-formal}** (The formal solution.) Let the cone data have size at most Λ, equal the
background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], on N_o ∩ {v < v_K} and on N_i ∩ {u < u_K}, where u_K, v_K ∈ [0, ∞],
and let 0 < δ_e ≤ δ_1/4. There are smooth functions Δ = (Δ_l) of (u, v, ϑ) on 𝒮 × [0, π/2] such that, with X̂ := X̊ + Δ,
the metric Ĝ of the form [[eq:loc-double-null]] with the functions X̂, and q̂_A := ρ̂_A/𝒱̂:

(a) Δ vanishes outside {ϑ_a′ ≤ ϑ ≤ ϑ_b′} ∩ ({|u| ≤ 2δ_e, v ≥ −2δ_e} ∪ {|v| ≤ 2δ_e, u ≥ 0}) and where u < u_K and
v < v_K, and ‖Δ‖_(C^(k+3)) ≤ C times the size, C depending only on Λ, δ_e, k and the background;

(b) the derivatives of X̂ across N are the a_j and b_k of [[lem:loc-cone-jets]]; so Ĝ and q̂_A induce the cone data on N,
and Ĝ is a smooth G-invariant Lorentzian metric on 𝒮 × S³, equal to g_e near the axes, for which u and v are null;

(c) E := Ric(Ĝ) − q̂_in dv ⊗ dv − q̂_out du ⊗ du, ∂_u ρ̂_in + ∂_ϑ(b̂ ρ̂_in) and ∂_v ρ̂_out vanish to infinite order on N.

*Proof.* Apply [[lem:loc-cone-borel]] to each component of (a_j − å_j) and (b_k − b̊_k), with Y = [0, π/2], λ_u = l_u +
δ_1, λ_v = l_v + δ_1, r := k + 3, ε_B := δ_e and γ_0 := min(1, the size) (Δ := 0 if the size is 0); the compatibility at
the corner holds for the data and for the background by [[lem:loc-cone-jets]] (i). (a) follows from parts (a) and (b)
there and [[lem:loc-cone-jets]] (ii), (iii), since m_0 − 4(k + 3) = 2(k + 3). (b) The double-null form with Ω̂ > 0 and
γ̂_ϑ > 0 is Lorentzian, with g^(uu) = g^(vv) = 0. (c) E′ and the conservation laws vanish to infinite order on N by
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

The cone data, of size at most Λ, now equal the background's at the points with ϑ ∉ [2η, π/2 − 2η], for a number η ∈ (0,
π/8]; for [[thm:loc-cone-development]], η is the number there, and [ϑ_a′, ϑ_b′] ⊂ (ϑ_a, ϑ_b) ⊂ [4η, π/2 − 4η]. Two cases
are treated together: (I) small data, the size at most ε ≤ ε_0, and (II) data of any size Λ, with b = 0 on N_i, on a
small rectangle at the corner. In case (II) we truncate the edges, l_u = l_v := 2δ_1: by [[lem:loc-cone-jets]] the
derivatives across N near the corner do not depend on the data farther out.

*Constants, coordinates and regions.* Fix a number C_* ≥ sup_𝒮 e^(σ_e)/R_e (in case (I), C_* := C_0, admissible by
[[lem:loc-cone-strips]] (b); for [[prop:loc-cone-local]], C_* := sup_(Q′) e^(σ_e)/R_e), c_+ := (min(δ_1, η/C_*)/4)², κ :=
δ_1/(4(l_u + l_v + 1)), and fix δ_c ∈ (0, √c_+/8]. On {u > −δ_c, v > −δ_c} put

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
Lorentzian metric close enough to g_e in C⁰. Every metric of the form [[eq:loc-double-null]] has g^(uu) = g^(vv) = 0 and
g^(uv) < 0, so dτ, du + κdv and dv + κdu are timelike for it and positive on ∂_τ; so these pieces are also spacelike,
with 𝒰 to their past, for every Lorentzian metric close enough in C⁰ to Ĝ below, which case (II) uses. On 𝒰, 2C_* e^(τ/2)
≤ 2C_*√c_+ ≤ η/2, and the corner sphere S_c, where τ = 2 ln δ_c, lies in 𝒰, with F ∩ 𝒰 ⊂ {τ ≥ 2 ln δ_c}.

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

*The reference metric in case (II).* In case (II) let b = 0 on N_i; then b = 0 on S_c, by (i) of [[def:loc-cone-data]].
We show that there is C_b, depending only on Λ, k and the background, and not on δ_e or δ_c, such that |b̂| ≤
C_b(|u| + |v|) on 𝒮, |b̂| ≤ C_b|v| where u ≥ 2δ_e, and |X̂ − X̊| ≤ C_b. In the proof of [[lem:loc-cone-borel]], with
ε_B = δ_e and r = k + 3, take the b-component. The term of index 0 of f_1 is χ(u/δ_e) ã_0, where ã_0 = b on N_o, with |b|
≤ Λ|v| there as b = 0 at v = 0, and for v < 0 ã_0 is the Borel sum of the c_(0k), with c_(00) = 0, so at most C|v|. Every
term of f_1 of index j ≥ 1 vanishes at u = 0 and is at most |u| sup |ã_j| for j ≤ r, as |u| ≤ 2ε_j ≤ 1/2 on its support,
and at most 2^(−j) γ_0 |u| for j > r, its C¹ norm being at most 2^(−j) γ_0. In the second sum d_0 = b_0 − f_1(·, 0, ·) =
0, since b_0 = 0 and the c_(j0) are the u-derivatives of b_0 at the corner; so each of its terms vanishes at v = 0 and is
at most C|v| in the same way. And f_1 vanishes where |u| ≥ 2δ_e. The constants are sums of the suprema of the a_j, b_k
and c_(jk) with j, k ≤ r, bounded by [[lem:loc-cone-jets]] (iii), and of γ_0 ≤ 1; none contains δ_e, since |χ| ≤ 1 and
2ε_j ≤ 1. The same terms give |X̂ − X̊| ≤ C_b for the other components. So at the points of supp Δ with |u| ≤ 2δ_e, where
u + δ_c ≤ 5δ_c/4 and v + δ_c ≥ 3δ_c/4, |b̂| ≤ 2C_b(v + δ_c), and at those with u ≥ 2δ_e, where |v| ≤ 2δ_e, |b̂| ≤ C_b
δ_c/4; with u + δ_c ≤ 4δ_1 and v + δ_c ≤ 4δ_1 on 𝒮, in both cases γ̂_ϑ b̂² (u + δ_c) ≤ 20 γ̂_ϑ C_b² δ_1² (v + δ_c), and

    4Ĝ(∂_τ, ∂_τ) = −4Ω̂² (u + δ_c)(v + δ_c) + γ̂_ϑ b̂² (u + δ_c)² ≤ −2Ω̂² (u + δ_c)(v + δ_c)

on the chart, b̂ vanishing off supp Δ, whenever δ_1 ≤ δ_2 := (e^(−4C_b) inf Ω_e²/(10 C_b² sup R_e²))^(1/2), the infimum
and the supremum over 𝒮 (for [[prop:loc-cone-local]], over Q′), which is at most (inf Ω̂²/(10 C_b² sup γ̂_ϑ))^(1/2)
by |X̂ − X̊| ≤ C_b; δ_2 depends only on Λ, k and the background. Then ∂_τ is future timelike for Ĝ, so the block Ĝ^(ab)
of the inverse metric on the dy^a, which annihilate ∂_τ, is positive definite (a covector ω with ω(∂_τ) = 0 has Ĝ⁻¹(ω,
ω) = Ĝ(ω^♯, ω^♯) > 0, as ω^♯ is orthogonal to the timelike ∂_τ); dτ is timelike for Ĝ and P̂_A(τ) > 0; so A^0(x, 𝐔̂) of
the system below is positive definite, without smallness of the data.

*The modified system.* Let 𝒜(U) = 0 denote the augmented system (Aug1)–(Aug4) of [[sec:class-augmented]] for the
unknowns U = (g, p_A, Θ_A, q_A), A ∈ {in, out}, with ζ_A := 1 and with the reduced Ricci tensor and the gauge vector
relative to Ĝ, D(g) := g^(ab)(Γ[g] − Γ[Ĝ])_(ab), in place of g̊; it is defined where g(K_i, K_i) > 0, in particular on
supp χ. In the first-order form of Step 9 of the proof of [[thm:class-stability-off-axes]], in the chart (τ, y), with the
variables 𝐔 := (g, g_τ, g_a, p_A, Θ_A, q_A) for (g, ∂_τ g, ∂_(y^a) g, …), it reads A^μ(x, 𝐔) ∂_μ𝐔 = F_0(x, 𝐔): the wave
block is ∂_τ g − g_τ = 0, a row with −g^(ττ) ∂_τ g_τ − 2g^(τa) ∂_a g_τ − g^(ab) ∂_a g_b, and g^(ab)(∂_τ g_b − ∂_b g_τ) =
0, so that A^0 = diag(1, −g^(ττ), g^(ab)) there and P_A^τ on the transports. The coefficients are smooth functions of x
and 𝐔 on the states with g Lorentzian, dτ and ∂_τ timelike and P_A^τ > 0, x entering through Ĝ and its derivatives
of order at most two ([[eq:gauge]] with Ĝ in place of g0).

In case (I) let 𝐔_c := 𝐔̊, in case (II) 𝐔_c := 𝐔̂ (the centre); A^0(x, 𝐔_c) is positive definite for x ∈ supp χ, in case
(I) as at 𝐔̊, g_e being Lorentzian with dτ and ∂_τ timelike and P̊_A(τ) > 0, and in case (II) by the paragraph on the
reference metric. Let c_0, r_0 > 0 be such that A^0(x, 𝐔_c + w) ≥ 2c_0 I for x ∈ supp χ and |w| ≤ 2r_0, and ϒ smooth with
ϒ(w) = w for |w| ≤ r_0 and |ϒ| ≤ 2r_0. Let A^μ_♭ be the first-order form, in the same variables, of the linear operator
−½ h^(ab) ∂_a∂_b on the wave block and of the transports P̄_A·∂, where h⁻¹ := χ_♭ g_e⁻¹ + (1 − χ_♭)(−∂_τ ⊗ ∂_τ + Σ_a
∂_(y^a) ⊗ ∂_(y^a)) and P̄_A := χ_♭ P̊_A + (1 − χ_♭) ∂_τ, χ_♭ a smooth function of (u, v) equal to 1 on supp χ_𝒰 and
supported in the chart and in 𝒮; on supp χ_𝒰, A^μ_♭ = A^μ(x, 𝐔̊). Let B_♭ be the constant matrix with B_♭Z = (Z_(g_τ), 0,
…, 0), Z_(g_τ) the component of Z in the place of g_τ, so that the first row of A^μ_♭ ∂_μ Z − B_♭Z is ∂_τ Z_g − Z_(g_τ),
as in Step 9. For Z := 𝐔 − 𝐔̊ put

    𝔄_χ(𝐔) := χ (A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) ∂_μ𝐔 − F_0(x, 𝐔_c + ϒ(𝐔 − 𝐔_c))) + (1 − χ)(A^μ_♭ ∂_μ Z − B_♭Z),
    F̃ := (1 − θ 1_F) 𝔄_χ(Û),                                                                    {#eq:loc-cone-modified}

1_F the indicator function of F. 𝔄_χ(𝐔) involves 𝐔̊ only where χ ≠ 0, so 𝔄_χ(𝐔) = F̃ is a system for Z on
[τ_init, τ_+] × ℝ⁴.

**Lemma {#lem:loc-cone-system}** (The modified system.) In case (I) let ε be small, in case (II) σ ≤ σ_1.

(a) 𝔄_χ(𝐔) = F̃ has the form A^μ_χ(x, Z) ∂_μ Z = Φ(x, Z) of [[eq:class-kato-system]] on [τ_init, τ_+] × ℝ⁴, with A^μ_χ :=
χ A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) + (1 − χ) A^μ_♭ symmetric, A^0_χ ≥ c_1 I with c_1 > 0, and Φ a local forcing term in the sense
of [[rem:class-kato-local]]. Every derivative of the A^μ_χ and of Φ is bounded on bounded sets of Z, and their bounds of
order k + 1, and c_1, depend only on Λ, η, k, δ_c and the background.

(b) Where χ = 1 and |𝐔 − 𝐔_c| ≤ r_0, 𝔄_χ(𝐔) = 𝒜(𝐔); at the points of 𝒰 where χ = 0, 𝔄_χ(𝐔) = A^μ(x, 𝐔̊) ∂_μ(𝐔 − 𝐔̊) −
B_♭(𝐔 − 𝐔̊).

(c) The first and the third row of the wave block of 𝔄_χ(𝐔) = F̃ are ∂_τ g − g_τ = 0 and h_χ^(ab)(∂_τ g_b − ∂_b g_τ) = 0,
with h_χ^(ab) positive definite; so g_τ = ∂_τ g and g_a = ∂_a g hold on [τ_init, τ_+] × ℝ⁴ if they hold at τ_init.

(d) 𝔄_χ(Û) = F̃ on P; F̃ is smooth and supported in supp χ_𝒰.

(e) R_I := 𝔄_χ(Ů) − F̃ and R_II := 𝔄_χ(Û) − F̃ are smooth, supported in supp χ_𝒰, and sup_τ ‖R_I(τ)‖_(H^k) ≤ C ε in case
(I), sup_τ ‖R_II(τ)‖_(H^k) ≤ C σ in case (II), with C depending on Λ in case (II). On 𝒰, F̃ − 𝔄_χ(Ů) vanishes outside K.

*Proof.* (a) A^μ_χ is a convex combination of the matrices of two systems of the form of Step 9, both symmetric; A^0 of
the first is at least 2c_0 I on supp χ for all Z, by the choice of ϒ, and A^0_♭ = diag(1, −h^(ττ), h^(ab), P̄_A^τ) is
positive definite, with a lower bound c_♭ > 0 on bounded sets of x and equal to the identity far out; so c_1 := min(2c_0,
c_♭) serves. Φ(x, Z) := χ (F_0(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) − A^μ(x, 𝐔_c + ϒ(𝐔 − 𝐔_c)) ∂_μ𝐔̊) + (1 − χ) B_♭Z + F̃(x) is smooth in
(x, Z), with every derivative bounded on bounded sets of Z, and Φ(x, 0) vanishes for x outside the compact set supp χ_𝒰,
by (d); so [[rem:class-kato-local]] applies. Its bounds involve Ĝ in C^(k+3), and ‖Δ‖_(C^(k+3)) ≤ C(Λ) by
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

(e) R_I = 𝔄_χ(Ů) − 𝔄_χ(Û) + θ 1_F 𝔄_χ(Û). 𝔄_χ is a smooth function of (x, 𝐔, ∂𝐔), so the first difference is bounded in
C^k by C‖𝐔̂ − 𝐔̊‖_(C^(k+1)) ≤ C‖Δ‖_(C^(k+2)) ≤ Cε. On F ∩ supp θ, 𝔄_χ(Û) = χ(𝒜(Û) − 𝒜(Ů)) + χ𝒜(Ů); there 𝒜(Ů) has only
the residual of (Aug1), Ric^H_Ĝ(g_e) − Ric^H_(g_e)(g_e), Ů solving the background's system on F ∩ 𝒮 (with
[[eq:class-raychaudhuri]] for (Aug3)); so it is bounded in C^k by C‖Ĝ − g_e‖_(C^(k+2)) ≤ Cε, and as θ 1_F 𝔄_χ(Û) is
smooth its C^k norm is at most Cε. In case (II), R_II = θ 1_F χ 𝒜(Û). Let x ∈ F ∩ supp θ, with u ≤ v say, so that u ≤
10σ; all derivatives of 𝒜(Û) vanish at (0, v, ϑ) ∈ N_o, so by Taylor's formula in u each derivative of 𝒜(Û) of order at
most k − p is at most C(Λ) u^(p+1) ≤ C(Λ)(10σ)^(p+1) at x, C(Λ) bounding the derivatives of order k + 1 of 𝒜(Û), hence
those of order k + 3 of Ĝ. The derivatives of order p of θ are at most Cσ^(−p). By Leibniz's rule each derivative of
order at most k of R_II is at most C(Λ)σ, and R_II is supported in the bounded set (−2σ, 10σ)² × S³; the chart (τ, y) has
bounded derivatives there. Finally, on 𝒰 ∖ K: on P, F̃ − 𝔄_χ(Ů) = 𝔄_χ(Û) − 𝔄_χ(Ů) = 0; on F, it is −θ 𝔄_χ(Ů), and
𝔄_χ(Ů) = 0 at each point of F ∩ 𝒰 ∖ K, where Ĝ = g_e on a neighbourhood and Ů solves its own system on F ∩ 𝒮. ∎

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
[[thm:class-kato-stability]] (a), with d = 4, s = k and ρ = ∞, to the system for Z of [[lem:loc-cone-system]] (a), with ū
:= 0 and u0 := 0: ū satisfies [[eq:class-kato-approximate]] with R := −Φ(x, 0) = 𝔄_χ(Ů) − F̃ = R_I, since 𝔄_χ(Ů) = χ𝒜(Ů).
(F1)–(F3) and (F1′) hold by [[rem:class-kato-local]]; ‖R_I(t)‖_(H^k) ≤ Cε ≤ 1 and sup_t ‖R_I‖ ≤ ε_0′ for ε small; and the
constants depend only on bounds of order k for the coefficients and on sup_t ‖Φ(t, ·, 0)‖_(H^k)
([[rem:class-kato-local]], the paragraph after it), which are uniform. So Z exists on [0, T], with sup_t ‖Z‖ ≤ Cε and
sup_t ‖Z‖_(H^(s′)) ≤ C ε^(1/(4k)) for s′ := k − 1/4 > 3; so sup |Z| ≤ C ε^(1/(4k)) ≤ r_0 for ε small, and the cut-off ϒ
is not active. For the bound in H^k, Z solves the linear problem of [[lem:class-kato-linear]] with v := Z and f := Φ(x,
Z) − Φ(x, 0) − R_I, and ‖Φ(·, Z) − Φ(·, 0)‖_(H^k) ≤ C‖Z‖_(H^k) by [[lem:class-composition]] (b); by part (a) of that
lemma Z is the solution of its part (b), whose bound and Gronwall's inequality give sup_t ‖Z‖_(H^k) ≤ C sup_t ‖R_I‖_(H^k)
≤ Cε. In case (II) write the system for Z̃ := 𝐔 − 𝐔̂ and apply the same theorem with ū := 0, u0 := 0 (𝐔̂ = 𝐔̊ near
Σ_init) and R := R_II, whose H^k norm is at most C(Λ)σ by [[lem:loc-cone-system]] (e); the constants depend on Λ through
the bounds of the coefficients near 𝐔̂, and not on σ, the system and T being fixed apart from F̃. For σ small this gives
the solution with ‖Z̃‖_(H^(s′)) ≤ C(Λ)σ^(1/(4k)), and ‖Z̃‖_(W^(1,∞)) ≤ C‖Z̃‖_(H^(s′)). The solution is smooth by the
argument of step (4) of the proof of [[cor:class-kato-sphere]] ([[thm:class-kato]] (a) at every order and
[[lem:class-kato-linear]] (c)), F̃ being smooth with compact support. The rows of (c) of [[lem:loc-cone-system]] hold at
τ_init, where 𝐔 = 𝐔̊. The system is invariant under G: χ, θ, the reference states, h and P̄_A are G-invariant, and G acts
on the components of 𝐔 in the chart (τ, y) by orthogonal maps fixing 𝐔_c, which preserve |𝐔 − 𝐔_c| ≤ r_0, where ϒ is the
identity. So the image of the solution under an element of G is a solution with the same data, and by the uniqueness in
[[thm:class-kato]] (a) it is the solution: U is G-invariant. ∎

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
u_in = v and u_out = u on P ∩ 𝒰; and (g, u_in, u_out, q_in, q_out) solves [[eq:class-system]] on F ∩ 𝒰_σ, with densities
of either sign for cone data of any sign, Ric(g) = q_in du_in ⊗ du_in + q_out du_out ⊗ du_out, in the gauge D(g) = 0
relative to Ĝ. If the densities of the data are nonnegative on N_o ∩ {v ≤ v̄} and on N_i ∩ {u ≤ ū}, then q_in ≥ 0 where
u_in ≤ v̄ and q_out ≥ 0 where u_out ≤ ū; for cone data, q_A ≥ 0 on F ∩ 𝒰_σ.

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

and D solves [[eq:class-gauge-wave]] with B_g T = Σ_A Δ_A q_A p_A, the tensor L being built with Γ[g] − Γ[Ĝ]; on 𝒪_2 all
these quantities vanish. In the first-order variables z := (D, ∂_τ D, ∂_y D, Δ_in, Δ_out) this is a linear system 𝐀^μ ∂_μ
z = Mz on F ∩ 𝒰_σ, of the form of Step 9 with the inverse metric g and the transport fields P_A, with C¹ coefficients.
Apply [[lem:loc-cone-energy]] on the closure of F ∩ 𝒰_σ with B_0 := N ∩ 𝒰_σ, where z = 0, and B_1 the future face and the
far cuts, spacelike for g with future conormals positive on the P_A. So D = 0 and Δ_A = 0 on F ∩ 𝒰_σ. Then (Aug1) is
Ric(g) = Σ_A q_A p_A ⊗ p_A, by the identity of the proof of [[lem:gauge-propagation]] with Ĝ in place of g0, and (Aug4)
with Θ_A = div_g P_A is div_g(q_A P_A) = 0; on 𝒪_2 this is the background. *The signs.* By (Aug4), q_A is multiplied
along each integral curve of P_A by a positive factor, and P_A(u_A) = −g⁻¹(du_A, du_A) = 0. So q_A at a point of F ∩ 𝒰_σ
is a positive multiple of its value at the point of N on the same integral curve, where u_A has the same value, and there
q_A is that of Û. On N_o, where u_in = v, q_in is the data's; on N_i, where u_in = 0, it is a positive multiple of its
value at the corner, as L̲ρ̂_in = −(∂_ϑ b̂) ρ̂_in along the generators of N_i. Likewise q_out is the data's on N_i, where
u_out = u, and on N_o, where u_out = 0, ρ̂_out is constant on each generator, so q_out is a positive multiple of its
value at the corner. This gives the signs. ∎

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

*Ψ is near the identity.* In case (I), sup |𝐔 − 𝐔̊| + |∂(𝐔 − 𝐔̊)| ≤ Cε, and the derivatives of order at most k − 3 of 𝐔 −
𝐔̊ are at most Cε, by [[lem:loc-cone-cauchy]] and the Sobolev inequality on the slices; in case (II) the same holds for 𝐔
− 𝐔̂ with C(Λ)σ^(1/(4k)) in place of Cε, at the order one. As d(u_out − u) = −(p_out − p̊_out) and d(u_in − v) = −(p_in −
p̊_in), and ϑ′ − ϑ solves P_out(ϑ′ − ϑ) = −(P_out − P̊_out)(ϑ) with zero values on P (in case (II) with P̂ in place of
P̊), Ψ − id is small in C¹ on F ∩ 𝒰_σ, in case (I) at most Cε in C^(k−3). In case (II), Ψ − id vanishes on N and every
point of F ∩ 𝒰_σ ⊂ [0, 6σ]² is joined to N in it by a segment of length at most 6σ, so |Ψ − id| ≤ 6σ sup |d(Ψ − id)| ≤
C(Λ) σ^(1 + 1/(4k)), while the points within σ of [0, σ]² lie in 𝒰_σ, as (δ_c + 2σ)² bounds (u + δ_c)(v + δ_c) there. The
set F ∩ 𝒰_σ is a down-set in (u, v): with (u, v) it contains [0, u] × [0, v]; so two of its points are joined in it by a
path of length at most 3 times their distance, through the point of least coordinates, and the bound on d(Ψ − id) makes Ψ
injective. Ψ is the identity on P ∩ 𝒰, where u_out = u, u_in = v and ϑ′ = ϑ, and on the sets of [[lem:loc-cone-support]].
Let y be a point of G_* (in case (II), of [0, σ]²) and B the closed ball about y of radius 2 sup |Ψ − id|, in the
coordinates (u, v, ϑ), with Ψ = id where ϑ ∉ [η, π/2 − η]; B lies in 𝒰′ for ε (for σ) small, and x ↦ y − (Ψ(x) − x) maps
B into B and is a contraction, sup |d(Ψ − id)| being less than 1/2. Its fixed point x satisfies Ψ(x) = y, and x lies in F
∩ 𝒰_σ, since Ψ fixes the points of P ∩ 𝒰. So the image of Ψ contains G_* (in case (II), [0, σ]²).

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
of order at most k at the points with 2η ≤ ϑ ≤ π/2 − 2η. For ε and ε_2 small, depending only on the background, u_1, v_1,
the band and k, it equals the solution of [[lem:loc-cone-gauge]], in their coordinates, at the points of G_* with 3η ≤ ϑ
≤ π/2 − 3η.

*Proof.* (1) *An extension of g′.* By [[lem:loc-cone-jets]] (iv), G_* being a past set, the functions of g′, like those
of Ĝ, have the derivatives a_j, b_k across N ∩ G_*; so g′ − Ĝ vanishes to infinite order on N ∩ G_*. Let G_*^+ be the set
of the points of 𝒰 within distance δ_c/4 of G_*, and fix ψ smooth on [0, π/2], equal to 1 on [17η/8, π/2 − 17η/8] and
supported in (2η, π/2 − 2η). The function f equal to ψ (g′ − Ĝ) on G_* and to 0 on P is smooth on G_* ∪ P; extend it
to G_*^+, for each ϑ, by the operator of [[thm:std-sy-extension]] for a bounded Lipschitz domain that contains G_* ∪ (P ∩
G_*^+) and lies in G_* ∪ P, and put g″ := Ĝ + f on G_*^+. Then g″ is smooth, equals Ĝ on P ∩ G_*^+ and g′ at the points
of G_* with 17η/8 ≤ ϑ ≤ π/2 − 17η/8, g″ − Ĝ vanishes to infinite order on N ∩ G_*^+, being smooth and zero on P there,
and ‖g″ − Ĝ‖_(C^(k−1)) ≤ C (ε + ε_2), the operator being bounded on W^(k,∞).

(2) *A wave map.* Let 𝒟′ be the set of the points of G_* with 9η/4 + 2C_* e^(τ/2) ≤ ϑ ≤ π/2 − 9η/4 − 2C_* e^(τ/2), τ of
[[eq:loc-cone-time]]; as G_* ⊂ F ∩ 𝒰, 2C_* e^(τ/2) ≤ η/2 there, so 𝒟′ contains the points of G_* with 3η ≤ ϑ ≤ π/2 − 3η,
and g″ = g′ on 𝒟′. Seek Φ = id + φ with id: (𝒟′, (Φ⁻¹)^*g″) → Ĝ a wave map, that is

    g″^(μν) (∂_μ∂_ν Φ^λ − Γ[g″]^ρ_(μν) ∂_ρ Φ^λ + Γ[Ĝ]^λ_(αβ)(Φ) ∂_μΦ^α ∂_νΦ^β) = 0,

a semilinear wave system for φ whose principal part is that of g″. As in [[lem:loc-cone-system]] and
[[lem:loc-cone-cauchy]], case (I), on the slab [τ_init, τ_+] × ℝ⁴, with a cut-off in ϑ equal to 1 on [9η/4, π/2 − 9η/4]
and supported in (17η/8, π/2 − 17η/8), a cut-off in (u, v) equal to 1 near G_* and supported in G_*^+, and the frozen
part taken with the wave operator of g_e: φ := 0 satisfies the cut-off system on P exactly, as g″ = Ĝ there, and on F up
to the residual 1_F g″^(μν)(Γ[Ĝ] − Γ[g″])^λ_(μν), which vanishes to infinite order on N and is at most C(ε + ε_2) in
C^(k−2). [[thm:class-kato-stability]] (a) with s = k − 2 > 3 gives a smooth solution φ on the slab with φ small in
W^(1,∞), the constants depending only on the background, u_1, v_1, the band, k and δ_c; φ = 0 on P, by the argument of
[[lem:loc-cone-past]]; and on 𝒟′ it solves the wave map system, the cut-offs being 1 there.

(3) *Comparison.* For ε, ε_2 small, Φ is a diffeomorphism near the identity, equal to it on P and so, with all
derivatives, on N. Put g̃ := (Φ⁻¹)^*g″, ũ_A := u′_A ∘ Φ⁻¹ with u′_in := v, u′_out := u the phases of g′, p̃_A := −dũ_A,
Θ̃_A := div_(g̃) P̃_A and q̃_A := q′_A ∘ Φ⁻¹ on Φ(𝒟′). Then D(g̃) = 0 relative to Ĝ, so (g̃, p̃_A, Θ̃_A, q̃_A) solves 𝒜 =
0 on Φ(𝒟′) (off the axes, with [[eq:class-raychaudhuri]] for (Aug3)), and so does U on F ∩ 𝒰 ∩ {η < ϑ < π/2 − η}, which
contains Φ(𝒟′) ([[lem:loc-cone-constraints]]). Both equal Û, with all derivatives, on N. The difference z of their
first-order variables satisfies A^μ(x, 𝐔̃) ∂_μ z = Mz on Φ(𝒟′), with the matrices of 𝐔̃, whose wave block has the inverse
metric g̃ and whose transport fields are P̃_A. The faces of 𝒟′ other than N are {uv = δ_*²}, {u = u_1}, {v = v_1} and two
angular faces. As g′ has the form [[eq:loc-double-null]] in these coordinates, the conormal v du + u dv of the first is
timelike for it, g′⁻¹(v du + u dv, v du + u dv) = 2uv g′^(uv) < 0; du and dv are null, du vanishes on −g′⁻¹du and is
positive on −g′⁻¹dv, and dv vanishes on −g′⁻¹dv and is positive on −g′⁻¹du; the angular conormals are timelike as in
[[lem:loc-cone-support]], g′ being C⁰-close to g_e there, and positive on −g′⁻¹du and −g′⁻¹dv. Φ carries g′ on 𝒟′ to g̃
and the phases of g′ to the ũ_A, so the outward conormals of the faces of Φ(𝒟′) other than N are future causal for g̃ and
nonnegative on P̃_in and P̃_out. [[lem:loc-cone-energy]] on Φ(𝒟′), with B_0 := N ∩ 𝒟′ and B_1 its other faces, gives
z = 0.

(4) *Conclusion.* So g = (Φ⁻¹)^*g″, p_A = p̃_A, and u_A = ũ_A, both being u or v on P. Hence Φ is an isometry from (g′,
u, v) to (g, u_out, u_in) on 𝒟′: u = u_out ∘ Φ and v = u_in ∘ Φ. It carries g′⁻¹du to g⁻¹du_out, so ϑ′ ∘ Φ is constant
along the integral curves of g′⁻¹du and equals ϑ on N_i, where Φ is the identity; as the angle of g′ has the same two
properties, ϑ′ ∘ Φ = ϑ. So Ψ ∘ Φ is the identity on 𝒟′, and the functions of g′ on 𝒟′ are those of the solution of
[[lem:loc-cone-gauge]]. ∎

**Lemma {#lem:loc-cone-extension}** (Extending cone data beyond the ends of the edges.) Let a background be given on 𝒮, k
≥ 6, η ∈ (0, π/8] and p := m_0 + 3. Let 0 < l_v′ ≤ l_v + δ_1 and 0 < l_u′ ≤ l_u + δ_1, and let functions as in
[[def:loc-cone-data]] be given on {0} × [0, l_v′] and on [0, l_u′] × {0}, with b = 0 on the second, that satisfy (i) and
(ii) there, equal the background's at the points with ϑ ∉ [2η, π/2 − 2η], and whose differences from the background's
have derivatives of order at most 2p bounded by Λ. There are λ_e ∈ (0, 1/2] and C, depending only on Λ, η, k and bounds
for σ_e, R_e, 1/R_e and their derivatives of order at most 2p + 2 on 𝒮, such that, if l_v + δ_1 ≤ l_v′ + λ_e and l_u +
δ_1 ≤ l_u′ + λ_e, the functions extend to cone data of any sign on N_o and N_i, with b = 0 on N_i, equal to the
background's at the points with ϑ ∉ [2η, π/2 − 2η], of size at most C. Beyond l_v′ and l_u′ the extended densities may be
negative.

*Proof.* We treat N_o; on N_i the same argument applies with u, q_out and [[eq:loc-cone-in]] in place of v, q_in and the
first line of [[eq:loc-cone]], b = 0 being kept: with b = 0, L̲ = ∂_u, χ̲_i = ∂_uϰ_i, and the last line of
[[eq:loc-cone-frame-ricci]] is the right side of [[eq:loc-cone-in]] minus q_out, for every Ω. If l_v′ = l_v + δ_1 there
is nothing to do. Write ϕ := (ϰ_1 + ϰ_2 + ϰ_3)/3 and ℓ_i := ϰ_i − ϕ. By the proof of [[prop:loc-cones]], whose
derivation does not use that Ω is the background's, (ii) on N_o says that y := e^ϕ solves

    y″ − 2(ln Ω)′ y′ + (1/3)(Σ_i (ℓ_i′)² + q_in) y = 0,      ′ := ∂_v,                                     (∗)

and that ∂_v b solves the linear first-order equation that the second line of [[eq:loc-cone]] gives, Ric(∂_v, ∂_ϑ) = 0,
whose leading coefficient is γ_ϑ/(4Ω²), whose other coefficient holds first derivatives of ln Ω and the ϰ_i, and whose
inhomogeneous term is −r of [[eq:loc-cone-r]], which holds derivatives of order at most two of ln Ω and the ϰ_i.

*The free functions.* For f one of ln Ω, ℓ_1, ℓ_2, ℓ_3 and q_in, with background value f̊, let B_f be the Borel sum in t
:= v − l_v′ of the sequence h_j := ∂_v^j(f − f̊)(l_v′, ·), j ≥ 0, as in the proof of [[lem:loc-cone-borel]], with ε_j :=
1/4 for j ≤ p and ε_j ≤ 1/4 for j > p so small that the j-th term has C^p norm at most 2^(−j). Put f̃ := f on [0, l_v′]
and f̃ := f̊ + B_f on [l_v′, l_v + δ_1]. All v-derivatives of the two pieces agree at v = l_v′, so f̃ is smooth; f̃ = f̊
at every ϑ at which f = f̊ on the given segment, since there all h_j vanish; and a term of index j ≤ p has C^p norm at
most C(p) ‖h_j‖_(C^p) ≤ C(p) ‖f − f̊‖_(C^(2p)), so ‖f̃ − f̊‖_(C^p) ≤ C(p)(p + 1)Λ + 1 =: Λ_2 on the edge. Nothing keeps
q̃_in nonnegative beyond l_v′.

*The constrained functions.* Let C_1 ≥ 1 bound 2|(ln Ω̃)′| + (1/3)|Σ_i (ℓ̃_i′)² + q̃_in| on N_o; it depends only on Λ_2
and the background. Solve (∗), with these coefficients, on [0, l_v + δ_1] with the values of y and y′ at v = 0; by
uniqueness the solution is the given y on [0, l_v′], and it is smooth, its coefficients being smooth. At a point of the
band, on [l_v′, l_v′ + a] with a ≤ 1, w := |y| + |y′| satisfies |w′| ≤ (1 + C_1) w, so w ≤ 2w(l_v′) for a ≤ ln 2/(1 +
C_1), and then |y − y(l_v′)| ≤ 2a w(l_v′) = 2a (1 + |ϕ′(l_v′)|) y(l_v′) ≤ y(l_v′)/2 for a ≤ 1/(4(1 + |ϕ′(l_v′)|)),
where |ϕ′| ≤ Λ + sup |∂_v ln R_e|. Let λ_e be the least of 1/2, ln 2/(1 + C_1) and 1/(4(1 + Λ + sup |∂_v ln R_e|)). Then
y > 0 on [0, l_v + δ_1], and y ≥ y(l_v′)/2 on [l_v′, l_v + δ_1], at the points of the band, and we put ϕ̃ := ln y and
ϰ̃_i := ϕ̃ + ℓ̃_i. Next solve the equation for ∂_v b with the extended functions, and obtain b by integration from the
corner, on [0, l_v + δ_1]; again the solution is the given b on [0, l_v′], and it is smooth. At every ϑ ∉ [2η, π/2 − 2η]
the free functions and their ϑ-derivatives are the background's, so the coefficients of both equations are the
background's there, and with the background's values at v = 0 both solutions are the background's. The extended functions
satisfy (i), the corner being untouched, (ii), by construction, and (iii) with [ϑ_a′, ϑ_b′] := [2η, π/2 − 2η]; so they
are cone data of any sign.

*The size.* On the band, the coefficients of (∗) have C^(p−1) norms at most C(Λ_2), and at v = l_v′ the functions y, 1/y
and the derivatives of y of order at most 2p are bounded by C, since ϕ − ϕ̊ is bounded by Λ in C^(2p) and ϕ̊ = ln R_e +
(1/3) ln(sin ϑ cos ϑ) is bounded with its derivatives there. Differentiating (∗) in ϑ, ∂_ϑ^i y solves an equation of the
form (∗) with an inhomogeneous term in the ∂_ϑ^(i′) y, i′ < i; Gronwall's inequality over [l_v′, l_v + δ_1], of length at
most λ_e ≤ 1/2, bounds ∂_ϑ^i y and ∂_ϑ^i y′ for i ≤ p − 1, and (∗) then bounds the further v-derivatives. So
‖y‖_(C^(p−1)) ≤ C, and with y ≥ y(l_v′)/2, ‖ϕ̃ − ϕ̊‖_(C^(p−1)) ≤ C. The equation for ∂_v b then has its coefficients in
C^(p−2) and its inhomogeneous term in C^(p−3) = C^(m_0), and the same argument gives ‖b̃‖_(C^(m_0)) ≤ C. So the size of
the extension is at most C. ∎

**Proposition {#prop:loc-cone-local}** (Developments near a corner sphere, without smallness.) Let k ≥ 6, m_0 = 6k + 18,
m_1 := 2m_0 + 6 = 12k + 42, the regularity index of this proposition, η ∈ (0, π/8] and Λ > 0. Let 𝒪 be an open set of
the (u, v)-plane, Q ⊂ 𝒪 and d ∈ (0, 1] such that the set Q′ of the points (u, v) with |u − u″| ≤ 4d and |v − v″| ≤ 4d for
some (u″, v″) ∈ Q is a compact subset of 𝒪, and u_Q, v_Q the least values of u and v on Q. Let a background be given on
𝒪, that is a round metric g_e = −2e^(2σ_e) du dv + R_e² dΩ₃², with σ_e and R_e smooth on 𝒪 and R_e > 0, and profiles
𝒜(v), ℬ(u) ≥ 0, that solves [[eq:two-dust-limit]] on 𝒪 ∩ {u ≥ u_Q, v ≥ v_Q}. There is σ > 0, depending only on k, η,
Λ, d and
bounds for σ_e, R_e, 1/R_e and their derivatives of order at most m_1 + 2 on Q′, with the following property. Let a
rectangle [u_c, u_c + λ_u] × [v_c, v_c + λ_v] ⊂ Q be given, with any λ_u, λ_v > 0, N_o := {u_c} × [v_c, v_c + λ_v] and
N_i := [u_c, u_c + λ_u] × {v_c}. Let smooth functions ln Ω, ϰ_1 = ½ ln γ_ϑ, ϰ_2 = A_c, ϰ_3 = A_s, b and q_in ≥ 0 of (v,
ϑ) ∈ [v_c, v_c + λ_v] × (0, π/2), and ln Ω, ϰ_1, ϰ_2, ϰ_3 and q_out ≥ 0 of (u, ϑ) ∈ [u_c, u_c + λ_u] × (0, π/2), be
given, with b = 0 on N_i and with Ω on both edges and b on N_o otherwise arbitrary, that agree on the corner sphere,
satisfy Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o, by [[eq:loc-cone]], and Ric(∂_u, ∂_u) = q_out on N_i, by
[[eq:loc-cone-in]], which holds for every Ω when b = 0 ([[eq:loc-cone-frame-ricci]]), equal the background's at the
points with ϑ ∉ [2η, π/2 − 2η], and whose differences from the background's have C^(m_1) norms at most Λ. Then there is a
class solution in the gauge on [u_c, u_c + min(λ_u, σ)] × [v_c, v_c + min(λ_v, σ)] × S³ that induces these functions on
the two edges and equals the background, with its densities, at the points with ϑ ∉ [η, π/2 − η]. No smallness of the
data is assumed: the smallness of the rectangle takes its place. The number σ is the same for every corner (u_c, v_c) ∈ Q
and does not depend on λ_u, λ_v.

*Proof.* Translate u and v so that the corner is (0, 0), the background's profiles with them. Constants C below depend
only on the quantities named in the statement. For δ_1 ≤ d the set 𝒮 of [[eq:loc-cone-collar]] with l_u = l_v = 2δ_1 lies
in [−δ_1, 3δ_1]², hence in the translate of Q′, and 𝒮 ∩ F lies where u ≥ u_Q and v ≥ v_Q; so the background restricts to
a background on 𝒮, bounds on Q′ bound it there, and C_* := sup_(Q′) e^(σ_e)/R_e is admissible.

*Step 1: a collar of fixed width.* Let λ_e and C be the numbers of [[lem:loc-cone-extension]] for Λ, η, k and the bounds
on Q′, and Λ_1 := max(Λ, C). Let δ_2 be the number of the paragraph on the reference metric in case (II) in
[[sec:loc-cone-reduced]], for the size Λ_1. Fix δ_1 := min(d, λ_e/3, δ_2) and l_u = l_v := 2δ_1. So δ_1 depends only on
Λ, η, k, d and the background on Q′, and not on the corner or on λ_u, λ_v; it is not tied to the lengths of the given
edges.

*Step 2: the data on edges of length 3δ_1.* Restrict the given functions to {0} × [0, min(λ_v, 3δ_1)] and [0, min(λ_u,
3δ_1)] × {0}. Where an edge is shorter than 3δ_1, extend it by [[lem:loc-cone-extension]] with l_v′ := min(λ_v, 3δ_1) and
l_u′ := min(λ_u, 3δ_1); its hypothesis holds, as l_v + δ_1 = 3δ_1 ≤ λ_e ≤ l_v′ + λ_e, likewise for u, and 2p = m_1. This
gives cone data of any sign on N_o = {0} × [0, 3δ_1] and N_i = [0, 3δ_1] × {0}, with b = 0 on N_i, equal to the
background's at the points with ϑ ∉ [2η, π/2 − 2η], of size at most Λ_1 (a restriction has size at most Λ, as m_0 ≤ m_1),
and equal to the given functions on N_o ∩ {v ≤ λ_v} and on N_i ∩ {u ≤ λ_u}, where their densities are nonnegative.

*Step 3: the smallness of the rectangle in place of that of the data.* Apply case (II) of [[sec:loc-cone-reduced]] to
these data, with the size Λ_1 and δ_c := √c_+/8, which depends only on δ_1, η and C_*. [[lem:loc-cone-jets]] and
[[prop:loc-cone-formal]] use no smallness: they give the formal solution Û, whose residual 𝒜(Û) vanishes to infinite
order on N. Since δ_1 ≤ δ_2, Ĝ serves as the reference metric of the chart (τ, y) without smallness. Where case (I) uses
that the data are small, case (II) uses that σ is small: the Cauchy problem is posed about Û, not about the background,
and its residual R_II = θ 1_F χ 𝒜(Û) is at most C(Λ_1)σ in H^k ([[lem:loc-cone-system]] (e)), because 𝒜(Û) vanishes to
infinite order on N and θ is supported within 10σ of the corner; the closeness of the solution to Û that
[[lem:loc-cone-constraints]] and [[lem:loc-cone-gauge]] use is C(Λ_1)σ^(1/(4k)) ([[lem:loc-cone-cauchy]]). Let σ := σ_0
of [[lem:loc-cone-cauchy]], which depends only on Λ_1, η, k, δ_c and the background. Then [[lem:loc-cone-cauchy]],
[[lem:loc-cone-past]], [[lem:loc-cone-support]], [[lem:loc-cone-constraints]] and [[lem:loc-cone-gauge]] give, on Ψ(F ∩
𝒰_σ) ⊃ [0, σ]², a metric of the form [[eq:loc-double-null]] and densities, of either sign, that solve
[[eq:class-system]], induce the data of Step 2 on the two edges, and equal the background and its densities where ϑ <
3η/2 or ϑ > π/2 − 3η/2.

*Step 4: the rectangle.* On [0, min(λ_u, σ)] × [0, min(λ_v, σ)] the functions induced on the two edges are the given
ones. In the coordinates of [[lem:loc-cone-gauge]], u_in = v and u_out = u, so by [[lem:loc-cone-constraints]] q_in ≥ 0
where v ≤ λ_v and q_out ≥ 0 where u ≤ λ_u. So on this rectangle the densities are nonnegative, and the restriction is a
class solution in the gauge with the stated properties. Every choice above depends only on k, η, Λ, d and the background
on Q′. ∎

No uniqueness is stated for these developments; the uniqueness of [[thm:loc-cone-development]] (d) concerns data near the
background's.

**Remark {#rem:loc-cone-local-scope}** (What the size of the rectangle depends on.) The number σ of
[[prop:loc-cone-local]] depends on the data only through their C^(m_1) norms on the two edges, and not on the lengths
λ_u, λ_v, on the position of the corner in Q or on any smallness of the data: the edges are first cut, or extended by
solving the constraints along them, to the fixed length 3δ_1 ([[lem:loc-cone-extension]]). The extension loses half the
derivatives, which is why m_1 is about twice m_0. σ depends on the background through bounds on Q′, for three reasons,
which are why the proof needs a background and not only bounds on the data: near the axes the solution is the background,
since the augmented system is used only off the axes ([[rem:loc-cone-scope]] (ii)); the modified system
[[eq:loc-cone-modified]] takes the background's coefficients where its cut-off vanishes; and the localisation in angle
([[lem:loc-cone-support]]) uses the constant C_*. A shift b given on N_i is removed before the proposition is applied, by
the change of angle ϑ ↦ Φ(u, ϑ) with (∂_u + b∂_ϑ)Φ = 0 and Φ(0, ϑ) = ϑ on the edge N_i cut at length 3δ_1: it keeps the
form [[eq:loc-double-null]], with γ_ϑ replaced by γ_ϑ/(∂_ϑΦ)² and b by ∂_uΦ + b∂_ϑΦ, so that b becomes 0 on N_i and b −
b(0, 0, ϑ) on N_o; it is the identity on N_o and off the band; and the C^(m_1) norms of the new functions are bounded in
terms of the C^(m_1 + 1) norms of the old ones. A statement with no background, the data being prescribed up to the axes,
needs a local theory of the augmented system at the axes, with a domain of dependence for null boundaries there, and is
not given in this paper.

*Proof of [[thm:loc-cone-development]].* Take the background of [[lem:loc-cone-strips]] (b) on 𝒮, with l_u = u_1, l_v =
v_1, and C_* = C_0. The free data are ε-close to the background's in C^m, m = m_0 + 3 = 6k + 21. The equations of
[[prop:loc-cones]] and [[lem:loc-cone-in]] are linear ordinary differential equations along the generators whose
coefficients differ from the background's by at most Cε in C^(m−1); so for ε small e^ϕ stays within Cε of the
background's, positive, on [0, v_1 + δ_1] and [0, u_1 + δ_1], ϕ is within Cε of the background's in C^(m−1), and b in
C^(m−3), r of [[eq:loc-cone-r]] holding two derivatives of the data. So the cone data have size at most Cε, are in the
normalised gauge, and equal the background's at the points with ϑ ∉ [ϑ_a′, ϑ_b′], on 𝒞_out ∩ {v < v_K} and on 𝒞_in ∩ {u <
u_K} (the constraints there have the background's coefficients and corner values). In case (I) take δ_c so small also
that 2C_0 (δ_c(u_1 + v_1 + 1))^(1/2) ≤ η/4, a condition depending only on the background, u_1, v_1 and the band.
[[lem:loc-cone-cauchy]], case (I), [[lem:loc-cone-past]], [[lem:loc-cone-support]], [[lem:loc-cone-constraints]] and
[[lem:loc-cone-gauge]] give a solution with (a) and (c) on G_*. For (b): [[lem:loc-cone-support]] and the last part of
[[lem:loc-cone-gauge]] give the background at the points of G_* with ϑ < ϑ_a′ − 2C_* ((u + δ_c)(v + δ_c))^(1/2), with ϑ >
ϑ_b′ + 2C_* ((u + δ_c)(v + δ_c))^(1/2), or with u < u_K and v < v_K; on G_*, (u + δ_c)(v + δ_c) ≤ uv + δ_c(u_1 + v_1 +
1), so 2C_* ((u + δ_c)(v + δ_c))^(1/2) ≤ 2C_0 (uv)^(1/2) + η/4. As 2C_0 (uv)^(1/2) ≤ 2C_* δ_* ≤ η/4 on G_*, ϑ_a′ > ϑ_a
and ϑ_b′ < ϑ_b, the solution equals the background where ϑ < ϑ_a′ − η/2 or ϑ > ϑ_b′ + η/2, in particular where ϑ ≤ ϑ_a −
η or ϑ ≥ ϑ_b + η, and where ϑ < 3η or ϑ > π/2 − 3η. So (d) is [[lem:loc-cone-unique]] together with (b) for the solution
of (a). ∎

### Developments of cone data without smallness {#sec:civp-large}

This section develops the cone data of [[prop:loc-cones]] without smallness; for data near the background's the
development is that of [[thm:loc-cone-development]]. For cone data of any size that equal the background's outside a
band away from the axes, with or without dust, a development in the gauge [[eq:loc-double-null]] exists on a
neighbourhood {min(u, v) ≤ δ} of the two cones, which contains {uv ≤ δ²}; it equals the background outside a slightly
wider band, and it is unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]).
The number δ depends on the data. The route is that of Cabet, Chruściel and Tagne Wafo [CCTW16]. Off the axes,
[[prop:reduction]] turns the class system into a three-dimensional one for the conformal orbit metric h, two waves ψ and
ω and the two densities. In three dimensions the curvature is determined by the Ricci tensor, and the reduction
expresses the Ricci tensor through the densities and the first derivatives of ψ and ω. So in a double-null frame of h
the connection coefficients obey transport equations along the two null directions with no angular derivative of an
unknown on the right, and the waves become first-order systems of the same kind ([[lem:civp-large-frame]]). The
resulting evolution system has the doubly-null form of [CCTW16, (2.7)–(2.8)] ([[prop:civp-large-system]]), and once it
is localised in angle their theorem ([[thm:std-cctw-existence]], [[thm:std-cctw-strips]]) gives a solution on two strips
along the cones. That this solution solves the Einstein equations is shown by the device of the proof of [CCTW16,
Theorem 5.3, pp. 55–56], which builds the development up in the time u + v; where that proof solves Cauchy and mixed
problems, the local developments here are those near corner spheres ([[prop:civp-large-corner]]), each of which
coincides with the strip solution by an energy estimate ([[lem:civp-large-energy]]).

*Notation.* The background g0, the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the corner sphere S = 𝒞_out ∩ 𝒞_in and the
gauge [[eq:loc-double-null]] are those of [[sec:loc-cones]], and R is the area radius of g0. We fix u_1, v_1 > 0 such
that the background is defined and smooth on [0, u_1′] × [0, v_1′] for some u_1′ > u_1 and v_1′ > v_1, and put Q1 := [0,
u_1] × [0, v_1]; every u_1 ≤ 7.2 and every v_1 > 0 will do ([[lem:civp-large-rectangle]] (a)). On Q1 × S³, in the gauge
[[eq:loc-double-null]], b = 0, γ_ϑ = R², A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ), Ω is a function of (u, v), and
Ric(g0) = q̊_in dv ⊗ dv + q̊_out du ⊗ du ([[eq:two-dust-limit]]). We extend Ω and R smoothly across the two cones, as in
[[lem:civp-large-rectangle]] (a), to an open set 𝒪 of the (u, v)-plane that contains Q1 and on which Ω, R > 0; so g0 =
−4Ω² du dv + R² dΩ₃² is given on 𝒪 × S³ and solves [[eq:two-dust-limit]] at the points of 𝒪 with u, v ≥ 0. We fix a band
0 < ϑ_a < ϑ_b < π/2 and put

    η0 := (1/3) min(ϑ_a, π/2 − ϑ_b),      J0 := [ϑ_a − 2η0, ϑ_b + 2η0] ⊂ [η0, π/2 − η0].  {#eq:civp-large-band}

A set D ⊂ Q1 is a *past set* if [0, u] × [0, v] ⊂ D for every (u, v) ∈ D. Class solutions in the gauge on D × S³, D ⊂
Q1, are those of [[sec:loc-cone-setting]], with the corner at S and g0 as the background; their metrics equal g0 near
the axes, and so extend smoothly to them.

**Definition {#def:civp-large-data}** (Cone data on Q1.) *Cone data on Q1* consist of smooth functions Ω > 0, γ_ϑ > 0,
b, A_c, A_s and q_in ≥ 0 of (v, ϑ) ∈ [0, v_1] × (0, π/2) on 𝒞_out, and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ)
∈ [0, u_1] × (0, π/2) on 𝒞_in, with b = 0 on 𝒞_in, such that:

(i) the two sets of functions agree on S;

(ii) for the metric [[eq:loc-double-null]] that they define, Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on 𝒞_out, and
Ric(∂_u, ∂_u) = q_out on 𝒞_in (each side involves only the functions given on that cone: on 𝒞_out by
[[lem:loc-cone-equations]], on 𝒞_in by (F1′) of [[lem:civp-large-frame]] and [[prop:reduction]], since b vanishes
there);

(iii) they equal the background's outside compact sets K_out ⊂ [0, v_1] × (ϑ_a, ϑ_b) and K_in ⊂ [0, u_1] × (ϑ_a, ϑ_b).

[[prop:loc-cones]] and [[lem:loc-cone-in]] produce cone data on Q1 from free data whenever the conformal factors e^ϕ
that they determine stay positive, and no smallness is needed for that ([[lem:civp-large-free]]).

**Lemma {#lem:civp-large-free}** (Cone data on Q1 from free data.) Let free data (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0 on 𝒞_out ∩
{v ≤ v_1} be given as in [[prop:loc-cones]], and (ℓ_1, ℓ_2, ℓ_3) and q_out ≥ 0 on 𝒞_in ∩ {u ≤ u_1} as in
[[lem:loc-cone-in]], smooth, agreeing on S, and equal to the background's outside compact subsets of [0, v_1] × (ϑ_a,
ϑ_b) and of [0, u_1] × (ϑ_a, ϑ_b). On a generator of either cone let y := e^ϕ be the factor that the constraint
determines, ′ the derivative along the generator, L := v_1 on 𝒞_out and L := u_1 on 𝒞_in, ρ := Ω^(−2) and p := (1/3)(Σ_i
(ℓ_i′)² + q), with q := q_in on 𝒞_out and q := q_out on 𝒞_in, and let ẙ := e^(ϕ̊) and p̊ be the background's.

(a) If y > 0 on [0, L] on every generator of both cones, then the functions so determined, Ω, γ_ϑ = e^(2ϕ + 2ℓ_1), b,
A_c = ϕ + ℓ_2, A_s = ϕ + ℓ_3 and q_in on 𝒞_out, and Ω, γ_ϑ, A_c, A_s and q_out on 𝒞_in, with b = 0 there, are cone data
on Q1.

(b) On a generator put

    I := ∫_0^L ρ(s) (p − p̊)_+(s) ẙ(s)² ∫_s^L ρ(t)⁻¹ ẙ(t)^(−2) dt ds,      (p − p̊)_+ := max(p − p̊, 0).

If I < 1, then y ≥ (1 − I) ẙ > 0 on [0, L]. In particular y ≥ ẙ on a generator on which p ≤ p̊.

*Proof.* (b) By the first line of [[eq:loc-cone]] and by [[eq:loc-cone-in]], as in the proof of [[prop:loc-cones]], y
solves y″ − 2(ln Ω)′y′ + py = 0, that is (ρy′)′ + ρpy = 0, since ρ′ = −2(ln Ω)′ρ; the background's ẙ solves (ρẙ′)′ +
ρp̊ẙ = 0, Ω being the background's; and y and ẙ have the same value and the same derivative at the corner. Put p̃ :=
p̊ + (p − p̊)_+, so that p ≤ p̃, let z solve (ρz′)′ + ρp̃z = 0 with the same initial values, and put w := z/ẙ. Then
ρẙ²w′ = ρ(z′ẙ − zẙ′), so (ρẙ²w′)′ = −ρ(p − p̊)_+ẙ²w, with w(0) = 1 and w′(0) = 0. On an interval [0, t_0] on which w ≥ 0
this gives ρẙ²w′ ≤ 0, so w ≤ 1, and, exchanging the order of integration, for t ≤ t_0

    w(t) = 1 − ∫_0^t (ρẙ²)⁻¹(τ) ∫_0^τ (ρ(p − p̊)_+ẙ²w)(s) ds dτ
         ≥ 1 − ∫_0^t ρ(s) (p − p̊)_+(s) ẙ(s)² ∫_s^t (ρẙ²)⁻¹(τ) dτ ds ≥ 1 − I.

If w vanished somewhere on [0, L], this bound at its first zero would contradict I < 1; so w ≥ 1 − I on [0, L]. Next, W
:= ρ(y′z − yz′) vanishes at 0 and has W′ = (ρy′)′z − y(ρz′)′ = ρ(p̃ − p)yz. On an interval [0, t_1) on which y > 0,
therefore, W ≥ 0, (y/z)′ = W/(ρz²) ≥ 0 and y ≥ z. If y had a first zero t_1 ∈ (0, L], continuity would give y(t_1) ≥
z(t_1) > 0, which is absurd. So y ≥ z = wẙ ≥ (1 − I)ẙ on [0, L]. If p ≤ p̊, then I = 0.

(a) By [[prop:loc-cones]] and [[lem:loc-cone-in]], the constraints determine ϕ and b on 𝒞_out, and ϕ on 𝒞_in, on every
generator on which y > 0, as solutions of linear ordinary differential equations along the generators whose coefficients
and initial values depend smoothly on the angle; so the functions are smooth on [0, v_1] × (0, π/2) and on [0, u_1] ×
(0, π/2), and Ω, γ_ϑ > 0. Condition (i) of [[def:civp-large-data]] holds: on S the free data agree, ϕ and Ω are the
background's on both cones, and b vanishes on both, being the background's at v = 0 on 𝒞_out. Condition (ii) holds by
construction, since T = q_in dv ⊗ dv + q_out du ⊗ du gives T(∂_v, ∂_v) = q_in, T(∂_v, ∂_ϑ) = 0 and T(∂_u, ∂_u) = q_out.
For (iii) let [ϑ_a″, ϑ_b″] ⊂ (ϑ_a, ϑ_b) contain in its interior the angles of the two compact sets. [[prop:loc-cones]]
and [[lem:loc-cone-in]], applied with the band (ϑ_a″, ϑ_b″), give the background's functions at every ϑ ∉ [ϑ_a″, ϑ_b″];
so K_out := [0, v_1] × [ϑ_a″, ϑ_b″] and K_in := [0, u_1] × [ϑ_a″, ϑ_b″] serve. ∎

**Lemma {#lem:civp-large-rectangle}** (The background on a rectangle of the two cones.) Use the coordinates (u, v) of
[[sec:loc-setting]], let v_1 > 0, and let V1 in [[prop:two-dust-background]] be chosen so large that V1′ > v_1 + 1, as
in the proof of [[lem:loc-cone-strips]] (a).

(a) The rectangle [0, 7.2] × [0, v_1] lies in the set G of [[prop:two-dust-background]] (d), and R_v > 0 and R ≥
1.519357 on it. There is δ ∈ (0, 1/2) such that the background is defined and smooth on [0, 7.2 + 2δ] × [0, v_1 + 2δ],
and Ω and R extend to smooth positive functions on [−δ, 7.2 + δ] × [−δ, v_1 + δ].

(b) Let free data be given as in [[lem:civp-large-free]], with u_1 ≤ 7.2. On 𝒞_out the number I of
[[lem:civp-large-free]] (b) is at most ∫_0^(v_1) (v_1 − s) (p − p̊)_+(s) ds, and on 𝒞_in it is at most R(7.2, 0)^(−2)
∫_0^(u_1) R(s, 0)² (u_1 − s) (p − p̊)_+(s) ds, with R(7.2, 0)² ≥ 2.308; and p − p̊ = (1/3)(Σ_i (ℓ_i′)² + q − q̊), q̊ the
background's density. So e^ϕ stays positive on every generator of a cone in each of the following cases, and when it
does on both cones the free data give cone data on Q1 ([[lem:civp-large-free]] (a)), the conformal data (ℓ_1, ℓ_2, ℓ_3)
being the background's and c a smooth function of ϑ with compact support in (ϑ_a, ϑ_b): a density q − q̊ ≥ 0 added on
𝒞_out with supremum A on an interval of v of length l, if v_1 A l < 3, or on 𝒞_in with supremum A on an interval of u of
length l, if 26 A l ≤ 1; the density of the shell multiplied by 1 + c with −1 ≤ c ≤ 76, if v_1 = 4.5; and the density of
the packet multiplied by 1 + c with −1 ≤ c ≤ 4.5, if u_1 = 7.2. In particular there are such data with densities of
every amplitude.

*Proof.* (a) Let σ be the function of [[eq:bg-field]], e^(2σ) = 2Ω². By [[lem:two-dust-reparametrisation]] (b),
[[prop:two-dust-background]] holds in these coordinates (proof of [[lem:loc-cone-strips]] (a)): G is closed in Q = [0,
∞) × [0, V1′], its boundary in Q lies in {R = a}, a = 0.70, the background is smooth on G, and μ ≥ μ0 > 0 on G. G is a
past set, 𝒟 being one: for p ∈ G and p′ ∈ J⁻(p) = [0, u_p] × [0, v_p], p′ ∈ 𝒟 and J⁻(p′) ⊂ J⁻(p). By
[[eq:two-dust-evolution]] and [[eq:two-dust-mass]], which hold in these coordinates, σ_uv = 3(e^(2σ) + 2R_uR_v)/(2R²) =
(3/2)e^(2σ)μ/R⁴ > 0 on G, and σ = −(1/2) ln 2 on both cones; so σ(u, v) = −(1/2) ln 2 + ∫_0^u ∫_0^v σ_uv ≥ −(1/2) ln 2
on every rectangle J⁻(p), p ∈ G, that is 1/2 ≤ e^(2σ) and e^(−2σ) ≤ 2. Put λ := e^(−2σ)R_v. Then λ_v = −𝒜e^(−2σ)/(3R²)
([[lem:bg-identities]]) and λ(u, 0) = 2R_v(u, 0) = ℓ_v(u) ([[lem:bg-reduction]] (a)).

*On 𝒞_in.* There R″ = −ℬ/(3R²) ≤ 0, and R′ = −0.47 on [0, u1], u1 = 5.7 ([[lem:bg-reduction]] (a)), so R(·, 0)
decreases, and R(u, 0) ≥ R(u2, 0) ≥ 1.519357 for u ≤ u2 = 7.2 ([[prop:bg-nprime]] (i)). μ(·, 0) is 3/2 on [0, u1]
([[lem:bg-reduction]] (b)) and
at least μ3 > 0 on [u1, u2] ([[prop:bg-nprime]] (iii)), so ℓ_v′ = −μ/R³ < 0 on [0, 7.2] ([[eq:bg-nprime]]) and ℓ_v(u) ≥
ℓ_v(u2) ≥ 0.529533 for u ≤ 7.2 ([[prop:bg-nprime]] (iii)).

*At a point of G.* Let p ∈ G with u_p ≤ 7.2 and v_p ≤ v_1, and (u, v) ∈ J⁻(p). For v ≤ 3, 𝒜 = 0, so λ(u, v) = ℓ_v(u) ≥
0.529533 and R_v = e^(2σ)λ ≥ 0.264766. Hence R(u, v) ≥ R(u, 0) ≥ 1.519357 for v ≤ min(v_p, 3), and R(u, 3) ≥ 1.519357 +
3 × 0.264766 ≥ 2.3136 if v_p ≥ 3. If v_p > 3, let w be the supremum of the v ∈ [3, v_p] such that λ(u, ·) > 0 on [3, v];
λ(u, 3) > 0, so w > 3. On [3, w], R(u, ·) is nondecreasing, so R ≥ 2.3136, and since 𝒜 ≥ 0 vanishes outside [3, 4.5] and
∫_3^4.5 𝒜 = 2.7 K ≤ 3.25878, K := ∫_(−1)^1 β ≤ 1.2069549 ([[lem:margins-bump-table]] (a)),

    λ(u, v) = ℓ_v(u) − (1/3) ∫_3^v 𝒜 e^(−2σ)/R² ≥ 0.529533 − (2 × 3.25878)/(3 × 2.3136²) ≥ 0.1236.

By continuity w = v_p. So R_v = e^(2σ)λ > 0 on J⁻(p), and R ≥ R(u, 0) ≥ 1.519357 > a there; in particular R(p) > a, p is
not on the boundary of G in Q, and G contains a neighbourhood of p in Q.

*Conclusion.* So G ∩ Q_*, Q_* := [0, 7.2] × [0, v_1], is open in Q_*; it is closed in Q_*, G being closed in Q; and it
contains the corner, which lies in G, R being 5 there. Q_* is connected, so Q_* ⊂ G, and by the previous paragraph R_v >
0 and R ≥ 1.519357 on Q_*. The points of G with R > a are interior points of G in Q, so they form a set open in Q that
contains the compact Q_*, hence [0, 7.2 + 2δ] × [0, v_1 + 2δ] for some δ ∈ (0, 1/2); there the background is smooth,
solves [[eq:two-dust-limit]] and has R > a. [[lem:loc-cone-borel]], with r := 0, applied as in the proof of
[[lem:loc-cone-strips]] (b) to the derivatives of σ and of R on {0} × [0, v_1 + 2δ] and on [0, 7.2 + 2δ] × {0}, which do
not depend on ϑ, extends σ and R to smooth functions on (−∞, 7.2 + 2δ] × (−∞, v_1 + 2δ]; after decreasing δ, R > 0 on
[−δ, 7.2 + δ] × [−δ, v_1 + δ] by continuity, and Ω = e^σ/√2 > 0.

(b) On the cones e^(2σ) = 1/2, so Ω² = 1/4 and ρ = 4; and ẙ = R (sin ϑ cos ϑ)^(1/3), since ϕ̊ = (ϰ̊_1 + ϰ̊_2 + ϰ̊_3)/3
with ϰ̊_1 = ln R, ϰ̊_2 = ln(R cos ϑ), ϰ̊_3 = ln(R sin ϑ). So ρ and the angular factor cancel in I, and I = ∫_0^L (p −
p̊)_+(s) ∫_s^L (R(s)/R(t))² dt ds, R taken on the cone. On 𝒞_out, R increases and R ≥ 5 (proof of
[[lem:loc-cone-strips]] (c)), so the inner integral is at most L − s. On 𝒞_in, R decreases, so for s ≤ t ≤ u_1 ≤ 7.2 it
is at least R(7.2, 0) ≥ 1.519357, and the inner integral is at most (u_1 − s)R(s, 0)²/R(7.2, 0)². The background's
ℓ̊_i = ϰ̊_i − ϕ̊ depend on ϑ only, so ℓ̊_i′ = 0 and p − p̊ = (1/3)(Σ_i (ℓ_i′)² + q − q̊). With the conformal data the
background's, (p − p̊)_+ = (q − q̊)_+/3. For an added density on 𝒞_out, I ≤ v_1 · A l/3 < 1. On 𝒞_in, R(s, 0) ≤ 5, so I
≤ (25/2.308) · 7.2 · A l/3 ≤ 25.997 A l < 1. For the shell, q̊_in = 𝒜/R³ ≤ 𝒜/125 on 𝒞_out; at an angle with c ≤ 0, p ≤
p̊, and at one with 0 < c ≤ 76, I ≤ (1.5/3) · 76 · ∫_3^4.5 𝒜/125 ≤ 0.5 × 76 × 3.25878/125 < 0.991, since (q − q̊)_+ = c
q̊_in vanishes outside [3, 4.5] and v_1 − s ≤ 1.5 there. For the packet, q̊_out = ℬ/R³ with ℬ supported in [u1, u2] and
∫ ℬ = 1.275 K ≤ 1.53887; at an angle with 0 < c ≤ 4.5, I ≤ (4.5/3) · 1.5 · ∫ ℬ/(R(s, 0) R(7.2, 0)²) ds ≤ 2.25 ×
1.53887/(1.519357 × 2.308) < 0.988, and where c ≤ 0, p ≤ p̊. In each case [[lem:civp-large-free]] (b) gives e^ϕ > 0. A
density added on 𝒞_out with supremum A on an interval of length l < 3/(v_1 A) has amplitude A, for every A > 0. ∎

No step of the proof of [[thm:civp-large]] uses the two lemmas, the theorem taking cone data on Q1 as given. Data with
q_in = q_out = 0 are vacuum data.

*The small-data theorem.* [[thm:loc-cone-development]] is used only for comparison, in [[rem:civp-large-domain]] and
[[rem:civp-large-beyond]]. Its data are cone data on Q1 in the sense of [[def:civp-large-data]], with Ω the background's
on both cones, obtained by [[prop:loc-cones]] and [[lem:loc-cone-in]] from free data within ε_0 of the background's in
C^(6k+21) that equal the background's outside compact subsets of [0, v_1) × (ϑ_a, ϑ_b) and [0, u_1) × (ϑ_a, ϑ_b), with
u_1, v_1 as in that theorem; it gives a class solution in the gauge [[eq:loc-double-null]] on the explicit past set {uv
≤ δ_*²} ∩ Q1, times S³, that induces the data and equals (g0, q̊_in, q̊_out) where ϑ ≤ ϑ_a − 3η0/4 or ϑ ≥ ϑ_b + 3η0/4,
with an estimate of the solution, and its uniqueness in the gauge is stated near the background only.

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

with ∇ the connection of h and ∇_i := ∇_(e_i). These are not the quantities of the same names in [[sec:loc-cone-proof]].
We write Ric_ij := Ric[h](e_i, e_j) and, for a function F, e_iF for its derivative. The *exchange* is the map e3 ↔ e4, χ
↔ χ̲, η ↔ η̲, ϖ ↔ ϖ̲, ζ ↔ −ζ; it maps each definition above to another one.

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

The equations of the first five lines have ∂_v and govern f₄; those of the last four have D_3 and govern f₃.

**Proposition {#prop:civp-large-system}** (The doubly-null form.) Write [[eq:civp-large-system]] as A^u∂_uf + A^v∂_vf +
A^ϑ∂_ϑf = G(f) on ℝ² × Y, Y an interval or a circle, with the Euclidean scalar product on ℝ²³ and the flat connection
∂. Then A^u, A^v, A^ϑ are symmetric and smooth functions of f, G is a smooth function of f, and

    A^u = diag(I₁₀, 0),      A^v = diag(0, I₁₃),      A^ϑ = (b I₁₀, Q; Qᵀ, 0),  {#eq:civp-large-form}

in the splitting f = (f₃, f₄), where the 10 × 13 matrix Q has exactly four nonzero entries, each equal to −k =
−e^(α−β), at the pairs (ψ_4, ψ′_1), (ψ_1, ψ_3), (ω_4, ω′_1), (ω_1, ω_3), so that |Q| = e^(α−β) in the operator norm. In
particular the system has the form (2.7)–(2.8) of [CCTW16] ([[thm:std-cctw-existence]]), with A^u_ϕϕ = I₁₀ > 0 and
A^v_ψψ = I₁₃ > 0, the scalar product, and the flat connection as both ∇ and ∇̊, preserving the splitting. Moreover:

(a) if (g, v, u, q_in, q_out) is a class solution in the gauge on D × S³, its *reduced fields* (the connection
coefficients of h, the densities, α, β, b, and Ψ° = Ψ, Ψ_4 = e4Ψ, Ψ_3 = e3Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}) solve
[[eq:civp-large-system]] on D × (0, π/2);

(b) conversely, let f be a smooth solution of [[eq:civp-large-system]] on an open set U ⊂ D × (0, π/2) that is
*geometric* there: χ, χ̲, η, η̲, ϖ, ϖ̲ are the connection coefficients of the metric h of [[eq:civp-large-h]] built
from (α, β, b), Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ, and Ric[h] equals the tensor with the frame components
[[eq:civp-large-m]]; and let q_in, q_out ≥ 0 on U. Then g := e^(−2ψ) h + e^(ψ−2ω) dφ1² + e^(ψ+2ω) dφ2², with v, u,
q_in, q_out, is a solution of [[eq:class-system]] on U × T², of the form [[eq:loc-double-null]] with Ω = e^(α−ψ), γ_ϑ =
e^(2β−2ψ), A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2.

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
ℓ and ω in the roles of e3 and e4; there the first equations of (4.48) and (4.50) are misprinted, and with ϕ0 = ψ0 = h
they read ℓ(ϕ0) = ψ₋ and ω(ψ0) = ϕ₊, the forms used here. The equations (F4), (F5), their images and the relations of
[[eq:civp-large-coefficients]] for χ̲, ϖ̲ and η + η̲ are not part of the system; they hold for the reduced fields of a
solution, and they determine the data on the cones.

#### Data on the two cones {#sec:civp-large-data}

**Lemma {#lem:civp-large-data}** (The data of the evolution system.) (a) Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂
Q1 and let g, g′ be class solutions in the gauge on neighbourhoods of the two edges N_o := {u_c} × [v_c, v_c + l_v] and
N_i := [u_c, u_c + l_u] × {v_c} (times S³) that induce the same functions Ω, γ_ϑ, b, A_c, A_s, q_in on N_o and the same
Ω, γ_ϑ, b, A_c, A_s, q_out on N_i. Then their reduced fields have the same f₃-components on N_o and the same
f₄-components on N_i. More precisely, for the reduced fields of a class solution in the gauge: the values at the corner
sphere of all reduced fields are given by [[eq:civp-large-coefficients]] in the functions on N_o and N_i near it; on
N_o the f₃-components other than χ̲ are the functions on N_o and their derivatives along N_o, ϖ and η̲ through
[[eq:civp-large-coefficients]], and χ̲ solves (F4′) along N_o with M_11 in place of Ric_11; on N_i the f₄-components
other than η and χ are the functions on N_i and their derivatives along N_i, ϖ̲ through [[eq:civp-large-coefficients]],
and η and χ solve (F5) (with η̲ = 2e1α − η) and (F4) along the integral curves of e3 in N_i with M_31, M_11 in place of
Ric_31, Ric_11.

(b) Let cone data on Q1 be given. Define on 𝒞_out, from its functions and with α, β, ψ, ω as in [[eq:civp-large-h]],

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

**Lemma {#lem:civp-large-energy}** (Energy for systems in doubly-null form.) Let 𝒬 := [u_c, u_c + l_u] × [v_c, v_c +
l_v], let J = [ϑ₋, ϑ₊] be an interval, or an arc of a circle with a coordinate ϑ on it, and let z = (z₃, z₄), of class
C¹ on 𝒬 × J with values in ℝ^(N₃) × ℝ^(N₄), solve

    ∂_u z₃ + P ∂_ϑ z₃ + Q ∂_ϑ z₄ = B₃ z,      ∂_v z₄ + Qᵀ ∂_ϑ z₃ = B₄ z,  {#eq:civp-large-linear}

with P symmetric, P and Q of class C¹ and B₃, B₄ continuous on 𝒬 × J. Assume z₃ = 0 on {u_c} × [v_c, v_c + l_v] × J
and z₄ = 0 on [u_c, u_c + l_u] × {v_c} × J.

(a) Let |P| ≤ p and |Q| ≤ q on 𝒬 × J (operator norms), let t > 0, c1 := p + t, c2 := q²/t and w(u, v) := c1(u − u_c) +
c2(v − v_c). Then z = 0 at every point of 𝒬 × J with ϑ₋ + w(u, v) ≤ ϑ ≤ ϑ₊ − w(u, v).

(b) If z = 0 on 𝒬 × ([ϑ₋, ϑ₋ + ε] ∪ [ϑ₊ − ε, ϑ₊]) for some ε > 0, then z = 0 on 𝒬 × J.

*Proof.* Put A^u := diag(I, 0), A^v := diag(0, I) and A^ϑ := (P, Q; Qᵀ, 0), so that [[eq:civp-large-linear]] reads
A^μ∂_μz = Bz with B := (B₃; B₄), and for λ ≥ 0 let X^μ := e^(−λ(u+v)) ⟨z, A^μz⟩, μ ∈ {u, v, ϑ}, a C¹ vector field in
the coordinates (u, v, ϑ). Since the A^μ are symmetric and A^u, A^v are constant,

    ∂_μX^μ = e^(−λ(u+v)) (−λ ⟨z, (A^u + A^v)z⟩ + ⟨z, (∂_ϑA^ϑ)z⟩ + 2⟨z, Bz⟩) ≤ e^(−λ(u+v)) (C₁ − λ) |z|²,

with C₁ := sup_(𝒬×J) (|∂_ϑA^ϑ| + 2|B|), finite since 𝒬 × J is compact, and A^u + A^v = I. Fix λ > C₁.

(a) Fix (u′, v′) ∈ 𝒬 with ϑ₋ + w(u′, v′) ≤ ϑ₊ − w(u′, v′), and let W be the set of (u, v, ϑ) with u_c ≤ u ≤ u′,
v_c ≤ v ≤ v′ and ϑ₋ + w(u, v) ≤ ϑ ≤ ϑ₊ − w(u, v); since w increases in u and v, its sections are nonempty intervals,
and W is compact with a piecewise smooth boundary. By the divergence theorem ∫_W ∂_μX^μ = ∫_(∂W) X^μ ν_μ dS, with ν the
outer unit conormal. On the face u = u′, X^μν_μ = e^(−λ(u+v)) |z₃|² ≥ 0; on v = v′ it is e^(−λ(u+v)) |z₄|² ≥ 0; on
u = u_c and v = v_c it vanishes, since these faces lie in the sets where z₃, respectively z₄, vanish. On the face
ϑ = ϑ₊ − w the conormal is a positive multiple of dϑ + c1 du + c2 dv, and on ϑ = ϑ₋ + w one of −dϑ + c1 du + c2 dv, so
X^μν_μ is a positive multiple of e^(−λ(u+v)) ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩, and

    ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩ ≥ (c1 − p)|z₃|² − 2q|z₃||z₄| + c2|z₄|² = (t^(1/2)|z₃| − q t^(−1/2)|z₄|)² ≥ 0.

Hence 0 ≤ ∫_(∂W) X^μν_μ dS = ∫_W ∂_μX^μ ≤ (C₁ − λ) ∫_W e^(−λ(u+v)) |z|², so z = 0 on W, and in particular at (u′, v′)
for every ϑ with ϑ₋ + w ≤ ϑ ≤ ϑ₊ − w.

(b) Take W := [u_c, u′] × [v_c, v′] × J. The faces u = u′, v = v′, u = u_c, v = v_c contribute as in (a), and on the
faces ϑ = ϑ± the field X vanishes, since z does. The same inequality gives z = 0 on W. ∎

#### Local developments {#sec:civp-large-local}

**Proposition {#prop:civp-large-corner}** (Developments near a corner sphere, without smallness.) Let m := 114, the
regularity index m_1 = 12k + 42 of [[prop:loc-cone-local]] for k = 6, and κ ∈ (0, π/8]. For every Λ > 0 there is σ > 0
with the following property. Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ Q1, N_o := {u_c} × [v_c, v_c + l_v] and N_i
:= [u_c, u_c + l_u] × {v_c}. Let smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of (v, ϑ) ∈ [v_c, v_c + l_v]
× (0, π/2), and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) ∈ [u_c, u_c + l_u] × (0, π/2), with b = 0 on N_i, be
given that agree on the corner sphere, satisfy Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(∂_u, ∂_u) =
q_out on N_i, equal the background's at the points with ϑ ∉ [2κ, π/2 − 2κ], and whose differences from the background's,
with ln Ω, ln γ_ϑ in place of Ω, γ_ϑ, have C^m norms at most Λ. Then there is a class solution in the gauge on [u_c,
u_c + min(l_u, σ)] × [v_c, v_c + min(l_v, σ)] × S³ that induces these functions on the two edges and equals (g0, q̊_in,
q̊_out) at the points with ϑ ∉ [κ, π/2 − κ].

*Proof.* Choose d ∈ (0, 1] such that the open set 𝒪 of the notation at the beginning of this section contains the points
within 4d of Q1 in each coordinate. In the notation of [[prop:loc-cone-local]], with Q := Q1, k := 6, η := κ, λ_u := l_u
and λ_v := l_v, the background is g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with e^(2σ_e) := 2Ω² and R_e := R, solving
[[eq:two-dust-limit]] on 𝒪 ∩ {u ≥ 0, v ≥ 0}, and the given functions are data of that proposition, with ϰ_1 = ½ ln γ_ϑ,
ϰ_2 = A_c, ϰ_3 = A_s: the C^m norm of ϰ_1 − ϰ̊_1 is half that of ln γ_ϑ − ln γ̊_ϑ, so each difference has C^m norm at
most Λ. That proposition gives the solution, with σ depending only on κ, Λ, d and bounds for the background on the
points within 4d of Q1. ∎

#### The theorem {#sec:civp-large-theorem}

**Theorem {#thm:civp-large}** (Developments of cone data without smallness.) Let cone data on Q1 be given
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
they are given by constants a*, b* that [[thm:std-cctw-strips]] provides for the localised system
[[eq:civp-large-localised]] with the data of [[lem:civp-large-data]], for any choice of the cut-off and the extension
in its definition, and by three suprema of its solution, and they depend on the cone data through these. No lower bound
for δ in terms of norms of the cone data is asserted.

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
(3.100)–(3.101)] of [[thm:std-cctw-existence]] for this system are its f₃-equations restricted to {v = 0} and its
f₄-equations restricted to {u = 0}. They have global solutions: on J0 take the solutions of [[lem:civp-large-data]] (b)
(i), and on the rest of Y the restrictions of f̊_e. Where ϱ = 1 these are the equations of [[lem:civp-large-data]] (b)
(i); at the other points of J0 those solutions equal f̊ ([[lem:civp-large-data]] (b) (ii)), which solves the localised
system; and the two pieces agree near the ends of J0.

*Step 2: the strip solution.* [[thm:std-cctw-existence]] and [[thm:std-cctw-strips]] apply with n = 2, a0 := u_1, b0 :=
v_1 and any integer ℓ ≥ 6 (ℓ > (n + 9)/2): Y is a compact one-dimensional manifold without boundary, the system has the
form (2.7)–(2.8) with the scalar product, and the flat connection as both ∇ and ∇̊, preserving the splitting, the data
are smooth, and the transport equations have global solutions. They give a* ∈ (0, u_1], b* ∈ (0, v_1] and a solution f of
[[eq:civp-large-localised]] with these data on 𝒰 := ([0, a*] × [0, v_1] ∪ [0, u_1] × [0, b*]) × Y, unique among C¹
solutions and smooth, the data being smooth.

*Step 3: localisation and δ.* Put z := f − f̊_e on 𝒰. Subtracting the equations for f and f̊_e,

    A^u∂_uz + A^v∂_vz + ϱA^ϑ(f)∂_ϑz = ϱ(G(f) − G(f̊_e)) − ϱ(A^ϑ(f) − A^ϑ(f̊_e))∂_ϑf̊_e,

whose right side is B z with B := ϱ∫_0^1 (dG − (dA^ϑ)∂_ϑf̊_e)(f̊_e + s z) ds continuous. This is [[eq:civp-large-linear]]
with P := ϱb I₁₀ and Q := ϱQ(f), b and Q(f) evaluated on f. Its data vanish on the arc I := Y ∖ (ϑ_a, ϑ_b). Let

    p1 := sup |b| over [0, a*] × [0, v_1] × Y,      β1 := sup |∂_vb| over [0, u_1] × [0, b*] × Y,
    q1 := sup e^(α−β) over 𝒰,      s1 := min(a*, η0²/(2p1η0 + 4q1²v_1)),
    s2 := min(b*, η0/(4u_1β1), η0²/(8q1²u_1)),      δ := min(s1, s2),
                                                                                             {#eq:civp-large-delta}

with the middle term of s2 omitted if β1 = 0, the components b, α, β being those of f. On [0, s1] × [0, v_1] apply
[[lem:civp-large-energy]] (a) with J := I, p := p1, q := q1 and t := 2q1²v_1/η0: then c2 = η0/(2v_1), c1 = p1 + t, and
w = c1u + c2v ≤ c1s1 + η0/2 ≤ η0. On [0, u_1] × [0, s2] the b-component of f vanishes at v = 0, both on J0 (b = 0 on
𝒞_in) and elsewhere (f̊_e has b = 0), so |b| ≤ β1 v ≤ β1 s2 ≤ η0/(4u_1) =: p there; with t := η0/(4u_1), c1 = p + t ≤
η0/(2u_1) and c2 = 4q1²u_1/η0, so w ≤ η0/2 + c2s2 ≤ η0. On both strips, therefore, z = 0 at the points of I at distance
at least η0 from its ends, that is

    f = f̊_e  at the points of 𝒮 × Y with ϑ ∉ (ϑ_a − η0, ϑ_b + η0),   𝒮 := [0, s1] × [0, v_1] ∪ [0, u_1] × [0, s2] ⊃ 𝒮_δ.

Define F on 𝒮_δ × (0, π/2) by F := f on J0 and F := f̊ off J0. It is smooth, since f = f̊_e = f̊ near the ends of J0; it
equals f̊ at the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0]; and it solves [[eq:civp-large-system]], since ϱ = 1 on [ϑ_a − η0,
ϑ_b + η0] and f̊ solves [[eq:civp-large-system]]. On 𝒞_out its f₃-components are f̄₃, and its f₄-components solve the
restriction of Step 1 with the same initial values at S; that restriction is a system of ordinary differential equations
in v along the lines {ϑ = const} (A^ϑ has no f₄f₄-block), so they are the solution of [[lem:civp-large-data]] (b) (i),
whose components α, β, b, ψ, ω are the functions of the data. Likewise on 𝒞_in its f₄-components are f̄₄ and its
f₃-components the solution of [[lem:civp-large-data]] (b) (i), b vanishing there.

*The signs of the densities.* The components q_in and q_out of F are nonnegative on 𝒮_δ × (0, π/2). Let (u′, v′) ∈ 𝒮_δ
and ϑ′ ∈ (0, π/2). Since 𝒮_δ is a past set, the segments [0, u′] × {v′} and {u′} × [0, v′] lie in it. The component b of
F is smooth on 𝒮_δ × (0, π/2) and vanishes at the angles outside [ϑ_a − η0, ϑ_b + η0], where F = f̊; so the constant
functions ϑ_a − η0 and ϑ_b + η0 solve dϑ/du = b(u, v′, ϑ), and by uniqueness the solution ϑ(·) with ϑ(u′) = ϑ′ stays in
[ϑ_a − η0, ϑ_b + η0] if ϑ′ lies there, and is constant otherwise. It therefore exists on all of [0, u′], with values in
(0, π/2), and c(u) := (u, v′, ϑ(u)) is an integral curve of D_3 = ∂_u + b∂_ϑ. By the equation D_3q_in = −e^α χ̲ q_in of
[[eq:civp-large-system]], (q_in ∘ c)′ = −(e^α χ̲ q_in) ∘ c, so

    q_in(u′, v′, ϑ′) = q_in(0, v′, ϑ(0)) exp(−∫_0^(u′) (e^α χ̲)(c(u)) du).

At u = 0, q_in is a component of f̄₃, the q_in of the data, which is nonnegative; so q_in(u′, v′, ϑ′) ≥ 0. Likewise the
equation ∂_vq_out = −e^α χ q_out gives q_out(u′, v′, ϑ′) = q_out(u′, 0, ϑ′) exp(−∫_0^(v′) (e^α χ)(u′, v, ϑ′) dv), and
q_out(u′, 0, ϑ′) is a component of f̄₄, the q_out of the data, which is nonnegative.

*Step 4: F is geometric.* Let h_F and g_F be the metrics built from the components α, β, b, ψ, ω of F as in
[[prop:civp-large-system]] (b); they are defined on all of 𝒮_δ × (0, π/2), times T² for g_F. F is geometric on a set
when the identities of [[prop:civp-large-system]] (b) hold at its points; on the closure of a set where they hold they
hold too, F being smooth. Where F is geometric, (g_F, v, u, q_in, q_out), extended by (g0, q̊_in, q̊_out) to the axes,
is a class solution in the gauge, by that proposition, the densities being nonnegative and F being f̊ off [ϑ_a − η0,
ϑ_b + η0]. We say that F is *geometric to first order* at a point if there its components χ, χ̲, η, η̲, ϖ, ϖ̲ are the
connection coefficients of h_F and Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}. We show that F is
geometric on 𝒮_δ × (0, π/2). As 𝒮_δ = 𝒯₁ ∪ 𝒯₂, 𝒯₁ := [0, δ] × [0, v_1], 𝒯₂ := [0, u_1] × [0, δ], it suffices to treat
one of them, 𝒯 = [0, l1] × [0, l2].

*Constants.* F is smooth on 𝒮_δ × (0, π/2) and equals f̊ off [ϑ_a − η0, ϑ_b + η0] ⊂ [2η0, π/2 − 2η0]. So the functions
Ω = e^(α−ψ), γ_ϑ = e^(2β−2ψ), b, A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2, q_in, q_out formed from F on segments {u_c} ×
[v_c, v_c + l_v] and [u_c, u_c + l_u] × {v_c} in 𝒯, transformed by the change of angle described below, have
differences from the background's whose C^m norms are bounded by one Λ, for all such segments, because F and its
derivatives are bounded on 𝒯 × [η0, π/2 − η0] and the change of angle has derivatives bounded by those of b. Let σ be
given by [[prop:civp-large-corner]] for this Λ and κ := η0, and L := σ/2.

*The corner step.* Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ 𝒯 with l_u, l_v ≤ σ and edges N_o, N_i, and assume: F
is geometric to first order at the points of the corner circle {(u_c, v_c)} × (0, π/2); N_o × (0, π/2) is contained in
a set on which F is geometric, or u_c = 0; and N_i × (0, π/2) is contained in a set on which F is geometric, or v_c =
0. We show that F is geometric on 𝒬 × (0, π/2). On N_o take the functions Ω, γ_ϑ, b, A_c, A_s, q_in formed from F, and
on N_i the functions Ω, γ_ϑ, b, A_c, A_s, q_out. Where an edge lies in 𝒞_out or 𝒞_in these are the cone data (Step 3),
and they satisfy the constraints by [[def:civp-large-data]] (ii); where F is geometric they are induced by the class
solution g_F, and the constraints are components of Ric(g_F) = q_in dv² + q_out du². They agree at the corner and equal
the background's off [2η0, π/2 − 2η0]. If b does not vanish on N_i, let Φ(u, ϑ) solve (∂_u + b(u, v_c, ϑ)∂_ϑ)Φ = 0 with
Φ(u_c, ϑ) = ϑ; for each u it is a diffeomorphism of (0, π/2) equal to the identity off [ϑ_a − η0, ϑ_b + η0], where b =
0. The change of angle (u, v, ϑ) ↦ (u, v, Φ(u, ϑ)) maps a metric of the form [[eq:loc-double-null]] to one of the same
form, with γ_ϑ replaced by γ_ϑ/(∂_ϑΦ)², b by ∂_uΦ + b∂_ϑΦ, and Ω, A_c, A_s unchanged, since Φ does not depend on v and
dϑ − b du = (dΦ − (∂_uΦ + b∂_ϑΦ) du)/∂_ϑΦ; it commutes with the T² action and the reflections, it is the identity on
N_o, and after it b = 0 on N_i, while b on N_o becomes b − b(u_c, v_c, ·). [[prop:civp-large-corner]] applies to the
transformed functions and gives a class solution in the gauge on 𝒬 × S³; changing the angle back gives a class solution
g_c in the gauge on 𝒬 × S³ that induces the functions above on N_o and N_i and equals (g0, q̊_in, q̊_out) off [η0, π/2
− η0]. Let f_c be its reduced fields, a solution of [[eq:civp-large-system]] on 𝒬 × (0, π/2)
([[prop:civp-large-system]] (a)). By [[lem:civp-large-data]] (a), the f₃-components of f_c on N_o and its f₄-components
on N_i are given by the functions on the edges, through [[eq:civp-large-coefficients]] and the equations (F4′) on N_o
and (F5), (F4) on N_i, with the values of f_c at the corner, which are given by [[eq:civp-large-coefficients]] in the
functions near the corner. The same holds for F. At the corner F is geometric to first order, and h_F, ψ, ω induce the
same functions on the edges as g_c, so F has the same values there as f_c. On an edge on which F is geometric, the
proof of [[lem:civp-large-data]] (a) applies to F, since it uses only identities that hold at the points of the edge.
On an edge in 𝒞_out or 𝒞_in it holds by the definition of f̄ in [[lem:civp-large-data]] (b), the linear equations there
being those used here, with the same coefficients, and the values at the corner being those of F. By uniqueness for
these linear equations, z := f_c − F has z₃ = 0 on N_o and z₄ = 0 on N_i. It solves the linear system A^μ(F)∂_μz =
G(f_c) − G(F) − (A^ϑ(f_c) − A^ϑ(F))∂_ϑf_c, of the form [[eq:civp-large-linear]] on 𝒬 × [η0/2, π/2 − η0/2], and z = 0 at
the points with ϑ ≤ η0 or ϑ ≥ π/2 − η0, where f_c = f̊ = F. By [[lem:civp-large-energy]] (b), z = 0 on 𝒬 × (0, π/2). So
F is the reduced fields of g_c on 𝒬 × (0, π/2) and is geometric there.

*Continuation in u + v.* For t > 0 let D_t := {(u, v) ∈ 𝒯 : u + v < t}, and let t* be the supremum of the t ∈ (0, l1 +
l2] such that F is geometric on D_t × (0, π/2), with t* := 0 if there is none. The corner step with 𝒬 = [0, min(L, l1)]
× [0, min(L, l2)] applies: its corner is S, where F is geometric to first order, because the values of f̄ at S are
those of [[eq:civp-large-coefficients]] in the cone data, and its edges lie in 𝒞_out and 𝒞_in. So t* ≥ min(L, l1, l2) >
0. Suppose t* < l1 + l2. F is geometric on the closure of D_t* × (0, π/2). Let Γ := {(u, v) ∈ 𝒯 : u + v = t*}, and for
p = (u_p, v_p) ∈ Γ let u_c := max(u_p − L/2, 0), v_c := max(v_p − L/2, 0) and 𝒬_p := [u_c, min(u_p + L/2, l1)] × [v_c,
min(v_p + L/2, l2)], whose sides are at most L < σ. Its corner satisfies u_c + v_c ≤ t*. If v_c > 0, the edge N_i =
[u_c, min(u_p + L/2, l1)] × {v_c} satisfies u + v ≤ u_p + L/2 + v_p − L/2 = t*, so it lies in the closure of D_t*;
likewise N_o if u_c > 0. So the corner step applies, and F is geometric on 𝒬_p × (0, π/2). Every (u, v) ∈ 𝒯 with t* ≤
u + v < t* + L/4 lies in some 𝒬_p: with s := (u + v − t*)/2 < L/8, take p := (u − s, v − s) if this point lies in 𝒯, and
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
theorem asserts their existence and gives no bound for them (a* does not depend on ℓ by [[thm:std-cctw-existence]], nor
b* by that theorem with u and v exchanged). p1, q1 and β1 are suprema of the strip solution, the shift, the ratio
e^(α−β) = Ω γ_ϑ^(−1/2) and ∂_vb, and are not bounded here in terms of the data. So δ depends on the data, on the band
through η0, on u_1, v_1 and on the choice of the cut-off and the extension, and no lower bound for it in terms of norms
of the data is asserted. For data near the background's, [[thm:loc-cone-development]] gives a development on the
explicit set {uv ≤ δ_*²}; it equals g0 near the axes, so by [[thm:civp-large]] (c) the two developments agree where both
are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
or measure-valued.

**Remark {#rem:civp-large-beyond}** (What the theorem adds.) With [[thm:civp-large]], the cone data of [[sec:loc-cones]]
that are localised in a band away from the axes have developments without any smallness. With u_1 = 7.2 and v_1 = 4.5,
which are admissible ([[lem:civp-large-rectangle]] (a)), every perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} and of
the packet on 𝒞_in ∩ {5.7 < u < 7.2}, together or apart, and every density added in the band, of any amplitude for which
the factors e^ϕ stay positive on [0, 4.5] and on [0, 7.2], gives cone data on Q1 ([[lem:civp-large-free]] (a)) and so
has a development. Such data exist with densities of every amplitude: the density of the shell may be multiplied by 1 +
c with −1 ≤ c ≤ 76, and that of the packet by 1 + c with −1 ≤ c ≤ 4.5, c a smooth function of ϑ with compact support in
the band, and densities of any supremum may be added on short enough intervals ([[lem:civp-large-rectangle]] (b)). The
development contains the strip {u ≤ δ} along all of 𝒞_out ∩ {v ≤ v_1} and the strip {v ≤ δ} along all of 𝒞_in ∩ {u ≤
u_1}, so the dust on the cones lies in it; it is in the double-null gauge of the class, with u and v the phases of the
two families; it is localised, equal to the background outside {ϑ_a − η0 ≤ ϑ ≤ ϑ_b + η0}, so that localisation on the
cones is localisation of a spacetime; and it is unique in the gauge among solutions that equal the background near the
axes. For vacuum cone data (v_1 < 3 and u_1 < 5.7, the densities zero), [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]) gives a vacuum development for data of any size; the theorem adds the double-null gauge,
uniqueness in it, and localisation. Compared with [[thm:loc-cone-development]], smallness is dropped and uniqueness
holds among all solutions that equal the background near the axes, not only near the background; the neighbourhood is
not explicit and no estimate of the solution is given.

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
compactly supported in (−t_0, t_0), χ = 1 near 0. Then g0 + εh has, on Σ_τ0, the lapse 1, the normal ∂_t and the data
(γ + εδγ, K + εδK), so the data's first variation is δ. Since Ein(g0) = 0 near supp h, the first variation of the
constraints is DΦ[δ] = (2Ein¹[h](n, n), Ein¹[h](n, ·)), Ein¹[h] the linearised Einstein tensor, because the variation of
the normal enters multiplied by Ein(g0). By (a), N_sDℋ[δ] + 2Y_s·Dℳ[δ] = 2Ein¹[h](ξ, n). The vector field J^a :=
Ein¹[h]^(ab) ξ_b is compactly supported, and ∇_aJ^a = (∇_a Ein¹[h]^(ab)) ξ_b + Ein¹[h]^(ab)∇_(a ξ_b) = 0: the first term
vanishes by the linearised contracted Bianchi identity at a vacuum metric, obtained by differentiating ∇^(g0+εh)_a
Ein(g0 + εh)^(ab) = 0 at ε = 0, and the second because ξ is Killing. By the divergence theorem on [0, t_1] × U′, supp χ ⊂
(−t_1, t_1), t_1 < t_0, the flux of J through Σ_τ0 equals that through {t = t_1}, which is 0.

(c) In the Tangherlini chart of [[lem:racz-split-formulas]] (d), let X = X^v∂_v + X^R∂_R + X^ϑ∂_ϑ + X^1∂_(φ1) +
X^2∂_(φ2) be an invariant Killing field; its components do not depend on φ1, φ2. The reflection φ_i ↦ −φ_i changes
the sign of X^i, so X^1 = X^2 = 0. The φ1φ1 and φ2φ2 components of L_X g are 2R cos²ϑ X^R − 2R² sc X^ϑ and 2R sin²ϑ
X^R + 2R² sc X^ϑ; their sum 2R X^R vanishes, so X^R = 0 and then X^ϑ = 0. With X = X^v∂_v, the RR, Rϑ and vR
components are 2∂_RX^v, ∂_ϑX^v and ∂_vX^v − f∂_RX^v, so X^v is constant. ∎

**Lemma {#lem:loc-kid-space}** (The Killing initial data of a closed band.) Let U = {R1 < R < R2} be a band as in
[[lem:loc-kid]] (b), let R1 < R₋ < R₊ < R2, and let 𝒱 := Σ_τ0 ∩ {R₋ ≤ R ≤ R₊}, with interior 𝒱°. Write 𝔍 := (−2ℳ, ℋ),
which is the constraint map (J, ρ) of [[thm:std-cd-constraints]], let P be its linearisation at the background's data
(K, γ), and P* the formal adjoint of P [CD03, (2.4), p. 5], quoted in [[sec:v-0]]. A *Killing initial data pair* on
𝒱° is a pair (Y, N) of a vector field and a function on 𝒱°, with locally square-integrable weak derivatives of order
at most 1 and at most 2 respectively, such that P*(Y, N) = 0 almost everywhere. Let 𝒢 be the group generated by the T²
action and the two reflections φ_i ↦ −φ_i; it acts on pairs by push-forward, and a pair is *invariant* if 𝒢 fixes it.

(a) Every Killing initial data pair on 𝒱° is smooth on 𝒱° and extends smoothly to 𝒱. These pairs form a vector space
of dimension at most 15.

(b) The pair 𝔨 := (−Y_s, N_s), with (N_s, Y_s) as in [[eq:racz-kid]], satisfies P*(𝔨) = 0 on U. Every invariant
Killing initial data pair on 𝒱° is a constant multiple of 𝔨.

*Proof.* (a) Let (Y, N) be such a pair, ∇ the connection of γ, and indices raised and traced with γ. By the formula
of [[sec:v-0]] at (K, γ), the first component of P*(Y, N) is 2(∇_(iY_j) − ∇^lY_l γ_ij − K_ijN + tr K N γ_ij). Its
trace is −6(∇^lY_l − N tr K), the slice having dimension 4; so ∇^lY_l = N tr K, and the first component vanishes
exactly when

    ∇_(iY_j) = N K_ij.                                                                          {#eq:loc-kid-first}

Let A_ij := ∇_[iY_j] be the antisymmetric part of ∇Y, so that ∇_iY_j = NK_ij + A_ij. The second component of
P*(Y, N) is ∇_i∇_jN − ΔN γ_ij + 𝔏_ij, where

    𝔏_ij := ∇^lY_l K_ij − 2K^l_(i∇_j)Y_l + K^q_l∇_qY^l γ_ij + (∇^pK_lp γ_ij − ∇_lK_ij)Y^l − N Ric(γ)_ij
            + 2NK^l_iK_jl − 2N(tr K)K_ij

is linear in (Y, ∇Y, N) with coefficients built from γ, K, ∇K and Ric(γ). Its trace is −3ΔN + tr 𝔏, so

    ∇_i∇_jN = (1/3) tr 𝔏 γ_ij − 𝔏_ij,                                                          {#eq:loc-kid-second}

and, with ∇Y = NK + A, the right side is linear in (Y, A, N) with smooth coefficients. For a smooth 1-form Y put
T_ijk := ∇_i∇_jY_k and S_ij := ∇_(iY_j). The Ricci identity reads T_ijk − T_jik = (ℛY)_ijk, where ℛY is a contraction
of the curvature tensor of γ with Y. Then ∇_iA_jk = ½(T_ijk − T_ikj) and ∇_jS_ik − ∇_kS_ij = ½(T_jik + T_jki − T_kij
− T_kji); inserting T_jik = T_ijk + (ℛY)_jik, T_kij = T_ikj + (ℛY)_kij and T_jki − T_kji = (ℛY)_jki gives

    ∇_iA_jk = ∇_jS_ik − ∇_kS_ij − ½((ℛY)_jik − (ℛY)_kij + (ℛY)_jki).                             {#eq:loc-kid-third}

Both sides of [[eq:loc-kid-third]] are continuous maps from 1-forms with locally square-integrable first derivatives to
distributions, and smooth 1-forms are dense among these, so [[eq:loc-kid-third]] holds for our Y in the sense of
distributions. By [[eq:loc-kid-first]], S = NK, so ∇_jS_ik = ∂_jN K_ik + N∇_jK_ik.

Let 𝔼 be the bundle T*Σ_τ0 ⊕ Λ²T*Σ_τ0 ⊕ ℝ ⊕ T*Σ_τ0 over U, of rank 4 + 6 + 1 + 4 = 15, and Ξ := (Y, A, N, dN), Y taken
as a 1-form. The four relations ∇Y = NK + A, [[eq:loc-kid-third]] with S = NK, ∇N = dN and [[eq:loc-kid-second]] say

    ∇Ξ = 𝔖Ξ                                                                                       {#eq:loc-kid-system}

in the sense of distributions on 𝒱°, where 𝔖 is a section of T*U ⊗ End(𝔼), smooth on U and built from γ, K and their
derivatives. Ξ is locally square integrable, hence so is 𝔖Ξ = ∇Ξ, so Ξ has locally square-integrable first derivatives;
and if Ξ has locally square-integrable derivatives up to order j, so has 𝔖Ξ = ∇Ξ, and Ξ has them up to order j + 1, in
coordinates the derivatives of Ξ differing from ∇Ξ by Christoffel symbols times Ξ. By Sobolev's inequality, Ξ, and with
it (Y, N), is smooth on 𝒱°.

Along every smooth curve c in 𝒱°, Ξ ∘ c solves the linear ordinary differential equation ∇_ċΞ = 𝔖(ċ)Ξ. So if Ξ vanishes
at a point p₀, it vanishes along every curve from p₀; as 𝒱°, which is (R₋, R₊) × S³, is connected, Ξ = 0. The map
(Y, N) ↦ Ξ(p₀) ∈ 𝔼_(p₀) is therefore linear and injective, and the pairs form a space of dimension at most 15. For the
extension, let y be coordinates on an open set O ⊂ S³. In the coordinates (R, y) and the coordinate frames of 𝔼, the
radial part ∇_(∂_R)Ξ = 𝔖(∂_R)Ξ of [[eq:loc-kid-system]] is a linear system ∂_RΞ = 𝔖_R(R, y)Ξ, with 𝔖_R smooth on
(R1, R2) × O. Fix R_m ∈ (R₋, R₊). The solution of this system with the value Ξ(R_m, y) at R = R_m is defined for all
R ∈ (R1, R2), is smooth in (R, y) by the smooth dependence of the solutions of linear systems on parameters and initial
values, and equals Ξ on (R₋, R₊) × O. The solutions over different sets O agree where both are defined, being solutions
of the same equation with the same values at R_m. So Ξ, and with it (Y, N), extends smoothly to a neighbourhood of 𝒱.

(b) P*(𝔨) is smooth on U. For every smooth pair δ = (δγ, δK) with compact support in U, Pδ = (−2Dℳ[δ], Dℋ[δ]), and the
definition of the formal adjoint gives

    ∫_U ⟨P*(𝔨), (δK, δγ)⟩ dvol = ∫_U (−Y_s·(−2Dℳ[δ]) + N_s Dℋ[δ]) dvol = ∫_U (N_s Dℋ[δ] + 2Y_s·Dℳ[δ]) dvol,

which vanishes by [[lem:loc-kid]] (b). As δ is arbitrary, P*(𝔨) = 0 on U.

Let (Y, N) be an invariant Killing initial data pair; by (a) it is smooth. In the coordinates (R, ϑ, φ1, φ2), on
0 < ϑ < π/2, the components of Y and N do not depend on φ1, φ2, and the reflection φ_i ↦ −φ_i reverses the component
Y^(φ_i), so Y^(φ_1) = Y^(φ_2) = 0. By [[eq:loc-kid-first]], ½L_Yγ = NK. On Σ_τ0, γ = G dR² + R² dΩ₃² and
K = κ0 G dR² + Y0 R² dΩ₃² with G, κ0 and Y0 functions of R ([[lem:racz-split-formulas]] (a), (b)), and Y0 = K^l_l/3 < 0,
as qf < 1 on Σ_τ0. The φ1φ1, φ2φ2, Rϑ and RR components of ½L_Yγ = NK read

    R cos²ϑ Y^R − R² sc Y^ϑ = N Y0 R² cos²ϑ,          R sin²ϑ Y^R + R² sc Y^ϑ = N Y0 R² sin²ϑ,
    ½(G ∂_ϑY^R + R² ∂_RY^ϑ) = 0,                        ½ Y^R ∂_RG + G ∂_RY^R = N κ0 G.

The sum of the first two gives Y^R = N Y0 R, and then the first gives Y^ϑ = 0. The third then gives ∂_ϑY^R = 0, and the
fourth, with N = Y^R/(Y0 R), gives

    ∂_RY^R = (κ0/(Y0 R) − ∂_RG/(2G)) Y^R.

So Y^R is a function of R alone that solves a linear equation of first order, and is fixed by its value at one radius;
then N = Y^R/(Y0 R) and Y = Y^R ∂_R are fixed on 0 < ϑ < π/2, hence everywhere by continuity. The invariant pairs
therefore form a space of dimension at most one. 𝔨 lies in it: it is smooth, P*(𝔨) = 0, and it is invariant, N_s and
Y_s^R being functions of R and Y_s = Y_s^R ∂_R. As N_s > 0, 𝔨 ≠ 0, and every invariant pair is a constant multiple of
𝔨. ∎

**Definition {#def:loc-charge}** (Seeds and the charge.) Let U be a band as in [[lem:loc-kid]] (b). A *seed* on U is a
smooth invariant pair δ = (δγ, δK) with compact support in U and DΦ[δ] = 0. Its *charge* is

    Q(δ) := ½ ∫_U (N_s D²ℋ[δ, δ] + 2Y_s·D²ℳ[δ, δ]) dvol.                                               {#eq:loc-charge}

A seed is a *momentum seed* if δγ = 0. It is a *gauge seed* if there are a band U″ with supp δ ⊂ U″ and Ū″ ⊂ U, and a
vector field Z on a neighbourhood of Ū″ in spacetime, the *generator*, vanishing near the outer sphere of ∂U″ and equal
to a constant multiple of ξ near the inner one, such that δ is the first variation of the data induced on the slice
by the pull-backs of g0 under the flow φ_ε of Z; otherwise it is *non-gauge*. Gauge seeds have Q = 0. Indeed, the data
D_ε that φ_ε*g0 induces on the slice are vacuum data, the background's data on a deformed slice pulled back by φ_ε;
they equal the background's outside a compact subset of U″, where Z is zero or a Killing field; and D_ε = bg + εδ + c_ε
with ‖c_ε‖_(C²) ≤ Cε², by Taylor's formula. So [[prop:loc-projection]] (a) gives ε²Q(δ) + O(ε³) = 0, and Q(δ) = 0.

**Lemma {#lem:loc-continuity}** (Corrections depending continuously on a parameter.) Let U be a band as in
[[lem:loc-kid]] (b), Ω_c ⊂ U compact, [s_a, s_b] a compact interval, and δ_s, s ∈ [s_a, s_b], seeds on U supported in
Ω_c, with s ↦ δ_s continuous into C^l(U) for every l. Let ρ_1 ≥ 0 be a smooth invariant function supported in Ω_c,
possibly zero, and J_1 := −ρ_1 dR/|dR|_γ. Fix an integer k ≥ 3. There are a smooth invariant function 𝔴 ≥ 0 with compact
support in U, positive on a band containing Ω_c, and ε_0 > 0 and C, such that for ε ∈ (0, ε_0] and s ∈ [s_a, s_b] there
are invariant pairs c_(ε,s) on Σ_τ0 with the following properties. Write D_(ε,s) := bg + εδ_s + c_(ε,s), γ_D for its
metric and g_(ε,s) for the metric of bg + εδ_s.

(i) c_(ε,s) is of class C^(k−1), vanishes outside a compact subset of U independent of ε and s, satisfies
‖c_(ε,s)‖_(C²) ≤ Cε², and is continuous in s in C². If ρ_1 = 0, c_(ε,s) is smooth.

(ii) For a real number m(ε, s), on U,

    ℋ(D_(ε,s)) = 2ε²s |J_1|_(γ_D) + m(ε, s) 𝔴 N_s,      ℳ(D_(ε,s)) = ε²s J_1 + ½ m(ε, s) 𝔴 g_(ε,s)(Y_s, ·).
                                                                                                {#eq:loc-continuity-res}

(iii) m(ε, ·) is continuous on [s_a, s_b], and, uniformly in s,

    m(ε, s) 𝔫(ε, s) = ε² (Q(δ_s) − 2s ∫_U (N_s ρ_1 + Y_s·J_1) dvol) + O(ε³),
    𝔫(ε, s) := ∫_U 𝔴 (N_s² + g_(ε,s)(Y_s, Y_s)) dvol > 0.                                          {#eq:loc-continuity-m}

*Proof.* *The band and the solvability statement.* Write U = {R1 < R < R2}, choose R1 < R₋ < R₊ < R2 with
Ω_c ⊂ {R₋ < R < R₊}, and let 𝒱 := Σ_τ0 ∩ {R₋ ≤ R ≤ R₊}: a compact manifold with boundary of dimension 4, the product
[R₋, R₊] × S³. Put 𝔩(R) := ∫_(R₋)^R √G(R′) dR′ and 𝔩₊ := 𝔩(R₊). As γ = G dR² + R² dΩ₃², |d𝔩|_γ = 1, so along a curve
in 𝒱 the function 𝔩 changes by at most the length of the curve, and the radial segments attain this; so the γ-distance
from a point of 𝒱 to ∂𝒱 is min(𝔩, 𝔩₊ − 𝔩). Let h ∈ C^∞([0, 𝔩₊]) with 0 < h ≤ 1 on (0, 𝔩₊), h(t) = t near 0 and
h(t) = 𝔩₊ − t near 𝔩₊, and x := h ∘ 𝔩. Then x is a defining function of ∂𝒱 as in [[sec:s28-solvability]]: smooth on 𝒱,
positive and at most 1 on 𝒱°, and equal to the γ-distance to ∂𝒱 near ∂𝒱; it depends on R alone. Put 𝔴 := e^(−2/x) on
𝒱° and 𝔴 := 0 on the rest of Σ_τ0. As e^(−2/x) and all its derivatives tend to 0 at ∂𝒱, 𝔴 is smooth; it is invariant,
its support is 𝒱 ⊂ U, and it is positive on 𝒱° ⊃ Ω_c.

We apply [[sec:s28-solvability]] with 𝒜 := 𝒱, u₀ := (K, γ) on 𝒱, this x, the weight parameter equal to 1 (so that the
weights are e^(±1/x)), and the integer k, which exceeds half the dimension. The space 𝒦₀ of [[sec:s28-solvability]]
consists of pairs with the regularity required in [[lem:loc-kid-space]] on which P* times positive weights vanishes,
that is, of Killing initial data pairs on 𝒱°. By [[lem:loc-kid-space]] (a) these are smooth on 𝒱 and form a
finite-dimensional space, so (Fin) holds, with a basis of pairs smooth on 𝒱. Conversely a Killing initial data pair
smooth on 𝒱 lies in the spaces of 𝒦₀ (*The spaces* in [[sec:s28-solvability]]), hence in 𝒦₀. In particular 𝔨 ∈ 𝒦₀,
and by [[lem:loc-kid-space]] (b) the invariant elements of 𝒦₀ are the constant multiples of 𝔨. So [[lem:s28-setting]]
and [[lem:v-3-2]] apply. Let ε_c, r_c, B, C₁, ε_s and C₅ be as there, C₆ the constant of the proof of [[lem:v-3-2]] (c),
so that ‖π₀♯_(g′)e^(2/x)σ‖_𝒵 ≤ C₆‖σ‖_𝒮 for σ ∈ 𝒮 and u′ = (K′, g′) ∈ 𝒩_(ε_c), and C_T a bound for the norm of T_(u′)
from 𝒴 to 𝒳, uniform for u′ ∈ 𝒩_(ε_c) (proof of [[lem:v-3-2]] (a)). We write σ for the right side (δJ, δρ) of
[[eq:v-3-1]].

*The data.* For δ_s = (δγ_s, δK_s) put u′ = u′_(ε,s) := (K + εδK_s, γ + εδγ_s) on 𝒱, so that g′ = g_(ε,s). As x ≤ 1
and the derivatives of x are bounded, the norm of 𝒩 of u′ − u₀ is at most Cε(‖δK_s‖_(C^(k+3)) + ‖δγ_s‖_(C^(k+4))),
which is at most Cε uniformly in s, s ↦ δ_s being continuous on a compact interval; so u′ ∈ 𝒩_(ε_c) for ε small, and
s ↦ u′ is continuous in that norm. 𝔍 is a smooth function of the 2-jet of the data, it vanishes at the background's
data on U, and P annihilates δ_s, as δ_s is a seed. By Taylor's formula, ‖𝔍(u′)‖_(C^(k+2)) ≤ Cε² uniformly in s;
𝔍(u′) is supported in Ω_c and continuous in s in C^(k+2). As x is bounded below on Ω_c, the weights of 𝒮 are bounded
there, and ‖𝔍(u′)‖_𝒮 ≤ C‖𝔍(u′)‖_(C^(k+1)) ≤ Cε².

*The matter term.* For a metric γ′ with |γ′ − γ|_γ < ½ put 𝔣(γ′) := |dR|_(γ′)/|dR|_γ. In coordinates (R, y), 𝔣 is a
smooth function of the point and of the components of γ′, 𝔣(γ) = 1, and ρ_1 𝔣(γ′) = |J_1|_(γ′). Choose a closed band
𝒱′ ⊂ 𝒱° with Ω_c in its interior; x is bounded below on 𝒱′. We claim:

(C) There is C such that for metrics a, b on 𝒱′ with |a − γ|_γ, |b − γ|_γ ≤ ¼ and ‖a − γ‖_(H^(k+2)(𝒱′)) ≤ 1,
‖b − γ‖_(H^(k+2)(𝒱′)) ≤ 1,

    ‖ρ_1 (𝔣(a) − 𝔣(b))‖_(H^k(𝒱′)) ≤ C ‖a − b‖_(H^(k+2)(𝒱′)).

Cover 𝒱′ by finitely many coordinate boxes [R₋′, R₊′] × Ō, O a ball of coordinates on S³; on each, the Sobolev norms of
𝒱′ are equivalent to the sums of those of the components on a bounded Lipschitz domain of ℝ⁴. There, by
[[thm:std-bh-embedding]] applied to derivatives of order at most k − 1, which lie in H³ with 3 · 2 > 4, and by
[[thm:std-bh17-embedding]] with (s, p, t, q) = (2, 2, 0, 4) applied to derivatives of order k, every component u of
a − γ, b − γ or ζ := a − b satisfies sup|∂^βu| ≤ C‖u‖_(H^(k+2)) for |β| ≤ k − 1, and
‖∂^βu‖_(L⁴) ≤ C‖u‖_(H^(k+2)) for |β| = k. Put a_t := b + tζ, t ∈ [0, 1]; then |a_t − γ|_γ ≤ ¼,
‖a_t − γ‖_(H^(k+2)) ≤ 1, and 𝔣(a) − 𝔣(b) = ∫₀¹ D𝔣(a_t)[ζ] dt, D𝔣 being the derivative in the metric. For |α| ≤ k, by
the Leibniz and chain rules, ∂^α(ρ_1 D𝔣(a_t)[ζ]) is a finite sum of terms

    b_t · (∂^(β₁)a_t ⊗ ⋯ ⊗ ∂^(β_i)a_t ⊗ ∂^(β₀)ζ),      |β₀| + |β₁| + ⋯ + |β_i| ≤ |α|,   |β_l| ≥ 1 for l ≥ 1,

where b_t is a derivative of ρ_1 times a derivative of 𝔣 in the point and the metric, evaluated at a_t, and is bounded,
as |a_t − γ|_γ ≤ ¼ on the compact 𝒱′. At most one of β₀, …, β_i has order k, two such orders adding up to 2k > k; the
other factors are bounded, by C‖ζ‖_(H^(k+2)) for the factor carrying ζ and by C for those carrying a_t, whose
derivatives are those of γ plus those of a_t − γ. The factor of order k, if there is one, is bounded in L⁴ in the same
way. So each term has L²-norm at most C‖ζ‖_(H^(k+2)) on a box, the L⁴-norm bounding the L²-norm there, and integrating
in t gives (C).

*The equation.* For z ∈ 𝒴 let (δK_z, δg_z) := T_(u′)z, and, when |εδγ_s + δg_z|_γ < ½ on Ω_c,

    σ(z) := −𝔍(u′) + ε²s (−2J_1, 2ρ_1 𝔣(g′ + δg_z)).                                     {#eq:loc-continuity-source}

By the proof of [[lem:s28-setting]] (a), [[eq:v-3-1]] with right side [[eq:loc-continuity-source]] holds for
(δK, δg) = T_(u′)z exactly when ♯_(g′)e^(2/x){𝔍(u′ + T_(u′)z) − 𝔍(u′) − σ(z)} ∈ 𝒦₀, that is,

    ♯_(g′)e^(2/x){𝔍(u′ + T_(u′)z) − ε²s (−2J_1, 2|J_1|_(g′ + δg_z))} ∈ 𝒦₀,               {#eq:loc-continuity-kid}

and, by [[lem:s28-setting]] (a), exactly when Ψ(u′, z) = π₀♯_(g′)e^(2/x)σ(z).

*Bounds.* ‖T_(u′)z‖_𝒳 ≤ C_T‖z‖_𝒴. On 𝒱′ the weights of 𝒳 are bounded above and below, so the norm of 𝒳 bounds
‖δg_z‖_(H^(k+2)(𝒱′)); and ‖δg_z‖_(C⁰) ≤ C‖T_(u′)z‖_𝒳 ([[lem:s28-setting]] (c)). The norm of the second factor of 𝒮
of a function supported in Ω_c is at most C times its H^k(𝒱′)-norm. Fix r ∈ (0, r_c) so small that ‖z‖_𝒴 ≤ r
implies |δg_z|_γ ≤ ⅛ and ‖δg_z‖_(H^(k+2)(𝒱′)) ≤ ½, and take ε_0 so small that |εδγ_s|_γ ≤ ⅛ and
‖εδγ_s‖_(H^(k+2)(𝒱′)) ≤ ½ for all s. Then (C), with a := g′ + δg_z and b := g′ + δg_w, gives for ‖z‖_𝒴, ‖w‖_𝒴 ≤ r

    ‖σ(z) − σ(w)‖_𝒮 ≤ C ε² ‖z − w‖_𝒴,      ‖σ(z)‖_𝒮 ≤ C ε²,

the second because ‖σ(0)‖_𝒮 ≤ ‖𝔍(u′)‖_𝒮 + Cε², ρ_1 𝔣(g′) being smooth and bounded with its derivatives uniformly in
s. Diminishing ε_0, Cε_0² < ε_s and C₅Cε_0² ≤ r.

*The fixed point.* Let B̄_r be the closed ball of radius r about zero in 𝒴, so B̄_r ⊂ B. For z ∈ B̄_r,
‖σ(z)‖_𝒮 < ε_s, so [[lem:v-3-2]] (c) gives z̃ ∈ B with Ψ(u′, z̃) = π₀♯_(g′)e^(2/x)σ(z) and
‖z̃‖_𝒴 ≤ C₅‖σ(z)‖_𝒮 ≤ r, and by [[lem:v-3-2]] (a) it is the only such z̃ in B. Put Θ(z) := z̃. So Θ maps B̄_r into
itself, and for z, w ∈ B̄_r, by [[eq:s28-lower]],

    ‖Θ(z) − Θ(w)‖_𝒴 ≤ 2C₁‖Ψ(u′, Θ(z)) − Ψ(u′, Θ(w))‖_𝒵 = 2C₁‖π₀♯_(g′)e^(2/x)(σ(z) − σ(w))‖_𝒵
                    ≤ 2C₁C₆‖σ(z) − σ(w)‖_𝒮 ≤ 2C₁C₆Cε²‖z − w‖_𝒴,

which is at most ½‖z − w‖_𝒴 once ε_0 is small. By the contraction mapping theorem, Θ has exactly one fixed point
z* = z*(ε, s) in B̄_r. Let (δK, δg) := T_(u′)z* and put c_(ε,s) := (δg, δK) on 𝒱 and c_(ε,s) := 0 on the rest of Σ_τ0.
If ρ_1 = 0, σ does not depend on z, and z* is the solution of [[lem:v-3-2]] (c) with right side −𝔍(u′).

*Invariance.* 𝒢 acts on 𝒱 by isometries of γ that preserve K and x. They map Killing initial data pairs to Killing
initial data pairs and preserve the weighted spaces and their norms, so 𝒦₀ is 𝒢-invariant; for invariant u′ the
L²-products with the weight e^(−1/x) built with g′ and with γ are 𝒢-invariant, so π_(g′) and π₀ commute with 𝒢. The
constraint map and P*_(u′) are natural, the weights are functions of x, and ♯_(g′) commutes with 𝒢 as g′ is invariant;
so T_(u′) commutes with 𝒢, and Ψ(u′, ·) is 𝒢-equivariant, as in step (3) of the proof of [[prop:vii-2-2]]. As 𝔍(u′),
ρ_1 and J_1 are invariant and |J_1|_(φ*g) = φ*|J_1|_g for φ ∈ 𝒢, σ(φ·z) = φ·σ(z). For φ ∈ 𝒢 and z ∈ B̄_r, φ·Θ(z) lies
in B and Ψ(u′, φ·Θ(z)) = φ·Ψ(u′, Θ(z)) = π₀♯_(g′)e^(2/x)σ(φ·z), so Θ(φ·z) = φ·Θ(z) by uniqueness. Then φ·z* is a fixed
point of Θ in B̄_r, so φ·z* = z*, and c_(ε,s) is invariant.

*Regularity and support.* T_(u′)z* lies in 𝒳 = x²H^(k+2)_(x²,e^(1/x)) × x⁴H^(k+2)_(x²,e^(1/x)); write it as
(x²w₁, x⁴w₂). As in the proof of [[lem:s28-setting]] (c), x^(4i)e^(2/x) is bounded below on 𝒱°, so w₁, w₂ ∈
H^(k+2)(𝒱), which lies in C^(k−1)(𝒱) by Sobolev's inequality, as (k + 2) − (k − 1) > 2. Let w be w₁ or w₂ and
i ≤ k − 1. ∇^iw is continuous on 𝒱, and ∫_𝒱 x^(4i)e^(2/x)|∇^iw|² dvol is finite. If ∇^iw did not vanish at a point of
∂𝒱, |∇^iw| would be bounded below on a neighbourhood, where in the coordinates (x, y) the volume element is bounded
below by a multiple of dx dy and ∫₀ t^(4i)e^(2/t) dt diverges. So the derivatives of w₁ and w₂ of order at most k − 1
vanish on ∂𝒱, and so do those of c := c_(ε,s). Hence c_(ε,s) is of class C^(k−1) on Σ_τ0 and vanishes outside 𝒱. By
[[lem:s28-setting]] (c), ‖c_(ε,s)‖_(C²) ≤ C‖T_(u′)z*‖_𝒳 ≤ CC_T‖z*‖_𝒴 ≤ CC_TC₅‖σ(z*)‖_𝒮 ≤ Cε². If ρ_1 = 0, by the
last sentence of [[lem:v-3-2]] (c) the correction is that of [[lem:s28-setting]] (a), and (b) of that lemma, with this
Ω_c and the bound ‖𝔍(u′)‖_(C^(k+2)) ≤ Cε², shows that it is smooth on 𝒱 and extends smoothly by zero.

*The residual.* The metric of D := D_(ε,s) is γ_D = g′ + δg_(z*) on 𝒱. As z* is a fixed point, Ψ(u′, z*) =
π₀♯_(g′)e^(2/x)σ(z*), so by [[eq:loc-continuity-kid]] the pair v := ♯_(g′)e^(2/x){𝔍(D) − ε²s(−2J_1, 2|J_1|_(γ_D))}
lies in 𝒦₀. It is invariant, as u′, g′, x, ρ_1, J_1 and c are; so v = m𝔨 on 𝒱° for a real number m = m(ε, s).
Lowering the index with g′ and multiplying by e^(−2/x), 𝔍(D) − ε²s(−2J_1, 2|J_1|_(γ_D)) = m e^(−2/x)(−g′(Y_s, ·), N_s)
on 𝒱°; as 𝔍 = (−2ℳ, ℋ), this is [[eq:loc-continuity-res]] on 𝒱°. On U ∖ 𝒱, D is the background's data, which are
vacuum there, and both sides of [[eq:loc-continuity-res]] vanish, as ρ_1, J_1 and 𝔴 do; on ∂𝒱 both sides are
continuous. This proves (ii).

*The coefficient.* Pair [[eq:loc-continuity-res]] with (N_s, 2Y_s) over U. The right sides give

    2ε²s ∫_U (N_s|J_1|_(γ_D) + Y_s·J_1) dvol + m𝔫 = 2ε²s ∫_U (N_sρ_1 + Y_s·J_1) dvol + O(ε³) + m𝔫,

since |J_1|_γ = ρ_1 and ||J_1|_(γ_D) − |J_1|_γ| ≤ Cρ_1|γ_D − γ|_γ ≤ Cερ_1, uniformly in s. For the left sides let
w := εδ_s + c_(ε,s), which is of class C², vanishes outside 𝒱 and has ‖w‖_(C²) ≤ Cε. Φ = (ℋ, ℳ) is a smooth function
of the 2-jet of the data and vanishes at the background's data on U, so on 𝒱, by Taylor's formula,
Φ(bg + w) = DΦ[w] + ½D²Φ[w, w] + O(ε³) uniformly in s, with DΦ[w] = DΦ[c_(ε,s)], as DΦ[δ_s] = 0, and
½D²Φ[w, w] = ½ε²D²Φ[δ_s, δ_s] + O(ε³). For c_(ε,s) = (δg, δK), the pairing of DΦ[c_(ε,s)] with (N_s, 2Y_s) is
∫_U ⟨P*(𝔨), (δK, δg)⟩ dvol = 0, by the identity in the proof of [[lem:loc-kid-space]] (b), the integrations by parts
being valid for a pair of class C² that vanishes outside the compact 𝒱. So the left sides give ε²Q(δ_s) + O(ε³), by
[[eq:loc-charge]], uniformly in s, and [[eq:loc-continuity-m]] follows; 𝔫 ≥ ∫_U 𝔴 N_s² dvol > 0.

*Continuity in s.* Let Θ_s be the map Θ built with s and u′_(ε,s), and z*_s its fixed point. For s, s′ ∈ [s_a, s_b],

    ‖z*_s − z*_(s′)‖_𝒴 ≤ ‖Θ_s(z*_s) − Θ_s(z*_(s′))‖_𝒴 + ‖Θ_s(z*_(s′)) − Θ_(s′)(z*_(s′))‖_𝒴
                        ≤ ½‖z*_s − z*_(s′)‖_𝒴 + ‖Θ_s(z*_(s′)) − Θ_(s′)(z*_(s′))‖_𝒴,

so ‖z*_s − z*_(s′)‖_𝒴 ≤ 2‖Θ_s(w) − Θ_(s′)(w)‖_𝒴 with w := z*_(s′). By *The equation*, Θ_s(w) and Θ_(s′)(w) are the
solutions in B of [[eq:v-3-1]] for (u′_(ε,s), σ_s(w)) and (u′_(ε,s′), σ_(s′)(w)), σ_s being σ built with s and
u′_(ε,s). By [[lem:v-3-2]] (b) their difference tends to zero as s → s′, as u′_(ε,s) → u′_(ε,s′) in the norm of 𝒩 and
σ_s(w) → σ_(s′)(w) in 𝒮. The latter holds because 𝔍(u′_(ε,s)) → 𝔍(u′_(ε,s′)) in C^(k+2) with supports in Ω_c;
T_(u′) depends continuously on u′ in operator norm (proof of [[lem:v-3-2]] (a)), so the metric part of T_(u′_(ε,s))w
tends to that of T_(u′_(ε,s′))w in 𝒳; g_(ε,s) → g_(ε,s′) in C^(k+4); and (C) applies. So s ↦ z*_s is continuous in
𝒴, and c_(ε,s), built from T_(u′_(ε,s))z*_s, is continuous in 𝒳, hence in C² ([[lem:s28-setting]] (c)). Finally
m(ε, s) is the left side of the pairing minus 2ε²s ∫_U (N_s|J_1|_(γ_D) + Y_s·J_1) dvol, divided by 𝔫(ε, s); D_(ε,s)
and γ_D are continuous in s in C², and 𝔫 is continuous in s, so m(ε, ·) is continuous. ∎

**Proposition {#prop:loc-projection}** (The charge decides localisation at second order.) Let U be a band as in
[[lem:loc-kid]] (b) and δ a seed on U.

(a) For every family D_ε = bg + εδ + c_ε of data on Σ_τ0, equal to the background's outside a fixed compact subset of
U, with ‖c_ε‖_(C²) ≤ Cε²,

    ∫_U (N_s ℋ + 2Y_s·ℳ)(D_ε) dvol = ε² Q(δ) + O(ε³).                                                {#eq:loc-pairing}

So if Q(δ) ≠ 0, no such D_ε satisfies the vacuum constraints for ε small.

(b) Let [s_a, s_b] be a compact interval and δ_s, s ∈ [s_a, s_b], seeds on U supported in a fixed compact subset of U,
with s ↦ δ_s continuous into C^l(U) for every l; for a single seed δ take δ_s := δ. There are a smooth invariant
function 𝔴 ≥ 0 with compact support in U, positive on a band containing the supports, and, for ε small, smooth
invariant corrections c_(ε,s) that vanish outside a compact subset of U independent of ε and s, with
‖c_(ε,s)‖_(C²) ≤ Cε² and continuous in s in C², such that, on U,

    ℋ(bg + εδ_s + c_(ε,s)) = m(ε, s) 𝔴 N_s,      ℳ(bg + εδ_s + c_(ε,s)) = ½ m(ε, s) 𝔴 g_(ε,s)(Y_s, ·),

g_(ε,s) the metric of bg + εδ_s, where m(ε, ·) is continuous on [s_a, s_b] and, uniformly in s,

    m(ε, s) 𝔫(ε, s) = ε² Q(δ_s) + O(ε³),      𝔫(ε, s) := ∫_U 𝔴 (N_s² + g_(ε,s)(Y_s, Y_s)) dvol > 0.

So m(ε, s) has the sign of ε²Q(δ_s) + O(ε³). Hence, if Q(δ_(s_a)) < 0 < Q(δ_(s_b)), then for ε small there is
s(ε) ∈ (s_a, s_b) such that bg + εδ_(s(ε)) + c_(ε,s(ε)) satisfies the vacuum constraints exactly on U and equals the
background's data outside a compact subset of U.

*Proof.* (a) By Taylor's formula, Φ(D_ε) = Φ(bg) + DΦ[εδ + c_ε] + ½ε² D²Φ[δ, δ] + O(ε³), with Φ(bg) = 0 and DΦ[δ] = 0.
Pairing with (N_s, 2Y_s), the term DΦ[c_ε] drops out by [[lem:loc-kid]] (b), which holds for c_ε of class C² vanishing
outside a compact subset of U by [[lem:loc-kid-space]] (b) and integration by parts, and the quadratic term gives
ε²Q(δ). Vacuum data have Φ(D_ε) = 0.

(b) This is [[lem:loc-continuity]] with ρ_1 = 0 and k = 3: by its item (i) the corrections are smooth, and its items
(ii) and (iii) are the displayed identities. If Q(δ_(s_a)) < 0 < Q(δ_(s_b)), the O(ε³) being uniform in s,
m(ε, s_a) < 0 < m(ε, s_b) for ε small, and the intermediate value theorem, applied to the continuous function m(ε, ·)
on [s_a, s_b], gives s(ε) with m(ε, s(ε)) = 0. ∎

### Momentum seeds {#sec:loc-momentum}

On a round slice γ = G dR² + R² dΩ₃² with round second fundamental form K0 = κ0 G dR² + Y0 R² dΩ₃², write an
invariant δK by its components in the frame of [[sec:loc-setting]]:

    δK(e_R, e_R) = δκ,   δK(e_R, e_ϑ) = p̂,   δK(e_ϑ, e_ϑ) = Kt/3 + s1,   δK(e_s, e_s) = Kt/3 + s2,
    δK(e_c, e_c) = Kt/3 − s1 − s2,                                                                    {#eq:loc-dk}

the other components vanishing. Put c := −(κ0 + 2Y0)/(3Y0), β_K := −κ0/(3Y0) and 𝔞 := −3(1 − β_K)/R, so that
3c − 1 = R𝔞.

**Lemma {#lem:loc-momentum-constraints}** (The linearised constraints at δγ = 0.) Let Y0 ≠ 0. For δ = (0, δK),

    Dℋ[δ] = 2(3Y0 δκ + (κ0 + 2Y0) Kt),
    √G Dℳ[δ](e_R) = −∂_R Kt + (3δκ − Kt)/R + (√G/R)(1/sc) ∂_ϑ(sc p̂),
    R Dℳ[δ](e_ϑ) = (1/(√G R³)) ∂_R(R⁴ p̂) − (2/3)∂_ϑ Kt − ∂_ϑδκ + ∂_ϑ s1 + (cot ϑ − 2 tan ϑ) s1 − s2/sc,  {#eq:loc-dm}

and the other components of Dℳ[δ] vanish. So δ is a momentum seed exactly when δκ = c Kt,
∂_R Kt = 𝔞 Kt + (√G/R)(1/sc)∂_ϑ(sc p̂), and

    s2 = sc ((1/(√G R³)) ∂_R(R⁴ p̂) − β_K ∂_ϑ Kt + ∂_ϑ s1 + (cot ϑ − 2 tan ϑ) s1).                        {#eq:loc-s2}

*Proof.* At δγ = 0, Dℋ[δ] = 2 tr K0 tr δK − 2⟨K0, δK⟩ with tr K0 = κ0 + 3Y0, tr δK = δκ + Kt and ⟨K0, δK⟩ = κ0δκ + Y0Kt.
Dℳ[δ] = div δK − d tr δK, with the Christoffel symbols of γ in (R, ϑ, φ1, φ2): Γ^R_RR = G′/(2G), Γ^R_ϑϑ = −R/G,
Γ^R_(φ1φ1) = −R cos²ϑ/G, Γ^R_(φ2φ2) = −R sin²ϑ/G, Γ^ϑ_(Rϑ) = Γ^(φi)_(Rφi) = 1/R, Γ^ϑ_(φ1φ1) = sc, Γ^ϑ_(φ2φ2) = −sc,
Γ^(φ1)_(ϑφ1) = −tan ϑ, Γ^(φ2)_(ϑφ2) = cot ϑ. Inserting the coordinate components of [[eq:loc-dk]] (δK_RR = Gδκ, δK_Rϑ =
√G R p̂, δK_ϑϑ = R²(Kt/3 + s1), δK_(φ2φ2) = R² sin²ϑ (Kt/3 + s2), δK_(φ1φ1) = R² cos²ϑ (Kt/3 − s1 − s2)) gives
[[eq:loc-dm]]; the φ components vanish because nothing depends on φ_i and δK has no mixed φ components. With δκ = cKt,
the combination −(2/3)∂_ϑKt − ∂_ϑδκ is −β_K∂_ϑKt. ∎

**Theorem {#thm:charge-identity}** (The charge of a momentum seed.) Let U be a band of a round slice on which Y0 ≠ 0,
let N > 0 be a function of R, and for a momentum seed δ supported in U put

    Q_N(δ) := ∫_U N((tr δK)² − |δK|²) dvol,      ν := N √G R³,      E := e^(∫𝔞 dR),
    P := 8νE²R/G − (2νER/√G)′ RE/√G,      Γ := 4νE² − P′,  {#eq:charge-identity-defs}

′ = d/dR. Then there is a function η(R, ϑ), compactly supported in R, with

    Kt = E ∂_ϑη/sc,      p̂ = (R/√G) E ∂_Rη/sc,      η = O(sc²),   ∂_ϑη = O(sc),  {#eq:charge-stream}

and, with Z := s2 + s1/2 and X := ∂_ϑη − (3/2)(cos 2ϑ/sc) η,

    Q_N(δ) = −(2π)² ∫∫ [ 2ν sc (Z − Eη/(2sc²))² + (3/2) ν sc (s1 − 2EX/(3sc))²
                         + Γ η²/sin 2ϑ ] dϑ dR.                                                  {#eq:charge-identity}

For N = N_s, Q_N(δ) = Q(δ).

*Proof.* *The stream function.* Since E′ = 𝔞E, the second condition of [[lem:loc-momentum-constraints]] reads
∂_R(sc Kt/E) = ∂_ϑ(√G sc p̂/(RE)). Put η(R, ϑ) := ∫_(R1)^R √G sc p̂/(RE) dR′. Then ∂_Rη is as stated, and
∂_R(∂_ϑη − sc Kt/E) = 0 with both terms vanishing for R near R1, so ∂_ϑη = sc Kt/E. Near the axis ϑ = 0 the
component p̂ = δK(e_R, e_ϑ) is O(sin ϑ). Indeed, in the plane (x3, x4) of [[sec:background]], with polar radius
ϱ = R sin ϑ, e_ϑ is the unit radial direction; along a line through the axis in that plane, the rotation by π in that
plane, an isometry preserving δK, maps the point at ϱ to the point at −ϱ and e_ϑ to −e_ϑ, so ϱ ↦ p̂ is an odd smooth
function on that line, and p̂ = O(ϱ). Likewise p̂ = O(cos ϑ) at ϑ = π/2. Hence ∂_Rη = O(sc²), so η = O(sc²); and
∂_ϑη = sc Kt/E = O(sc), Kt being bounded. For R ≥ R2, ∂_ϑη = 0, so η is constant on each sphere
there, and η = 0 on the axis; so η is compactly supported in R.

*The quadratic form.* Since δγ = 0 and ℳ is linear in K at fixed γ, D²ℳ[δ, δ] = 0 and D²ℋ[δ, δ] = 2((tr δK)² − |δK|²).
From [[eq:loc-dk]] and δκ = cKt, (tr δK)² − |δK|² = (2β_K − 2/3)Kt² − 2p̂² − s1² − s2² − (s1 + s2)², and dvol = √G R³ sc
dR dϑ dφ1 dφ2. So Q_N(δ) = (2π)² ∫∫ 𝔮 dϑ dR with 𝔮 := ν sc [(2β_K − 2/3)Kt² − 2p̂² − s1² − s2² − (s1 + s2)²], and
Q_(N_s) = Q by [[eq:loc-charge]].

*The identity.* Substitute Kt and p̂ from [[eq:charge-stream]] and s2 from [[eq:loc-s2]] into 𝔮 and into the integrand
𝔡 of [[eq:charge-identity]] (with its sign). Then, pointwise,

    𝔮 = 𝔡 + ∂_ϑ 𝔄 + ∂_R 𝔅,
    𝔄 := 2νβ_KE² η ∂_ϑη/sc − 2νE η s1 − νE² (cos 2ϑ/sc²) η²,
    𝔅 := −(P/2) η²/sc − 2νE² (R²/G) η ∂_Rη/sc.                                                      {#eq:charge-flux}

This is an identity between polynomials in η, s1 and their derivatives, with coefficients in R and ϑ, and it is
checked by expanding both sides, using E′ = 𝔞E, 𝔞 = −3(1 − β_K)/R and the definitions of P and Γ, with ν, G and β_K
arbitrary functions of R. It is found by writing s2 = Z − s1/2, integrating by parts the cross terms of η with s2 (in
R) and with s1 and ∂_ϑη (in ϑ), and completing the squares in Z and in s1; 𝔄 and 𝔅 record the integrations by parts.

*The boundary terms.* 𝔅 vanishes for R near R1 and R2. At ϑ → 0 and ϑ → π/2, by [[eq:charge-stream]] and the
boundedness of s1, each term of 𝔄 is O(sc²), so 𝔄 → 0; the integrand of [[eq:charge-identity]] is bounded, since
η/sc², X/sc and s2 are bounded and Γη²/sin 2ϑ = O(sc³). Integrating [[eq:charge-flux]] over (R1, R2) × (0, π/2) gives
[[eq:charge-identity]]. ∎

**Corollary {#cor:loc-charge-momentum}** (The sign for momentum seeds.) If Γ > 0 on U, then Q(δ) < 0 for every nonzero
momentum seed δ on U; precisely, Q(δ) ≤ −(2π)²∫∫ Γη²/sin 2ϑ if η ≠ 0, and Q(δ) = −(2π)²∫∫ ν sc (s1² + s2² + (s1 +
s2)²) < 0 if η = 0.

*Proof.* ν = N_s√G R³ > 0. If η ≠ 0 the first two terms of [[eq:charge-identity]] are nonnegative. If η = 0, then
Kt = p̂ = δκ = 0, and 𝔮 = −ν sc (s1² + s2² + (s1 + s2)²); this vanishes identically only if s1 = s2 = 0, that is
δ = 0. ∎

The positivity of Γ does not depend on the normalisation of E, since Γ scales with E². On every round slice of the
chart, N_s√G = 1 ([[eq:racz-kid]]), so ν = R³ for N = N_s; on a vacuum region of the background
[[lem:margins-gamma-form]] gives Γ/E² in closed form, and where ψ = 0 it gives Γ = 4μ/R for the normalisation
E = √G/R.

**Corollary {#cor:loc-charge-seed}** (Momentum seeds on Σ_τ0.) Let U be a band of Σ_τ0 on which the background is vacuum.
Then Γ > 0 on U, so Q(δ) < 0 for every nonzero momentum seed δ on U, and for ε small no vacuum data on Σ_τ0 of the form
bg + εδ + O(ε²), equal to the background's outside a compact subset of U, exist.

*Proof.* On Σ_τ0, qf < 1, so Y0 = K^l_l/3 < 0 ([[lem:racz-split-formulas]] (b)). By [[prop:bg-region-three-end]] (d), U
lies in region III, {0.70 ≤ R ≤ R_u2}, or in {R ≥ R_*}. In region III, Γ > 0 by [[prop:bg-region-three-end]] (c). On {R ≥
R_*} the points lie in region I ([[lem:margins-region-one]] (c)), where ψ = 0 and Γ/E² = 4R³μ/(R² + μ) > 0
([[lem:margins-gamma-form]]). Then [[cor:loc-charge-momentum]] and [[prop:loc-projection]] (a) apply; a band of Σ_τ0 on
which the background is vacuum has closure in a vacuum region after shrinking it slightly around the compact support. ∎

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

which has the sign of f. On Σ_τ0, where dv̂ = dR, ℓ_out^♭ restricts to (q − q²f/2) dR = (G/2) dR. With N(2 − qf) = √G
and |dR|_γ = G^(−1/2), the data of T on Σ_τ0 are ρ_T := T(n, n) = ϖG/4 and J_T := T(n, ·) = −ρ_T dR/|dR|_γ, and
T(ξ, n) = N_sρ_T + Y_s·J_T. Fix a nonzero invariant dust density ϖ_1 ≥ 0, smooth with compact support in U ∩ {f < 0},
with stress T_1 and data (ρ_1, J_1) := (ρ_(T_1), J_(T_1)); then ∫T_1(ξ, n) dvol < 0. Put
s* := Q(δ)/(2∫T_1(ξ, n) dvol), which is positive. Let Ω_c := supp δ ∪ supp ϖ_1 and U′ ⋐ U a band containing Ω_c; its
closure lies in the interior of the vacuum region, as in the proof of [[cor:loc-charge-seed]]. By [[lem:loc-continuity]]
on U′, with δ_s := δ for s ∈ [0, 2s*], this ρ_1 and k = 3, there are, for ε small, invariant data
D_(ε,s) = bg + εδ + c_(ε,s) of class C², with
‖c_(ε,s)‖_(C²) ≤ Cε², equal to the background's outside a compact subset of U′ independent of ε and s, and a
continuous function m(ε, ·) on [0, 2s*] with

    m(ε, s) 𝔫(ε, s) = ε² (Q(δ) − 2s ∫T_1(ξ, n) dvol) + O(ε³),      𝔫(ε, s) > 0,

uniformly in s, such that, with γ_D the metric of D_(ε,s), [[eq:loc-continuity-res]] holds on U′; as δγ = 0, it reads

    ℋ(D_(ε,s)) = 2ε²s |J_1|_(γ_D) + m(ε, s) 𝔴 N_s,      ℳ(D_(ε,s)) = ε²s J_1 + ½ m(ε, s) 𝔴 γ(Y_s, ·).

Since Q(δ) < 0 and Q(δ) − 4s*∫T_1(ξ, n) dvol = −Q(δ) > 0, we have m(ε, 0) < 0 < m(ε, 2s*) for ε small, and by the
intermediate value theorem m(ε, s(ε)) = 0 for some s(ε) ∈ (0, 2s*). The data D := D_(ε,s(ε)) then satisfy, on U,
ℋ(D) = 2ρ and ℳ(D) = J, with ρ := ε²s(ε)|J_1|_(γ_D) ≥ 0 and J := ε²s(ε)J_1 = −ρ dR/|dR|_(γ_D). These are the data of
outgoing radial null dust. Indeed, for a null dust T = ϖ ℓ^♭ ⊗ ℓ^♭ and the future unit normal n̂ of a slice, writing
ℓ = a_ℓ(n̂ + ν) with a_ℓ > 0 and ν a unit vector tangent to the slice gives (T(n̂, n̂), T(n̂, ·)) = (ϖa_ℓ², −ϖa_ℓ²ν^♭);
so the data (ρ, −ρν^♭) with ρ ≥ 0 are those of null dust moving along ν, here with ν^♭ = dR/|dR|_(γ_D), the outward
unit conormal of the spheres R = const for γ_D. So D are exact Einstein–null-dust data, equal to the background's
outside U, with outgoing radial null dust of energy density ε²s(ε)|J_1|_(γ_D) = ε²s(ε)ρ_1(1 + O(ε)) ≥ 0, supported in
the support of ϖ_1. ∎

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

**Lemma {#lem:loc-tt-second}** (The second variation of the scalar curvature of S³.) Let T be a smooth transverse
trace-free symmetric 2-tensor on the unit S³ with Δ̂T = −k_T²T, and put D²Scal_γ̂[T, T] := d²/dε² Scal(γ̂ + εT) at ε = 0.
Then

    ∫_(S³) D²Scal_γ̂[T, T] dvol_γ̂ = (1 − k_T²/2) ∫_(S³) |T|²_γ̂ dvol_γ̂.                             {#eq:loc-tt-second}

*Proof.* For a family g + εh of metrics on a closed manifold, the Levi-Civita connection varies by δΓ^k_ij = ½(∇_ih_j^k +
∇_jh_i^k − ∇^kh_ij), and Palatini's identity Ric′[h]_ij = ∇_kδΓ^k_ij − ∇_jδΓ^k_ki gives

    Ric′[h]_ij = ½(∇^k∇_ih_jk + ∇^k∇_jh_ik − ∇^k∇_kh_ij − ∇_i∇_j tr h),

whose trace gives the first variation DScal[h] = div div h − Δ tr h − ⟨h, Ric⟩ of the scalar curvature. Integrating, the
divergences drop out and

    d/dε ∫ Scal(g_ε) dvol_(g_ε) = ∫ (DScal_(g_ε)[h] + ½ Scal(g_ε) tr_(g_ε) h) dvol_(g_ε)
                                = ∫ ⟨𝔊(g_ε), h⟩_(g_ε) dvol_(g_ε),

g_ε := g + εh, 𝔊(g) := ½ Scal(g) g − Ric(g). Take g = γ̂ and h = T, and let ℰ(ε) := ∫ Scal(γ̂ + εT) dvol_(γ̂+εT); all
integrals below are over S³ against dvol_γ̂. Since Ric(γ̂) = 2γ̂ and Scal(γ̂) = 6, 𝔊(γ̂) = γ̂ and DScal[T] = −⟨T,
Ric(γ̂)⟩ = −2 tr T = 0. The Riemann tensor of the unit S³ is γ̂_ikγ̂_jl − γ̂_ilγ̂_jk, and the Ricci identity gives, for
trace-free T, ∇^k∇_iT_jk = ∇_i∇^kT_jk + 3T_ij = 3T_ij; so Ric′[T] = ½(6T − Δ̂T) = ½(6 + k_T²)T. Differentiating ℰ′(ε) =
∫⟨𝔊(γ̂ + εT), T⟩_(γ̂+εT) dvol_(γ̂+εT) at ε = 0, the derivative of 𝔊 is ½DScal[T]γ̂ + ½Scal(γ̂)T − Ric′[T] = −(k_T²/2)T,
the two inverse metrics in ⟨γ̂, T⟩ contribute −2|T|²_γ̂, and the variation ½ tr T dvol_γ̂ of the volume contributes ½⟨γ̂,
T⟩ tr T = 0; so ℰ″(0) = −(k_T²/2 + 2)∫|T|²_γ̂. On the other hand

    dvol_(γ̂+εT) = (1 + ½ε tr T + ε²(⅛(tr T)² − ¼|T|²_γ̂) + O(ε³)) dvol_γ̂ = (1 − ¼ε²|T|²_γ̂ + O(ε³)) dvol_γ̂

and Scal(γ̂ + εT) = 6 + ½ε² D²Scal_γ̂[T, T] + O(ε³), so ℰ″(0) = ∫ D²Scal_γ̂[T, T] − 3∫|T|²_γ̂. Comparing the two values
of ℰ″(0) gives [[eq:loc-tt-second]]. ∎

**Lemma {#lem:loc-tensor-variations}** (Second variations for tensor data on a round slice.) Let γ = G dR² + R²γ̂ and
K0 = κ0 G dR² + Y0 R² γ̂ be round data on a band, with G > 0, κ0 and Y0 smooth functions of R. Let T be as in
[[lem:loc-tt-second]], H and Π smooth functions of R, h := 2R²H T and k := R²(Π + 2Y0H) T. For a function X of the data
write [X]_2 for the ε² coefficient of X(γ + εh, K0 + εk), and write ′ := d/dR. Then, with ℳ_R := ℳ(∂_R) the radial
component of the momentum constraint and |T|²_γ̂ the pointwise norm, a function on S³,

    [(tr K)² − |K|²]_2 = −(Π² + 4(κ0 + 2Y0)HΠ) |T|²_γ̂,
    [ℳ_R]_2 = (2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′) |T|²_γ̂,
    ∫_(S³) [Scal]_2 dvol_γ̂ = ((2 − k_T²)H²/R² + (16HH′/R − H′²)/G + 4G^(−1/2)(G^(−1/2)HH′)′) ∫_(S³) |T|²_γ̂ dvol_γ̂.
                                                                                             {#eq:loc-tensor-variations}

*Proof.* Let T^♯ be the endomorphism of the tangent spaces of the spheres with γ̂(T^♯X, Z) = T(X, Z); then tr T^♯ = 0 and
tr (T^♯)² = |T|²_γ̂. The tensors h and k have no radial components, and on the spheres γ⁻¹h = 2HT^♯ and γ⁻¹k = (Π +
2Y0H)T^♯. Let A_ε := (γ + εh)⁻¹(K0 + εk), as an endomorphism. It is κ0 on ∂_R, and on the spheres, since (1 + 2εHT^♯)⁻¹ =
1 − 2εHT^♯ + 4ε²H²(T^♯)² + O(ε³),

    A_ε = Y0 + εΠT^♯ − 2ε²HΠ(T^♯)² + O(ε³).

So tr A_ε = κ0 + 3Y0 − 2ε²HΠ|T|²_γ̂ + O(ε³) and tr A_ε² = κ0² + 3Y0² + ε²(Π² − 4Y0HΠ)|T|²_γ̂ + O(ε³), the terms of order
ε vanishing with tr T^♯. Since (tr K)² − |K|² = (tr A_ε)² − tr A_ε², this gives the first identity.

For the second, let γ = G dR² + g with g = g(R) a family of metrics on S³, and K with K(∂_R, ∂_A) = 0, K(∂_R, ∂_R) = κG
for a function κ of R, and spherical part 𝒦. The Christoffel symbols Γ^R_RR = G′/(2G), Γ^R_AB = −g′_AB/(2G), Γ^A_RB =
½(g⁻¹g′)^A_B and Γ^A_RR = Γ^R_RA = 0 give (div K)_R = κ′ + ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′g⁻¹𝒦), and tr K = κ + tr(g⁻¹𝒦), so
that

    ℳ_R = ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′ g⁻¹𝒦) − (tr g⁻¹𝒦)′.

Along the family, g = R²(γ̂ + 2εHT), g⁻¹g′ = 2/R + 2εH′T^♯ − 4ε²HH′(T^♯)² + O(ε³), and g⁻¹𝒦 is A_ε on the spheres. The ε²
coefficients of the three terms are −2κ0HH′|T|²_γ̂, −½(−4HΠ/R + 2H′Π − 4Y0HH′)|T|²_γ̂ and 2(HΠ)′|T|²_γ̂, whose sum is the
second identity.

For the third, consider a metric G dR² + R²ĝ with ĝ = ĝ(R) a family of metrics on S³. For a foliation by hypersurfaces
S with unit normal ν, lapse N and second fundamental form L, the Gauss equation Scal = Scal_S + 2Ric(ν, ν) −
(tr L)² + |L|² and the Riccati equation Ric(ν, ν) = −ν(tr L) − |L|² − N⁻¹Δ_S N hold, as in the proof of
[[lem:constraints-evolution]] (a). The lapse G^(1/2) of the foliation by the spheres {R = const} is constant on each
sphere, so the last term vanishes and

    Scal = R⁻² Scal(ĝ) − (tr L)² − |L|² − 2G^(−1/2)(tr L)′,      L := ½G^(−1/2) ∂_R(R²ĝ),

L the second fundamental form of the spheres with respect to the unit normal G^(−1/2)∂_R. For ĝ = γ̂ + 2εHT, as an
endomorphism L = G^(−1/2)(1/R + εH′T^♯ − 2ε²HH′(T^♯)²) + O(ε³), so that tr L = G^(−1/2)(3/R − 2ε²HH′|T|²_γ̂) + O(ε³)
and |L|² = G⁻¹(3/R² + ε²(H′² − 4HH′/R)|T|²_γ̂) + O(ε³). The ε² coefficients of the last three terms of Scal are therefore
12HH′|T|²_γ̂/(RG), −(H′² − 4HH′/R)|T|²_γ̂/G and 4G^(−1/2)(G^(−1/2)HH′)′|T|²_γ̂. The ε² coefficient of the first term is
R⁻² times half of D²Scal_γ̂[2HT, 2HT] = 4H²D²Scal_γ̂[T, T], whose integral over S³ is, by [[lem:loc-tt-second]], R⁻²(2 −
k_T²)H²∫|T|²_γ̂. Adding gives the third identity. ∎

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

(iii) By [[lem:racz-split-formulas]] (b), K^l_l = 3n^R/R = 3Y0, so n^R = RY0 and δ = (h, k) is the variation of
[[lem:loc-tensor-variations]]. In [[eq:loc-charge]], D²ℋ[δ, δ] = 2[ℋ]_2, D²ℳ[δ, δ] = 2[ℳ]_2, Y_s·ℳ = Y_s^R ℳ_R and dvol =
√G R³ dR dvol_γ̂, and ∫_(S³) |T|²_γ̂ dvol_γ̂ = (2π)²|T|². So [[eq:loc-tensor-variations]] and G⁻¹ = N_s² ((ii)) give,
with ′ := d/dR,

    Q(δ) = (2π)²|T|² ∫ R³√G (N_s 𝔥 + 2Y_s^R 𝔪) dR,
    𝔥 := (2 − k_T²)H²/R² + N_s²(16HH′/R − H′²) + 4N_s(N_sHH′)′ − 4(κ0 + 2Y0)HΠ − Π²,
    𝔪 := 2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′.                                             {#eq:loc-tensor-density}

Since ξ is a Killing field, for X, Z tangent to Σ, 0 = g(∇_Xξ, Z) + g(∇_Zξ, X) = 2N_sK0(X, Z) + (L_(Y_s)γ)(X, Z), because
g(∇_X(N_sn), Z) = N_sK0(X, Z) and the tangential part of ∇_XY_s is D_XY_s. The components of this equation on the spheres
and on ∂_R are 2RY_s^R = −2N_sY0R² and Y_s^R G′ + 2G(Y_s^R)′ = −2N_sκ0G. With y_s := Y_s^R/N_s = √G Y_s^R they read

    Y0 = −y_s/R,        κ0 = −y_s′,                                                             {#eq:loc-tensor-kid}

and (ii) reads N_s² − y_s² = f. We collect the integrand of [[eq:loc-tensor-density]], using N_s√G = 1 and √G Y_s^R =
y_s. The terms in Π², ΠH′ and H′² are −R³Π², −2R³y_sΠH′ and −R³N_s²H′². The terms in HΠ and HΠ′ are

    −4R³(κ0 + 2Y0)HΠ + 4R²y_sHΠ + 4R³y_s(HΠ)′ = (4R³y_sHΠ)′ − 4R³(κ0 + y_s′ + 2Y0 + 2y_s/R)HΠ = (4R³y_sHΠ)′,

by [[eq:loc-tensor-kid]]. Writing 4R³N_s(N_sHH′)′ = (4R³N_s²HH′)′ − 4N_s(R³N_s)′HH′, the terms in H², HH′ and HH″ are

    (2 − k_T²)RH² + (16R²N_s² − 4N_s(R³N_s)′ + 4R³y_s(Y0 − κ0))HH′ + (4R³N_s²HH′)′,

and by [[eq:loc-tensor-kid]] the coefficient of HH′ is 4R²(N_s² − y_s²) − 2R³(N_s² − y_s²)′ = 4R²f − 2R³f′ = 4R² − 8μ,
since f = 1 − μ/R². With (4R² − 8μ)HH′ = ((2R² − 4μ)H²)′ − 4RH², these terms are −(k_T² + 2)RH² + (4R³N_s²HH′ + (2R² −
4μ)H²)′. Altogether

    R³√G (N_s 𝔥 + 2Y_s^R 𝔪) = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH² + 𝔅_T′,
    𝔅_T := 4R³N_s²HH′ + 4R³y_sHΠ + 2(R² − 2μ)H².                                            {#eq:loc-tensor-flux}

On the other hand, ξ(H) = N_sΠ + Y_s^RH′, |dH|² = −Π² + N_s²H′² and g(ξ, n) = −N_s give

    −2T_m(ξ, n)√G = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH².

Since 𝔅_T has compact support in (R1, R2), integrating [[eq:loc-tensor-flux]] in R gives [[eq:loc-tensor-charge]].

(iv) With g(ξ, n) = −N_s, T_m = R³(½N_sΠ² + Y_s^RΠ ∂_RH + (N_s/(2G))(∂_RH)²) + ½N_s(k_T² + 2)RH², and the
determinant is R⁶(N_s² − G(Y_s^R)²)/(4G) = R⁶f/(4G) by (ii). ∎

The quantity T_m is the flux through Σ of J^a = 𝕋^a_b ξ^b for 𝕋_ab := R³(∂_aH ∂_bH − ½g_ab|dH|²) − ½g_ab(k_T² +
2)RH², the canonical stress of the tensor master equation D_a(R³D^aH) − (k_T² + 2)RH = 0 of the orbit space
([[thm:std-ki-master]] (1), with n = 3, K = 1).

**Lemma {#lem:loc-tensor-sign}** (Tensor seeds of either sign.) In the setting of [[thm:loc-tensor]]:

(a) if Π = −(Y_s^R/N_s) ∂_RH, then Q(δ) = −(2π)²|T|² ∫ (R³ f (∂_RH)² + (k_T² + 2) R H²) dR;

(b) if H = 0, then Q(δ) = −(2π)²|T|² ∫ R³ Π² dR < 0 unless Π = 0;

(c) if f < 0 on an interval I ⊂ (R1, R2) and H_ω := β_I(R) sin(ωR) for a smooth bump β_I ≥ 0 supported in I, then
in (a) Q(δ) = ½(2π)²|T|²ω² ∫ R³|f|β_I² dR + O(ω) > 0 for ω large.

*Proof.* (a) ξ(H) = N_sΠ + Y_s^R∂_RH = 0, and |dH|² = (∂_RH)²(1/G − (Y_s^R)²/N_s²) = (∂_RH)² f/(N_s²G) by
[[thm:loc-tensor]] (ii). So T_m = ½N_s(R³f(∂_RH)²/(N_s²G) + (k_T² + 2)RH²), and with N_s√G = 1, 2T_m√G =
R³f(∂_RH)² + (k_T² + 2)RH². (b) ξ(H) = N_sΠ and |dH|² = −Π², so 2T_m√G = R³Π². (c) ∂_RH_ω = ωβ_I cos(ωR) +
β_I′ sin(ωR), so (∂_RH_ω)² = ω²β_I² cos²(ωR) + O(ω) uniformly, and cos²(ωR) = (1 + cos 2ωR)/2. One integration by
parts, β_I having compact support, gives ∫R³fβ_I² cos 2ωR dR = −(2ω)⁻¹∫(R³fβ_I²)′ sin 2ωR dR = O(ω⁻¹). So
∫R³f(∂_RH_ω)² dR = (ω²/2)∫R³fβ_I² dR + O(ω), while ∫(k_T² + 2)RH_ω² dR = O(1); as f = −|f| on I, (a) gives the
stated formula. ∎

**Theorem {#thm:loc-inside}** (Inside the apparent horizon.) Let U be a band of Σ_τ0 on which the background is vacuum
and which meets {f < 0}. Then:

(a) there are non-gauge seeds of tensor type on U with Q > 0 and with Q < 0;

(b) for every small ε > 0 there are exact invariant vacuum data on Σ_τ0, equal to the background's outside a compact
subset of U, of the form bg + εδ_ε + O(ε²) with δ_ε a non-gauge seed; δ_ε tends to a nonzero tensor seed as ε → 0.

*Proof.* Let T := T_0 of [[lem:loc-harmonics]] (c) and I ⊂ U ∩ {f < 0} an interval. (a) [[lem:loc-tensor-sign]] (c) gives
Q > 0 and (b) gives Q < 0. A gauge seed has a vanishing transverse trace-free part: its data are the variation of (γ, K0)
along a vector field Z = N_Z n + X_Z, (2N_Z K0 + L_(X_Z)γ, L_(X_Z)K0 + D²N_Z + N_Z 𝔯) with 𝔯 a round tensor built from
Ric(γ) and K0, and for invariant Z the angular trace-free parts of these are (D̂D̂ − (1/3)γ̂Δ̂) of scalars, the class
1-forms being exact ([[lem:loc-harmonics]] (a)), and so orthogonal to T. The generator may be taken invariant: if Z
generates an invariant seed, so does its average over the compact group T² × Z2 × Z2, since the seed generated depends
linearly on Z and the isometries of the group carry the seed generated by Z to that generated by the image of Z; and the
average keeps the properties of Z near the boundary spheres of [[def:loc-charge]], ξ being invariant. A seed of
[[thm:loc-tensor]] with (H, Π) ≠ 0 has a nonzero transverse trace-free part, so it is non-gauge.

(b) Let H := H_ω of [[lem:loc-tensor-sign]] (c) with ω so large that the seed δ_1 with Π = −(Y_s^R/N_s)∂_RH has
Q(δ_1) > 0, let Π_0 ≠ 0 be a bump in I, δ_0 the seed with (0, Π_0), and δ_s := (sH, −s(Y_s^R/N_s)∂_RH + (1 − s)Π_0)
for s ∈ [0, 1]. Every δ_s is a nonzero tensor seed, hence non-gauge, and Q(δ_s) is a quadratic polynomial in s with
Q(δ_0) < 0 < Q(δ_1), so with exactly one root s_* in (0, 1), at which it changes sign; s_* is simple, as a double root
of a quadratic does not change its sign, and |Q(δ_s)| ≥ c|s − s_*| on [0, 1] for some c > 0. [[prop:loc-projection]] (b)
on [0, 1] gives s(ε) and the data; at s(ε), ε²Q(δ_(s(ε))) = O(ε³) with the O(ε³) uniform in s, so s(ε) = s_* + O(ε),
and δ_ε := δ_(s(ε)) → δ_(s_*) ≠ 0. ∎

The charge Q vanishes on a whole cone of non-gauge seeds inside the apparent horizon. For a seed δ_0 on that cone whose
bilinear form 𝔟(δ_0, ·) := ½(Q(δ_0 + ·) − Q(δ_0) − Q(·)) is not identically zero, take a seed δ′ with
𝔟(δ_0, δ′) ≠ 0. Then Q(δ_0 + sδ′) = 2s𝔟(δ_0, δ′) + s²Q(δ′), and [[prop:loc-projection]] (b), applied to
δ_s := δ_0 + sδ′ on s ∈ [−1, 1], gives m(ε, s)𝔫(ε, s) = ε²(2s𝔟(δ_0, δ′) + s²Q(δ′)) + O(ε³) uniformly in s; at
s = ±k_0ε this is ±2k_0ε³𝔟(δ_0, δ′) + O(ε³), of opposite signs for a large number k_0, and the intermediate value
theorem on [−k_0ε, k_0ε] gives data bg + εδ_0 + O(ε²). Seeds in the radical of Q are not treated.

### Outside the apparent horizon {#sec:loc-outside}

**Lemma {#lem:loc-gauge-unique}** (Linearised vacuum solutions with zero data.) Let (𝒰, g) be a globally hyperbolic
Ricci-flat Lorentzian manifold, S a smooth spacelike Cauchy hypersurface with future unit normal n, and k a smooth
symmetric 2-tensor on 𝒰 with DRic(k) = 0 that induces zero linearised data on S: the first variations of the induced
metric and of the second fundamental form of S vanish. Then k = L_X g for a smooth vector field X on 𝒰.

*Proof.* We use [[lem:ix-2-1]], whose proof uses of the metric only that it is Ricci-flat, with S in place of the
hypersurface there, and its notation −Υ̇⁰(k)_ν = −∇^λk_λν + ½∇_ν tr_g k. Let Y be the vector field on S with
Y^♭ = k(n, ·) + ½k(n, n)n^♭, and, by [[lem:ix-1-1]] with the normally hyperbolic operator 2δ_gG_gδ*_g = −∇^α∇_α on
1-forms ([[lem:ix-2-1]] (a)), w the smooth 1-form on 𝒰 with 2δ_gG_gδ*_g w = −Υ̇⁰(k), w|_S = 0 and ∇_n w|_S = Y^♭. Put
X := w^♯ and h := k − L_X g. Since −Υ̇⁰(L_X g) = δ_gG_g(2δ*_g w) = −Υ̇⁰(k), Υ̇⁰(h) = 0 on 𝒰. By [[lem:ix-2-1]] (e), h = 0
on S; h induces zero linearised data, as k does and L_X g does by [[lem:ix-2-1]] (f); so (∇_n h)(e_i, e_j) = 0 for e_i,
e_j tangent to S by [[lem:ix-2-1]] (c), and then (∇_n h)(n, ·) = 0 by [[lem:ix-2-1]] (d) and Υ̇⁰(h) = 0. Finally
DRic(h) = 0 by [[lem:ix-2-1]] (b), so 2L⁰h = 0, L⁰ := DRic − δ*_gΥ̇⁰ being normally hyperbolic ([[lem:ix-2-1]] (a)),
with h|_S = 0 and ∇_n h|_S = 0; [[thm:std-bgp-cauchy]] (3) gives h = 0. ∎

**Lemma {#lem:loc-transfer}** (From the slice to a static slice.) Let U ⊂ {f > 0} be a band of Σ_τ0 on which the
background is vacuum, of mass μ, with the radial extent of supp δ equal to [R1′, R2′], and let δ be a seed on U. Extend
the slice to a Cauchy surface of the maximally extended Tangherlini spacetime M_μ, and let h be the linearised vacuum
solution with data δ in a harmonic gauge with invariant compactly supported gauge data, so that h is invariant and supp
h ⊂ J(supp δ). Then:

(1) Q(δ) = 2∫_Σ Ein²[h](ξ, n) dvol, Ein²[h] the ε² coefficient of Ein(g + εh);

(2) J^a := Ein²[h]^(ab) ξ_b is divergence-free;

(3) for a suitable static slice {t = t_1} of the exterior, h's data there are compactly supported, Q(δ) =
Q_static(h|_(t = t_1)), the charge [[eq:loc-charge]] on that slice, and δ is a gauge seed exactly when h|_(t = t_1) is,
in the sense of [[def:loc-charge]] on the static slice, all of whose bands are vacuum.

*Proof.* (1) For g_ε := g + εh with data (γ_ε, K_ε), normal n_ε and ξ = N_ε n_ε + Y_ε, [[lem:loc-kid]] (a) gives
N_sℋ + 2Y_s·ℳ = 2Ein_ε(ξ, n_ε) + (N_s − N_ε)ℋ + 2(Y_s − Y_ε)·ℳ, and the last two terms are O(ε³), since Ein_ε =
O(ε²) (Ein(g) = 0 and Ein¹[h] = 0). The ε² coefficient of the left side is ½(N_sD²ℋ + 2Y_s·D²ℳ)[δ, δ] + N_sDℋ[δ_2] +
2Y_s·Dℳ[δ_2], δ_2 the compactly supported second variation of the data, which pairs to zero by [[lem:loc-kid]] (b).
(2) The ε² coefficient of ∇^(ε)_a Ein_ε^(ab) = 0, with Ein¹[h] = 0, is ∇_a Ein²[h]^(ab) = 0, and ∇_(a ξ_b) = 0.
(3) In Kruskal coordinates (U_K, V_K) of the exterior, both increasing to the future, the slice is a curve along which
U_K decreases and V_K increases with R. The support supp δ lies in U_K ∈ [U_K(R2′), U_K(R1′)], V_K ∈
[V_K(R1′), V_K(R2′)], and J^±(supp δ) lie in {U_K ≥ U_K(R2′), V_K ≥ V_K(R1′)} and {U_K ≤ U_K(R1′), V_K ≤ V_K(R2′)},
causal curves projecting to causal curves of the orbit space. The rectangles S_in := {U_K(R1′) < U_K < 0, 0 < V_K <
V_K(R1′)} and S_out := {U_K < U_K(R2′), V_K > V_K(R2′)} meet neither. A static slice is a ray V_K = c|U_K|. Take R_a ∈
(√μ, R1′) on the slice and c ∈ (V_K(R_a)/|U_K(R1′)|, V_K(R1′)/|U_K(R1′)|); the ray meets S_in at a point U_K = U_s
slightly above U_K(R1′) with c|U_s| ∈ (V_K(R_a), V_K(R1′)), and S_out at every U_s′ with |U_s′| > max(|U_K(R2′)|,
V_K(R2′)/c); take R_b on the slice with |U_K(R_b)| > |U_s′| and V_K(R_b) > c|U_s′|. Let Σ″ consist of the slice up to
R_a, the segment to (U_s, c|U_s|), which lies in S_in with ΔU_K < 0 < ΔV_K and is spacelike, the ray to U_s′, the
segment to the slice at R_b, in S_out and spacelike, and the slice beyond R_b. Σ″ is spacelike and equals the slice
outside a compact set, so by (2) and the divergence theorem its J-flux is Q(δ). h vanishes on the two segments, and
J(supp δ) meets the ray only inside the part used; near the bifurcation sphere and beyond, the static slice does not
meet J(supp δ). So the flux is that through the whole static slice, which is Q_static of h's data there by (1).

*The last clause.* Let Σ̂ be the extension of Σ_τ0, and Σ_s* the static slice {t = t_1} continued through the
bifurcation sphere into the other exterior: the image of {t = 0} under the flow of ξ, an isometry, so a Cauchy surface
of M_μ. The slice Σ̂ meets S_out × S³ in its points with R > R2′ and S_in × S³ in those with √μ < R < R1′; the static
ray meets S_in × S³ between the bifurcation sphere and U_K = U_s, and S_out × S³ beyond U_K = U_s′; and h vanishes on
the open sets S_in × S³ and S_out × S³, which J(supp δ) does not meet.

Suppose that h's data on the static slice are a gauge seed, with a band U_s″ of the static slice and a generator
Z_s, equal to c_s ξ near the inner sphere of ∂U_s″ and to 0 near the outer one. Let Ẑ be a smooth vector field on
M_μ equal, near Σ_s*, to Z_s near Ū_s″, to c_s ξ on the part of Σ_s* inside U_s″, and to 0 outside it; ξ is a
Killing field of all of M_μ. Then L_Ẑ g induces h's data on Σ_s*: on U_s″ by hypothesis, the data being smooth
functions of the 1-jet of the metric, and elsewhere both vanish, Ẑ being zero or Killing there. By
[[lem:loc-gauge-unique]], h − L_Ẑ g = L_X g for a smooth vector field X, so h = L_(Z_h) g with Z_h := Ẑ + X. As
h = 0 on S_in × S³ and on S_out × S³, Z_h is a Killing field there. Its average Z̄_h over T² × Z2 × Z2 satisfies
L_(Z̄_h) g = h too, the group acting by isometries that fix h, and it is an invariant Killing field on these two
sets. They are connected and lie in the chart of [[lem:racz-split-formulas]] (d), where the argument of the proof
of [[lem:loc-kid]] (c), which is local, gives Z̄_h = c_in ξ on S_in × S³ and Z̄_h = c_out ξ on S_out × S³ for
constants c_in and c_out. So Z := Z̄_h − c_out ξ satisfies L_Z g = h and generates δ on Σ̂; it vanishes on S_out
× S³ and equals (c_in − c_out)ξ on S_in × S³. For η > 0 small, U″ := {R1′ − η < R < R2′ + η} has supp δ ⊂ U″ and
Ū″ ⊂ U, its outer boundary sphere lies in S_out × S³ and its inner one in S_in × S³, as U ⊂ {f > 0}; so δ is a
gauge seed. The converse is the same argument with Σ̂ and Σ_s* exchanged: from a generator of δ, extended by c ξ
on the inner part of Σ̂ and by 0 on the outer part, [[lem:loc-gauge-unique]] and the averaging give an invariant
Z̄_h with h = L_(Z̄_h) g, equal to c_in ξ on S_in × S³ and to c_out ξ on S_out × S³; and Z̄_h − c_out ξ generates
h's data on a band of the static slice whose boundary spheres lie in S_in × S³ and in S_out × S³. ∎

On a static slice, γ = dR²/f + R² dΩ₃², N_s = √f, K0 = 0 and Y_s = 0,
D²ℋ[(h, k), (h, k)] = D²Scal[h, h] + 2((tr k)² − |k|²), the mixed terms carrying K0, and the linearised constraints
decouple into DScal[h] = 0 and D^i(k_ij − tr k γ_ij) = 0. So Q = −𝔈_V(h) − 𝔈_K(k), with

    𝔈_V(h) := −½ ∫ N_s D²Scal[h, h] dvol,      𝔈_K(k) := ∫ N_s (|k|² − (tr k)²) dvol.  {#eq:loc-static-energies}

**Lemma {#lem:loc-gauge-invariance}** (Gauge invariance.) For a vector field X and a function ψ_g of compact support,
𝔈_V(h + L_Xγ) = 𝔈_V(h) when DScal[h] = 0, and 𝔈_K(k + k_ψ) = 𝔈_K(k) when D^i(k_ij − tr k γ_ij) = 0, where k_ψ :=
D²ψ_g − ψ_g Ric(γ).

*Proof.* Differentiating Scal(φ_t*(γ + sh)) = φ_t* Scal(γ + sh), φ_t the flow of X, at s = t = 0 gives DScal[L_Xγ] =
X(Scal) = 0 and D²Scal[h, L_Xγ] = X(DScal[h]) − DScal[L_Xh]. So the cross term of 𝔈_V(h + L_Xγ) is
−∫N_s D²Scal[h, L_Xγ] = −∫N_s X(DScal[h]) + ∫N_s DScal[L_Xh] = ∫ div(N_sX) DScal[h] + ∫⟨(DScal)*N_s, L_Xh⟩ = 0, using
DScal[h] = 0 and (DScal)*N_s = D²N_s − ΔN_s γ − N_s Ric(γ) = 0, the static vacuum equation; the quadratic term
−½∫N_s D²Scal[L_Xγ, L_Xγ] = ½∫N_s DScal[L_XL_Xγ] vanishes in the same way, as DScal[L_Xγ] = 0. For 𝔈_K, the
bilinear form B(k, k_ψ) = ∫N_s(⟨k, k_ψ⟩ − tr k tr k_ψ) dvol is, after two integrations by parts, ∫ψ_g (2dN_s·ℳ[k] +
N_s div ℳ[k]) dvol with ℳ[k] := D^jk_ji − D_i tr k, which vanishes when ℳ[k] = 0; and ℳ[k_ψ] = D^j(D_jD_iψ_g −
ψ_g Ric_ij) − D_i(Δψ_g − ψ_g Scal) = 0 by the contracted Bianchi identity and Scal = 0, so B(k_ψ, k_ψ) = 0. ∎

**Lemma {#lem:loc-scalar-reduction}** (The scalar modes.) On the static slice put ς := μ/R², so that f = 1 − ς and Rf′ =
2ς, and write ′ := d/dR. A class seed is a sum of scalar modes, tensor modes and an l = 0 part, and 𝔈_V, 𝔈_K and the
constraints split mode by mode. Write a scalar mode of degree l = 2j ≥ 2 as h_RR = aS, h_Rϑ = R b ∂_ϑS, h|_(S³) =
R²(cSγ̂ + eŜ), its other components vanishing, with S := P_j(cos 2ϑ), k² := l(l + 2), Ŝ := D̂D̂S + (k²/3)γ̂S, and k
likewise with (p, q_k, w, z) in place of (a, b, c, e); put ‖S‖² := ∫_0^(π/2) S² sc dϑ, m := k² − 3 and H_KI := m + 6ς.

(a) The vector field X = α̃S∂_R + β̃ ∂_ϑS ∂_ϑ shifts (a, b, c, e) by ((1/f)′α̃ + 2α̃′/f, α̃/(Rf) + Rβ̃′, 2α̃/R −
(2k²/3)β̃, 2β̃), so that b = e = 0 is reached by β̃ = −e/2 and α̃ = −Rf(b − Re′/2); the quantities A := a + (1/f)′α̃ +
2α̃′/f and F := c/2 − fb + k²e/6 + fRe′/2 are gauge invariant. The direction k_ψ with ψ_g = ψS has trace-free angular
part ψŜ, so z = 0 is reached by ψ = −R²z. Both gauges are local in R.

(b) For z = 0 the momentum constraint of the mode is ℳ = 𝔪_R S dR + 𝔪_ϑ ∂_ϑS dϑ, with

    𝔪_R := (3fp − 3w − k²q_k)/R − 3w′,        𝔪_ϑ := (4 − 3ς)q_k − fp + Rf q_k′ − 2w.                {#eq:loc-mom-modes}

With Z := R³(w − fq_k), the map Z ↦ (q_k, w, p) = (−3Z′/(R²H_KI), Z/R³ + fq_k, ((4 − 3ς)q_k + Rf q_k′ − 2w)/f) solves
the constraint, every compactly supported solution is the image of its own Z, and on the constraint

    𝔈_K = (2π)² ‖S‖² ∫ 6k²m Z²/(R³H_KI²) dR.                                                           {#eq:loc-ek}

(c) For b = e = 0 put A := a and F := c/2. Then DScal[h] = C(A, F) S, with

    C(A, F) := R⁻²((k² + 6 + 6ς)fA + 3Rf²A′ + 4(k² − 3)F − 6R(1 + 3f)F′ − 6R²fF″),                       {#eq:loc-c}

and 𝔈_V(h) = (2π)² ‖S‖² ∫ E_V(A, F) dR, with

    E_V(A, F) := Rf²(k²/2 + 6 + 12ς)A² + 6R²f³AA′ − 3R³f²A′F′ − 6R³f²AF″ − 12R²f(1 + f)AF′
                 + 3k²RfAF + (10k² − 24)RF² − 12R³fFF″ − 12R²(1 + 3f)FF′.                                {#eq:loc-ev-af}

With ℓ := A − (2R/f)F′ + (2H_KI/(3f²))F and κ_M := (k² + 6 + 6ς)/(3Rf),

    ℓ′ + κ_Mℓ − (2k²H_KI/(9Rf³)) F = (R/(3f²)) C(A, F),                                                {#eq:loc-moncrief}

so the map ℓ ↦ (A, F), F = 9Rf³(ℓ′ + κ_Mℓ)/(2k²H_KI), A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F, solves C = 0, and every
compactly supported solution is the image of its own ℓ. With Φ_M := R^(3/2)f²ℓ/H_KI, on the constraint,

    𝔈_V = (2π)² ‖S‖² (27m/(2k²)) ∫ (f Φ_M′² + Qp Φ_M²/(16R²H_KI²)) dR,
    Qp := 1296ς³ + (624m − 144)ς² + 36m(m − 12)ς + 16m³ + 60m².                                          {#eq:loc-ev}

(d) The l = 0 part of a seed is a gauge seed and contributes nothing to 𝔈_V and 𝔈_K: on the constraint, h_(l=0) =
L_(R𝔤∂_R)γ for a compactly supported function 𝔤 of R, and k_(l=0) = k_ψ with ψ_g := −N_s ∫_R^∞ R′w(R′)/(f(R′)N_s(R′))
dR′, where k_(l=0)|_(S³) = R²wγ̂; ψ_g vanishes beyond the support and is a constant multiple of N_s on its inner side.

*Proof.* *The static slice.* Here γ = f⁻¹dR² + R²γ̂, N_s = √f, K0 = 0 and Y_s = 0. The Christoffel symbols of γ are
Γ^R_RR = −ς/(Rf), Γ^R_AB = −Rf γ̂_AB, Γ^A_RB = δ^A_B/R and Γ^A_BC = Γ̂^A_BC, the others vanishing; Ric(γ) = −(3ς/(R²f))
dR² + ς γ̂ and Scal(γ) = 0; and N_s dvol = R³ dR dvol_γ̂. Integrals over S³ are against dvol_γ̂; for a class harmonic S
of degree l, Δ̂S = −k²S, ∫S² = (2π)²‖S‖² and ∫|D̂S|² = k²∫S², and ∫Δ̂φ = 0 for every function φ on S³.

*The splitting.* The isometries SO(4) of the round S³ act on the static slice by isometries fixing N_s, so the constraint
maps are SO(4)-equivariant and 𝔈_V and 𝔈_K are invariant quadratic forms. Under SO(4) ≅ (SU(2) × SU(2))/{±1} the scalar
harmonics of degree l span the irreducible representation of highest weights (l/2, l/2), and the transverse trace-free
tensor harmonics of degree l the sum of those of highest weights ((l ± 2)/2, (l ∓ 2)/2) ([[sec:iii-f1-1]]); for different
types or degrees these representations are pairwise inequivalent. A scalar mode of degree l is the image of the scalar
harmonics of degree l under the equivariant linear map u ↦ a u dR² + 2R b du dR + R²(c uγ̂ + e(D̂D̂u + (k²/3)γ̂u)), and
likewise for k, so it lies in the isotypic component of (l/2, l/2); a tensor mode of degree l lies in that of
((l ± 2)/2, (l ∓ 2)/2), and the l = 0 part in that of the trivial representation. An invariant bilinear form pairs
isotypic components of inequivalent representations to zero, and an equivariant linear map takes each isotypic component
into the isotypic component of the same representation (Schur's lemma). So the polarisations of 𝔈_V and 𝔈_K vanish
between different modes, and the constraints of a seed hold exactly when those of each mode hold. The mode expansions of
smooth data converge with all their derivatives, so 𝔈_V and 𝔈_K of a seed are the sums of those of its modes.

*(a) The gauges.* The vector field X has X^R = α̃S and X^ϑ = β̃∂_ϑS, so X_R = α̃S/f and X_A = R²β̃∂_AS. Then (L_Xγ)_RR =
(α̃(1/f)′ + 2α̃′/f)S, (L_Xγ)_RA = (α̃/f + R²β̃′)∂_AS and (L_Xγ)_AB = 2Rα̃Sγ̂_AB + 2R²β̃D̂_AD̂_BS = R²((2α̃/R −
(2k²/3)β̃)Sγ̂ + 2β̃Ŝ)_AB, which are the stated shifts. The shifts are linear in (α̃, β̃), and b = e = 0 is reached by
exactly one (α̃, β̃), the stated one; A and F are the a and c/2 of the representative so reached. Adding to the data the
shifts of another vector field X′ of this form changes the (α̃, β̃) that reaches b = e = 0 by −X′ and leaves that
representative unchanged, so A and F are gauge invariant. For ψ_g = ψ(R)S, the spherical part of D²ψ_g is ψD̂D̂S +
Rfψ′Sγ̂, since Γ^R_AB = −Rfγ̂_AB, and Ric(γ) is round; so the trace-free spherical part of k_ψ = D²ψ_g − ψ_g Ric(γ) is
ψ(D̂D̂S + (k²/3)γ̂S) = ψŜ, which shifts z by ψ/R². The gauge functions α̃, β̃ and ψ are built pointwise from the data and
their R-derivatives, so they have compact support with the data.

*(b) The momentum constraint.* For z = 0, k_RR = pS, k_RA = Rq_k ∂_AS and k_AB = R²wSγ̂_AB, and tr k = (fp + 3w)S. With
the Christoffel symbols above, (div k)_R = (fp′ + f′p + (3fp − 3w − k²q_k)/R)S and (div k)_A = (Rf q_k′ + (4 − 3ς)q_k +
w)∂_AS, and ℳ = div k − d tr k gives [[eq:loc-mom-modes]]. Expanding, with Rf′ = 2ς,

    Z′ + (R²H_KI/3) q_k + R² 𝔪_ϑ + (R³/3) 𝔪_R = 0                                                    {#eq:loc-z-identity}

identically. If 𝔪_R = 𝔪_ϑ = 0, then [[eq:loc-z-identity]] gives q_k = −3Z′/(R²H_KI) (H_KI ≥ m > 0), w = Z/R³ + fq_k by
the definition of Z, and p from 𝔪_ϑ = 0 (f > 0): the data are the image of their Z. Conversely, for the image of a Z,
𝔪_ϑ = 0 by the definition of p, and then 𝔪_R = 0 by [[eq:loc-z-identity]]. Since |k|² = (f²p² + 3w²)S² + 2fq_k²|D̂S|²
and (tr k)² = (fp + 3w)²S², 𝔈_K = (2π)²‖S‖² ∫ 𝔢_K dR with 𝔢_K := R³(2k²fq_k² − 6w² − 6fpw). On 𝔪_ϑ = 0, inserting fp
from 𝔪_ϑ = 0 and then w = Z/R³ + fq_k, and using (R⁴f²)′ = 4R³f and (Rf)′ = 1 + ς, an expansion gives

    𝔢_K = 6Z²/R³ + (12ς − 6) Z q_k + 2R³fH_KI q_k² + 6RfZ′q_k + (−3R⁴f²q_k² − 6RfZq_k)′.

On 𝔪_R = 0 as well, [[eq:loc-z-identity]] gives 6RfZ′q_k = −2R³fH_KI q_k², and q_k = −3Z′/(R²H_KI) gives (12ς − 6)Zq_k =
−9(2ς − 1)(Z²)′/(R²H_KI). Since ((2ς − 1)/(R²H_KI))′ = 2(m − 4mς − 12ς²)/(R³H_KI²) and 6H_KI² + 18(m − 4mς − 12ς²) =
6m(m + 3) = 6k²m,

    𝔢_K = 6k²m Z²/(R³H_KI²) + 𝔅_K′,        𝔅_K := −3R⁴f²q_k² − 6RfZq_k − 9(2ς − 1)Z²/(R²H_KI).

𝔅_K has compact support, which gives [[eq:loc-ek]].

*(c) The Hamiltonian constraint.* Let α and β be smooth functions of R and the angles, and γ_ε := f⁻¹e^(2α)dR² +
R²e^(2β)γ̂. Then, with ζ := α − β,

    R²e^(2β) Scal(γ_ε) = 6 − 2Δ̂ζ − 2|D̂ζ|² − 6Δ̂β − 6D̂α·D̂β − 6√f e^(−α) ∂_R(R√f e^(2β−α)(1 + R∂_Rβ)).
                                                                                                    {#eq:loc-scal-exact}

Indeed, γ_ε = Λ²ĝ with Λ := Re^β and ĝ := ã²dR² + γ̂, ã := e^(α−β)/(R√f). The spheres {R = const} carry the metric γ̂ in
ĝ for every R, so their second fundamental form vanishes, and the Gauss and Riccati equations of the proof of
[[lem:constraints-evolution]] (a), with lapse ã and second fundamental form 0, give Scal(ĝ) = 6 − 2ã⁻¹Δ̂ã. Tracing the
formula for Ric[h] − Ric[g] in the proof of [[lem:conformal]] with m = 4, g = ĝ and h = Λ²ĝ (so that ψ = ln Λ and □ =
Δ_ĝ there) gives Scal(Λ²ĝ) = Λ⁻²(Scal(ĝ) − 6Δ_ĝ ln Λ − 6|d ln Λ|²_ĝ) = Λ⁻²(Scal(ĝ) − 6Λ⁻¹Δ_ĝΛ), since
Δ_ĝ ln Λ + |d ln Λ|²_ĝ = Λ⁻¹Δ_ĝΛ; and Δ_ĝΛ = ã⁻¹∂_R(ã⁻¹∂_RΛ) + ã⁻¹D̂·(ãD̂Λ), the volume form of ĝ being
ã dR dvol_γ̂. Inserting ã⁻¹Δ̂ã = Δ̂ζ + |D̂ζ|², Λ⁻¹ã⁻¹∂_R(ã⁻¹∂_RΛ) = √f e^(−α)∂_R(R√f e^(2β−α)(1 + R∂_Rβ)) and
Λ⁻¹ã⁻¹D̂·(ãD̂Λ) = Δ̂β + D̂α·D̂β gives [[eq:loc-scal-exact]].

For b = e = 0, γ + εh = f⁻¹(1 + εfAS)dR² + R²(1 + 2εFS)γ̂, so α = εα_1 + ε²α_2 + O(ε³) and β = εβ_1 + ε²β_2 + O(ε³) with
α_1 = fAS/2, α_2 = −f²A²S²/4, β_1 = FS and β_2 = −F²S². Write 𝔜 := R√f e^(2β−α)(1 + R∂_Rβ) = 𝔜_0 + εy_1S + ε²y_2S² +
O(ε³) and 𝔛 := R²e^(2β)Scal(γ + εh) = ε𝔛_1 + ε²𝔛_2 + O(ε³). Then 𝔜_0 = R√f and 𝔜_0′ = (f + Rf′/2)/√f = 1/√f, so that the
term of order ε⁰ of 𝔛 is 6 − 6 = 0;

    y_1 = R√f (2F − fA/2 + RF′),        y_2 = R√f (3f²A²/8 − fAF − RfAF′/2);

and, from [[eq:loc-scal-exact]] with e^(−α) = 1 − α + α²/2 + O(α³),

    𝔛_1 = −2Δ̂(α_1 − β_1) − 6Δ̂β_1 + 6α_1 − 6√f y_1′S,
    𝔛_2 = −2Δ̂(α_2 − β_2) − 2|D̂(α_1 − β_1)|² − 6Δ̂β_2 − 6D̂α_1·D̂β_1 − 6√f (y_2′S² − α_1y_1′S) − 6(α_1²/2 − α_2).

With Δ̂S = −k²S, 𝔛_1 = ((k² + 3)fA + 4k²F − 6√f y_1′)S. Since DScal[h] = R⁻²𝔛_1 and 6√f y_1′ = 6Z_1 + 6RfZ_1′ with
Z_1 := 2F − fA/2 + RF′, this is [[eq:loc-c]]. Next, D²Scal[h, h] is twice the ε² coefficient of Scal(γ + εh), R³Scal =
Re^(−2β)𝔛, and N_s dvol = R³ dR dvol_γ̂; so 𝔈_V(h) = −∫∫ R(𝔛_2 − 2β_1𝔛_1) dvol_γ̂ dR. Integrating over S³, the Laplacian
terms of 𝔛_2 drop out, ∫|D̂(α_1 − β_1)|² = k²(fA/2 − F)²∫S², ∫D̂α_1·D̂β_1 = (k²fAF/2)∫S², α_1²/2 − α_2 = 3f²A²S²/8, and
∫β_1𝔛_1 = R²F C(A, F)∫S²; so 𝔈_V(h) = (2π)²‖S‖² ∫ E_V(A, F) dR with

    E_V(A, F) = R(2k²(fA/2 − F)² + 3k²fAF + 6√f (y_2′ − (fA/2) y_1′) + (9/4)f²A²) + 2R³F C(A, F),

and expanding the derivatives of y_1 and y_2 gives [[eq:loc-ev-af]].

Five identities, each checked by expanding both sides with Rf′ = 2ς, ς′ = −2ς/R, k² = m + 3 and H_KI = m + 6ς, reduce
𝔈_V on the constraint. First,

    E_V(A, F) = E_red + R⁴F′C(A, F) + 𝔅_1′,
    E_red := (k²/2)Rf²A² + 3k²RfAF − R²f(k² + 12f)AF′ + (14k² − 24)RF² + 24R³fF′²,
    𝔅_1 := 3R²f³A² − 6R³f²AF′ + (12μ − 2k²R²)F² − 12R³fFF′ + 3R⁴fF′².                                   {#eq:loc-ev-red}

Second, [[eq:loc-moncrief]]; it gives the statement about the map ℓ ↦ (A, F): for (A, F) with C = 0 and compact support,
F = 9Rf³(ℓ′ + κ_Mℓ)/(2k²H_KI) by [[eq:loc-moncrief]] and A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F by the definition of ℓ;
conversely, for (A, F) built from a given ℓ, the variable ℓ of (A, F) is the given one, and [[eq:loc-moncrief]] gives
C(A, F) = 0. Third, substituting A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F into E_red, the terms in F′² cancel (24R³f − 2R³(k² +
12f) + 2k²R³ = 0), and

    E_red = (k²/2)Rf²ℓ² + c_1ℓF + c_2ℓF′ + c_3F² + c_4FF′,
    c_1 := −(k²R/3)(2m − 9 + 21ς),        c_2 := R²f(m − 9 + 12ς),
    c_3 := (2R/(9f²))(m³ − 6m² + 36m + 81 + 21m²ς − 117mς − 324ς + 153mς² + 351ς²),
    c_4 := −(2R²/(3f))(m² − 18m − 27 + 27mς − 27ς + 72ς²).

Fourth, with c_2ℓF′ = (c_2ℓF)′ − c_2′ℓF − c_2ℓ′F and c_4FF′ = (½c_4F²)′ − ½c_4′F²,

    E_red = (k²/2)Rf²ℓ² + F(e_1ℓ − c_2ℓ′) + e_0F² + (c_2ℓF + ½c_4F²)′,
    e_1 := c_1 − c_2′ = −(R/3)(2m² + 3m − 81 + 21mς + 63ς + 72ς²),
    e_0 := c_3 − ½c_4′ = (2k²R/(9f²))(m² − 6m + 15mς − 54ς + 72ς²).

Fifth, on the constraint F = 𝔭(ℓ′ + κ_Mℓ) with 𝔭 := 9Rf³/(2k²H_KI), so that E_red = P_2ℓ′² + P_1ℓℓ′ + P_0ℓ² + (c_2ℓF +
½c_4F²)′ with

    P_2 := −𝔭c_2 + 𝔭²e_0 = 27mR³f⁵/(2k²H_KI²),
    P_1 := 𝔭e_1 − 𝔭κ_Mc_2 + 2𝔭²κ_Me_0 = −3R²f³(m³ − 3m² − 54m + 15m²ς + 45mς + 54mς² + 54ς²)/(2k²H_KI²),
    P_0 := (k²/2)Rf² + 𝔭κ_Me_1 + 𝔭²κ_M²e_0
        = −3Rf²(m³ − 12m² − 81m + 2m³ς + 24m²ς + 18mς + 24m²ς² + 126mς² + 54ς² + 72mς³ + 108ς³)/(2k²H_KI²).

With P_1ℓℓ′ = (½P_1ℓ²)′ − ½P_1′ℓ²,

    E_red = P_2ℓ′² + P̃_0ℓ² + 𝔅_2′,        𝔅_2 := c_2ℓF + ½c_4F² + ½P_1ℓ²,
    P̃_0 := P_0 − ½P_1′ = 27mRf³(m² + 3m − m²ς − 9mς − 54ς − 10mς² − 18ς² − 24ς³)/(2k²H_KI³).

Finally, ℓ = 𝔷Φ_M with 𝔷 := H_KI/(R^(3/2)f²), for which 𝔷′/𝔷 = −(3m + 5mς + 42ς + 6ς²)/(2RfH_KI), gives

    P_2ℓ′² + P̃_0ℓ² = P_2𝔷²Φ_M′² + (P_2𝔷′² + P̃_0𝔷² − (P_2𝔷𝔷′)′)Φ_M² + (P_2𝔷𝔷′Φ_M²)′,
    P_2𝔷² = 27mf/(2k²),        P_2𝔷𝔷′ = −27m(3m + 5mς + 42ς + 6ς²)/(4k²RH_KI),
    P_2𝔷′² + P̃_0𝔷² − (P_2𝔷𝔷′)′ = 27m Qp/(32k²R²H_KI²).

On the constraint R⁴F′C(A, F) = 0, and 𝔅_1, 𝔅_2 and P_2𝔷𝔷′Φ_M² have compact support; so the five identities give
[[eq:loc-ev]].

*(d) The l = 0 part.* For l = 0, S = 1, Ŝ = 0 and D̂S = 0, so h_(l=0) = a dR² + R²cγ̂ and k_(l=0) = p dR² + R²wγ̂ with
a, c, p, w functions of R. The derivation of [[eq:loc-c]] in (c) uses neither b nor e, so [[eq:loc-c]] holds with k² =
0, A := a and F := c/2. Put 𝔤 := F. By (a) with S = 1 and β̃ = 0, X := R𝔤∂_R gives L_Xγ = ((1/f)′R𝔤 + 2(R𝔤)′/f)dR² +
2R²𝔤γ̂, and DScal[L_Xγ] = X(Scal(γ)) = 0. So on the constraint A_r := a − (1/f)′R𝔤 − 2(R𝔤)′/f satisfies C(A_r, 0) = 0
with k² = 0, that is 6(1 + ς)fA_r + 3Rf²A_r′ = 0, whose solutions are the constant multiples of ς/f², since
(ln(ς/f²))′ = −2/R − 4ς/(Rf) = −2(1 + ς)/(Rf); these vanish nowhere unless the constant is 0. Compact support gives
A_r = 0, so h_(l=0) = L_(R𝔤∂_R)γ with 𝔤 compactly supported. By (b) with k² = 0 and q_k = 0, the momentum constraint of
the l = 0 part is fp = Rw′ + w. For ψ_g = ψ(R), k_ψ has spherical part R²w_ψγ̂ with w_ψ = fψ′/R − ςψ/R² =
(fN_s/R)(ψ/N_s)′, since N_s′/N_s = ς/(Rf); and k_ψ solves the momentum constraint (proof of
[[lem:loc-gauge-invariance]]), so its RR component is (Rw_ψ′ + w_ψ)/f. The ψ_g of (d) has (ψ_g/N_s)′ = Rw/(fN_s), so
w_ψ = w and k_(l=0) = k_ψ. Hence the l = 0 part is the first variation of the data along the generator ψ_g n + R𝔤∂_R, a
gauge seed. Its energies vanish: 𝔈_V(L_Xγ) = 𝔈_V(0) = 0 by [[lem:loc-gauge-invariance]], and 𝔈_K(k_(l=0)) = 2π² ∫
R³(−6w² − 6fpw) dR = −6π² ∫ (R⁴w²)′ dR = 0. ∎

The potential in [[eq:loc-ev]] is Kodama and Ishibashi's scalar potential: fQp/(16R²H_KI²) = V_S, with V_S/f the
function W_S of [[lem:rw-potentials]], whose variable ς is the ς := μ/R² above.

**Lemma {#lem:loc-positivity}** (Positivity.) For class modes, m ∈ {5, 21, 45, …}, and for every ς ∈ [0, 1], Qp > 0.

*Proof.* Class modes have l = 2j, so m = 4j(j + 1) − 3. At m = 5, Qp = 1296ς³ + 2976ς² − 1260ς + 3500, and the
quadratic 2976ς² − 1260ς + 3500 has discriminant 1260² − 4 · 2976 · 3500 = −40076400 < 0, so Qp > 0 for ς ≥ 0. For
m = 12 + t with t ≥ 0, every coefficient of Qp as a polynomial in (ς, t) is nonnegative (624m − 144 = 7344 + 624t,
36m(m − 12) = 36(12 + t)t) and Qp(0, 0) = 16 · 12³ + 60 · 12² > 0. ∎

**Theorem {#thm:loc-outside}** (Outside the apparent horizon.) Let U ⊂ {f > 0} be a band of Σ_τ0 on which the
background is vacuum. Then Q(δ) ≤ 0 for every seed δ on U, with equality exactly when δ is a gauge seed.

*Proof.* By [[lem:loc-transfer]], Q(δ) = Q_static of a compactly supported seed on a static slice, and δ is gauge
exactly when that seed is. There Q = −𝔈_V − 𝔈_K, unchanged by the compactly supported gauges of
[[lem:loc-scalar-reduction]] (a) ([[lem:loc-gauge-invariance]]), and the modes separate ([[lem:loc-scalar-reduction]]).
For a scalar mode, H_KI > 0, f > 0, 27m/(2k²) > 0 and 6k²m/(R³H_KI²) > 0, and Qp > 0 ([[lem:loc-positivity]]), so by
[[eq:loc-ek]] and [[eq:loc-ev]] 𝔈_K ≥ 0 with equality exactly when Z = 0, that is (q_k, w, p) = 0, and 𝔈_V ≥ 0 with
equality exactly when Φ_M = 0, that is ℓ = 0 and (A, F) = 0: the mode is gauge. A tensor mode on the static slice is
[[thm:loc-tensor]] with G = 1/f and Y_s = 0, where −Q = (2π)²|T|²∫(R³Π² + R³f(∂_RH)² + (k_T² + 2)RH²) dR > 0 unless H =
Π = 0. The l = 0 part is gauge and contributes 0 ([[lem:loc-scalar-reduction]] (d)). So Q ≤ 0, and Q = 0 exactly when
every mode is gauge, that is when δ is gauge. ∎

### The sign of the charge {#sec:loc-sign}

**Theorem {#thm:charge-sign}** (The sign of the charge of exactly localised data.) Let U be a band of Σ_τ0 on which the
background is vacuum, and consider invariant data on Σ_τ0 equal to the background's outside a compact subset of U and
of the form bg + εδ + O(ε²), δ a seed on U, ε > 0 small.

(a) *Momentum seeds.* If δ ≠ 0 has δγ = 0, then Q(δ) < 0 and no such vacuum data exist for ε small. With matter obeying
the dominant energy condition none exist if f ≥ 0 on U; if U meets {f < 0}, such data exist with outgoing radial null
dust.

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
for the scalar potential, Qp > 0 on ς ∈ [0, 1] holds for m = 5 and for every m ≥ 12 by the proof of
[[lem:loc-positivity]], which covers m = l(l + 2) − 3 for every l ≥ 2.

**Remark {#rem:loc-trapped-rays}** (Numerical observation.) On the same discretisation at 80 and 160 steps per unit,
every outgoing grid ray crossing Σ_τ0 between √μ3 = 0.9067 and R = 1.000 was untrapped at the crossing and ended
trapped after the ingoing shell, and every ray crossing from R = 1.005 outward ended untrapped; with the ingoing shell
removed no ray above √μ3 was trapped. So bands of Σ_τ0 on which f > 0 can lie where the outgoing rays end trapped;
[[thm:charge-sign]] is stated in terms of f. No proof uses this remark.

### The background below R_* {#sec:bg-below}

This section proves the properties of the background of the angle-localised families that the margins of the bent slice
and the sign of the charge use below R_*: the data on 𝒞_in and the mass μ3 of region III ([[prop:bg-nprime]]); that the
background's ψ_III lies in the tube of [[prop:margins-seed]] (b) around the explicit quintic ψ_s ([[prop:bg-seed]]); the
hyperbolicity margin κK^l_l on Σ_τ0 for 0.70 ≤ R ≤ R_* ([[prop:bg-slice]]); and that region III ends on Σ_τ0 at R_u2,
with Γ > 0 for 1.861 ≤ R ≤ R_u2, and no point of Σ_τ0 with R_u2 < R < R_* is vacuum ([[prop:bg-region-three-end]]). The
results are collected in [[thm:bg-margins]]. Below R_* the background reduces exactly to ordinary differential equations
along null rays ([[lem:bg-reduction]]). Their solutions are enclosed by explicit approximants with a posteriori bounds
([[prop:bg-nprime]], [[prop:bg-rays]]). The approximants and every row of the bounds are printed in [[sec:tab-bg]].

#### The data and the reduction {#sec:bg-data}

Put u1 := 5.7, u2 := 7.2 and τ0 := −0.68. With the bump β(w) = exp(1 − 1/(1 − w²)) for |w| < 1, β(w) = 0 otherwise,
and b(x; a, c) = β((2x − a − c)/(c − a)), both as in [[sec:table-bump]], put

    ℬ(u) := 1.7 b(u; 5.7, 7.2),        𝒜(v) := 3.6 b(v; 3, 4.5).                                       {#eq:bg-profiles}

The background is the spherically symmetric metric g0 = −2e^(2σ) du dv + R² dΩ₃² of [[sec:two-dust-background]] with
an outgoing null dust of profile ℬ(u) and an ingoing one of profile 𝒜(v), so that ([[ch:two-dusts]])

    R_uu − 2σ_u R_u = −ℬ/(3R²),     R_vv − 2σ_v R_v = −𝒜/(3R²),     R R_uv = −e^(2σ) − 2R_u R_v,       {#eq:bg-field}

with the characteristic data e^(2σ) = 1/2 on 𝒞_out = {u = 0} and on 𝒞_in = {v = 0}, and R = 5, R_u = −0.47, R_v = 1/2 at
the corner. The mass function is μ := R²(1 + 2e^(−2σ) R_u R_v), and f := 1 − μ/R² = −2e^(−2σ) R_u R_v. Let v̂(v) be
the ingoing coordinate with v̂(0) = 0 and ψ = 0 on 𝒞_out, where

    ψ := ln(−e^(2σ)/(R_u v̂′(v))),      g0 = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃²   where R_u ≠ 0,     {#eq:bg-chart}

the second identity following from du = (dR − R_v dv)/R_u. The slice Σ_τ0 is that of [[sec:loc-setting]],
{v̂ − R = τ0, 0.70 ≤ R ≤ b(τ0)}. Put

    F(R) := 2R + √(3/2) ln((R − √(3/2))/(R + √(3/2))),      F′(R) = 2/(1 − 3/(2R²)),  {#eq:bg-tangherlini}

the null function of Tangherlini's metric of mass 3/2, and for ρ > √(3/2)

    v̂(ρ) := F(ρ) − F(2.321),    f1(ρ) := 1 − 3/(2ρ²),    a(ρ) := f1(ρ)/2,    a′(ρ) = 3/(2ρ³).           {#eq:bg-label}

**Lemma {#lem:bg-identities}** (Identities.) A solution of [[eq:bg-field]] satisfies

    μ_u = −(2/3) ℬ e^(−2σ) R_v,    μ_v = −(2/3) 𝒜 e^(−2σ) R_u,    ψ_u = ℬ/(3R² R_u),
    (e^(−2σ) R_v)_v = −𝒜 e^(−2σ)/(3R²),    (e^(−2σ) R_u)_u = −ℬ e^(−2σ)/(3R²).

*Proof.* [[eq:bg-field]] are the two-null-dust equations of [[ch:two-dusts]], μ is the mass function
[[eq:two-dust-mass]] and ψ is that of [[eq:two-dust-chart]]; so these are [[lem:two-dust-identities]] (i), (iv) and
the identity for ψ_u in (v). ∎

**Lemma {#lem:bg-reduction}** (Reduction to rays.) Let ℛ := {v < 3}.

(a) *The data on 𝒞_in.* R(u) := R(u, 0) solves R″ = −ℬ/(3R²) with R(u1) = 2.321, R′(u1) = −0.47, and S(u) := R²R_v(u, 0)
solves S′ = −R/2 with S(u1) = 2.067575. The functions μ(u) := μ(u, 0) and ℓ_v(u) := 2R_v(u, 0) are

    μ = R² + 4R′S,     ℓ_v = 2S/R²,     μ′ = −(2/3) ℬ ℓ_v,     ℓ_v′ = −μ/R³.                              {#eq:bg-nprime}

(b) *Region I.* On {u ≤ u1} ∩ ℛ, μ = 3/2 and ψ = 0, so g0 is Tangherlini's metric of mass 3/2 in ingoing
coordinates; along the outgoing ray u = u1, v̂ = F(R) − F(2.321). The ingoing ray of label v̂ meets u = u1 at R = ρ,
where v̂ = v̂(ρ) in the notation [[eq:bg-label]]; we label rays by ρ.

(c) *The rays.* On ℛ, μ(u, v) = μ(u) and e^(−2σ)R_v(u, v) = ℓ_v(u), and R_u < 0. Where ℓ_v(u) > 0, along every
ingoing ray

    R_u = G(u, R),        G(u, X) := −(1 − μ(u)/X²)/(2ℓ_v(u)).                                              {#eq:bg-ray}

Write Ψ(u, ρ) for the solution of [[eq:bg-ray]] with Ψ(u1, ρ) = ρ, and J := ∂_ρΨ, K := ∂_ρ²Ψ, L := ∂_ρ³Ψ.

(d) *The packet.* At a point of ℛ with u1 ≤ u ≤ u2 and f > 0, on the ray ρ, in the chart [[eq:bg-chart]],

    q := e^ψ = 2aJ/f,    ψ_R = ℬ/(3R²G²),    f_R = 2μ/R³ − μ′/(R²G),    f_v̂ = μ′ J a/(R²G),
    ψ_v̂ = aK/J + a′ − 2μJa/(R³f) − (Ja/G) ℬ/(3R²G),                                                    {#eq:bg-inputs}

with R = Ψ(u, ρ), G = G(u, R), a = a(ρ), μ = μ(u), μ′ = μ′(u), ℬ = ℬ(u).

(e) *Region III.* On {u ≥ u2} ∩ ℛ, μ = μ3 := μ(u2) and ψ = ψ_III(v̂), where for the ray ρ, with Φ(ρ) := Ψ(u2, ρ)
and f3(X) := 1 − μ3/X²,

    ψ_III(v̂(ρ)) = ln Φ′(ρ) + ln f1(ρ) − ln f3(Φ(ρ)),  {#eq:bg-psi3-def}

provided f3(Φ(ρ)) > 0. There g0 = −e^(2ψ_III) f3 dv̂² + 2e^(ψ_III) dv̂ dR + R² dΩ₃².

(f) *The slice.* Every point of Σ_τ0 with R ≤ R_*, R_* as in [[lem:bg-rstar]], lies in ℛ, on the ray ρ with
v̂(ρ) − R = τ0 and 2.321 ≤ ρ ≤ R_*.

*Proof.* (a) On 𝒞_in, σ is constant, so [[eq:bg-field]] gives R″ = −ℬ/(3R²) and R R_uv = −1/2 − 2R′R_v; hence S′ =
2RR′R_v + R²R_uv = −R/2. Since ℬ = 0 on [0, u1], R = 5 − 0.47u there, so R(u1) = 2.321, and S(u1) = 25/2 − (1/2)∫_0^(u1)
(5 − 0.47u) du = 2.067575. With e^(−2σ) = 2, μ = R²(1 + 4R′R_v) = R² + 4R′S and ℓ_v = 2S/R². Then μ′ = −(2/3)ℬℓ_v by
[[lem:bg-identities]], and ℓ_v′ = 2R_uv = −(1 + 4R′R_v)/R = −μ/R³.

(b) On {u ≤ u1}, ℬ = 0, and on ℛ, 𝒜 = 0. By [[lem:bg-identities]] μ_u = μ_v = 0, so μ equals its corner value
25(1 − 0.94) = 3/2, and ψ_u = 0, so ψ = 0 as on 𝒞_out. In [[eq:bg-chart]] the outgoing null directions satisfy dv̂/dR =
2/f = F′(R); the ray u = u1 meets 𝒞_in at v̂ = 0, R = 5 − 0.47 u1 = 2.321.

(c) On ℛ, 𝒜 = 0, so [[lem:bg-identities]] gives μ_v = 0 and (e^(−2σ)R_v)_v = 0; hence μ and e^(−2σ)R_v take their
values on 𝒞_in. On 𝒞_out, R_u = (3/(2R²) − 1)/2 < 0 for v ≤ 3 (there μ = 3/2, R = 5 + v/2, e^(−2σ) = 2), and
(e^(−2σ)R_u)_u ≤ 0, so R_u < 0 on ℛ. Finally f = −2e^(−2σ)R_uR_v = −2ℓ_vR_u.

(d) On ℛ, e^(2σ) = R_v/ℓ_v and ℓ_vR_u = −f/2, so e^ψ = −R_v/(ℓ_vR_u v̂′) = (2/f) ∂_v̂R|_u, and ∂_v̂R|_u = J dρ/dv̂ = Ja.
The derivatives in the chart [[eq:bg-chart]] follow from ∂_R|_v̂ = G⁻¹∂_u and ∂_v̂|_R = ∂_v̂|_u − (Ja/G)∂_u: f_R =
2μ/R³ − μ′/(R²G), f_v̂ = μ′Ja/(R²G), ψ_R = ψ_u/G = ℬ/(3R²G²) by [[lem:bg-identities]], and ψ_v̂ = ∂_v̂ ln(2Ja/f)|_u −
(Ja/G)ψ_u, where ∂_v̂ J|_u = Ka, ∂_v̂ a = aa′ and ∂_v̂ f|_u = 2μJa/R³.

(e) On {u ≥ u2}, ℬ = 0, so μ_u = ψ_u = 0 ([[lem:bg-identities]]; R_u ≠ 0 by (c)): μ and ψ take their values on u =
u2. There (d) gives e^ψ = 2aΦ′/f3(Φ) = f1Φ′/f3(Φ).

(f) On Σ_τ0, v̂ = R + τ0 ≤ R_* − 0.68 < 2.7572, while v̂(3) = F(6.5) − F(5) > 3.1453 (on 𝒞_out before the shell R = 5 +
v/2 and dv̂/dR = F′(R)); v̂ is increasing in v, so the point lies in ℛ. Its ray meets u = u1 at the ρ with v̂(ρ) = v̂ ≤
R_* − 0.68, so ρ ≤ R_* by the definition of R_*; and v̂ = R + τ0 ≥ 0.02 > 0 = v̂(2.321) gives ρ ≥ 2.321. ∎

**Lemma {#lem:bg-rstar}** (The radius R_*.) Let R_* be the radius at which the ray u = u1 meets Σ_τ0, that is the
zero of τ(R) := F(R) − F(2.321) − R + 0.68 on R > 2.321. Then R_* is unique and 3.43718006 ≤ R_* ≤ 3.43718007.

*Proof.* τ′(R) = 2/f1(R) − 1 > 0, τ(3.43718006) ≤ −8.4 × 10⁻⁹ and τ(3.43718007) ≥ 4.4 × 10⁻⁹, by direct evaluation of
[[eq:bg-tangherlini]] at these two decimals. ∎

**Lemma {#lem:bg-slice-forms}** (The margin on Σ_τ0.) At a point of Σ_τ0 in ℛ, in the chart [[eq:bg-chart]] with q :=
e^ψ > 0 and qf < 2 (f of either sign), the radial extrinsic curvature κ and the sphere trace K^l_l of
[[lem:racz-split-formulas]] satisfy

    κ K^l_l = 3 N_κ (1 − qf)/(q R (2 − qf)²),
    N_κ := q²f²ψ_R + q²f f_R/2 − 3qfψ_R − qf_v̂/2 − 3qf_R/2 − ψ_v̂ + ψ_R,                                 {#eq:bg-kk}

and κ > 0, K^l_l < 0 exactly when N_κ < 0 and qf < 1. In the packet (u1 ≤ u ≤ u2, f > 0, inputs [[eq:bg-inputs]]),

    N_κ = −(μq/R³)(2 − qf) − aK/J − a′ + ℬ ℓ_v² (2 − qf)²/(3R²f²),        q f = 2aJ,  {#eq:bg-nk-packet}

and in region III, N_κ = (μ3q/R³)(qf − 3) − ψ_III′(v̂).

*Proof.* Since q > 0 and qf < 2, 2/q − f = (2 − qf)/q > 0. By [[lem:racz-split-formulas]],
κ = −N_κ/(q√(2/q − f)(2 − qf)) and K^l_l = 3(qf − 1)/(qR√(2/q − f)), and q²(2/q − f) = q(2 − qf); this gives the
product, and since q, R, √(2/q − f) and 2 − qf are positive, κ > 0 exactly when N_κ < 0 and K^l_l < 0 exactly when
qf < 1. In the packet substitute [[eq:bg-inputs]] with qf = 2aJ and μ′ = −(2/3)ℬℓ_v: the terms without ℬ give
(μq/R³)(qf − 3) − (aK/J + a′ − μq/R³), using 2μJa/(R³f) = μq/R³; the terms in ℬ are ℬ times
(4ℓ_v²/(3R²f²))[(qf)² − (5/2)qf + 1 − qf((3/4)qf − 3/2)] = ℬℓ_v²(2 − qf)²/(3R²f²). In region III, ψ_R = f_v̂ = 0 and
f_R = 2μ3/R³. ∎

#### Elementary bounds {#sec:bg-tools}

**Lemma {#lem:bg-tools}** (Elementary bounds.)

(a) *Chebyshev sums.* If p(x, y) = Σ c_(ij) T_i(x)T_j(y) is a polynomial, T_i the Chebyshev polynomials, then on
[−1, 1]² it lies in [c_00 − 𝔰′, c_00 + 𝔰′], 𝔰′ := Σ_((i,j)≠(0,0)) |c_(ij)|; in particular |p| ≤ Σ |c_(ij)|. On a box
[a, b] × [c, d] the same holds for the coefficients in the variables x = (u − (a + b)/2)/((b − a)/2), y likewise; a
polynomial written in powers of x has Chebyshev coefficients given by x^n = 2^(1−n) Σ′_(k ≤ n/2) C(n, k) T_(n−2k)(x),
the prime halving the term T_0.

(b) *Cauchy.* If g is holomorphic on a neighbourhood of {|z − c| ≤ r}, |g| ≤ 𝔐 there, and g_n are its Taylor
coefficients at c, then for real x with |x − c| ≤ h < r and every integer k ≥ 0, |g(x)| ≤ Σ_(n<k) |g_n|hⁿ +
𝔐(h/r)^k/(1 − h/r).

(c) *Taylor.* If k ≥ 0 is an integer and g ∈ C^(k+1)[c − h, c + h], then for |x − c| ≤ h, |g(x)| ≤
Σ_(n≤k) |g^(n)(c)|hⁿ/n! + h^(k+1) sup |g^(k+1)|/(k + 1)!.

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

*Proof.* (a) |T_i| ≤ 1 on [−1, 1], and with x = cos t, xⁿ is the binomial expansion of ((e^(it) + e^(−it))/2)ⁿ. (b)
Cauchy's estimate |g_n| ≤ 𝔐/rⁿ bounds the terms n ≥ k. (c) Taylor's formula with Lagrange's remainder. (d) is
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

(b) If e is absolutely continuous on [a, b] and e′ = −p e + r with p ≥ 0 continuous and r integrable, then |e(u)|
≤ |e(a)| + ∫_a^u |r|.

*Proof.* (a) By Taylor's formula, m(t) := |e(a)| + |e′(a)| t + ∫_0^t (t − s)(Λ|e(a + s)| + δ) ds satisfies |e(a + t)| ≤
m(t), m″ = Λ|e| + δ ≤ Λm + δ, m(0) ≤ E₀, m′(0) ≤ E₁. The right side of the first line of [[eq:bg-comparison-2]], call it
𝓔(t), solves 𝓔″ = Λ𝓔 + δ with 𝓔(0) = E₀, 𝓔′(0) = E₁. Then z := 𝓔 − m has z″ − Λz = 𝓆 ≥ 0 and z(0), z′(0) ≥ 0, so z(t) =
z(0) cosh kt + z′(0)(sinh kt)/k + ∫_0^t (sinh k(t − s)/k) 𝓆(s) ds ≥ 0. Then |e′(a + t)| ≤ E₁ + ∫_0^t (Λ𝓔 + δ) = 𝓔′(t).
(b) e(u) = e^(−P(u)) e(a) + ∫_a^u e^(P(s)−P(u)) r(s) ds with P(u) := ∫_a^u p, and P is nondecreasing. ∎

#### The data on 𝒞_in {#sec:bg-nprime}

The approximant R̂ is the piecewise polynomial of [[sec:tab-bg-nprime]] on twelve segments of [u1, u2]: affine on
[5.7, 5.73] (the data line) and on [7.17, 7.2], and a polynomial of degree 12 to 17 on each of the ten middle segments,
which are graded towards the ends of the packet. Put

    Ŝ(u) := 2.067575 − (1/2)∫_(u1)^u R̂,     μ̃ := R̂² + 4R̂′Ŝ,     ℓ̃_v := 2Ŝ/R̂²,  {#eq:bg-nprime-approx}

so that Ŝ and μ̃ are polynomials and ℓ̃_v is a rational function on each segment, and μ̃3 := R̂(u2)² + 4R̂′(u2)Ŝ(u2) =
0.82211255682735… (an explicit rational).

**Proposition {#prop:bg-nprime}** (The data on 𝒞_in.) On each segment [a, b] of [[sec:tab-bg-nprime-chain]], |R − R̂| ≤
E₀ and |R′ − R̂′| ≤ E₁ with E₀, E₁ of that row, and |S − Ŝ| ≤ I/2. In particular |R − R̂| ≤ 4.53 × 10⁻⁸, |R′ − R̂′| ≤
9.20 × 10⁻⁸ and |S − Ŝ| ≤ 1.82 × 10⁻⁸ on [u1, u2], and

(i) R(u2) ∈ [1.5193579, 1.5193581] ⊂ [1.519357, 1.519359];

(ii) |μ3 − μ̃3| ≤ 4.07 × 10⁻⁷, so μ3 ∈ [0.82211214, 0.82211297] ⊂ [0.8220998, 0.8221253], and R(u2)² > μ3;

(iii) μ is nonincreasing, 3/2 ≥ μ ≥ μ3, and ℓ_v is decreasing with ℓ_v ≥ ℓ_v(u2) ≥ 0.529533 > 0.529 on [u1, u2];

(iv) at every u ∈ [u1, u2], with E₀, E₁, I of a segment containing u and R̂, R̂′, Ŝ at u,

    |μ − μ̃| ≤ (2R̂ + E₀)E₀ + 4(|R̂′| I/2 + ŜE₁ + E₁I/2),      |ℓ_v − ℓ̃_v| ≤ (I + 2Ŝ(2R̂ + E₀)E₀/R̂²)/(R̂ − E₀)²;

in particular |μ − μ̃| ≤ 4.2 × 10⁻⁷ and |ℓ_v − ℓ̃_v| ≤ 5 × 10⁻⁸ on [u1, u2].

*Proof.* Let δ(u) := R̂″ + ℬ/(3R̂²) on a segment. On the ten middle segments δ is holomorphic on the disc |u − c| ≤ r,
r = (4/5)min(c − u1, u2 − c), since ℬ is holomorphic off u1 and u2 ([[lem:bg-tools]] (e)) and |R̂| > 0 there; on the
disc, |R̂″| ≤ Σ n(n − 1)|q_n|(r/h)^(n−2)/h², |R̂| ≥ q_0 − Σ_(n≥1)|q_n|(r/h)ⁿ and |ℬ| is bounded by [[eq:bg-bump-disc]]
with w0 = (c − 6.45)/0.75, ϱ = r/0.75. This gives 𝔐. The Taylor coefficients δ_n of δ at c follow from those of ℬ
([[lem:bg-tools]] (e)) by multiplication and division of power series, and [[lem:bg-tools]] (b) with k = 60 gives the
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

(iv) At u, μ − μ̃ = (R² − R̂²) + 4(R̂′(S − Ŝ) + (R′ − R̂′)Ŝ + (R′ − R̂′)(S − Ŝ)) and ℓ_v − ℓ̃_v = 2(S − Ŝ)/R² + 2Ŝ(R̂² −
R²)/(R²R̂²), where |R² − R̂²| = |e|(R + R̂) ≤ (2R̂ + E₀)E₀, |S − Ŝ| ≤ I/2, Ŝ > 0 and R ≥ R̂ − E₀ > 0; this gives the two
bounds. On each segment they are at most 4.17 × 10⁻⁷ and 4.89 × 10⁻⁸ when R̂ is replaced by R̂_max in the numerators
and by R̂_min in the denominators, |R̂′| by R̂′_max of [[sec:tab-bg-ray-chain]] and Ŝ by its value at the left end;
both largest values occur on [7.17, 7.2].

(i) R̂(u2) = 1.5193579823987569 exactly. (ii) The bound (iv) at u = u2, with the exact values R̂(u2), R̂′(u2) =
−0.60795759341336… and Ŝ(u2) and the last row's E₀, E₁, I, gives |μ3 − μ̃3| ≤ 4.068 × 10⁻⁷; and R(u2)² ≥ 2.308 > 0.823.

(iii) Since Ŝ ≥ Ŝ(u2) and |S − Ŝ| ≤ 1.82 × 10⁻⁸, S ≥ Ŝ(u2) − 1.82 × 10⁻⁸ > 0.6111 on [u1, u2], so ℓ_v = 2S/R² > 0 there.
Since ℬ ≥ 0, [[eq:bg-nprime]] gives μ′ = −(2/3)ℬℓ_v ≤ 0, so μ is nonincreasing and 3/2 = μ(u1) ≥ μ ≥ μ3 > 0 by (ii),
where μ(u1) = 2.321² − 4(0.47)(2.067575) = 3/2. Hence ℓ_v′ = −μ/R³ < 0, so ℓ_v is decreasing on [u1, u2] and ℓ_v ≥
ℓ_v(u2) = 2S(u2)/R(u2)² ≥ 2(Ŝ(u2) − I/2)/(R̂(u2) + E₀)² ≥ 0.529533. ∎

#### The rays {#sec:bg-rays}

The ray approximant Ψ̃ is the polynomial of [[sec:tab-bg-ray]] on [u1, u2] × [2.32, 3.44], of degree 24 in u and 12 in
ρ; put J̃ := ∂_ρΨ̃, K̃ := ∂_ρ²Ψ̃, L̃ := ∂_ρ³Ψ̃. On each segment of R̂ let

    G̃(u, X) := R̂²(μ̃ − X²)/(4ŜX²),     D := ∂_uΨ̃ − G̃(u, Ψ̃),     D_m := ∂_ρ^m D  (m ≤ 3),  {#eq:bg-ray-approx}

so that G̃ is [[eq:bg-ray]] with μ, ℓ_v replaced by μ̃, ℓ̃_v, and D_1, D_2, D_3 are the defects of J̃, K̃, L̃ in the
variational equations of [[eq:bg-ray]] (for G̃). The polynomial

    P := 4ŜΨ̃² ∂_uΨ̃ − R̂²(μ̃ − Ψ̃²) = 4ŜΨ̃² D  {#eq:bg-ray-numerator}

has Chebyshev sums 𝔰_m of ∂_ρ^m P on each box [a, b] × [2.32, 3.44]. Since Ŝ does not depend on ρ, D = (P/(4Ŝ)) Ψ̃^(−2)
and Leibniz's rule give

    |D_m| ≤ Σ_(j≤m) C(m, j) (𝔰_(m−j)/(4Ŝ_min)) g_j,    g_0 = Ψ̃_min^(−2),  g_1 = 2J̄Ψ̃_min^(−3),
    g_2 = 6J̄²Ψ̃_min^(−4) + 2K̄Ψ̃_min^(−3),
    g_3 = 24J̄³Ψ̃_min^(−5) + 18J̄K̄Ψ̃_min^(−4) + 2L̄Ψ̃_min^(−3),  {#eq:bg-ray-defects}

J̄, K̄, L̄ the bounds of |J̃|, |K̃|, |L̃| on the box ([[sec:tab-bg-ray-defects]]).

The fields G and G̃ differ through the data. Write G = 𝒬/(2X²) − V/2 with 𝒬 := μ/ℓ_v = R⁴/(2S) + 2R′R² and V := 1/ℓ_v =
R²/(2S), and 𝒬̃, Ṽ likewise from R̂, Ŝ. On a segment, with R̄ := R̂_max + E₀, R̄′ := R̂′_max + E₁ (R̂′_max ≥ |R̂′|
is the bound of [[sec:tab-bg-ray-chain]]), S̲ := Ŝ_min − I/2 and X̲ := Ψ̃_min − 10⁻⁵, the mean value theorem in (R,
R′, S) gives |𝒬 − 𝒬̃| ≤ Δ₁, |V − Ṽ| ≤ Δ₂ with

    Δ₁ := (2R̄³/S̲ + 4R̄′R̄) E₀ + 2R̄² E₁ + (R̄⁴/(2S̲²)) I/2,      Δ₂ := (R̄/S̲) E₀ + (R̄²/(2S̲²)) I/2,
    γ_0 := Δ₁/(2X̲²) + Δ₂/2,   γ_1 := Δ₁/X̲³,   γ_2 := 3Δ₁/X̲⁴,   γ_3 := 12Δ₁/X̲⁵,  {#eq:bg-gamma}

and |∂_X^m(G − G̃)| ≤ γ_m (m ≤ 3) on the tube

    {(u, X): |X − Ψ̃(u, ρ)| ≤ 10⁻⁵ for some ρ ∈ [2.32, 3.44]},                                             {#eq:bg-tube}

where also |∂_X^m G| ≤ H_m := c_m (3/2)/(0.529533 X̲^(m+2)), (c_2, c_3, c_4) = (3, 12, 60), by
[[prop:bg-nprime]] (iii) and ∂_X^m G = (−1)^m (m + 1)! μ/(2ℓ_vX^(m+2)) for m ≥ 1.

**Proposition {#prop:bg-rays}** (The rays.) For u ∈ [a, b], a segment of [[sec:tab-bg-ray-chain]], and ρ ∈ [2.32, 3.44],

    |Ψ − Ψ̃| ≤ ε₀,   |J − J̃| ≤ ε₁,   |K − K̃| ≤ ε₂,   |L − L̃| ≤ ε₃,

with the ε of that row. At u = u2: ε₀ = 8.69 × 10⁻⁷, ε₁ = 1.68 × 10⁻⁶, ε₂ = 6.10 × 10⁻⁶, ε₃ = 3.65 × 10⁻⁵. Moreover 0
< J ≤ 1, and the rays satisfy Ψ(u, ρ) > √μ(u) on [u1, u2] × [2.32, 3.44].

*Proof.* Fix ρ. By [[prop:bg-nprime]] (iii), ℓ_v > 0 on [u1, u2], so [[eq:bg-ray]] holds along the ray, and ∂_XG =
−μ/(ℓ_vX³) < 0 for X > 0. Let e₀ := Ψ − Ψ̃. Then e₀′ = −p e₀ + r with p := −∫_0^1 ∂_XG(u, Ψ̃ + te₀) dt ≥ 0 and r := (G −
G̃)(u, Ψ̃) − D. While |e₀| ≤ 10⁻⁵, [[lem:bg-comparison]] (b) gives |e₀(u)| ≤ |e₀(a)| + (u − a)(γ_0 + D₀). For e₁ := J −
J̃, differentiating [[eq:bg-ray]] in ρ, e₁′ = ∂_XG(u, Ψ)e₁ + (∂_XG(u, Ψ) − ∂_XG(u, Ψ̃))J̃ + (∂_XG − ∂_XG̃)(u, Ψ̃)J̃ −
D_1, whose last three terms are at most H_2ε₀J̄ + γ_1J̄ + D₁; the same lemma applies with p = −∂_XG(u, Ψ) ≥ 0. For e₂ and
e₃ the variational equations K′ = ∂_XG K + ∂_X²G J² and L′ = ∂_XG L + 3∂_X²G JK + ∂_X³G J³ give in the same way

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

(a) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in the points with 0.70 ≤ R ≤ R_u2, where 1.8614098 ≤ R_u2 ≤ 1.8614596;
in particular the seed region 0.70 ≤ R ≤ 1.861 (0.02 ≤ v̂ ≤ 1.181) lies in region III, and f3(Φ(ρ)) > 0 for every
ρ ∈ [2.32, 3.44].

(b) For every v̂ ∈ [0.02, 1.181],

    |ψ_s(v̂) − ψ_III(v̂)| ≤ 3.03 × 10⁻⁵,  |ψ_s′(v̂) − ψ_III′(v̂)| ≤ 2.40 × 10⁻⁴,  |ψ_s″(v̂) − ψ_III″(v̂)| ≤ 8.56 × 10⁻⁴,

and |μ3 − μ_s| ≤ 1.79 × 10⁻⁶. In particular the bounds 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ (k = 0, 1, 2) and 1.4 ×
10⁻⁵ hold at every point of the seed region.

(c) Consequently (ψ_III, ψ_III′, ψ_III″) lies within (10⁻³, 10⁻³, 3 × 10⁻²) of (ψ_s, ψ_s′, ψ_s″) on the seed region
and |μ3 − μ_s| ≤ 10⁻⁴: the background lies in the tube of [[prop:margins-seed]] (b), and Γ > 0 on the seed region.

*Proof.* (a) On Σ_τ0, R = v̂ + 0.68 ≥ 0.70, and by [[lem:bg-reduction]] (f) a point of Σ_τ0 with R ≤ R_* lies
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

The function ẽ_k is bounded by [[lem:bg-tools]] (c), of order 5, at the midpoint ρ_m of each interval: |ẽ_k| ≤
Σ_(n≤5) |c_n| hⁿ + h⁶ sup |c_6(ξ)|, where c_n is the n-th Taylor coefficient of ẽ_k at ρ_m, c_6(ξ) :=
ẽ_k^(6)(ξ)/6! for ξ in the interval, and h is the half-width. These coefficients are obtained as follows. The
function ẽ_k is built from ρ by sums, products, quotients, logarithms and 𝒟: Φ̃ = Σ C_j T_j(y) with y = (ρ −
2.88)/0.56 and T_(j+1) = 2yT_j − T_(j−1); f1 = 1 − 3/(2ρ²), a = f1/2 and f3(Φ̃) = 1 − μ̃3/Φ̃²; Ψ_0 = ln Φ̃′ + ln
f1 − ln f3(Φ̃), Ψ_1 = a𝒟Ψ_0 and Ψ_2 = a𝒟Ψ_1 ([[eq:bg-psi3]]); v̂ = F(ρ) − F(2.321) with F of
[[eq:bg-tangherlini]]; and ψ_s^(k)(v̂), where the k-th derivative ψ_s^(k) of the quintic is a polynomial.
Starting from the Taylor series ρ_0 + t of ρ at a point ρ_0, the rules [[eq:bg-series]] give the Taylor
coefficients at ρ_0 of each of these functions in turn, up to order 9 (Φ̃ is a polynomial, so its series is
exact; Φ̃′ and each 𝒟 lower the order by one), and so those of ẽ_k up to order 6; every operation on numbers is
replaced by [[lem:bg-tools]] (d), with √(3/2) enclosed by it. With ρ_0 = ρ_m this encloses c_0, …, c_5. With ρ_0
replaced by each of twenty equal parts P of the interval, the same steps enclose, at every ξ ∈ P, the
coefficients at ξ, since each is the same finite combination of ξ; the sixth one encloses c_6(ξ). This gives the
column "Taylor" of [[sec:tab-bg-seed]] and the rest, at most 2 × 10⁻¹⁰ in every row, and the totals Taylor +
rest + Δ_k bound |e_k| on each interval. The largest totals are 3.020 × 10⁻⁵, 2.394 × 10⁻⁴ and 8.558 × 10⁻⁴, all on
the first interval. Finally |μ3 − μ_s| ≤ |μ̃3 − μ_s| + 4.07 × 10⁻⁷ ≤ 1.3809 × 10⁻⁶ + 4.07 × 10⁻⁷.

(c) The bounds of (b) are below (10⁻³, 10⁻³, 3 × 10⁻²) and 10⁻⁴; [[prop:margins-seed]] (b) states Γ > 0 for every
background of the tube. ∎

#### The slice below R_* {#sec:bg-slice}

**Proposition {#prop:bg-slice}** (Hyperbolicity below R_*.) At every point of Σ_τ0 with R ≤ R_*, κ > 0, K^l_l < 0,
e^ψ f < 1 and κK^l_l ≤ −6.00 × 10⁻³; in particular κK^l_l ≤ −4.76 × 10⁻³.

*Proof.* By [[lem:bg-reduction]] (f) the point lies on a ray ρ ∈ [2.321, R_*] with R = v̂(ρ) + 0.68 =: T(ρ). By
[[prop:bg-seed]] (a) it lies in region III if ρ ≤ ρ_u2 ≤ 2.77364, and otherwise in the packet u1 ≤ u ≤ u2.

*Region III.* On each interval of [[sec:tab-bg-slice-iii]], ψ_III and ψ_III′ are enclosed by [[eq:bg-psi3]] with Φ
in Φ̃ ± ε₀, Φ′ in Φ̃′ ± ε₁, Φ″ in Φ̃″ ± ε₂ ([[prop:bg-rays]]), and R by T on the interval. [[lem:bg-slice-forms]] and
[[lem:bg-tools]] (d) give qf < 1, N_κ < 0 and κK^l_l ≤ −0.093 on every row (q = e^(ψ_III) > 0, qf < 2).

*The packet.* For ρ ∈ [ρ_u2, R_*] the slice point is at the unique u_s(ρ) ∈ [u1, u2] with Ψ(u_s, ρ) = T(ρ): the
difference Ψ(u, ρ) − T(ρ) is ≥ 0 at u1 (ρ ≥ T(ρ) for ρ ≤ R_*, by [[lem:bg-rstar]]), ≤ 0 at u2 (g(ρ) ≤ 0), and decreasing
in u (∂_uΨ = G < 0 since f > 0, [[prop:bg-rays]]). It is also decreasing in ρ, since ∂_ρ(Ψ − T) = J − 1/a < 0; hence u_s
is decreasing in ρ, and so is the inverse ρ_s(u). For each row [u_a, u_b] of [[sec:tab-bg-slice-packet]], Ψ̃(u_a, ρ_hi) +
ε₀ < T(ρ_hi) and Ψ̃(u_b, ρ_lo) − ε₀ > T(ρ_lo) (by direct evaluation; at u_a = u1 take ρ_hi ≥ R_* from [[lem:bg-rstar]],
at u_b = u2 take ρ_lo ≤ ρ_u2 from [[prop:bg-seed]] (a)), so the slice points with u_s ∈ [u_a, u_b] have ρ ∈ [ρ_lo,
ρ_hi]. On the box [u_a, u_b] × [ρ_lo, ρ_hi]: μ and ℓ_v lie between their values at u_a and u_b (monotone,
[[prop:bg-nprime]] (iii)), which are μ̃, ℓ̃_v there up to the errors 4.2 × 10⁻⁷ and 5 × 10⁻⁸ of [[prop:bg-nprime]] (iv);
ℬ lies between its end values, or between the smaller one and 17/10 when 6.45 is inside, by [[lem:bg-tools]] (e); J and K
lie in the Chebyshev enclosures of J̃, K̃ on the box widened by ε₁, ε₂, with J ≤ 1; and R ∈ [T(ρ_lo), T(ρ_hi)]. Then
[[eq:bg-nk-packet]] and [[lem:bg-tools]] (d) give the enclosures of qf and N_κ in the second table: qf < 1 and N_κ < 0 on
every row, and the largest upper bound of κK^l_l is −6.00 × 10⁻³, on the row u ∈ [6.05, 6.1]. ∎

Near R = R_* the packet's slice points approach region I, where q = 1 and N_κ = (μ/R³)(f − 3) exactly, and κK^l_l =
3(3/2)R_*⁻³(f − 3)(1 − f)/(R_*(2 − f)²) = −6.86 × 10⁻³ at R_*, f = 1 − 3/(2R_*²); the first rows' bounds are close to it.

#### The end of region III {#sec:bg-region-three-end}

**Proposition {#prop:bg-region-three-end}** (The end of region III.) Let R_u2 be as in [[prop:bg-seed]] (a) and ρ_u2 the
zero of g(ρ) := Φ(ρ) − v̂(ρ) − 0.68 on [2.32, 3.44] found in its proof, so that R_u2 = v̂(ρ_u2) + 0.68 and region III
meets Σ_τ0 in the points with 0.70 ≤ R ≤ R_u2 (the points with R ≥ R_* lie in region I, [[lem:margins-region-one]] (c)).

(a) 2.773631 < ρ_u2 < 2.7736325 and 1.8614372 ≤ R_u2 ≤ 1.8614410.

(b) At every point of Σ_τ0 with 1.861 ≤ R ≤ R_u2, the quantity Γ/E² of [[eq:margins-gamma-form]] for the background (ψ =
ψ_III and μ = μ3) satisfies Γ/E² ≥ 10.40.

(c) Γ > 0 at every point of Σ_τ0 in region III: Γ/E² ≥ 0.048 on the seed region 0.70 ≤ R ≤ 1.861, and Γ/E² ≥ 10.40 for
1.861 ≤ R ≤ R_u2.

(d) No point of Σ_τ0 with R_u2 < R < R_* is a vacuum point of the background. So every band of Σ_τ0 on which the
background is vacuum lies in region III, {0.70 ≤ R ≤ R_u2}, or in {R ≥ R_*}.

*Proof.* (a) By the proof of [[prop:bg-seed]] (a), g is decreasing on [2.32, 3.44] with the single zero ρ_u2. By direct
evaluation of the polynomial Φ̃ of [[sec:tab-bg-ray]] and of [[eq:bg-tangherlini]], Φ̃(2.773631) − v̂(2.773631) − 0.68 ≥
1.3949 × 10⁻⁶ and Φ̃(2.7736325) − v̂(2.7736325) − 0.68 ≤ −1.1149 × 10⁻⁶. Since |Φ − Φ̃| ≤ ε₀ = 8.69 × 10⁻⁷ at u = u2
([[prop:bg-rays]]), g(2.773631) > 0 > g(2.7736325), so 2.773631 < ρ_u2 < 2.7736325. As v̂ is increasing, R_u2 lies
between v̂(2.773631) + 0.68 ≥ 1.86143720 and v̂(2.7736325) + 0.68 ≤ 1.86144094.

(b) Let P be a point of Σ_τ0 with 1.861 ≤ R ≤ R_u2. It lies in region III, on the ray ρ with v̂(ρ) + 0.68 = R
([[lem:bg-reduction]] (f), [[prop:bg-seed]] (a)), and there ψ_III^(k)(v̂(ρ)) = Ψ_k(ρ, Φ(ρ), …, Φ‴(ρ), μ3) for k ≤ 2
([[eq:bg-psi3]]). Since v̂ is increasing, v̂(2.7734) + 0.68 ≤ 1.8608633 < 1.861 and ρ ≤ ρ_u2 < 2.7737, the ray has ρ ∈
[2.7734, 2.7737]. Put ρ_m := 2.77355 and h := 1.5 × 10⁻⁴. For such ρ and j ≤ 3, |Φ̃^(j)(ρ) − Φ̃^(j)(ρ_m)| ≤ h
sup|Φ̃^(j+1)|, the supremum over [2.32, 3.44]. For j + 1 = 1, 2, 3 the supremum is at most 0.9442, 0.344 and 0.376, the
bounds of the absolute values of J̃, K̃ and L̃ in the row [7.17, 7.2] of [[sec:tab-bg-ray-defects]] (at u = 7.2, J̃, K̃
and L̃ are Φ̃′, Φ̃″ and Φ̃‴), and for j + 1 = 4 it is at most 0.3182, the sum of the absolute values of the Chebyshev
coefficients of Φ̃⁗ on [2.32, 3.44] ([[lem:bg-tools]] (a)). By direct evaluation, to within 10⁻¹⁰,

    Φ̃(ρ_m) = 1.8613729013,   Φ̃′(ρ_m) = 0.8111250646,   Φ̃″(ρ_m) = 0.2026504300,   Φ̃‴(ρ_m) = −0.2475621243,

and |Φ^(j) − Φ̃^(j)| ≤ ε_j, (ε₀, ε₁, ε₂, ε₃) = (8.69 × 10⁻⁷, 1.68 × 10⁻⁶, 6.10 × 10⁻⁶, 3.65 × 10⁻⁵) at u = u2
([[prop:bg-rays]]). This gives the first four rows of the table of [[sec:tab-bg-region-three-end]]. Each later row
follows from the rows above it, from ρ ∈ [2.7734, 2.7737], μ3 ∈ [0.82211214, 0.82211297] ([[prop:bg-nprime]] (ii)) and
R ∈ [1.861, 1.861441] (by (a)), by the enclosure rule of [[lem:bg-tools]] (d), applied to f1 = 1 − 3/(2ρ²), a = f1/2,
a′ = 3/(2ρ³), a″ = −9/(2ρ⁴), f3(Φ) = 1 − μ3/Φ², h3(Φ) := 1/(Φ³ − μ3Φ), h3′(Φ) = −(3Φ² − μ3)h3(Φ)²,

    ψ_III = ln Φ′ + ln f1 − ln f3(Φ),        ψ_III′ = aΦ″/Φ′ + a′ − 2μ3aΦ′h3(Φ),
    ψ_III″ = a(a′Φ″/Φ′ + a(Φ‴/Φ′ − (Φ″/Φ′)²) + a″ − 2μ3(a′Φ′h3(Φ) + aΦ″h3(Φ) + aΦ′²h3′(Φ)))

(the derivatives in v̂, Ψ_0, Ψ_1 and Ψ_2 = a𝒟Ψ_1 of [[eq:bg-psi3]] written out), q = e^(ψ_III), 𝔲 = 1 − q, m = μ3/R²,
W = q(1 − m), and n0, A0, A1, A2, A3 and Γ/E² = A0 + A1ψ_III′ + A2ψ_III′² + A3ψ_III″ in the form written in
[[eq:margins-gamma-form]]. Every entry is rounded outward, and later rows use the printed entries.

Since W < 1 and 2 − W > 0 on the box, [[eq:margins-gamma-form]] applies at P, and Γ/E² ≥ 10.4024.

(c) On the seed region Γ/E² ≥ 0.048 by [[prop:bg-seed]] (c) and [[prop:margins-seed]] (b); the rest is (b).

(d) By [[lem:bg-reduction]] (f), a point of Σ_τ0 with R ≤ R_* lies on a ray ρ ∈ [2.321, R_*] with R = T(ρ) := v̂(ρ) +
0.68, and T is increasing. By the proof of [[prop:bg-slice]], for ρ ∈ [ρ_u2, R_*] the point lies at the parameter u =
u_s(ρ) ∈ [u1, u2] of its ray, u_s is strictly decreasing (∂_u(Ψ − T) = G < 0 and ∂_ρ(Ψ − T) < 0), u_s(ρ_u2) = u2 since
g(ρ_u2) = 0, and u_s(R_*) = u1 by the definition of R_*. So a point with R_u2 < R < R_* has u1 < u < u2, where ℬ(u) > 0,
and there Ric(g0) ≠ 0 by [[eq:two-dust-limit]]. A band {R1 < R < R2} on which the background is vacuum therefore does not
meet {R_u2 < R < R_*}, and it lies in {0.70 ≤ R ≤ R_u2} or in {R ≥ R_*}. ∎

#### The theorem {#sec:bg-theorem}

**Theorem {#thm:bg-margins}** (The background below R_*.) For the background of [[sec:two-dust-background]]:

(a) On 𝒞_in, ℓ_v ≥ 0.529 on [u1, u2]; R(u2) ∈ [1.519357, 1.519359]; the mass of region III satisfies μ3 ∈ [0.8220998,
0.8221253] and R(u2)² > μ3.

(b) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in 0.70 ≤ R ≤ R_u2, where 1.8614372 ≤ R_u2 ≤ 1.8614410, and contains the
seed region. On the seed region, |ψ_s^(k) − ψ_III^(k)| ≤ 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ for k = 0, 1, 2, and |μ3 −
μ_s| ≤ 1.4 × 10⁻⁵; so the background lies in the tube of [[prop:margins-seed]] (b) and Γ > 0 on the seed region. At the
points of Σ_τ0 with 1.861 ≤ R ≤ R_u2, Γ/E² ≥ 10.40, so Γ > 0 at every point of Σ_τ0 in region III.

(c) On Σ_τ0 for R ≤ R_*: κ > 0, K^l_l < 0, e^ψ f < 1 and κK^l_l ≤ −4.76 × 10⁻³.

*Proof.* (a) is [[prop:bg-nprime]], (b) is [[prop:bg-seed]] and [[prop:bg-region-three-end]], (c) is
[[prop:bg-slice]]. ∎

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
ln(−e^(2σ)/(R_u dv̂/dv)). Then τ := v̂ − R, τ0 := −0.68, and Σ_τ0 = {τ = τ0, 0.70 ≤ R ≤ b(τ0)} is the slice of
[[sec:loc-setting]]. Region I is {u ≤ 5.7}. The proofs use four
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

with l1 h_L = 54/305. At R = 4.415, 4.43 and 4.445 (y_P = y_21, y_22, y_23) the table of [[sec:table-bump]] gives, with
K̃ := C̃_40 and rounded to ten decimals,

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

the right-hand bound being the maximum over Ṙ. At the points of γ other than q, μ ≥ 3/2 and 3.5 < R < 5.75, so
2 − f = 1 + μ/R² ≥ 1 + 1.5/5.75² ≥ 1.045368 and √(2 − f) ≥ 1.02243. Hence |Ω̇| ≤ τ̇/(3.5 × 1.02243) ≤ τ̇/3.5785, and the
angular displacement is at most (τ0 − τ(p))/3.5785 = −φ(R_p)/3.5785 ≤ 0.0011596/3.5785 ≤ 3.25 × 10⁻⁴.

*Σ_τ0 is acausal.* In the chart [[eq:bg-chart]], g = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃², so the induced metric of
Σ_τ0 = {v̂ = τ0 + R, 0.70 ≤ R ≤ b(τ0)} is e^ψ(2 − e^ψ f) dR² + R² dΩ₃². Here e^ψ f < 1 at every point of Σ_τ0: for R ≥
R_* the point lies in region I by [[lem:margins-region-one]] (c), where ψ = 0 and f = 1 − μ/R² < 1; for R ≤ R_*, e^ψ f <
1 by [[prop:bg-slice]]. Parametrise the quotient curve of Σ_τ0 by R. Along it v̂ = τ0 + R increases, so v increases
strictly, and −2e^(2σ)(du/dR)(dv/dR) = e^ψ(2 − e^ψ f) > 0, so u decreases strictly. Let a future causal curve run from p1
∈ Σ_τ0 to p2 ∈ Σ_τ0. Then v(p2) ≥ v(p1) and u(p2) ≥ u(p1), which give R(p2) ≥ R(p1) and R(p2) ≤ R(p1); so u and v take
the same values at both ends, and as they do not decrease along the curve they are constant on it. Its tangent then has
u̇ = v̇ = 0 and R²|Ω̇|² ≤ 2e^(2σ) u̇ v̇ = 0, so the curve is constant. Finally, a point p of Σ′ with R_p < R_* has
φ(R_p) = 0 and lies on Σ_τ0, so a causal curve joining it to a point q of Σ_τ0 is constant, and R_q = R_p < R_*. ∎

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

*Proof.* On 𝒞_out, e^(2σ) = 1/2. Then (S3) gives P′ = −𝒜/(3R²); the definition of μ gives μ = R²(1 + 4R_uP), so
R_u = −f_N/(4P); (S1) gives μ′ = −(4/3)𝒜R_u = 𝒜w; and dv̂/dv = −e^(2σ)/R_u = −1/(2R_u) = g. Before the shell 𝒜 = 0,
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

On Σ′ the slice is V(R) = τ0 + R + φ(R), so V′ = 1 + φ′ ∈ [0.99786, 1.00149] and V″ = φ″ by
[[prop:margins-bend]], and Ξ = φ″ + (μ/R³)V′²(3 − fV′) − μ̇V′³/(2R²). On Σ′ ∩ {R ≥ R_*}, which lies in region I
by [[lem:margins-region-one]] (c), μ ≥ 3/2, so f ≤ 1 − 3/(2R²); with V′ ≤ 1.00149, and V′ = 1 for R ≥ 5.75, this
gives fV′ < 1 on Σ′ ∩ {R ≥ R_*}, so K′^l_l < 0 there, and κ′ > 0 exactly where Ξ > 0.

#### Hyperbolicity on R ≥ R_* {#sec:margins-hyperbolic}

For 3 ≤ v ≤ 4.5, the ingoing ray v meets Σ_τ0 at R0(v) := v̂(v) − τ0 and Σ′ at the radius R′(v) with R′ + φ(R′) = R0(v);
both are increasing in v. Write N_κ(v) and Ξ(v) for N_κ and Ξ at these points, with μ = μ(v) and μ̇ = (3/2)𝒜 w² by
[[eq:margins-rates]].

**Lemma {#lem:margins-curvature}** (Second derivatives along the slices.) On a cell [v_k, v_(k+1)] let S_i be the
supremum of |𝒜^(i)| (i = 0, 1, 2) and Φ4 the supremum of |φ⁗| over [R′(v_k), R′(v_(k+1))]. Then on the cell

    (a)  |d²N_κ/dv²| ≤ 𝔐 := 0.024 S_2 + 0.059 S_1 + 0.072 S_0 + 0.0013 S_0² + 0.17,
    (b)  |d²Ξ/dv²| ≤ 𝔐′ := 1.21 Φ4 + 0.024 S_2 + 0.061 S_1 + 0.075 S_0 + 0.0013 S_0² + 0.23.

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

and the bounds above give |N_κ″| ≤ 0.02363 S_2 + 0.05848 S_1 + 0.07172 S_0 + 0.00125 S_0² + 0.1672 ≤ 𝔐.

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
3.8254920; by the next paragraph |R′(3) − R′_0| ≤ 5.3 × 10⁻⁶, so R′(3) < 3.82550. On [R_*, 3.5], φ = 0 and Ξ =
(1.5/R³)(2 + 1.5/R²) ≥ 0.074254, while c ≥ 3(1.5/3.5²)/(3.5 (1 + 1.5/R_*²)²) ≥ 0.082639, so κ′K′^l_l ≤ −6.1 × 10⁻³. On
[3.5, 3.82550], φ″ ≥ −0.01 l1 ≥ −0.0064382, V′ ∈ [0.99786, 1] (φ′ ≤ 0 there) and f ∈ [0.877551, 0.897504], so Ξ ≥
−0.0064382 + 0.026793 × 0.995724 × 2.102496 ≥ 0.049653 and c ≥ 0.307488/(3.8255 × 1.124327²) ≥ 0.063585, so κ′K′^l_l ≤
−3.1 × 10⁻³.

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
[[lem:margins-curvature]] (b), on the cell [v_k, v_(k+1)], Ξ ≥ L_k := min(Ξ_k, Ξ_(k+1)) − 5 × 10⁻⁶ − 𝔐′_k/51200, where
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
s)R0_k + sR0_(k+1), and N_κ(v) is within 5 × 10⁻⁶ + 𝔐_k/51200 of (1 − s)N_k + sN_(k+1). Hence:

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
on the cells around R = 4.66, where the bend's central lobe is on its falling side. For R ≤ R_*, where Σ′ = Σ_τ0, the
margin is that of [[thm:bg-margins]] (c).

#### Γ on the seed region {#sec:margins-seed}

On a vacuum region of the background, in the chart (v̂, R), g = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃² with f = 1 −
μ/R², μ constant and ψ = ψ(v̂), the slice Σ_τ0 (v̂ = τ0 + R) has γ = G dR² + R² dΩ₃² with G = e^ψ(2 − e^ψ f), and
N_s√G = 1. Along it write ψ, ψ′ and ψ″ for ψ(τ0 + R) and its derivatives, q := e^ψ, 𝔲 := 1 − q, m := μ/R² and
W := qf = q(1 − m). The quantities ν, β_K, 𝔞, E, P and Γ of [[thm:charge-identity]] are then ν = R³,
β_K = R N_κ/(3(2 − W)(W − 1)) with N_κ = (q f′/2)(W − 3) − ψ′ and f′ = 2μ/R³ (from κ0 and Y0 of
[[lem:racz-split-formulas]]; N_κ is the quantity of [[lem:margins-racz]], here with ψ ≠ 0 and μ̇ = 0),
𝔞 = −3(1 − β_K)/R, E = e^(∫𝔞), P = 8νE²R/G − (2νER/√G)′ RE/√G and Γ = 4νE² − P′.

**Lemma {#lem:margins-gamma-form}** (Γ/E² in closed form.) On such a region, wherever W < 1,

    Γ/E² = A0 + A1 ψ′ + A2 ψ′² + A3 ψ″,   {#eq:margins-gamma-form}

    A0 := 4R³ n0/(q(2 − W)(1 − W)²),
    n0 := m³ − 2m(2m² − m + 1)𝔲 + (2m + 1)(3m² − 5m + 4)𝔲² − 4m(m − 1)²𝔲³ + (m − 1)³𝔲⁴,
    A1 := 2R⁴ (m(5 − m) − (1 − m)(7 + m)𝔲)/((2 − W)(1 − W)²),
    A2 := 2R⁵ (1 − m)(1 + 2W)/((2 − W)(1 − W)²),     A3 := 2R⁵ (1 − m)/((2 − W)(1 − W)).

Where ψ = 0 this is Γ/E² = 4R³μ/(R² + μ), that is Γ = 4μ/R for the normalisation E = √G/R.

*Proof.* Since E′ = 𝔞E and ν = R³, (2νER/√G)′ = E((2R⁴/√G)′ + 2𝔞R⁴/√G), so P = E²p with p := 8R⁴/G −
R(2R⁴/√G)′/√G − 2𝔞R⁵/G = (R⁵/G)(G′/G − 2𝔞), and Γ/E² = 4R³ − 2𝔞p − p′. Here G′/G = ψ′ − W′/(2 − W) with
W′ = q(ψ′f + f′), and 𝔞 = −3/R + N_κ/((2 − W)(W − 1)). Substituting, p′ contains ψ″ linearly through ψ″ in (G′/G)′
and in N_κ′ = (q/2)(ψ′f′ + f″)(W − 3) + (qf′/2)W′ − ψ″, f″ = −6μ/R⁴. Clearing the common denominator
qR⁶(2 − W)(1 − W)² and collecting the coefficients of 1, ψ′, ψ′² and ψ″, the numerator of the ψ′⁰ term becomes 4R⁹n0
after the substitution q = 1 − 𝔲, m = μ/R², which gives the stated A0, A1, A2, A3. At ψ = 0, 𝔲 = 0 and ψ′ = ψ″ = 0,
so Γ/E² = A0 = 4R³m³/((1 + m)m²) = 4R³μ/(R² + μ). Since E′ = 𝔞E fixes E only up to a constant factor, and Γ scales
with E², the last statement is for the normalisation E = √G/R, which solves E′ = 𝔞E where ψ = 0; there
E² = (R² + μ)/R⁴, and Γ = 4μ/R. ∎

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
(a), with R the cell, q = e^ψ, 𝔲 = 1 − q, m = μ/R², W = q(1 − m) and 2 − W, 1 − W positive on every cell. The resulting
lower ends are columns (a) and (b); their least values are 0.456 and 0.438, which exceed 0.4475 and 0.048. ∎

By [[prop:bg-seed]] (c), the background itself lies in the tube of (b), which gives Γ > 0 on its seed region; with
[[prop:bg-region-three-end]] it follows that Γ > 0 at every point of Σ_τ0 in region III, {0.70 ≤ R ≤ R_u2}, as
[[cor:loc-charge-seed]] uses.
