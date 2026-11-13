### The hypotheses for the envelope of the constants {#sec:edge-envelope}

[[thm:very-edge]] and [[prop:l-26]] (the crossover windows) place a list of hypotheses on the envelope near its left
edge v_s := inf supp env. This section proves every one of them, for every K ≥ 6, for the envelope of the explicit
constants ([[ch:explicit-constants]]),

    env(v) = c_e cos¹²(πξ/2) exp(−ξ²/(1 − ξ²)),   ξ := (2v − 4)/3,   for 1/2 < v < 7/2,              {#eq:edge-envelope}

env = 0 elsewhere, with c_e > 0 the constant fixed there (its value is not used below) and v_s = 1/2, and for the model
edge env(v) = exp(−1/(v − v_s)) for v > v_s. We write x := v − v_s and κ := (log env)′ (a prime is d/dv = d/dx), and
where env^(k) > 0, κ_k := (log env^(k))′ = env^(k+1)/env^(k), so κ_0 = κ. With α ∈ (0, 1), positive constants c_R,
c_j, c_t, c_* and an interval (v_s, v_s + x0], the hypotheses are:

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
(d) κ′ = −(2R_0 − xR_0′)/x³, so |κ′|/κ^(3/2) = |2R_0 − xR_0′|/R_0^(3/2), and κ′ < 0 where 2R_0 − xR_0′ > 0;
(e) if 1 ≤ n ≤ m − 1 and env^(k) is strictly log-concave for every k ≤ n − 1, then κ − κ_n ≥ κ − κ_1 = |κ′|/κ.

*Proof.* (a) By induction on k; k = 0 is trivial. Suppose env^(k) = env 𝒫_k with 𝒫_k := x^(−2k) Π_(i<k) R_i and k ≤ m.
Then env^(k+1) = env 𝒫_k (κ + 𝒫_k′/𝒫_k) and κ + 𝒫_k′/𝒫_k = R_0/x² − 2k/x + Σ_(i<k) R_i′/R_i. By [[eq:edge-recursion]],
R_i′/R_i − 2/x = (R_(i+1) − R_i)/x², and the sum telescopes: κ + 𝒫_k′/𝒫_k = R_k/x². Hence env^(k+1) = env 𝒫_k R_k/x² =
env 𝒫_(k+1) > 0 and κ_k = env^(k+1)/env^(k) = R_k/x². (b) follows from (a), since κ^j env = R_0^j x^(−2j) env.
(c) Differentiating env^(k+1) = κ_k env^(k) gives env^(k+2) = (κ_k′ + κ_k²) env^(k), so κ_k′ = κ_k κ_(k+1) − κ_k² =
κ_k (κ_(k+1) − κ_k), which is R_k (R_(k+1) − R_k)/x⁴ by (a). As κ_k > 0, (log env^(k))″ = κ_k′ < 0 exactly where
R_(k+1) < R_k, and then |κ_k′| = R_k (R_k − R_(k+1))/x⁴ ≤ c R_k^(3/2)/x³ = c κ_k^(3/2) exactly where R_k − R_(k+1) ≤
c x R_k^(1/2). (d) κ = R_0/x² gives κ′ = R_0′/x² − 2R_0/x³ and κ^(3/2) = R_0^(3/2)/x³. (e) κ − κ_n = Σ_(k<n)
(κ_k − κ_(k+1)), each term is positive by (c), and the term k = 0 is κ − κ_1 = −κ′/κ by (c). ∎

### The two envelopes near the edge {#sec:edge-envelope-a}

**Lemma {#lem:edge-a}** (the function x²κ). For exp(−1/x), R_0 = x²κ = 1. For [[eq:edge-envelope]], on 0 < x < 3,

    R_0(x) = x²κ = 3/4 − (3/4)(x/(3 − x))² + 4πx² cot(πx/3),                                       {#eq:edge-a}

and R_0 extends holomorphically to the disc |z| < 3. With Ê(r) := (3/4)(r/(3 − r))² + (4π²/9) r³/(1 − r²/9), for
complex z with |z| ≤ r ≤ 1/100,

    |R_0(z) − 3/4 − 12z| ≤ Ê(r) ≤ r²/7,      |R_0′(z) − 12| ≤ Ê′(r) ≤ r/2,                         {#eq:edge-a-disc}

and for real 0 < x ≤ 1/100,

    3/4 + 12x − x²/7 ≤ R_0(x) ≤ 3/4 + 12x,      12 − x/2 ≤ R_0′(x) ≤ 12.                          {#eq:edge-a-real}

*Proof.* Put t := 2x/3 = 1 + ξ. Then cos(πξ/2) = sin(πt/2) = sin(πx/3), and ξ²/(1 − ξ²) = 1/(t(2 − t)) − 1, since
t(2 − t) + (1 − t)² = 1; moreover 1/(t(2 − t)) = (1/2)(1/t + 1/(2 − t)) = (3/4)(1/x + 1/(3 − x)). So for 0 < x < 3

    log env = log c_e + 1 + 12 log sin(πx/3) − (3/4)(1/x + 1/(3 − x)),                               {#eq:edge-log}

and κ = 4π cot(πx/3) + (3/4)(1/x² − 1/(3 − x)²), which is [[eq:edge-a]] after multiplication by x². For exp(−1/x),
κ = 1/x². Put w := πz/3 and E(z) := 3/4 + 12z − R_0(z) = (3/4)(z/(3 − z))² + 4πz²(1/w − cot w), using 12z = 4πz²/w.
For |w| < π the partial fractions of the cotangent give

    1/w − cot w = Σ_(j≥1) 2w/(j²π² − w²) = Σ_(n≥1) (2ζ(2n)/π^(2n)) w^(2n−1),

so R_0 is holomorphic on |z| < 3, and every Taylor coefficient of E at 0 is nonnegative, (z/(3 − z))² being
Σ_(m≥2) (m − 1) z^m/3^m. Since 2ζ(2n) ≤ 2ζ(2) = π²/3, the coefficients of 1/w − cot w are at most those of
Σ_(n≥1) (π²/3) w^(2n−1)/π^(2n) = (w/3)/(1 − w²/π²); with w = πz/3, those of 4πz²(1/w − cot w) are at most those of
(4π²/9) z³/(1 − z²/9). So the Taylor coefficients of E lie between 0 and those of Ê. Hence |E(z)| ≤ Ê(|z|) and
|E′(z)| ≤ Ê′(|z|) for |z| < 3, and 0 ≤ E(x) ≤ Ê(x), 0 ≤ E′(x) ≤ Ê′(x) for 0 < x < 3. It remains to bound Ê and Ê′ for
r ≤ 1/100. There (3 − r)² ≥ 8.94, (3 − r)³ ≥ 26.7, 1 − r²/9 ≥ 0.9999, and π² ≤ 10, so 4π²/9 ≤ 4.45 and

    Ê(r) ≤ (0.75/8.94) r² + (4.45/0.9999) r³ ≤ 0.0839 r² + 0.0446 r² < r²/7,
    Ê′(r) = (9/2) r/(3 − r)³ + (4π²/9)(3r² − r⁴/9)/(1 − r²/9)² ≤ 0.1686 r + 13.4 r² ≤ 0.303 r < r/2.  ∎

**Lemma {#lem:edge-disc}** (the recursion on a disc). Let a ∈ [3/4, 1], 0 ≤ c_d ≤ 13 and n ≥ 1 an integer, and put
ϱ := 1/(24(n + 2)²) and ϱ_k := ϱ(1 − k/(2(n + 2))). Let R_0 be holomorphic on an open set containing the closed disc
𝔻 := {|z| ≤ ϱ}, with |R_0| ≥ 7a/8 and |R_0′| ≤ c_d on 𝔻, and define R_(k+1) by [[eq:edge-recursion]] with z in place
of x. Then for 0 ≤ k ≤ n + 1, R_k is holomorphic on an open set containing 𝔻_k := {|z| ≤ ϱ_k}, and on 𝔻_k

    R_k = R_0 − 2kz + z² 𝒯_k,   𝒯_k holomorphic,   |𝒯_k| ≤ ℬ_k := 2k(c_d + k)/a,   |R_k| ≥ 3a/4.      {#eq:edge-disc}

*Proof.* Induction on k. For k = 0, 𝒯_0 = 0 and |R_0| ≥ 7a/8. Suppose [[eq:edge-disc]] holds for some k ≤ n.
As R_k has no zero on 𝔻_k, R_(k+1) is holomorphic there, and since R_(k+1) − R_0 + 2(k + 1)z = z²𝒯_k + z² R_k′/R_k,

    𝒯_(k+1) = 𝒯_k + R_k′/R_k.

Let |z| ≤ ϱ_(k+1). The closed disc of radius ϱ_k − ϱ_(k+1) = ϱ/(2(n + 2)) about z lies in 𝔻_k, on which the function
z²𝒯_k is bounded by ℬ_k ϱ², so Cauchy's estimate gives |(z²𝒯_k)′(z)| ≤ 2(n + 2)ϱ ℬ_k, and |R_k′(z)| ≤ c_d + 2k +
2(n + 2)ϱ ℬ_k. With |R_k| ≥ 3a/4,

    |𝒯_(k+1)(z)| ≤ ℬ_k + (4/(3a))(c_d + 2k) + (8(n + 2)ϱ/(3a)) ℬ_k.

Here 8(n + 2)ϱ ℬ_k/(3a) = ℬ_k/(9a(n + 2)) = 2k(c_d + k)/(9a²(n + 2)) ≤ (8/27)(c_d + k)/a, since k < n + 2 and
1/a ≤ 4/3. So |𝒯_(k+1)| ≤ ℬ_k + (44/27)(c_d + 2k)/a ≤ ℬ_k + 2(c_d + 2k + 1)/a = ℬ_(k+1). Finally, on 𝔻_(k+1),
|R_(k+1)| ≥ |R_0| − 2(k + 1)ϱ − ℬ_(k+1) ϱ², and since k + 1 ≤ n + 1, a ≥ 3/4 and c_d ≤ 13,

    2(k + 1)ϱ ≤ (n + 1)/(12(n + 2)²) ≤ 1/36,      ℬ_(k+1) ϱ² ≤ (n + 1)(n + 14)/(216(n + 2)⁴) ≤ 15/(216 · 27) < 1/388,

so |R_(k+1)| ≥ 7a/8 − 1/36 − 1/388 > 7a/8 − 0.031 ≥ 7a/8 − a/8 = 3a/4, as a/8 ≥ 3/32 > 0.031. ∎

### The hypotheses, for every K {#sec:edge-envelope-every-k}

**Proposition {#prop:edge-envelope}** (the hypotheses for the envelope of the constants). Let env be
[[eq:edge-envelope]], or exp(−1/(v − v_s)); let n ≥ 1 be an integer and x_n := 1/(96(n + 2)²). Then:
(a) on (v_s, v_s + x_n], env^(k) > 0 for k ≤ n + 2, and |env^(j)| ≤ κ^j env for j ≤ n + 2;
(b) on (v_s, v_s + x_n], for every k ≤ n, env^(k) is strictly log-concave, 99/100 ≤ κ_k/κ ≤ 1 and
    |κ_k′| ≤ c_R κ_k^(3/2), with c_R = 12/5 for [[eq:edge-envelope]] and c_R = 21/10 for exp(−1/(v − v_s));
(c) on (v_s, v_s + 1/200], |κ′| ≥ c_t κ^(3/2) with c_t = 2.13951, resp. c_t = 2, and 3/4 ≤ κx² ≤ 81/100, resp.
    κx² = 1;
(d) (H_D) holds for every c > 0.

*Proof.* Here R_0 = x²κ is [[eq:edge-a]] for [[eq:edge-envelope]] and 1 for exp(−1/x); put a := 3/4, resp. a := 1.
For [[eq:edge-envelope]], on 𝔻, where ϱ = 1/(24(n + 2)²) ≤ 1/216, [[eq:edge-a-disc]] gives |R_0 − 3/4| ≤ 12ϱ + ϱ²/7 ≤
0.056 < 3/32, so |R_0| ≥ 21/32 = 7a/8, and |R_0′| ≤ 12 + ϱ/2 ≤ 13. So [[lem:edge-disc]] applies, with c_d := 13, resp.
c_d := 0. Fix 0 < x ≤ x_n = ϱ/4 and k ≤ n + 1. 𝒯_k is holomorphic on the disc of radius ϱ_(n+1) ≥ ϱ/2 about 0, which
contains the disc of radius ϱ/4 about x, so |𝒯_k(x)| ≤ ℬ_k and, by Cauchy's estimate, |𝒯_k′(x)| ≤ 4ℬ_k/ϱ ≤ ℬ_k/x.
Hence, R_k being real on the real axis,

    |R_k(x) − R_0(x) + 2kx| ≤ ℬ_k x²,      |x R_k′(x) − x R_0′(x) + 2kx| ≤ |x(2x𝒯_k + x²𝒯_k′)| ≤ 3ℬ_k x².

For both envelopes ℬ_k x ≤ 2(n + 1)(n + 14)/((3/4) · 96 (n + 2)²) ≤ (n + 14)/(36(n + 2)) ≤ 15/108 < 1/7 and 2kx ≤
2(n + 1)/(96(n + 2)²) ≤ 1/144; and R_0(x) ≥ a by [[eq:edge-a-real]]. Therefore

    R_k(x) − R_0(x) ≥ −1/144 − x/7 ≥ −1/140,      R_k(x) − R_0(x) ≤ x(1/7 − 2k) < 0   for k ≥ 1,

the first because x ≤ x_1 = 1/864 and 1/144 + 1/6048 < 1/140; so R_k(x) ≥ a − 1/140 > 0. So
[[lem:edge-logderivatives]] applies on (0, x_n] with m = n + 1. By its (a), env^(k) > 0 for k ≤ n + 2. By (b),
κ_k/κ = R_k/R_0 ≥ 1 − 1/(140R_0) ≥ 1 − 1/(140a) ≥ 99/100, since 4/(3 · 140) < 1/100, and κ_k/κ ≤ 1; and
env^(j)/(κ^j env) = Π_(i<j) R_i/R_0 ∈ (0, 1] for j ≤ n + 2. This is (a) and the bounds of κ_k/κ in (b). For the rest
of (b), |R_0′(x)| ≤ 12 by [[eq:edge-a-real]] (R_0′ = 0 for exp(−1/x)), so

    |x R_k′(x)| ≤ 12x + 2kx + 3ℬ_k x² ≤ 12/864 + 1/144 + 3/(7 · 864) < 0.0214,   resp.  1/144 + 3/(7 · 864) < 0.0075,

while R_k ≥ 0.74, resp. R_k ≥ 0.99; in both cases |x R_k′/R_k| ≤ 1/30. By [[eq:edge-recursion]], R_k − R_(k+1) =
x(2 − x R_k′/R_k) ∈ [59x/30, 61x/30] for k ≤ n. By [[lem:edge-logderivatives]] (c), env^(k) is strictly log-concave
and |κ_k′| ≤ c κ_k^(3/2) with c = (61/30) R_k^(−1/2) ≤ (61/30)/0.86 < 12/5, as √0.74 ≥ 0.86, resp.
c ≤ (61/30)/0.99 < 21/10, as √0.99 ≥ 0.99.
(c) For [[eq:edge-envelope]] and 0 < x ≤ 1/200, [[eq:edge-a-real]] gives 3/4 ≤ R_0 ≤ 3/4 + 12x ≤ 81/100 and, as
2x²/7 ≤ 0.002x,

    2R_0 − xR_0′ ≥ 3/2 + 24x − 2x²/7 − 12x ≥ 3/2 + 11.998x > 0.

By [[lem:edge-logderivatives]] (d), |κ′|/κ^(3/2) = (2R_0 − xR_0′)/R_0^(3/2) ≥ h(x) := (3/2 + 11.998x)/(3/4 + 12x)^(3/2).
The derivative of log h has the sign of 11.998(3/4 + 12x) − 18(3/2 + 11.998x) = −18.0015 − 71.988x < 0, so h
decreases and h(x) ≥ h(1/200) = 1.55999/0.81^(3/2) = 1.55999/0.729 = 2.13990… > 2.13951, which proves (c) with
c_t = 2.13951. For exp(−1/x), (2R_0 − xR_0′)/R_0^(3/2) = 2 and κx² = 1.
(d) For 0 < x ≤ 1/200, κ = R_0/x² ≤ 1/x² by (c), and [[eq:edge-log]] with sin(πx/3) ≤ 1 and 1/(3 − x) > 0 gives
env(v_s + x) ≤ c_e e^(1 − 3/(4x)). So for 0 < y ≤ 1/800 and every c > 0

    κ(v_s + y/2) κ(v_s + 4y)^c env(v_s + 4y) ≤ 4y⁻² (16y²)^(−c) c_e e^(1 − 3/(16y)),

which tends to 0 as y ↓ 0, e^(−3/(16y)) decaying faster than every power of y. For exp(−1/x) the left side equals
4y⁻² (16y²)^(−c) e^(−1/(4y)), which tends to 0 likewise. ∎

**Corollary {#cor:edge-envelope}** (every hypothesis, for every K). Let env be [[eq:edge-envelope]] or exp(−1/(v − v_s)),
N ≥ 2, and x0 := x_(N+2) = 1/(96(N + 4)²). On (v_s, v_s + x0], (H_N) and (H_N+2) hold with α = 1/2, the c_R of
[[prop:edge-envelope]] and c_j = 1, and for v_s < v′ ≤ v ≤ v_s + x0 and j ≤ N + 4

    κ(v′)^j env(v′) ≤ κ(v)^j env(v) e^(−κ(v)(v − v′)/2);                                           {#eq:edge-decay}

(H_t) holds with c_t = 2.13951, resp. 2; (H_*) holds with c_* = 3/4, resp. 1; and (H_D) holds. So every hypothesis that
[[thm:very-edge]] and [[prop:l-26]] place on the envelope holds for these two envelopes, for every K ≥ 6 (N = K + 3).

*Proof.* [[prop:edge-envelope]] with n = N + 2: (a) and (b) give, for k ≤ N + 2, env^(k) > 0, strictly log-concave,
κ_k/κ ∈ [99/100, 1] ⊂ [1/2, 2] and |κ_k′| ≤ c_R κ_k^(1+1/2), and for j ≤ N + 4, |env^(j)| ≤ κ^j env; this is (H_N+2),
which contains (H_N). For [[eq:edge-decay]]: as x0 ≤ 1/200, (c) gives κx² ≥ 3/4, resp. κx² = 1, on (v_s, v_s + x0],
so κ^(−1/2) ≤ 2x0/√3 there; κ′ < 0 there since env is strictly log-concave; and, as c_R ≤ 12/5, j c_R κ^(−1/2) ≤
(N + 4)(12/5)(2/√3) x0 = √3/(60(N + 4)) < 1/2. Hence (log(κ^j env))′ = κ + jκ′/κ ≥ κ − j c_R κ^(1/2) ≥ κ/2 ≥ κ(v)/2
on [v′, v], and integrating over [v′, v] gives [[eq:edge-decay]]. (c) also gives c_t and c_*. By
[[lem:edge-logderivatives]] (e) with n = N − 1, which uses the strict log-concavity of env^(k) for k ≤ N − 2,
κ − κ_(N−1) ≥ |κ′|/κ ≥ c_t κ^(1/2): this is (H_t) with α = 1/2. (H_D) is (d). ∎

The hypotheses are thus proved on (v_s, v_s + 1/(96(N + 4)²)], an interval that shrinks as N grows; [[thm:very-edge]]
and [[prop:l-26]] take their interval (v_s, v_s + x0] as given and use the hypotheses only on subintervals
(v_s, v_s + x0′] with x0′ ≤ x0, so this interval is all they need.

**Remark {#rem:edge-envelope-limits}** (the constants at the edge). By [[eq:edge-disc]], as x ↓ 0, R_k → R_0(0),
x R_k′ → 0 and (R_k − R_(k+1))/(x R_k^(1/2)) → 2R_0(0)^(−1/2); so κ_k/κ → 1 and env^(j)/(κ^j env) → 1. Hence, as
x0 ↓ 0, the best constants c on (v_s, v_s + x0] in |κ_k′| ≤ c κ_k^(3/2) and in |κ′| ≥ c κ^(3/2) tend to
2R_0(0)^(−1/2), which is 4/√3 = 2.309… for [[eq:edge-envelope]] and 2 for exp(−1/x); in (H_t) with α = 1/2 the best
constant tends to 2(N − 1)R_0(0)^(−1/2), since κ − κ_(N−1) = Σ_(k<N−1) (R_k − R_(k+1))/x² with each term ~ 2/x and
κ^(1/2) = R_0^(1/2)/x. The values 12/5 and 21/10 of c_R exceed these limits by 3.9 % and 5 %. The value 2.13951 of
the constant in |κ′| ≥ c κ^(3/2) is 7.4 % below its limit 4/√3, because it holds on all of (v_s, v_s + 1/200]: the
lower bound h in the proof of [[prop:edge-envelope]] (c) decreases from h(0) = 4/√3 to h(1/200) = 2.13990….

**Remark {#rem:edge-scaled}** (the edges exp(−a/x)). Let a > 0 and env(v) = exp(−a/(v − v_s)) for v > v_s. As a
function of x̃ := x/a, env is exp(−1/x̃), and d/dx = a⁻¹ d/dx̃; so κ_k = a⁻¹ κ̃_k, where κ̃_k are the logarithmic
derivatives of exp(−1/x̃) in x̃. Hence κ_k/κ, env^(j)/(κ^j env) and κ(v)(v − v′) are those of exp(−1/x̃) at x̃ = x/a,
|κ_k′|/κ_k^(3/2) and |κ′|/κ^(3/2) are those multiplied by a^(−1/2), and κx² = a. So [[cor:edge-envelope]] holds for
this envelope on (v_s, v_s + a x0], with c_R = (21/10)a^(−1/2), c_j = 1, c_t = 2a^(−1/2) and c_* = a, (H_D) included.

**Remark {#rem:edge-sin4}** (an envelope outside the class). The envelope sin⁴(π(v − v_s)/3) for v ≥ v_s, 0 for
v < v_s, is C³ and not C⁴ at v_s: near v_s it is (πx/3)⁴(1 + O(x²)), so env^(4)(v_s+) = 4!(π/3)⁴ = 8π⁴/27, while
env^(4) = 0 for v < v_s. So it lies outside the class of [[thm:main]]. It also satisfies no (H_N) with N ≥ 3, since
κ = 4/x + O(x) and κ_3 = env^(4)/env^(3) = 1/x + O(x) give κ_3/κ → 1/4 < 1/2.
