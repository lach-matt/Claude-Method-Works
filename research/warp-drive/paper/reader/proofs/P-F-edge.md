### The hypotheses for the envelope of the constants {#sec:edge-envelope}

[[thm:very-edge]] and the proposition on the crossover windows [[pending:edge-crossover-proposition]] place a list of
hypotheses on the envelope near its left edge v_s := inf supp env. This section proves every one of them, for every
K ≥ 6, for the envelope with which the constants are computed,

    env(v) = c_e cos¹²(πy/2) exp(−y²/(1 − y²)),   y := (2v − 4)/3,   for 1/2 < v < 7/2,              {#eq:edge-envelope}

env = 0 elsewhere, with c_e > 0 its normalising constant and v_s = 1/2, and for the model edge env(v) = exp(−1/(v − v_s))
for v > v_s. We write x := v − v_s, ℓ := log env, κ := ℓ′ (a prime is d/dv = d/dx), and where env^(k) > 0,
κ_k := (log env^(k))′ = env^(k+1)/env^(k), so κ_0 = κ. With α ∈ (0, 1), positive constants c_R, c_j, c_t, c_* and an
interval (v_s, v_s + x0], the hypotheses are:

    (H_N)     for k ≤ N: env^(k) > 0 and log-concave, 1/2 ≤ κ_k/κ ≤ 2 and |κ_k′| ≤ c_R κ_k^(1+α);
              for j ≤ N + 2: |env^(j)| ≤ c_j κ^j env;
    (H_N+2)   (H_N) with N + 2 in place of N and the same α;
    (H_t)     κ − κ_(N−1) ≥ c_t κ^α;
    (H_D)     κ(v_s + y/2) κ(v_s + 4y)^c env(v_s + 4y) → 0 as y ↓ 0, for every c > 0;
    (H_*)     κ(v)(v − v_s)² ≥ c_*  (the bound used at ρ0 = ρ*).

The proof reduces all of them to one recursion for x²κ_k, controlled on complex discs.

**Lemma {#lem:edge-logderivatives}** (the logarithmic derivatives). Let env be smooth and positive on an interval
I ⊂ (v_s, ∞), put R_0 := x²κ, and as long as R_k has no zero on I put

    R_(k+1) := R_k − 2x + x² R_k′/R_k.                                                              {#eq:edge-recursion}

Suppose R_0, …, R_m are positive on I. Then on I:
(a) env^(k) = env x^(−2k) R_0 R_1 ⋯ R_(k−1) > 0 for k ≤ m + 1, and κ_k = R_k/x² for k ≤ m;
(b) κ_k/κ = R_k/R_0 for k ≤ m, and env^(j)/(κ^j env) = Π_(i<j) R_i/R_0 for j ≤ m + 1;
(c) for k ≤ m − 1, κ_k′ = R_k (R_(k+1) − R_k)/x⁴; so env^(k) is strictly log-concave where R_(k+1) < R_k, and there
    |κ_k′| ≤ c κ_k^(3/2) exactly where R_k − R_(k+1) ≤ c x R_k^(1/2);
(d) κ′ = −(2R_0 − xR_0′)/x³, so |κ′| ≥ c κ^(3/2) exactly where 2R_0 − xR_0′ ≥ c R_0^(3/2) > 0;
(e) if n ≤ m − 1 and env^(k) is strictly log-concave for every k ≤ n − 1, then κ − κ_n ≥ κ − κ_1 = |κ′|/κ.

*Proof.* (a) By induction on k; k = 0 is trivial. Suppose env^(k) = env E_k with E_k := x^(−2k) Π_(i<k) R_i and k ≤ m.
Then env^(k+1) = env E_k (κ + E_k′/E_k) and κ + E_k′/E_k = R_0/x² − 2k/x + Σ_(i<k) R_i′/R_i. By [[eq:edge-recursion]],
R_i′/R_i − 2/x = (R_(i+1) − R_i)/x², and the sum telescopes: κ + E_k′/E_k = R_k/x². Hence env^(k+1) = env E_k R_k/x² =
env E_(k+1) > 0 and κ_k = env^(k+1)/env^(k) = R_k/x². (b) follows from (a), since κ^j env = R_0^j x^(−2j) env.
(c) Differentiating env^(k+1) = κ_k env^(k) gives env^(k+2) = (κ_k′ + κ_k²) env^(k), so κ_k′ = κ_k κ_(k+1) − κ_k² =
κ_k (κ_(k+1) − κ_k), which is R_k (R_(k+1) − R_k)/x⁴ by (a). As κ_k > 0, (log env^(k))″ = κ_k′ < 0 exactly where
R_(k+1) < R_k, and then |κ_k′| = R_k (R_k − R_(k+1))/x⁴ ≤ c R_k^(3/2)/x³ = c κ_k^(3/2) exactly where R_k − R_(k+1) ≤
c x R_k^(1/2). (d) κ = R_0/x². (e) κ − κ_n = Σ_(k<n) (κ_k − κ_(k+1)), each term is positive by (c), and the term k = 0
is κ − κ_1 = −κ′/κ by (c). ∎

### The two envelopes near the edge {#sec:edge-envelope-a}

**Lemma {#lem:edge-a}** (the function x²κ). For exp(−1/x), x²κ = 1. For [[eq:edge-envelope]], on 0 < x < 3,

    x²κ = A(x) := 3/4 − (3/4)(x/(3 − x))² + 4πx² cot(πx/3),                                         {#eq:edge-a}

and A extends holomorphically to the disc |z| < 3. With Ê(r) := (3/4)(r/(3 − r))² + (4π²/9) r³/(1 − r²/9), for
complex z with |z| ≤ r ≤ 1/100,

    |A(z) − 3/4 − 12z| ≤ Ê(r) ≤ r²/7,      |A′(z) − 12| ≤ Ê′(r) ≤ r/2,                               {#eq:edge-a-disc}

and for real 0 < x ≤ 1/100,

    3/4 + 12x − x²/7 ≤ A(x) ≤ 3/4 + 12x,      12 − x/2 ≤ A′(x) ≤ 12.                                {#eq:edge-a-real}

*Proof.* Put t := 2x/3 = 1 + y. Then cos(πy/2) = sin(πt/2) = sin(πx/3), and y²/(1 − y²) = 1/(t(2 − t)) − 1, since
t(2 − t) + (1 − t)² = 1; moreover 1/(t(2 − t)) = (1/2)(1/t + 1/(2 − t)) = (3/4)(1/x + 1/(3 − x)). So for 0 < x < 3

    ℓ = log c_e + 1 + 12 log sin(πx/3) − (3/4)(1/x + 1/(3 − x)),                                     {#eq:edge-log}

and κ = 4π cot(πx/3) + (3/4)(1/x² − 1/(3 − x)²), which is [[eq:edge-a]] after multiplication by x². For exp(−1/x),
κ = 1/x². Put w := πz/3 and E(z) := 3/4 + 12z − A(z) = (3/4)(z/(3 − z))² + 4πz²(1/w − cot w), using 12z = 4πz²/w.
For |w| < π the partial fractions of the cotangent give

    1/w − cot w = Σ_(j≥1) 2w/(j²π² − w²) = Σ_(n≥1) (2ζ(2n)/π^(2n)) w^(2n−1),

so A is holomorphic on |z| < 3, and every Taylor coefficient of E at 0 is nonnegative, (z/(3 − z))² being
Σ_(m≥2) (m − 1) z^m/3^m. Since 2ζ(2n) ≤ 2ζ(2) = π²/3, the coefficients of 1/w − cot w are at most those of
Σ_(n≥1) (π²/3) w^(2n−1)/π^(2n) = (w/3)/(1 − w²/π²); with w = πz/3, those of 4πz²(1/w − cot w) are at most those of
(4π²/9) z³/(1 − z²/9). So the Taylor coefficients of E lie between 0 and those of Ê. Hence |E(z)| ≤ Ê(|z|) and
|E′(z)| ≤ Ê′(|z|) for |z| < 3, and 0 ≤ E(x) ≤ Ê(x), 0 ≤ E′(x) ≤ Ê′(x) for 0 < x < 3. It remains to bound Ê and Ê′ for
r ≤ 1/100. There (3 − r)² ≥ 8.94, (3 − r)³ ≥ 26.7, 1 − r²/9 ≥ 0.9999, and π² ≤ 10, so 4π²/9 ≤ 4.45 and

    Ê(r) ≤ (0.75/8.94) r² + (4.45/0.9999) r³ ≤ 0.0839 r² + 0.0446 r² < r²/7,
    Ê′(r) = (9/2) r/(3 − r)³ + (4π²/9)(3r² − r⁴/9)/(1 − r²/9)² ≤ 0.1686 r + 13.4 r² ≤ 0.303 r < r/2.  ∎

**Lemma {#lem:edge-disc}** (the recursion on a disc). Let a ∈ [3/4, 1], 0 ≤ α′ ≤ 13 and n ≥ 1 an integer, and put
ρ := 1/(24(n + 2)²) and ρ_k := ρ(1 − k/(2(n + 2))). Let A be holomorphic on an open set containing the closed disc
D := {|z| ≤ ρ}, with |A| ≥ 7a/8 and |A′| ≤ α′ on D. Let R_0 := A and define R_(k+1) by [[eq:edge-recursion]] with z
in place of x. Then for 0 ≤ k ≤ n + 1, R_k is holomorphic on an open set containing D_k := {|z| ≤ ρ_k}, and on D_k

    R_k = A − 2kz + z² T_k,   T_k holomorphic,   |T_k| ≤ σ_k := 2k(α′ + k)/a,   |R_k| ≥ 3a/4.         {#eq:edge-disc}

*Proof.* Induction on k. For k = 0, T_0 = 0 and |R_0| = |A| ≥ 7a/8. Suppose [[eq:edge-disc]] holds for some k ≤ n.
As R_k has no zero on D_k, R_(k+1) is holomorphic there, and since R_(k+1) − A + 2(k + 1)z = z²T_k + z² R_k′/R_k,

    T_(k+1) = T_k + R_k′/R_k.

Let |z| ≤ ρ_(k+1) and h := ρ_k − ρ_(k+1) = ρ/(2(n + 2)). The circle |w − z| = h lies in D_k, where |w² T_k(w)| ≤
σ_k ρ², so Cauchy's estimate gives |(z² T_k)′| ≤ σ_k ρ²/h = 2(n + 2)ρ σ_k, and |R_k′(z)| ≤ α′ + 2k + 2(n + 2)ρ σ_k.
With |R_k| ≥ 3a/4,

    |T_(k+1)(z)| ≤ σ_k + (4/(3a))(α′ + 2k) + (8(n + 2)ρ/(3a)) σ_k.

Here 8(n + 2)ρ σ_k/(3a) = σ_k/(9a(n + 2)) = 2k(α′ + k)/(9a²(n + 2)) ≤ (8/27)(α′ + k)/a, since k < n + 2 and 1/a ≤ 4/3.
So |T_(k+1)| ≤ σ_k + (44/27)(α′ + 2k)/a ≤ σ_k + 2(α′ + 2k + 1)/a = σ_(k+1). Finally, on D_(k+1), |R_(k+1)| ≥ |A| −
2(k + 1)ρ − σ_(k+1) ρ², and since k + 1 ≤ n + 1, a ≥ 3/4 and α′ ≤ 13,

    2(k + 1)ρ ≤ (n + 1)/(12(n + 2)²) ≤ 1/36,      σ_(k+1) ρ² ≤ (n + 1)(n + 14)/(216(n + 2)⁴) ≤ 15/(216 · 27) < 1/388,

so |R_(k+1)| ≥ 7a/8 − 1/36 − 1/388 > 7a/8 − 0.031 ≥ 7a/8 − a/8 = 3a/4, as a/8 ≥ 3/32 > 0.031. ∎

### The hypotheses, for every K {#sec:edge-envelope-every-k}

**Proposition {#prop:edge-envelope}** (the hypotheses for the envelope of the constants). Let env be
[[eq:edge-envelope]], or exp(−1/(v − v_s)); let n ≥ 1 be an integer and x_n := 1/(96(n + 2)²). Then:
(a) on (v_s, v_s + x_n], env^(k) > 0 for k ≤ n + 2, and |env^(j)| ≤ κ^j env for j ≤ n + 2;
(b) on (v_s, v_s + x_n], for every k ≤ n, env^(k) is strictly log-concave, 99/100 ≤ κ_k/κ ≤ 1 and
    |κ_k′| ≤ c_R κ_k^(3/2), with c_R = 12/5 for [[eq:edge-envelope]] and c_R = 21/10 for exp(−1/(v − v_s));
(c) on (v_s, v_s + 1/200], |κ′| ≥ c_t κ^(3/2) with c_t = 2.139, resp. c_t = 2, and 3/4 ≤ κx² ≤ 81/100, resp. κx² = 1;
(d) (H_D) holds for every c > 0.

*Proof.* Let A := x²κ, so A = 1 for exp(−1/x) and A is [[eq:edge-a]] for [[eq:edge-envelope]], and put a := 1, resp.
a := 3/4. For [[eq:edge-envelope]], on D, ρ = 1/(24(n + 2)²) ≤ 1/216, [[eq:edge-a-disc]] gives |A − 3/4| ≤ 12ρ + ρ²/7 ≤
0.056 < 3/32, so |A| ≥ 21/32 = 7a/8, and |A′| ≤ 12 + ρ/2 ≤ 13. So [[lem:edge-disc]] applies, with α′ := 13, resp.
α′ := 0. Fix 0 < x ≤ x_n = ρ/4 and k ≤ n + 1. T_k is holomorphic on the disc of radius ρ_(n+1) ≥ ρ/2 about 0, which
contains the disc of radius ρ/4 about x, so |T_k(x)| ≤ σ_k and, by Cauchy's estimate, |T_k′(x)| ≤ 4σ_k/ρ ≤ σ_k/x.
Hence, R_k being real on the real axis,

    |R_k(x) − A(x) + 2kx| ≤ σ_k x²,      |x R_k′(x) − x A′(x) + 2kx| ≤ |x(2x T_k + x² T_k′)| ≤ 3σ_k x².

For both envelopes σ_k x ≤ 2(n + 1)(n + 14)/((3/4) · 96 (n + 2)²) ≤ (n + 14)/(36(n + 2)) ≤ 15/108 < 1/7 and 2kx ≤
2(n + 1)/(96(n + 2)²) ≤ 1/144; and A(x) ≥ a by [[eq:edge-a-real]]. Therefore

    R_k(x) ≥ a − 1/144 − x/7 ≥ a − 1/140 > 0,      R_k(x) − A(x) ≤ x(1/7 − 2k) < 0   for k ≥ 1,

the first because x ≤ x_1 = 1/864 and 1/144 + 1/6048 < 1/140. So [[lem:edge-logderivatives]] applies on (0, x_n]
with m = n + 1. By its (a), env^(k) > 0 for k ≤ n + 2. By (b), κ_k/κ = R_k/A lies in [1 − 1/(140a), 1] ⊂ [99/100, 1],
since 4/(3 · 140) < 1/100, and env^(j)/(κ^j env) = Π_(i<j) R_i/A ∈ (0, 1] for j ≤ n + 2. This is (a) and the bounds of
κ_k/κ in (b). For the rest of (b), |A′(x)| ≤ 12 by [[eq:edge-a-real]] (A′ = 0 for exp(−1/x)), so

    |x R_k′(x)| ≤ 12x + 2kx + 3σ_k x² ≤ 12/864 + 1/144 + 3/(7 · 864) < 0.0214,   resp.  1/144 + 3/(7 · 864) < 0.0075,

while R_k ≥ 0.74, resp. R_k ≥ 0.99; in both cases |x R_k′/R_k| ≤ 1/30. By [[eq:edge-recursion]], R_k − R_(k+1) =
x(2 − x R_k′/R_k) ∈ [59x/30, 61x/30] for k ≤ n. By [[lem:edge-logderivatives]] (c), env^(k) is strictly log-concave
and |κ_k′| ≤ c κ_k^(3/2) with c = (61/30) R_k^(−1/2) ≤ (61/30)/0.86 < 12/5, as √0.74 ≥ 0.86, resp.
c ≤ (61/30)/0.99 < 21/10, as √0.99 ≥ 0.99.
(c) For [[eq:edge-envelope]] and 0 < x ≤ 1/200, [[eq:edge-a-real]] gives 3/4 ≤ A ≤ 3/4 + 12x ≤ 81/100 and, as
2x²/7 ≤ 0.002x,

    2A − xA′ ≥ 3/2 + 24x − 2x²/7 − 12x ≥ 3/2 + 11.998x.

By [[lem:edge-logderivatives]] (d), |κ′|/κ^(3/2) = (2A − xA′)/A^(3/2) ≥ h(x) := (3/2 + 11.998x)/(3/4 + 12x)^(3/2). The
derivative of log h has the sign of 11.998(3/4 + 12x) − 18(3/2 + 11.998x) = −18.0015 − 71.988x < 0, so h decreases and
h(x) ≥ h(1/200) = 1.55999/0.81^(3/2) = 1.55999/0.729 > 2.139. For exp(−1/x), (2A − xA′)/A^(3/2) = 2 and κx² = 1.
(d) For 0 < x ≤ 1/200, κ = A/x² ≤ 1/x² by (c), and [[eq:edge-log]] with sin(πx/3) ≤ 1 and 1/(3 − x) > 0 gives
env(v_s + x) ≤ c_e e^(1 − 3/(4x)). So for 0 < y ≤ 1/800 and every c > 0

    κ(v_s + y/2) κ(v_s + 4y)^c env(v_s + 4y) ≤ 4y⁻² (16y²)^(−c) c_e e^(1 − 3/(16y)),

which tends to 0 as y ↓ 0, e^(−3/(16y)) decaying faster than every power of y. For exp(−1/x) the left side equals
4y⁻² (16y²)^(−c) e^(−1/(4y)), which tends to 0 likewise. ∎

**Corollary {#cor:edge-envelope}** (every hypothesis, for every K). Let env be [[eq:edge-envelope]] or exp(−1/(v − v_s)),
N ≥ 2, and x0 := x_(N+2) = 1/(96(N + 4)²). On (v_s, v_s + x0], (H_N) and (H_N+2) hold with α = 1/2, the c_R of
[[prop:edge-envelope]] and c_j = 1; (H_t) holds with c_t = 2.139, resp. 2; (H_*) holds with c_* = 3/4, resp. 1;
and (H_D) holds. So every hypothesis that [[thm:very-edge]] and [[pending:edge-crossover-proposition]] place on the
envelope holds for these two envelopes, for every K ≥ 6 (N = K + 3).

*Proof.* [[prop:edge-envelope]] with n = N + 2: (a) and (b) give, for k ≤ N + 2, env^(k) > 0, strictly log-concave,
κ_k/κ ∈ [99/100, 1] ⊂ [1/2, 2] and |κ_k′| ≤ c_R κ_k^(1+1/2), and for j ≤ N + 4, |env^(j)| ≤ κ^j env; this is (H_N+2),
which contains (H_N). As x0 ≤ 1/200, (c) gives c_t and c_*. By [[lem:edge-logderivatives]] (e) with n = N − 1, which
uses the strict log-concavity of env^(k) for k ≤ N − 2, κ − κ_(N−1) ≥ |κ′|/κ ≥ c_t κ^(1/2): this is (H_t) with
α = 1/2. (H_D) is (d). ∎

**Remark {#rem:edge-envelope-limits}** (the constants at the edge). By [[eq:edge-disc]], as x ↓ 0, R_k → A(0),
x R_k′ → 0 and (R_k − R_(k+1))/(x R_k^(1/2)) → 2A(0)^(−1/2). So on (v_s, v_s + x0] with x0 ↓ 0 the best constants
tend to κ_k/κ → 1, env^(j)/(κ^j env) → 1, and c_R, c_t → 2A(0)^(−1/2), which is 4/√3 = 2.309… for
[[eq:edge-envelope]] and 2 for exp(−1/x). The values 12/5 and 21/10 of c_R, and 2.139 of c_t on (v_s, v_s + 1/200],
are close to these limits.

**Remark {#rem:edge-sin4}** (an envelope outside the class). The envelope sin⁴(π(v − v_s)/3) for v ≥ v_s, 0 for v < v_s,
satisfies none of (H_N), N ≥ 3: near v_s it is (πx/3)⁴(1 + O(x²)), so env^(4)(v_s+) = 4!(π/3)⁴ = 8π⁴/27 while
env^(4) = 0 for v < v_s, and it is C³ and not C⁴; and κ = 4/x + O(x), κ_3 = env^(4)/env^(3) = 1/x + O(x), so
κ_3/κ → 1/4 < 1/2.
