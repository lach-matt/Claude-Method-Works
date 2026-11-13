## The development of g_λ's own data settles {#ch:own-data}

[[thm:settling]] (i) concerns data that agree with those of g_λ on a ball and are continued equivariantly to exact
Tangherlini data beyond it. This chapter proves that the maximal vacuum development of the data that g_λ itself induces
on Hintz's initial surface Σ^IVP settles to five-dimensional Tangherlini, with no gluing, for every λ below a threshold
and with no exceptional set. The data class of [[thm:settling]] (ii) does not contain these data: after the shell the
difference g_λ − g0 carries at past null infinity a coefficient of r^(−5/2), of size O(λ^∞) but, for every amplitude
but at most one, nonzero for all λ off a set whose only possible accumulation point is λ = 0, and it reaches the data
at spatial infinity as a term ρ^(5/2), ρ := 1/r. The class is therefore widened by the half-integer orders, and the
stability theory runs in the wider class with the same index sets.

The argument has five parts. (1) The far part S := Σ^IVP ∩ {r ≥ 4R} of the initial surface has a past domain of
dependence W for Tangherlini, bounded by S, by an ingoing null cone ℋ on which g_λ is known, and by past null infinity,
where nothing comes in after the shell (Section [[sec:own-far-part]]). (2) The tail at r^(−5/2) is computed
(Section [[sec:own-tail]]). (3) The stability theory holds in the half-integer class with the same index sets
(Section [[sec:own-half-class]]). (4) The constants of the construction from past null infinity are polynomial in
λ^(−1) at every order, which makes the data of g_λ on ℋ small at every weight that the estimate below uses
(Sections [[sec:own-orders]] and [[sec:own-sigma]]). (5) After its self-similar terms through r^(−4) are subtracted,
g_λ continues to W by one weighted energy estimate at a weight a ∈ (ℓ0 − 1, 3), run on bounded domains of dependence;
the continuation is vacuum, unique in a class of weight below ½, and its data on S lie in the half-integer class with
small norm (Sections [[sec:cutoff-expansion]], [[sec:own-continuation]] and [[sec:own-vacuum]]). The theorem is
assembled in Section [[sec:own-proof]].

*Notation.* We use the chart (τ, x) of [[sec:background]], v = τ + r, the background g0 of [[eq:background]] and the
gauge of [[sec:gauge]]. Ω′ is the domain of the form [[eq:omega]], with constants (T′, δ′0) and inner radius a′ = q0 −
δ′0, that [[lem:vii-1-2]] chooses for a radius R ≥ R_3, with V′ := v_end + T′ and τ′_end its constants, and P′ is its
past domain, [[eq:past-domain]] with these constants: P′ := {τ ≤ τ0, |x| ≥ a′, v + h_P(τ) ≤ V′_P}, V′_P := V′ + 1 +
(τ′_end − τ0) + κ_P, κ_P = ½. g_λ is the solution of [[thm:past-construction]] on P′ ∪ Ω′ ([[thm:past-construction]]
holds for every domain of the form [[eq:omega]] and its past domain). On {v ≥ v_end}, μ = μ_end, and we write μ := μ_end
in this chapter; there g0 = g_b0 := η + μ r⁻² dv ⊗ dv, five-dimensional Tangherlini in Kerr–Schild form, whose
Kerr–Schild time is τ ([[lem:vii-1-2]] (a)). In the far region we write t := τ, so that (t, x) are Kerr–Schild Cartesian
coordinates and v = t + r; this t is the Kerr–Schild time τ, not the time of the chart of [[lem:vii-1-2]], and the
variable t of [[ch:past-construction]] is written t_P := 1 + τ0 − τ. We put 𝔪 := μ r⁻². R is the radius of
[[lem:vii-1-2]], taken as in [[ch:interior]] (4R ≥ 20R₁) and, R ≥ R_3 being free, with 4R ≥ 1 as well; for r ≥ R_3 the
initial surface is a graph Σ^IVP = {τ = f(r)}, with f′ ∈ |x|⁻² C^∞ near infinity ([[lem:interior-where]] (ii), the
function F there). G = O(2) × O(2) acts by (t, x) ↦ (t, Ox) ([[sec:s27-class]]).

**Theorem {#thm:own-data}** (the development of g_λ's own data settles). Fix A, the envelope env ∈ C_c^∞, the angular
profile and the seed. Let ℓ0 ∈ (3, 4) ∖ {7/2}, ℓ_I ∈ (3, ℓ0) off the exclusion sets of row d2 of [[sec:vi-c-1]], ε_m > 0
and 0 < ε_t < ε_K, the parameters of the stability theory chosen as for [[thm:settling]]. Let ε and d_1 be those of
[[thm:iii-k-4-3]] in the class ℰ_0^½ ([[def:half-class]], [[thm:own-half-settling]]), below the threshold of
[[prop:vii-3-2]] and that of [[cor:s27-rate]] for ε_m and ε_t. Let a ∈ (ℓ0 − 1, 3), k1 := max(8, d_1 + 4),
M := 15 + 2(k1 + 1), K > max(d_1 + 14, K*(a, M, k1)) with K* of [[lem:own-e-flux]], and let the approximant of
[[thm:past-approximant]] have K + 4 + ⌈4β0(k_P)⌉ stages, k_P := 2k1 + 14 ([[cor:own-p-order]]). Then there is λ_2 > 0
such that for every 0 < λ ≤ λ_2, with no exceptional set:

(1) g_λ continues to the past domain of dependence W of S := Σ^IVP ∩ {r ≥ 4R} for g_b0 as a smooth G-invariant vacuum
metric g in the wave-map gauge relative to g_b0, and all of W but a strip along its null boundary, of v-width tending to
0 with λ, lies in the domain of dependence of S for g. It is the only continuation in that gauge with |g − g_b0| ≤ 1/50
whose energies of some weight a_0 ∈ (0, ½) of the fields Γ^α (g − g_b0), |α| ≤ 3, Γ ∈ {∂_t, L_Ω_ab, Z} (Section
[[sec:far-homogeneity]]), are bounded uniformly in the slices and whose energy tends to 0 toward past null infinity
([[prop:own-uniqueness]]);

(2) its data (γ, k) on Σ^IVP satisfy γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b, k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b, with
‖(γ − γ_b0, k − k_b0)‖_(d_1) < ε in the norm of [[sec:s27-class]] taken with ℰ_0 = ℰ_0^½;

(3) the maximal vacuum development ĝ of (γ, k) settles to a Tangherlini metric g_(m′,0) with |m′ − μ_end| < ε_m: on
{r_♭ ≤ r ≤ R′, t_* ≥ T′}, |(t_*∂_(t_*))^i ∂_x^β (ĝ − g_(m′,0))| ≤ C t_*^(−2−ε_t) for every R′, i and β, with C and T′
depending on them.

The threshold λ_2 is not evaluated, and ε, d_1, λ_2 depend on the class. The order k_P is what the subtracted
expansion of Section [[sec:own-sigma]] needs: a Cartesian derivative of order j of its terms costs 2j + 2 angular
derivatives of their data on ℋ ([[lem:own-self-similar]]), and the estimates use j ≤ k1 + 4. The proof is in Section
[[sec:own-proof]]; its first step checks every use of k_P.

### The far part of the initial surface and its past domain of dependence {#sec:own-far-part}

We use the far part of Σ^IVP and its past domain of dependence as they are set up before [[lem:interior-far-part]],
writing f for F, S for Σ_far, ℋ for H₁, Z_b for the set Z there (Z denotes a vector field below) and 𝔪 for m = μ r⁻².
So S = Σ^IVP ∩ {r ≥ 4R} = {τ = f(r), r ≥ 4R}, τ_S := f(4R), v1 := 4R + τ_S is the value of v on ∂S,
τ_max := sup_(r≥4R) f, and

    t̃ := τ − f(r),     W := {v ≥ v1, t̃ ≤ 0, r ≥ 4R},     ℋ := W ∩ {v = v1},
    Σ̃_σ := W ∩ {t̃ = σ} (σ ≤ 0),     s := (v − v1)/r,     W_T := W ∩ {t̃ ≥ T}.                         {#eq:own-wedge}

Σ̃_0 = S. On r ≥ 4R, 0 < f′ ≤ ¼ and 𝔪 ≤ 1/400, f is bounded, |f| ≤ C_f, and v1 − τ_max > 0. By
[[lem:interior-far-part]]: W = D⁻(S; g_b0), with boundary S, ℋ and past null infinity at v ≥ v1, and r ≥ v1 − τ on W
(i); ℋ and the strip {v1 ≤ v ≤ v1 + ½, r ≥ 4R} lie in Ω′ ∪ P′, and v1 ≤ V′_P − κ_P − 1 − m_Ω with m_Ω ≥ 3 (ii); for a
metric on W ∪ Z_b equal to g_λ on Z_b and within C_W ν (v1 − τ)⁻² of g0 on W, all of W but a strip along ℋ of v-width
O(λ + ν) lies in the domain of dependence of S ((iv) (b)); and for v ≥ v1 nothing comes in at past null infinity:
r^(3/2)(g_λ − g0) → 0 as r → ∞ at fixed v ∈ [v1, V′_P) and x̂ (v). Two further facts about W are used.

**Lemma {#lem:own-wedge}** (the geometry of W). (a) The conormals α̂ := d(r − 2t̃) and β̂ := d(r + 2t̃) satisfy

    g_b0⁻¹(β̂, β̂) = (2f′ − 3)(2f′ + 1) − 𝔪(1 + 2f′)²,
    g_b0⁻¹(α̂, α̂) = (2f′ − 1)(2f′ + 3) − 𝔪(3 + 2f′)²,                                              {#eq:own-cones}

both at most −7/4, with β̂(∂_τ) = 2 and α̂(∂_τ) = −2; |α̂|_E², |β̂|_E² ≤ 25/4 and g_b0⁻¹(dt̃, dt̃) ≤ −15/16.
(b) On W, s ∈ [0, 5/4] and |τ − v1| ≤ r. Each Σ̃_σ is {r ≥ r_σ} along the rays τ = f(r) + σ, r_σ being the solution of
r + f(r) = v1 − σ, and r_σ ≥ c_W (1 + |σ|) for some c_W > 0.

*Proof.* (a) These are the contractions of the proof of [[lem:interior-far-part]] (i) ((2f′ − 3)(2f′ + 1) =
−3 − 4f′ + 4f′², (2f′ − 1)(2f′ + 3) = −3 + 4f′ + 4f′²); and α̂ = (1 + 2f′) dr − 2 dτ, β̂ = (1 − 2f′) dr + 2 dτ give
the Euclidean norms |α̂|_E² = 4 + (1 + 2f′)² and |β̂|_E² = 4 + (1 − 2f′)². (b) On W, v − v1 = τ + r −
v1 ≥ 0 and τ ≤ f(r), so v − v1 ≤ f(r) − f(4R) + r − 4R ≤ (5/4)(r − 4R): hence 0 ≤ s ≤ 5/4. τ − v1 = (v − v1) − r ≥ −r,
and τ − v1 ≤ f(r) − f(4R) − 4R ≤ r. On Σ̃_σ, v = r + f(r) + σ increases in r (1 + f′ ≥ 1), so v ≥ v1 exactly for
r ≥ r_σ; and r_σ ≥ max(4R, |σ| + v1 − C_f) for σ ≤ 0, which is at least c_W (1 + |σ|) for some c_W > 0 depending on R,
v1 and C_f. ∎

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
from the flat operator. The latter: by [[eq:wave-operator-vr]], for ψ(v, x̂) smooth,

    □̃(r^(−p) ψ) = (3 − 2p) r^(−p−1) ∂_v ψ + r^(−p−2) (Δ̊ + p² − 2p) ψ − μ p(p + 1) r^(−p−4) ψ,
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
dividing by A_i, a_1 + A_i² a_3^sp = 0 for i = 1, 2 on that interval, a_3^sp the spatial part of a_3; subtracting,
a_3^sp = 0 and then a_1 = 0 there, hence for all ω > 0 by analyticity, and ê = 0 on (0, ∞), a contradiction. For any
other A > 0 some spatial component of G_5^∞ at some x̂ is a real-analytic function of ω that is not identically zero, and
its zeros are isolated. ∎

**Remark {#rem:own-no-tail-approximant}** (the approximant carries no tail). In the approximant from past null infinity
([[thm:past-approximant]]) a term of order k/2 in the expansion of a profile carries phase harmonics of the parity of k:
W_TT has order 3/2 and harmonic ±1, χ order 2 and harmonic ±2 ([[eq:past-classes]]), g0 integer orders and harmonic 0.
Products, ∂_v, ℓ, Ω, ∂_θ, the transports of [[lem:decay-calculus]] (d) (leading term −r^(1−q) f_q/(q − 5/2)), the mean
integrals 2/(2q − 5) ∫ S_q and the phase integrals from past null infinity each change k by an even number or not at
all, and keep the parity; a mean over θ is nonzero only on even harmonics. So the means m_j have only integer orders, and
after the shell, where g_app − g0 = Σ_j λ^j m_j ([[lem:np-10-50-a]] on Ω′, step (3) of the proof of [[prop:past-items]]
on P′), g_app − g0 has no term of half-integer order. The coefficient G_5^∞ is therefore carried by g_λ − g_app, in
agreement with (c): its two-scale expansion vanishes at every order in λ.

**Remark {#rem:own-tail-bump}** (Numerical observation.) For the bump envelope env_b(v) = exp(−1/(1 − y²)),
y = (v − 2)/(3/2), on [½, 7/2], e^(−2iω) ê_b(ω) is real, env_b being even about v = 2, so a_1 vanishes exactly at the
real zeros of that function. Evaluated numerically, ê_b(1/λ) ≠ 0 at λ = 2⁻¹, …, 2⁻⁷ (|ê_b| from 0.297 down to
3.4 × 10⁻⁸, falling faster than λ⁵ over [2⁻⁷, 2⁻⁵]), and its first zeros are at ω ≈ 3.331, 5.926, 8.399, 10.81: as far
as it was evaluated, the zero set of a_1 for this envelope continues without end and accumulates only at λ = 0. It does
not by itself determine the exceptional set of [[prop:own-tail]] (d), which also involves a_3. For the envelope
sin⁴(π(v − ½)/3), which is C³ but not C^∞ at its ends, |ê(ω)| ω⁵ stays between 17 and 61 for ω = 10, …, 320, so a_1 is of
order λ⁶ there rather than O(λ^∞). No proof uses these values.

### The stability theory in the half-integer class {#sec:own-half-class}

ℰ_0^½ is the index set of the half-integer class ([[def:half-class]], [[eq:half-class]]), and ℰ_0^ℤ := {(j, 0) : j ∈ ℕ,
j ≥ 2} that of [[eq:vii-0-1]]. By [[lem:half-class]] (a), ℰ_0^½ satisfies row d1 of [[sec:vi-c-1]] for every
ℓ0 ∈ (3, 4) ∖ {7/2}. This section shows that the stability theory runs in that class with the index sets of
[[eq:vii-0-1]], logarithmic orders included, which settles the question left open in [[rem:half-class-changes]].

**Definition {#def:own-iterates}** (the iterates). For an index set E_0 with min Re E_0 > 3/2 + 2γ_Υ, ⟨E_0⟩ denotes the
smallest index set containing E_0 and satisfying (2)–(3) of [[def:iii-c-3-1]] ([[lem:iii-c-3-2]] (e)), and the proof of
[[thm:iii-c1-3-1]] builds the sets

    ℰ^((0))(E_0) := ⟨E_0⟩,     ℰ^((m+1))(E_0) := ⟨E_0 ∪̄ ℰ^((m))(E_0)⟩,                              {#eq:own-iterates}

taking ℰ_I^C := ℰ^((J))(E_0), J the number of its repetitions. We write k(F, z) for the largest log order of an index set
F at z ([[def:s11-b-analysis]] (4)), and 𝒵_Υ := {(3/2 + s, 0) : s ∈ σ_Υ} for the set of points that [[eq:iii-c-3-1]]
adjoins to ℰ_I^C (each with its translates by ℕ_0).

**Lemma {#lem:own-words}** (the smallest set by words). Let A be an index set with min Re A > 3/2 + 2γ_Υ. Then ⟨A⟩ is
the set of pairs (z, k) with

    z = z_1 + ⋯ + z_r − (r − 1) + j,     0 ≤ k ≤ k_1 + ⋯ + k_r,                                          {#eq:own-word}

r ≥ 1, j ∈ ℕ_0, each (z_i, k_i) in A ∪ 𝒵_Υ, and (z_1, k_1) ∈ A when r = 1.

*Proof.* Let 𝔚(A) be the set described. *𝔚(A) ⊂ ⟨A⟩*, by induction on r. For r = 1 this is A ⊂ ⟨A⟩ and the index set
property. For r ≥ 2 the word with the first r − 1 factors lies in ⟨A⟩ ∪ 𝒵_Υ ⊂ ⟨A⟩^tot (in 𝒵_Υ only when r − 1 = 1 and
its factor lies there), so adding z_r − 1 gives an element of ⟨A⟩^tot + (⟨A⟩^tot − 1) ⊂ ⟨A⟩, by (3) of
[[def:iii-c-3-1]], with log order the sum; translations by ℕ_0 and lower log orders stay in ⟨A⟩. *⟨A⟩ ⊂ 𝔚(A).* 𝔚(A) is
closed under + ℕ_0 and under lowering the log order. Every z_i has real part at least 3/2, so a word with r ≥ 2 factors
has real part at least r/2 + 1; below any C there are therefore finitely many r, finitely many factors and finitely many
j, and 𝔚(A) is an index set. It contains A, its minimum real part is at least min(min Re A, 2) > 3/2 + 2γ_Υ, and the
sum of two elements of 𝔚(A) ∪ 𝒵_Υ minus 1 is a word with r_1 + r_2 ≥ 2 factors: 𝔚(A) satisfies (2)–(3) of
[[def:iii-c-3-1]]. ∎

**Proposition {#prop:own-same-index-sets}** (the same index sets). For every m ≥ 0,
ℰ^((m))(ℰ_0^½) = ℰ^((m))(ℰ_0^ℤ), and in this set k(n + ½) = k(n) for every integer n ≥ 2. Consequently, if the weights
in the proof of [[thm:iii-c1-3-1]] are chosen the same for ℰ_0^½ and ℰ_0^ℤ (each is chosen off a discrete set, and the
union of the two classes' sets is discrete), then ℰ_I^C is the same for the two classes, and so are Λ, the exclusion sets
of row d2, the conditions (G) and (G⁺), and the admissible ε_+, ε_K and α of rows w1–w2.

*Proof.* Write E := ℰ_0^ℤ, E′ := ℰ_0^½, F_m := ℰ^((m))(E), and 𝔚_½(A) for the set of words [[eq:own-word]] whose
factors lie in A ∪ {(3/2, 0)}. Put F^½_0 := 𝔚_½(E) and F^½_(m+1) := 𝔚_½(E ∪̄ F^½_m). By [[lem:own-words]] and the
monotonicity of ∪̄ and of words in their arguments, F^½_m ⊂ F_m. Every element of F^½_m has its first component in
½ℤ, and F^½_m is closed under (z, k) ↦ (z + ½, k): adjoining the factor (3/2, 0) to a word adds ½ to its value.

*Step 1 (lattice points have lattice words).* We show by induction on m: for every (z, k) ∈ F_m there are (z′, k) ∈ F^½_m
and c ∈ ℕ_0 δ_♯ + ℕ_0 γ_Υ, δ_♯ = (1 − e_Υ)γ_Υ, with z = z′ + c; and every (z, k) ∈ F_m with z ∈ ½ℤ lies in F^½_m. The
second statement follows from the first: c = z − z′ lies in ½ℤ and c ≥ 0, so c = q/2 with q ∈ ℕ_0, and (z, k) =
(z′ + q/2, k) ∈ F^½_m. For the first, each element of 𝒵_Υ is (3/2, 0) plus s ∈ σ_Υ ⊂ ℕ_0 δ_♯ + ℕ_0 γ_Υ. For m = 0 replace
every factor (3/2 + s, 0) of a word over E ∪ 𝒵_Υ by (3/2, 0). For m ≥ 1 the factors of a word for F_m lie in
𝒵_Υ or in A_m := E ∪̄ F_(m−1), whose elements are elements of E, elements of F_(m−1), or pairs (p, l + 1) with p ∈ π_1E
an integer and (p, l) ∈ F_(m−1) (with their translates and lower log orders). An element of F_(m−1) has a shadow in
F^½_(m−1) by induction; for a pair (p, l + 1), (p, l) ∈ F^½_(m−1) by the second statement at m − 1, so (p, l + 1) ∈ E ∪̄
F^½_(m−1). Replacing every factor by its shadow gives a word of 𝔚_½(E ∪̄ F^½_(m−1)) = F^½_m with the same log order and a
value smaller by a sum of elements of ℕ_0 δ_♯ + ℕ_0 γ_Υ.

*Step 2 (k(n + ½) ≤ k(n) in F_m).* For m = 0 every factor of a word in 𝔚_½(E) has log order 0, so by Step 1 every point
of F_0 in ½ℤ has log order 0, and n ∈ π_1 F_0 for n ≥ 2. Let m ≥ 1, assume the claim for F_(m−1), and let (n + ½, k) ∈
F_m, n ≥ 2 an integer. By Step 1 it is a word [[eq:own-word]] with factors in (E ∪̄ F^½_(m−1)) ∪ {(3/2, 0)}. If r ≥ 2 and
some factor is (3/2, 0), remove it: the value drops by ½, the log order is unchanged, and if one factor remains it lies
in E ∪̄ F^½_(m−1) (two factors (3/2, 0) give an integer value). Otherwise every factor lies in E ∪̄ F^½_(m−1) ⊂ ½ℤ × ℕ_0,
and as the value lies in ½ + ℤ, some factor (h, k_h) has h ∈ ½ + ℤ, h ≥ 5/2. E has no exponent at h, so k_h ≤ k(F_(m−1),
h) ≤ k(F_(m−1), h − ½), while E ∪̄ F^½_(m−1) has at the integer h − ½ ≥ 2 the log order k(F_(m−1), h − ½) + 1 (Step 1 at
m − 1 identifies the log orders of F^½_(m−1) and F_(m−1) on ½ℤ). Replace (h, k_h) by (h − ½, k_h). In both cases (n, k)
is a word of F^½_m ⊂ F_m.

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
by [[lem:half-class]] (a). By [[prop:own-same-index-sets]], ℰ_I^C and Λ are those of [[eq:vii-0-1]], so rows d2,
w1, w2 and b4 hold with the same choices, and step (6) chooses ε and d_1 for ℰ_0^½. ∎

**Remark {#rem:own-half-changes}** (what the class changes). (a) H^(∞,(ℰ_0^ℤ,ℓ0))_b lies continuously in
H^(∞,(ℰ_0^½,ℓ0))_b (the new coefficients are 0), so the bound of [[lem:vii-0-1]] holds in the larger class. (b) Step 1 of
the proof of [[thm:iii-c1-3-1]] applies R = Π_((z,k)∈ℰ_(0,≤))(X_0 − z), with one factor for each exponent of ℰ_0 up to
the weight reached: at the last step R has 3 factors for ℓ0 ∈ (3, 7/2) and 4 for ℓ0 ∈ (7/2, 4), against 2 for ℰ_0^ℤ,
and each factor costs one derivative (the converse part of [[lem:iii-a-1-3]]). So d_1 changes by a finite amount, and ε
with it; the thresholds λ1 and δ of [[thm:settling]] change accordingly. None of ε, d_1, λ1, δ is evaluated, in either
class. (c) The weights α_1, α′ avoid finitely many more points in each bounded interval.

### The construction from past null infinity at every order {#sec:own-orders}

The data of g_λ on ℋ are controlled by [[thm:past-construction]] at a fixed order of derivatives. This section takes that
order to be arbitrary, with constants polynomial in λ⁻¹ and independent of the order K of the approximant.

**Proposition {#prop:own-far-order}** ([[prop:far-region]] at every order). Let q ≥ 6 and let the approximant have an
order K′ > 5, so that |Ric^H(g_app)|_(q,P) ≤ C_R(q) λ^(K′) t_P^(−3/2). There are λ_F(q) > 0 and M_F(q), independent of
τ_n, such that the conclusions of [[prop:far-region]] hold with [[eq:far-energy]] at order q.

*Proof.* The proof of [[prop:far-region]] uses q at five places. (a) The bootstrap assumption gives through
[[lem:past-sobolev]] the bounds of w_n and ∂w_n, hence the margin of [[lem:past-domain]] (f) and w_n = 0 on
{v ≤ v_start} ([[lem:seed-region]]); this needs q ≥ 3 only. (b) In the commuted equation, λ^i ∂^i Ω^β of the 1/λ term is
at most C_q λ⁻¹ t_P^(−3/2) E by Leibniz's rule, every factor λ^(i₂) ∂^(i₂) Ω^(β₂) G2 being bounded by C_q t_P^(−3/2), G2
a profile in E_(3/2), and the factors of s by C E ([[lem:past-sobolev]] (b) for the undifferentiated one); B·∂w and C·w,
and the commutators, give C_q t_P^(−3/2) E. (c) A nonlinear monomial at order j ≤ q has total w-order at most j + 2 and
no factor of order j + 2; put its factor of highest order in L² and the others in the supremum norm through
[[lem:past-sobolev]] (a), which costs three orders. The second-largest order is at most ⌊(q + 2)/2⌋, and
⌊(q + 2)/2⌋ + 3 ≤ q + 1 for q ≥ 5; so these terms are at most C_q λ⁻⁵ t_P^(−3/2) E². (d) The residual gives
C_R(q) λ^(K′) t_P^(−3/2). (e) Over t_P ≥ λ⁻² the kernels C_q t_P^(−3/2) and C_q λ⁻¹ t_P^(−3/2) integrate to at most 2C_q
λ and 2C_q, the data at τ_n are fixed by the residual as in the proof of [[prop:far-region]], and Gronwall's inequality
gives E(τ) ≤ C_q e^(2C_q(1+λ)) (3C_R(q) λ^(K′) + C_q M_F² λ^(2K′−5)) t_P^(−1/2) ≤ M_F λ^(K′) t_P^(−1/2) with
M_F = M_F(q) := 4C_q e^(6C_q) C_R(q) + 1, for λ ≤ λ_F(q), since 2K′ − 5 > K′. Existence and continuation are Step 8 of
the proof of [[thm:uniform-existence]] at the regularity q. ∎

**Proposition {#prop:own-near-order}** ([[prop:near-region]] at every order). For q ≥ 6 let C(q) be the sum of the
constants of [[eq:near-lines]] at the orders j ≤ q, β0(q) := max(2, 4C(q) + 1), and let the approximant have
N_q := K + 4 + ⌈4β0(q)⌉ stages, K ≥ 6, so that K′ = N_q − 1. There are λ_N(q) > 0 and M_N(q) such that
[[eq:near-bootstrap]] holds at order q with β0(q), and 𝒩_P(τ0) ≤ M_N(q) λ^(K′−2β0(q)).

*Proof.* The proof of [[prop:near-region]] at order q: its data come from [[prop:own-far-order]]; every line of
[[eq:near-lines]] holds at every order j ≤ q with c0 unchanged, the commutation fields commuting with L0 and
[Z, r^(−c)] carrying r^(−c−1); each integral of a bootstrap quantity returns at most C(q)/(β0(q) − 1) ≤ ¼ of its bound;
and the nonlinear ratios are at most C″ λ^(K′−8−4β0(q)), which is at most 1/8 for λ small because
K′ = K + 3 + ⌈4β0(q)⌉ ≥ 9 + 4β0(q). ∎

**Corollary {#cor:own-p-order}** ([[thm:past-construction]] at every order). Let q ≥ 6 and K ≥ 6, and let g_app be the
approximant with N_q stages. There is λ_P(K, q) > 0 such that for λ ≤ λ_P(K, q) the solution g_λ of
[[thm:past-construction]] satisfies [[eq:far-energy]] at order q on the far region, on Ω′ the conclusions of
[[thm:uniform-existence]] at the regularity q, 𝒩_q ≤ M_q λ^K on [τ0, τ′_end] with 𝒩_q the quantity [[eq:ue-energy]] at
order q ([[rem:ue-every-order]]), and on P

    |∂^i Ω^β (g_λ − g_app)| ≤ C_q λ^(K−3−i) t_P⁻²,     i + |β| ≤ q − 3.                                   {#eq:own-p-iii}

*Proof.* The proof of [[thm:past-construction]] at order q: the data of w_n at τ0 by [[prop:own-near-order]];
[[thm:uniform-existence]] at the regularity q ([[rem:ue-every-order]]); and the limit n → ∞, the bounds at order q being
inherited by weak lower semicontinuity. The solution built at order q is g_λ: the two approximants differ by Σ_(j>N_6)
λ^j [g_j] = O(λ^(N_6)) t_P^(−3/2) in C¹, so the solution at order q lies in the uniqueness class of item 5 of
[[thm:past-construction]] for the order 6. The energies E and 𝒩_P contain the rotations, which cost no power of λ, and
[[lem:past-sobolev]] (a) costs three derivatives in ∂_r and Ω; on the near region (T_λ/t)^(β0(q)) ≤ λ^(−2β0(q)) is
absorbed by K′ − 2β0(q) ≥ K + 3. This gives [[eq:own-p-iii]]. ∎

So no order fails; what grows with q is the number of stages N_q, and λ_P(K, q) may decrease.

**Proposition {#prop:own-poly}** (the powers of λ at past null infinity). For J ≥ 4 and n, m ≥ 0 there are C and
λ_0 > 0, depending on J, n, m and the data (seed, A, env, angular profile) and not on K, such that for 0 < λ ≤ λ_0, on
{t_P ≥ λ⁻² + d1} and for |α| + |β| ≤ n, in the expansion of [[prop:bondi-hierarchy]],

    |∂_X^α Ω^β ℓ^m u_J| ≤ C λ^(−(3J−9+|α|+m)) r^(−(J+1)/2−m),
    |∂_X^α Ω^β G_k| ≤ C λ^(−(k−4+|α|))  (k ≥ 3).                                                    {#eq:own-poly}

*Proof.* Say that a quantity has λ-order p if it is bounded by C λ^(−p), and write B_J for the λ-order of u_J in
[[eq:own-poly]] at α = 0, m = 0. *The base.* By [[cor:own-p-order]] at K = 6 and order n + 4, which gives the same g_λ
for λ ≤ λ_P(6, n + 4), |∂^α Ω^β (g_λ − g_app)| ≤ C λ^(3−|α|) t_P⁻²; and g_app − g0 − r^(−3/2) G_3 is the sum of λ m_1, of
λ[χ dv dv], of the phase-shift terms and of λ^j [g_j], j ≥ 2, each of λ-order at most |α| − 1 under ∂^α Ω^β (a derivative
of an oscillating factor costs λ⁻¹, a rotation nothing, Ω v = 0) and of class E_2 ([[eq:past-classes]]).
So |∂^α Ω^β u_1| ≤ C λ^(1−|α|) t_P⁻²: B_3 = −1, every derivative ∂_X costing one order and Ω none. Likewise
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
After the shell every oscillating profile vanishes ([[lem:np-10-50-a]], and step (3) of the proof of [[prop:past-items]]
on P′) and μ = μ_end. The forcing terms of the stage equations are then products of earlier means and terms in μ: two
factors r⁻² with two derivatives, a ∂_v of a leading coefficient vanishing by the induction (∂_v M_(i,4) = ∂_v M_(i,5) =
0 there, by [[eq:own-flat-recursion]] with M_(i,2) = M_(i,3) = 0), or −(μ/r²) ℓℓ, Γ[g0]·∂ and ∂∂g0, which add r⁻² to r⁻⁴
to a factor r⁻²; every one is O(r⁻⁶). So they enter only from q = 6, and through k = 9 the coefficients obey the flat
recursion of [[lem:bondi-half-order]], which reads [[eq:own-flat-recursion]] by [[eq:own-box-p]] at μ = 0 and raises the
degree in v by one every second order; from q = 6 on, products of polynomials and the constant μ keep the coefficients
polynomial in v. ∎

On {v > v_end}, g_app − g0 = Σ_j λ^j m_j ([[lem:np-10-50-a]] on Ω′, step (3) of the proof of [[prop:past-items]] on P′),
so for the remainder e := g_λ − g_app there the expansions of [[prop:bondi-hierarchy]] and [[lem:own-means]] give

    e = Σ_(k=4)^8 r^(−k/2) e_k + e_(8),     e_k := G_k − Σ_j λ^j M_(j,k),     e_(8) := u_8 − Σ_j λ^j m_(j,8),
                                                                                                    {#eq:own-e-expansion}

and by [[eq:own-poly]] and [[lem:own-means]], |∂_X^α Ω^β ℓ^m e_(8)| ≤ C λ^(−(15+|α|+m)) r^(−9/2−m) on {t_P ≥ λ⁻² + d1}.

**Lemma {#lem:own-interpolation}** (interpolation). Let d ≥ 0, P(y) = Σ_(i=0)^d c_i y^i, y_* > 0, and |P| ≤ η on
[y_*/2, y_*]. Then |c_i| ≤ L_d y_*^(−i) η, where L_d is the largest row sum of the absolute values of the inverse of the
Vandermonde matrix of the d + 1 nodes y_l := ½ + l/(2d), l = 0, …, d (L_0 := 1).

*Proof.* Q(y) := P(y_* y) = Σ_i c_i y_*^i y^i satisfies |Q(y_l)| ≤ η, and its coefficients are the inverse Vandermonde
matrix applied to (Q(y_l))_l. ∎

**Lemma {#lem:own-e-flux}** (the coefficients and the remainder of e on ℋ). Let a ∈ (0, 7/2), j ≥ 0, M ≥ 15 + 2(j + 1),
θ_k := (k − 4)/5, s_R := max(5/2, (2M + 1)/(7 − 2a)), and

    K*(a, M, j) := max{ 4 + j + s_R (a + j);  3 + i + (s_R max(0, 2a + 2 − k)/2 + (M + i) θ_k)/(1 − θ_k) :
                        4 ≤ k ≤ 8, 0 ≤ i ≤ j + 1 }.                                                    {#eq:own-kstar}

Let K > K*(a, M, j), let k_P ≥ j + 5, and let g_λ satisfy [[eq:own-p-iii]] at order k_P and [[eq:own-poly]] at n = k_P −
4.
(1) For 4 ≤ k ≤ 8, i ≤ j + 1 and i + |β| ≤ k_P − 4, |∂_v^i Ω^β e_k(v1, x̂)| ≤ C λ^((K−3−i)(1−θ_k)−(M+i)θ_k), and the
exponent exceeds 1 for i ≤ j.
(2) Let Γ ∈ {∂_t, Ω_ab, Z}, Z := (t − v1)∂_t + x·∂_x, and for φ on a neighbourhood of ℋ put

    𝔉_ℋ^a[φ] := ∫_ℋ r^(2a) ( |ℓφ|² + r⁻² |∇̊φ|² + r⁻² |∂φ|² ) r³ dr dω,                              {#eq:own-flux-n}

∇̊ the gradient on S³. Then 𝔉_ℋ^a[Γ^α e_(8)] → 0 as λ → 0 for every |α| ≤ j.

*Proof.* (1) On ℋ at fixed x̂, put y := r^(−1/2), so that r² r^(−k/2) = y^(k−4). By [[eq:own-e-expansion]],
r² ∂_v^i Ω^β e = P(y) + r² ∂_v^i Ω^β e_(8) with P(y) := Σ_(k=4)^8 ∂_v^i Ω^β e_k(v1, x̂) y^(k−4), of degree 4. On the far
region of ℋ, r and t_P are comparable, and |r² ∂_v^i Ω^β e| ≤ C λ^(K−3−i) by [[eq:own-p-iii]] (∂_v = ∂_t at fixed x is a
Cartesian derivative), while |r² ∂_v^i Ω^β e_(8)| ≤ C λ^(−(15+i)) y⁵ ≤ C λ^(−(M+i)) y⁵. So |P| ≤ η := C(λ^(K−3−i) +
λ^(−(M+i)) y_*⁵) on [y_*/2, y_*]. Take y_*⁵ := λ^(K−3+M); then η ≤ 2C λ^(K−3−i), and [[lem:own-interpolation]]
gives |∂_v^i Ω^β e_k| ≤ C λ^(K−3−i) y_*^(−(k−4)) = C λ^((K−3−i)(1−θ_k)−(M+i)θ_k). The interval y ∈ [y_*/2, y_*] is
r ∈ [y_*⁻², 4y_*⁻²], in the far region for λ small since K − 3 + M > 5. For i ≤ j, the condition of [[eq:own-kstar]]
at i + 1 ≤ j + 1 gives (K − 4 − i)(1 − θ_k) > (M + i + 1) θ_k, that is
(K − 3 − i)(1 − θ_k) − (M + i)θ_k > (1 − θ_k) + θ_k = 1.

(2) Let R_λ := λ^(−s_R), which lies in the far region for λ small as s_R ≥ 5/2. *Above R_λ*, by the bounds of e_(8)
after [[eq:own-e-expansion]] with the ℓ-gain, and Z = rℓ on ℋ (Z(v − v1) = v − v1 and Z = (v − v1)∂_v + rℓ in
(v, r, x̂)), the integrand of [[eq:own-flux-n]] for Γ^α e_(8), |α| ≤ j, is at most C λ^(−2M) r^(2a−11+3), and its
integral over r ≥ R_λ is C λ^(−2M) R_λ^(2a−7) = C λ^(−2M + s_R(7−2a)) ≤ C λ, by the choice of s_R. *Below R_λ*, write
Γ^α e_(8) = Γ^α e − Σ_(k=4)^8 Γ^α(r^(−k/2) e_k). For Γ^α e: Z = rℓ costs a factor r and a derivative, ∂_t a derivative,
Ω nothing; on ℋ ∩ Ω′ the bounds of [[thm:uniform-existence]] at order k_P hold with λ^(K−3−i) ([[cor:own-p-order]]), and
on ℋ ∩ P′ [[eq:own-p-iii]] holds; so every derivative in [[eq:own-flux-n]] of Γ^α e is at most C r^j λ^(K−4−j) r⁻², and
its integral over r ≤ R_λ is at most C λ^(2(K−4−j)) R_λ^(2a+2j) = C λ^(2(K−4−j−s_R(a+j))) → 0 by the first entry of
[[eq:own-kstar]]. For Γ^α(r^(−k/2) e_k(v, x̂)) on ℋ: ∂_t acts as ∂_v on e_k, Ω on x̂, and Z = rℓ multiplies r^(−k/2) by
−k/2; the tangential derivatives in [[eq:own-flux-n]] gain r⁻¹ and the transverse one costs one more ∂_v. So the
integrand is at most C r^(2a+1−k) times |∂_v^i Ω^β e_k(v1)|² with i ≤ j + 1, and the integral over r ≤ R_λ is at most
C R_λ^(max(0, 2a+2−k)) (1 + log R_λ) λ^(2((K−3−i)(1−θ_k) −(M+i)θ_k)), which tends to 0 by the second entries of
[[eq:own-kstar]]. ∎

### The subtracted expansion and the data on ℋ {#sec:own-sigma}

**Lemma {#lem:own-self-similar}** (self-similar solutions of the flat equation). Let p ∈ {2, 5/2, 3, 7/2, 4} and let G be
a smooth symmetric tensor field on S³ (Cartesian components). There is exactly one F(s, x̂), smooth on [0, 3/2] × S³ up
to s = 0, with F(0, ·) = G, such that r^(−p) F((v − v1)/r, x̂) solves □_η = 0 on {0 ≤ s ≤ 3/2}. Harmonic by harmonic,

    F = Σ_l G_l ₂F₁(p + l, p − l − 2; p − ½; s/2),                                                   {#eq:own-2f1}

G_l the part of degree l of each Cartesian component of G, and for every i and β,
sup_(0≤s≤3/2) |∂_s^i Ω^β F| ≤ C_(i,β) ‖G‖_(C^(2i+|β|+2)(S³)), with C_(i,β) depending on p, i and β only.

*Proof.* In the coordinates (v, r, x̂), with s = (v − v1)/r, ∂_v s = r⁻¹ and ℓs = −s/r, [[eq:wave-operator-vr]] at μ = 0
gives, for G_l of degree l (Δ̊ G_l = −l(l + 2) G_l),

    □_η (r^(−p) F(s) G_l) = −2 r^(−p−2) G_l [ (s − s²/2) F″ + (p − ½)(1 − s) F′ − ½(p² − 2p − l(l + 2)) F ].

With y := s/2 the bracket vanishes exactly when y(1 − y) F_yy + (p − ½)(1 − 2y) F_y − (p² − 2p − l(l + 2)) F = 0, the
hypergeometric equation [DLMF, (15.10.1)] with a = p + l, b = p − l − 2, c = p − ½ (a + b + 1 = 2p − 1,
ab = p² − 2p − l(l + 2)); in this proof (a, b, c) are the parameters of [DLMF], not the weight a. Its exponents at
y = 0 are 0 and 1 − c = 3/2 − p < 0; c is not a nonpositive integer, so the solutions bounded at y = 0 are the
multiples of ₂F₁(a, b; c; y), analytic for |y| < 1. This gives existence and uniqueness harmonic by harmonic, and
[[eq:own-2f1]] once the sum converges.

*Bounds uniform in l.* Let φ := ₂F₁(a, b; c; y) on [0, ¾], c ≥ 3/2, and suppose κ² := −ab = (l + 1)² − (p − 1)² > 0. Then
y(1 − y) φ″ + c(1 − 2y) φ′ + κ² φ = 0, and 𝓔 := y(1 − y) φ′² + κ² φ² satisfies 𝓔′ = (1 − 2y)(1 − 2c) φ′². On [0, ½],
𝓔′ ≤ 0; on [½, ¾], 𝓔′ ≤ (2c − 1)(2y − 1) 𝓔/(y(1 − y)) ≤ (16/3)(2c − 1)(2y − 1) 𝓔, whose integral over [½, ¾] is (2c −
1)/3. So 𝓔 ≤ e^((2c−1)/3) 𝓔(0) = e^((2c−1)/3) κ², and |φ| ≤ e^((2c−1)/6) on [0, ¾]. By [DLMF, (15.5.1)],
∂_y ₂F₁(a, b; c; y) = (ab/c) ₂F₁(a + 1, b + 1; c + 1; y), and (a + 1, b + 1, c + 1) is the triple of p + 1 in place of p;
so ∂_y^i φ is a product of i factors (a + n)(b + n)/(c + n), each at most (l + p + n)², with the function of p + i, which
the energy bound controls for (l + 1)² > (p + i − 1)². For the finitely many other l, ₂F₁ is a fixed smooth function on
[0, ¾]. Hence |∂_y^i ₂F₁| ≤ C_i (1 + l)^(2i) on [0, ¾]. The rotations Ω_ab preserve the harmonics of degree l, with
‖Ω_ab Y‖_(L²) ≤ (l(l + 2))^(1/2) ‖Y‖_(L²) (as Σ_(a<b) Ω_ab² = Δ̊), and a harmonic of degree l has
‖Y‖_∞ ≤ C(1 + l)‖Y‖_(L²), the space having dimension (l + 1)². So
∂_s^i Ω^β F is at most C Σ_l (1 + l)^(2i+|β|+1) ‖G_l‖_(L²) ≤ C ‖G‖_(H^(2i+|β|+2)) ≤ C ‖G‖_(C^(2i+|β|+2)) in
modulus, by the Cauchy–Schwarz inequality with Σ_l (1 + l)⁻² < ∞. The series converges with all derivatives, and F
is smooth on [0, 3/2] × S³. ∎

**Definition {#def:own-sigma}** (the subtracted expansion). Let Π := {2, 5/2, 3, 7/2, 4}. For p ∈ Π let F_p be the
solution of [[lem:own-self-similar]] with F_p(0, ·) = G_(2p)(v1, ·), the coefficient of r^(−p) of g_λ − g0 at v = v1
([[prop:bondi-hierarchy]]), and put

    Σ_p := r^(−p) F_p(s, x̂),     Σ := Σ_(p∈Π) Σ_p,     h_R := g − g_b0 − Σ,                              {#eq:own-sigma}

for a metric g on W. All five Σ_p solve □_η Σ_p = 0, Σ_4 included; for this Σ, [[prop:far-residual]] gives the
bound |Π_i (Γ_i + c_i) P(Σ)| ≤ C λ r⁻⁶ and [[cor:far-kernels]] the kernel κ_Σ(σ) = C λ (1 + |σ|)^(a−4), and
[[rem:far-window-sigma4]] compares other choices of Σ_4.

**Lemma {#lem:own-sigma-data}** (the size of Σ). Under the hypotheses of [[thm:own-data]], for λ small:
(a) ‖G_(2p)(v1)‖_(C^(2k1+10)(S³)) ≤ C λ for p ∈ Π, and ‖G_5(v1)‖_(C^m(S³)) = O(λ^n) for all m, n;
(b) Σ_p = λ Σ̂_p, where every Cartesian derivative of order at most k1 + 4 of Σ̂_p is bounded on
{r = 1, 0 ≤ s ≤ 3/2} independently of λ, and at fixed λ every derivative of Σ̂_p is bounded there; hence on
W ∩ {r ≥ 1}, |∂^j Σ_p| ≤ C_j λ r^(−p−j) and |Γ^α Σ_p| ≤ C_α λ r^(−p) for j, |α| ≤ k1 + 4;
(c) Σ is G-invariant.

*Proof.* (a) By [[eq:own-e-expansion]], G_(2p)(v1) = Σ_j λ^j M_(j,2p)(v1) + e_(2p)(v1). The first sum consists of smooth
fields independent of λ times λ^j, j ≥ 1. For the second, [[lem:own-e-flux]] (1) with i = 0 and |β| ≤ 2k1 + 10 =
k_P − 4 gives |Ω^β e_(2p)(v1)| ≤ C λ^(1+). G_5(v1) = G_5^∞ ([[prop:own-tail]] (a), v1 ≥ v_end + 2), and the proof of
[[prop:own-tail]] (c) holds with every x̂-derivative, a_1 and a_3 depending smoothly on x̂ through smooth factors.
(b) On {r = 1, 0 ≤ s ≤ 3/2} a Cartesian derivative of order j of r^(−p) F_p(s, x̂) is a combination, with bounded
coefficients, of ∂_s^i Ω^β F_p with i + |β| ≤ j; by [[lem:own-self-similar]] these are at most C ‖G_(2p)(v1)‖_(C^(2j+2)),
which is O(λ) for j ≤ k1 + 4 by (a); at fixed λ, G_(2p)(v1) is smooth ([[prop:bondi-hierarchy]]), so every such
derivative is bounded. The bounds on W ∩ {r ≥ 1} follow by the homogeneity of Σ_p of degree −p under the dilation of
Section [[sec:far-homogeneity]], which maps {r = 1, 0 ≤ s ≤ 3/2} onto {r = ς, 0 ≤ s ≤ 3/2}, together with
[[lem:own-wedge]] (b). (c) g_λ is invariant under T² and the two reflections (item 5 of [[thm:past-construction]]),
which generate G, so it is G-invariant; so are the coefficients of its expansion, and the equation of
[[lem:own-self-similar]] commutes with G. ∎

**Lemma {#lem:own-n-data}** (the remainder on ℋ and on the band). Let 𝒰 := (P′ ∪ Ω′) ∩ {v1 ≤ v ≤ V′_P − h_P(τ)} ∩ W,
on which g_λ is defined, and put h_R := g_λ − g_b0 − Σ there.
(i) At fixed λ, every Γ^α h_R is O(r^(−9/2)) on 𝒰, with constants depending on λ and α; on ℋ, Γ^α h_R and its
derivatives along the spheres are O(r^(−9/2)) and its derivative along ℓ is O(r^(−11/2)).
(ii) Let a ∈ (0, 7/2). Near ℋ, h_R = e_(8) + Σ_j λ^j m_(j,8) − Σ_rem, where Σ_rem is Σ minus the terms of order at most
4 of its expansion at fixed v; for |α| ≤ k1, Γ^α Σ_rem and its first derivatives are O(λ r^(−9/2)) there, its derivatives
along ℓ and along the spheres O(λ r^(−11/2)). If K > K*(a, M, k1) as in [[thm:own-data]], then
𝔉_ℋ^a[Γ^α h_R] ≤ C(λ² + ν(λ)) for |α| ≤ k1, with ν(λ) → 0 as λ → 0.
(iii) The flux through ℋ ∩ {T ≤ t̃ ≤ σ} of the weighted energy of Γ^α h_R for a metric g with |g − g_b0| ≤ C r⁻² is at
most C 𝔉_ℋ^a[Γ^α h_R], and beyond r = ϱ it is at most C(λ) ϱ^(2a−7) for a < 7/2.

*Proof.* (i) On 𝒰, v > v_end, so g_λ − g_b0 = g_λ − g0 = Σ_(k=4)^9 r^(−k/2) G_k + u_9 ([[prop:bondi-hierarchy]], G_3 = 0
there). After the shell the coefficients G_k with k ≤ 9 obey the flat recursion [[eq:own-flat-recursion]], by the count
in the proof of [[lem:own-means]] applied to the forcing of [[prop:bondi-hierarchy]]: with G_3 = 0 and μ constant,
∂_v G_4 = 2S_3 = 0 and ∂_v G_5 = S_(7/2) = 0 ([[prop:own-tail]] (a)), so every forcing term is O(r⁻⁶). On the other side,
at fixed v ∈ [v1, V′_P], Taylor's formula in s = (v − v1)/r gives r^(−p) F_p(s) = Σ_(m<m₀) r^(−p−m) ∂_s^m F_p(0)(v −
v1)^m/m! + O(r^(−p−m₀)), with derivatives; since □_η(r^(−p) F_p) = 0, the coefficients of r^(−q) of this expansion solve
the same recursion (by [[eq:own-box-p]] at μ = 0, order by order), and at v = v1 they equal F_q(0) = G_(2q)(v1). The
recursion fixes the coefficient of r^(−q) at v from its value at v1 and the coefficient of r^(−q+1); so the coefficients
of r^(−k/2), k ≤ 8, of g_λ − g_b0 and of Σ agree on 𝒰, and h_R = O(r^(−9/2)) there with all derivatives. On ℋ, s = 0, Z =
rℓ (Z = (v − v1)∂_v + rℓ in (v, r, x̂)) and Ω are tangent, ∂_t = ∂_v; the ℓ-gain of u_9 ([[prop:bondi-hierarchy]]) and of
the explicit terms give the last claim.

(ii) At fixed v, g_λ − g_b0 = Σ_(k=4)^8 r^(−k/2) G_k + u_8, and by (i) the coefficients of order at most 4 of Σ are the
G_(2q), q ≤ 4; so h_R = u_8 − Σ_rem, and u_8 = e_(8) + Σ_j λ^j m_(j,8) by [[eq:own-e-expansion]]. Σ_rem is the sum over
p ∈ Π of r^(−p) times the Taylor remainder of F_p in s at the order m_p := ⌊4 − p⌋ + 1, which is O(λ s^(m_p)) with every
derivative of order at most k1 + 1 in (s, x̂) by [[lem:own-sigma-data]], and p + m_p ≥ 9/2; ℓ = ∂_r at fixed v and r⁻¹Ω
gain r⁻¹ on it, while ∂_t = ∂_v and Z = (v − v1)∂_v + rℓ keep its order. So 𝔉_ℋ^a[Γ^α Σ_rem] ≤ C λ² ∫ r^(2a−11+3) dr
≤ C λ² for a < 7/2. The means' part Σ_j λ^j m_(j,8) has, by [[lem:own-means]], λ-independent coefficients with the
ℓ-gain, and flux O(λ²). The part e_(8) has flux ν(λ) → 0 by [[lem:own-e-flux]] (2) with j = k1.

(iii) ℋ = {v = v1} is null for g_b0, and the flux of T_(g_b0)[φ](X, −∇v), X = w∂_t, through it contains only ℓφ and the
derivatives along the spheres, with bounded coefficients; w ≤ C r^(2a) on ℋ. For g = g_b0 + H the difference of the
integrands is at most C|H| w |∂φ|², which the last term of [[eq:own-flux-n]] bounds. The tail: by (i), at fixed λ the
integrand of [[eq:own-flux-n]] for Γ^α h_R is O(r^(2a−11+3)), and its integral beyond ϱ is C(λ) ϱ^(2a−7)/(7 − 2a). ∎

### The far region by homogeneity {#sec:far-homogeneity}

This section proves the exponents on which the weighted energy estimate of Section [[sec:own-continuation]] rests: the
decay of the coefficients of the linearised operator, the degree of the residual of the subtracted expansion, and the
naturality of the operator under G. Every exponent is obtained by counting powers of r under one dilation.

*Setting.* We work in the far region with the Cartesian coordinates (t, x), t = τ, of the Notation, r := |x|,
x̂ := x/r, v = t + r, μ = μ_end, and

    g_b0 = η + μ m,      m := r⁻² dv ⊗ dv,      P(h) := Ric^H(g_b0 + h; g_b0).                       {#eq:far-operator}

For Lorentzian metrics g and g′, Ric^H(g; g′) denotes the expression [[eq:gauge]] with g′ in place of g0: the vector
field D and the connection ∇̂ are formed with g′. By [[eq:background]], g_b0 = g0 on {v ≥ v_end}, which contains W, so
there P(h) is Ric^H(g0 + h) of [[eq:gauge]]. Pointwise norms |·| are those of [[sec:profiles]]: the Euclidean operator
norm on symmetric 2-tensors and the Frobenius norm on arrays of higher rank. W, ℋ, the slices Σ̃_σ, s = (v − v1)/r and
r_σ are those of Section [[sec:own-far-part]]: on W, 0 ≤ s ≤ 5/4 and |t − v1| ≤ r, and r_σ ≥ c_W (1 + |σ|)
([[lem:own-wedge]] (b)). The commutators are Γ ∈ {∂_t, L_Ω_ab, Z}, with Ω_ab := x_a ∂_b − x_b ∂_a and
Z := (t − v1) ∂_t + x·∂_x, acting on Cartesian components; Γ^α is a product of |α| of them. The subtracted expansion
Σ = Σ_(p∈Π) Σ_p, Σ_p = r^(−p) F_p(s, x̂), is that of [[def:own-sigma]]: □_η Σ_p = 0 for every p ∈ Π; each F_p is smooth
up to the boundary on [0, 3/2] × S³ ([[lem:own-self-similar]]), so that Σ_p is smooth up to the boundary on the closed
cone 𝒞 := {r > 0, 0 ≤ s ≤ 3/2}; and Σ_p = λ Σ̂_p, the derivatives of Σ̂_p on 𝔎 := {r = 1, 0 ≤ s ≤ 3/2} being bounded as
in [[lem:own-sigma-data]] (b): those of order at most k1 + 4 independently of λ, all of them at fixed λ.

*The dilation.* For ς > 0 put D_ς(t, x) := (v1 + ς(t − v1), ς x). It fixes s and x̂, maps {r = 1} onto {r = ς} and 𝒞
onto itself, and Z = (d/dς) D_ς at ς = 1. A function, or a tensor read through its Cartesian components, is
*homogeneous of degree −q* if f(D_ς X) = ς^(−q) f(X) for all ς > 0. Then ∂_a f is homogeneous of degree −q − 1,
Z f = −q f (differentiate in ς at ς = 1), and L_Ω_ab f is homogeneous of degree −q, D_ς commuting with rotations. The
region 𝒞_1 := 𝒞 ∩ {r ≥ 1} is the union of the images D_ς 𝔎, ς ≥ 1, and W ⊂ 𝒞_1, as 4R ≥ 1. So a function f on 𝒞,
smooth up to the boundary and homogeneous of degree −q, satisfies |∂^j f| ≤ (max_𝔎 |∂^j f|) r^(−q−j) on 𝒞_1. In
particular m and every Σ_p are homogeneous, of degrees −2 and −p, and Γ^α Σ_p is λ times a sum of homogeneous tensors
of degrees at most −p (Z and L_Ω_ab keep the degree, ∂_t lowers it by one), whose derivatives of order j on 𝔎 are
combinations of derivatives of Σ̂_p of order at most j + |α|. Hence on 𝒞_1

    |∂^j m| ≤ C_j r^(−2−j),      |∂^j Γ^α Σ_p| ≤ C_(j,α) λ r^(−p−j),                               {#eq:far-sigma-bounds}

with C_(j,α) independent of λ for j + |α| ≤ k1 + 4 and depending on λ otherwise.

**Lemma {#lem:far-scaling}** (structure and scaling of the operator). (a) With g := g_b0 + h and Γ̂ := Γ[g_b0],

    P(h)_mn = −(1/2) g^(ab) ∂_a ∂_b g_mn + q_mn(g)(∂g, ∂g) + l_mn(g)(Γ̂, ∂g) + c_mn(g)(∂Γ̂) + c′_mn(g)(Γ̂, Γ̂),

where q, l, c and c′ are multilinear in the displayed arguments with coefficients polynomial in the components of g
and g⁻¹. The components of Γ̂ are μ Θ_3 + μ² Θ_5, with Θ_3 and Θ_5 homogeneous of degrees −3 and −5.
(b) For every ς > 0 and every h, writing P_μ for P and h^(ς) := h ∘ D_ς,

    ς² P_μ(h)(D_ς X) = P_(μ ς⁻²)(h^(ς))(X).                                                    {#eq:far-scaling}

*Proof.* (a) In Cartesian coordinates Γ[η] = 0, so [[eq:gauge]] with reference metric η reads Ric^H(g; η)_mn =
−(1/2) g^(ab) ∂_a∂_b g_mn + q_mn(g)(∂g, ∂g) with q purely quadratic, its coefficients polynomial in g and g⁻¹; and the
gauge term of Ric^H(g; η) is −(1/2)(g_mρ ∂_n Γ^ρ + g_nρ ∂_m Γ^ρ), Γ^ρ := g^(ab) Γ[g]^ρ_ab. For the reference g_b0,
D^ρ = Γ^ρ − g^(ab) Γ̂^ρ_ab and ∇̂_n D^ρ = ∂_n D^ρ + Γ̂^ρ_nν D^ν. So Ric^H(g; g_b0) is Ric^H(g; η) plus the
symmetrisation of g_mρ (∂_n(g^(ab) Γ̂^ρ_ab) − Γ̂^ρ_nν (Γ^ν − g^(ab) Γ̂^ν_ab)). Here ∂_n g^(ab) = −g^(ac) g^(bd) ∂_n g_cd
and Γ^ν is linear in ∂g with coefficients polynomial in g⁻¹, which gives the form stated. By [[eq:background]],
g_b0⁻¹ = η⁻¹ − μ r⁻² L0 ⊗ L0 with L0 homogeneous of degree 0, and ∂g_b0 = μ ∂m, which gives the degrees of Γ̂.
(b) D_ς^* dt = ς dt and D_ς^* dx^i = ς dx^i, so D_ς^* η = ς² η; and v ∘ D_ς = v1 + ς(v − v1), r ∘ D_ς = ς r, so
D_ς^* m = m. Hence D_ς^* g_b0(μ) = ς² g_b0(μ ς⁻²), and the components of ς⁻² D_ς^* h are those of h^(ς). Ric^H is built
from the two metrics by Levi-Civita connections, curvature and contraction, so φ^* Ric^H(g; g′) = Ric^H(φ^* g; φ^* g′)
for every diffeomorphism φ, and Ric^H(c g; c g′) = Ric^H(g; g′) for every constant c > 0 (Christoffel symbols are
unchanged, D^ρ is multiplied by c⁻¹ and g_mρ by c). With φ = D_ς and c = ς⁻², D_ς^* P_μ(h) = P_(μ ς⁻²)(ς⁻² D_ς^* h),
and the components of D_ς^* T are ς² T(D_ς ·). ∎

**Proposition {#prop:far-coefficients}** (decay of the coefficients). On {r ≥ 4R}, where μ r⁻² ≤ 1/16, let H be a
symmetric tensor with |H| ≤ 1/50, g := g_b0 + H, and write

    DP(H)[k] = −(1/2) g^(ab) ∂_a ∂_b k + B(H)·∂k + C(H) k.

There are constants C and C_j, depending only on μ and j, such that:
(a) |B(H)| ≤ C(μ r⁻³ + |∂H|) and |C(H)| ≤ C(μ r⁻⁴ + |∂∂H| + |∂H|²);
(b) |g⁻¹ − g_b0⁻¹| ≤ C|H| and |B(H) − B(0)| ≤ C(|∂H| + μ r⁻³ |H|), and the coefficient of order zero satisfies
the bound |C(H) − C(0)| ≤ C(|∂∂H| + |∂H|² + μ r⁻³ |∂H| + μ r⁻⁴ |H|);
(c) for every j ≥ 1, the coefficients of (μ ∂_μ)^j DP(H) are bounded by C_j μ r⁻² (second order),
C_j μ (r⁻³ + r⁻²|∂H|) (first order) and C_j μ (r⁻⁴ + r⁻² |∂∂H| + r⁻² |∂H|² + r⁻³ |∂H|) (zero order).
In particular B(0) = O(μ r⁻³) and C(0) = O(μ r⁻⁴); and for λ small and H = Σ on W, by [[eq:far-sigma-bounds]],
g⁻¹ − g_b0⁻¹ = O(λ r⁻²), B(Σ) − B(0) = O(λ r⁻³) and C(Σ) − C(0) = O(λ r⁻⁴).

*Proof.* Differentiating [[lem:far-scaling]] (a) in h in the direction k,

    DP(H)[k] = −(1/2) g^(ab) ∂_a∂_b k + (1/2)(g⁻¹ k g⁻¹)^(ab) ∂_a∂_b g + 2 q(g)(∂g, ∂k) + (∂_g q)[k](∂g, ∂g)
               + l(g)(Γ̂, ∂k) + (∂_g l)[k](Γ̂, ∂g) + (∂_g c)[k](∂Γ̂) + (∂_g c′)[k](Γ̂, Γ̂),

so B(H)·∂k = 2q(g)(∂g, ∂k) + l(g)(Γ̂, ∂k) and C(H)k is the rest. *Bounds on g.* The covector dv has Cartesian components
(1, x̂), of Euclidean length √2, so |μ m| = 2μ r⁻² ≤ 1/8. By [[eq:background]], g_b0⁻¹ = η⁻¹ − μ r⁻² L0 ⊗ L0 with |L0|² =
2, so |g_b0⁻¹| ≤ 9/8. Hence |g_b0⁻¹ H| ≤ 9/400, and g = g_b0 (1 + g_b0⁻¹ H) is invertible, with norm of the
inverse |g⁻¹| ≤ (9/8)/(1 − 9/400) < 6/5; also the norm of g is at most 1 + 1/8 + 1/50 < 6/5. So the components of g and
g⁻¹ are bounded by an absolute constant, and so are the coefficients of q, l, c, c′ and their g-derivatives. (a) By
[[eq:far-sigma-bounds]] and [[lem:far-scaling]] (a), the first derivatives satisfy |∂g_b0| + |Γ̂| ≤ C μ r⁻³ and the
second ones |∂∂g_b0| + |∂Γ̂| ≤ C μ r⁻⁴. So |∂g| ≤ C μ r⁻³ + |∂H| and |∂∂g| ≤ C μ r⁻⁴ + |∂∂H|, and (a) follows term by
term, with μ² r⁻⁶ ≤ μ r⁻⁴/16 and 2|Γ̂| |∂H| ≤ |Γ̂|² + |∂H|². (b) Each coefficient is a polynomial in g^(±1), ∂g, ∂∂g, Γ̂,
∂Γ̂. Between H and 0, g^(±1) change by at most C|H| (g⁻¹ − g_b0⁻¹ = −g⁻¹ H g_b0⁻¹), ∂g by ∂H, ∂∂g by ∂∂H, and Γ̂ not at
all. Bounding the difference of a product by the sum, over its factors, of the change of one factor times the bounds of
the others gives (b). (c) The coefficients depend on μ only through g = η + μ m + H and Γ̂. The operator μ ∂_μ maps μ m,
μ ∂m and μ ∂∂m to themselves and g⁻¹ to −g⁻¹ (μ m) g⁻¹. By [[lem:far-scaling]] (a), Γ̂ = μ Θ_3 + μ² Θ_5, and μ ∂_μ maps
it to μ Θ_3 + 2μ² Θ_5; likewise ∂Γ̂. So μ ∂_μ of a term of the proof of (a) is a sum of terms in each of which one factor
is replaced: a factor of size O(1) by one of size O(μ r⁻²), and ∂g, ∂∂g, Γ̂, ∂Γ̂ by factors of sizes O(μ r⁻³), O(μ r⁻⁴),
O(μ r⁻³), O(μ r⁻⁴). Collecting the terms gives (c) for j = 1. A further μ ∂_μ acts on the new factors in the same way: it
maps μ m, μ ∂m and μ ∂∂m to themselves, μ Θ_3 + 2μ² Θ_5 to μ Θ_3 + 4μ² Θ_5, and a g-derivative of a coefficient evaluated
on μ m to terms of the same size or smaller. So each application replaces a factor by one of the same size or a smaller
one, and induction on j gives (c). ∎

**Proposition {#prop:far-residual}** (the degree of the residual). Let M_1[h] := ∂_μ(DP_μ(0)[h]) at μ = 0, the first
variation of P_μ at 0 differentiated in the mass, and M_2[h, h′] the second variation of Ric^H(η + ·; η) at 0; put

    Q_6 := μ M_1[Σ_2] + (1/2) M_2[Σ_2, Σ_2],

homogeneous of degree −6. For λ small, on W, for every multi-index α of commutators Γ and constants c = (c_i),

    |Π_i (Γ_i + c_i) P(Σ)| ≤ C_(α,c) λ r⁻⁶,   |Π_i (Γ_i + c_i) (P(Σ) − Q_6)| ≤ C_(α,c) λ r^(−13/2),  {#eq:far-residual}

with C_(α,c) independent of λ for |α| ≤ k1 + 2 and depending on λ otherwise.

*Proof.* For X ∈ 𝔎′ := 𝒞 ∩ {½ ≤ r ≤ 2}, 0 ≤ e ≤ 1/16 and d = (d_p)_(p∈Π) with |d| ≤ d_0, put

    Ψ(X; e, d) := Ric^H(η + e m + Σ_p d_p Σ̂_p; η + e m)(X).

Its components are rational in the jets of order at most two of the two metrics at X. The denominators do not vanish:
det(η + e m) = −1, since dv is null for η ([[eq:background]]), and d_0 is small. So Ψ is smooth in (e, d), and in X up
to the boundary of 𝔎′. Its derivatives of order at most k1 + 2 in X, with any number of derivatives in (e, d), are
bounded independently of λ, since the derivatives of order at most k1 + 4 of the Σ̂_p are bounded on 𝔎′ independently
of λ (on 𝔎 by [[lem:own-sigma-data]] (b), and on 𝔎′ by homogeneity); at fixed λ all its derivatives are bounded. For λ
small the values (e, d) = (μ ς⁻², (λ ς^(−p))_p), ς ≥ 4R, lie in this set. D_ς maps 𝒞 onto itself and
Σ̂_p ∘ D_ς = ς^(−p) Σ̂_p, so [[eq:far-scaling]] gives, for X ∈ 𝔎′ and ς ≥ 4R,

    P(Σ)(D_ς X) = ς⁻² Ψ(X; μ ς⁻², (λ ς^(−p))_p).                                                    {#eq:far-psi}

Three facts about Ψ. First, Ψ(X; e, 0) = Ric(η + e m)(X) = 0 for every e: the reference and the metric coincide, so
D = 0, and η + e m is flat for e = 0 and the vacuum metric of [[prop:vaidya]] (a) with constant mass e for e > 0. Hence
Ψ = Σ_p d_p Ψ_p with Ψ_p := ∫_0^1 ∂_(d_p)Ψ(X; e, y d) dy smooth, and Taylor's formula for each Ψ_p at (e, d) = (0, 0)
gives

    Ψ(X; e, d) = Σ_p d_p ∂_(d_p)Ψ(X; 0, 0) + Σ_p e d_p ∂_e ∂_(d_p)Ψ(X; 0, 0)
                 + (1/2) Σ_(p,p′) d_p d_p′ ∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0) + Rem(X; e, d),                {#eq:far-taylor}

where Rem = Σ_p d_p Ψ′_p with Ψ′_p smooth and vanishing to second order at (e, d) = (0, 0). So Rem is at most
C |d| (|e| + |d|)² in norm, uniformly in X and (e, d). Second, since Γ[η] = 0, the linearisation of Ric^H(η + ·; η) at
0 is −(1/2) □_η acting on components. So ∂_(d_p)Ψ(X; 0, 0) = −(1/2) □_η Σ̂_p(X), ∂_e ∂_(d_p)Ψ(X; 0, 0) = M_1[Σ̂_p](X)
and ∂_(d_p) ∂_(d_p′) Ψ(X; 0, 0) = M_2[Σ̂_p, Σ̂_p′](X). Third, [[eq:far-psi]] holds for every mass in place of μ and for
independent amplitudes λ_p in place of λ, both sides being smooth in them near 0. By the second fact, the coefficients
of μ^i Π_p λ_p^(n_p) in their Taylor expansions at 0 are, on the left, constant multiples of −(1/2) □_η Σ̂_p,
M_1[Σ̂_p] and M_2[Σ̂_p, Σ̂_p′] at D_ς X, and on the right ς^(−2−2i−Σ n_p p) times the same multiples at X. Hence
(□_η Σ̂_p)(D_ς X) = ς^(−p−2) (□_η Σ̂_p)(X), M_1[Σ̂_p](D_ς X) = ς^(−p−4) M_1[Σ̂_p](X) and
M_2[Σ̂_p, Σ̂_p′](D_ς X) = ς^(−p−p′−2) M_2[Σ̂_p, Σ̂_p′](X). So, by [[eq:far-psi]], the term of [[eq:far-taylor]] with
e^i Π d_p^(n_p), at e = μ ς⁻² and d_p = λ ς^(−p) and multiplied by ς⁻², is a term of P(Σ) at D_ς X homogeneous of
degree −2 − 2i − Σ n_p p; in particular Q_6 is homogeneous of degree −6.

Now count degrees, with Σ n_p ≥ 1 and ς = r. The terms of degree greater than −13/2, that is 2 + 2i + Σ n_p p < 13/2,
are: i = 0 and one factor d_p, every p ∈ Π (degree −p − 2); i = 1 and the factor d_2 (degree −6); i = 0 and d_2²
(degree −6). The first vanish on 𝒞, since □_η Σ_p = 0 there for every p ∈ Π. The other two sum to Q_6, which carries
the factor λ of Σ_2. Every other term of [[eq:far-taylor]] has degree at most −13/2 and carries a factor λ. Since |d| ≤ C λ ς⁻², Rem
contributes ς⁻² |Rem| ≤ C λ ς⁻⁴ (μ ς⁻² + λ ς⁻²)² ≤ C λ r⁻⁸. So P(Σ) − Q_6 is at most C λ r^(−13/2) in norm, and P(Σ) at
most C λ r⁻⁶. The terms of degree −13/2 are μ M_1[Σ_(5/2)] and M_2[Σ_2, Σ_(5/2)].

The commutators. A homogeneous term of degree −q is mapped by Z to −q times itself, by L_Ω_ab to a homogeneous term of
degree −q and by ∂_t to one of degree −q − 1, so it keeps its bound. For the remainder put
Rem′(D_ς X) := ς⁻² Rem(X; μ ς⁻², (λ ς^(−p))_p); it does not depend on the choice of (X, ς) with D_ς X given, since P(Σ)
and the homogeneous terms do not. Differentiation in ς gives Z Rem′ = −ς⁻² (2 + 2e ∂_e + Σ_p p d_p ∂_(d_p)) Rem. Here
e ∂_e Rem and d_p′ ∂_(d_p′) Rem are again of the form Σ_p d_p Ψ″_p, with Ψ″_p vanishing to second order at
(e, d) = (0, 0), and so is an X-derivative of Rem. Further ∂_a Rem′ = ς⁻¹ (∂_X Rem)′, and L_Ω_ab, which commutes with
D_ς, maps Rem′ to (L_Ω_ab Rem)′. So every Π_i (Γ_i + c_i) Rem′ is O(λ r⁻⁸), and [[eq:far-residual]] follows. At most
|α| derivatives in X enter, and the homogeneous terms involve the Σ̂_p through their jets of order |α| + 2 on 𝔎; so
the constants are independent of λ for |α| ≤ k1 + 2. ∎

**Lemma {#lem:far-naturality}** (naturality). Let O ∈ O(4), Õ(t, x) := (t, O x) and Ō := diag(1, O). For every
symmetric h, in Cartesian components,

    P(Ōᵀ h(Ō ·) Ō) = Ōᵀ P(h)(Ō ·) Ō.

In particular, for O ∈ G = O(2) × O(2), P maps G-invariant tensors to G-invariant tensors, and Õ^* g solves
Ric^H(·; g_b0) = 0 whenever g does.

*Proof.* r ∘ Õ = r and t ∘ Õ = t, so Õ^* η = η, Õ^* dv = dv and Õ^* g_b0 = g_b0. By the naturality of Ric^H used in
the proof of [[lem:far-scaling]] (b), Õ^* P(h) = Ric^H(Õ^* g_b0 + Õ^* h; Õ^* g_b0) = P(Õ^* h), and the Cartesian
components of Õ^* h are Ōᵀ h(Ō ·) Ō. ∎

### The expansion after the shell to every order {#sec:cutoff-expansion}

The truncated problems of Section [[sec:own-continuation]] interpolate, on a band of bounded width in v, between the
data of g_λ and data that continue them to spatial infinity. The commuted energies of the remainder at the initial
slice are bounded uniformly in the truncation only if the two data agree on the band to high order in r⁻¹: the
commutator Z is transverse to the initial slice at the band with a coefficient of size |T|, and each Z turns a time
derivative of a mismatch into a factor |T| ([[rem:cutoff-growth]]). This section constructs continuation data that
agree with those of g_λ to every prescribed order and are homogeneous, so that Z costs nothing on them. It uses only the
expansion of [[prop:bondi-hierarchy]] at fixed λ; no smallness in λ is needed of the new terms, because they enter only
the data of the truncated problems, whose effect disappears as T → −∞ at fixed λ.

*Setting.* We use the notation of Section [[sec:far-homogeneity]]: P(h) = Ric^H(g_b0 + h; g_b0), g_b0 = η + μ m with
m := r⁻² dv ⊗ dv, μ = μ_end, the coordinates (v, r, x̂) with ℓ = ∂_r at fixed (v, x̂) and ∂_v the derivative at fixed
(r, x̂), which is ∂_t at fixed x, and the commutators Γ ∈ {∂_t, L_Ω_ab, Z}, Z = (t − v1) ∂_t + x·∂_x. The Cartesian
derivatives are

    ∂_t = ∂_v,     ∂_i = x̂_i (∂_v + ℓ) + r⁻¹ Y_i,     Y_i := r (∂_i − x̂_i x̂·∂_x),               {#eq:cutoff-cartesian}

where Y_i is a vector field on the sphere {v, r fixed}, acting on x̂ only, with coefficients smooth in x̂. Put
I_1 := [v_end + 1, V′_P − 1], which contains v1 (v1 ≥ v_end + 2 and v1 ≤ V′_P − κ_P − 1 − m_Ω,
[[lem:interior-far-part]] (ii)), d_V := V′_P − v1, and 𝒰_1 := {(v, r, x̂) : v ∈ I_1, r ≥ r_1}, with r_1 so large that
𝒰_1 lies in the far region of P′ (there t_P is comparable with r, and v + h_P(τ) ≤ V′_P − 1 + κ_P < V′_P). On 𝒰_1,
v > v_end, so g0 = g_b0, G_3 = 0 ([[eq:own-g3]], env = 0) and, by [[prop:bondi-hierarchy]], for every J ≥ 4

    g_λ − g_b0 = H_J + u_J,     H_J := Σ_(k=4)^J r^(−k/2) G_k.                                            {#eq:cutoff-hj}

A family of smooth tensors F on 𝒰_1, or on a subset of it, is *of strip order q* if |∂_v^i Ω^β ℓ^j F| ≤ C r^(−q−j) for
all i, β, j up to a fixed order, the constant independent of the members of the family. A family of smooth tensors on
W ∩ {r ≥ r′}, for some r′ ≥ 1, is *tame of order q* if |∂^j Γ^α F| ≤ C r^(−q−j) there for all j and α, with C
depending on j and α but not on the member. By [[eq:bondi-expansion]], u_J is of strip order (J + 1)/2, and H_J of strip
order 2, the G_k being bounded with all their derivatives. A *monomial* is r^(−k/2) (v − v1)^n a(x̂) with integers
k, n ≥ 0 and a smooth; its *weight* is n − k/2. Since r^(−k/2) (v − v1)^n = r^(n−k/2) s^n with s = (v − v1)/r, a
monomial is homogeneous, of degree equal to its weight, under the dilation D_ς of Section [[sec:far-homogeneity]].

**Lemma {#lem:cutoff-expansion}** (the operator at fixed v). Let K_0 ≥ 4, let c_4, …, c_(K_0) be smooth symmetric
tensors on I_1 × S³ (Cartesian components), bounded with all derivatives, and put H := Σ_(k=4)^(K_0) r^(−k/2) c_k and
c_k := 0 for k ∉ [4, K_0]. There is r_2 ≥ r_1 and, for every q ∈ ½ℕ, a smooth π_q(v, x̂) such that for every Q ≥ 0
the difference P(H) − Σ_(q≤Q) r^(−q) π_q is of strip order Q + ½ on {v ∈ I_1, r ≥ r_2}; π_q = 0 for q < 3; and

    π_q = ((2q − 5)/2) ∂_v c_(2q−2) − ½ (Δ̊ + (q − 2)(q − 4)) c_(2q−4) + R_q,                             {#eq:cutoff-pi}

where R_q is a finite sum of terms

    a(x̂) μ^j Π_(i=1)^n ∂_v^(d_i) Y^(β_i) c_(k_i),     n ≥ 1,  n + j ≥ 2,  Σ_i d_i ≤ 2,
    Σ_i k_i/2 + 2j + 2 − Σ_i d_i = q,                                                                  {#eq:cutoff-terms}

with Y^(β_i) a product of fields Y_l, and a(x̂) smooth. In particular every c_(k_i) in R_q has k_i ≤ 2q − 4.

*Proof.* By [[lem:far-scaling]] (a), with g = g_b0 + H = η + μ m + H, P(H) is a finite sum of products of components
of g and g⁻¹ with ∂∂g, ∂g ∂g, Γ̂ ∂g, ∂Γ̂ or Γ̂ Γ̂, Γ̂ := Γ[g_b0]. Here ∂g = μ ∂m + ∂H and ∂∂g = μ ∂∂m + ∂∂H, and Γ̂ is
½ g_b0⁻¹ applied to first derivatives of μ m, with g_b0⁻¹ = η⁻¹ − μ r⁻² L0 ⊗ L0 ([[eq:background]]), the Cartesian
components of L0 and of dv being functions of x̂. For r ≥ r_2, |g_b0⁻¹ H| ≤ ½ on {v ∈ I_1}, and
g⁻¹ = Σ_(ν≥0) (−g_b0⁻¹ H)^ν g_b0⁻¹. So every term of P(H) is a product of constant tensors, of factors μ r⁻² b(x̂)
(from μ m and from g_b0⁻¹ − η⁻¹), of factors r^(−k/2) c_k, and of exactly two derivatives, Γ̂ counting as one derivative
of a factor μ r⁻² b and ∂Γ̂ as two. By [[eq:cutoff-cartesian]], ∂_v maps r^(−k/2) c to r^(−k/2) ∂_v c and annihilates
r⁻² b(x̂) and every function of x̂; ℓ and r⁻¹ Y_i map r^(−k/2) c to r^(−k/2−1) times −(k/2) c and Y_i c, and r⁻² b to
r⁻³ times a function of x̂. Hence a product with n factors c_(k_i), j factors μ r⁻² b, and d_i derivatives ∂_v on the
i-th factor c_(k_i) is a sum of terms r^(−q) times a term of the form [[eq:cutoff-terms]], with
q = Σ_i k_i/2 + 2j + 2 − Σ_i d_i: every derivative other than a ∂_v on a factor c_(k_i) raises the power of r⁻¹ by
one or gives zero. Truncating the Neumann series after ν_0 terms leaves a remainder of strip order 2ν_0, and the terms
with q > Q have q ≥ Q + ½; this gives the expansion, with π_q the sum of the terms of order q.

The terms with n = 0 are the expansion of P(0) = Ric^H(g_b0; g_b0) = Ric(g_b0) = 0 (with reference g_b0 itself the
vector field D vanishes, and g_b0 is the Tangherlini metric), so they sum to zero at every order. The terms with n = 1
and j = 0 come from −½ η^(ab) ∂_a ∂_b H only: every other term of [[lem:far-scaling]] (a) that is linear in H contains
Γ̂, ∂Γ̂, μ ∂m, μ ∂∂m or a factor μ r⁻² L0 ⊗ L0. By [[eq:own-box-p]] at μ = 0, applied to each Cartesian component,
−½ □_η (r^(−k/2) c_k) = ((k − 3)/2) r^(−k/2−1) ∂_v c_k − ½ r^(−k/2−2) (Δ̊ + k²/4 − k) c_k, which at q = k/2 + 1 and
q = k/2 + 2 gives the first two terms of [[eq:cutoff-pi]] ((k/2)² − k = (q − 2)(q − 4) for k = 2q − 4). The terms with
n + j ≥ 2 form R_q. The flat terms have d ≤ 1, since □_η has no term ∂_v² in (v, r, x̂) ([[eq:wave-operator-vr]] at
μ = 0); so they start at q = 3, and the terms of R_q at q ≥ 4. In a term of R_q each factor contributes at least 2 to
q, so k_i/2 ≤ q − 2. ∎

**Lemma {#lem:cutoff-polynomial}** (the coefficients after the shell). For every k ≥ 4 the restriction of G_k to
I_1 × S³ is a polynomial in v − v1 of degree at most k/2 − 2,

    G_k = Σ_(0≤n≤k/2−2) (v − v1)^n G_(k,n)(x̂),                                                        {#eq:cutoff-gkn}

with G_(k,n) smooth and G-invariant; so every monomial r^(−k/2)(v − v1)^n G_(k,n) has weight at most −2. For p ∈ Π let
F_(p,n) := (1/n!) ∂_s^n F_p(0, ·) be the Taylor coefficients at s = 0 of the F_p of [[def:own-sigma]], and put
F_(p,n) := 0 for p ∉ Π. Then G_(k,n) = F_(k/2−n, n) whenever the weight n − k/2 exceeds −4.

*Proof.* *The recursion.* Fix J ≥ 4. On 𝒰_1, P(H_J + u_J) = Ric^H(g_λ; g0) = 0, g_λ being vacuum and in the wave-map
gauge relative to g0 ([[thm:past-construction]]). Write P(H) = −½ g(H)^(ab) ∂_a ∂_b H + 𝒬(X, H, ∂H), 𝒬 collecting the
first-order terms of [[lem:far-scaling]] (a) and −½ g^(ab) ∂_a ∂_b g_b0. Then P(H_J + u_J) − P(H_J) is the sum of
−½ g_λ^(ab) ∂_a ∂_b u_J, of −½ (g_λ^(ab) − g_J^(ab)) ∂_a ∂_b (g_b0 + H_J) with g_J := g_b0 + H_J, and of
𝒬(X, H_J + u_J, ∂H_J + ∂u_J) − 𝒬(X, H_J, ∂H_J). By [[eq:cutoff-cartesian]] the Cartesian Hessian of a function φ is
(∂_a v)(∂_b v) ∂_v² φ plus terms each containing ℓ or r⁻¹ Y, or a first derivative with a coefficient O(r⁻¹) from the
derivatives of x̂; and g_λ⁻¹(dv, dv) = (g_λ⁻¹ − g_b0⁻¹)(dv, dv) = O(r⁻²), since dv(L0) = 0 makes dv null for g_b0. So
the first term is of strip order (J + 3)/2. The second and third contain u_J or ∂u_J times factors of strip order at
least 2, and are of strip order (J + 5)/2. Hence P(H_J) is of strip order (J + 3)/2, and by [[lem:cutoff-expansion]]
with c_k = G_k, multiplying by r^q and letting r → ∞ at fixed (v, x̂), π_q = 0 for q ≤ (J + 2)/2. As J is arbitrary,
for every q ≥ 3

    (2q − 5) ∂_v G_(2q−2) = (Δ̊ + (q − 2)(q − 4)) G_(2q−4) − 2 R_q,                                {#eq:cutoff-recursion}

R_q being formed from the G_k, k ≤ 2q − 4, by [[eq:cutoff-terms]] (G_2 := G_3 := 0).

*The degree.* By induction on k. For k = 4 (q = 3), R_3 = 0 and G_2 = 0, so ∂_v G_4 = 0. Let k ≥ 5, q := (k + 2)/2,
and suppose the claim for 4 ≤ k′ < k. G_(k−2) has degree at most q − 4, and a term [[eq:cutoff-terms]] of R_q has
degree at most Σ_i (k_i/2 − 2) − Σ_i d_i = q − 2 − 2j − 2n ≤ q − 6. So ∂_v G_k, by [[eq:cutoff-recursion]] with
2q − 5 = k − 3 > 0, is a polynomial of degree at most q − 4 = k/2 − 3 (zero if that is negative), and
G_k(v) = G_k(v1) + ∫_(v1)^v ∂_v G_k has degree at most k/2 − 2. The coefficients are smooth, and G-invariant because G_k
is ([[prop:bondi-hierarchy]]) and G fixes v.

*The weights above −4.* Take in [[eq:cutoff-recursion]] the coefficient of (v − v1)^n, with k := 2q − 2:
(k − 3)(n + 1) G_(k,n+1) = (Δ̊ + (q − 2)(q − 4)) G_(k−2,n) − 2 [R_q]_n, where [R_q]_n = 0 for n > q − 6. The monomials
(k, n + 1) and (k − 2, n) have the same weight n + 1 − k/2 =: −p. If p < 4 then n > q − 6, and with k = 2(p + n + 1),

    (n + 1)(2p + 2n − 1) G_(2(p+n+1), n+1) = (Δ̊ + (p + n)(p + n − 2)) G_(2(p+n), n).       {#eq:cutoff-weight-recursion}

The weights are at most −2 and lie in ½ℤ, so p < 4 means p ∈ {2, 5/2, 3, 7/2} ⊂ Π. For p ∈ Π, the calculation in the
proof of [[lem:own-self-similar]], made for a smooth F(s, x̂) with Δ̊ acting on each Cartesian component, gives

    □_η (r^(−p) F) = −2 r^(−p−2) [ (s − s²/2) ∂_s² F + (p − ½)(1 − s) ∂_s F − ½ (p² − 2p + Δ̊) F ].      {#eq:cutoff-ode}

Since □_η Σ_p = 0, the bracket vanishes for F = F_p on [0, 3/2] × S³, and its coefficient of s^n at s = 0 is
½ [(n + 1)(2p + 2n − 1) F_(p,n+1) − (Δ̊ + (p + n)(p + n − 2)) F_(p,n)], as n(n − 1) + (2p − 1) n + p² − 2p =
(p + n)(p + n − 2). So the F_(p,n) satisfy [[eq:cutoff-weight-recursion]] too. At n = 0, G_(2p,0) = G_(2p)(v1) = F_p(0) =
F_(p,0) ([[def:own-sigma]]), and 2p + 2n − 1 > 0; by induction on n, G_(2(p+n),n) = F_(p,n). ∎

**Definition {#def:cutoff-extension}** (the continuation of the expansion). For an integer J ≥ 8 put

    Σ′_J := Σ_(8≤k≤J) Σ_(0≤n≤k/2−4) r^(−k/2) (v − v1)^n (G_(k,n) − F_(k/2−n, n))
          = Σ_(8≤k≤J) Σ_(0≤n≤k/2−4) r^(−(k/2−n)) s^n (G_(k,n) − F_(k/2−n, n)),                     {#eq:cutoff-extension}

a finite sum, defined on {r > 0} by its second form, and m_J := g_λ − g_b0 − Σ − Σ′_J on 𝒰_1 ∩ {v ≥ v1}, where Σ is
defined.

**Lemma {#lem:cutoff-extension}** (the continued expansion). Let J ≥ 8.
(a) Σ′_J is a finite sum of smooth homogeneous tensors of degrees at most −4, and it is G-invariant. On
W ∩ {r ≥ 1}, |∂^j Γ^α Σ′_J| ≤ C r^(−4−j) for all j and α, with C depending on λ, J, j and α: Σ′_J is tame of order 4.
(b) m_J is of strip order (J + 1)/2 on 𝒰_1 ∩ {v ≥ v1}, with constants depending on λ and J.
(c) Let λ be below the threshold of [[prop:far-residual]]. There is r_3 ≥ r_2, depending on λ and J, such that the
bound |Σ| + |Σ′_J| ≤ 1/100 holds on W ∩ {r ≥ r_3}, and P(Σ + Σ′_J) is tame of order 6 on W ∩ {r ≥ r_3}, with
constants depending on λ and J.

*Proof.* (a) Each term is r^(−p) s^n a(x̂) with p = k/2 − n ≥ 4, a polynomial in s with smooth coefficients, so smooth
and homogeneous of degree −p on 𝒞_1 = {r ≥ 1, 0 ≤ s ≤ 3/2} ⊃ W. The bounds follow as [[eq:far-sigma-bounds]], from the
dilation (Section [[sec:far-homogeneity]]). G-invariance: G_(k,n) is a Taylor coefficient at v = v1 of the G-invariant
G_k ([[lem:cutoff-polynomial]]); G_(2p)(v1) is G-invariant and the equation of [[lem:own-self-similar]] commutes with G,
so each F_p, and each of its Taylor coefficients F_(p,n), is G-invariant.

(b) For p ∈ Π let M_p := ⌊J/2 − p⌋ ≥ 0 and split

    Σ_p = Σ_(n≤M_p) r^(−p−n) (v − v1)^n F_(p,n) + r^(−p) s^(M_p+1) ρ_p(s, x̂),

with ρ_p smooth on [0, 3/2] × S³ (Taylor's formula with integral remainder; F_p is smooth there by
[[lem:own-self-similar]]). The polynomial part of Σ consists of the monomials r^(−k/2)(v − v1)^n F_(k/2−n, n) with
k ≤ J. By [[lem:cutoff-polynomial]], H_J is the sum of the monomials r^(−k/2)(v − v1)^n G_(k,n), k ≤ J, and
G_(k,n) = F_(k/2−n, n) at the weights above −4; at the weights −4 and below, the coefficient of Σ plus that of Σ′_J is
F_(k/2−n,n) + (G_(k,n) − F_(k/2−n,n)) = G_(k,n). Hence, by [[eq:cutoff-hj]],

    m_J = u_J − Σ_(p∈Π) r^(−p) s^(M_p+1) ρ_p(s, x̂).

u_J is of strip order (J + 1)/2. On 𝒰_1 ∩ {v ≥ v1}, 0 ≤ v − v1 ≤ d_V, so 0 ≤ s ≤ d_V/r. With ∂_v = r⁻¹ ∂_s and
ℓ(r^(−p) φ(s, x̂)) = −r^(−p−1) (p φ + s ∂_s φ), every ∂_v^i Ω^β ℓ^j of r^(−p) s^(M+1) ρ is r^(−p−j) times a sum of terms
r^(−i′) ∂_s^(i′)(s^(M+1) ρ′) with ρ′ smooth, each at most C r^(−(M+1)) (1 + d_V)^(M+1); and p + M_p + 1 ≥ (J + 1)/2, as
J/2 − p ∈ ½ℤ.

(c) By (a) and [[eq:far-sigma-bounds]], |Σ| + |Σ′_J| ≤ C r⁻², which gives r_3. For P(Σ): by the proof of
[[prop:far-residual]] (with □_η Σ_4 = 0), P(Σ) is a finite sum of terms homogeneous of degrees at most −6 and of Rem′;
∂ maps a homogeneous term of degree −q′ to one of degree −q′ − 1, and Γ to one of degree at most −q′; and
∂_a Rem′ = ς⁻¹ (∂_X Rem)′, with Γ Rem′ treated there; so |∂^j Γ^α P(Σ)| ≤ C λ r^(−6−j). And
P(Σ + Σ′_J) − P(Σ) = ∫_0^1 DP(Σ + θ Σ′_J)[Σ′_J] dθ, with DP(H)[k] = −½ g^(ab) ∂_a ∂_b k + B(H)·∂k + C(H) k
([[prop:far-coefficients]]); g^(ab), B and C are polynomials in g^(±1), ∂g, ∂∂g, Γ̂ and ∂Γ̂, so by Leibniz's rule,
[[eq:far-sigma-bounds]] and (a) they are tame of orders 0, 3 and 4 for H = Σ + θ Σ′_J, uniformly in θ ∈ [0, 1], while
Σ′_J is tame of order 4; each of the three terms is tame of order 6. ∎

**Remark {#rem:cutoff-weights}** (what is new in Σ′_J). The weight −4 terms of Σ′_J are r⁻⁴ s^n (G_(8+2n,n) − F_(4,n)),
n ≥ 1. They are nonzero in general: at weight −4 the terms R_q of [[eq:cutoff-recursion]] are the products of two
factors of weight −2, or of μ with one, the terms of which Q_6 of [[prop:far-residual]] is made, whereas Σ_4 solves
□_η Σ_4 = 0; the two agree at s = 0. The terms of weight −9/2 and below are the higher homogeneous components of
g_λ − g_b0, truncated as polynomials in s. Their sizes in λ are not controlled here and are not needed.

### The continuation to the far part's past domain of dependence {#sec:own-continuation}

*Setting.* Fix ℓ0 ∈ (3, 4) ∖ {7/2}, a ∈ (ℓ0 − 1, 3) and k1 := max(8, d_1 + 4). On W we use the Kerr–Schild Cartesian
coordinates (t, x), t = τ, and P(h) := Ric^H(g_b0 + h; g_b0), which is the operator [[eq:gauge]] relative to g0 there
(g0 = g_b0 on v ≥ v_end). Put u := t − r, u* := τ_max + 1 and w := (u* − u)^(2a); on W, t ≤ f(r) ≤ τ_max and t − v1 ≥ −r,
so r + 1 ≤ u* − u ≤ 2r + |u* − v1|. The commutators are Γ ∈ {∂_t, L_Ω_ab, Z}, Z := (t − v1)∂_t + x·∂_x, acting on
Cartesian components; for a multi-index α, Γ^α is the product. For a metric g = g_b0 + H on W, |·| denotes the Euclidean
operator norm of a component matrix, and for a function φ and σ ≤ 0,

    E_σ[φ] := ∫_(Σ̃_σ) √|g| T_g[φ](X, −∇t̃) d⁴x,     X := w ∂_t,
    𝔈_k(σ) := Σ_(|α|≤k) Σ_(i≤j) E_σ[(Γ^α h_R)_ij],     h_R := g − g_b0 − Σ,
                                                                                                       {#eq:own-energies}

T_g[φ] := dφ ⊗ dφ − ½ g g⁻¹(dφ, dφ) the energy-momentum tensor of φ for g, d⁴x the coordinate measure of x on Σ̃_σ, and
𝔉_k the corresponding fluxes through ℋ ∩ {T ≤ t̃ ≤ σ}. On Σ̃_σ, d⁵x = dt̃ d⁴x. By [[lem:far-scaling]] (a), in Cartesian
components and with g := g_b0 + h,

    P(h) = −½ g^(ab) ∂_a ∂_b g + Q(g)(∂g, ∂g),
    Q(g)(∂g, ∂g) := q(g)(∂g, ∂g) + l(g)(Γ̂, ∂g) + c(g)(∂Γ̂) + c′(g)(Γ̂, Γ̂),                          {#eq:own-p-split}

where q, l, c and c′ are multilinear with coefficients polynomial in g and g⁻¹, Γ̂ = Γ[g_b0], |∂^i Γ̂| ≤ C r^(−3−i), and
every term carries exactly two derivatives, ∂∂g counting two, ∂g and Γ̂ one each, and ∂Γ̂ two.

**Lemma {#lem:own-margins}** (margins). Let 𝔪 ≤ 1/16 and |f′| ≤ ¼, and s_0 := 1/16 + (1 + 1/256)^(1/2) ≤ 1.0645, which
bounds |g_b0| and |g_b0⁻¹|.
(a) If |H| ≤ η_H < 1/s_0, then |g⁻¹ − g_b0⁻¹| ≤ s_0² η_H/(1 − s_0 η_H): at most 0.0232 for η_H = 1/50, at most 0.0474 for
η_H = 1/25, and at most 0.2845 r⁻² for η_H = r⁻²/4 on r ≥ 8.
(b) If |g⁻¹ − g_b0⁻¹| ≤ c < 7/25 on a region of {r ≥ 4R}, then there g⁻¹(α̂, α̂), g⁻¹(β̂, β̂) ≤ −7/4 + (25/4)c < 0
([[eq:own-cones]]), |g − g_b0| ≤ s_0² c/(1 − s_0 c) ≤ 0.4520, g(∂_t, ∂_t) < −0.485, and g⁻¹(dt̃, dt̃) ≤ −15/16 + (17/16)c
≤ −0.64. So the slices Σ̃_σ are spacelike, ∂_t is timelike, r − 2t̃ decreases and r + 2t̃ increases along future causal
curves, with margins depending on c only.
(c) If |g⁻¹ − g_b0⁻¹| ≤ r⁻²/2 on {r ≥ 4R}, then Φ_W := v + 1/r is a time function there: g⁻¹(dΦ_W, dΦ_W) ≤ −r⁻² + r⁻⁴ < 0
and dΦ_W(∂_t) = 1.
(d) If |H| ≤ 1/50, there are absolute constants c_1, c_2 > 0 with c_1 w |∂φ|² ≤ √|g| T_g[φ](X, −∇t̃) ≤ c_2 w |∂φ|².
(e) If |H| ≤ min(1/50, 𝔪/2), then −∇u and ∂_t are future causal for g, and T_g[φ](∇w, ∂_t) = |w′| T_g[φ](−∇u, ∂_t) ≥ 0.

*Proof.* The (t, r) block of g_b0 is [[−1 + 𝔪, 𝔪], [𝔪, 1 + 𝔪]] (dv = dt + x̂·dx) and that of g_b0⁻¹ is
[[−1 − 𝔪, 𝔪], [𝔪, 1 − 𝔪]], both with eigenvalues of largest modulus 𝔪 + (1 + 𝔪²)^(1/2) ≤ s_0; on the orthogonal
directions both are the identity. (a) is the Neumann series for (g_b0 + H)⁻¹, and the numbers follow from s_0 ≤ 1.0645
(s_0² ≤ 1.1332). (b) |α̂|_E², |β̂|_E² ≤ 4 + 9/4 = 25/4 and |dt̃|_E² = 1 + f′² ≤ 17/16, and [[lem:own-wedge]] (a) gives
the values for g_b0; |g − g_b0| ≤ s_0² c/(1 − s_0 c) is (a) with the roles exchanged, at most 0.4520 at c = 7/25, and
g_b0(∂_t, ∂_t) = −1 + 𝔪 ≤ −15/16. (c) dΦ_W = dv − r⁻² dr, and with g_b0⁻¹(dv, dv) = 0, g_b0⁻¹(dv, dr) = 1,
g_b0⁻¹(dr, dr) = 1 − 𝔪, g_b0⁻¹(dΦ_W, dΦ_W) = −2r⁻² + r⁻⁴(1 − 𝔪); |dΦ_W|_E² = 1 + (1 − r⁻²)² ≤ 2, so the
perturbation adds at most r⁻².
(d) For two future timelike vectors X and n of g the form p ↦ T_g[p](X, n) is positive definite: in a g-orthonormal frame
with X a positive multiple of e_0 and n a positive multiple of cosh s e_0 + sinh s e_1 it is, up to positive factors, ½
cosh s (p_0² + p_1²) + sinh s p_0 p_1 + ½ cosh s Σ_(i≥2) p_i², with eigenvalues ½e^(±s) and ½ cosh s. By (a) and (b) with
c = 0.0232, ∂_t and −∇t̃ are future timelike with margins, and (g, f′, x̂) range over a compact set; so the form is
bounded above and below by positive multiples of |p|_E², and √|det g| lies between positive constants (det g_b0 = −1).
(e) g_b0⁻¹(du, du) = −1 − 𝔪 − 2𝔪 + 1 − 𝔪 = −4𝔪 and |du|_E² = 2; by (a), |g⁻¹ − g_b0⁻¹| ≤ 0.59 𝔪 for |H| ≤ 𝔪/2, so g⁻¹(du,
du) ≤ −2.8𝔪 < 0, and g(−∇u, ∂_t) = −du(∂_t) = −1 < 0. w′ = −2a(u* − u)^(2a−1) < 0, so ∇w = |w′|(−∇u), and the
energy-momentum tensor is nonnegative on pairs of future causal vectors. ∎

**Lemma {#lem:own-energy-identity}** (the energy identity). For every metric g, every function φ and X = w(u)∂_t,

    ∇_a(T_g[φ]^a_b X^b) = (□_g φ) Xφ + T_g[φ](∇w, ∂_t) + ½ w T_g[φ]^(ab) ∂_t g_ab,
                                                                                                {#eq:own-energy-identity}

and g^(ab)∂_a∂_b φ = □_g φ + g^(ab) Γ[g]^c_ab ∂_c φ.

*Proof.* ∇_a T^a_b = (□_g φ) ∂_b φ, and T^(ab)∇_a X_b = ½ T^(ab)(ℒ_X g)_ab with (ℒ_(w∂_t) g)_ab = w ∂_t g_ab + ∂_a w
g_(tb) + ∂_b w g_(at). The second formula is the definition of □_g in coordinates. ∎

**Lemma {#lem:own-rays}** (estimates along the rays of Σ̃_σ). Let σ ≤ 0. Along a ray r ↦ (f(r) + σ, r x̂) of Σ̃_σ,
d/dr = x̂·∂_x + f′ ∂_t.
(a) For every function ψ and every c, ∂_i ψ = r⁻¹ x̂_i (Zψ − (t − v1)∂_t ψ) − r⁻² x_j Ω_ij ψ, and

    d/dr (∂_c ψ) = r⁻¹ ∂_c(Zψ) − r⁻¹(t − v1) ∂_c(∂_t ψ) + f′ ∂_c(∂_t ψ) − r⁻¹ ∂_c ψ.
                                                                                                 {#eq:own-ray-derivative}

So on W (|t − v1| ≤ r, [[lem:own-wedge]] (b)) every second derivative of ψ, and the r-derivative along the ray of
every first derivative, are combinations with coefficients bounded by 1 + 4/r of first derivatives of Γψ, Γ ∈ {∂_t, Z,
Ω}, and of r⁻¹ ∂ψ.
(b) If F := Ω^γ ∂ψ satisfies ∫_(S³) ∫_(r_σ)^∞ r^(2a+3) (|F|² + |dF/dr|²) dr dω < ∞, then for R′ ≥ r_σ

    ∫_(S³) R′^(2a+3) |F(R′, ω)|² dω ≤ 2 ‖r^(a+3/2) F‖ ‖r^(a+3/2) dF/dr‖,                                     {#eq:own-s1}

the norms in L²([R′, ∞) × S³, dr dω).
(c) If φ → 0 at spatial infinity along the rays and ∫^∞ r^(2a+3)(dφ/dr)² dr < ∞, then

    ∫_(r_σ)^∞ r^(2a+1) φ² dr ≤ (a + 1)⁻² ∫_(r_σ)^∞ r^(2a+3) (dφ/dr)² dr,
    r^(2a+2) φ(r)² ≤ (2a + 2)⁻¹ ∫_r^∞ s^(2a+3) (dφ/ds)² ds.                                         {#eq:own-hardy}

*Proof.* (a) x_j Ω_ij = x_i (x·∂) − r² ∂_i and x·∂ = Z − (t − v1)∂_t; and Z∂_c = ∂_c Z − ∂_c, as [Z, ∂_c] = −∂_c.
(b) On [R′, R″], R′^(2a+3)𝐅(R′)² = R″^(2a+3)𝐅(R″)² − ∫ ((2a + 3) r^(2a+2) 𝐅² + r^(2a+3) d(𝐅²)/dr) dr, with
𝐅(r)² := ∫_(S³) |F(r, ω)|² dω; drop the nonpositive term and use Cauchy–Schwarz. Since ∫ r^(2a+3) 𝐅² dr < ∞,
lim inf r^(2a+4) 𝐅(r)² = 0, and R″ → ∞ along such a sequence removes the boundary term. (c) The second inequality is
φ(r) = −∫_r^∞ dφ/ds ds and Cauchy–Schwarz; so the boundary term r^(2a+2)φ²/(2a + 2) of the integration by parts
∫ r^(2a+1) φ² = [r^(2a+2) φ²/(2a + 2)] − (a + 1)⁻¹ ∫ r^(2a+2) φ φ′ vanishes at infinity, the one at r_σ has the good
sign, and Cauchy–Schwarz gives the first. ∎

With [[lem:own-margins]] (d), these three tools bound the error terms of the energy identity ([[cor:far-kernels]]
below).

**Definition {#def:cutoff-truncation}** (the truncated problems). Let J ≥ 2k1 + 7 be an integer, and let λ be below
the threshold of [[prop:far-residual]]. Extend f from [4R, ∞) to a smooth function F̂ on [a′, ∞) with derivative at
most ¼ in modulus and |F̂| ≤ C_f. For T ≤ −1 put 𝒮_T := {τ = T + F̂(|x|), |x| ≥ a′}, which is {t̃ = T} on r ≥ 4R,
δ_0 := V′_P − κ_P − v1 (≥ 4 by [[lem:interior-far-part]] (ii)), V_T := V′_P − δ_0/2 − h_P(T − C_f), and let χ_T(v) be
smooth, 0 for v ≤ V_T and 1 for v ≥ V_T + δ_0/4, with derivatives bounded independently of T. Put

    𝔤_T := (1 − χ_T) g_λ + χ_T (g_b0 + Σ + Σ′_J),                                                      {#eq:cutoff-data}

defined where g_λ is defined or χ_T = 1. The *truncated problem* is the Cauchy problem for Ric^H(g) = 0 relative to g0
with data (g, ∂_τ g) on 𝒮_T equal to those of 𝔤_T; its solution is written g_T, or g_T^(J) when J is to be shown. (Σ is
defined on {v ≥ v1} and Σ′_J on {r > 0}; {v ≥ v1} contains the support of χ_T, as V_T ≥ v1 + δ_0/2.)

**Lemma {#lem:own-truncation}** (the truncated problems). There is T_0, depending on λ and J, such that for T ≤ T_0:
(i) 𝒮_T ∩ {v ≤ V_T + δ_0/4} ⊂ P′, so the data are defined; 𝒮_T is spacelike for g0 and g_λ; and r_T ≥ r_3, so that
the bound |Σ| + |Σ′_J| ≤ 1/100 holds on W ∩ {r ≥ r_T}, which contains Σ̃_T ([[lem:own-wedge]] (b),
[[lem:cutoff-extension]] (c)).
(ii) Every past g_λ-causal curve from a point p ∈ (P′ ∪ Ω′) ∩ {v ≤ v1, τ − F̂(|x|) ≥ T} stays in P′ ∪ Ω′ and meets 𝒮_T at
a point with v ≤ V_T. Hence the solution g_T of the truncated problem equals g_λ on (P′ ∪ Ω′) ∩ {v ≤ v1, τ − F̂ ≥ T}, and
ℋ ∩ {t̃ ≥ T} carries the data of g_λ: no characteristic problem is posed.
(iii) Let k ≥ 0 and h_R := g_T − g_b0 − Σ. On Σ̃_T, for |α| ≤ k,

    |Γ^α h_R| ≤ C (r⁻⁴ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),     |∂Γ^α h_R| ≤ C (r⁻⁵ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),
                                                                                         {#eq:cutoff-cap-general}

with C depending on λ, J and k but not on T, where 𝒮^♭_T := Σ̃_T ∩ {v ≤ V_T + δ_0/4}. If J ≥ 2k + 7,
then |Γ^α h_R| ≤ C r⁻⁴ and |∂Γ^α h_R| ≤ C r⁻⁵ on all of Σ̃_T, and for 0 < a < 3

    E_T[Γ^α h_R] ≤ C |T|^(2a−6)  (|α| ≤ k),     𝔈_k(T) ≤ C |T|^(2a−6).                                   {#eq:cutoff-cap}

On Σ̃_T ∩ {v ≤ V_T}, h_R and all its derivatives are those of g_λ − g_b0 − Σ; on Σ̃_T ∩ {v ≥ V_T + δ_0/4}, h_R = Σ′_J
and ∂_t h_R = ∂_t Σ′_J, and |∂^β (h_R − Σ′_J)| ≤ C r^(−4−|β|) for |β| ≥ 2.
(iv) g_T exists on W_T ∩ {t̃ ≤ T + δ_T} for some δ_T > 0, with every derivative bounded, and on any W_T ∩ {t̃ ≤ σ′} on
which its derivatives up to a fixed order stay bounded and the margins of [[lem:own-margins]] (b) hold, it continues
beyond σ′. g_T is G-invariant.

*Proof.* (i) On 𝒮_T, τ ≤ T + C_f ≤ τ0 and, where v ≤ V_T + δ_0/4, v + h_P(τ) ≤ V′_P − δ_0/4 + h_P(T + C_f) − h_P(T −
C_f), which is at most V′_P once h_P(T + C_f) − h_P(T − C_f) ≤ 2C_f sup h_P′ ≤ δ_0/4, true for T ≤ T_0. Spacelike: for
g0, g0⁻¹(dτ − F̂′ dr, ·) = −1 + F̂′² − (μ/r²)(1 + F̂′)² < 0 as in [[lem:interior-far-part]] (i); for g_λ, by the margin
of [[lem:past-domain]] (f). Finally r_T ≥ c_W (1 + |T|) ([[lem:own-wedge]] (b)), which is at least r_3 for T ≤ T_0.
(ii) On Ω′, Φ_Ω := v + ε_Ω(τ − τ0), with ε_Ω(τ′_end − τ0) < δ_0/2, is a time function for g0
with g0⁻¹(dΦ_Ω, dΦ_Ω) = −2ε_Ω − ε_Ω²(1 + 𝔪) < 0 ([[prop:vaidya]] (d)), and for g_λ, |g_λ − g0| ≤ C λ on the compact Ω′,
for λ small; on P′, Φ_P := v + h_P(τ) is a time function for g_λ ([[lem:past-domain]] (b), (f)). A past causal curve
leaves neither Ω′ (its boundaries other than Σ_τ0 are spacelike with Ω′ to their past, [[lem:domain]] (e)) nor P′ (its
outer boundary is spacelike with P′ to its past and r increases along past causal curves at r = a′), and τ → −∞ along a
past-inextendible one in P′, since P′ ∩ {τ ≥ τ1} is compact; as F̂ is bounded, it meets 𝒮_T. Along it, from p with
v(p) ≤ v1: on Ω′, Φ_Ω ≤ v1 + ε_Ω(τ′_end − τ0) < v1 + δ_0/2, so it enters P′ at τ0 with v < v1 + δ_0/2; on P′,
Φ_P ≤ v1 + δ_0/2 + κ_P = V′_P − δ_0/2; at its point q on 𝒮_T, τ(q) ≥ T − C_f, h_P is increasing, and
v(q) ≤ V′_P − δ_0/2 − h_P(T − C_f) = V_T. So p lies in the domain of dependence of 𝒮_T ∩ {v ≤ V_T}, where the data are
those of g_λ, and the uniqueness of the local theory on domains of dependence (Step 8 of the proof of
[[thm:uniform-existence]]) gives g_T = g_λ there. ℋ ⊂ Ω′ ∪ P′ by [[lem:interior-far-part]] (ii). (iv) Beyond the band
the data g_b0 + Σ + Σ′_J are smooth with every derivative bounded ([[lem:own-sigma-data]] (b) and [[eq:far-sigma-bounds]]
at fixed λ, [[lem:cutoff-extension]] (a)), and so are the data of g_λ on the bounded set 𝒮_T ∩ {v ≤ V_T + δ_0/4}; so the
local theory of Step 8 of the proof of [[thm:uniform-existence]], applied on the balls of a fixed radius, gives
solutions on a time interval independent of the ball, which agree on overlaps by finite speed of propagation; the
continuation criterion is that of the same local theory. The data are G-invariant (g_λ, Σ ([[lem:own-sigma-data]] (c)),
Σ′_J ([[lem:cutoff-extension]] (a)), χ_T(v) and F̂(|x|) are), G acts by isometries of g0, and Ric^H is natural
([[lem:far-naturality]]); uniqueness gives the invariance of g_T. Item (iii) is proved after [[lem:cutoff-jets]]
below. ∎

Near Σ̃_T put

    H_0 := Σ + Σ′_J,     𝔐 := (1 − χ_T) m_J  (𝔐 := 0 where χ_T = 1),     H_D := 𝔤_T − g_b0 = H_0 + 𝔐,     {#eq:cutoff-hd}

the identity on 𝒮^♭_T being 𝔤_T − g_b0 = Σ + Σ′_J + (1 − χ_T)(g_λ − g_b0 − Σ − Σ′_J). 𝒮^♭_T is the part of the initial
slice from ℋ to the outer edge of the band; it is {r_T ≤ r ≤ r_T + d_V} along the rays of Σ̃_T (v increases along them
with dv/dr ≥ 1, [[lem:own-wedge]] (b)), and r_T ≥ c_W (1 + |T|). Let δ := g_T − 𝔤_T, defined on W_T ∩ {t̃ ≤ T + δ_T}
near Σ̃_T, and wherever χ_T = 1. Then h_R = g_T − g_b0 − Σ = Σ′_J + 𝔐 + δ there.

**Definition {#def:cutoff-classes}** (two classes on the initial slice). Let N_∂ be an integer and q ∈ ℝ. A family of
functions F, each defined on a neighbourhood of Σ̃_T in {t̃ ≥ T} and depending on T ≤ T_0, belongs to
𝒯^q if |∂^β F| ≤ C r^(−q−|β|) on Σ̃_T for |β| ≤ N_∂, and to ℬ^q if |∂^β F| ≤ C r^(−q) on Σ̃_T for |β| ≤ N_∂ and
∂^β F = 0 on Σ̃_T ∖ 𝒮^♭_T; here ∂^β are Cartesian derivatives in (t, x) and C does not depend on T. 𝒪 is the class of F
with |∂^β F| ≤ C on Σ̃_T for |β| ≤ N_∂.

**Lemma {#lem:cutoff-classes}** (the calculus of the classes). (a) 𝒯^q ⊂ 𝒯^(q′) and ℬ^q ⊂ ℬ^(q′) for q ≥ q′;
𝒯^(q1) 𝒯^(q2) ⊂ 𝒯^(q1+q2), 𝒯^(q1) ℬ^(q2) ⊂ ℬ^(q1+q2) and ℬ^(q1) ℬ^(q2) ⊂ ℬ^(q1+q2); 𝒪 ℬ^q ⊂ ℬ^q; and 𝒯^q, ℬ^q ⊂ 𝒪 for
q ≥ 0. (b) ∂ maps 𝒯^q into 𝒯^(q+1) and ℬ^q into ℬ^q, with N_∂ lowered by one. (c) A field tame of order q on
W ∩ {r ≥ r_3} restricts to 𝒯^q. A family of strip order q on 𝒰_1 ∩ {v ≥ v1} whose members vanish where
v ≥ V_T + δ_0/4 belongs to ℬ^q. (d) Let Φ(X, w) be smooth in w ∈ ℝ^m, with |∂_X^β ∂_w^γ Φ| ≤ C r^(−|β|) for X near Σ̃_T
and w in a compact set, and let A_i ∈ 𝒯^0 and B_i ∈ ℬ^q (q ≥ 0) with A + θB in that compact set for θ ∈ [0, 1]. Then
Φ(X, A) ∈ 𝒯^0 and Φ(X, A + B) − Φ(X, A) ∈ ℬ^q.

*Proof.* (a) and (b) are Leibniz's rule, r ≥ 1 and the definitions. (c) For tame fields take α = 0 (Σ̃_T lies in
{r ≥ r_3} by [[lem:own-truncation]] (i)). For the strip class, the Cartesian derivatives are combinations of ∂_v, ℓ and
r⁻¹ Y_i with coefficients bounded with all their derivatives ([[eq:cutoff-cartesian]]), and ∂_v does not lower the order
while ℓ and r⁻¹ Y_i raise it; and 𝒮^♭_T ⊂ 𝒰_1 ∩ {v ≥ v1} for T ≤ T_0, since V_T + δ_0/4 ≤ V′_P − 1. (d) By the chain
rule ∂^β Φ(X, A) is a sum of products of a derivative of Φ with derivatives of the A_i whose orders add up, with the
X-derivatives of Φ, to |β|; each derivative gains r⁻¹. And Φ(X, A + B) − Φ(X, A) = Σ_i B_i ∫_0^1 ∂_(w_i) Φ(X, A + θB) dθ,
whose integrand is in 𝒪 by the chain rule, and 𝒪 ℬ^q ⊂ ℬ^q. ∎

**Lemma {#lem:cutoff-jets}** (the time derivatives at the initial slice). Let T ≤ T_0 and N_∂ ≥ 2. Then δ = ∂δ = 0 on
Σ̃_T, and for 2 ≤ |β| ≤ N_∂

    |∂^β δ| ≤ C (r^(−4−|β|) + 1_(𝒮^♭_T) r^(−(J+3)/2))   on Σ̃_T,                                       {#eq:cutoff-jets}

with C depending on λ, J and N_∂ but not on T. In the notation of [[def:cutoff-classes]], δ ∈ 𝒯^4 + ℬ^((J+3)/2) for
the derivatives of order at least 2.

*Proof.* *The forcing at the slice.* Put ℱ := P(H_D). We show ℱ ∈ 𝒯^6 + ℬ^((J+3)/2). P(H_0) is tame of order 6 on
W ∩ {r ≥ r_3} ([[lem:cutoff-extension]] (c)), so it lies in 𝒯^6 by [[lem:cutoff-classes]] (c). And ℱ − P(H_0) =
P(H_0 + 𝔐) − P(H_0) vanishes where χ_T = 1, and on 𝒮^♭_T it equals

    −½ g_𝔐^(ab) ∂_a ∂_b 𝔐 − ½ (g_𝔐^(ab) − g_0^(ab)) ∂_a ∂_b H_0 + 𝒬(X, H_0 + 𝔐, ∂H_0 + ∂𝔐) − 𝒬(X, H_0, ∂H_0),

with g_𝔐 := g_b0 + H_D, g_0 := g_b0 + H_0 and 𝒬 as in the proof of [[lem:cutoff-polynomial]]. 𝔐 is of strip order
(J + 1)/2, uniformly in T, by [[lem:cutoff-extension]] (b) and the bounds on χ_T(v). As in the proof of
[[lem:cutoff-polynomial]], g_𝔐⁻¹(dv, dv) = O(r⁻²) and every other second derivative in the first term contains ℓ, r⁻¹ Y
or an O(r⁻¹) coefficient, so the first term is of strip order (J + 3)/2; the other two contain 𝔐 or ∂𝔐 times factors of
strip order at least 2. By [[lem:cutoff-classes]] (c), ℱ − P(H_0) ∈ ℬ^((J+3)/2).

*Coordinates at the slice.* Use (y, x), y := t̃ − T, on r ≥ 4R: ∂_y = ∂_t, and ∂̃_i := ∂_i + f′ x̂_i ∂_t is tangent to
the slices, so ∂_i = ∂̃_i − f′ x̂_i ∂_y with f′ x̂_i tame of order 2 (f′ ∈ |x|⁻² C^∞). The classes may therefore be
defined with ∂_y and ∂̃_i in place of ∂_t and ∂_i. Put δ_[ν] := ∂_y^ν δ|_(y=0), functions on Σ̃_T. The Cauchy data of g_T
and 𝔤_T agree, so δ_[0] = δ_[1] = 0 and every ∂̃^γ δ_[0], ∂̃^γ δ_[1] vanishes. We show by induction on ν ≥ 2 that

    |∂̃^γ δ_[ν]| ≤ C (r^(−4−ν−|γ|) + 1_(𝒮^♭_T) r^(−(J+3)/2))   for ν + |γ| ≤ N_∂,                 {#eq:cutoff-induction}

which gives [[eq:cutoff-jets]], a Cartesian ∂^β at y = 0 being a combination of the ∂̃^γ δ_[ν], ν + |γ| ≤ |β|, with
coefficients in 𝒪 that gain r⁻¹ for each order they lack.

*The equation.* P(H_D + δ) = 0, and P(H_D + δ) − P(H_D) = −½ g_δ^(ab) ∂_a ∂_b δ + e_0 δ + e_1·∂δ, where
g_δ := g_b0 + H_D + δ = g_T and

    e_0 := ∫_0^1 [∂_H(−½ g^(ab)(H_D + θδ)) ∂_a ∂_b H_D + ∂_H 𝒬(X, H_D + θδ, ∂H_D + θ∂δ)] dθ,
    e_1 := ∫_0^1 ∂_(∂H) 𝒬(X, H_D + θδ, ∂H_D + θ∂δ) dθ.

In (y, x), g^(ab) ∂_a ∂_b = g⁻¹(dt̃, dt̃) ∂_y² + 2 g⁻¹(dt̃, dx^i) ∂_y ∂̃_i + g^(ij) ∂̃_i ∂̃_j + b^y ∂_y + b^i ∂̃_i, with
b^y, b^i built from g⁻¹ and second derivatives of f(r), tame of order 3. Apply ∂_y^ν, ν ≥ 0, and restrict to y = 0,
where δ = ∂δ = 0 and g_δ = g_D := g_b0 + H_D:

    −½ g_D⁻¹(dt̃, dt̃) δ_[ν+2] = −∂_y^ν ℱ|_(y=0) − ℛ_ν.                                         {#eq:cutoff-jet-equation}

By Leibniz's rule ℛ_ν is a finite sum of products, each with at least one factor ∂̃^γ δ_[μ], μ ≤ ν + 1, and the other
factors further such factors or y- and tangential derivatives, at y = 0, of g⁻¹(H_D), e_0, e_1, b^y, b^i at δ = 0 and of
their derivatives in δ, ∂δ. The term δ_[ν+2] occurs only on the left: the only way to place ν + 2 derivatives ∂_y on δ
is ∂_y^ν on ∂_y² δ with the undifferentiated coefficient. At δ = 0, by [[lem:cutoff-classes]] (d) applied with
A = (H_0, ∂H_0, ∂∂H_0) ∈ 𝒯^2 × 𝒯^3 × 𝒯^4 ⊂ 𝒪 and B = (𝔐, ∂𝔐, ∂∂𝔐) ∈ ℬ^((J+1)/2), the coefficients are: g⁻¹(H_D) and b
in 𝒯^0 + ℬ^((J+1)/2); e_1 in 𝒯^3 + ℬ^((J+1)/2), since ∂_(∂H) 𝒬 is linear in ∂g = μ ∂m + ∂H and in Γ̂, tame of order 3;
e_0 in 𝒯^4 + ℬ^((J+1)/2), since it is linear in ∂∂g, quadratic in ∂g and Γ̂, or contains ∂Γ̂, tame of order 4. Each y-
or tangential derivative of a coefficient raises the order of its 𝒯-part by one and keeps its ℬ-part.

*The count.* Suppose [[eq:cutoff-induction]] for 2 ≤ μ ≤ ν + 1. In ∂_y^ν of g_δ^(ab) ∂_a ∂_b δ the derivatives on δ and
on the coefficients number ν + 2 in total; in ∂_y^ν (e_1·∂δ) they number ν + 1 and e_1 brings the order 3; in
∂_y^ν (e_0 δ) they number ν and e_0 brings 4; a factor ∂̃^γ δ_[μ] counts μ + |γ| and has 𝒯-order 4 + μ + |γ|. So the
𝒯-part of each product of ℛ_ν is at most C r^(−4−(ν+2)), every further factor δ only lowering it. A product with a
ℬ-factor has either a factor ∂̃^γ δ_[μ] in ℬ^((J+3)/2) and the others in 𝒪, or a coefficient in ℬ^((J+1)/2) and a factor
∂̃^γ δ_[μ] with μ ≥ 2 in 𝒯^6 + ℬ^((J+3)/2); in both cases it is at most C r^(−(J+3)/2) and vanishes off 𝒮^♭_T. Also
∂_y^ν ℱ|_(y=0) ∈ 𝒯^(6+ν) + ℬ^((J+3)/2). Finally g_D⁻¹(dt̃, dt̃) ≤ −0.64 by [[lem:own-margins]] (b),
since |g_D⁻¹ − g_b0⁻¹| ≤ 0.0232 on Σ̃_T by [[lem:own-margins]] (a), as |H_D| ≤ |H_0| + |𝔐| ≤ 1/50 there for T ≤ T_0
([[lem:own-truncation]] (i)); and 1/g_D⁻¹(dt̃, dt̃) ∈ 𝒯^0 + ℬ^((J+1)/2) by [[lem:cutoff-classes]] (d). So
[[eq:cutoff-jet-equation]] gives [[eq:cutoff-induction]] for δ_[ν+2] at γ = 0; applying ∂̃^γ to
[[eq:cutoff-jet-equation]], which holds on Σ̃_T, and counting in the same way gives it for every γ. ∎

*Proof of [[lem:own-truncation]] (iii).* By [[eq:cutoff-hd]], h_R = Σ′_J + 𝔐 + δ near Σ̃_T. Each Γ is ∂_t, L_Ω_ab or
Z = (t − v1) ∂_t + x^i ∂_i, and on Cartesian components L_Ω_ab is Ω_ab = x_a ∂_b − x_b ∂_a plus a constant matrix acting
on the components. So, by induction on |α|,

    Γ^α = Σ_(|β|≤|α|) c_(α,β) ∂^β,     |∂^i c_(α,β)| ≤ C r^(|β|−i) on W (i ≤ |β|),     ∂^i c_(α,β) = 0 (i > |β|),
                                                                                         {#eq:own-gamma-cartesian}

with c_(α,β) a matrix of polynomials in (t − v1, x) of degree at most |β|: Γ(c ∂^β) = (Γc) ∂^β + c Γ∂^β; ∂_t lowers
the degree of c, and Ω_ab and Z do not raise it (Z is the Euler field of (t − v1, x)); and Γ∂^β is ∂_t ∂^β, or
x_a ∂_b ∂^β − x_b ∂_a ∂^β plus a constant matrix times ∂^β, or (t − v1) ∂_t ∂^β + x^i ∂_i ∂^β, which raise the order and
the degree by one together or keep both. On W, |t − v1| ≤ r ([[lem:own-wedge]] (b)), |x| = r and r ≥ 1, which gives the
bounds. By [[lem:cutoff-extension]] (a), |Γ^α Σ′_J| ≤ C r⁻⁴ and |∂Γ^α Σ′_J| ≤ C r⁻⁵. In (v, r, x̂), ∂_t = ∂_v and
Z = (v − v1) ∂_v + r ℓ, with 0 ≤ v − v1 ≤ d_V on 𝒮^♭_T; so Γ^α 𝔐 is of strip order (J + 1)/2
and |Γ^α 𝔐| + |∂Γ^α 𝔐| ≤ C r^(−(J+1)/2) ≤ C r⁻⁵, as J ≥ 9; and 𝔐 vanishes off 𝒮^♭_T. By [[lem:cutoff-jets]] with
N_∂ := max(2, k + 1), since δ and ∂δ vanish on Σ̃_T,

    |Γ^α δ| ≤ C Σ_(2≤|β|≤|α|) r^(|β|) (r^(−4−|β|) + 1_(𝒮^♭_T) r^(−(J+3)/2)) ≤ C (r⁻⁴ + 1_(𝒮^♭_T) r^(|α|−(J+3)/2)),

and ∂Γ^α δ = Σ_β ((∂c_(α,β)) ∂^β δ + c_(α,β) ∂∂^β δ) gives the bound with r⁻⁵. This is [[eq:cutoff-cap-general]]. If
J ≥ 2k + 7, then r^(|α|−(J+3)/2) ≤ r⁻⁵ for |α| ≤ k. On Σ̃_T, g_T − g_b0 = H_D and |H_D| ≤ 1/50 for T ≤ T_0, so by
[[lem:own-margins]] (d) and w ≤ C r^(2a), E_T[φ] ≤ C ∫_(Σ̃_T) r^(2a) |∂φ|² d⁴x; with d⁴x = r³ dr dω along the rays,
E_T[Γ^α h_R] ≤ C ∫_(r_T)^∞ r^(2a−10+3) dr = C r_T^(2a−6)/(6 − 2a) ≤ C |T|^(2a−6), as r_T ≥ c_W (1 + |T|). The last
statement: on Σ̃_T ∩ {v ≤ V_T}, χ_T = 0 and 𝔤_T = g_λ, δ and ∂δ vanish, and near the points of Σ̃_T with v < V_T,
ℱ = P(g_λ − g_b0) = 0 (g_λ is vacuum in the wave-map gauge, [[thm:past-construction]]), so [[eq:cutoff-jet-equation]]
gives by induction δ_[ν] = 0 there for every ν, and by continuity on {v ≤ V_T}; on Σ̃_T ∩ {v ≥ V_T + δ_0/4}, χ_T = 1 and
𝔐 = 0, δ and ∂δ vanish, and [[eq:cutoff-jets]] holds without the strip term. ∎

**Remark {#rem:cutoff-growth}** (the order of the matching). The condition J ≥ 2k + 7 is what the commuted fields need.
If the data beyond the band were those of g_b0 + Σ, that is with Σ′_J replaced by 0, the mismatch on the band would be
(1 − χ_T) h_λ, h_λ := g_λ − g_b0 − Σ, of strip order 9/2 only: by [[lem:cutoff-polynomial]] the coefficient of r^(−9/2)
of h_λ is G_(9,0), of weight −9/2 and constant in v, and the rest is of strip order 5. Since P(Σ + h_λ) = 0, the forcing
at the slice is ℱ = P(Σ + h_λ − χ_T h_λ) = χ_T′(v)(ℓ + 3/(2r)) h_λ + O(r⁻⁶) = −3 χ_T′(v) r^(−11/2) G_(9,0) + O(r⁻⁶) on
the band, and by [[eq:cutoff-jet-equation]] δ_[2] = 2ℱ/g_D⁻¹(dt̃, dt̃) and
δ_[3] = −6 χ_T″(v) r^(−11/2) G_(9,0)/g_D⁻¹(dt̃, dt̃) + O(r⁻⁶): a derivative ∂_y falls on χ_T without gain. In (y, r, x̂),
Z = (y + T + β_f) ∂_y + r ∂_r with ∂_r at fixed (y, x̂) and β_f := f − v1 − r f′ bounded, and ∂_r v = 1 + f′ there. So
at y = 0, ∂_y Z² δ = ((T + β_f)² + 2 (T + β_f) r (1 + f′)) δ_[3] + O(|T| r^(−11/2) + T² r⁻⁶), and the bracket is
−T² + O(|T|) on the band, where r = |T| + O(1). Hence |∂_y Z² h_R| ≥ c T² r^(−11/2) where |χ_T″| and |G_(9,0)| are
bounded below, and E_T[Z² h_R] ≥ c |T|^(2a−4) when G_(9,0) ≢ 0, which is unbounded as T → −∞ for every a > 2; with k
factors Z the order is |T|^(2a+2k−8). In general a mismatch of strip order q gives E_T[Γ^α h_R] up to
C |T|^(2a+2|α|−2q+1), and [[lem:own-truncation]] (iii) uses q = (J + 1)/2.

Let σ_1(T) be the supremum of the σ ≤ 0 such that g_T exists on W_T ∩ {t̃ ≤ σ} with every derivative bounded there.

**Lemma {#lem:own-exterior}** (finite and continuous energies). Let T ≤ T_0 and σ′ ∈ [T, 0], and suppose that g_T
exists and is smooth on W_T ∩ {t̃ ≤ σ′} (for instance σ′ < σ_1(T)) and that |g_T⁻¹ − g_b0⁻¹| ≤ c < 7/25 on
W_T ∩ {t̃ ≤ σ′} ∩ {r ≥ ϱ_0}, where ϱ_0 := max(4R, V_T + δ_0 − T + C_f). Let k ≥ 0 and h_R := g_T − g_b0 − Σ on
W_T ∩ {t̃ ≤ σ′}. There is C, depending on T, σ′, k, λ, J and c, such that:
(a) |∂^j Γ^γ h_R| ≤ C r^(−7/2−j) on W_T ∩ {t̃ ≤ σ′} for j + |γ| ≤ k;
(b) for σ ∈ [T, σ′], |α| ≤ k and ϱ ≥ 4R,

    ∫_(Σ̃_σ ∩ {r≥ϱ}) r^(2a) (|∂∂Γ^α h_R|² + |∂Γ^α h_R|² + r⁻² |Γ^α h_R|²) d⁴x ≤ C ϱ^(2a−6);          {#eq:own-ext-tail}

(c) 𝔈_k is finite and continuous on [T, σ′], and for σ ∈ [T, σ′], |α| ≤ k and ϱ ≥ 4R the weighted energy of Γ^α h_R
on Σ̃_σ ∩ {r ≥ ϱ} is at most C ϱ^(2a−6).

*Proof.* Put 𝒲 := W_T ∩ {t̃ ≤ σ′}. For every ϱ′ the set 𝒲 ∩ {r ≤ ϱ′} is compact and g_T is smooth on it, so every
derivative of h_R is bounded there by a constant depending on ϱ′; the work is the estimate as r → ∞. Fix the integer
k_+ := k + 6. Constants C below depend on T, σ′, k, λ, J and c, and are independent of the radii ϱ and V_* introduced
below unless said otherwise.

*Step 1 (the exterior domains and the energy inequality).* For ϱ ≥ ϱ_0 and V_* > ϱ + 4(σ′ − T) + 2 put

    X_(ϱ,V_*) := W ∩ {T ≤ t̃ ≤ σ′} ∩ {r − 2(t̃ − T) ≥ ϱ} ∩ {r + 2(t̃ − T) ≤ V_*},
    A_σ(ϱ, V_*) := Σ̃_σ ∩ {ϱ + 2(σ − T) ≤ r ≤ V_* − 2(σ − T)}   (σ ∈ [T, σ′]),

so that A_σ(ϱ, V_*) is the slice of X_(ϱ,V_*) at t̃ = σ; its r-range has length at least 2 and shrinks as σ increases.
X_(ϱ,V_*) is compact, as r ≤ V_* on it, and lies in 𝒲 ∩ {r ≥ ϱ_0}. On it v = t̃ + f(r) + r ≥ T − C_f + ϱ_0 ≥ V_T + δ_0,
so χ_T = 1 there: X_(ϱ,V_*) lies beyond the band, and 𝔤_T = g_b0 + Σ + Σ′_J on it. By [[lem:own-margins]] (b) the two
lateral boundary pieces of X_(ϱ,V_*), on {r − 2t̃ = ϱ − 2T} and on {r + 2t̃ = V_* + 2T}, are spacelike for g_T with
X_(ϱ,V_*) to their past, as r − 2t̃ decreases and r + 2t̃ increases along future causal curves; and ∂_t and −∇t̃ are
future timelike for g_T on 𝒲 ∩ {r ≥ ϱ_0} with margins depending on c only. As in the proof of [[lem:own-margins]] (d),
(g_T, f′, x̂) ranges there over a compact set on which these margins hold, so there are c_1, c_2 > 0 depending on c with

    c_1 w |∂φ|² ≤ √|g_T| T_(g_T)[φ](w ∂_t, −∇t̃) ≤ c_2 w |∂φ|²                                   {#eq:own-ext-density}

for every function φ and every function w > 0 on 𝒲 ∩ {r ≥ ϱ_0}. The identity [[eq:own-energy-identity]] holds, with
the same proof, for X = w ∂_t and any smooth w > 0. Integrate it, for w := r^(2p), p ≥ 0, over X_(ϱ,V_*) ∩ {t̃ ≤ σ},
whose boundary consists of A_σ(ϱ, V_*), A_T(ϱ, V_*) and the two lateral pieces; drop the fluxes through the lateral
pieces, which are nonnegative (T_(g_T)[φ](w ∂_t, n) ≥ 0 for n future causal); and use d⁵x = dt̃ d⁴x, the
bound |∇(r^(2p))| ≤ C p r^(2p−1) ≤ C p r^(2p), |T_(g_T)[φ](V, ∂_t)| ≤ C |V| |∂φ|² and |T_(g_T)[φ]^(ab) ∂_t g_ab| ≤
C |∂g_T| |∂φ|², C depending on c. With A_σ := A_σ(ϱ, V_*) this gives

    c_1 ∫_(A_σ) r^(2p) |∂φ|² d⁴x ≤ c_2 ∫_(A_T) r^(2p) |∂φ|² d⁴x
          + C ∫_T^σ ∫_(A_σ″) r^(2p) (|□_(g_T) φ| |∂φ| + (p + |∂g_T|) |∂φ|²) d⁴x dσ″.                 {#eq:own-ext-energy}

For a smooth ψ on X_(ϱ,V_*) and T ≤ σ_a ≤ σ_b ≤ σ′,

    ∫_(A_(σ_b)) r^(2p−2) |ψ|² d⁴x ≤ ∫_(A_(σ_a)) r^(2p−2) |ψ|² d⁴x
          + ∫_(σ_a)^(σ_b) ∫_(A_σ″) r^(2p−2) (|ψ|² + |∂_t ψ|²) d⁴x dσ″:                                 {#eq:own-ext-l2}

for x in the r-range of A_(σ_b), the segment {(f(|x|) + σ″, x) : σ_a ≤ σ″ ≤ σ_b} lies in X_(ϱ,V_*), as
r − 2(σ″ − T) ≥ r − 2(σ_b − T) and r + 2(σ″ − T) ≤ V_*; along it ∂_(σ″) |ψ|² = 2ψ·∂_t ψ ≤ |ψ|² + |∂_t ψ|²; and the
r-range of A_(σ_b) lies in that of every A_σ″, σ″ ≤ σ_b.

*Step 2 (the equation of δ).* On 𝒲 ∩ {r ≥ ϱ_0} we have χ_T = 1, so 𝔤_T = g_b0 + H_0, H_0 = Σ + Σ′_J, and
δ = g_T − 𝔤_T, with h_R = Σ′_J + δ there ([[eq:cutoff-hd]]). As ϱ_0 ≥ v1 − T + C_f ≥ r_T, |H_0| ≤ 1/100 there
([[lem:own-truncation]] (i)), so |𝔤_T⁻¹| ≤ C by [[lem:own-margins]] (a); |g_T| and |g_T⁻¹| are bounded by the hypothesis
and [[lem:own-margins]] (b); so |δ| ≤ C. At fixed λ, |∂^i 𝔤_T| ≤ C r^(−2−i) for i ≥ 1 (μ m is homogeneous of degree −2,
Σ is tame of order 2 by [[eq:far-sigma-bounds]], Σ′_J tame of order 4 by [[lem:cutoff-extension]] (a)), and
F := P(H_0) satisfies |∂^β F| ≤ C r^(−6−|β|) ([[lem:cutoff-extension]] (c)). Since P(g_T − g_b0) = 0, subtracting
P(H_0) = F in the form [[eq:own-p-split]] gives, in Cartesian components,

    g_T^(ab) ∂_a ∂_b δ = 2F + 𝒩,
    𝒩 := −(g_T^(ab) − 𝔤_T^(ab)) ∂_a ∂_b 𝔤_T + 2 (Q(g_T)(∂g_T, ∂g_T) − Q(𝔤_T)(∂𝔤_T, ∂𝔤_T)).
                                                                                         {#eq:own-ext-delta}

Here g_T⁻¹ − 𝔤_T⁻¹ = −g_T⁻¹ δ 𝔤_T⁻¹; a polynomial in (g_T, g_T⁻¹) minus the same polynomial in (𝔤_T, 𝔤_T⁻¹) is, by
telescoping, a sum of products each containing one factor δ or g_T⁻¹ δ 𝔤_T⁻¹; and ∂g_T − ∂𝔤_T = ∂δ. So 𝒩 is a finite
sum of products of components of g_T^(±1), 𝔤_T^(±1) and δ with factors from {∂𝔤_T, ∂∂𝔤_T, Γ̂, ∂Γ̂, ∂δ}, in which the
derivatives number exactly two (Γ̂ counting one, ∂Γ̂ and ∂∂𝔤_T two), at least one factor is δ or ∂δ, and no second
derivative of δ occurs. For a multi-index β of Cartesian derivatives with |β| ≤ k_+, apply ∂^β to [[eq:own-ext-delta]]:
∂^β(g_T^(ab) ∂_a ∂_b δ) − g_T^(ab) ∂_a ∂_b ∂^β δ = Σ_(0<β′≤β) (β choose β′) (∂^(β′) g_T^(ab)) ∂_a ∂_b ∂^(β−β′) δ, and
∂^(β′) (g_T⁻¹) is a sum of products of g_T⁻¹ with factors ∂^(β_i) g_T = ∂^(β_i) 𝔤_T + ∂^(β_i) δ, Σ_i β_i = β′, and
every |β_i| ≥ 1. Hence

    g_T^(ab) ∂_a ∂_b ∂^β δ = 2 ∂^β F + ℛ_β,                                                  {#eq:own-ext-derivatives}

where ℛ_β is a finite sum of products of components of g_T^(±1), 𝔤_T^(±1) and δ with factors ∂^i 𝔤_T (i ≥ 1), ∂^i Γ̂
(counting i + 1) and ∂^i δ (i ≥ 1), in which the derivatives number exactly |β| + 2, at least one factor is δ or a
derivative of δ, and every derivative of δ has order at most |β| + 1.

*Step 3 (weighted energies under a pointwise bound).* Let K ≥ 1, ϱ_1 ≥ max(ϱ_0, 2 + 4(σ′ − T)),
V_* > ϱ_1 + 4(σ′ − T) + 2 and σ ∈ [T, σ′], and suppose

    |∂^i δ| ≤ K r^(−i)   on X_(ϱ_1,V_*) ∩ {t̃ ≤ σ}   for 1 ≤ i ≤ k_+ − 2,                               {#eq:own-ext-pg}

∂^i δ standing for the array of all Cartesian derivatives of order i. For ϱ ≥ ϱ_1 and σ″ ∈ [T, σ] put

    𝒥(σ″; ϱ, V_*) := Σ_(|β|≤k_+) ∫_(A_σ″(ϱ,V_*)) r^(2(a+|β|)) (|∂∂^β δ|² + r⁻² |∂^β δ|²) d⁴x.

In a product of ℛ_β let ∂^(i_0) δ (i_0 ≥ 0, ∂^0 δ := δ) be a factor of δ of largest order. Every other factor of δ has
order at most min(i_0, |β| + 2 − i_0) ≤ (k_+ + 2)/2 ≤ k_+ − 2, as k_+ ≥ 6. By [[eq:own-ext-pg]], the bounds of Step 2 on
𝔤_T and |∂^i Γ̂| ≤ C r^(−3−i) ([[eq:own-p-split]]), every other factor that carries i derivatives is at most C K r^(−i),
and these i add up to |β| + 2 − i_0; the factors without derivatives are bounded. So the product is at most
C K^(n_β) r^(−(|β|+2−i_0)) |∂^(i_0) δ|, n_β the largest number of factors, and

    ‖r^(a+|β|) ℛ_β‖_(L²(A_σ″)) ≤ C_K Σ_(i_0≤|β|+1) ‖r^(a+i_0−2) ∂^(i_0) δ‖_(L²(A_σ″))
                                ≤ C_K 𝒥(σ″; ϱ, V_*)^(1/2):                                        {#eq:own-ext-products}

for i_0 ≥ 1, ∂^(i_0) δ is a first derivative ∂∂^(β̃) δ with |β̃| = i_0 − 1 ≤ k_+, carried in 𝒥 with the weight
r^(a+i_0−1) ≥ r^(a+i_0−2); for i_0 = 0, δ is carried with the weight r^(a−1). Here C_K depends on K besides. The terms
with i_0 = 0 are those in which δ enters undifferentiated: their coefficients are O(r^(−|β|−2)), and
[[eq:own-ext-products]] rests on this decay of the coefficients of order zero.

For φ := (∂^β δ)_ij, □_(g_T) φ = g_T^(ab) ∂_a ∂_b φ − g_T^(ab) Γ[g_T]^c_(ab) ∂_c φ ([[lem:own-energy-identity]]),
and |Γ[g_T]| + |∂g_T| ≤ C (|∂𝔤_T| + |∂δ|) ≤ C K by [[eq:own-ext-pg]] at i = 1; so by [[eq:own-ext-derivatives]] and
[[eq:own-ext-products]], ‖r^(a+|β|) □_(g_T) φ‖ ≤ 2 ‖r^(a+|β|) ∂^β F‖ + C_K 𝒥^(1/2). Apply [[eq:own-ext-energy]] with
p := a + |β| to φ, and [[eq:own-ext-l2]] with p := a + |β| to ψ := ∂^β δ, using r^(2p−2) |∂_t ψ|² ≤ r^(2p) |∂∂^β δ|²,
and sum over |β| ≤ k_+ and the components. With

    f(σ‴) := Σ_(|β|≤k_+) ‖r^(a+|β|) ∂^β F‖_(L²(A_σ‴(ϱ,V_*))),

this gives 𝒥(σ″) ≤ C_K (𝒥(T) + ∫_T^(σ″) (𝒥 + f 𝒥^(1/2)) dσ‴) for σ″ ∈ [T, σ], 𝒥 being continuous in σ″. With
Y(σ″) := sup_[T,σ″] 𝒥, C_K Y^(1/2) ∫ f ≤ ½ Y + ½ C_K² (∫ f)², so Y(σ″) ≤ 2C_K 𝒥(T) + C_K² (∫_T^(σ″) f)² +
2C_K ∫_T^(σ″) Y, and Gronwall's inequality gives Y(σ″) ≤ (2C_K 𝒥(T) + C_K² (∫_T^(σ″) f)²) e^(2C_K (σ″−T)).

The data: δ = ∂δ = 0 on A_T(ϱ, V_*), and A_T(ϱ, V_*) lies off 𝒮^♭_T, so by [[lem:cutoff-jets]] with N_∂ := k_+ + 1,
the bound |∂^i δ| ≤ C r^(−4−i) holds there for 2 ≤ i ≤ k_+ + 1. Every integrand of 𝒥(T) is therefore at most
C r^(2(a+|β|)) r^(−10−2|β|), and 𝒥(T) ≤ C ∫_ϱ^∞ r^(2a−10) r³ dr = C ϱ^(2a−6)/(6 − 2a), as a < 3. And A_σ‴ ⊂ {r ≥ ϱ},
so f(σ‴)² ≤ C ∫_ϱ^∞ r^(2(a+|β|)) r^(−12−2|β|) r³ dr ≤ C ϱ^(2a−8). Hence

    𝒥(σ″; ϱ, V_*) ≤ C_K ϱ^(2a−6)   for σ″ ∈ [T, σ] and ϱ ≥ ϱ_1,                           {#eq:own-ext-weighted}

with C_K independent of ϱ, ϱ_1 and V_*.

*Step 4 (pointwise bounds).* Let σ″ ∈ [T, σ], let ψ be smooth on A_σ″(ϱ, V_*), and let I be an interval of length 1
in the r-range of A_σ″(ϱ, V_*) containing r_p ≥ 2. Parametrise each sphere {r} of A_σ″ by x̂ ∈ S³, put
G(r) := ‖ψ(r, ·)‖_(L²(S³)) and G̃(r) := ‖(d/dr) ψ(r, ·)‖_(L²(S³)), d/dr = x̂·∂_x + f′ ∂_t along the rays. For s ∈ I,
G(r_p)² = G(s)² + ∫_s^(r_p) (G²)′ with |(G²)′| ≤ 2 G G̃; averaging over s ∈ I, G(r_p)² ≤ ∫_I (G² + 2G G̃) dr ≤
2 ∫_I (G² + G̃²) dr. The fields Ω_ab are tangent to the spheres and span their tangent spaces, so they bound the norm of
W^(2,2)(S³), and [[thm:std-bh-manifold]] (with s = p = 2, sp = 4 > 3) gives
sup_(S³) |ψ(r_p, ·)|² ≤ C Σ_(|γ|≤2) ‖Ω^γ ψ(r_p, ·)‖²_(L²(S³)). On I, r ≥ r_p − 1 ≥ r_p/2, so
dr dω = r⁻³ d⁴x ≤ 8 r_p⁻³ d⁴x, and

    sup_(S³) |ψ(r_p, ·)|² ≤ C r_p⁻³ Σ_(|γ|≤2) ∫_(I×S³) (|Ω^γ ψ|² + |(d/dr) Ω^γ ψ|²) d⁴x.      {#eq:own-ext-sobolev}

By [[eq:own-gamma-cartesian]] for products of the Ω_ab, Ω^γ = Σ_(|β|≤|γ|) c_β ∂^β with |∂^i c_β| ≤ C r^(|β|−i),
and |f′| ≤ ¼; so |Ω^γ ψ| + |(d/dr) Ω^γ ψ| ≤ C Σ_(i≤2) (r^i |∂^i ψ| + r^i |∂^(i+1) ψ|) for r ≥ 1. Take ψ := ∂^(β_0) δ,
q := |β_0| ≤ k_+ − 2. On I, r_p/2 ≤ r ≤ 2r_p, and, as a + q − 1 > 0,
r^(2i) |∂^(q+i) δ|² ≤ C r_p^(−2(a+q−1)) r^(2(a+q+i−1)) |∂^(q+i) δ|² and
r^(2i) |∂^(q+i+1) δ|² ≤ C r_p^(−2(a+q)) r^(2(a+q+i)) |∂^(q+i+1) δ|²; the right sides are integrands of 𝒥 (the first
with ∂^(q+i) δ = ∂∂^(β̃) δ, |β̃| = q + i − 1, or with δ itself if q + i = 0), as q + i + 1 ≤ k_+ + 1. So, if
I ⊂ the r-range of A_σ″(ϱ, V_*),

    |∂^(β_0) δ|² ≤ C r_p^(−3−2(a+q−1)) 𝒥(σ″; ϱ, V_*) = C r_p^(−2a−2q−1) 𝒥(σ″; ϱ, V_*)   on {r = r_p}.

Let o be a point of X_(ϱ_1,V_*) with t̃(o) = σ″ ≤ σ, and put r_p := r(o) ≥ ϱ_1. If r_p − 1 ≥ ϱ_1 + 2(σ″ − T), take
ϱ := r_p − 1 − 2(σ″ − T) ≥ ϱ_1 and I := [r_p − 1, r_p], which lies in the r-range of A_σ″(ϱ, V_*) as
r_p ≤ V_* − 2(σ″ − T); then ϱ ≥ r_p/2, as r_p ≥ 2 + 4(σ′ − T). Otherwise take ϱ := ϱ_1 and I := [r_p, r_p + 1], which
lies in the r-range of A_σ″(ϱ_1, V_*) as r_p + 1 < ϱ_1 + 2(σ′ − T) + 2 < V_* − 2(σ′ − T); then
ϱ_1 > r_p − 1 − 2(σ′ − T) ≥ r_p/2. In both cases [[eq:own-ext-weighted]] gives
𝒥(σ″; ϱ, V_*) ≤ C_K 2^(6−2a) r_p^(2a−6), and so

    |∂^q δ(o)| ≤ C′_K r_p^(−q−7/2)   (q ≤ k_+ − 2),                                     {#eq:own-ext-pointwise}

C′_K depending on K besides and independent of ϱ_1 and V_*.

*Step 5 (the continuity argument).* Let C be the constant of [[lem:cutoff-jets]] with N_∂ = k_+ + 1, and take
ϱ_1 ≥ max(ϱ_0, 2 + 4(σ′ − T)) so large that C ϱ_1^(−4) ≤ ½ and C′_1 ϱ_1^(−7/2) ≤ ½, C′_1 the constant of
[[eq:own-ext-pointwise]] at K = 1. Fix V_* > ϱ_1 + 4(σ′ − T) + 2, and let 𝒮 be the set of σ ∈ [T, σ′] for which
[[eq:own-ext-pg]] holds with K = 1. On A_T(ϱ_1, V_*), ∂δ = 0 and |∂^i δ| ≤ C r^(−4−i) ≤ C ϱ_1^(−4) r^(−i) ≤ ½ r^(−i) for
i ≥ 2, so T ∈ 𝒮. 𝒮 is closed, the ∂^i δ being continuous. If σ ∈ 𝒮, Steps 3 and 4 with K = 1
give |∂^i δ| ≤ C′_1 ϱ_1^(−7/2) r^(−i) ≤ ½ r^(−i) on X_(ϱ_1,V_*) ∩ {t̃ ≤ σ}, 1 ≤ i ≤ k_+ − 2; as X_(ϱ_1,V_*) is
compact, the functions r^i ∂^i δ are uniformly continuous on it, and [[eq:own-ext-pg]] with K = 1 holds on
X_(ϱ_1,V_*) ∩ {t̃ ≤ σ + ε} for some ε > 0. So 𝒮 is open in [T, σ′], and 𝒮 = [T, σ′]. Hence [[eq:own-ext-weighted]] and
[[eq:own-ext-pointwise]] hold with K = 1 on X_(ϱ_1,V_*), with constants independent of V_*. Letting V_* → ∞ (monotone
convergence), they hold on X_(ϱ_1) := W ∩ {T ≤ t̃ ≤ σ′} ∩ {r − 2(t̃ − T) ≥ ϱ_1}, with 𝒥(σ; ϱ) the integral over
A_σ(ϱ) := Σ̃_σ ∩ {r ≥ ϱ + 2(σ − T)}:

    𝒥(σ; ϱ) ≤ C ϱ^(2a−6)  (σ ∈ [T, σ′], ϱ ≥ ϱ_1),     |∂^q δ| ≤ C r^(−q−7/2)  on X_(ϱ_1)  (q ≤ k_+ − 2).

*Step 6 (the conclusions).* (a) On X_(ϱ_1), h_R = Σ′_J + δ. By [[eq:own-gamma-cartesian]] and Leibniz's rule,
∂^j Γ^γ δ is a finite sum of terms (∂^i c_(γ,β)) ∂^(j−i) ∂^β δ with i ≤ j and |β| ≤ |γ|, each at most
C r^(|β|−i) r^(−(j−i+|β|)−7/2) = C r^(−j−7/2), as j + |β| ≤ k ≤ k_+ − 2. With [[lem:cutoff-extension]] (a) for
Σ′_J this is (a) on X_(ϱ_1). The points of 𝒲 with r ≥ ϱ_1 + 2(σ′ − T) lie in X_(ϱ_1), and on the compact set
𝒲 ∩ {r ≤ ϱ_1 + 2(σ′ − T)} the derivatives of h_R are bounded.

(b) Let ϱ_2 := ϱ_1 + 4(σ′ − T) and ϱ ≥ ϱ_2. For σ ∈ [T, σ′], Σ̃_σ ∩ {r ≥ ϱ} ⊂ A_σ(ϱ′), ϱ′ := ϱ − 2(σ − T), and
ϱ′ ≥ max(ϱ_1, ϱ/2). By [[eq:own-gamma-cartesian]],

    |Γ^α δ|² ≤ C Σ_(|β|≤|α|) r^(2|β|) |∂^β δ|²,     |∂Γ^α δ|² ≤ C Σ_(|β|≤|α|) (r^(2|β|) |∂∂^β δ|² + r^(2|β|−2) |∂^β δ|²),
    |∂∂Γ^α δ|² ≤ C Σ_(|β|≤|α|) (r^(2|β|) |∂∂∂^β δ|² + r^(2|β|−2) |∂∂^β δ|² + r^(2|β|−4) |∂^β δ|²).

Multiplied by r^(2a) (by r^(2a−2) in the first), every term is at most C times an integrand of 𝒥(σ; ϱ′), as |α| ≤ k
and k + 1 ≤ k_+ (∂∂∂^β δ = ∂∂^(β′) δ with |β′| = |β| + 1, carried with the weight r^(a+|β|+1)). So the part of the left
side of [[eq:own-ext-tail]] coming from δ is at most C 𝒥(σ; ϱ′) ≤ C ϱ′^(2a−6) ≤ C ϱ^(2a−6). For Σ′_J, by
[[lem:cutoff-extension]] (a), |∂∂Γ^α Σ′_J| + |∂Γ^α Σ′_J| + r⁻¹ |Γ^α Σ′_J| ≤ C r⁻⁵, and its part is at most
C ∫_ϱ^∞ r^(2a−10) r³ dr = C ϱ^(2a−6)/(6 − 2a). For 4R ≤ ϱ < ϱ_2 the integral over Σ̃_σ ∩ {ϱ ≤ r ≤ ϱ_2} is bounded
uniformly in σ ∈ [T, σ′], its integrand being continuous on the compact set 𝒲 ∩ {r ≤ ϱ_2}, and ϱ^(2a−6) ≥ ϱ_2^(2a−6).
This is (b).

(c) On Σ̃_σ ∩ {r ≥ ϱ_0} the energy density of φ := (Γ^α h_R)_ij is at most c_2 w |∂φ|² by [[eq:own-ext-density]], and
w ≤ C r^(2a) on W; on the compact set 𝒲 ∩ {r ≤ ϱ_0} it is bounded. So by (b) the weighted energy of Γ^α h_R on
Σ̃_σ ∩ {r ≥ ϱ} is at most C ϱ^(2a−6) for ϱ ≥ 4R. For every ϱ, 𝔈_k(σ) is the sum of the energies on Σ̃_σ ∩ {r ≤ ϱ}, each
the integral over {x : r_σ ≤ |x| ≤ ϱ} of a function continuous in (σ, x), with r_σ continuous in σ, hence continuous in
σ, and of the tails, at most C ϱ^(2a−6) uniformly in σ ∈ [T, σ′]. So 𝔈_k is finite and, as ϱ → ∞, a uniform limit of
continuous functions on [T, σ′]. ∎

*The error terms of the energy identity.* Let T ≤ σ* ≤ 0, let g = g_b0 + H be a smooth metric on W_T ∩ {t̃ ≤ σ*}
with |H| ≤ 1/50 there, h_R := H − Σ, and φ := (Γ^α h_R)_ij, |α| ≤ k1. Norms ‖·‖ are those of L²(Σ̃_σ, d⁴x), and 𝔈 :=
𝔈_k1(σ) for σ ∈ [T, σ*]. The error terms of the energy identity [[eq:own-energy-identity]] for φ on Σ̃_σ are bounded by
three tools.
(1) By [[lem:own-margins]] (d) and r^(2a) ≤ w ≤ C r^(2a) on W, 𝔈 bounds c_1 ∫_(Σ̃_σ) w |∂Γ^β h_R|² d⁴x for |β| ≤ k1. So a
first-order coefficient c with |c| ≤ c_0 r^(−q) gives ‖w^(1/2) c ∂φ‖ ≤ C c_0 r_σ^(−q) 𝔈^(1/2).
(2) Suppose that every Γ^β h_R, |β| ≤ k1, tends to 0 at spatial infinity along the rays of Σ̃_σ. The first inequality of
[[eq:own-hardy]] on almost every ray, with |dψ/dr| ≤ C |∂ψ| along the rays, integrated over S³, gives ∫_(Σ̃_σ)
r^(2a−2) |Γ^β h_R|² d⁴x ≤ C 𝔈. So a zero-order coefficient with |c| ≤ c_0 r^(−q), q ≥ 1, gives ‖w^(1/2) c φ‖ ≤ C c_0
r_σ^(−q+1) 𝔈^(1/2).
(3) A second-order coefficient with |c| ≤ c_0 r^(−q) on ∂∂ψ, ψ := Γ^β h_R, |β| ≤ k1 − 1, gives C c_0 r_σ^(−q) 𝔈^(1/2): by
[[lem:own-rays]] (a), |∂∂ψ| ≤ C Σ_Γ |∂Γψ| + C r⁻¹ |∂ψ|, the fields Γψ having order at most k1 (Ω_ab acting componentwise
differs from L_Ω_ab by a constant linear map of the components). Since r_σ ≥ c_W (1 + |σ|), a term of the energy identity
bounded by C r_σ^(−q) 𝔈^(1/2) in the norm ‖w^(1/2) ·‖, or by C r_σ^(−q) 𝔈 as an integral over Σ̃_σ, has the *kernel*
(1 + |σ|)^(−q).

**Corollary {#cor:far-kernels}** (the kernels). Let 0 < a < 4 and λ be small, and let g = g_b0 + Σ + h_R be as in the
preceding paragraph, with P(Σ + h_R) = 0, 𝔈_k1 finite on [T, σ*], every Γ^β h_R, |β| ≤ k1, tending to 0 at spatial
infinity along the rays of the slices, and, for σ ∈ [T, σ*] and r ≥ r_σ, with some ε_B ≤ 1,

    |∂ Γ^β h_R| ≤ C_S ε_B r^(−3/2−a)  (|β| ≤ k1 − 3),     |∂∂ Γ^β h_R| ≤ C_S ε_B r^(−3/2−a)  (|β| ≤ k1 − 4),
    |Γ^β h_R| ≤ C_S ε_B r^(−1/2−a)  (|β| ≤ k1 − 3).
                                                                                                      {#eq:own-pointwise}

For σ ∈ [T, σ*] and |α| ≤ k1, take in the energy identity for φ = (Γ^α h_R)_ij the equation that Γ^α h_R satisfies,
obtained by applying Π_i (Γ_i + c_(Γ_i)) to P(Σ + h_R) = 0 ([[eq:own-commuted]] in Step 2 of the proof of
[[thm:own-continuation]]). Then its error terms on Σ̃_σ are at most C κ(σ) 𝔈_k1(σ), and the residual term at most
C κ_Σ(σ) 𝔈_k1(σ)^(1/2), with

    κ(σ) := C (μ + λ)(1 + |σ|)⁻² + C ε_B (1 + |σ|)^(−1/2−a),      κ_Σ(σ) := C λ (1 + |σ|)^(a−4),       {#eq:far-kernels}

and C independent of T, σ*, λ and ε_B. Hence ∫_(−∞)^0 κ < ∞ exactly when a > 1/2, and ∫_(−∞)^0 κ_Σ < ∞ exactly when
a < 3.

*Proof.* Differentiating [[lem:far-scaling]] (a) n times in h, D^n P(H)[h_1, …, h_n] is a sum of products of bounded
coefficients with factors ∂^(j_i) h_i, ∂^j H, μ ∂^j m (j = 1, 2), Γ̂ and ∂Γ̂. In each product the derivatives number
exactly two, μ ∂m and Γ̂ being counted as one and μ ∂∂m and ∂Γ̂ as two. Differentiating [[eq:far-scaling]] in ς at
ς = 1 gives (Z + 2) P(h) = DP(h)[Z h] − 2μ ∂_μ P(h). So the commutation with Z brings in the operators (μ ∂_μ)^j,
j ≥ 1, applied to DP(H) and to the higher variations. The terms (μ ∂_μ)^j D^n P(H), n ≥ 2, have the form of D^n P(H),
with factors of the same sizes or smaller, as in the proof of [[prop:far-coefficients]] (c); they are bounded as the
terms of D^n P(H) below.

The terms linear in Γ^β h_R with every other slot a field Γ^γ Σ have coefficients O(λ r^(−4+j)) on ∂^j Γ^β h_R, since
Γ^γ Σ is O(λ r⁻²) with each derivative gaining r⁻¹ ([[eq:far-sigma-bounds]], with |γ| + 2 ≤ k1 + 2). This gives
λ r⁻² (second order, on ∂∂Γ^β h_R with |β| ≤ max(|α| − 1, 0) ≤ k1 − 1, kernel 2 by (3)), λ r⁻³ (first order, kernel 3
by (1)) and λ r⁻⁴ (zero order, kernel 3 by (2)). By [[prop:far-coefficients]] with H = Σ + h_R,
[[eq:far-sigma-bounds]] and [[eq:own-pointwise]], the other linear terms are as follows. The terms
(μ ∂_μ)^j DP(H)[Γ^β h_R], j ≥ 1, |β| < |α|, give μ r⁻² (second order, kernel 2) and smaller. B(H)·∂φ and the
first-order part of □_g give (μ + λ) r⁻³ + C ε_B r^(−3/2−a) (kernels 3 and 3/2 + a). C(H) φ gives
(μ + λ) r⁻⁴ + C ε_B r^(−3/2−a) (zero order: kernels 3 and a + 1/2). The deformation term (1/2) w T^(ab) ∂_t g_ab carries
∂_t H = O(λ r⁻³ + ε_B r^(−3/2−a)) (kernels 3 and 3/2 + a).

The terms with at least two slots h_R have commutation orders summing to at most |α| ≤ k1, and a slot that carries two
derivatives has order at most max(|α| − 1, 0) ≤ k1 − 1, since second derivatives of a field of order |α| occur only in
DP(H)[Γ^α h_R]. Put the slot of highest order in L²: through (1), through (2) if it is undifferentiated, through (3)
if it carries two derivatives. Every other slot then has order at most k1/2 ≤ k1 − 4, since k1 ≥ 8, so it lies within
[[eq:own-pointwise]]: it is at most C_S ε_B r^(−1/2−a) if undifferentiated and C_S ε_B r^(−3/2−a) otherwise. In every
distribution of the two derivatives the term is then bounded by C ε_B r_σ^(−1/2−a) 𝔈^(1/2) (kernel a + 1/2). The least
exponents are 2 for the terms of size μ + λ and a + 1/2 for those of size ε_B, which is κ.

The residual: by [[prop:far-residual]], |Π_i (Γ_i + c_i) P(Σ)| ≤ C λ r⁻⁶ with C independent of λ, as |α| ≤ k1, and
w ≤ C r^(2a) on W, so

    ‖w^(1/2) Π_i (Γ_i + c_i) P(Σ)‖² ≤ C λ² ∫_(r_σ)^∞ r^(2a − 12 + 3) dr = C λ² r_σ^(2a−8)/(8 − 2a)

for a < 4, which is at most κ_Σ(σ)². Finally ∫_(−∞)^0 (1 + |σ|)^(−q) dσ < ∞ exactly when q > 1: q = 2 always,
q = a + 1/2 exactly when a > 1/2, and q = 4 − a exactly when a < 3. ∎

**Proposition {#prop:far-window}** (the weight window). Let ℓ0 ∈ (3, 4) ∖ {7/2}. The conditions that the proof of
[[thm:own-continuation]] places on the weight a are:
(i) the kernels of [[cor:far-kernels]]: 1/2 < a < 3;
(ii) the cap: 𝔈_k1(T) ≤ C(λ, J) |T|^(2a−6), with C(λ, J) independent of T, a bound that is finite and tends to 0 as
T → −∞ exactly when a < 3;
(iii) the flux through ℋ: its density is bounded by C(λ) r^(2a−8), and the bound is integrable, with tail C(λ) ϱ^(2a−7)
beyond r = ϱ, exactly when a < 7/2;
(iv) the class on S: with ρ := 1/r and L²_b := L²(dρ/ρ dω), the energy places h_R|_S in ρ^(a+1) L²_b, which lies in
ρ^(ℓ0) L²_b on {ρ ≤ ρ_0} exactly when a ≥ ℓ0 − 1;
(v) the remaining conditions: a ≥ 3/2, for |H| ≤ r⁻²/4 in Step 1 of the proof of [[thm:own-continuation]]; a > 1/2,
for uniqueness at a smaller weight ([[lem:own-two-continuations]]); a < 7/2, for the data on ℋ at weight a
([[lem:own-e-flux]], [[lem:own-n-data]] (ii)); and a < 3, for the finiteness of the energies of the full slices
([[lem:own-truncation]] (iii), [[lem:own-exterior]]). None of them restricts a beyond (ii) and (iv).
Their intersection is [ℓ0 − 1, 3), and [[thm:own-data]] uses its interior a ∈ (ℓ0 − 1, 3).

*Proof.* (i) is [[cor:far-kernels]]. (ii) By [[lem:own-truncation]] (iii) with k = k1 (J ≥ 2k1 + 7), |∂Γ^α h_R| ≤ C r⁻⁵
on all of Σ̃_T for |α| ≤ k1, on the band and beyond it alike, with C depending on λ and J and not on T. With w ≤ C
r^(2a), d⁴x = r³ dr dω and r_T ≥ c_W (1 + |T|), the energy is at most C ∫_(r_T)^∞ r^(2a−10+3) dr = C r_T^(2a−6)/(6 −
2a) ≤ C |T|^(2a−6) for a < 3; for a ≥ 3 the integral of the bound diverges. (iii) For g_b0 the covector dv is null and
−g_b0⁻¹ dv = L0 ([[prop:vaidya]] (c)), with g_b0(∂_t, L0) = −dv(∂_t) = −1. With L := ∂_t + x̂·∂_x and ∇̸ the gradient on
the spheres {t, r fixed}, |dφ|²_(g_b0) = −(Lφ)(L0φ) + |∇̸φ|² − μ r⁻² (L0φ)², so the flux density of g_b0 is

    T_(g_b0)[φ](w ∂_t, L0) = w ((1/2)(L0φ)² + (1/2)|∇̸φ|² − (1/2) μ r⁻² (L0φ)²).

It contains only derivatives tangent to ℋ, L0 being the generator. On ℋ, g_T = g_λ with all its derivatives
([[lem:own-truncation]] (ii)), so by [[lem:own-n-data]] (i), at fixed λ, the fields Γ^α h_R, |α| ≤ k1 + 1, and all
their first derivatives are O(r^(−9/2)) there, and their derivatives along the generators O(r^(−11/2)). So
L0φ = O(r^(−11/2)) on ℋ, and |∇̸φ| ≤ r⁻¹ Σ_(a<b) |Ω_ab φ| = O(r^(−11/2)), Ω_ab φ being a combination of components of
L_Ω_ab Γ^α h_R and Γ^α h_R, of orders at most k1 + 1. For g = g_b0 + H the density √|g| T_g[φ](w ∂_t, −g⁻¹ dv) differs
from √|g_b0| times that of g_b0 by at most C w |H| |∂φ|²: g(w ∂_t, −g⁻¹ dv) = −w for both metrics, and
g⁻¹ − g_b0⁻¹ = O(|H|). This term contains the transverse derivative. On ℋ, |H| ≤ C r⁻² by [[eq:far-sigma-bounds]] and
[[lem:own-n-data]] (i), and |∂φ| = O(r^(−9/2)), so it is at most C r^(2a) r⁻² r⁻⁹. With w ≤ C r^(2a) and
d⁴x = r³ dr dω the flux density is therefore at most C(λ) r^(2a − 11 + 3) = C(λ) r^(2a−8). Its integral beyond ϱ is
C(λ) ϱ^(2a−7)/(7 − 2a) for a < 7/2, and the bound is not integrable for a ≥ 7/2. (iv) The weighted energy on S bounds
∫ r^(2a+3) |∂h_R|² dr dω, hence, by the first inequality of [[eq:own-hardy]], ∫ r^(2a+1) h_R² dr dω. With r = 1/ρ and
dr = −ρ⁻² dρ, ∫ r^(2a+1) h_R² dr = ∫ (ρ^(−(a+1)) h_R)² dρ/ρ, so h_R|_S ∈ ρ^(a+1) L²_b, and ρ^(a+1) L²_b ⊂ ρ^(ℓ0) L²_b
on ρ ≤ ρ_0 exactly when a + 1 ≥ ℓ0. (v) is the list of the results cited. Since ℓ0 − 1 > 2 > 3/2 > 1/2, the conditions
reduce to ℓ0 − 1 ≤ a < 3. ∎

**Remark {#rem:far-window-sigma4}** (the term Σ_4). (a) Σ_4 could instead be taken to solve

    −(1/2) □_η Σ_4 = −Q_6,     Σ_4 = r⁻⁴ F_4(s, x̂),     F_4(0, ·) = G_8(v1, ·),                   {#eq:far-sigma4}

if a solution smooth up to s = 0, with derivatives bounded on 𝔎 as in [[lem:own-sigma-data]] (b), is available; none is
constructed here, and no proof uses this choice. With it the terms of degree −6 in the proof of [[prop:far-residual]]
sum to −(1/2) □_η Σ_4 + Q_6 = 0, so that P(Σ) is O(λ r^(−13/2)) with every Π_i (Γ_i + c_i), the residual integral of
[[cor:far-kernels]] is C λ² r_σ^(2a−9)/(9 − 2a), κ_Σ becomes C λ (1 + |σ|)^(a−9/2), and (i) of [[prop:far-window]]
becomes 1/2 < a < 7/2. On ℋ, where s = 0, both choices of Σ_4 equal r⁻⁴ G_8(v1, ·); on the initial slice the proof of
[[lem:own-truncation]] (iii) uses of Σ_4 only that it is smooth and homogeneous of degree −4 with F_4(0, ·) = G_8(v1, ·),
and that P(Σ) is tame of order 6, the continuation Σ′_J of [[def:cutoff-extension]] being formed with the Taylor
coefficients F_(4,n) of the chosen F_4. So (ii)–(v) keep their form, the cap's a < 3 binds, and the window is again
[ℓ0 − 1, 3). (b) Without the term p = 4 in Σ, h_R contains r⁻⁴ G_8(v1, ·) on ℋ, so that its derivatives along the
generators and along the spheres are O(r⁻⁵) there and the flux density of (iii) is bounded by C r^(2a−7), with tail
C ϱ^(2a−6) beyond ϱ, integrable exactly when a < 3; on the initial slice Σ′_J then contains the terms
r⁻⁴ s^n G_(8+2n,n), n ≥ 0, still homogeneous of degree −4, so the cap keeps its exponent 2a − 6; and P(Σ) keeps its
terms Q_6 of degree −6, so (i) gives a < 3. The conditions then leave [ℓ0 − 1, 3) again.

**Theorem {#thm:own-continuation}** (the continuation). Under the hypotheses of [[thm:own-data]] there are λ_2 > 0
and ε_2 > 0 such that for 0 < λ ≤ λ_2 the following holds. For every integer J ≥ 2k1 + 7 there is T_1(λ, J) such that
for T ≤ T_1(λ, J) the solution g_T^(J) of the truncated problem of [[def:cutoff-truncation]] exists on all of W_T, and as
T → −∞ the g_T^(J) converge in C^(k_J−3) on compact subsets of W, k_J := ⌊(J − 7)/2⌋, to a metric g on W that does not
depend on J. g is smooth and G-invariant, Ric^H(g; g_b0) = 0, and g joins g_λ smoothly across ℋ. Its remainder
h_R = g − g_b0 − Σ satisfies 𝔈_(k1)(σ) ≤ ε_B² for σ ≤ 0, with ε_B = ε_B(λ) → 0 as λ → 0, 𝔈_k(σ) ≤ C_k(λ) for every
k, and E_σ[Γ^α h_R] → 0 as σ → −∞ for |α| ≤ k1; the pointwise bounds [[eq:own-pointwise]] hold with ε_B. On S,
h_R|_S ∈ ρ^(a+1) H_b^k and ∂h_R|_S ∈ ρ^(a+2) H_b^k (dρ/ρ dω) for every k, and the data (γ, k) of g on S satisfy
γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b, k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b on S, with ‖·‖_(d_1) ≤ C(λ + ε_B) there.

*Proof.* Steps 1–5 fix J ≥ 2k1 + 7 and write g_T for g_T^(J); λ_2, ε_2 and ε_B will not depend on J.

*Step 1 (the bootstrap and the pointwise bounds).* Let T ≤ T_1(λ, J) (chosen in Step 3, with T_1(λ, J) ≤ T_0), put
H := g_T − g_b0 and h_R := H − Σ, and assume (BA): 𝔈_(k1)(σ) ≤ 4ε_B² on [T, σ*] and |H| ≤ 1/50 on W_T ∩ {t̃ ≤ σ*},
where σ* < σ_1(T) and ε_B ≤ ε_2 is to be fixed. Under (BA) the bounds [[eq:own-pointwise]] hold for σ ∈ [T, σ*] and
r ≥ r_σ, with C_S independent of T, J, λ and ε_B. Indeed, by [[lem:own-margins]] (a), |g_T⁻¹ − g_b0⁻¹| ≤ 0.0232 on
W_T ∩ {t̃ ≤ σ*}, so [[lem:own-exterior]] applies with σ′ := σ* and c := 0.0232; and by [[lem:own-margins]] (d),
E_σ[φ] ≥ c_1 ∫ r^(2a) |∂φ|² r³ dr dω, as w ≥ r^(2a). By [[eq:own-ray-derivative]] the ray derivative of
F := Ω^γ ∂Γ^β h_R, |γ| ≤ 2, is a combination, with bounded coefficients, of first derivatives of commuted fields of
order at most |β| + 3, with no undifferentiated term; so the two norms in [[eq:own-s1]] are at most C 𝔈_(|β|+3)(σ)^(1/2),
and [[eq:own-s1]] with the Sobolev embedding H²(S³) ⊂ L^∞(S³) gives the first bound for |β| ≤ k1 − 3. The second is
the first with one more commutation, by [[lem:own-rays]] (a). For the third, ψ := Ω^γ Γ^β h_R, |γ| ≤ 2, tends to 0 at
spatial infinity along the rays of Σ̃_σ by [[lem:own-exterior]] (a), and ∫ r^(2a+3) |dψ/dr|² dr < ∞ on almost every
ray; so the second inequality of [[eq:own-hardy]], integrated over S³, gives
∫_(S³) r^(2a+2) |ψ(r, ω)|² dω ≤ (2a + 2)⁻¹ ∫_(S³) ∫_r^∞ s^(2a+3) |dψ/ds|² ds dω ≤ C 𝔈_(|β|+2)(σ), and the Sobolev
embedding on S³ gives |Γ^β h_R| ≤ C ε_B r^(−1−a) ≤ C ε_B r^(−1/2−a). With [[lem:own-sigma-data]] (b), on
W_T ∩ {t̃ ≤ σ*}, |H| ≤ C λ r⁻² + C_S ε_B r^(−1/2−a) ≤ min(1/100, 𝔪/2, r⁻²/4) for λ ≤ λ_2 and ε_B ≤ ε_2, since a ≥ 3/2
and r ≥ 4R ≥ 1; so [[lem:own-margins]] (a)–(e) apply, with |g_T⁻¹ − g_b0⁻¹| ≤ 0.0232 and ≤ 0.2845 r⁻².

*Step 2 (the commuted equations and the energy inequality).* By [[lem:far-scaling]] (b), differentiated in ς at ς = 1,
(Z + 2)P_μ(h) = DP_μ(h)[Zh] − 2μ∂_μ P_μ(h) for every h; ∂_t P(h) = DP(h)[∂_t h], P being static; and
ℒ_Ω P(h) = DP(h)[ℒ_Ω h] by [[lem:far-naturality]]. Write (Γ + c_Γ)P(h) = DP(h)[Γh] + M_Γ P(h), with c_Z = 2,
M_Z = −2μ∂_μ, and c_Γ = 0, M_Γ = 0 otherwise. Since P(Σ + h_R) = 0, subtracting the identity for Σ gives
DP(H)[Γh_R] = −(Γ + c_Γ)P(Σ) − (DP(H) − DP(Σ))[ΓΣ] − M_Γ(P(H) − P(Σ)); differentiating the identity in h,
(Γ + c_Γ)DP(h)[k] = DP(h)[Γk] + D²P(h)[Γh, k] + M_Γ DP(h)[k], and by induction on |α|

    DP(H)[Γ^α h_R] = −R^α + (A) + (B) + (C),     R^α := Π_i (Γ_i + c_(Γ_i)) P(Σ),
                                                                                                       {#eq:own-commuted}

where (A) is linear in one Γ^β h_R, |β| ≤ |α|, with coefficients built from the Γ^γ Σ (from D^n P(H) with one slot h_R
and the others Σ, n ≥ 2, and from DP(H) − DP(Σ) on Γ^α Σ); (B) has at least two slots Γ^(α_i) h_R, with
Σ_i |α_i| ≤ |α|; and (C) is (μ∂_μ)^j DP(H)[Γ^β h_R], j ≥ 1, |β| < |α|. In (A), (B) and (C) a slot that carries two
derivatives has order at most max(|α| − 1, 0): second derivatives of a field of order |α| occur only in
DP(H)[Γ^α h_R], as the identities above show by induction. Componentwise DP(H)[k] = −½ g^(ab)∂_a∂_b k +
B(H)·∂k + C(H)k ([[prop:far-coefficients]]). For φ := (Γ^α h_R)_ij, [[eq:own-energy-identity]] on the bounded domain
D_*(σ) := W_T ∩ {t̃ ≤ σ} ∩ {Φ_W ≤ V_*}, σ ≤ σ*, whose boundary consists of Σ̃_σ ∩ {Φ_W ≤ V_*} (future), Σ̃_T ∩ {Φ_W ≤
V_*} and ℋ ∩ D_*(σ) (past) and {Φ_W = V_*} (future, spacelike by [[lem:own-margins]] (c), with nonnegative flux,
dropped), gives

    E_σ[φ] ≤ E_T[φ] + F_ℋ[φ] − ∫∫ √|g| w (□_g φ) ∂_t φ − ½ ∫∫ √|g| w T_g[φ]^(ab) ∂_t g_ab,
                                                                                              {#eq:own-energy-inequality}

with □_g φ = −2(DP(H)[Γ^α h_R])_ij + 2(B(H)·∂Γ^α h_R)_ij + 2(C(H)Γ^α h_R)_ij − g^(ab)Γ[g]^c_ab ∂_c φ, the bulk term
T_g[φ](∇w, ∂_t) ≥ 0 dropped, the integrals over D_*(σ) and the energies restricted to {Φ_W ≤ V_*}; as V_* → ∞, the left
side increases to E_σ[φ] and the right side converges to its value on the full slices, every integrand being integrable
over W_T ∩ {t̃ ≤ σ} by [[lem:own-exterior]] (b), as |□_g φ| ≤ C(|∂∂φ| + |∂φ|), |∂_t g| ≤ C and w ≤ C r^(2a) there.
The hypotheses of [[cor:far-kernels]] hold on [T, σ*]: |H| ≤ 1/50 and 𝔈_(k1) < ∞ by (BA), the decay at spatial
infinity by [[lem:own-exterior]] (a), and [[eq:own-pointwise]] by Step 1. So the error terms are bounded by
[[cor:far-kernels]]; in (B), a term of total order at most k1 with at least two slots has its slot of highest order in
L² (an undifferentiated slot through [[eq:own-hardy]], a twice differentiated one, of order at most k1 − 1, through
[[lem:own-rays]] (a)) and the others pointwise by [[eq:own-pointwise]], which is possible since the second-largest order
is at most k1/2 and k1/2 + 4 ≤ k1 for k1 ≥ 8. Summing over |α| ≤ k1 and the components, with the fluxes bounded by
[[lem:own-n-data]] (iii),

    𝔈_(k1)(σ) ≤ C_E [ 𝔈_(k1)(T) + 𝔉_(k1) + ∫_T^σ κ 𝔈_(k1) + ∫_T^σ κ_Σ 𝔈_(k1)^(1/2) ],
                                                                                                       {#eq:own-gronwall}

κ and κ_Σ as in [[eq:far-kernels]]; ∫ κ ≤ K_κ := C(μ + 1) and ∫ κ_Σ ≤ κ_∞ := C λ/(3 − a), independent of T.

*Step 3 (closing).* With y(σ) := sup_[T,σ] 𝔈_(k1)^(1/2), Gronwall's inequality gives
y² ≤ C_E e^(C_E K_κ)(𝔈_(k1)(T) + 𝔉_(k1) + 2y κ_∞), so 𝔈_(k1) ≤ C_*(𝔈_(k1)(T) + 𝔉_(k1) + λ²) on [T, σ*], with C_*
independent of T, J, λ and ε_B. By [[lem:own-n-data]] (ii) and (iii), 𝔉_(k1) ≤ C(λ² + ν(λ)). By [[lem:own-truncation]]
(iii) with k = k1, which applies as J ≥ 2k1 + 7, the cap satisfies 𝔈_(k1)(T) ≤ C(λ, J)|T|^(2a−6) (condition (ii) of
[[prop:far-window]]), and as a < 3 this is at most λ² for T ≤ T_1(λ, J). Put ε_B² := C_*(C(λ² + ν(λ)) + 2λ²), with
C_* ≥ 1, which depends on neither T nor J. So ε_B → 0 as λ → 0, ε_B ≤ ε_2 for λ ≤ λ_2, and 𝔈_(k1) ≤ ε_B² < 4ε_B² on
[T, σ*]; and by Step 1, |H| ≤ 1/100 < 1/50 on W_T ∩ {t̃ ≤ σ*}: (BA) is improved.

*Openness.* Let σ′ ∈ (σ*, σ_1(T)); every derivative of g_T is bounded on W_T ∩ {t̃ ≤ σ′}, say |∂H| ≤ C_1 there. Let p ∈
W_T with σ* < t̃(p) ≤ σ* + δ′ ≤ σ′. Along the segment from p on which v and x̂ are fixed and r increases, t̃ = v − r −
f(r) decreases at the rate 1 + f′ ≥ 1, while v ≥ v1 and r ≥ 4R stay true; so it reaches Σ̃_(σ*) after an increase of r by
at most δ′, inside W_T ∩ {t̃ ≤ σ′}, with Euclidean length at most √2 δ′. Hence |H(p)| ≤ 1/100 + √2 C_1 δ′ ≤ 1/50 for δ′
small, and [[lem:own-exterior]] applies on [T, σ* + δ′] with c = 0.0232: by its (c), 𝔈_(k1) is continuous there, and as
𝔈_(k1)(σ*) ≤ ε_B², (BA) holds on [T, σ* + δ″] for some δ″ > 0. The set of the σ* ∈ [T, σ_1(T)) at which (BA) holds is
therefore open; it is closed, both conditions being closed; and it contains T, since on Σ̃_T, 𝔈_(k1)(T) ≤ λ² ≤ 4ε_B² and
H = H_D, |H_D| ≤ 1/50 (the proof of [[lem:own-truncation]] (iii)). So (BA), and with it 𝔈_(k1) ≤ ε_B² and the bounds of
Step 1, hold on [T, σ_1(T)). If σ_1(T) < 0, these bounds, uniform on W_T ∩ {t̃ < σ_1(T)}, let the local theory continue
g_T with bounded derivatives beyond σ_1(T) ([[lem:own-truncation]] (iv)), against the definition of σ_1(T); so σ_1(T) =
0, and the same continuation across {t̃ = 0} shows that g_T exists and is smooth on all of W_T, with 𝔈_(k1) ≤ ε_B² and
the bounds of Step 1 on [T, 0].

*Step 4 (higher orders at fixed λ and J).* For k1 < k ≤ k_J, induct on k: in the commuted equations at order k the
terms of top order are linear in the order-k quantities, with coefficients bounded by [[eq:own-pointwise]] and its
analogues at the orders at most k − 1 (in (B) the second-largest order is at most ⌊k/2⌋, and ⌊k/2⌋ + 4 ≤ k − 1 for
k ≥ 9), so [[eq:own-gronwall]] holds at order k with ε_B replaced by C_(k−1)(λ, J) in the pointwise factors, 𝔈_k being
finite and continuous by [[lem:own-exterior]] (c), and Gronwall's inequality closes without smallness:
𝔈_k ≤ C_k(λ, J)(𝔈_k(T) + 𝔉_k + λ²). This is finite and uniform in T by [[lem:own-n-data]] (i), (iii) and the cap
𝔈_k(T) ≤ C(λ, J)|T|^(2a−6) of [[lem:own-truncation]] (iii), which applies as J ≥ 2k + 7 for k ≤ k_J.

*Step 5 (the limit).* For T′ < T ≤ T_1(λ, J), ξ := g_(T′) − g_T on W_T solves the linear system obtained by subtracting
the two equations, with g_(T′) as principal part, −½ g_(T′)^(ab)∂_a∂_b ξ = ½(g_(T′)^(ab) − g_T^(ab))∂_a∂_b g_T +
(Q(g_(T′))(∂g_(T′), ∂g_(T′)) − Q(g_T)(∂g_T, ∂g_T)) ([[eq:own-p-split]]), linear in (ξ, ∂ξ), whose coefficients ∂∂H_T,
∂H_T, ∂H_(T′) give the kernels of [[cor:far-kernels]]. ξ = 0 near ℋ ∩ W_T, where both equal g_λ. On Σ̃_T,
ξ = h_(R,T′)(T) − h_(R,T)(T): the second is the cap, and the first is bounded by Step 2 run for g_(T′) on
W_(T′) ∩ {t̃ ≤ T}, whose data are tails: 𝔈[h_(R,T′)](T) ≤ C(𝔈(T′) + 𝔉_(k1)(T′, T) + (∫_(−∞)^T κ_Σ)²) =: ϑ(T), with
𝔉(T′, T) ≤ C(λ)|T|^(2a−7) (ℋ ∩ {t̃ ≤ T} lies in r ≥ |T| − C, [[lem:own-n-data]] (iii)), the cap at most
C(λ, J)|T′|^(2a−6) and ∫_(−∞)^T κ_Σ ≤ C λ |T|^(a−3). So the energy of ξ on W_T is at most C ϑ(T) → 0 as T → −∞,
uniformly in T′ < T: (g_T) is a Cauchy family in the energy of weight a on every W_(T″).

*Convergence.* Let 𝔇 := W ∩ {T″ ≤ t̃ ≤ 0, r ≤ R′}, which is compact and connected and meets ℋ. By Step 4 and the
analogues of [[eq:own-pointwise]] at the order k_J (Step 1 with k_J in place of k1), |Γ^β h_R| and |∂Γ^β h_R| are
bounded on 𝔇 uniformly in T for |β| ≤ k_J − 3. As ∂_i = r⁻¹ x̂_i (Z − (t − v1)∂_t) − r⁻² x_j Ω_ij
([[lem:own-rays]] (a)), every Cartesian derivative of order j of h_R is, on 𝔇, a combination of the Γ^β h_R, |β| ≤ j,
with coefficients bounded on 𝔇; so the g_T are bounded in C^(k_J−2)(𝔇) uniformly in T. By the Arzelà–Ascoli theorem
every sequence T_n → −∞ has a subsequence along which g_(T_n) converges in C^(k_J−3)(𝔇). Two such limits g^(1), g^(2)
coincide: ∫_(𝔇) |∂(g_(T_n) − g_(T′_n))|² d⁵x ≤ C |T″| ϑ(max(T_n, T′_n)) → 0 by the Cauchy property, w ≥ 1 and
[[lem:own-margins]] (d), so ∂(g^(1) − g^(2)) = 0 on 𝔇, and g^(1) = g^(2) = g_λ on ℋ ∩ 𝔇. Hence the whole family
converges in C^(k_J−3)(𝔇), and so on every compact subset of W. Its limit g^(J) is of class C^(k_J−3), k_J − 3 ≥ 5,
solves Ric^H(g^(J); g_b0) = 0, equals g_λ on ℋ with its derivatives of order at most k_J − 3, and, with
h_R^(J) := g^(J) − g_b0 − Σ, has 𝔈_(k1) ≤ ε_B² and 𝔈_k ≤ C_k(λ, J) for k ≤ k_J by lower semicontinuity, satisfies
[[eq:own-pointwise]] (the g_T satisfy it with constants independent of T, and its derivatives have order at most
k1 − 2 ≤ k_J − 3), and has E_σ[Γ^α h_R^(J)] ≤ C ϑ(σ) → 0 as σ → −∞ for |α| ≤ k1. G-invariance passes to the limit.

*The limit does not depend on J.* For J′ ≥ J ≥ 2k1 + 7, g^(J′) = g^(J) by [[lem:cutoff-independence]], which is in
Section [[sec:own-vacuum]]; its proof uses only the properties of g^(J) and g^(J′) just listed and
[[lem:own-two-continuations]], not the conclusions of this theorem. Write g for the common limit. As g = g^(J) is of
class C^(k_J−3) for every J, g is smooth, and as it equals g_λ on ℋ with all its derivatives (each g_T equals g_λ on its
side v ≤ v1, [[lem:own-truncation]] (ii)), g and g_λ join smoothly across ℋ. Taking J := max(2k1 + 7, 2k + 7) gives
𝔈_k ≤ C_k(λ) := C_k(λ, J) for every k.

*Step 6 (the class on S).* On S = {t = f(r)}, r d/dr (h_R|_S) = (Z h_R)|_S + (v1 − f + r f′)(∂_t h_R)|_S, with
r f′ ∈ C^∞ in ρ := 1/r and f smooth in ρ (f′ ∈ |x|⁻² C^∞): every (ρ∂_ρ)^j Ω^β (h_R|_S) is a combination of restrictions
of commuted fields with coefficients smooth in ρ. On S, w ≥ r^(2a), and by [[eq:own-hardy]], with r = 1/ρ and
r^(2a+1) dr = ρ^(−2(a+1)) dρ/ρ, the energies place h_R|_S in ρ^(a+1) L²_b(dρ/ρ dω) and ∂h_R|_S in ρ^(a+2) L²_b, with
every b-derivative, a + 1 > ℓ0. On S, s = 1 + (f − v1)ρ is smooth in ρ, so Σ|_S = Σ_(p∈Π) ρ^p F_p(1 + (f − v1)ρ, x̂) is
polyhomogeneous with exponents p + j, j ∈ ℕ_0, all in ℰ_0^½, and its coefficients are O(λ) by [[lem:own-sigma-data]], the
coefficient of ρ^(5/2) being F_(5/2)(1, ·), which is O(λ^n) for every n by [[lem:own-sigma-data]] (a) and
[[lem:own-self-similar]]. The induced (γ, k) are smooth functions of (g, ∂g) on S and of (∂f, ∂²f), as in the proof of
[[lem:vii-2-1]], equal to (γ_b0, k_b0) at h = 0, and ℰ_0^½ is closed under sums; so γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b and
k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b on S, with ‖·‖_(d_1) ≤ C(λ + ε_B), since k1 ≥ d_1 + 4 covers the d_1 derivatives and
the commutations used here. ∎

### The continuation is vacuum, and it is unique {#sec:own-vacuum}

**Proposition {#prop:own-vacuum}** (the limit is vacuum). The metric g of [[thm:own-continuation]] has D(g) = 0 on W,
D the gauge field of [[eq:gauge]] relative to g0 (= g_b0 on W); hence Ric(g) = 0. Together with g_λ on P′ ∪ Ω′ it is a
smooth vacuum metric, and its data (γ, k) on Σ^IVP satisfy the constraint equations.

*Proof.* (i) *An identity.* For every Lorentzian g, ∇̂_n D^ρ = ∇_n D^ρ + (Γ[g0] − Γ[g])^ρ_(ns) D^s, ∇ the connection of
g, so by [[eq:gauge]] Ric(g)_mn = Ric^H(g)_mn + ½(∇_m D_n + ∇_n D_m) + C_mn, with
C_mn := ½(g_mρ (Γ[g0] − Γ[g])^ρ_(ns) + g_nρ (Γ[g0] − Γ[g])^ρ_(ms)) D^s. With Ein(X) := X − ½ g tr_g X, the contracted
Bianchi identity ∇^m Ein(Ric(g))_mn = 0 and ∇^m Ein(½(∇D + ∇D^T))_mn = ½ □_g D_n + ½(∇^m ∇_n D_m − ∇_n ∇^m D_m) =
½(□_g D_n + Ric(g)_n^d D_d) give

    ½(□_g D_n + Ric(g)_n^d D_d) + ∇^m Ein(C)_mn + ∇^m Ein(Ric^H(g))_mn = 0.
                                                                                                        {#eq:own-bianchi}

Where Ric^H(g) = 0 this is a linear homogeneous system for D: −½ g^(ab) ∂_a ∂_b D_n = b·∂D + cD in Cartesian components,
with Ric(g) and Γ[g] taken as known coefficients, |b| ≤ C(μ r⁻³ + |∂H|) and |c| ≤ C(μ r⁻⁴ + |∂∂H| + |∂H|²) on W,
H = g − g_b0.
(ii) *The truncations.* Fix J ≥ 2k1 + 7 and write g_T := g_T^(J), T ≤ T_1(λ, J). Each g_T solves Ric^H(g_T) = 0 on
W_T, so D_T := D(g_T) solves (i)'s system there. D(g) is linear in ∂(g − g_b0) with coefficients in g⁻¹, plus terms
(g⁻¹ − g_b0⁻¹)Γ̂, so |D(g_b0 + H)| ≤ C(|∂H| + r⁻³|H|), and |∂D(g_b0 + H)| ≤ C(|∂∂H| + |∂H| + r⁻³|H|) where |∂H| is
bounded. Take the energy of weight 1 ([[eq:own-energies]] with w = (u* − u)² ≤ C r² ≤ C r^(2a)); it is finite on every
Σ̃_σ, σ ∈ [T, 0], by [[lem:own-exterior]] (b) and [[lem:own-sigma-data]] (b), H = Σ + h_R, the hypotheses of
[[lem:own-exterior]] holding with σ′ = 0 and c = 0.0232 by Steps 1 and 3 of the proof of [[thm:own-continuation]]. By
[[eq:own-pointwise]] and [[lem:own-sigma-data]], the kernels of its error terms are those of [[cor:far-kernels]], with
exponents 3, 3/2 + a and a + 1/2, all integrable, the zero-order terms entering through [[eq:own-hardy]]; D_T tends
to 0 at spatial infinity along the slices by [[lem:own-exterior]] (a). On ℋ, D_T = D(g_λ) = 0 with its tangential
derivatives, g_T being g_λ on the side v ≤ v1 ([[lem:own-truncation]] (ii)) and g_λ vacuum in the wave-map gauge
([[thm:past-construction]]); so the flux through ℋ vanishes. On Σ̃_T, g_T and ∂g_T are those of 𝔤_T, and
∂²g_T = ∂²𝔤_T + ∂²δ ([[eq:cutoff-hd]]). On Σ̃_T ∩ {v ≤ V_T}, δ vanishes to every order (the proof of
[[lem:own-truncation]] (iii)), so D_T and ∂D_T are those of D(g_λ) = 0. On 𝒮^♭_T ∩ {v ≥ V_T},
H_D = (g_λ − g_b0) − χ_T m_J, so D(g_b0 + H_D) = D(g_λ) + O(r^(−(J+1)/2)) = O(r^(−(J+1)/2)) with its first derivatives
([[lem:cutoff-extension]] (b)), and |∂²δ| ≤ C r^(−(J+3)/2) + C r⁻⁶ ([[lem:cutoff-jets]]); as J ≥ 9, the
bound |D_T| + |∂D_T| ≤ C r⁻⁵ holds there. On Σ̃_T ∩ {v ≥ V_T + δ_0/4}, H_D = Σ + Σ′_J; D(g_b0 + Σ) = O(λ r⁻³) and
∂D(g_b0 + Σ) = O(λ r⁻⁴), as |∂^j Σ| ≤ C λ r^(−2−j) ([[lem:own-sigma-data]] (b)); the terms of Σ′_J add O(r⁻⁵) and
O(r⁻⁶) ([[lem:cutoff-extension]] (a)); and |∂²δ| ≤ C r⁻⁶; so |∂D_T| ≤ C λ r⁻⁴ + C r⁻⁶ there. Here C depends on λ and
J. With w ≤ C r², d⁴x = r³ dr dω and 𝒮^♭_T = {r_T ≤ r ≤ r_T + d_V} along the rays, the energy of D_T on Σ̃_T is at most
C ∫_(r_T)^∞ r² (λ² r⁻⁸ + r⁻¹²) r³ dr + C r_T^(2+3) r_T^(−10) d_V ≤ C λ² |T|⁻² + C |T|⁻⁴, as r_T ≥ c_W (1 + |T|).
Gronwall's inequality, with constants independent of T, gives E_σ[D_T] ≤ C λ² |T|⁻² + C(λ, J) |T|⁻⁴ for σ ∈ [T, 0],
which tends to 0 as T → −∞.
(iii) *The limit.* As T → −∞, g_T = g_T^(J) → g in C² on compact subsets of W ([[thm:own-continuation]],
k_J − 3 ≥ 5), so D(g_T) → D(g) in C¹ there, and the energy of D(g) on any compact part of any Σ̃_σ is the limit of
those of D_T, hence 0: ∂D(g) = 0 on W. As D(g) = 0 on ℋ, D(g) = 0.
Then Ric(g) = Ric^H(g) + ½(∇D + ∇D^T) + C = 0. g_λ is vacuum on P′ ∪ Ω′, and the join across ℋ is smooth
([[thm:own-continuation]]). ∎

**Lemma {#lem:own-two-continuations}** (two continuations coincide). Let a_0 ∈ (0, ½) and 0 < λ ≤ λ_2. Let
g = g_b0 + Σ + h_R be a C⁵ metric on W with Ric^H(g; g_b0) = 0, g = g_λ on ℋ with its first derivatives, satisfying
[[eq:own-pointwise]] on every Σ̃_σ, σ ≤ 0, with some ε_B ≤ ε_2, and with E_σ[h_R] → 0 as σ → −∞. Let g′ = g_b0 + h′ be
a C⁵ metric on W with Ric^H(g′; g_b0) = 0, g′ = g_λ on ℋ with its first derivatives, |h′| ≤ 1/50,
sup_(σ≤0) E^(a_0)_σ[Γ^α h′] < ∞ for |α| ≤ 3, Γ ∈ {∂_t, L_Ω_ab, Z}, and E^(a_0)_σ[h′] → 0 as σ → −∞, where E^(a_0) is the
energy [[eq:own-energies]] for g′ with the weight (u* − u)^(2a_0). Then g′ = g.

*Proof.* (1) By [[lem:own-margins]] (d) for g′ and [[eq:own-s1]], whose right side involves, by
[[eq:own-ray-derivative]], only the energies of first derivatives of Γ^α h′, |α| ≤ 3, which are bounded uniformly in
σ, |∂h′| ≤ C_0 r^(−3/2−a_0) on every Σ̃_σ, with C_0 independent of σ. (2) Along each ray of Σ̃_σ, |d h′/dr| ≤
(1 + |f′|) C_0 r^(−3/2−a_0) is integrable, so h′ has a limit c(σ, x̂) at spatial infinity. (3) c does not depend on σ:
for σ_1 < σ_2 ≤ 0 and r large the time segment from (f(r) + σ_1, r x̂) to (f(r) + σ_2, r x̂) lies in W, and the
difference of h′ at its ends is at most (σ_2 − σ_1) C_0 r^(−3/2−a_0) → 0. (4) c = 0: the inner edge of Σ̃_σ lies on ℋ,
where h′ = g_λ − g_b0 = O(r⁻²) (on ℋ, v1 > v_end, so g_λ − g0 = u_1 is in E_2, [[eq:bondi-u-split]] with G_3 = 0);
so |c(x̂)| ≤ C r_σ⁻² + C C_0 r_σ^(−1/2−a_0), and r_σ → ∞ as σ → −∞. Hence h′ = −∫_r^∞ ∂_s h′ ds along the
rays, and h′ is at most C r^(−1/2−a_0) in modulus with C independent of σ, and [[eq:own-hardy]] holds on every Σ̃_σ
at the weight a_0 with constants independent of σ. Now ξ := g′ − g solves
−½ g′^(ab) ∂_a ∂_b ξ = ½(g′^(ab) − g^(ab)) ∂_a ∂_b g + (Q(g′)(∂g′, ∂g′) − Q(g)(∂g, ∂g)) ([[eq:own-p-split]]), linear in
(ξ, ∂ξ): the zero-order coefficients are ∂∂g, with H := g − g_b0 and
r|∂∂H| ≤ C(μ + λ) r⁻³ + C ε_B r^(−1/2−a) by [[eq:own-pointwise]] and [[lem:own-sigma-data]] (b), and |∂g′|², and the
first-order ones |∂g| + |∂g′|. Apply [[eq:own-energy-identity]] to ξ with the metric g′ and the weight a_0: the
deformation term carries |∂_t h′| ≤ C_0 r^(−3/2−a_0); the bulk term T_(g′)(∇w, ∂_t) is at least −C|h′| |w′| |∂ξ|²,
with |w′|/w ≤ C r⁻¹, a kernel r^(−3/2−a_0); the zero-order terms through [[eq:own-hardy]] give the exponents
min(3, a + 1/2) and 2 + 2a_0; all exponents exceed 1 since a > ½. ξ = 0 on ℋ with its first derivatives, so the
flux through ℋ vanishes; on Σ̃_(σ_1), E^(a_0)[ξ] ≤ 2E^(a_0)[h′] + 2E^(a_0)[g − g_b0], and both tend to 0 as σ_1 → −∞
(for Σ, |∂Σ| ≤ C λ r⁻³ gives C λ² r_(σ_1)^(2a_0−2); for h_R, its weight-a energy tends to 0 and dominates its weight-a_0
energy, as u* − u ≥ 1 on W, the energies of g and g′ being comparable by [[lem:own-margins]] (d), as |H| ≤ 1/50 by
[[eq:own-pointwise]] and [[lem:own-sigma-data]] (b) as in Step 1 of the proof of [[thm:own-continuation]]). Gronwall's
inequality from σ_1, with constants independent of σ_1, and σ_1 → −∞ give ξ = 0. The proof uses of g′ its energies of
the Γ^α h′, |α| ≤ 3, and the ray bound [[eq:own-s1]] for Ω^γ ∂h′, |γ| ≤ 2, which involve at most four derivatives of
h′, and of g the bounds [[eq:own-pointwise]] and its energies; so C⁵ regularity suffices. ∎

**Lemma {#lem:cutoff-independence}** (the limit does not depend on J). For J ≥ 2k1 + 7 let g^(J) be the limit of the
g_T^(J) given by Steps 1–5 of the proof of [[thm:own-continuation]] at fixed J: a metric on W of class C^(k_J−3) with
Ric^H(g^(J); g_b0) = 0, equal to g_λ on ℋ with its first derivatives, satisfying [[eq:own-pointwise]] with ε_B and
𝔈_(k1) ≤ ε_B², and with E_σ[Γ^α h_R^(J)] → 0 as σ → −∞ for |α| ≤ k1, h_R^(J) := g^(J) − g_b0 − Σ. Then
g^(J′) = g^(J) for J′ ≥ J ≥ 2k1 + 7.

*Proof.* Let a_0 ∈ (0, ½). g := g^(J) satisfies the hypotheses of [[lem:own-two-continuations]] on g, as k_J − 3 ≥ 5.
g′ := g^(J′) is of class C⁵, as k_J′ − 3 ≥ 5, satisfies Ric^H(g′; g_b0) = 0, and equals g_λ on ℋ with its first
derivatives. With h′ := g′ − g_b0 = Σ + h_R^(J′): |h′| ≤ C λ r⁻² + C_S ε_B r^(−1/2−a) ≤ 1/50 as in Step 1 of the proof
of [[thm:own-continuation]]; the energies of weight a_0 of the Γ^α h_R^(J′), |α| ≤ 3, are bounded uniformly in σ and
tend to 0 as σ → −∞, being dominated by those of weight a, as u* − u ≥ 1 on W; and those of the Γ^α Σ are at most
C λ² r_σ^(2a_0−2), since |∂Γ^α Σ| ≤ C λ r⁻³ ([[lem:own-sigma-data]] (b)) and ∫_(r_σ)^∞ r^(2a_0) r⁻⁶ r³ dr =
r_σ^(2a_0−2)/(2 − 2a_0). So g′ satisfies the hypotheses of [[lem:own-two-continuations]] on g′, and g^(J′) = g^(J). ∎

**Proposition {#prop:own-uniqueness}** (uniqueness at a weight below ½). Let a_0 ∈ (0, ½), and let g′ = g_b0 + h′ be a
smooth metric on W with Ric^H(g′; g_b0) = 0, g′ = g_λ on ℋ with its first derivatives, |h′| ≤ 1/50,
sup_(σ≤0) E^(a_0)_σ[Γ^α h′] < ∞ for |α| ≤ 3, Γ ∈ {∂_t, L_Ω_ab, Z}, and E^(a_0)_σ[h′] → 0 as σ → −∞, where E^(a_0) is the
energy [[eq:own-energies]] for g′ with the weight (u* − u)^(2a_0). Then g′ = g, the metric of [[thm:own-continuation]].

*Proof.* The metric g of [[thm:own-continuation]] is smooth, satisfies Ric^H(g; g_b0) = 0, equals g_λ on ℋ with its
derivatives, satisfies [[eq:own-pointwise]] with ε_B ≤ ε_2, and has E_σ[h_R] → 0 as σ → −∞. g′ is smooth, hence C⁵.
So [[lem:own-two-continuations]] gives g′ = g. ∎

The class of [[prop:own-uniqueness]] contains every candidate whose difference from g_b0 approaches it like r⁻² without
radiation, with bounded commuted energies; the metric g of [[thm:own-continuation]] lies in it, since its energies of
weight a_0 < a are bounded by those of weight a.

**Remark {#rem:own-low-weight}** (why existence is proved at a larger weight). Existence is not attempted at a weight
a_0 ≤ ½. In the energies of weight a_0 of Γ^α h, h := g − g_b0, without the subtraction of Σ, the top-order term
−½(Dg⁻¹[Γ^α h])^(ab) ∂_a ∂_b h of the commuted equation, bounded through [[eq:own-hardy]] for Γ^α h and the pointwise
bound C ε r^(−3/2−a_0) of ∂∂h, gives the kernel (1 + |σ|)^(−a_0−1/2), which is not integrable for a_0 ≤ ½. And energies
of weight a_0 < ½ do not see a radiation field constant in v: for a spherical harmonic Y_l of degree l,
φ := r^(−3/2) ₂F₁(3/2 + l, −½ − l; 1; s/2) Y_l solves □_η φ = 0 (the equation of the proof of [[lem:own-self-similar]]
at p = 3/2), its radiation field r^(3/2) φ tends to Y_l at past null infinity at every v ≥ v1, and its flux through ℋ
and its energy on Σ̃_T are finite, the latter tending to 0 as T → −∞, exactly when a_0 < ½ (both densities are of order
r^(2a_0−2)). On a slice of constant t it reaches spatial infinity as ρ^(3/2) T_(3/2)(l) Y_l, with
T_(3/2)(l) = √π/(Γ((l + 5/2)/2) Γ((½ − l)/2)) ≠ 0 by [DLMF, (15.4.28)]. The subtraction of Σ and the weight a > ℓ0 − 1
of [[thm:own-continuation]] avoid both: the remainder decays like r^(−9/2) on ℋ and the weight places it in the class.

### The tail on the initial surface, and the proof of the theorem {#sec:own-proof}

**Proposition {#prop:own-transfer}** (the tail reaches the data). Let 0 < λ ≤ λ_2, with λ_2 as in [[thm:own-data]], and
let γ be the metric that g induces on S. In the spatial Cartesian components of γ − γ_b0 the coefficient of ρ^(5/2) at
spatial infinity is a_(5/2) := Σ_l T(l) (G_5^∞)_l, the sum over the spherical-harmonic parts of the spatial components of
G_5^∞, with

    T(l) := ₂F₁(5/2 + l, ½ − l; 2; ½) = √π/(Γ((2l + 7)/4) Γ((3 − 2l)/4)) ≠ 0.
                                                                                                       {#eq:own-transfer}

Off the exceptional set of [[prop:own-tail]] (d), a_(5/2) ≠ 0, and γ − γ_b0 does not lie in H^(∞,(ℰ_0^ℤ,ℓ0))_b on S for
any ℓ0 > 5/2. Since γ^m − γ_b0 ∈ ρ² C^∞ for the Tangherlini data of every mass m ([[lem:vii-2-1]] (a)), the data of g_λ
then differ from those of every Tangherlini metric by a term outside the class of [[thm:settling]] (ii).

*Proof.* γ_ij = g_ij + 2 g_(t(i) ∂_(j)) f + g_tt ∂_i f ∂_j f on S, and ∂f = O(ρ²), so the part of γ − γ_b0 that is linear
in h := g − g_b0 is h_ij|_S + O(ρ⁴), and its other parts are O(ρ⁴). By Step 6 of the proof of [[thm:own-continuation]],
h|_S = Σ|_S + h_R|_S with h_R|_S ∈ ρ^(a+1) L²_b, a + 1 > ℓ0 > 3, and Σ|_S = Σ_(p∈Π) ρ^p F_p(1 + (f − v1)ρ, x̂): the
exponent 5/2 arises only from p = 5/2, with coefficient F_(5/2)(1, x̂). By [[eq:own-2f1]] at p = 5/2, harmonic by
harmonic F_(5/2)(1) = G_(5,l)(v1) ₂F₁(5/2 + l, ½ − l; 2; ½), and since (a + b + 1)/2 = 2 = c, Gauss's second summation
theorem [DLMF, (15.4.28)], F(a, b; ½a + ½b + ½; ½) = √π Γ(½a + ½b + ½)/(Γ(½a + ½) Γ(½b + ½)), gives [[eq:own-transfer]].
1/Γ vanishes only at the nonpositive integers; (2l + 7)/4 > 0, and (3 − 2l)/4 = −n would need 2l = 3 + 4n: T(l) ≠ 0.
G_5(v1) = G_5^∞ by [[prop:own-tail]] (a), as v1 ≥ v_end + 2. Off the exceptional set the spatial part of G_5^∞ is
nonzero, hence so is a_(5/2). Suppose γ − γ_b0 = ρ² b_2 + ρ³ b_3 + ψ on S near spatial infinity, with ψ in ρ^(ℓ0) H^∞_b,
ℓ0 > 5/2. Take a component and a harmonic at which a_(5/2) ≠ 0, and q ∈ (5/2, min(ℓ0, 3)). Projected there,
ρ² c + ρ^(5/2) a_(5/2) lies in ρ^q L²_b(dρ/ρ) near ρ = 0, c being the difference of the ρ² coefficients, since every
other term lies there. But if c ≠ 0 its modulus is at least |c|ρ²/2, and otherwise it is |a_(5/2)| ρ^(5/2); in either
case ∫_0 |ρ^(−q)(ρ² c + ρ^(5/2) a_(5/2))|² dρ/ρ = ∞, as q > 5/2. ∎

*Proof of [[thm:own-data]].* *The order k_P.* By [[cor:own-p-order]] the solution g_λ is the same at every order, and
the proof uses its bounds at the order k_P = 2k1 + 14 at four places, each of which needs at most k_P. (a)
[[lem:own-sigma-data]] (a) applies [[lem:own-e-flux]] (1) with i = 0 and |β| ≤ 2k1 + 10, which needs
i + |β| ≤ k_P − 4. This is the largest demand: [[lem:own-sigma-data]] (b) bounds the Cartesian derivatives of order at
most k1 + 4 of Σ̂_p, which cost ‖G_(2p)(v1)‖ in C^(2(k1+4)+2) = C^(2k1+10) by [[lem:own-self-similar]], and k1 + 4 is
the order to which Σ enters: through the coefficients ∂^j Γ^γ Σ, j ≤ 2, |γ| ≤ k1, of [[eq:own-commuted]]; through the
residual Π_i (Γ_i + c_i) P(Σ), |α| ≤ k1, whose bound in [[prop:far-residual]] uses jets of order |α| + 2; and through
the Taylor remainders of [[lem:own-n-data]] (ii), which use (s, x̂)-derivatives of F_p of order at most
m_p + k1 + 1 ≤ k1 + 4, costing at most 2(m_p + k1 + 1) + 2 ≤ 2k1 + 10 angular derivatives of the data. (b)
[[lem:own-e-flux]] needs k_P ≥ j + 5, used at j = k1 in [[lem:own-n-data]] (ii), with [[eq:own-p-iii]] at order k_P and
[[eq:own-poly]] at n = k_P − 4, which [[cor:own-p-order]] and [[prop:own-poly]] give. (c) Part (2) below uses the
conclusions of [[thm:uniform-existence]] on Ω′ at an order at least J + 3, J := d_1 + 10; and k_P ≥ 2d_1 + 22 ≥ J + 3,
as k1 ≥ d_1 + 4. (d) [[prop:own-far-order]], [[prop:own-near-order]] and [[cor:own-p-order]] need k_P ≥ 6. The number
K + 4 + ⌈4β0(k_P)⌉ of stages is the N_(k_P) of [[prop:own-near-order]], and K* of [[eq:own-kstar]] does not involve k_P:
rotations cost no power of λ in [[eq:own-p-iii]] and [[eq:own-poly]], so the angular order changes only the constants
and the thresholds λ_P(K, k_P), λ_F(k_P) and λ_0 below.

*The threshold.* Let λ_2 be at most the thresholds λ_P(K, k_P) of [[cor:own-p-order]], λ_F(k_P) of
[[prop:own-far-order]], λ_0 of [[prop:own-poly]] at n = k_P − 4, and those of [[lem:own-sigma-data]],
[[lem:own-truncation]] and [[thm:own-continuation]]; none depends on whether G_5^∞ vanishes.

(1) [[thm:own-continuation]] gives the continuation g to W, smooth, G-invariant, in the wave-map gauge relative to g_b0,
joining g_λ smoothly across ℋ; [[prop:own-vacuum]] shows that it is vacuum. On W, |g − g0| ≤ |Σ| + |h_R| ≤
C(λ + ε_B)(v1 − τ)⁻² by [[lem:own-sigma-data]] and [[eq:own-pointwise]] (r ≥ v1 − τ > 0 on W and a ≥ 3/2), and the same
for the inverse; with g := g_λ on Z_b, [[lem:interior-far-part]] (iv) (b) with ν := λ + ε_B shows that all of W but a
strip along ℋ of v-width O(λ + ε_B) lies in D⁻(S; g), and ε_B → 0 with λ. g satisfies the hypotheses of
[[prop:own-uniqueness]] for every a_0 ∈ (0, ½): |h| ≤ 1/50 by Step 1 of the proof of [[thm:own-continuation]], its
energies of weight a_0 are bounded by those of weight a, uniformly in σ, and tend to 0 as σ → −∞ (for Σ as in the proof
of [[prop:own-uniqueness]]); so it is the only continuation in that class.

(2) On S, Step 6 of the proof of [[thm:own-continuation]] gives the class and ‖·‖_(d_1) ≤ C(λ + ε_B). On
Σ^IVP ∩ {r_♭ ≤ r ≤ 4R}, which [[lem:vii-1-2]] (b) places in the interior of Ω′_+, the data are those of g_λ. On Ω′,
g_λ satisfies the conclusions of [[thm:uniform-existence]] at the regularity k_P, 𝒩_(k_P) ≤ M_(k_P) λ^K
([[cor:own-p-order]]). The proof of [[lem:vii-1-1]], run for this solution with the energy order k_P in place of K and
with J := d_1 + 10, applies, as k_P ≥ J + 3 and K ≥ J + 4: |∂^j(g_λ − g_b0)| ≤ C λ on Ω′_+ for j ≤ J. As in the proof
of [[cor:vii-2-3]], the data differ there from (γ_b0, k_b0) by C λ in C^(d_1+4). The data are smooth across r = 4R, g
being smooth there, and satisfy the constraint equations ([[prop:own-vacuum]]). The norm of [[sec:s27-class]] with
ℰ_0 = ℰ_0^½ is bounded, as in the proof of [[lem:vii-0-1]], by C_R times the C^(d_1+3)-norm of the deviation on the
compact set Σ^IVP ∩ {r_♭ ≤ r ≤ 4R} plus its norm on S, which Step 6 of the proof of [[thm:own-continuation]] bounds.
So ‖·‖_(d_1) ≤ C(λ + ε_B) < ε for λ ≤ λ_2.

(3) The data are G-invariant (g is), vacuum, in the half-integer class and below the thresholds of [[prop:vii-3-2]] and
[[cor:s27-rate]]. By [[thm:own-half-settling]] they have a G-invariant vacuum development settling to g_(m′,0)
with |m′ − μ_end| < ε_m (b₀ = (μ_end, 0)) at the rate O(t_*^(−2−ε_t)) of [[eq:s27-rate]] on
{r_♭ ≤ r ≤ R′, t_* ≥ T′}; this development embeds in the maximal vacuum development of (γ, k), which therefore
settles in the same sense. No gluing is used, and no value of λ ∈ (0, λ_2] is excluded: [[prop:own-transfer]] shows
only that, off the exceptional set of [[prop:own-tail]] (d), the half-integer class is needed. ∎
