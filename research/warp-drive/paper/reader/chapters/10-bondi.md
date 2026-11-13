## Bondi coordinates and the mass law at past null infinity {#ch:bondi}

This chapter proves [[thm:bondi-law]]: the solution g_λ of [[thm:past-construction]] admits Bondi coordinates near past
null infinity, and in them its mass aspect obeys the five-dimensional Bondi law. The law is due to Tanabe, Tanahashi and
Shiromizu [TTS09]. We derive it again in the class at hand, with every coefficient general from the first order on, so
that nothing in the proof is taken from [TTS09] except the comparison. What has to be shown is that g_λ has the
asymptotic expansion at past null infinity which the law needs, in Bondi coordinates built on g_λ itself, and what the
law then gives.

The argument has four steps. At fixed λ the far region of [[thm:past-construction]] is a neighbourhood of past null
infinity, and there the remainder g_λ − g_app solves a wave equation whose forcing decays like r^(−3). First, every
derivative of the remainder obeys the bound which the construction gives for the first few
(Section [[sec:bondi-every-order]]). Second, subtracting the explicit leading term of the forcing and estimating the rest
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

We use the notation of Chapter 9 [[pending:ch9-decay-classes]]. X = (τ, x) ∈ R × R⁴, r = |x|, x̂ = x/r, v = τ + r and t
:= 1 + τ0 − τ; P is the past domain of [[thm:past-construction]], P+ := P ∩ {v ≥ v_start}, Σ_τ the slices of constant τ,
and ‖·‖ the flat L² norm on Σ_τ ∩ P+. The field ℓ := g0⁻¹ dv is null and tangent to the ingoing generators of the cones
{v = const}; ℓf := df(ℓ), and on P+ we use the coordinates (v, r, x̂), in which ℓ = ∂_r and ∂_v is the derivative at
fixed (r, x̂). Ω_ab := x_a ∂_b − x_b ∂_a are the rotations of R⁴, and □̃ := g0^{ab} ∂_a ∂_b acts on Cartesian
components. On S³ we use the polar angle ϑ ∈ [0, π/2] and the angles φ1, φ2 of the two rotation planes, the round metric
being γ = dϑ² + cos²ϑ dφ1² + sin²ϑ dφ2².

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
coframe (r dϑ, r cos ϑ dφ1, r sin ϑ dφ2) the components of [[eq:bondi-wave]] are r^(−3/2) times −2(p1 + p2), 2p1 and 2p2,
and the coframe has bounded Cartesian components with bounded derivatives along x̂; so G_3 is smooth and bounded with
all its derivatives, smooth at the axes [[pending:ch2-waves]], and zero for v ≤ v_start, where env vanishes. The
construction controls finitely many derivatives of u_1: with the regularity index 6, the far-region estimate and the
Sobolev inequality with rotations of Chapter 9 give ∂^i w ∈ E_2 for i ≤ 4, the higher norms bounded
[[pending:ch9-far-region]] [[pending:ch9-sobolev]]. The approximating solutions of the construction give every order at
fixed λ, uniformly; this is [[lem:every-order-fixed]], which the induction of Section [[sec:bondi-expansion]] consumes.

### Every order at fixed λ {#sec:bondi-every-order}

**Lemma {#lem:every-order-fixed}** (Every order at fixed λ.) Every Cartesian derivative ∂_X^α Ω^β u_1 is in E_2 on the
far region, with constants depending on λ and on the order.

Proof. Write g := g_λ = g0 + r^(−3/2) G_3 + u_1. By [[lem:bondi-equation-u]] below, u_1 = u − r^(−3/2) G_3 solves

    −½ g^{ab} ∂_a ∂_b u_1 = F_1 := S(u) − ½ (g^{ab} − g0^{ab}) ∂_a ∂_b u_1 + ½ □̃ (r^(−3/2) G_3).          {#eq:bondi-f1}

*The structure of F_1.* By the reduced equations [[pending:ch2-reduced-equations]], every Lorentzian g satisfies
Ric^H(g) = −½ g^{ab} ∂_a ∂_b g + Q(X; g)(∂g, ∂g), with Q a polynomial of degree two in ∂g whose coefficients are
rational in g and smooth in X through Γ[g0] and its first derivatives, and Ric^H(g0) = Ric(g0). Insert the definition
[[eq:bondi-s-def]] of S into [[eq:bondi-f1]], use ∂_a ∂_b (g0 + u) = ∂_a ∂_b (g0 + r^(−3/2) G_3) + ∂_a ∂_b u_1, and
replace Ric(g0) by −½ g0^{ab} ∂_a ∂_b g0 + Q(X; g0)(∂g0, ∂g0). The terms in g0 alone cancel, and

    F_1 = ½ g^{ab} ∂_a ∂_b (g0 + r^(−3/2) G_3) − Q(X; g)(∂g, ∂g)
        = −Ric^H(g) − ½ g^{ab} ∂_a ∂_b u_1,                                                         {#eq:bondi-f1-form}

an identity in u_1: it holds for every symmetric u_1 that keeps g Lorentzian, not only for the solution. So F_1 contains
no second derivative of u_1. It is a smooth function F_1(X, u_1, ∂u_1), and F_1(X, 0, 0) = −Ric^H(g0 + r^(−3/2) G_3)
is in E_3 with all its derivatives: at u_1 = 0 the terms of S are those of [[lem:bondi-equation-u]] in G_3 and g0, all
in E_3, and the third term of [[eq:bondi-f1]] is in E_(7/2), because by the decay calculus of Chapter 9
[[pending:ch9-decay-calculus]] □̃(r^(−p) F) = (3 − 2p) r^(−p−1) ∂_v F + E_(p+2), whose first term vanishes at p = 3/2.

Along g the partial derivatives of F_1 are as follows. The first is b := ∂F_1/∂(∂u_1). Only Q depends on ∂u_1, so b is
minus the derivative of Q(X; g)(∂g, ∂g) in ∂g. It is linear in ∂g = ∂g0 + ∂u, with coefficients rational in g and smooth
in X, and its part free of ∂g is built from Γ[g0], which is O(r^(−2)) like ∂g0. Since ∂u is in E_(3/2), b is in
E_(3/2). It is moreover of λ-order 0, that is, bounded by C t^(−3/2) with C independent of λ, because ∂u is. By the
two-scale chain rule ∂_a [f] = λ⁻¹ (∂_a v)[∂_θ f] + [∂_a f], the λ⁰ part of ∂(λ[W_TT]) is dv [∂_θ W_TT], in E_(3/2);
that of ∂(λ[χ dv dv]) is dv [∂_θ χ] dv dv, in E_2; that of the phase shift's term ∂(λ[W_TT(· + φ1)] − λ[W_TT]) is
dv ([∂_θ W_TT(· + φ1)] − [∂_θ W_TT]), at most |φ1| sup |∂_θ² W_TT| and so in E_1 E_(3/2) = E_(5/2), because φ1 is in L_1
[[thm:past-approximant]]; and every other term of ∂u is O(λ): the mean m1 does not oscillate, each later stage λ^j[g_j],
j ≥ 2, costs at most λ^(j−1), and ∂w is O(λ^(K−4) t^(−2)) by [[thm:past-construction]]. The second derivative is
c := ∂F_1/∂u_1. In the direction U, the derivative of g^{ab} is −(g⁻¹ U g⁻¹)^{ab}, so

    c U = −½ (g⁻¹ U g⁻¹)^{ab} ∂_a ∂_b (g0 + r^(−3/2) G_3) − (∂_g Q)(X; g)[U](∂g, ∂g).

The second term is O(r^(−2)|U|): it is quadratic in ∂g, or built from Γ[g0] and its derivatives, all O(r^(−2)) or
better. In the first, ∂_a ∂_b g0 = O(r^(−2)), and the chain rule gives

    ∂_a ∂_b (λ[W_TT]) = λ⁻¹ (∂_a v)(∂_b v)[∂_θ² W_TT] + (∂_a v)[∂_b ∂_θ W_TT] + (∂_b v)[∂_a ∂_θ W_TT] + λ[∂_a ∂_b W_TT].

Contracting with (g⁻¹ U g⁻¹)^{ab}, and writing ℓ_λ := g⁻¹ dv, the first term gives −½ λ⁻¹ U(ℓ_λ, ℓ_λ)[∂_θ² W_TT]. Since
the Cartesian components of W_TT are r^(−3/2) times smooth functions of (v, x̂, θ), ∂_b [∂_θ W_TT] =
(∂_b v)[∂_v ∂_θ W_TT] + E_(5/2), and the two middle terms give −U(ℓ_λ, ℓ_λ)[∂_v ∂_θ W_TT] + E_(5/2) U. Hence

    c = −½ λ⁻¹ (·)(ℓ_λ, ℓ_λ)[∂_θ² W_TT] + E_(3/2),                                                     {#eq:bondi-c}

whose E_(3/2) part contains −(·)(ℓ_λ, ℓ_λ)[∂_v ∂_θ W_TT], from the dependence of the envelope on v.

*The induction.* We induct on the order. Let |γ| = j + 1, and suppose the lemma holds for the orders up to j. By
Leibniz's rule U := ∂^γ u_1 solves

    −½ g^{ab} ∂_a ∂_b U = f_γ := b·∂U + c U + R_γ
                         + ½ Σ_{γ' ≤ γ, |γ'| = 1} C(γ, γ') (∂^{γ'} g^{ab}) ∂^{γ−γ'} ∂_a ∂_b u_1,

with C(γ, γ') := γ!/(γ'! (γ − γ')!), where

    R_γ := ∂^γ F_1 − b·∂U − c U + ½ Σ_{γ' ≤ γ, |γ'| ≥ 2} C(γ, γ') (∂^{γ'} g^{ab}) ∂^{γ−γ'} ∂_a ∂_b u_1

contains derivatives of u_1 of order at most j + 1 only. Indeed, by the chain rule the only term of ∂^γ[F_1(X, u_1,
∂u_1)] that contains a derivative of u_1 of order j + 2 is b·∂^γ ∂u_1 = b·∂U: every other term distributes the |γ|
derivatives over X or over at least two factors. The terms of the second sum carry ∂^{γ−γ'} ∂² u_1, of order at most
j + 1. In f_γ, the term b·∂U is of the order this step estimates and is not known; the terms with |γ'| = 1 are of the
form (∂g) ∂U' with ∂g in E_(3/2) and U' in the same family {∂^δ u_1 : |δ| = j + 1}; and c U is one order lower. They
enter through f_γ into the energy inequality of Chapter 9 [[pending:ch9-energy]], before Gronwall's lemma, not through
its kernel. Since U vanishes on {v = v_start}, the Poincaré inequality of [[pending:ch9-sobolev]] gives ‖U‖ ≤ C ‖∂U‖, so

    ‖b·∂U‖ ≤ C t^(−3/2) ‖∂U‖,       ‖c U‖ ≤ C λ⁻¹ t^(−3/2) ‖U‖ ≤ C λ⁻¹ t^(−3/2) ‖∂U‖,

and ‖f_γ‖ ≤ C (1 + λ⁻¹) t^(−3/2) Σ_{|δ| = j + 1} ‖∂ ∂^δ u_1‖ + ‖R_γ‖. Summed over the family, Gronwall's lemma then
costs the factor exp(∫ C (1 + λ⁻¹) t^(−3/2) dt). Over the far region t ≥ λ^(−2) this integral is at most 2 C (1 + λ⁻¹) λ
= 2 C (1 + λ), so the factor is at most e^(2C(1 + λ)), free of λ. (With c U taken as a forcing term, through the
energies of the lower steps, the step also closes at fixed λ, at the cost of one factor λ⁻¹ per order.)

R_γ is the sum of ∂_X^γ F_1(X, 0, 0), the forcing free of u_1, which is in E_3, and of products of a derivative of g or
of the coefficients of F_1, of order at most j + 1, with derivatives of u_1 of order at most j + 1. We estimate each
product in L²(Σ_τ), with the factor of higher order in L² (the energies of the lower steps, at most C t^(−1/2)) and the
others in the supremum norm (in E_2 by the induction hypothesis, through the Sobolev inequality with rotations
[[pending:ch9-sobolev]] for the orders it costs, and by the far-region bound [[pending:ch9-far-region]] for u_1^n,
below, at the lowest orders). The term ∂_X^γ F_1(X, 0, 0), in E_3, has L² norm at most C t^(−3/2) on Σ_τ ∩ P+, whose
volume is at most C t³; each product has L² norm at most C t^(−2), a coefficient in E_(3/2) or a second factor of u_1
in E_2 times the L² factor. So ‖R_γ‖ ≤ C(λ, j) t^(−3/2).

*The approximating solutions.* We do not apply the energy inequality on the region between {v = v_start} and Σ_τ: that
region is unbounded toward past null infinity [[pending:ch9-past-domain]], and the flux of ∂^γ u_1 through infinity there
is known to vanish only at the orders that [[thm:past-construction]] controls. We apply it instead to each
approximating solution g_n of the far-region construction [[pending:ch9-far-region]]. The metric g_n equals g0 on
{v ≤ v_start} and solves the same equations, so u_1^n := g_n − g0 − r^(−3/2) G_3 has the structure above:
[[lem:bondi-equation-u]] applies to it verbatim, with the far-region bound on g_n through the Sobolev inequality in
place of [[thm:past-construction]] at the lowest orders, uniformly in n. We use the region P ∩ {τ_n ≤ τ' ≤ τ}, where
the energy identity of the far-region bound itself holds. On Σ_(τ_n) the data of U_n := ∂^γ u_1^n are explicit:
w_n = g_n − g_app vanishes there with its first derivatives, its higher derivatives are those of the residual
Ric^H(g_app) of the approximant through the equation, and g_app − g0 − r^(−3/2) G_3 is explicit with all its
derivatives [[pending:ch9-decay-calculus]]. So ‖∂U_n(τ_n)‖ ≤ C(λ, j) t_n^(−1/2), with t_n ≥ t.

Let f_γ^n, b^n, c^n and R_γ^n be f_γ, b, c and R_γ with g_n and u_1^n in place of g_λ and u_1. Since
[[lem:bondi-equation-u]] applies to u_1^n verbatim, b^n and c^n obey the bounds on b and c above with the same constants.
Moreover ‖R_γ^n‖ ≤ C(λ, j) t^(−3/2) uniformly in n: ∂_X^γ F_1(X, 0, 0) does not depend on n, and every other factor of
R_γ^n is bounded by the induction hypothesis for u_1^n, which is uniform in n, with the far-region bound at the lowest
orders. The energy inequality [[pending:ch9-energy]] for U_n with forcing f_γ^n, summed over the family, and Gronwall's
lemma give

    Σ_{|γ| = j + 1} ‖∂U_n(τ)‖ ≤ C e^(2C(1 + λ)) Σ_{|γ| = j + 1} ( ‖∂U_n(τ_n)‖ + ∫_{τ_n}^{τ} ‖R_γ^n‖ dτ' ).

Since ‖∂U_n(τ_n)‖ ≤ C(λ, j) t_n^(−1/2) ≤ C(λ, j) t^(−1/2) and ∫_{τ_n}^{τ} t'^(−3/2) dτ' ≤ 2 t^(−1/2), we obtain
‖∂U_n(τ)‖ ≤ C(λ, j) t^(−1/2) at every order, uniformly in n.

*Supremum norm against L².* The bookkeeping closes at every order |γ|: the factor taken in the supremum norm has order at
most ⌊(|γ| + 2)/2⌋, the class E_2 is in hand pointwise to the order max(4, |γ| − 3) (the far-region bound with the
Sobolev inequality, for u_1^n, at the lowest orders, and the Sobolev inequality applied to the energies of the lower
steps for the rest, at the cost of three orders), and ⌊(|γ| + 2)/2⌋ ≤ max(4, |γ| − 3) for every |γ| ≥ 1. The Sobolev
inequality turns the energies of the next three orders into |∂^γ u_1^n| ≤ C(λ, j) t^(−3/2) t^(−1/2) = C(λ, j) t^(−2),
uniformly in n. Rotations Ω^β among the derivatives are treated the same way, with the rotation energies in the
Sobolev inequality and the commutator [Ω, g_n^{ab} ∂_a ∂_b] absorbed as in the far-region estimate
[[pending:ch9-far-region]]. For a pure rotation γ the Leibniz term of R_γ with |γ'| = |γ| has the L² factor
‖Ω^γ u_1^n‖, which the energies of the lower steps bound only by C t^(1/2), since |Ω f| ≤ 2 r |∂f|; that product is then
C t^(−3/2), so ‖R_γ‖ ≤ C(λ, j) t^(−3/2) still holds; alternatively the term can enter the Gronwall family through the
Poincaré inequality, with kernel t^(−2). The remark on c U taken as a forcing term concerns Cartesian γ.

*The limit.* The bounds pass to the limit. By the proof of [[thm:past-construction]], g_n → g_λ with k − 5
derivatives on compact sets [[pending:ch9-proof-of-past-construction]], and the higher derivatives of u_1^n are bounded
uniformly in n on each compact set. By the Arzelà–Ascoli theorem a subsequence converges in every C^j, its limit is
∂^γ u_1, and the bound is inherited: ∂^γ u_1 is in E_2. ∎

**Lemma {#lem:bondi-equation-u}** (The equation for u.) On P, −½ □̃ u = S(u) with

    S(u) := −Ric(g0) + ½ (g_λ^{ab} − g0^{ab}) ∂_a ∂_b (g0 + u)
            − [ Q(X; g0 + u)(∂g0 + ∂u, ∂g0 + ∂u) − Q(X; g0)(∂g0, ∂g0) ],                             {#eq:bondi-s-def}

and S(u) is in E_3. The terms of S have the following classes: Ric(g0) = (3μ'/(2r³)) dv dv exactly
[[pending:ch2-vaidya-ricci]]; g_λ⁻¹ − g0⁻¹ is in E_(3/2), ∂²g0 = O(r^(−2)) and ∂²u is in E_(3/2); and the difference of
the Q terms is quadratic in ∂u (in E_3) plus Γ[g0] times ∂u (in E_2 E_(3/2)).

Proof. Ric^H(g_λ) = 0 and Ric^H(g0) = Ric(g0) [[pending:ch2-reduced-equations]]; subtract the two, using the form
Ric^H(g) = −½ g^{ab} ∂_a ∂_b g + Q(X; g)(∂g, ∂g) for both. The classes are those of the count in the proof of
[[thm:past-approximant]], with ∂^i u in E_(3/2) at fixed λ for the orders that [[lem:every-order-fixed]] controls; that
lemma supplies them in turn, order by order. ∎

### The half-order gain and the expansion in r^(−1/2) {#sec:bondi-expansion}

**Lemma {#lem:bondi-half-order}** (One half-order.) Let q ∈ {3, 7/2, 4, …}, and let ũ be a symmetric tensor on the far
region, vanishing for v ≤ v_start, with every Cartesian derivative ∂_X^α Ω^β ũ in E_(q−1), solving

    −½ g_λ^{ab} ∂_a ∂_b ũ = r^(−q) S_q + S̃,       S̃ ∈ E_(q+1/2) with all derivatives,                  {#eq:bondi-half}

with S_q(v, x̂) smooth, bounded with all derivatives and vanishing for v ≤ v_start. Put
Y_q(v, x̂) := (2/(2q − 5)) ∫_{v_start}^{v} S_q dv'. Then ũ = r^(1−q) Y_q + ǔ with every Cartesian derivative of ǔ in
E_(q−1/2). If moreover, for some m ≥ 1 and every j < m,

    (H_m)    ℓ^j S̃ ∈ E_(q+1/2+j)   and   ℓ^j (g_λ − g0) ∈ E_(3/2+j),   each with all derivatives,

then ℓ^m ǔ is in E_(q−1/2+m) with all derivatives.

Proof. By the decay calculus [[pending:ch9-decay-calculus]], −½ □̃(r^(1−q) Y_q) = −½ (3 − 2(q − 1)) r^(−q) ∂_v Y_q +
E_(q+1) = r^(−q) S_q + E_(q+1), and (g_λ⁻¹ − g0⁻¹) ∂²(r^(1−q) Y_q) is in E_(3/2) E_(q−1) = E_(q+1/2). So
ǔ := ũ − r^(1−q) Y_q solves −½ g_λ^{ab} ∂_a ∂_b ǔ = S′ with S′ in E_(q+1/2) with all derivatives, vanishes for
v ≤ v_start, and has every derivative in E_(q−1).

*Energy.* The L² norm of an element of E_p on Σ_τ ∩ P+ is at most C t^(3/2 − p), the volume being at most C t³. Apply
the energy inequality of Chapter 9 [[pending:ch9-energy]] with the metric g_λ, which has the margin required there on P
by [[thm:past-construction]] [[pending:ch9-past-domain]] and satisfies ‖∂g_λ‖_∞ ≤ C t^(−3/2) on P+, an integrable
kernel, and with forcing S′, from τ1 → −∞. Since ‖∂ǔ(τ1)‖ ≤ C t1^(3/2 − (q−1)) → 0 because q > 5/2, and
‖S′(τ')‖ ≤ C t'^(3/2 − q − 1/2) = C t'^(1−q), we get ‖∂ǔ(τ)‖ ≤ C ∫_{−∞}^{τ} t'^(1−q) dτ' = C t^(2−q)/(q − 2).
Commuting with ∂_X and Ω preserves the form of the equation. [∂_X, g_λ^{ab} ∂_a ∂_b] = (∂_X g_λ^{ab}) ∂_a ∂_b with
∂_X g_λ^{ab} in E_(3/2) produces a forcing in E_(q+1/2), by the hypothesis on ǔ (its second derivatives are in
E_(q−1)), within the bound t^(1−q) of S′. And [Ω, □̃] = 0: the rotations are linear maps of R⁴ that preserve g0, and for
such a map R, □̃(f ∘ R) = (□̃ f) ∘ R. So every commuted energy is at most C t^(2−q). *Pointwise.* The Sobolev inequality
with rotations and the Poincaré inequality (ǔ = 0 on {v = v_start}) [[pending:ch9-sobolev]] give
|∂_X^α Ω^β ǔ| ≤ C t^(−3/2) t^(2−q) = C t^(1/2 − q). That is E_(q−1/2), since t and r are comparable on P+.

*The ℓ-gain.* In the coordinates (v, r, x̂) the operator □̃ reads [[pending:ch9-decay-calculus]]

    □̃ f = 2 ∂_v ℓ f + (3/r) ∂_v f + (1 − μ/r²) ℓ ℓ f + (3/r) ℓ f + r^(−2) Δ̊ f,                       {#eq:bondi-box-vr}

with Δ̊ the Laplacian of the unit S³. With ψ := ℓǔ (ℓ acting on Cartesian components) the equation of ǔ becomes

    2 ∂_v ψ + (1 − μ/r²) ℓ ψ + (3/r) ψ = −2 S′ − (3/r) ∂_v ǔ − r^(−2) Δ̊ ǔ − (g_λ^{ab} − g0^{ab}) ∂_a ∂_b ǔ =: f,
                                                                                                    {#eq:bondi-transport}

with f in E_(q+1/2): its terms are in E_(q+1/2), E_(q+1/2), E_(q+3/2) and E_(3/2) E_(q−1/2). The operator
L₊ := 2 ∂_v + (1 − μ/r²) ℓ is the outgoing null direction of g0: in (v, r), L₊ = 2 ∂_v + (1 − μ/r²) ∂_r, while
g0⁻¹(dv, dv) = 0, g0⁻¹(dv, dr) = 1 and g0⁻¹(dr, dr) = 1 − μ/r², so g0(L₊, L₊) = −4 (1 − μ/r²) + 4 (1 − μ/r²) = 0. So
[[eq:bondi-transport]] is a transport along the outgoing generators. Along one of them, parametrised by σ, dv/dσ = 2 and
dr/dσ = 1 − μ/r² ∈ (0, 1]. From a point (v, r) the generator therefore reaches {v = v_start}, where ψ = 0, after a
parameter length (v − v_start)/2 ≤ d1/2 [[pending:ch9-past-domain]], at a radius r' ∈ [r − d1/2, r]. Integrating
(L₊ + 3/r) ψ = f along it gives |ψ(v, r)| ≤ e^(3 d1/(2 r')) (d1/2) sup |f| ≤ C r^(−q−1/2), the supremum taken over the
segment, which lies in the far region once r is large.

Derivatives commute through [[eq:bondi-transport]] up to terms of the same kind. Ω commutes with L₊ and with 3/r, since
it annihilates v, r and μ(v); so Ω^b ψ solves [[eq:bondi-transport]] with the forcing Ω^b f. ∂_v commutes up to [∂_v,
L₊] = −(μ'/r²) ℓ, and ℓψ is read off [[eq:bondi-transport]] itself, (1 − μ/r²) ℓψ = f − 2 ∂_v ψ − (3/r) ψ. So ∂_v^a Ω^b
ψ solves [[eq:bondi-transport]] with a term of order zero, O(r^(−2)) times ∂_v^a Ω^b ψ, moved to the left (over a
parameter length at most d1/2 it changes the integrating factor by a bounded factor), and a forcing in E_(q+1/2) by the
lower a. The ℓ-components of the derivatives of ψ are then read off [[eq:bondi-transport]] in the same way: ℓ^c ∂_v^a
Ω^b ψ is in E_(q+1/2) by induction on c, and every Cartesian derivative is a combination of ℓ, ∂_v and r⁻¹ Ω with
coefficients bounded with all their derivatives. So ℓǔ is in E_(q+1/2) with all derivatives. This is the case m = 1,
which needs nothing of (H_m), since f contains no ℓ-derivative of S′ or of g_λ.

For m ≥ 2, under (H_m), the equation of ℓ^m ǔ = ℓ^(m−1) ψ is [[eq:bondi-transport]] commuted m − 1 times with ℓ. Its
forcing is ℓ^(m−1) f plus the commutators [ℓ, L₊] = (2μ/r³) ℓ, [ℓ, 3/r] = −3/r² and
[ℓ, (g_λ^{ab} − g0^{ab}) ∂_a ∂_b] = (ℓ (g_λ − g0)^{ab}) ∂_a ∂_b applied to the lower ℓ^j ǔ, with one exception:
[ℓ^(m−1), L₊] ψ = 2 (m − 1)(μ/r³) ℓ^m ǔ plus terms in ℓ^j ǔ with j < m contains the unknown itself, not a lower term.
It is moved to the left, and the transport becomes (L₊ + 3/r + 2 (m − 1) μ/r³) ℓ^(m−1) ψ = (the rest), whose O(r^(−3))
coefficient changes the integrating factor by a bounded factor. Each term of ℓ^(m−1) f is in E_(q+1/2+m−1): ℓ^j S′ by
(H_m) (S′ is S̃ plus (g_λ⁻¹ − g0⁻¹) ∂²(r^(1−q) Y_q) and □̃(r^(1−q) Y_q) − r^(−q) S_q, whose ℓ-derivatives gain by
(H_m) and explicitly), ℓ^j of (3/r) ∂_v ǔ and of r^(−2) Δ̊ ǔ by the gains already established for j < m, and
(ℓ^j (g_λ − g0)^{ab}) ∂² ℓ^(m−1−j) ǔ by (H_m) with those gains, E_(3/2+j) E_(q−1/2+m−1−j) = E_(q+m). The commutator terms
are of the same kind. So the transport gives ℓ^m ǔ in E_(q−1/2+m), and derivatives commute as before. ∎

**Proposition {#prop:bondi-hierarchy}** (The expansion in r^(−1/2).) For every J ≥ 3 there are smooth tensors G_k(v, x̂),
k = 3, …, J, bounded with all derivatives, vanishing for v ≤ v_start and invariant under T² × Z2 × Z2, with G_3 as in
[[eq:bondi-u-split]], such that on the far region

    u = Σ_{k=3}^{J} r^(−k/2) G_k + u_J,     ∂_X^α Ω^β ℓ^m u_J ∈ E_((J+1)/2 + m) for all α, β, m.  {#eq:bondi-expansion}

The G_k are determined inductively: G_k = (2/(k − 3)) ∫_{v_start}^{v} S_(k/2+1) dv' for k ≥ 4 (so G_4 = 2 ∫ S_3), where
r^(−q) S_q is the leading term of the forcing once the terms below it are known.

Proof. We induct on J with [[lem:bondi-half-order]]. For J = 3, u_3 := u_1 is in E_2 with all derivatives by
[[lem:every-order-fixed]], and by [[lem:bondi-equation-u]] it solves
−½ g_λ^{ab} ∂_a ∂_b u_3 = S(u) − ½ (g_λ^{ab} − g0^{ab}) ∂_a ∂_b u_3 + ½ □̃(r^(−3/2) G_3) =: F_1. The second term is in
E_(7/2) (E_(3/2) E_2), the third in E_(7/2) [[pending:ch9-decay-calculus]], and S(u) is in E_3 with a leading term
r^(−3) determined by G_3 alone: −(3μ'/2) dv dv from Ric(g0), plus the terms of [[eq:bondi-s-def]] quadratic in
∂(r^(−3/2) G_3) or of the form (r^(−3/2) G_3) ∂²(g0 + r^(−3/2) G_3), since every term containing u_3 is in E_(7/2)
(E_(3/2) E_2, or Γ[g0] times E_2). So [[eq:bondi-half]] holds at q = 3, and [[lem:bondi-half-order]] gives
u = r^(−3/2) G_3 + r^(−2) G_4 + u_4 with every derivative of u_4 in E_(5/2).

*The ℓ-gains at J = 3, by induction on m.* The case m = 1 needs no hypothesis: ℓu_4 is in E_3, hence
ℓu_1 = ℓ(r^(−2) G_4) + ℓu_4 is in E_3 and ℓ(g_λ − g0) = ℓ(r^(−3/2) G_3) + ℓu_1 is in E_(5/2), with all derivatives.
Suppose ℓ^j u_4 is in E_(5/2+j) for j < m. Then ℓ^j (g_λ − g0) is in E_(3/2+j) for j < m, and ℓ^j S̃ is in E_(7/2+j):
S̃ = F_1 − r^(−3) S_3 is a polynomial in g0, g_λ⁻¹, u, ∂u and ∂²u each of whose terms either is explicit (the terms in
G_3 and g0, whose ℓ-derivatives gain an order each because r^(−k) and the profiles do) or contains u_1 or a derivative
of it, on which ℓ^j gains j orders by the hypothesis, the other factors keeping their classes. So (H_m) holds, and
[[lem:bondi-half-order]] gives ℓ^m u_4 in E_(5/2+m): [[eq:bondi-expansion]] at J = 4.

*Stage J ≥ 4.* The remainder u_J has every ℓ-gain. So the forcing of u_J, a polynomial in (u, ∂u, ∂²u) with
coefficients smooth in (X, g) whose arguments are expanded to the previous order with remainders in E_((J+1)/2), has
the form r^(−q) S_q + S̃ with q = (J + 3)/2 and S̃ satisfying (H_m) for every m: every product with a remainder factor is
in E_(3/2 + (J+1)/2) = E_(q+1/2) or better and gains under ℓ. So the coefficient of r^(−q) is a polynomial in the G_k,
k ≤ J, and their derivatives, and [[lem:bondi-half-order]] applies at every m. The invariance and the vanishing for
v ≤ v_start are inherited by the integrals from v_start. ∎

**Remark {#rem:bondi-lambda}** The coefficients from G_4 on depend on λ, through the phase v/λ and the powers of λ of the
profiles, and [[prop:bondi-hierarchy]] claims nothing uniform in λ. It is an asymptotic statement at past null infinity
at each fixed λ, which is all the mass law needs.

### Bondi coordinates at past null infinity {#sec:bondi-chart}

**Lemma {#lem:bondi-ell}** (The ℓ-components.) G_3(ℓ, ·) = 0 and tr G_3 = 0. Hence u(ℓ, ·) is in E_2, the trace tr_S u
on the spheres S_(v,r) is in E_2, g_λ^{vv} = −u(ℓ, ℓ) + E_3 is in E_2, and (g_λ⁻¹ − g0⁻¹)(dv, ·) = −g0⁻¹ u(ℓ, ·) + E_3
is in E_2.

Proof. By [[eq:bondi-wave]] the wave λW_TT has no dv or dr component and is traceless on the spheres
[[pending:ch2-waves]], so G_3(ℓ, ·) = 0 and tr G_3 = tr_S G_3 = 0; the rest of u is u_1, in E_2. Then
g⁻¹ = g0⁻¹ − g0⁻¹ u g0⁻¹ + O(u²) and g0⁻¹ dv = ℓ. ∎

We write the coordinate components of the G_k in the basis of (v, r, ϑ) as scalar coefficients,

    u_rr = Σ_k s^k C_k,   u_vr = Σ_k s^k B_k,   u_vv = Σ_k s^k A_k,   u_(rϑ) = r Σ_k s^k E_k,   u_(vϑ) = r Σ_k s^k D_k,
    u_(ϑϑ) = r² Σ_k s^k F_k,   u_(φ1φ1) = r² cos²ϑ Σ_k s^k G_k,   u_(φ2φ2) = r² sin²ϑ Σ_k s^k H_k,     {#eq:bondi-coeffs}

with s := r^(−1/2) and one power of r for each angular index, the classes being of orthonormal components. These
A_k, …, H_k are scalar functions of (v, ϑ), the subscript being the power of s; they are not the classes E_p, the
tensors G_k of [[eq:bondi-expansion]] or the free data F, G. By [[lem:bondi-ell]], A_3 = B_3 = C_3 = D_3 = E_3 = 0 and
F_3 + G_3 + H_3 = 0, and by [[eq:bondi-wave]], F_3 = −2(p1 + p2), G_3 = 2p1 and H_3 = 2p2. The other components of u
vanish, by the reflections φ1 ↦ −φ1 and φ2 ↦ −φ2.

**Proposition {#prop:bondi-chart}** (The Bondi chart.) There is T_M(λ) such that on the far region P ∩ {t ≥ T_M} the
functions

    v_B := v + ů,      ϑ_B := ϑ + ν,      r_B := r (1 + ρ)

exist with the following properties. (i) g_λ⁻¹(dv_B, dv_B) = 0, and ů → 0 along every generator of g0 as r → ∞.
(ii) g_λ⁻¹(dv_B, dϑ_B) = 0, and ν → 0 likewise. (iii) r_B is the areal radius: r_B⁶ cos²ϑ_B sin²ϑ_B is the determinant
of the metric induced on {v_B, r_B = const} in the coordinates (ϑ_B, φ1, φ2). (iv) They are invariant under
T² × Z2 × Z2 and equal (v, ϑ, r) for v ≤ v_start. With u expanded to order J by [[eq:bondi-expansion]], they have
expansions in s with coefficients smooth in (v, ϑ) and vanishing for v ≤ v_start,

    ů = Σ_{k=2}^{J−2} s^k ů_k + E_((J−1)/2),     ν = Σ_{k=4}^{J−2} s^k ν_k + E_((J−1)/2),
    ρ = Σ_{k=4}^{J−2} s^k ρ_k + E_((J−1)/2),                                                       {#eq:bondi-shifts}

whose first coefficients are

    ů_2 = −C_4/2,   ů_3 = −C_5/3,   ů_4 = −C_6/4 + C_4 ∂_v C_4/8,   ν_4 = −E_4/2 − ∂_ϑ C_4/4,
    ρ_4 = (F_4 + G_4 + H_4)/6 − (1/3) div(ν_4),       div f := (sin ϑ cos ϑ)⁻¹ ∂_ϑ (f sin ϑ cos ϑ),     {#eq:bondi-first}

and whose remainders gain an order under ℓ. In the chart (v_B, r_B, ϑ_B, φ1, φ2) the metric has the form

    g_λ = −e^(2b) W dv_B² + 2 e^(2b) dv_B dr_B
          + r_B² [ e^(−2(P1+P2)) (dϑ_B − U dv_B)² + cos²ϑ_B e^(2P1) dφ1² + sin²ϑ_B e^(2P2) dφ2² ],     {#eq:bondi-metric}

its functions being given by the inverse components g^{v_B r_B} = e^(−2b), g^{r_B r_B} = e^(−2b) W,
g^{r_B ϑ_B} = e^(−2b) U, g^{ϑ_B ϑ_B} = 1/(r_B² S) with S := e^(−2(P1+P2)), g^{φ1 φ1} = 1/(r_B² cos²ϑ_B e^(2P1)) and
g^{φ2 φ2} = 1/(r_B² sin²ϑ_B e^(2P2)). The functions b, W, U, P1, P2 have expansions in s_B := r_B^(−1/2) with
coefficients smooth in (v_B, ϑ_B), equal to those of g0 for v_B ≤ v_start (zero there, but for W − 1 = −μ0 s_B⁴), to
order s_B^(J−2), with remainders o(s_B^(J−2)) whose r_B-derivatives gain an order each. Their first coefficients are

    e^(2P1) = 1 + 2 p1 s_B³ + O(s_B⁴),    e^(2P2) = 1 + 2 p2 s_B³ + O(s_B⁴),
    e^(−2b) = 1 − (∂_v C_4/2) s_B² − (∂_v C_5/3) s_B³ + O(s_B⁴).                                 {#eq:bondi-first-metric}

Proof. *(i) The null coordinate.* Write L := g_λ⁻¹ dv = ℓ + ε with ε := (g_λ⁻¹ − g0⁻¹)(dv, ·), in E_2 by
[[lem:bondi-ell]]. Since g_λ⁻¹(dv + dů, dv + dů) = g_λ^{vv} + 2 L(dů) + g_λ⁻¹(dů, dů), condition (i) is the eikonal
equation

    2 ℓ ů = −g_λ^{vv} − 2 ε(dů) − g_λ⁻¹(dů, dů) =: N[ů].                                             {#eq:bondi-eikonal}

We build v_B by characteristics, not by iterating [[eq:bondi-eikonal]]: an iteration in a norm of ů and ℓů loses a
derivative at each step through the term ε(dů). In g0 the generators of {v = v0} are the affinely parametrised null
geodesics y0(r) = (v0, r, x̂0), with ℓ = ∂_r their tangent and Γ[g0]^a_rr = 0. For each (v0, x̂0) let y be the null
geodesic of g_λ asymptotic to y0: y(r) = (v0 + ζ(r), r, x̂0 + ξ(r)), parametrised by r, solving
d²y^a/dr² + Γ[g_λ]^a_bc y'^b y'^c = κ_y y'^a with κ_y fixed by the r-component (y^r = r), and with ζ, ζ', ξ, ξ' → 0 as
r → ∞. Writing y' = ∂_r + η, the system is

    η' = −(Γ[g_λ] − Γ[g0])^a_rr − 2 Γ[g_λ]^a_rb η^b − Γ^a_bc η^b η^c + κ_y y'^a,

a Volterra system from r = ∞. Its forcing (Γ[g_λ] − Γ[g0])^v_rr = ½ g^{vd}(2 ∂_r u_(dr) − ∂_d u_rr) is in E_3 by
[[lem:bondi-ell]] and the ℓ-gain of u (g^{vr} = 1 + E_(3/2) multiplies ∂_r u_rr, in E_3; g^{vv}, in E_2, multiplies
E_2; and g^{vϑ} r⁻¹ is in E_3). Its angular forcing is in E_4 (g^{ϑϑ} = r^(−2)(1 + E_(3/2)) times
∂_r u_(ϑr) = r ∂_r u(e_ϑ, ℓ) + u(e_ϑ, ℓ), in E_2). Its linear part −2 Γ[g0]^a_rb η^b vanishes for a = v
(Γ[g0]^v_rb = 0 in the ingoing chart) and is −(2/r) ξ' for a = ϑ (Γ[g0]^ϑ_rϑ = 1/r). This is not an integrable
perturbation but the unperturbed operator of the angular equation, ξ'' + (2/r) ξ' = E_4, which the integrating factor r²
solves with ξ' in E_3 and ξ in E_2. The remaining coefficients are Lipschitz in (ζ, ξ, ζ', ξ') in the weighted norms
below, with constants integrable in r: ∂(Γ[g_λ] − Γ[g0]) is in E_(3/2), and the terms quadratic in η, whose largest
coefficient is Γ[g0]^v_ϑϑ = −r, are O(r^(−2)) times the norm. κ_y = Γ^r_bc y'^b y'^c is in E_2 and multiplies η. So
for r ≥ T_M the Picard iteration converges in the weighted supremum norm r² |ζ'| + r |ζ| + r³ |ξ'| + r² |ξ| (a
contraction for an ordinary differential equation, so no derivative is lost). The solution depends smoothly on
(v0, x̂0), with derivatives of the same decay (the variational equations have the same structure), it is invariant, and
it is y0 for v0 ≤ v_start (there g_λ = g0 along the whole generator).

Each generator stays in P outward, so the system is posed where g_λ is defined. Along y,
d/dr (v + h(τ)) = ζ'(1 + h') − h', with τ = v − r (so dτ/dr = ζ' − 1) and h' = dh/dτ = h/(4t), a positive multiple
of t^(−5/4) [[pending:ch9-past-domain]]. Moreover |ζ'| ≤ C r^(−2) < h'/2 and h' < 1 once T_M is large, t and r being
comparable on P+. So v + h decreases outward along each generator while t increases, and the ray of a generator from a
point of P ∩ {t ≥ T_M} out to past null infinity lies in P ∩ {t ≥ T_M} and never meets the outer boundary
{v + h(τ) = V_P}. (To solve for every (v0, x̂0) at once, continue g_λ − g0 across that boundary by a Seeley extension in
v + h(τ), which keeps every class E_p; by this monotonicity neither the generator through a point of P ∩ {t ≥ T_M} nor
Φ⁻¹ there depends on the continuation, so Φ⁻¹, below, is defined on all of P ∩ {t ≥ T_M}.)

The map Φ: (v0, r, x̂0) ↦ y(r) is then a C¹-small perturbation of the identity for r ≥ T_M, a diffeomorphism onto a
neighbourhood of past null infinity, and N_(v0) := Φ({v0} × [T_M, ∞) × S³) is a null hypersurface. Indeed, along each y,
d/dr g_λ(y', y') = 2 κ_y g_λ(y', y'), so g_λ(y', y') e^(−2∫κ_y) is constant and equal to its limit g0(ℓ, ℓ) = 0 at
infinity (y is null). And for each Jacobi field X = ∂_(x̂0) y of the congruence, tangent to N_(v0) as y' is, d/dr
g_λ(y', X) = κ_y g_λ(y', X) + g_λ(y', ∇_X y') = κ_y g_λ(y', X) + ½ X g_λ(y', y') = κ_y g_λ(y', X), so g_λ(y', X)
e^(−∫κ_y) is constant along y and equal to its limit at infinity, which is 0: g_λ(y', X) = ∂_(x̂0) ζ + r² ξ' (1 +
∂_(x̂0) ξ) + r u(ℓ, e_ϑ) + smaller terms, with ∂_(x̂0) ζ, r² ξ' and r u(ℓ, e_ϑ) in E_1. (The transverse field ∂_(v0) y
is not needed, and it is not orthogonal to y': g0(ℓ, ∂_v) = 1.) Hence y' is normal to N_(v0), which is null. Put v_B :=
v0 ∘ Φ⁻¹, so that g_λ⁻¹(dv_B, dv_B) = 0, and ů := v_B − v = −ζ ∘ Φ⁻¹. Then ů is in E_1, with ℓů in E_2 (ℓů = −ζ' up to
Jacobian corrections in E_2) and all derivatives; it vanishes for v ≤ v_start and is invariant.

*Expansion of ů.* v_B satisfies [[eq:bondi-eikonal]] exactly, so ů = −½ ∫_r^∞ N[ů] dr' along the generators of g0. Insert
[[eq:bondi-expansion]]. The integrals of the powers of s are powers of s, the nonlinear terms at order s^(k+2) involve
only ů_j with j < k, and the remainder of ů is the integral along the generator of a remainder, with ℓ of it the
integrand: this gives [[eq:bondi-shifts]] for ů. Since ∂_r s^k = −(k/2) s^(k+2), the s^(k+2) coefficient of the left side
2∂_r ů is −k ů_k, so the s^(k+2) coefficient of the equation is −k ů_k plus known terms. The first ones are found as
follows. In the coordinates (v, r, ϑ), ℓ = ∂_r, g0^{vv} = 0, g0^{vr} = 1, g0^{rr} = 1 − μ/r² and g0^{ϑϑ} = r^(−2).
Expanding g⁻¹ = g0⁻¹ − g0⁻¹ u g0⁻¹ + g0⁻¹ u g0⁻¹ u g0⁻¹ − …, the term quadratic in u of g^{vv} is
g0⁻¹(u(ℓ, ·), u(ℓ, ·)), built from u_rr, u_rv = O(s⁴) and r⁻¹ u_(rϑ) = O(s⁴), so it is O(s⁸), and
−g_λ^{vv} = C_4 s⁴ + C_5 s⁵ + C_6 s⁶ + O(s⁷). The components of ε are ε^v = −u_rr, ε^r = −u_rv − (1 − μ/r²) u_rr and
ε^ϑ = −r^(−2) u_(rϑ), up to terms quadratic in u; with ů = O(s²), ∂_v ů = O(s²) and ∂_r ů = O(s⁴),
2 ε(dů) = −2 C_4 ∂_v ů_2 s⁶ + O(s⁷), and g_λ⁻¹(dů, dů) = 2 ∂_v ů ∂_r ů + O(s⁸) = −2 ů_2 ∂_v ů_2 s⁶ + O(s⁷). So

    N[ů] = C_4 s⁴ + C_5 s⁵ + (C_6 + 2 C_4 ∂_v ů_2 + 2 ů_2 ∂_v ů_2) s⁶ + O(s⁷),

and comparing with −Σ_k k ů_k s^(k+2): ů_1 = 0, −2 ů_2 = C_4, −3 ů_3 = C_5, and
−4 ů_4 = C_6 + 2 C_4 ∂_v ů_2 + 2 ů_2 ∂_v ů_2 = C_6 − C_4 ∂_v C_4 + ½ C_4 ∂_v C_4 = C_6 − ½ C_4 ∂_v C_4. These are the
values in [[eq:bondi-first]].

*(ii) The angular coordinate.* ϑ_B := x̂0 ∘ Φ⁻¹ (the angle of the generator of g0 to which y is asymptotic) is constant
along the generators of N_(v0), whose tangent is L_B := g_λ⁻¹ dv_B up to a factor (y' is the null normal of N_(v0)). So
L_B ϑ_B = 0, which is (ii), and ν = ϑ_B − ϑ = −ξ ∘ Φ⁻¹ is in E_2 with ℓν in E_3. With L_B = ℓ + ε + g_λ⁻¹ dů, the
transport L_B ϑ_B = 0 reads

    2 ℓ ν = −2 ε(dϑ) − 2 g_λ⁻¹(dů, dϑ) − 2 (ε + g_λ⁻¹ dů)(dν),

where ε(dϑ) = −r^(−2) u(∂_ϑ, ℓ) + E_4 = −r⁻¹ u(e_ϑ, ℓ) + E_4 is in E_3 (e_ϑ := r⁻¹ ∂_ϑ) and
g_λ⁻¹(dů, dϑ) = r^(−2) ∂_ϑ ů + E_4 is in E_3. So ν expands as in [[eq:bondi-shifts]], the s^(k+2) coefficient of the
equation being −k ν_k plus known terms. In terms of the coefficients, −2 ε(dϑ) = 2 Σ_k E_k s^(k+2) + O(s⁸),
−2 g_λ⁻¹(dů, dϑ) = −2 ∂_ϑ ů_2 s⁶ + O(s⁷), and the last term is O(s⁸), since ν = O(s⁴), ε = O(s⁴) and dů = O(s²). As
E_k = 0 for k ≤ 3 and ů_1 = 0, the coefficients ν_1, ν_2, ν_3 vanish, and at s⁶, −4 ν_4 = 2 E_4 − 2 ∂_ϑ ů_2 =
2 E_4 + ∂_ϑ C_4: the value in [[eq:bondi-first]].

*(iii) The areal radius.* Let J0 be the Jacobian of (v, s, ϑ) ↦ (v_B, r_B, ϑ_B). In a chart with
g^{v_B v_B} = g^{v_B ϑ_B} = 0 the covariant metric has g_(r_B r_B) = g_(r_B ϑ_B) = 0, so it has the form
[[eq:bondi-metric]] once r_B is areal, and its inverse determinant is −e^(−4b)/(r_B⁶ cos²ϑ_B sin²ϑ_B) with
e^(−2b) = g^{v_B r_B}; the inverse determinant transforms with (det J0)². So the areal condition is the equation

    r_B⁶ cos²ϑ_B sin²ϑ_B det(g_λ⁻¹) (det J0)² + (g^{v_B r_B})² = 0,                                 {#eq:bondi-areal}

whose s^k coefficient is 6 ρ_k plus known terms. The factor ∂_r r_B = 1 + ρ + r ∂_r ρ of (det J0)² cancels against
the same factor of (g^{v_B r_B})² = (g_λ⁻¹(dv_B, dr_B))², and exactly, not only at this order. With
g^{v_B v_B} = g^{v_B ϑ_B} = 0 the inverse determinant in the chart is −(g^{v_B r_B})²/det q, q the metric induced on
{v_B, r_B = const} in (ϑ_B, φ1, φ2), so [[eq:bondi-areal]] is (g^{v_B r_B})² (1 − r_B⁶ cos²ϑ_B sin²ϑ_B/det q) = 0. And q,
induced on a cross-section of the null hypersurface {v_B = const} in coordinates constant along its generators, has no
component along them, so it depends on the points of the cross-section and not on its tilt: no derivative of ρ enters,
and r_B⁶ contributes 6 ρ_k (the leading determinant being 1). The condition is therefore algebraic in ρ and solvable for
every k ≥ 1.

The first coefficients follow. Since q annihilates the generators, q(∂_(ϑ_B), ∂_(ϑ_B)) = g_λ(X, X) for any vector X
tangent to N_(v0) with dϑ_B(X) = 1 and dφ_i(X) = 0; take X at fixed r. From d(v + ů)(X) = 0 and dϑ_B(X) = 1,
X = (1 − ∂_ϑ ν + O(s⁶)) ∂_ϑ − (∂_ϑ ů + O(s⁴)) ∂_v. Since g_(vϑ) = r O(s⁴) and g_vv = O(1), the terms of g_λ(X, X)
containing ∂_v are r² O(s⁸), and g_λ(X, X) = r² (1 + F_3 s³ + (F_4 − 2 ∂_ϑ ν_4) s⁴ + O(s⁵)). Likewise
g_λ(∂_(φ1), ∂_(φ1)) = r² cos²ϑ (1 + G_3 s³ + G_4 s⁴ + O(s⁵)) and g_λ(∂_(φ2), ∂_(φ2)) = r² sin²ϑ (1 + H_3 s³ + H_4 s⁴ +
O(s⁵)), the cross terms vanishing by the reflections, with cos²ϑ = cos²ϑ_B (1 + 2 ν_4 tan ϑ_B s⁴ + O(s⁵)) and
sin²ϑ = sin²ϑ_B (1 − 2 ν_4 cot ϑ_B s⁴ + O(s⁵)); the shifts of the arguments of the coefficients, by ů = O(s²) and
ν = O(s⁴), change F_3 s³, G_3 s³ and H_3 s³ only at O(s⁵). Since F_3 + G_3 + H_3 = 0,

    det q = r⁶ cos²ϑ_B sin²ϑ_B (1 + (F_4 + G_4 + H_4 − 2 ∂_ϑ ν_4 + 2 (tan ϑ − cot ϑ) ν_4) s⁴ + O(s⁵))
          = r⁶ cos²ϑ_B sin²ϑ_B (1 + (F_4 + G_4 + H_4 − 2 div(ν_4)) s⁴ + O(s⁵)),

because div f = ∂_ϑ f + (cot ϑ − tan ϑ) f. With r_B⁶ = r⁶ (1 + 6 ρ_4 s⁴ + …) the areal condition gives ρ_k = 0 for k ≤ 3
and 6 ρ_4 = F_4 + G_4 + H_4 − 2 div(ν_4): ρ starts at s⁴ with the value in [[eq:bondi-first]], the trace of G_4 on the
sphere plus the Jacobian of the angular shift. The remainder of ρ is algebraic in those of (i)–(ii) and of u.

*(iv) The invariance and the Bondi functions.* The invariance and the values for v ≤ v_start are inherited from the
construction. The covariant components of [[eq:bondi-metric]] in (v_B, r_B, ϑ_B) are g_vv = −e^(2b) W + r_B² S U²,
g_vr = e^(2b), g_(vϑ) = −r_B² S U, g_(ϑϑ) = r_B² S and g_rr = g_(rϑ) = 0, and multiplying them with the stated inverse
components gives the identity; so the formulae for b, W, U, S, P1, P2 are the inversion of [[eq:bondi-metric]]'s
(v_B, r_B, ϑ_B) block. To re-express them in (v_B, ϑ_B, s_B), a coefficient f(v, ϑ) = f(v_B − ů, ϑ_B − ν) is expanded by
Taylor's formula, ů = O(s²) and ν = O(s⁴) shifting the coefficients by two and four half-orders, and
s = s_B (1 + ρ)^(1/2) by four. The expansion to order s_B^(J−2) with remainders o(s_B^(J−2)) follows, and the
r_B-gains of the remainders follow from the ℓ-gains of the ingredients (∂_(r_B) is a combination of ℓ and of E_2
multiples of ∂_v and ∂_ϑ).

The first coefficients. e^(2P1) = 1/(r_B² cos²ϑ_B g^{11}) with g^{11} = g_λ^{11} unchanged, since φ1 is unchanged,
r_B/r = 1 + O(s⁴) and ϑ_B − ϑ = O(s⁴). By [[eq:bondi-coeffs]] and the reflections, g_λ^{11} = 1/g_(φ1φ1) =
r^(−2) cos^(−2)ϑ (1 − 2 p1 s³ + O(s⁴)), since G_3 = 2p1. So e^(2P1) = 1 + 2 p1 s_B³ + O(s_B⁴), the change from (v, ϑ, s)
to (v_B, ϑ_B, s_B) costing O(s⁵); likewise e^(2P2) with H_3 = 2p2. Next, e^(−2b) = g^{v_B r_B} =
g_λ⁻¹(dv + dů, dr_B). Here g_λ^{vr} = 1 + E_2, since its correction −u_rv − (1 − μ/r²) u_rr is O(s⁴);
g_λ⁻¹(dů, dr) = ∂_v ů + ℓů + O(s⁶) with ℓů = O(s⁴); and dr_B = (1 + O(s⁴)) dr + O(s²) dv + O(s²) dϑ, whose dv- and
dϑ-parts enter only at s⁶, because they meet g_λ^{vv} in E_2, g_λ^{vϑ} = O(r^(−3)), ℓů and r^(−2) ∂_ϑ ů. So
e^(−2b) = 1 + ∂_v ů + O(s⁴) at the orders shown, and with [[eq:bondi-first]],
e^(−2b) = 1 − (∂_v C_4/2) s² − (∂_v C_5/3) s³ + O(s⁴), which is [[eq:bondi-first-metric]] in s_B. ∎

**Remark {#rem:bondi-j8}** Taking J = 8 in [[prop:bondi-hierarchy]] gives the Bondi functions to order s_B⁶ with
o(s_B⁶) remainders, which is what Section [[sec:bondi-hierarchy]] uses. The hierarchy there, run from s¹, gives
b_1 = b_2 = b_3 = 0 for a vacuum metric. By [[eq:bondi-first-metric]] this means ∂_v C_4 = ∂_v C_5 = 0, and then
C_4 = C_5 = 0 by (iv): the (ℓ, ℓ) component of g_λ − g0 is O(r^(−3)). This is a consequence, not an input:
[[prop:hierarchy-scri]] lets b start at s¹.

### The hierarchy at past null infinity {#sec:bondi-hierarchy}

In this section (v, r, ϑ) are Bondi coordinates and the metric has the form [[eq:bondi-metric]], with b, W, U, P1, P2
functions of (v, r, ϑ), S = e^(−2(P1+P2)) and s = r^(−1/2). The metric of the spheres is q_AB = r² h_AB with
h := S dϑ² + cos²ϑ e^(2P1) dφ1² + sin²ϑ e^(2P2) dφ2², whose determinant is cos²ϑ sin²ϑ, that of γ; capital indices run
over (ϑ, φ1, φ2), D is the Levi-Civita connection of γ, div f = ∂_ϑ f + (cot ϑ − tan ϑ) f is the divergence on S³ of the
field f ∂_ϑ, and Δ_h is the Laplacian of h. The inverse metric is that of [[prop:bondi-chart]], with g^{vv} = g^{vϑ} = 0,
and √|det g| = e^(2b) r³ cos ϑ sin ϑ. We write the Ricci tensor as

    R_ab = ∂_c Γ^c_ab − ∂_a ∂_b log √|det g| + Γ^c_ab ∂_c log √|det g| − Γ^c_ad Γ^d_bc.

**The Christoffel symbols with a lower index r.** Since g^{va} = e^(−2b) δ^a_r, Γ^v_rb = ½ e^(−2b) ∂_b g_rr = 0 for every
b. Since g_rr = g_(rϑ) = 0, Γ^ϑ_rr = Γ^(φi)_rr = 0 and Γ^r_rr = 2 ∂_r b. By the reflections φi ↦ −φi,
Γ^r_(rφi) = Γ^ϑ_(rφi) = Γ^(φi)_(rϑ) = 0. The others that enter below are

    Γ^r_(rϑ) = ∂_ϑ b − ½ r² e^(−2b) S ∂_r U,     Γ^ϑ_(rϑ) = 1/r − ∂_r (P1 + P2),     Γ^(φi)_(r φi) = 1/r + ∂_r P_i,
    Γ^ϑ_(rv) = −(1/(2r²S)) ∂_r (r² S U) − e^(2b) ∂_ϑ b/(r² S),
    Γ^v_(ϑϑ) = −½ e^(−2b) ∂_r (r² S),    Γ^ϑ_(ϑϑ) = ½ ∂_ϑ log S + U Γ^v_(ϑϑ),
    Γ^(φ1)_(ϑ φ1) = ∂_ϑ P1 − tan ϑ,    Γ^(φ2)_(ϑ φ2) = ∂_ϑ P2 + cot ϑ,                                {#eq:bondi-gamma-r}

each obtained from Γ^a_bc = ½ g^{ad} (∂_b g_dc + ∂_c g_db − ∂_d g_bc) with the components of [[prop:bondi-chart]].

**The radial components.** With log √|det g| = 2b + 3 log r + log(cos ϑ sin ϑ) and [[eq:bondi-gamma-r]],

    R_rr = ∂_r(2 ∂_r b) − ∂_r²(2b + 3 log r) + 2 ∂_r b (2 ∂_r b + 3/r)
           − [ (2 ∂_r b)² + (1/r − ∂_r(P1 + P2))² + Σ_i (1/r + ∂_r P_i)² ],

and the terms in 1/r² and in (∂_r b)² cancel, as do the cross terms (2/r)(∂_r(P1 + P2) − ∂_r P1 − ∂_r P2), so

    R_rr = (6/r) ∂_r b − 2 ((∂_r P1)² + ∂_r P1 ∂_r P2 + (∂_r P2)²),                                  {#eq:bondi-ric-rr}

exactly. In the same way, R_(rϑ) is ∂_r Γ^r_(rϑ) + ∂_ϑ Γ^ϑ_(rϑ) − 2 ∂_r ∂_ϑ b + Γ^r_(rϑ) ∂_r log √|det g| + Γ^ϑ_(rϑ) ∂_ϑ
log √|det g| minus Γ^r_(ϑr) Γ^r_rr + Γ^ϑ_(ϑr) Γ^r_(rϑ) + Γ^v_(ϑϑ) Γ^ϑ_(rv) + Γ^ϑ_(ϑϑ) Γ^ϑ_(rϑ) + Σ_i Γ^(φi)_(ϑφi)
Γ^(φi)_(rφi); the other products vanish by the symbols listed. Collecting: the undifferentiated U cancels between
Γ^v_(ϑϑ) Γ^ϑ_(rv) and U Γ^v_(ϑϑ) Γ^ϑ_(rϑ), because Γ^ϑ_(rϑ) = ∂_r(r²S)/(2r²S); the terms in ∂_r U combine to −½ ∂_r(r²
e^(−2b) S ∂_r U) − (3/(2r)) r² e^(−2b) S ∂_r U; the terms in ∂_ϑ b combine to −∂_r ∂_ϑ b + (3/r) ∂_ϑ b; and the terms in
P alone give the last line below. So, exactly,

    R_(rϑ) = −(1/(2r³)) ∂_r (r⁵ e^(−2b) S ∂_r U) − r³ ∂_r (r^(−3) ∂_ϑ b) − ∂_r ∂_ϑ (P1 + P2)
             + tan ϑ (2 ∂_r P1 + ∂_r P2) − cot ϑ (∂_r P1 + 2 ∂_r P2)
             − (2 ∂_r P1 ∂_ϑ P1 + ∂_r P1 ∂_ϑ P2 + ∂_ϑ P1 ∂_r P2 + 2 ∂_r P2 ∂_ϑ P2).                   {#eq:bondi-ric-rth}

**The case b = U = 0.** For the metric −W dv² + 2 dv dr + q_AB dx^A dx^B the nonzero Christoffel symbols are

    Γ^v_vv = ½ ∂_r W,   Γ^v_AB = −½ ∂_r q_AB,   Γ^r_vv = ½ (W ∂_r W − ∂_v W),   Γ^r_vr = −½ ∂_r W,
    Γ^r_vA = −½ ∂_A W,   Γ^r_AB = −½ (∂_v q_AB + W ∂_r q_AB),   Γ^A_vv = ½ q^{AB} ∂_B W,
    Γ^A_vB = ½ q^{AC} ∂_v q_CB,   Γ^A_rB = ½ q^{AC} ∂_r q_CB,   Γ^A_BC = Γ[q]^A_BC,                   {#eq:bondi-gamma-0}

and √|det g| = r³ cos ϑ sin ϑ does not depend on v. Inserting them in the formula for R_ab,
R_vr = ∂_r Γ^r_vr + (3/r) Γ^r_vr − Γ^A_rB Γ^B_vA, R_vv = (r³ cos ϑ sin ϑ)⁻¹ ∂_c (r³ cos ϑ sin ϑ Γ^c_vv) − (Γ^v_vv)² −
(Γ^r_vr)² − Γ^A_vB Γ^B_vA, and, for R_AB, the terms with indices A, B, C only give the Ricci tensor R[q] of q on the
spheres, while the others are those of Γ^v_AB, Γ^r_AB, Γ^A_vB and Γ^A_rB. Since tr(h⁻¹ ∂_v h) = ∂_v log det h = 0, and
h⁻¹ ∂h = diag(−2 ∂(P1 + P2), 2 ∂P1, 2 ∂P2), this gives

    R_vr = −½ ∂_r² W − (3/(2r)) ∂_r W − (2 ∂_r P1 ∂_v P1 + ∂_r P1 ∂_v P2 + ∂_v P1 ∂_r P2 + 2 ∂_r P2 ∂_v P2),
    R_vv = ½ W ∂_r² W + (3/(2r)) (W ∂_r W − ∂_v W) + (1/(2r²)) Δ_h W − 2 ((∂_v P1)² + ∂_v P1 ∂_v P2 + (∂_v P2)²),
    R_AB = R[q]_AB − ∂_v ∂_r q_AB − ½ ∂_r (W ∂_r q_AB) − (3/(2r)) (∂_v q_AB + W ∂_r q_AB)
           + ½ (∂_r q q⁻¹ ∂_v q + ∂_v q q⁻¹ ∂_r q + W ∂_r q q⁻¹ ∂_r q)_AB.                              {#eq:bondi-ric-0}

For instance −Γ^A_rB Γ^B_vA = −¼ tr(q⁻¹ ∂_r q q⁻¹ ∂_v q) = −¼ tr(h⁻¹ ∂_r h h⁻¹ ∂_v h), which is the last term of R_vr.
With W = 1 − μ/r² and P1 = P2 = 0, [[eq:bondi-ric-0]] gives R_vr = 0 and R_vv = 3μ'/(2r³), the Ricci tensor of g0
[[pending:ch2-vaidya-ricci]].

**The terms linear in U.** At the flat metric η_B := −dv² + 2 dv dr + r² γ (b = 0, W = 1, P1 = P2 = 0), let U^A have the
single component U^ϑ = U and U_A := γ_AB U^B. The Christoffel symbols linear in U are

    δΓ^v_vA = δΓ^r_vA = ½ ∂_r (r² U_A),   δΓ^r_rA = −½ r² ∂_r U_A,   δΓ^r_AB = −½ r² (D_A U_B + D_B U_A),
    δΓ^A_vv = −∂_v U^A,   δΓ^A_vr = −(1/(2r²)) ∂_r (r² U^A),   δΓ^C_AB = −r U^C γ_AB,                 {#eq:bondi-gamma-U}

and the others vanish; U does not change det g. By Palatini's identity δR_ab = ∇̄_c δΓ^c_ab − ∇̄_b δΓ^c_ac, with ∇̄ the
connection of η_B and δΓ^c_ac = 0, the parts of R_ab linear in U at η_B are

    δR_vr = −(1/(2r²)) ∂_r (r² D_A U^A),     δR_vv = −D_A ∂_v U^A,
    δR_AB = −(1/(2r)) ∂_r (r³ (D_A U_B + D_B U_A)) − r γ_AB D_C U^C.                                    {#eq:bondi-ric-u}

D_A U^A = div U, and δR_AB contains no derivative in v.

**Lemma {#lem:bondi-orders}** (Orders in the Bondi form.) Use the frame e_0 = ∂_v, e_1 = ∂_r, e_2 = r⁻¹ ∂_ϑ,
e_3 = (r cos ϑ)⁻¹ ∂_(φ1), e_4 = (r sin ϑ)⁻¹ ∂_(φ2), put Û := r U and y := (b, W − 1, Û, P1, P2).

(a) The components of the metric in this frame are smooth functions of y: G_00 = −e^(2b) W + S Û², G_01 = e^(2b),
G_02 = −S Û, G_22 = S, G_33 = e^(2P1), G_44 = e^(2P2), and the others vanish.

(b) Each frame component R_ij of the Ricci tensor is a finite sum of terms F(y) Π, with F smooth and Π one of
e_k e_l y_α, (e_k y_α)(e_l y_β), c e_k y_α, c c' or e_k c, where c, c' are structure coefficients of the frame,
[e_i, e_j] = c^k_ij e_k. Each structure coefficient is r⁻¹ times 1, tan ϑ or cot ϑ, so e_0 c = 0, e_1 c = −r⁻¹ c, and
e_2 c is r^(−2) times a function of ϑ. Give e_0 the weight 0, and e_1, e_2 and a structure coefficient the weight 2.

(c) In R_00 the terms of (b) whose two slots are both e_0 sum to −2((e_0 P1)² + e_0 P1 e_0 P2 + (e_0 P2)²); in every
other component they sum to 0.

(d) Consequently, if y_α has an expansion in s starting at s^(m_α), a term of R_ij whose factors from y are
y_(α1), …, y_(αn) and whose slots have total weight w has an expansion starting at s^(m_(α1) + … + m_(αn) + w). In
particular a coefficient of R_ij at a given power of s is determined by finitely many coefficients of the y_α, and
remainders o(s⁶), which stay o(s⁶) under e_0 and ∂_ϑ and gain two orders under e_1, enter only through o(·) terms.

Proof. (a) is [[eq:bondi-metric]] in the frame. (b) In a frame the connection coefficients are
Γ_kij = ½ (e_i G_jk + e_j G_ik − e_k G_ij) plus structure coefficients times components of G, each a sum of terms with
one slot, and R_ij = e_k Γ^k_ij − e_j Γ^k_ik + Γ Γ − Γ Γ − c Γ has exactly two slots in each term, since
e_k (F(y)) = F'(y) e_k y. The functions depend on (v, r, ϑ) only, so e_3 and e_4 act on them as zero. The structure
coefficients follow from [e_1, e_2] = −r⁻¹ e_2, [e_1, e_3] = −r⁻¹ e_3, [e_1, e_4] = −r⁻¹ e_4, [e_2, e_3] = r⁻¹ tan ϑ e_3,
[e_2, e_4] = −r⁻¹ cot ϑ e_4 and [e_0, e_i] = 0.

(c) Freeze (r, ϑ) = (r0, ϑ0) and let y(v) := y(v, r0, ϑ0). The terms with two slots e_0, evaluated at (v, r0, ϑ0), are
exactly the Ricci components of the metric g' := G_ij(y(v)) dx^i dx^j on R⁵ with coordinates (v, ϱ, z1, z2, z3), whose
coordinate frame has no structure coefficients and on which only e_0 = ∂_v acts. Now
g' = e^(2b) dv (2 dϱ − W dv) + S (dz1 − Û dv)² + e^(2P1) dz2² + e^(2P2) dz3², all functions of v. Put dσ := e^(2b) dv,
ϱ' := ϱ − ½ ∫ W e^(−2b) dσ and z1' := z1 − ∫ Û dv. Then g' = 2 dσ dϱ' + Σ_i e^(2Q_i) dz_i'² with
(Q_1, Q_2, Q_3) := (−(P1 + P2), P1, P2) as functions of σ. For this metric the nonzero Christoffel symbols are
Γ^(z_i)_(σ z_i) = dQ_i/dσ and Γ^(ϱ')_(z_i z_i) = −(dQ_i/dσ) e^(2Q_i), and √|det g'| = e^(ΣQ_i) = 1. The formula for
R_ab gives R_σσ = −Σ_i (d²Q_i/dσ² + (dQ_i/dσ)²) = −Σ_i (dQ_i/dσ)², and all its other components vanish: nothing depends
on ϱ', Γ^c_(ϱ'd) = 0, and in R_(z_i z_i) the only candidate, ∂_(ϱ') Γ^(ϱ')_(z_i z_i), is zero. As
dQ_i/dσ = e^(−2b) ∂_v Q_i, the Ricci tensor of g' is −Σ_i (∂_v Q_i)² dv² = −2((∂_v P1)² + ∂_v P1 ∂_v P2 + (∂_v P2)²) dv².

(d) e_0 = ∂_v preserves the order of an expansion with smooth coefficients, e_1 = ∂_r raises it by two
(∂_r s^k = −(k/2) s^(k+2), and the remainders gain by hypothesis), e_2 = r⁻¹ ∂_ϑ raises it by two (r⁻¹ = s²), and so does
a structure coefficient; products add orders. ∎

Write R_ij = R_ij|_(b=U=0) + L_ij + H_ij, where L_ij collects the terms of degree one in (b, Û) with the other
components of y at their flat values (the parts linear in b and U at η_B) and H_ij the terms that contain b or Û together
with at least one further factor of y. By (c) the terms with two slots e_0 sum to a function of the P_i alone; so those
of L_ij and of H_ij sum to zero, and every remaining term of L_ij and H_ij has weight at least 2. The coordinate
components are R_vv = R_00, R_vr = R_01, R_rr = R_11, R_(rϑ) = r R_12 and R_AB = r² × (the frame components).

**Proposition {#prop:hierarchy-scri}** (The hierarchy at past null infinity.) Let a metric of the form
[[eq:bondi-metric]], with b, W, U, P1, P2 functions of (v, r, ϑ), be vacuum near past null infinity. Let P1, P2, b, U
and W − 1 have expansions in s to order s⁶, with coefficients smooth in (v, ϑ) and remainders o(s⁶) that stay o(s⁶)
under every (v, ϑ)-derivative and gain two s-orders (one power of r) under each r-derivative, as in
[[prop:bondi-chart]]; let P_i = O(s³), and b, U, W − 1 = O(s). Let p and q be the s³ coefficients of P1 and P2, a1 and
a2 their s⁴ coefficients, and b_k, u_k, w_k the coefficients of b, U and W. Then, in order:

(0) from R_rr at s⁵, s⁶ and R_(rϑ) at s¹, s²: b_1 = b_2 = 0 and u_1 = u_2 = 0;

(i) from R_rr at s⁷, …, s¹⁰: b_3 = b_4 = b_5 = 0 and b_6 = −¼ (p² + pq + q²);

(ii) from R_(rϑ) at s³, …, s⁶: u_3 = u_4 = 0 and

    u_5 = (12/5)(p + q) tan ϑ − (8p + 16q)/(5 sin 2ϑ) − (4/5) ∂_ϑ (p + q),
    u_6 = 4 (a1 + a2) tan ϑ − (8 a1 + 16 a2)/(3 sin 2ϑ) − (4/3) ∂_ϑ (a1 + a2);

(iii) from R_vr at s⁵, s⁶, s⁷: w_1 = w_2 = 0 and w_3 = −(2/3) div(u_5), so that ⟨w_3⟩ = 0;

(iv) from the traceless part of R_AB at s²: ∂_v a1 = ∂_v a2 = 0;

(v) R_vv at s⁵ is then an identity (the rate of (iii)), and at s⁶ it is linear in ∂_v w_4 and reads

    ∂_v M = (4/3) (p_v² + p_v q_v + q_v²) + (2/3) div(∂_v u_6),       M := −w_4.                      {#eq:bondi-law-div}

The coefficient at s⁶ involves only p, q, a1, a2 and w_4, so remainders o(s⁶) do not disturb it. With (iv), ∂_v u_6 = 0,
and [[eq:bondi-law-div]] is, pointwise,

    ∂_v M = (4/3) (p_v² + p_v q_v + q_v²).                                                           {#eq:bondi-law}

Proof. We use ∂_r s^k = −(k/2) s^(k+2) throughout, and [[lem:bondi-orders]] (d) for the orders of the terms not
displayed.

*(0) and (i).* In [[eq:bondi-ric-rr]], (6/r) ∂_r (b_k s^k) = −3k b_k s^(k+4), and ∂_r P_i = −(3/2) p_i s⁵ + O(s⁶), with
(p_1, p_2) = (p, q), so the second term is −(9/2)(p² + pq + q²) s¹⁰ + O(s¹¹). The coefficient of s^(k+4) in R_rr is
therefore −3k b_k for k ≤ 5 and −18 b_6 − (9/2)(p² + pq + q²) for k = 6; vacuum gives b_1 = … = b_5 = 0 and
b_6 = −¼ (p² + pq + q²). In [[eq:bondi-ric-rth]], e^(−2b) S = 1 − 2 b_1 s + O(s²) and
r⁵ e^(−2b) S ∂_r U = −½ u_1 s^(−7) + (b_1 u_1 − u_2) s^(−6) + O(s^(−5)), so its first term is
(7/8) u_1 s + (3/2)(u_2 − b_1 u_1) s² + O(s³); the second term is (7/2) ∂_ϑ b_1 s³ + O(s⁴), and the terms in P are O(s⁵).
Vacuum gives u_1 = 0 and then u_2 = 0.

*(ii).* Now b = O(s⁶), so the term of [[eq:bondi-ric-rth]] in ∂_ϑ b is O(s⁸), e^(−2b) − 1 = O(s⁶) and S − 1 = O(s³). For
U = Σ_{k≥3} u_k s^k, −(1/(2r³)) ∂_r (r⁵ ∂_r U) = −Σ_k (k(k − 8)/8) u_k s^k, while (S − 1) and e^(−2b) − 1 add terms of
order at least s³ times the lowest order of U. The terms in P are, with ∂_r P_i = −(3/2) p_i s⁵ − 2 a_i s⁶ + O(s⁷),
(3/2)(∂_ϑ(p + q) − tan ϑ (2p + q) + cot ϑ (p + 2q)) s⁵ + 2 (∂_ϑ(a1 + a2) − tan ϑ (2a1 + a2) + cot ϑ (a1 + 2a2)) s⁶ +
O(s⁷), the quadratic ones being O(s⁸). So R_(rϑ) is (15/8) u_3 s³ + O(s⁴), which gives u_3 = 0; then 2 u_4 s⁴ + O(s⁵),
which gives u_4 = 0; and then, U being O(s⁵), the coefficients of s⁵ and s⁶ are

    (15/8) u_5 + (3/2)(∂_ϑ(p + q) − tan ϑ (2p + q) + cot ϑ (p + 2q)),
    (3/2) u_6 + 2 (∂_ϑ(a1 + a2) − tan ϑ (2a1 + a2) + cot ϑ (a1 + 2a2)).

Vacuum gives u_5 = (4/5)((2p + q) tan ϑ − (p + 2q) cot ϑ − ∂_ϑ(p + q)) and
u_6 = (4/3)((2a1 + a2) tan ϑ − (a1 + 2a2) cot ϑ − ∂_ϑ(a1 + a2)). These are the stated forms, by
1/sin 2ϑ = ½ (tan ϑ + cot ϑ).

*(iii).* By [[eq:bondi-ric-0]], R_vr|_(b=U=0) = −½ ∂_r² W − (3/(2r)) ∂_r W + O(s⁸), the last term being a product of ∂_r
P_i and ∂_v P_j. For W − 1 = Σ_k w_k s^k, −½ ∂_r² (s^k) − (3/(2r)) ∂_r (s^k) = (k(4 − k)/8) s^(k+4). By
[[eq:bondi-ric-u]], L_vr has the part −(1/(2r²)) ∂_r (r² div U) = ¼ div(u_5) s⁷ + O(s⁸) linear in U, and its part linear
in b has weight at least 2 and so is O(s⁸), b being O(s⁶). The terms of H_vr contain b, of order 6, or Û, of order 3
since U = O(s⁵), together with a factor of order 3 (P_i or Û) or of the order m of W − 1, and have weight at least 2:
they are O(s^(5+m)) when m ≤ 3. With m = 1 the coefficient of s⁵ is (3/8) w_1, so w_1 = 0; then m = 2 and the
coefficient of s⁶ is ½ w_2, so w_2 = 0; then m = 3 and the coefficient of s⁷ is (3/8) w_3 + ¼ div(u_5), so w_3 = −(2/3)
div(u_5). Its sphere mean vanishes, since ∫_0^(π/2) ∂_ϑ (f sin ϑ cos ϑ) dϑ = 0 for every smooth f.

*(iv).* Now W − 1, P_i and Û are O(s³) and b is O(s⁶), so H_AB and the part of L_AB linear in b have frame order at
least 8, that is, coordinate order at least s⁴; by [[eq:bondi-ric-u]] the part linear in U has no derivative in v and
is O(s³) in coordinates. In R_AB|_(b=U=0) from [[eq:bondi-ric-0]], write W = 1 + ω and h = γ + k, so that q = r²(γ + k)
with k = diag(−2(P1 + P2), 2 cos²ϑ P1, 2 sin²ϑ P2) + O(s⁶). The terms of degree two or more in (ω, k) have weight at
least 2 by [[lem:bondi-orders]] (c), hence frame order at least 8 and coordinate order at least s⁴. R[q] = R[γ + k] =
2γ + O(s³). In the rest, to first order: the constant terms give −2γ, cancelling 2γ; the terms in ω give −(r ∂_r ω +
2ω) γ_AB = Σ_k (k/2 − 2) w_k s^k γ_AB, which is O(s³) now that w_1 = w_2 = 0; the terms in k with a derivative in v
come from −∂_v ∂_r q, −(3/(2r)) ∂_v q and ½ (∂_r q q⁻¹ ∂_v q + ∂_v q q⁻¹ ∂_r q), and sum to −r² ∂_r ∂_v k − (3/2) r ∂_v
k = Σ_j ((j − 3)/2) ∂_v k_j s^(j−2) for k = Σ_j k_j s^j; and the terms in k without a derivative in v are O(s³). So at
s² the three angular components of R_AB are those of ½ ∂_v k_4, with k_4 = diag(−2(a1 + a2), 2 cos²ϑ a1, 2 sin²ϑ a2):
they are −∂_v(a1 + a2), cos²ϑ ∂_v a1 and sin²ϑ ∂_v a2, a traceless tensor. Vacuum gives ∂_v a1 = ∂_v a2 = 0.

*(v).* All of W − 1, P_i and Û are O(s³) and b is O(s⁶). So H_vv and the part of L_vv linear in b are O(s⁸), and the
part linear in U is −div(∂_v U) = −div(∂_v u_5) s⁵ − div(∂_v u_6) s⁶ + o(s⁶), by [[eq:bondi-ric-u]]. In R_vv|_(b=U=0)
from [[eq:bondi-ric-0]], ½ W ∂_r² W, (3/(2r)) W ∂_r W and (1/(2r²)) Δ_h W are O(s⁷), −(3/(2r)) ∂_v W = −(3/2) ∂_v w_3 s⁵
− (3/2) ∂_v w_4 s⁶ + O(s⁷), and −2((∂_v P1)² + ∂_v P1 ∂_v P2 + (∂_v P2)²) = −2(p_v² + p_v q_v + q_v²) s⁶ + O(s⁷). Hence

    R_vv = −((3/2) ∂_v w_3 + div(∂_v u_5)) s⁵ − ((3/2) ∂_v w_4 + 2(p_v² + p_v q_v + q_v²) + div(∂_v u_6)) s⁶ + o(s⁶).

The coefficient of s⁵ vanishes identically by (iii). The coefficient of s⁶ involves only p, q, a1, a2 (through u_6) and
w_4, and its vanishing is [[eq:bondi-law-div]] with M = −w_4. With (iv), ∂_v u_6 = 0, since u_6 is linear in a1 and a2
with coefficients depending on ϑ alone. ∎

**Remark {#rem:bondi-tts}** (Comparison with [TTS09].) Tanabe, Tanahashi and Shiromizu write the five-dimensional Bondi
form as ds² = −(V e^B/r²) du² − 2 e^B du dr + r² h_AB (dx^A + U^A du)(dx^B + U^B du), with h_AB built from functions C1,
C2, C3, D1, D2, D3 and the areal condition r⁶ sin²θ cos²θ = det(g_AB) [TTS09, (2), (4), (5), p. 2]. For waves, C ~
r^(−3/2), and their equations give B = B1/r³ + O(r^(−7/2)) with B1 = −(C11² + C11 C21 + C21² + D11² + D21² + D31²)/8,
U^A = U_(A1)/r^(5/2) + O(1/r³), and V = r² + V1(u, x^A) r^(1/2) − M(u, x^A) + O(r^(−1/2)), with V1 minus two thirds of
the divergence of U_(A1) [TTS09, (20), (21), (25)–(27), pp. 3–4]. Their mass law reads

    "dM(u, x^A)/du = −(1/3)((C_11,u)² + C_11,u C_21,u + (C_21,u)² + (D_11,u)² + (D_21,u)² + (D_31,u)²)"
                                                                                  [TTS09, (28), p. 4],

and "Eq. (28) represents mass loss rate by gravitational waves" [TTS09, p. 4]. The r^(−2) term A of C satisfies
∂A/∂u = 0 and vanishes for asymptotic flatness, by its value at spatial infinity [TTS09, (35), (36), p. 5]. In the class
the reflections give D1 = D2 = D3 = 0, and with u = −v, θ = π/2 − ϑ and (φ, ψ) = (φ1, φ2) their form is
[[eq:bondi-metric]] with C1 = −2(P1 + P2), C2 = 2P1, C3 = 2P2, B = 2b, V/r² = W and U^θ = −U. So C11 = −2(p + q),
C21 = 2p, and B1 = −½(p² + pq + q²) = 2 b_6, as in (i); V1 = w_3, as in (iii); (35) is (iv); and (28) becomes
dM/du = −(4/3)(p_u² + p_u q_u + q_u²). The time reversal u = −v leaves the squares unchanged and reverses the sign of
the rate, which gives [[eq:bondi-law]]: an incoming flux raises the mass. [[prop:hierarchy-scri]] derives all of this in
[[eq:bondi-metric]] itself, with every coefficient general from s¹ on, and takes nothing from [TTS09].

### Proof of the mass law {#sec:bondi-proof}

Proof of [[thm:bondi-law]]. *The chart.* [[prop:bondi-chart]] with J = 8 gives, on the far region P ∩ {t ≥ T_M},
T_M = T_M(λ), Bondi coordinates (v_B, r_B, ϑ_B, φ1, φ2): v_B is null for g_λ, with v_B − v → 0 at past null infinity
along every generator of g0; ϑ_B is constant along the generators of {v_B = const}; r_B is the areal radius of the
spheres {v_B, r_B = const}; and g_λ has the form [[eq:bondi-metric]]. In s := r_B^(−1/2), the functions P1, P2, b, U and
W − 1 have expansions f = Σ_{k=1}^{6} s^k f_k(v_B, ϑ_B) + o(s⁶) whose coefficients are smooth, bounded with all their
derivatives, invariant under T² × Z2 × Z2 and equal to those of g0 for v_B ≤ v_start (zero there, but for
W − 1 = −μ0 s⁴), and whose remainders have every (v_B, ϑ_B)-derivative o(s⁶) and gain an order, one power of r_B and
two of s, under each r_B-derivative; the remainders of [[prop:bondi-chart]] lie in classes E_p with all their
derivatives. This is the chart and the form of the metric that the theorem asserts. By [[eq:bondi-first-metric]],
P_i = O(s³), and b, U and W − 1 are O(s), so [[prop:hierarchy-scri]] applies to g_λ, which is vacuum.

*Item 1, the angular metric.* The s³ coefficient of P_i is p_i, by the last part of [[prop:bondi-chart]]:

    p1 = (2 cos²ϑ_B G − sin²ϑ_B F)/3,    p2 = (2 sin²ϑ_B F − cos²ϑ_B G)/3,
    F = λ A env(v_B) h sin(v_B/λ),    G = λ A env(v_B) h cos(v_B/λ),                                  {#eq:bondi-p}

the free data at the phase v_B/λ, with h the angular profile, h² = 2/(1 + z²), z := cos 2ϑ_B. The radiation field of
[[thm:past-construction]] is this statement in the wave-map gauge, and the change of chart preserves it. For the s⁴
coefficients a_i: by [[prop:hierarchy-scri]] (iv), ∂_v a_i = 0, and a_i = 0 for v_B ≤ v_start, where the metric is
g0 ([[prop:bondi-chart]] (iv)); so a_i = 0. This is the argument of [TTS09] from spatial infinity, with the seed in its
place.

*Item 2, the mass aspect.* By [[prop:hierarchy-scri]] (iii), W = 1 + s³ V1 − s⁴ M + O(s⁵) with V1 := w_3 =
−(2/3) div(u_5), a divergence on S³, and by (v) with a_i = 0 the mass aspect obeys [[eq:bondi-law]] pointwise. M = μ0
for v_B ≤ v_start, since g_λ = g0 there: the Vaidya metric with μ = μ0, whose W is 1 − μ0 s⁴.

*Item 3, the Bondi mass.* Let μ_B(v) := ⟨M(v, ·)⟩, the mean over S³. By [[eq:bondi-p]], ∂_v F = A h D_s and
∂_v G = A h D_c, where

    D_c := ∂_v (λ env cos(v/λ)) = λ env' cos(v/λ) − env sin(v/λ),
    D_s := ∂_v (λ env sin(v/λ)) = λ env' sin(v/λ) + env cos(v/λ).

With x := cos²ϑ D_c and y := sin²ϑ D_s, ∂_v p1 = A h (2x − y)/3 and ∂_v p2 = A h (2y − x)/3. Since
(2x − y)² + (2x − y)(2y − x) + (2y − x)² = 3 (x² − xy + y²),

    (4/3)(p1_v² + p1_v p2_v + p2_v²) = (4/9) A² h² (cos⁴ϑ D_c² + sin⁴ϑ D_s² − cos²ϑ sin²ϑ D_c D_s),   {#eq:bondi-density}

the flux density at past null infinity of Chapter 9 [[pending:ch9-flux]]. The mean over S³ of a function of ϑ is
⟨f⟩ = 2 ∫_0^(π/2) f cos ϑ sin ϑ dϑ = ½ ∫_{−1}^{1} f dz. With cos²ϑ = (1 + z)/2, sin²ϑ = (1 − z)/2 and h² = 2/(1 + z²),

    ⟨h² cos⁴ϑ⟩ = ¼ ∫_{−1}^{1} (1 + 2z/(1 + z²)) dz = ½,     ⟨h² sin⁴ϑ⟩ = ½,
    ⟨h² cos²ϑ sin²ϑ⟩ = ¼ ∫_{−1}^{1} (2/(1 + z²) − 1) dz = π/4 − ½.

Since D_c² + D_s² = env² + λ² env'² and D_c D_s = −½ (env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ), the sphere
mean of [[eq:bondi-density]] is

    μ_B' = (2/9) A² [ env² + λ² env'²
             + (1 − π/2)(−½ (env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ)) ],      {#eq:bondi-flux}

exactly. We integrate from v_start, where μ_B = μ0 and env vanishes to all orders. The first term gives μ(v) − μ0, since
μ' = (2/9) A² env² [[pending:ch2-null-dust]]. For the oscillating term, a differentiation shows

    −½ (env² − λ² env'²) sin(2v/λ) + λ env env' cos(2v/λ)
        = d/dv [ (λ/4) env² cos(2v/λ) + (λ²/4) env env' sin(2v/λ) ] + (λ²/4)(env'² − env env'') sin(2v/λ),

and ∫_{v_start}^{v} f sin(2v'/λ) dv' = O(λ) for every smooth f vanishing at v_start, by one integration by parts; so
the last term contributes O(λ³). Hence

    μ_B(v) = μ(v) + (2/9) λ² A² ∫_{−∞}^{v} env'²
             + (1 − π/2) (2/9) A² ((λ/4) env² cos(2v/λ) + (λ²/4) env env' sin(2v/λ)) + O(λ³).              {#eq:bondi-mu}

Both boundary terms carry the factor 1 − π/2, because the integrated flux is linear in the oscillating coefficient. So
μ_B is μ(v) + O(λ) while the shell passes, with the oscillation that [[eq:bondi-flux]] gives, and after the shell, where
the boundary terms vanish with env and env', μ_B = μ(v_end) + (2/9) λ² A² ∫ env'² + O(λ³). In particular μ_B' is the
flux [[eq:bondi-flux]] exactly.

*Item 4, the Hawking mass.* By [[prop:mean-mass]], M[S] = R²(1 + (R²/9)⟨Θ⟩) with Θ := 2 θ⁺ θ⁻/(−g(n⁺, n⁻)) and
R := (Area(S)/(2π²))^(1/3). Write (v, r, ϑ) for the Bondi coordinates and let S = {v, r = const}. Since r is areal,
Area(S) = 2π² r³ and R = r. The future null normals of S are n⁻ = −∂_r and n⁺ = ∂_v + (W/2) ∂_r + U ∂_ϑ: by
[[eq:bondi-metric]], g(∂_r, ∂_r) = g(∂_r, ∂_ϑ) = 0, g(n⁺, ∂_ϑ) = g_(vϑ) + U g_(ϑϑ) = 0, and
g(n⁺, n⁺) = (−e^(2b) W + r² S U²) + W e^(2b) − 2 r² S U² + r² S U² = 0, while g(n⁺, n⁻) = −e^(2b). The area form of S is
r³ cos ϑ sin ϑ dϑ dφ1 dφ2, independent of v, so θ⁻ = −3/r exactly and θ⁺ = 3W/(2r) + div U. So
Θ = −(9/r²) e^(−2b) (W + (2r/3) div U) and

    M[S] = r² (1 − ⟨e^(−2b) (W + (2r/3) div U)⟩).

With b = O(s⁶), W = 1 + w_3 s³ + w_4 s⁴ + O(s⁵), U = u_5 s⁵ + u_6 s⁶ + o(s⁶) and r = s^(−2),
e^(−2b)(W + (2r/3) div U) = 1 + (w_3 + (2/3) div u_5) s³ + (w_4 + (2/3) div u_6) s⁴ + o(s⁴), and

    M[S] = −s⁻¹ ⟨w_3 + (2/3) div u_5⟩ − ⟨w_4 + (2/3) div u_6⟩ + o(1).

The divergences have zero mean, so M[S] → ⟨−w_4⟩ = ⟨M⟩ = μ_B(v_B) as r_B → ∞. ∎

**Remark {#rem:bondi-solver}** (An independent evolution of the same data.) The vacuum equations can be integrated in the
form [[eq:bondi-metric]] from the free data [[eq:bondi-p]] at past null infinity, the rate of the mass aspect being
fixed by the coefficient of s⁶ in R_vv, that is, by [[eq:bondi-law-div]]. Two facts make such an integration comparable
with [[thm:bondi-law]]. First, after the shell the aspect is independent of ϑ_B to O(λ³). Indeed, writing
cos⁴ϑ D_c² + sin⁴ϑ D_s² as ½ (cos⁴ϑ + sin⁴ϑ)(env² + λ² env'²) + (sin⁴ϑ − cos⁴ϑ) O_1 with
O_1 := ½ (env² − λ² env'²) cos(2v/λ) + λ env env' sin(2v/λ), and using h² (cos⁴ϑ + sin⁴ϑ) = 1, the density
[[eq:bondi-density]] is (2/9) A² (env² + λ² env'²) plus ϑ-dependent multiples of O_1 and of D_c D_s. Both oscillate at
twice the frequency of the wave, and, as above, each is a v-derivative of terms that vanish with env and env' plus
λ² times a smooth function times cos(2v/λ) or sin(2v/λ), whose integral is O(λ³). So for v ≥ v_end,
M(v, ϑ_B) = μ(v_end) + (2/9) λ² A² ∫ env'² + O(λ³) uniformly in ϑ_B, and any average of M over ϑ_B, for instance over a
set of nodes in cos 2ϑ_B, equals μ_B to O(λ³) there; while the shell passes, M depends on ϑ_B at O(λ), and such an
average need not equal μ_B. Second, for the envelope env(v) = sin⁴(π(v − ½)/3) on [½, 7/2] and A = 1, the substitution
ξ = π(v − ½)/3 gives ∫ env'² = (16π/3) ∫_0^π sin⁶ξ cos²ξ dξ = (16π/3)(5π/16 − 35π/128) = 5π²/24, so the coefficient of
λ² after the shell is (2/9)(5π²/24) = 5π²/108 = 0.45693… . [[pending:computational-1]] An evolution of this kind, on
Chebyshev–Lobatto nodes in cos 2ϑ, gives for the offset of its node-averaged aspect from μ after the shell, divided by
λ², the values 0.4589, 0.4577, 0.4568 at λ = 0.05, 0.025, 0.0125 (μ0 = 100 l5²) and 0.4578, 0.4569 at λ = 0.025, 0.0125
(μ0 = 1000 l5²), each the mean over the samples after the shell; at λ = 0.0125 the agreement with 5π²/108 is within
0.05 %, and one finer run, λ = 0.00625 at μ0 = 100 l5², gives 0.4535, 0.74 % below, on the grid of the previous run,
a grid too coarse for that wavelength. The rows at 1000 l5²
reproduce those at 100 l5² to about 10⁻⁴, the far region not depending on the inner cut, so they are not an
independent check. Such a comparison tests the law against an integration of the same law; it is not a premise of
[[thm:bondi-law]], which proves that g_λ obeys the law.

**Remark {#rem:bondi-scope}** (What is not claimed.) [[prop:bondi-hierarchy]] claims no uniformity in λ of the expansion
beyond its leading term, which the mass law does not need. Nothing is claimed about future null infinity or the Bondi
mass there, which the domain does not reach.

