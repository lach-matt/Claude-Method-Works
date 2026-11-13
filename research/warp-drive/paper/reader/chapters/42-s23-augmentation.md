## Augmentation by the expansion's coefficients and efficient parameterisation {#ch:s23}

This chapter proves three groups of results on the gauge-fixed Einstein operator in the forward cone, each a part of
[Hin26, Sections 11.8.3 and 12] (pp. 292–318) in dimension 4 + 1.

In [[sec:iii-i14-1]]–[[sec:iii-i14-3]] ([Hin26, Section 11.8.3], pp. 292–296) the parameters of the partial expansion of
[[thm:iii-i12-3-1]] become arguments of an augmented gauge-fixed Einstein operator P_5 ([[def:iii-i14-1-2]]; [Hin26,
Definition 11.63]). Its linearisation in the black hole parameters has the full order of decay at K⁺
([[lem:iii-i14-2-4]] (c); [Hin26, Lemma 11.65]), and the linearised equation at (h, p⃗, q) has, for every right-hand
side, a unique choice of p⃗′ for which the solution splits as h_rem(q′) + h′ with h′ of the decay assumed of h
([[thm:iii-i14-3-1]]; [Hin26, Corollary 11.66]).

In [[sec:iii-j-1]]–[[sec:iii-j-2]] ([Hin26, Definition 12.1, Section 12.2.1 with Lemma 12.2, Theorem 12.3 and Remarks
12.4–12.6], pp. 296–311) a tuple of data determines (h, p⃗, q) at which P_5 vanishes at ι⁺ to the order 5 + ε_+ and has
the K⁺-order α ([[thm:iii-j-2-4]]). The data are the final black hole parameters, the boost and translation, the free
ι⁺-data at each ι⁺-resonance, the conormal remainders of the modification parameters and a remainder tensor.

In [[sec:iii-j1-1]]–[[sec:iii-j1-2]] ([Hin26, Theorem 12.8 and Remark 12.9], pp. 312–318) every solution of the
linearised equation that [[thm:iii-i14-3-1]] produces, for a right-hand side of the class ℱ of [[def:iii-j-classes]], is
D_UΦ(U′) for data U′, so that the map Φ of [[thm:iii-j-2-4]] describes the linear forward solutions exactly
([[thm:iii-j1-2-1]]). The tame forms of the estimates of [[thm:iii-i14-3-1]] and [[thm:iii-j1-2-1]], and their forms at
exact weights, are proved in [[ch:s24]].

*Dimension 4 + 1.* The argument differs from that of [Hin26] in the following points.

(1) *The linearisation is taken at h, not at h + h_rem(q).* [Hin26] proves [Hin26, Corollary 11.66] by applying [Hin26,
Theorem 11.59] at the background h + h_rem(q), whose K⁺-order is only 2 + ε_K ([Hin26, Remark 11.61]). In dimension 4 +
1 that background has K⁺-order α − 2 − ε, while [[thm:iii-i11-4-1]] needs a_K ≥ 4 + ε_K, the remainders r^ν of the rows
need a_K > α + 1 − λ_♯ ([[lem:iii-i9-2-6]] (c)), and a perturbation series in q around it loses two derivatives per
term. Instead the forward solution u at h + h_rem(q), which exists and is smooth, satisfies L_(h,p⃗)u = F −
D_(p⃗)P_5(p⃗′) − R_q u, and its decay is raised level by level through the levels of [[def:iii-i13-1-1]], each step an
expansion at h, where a_K ≥ 4 + ε_K. The steps are shorter than α − 4, r^ν is only ever taken at h, and the derivatives
of the rows differ only by R_q(h_ν(W)), supported away from K⁺. The new coefficients at each level are the new
parameters up to a small error, as in [[thm:iii-i11-4-1]].

(2) *The losses.* The linear theory of [[ch:s22]] loses an ε at K⁺. The classes are read with the orders "w−", every
order below w ([[sec:iii-i14-1]]), and the constructions of [[thm:iii-i11-4-1]], [[thm:iii-i12-3-1]] and
[[sec:iii-i13-2]] accept sources of K⁺-order α− and do not depend on the loss ([[lem:iii-i14-2-5]]). This makes the
class of h′ that of h ([[rem:iii-i14-3-2]]). With a fixed loss, the boost and black hole parameter coefficients would
lose an ε at each application.

(3) *Rotation rows.* At the non-rotating b₀ every rotation is Killing, so the v1 terms of exponent below 2 carry no row
([[sec:iii-i9-1]]), and the bookkeeping of [Hin26] would put them into q. But at a rotating b near b₀ the rotation state
h_(b,v1) need not vanish, and such a coefficient would give the linearisation in b the K⁺-order α − 2 + λ_♯ only. These
terms are carried instead by rows of all rotations ([[def:iii-i14-1-3]]), whose coordinates are fixed in
[[thm:iii-i14-3-1]] by the expansion (Step 4′ of its proof). So are the v1 terms of real part 2, whose square would
leave P_5 at a rotating b with the K⁺-order 4 only ([[eq:iii-j-2-5]]).

(4) *The exterior family.* [Hin26, (11.228)] contains a tensor χ_−h_(−S), supported there in t_* ≤ 2, which carries
the initial data; [Hin26] permits h_(−S) = 0 in its Section 11.8.3, and we take h_(−S) = 0 throughout this chapter. The
family h_(−S) is built in [[prop:iii-k-1-2]] ([Hin26, (12.33)]). The term is restored in [[ch:s27]], with a cut-off
χ_−(t^♭_*) supported in {t^♭_* ≤ T̂ + 2}, T̂ ≥ 2 as in [[sec:iii-k-0]], where the map Ψ := (χ_−h_(−S), 0, 0) + Φ is
formed ([[def:iii-k-2-1]]):
[Hin26, Lemma 12.7], the counterpart of [[thm:iii-j-2-4]] for Ψ, is [[lem:iii-k-2-2]], and [Hin26, Theorem 12.8] for Ψ,
the counterpart of [[thm:iii-j1-2-1]], is [[lem:iii-k-2-3]]. [Hin26, Corollary 11.67], a linear stability statement
sketched there, is not used in this paper. The linear stability statement proved here is that of the
Schwarzschild–Tangherlini metric g_(b₀), at b₀ only: [[thm:viii-2-2]].

(5) *No step at t_*^(−1).* The first step of [Hin26, Section 12.2.1] solves for the t_*^(−1)-term, from the resonance at
λ = 1 and the t_*^(−1)-tail of the black hole. In dimension 4 + 1 the least ι⁺-exponent is λ_♯ = 3/2 + (1 − e_Υ)γ_Υ, a
simple pole with Res_(ι⁺)(L̄, λ_♯) = {0} ([[cor:iii-g3-2-6]], [[rem:iii-g3-3-8]]), and the black hole parameters enter
at t_*^(−2). Likewise the first step of the proof of [Hin26, Theorem 12.8] (the t_*^(−3)-terms of the right-hand side)
becomes the removal of the parameters p⃗′_(≤0), and every exponent is then treated by its second step.

(6) *The ι⁺-series below 3 + ε_+ is linear.* Every product of two terms has u-exponent at least 2λ_♯ = 3 + 2δ_♯ > 3 +
ε_+, and the departure of the background from Minkowski space shifts the u-exponent by at least 2. So each step of the
construction is one linear equation L̄ G(λ₀) = −F_0(λ₀) with F_0 depending only on the black hole parameters
([[lem:iii-j-2-1]]), and Φ is affine in the infinite-dimensional data, with coefficients smooth in the black hole, boost
and translation parameters, which gives its smoothness and tame bounds at once. The iteration of [Hin26], nonlinear in
dimension 3 + 1 (its terms of size t_*^(−1) interact), is here a finite sequence of linear model problems.

(7) *The modification parameters* are the rows of [[sec:iii-i9-1]] (rates at most 2) with the rotation rows of
[[def:iii-i14-1-3]], and the tower coefficients of q ([[def:iii-i14-1-1]], rates above 2); the formal solutions at ι⁺ ∩
K⁺ are matched to them by [[lem:iii-i10-2-1]] ([[lem:iii-j-2-2]]). The conormal V_(1,rem) of [Hin26, (12.11)] has no
counterpart: in dimension 4 + 1 the v1 coefficient of q has no conormal part ([[thm:iii-i12-3-1]]).

(8) *The resonances used* are those in π_1ℰ_♯: the forward solutions of [[thm:iii-i14-3-1]] have ι⁺-exponents in ℰ_♯ and
excite no other, so only these carry data; a pure ι⁺-resonance outside Λ is excited by no right-hand side of the
iteration.

(9) *Orders.* The K⁺-order is α− with α as in [[sec:iii-i14-1]], read as there; the ι⁺-order is (3 + ε_+)− for the
metric and (5 + ε_+)− for P_5. The constructions of [[ch:s22]] give the linear solutions the ι⁺-order (3 + η_2)− with
η_2 < ε_+. Under the condition (G⁺) ([[def:iii-j-g-plus]]) no exponent lies between, the construction does not depend on
η_2 in that window, and the linear solutions have the ι⁺-order (3 + ε_+)− of the nonlinear class ([[lem:iii-j1-1-1]]);
without this the scheme would lose ε_+ − η_2 at ι⁺ at every step.

*Base points.* The black hole parameter b ranges near b₀ = (m₀, 0). The coefficients and the augmented operator
([[def:iii-i14-1-1]]–[[def:iii-i14-1-3]], [[eq:iii-i14-1-4]]), the towers ([[lem:iii-i14-2-1]]), the order of L_b
h_(b,rem)(q) ([[lem:iii-i14-2-2]] (b)) and the construction of [[sec:iii-j-1]]–[[sec:iii-j-2]] are stated at every such
b. Their proofs at b use [[lem:iii-i14-2-2]] (a) at b, which [[thm:iii-i15-3-1]] supplies, the reality of the states at
b, which [[lem:iii-i15-1-1]] (P3) supplies, and, for the rate of the rotation rows at b, [[lem:iii-i15-2-1]].
[[lem:iii-i14-2-2]] (a), (c), [[lem:iii-i14-2-3]], [[lem:iii-i14-2-4]], [[lem:iii-i14-2-5]], [[thm:iii-i14-3-1]],
[[rem:iii-i14-3-2]], [[lem:iii-j1-1-1]] and [[thm:iii-j1-2-1]] are stated and proved at b = b₀, with derivatives in b
taken at b₀. Their forms at a base point whose black hole parameter is near b₀ are proved in [[ch:s25]];
[[sec:s23-base-points]] states what holds there and where it is proved.

*The inner radius.* Every result of the chapter holds with the inner radius r₀ = r_♭ ∈ (0, ½R₁] of [[def:s12-radii]] as
a parameter, with constants that depend on it. No result names the inner radius: all work on Ω_* = cl_M{t^♭_* ≥ 1}
([[sec:iii-i-1]]) with the spaces of [[ch:s04]], extendible at the inner boundary, and with the theorems of
[[ch:s04]]–[[ch:s10]], which hold at every such radius. The fixed radii used are scale-free ({r ≤ 2}, {r ≥ 1}) or far
out (|x| ≥ 5R₁, |x| ≤ 3R₁), and the levels and windows are fixed by weights at infinity and at K⁺.

*Notation.* For a function a of t_*, a′, a″ and a^(j) are its t_*-derivatives; on parameters and tensors (p⃗′, q′, h′,
W′_ν) a prime marks a second element or a direction of linearisation. The double prime of h″ := h + h_(b,rem)(q)
([[def:iii-i14-1-2]]), and of the metric g″ built from it, marks the augmented background. The black hole parameter is
b = (m, A), with mass m. The rows of the table of roots are written ψ = (μ, τ), as in [[sec:iii-i12-1]]. The number of
levels in the proof of [[thm:iii-i14-3-1]] is written K; it is unrelated to the K of K⁺, χ_K, K_τ and K_ι(λ).

### The coefficients and the augmented operator {#sec:iii-i14-1}

Everything of [[sec:iii-i12-1]], with w_ψ = 3 + η_2 − 2ε − d_ψ, and of [[sec:iii-i13-1]] is kept. α ∈ (4, 4 + ε_K] is
admissible in the sense of [[def:iii-i10-1-3]], where [[thm:iii-i11-4-1]] and [[thm:iii-i12-3-1]] are proved;
[[def:iii-i13-1-1]] serves the intermediate levels. The δ_+ of [[sec:iii-i12-1]] is taken ≤ η_E := min Re ℰ_ind. Then
3 + η_2 + η_E > 3 + ε_+, as η_E ≥ ε_ind > ε_+: the first by the convention for ℰ_ind of [[ch:s13]], with ε_ind the
constant of [[eq:iii-f1-2-2]] as in [[lem:iii-g4-4-3]], the second by [[eq:iii-i9-1-1]]. The class 𝒳 is restricted by
two requirements, [Hin26, Remark 11.64 (2)]. The first is ℰ_+ ⊃ (ℰ_♯ ∪ ℰ^♮) ∩ {Re < 3 + ε_+}, which can be imposed
together with (H1)–(H3) of [[sec:iii-i9-1]], as both sets do not depend on ℰ_+ below 3 + ε_+ ([[lem:iii-i10-1-2]] (b),
as in [[sec:iii-i12-1]]). The second is

    (H5)     a_+ < 3 + η_2.

For a weight w, "order w−" means order w − ε for every ε > 0, and

    Ḣ^(∞,w−)_b := ⋂_ε Ḣ^(∞,w−ε)_b,     𝒴^♮(α−) := ⋂_ε 𝒴^♮(α − ε),

and so on.

**Definition {#def:iii-i14-1-1}** (The coefficients; [Hin26, (11.227)].) For ψ ∈ ℛ′ let

    ℰ^α_ψ := {(z, k) ∈ ℰ_♯ − d_ψ : Re z > 2}   (ψ ≠ v1),     ℰ^α_v1 := ℰ_♯ ∩ {Re > 2}.

The v1 terms of exponent in

    ℳ_rot := ℳ ∪ (ℰ_♯ ∩ {Re = 2}),

which is ℰ_♯ ∩ {Re ≤ 2}, are carried by the rotation rows of [[def:iii-i14-1-3]]. 𝒬 is the real vector space of the
conjugation-symmetric tuples q = (S_rem, b_rem, (Y_ψ)_(ψ∈ℛ′)) with

    S_rem ∈ Ḣ^(∞,(α−2)−)_b([1, ∞]; 𝒮_1),     b_rem ∈ Ḣ^(∞,(α−1)−)_b([1, ∞]; 𝔟),
    Y_ψ ∈ ⋂_(ε>0) Ḣ^(∞,𝒬(ℰ^α_ψ, 3+η_2−2ε−d_ψ))_b([1, ∞]; 𝒴_(ψ,ℂ)).                                     {#eq:iii-i14-1-1}

"q small" means small in one fixed seminorm of large order, at a K⁺-weight a′_K < α − 2 above the level α_1 of Step 1 of
the proof of [[thm:iii-i14-3-1]], so that h + h_rem(q) is small in the class 𝒳^d of [[sec:iii-i8-1]] with a_K = a′_K.
The rate of a polyhomogeneous term t_*^(−z) of Y_ψ is Re z > 2 for ψ ≠ v1; for v1 it is Re z + 1 > 3 at b₀, where
h_(b₀,v1) = 0, and Re z > 2 at a rotating b. So by the gap (G) of [[def:iii-i10-1-3]] (with d_v1 = 0) the rate exceeds
2 + ε_K ≥ α − 2 at every b near b₀.

**Definition {#def:iii-i14-1-2}** (Augmentation; [Hin26, Definition 11.63].) For q ∈ 𝒬 and b near b₀ let

    h_(b,rem)(q) := χ_K( h^(≤1)_(b,s1)(S_rem(t_*)) + ġ_b(b_rem(t_*)) + Σ_(ψ∈ℛ′) T_(ψ,b)(Y_ψ(t_*)) ),   {#eq:iii-i14-1-2}

with the towers T_(ψ,b) of the table of [[sec:iii-g2-1]] for L_b ([[def:iii-g2-2-5]], chosen by [[lem:iii-i14-2-1]]),
with h^(≤2)_(b,v1) for v1, and with ġ_b(ḃ) := ṁ ġ^Υ_b(1, 0) + ġ^Υ_b(0, Ȧ) for ḃ = (ṁ, Ȧ) ([[sec:iii-h-1]]). At b = b₀ it
is the tensor χ_K u_exp of [[eq:iii-i12-3-1]] with the coefficients q. For p⃗ ∈ 𝒫 with black hole parameter b, and h and
q small, put h″ := h + h_(b,rem)(q), the augmented background, and

    P_5(h, p⃗, q) := P_4(h″, p⃗) = P_4(h + h_(b,rem)(q), p⃗)                                          {#eq:iii-i14-1-3}

with P_4 of [[eq:iii-i9-2-3]]. This is [Hin26, (11.228)] with h_(−S) = 0: q and h enter only through h″, both in the
Ricci term and in the gauge term. Since q ↦ h_(b,rem)(q) is linear,

    D_h P_5(h, p⃗, q) = L_(h″,p⃗),     D_q P_5(h, p⃗, q)(q′) = L_(h″,p⃗)(h_(b,rem)(q′)),               {#eq:iii-i14-1-4}

which is [Hin26, (11.231)]. We write

    R_q := L_(h″,p⃗) − L_(h,p⃗),     Δ_q := D_(p⃗)P_5(h, p⃗, q) − D_(p⃗)P_4(h, p⃗).

At b = b₀ we write h_rem(q) := h_(b₀,rem)(q).

**Definition {#def:iii-i14-1-3}** (Rotation rows.) Let 𝒩_rot := {(rot, λ, k) : (λ, k) ∈ ℳ_rot}, with ℳ_rot of
[[def:iii-i14-1-1]], an index set disjoint from the set 𝒩 of rows of [[sec:iii-i9-1]], whose v1 rows keep the
coefficient space 𝒱′ = 0. Each ν ∈ 𝒩_rot carries the coefficient space 𝒱_(1,ℂ) of all rotations. For ν = (rot, λ, k) let
a_ν = r_ν = t_*^(−λ)(log t_*)^k, ω_ν, m_ν, h_ν, ϑ_ν and ϑ_(ν,♯) be those that [[def:iii-i9-2-1]] assigns to the type v1
and the exponent (λ, k), with W ∈ 𝒱_(1,ℂ); [[sec:iii-i10-1]] extends that definition verbatim to every triple. From here
on 𝒫 is the parameter space of [[sec:iii-i9-1]] enlarged by the tuples (W_ν)_(ν∈𝒩_rot), conjugation-symmetric (W_(ν̄) =
W̄_ν, ν̄ := (rot, λ̄, k)), and h_tot(p⃗), ϑ_tot(p⃗) of [[def:iii-i9-2-3]] are summed over the disjoint union 𝒩 ⊔ 𝒩_rot.
So P_4 and P_5 take p⃗ in the enlarged 𝒫, of which the space of [[sec:iii-i9-1]] is the subspace W⃗^rot :=
(W_ν)_(ν∈𝒩_rot) = 0.

At b₀ a rotation row is given the rate Re λ + 1: every rotation is Killing there, so h_v1 = 0, m_ν(W) has K⁺-weight
Re λ + 1 − ε > α − 2 ([[lem:iii-i9-2-2]] (e)), and no level of [[thm:iii-i11-4-1]] or of [[thm:iii-i14-3-1]] eliminates
it; its coordinate is fixed in [[thm:iii-i14-3-1]] by the expansion (Step 4′ of the proof). At a rotating b its rate is
Re λ ([[lem:iii-i15-2-1]]), and the coordinates of the rotation rows are assigned as in [[prop:iii-i15-2-5]]. The
results of [[ch:s21]] and [[ch:s22]] hold with the enlarged 𝒫, except the uniqueness in [[thm:iii-i11-4-1]], which
fails there: the solutions form a graph over W⃗^rot (Step 3 of the proof of [[thm:iii-i14-3-1]]). [[thm:iii-i11-4-1]]
and [[thm:iii-i12-3-1]] are used only with the unknown parameter in the space of [[sec:iii-i9-1]] (the background p⃗
may lie in the enlarged one), the rotation-row terms being part of the right-hand side (Step 4′).

[[lem:iii-i9-2-2]] (a)–(e) and [[lem:iii-i9-2-4]]–[[lem:iii-i9-2-6]] hold for ν ∈ 𝒩_rot, with e_ν = λ and κ_ν = Re λ +
4: their proofs do not use the coefficient space. [[lem:iii-i9-2-2]] (f), the injectivity of h_τ on 𝒲_τ, fails for them,
h_v1 being 0 on 𝒱_1, and is not used for them ([[cor:iii-i10-2-3]] excludes v1). Each h_ν(W) is supported in 𝒞 with
ι⁺-exponents in (λ, k) + ℱ ⊂ ℰ_+, as for the v1 rows (v1, λ, k) of 𝒩, which exist as ℳ_rot ⊂ ℰ_par ([[eq:iii-i10-1-2]]);
here (λ, k) + ℱ ⊂ ℰ_+ is (H3) of [[sec:iii-i9-1]], which holds below 2 by [[eq:iii-i8-1-1]] and ℰ_++ + ℰ_ind ⊂ ℰ_++ ⊂
ℰ_+. So (H3) holds and h_tot(p⃗) ∈ 𝒳^∞. Finally

    f^ν_(h,p⃗)(W) := D_(p⃗)P_4(h, p⃗)(W_ν = W) = L_(h,p⃗) m_ν(W) + r^ν_(h,p⃗)(W)

([[lem:iii-i9-2-6]] (b)–(c)), with r^ν_(h,p⃗) of K⁺-weight Re λ + a_K − ε > α and plain ι⁺-weight Re λ + 2 + λ_♯ − ε >
w_+ ([[lem:iii-i9-2-6]] (c)), so these rows enter the constructions exactly as the rows of 𝒩 do.

### Properties of the augmented operator {#sec:iii-i14-2}

**Lemma {#lem:iii-i14-2-1}** (Towers near b₀.) For b near b₀ the states of the table of [[sec:iii-g2-1]] for L_b and
their companions h̆^((μ),j)_(b,τ) can be chosen smooth in b, equal at b₀ to those of [[sec:iii-g2-1]], with leading
terms at ∂X that do not depend on b; the rotation state h_(b,v1) ∈ 𝒜³ is smooth in b and vanishes at b₀; and ġ_b is
smooth in b. Then ∂_b h̆^((μ),j)_(b,τ)(Y) ∈ 𝒜^((μ−j)+ℰ_ind), and for a = χ_+ t_*^(−z)(log t_*)^k the tensor ∂_b(χ_K
T_(ψ,b)(a)) is polyhomogeneous at ι⁺ with exponents in z + d_ψ + ℰ_ind and, for v1, z + 3; all lie in z + d_ψ plus at
most two increments of Λ ((2, 0) ∈ ℰ_ind, [[sec:iii-i9-1]]).

*Proof.* The pure gauge states and their companions are δ*_(g_b) ω^(≤k)_b with ω^(≤k)_b ∈ ker □^Υ_b polynomial in t_*
and smooth in b ([[prop:iii-d3-3-1]]). By the remark closing [[lem:iii-d3-2-1]] their leading terms at ∂X are the
Minkowski model solutions, which do not depend on b and which (R4) of [[sec:iii-d3-1]] fixes uniquely, no root lying at
μ − k. (The tower relations [[eq:iii-g2-2-1]] alone fix the leading term of a companion only modulo the indicial kernel
at μ − j, [[lem:iii-g2-2-2]]; it is the construction of [[prop:iii-d3-3-1]] that fixes it.) The physical states at −2 (K
= 0) are those of [[prop:iii-f4-5-1]], smooth in b with the b-independent leading term h̄_τ(Y). Composing each family
with the inverse of the smooth invertible map Y ↦ (its leading coefficient), normalised to be the identity at b₀, keeps
everything at b₀, so [[def:iii-i14-1-2]] at b₀ is the tensor χ_K u_exp of [[eq:iii-i12-3-1]]. The corrections lie in
𝒜^((μ−j)+ℰ_ind) with ℰ_ind independent of b ([[sec:iii-g2-2]], [[prop:iii-d3-3-1]], [[prop:iii-f4-5-1]]), so their
b-derivatives do too. The rotation state h_(b,v1)(V) = δ*_(g_b) ω^(−1)_(b,v1)(V) ∈ 𝒜³ vanishes at b₀, where every
rotation is Killing (at a rotating b it need not vanish; nothing below uses that it does not); its b-derivative lies in
𝒜³ and gives the ι⁺-exponent z + 3. ġ^Υ_b is the gauge-corrected derivative of the Myers–Perry family, smooth in b; its
leading term may depend on b (through the mass), which is harmless, b_rem having order (α − 1)−. The statement at ι⁺
follows as in [[sec:iii-i12-1]]: the leading part of T_ψ(a) is homogeneous of degree −z − d_ψ. ∎

**Lemma {#lem:iii-i14-2-2}** (The augmentation; [Hin26, Remark 11.64].) Let q ∈ 𝒬.

(a) At b = b₀, h_rem(q) is real, linear in q, supported in supp χ_K ∩ {t^♭_* ≥ 10}, so away from ℐ⁺, of K⁺-order (α −
2)−, and at ι⁺ partially polyhomogeneous with exponents in ℰ_♯ ∪ ℰ^♮ to the order (3 + η_2)−, of plain weight ≥ λ_♯;
each of its seminorms is bounded by one of q.

(b) For b near b₀, L_b h_(b,rem)(q) has K⁺-order α−, uniformly and smoothly in b.

(c) Let χ̃ ∈ C^∞(M) vanish near K⁺ and equal 1 near supp(1 − χ_K) (a closed set disjoint from a neighbourhood of K⁺).
Then h + χ̃ h_rem(q) ∈ 𝒳^∞, small for (h, q) small.

*Proof.* (a) By [[sec:iii-i12-1]], h^(≤1)_(b₀,s1)(S_rem) has K⁺-order (α − 2)− and ι⁺-order (α + 1)− (h_(b₀,s1) ∈ 𝒜³,
h̆^1_(b₀,s1) ∈ 𝒜²); ġ(b_rem) has K⁺-order (α − 1)− and ι⁺-order (α + 1)− (weights 2 and 3, [[sec:iii-h-1]]). A
polyhomogeneous term t_*^(−z) of Y_ψ gives a K⁺-rate > α − 2 ([[def:iii-i14-1-1]]) and the ι⁺-exponent z + d_ψ ∈ ℰ_♯,
plus the corrections of the profiles, in ℰ^♮; a conormal part of order (3 + η_2 − d_ψ)− gives the ι⁺-order (3 + η_2)−
and a K⁺-order above α − 2. supp χ_K ⊂ {t^♭_* ≥ 10} by [[eq:iii-i-1-2]].

(b) By the tower relations for L_b ([[lem:iii-g2-2-6]]), L_b T_(ψ,b)(Y) consists, near K⁺, of the terms with Y^(k_μ+1)
and Y^(k_μ+2), of K⁺-order at least the rate plus k_μ + 1. This is ≥ λ_♯ + 3 > α for the polyhomogeneous parts and > α
for the conormal ones, as in the proof of [[lem:iii-i12-2-4]]. Next, with L_1 = [L_b, t_*] and
L_2 = ½[[L_b, t_*], t_*] ([[sec:iii-i6-1]]),

    L_b h^(≤1)_(b,s1)(S) = S″(L_2 h_(b,s1) + L_1 h̆^1_(b,s1)) + S‴ L_2 h̆^1_(b,s1),

of K⁺-order (α − 2)− + 2; L_b ġ_b(b_rem) = b_rem′ L_1 ġ_b + b_rem″ L_2 ġ_b, of K⁺-order (α − 1)− + 1; and [L_b, χ_K] is
supported away from K⁺. Smoothness in b holds by [[lem:iii-i14-2-1]].

(c) χ̃ h_rem(q) vanishes near K⁺, near ℐ⁺ and for t_* < 1. By (a), the requirement ℰ_+ ⊃ (ℰ_♯ ∪ ℰ^♮) ∩ {Re < 3 + ε_+} and
(H5), it has the ι⁺-data (ℰ_+, a_+). ∎

**Lemma {#lem:iii-i14-2-3}** (The perturbation.) Let b = b₀ and

    u ∈ ⋂_ε H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,w−ε)_b(Ω_*)^(•,−)

with w > 0 and β′_+ ∈ (3/2 − (δ_♯ − ε_+), 3/2). Then R_q u is supported in supp χ_K, vanishes near ℐ⁺, and lies in
𝒴^0_2(β) for every β < w + α − 2; each seminorm is bounded by C‖q‖ times a seminorm of u, uniformly for (h, p⃗, q)
small.

*Proof.* L_(h″,p⃗) = L^(g″,g_0) with g″ = g_0 + h_tot(p⃗) + h″ ([[lem:iii-i9-2-5]]), and

    R_q = ∫_0^1 ∂_s L^(g_0+h_tot(p⃗)+h+s h_rem(q), g_0) ds.

The coefficients of L^(g,g_0) are smooth functions of g and its first two derivatives (and of g_0), so R_q is a
second-order operator whose coefficients are linear in h_rem(q) and its first two derivatives, times smooth functions;
it is supported in supp χ_K. As in [[eq:iii-i-4-2]] of [[prop:iii-i-4-1]], with h_rem(q) in place of h: at K⁺ the
coefficients have the weight (α − 2)− of h_rem(q) ([[lem:iii-i14-2-2]] (a)), so R_q u has K⁺-weight (w + α − 2)−; at ι⁺
they have weight ≥ λ_♯ and each derivative gives a factor ρ_+, so R_q u has the plain weight β′_+ + 2 + λ_♯ − ε > w_+,
as β′_+ > 3/2 − δ_♯ + ε_+; and near ℐ⁺ it vanishes. These are the requirements of 𝒴^0_2(β) ([[sec:iii-i9-1]],
[[sec:iii-i10-1]]), the ι⁺-index set being void below w_+. ∎

**Lemma {#lem:iii-i14-2-4}** (The parameter derivatives; [Hin26, Lemma 11.65 and Remark 11.64].) At b = b₀, for (h, p⃗,
q) small:

(a) for a row ν and W ∈ 𝒲_(τ,ℂ), Δ_q(W_ν = W) = R_q(h_ν(W)), which has K⁺-order ∞ and plain ι⁺-weight > w_+, and lies in
𝒴^0_2(β) for every β, with norm O(‖q‖|W|);

(b) in the directions S, S^(0)_1, Δ_q takes values in the sections supported in supp χ_K away from K⁺ and ℐ⁺, of plain
ι⁺-weight > w_+, so in every 𝒴^0_2(β), with norm O(‖q‖);

(c) in the direction b, Δ_q(b′) ∈ 𝒴^♮_2(α−) with norm O(‖q‖|b′|); so D_b P_5(h, p⃗, q)(b′) ∈ 𝒴^♮(α−): the linearisation
in b has the full K⁺-order, which is [Hin26, Lemma 11.65].

*Proof.* (a) P_4 depends on W_ν through h_ν(W_ν) in g′ and through ϑ_(ν,♯)(W_ν) in ϑ_tot ([[eq:iii-i9-2-3]]), so

    D_(W_ν)P_5(h, p⃗, q)(W) = L_(h″,p⃗) h_ν(W) + δ*_(g_0,E_C) ϑ_(ν,♯)(W),

and Δ_q = R_q(h_ν(W)). h_ν(W) is supported in 𝒞, whose closure meets ∂M only in a compact subset of (ι⁺)°, and lies in
𝒜^((λ,k)+ℱ) there ([[lem:iii-i9-2-5]]); the argument of [[lem:iii-i14-2-3]] gives the ι⁺-weight ≥ λ_♯ + Re λ + 2 − ε >
w_+.

(b) h_rem(q) does not depend on S, S^(0)_1, so

    Δ_q(S′) = ∫_0^1 (D_S L_(h+s h_rem(q),p⃗))(S′)(h_rem(q)) ds,

where D_S L is the derivative of L^(g″,g_0) in S through g_0 and h_tot(p⃗). By [[eq:iii-i7-1-3]] g_0 depends on S,
S^(0)_1 only on supp(1 − χ_K), and the terms of h_tot that depend on them are supported in 𝒞 ([[lem:iii-i7-2-2]]). Their
derivatives have ι⁺-order ≥ 2: ∂_S g_(p⃗) ∈ ρ_+² C^∞ near (ι⁺)° ([[lem:iii-i7-1-3]] (c)), and h^(0)_s1(S) ∈ 𝒜^(𝒢+1)
([[lem:iii-i7-2-2]]). So Δ_q(S′) is supported in supp χ_K ∩ (supp(1 − χ_K) ∪ cl 𝒞), whose closure meets ∂M only in
(ι⁺)°, with ι⁺-weight ≥ 2 + λ_♯ + 2 − ε > w_+.

(c) On the interior of χ_K⁻¹(1), a neighbourhood of K⁺, g_0 = g_b and h_tot(p⃗) consists of terms supported in 𝒞, and
near K⁺

    P_5(h, p⃗, q) − P_4(h, p⃗) = ∫_0^1 L_(h+s h_(b,rem)(q),p⃗)(h_(b,rem)(q)) ds
                             = L_b h_(b,rem)(q) + ∫_0^1 (L_(h+s h_(b,rem)(q),p⃗) − L_b)(h_(b,rem)(q)) ds,

L_b being the linearisation at g_b. The second term has coefficients of K⁺-order (α − 2)− (h has a_K ≥ 4 + ε_K, h_rem
has (α − 2)−, and the 𝒞-terms vanish near K⁺), applied to a tensor of K⁺-order (α − 2)−, so it has K⁺-order (2α − 4)−,
above α as α > 4. The first has K⁺-order α− by [[lem:iii-i14-2-2]] (b), uniformly and smoothly in b, so its b-derivative
has K⁺-order α−. Near K⁺, L_(h+s h_(b,rem)(q),p⃗) = L^(g_b+h+s h_(b,rem)(q),g_b), so, as in the proof of
[[lem:iii-i14-2-3]], the coefficients of L_(h+s h_(b,rem)(q),p⃗) − L_b are linear in h + s h_(b,rem)(q) and its first two
derivatives, times smooth functions of g_b and of h + s h_(b,rem)(q). So the b-derivative of the second term at b₀ is a
sum of two kinds of products. The first kind are products of a factor of K⁺-order (α − 2)− (from h_(b₀,rem)(q), or from
h, of order α−) with ∂_b h_(b,rem)(q)b′. The second kind, from the dependence of the coefficients on g_b, are products
of ∂_b g_b(b′) with two such factors: one from the coefficients, which keep their factor h + s h_(b₀,rem)(q), and the
argument h_(b₀,rem)(q). Now ∂_b h_(b,rem)(q)b′ has K⁺-order ≥ 2 − ε. Indeed every coefficient of q has rate > 2 at
every b near b₀ ([[def:iii-i14-1-1]]: Re z > 2 for ψ ≠ v1 and for v1, whose state h_(b,v1) gives the rate Re z once b
rotates; the conormal parts have rate > 3; S_rem and b_rem the rates (α − 2)− and (α − 1)−), and the states are smooth
in b ([[lem:iii-i14-2-1]]). So the products of the first kind have K⁺-order ≥ (α − 2)− + 2 = α−; and those of the
second kind, ∂_b g_b(b′) being stationary, have K⁺-order (2α − 4)− > α. This is the argument of [Hin26], with one
change: a v1 coefficient of exponent z ∈ ℳ would give only (α − 2 + Re z)− < α, which is why those terms are carried by
the rotation rows ([[def:iii-i14-1-3]]). The v1 terms of real part 2 are carried there too, for [[eq:iii-j-2-5]], where
their square at a rotating b would have the K⁺-order 4 only.

Away from K⁺, Δ_q(b′) is supported in supp χ_K, away from ℐ⁺, and is

    ∫_0^1 ( (∂_b L)(b′) h_(b₀,rem)(q) + L(∂_b h_(b,rem)(q)b′) ) ds

up to terms quadratic in h_rem. Here ∂_b L has coefficients of ι⁺-order ≥ 2 (∂_b g_b, of weight 2, [[sec:iii-h-1]];
h^(0)(ḃ) ∈ 𝒜^𝒢, [[lem:iii-i7-2-2]]), giving the plain weight ≥ 2 + λ_♯ + 2 − ε > w_+. And ∂_b h_(b,rem)(q) has the
ι⁺-exponents of [[lem:iii-i14-2-1]], in ℰ^♮; below 2 they lie in ℳ, since there ℰ_♯ is ℳ ([[sec:iii-i12-1]]) and ℳ +
ℰ_ind stays in ℳ below 2. L maps these to the exponents ℰ^♮ + 2, the expansion of L at ι⁺ adding elements of ℰ^ι_ind,
which are increments of Λ. The conormal parts of ∂_b h_(b,rem)(q) are the b-derivatives of T_(ψ,b)(Y^c_ψ) for the rows
with μ_ψ ∈ (−1, 0] (Step 4 of the proof of [[thm:iii-i12-3-1]]), of ι⁺-order (3 + η_2 + η_E)− by [[lem:iii-i14-2-1]]
(the leading terms do not depend on b, and the corrections lie η_E further), which L maps to the weight (5 + η_2 +
η_E)− > w_+ ([[sec:iii-i14-1]]); and those of S_rem, b_rem, of ι⁺-order (α + 3)−. The terms quadratic in h_rem are as in
[[lem:iii-i14-2-3]]. ∎

**Lemma {#lem:iii-i14-2-5}** (Sources of order α−; the losses.) [[prop:iii-i11-3-1]], [[lem:iii-i11-3-2]] and
[[thm:iii-i11-4-1]], [[thm:iii-i12-3-1]], and [[prop:iii-i13-2-1]] and [[lem:iii-i13-2-2]] at the level α, hold for
sources in 𝒴^♮(α−), with the same conclusions. The decomposition [[eq:iii-i12-3-1]] of [[thm:iii-i12-3-1]] can be taken
independent of ε, so that its coefficients lie in the classes [[eq:iii-i12-3-2]] and ũ in [[eq:iii-i12-3-3]] for every
ε > 0 at once.

*Proof.* The conclusions are statements for every small ε > 0. The K⁺-weight of the right-hand side enters the
constructions only through [[lem:iii-i2-4-1]] and [[prop:iii-a-4-2]] (1) with β_K = α − ε (Step 0 of the proof of
[[prop:iii-i11-3-1]]), through Step 0 of the expansion lemmas (f′ of K⁺-weight α − ε), and through the zf-weights α − 1
− j − ε of the Taylor levels. A right-hand side of K⁺-weight α − ε′ for every ε′ > 0 meets each of these for every ε.

For the independence, fix ε̄ > 0 such that no exponent at hand (of the coefficients of the pieces and of the rows) has
real part in [α − 2 − 3ε̄, α − 2) ∪ [α − ε̄, α); there are finitely many below every bound, and none at α − 2 or α by
admissibility. For ε < ε̄ the constructions do not depend on ε. The zero-energy solves, [[prop:iii-g4-4-4]] and
[[prop:iii-g4-5-1]] and the inversion at the last level are applied to the same sources: the thresholds 2 + η_1, 2 + η_2
and δ are fixed; the rounds of the loop at level 3 stop when τ > α − 2; and ε enters only the weights in which their
outputs are estimated. The pairs removed in [[lem:iii-i12-2-4]] with β = α − ε are those of real part below α − ε̄, and
the exponents dropped in its Step 2 have zero coefficients. The construction at level 3 depends on ε also through the
weights τ_i(ε) = 1 + η_2 + iε_ind − (2 + i)ε, the switch α_τ = min(τ, 2 − δ) (δ fixed independent of ε), the order μ_3 =
τ − ε of the expansions recorded in the zero-energy solve, and the lowering of τ in Step 4 of the proof of
[[prop:iii-i11-3-1]]. We take ε̄ so small that, for ε < ε̄, none of these crosses an exponent at hand, a root, or a
value excluded in [[prop:iii-g4-5-1]]: each is affine in ε with nonzero slope, so it crosses each of the finitely many
thresholds at most once. [[prop:iii-g4-5-1]] solves [[eq:iii-g4-5-3]] by Mellin inversion on Re λ = α_τ − 2 − j, and
moving that line without crossing a root does not change the solution; the recorded expansions and the switch are then
the same for every ε < ε̄. So the pieces, the coefficients of [[eq:iii-i12-3-1]] and ũ are the same for every ε < ε̄,
and the estimates hold for each. ∎

### The decay of forward solutions {#sec:iii-i14-3}

**Theorem {#thm:iii-i14-3-1}** ([Hin26, Corollary 11.66] in dimension 4 + 1.) Let h ∈ 𝒳^∞, p⃗ ∈ 𝒫 (b = b₀) and q ∈ 𝒬 be
small, and F ∈ 𝒴^♮(α−). There is a unique p⃗′ ∈ 𝒫 (rotation rows included, [[def:iii-i14-1-3]]) such that the forward
solution u of

    L_(h+h_rem(q),p⃗) u = F − D_(p⃗)P_5(h, p⃗, q)(p⃗′)                                                 {#eq:iii-i14-3-1}

satisfies [[eq:iii-i11-4-2]]:

    u ∈ ⋂_ε H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α−2−ε)_b(Ω_*)^(•,−)     for every β_+ < min(3/2, min Re ℰ_+),

and u = h_rem(q′) + h′ with q′ ∈ 𝒬 (so the v1 coefficient has no term of exponent in ℳ_rot) and

    h′ ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_♯,3+η_2−2ε),α−ε)_b(Ω_*)^(•,−),
    D_h P_5(h, p⃗, q)(h′) = F − D_(p⃗)P_5(h, p⃗, q)(p⃗′) − D_q P_5(h, p⃗, q)(q′).                      {#eq:iii-i14-3-2}

p⃗′, q′ and h′ are linear in F, with bounds uniform for (h, p⃗, q) small.

*Proof.* Write u(p⃗′) for the forward solution of [[eq:iii-i14-3-1]], and 𝒵_β for the space of [[eq:iii-i11-4-2]] at the
level β, or of [[eq:iii-i8-4-2]] for β < 3.

*Step 0 (the forward solution).* L_(h+h_rem(q),p⃗) = L^(g″,g_0) is a wave operator with smooth coefficients, close to
L_(h,p⃗) in every C^k on every slab Ω_(1,T_1). [[prop:ii-e-3-4]] gives a unique forward solution on each slab, as for
L_(h,p⃗) ([[lem:iii-i9-2-4]]), and these agree. So u(p⃗′) exists, is smooth, and is affine in p⃗′.

*Step 1 (the base level, at h + h_rem(q)).* Fix an admissible α_1 ∈ (2, α − 2) in the sense of [[sec:iii-i8-1]]. The
hypotheses of [[prop:iii-i8-4-1]] on the background ask for K⁺-order only above α_1 (α_1 < min(a_K, 3) there;
[[lem:iii-i8-3-1]] and [[lem:iii-i8-3-2]] take steps below a_K − 2), so they hold for h + h_rem(q), which has K⁺-order
(α − 2)− and the other data of 𝒳 ([[lem:iii-i14-2-2]] (a), (c)). Split p⃗′ = p⃗′_< ⊕ W⃗ with p⃗′_< ∈ 𝒫_(α_1)
([[sec:iii-i11-4]]) and W⃗ = (W_ν)_(ν∈𝒩′⊔𝒩_rot). As in the proof of [[thm:iii-i11-4-1]] (its paragraph on
[[prop:iii-i8-4-1]] for P_4), [[prop:iii-i8-4-1]] holds for P_5 at (h, p⃗, q). Indeed P_5 is P_3 at (h + h_rem(q) + Σ_ν
h_ν(W_ν), p⃗_3), the sum over the rows other than the motions (the rotation rows included), up to the term
(∂δ*_(g_0,E_C))ϑ_rows, and in the direction b also up to L(∂_b h_(b,rem)(q)b′). This last term has K⁺-order > 2 + ε_K >
α_1: every coefficient of q has rate > 2 + ε_K at b₀, by (G) and [[def:iii-i14-1-1]], and L̂_(b₀)(0)∂_b h_(b,v1) = 0 as
h_(b₀,v1) = 0, so the v1 part has rate ≥ 3. All these terms lie in the class 𝒴(α_1) of [[sec:iii-i8-1]] and are O(|W⃗| +
‖q‖); so do D_(W⃗)P_5 = D_(W⃗)P_4 + Δ_q ([[lem:iii-i14-2-4]] (a); [[lem:iii-i9-2-6]] (b)) and F (the last sentence of
[[lem:iii-i13-2-2]]). So for every W⃗ there is a unique p⃗′_<(W⃗) ∈ 𝒫_(α_1), affine in W⃗, with u(p⃗′_<(W⃗) ⊕ W⃗) ∈
𝒵_(α_1). Let 𝒫_0 be the set of these p⃗′: the graph of W⃗ ↦ p⃗′_<(W⃗).

*Step 2 (one level).* Choose admissible levels α_1 = β_0 < β_1 < ⋯ < β_K = α ([[sec:iii-i8-1]] below 3,
[[def:iii-i13-1-1]] above 3) with β_(k+1) − β_k < α − 4 and β_(K−1) > 4; this is possible as the admissible levels are
dense. Let p⃗′ ∈ 𝒫 with u := u(p⃗′) ∈ 𝒵_(β_k). By [[eq:iii-i14-3-1]],

    L_(h,p⃗) u = G̃ − D_(p⃗)P_4(h, p⃗)(p⃗′),     G̃ := F − Δ_q(p⃗′) − R_q u,                           {#eq:iii-i14-3-3}

and G̃ ∈ 𝒴^♮(β_(k+1)), resp. 𝒴^♮(α−) for k + 1 = K. Indeed R_q u ∈ 𝒴^0_2(β) for β < β_k + α − 4 ([[lem:iii-i14-2-3]]
with w = β_k − 2; for k = K − 1, β_(K−1) + α − 4 > α), and Δ_q(p⃗′) ∈ 𝒴^♮(α−) ([[lem:iii-i14-2-4]]). The rows enter
[[eq:iii-i14-3-3]] through D_(p⃗)P_4 at h, whose defects r^ν_(h,p⃗) have the orders of [[lem:iii-i9-2-6]] (c), as a_K ≥
4 + ε_K. At h + h_rem(q) the row directions differ from these by exactly Δ_q(W⃗) = R_q(h_ν(W⃗)) ([[lem:iii-i14-2-4]]
(a)), supported in 𝒞, so no row defect of the background h + h_rem(q) enters. For β_(k+1) > 3, u_0 := u + Σ_(ν∈𝒩⊔𝒩_rot)
m_ν(W′_ν), with W′_ν the row components of p⃗′ (the motions and the rotation rows included), solves L_(h,p⃗) u_0 = G′,
where

    G′ := G̃ − f^S_(h,p⃗)(S′) − f^b_(h,p⃗)(b′) − f^s1_(h,p⃗)(S^(0)′_1) − Σ_(ν∈𝒩⊔𝒩_rot) r^ν_(h,p⃗)(W′_ν)

lies in 𝒴^♮(β_(k+1)) ([[lem:iii-i9-2-6]] (a), (c); [[sec:iii-i10-1]]), resp. in 𝒴^♮(α−) for k + 1 = K; and u_0 has
K⁺-weight min(β_k − 2, λ_♯ − 1) − ε > 0, with min(β_k − 2, λ_♯ − 1) + a_K > β_(k+1), and ι⁺-weight β′_+.
[[lem:iii-i13-2-2]] (with [[lem:iii-i14-2-5]] for k + 1 = K) gives

    u = Σ_(ν∈𝒩_(β_(k+1))) m_ν(C^(k+1)_ν(p⃗′)) + ũ,     ũ ∈ 𝒵_(β_(k+1)),
    C^(k+1)_ν(p⃗′) := S^(h,p⃗,β_(k+1))_ν(G′) − W′_ν,                                                   {#eq:iii-i14-3-4}

the m_ν(W′_ν) of the rows outside 𝒩_(β_(k+1)) and of the rotation rows, of K⁺-weight above β_(k+1) − 2
([[def:iii-i14-1-3]]), being part of ũ. For β_(k+1) < 3, [[lem:iii-i8-3-2]], transferred to P_4 as in Step 1, with
β_(k+1) − β_k < a_K − 2, applied to u gives [[eq:iii-i14-3-4]] with the motion rows of ℳ_(β_(k+1)) ∖ ℳ_(β_k) and
C^(k+1)_ν the K⁺-coefficient S_(λ,k) of u. In both cases the coefficients of the rows of 𝒩_(β_k) vanish
([[cor:iii-i10-2-3]], as u ∈ 𝒵_(β_k)), and u ∈ 𝒵_(β_(k+1)) if and only if C^(k+1)_ν(p⃗′) = 0 for the rows ν of rate in
[β_k − 2, β_(k+1) − 2), the *new rows* of the level.

*Step 3 (the elimination, level by level).* Let 𝒫_k := {p⃗′ ∈ 𝒫_0 : u(p⃗′) ∈ 𝒵_(β_k)}. We show by induction that 𝒫_k is
the graph of an affine map from the coordinates W_ν of the rows of rate ≥ β_k − 2 to the others. For k = 0 this is
Step 1. On 𝒫_k, C^(k+1) is an affine function of the free coordinates; we claim that in the coordinates of the new rows
it is −id + A_k, with A_k → 0 as (h, p⃗, q) → (0, 0, 0). At the base point, D_(p⃗)P_4(0, 0)(W_ν = W) = L_(b₀) m_ν(W)
([[lem:iii-i9-2-4]]), Δ_q = 0 and R_q = 0, so u(p⃗′) = u_F − Σ_ν m_ν(W_ν), with u_F the forward solution of L_(b₀) u_F =
F − D_(p⃗)P_4(0, 0)(p⃗′_<); and p⃗′_<, and the coordinates fixed at the earlier levels, do not depend on the coordinates
of rows of higher rate, as m_ν(W_ν) has no K⁺-coefficient at lower rows (as in the proof of [[thm:iii-i11-4-1]], at (0,
0)). So C^(k+1)_ν = C^(k+1)_ν(0) − W_ν there. Near the base point, C^(k+1) depends continuously on (h, p⃗, q), uniformly
for p⃗′ bounded: by [[prop:iii-i8-4-1]] (ii) and [[lem:iii-i8-3-3]] (the levels below 3), [[lem:iii-i13-2-3]] and
[[lem:iii-i11-3-3]] for the coefficients, [[lem:iii-i9-2-6]] for the r^ν, and [[lem:iii-i14-2-3]]–[[lem:iii-i14-2-4]]
for R_q and Δ_q, which are O(‖q‖); and u(p⃗′) is bounded in 𝒵_(β_k) on bounded subsets of 𝒫_k by the induction (finitely
many levels, each losing finitely many derivatives). So −id + A_k is invertible for (h, p⃗, q) small, and C^(k+1) = 0 on
𝒫_k solves for the new coordinates as an affine function of those of higher rate: 𝒫_(k+1) is a graph. At k = K the free
coordinates left are those of the rotation rows (𝒩_α = 𝒩; a rotation row is a new row at no level, its rate Re λ + 1
exceeding α − 2, [[def:iii-i14-1-3]]): 𝒫_K is the graph of an affine map W⃗^rot ↦ p⃗′(W⃗^rot). *Uniqueness:* if u(p⃗″) ∈
𝒵_α, then u(p⃗″) ∈ 𝒵_(β_k) for all k, so p⃗″ ∈ 𝒫_0 by the uniqueness in Step 1 and then p⃗″ ∈ 𝒫_K; Step 4′ fixes the
rotation coordinates.

*Step 4′ (the rotation coordinates).* For p⃗′ ∈ 𝒫_K split p⃗′ = p⃗′_0 ⊕ W⃗′^rot, with p⃗′_0 in the parameter space of
[[sec:iii-i9-1]] ([[def:iii-i14-1-3]]), and put

    G̃_0 := G̃ − Σ_(ν∈𝒩_rot) f^ν_(h,p⃗)(W′_ν),     so that
    L_(h,p⃗) u = G̃_0 − D_(p⃗)P_4(h, p⃗)(p⃗′_0)                                                        {#eq:iii-i14-3-5}

by [[eq:iii-i14-3-3]], D_(p⃗)P_4(h, p⃗) being linear. G̃_0 ∈ 𝒴^♮(α−), as f^ν_(h,p⃗)(W) ∈ 𝒴_2(α) ([[lem:iii-i9-2-6]] (b),
[[def:iii-i14-1-3]]). So u = u(p⃗′) ∈ 𝒵_α solves [[eq:iii-i14-3-5]], whose parameter p⃗′_0 lies in the parameter space
of [[sec:iii-i9-1]]. By the uniqueness in [[thm:iii-i11-4-1]] ([[lem:iii-i14-2-5]]), p⃗′_0 = p⃗′_(h,p⃗)(G̃_0), and
[[thm:iii-i12-3-1]] ([[lem:iii-i14-2-5]], [[prop:iii-i13-2-4]]) applies with F = G̃_0: u = χ_K u_exp + ũ, with ũ of
K⁺-order α− ([[eq:iii-i12-3-3]]). Let C^rot(p⃗′) be the tuple of the polyhomogeneous coefficients, at the exponents in
ℳ_rot, of the v1 coefficient Ẏ_v1 of u_exp.

*The coefficients are determined by u.* Let ℋ_st be the finite-dimensional space of the stationary tensors

    Σ_ψ h̆^((μ_ψ),0)_(b₀,τ_ψ)(Y_ψ) + h̆^1_(b₀,v1)(V) + ġ(ḃ) + h_(b₀,s1)(S)

of [[lem:iii-i12-2-3]] (a), the sum over the rows of ℛ′ other than v1, whose coefficients are unique. Each nonzero
element of ℋ_st is nonzero on an open set, so, the unit sphere of ℋ_st being compact, there is a compact set Z_0 in the
interior of X on which restriction is injective on ℋ_st, and there are continuous linear functionals on C⁰(Z_0) that
return the coefficients; let ℓ be the one returning V. On Z_0, for t_* large, χ_K u_exp is the element of ℋ_st with the
coefficients Ẏ_ψ, Ẏ_v1′, ḃ_rem, Ṡ_rem at t_*, plus the higher terms of the towers, whose coefficients are
t_*-derivatives of these (the v1 bottom is h_(b₀,v1) = 0, and Ẏ_v1 enters through h̆^1_(b₀,v1)(Ẏ_v1′)). Suppose u has
two such expansions with remainders of K⁺-order α−, and let ΔẎ_v1, ΔṠ_rem, … be the differences of their coefficients.
Then ℓ applied to the difference of the expansions gives (ΔẎ_v1)′ plus terms O(t_*^(−3−δ′)), with δ′ := ½ min(ε_K, α
− 4) > 0. The bottoms are removed by ℓ exactly, and what remains is: the remainders (K⁺-order α − ε > 3 + δ′); the
derivatives of ΔṠ_rem and Δḃ_rem (order (α − 1)−) and of the other coefficients (rate > 2 + ε_K: every term of χ_K u_exp
has K⁺-order ≥ α − 2 − ε by [[thm:iii-i12-3-1]], and (G)); and the second derivative of ΔẎ_v1 (order ≥ Re λ + 2 ≥ λ_♯ +
2 > 3 + δ′ at the exponents of ℳ_rot, > 4 at the others). The derivative of ΔẎ_v1 at its exponents of real part > 2,
hence > 2 + ε_K, is also O(t_*^(−3−δ′)), while at (λ, k) ∈ ℳ_rot it is triangular in the log power with diagonal −λ ≠ 0
and has rate Re λ + 1 ≤ 3. As the functions t_*^(−λ−1)(log t_*)^k with Re λ + 1 ≤ 3 are linearly independent modulo
O(t_*^(−3−δ′)), the coefficients of ΔẎ_v1 at ℳ_rot vanish. So C^rot is determined by u, and it is an affine function of
W⃗′^rot, as u is on 𝒫_K.

*The derivative and continuity.* At (0, 0, 0), u = u_F − Σ_ν m_ν(W_ν) (Step 3), where u_F and the m_ν(W_ν) with ν ∉
𝒩_rot do not depend on W⃗′^rot (Step 3). For ν = (rot, λ, k), m_ν(W) is χ_K T_v1(t_*^(−λ)(log t_*)^k W) up to K⁺-order ≥
Re λ + 3 − ε > α: by [[lem:iii-i10-2-1]] (a) and the argument of its part (b) for v1, the terms i ≤ 2 of Σ_i a_ν^(i)
h̆^i_v1(W) are the v1 tower of [[def:iii-g2-2-5]] at b₀, both being δ*_(g_(b₀)) of the polynomial gauge 1-forms of
[[prop:iii-d3-3-1]] (3), with h̆^0_v1 = h_(b₀,v1) = 0; the term i = 3 and the dt_*-term have K⁺-order ≥ Re λ + 3 − ε
([[eq:iii-i10-2-1]]). Its v1 coefficient is t_*^(−λ)(log t_*)^k W. So C^rot has derivative −id in W⃗′^rot at (0, 0, 0).

Near the base point C^rot tends to its value there, uniformly for W⃗′^rot bounded, by the argument of
[[lem:iii-i11-3-3]]. Let u_(0) be the solution at (0, 0, 0) with the same W⃗′^rot, and F_tot, F_(tot,(0)) the right
sides of [[eq:iii-i14-3-5]] for u and u_(0). Then u − u_(0) is the forward solution of

    L_(b₀)(u − u_(0)) = R := F_tot − F_(tot,(0)) − (L_(h,p⃗) − L_(b₀))u,

and R tends to 0 in 𝒴^♮(α−): by the lemmas of Step 3, by which the coordinates of 𝒫_K over W⃗′^rot tend to those at the
base point, and by the count of [[lem:iii-i11-3-3]] for the last term. As u − u_(0) ∈ 𝒵_α, its parameter at (0, 0) is 0
(the uniqueness in [[thm:iii-i11-4-1]]), and [[thm:iii-i12-3-1]] at (0, 0), with [[prop:iii-i10-3-1]] for the exponents
below 2, bounds its coefficients by R. By the uniqueness just shown, the coefficients of u are those of u_(0) plus those
of u − u_(0). Hence for (h, p⃗, q) small there is a unique W⃗′^rot with C^rot = 0, and this fixes p⃗′.

*Step 4 (the expansion).* With p⃗′ of Step 4′, u ∈ 𝒵_α solves [[eq:iii-i14-3-5]] with p⃗′_0 = p⃗′_(h,p⃗)(G̃_0) and G̃_0
∈ 𝒴^♮(α−), and R_q u has K⁺-weight (2α − 4)−. [[thm:iii-i12-3-1]] with F = G̃_0 (Step 4′) gives u = χ_K u_exp + ũ, with
a decomposition independent of ε. Its coefficients q′ := (Ṡ_rem, ḃ_rem, (Ẏ_ψ)) lie in 𝒬. They lie in the classes
[[eq:iii-i12-3-2]] for every ε. Every term of χ_K u_exp has K⁺-order ≥ α − 2 − ε, so the polyhomogeneous coefficients of
rate ≤ 2 < α − 2 − ε vanish, which is the condition Re z > 2 of [[def:iii-i14-1-1]]; and Ẏ_v1 has no exponent in ℳ_rot
(Step 4′), which is its ℰ^α_v1. Conjugation symmetry holds by Step 6 of the proof of [[thm:iii-i12-3-1]]. Put h′ := ũ,
which satisfies the first statement of [[eq:iii-i14-3-2]] by [[eq:iii-i12-3-3]]. As χ_K u_exp = h_rem(q′)
([[def:iii-i14-1-2]] at b₀), [[eq:iii-i14-1-4]] gives

    D_h P_5(h′) + D_q P_5(q′) = L_(h+h_rem(q),p⃗)(h′ + h_rem(q′)) = L_(h+h_rem(q),p⃗) u,

which is [[eq:iii-i14-3-2]] by [[eq:iii-i14-3-1]]. *Linearity and bounds:* every map used is linear and bounded,
uniformly for (h, p⃗, q) small, and the inverses (−id + A_k)⁻¹ are bounded. ∎

**Remark {#rem:iii-i14-3-2}** (Orders; [Hin26, Remark 11.64 (1)] and the sentence after [Hin26, Corollary 11.66].) (1)
*The background.* h + h_rem(q) has K⁺-order (α − 2)− only, against a_K ≥ 4 + ε_K for h; [[thm:iii-i14-3-1]] never uses
the linear theory at it beyond the levels of [[ch:s21]] below α − 2 (Step 1), which ask no more.

(2) *The class reproduces.* h′ has the ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I), the ι⁺-data (ℰ_♯, (3 + η_2)−) and the K⁺-order α−. This
is the class of h if (H2) of [[sec:iii-i9-1]] is read as "K⁺-order α−" with α ≤ 4 + ε_K the level used, a_I = ℓ_I (off
the exclusion sets of (H4) of [[sec:iii-i10-1]]), and a_+ < 3 + η_2 by (H5). Every use of a_K in [[ch:s21]] and
[[ch:s22]] is a strict inequality at an admissible level, or the membership of f^b_(h,p⃗) in 𝒴_2(α) ([[lem:iii-i9-2-6]]
(a)), which becomes 𝒴_2(α−) and is accepted by [[lem:iii-i14-2-5]]. So [[thm:iii-i14-3-1]] proves for h′ the decay at
ℐ⁺, ι⁺ and K⁺ that it assumes of h, as [Hin26, Corollary 11.66] does.

(3) *Nonlinear errors.* As in [Hin26], P_5(h, p⃗, q) for general small (h, p⃗, q) is not of the class of F; the
parameterisation that accounts for this is [[sec:iii-j-1]]–[[sec:iii-j-2]].

### The data space {#sec:iii-j-1}

Everything of [[sec:iii-i14-1]] is kept, and through it everything of [[ch:s21]] and [[ch:s22]]: α, the constants 0 <
ε_K < ε_+ < min(δ_♯, ε_ind) of [[eq:iii-i9-1-1]], w_+ = 5 + ε_+, η_2, (H1)–(H5), (C5), (G), Λ, k̄(λ), k̄_0, l_*, J_*,
ℰ_par, ℰ_♯, ℳ, ℰ_++, 𝒢 = (2, 0) ∪ (2 + ℰ_ind), ℱ = (0, 0) ∪ ℰ_ind, the rows 𝒩 with the rotation rows 𝒩_rot and the
enlarged 𝒫, the towers T_(ψ,b), ℛ, ℛ′, d_ψ, k_μ, 𝒬, h_(b,rem)(q) and P_5. The black hole parameter b ranges near b₀, and
p⃗_(≤0) = (S, b − b₀, S^(0)_1), with g_0 = g_(p⃗_(≤0)) ([[eq:iii-i7-1-3]]). From [[ch:s17]]: the spaces
[[eq:iii-g3-1-2]]–[[eq:iii-g3-3-5]], the inverse [[eq:iii-g3-2-2]] of N_(ι⁺)(L̄, ·) on partially polyhomogeneous spaces,
spec^(<ℓ_I)_(ι⁺)(L̄, ℰ^C_I), [[cor:iii-g3-3-1]], Res^k_(ι⁺)(L̄, ℰ^C_I, λ), Res_(ι⁺)(L̄, λ) and the map
[[eq:iii-g3-3-6]]. ℓ_I is the one of the class, with ℓ_I > 3 + ε_+ ((H4) of [[sec:iii-i10-1]]), and [[eq:iii-g3-1-2]]
holds, s_C being large by (C1). K_ι(λ) denotes the order of the pole of [[eq:iii-g3-2-2]] at λ, as in
[[prop:iii-g3-3-7]]. Also from [[ch:s17]]: the table of [[sec:iii-g2-1]], the Minkowski formal solutions
([[def:iii-g2-2-3]]), [[thm:iii-g2-3-1]] and [[lem:iii-g2-4-1]]. Two further conditions are imposed, each removing
finitely many values.

**Definition {#def:iii-j-g-plus}** (The condition (G⁺).) (G⁺) *No λ ∈ Λ has real part in (3, 3 + ε_+].* Λ does not
depend on the constants ([[lem:iii-i10-1-2]] (a)), so (G⁺) holds after decreasing ε_+ (with ε_K, η_1, η_2). Every
statement of [[ch:s21]], [[ch:s22]] and [[sec:iii-i14-1]]–[[sec:iii-i14-3]] holds for the smaller values
([[eq:iii-i9-1-1]]), the choices of η_1, η_2, δ_+ and α in [[sec:iii-i10-1]]–[[sec:iii-i14-1]] being made again.

**Definition {#def:iii-j-a-j}** (The condition (A_J).) (A_J) *For every λ₀ ∈ Λ with Re λ₀ < 3 + ε_+, the number ℓ_K(λ₀)
:= α − Re λ₀ is not −Re μ for a root μ of L̂_(b₀)(0), and is not in Re π_1ℰ_K.* Then ℓ_K(λ₀) ∈ (α − 3 − ε_+,
α − λ_♯] ⊂ (0, 3), as ε_+ < δ_♯ < ¼ ([[eq:iii-i9-1-1]]), so ℓ_K(λ₀) is admissible in [[sec:iii-g3-1]] (ℓ^max_K = 3
under (C5), [[sec:iii-g2-1]]). The admissible α meeting (A_J) are dense in (4 + ε_K − ε′_0, 4 + ε_K] (ε′_0 of
[[def:iii-i10-1-3]]).

**Definition {#def:iii-j-classes}** (The classes.) For k ∈ ℕ_0 ∪ {∞}, with the orders read as "w−" ([[sec:iii-i14-1]]),

    𝒳^k_J := H^(k,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_+,(3+ε_+)−),α−)_b(Ω_*; S²T*)^(•,−),
    ℱ^k := H^(k,(⟨ℰ^C_I+1⟩′,ℓ_I+1),(5+ε_+)−,α−)_b(Ω_*; S²T*)^(•,−),

the latter with a plain weight at ι⁺; and 𝒬^k_J is the space of tuples (S_rem, b_rem, (Y_ψ)_(ψ∈ℛ′)) with S_rem ∈
Ḣ^(k,(α−2)−)_b, b_rem ∈ Ḣ^(k,(α−1)−)_b and Y_ψ ∈ Ḣ^(k,𝒬(ℰ^α_ψ,(3+ε_+−d_ψ)−))_b. Here ℰ_+ is as in [[sec:iii-i14-1]]; it
contains ℰ_♯ ∩ {Re < 3 + ε_+}. Since 3 + ε_+ > 3 + η_2, 𝒬^∞_J ⊂ 𝒬; and 𝒳^∞_J is the class of [[sec:iii-i14-1]] with a_+
= (3 + ε_+)− in place of (H5). The class used by [[thm:iii-i14-3-1]] is related to these in [[lem:iii-j1-1-1]].

**Definition {#def:iii-j-terms}** (Terms at ι⁺.) A tensor w on Ω_* that is partially polyhomogeneous at ι⁺ has terms
t_*^(−λ)(log t_*)^k w_(λ,k)(R, ω), quasi-homogeneous in the coordinates (t_*, R, ω) near ι⁺. We write

    [w]_λ := Σ_k t_*^(−λ)(log t_*)^k w_(λ,k)

for its *t_*^(−λ)-term*. A term t_*^(−λ−2)(log t_*)^k f of a right-hand side is at the *u-exponent* λ, so [f]_(λ+2) is
the part of u-exponent λ.

By [[lem:iii-g2-4-1]], [L_b w]_(λ+2) = L̄[w]_λ when [w]_(λ′) = 0 for Re λ′ ≤ Re λ − 2; here 2L̄(t_*^(−λ)w) =
t_*^(−λ−2)N_(ι⁺)(λ)w, and the cut-off region {|x| ≤ 3R₁} of [[lem:iii-g2-4-1]] lies, near ι⁺, in every neighbourhood of
K⁺, where orders are K⁺-orders.

**Definition {#def:iii-j-1-1}** (The data space; [Hin26, Definition 12.1] in dimension 4 + 1.) Let

    Σ := spec^(<3+ε_+)_(ι⁺)(L̄, ℰ^C_I) ∩ π_1ℰ_♯,

a finite set, and ℛ′_0 := {ψ = (μ, τ) ∈ ℛ′ : μ ∈ (−1, 0]} (the rows s0 and s2 at the root 0 and the class rows c0, c1).
For k ∈ ℕ_0 ∪ {∞}, 𝒟^k is the space of tuples

    U = ( b − b₀, S, S^(0)_1, (u^0_λ, f_λ)_(λ∈Σ), S_rem, b_rem, (Y_(ψ,rem))_(ψ∈ℛ′_0), h̃ )               {#eq:iii-j-1-1}

with b ∈ 𝔟; S, S^(0)_1 ∈ 𝒮_1; u^0_λ ∈ Res_(ι⁺)(L̄, λ) and f_λ ∈ Poly^(K_ι(λ))(ℂ_z; H^(k,(⟨ℰ^C_I+1⟩′,≤ℓ_I+1))_b)
([[eq:iii-g3-3-5]]); S_rem ∈ Ḣ^(k,(α−2)−)_b([1, ∞]; 𝒮_1), b_rem ∈ Ḣ^(k,(α−1)−)_b([1, ∞]; 𝔟), Y_(ψ,rem) ∈
Ḣ^(k,(3+ε_+−d_ψ)−)_b([1, ∞]; 𝒴_ψ); and h̃ ∈ H^(k,(⟨ℰ^C_I⟩,ℓ_I),(3+ε_+)−,α−)_b(Ω_*; S²T*)^(•,−). The components are real,
except (u^0_λ, f_λ), which are conjugation-symmetric: (u^0_λ̄, f_λ̄) is the complex conjugate of (u^0_λ, f_λ). Put

    u_λ := u^0_λ + res_(z=λ)( t_*^(−z) N_(ι⁺)(z)⁻¹ f_λ(z) ),

the image under [[eq:iii-g3-3-6]]; U_0 := (b − b₀, S, S^(0)_1); and U_1 the remaining components. The seminorms are
those of the components, at every loss ε > 0 in the orders "w−".

**Lemma {#lem:iii-j-1-2}** (The exponents of the data.) For λ ∈ Σ, K_ι(λ) ≤ 2l_* + 1, and

    u_λ = Σ_(j<K_ι(λ)) t_*^(−λ)(log t_*)^j u^(λ,j)

with (λ, j) ∈ ℰ_♯ for j < K_ι(λ), and u^(λ,j) ∈ H^(k−l,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺) for ℓ_K < ℓ^max_K, with l of
[[prop:iii-g3-3-7]].

*Proof.* The order of the pole of [[eq:iii-g3-2-2]] at λ is at most the order of λ in Spec_(ι⁺)(L̄) plus k(ℰ^C_(I,♯),
λ) + 1 ([[prop:iii-g3-2-4]]; [Hin26, Proposition 9.15]), and l_* bounds both the orders of the poles of N_(ι⁺)(L̄, ·)⁻¹
and the log orders of ℰ^C_I ([[def:iii-i10-1-1]]); so K_ι(λ) ≤ 2l_* + 1, and the residue of a pole of order K_ι(λ) has
log powers below K_ι(λ) (as does u^0_λ, a residue of a pole of N_(ι⁺)(L̄, ·)⁻¹). For Re λ ≥ 2: λ ∈ Λ (as Σ ⊂ π_1ℰ_♯) and
j ≤ 2l_* < k̄(λ), so (λ, j) ∈ ℰ_♯. For Re λ < 2: spec_(ι⁺)(L̄) ⊂ {Re ≥ 2} ([[lem:iii-g1-4-2]] (a)), so λ ∈ {λ_♯} ∪
π_1ℰ^C_I ([[cor:iii-g3-2-6]]), with K_ι(λ_♯) = 1 and K_ι(z) ≤ k(ℰ^C_I, z) + 1 for z ∈ π_1ℰ^C_I, z ≠ λ_♯ (the pole bound
of [[prop:iii-g3-2-4]], with m_ι = 0 below 2). And ℰ^♯_+ contains (λ_♯, 0) and, for each z ∈ π_1ℰ^C_I, the extended
union taken k(ℰ^C_I, z) + 1 times ([[eq:iii-i1-3-2]]), so (λ, j) ∈ ℰ^♯_+ ∩ {Re < 2} ⊂ ℳ
([[eq:iii-i8-1-1]]–[[eq:iii-i8-1-2]]). The regularity is [[prop:iii-g3-3-7]]. ∎

### Approximate solutions from data {#sec:iii-j-2}

Let U ∈ 𝒟^∞ be small. The construction assigns to the exponents λ₀ ∈ Λ_* := Λ ∩ {Re < 3 + ε_+}, a finite set, in order
of increasing real part (exponents of equal real part together; their equations below are independent), a correction
h_(λ₀), quasi-homogeneous of degree λ₀ in t_*⁻¹, row coordinates W_ν for the rows ν = (τ, λ₀, j) of 𝒩 and (rot, λ₀, j)
of 𝒩_rot, and the polyhomogeneous coefficients of q at the exponents (λ₀ − d_ψ, j); and then

    h := χ_ι Σ_(λ∈Σ) u_λ + h̃ + χ_ι Σ_(λ₀∈Λ_*) h_(λ₀),     p⃗ := (U_0, (W_ν)),
    q := ( S_rem, b_rem, (Y_(ψ,rem) (ψ ∈ ℛ′_0)) + (the polyhomogeneous coefficients) ),                  {#eq:iii-j-2-1}

with χ_ι the cut-off of [[sec:iii-g2-4]]. The rows m_ν here are those built at b₀ ([[def:iii-i9-2-1]],
[[def:iii-i14-1-3]]); the towers are T_(ψ,b). For (h, p⃗, q) of the form [[eq:iii-j-2-1]], and for each λ₀, put

    G(λ₀) := [ h + Σ_(ν∈𝒩⊔𝒩_rot) m_ν(W_ν) + h_(b,rem)(q) ]_(λ₀),     F_0(λ₀) := [ P_4(0, p⃗_(≤0)) ]_(λ₀+2),

the latter with every row coordinate 0.

**Lemma {#lem:iii-j-2-1}** (The ι⁺-terms below 3 + ε_+.) For (h, p⃗, q) of the form [[eq:iii-j-2-1]], with U small,
P_5(h, p⃗, q) is partially polyhomogeneous at ι⁺ to the weight (5 + ε_+)−, with u-exponents in Λ, and for λ₀ ∈ Λ_*

    [ P_5(h, p⃗, q) ]_(λ₀+2) = F_0(λ₀) + L̄ G(λ₀).                                                       {#eq:iii-j-2-2}

F_0(λ₀) depends only on p⃗_(≤0), smoothly; it vanishes unless λ₀ ∈ π_1𝒢, and its coefficients are compactly supported in
(ι⁺)°.

*Proof.* Write P_5(h, p⃗, q) = P_4(h″, p⃗) ([[eq:iii-i14-1-3]]), and Taylor-expand P_4 at (0, p⃗_(≤0) ⊕ 0) in h″ and
in the row coordinates W:

    P_4(h″, p⃗) = P_4(0, p⃗_(≤0)) + L_(0,p⃗_(≤0)) h″ + Σ_ν D_(W_ν)P_4(0, p⃗_(≤0))(W_ν) + Q,

with Q at least quadratic in (h″, W). Every term of h″ and every h_ν(W_ν), m_ν(W_ν) has ι⁺-order at least λ_♯: u_λ and
h_(λ₀) as Λ ⊂ {Re ≥ λ_♯} ([[lem:iii-i10-1-2]] (a)); h̃ by its class; the rows by [[lem:iii-i9-2-2]] (b) (with
[[def:iii-i14-1-3]]); the towers by [[lem:iii-i14-2-2]] (a) (at b, [[thm:iii-i15-3-1]]). Q is of order two in its
arguments and their first two derivatives, each derivative giving a factor ρ_+ at ι⁺, so its u-exponents are at least
2λ_♯ = 3 + 2δ_♯ > 3 + ε_+ (ε_+ < δ_♯, [[eq:iii-i9-1-1]]), and it has the weight (5 + 2δ_♯)− > w_+.

L_(0,p⃗_(≤0)) = L^(g_0+h_tot(p⃗_(≤0)),g_0) differs from L_(b₀) by coefficients of ι⁺-order at least 2: g_0 − g_(b₀) and
h_tot(p⃗_(≤0)) have ι⁺-order ≥ 2 ([[eq:iii-i7-1-3]] and [[lem:iii-i7-2-2]], [[lem:iii-i9-2-5]]). And L_(b₀) differs from
L̄, near ι⁺ away from K⁺, by the term t_*^(−λ−4)v²Bw of [[eq:iii-g2-4-1]]. So for a term w of ι⁺-order ≥ λ_♯,
[L_(0,p⃗_(≤0)) w]_(λ₀+2) = L̄[w]_(λ₀) for Re λ₀ < λ_♯ + 2, a range which contains Λ_*. Likewise D_(W_ν)P_4(0,
p⃗_(≤0))(W) − D_(W_ν)P_4(0, 0)(W) consists of terms linear in W, of size O(|p⃗_(≤0)||W|) (through g_0, h_tot(p⃗_(≤0))
and δ*_(g_0,E_C), [[eq:iii-i9-2-3]]), of u-exponent ≥ λ_♯ + 2; and D_(W_ν)P_4(0, 0)(W) = L_(b₀) m_ν(W)
([[lem:iii-i9-2-4]]; for the rotation rows [[def:iii-i14-1-3]]), so its term of u-exponent λ₀ is L̄[m_ν(W)]_(λ₀).
Summing gives [[eq:iii-j-2-2]].

The conormal remainders: h̃ and the conormal parts of q have ι⁺-order (3 + ε_+)− ([[lem:iii-i14-2-2]] (a), at b by
[[thm:iii-i15-3-1]], with 3 + ε_+ for 3 + η_2; S_rem, b_rem give (α + 1)−), which L_(0,p⃗_(≤0)) maps to the weight (5 +
ε_+)−. The terms of the rows of u-exponent ≥ 3 + ε_+ have the weight w_+ ([[lem:iii-i9-2-6]] (b): the plain weight a_+ +
Re λ + 2 − ε). And P_4(0, p⃗_(≤0)) is smooth in p⃗_(≤0) and supported in supp dχ_K: there g_0 is a pulled-back
Myers–Perry metric, so Ric(g_0) = 0 off supp dχ_K ([[eq:iii-i7-1-3]]), and h_tot(p⃗_(≤0)), ϑ_tot(p⃗_(≤0)) are supported
in supp dχ_K ([[def:iii-i7-2-3]]), a set whose closure meets ι⁺ in a compact subset of (ι⁺)° (χ_K is a function of R near
ι⁺, equal to 1 near R = 0 and to 0 near ℐ⁺). Its ι⁺-exponents lie in 𝒢 ([[lem:iii-i7-2-2]], [[lem:iii-i9-2-5]]), and
those of every other term lie in Λ ([[lem:iii-j-2-3]], which [[eq:iii-j-2-2]] does not use). ∎

**Lemma {#lem:iii-j-2-2}** (Rows and towers at ι⁺.) Let λ₀ ∈ Λ_* and j ∈ ℕ_0.

(a) Let ν = (τ, λ₀, j), whose ι⁺-exponent is λ₀ ([[lem:iii-i9-2-2]] (b)), with τ ∈ 𝒯 ∖ {v1}; put μ_s0 = μ_s2 := 0, μ_s1
:= −1, and μ_c0, μ_c1 the class roots; and let W ∈ 𝒲_(τ,ℂ). Then [m_ν(W)]_(λ₀) is χ_K times t_*^(−λ₀) times a finite sum
Σ_(i≤j)(log t_*)^i φ_i, whose expansion as R → 0 is the formal solution of [[thm:iii-g2-3-1]] of type τ at the root μ_τ
with coefficient c_τ(λ₀)W in the top log power j, plus formal solutions of the same type with lower log powers, plus
terms of K⁺-order ≥ Re λ₀ + 3. Here c_s1(λ₀) = λ₀(λ₀ − 1) and c_τ = 1 otherwise. The same holds for the rotation rows ν
= (rot, λ₀, j), (λ₀, j) ∈ ℳ_rot, W ∈ 𝒱_(1,ℂ), with the v1 formal solution and c_v1 = −λ₀.

(b) For ψ = (μ, τ) ∈ ℛ′ and Y ∈ 𝒴_ψ, [χ_K T_(ψ,b)(t_*^(−(λ₀−d_ψ))(log t_*)^j Y)]_(λ₀) is χ_K times the formal solution
of type τ at μ with coefficient Y (and, for v1, coefficient −λ₀Y) in the top log power, plus lower log powers, plus
terms of K⁺-order ≥ Re λ₀ + 3; it does not depend on b.

*Proof.* (a) By [[lem:iii-i10-2-1]] (a),

    m_ν(W) = χ_K( Σ_(i≤K_τ) a_ν^(i) h̆^i_τ(W) + a_ν^(K_τ+1) dt_* ⊗_s ω̆^(K_τ)_τ(W) ).

The stationary tensors h̆^i_τ are polyhomogeneous at ∂X with leading terms homogeneous of degree μ_τ − i (for s1 the
leading orders are ρ³, ρ², then ρ^(1−i) for i ≥ 2; for s0, h̆^0_s0 = 0 and h̆^(i+1)_s0 has degree −i), the Myers–Perry
corrections being smaller by ℰ_ind ([[sec:iii-g2-2-2]], [[lem:iii-i10-2-1]] (b), [[eq:iii-i9-2-1]]); and a_ν^(i) is a
combination of t_*^(−e_ν−i)(log t_*)^(i′), i′ ≤ j. Write h̆̄ for the leading term at ∂X of a stationary tensor h̆, as in
[[sec:iii-g2-2-2]]. Near ι⁺, r = Rt_*, so a_ν^(i) h̆̄^i_τ is quasi-homogeneous of degree λ₀ in t_*⁻¹ (for s0, s2, c0,
c1, e_ν + μ_τ = λ₀, as d_τ = −μ_τ; for s1, whose h̆̄^i has degree 1 − i, e_ν + 1 = λ₀; for v1, e_ν = λ₀) and has
K⁺-order Re e_ν + i; the corrections have u-exponents in λ₀ + ℰ_ind. For s1 the terms i = 0, 1 (ρ³, ρ²) have u-exponent
λ₀ + 2, and the rest is

    Σ_(i≥2) a_ν^(i) h̆̄^i_s1 = h̄^(≤K_s1)_s1(a_ν″),     a_ν″ = λ₀(λ₀ − 1) t_*^(−λ₀−1)(log t_*)^j + ⋯

([[eq:iii-g2-2-5]]). For s0, where a_ν = A_ν with A_ν′ = r_ν ([[def:iii-i9-2-1]]), Σ_(i≥1) A_ν^(i) h̆̄^i_s0 = Σ_i r_ν^(i)
h̆̄^(i+1)_s0 with r_ν = t_*^(−λ₀)(log t_*)^j. For s2, c0, c1, Σ_i a_ν^(i) h̆̄^i_τ = h̄^((μ_τ),≤K_τ)_τ(a_ν) with a_ν =
t_*^(−λ₀+μ_τ)(log t_*)^j. Comparing with [[eq:iii-g2-3-1]] of [[thm:iii-g2-3-1]] (and its (log t_*)^j-version,
[[cor:iii-g3-3-1]] (2)): the terms with i ≤ k_(μ_τ) (for s1 the convention h̄^(≤3)_s1, i ≤ 3) are the formal solution,
with coefficient c_τ(λ₀)W in the top log power; derivatives of (log t_*)^j produce the lower powers; and the terms with
i > k_(μ_τ) and the dt_*-term have K⁺-order ≥ Re e_ν + k_(μ_τ) + 1 ≥ Re λ₀ + 3 (the table of [[sec:iii-g2-1]]: k_μ ≥ 2 +
μ, and for s1, k = 3). For the rotation rows the same argument applies with h̆^0_v1 = h_(b₀,v1) = 0
([[def:iii-i14-1-3]]): Σ_(i≥1) a_ν^(i) h̆̄^i_v1 = h̄^(≤K_v1)_v1(a_ν′) ([[eq:iii-g2-2-5]]), with a_ν′ = −λ₀
t_*^(−λ₀−1)(log t_*)^j + ⋯.

(b) T_(ψ,b) = h^((μ),≤k_μ)_(b,τ) ([[def:iii-g2-2-5]]), whose leading part at ∂X is the Minkowski tower of
[[def:iii-g2-2-3]] and does not depend on b ([[lem:iii-i14-2-1]]). Take a = t_*^(−λ₀+μ)(log t_*)^j Y for ψ other than
v1; for v1, h^(≤2)_(b,v1)(a) has the leading part h̄^(≤2)_v1(a′), a = t_*^(−λ₀)(log t_*)^j Y ([[eq:iii-g2-2-5]],
[[eq:iii-g2-2-7]]), and h_(b,v1) ∈ 𝒜³ contributes at u-exponent ≥ λ₀ + 3. ∎

#### The step at an exponent λ₀ {#sec:s23-step}

Suppose every choice for the exponents of real part below Re λ₀ is made. Let T(λ₀) := G(λ₀) computed with these choices
only (no datum, correction, row or coefficient at λ₀ itself): the t_*^(−λ₀)-terms of the rows and towers already chosen,
which arise from their Myers–Perry corrections (λ₀ ∈ λ + π_1ℰ_ind). Put

    f := −F_0(λ₀) − L̄ T(λ₀),     v := u_(λ₀) + 𝒮_(λ₀)(f),

with u_(λ₀) := 0 if λ₀ ∉ Σ, and 𝒮_(λ₀)(f) the solution of L̄𝒮 = f that [[cor:iii-g3-3-1]] (1), which solves 2L̄u = ·,
gives for 2f, with ℓ_K = ℓ_K(λ₀). By [[cor:iii-g3-3-1]] (2) and [[rem:iii-g3-3-3]], v = χ_K v_0 + ṽ, with v_0 a sum of
formal solutions of [[thm:iii-g2-3-1]] (with powers (log t_*)^i, i bounded as in [[cor:iii-g3-3-1]] (2)) at the roots μ
∈ 𝒲(ℓ_K(λ₀)), and ṽ a sum of terms t_*^(−λ₀)(log t_*)^i H^(∞,(⟨ℰ^C_I⟩,ℓ_I),ℓ_K(λ₀))_b(ι⁺), so of K⁺-order α−. Each
formal solution in v_0, of type τ at the root μ, has K⁺-order Re(λ₀ − μ) < α, as −Re μ < ℓ_K(λ₀), and is carried below
by a row or a tower, of rate Re(λ₀ − μ), except for the boost row s1 (rate Re λ₀ − 1) and for v1 at a rotating b (rate
Re λ₀). We assign, top log power first:

(i) the terms of type τ ∈ 𝒯 ∖ {v1} at μ_τ whose row has rate Re e_ν ≤ 2 to the row ν = (τ, λ₀, i), with W_ν := c_τ(λ₀)⁻¹
times the coefficient; by (G) these are all the s1, s0, s2, c0, c1 terms of rate ≤ 2 + ε_K, and the s1 terms have Re λ₀
≤ 3;

(ii) the v1 terms with Re λ₀ ≤ 2, whose exponents lie in ℳ_rot ([[lem:iii-j-2-3]]; [[def:iii-i14-1-1]]), to the rotation
row (rot, λ₀, i), with W := c_v1(λ₀)⁻¹ times the coefficient;

(iii) every other term, of type τ at μ with rate in (2, α) (the s0, s2, c0, c1 terms of rate > 2, the v1 terms with Re
λ₀ > 2, and the rows of the table of [[sec:iii-g2-1]] with μ ≤ −1 other than s1 and v1, of rate ≥ Re λ₀ + 1 > 5/2), to
the coefficient of Y_ψ, ψ = (μ, τ), at the exponent (λ₀ − d_ψ, i): the coefficient itself (for v1, −λ₀⁻¹ times it).

Since the lower log powers that each assignment produces ([[lem:iii-j-2-2]]) are of the same type, the assignment
proceeds downward in the log power and is unique. Let R(λ₀) be the sum of [m_ν(W_ν)]_(λ₀) and [χ_K T_(ψ,b)(·)]_(λ₀) over
the rows and coefficients just assigned, and put

    h_(λ₀) := 𝒮_(λ₀)(f) − R(λ₀).

Then [h]_(λ₀) = u_(λ₀) + h_(λ₀) = v − R(λ₀) has, by [[lem:iii-j-2-2]], the same formal solutions removed, so it is ṽ
plus terms of K⁺-order ≥ Re λ₀ + 3 > α: its K⁺-order is α−. And G(λ₀) = [h]_(λ₀) + R(λ₀) + T(λ₀) = v + T(λ₀), so by
[[eq:iii-j-2-2]] and L̄u_(λ₀) = 0

    [ P_5(h, p⃗, q) ]_(λ₀+2) = F_0(λ₀) + L̄ 𝒮_(λ₀)(f) + L̄ T(λ₀) = 0.                                    {#eq:iii-j-2-3}

The choices at higher real part change no t_*^(−λ₀)-term: their own terms and their corrections have u-exponents of
larger real part.

The hypotheses of [[cor:iii-g3-3-1]] hold. First, Re λ₀ < 3 + ε_+ < ℓ_I. Second, ℓ_K(λ₀) is admissible by (A_J)
([[def:iii-j-a-j]]). Third, f has no ℐ⁺-expansion: it vanishes near ℐ⁺ ∩ ι⁺, as F_0 is supported in supp dχ_K and the
rows and towers in supp χ_K. Fourth, the coefficients of f have K⁺-order ≥ α, so they lie in H^(∞,ℓ_K(λ₀)−2)_b at R = 0:
F_0 is compactly supported in (ι⁺)°, and L̄T(λ₀) = [L_(b₀) Σ m_ν + L_b χ_K Σ T_(ψ,b)]_(λ₀+2) by the proof of
[[lem:iii-j-2-1]] ([L_b w]_(λ+2) = L̄[w]_λ as for L_(b₀), L_b − L̄ raising the u-exponent by 2 near ι⁺ away from K⁺,
[[eq:iii-g2-4-1]]). Here L_(b₀) m_ν = f^ν_(0,0) has K⁺-weight κ_ν − ε > 9/2 > α ([[lem:iii-i9-2-2]] (d)), and L_b
T_(ψ,b)(a) consists of the terms with a^(k_μ+1), a^(k_μ+2), of K⁺-order ≥ Re λ₀ + 3 ([[lem:iii-g2-2-6]]), the
commutators with χ_K being supported away from K⁺. As f has no ℐ⁺-expansion, [[eq:iii-g3-2-2]] acts on it as the inverse
of [[thm:iii-g1-3-1]] (2) (the construction of [[prop:iii-g3-2-4]] with f of plain ℐ⁺-weight), whose poles lie in
spec_(ι⁺)(L̄) ⊂ {Re ≥ 2}: below 2, 𝒮_(λ₀) raises no log power, and above 2 it raises it by at most l_*.

In particular no right-hand side f of a step carries the exceptional term v^(1+λ_♯)e₇ at ℐ⁺ ∩ ι⁺ of [[sec:iii-g3-2]],
and the pole of [[eq:iii-g3-2-2]] at λ_♯ enters the construction only through the datum f_(λ_♯).

**Lemma {#lem:iii-j-2-3}** (The log count.) Every exponent (λ₀, i) of the construction (of [h]_(λ₀), of the rows
assigned, and of the coefficients of q, shifted by d_ψ) lies in ℰ_♯; the rows assigned lie in 𝒩 ⊔ 𝒩_rot, and the
coefficients of q in 𝒬^∞_J.

*Proof.* By induction over Λ_* in order of real part. The log powers at λ₀ come from: the data u_(λ₀), ≤ 2l_*
([[lem:iii-j-1-2]]); F_0(λ₀), ≤ k̄_0 (𝒢, [[def:iii-i10-1-1]]); the corrections of rows and towers chosen at λ < λ₀, ≤
k̄(λ) + l_* by induction, as λ₀ ∈ λ + π_1ℰ_ind and the log orders of ℰ_ind are ≤ l_*; and 𝒮_(λ₀) adds at most l_* for Re
λ₀ ≥ 2 and nothing below 2. For Re λ₀ ≥ 2, λ₀ ∈ Λ has n(λ₀) ≥ n(λ) + 1 for each such λ, so k̄(λ₀) ≥ k̄(λ) +
(J_* + 1)(l_* + 1) ≥ k̄(λ) + 2l_* and k̄(λ₀) ≥ k̄_0 + (J_* + 1)(l_* + 1): every log power is ≤ k̄(λ₀). Below 2: the data
lie in ℳ ([[lem:iii-j-1-2]]), F_0(λ₀) = 0 (𝒢 ⊂ {Re ≥ 2}), the corrections of terms at exponents in ℳ lie in ℳ + ℰ_ind,
which below 2 is in ℳ ([[eq:iii-i8-1-1]], [[sec:iii-i12-1]]), and no log is raised. So (λ₀, i) ∈ ℰ_♯. The rows: a row
assigned in (i) is (τ, λ₀, i) with (λ₀, i) ∈ ℰ_♯ and Re λ₀ ≤ 3 (its rate Re λ₀ + d_τ ≤ 2, d_τ ≥ −1), hence (λ₀, i) ∈
ℰ_par ([[eq:iii-i10-1-2]]) and ν ∈ 𝒩; the rotation rows of (ii) are in 𝒩_rot, their exponents lying in ℰ_♯ ∩ {Re ≤ 2} =
ℳ_rot. The coefficients of (iii): (λ₀ − d_ψ, i) ∈ ℰ_♯ − d_ψ with rate > 2, which is ℰ^α_ψ ([[def:iii-i14-1-1]]; for v1,
Re λ₀ > 2), and Re(λ₀ − d_ψ) < 3 + ε_+ − d_ψ, below the conormal order of 𝒬^∞_J. ∎

**Theorem {#thm:iii-j-2-4}** ([Hin26, Theorem 12.3] in dimension 4 + 1.) There are d ∈ ℕ and ε_0 > 0 such that for U ∈
𝒟^∞ with ‖U‖_(𝒟^d) < ε_0 the construction defines

    Φ(U) = (h, p⃗, q) = Φ_0(U_0) + A(U_0)U_1 ∈ 𝒳^∞_J × 𝒫 × 𝒬^∞_J,                                        {#eq:iii-j-2-4}

with Φ_0 smooth on {|U_0| < ε_0}, Φ_0(0) = 0, and A(U_0) linear, smooth in U_0, and bounded from the U_1-components of
𝒟^(k+d) to 𝒳^k_J × 𝒫 × 𝒬^k_J for every k, with bounds uniform in |U_0| < ε_0. So Φ extends continuously to 𝒟^(k+d) →
𝒳^k_J ⊕ 𝒫 ⊕ 𝒬^k_J, is smooth (in particular N-fold differentiable for every N), and is tame: ‖Φ(U)‖_k ≤
C_k‖U‖_(𝒟^(k+d)). Moreover

    P_5(Φ(U)) ∈ ℱ^(k−2)     for U ∈ 𝒟^(k+d),                                                             {#eq:iii-j-2-5}

and:

(1) the components S, b − b₀, S^(0)_1 of p⃗ are those of U;

(2) the components S_rem, b_rem of q are those of U, the conormal part of Y_ψ is Y_(ψ,rem) for ψ ∈ ℛ′_0 and 0 otherwise,
and replacing h̃ by h̃ + h̃′ replaces h by h + h̃′;

(3) if U and U′ differ only in (u^0_(λ₀), f_(λ₀)), by (u′^0, f′), and u′_(λ₀) is the image of (u′^0, f′) under
[[eq:iii-g3-3-6]], then (h′, p⃗′, q′) := Φ(U′) − Φ(U) has: h′ with ι⁺-terms only at exponents of real part ≥ Re λ₀; no
row or coefficient of q at an exponent of real part below Re λ₀; and [h′]_(λ₀) = u′_(λ₀) − R′(λ₀), where R′(λ₀), the
t_*^(−λ₀)-term of the rows and coefficients of (p⃗′, q′) at λ₀, has the same formal solutions at R = 0 as u′_(λ₀) of
rate below α;

(4) Φ commutes with conjugation: h and q are real and the row coordinates conjugation-symmetric.

*Proof.* The construction is well defined by [[lem:iii-j-2-1]]–[[lem:iii-j-2-3]] and [[cor:iii-g3-3-1]].

*Membership.* h: its ℐ⁺-data are (⟨ℰ^C_I⟩, ℓ_I) (those of the u_λ, 𝒮_(λ₀)(f) and h̃; the R(λ₀) vanish near ℐ⁺); at ι⁺ it
is partially polyhomogeneous with exponents in ℰ_♯ ⊂ ℰ_+ ([[lem:iii-j-2-3]]) to the order (3 + ε_+)− (that of h̃); at K⁺
each [h]_(λ₀) has order α− (the step at λ₀), so χ_ι[h]_(λ₀) does, and h̃ does. p⃗ ∈ 𝒫 and q ∈ 𝒬^∞_J by
[[lem:iii-j-2-3]].

*[[eq:iii-j-2-5]].* At ι⁺: by [[lem:iii-j-2-1]] and [[eq:iii-j-2-3]], every u-exponent of real part below 3 + ε_+ has
vanishing term, so P_5(Φ(U)) has the plain weight (5 + ε_+)−. At ℐ⁺: h + h_(b,rem)(q) + h_tot(p⃗) is small in the class
[[eq:iii-i-1-4]] with the ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I), the rows and towers vanishing near ℐ⁺, so [[cor:iii-i-4-2]] gives the
ℐ⁺-order (⟨ℰ^C_I+1⟩′, ℓ_I + 1). At K⁺: near K⁺, g_0 = g_b, the rows enter only through ϑ_(ν,♯), of K⁺-weight κ_ν − ε > α
([[lem:iii-i9-2-2]] (d); h_ν is supported in 𝒞), and

    P_5 − P_4(h, p⃗) = L_b h_(b,rem)(q) + ∫_0^1 (L_(h+s h_(b,rem)(q),p⃗) − L_b) h_(b,rem)(q) ds,

with L_b h_(b,rem)(q) of K⁺-order α− ([[lem:iii-i14-2-2]] (b)) and the integral of K⁺-order (2α − 4)− > α at every b
near b₀, as in the proof of [[lem:iii-i14-2-4]] (c). Indeed h_(b,rem)(q) has K⁺-order (α − 2)− there, its v1 part
included, whose exponents have real part > 2, hence > 2 + ε_K ≥ α − 2 by (G), even where h_(b,v1) does not vanish
([[def:iii-i14-1-1]]; the v1 terms of real part ≤ 2 are those of the rotation rows, which enter only through h_ν and
ϑ_ν). And P_4(h, p⃗) near K⁺ is Ric(g_b + h) − δ*_(g_b,E_C)(Υ(g_b + h, g_b) − ϑ_tot), whose linear part L_b h has
K⁺-order α− (h has it; L_b is stationary), and whose nonlinear part has K⁺-order ≥ 2(α−).

*Structure.* Given U_0, every map of the construction is linear in U_1: F_0 depends on U_0 only ([[lem:iii-j-2-1]]), and
T(λ₀), 𝒮_(λ₀), the coefficient functionals of [[thm:iii-g2-3-1]] and [[cor:iii-g3-3-1]] (2), the assignment and R(λ₀)
are linear. The dependence on U_0 is through F_0, smooth in p⃗_(≤0), and through the towers T_(ψ,b), smooth in b
([[lem:iii-i14-2-1]]). This is [[eq:iii-j-2-4]], Φ_0(U_0) being the construction with U_1 = 0.

*Bounds.* There are finitely many steps. Each uses [[cor:iii-g3-3-1]] on a strip containing λ₀, with a fixed loss of
b-regularity there ([[prop:iii-g3-2-4]]), the functionals of [[thm:iii-g2-3-1]] (continuous on H^(k+2)_b) and
[[prop:iii-g3-3-7]] (loss l); d is the sum of these losses plus 2. The bounds are uniform for |U_0| small, since F_0 and
the towers are. As U_0 is finite-dimensional, |U_0| ≤ C‖U‖_(𝒟⁰), and the tame bound follows from [[eq:iii-j-2-4]].

*(1), (2)* hold by [[eq:iii-j-2-1]]. *(3)* By linearity in U_1, Φ(U′) − Φ(U) = A(U_0)(0, …, (u′^0, f′), …, 0). In the
construction with these data, every step below Re λ₀ has u = 0, F_0 = 0 and T = 0, so assigns nothing; at λ₀, f = 0
and v = u′_(λ₀), so [h′]_(λ₀) = u′_(λ₀) − R′(λ₀) with R′(λ₀) removing exactly the formal solutions of u′_(λ₀). *(4)* L̄,
χ_K, χ_ι, the states (at b, [[lem:iii-i15-1-1]] (P3)) and the cut-offs are real, conjugation maps the construction at λ₀
to that at λ̄₀, and the data are conjugation-symmetric. ∎

**Remark {#rem:iii-j-2-5}** (Linearisation; [Hin26, Remark 12.4].) Differentiating [[eq:iii-j-2-5]] in U: for U′ ∈ 𝒟^∞,
D_(Φ(U))P_5(D_UΦ(U′)) ∈ ℱ^∞, and

    D_UΦ(U′) = DΦ_0(U_0)U′_0 + (DA(U_0)U′_0)U_1 + A(U_0)U′_1;

parts (1)–(4) of [[thm:iii-j-2-4]] hold for D_UΦ with the obvious changes. So D_UΦ(U′) is an approximate solution of the
linearised equation at Φ(U), to the orders of ℱ.

**Remark {#rem:iii-j-2-6}** (Interpretation and the forward problem; [Hin26, Remarks 12.5–12.6].) By [[thm:iii-j-2-4]]
(3), each datum (u^0_λ, f_λ) enters h as u_λ minus the rows and tower coefficients that remove its expansion at K⁺ below
the rate α. The removed terms are pure gauge (for g_(b₀)) for the rows (types s1, v1, s0, s2, c0, c1 at rates ≤ 2) and
zero energy towers for q. As in [Hin26], the construction is much simpler than the forward problem of [[ch:s21]],
[[ch:s22]] and [[sec:iii-i14-3]]: it uses only the Minkowski model at ι⁺ and the formal solutions at ι⁺ ∩ K⁺, whereas
the K⁺-expansion of the forward solutions requires the full spectral analysis. In dimension 4 + 1 it is moreover linear
below 3 + ε_+, by the count of exponents in the proof of [[lem:iii-j-2-1]].

### The ι⁺-order of the linear solutions {#sec:iii-j1-1}

Everything of [[sec:iii-j-1]]–[[sec:iii-j-2]] is kept: α with (A_J), (G⁺), the classes 𝒳_J, ℱ, 𝒬_J, the data space 𝒟
with Σ and ℛ′_0, Λ_* = Λ ∩ {Re < 3 + ε_+}, the t_*^(−λ)-terms [·]_λ and the map Φ of [[thm:iii-j-2-4]]. Moreover Λ_* =
π_1ℰ_♯ ∩ {Re < 3 + ε_+} ([[lem:iii-i10-1-2]] (a), [[sec:iii-i12-1]]). The parameters are at b = b₀ unless said otherwise
(p⃗′ may still have a component b′, the direction of the derivative).

**Lemma {#lem:iii-j1-1-1}** (The ι⁺-order under (G⁺).) Under (G⁺), [[prop:iii-i11-3-1]], [[thm:iii-i12-3-1]] and
[[thm:iii-i14-3-1]] hold with η_2 replaced by ε_+ in their ι⁺-orders: in [[eq:iii-i12-3-2]]–[[eq:iii-i12-3-3]], w_ψ =
(3 + ε_+ − d_ψ)− and ũ has the ι⁺-data (ℰ_♯, (3 + ε_+)−); in [[eq:iii-i14-3-2]], h′ has the ι⁺-data (ℰ_♯, (3 + ε_+)−),
and q′ ∈ 𝒬^∞_J.

*Proof.* In [[prop:iii-i11-3-1]], η_2 enters as the threshold of level 2 (Step 3 of its proof: the tf-exponents α_0 of
g_2 with Re α_0 < 2 + η_2 are treated), as the order μ_2 = 2 + η_2 of the zero-energy solve there ([[lem:iii-i11-2-1]]
with μ′ = 2 + ε_+ − ε), and through the resulting tf-weight τ_3 = 1 + η_2 − 2ε of g_3, a lower bound; with the
conditions η_2 ∈ (ε_K, ε_+), η_2 > η_1, no λ ∈ Λ of real part 3 + η_2, and 2ε < ε_+ − η_2. The tf-exponents of the
sources at level 2 (of g_2 and of the remainders α_0 + ℰ_ind of the rounds of the loop) are u-exponents minus 1, so they
lie in Λ − 1: at level 2 the tf-exponent α_0 is the u-exponent α_0 + 1 ([[sec:iii-i11-3]]; [[lem:iii-i10-1-2]] (c)). By
(G⁺) none has real part in (2, 2 + ε_+]. So for every η_2 in (η^0_2, ε_+), η^0_2 the value fixed in [[sec:iii-i12-1]],
level 2 treats the same exponents. [[lem:iii-i11-2-1]] applies L̃_(b₀)(0)⁻¹ at the weight μ_2 − 4, and moving μ_2 within
(2 + η^0_2, 2 + ε_+) crosses neither an exponent of its right-hand side (those exceed 2 + ε_+, again by (G⁺), as the
last sentence of that lemma records them Λ-valued) nor an indicial root (none has real part in (0, 1),
[[prop:iii-f1-2-3]]); so its output is the same ([[prop:iii-h-3-2]]: its inverses on two such weights agree). Hence g_3
is one tensor for all these η_2, and has the tf-weight 1 + η_2 − 2ε for each of them with 2ε < ε_+ − η_2. Given ε, take
η_2 := ε_+ − 3ε; so g_3 has the tf-weight τ_3 := 1 + ε_+ − 5ε.

Step 4 of the proof of [[prop:iii-i11-3-1]] (level 3) and everything after it in [[ch:s22]] and
[[sec:iii-i14-2]]–[[sec:iii-i14-3]] use τ_3 only as a lower bound on the tf-weight of g_3, through: α_τ ≥ τ_3 > 1 + ℓ_3
(true, as ε_+ > ε_K > ℓ_3); the zf-weight α_τ ≥ τ_3 of the pieces at level 3, so their K⁺-weight ≥ 2 + ε_+ − 5ε > α − 2;
their ι⁺-order α_τ + 2 ≥ 3 + ε_+ − 5ε (Step 2 (viii) of the proof of [[thm:iii-i12-3-1]]); and w_ψ, chosen in
[[sec:iii-i12-1]] as the ι⁺-order of the pieces at level 3 minus d_ψ. With τ_3 = 1 + ε_+ − 5ε these give the ι⁺-order
3 + ε_+ − 5ε and w_ψ = 3 + ε_+ − 5ε − d_ψ, for every small ε; the polyhomogeneous parts are unchanged below 3 + ε_+,
there being no exponent in [3 + η^0_2, 3 + ε_+]. The independence of the decomposition from ε is [[lem:iii-i14-2-5]],
whose parameters at level 3 now are τ_i(ε) = 1 + ε_+ + iε_ind − (5 + i)ε, stable in the same way. [[thm:iii-i14-3-1]]
takes its ι⁺-orders from [[thm:iii-i12-3-1]] (Step 4 of its proof), and its intermediate levels do not enter h′, q′. So
h′ has (ℰ_♯, (3 + ε_+)−) at ι⁺, and q′ ∈ 𝒬^∞_J: its polyhomogeneous parts are those of [[def:iii-i14-1-1]] (exponents
below 3 + ε_+ − d_ψ), and its conormal parts Ṡ_rem, ḃ_rem and Y^c_ψ (ψ ∈ ℛ′_0 only, Step 4 of the proof of
[[thm:iii-i12-3-1]]) have the orders (α − 2)−, (α − 1)−, (3 + ε_+ − d_ψ)−. ∎

### Linear forward solutions {#sec:iii-j1-2}

**Theorem {#thm:iii-j1-2-1}** ([Hin26, Theorem 12.8] in dimension 4 + 1, at b₀.) There is d such that for U ∈ 𝒟^∞ with b
= b₀, small in 𝒟^d, and (h, p⃗, q) := Φ(U), the following holds. For every f ∈ ℱ^∞ there is U′ ∈ 𝒟^∞ with

    D_((h,p⃗,q))P_5( D_UΦ(U′) ) = f.                                                                    {#eq:iii-j1-2-1}

U′ is linear in f, and for every k there are d_k and C_k with ‖U′‖_(𝒟^k) ≤ C_k‖f‖_(ℱ^(k+d_k)) for U small in 𝒟^(d_k).

*Proof.* *Step 0 (the solution of [[thm:iii-i14-3-1]]).* (h, p⃗, q) = Φ(U) is admissible in [[thm:iii-i14-3-1]]: h ∈
𝒳^∞_J is in the class 𝒳 of [[sec:iii-i14-1]] with (H2) read as "α−" ([[rem:iii-i14-3-2]] (2)) and a_+ any value below
3 + ε_+ ((H5) for η_2 close to ε_+, [[lem:iii-j1-1-1]]); p⃗ ∈ 𝒫 at b₀; q ∈ 𝒬^∞_J ⊂ 𝒬; all small with U. And f ∈ ℱ^∞ ⊂
𝒴^0(α−): ℱ has the ℐ⁺-data of 𝒴^0_1, a plain ι⁺-weight (5 + ε_+)−, which the ι⁺-data (ℰ^0_src + 2, w_+ − ε) of 𝒴^0_1
contain, and the K⁺-order α−. [[thm:iii-i14-3-1]] with [[lem:iii-j1-1-1]] gives p⃗′ ∈ 𝒫, q′ ∈ 𝒬^∞_J and h′ with the
ι⁺-data (ℰ_♯, (3 + ε_+)−), the ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I) and the K⁺-order α−, such that

    D_((h,p⃗,q))P_5(h′, p⃗′, q′) = f.                                                                   {#eq:iii-j1-2-2}

We now subtract from (h′, p⃗′, q′) values of D_UΦ, each time keeping [[eq:iii-j1-2-2]] with a new f in ℱ^∞
([[rem:iii-j-2-5]]), until nothing is left but conormal remainders.

*Step 1 (the parameters p⃗′_(≤0)).* Let U′_0 := p⃗′_(≤0) = (S′, b′, S^(0)′_1), and replace (h′, p⃗′, q′) by (h′, p⃗′,
q′) − D_UΦ(U′_0 ⊕ 0). By [[thm:iii-j-2-4]] (1), linearised, the new p⃗′_(≤0) vanishes. This step has no t_*^(−1)-term to
treat: the parameters p⃗_(≤0) enter at the u-exponents of 𝒢 ⊂ {Re ≥ 2} ([[lem:iii-j-2-1]]).

*Step 2 (the exponents of Λ_*).* Suppose p⃗′_(≤0) = 0, and that for every λ ∈ Λ_* with Re λ < Re λ₀ the term [h′]_λ, the
rows W′_ν with ν = (τ, λ, k) or (rot, λ, k), and the polyhomogeneous coefficients of q′ at the exponents (λ − d_ψ, k)
vanish. Put

    G′(λ₀) := [ h′ + Σ_(ν∈𝒩⊔𝒩_rot) m_ν(W′_ν) + h_(b₀,rem)(q′) ]_(λ₀).

Differentiate [[lem:iii-j-2-1]] at (h, p⃗, q) in the direction (h′, p⃗′, q′): the quadratic part contributes at
u-exponents ≥ 2λ_♯ > 3 + ε_+, the dependence of F_0 and of L_(0,p⃗_(≤0)) on p⃗_(≤0) drops out as p⃗′_(≤0) = 0, and the
terms below λ₀ vanish; so

    [ D_((h,p⃗,q))P_5(h′, p⃗′, q′) ]_(λ₀+2) = L̄ G′(λ₀),

and as f has no ι⁺-term below (5 + ε_+)−, L̄G′(λ₀) = 0. Now G′(λ₀) = Σ_j t_*^(−λ₀)(log t_*)^j g_j with g_j ∈
H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺), ℓ_K := ℓ_K(λ₀) − ε. Indeed [h′]_(λ₀) has these ℐ⁺-data and, from the K⁺-order α− of
h′, the weight ℓ_K at R = 0; the rows and towers are supported in supp χ_K, away from ℐ⁺, and at R = 0 consist of formal
solutions of [[thm:iii-g2-3-1]] (exponents −μ + i ≥ 0, in ℰ_K below ℓ_K, [[cor:iii-g2-3-2]]) and terms of K⁺-order ≥ Re
λ₀ + 3 ([[lem:iii-j-2-2]]). So G′(λ₀) ∈ Res^∞_(ι⁺)(L̄, ℰ^C_I, λ₀) ([[def:iii-g3-3-2]]).

*Case A: λ₀ is not a pole of [[eq:iii-g3-2-2]].* Then Res^∞_(ι⁺)(L̄, ℰ^C_I, λ₀) = 0 ([[lem:iii-g3-3-5]]: its elements
are residues of t_*^(−z)N_(ι⁺)(z)⁻¹f(z) with f polynomial), so G′(λ₀) = 0. The coefficients of q′ have rate < α (the
proof of [[lem:iii-i12-2-4]] removes only the pairs below β = α − ε; Step 4 of the proof of [[thm:iii-i14-3-1]]), and so
do those of D_UΦ ((iii) of the step at λ₀, [[sec:s23-step]]), the rows having rate ≤ 3 (for s1 the order of the formal
solution is Re λ₀ + 1 ≤ 4). So every row and coefficient at λ₀ carries a formal solution of K⁺-order below Re λ₀ +
ℓ_K(λ₀) = α, visible below ℓ_K. Then the rows and coefficients at λ₀ vanish. Indeed the expansion of G′(λ₀) at R = 0
below ℓ_K is the sum of the formal solutions that the rows and coefficients at λ₀ carry ([[lem:iii-j-2-2]]), as
[h′]_(λ₀) = O(R^(ℓ_K)); the coefficients of [[thm:iii-g2-3-1]] are determined by the tensor ([[thm:iii-g2-3-1]],
[[lem:iii-g2-1-2]]: distinct rows have independent, injective leading terms); and [[lem:iii-j-2-2]] expresses them
through the rows and coefficients triangularly in the log power, with the nonzero factors c_τ(λ₀). So, downward in the
log power, every row and coefficient at λ₀ is 0. Then [h′]_(λ₀) = G′(λ₀) = 0.

*Case B: λ₀ is a pole of [[eq:iii-g3-2-2]].* Then λ₀ ∈ spec^(<3+ε_+)_(ι⁺)(L̄, ℰ^C_I) ∩ Λ_* ⊂ Σ. By [[prop:iii-g3-3-7]]
(its right inverse at k = ∞),

    G′(λ₀) = u^0_(λ₀) + res_(z=λ₀)( t_*^(−z)N_(ι⁺)(z)⁻¹ f_(λ₀)(z) )

for some (u^0_(λ₀), f_(λ₀)) in the domain of [[eq:iii-g3-3-6]], linear and continuous in G′(λ₀). It is
conjugation-symmetric, as G′(λ₀) and G′(λ̄₀) are conjugate; at real λ₀, [[eq:iii-g3-3-6]] being real, the real part of
the output of the right inverse is taken. Let U′_(λ₀) ∈ 𝒟^∞ have these data at λ₀ and λ̄₀ and all else 0. By
[[thm:iii-j-2-4]] (3), linearised, D_UΦ(U′_(λ₀)) has no term, row or coefficient below Re λ₀, and its total
t_*^(−λ₀)-term is u_(λ₀) − R′(λ₀) + R′(λ₀) = G′(λ₀). Replacing (h′, p⃗′, q′) by (h′, p⃗′, q′) − D_UΦ(U′_(λ₀)) makes the
new G′(λ₀) zero and leaves the lower terms zero; the argument of Case A then makes every term, row and coefficient at λ₀
vanish.

Exponents of equal real part are treated together, independently. After the finitely many exponents of Λ_*: p⃗′ = 0
(every row (τ, λ, k) or (rot, λ, k) of 𝒩 ⊔ 𝒩_rot has λ ∈ Λ_*, as Re λ ≤ 3; p⃗′_(≤0) = 0 by Step 1); q′ has no
polyhomogeneous part (each has ι⁺-exponent z + d_ψ ∈ Λ_*, [[def:iii-i14-1-1]] and [[lem:iii-j1-1-1]]); and h′ has no
ι⁺-term below 3 + ε_+, so h′ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(3+ε_+)−,α−)_b(Ω_*)^(•,−), the class of h̃ in [[def:iii-j-1-1]].

*Step 3 (conclusion).* Now q′ = (S′_rem, b′_rem, (Y′^c_ψ)_(ψ∈ℛ′_0)) with the orders of [[def:iii-j-1-1]]
([[lem:iii-j1-1-1]]), and (h′, 0, q′) = D_UΦ(U′_c) with

    U′_c := (0, 0, 0, (0, 0), S′_rem, b′_rem, (Y′^c_ψ), h′):

these components enter Φ additively ([[thm:iii-j-2-4]] (2)) and contribute to no t_*^(−λ₀)-term with λ₀ ∈ Λ_* (their
ι⁺-orders are (3 + ε_+)− and (α + 1)−), so they enter no step of the construction. Summing, the data U′ := U′_0 ⊕ Σ_(λ₀)
U′_(λ₀) + U′_c satisfy (h′, p⃗′, q′) = D_UΦ(U′) for the (h′, p⃗′, q′) of Step 0, and [[eq:iii-j1-2-2]] is
[[eq:iii-j1-2-1]]. *Linearity and bounds.* The solution of [[thm:iii-i14-3-1]] is linear in f with bounds uniform for
(h, p⃗, q) small; each subtraction is D_UΦ (bounded, [[thm:iii-j-2-4]]) of data that are continuous linear functions of
the current (h′, p⃗′, q′) ([[prop:iii-g3-3-7]] with loss l; finitely many steps). ∎

**Remark {#rem:iii-j1-2-2}** (Non-uniqueness; [Hin26, Remark 12.9].) Neither D_((h,p⃗,q))P_5 nor D_UΦ is injective: a
part of b′_rem of order α can be moved into h′, and the conormal parts of the data overlap with h̃ in the same way.
[[thm:iii-j1-2-1]] asserts that the particular solution of [[thm:iii-i14-3-1]] is of the form D_UΦ(U′), with U′ obtained
constructively from it, so U′ inherits its bounds. The construction of U′ from (h′, p⃗′, q′) (Steps 1–3) is linear, with
fixed losses and with coefficients that depend on U only through finitely many derivatives at the exponents of Λ_*. The
tame form of the bound of [[thm:iii-j1-2-1]], ‖U′‖_k ≤ C_k(‖f‖_(k+d) + ‖U‖_(k+d)‖f‖_d) as [Hin26] states it, is
[[thm:iii-j2-4-2]], and its form at exact weights is [[thm:iii-j3-5-5]].

### The statements at a base point near b₀ {#sec:s23-base-points}

The results of [[sec:iii-i14-1]]–[[sec:iii-j1-2]] that are stated at b = b₀ hold at every base point whose black hole
parameter b lies in the closed ball ℬ̄_* about b₀ of [[sec:iii-h2-0]], shrunk as in [[lem:iii-i15-1-2]] and
[[prop:iii-i15-2-5]], with constants and smallness conditions uniform in b ([[thm:iii-i15-3-1]]). The statement at b of
each of them is obtained by replacing L_(b₀), g_(b₀) near K⁺, the states, towers and companions at b₀ and the index set
ℰ_ind by those at b, by taking derivatives in b at b, and by treating the v1 terms as in [[ch:s25]]. In detail (items
(1) and (3) also name the results that are stated above at every b):

(1) [[lem:iii-i14-2-2]] (a), (c), [[lem:iii-i14-2-3]]–[[lem:iii-i14-2-5]] and [[rem:iii-i14-3-2]] (2) hold at b;
[[def:iii-i14-1-2]], [[eq:iii-i14-1-4]] and [[lem:iii-i14-2-2]] (b) are stated at b above. The proof of
[[lem:iii-i14-2-4]] (c) above is written for every b near b₀; it uses that every coefficient of q has rate > 2 at every
such b. The point of Step 1 of the proof of [[thm:iii-i14-3-1]] that uses L̂_(b₀)(0)∂_b h_(b,v1) = 0 needs only that
the q-terms have K⁺-order above α_1. At b, L̂_b(0)∂_b h_(b,v1) = −(∂_b L̂_b(0))h_(b,v1) need not vanish, but the v1
coefficients of q have rate > 2 + ε_K > α_1 ([[def:iii-i14-1-1]], (G)), so the K⁺-order of L(∂_b h_(b,rem)(q)b′) is
still > 2 + ε_K > α_1.

(2) [[thm:iii-i14-3-1]] holds at b in the form of [[prop:iii-i15-2-5]]: the p⃗′ there is unique among the parameters
whose rotation coordinates are the assigned ones ([[rem:iii-i15-2-6]]), and at b₀ it is the p⃗′ of [[thm:iii-i14-3-1]]
([[prop:iii-i15-2-5]]). Step 4′ of the proof of [[thm:iii-i14-3-1]] is not used at b.

(3) [[lem:iii-j-2-1]], [[lem:iii-j-2-2]], [[thm:iii-j-2-4]] and [[rem:iii-j-2-5]] are stated above at every b, under
the convention that the rows m_ν are built at b₀, the towers T_(ψ,b) at b and the corrections at b₀. Their proofs at b
use [[lem:iii-i14-2-2]] (a) at b, by (1), and the reality of the states at b ([[lem:iii-i15-1-1]] (P3)). P_5 and the
coordinates W_ν do not depend on whether the rows are built at b₀ or at b, as the rows enter P_4 only through the
corrections and counterterms built at b₀ ([[lem:iii-i14-2-4]] (a)), and Step 2 of the proof of [[thm:iii-j1-2-1]] uses
only the λ₀-terms of the rows, which do not depend on b ([[lem:iii-j-2-2]]). The pure gauge of [[rem:iii-j-2-6]] refers
to g_(b₀).

(4) [[lem:iii-j1-1-1]] holds for the output of [[prop:iii-i15-2-5]], and [[thm:iii-j1-2-1]], with its tame and exact
forms, holds at every base point U ∈ 𝒟^∞ small in 𝒟^d, whose black hole parameter then lies in ℬ_*, with constants
uniform in U; at a rotating b the right inverse is the one constructed from [[prop:iii-i15-2-5]] ([[cor:iii-i15-3-2]]).
These are the right inverses that [[thm:ii-g-2-1]] (iii) asks for at every point of its domain.