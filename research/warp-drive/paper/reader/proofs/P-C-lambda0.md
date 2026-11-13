This part proves, at one parameter point, the constants on which the bounds of [[prop:lambda0]] and the threshold of
[[thm:layer]] rest: the envelope constant c_e, the constants of the domain, and ε1 and C_app in three norms; the
admissible range of ε1 there is that of [[sec:profiles]]. Every number below is justified by an inequality between
explicit rationals, or by the value of an elementary function at a rational point, and can be checked by hand.

### The numerical point {#sec:lambda0-point}

**Definition {#def:lambda0-point}** (The numerical point.) The numerical point is l5 = 1/10, μ0 = 1, A = 1, T = 1,
τ0 = −2, the envelope env of [[lem:envelope-constant]], with v_start = 1/2 and v_end = 7/2, and a = δ0 = q0/2. Then
V = v_end + T = 9/2, and μ' = (2/9) A² env² ([[eq:mu-rate]]).

**Lemma {#lem:lambda0-point}** (The domain at the numerical point.) At the numerical point:

(a) q0⁸ = 9/1250, 0.539717577 < q0 < 0.539717578, 0.2698587885 < a < 0.269858789, and μ0/a² = 4/q0² > 13;

(b) μ_end = 227/192 and 1.042752 < μ_end^(1/4) < 1.042753;

(c) v − r_q(v) increases in v, so τ_end = V − q_end with q_end := q0 μ_end^(1/4) ∈ (0.5627915, 0.5627922);

(d) m* := sup_Ω μ/r² equals μ_end/a² = (227/48) q0⁻², lies in (16.23497014, 16.23497021), and is attained at the
corner τ = τ_end, r = a of Ω.

*Proof.* (a) q0 = (√72 μ0 l5²)^(1/4) gives q0⁸ = 72/10⁴ = 9/1250 = 0.0072. Three squarings give
0.539717577⁸ < 0.0072 < 0.539717578⁸, and a = q0/2. Then μ0/a² = 4/q0² > 4/0.539717578² > 13.73.

(b) μ_end = μ0 + (2/9) A² ∫ env² = 1 + (2/9)(105/128) = 227/192 by [[lem:envelope-constant]] (a), and
1.042752⁴ < 227/192 < 1.042753⁴.

(c) r_q(v) = q0 μ(v)^(1/4), so r_q' = (q0/4) μ^(−3/4) μ' ≤ (q0/4)(2/9) c_e² < 0.06, using μ ≥ 1 and
env ≤ c_e < 1.33 ([[lem:envelope-constant]]). So v − r_q(v) increases, its maximum over v ≤ V is at v = V, where
μ = μ_end, and τ_end = V − q_end. The bounds on q_end are the products of those in (a) and (b).

(d) On Ω, μ ≤ μ_end and r ≥ a, so μ/r² ≤ μ_end/a² = (227/192)(4/q0²). The corner τ = τ_end, r = a lies in Ω, since
v + τ − τ_end = τ_end + a < V + 1; there v = τ_end + a = 9/2 − q_end + a > 4.2 > v_end, so μ = μ_end. The bounds
follow from (a): (227/48)/0.539717578² > 16.23497014 and (227/48)/0.539717577² < 16.23497021. ∎

### The envelope and its constant {#sec:envelope-constant}

Put, for y ∈ ℝ,

    β(y) := cos¹²(πy/2) exp(−y²/(1 − y²))  for |y| < 1,     β(y) := 0  for |y| ≥ 1,
    I := ∫_(−1)^1 β(y)² dy,      c_e := (35/(64 I))^(1/2),      env(v) := c_e β((2v − 4)/3).            {#eq:envelope}

This is the envelope env_C of [[rem:envelope-regularity]], and c_e is the constant written c there.

**Lemma {#lem:envelope-constant}** (The envelope constant.) (a) env ∈ C_c^∞(ℝ) with support [1/2, 7/2],
∫ env² = 105/128, and max env = env(2) = c_e. With μ' = (2/9) A² env² and μ = μ0 before v = 1/2, μ is smooth,
nondecreasing, constant outside [1/2, 7/2], and μ_end = μ0 + (2/9) A² (105/128).

(b) 0.3119281 < I < 0.3119286, and therefore

    1.3240867 < c_e < 1.3240879;   in particular   1.3240711 < c_e < 1.3241035.                          {#eq:envelope-c}

*Proof.* (a) exp(−y²/(1 − y²)) = e · exp(−1/(1 − y²)), so β = e cos¹²(πy/2) φ(1 − y²) with φ(t) = exp(−1/t) for t > 0
and φ(t) = 0 for t ≤ 0. For t > 0, φ^(k)(t) = P_k(1/t) exp(−1/t) with P_0 = 1 and P_(k+1)(x) = x² (P_k(x) − P_k'(x)),
by induction from d/dt [P(1/t) e^(−1/t)] = t⁻² (P − P')(1/t) e^(−1/t); since P_k(x) e^(−x) → 0 as x → ∞, every
derivative of φ tends to 0 at 0+, and φ ∈ C^∞(ℝ). Composition with 1 − y² and the product with cos¹² keep C^∞, and
β > 0 exactly on |y| < 1, so env has support [1/2, 7/2]. The substitution y = (2v − 4)/3 gives ∫ env² = (3/2) c_e² I =
(3/2)(35/64) = 105/128. Since 0 ≤ β ≤ 1 = β(0), max env = c_e at v = 2. The statements on μ follow from μ' ≥ 0.

(b) *The substitution.* Put y = tanh s. Then dy = sech² s ds, 1 − y² = sech² s and y²/(1 − y²) = sinh² s, so

    I = ∫_ℝ G(s) ds,        G(s) := cos²⁴((π/2) tanh s) exp(−2 sinh² s) sech² s.

G is even, positive, and decreasing on [0, ∞), each of its three factors being so.

*Bounds in a strip.* G extends holomorphically to |Im s| < π/4. Let s = x + it with x real and |t| ≤ d < π/4. From
tanh(x + it) = (sinh 2x + i sin 2t)/(cosh 2x + cos 2t) one has |Im tanh s| ≤ sin 2|t|/(1 + cos 2t) = tan |t| ≤ tan d;
with |cos w|² = cos²(Re w) + sinh²(Im w) ≤ cosh²(Im w) this gives |cos²⁴((π/2) tanh s)| ≤ cosh²⁴((π/2) tan d). From
sinh s = sinh x cos t + i cosh x sin t, Re sinh² s = sinh² x cos 2t − sin² t, so |exp(−2 sinh² s)| ≤
exp(2 sin² d − 2 cos(2d) sinh² x). And |cosh s|² = sinh² x + cos² t ≥ cos² d. Since sinh² x ≥ x²,

    ∫_ℝ |G(x + it)| dx ≤ M_d := cosh²⁴((π/2) tan d) e^(2 sin² d) sec² d (π/(2 cos 2d))^(1/2),         {#eq:strip-bound}

and |G(x + it)| → 0 as |x| → ∞ uniformly in |t| ≤ d.

*The trapezoidal rule.* Let Ĝ(ω) := ∫_ℝ G(s) e^(−iωs) ds. Moving the line of integration to Im s = −d sgn ω, which
Cauchy's theorem on long rectangles allows by the uniform decay, gives |Ĝ(ω)| ≤ M_d e^(−d|ω|) by [[eq:strip-bound]].
We use the Poisson summation formula in the following form: if G is continuous and integrable on ℝ, h > 0, the series
Σ_(n∈ℤ) G(x + nh) converges uniformly for x ∈ [0, h], and Σ_(k∈ℤ) |Ĝ(2πk/h)| < ∞, then h Σ_(n∈ℤ) G(nh) =
Σ_(k∈ℤ) Ĝ(2πk/h). Indeed, F(x) := Σ_(n∈ℤ) G(x + nh) is then continuous and h-periodic, and integration term by term
gives its Fourier coefficients (1/h) ∫_0^h F(x) e^(−2πikx/h) dx = (1/h) Ĝ(2πk/h). These are absolutely summable, so
the Fourier series of F converges uniformly to a continuous h-periodic function with the same Fourier coefficients as
F; that function is F, since a continuous periodic function is determined by its Fourier coefficients (Fejér's
theorem), and at x = 0 this is the formula. The hypotheses hold here. G is continuous, and 0 < G(s) ≤ e^(−2s²) since
cos²⁴((π/2) tanh s) ≤ 1, sech² s ≤ 1 and sinh² s ≥ s², so G is integrable. As G is even and decreasing on [0, ∞), for
x ∈ [0, h] one has G(x + nh) ≤ G(nh) ≤ e^(−2n²h²) when n ≥ 0 and G(x + nh) ≤ G((|n| − 1)h) ≤ e^(−2(|n| − 1)²h²) when
n ≤ −1, a summable majorant independent of x; and Σ_k |Ĝ(2πk/h)| ≤ Σ_k M_d e^(−2πd|k|/h) < ∞. Hence, as Ĝ(0) = I,
for every h > 0

    T_h := h Σ_(n∈ℤ) G(nh) = Σ_(k∈ℤ) Ĝ(2πk/h),     |T_h − I| ≤ 2 M_d Σ_(k≥1) e^(−2πkd/h) = 2 M_d/(e^(2πd/h) − 1).

Take d = 1/2 and h = 1/8, so 2πd/h = 8π and e^(8π) > 8.2 · 10¹⁰. The four factors of M_(1/2) are
cosh((π/2) tan(1/2)) = 1.39134…, whose 24th power is below 2770, e^(2 sin²(1/2)) < 1.5836, sec²(1/2) < 1.2985 and
(π/(2 cos 1))^(1/2) < 1.7051. So M_(1/2) < 9720 and |T_(1/8) − I| < 2.4 · 10⁻⁷.

*The nodes.* The values of G at the nodes, each within 5 · 10⁻¹³ of the printed decimal, are

    G(0) = 1,                    G(1/8) = 0.601818088179,     G(2/8) = 0.133828260085,
    G(3/8) = 0.011630921782,     G(4/8) = 0.000428710754,     G(5/8) = 0.000007358228,
    G(6/8) = 0.000000064420,     G(7/8) = 0.000000000311.

For s ≥ 1, cos((π/2) tanh s) ≤ cos((π/2) tanh 1) < 0.366 and sech² s ≤ 1, sinh² s ≥ s², so
G(s) ≤ 0.366²⁴ e^(−2s²), and since n²/32 ≥ n/4 for n ≥ 8,

    Σ_(n≥8) G(n/8) ≤ 0.366²⁴ Σ_(n≥8) e^(−n/4) = 0.366²⁴ e^(−2)/(1 − e^(−1/4)) < 3 · 10⁻¹¹.

The seven printed values for n = 1, …, 7 sum to 0.747713403759, so T_(1/8) = (1/8)(1 + 2 Σ_(n≥1) G(n/8)) lies in
(0.31192835093, 0.31192835095 + 10⁻¹¹). With the error bound, 0.3119281 < I < 0.3119286.

*The constant.* c_e² = 35/(64 I). Now 1.3240867² · 64 · 0.3119286 < 35 < 1.3240879² · 64 · 0.3119281, which is
[[eq:envelope-c]]. ∎

**Remark {#rem:envelope-dependence}** (Which end of c_e each bound uses.) The two ends of [[eq:envelope-c]] enter
different bounds. (i) The lower end enters every bound on λ0 at the numerical point that rests on the size of the wave.
In the operator norm, whatever the mean m1, every admissible C_app is at least (4/3) c_e a^(−3/2), the operator norm
of W_TT at the point X* of [[sec:lambda0-norms]] at the phase s = 0 ([[prop:lambda0-norms]] (i) and its proof), and by
[[lem:lambda0-point]] (a), a^(−3/2) > 7.133376, so

    (4/3) c_e a^(−3/2) ≥ (4/3) · 1.3240711 · 7.133376 > 12.593309.

This uses c_e ≥ 1.3240711 and nothing else about c_e; with any proven lower bound c₋ for c_e in its place the constant
is (4/3) c₋ a^(−3/2). Combined with ε1 < s0 < 0.030768560 ([[sec:epsilon-one]]), the quotient of the two is
0.030768560/12.593309 < 0.0024433, which is the operator-norm bound of [[prop:lambda0]]; that bound therefore holds
exactly as far as the lower end of c_e does. The Frobenius and largest-entry bounds 0.0019079 and 0.0012228 use the
lower end in the same way, and no other property of c_e ([[rem:lambda0-norms-c]]). (ii) The upper end enters through
env ≤ c_e: in [[lem:lambda0-point]] (c), where any c_e < 3 suffices, and in the bound 1 + c_e²/18 ≤ 1.0974028 used for
the threshold of [[thm:layer]], which needs c_e ≤ 1.3241035.

### The admissible range of ε1 {#sec:epsilon-one}

At the numerical point, items (i)–(iii) at the end of [[sec:profiles]] give three facts. First, μ0/a² − 1 > 12, so the
standing condition 0 < ε1 < min(s0, μ0/a² − 1) of [[sec:profiles]] reads 0 < ε1 < s0. Second, no ε1 ≥ 0.6013096
serves for [[lem:domain]] (e). Third, 0.030768559 < s0 < 0.030768560, where s0 = (m*² + 1)^(1/2) − m* and m* = μ_end/a²
is the number of [[lem:lambda0-point]] (d). So every admissible ε1 is below 0.030768560.

### The second harmonic of stage 0 {#sec:second-harmonic}

The wave W_TT and the second harmonic χ are those of [[lem:stage-zero]] and [[eq:chi-transport]]. Here c² = cos² ϑ and
s² = sin² ϑ are the angular functions of [[sec:waves]], q := cos 2ϑ = c² − s², and h² = 2/(1 + q²).

**Lemma {#lem:chi-closed-form}** (The second harmonic.) On Ω × S¹,

    χ = −(1/12) A² env(v)² h² (4q sin 2θ + (1 − q²) cos 2θ) (r⁻² − (v − τ0)^(−1/2) r^(−3/2)).

*Proof.* With ∂_θ y1 = −(α/3) a1, ∂_θ y2 = (α/3) a2, a1 := 2c² sin θ + s² cos θ, a2 := 2s² cos θ + c² sin θ, one has
a1² − a1 a2 + a2² = 3(c⁴ sin² θ + s⁴ cos² θ + c² s² sin θ cos θ). With sin² θ = (1 − cos 2θ)/2, cos² θ =
(1 + cos 2θ)/2, c⁴ − s⁴ = q and c² s² = (1 − q²)/4, the definition of F_2 after [[lem:stage-zero]] becomes

    F_2 = (α²/3)((c⁴ − s⁴) cos 2θ − c² s² sin 2θ) = (α²/12)(4q cos 2θ − (1 − q²) sin 2θ),   α² = A² env² h² r⁻³.

Along ℓ = ∂_r at fixed (v, ϑ, φ1, φ2), the transport (∂_r + 3/(2r)) Z = r⁻³ K, K independent of r, with Z = 0 at
r = v − τ0 (that is, on Σ_τ0), has the solution Z = −2K (r⁻² − (v − τ0)^(−1/2) r^(−3/2)), since (r^(3/2) Z)' =
r^(−3/2) K. The θ-primitive of 4q cos 2θ − (1 − q²) sin 2θ with zero mean is (1/2)(4q sin 2θ + (1 − q²) cos 2θ). ∎

### The threshold in three norms {#sec:lambda0-norms}

The bounds of [[prop:lambda0]] compare ε1 with a constant C_app such that |g_app − g0| ≤ C_app λ. Both depend on how
|·| is read on symmetric 2-tensors of Cartesian components. This section treats three readings: the operator norm of
[[sec:profiles]], the Frobenius norm |·|_F, and the largest absolute entry |·|_max. Let X* be the point
τ = 2 − a, x = (a, 0, 0, 0) (so r = a, v = 2, ϑ = 0, φ1 = 0). It lies in Ω of [[eq:omega]], since τ0 < 2 − a < τ_end
by [[lem:lambda0-point]] (c) and v + τ − τ_end < 4 < V + 1. Put

    K := c_e a^(−3/2),      χ* := (c_e²/3)(a⁻² − a^(−3/2)/2),      B := (4/3) K² + 4 χ*².

**Proposition {#prop:lambda0-norms}** (ε1 and C_app in three norms.) At the numerical point let g_app = g0 + λ [g1] +
Σ_(j≥2) λ^j [g_j] be an approximant of [[thm:approximant]], built from any stage data, and let C_app be a number such
that |g_app − g0| ≤ C_app λ on Ω for every λ in some interval (0, λ̄], λ̄ > 0. Let ε1 > 0 be such that every symmetric
g̃ with |g̃ − g0| ≤ ε1 on Ω is nondegenerate, as [[lem:lorentz-margin]] requires of it, and let M_22 be the (x2, x2)
Cartesian component of the mean m1(X*) of g1 at X*. Then:

(i) in the operator norm, ε1 < s0 and C_app ≥ (4/3) K + |M_22|;

(ii) in the Frobenius norm, ε1 < s0 and C_app² ≥ B + |m1(X*)|_F²;

(iii) in the largest absolute entry, ε1 < 1/(4m*) and C_app ≥ (4/3) K + |M_22|.

In particular, whatever the stage data, C_app > 12.593309 in (i) and (iii) and C_app > 16.127552 in (ii), and

    ε1/C_app < 0.0024433 in (i),    ε1/C_app < 0.0019079 in (ii),    ε1/C_app < 0.0012228 in (iii).  {#eq:lambda0-norms}

*Proof.* *C_app bounds g1 at every point.* Fix (X, θ) ∈ Ω × S¹ with v(X) > 0, and take θ ∈ (0, 2π]. For n = 1, 2, …
put λ_n := v(X)/(θ + 2πn). Then λ_n → 0 and v(X)/λ_n = θ + 2πn, so at X, (g_app − g0)/λ_n = g1(X, θ) +
Σ_(j≥2) λ_n^(j−1) g_j(X, θ). The profiles g_j are bounded, so letting n → ∞ gives |g1(X, θ)| ≤ C_app. At X*, v = 2.

*g1 at X*.* By [[thm:approximant]], g1(X*, θ) = m1(X*) + W_TT(X*, s) + χ(X*, s) D with s := θ + φ1(X*) and
D := dv ⊗ dv; as θ runs over S¹, so does s. At X*, A = 1, env(2) = c_e β(0) = c_e, cos 2ϑ = 1 and h = 1, and
x1 = a, x2 = x3 = x4 = 0, cos²ϑ = 1, sin²ϑ = 0. The Cartesian formula of [[lem:waves]] (a), at the phase s, gives
λ W_TT = 2 a^(−3/2) (G dx2² − (G/3)(dx2² + dx3² + dx4²)) with G/λ = A env h cos s = c_e cos s, so in the components
(τ, x1, x2, x3, x4)

    W_TT(X*, s) = K cos s Λ,      Λ := diag(0, 0, 4/3, −2/3, −2/3).

By [[lem:chi-closed-form]], with cos 2ϑ = 1, h = 1 and v − τ0 = 4, χ(X*, s) = −(1/3) c_e² sin 2s (a⁻² − a^(−3/2)/2) =
−χ* sin 2s. And dv = dτ + dx1 at X*, so D = U Uᵀ with U = (1, 1, 0, 0, 0): D_22 = 0 and |D|_F = |U|² = 2.

*(i) and (iii).* The (x2, x2) entry of g1(X*, θ) is M_22 + (4/3) K cos s. It is e2ᵀ g1 e2 for the unit vector e2, so
it bounds both the operator norm and the largest absolute entry, and its supremum over s is |M_22| + (4/3) K.

*(ii).* Write W(s) := W_TT(X*, s), χ := χ(X*, s) and Y(s) := g1 at the phase s. Since W(s + π) = −W(s),
χ(X*, s + π) = χ and χ(X*, s ± π/2) = −χ, the parallelogram law gives |Y(s)|_F² + |Y(s + π)|_F² =
2|m1(X*) + χD|_F² + 2|W(s)|_F² and |Y(s + π/2)|_F² + |Y(s − π/2)|_F² = 2|m1(X*) − χD|_F² + 2|W(s + π/2)|_F². Here
|W(s)|_F² + |W(s + π/2)|_F² = K² |Λ|_F² = (8/3) K² and |m1(X*) + χD|_F² + |m1(X*) − χD|_F² = 2|m1(X*)|_F² + 8χ², so
the four squares sum to 4|m1(X*)|_F² + 16χ² + (16/3) K², and the largest of them is at least
|m1(X*)|_F² + 4χ² + (4/3) K². At s = π/4, χ² = χ*², so C_app² ≥ |m1(X*)|_F² + B.

*The thresholds for ε1.* At a point of Ω where μ/r² = m*, let e be the unit eigenvector of g0 with eigenvalue −s0
([[lem:lorentz-margin]]). Then g0 + s0 e eᵀ annihilates e, and |s0 e eᵀ| = s0 in the operator and in the Frobenius
norm, e eᵀ having rank one; so ε1 < s0 in (i) and (ii). For (iii) take the point (τ_end, (a, 0, 0, 0)) of Ω, where
μ/r² = m* ([[lem:lambda0-point]] (d)) and x̂ = e1. There the (τ, x1) block of g0 is [[−1 + m*, m*], [m*, 1 + m*]], with
inverse [[−1 − m*, m*], [m*, 1 − m*]], and g0 is the identity on the other directions. For ξ := (1, −1, 0, 0, 0),
ξᵀ g0⁻¹ ξ = (−1 − m*) − 2m* + (1 − m*) = −4m*, so the rank-one formula gives det(g0 + t ξ ξᵀ) = det g0 (1 − 4m* t) =
4m* t − 1. Every entry of t ξ ξᵀ is ±t or 0, so g0 + ξ ξᵀ/(4m*) is degenerate and |ξ ξᵀ/(4m*)|_max = 1/(4m*); so
ε1 < 1/(4m*).

*The numbers.* By [[lem:lambda0-point]] (a), 0.2698587885 < a < 0.269858789, so a^(−3/2) > 7.1333765,
a^(−3/2) < 7.1333766 and a⁻² > 13.7317809: indeed 0.269858789³ · 7.1333765² < 1, 0.2698587885³ · 7.1333766² > 1 and
0.269858789² · 13.7317809 < 1. Hence a⁻² − a^(−3/2)/2 > 13.7317809 − 3.5666883 = 10.1650926. With c_e > 1.3240711
([[eq:envelope-c]]),

    (4/3) K > (4/3)(1.3240711)(7.1333765) > 12.5934635,      χ* > (1.3240711²/3)(10.1650926) > 5.9403588,
    B > (3/4)(12.5934635)² + 4 (5.9403588)² > 260.097942 > 16.127552² = 260.0979337….

By [[sec:epsilon-one]], s0 < 0.030768560, and by [[lem:lambda0-point]] (d), m* > 16.23497014, so 1/(4m*) <
0.0153989. Now 0.0024433 · 12.593309 > 0.03076918, 0.0019079 · 16.127552 > 0.03076975 and 0.0012228 · 12.593309 >
0.01539909, which with these bounds give [[eq:lambda0-norms]]. ∎

Since the threshold of [[prop:lambda0]] lies below ε1/C_app, [[eq:lambda0-norms]] bounds it by 0.0024433, 0.0019079
and 0.0012228 in the three readings, whatever the stage data. A nonzero M_22 lowers the bounds of (i) and (iii), and a
nonzero m1(X*) that of (ii).

**Remark {#rem:lambda0-norms-c}** (The constant c_e in the three bounds.) [[prop:lambda0-norms]] uses about c_e only
a lower bound, through K, χ* and B, which increase with c_e; s0 and m* depend on a and μ_end = 227/192 alone, and the
upper end of c_e enters nowhere. The figure 12.593309 holds for every c_e ≥ 1.3240549 and 16.127552 for every
c_e ≥ 1.3240711, while the three bounds of [[eq:lambda0-norms]] hold for every c_e ≥ 1.32404: at c_e = 1.32404 the
arithmetic above gives (4/3) K > 12.593167 and B > 16.12696², and 0.0024433 · 12.593167, 0.0019079 · 16.12696 and
0.0012228 · 12.593167 exceed 0.030768560, 0.030768560 and 0.0153989. With the sharper lower end c_e > 1.3240867 of
[[eq:envelope-c]] one gets C_app > 12.593611 in (i) and (iii) and C_app > 16.127845 in (ii).
