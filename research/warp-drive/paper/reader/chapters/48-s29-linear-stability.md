## Linear stability of five-dimensional Tangherlini, and the comparison of gauges {#ch:s29}

This chapter proves the linear stability of the five-dimensional Schwarzschild–Tangherlini metric g_(b₀),
b₀ = (m₀, 0), in the gauge of the nonlinear problem of [[ch:s27]], and compares that gauge with every other. Every
solution (γ̇, k̇) of the linearised constraint equations in the data class of [[thm:iii-k-4-3]] has a linearised vacuum
development ġ in the generalised wave gauge of [[prop:iii-k-4-2]]. Up to a linearised boost and translation, ġ induces
(γ̇, k̇), and where χ_K = 1 it differs from a linearised Myers–Perry metric ∂_b g_b(ḃ) by terms of K⁺-order (α − 2)−:
on spatially compact sets it is O(t_*^(−2−ε)) for each ε < ε_K, with α chosen for ε ([[thm:viii-2-2]]). In the
symmetry class of [[thm:settling]], ḃ is a change of mass alone and the boost and the translation vanish
([[cor:viii-2-3]]). This is [[thm:settling]] one order down.

No new linear theory is needed. The linear solution is the derivative at zero data of the equation P_5(Ψ(U)) = 0 of
[[ch:s27]], solved directly: the linear Cauchy problem near Σ^IVP ([[thm:iv2-2-4]], [[thm:iv3-2-1]], (L) of
[[sec:s27-local]] and the proof of [[thm:iii-c1-3-1]], each at h = 0), the right inverse of [[lem:iii-k-2-3]] at U = 0,
and the second Bianchi identity linearised at the Ricci-flat g_(b₀) in place of the nonlinear one. The Nash–Moser
theorem [[thm:ii-g-2-1]] gives existence and bounds but no differentiability of the nonlinear solution in the data, so
the linear solution is not obtained by differentiating the solution of [[thm:iii-k-4-3]]. Being linear, nothing here
needs smallness.

[[sec:ix-0]]–[[sec:ix-2]] compare ġ with a linearised vacuum solution given in another gauge. Every solution of
DRic = 0 on the future half of the Cauchy development, in {r > r_♭}, of a piece Σ_U of Σ^IVP, smooth up to Σ_U, whose
data agree with (γ̇, k̇) up to those of a linearised diffeomorphism, is ġ + ℒ_X g there for a vector field X, unique up
to Killing fields ([[thm:ix-2-2]], [[cor:ix-2-3]]). So the linear stability of [[thm:viii-2-2]] holds in every gauge,
modulo a linearised diffeomorphism. The argument is the standard one: put the difference into the linearised harmonic
gauge by solving a linear wave equation for X, show that the result has vanishing Cauchy data, and conclude by
uniqueness for a linear wave equation. Its inputs beyond [[sec:viii-0]]–[[sec:viii-2]] are chiefly the Cauchy problem
for normally hyperbolic operators on globally hyperbolic manifolds ([BGP]; [[sec:std-linear-wave]]) and the pointwise
identities of [[lem:ix-2-1]]. Nothing is asserted here about the size or decay of X ([[rem:ix-2-4]]). Linear
solutions in the Regge–Wheeler-type gauge of [KI03], whose gauge-invariant master quantities decay by [HKW18], and in
the harmonic gauge are treated in [[ch:rw-gauge]]–[[ch:harmonic-rate]], from the results of this chapter.

*The inner radius.* The inner radius r_♭ ∈ (0, ½R₁] of [[ch:s11]], R₁ = m₀^(1/2), is a parameter, with the radii of
[[def:s12-radii]]; so r₀ = r_♭ and r^♮ = ½(r_♭ + r₂) < r₂ < R₁. Every result of the chapter holds for every such r_♭,
with constants depending on it. Besides results of earlier chapters stated for every such r_♭, the arguments of this
chapter use the inner radius directly only through: [[lem:s11-ks-domain]] (g_(b₀) is defined on {|x| ≥ ½r_♭});
[[lem:iii-b-3-7]] (the time functions; ψ_IVP(r_♭) = 0 by the proof of its (b)); [[lem:ii-c-3-2]] (1)–(2) at h = 0
(dr future timelike on {r_♭ ≤ r ≤ r^♮}, dt^♭_* past timelike); [[lem:ii-f-1-4]] (a) with r₀ = r_♭; [[lem:s27-cover]]
(c) (the boundary piece {r = r_♭} of 𝒦); the identity F = 0 on [r_♭, 5R₁] of [[sec:iii-k-0]], so that t_* = t_IVP
there; and the radius R_ν = ½(r_♭ + 5R₁) of [[prop:iii-k-1-2]]. Each holds at r_♭. [[lem:ii-c-3-2]] is stated on
{t_* > 1}, but it is used below also near Σ^IVP, where t_* is near 0. At h = 0 its statement (1) concerns r only,
g_(b₀) being stationary, so it holds on all of {r_♭ ≤ r ≤ r^♮}, at every t_*: this is the argument of
[[lem:s27-below]] (iv), and [[prop:np-10-19-iv]] (d) gives it as well, as r^♮ < R₁ = r_h.

*Notation.* g := g_(b₀). The future unit normal of Σ^IVP for g is written n; the letter ν is kept for the function
ν(r) of [[prop:iii-k-1-2]]. For data on Σ^IVP, ‖(γ̇, k̇)‖_(H^k) is the norm of H^k of the classes
H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b, as in [[thm:iii-k-4-3]]. G = O(2) × O(2) is the group of
[[sec:s27-class]]; G_g k := k − ½g tr_g k is the trace reversal ([[sec:iii-b-6]]).

### Setting {#sec:viii-0}

Everything of [[sec:iii-k-0]] is kept: t_*, t_IVP, Σ^IVP := t_IVP⁻¹(0), t^♭_* and C_♭ (the constant C′ of
[[lem:ii-c-3-2]] (b)), T̂ = 2/C_♭, Ω_* = cl_M{t^♭_* ≥ 1}, the cut-offs χ_− ([[def:iii-k-2-1]]), χ_K (with χ_K = 0
on {t^♭_* < T̂ + 2}) and χ_ι, E_C, E_Υ, ℰ_0, ℓ_0, ℰ^C_I, ℓ_I, the weights of the cone and α. The parameters are those
of [[thm:vi-c-2-1]], as in [[thm:settling]]. A sublevel set {t^♭_* ≤ c} is the complement of {t^♭_* > c}, so that it
contains the points where t^♭_* is not defined. Also kept are χ^♮_0 and P^♮ of [[lem:iii-k-1-1]], and the region of
[[prop:iii-k-1-2]], which does not depend on the parameters,

    𝒟 = N_ν ∩ {t^♭_* ≤ T̂ + 3},        N_ν = {t_IVP ≥ −ν(|x|)},

with ν = 0 on [0, R_ν] and ν > 0 on (R_ν, ∞), and its cover by Ω_(ext,r_1), the compact part 𝒦 and the slab 𝒮
([[lem:s27-cover]], with the same r_1, R_8, R_9, c, T″ and ρ′_I), with 𝒟^± := 𝒟 ∩ {±t_IVP ≥ 0} and the compact set 𝒦⁻
of its part (e). 𝒟 contains Ω_* ∩ {t^♭_* ≤ T̂ + 3}, as t_IVP ≥ t_* ≥ t^♭_* ≥ 1 there.

*Linearised operators.* For a symmetric 2-tensor k let DRic(k) := (d/ds) Ric(g + sk)|_(s=0), and let Υ̇(k), Υ̇^♮(k),
Υ̇⁰(k) be the derivatives at (g, g) in the first argument of Υ^(E_Υ), Υ^(χ^♮_0E_Υ) and Υ⁰ ([[eq:iii-b-6-3]],
[[eq:iii-c2-2-1]], [[lem:iii-k-1-1]]). As δ*_(g_0,E_C) depends on g_0 only,

    L := D_1P(g, g) = DRic − δ*_(g,E_C)Υ̇,        L^♮ := D_1P^♮(g, g) = DRic − δ*_(g,E_C)Υ̇^♮.             {#eq:viii-0-1}

L is the operator L_g of [[eq:iii-b-6-4]], and L^♮ is the linearisation L^(χ^♮_0)_(g,g) of P^♮. On Ω_*, χ^♮_0 = 1
([[lem:iii-k-1-1]] (b)), so L^♮ = L and Υ̇^♮ = Υ̇ there. Near Σ^IVP, χ^♮_0 = 0 ([[lem:iii-k-1-1]] (d)), so
Υ̇^♮ = Υ̇⁰ there. And Υ^(E_Υ)(g_0, g_0) = Υ^(χ^♮_0E_Υ)(g_0, g_0) = 0 for every metric g_0, since Υ⁰(g_0, g_0) = 0 and the
E^Υ-term is linear in g − g_0 ([[eq:iii-b-6-3]], [[eq:iii-c2-2-1]]). [[lem:ii-f-1-3]] asks for the principal symbol
g⁻¹(ζ, ζ) Id. L^♮ and the operator δ_gG_gδ*_(g,E_C) of the constraint propagation have the principal symbol
½g⁻¹(ζ, ζ) Id (the proof of [[prop:viii-1-2]]); so wherever [[lem:ii-f-1-3]] is applied below to one of them, it is
applied to twice the operator, 2L^♮ or 2δ_gG_gδ*_(g,E_C), which has the same solutions.

*The constraints.* For a metric g̃ near Σ^IVP with future unit normal n_g̃, inducing the first and second fundamental
forms (γ, k), the Gauss and Codazzi equations write (G_g̃ Ric(g̃))(n_g̃, ·)|_(Σ^IVP) = 𝒞(γ, k), where 𝒞 is the
constraint map; it depends on g̃ only through (γ, k). Its vanishing is the constraint equations, as [[prop:iii-k-1-2]]
uses them. Data (γ̇, k̇) satisfy the *linearised constraint equations* if D𝒞_((γ_(b₀),k_(b₀)))(γ̇, k̇) = 0.

*The boost and translation generators.* Let Θ := χ_r(|x|)χ^♯_IVP(1 − χ^♭_K) ∈ [0, 1] be the cut-off factor of
[[lem:iii-b-5-1]]. The boosts are φ_S = exp V(S), with V(S_w) = ½ΘX_w linear in S = S_w ∈ 𝒮_1 ([[lem:iii-b-5-1]]),
and the translations are ψ_(S⁰) = exp V⁰(S⁰), with V⁰(S_w) = ½Θ w·∂_x linear in S⁰ = S_w ∈ 𝒮_1
([[lem:iii-i7-1-1]]). Both vector fields vanish where Θ = 0, so on {|x| ≤ 5R₁} and where χ^♭_K = 1. Their composite
is φ_(S,S⁰) = ψ_(S⁰) ∘ φ_S ([[eq:s27-motion]]). For S′, S⁰′ ∈ 𝒮_1 put

    ġ_(S′) := (d/ds) φ*_(−sS′) g |_(s=0) = −ℒ_(V(S′)) g,
    ġ⁰_(S⁰′) := (d/ds) ψ*_(−sS⁰′) g |_(s=0) = −ℒ_(V⁰(S⁰′)) g,                                           {#eq:viii-0-2}

linearised diffeomorphisms: φ_(−sS′) = exp(−sV(S′)) is the time-s flow of −V(S′), and likewise for ψ_(−sS⁰′). The
second is the derivative −δ*_g(Θw⁰(S⁰′)) of [[ch:s21]], as g(V⁰(S⁰′), ·) = ½Θw⁰(S⁰′) and ℒ_Xg = 2δ*_g(g(X, ·)). As
φ*_(−sS′,−sS⁰′)g = φ*_(−sS′)(ψ*_(−sS⁰′)g), by [[eq:s27-motion]], is smooth in s and both flows are the identity at
s = 0,

    (d/ds) φ*_(−sS′,−sS⁰′) g |_(s=0) = ġ_(S′) + ġ⁰_(S⁰′).

DRic(ġ_(S′)) = (d/ds) Ric(φ*_(−sS′)g)|_(s=0) = 0, Ric(φ*_(−sS′)g) = φ*_(−sS′)Ric(g) vanishing for every s, and
DRic(ġ⁰_(S⁰′)) = 0 likewise. Both tensors vanish on the interior of {Θ = 0}, which contains {|x| < 5R₁} and the
interior of {χ^♭_K = 1}, as V(S′) and V⁰(S⁰′) vanish there.

*The background.* The background of P_5 at p⃗_(≤0) = (S, b − b₀, S⁰) is the translated background of
[[eq:iii-i7-1-3]] ([[sec:iii-k-0]]),

    g_(p⃗) = (1 − χ_K) φ*_(−S,−S⁰) g + χ_K g_b,

which is φ*_(−S,−S⁰)g where χ_K = 0 and g_b where χ_K = 1, and is smooth in p⃗ ([[lem:iii-i7-1-3]] (a),
[[lem:s27-translated-exterior]] (a)).

Put 𝒟′ := 𝒟 ∖ {t^♭_* ≥ T̂ + 7/4}. Then Ω_* ∪ 𝒟 = Ω_* ∪ 𝒟′, as the points of 𝒟 with
t^♭_* ≥ T̂ + 7/4 lie in Ω_*; and Ω_* ∩ 𝒟′ = Ω_* ∩ {t^♭_* < T̂ + 7/4}, as 𝒟 contains Ω_* ∩ {t^♭_* ≤ T̂ + 3}.

### The linear initial-value problem {#sec:viii-1}

**Lemma {#lem:viii-1-1}** (Linearised gauged Cauchy data; [[prop:iii-c2-4-1]] linearised.) Let
γ̇ ∈ H^(∞,(ℰ_0,ℓ_0))_b(Σ^IVP; S²T*Σ^IVP) and k̇ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b(Σ^IVP; S²T*Σ^IVP). There are
ḣ_0, ḣ_1 ∈ H^(∞,(ℰ_0,ℓ_0))_b(Σ^IVP; S²T*), linear in (γ̇, k̇), each seminorm bounded by finitely many of (γ̇, k̇), such
that every symmetric 2-tensor ḣ, smooth near Σ^IVP or on one side of it up to Σ^IVP, with ḣ|_(Σ^IVP) = ḣ_0 and
(rℒ_(∂_(t_IVP))ḣ)|_(Σ^IVP) = ḣ_1 satisfies:

(1) the first and second fundamental forms of Σ^IVP for g + sḣ have the derivatives (γ̇, k̇) at s = 0;

(2) Υ̇⁰(ḣ) = 0 at Σ^IVP;

(3) if (γ̇, k̇) satisfy the linearised constraint equations, then (G_g DRic(ḣ))(n, ·) = 0 at Σ^IVP.

*Proof.* For |ε| small, [[prop:iii-c2-4-1]] applies to (γ̃, k̃) := ε(γ̇, k̇) (γ̃ is small in H³_b, and
the constraints are not assumed there). It gives h_0(ε) = εγ̇, extended by h_0(n, ·) := 0, and h_1(ε) = r h̃_1(ε). Its
proof determines h̃_1(ε) at each point by linear algebraic equations, solved in the order (ij), (0j), (00), each step
dividing by a multiple of e_0 t_IVP, which is bounded away from 0. Their other coefficients (the frame, the normal n_0
of g + h_0, written ν₀ there, the Christoffel symbols of g + h_0) are smooth functions of h_0 and its first derivatives.
Their right sides are smooth in these and affine in k̃ (the proof of [[prop:iii-c2-4-1]]). So ε ↦ h_1(ε) is
smooth at each point, with h_1(0) = 0. Put ḣ_0 := γ̇, extended in the same way, and ḣ_1 := ∂_ε h_1(0). This is the same
construction with the two equations of that proof, for the second fundamental form and for Υ⁰, linearised at g. Their
right sides are linear in γ̇, its b-derivatives and k̇, with the coefficients of that proof. So they lie in
H^(∞,(ℰ_0+1,ℓ_0+1))_b by its count, and ḣ_1 ∈ H^(∞,(ℰ_0,ℓ_0))_b, linearly and with the stated bounds.

Given ḣ, extend it smoothly across Σ^IVP if it is given on one side only; (1)–(3) involve only its derivatives at
Σ^IVP. Fix χ ∈ C^∞_c(ℝ) equal to 1 near 0, and in the coordinates (t_IVP, x) put

    g_ε := g + εḣ + t_IVP χ(t_IVP) r⁻¹(h_1(ε) − εḣ_1),

the last bracket taken independent of t_IVP. Then (g_ε − g)|_(Σ^IVP) = εγ̇ = h_0(ε) and
(rℒ_(∂_(t_IVP))(g_ε − g))|_(Σ^IVP) = εḣ_1 + h_1(ε) − εḣ_1 = h_1(ε). The conclusions of [[prop:iii-c2-4-1]] are
identities at each point of Σ^IVP, derived pointwise in its proof. So they hold for g_ε near any compact piece of
Σ^IVP, where g_ε is Lorentzian for |ε| small. By its (1)–(2), g_ε induces (γ_(b₀) + εγ̇, k_(b₀) + εk̇) and
Υ⁰(g_ε, g) = 0 at Σ^IVP, for every small ε. The induced data and Υ⁰ at Σ^IVP are smooth functions of g_ε and its first
derivatives there, and the 1-jet of the last term at Σ^IVP is O(ε²) at each point: the term vanishes there, so do its
tangential derivatives, and its t_IVP-derivative is r⁻¹(h_1(ε) − εḣ_1) = O(ε²). So the 1-jet of g_ε at Σ^IVP has the
ε-derivative at ε = 0 of that of g + εḣ. Differentiating at ε = 0 gives (1) and (2).

(3) We use g + sḣ, not g_ε, since differentiating along g_ε would need the ε-derivative of its 2-jet. For |s| small
g + sḣ is Lorentzian near any compact piece of Σ^IVP, and there the Gauss and Codazzi equations give
(G_(g+sḣ) Ric(g + sḣ))(n_s, ·) = 𝒞(γ_s, k_s) at Σ^IVP, with (γ_s, k_s) the data g + sḣ induces and n_s its future unit
normal. Both sides are smooth in s. Differentiate at s = 0. On the left, the variations of G_(g+sḣ) and n_s multiply
Ric(g) = 0, leaving (G_g DRic(ḣ))(n, ·). On the right, (d/ds)(γ_s, k_s)|_(s=0) = (γ̇, k̇) by (1), so the derivative is
D𝒞(γ̇, k̇) = 0. ∎

**Proposition {#prop:viii-1-2}** (The linear initial solution; [[prop:iii-k-1-2]] linearised at zero data.) Let
(γ̇, k̇) be as in [[lem:viii-1-1]] and satisfy the linearised constraint equations. There is a unique ḣ on 𝒟, in the
classes named in the proof, with

    L^♮ḣ = 0,        ḣ = ḣ_0,   rℒ_(∂_(t_IVP))ḣ = ḣ_1   on Σ^IVP,                                          {#eq:viii-1-1}

and:

(1) Υ̇^♮(ḣ) = 0 and DRic(ḣ) = 0 on 𝒟; on 𝒟 ∩ Ω_*, Υ̇(ḣ) = 0;

(2) on 𝒟 ∩ Ω_*, ḣ ∈ H̄^(∞,(⟨ℰ^C_I⟩,ℓ_I))_b (orders at ℐ⁺; the set is bounded in t_*), and for each k there are k′ and
C_k with ‖ḣ‖_(H^k) ≤ C_k‖(γ̇, k̇)‖_(H^(k+k′)).

*Proof.* *The solution.* As in the proof of [[prop:iii-k-1-2]], 𝒟 is the union of 𝒟 ∩ Ω_(ext,r_1), of
𝒟⁺ = 𝒟 ∩ {t_IVP ≥ 0} and of the compact set 𝒦⁻ ([[lem:s27-cover]] (b), (e)); the solution is found on each, the three
agree where two of them are defined, and they are glued across Σ^IVP. The linear theorems take the place of the
nonlinear ones. The data lie in H^(∞,ℓ^♭_0)_b, as ℓ^♭_0 < min Re ℰ_0 and ℓ^♭_0 < ℓ_0 (the first step of the proof of
[[thm:iii-c1-3-1]]).

- *Exterior.* On Ω_(ext,r_1) (the radius r₀ of [[thm:iv2-2-4]] being r_1), L^♮ = L^(χ_0)_(g,g) ([[lem:iii-k-1-1]] (c)).
  [[thm:iv2-2-4]] with [[cor:iv2-4-1]], at h = 0 and α₀ = ℓ^♭_0, gives the unique
  ḣ ∈ H^(k,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω_(ext,r_1)) with these data, bounded by [[eq:iv2-2-3]], whose tame term vanishes at
  h = 0. [[lem:iv2-2-2]], which it uses, covers the past slab.

- *Forward part.* [[thm:iv3-2-1]] with g_0 := g, h = 0, α_0 := ℓ^♭_0 and f = 0, with the data (ḣ_0, ḣ_1) on Σ^IVP,
  gives for every k ≥ 2 a solution ḣ ∈ H^(k,ℓ^♭_0,(−,ℓ^♭_I))_b(𝒟⁺), the same for every k by its uniqueness clause,
  bounded by [[eq:iv2-2-3]], whose tame term vanishes at h = 0; on 𝒟⁺, L^♮ = L^(χ^♮_0)_(g,g). On
  Ω_(ext,r_1) ∩ {t_IVP ≥ 0} it equals the exterior solution: both solve the forward problem there with the data on
  Σ^IVP_(r_1), and their difference vanishes by the forward parts of [[lem:iv2-2-2]] and [[lem:iv2-2-3]], as in the
  uniqueness of [[thm:iv2-2-4]] (the last clause of [[thm:iv3-2-1]]).

- *Backward part.* 𝒦⁻ is compact, and for the reversed time orientation it is the domain of dependence of
  Σ^IVP ∩ {r ≤ 2R_8} within 𝒟⁻ = 𝒟 ∩ {t_IVP ≤ 0}: a compact set of the second kind of [[sec:s27-local]]
  ([[lem:s27-cover]] (e), which holds for g). L^♮ is a linear operator with smooth coefficients and principal part
  ½□_g ⊗ id = −½g^(αβ)∂_α∂_β ⊗ id, □_g as in [[eq:iii-b-6-7]], that is with principal symbol ½g⁻¹(ζ, ζ) Id
  (∂ → iζ): this is the normal form of the gauge of [[sec:s27-local]], at h = 0. Its only data are those on
  Σ^IVP ∩ 𝒦⁻. The linear local theory (L) of [[sec:s27-local]], with 𝒦′ := 𝒦⁻, then gives ḣ on 𝒦⁻, backward from
  Σ^IVP to {t_IVP = −ν}, unique in H²(𝒦⁻), and bounded in H^(k+1)(𝒦⁻) for every k ≥ 4 by finitely many norms of the
  data; uniqueness also follows from [[lem:ii-f-1-3]]. On Ω_(ext,r_1) ∩ 𝒦⁻, which lies in the past slab, it equals
  the exterior solution, by the uniqueness clause of (L), as in the proof of [[prop:iii-k-1-2]] (*Backward part*).

*Gluing.* 𝒟⁺ ∩ 𝒦⁻ = Σ^IVP ∩ {r ≤ 2R_8}, where both solutions take the data, and each point of 𝒟 off
Σ^IVP ∩ {R_ν ≤ r ≤ r_1} has a neighbourhood in 𝒟 contained in one of the three sets, as in the proof of
[[prop:iii-k-1-2]] (*Gluing*). Near a point p of Σ^IVP with R_ν ≤ r(p) ≤ r_1 and for m ≥ 2, the forward solution is
the restriction to {t_IVP ≥ 0} of a C^m tensor u_1 on a small coordinate ball V about p (Sobolev embedding, its class
imposing H^k away from infinity for every k), and the backward one the restriction of the solution u_2 on the slab of
the proof of (L), which is C^m and solves L^♮u_2 = 0 below Σ^IVP near p, beyond 𝒟 as well. [[lem:s27-gluing]], for
the linear operator L^♮, with A₁ := V ∩ {t_IVP ≥ 0}, A₂ := V ∩ {t_IVP ≤ 0} and the one hypersurface Σ^IVP ∩ V,
spacelike for g, shows that ḣ is C^m on V ∩ 𝒟. So ḣ is smooth on 𝒟, up to its boundary.
*The uniqueness classes:* H^(max(k,1),ℓ^♭_0,(−,ℓ^♭_I))_b of [[thm:iv2-2-4]] on Ω_(ext,r_1), that of [[thm:iv3-2-1]] on
𝒟⁺, H^(max(k,2),ℓ^♭_0,(−,ℓ^♭_I))_b(𝒟⁺) (k ≥ 1), and H² on 𝒦⁻ ((L) of [[sec:s27-local]]). Each
is preserved by every isometry of g that fixes t and |x|, the weights being functions of (t, |x|) ([[eq:iii-b-2-2]])
and ρ′_I a function of (t, |x|) ([[sec:s27-cover]]).

*(2).* On Ω_(ext,r_1) this is the proof of [[thm:iii-c1-3-1]] for L^(χ_0) ([[lem:iii-c2-2-1]]). There
L^(χ_0)_(g,g)ḣ = 0, with [[lem:iii-c2-2-1]] giving the structure of [[prop:iii-c-4-4]] for L^(χ_0); so [[eq:iii-c1-3-4]]
holds with right side 0 and [[eq:iii-c1-3-5]] without its integral, and every step is linear in the data. Its
[[eq:iii-c1-3-2]] becomes ‖ḣ‖_(H^(k,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b) ≤ C_k‖(ḣ_0, ḣ_1)‖_(H^(k_0,(ℰ_0,ℓ_0))_b), a linear map
continuous at 0 being bounded. On 𝒮, the proof of [[cor:iv3-2-3]] (the proof of [[thm:iii-c1-3-1]] on Ω^♮) gives the
same, with the data on Σ_c bounded by (L) on 𝒦. On 𝒦 there is nothing at ℐ⁺. [[lem:viii-1-1]] bounds
(ḣ_0, ḣ_1) by (γ̇, k̇).

*(1).* This is the argument of [[prop:iii-k-1-2]] (2), linearised. Put η̇ := Υ̇^♮(ḣ). By [[eq:viii-0-1]] and
[[eq:viii-1-1]], DRic(ḣ) = δ*_(g,E_C)η̇. The second Bianchi identity δ_g̃ G_g̃ Ric(g̃) = 0 holds for every metric g̃.
Differentiated at the Ricci-flat g, the variation of δ_g̃ G_g̃ multiplies Ric(g) = 0, so δ_g G_g DRic(k) = 0 for
every k. Hence δ_g G_g δ*_(g,E_C)η̇ = 0 on 𝒟. This operator has the principal symbol of δ_g G_g δ*_g, which is
½g⁻¹(ζ, ζ) times the identity ([[lem:ix-2-1]] (a)), as δ*_(g,E_C) − δ*_g is of order 0 ([[def:iii-b-6-1]]). At
Σ^IVP, η̇ = Υ̇⁰(ḣ) = 0 by [[lem:viii-1-1]] (2). Also (G_g δ*_(g,E_C)η̇)(n, ·) = (G_g DRic(ḣ))(n, ·) = 0 there by
[[lem:viii-1-1]] (3), so [[lem:iii-k-4-1]], with g for its metric, Σ^IVP for its Σ and n for its unit normal ν, gives
∂_nη̇ = 0. So the Cauchy data of η̇ vanish, and η̇ = 0 on 𝒟 by [[lem:ii-f-1-3]], forward and backward of
Σ^IVP, as in the proof of [[prop:iii-k-1-2]] (2). Then DRic(ḣ) = 0, and Υ̇ = Υ̇^♮ on Ω_*. ∎

### The linear solution {#sec:viii-2}

**Lemma {#lem:viii-2-1}** (The source.) Let ḣ be given by [[prop:viii-1-2]]. χ_−(t^♭_*)ḣ is defined on
Ω_* ∩ {t^♭_* ≤ T̂ + 2} ⊂ 𝒟; extend it by 0 to Ω_*, and put

    f := −L(χ_−(t^♭_*)ḣ)     on Ω_*.                                                                       {#eq:viii-2-1}

Then f = −[L, χ_−(t^♭_*)]ḣ is supported in {T̂ + 7/4 ≤ t^♭_* ≤ T̂ + 2}, f ∈ ℱ^∞_ex, and
‖f‖_(ℱ^k_ex) ≤ C_k‖(γ̇, k̇)‖_(H^(k+k′_k)), with k′_k as in [[lem:iii-k-2-2]] (d).

*Proof.* On 𝒟 ∩ Ω_*, Lḣ = L^♮ḣ = 0 by [[eq:viii-0-1]] and [[eq:viii-1-1]]. So L(χ_−ḣ) = [L, χ_−]ḣ, a first-order
operator applied to ḣ, with coefficients supported in supp dχ_−(t^♭_*) ⊂ {T̂ + 7/4 ≤ t^♭_* ≤ T̂ + 2}. This set is
bounded in t_*, so f vanishes near ι⁺ and K⁺. It vanishes on {t^♭_* < T̂ + 7/4}, which gives the supported character
of ℱ_ex. Near ℐ⁺, χ_−ḣ has the orders (⟨ℰ^C_I⟩, ℓ_I) by [[prop:viii-1-2]] (2), as in [[lem:iii-k-2-2]] (c).
[[prop:iii-c-5-2]] with g_1 = g_0 = g and h = 0 then puts L(χ_−ḣ) in the orders (⟨ℰ^C_I + 1⟩′, ℓ_I + 1) of ℱ_ex
there, continuously, as [[lem:iii-k-2-2]] (c) uses [[cor:iii-c-5-3]]. The bound follows from [[prop:viii-1-2]] (2). ∎

**Theorem {#thm:viii-2-2}** (Linear stability of Schwarzschild–Tangherlini in dimension 4 + 1.) Let
γ̇ ∈ H^(∞,(ℰ_0,ℓ_0))_b(Σ^IVP) and k̇ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b(Σ^IVP) satisfy the linearised constraint equations at
(γ_(b₀), k_(b₀)). Then there are U′ ∈ 𝒟^∞_ex with components ḃ ∈ 𝔟, S′ ∈ 𝒮_1 (boost) and S⁰′ := S′^(0)_1 ∈ 𝒮_1
(translation) ([[def:iii-j-1-1]]), and a symmetric 2-tensor ġ on Ω_* ∪ 𝒟, all linear in (γ̇, k̇), with:

(1) DRic(ġ) = 0 on Ω_* ∪ 𝒟;

(2) ġ = ḣ + ġ_(S′) + ġ⁰_(S⁰′) on 𝒟′ ([[sec:viii-0]]), with ḣ of [[prop:viii-1-2]] and ġ_(S′), ġ⁰_(S⁰′) of
[[eq:viii-0-2]]; so ġ − ġ_(S′) − ġ⁰_(S⁰′) induces the linearised data (γ̇, k̇) on Σ^IVP ([[lem:viii-1-1]] (1)), and
ġ induces them up to the data of the linearised diffeomorphism −ℒ_(V(S′)+V⁰(S⁰′))g;

(3) on Ω_* ∩ {t^♭_* ≥ T̂ + 2}, ġ = D_0𝔤(U′), the derivative at U = 0 of

    𝔤(U) := g_(p⃗) + h_tot(p⃗) + h_(b,rem)(q) + h,        (h, p⃗, q) = Φ(U),

with g_(p⃗) the translated background of [[eq:iii-i7-1-3]] ([[sec:viii-0]]): the metric of [[thm:iii-k-4-3]] (3); and
D_0Φ(U′) = (h′, p⃗′, q′) with h′ ∈ 𝒳^∞_(J,ex) and q′ ∈ 𝒬_ex ([[prop:iii-j3-5-4]]);

(4) where χ_K = 1,

    ġ − ∂_b g_b|_(b=b₀)(ḃ) = h_(b₀,rem)(q′) + h′.                                                          {#eq:viii-2-2}

So for every R′, ε′ > 0 and i, β there are C, k₁ and T′ with

    |(t_*∂_(t_*))^i ∂^β_x (ġ − ∂_b g_b|_(b₀)(ḃ))| ≤ C‖(γ̇, k̇)‖_(H^(k₁)) t_*^(−(α−2)+ε′)
                                                                  on {r_♭ ≤ r ≤ R′, t_* ≥ T′};             {#eq:viii-2-3}

and if, for a given ε_t < ε_K, α is chosen with α > 4 + ε_t, then ε′ := α − 4 − ε_t gives
ġ − ∂_b g_b(ḃ) = O(t_*^(−2−ε_t)) there. Such α exist, as ε_K does not depend on ε_t and the admissible α are dense in
(4 + ε_K − ε′_0, 4 + ε_K] ([[def:iii-j-a-j]], [[lem:iii-j3-1-4]]);

(5) the linearised gauge 1-form vanishes: on Ω_*,

    η̇ := Υ̇(ġ) + D_2Υ^(E_Υ)(g, g)(ġ_(p⃗′)) − Dϑ_tot(p⃗′) = 0,        ġ_(p⃗′) := D_0 g_(p⃗)(U′),

and on 𝒟′, Υ̇^♮(ġ) + D_2Υ^(χ^♮_0E_Υ)(g, g)(ġ_(S′) + ġ⁰_(S⁰′)) = 0. These are the derivatives of the two lines of the
gauge 1-form κ of [[prop:iii-k-4-2]]: of Υ^(E_Υ)(𝔤(U) + k, g_(p⃗)) − ϑ_tot(p⃗) at (U, k) = (0, 0) in the direction
(U′, χ_−(t^♭_*)ḣ), and of Υ^(χ^♮_0E_Υ)(φ*_(−sS′,−sS⁰′)g + sḣ, φ*_(−sS′,−sS⁰′)g) at s = 0;

(6) |ḃ| + |S′| + |S⁰′| + ‖U′‖_(𝒟^k_ex) ≤ C_k‖(γ̇, k̇)‖_(H^(k+k′)).

*Proof.* *Step 1 (the right inverse at Tangherlini).* At zero data, h_(S,S⁰) = 0 for every (S, S⁰)
([[prop:iii-k-1-2]] (3)), so Ψ = Φ ([[eq:iii-k-2-1]]). [[lem:iii-k-2-3]] at zero data and U = 0 gives a linear
ℛ : ℱ^∞_ex → 𝒟^∞_ex with D_0(P_5 ∘ Φ)(ℛf) = f, bounded by the tame estimate of [[thm:iii-j2-4-2]] on the exact scales
([[cor:iii-j3-6-6]]), which at U = 0 reads ‖ℛf‖_(𝒟^k_ex) ≤ C_k‖f‖_(ℱ^(k+d)_ex), d its loss. The tail of U = 0
vanishes everywhere, so the support clause of [[lem:iii-k-2-3]] applies with c := T̂ + 7/4: if f vanishes on
{t^♭_* < T̂ + 7/4}, so does the tail of ℛf. Put U′ := ℛf with f of [[lem:viii-2-1]]. Its tail h̃′ vanishes on
{t^♭_* < T̂ + 7/4}, and (6) follows from [[lem:viii-2-1]].

*Step 2 (the equation in the cone).* For U small and a symmetric 2-tensor k on Ω_*, the equation of the proof of
[[prop:iii-k-4-2]] gives, with zero data,

    P_5(Φ(U) + (k, 0, 0)) = Ric(𝔤(U) + k) − δ*_(𝔤_0(U),E_C)(Υ^(E_Υ)(𝔤(U) + k, 𝔤_0(U)) − ϑ_tot(p⃗)),
                                                                                       𝔤_0(U) := g_(p⃗),

which is P_5(Ψ(U)) of [[ch:s27]] for k = χ_−h_(−S,−S⁰), S and S⁰ := S^(0)_1 the boost and translation components of U.
The right side is smooth in (U, k). Φ is smooth ([[thm:iii-j-2-4]]; on the exact classes [[prop:iii-j3-5-4]]), g_(p⃗) is
smooth in p⃗ ([[sec:viii-0]]; [[lem:iii-i7-1-3]] (a)), and h_tot, ϑ_tot and h_(b,rem) are smooth in (p⃗, q)
([[def:iii-i7-2-3]], [[def:iii-i8-2-1]], [[def:iii-i9-2-1]], [[def:iii-i9-2-3]], [[def:iii-i14-1-2]]). At
(U, k) = (0, 0) the metric is g and the gauge 1-form vanishes, so the variation of δ*_(𝔤_0(U),E_C) drops out.
Differentiating at (0, 0) in the direction (U′, χ_−ḣ) gives

    DRic(ġ) − δ*_(g,E_C)η̇ = D_0(P_5 ∘ Φ)(U′) + L(χ_−ḣ) = f − f = 0     on Ω_*,                            {#eq:viii-2-4}

with ġ := D_0𝔤(U′) + χ_−ḣ and η̇ as in (5). Here D_hP_5(0)(k) = Lk, since at U = 0 the right side is P(g + k, g).

*Step 3 (the initial part of the cone).* On Ω_* ∩ {t^♭_* < T̂ + 7/4}, for every U: χ_K = 0, so
g_(p⃗) = φ*_(−S,−S⁰)g ([[sec:viii-0]]), with S and S⁰ the boost and translation components of U; h_tot(p⃗) and
ϑ_tot(p⃗) vanish, being supported in supp χ_K (h_tot in 𝒞 ⊂ supp χ_K; [[lem:iii-i7-2-2]] and the definitions cited in
Step 2), and h_(b,rem)(q) vanishes, carrying χ_K; and the metric component of Φ(U) is h̃, as χ_ι = 0 there (the proof
of [[lem:iii-k-2-2]]). So there ġ_(p⃗′) = ġ_(S′) + ġ⁰_(S⁰′) ([[sec:viii-0]]), Dϑ_tot(p⃗′) = 0,
D_0𝔤(U′) = ġ_(S′) + ġ⁰_(S⁰′) + h̃′ = ġ_(S′) + ġ⁰_(S⁰′) (Step 1) and χ_− = 1, whence

    ġ = ġ_(S′) + ġ⁰_(S⁰′) + ḣ,        η̇ = Υ̇(ḣ) + (D_1 + D_2)Υ^(E_Υ)(g, g)(ġ_(S′) + ġ⁰_(S⁰′)) = 0.

The first term vanishes by [[prop:viii-1-2]] (1). The second is
(d/ds)Υ^(E_Υ)(φ*_(−sS′,−sS⁰′)g, φ*_(−sS′,−sS⁰′)g)|_(s=0), by the chain rule and [[sec:viii-0]], and this is 0, as
Υ^(E_Υ)(g_0, g_0) = 0 for every metric g_0 ([[sec:viii-0]]).

*Step 4 (propagation).* By [[eq:viii-2-4]] and the linearised Bianchi identity (the proof of [[prop:viii-1-2]]),
δ_gG_gδ*_(g,E_C)η̇ = 0 on Ω_*. η̇ vanishes on Ω_* ∩ {t^♭_* < T̂ + 7/4}, which contains Ω_* ∩ {t^♭_* ≤ 2} (T̂ ≥ 2).
[[lem:ii-f-1-3]] on Ω_*° with τ := t^♭_* and c := 3/2, as in the proof of [[prop:iii-k-4-2]], gives η̇ = 0. Its
hypotheses hold. dt^♭_* is past timelike for g ([[lem:ii-c-3-2]] (2) at h = 0), so t^♭_* is a time function on Ω_*°.
The compact sets are those of [[lem:ii-f-1-4]] (a) with θ = 0, which applies to g: along future causal curves of g,
t_* is non-decreasing and B := t_* + R̃(r) is a time function, and near the inner boundary past causal curves stay in
{r ≥ min(r(p), r^♮)}, as dr is future timelike on {r_♭ ≤ r ≤ r^♮} ([[lem:ii-c-3-2]] (1) at h = 0). So for p ∈ Ω_*°
with t^♭_*(p) > c, J⁻_(Ω_*°)(p) ∩ {t^♭_* ≥ c} lies in

    L′_p := {c ≤ t^♭_* ≤ t^♭_*(p),  B ≤ B(p),  r ≥ min(r(p), r^♮)},

t^♭_* being a time function: this is the set L′_p of [[eq:ii-f-lp-prime]] ([[lem:ii-f-1-4]] (a)) with X := Ω_*°,
τ′ := t^♭_* (≤ t_*) and C′ := C_♭, which drops the condition t_* ≤ t_*(p) of [[eq:ii-f-lp]] as C_♭t_* ≤ t^♭_*. L′_p is
compact, as B bounds r there (c ≤ t_* ≤ t^♭_*(p)/C_♭, R̃(r) ≤ B(p) − c, and R̃(r) = r for r ≥ r′_0 + 1), and it lies in
Ω_*°, as t^♭_* ≥ c > 1 and r ≥ min(r(p), r^♮) > r_♭ on it. ([[lem:iii-k-6-1]] (c) at h = 0 gives such sets as well.) So
DRic(ġ) = 0 on Ω_* by [[eq:viii-2-4]].

*Step 5 (the initial region).* On 𝒟′ put ġ := ḣ + ġ_(S′) + ġ⁰_(S⁰′). DRic(ḣ) = 0 ([[prop:viii-1-2]] (1)) and
DRic(ġ_(S′)) = DRic(ġ⁰_(S⁰′)) = 0 ([[sec:viii-0]]). The gauge 1-form of (5) on 𝒟′ is
Υ̇^♮(ḣ) + (D_1 + D_2)Υ^(χ^♮_0E_Υ)(g, g)(ġ_(S′) + ġ⁰_(S⁰′)) = 0 + 0, as in Step 3, Υ^(χ^♮_0E_Υ)(g_0, g_0) vanishing for
every metric g_0. On Ω_* ∩ 𝒟′ = Ω_* ∩ {t^♭_* < T̂ + 7/4} the two definitions of ġ agree (Step 3), and so do those of
the gauge 1-form, χ^♮_0 being 1 there. As Ω_* ∪ 𝒟′ = Ω_* ∪ 𝒟, this gives (1), (2) and (5).

*Step 6 ((3) and (4)).* On {t^♭_* ≥ T̂ + 2}, χ_− = 0, so ġ = D_0𝔤(U′); this is (3), with D_0Φ(U′) in the exact
classes by [[prop:iii-j3-5-4]]. Where χ_K = 1: g_(p⃗) = g_b for every p⃗ ([[eq:iii-i7-1-3]]), so
ġ_(p⃗′) = D_0 g_(p⃗)(U′) = ∂_b g_b|_(b₀)(ḃ); h_tot(p⃗) vanishes for every p⃗, each of its terms carrying a factor dχ_K
([[def:iii-i4-2-1]], [[def:iii-i7-2-1]], [[def:iii-i8-2-1]], [[def:iii-i9-2-1]]), so its derivative vanishes;
h_(b,rem)(q) is linear in q for each b ([[eq:iii-i14-1-2]]), so its derivative at (b₀, 0) in the direction (ḃ, q′) is
h_(b₀,rem)(q′); and the derivative of h is h′. This is [[eq:viii-2-2]].

*The rate.* This is the argument of [[cor:s27-rate]] (c). On {r ≤ R′} and for t_* large, χ_K = 1, as supp(1 − χ_K) is
disjoint from a neighbourhood of K⁺ ([[lem:iii-i14-2-2]] (c)). h′ has K⁺-order α−, and h_(b₀,rem)(q′) has K⁺-order
(α − 2)−, each seminorm bounded by one of q′ ([[lem:iii-i14-2-2]] (a)). Near the interior of K⁺, ρ_K = t₀⁻¹ with
t₀ = t − |x| ([[eq:iii-b-2-2]], [[eq:iii-b-4-1]]), comparable to t_* on {r ≤ R′}, and the b-vector fields there are
spanned by t_*∂_(t_*) and ∂_x. By b-Sobolev embedding for the b-density μ_b of [[sec:iii-i-1]], as in the proof of
[[lem:iii-i-2-2]] (a weight is then the pointwise order), (t_*∂_(t_*))^i ∂^β_x of a function of K⁺-order w− is
O(t_*^(−w+ε′)), bounded by a seminorm of it. With w = α − 2, (6) and the tame bound for D_UΦ at U = 0
([[prop:iii-j3-5-4]]), ‖D_0Φ(U′)‖_k ≤ C_k‖U′‖_(𝒟^(k+d)_ex), this is [[eq:viii-2-3]]. The bound on α is the choice of
α in step (4) of [[thm:vi-c-2-1]] (row w2 of [[sec:vi-c-1]]), made with α > 4 + ε_t. ∎

**Corollary {#cor:viii-2-3}** (In the class.) Let G act as in [[sec:s27-class]], and make the choices of [[lem:vii-3-1]]
equivariant. If (γ̇, k̇) are G-invariant, [[thm:viii-2-2]] holds with U′ fixed by G, ḃ = (ṁ, 0), S′ = S⁰′ = 0 and ġ
G-invariant. So ġ = ḣ on 𝒟′, near Σ^IVP, and it induces (γ̇, k̇); and where χ_K = 1

    ġ − ṁ ∂_m g_((m,0))|_(m=m₀) = h_(b₀,rem)(q′) + h′,

with the rate [[eq:viii-2-3]]: the perturbation settles to a change of mass alone, as O(t_*^(−2−ε_t)) on spatially
compact sets.

*Proof.* G acts on M fixing t, t_*, t_IVP, t^♭_* and |x|, so it preserves Σ^IVP, Ω_*, 𝒟 and the support classes. It
acts on 𝒟^k_ex and ℱ^k_ex boundedly, isometrically for the norms sup_(σ∈G)|σ · (·)|_k, and Π := ∫_G σ dσ projects
onto the fixed elements and preserves every support class (the proof of [[prop:vii-3-2]]). The construction of
[[lem:viii-1-1]] is natural: it sets ḣ_0 := γ̇ with ḣ_0(n, ·) := 0 and solves tensorial linear equations for ḣ_1
uniquely, as [[lem:vii-3-1]] records for [[prop:iii-c2-4-1]]. So ḣ_0, ḣ_1 are G-invariant. L^♮ is natural, its
cut-offs being functions of (t_IVP, |x|) and t_* and its gauge 1-forms radial ([[lem:vii-3-1]] (C1)–(C2)). So σ_*ḣ
solves [[eq:viii-1-1]] for σ ∈ G, and ḣ is G-invariant by the uniqueness in [[prop:viii-1-2]], whose classes G
preserves. χ_− is a function of t^♭_*, so f is G-fixed. Differentiating P_5(Ψ(σ · U)) = σ_*P_5(Ψ(U))
([[lem:vii-3-1]]) at the fixed point U = 0, at zero data, gives D_0(P_5 ∘ Φ) ∘ σ = σ_* ∘ D_0(P_5 ∘ Φ). So U″ := Πℛf
satisfies D_0(P_5 ∘ Φ)(U″) = Πf = f. Its tail vanishes on {t^♭_* < T̂ + 7/4}, and it is bounded as in (6). Run Steps
2–6 of the proof of [[thm:viii-2-2]] with U″ in place of U′. U″_0 = (ḃ, S′, S⁰′) lies in
𝔟^G × 𝒮_1^G × 𝒮_1^G = (ℝ × {0}) × 0 × 0, as 𝔟 = ℝ × 𝔰𝔬(4), 𝒮_1 ≅ ℝ⁴ as a representation (for the boost and for the
translation components alike), and (ℝ⁴)^G = 0, 𝔰𝔬(4)^G = 0 ([[sec:s27-class]]). So ġ_(S′) = ġ⁰_(S⁰′) = 0, and ġ is
G-invariant, every ingredient being equivariant and U″ fixed. ∎

**Remark {#rem:viii-2-4}** (What is and is not asserted.) (a) [[thm:viii-2-2]] has the form of [[thm:settling]]: every
linearised data set in the class has a linearised vacuum development, in a fixed gauge, that settles at the stated
rate. By itself it does not assert that a given linearised solution in another gauge differs from ġ by a linearised
diffeomorphism. That comparison, on the future N⁺ of Σ^IVP in {r > r_♭}, is [[thm:ix-2-2]] and [[cor:ix-2-3]] below,
by a linear wave equation for the 1-form that generates the change of gauge; it is the linear counterpart of the
nonlinear comparison of [[rem:vii-4-1]] ([[lem:interior-one-spacetime]]). Nothing in [[sec:viii-1]]–[[sec:viii-2]]
uses it. (b) The rate is that of the slowest term at K⁺, h_(b₀,rem)(q′), which carries the decaying tails of the
parameter and centre-of-mass motions ([[eq:iii-i14-1-2]]).

### The comparison of gauges: setting and conventions {#sec:ix-0}

This section and the next two compare the solution ġ of [[thm:viii-2-2]] with a linearised vacuum solution given in
another gauge, on the whole future of Σ^IVP in {r > r_♭}: the future half of the Cauchy development of
Σ^IVP ∩ {r > r_♭} ([[lem:ix-1-2]]).

*The spacetime.* g := g_(b₀) on M_♭ := ℝ_t × {|x| ≥ r_♭}, in the coordinates (t, x) of [[sec:iii-b-3]]
([[eq:iii-b-3-3]] defines g_(b₀) there, by [[lem:s11-ks-domain]]), with interior M°_♭ := ℝ_t × {|x| > r_♭}. t_IVP is
the function of [[lem:iii-b-3-7]] (b), and Σ^IVP := t_IVP⁻¹(0). ν is the function of [[prop:iii-k-1-2]], smooth and
non-decreasing with ν = 0 on [0, R_ν], R_ν = ½(r_♭ + 5R₁), and ν > 0 on (R_ν, ∞); so ν ≥ 0, but ν is not positive
everywhere. N_ν = {t_IVP ≥ −ν(|x|)} is the set of [[sec:viii-0]]. On {|x| ≤ R_ν}, then, N_ν ends at Σ^IVP, which is
there part of its boundary, and ġ is not defined to its past. So the comparison is posed in a region that extends past
Σ^IVP, where only g is used, and the tensors compared live on its future half. Put

    U^♯ := M°_♭ ∩ {t_IVP > −1},     Σ° := Σ^IVP ∩ M°_♭ ⊂ U^♯,     N⁺ := M°_♭ ∩ {t_IVP ≥ 0} ⊂ N_ν,

the inclusion as ν ≥ 0 (and t ≥ t_IVP ≥ 0 > −½|x| on N⁺, by [[lem:iii-b-3-7]] (b), so N⁺ lies in the spacetime M of
[[eq:iii-b-2-1]]). For an open U ⊂ U^♯ put Σ_U := Σ^IVP ∩ U and U_+ := U ∩ {t_IVP ≥ 0}.

*Smooth up to Σ_U.* U_+ is a manifold with boundary Σ_U, as dt_IVP ≠ 0. A tensor on U_+ is *smooth up to Σ_U* if it
is smooth on U ∩ {t_IVP > 0} and, in coordinates (t_IVP, y) near Σ_U, every derivative of its components extends
continuously to Σ_U. Such a tensor is the restriction to U_+ of a smooth tensor on an open neighbourhood of U_+ in U:
apply Seeley's extension operator ([[thm:std-seeley]]) in each chart {t_IVP ≥ 0}, after a cut-off, and patch with a
partition of unity subordinate to a cover of Σ_U by such charts and to U ∩ {t_IVP > 0}.

**Lemma {#lem:s29-g-on-n}** (The domain of ġ.) Ω_* ∪ 𝒟 = N_ν. The tensor ġ of [[thm:viii-2-2]] is a smooth symmetric
2-tensor on the interior of N_ν, with DRic(ġ) = 0 there, and its restriction to N⁺ is smooth up to Σ°.

*Proof.* *The domain.* Ω_* = cl_M{t^♭_* ≥ 1} lies in N_ν, as t_IVP ≥ t_* ≥ t^♭_* there ([[sec:viii-0]];
[[lem:iii-b-3-7]], [[lem:ii-c-3-2]] (b)). A point of N_ν has either t^♭_* > T̂ + 3 ≥ 1, so lies in Ω_*, or lies in
𝒟 = N_ν ∩ {t^♭_* ≤ T̂ + 3}, with the convention of [[sec:viii-0]] that this sublevel set contains the points where
t^♭_* is not defined. So Ω_* ∪ 𝒟 = N_ν, and DRic(ġ) = 0 there ([[thm:viii-2-2]] (1)).

*ḣ is smooth on the interior of 𝒟.* The proof of [[prop:viii-1-2]] gives ḣ on two closed sets that cover 𝒟: the compact
set 𝒦 ([[lem:s27-cover]] (c)), and the closure 𝒜 of Ω^♮ = Ω_(ext,r_1) ∪ 𝒮 in 𝒟, on which ḣ is the solution of
[[thm:iv3-2-1]], equal to the exterior solution on Ω_(ext,r_1), with its past slab. On each of the two, near each of its
points in the interior of M, ḣ is for every k the restriction of a tensor of class H^k on a neighbourhood: on 𝒦 by (L)
of [[sec:s27-local]], its data being smooth and H^k(𝒦) consisting of restrictions; on 𝒜 because ḣ lies, for every k, in
the classes of order k of [[thm:iv2-2-4]] and [[thm:iv3-2-1]], b-Sobolev spaces of restrictions ([[sec:iii-c-2]]), which
near points of the interior of M are the spaces H^k. Fix an interior point q of 𝒟 and m ≥ 2. By Sobolev embedding on ℝ⁵,
for k > m + 5/2, there are a coordinate ball V ∋ q in the interior of 𝒟 and u_1, u_2 ∈ C^m(V) with ḣ = u_1 on 𝒦 ∩ V and
ḣ = u_2 on 𝒜 ∩ V. Put Γ := 𝒦 ∩ 𝒜 ∩ V and w := u_1 − u_2. If Γ is empty, the connected V lies in one of the two closed
sets, and ḣ is C^m on V. Otherwise ḣ is C^m on V by (i) and (ii) below. As q and m are arbitrary, ḣ is smooth on the
interior of 𝒟.

(i) *Every derivative of w of order at most m vanishes on Γ.* In the interior of 𝒟, 𝒦 meets 𝒜 only on three spacelike
hypersurfaces ([[lem:s27-cover]] (c), [[lem:iii-c1-1-1]]): Σ^fut_(r_1) ∩ {ρ′_I ≥ c}, with 𝒦 above it and Ω_(ext,r_1)
below; Σ^past_(r_1) where 𝒦 reaches below the past slab, with Ω_(ext,r_1) above it; and {ρ′_I = c}, with 𝒦 below it and
𝒮 above. Let p ∈ Γ lie on only one of them, H, so that near p the set 𝒦 lies on one side of H and 𝒜 on the other. In the
proof of [[prop:viii-1-2]] the solution on one side gives the solution on the other its Cauchy data on H; so u_1 and u_2
have the same restriction and the same first transversal derivative on H near p, and w and its first derivatives vanish
there. Take coordinates (s, y) near p with H = {s = 0}. As H is spacelike, g⁻¹(ds, ds) < 0, and the principal part
½□_g ⊗ id of L^♮ gives 2L^♮ = −g⁻¹(ds, ds)∂²_s + R, with R of order 2 and of order at most 1 in ∂_s: H is
noncharacteristic. L^♮u_1 = 0 on the interior of 𝒦, which lies on one side of H near p; so every derivative of L^♮u_1 of
order at most m − 2 vanishes on H near p, by continuity. Likewise for L^♮u_2, from the side of 𝒜. So ∂^(j−2)_s L^♮w = 0
on H near p for 2 ≤ j ≤ m. If every derivative of w of order below j vanishes on H near p, so does every derivative of
order j with at most j − 1 factors ∂_s, a tangential derivative of one of order below j; and the identity gives
∂^j_s w = 0 there. By induction on j, as in Step 3 of the proof of [[thm:ix-2-2]], every derivative of w of order at
most m vanishes on H near p. The other points of Γ lie on two of the three hypersurfaces, on one of two edges. The first
is {r = r_1, t_IVP = 0}, where Σ^fut_(r_1) and Σ^past_(r_1) bound the wedge Ω_(ext,r_1) and 𝒦 fills the rest of a
neighbourhood; its points are interior points of 𝒟, as ν(r_1) > 0 (r_1 > R_ν, as in the last step of this proof). The
second is the intersection of Σ^fut_(r_1) with {ρ′_I = c}, where 𝒦, Ω_(ext,r_1) and 𝒮 meet. ({ρ′_I = c} does not meet
Σ^past_(r_1) in Γ: its points in Γ lie in the closure of 𝒮, where t_IVP ≥ r/4 > 0 ([[lem:s27-cover]] (d)), while
t_IVP ≤ 0 on Σ^past_(r_1).) Each point of an edge is a limit of points of Γ that lie on only one of the three
hypersurfaces, and the derivatives of w of order at most m are continuous; so they vanish on the edges too.

(ii) *Gluing.* For a function v on V that vanishes on Γ, let v^Γ := v on 𝒦 ∩ V and v^Γ := 0 on 𝒜 ∩ V. If v ∈ C¹(V) and
its first derivatives vanish on Γ as well, then v^Γ is C¹ on V, with first derivatives (∂v)^Γ. Indeed V is the union of
Γ and of the open sets V ∖ 𝒜 ⊂ 𝒦 and V ∖ 𝒦 ⊂ 𝒜, on which v^Γ is v and 0. At p ∈ Γ, v(p) = 0 and ∂v(p) = 0, so
|v^Γ(p′)| ≤ |v(p′)| = o(|p′ − p|) as p′ → p: v^Γ is differentiable at p with derivative 0 = ∂v(p). And (∂v)^Γ is
continuous on V, its restrictions to the closed sets 𝒦 ∩ V and 𝒜 ∩ V, which cover V, being ∂v and 0. Applied to w and to
its derivatives of order below m, which vanish with their first derivatives on Γ by (i), this gives, by induction on the
order, w^Γ ∈ C^m(V) with ∂^βw^Γ = (∂^βw)^Γ for |β| ≤ m. So ḣ = u_2 + w^Γ, which is u_1 on 𝒦 ∩ V and u_2 on 𝒜 ∩ V, is C^m
on V.

*ġ is smooth on the interior of N_ν.* The interior of N_ν is covered by two open sets: its points with t^♭_* > 1,
which lie in the interior of Ω_*, and its points outside the closed set {t^♭_* ≥ T̂ + 7/4}, which lie in 𝒟′
([[sec:viii-0]]). On the second, ġ = ḣ + ġ_(S′) + ġ⁰_(S⁰′) ([[thm:viii-2-2]] (2)); ġ_(S′) and ġ⁰_(S⁰′) are smooth
([[eq:viii-0-2]]), and ḣ is smooth, as just shown. On the first, ġ = D_0𝔤(U′) + χ_−(t^♭_*)ḣ (Step 2 of the proof of
[[thm:viii-2-2]]). χ_−(t^♭_*)ḣ is smooth there: its points with t^♭_* < T̂ + 3 are interior points of 𝒟, where ḣ is
smooth, and it vanishes on {t^♭_* > T̂ + 2}. The derivative of 𝔤 is

    D_0𝔤(U′) = ġ_(p⃗′) + D_(p⃗)h_tot(0)(p⃗′) + h_(b₀,rem)(q′) + h′,

h_(b,rem)(q) being linear in q and vanishing at q = 0 for every b ([[eq:iii-i14-1-2]]). The first two terms are
smooth, g_(p⃗) and h_tot(p⃗) being smooth tensors depending smoothly on p⃗ ([[sec:viii-0]]; the definitions cited in
Step 2 of that proof). As U′ ∈ 𝒟^∞_ex, h′ ∈ 𝒳^∞_(J,ex) and q′ ∈ 𝒬_ex ([[prop:iii-j3-5-4]]): h′ lies in a b-Sobolev
class of infinite order, and h_(b₀,rem)(q′) is χ_K times smooth tensors applied to the components of q′, functions of
t_* of infinite b-regularity ([[eq:iii-i14-1-1]], [[eq:iii-i14-1-2]]); both are smooth on the interior of M. So ġ is
smooth on the interior of N_ν.

*Up to Σ°.* Where ν > 0, Σ° lies in the interior of N_ν, where ġ is smooth. Where ν = 0, Σ° is part of the boundary
of N_ν. Such points have r ≤ R_ν < r_1: R_ν = ½(r_♭ + 5R₁) < 5R₁, and r_1 ≥ R_6 ≥ R₃ > 5R₁ ([[sec:iii-k-0]],
[[sec:s27-cover]]), as ψ′_IVP = ψ′ > 0 at 5R₁ and ψ′_IVP = 0 on [R₃, ∞) (the proof of [[lem:iii-b-3-7]] (b)). So of
the cover of 𝒟 used in [[prop:viii-1-2]] only the compact part 𝒦 reaches them: Ω_(ext,r_1) ⊂ {r ≥ r_1}, and the slab
𝒮 lies in {|x| > R_9}, R_9 ≥ R₃ > 5R₁ > R_ν, and does not meet Σ^IVP, as t_IVP ≥ r/4 > 0 on 𝒮 ([[lem:s27-cover]] (a),
(d)). So a half-ball {t_IVP ≥ 0} about each such point lies in 𝒦. There ġ = ḣ + ġ_(S′) + ġ⁰_(S⁰′)
([[thm:viii-2-2]] (2)); ġ_(S′) and ġ⁰_(S⁰′) vanish on {|x| < 5R₁}, which contains these points ([[sec:viii-0]]), and
ḣ ∈ H^k(𝒦) for every k, up to Σ^IVP ((L) of [[sec:s27-local]]). In a chart {t_IVP ≥ 0} near such a point, H^k for
every k gives every derivative continuous up to Σ°: after a cut-off, extend by the operator of [[thm:std-ly-extension]],
bounded on every W^(k,2) of a half-space, and apply Sobolev embedding on ℝ⁵. ∎

*Time orientation.* As in [[lem:ii-b-1-1]], dt_* is past timelike. dt_IVP is timelike for g on M_♭
([[lem:iii-b-3-7]] (b)) and past timelike: both dt_* and dt_IVP are dt − φ′(|x|) d|x| with β := φ′ − T′_(m₀) in
(−1, 1] (the proof of [[lem:iii-b-3-7]]), so are all their convex combinations, which are therefore timelike, and the
two covectors lie in the same cone. So t_IVP is a time function on M°_♭ in the sense of [[sec:ii-f-1-4]]: it is
strictly increasing along future directed causal curves (the property [BGP, p. 24] records of a Cauchy time-function,
[[thm:std-bgp-causal]] (2); t_IVP is not claimed to be one). Hence Σ° is a smooth spacelike hypersurface of M°_♭,
acausal in every open subset of M°_♭.

*Operators.* For a 1-form w and a symmetric 2-tensor k: (δ_g k)_μ := −∇^α k_αμ, G_g k := k − ½g tr_g k,
δ*_g w := ½(∇w + (∇w)^T), so that ℒ_X g = 2δ*_g X^♭, as in [[sec:iii-b-6]]. DRic and Υ̇⁰, the derivative at (g, g)
in the first argument of Υ⁰, are as in [[sec:viii-0]], now on M_♭, Υ⁰ being defined pointwise by [[eq:iii-b-6-3]]. By
[[lem:iii-b-6-3]] ([[eq:iii-b-6-6]] at g₀ = g, where C_(g,g) = 0 and Y_(g,g) = 0, as Υ⁰(g, g) = 0),

    Υ̇⁰(k) = −δ_g G_g k,

so −Υ̇⁰(k) is the linearised harmonic gauge 1-form. Put

    L⁰ := DRic − δ*_g Υ̇⁰ = DRic + δ*_g δ_g G_g,                                                             {#eq:ix-0-1}

the operator L of [[eq:viii-0-1]] with E_C = E_Υ = 0.

*Linearised data.* As in [[lem:viii-1-1]] (1): a symmetric 2-tensor k, defined near a piece of Σ^IVP or on one side of
it up to Σ^IVP, *induces* the linearised data (γ̇, K̇), the s-derivatives at s = 0 of the first and second fundamental
forms of Σ^IVP for g + sk, with K(X, Y) := g(∇_X n, Y), the convention of [[lem:iii-b-3-9]]. They are linear in k and
depend only on its 1-jet at Σ^IVP; γ̇ is the restriction of k to TΣ^IVP. K is the second fundamental form, written
k_(b₀) for g in [[sec:viii-0]]–[[sec:viii-2]], where k̇ denotes its variation; so the linearised data (γ̇, k̇) of
[[thm:viii-2-2]] are a pair (γ̇, K̇) in the present notation, and the tensor ḣ of [[prop:viii-1-2]] induces them
([[lem:viii-1-1]] (1)).

*The Cauchy problem.* We use [[thm:std-bgp-causal]], [[thm:std-bgp-development]], [[def:std-normally-hyperbolic]] and
[[thm:std-bgp-cauchy]]. The two operators to which they are applied below, 2L⁰ and 2δ_gG_gδ*_g, have in local
coordinates the principal part −g^(αβ)∂_α∂_β ⊗ id ([[lem:ix-2-1]] (a)), which is the local form that
[[def:std-normally-hyperbolic]] gives: they are normally hyperbolic as they stand. (With ∂ → iζ their principal symbol
is g⁻¹(ζ, ζ) Id; [BGP] writes the same symbol −⟨ξ, ξ⟩ with ∂ → ξ.) [BGP]'s globally hyperbolic manifolds are connected
([[thm:std-bgp-causal]] (1)). A Cauchy development below may have several connected components, and every statement
taken from [BGP] is applied on each component C, with Cauchy hypersurface S ∩ C: components of an open set are open and
closed in it, so an inextendible causal curve of C is one of D(S) and meets S, and it does so in C.

### The Cauchy problem, and the domain {#sec:ix-1}

The proof of [[lem:ix-1-1]] uses two facts about slabs, which follow from [[thm:std-bgp-causal]] and
[[thm:std-bgp-development]].

**Lemma {#lem:s29-slabs}** (Slabs.) Let (Y, g) be globally hyperbolic and S a smooth spacelike Cauchy hypersurface.
There is a Cauchy time-function t on Y with S = t⁻¹(0) ([[thm:std-bgp-causal]] (3)); its level sets are smooth
spacelike Cauchy hypersurfaces, and t is strictly increasing along future directed causal curves
([[thm:std-bgp-causal]] (2)). Then:

(a) for a ≤ b and a compact set C ⊂ Y, {a ≤ t ≤ b} ∩ J(C) is compact, where J(C) := J⁺(C) ∪ J⁻(C);

(b) for a < 0 < b, the open set Y_(a,b) := {a < t < b} is globally hyperbolic (on each component), and S is a smooth
spacelike Cauchy hypersurface of it.

*Proof.* (a) Let S_b := t⁻¹(b). A point q ∈ J⁺(C) with t(q) ≤ b lies in J⁻(S_b): the inextendible future directed
causal curves from q meet the Cauchy hypersurface S_b, and they do so to the future of q, t increasing along them. So
J⁺(C) ∩ {t ≤ b} ⊂ J⁺(C) ∩ J⁻(S_b), which is compact ([[thm:std-bgp-causal]] (4)); intersecting with the closed set
{t ≥ a} keeps it compact. Likewise J⁻(C) ∩ {t ≥ a} lies in the compact set J⁻(C) ∩ J⁺(S_a).

(b) S is acausal in Y_(a,b), t being strictly increasing along causal curves. So the Cauchy development of S in
Y_(a,b) is open and globally hyperbolic, with Cauchy hypersurface S ([[thm:std-bgp-development]]). It remains to show
that it is all of Y_(a,b): that every inextendible causal curve γ of Y_(a,b) meets S. Let p lie on γ, say with
t(p) ≥ 0 (the case t(p) ≤ 0 is symmetric). If t > 0 along the whole past half γ_− of γ from p, then γ_− lies in
J⁻(p) ∩ {0 ≤ t ≤ t(p)}, which is compact by (a). As in the proof of [[lem:ii-f-1-3]], t is then a parameter on γ_− in
which its tangent, normalised by dt = 1, ranges in a compact set over that compact set; so γ_− is Lipschitz in t and,
as t decreases to inf_(γ_−) t ∈ [0, t(p)], converges to an end point q with t(q) ∈ [0, b). Then q ∈ Y_(a,b), and γ is
extendible in Y_(a,b), a contradiction. So t takes the value 0 on γ_−, and γ meets S. ∎

**Lemma {#lem:ix-1-1}** ([BGP, Theorem 3.2.11] for data without compact support.) Let (Y, g) be globally hyperbolic,
S a smooth spacelike Cauchy hypersurface, n its future unit normal, and P a normally hyperbolic operator on a vector
bundle E, ∇ the connection on E with which [[thm:std-bgp-cauchy]] (5) poses the data. For every u_0, u_1 ∈ C^∞(S; E)
and f ∈ C^∞(Y; E) there is a unique u ∈ C^∞(Y; E) with Pu = f, u|_S = u_0 and ∇_n u|_S = u_1. (In every use below
u_0 = 0, and then ∇_n u|_S does not depend on the connection.)

*Proof.* Uniqueness is [[thm:std-bgp-cauchy]] (3). For existence, let t be the Cauchy time-function of
[[lem:s29-slabs]], with S = t⁻¹(0). Choose a locally finite partition of unity (φ_j) on S with compact supports, and a
locally finite partition of unity (ψ_i) on Y with compact supports, each supp ψ_i in a slab {a_i ≤ t ≤ a_i + 1}. By
[[thm:std-bgp-cauchy]] (5) let u_j solve Pu_j = 0 with data (φ_ju_0, φ_ju_1), and v_i solve Pv_i = ψ_if with zero
data; then supp u_j ⊂ J(supp φ_j) and supp v_i ⊂ J(supp ψ_i).

- *Sources away from S.* If a_i > 0, then v_i = 0 on Y_(−R,a_i) for every R > 0: that slab is globally hyperbolic with
  Cauchy hypersurface S ([[lem:s29-slabs]] (b)), there Pv_i = 0, and v_i has zero data on S, so
  [[thm:std-bgp-cauchy]] (3) applies on it. So v_i = 0 where t < a_i. Likewise, if a_i + 1 < 0, then v_i = 0 where
  t > a_i + 1. The remaining i have −1 ≤ a_i ≤ 0; the cases a_i = 0 and a_i + 1 = 0 are among them.

- *Local finiteness.* Let C ⊂ {−T ≤ t ≤ T} be compact. u_j ≠ 0 somewhere on C only if supp φ_j meets J(C) ∩ S, which is
  compact ([[thm:std-bgp-causal]] (4)): finitely many j. If a_i > 0, v_i ≠ 0 somewhere on C only if a_i ≤ T and
  supp ψ_i meets {0 ≤ t ≤ T + 1} ∩ J(C), which is compact ([[lem:s29-slabs]] (a)): finitely many i. The case
  a_i + 1 < 0 is symmetric. If −1 ≤ a_i ≤ 0, then supp ψ_i ⊂ {−1 ≤ t ≤ 1} meets the compact set
  {−1 ≤ t ≤ 1} ∩ J(C): finitely many i.

So u := Σ_j u_j + Σ_i v_i is a locally finite sum of smooth sections, Pu = Σ_i ψ_if = f, u|_S = Σ_j φ_ju_0 = u_0 and
∇_n u|_S = u_1. ∎

**Lemma {#lem:ix-1-2}** (The domain.) For every open U ⊂ U^♯, D_U(Σ_U), the Cauchy development of Σ_U in U, is open and
globally hyperbolic (on each component, [[sec:ix-0]]), with smooth spacelike Cauchy hypersurface Σ_U.
Ω^♯ := D_(U^♯)(Σ°) contains N⁺ = M°_♭ ∩ {t_IVP ≥ 0}, so that Ω^♯_+ := Ω^♯ ∩ {t_IVP ≥ 0} = N⁺.

*Proof.* Σ_U is a smooth hypersurface of U, as dt_IVP ≠ 0, spacelike and acausal in U ([[sec:ix-0]]).
[[thm:std-bgp-development]] gives the first assertion. Let p ∈ M°_♭ with t_IVP(p) ≥ 0; then p ∈ U^♯.

- *A compact set.* Along a past directed causal curve from p in M°_♭:
  - t_IVP decreases ([[sec:ix-0]]), and t = t_IVP + ψ_IVP(|x|) with 0 ≤ ψ_IVP ≤ C₃ := max ψ_IVP, finite as ψ_IVP is
    constant on [R₃, ∞) ([[lem:iii-b-3-7]] (b) and its proof).
  - |x| stays ≥ min(|x(p)|, r^♮), r^♮ > r_♭: dr is future timelike for g on {r_♭ ≤ r ≤ r^♮} ([[lem:ii-c-3-2]] (1) at
    h = 0, which holds there at every t_*, g being stationary, as in [[lem:s27-below]] (iv); also
    [[prop:np-10-19-iv]] (d)), so r strictly increases towards the past there.
  - On {|x| ≥ 3R₁}, d(t + |x|) is past timelike. By [[prop:iii-b-3-6]], g⁻¹ = ḡ⁻¹ − m₀|x|⁻²(∂_t + ∂_|x|)^(⊗2) there,
    so g⁻¹(d(t + |x|), d(t + |x|)) = −4m₀|x|⁻² < 0. With dt_* = dt − ψ′ d|x|,
    g⁻¹(d(t + |x|), dt_*) = −1 − ψ′ − 2m₀|x|⁻²(1 − ψ′) < 0, as −1 < ψ′ < 1 there ([[eq:iii-b-3-6]]: ψ′ = 1 − 8m₀ϱ⁻²
    for ϱ ≥ 3R₁). So d(t + |x|) and dt_* lie in the same cone, and t + |x| decreases towards the past there.

  Let q ∈ J⁻_(M°_♭)(p) ∩ {t_IVP ≥ 0} with |x(q)| ≥ 3R₁, reached along a past directed causal curve from p. Its last
  segment in {|x| ≥ 3R₁} starts at p or at a point q_0 with |x(q_0)| = 3R₁ and t(q_0) ≤ t_IVP(p) + C₃, so

      t(q) + |x(q)| ≤ B_p := max(t(p) + |x(p)|, t_IVP(p) + C₃ + 3R₁).

  As t(q) ≥ t_IVP(q) ≥ 0, |x(q)| ≤ B_p. Hence

      J⁻_(M°_♭)(p) ∩ {t_IVP ≥ 0} ⊂ L_p := {0 ≤ t_IVP ≤ t_IVP(p),  min(|x(p)|, r^♮) ≤ |x| ≤ max(B_p, 3R₁)},

  a compact subset of U^♯ (closed and bounded in (t, x), with t ∈ [0, t_IVP(p) + C₃]; |x| > r_♭ and t_IVP ≥ 0 > −1
  on it).

- *Every inextendible causal curve through p meets Σ°.* Let γ be one, in U^♯. If t_IVP > 0 along its whole past half,
  that half lies in L_p. As in the proof of [[lem:ii-f-1-3]], a past inextendible causal curve along which a time
  function is bounded below, and which lies in a compact set, extends continuously to a past end point: its tangent,
  normalised by dt_IVP = 1, ranges in a compact set over L_p, so the curve is Lipschitz in t_IVP and converges in
  L_p ⊂ U^♯. That contradicts inextendibility in U^♯. So t_IVP reaches 0 on γ, and γ meets Σ°, once by acausality.
  Hence p ∈ Ω^♯, and N⁺ ⊂ Ω^♯_+; the reverse inclusion holds as Ω^♯ ⊂ U^♯ ⊂ M°_♭. ∎

The region U^♯ reaches to t_IVP = −1 only so that Σ° lies inside it. Nothing below uses Ω^♯ ∩ {t_IVP < 0} beyond the
background g, the extension of Υ̇⁰(k) in Step 1 of the proof of [[thm:ix-2-2]], with that step's solution w and
field X := w^♯, which live on all of Ω′, and the extension by zero in its Step 3.

### The comparison {#sec:ix-2}

**Lemma {#lem:ix-2-1}** (Pointwise identities.) At the Ricci-flat g:

(a) 2L⁰ and 2δ_gG_gδ*_g have principal part −g^(αβ)∂_α∂_β ⊗ id, so principal symbol g⁻¹(ζ, ζ) Id (∂ → iζ). In fact

    2L⁰k = −∇^α∇_α k + ([∇^λ, ∇_μ]k_λν + [∇^λ, ∇_ν]k_λμ)_(μν),        2δ_gG_gδ*_g w = −∇^α∇_α w,

where [∇^λ, ∇_μ]k_λν := ∇^λ∇_μk_λν − ∇_μ∇^λk_λν is of order zero, a contraction of the curvature with k.

(b) DRic(ℒ_X g) = 0 for every smooth vector field X.

(c) If k = 0 on Σ^IVP, then K̇ = ½(∇_n k)|_(TΣ^IVP).

(d) If k = 0 on Σ^IVP, then in an orthonormal frame (n, e_i) there, with k′ := ∇_n k:
−Υ̇⁰(k)(e_j) = k′(n, e_j) and −Υ̇⁰(k)(n) = ½k′(n, n) + ½Σ_i k′(e_i, e_i).

(e) If X = 0 on Σ^IVP and ∇_n X = Y there, then on Σ^IVP: (ℒ_Xg)(e_i, e_j) = 0, (ℒ_Xg)(n, e_j) = g(Y, e_j) and
(ℒ_Xg)(n, n) = 2g(Y, n). For k with k(e_i, e_j) = 0 on Σ^IVP, the vector field Y := Σ_j k(n, e_j)e_j − ½k(n, n)n on
Σ^IVP, that is Y^♭ = k(n, ·) + ½k(n, n)n^♭, gives ℒ_X g = k on Σ^IVP.

(f) If X = 0 on Σ^IVP, then ℒ_X g induces zero linearised data.

*Proof.* (a) The variation of the Christoffel symbols is Γ̇^κ_μν = ½g^κλ(∇_μk_λν + ∇_νk_λμ − ∇_λk_μν), and that of
the Ricci tensor is DRic(k)_μν = ∇_κΓ̇^κ_μν − ∇_νΓ̇^κ_κμ, with Γ̇^κ_κμ = ½∇_μ tr_g k. So

    DRic(k)_μν = ½(∇^λ∇_μk_λν + ∇^λ∇_νk_λμ − ∇^λ∇_λk_μν − ∇_μ∇_ν tr_g k).

−Υ̇⁰(k)_ν = (δ_gG_gk)_ν = −∇^λk_λν + ½∇_ν tr_g k ([[sec:ix-0]]), so
(−δ*_gΥ̇⁰(k))_μν = −½(∇_μ∇^λk_λν + ∇_ν∇^λk_λμ) + ½∇_μ∇_ν tr_g k. Adding gives the formula for
2L⁰ = 2DRic − 2δ*_gΥ̇⁰. For a 1-form w, tr_g δ*_g w = ∇^λw_λ and

    (δ_gG_gδ*_g w)_ν = −½∇^λ∇_λw_ν − ½∇^λ∇_νw_λ + ½∇_ν∇^λw_λ = −½∇^λ∇_λw_ν − ½Ric_νλw^λ,

by the Ricci identity ∇^λ∇_νw_λ − ∇_ν∇^λw_λ = Ric_νλw^λ; at the Ricci-flat g the last term vanishes. A commutator of
two covariant derivatives acting on a tensor is a contraction of the curvature with it, of order zero. In local
coordinates ∇^α∇_α = g^(αβ)∂_α∂_β + (first order), the Christoffel symbols entering only at lower order. So both
operators have principal part −g^(αβ)∂_α∂_β, the local form of [[def:std-normally-hyperbolic]], and are normally
hyperbolic.

(b) Let φ_s be the local flow of X. Ric(φ*_sg) = φ*_s Ric(g) = 0, and (d/ds)φ*_sg|_(s=0) = ℒ_X g. Ric at a point is a
smooth function of the 2-jet of the metric there, and the 2-jet of φ*_sg is smooth in s; so the derivative at s = 0,
which is DRic(ℒ_X g), vanishes, pointwise.

(c) Let g_s := g + sk and n_s its future unit normal. As k = 0 on Σ^IVP, g_s = g at the points of Σ^IVP, so n_s = n
there for every s, and ṅ = 0. For X, Y tangent, K_s(X, Y) = g_s(∇^(g_s)_X n_s, Y), and its s-derivative at 0 is
k(∇_Xn, Y) + g(∇_Xṅ, Y) + g(C(X, n), Y), where C is the variation of the connection,

    g(C(X, Z), Y) = ½(∇_Xk(Z, Y) + ∇_Zk(X, Y) − ∇_Yk(X, Z)).

The first term vanishes as k = 0 on Σ^IVP, and the second as ṅ = 0 along Σ^IVP and X is tangent. As k = 0 on Σ^IVP,
its tangential covariant derivatives vanish there, ∇_Xk = ∇_Yk = 0. So K̇(X, Y) = g(C(X, n), Y) = ½(∇_nk)(X, Y).

(d) As k = 0 on Σ^IVP, ∇_(e_i)k = 0 there, and only normal derivatives survive. In the frame,
g⁻¹ = −n ⊗ n + Σ_i e_i ⊗ e_i, so the divergence is ∇^λk_λ· = −(∇_nk)(n, ·) + Σ_i(∇_(e_i)k)(e_i, ·) = −k′(n, ·);
and d tr_g k = tr_g ∇k vanishes on e_j, while (d tr_g k)(n) = tr_g k′ = −k′(n, n) + Σ_i k′(e_i, e_i). As
−Υ̇⁰(k) = −∇^λk_λ· + ½ d tr_g k, this gives −Υ̇⁰(k)(e_j) = k′(n, e_j), and
−Υ̇⁰(k)(n) = k′(n, n) + ½(−k′(n, n) + Σ_i k′(e_i, e_i)) = ½k′(n, n) + ½Σ_i k′(e_i, e_i).

(e) As X = 0 on Σ^IVP, its tangential covariant derivatives vanish there, ∇_(e_i)X = 0, and ∇_nX = Y. With
(ℒ_Xg)(a, b) = g(∇_aX, b) + g(a, ∇_bX) this gives the three values. For the given k, Y = Σ_j k(n, e_j)e_j − ½k(n, n)n
has g(Y, e_j) = k(n, e_j) and 2g(Y, n) = k(n, n), as g(n, n) = −1; so ℒ_X g = k at Σ^IVP, both vanishing on
(e_i, e_j). Since a covector ω equals Σ_j ω(e_j)e_j^♭ − ω(n)n^♭, Y^♭ = k(n, ·) + ½k(n, n)n^♭.

(f) Let φ_s be the flow of X, defined near any compact piece of Σ^IVP for |s| small. It fixes Σ^IVP pointwise, so φ_s
is an isometry from a neighbourhood of that piece with the metric φ*_sg to its image with the metric g, the identity
on Σ^IVP, and it preserves the future normal for |s| small, by continuity from s = 0. So φ*_sg induces exactly the
data (γ, K) of g on Σ^IVP, for every small s. The induced data are smooth functions of the 1-jet of the metric at
Σ^IVP, whose s-derivative at 0 is that of ℒ_X g. So the derivative of the data, which is the data induced by ℒ_X g,
vanishes. ∎

**Theorem {#thm:ix-2-2}** (Linearised vacuum solutions with gauge-equivalent data are gauge-equivalent.) Let U ⊂ U^♯
be open, Ω′ := D_U(Σ_U) and Ω′_+ := Ω′ ∩ {t_IVP ≥ 0}, a manifold with boundary Σ_U. Let k be a symmetric 2-tensor on
Ω′_+, smooth up to Σ_U ([[sec:ix-0]]), with DRic(k) = 0, inducing on Σ_U the linearised data that ℒ_Z g induces, for a
vector field Z on a neighbourhood of Σ_U in Ω′_+, smooth up to Σ_U (Z = 0: zero data). Then there is a vector field X
on Ω′_+, smooth up to Σ_U, with

    k = ℒ_X g     on Ω′_+.

X is unique up to a Killing field of g on Ω′_+.

*Proof.* Ω′ is globally hyperbolic with smooth spacelike Cauchy hypersurface Σ_U ([[lem:ix-1-2]]), and the data of a
tensor smooth up to Σ_U are defined from one side (the definition of linearised data in [[sec:ix-0]] allows this).
Uniqueness up to Killing fields is
ℒ_(X−X′)g = 0.

*Step 0 (zero data).* Let W = W̃ ∩ Ω′_+, W̃ open in Ω′, be the neighbourhood of Σ_U where Z is defined, and
ψ̃ ∈ C^∞(Ω′) equal to 1 near Σ_U with supp_(Ω′) ψ̃ ⊂ W̃ (smooth Urysohn: Σ_U is closed in Ω′); ψ := ψ̃|_(Ω′_+).
k_0 := k − ℒ_(ψZ)g has DRic(k_0) = 0 ([[lem:ix-2-1]] (b)), and it induces zero data: those of ℒ_(ψZ)g and ℒ_Zg agree,
as ψZ = Z near Σ_U. If k_0 = ℒ_(X_0)g, then k = ℒ_(X_0+ψZ)g. So we may assume Z = 0.

*Step 1 (the gauge vector field).* Zero data means k(e_i, e_j) = 0 on Σ_U (γ̇ = 0) and K̇ = 0. Let Y be the vector field
of [[lem:ix-2-1]] (e) on Σ_U, smooth, as Y^♭ = k(n, ·) + ½k(n, n)n^♭. Υ̇⁰(k) = −δ_gG_gk is a 1-form on Ω′_+, smooth up
to Σ_U. Let F be a smooth 1-form on Ω′ with F = −Υ̇⁰(k) on Ω′_+: [[sec:ix-0]] extends Υ̇⁰(k) to an open neighbourhood V
of Ω′_+ in Ω′, and a smooth function equal to 1 on the closed set Ω′_+ with support in V (smooth Urysohn) extends it by
0 beyond. By [[lem:ix-1-1]] on Ω′, with P := 2δ_gG_gδ*_g ([[lem:ix-2-1]] (a)), there is a smooth 1-form w on Ω′ with

    2δ_gG_gδ*_g w = F,        w|_(Σ_U) = 0,        ∇_n w|_(Σ_U) = Y^♭.

Put X := w^♯, a smooth vector field on Ω′; the theorem's X is its restriction to Ω′_+, and [[lem:ix-2-1]] (f) applies
to it as it stands. Then −Υ̇⁰(ℒ_X g) = δ_gG_g(2δ*_g w) = F = −Υ̇⁰(k) on Ω′_+, and X = 0, ∇_n X = Y on Σ_U.

*Step 2 (the difference has vanishing Cauchy data).* Let h := k − ℒ_X g.

- h = 0 on Σ_U, by [[lem:ix-2-1]] (e).

- h induces zero linearised data: k does by assumption, and ℒ_X g does by [[lem:ix-2-1]] (f). So by
  [[lem:ix-2-1]] (c), (∇_n h)(e_i, e_j) = 2K̇(e_i, e_j) = 0.

- Υ̇⁰(h) = 0 on Ω′_+ by Step 1. At Σ_U, [[lem:ix-2-1]] (d) with h′ := ∇_n h and h′(e_i, e_i) = 0 gives
  h′(n, e_j) = 0 and h′(n, n) = 0.

So h|_(Σ_U) = 0 and ∇_n h|_(Σ_U) = 0.

*Step 3 (it vanishes).* DRic(h) = DRic(k) − DRic(ℒ_X g) = 0 ([[lem:ix-2-1]] (b)), and Υ̇⁰(h) = 0, so L⁰h = 0 on Ω′_+
by [[eq:ix-0-1]]; h is smooth up to Σ_U.

- *h vanishes to infinite order along Σ_U.* Work in coordinates (t_IVP, y) near a point of Σ_U. As h = 0 on Σ_U,
  ∇_n h = n^t ∂_(t_IVP) h there, with n^t := dt_IVP(n) > 0; so ∂_(t_IVP) h = 0 on Σ_U. Suppose ∂^j_(t_IVP) h = 0 on
  Σ_U for j < m, some m ≥ 2, so that every derivative of h of order below m vanishes there. By [[lem:ix-2-1]] (a),
  2L⁰ = −g⁻¹(dt_IVP, dt_IVP)∂²_(t_IVP) + R, with R of second order and at most first order in ∂_(t_IVP), and
  g⁻¹(dt_IVP, dt_IVP) < 0 as dt_IVP is timelike: Σ_U is noncharacteristic. Apply ∂^(m−2)_(t_IVP) to 2L⁰h = 0 and
  restrict to Σ_U. Every term but −g⁻¹(dt_IVP, dt_IVP)∂^m_(t_IVP)h is a derivative of h of order below m, or of order m
  with at most m − 1 derivatives in t_IVP (a tangential derivative of a vanishing normal one), so it vanishes; hence
  ∂^m_(t_IVP) h = 0 on Σ_U.

- *Extension by zero.* Put h̃ := h on Ω′_+ and h̃ := 0 on Ω′ ∩ {t_IVP < 0}. Every derivative of h tends to 0 at Σ_U,
  so h̃ is smooth on Ω′: each derivative of h̃ off Σ_U extends continuously by 0 across Σ_U, and a continuous function
  on Ω′ that is C¹ off the hypersurface Σ_U, with first derivatives extending continuously across it, is C¹ (the mean
  value theorem along curves transverse to Σ_U); induction on the order gives every C^j. L⁰h̃ is smooth and vanishes
  off Σ_U, so everywhere; and h̃|_(Σ_U) = 0, ∇_n h̃|_(Σ_U) = 0.

2L⁰ is normally hyperbolic ([[lem:ix-2-1]] (a)). [[thm:std-bgp-cauchy]] (3) on Ω′, on each component, gives h̃ = 0,
so h = 0 on Ω′_+. ∎

**Corollary {#cor:ix-2-3}** (The solution of [[thm:viii-2-2]] in any gauge.) Let (γ̇, k̇), ġ, S′, S⁰′, ḃ and U′ be as
in [[thm:viii-2-2]], U ⊂ U^♯ open, Ω′ := D_U(Σ_U) and Ω′_+ := Ω′ ∩ {t_IVP ≥ 0} ⊂ N⁺ ⊂ N_ν. Let ġ′ be a symmetric
2-tensor on Ω′_+, smooth up to Σ_U, with DRic(ġ′) = 0, that induces on Σ_U the data (γ̇, k̇) plus those of ℒ_Z g, for
a vector field Z near Σ_U in Ω′_+, smooth up to Σ_U. Then

    ġ′ = ġ + ℒ_X g     on Ω′_+

for a vector field X on Ω′_+, smooth up to Σ_U. In particular, where χ_K = 1 in Ω′_+,

    ġ′ − ℒ_X g − ∂_b g_b|_(b=b₀)(ḃ) = h_(b₀,rem)(q′) + h′,

with q′ and h′ the components of D_0Φ(U′) = (h′, p⃗′, q′) named in [[thm:viii-2-2]] (3), as in [[eq:viii-2-2]]. For
U = U^♯, Ω′_+ = N⁺ = M°_♭ ∩ {t_IVP ≥ 0} ([[lem:ix-1-2]]). The region where [[eq:viii-2-3]] is stated has
t_IVP ≥ t_* ≥ T′ ≥ 0 ([[eq:viii-2-3]] holds with T′ enlarged, so we take T′ ≥ 0), so its part in {r > r_♭} lies in
N⁺, and there the remainder has the rate [[eq:viii-2-3]]: every linearised vacuum solution with these data settles, up
to the linearised diffeomorphism ℒ_X g, to a linearised Myers–Perry metric, with X itself not controlled
([[rem:ix-2-4]] (b)). For a general open U this holds only on the part of that region which Ω′_+ contains.

*Proof.* ġ is smooth on the interior of N_ν with DRic(ġ) = 0, and its restriction to N⁺ ⊃ Ω′_+ is smooth up to Σ°
([[lem:s29-g-on-n]]). Near Σ^IVP in N_ν, ġ = ḣ + ġ_(S′) + ġ⁰_(S⁰′) with ġ_(S′) + ġ⁰_(S⁰′) = −ℒ_(V(S′)+V⁰(S⁰′))g
([[eq:viii-0-2]]): the set 𝒟′ = 𝒟 ∖ {t^♭_* ≥ T̂ + 7/4} of [[thm:viii-2-2]] (2) contains N_ν ∩ {t_IVP < T̂ + 7/4}, as
t^♭_* ≤ t_* ≤ t_IVP where t^♭_* is defined. ḣ induces (γ̇, k̇) ([[lem:viii-1-1]] (1), which allows a tensor given on
one side up to Σ^IVP, with the data of [[prop:viii-1-2]]). The induced data being linear in the tensor and ℒ_Xg linear
in X, k := ġ′ − ġ is smooth up to Σ_U on Ω′_+, has DRic(k) = 0 there, and induces the data of
ℒ_(Z+V(S′)+V⁰(S⁰′))g, where Z + V(S′) + V⁰(S⁰′) is a vector field near Σ_U in Ω′_+, smooth up to Σ_U.
[[thm:ix-2-2]] gives k = ℒ_X g. The second display is [[eq:viii-2-2]] with ġ = ġ′ − ℒ_X g. ∎

**Remark {#rem:ix-2-4}** (What is and is not asserted.) (a) The statement is the linear counterpart of the nonlinear
comparison of [[rem:vii-4-1]] ([[lem:interior-one-spacetime]]); it is proved here for the linearisation only.

(b) Nothing is asserted here about the size or decay of X. X solves a linear wave equation with right side
−Υ̇⁰(k) = δ_gG_gk and its own Cauchy data, and its behaviour at ℐ⁺ and K⁺ depends on the gauge of ġ′. A solution in the
Regge–Wheeler-type gauge or in the harmonic gauge with the same data, given on N⁺, the future of Σ^IVP in {r > r_♭}, and
smooth up to Σ°, is ġ + ℒ_X g there ([[cor:ix-2-3]] with U = U^♯), and so settles modulo ℒ_X g; the decay in those
gauges is the decay of ℒ_X g there. It is proved in the Regge–Wheeler-type gauge in [[thm:rw-settling]], and for the
harmonic-gauge representative in [[thm:harmonic-rate]].

(c) In the class, if U is G-invariant (for instance U = U^♯: G preserves t_IVP and |x|), so that Ω′ and Ω′_+ are
G-stable, the data (γ̇, k̇) are in the class of [[cor:viii-2-3]], and ġ′ is G-invariant, then X may be taken
G-invariant; Z's invariance is not needed, only k's is used. G is compact and acts by isometries of g (the proof of
[[cor:viii-2-3]]); ġ is G-invariant by [[cor:viii-2-3]], so k = ġ′ − ġ is; and the Haar average
X_G := ∫_G σ_*X dσ has ℒ_(X_G)g = ∫_G σ_*(ℒ_X g) dσ = k.

