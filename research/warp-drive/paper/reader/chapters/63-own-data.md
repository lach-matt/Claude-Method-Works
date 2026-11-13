## The development of g_λ's own data settles {#ch:own-data}

[[thm:settling]] (i) concerns data that agree with those of g_λ on a ball and are continued equivariantly to exact
Tangherlini data beyond it. This chapter proves that the maximal vacuum development of the data that g_λ itself induces on
Hintz's initial surface Σ^IVP settles to five-dimensional Tangherlini, with no gluing, for every λ below a threshold and
with no exceptional set. The data class of [[thm:settling]] (ii) does not contain these data: after the shell the
difference g_λ − g0 carries at past null infinity a coefficient of r^(−5/2), of size O(λ^∞) but nonzero for all λ off a
discrete set, and it reaches the data at spatial infinity as a term ρ^(5/2), ρ := 1/r. The class is therefore widened by
the half-integer orders, and the stability theory runs in the wider class with the same index sets.

The argument has five parts. (1) The far part S := Σ^IVP ∩ {r ≥ 4R} of the initial surface has a past domain of dependence
W for Tangherlini, bounded by S, by an ingoing null cone N on which g_λ is known, and by past null infinity, where
nothing comes in after the shell (Section [[sec:own-far-part]]). (2) The tail at r^(−5/2) is computed
(Section [[sec:own-tail]]). (3) The stability theory holds in the half-integer class with the same index sets
(Section [[sec:own-half-class]]). (4) The constants of the construction from past null infinity are polynomial in
λ^(−1) at every order, which makes the data of g_λ on N small at every weight that the estimate below uses
(Sections [[sec:own-orders]] and [[sec:own-sigma]]). (5) After its self-similar terms through r^(−4) are subtracted,
g_λ continues to W by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence;
the continuation is vacuum, unique in a class of weight below ½, and its data on S lie in the half-integer class with
small norm (Sections [[sec:own-continuation]] and [[sec:own-vacuum]]). The theorem is assembled in
Section [[sec:own-proof]].

*Notation.* We use the chart (τ, x) of [[sec:background]], v = τ + r, the background g0 of [[eq:background]] and the gauge
of [[sec:gauge]]. Ω′ is the domain of the form [[eq:omega]], with constants (T′, δ′0) and inner radius a′ = q0 − δ′0, that
[[lem:vii-1-2]] chooses for a radius R ≥ R_3, with V′ := v_end + T′ and τ′_end its constants, and P′ is its past domain,
[[eq:past-domain]] with these constants: P′ := {τ ≤ τ0, |x| ≥ a′, v + h_P(τ) ≤ V′_P}, V′_P := V′ + 1 + (τ′_end − τ0) +
κ_P, κ_P = ½. g_λ is the solution of [[thm:past-construction]] on P′ ∪ Ω′ ([[thm:past-construction]] holds for every
domain of the form [[eq:omega]] and its past domain). On {v ≥ v_end}, μ = μ_end, and we write μ := μ_end in this chapter;
there g0 = g_b0 := η + μ r⁻² dv ⊗ dv, five-dimensional Tangherlini in Kerr–Schild form, whose Kerr–Schild time is τ
([[lem:vii-1-2]] (a)). In the far region we write t := τ, so that (t, x) are Kerr–Schild Cartesian coordinates and
v = t + r; the variable t of [[ch:past-construction]] is written t_P := 1 + τ0 − τ. We put 𝔪 := μ r⁻². For |x| ≥ R_3 the
initial surface is a graph, Σ^IVP ∩ {|x| ≥ R_3} = {t = f(|x|)}, with f′ ∈ |x|⁻² C^∞ near infinity ([[lem:vii-2-1]] and
the paragraph before it, with t_KS = τ up to a constant absorbed in f). Enlarging R, |f′| ≤ ¼ and 𝔪 ≤ 1/16 on r ≥ 4R.
G = O(2) × O(2) acts by (t, x) ↦ (t, Ox) ([[sec:s27-class]]).

**Theorem {#thm:own-data}** (the development of g_λ's own data settles). Fix A, the envelope env ∈ C_c^∞, the angular
profile and the seed. Let ℓ0 ∈ (3, 4) ∖ {7/2}, ℓ_I ∈ (3, ℓ0) off the exclusion sets of row d2 of [[sec:vi-c-1]], ε_m > 0
and 0 < ε_t < ε_K, the parameters of the stability theory chosen as for [[thm:settling]]. Let ε and d_1 be those of
[[thm:iii-k-4-3]] in the class ℰ_0^½ ([[def:own-half-class]], [[thm:own-half-settling]]), below the threshold of
[[prop:vii-3-2]] and that of [[cor:s27-rate]] for ε_m and ε_t. Let a ∈ (ℓ0 − 1, 3), k1 := max(8, d_1 + 4),
M := 15 + 2(k1 + 1), K > max(d_1 + 14, K*(a, M, k1)) with K* of [[lem:own-e-flux]], and let the approximant of
[[thm:past-approximant]] have K + 4 + ⌈4β0(k_P)⌉ stages, k_P := 2k1 + 14 ([[cor:own-p-order]]). Then there is λ_2 > 0
such that for every 0 < λ ≤ λ_2, with no exceptional set:

(1) g_λ continues to the past domain of dependence W of S := Σ^IVP ∩ {r ≥ 4R} for g_b0 as a smooth G-invariant vacuum
metric g in the wave-map gauge relative to g_b0, and all of W but a strip along its null boundary, of v-width tending to 0
with λ, lies in the domain of dependence of S for g. It is the only continuation in that gauge with |g − g_b0| ≤ 1/50,
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

    g_b0⁻¹(β̂, β̂) = (2f′ − 3)(2f′ + 1) − 𝔪(1 + 2f′)²,     g_b0⁻¹(α̂, α̂) = (2f′ − 1)(2f′ + 3) − 𝔪(3 + 2f′)²,   {#eq:own-cones}

both at most −7/4 for |f′| ≤ ¼ (with y := 2f′ ∈ [−½, ½], y² − 2y − 3 and y² + 2y − 3 are at most −7/4), and
β̂(∂_τ) = 2, α̂(∂_τ) = −2. So |dr(Y)| < 2 dt̃(Y) for future causal Y. L0 is future null with L0(v) = 0, L0(τ) = 1,
L0(r) = −1; along its rays t̃ = v − r − f(r) increases as r decreases, and d(r + f)/dr = 1 + f′ ≥ ¾.
*D⁻(S; g_b0) ⊂ W.* For p in D⁻(S), the future ingoing null ray from p (v = v(p), r decreasing) must meet S, at some r* ≥ 4R with τ = f(r*); so v(p) = r* + f(r*) ≥ 4R + f(4R) = v1, r(p) ≥ r* ≥ 4R, and
t̃(p) ≤ 0, as t̃ increases along the ray to 0 at r*. *W ⊂ D⁻(S; g_b0).* Let p ∈ W and γ a future-inextendible causal
curve from p; v ≥ v1 along it. If γ reaches {r = 4R}, at a first point q, then t̃(q) = τ(q) − τ_S = v(q) − v1 ≥ 0, so γ
meets {t̃ = 0} at or before q, at a point with r ≥ 4R and v ≥ v1, a point of S. Otherwise γ stays in {r ≥ 4R}; while
t̃ ≤ 0 it lies in the compact set {t̃(p) ≤ t̃ ≤ 0, 4R ≤ r ≤ r(p) + 2|t̃(p)|}, where dt̃ is uniformly timelike, so its
coordinate velocity parametrised by t̃ is bounded; if t̃ stayed below 0, γ would have an endpoint and be extendible. So γ
reaches t̃ = 0 at a point of S. The description of the boundary and r = v − τ ≥ v1 − τ follow from the definitions.

(ii) m_Ω = V′ + 1 + τ′_end − 2τ_S − 4R ≥ 2V′ + 1 − q_end − 2τ_top − 4R ≥ q_end + 3, by τ_S ≤ τ_top, τ′_end ≥ V′ − q_end
and V′ ≥ τ_top + 2R + q_end + 1; and v1 ≥ v_end + 2 since ∂S ⊂ Σ^IVP ∩ {r_0 ≤ r ≤ 4R}. Let v ≤ v1 + ½ and r ≥ 4R. Then
τ = v − r ≤ τ_S + ½ ≤ τ′_end − ½. If τ ≥ τ0: v + (τ − τ′_end) ≤ v1 + τ_S + 1 − τ′_end = V′ + 2 − m_Ω ≤ V′ − 1, and
r > a′, so the point lies in the interior of Ω′ ([[eq:omega]]). If τ ≤ τ0: v + h_P(τ) ≤ v1 + ½ + κ_P = V′_P − (τ_S − τ0)
− m_Ω + ½ ≤ V′_P − 3, as τ_S ≥ τ0 + 1, h_P ≤ κ_P and V′_P = V′ + 1 + (τ′_end − τ0) + κ_P; so it lies in P′. The last
inequality is the same computation.

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

Enlarging R, we also take sup_(r≥4R) |f − f(4R)| ≤ 1 (f′ = O(r⁻²)), so that v1 − τ_max ≥ 4R − 1 > 0. We write W_T := W ∩ {t̃ ≥ T} for T ≤ 0.

