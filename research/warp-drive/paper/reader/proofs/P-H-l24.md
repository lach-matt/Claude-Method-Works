### The growth of the margin at the crossover {#sec:l-24-margin}

The proof of [[thm:l-24]] compares, over one carrier period, the growth of the margin m0 with the change of the
first-degree amplitude S. It uses two inequalities at the points of the band: m0′ ≥ 1.9 κ m0, and m0′ − |S′| ≥ c κ m0
with a fixed c > 0 where R ≤ 1.1. This section proves both, with explicit constants and thresholds. The first holds,
for λ below an explicit threshold, for every envelope that is positive and log-concave on (v_s, v], which is part of the
hypothesis (H_N) of [[thm:l-24]]; for the two envelopes of [[sec:edge-envelope]] the thresholds are written out. The
second holds with c = 0.89 where R ≤ 1.1, with c = 0.93 where R ≤ 1.06 and with c = 0.99 where R ≤ 1.005. The factor
is 2 − R up to small terms ([[rem:l-24-sharp]]), so that no c above 0.904 holds at R = 1.1. [[cor:l-24-period]] gives
the decrease over one carrier period that the proof of [[thm:l-24]] draws from these inequalities.

*Setting.* As in [[ch:equality-layer]], μ0 > 0 is the seed's mass, A > 0 the amplitude of the waves, env ≥ 0 the
envelope and v_s := inf supp env. The margin of the boundary {r = r_q} at equality is

    μ(v) := μ0 + (2/9) A² ∫_(v_s)^v env²,    r_q := (μ0 μ)^(1/4),    m0 := √(μ/μ0) − 1 + r_q μ′/(2μ),  {#eq:l-24-margin}

so that μ′ = (2/9) A² env² and μ ≥ μ0. A prime is d/dv. Where env > 0 we write κ := (log env)′. We put E(v) :=
sup_(v′≤v) env(v′); the band is the set of v with λ^(3+δ) ≤ E(v) ≤ λ^(3−δ), where 0 < δ ≤ 1/2; at a point (v, ω) of
the boundary, R(v, ω) := λ³ A env(v) |ν(v − τ0)| |d(ϑ)|/m0(v), with ν and d as in [[ch:equality-layer]]; and S is the
first-degree amplitude of [[thm:l-24]] at fixed ω, a continuously differentiable complex function of v. In this section
only, p := (μ/μ0)^(1/2) ≥ 1.

**Lemma {#lem:l-24-margin}** (The logarithmic growth of the margin.) Let v > v_s, let env be positive and log-concave on
(v_s, v], and let κ(v) > 0. Put

    ξ := μ′/(μ0 κ) = 2A² env²/(9 μ0 κ)     at v.                                                  {#eq:l-24-xi}

Then at v

    (2 − 3ξ/4) κ m0 ≤ m0′ ≤ (2 + (1 + ξ/8)/(√μ0 κ)) κ m0.                                        {#eq:l-24-margin-bounds}

*Proof.* Write ℓ := log env and κ for κ(v). As ℓ is concave and differentiable on (v_s, v], ℓ(t) ≤ ℓ(v) + κ(t − v) for
v_s < t ≤ v, so env(t)² ≤ env(v)² e^(2κ(t − v)) there, and

    μ − μ0 = (2/9) A² ∫_(v_s)^v env² ≤ (2/9) A² env(v)² ∫_(−∞)^v e^(2κ(t − v)) dt = μ′/(2κ).    {#eq:l-24-logconcave}

*The two terms of m0.* From μ = μ0 p², r_q/(2μ) = μ0^(1/4) μ^(−3/4)/2 = 1/(2 √μ0 p^(3/2)), and p − 1 = (p² − 1)/(p + 1) =
(μ − μ0)/(μ0 (p + 1)). So m0 = p − 1 + μ′/(2 √μ0 p^(3/2)), and

    κ m0 = a_1 + a_2,      a_1 := κ (μ − μ0)/(μ0 (p + 1)) ≥ 0,      a_2 := κ μ′/(2 √μ0 p^(3/2)) > 0.     {#eq:l-24-m0}

*The derivative.* μ″ = (2/9) A² · 2 env env′ = 2κ μ′, and p′ = μ′/(2 √(μ0 μ)) = μ′/(2 μ0 p). Hence
(μ′ p^(−3/2))′ = 2κ μ′ p^(−3/2) − (3/2) μ′ p^(−5/2) p′ = 2κ μ′ p^(−3/2) − 3μ′²/(4 μ0 p^(7/2)), and

    m0′ = μ′/(2 μ0 p) + κ μ′/(√μ0 p^(3/2)) − 3μ′²/(8 μ0^(3/2) p^(7/2)).                             {#eq:l-24-dm0}

*Comparison with 2κ m0.* The second term of [[eq:l-24-dm0]] is 2a_2. Since 1/(p + 1) − 1/(2p) = (p − 1)/(2p(p + 1)),
the first term is μ′/(μ0 (p + 1)) − b_1 with b_1 := μ′ (p − 1)/(2 μ0 p (p + 1)) ≥ 0. With b_2 := 3μ′²/(8 μ0^(3/2)
p^(7/2)) and 2κ m0 = 2a_1 + 2a_2 this gives

    m0′ − 2κ m0 = (μ′ − 2κ (μ − μ0))/(μ0 (p + 1)) − b_1 − b_2.                                      {#eq:l-24-split}

*Lower bound.* The first term of [[eq:l-24-split]] is nonnegative by [[eq:l-24-logconcave]]. Since p − 1 = (μ − μ0)/(μ0
(p + 1)) ≤ (μ − μ0)/(2μ0) and p ≥ 1,

    b_1 ≤ μ′ (μ − μ0)/(4 μ0² p (p + 1)) ≤ μ′ (μ − μ0)/(4 μ0² (p + 1)) = (ξ/4) a_1,
    b_2 = (3μ′/(4 μ0 κ p²)) a_2 ≤ (3ξ/4) a_2.

So b_1 + b_2 ≤ (3ξ/4)(a_1 + a_2) = (3ξ/4) κ m0, which is the left inequality of [[eq:l-24-margin-bounds]].

*Upper bound.* In [[eq:l-24-split]], (μ′ − 2κ(μ − μ0))/(μ0 (p + 1)) − b_1 ≤ μ′/(μ0 (p + 1)) − b_1 = μ′/(2 μ0 p) and
b_2 ≥ 0, so m0′ − 2κ m0 ≤ μ′/(2 μ0 p) = (p^(1/2)/(√μ0 κ)) a_2 ≤ (p^(1/2)/(√μ0 κ)) κ m0. Finally p² = 1 + (μ − μ0)/μ0 ≤
1 + ξ/2 by [[eq:l-24-logconcave]], and (1 + y)^(1/4) ≤ 1 + y/4 for y ≥ 0, so p^(1/2) ≤ 1 + ξ/8. ∎

**Proposition {#prop:l-24-band}** (The margin in the band.) Let x0 > 0, let env be positive and log-concave on
(v_s, v_s + x0] with κ̂ := κ(v_s + x0) > 0, and let 0 < δ ≤ 1/2 and 0 < λ < 1 with λ^(5/2) < env(v_s + x0). Then every
v with 0 < E(v) ≤ λ^(3−δ), in particular every point of the band, lies in (v_s, v_s + x0), and at v

    ξ ≤ 2A² λ^(6−2δ)/(9 μ0 κ̂) ≤ 2A² λ⁵/(9 μ0 κ̂),      m0′ ≥ (2 − A² λ⁵/(6 μ0 κ̂)) κ m0.            {#eq:l-24-band}

So m0′ ≥ 1.9 κ m0 at every such v once λ⁵ ≤ 3μ0 κ̂/(5A²), and ξ ≤ 10⁻³ there once λ⁵ ≤ 9μ0 κ̂/(2000 A²).

*Proof.* As log env is concave on (v_s, v_s + x0], κ is nonincreasing there, so κ ≥ κ̂ > 0 and env is increasing on
(v_s, v_s + x0]. If v ≤ v_s, then E(v) = 0. If v ≥ v_s + x0, then E(v) ≥ env(v_s + x0) > λ^(5/2) ≥ λ^(3−δ), since
3 − δ ≥ 5/2 and λ < 1. Hence v_s < v < v_s + x0; env is positive and log-concave on (v_s, v], κ(v) ≥ κ̂ > 0, and
env(v) = E(v) ≤ λ^(3−δ). So ξ = 2A² env(v)²/(9 μ0 κ(v)) ≤ 2A² λ^(6−2δ)/(9 μ0 κ̂), which is at most 2A² λ⁵/(9 μ0 κ̂)
as 6 − 2δ ≥ 5, and [[lem:l-24-margin]] gives m0′ ≥ (2 − 3ξ/4) κ m0 with 3ξ/4 ≤ A² λ⁵/(6 μ0 κ̂). The two thresholds are
the conditions A² λ⁵/(6 μ0 κ̂) ≤ 1/10 and 2A² λ⁵/(9 μ0 κ̂) ≤ 10⁻³. ∎

**Corollary {#cor:l-24-envelopes}** (The two envelopes.) Let 0 < δ ≤ 1/2 and let v satisfy 0 < E(v) ≤ λ^(3−δ).

(a) For env = exp(−1/(v − v_s)) on v > v_s and 0 < λ ≤ e^(−1): at v, ξ ≤ 8A² λ⁵/(225 μ0) and
m0′ ≥ (2 − 2A² λ⁵/(75 μ0)) κ m0. So m0′ ≥ 1.9 κ m0 once λ⁵ ≤ 15μ0/(4A²), and ξ ≤ 10⁻³ once λ⁵ ≤ 9μ0/(320 A²).

(b) For the envelope [[eq:edge-envelope]], with c_e its constant, and 0 < λ < 1 with λ^(5/2) < (729/4096) e^(−1/8) c_e:
at v, ξ ≤ 2A² λ⁵/(63 μ0) and m0′ ≥ (2 − A² λ⁵/(42 μ0)) κ m0. So m0′ ≥ 1.9 κ m0 once λ⁵ ≤ 21μ0/(5A²), and ξ ≤ 10⁻³ once
λ⁵ ≤ 63μ0/(2000 A²).

*Proof.* Put x := v − v_s. (a) Here log env = −1/x, κ = 1/x² > 0 and (log env)″ = −2/x³ < 0, so env is positive,
increasing and log-concave on (v_s, ∞), E(v) = env(v) for v > v_s, and E(v) > 0 gives x > 0. From e^(−1/x) ≤ λ^(3−δ) ≤
λ^(5/2) we get 1/x ≥ (5/2) log(1/λ) ≥ 5/2, so x ≤ 2/5. [[lem:l-24-margin]] applies at v, with
ξ = (2A²/(9 μ0)) x² e^(−2/x) ≤ (2A²/(9 μ0))(4/25) λ⁵ = 8A² λ⁵/(225 μ0) and 3ξ/4 ≤ 2A² λ⁵/(75 μ0). The thresholds
are 2A² λ⁵/(75 μ0) ≤ 1/10 and 8A² λ⁵/(225 μ0) ≤ 10⁻³.
(b) By [[eq:edge-log]], on 0 < x < 3, log env = log c_e + 1 + 12 log sin(πx/3) − (3/4)(1/x + 1/(3 − x)), so

    κ = 4π cot(πx/3) + (3/4)(1/x² − 1/(3 − x)²),      κ′ = −(4π²/3)/sin²(πx/3) − (3/2)(1/x³ + 1/(3 − x)³) < 0.

So env is positive and log-concave on (v_s, v_s + 3). At x = 1, cot(π/3) = 1/√3 gives κ = 4π/√3 + 9/16 > 7, since
16π² > 147; and sin²(π/3) = 3/4 gives env(v_s + 1) = c_e e^(1 − 9/8) (3/4)⁶ = (729/4096) e^(−1/8) c_e. So
[[prop:l-24-band]] applies with x0 := 1 and κ̂ > 7: ξ ≤ 2A² λ⁵/(63 μ0) and 3ξ/4 ≤ A² λ⁵/(42 μ0). The thresholds are
A² λ⁵/(42 μ0) ≤ 1/10 and 2A² λ⁵/(63 μ0) ≤ 10⁻³. ∎

In both cases the lower bound of [[eq:l-24-margin-bounds]] needs only log-concavity of env, which holds on the whole
increasing part of each envelope, and not the finer hypotheses that [[cor:edge-envelope]] proves on (v_s, v_s + x0].

**Proposition {#prop:l-24-transition}** (The first-degree term against the margin.) Let (v, ω) be a point at which
[[lem:l-24-margin]] applies with ξ ≤ 10⁻³ (by [[prop:l-24-band]], every point of the band once λ is below the thresholds
there), and suppose that

    |S′| ≤ 1.001 κ |S|,      |S| ≤ 1.001 R m0      at (v, ω).                                         {#eq:l-24-s-bounds}

Then at (v, ω)

    m0′ − |S′| ≥ (2 − 3ξ/4 − 1.002001 R) κ m0 ≥ (1.99925 − 1.002001 R) κ m0;                       {#eq:l-24-transition}

in particular m0′ − |S′| ≥ 0.89 κ m0 where R ≤ 1.1, m0′ − |S′| ≥ 0.93 κ m0 where R ≤ 1.06, and m0′ − |S′| ≥ 0.99 κ m0
where R ≤ 1.005.

*Proof.* By [[eq:l-24-s-bounds]], |S′| ≤ 1.001² κ R m0 = 1.002001 κ R m0, and by [[lem:l-24-margin]],
m0′ ≥ (2 − 3ξ/4) κ m0; subtracting gives the first inequality, and 3ξ/4 ≤ 0.00075 gives the second. Finally
1.99925 − 1.002001 · 1.1 = 0.8970489, 1.99925 − 1.002001 · 1.06 = 0.93712894 and 1.99925 − 1.002001 · 1.005 =
0.992238995. ∎

The two bounds [[eq:l-24-s-bounds]] are the properties of S that the proof of [[thm:l-24]] uses.

**Remark {#rem:l-24-sharp}** (The factor 2 − R.) The constant 2 of [[lem:l-24-margin]] is attained at the edge. Let env
be positive and log-concave on (v_s, v_s + x0] with env(v) → 0 as v ↓ v_s. Then κ is nonincreasing there and κ(v) → ∞
as v ↓ v_s, since a finite limit K would give log env(v) ≥ log env(v_s + x0) − K x0 for every v in (v_s, v_s + x0]; so
ξ → 0, and both bounds of [[eq:l-24-margin-bounds]] tend to 2. Hence the factor 2 − R in [[eq:l-24-transition]] cannot
be improved. If at (v, ω) also |S′| ≥ 0.999 κ |S| (as for any constant multiple of env, for which |S′| = κ|S|) and
|S| ≥ 0.999 R m0, with ξ ≤ 10⁻³ and √μ0 κ ≥ 10³, then (1 + ξ/8)/(√μ0 κ) ≤ 1.001 · 10⁻³, 0.999² ≥ 0.998, and the
upper bound of [[eq:l-24-margin-bounds]] gives

    m0′ − |S′| ≤ (2.001001 − 0.998 R) κ m0,

which is 0.903201 κ m0 at R = 1.1 and below 0.93 κ m0 for every R ≥ 1.075. For such S no bound m0′ − |S′| ≥ 0.93 κ m0
holds on 1.075 ≤ R ≤ 1.1, and at R = 1.1 the constant 0.89 of [[prop:l-24-transition]] is within 0.014 of the best one.

**Corollary {#cor:l-24-period}** (One carrier period.) Let t be real and I := [t, t + 2πλ]. Suppose that at every point
of I [[prop:l-24-transition]] applies with R ≤ 1.1 and √μ0 κ ≥ 2, and that

    2πλ sup_I (|κ′|/κ + 3κ) ≤ 1/26.                                                                {#eq:l-24-period-cond}

Then

    m0(t + 2πλ) − m0(t) + Re[(S(t + 2πλ) − S(t)) e^(it/λ)] ≥ 1.7 πλ κ(t) m0(t).                     {#eq:l-24-period}

Under (H_N) on I with κ ≥ 1 there, |κ′|/κ ≤ c_R κ^α ≤ c_R κ, so [[eq:l-24-period-cond]] holds once
2π (c_R + 3) λ sup_I κ ≤ 1/26.

*Proof.* On I, κ′ ≤ 0 by log-concavity, and by [[lem:l-24-margin]] with ξ ≤ 10⁻³ and √μ0 κ ≥ 2,
0 < m0′/m0 ≤ (2 + 1.000125/2) κ ≤ 3κ. So |(log(κ m0))′| = |κ′/κ + m0′/m0| ≤ |κ′|/κ + 3κ, and by [[eq:l-24-period-cond]]
log(κ m0) varies by at most 1/26 on I. As e^y < 1/(1 − y) for 0 < y < 1, e^(1/26) < 26/25, so κ m0 ≥ (25/26) κ(t) m0(t)
on I. The left side of [[eq:l-24-period]] is ∫_I (m0′(s) + Re[S′(s) e^(it/λ)]) ds ≥ ∫_I (m0′ − |S′|) ds, and by
[[prop:l-24-transition]] this is at least 0.89 · 2πλ · (25/26) κ(t) m0(t) ≥ 1.71 πλ κ(t) m0(t). ∎
