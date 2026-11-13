## Bondi coordinates and the mass law at past null infinity {#ch:bondi}

This chapter proves [[thm:bondi-law]]: the solution g_λ of [[thm:past-construction]] admits Bondi coordinates near past
null infinity, and in them its mass aspect obeys the five-dimensional Bondi law. The law is due to Tanabe, Tanahashi and
Shiromizu [TTS09]. We derive it again in the class at hand, with every coefficient general from the first order on, so
that nothing in the proof is taken from [TTS09] except the comparison. What has to be shown is that g_λ has the
asymptotic expansion at past null infinity which the law needs, in Bondi coordinates built on g_λ itself, and what the
law then gives.

The argument has four steps. At fixed λ the far region of [[thm:past-construction]] is a neighbourhood of past null
infinity, and there the remainder g_λ − g_app solves a wave equation whose source decays like r^(−3). First, every
derivative of the remainder obeys the bound which the construction gives for the first few
(Section [[sec:bondi-every-order]]). Second, subtracting the explicit leading term of the source and estimating the rest
with the energy of the far region gains half a power of r; repeated, this gives an expansion of g_λ − g0 in powers of
r^(−1/2) to any order, with the radiation field as its leading term. The derivatives of the remainders along the ingoing
generators gain a full order, because for them the wave equation is a transport along the outgoing generators, and these
reach the seed region, where everything vanishes, after a bounded parameter length (Section [[sec:bondi-expansion]]).
Third, Bondi coordinates are built from the null geodesics of g_λ asymptotic to the ingoing generators of the
background, in the manner of the eikonal function of [HL21] at future null infinity (Section [[sec:bondi-chart]]).
Fourth, in the Bondi form the vacuum equations are a hierarchy in r^(−1/2). Its radial equations kill every coefficient
below the waves' and fix the shift and the first correction of W; the traceless angular equation makes the r^(−2)
coefficients of the angular metric constant in v, which the seed sets to zero; and R_vv at order r^(−3) is the mass law
plus a divergence that then vanishes (Section [[sec:bondi-hierarchy]]).

Throughout the chapter λ is fixed, 0 < λ ≤ λ_P, and every constant may depend on λ.

### The setting at fixed λ {#sec:bondi-setting}

We use the notation of Chapter 9 [[pending:ch9-decay-classes]]. X = (τ, x) ∈ R × R⁴, r = |x|, x̂ = x/r, v = τ + r and
t := 1 + τ0 − τ; P is the past domain of [[thm:past-construction]], P+ := P ∩ {v ≥ v_start}, Σ_τ the slices of constant
τ, and ‖·‖ the flat L² norm on Σ_τ ∩ P+. The field ℓ := g0⁻¹ dv is null and tangent to the ingoing generators of the
cones {v = const}; ℓf := df(ℓ), and on P+ we use the coordinates (v, r, x̂), in which ℓ = ∂_r and ∂_v is the derivative at
fixed (r, x̂). Ω_ab := x_a ∂_b − x_b ∂_a are the rotations of R⁴, and □̃ := g0^{ab} ∂_a ∂_b acts on Cartesian components.
On S³ we use the polar angle ϑ ∈ [0, π/2] and the angles φ1, φ2 of the two rotation planes, the round metric being
γ = dϑ² + cos²ϑ dφ1² + sin²ϑ dφ2².

For p ≥ 0, E_p is the class of tensors f on P+ (Cartesian components) that vanish for v ≤ v_start and satisfy
|∂_X^α Ω^β f| ≤ C r^(−p) for all α and β. At fixed λ an oscillating factor [f], the profile f taken at the phase v/λ,
belongs to these classes like any other function, since each derivative of [f] costs a factor λ^(−1), now a constant. A
coefficient that does not vanish for v ≤ v_start, such as g0 − η or Γ[g0], is said to be in E_p when it obeys the same
bounds. The classes multiply, E_p E_q ⊂ E_(p+q), and E_p ⊂ E_q for p ≥ q, since r ≥ 1 on P+. On P+ the quantities t and
r are comparable, t + a1 ≤ r ≤ t + a2 [[pending:ch9-past-domain]].

The *far region* is P ∩ {t ≥ T}, T := λ^(−2) [[pending:ch9-far-region]]. On it [[thm:past-construction]] and its
proof give

    u := g_λ − g0 = λ[W_TT] + u_1,       λ[W_TT] = r^(−3/2) G_3,                                    {#eq:bondi-u-split}

with u_1 in E_2 pointwise together with the Cartesian derivatives that the construction controls (the terms of u_1 are
m1, χ, the later stages, the Taylor terms of the phase and the remainder w := g_λ − g_app)
[[pending:ch9-proof-of-past-construction]]. Here G_3(v, x̂) denotes the r^(3/2)-normalised Cartesian components of λW_TT
at the phase v/λ. By the formula for the first-order wave [[pending:ch2-waves]],

    λ W_TT = 2 r^(1/2) (cos²ϑ p1 dφ1² + sin²ϑ p2 dφ2² − (p1 + p2) dϑ²),
    p1 := (2 cos²ϑ G − sin²ϑ F)/3,     p2 := (2 sin²ϑ F − cos²ϑ G)/3,                               {#eq:bondi-wave}

with the free data F = λ A env(v) h sin(v/λ) and G = λ A env(v) h cos(v/λ), h the angular profile. In the orthonormal
coframe (r dϑ, r cos ϑ dφ1, r sin ϑ dφ2) the components of (eq:bondi-wave) are r^(−3/2) times −2(p1 + p2), 2p1 and 2p2,
and the coframe has bounded Cartesian components with bounded derivatives along x̂; so G_3 is smooth and bounded with
all its derivatives, smooth at the axes [[pending:ch2-waves]], and zero for v ≤ v_start, where env vanishes. The
construction controls finitely many derivatives of u_1: with the regularity index 6, the far-region estimate and the
Sobolev inequality with rotations of Chapter 9 give ∂^i w ∈ E_2 for i ≤ 4, the higher norms bounded
[[pending:ch9-far-region]] [[pending:ch9-sobolev]]. The approximating solutions of the construction give every order at
fixed λ, uniformly; this is [[lem:every-order-fixed]], which the induction of Section [[sec:bondi-expansion]] consumes.

### Every order at fixed λ {#sec:bondi-every-order}

**Lemma {#lem:every-order-fixed}** (Every order at fixed λ.) Every Cartesian derivative ∂_X^α Ω^β u_1 is in E_2 on the
far region, with constants depending on λ and on the order.

