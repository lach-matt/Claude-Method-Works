This part proves, at one parameter point, the constants on which the bounds of [[prop:lambda0]] and the threshold of
[[thm:layer]] rest: the normalising constant of the envelope and the derivatives of the envelope, the admissible range
of ε1, the energy constant of the wave operator of g0 on Ω, and the size of the explicit profiles of stage 0. Every
number below is justified by an inequality between explicit rationals, or by the value of an elementary function at a
rational point, which the reader can check by hand.

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
and by [[lem:lambda0-point]] (a), a^(−3/2) > 7.133376, so

    (4/3) c a^(−3/2) ≥ (4/3) · 1.3240711 · 7.133376 > 12.593309.

This uses c ≥ 1.3240711 and nothing else about c; with any proven lower bound c_− in its place the constant is
(4/3) c_− a^(−3/2). Combined with ε1 < s0 < 0.030768560 ([[lem:epsilon-one]]), the quotient of the two is
0.030768560/12.593309 < 0.0024433, which is the operator-norm bound of [[prop:lambda0]]; that bound therefore holds
exactly as far as the lower end of c does. (ii) The upper end enters through env ≤ c: in [[lem:lambda0-point]] (c),
where any c < 3 suffices; in the range 0 ≤ μ' ≤ (2/9) c² used in [[prop:energy-constant]]; and in the bound
1 + c²/18 ≤ 1.0974028 used for the threshold of [[thm:layer]], which needs c ≤ 1.3241035.

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

Bounds on the derivatives of orders 1 to 14 on Ω × S¹ of W_TT, of χ dv ⊗ dv and of the θ-mean of R^(1) at
stage 1, of the kind [[lem:envelope-derivatives]] gives for the envelope, are [[pending:computational-1]]. No result
of the paper uses them.
