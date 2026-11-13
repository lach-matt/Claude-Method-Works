This part proves, at one parameter point, the constants on which the bounds of [[prop:lambda0]] and the threshold of
[[thm:layer]] rest: the normalising constant of the envelope and the derivatives of the envelope, the admissible range
of ε1, the energy constant of the wave operator of g0 on Ω, the size of the explicit profiles of stage 0, and the
bounds on ε1 and C_app in three norms. Every number below is justified by an inequality between explicit rationals,
or by the value of an elementary function at a rational point, which the reader can check by hand; the tables that
the bounds on the derivatives of the envelope use are in [[sec:envelope-tables]].

### The numerical point {#sec:lambda0-point}

**Definition {#def:lambda0-point}** (The numerical point.) The numerical point is l5 = 1/10, μ0 = 1, A = 1, T = 1,
τ0 = −2, the envelope env of [[lem:envelope-constant]], with v_start = 1/2 and v_end = 7/2, and a = δ0 = q0/2. Then
V = v_end + T = 9/2, and μ' = (2/9) A² env² ([[eq:mu-rate]]).

**Lemma {#lem:lambda0-point}** (The domain at the numerical point.) At the numerical point:

(a) q0⁸ = 9/1250, 0.539717577 < q0 < 0.539717578, 0.2698587885 < a < 0.269858789, and μ0/a² = 4/q0² > 13;

(b) μ_end = 227/192 and 1.042752 < μ_end^(1/4) < 1.042753;

(c) v − r_q(v) increases in v, so τ_end = V − q_end with q_end := q0 μ_end^(1/4) ∈ (0.5627915, 0.5627922); hence
τ_end − τ0 = 13/2 − q_end < 5.937209 and b(τ0) = 14 − q_end ∈ (13.437207, 13.437209);

(d) m* := sup_Ω μ/r² equals μ_end/a² = (227/48) q0⁻², lies in (16.23497014, 16.23497021), and is attained at the
corner τ = τ_end, r = a of Ω;

(e) on the outer boundary {v + τ = V + 1 + τ_end} of Ω one has μ = μ_end and r = b(τ) ≤ b(τ0), with r = b(τ0) at the
corner τ = τ0.

*Proof.* (a) q0 = (√72 μ0 l5²)^(1/4) gives q0⁸ = 72/10⁴ = 9/1250 = 0.0072. Three squarings give
0.539717577⁸ < 0.0072 < 0.539717578⁸, and a = q0/2. Then μ0/a² = 4/q0² > 4/0.539717578² > 13.73.

(b) μ_end = μ0 + (2/9) A² ∫ env² = 1 + (2/9)(105/128) = 227/192 by [[lem:envelope-constant]] (a), and
1.042752⁴ < 227/192 < 1.042753⁴.

(c) r_q(v) = q0 μ(v)^(1/4), so r_q' = (q0/4) μ^(−3/4) μ' ≤ (q0/4)(2/9) c² < 0.06, using μ ≥ 1 and env ≤ c < 1.33
([[lem:envelope-constant]]). So v − r_q(v) increases, its maximum over v ≤ V is at v = V, where μ = μ_end, and
τ_end = V − q_end. The bounds on q_end are the products of those in (a) and (b). Then τ_end − τ0 = 9/2 − q_end + 2,
and b(τ0) = V + 1 − τ0 + (τ_end − τ0) = 19/2 + τ_end = 14 − q_end.

(d) On Ω, μ ≤ μ_end and r ≥ a, so μ/r² ≤ μ_end/a² = (227/192)(4/q0²). The corner τ = τ_end, r = a lies in Ω, since
v + τ − τ_end = τ_end + a < V + 1; there v = τ_end + a = 9/2 − q_end + a > 4.2 > v_end, so μ = μ_end. The bounds
follow from (a): (227/48)/0.539717578² > 16.23497014 and (227/48)/0.539717577² < 16.23497021.

(e) On the outer boundary v = V + 1 + τ_end − τ ≥ V + 1 > v_end, so μ = μ_end, and r = b(τ) decreases in τ. ∎

### The envelope and its constant {#sec:envelope-constant}

Put, for y ∈ ℝ,

    β(y) := cos¹²(πy/2) exp(−y²/(1 − y²))  for |y| < 1,     β(y) := 0  for |y| ≥ 1,
    I := ∫_(−1)^1 β(y)² dy,      c := (35/(64 I))^(1/2),      env(v) := c β((2v − 4)/3).                {#eq:envelope}

**Lemma {#lem:envelope-constant}** (The envelope constant.) (a) env ∈ C_c^∞(ℝ) with support [1/2, 7/2],
∫ env² = 105/128, and max env = env(2) = c. With μ' = (2/9) A² env² and μ = μ0 before v = 1/2, μ is smooth,
nondecreasing, constant outside [1/2, 7/2], and μ_end = μ0 + (2/9) A² (105/128).

(b) 0.3119281 < I < 0.3119286, and therefore

    1.3240867 < c < 1.3240879;   in particular   1.3240711 < c < 1.3241035.                              {#eq:envelope-c}

*Proof.* (a) exp(−y²/(1 − y²)) = e · exp(−1/(1 − y²)), so β = e cos¹²(πy/2) φ(1 − y²) with φ(t) = exp(−1/t) for t > 0
and φ(t) = 0 for t ≤ 0. For t > 0, φ^(k)(t) = P_k(1/t) exp(−1/t) with P_0 = 1 and P_(k+1)(x) = x² (P_k(x) − P_k'(x)),
by induction from d/dt [P(1/t) e^(−1/t)] = t⁻² (P − P')(1/t) e^(−1/t); since P_k(x) e^(−x) → 0 as x → ∞, every
derivative of φ tends to 0 at 0+, and φ ∈ C^∞(ℝ). Composition with 1 − y² and the product with cos¹² keep C^∞, and
β > 0 exactly on |y| < 1, so env has support [1/2, 7/2]. The substitution y = (2v − 4)/3 gives ∫ env² = (3/2) c² I =
(3/2)(35/64) = 105/128. Since 0 ≤ β ≤ 1 = β(0), max env = c at v = 2. The statements on μ follow from μ' ≥ 0.

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
Cauchy's theorem on long rectangles allows by the uniform decay, gives |Ĝ(ω)| ≤ M_d e^(−d|ω|). G decays faster than
any exponential together with all its derivatives, so the Poisson summation formula applies to it, and for h > 0

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

*The constant.* c² = 35/(64 I). Now 1.3240867² · 64 · 0.3119286 < 35 < 1.3240879² · 64 · 0.3119281, which is
[[eq:envelope-c]]. ∎

**Lemma {#lem:envelope-derivatives}** (Derivatives of the envelope.) For k = 0, …, 14 let e_k := sup_ℝ |env^(k)| and
S_k := sup_ℝ |β^(k)|. Then e_k = c (2/3)^k S_k, and:

(a) for even k, S_k = |β^(k)(0)|, where

    β(0) = 1,     β''(0) = −2 − 3π²,     β⁽⁴⁾(0) = −12 + 36π² + (51/2)π⁴,
    β⁽⁶⁾(0) = −120 + 540π² − 765π⁴ − (681/2)π⁶,
    β⁽⁸⁾(0) = 1680 + 10080π² − 21420π⁴ + 19068π⁶ + 5988π⁸,
    β⁽¹⁰⁾(0) = 574560 − 226800π² − 642600π⁴ + 858060π⁶ − 538920π⁸ − 127128π¹⁰,
    β⁽¹²⁾(0) = 100457280 − 113762880π² + 21205800π⁴ + 37754640π⁶ − 35568720π⁸ + 16780896π¹⁰
               + (12368577/4)π¹²,
    β⁽¹⁴⁾(0) = 18871332480 − 27424837440π² + 14665931280π⁴ − 1717836120π⁶ − 2157835680π⁸
               + 1527061536π¹⁰ − (1125540507/2)π¹² − (332780187/4)π¹⁴;                              {#eq:beta-even}

(b) for odd k, |β^(k)(m_k)| ≤ S_k ≤ |β^(k)(m_k)| + β^(k+1)(m_k)²/(2ν_k), with the points m_k and the numbers ν_k > 0
of [[sec:envelope-table-peaks]]; the two ends differ by less than 5 · 10⁻⁸ S_k;

(c) in numbers, with 1.3240867 < c < 1.3240879 ([[eq:envelope-c]]),

    k    S_k                                   e_k                             e_k ≤
    0    1                                     c                               1.3241
    1    [3.485522216, 3.485522219]            [3.076755, 3.076759]            3.077
    2    31.60881320…                          [18.60124, 18.60127]            18.61
    3    [244.0561121, 244.0561124]            [95.74857, 95.74867]            95.75
    4    2827.237579…                          [739.4583, 739.4590]            739.5
    5    [29624.95630, 29624.95632]            [5165.565, 5165.570]            5166
    6    3.966613886… · 10⁵                    [46109.32, 46109.38]            4.611 · 10⁴
    7    [4.956575167, 4.956575169] · 10⁶      [3.841132, 3.841137] · 10⁵      3.842 · 10⁵
    8    7.316375574… · 10⁷                    [3.779917, 3.779922] · 10⁶      3.780 · 10⁶
    9    [1.027395856, 1.027395858] · 10⁹      [3.538611, 3.538615] · 10⁷      3.539 · 10⁷
    10   1.625817745… · 10¹⁰                   [3.733152, 3.733156] · 10⁸      3.734 · 10⁸
    11   [2.479629522, 2.479629524] · 10¹¹     [3.795765, 3.795769] · 10⁹      3.796 · 10⁹
    12   4.129317080… · 10¹²                   [4.214048, 4.214053] · 10¹⁰     4.215 · 10¹⁰
    13   [6.690168788, 6.690169106] · 10¹³     [4.551631, 4.551637] · 10¹¹     4.552 · 10¹¹
    14   1.157013734… · 10¹⁵                   [5.247800, 5.247806] · 10¹²     5.248 · 10¹²   {#eq:envelope-derivatives}

where a bracket is an enclosure and a value ending in … is truncated.

*Proof.* Since env^(k)(v) = c (2/3)^k β^(k)((2v − 4)/3), e_k = c (2/3)^k S_k. β is even and vanishes with all its
derivatives on |y| ≥ 1 ([[lem:envelope-constant]] (a)), so |β^(k)| is even and S_k is its supremum over [0, 1); and
S_0 = β(0) = 1, since 0 ≤ β ≤ 1. The rest of the proof has five steps.

*Step 1: the Taylor coefficients.* For 0 ≤ m < 1 let β_n(m) := β^(n)(m)/n!, and let γ_i(m) and ψ_j(m) be the Taylor
coefficients at m of cos¹²(πy/2) and of ψ(y) := exp(−y²/(1 − y²)). Then β_n = Σ_(i=0)^n γ_i ψ_(n−i), with

    γ_0(m) = 2⁻¹² (924 + 2 Σ_(l=1)^6 C(12, 6 − l) cos(lπm)),
    γ_i(m) = 2⁻¹¹ Σ_(l=1)^6 C(12, 6 − l) (lπ)^i cos(lπm + iπ/2)/i!   (i ≥ 1),
    ψ_0(m) = exp(−m²/(1 − m²)),
    (n + 1) q_0 ψ_(n+1)(m) = −2m ψ_n(m) − 2ψ_(n−1)(m) − Σ_(i=1)^4 (n + 1 − i) q_i ψ_(n+1−i)(m), n ≥ 0, {#eq:taylor-beta}

where C(12, 5), …, C(12, 0) = 792, 495, 220, 66, 12, 1, ψ_j := 0 for j < 0, p := 1 − m², and q_0 = p², q_1 = −4mp,
q_2 = 4m² − 2p, q_3 = 4m, q_4 = 1. Indeed cos¹²x = 2⁻¹² (924 + 2 Σ_l C(12, 6 − l) cos 2lx), by the binomial expansion
of ((e^(ix) + e^(−ix))/2)¹², and cos(lπ(m + t)) = Σ_i (lπ)^i cos(lπm + iπ/2) t^i/i!. The function ψ satisfies
(1 − y²)² ψ' = −2y ψ on (−1, 1), and (1 − (m + t)²)² = Σ_(i=0)^4 q_i t^i; comparing the coefficients of t^n in this
equation at y = m + t gives the recursion. So each β_n(m) is a finite expression in exp(−m²/(1 − m²)), cos(lπm) and
sin(lπm) (l ≤ 6), π and rationals. At m = 0 the odd coefficients vanish, γ_0(0) = 1,

    γ_(2i)(0) = (−1)^i π^(2i) (792 + 495 · 4^i + 220 · 9^i + 66 · 16^i + 12 · 25^i + 36^i)/(2¹¹ (2i)!)   (i ≥ 1),

and ψ_(2j)(0) = L_j := Σ_(r=1)^j (−1)^r C(j − 1, r − 1)/r! for j ≥ 1, L_0 = 1, since exp(−w/(1 − w)) =
Σ_r (−w)^r (1 − w)^(−r)/r! with w = y². Hence β^(2j)(0) = (2j)! Σ_(i=0)^j γ_(2i)(0) L_(j−i), which is [[eq:beta-even]];
for instance L_1 = −1, γ_2(0) = −(3/2)π², and β''(0) = 2(γ_2(0) + L_1) = −2 − 3π². The entries of
[[sec:envelope-table-nodes]] are the values of [[eq:taylor-beta]] at thirty nodes m, for n ≤ 30.

*Step 2: Cauchy's inequality.* Let 0 < ρ < 1 − m. The closed disc D(m, ρ) ⊂ ℂ avoids ±1, β(ζ) = cos¹²(πζ/2)
exp(1 − 1/(1 − ζ²)) is holomorphic near it, and |β| ≤ M(m, ρ) on it, where

    M(m, ρ) := (cos²((π/2) max(m − ρ, 0)) + sinh²(πρ/2))⁶ exp(1 − (1/2)(1/(1 − m + ρ) + 1/(1 + m + ρ))).   {#eq:cauchy-m}

Indeed, for ζ = a' + i b' in D(m, ρ), |cos(πζ/2)|² = cos²(πa'/2) + sinh²(πb'/2) with |b'| ≤ ρ and a' ∈ [m − ρ, m + ρ] ⊂
(−1, 1), on which cos²(πa'/2) is largest at the point nearest 0. Next, 1/(1 − ζ²) = (1/2)(1/(1 − ζ) + 1/(1 + ζ)), where
1 − ζ and 1 + ζ lie in the closed discs of radius ρ about 1 − m and 1 + m; and w ↦ 1/w maps the closed disc of radius
ρ about p > ρ onto the disc with real diameter [1/(p + ρ), 1/(p − ρ)]. So Re 1/(1 − ζ²) ≥ (1/2)(1/(1 − m + ρ) +
1/(1 + m + ρ)), and |exp(1 − 1/(1 − ζ²))| = exp(1 − Re 1/(1 − ζ²)). By Cauchy's inequality, |β_n(m)| ≤ M(m, ρ) ρ^(−n)
for every n.

*Step 3: the cells.* Let 0 < h < ρ < 1 − m and x := h/ρ. The Taylor series of β at m converges on D(m, ρ), so
β^(k)(m + t) = k! Σ_(n≥k) C(n, k) β_n(m) t^(n−k) for |t| ≤ h. Bounding the terms with n ≤ 30 by their absolute values
and those with n > 30 by Step 2, and using Σ_(n≥k) C(n, k) x^(n−k) = (1 − x)^(−k−1),

    sup_(|t|≤h) |β^(k)(m + t)| ≤ Γ_k := k! (Σ_(n=k)^30 C(n, k) |β_n(m)| h^(n−k)
                       + M(m, ρ) ρ^(−k) ((1 − x)^(−k−1) − Σ_(n=k)^30 C(n, k) x^(n−k))).                 {#eq:cell-bound}

[[sec:envelope-table-cells]] lists twenty-three cells [m − h, m + h] ∩ [0, 1) whose union is [0, 0.984], with their Γ_k.

*Step 4: the peak intervals.* Fix k and the data m_k, h_k < ρ_k of [[sec:envelope-table-peaks]], let x := h_k/ρ_k,
M_k := M(m_k, ρ_k), and write u, u′, u″ for the values of β^(k), β^(k+1), β^(k+2) at m_k. The argument of Step 3
applied to β^(k+2), with its constant term left out, gives for |t| ≤ h_k

    |β^(k+2)(m_k + t) − u″| ≤ R_k := (k + 2)! (Σ_(n=k+3)^30 C(n, k + 2) |β_n(m_k)| h_k^(n−k−2)
                    + M_k ρ_k^(−k−2) ((1 − x)^(−k−3) − Σ_(n=k+2)^30 C(n, k + 2) x^(n−k−2))).         {#eq:peak-remainder}

Let σ be the sign of u. [[sec:envelope-table-peaks]] shows σu″ < 0 and ν_k = |u″| − R_k > 0; so σβ^(k+2) ≤ −ν_k
and |β^(k+2)| ≤ G_k on J_k = [m_k − h_k, m_k + h_k] ∩ [0, 1). By Taylor's formula with integral remainder, for |t| ≤ h_k,

    σβ^(k)(m_k + t) ≤ |u| + σu′t − ν_k t²/2 ≤ |u| + u′²/(2ν_k),     σβ^(k)(m_k + t) ≥ |u| − |u′| h_k − G_k h_k²/2 = w_k,

and that table shows w_k > −|u|. So |β^(k)| ≤ |u| + u′²/(2ν_k) on J_k, and |β^(k)(m_k)| = |u|. For even k, m_k = 0 and
u′ = β^(k+1)(0) = 0, so the supremum of |β^(k)| over J_k is exactly |β^(k)(0)|.

*Step 5: the end.* Let 0.984 ≤ y < 1, t := 1 − y ≤ 0.016 and 0 < ρ < t. On D(y, ρ), 1 − ζ lies in the disc of radius ρ
about t, so Re 1/(1 − ζ) ≥ 1/(t + ρ) > 1/(2t), and 1 + ζ in the disc of radius ρ < t about 2 − t, so Re 1/(1 + ζ) ≥
1/2; hence |exp(1 − 1/(1 − ζ²))| ≤ e^(3/4 − 1/(4t)). Also Re ζ ∈ (1 − 2t, 1) ⊂ [1/3, 1], so cos²(π Re ζ/2) ≤
sin²(πt) ≤ π²t², and |Im ζ| < t ≤ 1/3, so, sinh s/s being increasing, sinh²(π Im ζ/2) ≤ (πt/2)² (sinh(π/6)/(π/6))² ≤
1.0948 (πt/2)². So |cos(πζ/2)|² ≤ π²t² (1 + 1.0948/4) < 12.58 t², and Cauchy's estimate with ρ → t gives

    |β^(k)(y)| ≤ k! 12.58⁶ e^(3/4) t^(12−k) e^(−1/(4t)).

For k ≤ 14, t^(12−k) e^(−1/(4t)) increases on (0, 1/8], so on [0.984, 1) the bound is at most k! 12.58⁶ e^(3/4)
(0.016)^(12−k) e^(−15.625). This is below 4.68 · 10¹⁴ < 0.41 S_14⁻ at k = 14, below 5.35 · 10¹¹ < 0.008 S_13⁻ at
k = 13, and below 2 · 10⁻⁴ S_k⁻ for k ≤ 12, with S_k⁻ the lower ends of [[sec:envelope-table-peaks]].

*Conclusion.* For each k, every cell of [[sec:envelope-table-cells]] either lies in J_k or has Γ_k < S_k⁻ ≤ |u|, and
the cells cover [0, 0.984]. With Steps 4 and 5, S_k is the supremum of |β^(k)| over J_k, which lies between |u| and
|u| + u′²/(2ν_k), and equals |β^(k)(0)| for even k. This is (a) and (b); the enclosures [S_k⁻, S_k⁺] of
[[sec:envelope-table-peaks]] and the bounds on c give (c). ∎

A reader checks this proof row by row: each entry of [[sec:envelope-table-nodes]] from [[eq:taylor-beta]] (one
exponential and twelve trigonometric values per node, then the recursion and a convolution); each Γ_k of
[[sec:envelope-table-cells]] from [[eq:cell-bound]] with the entries of that cell's node and the value of
[[eq:cauchy-m]]; each line of [[sec:envelope-table-peaks]] from [[eq:peak-remainder]]; and the comparisons Γ_k < S_k⁻,
σu″ < 0, ν_k > 0 and w_k > −|u_k|, which are comparisons of printed decimals. The closest comparison is Γ_14 =
1.143 · 10¹⁵ on [0.175, 0.205] against S_14⁻ = 1.157013733 · 10¹⁵. For even k the value S_k itself is checked from
[[eq:beta-even]] alone.

**Remark {#rem:envelope-dependence}** (Which end of c each bound uses.) The two ends of [[eq:envelope-c]] enter different
bounds. (i) The lower end enters every bound on λ0 at the numerical point that rests on the size of the wave: at the
point v = 2, r = a, ϑ = 0, θ = 0 of Ω × S¹ the operator norm of W_TT is (4/3) c a^(−3/2) ([[prop:stage-zero-bounds]]),
every admissible C_app is at least this, whatever the mean m1 ([[prop:lambda0-norms]]), and by [[lem:lambda0-point]]
(a), a^(−3/2) > 7.133376, so

    (4/3) c a^(−3/2) ≥ (4/3) · 1.3240711 · 7.133376 > 12.593309.

This uses c ≥ 1.3240711 and nothing else about c; with any proven lower bound c_− in its place the constant is
(4/3) c_− a^(−3/2). Combined with ε1 < s0 < 0.030768560 ([[lem:epsilon-one]]), the quotient of the two is
0.030768560/12.593309 < 0.0024433, which is the operator-norm bound of [[prop:lambda0]]; that bound therefore holds
exactly as far as the lower end of c does. The Frobenius and largest-entry bounds 0.0019079 and 0.0012228 use the
lower end in the same way, and no other property of c ([[rem:lambda0-norms-c]]). (ii) The upper end enters through
env ≤ c: in [[lem:lambda0-point]] (c), where any c < 3 suffices; in the range 0 ≤ μ' ≤ (2/9) c² used in
[[prop:energy-constant]]; and in the bound 1 + c²/18 ≤ 1.0974028 used for the threshold of [[thm:layer]], which needs
c ≤ 1.3241035. The bounds e_k of [[lem:envelope-derivatives]] use both ends.

### The admissible range of ε1 {#sec:epsilon-one}

**Lemma {#lem:epsilon-one}** (ε1 at the numerical point.) At the numerical point:

(a) μ0/a² − 1 > 12, so the standing condition 0 < ε1 < min(s0, μ0/a² − 1) of [[sec:profiles]] reads 0 < ε1 < s0;

(b) the least value of (3 + μ/r²)/5 on the outer boundary of Ω is λ_out := (3 + μ_end/b(τ0)²)/5, taken at τ = τ0,
and 0.6013095 < λ_out < 0.6013096. For every ε1 < λ_out the restrictions of [[lem:eigen]] stay positive definite for
every symmetric g with |g − g0| ≤ ε1. The metric

    g̃ := g0 − λ_out e ⊗ e,        e := 5^(−1/2) (−1, 2 x̂)  (Euclidean components),

is Lorentzian on Ω with |g̃ − g0| = λ_out, and the outer boundary is null for g̃ at its corner τ = τ0; so
[[lem:domain]] (e) fails for every ε1 ≥ λ_out;

(c) s0 = (m*² + 1)^(1/2) − m* satisfies 0.030768559 < s0 < 0.030768560. Hence every admissible ε1 is below
0.030768560.

*Proof.* (a) μ0/a² > 13 by [[lem:lambda0-point]] (a).

(b) By [[lem:lambda0-point]] (e), (3 + μ/r²)/5 ≥ (3 + μ_end/b(τ0)²)/5 on the outer boundary, with equality at τ = τ0.
From b(τ0) ∈ (13.437207, 13.437209), 1.182291 < μ_end < 1.182292 and 13.437207² > 180.5585, 13.437209² < 180.5587,
one gets 0.0065479 < μ_end/b(τ0)² < 0.0065480 and the bounds on λ_out. By [[lem:eigen]] the least eigenvalues of the
three restrictions are 1 on ker dτ, min(1, μ/a² − 1) = 1 on ker dr at r = a (by (a)), and min(1, (3 + μ/r²)/5) ≥ λ_out
on the outer boundary; a symmetric perturbation of operator norm at most ε1 < λ_out lowers each by at most ε1.

The vector e is a unit vector of ker d(v + τ) = ker(2dτ + dr): with T = −1/√5 and X = (2/√5) x̂ one has 2T + x̂·X = 0.
In the notation of the proof of [[lem:eigen]] it is the direction X⊥ = 0, s = 2/√5, on which g0(e, e) = (3 + μ/r²)/5.
Since e ⊗ e has rank one and |e| = 1, |g̃ − g0| = λ_out. On ker dτ, g̃ = |X|² + (μ/r²)(x̂·X)² − (4λ_out/5)(x̂·X)² ≥
(1 − 4λ_out/5)|X|², positive definite. By the determinant formula for a rank-one change, det g̃ = det g0 ·
(1 − λ_out e·g0⁻¹e), where det g0 = −1 and, with g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0, L0 = (1, −x̂),

    e·η⁻¹e = −1/5 + 4/5 = 3/5,     L0·e = −3/√5,     e·g0⁻¹e = (3 − 9μ/r²)/5.

So det g̃ = −(1 − λ_out (3 − 9μ/r²)/5) ≤ −(1 − 3λ_out/5) < 0. A symmetric form that is positive definite on a
four-dimensional subspace has at most one non-positive eigenvalue, and a negative determinant then forces exactly one
negative eigenvalue and no zero one: g̃ is Lorentzian. At the corner τ = τ0, r = b(τ0), where μ/r² = μ_end/b(τ0)², the
restriction of g0 to ker d(v + τ) has the eigenvalues 1, 1, 1 and λ_out relative to the Euclidean product, the last on
e; so the restriction of g̃ has the eigenvalues 1, 1, 1, 0. The tangent space of the outer boundary there is a null
hyperplane of g̃, the boundary is not spacelike for g̃, and [[lem:domain]] (e) fails for ε1 = λ_out and every larger ε1.

(c) The map m ↦ (m² + 1)^(1/2) − m is decreasing, with inverse s ↦ (1 − s²)/(2s). By [[lem:lambda0-point]] (d) and
the paragraph on s0 after [[lem:eigen]], s0 = (m*² + 1)^(1/2) − m*. Now (1 − x²)/(2x) at x = 0.030768559 exceeds
16.2349705 > m*, and at x = 0.030768560 is below 16.2349700 < m*; this gives the two bounds. ∎

### The energy constant of g0 on Ω {#sec:energy-constant}

Let u, a function or a Cartesian array, satisfy −(1/2) □̃u = f on Ω, with □̃ = g0^(ab) ∂_a ∂_b componentwise. Put
Y := −g0⁻¹ dτ, T_ab := ∂_a u ∂_b u − (1/2)(g0)_ab g0⁻¹(du, du) summed over components, and E(τ) := ∫_(Σ_τ) T(Y, Y) dx.
|du|² is the Euclidean sum of the squares of all first coordinate derivatives.

**Proposition {#prop:energy-constant}** (The energy constant at the numerical point.) Put q_lo := 0.2647,
q_hi := 280.545 and κ := 12. On Ω:

(a) q_lo |du|² ≤ T(Y, Y) ≤ q_hi |du|²;

(b) (Yu)² ≤ 2 T(Y, Y), and the constant 2 is attained;

(c) |𝔅| ≤ κ T(Y, Y) pointwise, for the bulk form 𝔅 of [[eq:energy-bulk]] below, and dE/dτ ≤ κ E + 2√2 ‖f‖ E^(1/2);

(d) for τ ∈ [τ0, τ_end],

    ‖du(τ)‖ ≤ (q_hi/q_lo)^(1/2) e^(κ(τ−τ0)/2) ‖du(τ0)‖ + √2 q_lo^(−1/2) e^(κ(τ−τ0)/2) ∫_(τ0)^τ ‖f(s)‖ ds
            ≤ 9.7 · 10¹⁶ ‖du(τ0)‖ + 8.2 · 10¹⁵ ∫_(τ0)^τ ‖f(s)‖ ds.                              {#eq:energy-constant}

The same holds with the larger rate κ = 13.2197 and the smaller q_lo = 0.196683, which give e^(κ(τ_end−τ0)/2) <
e^(39.24407) < 1.10531 · 10¹⁷ and the coefficients 4.18 · 10¹⁸ and 3.525 · 10¹⁷ in [[eq:energy-constant]].

*Proof.* *Coordinates.* By the O(4) invariance work at a point with x̂ = e1, in the coordinates (τ, r, ω) in which
g0 = −dτ² + dr² + r² γ + m (dτ + dr)², m := μ(v)/r², and put k := μ'(v)/r ≥ 0. The (τ, r) block of g0 is
[[−1 + m, m], [m, 1 + m]], of determinant −1, with inverse [[−1 − m, m], [m, 1 − m]], so Y = (1 + m) ∂_τ − m ∂_r and
g0(Y, Y) = −(1 + m). Since ∂_τ m = k/r and ∂_r m = (k − 2m)/r, Y(m) = (k + 2m²)/r.

*The deformation tensor.* With π := 𝓛_Y g0, π_ab = Y(g_ab) + g_cb ∂_a Y^c + g_ac ∂_b Y^c, one finds

    r π_ττ = 2m² − k,     r π_τr = 2m² + 2m − k,     r π_rr = 2m² + 4m − k,     π_AB = −2 m r γ_AB,

and g0^(ab) π_ab = 2 div Y = −2m/r (in Cartesian components div Y = ∂_τ m + ∂_i(−m x^i/r) = k/r − (k − 2m)/r − 3m/r).
For example π_ττ = Y(m) + 2((−1 + m) ∂_τ(1 + m) + m ∂_τ(−m)) = (k + 2m²)/r − 2k/r.

*The identity.* Since det g0 = −1 in Cartesian coordinates, the current J^a := T^a_b Y^b has ∂_a J^a = (□_(g0) u)(Yu)
+ (1/2) π^(ab) T_ab, and □_(g0) u = □̃u − H0^c ∂_c u = □̃u + (m/r) L0 u by [[prop:vaidya]] (f). J^τ = −T(Y, Y). The
flux argument in the proof of [[lem:energy]] (the lateral boundaries spacelike with Ω to their past, their fluxes
nonnegative and dropped) gives dE/dτ ≤ ∫_(Σ_τ) (2 f · Yu + 𝔅) dx with

    𝔅 := −(m/r)(L0 u)(Yu) − (1/2) π^(ab) T_ab.                                                     {#eq:energy-bulk}

*The two forms.* Write p = ∂_τ u, q = ∂_r u, w² for the angular part of |du|², and A := Yu = (1 + m) p − m q,
B := mp + (1 − m) q, the r-component of g0⁻¹ du. The map (p, q) ↦ (A, B) has determinant 1, L0 u = A − B,
g0⁻¹(du, du) = −(1 − m) A² − 2m AB + (1 + m) B² + w², and π^(ab) ∂_a u ∂_b u = π_ττ A² − 2π_τr AB + π_rr B²
− (2m/r) w². Substituting,

    2 T(Y, Y) = (1 + m²) A² − 2m(1 + m) AB + (1 + m)² B² + (1 + m) w²
              = (1 + m)² p² − 2m(1 + m) pq + (1 + m²) q² + (1 + m) w²,
    2r 𝔅     = (k − m − 3m²) A² + 2(3m + 3m² − k) AB + (k − 5m − 3m²) B² + m w².

(a) The (p, q) block of 2T(Y, Y) has trace 2(m² + m + 1) and determinant (1 + m)², so T(Y, Y) has the Euclidean
eigenvalues ν± = (m² + m + 1 ± m (m² + 2m + 2)^(1/2))/2 and (1 + m)/2 ∈ [1/2, 9). Here ν₊ increases in m, and
ν₋ = (1 + m)²/(4 ν₊) = 1/(2φ(z)) with z := 1/(1 + m) and φ(z) = 1 − z + z² + (1 − z)(1 + z²)^(1/2); one has
φ'(z) < 0 on (0, 1], because (2z − 1)(1 + z²)^(1/2) < 1 − z + 2z² (trivially if 2z ≤ 1, and otherwise by squaring,
the difference of the squares being 2z). So ν₋ decreases in m. By [[lem:lambda0-point]] (d), m ≤ m* < 16.234971, and
at m = 16.234971 one has ν₊ < 280.5447 and ν₋ > 0.26470; so every eigenvalue lies in [q_lo, q_hi].

(b) For a covector ξ write ξ = α g0(Y, ·) + ξ' with ξ'(Y) = 0; ξ' is g0-orthogonal to the timelike Y, so
g0⁻¹(ξ', ξ') ≥ 0, and g0⁻¹(ξ, ξ) ≥ α² g0(Y, Y) = −ξ(Y)²/(1 + m). Hence T(Y, Y) = (Yu)² + ((1 + m)/2) g0⁻¹(du, du)
≥ (Yu)²/2, with equality when du is proportional to g0(Y, ·).

(c) In (A, B) the generalized eigenvalues λ of the block of 2r𝔅 relative to that of 2T(Y, Y) solve
(1 + m)² λ² − 2wλ − 4m² = 0 with w := k − m² − 3m, that is

    λ± = (w ± (w² + 4m²(1 + m)²)^(1/2))/(1 + m)²,

and on the angular part the ratio of 2r𝔅 to 2T(Y, Y) is m/(1 + m) < 1. So |𝔅| ≤ r⁻¹ max(|λ₊|, |λ₋|, 1) T(Y, Y).
On Ω, k ≤ (2/9) c²/r < 0.39/r by [[lem:envelope-constant]]. If w ≤ 0, then |w| ≤ m² + 3m and λ₊ ≤ 2m/(1 + m) < 2,
while

    |λ₋| ≤ m (m + 3 + (5m² + 14m + 13)^(1/2))/(1 + m)² < 1 + √5,

since m(5m² + 14m + 13)^(1/2) < √5 m² + (2√5 − 1) m + 1 + √5: the square of the right side is 5m⁴ + (20 − 2√5) m³ +
(31 − 2√5) m² + … with positive remaining terms, and 20 − 2√5 > 14, 31 − 2√5 > 13. If w > 0, then k > 3m ≥ 3μ0/r², so
r > 3/0.39 > 7.6, and |λ±| ≤ (2w + 2m(1 + m))/(1 + m)² ≤ 2k + 2 < 2.2. Hence |𝔅| ≤ ((1 + √5)/a) T(Y, Y), and
(1 + √5)/a < 3.23607/0.2698587 < 12. With (b) and the Cauchy–Schwarz inequality, ∫ 2 |f| |Yu| ≤ 2√2 ‖f‖ E^(1/2).

(d) For y := E^(1/2), (c) gives y' ≤ (κ/2) y + √2 ‖f‖, so y(τ) ≤ e^(κ(τ−τ0)/2)(y(τ0) + √2 ∫ ‖f‖) by Gronwall's
inequality, and (a) converts y to ‖du‖. With τ_end − τ0 < 5.937209 ([[lem:lambda0-point]] (c)),
e^(6 · 5.937209) < 2.958 · 10¹⁵, (q_hi/q_lo)^(1/2) < 32.56 and (2/q_lo)^(1/2) < 2.749, which gives the numbers in
[[eq:energy-constant]]. Since κ = 12 < 13.2197 and q_lo > 0.196683, the weaker constants follow too:
13.2197 · 5.937209/2 < 39.24407, e^(39.24407) < 1.10531 · 10¹⁷, (280.545/0.196683)^(1/2) < 37.77 and
(2/0.196683)^(1/2) < 3.18884. ∎

**Remark {#rem:energy-one-sided}** (A one-sided rate.) Only the upper bound 𝔅 ≤ r⁻¹ max(λ₊, 1) T(Y, Y) enters the
differential inequality, and λ₊ < 2 where w ≤ 0. So κ in (c) and (d) may be replaced by 2/a < 7.42.

### The profiles of stage 0 {#sec:stage-zero-bounds}

The wave W_TT and the second harmonic χ are those of [[lem:stage-zero]] and [[eq:chi-transport]], with
q := cos 2ϑ = c² − s² (here c², s² are the angular functions of [[sec:waves]], not the envelope constant) and
h² = 2/(1 + q²). Norms of tensors are Euclidean, of Cartesian components.

**Lemma {#lem:chi-closed-form}** (The second harmonic.) On Ω × S¹,

    χ = −(1/12) A² env(v)² h² (4q sin 2θ + (1 − q²) cos 2θ) (r⁻² − (v − τ0)^(−1/2) r^(−3/2)).

*Proof.* With ∂_θ y1 = −(α/3) a1, ∂_θ y2 = (α/3) a2, a1 := 2c² sin θ + s² cos θ, a2 := 2s² cos θ + c² sin θ, one has
a1² − a1 a2 + a2² = 3(c⁴ sin² θ + s⁴ cos² θ + c² s² sin θ cos θ). With sin² θ = (1 − cos 2θ)/2, cos² θ =
(1 + cos 2θ)/2, c⁴ − s⁴ = q and c² s² = (1 − q²)/4, the definition of F_2 after [[lem:stage-zero]] becomes

    F_2 = (α²/3)((c⁴ − s⁴) cos 2θ − c² s² sin 2θ) = (α²/12)(4q cos 2θ − (1 − q²) sin 2θ),   α² = A² env² h² r⁻³.

Along ℓ = ∂_r at fixed (v, ϑ, φ1, φ2), the transport (∂_r + 3/(2r)) Z = r⁻³ K, K independent of r, with Z = 0 at
r = v − τ0 (that is, on Σ_τ0), has the solution Z = −2K (r⁻² − (v − τ0)^(−1/2) r^(−3/2)), since (r^(3/2) Z)' =
r^(−3/2) K. The θ-primitive of 4q cos 2θ − (1 − q²) sin 2θ with zero mean is (1/2)(4q sin 2θ + (1 − q²) cos 2θ). ∎

**Proposition {#prop:stage-zero-bounds}** (Stage 0 at the numerical point.) On Ω × S¹,

    |W_TT| ≤ (4/3) A env(v) r^(−3/2) ≤ (4/3) c a^(−3/2) < 12.5937,      |W_TT|_F ≤ (2√6/3) c a^(−3/2) < 15.4241,
    |χ| ≤ A² env(v)²/(3r²) ≤ c²/(3a²) < 8.025,                          |χ dv ⊗ dv|_F = 2|χ| < 16.05,

with |·| the operator norm and |·|_F the Frobenius norm. The first bound is attained at v = 2, r = a, ϑ = 0, θ = 0,
where |W_TT| = (4/3) c a^(−3/2) > 12.5934 and |W_TT|_F = (2√6/3) c a^(−3/2).

*Proof.* W_TT has only angular components, and r⁻¹ ∂_ϑ, (rc)⁻¹ ∂_φ1, (rs)⁻¹ ∂_φ2 are Euclidean-orthonormal and
orthogonal to ∂_τ and ∂_r; so off the axes the eigenvalues of W_TT are 0, 0, −2(y1 + y2), 2y1, 2y2, and the bounds
below extend to the axes by continuity. With α = A env h r^(−3/2),

    2|y1| ≤ (2α/3)(4c⁴ + s⁴)^(1/2),   2|y2| ≤ (2α/3)(4s⁴ + c⁴)^(1/2),   2|y1 + y2| ≤ (2α/3)(c⁴ + s⁴)^(1/2),

and h²(4c⁴ + s⁴) = 5/2 + 3q/(1 + q²) ≤ 4, h²(4s⁴ + c⁴) = 5/2 − 3q/(1 + q²) ≤ 4, h²(c⁴ + s⁴) = 1. This gives the
operator bound, with equality at q = 1, θ = 0. For the Frobenius norm, (y1 + y2)² + y1² + y2² = (2α²/3)(c⁴ cos² θ −
c² s² sin θ cos θ + s⁴ sin² θ), and the largest eigenvalue of this form in (cos θ, sin θ) is
((c⁴ + s⁴) + ((c⁴ − s⁴)² + c⁴ s⁴)^(1/2))/2 = ((1 + q²)/2 + (q² + (1 − q²)²/16)^(1/2))/2 ≤ (1 + q²)/2 = h⁻², the last
step being 16q² + (1 − q²)² ≤ 4(1 + q²)², that is 0 ≤ 3(1 − q²)². So |W_TT|_F² ≤ (8/3) A² env² r⁻³. For χ,
h²|4q sin 2θ + (1 − q²) cos 2θ| ≤ h²(16q² + (1 − q²)²)^(1/2) = 2(1 + 12q²/(1 + q²)²)^(1/2) ≤ 4, and on Ω,
0 ≤ (v − τ0)^(−1/2) r^(−3/2) ≤ r⁻² because r ≤ v − τ0; so |χ| ≤ A² env²/(3r²) by [[lem:chi-closed-form]]. The
Euclidean norm of dv = dτ + x̂·dx is √2, so |χ dv ⊗ dv|_F = 2|χ|. The numbers follow from c < 1.3240879 and
a > 0.2698587885 ([[lem:envelope-constant]], [[lem:lambda0-point]]): a^(−3/2) < 7.1333767 and a⁻² < 13.73179; and
from c > 1.3240867, a^(−3/2) > 7.133376 at the point of equality. ∎

### The mean forcing term of stage 1 {#sec:stage-one-source}

At stage 1 the mean equation (a) of [[eq:stage-system]] has the right-hand side 𝒮_1 = −⟨𝒦_1⟩, and by
[[lem:first-entry]] 𝒦_1 depends on g0, v and W alone. Setting every unknown of the stages m ≥ 1 to zero in
[[eq:stage-m]] at m = 1 removes T̂ ĝ2 and 𝒲(m1, φ1), makes e2 vanish (q2 vanishes with m1 and dφ1), and leaves
G = g0 + λW and u = v. So 𝒦_1 is the coefficient R^(1) of λ in the two-scale expansion [[eq:two-scale-expansion]] of
R[g0 + λW], and 𝒮_1 = −⟨R^(1)⟩. In this section and the next, c² = cos² ϑ and s² = sin² ϑ are the angular functions of
[[sec:waves]] and q = c² − s² = cos 2ϑ, as in [[sec:stage-zero-bounds]].

**Lemma {#lem:stage-one-source}** (The mean forcing term of stage 1.) Let g0 be built on any smooth mass function μ,
let χ be a smooth function on Ω × S¹ that is, at each X, a combination of cos 2θ and sin 2θ, put W := W_TT + χ dv ⊗ dv,
and let R^(1) be the coefficient of λ in the two-scale expansion of R[g0 + λW]. Then

    ⟨R^(1)⟩ = S := −(4/9) A² env(v)² h² sin 2ϑ r⁻³ (dv ⊗ dϑ + dϑ ⊗ dv).                            {#eq:stage-one-source}

The function χ of [[eq:chi-transport]] is of this kind ([[lem:chi-closed-form]]); so at stage 1 of [[lem:stage-system]]
the mean equation has the right-hand side 𝒮_1 = −S, whatever the data of the stages.

*Proof.* We use the notation of the proof of [[lem:leading-coefficient]]: ∂ := ∂_θ, v_a := ∂_a v, indices are moved with
g0, ℓ^a = g0^(ab) v_b, ∇ is the Levi-Civita connection of g0 acting at fixed θ, and C_0, C_1 and D_1 are the profiles
defined there. Put K_ab := ∇_a ∇_b v. Since g0⁻¹(dv, dv) = 0 identically, 0 = ∇_a (ℓ^b v_b) = 2 ℓ^b K_ab; so
K(ℓ, ·) = 0, ∇_ℓ ℓ = 0 and ∇_ℓ dv = 0. Write W = W_TT + Y with Y := χ dv ⊗ dv. By [[lem:stage-zero]] (a), W_TT, Y and
their θ-derivatives vanish on ℓ and have g0-trace zero, and so does W; and Y^(cd) = χ ℓ^c ℓ^d.

*The coefficient of λ.* With h = λW one has C := Γ[g] − Γ[g0] = C_0 + λ C_1 + λ² C_2 + O(λ³) and
D = λ D_1 + λ² D_2 + O(λ³), C_2 and D_2 being profiles. In Ric(g) − Ric(g0) = ∇^v_c C^c_ab − ∇^v_b C^c_ac +
C^c_cd C^d_ab − C^c_bd C^d_ac, where ∇^v = ∇ + λ⁻¹ v ⊗ ∂, the coefficient of λ is

    ∇_c C_1^c_ab + v_c ∂C_2^c_ab − ∇_b C_1^c_ac − v_b ∂C_2^c_ac + C_0^c_cd C_1^d_ab + C_1^c_cd C_0^d_ab
        − C_0^c_bd C_1^d_ac − C_1^c_bd C_0^d_ac,

and in the gauge term (1/2)(g_mρ ∇^v_n D^ρ + g_nρ ∇^v_m D^ρ), with g = g0 + λW, it is

    (1/2)(v_n W_mρ ∂D_1^ρ + (g0)_mρ (∇_n D_1^ρ + v_n ∂D_2^ρ)) + (the same with m and n exchanged).

*Terms of mean zero.* The θ-mean of a θ-derivative vanishes, and ⟨·⟩ commutes with ∇ and with multiplication by
functions of X. W_TT is a combination of cos θ and sin θ and Y one of cos 2θ and sin 2θ, so ⟨W⟩ = 0 and every term
linear in W has mean zero; the terms with ∂C_2 and ∂D_2 are θ-derivatives. The proof of [[lem:leading-coefficient]]
gives C_0^c_cd = 0 and C_1^c_ac = −(1/2) v_a W·∂W, where W·∂W = W^(cd) ∂W_cd = (1/2) ∂(W^(cd) W_cd) is a θ-derivative;
so ∇_b C_1^c_ac has mean zero, and C_0^c_cd C_1^d_ab + C_1^c_cd C_0^d_ab = −(1/2)(W·∂W) v_d C_0^d_ab = 0, because
v_d C_0^d_ab = (1/2)(v_a v_d ∂W_b^d + v_b v_d ∂W_a^d − v_d ℓ^d ∂W_ab) = 0. In the gauge term D_1 = div W +
(1/2) ℓ W·∂W; the part (1/2) ℓ^ρ W·∂W is a θ-derivative in ∇_n D_1 and is annihilated by W_mρ ℓ^ρ = 0, and div W is
linear. Since W^(cd) v_d = 0, the part of C_1 quadratic in W is C_Q^c_ab := −(1/2)(v_a W^(cd) ∂W_bd + v_b W^(cd)
∂W_ad). Put P_ab := C_0^c_bd C_1^d_ac; then C_1^c_bd C_0^d_ac = P_ba. Hence

    ⟨R^(1)⟩_ab = ∇_c ⟨C_Q^c_ab⟩ − ⟨P_ab + P_ba⟩ − (1/2)(v_b ⟨W_aρ ∂(div W)^ρ⟩ + v_a ⟨W_bρ ∂(div W)^ρ⟩).     {#eq:mean-r1}

*The first term vanishes.* Off the axes the vectors e_ϑ := r⁻¹ ∂_ϑ, e_1 := (rc)⁻¹ ∂_φ1, e_2 := (rs)⁻¹ ∂_φ2 are
g0-orthonormal and g0-orthogonal to ∂_v and ∂_r ([[eq:eddington]]), and W_TT = Σ_i w_i e^i ⊗ e^i with e^i := g0(e_i, ·),
w_ϑ := −2(y1 + y2), w_1 := 2y1, w_2 := 2y2. So the frame components of W_TT^(cd) ∂(W_TT)_bd are w_i ∂w_i δ_ij =
(1/2) ∂(w_i²) δ_ij, of mean zero. The remaining parts of W^(cd) ∂W_bd vanish: W_TT^(cd) ∂Y_bd = ∂χ v_b W_TT^(cd) v_d = 0
and Y^(cd) ∂W_bd = χ ℓ^c ℓ^d ∂W_bd = 0. So ⟨C_Q⟩ = 0 off the axes, and everywhere by continuity.

*The second term.* Differentiating v_d W_c^d = 0 and ℓ^c W_cd = 0 gives v_d ∇_a W_c^d = −W_c^d K_ad and
ℓ^c ∇_a W_c^d = −W_c^d K_a^c; and ∇_c ℓ^d = K_c^d. Of the nine products in

    4 P_ab = (v_b ∂W_d^c + v_d ∂W_b^c − ℓ^c ∂W_bd)(∇_a W_c^d + ∇_c W_a^d − ∇^d W_ac),

the first is v_b ∂W:∇_a W, with ∂W:∇_a W := ∂W^(cd) ∇_a W_cd; v_b ∂W_d^c ∇_c W_a^d and −v_b ∂W_d^c ∇^d W_ac cancel
(exchange c and d); v_d ∂W_b^c ∇_a W_c^d = −∂W_b^c W_c^d K_da and −ℓ^c ∂W_bd ∇_a W_c^d = ∂W_bd W_c^d K_a^c cancel;
v_d ∂W_b^c ∇_c W_a^d = −∂W_b^c W_a^d K_cd and ℓ^c ∂W_bd ∇^d W_ac = −∂W_bd W_ac K^(dc) are equal; and
−v_d ∂W_b^c ∇^d W_ac and −ℓ^c ∂W_bd ∇_c W_a^d both equal −∂W_b^c (∇_ℓ W)_ca. So

    4 P_ab = v_b ∂W:∇_a W − 2 ∂W_bc K^(cd) W_da − 2 ∂W_b^c (∇_ℓ W)_ca.

Integrating by parts in θ, ⟨∂W_ac K^(cd) W_db⟩ = −⟨W_ac K^(cd) ∂W_db⟩ = −⟨∂W_bd K^(dc) W_ca⟩, so the K-terms of
P_ab + P_ba have mean zero. In the ∇_ℓ-terms Y contributes nothing: ∇_ℓ Y = ℓ(χ) dv ⊗ dv, ∂Y_a^c = ∂χ v_a ℓ^c, and
ℓ^c (∇_ℓ W_TT)_cb = −W_TT(∇_ℓ ℓ, ·)_b = 0, ∂(W_TT)_ac ℓ^c = 0 and v_c ℓ^c = 0. The angular components of W_TT are
r^(1/2) times functions of (v, ϑ, θ), so [[eq:transport-angular]] gives ∇_ℓ W_TT = −(3/(2r)) W_TT, and the ∇_ℓ-terms
of 4(P_ab + P_ba) are (3/r) ∂((W_TT)_a^c (W_TT)_cb), of mean zero. Likewise ∂W:∇_a W = ∂W_TT:∇_a W_TT, since
∂Y^(cd) ∇_a W_cd = ∂χ ℓ^c ℓ^d ∇_a W_cd = −2 ∂χ W_cd ℓ^c K_a^d = 0 and ∂W_TT^(cd) ∇_a Y_cd =
∂W_TT^(cd)(∂_a χ v_c v_d + χ K_ac v_d + χ v_c K_ad) = 0. Therefore

    ⟨P_ab + P_ba⟩ = (1/4)(v_b ⟨∂W_TT:∇_a W_TT⟩ + v_a ⟨∂W_TT:∇_b W_TT⟩).

*The third term.* ℓ^ρ (div W)_ρ = ∇^c (W_cρ ℓ^ρ) − W^(cρ) K_cρ = −W_TT^(cρ) K_cρ, because K(ℓ, ℓ) = 0. So
Y_aρ ∂(div W)^ρ = −χ v_a ∂(W_TT^(cρ) K_cρ) is the product of a combination of cos 2θ and sin 2θ with one of cos θ and
sin θ, and has mean zero. Further div Y = (ℓ(χ) + χ □_(g0) v) dv, since ∇_ℓ dv = 0, so W_aρ ∂(div Y)^ρ = 0. Hence
⟨W_aρ ∂(div W)^ρ⟩ = ⟨(W_TT)_aρ ∂(div W_TT)^ρ⟩, and [[eq:mean-r1]] becomes ⟨R^(1)⟩ = dv ⊗ X + X ⊗ dv with

    X_b := −(1/4) ⟨∂W_TT:∇_b W_TT⟩ − (1/2) ⟨(W_TT)_b^ρ ∂(div W_TT)_ρ⟩.

*Evaluation.* In the frame above ∂W_TT is diagonal with entries ∂w_i, and (∇_b W_TT)(e_i, e_i) = ∂_b w_i −
2 W_TT(∇_b e_i, e_i) = ∂_b w_i, since W_TT(·, e_i) = w_i g0(·, e_i) and g0(∇_b e_i, e_i) = 0. So ∂W_TT:∇_b W_TT =
Σ_i ∂w_i ∂_b w_i. Write w_i = (2α/3) P̂_i with α = A env(v) h r^(−3/2), a function of (v, r, ϑ), and

    P̂_ϑ := −(c² cos θ + s² sin θ),     P̂_1 := 2c² cos θ − s² sin θ,     P̂_2 := 2s² sin θ − c² cos θ.

For b ∈ {v, r, φ1, φ2}, ∂_b w_i = (∂_b α/α) w_i and ⟨w_i ∂w_i⟩ = 0. For b = ϑ the term with ∂_ϑ α again has mean zero,
and ⟨∂w_i ∂_ϑ w_i⟩ = (4α²/9) ⟨∂P̂_i ∂_ϑ P̂_i⟩, where

    ⟨∂P̂_1 ∂_ϑ P̂_1⟩ = ⟨(2c² sin θ + s² cos θ) 2cs (2 cos θ + sin θ)⟩ = 2cs,
    ⟨∂P̂_2 ∂_ϑ P̂_2⟩ = ⟨(2s² cos θ + c² sin θ) 2cs (2 sin θ + cos θ)⟩ = 2cs,
    ⟨∂P̂_ϑ ∂_ϑ P̂_ϑ⟩ = ⟨(c² sin θ − s² cos θ) 2cs (cos θ − sin θ)⟩ = −cs.

So ⟨∂W_TT:∇_ϑ W_TT⟩ = (4/3) α² cs, and the other components of ⟨∂W_TT:∇_b W_TT⟩ vanish.

For the divergence, the Christoffel symbols of [[eq:eddington]] satisfy Γ^B_(vr) = Γ^B_(rr) = Γ^B_(vC) = 0 and
Γ^B_(rC) = r⁻¹ δ^B_C for angular B, C, and on angular indices Γ^D_(BC) are those of the round metric
γ := dϑ² + c² dφ1² + s² dφ2². For a symmetric W' with only angular components and g0-trace zero it follows that
(div W')_v = −g0^(BC) Γ^D_(Cv) W'_BD = 0, (div W')_r = −g0^(BC) Γ^D_(Cr) W'_BD = −r⁻¹ tr W' = 0, and
(div W')_A = γ^(BC) 𝒟_C w'_BA, where w' := r⁻² W' and 𝒟 is the Levi-Civita connection of γ. The nonzero symbols of γ
are Γ^ϑ_(φ1φ1) = cs, Γ^ϑ_(φ2φ2) = −cs, Γ^(φ1)_(ϑφ1) = −s/c and Γ^(φ2)_(ϑφ2) = c/s (with their symmetric partners), and
w' = 2(−(y1 + y2) dϑ² + c² y1 dφ1² + s² y2 dφ2²) for W' = W_TT does not depend on φ1, φ2. This gives
(div W_TT)_φ1 = (div W_TT)_φ2 = 0 and

    (div W_TT)_ϑ = −2 ∂_ϑ(y1 + y2) + 2(s/c − c/s)(y1 + y2) + 2(s/c) y1 − 2(c/s) y2
                 = −(2/3) α_ϑ (c² cos θ + s² sin θ) + (10/3) α cs (cos θ − sin θ),

with α_ϑ := ∂_ϑ α, since y1 + y2 = (α/3)(c² cos θ + s² sin θ) and (4s² − 2c²) y1 + (2s² − 4c²) y2 =
2α c² s² (cos θ − sin θ). As (W_TT)_ϑ^ϑ = −2(y1 + y2) and the other components (W_TT)_b^ϑ vanish, the second part of
X_b is zero for b ≠ ϑ, and for b = ϑ it is

    ⟨(y1 + y2) ∂(div W_TT)_ϑ⟩ = (α/3) ⟨(c² cos θ + s² sin θ)((2/3) α_ϑ (c² sin θ − s² cos θ)
                                     − (10/3) α cs (sin θ + cos θ))⟩ = −(5/9) α² cs.

So X = −(1/3 + 5/9) α² cs dϑ = −(4/9) α² sin 2ϑ dϑ, and α² = A² env² h² r⁻³ gives [[eq:stage-one-source]]. ∎

### Derivatives of the stage-0 profiles and of the mean forcing term {#sec:stage-bounds-higher}

**Definition {#def:stage-derivative-bound}** (Derivative bounds.) For a smooth array F of functions on a neighbourhood
of Ω × S¹ and n ≥ 0, D_F[n] is the supremum, over the points p ∈ Ω × S¹ and the vectors e ∈ ℝ⁶ with |e| = 1, of
|(d/dt)ⁿ F(p + te)|_(t=0)|_F. Here p + te is formed in the coordinates (τ, x1, …, x4, θ), and |·|_F is the Frobenius
norm of the Cartesian components in (τ, x).

This section bounds D_F[n] for 0 ≤ n ≤ 14 at the numerical point, for F = W_TT, χ dv ⊗ dv, their sum and S.

**Lemma {#lem:stage-cartesian}** (Cartesian forms.) Let x ∈ ℝ⁴ ∖ {0}, ξ := x/r, ξ' := (ξ1, ξ2), ξ'' := (ξ3, ξ4), so
that c² = |ξ'|², s² = |ξ''|² and q = c² − s², and let U := (1, ξ) ∈ ℝ⁵, the components of dv. Then W_TT has no
τ components, and its spatial components form the 4 × 4 array

    W_TT = (A env(v) h/(3 r^(3/2))) B,      B := ( α1 I₂ + β1 ξ' ⊗ ξ'      γ ξ' ⊗ ξ''             )
                                                 ( γ ξ'' ⊗ ξ'             α2 I₂ + β2 ξ'' ⊗ ξ'' ),
    α1 := 4c² cos θ − 2s² sin θ,     α2 := −2c² cos θ + 4s² sin θ,     γ := 2(c² cos θ + s² sin θ),
    β1 := −(5 − q) cos θ + (1 − q) sin θ,     β2 := (1 + q) cos θ − (5 + q) sin θ,                {#eq:stage-cartesian-w}

I₂ the 2 × 2 identity. With T := 4q sin 2θ + (1 − q²) cos 2θ and Z := (0, −s² ξ', c² ξ'') ∈ ℝ⁵,

    χ dv ⊗ dv = −(A² env(v)² h² T/12)(r⁻² − (v − τ0)^(−1/2) r^(−3/2)) U ⊗ U,
    S = −(8/9) A² env(v)² h² r⁻⁴ (U ⊗ Z + Z ⊗ U).                                                {#eq:stage-cartesian-cs}

*Proof.* In the plane of (x1, x2), |dx'|² = dρ1² + ρ1² dφ1² with ρ1 = |x'| = rc and ρ1 dρ1 = x'·dx', so
ρ1² dφ1² = |dx'|² − (ξ'·dx')²/c²; likewise ρ2² dφ2² = |dx''|² − (ξ''·dx'')²/s² with ρ2 = rs. From ρ1 = r cos ϑ and
ρ2 = r sin ϑ, ρ1 dρ2 − ρ2 dρ1 = r² dϑ, that is r dϑ = (c/s) ξ''·dx'' − (s/c) ξ'·dx'. Substituting these into
W_TT = 2(−(y1 + y2)(r dϑ)² + y1 ρ1² dφ1² + y2 ρ2² dφ2²) and collecting the coefficients of |dx'|², |dx''|², (ξ'·dx')²,
(ξ''·dx'')² and (ξ'·dx')(ξ''·dx'') gives [[eq:stage-cartesian-w]], with α = A env h r^(−3/2); for example the
coefficient of (ξ'·dx')² is −2((y1 + y2) s² + y1)/c² = −(2α/3)((2c² + 3s²) cos θ − s² sin θ) = (α/3) β1, since
2(2c² + 3s²) = 5 − q and 2s² = 1 − q. The form of χ dv ⊗ dv is [[lem:chi-closed-form]] with dv = dτ + ξ·dx. For S,
d(c²) = d(|x'|²/r²) = (2/r)(ξ'·dx' − c² ξ·dx) = (2/r)(s² ξ'·dx' − c² ξ''·dx'') and d(c²) = −sin 2ϑ dϑ; insert this
into [[eq:stage-one-source]]. ∎

For complex vectors z, w ∈ ℂ⁴ write z·w := Σ_i z_i w_i, R²(z) := z·z and ‖z‖² := Σ_i |z_i|², and for a complex
array M write ‖M‖ := (Σ |M_ij|²)^(1/2); on real arrays ‖·‖ is |·|_F. Put K(σ) := (1 + σ²)/(1 − σ²).

**Lemma {#lem:complex-lines}** (Complex lines.) Let 0 < σ ≤ 1/2, let x ∈ ℝ⁴ with |x| = r > 0, e_x ∈ ℝ⁴ with
|e_x| ≤ 1 and t ∈ ℂ with |t| ≤ σr, and put z := x + t e_x. Then:

(a) (1 − σ)² r² ≤ |R²(z)| ≤ (1 + σ)² r²;

(b) for either square root r(z) of R²(z), ξ := z/r(z) satisfies ξ·ξ = 1 and ‖ξ‖² ≤ K(σ).

*Proof.* If e_x = 0 then z = x. Otherwise put ω := x/r, ê := e_x/|e_x|, u := ω·ê ∈ [−1, 1] and η := t|e_x|/r, so
that z = r(ω + η ê) and |η| ≤ σ. (a) R²(z) = r²(1 + 2ηu + η²) = r²(η − η₊)(η − η₋) with η± := −u ± i(1 − u²)^(1/2),
|η±| = 1; so (1 − |η|)² ≤ |1 + 2ηu + η²| ≤ (1 + |η|)². (b) ξ·ξ = R²(z)/r(z)² = 1, and ‖ξ‖² = ‖z‖²/|R²(z)|. If
u = ±1 then ξ = ±ω is real and ‖ξ‖² = 1. Otherwise ê = uω + (1 − u²)^(1/2) f with f a real unit vector orthogonal to
ω, and with w := η(1 − u²)^(1/2)/(1 + ηu) (note |ηu| < 1) one has ω + η ê = (1 + ηu)(ω + w f). Hence
‖z‖² = r²|1 + ηu|²(1 + |w|²) and R²(z) = r²(1 + ηu)²(1 + w²), so ‖ξ‖² = (1 + |w|²)/|1 + w²|. With w = w1 + i w2,
both |1 + w²|² and (1 + |w|²)² − 4w2² equal (1 + w1² − w2²)² + 4w1²w2²; therefore

    ‖ξ‖² = (1 − (2|w2|/(1 + |w|²))²)^(−1/2) ≤ (1 − (2|w2|/(1 + w2²))²)^(−1/2) = (1 + w2²)/(1 − w2²),

provided |w2| < 1, and it suffices to show |w2| ≤ σ. Now w2 = (1 − u²)^(1/2) Im η/|1 + ηu|². Write η = ϱ e^(iφ) with
ϱ ≤ σ; then |1 + ηu|² = 1 + 2ϱu cos φ + ϱ²u² ≥ 1 + 2ϱu cos φ ≥ 0, and (1 − u²)^(1/2)|sin φ| − 2ϱu cos φ ≤
(1 − u² + 4ϱ²u²)^(1/2) ≤ 1 because 2ϱ ≤ 1. So (1 − u²)^(1/2)|Im η| ≤ ϱ(1 + 2ϱu cos φ) ≤ σ|1 + ηu|². ∎

**Lemma {#lem:complex-unit}** (Unit complex vectors.) Let ξ ∈ ℂ⁴ with ξ·ξ = 1, put K := ‖ξ‖², and assume K² < 2. Let
ξ' := (ξ1, ξ2), ξ'' := (ξ3, ξ4), c² := ξ'·ξ', s² := ξ''·ξ'', q := c² − s², ν1 := ‖ξ'‖² and ν2 := ‖ξ''‖². Then:

(a) c² + s² = 1, ν1 + ν2 = K, |c²| ≤ ν1, |s²| ≤ ν2, |c²| + |s²| ≥ 1, and |c²|² + |s²|² = (1 + |q|²)/2;

(b) |Im q| ≤ (K² − 1)^(1/2) < 1; and Q := (1 + |q|²)/|1 + q²| satisfies Q ≤ K²/(2 − K²), so that 1 + q² ≠ 0;

(c) (ν1² − |c²|²) + (ν2² − |s²|²) ≤ K² − 1;

(d) |ν1 − c²| + |ν2 − s²| ≤ K − 1 + (K² − 1)^(1/2).

*Proof.* Write ξ = α + iβ with α, β ∈ ℝ⁴ and α', β', α'', β'' for their halves. From ξ·ξ = |α|² − |β|² + 2iα·β = 1
and K = |α|² + |β|², α·β = 0, |α|² = (K + 1)/2, |β|² = (K − 1)/2 and 4|α|²|β|² = K² − 1. (a) The first two hold by
definition; |c²| = |ξ'·ξ'| ≤ ν1 and |s²| ≤ ν2 by the Cauchy–Schwarz inequality; |c²| + |s²| ≥ |c² + s²| = 1; and
c² = (1 + q)/2, s² = (1 − q)/2 give the last. (b) Im q = 2(α'·β' − α''·β''), and α'·β' + α''·β'' = α·β = 0, so
Im q = 4α'·β' = −4α''·β'' and (Im q)² = 16|α'·β'||α''·β''| ≤ 16|α'||α''||β'||β''| ≤ 4|α|²|β|² = K² − 1, using
|α'||α''| ≤ |α|²/2 and |β'||β''| ≤ |β|²/2. For every complex q, both |1 + q²|² and (1 + |q|²)² − 4(Im q)² equal
(1 + q1² − q2²)² + 4q1²q2², q = q1 + iq2. With b := |Im q| < 1 and 1 + |q|² ≥ 1 + b² this gives
Q = (1 − (2b/(1 + |q|²))²)^(−1/2) ≤ (1 + b²)/(1 − b²) ≤ K²/(2 − K²). (c) ν1² − |c²|² = (|α'|² + |β'|²)² −
(|α'|² − |β'|²)² − 4(α'·β')² ≤ 4|α'|²|β'|², likewise for the second halves, and |α'|²|β'|² + |α''|²|β''|² ≤
|α|²|β|². (d) ν1 − c² = 2|β'|² − 2iα'·β', so |ν1 − c²| ≤ 2|β'|² + 2|α'||β'|, and adding the second halves gives at most
2|β|² + 2|α||β| = K − 1 + (K² − 1)^(1/2). ∎

**Lemma {#lem:profile-complex}** (The profiles along complex lines.) On (ℝ⁴ ∖ {0}) × ℝ put, in the notation of
[[lem:stage-cartesian]],

    G_W := h B/(3 r^(3/2)),   G_a := −h² T U ⊗ U/(12 r²),   G_b := h² T U ⊗ U/(12 r^(3/2)),
    G_S := −(8/9) h² r⁻⁴ (U ⊗ Z + Z ⊗ U),

so that at the numerical point, where A = 1,

    W_TT = env(v) G_W,   χ dv ⊗ dv = env(v)² G_a + env(v)² (v − τ0)^(−1/2) G_b,   S = env(v)² G_S.  {#eq:profile-split}

Let 0 < σ ≤ 9/25, ρ := σa, p = (τ, x, θ) ∈ Ω × S¹ and e = (e_τ, e_x, e_θ) ∈ ℝ⁶ with |e| = 1. Put K := K(σ) and
Q̄ := K²/(2 − K²). Then:

(a) for each i ∈ {W, a, b, S} the function t ↦ G_i(x + t e_x, θ + t e_θ) of real t extends holomorphically to a
neighbourhood of the disc |t| ≤ ρ, and there

    ‖G_W‖ ≤ ((1 − σ)a)^(−3/2) M_W(σ),     M_W(σ) := (1/3)(1.02 Q̄ (20 + 4K² + 54.84 (K² − 1)))^(1/2),
    ‖G_a‖ ≤ ((1 − σ)a)^(−2) M_A(σ),       ‖G_b‖ ≤ ((1 − σ)a)^(−3/2) M_A(σ),
    M_A(σ) := (1/3)(1.08)^(1/2) (2Q̄² − 1)^(1/2) (1 + K),
    ‖G_S‖ ≤ ((1 − σ)a)^(−4) M_S(σ),       M_S(σ) := (8/9) Q̄ K (2(1 + K) + 32σ²/(1 − σ)²)^(1/2);

(b) on Ω × S¹, |G_W|_F ≤ (2√6/3) a^(−3/2), |G_a|_F ≤ (2/3) a⁻², |G_b|_F ≤ (2/3) a^(−3/2) and |G_S|_F ≤ (16/9) a⁻⁴;
and for m ≥ 1, with ā := 3.70565,

    ‖(d/dt)^m G_i(x + t e_x, θ + t e_θ)|_(t=0)‖ ≤ m! (ā/σ)^m L_i(σ),                                {#eq:profile-cauchy}

where L_W := ā^(3/2)(1 − σ)^(−3/2) M_W, L_a := ā²(1 − σ)^(−2) M_A, L_b := ā^(3/2)(1 − σ)^(−3/2) M_A and
L_S := ā⁴(1 − σ)^(−4) M_S.

*Proof.* (a) Let |t| ≤ ρ and z := x + t e_x. Since r ≥ a on Ω, |t| ≤ σr, and [[lem:complex-lines]] (a) gives
|R²(z)| ≥ (1 − σ)² a² > 0. So R²(z) has a holomorphic square root r(z) on a neighbourhood of the disc, equal to |x| at
t = 0, and ξ := z/r(z) is holomorphic, with ξ·ξ = 1 and ‖ξ‖² ≤ K ≤ K(9/25) = 353/272 by [[lem:complex-lines]] (b);
so K² < 2. Put c² := ξ'·ξ', s² := ξ''·ξ'' and q := c² − s². By [[lem:complex-unit]] (b), 1 + q² ≠ 0, so
h := 2^(1/2)(1 + q²)^(−1/2) has a holomorphic branch, positive at t = 0, and so do r(z)^(−1/2) and r(z)^(−3/2); and
θ' := θ + t e_θ enters only through cos θ', sin θ', cos 2θ' and sin 2θ'. The formulas of [[lem:stage-cartesian]] with
these functions define the extensions. For real t they agree with the profiles, because the roots involved are
continuous roots of the same nonvanishing functions and agree at t = 0. Since a < 0.27, |Im θ'| ≤ ρ < 0.0972, so
κ² := |cos θ'|² + |sin θ'|² = cosh(2 Im θ') < cosh 0.1944 < 1.02 and κ₂² := |cos 2θ'|² + |sin 2θ'|² =
cosh(4 Im θ') < cosh 0.3888 < 1.08. For complex p1, p2 the Cauchy–Schwarz inequality gives
|p1 cos θ' + p2 sin θ'|² ≤ κ²(|p1|² + |p2|²), and the same with 2θ' and κ₂. Put Q := (1 + |q|²)/|1 + q²| ≤ Q̄. Then
|h|² = 2/|1 + q²| = 2Q/(1 + |q|²), and by [[lem:complex-unit]] (a), |h|²(|c²|² + |s²|²) = Q. Finally |r(z)| ≥
(1 − σ)a by [[lem:complex-lines]] (a).

*G_W.* For complex numbers α, β and the complex 2-vector ξ', ‖α I₂ + β ξ' ⊗ ξ'‖² = 2|α|² + 2 Re(ᾱ β c²) + |β|² ν1² =
|α|² + |α + β c²|² + |β|²(ν1² − |c²|²), with ν1 := ‖ξ'‖². Here α1 + β1 c² = −s² γ and α2 + β2 s² = −c² γ, and the
off-diagonal blocks have the squared norm |γ|² ν1 ν2 each, ν2 := ‖ξ''‖². So

    ‖B‖² = |α1|² + |α2|² + |γ|²(|c²|² + |s²|² + 2ν1ν2) + |β1|²(ν1² − |c²|²) + |β2|²(ν2² − |s²|²).

Now |α1|² + |α2|² ≤ 20κ²(|c²|² + |s²|²), |γ|² ≤ 4κ²(|c²|² + |s²|²), |c²|² + |s²|² + 2ν1ν2 ≤ (ν1 + ν2)² ≤ K², and
|β1|², |β2|² ≤ κ²(26 + 12|q| + 2|q|²). Since the quadratic (12 + 6√5)y² − 12y + 6√5 − 12 has discriminant zero,
12y + 24 ≤ (12 + 6√5)(1 + y²) for real y; so 2(26 + 12|q| + 2|q|²)/(1 + |q|²) ≤ 28 + 12√5 < 54.84 and
|h|² |β_j|² ≤ 54.84 κ² Q. With [[lem:complex-unit]] (c), |h|² ‖B‖² ≤ κ² Q (20 + 4K² + 54.84 (K² − 1)), and
‖G_W‖ = |h| ‖B‖ |r(z)|^(−3/2)/3 gives the bound.

*G_a and G_b.* As c² + s² = 1, 1 + q² = 2(c⁴ + s⁴), 1 − q² = 4c²s² and q = c⁴ − s⁴, so
h²T = 4((c⁴ − s⁴) sin 2θ' + c²s² cos 2θ')/(c⁴ + s⁴). Put Σ := |c²|² + |s²|² and J := 2 Im(c² s̄²). Then
|c² ± i s²|² = Σ ± J, so |c⁴ + s⁴|² = Σ² − J² and Q = 2Σ/|1 + q²| = Σ/|c⁴ + s⁴|. Moreover |c²s²|² − Re(c⁴ s̄⁴) =
|c² s̄²|² − Re((c² s̄²)²) = J²/2, whence |c⁴ − s⁴|² + |c²s²|² = |c⁴ + s⁴|² − 4 Re(c⁴ s̄⁴) + |c²s²|² =
Σ² + J² − 3|c²s²|² ≤ Σ² + J². So (|c⁴ − s⁴|² + |c²s²|²)/|c⁴ + s⁴|² ≤ (Σ² + J²)/(Σ² − J²) = 2Q² − 1 and
|h²T| ≤ 4κ₂(2Q² − 1)^(1/2). With U := (1, ξ), ‖U ⊗ U‖ = ‖U‖² = 1 + ‖ξ‖² ≤ 1 + K; and |r(z)|⁻² and |r(z)|^(−3/2) are
at most ((1 − σ)a)^(−2) and ((1 − σ)a)^(−3/2).

*G_S.* For complex 5-vectors, ‖U ⊗ Z + Z ⊗ U‖² = 2‖U‖²‖Z‖² + 2|U·Z̄|², Z̄ the complex conjugate. Here
Z = (0, −s² ξ', c² ξ''), so ‖Z‖² = |s²|² ν1 + |c²|² ν2 ≤ ν1ν2(|c²| + |s²|), and U·Z̄ = c̄² ν2 − s̄² ν1, so
|U·Z̄| = |(c² − ν1)ν2 − (s² − ν2)ν1| ≤ K(K − 1 + (K² − 1)^(1/2)) = 2σK/(1 − σ) by [[lem:complex-unit]] (d), the bound
being increasing in K. As |h²| = 2/|1 + q²| = Q/Σ and Σ ≥ (|c²| + |s²|)²/2 ≥ 1/2, one has ‖Z‖²/Σ² ≤
4ν1ν2/(|c²| + |s²|)³ ≤ K² and |U·Z̄|²/Σ² ≤ 4(2σK/(1 − σ))²; so |h²| ‖U ⊗ Z + Z ⊗ U‖ ≤
Q K (2(1 + K) + 32σ²/(1 − σ)²)^(1/2), and |r(z)|⁻⁴ ≤ ((1 − σ)a)⁻⁴.

(b) For real arguments ξ is real, so K = Q = 1, ν1 = |c²| and ν2 = |s²|, and with κ = κ₂ = 1 the estimates of the
proof of (a) give |G_W|_F ≤ (1/3) 24^(1/2) r^(−3/2) = (2√6/3) r^(−3/2), |G_a|_F ≤ (2/3) r⁻² and
|G_b|_F ≤ (2/3) r^(−3/2), as in the proof of [[prop:stage-zero-bounds]]. For G_S, U·Z = 0, |U| = √2
and |Z| = cs, so |G_S|_F = (8/9) h² r⁻⁴ · 2cs = (16/9) r⁻⁴ sin 2ϑ/(1 + cos² 2ϑ) ≤ (16/9) r⁻⁴. On Ω, r ≥ a. For m ≥ 1,
Cauchy's estimate on the circle |t| = ρ, applied to the holomorphic function of (a), gives the bound
m! ρ^(−m) max_(|t|=ρ) ‖G_i‖; and ρ^(−m) ≤ (ā/σ)^m and ((1 − σ)a)^d ≤ ā^(−d)(1 − σ)^d for d < 0, because
a > 1/ā by [[lem:lambda0-point]] (a). ∎

**Lemma {#lem:envelope-lines}** (The factors that depend on v, along lines.) Let V_1 := √2 and V_m := 4|b_m| a^(1−m)
for 2 ≤ m ≤ 14, where |b_m| := C(2m, m)/((2m − 1) 4^m), and for 0 ≤ k ≤ j ≤ 14 let B_(j,k) be j!/k! times the
coefficient of T^j in (Σ_(m=1)^14 V_m T^m)^k. Let E be a smooth function on (τ0, ∞) with |E^(k)| ≤ F_k for
0 ≤ k ≤ 14. Then for p ∈ Ω × S¹ and e ∈ ℝ⁶ with |e| = 1, and v(p + te) := τ + t e_τ + |x + t e_x|,

    |(d/dt)^j E(v(p + te))|_(t=0)| ≤ Σ_(k=0)^j F_k B_(j,k)          (0 ≤ j ≤ 14).                    {#eq:envelope-lines}

For E = env one may take F_k = e_k, the bound of the third column of [[eq:envelope-derivatives]]; for E = env²,
F_k^a := Σ_(l=0)^k C(k, l) e_l e_(k−l); and for E = env² (v − τ0)^(−1/2), F_k^b := Σ_(l=0)^k C(k, l) F_l^a w_(k−l),
where w_n := (1/2)_n (2/5)^(n+1/2) and (1/2)_n := (1/2)(3/2)⋯((2n − 1)/2).

*Proof.* Put g(t) := v(p + te). Then g'(0) = e_τ + ξ·e_x and |g'(0)| ≤ |e_τ| + |e_x| ≤ √2. If e_x ≠ 0, put
cos ψ := ξ·e_x/|e_x| and w := −t|e_x|/r. For real t near 0, |x + t e_x| = r(1 − 2w cos ψ + w²)^(1/2) =
r(1 − w e^(iψ))^(1/2)(1 − w e^(−iψ))^(1/2), the two factors being complex conjugate. The binomial series
(1 − ζ)^(1/2) = Σ_k b_k ζ^k, |ζ| < 1, has b_0 = 1 and b_k = −|b_k| for k ≥ 1. So the coefficient of w^m in the
product is Σ_(k+l=m) b_k b_l e^(i(k−l)ψ). Its modulus is at most Σ_(k+l=m) |b_k||b_l|, the coefficient of ζ^m in
(2 − (1 − ζ)^(1/2))² = 5 − ζ − 4(1 − ζ)^(1/2), that is 4|b_m| for m ≥ 2. Hence |g^(m)(0)|/m! ≤ 4|b_m| |e_x|^m
r^(1−m) ≤ V_m for m ≥ 2, since |e_x| ≤ 1 and r ≥ a.

Let P(t) := Σ_(m=1)^j g^(m)(0) t^m/m!. Taylor's formula for E at g(0), with y = g(t) − g(0) = P(t) + o(|t|^j) and
y = O(|t|), gives E(g(t)) = Σ_(k=0)^j E^(k)(g(0)) P(t)^k/k! + o(|t|^j). So (E∘g)^(j)(0)/j! is the coefficient of t^j
in Σ_k E^(k)(g(0)) P(t)^k/k!. That coefficient is a polynomial in the coefficients of P with nonnegative coefficients;
its modulus is therefore at most the same polynomial in the bounds V_m, with |E^(k)| ≤ F_k, which is
[[eq:envelope-lines]]. For the three choices of E, Leibniz's rule gives |(env²)^(k)| ≤ F_k^a. On the support
[1/2, 7/2] of env one has v − τ0 ≥ 5/2, where |d^n (v − τ0)^(−1/2)/dv^n| = (1/2)_n (v − τ0)^(−1/2−n) ≤ w_n; and off
the support env² vanishes with all its derivatives. ∎

[[sec:stage-bounds-table-v]], [[sec:stage-bounds-table-b]] and [[sec:stage-bounds-table-f]] print upper bounds for
V_m, B_(j,k), F_k^a, w_k and F_k^b, and [[sec:stage-bounds-table-eps]] the resulting bounds ε_j^W, ε_j^a and ε_j^b of
the right side of [[eq:envelope-lines]] for env, env² and env²(v − τ0)^(−1/2). [[sec:stage-bounds-table-sigma]] and
[[sec:stage-bounds-table-gamma]] print M_W, M_A, M_S and L_i at eight values of σ, and the bounds γ_m^i of
[[lem:profile-complex]] (b) with the σ used for each m.

**Proposition {#prop:stage-bounds-higher}** (Derivative bounds at the numerical point.) At the numerical point, for
0 ≤ n ≤ 14,

    D_(W_TT)[n] ≤ D^W[n],    D_(χ dv⊗dv)[n] ≤ D^χ[n],    D_S[n] ≤ D^S[n],    D_(W_TT + χ dv⊗dv)[n] ≤ D^W[n] + D^χ[n],

with the numbers of [[sec:stage-bounds-table-d]]. At n = 0, D_S[0] = (16/9) c² a⁻⁴ ∈ (587.711, 587.713), c the
envelope constant of [[eq:envelope]], attained at v = 2, r = a, ϑ = π/4. In particular:

    n     D_(W_TT)[n]       D_(χ dv⊗dv)[n]     D_S[n]            D_(W_TT + χ dv⊗dv)[n]
    0     15.43             16.05              587.72            31.48
    1     6.253 · 10²       1.196 · 10³        4.260 · 10⁴       1.822 · 10³
    3     9.341 · 10⁵       3.017 · 10⁶        1.526 · 10⁸       3.952 · 10⁶
    6     1.562 · 10¹¹      8.028 · 10¹¹       6.025 · 10¹³      9.590 · 10¹¹
    9     8.741 · 10¹⁶      5.301 · 10¹⁷       5.044 · 10¹⁹      6.176 · 10¹⁷
    11    1.020 · 10²¹      6.330 · 10²¹       6.444 · 10²³      7.350 · 10²¹
    14    2.430 · 10²⁷      1.518 · 10²⁸       1.583 · 10³⁰      1.761 · 10²⁸

*Proof.* Let p ∈ Ω × S¹ and e ∈ ℝ⁶ with |e| = 1. By [[eq:profile-split]] and Leibniz's rule along the line,

    (d/dt)ⁿ W_TT(p + te)|_(t=0) = Σ_(j=0)^n C(n, j) ((d/dt)^j env(v(p + te))) ((d/dt)^(n−j) G_W(x + t e_x, θ + t e_θ))

at t = 0, and likewise for the two terms of χ dv ⊗ dv and for S. By [[lem:envelope-lines]] the first factor is at most
ε_j^W, ε_j^a, ε_j^b or ε_j^S := ε_j^a. By [[lem:profile-complex]] (b), with the σ printed in
[[sec:stage-bounds-table-gamma]], the second is at most γ_(n−j)^W, γ_(n−j)^a, γ_(n−j)^b or γ_(n−j)^S. Summing gives
D^W[n], D^χ[n] and D^S[n], and the triangle inequality gives the sum. At n = 0 the sharper values 15.43 and 16.05 are
those of [[prop:stage-zero-bounds]]. By [[lem:profile-complex]] (b), |S|_F = (16/9) env² r⁻⁴ sin 2ϑ/(1 + cos² 2ϑ) ≤
(16/9) c² a⁻⁴, with equality at v = 2, r = a, ϑ = π/4; this is a point of Ω × S¹, since Ω is invariant under rotations
of x and contains the point X* of [[sec:lambda0-norms]], where v = 2 and r = a. The enclosure follows
from 1.3240867 < c < 1.3240879 and 0.2698587885 < a < 0.269858789. ∎

No result of the paper uses the bounds of this section.

### The threshold in three norms {#sec:lambda0-norms}

The bounds of [[prop:lambda0]] compare ε1 with a constant C_app such that |g_app − g0| ≤ C_app λ. Both depend on how
|·| is read on symmetric 2-tensors of Cartesian components. This section treats three readings: the operator norm of
[[sec:profiles]], the Frobenius norm |·|_F, and the largest absolute entry |·|_max. Let X* be the point
τ = 2 − a, x = (a, 0, 0, 0) (so r = a, v = 2, ϑ = 0, φ1 = 0). It lies in Ω of [[eq:omega]], since τ0 < 2 − a < τ_end
by [[lem:lambda0-point]] (c) and v + τ − τ_end < 4 < V + 1. Put

    K := c a^(−3/2),      χ* := (c²/3)(a⁻² − a^(−3/2)/2),      B := (4/3) K² + 4 χ*².

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
D := dv ⊗ dv; as θ runs over S¹, so does s. At X*, A = 1, env(2) = c β(0) = c, cos 2ϑ = 1 and h = 1, and
x1 = a, x2 = x3 = x4 = 0, cos²ϑ = 1, sin²ϑ = 0. The Cartesian formula of [[lem:waves]] (a), at the phase s, gives
λ W_TT = 2 a^(−3/2) (G dx2² − (G/3)(dx2² + dx3² + dx4²)) with G/λ = A env h cos s = c cos s, so in the components
(τ, x1, x2, x3, x4)

    W_TT(X*, s) = K cos s Λ,      Λ := diag(0, 0, 4/3, −2/3, −2/3).

By [[lem:chi-closed-form]], with cos 2ϑ = 1, h = 1 and v − τ0 = 4, χ(X*, s) = −(1/3) c² sin 2s (a⁻² − a^(−3/2)/2) =
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
0.269858789² · 13.7317809 < 1. Hence a⁻² − a^(−3/2)/2 > 13.7317809 − 3.5666883 = 10.1650926. With c > 1.3240711
([[eq:envelope-c]]),

    (4/3) K > (4/3)(1.3240711)(7.1333765) > 12.5934635,      χ* > (1.3240711²/3)(10.1650926) > 5.9403588,
    B > (3/4)(12.5934635)² + 4 (5.9403588)² > 260.097942 > 16.127552² = 260.0979337….

By [[lem:epsilon-one]] (c), s0 < 0.030768560, and by [[lem:lambda0-point]] (d), m* > 16.23497014, so 1/(4m*) <
0.0153989. Now 0.0024433 · 12.593309 > 0.03076918, 0.0019079 · 16.127552 > 0.03076975 and 0.0012228 · 12.593309 >
0.01539909, which with these bounds give [[eq:lambda0-norms]]. ∎

Since the threshold of [[prop:lambda0]] lies below ε1/C_app, [[eq:lambda0-norms]] bounds it by 0.0024433, 0.0019079
and 0.0012228 in the three readings, whatever the stage data. A nonzero M_22 lowers the bounds of (i) and (iii), and a
nonzero m1(X*) that of (ii).

**Remark {#rem:lambda0-norms-c}** (The constant c in the three bounds.) [[prop:lambda0-norms]] uses about c only a
lower bound, through K, χ* and B, which increase with c; s0 and m* depend on a and μ_end = 227/192 alone, and the upper
end of c enters nowhere. The figure 12.593309 holds for every c ≥ 1.3240549 and 16.127552 for every c ≥ 1.3240711,
while the three bounds of [[eq:lambda0-norms]] hold for every c ≥ 1.32404: at c = 1.32404 the arithmetic above gives
(4/3) K > 12.593167 and B > 16.12696², and 0.0024433 · 12.593167, 0.0019079 · 16.12696 and 0.0012228 · 12.593167
exceed 0.030768560, 0.030768560 and 0.0153989. With the sharper lower end
c > 1.3240867 of [[eq:envelope-c]] one gets C_app > 12.593611 in (i) and (iii) and C_app > 16.127845 in (ii).
