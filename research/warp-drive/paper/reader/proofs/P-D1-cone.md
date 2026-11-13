### The data cone: an explicit approximant and exact data {#sec:cone-approximant}

This section concerns the characteristic data on the outgoing cone u = −10 at the two seeds of [[ch:ten-l5]], whose
wavelength parameters are λ = 1 (the first seed) and λ = 1/√10 (the second seed). On this cone the Raychaudhuri
constraint determines the areal radius R from the other data. We prove two things. First, an explicit approximant
R_app, a tensor Chebyshev series with the coefficients of Appendix B ([[sec:cone-tables]]), satisfies the constraint
up to an explicit residual ([[prop:cone-residual]]). Second, the constraint has an exact solution on every generator,
positive and within an explicit distance of the Tangherlini radius ([[prop:cone-exact]]); the approximant lies within
10⁻⁶ of it ([[cor:cone-compare]]).

### The constraint on the data cone {#sec:cone-constraint}

The metrics of the class in double-null gauge are

    g = −4 e^(2W) du dv + G_x (dx − β du)² + R² ((1 + x)/2) e^(2P) dφ1² + R² ((1 − x)/2) e^(2Q) dφ2²,

with R, P, Q, W, G_x, β functions of (u, v, x) and x ∈ [−1, 1]. For every such metric
(see [[pending:raychaudhuri-identity]])

    Ric_vv = −(3/R) (∂_v²R − 2 ∂_vW ∂_vR) − ((∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)²),          {#eq:cone-raychaudhuri}

which contains no shift and no derivative in x, and so is determined by the data (R, P, Q, W) on an outgoing cone
u = const. For such data, Ric_vv[R] denotes the right side of [[eq:cone-raychaudhuri]].

Put f(r) := 1 − r^(−2). Along the cone u = −10 the Tangherlini areal radius r ∈ [10, ∞) is a parameter on each
generator, related to v by

    v(r) = 2(r − 10) + ln(11(r − 1)/(9(r + 1))),        v′(r) = 2 + 2/(r² − 1) = 2/f(r),                {#eq:cone-v}

so v(10) = 0 and dr/dv = f/2. Let r_s < r_e be the solutions of v(r_s) = 1/2 and v(r_e) = 7/2 (v is increasing);
r_s = 10.2475603901…, r_e = 11.7350863591…. The data on the cone are W = (1/2) ln(f(r)/(2 f(10))) and

    m = h(x) φ(r) cos θ(r),     n = h(x) φ(r) sin θ(r),     h(x) = (2/(1 + x²))^(1/2),
    φ(r) = (λ/2) r^(−3/2) env(v(r)),     θ(r) = v(r)/λ,                                                   {#eq:cone-data}
    P = (2(1 + x) m − (1 − x) n)/3,     Q = (2(1 − x) n − (1 + x) m)/3,

where env(v) = sin⁴(π(v − 1/2)/3) for 1/2 < v < 7/2 and env(v) = 0 otherwise. The function env is C³, so φ is C³ in
r, and φ = φ′ = 0 for r ∉ (r_s, r_e): there the data are those of Tangherlini. R is the unknown.

**Lemma {#lem:cone-generator}** (The constraint on a generator.) Let A := (φ cos θ)′ and B := (φ sin θ)′, the prime
denoting d/dr, and

    w(r, x) := (4/(9(1 + x²))) H(r, x),      H := (1 + x)² A² − (1 − x²) A B + (1 − x)² B².                {#eq:cone-w}

Then s := (∂_vP)² + (∂_vQ)² + (∂_vP + ∂_vQ)² = (3f²/4) w, w vanishes for r ∉ (r_s, r_e), and for R(·, x) of class C²
in r and nonzero,

    Ric_vv[R] = −(3f²/(4R)) (∂_r²R + w R).                                                               {#eq:cone-ricvv}

*Proof.* Since dr/dv = f/2 and f′ = 2r^(−3), ∂_vR = (f/2) ∂_rR and ∂_v²R = (f/2)² ∂_r²R + (f/(2r³)) ∂_rR, while
∂_vW = (f/2) f′/(2f) = 1/(2r³). Hence ∂_v²R − 2 ∂_vW ∂_vR = (f/2)² ∂_r²R. Next, ∂_r m = h A and ∂_r n = h B. With
a := (1 + x) A and b := (1 − x) B,

    ∂_vP = (f h/6)(2a − b),     ∂_vQ = (f h/6)(2b − a),     ∂_vP + ∂_vQ = (f h/6)(a + b),

and (2a − b)² + (2b − a)² + (a + b)² = 6(a² − ab + b²). So s = (f² h²/6)(a² − ab + b²) = (f²/(3(1 + x²))) H =
(3f²/4) w. Substituting both in [[eq:cone-raychaudhuri]] gives [[eq:cone-ricvv]]. Outside (r_s, r_e), φ = φ′ = 0, so
A = B = 0 and w = 0. ∎

So on each generator the constraint Ric_vv = 0 is the linear equation ∂_r²R = −w R, that is
∂_r²R = −(4/(3f²)) R s.

**Lemma {#lem:cone-w}** (The size of w.) On [r_s, r_e] × [−1, 1], A² + B² = φ′² + φ² θ′² and

    0 ≤ w ≤ (8/9)(A² + B²) ≤ W̄,      s ≤ s̄,

with W̄ = 1.99 × 10⁻³ and s̄ = 1.46 × 10⁻³ at the first seed, and W̄ = 8.55 × 10⁻⁴ and s̄ = 6.3 × 10⁻⁴ at the second.

*Proof.* Expanding,

    H = (1 + x²)(A² + B²) + A B (x² − 1) + 2(A² − B²) x.

By the Cauchy–Schwarz inequality, |A B (x² − 1) + 2(A² − B²) x| ≤ (A²B² + (A² − B²)²)^(1/2) ((x² − 1)² + 4x²)^(1/2),
and A²B² + (A² − B²)² ≤ 4A²B² + (A² − B²)² = (A² + B²)², (x² − 1)² + 4x² = (1 + x²)². Hence
0 ≤ H ≤ 2(1 + x²)(A² + B²), which is the first claim. Next, A + iB = (φ e^(iθ))′ = (φ′ + iφθ′) e^(iθ), so
A² + B² = φ′² + φ²θ′². Write σ := sin(π(v − 1/2)/3) and κ := cos(π(v − 1/2)/3), so env = σ⁴ and
d env/dv = (4π/3) σ³ κ. With v′ = 2/f,

    φ θ′ = r^(−3/2) σ⁴/f,      φ′ = λ r^(−3/2) σ³ ((4π/3) κ/f − 3σ/(4r)),
    A² + B² = r^(−3) f^(−2) σ⁶ (σ² + λ² ((4π/3) κ − 3fσ/(4r))²).

On [r_s, r_e] we have 0 ≤ σ ≤ 1, |κ| = (1 − σ²)^(1/2), 3f/(4r) ≤ 3/(4r_s) ≤ β := 0.0732, and r^(−3) f^(−2) =
r/(r² − 1)² is decreasing, so r^(−3) f^(−2) ≤ r_s/(r_s² − 1)² ≤ 9.473 × 10⁻⁴. With y := σ² ∈ [0, 1] and a := 4π/3
(a² = 16π²/9 = 17.5460…),

    σ⁶ (σ² + λ² (aκ − 3fσ/(4r))²) ≤ g(y) := y⁴ + λ² y³ (a (1 − y)^(1/2) + β)².

The function y³ (1 − y)^(1/2) has its maximum on [0, 1] at y = 6/7, equal to 216/(343 √7) ≤ 0.23803. At the first
seed, g(y) = α y³ − γ y⁴ + 2aβ y³ (1 − y)^(1/2) with α := a² + β² and γ := a² − 1; the polynomial α y³ − γ y⁴ has
its maximum on [0, ∞) at y = 3α/(4γ), equal to 27α⁴/(256γ³) ≤ 2.2097. So g ≤ 2.2097 + 2aβ (0.23803) ≤ 2.3557 and
w ≤ (8/9)(9.473 × 10⁻⁴)(2.3557) ≤ 1.99 × 10⁻³. At the second seed, λ² = 1/10 and the polynomial part of g is
(1 − a²/10) y⁴ + ((a² + β²)/10) y³, whose derivative y² (4(1 − a²/10) y + 3(a² + β²)/10) is positive on (0, 1]
because 1 − a²/10 < 0 and 4(1 − a²/10) + 3a²/10 = 4 − a²/10 > 0. So the polynomial part is at most its value 1 + β²/10
at y = 1, g ≤ 1 + β²/10 + (2aβ/10)(0.23803) ≤ 1.0152, and w ≤ (8/9)(9.473 × 10⁻⁴)(1.0152) ≤ 8.55 × 10⁻⁴. Finally
s = (3f²/4) w ≤ (2f²/3)(A² + B²) = (2/3) r^(−3) σ⁶ (σ² + λ² (aκ − 3fσ/(4r))²) ≤ (2/3) r_s^(−3) g, with
r_s^(−3) ≤ 9.294 × 10⁻⁴; this gives s̄. ∎

### The approximant {#sec:cone-approximant-def}

T_k denotes the Chebyshev polynomial of degree k, T_k(cos ψ) = cos(kψ).

**Definition {#def:cone-approximant}** (The approximant.) Let N_r := 40 at the first seed and N_r := 64 at the
second, c := (r_s + r_e)/2, ℓ := (r_e − r_s)/2 and t := (r − c)/ℓ, so that t ∈ [−1, 1] for r ∈ [r_s, r_e]. Let
C_(ij), 0 ≤ i ≤ N_r, 0 ≤ j ≤ 28, be the decimal numbers of [[sec:cone-table-c1]] (first seed) and
[[sec:cone-table-c2]] (second seed), and

    S(r, x) := Σ_(i=0)^(N_r) Σ_(j=0)^(28) C_(ij) T_i(t) T_j(x),    a(x) := r_s − S(r_s, x),    b(x) := 1 − ∂_rS(r_s, x).

The approximant is

               ⎧ r                                              for 10 ≤ r ≤ r_s,
    R_app :=   ⎨ S(r, x) + a(x) + b(x)(r − r_s)                 for r_s ≤ r ≤ r_e,             {#eq:cone-approximant}
               ⎩ R_app(r_e, x) + ∂_rR_app(r_e, x)(r − r_e)      for r ≥ r_e,

and g_app denotes the data (R_app, P, Q, W) on the cone.

Since T_i(−1) = (−1)^i and T_i′(−1) = (−1)^(i−1) i², the corrections are a(x) = Σ_j a_j T_j(x) and
b(x) = Σ_j b_j T_j(x) with

    a_j = r_s δ_(j0) − Σ_i (−1)^i C_(ij),      b_j = δ_(j0) − ℓ^(−1) Σ_i (−1)^(i−1) i² C_(ij),

δ_(j0) the Kronecker symbol. By construction R_app is C¹ in r: both formulas at r_s give the value r_s and the slope
1, and the last line continues the middle one to first order at r_e. Moreover ∂_r²R_app = 0 for r ∉ [r_s, r_e] and
∂_r²R_app = ∂_r²S = ℓ^(−2) ∂_t²S on (r_s, r_e). The approximant has 41 × 29 = 1,189 coefficients at the first seed and
65 × 29 = 1,885 at the second.

**Proposition {#prop:cone-residual}** (The residual of the approximant.) At each seed:

(a) Ric_vv[g_app] = 0 on the cone outside 1/2 ≤ v ≤ 7/2.

(b) For 1/2 ≤ v ≤ 7/2 and x ∈ [−1, 1] (one-sided at v = 1/2 and v = 7/2),
|Ric_vv[g_app]| ≤ 4.97 × 10⁻⁵ at the first seed and |Ric_vv[g_app]| ≤ 2.28 × 10⁻⁵ at the second.

(c) The jumps of ∂_r²R_app across v = 1/2 and across v = 7/2 are at most 3.6 × 10⁻⁸ at the first seed and at most
8.5 × 10⁻⁸ at the second.

The proof occupies the next section. It bounds the residual of the linear equation by its values at the nodes of a
Chebyshev grid: in x it uses that the residual, multiplied by 1 + x², is a polynomial of degree 30; in r it uses that
the polynomial part is reproduced exactly by interpolation and that the rest is holomorphic on an explicit ellipse.

### Proof of the residual bound {#sec:cone-residual-proof}

On [r_s, r_e] × [−1, 1] put

    ℰ := ∂_r²R_app + w R_app,      G := (1 + x²) ℰ = (1 + x²) ℓ^(−2) ∂_t²S + F,      F := (4/9) H R_app,   {#eq:cone-g}

with H as in [[eq:cone-w]]. By [[lem:cone-generator]], Ric_vv[g_app] = −(3f²/(4R_app)) ℰ wherever R_app ≠ 0.

**Lemma {#lem:cone-structure}** (Structure of G.) (a) For each r ∈ [r_s, r_e], G(r, ·) is a polynomial of degree at
most 30. (b) For each x ∈ [−1, 1], (1 + x²) ℓ^(−2) ∂_t²S is a polynomial in t of degree at most N_r − 2, and F is
the restriction to t ∈ [−1, 1] of a function holomorphic in t on the set {t : Re(c + ℓt) > 1}.

*Proof.* (a) S is a polynomial of degree 28 in x, hence so are ∂_t²S, a, b and R_app(r, ·); H is a polynomial of
degree 2 in x. (b) The first statement is clear. For the second, r ↦ v(r) extends holomorphically to Re r > 1 as
2(r − 10) + ln(11/9) + Log(r − 1) − Log(r + 1), Log the principal branch; r^(−3/2) extends as the principal branch on
Re r > 0; on [r_s, r_e], env is the restriction of the entire function sin⁴(π(v − 1/2)/3), cos θ and sin θ are
entire functions of v, and S, a, b are polynomials. ∎

**Lemma {#lem:cone-ellipse}** (F on a Bernstein ellipse.) For ϱ > 1 let E_ϱ be the closed region bounded by the
ellipse with foci ±1 and semi-axes (ϱ + ϱ^(−1))/2 and (ϱ − ϱ^(−1))/2. Take ϱ = 2 at the first seed and ϱ = 3/2 at the
second. Then for t ∈ E_ϱ and x ∈ [−1, 1], with r = c + ℓt, the holomorphic extension of F satisfies |F| ≤ M, where
M = 192.3 at the first seed and M = 7.878 at the second.

*Proof.* Let t ∈ E_ϱ and z := c + ℓt = p + iq. Then |q| ≤ η := ℓ(ϱ − ϱ^(−1))/2, |z − c| ≤ ℓ(ϱ + ϱ^(−1))/2 and
p ≥ r_− := c − ℓ(ϱ + ϱ^(−1))/2. At the first seed η ≤ 0.5579, ℓ(ϱ + ϱ^(−1))/2 ≤ 0.9298 and r_− ≥ 10.061; at the second
η ≤ 0.3100, ℓ(ϱ + ϱ^(−1))/2 ≤ 0.8058 and r_− ≥ 10.185. Put V := 2 + 2/(r_−² − 1) ≤ 2.021 (both seeds).

(i) The phase. Im v(z) = 2q + arctan(q/(p − 1)) − arctan(q/(p + 1)), and since arctan has derivative at most 1,
|arctan(q/(p − 1)) − arctan(q/(p + 1))| ≤ |q| (1/(p − 1) − 1/(p + 1)) = 2|q|/(p² − 1). So |Im v(z)| ≤ η V =: η_v,
with η_v ≤ 1.128 (first seed) and η_v ≤ 0.6266 (second). Also v′(z) = 2 + 2/(z² − 1) and |z² − 1| ≥ |z|² − 1 ≥
r_−² − 1, so |v′(z)| ≤ V.

(ii) The trigonometric factors. For complex ξ, |sin ξ| and |cos ξ| are at most cosh(Im ξ). Hence
|env(v(z))| ≤ c₄ and |d env/dv (v(z))| ≤ (4π/3) c₄, where c₄ := cosh⁴(π η_v/3) ≤ 10.1 (first seed), ≤ 2.24
(second); and |cos θ|, |sin θ| ≤ cosh(η_v/λ) ≤ 1.707 (first seed), ≤ 3.696 (second).

(iii) A and B. Here φ = (λ/2) z^(−3/2) env(v(z)), φ′ = (λ/2)(−(3/2) z^(−5/2) env + z^(−3/2) (d env/dv) v′) and
θ′ = v′/λ, with |z| ≥ p ≥ r_−. So |A| and |B| are at most (|φ′| + |φ| |θ′|) cosh(η_v/λ) ≤ Ā, where

    Ā := r_−^(−3/2) c₄ cosh(η_v/λ) ((λ/2)(3/(2r_−) + (4π/3) V) + V/2).

At the first seed r_−^(−3/2) ≤ 0.03134, the last factor is at most 5.318 and Ā ≤ 2.874; at the second
r_−^(−3/2) ≤ 0.03077, the last factor is at most 2.373 and Ā ≤ 0.6046.

(iv) R_app. Each t ∈ E_ϱ is t = (ω + ω^(−1))/2 with 1 ≤ |ω| ≤ ϱ, and T_i(t) = (ω^i + ω^(−i))/2, so |T_i(t)| ≤ ϱ^i. Also
|T_j(x)| ≤ 1 and |z − r_s| ≤ |z − c| + ℓ. So

    |R_app| ≤ Σ_(i,j) |C_(ij)| ϱ^i + Σ_j |a_j| + Σ_j |b_j| (ℓ(ϱ + ϱ^(−1))/2 + ℓ) ≤ R̄,

with R̄ = 13.089 at the first seed and R̄ = 12.122 at the second, by the sums of [[sec:cone-table-constants]].

(v) Since (1 + x)² + (1 − x²) + (1 − x)² = 3 + x² ≤ 4, |H| ≤ 4Ā², and |F| ≤ (16/9) Ā² R̄. This is at most
(16/9)(2.874)²(13.089) ≤ 192.3 at the first seed and (16/9)(0.6046)²(12.122) ≤ 7.878 at the second. ∎

The nodes of the grid are

    t_k := cos(kπ/n),  r_k := c + ℓ t_k  (0 ≤ k ≤ n),      x_l := cos(lπ/30)  (0 ≤ l ≤ 30),

with n := 40 at the first seed and n := 64 at the second.

**Lemma {#lem:cone-nodes}** (Values at the nodes.) For 0 ≤ k ≤ n and 0 ≤ l ≤ 30, |G(r_k, x_l)| ≤ ε_k, where ε_k is
the entry of row k of [[sec:cone-table-n1]] (first seed) or [[sec:cone-table-n2]] (second seed). In particular
|G(r_k, x_l)| ≤ ε_* at every node, with ε_* = 1.5 × 10⁻⁸ at the first seed and ε_* = 7.4 × 10⁻⁸ at the second.

*Proof.* Each row is a finite evaluation, which a reader can repeat by hand. At a node, T_i(t_k) = cos(ikπ/n) and
T_j(x_l) = cos(jlπ/30); with ψ := kπ/n,

    T_i″(cos ψ) = (i cos ψ sin(iψ) − i² sin ψ cos(iψ))/sin³ψ   (0 < k < n),      T_i″(±1) = (±1)^i i²(i² − 1)/3.

So G(r_k, x_l) = (1 + x_l²) ℓ^(−2) Σ_(i,j) C_(ij) T_i″(t_k) T_j(x_l) + (4/9) H(r_k, x_l) R_app(r_k, x_l) is a finite
sum of products of the tabulated coefficients with values of sin, cos, ln and square roots at explicit points:
H(r_k, x_l) by [[eq:cone-data]] and [[eq:cone-w]], R_app(r_k, x_l) by [[eq:cone-approximant]] and the formulas for a_j
and b_j. The two terms of G are at most 3.1 × 10⁻² (first seed) and 1.5 × 10⁻² (second seed) in modulus, and they
cancel. Evaluated at the 31 points x_l, they give the moduli whose largest value, rounded up, is the entry ε_k. Only
ε_* is used below; to confirm |G(r_k, x_l)| ≤ ε_* at a node it suffices to evaluate the two terms with absolute error
below 10⁻⁹. ∎

We use two results on polynomial interpolation in the Chebyshev points cos(kπ/n), 0 ≤ k ≤ n. For a continuous g on
[−1, 1], I_n g denotes the polynomial of degree at most n that equals g at these n + 1 points; I_n g = g when g is a
polynomial of degree at most n, and I_n is linear.

- (I1) [Tre19, Theorem 15.2]: the Lebesgue constant Λ_n of these points, the norm of I_n on C[−1, 1], satisfies
  Λ_n ≤ (2/π) ln(n + 1) + 1. So |I_n g| ≤ Λ_n max_k |g(cos(kπ/n))| on [−1, 1].
- (I2) [Tre19, Theorem 8.2]: if g is analytic in the open region bounded by the ellipse of [[lem:cone-ellipse]] with
  parameter ϱ > 1, and |g| ≤ M there, then |g − I_n g| ≤ 4M ϱ^(−n)/(ϱ − 1) on [−1, 1].

In particular Λ_30 ≤ 3.19, Λ_40 ≤ 3.37 and Λ_64 ≤ 3.66.

**Lemma {#lem:cone-residual-bound}** (The residual of the linear equation.) On [r_s, r_e] × [−1, 1],

    |ℰ| ≤ |G| ≤ ℰ̄ := Λ_30 (Λ_n ε_* + 4M ϱ^(−n)/(ϱ − 1)),

and ℰ̄ ≤ 1.7 × 10⁻⁷ at the first seed and ℰ̄ ≤ 8.7 × 10⁻⁷ at the second.

*Proof.* The first inequality holds because 1 + x² ≥ 1. Fix r ∈ [r_s, r_e]. By [[lem:cone-structure]] (a), G(r, ·)
is a polynomial of degree at most 30, so it equals its interpolant in the points x_l, and by (I1) with n = 30,
|G(r, x)| ≤ Λ_30 max_l |G(r, x_l)|. Now fix l and put g_l(t) := G(c + ℓt, x_l) for t ∈ [−1, 1]. By [[eq:cone-g]],
g_l = P_l + F_l, where P_l := (1 + x_l²) ℓ^(−2) ∂_t²S(·, x_l) is a polynomial of degree at most N_r − 2 ≤ n and
F_l(t) := F(c + ℓt, x_l). So I_n P_l = P_l and g_l − I_n g_l = F_l − I_n F_l. By [[lem:cone-structure]] (b) and
[[lem:cone-ellipse]], F_l is holomorphic on a neighbourhood of E_ϱ (whose points have Re(c + ℓt) ≥ r_− > 1) and
bounded there by M, so (I2) gives |F_l − I_n F_l| ≤ 4M ϱ^(−n)/(ϱ − 1). By (I1) and [[lem:cone-nodes]],
|I_n g_l| ≤ Λ_n max_k |g_l(t_k)| ≤ Λ_n ε_*. Hence |g_l| ≤ Λ_n ε_* + 4M ϱ^(−n)/(ϱ − 1) on [−1, 1], for every l,
and the bound on G follows. At the first seed 4M ϱ^(−n)/(ϱ − 1) = 4(192.3) 2^(−40) ≤ 7.0 × 10⁻¹⁰ and
ℰ̄ ≤ 3.19 (3.37 × 1.5 × 10⁻⁸ + 7.0 × 10⁻¹⁰) ≤ 1.7 × 10⁻⁷. At the second, 8(7.878)(2/3)^64 ≤ 3.4 × 10⁻¹⁰ and
ℰ̄ ≤ 3.19 (3.66 × 7.4 × 10⁻⁸ + 3.4 × 10⁻¹⁰) ≤ 8.7 × 10⁻⁷. ∎

*Proof of [[prop:cone-residual]].* Let W̄ be as in [[lem:cone-w]] and R̄ as in [[lem:cone-ellipse]] (iv), which
bounds R_app also for real t ∈ [−1, 1] ⊂ E_ϱ. On [r_s, r_e] × [−1, 1], ∂_r²R_app = ℰ − w R_app, so by
[[lem:cone-residual-bound]] and [[lem:cone-w]]

    |∂_r²R_app| ≤ K := ℰ̄ + W̄ R̄,      K ≤ 0.0261 (first seed),  K ≤ 0.0104 (second seed).

Since R_app(r_s, x) = r_s and ∂_rR_app(r_s, x) = 1,

    R_app(r, x) − r = ∫_(r_s)^r (r − q) ∂_r²R_app(q, x) dq ≥ −K (r − r_s)²/2,

so R_app(r, x) ≥ r_s + (r − r_s)(1 − Kℓ) ≥ r_s on [r_s, r_e], as Kℓ ≤ 0.02. Also
∂_rR_app(r_e, x) ≥ 1 − 2ℓK ≥ 0.96.

(a) For 10 ≤ r < r_s, R_app = r, so ∂_r²R_app = 0, and w = 0 by [[lem:cone-generator]]. For r > r_e, ∂_r²R_app = 0
and w = 0, and R_app ≥ R_app(r_e, x) ≥ r_s > 0 since R_app increases there. In both cases [[eq:cone-ricvv]] gives
Ric_vv[g_app] = 0.

(b) On [r_s, r_e], f² ≤ (1 − r_e^(−2))² and R_app ≥ r_s, so by [[eq:cone-ricvv]] and [[lem:cone-residual-bound]]

    |Ric_vv[g_app]| ≤ (3 (1 − r_e^(−2))²/(4 r_s)) ℰ̄ ≤ 0.0722 ℰ̄.

This is at most 0.0722 × 1.7 × 10⁻⁷ ≤ 1.3 × 10⁻⁸ ≤ 4.97 × 10⁻⁵ at the first seed, and at most
0.0722 × 8.7 × 10⁻⁷ ≤ 6.3 × 10⁻⁸ ≤ 2.28 × 10⁻⁵ at the second.

(c) For r < r_s and for r > r_e, ∂_r²R_app = 0. Since T_i″(±1) = (±1)^i i²(i² − 1)/3, the one-sided values at the
ends are

    ∂_r²R_app(r_s+, x) = Σ_j δ^s_j T_j(x),      ∂_r²R_app(r_e−, x) = Σ_j δ^e_j T_j(x),
    δ^s_j := ℓ^(−2) Σ_i (−1)^i (i²(i² − 1)/3) C_(ij),      δ^e_j := ℓ^(−2) Σ_i (i²(i² − 1)/3) C_(ij).

As |T_j| ≤ 1 on [−1, 1], the jumps are at most Σ_j |δ^s_j| and Σ_j |δ^e_j|. By [[sec:cone-table-jumps]] these are at
most 2.55 × 10⁻⁸ and 2.72 × 10⁻⁸ at the first seed, and 6.84 × 10⁻⁸ and 7.29 × 10⁻⁸ at the second. ∎

The proof gives more than the proposition states: |Ric_vv[g_app]| ≤ 1.3 × 10⁻⁸ at the first seed and
≤ 6.3 × 10⁻⁸ at the second, against terms of size up to s̄ that cancel in Ric_vv.

### Exact data on the cone {#sec:cone-exact}

**Proposition {#prop:cone-exact}** (Exact data.) Fix a seed and x ∈ [−1, 1]. There is exactly one function
R(·, x) ∈ C²([10, ∞)) with R(r, x) = r for 10 ≤ r ≤ r_s and

    ∂_r²R = −(4/(3f²)) R s      on [10, ∞).                                                                {#eq:cone-ode}

With W̄ as in [[lem:cone-w]] it satisfies:

(a) for r_s ≤ r ≤ r_e, 0 ≤ r − R(r, x) ≤ W̄ r (r − r_s)²/2 and 1 − W̄ (r² − r_s²)/2 ≤ ∂_rR(r, x) ≤ 1; so
r − R ≤ 0.0259 and ∂_rR ≥ 0.967 at the first seed, and r − R ≤ 0.0112 and ∂_rR ≥ 0.986 at the second;

(b) for r ≥ r_e, R(r, x) = R(r_e, x) + ∂_rR(r_e, x)(r − r_e), so 0 ≤ r − R(r, x) ≤ 0.0259 + 0.0326 (r − r_e) at the
first seed and 0 ≤ r − R(r, x) ≤ 0.0112 + 0.0140 (r − r_e) at the second;

(c) R > 0 on [10, ∞) × [−1, 1]; R and ∂_rR are continuous there, and R is C^∞ in x.

The data (R, P, Q, W) therefore satisfy the Raychaudhuri constraint exactly: Ric_vv[R] = 0 on the whole cone, by
[[eq:cone-ricvv]]. The constraint Ric_vx, which determines the shift on the cone, is not treated here.

*Proof.* By [[lem:cone-generator]], [[eq:cone-ode]] is ∂_r²R = −w R, with w continuous on [10, ∞) × [−1, 1] and zero
outside (r_s, r_e). On [10, r_s] the function R = r solves it. On [r_s, ∞) the linear equation ∂_r²R = −w R with
R(r_s) = r_s and ∂_rR(r_s) = 1 has exactly one C² solution, and the two pieces join to a C² function because
w(r_s, x) = 0. Any solution equal to r on [10, r_s] has these values at r_s, which gives uniqueness.

For the bounds we compare with the solution r of ∂_r²R = 0. Let r₁ be the supremum of the r₁′ ∈ (r_s, r_e] with
R > 0 on [r_s, r₁′]. On [r_s, r₁), ∂_r²R = −w R ≤ 0, so ∂_rR ≤ 1 and R ≤ r; hence 0 ≤ w R ≤ W̄ q at every
q ∈ [r_s, r₁), and

    ∂_rR(r) = 1 − ∫_(r_s)^r w R dq ≥ 1 − W̄ (r² − r_s²)/2,      r − R(r) = ∫_(r_s)^r (r − q) w R dq ∈ [0, W̄ r (r − r_s)²/2].

So R(r) ≥ r (1 − W̄ (r − r_s)²/2) ≥ r (1 − 2ℓ² W̄) on [r_s, r₁), and 2ℓ² W̄ ≤ 0.0023. If r₁ < r_e, continuity would
give R(r₁) > 0 and R > 0 beyond r₁, against the definition of r₁; so r₁ = r_e and the bounds hold on [r_s, r_e]. With
r ≤ r_e, (r − r_s)²/2 ≤ 2ℓ² ≤ 1.1064 and (r_e² − r_s²)/2 ≤ 16.35, they give the numbers in (a). For r ≥ r_e, w = 0,
so R is affine with slope ∂_rR(r_e, x) ∈ [0.967, 1] (first seed) or [0.986, 1] (second), which gives (b) and R > 0
there; on [10, r_s], R = r > 0.

For the regularity, R(r, x) = r − ∫_(r_s)^r (r − q) w(q, x) R(q, x) dq on [r_s, r_e]. By [[eq:cone-w]], w is
continuous on [r_s, r_e] × [−1, 1] and smooth in x, with every x-derivative continuous (it is a polynomial in x
divided by 1 + x²). The Picard iterates of this integral equation and all their x-derivatives converge uniformly on
[r_s, r_e] × [−1, 1]: by induction on k, the m-th x-derivative of the k-th increment is bounded by
C_m D_m^k (r − r_s)^(2k)/(2k)! for constants C_m and D_m. So R and ∂_rR are continuous and R is C^∞ in x on [r_s, r_e] × [−1, 1], and then on
[10, ∞) × [−1, 1] by the explicit formulas on the other two intervals. ∎

**Corollary {#cor:cone-compare}** (The approximant and the exact data.) With R as in [[prop:cone-exact]] and ℰ̄ as in
[[lem:cone-residual-bound]], put Δ := 2ℓ² ℰ̄/(1 − 2ℓ² W̄). On [r_s, r_e] × [−1, 1]

    |R_app − R| ≤ Δ,      |∂_r(R_app − R)| ≤ 2ℓ (ℰ̄ + W̄ Δ),

that is, |R_app − R| ≤ 1.9 × 10⁻⁷ and |∂_r(R_app − R)| ≤ 2.6 × 10⁻⁷ at the first seed, and |R_app − R| ≤ 9.7 × 10⁻⁷
and |∂_r(R_app − R)| ≤ 1.3 × 10⁻⁶ at the second. For r ≤ r_s, R_app = R; for r ≥ r_e both are affine in r, so
|R_app − R| grows at most linearly, with these values and slopes at r_e.

*Proof.* D := R_app − R satisfies D(r_s, x) = ∂_rD(r_s, x) = 0 and, on [r_s, r_e], ∂_r²D = (ℰ − w R_app) + w R =
ℰ − w D. Let Δ₀ := max |D| over [r_s, r_e] × [−1, 1]. Then |D(r, x)| ≤ ∫_(r_s)^r (r − q)(ℰ̄ + W̄ Δ₀) dq ≤
2ℓ²(ℰ̄ + W̄ Δ₀), so Δ₀ (1 − 2ℓ² W̄) ≤ 2ℓ² ℰ̄, that is Δ₀ ≤ Δ; and |∂_rD| ≤ ∫_(r_s)^r (ℰ̄ + W̄ Δ₀) dq ≤
2ℓ(ℰ̄ + W̄ Δ). The numbers follow
from [[lem:cone-w]], [[lem:cone-residual-bound]], 2ℓ² ≤ 1.1064 and 2ℓ ≤ 1.4876. ∎
