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
envelope env, the wave W_TT with free data F, G at past null infinity ([[pending:eq-waves]]), the means m_j, phases φ_j
and oscillating profiles ĝ_j of the stages ([[pending:ansatz]]), and □̃ := g0^(ab) ∂_a ∂_b acting componentwise.

### The past domain {#sec:past-domain}

Put t := 1 + τ0 − τ for τ ≤ τ0, fix κ := 1/2, h(τ) := κ t^(−1/4), and V_P := V + 1 + (τ_end − τ0) + κ, with
V := v_end + T and τ_end as in [[pending:lem-domain]], so that V_P − κ is the largest v on Σ_τ0 ∩ Ω. Let

    P := { τ ≤ τ0,  |x| ≥ a,  v + h(τ) ≤ V_P },      P⁺ := P ∩ {v ≥ v_start},
    A_P(τ) := Σ_τ ∩ P⁺ = { r_in(τ) ≤ |x| ≤ r_out(τ) },      r_in := v_start − τ,   r_out := V_P − h(τ) − τ.   {#eq:past-domain}

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

*Proof.* (a) is [[pending:lem-domain]] (a). (b) dΦ = dv + h′ dτ, with h′ = dh/dτ = (κ/4) t^(−5/4) > 0 because
dt/dτ = −1. By [[pending:prop-vaidya-contractions]], g0⁻¹(dv, dv) = 0, g0⁻¹(dv, dτ) = −1 and g0⁻¹(dτ, dτ) = −1 − μ/r²,
so g0⁻¹(dΦ, dΦ) = −2h′ − h′²(1 + μ/r²) ≤ −2h′ = −(κ/2) t^(−5/4). For a future causal Y, dv(Y) = −g0(L0, Y) ≥ 0 and
dτ(Y) > 0, so dΦ(Y) > 0. (c) At τ0, h = κ and the condition reads v ≤ V_P − κ. (d) On P⁺, r = v − τ = v − τ0 − 1 + t
with v ∈ [v_start, V_P]; a1 > √μ0 because v_start − τ0 > √μ0 + 1; and d0 ≥ 1 because V_P − κ = V + 1 + τ_end − τ0 ≥
v_start + 1. (e) Along −L0, v and x̂ are fixed, τ decreases and h decreases, so v + h ≤ V_P is kept, r = v − τ grows
without bound, and v ≥ v_start is kept. (f) The inequalities of (a), (b) and of [[pending:lem-domain]] (b) are strict,
with a margin of at least (κ/2) t^(−5/4) in (b) and fixed margins in (a) and in [[pending:lem-domain]] (b), the latter
holding at r = a < √μ0 whatever τ is; the causal claim follows as in [[pending:lem-domain]] (e). ∎

**Lemma {#lem:seed-region}** (The seed region.) Let g solve Ric^H(g) = 0 on P ∩ {τ1 ≤ τ ≤ τ2}, be C², satisfy the
margin of [[lem:past-domain]] (f), and agree with g0 on Σ_τ1 ∩ {v ≤ v_start} together with its first τ-derivative.
Then g = g0 on P ∩ {τ1 ≤ τ ≤ τ2, v ≤ v_start}.

*Proof.* g0 is vacuum on {v ≤ v_start}, where μ is constant. For 0 < ε ≤ 1 let R_ε := P ∩ {τ ≥ τ1, v + ε h(τ) ≤
v_start}, and τ* the supremum of the τ′ ≤ τ2 with g = g0 on R_ε ∩ {τ ≤ τ′}. R_ε ∩ Σ_τ* is compact, g = g0 on it, and g is
continuous, so on a neighbourhood U of it |g⁻¹ − g0⁻¹| ≤ (εκ/8) t^(−5/4). There {v + ε h = v_start} is spacelike for g
and g0 with R_ε to its past (the calculation of [[lem:past-domain]] (b) with εκ in place of κ), and {r = a} likewise
([[lem:past-domain]] (f)). The difference u := g − g0 solves −½ g^(ab) ∂_a ∂_b u = f with |f| ≤ C(|u| + |∂u|), since
the principal part and Q of [[pending:eq-reduced]] are smooth in (g, ∂g) and ∂²g0 is bounded; u = ∂_τ u = 0 on Σ_τ*,
and the proof of [[pending:lem-energy]] on R_ε ∩ {τ* ≤ τ ≤ τ* + δ}, δ small so that the region lies in U, gives u = 0
there. So τ* = τ2. Letting ε → 0 covers {v < v_start}, and continuity covers v = v_start. ∎

### Inequalities on the past slices {#sec:past-inequalities}

All constants below depend on P (through a, a1, a2, d0, d1, κ) and not on τ or λ, and 0 < λ ≤ min(λ1, d0/20) with
λ1 := min(1, δ0)/10 as in [[pending:lem-sobolev]]. With Ω_ab := x_a ∂_b − x_b ∂_a the rotations of R⁴, the scaled norms
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

**Lemma {#lem:past-mollifier}** (The mollifier on the past slices.) The mollifier of [[pending:lem-mollifier]], with
σ(τ, x) := σ0((|x| − r_in)/(r_out − r_in)) and ρ radial, satisfies (M1)–(M6) of [[pending:lem-mollifier]] on A_P(τ)
for 0 < λ ≤ min(λ1, d0/20), with constants independent of τ, and commutes with the rotations, hence with T² and both
reflections.

*Proof.* The proof of [[pending:lem-mollifier]] is local at the scale λ and uses only that the annulus has thickness
Δ := r_out − r_in at least d0 ≥ 1 and inner radius at least 1; that DΦ = I + λ E with E bounded with its derivatives
(E involves ∂σ, of size at most 7/d0, and ∂x̂, of size 1/r ≤ 1); that Φ is a diffeomorphism onto its image with
Jacobian bounded above and below uniformly in λ; and, for (M6), that ∂_τ r_in = −1 and ∂_τ r_out = −1 − h′ are
bounded. The Jacobian: Φ is radial, r ↦ r + 2λσ, so DΦ has the radial eigenvalue 1 + 2λ σ0′/Δ and the angular ones
1 + 2λσ/r. Since σ0 is non-increasing with |σ0′| ≤ 7, and λ/Δ ≤ λ/d0 ≤ 1/20, the radial eigenvalue lies in
[1 − 14/20, 1] = [3/10, 1]. Since |σ| ≤ 1, r ≥ r_in ≥ 1 and λ ≤ 1/10, |2λσ/r| ≤ 1/5, so the angular ones lie in
[4/5, 6/5]. The map Φ(x) = x + 2λσ x̂ and ρ are invariant under O(4), so P(f ∘ R) = (P f) ∘ R for R in O(4). ∎

**Lemma {#lem:past-commutator}** (The mollifier's commutator with □̃.) Write P = C ∘ M, with M f := ρ_λ * f the
convolution (ρ_λ(y) := λ⁻⁴ ρ(y/λ)) and C g := g ∘ Φ the radial shift. In the coordinates (τ, v, x̂), with Δ(τ) :=
r_out − r_in, C is g(τ, v, x̂) ↦ g(τ, ψ(τ, v), x̂), where ψ(τ, v) = v + 2λ σ0((v − v_start)/Δ(τ)), since |x| − r_in =
v − v_start at fixed τ. Put

    X_f := 4λ σ_v C(∂_r M f),      σ_v := σ0′((v − v_start)/Δ)/Δ.                                     {#eq:past-commutator}

Then [□̃, P] f = −L0 X_f + R_f, and for j ≤ k, with Z ranging over 𝒵 := {λ∂_τ, λ∂_r, Ω_ab} (∂_r = x̂·∂_x),

    ‖Z^j X_f‖ ≤ C λ Σ_(i ≤ j) ‖Z^i ∂f‖,
    ‖Z^j R_f‖ ≤ C (t⁻¹ + h′) Σ_(i ≤ j) ‖Z^i ∂f‖ + ‖Z^j R′_f‖,

where R′_f collects the terms with two time derivatives of f, each with a factor at most C λ (μ r⁻³ + |μ′| r⁻²); for
f = s := w(ℓ, ℓ) these are rewritten through the equation of [[pending:lem-ell-ell]], as in Step 6 of the proof of
[[thm:uniform-existence]].

*Proof.* *The operator.* In the coordinates (τ, v, x̂), L0 = ∂_τ at fixed (v, x̂) and ∂_r = ∂_v at fixed τ, while
∂_τ at fixed x is L0 + ∂_v. The flat wave operator is −∂_τ² + ∂_r² + (3/r)∂_r + r⁻² Δ̊, with Δ̊ the Laplacian of the
unit S³, so it equals −(L0 + ∂_v)² + ∂_v² + (3/r)∂_v + r⁻² Δ̊ = −L0² − 2 ∂_v L0 + (3/r)∂_v + r⁻² Δ̊ (L0 and ∂_v are
coordinate fields and commute). With g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 and L0^a L0^b ∂_a ∂_b = L0²,

    □̃ = −(1 + μ/r²) L0² − 2 ∂_r L0 + (3/r) ∂_r + r⁻² Δ̊.

*The radial part.* Write □̃_rad for the first three terms, r = v − τ and ψ_τ := ∂_τ ψ, ψ_v := ∂_v ψ. With C g =
g(τ, ψ, x̂), the chain rule gives L0 C g = C L0 g + ψ_τ C ∂_v g, ∂_v C g = ψ_v C ∂_v g, and the second derivatives
likewise. Collecting terms,

    [□̃_rad, C] g = −L0(2(ψ_v − 1) C ∂_v g) + (3ψ_v/r − 3/(ψ − τ)) C ∂_v g − μ(v)(1/r² − 1/(ψ − τ)²) C L0² g
                   + ((μ(ψ) − μ(v))/(ψ − τ)²) C L0² g
                   − (1 + μ(v)/r²)(2 ψ_τ C ∂_v L0 g + ψ_τ² C ∂_v² g + ψ_ττ C ∂_v g) − 2 ψ_τ C ∂_v² g.

For ψ independent of τ the last line vanishes: then □̃_rad C g − C □̃_rad g = −(μ(v)/r² − μ(ψ)/(ψ − τ)²) C L0² g −
2(ψ_v − 1) C ∂_v L0 g + (3ψ_v/r − 3/(ψ − τ)) C ∂_v g, and −2(ψ_v − 1) C ∂_v L0 g = −L0(2(ψ_v − 1) C ∂_v g) since L0
commutes with C and with ψ_v. When ψ depends on τ, L0 C g and L0² C g acquire the terms with ψ_τ and ψ_ττ, and writing
−2(ψ_v − 1) C ∂_v L0 g as −L0(2(ψ_v − 1) C ∂_v g) adds 2 ∂_τ ψ_v C ∂_v g + 2(ψ_v − 1) ψ_τ C ∂_v² g; the terms with
∂_τ ψ_v cancel against those from −2 ∂_v L0 C g, and what remains is the last line. Here 2(ψ_v − 1) = 4λ σ_v, and

    ψ_τ = 2λ σ0′((v − v_start)/Δ) (v − v_start) h′/Δ²,

since Δ′ = −h′ by [[eq:past-domain]]; as |v − v_start| ≤ Δ, |σ0′| ≤ 7 and h″ = (5/4) h′/t, both ψ_τ and ψ_ττ are at
most C λ h′. Moreover |ψ − v| ≤ 2λ, so |μ(ψ) − μ(v)| ≤ 2λ |μ′|, |1/r² − 1/(ψ − τ)²| ≤ C λ r⁻³ and |3ψ_v/r − 3/(ψ − τ)|
≤ C/r.

*The angular part.* Δ̊ acts on x̂ at fixed (τ, v) and commutes with C, so [r⁻² Δ̊, C] = (r⁻² − (ψ − τ)⁻²) C Δ̊, of size
C λ r⁻³ times two rotations, that is C λ r⁻¹ times two derivatives.

*The convolution.* M commutes with the constant-coefficient part η^(ab) ∂_a ∂_b of □̃; with the rest, −(μ/r²) L0 L0,
it commutes up to terms with the factor λ |∂(μ x̂ x̂/r²)| ≤ C λ (μ r⁻³ + |μ′| r⁻²) ((M5) of [[pending:lem-mollifier]]).

*The bounds.* Apply the radial and angular identities to g = M f. A λ-weighted second spatial derivative of M f costs
no more than one derivative of f (Bernstein's inequality, (M2)). The term −L0(4λ σ_v C ∂_v M f) is −L0 X_f, and
‖Z^j X_f‖ ≤ C λ Σ ‖Z^i ∂f‖ needs no decaying factor. Every other term carries a factor C/r ≤ C t⁻¹, or C λ h′ (the
last line, with two derivatives of M f, of which one is absorbed by the factor λ), or C λ (μ r⁻³ + |μ′| r⁻²) (the
terms with L0², which form R′_f). L0 commutes with λσ_v, C and M up to factors C(h′ + r⁻¹): L0 σ_v = O(h′), the ψ_τ
terms above, and [x̂·∂_x, M] = O(λ r⁻¹) by (M5). The fields Z commute with these operators up to bounded operators of the
same order, which suffices, since every term of R_f already carries a decaying factor and the bound on X_f needs none.
Z commutes with L0 exactly (∂_τ, ∂_r and Ω_ab do, and L0 = ∂_τ − ∂_r in these coordinates), so the same holds at every
order. ∎

So the part of [□̃, P] f with no decaying factor is an exact L0-derivative. On Ω the commutator has the same form,
harmlessly. On P it would force the transport of Ψ := □̃ φ ([[pending:lem-commutator-transport]]) by a term of size
‖∂s‖ with no decay; [[prop:near-region]] removes it by transporting Ψ − ½ X_s in place of Ψ.

**Lemma {#lem:past-energy}** (Energy on P.) Let g̃ be a Lorentzian metric on P with the margin of [[lem:past-domain]]
(f) and ‖∂g̃‖_∞ ≤ k(τ) on Σ_τ ∩ P⁺, and let u vanish on P ∩ {v ≤ v_start} and satisfy −½ g̃^(ab) ∂_a ∂_b u = f on
P ∩ {τ1 ≤ τ ≤ τ2}. Then for τ in [τ1, τ2]

    ‖∂u(τ)‖ ≤ C exp(C ∫_(τ1)^τ k) ( ‖∂u(τ1)‖ + ∫_(τ1)^τ ‖f‖ ),      ‖u(τ)‖ ≤ C ‖∂u(τ)‖.                {#eq:past-energy}

*Proof.* The proof of [[pending:lem-energy]] on P ∩ {τ1 ≤ s ≤ τ}. B has P to its past with a spacelike normal for g̃
([[lem:past-domain]] (b), (f)), so its flux is nonnegative and is dropped. u vanishes near {r = a}. On P⁺ the slices
are uniformly spacelike and Y := −g̃⁻¹ dτ is uniformly timelike (g0⁻¹(dτ, dτ) = −1 − μ/r² with μ/r² bounded), so the
fluxes through Σ_τ are comparable to ‖∂u‖² with constants independent of τ. The bulk is at most C k ‖∂u‖² + ‖f‖ ‖∂u‖.
Gronwall's inequality gives the first bound, and [[lem:past-sobolev]] (b) the second. ∎

**Lemma {#lem:past-transport}** (Transport on P.) Let L0 ψ − (c0/r) ψ = f on P⁺ ∩ {τ1 ≤ τ ≤ τ2}, with c0 a constant,
and put γ := c0 − 3/2. With a₊ := a1 if γ > 0 and a₊ := a2 if γ ≤ 0,

    (t + a₊)^γ ‖ψ(τ)‖ ≤ (t1 + a₊)^γ ‖ψ(τ1)‖ + ∫_(τ1)^τ (t′ + a₊)^γ ‖f(τ′)‖ dτ′.                          {#eq:past-transport}

*Proof.* As in [[pending:lem-transport]], ∂_τ ‖ψ‖² = 2⟨ψ, L0 ψ⟩ − ∫ (3/r) ψ² plus boundary terms. L0 is tangent to
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

(d) If S = r^(−q) S_q + S̃ is in L_q with q > 5/2, and c is in E_(3/2) (a multiplication, or a bounded operator on
zero-mean functions of θ with coefficients in E_(3/2), as in [[pending:lem-th-operator]]), then the transport
(ℓ + 3/(2r) + c) Z = S has exactly one solution with r^(3/2) Z → 0 along every generator, and

    Z = −r^(1−q) S_q/(q − 5/2) + Z̃   is in O_(q−1).

At q = 5/2 a logarithm appears: (ℓ + 3/(2r))(r^(−3/2) log r · S_(5/2)) = r^(−5/2) S_(5/2).

*Proof.* (a) Leibniz's rule, with ∂_X = x̂ (∂_v + ℓ) + r⁻¹ (angular derivatives), whose coefficients have bounded
derivatives; ∂_X (r^(−p) F) = r^(−p) x̂ ∂_v F + E_(p+1).

(b) Since v = τ + r, η = −dτ² + dr² + r² dω² = −dv² + 2 dv dr + r² dω², and g0 = η + (μ/r²) dv² = −(1 − μ/r²) dv² +
2 dv dr + r² dω². The (v, r) block [[−(1 − μ/r²), 1], [1, 0]] has determinant −1 and inverse [[0, 1], [1, 1 − μ/r²]],
which gives the inverse metric. For [[eq:wave-operator-vr]]: □̃ is the flat wave operator plus −(μ/r²) L0 L0 =
−(μ/r²) ℓ ℓ (as in the proof of [[lem:past-commutator]]). The flat operator is −∂_τ² + ∂_r² + (3/r) ∂_r + r⁻² Δ̊, and at
fixed x̂, ∂_τ = ∂_v and the radial derivative at fixed τ is ∂_v + ℓ, so it equals −∂_v² + (∂_v + ℓ)² + (3/r)(∂_v + ℓ) +
r⁻² Δ̊ = 2 ∂_v ℓ + ℓℓ + (3/r)∂_v + (3/r)ℓ + r⁻² Δ̊, ∂_v and ℓ being coordinate fields. Adding −(μ/r²) ℓℓ gives
[[eq:wave-operator-vr]].

(c) F does not depend on r at fixed (v, x̂), so ℓ F = 0 and ℓ(r^(−p) F) = −p r^(−p−1) F. In [[eq:wave-operator-vr]],
2 ∂_v ℓ (r^(−p) F) = −2p r^(−p−1) ∂_v F and (3/r) ∂_v (r^(−p) F) = 3 r^(−p−1) ∂_v F, which sum to (3 − 2p) r^(−p−1)
∂_v F; the other three terms are (1 − μ/r²) p(p + 1) r^(−p−2) F − 3p r^(−p−2) F + r^(−p−2) Δ̊F, in E_(p+2). On f̃ with
ℓ f̃ in E_(p+3/2) every term of [[eq:wave-operator-vr]] is in E_(p+3/2). For W_TT: in [[eq:waves-hopf]] write the
round coframe as r dϑ, r cos ϑ dξ1, r sin ϑ dξ2, whose Cartesian components depend on x̂ alone; then

    W_TT = r^(−3/2) · 2 λ⁻¹ (p1 (r cos ϑ dξ1)² + p2 (r sin ϑ dξ2)² − (p1 + p2)(r dϑ)²),

and λ⁻¹ p1, λ⁻¹ p2 are functions of (v, ϑ, θ). So r^(3/2) W_TT =: F_W does not depend on r, and it is smooth in
(v, x̂, θ), the axes included, because W_TT is smooth there ([[pending:eq-waves]]). Then (ℓ + 3/(2r)) W_TT =
−(3/2) r^(−5/2) F_W + (3/2) r^(−5/2) F_W = 0.

(d) Along a generator, with C(r) := −∫_r^∞ c, (r^(3/2) e^C Z)′ = r^(3/2) e^C S, and |C| ≤ C′ r^(−1/2); for an operator
c, e^C is the propagator of the linear ordinary differential equation along the generator, bounded since the integral of
the norm of c converges. So Z = −r^(−3/2) e^(−C) ∫_r^∞ r′^(3/2) e^(C(r′)) S dr′ is the solution, and every other
solution differs from it by r^(−3/2) e^(−C) times a function of (v, x̂, θ). For the leading term,
(ℓ + 3/(2r))(r^(1−q) A) = (1 − q + 3/2) r^(−q) A = (5/2 − q) r^(−q) A, which equals r^(−q) S_q for A = −S_q/(q − 5/2);
at q = 5/2 the same calculation with r^(−3/2) log r gives the logarithm. The remainder has forcing terms S̃ and −c Z in
E_(q+1/2), so the integral formula puts it in E_(q−1/2), and ℓ Z̃ = −(3/(2r)) Z̃ − c Z + S̃ is in E_(q+1/2). ∂_v, Ω and
∂_θ commute with ℓ and r, which gives the derivatives. ∎

**Theorem {#thm:past-approximant}** (The approximant from past null infinity.) For every N the stages of
[[thm:approximant]] have unique solutions on P with nothing coming in from past null infinity: the energy of each m_m
on A_P(τ) tends to zero as τ → −∞, and φ_m, χ and ĝ_(m+1) are the transport solutions of [[lem:decay-calculus]] (d)
that vanish there. They vanish for v ≤ v_start, are T² × Z2 × Z2-invariant, satisfy S g = g ([[lem:quarter-turn]]),
and

    W_TT ∈ O_(3/2) (a pure leading term),  χ ∈ O_2,  m_m ∈ L_2,  φ_m ∈ L_1 with ℓφ_m ∈ L_2,  ĝ_(m+1) ∈ O_2.
                                                                                                   {#eq:past-classes}

The approximant g_app built from them as in [[pending:sec-fixed-phase]] satisfies (E1) and (E2) of
[[thm:uniform-existence]] on P, and Ric^H(g_app) = λ^(N−1) [R_N] + λ^N [R′_N] with R_N, R′_N in E_3, uniformly for
0 < λ ≤ 1, so |Ric^H(g_app)|_(k,P) ≤ C_R λ^(N−1) t^(−3/2). On Ω the profiles continue as the solutions of
[[pending:lem-stage-system]] with their own data on Σ_τ0, g_app is smooth on P ∪ Ω, and the conclusions of
[[thm:approximant]] hold on Ω.

*Proof.* *The count.* Give the factors of [[pending:eq-reduced]] these classes: g0 − η in L_2 (a coefficient, not a
profile: it does not vanish for v ≤ v_start, and its class is used only through its bounds); Γ[g0] in E_2 (its μ′ part
is (μ′/(2r²)) ℓ dv dv) and H0 := g0^(ab) Γ[g0]_(ab) in E_3; W_TT in O_(3/2); χ and ĝ_i in O_2; m_i in L_2; φ_i in L_1
with ℓφ_i in L_2.

*Claim:* for m ≥ 1, every monomial of the coefficient ℛ^(m) of λ^m ([[pending:lem-first-entry]]) that contains none of
m_m, φ_m, ĝ_(m+1) lies in L_3. A monomial of [[pending:eq-reduced]] has at most two derivatives; g⁻¹ is expanded about
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
one fast derivative gives the operator T̂ of [[pending:lem-th-operator]] applied to Y (j = m + 1: the unknown
ĝ_(m+1)); two fast derivatives carry g0⁻¹(dv, dv) = 0. This proves the claim. The same count shows that the
coefficients with which the unknowns enter (a)–(c) of [[pending:lem-stage-system]] are in E_2 for m_m and E_3 for dφ_m
in (a), E_(3/2) for ĝ_(m+1) in (a) (the mean of a product with ∂_θ W), and, in (c), E_(3/2) for m_m, Ψ_m := □̃ φ_m and
ℓφ_m, and E_(5/2) for ∂_v φ_m and r⁻¹ Ω φ_m (which multiply ℓ∂_θW or r⁻¹ Ω ∂_θW).

*Stage 0.* The identities of stage 0 ([[pending:stage-zero]]) hold pointwise wherever the profiles are defined. The
second harmonic of R^(0) is r⁻³ times a function of (v, x̂, θ), times dv ⊗ dv. Indeed, the terms of R^(0) linear in
W_TT are first harmonics, so the second harmonic comes from the terms quadratic in W_TT, which have two factors λ W_TT
and two fast derivatives λ⁻¹ dv ∂_θ. In the principal part −½ g^(ab) ∂_a ∂_b g the only such term is
½ λ W_TT^(ab) λ⁻² ∂_a v ∂_b v ∂_θ²(λ W_TT) = ½ W_TT(ℓ, ℓ) ∂_θ² W_TT = 0. The others come from the part of Ric^H
quadratic in first derivatives, with coefficients taken at g0: Ricci's terms in Γ Γ and in ∂(g⁻¹) ∂g, and those of the
gauge term, in which g_(mρ) meets only D^ρ and so cancels an inverse metric. Each is a contraction by g0⁻¹ of two
factors (∂_a v)(∂_θ W_TT)_(bc), with two indices left free. A contraction involving an index of dv gives g0⁻¹(dv, dv) =
0 or W_TT(ℓ, ·) = 0, so both dv indices are free; the four indices of the two factors ∂_θ W_TT are contracted with each
other, and on them g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 acts as η⁻¹, since W_TT(L0, ·) = 0. Since tr W_TT = 0, the quadratic
part of R^(0) is c0 |∂_θ W_TT|²_η dv ⊗ dv for a constant c0, and |∂_θ W_TT|²_η = r⁻³ |∂_θ F_W|²_η by
[[lem:decay-calculus]] (c), the components of η⁻¹ being constant. So χ, the solution of (ℓ + 3/(2r)) ∂_θ χ = (that
harmonic) vanishing at past null infinity, is r⁻² times a function of (v, x̂, θ): writing the harmonic as r⁻³ f3,
(ℓ + 3/(2r))(r⁻² A) = −½ r⁻³ A gives ∂_θ χ = −2 r⁻² f3, by [[lem:decay-calculus]] (d) at q = 3 with no remainder. So χ
is in O_2. It is smooth at the axes, as on Ω ([[pending:stage-zero]]).

*Stage m ≥ 1.* Let the earlier stages be solved, in their classes. By the count, the forcing term of (a) is
S_m = r⁻³ S_(m,3) + S̃_m with S̃_m in E_(7/2); the forcing term of (c) without the unknowns is r⁻³ K_(m,3) + E_(7/2);
and q_m is in L_3, each of its terms pairing two of m_i, dφ_i as in (ii). *Leading terms:* M_m := 2 ∫_(−∞)^v S_(m,3)
dv′, which vanishes for v ≤ v_start; m⁰ := r⁻² M_m; φ⁰ := −½ r⁻¹ M_m(ℓ, ℓ); ĝ⁰ := the leading term of
[[lem:decay-calculus]] (d) at q = 3 for the forcing r⁻³ K_(m,3). Then −½ □̃ m⁰ = −½ (3 − 4) r⁻³ ∂_v M_m + E_4 = r⁻³
S_(m,3) + E_4 by [[lem:decay-calculus]] (c) at p = 2, and ℓφ⁰ = ½ r⁻² M_m(ℓ, ℓ) = ½ m⁰(ℓ, ℓ). So the remainders
(m̃, φ̃, ĝ̃) := (m_m − m⁰, φ_m − φ⁰, ĝ_(m+1) − ĝ⁰) solve the system (a)–(c) with every forcing term in E_(7/2): the
coefficients act on the leading terms through the classes of the count, and ℓφ̃ = ½ (m̃(ℓ, ℓ) + q_m) with q_m in E_3.

*Estimates.* For n large let P_n := P ∩ {τ ≥ τ_n}. [[pending:lem-stage-system]], whose proof uses only
[[pending:lem-energy]] and [[pending:lem-transport]], holds on P_n with [[lem:past-energy]] and [[lem:past-transport]]
in their place, and gives the solution of the stage system on P_n whose data on Σ_(τ_n) are the leading terms; its
remainders start at zero. Commute the system with ∂_X and Ω to an order j0 (the classes are preserved), and let e(τ) be
the energy of m̃ to that order, f(τ) the norms of ∂_v φ̃ and Ω φ̃, p(τ) that of Ψ̃ := □̃ φ̃, and z(τ) that of Z̃ :=
∂_θ ĝ̃ (zero mean, so ‖ĝ̃‖ ≤ ‖Z̃‖). The L² norm of an E_q-profile on A_P(τ) is at most C t^(3/2−q), and
[[lem:past-sobolev]] (b) bounds m̃ by e. [[lem:past-energy]] for (a), [[lem:past-transport]] with c0 = 0 for ∂_v φ̃ and
Ω φ̃ (L0 commutes with ∂_v and Ω), with c0 = 2 for Ψ̃ (the transport of [[pending:lem-commutator-transport]] with
σ̃ := m̃(ℓ, ℓ) + q_m in place of P s, □̃ σ̃ taken from (a), so that no derivative is lost), and with c0 = 3/2 for Z̃
((c) and [[pending:lem-th-operator]]) give, with every integral over (τ_n, τ),

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

*The residual, the phase, the continuation.* The argument of [[pending:sec-fixed-phase]] gives ℛ^(m) = 0 for m ≤ N − 1.
The rest of the residual is λ^N times a sum of monomials of [[pending:eq-reduced]] with all factors known, each in E_3
by the count; the expansion of g⁻¹ converges uniformly, since |g_app − g0| ≤ C λ r^(−3/2). Rewriting with the fixed
phase v (Taylor's formula in λΨ about θ + φ1) multiplies profiles by powers of φ_j, keeping every product in its class,
and costs λ^(N+1) in the metric and so λ^(N−1) in Ric^H: R_N is in E_3. The scaled norm follows because ∂^i [f] costs
λ^(−i) and Ω costs nothing, and the L² norm of an E_3 profile on A_P(τ) is at most C t^(−3/2). (E1) holds (W_TT and
χ dv dv are transverse to ℓ), and (E2) by stage 0. On Σ_τ0 ([[lem:past-domain]] (c)) the profiles' data determine, by
[[pending:lem-stage-system]] on Ω, solutions there; the two solve the same smooth linear system and agree on Σ_τ0 with
all their τ-derivatives, each fixed by the system from the data, so together they are smooth on P ∪ Ω. The stage system
is equivariant under T² × Z2 × Z2 and under S of [[lem:quarter-turn]], the condition of nothing coming in is invariant,
and the solutions are unique, so they are invariant. ∎

[[PART4-ANCHOR]]
