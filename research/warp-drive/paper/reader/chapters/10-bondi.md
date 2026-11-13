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

Proof. Write g := g_λ = g0 + r^(−3/2) G_3 + u_1. By [[lem:bondi-equation-u]] below, u_1 = u − r^(−3/2) G_3 solves

    −½ g^{ab} ∂_a ∂_b u_1 = F_1 := S(u) − ½ (g^{ab} − g0^{ab}) ∂_a ∂_b u_1 + ½ □̃ (r^(−3/2) G_3).          {#eq:bondi-f1}

*The structure of F_1.* By the reduced equations [[pending:ch2-reduced-equations]], every Lorentzian g satisfies
Ric^H(g) = −½ g^{ab} ∂_a ∂_b g + Q(X; g)(∂g, ∂g), with Q a polynomial of degree two in ∂g whose coefficients are
rational in g and smooth in X through Γ[g0] and its first derivatives, and Ric^H(g0) = Ric(g0). Insert the definition
(eq:bondi-S) of S into (eq:bondi-f1), use ∂_a ∂_b (g0 + u) = ∂_a ∂_b (g0 + r^(−3/2) G_3) + ∂_a ∂_b u_1, and replace
Ric(g0) by −½ g0^{ab} ∂_a ∂_b g0 + Q(X; g0)(∂g0, ∂g0). The terms in g0 alone cancel, and

    F_1 = ½ g^{ab} ∂_a ∂_b (g0 + r^(−3/2) G_3) − Q(X; g)(∂g, ∂g)
        = −Ric^H(g) − ½ g^{ab} ∂_a ∂_b u_1,                                                         {#eq:bondi-f1-form}

an identity in u_1: it holds for every symmetric u_1 that keeps g Lorentzian, not only for the solution. So F_1 contains
no second derivative of u_1. It is a smooth function F_1(X, u_1, ∂u_1), and F_1(X, 0, 0) = −Ric^H(g0 + r^(−3/2) G_3)
is in E_3 with all its derivatives: at u_1 = 0 the terms of S are those of [[lem:bondi-equation-u]] in G_3 and g0, all
in E_3, and the third term of (eq:bondi-f1) is in E_(7/2), because by the decay calculus of Chapter 9
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
            − [ Q(X; g0 + u)(∂g0 + ∂u, ∂g0 + ∂u) − Q(X; g0)(∂g0, ∂g0) ],                             {#eq:bondi-S}

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
(eq:bondi-transport) is a transport along the outgoing generators. Along one of them, parametrised by σ, dv/dσ = 2 and
dr/dσ = 1 − μ/r² ∈ (0, 1]. From a point (v, r) the generator therefore reaches {v = v_start}, where ψ = 0, after a
parameter length (v − v_start)/2 ≤ d1/2 [[pending:ch9-past-domain]], at a radius r' ∈ [r − d1/2, r]. Integrating
(L₊ + 3/r) ψ = f along it gives |ψ(v, r)| ≤ e^(3 d1/(2 r')) (d1/2) sup |f| ≤ C r^(−q−1/2), the supremum taken over the
segment, which lies in the far region once r is large.

Derivatives commute through (eq:bondi-transport) up to terms of the same kind. Ω commutes with L₊ and with 3/r, since it
annihilates v, r and μ(v); so Ω^b ψ solves (eq:bondi-transport) with the forcing Ω^b f. ∂_v commutes up to
[∂_v, L₊] = −(μ'/r²) ℓ, and ℓψ is read off (eq:bondi-transport) itself, (1 − μ/r²) ℓψ = f − 2 ∂_v ψ − (3/r) ψ. So
∂_v^a Ω^b ψ solves (eq:bondi-transport) with a term of order zero, O(r^(−2)) times ∂_v^a Ω^b ψ, moved to the left (over
a parameter length at most d1/2 it changes the integrating factor by a bounded factor), and a forcing in E_(q+1/2) by
the lower a. The ℓ-components of the derivatives of ψ are then read off (eq:bondi-transport) in the same way:
ℓ^c ∂_v^a Ω^b ψ is in E_(q+1/2) by induction on c, and every Cartesian derivative is a combination of ℓ, ∂_v and
r⁻¹ Ω with coefficients bounded with all their derivatives. So ℓǔ is in E_(q+1/2) with all derivatives. This is the
case m = 1, which needs nothing of (H_m), since f contains no ℓ-derivative of S′ or of g_λ.

For m ≥ 2, under (H_m), the equation of ℓ^m ǔ = ℓ^(m−1) ψ is (eq:bondi-transport) commuted m − 1 times with ℓ. Its
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
(eq:bondi-u-split), such that on the far region

    u = Σ_{k=3}^{J} r^(−k/2) G_k + u_J,     ∂_X^α Ω^β ℓ^m u_J ∈ E_((J+1)/2 + m) for all α, β, m.  {#eq:bondi-expansion}

The G_k are determined inductively: G_k = (2/(k − 3)) ∫_{v_start}^{v} S_(k/2+1) dv' for k ≥ 4 (so G_4 = 2 ∫ S_3), where
r^(−q) S_q is the leading term of the forcing once the terms below it are known.

Proof. We induct on J with [[lem:bondi-half-order]]. For J = 3, u_3 := u_1 is in E_2 with all derivatives by
[[lem:every-order-fixed]], and by [[lem:bondi-equation-u]] it solves
−½ g_λ^{ab} ∂_a ∂_b u_3 = S(u) − ½ (g_λ^{ab} − g0^{ab}) ∂_a ∂_b u_3 + ½ □̃(r^(−3/2) G_3) =: F_1. The second term is in
E_(7/2) (E_(3/2) E_2), the third in E_(7/2) [[pending:ch9-decay-calculus]], and S(u) is in E_3 with a leading term
r^(−3) determined by G_3 alone: −(3μ'/2) dv dv from Ric(g0), plus the terms of (eq:bondi-S) quadratic in
∂(r^(−3/2) G_3) or of the form (r^(−3/2) G_3) ∂²(g0 + r^(−3/2) G_3), since every term containing u_3 is in E_(7/2)
(E_(3/2) E_2, or Γ[g0] times E_2). So (eq:bondi-half) holds at q = 3, and [[lem:bondi-half-order]] gives
u = r^(−3/2) G_3 + r^(−2) G_4 + u_4 with every derivative of u_4 in E_(5/2).

*The ℓ-gains at J = 3, by induction on m.* The case m = 1 needs no hypothesis: ℓu_4 is in E_3, hence
ℓu_1 = ℓ(r^(−2) G_4) + ℓu_4 is in E_3 and ℓ(g_λ − g0) = ℓ(r^(−3/2) G_3) + ℓu_1 is in E_(5/2), with all derivatives.
Suppose ℓ^j u_4 is in E_(5/2+j) for j < m. Then ℓ^j (g_λ − g0) is in E_(3/2+j) for j < m, and ℓ^j S̃ is in E_(7/2+j):
S̃ = F_1 − r^(−3) S_3 is a polynomial in g0, g_λ⁻¹, u, ∂u and ∂²u each of whose terms either is explicit (the terms in
G_3 and g0, whose ℓ-derivatives gain an order each because r^(−k) and the profiles do) or contains u_1 or a derivative
of it, on which ℓ^j gains j orders by the hypothesis, the other factors keeping their classes. So (H_m) holds, and
[[lem:bondi-half-order]] gives ℓ^m u_4 in E_(5/2+m): (eq:bondi-expansion) at J = 4.

*Stage J ≥ 4.* The remainder u_J has every ℓ-gain. So the forcing of u_J, a polynomial in (u, ∂u, ∂²u) with
coefficients smooth in (X, g) whose arguments are expanded to the previous order with remainders in E_((J+1)/2), has
the form r^(−q) S_q + S̃ with q = (J + 3)/2 and S̃ satisfying (H_m) for every m: every product with a remainder factor is
in E_(3/2 + (J+1)/2) = E_(q+1/2) or better and gains under ℓ. So the coefficient of r^(−q) is a polynomial in the G_k,
k ≤ J, and their derivatives, and [[lem:bondi-half-order]] applies at every m. The invariance and the vanishing for
v ≤ v_start are inherited by the integrals from v_start. ∎

**Remark {#rem:bondi-lambda}** The coefficients from G_4 on depend on λ, through the phase v/λ and the powers of λ of the
profiles, and [[prop:bondi-hierarchy]] claims nothing uniform in λ. It is an asymptotic statement at past null infinity
at each fixed λ, which is all the mass law needs.

