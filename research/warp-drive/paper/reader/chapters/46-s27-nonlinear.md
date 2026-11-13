## The nonlinear stability theorem near Tangherlini, the parameters, and the symmetry class {#ch:s27}

This chapter proves the nonlinear stability of the five-dimensional Schwarzschild–Tangherlini black hole g_(b₀),
b₀ = (m₀, 0), for initial data on the hypersurface Σ^IVP of [[sec:iii-b-3-3]] that are small in a weighted,
partially polyhomogeneous class ([[thm:iii-k-4-3]]). This is [Hin26, Theorem 13.1] in dimension 4 + 1, assembled, as in
[Hin26, Section 13.1, pp. 318–323], from the linear theory of [[ch:s11]]–[[ch:s25]] and the Nash–Moser theorem
[[thm:ii-g-2-1]]. The proof has four steps: the parameters ([[sec:iii-k-0]]), the solution up to a fixed level of the
time function, from the initial data ([[sec:iii-k-1]]), the Nash–Moser iteration for the map Ψ ([[sec:iii-k-2]],
[[sec:iii-k-3]]), and the propagation of the constraints ([[sec:iii-k-4]]). [[sec:vi-c-1]] and [[sec:vi-c-2]] list
every condition that the stability theory places on its parameters and show that the conditions can be met together,
in an order with no circular threshold ([[thm:vi-c-2-1]]). [[sec:s27-class]] and [[sec:vii-3]] restrict the theorem to
data invariant under G = O(2) × O(2): the development is then G-invariant and settles to a Tangherlini metric, without
boost or rotation ([[prop:vii-3-2]]). [[cor:s27-rate]] chooses the constants so that the final parameters lie within a
prescribed distance of b₀, and states the rate of settling on compact sets.

In dimension 4 + 1 the argument of [Hin26] needs three changes. (1) The initial family solves a gauge-fixed equation
whose gauge is cut off near the initial surface ([[thm:iii-c2-3-1]]), while the map Ψ uses the gauge of the forward
cone; the cut-off of [[lem:iii-k-1-1]] equals 1 on Ω_* and agrees with that of [[thm:iii-c2-3-1]] on the exterior
domain. (2) The Nash–Moser theorem with support classes asks for support conditions on every component of supported
character ([[sec:iii-k-3]]). (3) The right inverses of [[thm:iii-j1-2-1]] are formed for Ψ, in which the boost
direction carries the initial family ([[lem:iii-k-2-3]]). The region near null infinity that the initial family must
reach, a slab bounded in t_*, is solved together with the exterior problem ([[sec:iv3-0]]–[[sec:iv3-2]]), and the
compact sets that the uniqueness lemma [[lem:ii-f-1-3]] asks for are supplied near ℐ⁺ and near spatial infinity by
[[lem:iii-k-6-1]] and [[lem:iii-k-6-2]].

*Notation and the inner radius.* The notation is that of [[ch:s11]]–[[ch:s25]]. b₀ = (m₀, 0), R₁ = m₀^(1/2), and the
inner radius r_♭ ∈ (0, ½R₁] of [[ch:s11]] is a parameter: the spacetime M of [[eq:iii-b-2-1]] has the inner boundary
{|x| = r_♭}, and the radius r_0 of the artificial boundary of [[ch:s04]]–[[ch:s10]] is r_♭ ([[def:s12-radii]]), as
in [[ch:s19]]. Every result of this chapter holds for each such r_♭, with constants and neighbourhoods of b₀ that may
depend on it. C′ is the constant of [[eq:iii-b-3-6]], so that t_* = t − |x| + C′ − 8m₀|x|⁻¹ on {|x| ≥ 3R₁}, and C″ is
the constant value of ψ_IVP on [R₃, ∞) ([[lem:iii-b-3-7]] (b)), so that t_IVP = t − C″ on {|x| ≥ R₃}. The time function
t^♭_* is that of [[lem:ii-c-3-2]] with ℓ = ½; its constant C′ of [[lem:ii-c-3-2]] (b) is written C_♭ ∈ (0, 1) here, to
distinguish it from the constant of [[eq:iii-b-3-6]]. M_(1/2) is the space of [[def:iii-b-2-1]] on which ρ_I^(1/2) is
smooth. For S = S_w ∈ 𝒮_1 we write |S| := |w|.

### Setting {#sec:iii-k-0}

*The time functions.* t^♭_* is defined on {t_* ≥ ½} ([[lem:ii-c-3-2]], [[lem:ii-e-1-2]] (iv)), with
C_♭ t_* ≤ t^♭_* ≤ t_* there ([[lem:ii-c-3-2]] (b)); a sublevel set {t^♭_* ≤ c}, c ≥ 1, means the complement of
{t^♭_* > c}, which lies in {t_* > c}. Ω_* := cl_M{t^♭_* ≥ 1}. Put

    T̂ := 2/C_♭ ≥ 2,     T_ι := (T̂ + 2)/C_♭,     T_K := max(10, T_ι + 2),

so that {t^♭_* ≥ T̂} ⊂ Ω_*. Every level used below, the top of the region 𝒟 of [[prop:iii-k-1-2]] and the levels of
the support classes of [[sec:iii-k-3]], lies at t^♭_* ≥ T̂ ≥ 2. The cut-off χ_−, the region 𝒟 and the support classes
are defined by t^♭_*. Its differential is past timelike for every g_(b₀) + h with h small in 𝒢̃^(0,(1,0,0))_(e3b)
([[lem:ii-c-3-2]] (2)), a margin that survives the perturbations used below; the timelike margin of dt_* near ℐ⁺ is
only of order m₀r⁻², as g_(b₀)⁻¹(dt_*, dt_*) = −18m₀r⁻² + O(r⁻⁴) there, and a perturbation h₀₀ of order ρ_I^z,
Re z < 2, can overturn it. t^♭_* is smooth on M_(1/2) near ℐ⁺ ([[lem:ii-c-3-2]] (a)) and equals t_* on ℐ⁺.

*The cut-off χ_K and the background.* We take the cut-offs χ^♭_K, χ_K, χ^♯_K of [[sec:iii-b-5]] with the condition
[[eq:iii-i-1-2]] at the threshold T_K in place of 10, a condition of the same kind:

    supp χ_K ⊂ {t^♭_* ≥ T_K};

so χ_K = 0 on {t_* < T_K}, as t^♭_* ≤ t_*. Every statement of [[ch:s19]]–[[ch:s25]] holds with this threshold, the
supports only shrinking. 𝒮_1 and the boosts φ_S are those of [[sec:iii-b-5]], g_(b₀,b,−S) is [[eq:iii-i-1-1]], and P_5
is the augmented operator [[eq:iii-i14-1-3]]. Φ, the data space 𝒟, the class ℱ and 𝒳_J are those of [[def:iii-j-1-1]],
[[def:iii-j-classes]] and [[thm:iii-j-2-4]], and 𝒟_ex, ℱ_ex, 𝒳_(J,ex), 𝒬_ex are the exact classes of [[def:iii-j3-1-1]].

*The two time functions.* Put F(r) := t_IVP − t_* = ψ(r) − ψ_IVP(r). By [[lem:iii-b-3-7]] (b), ψ_IVP = ψ on [r_♭, 5R₁]
and 0 ≤ ψ_IVP′ ≤ ψ′ beyond, so F ≥ 0, F′ ≥ 0 and F = 0 on [r_♭, 5R₁]; so t_* ≤ t_IVP. For r ≥ R_5 := max(R₃, 3R₁),
ψ(r) = r − C′ + 8m₀r⁻¹ and ψ_IVP(r) = C″, so F(r) = r − C′ − C″ + 8m₀r⁻¹. As ψ_IVP ≥ 0, C″ ≥ 0. Let
R_6 := max(R_5, 2(|C′| + C″)); then

    F(r) ≥ r/4     for r ≥ R_6.                                                                        {#eq:s27-f}

*Parameters* ([Hin26, Section 13.1, Step 1]). The constraint damping E_C has the constants of [[thm:iii-e-1-1]] fixed
in [[eq:iv4-0-1]], with C_0 = 100: v_C = ½, e_C = 1/102400 and γ_C = h⁻¹, h ∈ 𝖧; as h < 10⁻⁶,
s_C := (1 − e_C)(1 − v_C)γ_C > 100. The gauge modification E_Υ = (c_Υ, e_Υ, γ_Υ; c_(Υ,H), γ_(Υ,H)) has c_Υ and c_(Υ,H)
as in [[sec:iii-d-1]] and [[lem:iii-d1-3-1]], and γ_(Υ,H), e_Υ, γ_Υ small enough for the mode stability of
[[prop:iii-d1-4-1]] and the tf-admissibility of [[prop:iii-f1-3-3]]. The data index set ℰ_0 and the weight ℓ_0 satisfy
the hypotheses of [[thm:iii-c1-3-1]]:

    min Re ℰ_0 > 3/2 + 2γ_Υ,     jℰ_0 ⊂ ℰ_0 (j ∈ ℕ),     ℓ_0 > 3,     ℓ_0 ∉ Re π_1ℰ_0,

the bound ℓ_0 > 3 coming from (H4) of [[sec:iii-i10-1]] (see row d1 of [[sec:vi-c-1]]). ℰ^C_I and ℓ_I are then those
of [[thm:iii-c1-3-1]]. The weights ℓ_I, ε_+, ε_K and α of the cone are those of [[ch:s19]]–[[ch:s24]]. The weights
3 + ε_0 and 1 + ε_0 of [Hin26] at spatial and null infinity are ℓ_0 and 3/2 + ε_0 here, in the normalisation of
[[ch:s17]], in which the weights at null infinity are shifted by ½ ([[eq:iii-c1-1-1]]). [[thm:vi-c-2-1]] shows that all
the conditions can be met together.

*The cut-off χ_ι.* We take the cut-off χ_ι = χ(t_*) of [[sec:iii-g2-4]] with χ = 0 on (−∞, T_ι] and χ = 1 on
[T_ι + 1, ∞). Then χ_ι = 0 on {t_* ≤ T_ι} ⊃ {t^♭_* ≤ T̂ + 2} (as C_♭t_* ≤ t^♭_*), and supp dχ_ι ⊂
{T_ι ≤ t_* ≤ T_ι + 1} is disjoint from supp χ_K, as T_K > T_ι + 1. [[sec:iii-g2-4]] and [[ch:s23]] use of χ_ι only that
it is a function of t_*, equal to 1 near ι⁺, supported in Ω_*, with derivatives supported in a compact t_*-interval;
so this choice is admissible, and the ι⁺-terms of Φ do not reach the region of the initial family.

### The initial family {#sec:iii-k-1}

**Lemma {#lem:iii-k-1-1}** (The cut-off of the gauge.) Let χ_♮ ∈ C^∞(ℝ) equal 0 on (−∞, ½] and 1 on [1, ∞), let χ_0
be the cut-off of [[sec:iii-c2-2]], χ_0 = 1 − χ̌_0(t_IVP/r) with χ̌_0 ∈ C^∞_c((−¼, ¼)) equal to 1 on [−⅛, ⅛], and

    χ^♮_0 := 1 − (1 − χ_0)(1 − χ_♮(t_*)).                                                             {#eq:iii-k-1-1}

Then: (a) χ^♮_0 ∈ C^∞(M); (b) χ^♮_0 = 1 on {t_* ≥ 1} ⊃ Ω_*; (c) χ^♮_0 = χ_0 on {t_* ≤ ½}, and on Ω_(ext,r_1) for
r_1 ≥ R_6; (d) χ^♮_0 = 0 near Σ^IVP and near φ_(±S)(Σ^IVP) for |S| small.

Here Ω_(ext,r_1) is the exterior domain of [[lem:iii-c1-1-1]] at the radius r_1. The proof of (d) uses the following
bound on the boosts.

**Lemma {#lem:s27-boost-move}** (The boosts move t_IVP by O(|S|r).) There is C such that for S ∈ 𝒮_1 with |S| ≤ 1 and
every p ∈ M, |t_IVP(φ_(±S)(p)) − t_IVP(p)| ≤ C|S| r(p), and r(φ_(±S)(p)) ≤ C r(p). φ_(±S) is the identity on
{|x| ≤ 5R₁} and maps {|x| > 5R₁} into itself.

*Proof.* φ_(S_w) is the time-1 flow of V(S_w) = ½χ_r(|x|)χ^♯_IVP(1 − χ^♭_K)X_w, X_w = t w·∂_x + (w·x)∂_t
([[lem:iii-b-5-1]]); φ_(−S) is that of V(S_(−w)) = −V(S_w). As 1 − χ^♭_K = 0 on {|x| < t/10, t > 60R₁}, every point of
supp V(S_w) has t ≤ 10|x| + 60R₁, and t ≥ −½|x| on M; so |t| ≤ 10|x| + 60R₁ ≤ C|x| there, |x| ≥ r_♭ being bounded
below. With X_w|x| = t S_w(x̂) and t_IVP = t − ψ_IVP(|x|), 0 ≤ ψ_IVP′ ≤ ψ′ ≤ 1,

    |V(S_w)|x|| ≤ ½|w||t| ≤ C|w||x|,     |V(S_w)t_IVP| = ½χ_rχ^♯_IVP(1 − χ^♭_K)|w·x − ψ_IVP′ t S_w(x̂)| ≤ C|w||x|

on M, the left sides vanishing off supp V(S_w). Along an integral curve γ(s), s ∈ [0, 1], of ±V(S_w),
|d log|x(γ(s))|/ds| ≤ C|w|, so |x(γ(s))| ≤ e^(C|w|)|x(γ(0))|; and |d t_IVP(γ(s))/ds| ≤ C|w||x(γ(s))|. Integrating
gives both bounds. V(S_w) vanishes on {|x| ≤ 5R₁} (χ_r = 0 there), whose points are fixed by the flow; by uniqueness
of integral curves no curve starting in {|x| > 5R₁} reaches it. ∎

*Proof of [[lem:iii-k-1-1]].* (a) χ_0 ∈ C^∞(M) ([[sec:iii-c2-2]]). Near ℐ⁺, t_* is a smooth function on M
([[eq:iii-b-3-6]]); near I₀ and near the corner I₀ ∩ ℐ⁺, t_* → −∞, so χ_♮(t_*) = 0; near ι⁺ and K⁺, t_* → +∞, so
χ_♮(t_*) = 1. (b) There χ_♮(t_*) = 1, and t^♭_* ≤ t_*. (c) The first claim is clear. On
Ω_(ext,r_1) ∩ {t_* > ½}, r ≥ r_1 ≥ R_6, so t_IVP = t_* + F(r) > r/4 by [[eq:s27-f]], where χ_0 = 1
([[sec:iii-c2-2]]); both cut-offs are 1 there. (d) On Σ^IVP, t_* = −F ≤ 0. Let ν_0 := min(¼, r_♭/8). On
{|t_IVP| < ν_0}, a neighbourhood of Σ^IVP, t_* ≤ t_IVP < ¼, so χ_♮(t_*) = 0; and |t_IVP| < r/8 as r ≥ r_♭, so
χ_0 = 0. Hence χ^♮_0 = 0 there. Let p be near φ_(±S)(Σ^IVP), p = φ_(±S)(q) with |t_IVP(q)| small. If r(p) ≥ R_6 + 1,
then by [[lem:s27-boost-move]] |t_IVP(p)| ≤ |t_IVP(q)| + C|S|r(q) ≤ |t_IVP(q)| + C²|S|r(p) < r(p)/8 for |S| and
|t_IVP(q)| small, so χ_0(p) = 0, and t_*(p) = t_IVP(p) − F(r(p)) < r(p)/8 − r(p)/4 < 0, so χ_♮(t_*(p)) = 0. On the
compact set {r ≤ R_6 + 2} ∩ M, the boosts tend to the identity smoothly as S → 0, so φ_(±S)(Σ^IVP) ∩ {r ≤ R_6 + 1}
lies in {|t_IVP| < ν_0} for |S| small, and χ^♮_0 = 0 there, as just shown. ∎

Let

    P^♮(g, g_0) := Ric(g) − δ*_(g_0,E_C) Υ^(χ^♮_0E_Υ)(g, g_0),

[[eq:iii-c2-2-1]] with χ^♮_0 in place of χ_0. Its linearisation in g at (g, g_0) is written L^(χ^♮_0)_(g,g_0).

**Proposition {#prop:iii-k-1-2}** (The initial family; [Hin26, (13.5) and (12.33)].) Let γ = γ_(b₀) + γ̃ and
k = k_(b₀) + k̃ be data on Σ^IVP satisfying the constraint equations, with γ̃ ∈ H^(∞,(ℰ_0,ℓ_0))_b and
k̃ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b, small in H^(d_1) of these classes for a d_1 fixed below. Let h̊_0, h̊_1 be the Cauchy data of
[[prop:iii-c2-4-1]] for (γ, k). For S ∈ 𝒮_1 small let h_(S,0), h_(S,1) be the pulled-back data [[eq:iii-c2-3-1]] of
these, now on all of Σ^IVP. Let N := {t_IVP ≥ −ν(r)}, with ν smooth and non-decreasing, ν = 0 on [0, R_ν],
R_ν := ½(r_♭ + 5R₁), ν > 0 on (R_ν, ∞), 0 ≤ ν′ ≤ 1/32, and ν(r) = r/64 for r ≥ 16R_8, where R_8 ≥ max(2r_1, 8, 5R₁) is
fixed in [[lem:s27-cover]]. Such ν exists, as 16R_8/64 ≤ (16R_8 − R_ν)/32; and ν(r) ≤ (r − R_ν)/32 ≤ r/32. So
{t_IVP = −ν} is spacelike for g_(b₀) (see below), N = {t_IVP ≥ 0} near {r = r_♭}, and {r = r_♭} is an inflow boundary
for a backward problem. Put

    𝒟 := N ∩ {t^♭_* ≤ T̂ + 3},     𝒟_S := φ_S⁻¹({t_IVP ≥ 0}) ∩ {t^♭_* ≤ T̂ + 2}.

For |S| small, 𝒟_S ⊂ 𝒟, and φ_S maps a neighbourhood of Σ^IVP ∪ φ_S⁻¹(Σ^IVP) into N. There is a unique h_S on 𝒟 with

    P^♮(φ_S^*g_(b₀) + h_S, φ_S^*g_(b₀)) = 0,     h_S = h_(S,0),  r ℒ_(∂_(t_IVP)) h_S = h_(S,1)  on Σ^IVP,
                                                                                                  {#eq:iii-k-1-2}

and:

(1) h_S = φ_S^*h_0 on a neighbourhood of Σ^IVP ∪ φ_S⁻¹(Σ^IVP) in 𝒟, where h_0 := h_S|_(S=0) on 𝒟, a two-sided
neighbourhood of Σ^IVP off {r ≤ R_ν}; on {r ≤ R_ν}, 𝒟 ends at Σ^IVP and φ_S is the identity, so φ_S^*h_0 is defined
there. Hence φ_S^*g_(b₀) + h_S = φ_S^*(g_(b₀) + h_0) there;

(2) Ric(φ_S^*g_(b₀) + h_S) = 0 and Υ^(χ^♮_0E_Υ)(φ_S^*g_(b₀) + h_S, φ_S^*g_(b₀)) = 0 on 𝒟; on 𝒟 ∩ Ω_* the gauge 1-form
is Υ^(E_Υ) ([[lem:iii-k-1-1]] (b)), which is [Hin26, (12.33b)];

(3) on 𝒟 ∩ Ω_*, h_S ∈ H̄^(∞,(⟨ℰ^C_I⟩,ℓ_I))_b (orders at ℐ⁺; the set is bounded in t_*); h_S is C^l in S with values in
each H^k of this class, for data of regularity depending on k and l ([[thm:iii-c2-3-1]] (2)); and for each k there are
k′ and C_k with ‖h_S‖_(H^k) + ‖∂_S h_S‖_(H^k) + ‖∂²_S h_S‖_(H^k) ≤ C_k ‖(γ̃, k̃)‖_(H^(k+k′)).

*The hypersurface {t_IVP = −ν} and the inclusions.* In the Kerr–Schild coordinates of [[lem:iii-b-3-7]],
t_IVP + ν = t − (ψ_IVP − ν)(|x|) has differential dt_KS − β′ d|x| with β′ = β_IVP − ν′, where β_IVP :=
ψ_IVP′ + 2χ_∞m₀/(|x|² − m₀) is the coefficient of t_IVP in the proof of [[lem:iii-b-3-7]]. There β_IVP ≤ 1, β_IVP > 0
on [5R₁, ∞), and on [r_♭, 5R₁], where β_IVP = 1 − χ_∞(8m₀/ϱ² − 2m₀/(ϱ² − m₀)) (ϱ = |x|), either χ_∞ = 0 and
β_IVP = 1, or ϱ ≥ 2R₁ and 8m₀/ϱ² − 2m₀/(ϱ² − m₀) ≤ 6m₀/ϱ² ≤ 3/2, so β_IVP ≥ −½. As 0 ≤ ν′ ≤ 1/32,
β′ ∈ (−1, 1], and d(t_IVP + ν) is timelike for g_(b₀) by [[lem:iii-b-3-3]] (e) and [[lem:s11-ks-domain]]: {t_IVP = −ν}
is spacelike. Near {r = r_♭}, ν = 0, and {r = r_♭} is spacelike with dr future timelike ([[lem:ii-c-3-2]] (1)), N
lying to its past; past directed causal curves from points with r > r_♭ stay in {r ≥ min(r(p), r^♮)}, so a backward
problem needs no data there. For the inclusions: near |x| = r, φ_S moves t_IVP by at most C|S|r
([[lem:s27-boost-move]]) and not at all for r ≤ 5R₁, while ν(r) ≥ c_ν r on [5R₁, ∞) with
c_ν := min(ν(5R₁)/(16R_8), 1/64) > 0; so C|S| ≤ ½c_ν suffices. (φ_S⁻¹, not φ_S, appears in 𝒟_S: φ_S^*h_0 at p needs
h_0 at φ_S(p).)

#### The cover of 𝒟 {#sec:s27-cover}

Let r_ext ≥ R_0 be the exterior radius at which [[thm:iii-c2-3-1]] is applied (R_0 that of [[lem:iii-c1-1-1]]), and
r_1 := 2r_ext ≥ R_6, the radius of its boosted problem; Ω_(ext,r_1), Σ^IVP_(r_1) := Ω_(ext,r_1) ∩ Σ^IVP and its future
boundary Σ^fut_(r_1) = {t_IVP = r + 2r^(1−ℓ^♭_I) − (r_1 + 2r_1^(1−ℓ^♭_I))} are those of [[lem:iii-c1-1-1]], with the
weights ℓ^♭_0, ℓ^♭_I of [[eq:iii-c1-1-1]]. Let

    R_8 ≥ max(2r_1, 8, 5R₁),     T″ := (T̂ + 3)/C_♭ + max(0, −C′) + 2,

and, with the chart [[eq:iii-c-1-2]] of [[ch:s17]] translated in t (g_(b₀) is stationary),

    ρ′_I := (T″ − x¹)/|x|     near infinity,     x¹ = t − |x|.

On 𝒟 near infinity t_* ≤ t^♭_*/C_♭ ≤ (T̂ + 3)/C_♭ ([[lem:ii-c-3-2]] (b)), so x¹ = t_* − C′ + 8m₀|x|⁻¹ ≤ T″ − 1 and
ρ′_I > 0 there. Fix c ∈ (0, ½] as in [[lem:iv2-2-1]], and R_9 ≥ max(R_5, 4R₁, 4C″); decreasing c, which nothing chosen
before it depends on, we take c ≤ min(½, 1/R_9).

**Lemma {#lem:s27-cover}** (The cover.) Put 𝒮 := 𝒟 ∩ {ρ′_I < c, r ≥ R_9} ∖ Ω_(ext,r_1) and
𝒦 := 𝒟 ∖ (Ω_(ext,r_1) ∪ 𝒮). Then:

(a) On 𝒟, ρ′_I < c forces |x| > 1/c ≥ R_9, so 𝒮 = 𝒟 ∩ {ρ′_I < c} ∖ Ω_(ext,r_1) has no side {r = R_9}; on {r ≥ R_9},
ρ′_I is defined and t_IVP = t − C″.

(b) 𝒟 ∩ {t_IVP < 0, r ≥ R_8} ⊂ Ω_(ext,r_1).

(c) 𝒦 is compact. Its boundary consists of the part of Σ^IVP in it, {t_IVP = −ν}, Σ^fut_(r_1) ∩ {ρ′_I ≥ c},
{ρ′_I = c}, {t^♭_* = T̂ + 3} and {r = r_♭}; the last four are spacelike, with 𝒦 to their past, for g_(b₀) and for every
metric C⁰-close to it on 𝒦 whose difference from g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b). So Ω_(ext,r_1) ∪ 𝒦 is closed
under past causal curves within 𝒟, and 𝒦 is the domain of dependence of the past part of its boundary.

(d) 𝒮 lies near the interior of ℐ⁺: x¹ is bounded on it. On 𝒮, t_IVP ≥ r/4.

*Proof.* (a) As x¹ ≤ T″ − 1 on 𝒟, ρ′_I < c gives |x| > (T″ − x¹)/c ≥ 1/c ≥ R_9. For r ≥ R_9 ≥ R₃, t_IVP = t − C″.
(b) For r ≥ R_8 ≥ 2r_1, ν(r) ≤ r/32 ≤ (r − r_1)/12, so the points of 𝒟 there with t_IVP < 0 lie in the past slab
{−(r − r_1)/12 ≤ t_IVP ≤ 0} of Ω_(ext,r_1). (c) On 𝒦 near infinity, above Σ^fut_(r_1), t_IVP ≥ r + 2r^(1−ℓ^♭_I) −
(r_1 + 2r_1^(1−ℓ^♭_I)) and t_IVP = t − C″, so x¹ ≥ C″ − r_1 − 2 (as ℓ^♭_I > 1 and r_1 ≥ 1), and ρ′_I ≥ c, so
|x| ≤ (T″ + r_1 + 2 − C″)/c. With t^♭_* ≤ T̂ + 3, t_IVP ≥ −ν and (b) on 𝒦, 𝒦 is closed and bounded, hence compact.
{ρ′_I = c} is spacelike with {ρ′_I < c} to its future ([[lem:iv2-1-1]] (a) in the translated chart); {t^♭_* = T̂ + 3}
is spacelike for the metrics named, dt^♭_* being past timelike ([[lem:ii-c-3-2]] (2)); {r = r_♭} is spacelike with dr
future timelike ([[lem:ii-c-3-2]] (1)); Σ^fut_(r_1) is spacelike ([[lem:iii-c1-1-1]]). For g_(b₀), dt_IVP is past
timelike ([[lem:iii-b-3-7]] (b)) and {t_IVP = −ν} is spacelike (after [[prop:iii-k-1-2]]); on the compact 𝒦 these
persist for C⁰-close metrics. The boundary that 𝒮 shares with Ω_(ext,r_1) ∪ 𝒦 lies in {ρ′_I = c} ∪ Σ^fut_(r_1), with
𝒮 to its future; so no past directed causal curve enters 𝒮 from Ω_(ext,r_1) ∪ 𝒦, and 𝒦 is the domain of dependence of
the part of its boundary in Σ^IVP ∪ {t_IVP = −ν} ∪ Σ^fut_(r_1). (d) 𝒮 is disjoint from Ω_(ext,r_1) and lies near
infinity, so by (b) it lies in {t_IVP ≥ 0} ∖ Ω_(ext,r_1), above Σ^fut_(r_1); so x¹ ≥ C″ − r_1 − 2 as in (c), and
x¹ ≤ T″ − 1. ρ′_I < c ≤ ½ gives t > (1 − c)|x| + T″ ≥ ½|x| + T″, so t_IVP > ½|x| + T″ − C″ ≥ r/4, as r ≥ R_9 ≥ 4C″.
∎

The slab 𝒮 is bounded by {ρ′_I = c} ∪ Σ^fut_(r_1) to the past and by {t^♭_* = T̂ + 3} to the future. Its points near
ℐ⁺ depend on all of Σ^IVP, so it is solved after 𝒦, together with the exterior: [[sec:iv3-0]]–[[sec:iv3-2]].
