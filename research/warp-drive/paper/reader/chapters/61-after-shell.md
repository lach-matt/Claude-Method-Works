## After the shell: the reach of the settling theorem {#ch:after-shell}

[[thm:main]] holds on D_T for each fixed T. This chapter takes up what happens after the shell and how far the settling
theorem [[thm:settling]] reaches. [[sec:after-shell-question]] places the question: settling for all later times is the
nonlinear stability of five-dimensional Schwarzschild–Tangherlini within the class, and the biaxial class in which that
stability is known meets the class only in spherical symmetry ([[prop:after-shell-classes]]).
[[sec:after-shell-profiles]] proves that every oscillating profile of the approximant vanishes after the shell, so that
there g_λ is Tangherlini of mass μ_end up to smooth corrections of order λ ([[prop:after-shell-profiles]]).
[[sec:after-shell-gluing]] recalls how the data of g_λ near the hole are glued, in the class, to exact Tangherlini data
with only the mass to match, which gives the data of item (i) of [[thm:settling]].

[[sec:after-shell-reach]] determines which perturbations of these data item (ii) reaches. A perturbation that decays
like r^(−a), with a > 3, lies in Hintz's class and is reached directly ([[prop:after-shell-above]],
[[cor:after-shell-every-rate]]). For 3/2 < a ≤ ℓ0 the rate does not decide. Agreement on every ball with data to which
(ii) applies, uniformly in the radius, is equivalent to membership in the class ([[prop:after-shell-membership]]). At
every such rate some pure-gauge perturbations lie outside the class, and every data set in the class that agrees with
them on {r < R} has norm at least of order R^(ℓ0−a) ([[prop:after-shell-outside]]). Gluing to the translated, rotated
and boosted Myers–Perry data on Hintz's own surface ([[lem:after-shell-mp-data]]) does no worse than this order for
every perturbation ([[prop:after-shell-gluing]], [[cor:after-shell-glued-norm]]). [[thm:after-shell-reach]] collects
the answer: the perturbations to which (ii) applies, directly or through gluing uniformly in the gluing radius, are
exactly those small in Hintz's class.

### The question {#sec:after-shell-question}

[[thm:main]] holds on D_T for each fixed T; the theorems of Huneau and Luk [HL18], of Touati [Tou23a] and of Luk and
Rodnianski [LR20] hold on a fixed interval too. Settling for all later v is the nonlinear stability of five-dimensional
Schwarzschild–Tangherlini within the class. Linear stability against every type of perturbation is known: Ishibashi and
Kodama "have shown that higher-dimensional Schwarzschild black holes are stable with respect to all tensorial types of
linear perturbations" ([IK03, p. 16]). Nonlinear asymptotic stability is known in a class of perturbations with more
symmetry: Holzegel proves "the non-linear asymptotic stability of the five-dimensional Schwarzschild metric under
biaxial vacuum perturbations", that is, "the evolution of (SU(2) × U(1))-symmetric vacuum perturbations of initial data
for the five-dimensional Schwarzschild metric finally converges in a suitable sense to a member of the Schwarzschild
family" ([Hol08, p. 1; Theorem 1.1, pp. 5–6]). In that class the vacuum equations reduce to a system of partial
differential equations in 1 + 1 dimensions ([Hol08, p. 4]); its metrics are ([Hol08, (22), p. 14])

    g = −Ω²(u, v) du dv + (1/4) r²(u, v) (e^(2B(u,v)) (σ1² + σ2²) + e^(−4B(u,v)) σ3²),          {#eq:after-shell-biaxial}

with σ1, σ2, σ3 a basis of left-invariant 1-forms on SU(2) = S³, normalised so that the round metric of S³ is
(1/4)(σ1² + σ2² + σ3²) ([Hol08, p. 14, footnote 25]); the squashing B vanishes for Schwarzschild–Tangherlini. That class
shares the torus T² of the T²-mirror class but not the reflections.

**Proposition {#prop:after-shell-classes}** (The biaxial class meets the class only in spherical symmetry.) On S³ use the
coordinates of [[sec:background]], x1 + i x2 = cos ϑ e^(iφ1), x3 + i x4 = sin ϑ e^(iφ2), with c = cos ϑ, s = sin ϑ, and
choose the left-invariant forms so that σ3 is dual to the generator of the diagonal action (z1, z2) ↦ (e^(it) z1,
e^(it) z2) of S³ ⊂ ℂ². Then, with η := c² dφ1 + s² dφ2,

    (1/4) σ3² = η²,      (1/4)(σ1² + σ2²) = dϑ² + c² s² (dφ1 − dφ2)²,                              {#eq:after-shell-hopf}

and the coefficient of dφ1 dφ2 in the quadratic form (1/4)(e^(2B)(σ1² + σ2²) + e^(−4B) σ3²) is

    2 c² s² (e^(−4B) − e^(2B)),                                                                  {#eq:after-shell-squash}

which vanishes at a point with c s ≠ 0 exactly when B = 0 there. Hence a metric [[eq:after-shell-biaxial]] is of the
form [[eq:class-metric]] in these coordinates if and only if B ≡ 0, and then it is spherically symmetric.

*Proof.* Write S³ as SU(2) by (z1, z2) ↦ ((z1, −z̄2), (z2, z̄1)), the columns of the matrix. Right multiplication by
diag(e^(it), e^(−it)) multiplies the first column by e^(it), so the diagonal action is a right action and its generator
∂_φ1 + ∂_φ2 is a left-invariant vector field. For the metric (1/4)(σ1² + σ2² + σ3²) the frame X1, X2, X3 dual to σ1, σ2,
σ3 is orthogonal with |X_i| = 1/2. The field ∂_φ1 + ∂_φ2 has length (c² + s²)^(1/2) = 1 for the round metric dϑ² + c²
dφ1² + s² dφ2², so it equals ±2X3, and its metric dual, η, equals ±σ3/2: both vanish on the orthogonal complement of
X3 and take the value 1 on ∂_φ1 + ∂_φ2 up to the sign. This gives the first identity. For the second,

    dϑ² + c² dφ1² + s² dφ2² − η² = dϑ² + c²(1 − c²) dφ1² + s²(1 − s²) dφ2² − 2 c² s² dφ1 dφ2
                                 = dϑ² + c² s² (dφ1 − dφ2)²,

and the left side is (1/4)(σ1² + σ2²). Hence (1/4)(e^(2B)(σ1² + σ2²) + e^(−4B) σ3²) = e^(2B)(dϑ² + c² s² (dφ1 − dφ2)²) +
e^(−4B)(c² dφ1 + s² dφ2)², whose dφ1 dφ2 coefficient is −2 c² s² e^(2B) + 2 c² s² e^(−4B), which is
[[eq:after-shell-squash]]. As e^(−4B) − e^(2B) is strictly decreasing in B and zero at B = 0, it vanishes exactly when
B = 0. A metric [[eq:class-metric]] has no dφ1 dφ2 term. B is a function of (u, v), so if B ≢ 0 the coefficient is
nonzero on a whole orbit off the axes, and the metric is not of the form [[eq:class-metric]]. If B ≡ 0,
[[eq:after-shell-biaxial]] is −Ω² du dv + r² (dϑ² + c² dφ1² + s² dφ2²), which is spherically symmetric. ∎

The waves of [[sec:waves]] depend on the polar angle ϑ, so they lie outside the biaxial class in any case.

After the shell the oscillating profiles vanish ([[prop:after-shell-profiles]]) and only the mean corrections remain: on
Ω ∩ {v > v_end}, g_λ differs from Tangherlini of the final mass μ_end by λ m1 + O(λ²), with its first derivatives.
Settling would therefore follow from the small-data stability of Tangherlini in the T²-mirror class, once the solution
is also constructed outside D_T. The first step is the stability theory of [[part:stability]] to
[[part:stability-nonlinear]], which gives [[thm:settling]]. The second, continuing g_λ outside D_T, is replaced by a
gluing ([[sec:after-shell-gluing]]). That the development of g_λ's own data settles, with no gluing, in a class wider
by half-integer orders, is [[thm:own-data]].

### No oscillation after the shell {#sec:after-shell-profiles}

We use the approximant of [[thm:approximant]] with the stage data of [[lem:stage-data]] (as [[thm:main]] does), with
the notation of [[sec:ansatz]]: the mean metric ḡ = g0 + Σ_(j=1)^N λ^j m_j, the phase u = v + Σ_(j=1)^N λ^j φ_j, the
leading oscillation W = W_TT + χ dv ⊗ dv of [[sec:stage-zero]], and the oscillating profiles ĝ_j, 2 ≤ j ≤ N + 1, of
zero θ-mean. The *oscillating profiles* are W and the ĝ_j.

**Proposition {#prop:after-shell-profiles}** (No oscillation after the shell.) Let g_λ and g_app be as in [[thm:main]].

(a) On Ω ∩ {v > v_end}, W = 0 and ĝ_j = 0 for 2 ≤ j ≤ N + 1, so that there

    g_app = g0 + Σ_(j=1)^N λ^j m_j,                                                                {#eq:after-shell-gapp}

with g0 = η + (μ_end/r²) dv ⊗ dv, five-dimensional Schwarzschild–Tangherlini of mass μ_end, and the m_j smooth and
independent of λ. In the coordinates (t, x) := (τ, x), g0 = g^KS_(μ_end,0) of [[def:iii-b-3-2]] there.

(b) On Ω ∩ {v > v_end}, |g_λ − g0 − λ m1| ≤ C λ² and |∂(g_λ − g0 − λ m1)| ≤ C λ². If [[thm:main]] is run at order k ≥ d
with K ≥ d + 1, then g_λ − g0 is O(λ) in H^d of the slices Σ_τ ∩ {v > v_end} ([[rem:ue-every-order]]).

(c) If T > r_q(μ_end) − a, a the inner radius of Ω ([[sec:domain]]), then for every τ1 ∈ (v_end − a, τ_end] the whole
slice Σ_τ1 lies in {v > v_end}, and its inner sphere {r = a} lies inside the horizon {r = √μ_end} of g0.

*Proof.* (a) *The leading oscillation.* μ′ = (2/9) A² env² ([[eq:mu-rate]]) and env is supported in [v_start, v_end],
so μ = μ_end and env = 0 for v ≥ v_end. W_TT is proportional to α = A env(v) h r^(−3/2) ([[sec:stage-zero]]), so it
vanishes on {v > v_end}. The source F_2 of the transport [[eq:chi-transport]] is quadratic in α, since y1 and y2 are
linear in α; so F_2 = 0 on {v > v_end}. The transport runs along ℓ = ∂_r, the derivative at fixed v. By
[[lem:domain]] (d) the integral curve of L0 = −ℓ through a point of Ω, followed to the past, stays in Ω, keeps v
(L0(v) = 0) and meets Σ_τ0. So {v > v_end} ∩ Ω is a union of such curves. On each of them ∂_θ χ solves
(∂_r + 3/(2r)) ∂_θ χ = 0 with ∂_θ χ = 0 on Σ_τ0 ([[lem:stage-data]]: χ = 0 on Σ_τ0), hence ∂_θ χ = 0, and χ, its
primitive of zero mean, vanishes. So W = 0 on Ω ∩ {v > v_end}.

*An oscillating factor in every term.* By [[lem:first-entry]] the coefficients ℛ^(m) and, likewise, the coefficients
D^(m) of the gauge function ([[sec:data-approximant]]) are sums of monomials in g0, v, the means m_i, the phases φ_i,
W and the ĝ_i, with their X-derivatives and with ∂_θ acting only on W and the ĝ_i. A monomial with no factor W or ĝ_i
(differentiated or not) does not depend on θ, so its oscillating part Π_osc vanishes. Hence every term of the
oscillating part of such a coefficient contains W or some ĝ_i, or a derivative of one, as a factor.

*Induction on the stage.* Let 1 ≤ m ≤ N and suppose ĝ_i = 0 on Ω ∩ {v > v_end} for 2 ≤ i ≤ m (for m = 1 there is no
such i). As this set is relatively open in Ω, W and these ĝ_i vanish there with all their derivatives, by continuity up
to the boundary of Ω.

The data of ĝ_(m+1) on Σ_τ0 are given pointwise by [[lem:stage-data]] (i): ∂_θ ĝ_(m+1) = −Pol⁺(Λ_m(γ_m) + known), where
Λ_m(γ_m) is bilinear with ∂_θ W and "known" is the rest of the oscillating part of D^(m) on Σ_τ0, which involves the
profiles of stages up to m only. Each term of both contains an oscillating factor W or ĝ_i with i ≤ m, so at every point
of Σ_τ0 ∩ {v > v_end}, ∂_θ ĝ_(m+1) = 0, and ĝ_(m+1), of zero θ-mean, vanishes there.

On Ω, Z := ∂_θ ĝ_(m+1) solves the transport −(ℓ·∂_X) Z + ℳ′ Z = F of the proof of [[lem:stage-system]], where ℳ′ is a
bounded operator on the zero-mean functions of θ, uniformly in X, and F = −Π_osc(𝒲(m_m, φ_m) + 𝒦_m), the oscillating
part of the terms of ℛ^(m) other than T̂ ĝ_(m+1) and the e_(m+1) term. By [[lem:first-entry]], 𝒦_m involves only m_i,
φ_i (i < m) and ĝ_i (i ≤ m), and the θ-dependent part of 𝒲(m_m, φ_m) carries the factor W (the term in □̃φ_m being
−(1/2)(□̃φ_m) ∂_θ W). So F = 0 on Ω ∩ {v > v_end}. On each integral curve of ℓ in Ω ∩ {v > v_end}, Z therefore solves a
linear homogeneous ordinary differential equation with values in L²(S¹), with Z = 0 where the curve meets Σ_τ0;
Gronwall's inequality gives Z = 0 on the curve. So ĝ_(m+1) = 0 on Ω ∩ {v > v_end}, which completes the induction.

*The approximant.* On Ω ∩ {v > v_end} we now have G = ḡ ([[eq:ansatz]]), which does not depend on θ. The profiles of the
fixed-phase form of [[thm:approximant]] come from the Taylor expansion of G(X, θ + φ1 + λΨ) about θ + φ1; every term
with a θ-derivative of G vanishes, so g1 = m1 + W(X, θ + φ1) = m1 and g_j = m_j for 2 ≤ j ≤ N. This is
[[eq:after-shell-gapp]]. The m_j are profiles of [[thm:approximant]] with zero oscillation, hence smooth and independent
of λ. For v ≥ v_end, μ = μ_end, so g0 = η + (μ_end/r²) dv ⊗ dv ([[eq:background]]), which is
[[eq:vr-form]] with f = 1 − μ_end/r², five-dimensional Schwarzschild–Tangherlini of mass μ_end in ingoing
Eddington–Finkelstein form. As dv = dτ + d|x|, it is η + μ_end|x|⁻²(dτ + d|x|)², which is g^KS_(μ_end,0) of
[[def:iii-b-3-2]] at A = 0 ([[prop:iii-b-3-4]]) with t = τ.

(b) By [[thm:main]] item 3, g_λ = g_app + w with |w| ≤ C λ^(K−3) and |∂w| ≤ C λ^(K−4) on Ω, and K ≥ 6. By (a),
g_λ − g0 − λ m1 = Σ_(j=2)^N λ^j m_j + w on Ω ∩ {v > v_end}, and the m_j are bounded with their first derivatives on the
compact set Ω. The statement at order k is [[rem:ue-every-order]] (d) with (a).

(c) Write V = v_end + T and r_q(μ) := (√72 μ l5²)^(1/4). As μ(V) = μ_end, τ_end = max_(v ≤ V)(v − r_q(v)) ≥
V − r_q(μ_end) = v_end + T − r_q(μ_end) > v_end − a, so the interval (v_end − a, τ_end] is nonempty. For τ1 in it,
Σ_τ1 = {a ≤ |x| ≤ b(τ1)} ([[sec:domain]]), and there v = τ1 + r ≥ τ1 + a > v_end. Finally a = q0 − δ0 < q0, the seed
condition μ0 ≥ √72 l5² gives q0⁴ = √72 μ0 l5² ≤ μ0², that is q0 ≤ √μ0, and μ_end = μ0 + (2/9) A² ∫ env² ≥ μ0, so
a < √μ_end. ∎

By (b), with K and the order of [[thm:main]] large enough for the number of derivatives needed, the data of g_λ near the
hole are small in every norm the stability theory uses. The proof of [[thm:settling]] ([[ch:settling-proof]]) places
Hintz's initial surface Σ^IVP in an enlarged domain of the form of Ω, so that its part near the hole lies in the region
after the shell, and there the data of g_λ differ from those of Tangherlini of mass μ_end by O(λ) in every C^j
([[cor:vii-2-3]]).

### Gluing in the class: only the mass is matched {#sec:after-shell-gluing}

Beyond a ball the data of g_λ on Σ^IVP are glued G-equivariantly to exact Tangherlini data on the same surface, by the
method of Chruściel and Delay [CD03] ([[thm:v-3-1]], [[prop:vii-2-2]]). The obstruction of that gluing is the space 𝔎 of
Killing initial data of flat space ([[eq:v-0-4]]). On G-invariant data only its G-invariant part enters, and
𝔎^G = span(e₀), the Killing initial data of ∂_t ([[sec:vii-2]]); so only the mass is matched. The antipodal map −I lies
in G, being the composition of the half-turns of the planes (x1, x2) and (x3, x4), so G-invariant data are invariant
under x ↦ −x; in space dimension 4 the gluing needs no parity condition at all ([[rem:s28-cd03]]). The flux identity
[[eq:v-1-1]] at X = e₀ bounds the distance of the glued mass from μ_end by the size of the data's deviation on the
annulus: the flux of Tangherlini's data is 6π²m at every radius ([[lem:vii-2-1]] (c)), and the remainder q_(e₀) vanishes
to second order at flat data, which gives the mass bound of step (6) of the proof of [[prop:vii-2-2]]. So the glued data
stay O(λ)-close to Tangherlini in the weighted norm of the stability theory at a fixed gluing radius ([[cor:vii-2-3]],
[[rem:s28-mass-bound]]). The stability theorem, run on G-invariant spaces with its choices made equivariant
([[lem:vii-3-1]]), gives a G-invariant development whose final parameters, fixed by G, are a mass alone
([[prop:vii-3-2]]). These are the data and the development of item (i) of [[thm:settling]].

The glued data are not the data of a continuation of g_λ beyond the ball, and their development is not one. The
developments of two data sets that agree on Σ^IVP ∩ {r ≤ R} agree on the domain of dependence of that set; the
statement of settling concerns late times near the hole, outside it.

### Which perturbations the settling theorem reaches {#sec:after-shell-reach}

In this section the letter a denotes an order of decay, not the inner radius of Ω.

*The data of (i).* Fix ℓ0 ∈ (3, 4), and let d_1 ([[thm:iii-k-4-3]]), λ1, δ and the data (γ_λ, k_λ) of item (i) be
those of [[thm:settling]] and its proof run with this ℓ0, and fix λ ≤ λ1. By [[cor:vii-2-3]], (γ_λ, k_λ) are G-invariant
smooth vacuum data on Σ := Σ^IVP, equal to (γ^(m_λ), k^(m_λ)) on Σ ∩ {r ≥ 4R_i}, where R_i is the gluing radius there,
|m_λ − μ_end| ≤ C λ, and (γ^m, k^m) are the data that g^KS_(m,0) induces on Σ far out ([[sec:vii-2]]). We write
b₀ = (μ_end, 0) and R₁ = μ_end^(1/2). For r ≥ R₃, Σ is the graph {t_KS = f(|x|)} in the Kerr–Schild time of
g^KS_(μ_end,0), with

    f := C″ − T_(μ_end)(|x|),      f′(r) = 2μ_end/(r² − μ_end)   (r ≥ 3R₁)                            {#eq:after-shell-f}

([[lem:iii-b-3-7]] (b), [[eq:iii-b-3-3]]), and Σ is identified with {|x| > R₃} ⊂ ℝ⁴ there. We write r = |x|, ρ = r⁻¹,
ω = x/r ∈ 𝕊³ and |𝕊³| = 2π². Constants c, C may depend on λ, ℓ0, d_1, a and the data of (i), never on the radius R,
the size Ξ or the perturbation.

#### The class and its norm {#sec:after-shell-class}

**Definition {#def:after-shell-norm}** (The norm.) Fix r_χ ≥ max(R₃, 4R_i) and χ_c ∈ C^∞(ℝ) with χ_c(r) = 0 for r ≤ r_χ
and χ_c(r) = 1 for r ≥ 2r_χ. Let 𝒜_d be the set of compositions of at most d of the b-vector fields r∂_r and
Ω_ij := x^i∂_j − x^j∂_i, the empty composition included. For w on {r > r_χ} put

    ‖w‖²_(H^(d,ℓ)_b) := Σ_(A∈𝒜_d) ∫_(r_χ)^∞ ∫_(𝕊³) r^(2ℓ) |Aw|² dω dr/r.

A symmetric 2-tensor u on Σ lies in ℋ^d_0 if u ∈ H^d(Σ ∩ {r ≤ 2r_χ}) and, on {r > r_χ}, in the frame ∂_(x^i),

    u_ij = χ_c(r) (ρ² u^((2))_ij(ω) + ρ³ u^((3))_ij(ω)) + ũ_ij,      u^((z))_ij ∈ H^d(𝕊³),   ũ_ij ∈ H^(d,ℓ0)_b.
                                                                                              {#eq:after-shell-expansion}

Its norm is ‖u‖_(ℋ^d_0) := Σ_(i,j)(‖u^((2))_ij‖_(H^d(𝕊³)) + ‖u^((3))_ij‖_(H^d(𝕊³)) + ‖ũ_ij‖_(H^(d,ℓ0)_b)) +
‖u‖_(H^d(Σ∩{r≤2r_χ})). The space ℋ^d_1 is defined likewise with ρ³, ρ⁴ and the weight ℓ0 + 1. For pairs,
‖(u, v)‖_d := ‖u‖_(ℋ^d_0) + ‖v‖_(ℋ^d_1), and the *class* is ℋ^∞ := ⋂_d ℋ^d_0 × ℋ^d_1.

Near infinity the b-vector fields of the radial compactification are spanned by r∂_r = −ρ∂_ρ and the rotation fields
Ω_ij, and dr/r dω is a b-density, so 𝒜_d spans Diff^d_b there. The space ℋ^∞ is therefore the class
H^(∞,(ℰ0,ℓ0))_b × H^(∞,(ℰ0+1,ℓ0+1))_b of [[def:s11-b-analysis]] (5) with the index set ℰ0 = {(j, 0) : j ≥ 2} of
[[eq:vii-0-1]], whose exponents below ℓ0 are 2 and 3, and those of ℰ0 + 1 below ℓ0 + 1 are 3 and 4; and ‖·‖_(d_1) is a
norm in which [[thm:iii-k-4-3]] measures the data. Other choices of the cut-off, of the spanning set or of the sum over
components give the same spaces and equivalent norms ([[def:s11-b-analysis]] (3), (5)). We read δ for this norm; an
equivalent norm changes δ and the constants below by fixed factors. [[thm:settling]] (ii) asks
(γ − γ_λ, k − k_λ) ∈ ℋ^∞ with ‖(γ − γ_λ, k − k_λ)‖_(d_1) < δ.

**Lemma {#lem:after-shell-expansion}** (The expansion is unique.) If b2, b3 ∈ L²(𝕊³) and χ_c (ρ² b2 + ρ³ b3) ∈ H^(0,ℓ0)_b,
then b2 = b3 = 0. So the coefficients u^((z)) are determined by u, the norm is well defined, and ℋ^d_0, ℋ^d_1 are
reflexive Banach spaces: each is a closed subspace of a product of Hilbert spaces (the two descriptions agreeing on
{r_χ < r < 2r_χ}), with an equivalent norm.

*Proof.* For almost every ω with b2(ω) ≠ 0, r^(2ℓ0) |r⁻² b2 + r⁻³ b3|² ≥ (1/2) r^(2ℓ0−4) |b2|² for r large, and
∫^∞ r^(2ℓ0−4) dr/r = ∞ as 2ℓ0 − 4 > 0. Where b2 = 0 ≠ b3, the same holds with the exponent 2ℓ0 − 6 > 0, as ℓ0 > 3. By
Fubini's theorem the weighted integral is infinite unless b2 = b3 = 0 almost everywhere. ∎

**Definition {#def:after-shell-order}** (Perturbations of order a.) Let a > 3/2 and Ξ ∈ (0, 1]. A smooth vacuum data set
(γ, k) on Σ is a *perturbation of order a and size Ξ* if h := γ − γ_λ and κ := k − k_λ satisfy, in the coordinates x
of Σ,

    |∂^β h| ≤ Ξ ⟨r⟩^(−a−|β|),      |∂^β κ| ≤ Ξ ⟨r⟩^(−a−1−|β|)      (|β| ≤ d_1 + 6),               {#eq:after-shell-order}

and the same bounds with some constant C_β in place of Ξ for every β (conormality). Nothing is assumed about
expansions: such a perturbation may or may not lie in the class.

**Definition {#def:after-shell-statement}** (The gluing statement.) For R ≥ 2r_χ let N^((d))_R(γ, k) be the infimum of
‖(γ′ − γ_λ, k′ − k_λ)‖_d over the smooth vacuum data (γ′, k′) on Σ with (γ′ − γ_λ, k′ − k_λ) ∈ ℋ^∞ and (γ′, k′) =
(γ, k) on Σ ∩ {r < R} (the infimum of the empty set being ∞). The statement "(γ, k) agrees on every large ball with data
to which [[thm:settling]] (ii) applies, with smallness uniform as R → ∞" is

(S) there are R₀ and M < δ with N^((d_1))_R(γ, k) ≤ M for every R ≥ R₀;

and (S_∞) is (S) together with sup_(R≥R₀) N^((d))_R(γ, k) < ∞ for every d.

#### Above the threshold: a > ℓ0 {#sec:after-shell-above}

**Proposition {#prop:after-shell-above}** (In the class without gluing.) Let a > ℓ0 and let (γ, k) be a perturbation of
order a and size Ξ. Then (h, κ) ∈ ℋ^∞, all its coefficients u^((z)) vanish, and

    ‖(h, κ)‖_(d_1) ≤ C_1 Ξ (1 + (a − ℓ0)^(−1/2)),                                                 {#eq:after-shell-above}

with C_1 depending only on d_1, r_χ and [[def:after-shell-norm]]. So if C_1 Ξ (1 + (a − ℓ0)^(−1/2)) < δ,
[[thm:settling]] (ii) applies to (γ, k) itself, and (S_∞) holds with (γ′, k′) = (γ, k) for every R.

*Proof.* Each of r∂_r = x^i∂_i and Ω_ij has coefficients linear in x. So a composition A ∈ 𝒜_d is
Σ_(|β|≤d) c_β ∂^β with c_β homogeneous polynomials of degree |β|, and |Ah| ≤ C Σ_(|β|≤d) r^(|β|) |∂^β h| ≤ C Ξ r^(−a)
on {r > r_χ} by [[eq:after-shell-order]], for d ≤ d_1 + 6. Take the coefficients zero, so ũ = h. Then

    ‖r^(ℓ0) A h‖²_(L²({r>r_χ}, dr/r dω)) ≤ C² Ξ² 2π² ∫_(r_χ)^∞ r^(2(ℓ0−a)) dr/r = C² Ξ² 2π² r_χ^(2(ℓ0−a)) / (2(a − ℓ0)).

For κ the weight is ℓ0 + 1 and the order a + 1, with the same integral. On {r ≤ 2r_χ}, ‖(h, κ)‖_(H^(d_1)) ≤ C Ξ by
[[eq:after-shell-order]]. With C_β in place of Ξ the same argument gives every d, so (h, κ) ∈ ℋ^∞. ∎

**Corollary {#cor:after-shell-every-rate}** (Every rate above 3.) [[thm:settling]] holds for every ℓ0 ∈ (3, 4), its
constants ε_K, λ1, δ and its data of (i) depending on ℓ0, which its statement fixes first. Let a > 3 and run it with
ℓ0 ∈ (3, min(a, 4)). Then its item (ii) covers every perturbation of order a of its data of (i) with Ξ below
δ/(C_1(1 + (a − ℓ0)^(−1/2))), at the rate t*^(−2−ε) for every ε < ε_K, where ε_K < ℓ0 − 3 < a − 3.

*Proof.* [[prop:after-shell-above]] with that ℓ0. The bound ε_K < ℓ0 − 3 is the chain ε_K < ε_+ < ℓ_I − 3 with
ℓ_I < ℓ0 of [[thm:settling]]. ∎

In four dimensions Hintz's theorem asks, "for structureless data", "O(r^(−3−ϵ0))-decay" ([Hin26, p. 2, footnote 1]);
[[cor:after-shell-every-rate]] is the five-dimensional counterpart. The threshold is sharp: at a = ℓ0 the integral of
the proof is log(R/r_χ) on {r_χ < r < R}, and [[prop:after-shell-outside]] gives perturbations of order ℓ0 outside the
class.

#### The gluing statement is class membership {#sec:after-shell-membership}

**Proposition {#prop:after-shell-membership}** Let (γ, k) be smooth vacuum data on Σ, (h, κ) := (γ − γ_λ, k − k_λ), and
d ≥ 0.

(a) R ↦ N^((d))_R(γ, k) is nondecreasing. Its limit is at least ‖(h, κ)‖_d, read as ∞ when (h, κ) ∉ ℋ^d_0 × ℋ^d_1.

(b) If (h, κ) ∈ ℋ^∞, then N^((d))_R(γ, k) ≤ ‖(h, κ)‖_d for every R, so the limit equals ‖(h, κ)‖_d.

*Proof.* (a) Data equal to (γ, k) on {r < R′} are equal to it on {r < R} for R < R′, so the infimum over the smaller
set is larger. Let L := lim_R N^((d))_R < ∞. Choose R_n → ∞ and admissible (γ′_n, k′_n) with
u_n := (γ′_n − γ_λ, k′_n − k_λ) and ‖u_n‖_d ≤ L + 1/n. The space ℋ^d_0 × ℋ^d_1 is reflexive
([[lem:after-shell-expansion]]), so a subsequence converges weakly to some u, and ‖u‖_d ≤ L, the norm being convex and
continuous. For a compact K ⊂ Σ the restriction ℋ^d_0 × ℋ^d_1 → L²(K) is continuous, the weights being bounded on K,
so u_n|_K converges weakly to u|_K in L²(K). But u_n|_K = (h, κ)|_K once R_n > sup_K r. Hence u = (h, κ) on every
compact set, (h, κ) ∈ ℋ^d_0 × ℋ^d_1 and ‖(h, κ)‖_d ≤ L. (b) (γ, k) itself is admissible for every R. ∎

**Corollary {#cor:after-shell-membership}** (S) implies (h, κ) ∈ ℋ^(d_1)_0 × ℋ^(d_1)_1 with ‖(h, κ)‖_(d_1) ≤ M < δ.
(S_∞) holds if and only if (h, κ) ∈ ℋ^∞ with ‖(h, κ)‖_(d_1) < δ, that is, if and only if [[thm:settling]] (ii)
applies to (γ, k) itself.

*Proof.* [[prop:after-shell-membership]] (a) at d_1, and at every d for (S_∞); the converse is
[[prop:after-shell-membership]] (b). ∎

So, whatever the decay rate, gluing uniformly in the radius gives nothing beyond (ii) applied directly.
[[prop:after-shell-membership]] uses neither a decay rate nor the vacuum condition of the competitors, only the norm.

#### The obstruction at every rate a ≤ ℓ0 {#sec:after-shell-obstruction}

**Lemma {#lem:after-shell-distance}** (A positive distance.) Let q ∈ ℝ and let p1 ≠ p2 be real. On (1/2, 1) with the
measure ds/s, the functions s^q cos log s, s^q sin log s, s^(p1) and s^(p2) are linearly independent. Hence

    ϰ(q; p1, p2) := min_(θ∈ℝ) dist_(L²((1/2,1), ds/s)) (s^q cos(log s + θ), span(s^(p1), s^(p2))) > 0,

and ϰ² is the least eigenvalue of the Schur complement S = G11 − G12 G22⁻¹ G21 of the Gram matrix of the four
functions, block 1 being the pair (s^q cos log s, s^q sin log s). We write ϰ(a, ℓ0) := ϰ(ℓ0 − a; ℓ0 − 2, ℓ0 − 3).

*Proof.* With t = log s ∈ (−log 2, 0), a real relation α s^q cos log s + β s^q sin log s + γ1 s^(p1) + γ2 s^(p2) = 0
reads ((α − iβ)/2) e^((q+i)t) + ((α + iβ)/2) e^((q−i)t) + γ1 e^(p1 t) + γ2 e^(p2 t) = 0. The exponents q ± i, p1, p2
are pairwise distinct, and the Wronskian of e^(z1 t), …, e^(z4 t) is e^((z1+⋯+z4)t) Π_(j<k)(z_k − z_j) ≠ 0, a
Vandermonde determinant; so all coefficients vanish. Now s^q cos(log s + θ) = cos θ s^q cos log s − sin θ s^q sin log s
is a nonzero combination of the first two functions, hence not in the span of the last two. By least squares its
squared distance from that span is vᵀ S v with v = (cos θ, −sin θ), and S is positive definite because the Gram matrix
is. The minimum over the unit circle is the least eigenvalue of S. ∎

**Remark {#rem:after-shell-distance-values}** (Numerical observation.) Evaluated by quadrature of the Gram matrix,
ϰ(5/2, 7/2) ≈ 7.655 × 10⁻⁴ and ϰ(7/2, 7/2) ≈ 1.737 × 10⁻³. The constant is small because the interval (1/2, 1) is
short in the variable log s. No proof uses these values; only the positivity of [[lem:after-shell-distance]] is used.

**Proposition {#prop:after-shell-outside}** (Perturbations outside the class.) Let 3/2 < a ≤ ℓ0. Put r_2 := 2r_χ, take
a cut-off χ_1(r) equal to 0 for r ≤ r_2 and to 1 for r ≥ 2r_2, and let

    ζ_a(r) := r^(1−a) cos log r,    φ_Ξ(r) := r + Ξ χ_1(r) ζ_a(r),    Ψ_Ξ(x) := φ_Ξ(|x|) x/|x|,
    (γ_Ξ, k_Ξ) := Ψ_Ξ*(γ_λ, k_λ).

(a) There is Ξ1 > 0 such that for 0 < Ξ ≤ Ξ1, Ψ_Ξ is an O(4)-equivariant diffeomorphism of Σ, the identity on
{r ≤ r_2}, and (γ_Ξ, k_Ξ) is G-invariant smooth vacuum data, isometric to (γ_λ, k_λ), and a perturbation of order a and
size C_P Ξ.

(b) There are R_P ≥ 4r_2 and c_P := (2π²)^(1/2) A_a ϰ(a, ℓ0), with A_a := ((4 − a)² + 1)^(1/2), such that for
0 < Ξ ≤ Ξ1, R ≥ R_P and every d,

    N^((d))_R(γ_Ξ, k_Ξ) ≥ c_P Ξ R^(ℓ0−a)   (a < ℓ0),      N^((d))_R(γ_Ξ, k_Ξ) ≥ c_P Ξ (log₂(R/R_P))^(1/2)   (a = ℓ0).
                                                                                                  {#eq:after-shell-lower}

(c) Hence (S) fails for (γ_Ξ, k_Ξ) at every Ξ ∈ (0, Ξ1]. For a < ℓ0, once R > max(R_P, (δ/(c_P Ξ))^(1/(ℓ0−a))), no
data in the class that agree with (γ_Ξ, k_Ξ) on {r < R} have norm ‖·‖_(d_1) < δ; for a = ℓ0, once
R > R_P 2^((δ/(c_P Ξ))²).

*Proof.* (a) |∂_r^j(χ_1 ζ_a)| ≤ C_j r^(1−a−j), so φ_Ξ′ ≥ 1/2 for Ξ ≤ Ξ1 := (2 sup|(χ_1 ζ_a)′|)⁻¹. Also φ_Ξ(r) = r for
r ≤ r_2 and φ_Ξ(r) → ∞, so φ_Ξ is an increasing bijection of [r_♭, ∞) and Ψ_Ξ a diffeomorphism, with inverse
x ↦ φ_Ξ⁻¹(|x|) x/|x|, commuting with O(4). The constraint map is natural under diffeomorphisms, so the pull-back is
vacuum. It is G-invariant, as (γ_λ, k_λ) is and G ⊂ O(4). On {r ≥ r_2} ⊂ {r ≥ 4R_i}, which Ψ_Ξ maps to itself, the
data are (γ^(m_λ), k^(m_λ)), which are O(4)-invariant ([[lem:vii-2-1]] (b)). An O(4)-invariant symmetric 2-tensor is
A(r) x̂ ⊗ x̂ + B(r)(δ − x̂ ⊗ x̂): the stabiliser O(3) of x̂ acts irreducibly on x̂^⊥ and fixes no vector there, so an
invariant symmetric bilinear form has no x̂ ⊗ x̂^⊥ part and is a multiple of the identity on x̂^⊥. By [[lem:vii-2-1]] (a),
α := A − 1 and β := B − 1 lie in ρ²C^∞, and k^(m_λ) = C x̂ ⊗ x̂ + D(δ − x̂ ⊗ x̂) with C, D ∈ ρ³C^∞. Since
A x̂ ⊗ x̂ + B(δ − x̂ ⊗ x̂) = A dr² + B r² g_(𝕊³), a radial map r ↦ φ(r) pulls it back to

    Ψ*(A x̂ ⊗ x̂ + B(δ − x̂ ⊗ x̂)) = A(φ) φ′² x̂ ⊗ x̂ + B(φ) (φ²/r²)(δ − x̂ ⊗ x̂).               {#eq:after-shell-radial}

Hence h = [A(φ_Ξ) φ_Ξ′² − A] x̂ ⊗ x̂ + [B(φ_Ξ) φ_Ξ²/r² − B](δ − x̂ ⊗ x̂) on {r ≥ r_2} and h = 0 inside, and likewise κ with
(C, D). Write A(φ) φ′² − A = (φ′² − 1) + (α(φ) − α) φ′² + α(φ′² − 1), with α(φ) − α = Ξ χ_1 ζ_a ∫_0^1 α′(r + sΞ χ_1 ζ_a)
ds. The three terms are conormal, with constants times Ξ, of orders a, a + 2 and a + 2; the B terms likewise, and the
(C, D) terms are of order a + 3. The components x̂_i x̂_j lie in C^∞ of the radial compactification. So
[[eq:after-shell-order]] holds with C_P Ξ in place of Ξ, and with C_β Ξ at all orders.

(b) Let R ≥ 4r_2 and let (γ′, k′) be admissible for N^((d))_R. Write u := γ′ − γ_λ as in
[[eq:after-shell-expansion]], and Γ := {R/2 < r < R}, which lies in {χ_c = 1} ∩ {χ_1 = 1} ∩ {r < R}. On Γ, u = h, so
ũ_ij = h_ij − ρ² u^((2))_ij(ω) − ρ³ u^((3))_ij(ω), and

    ‖(u, ·)‖_d ≥ Σ_(i,j) ‖r^(ℓ0) ũ_ij‖_(L²(Γ)) ≥ ‖r^(ℓ0) Σ_i ũ_ii‖_(L²(Γ)),     Σ_i ũ_ii = τ(r) − ρ² b2(ω) − ρ³ b3(ω),

with τ := tr_δ h, which is radial, and b_z := tr u^((z)). Integrating first in r at fixed ω,

    ‖r^(ℓ0)(τ − ρ² b2 − ρ³ b3)‖_(L²(Γ, dr/r dω)) ≥ (2π²)^(1/2) inf_(β2,β3∈ℝ) ‖r^(ℓ0)(τ − β2 r⁻² − β3 r⁻³)‖_(L²((R/2,R), dr/r)).

On Γ, φ_Ξ = r + Ξ ζ_a. By [[eq:after-shell-radial]], τ = (φ_Ξ′² − 1) + 3(φ_Ξ²/r² − 1) + e_αβ, where e_αβ collects the
α and β terms. With φ_Ξ′ = 1 + Ξ ζ_a′, ζ_a′ = r^(−a)((1 − a) cos log r − sin log r), and φ_Ξ/r = 1 + Ξ r^(−a) cos log r,

    τ = 2Ξ r^(−a)((4 − a) cos log r − sin log r) + Ξ² (ζ_a′² + 3 ζ_a²/r²) + e_αβ.

As in (a), |e_αβ| ≤ C Ξ r^(−2−a). Since 4 − a > 0, (4 − a) cos t − sin t = A_a cos(t + φ_a) with φ_a := arctan(1/(4 − a)),
so τ = 2Ξ A_a r^(−a) cos(log r + φ_a) + e with |e| ≤ C_e(Ξ r^(−2−a) + Ξ² r^(−2a)). Substitute r = Rs, so that
dr/r = ds/s and r^(ℓ0) β_z r^(−z) = β_z R^(ℓ0−z) s^(ℓ0−z). The main term contributes

    inf_β ‖r^(ℓ0)(2Ξ A_a r^(−a) cos(log r + φ_a) − β2 r⁻² − β3 r⁻³)‖
        = 2Ξ A_a R^(ℓ0−a) dist(s^(ℓ0−a) cos(log s + log R + φ_a), span(s^(ℓ0−2), s^(ℓ0−3))) ≥ 2Ξ A_a ϰ(a, ℓ0) R^(ℓ0−a)

by [[lem:after-shell-distance]]. On (R/2, R), r^(ℓ0−2−a) ≤ 2^(2+a) R^(ℓ0−2−a) and r^(ℓ0−2a) ≤ 2^(2a) R^(ℓ0−2a), so
‖r^(ℓ0) e‖_(L²((R/2,R), dr/r)) ≤ (log 2)^(1/2) C_e (2^(2+a) Ξ R^(ℓ0−2−a) + 2^(2a) Ξ² R^(ℓ0−2a)). For R ≥ R_P this is at
most Ξ A_a ϰ R^(ℓ0−a), uniformly in Ξ ≤ 1, since R⁻² and R^(−a) tend to 0. By the triangle inequality the infimum is at
least Ξ A_a ϰ R^(ℓ0−a), which gives [[eq:after-shell-lower]] for a < ℓ0. For a = ℓ0, apply the same to the disjoint
annuli Γ_j := {2^(−j−1) R < r < 2^(−j) R} with 2^(−j) R ≥ R_P. The coefficients b2, b3 are common to all of them, so the
square of the norm over their union is at least the sum of the squares of the separate infima, each at least
(c_P Ξ)², over ⌊log₂(R/R_P)⌋ + 1 ≥ log₂(R/R_P) annuli.

(c) follows from [[eq:after-shell-lower]] at d = d_1: N^((d_1))_R ≥ δ in the stated ranges, and N^((d_1))_R → ∞. ∎

**Remark {#rem:after-shell-pure-gauge}** (What the examples show.) The examples are pure gauge. Their maximal
developments are isometric to that of the data of (i), so the obstruction lies in the norm of [[thm:settling]] (ii),
which a diffeomorphism of the initial surface does not preserve, and not in the geometry; settling itself is not
confined to the class. The examples are radial, hence G-invariant: the obstruction persists in the symmetry class of
(i). [[prop:after-shell-membership]] holds for every perturbation, gauge or not; the examples serve only to show that at
every rate a ≤ ℓ0 some vacuum perturbation lies outside the class. The function R ↦ dist(s^(ℓ0−a) cos(log s + log R +
φ_a), span(s^(ℓ0−2), s^(ℓ0−3))) in the proof is periodic in log R with period 2π, with minimum ϰ(a, ℓ0).

#### The Myers–Perry data on Hintz's surface, and the upper bound {#sec:after-shell-upper}

We use the family of [[def:v-2-1]] with base mass μ_end: for p = (m, A, w, c) in its range, 𝔤_p = 𝒫_p* g^KS_(m,A) with
𝒫_p(y) = Λ_w y + (0, c), in coordinates y = (y⁰, y) of ℝ^(1+4), and (g_p, K_p) are its data on the slice {y⁰ = 0}. Let
(g̃_p, K̃_p) be the data that 𝔤_p induces on the graph {y⁰ = f(|y|)} over {|y| > R_F}, f as in [[eq:after-shell-f]],
identified with Σ ∩ {r > R_F} by x = y. Write p_λ := (m_λ, 0, 0, 0), p₂ := (m, w) and Δp := p − p_λ. Let 𝔔_X be the
charges of [[prop:v-1-3]], 𝔟_X and q_X those of [[lem:v-1-2]], and d(X) the degree of X in the basis [[eq:v-0-4]]. A
Cartesian derivative gains a power of ρ near infinity: since r²∂_i = x_i r∂_r + Σ_j x_j Ω_ji,

    ∂_i = ρ (ω_i r∂_r + Σ_j ω_j Ω_ji),                                                             {#eq:after-shell-gain}

and as ω_j ∈ C^∞ and r∂_r, Ω_ji preserve ρ^p C^∞ of the radial compactification, ∂_i maps ρ^p C^∞ into ρ^(p+1) C^∞.

**Lemma {#lem:after-shell-mp-data}** (The Myers–Perry data on Hintz's surface.) For R_F large:

(a) (g̃_p, K̃_p) are smooth vacuum data; g̃_p − δ ∈ ρ²C^∞ and K̃_p ∈ ρ³C^∞ of the compactified {r ≥ R_F}, smoothly in p;
and (g̃_(p_λ), K̃_(p_λ)) = (γ^(m_λ), k^(m_λ)).

(b) The ρ² coefficient of g̃_p and the ρ³ coefficient of K̃_p depend on p only through p₂. Hence
g̃_p − γ^(m_λ) = ρ² a2(p) + ρ³ a3(p) + ρ⁴ ℛ0(p), with |a2|_(C^m(𝕊³)) ≤ C_m |Δp₂| and
|a3|_(C^m(𝕊³)) + ‖ℛ0‖_(C^m) ≤ C_m |Δp|; the same holds for K̃_p − k^(m_λ) with ρ³, ρ⁴, ρ⁵.

(c) The charge map 𝔮̃(p) := (𝔔_X(g̃_p, K̃_p))_X is C¹ and D𝔮̃(p_λ) is invertible. Its degree-0 part
𝔮̃_0 := (𝔔_(e₀), 𝔔_(e_l)), the energy and momentum, depends only on p₂, and p₂ ↦ 𝔮̃_0 has invertible derivative at
(m_λ, 0). So there are r_U, r_V and L with |Δp| ≤ L |𝔮̃(p) − 𝔮̃(p_λ)| and |Δp₂| ≤ L |𝔮̃_0(p) − 𝔮̃_0(p_λ)| for
|Δp| < r_U; and 𝔮̃ maps {|Δp| < r_U} homeomorphically onto a set containing the ball of radius r_V about 𝔮̃(p_λ). We
write p(Q) for the inverse.

(d) The members of [[def:v-2-1]] on the slices {y⁰ = 0} satisfy g̃_p − g_p ∈ ρ³C^∞ and

    K̃_p − K_p = ∇²f + ρ⁴C^∞,      tr ∇²f = 2μ_end r⁻³ + O(r⁻⁵),                                {#eq:after-shell-hessian}

∇²f the Euclidean Hessian. In particular K_(p_λ) − k^(m_λ) = −∇²f + ρ⁵C^∞ has a ρ³ coefficient of size μ_end, which
does not depend on any perturbation.

*Proof.* (a) g^KS_(m,A) − η = H_(m,A) k_A ⊗ k_A is independent of t, with H_(m,A) ∈ |x|⁻²C^∞ and the coefficients of k_A
in C^∞ of the compactification, smoothly in (m, A) (proof of [[prop:iii-b-3-6]]). The map 𝒫_p is affine, and on the
graph the spatial point of 𝒫_p(f(|y|), y) is x(y) = L_w y + f(|y|) b_w + c, where L_w, the spatial block of Λ_w, is
invertible and b_w ∈ ℝ⁴. As T_(μ_end) ∈ |x|⁻¹C^∞ ([[lem:iii-b-3-5]] (a)), f lies in C^∞ of the compactification near
infinity, so |x(y)|⁻¹ = |y|⁻¹ |L_w ŷ + |y|⁻¹(f b_w + c)|⁻¹ is ρ times a smooth positive function of (ρ, ŷ), and x̂(y) is
smooth in (ρ, ŷ): y ↦ x(y) extends to a diffeomorphism near the boundary of the compactification and preserves
ρ^j C^∞. The components of 𝔤_p − η are those of g^KS_(m,A) − η composed with 𝒫_p and multiplied by the constant matrix
Λ_w; so on the graph they lie in ρ²C^∞, and by [[eq:after-shell-gain]] their first derivatives lie in ρ³C^∞, smoothly
in p. The data of the graph are smooth functions of 𝔤_p and ∂𝔤_p at the graph and of ∂f ∈ ρ²C^∞ and ∂²f ∈ ρ³C^∞
([[eq:after-shell-f]]): the induced metric is g̃_ij = G_ij + G_(0i) ∂_jf + G_(0j) ∂_if + G_00 ∂_if ∂_jf, with G := 𝔤_p,
and the second fundamental form, given by [[eq:v-0-2]] in the coordinates (y⁰ − f(|y|), y), is linear in (∂G, ∂²f) with
coefficients smooth in (G, ∂f). They equal (δ, 0) at G = η and f constant. This gives g̃_p − δ ∈ ρ²C^∞ and
K̃_p ∈ ρ³C^∞. For R_F large the graph is spacelike, as its conormal dy⁰ − df has 𝔤_p⁻¹-norm −1 + O(ρ²), and 𝔤_p is
Ricci-flat ([[prop:iii-b-3-4]]), so the data are vacuum. At p_λ, 𝒫_(p_λ) = id and the data are (γ^(m_λ), k^(m_λ)) by
definition ([[sec:vii-2]]).

(b) g^KS_(m,A) − g^KS_(m,0) ∈ |x|⁻³C^∞, since H_(m,A) − H_(m,0) ∈ |x|⁻⁴C^∞ and ℓ_A − ℓ_0 ∈ |x|⁻¹C^∞ (proof of
[[prop:iii-b-3-6]]). A translation changes a function F ∈ ρ²C^∞ by F(x + c) − F(x) = c · ∫_0^1 ∂F(x + sc) ds ∈ ρ³C^∞,
by [[eq:after-shell-gain]]. So 𝔤_p − 𝔤_((m,0,w,0)) ∈ ρ³C^∞ on the graph, in the sense of (a). On the graph,
g̃ − δ = (G − η)_ij(f, y) + ρ⁴C^∞, as the terms G_(0i) ∂_jf and G_00 ∂_if ∂_jf lie in ρ⁴C^∞; and
(G − η)_ij(f, y) − (G − η)_ij(0, y) = f ∫_0^1 ∂_0 G_ij(sf, y) ds ∈ ρ³C^∞. So the ρ² coefficient of g̃_p is that of
(𝔤_((m,0,w,0)) − η)_ij(0, y), a function of p₂. The ρ³ coefficient of K̃_p is that of the part of K̃_p linear in
∂𝔤_((m,0,w,0)) plus that of ∇²f, which does not depend on p. The bounds follow by the mean value theorem in p, the
coefficients being smooth in p and equal at p_λ to those of (γ^(m_λ), k^(m_λ)), with a2 a function of p₂.

(d) In the coordinates y′⁰ := y⁰ − f(|y|), y′ := y, the graph is {y′⁰ = 0}, and with G := 𝔤_p the new shift, metric and
lapse are β′ = β + G_00 ∂f = β − ∂f + ρ⁴C^∞, g′ − g ∈ ρ⁴C^∞ and N′ − N ∈ ρ⁴C^∞, at the same point, since G_00 + 1,
G_(0i) and G^(0i) lie in ρ²C^∞ and ∂f ∈ ρ²C^∞. The values on the graph are taken at (f, y) instead of (0, y), and
G(f, y) − G(0, y) = f ∂_0 G(0, y) + ρ⁴C^∞, where ∂_0 G_p = O(|w| ρ³). Inserting these in [[eq:v-0-2]], the term
−D′_iβ′_j − D′_jβ′_i contributes 2∂_i∂_j f + ρ⁵C^∞, and 1/(2N′) = 1/2 + ρ²C^∞, which gives K̃_p − K_p = ∇²f + ρ⁴C^∞
and g̃_p − g_p ∈ ρ³C^∞. At w = 0, G_p does not depend on y⁰, there is no change of the point of evaluation, and
K̃_p − K_p − ∇²f ∈ ρ⁵C^∞; this is used in (c). For the trace: f is radial, ∇²f = f″ x̂ ⊗ x̂ + (f′/r)(δ − x̂ ⊗ x̂), and by
[[eq:after-shell-f]] f′ = 2μ_end r⁻² + 2μ_end² r⁻⁴ + O(r⁻⁶), so tr ∇²f = f″ + 3f′/r = (−4μ_end + 6μ_end) r⁻³ + O(r⁻⁵).
At p_λ, (g_(p_λ), K_(p_λ)) are the data of g^KS_(m_λ,0) on {t_KS = 0}, and their difference from (γ^(m_λ), k^(m_λ)) is
the case w = 0 of the above, with the sign of ∇²f reversed.

(c) C¹ and O(4)-equivariance follow as in the proof of [[prop:v-2-3]], since (a) gives the bounds of [[lem:v-2-2]] and
the graph is O(4)-invariant. By Schur's lemma, as there, D𝔮̃(p_λ) consists of scalars c̃_E (from m to 𝔔_(e₀)) and c̃_J
(from A to (𝔔_(e_ab)), times I₆), and a matrix (ã11 ã12; ã21 ã22) ⊗ I₄ from (w, c) to (𝔔_(e_l), 𝔔_(e′_l)), with zero
elsewhere. We compare with the charges 𝔮 of the members (g_p, K_p), for which the proof of [[prop:v-2-3]] computes, at
every base point (m, 0, 0, 0) with m in place of m₀, c_E = 6π², a11 = a22 = −6π²m, a12 = 0 and c_J = −4π²m.

The flux 𝔟_X is linear in the data, a degree-0 flux of a change in ρ³C^∞ of the metric or ρ⁴C^∞ of K tends to 0
(ρ⁴ · r³ → 0), and the term ∇²f carries no momentum at any radius: (∇²f − Δf δ)x̂ = −3(f′/r) x̂, which is odd. So by
(d), 𝔮̃_0 = 𝔮_0 for every p. By the argument of (b) on {y⁰ = 0}, g_p − g_((m,0,w,0)) ∈ ρ³C^∞ and
K_p − K_((m,0,w,0)) ∈ ρ⁴C^∞, so 𝔮_0(p) = 𝔮_0(m, 0, w, 0): the energy and momentum depend only on p₂. Hence c̃_E = c_E,
ã11 = a11 and ã12 = a12 = 0. At w = 0 the differences of the graph's data from the slice's are ρ⁴C^∞ in the metric and
∇²f + ρ⁵C^∞ in K, smoothly in (m, A, c), by (d). The term ∇²f does not depend on p and carries no angular momentum:
(Wx) · ∇²f · x̂ = f″ (Wx) · x̂ = 0 and (Wx) · x̂ = 0 for W antisymmetric. The degree-1 fluxes of the A- and c-derivatives
of the rest tend to 0, as r · ρ⁵ · r³ → 0 and ρ⁴ · r³ → 0. So c̃_J = c_J and ã22 = a22, and
det D𝔮̃(p_λ) = c̃_E (ã11 ã22)⁴ c̃_J⁶ = 6π² (6π² m_λ)⁸ (4π² m_λ)⁶ ≠ 0. The p₂-block of D𝔮̃_0 is diag(c_E, a11 I₄),
invertible. The rest is the inverse function theorem. ∎

So, by [[lem:vii-0-1]], a smooth vacuum data set on Σ that agrees for r large with the data (g̃_p, K̃_p) of a nearby
translated, rotated and boosted Myers–Perry metric differs from (γ_λ, k_λ) by an element of the class: the class
contains these data on Hintz's own surface. On the slices {y⁰ = 0} of [[def:v-2-1]] it does not: by (d), already at p_λ
the second fundamental form differs from k^(m_λ) by a fixed term of order r⁻³, of size μ_end, so the members of
[[def:v-2-1]] are at a distance from (γ_λ, k_λ), in the norm of the class, that no smallness of a perturbation removes.
This is why the gluing below takes its family on Σ, as [[prop:vii-2-2]] does in the class. That the mass and the boost
are fixed by the energy and momentum alone (c) is what makes the coefficient of ρ² of the glued data decay with R when
a > 2 ([[eq:after-shell-params]] below).

**Lemma {#lem:after-shell-charges}** (Charges.) (a) For data z_i = (δ + h_i, K_i), i = 1, 2, with |h_i| ≤ 1/2, put
m(z) := Σ_(|β|≤2) r^(|β|) |∂^β h| + Σ_(|β|≤1) r^(1+|β|) |∂^β K|. If m(z_1), m(z_2) ≤ 1, then

    |q_X(z_1) − q_X(z_2)| ≤ C (1 + r)^(d(X)) r⁻² (m(z_1) + m(z_2)) m(z_1 − z_2).               {#eq:after-shell-bilinear}

(b) For a perturbation of order a and size Ξ, with Δ𝔔_X := 𝔔_X(γ, k) − 𝔮̃_X(p_λ): Δ𝔔_X = 0 if a > 2 + d(X), and
|Δ𝔔_X| ≤ C_1′ Ξ in every case.

*Proof.* (a) By the proof of [[lem:v-1-2]], q_X is linear in (N, Y), with |N| + |Y| ≤ C(1 + r)^(d(X)). The scalar
curvature is g⁻¹g⁻¹∂²h + g⁻¹g⁻¹g⁻¹ ∂h ∂h, the K-terms of ρ are quadratic in K with coefficients smooth in h, J is
g⁻¹∂K + g⁻¹g⁻¹ ∂h K, and (det g)^(1/2) is smooth in h. Subtracting the linear part, q_X is a sum of terms c(h)·P, where
either P is quadratic, one of ∂h ∂h, ∂h K, K K, or P is linear, ∂²h or ∂K, and then c(0) = 0. Telescoping each product
and applying the mean value theorem to the coefficients c, each term of the difference is at most C r⁻² times
m(z_1 − z_2) and a factor m(z_1) or m(z_2), with the bound m(z_i) ≤ 1 absorbing the cubic terms of the coefficients'
differences; this is [[eq:after-shell-bilinear]].

(b) 𝔔_X(γ, k) exists by [[prop:v-1-3]] with α = min(a, 2) > 3/2: (γ_λ, k_λ) = (γ^(m_λ), k^(m_λ)) far out
([[lem:vii-2-1]] (a)), and (h, κ) satisfies [[eq:after-shell-order]]. Also 𝔮̃_X(p_λ) = 𝔔_X(γ_λ, k_λ), the two data sets
agreeing for r ≥ 4R_i. As 𝔟_X is linear, Δ𝔔_X = lim_ϱ ∮_(S_ϱ) 𝔟_X(h, κ), and |∮_(S_ϱ) 𝔟_X(h, κ)| ≤ C Ξ ϱ^(2+d−a), which
tends to 0 if a > 2 + d. In general, put R_λ := max(r_χ, R_F, 1) and subtract the flux identity [[eq:v-1-1]] for
(γ_λ, k_λ) on Γ(R_λ, ϱ) from that for (γ, k); both are vacuum. By [[eq:after-shell-bilinear]], with m(γ_λ, k_λ) ≤ C r⁻²
and m(h, κ) ≤ C Ξ r^(−a), |Δ𝔔_X| ≤ C Ξ R_λ^(2+d−a) + C Ξ ∫_(R_λ)^∞ r^(d−2)(r⁻² + Ξ r^(−a)) r^(−a) r³ dr. The integrand is
O(r^(d−1−a) + r^(d+1−2a)), and for d ∈ {0, 1} and a > 3/2 both exponents are below −1: d − 1 − a ≤ −a < −1 and
d + 1 − 2a ≤ 2 − 2a < −1. ∎

**Proposition {#prop:after-shell-gluing}** (Gluing to the Myers–Perry data on Hintz's surface, with the error.) Let
3/2 < a ≤ ℓ0 and k_g := d_1 + 2, the order of the gluing. There are R_G, Ξ0 and C with the following property. For every
perturbation (γ, k) of order a and size Ξ ≤ Ξ0, and every R ≥ R_G, there are p_R and smooth vacuum data (γ̂_R, k̂_R) on
Σ, equal to (γ, k) on {r ≤ R} and to (g̃_(p_R), K̃_(p_R)) on {r ≥ 4R}, with

    |Δp_(R,2)| ≤ C Ξ R^(min(0, 2−a)),      |Δp_R| ≤ C Ξ R^(min(0, 3−a)),                         {#eq:after-shell-params}

    sup_(R≤r≤4R) ( Σ_(|β|≤k_g−1) r^(|β|) |∂^β(γ̂_R − γ_λ)| + Σ_(|β|≤k_g−2) r^(1+|β|) |∂^β(k̂_R − k_λ)| ) ≤ C Ξ R^(−a).
                                                                                                {#eq:after-shell-annulus}

*Proof.* We follow the proof of [[thm:v-3-1]], with k_g in place of 3 as in [[prop:vii-2-2]] (the solvability statement
[[lem:s28-setting]] allows every integer above n/2), the data on {r > R₀} being (γ, k) with R₀ := max(R_F, r_χ), and we
make six changes. By [[eq:after-shell-order]], |||(γ, k)|||_(min(a,2), k_g+4) < ∞ ([[eq:v-0-3]]), as k_g + 4 = d_1 + 6.

(1) *The family and the box.* The members (g̃_p, K̃_p) of [[lem:after-shell-mp-data]] replace those of [[def:v-2-1]]:
its (a) gives the bounds of [[lem:v-2-2]] and its (c) the inverse p(Q) of [[cor:v-2-4]]. In Step 2 let Q range over the
box 𝔅_R := {Q : |Q_X − 𝔮̃_X(p_λ)| ≤ r_X for every X}, with r_X := C_0 Ξ R^(min(0, 2+d(X)−a)) and C_0 := C_1′ + 1. Then
𝔅_R lies in the ball of radius r_V once √15 C_0 Ξ0 < r_V. The five degree-0 radii are C_0 Ξ R^(min(0,2−a)), and the ten
others C_0 Ξ R^(min(0,3−a)), the larger. So for Q ∈ 𝔅_R, [[lem:after-shell-mp-data]] (c) gives
|Δp₂| ≤ √5 L C_0 Ξ R^(min(0,2−a)) and |Δp| ≤ √15 L C_0 Ξ R^(min(0,3−a)), where Δp := p(Q) − p_λ.

(2) *The source in relative form.* On 𝒜 = Γ̄(1, 4) write a_R := 𝒮_R(γ, k) and b_Q := 𝒮_R(g̃_(p(Q)), K̃_(p(Q))), with
𝒮_R of [[lem:v-1-4]]. Both are vacuum, and the approximate data of Step 2 are u_(Q,R) = b_Q + χ(a_R − b_Q). The
constraint map is smooth near flat data and vanishes at b_Q, so ‖(J, ρ)(u_(Q,R))‖_(C^(k_g+1)) ≤
C ‖a_R − b_Q‖_(C^(k_g+3) × C^(k_g+4)) ≤ C θ_R(Q), with

    θ_R(Q) := Ξ R^(−a) + |Δp₂| R⁻² + |Δp| R⁻³ ≤ C (1 + C_0) Ξ R^(−a).                             {#eq:after-shell-theta}

Here we used the scaling ‖𝒮_R u‖_(C^m(𝒜)) ≤ C sup_(R≤r≤4R) Σ_(|β|≤m) r^(|β|) |∂^β u| (one more power of r for the
second fundamental form), the bounds [[eq:after-shell-order]] for a_R − 𝒮_R(γ_λ, k_λ), and [[lem:after-shell-mp-data]]
(b) for b_Q − 𝒮_R(γ_λ, k_λ), as (g̃_(p_λ), K̃_(p_λ)) = (γ_λ, k_λ) on {r ≥ R}. The inequality in [[eq:after-shell-theta]]
holds by (1): min(0, 2 − a) − 2 ≤ −a and min(0, 3 − a) − 3 ≤ −a. By the bound of Step 1 and [[lem:v-3-2]],
‖δu_(Q,R)‖_(C^(k_g−1)(𝒜)) ≤ C ‖δu_(Q,R)‖_(H^(k_g+2)(𝒜)) ≤ C θ_R(Q), continuously in Q. So the unscaled data
𝔵̂_Q := 𝒮_R⁻¹(u_(Q,R) + δu_(Q,R)) on Γ(R, 4R) satisfy the bound of [[eq:after-shell-annulus]] by C θ_R(Q) against
(γ_λ, k_λ); they are the sum of χ times the deviation of the data, (1 − χ) times that of the member, and δu. The
hypotheses of Step 1 hold for R large, as u_(Q,R) is within C R⁻² + C Ξ R^(−a) of flat data.

(3) *Step 4 in relative form.* [[lem:v-1-4]] and [[eq:v-1-1]] give G_R(Q)_X := R^(2+d(X)) F_R(Q)_X =
∮_(S_(4R)) 𝔟_X(𝔵̂_Q) − ∮_(S_R) 𝔟_X(𝔵̂_Q) + ∫_(Γ(R,4R)) q_X(𝔵̂_Q). Near S_(4R) the data are the member's, near S_R the
perturbation's. By the flux identity on the vacuum regions outside, ∮_(S_(4R)) 𝔟_X = Q_X + ∫_(r>4R) q_X(member) and
∮_(S_R) 𝔟_X = 𝔔_X(γ, k) + ∫_(r>R) q_X(γ, k). Subtracting the identity 0 = ∫_(r>4R) q_X − ∫_(r>R) q_X + ∫_(Γ(R,4R)) q_X
for (γ_λ, k_λ),

    G_R(Q)_X = Q_X − 𝔮̃_X(p_λ) − Δ𝔔_X + T_X(Q),

where T_X(Q) is the sum of ∫_(r>4R)[q_X(member) − q_X(γ_λ, k_λ)], −∫_(r>R)[q_X(γ, k) − q_X(γ_λ, k_λ)] and
∫_(Γ(R,4R))[q_X(𝔵̂_Q) − q_X(γ_λ, k_λ)]. By [[eq:after-shell-bilinear]], with m ≤ C r⁻² for the reference,
m(member − reference) ≤ C(|Δp₂| r⁻² + |Δp| r⁻³), m(h, κ) ≤ Ξ r^(−a) and (2) on the annulus, with d := d(X),

    |T_X(Q)| ≤ C R^d (|Δp₂| R⁻² + |Δp| R⁻³) + C Ξ (R^(d−a) + Ξ R^(d+2−2a)) + C R^d (θ_R + R² θ_R²).

By (1) and [[eq:after-shell-theta]], each term is C(1 + C_0)² Ξ times one of R^(d−2+min(0,2−a)), R^(d−3+min(0,3−a)),
R^(d−a) and R^(d+2−2a). Each of these exponents is strictly below E := min(0, 2 + d − a), for d ∈ {0, 1} and
3/2 < a ≤ ℓ0 < 4. Indeed d − a < 0 and d − a < 2 + d − a; d + 2 − 2a < 0, as 2a > 3 ≥ d + 2, and d + 2 − 2a < 2 + d − a;
d − 2 + min(0, 2 − a) ≤ d − 2 < 0 and ≤ d − a; and d − 3 + min(0, 3 − a) ≤ d − 3 < 0 and ≤ d − a. So for R ≥ R_G,
|T_X(Q)| ≤ Ξ R^E on 𝔅_R.

(4) *The charges.* By [[lem:after-shell-charges]] (b), Δ𝔔_X = 0 if a > 2 + d(X), and |Δ𝔔_X| ≤ C_1′ Ξ otherwise.

(5) *A zero by Brouwer's fixed point theorem* (in place of [[lem:v-3-3]]). Let Θ(Q) := 𝔮̃(p_λ) + Δ𝔔 − T(Q). By (3)
and (4), |Θ_X(Q) − 𝔮̃_X(p_λ)| ≤ r_X on 𝔅_R: if a ≤ 2 + d this reads C_1′ Ξ + Ξ = C_0 Ξ, and if a > 2 + d it reads
0 + Ξ R^(2+d−a). Θ is continuous, by Step 3 of the proof of [[thm:v-3-1]] and [[lem:v-3-2]], and 𝔅_R is a product of
closed intervals, so Θ has a fixed point Q_R. Then G_R(Q_R) = 0, and by Step 3 the data u_(Q_R,R) + δu_(Q_R,R) are
vacuum.

(6) *Conclusion.* Step 5 of the proof of [[thm:v-3-1]] gives the smooth vacuum data, with p_R := p(Q_R). Then
[[eq:after-shell-params]] is (1), and [[eq:after-shell-annulus]] is (2) with [[eq:after-shell-theta]]. ∎

**Remark {#rem:after-shell-box}** (Why the box does not shrink.) For a ≤ 2 + d(X) the charge difference Δ𝔔_X is
O(Ξ) and need not vanish, so the radius r_X cannot tend to 0 with R. For instance, with d = 1, pull the data of (i) back
by x ↦ x + χ_1(|x|) c for a small constant c ∈ ℝ⁴, χ_1 as in [[prop:after-shell-outside]]. This is a vacuum perturbation,
pure gauge, of order 3 = 2 + d: by [[eq:after-shell-gain]], γ^(m_λ)(x + c) − γ^(m_λ)(x) ∈ ρ³C^∞. Its centre-of-mass
charges are Δ𝔔_(e′_l) = −6π² m_λ c_l + O(|c|²): they involve the metric only, the metric on Σ differs from that on the
Kerr–Schild slice by ρ⁴C^∞ ([[lem:after-shell-mp-data]] (d) at w = 0), whose translation derivative contributes no
degree-1 flux, and the derivative of the slice charges is a22 = −6π² m_λ ([[prop:v-2-3]]). This does not depend on R, so
a box of radius tending to 0 would exclude it. The same example lies in the class: its difference from (γ_λ, k_λ) lies in
ρ³C^∞ × ρ⁴C^∞ far out, so in ℋ^∞ by [[lem:vii-0-1]].

**Corollary {#cor:after-shell-glued-norm}** (The norm of the glued data.) In [[prop:after-shell-gluing]],
(γ̂_R − γ_λ, k̂_R − k_λ) ∈ ℋ^∞ and

    ‖(γ̂_R − γ_λ, k̂_R − k_λ)‖_(d_1) ≤ C Ξ (1 + R^(ℓ0−a))   (a < ℓ0),      ≤ C Ξ (1 + log R)^(1/2)   (a = ℓ0).
                                                                                                  {#eq:after-shell-glued}

So [[thm:settling]] (ii) applies to the glued data when C Ξ (1 + R^(ℓ0−a)) < δ. For a < ℓ0, as 1 + R^(ℓ0−a) ≤
2R^(ℓ0−a) for R ≥ 1, this holds for R_G ≤ R < (δ/(2CΞ))^(1/(ℓ0−a)), a range that is nonempty when 2CΞ R_G^(ℓ0−a) < δ;
at a = ℓ0 it holds for R ≥ R_G with log R < (δ/(CΞ))² − 1. For the perturbations of [[prop:after-shell-outside]], to
which [[prop:after-shell-gluing]] applies when also C_P Ξ ≤ Ξ0, no data in the class that agree with them on {r < R} do
better than [[eq:after-shell-lower]], so for them the order of the window is attained.

*Proof.* Membership: the data are smooth, and for r ≥ 4R the difference is (g̃_(p_R) − γ^(m_λ), K̃_(p_R) − k^(m_λ)) ∈
ρ²C^∞ × ρ³C^∞ ([[lem:after-shell-mp-data]] (a)), which lies in the class by [[lem:vii-0-1]], whose proof applies at
every order. For the norm let u := γ̂_R − γ_λ and use |Au| ≤ C Σ_(|β|≤d_1) r^(|β|) |∂^β u| as in the proof of
[[prop:after-shell-above]]. The coefficients of u in [[eq:after-shell-expansion]] are those of g̃_(p_R) − γ^(m_λ)
([[lem:after-shell-expansion]]), namely a2(p_R) and a3(p_R), of size at most C|Δp_R| ≤ C Ξ ([[lem:after-shell-mp-data]]
(b), [[eq:after-shell-params]]). The remainder ũ = u − χ_c(ρ² a2 + ρ³ a3) splits by region.

- r ≤ 2r_χ: u = h, of norm at most C Ξ.
- r_χ < r < R: ũ = h − χ_c(ρ² a2 + ρ³ a3). Its norm is at most C Ξ ‖r^(ℓ0−a)‖_(L²((r_χ,R), dr/r)) +
  C |Δp₂| ‖r^(ℓ0−2)‖ + C |Δp| ‖r^(ℓ0−3)‖, so at most C Ξ R^(ℓ0−a), or C Ξ (log R)^(1/2) at a = ℓ0, by
  [[eq:after-shell-params]], since min(0, 2 − a) + ℓ0 − 2 ≤ ℓ0 − a and min(0, 3 − a) + ℓ0 − 3 ≤ ℓ0 − a.
- R ≤ r ≤ 4R: |Aũ| ≤ C Ξ R^(−a) + C |Δp₂| R⁻² + C |Δp| R⁻³ ≤ C Ξ R^(−a), by [[eq:after-shell-annulus]] (k_g − 1 > d_1)
  and [[eq:after-shell-theta]]; so the norm there is at most C Ξ R^(ℓ0−a) (log 4)^(1/2).
- r ≥ 4R: ũ = ρ⁴ ℛ0(p_R), so the norm is at most C |Δp_R| (4R)^(ℓ0−4) (2(4 − ℓ0))^(−1/2) ≤ C Ξ.

The same holds for k̂_R − k_λ, with the weight ℓ0 + 1, the order a + 1 and the exponents 3 and 4. ∎

**Remark {#rem:after-shell-bump}** (The cost of a bump.) The annulus term of [[cor:after-shell-glued-norm]] at a = 3 is the
cost of a bump of relative size R⁻¹ at radius R, read against the deviation of Tangherlini's data there (μ r⁻² in the
metric, r⁻³ in the second fundamental form): f_R := R⁻³ ϕ(r/R) and k_R := R⁻⁴ ϕ(r/R), ϕ ∈ C_c^∞((0, ∞)). With r = Rs,

    ‖r^(ℓ0) f_R‖²_(L²(dr/r dω)) = 2π² R^(2ℓ0−6) ∫_0^∞ s^(2ℓ0) ϕ(s)² ds/s,

and the weight r^(ℓ0+1) on k_R gives the same power of R. As (r∂_r)^j (ϕ(r/R)) = ((s∂_s)^j ϕ)(r/R), every b-derivative
scales alike, so the bump has norm of order R^(ℓ0−3) in the class, which grows with R. This is the bound mentioned in
[[rem:s28-mass-bound]]. [[prop:after-shell-outside]] supplies the matching lower bound, valid for every data set in the
class that agrees with the examples, and not only for the glued one.

#### The reach of the settling theorem {#sec:after-shell-theorem}

**Theorem {#thm:after-shell-reach}** (Which perturbations [[thm:settling]] (ii) reaches.) Fix ℓ0 ∈ (3, 4), d_1, λ ≤ λ1,
the data of (i) and δ as in [[thm:settling]], and let a > 3/2.

(i) If a > ℓ0, every perturbation of order a and size Ξ < δ/(C_1(1 + (a − ℓ0)^(−1/2))) lies in the class with
‖·‖_(d_1) < δ. So [[thm:settling]] (ii) applies to it directly, and (S) and (S_∞) hold with the perturbation itself as
the data on every ball. Over the admissible ℓ0 of [[thm:settling]], this covers every a > 3
([[cor:after-shell-every-rate]]).

(ii) If 3/2 < a ≤ ℓ0, the decay rate does not decide. (S_∞) holds for a perturbation exactly when it lies in the class
with ‖·‖_(d_1) < δ, and (S) only if it lies in the class at regularity d_1 ([[cor:after-shell-membership]]). At every
such a and every Ξ ∈ (0, Ξ1], some perturbation of order a and size C_P Ξ fails (S): every data set in the class that
agrees with it on {r < R} has norm at least c_P Ξ R^(ℓ0−a), or c_P Ξ (log₂(R/R_P))^(1/2) at a = ℓ0
([[prop:after-shell-outside]]). The gluing of [[prop:after-shell-gluing]] does no worse than this order for every
perturbation of order a ([[cor:after-shell-glued-norm]]), and attains it for these examples.

So the statement "[[thm:settling]] (ii) applies up to the gluing" is false for fixed Ξ and large R at every
a ∈ (3/2, ℓ0]; its form uniform in R is equivalent to (ii) applied directly; and the perturbations to which
[[thm:settling]] (ii) applies, directly or through gluing uniformly in R, are exactly those small in Hintz's class.

*Proof.* (i) is [[prop:after-shell-above]] with [[cor:after-shell-every-rate]], and (ii) is [[cor:after-shell-membership]]
with [[prop:after-shell-outside]], [[prop:after-shell-gluing]] and [[cor:after-shell-glued-norm]]. ∎

That the rate does not decide below the threshold is seen from both sides. Perturbations of order a ≤ ℓ0 can lie in
the class: the translation pull-back of [[rem:after-shell-box]] has order 3 and lies in it, and the glued data of
[[cor:after-shell-glued-norm]] have order 2 and lie in it. Others of the same orders lie outside it
([[prop:after-shell-outside]]). Settling itself is not confined to the class, since the examples of
[[prop:after-shell-outside]] have developments isometric to that of (i) ([[rem:after-shell-pure-gauge]]). The
development of glued data is not the perturbation's: the two data sets differ on {r > R}, and the late-time solution
near the hole depends on them.
