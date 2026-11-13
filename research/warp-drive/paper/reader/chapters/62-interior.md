## The interior after the shell {#ch:interior}

[[thm:main]], [[thm:past-construction]] and [[thm:bondi-law]] are made on D_T, on Ω and on the past domain of
[[thm:past-construction]], whose inner boundary r = a lies a fixed distance inside x_K = 1; [[thm:settling]] is stated
outside the black hole. Two regions lie beyond. Inside x_K = 1, where the curvature exceeds the scale l5, nothing is
claimed. The second region is the interior after the time T: q_end ≤ r < μ_end^(1/2), v > v_end + T, below the event
horizon and above the curvature boundary, for all later times. This chapter shows that the development of
[[thm:settling]] (i) covers it. With the inner radius of the stability theory lowered below the curvature boundary,
the development is defined on all of {r ≥ q_end} to the future of its initial surface, for every final mass, its
constants then depending on that mass, and it settles there at the rate of [[thm:settling]] ([[prop:interior]]).
Glued along the part of Σ^IVP between that inner radius and the gluing radius, where the two induce the same data, it
and g_λ form one vacuum spacetime for λ small, and the two developments of those data are isometric on their maximal
common globally hyperbolic development, which contains a neighbourhood of that part and whose reach is left open
([[lem:interior-one-spacetime]]). The last section locates the first step towards the continuation of g_λ's own
data, the past domain of dependence of the far part of the initial surface ([[lem:interior-far-part]]), and defines a
data class wider than that of [[thm:settling]] (ii) by half-integer orders ([[def:half-class]]), in which
[[ch:own-data]] proves that the development of g_λ's own data settles.

*Notation.* b₀ := (μ_end, 0), so that the mass m₀ of the stability theory is μ_end and R₁ = μ_end^(1/2) = r_h, the radius
of the horizon of g_(b₀). q_end := (√72 μ_end l5²)^(1/4) is the radius of the curvature boundary x_K = 1 of the
background after the shell ([[sec:domain]]); as μ_end ≥ μ0 ≥ √72 l5², q_end ≤ R₁. The inner radius r_♭ ∈ (0, ½R₁], the
spacetime M of [[eq:iii-b-2-1]], its coordinates (t, x), the functions T_m, ψ and ψ_IVP, the time functions t_* and
t_IVP, the initial surface Σ^IVP := t_IVP⁻¹(0) and the radius R₃ beyond which t_IVP = t − C″ are those of [[ch:s11]]
([[eq:iii-b-3-3]], [[eq:iii-b-3-6]], [[lem:iii-b-3-7]]). Since ψ_IVP = ψ on [r_♭, 5R₁] and ψ′ > 0 on [3R₁, ∞), R₃ ≥ 5R₁.
Ω_*, t^♭_* and T̂ are those of [[sec:iii-k-0]] and [[prop:iii-k-1-2]], and 𝒟_0 := 𝒟_(0,0) is the region 𝒟_(S,S⁰) of
[[prop:iii-k-1-2]] at (S, S⁰) = (0, 0); φ_(0,0) = ψ_0 ∘ φ_0 ([[eq:s27-motion]]) is the identity, its factors being the
time-1 flows of the vector fields V(0) and V⁰(0) of [[lem:iii-b-5-1]] and [[lem:iii-i7-1-1]] (a), which are zero, these
fields being linear in S. The domain Ω′ of the form [[eq:omega]] with constants (T′, δ′_0), a′ := q0 − δ′_0,
V′ := v_end + T′ and τ′_end := max_(v ≤ V′)(v − r_q(v)), the constant c₀ of the chart
(t, x) = (τ + T_(μ_end)(|x|) + c₀, x), which places Σ^IVP in the coordinates (τ, x) of [[sec:background]], and the
gluing radius R ≥ R₃ are those of [[lem:vii-1-2]] and [[thm:settling-precise]]; Ω′_+ := Ω′ ∩ {v ≥ v_end + 1}.
G = O(2) × O(2) is the group of [[sec:s27-class]].

### The development inside the black hole {#sec:interior-development}

On {|x| ≤ 2R₁}, χ_∞ = 0, so T_m is constant and ψ′ = 1 there: g_(b₀) is the Kerr–Schild Tangherlini metric
η + (μ_end/r²)(dt + dr)² translated in time, and dt_* = dt − dr. With f := 1 − μ_end/r², its inverse has
g⁻¹(dr, dr) = f, g⁻¹(dt, dr) = μ_end/r² and g⁻¹(dt, dt) = −1 − μ_end/r² ([[lem:iii-b-3-3]] (d)). Hence

    g⁻¹(dt − dr, dt − dr) = −1 − 3μ_end/r² + f = −4μ_end/r² < 0,

so the level sets of t_* are spacelike at every r ∈ (0, 2R₁]. The time orientation is the one in which dt_* is past
timelike; g⁻¹(dt, dt_*) = −1 − 2μ_end/r² < 0, so dt is past timelike too. On 0 < r < r_h, f < 0 and dr is timelike,
and g⁻¹(dt, dr) > 0 puts it in the cone opposite to dt: dr is future timelike, and r decreases along future causal
curves. At every inner radius r_♭ ≤ ½R₁,

    f(r_♭) = 1 − μ_end/r_♭² ≤ 1 − 4 = −3,

so the inner boundary {r = r_♭} of M is spacelike, for every final mass.

The stability theory is written for every inner radius r_♭ ∈ (0, ½R₁] ([[ch:s11]], [[def:s12-radii]], [[ch:s14]],
[[ch:s27]]); in [[ch:s14]] the inner radius r_♯ of the analysis near the black hole is r_♭ ([[sec:iv5-0]]). One
explicit fact at small radii is the sign of the damping 1-form, which [[prop:np-10-14]] gives at m = 1: (i) at every
r > 0, and (ii) on (0, 99.375], which ends just inside the saddle point r_0 = 100 of the 1-form. The next lemma writes
out the inequalities on the inner piece of the 1-form, all of them strict.

**Lemma {#lem:interior-damping}** (The damping 1-form inside half the horizon radius.) Let m = 1, so that r_h = 1 (the
case μ_end = 1), let g and c be as in [[prop:np-10-14]], and e its constant. On the piece 0 < r ≤ 50 of
[[eq:s14-cform]], c = α(dt + ¼ dr) with α = 1/200, and for every r in (0, 50]

    g⁻¹(c, c) = α²(−3/2 + (9/16) f) < 0,    g⁻¹(c, dt) = α(−7/4 + (3/4) f) < −α,    g⁻¹(c, dr) = α(¼ + (3/4) r⁻²) > 0;

on 0 < r < r_h = 1, moreover, f e g⁻¹(c, c) + 2(1 − e) g⁻¹(c, dr)² > 0. These are (i) and (ii) of [[prop:np-10-14]] on
(0, r_h/2], and ℓ(−dr) is negative definite there ([[prop:np-10-13]] (i)). By scaling, the same holds at every mass.

*Proof.* With g^(tt) = −(2 − f), g^(tr) = 1 − f and g^(rr) = f, a form c = α(dt + b dr) has
α⁻²g⁻¹(c, c) = −2 + 2b + f(1 − b)², α⁻¹g⁻¹(c, dt) = −(2 − b) + f(1 − b) and α⁻¹g⁻¹(c, dr) = 1 − f + fb. At b = ¼
these are −3/2 + (9/16)f, −7/4 + (3/4)f and 1 − (3/4)f = ¼ + (3/4)r⁻². As f < 1, the first is below −3/2 + 9/16 < 0
and the second below −1; so c is timelike and in the cone of dt, which is past, and r c is past timelike. The third is
positive at every r > 0. On 0 < r < 1, f < 0, so f e g⁻¹(c, c) > 0, and 2(1 − e) g⁻¹(c, dr)² > 0. ∎

**Proposition {#prop:interior}** (The development reaches the curvature boundary inside the black hole.) Let the
constants be as in [[thm:settling]], and take the inner radius of the stability theory to be

    r_♭ := ½ min(R₁, q_end) = ½ q_end.

Then for λ ≤ λ1 the G-invariant vacuum development g of [[thm:settling]] (i) is defined on

    M ∩ {t_IVP ≥ 0} = {|x| ≥ r_♭, t_IVP ≥ 0} ⊃ {r ≥ q_end, t_IVP ≥ 0},

the whole coordinate region outside the curvature boundary x_K = 1 of the background after the shell, to the future of
Σ^IVP, for all later times. Its data on Σ^IVP differ from those of g_(b₀) by at most Cλ in the norm of
[[thm:iii-k-4-3]], and for every R′ and i, β there are C and T_1 with

    |(t_*∂_(t_*))^i ∂^β_x (g − g_(m′,0))| ≤ C t_*^(−2−ε)     on {q_end ≤ r ≤ R′, t_* ≥ T_1},

m′ and ε being those of [[thm:settling]]. This holds for every final mass μ_end; λ1, δ and the constants depend on
r_♭, hence on μ_end. The part {r_♭ ≤ r < q_end} of the domain lies beyond the curvature boundary.

*Proof.* *The inner radius.* r_♭ ∈ (0, ½R₁] since q_end ≤ R₁, and [[thm:settling-precise]] holds at every such
inner radius, its choices depending on r_♭ ([[sec:vii-4]]); its g is the development of [[thm:settling]] (i). The
stability theory it rests on is written at every r_♭ ∈ (0, ½R₁] ([[ch:s11]], [[def:s12-radii]], [[ch:s14]],
[[ch:s27]]), the inner radius r_♯ of [[sec:iv5-0]] being r_♭. The radius enters it through choices of small
constants, which exist at every r_♭ > 0 and depend on it, and through four facts at the inner radius, each of which
holds at r_♭: the Kerr–Schild family is defined on {|x| ≥ ½r_♭} ([[lem:s11-ks-domain]]); ψ ≥ 0, and dt_* and dt_IVP
are timelike on {|x| ≥ r_♭} ([[lem:iii-b-3-7]]); dr is future timelike inside the horizon for g_(b₀), as shown above,
and for b near b₀ uniformly on the compact {½r_♭ ≤ r ≤ ¾R₁}, by continuity in b ([[lem:iv5-0-3]] (c)); and the damping
1-form has the signs of [[prop:np-10-14]] (i)–(ii) for g_(b₀) on all of (0, r_h/2], which contains the collar down to
½r_♭ ([[prop:np-10-14]], [[lem:interior-damping]]), and, the inequalities being strict there, for b near b₀ by
continuity in b: (i) on the compact {½r_♭ ≤ r ≤ ½r_h} ([[sec:iv5-0]]) and (ii) on {r_♭ ≤ r ≤ ½r_h}
([[lem:iv5-0-5]]). [[lem:vii-1-2]] takes δ′_0 in (max(0, q0 − ½r_♭), q0), which is not empty, so that
a′ = q0 − δ′_0 < ½r_♭; [[thm:main]] holds on such an Ω′.

*The domain.* g is defined on Ω_* ∪ 𝒟_0 ([[thm:settling-precise]] (i)). This set is M ∩ {t_IVP ≥ 0}. Indeed,
t^♭_* ≤ t_* ≤ t_IVP where t^♭_* is defined ([[sec:iii-k-0]]), so Ω_* = cl_M{t^♭_* ≥ 1} lies in {t_IVP ≥ 1}; and a
point of M with t_IVP ≥ 0 lies in 𝒟_0 = {t_IVP ≥ 0} ∩ {t^♭_* ≤ T̂ + 2} or in {t^♭_* > T̂ + 2} ⊂ Ω_*. Since t_IVP ≤ t,
t_IVP ≥ 0 implies t ≥ 0 ≥ −½|x|, so M ∩ {t_IVP ≥ 0} = {|x| ≥ r_♭, t_IVP ≥ 0}. As r_♭ = ½q_end < q_end, it contains
{r ≥ q_end, t_IVP ≥ 0}.

*The data and the rate.* G-invariance, Ric(g) = 0 and the bound on the data are [[thm:settling-precise]] (i), and the
rate is [[eq:vii-0-2]] with ε_t := ε, its threshold time written T_1 here, on {r_♭ ≤ r ≤ R′, t_* ≥ T_1}, which
contains {q_end ≤ r ≤ R′, t_* ≥ T_1}. ∎

**Remark {#rem:interior-condition}** (At the inner radius ½R₁.) With the inner radius ½R₁ the development already
covers {r ≥ q_end} exactly when q_end ≥ ½R₁, that is when

    μ_end ≤ 16√72 l5² ≈ 135.76 l5²:                                                             {#eq:interior-condition}

q_end ≥ ½μ_end^(1/2) ⟺ √72 μ_end l5² ≥ μ_end²/16 ⟺ [[eq:interior-condition]]. At the numerical point of
[[ch:lambda0]] (μ0 = 1, l5 = 1/10, A = 1, ∫ env² = 105/128), [[eq:mu-rate]] gives μ_end = 1 + (2/9)(105/128) =
227/192 ≈ 118.2 l5², and [[eq:interior-condition]] holds with a margin of about 17.5 l5²: μ_end² = 51529/36864 < 1.4,
while 256 · 72 l5⁴ = 1.8432. For a seed μ0 = 1000 l5², μ_end ≥ μ0 > 16√72 l5² and [[eq:interior-condition]] fails;
[[prop:interior]] covers both.

### One spacetime across the common part of the initial surface {#sec:interior-one-spacetime}

g is the development of the glued data (γ_λ, k_λ) of [[thm:settling]] (i), which equal the data of g_λ on
Σ^IVP ∩ {r ≤ R} and the data of the Tangherlini metric g^KS_(m_λ,0) on Σ^IVP ∩ {r ≥ 4R} ([[cor:vii-2-3]],
[[ch:after-shell]]). On Σ^IVP ∩ {r_♭ < r < R}, g and g_λ induce the same data, so near it they are vacuum
developments of the same data. [[lem:interior-one-spacetime]] makes this precise, without deciding how far their
identification reaches; it makes g_λ, near the hole just before Σ^IVP, and g, after Σ^IVP, one vacuum spacetime. Its
proof compares g_λ with g_(b₀) on a neighbourhood of Σ^IVP ∩ {r_♭ ≤ r ≤ R}, which reaches below r_♭, outside the set
on which [[lem:vii-1-2]] (a) is stated. The next lemma gives that comparison; its part (a) is [[lem:vii-1-2]] (a) on a
larger set, and the proof of (a) there extends to it, its formula holding at every r > 0.

**Lemma {#lem:interior-chart}** (The Tangherlini metric in the chart of [[lem:vii-1-2]].) In the chart
(t, x) = (τ + T_(μ_end)(|x|) + c₀, x) of [[lem:vii-1-2]]:

(a) the Tangherlini metric g^KS_(μ_end,0) = η + (μ_end/r²)(dτ + dr)² of [[lem:vii-1-1]] is g_(b₀) on
ℝ_t × {|x| ≥ ½r_♭}, and g0 = g_(b₀) on {v ≥ v_end, |x| ≥ ½r_♭};

(b) with C_J and λ_1 those of [[lem:vii-1-1]], the components of g_λ − g_(b₀) in the chart are at most 25C_Jλ on
Ω′_+ ∩ {|x| ≥ ½r_♭} for 0 < λ ≤ λ_1; and for every compact set Q ⊂ Ω′_+ ∩ {|x| ≥ ½r_♭} there are C_Q and λ_Q > 0 such
that the components of g_λ⁻¹ − g_(b₀)⁻¹ in the chart are at most C_Qλ on Q for 0 < λ ≤ λ_Q.

*Proof.* (a) The map (t, x) ↦ (τ, x) is the map Φ_(μ_end)(t, x) = (t − T_(μ_end)(|x|), x) of [[eq:iii-b-3-3]]
followed by the translation τ ↦ τ − c₀. T_(μ_end) is smooth on [0, ∞) and constant on [0, 2R₁], so this is a
diffeomorphism of ℝ × (ℝ⁴ ∖ 0). The coefficients of g^KS_(μ_end,0) do not depend on τ, so the translation preserves it,
and in the chart g^KS_(μ_end,0) is Φ_(μ_end)*g^KS_(μ_end,0), which [[eq:iii-b-3-3]] defines as g_(b₀) on
ℝ_t × {|x| ≥ ½r_♭}. On {v ≥ v_end}, μ = μ_end, and g0 = η + (μ_end/r²) dv ⊗ dv with dv = dτ + dr ([[eq:background]]),
which is g^KS_(μ_end,0) at every r > 0.

(b) By [[lem:vii-1-1]] with j = 0, the components of g_λ − g^KS_(μ_end,0) in the coordinates (τ, x) are at most C_Jλ
on Ω′_+ for 0 < λ ≤ λ_1. In the chart, dτ = dt − T′_(μ_end)(|x|) x̂ · dx and the dxⁱ are unchanged, and
|T′_(μ_end)(ϱ)| = 2χ_∞(ϱ)μ_end/(ϱ² − μ_end) ≤ 2/3, as ϱ² ≥ 4μ_end on the support of χ_∞; so every entry of this change of
basis has absolute value at most 1, and a component in the chart is a sum of at most 25 components in (τ, x), each
multiplied by two such entries. With (a) this gives the first bound. On Q, g_(b₀)⁻¹ is continuous, so the operator norm
of its matrix is at most some B_Q. Let E be the matrix of g_λ − g_(b₀); its operator norm is at most 125C_Jλ, five
times its largest entry. For λ ≤ λ_Q := min(λ_1, (250C_JB_Q)⁻¹), g_(b₀)⁻¹E has operator norm at most ½, so
g_λ = g_(b₀)(I + g_(b₀)⁻¹E) is invertible, with g_λ⁻¹ of operator norm at most 2B_Q by the Neumann series, and
g_λ⁻¹ − g_(b₀)⁻¹ = −g_λ⁻¹Eg_(b₀)⁻¹ has operator norm, and so components, at most C_Qλ with C_Q := 250C_JB_Q². ∎

**Lemma {#lem:interior-one-spacetime}** (One vacuum spacetime.) Let Σ := Σ^IVP ∩ {r_♭ < r < R}, with the data (γ, k)
that g_λ and g both induce on it; in the chart of [[lem:vii-1-2]] Σ is one set for both metrics, and the sets A and B
below lie in the coordinate space ℝ × ℝ⁴ of that chart. Let λ ≤ λ1 be so small, depending on R and Ω′, that dt_IVP,
with ψ_IVP continued below r_♭ by ψ′_IVP = 1, is timelike for g_λ and in the cone of dτ on a connected open
neighbourhood of the closure Σ̄ in Ω′_+ (such λ exist, see the proof), and let V ⊂ Ω′_+ be such a neighbourhood,
time-oriented as on Ω′, so that dt_IVP is past timelike on V. Let D_V(Σ) be the Cauchy development of Σ in (V, g_λ)
([[thm:std-bgp-development]]), and put

    A := D_V(Σ) ∩ {t_IVP ≤ 0}  with g_λ,     B := {|x| > r_♭, t_IVP > 0} ∪ Σ  with g.

B is the domain M ∩ {t_IVP ≥ 0} of g with the points of Σ^IVP ∖ Σ and of {|x| = r_♭} removed. B is time-oriented as
the development of its data on Σ^IVP, so that the unit normal of Σ pointing into B is future directed; this is the
orientation in which g induces k on Σ. A and B are manifolds with boundary, the boundary of each being Σ (see the
proof), and (i) glues them along the whole of it. The points of Σ^IVP ∖ Σ and of {|x| = r_♭} are left out of B
because the glued space would have boundary points there, and at the edge of Σ it would not be a manifold.

(i) The space M_gl := (A ⊔ B)/∼, gluing Σ ⊂ A to Σ ⊂ B by the identity, is a connected, smooth, Hausdorff,
time-oriented vacuum spacetime, equal to (A, g_λ) and (B, g) away from Σ. Σ is a smooth spacelike hypersurface of
M_gl, on which its metric induces (γ, k).

(ii) Σ is acausal in M_gl and in V, and its Cauchy developments D_(M_gl)(Σ) and D_V(Σ) are globally hyperbolic
developments of (Σ, γ, k) in the sense of [Sbi15, Definition 2.1] ([[thm:std-sbierski]] (1)). Their maximal common
globally hyperbolic development U ⊂ D_(M_gl)(Σ) contains a neighbourhood of Σ; there is a time-orientation-preserving
isometric embedding j : U → D_V(Σ), the identity on Σ, so that on U the metric of M_gl and g_λ agree up to j; and the
two developments glued along U by j form one Hausdorff globally hyperbolic development of (Σ, γ, k).

*Proof.* *V exists.* Σ̄ = Σ^IVP ∩ {r_♭ ≤ r ≤ R} is compact and connected, a graph over the closed shell
{r_♭ ≤ |x| ≤ R}, and lies in the interior of Ω′_+ ([[lem:vii-1-2]] (b)). dt_IVP is timelike for g_(b₀) on
{|x| ≥ ½r_♭}: on {|x| ≥ r_♭} by [[lem:iii-b-3-7]] (b), and on {½r_♭ ≤ |x| ≤ r_♭}, where ψ′_IVP = ψ′ = 1, as for t_*
after [[lem:iii-b-3-7]]. In the Kerr–Schild coordinates, with τ = t_KS − c₀, dt_IVP = dt_KS − β dr with β ∈ (−1, 1],
and g_(b₀)⁻¹(dt_KS, dt_IVP) = −1 − H(1 + β) < 0, H = μ_end r⁻² ([[lem:iii-b-3-3]] (d)); so dt_IVP lies in the cone of
dτ. By compactness and continuity there are c_V, δ_V > 0 such that the closed coordinate δ_V-neighbourhood Q of Σ̄ lies
in the interior of Ω′_+ ∩ {|x| > ½r_♭}, and g_(b₀)⁻¹(dt_IVP, dt_IVP) and g_(b₀)⁻¹(dτ, dt_IVP) are at most −2c_V on Q.
Q is compact, so by [[lem:interior-chart]] (b) the components of g_λ⁻¹ − g_(b₀)⁻¹ are at most C_Qλ on Q. So for
λ small, depending on c_V and Q and hence on R and Ω′, the two quantities, in which dt_IVP and dτ have components
bounded on Q, are at most −c_V for g_λ on Q. Let V be the open δ_V-neighbourhood of Σ̄; it is connected, the union of
balls each meeting the connected set Σ̄. So this V is one such neighbourhood as the statement asks for. On any such V,
dt_IVP is timelike for g_λ and in the cone of dτ, which is past: Ω′ is time-oriented by dτ, which is timelike for g_λ
([[lem:domain]] (e) on Ω′, with item 4 of [[thm:main]]). So t_IVP increases strictly along future causal curves of
(V, g_λ).

*Σ in V.* Σ = V ∩ {r_♭ < |x| < R, t_IVP = 0} is an open subset of a level set of t_IVP, whose differential does not
vanish; so Σ is a smooth hypersurface of V, spacelike as dt_IVP is timelike, and acausal, as t_IVP increases strictly
along future causal curves. By [[thm:std-bgp-development]], D_V(Σ) is an open subset of V containing Σ, globally
hyperbolic, with Σ as a Cauchy hypersurface. Moreover D_V(Σ) ∩ {t_IVP = 0} = Σ: an inextendible causal curve through a
point p of D_V(Σ) meets Σ, and t_IVP increases strictly along it, so that if t_IVP(p) = 0 it meets Σ at p.

*A and B are manifolds with boundary Σ.* As D_V(Σ) is open in V and dt_IVP ≠ 0, A = D_V(Σ) ∩ {t_IVP ≤ 0} is a
manifold with boundary D_V(Σ) ∩ {t_IVP = 0} = Σ, and A ∖ Σ = D_V(Σ) ∩ {t_IVP < 0} is open in V. B ∖ Σ =
{|x| > r_♭, t_IVP > 0} is open in ℝ × ℝ⁴. A point of Σ has an open neighbourhood N ⊂ {r_♭ < |x| < R}, on which
N ∩ {t_IVP = 0} = N ∩ Σ^IVP ⊂ Σ, so that B ∩ N = N ∩ {t_IVP ≥ 0}; as dt_IVP ≠ 0, B is a manifold with boundary Σ. g is
smooth on B up to Σ, which is spacelike for it, γ being Riemannian. As A ⊂ {t_IVP ≤ 0} and B ⊂ {t_IVP ≥ 0},
A ∩ B = Σ.

*(i), the topology.* The inclusions of A and B into ℝ × ℝ⁴ agree on Σ, so they define a continuous injective map from
M_gl onto A ∪ B. It is open. Indeed, A = (A ∪ B) ∩ {t_IVP ≤ 0} and B = (A ∪ B) ∩ {t_IVP ≥ 0} are closed in A ∪ B; so if
S ⊂ A ∪ B meets A and B in relatively open sets, (A ∪ B) ∖ S is the union of the closed sets A ∖ S and B ∖ S, and S is
open in A ∪ B. We identify M_gl with A ∪ B by this homeomorphism. Then M_gl is Hausdorff and second countable, and
A ∖ Σ = M_gl ∩ {t_IVP < 0} and B ∖ Σ = M_gl ∩ {t_IVP > 0} are disjoint open subsets of it, covering M_gl ∖ Σ, which
carry the smooth structures of V and of ℝ × ℝ⁴ and the metrics g_λ and g. The smooth structure across Σ is the one
constructed next, not that of the coordinates (t, x): g_λ and g need not agree as matrices on Σ.

*(i), the charts at Σ.* Let n_λ and n be the future unit normals of Σ for g_λ and g. Then dt_IVP(n_λ) > 0, as dt_IVP
is past timelike for g_λ on V, and dt_IVP(n) > 0, as n points into B. In the chart, Σ is the graph t = ψ_IVP(|x|) over
the open shell {r_♭ < |x| < R}, so the coordinates x = (x¹, …, x⁴) of the chart, restricted to Σ, are coordinates on all
of Σ; every chart below uses them. Let p ∈ Σ, and let Π_0 be a neighbourhood of p in Σ. Near p, g is the restriction to
B of a smooth Lorentzian metric g̃ on an open set of ℝ × ℝ⁴, g being smooth up to Σ. The maps

    E_λ(s, x) := exp^(g_λ)_x(s n_λ),     Ẽ(s, x) := exp^(g̃)_x(s n)

are defined and smooth near (0, p) in ℝ × Π_0, and their differentials at (0, p) map (σ, ξ) ∈ ℝ × T_pΣ to σn_λ + ξ
and to σn + ξ, which are isomorphisms, n_λ and n being transverse to Σ. By the inverse function theorem there are an
open neighbourhood Π ⊂ Π_0 of p and s_0 > 0 such that E_λ and Ẽ map (−s_0, s_0) × Π diffeomorphically onto open sets
O_λ ⊂ D_V(Σ) and O ⊂ {r_♭ < |x| < R}, and such that ∂_s(t_IVP ∘ E_λ) > 0 and ∂_s(t_IVP ∘ Ẽ) > 0 there, these being
dt_IVP(n_λ) and dt_IVP(n) at s = 0. Since t_IVP vanishes at s = 0, t_IVP ∘ E_λ and t_IVP ∘ Ẽ have the sign of s. So
E_λ maps (−s_0, 0] × Π onto O_λ ∩ {t_IVP ≤ 0} = O_λ ∩ A, and Ẽ maps [0, s_0) × Π onto O ∩ {t_IVP ≥ 0} = O ∩ B, with
O ∩ Σ = Π. For 0 ≤ s < s_0 the g̃-geodesic σ ↦ Ẽ(σ, x), σ ∈ [0, s], lies in B, where g̃ = g; so Ẽ(s, x) =
E(s, x) := exp^g_x(s n) there, whatever the extension g̃. Put

    Φ_Π(s, x) := E_λ(s, x)  (−s_0 < s ≤ 0),     Φ_Π(s, x) := E(s, x)  (0 ≤ s < s_0),

both being x at s = 0. Φ_Π is a bijection from (−s_0, s_0) × Π onto W_Π := (O_λ ∩ A) ∪ (O ∩ B), which is open in
M_gl, since W_Π ∩ A = O_λ ∩ A and W_Π ∩ B = O ∩ B are open in A and in B. Φ_Π is continuous on the closed halves
{s ≤ 0} and {s ≥ 0}, and its inverse on the closed pieces W_Π ∩ A and W_Π ∩ B; so Φ_Π is a homeomorphism. On {s < 0}
and on {s > 0} it is a diffeomorphism onto the open subsets O_λ ∩ (A ∖ Σ) of A ∖ Σ and O ∩ (B ∖ Σ) of B ∖ Σ.

*(i), the smooth structure.* Two charts Φ_Π and Φ_Π′ of this kind are given by the same formulas where both are
defined, both using the coordinates x on Σ. Let (s, x) lie in the domain of Φ_Π′⁻¹ ∘ Φ_Π. If s ≠ 0, this map is smooth
near (s, x), as both charts are diffeomorphisms onto open subsets of A ∖ Σ, or both of B ∖ Σ, there. If s = 0, then
x ∈ Π ∩ Π′, and Φ_Π = Φ_Π′ on a neighbourhood N of (0, x) contained in both domains. Φ_Π′⁻¹ ∘ Φ_Π is continuous and
fixes (0, x), so it maps a smaller neighbourhood N′ ⊂ N into N, and for y ∈ N′, Φ_Π′(Φ_Π′⁻¹Φ_Π(y)) = Φ_Π(y) = Φ_Π′(y),
whence Φ_Π′⁻¹Φ_Π(y) = y, Φ_Π′ being injective. So the transition maps are smooth, and the charts Φ_Π, with the charts
of A ∖ Σ and of B ∖ Σ, form a smooth atlas of M_gl, a five-dimensional manifold without boundary. A ∖ Σ and B ∖ Σ are
open submanifolds of it, and Σ, which is {s = 0} in every chart Φ_Π, is a smooth embedded hypersurface.

*(i), the metric.* s ↦ E_λ(s, x) and s ↦ E(s, x) are geodesics of g_λ and of g with unit timelike tangent, equal to
n_λ and n at s = 0. So E_λ^*g_λ = −ds² + h^λ_s on (−s_0, 0] × Π and E^*g = −ds² + h_s on [0, s_0) × Π, with
Riemannian metrics h^λ_s and h_s on Π: along a unit timelike geodesic g(∂_s, ∂_s) = −1, and for a coordinate field ∂_i
of Π, ∂_s g(∂_s, ∂_i) = g(∂_s, ∇_(∂_s)∂_i) = g(∂_s, ∇_(∂_i)∂_s) = ½∂_i g(∂_s, ∂_s) = 0, with g(∂_s, ∂_i) = 0 at s = 0.
At s = 0, h^λ_0 = h_0 = γ, and ∂_s h^λ_0 = ∂_s h_0: ∂_s g(∂_i, ∂_j) = g(∇_(∂_i)∂_s, ∂_j) + g(∂_i, ∇_(∂_j)∂_s) is at
s = 0 twice the form (X, Y) ↦ g(∇_X ν, Y) on the tangent spaces of Σ, ν being the future unit normal, n_λ resp. n,
which ∂_s is at s = 0. The form is symmetric: for vector fields X, Y tangent to Σ, g(∇_X ν, Y) = −g(ν, ∇_X Y), and
∇_X Y − ∇_Y X = [X, Y] is tangent to Σ. It is the second fundamental form up to the sign of its convention, so it is
the same for both metrics, both inducing k. The metric −ds² + h_s has the Christoffel symbols Γ^s_ij = ½∂_s h_ij,
Γ^i_sj = ½h^ik ∂_s h_kj and Γ^i_jk those of h_s, the others vanishing; so the spatial components of its Ricci tensor are

    R_ij = ½∂_s²h_ij + Ric(h_s)_ij + ¼(h^kl ∂_s h_kl) ∂_s h_ij − ½h^kl ∂_s h_ik ∂_s h_jl.

Ric = 0 therefore reads ∂_s²h = F(h, ∂_s h, ∂_x h, ∂_x²h), with
F := −2 Ric(h) − ½(h^kl ∂_s h_kl) ∂_s h + (∂_s h)h⁻¹(∂_s h) a universal expression, polynomial in h⁻¹, h, ∂_s h and the
first and second x-derivatives of h. Differentiating m times in s makes ∂_s^(m+2)h at s = 0 a universal expression in the
∂_s^j h, j ≤ m + 1, and their x-derivatives. By induction on m, from h^λ_0 = h_0 and ∂_s h^λ_0 = ∂_s h_0, ∂_s^m h^λ and
∂_s^m h agree at s = 0 for every m, with all their x-derivatives. So H := h^λ on s ≤ 0 and h on s ≥ 0 has one-sided
partial derivatives of every order which agree at s = 0. By induction on the order, every partial derivative of H exists,
the one-sided difference quotients in s having the same limit at s = 0, and it is continuous; so H is C^∞. The metric
−ds² + H is then smooth on (−s_0, s_0) × Π, Ricci-flat on s ≠ 0, and so on s = 0 as well, Ric depending continuously
on two derivatives. As the transition maps between the Φ_Π are the identity near Σ, these metrics, g_λ on A ∖ Σ and g
on B ∖ Σ, form one smooth Ricci-flat Lorentzian metric g_gl on M_gl. On Σ = {s = 0} it induces the metric H_0 = γ, and
its form (X, Y) ↦ g_gl(∇_X ∂_s, Y) there is ½∂_s H_0 = ½∂_s h_0, the form of g; so it induces the second fundamental
form k, as g does.

*(i), time orientation and connectedness.* Along each geodesic s ↦ Φ_Π(s, x) the tangent ∂_s is timelike and
continuous, so it stays in the cone of its value n_λ, resp. n, at s = 0: ∂_s is future directed for g_λ on s < 0 and
for g on s > 0. The future cones of g_λ on A ∖ Σ, of g on B ∖ Σ and the cones of ∂_s on the sets W_Π therefore agree
where these sets overlap, and define a time orientation of g_gl, in which the unit normal ∂_s of Σ is future.
B ∖ Σ = {|x| > r_♭, t > ψ_IVP(|x|)} is connected, the region above the graph of a continuous function over the
connected set {|x| > r_♭} ⊂ ℝ⁴, and B lies in its closure; so B is connected. For A, and for later use: let S be an
acausal set in a time-oriented Lorentzian manifold N, p ∈ D_N(S), and c an inextendible future causal curve through p
meeting S at q, say with p before q (the other case is the same with past and future exchanged). Then every point y
of c between p and q lies in D_N(S). Indeed, for an inextendible causal curve c′ through y, the curve formed by c up to
y and the future half of c′ from y is causal, inextendible and passes through p, so it meets S; c meets S only at q,
S being acausal, and q follows y; so c′ meets S. In V, through a point p of A ∖ Σ passes an inextendible timelike
geodesic of g_λ, which meets Σ at a point q, after p as t_IVP(p) < 0 = t_IVP(q). Every point of it between p and q
lies in D_V(Σ) and has t_IVP ≤ 0, so it lies in A. So every point of A is joined to the connected set Σ in A, and A is
connected; M_gl = A ∪ B, with A ∩ B = Σ ≠ ∅, is connected. Every point of D_(M_gl)(Σ) and of D_V(Σ) is joined to Σ
within it in the same way, so these two sets are connected too.

*(ii).* In V, Σ is acausal (above). In M_gl, let c be a future causal curve with c(0) ∈ Σ. In each chart Φ_Π, ds is
timelike, as g_gl⁻¹(ds, ds) = −1, and past, as its metric dual is −∂_s; so s increases strictly along future causal
curves. So c lies in {s > 0} ⊂ B ∖ Σ just after the parameter 0, and if c meets Σ at a parameter σ₁ it lies in
{s < 0} ⊂ A ∖ Σ just before σ₁. Σ is closed in M_gl. If c met Σ again, let σ₁ be the first parameter after 0 at which
it does; then c((0, σ₁)) is a connected subset of (A ∖ Σ) ⊔ (B ∖ Σ) meeting both open sets, which is impossible. So Σ
is acausal in M_gl.

So Σ is an acausal smooth spacelike hypersurface in each of the connected time-oriented Lorentzian manifolds M_gl and
V. By [[thm:std-bgp-development]], D_(M_gl)(Σ) and D_V(Σ) are open, globally hyperbolic and connected, and have Σ as a
Cauchy hypersurface. In the chart, Σ is the graph of a function over the shell {r_♭ < |x| < R} ⊂ ℝ⁴, which is
connected; γ is Riemannian; and (γ, k) satisfies the constraint equations, by the Gauss and Codazzi equations, both
metrics being vacuum. So (Σ, γ, k) is initial data in the sense of [Sbi15, p. 11], with d = 4, and both Cauchy
developments, with the inclusion of Σ, are globally hyperbolic developments of it [Sbi15, Definition 2.1]
([[thm:std-sbierski]] (1)): they are connected and time oriented, as [Sbi15] assumes of every Lorentzian manifold
(p. 10), vacuum, and induce (γ, k) on Σ with respect to the future normal, by (i) for M_gl. By [Sbi15, Theorem 2.6]
they have a common globally hyperbolic development, and by [Sbi15, Theorem 3.4] a maximal one ([[thm:std-sbierski]]
(3), (4)), U ⊂ D_(M_gl)(Σ), with an isometric embedding j into D_V(Σ) that preserves the time orientation and the
embedding of Σ [Sbi15, Definitions 2.2 and 2.4] ([[thm:std-sbierski]] (2)), so that j is the identity on Σ. U is open
(the proof of [Sbi15, Theorem 3.4]; [[thm:std-sbierski]] (4)) and contains Σ, a Cauchy surface of U. By [Sbi15,
Theorem 3.13] U has no corresponding boundary points ([[thm:std-sbierski]] (5)), and gluing the two developments
along U by j gives a Hausdorff globally hyperbolic development that extends both [Sbi15, Theorem 2.7 and its proof]
([[thm:std-sbierski]] (3), (6)). ∎

**Remark {#rem:interior-one-spacetime}** (What [[lem:interior-one-spacetime]] says.)

- M_gl is one vacuum spacetime: g_λ just before Σ, near the hole, and g after Σ^IVP, everywhere in {r > r_♭}. Across
  Σ^IVP ∩ {r ≥ R} nothing is glued, since on R < r < 4R the glued data differ from those of g_λ.
- The identification of g with g_λ to the future of Σ holds on U, the largest region on which the two developments
  are isometric. How far U reaches into the future of Σ in each is not decided here: it is as far as both are
  determined by (Σ, γ, k) alone.
- The side of g_λ is taken in V, where Σ is acausal by construction. Whether Σ is acausal in all of Ω′, which would
  enlarge the development on that side, is not decided here.
- At late times near the hole, the domain of dependence of no bounded part of Σ^IVP reaches. For g_(b₀): on
  {|x| ≤ 2R₁}, v = t_* + 2r + const, and the past ingoing null ray {v = v(p), x̂ = x̂(p)} from a point p near r = r_h
  meets Σ^IVP = {τ = F(r)} on r ≥ R₃ (see [[lem:interior-where]]) at the radius where r + F(r) = v(p), which tends to
  infinity with t_*(p). So the interior covered by [[prop:interior]] belongs to a vacuum continuation of g_λ fixed by
  the gluing. It is not the continuation of g_λ's own data, since g_λ is constructed on the compact Ω′ only.

### Towards the continuation of g_λ's own data {#sec:interior-own-data}

To continue g_λ's own data, g_λ would first have to be constructed on the whole of Σ^IVP, out to spatial infinity. The
region there lies after the shell (v > v_end), where g_λ is Tangherlini plus the means times powers of λ plus the
remainder of [[lem:vii-1-1]]. Those data would then have to be shown to lie in a data class of [[thm:iii-k-4-3]], and
[[prop:vii-3-2]] with b = (m′, 0) and S = S⁰ = 0, applied to g_λ's own data, would give their development, with the
interior of [[prop:interior]] at late times; without the symmetry, [[thm:settling]] (ii) would. The first step needs
estimates on a domain reaching spatial infinity at the time of Σ^IVP; the construction from past null infinity
([[thm:past-construction]]) is the natural start. This section locates that step and fixes the data class.

Let P′ be the past domain [[eq:past-domain]] built with V′, τ′_end and a′ in place of V, τ_end and a, so that
V′_P := V′ + 1 + (τ′_end − τ0) + κ_P, with κ_P = ½ and h_P(τ) = κ_P t^(−1/4), t := 1 + τ0 − τ. The proof of
[[lem:vii-1-2]] chooses c₀ and T′ so that on Σ^IVP ∩ {r_♭ ≤ r ≤ 4R}

    τ ≥ τ0 + 1,   v ≥ v_end + 2,   τ ≤ τ_top,   and   V′ ≥ τ_top + 2R + q_end + 1,               {#eq:interior-placing}

τ_top a constant; then τ′_end ≥ V′ − q_end ≥ τ_top + 1, as r_q(v) ≤ q_end. Also a′ < ½r_♭ < 4R.

Two solutions carry the name g_λ here: that of [[thm:main]] on Ω′, whose data [[thm:settling]] glues, and that of
[[thm:past-construction]] on P′ ∪ Ω′, which satisfies items 1 and 3–5 of [[thm:main]] on Ω′ (item 4 of
[[thm:past-construction]]). [[lem:interior-where]] (i) speaks of both; from [[lem:interior-where]] (ii) on, g_λ denotes
the solution of [[thm:past-construction]], whose own data this section continues.

**Lemma {#lem:interior-where}** (Where g_λ is defined.) (i) [[thm:main]] gives g_λ on Ω′, and [[thm:past-construction]]
gives its solution on P′ ∪ Ω′; both domains lie in {v ≤ V′_P}: on Ω′, v ≤ V′ + 1 + τ′_end − τ ≤ V′_P − κ_P, as
τ ≥ τ0; on P′, v ≤ V′_P − h_P(τ).

(ii) On r ≥ R₃, Σ^IVP = {τ = F(r)} with F(r) := C″ − c₀ − T_(μ_end)(r), and v = r + F(r) → ∞ along it as r → ∞. So
Σ^IVP ∩ {v > V′_P} is not empty and contains the whole end of Σ^IVP at spatial infinity, where neither solution gives
data; [[thm:settling]] (i) replaces the data there, beyond 4R, by those of g^KS_(m_λ,0).

*Proof.* (i) Ω′ = {τ0 ≤ τ ≤ τ′_end, |x| ≥ a′, v + (τ − τ′_end) ≤ V′ + 1}, and V′_P − κ_P = V′ + 1 + τ′_end − τ0. P′
is {v + h_P(τ) ≤ V′_P} intersected with {τ ≤ τ0, |x| ≥ a′}. (ii) In the chart of [[lem:vii-1-2]], t = τ + T_(μ_end)(r)
+ c₀, and Σ^IVP = {t = C″} on r ≥ R₃ ([[lem:iii-b-3-7]] (b)). T_(μ_end)(r) → 0 as r → ∞ ([[lem:iii-b-3-5]] (a)). ∎

**Remark {#rem:interior-reach}** (Neither construction reaches further at a fixed λ.) The threshold of [[thm:main]] on
Ω′ depends on T′. The constants of [[thm:past-construction]] depend on the past domain, through V′_P: the annuli
A_P(τ) have thickness up to d1 = V′_P − v_start and outer radius up to t + a2, a2 = V′_P − τ0 − 1
([[lem:past-domain]] (d)); the Poincaré constant of [[lem:past-sobolev]] (b) grows with d1, r³ varying along a ray by a
factor up to (1 + d1)³; [[lem:past-transport]] carries the weight (t + a2)^γ when γ ≤ 0; and the decay classes E_p of
[[sec:past-approximant]] are bounds whose constants are taken on the domain. The proofs give no threshold uniform in
V′_P. So at a fixed λ the data of either solution are available on a bounded part of Σ^IVP: on Σ^IVP ∩ {r ≤ 4R} for
λ small depending on R, which is what [[cor:vii-2-3]] uses for the solution of [[thm:main]].

*The far part and its past domain of dependence.* On {v ≥ v_end}, μ = μ_end and

    g0 = η + m dv dv,     g0⁻¹ = η⁻¹ − m L0 L0,     m := μ_end r⁻²,     L0 = ∂_τ − x̂·∂_x

([[eq:background]]); there g0 = g_(b₀) in the chart of [[lem:vii-1-2]] ([[lem:interior-chart]] (a)). On r ≥ 4R ≥ 20R₁,
m ≤ 1/400. By [[lem:interior-where]] (ii) and [[lem:iii-b-3-5]] (a), on r ≥ 4R

    F′(r) = 2μ_end/(r² − μ_end) ∈ (0, ¼],     F(r) − F(4R) ≤ T_(μ_end)(4R) = μ_end^(1/2) log((4R + R₁)/(4R − R₁)),

and the last is at most R₁ log(21/19) < R₁/9. Put

    Σ_far := Σ^IVP ∩ {r ≥ 4R},   τ_S := F(4R),   v1 := 4R + τ_S,   τ_max := sup_(r ≥ 4R) F,   t̃ := τ − F(r),
    W := {v ≥ v1, t̃ ≤ 0, r ≥ 4R},     H₁ := W ∩ {v = v1} = {v = v1, τ ≤ τ_S},     Z := {v ≤ v1, r ≥ 4R}.

v1 is the value of v on the edge ∂Σ_far, and τ_max − τ_S < R₁/9, so v1 − τ_max > 4R − R₁/9 > 0. By
[[eq:interior-placing]] at r = 4R, τ0 + 1 ≤ τ_S ≤ τ_top and v1 ≥ v_end + 2. For a metric g on a set containing W ∪ Z,
|g − g0|_op denotes the Euclidean operator norm of the matrix of Cartesian components of g − g0 at a point.

**Lemma {#lem:interior-far-part}** (The far part's past domain of dependence.)

(i) *For g0.* t̃ is a time function on {r ≥ 4R}, with g0⁻¹(dt̃, dt̃) = −1 + F′² − m(1 + F′)² ≤ −15/16, and v is
nondecreasing along future causal curves, dv being null. W = D⁻(Σ_far; g0) in (ℝ × (ℝ⁴ ∖ 0), g0). Its boundary is
Σ_far, H₁ and past null infinity at v ≥ v1 (τ → −∞ at fixed v ≥ v1 and x̂, r → ∞), and r ≥ v1 − τ on W.

(ii) *The placement.* m_Ω := V′ + 1 − (v1 + τ_S − τ′_end) ≥ q_end + 3 ≥ 3. Every point of {v ≤ v1 + ½, r ≥ 4R}
lies in Ω′ if τ ≥ τ0, with τ ≤ τ′_end − ½, v + (τ − τ′_end) ≤ V′ − 1 and r > a′, and in P′ if τ ≤ τ0, with
v + h_P(τ) ≤ V′_P − 3. So H₁ and a strip of v-width ½ beyond it lie in Ω′ ∪ P′, and
v1 = V′_P − κ_P − (τ_S − τ0) − m_Ω ≤ V′_P − κ_P − 1 − m_Ω.

(iii) *Under a nearby metric.* Let g be a smooth Lorentzian metric on an open set containing W ∪ Z, and ε_g a
continuous function of τ with 0 ≤ ε_g ≤ 1/8 and |g − g0|_op, |g⁻¹ − g0⁻¹|_op ≤ ε_g(τ) at the points of W ∪ Z, with
I(τ) := 2 ∫_τ^(τ_max) ε_g finite. Then ∂_τ is timelike for g on W ∪ Z, taken future directed, and

    W_+ := {v ≥ v1 + I(τ), t̃ ≤ 0, r ≥ 4R} ⊂ D⁻(Σ_far; g):

all of W but the strip {v1 ≤ v < v1 + I(τ)} along H₁ lies in the domain of dependence of Σ_far for g.

(iv) *The width of the strip.* (a) Let g_λ be the solution of [[thm:past-construction]] on P′ ∪ Ω′. On Z,
|g_λ − g0|_op and |g_λ⁻¹ − g0⁻¹|_op are at most ε_λ(τ) := C_1 λ min(1, t^(−3/2)) for λ small, min(1, t^(−3/2)) being
read as 1 where t ≤ 1, and 2∫_(−∞)^(τ_S) ε_λ dτ = 2C_1λ(τ_S − τ0 + 2). (b) Let g be a smooth Lorentzian metric on an
open set containing W ∪ Z, equal to g_λ on Z, with |g − g0|_op, |g⁻¹ − g0⁻¹|_op ≤ C_W ν (v1 − τ)⁻² on W for numbers
C_W and ν ≥ 0. Then ε_g := ε_λ + C_W ν (v1 − τ)⁻² satisfies the hypotheses of (iii) for λ and ν small, and

    I(−∞) ≤ 2C_1λ(τ_max − τ0 + 2) + 2C_W ν/(v1 − τ_max):

all of W but a strip along H₁ of v-width O(λ + ν) lies in D⁻(Σ_far; g).

(v) *Nothing incoming.* At past null infinity, for v ≥ v1 ≥ v_end + 2, the radiation field λ[W_TT] of
[[thm:past-construction]] (2) vanishes: W_TT is proportional to env ([[eq:waves]]), which vanishes for v ≥ v_end. So
r^(3/2)(g_λ − g0) → 0 as r → ∞ at every fixed v ∈ [v1, V′_P) and x̂.

*Proof.* (i) From g0⁻¹ = η⁻¹ − m L0 L0 and L0(v) = 0, L0(τ) = 1, L0(r) = −1:

    g0⁻¹(dv, dv) = 0,  g0⁻¹(dv, dτ) = −1,  g0⁻¹(dτ, dτ) = −1 − m,  g0⁻¹(dr, dr) = 1 − m,  g0⁻¹(dτ, dr) = m.

With dt̃ = dτ − F′ dr this gives g0⁻¹(dt̃, dt̃) = −1 + F′² − m(1 + F′)², at most −15/16 on |F′| ≤ ¼ (its maximum is at
m = 0, and it decreases in m). dt̃(∂_τ) = dv(∂_τ) = 1, and ∂_τ is future timelike (g0(∂_τ, ∂_τ) = −1 + m < 0, dτ past
timelike), so t̃ increases and v does not decrease along future causal curves. The covectors ζ_± := d(r ± 2t̃) have

    g0⁻¹(ζ_+, ζ_+) = −3 − 4F′ + 4F′² − m(1 + 2F′)²,     g0⁻¹(ζ_−, ζ_−) = −3 + 4F′ + 4F′² − m(3 + 2F′)²,

both at most −7/4 on |F′| ≤ ¼, and ζ_+(∂_τ) = 2, ζ_−(∂_τ) = −2; so ζ_+(Y) > 0 > ζ_−(Y), that is |dr(Y)| < 2 dt̃(Y),
for every future causal Y. L0 is future null; along its rays v is fixed and t̃ = v − (r + F(r)) increases as r
decreases, since d(r + F)/dr = 1 + F′ ≥ 1.

*D⁻(Σ_far; g0) lies in W.* For p in it, the ingoing null ray from p (v = v(p), x̂ fixed, r decreasing to 0) is future
inextendible, so it meets Σ_far, at some r_* ≥ 4R with τ = F(r_*). So v(p) = r_* + F(r_*) ≥ 4R + F(4R) = v1,
r(p) ≥ r_* ≥ 4R, and t̃(p) ≤ 0, as t̃ increases along the ray to 0 at r_*.

*W lies in D⁻(Σ_far; g0).* Let p ∈ W and c a future inextendible causal curve from p; v ≥ v1 along c. If c reaches
{r = 4R}, at a first point q, then t̃(q) = τ(q) − τ_S = v(q) − v1 ≥ 0, so c meets {t̃ = 0} at or before q, at a point
with r ≥ 4R and v ≥ v1, a point of Σ_far = {t̃ = 0, r ≥ 4R}. Otherwise c stays in {r ≥ 4R}, where t̃ increases and
|dr| < 2 dt̃. While t̃ ≤ 0 it lies in the compact set {t̃(p) ≤ t̃ ≤ 0, 4R ≤ r ≤ r(p) + 2|t̃(p)|}, on which dt̃ is
uniformly timelike, so its coordinate velocity, parametrised by t̃, is bounded; if t̃ stayed below 0, c would have an
end point and be extendible. So c reaches t̃ = 0 at a point with r ≥ 4R and v ≥ v1, a point of Σ_far. In the chart,
{t̃ = 0} ∩ W = Σ_far and {v = v1} ∩ W = H₁, the rest of the boundary is the end τ → −∞ at fixed v and x̂, and
r = v − τ ≥ v1 − τ on W.

(ii) By [[eq:interior-placing]], τ_S ≤ τ_top and τ′_end ≥ V′ − q_end, so

    m_Ω = V′ + 1 + τ′_end − 2τ_S − 4R ≥ 2V′ + 1 − q_end − 2τ_top − 4R ≥ q_end + 3,

using V′ ≥ τ_top + 2R + q_end + 1. For v ≤ v1 + ½ and r ≥ 4R, τ = v − r ≤ τ_S + ½ ≤ τ_top + ½ ≤ τ′_end − ½. If τ ≥ τ0,
then v + (τ − τ′_end) ≤ v1 + τ_S + 1 − τ′_end = V′ + 2 − m_Ω ≤ V′ − 1, and r ≥ 4R > a′: the point lies in Ω′, strictly
inside its defining inequalities other than τ ≥ τ0. If τ ≤ τ0, then, as h_P ≤ κ_P and v1 = V′_P − κ_P − (τ_S − τ0) − m_Ω
by the definitions of m_Ω and V′_P,

    v + h_P(τ) ≤ v1 + ½ + κ_P = V′_P − (τ_S − τ0) − m_Ω + ½ ≤ V′_P − 1 − 3 + ½ < V′_P − 3,

as τ_S − τ0 ≥ 1, and r ≥ 4R > a′: the point lies in P′.

(iii) As g0(∂_τ, ∂_τ) = −1 + m and g0⁻¹(dτ, dτ) = −1 − m, and |∂_τ|_E = |dτ|_E = 1,

    g(∂_τ, ∂_τ) ≤ −1 + m + ε_g < 0,     g⁻¹(dτ, dτ) ≤ −1 − m + ε_g < 0,

so dτ(Y) > 0 for every future causal Y of g. *The cone of dv.* ζ := dv + 2ε_g dτ = (1 + 2ε_g) dτ + x̂·dx has
|ζ|_E² = 2 + 4ε_g + 4ε_g² and g0⁻¹(ζ, ζ) = −4ε_g − 4ε_g²(1 + m), so

    g⁻¹(ζ, ζ) ≤ g0⁻¹(ζ, ζ) + ε_g |ζ|_E² = −2ε_g − 4mε_g² + 4ε_g³ < 0     (0 < ε_g ≤ 1/8),

and ζ(∂_τ) = 1 + 2ε_g > 0. So ζ(Y) > 0 for every future causal Y of g (where ε_g = 0, g = g0 and dv(Y) ≥ 0): that is,
dv(Y) ≥ −2ε_g dτ(Y). Along a future causal curve of g parametrised by τ, v − I(τ) is therefore nondecreasing, as
dI/dτ = −2ε_g. *t̃ for g.* |ζ_±|_E² = 4 + (1 ∓ 2F′)² ≤ 25/4, so g⁻¹(ζ_±, ζ_±) ≤ −7/4 + (25/4)ε_g < 0 for
ε_g < 7/25, and g⁻¹(dt̃, dt̃) ≤ −15/16 + (17/16)ε_g < 0. With ζ_+(∂_τ) = 2 and ζ_−(∂_τ) = −2 as before, t̃ is a time
function of g on W ∪ Z with |dr(Y)| < 2 dt̃(Y) for future causal Y of g there. The argument of (i) uses these
properties only on {t̃ ≤ 0, r ≥ 4R}, which is W ∪ Z. For p in W_+ and c a future inextendible causal curve of g from
p, v ≥ v1 + I(τ) ≥ v1 along c while it is in W, as v − I is nondecreasing; and the argument of
(i) applies verbatim: c meets Σ_far.

(iv) (a) On Ω′, item 4 of [[thm:past-construction]] gives items 1 and 3–5 of [[thm:main]], among them |g_λ − g0| ≤ Cλ
(item 4 of [[thm:main]]). On P′, g_app − g0 = λW + Σ_j λ^j m_j + Σ_j λ^j ĝ_j, evaluated at θ = u/λ ([[eq:ansatz]]), a
finite sum whose profiles vanish for v ≤ v_start and are at most C r^(−3/2) on P′ ∩ {v ≥ v_start} by [[eq:past-classes]]:
W_TT ∈ O_(3/2), while χ, m_j and ĝ_j lie in O_2 or L_2 and are at most C r⁻² ≤ C a1^(−1/2) r^(−3/2), dv ⊗ dv having
bounded Cartesian components. As r ≥ t + a1 ≥ t there ([[lem:past-domain]] (d)) and 0 < λ ≤ 1, |g_app − g0| ≤ Cλ t^(−3/2)
on P′, the bound stated in (P-v) of [[sec:past-proof]]. With items 1 and 3 of [[thm:past-construction]], |g_λ − g0| ≤
Cλ^(K−3) t^(−2) + Cλ t^(−3/2) ≤ C′λ t^(−3/2) on P′, as K ≥ 6 and t ≥ 1 there, and g_λ = g0 for v ≤ v_start. By (ii), Z ⊂
Ω′ ∪ P′ and Z ⊂ {τ ≤ τ_S}, and t ≤ 1 on Z ∩ Ω′. So ε_λ bounds |g_λ − g0|_op on Z, the operator norm of a 5 × 5 matrix
being at most five times its largest entry, and |g_λ⁻¹ − g0⁻¹|_op by the Neumann series, for λ small. The integral is
∫_(−∞)^(τ0) t^(−3/2) dτ = ∫_1^∞ t^(−3/2) dt = 2 plus τ_S − τ0. (b) ε_g is continuous, at most 1/8 for λ and ν small, as
v1 − τ ≥ v1 − τ_max > 0 on W ∪ Z, and it bounds both norms on W ∪ Z by (a) and the hypothesis. Its integral over (−∞,
τ_max] is at most C_1λ(τ_max − τ0 + 2) + C_W ν ∫_(−∞)^(τ_max) (v1 − τ)⁻² dτ = C_1λ(τ_max − τ0 + 2) + C_W ν/(v1 − τ_max).
(iii) applies.

(v) env vanishes for v ≥ v_end, and [W_TT] with it ([[eq:waves]]); [[thm:past-construction]] (2) then reads
r^(3/2)(g_λ − g0) → 0. ∎

So the first step is a characteristic problem on W: the data of g_λ on H₁, nothing incoming at past null infinity,
solved up to Σ_far and uniformly up to spatial infinity I₀, in the wave-map gauge relative to g_(b₀). It is a
scattering problem near spatial infinity without incoming radiation, for a perturbation that is O(λ) on H₁. The data of
g_λ near I₀ are not needed: past null infinity carries nothing there. [[ch:own-data]] continues the metric on W.
Parts (i), (ii) and (v) of [[lem:interior-far-part]] describe the domain W, its place in Ω′ ∪ P′ and the absence of
incoming radiation; (iii) and (iv) (b) bound, for any continuation close to g0 at the rate of (iv) (b), the strip along
H₁ that may lie outside the domain of dependence of Σ_far.

**Remark {#rem:interior-far-part-numerical}** (Numerical observation.) For a radial model g⁻¹ = g0⁻¹ + ε(τ) n ⊗ n with
ε = 0.05 min(1, t^(−3/2)) and eight fixed covectors n, the past null generator through ∂Σ_far of the boundary of
D⁻(Σ_far; g) was integrated numerically down to τ_S − 3000: along it |v − v1| stayed below I(τ), the largest ratio
|v − v1|/I(τ) being 0.5128, attained for n proportional to dv. Sampling perturbations of each kind put the sharp
constant of the comparison dv(Y) ≥ −2ε_g dτ(Y) of [[lem:interior-far-part]] (iii) between ½ and 2. No proof uses these
observations.

*What H₁ carries.* On H₁ ∩ P′, |g_λ − g_app| ≤ Cλ^(K−3) t^(−2) ([[thm:past-construction]] (3)). After the shell g_app −
g0 = Σ_j λ^j m_j, the means alone, every oscillating profile vanishing on {v ≥ v_end} (step (3) of the proof of
[[prop:past-items]]); and m_m ∈ L_2 ([[thm:past-approximant]]): a leading term r⁻² M_m(v, x̂), with M_m := 2 ∫_(−∞)^v
𝒮_(m,3) dv′, plus a remainder in E_(5/2). That is a leading term and a bound, not an expansion. The sufficient condition
of [[lem:vii-0-1]] asks for components in ρ²C^∞ and ρ³C^∞, expansions in integer powers of ρ = 1/r, and the class of
[[thm:settling]] (ii) is polyhomogeneous with terms of orders r⁻² and r⁻³. An E_(5/2) bound neither gives such an
expansion nor excludes one. The data index set of [[thm:iii-k-4-3]] need not be integral: row d1 of [[sec:vi-c-1]] asks
min Re ℰ_0 > 3/2 + 2γ_Υ, jℰ_0 ⊂ ℰ_0, ℓ_0 > 3 and ℓ_0 ∉ Re π_1ℰ_0, and none of these is integrality. Closure under sums is
the only condition linking the elements, so (5/2, 0) ∈ ℰ_0 forces (5, 0), (15/2, 0), … into it. As ℓ_0 > 5/2, the norm
‖·‖_(d_1) of [[sec:s27-class]] is finite on a term ρ^(5/2) a(ω) exactly when (5/2, 0) ∈ ℰ_0; for the class [[eq:vii-0-1]]
it is infinite.

**Definition {#def:half-class}** (The half-integer class.) The *half-integer class* is the data class of
[[thm:iii-k-4-3]] with

    ℰ_0^½ := {(2 + j/2, 0) : j ∈ ℕ₀},     ℓ_0 ∈ (3, 4) ∖ {7/2},     ℓ_I ∈ (3, ℓ_0),                   {#eq:half-class}

with ℓ_I off the discrete exclusion sets of row d2 of [[sec:vi-c-1]] and of (H4) of [[sec:iii-i10-1]], as for
[[eq:vii-0-1]]; ‖·‖^½_(d_1) denotes the H^(d_1)-norm of H^(∞,(ℰ_0^½,ℓ_0))_b × H^(∞,(ℰ_0^½+1,ℓ_0+1))_b, infinite outside
these spaces.

**Lemma {#lem:half-class}** (Row d1, and what lies in the half-integer class.) (a) ℰ_0^½ and ℓ_0 satisfy row d1 of
[[sec:vi-c-1]], and ℰ_0^½ contains the index set of [[eq:vii-0-1]]. (b) Let γ̃, k̃ be smooth symmetric 2-tensors on
Σ^IVP whose Cartesian components are, on {r ≥ R′}, ρ² and ρ³ times smooth functions of (ρ^(1/2), x̂) on
[0, R′^(−1/2)] × 𝕊³. Then ‖(γ̃, k̃)‖^½_(d_1) is finite, bounded as in [[lem:vii-0-1]].

*Proof.* (a) min Re ℰ_0^½ = 2 > 3/2 + 2γ_Υ, as γ_Υ < ¼. (2 + j/2) + (2 + k/2) = 2 + (j + k + 4)/2, so ℰ_0^½ is closed
under sums, and jℰ_0^½ ⊂ ℰ_0^½. ℓ_0 > 3, and Re π_1ℰ_0^½ = {2, 5/2, 3, 7/2, 4, …} does not contain ℓ_0. The index set
of [[eq:vii-0-1]] is the part of ℰ_0^½ with j even.

(b) Put s := ρ^(1/2). Taylor's formula in s writes

    ρ²Φ(s, x̂) = Σ_(j ≤ 3) ρ^(2+j/2) a_j(x̂) + ρ⁴Φ₄(s, x̂),

with a_j and Φ₄ smooth, the seminorms of the remainder bounded by those of Φ. Smooth functions of s are conormal in ρ,
as ρ∂_ρ = ½ s∂_s. The exponents 2 + j/2 < ℓ_0 lie in ℰ_0^½; the term with 2 + j/2 > ℓ_0, if any (j = 3 when
ℓ_0 < 7/2), and the remainder lie in ρ^(ℓ_0)H^∞_b, as ℓ_0 < 4 and the weights are those of the b-density, a weight
being the pointwise order. Likewise ρ³Φ = Σ_(j ≤ 3) ρ^(3+j/2) b_j + ρ⁵Φ₅, with exponents in ℰ_0^½ + 1 below
ℓ_0 + 1 < 5. On {r ≤ 2R′} the weights are bounded above and below. ∎

**Remark {#rem:half-class-changes}** (What the half-integer class changes.) The data index set enters the rest of the
stability theory only through ℰ^C_I ([[thm:iii-c1-3-1]], row d2 of [[sec:vi-c-1]]), the exponents Λ ⊃ π_1ℰ^C_I and the
bound l_* of [[def:iii-i10-1-1]], and the threshold ε and order d_1 of [[thm:iii-k-4-3]] (row n1). Every index set
ℰ^C_I satisfying [[def:iii-c-3-1]] contains (2, 0) and is closed under adding ½ ([[lem:iii-c-3-2]] (a)), so it contains
ℰ_0^½. Hence the smallest such set containing the index set of [[eq:vii-0-1]] ([[lem:iii-c-3-2]] (e)), from which the
proof of [[thm:iii-c1-3-1]] starts, is also the smallest containing ℰ_0^½. So π_1ℰ^C_I, Λ, the conditions (G) and
(G⁺), ε_+, ε_K and the loss d ([[thm:loss-d]]) are the same in the half-integer class. Only the logarithmic orders of
ℰ^C_I at the half-integers can rise, through the extended unions ℰ_0 ∪̄ ℰ^C_I of that proof; they enter l_* and
k̄(λ) of [[def:iii-i10-1-1]], and their values are not determined here. ε and d_1, and with them λ1 and δ, may change.

So the continuation of g_λ's own data consists of three steps: (1) the scattering problem on W of
[[lem:interior-far-part]], with r-weighted estimates in place of the annuli of bounded thickness of
[[lem:past-sobolev]]; (2) the expansion of its solution at I₀, to put the data on Σ_far in the half-integer class;
(3) [[prop:vii-3-2]] on g_λ's own data, in that class. [[ch:own-data]] carries them out ([[thm:own-data]]).
