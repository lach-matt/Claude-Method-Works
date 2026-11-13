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
R is the radius of [[lem:vii-1-2]], taken as in [[ch:interior]] (4R ≥ 20R₁); for r ≥ R_3 the initial surface is a graph Σ^IVP = {τ = f(r)}, with f′ ∈ |x|⁻² C^∞ near infinity ([[lem:interior-where]] (ii), the function F there). G = O(2) × O(2) acts by (t, x) ↦ (t, Ox) ([[sec:s27-class]]).

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

We use the far part of Σ^IVP and its past domain of dependence as they are set up before [[lem:interior-far-part]],
writing f for F, S for Σ_far, N for H₁, Z_b for the set Z there (Z denotes a vector field below) and 𝔪 for m = μ r⁻².
So S = Σ^IVP ∩ {r ≥ 4R} = {τ = f(r), r ≥ 4R}, τ_S := f(4R), v1 := 4R + τ_S is the value of v on ∂S,
τ_max := sup_(r≥4R) f, and

    t̃ := τ − f(r),     W := {v ≥ v1, t̃ ≤ 0, r ≥ 4R},     N := W ∩ {v = v1},
    Σ̃_σ := W ∩ {t̃ = σ} (σ ≤ 0),     s := (v − v1)/r,     W_T := W ∩ {t̃ ≥ T}.                         {#eq:own-wedge}

Σ̃_0 = S. On r ≥ 4R, 0 < f′ ≤ ¼ and 𝔪 ≤ 1/400, f is bounded, |f| ≤ C_f, and v1 − τ_max > 0. By
[[lem:interior-far-part]]: W = D⁻(S; g_b0), with boundary S, N and past null infinity at v ≥ v1, and r ≥ v1 − τ on W
(i); N and the strip {v1 ≤ v ≤ v1 + ½, r ≥ 4R} lie in Ω′ ∪ P′, and v1 ≤ V′_P − κ_P − 1 − m_Ω with m_Ω ≥ 3 (ii); for a
metric on W ∪ Z_b equal to g_λ on Z_b and within C_W ν (v1 − τ)⁻² of g0 on W, all of W but a strip along N of v-width
O(λ + ν) lies in the domain of dependence of S ((iv) (b)); and for v ≥ v1 nothing comes in at past null infinity:
r^(3/2)(g_λ − g0) → 0 as r → ∞ at fixed v ∈ [v1, V′_P) and x̂ (v). Two further facts about W are used.

**Lemma {#lem:own-wedge}** (the geometry of W). (a) The conormals α̂ := d(r − 2t̃) and β̂ := d(r + 2t̃) satisfy

    g_b0⁻¹(β̂, β̂) = (2f′ − 3)(2f′ + 1) − 𝔪(1 + 2f′)²,
    g_b0⁻¹(α̂, α̂) = (2f′ − 1)(2f′ + 3) − 𝔪(3 + 2f′)²,                                              {#eq:own-cones}

both at most −7/4, with β̂(∂_τ) = 2 and α̂(∂_τ) = −2; |α̂|_E², |β̂|_E² ≤ 25/4 and g_b0⁻¹(dt̃, dt̃) ≤ −15/16.
(b) On W, s ∈ [0, 5/4] and |τ − v1| ≤ r. Each Σ̃_σ is {r ≥ r_σ} along the rays τ = f(r) + σ, r_σ being the solution of
r + f(r) = v1 − σ, and r_σ ≥ c_W (1 + |σ|) for some c_W > 0.

*Proof.* (a) These are the contractions of the proof of [[lem:interior-far-part]] (i) ((2f′ − 3)(2f′ + 1) =
−3 − 4f′ + 4f′², (2f′ − 1)(2f′ + 3) = −3 + 4f′ + 4f′²), and |α̂|_E², |β̂|_E² = 4 + (1 ± 2f′)². (b) On W, v − v1 = τ + r −
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
After the shell every oscillating profile vanishes ([[lem:interior-far-part]] (v)) and μ = μ_end. The forcing terms of the stage
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

### The subtracted expansion and the data on N {#sec:own-sigma}

**Lemma {#lem:own-self-similar}** (self-similar solutions of the flat equation). Let p ∈ {2, 5/2, 3, 7/2, 4} and let G be a
smooth symmetric tensor field on S³ (Cartesian components). There is exactly one F(s, x̂), smooth on [0, 3/2] × S³ up to
s = 0, with F(0, ·) = G, such that r^(−p) F((v − v1)/r, x̂) solves □_η = 0 on {0 ≤ s ≤ 3/2}. Harmonic by harmonic,

    F = Σ_l G_l ₂F₁(p + l, p − l − 2; p − ½; s/2),                                                   {#eq:own-2f1}

G_l the part of degree l of each Cartesian component of G, and for every i and β,
sup_(0≤s≤3/2) |∂_s^i Ω^β F| ≤ C_(i,β) ‖G‖_(C^(2i+|β|+2)(S³)), with C_(i,β) depending on p, i and β only.

*Proof.* In the coordinates (v, r, x̂), with s = (v − v1)/r, ∂_v s = r⁻¹ and ℓs = −s/r, [[eq:wave-operator-vr]] at μ = 0
gives, for G_l of degree l (Δ̊ G_l = −l(l + 2) G_l),

    □_η (r^(−p) F(s) G_l) = −2 r^(−p−2) G_l [ (s − s²/2) F″ + (p − ½)(1 − s) F′ − ½(p² − 2p − l(l + 2)) F ].

With y := s/2 the bracket vanishes exactly when y(1 − y) F_yy + (p − ½)(1 − 2y) F_y − (p² − 2p − l(l + 2)) F = 0, the
hypergeometric equation [DLMF, (15.10.1)] with a = p + l, b = p − l − 2, c = p − ½ (a + b + 1 = 2p − 1,
ab = p² − 2p − l(l + 2)). Its exponents at y = 0 are 0 and 1 − c = 3/2 − p < 0; c is not a nonpositive integer, so the
solutions bounded at y = 0 are the multiples of ₂F₁(a, b; c; y), analytic for |y| < 1. This gives existence and
uniqueness harmonic by harmonic, and [[eq:own-2f1]] once the sum converges.

*Bounds uniform in l.* Let φ := ₂F₁(a, b; c; y) on [0, ¾], c ≥ 3/2, and suppose κ² := −ab = (l + 1)² − (p − 1)² > 0. Then
y(1 − y) φ″ + c(1 − 2y) φ′ + κ² φ = 0, and 𝓔 := y(1 − y) φ′² + κ² φ² satisfies 𝓔′ = (1 − 2y)(1 − 2c) φ′². On [0, ½],
𝓔′ ≤ 0; on [½, ¾], 𝓔′ ≤ (2c − 1)(2y − 1) 𝓔/(y(1 − y)) ≤ (16/3)(2c − 1)(2y − 1) 𝓔, whose integral over [½, ¾] is (2c − 1)/3.
So 𝓔 ≤ e^((2c−1)/3) 𝓔(0) = e^((2c−1)/3) κ², and |φ| ≤ e^((2c−1)/6) on [0, ¾]. By [DLMF, (15.5.1)],
∂_y ₂F₁(a, b; c; y) = (ab/c) ₂F₁(a + 1, b + 1; c + 1; y), and (a + 1, b + 1, c + 1) is the triple of p + 1 in place of p;
so ∂_y^i φ is a product of i factors (a + n)(b + n)/(c + n), each at most (l + p + n)², with the function of p + i, which
the energy bound controls for (l + 1)² > (p + i − 1)². For the finitely many other l, ₂F₁ is a fixed smooth function on
[0, ¾]. Hence |∂_y^i ₂F₁| ≤ C_i (1 + l)^(2i) on [0, ¾]. The rotations Ω_ab preserve the harmonics of degree l, with
‖Ω_ab Y‖_(L²) ≤ (l(l + 2))^(1/2) ‖Y‖_(L²) (as Σ_(a<b) Ω_ab² = Δ̊), and a harmonic of degree l has
‖Y‖_∞ ≤ C(1 + l)‖Y‖_(L²), the space having dimension (l + 1)². So
|∂_s^i Ω^β F| ≤ C Σ_l (1 + l)^(2i+|β|+1) ‖G_l‖_(L²) ≤ C ‖G‖_(H^(2i+|β|+2)) ≤ C ‖G‖_(C^(2i+|β|+2)), by the Cauchy–Schwarz
inequality with Σ_l (1 + l)⁻² < ∞. The series converges with all derivatives, and F is smooth on [0, 3/2] × S³. ∎

Such an F extends smoothly to s ∈ (−1, 2), with the same bounds, by a reflection extension in s across s = 0; the
extension does not solve the equation for s < 0, and only its values on s ≥ 0 are used below.

**Definition {#def:own-sigma}** (the subtracted expansion). Let Π := {2, 5/2, 3, 7/2, 4}. For p ∈ Π let F_p be the
solution of [[lem:own-self-similar]] with F_p(0, ·) = G_(2p)(v1, ·), the coefficient of r^(−p) of g_λ − g0 at v = v1
([[prop:bondi-hierarchy]]), and put

    Σ_p := r^(−p) F_p(s, x̂),     Σ := Σ_(p∈Π) Σ_p,     h_R := g − g_b0 − Σ,                              {#eq:own-sigma}

for a metric g on W. All five Σ_p solve □_η Σ_p = 0: this is the second choice of Σ_4 in Section [[sec:far-homogeneity]]
(□_η Σ_4 = 0), for which [[prop:far-residual]] gives |Π_i (Γ_i + c_i) P(Σ)| ≤ C_α λ r⁻⁶ and [[cor:far-kernels]] the
kernel ρ(σ) = C λ (1 + |σ|)^(a−4).

**Lemma {#lem:own-sigma-data}** (the size of Σ). Under the hypotheses of [[thm:own-data]], for λ small:
(a) ‖G_(2p)(v1)‖_(C^(2k1+10)(S³)) ≤ C λ for p ∈ Π, and ‖G_5(v1)‖_(C^m(S³)) = O(λ^n) for all m, n;
(b) Σ_p = λ Σ̂_p, where every Cartesian derivative of order at most k1 + 4 of Σ̂_p is bounded on
{r = 1, 0 ≤ s ≤ 3/2} independently of λ; hence on W ∩ {r ≥ 1}, |∂^j Σ_p| ≤ C_j λ r^(−p−j) and |Γ^α Σ_p| ≤ C_α λ r^(−p)
for j, |α| ≤ k1 + 4;
(c) Σ is G-invariant.

*Proof.* (a) By [[eq:own-e-expansion]], G_(2p)(v1) = Σ_j λ^j M_(j,2p)(v1) + e_(2p)(v1). The first sum consists of smooth
fields independent of λ times λ^j, j ≥ 1. For the second, [[lem:own-e-flux]] (1) with i = 0 and |β| ≤ 2k1 + 10 =
k_P − 4 gives |Ω^β e_(2p)(v1)| ≤ C λ^(1+). G_5(v1) = G_5^∞ ([[prop:own-tail]] (a), v1 ≥ v_end + 2), and the proof of
[[prop:own-tail]] (c) holds with every x̂-derivative, a_1 and a_3 depending smoothly on x̂ through smooth factors.
(b) On {r = 1, 0 ≤ s ≤ 3/2} a Cartesian derivative of order j of r^(−p) F_p(s, x̂) is a combination, with bounded
coefficients, of ∂_s^i Ω^β F_p with i + |β| ≤ j; by [[lem:own-self-similar]] these are at most C ‖G_(2p)(v1)‖_(C^(2j+2)),
which is O(λ) for j ≤ k1 + 4 by (a). The bounds on W ∩ {r ≥ 1} follow by the homogeneity of Σ_p of degree −p under the
dilation of Section [[sec:far-homogeneity]], which maps {r = 1, 0 ≤ s ≤ 3/2} onto {r = ς, 0 ≤ s ≤ 3/2}, together with
[[lem:own-wedge]] (b). (c) g_λ is G-invariant (item 5 of [[thm:past-construction]]; T² × Z2 × Z2 is G), so are the
coefficients of its expansion, and the equation of [[lem:own-self-similar]] commutes with G. ∎

**Lemma {#lem:own-n-data}** (the remainder on N and on the band). Let 𝒰 := (P′ ∪ Ω′) ∩ {v1 ≤ v ≤ V′_P − h_P(τ)} ∩ W,
on which g_λ is defined, and put h_R := g_λ − g_b0 − Σ there.
(i) At fixed λ, every Γ^α h_R is O(r^(−9/2)) on 𝒰, with constants depending on λ and α; on N, Γ^α h_R and its
derivatives along the spheres are O(r^(−9/2)) and its derivative along ℓ is O(r^(−11/2)).
(ii) Let a ∈ (0, 7/2). Near N, h_R = e_(8) + Σ_j λ^j m_(j,8) − Σ_rem, where Σ_rem is Σ minus the terms of order at most
4 of its expansion at fixed v; for |α| ≤ k1, Γ^α Σ_rem and its first derivatives are O(λ r^(−9/2)) there, its derivatives
along ℓ and along the spheres O(λ r^(−11/2)). If K > K*(a, M, k1) as in [[thm:own-data]], then
𝔉_N^a[Γ^α h_R] ≤ C(λ² + ν(λ)) for |α| ≤ k1, with ν(λ) → 0 as λ → 0.
(iii) The flux through N ∩ {T ≤ t̃ ≤ σ} of the weighted energy of Γ^α h_R for a metric g with |g − g_b0| ≤ C r⁻² is at
most C 𝔉_N^a[Γ^α h_R], and beyond r = ϱ it is at most C(λ) ϱ^(2a−7) for a < 7/2.

*Proof.* (i) On 𝒰, v > v_end, so g_λ − g_b0 = g_λ − g0 = Σ_(k=4)^9 r^(−k/2) G_k + u_9 ([[prop:bondi-hierarchy]], G_3 = 0
there). After the shell the coefficients G_k with k ≤ 9 obey the flat recursion [[eq:own-flat-recursion]], by the count in
the proof of [[lem:own-means]] applied to the forcing of [[prop:bondi-hierarchy]]: with G_3 = 0 and μ constant,
∂_v G_4 = 2S_3 = 0 and ∂_v G_5 = S_(7/2) = 0 ([[prop:own-tail]] (a)), so every forcing term is O(r⁻⁶). On the other side,
at fixed v ∈ [v1, V′_P], Taylor's formula in s = (v − v1)/r gives r^(−p) F_p(s) = Σ_(m<m₀) r^(−p−m) ∂_s^m F_p(0)(v − v1)^m/m! +
O(r^(−p−m₀)), with derivatives; since □_η(r^(−p) F_p) = 0, the coefficients of r^(−q) of this expansion solve the same
recursion (by [[eq:own-box-p]] at μ = 0, order by order), and at v = v1 they equal F_q(0) = G_(2q)(v1). The recursion
fixes the coefficient of r^(−q) at v from its value at v1 and the coefficient of r^(−q+1); so the coefficients of
r^(−k/2), k ≤ 8, of g_λ − g_b0 and of Σ agree on 𝒰, and h_R = O(r^(−9/2)) there with all derivatives. On N, s = 0, Z = rℓ
(Z = (v − v1)∂_v + rℓ in (v, r, x̂)) and Ω are tangent, ∂_t = ∂_v; the ℓ-gain of u_9 ([[prop:bondi-hierarchy]]) and of
the explicit terms give the last claim.

(ii) At fixed v, g_λ − g_b0 = Σ_(k=4)^8 r^(−k/2) G_k + u_8, and by (i) the coefficients of order at most 4 of Σ are the
G_(2q), q ≤ 4; so h_R = u_8 − Σ_rem, and u_8 = e_(8) + Σ_j λ^j m_(j,8) by [[eq:own-e-expansion]]. Σ_rem is the sum over
p ∈ Π of r^(−p) times the Taylor remainder of F_p in s at the order m_p := ⌊4 − p⌋ + 1, which is O(λ s^(m_p)) with every
derivative of order at most k1 + 1 in (s, x̂) by [[lem:own-sigma-data]], and p + m_p ≥ 9/2; ℓ = ∂_r at fixed v and r⁻¹Ω
gain r⁻¹ on it, while ∂_t = ∂_v and Z = (v − v1)∂_v + rℓ keep its order. So 𝔉_N^a[Γ^α Σ_rem] ≤ C λ² ∫ r^(2a−11+3) dr
≤ C λ² for a < 7/2. The means' part Σ_j λ^j m_(j,8) has, by [[lem:own-means]], λ-independent coefficients with the
ℓ-gain, and flux O(λ²). The part e_(8) has flux ν(λ) → 0 by [[lem:own-e-flux]] (2) with j = k1.

(iii) N = {v = v1} is null for g_b0, and the flux of T_(g_b0)[φ](X, −∇v), X = w∂_t, through it contains only ℓφ and the
derivatives along the spheres, with bounded coefficients; w ≤ C r^(2a) on N. For g = g_b0 + H the difference of the
integrands is at most C|H| w |∂φ|², which the last term of [[eq:own-flux-n]] bounds. The tail: by (i), at fixed λ the
integrand of [[eq:own-flux-n]] for Γ^α h_R is O(r^(2a−11+3)), and its integral beyond ϱ is C(λ) ϱ^(2a−7)/(7 − 2a). ∎

### The continuation to the far part's past domain of dependence {#sec:own-continuation}

*Setting.* Fix ℓ0 ∈ (3, 4) ∖ {7/2}, a ∈ (ℓ0 − 1, 3) and k1 := max(8, d_1 + 4). On W we use the Kerr–Schild Cartesian
coordinates (t, x), t = τ, and P(h) := Ric^H(g_b0 + h; g_b0), which is the operator [[eq:gauge]] relative to g0 there
(g0 = g_b0 on v ≥ v_end). Put u := t − r, u* := τ_max + 1 and w := (u* − u)^(2a); on W, t ≤ f(r) ≤ τ_max and t − v1 ≥ −r,
so r + 1 ≤ u* − u ≤ 2r + |u* − v1|. The commutators are Γ ∈ {∂_t, L_Ω_ab, Z}, Z := (t − v1)∂_t + x·∂_x, acting on
Cartesian components; for a multi-index α, Γ^α is the product. For a metric g = g_b0 + H on W, |·| denotes the Euclidean
operator norm of a component matrix, and for a function φ and σ ≤ 0,

    E_σ[φ] := ∫_(Σ̃_σ) √|g| T_g[φ](X, −∇t̃) d⁴x,     X := w ∂_t,
    𝔈_k(σ) := Σ_(|α|≤k) Σ_(i≤j) E_σ[(Γ^α h_R)_ij],     h_R := g − g_b0 − Σ,                                {#eq:own-energies}

T_g[φ] := dφ ⊗ dφ − ½ g g⁻¹(dφ, dφ) the energy-momentum tensor of φ for g, d⁴x the coordinate measure of x on Σ̃_σ, and
𝔉_k the corresponding fluxes through N ∩ {T ≤ t̃ ≤ σ}. On Σ̃_σ, d⁵x = dt̃ d⁴x.

**Lemma {#lem:own-margins}** (margins). Let 𝔪 ≤ 1/16 and |f′| ≤ ¼, and s_0 := 1/16 + (1 + 1/256)^(1/2) ≤ 1.0645, which
bounds |g_b0| and |g_b0⁻¹|.
(a) If |H| ≤ η_H < 1/s_0, then |g⁻¹ − g_b0⁻¹| ≤ s_0² η_H/(1 − s_0 η_H): at most 0.0232 for η_H = 1/50, at most 0.0474 for
η_H = 1/25, and at most 0.2845 r⁻² for η_H = r⁻²/4 on r ≥ 8.
(b) If |g⁻¹ − g_b0⁻¹| ≤ c < 7/25 on a region of {r ≥ 4R}, then there g⁻¹(α̂, α̂), g⁻¹(β̂, β̂) ≤ −7/4 + (25/4)c < 0
([[eq:own-cones]]), |g − g_b0| ≤ s_0² c/(1 − s_0 c) ≤ 0.4520, g(∂_t, ∂_t) < −0.485, and g⁻¹(dt̃, dt̃) ≤ −15/16 + (17/16)c ≤
−0.64. So the slices Σ̃_σ are spacelike, ∂_t is timelike, r − 2t̃ decreases and r + 2t̃ increases along future causal
curves, with margins depending on c only.
(c) If |g⁻¹ − g_b0⁻¹| ≤ r⁻²/2 on {r ≥ 4R}, then Φ_W := v + 1/r is a time function there: g⁻¹(dΦ_W, dΦ_W) ≤ −r⁻² + r⁻⁴ < 0
and dΦ_W(∂_t) = 1.
(d) If |H| ≤ 1/50, there are absolute constants c_1, c_2 > 0 with c_1 w |∂φ|² ≤ √|g| T_g[φ](X, −∇t̃) ≤ c_2 w |∂φ|².
(e) If |H| ≤ min(1/50, 𝔪/2), then −∇u and ∂_t are future causal for g, and T_g[φ](∇w, ∂_t) = |w′| T_g[φ](−∇u, ∂_t) ≥ 0.

*Proof.* The (t, r) block of g_b0 is [[−1 + 𝔪, 𝔪], [𝔪, 1 + 𝔪]] (dv = dt + x̂·dx) and that of g_b0⁻¹ is
[[−1 − 𝔪, 𝔪], [𝔪, 1 − 𝔪]], both with eigenvalues of largest modulus 𝔪 + (1 + 𝔪²)^(1/2) ≤ s_0; on the orthogonal
directions both are the identity. (a) is the Neumann series for (g_b0 + H)⁻¹, and the numbers follow from s_0 ≤ 1.0645
(s_0² ≤ 1.1332). (b) |α̂|_E², |β̂|_E² ≤ 4 + 9/4 = 25/4 and |dt̃|_E² = 1 + f′² ≤ 17/16, and [[lem:own-wedge]] (a) gives the values for g_b0; |g − g_b0| ≤ s_0² c/(1 − s_0 c) is (a) with the roles exchanged, at most
0.4520 at c = 7/25, and g_b0(∂_t, ∂_t) = −1 + 𝔪 ≤ −15/16. (c) dΦ_W = dv − r⁻² dr, and with g_b0⁻¹(dv, dv) = 0,
g_b0⁻¹(dv, dr) = 1, g_b0⁻¹(dr, dr) = 1 − 𝔪, g_b0⁻¹(dΦ_W, dΦ_W) = −2r⁻² + r⁻⁴(1 − 𝔪); |dΦ_W|_E² = 1 + (1 − r⁻²)² ≤ 2, so
the perturbation adds at most r⁻². (d) For two future timelike vectors X and n of g the form p ↦ T_g[p](X, n) is
positive definite: in a g-orthonormal frame with X a positive multiple of e_0 and n a positive multiple of
cosh s e_0 + sinh s e_1 it is, up to positive factors, ½ cosh s (p_0² + p_1²) + sinh s p_0 p_1 + ½ cosh s Σ_(i≥2) p_i²,
with eigenvalues ½e^(±s) and ½ cosh s. By (a) and (b) with c = 0.0232, ∂_t and −∇t̃ are future timelike with margins,
and (g, f′, x̂) range over a compact set; so the form is bounded above and below by positive multiples of |p|_E², and
√|det g| lies between positive constants (det g_b0 = −1). (e) g_b0⁻¹(du, du) = −1 − 𝔪 − 2𝔪 + 1 − 𝔪 = −4𝔪 and |du|_E² = 2;
by (a), |g⁻¹ − g_b0⁻¹| ≤ 0.59 𝔪 for |H| ≤ 𝔪/2, so g⁻¹(du, du) ≤ −2.8𝔪 < 0, and g(−∇u, ∂_t) = −du(∂_t) = −1 < 0. w′ =
−2a(u* − u)^(2a−1) < 0, so ∇w = |w′|(−∇u), and the energy-momentum tensor is nonnegative on pairs of future causal
vectors. ∎

**Lemma {#lem:own-energy-identity}** (the energy identity). For every metric g, every function φ and X = w(u)∂_t,

    ∇_a(T_g[φ]^a_b X^b) = (□_g φ) Xφ + T_g[φ](∇w, ∂_t) + ½ w T_g[φ]^(ab) ∂_t g_ab,                              {#eq:own-energy-identity}

and g^(ab)∂_a∂_b φ = □_g φ + g^(ab) Γ[g]^c_ab ∂_c φ.

*Proof.* ∇_a T^a_b = (□_g φ) ∂_b φ, and T^(ab)∇_a X_b = ½ T^(ab)(ℒ_X g)_ab with (ℒ_(w∂_t) g)_ab = w ∂_t g_ab + ∂_a w g_(tb) +
∂_b w g_(at). The second formula is the definition of □_g in coordinates. ∎

**Lemma {#lem:own-rays}** (estimates along the rays of Σ̃_σ). Let σ ≤ 0. Along a ray r ↦ (f(r) + σ, r x̂) of Σ̃_σ,
d/dr = x̂·∂_x + f′ ∂_t.
(a) For every function ψ and every c, ∂_i ψ = r⁻¹ x̂_i (Zψ − (t − v1)∂_t ψ) − r⁻² x_j Ω_ij ψ, and

    d/dr (∂_c ψ) = r⁻¹ ∂_c(Zψ) − r⁻¹(t − v1) ∂_c(∂_t ψ) + f′ ∂_c(∂_t ψ) − r⁻¹ ∂_c ψ.                       {#eq:own-ray-derivative}

So on W (|t − v1| ≤ r, [[lem:own-wedge]] (b)) every second derivative of ψ, and the r-derivative along the ray of
every first derivative, are combinations with coefficients bounded by 1 + 4/r of first derivatives of Γψ, Γ ∈ {∂_t, Z,
Ω}, and of r⁻¹ ∂ψ.
(b) If ∫_(r_σ)^∞ r^(2a+3)(F² + (dF/dr)²) dr < ∞ on almost every ray, with F := Ω^γ ∂ψ, then for R′ ≥ r_σ

    ∫_(S³) R′^(2a+3) |F(R′, ω)|² dω ≤ 2 ‖r^(a+3/2) F‖ ‖r^(a+3/2) dF/dr‖,                                     {#eq:own-s1}

the norms in L²([R′, ∞) × S³, dr dω).
(c) If φ → 0 at spatial infinity along the rays and ∫^∞ r^(2a+3)(dφ/dr)² dr < ∞, then

    ∫_(r_σ)^∞ r^(2a+1) φ² dr ≤ (a + 1)⁻² ∫_(r_σ)^∞ r^(2a+3) (dφ/dr)² dr,     r^(2a+2) φ(r)² ≤ (2a + 2)⁻¹ ∫_r^∞ s^(2a+3) (dφ/ds)² ds.
                                                                                                    {#eq:own-hardy}

*Proof.* (a) x_j Ω_ij = x_i (x·∂) − r² ∂_i and x·∂ = Z − (t − v1)∂_t; and Z∂_c = ∂_c Z − ∂_c, as [Z, ∂_c] = −∂_c.
(b) On [R′, R″], R′^(2a+3)𝐅(R′)² = R″^(2a+3)𝐅(R″)² − ∫ ((2a + 3) r^(2a+2) 𝐅² + r^(2a+3) d(𝐅²)/dr) dr, with
𝐅(r)² := ∫_(S³) |F(r, ω)|² dω; drop the nonpositive term and use Cauchy–Schwarz. Since ∫ r^(2a+3) 𝐅² dr < ∞,
lim inf r^(2a+4) 𝐅(r)² = 0, and R″ → ∞ along such a sequence removes the boundary term. (c) The second inequality is
φ(r) = −∫_r^∞ dφ/ds ds and Cauchy–Schwarz; so the boundary term r^(2a+2)φ²/(2a + 2) of the integration by parts
∫ r^(2a+1) φ² = [r^(2a+2) φ²/(2a + 2)] − (a + 1)⁻¹ ∫ r^(2a+2) φ φ′ vanishes at infinity, the one at r_σ has the good
sign, and Cauchy–Schwarz gives the first. ∎

These three tools bound the error terms of the energy identity in Section [[sec:far-homogeneity]] (the hypotheses there
on the energy tools and the pointwise bounds are [[lem:own-rays]] and [[eq:own-pointwise]] below).

*The truncated problems.* Extend f from [4R, ∞) to a smooth function F̂ on [a′, ∞) with |F̂′| ≤ ¼ and |F̂| ≤ C_f. For
T ≤ −1 put 𝒮_T := {τ = T + F̂(|x|), |x| ≥ a′}, which is {t̃ = T} on r ≥ 4R, δ_0 := V′_P − κ_P − v1 (≥ 4 by
[[lem:interior-far-part]] (ii)), V_T := V′_P − δ_0/2 − h_P(T − C_f), and let χ_T(v) be smooth, 0 for v ≤ V_T and 1 for
v ≥ V_T + δ_0/4, with derivatives bounded independently of T. The *truncated problem* is the Cauchy problem for
Ric^H(g) = 0 relative to g0 with data (g, ∂_τ g) on 𝒮_T equal to those of (1 − χ_T) g_λ + χ_T(g_b0 + Σ). (Σ is defined on
{v ≥ v1}, which contains the support of χ_T, as V_T ≥ v1 + δ_0/2.)

**Lemma {#lem:own-truncation}** (the truncated problems). There is T_0 such that for T ≤ T_0:
(i) 𝒮_T ∩ {v ≤ V_T + δ_0/4} ⊂ P′, so the data are defined; 𝒮_T is spacelike for g0 and g_λ.
(ii) Every past g_λ-causal curve from a point p ∈ (P′ ∪ Ω′) ∩ {v ≤ v1, τ − F̂(|x|) ≥ T} stays in P′ ∪ Ω′ and meets 𝒮_T at a
point with v ≤ V_T. Hence the solution g_T of the truncated problem equals g_λ on (P′ ∪ Ω′) ∩ {v ≤ v1, τ − F̂ ≥ T}, and
N ∩ {t̃ ≥ T} carries the data of g_λ: no characteristic problem is posed.
(iii) Beyond the band, {v ≥ V_T + δ_0/4} ∩ 𝒮_T, the data are g_b0 + Σ, so h_R and all its first derivatives vanish at
t̃ = T there, ∂_t^j h_R = O(λ r^(−4−j)) for j ≥ 2 with their derivatives, and every Γ^α h_R at t̃ = T is O(λ r⁻⁴), its
first derivatives O(λ r⁻⁵), with constants depending on α and T. On the band, h_R = (1 − χ_T)(g_λ − g_b0 − Σ) and its
first derivatives at t̃ = T are O(r^(−9/2)), with their derivatives along 𝒮_T ([[lem:own-n-data]] (i)).
(iv) g_T exists on W_T ∩ {t̃ ≤ T + δ_T} for some δ_T > 0, with every derivative bounded, and on any W_T ∩ {t̃ ≤ σ′} on which
its derivatives up to a fixed order stay bounded and the margins of [[lem:own-margins]] (b) hold, it continues beyond σ′.
g_T is G-invariant.

*Proof.* (i) On 𝒮_T, τ ≤ T + C_f ≤ τ0 and, where v ≤ V_T + δ_0/4, v + h_P(τ) ≤ V′_P − δ_0/4 + h_P(T + C_f) − h_P(T − C_f),
which is at most V′_P once h_P(T + C_f) − h_P(T − C_f) ≤ 2C_f sup h_P′ ≤ δ_0/4, true for T ≤ T_0. Spacelike: for g0,
g0⁻¹(dτ − F̂′ dr, ·) = −1 + F̂′² − (μ/r²)(1 + F̂′)² < 0 as in [[lem:interior-far-part]] (i); for g_λ, by the margin of
[[lem:past-domain]] (f). (ii) On Ω′, Φ_Ω := v + ε_Ω(τ − τ0), with ε_Ω(τ′_end − τ0) < δ_0/2, is a time function for g0 with
g0⁻¹(dΦ_Ω, dΦ_Ω) = −2ε_Ω − ε_Ω²(1 + 𝔪) < 0 ([[prop:vaidya]] (d)), and for g_λ, |g_λ − g0| ≤ C λ on the compact Ω′, for λ
small; on P′, Φ_P := v + h_P(τ) is a time function for g_λ ([[lem:past-domain]] (b), (f)). A past causal curve leaves
neither Ω′ (its boundaries other than Σ_τ0 are spacelike with Ω′ to their past, [[lem:domain]] (e)) nor P′ (its outer
boundary is spacelike with P′ to its past and r increases along past causal curves at r = a′), and τ → −∞ along a
past-inextendible one in P′, since P′ ∩ {τ ≥ τ1} is compact; as F̂ is bounded, it meets 𝒮_T. Along it, from p with
v(p) ≤ v1: on Ω′, Φ_Ω ≤ v1 + ε_Ω(τ′_end − τ0) < v1 + δ_0/2, so it enters P′ at τ0 with v < v1 + δ_0/2; on P′,
Φ_P ≤ v1 + δ_0/2 + κ_P = V′_P − δ_0/2; at its point q on 𝒮_T, τ(q) ≥ T − C_f, h_P is increasing, and
v(q) ≤ V′_P − δ_0/2 − h_P(T − C_f) = V_T. So p lies in the domain of dependence of 𝒮_T ∩ {v ≤ V_T}, where the data are
those of g_λ, and the uniqueness of the local theory on domains of dependence (Step 8 of the proof of
[[thm:uniform-existence]]) gives g_T = g_λ there. N ⊂ Ω′ ∪ P′ by [[lem:interior-far-part]] (ii). (iii) Beyond the band g_T =
g_b0 + Σ + h_R with h_R = ∂_τ h_R = 0 at t̃ = T, so every derivative of h_R of order at most 1, and every derivative of
h_R or ∂_τ h_R along 𝒮_T, vanishes there; the equation P(Σ + h_R) = 0 then gives ∂_t² h_R = 2(g^(tt))⁻¹ P(Σ), and
differentiating it in t, ∂_t^j h_R = O(λ r^(−4−j)), every ∂_t applied to the homogeneous terms of P(Σ) gaining r⁻¹
([[prop:far-residual]]). As |t − v1| ≤ |T| + C ≤ 2r there and Z = (t − v1)∂_t + x·∂_x, the claim on Γ^α h_R follows. The band:
[[lem:own-n-data]] (i), with h_R = (1 − χ_T)(g_λ − g_b0 − Σ). (iv) Beyond the band the data g_b0 + Σ are smooth with every
derivative bounded, so the local theory of Step 8 of the proof of [[thm:uniform-existence]], applied on the balls of a
fixed radius, gives solutions on a time interval independent of the ball, which agree on overlaps by finite speed of
propagation; the continuation criterion is that of the same local theory. The data are G-invariant (g_λ, Σ
([[lem:own-sigma-data]] (c)), χ_T(v) and F̂(|x|) are), G acts by isometries of g0, and Ric^H is natural
([[lem:far-naturality]]); uniqueness gives the invariance of g_T. ∎

Let σ_1(T) be the supremum of the σ ≤ 0 such that g_T exists on W_T ∩ {t̃ ≤ σ} with every derivative bounded there.

**Lemma {#lem:own-exterior}** (finite and continuous energies). Let σ′ < σ_1(T), and suppose |g_T⁻¹ − g_b0⁻¹| ≤ c < 7/25
on W_T ∩ {t̃ ≤ σ′} ∩ {r ≥ ϱ_0}, where ϱ_0 := max(4R, V_T + δ_0 − T + C_f). Then for every k, 𝔈_k is finite and continuous on
[T, σ′], and the weighted energy of Γ^α h_R, |α| ≤ k, on Σ̃_σ ∩ {r ≥ ϱ} is at most C(T, σ′, k) λ² ϱ^(2a−6) for
ϱ ≥ max(2ϱ_0, 4(σ′ − T)) and every σ ∈ [T, σ′].

*Proof.* For ϱ ≥ ϱ_0 and V_* > 0 let X_(ϱ,V_*) := W ∩ {T ≤ t̃ ≤ σ} ∩ {r − 2(t̃ − T) ≥ ϱ} ∩ {r + 2(t̃ − T) ≤ V_*}, σ ≤ σ′.
It is bounded (r ≤ V_* on it); on it v ≥ T − C_f + ϱ_0 ≥ V_T + δ_0, beyond the band. By [[lem:own-margins]] (b) its two
lateral boundary pieces are spacelike for g_T with X_(ϱ,V_*) to their past, so it is a domain of dependence of its bottom
and the fluxes T_(g_T)[φ](∂_t, n) through the lateral pieces, n their future normals, are nonnegative and are dropped.
Apply [[eq:own-energy-identity]] with w = 1 to φ := (Γ^α h_R)_ij, |α| ≤ k. Its equation is that of [[eq:own-commuted]]
below, whose coefficients are bounded on W_T ∩ {t̃ ≤ σ′} by the definition of σ_1(T) and whose forcing R^α = Π_i(Γ_i + c_i)
P(Σ) is O(λ r⁻⁶) ([[prop:far-residual]]). With e(σ) the sum over |α| ≤ k of the energies and squared L² norms of Γ^α h_R
on the top Σ̃_σ ∩ {r ≥ ϱ + 2(σ − T), r ≤ V_* − 2(σ − T)} (the L² part satisfies d‖φ‖²/dσ ≤ 2‖φ‖‖∂_t φ‖, its lateral
edges moving so as to shrink the top), Gronwall's inequality gives e(σ)^(1/2) ≤ e^(C(σ−T))(e(T)^(1/2) + ∫_T^σ ‖R^α‖),
with C independent of V_* and ϱ. By [[lem:own-truncation]] (iii), e(T) ≤ C λ² ∫_ϱ^∞ r⁻¹⁰ r³ dr = C λ² ϱ⁻⁶, and
‖R^α‖_(L²(r≥ϱ)) ≤ C λ ϱ⁻⁴. Letting V_* → ∞ (monotone convergence), the unweighted energy of Σ̃_σ ∩ {r ≥ ϱ + 2(σ − T)} is
at most C λ² ϱ⁻⁶. On Σ̃_σ, w ≤ (2r + C)^(2a), and for ϱ ≥ max(2ϱ_0, 4(σ′ − T)) the shell {2^j ϱ ≤ r ≤ 2^(j+1) ϱ} lies in
{r ≥ ϱ_j + 2(σ − T)}, ϱ_j := 2^(j−1)ϱ ≥ ϱ_0; so its weighted energy is at most C(2^(j+1)ϱ)^(2a) λ² (2^(j−1)ϱ)⁻⁶, and the
sum over j ≥ 0 is at most C λ² ϱ^(2a−6), as a < 3. 𝔈_k(σ) is the energy of Σ̃_σ ∩ {r ≤ ϱ}, the integral of a smooth
function over a compact set depending continuously on σ, plus this tail, uniformly small in σ: 𝔈_k is finite and is a
uniform limit of continuous functions. ∎

**Theorem {#thm:own-continuation}** (the continuation). Under the hypotheses of [[thm:own-data]] there are λ_2 > 0,
ε_2 > 0 and T_1(λ) such that for 0 < λ ≤ λ_2 the following holds. For T ≤ T_1(λ), g_T exists on all of W_T, and as
T → −∞ the g_T converge in C^k on compact subsets of W, for every k, to a smooth G-invariant metric g on W with
Ric^H(g; g_b0) = 0, which joins g_λ smoothly across N. Its remainder h_R = g − g_b0 − Σ satisfies 𝔈_(k1)(σ) ≤ ε_B² for
σ ≤ 0, with ε_B = ε_B(λ) → 0 as λ → 0, 𝔈_k(σ) ≤ C_k(λ) for every k, and E_σ[Γ^α h_R] → 0 as σ → −∞ for |α| ≤ k1; the
pointwise bounds [[eq:own-pointwise]] hold with ε_B. On S, h_R|_S ∈ ρ^(a+1) H_b^k and ∂h_R|_S ∈ ρ^(a+2) H_b^k
(dρ/ρ dω) for every k, and the data (γ, k) of g on S satisfy γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b, k − k_b0 ∈
H^(∞,(ℰ_0^½+1,ℓ0+1))_b on S, with ‖·‖_(d_1) ≤ C(λ + ε_B) there.

*Proof.* *Step 1 (the bootstrap and the pointwise bounds).* Let T ≤ T_1(λ) (chosen in Step 3), and assume (BA):
𝔈_(k1)(σ) ≤ 4ε_B² on [T, σ*], σ* < σ_1(T), with ε_B ≤ ε_2 to be fixed. Under (BA), for σ ∈ [T, σ*] and r ≥ r_σ,

    |∂ Γ^β h_R| ≤ C_S ε_B r^(−3/2−a)  (|β| ≤ k1 − 3),     |∂∂ Γ^β h_R| ≤ C_S ε_B r^(−3/2−a)  (|β| ≤ k1 − 4),
    |Γ^β h_R| ≤ C_S ε_B r^(−1/2−a)  (|β| ≤ k1 − 3).                                                    {#eq:own-pointwise}

Indeed, by [[lem:own-exterior]] 𝔈_(k1)(σ) is finite; by [[lem:own-margins]] (d), E_σ[φ] ≥ c_1 ∫ r^(2a) |∂φ|² r³ dr dω,
w ≥ r^(2a); and by [[eq:own-ray-derivative]] the ray derivative of F := Ω^γ ∂Γ^β h_R, |γ| ≤ 2, is a combination of
first derivatives of commuted fields of one more order, with no undifferentiated term. So [[eq:own-s1]] with the Sobolev
embedding H²(S³) ⊂ L^∞(S³) gives the first bound with 𝔈_(|β|+3); the second is the first with one more commutation, by
[[lem:own-rays]] (a). Every Γ^β h_R(σ, ·) tends to 0 along Σ̃_σ: at fixed x beyond the band,
|Γ^β h_R(σ, x)| ≤ |Γ^β h_R(T, x)| + (σ − T) sup_[T,σ] |∂_t Γ^β h_R(·, x)|, the first term O(λ r⁻⁶) or 0 and the second
O(r^(−3/2−a)) by the first bound at all times in [T, σ] (with a constant depending on sup 𝔈), the time segment lying in
W_T. So [[eq:own-hardy]] applies, and its second inequality gives the third bound. With [[lem:own-sigma-data]] (b),
|H| ≤ C λ r⁻² + C_S ε_B r^(−1/2−a) ≤ min(1/50, 𝔪/2, r⁻²/4) on W ∩ {t̃ ≤ σ*} for λ ≤ λ_2 and ε_B ≤ ε_2, since a ≥ 3/2;
so [[lem:own-margins]] (a)–(e) apply, with |g_T⁻¹ − g_b0⁻¹| ≤ 0.0232 and ≤ 0.2845 r⁻².

*Step 2 (the commuted equations and the energy inequality).* By [[lem:far-scaling]] (b), differentiated in ς at ς = 1,
(Z + 2)P_μ(h) = DP_μ(h)[Zh] − 2μ∂_μ P_μ(h) for every h; ∂_t P(h) = DP(h)[∂_t h], P being static; and
ℒ_Ω P(h) = DP(h)[ℒ_Ω h] by [[lem:far-naturality]]. Write (Γ + c_Γ)P(h) = DP(h)[Γh] + M_Γ P(h), with c_Z = 2,
M_Z = −2μ∂_μ, and c_Γ = 0, M_Γ = 0 otherwise. Since P(Σ + h_R) = 0, subtracting the identity for Σ gives
DP(H)[Γh_R] = −(Γ + c_Γ)P(Σ) − (DP(H) − DP(Σ))[ΓΣ] − M_Γ(P(H) − P(Σ)); differentiating the identity in h,
(Γ + c_Γ)DP(h)[k] = DP(h)[Γk] + D²P(h)[Γh, k] + M_Γ DP(h)[k], and by induction on |α|

    DP(H)[Γ^α h_R] = −R^α + (A) + (B) + (C),     R^α := Π_i (Γ_i + c_(Γ_i)) P(Σ),                              {#eq:own-commuted}

where (A) is linear in one Γ^β h_R, |β| ≤ |α|, with coefficients built from the Γ^γ Σ (from D^m P(H) with one slot h_R
and the others Σ, m ≥ 2, and from DP(H) − DP(Σ) on Γ^α Σ); (B) has at least two slots h_R, each |α_i| ≥ 1 and
Σ|α_i| ≤ |α|; and (C) is (μ∂_μ)^j DP(H)[Γ^β h_R], j ≥ 1, |β| < |α|. Componentwise DP(H)[k] = −½ g^(ab)∂_a∂_b k +
B(H)·∂k + C(H)k ([[prop:far-coefficients]]). For φ := (Γ^α h_R)_ij, [[eq:own-energy-identity]] on the bounded domain
D_*(σ) := W_T ∩ {t̃ ≤ σ} ∩ {Φ_W ≤ V_*}, σ ≤ σ*, whose boundary consists of Σ̃_σ ∩ {Φ_W ≤ V_*} (future), Σ̃_T ∩ {Φ_W ≤ V_*}
and N ∩ D_*(σ) (past) and {Φ_W = V_*} (future, spacelike by [[lem:own-margins]] (c), with nonnegative flux, dropped), gives

    E_σ[φ] ≤ E_T[φ] + F_N[φ] − ∫∫ √|g| w (□_g φ) ∂_t φ − ½ ∫∫ √|g| w T_g[φ]^(ab) ∂_t g_ab,                    {#eq:own-energy-inequality}

with □_g φ = −2(DP(H)[Γ^α h_R])_ij + 2(B(H)·∂Γ^α h_R)_ij + 2(C(H)Γ^α h_R)_ij − g^(ab)Γ[g]^c_ab ∂_c φ, the bulk term
T_g[φ](∇w, ∂_t) ≥ 0 dropped, the integrals over D_*(σ) and the energies restricted to {Φ_W ≤ V_*}; as V_* → ∞, the left
side increases to E_σ[φ] and the right side converges to its value on the full slices, every integrand being integrable
by [[lem:own-exterior]]. The error terms are bounded by [[cor:far-kernels]], with [[lem:own-rays]] and
[[eq:own-pointwise]] as its tools; in (B), a term of total order at most k1 with at least two slots has its slot of
highest order in L² (an undifferentiated slot through [[eq:own-hardy]], a twice differentiated one through
[[lem:own-rays]] (a)) and the others pointwise by [[eq:own-pointwise]], which is possible since the second-largest order
is at most k1/2 and k1/2 + 4 ≤ k1 for k1 ≥ 8. Summing over |α| ≤ k1 and the components, with the fluxes bounded by
[[lem:own-n-data]] (iii),

    𝔈_(k1)(σ) ≤ C_E [ 𝔈_(k1)(T) + 𝔉_(k1) + ∫_T^σ κ 𝔈_(k1) + ∫_T^σ ρ 𝔈_(k1)^(1/2) ],                             {#eq:own-gronwall}

κ and ρ as in [[eq:far-kernels]] with ρ(σ) = C λ (1 + |σ|)^(a−4) (□_η Σ_4 = 0); ∫ κ ≤ K_κ := C(μ + 1) and
∫ ρ ≤ ρ_∞ := C λ/(3 − a), independent of T.

*Step 3 (closing).* With y(σ) := sup_[T,σ] 𝔈_(k1)^(1/2), Gronwall's inequality gives
y² ≤ C_E e^(C_E K_κ)(𝔈_(k1)(T) + 𝔉_(k1) + 2y ρ_∞), so 𝔈_(k1) ≤ C_*(𝔈_(k1)(T) + 𝔉_(k1) + λ²) on [T, σ*], with C_*
independent of T, λ and ε_B. Put ε_B² := C_*(sup_(T≤T_1(λ)) 𝔈_(k1)(T) + C(λ² + ν(λ)) + λ²). By [[lem:own-n-data]] (ii)
and (iii), 𝔉_(k1) ≤ C(λ² + ν(λ)); by [[prop:far-window]] (ii), the cap energy satisfies 𝔈_(k1)(T) ≤ C(λ)|T|^(2a−6), which
is below λ² for T ≤ T_1(λ), the hypotheses of [[prop:far-window]] on the initial slice and on N being
[[lem:own-truncation]] (iii) and [[lem:own-n-data]] (i). [[pending:issue-2]] So ε_B → 0 as λ → 0, ε_B ≤ ε_2 for λ ≤ λ_2, and 𝔈_(k1) ≤ ε_B² <
4ε_B² on [T, σ*]: (BA) is improved. *Openness.* At σ* the bounds of Step 1 give |H| ≤ 1/50. For x with r ≥ ϱ_0 (the exterior regions of
[[lem:own-exterior]]) and t̃ ∈ [σ*, σ* + δ′], the time segment from (σ*, x) lies in W_T (v increases with t at fixed x, and v > v1 at t̃ = T, r ≥ ϱ_0), and ∂_t H is bounded on W_T ∩ {t̃ ≤ σ′} for
σ′ ∈ (σ*, σ_1(T)); so |H| ≤ 1/25 there for δ′ small, and |g_T⁻¹ − g_b0⁻¹| ≤ 0.0474 < 7/25 by [[lem:own-margins]] (a). The
points of W_T with r ≤ ϱ_0 form a compact set, on which no margin is needed. By [[lem:own-exterior]], 𝔈_(k1) is
continuous on [T, σ* + δ′], and (BA) holds on [T, σ* + δ″] for some δ″ > 0. The set where (BA) holds is therefore open
and closed in [T, σ_1(T)), and contains T. With the bounds of Step 1, the local theory continues g_T beyond any
σ_1(T) < 0: g_T exists on all of W_T, with 𝔈_(k1) ≤ ε_B².

*Step 4 (every order at fixed λ).* For k > k1, induct on k: in the commuted equations at order k the terms of top order
are linear in the order-k quantities, with coefficients bounded by [[eq:own-pointwise]] and its analogues at the orders at
most k − 1 (in (B) the second-largest order is at most k/2, and k/2 + 4 ≤ k − 1 for k ≥ 10), so
[[eq:own-gronwall]] holds at order k with ε_B replaced by C_(k−1)(λ) in the pointwise factors, and Gronwall's inequality
closes without smallness: 𝔈_k ≤ C_k(λ)(𝔈_k(T) + 𝔉_k + λ²), finite and uniform in T by [[lem:own-n-data]] (i), (iii) and
the cap at order k.

*Step 5 (the limit).* For T′ < T ≤ T_1, δ := g_(T′) − g_T on W_T solves the linear system obtained by subtracting the two
equations, with g_(T′) as principal part, −½ g_(T′)^(ab)∂_a∂_b δ = ½(g_(T′)^(ab) − g_T^(ab))∂_a∂_b g_T + (Q(g_(T′))(∂g_(T′),
∂g_(T′)) − Q(g_T)(∂g_T, ∂g_T)), linear in (δ, ∂δ), whose coefficients ∂∂H_T, ∂H_T, ∂H_(T′) give the kernels of
[[cor:far-kernels]]. δ = 0 near N ∩ W_T, where both equal g_λ. On Σ̃_T, δ = h_(R,T′)(T) − h_(R,T)(T): the second is the cap,
and the first is bounded by Step 2 run for g_(T′) on W_(T′) ∩ {t̃ ≤ T}, whose data are tails:
𝔈[h_(R,T′)](T) ≤ C(𝔈(T′) + 𝔉_(k1)(T′, T) + (∫_(−∞)^T ρ)²) =: ϑ(T), with 𝔉(T′, T) ≤ C(λ)|T|^(2a−7) (N ∩ {t̃ ≤ T} lies in
r ≥ |T| − C, [[lem:own-n-data]] (iii)), the cap at most C(λ)|T′|^(2a−6) and ∫_(−∞)^T ρ ≤ C λ |T|^(a−3). So the energy of δ
on W_T is at most C ϑ(T) → 0 as T → −∞, uniformly in T′ < T: (g_T) is a Cauchy family in the energy of weight a on every
W_(T_0), and with the bounds of Step 4 at every order it converges in C^k on compact subsets of W for every k. The limit g
is smooth, solves Ric^H(g; g_b0) = 0, has 𝔈_(k1) ≤ ε_B² and 𝔈_k ≤ C_k(λ) by lower semicontinuity, and
E_σ[Γ^α h_R] ≤ C ϑ(σ) → 0 as σ → −∞. Each g_T is smooth across N and equals g_λ on its side v ≤ v1
([[lem:own-truncation]] (ii)), so g and g_λ join smoothly. G-invariance passes to the limit.

*Step 6 (the class on S).* On S = {t = f(r)}, r d/dr (h_R|_S) = (Z h_R)|_S + (v1 − f + r f′)(∂_t h_R)|_S, with
r f′ ∈ C^∞ in ρ := 1/r and f smooth in ρ (f′ ∈ |x|⁻² C^∞): every (ρ∂_ρ)^j Ω^β (h_R|_S) is a combination of restrictions of
commuted fields with coefficients smooth in ρ. On S, w ≥ r^(2a), and by [[eq:own-hardy]], with r = 1/ρ and
r^(2a+1) dr = ρ^(−2(a+1)) dρ/ρ, the energies place h_R|_S in ρ^(a+1) L²_b(dρ/ρ dω) and ∂h_R|_S in ρ^(a+2) L²_b, with every
b-derivative, a + 1 > ℓ0. On S, s = 1 + (f − v1)ρ is smooth in ρ, so Σ|_S = Σ_(p∈Π) ρ^p F_p(1 + (f − v1)ρ, x̂) is
polyhomogeneous with exponents p + j, j ∈ ℕ_0, all in ℰ_0^½, and its coefficients are O(λ) by [[lem:own-sigma-data]], the
coefficient of ρ^(5/2) being F_(5/2)(1, ·), which is O(λ^n) for every n by [[lem:own-sigma-data]] (a) and
[[lem:own-self-similar]]. The induced (γ, k) are smooth functions of (g, ∂g) on S and of (∂f, ∂²f), as in the proof of
[[lem:vii-2-1]], equal to (γ_b0, k_b0) at h = 0, and ℰ_0^½ is closed under sums; so γ − γ_b0 ∈ H^(∞,(ℰ_0^½,ℓ0))_b and
k − k_b0 ∈ H^(∞,(ℰ_0^½+1,ℓ0+1))_b on S, with ‖·‖_(d_1) ≤ C(λ + ε_B), since k1 ≥ d_1 + 4 covers the d_1 derivatives and the
commutations used here. ∎

