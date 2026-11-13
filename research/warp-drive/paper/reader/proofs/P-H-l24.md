### The growth of the margin at the crossover {#sec:l-24-margin}

The proof of [[thm:l-24]] compares, over one carrier period, the growth of the margin m0 with the change of the
first-degree amplitude S. It uses two inequalities at the points of the band: m0′ ≥ 1.9 κ m0, and m0′ − |S′| ≥ c κ m0
with a fixed c > 0 where R ≤ 1.1. This section proves both, with explicit constants and thresholds. The first holds,
for λ below an explicit threshold, for every envelope that is positive and log-concave on an interval (v_s, v_s + x0]
with κ(v_s + x0) > 0, which is part of the hypothesis (H_N) of [[thm:l-24]]; for the two envelopes of
[[sec:edge-envelope]] the thresholds are written out. The second holds with c = 0.89 where R ≤ 1.1, with c = 0.93 where
R ≤ 1.06 and with c = 0.99 where R ≤ 1.005, for every S with |S′| ≤ 1.001 κ |S| and |S| ≤ 1.001 R m0. The first-degree
amplitude has these two properties at the points of the band where R ≥ 1/2, once λ is small ([[prop:l-24-s-bounds]]),
and the proof of [[thm:l-24]] uses them at no other points. The factor is 2 − R up to small terms: for S that also
satisfies the reverse bounds |S′| ≥ 0.999 κ |S| and |S| ≥ 0.999 R m0, as the first-degree amplitude does at the same
points, no c above 0.904 holds at R = 1.1 once λ is small ([[rem:l-24-sharp]]). [[cor:l-24-period]] gives the decrease
over one carrier period that the proof of [[thm:l-24]] draws from these inequalities, and [[rem:l-24-eps]] compares the
degree-two terms of that proof with m0.

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

    ς := μ′/(μ0 κ) = 2A² env²/(9 μ0 κ)     at v.                                                  {#eq:l-24-xi}

Then at v

    (2 − 3ς/4) κ m0 ≤ m0′ ≤ (2 + (1 + ς/8)/(√μ0 κ)) κ m0.                                        {#eq:l-24-margin-bounds}

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

    b_1 ≤ μ′ (μ − μ0)/(4 μ0² p (p + 1)) ≤ μ′ (μ − μ0)/(4 μ0² (p + 1)) = (ς/4) a_1,
    b_2 = (3μ′/(4 μ0 κ p²)) a_2 ≤ (3ς/4) a_2.

So b_1 + b_2 ≤ (3ς/4)(a_1 + a_2) = (3ς/4) κ m0, which is the left inequality of [[eq:l-24-margin-bounds]].

*Upper bound.* In [[eq:l-24-split]], (μ′ − 2κ(μ − μ0))/(μ0 (p + 1)) − b_1 ≤ μ′/(μ0 (p + 1)) − b_1 = μ′/(2 μ0 p) and
b_2 ≥ 0, so m0′ − 2κ m0 ≤ μ′/(2 μ0 p) = (p^(1/2)/(√μ0 κ)) a_2 ≤ (p^(1/2)/(√μ0 κ)) κ m0. Finally p² = 1 + (μ − μ0)/μ0 ≤
1 + ς/2 by [[eq:l-24-logconcave]], and (1 + y)^(1/4) ≤ 1 + y/4 for y ≥ 0, so p^(1/2) ≤ 1 + ς/8. ∎

**Proposition {#prop:l-24-band}** (The margin in the band.) Let x0 > 0, let env be positive and log-concave on
(v_s, v_s + x0] with κ̂ := κ(v_s + x0) > 0, and let 0 < δ ≤ 1/2 and 0 < λ < 1 with λ^(5/2) < env(v_s + x0). Then every
v with 0 < E(v) ≤ λ^(3−δ), in particular every point of the band, lies in (v_s, v_s + x0), and at v

    ς ≤ 2A² λ^(6−2δ)/(9 μ0 κ̂) ≤ 2A² λ⁵/(9 μ0 κ̂),      m0′ ≥ (2 − A² λ⁵/(6 μ0 κ̂)) κ m0.            {#eq:l-24-band}

So m0′ ≥ 1.9 κ m0 at every such v once λ⁵ ≤ 3μ0 κ̂/(5A²), and ς ≤ 10⁻³ there once λ⁵ ≤ 9μ0 κ̂/(2000 A²).

*Proof.* As log env is concave on (v_s, v_s + x0], κ is nonincreasing there, so κ ≥ κ̂ > 0 and env is increasing on
(v_s, v_s + x0]. If v ≤ v_s, then E(v) = 0. If v ≥ v_s + x0, then E(v) ≥ env(v_s + x0) > λ^(5/2) ≥ λ^(3−δ), since
3 − δ ≥ 5/2 and λ < 1. Hence v_s < v < v_s + x0; env is positive and log-concave on (v_s, v], κ(v) ≥ κ̂ > 0, and
env(v) = E(v) ≤ λ^(3−δ). So ς = 2A² env(v)²/(9 μ0 κ(v)) ≤ 2A² λ^(6−2δ)/(9 μ0 κ̂), which is at most 2A² λ⁵/(9 μ0 κ̂)
as 6 − 2δ ≥ 5, and [[lem:l-24-margin]] gives m0′ ≥ (2 − 3ς/4) κ m0 with 3ς/4 ≤ A² λ⁵/(6 μ0 κ̂). The two thresholds are
the conditions A² λ⁵/(6 μ0 κ̂) ≤ 1/10 and 2A² λ⁵/(9 μ0 κ̂) ≤ 10⁻³. ∎

**Corollary {#cor:l-24-envelopes}** (The two envelopes.) Let 0 < δ ≤ 1/2 and let v satisfy 0 < E(v) ≤ λ^(3−δ).

(a) For env = exp(−1/(v − v_s)) on v > v_s and 0 < λ ≤ e^(−1): at v, ς ≤ 8A² λ⁵/(225 μ0) and
m0′ ≥ (2 − 2A² λ⁵/(75 μ0)) κ m0. So m0′ ≥ 1.9 κ m0 once λ⁵ ≤ 15μ0/(4A²), and ς ≤ 10⁻³ once λ⁵ ≤ 9μ0/(320 A²).

(b) For the envelope [[eq:edge-envelope]], with c_e its constant, and 0 < λ < 1 with λ^(5/2) < (729/4096) e^(−1/8) c_e:
at v, ς ≤ 2A² λ⁵/(63 μ0) and m0′ ≥ (2 − A² λ⁵/(42 μ0)) κ m0. So m0′ ≥ 1.9 κ m0 once λ⁵ ≤ 21μ0/(5A²), and ς ≤ 10⁻³ once
λ⁵ ≤ 63μ0/(2000 A²).

*Proof.* Put x := v − v_s. (a) Here log env = −1/x, κ = 1/x² > 0 and (log env)″ = −2/x³ < 0, so env is positive,
increasing and log-concave on (v_s, ∞), E(v) = env(v) for v > v_s, and E(v) > 0 gives x > 0. From e^(−1/x) ≤ λ^(3−δ) ≤
λ^(5/2) we get 1/x ≥ (5/2) log(1/λ) ≥ 5/2, so x ≤ 2/5. [[lem:l-24-margin]] applies at v, with
ς = (2A²/(9 μ0)) x² e^(−2/x) ≤ (2A²/(9 μ0))(4/25) λ⁵ = 8A² λ⁵/(225 μ0) and 3ς/4 ≤ 2A² λ⁵/(75 μ0). The thresholds
are 2A² λ⁵/(75 μ0) ≤ 1/10 and 8A² λ⁵/(225 μ0) ≤ 10⁻³.
(b) By [[eq:edge-log]], on 0 < x < 3, log env = log c_e + 1 + 12 log sin(πx/3) − (3/4)(1/x + 1/(3 − x)), so

    κ = 4π cot(πx/3) + (3/4)(1/x² − 1/(3 − x)²),      κ′ = −(4π²/3)/sin²(πx/3) − (3/2)(1/x³ + 1/(3 − x)³) < 0.

So env is positive and log-concave on (v_s, v_s + 3). At x = 1, cot(π/3) = 1/√3 gives κ = 4π/√3 + 9/16 > 7, since
16π² > 147; and sin²(π/3) = 3/4 gives env(v_s + 1) = c_e e^(1 − 9/8) (3/4)⁶ = (729/4096) e^(−1/8) c_e. So
[[prop:l-24-band]] applies with x0 := 1 and κ̂ > 7: ς ≤ 2A² λ⁵/(63 μ0) and 3ς/4 ≤ A² λ⁵/(42 μ0). The thresholds are
A² λ⁵/(42 μ0) ≤ 1/10 and 2A² λ⁵/(63 μ0) ≤ 10⁻³. ∎

In both cases the lower bound of [[eq:l-24-margin-bounds]] needs only log-concavity of env, which holds on the whole
increasing part of each envelope, and not the finer hypotheses that [[cor:edge-envelope]] proves on (v_s, v_s + x0].

The next lemma uses one more part of (H_N): the bound on κ′ ([[sec:edge-envelope]], k = 0).

**Lemma {#lem:l-24-kappa}** (The size of κ in the band.) Let x0 > 0, let env be positive and log-concave on
(v_s, v_s + x0] with env′ > 0 and |κ′| ≤ c_R κ^(1+α) there, where c_R > 0 and 0 < α < 1, and let env(v) → 0 as v ↓ v_s.
For v_s < v ≤ v_s + x0 put x := v − v_s. Then

    κ(v) ≥ (α c_R x)^(−1/α),                                                                       {#eq:l-24-kappa-low}

and if moreover v ≤ v_s + x0/2,

    κ(v) ≤ max{(2/(α c_R x0))^(1/α), (2^(1/α) α c_R log(env(v_s + x0)/env(v)))^(1/(1−α))}.          {#eq:l-24-kappa-up}

Let 0 < δ ≤ 1/2 and 0 < λ < 1 with λ^(5/2) < env(v_s + x0/2) and env(v_s + x0) ≤ λ^(−1/2), and let x_λ ∈ (0, x0/2) be
defined by env(v_s + x_λ) = λ^(5/2). Then every point v of the band satisfies v_s < v ≤ v_s + x_λ and

    (α c_R x_λ)^(−1/α) ≤ κ(v) ≤ K_λ := max{(2/(α c_R x0))^(1/α), (2^(2+1/α) α c_R log(1/λ))^(1/(1−α))},
    κ(v) (v − v_s) ≥ (α c_R)^(−1/α) x_λ^(1−1/α).                                                   {#eq:l-24-kappa-band}

As λ → 0, x_λ → 0 and λ K_λ^j → 0 for every j ≥ 1. So κ and κ(v − v_s) tend to ∞ uniformly on the band, and for every
δ′ ∈ (0, 1) there is a threshold on λ below which λκ ≤ λ^(δ′) at every point of the band.

*Proof.* As log env is concave and differentiable, κ is nonincreasing and κ′ ≤ 0; and κ > 0 since env′ > 0. If κ were
bounded by some K on (v_s, v_s + x0], then log env(v) ≥ log env(v_s + x0) − K x0 for every v there, against env(v) → 0;
so κ(t) → ∞ as t ↓ v_s. Now (κ^(−α))′ = −α κ^(−α−1) κ′ = α κ^(−α−1) |κ′| lies in [0, α c_R]. For v_s < t < v,
κ(v)^(−α) ≤ κ(t)^(−α) + α c_R (v − t), and letting t ↓ v_s gives [[eq:l-24-kappa-low]].
For [[eq:l-24-kappa-up]] put h := κ(v)^(−α)/(α c_R). If h > x0/2, then κ(v) < (2/(α c_R x0))^(1/α). Otherwise
v + h ≤ v_s + x0, and for v ≤ t ≤ v + h, κ(t)^(−α) ≤ κ(v)^(−α) + α c_R h = 2κ(v)^(−α), so κ(t) ≥ 2^(−1/α) κ(v). As env
is increasing,

    log(env(v_s + x0)/env(v)) ≥ ∫_v^(v+h) κ ≥ 2^(−1/α) κ(v) h = 2^(−1/α) κ(v)^(1−α)/(α c_R),

which is [[eq:l-24-kappa-up]] in this case.
Let v be a point of the band. Then E(v) ≥ λ^(3+δ) > 0, so v > v_s. If v_s + x_λ < v ≤ v_s + x0, then E(v) ≥ env(v) >
env(v_s + x_λ) = λ^(5/2); if v > v_s + x0, then E(v) ≥ env(v_s + x0) > λ^(5/2). Both contradict E(v) ≤ λ^(3−δ) ≤ λ^(5/2),
so v ≤ v_s + x_λ, and env(v) = E(v) ≥ λ^(3+δ), as env is increasing on (v_s, v]. Hence log(env(v_s + x0)/env(v)) ≤
(1/2 + 3 + δ) log(1/λ) ≤ 4 log(1/λ), and [[eq:l-24-kappa-up]] gives κ(v) ≤ K_λ. The lower bounds of
[[eq:l-24-kappa-band]] follow from [[eq:l-24-kappa-low]] with x ≤ x_λ, since −1/α < 0 and 1 − 1/α < 0. Finally, env is
continuous and positive on (v_s, v_s + x0], so for every y in (0, x0/2) we have x_λ < y once λ^(5/2) < env(v_s + y);
and K_λ grows like a power of log(1/λ), so λ K_λ^j → 0 and λ^(1−δ′) K_λ → 0. ∎

**Proposition {#prop:l-24-transition}** (The first-degree term against the margin.) Let (v, ω) be a point at which
[[lem:l-24-margin]] applies with ς ≤ 10⁻³ (by [[prop:l-24-band]], every point of the band once λ is below the thresholds
there), and suppose that

    |S′| ≤ 1.001 κ |S|,      |S| ≤ 1.001 R m0      at (v, ω)                                          {#eq:l-24-s-bounds}

(by [[prop:l-24-s-bounds]], at every point of the band with R ≥ 1/2 once λ is small). Then at (v, ω)

    m0′ − |S′| ≥ (2 − 3ς/4 − 1.002001 R) κ m0 ≥ (1.99925 − 1.002001 R) κ m0;                       {#eq:l-24-transition}

in particular m0′ − |S′| ≥ 0.89 κ m0 where R ≤ 1.1, m0′ − |S′| ≥ 0.93 κ m0 where R ≤ 1.06, and m0′ − |S′| ≥ 0.99 κ m0
where R ≤ 1.005.

*Proof.* By [[eq:l-24-s-bounds]], |S′| ≤ 1.001² κ R m0 = 1.002001 κ R m0, and by [[lem:l-24-margin]],
m0′ ≥ (2 − 3ς/4) κ m0; subtracting gives the first inequality, and 3ς/4 ≤ 0.00075 gives the second. Finally
1.99925 − 1.002001 · 1.1 = 0.8970489, 1.99925 − 1.002001 · 1.06 = 0.93712894 and 1.99925 − 1.002001 · 1.005 =
0.992238995. ∎

The two bounds [[eq:l-24-s-bounds]] are the properties of S that the proof of [[thm:l-24]] uses. They are needed only
at points where R lies near 1, and they follow there, for λ small, from the first-degree horizon value. We use it in the
following form. Let N ≥ 9 and let (H_N) of [[sec:edge-envelope]] hold on (v_s, v_s + x0], with constants c_R > 0 and
α ∈ (0, 1); put r0 := v − τ0, T := λ κ_(N−1), c_N := N μ0/(r0² + μ0) and Λ := λ^(N−2) env^(N−1)/env. The first-degree
horizon value [[pending:ch85-s-bounds]] gives, with a constant C independent of λ, v and ω, at every point (v, ω) with
v_s < v ≤ v_s + x0 and λκ(v) ≤ 1,

    S = S_st + S_U + E_S,      S_st := λ³ A ν(r0) d(ϑ) env (1 + 2iλκ),
    S_U := −λ^(N+1) A i^N d(ϑ) Γ_R(r0) Ξ env^(N−1),      Ξ := ((1 − c_N) T − i c_N)/(T + i),
    |E_S| + |E_S′|/κ ≤ C [λ³ env (|ν(r0)| (λκ)² + λ) + |S_U|],                                    {#eq:l-24-s-split}

where ν and Γ_R > 0 are real functions of r0, smooth near r0 = v_s − τ0, d is a bounded function of the polar angle ϑ,
and either ν(v_s − τ0) ≠ 0 or ν(v_s − τ0) = ν′(v_s − τ0) = 0 ≠ ν″(v_s − τ0). The factor |1 + 2iλκ| makes
|S_st| = R m0 (1 + 4λ²κ²)^(1/2), so S_st carries R exactly; the work is to show that S_U and E_S, and their derivatives,
are small against R m0 and κ R m0.

**Proposition {#prop:l-24-s-bounds}** (The first-degree amplitude where R ≥ 1/2.) Assume [[eq:l-24-s-split]] with the
properties stated after it, and let 0 < δ ≤ 1/2. There is λ_S ∈ (0, 1), independent of v and ω, such that for
0 < λ < λ_S, at every point (v, ω) of the band with R(v, ω) ≥ 1/2,

    0.999 κ |S| ≤ |S′| ≤ 1.001 κ |S|,      0.999 R m0 ≤ |S| ≤ 1.001 R m0.                          {#eq:l-24-s-two-sided}

In particular [[eq:l-24-s-bounds]] holds at these points, and Λ ≤ λ and λκ ≤ λ^(δ′) (any fixed δ′ < 1) hold at every
point of the band once λ is small.

*Proof.* Put x := v − v_s. As Γ_R, ν and c_N are smooth near r0 = v_s − τ0 and d is bounded, there are x_1 > 0 and C
such that Γ_R, |Γ_R′|, |ν|, |c_N′| and |d| are at most C for 0 < x ≤ x_1, and c_N ≤ N everywhere. Moreover, after
decreasing x_1, |ν′(r0)| ≤ C (1 + 1/x) |ν(r0)| for 0 < x ≤ x_1: if ν(v_s − τ0) ≠ 0, take x_1 so small that
|ν(r0)| ≥ |ν(v_s − τ0)|/2; otherwise r0 − (v_s − τ0) = x, and Taylor's formula gives ν(r0) = (ν″(v_s − τ0)/2) x²
(1 + O(x)) and ν′(r0) = ν″(v_s − τ0) x (1 + O(x)), so x ν′/ν → 2 and |ν′/ν| ≤ 3/x for x small.
Take λ below the thresholds of [[prop:l-24-band]] and [[lem:l-24-kappa]], with x_λ ≤ min(x_1, 1), α c_R x_λ ≤ 1 and
λ K_λ ≤ 1. Let (v, ω) be a point of the band with R ≥ 1/2. By [[lem:l-24-kappa]], 0 < x ≤ x_λ, env(v) = E(v) lies in
[λ^(3+δ), λ^(3−δ)] and 1 ≤ κ ≤ K_λ, so λκ ≤ 1 and [[eq:l-24-s-split]] applies; by [[prop:l-24-band]], ς ≤ 10⁻³. Put

    θ := λ^(1−δ) (1 + λ K_λ² + λ^(N−3) K_λ^(N−1)) + λ K_λ + x_λ^(1/α − 1),

which depends on λ alone and tends to 0 with λ, by [[lem:l-24-kappa]]. By [[eq:l-24-kappa-low]] and x ≤ x_λ ≤ 1,
1/κ and 1/(κx) are at most (α c_R)^(1/α) x_λ^(1/α − 1); so 1/κ, 1/(κx) and λκ are at most Cθ. Below, C is independent of
λ, v and ω and may change from line to line.

*The size of |ν| |d|.* By [[eq:l-24-m0]], m0 ≥ a_2/κ = A² env²/(9 √μ0 p^(3/2)), and p^(3/2) ≤ (1 + ς/2)^(3/4) ≤ 10/9
by the proof of [[lem:l-24-margin]]; so m0 ≥ A² env²/(10 √μ0). As R m0 = λ³ A env |ν(r0)| |d(ϑ)| and R ≥ 1/2,

    |ν(r0)| |d(ϑ)| ≥ A env/(20 √μ0 λ³) ≥ (A/(20 √μ0)) λ^δ,

and, |ν| and |d| being at most C, both |ν(r0)| and |d(ϑ)| are at least λ^δ/C. In particular ν(r0) ≠ 0.

*The size of S − S_st.* By (H_N), env^(N−1) = κ_0 κ_1 ⋯ κ_(N−2) env with 0 < κ_k ≤ 2κ, so Λ ≤ 2^(N−1) λ^(N−2) κ^(N−1)
≤ 2^(N−1) λ^(N−2) K_λ^(N−1) ≤ C θ λ^δ, which is also at most λ for λ small. As |T + i| ≥ max(T, 1), |Ξ| ≤ |1 − c_N| + c_N
≤ C, and Γ_R ≤ C; hence, with |ν| ≥ λ^δ/C,

    |S_U| ≤ C Λ λ³ A |d| env = C (Λ/|ν|) R m0 ≤ C θ R m0.

Dividing the bound on E_S in [[eq:l-24-s-split]] by R m0 = λ³ A env |ν| |d| and using the lower bounds on |d| and
|ν| |d|,

    |E_S| ≤ C [(λκ)²/|d| + λ/(|ν| |d|)] R m0 + C |S_U| ≤ C [λ^(2−δ) K_λ² + λ^(1−δ) + θ] R m0 ≤ C θ R m0.

So |S − S_st| ≤ C θ R m0. As R m0 ≤ |S_st| = R m0 (1 + 4λ²κ²)^(1/2) ≤ (1 + 2θ²) R m0,

    (1 − C θ) R m0 ≤ |S| ≤ (1 + 2θ² + C θ) R m0.                                                   {#eq:l-24-s-size}

*The derivative.* At fixed ω, d(ϑ) does not depend on v, and r0′ = 1. So S_st′ = S_st (κ + ν′/ν + 2iλκ′/(1 + 2iλκ)),
and with |ν′/ν| ≤ C (1 + 1/x) and |κ′| ≤ c_R κ^(1+α) ≤ c_R κ² (κ ≥ 1),

    |S_st′ − κ S_st| ≤ (C (1 + 1/x) + 2 c_R λκ²) |S_st| ≤ C θ κ |S_st|,

since 1 + 1/x = κ (1/κ + 1/(κx)) and λκ² ≤ θκ. In S_U, (env^(N−1))′ = κ_(N−1) env^(N−1) with κ_(N−1) ≤ 2κ; Ξ is affine
in c_N with ∂Ξ/∂c_N = −1, and ∂Ξ/∂T = i/(T + i)², so |Ξ′| ≤ |c_N′| + |T′| ≤ C + c_R λ (2κ)^(1+α) ≤ Cκ, by (H_N) for
κ_(N−1) and λκ^α ≤ λκ ≤ 1. Hence |(Γ_R Ξ env^(N−1))′| ≤ Cκ |env^(N−1)|, and |S_U′| ≤ C κ Λ λ³ A |d| env ≤ C θ κ R m0. By
[[eq:l-24-s-split]], |E_S′| is at most κ times the bound on |E_S| used above, so |E_S′| ≤ C θ κ R m0. Since
R m0 ≤ |S_st| and, by [[eq:l-24-s-size]], |S_st| ≤ |S| + C θ R m0 ≤ |S| + C θ |S_st|,

    | |S′| − κ |S| | ≤ |S′ − κ S| ≤ |S_st′ − κ S_st| + |S_U′| + κ |S_U| + |E_S′| + κ |E_S| ≤ C θ κ |S|/(1 − C θ).

As θ → 0 with λ, this and [[eq:l-24-s-size]] give [[eq:l-24-s-two-sided]] once λ is small. The bound Λ ≤ λ was shown
above, and λκ ≤ λ^(δ′) is [[lem:l-24-kappa]]. ∎

Where R is small the bounds are not claimed. The bound on E_S in [[eq:l-24-s-split]] keeps the term C λ⁴ env, which
carries no factor |ν| |d|, while R m0 = λ³ A env |ν| |d|; so E_S need not be small against R m0 at points where |ν| |d|
is of order λ or smaller. The proof of [[thm:l-24]] uses [[eq:l-24-s-bounds]] only where R ∈ [1 − 2λ^γ, 1 + 2λ^γ], which
lies in [1/2, 1.1] once 2λ^γ ≤ 1/10. So, for λ small, the conclusions of [[prop:l-24-transition]] hold at every point of
the band with 1/2 ≤ R ≤ 1.1.

**Remark {#rem:l-24-sharp}** (The factor 2 − R.) The constant 2 of [[lem:l-24-margin]] is approached as v ↓ v_s. Let
env be positive and log-concave on (v_s, v_s + x0] with env(v) → 0 as v ↓ v_s. Then κ is nonincreasing there and
κ(v) → ∞ as v ↓ v_s, since a finite limit K would give log env(v) ≥ log env(v_s + x0) − K x0 for every v in
(v_s, v_s + x0]; so ς → 0, and both bounds of [[eq:l-24-margin-bounds]] tend to 2. So the constant 2 in
[[eq:l-24-transition]] cannot be raised; nor can the coefficient of R be lowered, as follows. If at (v, ω) also
|S′| ≥ 0.999 κ |S| (as for any constant multiple of env, for which |S′| = κ|S|) and |S| ≥ 0.999 R m0, with ς ≤ 10⁻³
and √μ0 κ ≥ 10³, then (1 + ς/8)/(√μ0 κ) ≤ 1.001 · 10⁻³, 0.999² ≥ 0.998, and the upper bound of
[[eq:l-24-margin-bounds]] gives

    m0′ − |S′| ≤ (2.001001 − 0.998 R) κ m0,

which is 0.903201 κ m0 at R = 1.1 and below 0.93 κ m0 for every R ≥ 1.075. For such S no bound m0′ − |S′| ≥ 0.93 κ m0
holds on 1.075 ≤ R ≤ 1.1, and at R = 1.1 the constant 0.89 of [[prop:l-24-transition]] is within 0.014 of the best
constant for such S. The first-degree amplitude is such an S at every point of the band with R ≥ 1/2 once λ is small:
the reverse bounds are part of [[eq:l-24-s-two-sided]], ς ≤ 10⁻³ is [[prop:l-24-band]], and √μ0 κ ≥ 10³ holds since κ
tends to ∞ uniformly on the band ([[lem:l-24-kappa]]).

**Corollary {#cor:l-24-period}** (One carrier period.) Let t be real and I := [t, t + 2πλ]. Suppose that at every point
of I [[prop:l-24-transition]] applies with R ≤ 1.1 and √μ0 κ ≥ 2, and that

    2πλ sup_I (|κ′|/κ + 3κ) ≤ 1/26.                                                                {#eq:l-24-period-cond}

Then

    m0(t + 2πλ) − m0(t) + Re[(S(t + 2πλ) − S(t)) e^(it/λ)] ≥ 1.7 πλ κ(t) m0(t).                     {#eq:l-24-period}

Under (H_N) on I with κ ≥ 1 there, |κ′|/κ ≤ c_R κ^α ≤ c_R κ, so [[eq:l-24-period-cond]] holds once
2π (c_R + 3) λ sup_I κ ≤ 1/26. For a carrier period I contained in the band on which 1/2 ≤ R ≤ 1.1, every hypothesis
holds once λ is small: [[prop:l-24-transition]] applies at each point of I by [[prop:l-24-band]] and
[[prop:l-24-s-bounds]]; and by [[lem:l-24-kappa]], (α c_R x_λ)^(−1/α) ≤ κ ≤ K_λ on I, so √μ0 κ ≥ 2 and κ ≥ 1 once
x_λ is small, and 2π (c_R + 3) λ K_λ ≤ 1/26 once λ is small.

*Proof.* By [[lem:l-24-margin]] with ς ≤ 10⁻³ and √μ0 κ ≥ 2,
0 < m0′/m0 ≤ (2 + 1.000125/2) κ ≤ 3κ. So |(log(κ m0))′| = |κ′/κ + m0′/m0| ≤ |κ′|/κ + 3κ, and by [[eq:l-24-period-cond]]
log(κ m0) varies by at most 1/26 on I. As e^y < 1/(1 − y) for 0 < y < 1, e^(1/26) < 26/25, so κ m0 ≥ (25/26) κ(t) m0(t)
on I. The left side of [[eq:l-24-period]] is ∫_I (m0′(s) + Re[S′(s) e^(it/λ)]) ds ≥ ∫_I (m0′ − |S′|) ds, and by
[[prop:l-24-transition]] this is at least 0.89 · 2πλ · (25/26) κ(t) m0(t) ≥ 1.71 πλ κ(t) m0(t). ∎

**Remark {#rem:l-24-eps}** (The degree-two terms against the margin.) The proof of [[thm:l-24]] bounds the degree-two
terms at the boundary through the costs ε_c(v) := Σ_(i≤c) sup_(v′≤v) |env^(i)(v′)|, for fixed c ≥ 1, among them
c = M* := 2N + 8, the cost of the expansion on the boundary in [[ch:equality-layer]]. No bound m0 ≥ c′ ε_c² with c′ > 0
independent of λ holds in the band: there ε_c ≥ env′ = κ env, while by [[eq:l-24-m0]] and [[eq:l-24-logconcave]]
m0 = (a_1 + a_2)/κ ≤ (A² env²/(9 √μ0)) (1 + 1/(2 √μ0 κ)), so m0/ε_c² ≤ C/κ², which tends to 0 with λ by
[[lem:l-24-kappa]]. What holds, and suffices, follows from the interpolation inequality on a half-line
[[pending:lemma-l5]], sup_(v′≤v) |env^(i)(v′)| ≤ C_(i,m) E(v)^(1−i/m) (sup_(v′≤v) |env^(m)(v′)|)^(i/m) for 0 < i < m.
Take m := 56c, env^(m) being bounded. At a point of the band, E ≤ λ^(3−δ) ≤ 1 gives ε_c ≤ C E^(1−c/m); and
E = env ≥ λ^(3+δ), m0 ≥ A² env²/(10 √μ0) (as in the proof of [[prop:l-24-s-bounds]]) and 2(3 + δ)c/m ≤ 1/8 give

    ε_c(v)² ≤ C E(v)^(2−2c/m) ≤ C λ^(−1/8) m0(v),                                                   {#eq:l-24-eps}

with C independent of λ and v. So the degree-two increments over one carrier period, at most C κ λ² ε_c² and
C λ^(N−6) ε_c², are at most C κ λ^(15/8) m0 and C λ^(N−6−1/8) m0, both below πλκ m0/4 for λ small, as N ≥ 9 and
κ ≥ κ̂ in the band.
