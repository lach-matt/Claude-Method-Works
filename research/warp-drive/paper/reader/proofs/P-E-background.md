### The background below R_* {#sec:bg-below}

This section proves the properties of the background of the angle-localised families that the margins of the bent slice
and of the seed region use below R_*: the data on 𝒩′ and the mass μ3 of region III ([[prop:bg-nprime]]); that the
background's ψ_III lies in the tube of [[prop:margins-seed]] (b) around the explicit quintic ψ_s
([[prop:bg-seed]]); and the hyperbolicity margin κK^l_l on Σ_τ0 for 0.68 ≤ R ≤ R_* ([[prop:bg-slice]]). The results
are collected in [[thm:bg-margins]]. Below R_* the background reduces exactly to ordinary differential equations along
null rays ([[lem:bg-reduction]]). Their solutions are enclosed by explicit approximants with a posteriori bounds
([[prop:bg-nprime]], [[prop:bg-rays]]). The approximants and every row of the bounds are printed in [[sec:tab-bg]].

#### The data and the reduction {#sec:bg-data}

Put u1 := 5.7, u2 := 7.2 and τ0 := −0.68. With the bump β(w) = exp(1 − 1/(1 − w²)) for |w| < 1, β(w) = 0 otherwise,
and b(x; a, c) = β((2x − a − c)/(c − a)), both as in [[sec:table-bump]], put

    B(u) := 1.7 b(u; 5.7, 7.2),        α(v) := 3.6 b(v; 3, 4.5).                                       {#eq:bg-profiles}

The background is the spherically symmetric metric g0 = −2e^(2s) du dv + R² dΩ₃² of [[pending:sec-two-dust-background]]
with an outgoing null dust of profile B(u) and an ingoing one of profile α(v), so that ([[ch:two-dusts]])

    R_uu − 2s_u R_u = −B/(3R²),     R_vv − 2s_v R_v = −α/(3R²),     R R_uv = −e^(2s) − 2R_u R_v,       {#eq:bg-field}

with the characteristic data e^(2s) = 1/2 on 𝒩 = {u = 0} and on 𝒩′ = {v = 0}, and R = 5, R_u = −0.47, R_v = 1/2 at
the corner. The mass function is μ := R²(1 + 2e^(−2s) R_u R_v), and f := 1 − μ/R² = −2e^(−2s) R_u R_v. Let v̂(v) be
the ingoing coordinate with v̂(0) = 0 and ψ = 0 on 𝒩, where

    ψ := ln(−e^(2s)/(R_u v̂′(v))),      g0 = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃²   where R_u ≠ 0,     {#eq:bg-chart}

the second identity following from du = (dR − R_v dv)/R_u. The slice is Σ_τ0 := {v̂ − R = τ0}. Put

    F(R) := 2R + √(3/2) ln((R − √(3/2))/(R + √(3/2))),      F′(R) = 2/(1 − 3/(2R²)),  {#eq:bg-tangherlini}

the null function of Tangherlini's metric of mass 3/2, and for ρ > √(3/2)

    v̂(ρ) := F(ρ) − F(2.321),    f1(ρ) := 1 − 3/(2ρ²),    a(ρ) := f1(ρ)/2,    a′(ρ) = 3/(2ρ³).           {#eq:bg-label}

**Lemma {#lem:bg-identities}** (Identities.) A solution of [[eq:bg-field]] satisfies

    μ_u = −(2/3) B e^(−2s) R_v,    μ_v = −(2/3) α e^(−2s) R_u,    ψ_u = B/(3R² R_u),
    (e^(−2s) R_v)_v = −α e^(−2s)/(3R²),    (e^(−2s) R_u)_u = −B e^(−2s)/(3R²).

Proof. Differentiating, μ_u = 2RR_u + 4Re^(−2s)R_u²R_v + 2R²e^(−2s)R_v(R_uu − 2s_uR_u) + 2R²e^(−2s)R_uR_uv. By the
third equation of [[eq:bg-field]] the last term is −2RR_u − 4Re^(−2s)R_u²R_v, and by the first the third term is
−(2/3)Be^(−2s)R_v. The identity for μ_v follows in the same way with u and v exchanged. The two others are e^(−2s)
times the first two equations of [[eq:bg-field]], and ψ_u = 2s_u − R_uu/R_u = B/(3R²R_u) by the first. ∎

**Lemma {#lem:bg-reduction}** (Reduction to rays.) Let ℛ := {v < 3}.

(a) *The data on 𝒩′.* R(u) := R(u, 0) solves R″ = −B/(3R²) with R(u1) = 2.321, R′(u1) = −0.47, and S(u) := R²R_v(u,
0) solves S′ = −R/2 with S(u1) = 2.067575. The functions μ(u) := μ(u, 0) and λ(u) := 2R_v(u, 0) are

    μ = R² + 4R′S,     λ = 2S/R²,     μ′ = −(2/3) B λ,     λ′ = −μ/R³.                                   {#eq:bg-nprime}

(b) *Region I.* On {u ≤ u1} ∩ ℛ, μ = 3/2 and ψ = 0, so g0 is Tangherlini's metric of mass 3/2 in ingoing
coordinates; along the outgoing ray u = u1, v̂ = F(R) − F(2.321). The ingoing ray of label v̂ meets u = u1 at R = ρ,
where v̂ = v̂(ρ) in the notation [[eq:bg-label]]; we label rays by ρ.

(c) *The rays.* On ℛ, μ(u, v) = μ(u) and e^(−2s)R_v(u, v) = λ(u), and R_u < 0. Where λ(u) > 0, along every ingoing ray

    R_u = G(u, R),        G(u, X) := −(1 − μ(u)/X²)/(2λ(u)).                                              {#eq:bg-ray}

Write Ψ(u, ρ) for the solution of [[eq:bg-ray]] with Ψ(u1, ρ) = ρ, and J := ∂_ρΨ, K := ∂_ρ²Ψ, L := ∂_ρ³Ψ.

(d) *The packet.* At a point of ℛ with u1 ≤ u ≤ u2 and f > 0, on the ray ρ, in the chart [[eq:bg-chart]],

    E := e^ψ = 2aJ/f,    ψ_R = B/(3R²G²),    f_R = 2μ/R³ − μ′/(R²G),    f_v̂ = μ′ J a/(R²G),
    ψ_v̂ = aK/J + a′ − 2μJa/(R³f) − (Ja/G) B/(3R²G),                                                    {#eq:bg-inputs}

with R = Ψ(u, ρ), G = G(u, R), a = a(ρ), μ = μ(u), μ′ = μ′(u), B = B(u).

(e) *Region III.* On {u ≥ u2} ∩ ℛ, μ = μ3 := μ(u2) and ψ = ψ_III(v̂), where for the ray ρ, with Φ(ρ) := Ψ(u2, ρ)
and f3(X) := 1 − μ3/X²,

    ψ_III(v̂(ρ)) = ln Φ′(ρ) + ln f1(ρ) − ln f3(Φ(ρ)),  {#eq:bg-psi3-def}

provided f3(Φ(ρ)) > 0. There g0 = −e^(2ψ_III) f3 dv̂² + 2e^(ψ_III) dv̂ dR + R² dΩ₃².

(f) *The slice.* Every point of Σ_τ0 with 0.68 ≤ R ≤ R_*, R_* as in [[lem:bg-rstar]], lies in ℛ, on the ray ρ with
v̂(ρ) − R = τ0 and 2.321 ≤ ρ ≤ R_*.

Proof. (a) On 𝒩′, s is constant, so [[eq:bg-field]] gives R″ = −B/(3R²) and R R_uv = −1/2 − 2R′R_v; hence S′ = 2RR′R_v
+ R²R_uv = −R/2. Since B = 0 on [0, u1], R = 5 − 0.47u there, so R(u1) = 2.321, and S(u1) = 25/2 − (1/2)∫_0^(u1) (5 −
0.47u) du = 2.067575. With e^(−2s) = 2, μ = R²(1 + 4R′R_v) = R² + 4R′S and λ = 2S/R². Then μ′ = −(2/3)Bλ by
[[lem:bg-identities]], and λ′ = 2R_uv = −(1 + 4R′R_v)/R = −μ/R³.

(b) On {u ≤ u1}, B = 0, and on ℛ, α = 0. By [[lem:bg-identities]] μ_u = μ_v = 0, so μ equals its corner value
25(1 − 0.94) = 3/2, and ψ_u = 0, so ψ = 0 as on 𝒩. In [[eq:bg-chart]] the outgoing null directions satisfy dv̂/dR =
2/f = F′(R); the ray u = u1 meets 𝒩′ at v̂ = 0, R = 5 − 0.47 u1 = 2.321.

(c) On ℛ, α = 0, so [[lem:bg-identities]] gives μ_v = 0 and (e^(−2s)R_v)_v = 0; hence μ and e^(−2s)R_v take their
values on 𝒩′. On 𝒩, R_u = (3/(2R²) − 1)/2 < 0 for v ≤ 3 (there μ = 3/2, R = 5 + v/2, e^(−2s) = 2), and
(e^(−2s)R_u)_u ≤ 0, so R_u < 0 on ℛ. Finally f = −2e^(−2s)R_uR_v = −2λR_u.

(d) On ℛ, e^(2s) = R_v/λ and λR_u = −f/2, so e^ψ = −R_v/(λR_u v̂′) = (2/f) ∂_v̂R|_u, and ∂_v̂R|_u = J dρ/dv̂ = Ja.
The derivatives in the chart [[eq:bg-chart]] follow from ∂_R|_v̂ = G⁻¹∂_u and ∂_v̂|_R = ∂_v̂|_u − (Ja/G)∂_u: f_R =
2μ/R³ − μ′/(R²G), f_v̂ = μ′Ja/(R²G), ψ_R = ψ_u/G = B/(3R²G²) by [[lem:bg-identities]], and ψ_v̂ = ∂_v̂ ln(2Ja/f)|_u −
(Ja/G)ψ_u, where ∂_v̂ J|_u = Ka, ∂_v̂ a = aa′ and ∂_v̂ f|_u = 2μJa/R³.

(e) On {u ≥ u2}, B = 0, so μ_u = ψ_u = 0 ([[lem:bg-identities]]; R_u ≠ 0 by (c)): μ and ψ take their values on u =
u2. There (d) gives e^ψ = 2aΦ′/f3(Φ) = f1Φ′/f3(Φ).

(f) On Σ_τ0, v̂ = R + τ0 ≤ R_* − 0.68 < 2.7572, while v̂(3) = F(6.5) − F(5) > 3.1453 (on 𝒩 before the shell R = 5 +
v/2 and dv̂/dR = F′(R)); v̂ is increasing in v, so the point lies in ℛ. Its ray meets u = u1 at the ρ with v̂(ρ) = v̂ ≤
R_* − 0.68, so ρ ≤ R_* by the definition of R_*; and v̂ ≥ 0 gives ρ ≥ 2.321. ∎

**Lemma {#lem:bg-rstar}** (The radius R_*.) Let R_* be the radius at which the ray u = u1 meets Σ_τ0, that is the
zero of τ(R) := F(R) − F(2.321) − R + 0.68 on R > 2.321. Then R_* is unique and 3.43718006 ≤ R_* ≤ 3.43718007.

Proof. τ′(R) = 2/f1(R) − 1 > 0, τ(3.43718006) ≤ −8.4 × 10⁻⁹ and τ(3.43718007) ≥ 4.4 × 10⁻⁹, by direct evaluation of
[[eq:bg-tangherlini]] at these two decimals. ∎

**Lemma {#lem:bg-slice-forms}** (The margin on Σ_τ0.) At a point of Σ_τ0 in ℛ, in the chart [[eq:bg-chart]] with E :=
e^ψ > 0 and Ef < 2 (f of either sign), the radial extrinsic curvature κ and the sphere trace K^l_l of
[[pending:lem-racz-split-formulas]] satisfy

    κ K^l_l = 3 N_κ (1 − Ef)/(E R (2 − Ef)²),
    N_κ := E²f²ψ_R + E²f f_R/2 − 3Efψ_R − Ef_v̂/2 − 3Ef_R/2 − ψ_v̂ + ψ_R,                                 {#eq:bg-kk}

and κ > 0, K^l_l < 0 exactly when N_κ < 0 and Ef < 1. In the packet (u1 ≤ u ≤ u2, f > 0, inputs [[eq:bg-inputs]]),

    N_κ = −(μE/R³)(2 − Ef) − aK/J − a′ + B λ² (2 − Ef)²/(3R²f²),        E f = 2aJ,  {#eq:bg-nk-packet}

and in region III, N_κ = (μ3E/R³)(Ef − 3) − ψ_III′(v̂).

Proof. Since E > 0 and Ef < 2, 2/E − f = (2 − Ef)/E > 0. By [[pending:lem-racz-split-formulas]],
κ = −N_κ/(E√(2/E − f)(2 − Ef)) and K^l_l = 3(Ef − 1)/(ER√(2/E − f)), and E²(2/E − f) = E(2 − Ef); this gives the
product, and since E, R, √(2/E − f) and 2 − Ef are positive, κ > 0 exactly when N_κ < 0 and K^l_l < 0 exactly when
Ef < 1. In the packet substitute [[eq:bg-inputs]] with Ef = 2aJ and μ′ = −(2/3)Bλ: the terms without B give
(μE/R³)(Ef − 3) − (aK/J + a′ − μE/R³), using 2μJa/(R³f) = μE/R³; the terms in B are B times
(4λ²/(3R²f²))[(Ef)² − (5/2)Ef + 1 − Ef((3/4)Ef − 3/2)] = Bλ²(2 − Ef)²/(3R²f²). In region III, ψ_R = f_v̂ = 0 and
f_R = 2μ3/R³. ∎

#### Elementary bounds {#sec:bg-tools}

**Lemma {#lem:bg-tools}** (Elementary bounds.)

(a) *Chebyshev sums.* If p(x, y) = Σ c_(ij) T_i(x)T_j(y) is a polynomial, T_i the Chebyshev polynomials, then on
[−1, 1]² it lies in [c_00 − σ′, c_00 + σ′], σ′ := Σ_((i,j)≠(0,0)) |c_(ij)|; in particular |p| ≤ Σ |c_(ij)|. On a box
[a, b] × [c, d] the same holds for the coefficients in the variables x = (u − (a + b)/2)/((b − a)/2), y likewise; a
polynomial written in powers of x has Chebyshev coefficients given by x^n = 2^(1−n) Σ′_(k ≤ n/2) C(n, k) T_(n−2k)(x),
the prime halving the term T_0.

(b) *Cauchy.* If g is holomorphic on a neighbourhood of {|z − c| ≤ r}, |g| ≤ M there, and g_n are its Taylor
coefficients at c, then for real x with |x − c| ≤ h < r and every N, |g(x)| ≤ Σ_(n<N) |g_n|hⁿ + M(h/r)^N/(1 − h/r).

(c) *Taylor.* If g ∈ C^(N+1)[c − h, c + h], then |g(x)| ≤ Σ_(n≤N) |g^(n)(c)|hⁿ/n! + h^(N+1) sup |g^(N+1)|/(N + 1)!.

(d) *Enclosures.* If x ∈ X and y ∈ Y for closed intervals X, Y, then x + y, x − y, xy and (if 0 ∉ Y) x/y lie in the
intervals spanned by the corresponding combinations of the endpoints, and φ(x) ∈ φ(X) for φ = exp, ln, √ (monotone).
Replacing each operation of an explicit expression by this rule encloses the expression's range on a box.

(e) *The bump.* β is increasing on (−1, 0] and decreasing on [0, 1). For real w0 and complex w with |w − w0| ≤ ϱ <
1 − |w0|,

    |β(w)| ≤ exp(1 − (1/2)(1/(1 − w0 + ϱ) + 1/(1 + w0 + ϱ))),  {#eq:bg-bump-disc}

and β(w0 + t) = exp(Σ_n g_n tⁿ) with g_0 = 1 − 1/(1 − w0²) and g_n = −(1/2)((1 − w0)^(−n−1) + (−1)ⁿ(1 + w0)^(−n−1))
for n ≥ 1; its Taylor coefficients are e_0 = e^(g_0), n e_n = Σ_(k=1)^n k g_k e_(n−k).

(f) *Power series.* Let p = Σ p_n tⁿ and q = Σ q_n tⁿ be the Taylor series at a point of two smooth functions. The
Taylor coefficients there of p + q, pq, r := p/q (q_0 ≠ 0), e := exp p, ℓ := ln p (p_0 > 0) and the derivative p′ are
p_n + q_n, Σ_(k≤n) p_k q_(n−k), and, with e_0 = exp p_0 and ℓ_0 = ln p_0,

    q_0 r_n = p_n − Σ_(k=1)^n q_k r_(n−k),     (p′)_n = (n + 1) p_(n+1),
    n e_n = Σ_(k=1)^n k p_k e_(n−k),     n p_0 ℓ_n = n p_n − Σ_(k=1)^(n−1) k ℓ_k p_(n−k)   (n ≥ 1).  {#eq:bg-series}

Proof. (a) |T_i| ≤ 1 on [−1, 1], and the expansion of xⁿ is the binomial expansion of ((e^(iθ) + e^(−iθ))/2)ⁿ. (b)
Cauchy's estimate |g_n| ≤ M/rⁿ bounds the terms n ≥ N. (c) Taylor's formula with Lagrange's remainder. (d) is
elementary. (e) 1/(1 − w²) = (1/2)(1/(1 − w) + 1/(1 + w)). The disc 1 − w ∈ {|ζ − (1 − w0)| ≤ ϱ} does not contain 0,
and ζ ↦ 1/ζ maps it onto the disc with real diameter [1/(1 − w0 + ϱ), 1/(1 − w0 − ϱ)], so Re 1/(1 − w) ≥ 1/(1 − w0 +
ϱ); likewise for 1 + w; and |e^(1−Z)| = e^(1−Re Z). The series of ln β = 1 − 1/(1 − w²) follows from the two
geometric series, and n e_n = Σ k g_k e_(n−k) from (exp g)′ = g′ exp g. (f) Compare the coefficients of tⁿ in
rq = p, and of tⁿ⁻¹ in e′ = p′e and in pℓ′ = p′. ∎

**Lemma {#lem:bg-comparison}** (Comparison.)

(a) If e ∈ C²[a, b], |e″| ≤ Λ|e| + δ with Λ > 0, δ ≥ 0, |e(a)| ≤ E₀ and |e′(a)| ≤ E₁, then with k := √Λ and t := u −
a,

    |e(u)| ≤ E₀ cosh kt + E₁ (sinh kt)/k + δ (cosh kt − 1)/Λ,
    |e′(u)| ≤ E₀ k sinh kt + E₁ cosh kt + δ (sinh kt)/k.  {#eq:bg-comparison-2}

(b) If e is absolutely continuous on [a, b] and e′ = −p e + r with p ≥ 0 continuous and r integrable, then |e(u)| ≤
|e(a)| + ∫_a^u |r|.

Proof. (a) By Taylor's formula, m(t) := |e(a)| + |e′(a)| t + ∫_0^t (t − σ)(Λ|e(a + σ)| + δ) dσ satisfies |e(a + t)| ≤
m(t), m″ = Λ|e| + δ ≤ Λm + δ, m(0) ≤ E₀, m′(0) ≤ E₁. The right side of the first line of [[eq:bg-comparison-2]], call it
𝓔(t), solves 𝓔″ = Λ𝓔 + δ with 𝓔(0) = E₀, 𝓔′(0) = E₁. Then z := 𝓔 − m has z″ − Λz = q ≥ 0 and z(0), z′(0) ≥ 0, so z(t)
= z(0) cosh kt + z′(0)(sinh kt)/k + ∫_0^t (sinh k(t − σ)/k) q(σ) dσ ≥ 0. Then |e′(a + t)| ≤ E₁ + ∫_0^t (Λ𝓔 + δ) =
𝓔′(t). (b) e(u) = e^(−P(u)) e(a) + ∫_a^u e^(P(σ)−P(u)) r(σ) dσ with P(u) := ∫_a^u p, and P is nondecreasing. ∎

#### The data on 𝒩′ {#sec:bg-nprime}

The approximant R̂ is the piecewise polynomial of [[sec:tab-bg-nprime]] on twelve segments of [u1, u2]: affine on
[5.7, 5.73] (the data line) and on [7.17, 7.2], and a polynomial of degree 12 to 17 on each of the ten middle segments,
which are graded towards the ends of the packet. Put

    Ŝ(u) := 2.067575 − (1/2)∫_(u1)^u R̂,     μ̃ := R̂² + 4R̂′Ŝ,     λ̃ := 2Ŝ/R̂²,  {#eq:bg-nprime-approx}

so that Ŝ and μ̃ are polynomials and λ̃ is a rational function on each segment, and μ̃3 := R̂(u2)² + 4R̂′(u2)Ŝ(u2) =
0.82211255682735… (an explicit rational).

**Proposition {#prop:bg-nprime}** (The data on 𝒩′.) On each segment [a, b] of [[sec:tab-bg-nprime-chain]], |R − R̂| ≤ E₀
and |R′ − R̂′| ≤ E₁ with E₀, E₁ of that row, and |S − Ŝ| ≤ I/2. In particular |R − R̂| ≤ 4.53 × 10⁻⁸, |R′ − R̂′| ≤ 9.20
× 10⁻⁸ and |S − Ŝ| ≤ 1.82 × 10⁻⁸ on [u1, u2], and

(i) R(u2) ∈ [1.5193579, 1.5193581] ⊂ [1.519357, 1.519359];

(ii) |μ3 − μ̃3| ≤ 4.07 × 10⁻⁷, so μ3 ∈ [0.82211214, 0.82211297] ⊂ [0.8220998, 0.8221253], and R(u2)² > μ3;

(iii) μ is nonincreasing, 3/2 ≥ μ ≥ μ3, and λ is decreasing with λ ≥ λ(u2) ≥ 0.529533 > 0.529 on [u1, u2];

(iv) at every u ∈ [u1, u2], with E₀, E₁, I of a segment containing u and R̂, R̂′, Ŝ at u,

    |μ − μ̃| ≤ (2R̂ + E₀)E₀ + 4(|R̂′| I/2 + ŜE₁ + E₁I/2),      |λ − λ̃| ≤ (I + 2Ŝ(2R̂ + E₀)E₀/R̂²)/(R̂ − E₀)²;

in particular |μ − μ̃| ≤ 4.2 × 10⁻⁷ and |λ − λ̃| ≤ 5 × 10⁻⁸ on [u1, u2].

Proof. Let δ(u) := R̂″ + B/(3R̂²) on a segment. On the ten middle segments δ is holomorphic on the disc |u − c| ≤ r, r =
(4/5)min(c − u1, u2 − c), since B is holomorphic off u1 and u2 ([[lem:bg-tools]] (e)) and |R̂| > 0 there; on the
disc, |R̂″| ≤ Σ n(n − 1)|q_n|(r/h)^(n−2)/h², |R̂| ≥ q_0 − Σ_(n≥1)|q_n|(r/h)ⁿ and |B| is bounded by [[eq:bg-bump-disc]]
with w0 = (c − 6.45)/0.75, ϱ = r/0.75. This gives M. The Taylor coefficients δ_n of δ at c follow from those of B
([[lem:bg-tools]] (e)) by multiplication and division of power series, and [[lem:bg-tools]] (b) with N = 60 gives the
bound δ of [[sec:tab-bg-nprime-defects]]. On the outer segments R̂″ = 0 and |δ| = B/(3R̂²) ≤ B_max/(3R̂_min²), B being
monotone there.

The error e := R − R̂ satisfies e″ = −(B/3)(1/R² − 1/R̂²) − δ, and |1/R² − 1/R̂²| = |e|(R + R̂)/(R²R̂²). While |e| ≤
10⁻⁶ this gives |e″| ≤ Λ|e| + δ with the Λ of [[sec:tab-bg-nprime-chain]]. On the first segment e(u1) = e′(u1) = 0;
on each later one the initial bounds are the previous segment's E₀, E₁ plus the jumps j₀, j₁ of R̂ and R̂′ (exact
differences of the two polynomials at the common end). [[lem:bg-comparison]] (a) gives E₀, E₁ row by row; since
[[eq:bg-comparison-2]] is increasing in t they bound |e|, |e′| on the whole segment. They stay below 4.53 × 10⁻⁸ <
10⁻⁶, so by continuity the hypothesis |e| ≤ 10⁻⁶ holds on every segment. Then S − Ŝ = −(1/2)∫_(u1)^u e by
[[lem:bg-reduction]] (a), and I accumulates the segment lengths times E₀.

Since R̂ ≥ R̂_min > 1.5 on every segment ([[sec:tab-bg-nprime-chain]]), Ŝ′ = −R̂/2 < 0, so Ŝ decreases from 2.067575
to Ŝ(u2) = 0.61120057465952… ([[sec:tab-bg-nprime]]) and is positive on [u1, u2]; and R ≥ R̂ − E₀ > 1.5. The column
I does not decrease down the rows, so |S − Ŝ| ≤ I/2 ≤ (3.63 × 10⁻⁸)/2 < 1.82 × 10⁻⁸ on [u1, u2], by the last row.

(iv) At u, μ − μ̃ = (R² − R̂²) + 4(R̂′(S − Ŝ) + (R′ − R̂′)Ŝ + (R′ − R̂′)(S − Ŝ)) and λ − λ̃ = 2(S − Ŝ)/R² + 2Ŝ(R̂² −
R²)/(R²R̂²), where |R² − R̂²| = |e|(R + R̂) ≤ (2R̂ + E₀)E₀, |S − Ŝ| ≤ I/2, Ŝ > 0 and R ≥ R̂ − E₀ > 0; this gives the two
bounds. On each segment they are at most 4.17 × 10⁻⁷ and 4.89 × 10⁻⁸ when R̂ is replaced by R̂_max in the numerators
and by R̂_min in the denominators, |R̂′| by R̂′_max of [[sec:tab-bg-ray-chain]] and Ŝ by its value at the left end;
both largest values occur on [7.17, 7.2].

(i) R̂(u2) = 1.5193579823987569 exactly. (ii) The bound (iv) at u = u2, with the exact values R̂(u2), R̂′(u2) =
−0.60795759341336… and Ŝ(u2) and the last row's E₀, E₁, I, gives |μ3 − μ̃3| ≤ 4.068 × 10⁻⁷; and R(u2)² ≥ 2.308 > 0.823.

(iii) Since Ŝ ≥ Ŝ(u2) and |S − Ŝ| ≤ 1.82 × 10⁻⁸, S ≥ Ŝ(u2) − 1.82 × 10⁻⁸ > 0.6111 on [u1, u2], so λ = 2S/R² > 0 there.
Since B ≥ 0, [[eq:bg-nprime]] gives μ′ = −(2/3)Bλ ≤ 0, so μ is nonincreasing and 3/2 = μ(u1) ≥ μ ≥ μ3 > 0 by (ii), where
μ(u1) = 2.321² − 4(0.47)(2.067575) = 3/2. Hence λ′ = −μ/R³ < 0, so λ is decreasing on [u1, u2] and λ ≥ λ(u2) =
2S(u2)/R(u2)² ≥ 2(Ŝ(u2) − I/2)/(R̂(u2) + E₀)² ≥ 0.529533. ∎

#### The rays {#sec:bg-rays}

The ray approximant Ψ̃ is the polynomial of [[sec:tab-bg-ray]] on [u1, u2] × [2.32, 3.44], of degree 24 in u and 12 in
ρ; put J̃ := ∂_ρΨ̃, K̃ := ∂_ρ²Ψ̃, L̃ := ∂_ρ³Ψ̃. On each segment of R̂ let

    G̃(u, X) := R̂²(μ̃ − X²)/(4ŜX²),     D := ∂_uΨ̃ − G̃(u, Ψ̃),     D_m := ∂_ρ^m D  (m ≤ 3),  {#eq:bg-ray-approx}

so that G̃ is [[eq:bg-ray]] with μ, λ replaced by μ̃, λ̃, and D_1, D_2, D_3 are the defects of J̃, K̃, L̃ in the
variational equations of [[eq:bg-ray]] (for G̃). The polynomial

    P := 4ŜΨ̃² ∂_uΨ̃ − R̂²(μ̃ − Ψ̃²) = 4ŜΨ̃² D  {#eq:bg-ray-numerator}

has Chebyshev sums σ_m of ∂_ρ^m P on each box [a, b] × [2.32, 3.44]. Since Ŝ does not depend on ρ, D = (P/(4Ŝ)) Ψ̃^(−2)
and Leibniz's rule give

    |D_m| ≤ Σ_(j≤m) C(m, j) (σ_(m−j)/(4Ŝ_min)) g_j,    g_0 = Ψ̃_min^(−2),  g_1 = 2J̄Ψ̃_min^(−3),
    g_2 = 6J̄²Ψ̃_min^(−4) + 2K̄Ψ̃_min^(−3),
    g_3 = 24J̄³Ψ̃_min^(−5) + 18J̄K̄Ψ̃_min^(−4) + 2L̄Ψ̃_min^(−3),  {#eq:bg-ray-defects}

J̄, K̄, L̄ the bounds of |J̃|, |K̃|, |L̃| on the box ([[sec:tab-bg-ray-defects]]).

The fields G and G̃ differ through the data. Write G = Q/(2X²) − V/2 with Q := μ/λ = R⁴/(2S) + 2R′R² and V := 1/λ =
R²/(2S), and Q̃, Ṽ likewise from R̂, Ŝ. On a segment, with R̄ := R̂_max + E₀, R̄′ := R̂′_max + E₁ (R̂′_max ≥ |R̂′|
is the bound of [[sec:tab-bg-ray-chain]]), S̲ := Ŝ_min − I/2 and X̲ := Ψ̃_min − 10⁻⁵, the mean value theorem in (R,
R′, S) gives |Q − Q̃| ≤ Δ₁, |V − Ṽ| ≤ Δ₂ with

    Δ₁ := (2R̄³/S̲ + 4R̄′R̄) E₀ + 2R̄² E₁ + (R̄⁴/(2S̲²)) I/2,      Δ₂ := (R̄/S̲) E₀ + (R̄²/(2S̲²)) I/2,
    γ_0 := Δ₁/(2X̲²) + Δ₂/2,   γ_1 := Δ₁/X̲³,   γ_2 := 3Δ₁/X̲⁴,   γ_3 := 12Δ₁/X̲⁵,  {#eq:bg-gamma}

and |∂_X^m(G − G̃)| ≤ γ_m (m ≤ 3) on the tube

    {(u, X): |X − Ψ̃(u, ρ)| ≤ 10⁻⁵ for some ρ ∈ [2.32, 3.44]},                                             {#eq:bg-tube}

where also |∂_X^m G| ≤ H_m := c_m (3/2)/(0.529533 X̲^(m+2)), (c_2, c_3, c_4) = (3, 12, 60), by
[[prop:bg-nprime]] (iii) and ∂_X^m G = (−1)^m (m + 1)! μ/(2λX^(m+2)) for m ≥ 1.

**Proposition {#prop:bg-rays}** (The rays.) For u ∈ [a, b], a segment of [[sec:tab-bg-ray-chain]], and ρ ∈ [2.32, 3.44],

    |Ψ − Ψ̃| ≤ ε₀,   |J − J̃| ≤ ε₁,   |K − K̃| ≤ ε₂,   |L − L̃| ≤ ε₃,

with the ε of that row. At u = u2: ε₀ = 8.69 × 10⁻⁷, ε₁ = 1.68 × 10⁻⁶, ε₂ = 6.10 × 10⁻⁶, ε₃ = 3.65 × 10⁻⁵. Moreover 0
< J ≤ 1, and the rays satisfy Ψ(u, ρ) > √μ(u) on [u1, u2] × [2.32, 3.44].

Proof. Fix ρ. By [[prop:bg-nprime]] (iii), λ > 0 on [u1, u2], so [[eq:bg-ray]] holds along the ray, and ∂_XG = −μ/(λX³)
< 0 for X > 0. Let e₀ := Ψ − Ψ̃. Then e₀′ = −p e₀ + r with p := −∫_0^1 ∂_XG(u, Ψ̃ + θe₀) dθ ≥ 0 and r := (G −
G̃)(u, Ψ̃) − D. While |e₀| ≤ 10⁻⁵, [[lem:bg-comparison]] (b) gives |e₀(u)| ≤ |e₀(a)| + (u − a)(γ_0 + D₀). For e₁ := J
− J̃, differentiating [[eq:bg-ray]] in ρ, e₁′ = ∂_XG(u, Ψ)e₁ + (∂_XG(u, Ψ) − ∂_XG(u, Ψ̃))J̃ + (∂_XG − ∂_XG̃)(u, Ψ̃)J̃ −
D_1, whose last three terms are at most H_2ε₀J̄ + γ_1J̄ + D₁; the same lemma applies with p = −∂_XG(u, Ψ) ≥ 0. For
e₂ and e₃ the variational equations K′ = ∂_XG K + ∂_X²G J² and L′ = ∂_XG L + 3∂_X²G JK + ∂_X³G J³ give in the same
way

    ε₀(b) = ε₀(a) + (b − a)(γ_0 + D₀),
    ε₁(b) = ε₁(a) + (b − a)(H_2ε₀J̄ + γ_1J̄ + D₁),
    ε₂(b) = ε₂(a) + (b − a)((H_2ε₀ + γ_1)K̄ + H_2ε₁(2J̄ + ε₁) + (H_3ε₀ + γ_2)J̄² + D₂),
    ε₃(b) = ε₃(a) + (b − a)((H_2ε₀ + γ_1)L̄ + 3(H_2(ε₁K̄ + J̄ε₂ + ε₁ε₂) + (H_3ε₀ + γ_2)J̄K̄)
                   + H_3ε₁(3J̄² + 3J̄ε₁ + ε₁²) + (H_4ε₀ + γ_3)J̄³ + D₃),  {#eq:bg-ray-chain}

the ε on the right without argument being those at b, taken in the order m = 0, 1, 2, 3. The bounds |J² − J̃²| ≤
ε₁(2J̄ + ε₁), |JK − J̃K̃| ≤ ε₁K̄ + J̄ε₂ + ε₁ε₂ and |J³ − J̃³| ≤ ε₁(3J̄² + 3J̄ε₁ + ε₁²) enter here. The initial values
at u1 are the sums of [[sec:tab-bg-ray-chain]] ([[lem:bg-tools]] (a)), the defects are bounded by [[eq:bg-ray-defects]]
and the rows of [[sec:tab-bg-ray-defects]], the γ_m by [[eq:bg-gamma]] and the H_m by the bound after [[eq:bg-tube]].
Since ε₀ ≤ 8.69 × 10⁻⁷ < 10⁻⁵ everywhere,
the hypothesis |e₀| ≤ 10⁻⁵ holds throughout by continuity.

J = exp(∫_(u1)^u ∂_XG(σ, Ψ) dσ) ∈ (0, 1]. Finally Ψ ≥ Ψ̃_min − ε₀ ≥ 1.4832 on every segment
([[sec:tab-bg-ray-defects]]), while μ ≤ 3/2 < 1.4832²: so f > 0 along every ray of the box. ∎

#### Region III and the seed region {#sec:bg-seed}

Let Φ := Ψ(u2, ·), Φ̃ := Ψ̃(u2, ·), a polynomial of degree 12 in ρ (its Chebyshev coefficients C_k are the column sums
of [[sec:tab-bg-ray]]). By [[eq:bg-psi3-def]] and d/dv̂ = a(ρ) d/dρ, the derivatives of ψ_III are ψ_III^(k)(v̂(ρ)) =
Ψ_k(ρ, Φ(ρ), Φ′(ρ), Φ″(ρ), Φ‴(ρ), μ3), where

    Ψ_0 := ln Φ′ + ln f1(ρ) − ln f3(Φ),    Ψ_1 := a(ρ) 𝒟Ψ_0,    Ψ_2 := a(ρ) 𝒟Ψ_1,                       {#eq:bg-psi3}

𝒟 the total derivative in ρ (Φ^(j) ↦ Φ^(j+1)). Explicitly, with h3(X) := 1/(X³ − μ3X),

    Ψ_1 = a(Φ″/Φ′) + a′ − 2μ3 a Φ′ h3(Φ),     Ψ_2 = a 𝒟Ψ_1,

that is Ψ_1 = aΦ″/Φ′ + a′ − μ3E/Φ³ with E = f1Φ′/f3(Φ), which is ψ_v̂ of [[eq:bg-inputs]] at u = u2, where B = 0.

**Proposition {#prop:bg-seed}** (Region III and the seed region.) Let ψ_s and μ_s be the reference quintic and mass of
[[sec:table-seed-profile]].

(a) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in the points with 0.68 ≤ R ≤ R_u2, where 1.8614098 ≤ R_u2 ≤ 1.8614596;
in particular the seed region 0.70 ≤ R ≤ 1.861 (0.02 ≤ v̂ ≤ 1.181) lies in region III, and f3(Φ(ρ)) > 0 for every
ρ ∈ [2.32, 3.44].

(b) For every v̂ ∈ [0.02, 1.181],

    |ψ_s(v̂) − ψ_III(v̂)| ≤ 3.03 × 10⁻⁵,  |ψ_s′(v̂) − ψ_III′(v̂)| ≤ 2.40 × 10⁻⁴,  |ψ_s″(v̂) − ψ_III″(v̂)| ≤ 8.56 × 10⁻⁴,

and |μ3 − μ_s| ≤ 1.79 × 10⁻⁶. In particular the bounds 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ (k = 0, 1, 2) and 1.4 ×
10⁻⁵ hold at every point of the seed region.

(c) Consequently (ψ_III, ψ_III′, ψ_III″) lies within (10⁻³, 10⁻³, 3 × 10⁻²) of (ψ_s, ψ_s′, ψ_s″) on the seed region and
|μ3 − μ_s| ≤ 10⁻⁴: the background lies in the tube of [[prop:margins-seed]] (b), and Γ > 0 on the seed region.

Proof. (a) On Σ_τ0, R = v̂ + 0.68 ≥ 0.68 since v̂ ≥ 0, and by [[lem:bg-reduction]] (f) a point of Σ_τ0 with R ≤ R_* lies
on a ray ρ ∈ [2.321, R_*] ⊂ [2.32, 3.44]. Let g(ρ) := Φ(ρ) − v̂(ρ) − 0.68 for ρ ∈ [2.32, 3.44]. Its derivative is J(u2,
ρ) − 1/a(ρ) < 1 − 2 < 0 since J ≤ 1 ([[prop:bg-rays]]) and a < 1/2. By [[prop:bg-rays]], g(2.77362) ≥ Φ̃(2.77362) −
v̂(2.77362) − 0.68 − ε₀ ≥ 1.89 × 10⁻⁵ > 0 and g(2.77364) ≤ −1.27 × 10⁻⁵ < 0; so g has one zero ρ_u2 ∈ (2.77362, 2.77364).
A point of Σ_τ0 on the ray ρ has R = v̂(ρ) + 0.68; since R decreases along the ray ([[lem:bg-reduction]] (c)) it lies in
{u ≥ u2} exactly when R ≤ Φ(ρ), that is g(ρ) ≥ 0, that is ρ ≤ ρ_u2. Hence R_u2 = v̂(ρ_u2) + 0.68 ∈ [v̂(2.77362) + 0.68,
v̂(2.77364) + 0.68] ⊂ [1.8614098, 1.8614596]. The seed region has ρ ≤ v̂⁻¹(1.181) < 2.7735 < ρ_u2 (v̂(2.7735) ≥ 1.18111).
And f3(Φ) ≥ 1 − 0.8222/1.4832² > 0 by [[prop:bg-rays]] and [[prop:bg-nprime]].

(b) Since v̂(2.3282) ≤ 0.0199332 < 0.02 and v̂(2.7735) ≥ 1.18111 > 1.181, it suffices to bound, for ρ ∈ [2.3282,
2.7735] and k = 0, 1, 2, the function e_k(ρ) := ψ_s^(k)(v̂(ρ)) − Ψ_k(ρ, Φ, …, μ3). Split

    e_k = ẽ_k + (Ψ_k(ρ, Φ̃, …, μ̃3) − Ψ_k(ρ, Φ, …, μ3)),
    ẽ_k(ρ) := ψ_s^(k)(v̂(ρ)) − Ψ_k(ρ, Φ̃, …, μ̃3).  {#eq:bg-seed-split}

On each interval of [[sec:tab-bg-seed]], consider the box

    ρ in the interval,   Φ^(j) in the enclosure of Φ̃^(j) on it widened by ε_j (j ≤ 3),
    |μ3 − μ̃3| ≤ 4.07 × 10⁻⁷.  {#eq:bg-seed-box}

It contains (Φ, …, μ3) and (Φ̃, …, μ̃3) ([[prop:bg-rays]] at u2, [[prop:bg-nprime]] (ii)), and the partial derivatives
of Ψ_k are bounded there as in [[sec:tab-bg-seed]] ([[lem:bg-tools]] (d)). By the mean value theorem the second term
of [[eq:bg-seed-split]] is at most

    Δ_k := Σ_(j≤3) sup|∂Ψ_k/∂Φ^(j)| ε_j + sup|∂Ψ_k/∂μ3| · 4.07 × 10⁻⁷,  {#eq:bg-seed-delta}

that is Δ_0 = 3.34 × 10⁻⁶, Δ_1 = 5.20 × 10⁻⁶, Δ_2 = 1.50 × 10⁻⁵.

The function ẽ_k is bounded by [[lem:bg-tools]] (c) with N = 5 at the midpoint ρ_m of each interval: |ẽ_k| ≤ Σ_(n≤5)
|c_n| hⁿ + h⁶ sup |c_6(ξ)|, where c_n is the n-th Taylor coefficient of ẽ_k at ρ_m, c_6(ξ) := ẽ_k^(6)(ξ)/6! for ξ in
the interval, and h is the half-width. These coefficients are obtained as follows. The function ẽ_k is built from ρ by
sums, products, quotients, logarithms and 𝒟: Φ̃ = Σ C_j T_j(y) with y = (ρ − 2.88)/0.56 and T_(j+1) = 2yT_j − T_(j−1);
f1 = 1 − 3/(2ρ²), a = f1/2 and f3(Φ̃) = 1 − μ̃3/Φ̃²; Ψ_0 = ln Φ̃′ + ln f1 − ln f3(Φ̃), Ψ_1 = a𝒟Ψ_0 and Ψ_2 = a𝒟Ψ_1
([[eq:bg-psi3]]); v̂ = F(ρ) − F(2.321) with F of [[eq:bg-tangherlini]]; and ψ_s^(k)(v̂), where the k-th derivative
ψ_s^(k) of the quintic is a polynomial. Starting from the Taylor series ρ_0 + t of ρ at a point ρ_0, the rules
[[eq:bg-series]] give the Taylor coefficients at ρ_0 of each of these functions in turn, up to order 9 (Φ̃ is a
polynomial, so its series is exact; Φ̃′ and each 𝒟 lower the order by one), and so those of ẽ_k up to order 6; every
operation on numbers is replaced by [[lem:bg-tools]] (d), with √(3/2) enclosed by it. With ρ_0 = ρ_m this encloses c_0,
…, c_5. With ρ_0 replaced by each of twenty equal parts P of the interval, the same steps enclose, at every ξ ∈ P, the
coefficients at ξ, since each is the same finite combination of ξ; the sixth one encloses c_6(ξ). This gives the column
"Taylor" of [[sec:tab-bg-seed]] and the rest, at most 2 × 10⁻¹⁰ in every row, and the totals Taylor + rest + Δ_k
bound |e_k| on each interval. The largest totals are 3.020 × 10⁻⁵, 2.394 × 10⁻⁴ and 8.558 × 10⁻⁴, all on the first
interval. Finally |μ3 − μ_s| ≤ |μ̃3 − μ_s| + 4.07 × 10⁻⁷ ≤ 1.3809 × 10⁻⁶ + 4.07 × 10⁻⁷.

(c) The bounds of (b) are below (10⁻³, 10⁻³, 3 × 10⁻²) and 10⁻⁴; [[prop:margins-seed]] (b) states Γ > 0 for every
background of the tube. ∎

#### The slice below R_* {#sec:bg-slice}

**Proposition {#prop:bg-slice}** (Hyperbolicity below R_*.) At every point of Σ_τ0 with 0.68 ≤ R ≤ R_*, κ > 0, K^l_l <
0 and κK^l_l ≤ −6.00 × 10⁻³; in particular κK^l_l ≤ −4.76 × 10⁻³.

Proof. By [[lem:bg-reduction]] (f) the point lies on a ray ρ ∈ [2.321, R_*] with R = v̂(ρ) + 0.68 =: T(ρ). By
[[prop:bg-seed]] (a) it lies in region III if ρ ≤ ρ_u2 ≤ 2.77364, and otherwise in the packet u1 ≤ u ≤ u2.

*Region III.* On each interval of [[sec:tab-bg-slice-iii]], ψ_III and ψ_III′ are enclosed by [[eq:bg-psi3]] with Φ
in Φ̃ ± ε₀, Φ′ in Φ̃′ ± ε₁, Φ″ in Φ̃″ ± ε₂ ([[prop:bg-rays]]), and R by T on the interval. [[lem:bg-slice-forms]] and
[[lem:bg-tools]] (d) give Ef < 1, N_κ < 0 and κK^l_l ≤ −0.093 on every row (E = e^(ψ_III) > 0, Ef < 2).

*The packet.* For ρ ∈ [ρ_u2, R_*] the slice point is at the unique u_s(ρ) ∈ [u1, u2] with Ψ(u_s, ρ) = T(ρ): the
difference Ψ(u, ρ) − T(ρ) is ≥ 0 at u1 (ρ ≥ T(ρ) for ρ ≤ R_*, by [[lem:bg-rstar]]), ≤ 0 at u2 (g(ρ) ≤ 0), and decreasing
in u (∂_uΨ = G < 0 since f > 0, [[prop:bg-rays]]). It is also decreasing in ρ, since ∂_ρ(Ψ − T) = J − 1/a < 0; hence u_s
is decreasing in ρ, and so is the inverse ρ_s(u). For each row [u_a, u_b] of [[sec:tab-bg-slice-packet]], Ψ̃(u_a, ρ_hi) +
ε₀ < T(ρ_hi) and Ψ̃(u_b, ρ_lo) − ε₀ > T(ρ_lo) (by direct evaluation; at u_a = u1 take ρ_hi ≥ R_* from [[lem:bg-rstar]],
at u_b = u2 take ρ_lo ≤ ρ_u2 from [[prop:bg-seed]] (a)), so the slice points with u_s ∈ [u_a, u_b] have ρ ∈ [ρ_lo, ρ_hi].
On the box [u_a, u_b] × [ρ_lo, ρ_hi]: μ and λ lie between their values at u_a and u_b (monotone, [[prop:bg-nprime]]
(iii)), which are μ̃, λ̃ there up to the errors 4.2 × 10⁻⁷ and 5 × 10⁻⁸ of [[prop:bg-nprime]] (iv); B lies between its
end values, or between the smaller one and 17/10 when 6.45 is inside, by [[lem:bg-tools]] (e); J and K lie in the
Chebyshev enclosures of J̃, K̃ on the box widened by ε₁, ε₂, with J ≤ 1; and R ∈ [T(ρ_lo), T(ρ_hi)]. Then
[[eq:bg-nk-packet]] and [[lem:bg-tools]] (d) give the enclosures of Ef and N_κ in the second table: Ef < 1 and N_κ < 0 on
every row, and the largest upper bound of κK^l_l is −6.00 × 10⁻³, on the row u ∈ [6.05, 6.1]. ∎

Near R = R_* the packet's slice points approach region I, where E = 1 and N_κ = (μ/R³)(f − 3) exactly, and κK^l_l =
3(3/2)R_*⁻³(f − 3)(1 − f)/(R_*(2 − f)²) = −6.86 × 10⁻³ at R_*, f = 1 − 3/(2R_*²); the first rows' bounds are close to it.

#### The theorem {#sec:bg-theorem}

**Theorem {#thm:bg-margins}** (The background below R_*.) For the background of [[pending:sec-two-dust-background]]:

(a) On 𝒩′, λ ≥ 0.529 on [u1, u2]; R(u2) ∈ [1.519357, 1.519359]; the mass of region III satisfies μ3 ∈ [0.8220998,
0.8221253] and R(u2)² > μ3.

(b) Region III meets Σ_τ0 ∩ {R ≤ R_*} exactly in 0.68 ≤ R ≤ R_u2, where 1.861394 ≤ R_u2 ≤ 1.861466, and contains the
seed region. On the seed region, |ψ_s^(k) − ψ_III^(k)| ≤ 5.1 × 10⁻⁵, 2.6 × 10⁻⁴, 8.7 × 10⁻⁴ for k = 0, 1, 2, and |μ3 −
μ_s| ≤ 1.4 × 10⁻⁵; so the background lies in the tube of [[prop:margins-seed]] (b) and Γ > 0 on the seed region.

(c) On Σ_τ0 for 0.68 ≤ R ≤ R_*: κ > 0, K^l_l < 0 and κK^l_l ≤ −4.76 × 10⁻³.

Proof. (a) is [[prop:bg-nprime]], (b) is [[prop:bg-seed]], (c) is [[prop:bg-slice]]. ∎

**Remark {#rem:bg-grid}** (Numerical observation.) The reference quintic ψ_s of [[sec:table-seed-profile]] is the first
piece of a degree-5 smoothing spline fitted to the values of ψ_III on a second-order finite-difference solution of the
characteristic problem on a double-null grid with 160 steps per unit, and μ_s is that solution's mass in region III.
The same grid solution reproduces the six inputs [[eq:bg-inputs]] at 40 points of the packet on Σ_τ0 to within
2.0 × 10⁻³ (E), 1.1 × 10⁻³ (f), 2.7 × 10⁻³ (ψ_R, of size 0.20), 2.0 × 10⁻³ (ψ_v̂, of size 0.06), 2.8 × 10⁻³ (f_R) and
7.7 × 10⁻⁴ (f_v̂), up to 3 % of the smaller inputs. No proof uses this remark: [[prop:bg-seed]] uses only the printed
coefficients of ψ_s and the number μ_s.