## The development of g_λ's own data settles {#ch:own-data}

[[thm:settling]] (i) concerns data that agree with those of g_λ on a ball and are continued equivariantly to exact
Tangherlini data beyond it. This chapter proves that the maximal vacuum development of the data that g_λ itself induces
on Hintz's initial surface Σ^IVP settles to five-dimensional Tangherlini, with no gluing, for every λ below a threshold
and with no exceptional set. The data class of [[thm:settling]] (ii) does not contain these data: after the shell the
difference g_λ − g0 carries at past null infinity a coefficient of r^(−5/2), of size O(λ^∞) but nonzero for all λ off a
discrete set, and it reaches the data at spatial infinity as a term ρ^(5/2), ρ := 1/r. The class is therefore widened by
the half-integer orders, and the stability theory runs in the wider class with the same index sets.

The argument has five parts. (1) The far part S := Σ^IVP ∩ {r ≥ 4R} of the initial surface has a past domain of
dependence W for Tangherlini, bounded by S, by an ingoing null cone N on which g_λ is known, and by past null infinity,
where nothing comes in after the shell (Section [[sec:own-far-part]]). (2) The tail at r^(−5/2) is computed
(Section [[sec:own-tail]]). (3) The stability theory holds in the half-integer class with the same index sets
(Section [[sec:own-half-class]]). (4) The constants of the construction from past null infinity are polynomial in
λ^(−1) at every order, which makes the data of g_λ on N small at every weight that the estimate below uses
(Sections [[sec:own-orders]] and [[sec:own-sigma]]). (5) After its self-similar terms through r^(−4) are subtracted,
g_λ continues to W by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence;
the continuation is vacuum, unique in a class of weight below ½, and its data on S lie in the half-integer class with
small norm (Sections [[sec:own-continuation]] and [[sec:own-vacuum]]). The theorem is assembled in
Section [[sec:own-proof]].

*Notation.* We use the chart (τ, x) of [[sec:background]], v = τ + r, the background g0 of [[eq:background]] and the
gauge of [[sec:gauge]]. Ω′ is the domain of the form [[eq:omega]], with constants (T′, δ′0) and inner radius a′ = q0 −
δ′0, that [[lem:vii-1-2]] chooses for a radius R ≥ R_3, with V′ := v_end + T′ and τ′_end its constants, and P′ is its
past domain, [[eq:past-domain]] with these constants: P′ := {τ ≤ τ0, |x| ≥ a′, v + h_P(τ) ≤ V′_P}, V′_P := V′ + 1 +
(τ′_end − τ0) + κ_P, κ_P = ½. g_λ is the solution of [[thm:past-construction]] on P′ ∪ Ω′ ([[thm:past-construction]]
holds for every domain of the form [[eq:omega]] and its past domain). On {v ≥ v_end}, μ = μ_end, and we write μ := μ_end
in this chapter; there g0 = g_b0 := η + μ r⁻² dv ⊗ dv, five-dimensional Tangherlini in Kerr–Schild form, whose
Kerr–Schild time is τ ([[lem:vii-1-2]] (a)). In the far region we write t := τ, so that (t, x) are Kerr–Schild Cartesian
coordinates and v = t + r; the variable t of [[ch:past-construction]] is written t_P := 1 + τ0 − τ. We put 𝔪 := μ r⁻².
For |x| ≥ R_3 the initial surface is a graph, Σ^IVP ∩ {|x| ≥ R_3} = {t = f(|x|)}, with f′ ∈ |x|⁻² C^∞ near infinity
([[lem:vii-2-1]] and the paragraph before it, with t_KS = τ up to a constant absorbed in f). Enlarging R, |f′| ≤ ¼ and 𝔪
≤ 1/16 on r ≥ 4R. G = O(2) × O(2) acts by (t, x) ↦ (t, Ox) ([[sec:s27-class]]).

**Theorem {#thm:own-data}** (the development of g_λ's own data settles). Fix A, the envelope env ∈ C_c^∞, the angular
profile and the seed. Let ℓ0 ∈ (3, 4) ∖ {7/2}, ℓ_I ∈ (3, ℓ0) off the exclusion sets of row d2 of [[sec:vi-c-1]], ε_m > 0
and 0 < ε_t < ε_K, the parameters of the stability theory chosen as for [[thm:settling]]. Let ε and d_1 be those of
[[thm:iii-k-4-3]] in the class ℰ_0^½ ([[def:own-half-class]], [[thm:own-half-settling]]), below the threshold of
[[prop:vii-3-2]] and that of [[cor:s27-rate]] for ε_m and ε_t. Let a ∈ (ℓ0 − 1, 3), k1 := max(8, d_1 + 4),
M := 15 + 2(k1 + 1), K > max(d_1 + 14, K*(a, M, k1)) with K* of [[lem:own-e-flux]], and let the approximant of
[[thm:past-approximant]] have K + 4 + ⌈4β0(k_P)⌉ stages, k_P := 2k1 + 14 ([[cor:own-p-order]]). Then there is λ_2 > 0
such that for every 0 < λ ≤ λ_2, with no exceptional set:

(1) g_λ continues to the past domain of dependence W of S := Σ^IVP ∩ {r ≥ 4R} for g_b0 as a smooth G-invariant vacuum
metric g in the wave-map gauge relative to g_b0, and all of W but a strip along its null boundary, of v-width tending to
0 with λ, lies in the domain of dependence of S for g. It is the only continuation in that gauge with |g − g_b0| ≤ 1/50,
commuted energies of some weight a_0 ∈ (0, ½) bounded uniformly in the slices, and energy tending to 0 toward past null
infinity ([[prop:own-uniqueness]]);

(2) its data (γ, k) on Σ^IVP satisfy γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b, k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b, with
‖(γ − γ_b0, k − k_b0)‖_(d_1) < ε in the norm of [[sec:s27-class]] taken with ℰ_0 = ℰ_0^½;

(3) the maximal vacuum development of (γ, k) settles to a Tangherlini metric g_(m′,0) with |m′ − μ_end| < ε_m: on
{r_0 ≤ r ≤ R′, t_* ≥ T′}, |(t_*∂_(t_*))^i ∂_x^β (g − g_(m′,0))| ≤ C t_*^(−2−ε_t) for every R′, i and β, with C and T′
depending on them.

The threshold λ_2 is not evaluated, and ε, d_1, λ_2 depend on the class. The proof is in Section [[sec:own-proof]].
[[pending:issue-1]]

### The far part of the initial surface and its past domain of dependence {#sec:own-far-part}

Let S := Σ^IVP ∩ {r ≥ 4R} = {τ = f(r), r ≥ 4R}, τ_S := f(4R), v1 := 4R + τ_S the value of v on ∂S,
τ_max := sup_(r≥4R) f, and put

    t̃ := τ − f(r),     W := {v ≥ v1, t̃ ≤ 0, r ≥ 4R},     N := W ∩ {v = v1},     Z_b := {v ≤ v1, r ≥ 4R},
    Σ̃_σ := W ∩ {t̃ = σ} (σ ≤ 0),     s := (v − v1)/r.                                                {#eq:own-wedge}

Σ̃_0 = S. The constants τ0, τ_top, q_end and r_0 are those of [[lem:vii-1-2]] and its proof: on Σ^IVP ∩ {r_0 ≤ r ≤ 4R},
τ ≥ τ0 + 1, v ≥ v_end + 2 and τ ≤ τ_top; V′ ≥ τ_top + 2R + q_end + 1; τ′_end ≥ V′ − q_end and τ′_end ≥ τ_top + 1;
r_0 > a′; and 4R > r_0.

**Lemma {#lem:own-domain}** (the far part's past domain of dependence).
(i) t̃ is a time function on {r ≥ 4R} for g_b0, with g_b0⁻¹(dt̃, dt̃) = −1 + f′² − 𝔪(1 + f′)² ≤ −15/16, and v is
nondecreasing along future causal curves. W = D⁻(S; g_b0). Its boundary is S, N and past null infinity at v ≥ v1 (τ → −∞
at fixed v and x̂), and r ≥ v1 − τ on W.
(ii) m_Ω := V′ + 1 − (v1 + τ_S − τ′_end) ≥ q_end + 3 ≥ 3 and v1 ≥ v_end + 2. Every point of {v ≤ v1 + ½, r ≥ 4R} lies in
Ω′ if τ ≥ τ0 and in P′ if τ ≤ τ0, with v + h_P(τ) ≤ V′_P − 3 in the latter case. So N and the strip
{v1 ≤ v ≤ v1 + ½, r ≥ 4R} lie in Ω′ ∪ P′, and v1 ≤ V′_P − κ_P − 1 − m_Ω.
(iii) Let g be a smooth Lorentzian metric on an open set containing W and ε_g a continuous function of τ with
0 ≤ ε_g ≤ 1/8, |g − g_b0|_op ≤ ε_g(τ) and |g⁻¹ − g_b0⁻¹|_op ≤ ε_g(τ) on W (Euclidean operator norms of the component
matrices), and I(τ) := 2 ∫_τ^(τ_max) ε_g finite. Then W_+ := {v ≥ v1 + I(τ), t̃ ≤ 0, r ≥ 4R} lies in D⁻(S; g).
(iv) For the metric g of [[thm:own-continuation]] on W, I(−∞) ≤ C(λ + ε_B), with ε_B the size of the bootstrap there,
which tends to 0 with λ: all of W but a strip along N of v-width at most C(λ + ε_B) lies in D⁻(S; g).
(v) For v ≥ v1 the radiation field of g_λ at past null infinity vanishes: r^(3/2)(g_λ − g0) → 0 as r → ∞ at every fixed
v ∈ [v1, V′_P) and x̂.
(vi) On W, s ∈ [0, 5/4], |τ − v1| ≤ r and r ≥ v1 − τ. Each Σ̃_σ is {r ≥ r_σ} along the rays t = f(r) + σ, with r_σ
the solution of r + f(r) = v1 − σ, and r_σ ≥ c_W (1 + |σ|) for some c_W > 0.

*Proof.* (i) By [[prop:vaidya]] (c)–(d), g_b0⁻¹(dv, dv) = 0, g_b0⁻¹(dv, dτ) = −1, g_b0⁻¹(dτ, dτ) = −1 − 𝔪,
g_b0⁻¹(dr, dr) = 1 − 𝔪 and g_b0⁻¹(dτ, dr) = 𝔪. With dt̃ = dτ − f′ dr this gives the stated value, whose maximum over
𝔪 ≥ 0 is at 𝔪 = 0, and −1 + f′² ≤ −15/16. dt̃(∂_τ) = dv(∂_τ) = 1, so t̃ increases and v does not decrease along future
causal curves (dv is null). The conormals β̂ := d(r + 2t̃) and α̂ := d(r − 2t̃) satisfy, by the same contractions,

    g_b0⁻¹(β̂, β̂) = (2f′ − 3)(2f′ + 1) − 𝔪(1 + 2f′)²,
    g_b0⁻¹(α̂, α̂) = (2f′ − 1)(2f′ + 3) − 𝔪(3 + 2f′)²,                                              {#eq:own-cones}

both at most −7/4 for |f′| ≤ ¼ (with y := 2f′ ∈ [−½, ½], y² − 2y − 3 and y² + 2y − 3 are at most −7/4), and
β̂(∂_τ) = 2, α̂(∂_τ) = −2. So |dr(Y)| < 2 dt̃(Y) for future causal Y. L0 is future null with L0(v) = 0, L0(τ) = 1,
L0(r) = −1; along its rays t̃ = v − r − f(r) increases as r decreases, and d(r + f)/dr = 1 + f′ ≥ ¾.
*D⁻(S; g_b0) ⊂ W.* For p in D⁻(S), the future ingoing null ray from p (v = v(p), r decreasing) must meet S, at some r* ≥
4R with τ = f(r*); so v(p) = r* + f(r*) ≥ 4R + f(4R) = v1, r(p) ≥ r* ≥ 4R, and t̃(p) ≤ 0, as t̃ increases along the ray
to 0 at r*. *W ⊂ D⁻(S; g_b0).* Let p ∈ W and γ a future-inextendible causal curve from p; v ≥ v1 along it. If γ reaches
{r = 4R}, at a first point q, then t̃(q) = τ(q) − τ_S = v(q) − v1 ≥ 0, so γ meets {t̃ = 0} at or before q, at a point
with r ≥ 4R and v ≥ v1, a point of S. Otherwise γ stays in {r ≥ 4R}; while t̃ ≤ 0 it lies in the compact set {t̃(p) ≤ t̃
≤ 0, 4R ≤ r ≤ r(p) + 2|t̃(p)|}, where dt̃ is uniformly timelike, so its coordinate velocity parametrised by t̃ is
bounded; if t̃ stayed below 0, γ would have an endpoint and be extendible. So γ reaches t̃ = 0 at a point of S. The
description of the boundary and r = v − τ ≥ v1 − τ follow from the definitions.

(ii) m_Ω = V′ + 1 + τ′_end − 2τ_S − 4R ≥ 2V′ + 1 − q_end − 2τ_top − 4R ≥ q_end + 3, by τ_S ≤ τ_top, τ′_end ≥ V′ − q_end
and V′ ≥ τ_top + 2R + q_end + 1; and v1 ≥ v_end + 2 since ∂S ⊂ Σ^IVP ∩ {r_0 ≤ r ≤ 4R}. Let v ≤ v1 + ½ and r ≥ 4R. Then
τ = v − r ≤ τ_S + ½ ≤ τ′_end − ½. If τ ≥ τ0: v + (τ − τ′_end) ≤ v1 + τ_S + 1 − τ′_end = V′ + 2 − m_Ω ≤ V′ − 1, and
r > a′, so the point lies in the interior of Ω′ ([[eq:omega]]). If τ ≤ τ0: v + h_P(τ) ≤ v1 + ½ + κ_P = V′_P − (τ_S − τ0)
− m_Ω + ½ ≤ V′_P − 3, as τ_S ≥ τ0 + 1, h_P ≤ κ_P and V′_P = V′ + 1 + (τ′_end − τ0) + κ_P; so it lies in P′. The last
inequality is the same estimate.

(iii) Since ε_g ≤ 1/8 < 1, g(∂_τ, ∂_τ) ≤ −1 + 𝔪 + ε_g < 0 and g⁻¹(dτ, dτ) ≤ −1 − 𝔪 + ε_g < 0; we time-orient g by
∂_τ, so dτ(Y) > 0 for future g-causal Y. The covector ω := dv + 2ε_g dτ has |ω|_E² ≤ 2 + 4ε_g + 4ε_g² and

    g⁻¹(ω, ω) ≤ g_b0⁻¹(ω, ω) + ε_g |ω|_E² = −4ε_g − 4ε_g²(1 + 𝔪) + ε_g |ω|_E² ≤ −2ε_g − 4𝔪ε_g² + 4ε_g³ < 0

for 0 < ε_g ≤ 1/8, and ω(∂_τ) = 1 + 2ε_g > 0; so ω(Y) > 0 for future g-causal Y: dv(Y) ≥ −2ε_g dτ(Y). Along a future
g-causal curve parametrised by τ, v − I(τ) is therefore nondecreasing. By [[eq:own-cones]] and ε_g ≤ 1/8 < 7/25 (the
perturbation changes g⁻¹(α̂, α̂) and g⁻¹(β̂, β̂) by at most (25/4) ε_g ≤ 25/32 < 7/4), t̃ is a g-time function on
{r ≥ 4R} and |dr(Y)| < 2 dt̃(Y) for future g-causal Y. For p ∈ W_+ and γ a future-inextendible g-causal curve from p,
v ≥ v1 + I(τ) ≥ v1 along γ while it lies in W, and the argument of (i) applies verbatim: γ meets S.

(iv) On W, by the pointwise bounds [[eq:own-pointwise]] of [[thm:own-continuation]] and [[lem:own-sigma-data]],
|g − g_b0| ≤ C λ r⁻² + C_S ε_B r^(−1/2−a) ≤ C(λ + ε_B)(v1 − τ)⁻², as r ≥ v1 − τ > 0 and a ≥ 3/2, and the same holds
for the inverse by the Neumann series. So ε_g := C(λ + ε_B)(v1 − τ)⁻² serves for λ small, and
I(−∞) = 2 C(λ + ε_B)/(v1 − τ_max). (iii) gives the claim.

(v) For v > v_end the envelope vanishes, so the leading wave, proportional to it, vanishes, and every oscillating
profile of the approximant vanishes there ([[lem:vii-1-1]], the paragraph *After the shell* of its proof, which is a
statement about the profiles and holds on P′ as on Ω′: on P′ each oscillating profile is the transport solution along ℓ
from past null infinity at fixed v ([[thm:past-approximant]]), with data and forcing that vanish at v > v_end, by
induction on the stage). Item 2 of [[thm:past-construction]] with λ[W_TT] = 0 at v ≥ v1 > v_end gives the claim.

(vi) On W, v − v1 = τ + r − v1 ≥ 0 and τ ≤ f(r), so v − v1 ≤ f(r) − f(4R) + r − 4R ≤ (5/4)(r − 4R), as |f′| ≤ ¼: hence
0 ≤ s ≤ 5/4. τ − v1 = (v − v1) − r ≥ −r, and τ − v1 ≤ f(r) − f(4R) − 4R ≤ r. On Σ̃_σ, τ = f(r) + σ and v = r + f(r) + σ,
which increases in r (1 + f′ ≥ ¾), so v ≥ v1 exactly for r ≥ r_σ. As f′ = O(r⁻²), f is bounded on r ≥ 4R, |f| ≤ C_f; then
r_σ ≥ max(4R, |σ| + v1 − C_f) for σ ≤ 0, which is at least c_W (1 + |σ|) for some c_W > 0 depending on R, v1 and
C_f. ∎

Enlarging R, we also take sup_(r≥4R) |f − f(4R)| ≤ 1 (f′ = O(r⁻²)), so that v1 − τ_max ≥ 4R − 1 > 0. We write W_T := W ∩
{t̃ ≥ T} for T ≤ 0.

### The half-order tail at past null infinity {#sec:own-tail}

At fixed λ, on the far region of [[thm:past-construction]], g_λ − g0 = Σ_(k=3)^J r^(−k/2) G_k + u_J for every J
([[prop:bondi-hierarchy]]), with G_3 the radiation field and G_k = (2/(k − 3)) ∫_(v_start)^v S_(k/2+1) dv′ for k ≥ 4,
r^(−q) S_q being the leading term of the forcing of u_(2q−3)'s equation. By [[lem:waves]] (a),

    G_3 = F T_F + G T_G = λ A env(v) h(ζ) (T_F sin(v/λ) + T_G cos(v/λ)),
    T_F := 2 ((x3 dx4 − x4 dx3)²/r² − (s²/3)(|dx|² − (x̂·dx)²)),
    T_G := 2 ((x1 dx2 − x2 dx1)²/r² − (c²/3)(|dx|² − (x̂·dx)²)),                                       {#eq:own-g3}

where T_F and T_G have Cartesian components that are smooth functions of x̂ alone, purely spatial and linearly
independent (T_G has a component along (x1 dx2 − x2 dx1)², T_F none). Put ê(ω) := ∫ env(v) e^(iωv) dv and ω := 1/λ.

**Proposition {#prop:own-tail}** (the tail). Let v ≥ v_end.
(a) G_5(v) = G_5(v_end) =: G_5^∞.
(b) G_5^∞ = A a_1(λ) + A³ a_3(λ), where a_1 = ½(Δ̊ − ¾)[λ h (T_F Im ê(ω) + T_G Re ê(ω))], Δ̊ acting on each Cartesian
component, and a_3 is the integral over v of the part of S_(7/2) cubic in A.
(c) a_1 and a_3 are O(λ^n) for every n.
(d) a_1 is purely spatial, and a_1 = 0 exactly when ê(1/λ) = 0. There is at most one A* > 0 for which the spatial
components of G_5^∞ vanish for every λ ∈ (0, λ_P]; for every other A > 0 the λ ∈ (0, λ_P] at which they vanish form a
set with no accumulation point in (0, λ_P].

*Proof.* *The order count.* Give each factor of a term of S_q its order, the power of r⁻¹ it carries, and its degree in
A. G_3 has order 3/2 and degree 1. G_4 = 2 ∫ S_3 has order 2 and degree 2: S_3 is quadratic in G_3 and its
v-derivatives plus −(3μ′/2) dv dv from Ric(g0) ([[eq:bondi-s-def]], [[prop:vaidya]] (a)), and μ′ = (2/9) A² env²
([[eq:mu-rate]]). μ − μ0, μ′ and μ″ enter g0 − η = μ r⁻² dv dv and its derivatives with order 2 and degree 2. The static
part μ0 r⁻² enters the inverse metric through −(μ/r²) ℓℓ, which raises the order of what it acts on by 4, and the terms
of Γ[g0] it produces have order at least 3. ∂_v keeps the order; ℓ and r⁻¹ Ω raise it by 1. A term of S_(7/2) has order
7/2 and contains a factor from u. No factor has order ½, so its factors are either G_3 together with one factor of order
2 (G_4, μ − μ0, μ′ or μ″, with ∂_v-derivatives), of degree 3, or G_3 with two order-raising derivatives, which comes
from the flat operator. The latter: by [[eq:wave-operator-vr]], for Z(v, x̂) smooth,

    □̃(r^(−p) Z) = (3 − 2p) r^(−p−1) ∂_v Z + r^(−p−2) (Δ̊ + p² − 2p) Z − μ p(p + 1) r^(−p−4) Z,
                                                                                                    {#eq:own-box-p}

so □̃(r^(−3/2) G_3) = r^(−7/2)(Δ̊ − ¾) G_3 − (15/4) μ r^(−11/2) G_3, and the forcing [[eq:bondi-f1]] carries
+½ □̃(r^(−3/2) G_3). The other term of the forcing of u_4 at order 7/2, ½ (g_λ^(ab) − g0^(ab)) ∂_a ∂_b (r⁻² G_4), and the
terms of S(u) at that order have degree 3. Hence S_(7/2) = ½(Δ̊ − ¾) G_3 + C_(7/2), with C_(7/2) a finite sum of products
of a v-derivative of G_3 with a v-derivative of one of G_4, μ − μ0, μ′, μ″, with coefficients smooth in x̂, and
G_5 = ∫_(v_start)^v S_(7/2) dv′.

(a) For v ≥ v_end, env = 0, so G_3 and all its v-derivatives vanish, and every term of S_(7/2) contains one: ∂_v G_5 =
S_(7/2) = 0.

(b) By (a) and the order count, G_5^∞ = ∫ S_(7/2) dv = ½(Δ̊ − ¾) ∫ G_3 dv + ∫ C_(7/2) dv, and ∫ G_3 dv =
λ A h (T_F ∫ env sin(ωv) dv + T_G ∫ env cos(ωv) dv) = A λ h (T_F Im ê(ω) + T_G Re ê(ω)).

(c) |ê(ω)| ≤ ‖env^(n)‖_(L¹) ω^(−n) for every n (n integrations by parts), so a_1 = O(λ^∞). For a_3 use the phase θ = v/λ.
A function [f] = f(v, x̂, v/λ) with f smooth and 2π-periodic in θ has ∂_v[f] = [∂_v f] + λ⁻¹[∂_θ f], which keeps its
harmonics in θ. G_3 has the harmonics ±1, so S_3 = Σ_(k∈{0,±2}) P_k(v, x̂) e^(ikv/λ), with P_k smooth, supported in
v ∈ [v_start, v_end] and polynomial in λ^(±1). Integrating by parts n times, for k = ±2,

    ∫_(v_start)^v P_k e^(ikv′/λ) dv′ = Σ_(j<n) (−1)^j (λ/(ik))^(j+1) ∂_v^j P_k(v) e^(ikv/λ) + O(λ^(n−c)),

uniformly in v, with c fixed by the powers of λ⁻¹ in P_k. So G_4 is a sum of terms with the harmonics 0 and ±2 plus
O(λ^(n−c)), and so are μ − μ0, μ′, μ″ (harmonic 0). C_(7/2) is then Σ_(k∈{±1,±3}) Q_k(v, x̂) e^(ikv/λ) + O(λ^(n−c′)),
with Q_k smooth and supported in [v_start, v_end], because each term contains a factor of G_3, of odd harmonic, and one
of harmonic 0 or ±2. Each ∫ Q_k e^(ikv/λ) dv, k ≠ 0, is O(λ^m) for every m, by m integrations by parts; so a_3 = O(λ^∞).

(d) The eigenvalues of Δ̊ − ¾ on S³ are −l(l + 2) − ¾ = −(l + ½)(l + 3/2) ≠ 0, so it is injective; h > 0; T_F and T_G
are linearly independent and spatial. So a_1 is spatial and vanishes exactly when Im ê(ω) = Re ê(ω) = 0. ê is entire,
and not identically zero, as env ≢ 0. Every factor of a_1 and a_3 is an iterated integral over [v_start, v] of products
of smooth compactly supported functions of v with e^(±ikωv), times polynomials in ω^(±1); so a_1 and a_3 are
real-analytic in ω > 0. If two amplitudes A_1 ≠ A_2 had vanishing spatial components of G_5^∞ for all ω ≥ 1/λ_P, then,
dividing by A_i, a_1 + A_i² a_3^sp = 0 for i = 1, 2 on that interval, a_3^sp the spatial part of a_3; subtracting, a_3^sp
= 0 and then a_1 = 0 there, hence for all ω > 0 by analyticity, and ê = 0 on (0, ∞), a contradiction. For any other A > 0
some spatial component of G_5^∞ at some x̂ is a real-analytic function of ω that is not identically zero, and its zeros
are isolated. ∎

**Remark {#rem:own-no-tail-approximant}** (the approximant carries no tail). In the approximant from past null infinity
([[thm:past-approximant]]) a term of order k/2 in the expansion of a profile carries phase harmonics of the parity of k:
W_TT has order 3/2 and harmonic ±1, χ order 2 and harmonic ±2 ([[eq:past-classes]]), g0 integer orders and harmonic 0.
Products, ∂_v, ℓ, Ω, ∂_θ, the transports of [[lem:decay-calculus]] (d) (leading term −r^(1−q) f_q/(q − 5/2)), the mean
integrals 2/(2q − 5) ∫ S_q and the phase integrals from past null infinity each change k by an even number or not at
all, and keep the parity; a mean over θ is nonzero only on even harmonics. So the means m_j have only integer orders, and
after the shell, where g_app − g0 = Σ_j λ^j m_j ([[lem:vii-1-1]]), g_app − g0 has no term of half-integer order. The
coefficient G_5^∞ is therefore carried by g_λ − g_app, in agreement with (c): its two-scale expansion vanishes at every
order in λ.

**Remark {#rem:own-tail-bump}** (Numerical observation.) For the bump envelope env_b(v) = exp(−1/(1 − y²)),
y = (v − 2)/(3/2), on [½, 7/2], e^(−2iω) ê_b(ω) is real, env_b being even about v = 2, so a_1 vanishes exactly at the
real zeros of that function. Evaluated numerically, ê_b(1/λ) ≠ 0 at λ = 2⁻¹, …, 2⁻⁷ (|ê_b| from 0.297 down to
3.4 × 10⁻⁸, falling faster than λ⁵ over [2⁻⁷, 2⁻⁵]), and the first zeros are at ω ≈ 3.331, 5.926, 8.399, 10.81: the
exceptional set of [[prop:own-tail]] (d) is infinite for this envelope, and accumulates only at λ = 0. For the envelope
sin⁴(π(v − ½)/3), which is C³ but not C^∞ at its ends, |ê(ω)| ω⁵ stays between 17 and 61 for ω = 10, …, 320, so a_1 is of
order λ⁶ there rather than O(λ^∞). No proof uses these values.

### The stability theory in the half-integer class {#sec:own-half-class}

**Definition {#def:own-half-class}** (the half-integer class). ℰ_0^½ := {(2 + j/2, 0) : j ∈ ℕ_0}, and ℰ_0^ℤ := {(j, 0) :
j ∈ ℕ, j ≥ 2} is the class [[eq:vii-0-1]]. For an index set E_0 with min Re E_0 > 3/2 + 2γ_Υ, ⟨E_0⟩ denotes the smallest
index set containing E_0 and satisfying (2)–(3) of [[def:iii-c-3-1]] ([[lem:iii-c-3-2]] (e)), and the proof of
[[thm:iii-c1-3-1]] builds the sets

    ℰ^((0))(E_0) := ⟨E_0⟩,     ℰ^((m+1))(E_0) := ⟨E_0 ∪̄ ℰ^((m))(E_0)⟩,                              {#eq:own-iterates}

taking ℰ_I^C := ℰ^((J))(E_0), J the number of its repetitions. We write k(F, z) for the largest log order of an index set
F at z ([[def:s11-b-analysis]] (4)), and 𝒵_Υ := {(3/2 + s, 0) : s ∈ σ_Υ} for the set of points that [[eq:iii-c-3-1]]
adjoins to ℰ_I^C (each with its translates by ℕ_0).

**Lemma {#lem:own-half-admissible}** (the class is admissible). ℰ_0^½ is an index set, closed under sums, with
min Re ℰ_0^½ = 2 > 3/2 + 2γ_Υ. Row d1 of [[sec:vi-c-1]] holds for ℰ_0^½ and every ℓ0 ∈ (3, 4) ∖ {7/2}.

*Proof.* (2 + j/2) + (2 + j′/2) = 2 + (j + j′ + 4)/2, so ℰ_0^½ + ℰ_0^½ ⊂ ℰ_0^½ and jℰ_0^½ ⊂ ℰ_0^½; it is closed under +
ℕ_0 and has finitely many elements below every real number. γ_Υ < ¼ (row u4), so 3/2 + 2γ_Υ < 2. Re π_1 ℰ_0^½ meets (3,
4) only at 7/2, so ℓ0 ∉ Re π_1 ℰ_0^½, and ℓ0 > 3. ∎

**Lemma {#lem:own-words}** (the smallest set by words). Let A be an index set with min Re A > 3/2 + 2γ_Υ. Then ⟨A⟩ is
the set of pairs (z, k) with

    z = z_1 + ⋯ + z_r − (r − 1) + j,     0 ≤ k ≤ k_1 + ⋯ + k_r,                                          {#eq:own-word}

r ≥ 1, j ∈ ℕ_0, each (z_i, k_i) in A ∪ 𝒵_Υ, and (z_1, k_1) ∈ A when r = 1.

*Proof.* Let W(A) be the set described. *W(A) ⊂ ⟨A⟩*, by induction on r. For r = 1 this is A ⊂ ⟨A⟩ and the index set
property. For r ≥ 2 the word with the first r − 1 factors lies in ⟨A⟩ ∪ 𝒵_Υ ⊂ ⟨A⟩^tot (in 𝒵_Υ only when r − 1 = 1 and
its factor lies there), so adding z_r − 1 gives an element of ⟨A⟩^tot + (⟨A⟩^tot − 1) ⊂ ⟨A⟩, by (3) of
[[def:iii-c-3-1]], with log order the sum; translations by ℕ_0 and lower log orders stay in ⟨A⟩. *⟨A⟩ ⊂ W(A).* W(A) is
closed under + ℕ_0 and under lowering the log order. Every z_i has real part at least 3/2, so a word with r ≥ 2 factors
has real part at least r/2 + 1; below any C there are therefore finitely many r, finitely many factors and finitely many
j, and W(A) is an index set. It contains A, its minimum real part is at least min(min Re A, 2) > 3/2 + 2γ_Υ, and the
sum of two elements of W(A) ∪ 𝒵_Υ minus 1 is a word with r_1 + r_2 ≥ 2 factors: W(A) satisfies (2)–(3) of
[[def:iii-c-3-1]]. ∎

**Proposition {#prop:own-same-index-sets}** (the same index sets). For every m ≥ 0,
ℰ^((m))(ℰ_0^½) = ℰ^((m))(ℰ_0^ℤ), and in this set k(n + ½) = k(n) for every integer n ≥ 2. Consequently, if the weights
in the proof of [[thm:iii-c1-3-1]] are chosen the same for ℰ_0^½ and ℰ_0^ℤ (each is chosen off a discrete set, and the
union of the two classes' sets is discrete), then ℰ_I^C is the same for the two classes, and so are Λ, the exclusion sets
of row d2, the conditions (G) and (G⁺), and the admissible ε_+, ε_K and α of rows w1–w2.

*Proof.* Write E := ℰ_0^ℤ, E′ := ℰ_0^½, F_m := ℰ^((m))(E), L := ½ℤ, and W_L(A) for the set of words [[eq:own-word]] whose
factors lie in A ∪ {(3/2, 0)}. Put F^L_0 := W_L(E) and F^L_(m+1) := W_L(E ∪̄ F^L_m). By [[lem:own-words]] and the
monotonicity of ∪̄ and of words in their arguments, F^L_m ⊂ F_m. Every element of F^L_m has its first component in L, and
F^L_m is closed under (z, k) ↦ (z + ½, k): adjoining the factor (3/2, 0) to a word adds ½ to its value.

*Step 1 (lattice points have lattice words).* We show by induction on m: for every (z, k) ∈ F_m there are (z′, k) ∈ F^L_m
and c ∈ ℕ_0 δ_♯ + ℕ_0 γ_Υ, δ_♯ = (1 − e_Υ)γ_Υ, with z = z′ + c; and every (z, k) ∈ F_m with z ∈ L lies in F^L_m. The
second statement follows from the first: c = z − z′ lies in L and c ≥ 0, so c = q/2 with q ∈ ℕ_0, and (z, k) =
(z′ + q/2, k) ∈ F^L_m. For the first, each element of 𝒵_Υ is (3/2, 0) plus s ∈ σ_Υ ⊂ ℕ_0 δ_♯ + ℕ_0 γ_Υ. For m = 0 replace
every factor (3/2 + s, 0) of a word over E ∪ 𝒵_Υ by (3/2, 0). For m ≥ 1 the factors of a word for F_m lie in
𝒵_Υ or in A_m := E ∪̄ F_(m−1), whose elements are elements of E, elements of F_(m−1), or pairs (p, l + 1) with p ∈ π_1E
an integer and (p, l) ∈ F_(m−1) (with their translates and lower log orders). An element of F_(m−1) has a shadow in
F^L_(m−1) by induction; for a pair (p, l + 1), (p, l) ∈ F^L_(m−1) by the second statement at m − 1, so (p, l + 1) ∈ E ∪̄
F^L_(m−1). Replacing every factor by its shadow gives a word of W_L(E ∪̄ F^L_(m−1)) = F^L_m with the same log order and a
value smaller by a sum of elements of ℕ_0 δ_♯ + ℕ_0 γ_Υ.

*Step 2 (k(n + ½) ≤ k(n) in F_m).* For m = 0 every factor of a word in W_L(E) has log order 0, so by Step 1 every point
of F_0 in L has log order 0, and n ∈ π_1 F_0 for n ≥ 2. Let m ≥ 1, assume the claim for F_(m−1), and let (n + ½, k) ∈
F_m, n ≥ 2 an integer. By Step 1 it is a word [[eq:own-word]] with factors in (E ∪̄ F^L_(m−1)) ∪ {(3/2, 0)}. If r ≥ 2 and
some factor is (3/2, 0), remove it: the value drops by ½, the log order is unchanged, and if one factor remains it lies
in E ∪̄ F^L_(m−1) (two factors (3/2, 0) give an integer value). Otherwise every factor lies in E ∪̄ F^L_(m−1) ⊂ L × ℕ_0,
and as the value lies in ½ + ℤ, some factor (h, k_h) has h ∈ ½ + ℤ, h ≥ 5/2. E has no exponent at h, so k_h ≤ k(F_(m−1),
h) ≤ k(F_(m−1), h − ½), while E ∪̄ F^L_(m−1) has at the integer h − ½ ≥ 2 the log order k(F_(m−1), h − ½) + 1 (Step 1 at
m − 1 identifies the log orders of F^L_(m−1) and F_(m−1) on L). Replace (h, k_h) by (h − ½, k_h). In both cases (n, k)
is a word of F^L_m ⊂ F_m.

*Step 3 (equality).* ⟨E⟩ ⊂ ⟨E′⟩ as E ⊂ E′, and E′ ⊂ ⟨E⟩ since (n + ½, 0) is the word (n, 0) + (3/2, 0) − 1; so ⟨E′⟩ =
⟨E⟩. Let m ≥ 1 and F_(m−1) = ℰ^((m−1))(E′). E ∪̄ F_(m−1) ⊂ E′ ∪̄ F_(m−1), so F_m ⊂ ℰ^((m))(E′). Conversely, E′ ∪̄ F_(m−1)
differs from E ∪̄ F_(m−1) ∪ E′ only by the pairs (h, k(F_(m−1), h) + 1), h ∈ ½ + ℤ, h ≥ 5/2, and their lower log orders.
(h − ½, k(F_(m−1), h − ½) + 1) lies in E ∪̄ F_(m−1) ⊂ F_m, and F_m + ½ ⊂ F_m ([[lem:iii-c-3-2]] (a)); so
(h, k(F_(m−1), h − ½) + 1) ∈ F_m, and k(F_(m−1), h − ½) ≥ k(F_(m−1), h) by Step 2. Hence E′ ∪̄ F_(m−1) ⊂ F_m and
ℰ^((m))(E′) ⊂ F_m. Finally k(n + ½) ≥ k(n) by [[lem:iii-c-3-2]] (a), and ≤ by Step 2.

*The consequences.* The proof of [[thm:iii-c1-3-1]] chooses its weights α_1 and α′ off Re π_1E_0, off 3/2 + σ_Υ and
below ℓ_I, each from an interval minus a discrete set; with the same choices for the two classes the number J of
repetitions is the same, and ℰ_I^C = ℰ^((J)) is the same. Step (3) of [[thm:vi-c-2-1]] fixes Λ from ℰ_I^C and the gauge,
and rows d2, w1, w2 and b4 depend on ℰ_0 only through ℰ_I^C and Λ. ∎

**Theorem {#thm:own-half-settling}** (the stability theorem in the half-integer class). Let ℓ0 ∈ (3, 4) ∖ {7/2} and
ℓ_I ∈ (3, ℓ0) off the exclusion sets of row d2. Make the choices of [[thm:vi-c-2-1]] as for [[eq:vii-0-1]] with these ℓ0
and ℓ_I, the weights of [[thm:iii-c1-3-1]] as in [[prop:own-same-index-sets]], and take ℰ_0 := ℰ_0^½ in its step (3).
Then [[thm:iii-k-4-3]], [[prop:vii-3-2]] and [[cor:s27-rate]] hold with ℰ_0 = ℰ_0^½, with ε and d_1 chosen in step (6)
for this class. In particular G-invariant vacuum data (γ, k) on Σ^IVP with γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b,
k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b and norm below the threshold have a G-invariant vacuum development which settles to a
Tangherlini metric g_(m′,0), |m′ − m0| < ε_m, at the rate O(t_*^(−2−ε_t)) of [[eq:s27-rate]], for every ε_t < ε_K.

*Proof.* Every result of [[part:stability]]–[[part:stability-nonlinear]] that involves ℰ_0 is stated for an index set
satisfying row d1 (the setting of [[sec:iii-k-0]]): [[thm:iii-c1-3-1]], [[thm:iii-c2-3-1]], [[prop:iii-c2-4-1]] (any
index set with positive minimum real part, closed under positive multiples), [[cor:iv3-2-3]], [[lem:viii-1-1]],
[[thm:iii-k-4-3]], [[prop:vii-3-2]] and [[cor:s27-rate]], with the norm of [[sec:s27-class]] built from ℰ_0. Row d1 holds
by [[lem:own-half-admissible]]. By [[prop:own-same-index-sets]], ℰ_I^C and Λ are those of [[eq:vii-0-1]], so rows d2,
w1, w2 and b4 hold with the same choices, and step (6) chooses ε and d_1 for ℰ_0^½. ∎

**Remark {#rem:own-half-changes}** (what the class changes). (a) H^(∞,(ℰ_0^ℤ,ℓ0))_b lies continuously in
H^(∞,(ℰ_0^½,ℓ0))_b (the new coefficients are 0), so the bound of [[lem:vii-0-1]] holds in the larger class. (b) Step 1 of
the proof of [[thm:iii-c1-3-1]] applies R = Π_((z,k)∈ℰ_(0,≤))(X_0 − z), with one factor for each exponent of ℰ_0 up to
the weight reached: at the last step R has 3 factors for ℓ0 ∈ (3, 7/2) and 4 for ℓ0 ∈ (7/2, 4), against 2 for ℰ_0^ℤ,
and each factor costs one derivative (the converse part of [[lem:iii-a-1-3]]). So d_1 changes by a finite amount, and ε
with it; the thresholds λ1 and δ of [[thm:settling]] change accordingly. None of ε, d_1, λ1, δ is evaluated, in either
class. (c) The weights α_1, α′ avoid finitely many more points in each bounded interval.

### The construction from past null infinity at every order {#sec:own-orders}

The data of g_λ on N are controlled by [[thm:past-construction]] at a fixed order of derivatives. This section takes that
order to be arbitrary, with constants polynomial in λ⁻¹ and independent of the order K of the approximant.

**Proposition {#prop:own-far-order}** ([[prop:far-region]] at every order). Let k ≥ 6 and let the approximant have an
order K′ > 5, so that |Ric^H(g_app)|_(k,P) ≤ C_R(k) λ^(K′) t_P^(−3/2). There are λ_F(k) > 0 and M_F(k), independent of
τ_n, such that the conclusions of [[prop:far-region]] hold with [[eq:far-energy]] at order k.

*Proof.* The proof of [[prop:far-region]] uses k at five places. (a) The bootstrap assumption gives through
[[lem:past-sobolev]] the bounds of w_n and ∂w_n, hence the margin of [[lem:past-domain]] (f) and w_n = 0 on
{v ≤ v_start} ([[lem:seed-region]]); this needs k ≥ 3 only. (b) In the commuted equation, λ^i ∂^i Ω^β of the 1/λ term is
at most C_k λ⁻¹ t_P^(−3/2) E by Leibniz's rule, every factor λ^(i₂) ∂^(i₂) Ω^(β₂) G2 being bounded by C_k t_P^(−3/2), G2
a profile in E_(3/2), and the factors of s by C E ([[lem:past-sobolev]] (b) for the undifferentiated one); B·∂w and C·w,
and the commutators, give C_k t_P^(−3/2) E. (c) A nonlinear monomial at order j ≤ k has total w-order at most j + 2 and
no factor of order j + 2; put its factor of highest order in L² and the others in the supremum norm through
[[lem:past-sobolev]] (a), which costs three orders. The second-largest order is at most ⌊(k + 2)/2⌋, and
⌊(k + 2)/2⌋ + 3 ≤ k + 1 for k ≥ 5; so these terms are at most C_k λ⁻⁵ t_P^(−3/2) E². (d) The residual gives
C_R(k) λ^(K′) t_P^(−3/2). (e) Over t_P ≥ λ⁻² the kernels C_k t_P^(−3/2) and C_k λ⁻¹ t_P^(−3/2) integrate to at most 2C_k
λ and 2C_k, the data at τ_n are fixed by the residual as in the proof of [[prop:far-region]], and Gronwall's inequality
gives E(τ) ≤ C_k e^(2C_k(1+λ)) (3C_R(k) λ^(K′) + C_k M_F² λ^(2K′−5)) t_P^(−1/2) ≤ M_F λ^(K′) t_P^(−1/2) with
M_F = M_F(k) := 4C_k e^(6C_k) C_R(k) + 1, for λ ≤ λ_F(k), since 2K′ − 5 > K′. Existence and continuation are Step 8 of
the proof of [[thm:uniform-existence]] at the regularity k. ∎

**Proposition {#prop:own-near-order}** ([[prop:near-region]] at every order). For k ≥ 6 let C(k) be the sum of the
constants of [[eq:near-lines]] at the orders j ≤ k, β0(k) := max(2, 4C(k) + 1), and let the approximant have
N_k := K + 4 + ⌈4β0(k)⌉ stages, K ≥ 6, so that K′ = N_k − 1. There are λ_N(k) > 0 and M_N(k) such that
[[eq:near-bootstrap]] holds at order k with β0(k), and 𝒩_P(τ0) ≤ M_N(k) λ^(K′−2β0(k)).

*Proof.* The proof of [[prop:near-region]] at order k: its data come from [[prop:own-far-order]]; every line of
[[eq:near-lines]] holds at every order j ≤ k with c0 unchanged, the commutation fields commuting with L0 and
[Z, r^(−c)] carrying r^(−c−1); each integral of a bootstrap quantity returns at most C(k)/(β0(k) − 1) ≤ ¼ of its bound;
and the nonlinear ratios are at most C″ λ^(K′−8−4β0(k)), which is at most 1/8 for λ small because
K′ = K + 3 + ⌈4β0(k)⌉ ≥ 9 + 4β0(k). ∎

**Corollary {#cor:own-p-order}** ([[thm:past-construction]] at every order). Let k ≥ 6 and K ≥ 6, and let g_app be the
approximant with N_k stages. There is λ_P(K, k) > 0 such that for λ ≤ λ_P(K, k) the solution g_λ of
[[thm:past-construction]] satisfies [[eq:far-energy]] at order k on the far region, and on P

    |∂^i Ω^β (g_λ − g_app)| ≤ C_k λ^(K−3−i) t_P⁻²,     i + |β| ≤ k − 3.                                   {#eq:own-p-iii}

*Proof.* The proof of [[thm:past-construction]] at order k: the data of w_n at τ0 by [[prop:own-near-order]];
[[thm:uniform-existence]] at the regularity k, whose proof uses k only through Sobolev indices, as in the proof of
[[lem:vii-1-1]]; and the limit n → ∞, the bounds at order k being inherited by weak lower
semicontinuity. The solution built at order k is g_λ: the two approximants differ by Σ_(j>N_6) λ^j [g_j] = O(λ^(N_6))
t_P^(−3/2) in C¹, so the solution at order k lies in the uniqueness class of item 5 of [[thm:past-construction]] for the
order 6. The energies E and 𝒩_P contain the rotations, which cost no power of λ, and [[lem:past-sobolev]] (a) costs three
derivatives in ∂_r and Ω; on the near region (T_λ/t)^(β0(k)) ≤ λ^(−2β0(k)) is absorbed by K′ − 2β0(k) ≥ K + 3. This gives
[[eq:own-p-iii]]. ∎

So no order fails; what grows with k is the number of stages N_k, and λ_P(K, k) decreases.

**Proposition {#prop:own-poly}** (the powers of λ at past null infinity). For J ≥ 4 and n, m ≥ 0 there are C and
λ_0 > 0, depending on J, n, m and the data (seed, A, env, angular profile) and not on K, such that for 0 < λ ≤ λ_0, on
{t_P ≥ λ⁻² + d1} and for |α| + |β| ≤ n, in the expansion of [[prop:bondi-hierarchy]],

    |∂_X^α Ω^β ℓ^m u_J| ≤ C λ^(−(3J−9+|α|+m)) r^(−(J+1)/2−m),
    |∂_X^α Ω^β G_k| ≤ C λ^(−(k−4+|α|))  (k ≥ 3).                                                    {#eq:own-poly}

*Proof.* Say that a quantity has λ-order p if it is bounded by C λ^(−p), and write B_J for the λ-order of u_J in
[[eq:own-poly]] at α = 0, m = 0. *The base.* By [[cor:own-p-order]] at K = 6 and order n + 4, which gives the same g_λ
for λ ≤ λ_P(6, n + 4), |∂^α Ω^β (g_λ − g_app)| ≤ C λ^(3−|α|) t_P⁻²; and g_app − g0 − r^(−3/2) G_3 is the sum of λ m_1, of
λ[χ dv dv], of the phase-shift terms and of λ^j [g_j], j ≥ 2, each of λ-order at most |α| − 1 under ∂^α Ω^β (a derivative
of an oscillating factor costs λ⁻¹, a rotation nothing, Ω v = 0) and of class E_2 ([[eq:past-classes]]). So
|∂^α Ω^β u_1| ≤ C λ^(1−|α|) t_P⁻²: B_3 = −1, every derivative ∂_X costing one order and Ω none. Likewise
G_3 = λ[W_TT] r^(3/2) has λ-order −1 + |α| under ∂^α, that is k − 4 + |α| at k = 3.

*The trade.* On t_P ≥ λ⁻² + d1, r ≥ λ⁻², so r^(−1/2) ≤ λ: a quantity of λ-order p bounded by r^(−ρ) is of λ-order
p − 2(ρ − ρ′) as a bound by r^(−ρ′), for ρ′ ≤ ρ. In particular u_J = u_1 − Σ_(k=4)^J r^(−k/2) G_k has |∂^d u_J| ≤
C λ^(−d) r⁻² there, given the claimed orders of the G_k (r^(−k/2) λ^(−(k−4)) ≤ r⁻²).

*The step J → J + 1.* By [[lem:bondi-half-order]] and the proof of [[prop:bondi-hierarchy]], u_(J+1) = u_J −
r^(−(J+1)/2) G_(J+1) solves −½ g_λ^(ab) ∂_a ∂_b u_(J+1) = S′, S′ of r-order (J + 4)/2, and G_(J+1) = (2/(J − 2)) ∫ S_q,
q = (J + 3)/2. The forcing is a polynomial in (u, ∂u, ∂²u) with coefficients smooth in (X, g); after expansion its
monomials are products of m₁ ≥ 1 factors from {G_3, …, G_J, u_J} (with their r-powers), with a coefficient built from η,
μ r⁻², Γ[g0], ∂∂g0 or (∂g0)², whose r-order is c ∈ {0} ∪ [2, ∞) and whose λ-order is 0, and with at most two
derivatives, each a ∂_v (λ-order +1, r-order 0) or an order-raising derivative ℓ, r⁻¹Ω (λ-order 0, r-order +1). For a
monomial, λ-order minus twice r-order is a sum over its parts: −4 for each factor G_k or for a factor u_J bounded crudely
by λ^(−d) r⁻² (with its own derivatives counted separately), +1 for each ∂_v, −2 for each order-raising derivative and
−2c for the coefficient. After the trade to r-order (J + 4)/2 its λ-order is that sum plus J + 4.

The explicit monomials (no u_J) have λ-order at most J − 2. With c = 0 and one factor they are the flat operator applied
to r^(−k/2) G_k, which by [[eq:own-box-p]] has no ∂_v∂_v term: its terms of r-order at least (J + 4)/2 have two
order-raising derivatives and λ-order J − 4. Otherwise c ≥ 2 or m₁ ≥ 2, and the sum is at most −4m₁ + 2 − 2c ≤ −6,
giving J − 2. The term (g_λ⁻¹ − g0⁻¹) ∂_v² (r^(−(J+1)/2) G_(J+1)) of S′ has λ-order (J − 3) − 1 + 2 = J − 2 at r-order
(J + 4)/2. A monomial with one factor u_J bounded sharply, of λ-order B_J + d₀ at r-order (J + 1)/2, has after the trade
the λ-order B_J + d₀ + 3 + (the sum over its other parts) ≤ B_J + 5 − 4m′ − 2c, m′ the number of other factors. Linear
terms with c = 0 belong to the operator, so either m′ ≥ 1 or c ≥ 2, and the λ-order is at most B_J + 1; with two or more
factors u_J, all but one bounded crudely, the same count gives at most B_J + 1. So S′ has λ-order at most
max(B_J + 1, J − 2), each derivative of S′ costing one more. The energy step of [[lem:bondi-half-order]] is free of λ on
the far region (its kernel is ‖∂g_λ‖_∞ ≤ C t_P^(−3/2), and ∂(λ[W_TT]) has λ-order 0), [[lem:past-sobolev]] (a) costs two
orders in ∂_r beyond the energy, and each ℓ-derivative in the transport of [[lem:bondi-half-order]] at most one. So
B_(J+1) = 2 + max(B_J + 1, J − 2) = B_J + 3, and B_J = 3J − 9. The coefficient S_q of r^(−q) involves the G_k, k ≤ J,
only; by the same count its λ-order is at most J − 3, and the integral over v costs nothing: G_(J+1) has λ-order
(J + 1) − 4. ∎

**Lemma {#lem:own-means}** (the means at past null infinity). For every stage j ≥ 1 and J ≥ 4 there are smooth tensors
M_(j,k)(v, x̂), k = 4, …, J, independent of λ and vanishing for v ≤ v_start, with m_j = Σ_(k=4)^J r^(−k/2) M_(j,k) +
m_(j,J), ∂_X^α Ω^β ℓ^m m_(j,J) in E_((J+1)/2+m) on P⁺ with constants independent of λ, and no logarithm. For v ≥ v_end
every M_(j,k) is a polynomial in v, and for k ≤ 9 the coefficients satisfy there the flat recursion

    (2q − 3) ∂_v M_(j,2q) = (Δ̊ + (q − 1)(q − 3)) M_(j,2q−2),                                {#eq:own-flat-recursion}

so that M_(j,k) has degree at most ⌊(k − 4)/2⌋ in v there.

*Proof.* Induction on the stage j and, within it, on J, as in the proof of [[prop:bondi-hierarchy]], for the stage
system (a)–(c) of [[lem:stage-system]] on P ([[thm:past-approximant]]), whose coefficients and forcing terms are
polynomials in the profiles of the earlier stages (expanded by the induction), in W_TT, χ and in g0 (W_TT = r^(−3/2) F_W,
χ = r⁻² X(v, x̂, θ), g0 − η = μ r⁻² dv dv). The wave equation (a) is [[lem:bondi-half-order]] with g0 in place of g_λ
(no quasilinear term): ũ = m_j, forcing r^(−q) S_q + S̃ with q ≥ 3, and (H_m) from the induction. The transport (c) is
[[lem:decay-calculus]] (d), iterated: at each order the leading term −r^(1−q) S_q/(q − 5/2) and a remainder whose forcing
gains ½. The transport (b), L0 φ_j = −½ m_j(ℓ, ℓ) − ½ q_j, integrated along ℓ from past null infinity, maps r^(−q) S to
−r^(1−q) S/(q − 1). The threshold q = 5/2 of (a) and (c) and q = 1 of (b) are never met: by the count in the proof of
[[thm:past-approximant]], the unknowns enter (a) with coefficients in E_2 (for m_j), E_3 (for dφ_j) and E_(3/2) (for
ĝ_(j+1)), and (c) with coefficients in E_(3/2) (for m_j, Ψ_j and ℓφ_j) and E_(5/2) (for ∂_v φ_j and r⁻¹ Ω φ_j), while
m_j, ℓφ_j, Ψ_j, r⁻¹ Ω φ_j are in L_2, φ_j and ∂_v φ_j in L_1 and ĝ_(j+1) in O_2, and the known forcing terms lie in L_3;
so every input of (a) and (c) has exponent at least 3 and every input of (b) at least 2, and each order adds ½.
After the shell every oscillating profile vanishes ([[lem:own-domain]] (v)) and μ = μ_end. The forcing terms of the stage
equations are then products of earlier means and terms in μ: two factors r⁻² with two derivatives, a ∂_v of a leading
coefficient vanishing by the induction (∂_v M_(i,4) = ∂_v M_(i,5) = 0 there, by [[eq:own-flat-recursion]] with M_(i,2) =
M_(i,3) = 0), or −(μ/r²) ℓℓ, Γ[g0]·∂ and ∂∂g0, which add r⁻² to r⁻⁴ to a factor r⁻²; every one is O(r⁻⁶). So they enter
only from q = 6, and through k = 9 the coefficients obey the flat recursion of [[lem:bondi-half-order]], which reads
[[eq:own-flat-recursion]] by [[eq:own-box-p]] at μ = 0 and raises the degree in v by one every second order; from q = 6
on, products of polynomials and the constant μ keep the coefficients polynomial in v. ∎

On {v > v_end}, g_app − g0 = Σ_j λ^j m_j ([[lem:vii-1-1]]), so for the remainder e := g_λ − g_app there the expansions of
[[prop:bondi-hierarchy]] and [[lem:own-means]] give

    e = Σ_(k=4)^8 r^(−k/2) e_k + e_(8),     e_k := G_k − Σ_j λ^j M_(j,k),     e_(8) := u_8 − Σ_j λ^j m_(j,8),
                                                                                                    {#eq:own-e-expansion}

and by [[eq:own-poly]] and [[lem:own-means]], |∂_X^α Ω^β ℓ^m e_(8)| ≤ C λ^(−(15+|α|+m)) r^(−9/2−m) on {t_P ≥ λ⁻² + d1}.

**Lemma {#lem:own-interpolation}** (interpolation). Let d ≥ 0, P(y) = Σ_(i=0)^d c_i y^i, σ > 0, and |P| ≤ η on [σ/2, σ].
Then |c_i| ≤ L_d σ^(−i) η, where L_d is the largest row sum of the absolute values of the inverse of the Vandermonde
matrix of the d + 1 nodes y_l := ½ + l/(2d), l = 0, …, d (L_0 := 1).

*Proof.* Q(y) := P(σy) = Σ_i c_i σ^i y^i satisfies |Q(y_l)| ≤ η, and its coefficients are the inverse Vandermonde matrix
applied to (Q(y_l))_l. ∎

**Lemma {#lem:own-e-flux}** (the coefficients and the remainder of e on N). Let a ∈ (0, 7/2), j ≥ 0, M ≥ 15 + 2(j + 1),
θ_k := (k − 4)/5, s_R := max(5/2, (2M + 1)/(7 − 2a)), and

    K*(a, M, j) := max{ 4 + j + s_R (a + j);  3 + i + (s_R max(0, 2a + 2 − k)/2 + (M + i) θ_k)/(1 − θ_k) :
                        4 ≤ k ≤ 8, 0 ≤ i ≤ j + 1 }.                                                    {#eq:own-kstar}

Let K > K*(a, M, j), let k_P ≥ j + 5, and let g_λ satisfy [[eq:own-p-iii]] at order k_P and [[eq:own-poly]] at n = k_P −
4.
(1) For 4 ≤ k ≤ 8, i ≤ j + 1 and i + |β| ≤ k_P − 4, |∂_v^i Ω^β e_k(v1, x̂)| ≤ C λ^((K−3−i)(1−θ_k)−(M+i)θ_k), and the
exponent exceeds 1 for i ≤ j.
(2) Let Γ ∈ {∂_t, Ω_ab, Z}, Z := (t − v1)∂_t + x·∂_x, and for φ on a neighbourhood of N put

    𝔉_N^a[φ] := ∫_N r^(2a) ( |ℓφ|² + r⁻² |∇̊φ|² + r⁻² |∂φ|² ) r³ dr dω,                              {#eq:own-flux-n}

∇̊ the gradient on S³. Then 𝔉_N^a[Γ^α e_(8)] → 0 as λ → 0 for every |α| ≤ j.

*Proof.* (1) On N at fixed x̂, put y := r^(−1/2), so that r² r^(−k/2) = y^(k−4). By [[eq:own-e-expansion]],
r² ∂_v^i Ω^β e = P(y) + r² ∂_v^i Ω^β e_(8) with P(y) := Σ_(k=4)^8 ∂_v^i Ω^β e_k(v1, x̂) y^(k−4), of degree 4. On the far
region of N, r and t_P are comparable, and |r² ∂_v^i Ω^β e| ≤ C λ^(K−3−i) by [[eq:own-p-iii]] (∂_v = ∂_t at fixed x is a
Cartesian derivative), while |r² ∂_v^i Ω^β e_(8)| ≤ C λ^(−(15+i)) y⁵ ≤ C λ^(−(M+i)) y⁵. So |P| ≤ η := C(λ^(K−3−i) +
λ^(−(M+i)) σ⁵) on [σ/2, σ]. Take σ⁵ := λ^(K−3+M); then η ≤ 2C λ^(K−3−i), and [[lem:own-interpolation]] gives
|∂_v^i Ω^β e_k| ≤ C λ^(K−3−i) σ^(−(k−4)) = C λ^((K−3−i)(1−θ_k)−(M+i)θ_k). The interval y ∈ [σ/2, σ] is r ∈ [σ⁻², 4σ⁻²],
in the far region for λ small since K − 3 + M > 5. For i ≤ j, the condition of [[eq:own-kstar]] at i + 1 ≤ j + 1 gives
(K − 4 − i)(1 − θ_k) > (M + i + 1) θ_k, that is (K − 3 − i)(1 − θ_k) − (M + i)θ_k > (1 − θ_k) + θ_k = 1.

(2) Let R := λ^(−s_R), which lies in the far region for λ small as s_R ≥ 5/2. *Above R*, by the bounds of e_(8) after
[[eq:own-e-expansion]] with the ℓ-gain, and Z = rℓ on N (Z(v − v1) = v − v1 and Z = (v − v1)∂_v + rℓ in (v, r, x̂)), the
integrand of [[eq:own-flux-n]] for Γ^α e_(8), |α| ≤ j, is at most C λ^(−2M) r^(2a−11+3), and its integral over r ≥ R is
C λ^(−2M) R^(2a−7) = C λ^(−2M + s_R(7−2a)) ≤ C λ, by the choice of s_R. *Below R*, write Γ^α e_(8) = Γ^α e −
Σ_(k=4)^8 Γ^α(r^(−k/2) e_k). For Γ^α e: Z = rℓ costs a factor r and a derivative, ∂_t a derivative, Ω nothing; on N ∩ Ω′
the bounds of [[thm:uniform-existence]] at order k_P hold with λ^(K−3−i), and on N ∩ P′ [[eq:own-p-iii]] holds; so every
derivative in [[eq:own-flux-n]] of Γ^α e is at most C r^j λ^(K−4−j) r⁻², and its integral over r ≤ R is at most
C λ^(2(K−4−j)) R^(2a+2j) = C λ^(2(K−4−j−s_R(a+j))) → 0 by the first entry of [[eq:own-kstar]]. For Γ^α(r^(−k/2) e_k(v,
x̂)) on N: ∂_t acts as ∂_v on e_k, Ω on x̂, and Z = rℓ multiplies r^(−k/2) by −k/2; the tangential derivatives in
[[eq:own-flux-n]] gain r⁻¹ and the transverse one costs one more ∂_v. So the integrand is at most C r^(2a+1−k) times
|∂_v^i Ω^β e_k(v1)|² with i ≤ j + 1, and the integral over r ≤ R is at most C R^(max(0, 2a+2−k)) (1 + log R)
λ^(2((K−3−i)(1−θ_k) −(M+i)θ_k)), which tends to 0 by the second entries of [[eq:own-kstar]]. ∎

