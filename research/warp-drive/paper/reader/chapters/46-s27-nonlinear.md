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

In dimension 4 + 1 the argument of [Hin26] needs four changes. (1) The initial family solves a gauge-fixed equation
whose gauge is cut off near the initial surface ([[thm:iii-c2-3-1]]), while the map Ψ uses the gauge of the forward
cone; the cut-off of [[lem:iii-k-1-1]] equals 1 on Ω_* and agrees with that of [[thm:iii-c2-3-1]] on the exterior
domain. (2) The background of [[ch:s21]] is translated as well as boosted ([[def:iii-i7-1-2]]), so the initial family
is posed for a translation composed with a boost ([[prop:iii-k-1-2]]). (3) The Nash–Moser theorem with support classes
asks for support conditions on every component of supported character ([[sec:iii-k-3]]). (4) The right inverses of
[[thm:iii-j1-2-1]] are formed for Ψ, in which the boost and translation directions carry the initial family
([[lem:iii-k-2-3]]). The region near null infinity that the initial family must
reach, a slab bounded in t_*, is solved together with the exterior problem ([[sec:iv3-0]]–[[sec:iv3-2]]), and the
compact sets that the uniqueness lemma [[lem:ii-f-1-3]] asks for are supplied near ℐ⁺ and near spatial infinity by
[[lem:iii-k-6-1]] and [[lem:iii-k-6-2]].

*Notation and the inner radius.* The notation is that of [[ch:s11]]–[[ch:s25]]. b₀ = (m₀, 0), R₁ = m₀^(1/2), and the
inner radius r_♭ ∈ (0, ½R₁] of [[ch:s11]] is a parameter: the spacetime M of [[eq:iii-b-2-1]] has the inner boundary
{|x| = r_♭}, and the radius r_0 of the artificial boundary of [[ch:s04]]–[[ch:s10]] is r_♭ ([[def:s12-radii]]), as
in [[ch:s19]]. Every result of this chapter holds for each such r_♭, with constants and neighbourhoods of b₀ that may
depend on it. C′ is the constant of [[eq:iii-b-3-6]], so that t_* = t − |x| + C′ − 8m₀|x|⁻¹ on {|x| ≥ 3R₁}, and C″ is
the constant value of ψ_IVP on [R₃, ∞) ([[lem:iii-b-3-7]] (b)), so that t_IVP = t − C″ on {|x| ≥ R₃}. The time function
t^♭_* is that of [[lem:ii-c-3-2]] with ℓ = ½, built with the constant C of the gluing in its proof, written C_g here,
taken ≥ max(4(r′_0 + 1), 32, 16R₁), r′_0 the radius of [[lem:ii-c-3-2]]. Every condition that proof places on C_g is a
lower bound, so this is allowed; [[lem:ii-e-1-2]] (iv) takes C_g ≥ 4(r′_0 + 1), and [[lem:s27-below]] uses the other two
bounds. The constant C′ of [[lem:ii-c-3-2]] (b) is written C_♭ ∈ (0, 1) here, to distinguish it from the constant of
[[eq:iii-b-3-6]]. M_(1/2) is the space of [[def:iii-b-2-1]] on which ρ_I^(1/2) is
smooth. For S = S_w ∈ 𝒮_1 we write |S| := |w|. The boosts φ_S, S ∈ 𝒮_1, are those of [[sec:iii-b-5]] and the
translations ψ_(S⁰), S⁰ ∈ 𝒮_1, those of [[lem:iii-i7-1-1]]; for S, S⁰ ∈ 𝒮_1 put

    φ_(S,S⁰) := ψ_(S⁰) ∘ φ_S,     so that φ_(S,0) = φ_S.                                                {#eq:s27-motion}

Both factors are time-1 flows of b-vector fields, φ_(−S) = φ_S⁻¹ and ψ_(−S⁰) = ψ_(S⁰)⁻¹ ([[lem:iii-b-5-1]],
[[lem:iii-i7-1-1]] (a)), so φ_(S,S⁰)⁻¹ = φ_(−S) ∘ ψ_(−S⁰).

### Setting {#sec:iii-k-0}

*The time functions.* t^♭_* is defined on {t_* ≥ ½} ([[lem:ii-c-3-2]], [[lem:ii-e-1-2]] (iv)), with
C_♭ t_* ≤ t^♭_* ≤ t_* there ([[lem:ii-c-3-2]] (b)); a sublevel set {t^♭_* ≤ c}, c ≥ 1, means the complement of
{t^♭_* > c}, which lies in {t_* > c}. Ω_* := cl_M{t^♭_* ≥ 1}. Put

    T̂ := 2/C_♭ ≥ 2,     T_ι := (T̂ + 2)/C_♭,     T_K := max(10, T_ι + 2),

so that {t^♭_* ≥ T̂} ⊂ Ω_*. Every level used below, the top of the region 𝒟 of [[prop:iii-k-1-2]] and the levels of the
support classes of [[sec:iii-k-3]], lies at t^♭_* ≥ T̂ ≥ 2. The cut-off χ_−, the region 𝒟 and the support classes are
defined by t^♭_*. Its differential is past timelike for every g_(b₀) + h with h small in 𝒢̃^(0,(1,0,0))_(e3b), on
{t_* > 1} by [[lem:ii-c-3-2]] (2), and on {t_* > ½}, for h small in that class on {t_* ≥ ½}, by [[lem:s27-below]]; this
margin survives the perturbations used below. The timelike margin of dt_* near ℐ⁺ is only of order m₀r⁻², as
g_(b₀)⁻¹(dt_*, dt_*) = −16m₀r⁻² + O(r⁻⁴) there, and a perturbation h₀₀ of order ρ_I^z, Re z < 2, can overturn it. t^♭_*
is smooth on M_(1/2) near ℐ⁺ ([[lem:ii-c-3-2]] (a)) and equals t_* on ℐ⁺.

*The cut-off χ_K and the background.* We take the cut-offs χ^♭_K, χ_K, χ^♯_K of [[sec:iii-b-5]] with the condition
[[eq:iii-i-1-2]] at the threshold T_K in place of 10, a condition of the same kind:

    supp χ_K ⊂ {t^♭_* ≥ T_K};

so χ_K = 0 on {t_* < T_K}, as t^♭_* ≤ t_*. Every statement of [[ch:s19]]–[[ch:s25]] holds with this threshold, the
supports only shrinking. The cut-offs being chosen consistently, the threshold 60R₁ of [[sec:iii-b-5]] at which
χ^♭_K = 1 on {|x| < t/10} is raised with T_K, as [[eq:iii-i-1-2]] presumes: there is T′ ≥ 60R₁ with χ^♭_K = 1 on
{|x| < t/10, t > T′}. g_(b₀,b,−S) is [[eq:iii-i-1-1]], and P_5 is the augmented operator [[eq:iii-i14-1-3]]; its
background at p⃗_(≤0) = (S, b − b₀, S^(0)_1) is the translated background of [[eq:iii-i7-1-3]],

    g_(p⃗) = (1 − χ_K) φ_(−S,−S^(0)_1)^* g_(b₀) + χ_K g_b,

which is g_(b₀,b,−S) when S^(0)_1 = 0. Φ, the data space 𝒟, the class ℱ and 𝒳_J are those of [[def:iii-j-1-1]],
[[def:iii-j-classes]] and [[thm:iii-j-2-4]], and 𝒟_ex, ℱ_ex, 𝒳_(J,ex), 𝒬_ex are the exact classes of [[def:iii-j3-1-1]].
The data space is always written with a sub- or superscript (𝒟_ex, 𝒟^k_ex, 𝒟^∞_ex) below, so that 𝒟 alone denotes the
region of [[prop:iii-k-1-2]].

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
[T_ι + 1, ∞). Then χ_ι = 0 on {t_* ≤ T_ι} ⊃ {t^♭_* ≤ T̂ + 2} (as C_♭t_* ≤ t^♭_*), and supp dχ_ι ⊂ {T_ι ≤ t_* ≤ T_ι + 1}
is disjoint from supp χ_K, as T_K > T_ι + 1. [[sec:iii-g2-4]] uses χ_ι in the proof of [[thm:iii-g2-4-2]] only through
χ_ι = 1 near ι⁺ and through the commutator of L_b with χ_ι, which is χ′(t_*) and χ″(t_*) times commutators of L_b with
t_* and so is supported where χ′(t_*) ≠ 0, a compact t_*-interval; [[ch:s23]] uses it in [[eq:iii-j-2-1]] and the results
built on it only as a real function of t_*, equal to 1 near ι⁺ and supported in Ω_*. Both hold for this choice, so it is
admissible, and the ι⁺-terms of Φ do not reach the region of the initial family.

### The initial family {#sec:iii-k-1}

**Lemma {#lem:iii-k-1-1}** (The cut-off of the gauge.) Let χ_♮ ∈ C^∞(ℝ) equal 0 on (−∞, ½] and 1 on [1, ∞), let χ_0
be the cut-off of [[sec:iii-c2-2]], χ_0 = 1 − χ̌_0(t_IVP/r) with χ̌_0 ∈ C^∞_c((−¼, ¼)) equal to 1 on [−⅛, ⅛], and

    χ^♮_0 := 1 − (1 − χ_0)(1 − χ_♮(t_*)).                                                             {#eq:iii-k-1-1}

Then: (a) χ^♮_0 ∈ C^∞(M); (b) χ^♮_0 = 1 on {t_* ≥ 1} ⊃ Ω_*; (c) χ^♮_0 = χ_0 on {t_* ≤ ½}, and on Ω_(ext,r_1) for
r_1 ≥ R_6; (d) χ^♮_0 = 0 near Σ^IVP, and near φ(Σ^IVP) for φ = φ_(S,S⁰) and φ = φ_(S,S⁰)⁻¹, |S| + |S⁰| small.

Here Ω_(ext,r_1) is the exterior domain of [[lem:iii-c1-1-1]] at the radius r_1. The proof of (d) uses the following
bound on the boosts and translations.

**Lemma {#lem:s27-boost-move}** (Boosts and translations move t_IVP and r by O((|S| + |S⁰|)r).) There is C such that
for S, S⁰ ∈ 𝒮_1 with |S|, |S⁰| ≤ 1, for φ = φ_(S,S⁰) and φ = φ_(S,S⁰)⁻¹, and for every p ∈ M,

    |t_IVP(φ(p)) − t_IVP(p)| ≤ C(|S| + |S⁰|) r(p),     |r(φ(p)) − r(p)| ≤ C(|S| + |S⁰|) r(p).

φ is the identity on {|x| ≤ 5R₁} and maps {|x| > 5R₁} into itself.

*Proof.* *Boosts.* φ_(S_w) is the time-1 flow of V(S_w) = ½χ_r(|x|)χ^♯_IVP(1 − χ^♭_K)X_w,
X_w = t w·∂_x + (w·x)∂_t ([[lem:iii-b-5-1]]); φ_(−S) is that of V(S_(−w)) = −V(S_w). As 1 − χ^♭_K = 0 on
{|x| < t/10, t > T′} ([[sec:iii-k-0]]), every point of supp V(S_w) has t ≤ 10|x| + T′. And t ≥ −½|x| on supp V(S_w):
there χ^♯_IVP ≠ 0, so t_IVP > −|x|/2 ([[sec:iii-b-5]]), and t = t_IVP + ψ_IVP(|x|) ≥ t_IVP as ψ_IVP ≥ 0
([[lem:iii-b-3-7]] (b)). So |t| ≤ 10|x| + T′ ≤ C|x| there, |x| ≥ r_♭ being bounded below. With X_w|x| = t S_w(x̂),
t_IVP = t − ψ_IVP(|x|), and
0 ≤ ψ_IVP′ ≤ ψ′ ≤ 1 on {|x| ≥ 5R₁} ⊃ supp V(S_w) ([[lem:iii-b-3-7]] (b); ψ′ = 1 − 8m₀|x|⁻² there),

    |V(S_w)|x|| ≤ ½|w||t| ≤ C|w||x|,     |V(S_w)t_IVP| = ½χ_rχ^♯_IVP(1 − χ^♭_K)|w·x − ψ_IVP′ t S_w(x̂)| ≤ C|w||x|

on M, the left sides vanishing off supp V(S_w). Along an integral curve γ(s), s ∈ [0, 1], of ±V(S_w),
|d log|x(γ(s))|/ds| ≤ C|w|, so e^(−C|w|)|x(γ(0))| ≤ |x(γ(s))| ≤ e^(C|w|)|x(γ(0))|; and
|d t_IVP(γ(s))/ds| ≤ C|w||x(γ(s))| ≤ Ce^(C|w|)|w||x(γ(0))|. Integrating over s ∈ [0, 1] gives both bounds for φ_(±S),
as e^(C|w|) − 1 ≤ C|w|e^C and 1 − e^(−C|w|) ≤ C|w| for |w| ≤ 1. *Translations.* ψ_(S⁰), S⁰ = S_w, is the time-1 flow
of V⁰(S⁰) = ½Θ w·∂_x, with Θ = χ_r(|x|)χ^♯_IVP(1 − χ^♭_K) ∈ [0, 1] ([[lem:iii-i7-1-1]]), and ψ_(−S⁰) is that of
−V⁰(S⁰). So |V⁰(S⁰)|x|| = ½Θ|w·x̂| ≤ ½|w| and |V⁰(S⁰)t_IVP| = ½Θψ_IVP′|w·x̂| ≤ ½|w|, as ψ_IVP′ ∈ [0, 1] on
supp Θ ⊂ {|x| ≥ 5R₁}. An integral curve of ±V⁰(S⁰) that moves starts and stays in {|x| > 5R₁} (below), so in time 1
it changes |x| and t_IVP by at most ½|w| ≤ |w||x(p)|/(10R₁); this gives both bounds for ψ_(±S⁰). *Composites.* For
φ_(S,S⁰) = ψ_(S⁰) ∘ φ_S and q := φ_S(p), r(q) ≤ (1 + C|S|)r(p) ≤ (1 + C)r(p), so
|t_IVP(ψ_(S⁰)(q)) − t_IVP(p)| ≤ C|S⁰|r(q) + C|S|r(p) ≤ C′(|S| + |S⁰|)r(p) and
|r(ψ_(S⁰)(q)) − r(p)| ≤ C|S⁰|r(q) + C|S|r(p) ≤ C′(|S| + |S⁰|)r(p); likewise for φ_(S,S⁰)⁻¹ = φ_(−S) ∘ ψ_(−S⁰).
V(S_w) and V⁰(S⁰) vanish on {|x| ≤ 5R₁} (χ_r = 0 there), whose points are fixed by the flows; by uniqueness of
integral curves no curve starting in {|x| > 5R₁} reaches it. ∎

*Proof of [[lem:iii-k-1-1]].* (a) χ_0 ∈ C^∞(M) ([[sec:iii-c2-2]]). Near ℐ⁺, t_* is a smooth function on M
([[eq:iii-b-3-6]]); near I₀ and near the corner I₀ ∩ ℐ⁺, t_* → −∞, so χ_♮(t_*) = 0; near ι⁺ and K⁺, t_* → +∞, so
χ_♮(t_*) = 1. (b) There χ_♮(t_*) = 1, and t^♭_* ≤ t_*. (c) The first claim is clear. On
Ω_(ext,r_1) ∩ {t_* > ½}, r ≥ r_1 ≥ R_6, so t_IVP = t_* + F(r) > r/4 by [[eq:s27-f]], where χ_0 = 1
([[sec:iii-c2-2]]); both cut-offs are 1 there. (d) On Σ^IVP, t_* = −F ≤ 0. Let ν_0 := min(¼, r_♭/8). On
{|t_IVP| < ν_0}, a neighbourhood of Σ^IVP, t_* ≤ t_IVP < ¼, so χ_♮(t_*) = 0; and |t_IVP| < r/8 as r ≥ r_♭, so
χ_0 = 0. Hence χ^♮_0 = 0 there. Let p be near φ(Σ^IVP), p = φ(q) with |t_IVP(q)| small. If r(p) ≥ R_6 + 1, then by
[[lem:s27-boost-move]], applied to φ⁻¹ at p, |t_IVP(p)| ≤ |t_IVP(q)| + C(|S| + |S⁰|)r(p) < r(p)/8 for |S| + |S⁰|
and |t_IVP(q)| small, so χ_0(p) = 0, and t_*(p) = t_IVP(p) − F(r(p)) < r(p)/8 − r(p)/4 < 0, so χ_♮(t_*(p)) = 0. On
the compact set {r ≤ R_6 + 2} ∩ M, φ tends to the identity smoothly as (S, S⁰) → 0, so φ(Σ^IVP) ∩ {r ≤ R_6 + 1} lies
in {|t_IVP| < ν_0} for |S| + |S⁰| small, and χ^♮_0 = 0 there, as just shown. ∎

The exterior theory of [[ch:s26]] is stated for the boosts φ_S. It holds for φ_(S,S⁰), with the same proofs:

**Lemma {#lem:s27-translated-exterior}** (The exterior theory for translated boosts.) Let S, S⁰ ∈ 𝒮_1 be small.

(a) φ_(S,S⁰) is a diffeomorphism of M with the properties stated for φ_(S_w) in [[lem:iii-b-5-1]], smooth in
(S, S⁰), and the identity on {|x| ≤ 5R₁}.

(b) With 𝔥_S the function h_(S_w) of [[eq:iii-b-5-2]] (S = S_w), for every b near b₀,

    χ_IVP(1 − χ_K)(φ_(S,S⁰)^*g_b − (g_b + |x|⁻²𝔥_S(ω)(dx¹)²)) ∈ ρ₀²ρ_I³ρ_+²C^∞(M; S²T*),

smoothly in (S, S⁰).

(c) [[lem:iii-c2-1-1]], [[thm:iii-c2-3-1]] and [[rem:iii-c2-3-2]] hold with φ_(S,S⁰) in place of φ_S and |S| + |S⁰|
in place of |S|.

*Proof.* (a) φ_S and ψ_(S⁰) have these properties ([[lem:iii-b-5-1]], [[lem:iii-i7-1-1]] (a)), and they persist under
composition. (b) is [[lem:iii-i7-1-3]] (a), stated there for the composite ψ_(−S^(0)_1) ∘ φ_(−S) at every small pair
(−S, −S^(0)_1), hence for φ_(S,S⁰) at every small (S, S⁰); its leading term is that of φ_S. (c) The proof of
[[lem:iii-c2-1-1]] uses of φ_S only [[eq:iii-b-5-3]] on Ω_(ext,r_1) ⊂ {χ_IVP(1 − χ_K) = 1} and the naturality of Ric,
and (b) is [[eq:iii-b-5-3]] for φ_(S,S⁰). The proof of [[thm:iii-c2-3-1]] uses of φ_S: that near |x| = r it moves t_IVP
and r by at most C|S|r, so that it maps a neighbourhood of Σ_(IVP,r₁) into {|t_IVP| < r/8} ∩ Ω_(ext,r₀) (after
[[eq:iii-c2-3-1]]), which [[lem:s27-boost-move]] gives for φ_(S,S⁰) with C(|S| + |S⁰|); the naturality of Ric and of Υ⁰
([[eq:iii-c2-2-2]]) under diffeomorphisms; that S ↦ φ_S^*g_(b₀) is smooth, with derivative in ρ₀²ρ_I²C^∞ with the
slots of [[eq:iii-c-3-4]] on Ω_(ext,r_1), which (b), differentiated in (S, S⁰), gives; and that pull-back by the flow
of a b-vector field tangent to every boundary hypersurface preserves the weighted, partially polyhomogeneous b-Sobolev
spaces near compact subsets of the interior of I₀, which holds for both factors by (a). [[rem:iii-c2-3-2]] is
uniqueness. ∎

Let

    P^♮(g, g_0) := Ric(g) − δ*_(g_0,E_C) Υ^(χ^♮_0E_Υ)(g, g_0),

[[eq:iii-c2-2-1]] with χ^♮_0 in place of χ_0. Its linearisation in g at (g, g_0) is written L^(χ^♮_0)_(g,g_0).

**Proposition {#prop:iii-k-1-2}** (The initial family; [Hin26, (13.5) and (12.33)].) Let γ = γ_(b₀) + γ̃ and
k = k_(b₀) + k̃ be data on Σ^IVP satisfying the constraint equations, with γ̃ ∈ H^(∞,(ℰ_0,ℓ_0))_b and
k̃ ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b, small in H^(d_0) of these classes, where d_0 is the largest of the regularities that
[[thm:iii-c2-3-1]] (with [[thm:iii-c1-3-1]]), [[thm:iv3-2-2]] and the local theory on 𝒦 in the proof below ask of the
data. Let h̊_0, h̊_1 be the Cauchy data of [[prop:iii-c2-4-1]] for (γ, k). For S, S⁰ ∈ 𝒮_1 small let h⁰_(S,S⁰),
h¹_(S,S⁰) be the pulled-back data [[eq:iii-c2-3-1]] of these, with φ_(S,S⁰) in place of φ_S, now on all of Σ^IVP. Let
N_ν := {t_IVP ≥ −ν(r)}, with ν smooth and non-decreasing, ν = 0 on [0, R_ν], R_ν := ½(r_♭ + 5R₁), ν > 0 on (R_ν, ∞),
0 ≤ ν′ ≤ 1/32, and ν(r) = r/64 for r ≥ 16R_8, where R_8 ≥ max(2r_1, 8, 5R₁) is fixed in [[lem:s27-cover]]. Such ν
exists, as 16R_8/64 ≤ (16R_8 − R_ν)/32; and ν(r) ≤ (r − R_ν)/32 ≤ r/32. So {t_IVP = −ν} is spacelike for g_(b₀) (see
below), N_ν = {t_IVP ≥ 0} near {r = r_♭}, and {r = r_♭} is an inflow boundary for a backward problem. Put

    𝒟 := N_ν ∩ {t^♭_* ≤ T̂ + 3},     𝒟_(S,S⁰) := φ_(S,S⁰)⁻¹({t_IVP ≥ 0}) ∩ {t^♭_* ≤ T̂ + 2}.

For |S| + |S⁰| small, 𝒟_(S,S⁰) ⊂ 𝒟, and φ_(S,S⁰) maps a neighbourhood of Σ^IVP ∪ φ_(S,S⁰)⁻¹(Σ^IVP) in N_ν into N_ν. There
is a unique h_(S,S⁰) on 𝒟 with

    P^♮(φ_(S,S⁰)^*g_(b₀) + h_(S,S⁰), φ_(S,S⁰)^*g_(b₀)) = 0,
    h_(S,S⁰) = h⁰_(S,S⁰),  r ℒ_(∂_(t_IVP)) h_(S,S⁰) = h¹_(S,S⁰)  on Σ^IVP,                                {#eq:iii-k-1-2}

and:

(1) h_(S,S⁰) = φ_(S,S⁰)^*h_0 on a neighbourhood of Σ^IVP ∪ φ_(S,S⁰)⁻¹(Σ^IVP) in 𝒟, where h_0 := h_(0,0) on 𝒟, a
two-sided neighbourhood of Σ^IVP off {r ≤ R_ν}; on {r ≤ R_ν}, 𝒟 ends at Σ^IVP and φ_(S,S⁰) is the identity, so
φ_(S,S⁰)^*h_0 is defined there. Hence φ_(S,S⁰)^*g_(b₀) + h_(S,S⁰) = φ_(S,S⁰)^*(g_(b₀) + h_0) there;

(2) Ric(φ_(S,S⁰)^*g_(b₀) + h_(S,S⁰)) = 0 and Υ^(χ^♮_0E_Υ)(φ_(S,S⁰)^*g_(b₀) + h_(S,S⁰), φ_(S,S⁰)^*g_(b₀)) = 0 on 𝒟;
on 𝒟 ∩ Ω_* the gauge 1-form is Υ^(E_Υ) ([[lem:iii-k-1-1]] (b)), which is [Hin26, (12.33b)];

(3) on 𝒟 ∩ Ω_*, h_(S,S⁰) ∈ H̄^(∞,(⟨ℰ^C_I⟩,ℓ_I))_b (orders at ℐ⁺; the set is bounded in t_*); h_(S,S⁰) is C^l in
(S, S⁰) with values in each H^k of this class, for data of regularity depending on k and l ([[thm:iii-c2-3-1]] (2)); and
for each k there are k′_k, s_k > 0 and a non-decreasing ω_k : [0, s_k] → [0, ∞) with ω_k(s) → 0 as s → 0 such that,
if ‖(γ̃, k̃)‖_(H^(k+k′_k)) ≤ s_k,

    ‖h_(S,S⁰)‖_(H^(k+2)) + ‖∂_(S,S⁰)h_(S,S⁰)‖_(H^(k+2)) + ‖∂²_(S,S⁰)h_(S,S⁰)‖_(H^(k+2)) ≤ ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))),

in the norms of this class, uniformly for |S| + |S⁰| small (the shift by 2 is the order of P_5, as [[lem:iii-k-2-2]]
uses it). We take k′_k non-decreasing in k.

*The hypersurface {t_IVP = −ν} and the inclusions.* In the Kerr–Schild coordinates of [[lem:iii-b-3-7]],
t_IVP + ν = t − (ψ_IVP − ν)(|x|) has differential dt_KS − β′ d|x| with β′ = β_IVP − ν′, where β_IVP :=
ψ_IVP′ + 2χ_∞m₀/(|x|² − m₀) is the coefficient of t_IVP in the proof of [[lem:iii-b-3-7]]. There β_IVP ≤ 1, β_IVP > 0
on [5R₁, ∞), and on [r_♭, 5R₁], where β_IVP = 1 − χ_∞(8m₀/ϱ² − 2m₀/(ϱ² − m₀)) (ϱ = |x|), either χ_∞ = 0 and
β_IVP = 1, or ϱ ≥ 2R₁ and 8m₀/ϱ² − 2m₀/(ϱ² − m₀) ≤ 6m₀/ϱ² ≤ 3/2, so β_IVP ≥ −½. As 0 ≤ ν′ ≤ 1/32,
β′ ∈ (−1, 1], and d(t_IVP + ν) is timelike for g_(b₀) by [[lem:iii-b-3-3]] (e) and [[lem:s11-ks-domain]]: {t_IVP = −ν}
is spacelike. Near {r = r_♭}, ν = 0, and {r = r_♭} is spacelike with dr future timelike ([[lem:ii-c-3-2]] (1)), N_ν
lying to its past; past directed causal curves from points with r > r_♭ stay in {r ≥ min(r(p), r^♮)}, so a backward
problem needs no data there. For the inclusions: φ := φ_(S,S⁰) and φ⁻¹ are the identity on {r ≤ 5R₁} and map
{r > 5R₁} into itself, where they move t_IVP and r by at most C(|S| + |S⁰|)r ([[lem:s27-boost-move]]); and
ν(r) ≥ c_ν r on [5R₁, ∞), with c_ν := min(ν(5R₁)/(16R_8), 1/64) > 0. Let C(|S| + |S⁰|) ≤ min(¼c_ν, ⅓). Then
φ⁻¹({t_IVP ≥ 0}) ⊂ N_ν: a point p of it with r(p) > 5R₁ has t_IVP(p) ≥ −¼c_ν r(p) > −ν(r(p)). In particular
𝒟_(S,S⁰) ⊂ 𝒟, and φ⁻¹(Σ^IVP) lies in W := N_ν ∩ {t_IVP > −⅓c_ν r}, a neighbourhood of Σ^IVP ∪ φ⁻¹(Σ^IVP) in N_ν. And
φ(W) ⊂ N_ν: for p ∈ W with r(p) > 5R₁, t_IVP(φ(p)) > −(⅓ + ¼)c_ν r(p) and r(φ(p)) ≥ ⅔r(p), so
t_IVP(φ(p)) > −c_ν r(φ(p)) ≥ −ν(r(φ(p))). (φ_(S,S⁰)⁻¹, not φ_(S,S⁰), appears in 𝒟_(S,S⁰): φ_(S,S⁰)^*h_0 at p needs
h_0 at φ_(S,S⁰)(p).)

#### The cover of 𝒟 {#sec:s27-cover}

Let r_ext ≥ R_0 be the exterior radius at which [[thm:iii-c2-3-1]] is applied, for φ_(S,S⁰) by
[[lem:s27-translated-exterior]] (c) (R_0 that of [[lem:iii-c1-1-1]]), and r_1 := 2r_ext ≥ R_6, the radius of its
boosted problem; Ω_(ext,r_1), Σ^IVP_(r_1) := Ω_(ext,r_1) ∩ Σ^IVP and its future
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

(c) 𝒦 is compact. Its boundary lies in the union of Σ^IVP ∩ {r ≤ R_ν}, {t_IVP = −ν}, Σ^fut_(r_1) ∩ {ρ′_I ≥ c},
Σ^past_(r_1), {ρ′_I = c}, {t^♭_* = T̂ + 3} and {r = r_♭}. These are spacelike, for g_(b₀) and for every metric C⁰-close
to it on 𝒦 whose difference from g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b); 𝒦 lies to the future of the first three and
to the past of the other four. So Ω_(ext,r_1) ∪ 𝒦 is closed under past causal curves within 𝒟. 𝒦⁺ := 𝒦 ∩ {t_IVP ≥ 0}
is the domain of dependence of its part of Σ^IVP together with Σ^fut_(r_1) ∩ {ρ′_I ≥ c}; and 𝒦⁻ := 𝒦 ∩ {t_IVP ≤ 0} is,
for the reversed time orientation, the domain of dependence of its part of Σ^IVP together with Σ^past_(r_1) ∩ 𝒟, where
𝒦 reaches below the past slab of Ω_(ext,r_1) (for r slightly above r_1, where ν(r) > (r − r_1)/12).

(d) 𝒮 lies near the interior of ℐ⁺: x¹ is bounded on it. On 𝒮, t_IVP ≥ r/4.

*Proof.* (a) As x¹ ≤ T″ − 1 on 𝒟, ρ′_I < c gives |x| > (T″ − x¹)/c ≥ 1/c ≥ R_9. For r ≥ R_9 ≥ R₃, t_IVP = t − C″.
(b) For r ≥ R_8 ≥ 2r_1, ν(r) ≤ r/32 ≤ (r − r_1)/12, so the points of 𝒟 there with t_IVP < 0 lie in the past slab
{−(r − r_1)/12 ≤ t_IVP ≤ 0} of Ω_(ext,r_1). (c) On 𝒦 near infinity, above Σ^fut_(r_1), t_IVP ≥ r + 2r^(1−ℓ^♭_I) −
(r_1 + 2r_1^(1−ℓ^♭_I)) and t_IVP = t − C″, so x¹ ≥ C″ − r_1 − 2 (as ℓ^♭_I > 1 and r_1 ≥ 1), and ρ′_I ≥ c, so
|x| ≤ (T″ + r_1 + 2 − C″)/c. With t^♭_* ≤ T̂ + 3, t_IVP ≥ −ν and (b) on 𝒦, 𝒦 is closed and bounded, hence compact.
Where ν = 0, that is on {r ≤ R_ν}, 𝒟 = {t_IVP ≥ 0} near Σ^IVP, so only there is Σ^IVP part of the boundary of 𝒦.
{ρ′_I = c} is spacelike with {ρ′_I < c} to its future ([[lem:iv2-1-1]] (a) in the translated chart); {t^♭_* = T̂ + 3}
is spacelike for the metrics named, dt^♭_* being past timelike ([[lem:ii-c-3-2]] (2)); {r = r_♭} is spacelike with dr
future timelike ([[lem:ii-c-3-2]] (1)); Σ^fut_(r_1) and Σ^past_(r_1) are spacelike ([[lem:iii-c1-1-1]]), with
Ω_(ext,r_1) to the past of the first and to the future of the second. For g_(b₀), dt_IVP is past timelike
([[lem:iii-b-3-7]] (b)), so Σ^IVP is spacelike, and {t_IVP = −ν} is spacelike (after [[prop:iii-k-1-2]]); on the
compact 𝒦 these persist for C⁰-close metrics. The points of 𝒦 with r ≥ r_1 and t_IVP < 0 lie below the past slab
{−(r − r_1)/12 ≤ t_IVP ≤ 0} of Ω_(ext,r_1), that is to the past of Σ^past_(r_1), and by (b) they have r < R_8. The
boundary that 𝒮 shares with Ω_(ext,r_1) ∪ 𝒦 lies in {ρ′_I = c} ∪ Σ^fut_(r_1), with 𝒮 to its future; so no past
directed causal curve enters 𝒮 from Ω_(ext,r_1) ∪ 𝒦. *Domains of dependence.* Let p ∈ 𝒦⁺, and let γ be a past directed
causal curve from p, past inextendible in 𝒟, for one of the metrics named. t_IVP decreases strictly along γ. γ cannot
leave 𝒦⁺ through {ρ′_I = c}, {t^♭_* = T̂ + 3} or {r = r_♭}, 𝒦 lying to their past; and it cannot stay in the compact
set 𝒦⁺, on which t_IVP is a time function: parametrised by t_IVP it would converge and extend, as in the proof of
[[lem:ii-f-1-3]]. So it meets Σ^IVP ∩ 𝒦 or Σ^fut_(r_1) ∩ {ρ′_I ≥ c}. Likewise a future directed causal curve from
p ∈ 𝒦⁻, along which t_IVP and t_IVP + ν increase, cannot leave 𝒦⁻ through {t_IVP = −ν}, and so meets Σ^IVP ∩ 𝒦 or
Σ^past_(r_1) ∩ 𝒟. (d) 𝒮 is disjoint from Ω_(ext,r_1) and lies near
infinity, so by (b) it lies in {t_IVP ≥ 0} ∖ Ω_(ext,r_1), above Σ^fut_(r_1); so x¹ ≥ C″ − r_1 − 2 as in (c), and
x¹ ≤ T″ − 1. ρ′_I < c ≤ ½ gives t > (1 − c)|x| + T″ ≥ ½|x| + T″, so t_IVP > ½|x| + T″ − C″ ≥ r/4, as r ≥ R_9 ≥ 4C″.
∎

The slab 𝒮 is bounded by {ρ′_I = c} ∪ Σ^fut_(r_1) to the past and by {t^♭_* = T̂ + 3} to the future. Its points near
ℐ⁺ depend on all of Σ^IVP, so it is solved after 𝒦, together with the exterior: [[sec:iv3-0]]–[[sec:iv3-2]].

#### The local theory on compact sets {#sec:s27-local}

On the compact pieces of 𝒟 (the set 𝒦, and the part of 𝒮 away from ℐ⁺ in the proof of [[thm:iv3-2-1]]) the equations are
solved by the local theory of quasilinear wave equations. The equation [[eq:iii-k-1-2]] is, in the gauge's normal form,
P^♮(g_0 + h, g_0) = ½□_(g_0+h)h plus a smooth function of (x, h, ∂h), with g_0 = φ_(S,S⁰)^*g_(b₀) and □ the operator of
[[eq:iii-b-6-7]]: its principal part is ½□_(g_0+h) ⊗ id = −½(g_0 + h)^(αβ)∂_α∂_β ⊗ id, with principal symbol
½(g_0 + h)⁻¹(ζ, ζ) times the identity (∂ → iζ), and everything is smooth in the parameters (S, S⁰); h = 0 solves it for
every value of the parameters, as P^♮(g_0, g_0) = Ric(g_0) = 0. Its linearisations have the same principal part at h.
[[lem:ii-f-1-3]] and [[lem:s26-uniqueness]] are applied below to twice these operators, and to twice the operators
δ_gG_gδ*_(g_0,E_C) of the constraint propagation, whose principal symbol is then g⁻¹(ζ, ζ) times the identity. Two
statements are used, on a compact set 𝒦′ that is the domain of dependence, within 𝒟, of the part of its boundary
carrying the data (a level set of t_IVP, with a forward and a backward problem, or a piecewise smooth spacelike past
boundary). On a domain, H^k denotes the restrictions of H^k functions, with the quotient norm.

(L) Let k ≥ 4. For a linear equation of this kind with smooth coefficients, data in H^(k+1) × H^k and forcing
f ∈ H^k(𝒦′), there is a unique solution h ∈ H²(𝒦′) on 𝒦′; it lies in H^(k+1)(𝒦′), and
‖h‖_(H^(k+1)(𝒦′)) ≤ C_k(‖h₀‖_(H^(k+1)) + ‖h₁‖_(H^k) + ‖f‖_(H^k(𝒦′))) for the data (h₀, h₁).

(N) (Cauchy stability) for the quasilinear equation, there is r_0 such that for data small in H^(r_0+1) × H^(r_0) and
(S, S⁰) small there is a unique solution on all of 𝒦′; it lies in H^(r+1)(𝒦′) for every r for which the data lie in
H^(r+1) × H^r, and it tends to 0 in H^(r+1)(𝒦′) as the data tend to 0 in H^(r+1) × H^r and (S, S⁰) tends to 0.

Both rest on [DS23, Theorems 2.4, 2.5 and 2.6] ([[thm:std-ds-existence]], [[thm:std-ds-stability]],
[[thm:std-ds-continuation]]). Data on a piecewise smooth past boundary are first made zero by subtracting an extension
of them, cut off near the boundary, as in [[rem:iv-4-2]]; the forcing problem is then posed with zero data on a level
set of t_IVP to the past of 𝒦′. dt_IVP is past timelike for g_(b₀) ([[lem:iii-b-3-7]] (b)), with a margin on a
neighbourhood of 𝒦′, hence for every metric C⁰-close to g_(b₀) there. As in Step 8 (ii)–(iii) of [[sec:ue-existence]],
the coefficients are extended from a neighbourhood of 𝒦′ to a spatial torus 𝕋⁴ with a cut-off of the values, the time
lines are taken orthogonal to the level sets of t_IVP, and the equation becomes a first-order symmetric hyperbolic
system ∂_tu + A^i(t, x, u)∂_iu = R(t, x, u) for u = (h, ∂h) satisfying (A1)–(A4) of [DS23], t = t_IVP; the data and
the forcing are extended to the torus by the definition of the spaces and cut off in the same way. The parameters
(S, S⁰) are adjoined as unknowns constant in t_IVP, which adds the eigenvalue 0 that the symbol already has. [DS23] asks
r > N/2 + 1 = 3 for u ∈ H^r, r an integer, so r ≥ 4, which for h means data in H^(r+1) × H^r; this is why (L) is
stated for k ≥ 4. Finite speed of propagation, [[lem:ii-f-1-3]] with the compact sets of [[lem:s27-cover]] (c) and
[[lem:iii-k-6-2]], shows that on 𝒦′ the solution depends only on the data on its past boundary and on the forcing on
𝒦′, not on the extensions; and that it is unique among solutions in H²(𝒦′), which, extended by 0 across the data
surface where their Cauchy data vanish, are solutions in the sense of distributions, as in the proof of
[[prop:iii-k-1-2]].

*(N).* [[thm:std-ds-existence]] at u₀ = 0, from a starting level t₀ of t_IVP, gives an interval [t₀ − T, t₀ + T] with
T > 0 depending on ‖u₀‖_r = 0 and on the structure only, so not on t₀, the bounds of (A1)–(A2) holding uniformly in
t_IVP. The solution 0 exists for all t_IVP and all parameters, and [[thm:std-ds-stability]] at it, on that interval,
shows that solutions with data near 0 at t₀ exist on [t₀ − T, t₀ + T] and tend to 0 in C([t₀ − T, t₀ + T]; H^r) as
the data tend to 0. Applied on successive intervals of length T, each time with the values of the solution at the end
of the previous one as data, finitely many to cover the t_IVP-range of 𝒦′ in both time directions, this gives (N) with
r_0 := 4, in C(I; H^r) for u; the higher regularity is [[thm:std-ds-continuation]], and the spacetime norm on 𝒦′
follows as in step (iv) below, the equation being solved for the second time derivative in the same way.

*(L).* For a linear equation, A^i = A^i(t, x) and R = B(t, x)u + F(t, x), with A^i, B smooth and bounded with all their
derivatives, and F the forcing; (A1)–(A4) hold on U = ℝ^m, so the distance M̃ of [[thm:std-ds-existence]] is infinite,
and solutions scale with their data. Let I be the t_IVP-range of 𝒦′, enlarged by 1, and r ≥ 4.

(i) *The homogeneous system* (F = 0). For σ ∈ ℝ, w(τ) := u(σ + τ) solves the system with coefficients A^i(σ + τ, x),
B(σ + τ, x); adjoin σ as an unknown constant in τ, as the parameters are. At the solution (0, σ₀),
[[thm:std-ds-existence]] gives an interval [−T(σ₀), T(σ₀)], and [[thm:std-ds-stability]] a δ(σ₀) > 0 such that data
(w₀, σ) with ‖w₀‖_r ≤ δ(σ₀) and |σ − σ₀| ≤ δ(σ₀) have solutions on that interval with ‖w(τ)‖_r ≤ 1. Covering I by
finitely many intervals (σ₀ − δ(σ₀), σ₀ + δ(σ₀)), and scaling, there are T₁ > 0 and K such that for every s ∈ I and
u₀ ∈ H^r the solution with u(s) = u₀ exists on [s − T₁, s + T₁] and satisfies ‖u(t)‖_r ≤ K‖u₀‖_r there. So the
solution operators 𝒰(t, s) exist for t, s ∈ I; they are linear, by uniqueness, satisfy 𝒰(t, s)𝒰(s, s′) = 𝒰(t, s′),
and are bounded on H^r by K^m, m the least integer ≥ |I|/T₁, uniformly in t, s ∈ I. By [[thm:std-ds-existence]],
t ↦ 𝒰(t, s)u₀ is continuous into H^r and C¹ into H^(r−1), with derivative 𝒜(t)𝒰(t, s)u₀, 𝒜(t) := −A^i∂_i + B; and
s ↦ 𝒰(t, s)u₀ is continuous into H^r, as 𝒰(t, s′)u₀ − 𝒰(t, s)u₀ = 𝒰(t, s′)(u₀ − 𝒰(s′, s)u₀) and the 𝒰(t, s′) are
uniformly bounded.

(ii) *Duhamel's formula.* Let u₀ and F be smooth, and u the solution of [[thm:std-ds-existence]] with u(t₀) = u₀,
t₀ ∈ I; R = Bu + F satisfies (A2). On an interval J ⊂ I on which u exists, u ∈ C(J; H^(r+1)) ∩ C¹(J; H^r) for every r.
For fixed t, w(s) := 𝒰(t, s)u(s) satisfies w(s + ε) − w(s) = 𝒰(t, s + ε)(u(s + ε) − 𝒰(s + ε, s)u(s)), and in H^r
the bracket is εF(s) + o(ε), u and 𝒰(·, s)u(s) being C¹ into H^r with derivatives at s differing by F(s). With the
uniform bound and the continuity in s of (i), w has the continuous right derivative 𝒰(t, s)F(s) in H^r; a continuous
function with a continuous right derivative is continuously differentiable, so
u(t) = 𝒰(t, t₀)u₀ + ∫_(t₀)^t 𝒰(t, s)F(s) ds, and ‖u(t)‖_r ≤ K^m(‖u₀‖_r + ∫_I ‖F(s)‖_r ds) on J. This bounds u in
C(J; C¹) ∩ C¹(J; C), H^r lying in C¹ for r ≥ 4, so by [[thm:std-ds-continuation]] u exists on all of I.

(iii) *Density.* For u₀ ∈ H^r and F ∈ L¹(I; H^r), approximate by smooth ones. By (ii) the solutions converge in
C(I; H^r), and the limit solves the system in the sense of distributions, with the same bound.

(iv) *The spacetime norm.* With r := k, u ∈ C(I; H^k) gives h ∈ C(I; H^(k+1)) and ∂_(t_IVP)h ∈ C(I; H^k). The
derivatives of h with j ≥ 2 derivatives along the time lines follow from the equation, solved for the second time
derivative (its coefficient does not vanish, the level sets of t_IVP being spacelike), by induction on j: each is a
combination, with smooth coefficients, of derivatives of h with at most j − 1 time derivatives and of j − 2 derivatives
of f. So h ∈ H^(k+1) of the slab I × 𝕋⁴, with norm at most C_k(‖h₀‖_(H^(k+1)) + ‖h₁‖_(H^k) + ‖f‖_(H^k)), f ∈ H^k of
the slab lying in L¹(I; H^k); its restriction to 𝒦′ gives (L). [Hin26, p. 320] cites the same theory as "standard
local well-posedness results".

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

**Lemma {#lem:iv3-0-1}** (The background on the slab.) Let S, S⁰ ∈ 𝒮_1 be small as in [[lem:iii-b-5-2]] and
[[lem:s27-translated-exterior]]. On a neighbourhood of 𝒮̄ in U″, φ_(S,S⁰)^*g_(b₀) agrees with an element of 𝒢″; on
Ω_(ext,r_1) it is the background of [[lem:iii-c2-1-1]] for φ_(S,S⁰) ([[lem:s27-translated-exterior]] (c)).

*Proof.* On 𝒮, χ_IVP = 1, as t_IVP ≥ 0 > −|x|/10 ([[sec:iii-b-5]]). And χ_K = 0 on 𝒮: supp χ_K lies in the interior
of {χ^♯_K = 1} ⊂ supp χ^♯_K ⊂ {|x| < t/2}, while on 𝒮, t^♭_* ≤ T̂ + 3 gives t_* ≤ (T̂ + 3)/C_♭ and so x¹ ≤ T″ − 1,
so t ≤ |x| + T″ < 2|x| near infinity, where 𝒮 lies. So [[lem:s27-translated-exterior]] (b) gives near 𝒮̄

    φ_(S,S⁰)^*g_(b₀) − g_(b₀) − |x|⁻² 𝔥_S(ω)(dx¹)² ∈ ρ₀²ρ_I³ρ_+² C^∞(M; S²T*),

with 𝔥_S the function h_(S_w) of [[eq:iii-b-5-2]]; and g_(b₀) − η = m₀|x|⁻²(dx¹)² + |x|⁻³C^∞ on {|x| ≥ 3R₁}
([[lem:iii-c-3-5]] (1) and its proof). On 𝒮, ρ₀, ρ′_0 and ρ_+ are bounded below and ρ_I/ρ′_I is smooth and positive,
so φ_(S,S⁰)^*g_(b₀) − η ∈ (ρ′_0)²(ρ′_I)²C^∞ with only the slot π₁₁ at that order, (dx¹)² being of type π₁₁, and the
other slots in (ρ′_0)²(ρ′_I)³C^∞: this is [[eq:iii-c-3-4]] in the translated chart, and φ_(S,S⁰)^*g_(b₀) is smooth on
M. On Ω_(ext,r_1) the statement is [[lem:s27-translated-exterior]] (c). ∎

#### The curves on Ω^♮ {#sec:iv3-1}

**Lemma {#lem:iv3-1-1}** Let c_♮ ∈ (0, c/4] and r_ext large. (a) {ρ′_I = c_♮} = {t = (1 − c_♮)|x| + T″} is spacelike
near infinity, with {ρ′_I < c_♮} to its future. (b) For p ∈ Ω^♮ with ρ′_I(p) < c_♮, the integral curves of
X′_I := ρ′_I∂_(ρ′_I) and of X′_0 − X′_I through p (the outgoing ray at fixed x¹, and the curve of fixed |x|), followed
in the direction of increasing ρ′_I, stay in Ω^♮ until they reach {ρ′_I = c_♮}, which they do. (c)
Ω^♮ ∩ {ρ′_I < c_♮} does not meet 𝒦, and Σ_c lies in {ρ′_I = c}.

*Proof.* (a) is [[lem:iv2-1-1]] (a) in the translated chart. (b) Near infinity, Ω^♮ ∩ {ρ′_I < c} is the set
{ρ′_I < c, t_IVP ≥ 0, t^♭_* ≤ T̂ + 3}: below Σ^fut_(r_1) it is Ω_(ext,r_1), above it 𝒮. So it suffices that along the
segment ρ′_I stays below c and t_IVP ≥ 0 and t^♭_* ≤ T̂ + 3 persist. *The ray.* Along it x¹ = x¹_p, and |x| decreases
to r_c := (T″ − x¹_p)/c_♮, where ρ′_I = c_♮ < c. t_* = x¹ + C′ − 8m₀|x|⁻¹ decreases along it. So does t^♭_*, along
this curve and the next: both are past directed causal for g_(b₀) (the ray is g_(b₀)-null, as
g_(b₀) = η + m₀|x|⁻²(dx¹)² there, [[lem:iii-b-3-5]] (b)), and dt^♭_* is past timelike for g_(b₀) ([[lem:ii-c-3-2]]
(2)). t_IVP = x¹ + |x| − C″ decreases too, and at r_c it is x¹_p(1 − c_♮⁻¹) + T″c_♮⁻¹ − C″, which is
≥ |x¹_p|(c_♮⁻¹ − 1) + T″c_♮⁻¹ − C″ > 0 if x¹_p < 0, and ≥ T″ − 1 + c_♮⁻¹ − C″ > 0 if x¹_p ∈ [0, T″ − 1], for c_♮ small;
and r_c = (T″ − x¹_p)/c_♮ ≥ 1/c_♮ ≥ 4/c ≥ 4R_9, as T″ − x¹ ≥ 1 on 𝒟 and c ≤ 1/R_9, so the ray stays in {r ≥ R_9}.
*The curve of fixed |x|.* t decreases to t_c := (1 − c_♮)|x| + T″; t_* decreases; the curve may cross Σ^fut_(r_1) into
Ω_(ext,r_1); t_IVP(t_c) ≥ ½|x| + T″ − C″ > 0; and ρ′_I < c_♮ along it, so it avoids 𝒦. (c) is the definition of 𝒮
and 𝒦 ⊂ 𝒟 ∖ 𝒮. ∎

So [[lem:iv2-1-2]] holds on Ω^♮_(c_♮) := Ω^♮ ∩ {ρ′_I < c_♮}, in the translated chart, with the same proof, with
ℐ⁺_c of [[lem:iv2-1-2]] (b) and of [[eq:iv2-0-3]] replaced by ℐ⁺_♮, the image of Ω^♮ ∩ {ρ′_I < c} under
(ρ′_0, ρ′_I, ω) ↦ (ρ′_0, ω): a domain of ℐ⁺ containing ℐ⁺ ∩ cl Ω^♮, and in general larger. Near ℐ⁺, Ω^♮ ends at the
future boundary {t^♭_* = T̂ + 3}, and t^♭_* = t_*(1 − ρ_I^(1/2)) increases along an X′_I-curve at fixed x¹ towards ℐ⁺;
so the curves through points with t^♭_* < T̂ + 3 < t_* leave Ω^♮ before they reach ℐ⁺, at points of ℐ⁺ with
t_* > T̂ + 3. The classes on Ω^♮ below are taken accordingly: in H^(k,α_0,(−,ℓ^♭_I))_b(Ω^♮), which is [[eq:iv2-0-3]] in
terms of u, in the translated chart and with χ_I := χ̂(ρ′_I), the radiation field is a function on ℐ⁺_♮, and in the
classes of [[cor:iv3-2-3]] so are the coefficients of the expansion at ℐ⁺.

#### The solution on Ω^♮ {#sec:iv3-2}

**Theorem {#thm:iv3-2-1}** (The linear estimate on Ω^♮.) Let g_0 := φ_(S,S⁰)^*g_(b₀) with |S| + |S⁰| small, or
g_0 := g_(b₀); h small in H^(8,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω^♮) (weights at ℐ⁺ in ρ′_I); L := L^(χ^♮_0)_(g_0+h,g_0);
α_0 > ℓ^♭_I, k ∈ ℕ with k ≥ 1, and d := 4. For f ∈ H^(k+d,α_0+2,(−′,ℓ^♭_I+1))_b(Ω^♮), data ġ_0, ġ_1 ∈ H^(k+d,α_0)_b(Σ^IVP_(r_1)) and data
k̇_0, k̇_1 ∈ H^(k+d)(Σ_c), there is a unique ġ ∈ H^(k,α_0,(−,ℓ^♭_I))_b(Ω^♮) with Lġ = f, ġ = ġ_0 and
r ℒ_(∂_(t_IVP))ġ = ġ_1 on Σ^IVP_(r_1), and the Cauchy data (k̇_0, k̇_1) on Σ_c; and [[eq:iv2-2-3]] holds with
‖k̇_0‖_(H^(k+d)) + ‖k̇_1‖_(H^(k+d)) added to N(f, ġ_0, ġ_1; k + d) and their H⁸-norms added to N(f, ġ_0, ġ_1; 8).

*Proof.* As [[thm:iv2-2-4]], with three changes. *The gauge.* On Ω_(ext,r_1), χ^♮_0 = χ_0 ([[lem:iii-k-1-1]] (c));
on 𝒮, χ^♮_0 = 1 = χ_0, as t_IVP ≥ r/4 there ([[lem:s27-cover]] (d)); so L = L^(χ_0) on Ω^♮, and [[cor:iv2-4-1]]
applies, χ_0 = 1 on Ω^♮_(c_♮) (ρ′_I < c_♮ gives t_IVP ≥ r/4). *The background.* g_0 ∈ 𝒢″ near 𝒮̄ by
[[lem:iv3-0-1]], and in the class of [[lem:iii-c2-1-1]] on Ω_(ext,r_1) ([[lem:s27-translated-exterior]] (c)); it is
Ricci flat. *The regions.* Fix
c_♮ ≤ c/4 so small that [[prop:iv1-2-2]] holds on Ω^♮_(c_♮) with Σ_in := {ρ′_I = c_♮} ∩ Ω^♮ and
Σ_fin := {t^♭_* = T̂ + 3} ∩ Ω^♮_(c_♮), which is spacelike for g_0 + h, dt^♭_* being past timelike for every g_(b₀) + h′
with h′ small in 𝒢̃^(0,(1,0,0))_(e3b) ([[lem:ii-c-3-2]] (2)); every X′_I-curve there begins on Σ_in
([[lem:iv3-1-1]] (b)). Then:

(i) On Ω_N (near the interior of I₀, with the past slab), [[lem:iv2-2-2]] with the data on Σ^IVP_(r_1), unchanged.

(ii) On Ω^♮ ∩ {ρ′_I ≥ c_♮/4} ∩ {τ′ ≥ 1/16}, away from ℐ⁺ (τ′ = t_IVP/|x| as in [[sec:iv2-0]]): its part in
Ω_(ext,r_1) by the first step of [[lem:iv2-2-3]] ([[prop:iv-4-1]] for the system near the interior of I₀, and standard
energy estimates on the compact part); then its part in 𝒮, which is compact (|x| ≤ 4(T″ − x¹)/c_♮, x¹ bounded), by the
energy estimate for the Cauchy problem of a linear wave equation on a compact domain of dependence, with data on Σ_c
(given) and on Σ^fut_(r_1) ∩ {c_♮/4 ≤ ρ′_I < c} (from the part in Ω_(ext,r_1)), both spacelike and compact: this is
(L) of [[sec:s27-local]] at the order k + 3, which is at least 4 as k ≥ 1: the data on Σ_c lie in H^(k+4) × H^(k+3)
and the forcing in H^(k+3), and the solution lies in H^(k+4) there, the order the next step uses. Its
boundary to the future, {ρ′_I = c_♮/4}, {t^♭_* = T̂ + 3} and Σ^fut_(r_1) ∩ {ρ′_I ≥ c} (where Ω^♮ borders 𝒦), is
spacelike, so the region is closed under past causal curves within Ω^♮, and [[lem:ii-f-1-3]] gives uniqueness.

(iii) On Ω^♮_(c_♮), the second step of [[lem:iv2-2-3]] and the steps of the proof of [[thm:iv2-2-4]] near ℐ⁺, with
c_♮ in place of c: the cut-off χ̂_(c_♮)(ρ′_I), [[prop:iv1-2-2]], and the two integrations of [[lem:iv2-1-2]] along the
curves of [[lem:iv3-1-1]]. Nothing in these steps uses ρ′_0 beyond its role as a coordinate; on 𝒮 it is bounded
below, where the weight at I₀ is immaterial.

The forcing of each step vanishes near its initial surface after the cut-offs of the proof of [[thm:iv2-2-4]] and of
[[lem:iv2-2-3]], and the estimates compose as there; the data on Σ_c enter through (ii) only, at the order of
H^(k+4). Uniqueness: [[lem:ii-f-1-3]] on each region. The case k = 0 is not needed: [[thm:iv3-2-2]] uses the estimate
for k ≥ d only, as [[eq:ii-g-2-4]] asks, and a bound in H^(0,α_0,(−,ℓ^♭_I))_b follows from the case k = 1. ∎

**Theorem {#thm:iv3-2-2}** (The nonlinear solution on Ω^♮; [Hin26, p. 321].) Let g_0 be as in [[thm:iv3-2-1]],
(h_0, h_1) data on Σ^IVP_(r_1) as in [[thm:iv2-3-1]], and (k_0, k_1) the Cauchy data on Σ_c of a solution of
P^♮(g_0 + h, g_0) = 0 on a neighbourhood of Σ_c in 𝒦 ∪ Ω_(ext,r_1) that agrees on Ω_(ext,r_1) with the solution of
[[thm:iv2-3-1]]. Let d := 7 and N_ex := 21d + 6 = 153, the regularity of [[thm:ii-g-2-1]] for this d. There is
ε_0 > 0 such that, if ‖h_j‖_(H^(N_ex,ℓ^♭_0)_b) + ‖k_j‖_(H^(N_ex)(Σ_c)) < ε_0, there is a unique
h ∈ H^(∞,ℓ^♭_0,(−,ℓ^♭_I))_b(Ω^♮), small in H^(3d), with P^♮(g_0 + h, g_0) = 0 and these data, and it equals the solution
of [[thm:iv2-3-1]] on Ω_(ext,r_1); and for every k and ε > 0 there is ε_1 ∈ (0, ε_0] such that
‖h_j‖_(H^(N_ex+k,ℓ^♭_0)_b) + ‖k_j‖_(H^(N_ex+k)(Σ_c)) < ε_1 gives ‖h‖_(H^(3d+k,ℓ^♭_0,(−,ℓ^♭_I))_b) < ε.

*Proof.* The proof of [[thm:iv2-3-1]] on Ω^♮, with the spaces F^k of right sides enlarged by H^k(Σ_c)² and the map by
the traces on Σ_c minus (k_0, k_1); the right inverses are those of [[thm:iv3-2-1]], and the smoothing and the map are
as there (the smoothing of the radiation field built on ℐ⁺_♮; P^♮ = P^(χ_0) on Ω^♮, and [[cor:iii-c-5-3]] holds for it
by [[lem:iii-c2-2-1]], near 𝒮 in the translated chart). The data enter the map: ‖Φ(h)‖_k ≤ C′_k(1 + |h|_(k+d)) + Σ_j(‖h_j‖_(H^(k,ℓ^♭_0)_b) + ‖k_j‖_(H^k(Σ_c))),
with C′_k independent of the data, so for k ≤ N_ex the constants C_k of [[eq:ii-g-2-3]] are bounded independently of
the data once these norms are at most 1 in H^(N_ex). The threshold of [[thm:ii-g-2-1]] depends on the constants up to
the order N_ex only, so it is then uniform, and ‖Φ(0)‖_(2d) is below it for data small in H^(N_ex); the shifted scales
of the proof of [[thm:iv2-3-1]] give the higher norms in the same way, with N_ex + k in place of N_ex. Ω_(ext,r_1) is
closed under past causal curves within Ω^♮, and its past boundary is
Σ^IVP_(r_1) ∪ Σ^past_(r_1); so on it the solution depends on (h_0, h_1) only, and it is the solution of
[[thm:iv2-3-1]] by uniqueness there. ∎

So the solution of [[prop:iii-k-1-2]] on 𝒮 is the restriction of that of [[thm:iv3-2-2]], with (k_0, k_1) from the
compact part (whose data on Σ^fut_(r_1) ∩ {ρ′_I ≥ c} come from the exterior); the three solutions agree on overlaps by
[[lem:ii-f-1-3]] with the compact sets of [[lem:iii-k-6-2]].

**Corollary {#cor:iv3-2-3}** (The orders on the slab.) Under the hypotheses of [[thm:iii-c1-3-1]] on the data, the
solution of [[thm:iv3-2-2]] lies in H^(∞,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b(Ω^♮), with the bound [[eq:iii-c1-3-2]], the
coefficients of its expansion at ℐ⁺ being functions on ℐ⁺_♮ ([[sec:iv3-1]]); in particular h_(S,S⁰) has the orders
(⟨ℰ^C_I⟩, ℓ_I) at ℐ⁺ on 𝒮, as [[prop:iii-k-1-2]] (3) states.

*Proof.* The proof of [[thm:iii-c1-3-1]] on Ω^♮, with [[thm:iv3-2-1]] in place of the linear estimate
[[eq:iii-c1-2-2]]. Its Step 1 works at I₀, which Ω^♮ meets only within Ω_(ext,r_1); its Step 2 integrates, slot by
slot, along X_I and X_0 − X_I near ℐ⁺ ([[lem:iii-a-1-2]], [[lem:iii-a-3-2]]), and on Ω^♮_(c_♮) the curves followed
backward reach {ρ′_I = c_♮}, where the solution is smooth ([[lem:iv3-1-1]] (b)); away from ℐ⁺ there is nothing to show.
The structure [[eq:iii-c-4-4]] used there holds near 𝒮 by [[lem:iv3-0-1]] and the translation. ∎

#### Past causal curves near null infinity and near spatial infinity {#sec:iii-k-6}

The uniqueness lemma [[lem:ii-f-1-3]] asks, at each point p, for a compact set containing the part of the causal past of
p above a level of the time function. Near ℐ⁺ the levels of t^♭_* reach r = ∞, and near I₀ those of t_IVP do; so these
sets need a bound on r along past causal curves. [[lem:ii-f-1-4]] (a) bounds r by t_* + R̃(r), a time function of
g_(b₀) and of the combinations G_θ only: for h small in the class of [[lem:ii-c-3-2]], dt, and with it d(t_* + R̃), can
be spacelike near ℐ⁺, as (g_(b₀)⁻¹ − η⁻¹)(dt, dt) = O(r⁻²) there while a perturbation of that class is larger. The next
two lemmas give the bounds for every metric of the classes used.

**Lemma {#lem:s27-below}** (The time function below Ω_*.) Let ℓ = ½, and let ε_G, C_♭, r′_0, r^♮ and t^♭_* be those of
[[lem:ii-c-3-2]] for g_0 = g_(b₀), built with the gluing constant C_g ≥ max(4(r′_0 + 1), 32, 16R₁) fixed at the start
of the chapter, with t^♭_* given on {t_* > 0} by the formulae of its proof ([[lem:ii-e-1-2]] (iv)).
Let Ω_(1/2) := cl_M{t_* ≥ ½}, with interior Ω°_(1/2), and let 𝒢̃_(1/2) be the class 𝒢̃^(0,(2ℓ,0,0))_(e3b) of
[[def:ii-c-3-1]] with Ω_(1/2) in place of Ω, with its norm. There are ε′_G ∈ (0, ε_G], C₁ and R_V such that for every
g = g_(b₀) + h with ‖h‖_(𝒢̃_(1/2)) < ε′_G:

(i) near ℐ⁺ on Ω_(1/2), with ρ := ρ_I = t_*/r, the coefficients of g⁻¹ − g_(b₀)⁻¹ in the basis

    ρ∂²_(t_*),   ∂_(t_*) ⊗_s ∂_r,   x_I∂_(t_*) ⊗_s r⁻¹∂_ω,   ρ⁻¹∂²_r,   x_I⁻¹∂_r ⊗_s r⁻¹∂_ω,   r⁻¹∂_ω ⊗_s r⁻¹∂_ω

of the proof of [[lem:ii-c-3-2]] are at most C₁ε′_Gρ^ℓ, and those of g⁻¹ − ḡ⁻¹ at most C₁(ε′_G + ρ^(1−ℓ))ρ^ℓ;

(ii) V := t∂_t + r∂_r is future timelike for g on Ω_(1/2) ∩ {r ≥ R_V};

(iii) dt^♭_* is past timelike for g on Ω°_(1/2), so t^♭_* is a time function of g there, and dt^♭_*(V) > 0 on
Ω°_(1/2) ∩ {r ≥ R_V};

(iv) dr is future timelike for g on Ω_(1/2) ∩ {r_♭ ≤ r ≤ r^♮}.

The statements are pointwise, so they hold as well for h given only on an open subset of Ω_(1/2), and small there in
that norm, on that subset.

*Proof.* On Ω_(1/2) ∩ {t_* ≥ 1} ⊂ Ω (Ω = cl_M{t_* ≥ 1}, [[def:ii-a-1-3]]) the statements are [[lem:ii-c-3-2]] and its
proof, the norm of h on Ω being at most its norm on Ω_(1/2). The proof of [[lem:ii-c-3-2]] is pointwise, and it is run
on Ω_(1/2) ∩ {t_* ≤ 1} as follows.

(i) The proof of [[lem:ii-c-3-2]] bounds the coefficients of g⁻¹ − g_(b₀)⁻¹ by C‖h‖ρ^ℓ and those of g_(b₀)⁻¹ − ḡ⁻¹
by Cρ, times powers of ρ_+, and uses ρ_+ ≤ 1 on Ω only to bound these powers. On Ω_(1/2), ρ_+ ≤ 2, as in the proof of
[[lem:ii-e-1-2]] (iv) (near ℐ⁺ ∩ ι⁺, ρ_+ = 1/t_*); so both bounds hold with a larger C₁. That proof uses them on
{ρ_I ≤ ρ_a}, ρ_a its constant, with 2/C_g ≤ ρ_a; they hold on the same set here.

(ii) As in the proof of [[lem:ii-c-3-2]] and in [[sec:ii-b-7]]: ḡ(V, V) = −t_*² − 2t_*r, and by (K1)
|g_(b₀)(V, V) − ḡ(V, V)| ≤ C₂r⁻²(t_* + r)². For t_* ≥ ½ this is at most ½(t_*² + 2t_*r) once r ≥ 8C₂ and
r² ≥ 8C₂: if t_* ≤ r, the left side is at most 4C₂ and the right side at least t_*r ≥ r/2; if t_* > r, the left side is
at most 4C₂t_*²r⁻² and the right side at least ½t_*². Take R_V ≥ R₂ with R_V ≥ 8C₂ and R_V² ≥ 8C₂. The bound
|h(V, V)| ≤ Cε′_G|g_(b₀)(V, V)| of that proof uses, near ℐ⁺, the bound of (i), and where x_I ≥ c_V the membership of
h in its frames, both valid on Ω_(1/2); so V is timelike for g on Ω_(1/2) ∩ {r ≥ R_V} once ε′_G is small. It is future
directed for g_(b₀), as there, and so for g, the orientation being continuous along g_(b₀) + sh, s ∈ [0, 1].

(iii) Where t^♭_* = t_*F₁(ρ), dt^♭_* = d(t_*F₁) = A dt_* + B dr with A = 1 − (1 + ℓ)ρ^ℓ and B = ℓρ^(ℓ+1), as in the
proof of [[lem:ii-c-3-2]].

*The background near ℐ⁺.* Let Y := Ω_(1/2) ∩ {ρ_I ≤ 2/C_g}. On Y, ρ ≤ 2/C_g ≤ 1/16, so ρ^ℓ ≤ ¼, A ∈ [5/8, 1] and
0 < B ≤ ½ρ^(3/2) ≤ 1/128; and r = t_*/ρ ≥ C_g/4 ≥ max(r′_0 + 1, 4R₁), as t_* ≥ ½. So t^♭_* = t_*F(ρ) on Y, and the
exact forms of g_(b₀) and t_* on {r ≥ 3R₁} apply: in the coordinates (t, x) of [[sec:iii-b-2]] (t is not the t_* + r
of [[lem:ii-c-3-2]]), g_(b₀)⁻¹ = η⁻¹ − u(∂_t + ∂_r)^(⊗2) with u := m₀r⁻² ([[prop:iii-b-3-6]]), and
dt_* = dt − (1 − 8u)dr ([[eq:iii-b-3-6]]), so (∂_t + ∂_r)t_* = 8u and

    g_(b₀)⁻¹(dt_*, dt_*) = −16u(1 − 2u)²,     g_(b₀)⁻¹(dt_*, dr) = −1 + 8u(1 − u),     g_(b₀)⁻¹(dr, dr) = 1 − u.

On Y, u ≤ 1/16, so the first is ≤ 0, the second ≤ −½ and the third ≤ 1. As A, B > 0,

    g_(b₀)⁻¹(d(t_*F₁), d(t_*F₁)) ≤ 2AB(−½) + B² = −B(A − B) ≤ −½B = −½ℓρ^(ℓ+1)     on Y,

at every t_* ≥ ½: the correction to ḡ⁻¹ that carries no factor B, the A²-term, has the sign of the main term. Also
g_(b₀)⁻¹(d(t_*F₁), dt_*) = A g_(b₀)⁻¹(dt_*, dt_*) + B g_(b₀)⁻¹(dt_*, dr) < 0, and dt_* is past timelike for g_(b₀)
([[lem:ii-b-1-1]]); two timelike covectors with negative product lie in the same cone, so d(t_*F₁) is past timelike
for g_(b₀) on Y.

*The perturbation near ℐ⁺.* On Y ∩ {ρ_I ≤ ρ_−}, where dt^♭_* = d(t_*F₁) (ρ_− < 1/C_g, and r ≥ r′_0 + 1 there), the
coefficients of g⁻¹ − g_(b₀)⁻¹ in the basis of (i) are at most C₁ε′_Gρ^ℓ, and the six basis elements take on
α ⊗ α, α := dt^♭_*, the values ρA², at most 2AB in modulus, 0, ρ⁻¹B², 0 and 0, each at most ρ (2AB ≤ ρ^(3/2) and
ρ⁻¹B² = ¼ρ²). So |(g⁻¹ − g_(b₀)⁻¹)(α, α)| ≤ 3C₁ε′_Gρ^(ℓ+1) = 6C₁ε′_G B, and g⁻¹(α, α) ≤ −¼ℓρ^(ℓ+1) once
ε′_G ≤ 1/(24C₁). The same holds for g_(b₀) + sh, s ∈ [0, 1], so α is timelike for each of these metrics; it is past
timelike for g_(b₀), so it stays in the past cone along the path, which is the time orientation of g (as in (ii)).
So dt^♭_* is past timelike for g on Ω°_(1/2) ∩ {ρ_I ≤ ρ_−}.

*The rest.* The rest of Ω_(1/2) ∩ {t_* ≤ 1} is K := {½ ≤ t_* ≤ 1, ρ_I ≥ ρ_−} ∩ Ω_(1/2), which is compact (r ≤ t_*/ρ_−
there). On K, dt^♭_* is past timelike for g_(b₀). Indeed, by the formulae of the proof of [[lem:ii-c-3-2]], which cover
{t_* ≥ ½} as C_g ≥ 4(r′_0 + 1) ([[lem:ii-e-1-2]] (iv)), and with t := t_* + r there, dt^♭_* is C_♭dt_* on
{r ≤ r′_0 − 1}, a positive combination of dt_* and dt on {r ≤ C_g t_*/2}, and, on {r ≥ r′_0 + 1}, d(t_*F₁) where
ρ_I ≤ ρ_−, C_♭dt where ρ_I ≥ ρ⁺, and a positive combination of d(t_*F₁) and dt on [ρ_−, ρ⁺]. dt_* is past timelike for
g_(b₀) everywhere ([[lem:ii-b-1-1]]), and dt on {r ≥ r′_0 − 1} (g_(b₀)⁻¹(dt, dt) ≤ −1 + C₂r⁻² < 0 there, and
g_(b₀)⁻¹(dt, dt_*) = −1 + O(r⁻²) < 0 with dt_* past timelike, [[lem:ii-b-1-1]]); these two are statements at a point
that do not involve t_*, dt_*, dt and g_(b₀) being stationary. d(t_*F₁) is past timelike for g_(b₀) on
Ω_(1/2) ∩ {ρ_I ≤ ρ⁺} ⊂ Y, by the first step, as ρ⁺ < 2/C_g. The past cone being convex, dt^♭_* is past timelike for
g_(b₀) at every point of K. By compactness, g_(b₀)⁻¹(dt^♭_*, dt^♭_*) ≤ −c_K < 0 on K, and, the norm bounding h in C⁰ on
K, g_s⁻¹(dt^♭_*, dt^♭_*) ≤ −½c_K for g_s := g_(b₀) + sh, s ∈ [0, 1], once ε′_G is small; as before dt^♭_* is past
timelike for g on K. Where dt^♭_* is past timelike and V is future timelike, dt^♭_*(V) > 0.

(iv) g_(b₀)⁻¹(dr, dr) ≤ −c_r < 0 on {r_♭ ≤ r ≤ r^♮} by (H4) and compactness of this range of r, at every t_*, as g_(b₀)
is stationary; dr is future timelike for g_(b₀) there, as in the proof of [[lem:ii-c-3-2]] (1), and on
Ω_(1/2) ∩ {t_* ≤ 1, r_♭ ≤ r ≤ r^♮}, a compact set, the perturbation is O(ε′_G). ∎

**Lemma {#lem:iii-k-6-1}** (The radius near ℐ⁺ along past causal curves.) Let ℓ = ½, ε′_G, C₁, R_V, r′_0, r^♮,
t^♭_*, Ω_(1/2) and 𝒢̃_(1/2) be those of [[lem:s27-below]], C_♭ the constant of [[lem:ii-c-3-2]] (b), and T ≥ ½; put
T_1 := T/C_♭ + 1. There is R_T < ∞, depending only on T and on the constants of [[lem:ii-c-3-2]], [[lem:s27-below]]
and their proofs, such that for every g = g_(b₀) + h with ‖h‖_(𝒢̃_(1/2)) < ε′_G:

(a) on W_T := Ω°_(1/2) ∩ {t_* < T_1, r > R_T} the covector α := dt^♭_* + r⁻¹dr is past timelike for g, so
Ξ := t^♭_* + log r is a time function on W_T;

(b) if ½ < c < t^♭_*(p) ≤ T and γ is a past directed causal curve of g in Ω°_(1/2) from p along which t^♭_* ≥ c,
then r ≤ R_p := max(R_T, r(p)) e^(t^♭_*(p)−c) on γ;

(c) if moreover X ⊂ Ω°_(1/2) is open and contains L_p := {c ≤ t^♭_* ≤ t^♭_*(p), min(r(p), r^♮) ≤ r ≤ R_p}, then
L_p is compact and contains J⁻_X(p) ∩ {t^♭_* ≥ c}. These are the compact sets [[lem:ii-f-1-3]] asks for, with
τ := t^♭_*.

The proof is pointwise along the curves, so (a)–(c) hold as well for h given and small in that norm on an open
Y ⊂ Ω°_(1/2) only, with W_T ∩ Y in (a) and the curves and X in Y in (b)–(c).

*Proof.* (a) By [[lem:s27-below]] (i), near ℐ⁺ and with ρ := ρ_I = t_*/r, the coefficients of g⁻¹ − ḡ⁻¹ in the basis
displayed there are at most C₁(ε′_G + ρ^(1−ℓ))ρ^ℓ ≤ Cρ^ℓ for ρ ≤ 1, with C := max(1, C₁(ε′_G + 1));
ḡ⁻¹(dt_*, dt_*) = 0, ḡ⁻¹(dt_*, dr) = −1 and ḡ⁻¹(dr, dr) = 1; on {ρ ≤ ρ_−, r ≥ r′_0 + 1}, t^♭_* = t_*F₁(ρ) and
dt^♭_* = A dt_* + B dr with A = 1 − (1 + ℓ)ρ^ℓ and B = ℓρ^(ℓ+1) (the coefficients of the proof of [[lem:ii-c-3-2]]);
and V := t∂_t + r∂_r is future timelike for g on {r ≥ R_V}, with dt^♭_*(V) > 0 ([[lem:s27-below]] (ii)–(iii)). Let
x := ρ^ℓ, so ρ ≤ x ≤ 1 for ρ ≤ 1, and

    ρ_T := min(ρ_−, (37CT_1)^(−1/ℓ)),     R_T := max(R_V, r′_0 + 1, T_1/ρ_T).

On W_T, ρ < T_1/R_T ≤ ρ_T, so all of this applies, and x ≤ (37CT_1)⁻¹ ≤ 1/37. Then α = A dt_* + B′dr with
B′ := B + r⁻¹. As (1 + ℓ)x ≤ 3/74, A ∈ [½, 1]. As t_* ∈ (½, T_1) on W_T, r⁻¹ = ρ/t_* ∈ [ρ/T_1, 2ρ], and
B = ℓxρ ≤ ½ρ, so B′ ∈ [r⁻¹, (5/2)ρ]. The six basis elements take on α ⊗ α the values ρA², at most 2AB′ in modulus
(AB′ ≥ 0), 0, ρ⁻¹B′², 0 and 0. Hence

    g⁻¹(α, α) ≤ ḡ⁻¹(α, α) + Cx(ρA² + 2AB′ + ρ⁻¹B′²) = −2AB′ + B′² + Cx(ρA² + 2AB′ + ρ⁻¹B′²).

Each term is bounded as follows. −2AB′ ≤ −2A r⁻¹ ≤ −r⁻¹, as B′ ≥ r⁻¹ and A ≥ ½. B′² ≤ (25/4)ρ². And
ρA² + 2AB′ + ρ⁻¹B′² ≤ ρ + 5ρ + (25/4)ρ = (49/4)ρ. So

    g⁻¹(α, α) ≤ −r⁻¹ + (25/4)ρ² + (49/4)Cxρ ≤ −r⁻¹ + ((25/4) + (49/4)C)xρ ≤ −r⁻¹ + (37/2)Cxρ,

using ρ ≤ x and C ≥ 1. Finally ρ ≤ T_1 r⁻¹ (as r⁻¹ ≥ ρ/T_1), so

    g⁻¹(α, α) ≤ r⁻¹(−1 + (37/2)CT_1x) ≤ r⁻¹(−1 + ½) = −1/(2r).

So α is timelike, and α(V) = dt^♭_*(V) + 1 > 0, as dr(V) = r: a timelike covector positive on a future timelike vector
is past timelike. So Ξ, with dΞ = α, is a time function on W_T.

(b) t^♭_* is a time function of g on Ω°_(1/2) ([[lem:s27-below]] (iii)), so along γ, c ≤ t^♭_* ≤ t^♭_*(p) ≤ T, and
½ < t_* ≤ t^♭_*/C_♭ < T_1 ([[lem:ii-c-3-2]] (b)). Let R′_p := max(R_T, r(p)), suppose that r > R_p at γ(s_1), and let
s_0 := sup{s ≤ s_1 : r(γ(s)) ≤ R′_p}, which exists as r(γ(0)) = r(p). On (s_0, s_1], r > R′_p ≥ R_T, so γ lies in W_T
there and Ξ ∘ γ is non-increasing (dΞ = α is negative on past causal vectors); by continuity Ξ(γ(s_1)) ≤ Ξ(γ(s_0)),
and r(γ(s_0)) = R′_p. Hence log r(γ(s_1)) ≤ log R′_p + t^♭_*(γ(s_0)) − t^♭_*(γ(s_1)) ≤ log R′_p + t^♭_*(p) − c, that
is r(γ(s_1)) ≤ R_p, against the assumption. So r ≤ R_p on γ.

(c) For q ∈ J⁻_X(p) ∩ {t^♭_* ≥ c} let γ be a past directed causal curve in X from p to q. t^♭_* decreases along γ, so
c ≤ t^♭_*(q) ≤ t^♭_* ≤ t^♭_*(p) on it; r ≥ min(r(p), r^♮) on it, dr being future timelike for g on Ω_(1/2) ∩ {r ≤ r^♮}
([[lem:s27-below]] (iv)), as in [[lem:ii-f-1-4]] (a); and r ≤ R_p by (b). So q ∈ L_p. L_p is closed, and on it
t_* ∈ [c, t^♭_*(p)/C_♭] and min(r(p), r^♮) ≤ r ≤ R_p, where r(p) (p ∈ X) and r^♮ lie in the range of r on M°; so L_p is
compact. ∎

**Lemma {#lem:iii-k-6-2}** (Uniqueness near spatial infinity for the initial family.) Let
g_(S,S⁰) := φ_(S,S⁰)^*g_(b₀) + h_(S,S⁰) on 𝒟, where h_(S,S⁰) is given on 𝒟 ∩ Ω_(ext,r_1) by [[thm:iii-c2-3-1]] for
φ_(S,S⁰) and on 𝒮 by [[thm:iv3-2-2]], and is small in C⁰ on 𝒦, with |S| + |S⁰| and the data small. There is R ≥ R_5 such
that 𝒟 ∩ {r ≥ R} ⊂ Ω_(ext,r_1) ∪ 𝒮 and t_IVP = t − C″ there, and:

(a) on 𝒟 ∩ {r ≥ R}, every Cartesian component of g_(S,S⁰) − η is at most 1/20 in modulus, g_(S,S⁰)⁻¹(dt, dt) ≤ −½, and
|V^x| ≤ 2|V^t| for every g_(S,S⁰)-causal vector V; dt lies in the component of the timelike covectors of g_(S,S⁰) that
continues the past cone of η along η + s(g_(S,S⁰) − η), s ∈ [0, 1], and g_(S,S⁰) is time-oriented on 𝒟 as a small
deformation of g_(b₀), for which dt_IVP is past timelike ([[lem:iii-b-3-7]] (b)); so dt_IVP is past timelike for g_(S,S⁰)
on 𝒟;

(b) along causal curves of g_(S,S⁰) in {r ≥ R}, r + 2t_IVP does not increase towards the past and r − 2t_IVP does not
increase towards the future;

(c) along a past (future) directed causal curve of g_(S,S⁰) from p on which τ := t_IVP (τ := −t_IVP) stays ≥ c,

    r ≤ max(R, r(p)) + 2(τ(p) − c).

*Proof.* 𝒦 is compact, so for R above its radius 𝒟 ∩ {r ≥ R} lies in Ω_(ext,r_1) ∪ 𝒮 ([[lem:s27-cover]]), and
t_IVP = t − C″ for r ≥ R_5. There φ_(S,S⁰)^*g_(b₀) agrees with an element of the class 𝒢 of [[def:iii-c-3-4]], so
φ_(S,S⁰)^*g_(b₀) − η ∈ ρ₀²ρ_I²C^∞: on Ω_(ext,r_1) by [[lem:iii-c2-1-1]] for φ_(S,S⁰) ([[lem:s27-translated-exterior]]
(c)), and on 𝒮 by [[lem:iv3-0-1]]. And h_(S,S⁰) lies in the class H^(k,(ℰ_0,ℓ_0),⟨ℰ^C_I⟩,ℓ_I)_b of [[def:iii-c-3-1]],
k ≥ 5, with norm tending to 0 with ‖(γ̃, k̃)‖_(H^(d_0)): on Ω_(ext,r_1) by [[thm:iii-c2-3-1]] (2) with
[[thm:iii-c1-3-1]], and on 𝒮 by [[cor:iv3-2-3]]. Its slot coordinates are bounded pointwise by that norm (Sobolev
embedding on the unit cubes of a b-metric, as in the proof of [[lem:iii-c-2-1]]: k ≥ 5 > 5/2, and the weights ℓ_0 > 0,
ℓ_I > 3/2 and the real parts of the index sets are positive), and they are bounded multiples of its Cartesian components
([[lem:iii-c-1-3]]: the frames are related by F_0(ω)(I + ρ²C^∞)). So for R large and the data and |S| + |S⁰| small, each
Cartesian component of δ := g_(S,S⁰) − η is at most ε := 1/20 in modulus on 𝒟 ∩ {r ≥ R}.

Then, in the coordinates (t, x), with η = diag(−1, 1, 1, 1, 1), the matrix η⁻¹δ has entries ±δ_ij, so its maximum row-sum
norm is at most 5ε = ¼. The Neumann series g_(S,S⁰)⁻¹ = Σ_(k≥0)(−η⁻¹δ)^k η⁻¹ gives
|(g_(S,S⁰)⁻¹ − η⁻¹)(dt, dt)| ≤ Σ_(k≥1)(5ε)^k = 5ε/(1 − 5ε) = ⅓, so g_(S,S⁰)⁻¹(dt, dt) ≤ −1 + ⅓ = −⅔ ≤ −½. The same bound
holds for η + sδ, s ∈ [0, 1], so dt stays timelike along that path, in the component that continues the past cone of η.
For V causal for g_(S,S⁰), η(V, V) ≤ −δ(V, V) ≤ Σ_(i,j)|δ_ij||V^i||V^j| ≤ ε(Σ_i|V^i|)² ≤ 5ε((V^t)² + |V^x|²), by the
Cauchy–Schwarz inequality in five variables; with η(V, V) = −(V^t)² + |V^x|² this gives
|V^x|² ≤ ((1 + 5ε)/(1 − 5ε))(V^t)² = (5/3)(V^t)², so |V^x| ≤ 2|V^t|.

On 𝒟 ∩ {r ≤ R}, dt_IVP is past timelike for g_(b₀) ([[lem:iii-b-3-7]] (b)), with a margin on this compact set, so also
for g_(S,S⁰), φ_(S,S⁰) tending to the identity there and h_(S,S⁰) being small in C⁰ (Cauchy stability on 𝒦, (N) of
[[sec:s27-local]], and the classes above). This proves (a), dt_IVP = dt on {r ≥ R}.

(b) For a past directed causal V in {r ≥ R}, dt(V) = V^t < 0 and dr(V) ≤ |V^x| ≤ −2V^t, so
d(r + 2t_IVP)(V) ≤ 0; likewise for future directed V, d(r − 2t_IVP)(V) ≤ |V^x| − 2V^t ≤ 0.

(c) Let γ be a past directed causal curve from p to q along which τ = t_IVP ≥ c, put R′ := max(R, r(p)), and let s_0
be the last parameter before q at which r ≤ R′ (it exists, as r(p) ≤ R′). Beyond s_0, γ lies in {r > R′} ⊂ {r ≥ R},
so by (b) r(q) + 2τ(q) ≤ r(γ(s_0)) + 2τ(γ(s_0)) ≤ R′ + 2τ(p), τ decreasing along γ. So
r(q) ≤ R′ + 2(τ(p) − τ(q)) ≤ R′ + 2(τ(p) − c). For future directed curves and τ = −t_IVP the same argument with
r − 2t_IVP applies. ∎

#### Proof of the initial family {#sec:s27-initial-proof}

*Proof of [[prop:iii-k-1-2]].* The region 𝒟 is covered by Ω_(ext,r_1), 𝒦 and 𝒮 ([[lem:s27-cover]]), solved in this
order. Write φ := φ_(S,S⁰).

*Exterior.* By [[lem:iii-k-1-1]] (c), P^♮ = P^(χ_0) on Ω_(ext,r_1), so [[thm:iii-c2-3-1]] for φ_(S,S⁰)
([[lem:s27-translated-exterior]] (c)) gives h_(S,S⁰) there, smooth in (S, S⁰), with (2) there by its (3); its
hypotheses (the constraints, and Υ^0 = 0 at Σ^IVP) are [[prop:iii-c2-4-1]] (1)–(2).

*Compact part.* On 𝒦, [[eq:iii-k-1-2]] is the quasilinear wave equation of [[sec:s27-local]]. Its data on the part of
Σ^IVP in 𝒦 are small and smooth, and where 𝒦 borders Ω_(ext,r_1) the exterior solution gives them. dt_IVP is past
timelike ([[lem:iii-b-3-7]] (b)), and the inner boundary {r = r_♭} is spacelike with dr future timelike
([[lem:ii-c-3-2]] (1)); 𝒦 is a compact domain of dependence ([[lem:s27-cover]] (c)). So (N) of [[sec:s27-local]] gives
h_(S,S⁰) there, forward from Σ^IVP and backward to {t_IVP = −ν}, small in every H^k when the data are small in
H^(k+k′) for some k′. It is smooth in (S, S⁰) as its data are: the candidate derivative ḣ solves the linearised
equation with the differentiated data and the forcing from varying the background, which (L) of [[sec:s27-local]]
solves; and, as in [[thm:iii-c2-3-1]] (2), the difference of a difference quotient and ḣ solves a linear equation of
this kind, with coefficients bounded uniformly and with data and forcing tending to 0, so by (L) it tends to 0, and the
difference quotients converge to ḣ. Higher derivatives follow likewise.

*Slab.* On 𝒮 the solution is the restriction of that of [[thm:iv3-2-2]], posed on Ω^♮ = Ω_(ext,r_1) ∪ 𝒮 from Σ^IVP_(r_1)
and Σ_c, with the data that 𝒦 gives on Σ_c; these data and those on Σ^IVP_(r_1) are small in H^(N_ex) when (γ̃, k̃) is
small in H^(d_0), by the choice of d_0. It is the continuation near the interior of ℐ⁺ to {t^♭_* = T̂ + 3}, small, with
the orders (⟨ℰ^C_I⟩, ℓ_I) at ℐ⁺ ([[cor:iv3-2-3]]). Here χ^♮_0 = 1, as t_IVP ≥ r/4 on 𝒮 ([[lem:s27-cover]] (d)) and so
χ_0 = 1.

*Agreement and uniqueness.* By [[lem:ii-f-1-3]] with τ := t_IVP, the three solutions agree on overlaps, and the solution
on 𝒟 is unique; the compact sets that [[lem:ii-f-1-3]] asks for are bounded near infinity by [[lem:iii-k-6-2]] (c), and
away from infinity they lie in the compact 𝒦 or in the exterior and slab regions, closed under past causal curves
within 𝒟 ([[lem:s27-cover]] (c)). In each use the solution (or the difference of two solutions) is extended by 0 across
Σ^IVP, where its Cauchy data vanish, so that it solves the equation across Σ^IVP and its support lies above a level c < 0
of τ, as [[lem:ii-f-1-3]] asks; on {r ≤ R_ν}, beyond 𝒟, the operator is extended smoothly.

*(2).* The argument of [[thm:iii-c2-3-1]] (3) on 𝒟. The data satisfy the constraints and Υ^(χ^♮_0E_Υ) = Υ^0 = 0 at
Σ^IVP ([[lem:iii-k-1-1]] (d); [[prop:iii-c2-4-1]] (2)). With g := φ^*g_(b₀) + h_(S,S⁰), g_0 := φ^*g_(b₀) and
Υ := Υ^(χ^♮_0E_Υ)(g, g_0), [[eq:iii-k-1-2]] reads Ric(g) = δ*_(g_0,E_C)Υ, and the second Bianchi identity
δ_gG_gRic(g) = 0 gives

    δ_gG_g δ*_(g_0,E_C) Υ = 0,

a wave equation for Υ: its principal symbol is that of δ_gG_gδ*_g, ½g⁻¹(ζ, ζ) times the identity, as
δ*_(g_0,E_C) − δ*_g is of order 0 ([[def:iii-b-6-1]]). Its Cauchy data at Σ^IVP vanish: Υ = 0 there, and the
constraints give (G_g Ric(g))(ν, ·) = 0, that is (G_g δ*_(g_0,E_C)Υ)(ν, ·) = 0 there, which with Υ = 0 gives ∂_νΥ = 0
([[lem:iii-k-4-1]] below). So Υ vanishes on 𝒟 by [[lem:ii-f-1-3]], with τ := t_IVP forward from Σ^IVP and, backward
to {t_IVP = −ν}, τ := −t_IVP, a time function for the reversed time orientation; the compact sets are those described
above, and for the backward problem they are bounded as follows. Past directed causal curves lose no r near the inner
boundary (by [[lem:ii-c-3-2]] (1)). Future directed causal curves lose r inside the horizon ({r ≤ r^♮}, where dr is
future timelike), and are bounded below in r by three facts: N_ν ∩ {t_IVP < 0} ⊂ {r > R_ν}, as ν = 0 on [0, R_ν];
t_IVP + ν increases along future causal curves, {t_IVP = −ν} being spacelike with N_ν to its future; and in a thin slab
{0 ≤ t_IVP ≤ t_1} above Σ^IVP the radial speed is bounded, |dr(V)| ≤ C_r dt_IVP(V) for future causal V, with C_r ≥ 2
depending on t_1 (dt_IVP being past timelike on the compact part of the slab, and |V^x| ≤ 2V^t near infinity by
[[lem:iii-k-6-2]] (a)). Fix t_1 := 1, the constant C_r for it, the level c < 0 and δ > 0 with
|c| + δ < min(1, (R_ν − r_♭)/(2C_r)). The backward problem is posed on

    X := (N_ν ∩ {t_IVP < 0}) ∪ ({0 ≤ t_IVP ≤ |c| + δ} ∩ {r + 2C_r t_IVP ≥ R_ν}),

which future causal curves do not leave while t_IVP ≤ |c| + δ: they meet Σ^IVP from N_ν ∩ {t_IVP < 0} at r ≥ R_ν, and
d(r + 2C_r t_IVP)(V) ≥ C_r dt_IVP(V) > 0 along them. So r ≥ R_ν − 2C_r(|c| + δ) > r_♭ on X, which is closed, and
[[lem:ii-f-1-3]] is applied on X° with τ := −t_IVP at the level c, the slab being taken to |c| + δ so that the sets
L_p lie in X°; near infinity [[lem:iii-k-6-2]] (c) bounds r on them. The proof of [[thm:iii-c2-3-1]] (3) uses no
property of the cut-off but its smoothness.

*(1).* The order is that of the proof of [[thm:iii-c2-3-1]]: first (S, S⁰) = (0, 0), which defines h_0 on 𝒟, a
two-sided neighbourhood of Σ^IVP off {r ≤ R_ν} (the backward part lying in N_ν; on {r ≤ R_ν} 𝒟 ends at Σ^IVP, which is
harmless as φ is the identity there); then (S, S⁰) ≠ (0, 0), which uses h_0 at φ(p) for p near Σ^IVP ∪ φ⁻¹(Σ^IVP).
The argument is that of the proof of [[thm:iii-c2-3-1]] (1), made on all of 𝒟 at once.

*A band.* Let R be the radius of [[lem:iii-k-6-2]]. dt_IVP is past timelike for g_(b₀) with a margin on the compact set
𝒟 ∩ {r ≤ R} ([[lem:iii-b-3-7]] (b)). Fix c′ ∈ (0, min(1/16, 1/(4R_6), ⅓c_ν)] (c_ν of the inclusions above) so small
that d(t_IVP − c′r) and d(t_IVP + c′r) are past timelike, with a margin, for g_(b₀) there. On {r ≥ R}, t_IVP = t − C″,
and for every metric g whose Cartesian components lie within 1/20 of those of η, g⁻¹(dt, dt) ≤ −⅔ and
|g⁻¹(dt, dr)|, |g⁻¹(dr, dr)| ≤ 2 (the Neumann series of the proof of [[lem:iii-k-6-2]] (a)), so
g⁻¹(dt ∓ c′dr, dt ∓ c′dr) ≤ −⅔ + 4c′ + 2c′² < 0, and dt ∓ c′dr lies in the cone of dt. Let
𝒰′ := 𝒟 ∩ {|t_IVP| < c′r}, a neighbourhood of Σ^IVP in 𝒟, and take C(|S| + |S⁰|) ≤ ¼c′ in [[lem:s27-boost-move]],
besides the smallness of the statement.

*The cut-off vanishes.* Let 𝒪 := {|t_IVP| < 2c′r}. On 𝒪, |t_IVP| < r/8, so χ_0 = 0, and t_* < ½: for r ≥ R_6,
t_* = t_IVP − F < 2c′r − r/4 < 0 by [[eq:s27-f]], and for r < R_6, t_* ≤ t_IVP < 2c′R_6 ≤ ½. So χ^♮_0 = 0 on 𝒪. For
p ∈ 𝒰′, |t_IVP(φ(p))| < (5/4)c′r(p) ≤ (5/3)c′r(φ(p)), as r(φ(p)) ≥ ¾r(p) ([[lem:s27-boost-move]]); so φ(p) ∈ 𝒪. And
φ(p) ∈ N_ν, as 𝒰′ ⊂ W (c′ ≤ ⅓c_ν; the inclusions above), and t_*(φ(p)) < ½; so φ(p) ∈ 𝒟 ∩ 𝒪.

*φ^*h_0 solves the equation near the data surface.* By (2) at (0, 0), Ric(g_(b₀) + h_0) = 0 on 𝒟 and
Υ^(χ^♮_0E_Υ)(g_(b₀) + h_0, g_(b₀)) = 0 on 𝒟, which on 𝒟 ∩ 𝒪 is Υ⁰(g_(b₀) + h_0, g_(b₀)) = 0. Pulling back by φ,
Ric(φ^*g_(b₀) + φ^*h_0) = φ^*Ric(g_(b₀) + h_0) = 0 and, by [[eq:iii-c2-2-2]],
Υ⁰(φ^*g_(b₀) + φ^*h_0, φ^*g_(b₀)) = φ^*Υ⁰(g_(b₀) + h_0, g_(b₀)) = 0 on 𝒰′, where χ^♮_0 = 0 as well. So both terms of
P^♮(φ^*g_(b₀) + φ^*h_0, φ^*g_(b₀)) vanish on 𝒰′, and φ^*h_0 solves [[eq:iii-k-1-2]] there, with the data
h⁰_(S,S⁰), h¹_(S,S⁰) on Σ^IVP, by their definition. (The operator δ*_(g_0,E_C) is not pulled back, as in the proof
of [[thm:iii-c2-3-1]] (1); it acts on a vanishing 1-form.)

*Uniqueness.* v := h_(S,S⁰) − φ^*h_0 solves L̄v = 0 on 𝒰′, L̄ := ∫_0^1 L^(χ^♮_0)_(g_s,g_0) ds with g_0 := φ^*g_(b₀)
and g_s := g_0 + φ^*h_0 + sv, and v and its first derivatives vanish on Σ^IVP. Each g_s is a convex combination of
φ^*(g_(b₀) + h_0) and φ^*g_(b₀) + h_(S,S⁰), so 2L̄ has principal symbol ḡ⁻¹(ζ, ζ)Id, ḡ⁻¹ := ∫_0^1 g_s⁻¹ ds, and ḡ is a
Lorentzian metric, C⁰-close to g_(b₀) on 𝒰′ ∩ {r ≤ R} and with Cartesian components within 1/20 of those of η on
𝒰′ ∩ {r ≥ R}, as g_(S,S⁰) is in [[lem:iii-k-6-2]] (a), for |S| + |S⁰| and the data small. So (a)–(c) of
[[lem:iii-k-6-2]] hold for ḡ, with the same proofs, and d(t_IVP − c′r), d(t_IVP + c′r) are past timelike for ḡ on
𝒰′. Then v = 0 on 𝒰′ by [[lem:ii-f-1-3]], applied to 2L̄ as in the *(2)* paragraph, with 𝒰′ in place of 𝒟, the
constants there taken for ḡ, and |c| + δ moreover below c′(R_ν − 2C_r(|c| + δ)): forward from Σ^IVP with
τ := t_IVP, and backward on X ∩ 𝒰′ with τ := −t_IVP. The compact sets described there lie in 𝒰′: along future causal
curves of ḡ, t_IVP − c′r and t_IVP + c′r increase, so past curves from points with t_IVP < c′r keep t_IVP < c′r, and
future curves from points with t_IVP > −c′r keep t_IVP > −c′r; and the slab {0 ≤ t_IVP ≤ |c| + δ} ∩ X lies in
{t_IVP < c′r}, as r ≥ R_ν − 2C_r(|c| + δ) there. Finally φ⁻¹(Σ^IVP) ⊂ 𝒟 (the inclusions above) and
|t_IVP| ≤ ¼c′r on it ([[lem:s27-boost-move]]), so 𝒰′ is a neighbourhood of Σ^IVP ∪ φ⁻¹(Σ^IVP) in 𝒟, on which
h_(S,S⁰) = φ^*h_0.

*(3).* The exterior part is [[thm:iii-c1-3-1]] with [[thm:iii-c2-3-1]] (2), for φ_(S,S⁰); the slab part is
[[cor:iv3-2-3]]; the compact part is (N) of [[sec:s27-local]]. For the derivatives in (S, S⁰), ∂^j_(S,S⁰)h_(S,S⁰)
solves the linearised equation with data ∂^j_(S,S⁰)(h⁰_(S,S⁰), h¹_(S,S⁰)), which are pull-backs of h_0 and its
derivatives, and so small with h_0; its equation also has the term from varying the background φ^*g_(b₀), which carries
a factor of h_(S,S⁰) (the proof of [[thm:iii-c2-3-1]] (2)) and is small too; so (L) and the linear estimates of
[[thm:iv2-2-4]] and [[thm:iv3-2-1]] bound it by quantities that tend to 0 with the data. The sources give continuity at
0, not a linear bound: (N), [[eq:iii-c1-3-2]] and the ε₁ clauses of [[thm:iv2-3-1]] and [[thm:iv3-2-2]] state that the
solution tends to 0 as the data do, at a finite loss of derivatives; uniformly in (S, S⁰) small, as the proof of (N)
gives continuity at every (0, S, S⁰), the closed ball of parameters is compact, and the constants of the exterior and
slab theorems depend on the background only through bounds uniform in it. k′_k collects the losses up to the order
k + 2, and ω_k(s) is the supremum of the left side over the parameters and the data with ‖(γ̃, k̃)‖_(H^(k+k′_k)) ≤ s,
finite for s ≤ s_k and tending to 0 with s. ∎

### The map Ψ {#sec:iii-k-2}

**Definition {#def:iii-k-2-1}** (The map Ψ; [Hin26, (12.34)].) Let χ_− ∈ C^∞(ℝ) equal 1 on (−∞, T̂ + 7/4] and 0 on
[T̂ + 2, ∞). For U ∈ 𝒟^∞_ex small, with boost component S and translation component S⁰ := S^(0)_1
([[def:iii-j-1-1]]),

    Ψ(U) := (χ_−(t^♭_*) h_(−S,−S⁰), 0, 0) + Φ(U).                                                       {#eq:iii-k-2-1}

The first component is defined on Ω_* ∩ {t^♭_* ≤ T̂ + 2} ⊂ 𝒟_(−S,−S⁰), and extended by 0. For S, S⁰ ∈ 𝒮_1 small put

    ĝ_(S,S⁰) := φ_(−S,−S⁰)^*g_(b₀),     G_(S,S⁰) := ĝ_(S,S⁰) + h_(−S,−S⁰),

so that g_(p⃗) = ĝ_(S,S⁰) where χ_K = 0, and G_(S,S⁰) = φ_(−S,−S⁰)^*(g_(b₀) + h_0) near φ_(−S,−S⁰)⁻¹(Σ^IVP)
([[prop:iii-k-1-2]] (1)).

**Lemma {#lem:iii-k-2-2}** ([[thm:iii-j-2-4]] for Ψ; [Hin26, Lemma 12.7].) There are d and ε_0 > 0 such that for
U ∈ 𝒟^∞_ex with ‖U‖_(𝒟^d_ex) < ε_0:

(a) Ψ(U) − Φ(U) is supported in {t^♭_* ≤ T̂ + 2}, and P_5(Ψ(U)) = P_5(Φ(U)) on {t^♭_* > T̂ + 2};

(b) if the tail h̃ of U vanishes on {t^♭_* < c}, c ∈ [T̂, T̂ + 7/4], then P_5(Ψ(U)) = 0 on Ω_* ∩ {t^♭_* < c};

(c) P_5(Ψ(U)) ∈ ℱ^∞_ex, and U ↦ P_5(Ψ(U)) satisfies [[prop:iii-j2-4-3]] on the scales of [[cor:iii-j3-6-6]], with
constants depending on the data through finitely many norms of (γ̃, k̃);

(d) P_5(Ψ(0)) is supported in {T̂ + 7/4 ≤ t^♭_* ≤ T̂ + 2}, and ‖P_5(Ψ(0))‖_(ℱ^k_ex) ≤ C_kω_k(‖(γ̃, k̃)‖_(H^(k+k′_k)))
when ‖(γ̃, k̃)‖_(H^(k+k′_k)) ≤ s_k, with k′_k, s_k and ω_k of [[prop:iii-k-1-2]] (3).

Below, d is the d of [[thm:iii-k-3-2]], fixed in its proof (not the d = 7 of [[ch:s26]], whose N_NM is the N_ex of
[[thm:iv3-2-2]] here), N_NM := 21d + 6 is the regularity of [[thm:ii-g-2-1]] for it, k″ := max_(k≤N_NM) k′_k = k′_(N_NM),
s_♭ := min_(k≤N_NM) s_k and ω_♭ := max_(k≤N_NM) ω_k on [0, s_♭]. The smallness constants use orders k ≤ N_NM only; a
bound needed at every order k (the bound on e_S and e_(S⁰) in the proof of [[lem:iii-k-2-3]], which feeds
[[eq:ii-g-2-4]]) carries k′_k and ω_k.

*Proof.* Write ĝ := ĝ_(S,S⁰) and G := G_(S,S⁰), with S⁰ := S^(0)_1. On {t^♭_* < T̂ + 2}, χ_K = 0 (as T_K > T̂ + 2), so
g_(p⃗) = ĝ ([[sec:iii-k-0]]). Also h_tot(p⃗) and ϑ_tot(p⃗) vanish there, being supported in 𝒞 ⊂ supp χ_K
([[lem:iii-i7-2-2]], [[def:iii-i9-2-3]]), and so does h_(b,rem)(q), which carries χ_K ([[eq:iii-i14-1-2]]). By
[[eq:iii-j-2-1]], the metric component of Φ(U) is χ_ι Σ_λ u_λ + h̃ + χ_ι Σ_(λ₀) h_(λ₀), which is h̃ on
{t^♭_* ≤ T̂ + 2}, as χ_ι = 0 there ([[sec:iii-k-0]]). So on Ω_* ∩ {t^♭_* < T̂ + 2},

    P_5(Ψ(U)) = P(ĝ + χ_−h_(−S,−S⁰) + h̃, ĝ),     P(g, g_0) := Ric(g) − δ*_(g_0,E_C)Υ^(E_Υ)(g, g_0)

([[eq:iii-i9-2-3]], with g_0 = g_(p⃗) as in [[def:iii-i7-2-3]]).

(a) holds as χ_− = 0 on {t^♭_* ≥ T̂ + 2} and P_5 is a differential operator.

(b) On Ω_* ∩ {t^♭_* < c}, χ_− = 1 and h̃ = 0, so P_5(Ψ(U)) = P(G, ĝ). This is 0 − δ*0 = 0 by [[prop:iii-k-1-2]] (2)
with (−S, −S⁰), as Ω_* ⊂ {t_* ≥ 1}, where χ^♮_0 = 1.

(c) Near ℐ⁺ ∩ {t^♭_* ≤ T̂ + 2}, [[cor:iii-c-5-3]] applies with g_0 = ĝ (in 𝒢 by [[lem:s27-translated-exterior]] (b),
as in [[lem:iv3-0-1]]; Ric(g_0) = 0) and h = χ_−h_(−S,−S⁰) + h̃, which has the orders (⟨ℰ^C_I⟩, ℓ_I) at ℐ⁺
([[prop:iii-k-1-2]] (3), [[def:iii-j3-1-1]]). So P_5(Ψ(U)) has the orders (⟨ℰ^C_I + 1⟩′, ℓ_I + 1) of ℱ_ex there. On
{t^♭_* > T̂ + 2} it is P_5(Φ(U)) ∈ ℱ^∞_ex ([[cor:iii-j3-6-6]]). Supported character: for U whose tail vanishes on
{t^♭_* < T̂} (the class B^∞ of [[sec:iii-k-3]]), P_5(Ψ(U)) vanishes there by (b); and on {t^♭_* < T̂ + 7/4},

    P_5(Ψ(U)) = ∫_0^1 L_(G+sh̃, ĝ) h̃ ds,

as P(G, ĝ) = 0; here L_(g,g_0) is the linearisation of P in its first argument. This is a differential operator applied
to h̃, which has supported character. The bounds of [[prop:iii-j2-4-3]] hold for Φ. The added terms are
χ_−h_(−S,−S⁰), a fixed tensor smooth in the finite-dimensional (S, S⁰) ([[prop:iii-k-1-2]] (3)), and its products with
h̃ in P on the compact t^♭_*-range [1, T̂ + 2]. The tame bounds of [[sec:iii-j2-1]] (with [[lem:ii-g-4-1]]) bound them,
with constants depending on finitely many norms of h_(−S,−S⁰) and of its derivatives in (S, S⁰) of order at most 2.

(d) At U = 0, h̃ = 0 and S = S⁰ = 0, so P_5(Ψ(0)) = P(g_(b₀) + χ_−h_0, g_(b₀)) on Ω_* ∩ {t^♭_* < T̂ + 2} by the display
above, and P_5(Ψ(0)) = P_5(Φ(0)) = P(g_(b₀), g_(b₀)) = 0 on {t^♭_* > T̂ + 2} by (a). On {t^♭_* < T̂ + 7/4} it is
P(g_(b₀) + h_0, g_(b₀)) = 0 by [[prop:iii-k-1-2]] (2). So it vanishes outside supp dχ_−, and it is a smooth function
of h_0 and its derivatives of order at most 2, vanishing at h_0 = 0; so its ℱ^k_ex-norm is at most C_k‖h_0‖_(H^(k+2))
while h_0 is bounded in a fixed norm of finite order (a Moser bound), and [[prop:iii-k-1-2]] (3) bounds
‖h_0‖_(H^(k+2)) by ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))). ∎

**Lemma {#lem:iii-k-2-3}** (Right inverses for Ψ; [[thm:iii-j1-2-1]] for Ψ, [Hin26, Theorem 12.8, last paragraph].)
There are d and ε_0 such that for U ∈ 𝒟^∞_ex with ‖U‖_(𝒟^d_ex) < ε_0 there is a linear map
ℛ(U) : ℱ^∞_ex → 𝒟^∞_ex with D_U(P_5 ∘ Ψ)(ℛ(U)f) = f. It satisfies the tame estimate [[eq:iii-j2-4-2]] on the exact
scales ([[cor:iii-j3-6-6]]). If the tail h̃ of U and f vanish on {t^♭_* < c}, c ∈ [T̂, T̂ + 7/4], then so does the tail
h̃′ of ℛ(U)f.

*Proof.* Write S⁰ := S^(0)_1 for the translation component of U, and S′, S⁰′ for the boost and translation components
of U′. *The base point.* Ψ(U) = (h + χ_−h_(−S,−S⁰), p⃗, q) with (h, p⃗, q) = Φ(U). Its black hole parameter b lies in
ℬ_*, as |b − b₀| ≤ ‖U‖_(𝒟^d). Its metric component h + χ_−h_(−S,−S⁰) lies in the background class 𝒳^∞ of
[[eq:iii-i-1-4]], which has no support condition, and is small there ([[prop:iii-k-1-2]] (3)). [[thm:iii-i14-3-1]] (at
a rotating b, through [[prop:iii-i15-2-5]]) and [[thm:iii-j2-4-1]] take the base point only through such a class and its
smallness. The proof of [[thm:iii-j1-2-1]] takes it only through these and through D_UΦ at U, which depends on U only
through U_0 = (b − b₀, S, S⁰), as Φ is affine in U_1 ([[thm:iii-j-2-4]]).

*The boost and translation directions.* With H(S, S⁰) := h_(−S,−S⁰),
D_UΨ(U′) = D_UΦ(U′) + (χ_−(∂_S H(S′) + ∂_(S⁰) H(S⁰′)), 0, 0), so

    D_U(P_5 ∘ Ψ)(U′) = D_(Ψ(U))P_5(D_UΦ(U′)) + D_hP_5(Ψ(U))(χ_−(∂_S H(S′) + ∂_(S⁰) H(S⁰′))).

In the construction of the proof of [[thm:iii-j1-2-1]], D_(Ψ(U))P_5(D_UΦ(U′)) enters [[eq:iii-i14-3-1]] through
D_(p⃗)P_5(p⃗′). The boost component S′ enters there through its defect f^S_(h,p⃗)(S′), and the translation component
S⁰′ through its defect f^s1_(h,p⃗)(S⁰′) ([[lem:iii-i7-3-1]]; Step 2 of the proof of [[thm:iii-i14-3-1]]). Replace
these defects by

    f^S_Ψ(S′) := f^S_(h,p⃗)(S′) + e_S(S′),     f^s1_Ψ(S⁰′) := f^s1_(h,p⃗)(S⁰′) + e_(S⁰)(S⁰′),
    e_S(S′) := (D_(p⃗)P_5|_(Ψ(U)) − D_(p⃗)P_5|_(Φ(U)))(S′, 0, 0) + D_hP_5(Ψ(U))(χ_− ∂_S H(S′)),
    e_(S⁰)(S⁰′) := (D_(p⃗)P_5|_(Ψ(U)) − D_(p⃗)P_5|_(Φ(U)))(0, 0, S⁰′) + D_hP_5(Ψ(U))(χ_− ∂_(S⁰) H(S⁰′)),

the parameter directions written (S, b, S^(0)_1). e_S and e_(S⁰) are supported in Ω_* ∩ {t^♭_* ≤ T̂ + 2}: the two base
points differ by χ_−h_(−S,−S⁰), and D_(p⃗)P_5 is local. On {t^♭_* < T̂ + 7/4}, e_S(S′) = f^S_Ψ(S′) − f^S_(h,p⃗)(S′)
and e_(S⁰)(S⁰′) = f^s1_Ψ(S⁰′) − f^s1_(h,p⃗)(S⁰′), and the four terms are O(h̃): f^S_Ψ and f^s1_Ψ are the derivatives
of U ↦ P_5(Ψ(U)) in the boost and translation directions, and f^S_(h,p⃗), f^s1_(h,p⃗) those of P_5 at Φ(U); where h̃
vanishes, P_5 vanishes identically in (S, S⁰) along both families ([[lem:iii-k-2-2]] (b) for Ψ; for Φ,
P(ĝ_(S,S⁰), ĝ_(S,S⁰)) = Ric(ĝ_(S,S⁰)) = 0, the other parameter terms being supported in supp χ_K), so the four
derivatives vanish there; in general each is an integral of h̃ as in [[lem:iii-k-2-2]] (c). So for U whose tail
vanishes on {t^♭_* < T̂}, e_S and e_(S⁰) vanish there, and they lie in ℱ^∞_ex, at ℐ⁺ by [[cor:iii-c-5-3]] as in
[[lem:iii-k-2-2]] (c). Their bounds are tame, e_S and e_(S⁰) involving h̃ through D_hP_5 at Ψ(U):

    ‖e_S(S′)‖_(ℱ^k_ex) + ‖e_(S⁰)(S⁰′)‖_(ℱ^k_ex)
        ≤ C_k (ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))) + ω_♭(‖(γ̃, k̃)‖_(H^(N_NM+k″))) ‖U‖_(𝒟^(k+d)_ex)) (|S′| + |S⁰′|),

by [[prop:iii-k-1-2]] (3) and the tame bounds of [[sec:iii-j2-1]], when ‖(γ̃, k̃)‖_(H^(k+k′_k)) ≤ s_k and
‖(γ̃, k̃)‖_(H^(N_NM+k″)) ≤ s_♭. At an order k > N_NM at which the first condition fails, ω_k(‖(γ̃, k̃)‖_(H^(k+k′_k))) is
replaced by a finite constant depending on the data, h_(S,S⁰) and its derivatives in (S, S⁰) lying in every H^(k+2)
([[prop:iii-k-1-2]] (3)); such a constant does not enter the threshold of [[thm:ii-g-2-1]].

So [[thm:iii-i14-3-1]] at the base point Ψ(U), with the defects f^S_Ψ and f^s1_Ψ, is [[thm:iii-i14-3-1]] with two
more terms e_S(S′) + e_(S⁰)(S⁰′) in the forcing G′ of Step 2 of its proof. They are small with the data and linear in
the finite-dimensional (S′, S⁰′); they enter the maps A_k of Step 3 as Δ_q does ([[lem:iii-i14-2-4]]), and they perturb
Step 1 (the base level, where the parameters of low rate, among them S′ and S⁰′, are determined) by terms of the same
kind, small with the data. So the elimination runs unchanged for data small, and the construction of U′ in the proof of
[[thm:iii-j1-2-1]], [[thm:iii-j2-4-2]] and [[cor:iii-j3-6-6]] follow as for Φ. At a rotating b,
[[cor:iii-i15-3-2]] provides them.

*Supports.* Let h̃ and f vanish on {t^♭_* < c}, c ∈ [T̂, T̂ + 7/4]. There χ_ι, χ_K and the corrections vanish, as in
[[lem:iii-k-2-2]], and χ_− = 1; so P_5 ∘ Ψ = Q(S, S⁰, h̃) := P(G_(S,S⁰) + h̃, ĝ_(S,S⁰)) there, Q being a differential
operator in h̃. As Q(S, S⁰, 0) = 0 for all small (S, S⁰) ([[prop:iii-k-1-2]] (2) with (−S, −S⁰)),
∂_(S,S⁰)Q(S, S⁰, 0) = 0; and as h̃ vanishes on the open set {t^♭_* < c}, there

    D_U(P_5 ∘ Ψ)(U′) = ∂_(S,S⁰)Q(S, S⁰, 0)(S′, S⁰′) + D_(h̃)Q(S, S⁰, 0)h̃′ = L_(G_(S,S⁰), ĝ_(S,S⁰)) h̃′;

the boost and translation components of U′ enter only through the first term, which vanishes. So
L_(G_(S,S⁰), ĝ_(S,S⁰)) h̃′ = f = 0 on {t^♭_* < c}. Within the construction, h̃′ is the remainder of the forward
solution there: the rows and towers are supported in supp χ_K, and the ι⁺-terms carry χ_ι. h̃′ has supported character
at {t^♭_* = 1} (the spaces of [[def:iii-j-1-1]]), so, extended by 0, it solves L_(G_(S,S⁰), ĝ_(S,S⁰)) h̃′ = 0 on

    X := 𝒟°_(−S,−S⁰) ∩ {¾ < t^♭_* < c},

and [[lem:ii-f-1-3]] is applied on X with τ := t^♭_* at the level 7/8, below its support; t^♭_* is a time function of
G_(S,S⁰) on X by [[lem:s27-below]] (iii) on Y := X. [[lem:iii-k-6-1]] with G_(S,S⁰) in place of g, Y := X, its c equal
to 7/8 and T := T̂ + 2 gives the compact sets. Indeed L_p ⊂ X: 7/8 ≤ t^♭_* ≤ t^♭_*(p) < c on L_p, and {t^♭_* > ¾}
lies in φ_(−S,−S⁰)⁻¹({t_IVP ≥ 0}), since on it t_IVP = t_* + F ≥ t^♭_* + F > ¾ + F, F ≥ r/4 for r ≥ R_6
([[eq:s27-f]]), while φ_(−S,−S⁰) moves t_IVP by at most C(|S| + |S⁰|)r and not at all on {r ≤ 5R₁}
([[lem:s27-boost-move]]). G_(S,S⁰) lies in the class of [[lem:s27-below]] on X: on Ω_* as G_(S,S⁰) − g_(b₀) is small in
𝒢̃^(0,(1,0,0))_(e3b) on Ω_* ∩ {t^♭_* ≤ T̂ + 2} ([[prop:iii-k-1-2]] (3), [[lem:iii-b-5-2]],
[[lem:s27-translated-exterior]] (b)); below Ω_* near ℐ⁺ by the same facts, h_(−S,−S⁰) having the orders of
[[def:iii-c-3-1]] on 𝒟 near infinity ([[thm:iii-c2-3-1]] (2), [[cor:iv3-2-3]]); and on the compact rest by its
smallness in C⁰. So h̃′ = 0 on {t^♭_* < c}.

Without the hypothesis on h̃, D_U(P_5 ∘ Ψ)(U′) contains ∂_(S,S⁰)Q(S, S⁰, h̃)(S′, S⁰′), which need not vanish on
{t^♭_* < c}; so the support property holds only at base points whose tail vanishes below the level.
[[thm:ii-g-2-1]] (iii) asks it only there ([[rem:s10-right-inverses]]), and that is how [[thm:iii-k-3-2]] uses it. ∎

### The Nash–Moser iteration {#sec:iii-k-3}

*The scales.* Let c_1 := ⅛ and c_0 := c_1/8 = 1/64 be the constants of [[prop:ii-g-3-1]] for t := t^♭_* − T̂ on
M_(1/2), with t := −1 where t_* < ½. (T1)–(T3) of [[sec:ii-g-3-1]] hold for this t as for t^♭_* − 1 in
[[rem:ii-g-3-2]], the level only moving: t^♭_* is smooth on M_(1/2) with dt^♭_*|_(Tℐ⁺) = dt_*|_(Tℐ⁺) ≠ 0, the set
{|t| ≤ 2c_1} is bounded in t_* (t_* ≤ (T̂ + ¼)/C_♭ there) and lies in {t_* ≥ T̂ − ¼ ≥ 7/4}, so it meets neither ι⁺ nor
K⁺ nor {t_* = ½}, and on ℐ⁺, t^♭_* = t_* and t − t̄ ∈ ρ_I^(1/2)C^∞_b with
t̄ := t_* − T̂. The weighted b-Sobolev spaces on
M and on M_(1/2) coincide, their b-vector fields being the same. Fix χ_9 ∈ C^∞(ℝ) equal to 0 on (−∞, 17/2] and 1 on
[9, ∞). For η ∈ [0, 1] and k ∈ ℕ₀ ∪ {∞} let

    B^k := {U ∈ 𝒟^k_ex : S_rem, b_rem, Y_(ψ,rem) supported in {t_* ≥ 8}, supp h̃ ⊂ {t^♭_* ≥ T̂}},
    B^k_η := {U ∈ B^k : supp h̃ ⊂ {t^♭_* ≥ T̂ + c_0η}, the q-tails supported in {t_* ≥ 8 + c_0η}},
    F^k := {f ∈ ℱ^k_ex : supp f ⊂ {t^♭_* ≥ T̂}},     F^∞_η := {f ∈ F^∞ : supp f ⊂ {t^♭_* ≥ T̂ + c_0η}},

with the norms of 𝒟^k_ex and ℱ^k_ex. Here the q-tails are the components S_rem, b_rem and Y_(ψ,rem), ψ ∈ ℛ′_0, of U
([[def:iii-j-1-1]]). B^k_η is closed in B^k (support conditions are closed), non-increasing in η, and B^k_0 = B^k;
F^k is closed in ℱ^k_ex.

**Lemma {#lem:iii-k-3-1}** (Smoothing on 𝒟_ex; [Hin26, Section 13.1, Step 3 (4)].) For θ > 1 there are linear maps
S_θ : B^∞_(θ^(−1/2)) → B^∞ with S_θ(B^∞_η) ⊂ B^∞_(η−θ^(−1/2)) for η ∈ [θ^(−1/2), 1], satisfying [[eq:ii-g-2-1]] with
constants independent of θ.

*Proof.* Componentwise: the norm of 𝒟^k_ex is the sum of the norms of the components ([[def:iii-j3-1-1]]), so
[[eq:ii-g-2-1]] for each component gives it for the sum.

*The finite-dimensional components* b − b₀, S, S^(0)_1 and u^0_λ: S_θ := id.

*f_λ:* a polynomial in z of bounded degree with coefficients in a partially polyhomogeneous b-Sobolev space on a compact
manifold with boundary, with no support condition. Smooth each expansion coefficient and the remainder by the operator
S̃_θ of Step 4 of the proof of [[prop:ii-g-3-1]], the smoothing on all of w H̄^0_b with no condition on supports, built
on the manifold carrying it; then reassemble.

*The q-tails* S_rem, b_rem, Y_(ψ,rem): weighted b-Sobolev functions of t_* ∈ [1, ∞]. Use [[prop:ii-g-3-1]] on the
one-dimensional manifold [1, ∞] with t := t_* − 8, for which (T1)–(T3) hold trivially (the set {|t| < 2c_1} lies in
the interior). This gives the support behaviour.

*h̃:* partially polyhomogeneous at ℐ⁺ with index set collection ⟨ℰ^C_I⟩ and remainder of order ℓ_I ([[eq:iii-c-3-3]],
in the splitting [[eq:iii-c-1-6]]). By the definition of these spaces, h̃ corresponds one to one to its expansion
coefficients a_(z,j) (functions on ℐ⁺ ∩ Ω_*) and its remainder, and the norm is the sum of their norms. Put

    S_θ h̃ := Σ_((z,j)) χ_I ρ_I^z (log ρ_I)^j E(S^ℐ_θ(a_(z,j))) + S_θ(h̃_rem).

Here S^ℐ_θ is [[prop:ii-g-3-1]] on ℐ⁺ with t|_ℐ⁺ (= t^♭_* − T̂ there), S_θ(h̃_rem) is [[prop:ii-g-3-1]] on M_(1/2) with
t = t^♭_* − T̂, and E(a) is the extension of a function a on ℐ⁺ that is constant along the fibres of a collar of ℐ⁺
which lie in the level sets of (t^♭_*, ω) on {t^♭_* ≤ T̂ + 2}, and along any b-smooth collar beyond. (t^♭_*, x_I, ω)
are smooth coordinates on M_(1/2) near ℐ⁺, so the fibres are smooth curves in M_(1/2) transversal to ℐ⁺, and a function
constant along them is smooth on M_(1/2): on M it is polyhomogeneous at ℐ⁺ with index set ½ℕ₀, without logarithms. So
passing from a smooth collar of M to this one changes χ_Iρ_I^z(log ρ_I)^jE(a) by terms ρ_I^(z+k/2)(log ρ_I)^j times
smooth functions, k ≥ 1. These stay in the class: each slot's index set ℰ_s in [[eq:iii-c-3-3]] is ℰ^C_I together with
points of ℰ^tot_I ([[eq:iii-c-3-2]]), so ℰ_s + ½ ⊂ ℰ^C_I ⊂ ℰ_s by [[lem:iii-c-3-2]] (a), logarithmic orders included.
The terms of order below ℓ_I join the expansion and the others the remainder, so the space and its norm are unchanged
up to equivalence. For U ∈ B_η the coefficients vanish on {t^♭_* < T̂ + c_0η} ∩ ℐ⁺, as h̃ does near it; so each term
χ_Iρ_I^z(log ρ_I)^jE(a_(z,j)), and hence the remainder, is supported in {t^♭_* ≥ T̂ + c_0η}, the fibres preserving
t^♭_*. The operators of [[prop:ii-g-3-1]] preserve the support classes, and [[eq:ii-g-2-1]] holds for each piece by
[[eq:ii-g-3-1]]. The collar follows the levels of the function that defines the classes, and that function has a robust
timelike margin; the cost is the half-integer powers just absorbed. ∎

**Theorem {#thm:iii-k-3-2}** (The solution of the gauge-fixed equation in the cone; [Hin26, Section 13.1, Step 3].)
There are d_1 and ε > 0 such that, if ‖(γ̃, k̃)‖_(H^(d_1)) < ε, there is U ∈ B^∞_(1/2), small in 𝒟^(3d)_ex, with
P_5(Ψ(U)) = 0 on Ω_*. Its tail h̃ is supported in {t^♭_* ≥ T̂ + ½c_0}.

*Proof.* Apply [[thm:ii-g-2-1]] with B^k, B^k_η, F^k and F^∞_η as above, η_0 := 1, d the largest of the d's of
[[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], and the map U ↦ P_5(Ψ(U)) on {U ∈ B^∞ : |U|_(3d) < δ}
in the role of the map of [[thm:ii-g-2-1]], with δ at most the ε_0 of [[lem:iii-k-2-2]] and [[lem:iii-k-2-3]] (a bound
in 𝒟^d_ex) and of [[prop:iii-j2-4-3]] (a bound in 𝒟^(3d)_ex), as ‖U‖_(𝒟^d_ex) ≤ |U|_(3d).

*(i)* is [[lem:iii-k-3-1]].

*(ii)* For U ∈ B_η, η ≤ 1, the tail vanishes on {t^♭_* < T̂ + c_0η}, and T̂ + c_0η ≤ T̂ + 1/64 < T̂ + 7/4. So
P_5(Ψ(U)) ∈ F^∞_η by [[lem:iii-k-2-2]] (b)–(c). The map is twice differentiable in the sense of [[thm:ii-g-2-1]], with
[[eq:ii-g-2-2]]–[[eq:ii-g-2-3]], by [[lem:iii-k-2-2]] (c). Its q-tails enter only through h_(b,rem)(q), whose factor χ_K
vanishes on {t_* < 10} ([[eq:iii-i14-1-2]], and T_K ≥ 10). They also enter through the iteration of [[sec:iii-j-2]],
whose sources involve them only through h_(b,rem)(q) ([[thm:iii-j-2-4]] (2)). So the map depends on the q-tails only
through their values on {t_* ≥ 10}.

*(iii)* For U in the domain put Ψ_NM(U) := Zℛ(U), the right inverse that [[thm:ii-g-2-1]] (iii) asks for, with ℛ(U)
from [[lem:iii-k-2-3]] and Z the multiplication of the q-tails by χ_9(t_*). By the last sentence of (ii),
D_U(P_5 ∘ Ψ)(ZU′) = D_U(P_5 ∘ Ψ)(U′), as χ_9 = 1 on {t_* ≥ 9}. So Ψ_NM(U) is a right inverse. Z is bounded on every
𝒟^k_ex (χ_9(t_*) is smooth and constant near t_* = ∞), so [[eq:ii-g-2-4]] holds by [[lem:iii-k-2-3]]. As far as the
q-tails are concerned Z maps into B^∞_1: their support lies in {t_* ≥ 17/2} ⊂ {t_* ≥ 8 + c_0}. For U ∈ B_η in the
domain and f ∈ F_η, the tails of U and f vanish on {t^♭_* < T̂ + c_0η}, so the tail of ℛ(U)f does
([[lem:iii-k-2-3]]), and Ψ_NM(U)(F^∞_η) ⊂ B^∞_η; at η = 0 this says that Ψ_NM(U) maps F^∞ into B^∞. This is
[[thm:ii-g-2-1]] (iii), which asks the support property for u ∈ U ∩ B^∞_η only ([[rem:s10-right-inverses]]); the form
at every u in the domain does not hold here (the proof of [[lem:iii-k-2-3]]).

*Smallness.* The constants C_k (k ≤ N_NM), C_1, C_2 and δ depend on the data only through ‖(γ̃, k̃)‖_(H^(N_NM+k″))
([[lem:iii-k-2-2]] (c), [[lem:iii-k-2-3]]); they are bounded independently of the data once that norm is at most s_♭,
the threshold of [[prop:iii-k-1-2]] (3) at the orders k ≤ N_NM. So the threshold of [[thm:ii-g-2-1]], ε_NM, is
uniform. Let d_1 := max(d_0, N_NM + k″), with d_0 of [[prop:iii-k-1-2]]. By [[lem:iii-k-2-2]] (d),
‖P_5(Ψ(0))‖_(ℱ^(2d)_ex) ≤ C_(2d)ω_(2d)(‖(γ̃, k̃)‖_(H^(2d+k′_(2d)))), and 2d + k′_(2d) ≤ N_NM + k″ ≤ d_1; as ω_(2d)(s)
tends to 0 with s, ‖P_5(Ψ(0))‖_(ℱ^(2d)_ex) < ε_NM for data small in H^(d_1). [[thm:ii-g-2-1]] gives U ∈ B^∞_(1/2)
with |U|_(3d) < δ and P_5(Ψ(U)) = 0. ∎

### Constraint propagation and the theorem {#sec:iii-k-4}

**Lemma {#lem:iii-k-4-1}** (The normal derivative; in any dimension.) Let g be a Lorentzian metric, Σ a spacelike
hypersurface with unit normal ν, κ a 1-form with κ|_Σ = 0, and δ*_(g_0,E_C) as in [[def:iii-b-6-1]]. If
(G_g δ*_(g_0,E_C)κ)(ν, ·) = 0 on Σ, then ∂_νκ = 0 on Σ.

*Proof.* On Σ the tangential derivatives of κ vanish, and the zeroth-order part of δ*_(g_0,E_C) vanishes as κ = 0
(δ*_(g_0,E_C) − δ*_(g_0) and δ*_(g_0) − δ*_g are of order 0). So, as ∇_Y κ = −g(ν, Y)∂_νκ on Σ,
k := δ*_(g_0,E_C)κ = ½(ν^♭ ⊗ w + w ⊗ ν^♭) with w := −∂_νκ, ν^♭ := g(ν, ·), g(ν, ν) = −1. Then
tr_g k = g^(ab)ν_a w_b = w(ν), and (G_gk)(ν, X) = k(ν, X) − ½g(ν, X)w(ν). For X tangent to Σ:
k(ν, X) = ½(g(ν, ν)w(X) + w(ν)g(ν, X)) = −½w(X) and g(ν, X) = 0, so w(X) = 0. For X = ν: k(ν, ν) = −w(ν), so
(G_gk)(ν, ν) = −w(ν) + ½w(ν) = −½w(ν), and w(ν) = 0. So w = 0. ∎

**Proposition {#prop:iii-k-4-2}** (The metric and the constraints.) Let U be given by [[thm:iii-k-3-2]],
(h, p⃗, q) := Φ(U), S its boost, S⁰ := S^(0)_1 its translation and b its black hole parameter. Define

    g := g_(p⃗) + h_tot(p⃗) + h_(b,rem)(q) + χ_−(t^♭_*)h_(−S,−S⁰) + h     on Ω_*,
    g := ĝ_(S,S⁰) + h_(−S,−S⁰)                                            on 𝒟_(−S,−S⁰) ∩ {t^♭_* ≤ T̂ + ¼c_0},

    κ := Υ^(E_Υ)(g, g_(p⃗)) − ϑ_tot(p⃗)          on Ω_*,
    κ := Υ^(χ^♮_0E_Υ)(g, ĝ_(S,S⁰))              on 𝒟_(−S,−S⁰) ∩ {t^♭_* ≤ T̂ + ¼c_0},

with ĝ_(S,S⁰) = φ_(−S,−S⁰)^*g_(b₀) of [[def:iii-k-2-1]]. The two definitions agree on the overlap
Ω_* ∩ {t^♭_* ≤ T̂ + ¼c_0}, and Ric(g) = 0, κ = 0 on the union.

*Proof.* *Overlap.* There χ_K = 0, so g_(p⃗) = ĝ_(S,S⁰); h_tot, h_(b,rem) and ϑ_tot vanish; h = h̃ = 0 (the proof of
[[lem:iii-k-2-2]], and supp h̃ ⊂ {t^♭_* ≥ T̂ + ½c_0}); χ_− = 1; and χ^♮_0 = 1 ([[lem:iii-k-1-1]] (b)). So the two
lines of each definition coincide.

*The equation.* On Ω_*, P_5(Ψ(U)) = 0 reads Ric(g) − δ*_(g_0,E_C)κ = 0 with g_0 := g_(p⃗): this is [[eq:iii-i9-2-3]]
with g′ = g, and [[eq:iii-i14-1-3]], P_5(h′, p⃗, q) = P_4(h′ + h_(b,rem)(q), p⃗), with h′ := h + χ_−h_(−S,−S⁰). On the
second region, Ric(g) = 0 and κ = 0 by [[prop:iii-k-1-2]] (2) with (−S, −S⁰).

*Propagation.* On Ω_* the second Bianchi identity δ_gG_gRic(g) = 0 gives δ_gG_gδ*_(g_0,E_C)κ = 0. The operator
δ_gG_gδ*_(g_0,E_C) has the principal symbol of δ_gG_gδ*_g, which is ½g⁻¹(ζ, ζ) times the identity, as
δ*_(g_0,E_C) − δ*_g is of order 0. κ vanishes on Ω_* ∩ {t^♭_* ≤ T̂ + ¼c_0}, which contains Ω_* ∩ {t^♭_* ≤ 2}
(T̂ ≥ 2). [[lem:ii-f-1-3]] on Ω°_*, with τ := t^♭_* and c := 3/2, gives κ = 0. Its compact sets are those of
[[lem:iii-k-6-1]] (c), with Y := X := Ω°_*, c := 3/2 and T := t^♭_*(p): L_p ⊂ X, as t^♭_* ≥ c > 1 on it. The lemma
applies, g being a metric on Ω_* whose difference from g_(b₀) is small in 𝒢̃^(0,(1,0,0))_(e3b), by (B2) of
[[sec:iii-h2-0]], [[lem:iii-i7-1-3]] (a) for g_(p⃗), and the smallness of U and h_(−S,−S⁰); near the inner boundary,
past causal curves stay in {r ≥ min(r(p), r^♮)} by [[lem:ii-c-3-2]] (1), as in [[lem:ii-f-1-4]] (a). So
Ric(g) = δ*_(g_0,E_C)0 = 0. ∎

[Hin26] propagates the constraints from φ_S(Σ^IVP), using [[lem:iii-k-4-1]] there. Here κ already
vanishes on an open slab of Ω_* ([[prop:iii-k-1-2]] (2)), and [[lem:iii-k-4-1]] enters only through the proof of
[[prop:iii-k-1-2]].

**Theorem {#thm:iii-k-4-3}** (Nonlinear stability near Tangherlini; [Hin26, Theorem 13.1] in dimension 4 + 1.) Let
b₀ = (m₀, 0), let the parameters be chosen as in [[thm:vi-c-2-1]], and let ℰ_0, ℓ_0 be as in [[sec:iii-k-0]]. There
are ε > 0 and d_1 such that the following holds. Let (γ, k) be initial data on Σ^IVP satisfying the constraint
equations, with

    γ − γ_(b₀) ∈ H^(∞,(ℰ_0,ℓ_0))_b(Σ^IVP),     k − k_(b₀) ∈ H^(∞,(ℰ_0+1,ℓ_0+1))_b(Σ^IVP),

of norm < ε in H^(d_1) of these classes. Then there are a Myers–Perry parameter b ∈ ℬ_*, a boost parameter S ∈ 𝒮_1
and a translation parameter S⁰ ∈ 𝒮_1, with |b − b₀|, |S| and |S⁰| small, and a Lorentzian metric g on
Ω_* ∪ 𝒟_(−S,−S⁰) with, for φ := φ_(−S,−S⁰) = ψ_(−S⁰) ∘ φ_(−S):

(1) Ric(g) = 0;

(2) g = φ^*(g_(b₀) + h_0) near φ⁻¹(Σ^IVP), so g induces on φ⁻¹(Σ^IVP) the data (φ|)^*(γ, k);

(3) on Ω_* ∩ {t^♭_* ≥ T̂ + 2},

    g = g_(p⃗) + h_tot(p⃗) + h_(b,rem)(q) + h,     (h, p⃗, q) = Φ(U),  U ∈ 𝒟^∞_ex,

with g_(p⃗) the translated background of [[eq:iii-i7-1-3]], h ∈ 𝒳^∞_(J,ex) (orders (⟨ℰ^C_I⟩, ℓ_I) at ℐ⁺,
(ℰ_+, 3 + ε_+) at ι⁺, α at K⁺), q ∈ 𝒬_ex, and p⃗ with the components b − b₀, S, S⁰ of U ([[thm:iii-j-2-4]] (1)–(2));

(4) where χ_K = 1, g_(p⃗) = g_b, so g − g_b = h_tot(p⃗) + h_(b,rem)(q) + h there: g settles to the Myers–Perry metric
g_b at ι⁺ and K⁺ at the orders of these classes;

(5) the gauge condition κ = 0 of [[prop:iii-k-4-2]] holds on Ω_* ∪ 𝒟_(−S,−S⁰).

*Proof.* [[thm:iii-k-3-2]] and [[prop:iii-k-4-2]]. (2) is [[prop:iii-k-1-2]] (1) with (−S, −S⁰): there
g = φ^*g_(b₀) + h_(−S,−S⁰) = φ^*(g_(b₀) + h_0). (3) holds as χ_− = 0 on {t^♭_* ≥ T̂ + 2}, with [[cor:iii-j3-6-6]] for
the exact classes. (4) is [[eq:iii-i7-1-3]]. ∎

**Remark {#rem:iii-k-4-4}** ([Hin26, Remark 13.4 and Theorem 1.1].) (3) is [Hin26, Remark 13.4 (1)], with the
background translated as well as boosted: in dimension 4 + 1 the shift of the centre of mass is undone by translating
the exterior background ([[def:iii-i7-1-2]]), where [Hin26] uses a correction term ([[ch:s21]]); so the data surface
of (2) is φ_(−S,−S⁰)⁻¹(Σ^IVP), translated as well as boosted. As in [Hin26], the slowest terms at ι⁺ come from
h_tot(p⃗), which is supported in 𝒞 ([[lem:iii-i7-2-2]]); in dimension 4 + 1 their orders are those of [[ch:s21]].
[Hin26] deduces its Theorem 1.1 by pulling back along a diffeomorphism of M that is the identity near
ℐ⁺ ∪ ι⁺ ∪ K⁺, which changes nothing above.

### The parameters: the conditions {#sec:vi-c-1}

The stability theory leaves open the constraint damping gauge E_C, the gauge modification parameters E_Υ, the weights
at ℐ⁺, ι⁺ and K⁺, the data classes and the set of Myers–Perry parameters, and its results state conditions on them.
This section lists every such condition with the results that state or use it, and what its threshold depends on;
[[thm:vi-c-2-1]] shows that they can all be met, in an order in which each threshold depends only on choices already
made. m₀ > 0 is fixed and R₁ := m₀^(1/2). Conditions that only restate a choice made in another row are omitted. The
constants v_C, e_C, C_0 and γ_C of the damping are fixed once, in [[eq:iv4-0-1]], at the point where [[thm:iii-e-1-1]]
is proved, and no result varies them; every result that names them uses that point.

**c1.** (v_C, e_C, C_0) = (½, 1/102400, 100), the point at which [[thm:iii-e-1-1]] is proved ([[eq:iv4-0-1]],
[[sec:iii-k-0]]). Threshold: none.

**c2.** γ_C = h⁻¹, h ∈ 𝖧 = (0, h_*) ∖ 𝖹, h_* = min(10⁻⁶, h_0, h_tf), 𝖹 countable ([[eq:iv4-0-1]], [[lem:iv4-1-3]] (b),
[[prop:np-10-52]] (ii)–(iii)). Threshold: c1.

**c3.** γ_C: (C1)–(C4), the clauses of [[thm:iii-e-1-1]] (3) after its first sentence: the indicial roots of □^C_b are
simple, avoid the listed sets, and are real where their real part is an integer in [3, 51] (used in [[ch:s15]]).
Threshold: c1, c2.

**c4.** γ_C: (C5) γ_C v_C ≥ ½ ([[sec:iii-i10-1]], [[sec:iii-g2-1]]), and s_C := (1 − e_C)(1 − v_C)γ_C > 100
([[sec:iii-f-1]], [[sec:iii-k-0]]). Both hold as γ_C > 10⁶. Threshold: c1.

**u1.** c_Υ, c_(Υ,H), c_C: the fixed 1-forms of [[def:iii-b-6-1]], in the radial forms the proofs use: c_Υ =
ζ(|x|)|x|⁻¹dt and c_(Υ,H) = −½χ(|x|)d|x| ([[sec:iii-d2-1]], [[lem:iii-d-5-1]]), and c_C of [[sec:iv4-0]]. Threshold:
c1.

**u2.** γ_(Υ,H) ∈ (0, ε_0], ε_0 that of [[prop:iii-d1-4-1]]. Threshold: none.

**u3.** e_Υ ∈ (0, min(ε_1, ε_L)), with ε_1 of [[prop:iii-d1-4-1]] and ε_L of [[lem:iii-d-7-1]]
([[prop:iii-f1-3-3]]). Threshold: ε_1 on u2; ε_L on c1–c2.

**u4.** 0 < γ_Υ < min(ε_1, ε_L, γ_1, 3/8, ½s_C, ¼), with γ_1 of [[prop:iii-f1-3-3]]; ε_L contains the bound
C′|γ_Υ| ≤ ½ of the proof of [[lem:iii-d-7-1]] ([[prop:iii-d1-4-1]], [[sec:iii-g2-1]], [[eq:iii-c-1-1]],
[[eq:iii-i9-1-1]]). Threshold: γ_1 on c1–c3 and u2–u3; ε_L on c1–c2.

**u5.** z_Υ := 4e_Υγ_Υ² ∈ (0, ½] ∖ 𝖹_exc, 𝖹_exc countable ([[prop:iii-f1-2-3]] (e), [[sec:iii-g2-1]]). Threshold:
𝖹_exc on c1–c3; u3.

**b1.** b in the ball ℬ_VI of [[thm:vi-b1-5-1]], on which (Dyn) holds. Threshold: none.

**b2.** b ∈ ℬ(γ_(Υ,H)) ([[prop:iii-d1-4-1]]); with the low-frequency radius c_0 of [[cor:iii-h-4-3]], written c_σ in this
section and the next to distinguish it from the constant c_0 of [[sec:iii-k-3]], b ∈ ℬ(c_σ) ([[prop:iii-f2-4-1]]) and in
the neighbourhood of [[cor:iii-h-4-3]]–[[cor:iii-h-4-4]]; and b near b₀ as [[thm:iii-e-1-1]], [[prop:iii-f1-3-3]] and
[[sec:iii-j-1]] ask. Threshold: c1–c2, u1–u5.

**b3.** ℬ_*: open, with closure in ℬ_1, and (B5) of [[sec:iii-h2-0]]: ‖P − 2L_b‖_((0;d)) < ε_0 on ℬ̄_*. This is the only
condition on ℬ_* there; b4 shrinks it further. Threshold: b2, u1–u5.

**b4.** ℬ_*: shrunk so that the states at b are jointly injective ([[lem:iii-i15-1-2]]) and the maps −id + A_k of the
elimination are invertible at every base point ([[thm:iii-i15-3-1]]); both depend on the row set and on the levels up
to α. Threshold: b3, w1–w2, d1–d2.

**w1.** ε_+, ε_K: 0 < ε_K < ε_+ < min(δ_♯, ε_ind, ℓ_I − 3) and ε_+ < ¼ ([[eq:iii-i9-1-1]], (H4) of
[[sec:iii-i10-1]]); (G⁺) ([[def:iii-j-g-plus]]) after decreasing ε_+, Λ containing π_1ℰ^C_I ([[sec:iii-i10-1]]), so
that it is fixed after rows d1–d2; the gap (G) of [[def:iii-i10-1-3]] for ε_K, which includes ε_K < ε_Υ, so that
ε_K < ε_g := min(ε_Υ, ε_ind) ([[ch:s22]]); and the exactness conditions (Ex1) (which is (G⁺) with its closed endpoint)
and (Ex2) of [[def:iii-j3-1-3]]. Here δ_♯ = (1 − e_Υ)γ_Υ; ε_ind is the constant of [[eq:iii-f1-2-2]], fixed by the
indicial roots of L̂_b(0), with which the hypotheses of [[prop:iii-g4-5-1]] are stated; and ε_Υ is the constant of
[[sec:iii-d2-1]], fixed by the indicial roots of (□^Υ_b)^(0), with which the gain in the conclusion of
[[prop:iii-g4-5-1]] is stated. At the gauge parameters of [[prop:np-10-52]], ε_ind ≤ δ_50 = 1.94137… × 10⁻⁸
([[prop:np-10-52]] (iii), [[prop:iii-f1-2-3]] (f)), and δ_50 is the least distance from ℤ among the non-integer
entries of modulus at most 50 that do not depend on h; no proof uses its value. Threshold: u1–u5, d1–d2.

**w2.** α: admissible ([[def:iii-i10-1-3]]), with (A_J) ([[def:iii-j-a-j]]) and the exactness conditions (Ex3)–(Ex4) of
[[def:iii-j3-1-3]], in (4 + ε_K − ε′_0, 4 + ε_K], where such α are dense ([[def:iii-j-a-j]], [[lem:iii-j3-1-4]]).
Threshold: w1, d1–d2 ((A_J) involves Λ).

**d1.** ℰ_0, ℓ_0: min Re ℰ_0 > 3/2 + 2γ_Υ, jℰ_0 ⊂ ℰ_0, ℓ_0 > 3 (so that row d2 is nonempty), ℓ_0 ∉ Re π_1ℰ_0
([[thm:iii-c1-3-1]], [[sec:iii-k-0]], (H4) of [[sec:iii-i10-1]]). Threshold: u4.

**d2.** ℓ_I: 3 < ℓ_I < min(ℓ_0, 3/2 + s_C), with row w1's ε_+ < ℓ_I − 3: [[thm:iii-c1-3-1]] asks 3/2 < ℓ_I < ℓ_0, (H4)
asks ℓ_I > 3 + ε_+, and [[thm:iii-k-4-3]] uses one ℓ_I for both. ℓ_I avoids the exclusion sets of (H4), which are
discrete: for ℓ_I in a bounded interval, ℰ^C_I ranges over finitely many index sets ([[thm:iii-c1-3-1]]), and
ℓ_I ∉ Re π_1ℰ^C_I avoids their real parts; and ℓ_I ∉ 3/2 + σ_Υ, σ_Υ = {0, (1 − e_Υ)γ_Υ, γ_Υ, 2γ_Υ} ([[def:iii-c-3-1]],
[[prop:iii-i1-3-1]], [[sec:iii-i10-1]]). Threshold: c1–c2, u3–u4, d1.

**n1.** ε, d_1: the smallness and regularity of [[thm:iii-k-4-3]]. Threshold: all the above.

### The parameters: the choice {#sec:vi-c-2}

**Theorem {#thm:vi-c-2-1}** (The parameters can be chosen together.) The conditions of [[sec:vi-c-1]] can be met
together. Make the choices in this order; at each step the thresholds depend only on the choices before it:

(0) ℬ_VI := {|b − b₀| ≤ ε_VI} of [[thm:vi-b1-5-1]]. It depends on the metrics alone.

(1) (v_C, e_C, C_0) := (½, 1/102400, 100) and h ∈ 𝖧, γ_C := h⁻¹. Then [[thm:iii-e-1-1]] holds at these values
([[thm:iv4-2-1]] for (1)–(3), [[thm:iv6-4-1]] for (4)), with (C1)–(C4) (row c3), and (C5) and s_C > 100 hold, as
γ_C > 10⁶.

(2) The gauge. ε_0 of [[prop:iii-d1-4-1]] is uniform. Choose γ_(Υ,H) ∈ (0, ε_0]; this fixes ε_1 and ℬ(γ_(Υ,H)).
Choose e_Υ ∈ (0, min(ε_1, ε_L)); this fixes γ_1 of [[prop:iii-f1-3-3]], which fixes all parameters but γ_Υ and
depends on the orders, hence on γ_C. 𝖹_exc is fixed by step (1). Choose γ_Υ in the interval of row u4 with
4e_Υγ_Υ² ∉ 𝖹_exc. This is possible because the interval is nonempty and open, while {γ > 0 : 4e_Υγ² ∈ 𝖹_exc} is
countable. Then z_Υ ∈ (0, ½], as γ_Υ < ¼ and e_Υ < 1. [[prop:iii-d-6-3]] (the invertibility of the spectral family
of □^Υ_b at |σ| ≥ c_σ) is then implied, for every c_σ and b ∈ ℬ(γ_(Υ,H)), by [[prop:iii-d1-4-1]], which gives it for
every σ with Im σ ≥ 0; so it imposes no further condition.

(3) The data classes: ℰ_0 and ℓ_0 > 3 as in row d1, then ℓ_I in the interval (3, min(ℓ_0, 3/2 + s_C)) of row d2,
minus the four points 3/2 + σ_Υ and the exclusion sets of (H4). This fixes ℰ^C_I ([[thm:iii-c1-3-1]]) and Λ. In the
symmetry class, [[sec:s27-class]] takes ℰ_0 = {(j, 0) : j ≥ 2}, ℓ_0 ∈ (3, 4) and ℓ_I ∈ (3, ℓ_0) ([[eq:vii-0-1]]).

(4) The weights. δ_♯, ε_ind and ε_Υ, all positive, are fixed by step (2). Choose ε_+ < min(δ_♯, ε_ind, ¼, ℓ_I − 3),
decreased for (G⁺) and (Ex1)–(Ex2) (possible: no λ ∈ Λ has real part in (3, 3 + ε_+] for ε_+ small,
[[def:iii-j-g-plus]], and (Ex2) excludes finitely many values in a bounded range, [[lem:iii-j3-1-4]]; (Ex2) involves
ℰ^tot_I and λ_♯, fixed by steps (2)–(3)); then ε_K, decreased for (G) ([[def:iii-i10-1-3]]), which includes
ε_K < ε_Υ; then α as in row w2. (H4) holds as ε_+ < ℓ_I − 3, and decreasing ε_+ keeps rows d1–d2.

(5) The parameter set. The gauge being fixed, take c_σ of [[cor:iii-h-4-3]] (uniform near b₀), then ℬ(c_σ) of
[[prop:iii-f2-4-1]], which fixes the modification parameters first and then allows every c_σ > 0. Let ℬ_* be an open
ball about b₀ whose closure lies in ℬ_VI, in every neighbourhood of row b2, and in ℬ_1, with (B5). These are finitely
many neighbourhoods of b₀, fixed by steps (0)–(4). Balls are taken in the norm |m − m₀| + |A|, |A| the Frobenius norm,
which is invariant under conjugation by O(4), so every parameter ball is O(4)-invariant ([[lem:vii-3-1]] uses this).
[[sec:iii-h2-0]] imposes no lower bound on ℬ_*, so shrinking it is allowed. Every operator family of the stability
theory is then taken over ℬ̄_*, a compact set on which (Dyn) holds (step (0)), as (H5) and its extensions ask. Last,
ℬ_* is shrunk as row b4 asks, which depends on steps (3)–(4) only.

(6) ε and d_1 of [[thm:iii-k-4-3]], which depend on all of the above.

*Proof.* Each step's existence claim is the cited statement, read with the quantifiers it has; the last entry of each
row of [[sec:vi-c-1]] records that no threshold depends on a later choice. In step (2), the ε_0 of [[prop:iii-d1-4-1]]
is uniform, while its ε_1 and ℬ(γ_(Υ,H)) come after γ_(Υ,H), so the order γ_(Υ,H), e_Υ, γ_Υ meets it. The only
low-frequency radius that depends on the gauge is the c_σ of [[cor:iii-h-4-3]], and it is used only after the gauge is
fixed, through [[prop:iii-f2-4-1]], whose neighbourhood is then chosen. In step (5), each neighbourhood of rows b2 and
b4 is open and contains b₀, so their intersection with ℬ_VI contains a ball. The ball of [[thm:vi-b1-5-1]] depends on
no gauge parameter, as the dynamical hypotheses concern the metric alone ([[sec:vi-a-0]]). (K3) holds for every ε
([[prop:vi-b1-3-4]]), so ε_VI depends neither on the regularity d_0 of [[thm:ii-c1-1-1]] nor on its order k. ∎

The invertibility of L̂_b(σ) for b ≠ b₀ and 0 < |σ| < c_σ, which [[sec:iii-f2-5]] leaves open, holds for b near b₀ and
σ ∈ Σ_0, |σ| ≤ c_σ, by [[cor:iii-h-4-3]]; its neighbourhood is one of row b2, so it holds on ℬ̄_*.

### The symmetry class {#sec:s27-class}

*The group.* G := O(2) × O(2) acts on ℝ⁴ = ℝ² × ℝ² by the rotations of the planes (x¹, x²) and (x³, x⁴) and by the
reflections x² ↦ −x² and x⁴ ↦ −x⁴; on spacetime it acts by (t, x) ↦ (t, σx). Every element of O(4), acting so, is an
isometry of every g^KS_(m,0) and fixes every function of (t, |x|). The fixed spaces are

    (ℝ⁴)^G = 0,     𝔰𝔬(4)^G = 0.

Indeed, the torus T² = SO(2) × SO(2) fixes in ℝ⁴ only 0, and in 𝔰𝔬(4), acting by conjugation, exactly
span(W₁₂, W₃₄), the infinitesimal rotations of the two planes (T² is a maximal torus of SO(4), so its fixed subalgebra
is its own Lie algebra); and x² ↦ −x² reverses W₁₂ while fixing W₃₄, x⁴ ↦ −x⁴ reverses W₃₄ while fixing W₁₂.

*The data class.* In the class we take, in step (3) of [[thm:vi-c-2-1]],

    ℰ_0 := {(j, 0) : j ∈ ℕ, j ≥ 2},     ℓ_0 ∈ (3, 4),     ℓ_I ∈ (3, ℓ_0).                               {#eq:vii-0-1}

Row d1 holds: min Re ℰ_0 = 2 > 3/2 + 2γ_Υ, as γ_Υ < ¼ (step (2)); ℰ_0 is closed under sums and positive multiples; and
ℓ_0 > 3 with ℓ_0 ∉ ℕ, so ℓ_0 ∉ Re π_1ℰ_0. Row d2 holds for ℓ_I ∈ (3, min(ℓ_0, 3/2 + s_C)) = (3, ℓ_0), as s_C > 100,
off the discrete exclusion sets of row d2 and of (H4). Step (4) then takes ε_+ < ℓ_I − 3, so (H4) of
[[sec:iii-i10-1]] holds. ε and d_1 are those of [[thm:iii-k-4-3]] (step (6)). For a pair (γ̃, k̃) of symmetric
2-tensors on Σ^IVP, ‖(γ̃, k̃)‖_(d_1) denotes the norm in which [[thm:iii-k-4-3]] measures (γ − γ_(b₀), k − k_(b₀)):
the H^(d_1)-norm of H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b, and ∞ outside these spaces. The weights are those of the
b-density, so that a weight is the pointwise order (the notation of [[ch:s26]]).

**Lemma {#lem:vii-0-1}** (What lies in the class.) Let ρ := |x|⁻¹, and let γ̃, k̃ be smooth symmetric 2-tensors on
Σ^IVP whose Cartesian components lie, on {r ≥ R′}, in ρ²C^∞ and ρ³C^∞ of the radial compactification. Then
‖(γ̃, k̃)‖_(d_1) is finite, and it is bounded by C_(R′) times the sum of the C^(d_1+3)-norms of the components on
{r ≤ 2R′} and finitely many C^∞-seminorms of ρ⁻²γ̃ and ρ⁻³k̃ on the compactified {r ≥ R′}.

*Proof.* Near ρ = 0, Taylor's formula in ρ writes a function of ρ²C^∞ as ρ²a₂(ω) + ρ³a₃(ω) + ρ⁴C^∞. The a_j are
smooth on 𝕊³, and the seminorms of the remainder are bounded by those of ρ⁻²γ̃. The exponents (2, 0) and (3, 0) lie in
ℰ_0 below ℓ_0, and ρ⁴C^∞ ⊂ ρ^(ℓ_0)H^∞_b, as ℓ_0 < 4. Likewise ρ³C^∞ = ρ³a₃ + ρ⁴a₄ + ρ⁵C^∞, with (3, 0) and (4, 0)
in ℰ_0 + 1 below ℓ_0 + 1 < 5. On {r ≤ 2R′} the weights are bounded above and below. ∎

### The nonlinear theorem in the symmetry class {#sec:vii-3}

O(4) acts on M by (t, x) ↦ (t, σx) and on tensors by σ_* := (σ⁻¹)^*. On the components of 𝒟_ex ([[def:iii-j3-1-1]],
[[def:iii-j-1-1]]) it acts as follows: on b = (m, A) ∈ 𝔟 by (m, σAσ⁻¹); on 𝒮_1 ∋ S_w by S_w ↦ S_(σw); on the
coefficient spaces 𝒲_τ, 𝒴_ρ (spaces of harmonics on 𝕊³, 𝒮_1, and 𝒱′ = 0) by their representations; on 𝒱_1, the
rotations, the coefficient space of the rotation rows ([[def:iii-i14-1-3]]), by conjugation V ↦ σVσ⁻¹; and on the
tensor and function components (u^0_λ, f_λ, h̃, and the values of the q-tails) by σ_*.

**Lemma {#lem:vii-3-1}** (Naturality.) Make the following choices O(4)-equivariant.

(C1) *Cut-offs:* χ^♭_K, χ_K, χ^♯_K, χ_IVP, χ^♯_IVP and χ_r of [[sec:iii-b-5]], χ_∞ of [[eq:iii-b-3-6]], χ_ι and χ_9
([[sec:iii-k-0]], [[sec:iii-k-3]]), χ_− ([[def:iii-k-2-1]]), the factor Θ = χ_rχ^♯_IVP(1 − χ^♭_K), and the cut-offs
inside t^♭_* ([[lem:ii-c-3-2]]). Every set in their conditions (the values 0 and 1, the supports, and the nesting of
[[sec:iii-b-5]], each later function equal to 1 near the support of the earlier) is defined by (t, t_*, t_IVP, t^♭_*,
|x|), hence O(4)-invariant. So they are chosen directly, in nesting order, as smooth functions of these and of |x|²:
each is a cut-off between an invariant closed set and the interior of a larger invariant set. No averaging is used;
averaging separately could break the nesting.

(C2) *Gauge 1-forms:* c_Υ, c_(Υ,H), c_C ([[def:iii-b-6-1]], [[sec:iii-e-1]]). They are stationary, lie in |x|⁻¹C^∞ or
are supported in {|x| < 5R₁}, and equal |x|⁻¹dt or |x|⁻¹(dt − v_C d|x|) for large |x|. The proofs use the forms
c_Υ = ζ(|x|)|x|⁻¹dt, c_(Υ,H) = −½χ(|x|)d|x| ([[sec:iii-d2-1]]) and c_C of [[sec:iv4-0]] (that of [[prop:np-10-14]],
whose coefficients are functions of r), which are O(4)-invariant; no averaging is needed.

(C3) *Linear maps given by existence statements:* ω_s1(S) and ω̆(S) ([[prop:iii-d2-3-1]] at b₀, linear in S ∈ 𝒮_1);
the 1-form towers ω̆^i_τ(W), 0 ≤ i ≤ K_τ, of every type τ ∈ 𝒯 ([[prop:iii-d2-3-1]] and [[prop:iii-d3-3-1]] at b₀,
linear in W), for v1 as a map of all of 𝒱_1 and not only of 𝒲_v1 = 𝒱′ = 0, since the rotation rows use it there
([[def:iii-i14-1-3]]); the proofs use these towers themselves, in the term dt_* ⊗_s ω̆^(K_τ)_τ of the rows m_ν and in
the corrections h_ν = −dχ_K ⊗_s ω_ν at every level ([[sec:iii-i9-2]]); the states and towers of the table of
[[sec:iii-g2-1]], as linear maps of the coefficient spaces 𝒴_τ; and the solution operators 𝒮_(λ₀) of
[[sec:iii-j-2]]. Each is a linear map L : V → 𝒯 from an O(4)-representation into tensors. Its conditions are affine
in L and O(4)-invariant: equations with natural operators of g_(b₀), asymptotic or support conditions at faces fixed by
O(4), and prescribed leading terms and right sides given by O(4)-equivariant data (for the towers the leading terms
d(|x|S) for s1, V and (1 + (2/5)γ_Υ)|x|V for v1, χ_∂W̄ for s0 and the model ω̄(Y) for s2, c0, c1,
[[prop:iii-d3-3-1]]), so that an average of solutions is a solution. So

    L^(O(4)) := ∫_(O(4)) σ_* ∘ L ∘ σ⁻¹ dσ

(Haar probability measure) meets them, with the same bounds. The 1-form towers are averaged once, and the towers of
the table of [[sec:iii-g2-1]] at b₀ of the types of 𝒯 are taken as δ*_(g_(b₀)) of the averaged 1-forms, as they are
of the unaveraged ones; the pure-gauge rows outside 𝒯 are δ*-images of 1-forms that (C3) does not name, and the
physical rows are not δ*-images; both are averaged as the maps of 𝒴_τ. One averaged choice serves both names, as
δ*_(g_(b₀)) commutes with the average: δ*_g ω = ½ℒ_(g⁻¹ω) g, and for a diffeomorphism φ,
φ^*(ℒ_X g) = ℒ_(φ^*X)(φ^*g) and φ^*(g⁻¹ω) = (φ^*g)⁻¹(φ^*ω), so φ^*(δ*_g ω) = δ*_(φ^*g)(φ^*ω); every σ ∈ O(4) is an
isometry of g_(b₀), so σ_* δ*_(g_(b₀)) = δ*_(g_(b₀)) σ_*.

(C3′) *Families in b:* the towers and states at b used in h_(b,rem)(q), namely T_(ρ,b), h^(≤1)_(b,s1), h_(b,v1) and
h^(≤2)_(b,v1), chosen smooth in b by [[lem:iii-i14-2-1]]. Replace a family L_b by

    L^(O(4))_b := ∫_(O(4)) σ_* ∘ L_(σ⁻¹·b) ∘ σ⁻¹ dσ.

Then σ_* ∘ L^(O(4))_b ∘ σ⁻¹ = L^(O(4))_(σ·b), and the average keeps the tower relations for L_b (natural, given (C2)),
smoothness in b, the b-independent leading terms, and the value at b₀ once (C3) is applied there. The parameter balls
are O(4)-invariant, being balls in the conjugation-invariant norm of step (5) of [[thm:vi-c-2-1]].

(C4) *The complement 𝒱′* of [[sec:iii-i9-1]], which is 0 at b₀.

Then, for every closed subgroup G′ of O(4), every G′-invariant data (γ, k), every σ ∈ G′ and every small U ∈ 𝒟_ex,

    Φ(σ·U) = σ·Φ(U),     Ψ(σ·U) = σ_*Ψ(U),     P_5(Ψ(σ·U)) = σ_*P_5(Ψ(U)).

The averaged choices are admissible. Each object of (C3) and (C3′) is given by an existence statement, which asserts
that a choice with the conditions listed exists: [[prop:iii-d2-3-1]] for ω_s1(S) and ω̆(S), [[prop:iii-d2-3-1]] and
[[prop:iii-d3-3-1]] for the 1-form towers, the table of [[sec:iii-g2-1]] for the states and towers of the rows, the
step of [[sec:iii-j-2]] for the operators 𝒮_(λ₀), and [[lem:iii-i14-2-1]] for the families in b. The results of
[[ch:s13]]–[[ch:s25]] that use these objects take them as given by those statements, for any choice with the
conditions listed, and so hold for the averaged one. Three
properties used there are not themselves linear conditions, and each is kept. The s1 and v1 states are unique given
their conditions (the zero energy operator is injective at the weights in the gap, [[prop:iii-d2-3-1]]), so the
average is the choice. The bijectivity of [[lem:iii-g2-1-2]] is a statement about leading terms, which are prescribed
by O(4)-equivariant maps onto kernels split by harmonic, and which the average keeps. The isotypic type of each
construction is that of an equivariant map (Schur's lemma).

*Proof.* By induction along the definitions; each object is natural, given (C1)–(C4) and (C3′).

- g_b = Φ_m^*g^KS_(m,A): [[def:iii-b-3-2]] builds r_A, ℓ_A and H_(m,A) from (m, A, x) by matrix operations, which are
  equivariant under x ↦ σx, A ↦ σAσ⁻¹; so σ_*g_((m,A)) = g_((m,σAσ⁻¹)). Φ_m and T_m are radial. So
  g_(b₀,σ·b,−σ·S) = σ_*g_(b₀,b,−S) ([[eq:iii-i-1-1]]) and g_(σ·p⃗) = σ_*g_(p⃗) ([[eq:iii-i7-1-3]]), given the next
  item.

- φ_S = exp V(S_w), V(S_w) = ½ΘX_w, X_w = t w·∂_x + (w·x)∂_t ([[lem:iii-b-5-1]]). So σ_*X_w = X_(σw) and
  σφ_(S_w)σ⁻¹ = φ_(S_(σw)); likewise for the translations ψ_(S_w) of [[eq:iii-i7-1-3]], generated by ½Θ w·∂_x, so
  σφ_(S,S⁰)σ⁻¹ = φ_(σ·S,σ·S⁰) ([[eq:s27-motion]]).

- t_* and t_IVP are functions of (t, |x|), and t^♭_* is a function of (t_*, r): C_♭(t_* + R̃(r)) and t_*F(t_*/r)
  ([[lem:ii-c-3-2]]), given (C1).

- E^Υ_(g_0), E^C_g, Υ^(E_Υ)(g, g_0) = Υ^0(g, g_0) − E^Υ_(g_0)G_(g_0)(g − g_0) and δ*_(g,E_C) ([[def:iii-b-6-1]]) are
  natural in (g, g_0) and the forms of (C2). So are P, P_2–P_5 ([[eq:iii-i9-2-3]], [[eq:iii-i14-1-3]]) and P^♮,
  χ^♮_0 being a function of (t_IVP, |x|, t_*).

- ω̇_b(ḃ) = −(□̂^Υ_b(0))⁻¹η_b(ḃ) and ġ^Υ_b ([[eq:iii-f3-2-1]]) are natural, the inverse being unique.
  w(S) = g_(b₀)(X_S, ·) is natural.

- h_tot and ϑ_tot ([[def:iii-i7-2-3]], [[def:iii-i8-2-1]], [[def:iii-i9-2-1]], [[def:iii-i9-2-3]]) are built from χ_K,
  δ*_(g_(b₀)) and commutators with χ_K, the maps of (C3), w(S), Θ and functions of t_*. h_(b,rem)(q)
  ([[def:iii-i14-1-2]]) is χ_K times h^(≤1)_(b,s1), ġ_b and the towers of (C3′).

- Φ ([[eq:iii-j-2-1]]) is built from χ_ι, u_λ = u^0_λ + res_(z=λ)(t_*^(−z)N_(ι⁺)(z)⁻¹f_λ(z)), with N_(ι⁺) the normal
  operator of a natural operator, h̃, and the corrections h_(λ₀), given by the solution operators 𝒮_(λ₀) and the
  t_*^(−λ₀)-terms of rows and towers ([[sec:iii-j-2]]).

- h_(S,S⁰) ([[prop:iii-k-1-2]]) is the unique solution of [[eq:iii-k-1-2]] with data h⁰_(S,S⁰), h¹_(S,S⁰), the
  restrictions to Σ^IVP of the pull-backs by φ_(S,S⁰) of h_0, the solution with the data h̊_0, h̊_1 of
  [[prop:iii-c2-4-1]]. The proof of [[prop:iii-c2-4-1]] builds these from (γ̃, k̃) and g_(b₀) by setting h̊_0 := γ̃ with
  h̊_0(ν_(b₀), ·) := 0, and by solving tensorial linear equations for the second datum, uniquely. So for G′-invariant
  data and σ ∈ G′, h̊_0, h̊_1 and h_0 are G′-invariant by uniqueness, h^j_(σ·S,σ·S⁰) = σ_*h^j_(S,S⁰), and
  h_(σ·S,σ·S⁰) = σ_*h_(S,S⁰) by uniqueness.

So Ψ(U) = (χ_−h_(−S,−S^(0)_1), 0, 0) + Φ(U) ([[eq:iii-k-2-1]]) and P_5 ∘ Ψ are equivariant. ∎

**Proposition {#prop:vii-3-2}** ([[thm:iii-k-4-3]] in the symmetry class; [Hin26, Theorem 13.1] in the class.) Make
the choices of [[lem:vii-3-1]] equivariant. If the data (γ, k) of [[thm:iii-k-4-3]] are G-invariant, and small for the
threshold ε^G_NM below, its conclusion holds with U fixed by G, b = (m′, 0), S = S⁰ = 0 and g G-invariant.

*Proof.* *The action.* G ⊂ O(4) acts on M by diffeomorphisms that are smooth on the compactification, preserve each
boundary hypersurface (the defining functions of [[eq:iii-b-2-2]] are functions of (t, |x|)), and fix t, t_*, t_IVP and
t^♭_*. So it preserves Σ^IVP, Ω_*, 𝒟, the classes B^k, B^k_η, F^k, F^∞_η of [[sec:iii-k-3]], and the collar of
[[lem:iii-k-3-1]]. Its action on each 𝒟^k_ex and ℱ^k_ex is bounded uniformly in σ, G being compact and acting
smoothly. Replace each norm |·|_k by sup_(σ∈G)|σ·(·)|_k, an equivalent norm. Then G acts isometrically, and every
estimate used below holds with changed constants.

*Fixed spaces.* Let B^(k,G), B^(k,G)_η, F^(k,G) and F^(∞,G)_η be the G-fixed elements. They are closed, and
Π := ∫_G σ dσ (Haar probability measure) is a projection onto them of norm at most 1 that preserves every support
class.

*[[thm:ii-g-2-1]] on the fixed spaces.* (i) ΠS_θ, with S_θ of [[lem:iii-k-3-1]], maps B^(∞,G)_(θ^(−1/2)) into B^(∞,G) and
B^(∞,G)_η into B^(∞,G)_(η−θ^(−1/2)), and satisfies [[eq:ii-g-2-1]] with the constants of the G-sup norms: for
v ∈ B^(∞,G), v − ΠS_θv = Π(v − S_θv), and Π has norm at most 1. (ii) By [[lem:vii-3-1]], U ↦ P_5(Ψ(U)) maps the fixed
part of the domain of [[thm:iii-k-3-2]] into F^(∞,G), and B^(∞,G)_η into F^(∞,G)_η. Differentiability and
[[eq:ii-g-2-2]]–[[eq:ii-g-2-3]] hold by restriction. (iii) For U ∈ B^(∞,G), differentiating P_5(Ψ(σ·V)) = σ_*P_5(Ψ(V)) at
V = U gives D_U(P_5 ∘ Ψ) ∘ σ = σ_* ∘ D_U(P_5 ∘ Ψ), so D_U(P_5 ∘ Ψ) commutes with Π. So Ψ^G_NM(U) := ΠΨ_NM(U) on F^(∞,G)
satisfies D_U(P_5 ∘ Ψ)Ψ^G_NM(U)f = ΠD_U(P_5 ∘ Ψ)Ψ_NM(U)f = Πf = f, and it inherits [[eq:ii-g-2-4]]. It maps F^(∞,G)_η
into B^(∞,G)_η for U in the domain of (ii) and in B^(∞,G)_η, which is what [[thm:ii-g-2-1]] (iii) asks. Indeed, let
f ∈ F^(∞,G)_η, U′ := ℛ(U)f and V := ΠZU′ = Ψ^G_NM(U)f, with Z of the proof of [[thm:iii-k-3-2]]. V ∈ B^(∞,G), and its
boost and translation components vanish, as 𝒮_1^G = 0. Its q-tails lie in {t_* ≥ 17/2} ⊂ {t_* ≥ 8 + c_0η}, as Z and Π
commute (χ_9(t_*) is invariant). On {t^♭_* < T̂ + c_0η}, D_U(P_5 ∘ Ψ)V = Πf = f vanishes; and there U, being fixed, has
S = S^(0)_1 = 0 and tail 0, so, as in the *Supports* part of the proof of [[lem:iii-k-2-3]],
D_U(P_5 ∘ Ψ)V = L_(G_(0,0), g_(b₀))h̃_V with G_(0,0) = g_(b₀) + h_0, the boost and translation components of V vanishing.
The argument there, with [[lem:s27-below]] and [[lem:iii-k-6-1]], gives h̃_V = 0 on {t^♭_* < T̂ + c_0η}. So
V ∈ B^(∞,G)_η. Hence [[thm:ii-g-2-1]] holds on the fixed spaces, with its own threshold ε^G_NM computed from the
constants of the G-sup norms, and gives U ∈ B^(∞,G)_(1/2) with P_5(Ψ(U)) = 0 on Ω_*.

*The metric.* [[prop:iii-k-4-2]] builds g from (h, p⃗, q) = Φ(U), h_(−S,−S^(0)_1) and g_(p⃗). By [[lem:vii-3-1]] every
ingredient is equivariant and U is fixed, so g is G-invariant. U_0 = (b − b₀, S, S^(0)_1) is fixed: 𝔟^G = ℝ × {0} and
𝒮_1^G = 0, 𝒮_1 being ℝ⁴ as a representation. So b = (m′, 0) and S = S^(0)_1 = 0, and [[thm:iii-k-4-3]] (1)–(5) hold
with these values. ∎

### Small final parameters and the rate of settling {#sec:s27-rate}

**Corollary {#cor:s27-rate}** (Small final parameters; the rate on compact sets.) Make the choices of
[[thm:vi-c-2-1]] through the choice of ε_K in step (4). Let ε_m > 0 and ε_t ∈ (0, ε_K); take α in row w2 with
α > 4 + ε_t (possible: the α of row w2 are dense in (4 + ε_K − ε′_0, 4 + ε_K], and 4 + ε_t < 4 + ε_K), and finish
steps (5)–(6). Then there is ε = ε(ε_m, ε_t) > 0, with d_1 as in [[thm:iii-k-4-3]], such that for data as in
[[thm:iii-k-4-3]] of norm below ε:

(a) the conclusion of [[thm:iii-k-4-3]] holds with |b − b₀| < ε_m, |S| < ε_m and |S⁰| < ε_m;

(b) if the data are G-invariant, the conclusion of [[prop:vii-3-2]] holds, with |m′ − m₀| < ε_m;

(c) in either case, for every R′, ε′ > 0 and i, β there are C and T′ such that the Cartesian components of g − g_b, in
the coordinates (t, x) of [[sec:iii-b-2]], satisfy

    |(t_*∂_(t_*))^i ∂^β_x (g − g_b)| ≤ C t_*^(−(α−2)+ε′)     on {r_♭ ≤ r ≤ R′, t_* ≥ T′},              {#eq:s27-rate}

where α − 2 > 2 + ε_K − ε′_0 > 2 ([[def:iii-i10-1-3]]) and α − 2 > 2 + ε_t; with ε′ := α − 4 − ε_t, g − g_b =
O(t_*^(−2−ε_t)) there.

*Proof.* (a) In the proof of [[thm:iii-k-3-2]], apply [[thm:ii-g-2-1]] with its radius δ replaced by min(δ, ε_m): its
hypotheses restrict to the smaller set, and its threshold then depends on ε_m. This gives [[thm:iii-k-4-3]] with
|b − b₀| ≤ ‖U‖_(𝒟^d_ex) ≤ |U|_(3d) < ε_m and |S|, |S⁰| ≤ |U|_(3d) < ε_m, the black hole parameter, the boost and the
translation being components of U, for data of norm below some ε. (b) Take ε moreover below the threshold ε^G_NM of the
run of [[thm:ii-g-2-1]] in [[prop:vii-3-2]], with the radius min(δ, ε_m) there too, through the equivalence of the norms.

(c) Where χ_K = 1, g − g_b = h_tot(p⃗) + h_(b,rem)(q) + h ([[thm:iii-k-4-3]] (4)). h_tot(p⃗) is supported in 𝒞, whose
closure is disjoint from K⁺ ([[lem:iii-i7-2-2]]); so it vanishes on {r ≤ R′} for t_* large, as does 1 − χ_K.
h ∈ 𝒳^∞_(J,ex) has K⁺-order α, and h_(b,rem)(q) has K⁺-order (α − 2)− ([[lem:iii-i14-2-2]] (a) at b₀; at b near b₀,
the rates of [[eq:iii-i14-1-1]], which exceed α − 2, with [[lem:iii-i14-2-1]]). Near the interior of K⁺,
ρ_K = t₀⁻¹ with t₀ = t − |x| ([[eq:iii-b-2-2]]), comparable to t_* on {r ≤ R′}, and the b-vector fields there are
spanned by t_*∂_(t_*) and ∂_x. By b-Sobolev embedding for the b-density μ_b of [[sec:iii-i-1]], as in the proof of
[[lem:iii-i-2-2]] (a weight is then the pointwise order),
(t_*∂_(t_*))^i∂^β_x of a function of K⁺-order w− is O(t_*^(−w+ε′)) for every ε′ > 0. With w = α − 2 this is
[[eq:s27-rate]]. ∎
