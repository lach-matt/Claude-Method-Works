## The construction from past null infinity {#ch:past-construction}

This chapter proves [[thm:past-construction]]: the waves are prescribed by their own free data at past null infinity,
the solution is constructed on a past domain P together with Ω, and the constraints are never solved. Before the shell
the solution is the black hole: the region v ≤ v_start is a past set for the black hole's cones, and the data there are
the black hole's. Near past null infinity every stage of the approximant is solved with nothing coming in. Each stage
has an explicit leading term in r and a remainder half a power of r better, and no forcing term of a stage falls off
like r^(−5/2), the rate that would produce a logarithm. So the residual decays like r^(−3), and the remainder is
estimated with the rotations as commutators, which gain t^(−3/2) in Sobolev's inequality. The past is split at
t = λ^(−2). Before the split, the one coefficient of size 1/λ integrates in time to a constant, and no decomposition is
needed. After it, the decomposition of the proof of [[thm:uniform-existence]] runs over an interval of length λ^(−2);
there the transport of its auxiliary field loses a logarithm per unit of log t, which weights (T_λ/t)^β0 absorb at a
cost λ^(−2β0), with β0 independent of the order of the approximant. The mollifier's commutator with the wave operator
is, apart from decaying terms, an exact derivative along the generators, and is absorbed into the auxiliary field. The
limit is vacuum because the gauge field of the approximant decays at past null infinity.

The notation is that of [[ch:horizon-mass]] and of [[thm:approximant]]: the seed of mass μ0, the amplitude A, the
envelope env, the wave W_TT with free data F, G at past null infinity ([[sec:waves]]), the means m_j, phases φ_j
and oscillating profiles ĝ_j of the stages ([[eq:ansatz]]), and □̃ := g0^(ab) ∂_a ∂_b acting componentwise.

### The past domain {#sec:past-domain}

Put t := 1 + τ0 − τ for τ ≤ τ0, fix κ := 1/2, h(τ) := κ t^(−1/4), and V_P := V + 1 + (τ_end − τ0) + κ, with
V := v_end + T and τ_end as in [[sec:domain]], so that V_P − κ is the largest v on Σ_τ0 ∩ Ω. Let

    P := { τ ≤ τ0,  |x| ≥ a,  v + h(τ) ≤ V_P },      P⁺ := P ∩ {v ≥ v_start},
    A_P(τ) := Σ_τ ∩ P⁺ = { r_in(τ) ≤ |x| ≤ r_out(τ) },   r_in := v_start − τ,   r_out := V_P − h(τ) − τ.
                                                                                                    {#eq:past-domain}

**Lemma {#lem:past-domain}** (The past domain.) (a) Each Σ_τ is spacelike. (b) The outer boundary B := {v + h(τ) =
V_P} is spacelike, with Φ := v + h(τ),

    g0⁻¹(dΦ, dΦ) = −2 h′ − h′² (1 + μ/r²) ≤ −(κ/2) t^(−5/4),

and v + h(τ) increases along future causal curves, so P lies to the past of B. (c) Σ_τ0 ∩ P = Σ_τ0 ∩ Ω. (d) On P⁺,
t + a1 ≤ r ≤ t + a2 with a1 := v_start − τ0 − 1 > √μ0 and a2 := V_P − τ0 − 1, and the thickness r_out − r_in =
V_P − h − v_start lies in [d0, d1], d0 := V_P − κ − v_start ≥ 1, d1 := V_P − v_start. (e) L0 is tangent to the inner
boundary {v = v_start} of P⁺; the past integral curve of L0 through any point of P stays in P and runs to past null
infinity (v and x̂ fixed, r → ∞). (f) There is ε_P > 0 such that for every Lorentzian g on P with |g⁻¹ − g0⁻¹| ≤
ε_P t^(−5/4): B and the Σ_τ are spacelike for g with g⁻¹(dΦ, dΦ) ≤ −(κ/4) t^(−5/4); {r = a} is spacelike with r
decreasing along future causal curves; L0 is transverse to Σ_τ; and J⁻(p; g) ∩ {τ ≥ τ1} lies in P for every p in P and
τ1 ≤ τ(p).

*Proof.* (a) is [[lem:domain]] (a). (b) dΦ = dv + h′ dτ, with h′ = dh/dτ = (κ/4) t^(−5/4) > 0 because
dt/dτ = −1. By [[prop:vaidya]] (c)–(d), g0⁻¹(dv, dv) = 0, g0⁻¹(dv, dτ) = −1 and g0⁻¹(dτ, dτ) = −1 − μ/r²,
so g0⁻¹(dΦ, dΦ) = −2h′ − h′²(1 + μ/r²) ≤ −2h′ = −(κ/2) t^(−5/4). For a future causal Y, dv(Y) = −g0(L0, Y) ≥ 0 and
dτ(Y) > 0, so dΦ(Y) > 0. (c) At τ0, h = κ and the condition reads v ≤ V_P − κ. (d) On P⁺, r = v − τ = v − τ0 − 1 + t
with v ∈ [v_start, V_P]; a1 > √μ0 because v_start − τ0 > √μ0 + 1; and d0 ≥ 1 because V_P − κ = V + 1 + τ_end − τ0 ≥
v_start + 1. (e) Along −L0, v and x̂ are fixed, τ decreases and h decreases, so v + h ≤ V_P is kept, r = v − τ grows
without bound, and v ≥ v_start is kept. (f) The inequalities of (a), (b) and of [[lem:domain]] (b) are strict,
with a margin of at least (κ/2) t^(−5/4) in (b) and fixed margins in (a) and in [[lem:domain]] (b), the latter
holding at r = a < √μ0 whatever τ is; the causal claim follows as in [[lem:domain]] (e). ∎

**Lemma {#lem:seed-region}** (The seed region.) Let g solve Ric^H(g) = 0 on P ∩ {τ1 ≤ τ ≤ τ2}, be C², satisfy the
margin of [[lem:past-domain]] (f), and agree with g0 on Σ_τ1 ∩ {v ≤ v_start} together with its first τ-derivative.
Then g = g0 on P ∩ {τ1 ≤ τ ≤ τ2, v ≤ v_start}.

*Proof.* g0 is vacuum on {v ≤ v_start}, where μ is constant. For 0 < ε ≤ 1 let R_ε := P ∩ {τ ≥ τ1, v + ε h(τ) ≤
v_start}, and τ* the supremum of the τ′ ≤ τ2 with g = g0 on R_ε ∩ {τ ≤ τ′}. R_ε ∩ Σ_τ* is compact, g = g0 on it, and g is
continuous, so on a neighbourhood U of it |g⁻¹ − g0⁻¹| ≤ (εκ/8) t^(−5/4). There {v + ε h = v_start} is spacelike for g
and g0 with R_ε to its past (the calculation of [[lem:past-domain]] (b) with εκ in place of κ), and {r = a} likewise
([[lem:past-domain]] (f)). The difference u := g − g0 solves −½ g^(ab) ∂_a ∂_b u = f with |f| ≤ C(|u| + |∂u|), since
the principal part and Q of [[eq:gauge]] are smooth in (g, ∂g) and ∂²g0 is bounded; u = ∂_τ u = 0 on Σ_τ*,
and the proof of [[lem:energy]] on R_ε ∩ {τ* ≤ τ ≤ τ* + δ}, δ small so that the region lies in U, gives u = 0
there. So τ* = τ2. Letting ε → 0 covers {v < v_start}, and continuity covers v = v_start. ∎

### Inequalities on the past slices {#sec:past-inequalities}

All constants below depend on P (through a, a1, a2, d0, d1, κ) and not on τ or λ, and 0 < λ ≤ min(λ1, d0/20) with
λ1 := min(1, δ0)/10 as in [[eq:lambda-one]]. With Ω_ab := x_a ∂_b − x_b ∂_a the rotations of R⁴, the scaled norms
on A_P(τ) are

    |f|_(j,P) := Σ_(i + |β| ≤ j) λ^i ‖∂^i Ω^β f‖,      ‖·‖ the flat L²(A_P(τ)),                         {#eq:past-norms}

∂^i the spacetime coordinate derivatives of order i. The rotations carry no weight: Ω_ab τ = 0 and Ω_ab r = 0, so
Ω_ab v = 0 and Ω [f] = [Ω f] costs no power of λ. They also commute with □̃: they commute with ∂_τ and with the flat
Laplacian, and with L0 = ∂_τ − x̂·∂_x and the function μ(v)/r², which are invariant under rotations; and L0 L0 u =
L0^a L0^b ∂_a ∂_b u, the Cartesian components (1, −x̂) of L0 being constant along L0. Hence [Ω_ab, □̃] = 0.

**Lemma {#lem:past-sobolev}** (Sobolev with rotations; Poincaré.) (a) ‖f‖_∞ ≤ C t^(−3/2) Σ_(i + |β| ≤ 3) ‖∂_r^i Ω^β
f‖ on A_P(τ), ∂_r = x̂·∂_x; hence ‖∂^i f‖_∞ ≤ C λ^(−3−i) t^(−3/2) |f|_(i+3,P). (b) If f = 0 on {r = r_in(τ)}, then
‖f‖ ≤ C ‖∂_r f‖.

*Proof.* (a) In polar coordinates A_P(τ) = [r_in, r_out] × S³ with r_out − r_in in [d0, d1]. On [0, d] × S³ with the
product metric, H³ embeds in L^∞ with a constant uniform for d in [d0, d1] ([BH17, Theorem 7.26] in charts, for a
compact family of compact manifolds with boundary). The covariant derivatives of S³ are bounded by the rotations,
|∇^k f| ≤ C Σ_(|β| ≤ k) |Ω^β f|, because the Ω_ab span every tangent space of S³ and their commutators are rotations.
And ∫ |·|² dr dω ≤ r_in⁻³ ∫ |·|² r³ dr dω ≤ t⁻³ ‖·‖², since r_in ≥ t by [[lem:past-domain]] (d). For the scaled form
apply this to ∂^i f and reorder, using [Ω_ab, ∂_c] = −δ_ac ∂_b + δ_bc ∂_a. (b) On each ray f(r) is the integral of
∂_r f from r_in over a length at most d1, and r³ varies over the ray by a factor at most (1 + d1)³ since r_in ≥ 1;
Cauchy–Schwarz. ∎

**Lemma {#lem:past-mollifier}** (The mollifier on the past slices.) The mollifier [[eq:mollifier]], with
σ(τ, x) := σ0((|x| − r_in)/(r_out − r_in)) and ρ radial, satisfies (M1)–(M6) of [[lem:mollifier]] on A_P(τ)
for 0 < λ ≤ min(λ1, d0/20), with constants independent of τ, and commutes with the rotations, hence with T² and both
reflections.

*Proof.* The proof of [[lem:mollifier]] is local at the scale λ and uses only that the annulus has thickness
Δ := r_out − r_in at least d0 ≥ 1 and inner radius at least 1; that DΦ = I + λ E with E bounded with its derivatives
(E involves ∂σ, of size at most 7/d0, and ∂x̂, of size 1/r ≤ 1); that Φ is a diffeomorphism onto its image with
Jacobian bounded above and below uniformly in λ; and, for (M6), that ∂_τ r_in = −1 and ∂_τ r_out = −1 − h′ are
bounded. The Jacobian: Φ is radial, r ↦ r + 2λσ, so DΦ has the radial eigenvalue 1 + 2λ σ0′/Δ and the angular ones
1 + 2λσ/r. Since σ0 is non-increasing with |σ0′| ≤ 7, and λ/Δ ≤ λ/d0 ≤ 1/20, the radial eigenvalue lies in
[1 − 14/20, 1] = [3/10, 1]. Since |σ| ≤ 1, r ≥ r_in ≥ 1 and λ ≤ 1/10, |2λσ/r| ≤ 1/5, so the angular ones lie in
[4/5, 6/5]. The map Φ(x) = x + 2λσ x̂ and ρ are invariant under O(4), so 𝒫(f ∘ R) = (𝒫 f) ∘ R for R in O(4). ∎

**Lemma {#lem:past-commutator}** (The mollifier's commutator with □̃.) Write 𝒫 = 𝒞 ∘ M, with M f := ρ_λ * f the
convolution (ρ_λ(y) := λ⁻⁴ ρ(y/λ)) and 𝒞 g := g ∘ Φ the radial shift. In the coordinates (τ, v, x̂), with Δ(τ) :=
r_out − r_in, 𝒞 is g(τ, v, x̂) ↦ g(τ, ψ(τ, v), x̂), where ψ(τ, v) = v + 2λ σ0((v − v_start)/Δ(τ)), since |x| − r_in =
v − v_start at fixed τ. Put

    X_f := 4λ σ_v 𝒞(∂_r M f),      σ_v := σ0′((v − v_start)/Δ)/Δ.                                   {#eq:past-commutator}

Then [□̃, 𝒫] f = −L0 X_f + R_f, and for j ≤ k, with Z ranging over 𝒵 := {λ∂_τ, λ∂_r, Ω_ab} (∂_r = x̂·∂_x),

    ‖Z^j X_f‖ ≤ C λ Σ_(i ≤ j) ‖Z^i ∂f‖,
    ‖Z^j R_f‖ ≤ C (t⁻¹ + h′) Σ_(i ≤ j) ‖Z^i ∂f‖ + ‖Z^j R′_f‖,

where R′_f collects the terms with two time derivatives of f, each with a factor at most C λ (μ r⁻³ + |μ′| r⁻²); for
f = s := w(ℓ, ℓ) these are rewritten through the equation of [[lem:ell-ell]], as in Step 6 of the proof of
[[thm:uniform-existence]].

*Proof.* *The operator.* In the coordinates (τ, v, x̂), L0 = ∂_τ at fixed (v, x̂) and ∂_r = ∂_v at fixed τ, while
∂_τ at fixed x is L0 + ∂_v. The flat wave operator is −∂_τ² + ∂_r² + (3/r)∂_r + r⁻² Δ̊, with Δ̊ the Laplacian of the
unit S³, so it equals −(L0 + ∂_v)² + ∂_v² + (3/r)∂_v + r⁻² Δ̊ = −L0² − 2 ∂_v L0 + (3/r)∂_v + r⁻² Δ̊ (L0 and ∂_v are
coordinate fields and commute). With g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 and L0^a L0^b ∂_a ∂_b = L0²,

    □̃ = −(1 + μ/r²) L0² − 2 ∂_r L0 + (3/r) ∂_r + r⁻² Δ̊.

*The radial part.* Write □̃_rad for the first three terms, r = v − τ and ψ_τ := ∂_τ ψ, ψ_v := ∂_v ψ. With 𝒞 g =
g(τ, ψ, x̂), the chain rule gives L0 𝒞 g = 𝒞 L0 g + ψ_τ 𝒞 ∂_v g, ∂_v 𝒞 g = ψ_v 𝒞 ∂_v g, and the second derivatives
likewise. Collecting terms,

    [□̃_rad, 𝒞] g = −L0(2(ψ_v − 1) 𝒞 ∂_v g) + (3ψ_v/r − 3/(ψ − τ)) 𝒞 ∂_v g − μ(v)(1/r² − 1/(ψ − τ)²) 𝒞 L0² g
                   + ((μ(ψ) − μ(v))/(ψ − τ)²) 𝒞 L0² g
                   − (1 + μ(v)/r²)(2 ψ_τ 𝒞 ∂_v L0 g + ψ_τ² 𝒞 ∂_v² g + ψ_ττ 𝒞 ∂_v g) − 2 ψ_τ 𝒞 ∂_v² g.

For ψ independent of τ the last line vanishes: then □̃_rad 𝒞 g − 𝒞 □̃_rad g = −(μ(v)/r² − μ(ψ)/(ψ − τ)²) 𝒞 L0² g −
2(ψ_v − 1) 𝒞 ∂_v L0 g + (3ψ_v/r − 3/(ψ − τ)) 𝒞 ∂_v g, and −2(ψ_v − 1) 𝒞 ∂_v L0 g = −L0(2(ψ_v − 1) 𝒞 ∂_v g) since L0
commutes with 𝒞 and with ψ_v. When ψ depends on τ, L0 𝒞 g and L0² 𝒞 g acquire the terms with ψ_τ and ψ_ττ, and writing
−2(ψ_v − 1) 𝒞 ∂_v L0 g as −L0(2(ψ_v − 1) 𝒞 ∂_v g) adds 2 ∂_τ ψ_v 𝒞 ∂_v g + 2(ψ_v − 1) ψ_τ 𝒞 ∂_v² g; the terms with
∂_τ ψ_v cancel against those from −2 ∂_v L0 𝒞 g, and what remains is the last line. Here 2(ψ_v − 1) = 4λ σ_v, and

    ψ_τ = 2λ σ0′((v − v_start)/Δ) (v − v_start) h′/Δ²,

since Δ′ = −h′ by [[eq:past-domain]]; as |v − v_start| ≤ Δ, |σ0′| ≤ 7 and h″ = (5/4) h′/t, both ψ_τ and ψ_ττ are at
most C λ h′. Moreover |ψ − v| ≤ 2λ, so |μ(ψ) − μ(v)| ≤ 2λ |μ′|, |1/r² − 1/(ψ − τ)²| ≤ C λ r⁻³ and |3ψ_v/r − 3/(ψ − τ)|
≤ C/r.

*The angular part.* Δ̊ acts on x̂ at fixed (τ, v) and commutes with 𝒞, so [r⁻² Δ̊, 𝒞] = (r⁻² − (ψ − τ)⁻²) 𝒞 Δ̊, of size
C λ r⁻³ times two rotations, that is C λ r⁻¹ times two derivatives.

*The convolution.* M commutes with the constant-coefficient part η^(ab) ∂_a ∂_b of □̃; with the rest, −(μ/r²) L0 L0,
it commutes up to terms with the factor λ |∂(μ x̂ x̂/r²)| ≤ C λ (μ r⁻³ + |μ′| r⁻²) ((M5) of [[lem:mollifier]]).

*The bounds.* Apply the radial and angular identities to g = M f. A λ-weighted second spatial derivative of M f costs
no more than one derivative of f (Bernstein's inequality, (M2)). The term −L0(4λ σ_v 𝒞 ∂_v M f) is −L0 X_f, and
‖Z^j X_f‖ ≤ C λ Σ ‖Z^i ∂f‖ needs no decaying factor. Every other term carries a factor C/r ≤ C t⁻¹, or C λ h′ (the
last line, with two derivatives of M f, of which one is absorbed by the factor λ), or C λ (μ r⁻³ + |μ′| r⁻²) (the
terms with L0², which form R′_f). L0 commutes with λσ_v, 𝒞 and M up to factors C(h′ + r⁻¹): L0 σ_v = O(h′), the ψ_τ
terms above, and [x̂·∂_x, M] = O(λ r⁻¹) by (M5). The fields Z commute with these operators up to bounded operators of the
same order, which suffices, since every term of R_f already carries a decaying factor and the bound on X_f needs none.
Z commutes with L0 exactly (∂_τ, ∂_r and Ω_ab do, and L0 = ∂_τ − ∂_r in these coordinates), so the same holds at every
order. ∎

So the part of [□̃, 𝒫] f with no decaying factor is an exact L0-derivative. On Ω the commutator has the same form,
harmlessly. On P it would force the transport of Ψ := □̃ φ ([[lem:commutator-transport]]) by a term of size
‖∂s‖ with no decay; [[prop:near-region]] removes it by transporting Ψ − ½ X_s in place of Ψ.

**Lemma {#lem:past-energy}** (Energy on P.) Let g̃ be a Lorentzian metric on P with the margin of [[lem:past-domain]]
(f) and ‖∂g̃‖_∞ ≤ k(τ) on Σ_τ ∩ P⁺, and let u vanish on P ∩ {v ≤ v_start} and satisfy −½ g̃^(ab) ∂_a ∂_b u = f on
P ∩ {τ1 ≤ τ ≤ τ2}. Then for τ in [τ1, τ2]

    ‖∂u(τ)‖ ≤ C exp(C ∫_(τ1)^τ k) ( ‖∂u(τ1)‖ + ∫_(τ1)^τ ‖f‖ ),      ‖u(τ)‖ ≤ C ‖∂u(τ)‖.                {#eq:past-energy}

*Proof.* The proof of [[lem:energy]] on P ∩ {τ1 ≤ s ≤ τ}. B has P to its past with a spacelike normal for g̃
([[lem:past-domain]] (b), (f)), so its flux is nonnegative and is dropped. u vanishes near {r = a}. On P⁺ the slices
are uniformly spacelike and Y := −g̃⁻¹ dτ is uniformly timelike (g0⁻¹(dτ, dτ) = −1 − μ/r² with μ/r² bounded), so the
fluxes through Σ_τ are comparable to ‖∂u‖² with constants independent of τ. The bulk is at most C k ‖∂u‖² + ‖f‖ ‖∂u‖.
Gronwall's inequality gives the first bound, and [[lem:past-sobolev]] (b) the second. ∎

**Lemma {#lem:past-transport}** (Transport on P.) Let L0 ψ − (c0/r) ψ = f on P⁺ ∩ {τ1 ≤ τ ≤ τ2}, with c0 a constant,
and put γ := c0 − 3/2. With a₊ := a1 if γ > 0 and a₊ := a2 if γ ≤ 0,

    (t + a₊)^γ ‖ψ(τ)‖ ≤ (t1 + a₊)^γ ‖ψ(τ1)‖ + ∫_(τ1)^τ (t′ + a₊)^γ ‖f(τ′)‖ dτ′.                      {#eq:past-transport}

*Proof.* As in [[lem:transport]], ∂_τ ‖ψ‖² = 2⟨ψ, L0 ψ⟩ − ∫ (3/r) ψ² plus boundary terms. L0 is tangent to
{v = v_start}, so that face contributes nothing, and the outer face contributes −h′ ∫_(r = r_out) ψ² r³ dω ≤ 0. Hence
∂_τ ‖ψ‖² ≤ 2γ ∫ ψ²/r + 2⟨ψ, f⟩, and t + a1 ≤ r ≤ t + a2 ([[lem:past-domain]] (d)) gives ∂_τ ‖ψ‖ ≤ γ (t + a₊)⁻¹ ‖ψ‖ +
‖f‖. Since ∂_τ t = −1, ∂_τ ((t + a₊)^γ ‖ψ‖) ≤ (t + a₊)^γ ‖f‖. ∎

The transports used below have c0 = 0 (φ and its derivatives; γ = −3/2), c0 = 3/2 (the oscillating profiles; γ = 0)
and c0 = 2 (Ψ; γ = 1/2).

### Decay classes and the approximant from past null infinity {#sec:past-approximant}

On P⁺ we use the coordinates (v, r, x̂): ∂_v is the derivative at fixed (r, x̂), which is ∂_τ at fixed x, and ℓ is the
derivative at fixed (v, x̂), so that ℓ = −L0, ℓ(v) = 0, ℓ(r) = 1 and the radial derivative at fixed τ is ∂_v + ℓ.
Profiles are smooth on P × S¹ and vanish for v ≤ v_start, then to all orders at v = v_start, env being smooth.

- E_p: profiles f with |∂_X^α Ω^β ∂_θ^j f| ≤ C r^(−p) on P⁺ × S¹ for all α, β, j (∂_X the Cartesian derivatives).
- L_p ("a leading term"): f = r^(−p) F + f̃ with F(v, x̂, θ) smooth, bounded with all its derivatives and vanishing for
  v ≤ v_start, and f̃ in E_(p+1/2).
- O_p ("transported"): f in L_p whose remainder also has ℓ f̃ in E_(p+3/2); then ℓ f is in L_(p+1).

The L² norm on A_P(τ) of a profile of class E_q is at most C t^(3/2−q): by [[lem:past-domain]] (d) the annulus has
r ≥ t + a1 and thickness at most d1, so ∫ r^(−2q) r³ dr dω ≤ C t^(3−2q).

**Lemma {#lem:decay-calculus}** (The decay calculus.) (a) E_p E_q ⊂ E_(p+q) and L_p L_q ⊂ L_(p+q); ∂_X, Ω, ∂_θ and
∂_v preserve E_p and L_p.

(b) In (v, r, x̂), g0⁻¹(du, du′) = ∂_v u ℓu′ + ℓu ∂_v u′ + (1 − μ/r²) ℓu ℓu′ + r⁻² ⟨∂̊u, ∂̊u′⟩, with ∂̊ the
gradient on the unit S³; that is, g^vv = 0, g^vr = 1 and g^rr = 1 − μ/r². For every function,

    □̃ u = 2 ∂_v ℓ u + (3/r) ∂_v u + (1 − μ/r²) ℓ ℓ u + (3/r) ℓ u + r⁻² Δ̊ u.   {#eq:wave-operator-vr}

(c) □̃(r^(−p) F) = (3 − 2p) r^(−p−1) ∂_v F + E_(p+2) for F as in L_p. At p = 3/2 the first term vanishes, so □̃ W_TT is
in E_(7/2); and □̃ maps O_p into L_(p+1). The Cartesian components of W_TT are r^(−3/2) F_W with F_W(v, x̂, θ) smooth, so
W_TT is in O_(3/2), a pure leading term, and (ℓ + 3/(2r)) W_TT = 0.

(d) If f = r^(−q) f_q + f̃ is in L_q with q > 5/2, and c is in E_(3/2) (a multiplication, or a bounded operator on
zero-mean functions of θ with coefficients in E_(3/2), as in [[lem:first-stage-operator]]), then the transport
(ℓ + 3/(2r) + c) Z = f has exactly one solution with r^(3/2) Z → 0 along every generator, and

    Z = −r^(1−q) f_q/(q − 5/2) + Z̃   is in O_(q−1).

At q = 5/2 a logarithm appears: (ℓ + 3/(2r))(r^(−3/2) log r · f_(5/2)) = r^(−5/2) f_(5/2).

*Proof.* (a) Leibniz's rule, with ∂_X = x̂ (∂_v + ℓ) + r⁻¹ (angular derivatives), whose coefficients have bounded
derivatives; ∂_X (r^(−p) F) = r^(−p) x̂ ∂_v F + E_(p+1).

(b) Since v = τ + r, η = −dτ² + dr² + r² dω² = −dv² + 2 dv dr + r² dω², and g0 = η + (μ/r²) dv² = −(1 − μ/r²) dv² +
2 dv dr + r² dω². The (v, r) block, with rows (−(1 − μ/r²), 1) and (1, 0), has determinant −1 and inverse with rows
(0, 1) and (1, 1 − μ/r²), which gives the inverse metric. For [[eq:wave-operator-vr]]: □̃ is the flat wave operator
plus −(μ/r²) L0 L0 = −(μ/r²) ℓ ℓ (as in the proof of [[lem:past-commutator]]). The flat operator is −∂_τ² + ∂_r² +
(3/r) ∂_r + r⁻² Δ̊, and at fixed x̂, ∂_τ = ∂_v and the radial derivative at fixed τ is ∂_v + ℓ, so it equals −∂_v² +
(∂_v + ℓ)² + (3/r)(∂_v + ℓ) + r⁻² Δ̊ = 2 ∂_v ℓ + ℓℓ + (3/r)∂_v + (3/r)ℓ + r⁻² Δ̊, ∂_v and ℓ being coordinate fields.
Adding −(μ/r²) ℓℓ gives
[[eq:wave-operator-vr]].

(c) F does not depend on r at fixed (v, x̂), so ℓ F = 0 and ℓ(r^(−p) F) = −p r^(−p−1) F. In [[eq:wave-operator-vr]],
2 ∂_v ℓ (r^(−p) F) = −2p r^(−p−1) ∂_v F and (3/r) ∂_v (r^(−p) F) = 3 r^(−p−1) ∂_v F, which sum to (3 − 2p) r^(−p−1)
∂_v F; the other three terms are (1 − μ/r²) p(p + 1) r^(−p−2) F − 3p r^(−p−2) F + r^(−p−2) Δ̊F, in E_(p+2). On f̃ with
ℓ f̃ in E_(p+3/2) every term of [[eq:wave-operator-vr]] is in E_(p+3/2). For W_TT: in [[eq:waves-hopf]] write the
round coframe as r dϑ, r cos ϑ dξ1, r sin ϑ dξ2, whose Cartesian components depend on x̂ alone; then

    W_TT = r^(−3/2) · 2 λ⁻¹ (p1 (r cos ϑ dξ1)² + p2 (r sin ϑ dξ2)² − (p1 + p2)(r dϑ)²),

and λ⁻¹ p1, λ⁻¹ p2 are functions of (v, ϑ, θ). So r^(3/2) W_TT =: F_W does not depend on r, and it is smooth in
(v, x̂, θ), the axes included, because W_TT is smooth there ([[lem:waves]] (a)). Then (ℓ + 3/(2r)) W_TT =
−(3/2) r^(−5/2) F_W + (3/2) r^(−5/2) F_W = 0.

(d) Along a generator, with I(r) := −∫_r^∞ c, (r^(3/2) e^I Z)′ = r^(3/2) e^I f, and |I| ≤ C′ r^(−1/2); for an operator
c, e^I is the propagator of the linear ordinary differential equation along the generator, bounded since the integral of
the norm of c converges. So Z = −r^(−3/2) e^(−I) ∫_r^∞ r′^(3/2) e^(I(r′)) f dr′ is the solution, and every other
solution differs from it by r^(−3/2) e^(−I) times a function of (v, x̂, θ). For the leading term,
(ℓ + 3/(2r))(r^(1−q) A) = (1 − q + 3/2) r^(−q) A = (5/2 − q) r^(−q) A, which equals r^(−q) f_q for A = −f_q/(q − 5/2);
at q = 5/2 the same calculation with r^(−3/2) log r gives the logarithm. The remainder has forcing terms f̃ and −c Z in
E_(q+1/2), so the integral formula puts it in E_(q−1/2), and ℓ Z̃ = −(3/(2r)) Z̃ − c Z + f̃ is in E_(q+1/2). ∂_v, Ω and
∂_θ commute with ℓ and r, which gives the derivatives. ∎

**Theorem {#thm:past-approximant}** (The approximant from past null infinity.) For every N the stages of
[[thm:approximant]] have unique solutions on P with nothing coming in from past null infinity: the energy of each m_m
on A_P(τ) tends to zero as τ → −∞, and φ_m, χ and ĝ_(m+1) are the transport solutions of [[lem:decay-calculus]] (d)
that vanish there. They vanish for v ≤ v_start, are T² × Z2 × Z2-invariant, satisfy S g = g ([[lem:quarter-turn]]),
and

    W_TT ∈ O_(3/2) (a pure leading term),  χ ∈ O_2,  m_m ∈ L_2,  φ_m ∈ L_1 with ℓφ_m ∈ L_2,  ĝ_(m+1) ∈ O_2.
                                                                                                   {#eq:past-classes}

The approximant g_app built from them as in the proof of [[thm:approximant]] satisfies (E1) and (E2) of
[[thm:uniform-existence]] on P, and Ric^H(g_app) = λ^(N−1) [R_N] + λ^N [R′_N] with R_N, R′_N in E_3, uniformly for
0 < λ ≤ 1, so |Ric^H(g_app)|_(k,P) ≤ C_R λ^(N−1) t^(−3/2). On Ω the profiles continue as the solutions of
[[lem:stage-system]] with their own data on Σ_τ0, g_app is smooth on P ∪ Ω, and the conclusions of
[[thm:approximant]] hold on Ω.

*Proof.* *The count.* Give the factors of [[eq:gauge]] these classes: g0 − η in L_2 (a coefficient, not a
profile: it does not vanish for v ≤ v_start, and its class is used only through its bounds); Γ[g0] in E_2 (its μ′ part
is (μ′/(2r²)) ℓ dv dv) and H0^ρ := g0^(ab) Γ[g0]^ρ_(ab) in E_3; W_TT in O_(3/2); χ and ĝ_i in O_2; m_i in L_2; φ_i in L_1
with ℓφ_i in L_2.

*Claim:* for m ≥ 1, every monomial of the coefficient ℛ^(m) of λ^m ([[lem:first-entry]]) that contains none of
m_m, φ_m, ĝ_(m+1) lies in L_3. A monomial of [[eq:gauge]] has at most two derivatives; g⁻¹ is expanded about
g0⁻¹, each term of the expansion adding profile factors; the phase enters only through du = dv + Σ λ^j dφ_j acting on
an oscillating factor. (i) Two profile factors from {W, χ, ĝ_i, m_i} give L_3 at least ([[lem:decay-calculus]] (a)).
(ii) A factor dφ_i, in E_1 only, occurs as (∂_a φ_i) ∂_θ Y with Y oscillating. With a second profile factor besides Y
the monomial is in E_4. Without one, both derivatives sit on Y in the principal part, contracted by g0⁻¹, and the
monomial is one of g0⁻¹(dφ_i, dv) ∂_θ² Y = (ℓφ_i) ∂_θ² Y, g0⁻¹(dφ_i, dφ_j) ∂_θ² Y, g0⁻¹(dφ_i, d∂_θY) or (□̃ φ_i) ∂_θ Y.
By [[eq:wave-operator-vr]] the first is in L_2 L_(3/2); the second in L_3 L_(3/2), since g^vv = 0 and no product
∂_v φ_i ∂_v φ_j occurs; the third, ∂_v φ_i ℓ∂_θY + ℓφ_i ∂_v∂_θY + …, is in L_1 L_(5/2) + L_2 L_(3/2), since Y in O_p
gives ℓY in L_(p+1); and □̃ φ_i = 2 ∂_v ℓφ_i + (3/r) ∂_v φ_i + … is in L_2. Each is in L_(7/2). (iii) A monomial with
one profile factor and no dφ: the factor has weight j and carries derivatives of total weight m − j. If it is a mean
m_j, the only such terms are those of its own stage equation (j = m) and Γ[g0] times m_j (E_2 L_2). If it is
oscillating, two slow derivatives give □̃ Y (j = m; in L_3 by [[lem:decay-calculus]] (c), and in E_(7/2) for W_TT) and
one fast derivative gives the operator T̂ of [[lem:first-stage-operator]] applied to Y (j = m + 1: the unknown
ĝ_(m+1)); two fast derivatives carry g0⁻¹(dv, dv) = 0. This proves the claim. The same count shows that the
coefficients with which the unknowns enter (a)–(c) of [[lem:stage-system]] are in E_2 for m_m and E_3 for dφ_m
in (a), E_(3/2) for ĝ_(m+1) in (a) (the mean of a product with ∂_θ W), and, in (c), E_(3/2) for m_m, Ψ_m := □̃ φ_m and
ℓφ_m, and E_(5/2) for ∂_v φ_m and r⁻¹ Ω φ_m (which multiply ℓ∂_θW or r⁻¹ Ω ∂_θW).

*Stage 0.* The identities of [[lem:stage-zero]] hold pointwise wherever the profiles are defined. By [[lem:stage-zero]]
(b) and (d), with χ = 0 the oscillating part of R^(0) is F_2 dv ⊗ dv, with F_2 the second harmonic of
[[eq:chi-transport]]. F_2 is r⁻³ env² h² times a polynomial in sin θ, cos θ and the functions c², s² of x̂, so
F_2 = r⁻³ f3 with f3 a smooth function of (v, x̂, θ). So χ, the solution of [[eq:chi-transport]] that vanishes at past
null infinity, is r⁻² times a function of (v, x̂, θ): since (ℓ + 3/(2r))(r⁻² a) = −½ r⁻³ a for a independent of r,
∂_θ χ = −2 r⁻² f3, by [[lem:decay-calculus]] (d) at q = 3 with no remainder. So χ is in O_2. It is smooth at the axes,
by the argument given with [[eq:chi-transport]].

*Stage m ≥ 1.* Let the earlier stages be solved, in their classes. By the count, the forcing term of (a) is
𝒮_m = r⁻³ 𝒮_(m,3) + 𝒮̃_m with 𝒮̃_m in E_(7/2); the forcing term of (c) without the unknowns is r⁻³ K_(m,3) + E_(7/2);
and q_m is in L_3, each of its terms pairing two of m_i, dφ_i as in (ii). *Leading terms:* M_m := 2 ∫_(−∞)^v 𝒮_(m,3)
dv′, which vanishes for v ≤ v_start; m⁰ := r⁻² M_m; φ⁰ := −½ r⁻¹ M_m(ℓ, ℓ); ĝ⁰ := the leading term of
[[lem:decay-calculus]] (d) at q = 3 for the forcing r⁻³ K_(m,3). Then −½ □̃ m⁰ = −½ (3 − 4) r⁻³ ∂_v M_m + E_4 = r⁻³
𝒮_(m,3) + E_4 by [[lem:decay-calculus]] (c) at p = 2, and ℓφ⁰ = ½ r⁻² M_m(ℓ, ℓ) = ½ m⁰(ℓ, ℓ). So the remainders
(m̃, φ̃, ĝ̃) := (m_m − m⁰, φ_m − φ⁰, ĝ_(m+1) − ĝ⁰) solve the system (a)–(c) with every forcing term in E_(7/2): the
coefficients act on the leading terms through the classes of the count, and ℓφ̃ = ½ (m̃(ℓ, ℓ) + q_m) with q_m in E_3.

*Estimates.* For n large let P_n := P ∩ {τ ≥ τ_n}. [[lem:stage-system]], whose proof uses only
[[lem:energy]] and [[lem:transport]], holds on P_n with [[lem:past-energy]] and [[lem:past-transport]]
in their place, and gives the solution of the stage system on P_n whose data on Σ_(τ_n) are the leading terms; its
remainders start at zero. Commute the system with ∂_X and Ω to an order j0 (the classes are preserved), and let e(τ) be
the energy of m̃ to that order, f(τ) the norms of ∂_v φ̃ and Ω φ̃, p(τ) that of Ψ̃ := □̃ φ̃, and z(τ) that of Z̃ :=
∂_θ ĝ̃ (zero mean, so ‖ĝ̃‖ ≤ ‖Z̃‖). The L² norm of an E_q-profile on A_P(τ) is at most C t^(3/2−q), and
[[lem:past-sobolev]] (b) bounds m̃ by e. [[lem:past-energy]] for (a), [[lem:past-transport]] with c0 = 0 for ∂_v φ̃ and
Ω φ̃ (L0 commutes with ∂_v and Ω), with c0 = 2 for Ψ̃ (the transport of [[lem:commutator-transport]] with
σ̃ := m̃(ℓ, ℓ) + q_m in place of 𝒫 s, □̃ σ̃ taken from (a), so that no derivative is lost), and with c0 = 3/2 for Z̃
((c) and [[lem:first-stage-operator]]) give, with every integral over (τ_n, τ),

    e ≤ C ∫ ( t⁻² e + t^(−3/2) z + t⁻³ f + t⁻² ),            t^(−3/2) f ≤ C ∫ t^(−3/2) ( e + t^(−3/2) ),
    t^(1/2) p ≤ C ∫ t^(1/2) ( t⁻¹ e + t⁻² f + t^(−3/2) (z + p) + t⁻² ),
    z ≤ C ∫ ( t^(−3/2) (z + e + p) + t^(−5/2) f + t⁻² ).                                         {#eq:stage-estimates}

The bad terms of the forcing of Ψ̃, r⁻¹ (∂_τ + ∂_r) σ̃ and r⁻² ∂_r φ̃, are the t⁻¹ e and t⁻² f. Every kernel is
integrable at −∞, and the forcing terms give e, z ≤ A_e t⁻¹, f ≤ A_f and p ≤ A_p t⁻¹ uniformly in n, with the
constants taken in order. The quantities e and z are fed by f and p through kernels with an extra integrable power, so
for t ≥ T0, T0 large, [[eq:stage-estimates]] returns their bounds with a factor ½. The quantities f and p are fed by e
with kernels of size O(1): f ≤ (2/3) C sup t e and p ≤ 2C (A_e + A_f + 1) t⁻¹, so A_f := C′ A_e and A_p := C″(A_e +
A_f) close. And [1, T0] is a bounded interval, on which Gronwall's inequality applies.

As n → ∞ the solutions converge. The difference of the n-th and the n′-th solves the homogeneous system on P_n with
data on Σ_(τ_n) given by the n′-th remainders there, of sizes C t_n⁻¹ (for e, z, p) and O(1) (for f).
[[eq:stage-estimates]] without forcing keeps e and z of size C t_n⁻¹, p of size C t^(−1/2) t_n^(−1/2), and f,
transported with γ = −3/2, of size C (t/t_n)^(3/2) ≤ C t^(3/2) t_n^(−3/2); so the difference tends to zero on every
bounded part of P. The limit solves the stage system on P with the same bounds. A solution with nothing coming in is
unique, since the difference of two satisfies [[eq:stage-estimates]] without forcing and tends to zero at −∞.

*Classes.* [[lem:past-sobolev]] (a), with the bound of m̃ by e, turns e ≤ C t⁻¹ into m̃ in E_(5/2). Then σ̃ is in
E_(5/2); φ̃ = −½ ∫_r^∞ σ̃ dr′ is in E_(3/2), with ℓφ̃ in E_(5/2); Ψ̃ is in E_(5/2) by [[eq:wave-operator-vr]]; the
forcing term of (c) is in E_(7/2); and ĝ̃ is in E_(5/2) with ℓĝ̃ in E_(7/2). For the last, the integral formula of
[[lem:decay-calculus]] (d) with no leading term gives |ĝ̃| ≤ C r^(−3/2) ∫_r^∞ r′^(3/2) r′^(−7/2) dr′ = C r^(−5/2),
likewise for the derivatives that commute with ℓ, and ℓĝ̃ = −(3/(2r)) ĝ̃ − c ĝ̃ + (forcing) is in E_(7/2). So
ĝ_(m+1) = ĝ⁰ + ĝ̃ is in O_2. This is [[eq:past-classes]] at stage m.

*The residual, the phase, the continuation.* The argument of the proof of [[thm:approximant]] gives ℛ^(m) = 0 for m ≤ N −
1. The rest of the residual is λ^N times a sum of monomials of [[eq:gauge]] with all factors known, each in E_3 by the
count; the expansion of g⁻¹ converges uniformly, since |g_app − g0| ≤ C λ r^(−3/2). Rewriting with the fixed phase v
(Taylor's formula in λΨ about θ + φ1) multiplies profiles by powers of φ_j, keeping every product in its class, and costs
λ^(N+1) in the metric and so λ^(N−1) in Ric^H: R_N is in E_3. The scaled norm follows because ∂^i [f] costs λ^(−i) and Ω
costs nothing, and the L² norm of an E_3 profile on A_P(τ) is at most C t^(−3/2). (E1) holds (W_TT and χ dv dv are
transverse to ℓ), and (E2) by stage 0. On Σ_τ0 ([[lem:past-domain]] (c)) the profiles' data determine, by
[[lem:stage-system]] on Ω, solutions there; the two solve the same smooth linear system and agree on Σ_τ0 with all their
τ-derivatives, each fixed by the system from the data, so together they are smooth on P ∪ Ω. The stage system is
equivariant under T² × Z2 × Z2 and under S of [[lem:quarter-turn]], the condition of nothing coming in is invariant, and
the solutions are unique, so they are invariant. ∎

### The far and near regions {#sec:far-near}

Let β0 be the number of [[prop:near-region]], which does not depend on the order of the approximant. For K ≥ 6 take the
approximant of [[thm:past-approximant]] of order N := K + 4 + ⌈4β0⌉ and put K′ := N − 1 = K + 3 + ⌈4β0⌉, so that
F := −Ric^H(g_app) has |F|_(k,P) ≤ C_R λ^(K′) t^(−3/2), with k = 6. Put T_λ := λ⁻² and let τ_λ be the time with t =
T_λ; the *far region* is P ∩ {τ ≤ τ_λ}, the *near region* P ∩ {τ_λ ≤ τ ≤ τ0}.

*The coefficients on P.* By [[thm:past-approximant]] and [[eq:ue-linearisation]], on P⁺: the coefficients B and C
of the linearised operator are in E_(3/2), being built from g_app and ∂g_app, and ∂[λ g1] = dv [∂_θ g1] + λ [∂g1];
G1 := [∂_θ g1] and G2 := [∂_θ² g1] are in E_(3/2), and the slow derivative [ℓ ∂_θ g1] is in E_(5/2), since the
oscillating part W_TT(· + φ1) of g1 is in O_(3/2) up to L_(5/2); g_app⁻¹ − g0⁻¹ is in λ E_(3/2) and ℓ_app − ℓ in λ E_2.
The profile T1 of [[lem:phase-shift]] is in E_3: it collects the λ¹ terms of the linearisation in the direction
∂_θ G, namely ∂_θ ℛ^(1) = 0, −P_0(∂_θ g1) and −T(∂_θ g2), and the count of [[thm:past-approximant]] puts each in E_3.
For instance □̃(W_TT(· + φ1)) = □̃ W_TT + 2 g0⁻¹(dφ1, d∂_θ W_TT) + (□̃ φ1) ∂_θ W_TT + g0⁻¹(dφ1, dφ1) ∂_θ² W_TT, each in
E_(7/2), and ℓ + 3/(2r) annihilates W_TT and maps ĝ_2 into L_3. In the equation [[eq:ue-h]] for h
and in [[lem:ue-decomposition]] the terms in φ therefore have these coefficients: E_(3/2) on ℓφ = ½ 𝒫 s and on Ψ;
E_(5/2) on ∂_v φ (the slow coupling (∂_v ∂_θ g1)(∂_r φ) acts through ℓφ, by [[eq:wave-operator-vr]]) and on the
angular derivatives r⁻¹ Ω φ (the angular block r⁻² ⟨∂̊φ, ∂̊∂_θ g1⟩ of [[eq:wave-operator-vr]] is (r⁻¹ Ω φ) ·
(r⁻¹ Ω ∂_θ g1)); and E_3 on φ and on λ ∂_x² φ. The same holds for the ℓℓ contraction of [[lem:ell-ell]], in
which the dφ terms of B1 vanish, since the oscillating part of g1 is transverse to ℓ and ℓ depends on x̂ alone.

**Proposition {#prop:far-region}** (The far region.) There are λ_F > 0 and M_F, independent of τ_n, such that for
0 < λ ≤ λ_F and every τ_n < τ_λ, the solution g_n of Ric^H(g_n) = 0 on P ∩ {τ ≥ τ_n} with g_n = g_app and ∂_τ g_n =
∂_τ g_app on Σ_(τ_n) exists on P ∩ {τ_n ≤ τ ≤ τ_λ}, equals g0 on {v ≤ v_start} there, and w_n := g_n − g_app satisfies

    E(τ) := Σ_(i + |β| ≤ k) λ^i ‖∂^i Ω^β ∂w_n‖ ≤ M_F λ^(K′) t^(−1/2).                                    {#eq:far-energy}

*Proof.* Assume E ≤ 2 M_F λ^(K′) t^(−1/2). [[lem:past-sobolev]] gives |w_n| ≤ C M_F λ^(K′−3) t⁻² and |∂w_n| ≤
C M_F λ^(K′−4) t⁻², so g_n has the margin of [[lem:past-domain]] (f) (|g_app⁻¹ − g0⁻¹| ≤ C λ t^(−3/2)), and
[[lem:seed-region]] gives w_n = 0 on {v ≤ v_start}; also |∂g_n| ≤ C t^(−3/2). Apply λ^i ∂^i Ω^β to P(w) = F + 𝒬(w), the
equation for w without the decomposition ([[eq:ue-linearisation]]), and [[lem:past-energy]] with
k(τ) = C t^(−3/2):

(i) the term with coefficient 1/λ: λ⁻¹ |s G2|_k ≤ C λ⁻¹ t^(−3/2) E, by [[lem:past-sobolev]] (b) for the
undifferentiated s and [λ ∂G2] in E_(3/2);
(ii) B·∂w and C·w give C t^(−3/2) E;
(iii) the commutators [λ^i ∂^i Ω^β, g^(ab)] ∂_a ∂_b w are as in Step 4 of the proof of [[thm:uniform-existence]], with
λ^i ∂^i g_app in λ E_(3/2) for i ≥ 1; for the rotations, [Ω, □̃] = 0, and Ω and [Ω, ∂_a ∂_b], a combination of second
derivatives, act otherwise only through g⁻¹ − g0⁻¹, in λ E_(3/2) plus w; so they are at most C t^(−3/2) E;
(iv) the nonlinear terms are at most C λ⁻⁵ t^(−3/2) E², as in Step 4, with [[lem:past-sobolev]] (a) in place of
[[lem:sobolev]];
(v) |F|_k ≤ C_R λ^(K′) t^(−3/2).

On the far region t ≥ T_λ, so ∫ λ⁻¹ t^(−3/2) ≤ 2 λ⁻¹ T_λ^(−1/2) = 2: the coupling of size 1/λ integrates to a constant.
Since E(τ_n) = 0 and ∫_t^∞ t′^(−3/2) dt′ = 2 t^(−1/2), Gronwall's inequality gives E(τ) ≤ C e^(6C) (2 C_R λ^(K′) +
C M_F² λ^(2K′−5)) t^(−1/2), which is at most M_F λ^(K′) t^(−1/2) for M_F := 4 C e^(6C) C_R + 1 and λ small, as
2K′ − 5 > K′. Existence and continuation are Step 8 of the proof of [[thm:uniform-existence]] on the bounded pieces
P ∩ {τ_i ≤ τ ≤ τ_i + δ}, whose slices are compact annuli of the kind used there. ∎

**Proposition {#prop:near-region}** (The near region.) There are β0 ≥ 2, λ_N > 0 and M_N such that for 0 < λ ≤ λ_N the
solutions of [[prop:far-region]] continue to P ∩ {τ_λ ≤ τ ≤ τ0}, with w_n = h + φ [∂_θ g1] as in
[[sec:ue-decomposition]] (φ = 0 on Σ_(τ_λ)), and

    𝒩_P(τ) ≤ M_N λ^(K′) t^(−1/2) (T_λ/t)^β0      on [τ_λ, τ0].                                       {#eq:near-bootstrap}

Here 𝒩_P is the quantity 𝒩 of [[eq:ue-energy]] with four changes: Ω^β stands beside ∂^i in the
h-part (i + |β| ≤ k); the parts in φ and Ψ are commuted with Z ∈ 𝒵 = {λ∂_τ, λ∂_r, Ω_ab}, which commute with L0
exactly, and the second derivatives of φ are taken as λ (∂_r² φ, r⁻¹ ∂_r Ω φ, r⁻² Ω² φ) (with ∂_τ = L0 + ∂_r and
L0 φ = −½ 𝒫 s these give every second derivative; at each order the norms are equivalent to the Cartesian ones, with
constants depending on k); the Ψ-part is that of Ψ′ := Ψ − ½ X_s ([[lem:past-commutator]]); and the factor t^(−1/2) of
[[eq:near-bootstrap]] is t^(1/2) for the parts in φ. β0 depends only on the constants C of [[eq:near-lines]] below at
the orders j ≤ k, which are built from the bounds of g0, g1, g2, from P and from [[lem:past-sobolev]],
[[lem:past-mollifier]], [[lem:past-commutator]], [[lem:past-energy]] and [[lem:past-transport]]. The profiles g0, g1, g2
do not depend on N, since stage m of [[thm:past-approximant]] is fixed by the stages before it; every term with a
profile g_j, j ≥ 3, carries a factor λ and is absorbed for λ ≤ λ_N. In particular 𝒩_P(τ0) ≤ M_N λ^(K′−2β0).

*Proof.* Run Steps 1–7 of the proof of [[thm:uniform-existence]] on [τ_λ, τ], with these changes.
[[lem:past-sobolev]]–[[lem:past-transport]] replace [[lem:sobolev]], [[lem:mollifier]],
[[lem:energy]] and [[lem:transport]]; the mollifier is that of [[lem:past-mollifier]]; the
coefficients have the decay listed above; and the φ-quantities are transported from Σ_(τ_λ), where φ vanishes (h = w_n
there). Its Z-derivatives containing λ∂_τ, and Ψ′, do not vanish there, but with L0 φ = −½ 𝒫 s all are bounded by
C′ E(τ_λ), so 𝒩_P(τ_λ) ≤ C′ E(τ_λ) ≤ C′ M_F λ^(K′) T_λ^(−1/2) by [[eq:far-energy]], and each line below carries this
data term.

Write H for the h-part of 𝒩_P, Q′ for the Ψ′-part, and D0, D1, D2 for the parts ‖φ‖, the first derivatives
(∂_τ φ, ∂_r φ, r⁻¹ Ω φ) and the second derivatives of φ. Since Ψ = Ψ′ + ½ X_s and ‖Z^j X_s‖ ≤ C λ H by
[[lem:past-commutator]], the Ψ-part is at most Q′ + C λ H. The transport of Ψ′ follows from that of Ψ
([[lem:commutator-transport]]) and [[lem:past-commutator]]:

    (L0 − 2/r) Ψ′ = −½ 𝒫 □̃ s − ½ R_s + r⁻¹ X_s − r⁻¹ (∂_τ + ∂_r) 𝒫 s − 3 r⁻² ∂_r φ,            {#eq:psi-prime-transport}

in which the term ½ L0 X_s of −½ [□̃, 𝒫] s has been absorbed. With every integral over (τ_λ, τ), the initial values at
τ_λ of [[lem:past-transport]] being those of 𝒩_P(τ_λ) and included in the first term of each line:

    H ≤ C 𝒩_P(τ_λ) + C ∫ ( t^(−3/2) (H + Q′) + t^(−5/2) D1 + t⁻³ (D0 + D2) + λ^(K′) t^(−3/2) + R_nl ),
    t^(−1/2) (D0 + D1) ≤ C T_λ^(−1/2) 𝒩_P(τ_λ) + C ∫ t^(−1/2) H,
    t^(1/2) D2 ≤ C T_λ^(1/2) 𝒩_P(τ_λ) + C ∫ t^(1/2) H,
    t^(1/2) Q′ ≤ C T_λ^(1/2) 𝒩_P(τ_λ)
                 + C ∫ t^(1/2) ( t⁻¹ H + t⁻² D1 + t^(−3/2) (H + Q′) + t⁻³ (D0 + D2) + λ^(K′) t^(−3/2) + R_nl ),
                                                                                                    {#eq:near-lines}

with R_nl the nonlinear terms. The first line is Step 4 with the coefficients above; ℓφ = ½ 𝒫 s is bounded by H
through [[lem:past-sobolev]] (b). The second is Step 5: [[lem:past-transport]] with c0 = 0 for φ, ∂_τ φ and ∂_r φ and
c0 = 1 for r⁻¹ Ω φ, with forcing −½ Z^j of 𝒫 s, ∂_τ 𝒫 s, ∂_r 𝒫 s and r⁻¹ Ω 𝒫 s, the last bounded at top order by
Bernstein's inequality in one r⁻¹ Ω; the parts with c0 = 0 satisfy the stronger bound with t^(−3/2). The third: the
transports of λ ∂_r² φ, λ r⁻¹ ∂_r Ω φ and λ r⁻² Ω² φ have c0 = 0, 1, 2, so [[lem:past-transport]] applies with
c0 ≤ 2, and their forcing, λ times the same derivatives of 𝒫 s, is bounded by Bernstein's inequality (M2) in one ∂_r or
one r⁻¹ Ω. The fourth is [[lem:past-transport]] with c0 = 2 for [[eq:psi-prime-transport]]: [[lem:past-commutator]]
bounds R_s and r⁻¹ X_s by C (t⁻¹ + h′) H ≤ C t⁻¹ H, its terms R′_s being rewritten through [[lem:ell-ell]] as
in Step 6; r⁻¹ (∂_τ + ∂_r) 𝒫 s and r⁻² ∂_r φ give t⁻¹ H and t⁻² D1; and 𝒫 □̃ s is bounded through
[[lem:ell-ell]] with the coefficients above. Z commutes with L0, and [Z, r^(−c)] carries the factor r^(−c−1),
so every line holds at every order j ≤ k with c0 unchanged.

*The bootstrap.* Assume H, Q′ ≤ B t^(−1/2) (T_λ/t)^β and D0, D1, D2 ≤ B t^(1/2) (T_λ/t)^β on [τ_λ, τ], with
B := 8 C C′ (M_F + C_R + 1) λ^(K′), C the sum of the constants of each line of [[eq:near-lines]] and C′ ≥ 2. Two
integrals are used, for t ≤ T_λ and β > 1: for a > −β,

    ∫_t^(T_λ) t′^(−1−a) (T_λ/t′)^β dt′ ≤ T_λ^β ∫_t^∞ t′^(−1−a−β) dt′ = t^(−a) (T_λ/t)^β/(β + a),

and ∫_t^(T_λ) t′⁻¹ dt′ = log(T_λ/t) ≤ (T_λ/t)^β/β, since log x = β⁻¹ log x^β ≤ β⁻¹ x^β for x ≥ 1. Substituting the
assumed bounds, each integrand of [[eq:near-lines]], with the weight of its line, is B t′^(−1−a) (T_λ/t′)^β times a
constant, with the following exponents a:

- the H-line: t^(−3/2)(H + Q′) and t^(−5/2) D1 give a = 1, and t⁻³(D0 + D2) gives a = 3/2; the integrals are at most
  C B t⁻¹ (T_λ/t)^β/(β + 1), which is the bound of H times C t^(−1/2)/(β + 1);
- the D0/D1-line: t^(−1/2) H gives a = 0, so D0 + D1 ≤ (C/β) B t^(1/2) (T_λ/t)^β;
- the D2-line: t^(1/2) H gives a = −1, so D2 ≤ (C/(β − 1)) B t^(1/2) (T_λ/t)^β;
- the Q′-line: t^(1/2) t⁻¹ H and t^(1/2) t⁻² D1 give a = 0, so they contribute (C/β) B t^(−1/2) (T_λ/t)^β to Q′: this is
  the loss the split pays; t^(1/2) t^(−3/2)(H + Q′) gives a = 1/2 and t^(1/2) t⁻³(D0 + D2) gives a = 1, which carry an
  extra integrable power.

So every integral of a bootstrap quantity returns at most C/(β − 1) times the bound of its line. The data terms and the
forcing terms λ^(K′) t^(−3/2) together contribute at most B/8 times the bound of each line: 𝒩_P(τ_λ) ≤
C′ M_F λ^(K′) T_λ^(−1/2) and T_λ^(−1/2) ≤ t^(−1/2) for the H-line; t^(1/2) T_λ^(−1/2) 𝒩_P(τ_λ) ≤ C′ M_F λ^(K′) t^(1/2)
T_λ⁻¹ for the D0/D1-line; t^(−1/2) T_λ^(1/2) 𝒩_P(τ_λ) ≤ C′ M_F λ^(K′) t^(−1/2) for the D2- and Q′-lines; ∫ λ^(K′)
t′^(−3/2) ≤ 2 λ^(K′) t^(−1/2) in the H-line and ∫ t′^(1/2) λ^(K′) t′^(−3/2) = λ^(K′) log(T_λ/t) ≤ λ^(K′) (T_λ/t)^β/β in
the Q′-line; and C C′ M_F λ^(K′) + 2 C λ^(K′) ≤ B/8 since C′ ≥ 2.

The nonlinear terms are small. Every bootstrap quantity is at most B λ^(−2β) t^(1/2) ≤ B λ^(−2β−1), since (T_λ/t)^β ≤
T_λ^β = λ^(−2β) and t^(1/2) ≤ T_λ^(1/2) = λ⁻¹. So by [[lem:past-sobolev]] (a), R_nl ≤ C λ⁻⁵ t^(−3/2) (B λ^(−2β−1))².
Its contribution to the H-line is at most C B² λ^(−7−4β) ∫ t^(−3/2) ≤ 2 C B² λ^(−7−4β), and the bound of H is at least
B T_λ^(−1/2) = B λ; its contribution to t^(1/2) Q′ is at most C B² λ^(−7−4β) log T_λ ≤ C B² λ^(−8−4β), and the bound of
t^(1/2) Q′ is at least B. Both ratios are at most C B λ^(−8−4β), which is C″ λ^(K′−8−4β) since B is a constant times
λ^(K′). For β = β0, K′ = K + 3 + ⌈4β0⌉ ≥ 9 + 4β0, so the ratios are at most C″ λ and at most 1/8 for λ small.

Take β = β0 := max(2, 4C + 1), so that C/(β0 − 1) ≤ 1/4. Then each line returns at most (1/8 + 1/4 + 1/8) times its
bound: the bootstrap bounds improve to B/2. The margin of [[lem:past-domain]] (f) holds, by [[lem:past-sobolev]], as in
[[prop:far-region]]. At τ0, t = 1 and (T_λ/t)^β0 = λ^(−2β0), which gives 𝒩_P(τ0) ≤ M_N λ^(K′−2β0). ∎

### Proof of the construction {#sec:past-proof}

The proof below gives, for every K ≥ 6, numbers λ_P > 0 and C and, for 0 < λ ≤ λ_P, a smooth vacuum metric g_λ on
P ∪ Ω in the wave-map gauge relative to g0, with g_app the approximant of [[thm:past-approximant]] of order N =
K + 4 + ⌈4β0⌉, such that:

- (P-i) g_λ = g0 on P ∩ {v ≤ v_start}: the seed, exactly;
- (P-ii) for every v < V_P and x̂, r^(3/2) (g_λ − g0 − λ [W_TT])(v − r, r x̂) → 0 as r → ∞, with [W_TT] taken at the
  phase v/λ;
- (P-iii) on P, |g_λ − g_app| ≤ C λ^(K−3) t⁻² and |∂(g_λ − g_app)| ≤ C λ^(K−4) t⁻²;
- (P-iv) on Ω, the conclusions of [[thm:uniform-existence]] with this K, the bound on 𝒩 included;
- (P-v) g_λ is invariant under T² × Z2 × Z2, and it is the only solution of Ric^H(g) = 0 on P with (P-i), with
  |g − g_app| + |∂(g − g_app)| ≤ ε_U t^(−3/2), and with the energy of g − g_app on A_P(τ) tending to zero as τ → −∞;
  here ε_U > 0 is so small that this class lies in the margin of [[lem:past-domain]] (f), since |g_app − g0| ≤
  C λ t^(−3/2) and t^(−3/2) ≤ t^(−5/4).

These are items 1, 2, 3, 5 and the first part of item 4 of [[thm:past-construction]]; the second part of item 4 is
[[prop:past-items]].

*Proof of [[thm:past-construction]].* *The solution on P ∪ Ω.* At τ0, Data(w_n), the norm of (E4) of
[[thm:uniform-existence]], satisfies Data(w_n) ≤ C λ⁻¹ 𝒩_P(τ0) ≤ C M_N λ^(K′−2β0−1), since the term ‖∂_x(φ G1)‖
contains λ⁻¹ ‖φ‖; and K′ − 2β0 − 1 = K + 2 + ⌈4β0⌉ − 2β0 ≥ K + 2. (E1)–(E3) hold on Ω by [[thm:past-approximant]], so
[[thm:uniform-existence]] with this K continues g_n to Ω with its bound on 𝒩: (P-iv) for g_n.

*The limit.* For n′ > n, δ := g_n − g_n′ solves on P ∩ {τ ≥ τ_n} a linear system −½ g_n^(ab) ∂_a ∂_b δ = f with
|f| ≤ C(λ) t^(−3/2) (|δ| + |∂δ|), whose coefficient involves ∂²g_n′, at most C λ⁻¹ t^(−3/2). [[lem:past-energy]] gives
‖∂δ(τ)‖ ≤ C(λ) ‖∂w_n′(τ_n)‖ ≤ C(λ) M_F λ^(K′) t_n^(−1/2), and [[lem:energy]] continues the bound to Ω. So g_n
converges, with the bounds of [[prop:far-region]] and [[prop:near-region]] and of [[thm:uniform-existence]], uniformly
with k − 5 derivatives on compact sets. The limit is smooth: for fixed λ the higher norms of g_n are bounded uniformly
in n by the linear energy estimates for the commuted equation, with constants depending on λ and the order, whose
kernels are C(λ) t^(−3/2) on the far region, which is integrable, and are taken over the bounded interval [τ_λ, τ0] on
the near region, with no decomposition needed for fixed λ; the limit does not depend on the order used, by the
uniqueness of (P-v). It solves Ric^H(g_λ) = 0 on P ∪ Ω and equals g0 on {v ≤ v_start}: (P-i).

*The bounds (P-iii).* On the far region, [[eq:far-energy]] and [[lem:past-sobolev]] (a) give |w| ≤ C M_F λ^(K′−3) t⁻²
and |∂w| ≤ C M_F λ^(K′−4) t⁻². On the near region, [[eq:near-bootstrap]] with (T_λ/t)^β0 ≤ λ^(−2β0) gives
H ≤ M_N λ^(K′−2β0) t^(−1/2) and D0 ≤ M_N λ^(K′−2β0) t^(1/2), so by [[lem:past-sobolev]] (a) |h| ≤ C λ^(K′−2β0−3) t⁻²
and |φ G1| ≤ C λ^(K′−2β0−3) t⁻¹ · t^(−3/2), with one more factor λ⁻¹ for the first derivatives. Since K′ − 2β0 ≥ K + 3
> K, this is (P-iii).

*The gauge.* D(g_λ) solves the homogeneous linear system of the proof of [[lem:gauge-propagation]], whose coefficients
are built from g_λ, ∂g_λ and ∂²g_λ, and so are at most C(λ) t^(−3/2) on P⁺. D(g_λ) = D(g_app) + O(|w| + |∂w|), and
D(g_app) = Σ_(j≥1) λ^j [D_j] with D_j in E_2. Indeed, the λ⁰ part of D(g_app) comes from the fast derivative of λ[g1] in
g^(ab)(Γ[g] − Γ[g0])^ρ_(ab), and equals g0^(ρσ) (∂_θ g1)(ℓ, ·)_σ − ½ ℓ^ρ tr_(g0) ∂_θ g1; it vanishes by (E1) and tr W_TT
= 0, χ dv dv being transverse and traceless too. In the λ¹ part, the ∂_v-part of the slow divergence of W_TT is ∂_v
(W_TT(ℓ, ·)) = 0, since the Cartesian components of ℓ do not depend on v; the rest of it gains a power, as ℓ W_TT =
−(3/(2r)) W_TT and r⁻¹ Ω W_TT are in E_(5/2); and every other term is a product, or a derivative of a stage-j profile of
class E_2. An r⁻² amplitude on A_P(τ) has L² norm at most C (∫_(r_in)^(r_in+d1) r⁻⁴ r³ dr)^(1/2) ≤ C t^(−1/2); so the
energy of D(g_λ) on A_P(τ) is at most C t^(−1/2), and tends to zero as τ → −∞. [[lem:past-energy]], with the integrable
kernel C(λ) t^(−3/2), gives D(g_λ) = 0 on P. Then D = ∂_τ D = 0 on Σ_τ0, and [[lem:gauge-propagation]] gives D = 0 on Ω:
g_λ is vacuum.

*The radiation field (P-ii).* g_λ − g0 − λ[W_TT] = w + λ[m1] + λ[χ dv dv] + λ([W_TT(· + φ1)] − [W_TT]) +
Σ_(j≥2) λ^j [g_j]. Here |w| ≤ C λ^(K−3) t⁻², m1 and χ are in L_2, W_TT(· + φ1) − W_TT is in L_1 L_(3/2), and every g_j
with j ≥ 2 is in E_2 (means, oscillating profiles and the Taylor terms φ_i^p ∂_θ^p W_TT of the fixed-phase rewriting).
Along v = const and x̂ = const, t and r grow together (r − t is bounded on P⁺), so r^(3/2) times the sum tends to zero
as r → ∞.

*Uniqueness and symmetry (P-v).* For a second solution g′ with (P-i), |g′ − g_app| + |∂(g′ − g_app)| ≤ ε_U t^(−3/2)
and energy of g′ − g_app tending to zero, δ := g_λ − g′ solves a linear system with coefficients at most
C(λ) t^(−3/2) (they involve ∂²g_λ and ∂g′, both controlled), its energy tends to zero at −∞, and [[lem:past-energy]]
gives δ = 0 on P; the uniqueness of Step 8 of the proof of [[thm:uniform-existence]] continues this to Ω. The data at
past null infinity, g_app and the equation are invariant under T² × Z2 × Z2, so g_λ is too, by this uniqueness.
Finally, the argument of [[lem:gauge-propagation]] holds on Ω for g_λ, with the datum on Σ_τ0 being the trace of g_λ
itself. ∎

### The horizon and the mean mass for these solutions {#sec:past-items}

**Proposition {#prop:past-items}** (Items 6 and 7 of [[thm:main]] for the solutions of [[thm:past-construction]].)
Let g_λ be the solution of [[thm:past-construction]], K ≥ 6, λ ≤ λ_P. Then on D_T ∩ {τ ≥ τ0}:
(a) if μ0 > √72 l5², the conclusions of [[prop:one-zero]] hold for g_λ, with λ_H and C of the same form;
(b) the conclusions of [[prop:mean-mass]] hold for g_λ: |M[S_(v,r)](g_λ) − μ(v)| ≤ C λ² if v ≤ v_start or v ≥ v_end,
and ≤ C λ in between.

*Proof.* The proofs of [[prop:one-zero]] and [[prop:mean-mass]] in [[ch:horizon-mass]] use four facts about the
solution, and none about how its data were obtained. We check each for the g_λ of [[thm:past-construction]], with
g_app the approximant of [[thm:past-approximant]].

(1) *The remainder bounds:* g_λ = g_app + w on Ω with ‖∂^i w‖_∞ ≤ C M λ^(K−3−i) for i ≤ 4, as in
[[eq:remainder-pointwise]]. These follow from Step 1 of the proof of [[thm:uniform-existence]] once the bound on 𝒩 of
that theorem holds for g_λ itself on Ω. It does: the w_n of [[sec:past-proof]] have Data(w_n) ≤ C M_N
λ^(K′−2β0−1) ≤ C λ^(K+2) uniformly in n, and g_n → g_λ on Σ_τ0, so Data(w_λ) ≤ liminf Data(w_n), since the bound is
uniform in n and the slice is compact, so that the derivatives up to order k + 1 converge weakly in L². Then
[[thm:uniform-existence]] applied to the trace of g_λ on Σ_τ0 gives a solution on Ω with the bound on 𝒩, which is g_λ
by the uniqueness on Ω (Step 8 of its proof).

(2) *The first stage:* g1 = m1 + W(X, θ + φ1) with W = W_TT + χ dv², W(ℓ, ·) = 0 and tr W_TT = 0, m1 independent of θ.
The stages of [[thm:past-approximant]] are those of [[thm:approximant]] with nothing coming in, so W_TT is the same, and
χ is −2 r⁻² times a function of (v, x̂, θ), with no radiation at past null infinity ([[thm:past-approximant]], stage 0).
So tr_S W = 0 on every sphere, as in [[eq:wave-traceless]], and [[lem:sphere-two-scale]] applies to this g_app: along
every column θ⁺(g_app) = θ⁺(g0) + λ [Θ⁺_1] + λ² E⁺, with no term of order λ⁻², λ⁻¹ or λ⁰ beyond g0's. The later stages
are smooth on P ∪ Ω, and so bounded with their X-derivatives on the compact Ω.

(3) *The support of the oscillating profiles:* the stages of [[thm:past-approximant]] vanish for v ≤ v_start, and its
oscillating profiles are transport solutions along ℓ at fixed v with forcing supported in v_start < v < v_end
([[lem:decay-calculus]] (d), and on Ω [[lem:stage-system]] (c) with the trace data on Σ_τ0), so they vanish for
v ≥ v_end, as in the proof of [[prop:mean-mass]].

(4) *The symmetry:* the stages of [[thm:past-approximant]] satisfy S g = g ([[lem:quarter-turn]]): the stage system is
S-equivariant, the condition of nothing coming in is S-invariant, and the solutions are unique. So J* m1 = −m1.

With (1)–(4) the two proofs run verbatim. In the proof of [[prop:one-zero]], steps (i)–(ii) concern g0 and the
expansion as a function of the metric; (iii) is (2); (iv) is (1), giving C λ^(K−5) ≤ C λ; and (v) uses Ω, μ and r_q
only. In the proof of [[prop:mean-mass]], outside the shell g_app = g0 + λ m1 + λ² E by (3), DM[m1] = 0 by (4) and
naturality, and the remainder is O(λ^(K−4)) by (1); inside the shell the wave enters M[S](g_app) at order λ⁰ only
through ½ k^±(ℓ) ∂_θ tr_S g1, which vanishes by (2), θ⁻, the area and g(n⁺, n⁻) carrying none
([[lem:sphere-two-scale]]). ∎

The columns of [[prop:one-zero]] are those of D_T ∩ {τ ≥ τ0}. On P the columns continue below Σ_τ0, where (P-iii)
bounds g_λ − g_app and its first derivatives by C λ^(K−3) t⁻² and C λ^(K−4) t⁻², and the second derivatives that step
(iv) needs come from [[eq:far-energy]] and [[eq:near-bootstrap]] with [[lem:past-sobolev]]. So the same argument runs on
P ∩ {r ≤ R} for each R, with constants depending on R, θ⁺(g0) being of size 3/r far out. The statement above is on
D_T ∩ {τ ≥ τ0}, as item 4 of [[thm:past-construction]] is.

### The flux at past null infinity {#sec:flux}

By (P-ii) the radiation field of g_λ at past null infinity is λ[W_TT] exactly, at every λ: its two polarizations are
the free data F, G, with no correction at any order. Write P1(v, ϑ) := p1(v, ϑ, v/λ) and P2(v, ϑ) := p2(v, ϑ, v/λ) for
the polarizations of [[eq:waves-hopf]] at the phase v/λ, and

    a_s(v) := λ env(v) sin(v/λ),   a_c(v) := λ env(v) cos(v/λ),   D_s := a_s′,   D_c := a_c′,

so that F = A h(ζ) a_s and G = A h(ζ) a_c along the phase. The flux density is the quadratic form (4/3)(∂_v P1² + ∂_v P1
∂_v P2 + ∂_v P2²), whose phase mean at leading order is μ′ ([[eq:stage-zero]], [[prop:limit]]).

**Lemma {#lem:flux-density}** (The flux and its integral.) (a) The flux density is

    (4/3)(∂_v P1² + ∂_v P1 ∂_v P2 + ∂_v P2²) = (4/9) A² h(ζ)² (cos⁴ϑ D_c² + sin⁴ϑ D_s² − cos²ϑ sin²ϑ D_c D_s).

(b) Its mean over S³ is exactly

    (2/9) A² [ env² + λ² env′² + (1 − π/2) ( −½ (env² − λ² env′²) sin(2v/λ) + λ env env′ cos(2v/λ) ) ].   {#eq:flux}

(c) Its integral in v from −∞ is

    μ(v) − μ0 + (2/9) λ² A² ∫_(−∞)^v env′² + (1 − π/2)(2/9) A² ( (λ/4) env² cos(2v/λ) + (λ²/4) env env′ sin(2v/λ) )
        + (1 − π/2)(2/9) A² (λ²/4) ∫_(−∞)^v (env′² − env env″) sin(2v′/λ) dv′,

and the last term is O(λ³).

*Proof.* (a) Write c := cos ϑ, s := sin ϑ. By [[eq:waves-hopf]], ∂_v P1 = A h (2c² D_c − s² D_s)/3 and ∂_v P2 =
A h (2s² D_s − c² D_c)/3. Put a := 2c² D_c − s² D_s and b := 2s² D_s − c² D_c. Then a + b = c² D_c + s² D_s and
ab = 5 c² s² D_c D_s − 2c⁴ D_c² − 2s⁴ D_s², so a² + ab + b² = (a + b)² − ab = 3(c⁴ D_c² + s⁴ D_s² − c² s² D_c D_s), and
(4/3)(A² h²/9)(a² + ab + b²) is the stated form.

(b) The volume form of S³ in the angles of [[sec:horizon-notation]] is cos ϑ sin ϑ dϑ dξ1 dξ2, and with z := cos 2ϑ,
dz = −4 sin ϑ cos ϑ dϑ, so the mean over S³ of a function of ϑ is ½ ∫_(−1)^1 dz. Here h² = 2/(1 + z²), c² = (1 + z)/2
and s² = (1 − z)/2, so

    h² c⁴ = ½ + z/(1 + z²),    h² s⁴ = ½ − z/(1 + z²),    h² c² s² = (1 − z²)/(2(1 + z²)) = 1/(1 + z²) − ½.

The odd parts integrate to zero, so ⟨h² c⁴⟩ = ⟨h² s⁴⟩ = ½, and ⟨h² c² s²⟩ = ½ (2 arctan 1 − 1) = π/4 − ½. The sphere
mean of (a) is therefore (4/9) A² (½ D_c² + ½ D_s² − (π/4 − ½) D_c D_s) = (2/9) A² (D_c² + D_s² + (1 − π/2) D_c D_s).
Finally D_c = λ env′ cos(v/λ) − env sin(v/λ) and D_s = λ env′ sin(v/λ) + env cos(v/λ), so D_c² + D_s² = env² +
λ² env′², and D_c D_s = ½ (λ² env′² − env²) sin(2v/λ) + λ env env′ cos(2v/λ). This is [[eq:flux]].

(c) The non-oscillating part integrates to (2/9) A² ∫ (env² + λ² env′²) = μ(v) − μ0 + (2/9) λ² A² ∫ env′², by
μ′ = (2/9) A² env². For the oscillating part, the derivative of (λ/4) env² cos(2v/λ) + (λ²/4) env env′ sin(2v/λ) is

    −½ env² sin(2v/λ) + λ env env′ cos(2v/λ) + (λ²/4)(env′² + env env″) sin(2v/λ),

and adding (λ²/4)(env′² − env env″) sin(2v/λ) gives −½ (env² − λ² env′²) sin(2v/λ) + λ env env′ cos(2v/λ), the
oscillating bracket of [[eq:flux]]. One more integration by parts, with the antiderivative −(λ/2) cos(2v′/λ) of
sin(2v′/λ), shows that the last integral is O(λ³), env being smooth with compact support. ∎

Both boundary terms carry the factor 1 − π/2: the integrated flux is linear in the oscillating coefficient. While the
shell passes, the integrated flux oscillates about μ(v) − μ0 with amplitude (π/2 − 1)(λ/18) A² env², at twice the wave
frequency (π/2 − 1 ≈ 0.571). After the shell (env = env′ = 0) the integrated flux exceeds μ(v_end) − μ0 by exactly
(2/9) λ² A² ∫ env′² + O(λ³), which comes from the non-oscillating part. The phase mean of [[eq:flux]] is
μ′ + (2/9) λ² A² env′². The mass law that turns this flux into the Bondi mass of g_λ is [[thm:bondi-law]].
