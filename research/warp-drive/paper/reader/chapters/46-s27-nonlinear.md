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

#### The slab near null infinity: setting {#sec:iv3-0}

This subsection and the next two solve the gauge-fixed equation on the slab 𝒮 of [[lem:s27-cover]], near the interior
of ℐ⁺ up to {t^♭_* = T̂ + 3}, with its orders at ℐ⁺. The past boundary of 𝒮 contains the part of Σ^fut_(r_1) near ℐ⁺,
which reaches ℐ⁺ and is asymptotically null there; Cauchy data on it are avoided. The solution is instead posed on

    Ω^♮ := Ω_(ext,r_1) ∪ 𝒮,

from Σ^IVP_(r_1) and from the compact surface Σ_c where 𝒮 meets 𝒦, neither of which reaches ℐ⁺. The argument of
[[thm:iv2-2-4]] and [[thm:iv2-3-1]] then applies on Ω^♮, in the chart of [[ch:s17]] translated in t, and the solution
restricts to the exterior solution on Ω_(ext,r_1). [Hin26, p. 321] covers this region in one sentence ("for globally
small initial data, h_S thus exists … on φ_S({t_IVP ≥ 0}) ∩ {t_* ≤ 2}").

Let T₀ := C′ + 1 − 2R₁ be the constant of [[eq:iii-c-1-3]], and put

    ρ′_0 := (T″ − x¹)⁻¹,     x′_I := (ρ′_I)^(1/2),     U″ := cl_M{t_* ≤ T₀ + T″ − 2} ∩ {|x| ≥ 4R₁},

[[eq:iii-c-1-2]]–[[eq:iii-c-1-3]] with 2 replaced by T″. On U″, x¹ = t_* − C′ + 8m₀|x|⁻¹ ≤ T₀ + T″ − 2 − C′ + 2R₁ =
T″ − 1, so ρ′_0 ≤ 1, and (ρ′_0, ρ′_I, ω) are coordinates near I₀ ∪ ℐ⁺. On U the ratios ρ′_0/ρ_0 = (2 − x¹)/(T″ − x¹)
and ρ′_I/ρ_I are smooth and positive up to I₀ and ℐ⁺, tending to 1 at I₀; so the weighted b- and edge-b spaces of the
two charts coincide on U, with equivalent norms (the fibration of ℐ⁺ by ω is the same). Let

    Σ_c := {ρ′_I = c} ∩ ∂𝒮.

Σ_c is compact: on it x¹ ≥ C″ − r_1 − 2 (the proof of [[lem:s27-cover]] (c)), so |x| ≤ (T″ + r_1 + 2 − C″)/c. 𝒢″
denotes the class of [[def:iii-c-3-4]] on U″ in the coordinates (ρ′_0, ρ′_I).

*Translation.* t ↦ t − (T″ − 2) is an isometry of g_(b₀) (stationary in the coordinates of [[sec:iii-b-2]]) and of η,
and it maps the coordinates [[eq:iii-c-1-2]] and the frame [[eq:iii-c-1-6]] to those above. [[sec:iii-c-1]] and
[[sec:iii-c-4]] ([[lem:iii-c-1-1]], [[lem:iii-c-1-3]], [[lem:iii-c-4-1]]–[[lem:iii-c-4-3]], [[prop:iii-c-4-4]]) and
the results of [[ch:s26]] on the exterior region use the chart only through the form of η in it and through the bounds
of [[lem:iii-c-1-3]] for g_(b₀) − η, which are invariant under this map; so they hold on U″ in the translated chart, for
backgrounds in 𝒢″, with the same proofs.

**Lemma {#lem:iv3-0-1}** (The background on the slab.) Let S ∈ 𝒮_1 be small as in [[lem:iii-b-5-2]]. On a
neighbourhood of 𝒮̄ in U″, φ_S^*g_(b₀) agrees with an element of 𝒢″; on Ω_(ext,r_1) it is the background of
[[lem:iii-c2-1-1]].

*Proof.* On 𝒮, χ_IVP = 1, as t_IVP ≥ 0 > −|x|/10 ([[sec:iii-b-5]]). And χ_K = 0 on 𝒮: supp χ_K lies in the interior
of {χ^♯_K = 1} ⊂ supp χ^♯_K ⊂ {|x| < t/2}, while on 𝒮, t^♭_* ≤ T̂ + 3 gives t_* ≤ (T̂ + 3)/C_♭ and so x¹ ≤ T″ − 1,
so t ≤ |x| + T″ < 2|x| near infinity, where 𝒮 lies. So [[eq:iii-b-5-3]] holds near 𝒮̄:

    φ_S^*g_(b₀) − g_(b₀) − |x|⁻² 𝔥_S(ω)(dx¹)² ∈ ρ₀²ρ_I³ρ_+² C^∞(M; S²T*),

with 𝔥_S the function h_(S_w) of [[eq:iii-b-5-2]]; and g_(b₀) − η = m₀|x|⁻²(dx¹)² + |x|⁻³C^∞ on {|x| ≥ 3R₁}
([[lem:iii-c-3-5]] (1) and its proof). On 𝒮, ρ₀, ρ′_0 and ρ_+ are bounded below and ρ_I/ρ′_I is smooth and positive,
so φ_S^*g_(b₀) − η ∈ (ρ′_0)²(ρ′_I)²C^∞ with only the slot π₁₁ at that order, (dx¹)² being of type π₁₁, and the other
slots in (ρ′_0)²(ρ′_I)³C^∞: this is [[eq:iii-c-3-4]] in the translated chart, and φ_S^*g_(b₀) is smooth on M. On
Ω_(ext,r_1) the statement is [[lem:iii-c2-1-1]]. ∎

#### The curves on Ω^♮ {#sec:iv3-1}

**Lemma {#lem:iv3-1-1}** Let c_1 ∈ (0, c/4] and r_ext large. (a) {ρ′_I = c_1} = {t = (1 − c_1)|x| + T″} is spacelike
near infinity, with {ρ′_I < c_1} to its future. (b) For p ∈ Ω^♮ with ρ′_I(p) < c_1, the integral curves of
X′_I := ρ′_I∂_(ρ′_I) and of X′_0 − X′_I through p (the outgoing ray at fixed x¹, and the curve of fixed |x|), followed
in the direction of increasing ρ′_I, stay in Ω^♮ until they reach {ρ′_I = c_1}, which they do. (c)
Ω^♮ ∩ {ρ′_I < c_1} does not meet 𝒦, and Σ_c lies in {ρ′_I = c}.

*Proof.* (a) is [[lem:iv2-1-1]] (a) in the translated chart. (b) Near infinity, Ω^♮ ∩ {ρ′_I < c} is the set
{ρ′_I < c, t_IVP ≥ 0, t^♭_* ≤ T̂ + 3}: below Σ^fut_(r_1) it is Ω_(ext,r_1), above it 𝒮. So it suffices that along the
segment ρ′_I stays below c and t_IVP ≥ 0 and t^♭_* ≤ T̂ + 3 persist. *The ray.* Along it x¹ = x¹_p, and |x| decreases
to r_c := (T″ − x¹_p)/c_1, where ρ′_I = c_1 < c. t_* = x¹ + C′ − 8m₀|x|⁻¹ decreases along it. So does t^♭_*, along
this curve and the next: both are past directed causal for g_(b₀) (the ray is g_(b₀)-null, as
g_(b₀) = η + m₀|x|⁻²(dx¹)² there, [[lem:iii-b-3-5]] (b)), and dt^♭_* is past timelike for g_(b₀) ([[lem:ii-c-3-2]]
(2)). t_IVP = x¹ + |x| − C″ decreases too, and at r_c it is x¹_p(1 − c_1⁻¹) + T″c_1⁻¹ − C″, which is
≥ |x¹_p|(c_1⁻¹ − 1) + T″c_1⁻¹ − C″ > 0 if x¹_p < 0, and ≥ T″ − 1 + c_1⁻¹ − C″ > 0 if x¹_p ∈ [0, T″ − 1], for c_1 small;
and r_c = (T″ − x¹_p)/c_1 ≥ 1/c_1 ≥ 4/c ≥ 4R_9, as T″ − x¹ ≥ 1 on 𝒟 and c ≤ 1/R_9, so the ray stays in {r ≥ R_9}.
*The curve of fixed |x|.* t decreases to t_c := (1 − c_1)|x| + T″; t_* decreases; the curve may cross Σ^fut_(r_1) into
Ω_(ext,r_1); t_IVP(t_c) ≥ ½|x| + T″ − C″ > 0; and ρ′_I < c_1 along it, so it avoids 𝒦. (c) is the definition of 𝒮
and 𝒦 ⊂ 𝒟 ∖ 𝒮. ∎

So [[lem:iv2-1-2]] holds on Ω^♮_(c_1) := Ω^♮ ∩ {ρ′_I < c_1}, in the translated chart, with the same proof.

#### The solution on Ω^♮ {#sec:iv3-2}

**Theorem {#thm:iv3-2-1}** (The linear estimate on Ω^♮.) Let g_0 := φ_S^*g_(b₀) with |S| small, or g_0 := g_(b₀); h
small in H^(8,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω^♮) (weights at ℐ⁺ in ρ′_I); L := L^(χ^♮_0)_(g_0+h,g_0); α_0 > ℓ^♭_I, k ∈ ℕ₀ and
d := 4. For f ∈ H^(k+d,α_0+2,(−′,ℓ^♭_I+1))_b(Ω^♮), data ġ_0, ġ_1 ∈ H^(k+d,α_0)_b(Σ^IVP_(r_1)) and data
k̇_0, k̇_1 ∈ H^(k+d)(Σ_c), there is a unique ġ ∈ H^(k,α_0,(−,ℓ^♭_I))_b(Ω^♮) with Lġ = f, ġ = ġ_0 and
r ℒ_(∂_(t_IVP))ġ = ġ_1 on Σ^IVP_(r_1), and the Cauchy data (k̇_0, k̇_1) on Σ_c; and [[eq:iv2-2-3]] holds with
‖k̇_0‖_(H^(k+d)) + ‖k̇_1‖_(H^(k+d)) added to N(f, ġ_0, ġ_1; k + d) and their H⁸-norms added to N(f, ġ_0, ġ_1; 8).

*Proof.* As [[thm:iv2-2-4]], with three changes. *The gauge.* On Ω_(ext,r_1), χ^♮_0 = χ_0 ([[lem:iii-k-1-1]] (c));
on 𝒮, χ^♮_0 = 1 = χ_0, as t_IVP ≥ r/4 there ([[lem:s27-cover]] (d)); so L = L^(χ_0) on Ω^♮, and [[cor:iv2-4-1]]
applies, χ_0 = 1 on Ω^♮_(c_1) (ρ′_I < c_1 gives t_IVP ≥ r/4). *The background.* g_0 ∈ 𝒢″ near 𝒮̄ by
[[lem:iv3-0-1]], and in the class of [[lem:iii-c2-1-1]] on Ω_(ext,r_1); it is Ricci flat. *The regions.* Fix
c_1 ≤ c/4 so small that [[prop:iv1-2-2]] holds on Ω^♮_(c_1) with Σ_in := {ρ′_I = c_1} ∩ Ω^♮ and
Σ_fin := {t^♭_* = T̂ + 3} ∩ Ω^♮_(c_1), which is spacelike for g_0 + h, dt^♭_* being past timelike for every g_(b₀) + h′
with h′ small in 𝒢̃^(0,(1,0,0))_(e3b) ([[lem:ii-c-3-2]] (2)); every X′_I-curve there begins on Σ_in
([[lem:iv3-1-1]] (b)). Then:

(i) On Ω_N (near the interior of I₀, with the past slab), [[lem:iv2-2-2]] with the data on Σ^IVP_(r_1), unchanged.

(ii) On Ω^♮ ∩ {ρ′_I ≥ c_1/4} ∩ {τ′ ≥ 1/16}, away from ℐ⁺ (τ′ = t_IVP/|x| as in [[sec:iv2-0]]): its part in
Ω_(ext,r_1) by the first step of [[lem:iv2-2-3]] ([[prop:iv-4-1]] for the system near the interior of I₀, and standard
energy estimates on the compact part); then its part in 𝒮, which is compact (|x| ≤ 4(T″ − x¹)/c_1, x¹ bounded), by the
standard energy estimate for the Cauchy problem of a linear wave equation on a compact domain of dependence, with data
on Σ_c (given) and on Σ^fut_(r_1) ∩ {c_1/4 ≤ ρ′_I < c} (from the part in Ω_(ext,r_1)), both spacelike and compact. Its
boundary to the future, {ρ′_I = c_1/4}, {t^♭_* = T̂ + 3} and Σ^fut_(r_1) ∩ {ρ′_I ≥ c} (where Ω^♮ borders 𝒦), is
spacelike, so the region is closed under past causal curves within Ω^♮, and [[lem:ii-f-1-3]] gives uniqueness.

(iii) On Ω^♮_(c_1), the second step of [[lem:iv2-2-3]] and the steps of the proof of [[thm:iv2-2-4]] near ℐ⁺, with
c_1 in place of c: the cut-off χ̂_(c_1)(ρ′_I), [[prop:iv1-2-2]], and the two integrations of [[lem:iv2-1-2]] along the
curves of [[lem:iv3-1-1]]. Nothing in these steps uses ρ′_0 beyond its role as a coordinate; on 𝒮 it is bounded
below, where the weight at I₀ is immaterial.

The forcing of each step vanishes near its initial surface after the cut-offs of the proof of [[thm:iv2-2-4]] and of
[[lem:iv2-2-3]], and the estimates compose as there; the data on Σ_c enter through (ii) only, at the order of
H^(k+4). Uniqueness: [[lem:ii-f-1-3]] on each region. ∎

**Theorem {#thm:iv3-2-2}** (The nonlinear solution on Ω^♮; [Hin26, p. 321].) Let g_0 be as in [[thm:iv3-2-1]],
(h_0, h_1) data on Σ^IVP_(r_1) as in [[thm:iv2-3-1]], and (k_0, k_1) the Cauchy data on Σ_c of a solution of
P^♮(g_0 + h, g_0) = 0 on a neighbourhood of Σ_c in 𝒦 ∪ Ω_(ext,r_1) that agrees on Ω_(ext,r_1) with the solution of
[[thm:iv2-3-1]]. If ‖h_j‖_(H^(2d,ℓ^♭_0)_b) + ‖k_j‖_(H^(2d)(Σ_c)) < ε_0 (d = 7), there is a unique
h ∈ H^(∞,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω^♮), small in H^(3d), with P^♮(g_0 + h, g_0) = 0 and these data; it equals the solution of
[[thm:iv2-3-1]] on Ω_(ext,r_1), and the higher norms are bounded as there.

*Proof.* The proof of [[thm:iv2-3-1]] on Ω^♮, with the spaces F^k of right sides enlarged by H^k(Σ_c)² and the map by
the traces on Σ_c minus (k_0, k_1); the right inverses are those of [[thm:iv3-2-1]], and the smoothing and the map are
as there (P^♮ = P^(χ_0) on Ω^♮, and [[cor:iii-c-5-3]] holds for it by [[lem:iii-c2-2-1]], near 𝒮 in the translated
chart). Ω_(ext,r_1) is closed under past causal curves within Ω^♮, and its past boundary is
Σ^IVP_(r_1) ∪ Σ^past_(r_1); so on it the solution depends on (h_0, h_1) only, and it is the solution of
[[thm:iv2-3-1]] by uniqueness there. ∎

So the solution of [[prop:iii-k-1-2]] on 𝒮 is the restriction of that of [[thm:iv3-2-2]], with (k_0, k_1) from the
compact part (whose data on Σ^fut_(r_1) ∩ {ρ′_I ≥ c} come from the exterior); the three solutions agree on overlaps by
[[lem:ii-f-1-3]] with the compact sets of [[lem:iii-k-6-2]].

**Corollary {#cor:iv3-2-3}** (The orders on the slab.) Under the hypotheses of [[thm:iii-c1-3-1]] on the data, the
solution of [[thm:iv3-2-2]] lies in H^(∞,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b(Ω^♮), with the bound [[eq:iii-c1-3-2]]; in
particular h_S has the orders (⟨ℰ^C_I⟩, ℓ_I) at ℐ⁺ on 𝒮, as [[prop:iii-k-1-2]] (3) states.

*Proof.* The proof of [[thm:iii-c1-3-1]] on Ω^♮, with [[thm:iv3-2-1]] in place of the linear estimate
[[eq:iii-c1-2-2]]. Its Step 1 works at I₀, which Ω^♮ meets only within Ω_(ext,r_1); its Step 2 integrates, slot by
slot, along X_I and X_0 − X_I near ℐ⁺ ([[lem:iii-a-1-2]], [[lem:iii-a-3-2]]), and on Ω^♮_(c_1) the curves followed
backward reach {ρ′_I = c_1}, where the solution is smooth ([[lem:iv3-1-1]] (b)); away from ℐ⁺ there is nothing to show.
The structure [[eq:iii-c-4-4]] used there holds near 𝒮 by [[lem:iv3-0-1]] and the translation. ∎
