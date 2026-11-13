# Part. Settling at late times {#part:settling}

## The proof of the settling theorem {#ch:settling-proof}

This chapter proves [[thm:settling]]. The solutions g_λ of [[thm:main]] live on a bounded domain Ω, which ends at the
time T after the shell. Settling concerns all later times, and it is proved with the nonlinear stability theory of
five-dimensional Schwarzschild–Tangherlini of [[part:stability]] to [[part:stability-nonlinear]], which is posed on
Hintz's initial surface Σ^IVP ([[sec:iii-b-3-3]]). The proof has three steps. First, after the shell the approximant
carries no oscillation ([[lem:np-10-50-a]]), so there g_λ lies within O(λ) of the Tangherlini metric of the final mass
μ_end in C^J, J = K − 4 ([[lem:vii-1-1]]); and Ω can be enlarged so that it contains the part of Σ^IVP that is needed,
in coordinates in which the background is the Tangherlini metric g_(b₀), b₀ = (μ_end, 0), of the stability theory
([[lem:vii-1-2]]). The data of g_λ are read on Σ^IVP itself, so no Cauchy stability argument is used. Second, these
data are continued G-equivariantly to exact Tangherlini data far out, with only the mass to match ([[cor:vii-2-3]]),
and their development settles to Tangherlini by the nonlinear stability theorem run in the symmetry class
([[prop:vii-3-2]], [[cor:s27-rate]]): this is item (i). Third, every perturbation of those data that is small in
Hintz's data class has a development that settles to a Myers–Perry metric ([[thm:iii-k-4-3]]): this is item (ii).
[[thm:settling-precise]] states the result with all its quantifiers, and [[thm:settling]] is deduced from it at the end
of [[sec:vii-4]].

*The inner radius.* The inner radius r_♭ ∈ (0, ½R₁] of [[sec:iii-b-2]], R₁ = μ_end^(1/2), is a parameter: the
spacetime M of [[eq:iii-b-2-1]] has the inner boundary {|x| = r_♭}, and every result of this chapter holds for each
such r_♭, with constants that may depend on it. The domain of [[thm:main]] is enlarged inward, through its inner
constant alone, so that it reaches r ≥ a′ with a′ < ½r_♭, and forward through T′ ([[lem:vii-1-2]]). r_♭ may be chosen
depending on μ_end, as in [[ch:interior]]; every choice made in [[sec:vii-4]] comes after it.

*Notation.* The parameters l5, μ0 ≥ √72 l5², A, env and τ0 of [[thm:main]] are fixed; its domain is a domain Ω′ of the
form [[eq:omega]], with constants T′, δ′_0 in place of T, δ0, which [[lem:vii-1-2]] chooses. As in [[ch:s27]], ε denotes
the smallness threshold of [[cor:s27-rate]]; the exponent of the rate, written ε in [[thm:settling]], is written ε_t
here. The integer J of [[lem:vii-1-1]] is unrelated to the index J of the class 𝒳^∞_(J,ex) of [[thm:iii-k-4-3]], and
the constant c₀ of [[lem:vii-1-2]] is a time shift.

### The setting and the precise statement {#sec:vii-0}

*The main argument's side.* We use the coordinates (τ, x) of [[sec:background]], with r = |x| and v = τ + r, and the
Vaidya background g0 = η + (μ(v)/r²) dv ⊗ dv of [[eq:background]], where μ = μ_end for v ≥ v_end. As dv = dτ + dr,

    g0 = η + (μ_end/r²)(dτ + dr)²     on {v ≥ v_end},

which is the Kerr–Schild Tangherlini metric g^KS_(μ_end,0) of [[def:iii-b-3-2]], with Kerr–Schild time τ. A domain Ω′
of the form [[eq:omega]] has the τ0 of [[thm:main]] and constants T′ > 0 and δ′_0 ∈ (0, q0): with a′ := q0 − δ′_0,
V′ := v_end + T′ and τ′_end := max_(v≤V′) (v − r_q(v)),

    Ω′ = {τ0 ≤ τ ≤ τ′_end,  |x| ≥ a′,  v + (τ − τ′_end) ≤ V′ + 1}.

[[thm:main]] holds on every such domain, its constants depending on it, and we put Ω′_+ := Ω′ ∩ {v ≥ v_end + 1}.

*The stability theory's side.* Put b₀ := (μ_end, 0), so that the mass m₀ of [[ch:s11]]–[[ch:s29]] is μ_end and
R₁ = μ_end^(1/2). In the coordinates (t, x) of [[sec:iii-b-2]], g_(b₀) = Φ_(μ_end)^*g^KS_(μ_end,0), that is
t = t_KS + T_(μ_end)(|x|) with t_KS the Kerr–Schild time ([[eq:iii-b-3-3]]). The time functions t_* and
t_IVP = t − ψ_IVP(|x|), the initial surface Σ^IVP := t_IVP⁻¹(0), the radius R₃ beyond which ψ_IVP is constant and its
value C″ there are those of [[eq:iii-b-3-6]] and [[lem:iii-b-3-7]]; (γ_(b₀), k_(b₀)) are the data that g_(b₀) induces
on Σ^IVP ([[lem:iii-b-3-9]]). Ω_*, the region 𝒟 and its parts 𝒟_(S,S⁰), the cut-off χ_K, the cut-off Lorentz boosts
φ_S of [[sec:iii-b-5]] and the cut-off translations ψ_(S⁰) of [[lem:iii-i7-1-1]], S, S⁰ ∈ 𝒮_1, composed as
φ_(S,S⁰) := ψ_(S⁰) ∘ φ_S in [[eq:s27-motion]], the parameter set ℬ_*, and the terms h_tot(p⃗) and h_(b,rem)(q) are
those of [[sec:iii-k-0]], [[prop:iii-k-1-2]] and [[thm:iii-k-4-3]]. The parameters of the stability theory are chosen
by [[thm:vi-c-2-1]], with the data class [[eq:vii-0-1]] at its step (3):

    ℰ_0 = {(j, 0) : j ∈ ℕ, j ≥ 2},     ℓ_0 ∈ (3, 4),     ℓ_I ∈ (3, ℓ_0);

its steps (0)–(4), up to the choice of α with which step (4) ends, are made once, and fix ε_K, the number of row w1 of
[[sec:vi-c-1]]. The order α of row w2 and steps (5)–(6) are chosen in the proof ([[sec:vii-4]]), depending on the
exponent of the rate; with them the order d_1 and the norm ‖·‖_(d_1) of [[sec:s27-class]] are fixed. The group
G = O(2) × O(2) acts as in [[sec:s27-class]], and the choices of [[lem:vii-3-1]] are made O(4)-equivariant; they are
admissible choices of the stability theory, so [[thm:iii-k-4-3]] holds with them.

**Theorem {#thm:settling-precise}** (Settling, precise form.) Let l5, μ0, A, env and τ0 be fixed and
b₀ = (μ_end, 0), as above; let r_♭ ∈ (0, ½R₁], and let steps (0)–(4) of [[thm:vi-c-2-1]], up to the choice of α, be
made as above. For every ε_t ∈ (0, ε_K) there are a choice of α in row w2 and of steps (5)–(6), R ≥ R₃ and a domain Ω′
of the form [[eq:omega]], depending on ε_t and r_♭ only, such that for every ε_m > 0 there are λ_1 > 0 and δ > 0,
depending moreover on ε_m, for which the following holds for 0 < λ ≤ λ_1. Here g_λ is the solution of [[thm:main]] on
Ω′, built with K = d_1 + 14 and N = K + 3 stages, and Σ^IVP is placed in the coordinates (τ, x) by [[lem:vii-1-2]].

(i) *In the class.* There are G-invariant smooth vacuum data (γ_λ, k_λ) on Σ^IVP that equal the data of g_λ on
Σ^IVP ∩ {r ≤ R}, and on Σ^IVP ∩ {r ≥ 4R} the data (γ^(m_λ), k^(m_λ)) that the Tangherlini metric g^KS_(m_λ,0) induces
there ([[lem:vii-2-1]]), with

    |m_λ − μ_end| ≤ Cλ,     ‖(γ_λ − γ_(b₀), k_λ − k_(b₀))‖_(d_1) ≤ Cλ.

There are also m′ with |m′ − μ_end| < ε_m and a G-invariant metric g on Ω_* ∪ 𝒟_0 with Ric(g) = 0, inducing
(γ_λ, k_λ) on Σ^IVP, such that, where χ_K = 1,

    g − g_(m′,0) = h_tot(p⃗) + h_(b,rem)(q) + h,     h ∈ 𝒳^∞_(J,ex),  q ∈ 𝒬_ex,

the conclusions (3)–(4) of [[thm:iii-k-4-3]] with b = (m′, 0) and S = S⁰ = 0, where h_tot(p⃗) = 0 on the interior of
{χ_K = 1}. In particular, for every R′, ε′ > 0 and i, β there are C and T′ with

    |(t_*∂_(t_*))^i ∂^β_x (g − g_(m′,0))| ≤ C t_*^(−(α−2)+ε′)     on {r_♭ ≤ r ≤ R′, t_* ≥ T′},           {#eq:vii-0-2}

where α − 2 > 2 + ε_K − ε′_0 > 2 (row w2 of [[sec:vi-c-1]]), α may be chosen as close to 4 + ε_K as desired, and
α > 4 + ε_t; so ε′ := α − 4 − ε_t gives g − g_(m′,0) = O(t_*^(−2−ε_t)) there. On Σ^IVP ∩ {r < R}, g and g_λ induce
the same data.

(ii) *Without symmetry.* Let (γ, k) be smooth vacuum data on Σ^IVP with

    (γ − γ_λ, k − k_λ) ∈ H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b,     ‖(γ − γ_λ, k − k_λ)‖_(d_1) < δ.

Then there are b ∈ ℬ_* with |b − b₀| < ε_m, S, S⁰ ∈ 𝒮_1 with |S|, |S⁰| < ε_m, and a metric g on
Ω_* ∪ 𝒟_(−S,−S⁰) with Ric(g) = 0 inducing (φ|)^*(γ, k) on φ⁻¹(Σ^IVP) = φ_S(ψ_(S⁰)(Σ^IVP)), φ := φ_(−S,−S⁰), such
that, where χ_K = 1, g − g_b = h_tot(p⃗) + h_(b,rem)(q) + h with the classes of (i), h_tot(p⃗) = 0 on the interior
of {χ_K = 1}, and [[eq:vii-0-2]] holds with g_b in place of g_(m′,0). So g settles to the Myers–Perry metric g_b at
the rates [[eq:vii-0-2]].

Here 𝒟_0 := 𝒟_(0,0) ⊂ 𝒟 is the region 𝒟_(S,S⁰) of [[prop:iii-k-1-2]] at S = S⁰ = 0, and |b − b₀| = |m − μ_end| + |A|
for b = (m, A), the norm of step (5) of [[thm:vi-c-2-1]]. On the finite-dimensional space 𝔟 it is equivalent to the
norm ‖·‖_𝔟 of 𝔟 as a component of 𝒟_ex, in which [[cor:s27-rate]] (a) bounds b − b₀; we fix C_𝔟 ≥ 1 with
|b − b₀| ≤ C_𝔟‖b − b₀‖_𝔟, so that [[cor:s27-rate]], applied with ε_m/C_𝔟 in place of ε_m, gives |b − b₀| < ε_m.
C depends on R and on the data of [[thm:main]], not on λ.

### The solution after the shell {#sec:vii-1}

After the shell the approximant of [[thm:approximant]] carries no oscillation. We write it as in [[eq:ansatz]]: the
profile G = ḡ + λW + Σ_(j=2)^(N+1) λ^j ĝ_j, with the mean metric ḡ = g0 + Σ_(j=1)^N λ^j m_j, the phase
u = v + Σ_(j=1)^N λ^j φ_j, the leading wave W = W_TT + χ dv ⊗ dv of [[sec:stage-zero]] and the oscillating profiles
ĝ_j of zero θ-mean, and g_app = g0 + λ[g1] + Σ_(j=2)^N λ^j [g_j] its form with the fixed phase v.

**Lemma {#lem:np-10-50-a}** (No oscillation after the shell.) Let Ω be a domain of the form [[eq:omega]], N ≥ 1, and
let g_app be the approximant of [[thm:approximant]] on Ω with N stages and the stage data of [[lem:stage-data]]. Put
Ω_> := Ω ∩ {v > v_end}. Then W and ĝ_2, …, ĝ_(N+1) vanish on Ω_> × S¹. Consequently, on Ω_>,

    g_app = g0 + Σ_(j=1)^N λ^j m_j,     g0 = η + (μ_end/r²)(dτ + dr)²,

with m_j smooth on Ω and independent of λ; and if g = g_app + w is the solution of [[thm:uniform-existence]] with this
approximant, then w = h on Ω_>, h of [[eq:ue-remainder]].

*Proof.* Ω_> is relatively open in Ω, so a profile that vanishes on Ω_> × S¹ vanishes there with all its derivatives.
Let p ∈ Ω_>. The integral curve of ℓ = −L0 through p, followed to the past, stays in Ω and meets Σ_τ0
([[lem:domain]] (d)); since L0(v) = 0, v is constant along it, so it stays in Ω_>. We call it the generator through p.

*The wave.* W_TT is proportional to env(v) ([[eq:waves]]), and env vanishes for v > v_end; so W_TT = 0 on Ω_>. The
second harmonic χ has zero θ-mean, vanishes on Σ_τ0 and solves (∂_r + 3/(2r))∂_θχ = F_2 ([[eq:chi-transport]]), where
∂_r = ℓ in the coordinates (v, r, ϑ, φ1, φ2) and F_2 is quadratic in env(v) through y1, y2 and α ([[sec:stage-zero]]).
On a generator in Ω_>, F_2 = 0, so r^(3/2)∂_θχ is constant along it; it vanishes at the generator's point on Σ_τ0, so
∂_θχ = 0, and χ, of zero θ-mean, vanishes. So W = 0 on Ω_>.

*The oscillating profiles.* We use one observation twice. In the two-scale expansion of the reduced Ricci tensor and of
the gauge field, the dependence on θ enters only through W and the ĝ_j: g0, the means m_j and the phases φ_j do not
depend on θ, and a product of factors that do not depend on θ has zero oscillating part. So every term of the
oscillating part of an expression polynomial in the profiles and their derivatives contains W, some ĝ_j, or a
derivative of one of these.

We show by induction on m = 1, …, N that ĝ_(m+1) = 0 on Ω_> × S¹, given that W, ĝ_2, …, ĝ_m vanish there (for m = 1
this is the preceding step).

(a) The data. By [[lem:stage-data]] (i), on Σ_τ0 the oscillating part of the order-m coefficient D^(m) of the gauge
field, its index lowered by g0, is Pol(∂_θĝ_(m+1)) + Λ_m(γ_m) + (known), and the stage datum is
∂_θĝ_(m+1) := −Pol⁺(Λ_m(γ_m) + known), solved pointwise. The sum Λ_m(γ_m) + known does not contain ĝ_(m+1), and the
profiles of later stages are not defined at this stage; so by the observation each of its terms contains W, one of
ĝ_2, …, ĝ_m, or a derivative of one of these, and it vanishes on Σ_τ0 ∩ Ω_>. Pol⁺ acts pointwise, so ∂_θĝ_(m+1) = 0
on Σ_τ0 ∩ Ω_>, and ĝ_(m+1), of zero θ-mean, vanishes there.

(b) The transport. Stage 1 imposes e_1 = 0, so [[lem:first-stage-operator]] gives T̂Y = −(ℓ·∂_X)∂_θY + ℳY, and
the equation (c) of [[lem:stage-system]] is, for Z := ∂_θĝ_(m+1), the transport

    −(ℓ·∂_X)Z + ℳ′Z = F,     F := −Π_osc(𝒲(m_m, φ_m) + 𝒦_m),

along ℓ, with ℳ′ = Π_osc ℳ ∂_θ⁻¹ a bounded operator on the zero-mean functions of θ, bounded uniformly on Ω. By
[[lem:first-entry]], 𝒲 is linear in (m_m, φ_m) and 𝒦_m depends only on m_i, φ_i (i < m) and ĝ_i (i ≤ m); neither
contains ĝ_(m+1). By the observation each term of F contains W, one of ĝ_2, …, ĝ_m, or a derivative of one of these,
so F = 0 on Ω_>. On a generator in Ω_>, parametrised by s, Z solves ℓ·∂_X Z = ℳ′Z, so
|(d/ds)‖Z‖²_(L²(S¹))| ≤ 2‖ℳ′‖ ‖Z‖²_(L²(S¹)); Z vanishes at the generator's point on Σ_τ0 by (a), and so, by Gronwall's
inequality, along the whole generator. Hence ∂_θĝ_(m+1) = 0 on Ω_>, and ĝ_(m+1) = 0 there. This completes the
induction.

*The approximant.* So G = ḡ on Ω_> × S¹, and G does not depend on θ there. The profiles g_j of [[thm:approximant]] are
the coefficients of λ^j, j ≤ N, in the expansion of G(X, θ + φ1 + λΨ), Ψ = Σ_(j≥2) λ^(j−2) φ_j, by Taylor's formula in
λΨ about θ + φ1. At X ∈ Ω_> every θ-derivative of G vanishes, so the expansion is G(X, θ + φ1) = ḡ(X), without
remainder, and g_j = m_j for 1 ≤ j ≤ N (in particular g1 = m1 + W(X, θ + φ1) = m1). Hence g_app = ḡ on Ω_>. The means
m_j are smooth on Ω ([[lem:stage-system]]) and, like every profile of [[thm:approximant]], independent of λ. The formula
for g0 is the one displayed in [[sec:vii-0]]. Finally ∂_θg1 = 0 on Ω_>, so w = h + φ[∂_θg1] = h there
([[eq:ue-remainder]]). ∎

**Lemma {#lem:vii-1-1}** (After the shell.) Let Ω′ be a domain of the form [[eq:omega]], with constants (T′, δ′_0) and
the τ0 of [[thm:main]], and let J ≥ 2 be an integer. Put K := J + 4 and N := K + 3, and let g_λ be the solution of
[[thm:main]] on Ω′ with these orders. There are C_J and λ_1 > 0, depending on Ω′ and J, such that for 0 < λ ≤ λ_1, on
Ω′_+ = Ω′ ∩ {v ≥ v_end + 1}, g_λ is G-invariant and vacuum, and its Cartesian components satisfy

    |∂^j(g_λ − g^KS_(μ_end,0))| ≤ C_J λ     (j ≤ J),                                                    {#eq:vii-1-1}

with ∂^j any j derivatives in (τ, x), and g^KS_(μ_end,0) = η + (μ_end/r²)(dτ + dr)².

*Proof.* *The order.* [[thm:main]] builds g_λ by [[thm:uniform-existence]] from the approximant of [[thm:approximant]]
with N = K + 3 stages and the data of [[thm:data]]. By [[rem:ue-every-order]] with its energy order k taken equal to
K ≥ 6, whose inputs (E3) and (E4) hold at every order for this approximant and these data, there are M and λ_1 > 0
such that 𝒩_K(τ) ≤ Mλ^K on [τ0, τ′_end] for 0 < λ ≤ λ_1, 𝒩_K being the quantity [[eq:ue-energy]] at order k = K.
Since 𝒩_K contains ‖h‖ and λ^i‖∂^i∂h‖ for i ≤ K, the L²(Σ_τ) norms satisfy

    ‖h(τ)‖ ≤ Mλ^K,     ‖∂^i∂h(τ)‖ ≤ Mλ^(K−i)     (i ≤ K).

*After the shell.* Ω′_+ ⊂ Ω′ ∩ {v > v_end}, so by [[lem:np-10-50-a]], on Ω′_+,

    g_λ − g^KS_(μ_end,0) = Σ_(j=1)^N λ^j m_j + h.

*Bounds.* By the Sobolev inequality [[eq:sobolev]] on the slices A(τ) of Ω′, with a constant independent of τ,
|∂^jh| ≤ C Σ_(i≤3) ‖∂_x^i ∂^jh‖ on A(τ). Let j ≤ K − 3. For j ≥ 1 the terms are bounded by
‖∂^(i+j−1)∂h‖ ≤ Mλ^(K−i−j+1) ≤ Mλ^(K−j−2), as i + j − 1 ≤ K; for j = 0 they are ‖h‖ ≤ Mλ^K and
‖∂^(i−1)∂h‖ ≤ Mλ^(K−i+1) ≤ Mλ^(K−2) (1 ≤ i ≤ 3). As λ ≤ 1, |∂^jh| ≤ C_Kλ^(K−j−3) on Ω′ for j ≤ K − 3. With K = J + 4
this is at most C_Kλ for j ≤ J. The derivatives of order at most J of Σ_j λ^j m_j are at most Cλ on the compact set
Ω′_+, the m_j being smooth and independent of λ. This gives [[eq:vii-1-1]]. Finally Ric(g_λ) = 0 on Ω′, and g_λ is
invariant under the T² action and both reflections, which generate G ([[thm:main]], item 1). ∎

**Lemma {#lem:vii-1-2}** (Placing Σ^IVP.) Let R ≥ R₃. There are c₀ ∈ ℝ and a domain Ω′ of the form [[eq:omega]], with
the τ0 of [[thm:main]] and with a′ = q0 − δ′_0 < ½r_♭, such that in the chart

    (t, x) := (τ + T_(μ_end)(|x|) + c₀, x):

(a) g0 = g_(b₀) on Ω′ ∩ {v ≥ v_end, |x| ≥ r_♭};

(b) Σ^IVP ∩ {r_♭ ≤ r ≤ 4R} lies in the interior of Ω′_+.

The chart change commutes with G, and Σ^IVP is G-invariant.

*Proof.* (a) On {v ≥ v_end}, g0 = g^KS_(μ_end,0) in the coordinates (τ, x), by a formula valid for every r > 0 whose
coefficients do not depend on τ. In the chart, τ = t − T_(μ_end)(|x|) − c₀, so the map (t, x) ↦ (τ, x) is the map
Φ_(μ_end) of [[eq:iii-b-3-3]] followed by the translation τ ↦ τ − c₀, which preserves g^KS_(μ_end,0). So there
g0 = Φ_(μ_end)^*g^KS_(μ_end,0) = g_(b₀), which [[eq:iii-b-3-3]] defines on ℝ_t × {|x| ≥ ½r_♭}.

(b) On Σ^IVP, t = ψ_IVP(|x|), so τ = f_IVP(r) − c₀ with f_IVP := ψ_IVP − T_(μ_end), continuous on [r_♭, 4R]. Take

    c₀ := min_([r_♭,4R]) f_IVP − max(τ0 + 1, v_end + 2 − r_♭).

Then on Σ^IVP ∩ {r_♭ ≤ r ≤ 4R} we have τ ≥ τ0 + 1, v = τ + r ≥ v_end + 2, and τ ≤ τ_top := max_([r_♭,4R]) f_IVP − c₀.
Take δ′_0 ∈ (max(0, q0 − ½r_♭), q0), an interval that is nonempty as r_♭ > 0; then 0 < a′ < ½r_♭. Put
q_end := (√72 μ_end l5²)^(1/4); μ being nondecreasing, r_q(v) ≤ q_end for every v. Take T′ > 0 so large that
V′ = v_end + T′ ≥ τ_top + 2R + q_end + 1. Then τ′_end = max_(v≤V′) (v − r_q(v)) ≥ V′ − q_end ≥ τ_top + 1, and on
Σ^IVP ∩ {r_♭ ≤ r ≤ 4R}

    v + (τ − τ′_end) = 2τ + r − τ′_end ≤ 2τ_top + 4R + q_end − V′ < V′ + 1.

With τ0 < τ ≤ τ_top < τ′_end and r ≥ r_♭ > a′, every defining inequality of Ω′ holds strictly there, and
v ≥ v_end + 2 > v_end + 1. So these points lie in the interior of Ω′_+. Finally, T_(μ_end) and ψ_IVP are functions of
|x|, and G fixes τ, t and |x|. ∎

### Proof of the theorem {#sec:vii-4}

*Proof of [[thm:settling-precise]].* *The choices.* Let ε_t ∈ (0, ε_K). The parameters are chosen by [[thm:vi-c-2-1]]
with [[eq:vii-0-1]] at its step (3), up to ε_K at its step (4); ε_K does not depend on ε_t. Take α > 4 + ε_t in row w2
and finish steps (5)–(6); this fixes the order d_1 of [[thm:iii-k-4-3]]. These choices do not involve ε_m:
[[cor:s27-rate]] takes the parameters so chosen, with d_1 as in [[thm:iii-k-4-3]], and ε_m enters only its threshold.
Then choose, in this order:

- k := d_1 + 5, the order of the gluing in [[prop:vii-2-2]];
- R ≥ max(R_gl, R₃), with R_gl of [[prop:vii-2-2]] at this k;
- c₀ and Ω′ by [[lem:vii-1-2]], and J := k + 5 in [[lem:vii-1-1]], so that g_λ is built on Ω′ with
  K = J + 4 = d_1 + 14.

Let ε_m > 0. [[cor:s27-rate]], applied with ε_m/C_𝔟 in place of ε_m (C_𝔟 of [[sec:vii-0]]), gives
ε = ε(ε_m, ε_t) > 0 such that its conclusions (a)–(c) hold for data of norm below ε; its part (b) contains the
threshold of the run of [[thm:ii-g-2-1]] in the symmetry class ([[prop:vii-3-2]]). Take λ_1 > 0 so small that
[[lem:vii-1-1]] and [[cor:vii-2-3]] apply for λ ≤ λ_1, and C_Rλ_1 < ½ε, with C_R the constant of [[cor:vii-2-3]], and
put δ := ½ε. The choices of [[lem:vii-1-2]] depend on r_♭ through δ′_0, c₀ and T′. So R, Ω′ and K depend on ε_t and
r_♭ only; λ_1 and δ depend moreover on ε_m.

*(i).* Let 0 < λ ≤ λ_1. [[cor:vii-2-3]], with k = d_1 + 5 and the data of g_λ on Σ^IVP ∩ {r_♭ ≤ r ≤ 4R}, gives
G-invariant smooth vacuum data (γ_λ, k_λ) := (ĝ, K̂) and m_λ := m, equal to the data of g_λ on Σ^IVP ∩ {r ≤ R} and to
(γ^(m_λ), k^(m_λ)) on Σ^IVP ∩ {r ≥ 4R}, with |m_λ − μ_end| ≤ C_Rλ and

    ‖(γ_λ − γ_(b₀), k_λ − k_(b₀))‖_(d_1) ≤ C_Rλ < ½ε.

The differences lie in H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b, by [[lem:vii-0-1]] with R′ = 4R: beyond 4R they are
(γ^(m_λ) − γ_(b₀), k^(m_λ) − k_(b₀)), whose Cartesian components lie in ρ²C^∞ and ρ³C^∞ of the radial
compactification ([[lem:vii-2-1]] (a), with γ_(b₀) = γ^(μ_end) and k_(b₀) = k^(μ_end)). So [[cor:s27-rate]] (b)
applies: [[prop:vii-3-2]] gives U fixed by G, b = (m′, 0) with |m′ − μ_end| < ε_m/C_𝔟 ≤ ε_m, S = S⁰ = 0, and a
G-invariant metric g with the conclusions (1)–(5) of [[thm:iii-k-4-3]]. By (2) with S = S⁰ = 0, φ_(0,0) = ψ_0 ∘ φ_0
being the identity ([[eq:s27-motion]]), g is defined on Ω_* ∪ 𝒟_0 and induces (γ_λ, k_λ) on Σ^IVP; on
Σ^IVP ∩ {r < R} these are the data of g_λ.

*The rate.* Where χ_K = 1, g − g_(m′,0) = h_tot(p⃗) + h_(b,rem)(q) + h, by (3)–(4) of [[thm:iii-k-4-3]] with
b = (m′, 0) and S = S⁰ = 0. Every term of h_tot(p⃗) carries a factor dχ_K: the terms are those of [[def:iii-i4-2-1]],
[[def:iii-i7-2-1]], [[def:iii-i8-2-1]] and [[def:iii-i9-2-1]], summed in [[def:iii-i7-2-3]] and [[def:iii-i9-2-3]] over
the rows and the rotation rows of [[def:iii-i14-1-3]] (a rotation row has the terms that [[def:iii-i9-2-1]] assigns to
the type v1), and each is −dχ_K ⊗_s ω for a 1-form ω. So h_tot(p⃗) vanishes on the interior of {χ_K = 1}.
[[cor:s27-rate]] (c) gives [[eq:vii-0-2]], with α − 2 > 2 + ε_K − ε′_0 > 2 and α − 2 > 2 + ε_t. α was chosen with
α > 4 + ε_t among the admissible orders of row w2, which are dense in (4 + ε_K − ε′_0, 4 + ε_K]; so it may be taken as
close to 4 + ε_K as desired. With ε′ := α − 4 − ε_t > 0, [[eq:vii-0-2]] gives g − g_(m′,0) = O(t_*^(−2−ε_t)) on
{r_♭ ≤ r ≤ R′, t_* ≥ T′}.

*(ii).* The difference

    (γ − γ_(b₀), k − k_(b₀)) = (γ − γ_λ, k − k_λ) + (γ_λ − γ_(b₀), k_λ − k_(b₀))

lies in the class, with norm below δ + ½ε = ε. So [[cor:s27-rate]] (a) applies: [[thm:iii-k-4-3]] holds with
‖b − b₀‖_𝔟 < ε_m/C_𝔟 and |S|, |S⁰| < ε_m/C_𝔟, hence |b − b₀| < ε_m and |S|, |S⁰| < ε_m, as C_𝔟 ≥ 1. By (2) of
[[thm:iii-k-4-3]], g induces (φ|)^*(γ, k) on φ⁻¹(Σ^IVP), φ := φ_(−S,−S⁰), and φ⁻¹ = φ_S ∘ ψ_(S⁰) ([[eq:s27-motion]]).
The vanishing of h_tot(p⃗) on the interior of {χ_K = 1} holds as in (i), and [[cor:s27-rate]] (c) gives [[eq:vii-0-2]]
with g_b in place of g_(m′,0). ∎

*Proof of [[thm:settling]].* *The parameters.* [[thm:settling]] fixes its quantities in the order of
[[thm:settling-precise]]: first l5, μ0, A, env and τ0, then b₀ = (μ_end, 0), about which the stability theory is set
up, and its inner radius r_♭ ∈ (0, ½R₁] = (0, √μ_end/2], and then ℓ0 and ε_K. The number ℓ0 ∈ (3, 4) is the ℓ_0 of the
data class [[eq:vii-0-1]], and ε_K is the one chosen at step (4) of [[thm:vi-c-2-1]], with [[eq:vii-0-1]] at step (3).
With the ℓ_I ∈ (3, ℓ_0) chosen at step (3), which is admissible in row d2 of [[sec:vi-c-1]] (it avoids the discrete
exclusion sets of that row, [[sec:s27-class]]), and the ε_+ chosen at step (4), ε_K satisfies the conditions that
[[thm:settling]] states, all of them conditions of row w1: 0 < ε_K < ε_+ < min(δ_♯, ε_ind, ℓ_I − 3, ¼), (G⁺) and (G).
Row w1 also asks the exactness conditions (Ex1)–(Ex2) of [[def:iii-j3-1-3]], which [[thm:settling]] does not list;
step (4) imposes them on the ε_+ it chooses, together with the others. (Ex1) is (G⁺) with its closed endpoint, as
[[thm:settling]] states it. With the parameters so chosen, the hypotheses of [[thm:settling-precise]] hold.

Let ε ∈ (0, ε_K) be the exponent of [[thm:settling]], put ε_t := ε, and apply [[thm:settling-precise]]. It gives
K = d_1 + 14, R and Ω′, which depend on ε_t and r_♭ only, and, for each ε_m > 0, λ_1 and δ, which depend moreover on
ε_m. The solutions g_λ of [[thm:settling]] are those of [[thm:main]] on the enlarged domain Ω′ of [[lem:vii-1-2]],
built with K = d_1 + 14, d_1 the regularity of [[thm:iii-k-4-3]].

Item (i). The data of g_λ on Σ^IVP ∩ {r ≤ R}, continued G-equivariantly to the exact Tangherlini data
(γ^(m_λ), k^(m_λ)) on {r ≥ 4R}, are the data (γ_λ, k_λ) of [[thm:settling-precise]] (i), constructed in
[[cor:vii-2-3]]. Their development g is G-invariant and vacuum, induces the data of g_λ on the ball Σ^IVP ∩ {r < R},
and by [[eq:vii-0-2]] satisfies g − g_(m′,0) = O(t_*^(−2−ε_t)) on every set {r_♭ ≤ r ≤ R′, t_* ≥ T′}, where g_(m′,0)
is the Tangherlini metric of mass m′, |m′ − μ_end| < ε_m. Every spatially compact subset of the exterior of the black
hole lies in M ∩ {r ≤ R′} for some R′, and its points with t_* ≥ T′ lie in {r_♭ ≤ r ≤ R′, t_* ≥ T′}.

Item (ii). The data class of (ii) in [[thm:settling]] is H^(∞,(ℰ_0,ℓ_0))_b × H^(∞,(ℰ_0+1,ℓ_0+1))_b with
[[eq:vii-0-1]]: the elements of ℰ_0 below ℓ_0 give the polyhomogeneous terms of orders 2 and 3 in the metric, those of
ℰ_0 + 1 below ℓ_0 + 1 the terms of orders 3 and 4 in the second fundamental form, and the remainders have the weights
ℓ_0 and ℓ_0 + 1 ([[sec:s27-class]]). For data in it, of norm below δ, [[thm:settling-precise]] (ii) gives a vacuum
development g whose initial surface is the surface φ_(−S,−S⁰)⁻¹(Σ^IVP) = φ_S(ψ_(S⁰)(Σ^IVP)), φ_S the cut-off Lorentz
boost of [[sec:iii-b-5]] and ψ_(S⁰) the cut-off translation of [[lem:iii-i7-1-1]], with |S|, |S⁰| < ε_m, and which
settles at the rate [[eq:vii-0-2]] to the Myers–Perry metric g_b, b = (m′, A), with |m′ − μ_end| + |A| = |b − b₀| < ε_m:
mass within ε_m of μ_end and spin below ε_m. ∎

### Remarks on the statement {#sec:vii-5}

**Remark {#rem:vii-4-1}** (The development and g_λ.) The development g of [[thm:settling-precise]] (i) and g_λ are
vacuum metrics that induce the same data on Σ^IVP ∩ {r < R}, in different gauges. Let Σ := Σ^IVP ∩ {r_♭ < r < R}.
That g_λ, near the hole just before Σ, and g, after Σ^IVP, glued along Σ by the identity, form one smooth vacuum
spacetime M_gl; and that the Cauchy developments of Σ in M_gl and, for g_λ, in a neighbourhood of the closure of Σ
have a maximal common globally hyperbolic development U, which contains a neighbourhood of Σ, with an isometric
embedding of U into the second that preserves the time orientation and is the identity on Σ, is
[[lem:interior-one-spacetime]] of [[ch:interior]]. How far U reaches into the future of Σ is not decided there.
Nothing in [[thm:settling-precise]] or in its proof uses the lemma.

**Remark {#rem:settling-class}** (Perturbations and gluing.) [[thm:settling-precise]] (ii) takes the perturbation in
the data class of [[thm:iii-k-4-3]], and not in a class of decaying data reached by gluing. Gluing a perturbation that
decays faster than r^(−3/2) far out to a translated, rotated and boosted Myers–Perry metric ([[thm:v-3-1]]) replaces
its data near infinity, and the solution near the black hole at late times depends on those data: K⁺ at late times is
not in the domain of dependence of any bounded part of the initial surface. So a settling statement reached by gluing
holds for the glued data, not for the perturbation. With [[eq:vii-0-1]] the data class has polyhomogeneous terms of
orders 2 and 3 at spatial infinity and a conormal remainder of order ℓ_0 ∈ (3 + ε_+, 4). By [[lem:vii-0-1]] it
contains every perturbation that is, outside a compact set, a classical symbol of order −2 (in the metric) and −3 (in
the second fundamental form), that is an element of ρ²C^∞, resp. ρ³C^∞, of the radial compactification, for instance
the data of a nearby translated, rotated and boosted Myers–Perry metric. So (ii) needs no gluing and no parity
condition; the gluing is used in (i) only, in its class form [[prop:vii-2-2]]. For a merely decaying perturbation,
gluing gives only that it agrees on a large ball with one to which (ii) applies, and that statement is not made here.
Which decaying perturbations (ii) reaches, directly or through gluing, is determined in [[ch:after-shell]].
