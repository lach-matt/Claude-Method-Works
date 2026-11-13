## The boundary at equality, II: the very edge and the dips {#ch:equality-edge}

This chapter continues [[ch:equality-layer]] at the left edge v_s of the envelope, where the window argument of
[[thm:layer]] stops. There the margin m0, the first-degree term and the degree-two terms of g_λ⁻¹(dΦ0, dΦ0) on the
boundary all vanish to every order, and the expansion in λ of [[ch:equality-layer]] stops being ordered: on the *very
edge*, where λκ ≥ 1 with κ := (log env)′, every derivative of env costs more than the phase does. We decide the
causal character of the boundary there in three steps. First, for the solutions of [[thm:past-construction]], the
part of g_λ of first degree in the waves is written exactly, as a convolution of env with an explicit kernel against
the phase, and a kernel lemma evaluates it for every λ ([[thm:edge-past]]). Second, for the metric g_λ of
[[thm:main]], the first-degree part on the very edge is carried by the constraint correction of [[ch:data]] at first
degree; its value on the horizon is computed to leading order ([[prop:edge-horizon-value]]), and [[thm:very-edge]]
shows that on every interval of length 4πλ below a fixed power of λ, down to v_s, the boundary has timelike and
spacelike points on every column, for every admissible τ0. The degree-two terms are bounded at every depth of the edge
by a localisation of the remainder estimates ([[lem:edge-localisation]]). Third, in the band λ^(3+δ) ≤ E ≤ λ^(3−δ) of
[[prop:layer-regions]] the ratio of the first-degree amplitude to the margin crosses 1 once per column, and the
boundary switches from timelike points to spacelike once ([[thm:l-24]]). The hypotheses on the envelope are properties
of its edge; we prove them, for every order, for the envelope of the numerical point and for the edges exp(−a/x)
([[sec:edge-envelope]]). For some C_c^∞ envelopes whose intervals of zeros accumulate at the edge, intervals of length
4πλ below λ^(3+δ) on which the boundary is spacelike throughout occur for every small λ ([[prop:edge-dips]]): some
regularity of the edge is needed.

Throughout, μ0 = √72 l5², and the notation is that of [[ch:equality-layer]]: g0, the seed g0°, r_q, Φ0, Φ0♯ = ∂_v +
β_Φ ∂_r, the margin m0 of [[eq:eq-margin]], the coefficient ν of [[eq:layer-nu]], the angular factors d_1, d of
[[eq:layer-divergence]], the operators 𝒯, R_X, D_X, Pol and Pol⁺ of [[sec:layer-operators]], the profiles H_j of
[[def:layer-profiles]], the level E(v) and the costs ε_c(v) of [[eq:layer-costs]], M* := 2N + 8, and the ratio
R(v, x̂) := λ³ A env(v) |ν(v − τ0)| |d(ϑ)|/m0(v) of [[sec:layer-regions]]. A boundary point is X = (v, r_q(v), x̂),
x̂ ∈ S³ with polar angle ϑ. The phase is θ.

### Setting and hypotheses on the edge {#sec:edge-setting}

*The inverse of s.* On functions of v that vanish on (−∞, v_s] put s := ∂_v + i/λ and

    (s⁻¹g)(v) := ∫_(v_s)^v e^(−i(v−v′)/λ) g(v′) dv′ = ∫_0^∞ e^(−iu/λ) g(v − u) du,                    {#eq:edge-sinv}

so that s s⁻¹ g = s⁻¹ s g = g and ∫_(v_s)^v e^(iv′/λ) g(v′) dv′ = e^(iv/λ) (s⁻¹g)(v). Since ∂_v = s − i/λ,

    s⁻¹ ∂_v g = g − (i/λ) s⁻¹g,      (s⁻¹g)′ = g − (i/λ) s⁻¹g.                                      {#eq:edge-sinv-parts}

Put I_0 := env and

    I_n(v) := (s^(−n) env)(v) = ∫_0^∞ u^(n−1)/(n − 1)! e^(−iu/λ) env(v − u) du      (n ≥ 1),        {#eq:edge-in}

so that s I_n = I_(n−1). Where env > 0 put κ := (log env)′ and, where env^(k) > 0, κ_k := (log env^(k))′ =
env^(k+1)/env^(k), so κ_0 = κ. We write x := v − v_s, s̃ := κ(v) + i/λ, T0 := λκ and T := λκ_(N−1). The *very edge*
is the set of v near v_s with λκ(v) ≥ 1.

**Definition {#def:edge-hypotheses}** (Hypotheses on the edge.) Let x0 > 0, α ∈ (0, 1), and let c_R, c_j, c_t, c_*
be positive constants. On the interval (v_s, v_s + x0] consider:

    (H_N)     for k ≤ N: env^(k) > 0 and log-concave, 1/2 ≤ κ_k/κ ≤ 2 and |κ_k′| ≤ c_R κ_k^(1+α);
              for j ≤ N + 2: |env^(j)| ≤ c_j κ^j env;
    (H_N+2)   (H_N) with N + 2 in place of N and the same α;
    (H_t)     κ − κ_(N−1) ≥ c_t κ^α;
    (H_D)     κ(v_s + y/2) κ(v_s + 4y)^c env(v_s + 4y) → 0 as y ↓ 0, for every c > 0;
    (H_*)     κ(v) (v − v_s)² ≥ c_*;
    (B_J)     |env^(j)| ≤ c_j κ^j env for j ≤ J.

These are properties of env near v_s alone. [[sec:edge-envelope]] proves all of them, for every N and J, on short
intervals at the edge, for the envelope of the numerical point and for exp(−a/(v − v_s)).

**Lemma {#lem:edge-kappa}** (Log-concave flat edges.) Let env be positive and log-concave on (v_s, v_s + x0] with
env(v) → 0 as v ↓ v_s and |κ′| ≤ c_R κ^(1+α) there, 0 < α < 1. Then on (v_s, v_s + x0]:

(a) κ is nonincreasing, κ(v) ≥ (α c_R x)^(−1/α), and κ(v) → ∞ and κ(v) x → ∞ as v ↓ v_s;

(b) if v_s < t ≤ v and v − t ≤ U_*(v) := (1 − 2^(−α)) κ(v)^(−α)/(α c_R), then κ(t) ≤ 2κ(v); if v ≤ t ≤ v_s + x0 and
t − v ≤ κ(v)^(−α)/(α c_R), then κ(t) ≥ 2^(−1/α) κ(v);

(c) for every j ≥ 0 there is x_j ∈ (0, x0] such that κ(v′)^j env(v′) ≤ κ(v)^j env(v) e^(−κ(v)(v − v′)/2) for
v_s < v′ ≤ v ≤ v_s + x_j;

(d) ∫_(v_s)^v env ≤ env(v)/κ(v) and ∫_(v_s)^v env² ≤ env(v)²/(2κ(v));

(e) if (H_D) holds, then κ(v)^p env(v) → 0 as v ↓ v_s, for every p ≥ 0.

*Proof.* (a) As log env is concave and differentiable, κ is nonincreasing. If κ were bounded by a number B on (v_s,
v_s + x0], then log env(v) ≥ log env(v_s + x0) − B x0 for every v there, against env(v) → 0; so κ(t) → ∞ as t ↓ v_s.
Now (κ^(−α))′ = α κ^(−α−1) |κ′| lies in [0, α c_R]: for v_s < t < v, κ(v)^(−α) ≤ κ(t)^(−α) + α c_R (v − t), and t ↓
v_s gives κ(v)^(−α) ≤ α c_R x. Then κ x ≥ (α c_R)^(−1/α) x^(1−1/α) → ∞, as 1 − 1/α < 0.

(b) With the same derivative bound, κ(t)^(−α) ≥ κ(v)^(−α) − α c_R (v − t) ≥ 2^(−α) κ(v)^(−α) in the first case, and
κ(t)^(−α) ≤ κ(v)^(−α) + α c_R (t − v) ≤ 2 κ(v)^(−α) in the second.

(c) By (a) there is x_j with 2 j c_R κ^(α−1) ≤ 1 on (v_s, v_s + x_j]. There (log(κ^j env))′ = κ + jκ′/κ ≥ κ − j c_R κ^α
≥ κ/2 ≥ κ(v)/2 on [v′, v], since κ is nonincreasing; integrate over [v′, v].

(d) By concavity, log env(v − u) ≤ log env(v) − κ(v) u for 0 ≤ u < x, and env = 0 on (−∞, v_s]; integrate env(v − u)
≤ env(v) e^(−κ(v)u) and its square over u ≥ 0.

(e) For p > 1 put y := x/4 and c := p − 1 in (H_D): κ(v_s + y/2) ≥ κ(v), so κ(v)^p env(v) ≤ κ(v_s + y/2) κ(v)^c
env(v) → 0. For p ≤ 1 use p = 2 and κ ≥ 1 near v_s. ∎

### The kernel lemma and the inverse of s {#sec:edge-kernel}

**Lemma {#lem:edge-kernel}** (The kernel lemma.) Let env be positive and log-concave on (v_s, v_s + x0], with κ > 0
there, and let v_s < v ≤ v_s + x0. For every λ > 0:

(a) |I_n(v)| ≤ env(v)/κ(v)^n for n ≥ 1.

(b) I_2(v) = env(v) s̃^(−2) (1 + ρ_2) with |ρ_2| ≤ R_2(v), where, with ψ′(u) := κ(v − u) − κ(v) ≥ 0 and ψ″(u) :=
−κ′(v − u) ≥ 0,

    R_2(v) := ∫_0^x [κ(v)⁻¹ (ψ″ + ψ′²) + ψ′ + u (ψ″ + ψ′²)] env(v − u)/env(v) du;                      {#eq:edge-r2}

R_2 does not depend on λ. If |κ′| ≤ c_R κ^(1+α) on (v_s, v], 0 < α < 1, and κ(v) ≥ 1, then

    R_2(v) ≤ 3 · 2^(1+α) c_R κ^(α−1) + 2^(5+2α) c_R² κ^(2α−2) + T_2(v),
    T_2(v) ≤ x (1 + x) sup_(v_s<v′≤v−U_*) (κ² + |κ′| + κ)(v′) env(v′)/env(v),                     {#eq:edge-r2-bound}

with U_* = U_*(v) of [[lem:edge-kappa]] (b).

(c) If moreover, for j ≤ n + 1 and v_s < v′ ≤ v, |env^(j)(v′)| ≤ c_j κ(v′)^j env(v′) and κ(v′)^j env(v′) ≤ c_j
κ(v)^j env(v) e^(−κ(v)(v − v′)/2), then |I_n(v)| ≤ C_n env(v) λ^n (1 + λκ(v)), C_n depending on n and the c_j; with
(a), |I_n(v)| ≤ C′_n env(v) min(λ, 1/κ(v))^n.

*Proof.* (a) By concavity of log env, env(v − u) ≤ env(v) e^(−κ(v)u) for u ≥ 0 (env = 0 left of v_s), and
∫_0^∞ u^(n−1) e^(−κu) du/(n − 1)! = κ^(−n).

(b) Put e^(−ψ(u)) := env(v − u) e^(κ(v)u)/env(v) for 0 ≤ u < x and e^(−ψ) := 0 for u ≥ x. Then ψ(0) = ψ′(0) = 0 and ψ
≥ 0, with ψ′, ψ″ as stated, of one sign because κ is nonincreasing; and f := e^(−ψ) − 1 is C¹ on [0, ∞), since env
and env′ vanish at v_s. As ∫_0^∞ u e^(−s̃u) du = s̃^(−2) and e^(−iu/λ) env(v − u)/env(v) = e^(−s̃u) e^(−ψ),

    I_2(v)/env(v) − s̃^(−2) = ∫_0^∞ u e^(−s̃u) f(u) du.

Integrate by parts with u e^(−s̃u) = −(d/du)[(u/s̃ + 1/s̃²) e^(−s̃u)]: the boundary terms vanish (f(0) = 0, and the
modulus of e^(−s̃u) is e^(−κu)), and f′ = −ψ′ e^(−ψ) on (0, x), f′ = 0 beyond. So the right side is −s̃^(−2) ∫_0^x G_1
e^(−s̃u) du − s̃^(−1) ∫_0^x G_2 e^(−s̃u) du with G_1 := ψ′ e^(−ψ) and G_2 := u ψ′ e^(−ψ). Both vanish at u = 0 and as u ↑
x (G_1 = −f′), so a second integration by parts gives ∫_0^x G_m e^(−s̃u) du = s̃^(−1) ∫_0^x G_m′ e^(−s̃u) du, and

    ρ_2 = −J_1 − s̃ J_2,      J_m := s̃^(−1) ∫_0^x G_m′ e^(−s̃u) du.

Here |G_1′| ≤ (ψ″ + ψ′²) e^(−ψ), |G_2′| ≤ (ψ′ + u(ψ″ + ψ′²)) e^(−ψ), e^(−ψ) |e^(−s̃u)| = env(v − u)/env(v) and |s̃| ≥
κ(v); so |ρ_2| ≤ R_2. For [[eq:edge-r2-bound]] split [0, x] at U_*. On [0, U_*], κ(v − u) ≤ 2κ by [[lem:edge-kappa]]
(b), so with c := c_R (2κ)^(1+α) we have ψ″ ≤ c and ψ′ ≤ c u, and env(v − u)/env(v) ≤ e^(−κu); hence the integral over
[0, U_*] is at most ∫_0^∞ [κ⁻¹(c + c²u²) + c u + u(c + c²u²)] e^(−κu) du = 3c/κ² + 8c²/κ⁴, which is the sum of the
first two terms of [[eq:edge-r2-bound]]. On [U_*, x], ψ′ ≤ κ(v − u) and ψ″ = |κ′(v − u)|, and κ(v) ≥ 1; the bracket is
at most (1 + u)(κ² + |κ′|)(v − u) + κ(v − u), and u ≤ x.

(c) Put φ(u) := u^(n−1) env(v − u)/(n − 1)! and T_λ := −iλ. For h smooth on [0, ∞), vanishing for large u,
integration by parts with e^(−iu/λ) = (d/du)(iλ e^(−iu/λ)) gives ∫_0^∞ h e^(−iu/λ) du = T_λ h(0) + T_λ ∫_0^∞ h′
e^(−iu/λ) du. Applied n + 1 times to h = φ,

    I_n = Σ_(k=0)^n T_λ^(k+1) φ^(k)(0) + T_λ^(n+1) ∫_0^∞ φ^(n+1) e^(−iu/λ) du,

with φ^(k)(0) = 0 for k < n − 1, φ^(n−1)(0) = env(v) and φ^(n)(0) = −n env′(v). By Leibniz's rule φ^(n+1) is a sum of
constants times u^(j−2) env^(j)(v − u), 2 ≤ j ≤ n + 1, and by the two hypotheses ∫_0^∞ u^(j−2) |env^(j)(v − u)| du ≤
c_j² κ(v)^j env(v) ∫_0^∞ u^(j−2) e^(−κ(v)u/2) du = c_j² (j − 2)! 2^(j−1) κ(v) env(v). With |env′| ≤ c_1 κ env, we
get |I_n| ≤ λ^n env + n c_1 λ^(n+1) κ env + C λ^(n+1) κ env. If λκ ≤ 1 this is at most C λ^n env = C env min(λ,
1/κ)^n; if λκ > 1, (a) gives env κ^(−n) = env min(λ, 1/κ)^n. ∎

**Lemma {#lem:edge-sinv}** (The inverse of s on a log-concave function.) Let env satisfy the hypotheses of
[[lem:edge-kappa]] on (v_s, v_s + x0]. Let g be smooth on ℝ, zero on (−∞, v_s], positive and log-concave on (v_s,
v_s + x0], with κ_g := (log g)′ ∈ [κ/2, 2κ], |κ_g′| ≤ c_R κ_g^(1+α) and |g^(j)| ≤ c_j κ^j g for j ≤ 3 there. Put s̃_g
:= κ_g + i/λ, T_g := λκ_g, and define ρ_g by

    s⁻¹g = g s̃_g⁻¹ (1 + ρ_g).                                                                      {#eq:edge-rho-g}

There are x_g ∈ (0, x0] and C, depending on c_R, α and the c_j, such that on (v_s, v_s + x_g], for every λ > 0:

(a) |ρ_g| ≤ C ϵ′, where ϵ′ := min{(λκ)² + λκ^α, κ^(α−1)};

(b) (s⁻¹g/g)′ = −ρ_g and ρ_g′ = κ_g′ (1 + ρ_g)/s̃_g − s̃_g ρ_g;

(c) if moreover g′, g″ and g‴ are positive and log-concave on (v_s, v_s + x0], with logarithmic derivatives κ_1, κ_2,
κ_3 in [κ/2, 2κ] and |κ_i′| ≤ c_R κ_i^(1+α), then for λκ ≤ 1/4

    ρ_g = −λ² κ_g′ + O((λκ)³ κ^(α−1) + (λκ)² κ^(2α−2)),                                           {#eq:edge-rho-sharp}

so that |ρ_g| ≤ C (λκ)² κ^(α−1) and |ρ_g|/λ ≤ C λ κ^(1+α).

*Proof.* (a), first for λκ ≤ 1/4. Three integrations by parts by [[eq:edge-sinv-parts]] (g and its derivatives vanish
at v_s) give s⁻¹g = −iλ g + λ² g′ + iλ³ g″ − iλ³ s⁻¹g‴. Since g″ = (κ_g² + κ_g′) g and s̃_g⁻¹ = −iλ (1 − iT_g)⁻¹ =
−iλ (1 + iT_g − T_g²) + O(λ⁴κ³), the difference s⁻¹g − g s̃_g⁻¹ equals iλ³ κ_g′ g − iλ³ s⁻¹g‴ + O(λ⁴κ³ g). Take
x_g so small that 12 c_R κ^(α−1) ≤ 1 there ([[lem:edge-kappa]] (a)). Then (log(κ³ g))′ = κ_g + 3κ′/κ ≥ κ/2 − 3 c_R κ^α
≥ κ/4 on (v_s, v], so κ(v′)³ g(v′) ≤ κ(v)³ g(v) e^(−κ(v)(v−v′)/4), and |s⁻¹g‴| ≤ c_3 ∫_(v_s)^v κ³ g ≤ 4 c_3 κ² g. As
T_g ≤ 2λκ ≤ 1/2 gives |g s̃_g⁻¹| ≥ g λ/2, |ρ_g| ≤ C (λ² κ^(1+α) + (λκ)² + λ³κ³) ≤ C ((λκ)² + λκ^α).

(a) for every λ. Put e^(−ψ(u)) := g(v − u) e^(κ_g(v)u)/g(v) for u < x, zero beyond. As in [[lem:edge-kernel]] (b),
g⁻¹ s⁻¹g − s̃_g⁻¹ = ∫_0^∞ e^(−s̃_g u)(e^(−ψ) − 1) du, and one integration by parts (ψ(0) = 0) gives

    ρ_g = −∫_0^x e^(−s̃_g u) ψ′(u) e^(−ψ(u)) du,      ψ′(u) = κ_g(v − u) − κ_g(v) ≥ 0,

so |ρ_g| ≤ ∫_0^x ψ′(u) g(v − u)/g(v) du. On [0, U_g], U_g := (1 − 2^(−α)) κ_g(v)^(−α)/(α c_R), the argument of
[[lem:edge-kappa]] (b) for κ_g gives κ_g(v − u) ≤ 2κ_g(v), so ψ′(u) ≤ c_R (2κ_g)^(1+α) u, and with g(v − u) ≤ g(v)
e^(−κ_g u) that part is at most 2^(1+α) c_R κ_g^(α−1). On [U_g, x], ψ′(u) g(v − u) ≤ κ_g(v − u) g(v − u) = g′(v − u),
whose integral is g(v − U_g) ≤ g(v) e^(−κ_g U_g). So |ρ_g| ≤ 2^(1+α) c_R κ_g^(α−1) + exp(−(1 − 2^(−α)) κ_g^(1−α)/(α
c_R)) ≤ C κ^(α−1). For λκ ≤ 1/4 take the smaller of the two bounds; for λκ > 1/4, (λκ)² > κ^(α−1) once κ ≥ 16^(1/(1−α)),
which holds near v_s, and ϵ′ = κ^(α−1).

(b) By [[eq:edge-sinv-parts]], (s⁻¹g)′ = g − (i/λ) s⁻¹g, so q := s⁻¹g/g satisfies q′ = 1 − (i/λ) q − κ_g q = 1 −
s̃_g q = −ρ_g; and ρ_g = s̃_g q − 1 gives ρ_g′ = κ_g′ q + s̃_g q′.

(c) From the three integrations by parts, with s̃_g = (i/λ)(1 − iT_g),

    1 + ρ_g = s̃_g s⁻¹g/g = (1 − iT_g) [1 + iT_g − λ² g″/g + λ² s⁻¹g‴/g].

Write g″/g = κ_g κ_1 and g‴/g = κ_g κ_1 κ_2, and apply (a) for every λ to g‴, whose logarithmic derivative is κ_3:
s⁻¹g‴ = −iλ g‴ (1 − iT_3)⁻¹ (1 + ρ_3), T_3 := λκ_3, |ρ_3| ≤ C κ^(α−1). So

    1 + ρ_g = 1 + T_g² − (1 − iT_g) λ² κ_g κ_1 [1 + iλκ_2 (1 + ρ_3)/(1 − iT_3)].

If κ_1 = κ_2 = κ_3 = κ_g and ρ_3 = 0, the bracket is 1/(1 − iT_g) and ρ_g = 0. Each difference κ_i − κ_(i−1) (κ_0 :=
κ_g) equals κ_(i−1)′/κ_(i−1), of size at most 2c_R κ^α, and ρ_3 = O(κ^(α−1)). To first order in these deviations,
ρ_g = −T_g² (κ_1 − κ_g)/κ_g + O(T_g³ κ^(α−1)), the deviations of κ_2, κ_3 and ρ_3 carrying the extra factor λκ_2;
and the second-order terms are O(T_g² κ^(2α−2)). Finally T_g² (κ_1 − κ_g)/κ_g = λ² κ_g (κ_1 − κ_g) = λ² κ_g′, since
g″ = (κ_g′ + κ_g²) g. The last two bounds follow from |κ_g′| ≤ c_R (2κ)^(1+α). ∎

### Two signs on a window {#sec:edge-two-signs}

**Lemma {#lem:edge-two-signs}** (Two signs on a window.) Let J := [v, v + 4πλ], S ∈ C²(J; ℂ), ε: J → ℝ and f :=
Re[S e^(i·/λ)] + ε.

(A) If S ≠ 0 on J, arg S varies by at most π/6 on J and |ε(t)| ≤ |S(t)|/4 for every t ∈ J, then f takes both signs on
J.

(B) If |S′| ≥ L0 > 0 and |S″| ≤ L0/(80πλ) on J, and |ε| ≤ πλL0/5 on J, then f takes both signs on J.

*Proof.* (A) t/λ + arg S(t) increases by at least 4π − π/6 > 2π on J, so it meets 0 and π modulo 2π at points t₁,
t₂ ∈ J; f(t₁) ≥ |S(t₁)| − |S(t₁)|/4 > 0 and f(t₂) ≤ −|S(t₂)| + |S(t₂)|/4 < 0.

(B) By Taylor's formula, S(t) = S(v) + S′(v)(t − v) + R(t) with |R(t)| ≤ (4πλ)² L0/(2 · 80πλ) = πλL0/10. Put t0 :=
v − S(v)/S′(v) = α0 + iβ0 (S′(v) ≠ 0), so S(t) = S′(v)(t − t0) + R(t). At the points t_k ∈ J where e^(i(t/λ + arg
S′(v))) = ±1, which are πλ apart with alternating signs, S′(v) e^(it_k/λ) = ±|S′(v)| is real, so Re[S′(v)(t_k − t0)
e^(it_k/λ)] = ±|S′(v)| (t_k − α0), the β0-part vanishing; hence |f(t_k) ∓ |S′(v)|(t_k − α0)| ≤ πλL0/10 + πλL0/5 =
3πλL0/10. Where |t_k − α0| ≥ πλ/2, |S′(v)| |t_k − α0| ≥ πλL0/2 > 3πλL0/10, so f(t_k) has the sign ±sign(t_k − α0).
Remove from J the gap (α0 − πλ/2, α0 + πλ/2), of length πλ. If one of the two remaining sides has length at least
2πλ, it contains two consecutive t_k, of opposite types and with t_k − α0 of one sign: f takes both signs. Otherwise
both sides have length in (πλ, 2πλ), since their lengths add up to at least 3πλ; each contains a t_k, and the gap
contains exactly one; so the last t_k of the left side and the first of the right side are two steps apart, of the
same type, and on opposite sides of α0: f takes both signs. ∎

### Degree two and localisation {#sec:edge-degree-two}

We treat two cases together. In *case P*, g_λ is the metric of [[thm:past-construction]] with N := N_P stages
([[sec:layer-past]]), M := M_P = 2N_P + 8, and S(V) := (P ∪ Ω) ∩ {v ≤ V}. In *case Ω*, g_λ is the metric of
[[thm:main]] as in [[thm:layer]], N = K + 3, M := M* = 2N + 8, and S(V) := Ω ∩ {v ≤ V}. In both, dRic^H and dD are the
linearisations at the seed g0° with the gauge relative to g0° ([[lem:layer-seed-operators]]), and N_V := S(V) ∩
{v = V}.

*The part of first degree.* By [[lem:layer-seed-operators]] (b) and [[prop:layer-structure]] (a), for every symmetric
2-tensor H(v, r, ϑ) of the class of [[lem:layer-seed-operators]],

    dRic^H(H e^(iv/λ)) = e^(iv/λ) (−𝒫(sH) + Q H),      𝒫 := i𝒯 = ∇_ℓ + 3/(2r),                         {#eq:edge-p-q}

with s acting on the v-dependence and 𝒫, Q containing no derivative in v; both sides are polynomials in 1/λ, and the
coefficient of λ⁰ gives dRic^H(H) = −𝒫 ∂_v H + Q H. In case P let b_0 := r^(1/2) T, so that H_1 = A env b_0 and
𝒫 b_0 = 0, and let h^(1) := Re[λ e^(iv/λ) A env b_0] + h̃, where h̃ solves dRic^H(h̃) = −Re[λ e^(iv/λ) A env Q b_0] on
P ∪ Ω with nothing coming in: h̃ is the limit, as τ_n → −∞, of the solutions with zero data on Σ̂_(τ_n), which exists
by the scheme of [[prop:far-region]] with the linear estimate of [[lem:edge-resummation]] (b) below. So h^(1) solves
dRic^H(h^(1)) = 0, vanishes on {v ≤ v_s}, and its incoming radiation is that of the wave Re[λ H_1 e^(iv/λ)] and
nothing else. In case Ω let

    h_app^(1) := Re Σ_(j≤N+1) λ^j H_j e^(iv/λ),                                                    {#eq:edge-happ}

let Φ^(1) be the part of first degree of the constraint map of g_app's data on Σ_τ0 (the linearised constraint map at
the seed's data applied to the data of h_app^(1)), and let U^(1) = (a^(1), ϖ^(1), q^(1)) solve the linear system
[[eq:data-linear]] with the coefficients of [[lem:constraints-evolution]] at the seed's data, forcing −Φ^(1) and zero
data at r = a ([[lem:linear-evolution]]). Then h^(1) is the solution of dRic^H(h) = 0 on Ω whose Cauchy data on Σ_τ0
are those that the construction of [[sec:data-proof]], linearised at the seed, assigns to (h_app^(1), U^(1)): the data
of h_app^(1), the spatial part changed by a^(1) dr ⊗ dr with the lapse and the shift vector kept (so the components
(τ ·) change by a^(1) dr(β) dr and a^(1) dr(β)², β the seed's shift), ∂_τ of the spatial part changed through ϖ^(1)
Π + q^(1) ⊗ dr + dr ⊗ q^(1) and a^(1) with the lapse and shift kept, and ∂_τ of lapse and shift fixed by the
linearised D = 0. Put e := h^(1) − h_app^(1). By [[lem:edge-constraint]] (i) below,

    dRic^H(e) = −λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)]      on Ω,                                       {#eq:edge-e-equation}

with the data that U^(1) induces. In both cases put

    r2 := g_λ − g0° − h^(1).

**Lemma {#lem:edge-u-difference}** (The correction at degree two.) Let U be the correction of
[[prop:exact-correction]] and U^(1) as above. For τ0 + r ≤ v ≤ v_♯ and j ≤ 3, sup_(r′≤r) ‖∂_r^j (U −
U^(1))(r′)‖_(H^s(S³)) ≤ C λ^(N−2−j) ε_c(v)², with a fixed cost c and s as in [[prop:exact-correction]].

*Proof.* Write the constraint map of (γ_U, κ_U) as 𝒞(γ, κ) + 𝔏 U + 𝒬(U), as in the proof of
[[prop:exact-correction]], and let 𝔏_0 be the linearisation at the seed's data. Then U − U^(1) solves 𝔏_0(U − U^(1))
= −(𝒞(γ, κ) − Φ^(1)) − 𝒬(U) − (𝔏 − 𝔏_0) U with zero data at r = a. (i) The profiles of 𝒞(γ, κ) vanish below order
N − 2 ([[lem:gauge-hierarchy]]); its part of degree at least two has every monomial with two factors of degree one or
one factor of degree two ((F2) of [[sec:layer-flat]], [[lem:layer-flat]] (b), (c)), each radial derivative costing
λ⁻¹ through the phase on Σ_τ0; so, by Taylor's formula in λ as in the proof of [[lem:layer-flat]] (e), it is at most C
λ^(N−2−j) ε_c² with j radial derivatives. (ii) 𝒬(U) is at most C λ⁻¹ |U|²_(C¹), and |∂_r^j U| ≤ C λ^(N−2−j) ε
([[lem:layer-flat]] (e)): at most C λ^(2N−7−j) ε², below λ^(N−2−j) ε² for N ≥ 5. (iii) 𝔏 − 𝔏_0 has coefficients of
degree one, with j radial derivatives at most C λ^(−j) ε; times U this is C λ^(N−2−j) ε². [[lem:linear-evolution]] on
[a, r], with its constant on [a, b1], and the derivative count of [[lem:layer-flat]] (e) give the bound. ∎

**Lemma {#lem:edge-degree-two}** (Degree two.) Let v1 := v + ρ_v, where ρ_v is the reach of the remainder estimate
used at the boundary point X = (v, r_q(v), x̂): ρ_v := 2C1λ(τ_end − τ0) in case Ω ([[lem:layer-remainder]]) and ρ_v :=
2C_Pλ(2 + τ_end − τ0) in case P ([[lem:layer-remainder-past]]), or the smaller reach of [[lem:edge-localisation]].
Assume ε_M(v1) ≤ λ⁵. Then for v_s < v ≤ v_♯

    |r2(X)| ≤ C_2 [ε_c(v)² + ε_c(v) η(v1) + η(v1)²],      η(v1) := λ^(N−6) ε_M(v1),
    |(g0 − g0°)(X)| ≤ C ε_0(v)²,                                                                   {#eq:edge-degree-two}

with a fixed cost c and C_2 depending on the quantities of [[sec:layer-setting]] (in case P also on the bounds of
[[thm:past-construction]]).

*Proof.* (1) *The equation.* g_λ solves Ric^H(g_λ) = 0 with the gauge relative to g0. The gauge vectors relative to g0
and to g0° differ by g^(ab)(Γ[g0°] − Γ[g0])^ρ_ab. By [[eq:layer-christoffel]] with μ in place of μ0, and Γ^r_vv =
μ′/(2r²) + F μ/r³, every component of Γ[g0] − Γ[g0°] is a polynomial of degree at most two in (μ − μ0, μ′), without
constant term, with coefficients functions of r and of the angles. So Ric^H relative to g0 equals Ric^H relative to g0°
plus a term 𝒜(g) with |𝒜| ≤ C (|μ − μ0| + |μ′| + |μ″|) for (g, ∂g) bounded, and |∂^k Ω^β 𝒜| ≤ C ε_(k+1)(v)² at points
with that v, since 0 ≤ μ − μ0 ≤ (2/9) A² (v − v_s) ε_0², μ′ = (2/9) A² env² and μ″ = (4/9) A² env env′. With u := g_λ −
g0°, g0° vacuum and D(g0°) = 0, Ric^H(g0° + u) = dRic^H(u) + 𝒩(u), and by the quasilinear form [[eq:gauge]] (second
derivatives only in −(1/2) g^(ab) ∂_a ∂_b g) |𝒩(u)| ≤ C (|u| |∂²u| + |∂u|² + |u|²) for |u| + |∂u| small, with
Ω^β-derivatives by Leibniz's rule. As dRic^H(h^(1)) = 0, dRic^H(r2) = −𝒩(u) − 𝒜(g_λ) =: f_2.

(2) *Bounds on u* = (g_app − g0°) + w. By [[lem:layer-flat]] (a)–(c) (case Ω), [[lem:layer-flat-past]] (a)–(c) (case
P) and [[cor:layer-expansion]], |∂^k Ω^β (g_app − g0°)| ≤ C λ^(1−k) ε_c(v′) at points with v = v′, k ≤ 2, each
derivative of a profile [g_j] costing λ⁻¹ only through ∂_θ and the rotations costing nothing, since Ω_ab v = 0; on P
with the decay of the classes E_(3/2), E_2. For w, run [[lem:layer-remainder]] (case Ω), [[lem:layer-remainder-past]]
(case P) with ∂^α, |α| ≤ 4, in place of |α| ≤ 2. The coefficients ∂^j g_app, j ≤ 6, are bounded on the region, since
ε_M(v1) ≤ λ⁵ gives λ^(1−j) ε_j ≤ 1 there; ∂^j w, j ≤ 3, are bounded by step 1 of the proof of
[[thm:uniform-existence]], resp. item 3 of [[thm:past-construction]]; so every coefficient of the energy inequality for
the derivatives of order at most four is bounded, while the forcing term and the data cost λ⁻¹ per derivative
([[lem:layer-flat]] (d), (e), [[lem:layer-flat-past]] (d)). Hence E_4(τ) ≤ C λ^(N−7) ε_M(v1), and Sobolev's inequality
on the slices (step 7 of [[lem:layer-remainder]]) gives |∂^k Ω^β w| ≤ C λ^(N−5−k) ε_M(v1) ≤ C λ^(1−k) η(v1), k ≤ 2.

(3) *The source.* By (2), |u| ≤ C(λε_c + λη), |∂u| ≤ C(ε_c + η) and |∂²u| ≤ C λ⁻¹(ε_c + η), so |𝒩(u)| ≤ C(ε_c +
η)², and |f_2| ≤ C(ε_c(v′)² + ε_c(v′) η(v1) + η(v1)²) at points with v = v′ ≤ v. On P each product carries the decay
of two factors, at least t^(−3), so ‖Ω^β f_2(τ)‖_(L²(Σ̂_τ ∩ S(v))) ≤ C (…) t^(−3/2), integrable in τ.

(4) *The linear estimate.* r2 = 0 on {v ≤ v_s}: there g_λ = g0 = g0° and h^(1) = 0 ([[prop:eq-seed-region]],
[[prop:layer-seed-past]]). In case P, r2 has nothing coming in, since the incoming radiation of g_λ − g0° and of h^(1)
is that of the wave (item 2 of [[thm:past-construction]]), and steps (2) and (4) of the proof of
[[lem:edge-resummation]] (b) give |r2(X)| ≤ C Σ_(|β|≤2) ∫ ‖Ω^β f_2‖ dτ. In case Ω the data of r2 on Σ_τ0 ∩ {v′ ≤ v}
are the part of degree at least two of g_λ's data: g_app's data minus their part of first degree, at most C ε_c(v)²
with their derivatives ([[lem:layer-flat]] (b), (c), (e)), and the data induced by U − U^(1), at most C ε_c(v)² by
[[lem:edge-u-difference]]. [[lem:layer-energy-null]] for the seed (the case μ ≡ μ0) on Ω_v, the lower-order terms of
dRic^H moved to the right and absorbed by Gronwall's inequality, and [[lem:layer-null-pointwise]] from the generator's
point on Σ_τ0 give the same bound, plus C ε_c(v)² from the data. Finally g0 − g0° = (μ − μ0) r⁻² dv ⊗ dv, and
μ − μ0 ≤ C ε_0(v)². ∎

**Lemma {#lem:edge-localisation}** (Localisation at every depth.) Let env be positive and log-concave on (v_s, v_s +
x0], with κ := (log env)′ > 0, |κ′| ≤ c_R κ^(1+α) for some α ∈ (0, 1), and (H_D) there. There are λ_D, x_D > 0
such that for λ ≤ λ_D the bounds of
[[lem:edge-degree-two]] hold with a reach ρ_v ≤ 1/κ(v) at every boundary point X with x = v − v_s ≤ x_D at which
ε_M(v + 1/κ(v)) ≤ λ⁵. If moreover, with c′ := max(c, M), (B_(c′)) holds and κ(v′)^j env(v′) ≤ c_j κ(v)^j env(v)
for v_s < v′ ≤ v ≤ v_s + x0 and j ≤ c′, then at those points

    |r2(X)| ≤ C κ(v)^(2c′) env(v)².                                                                  {#eq:edge-localised}

*Proof.* (1) *Any tilt serves.* Put ψ(τ) := τ − τ0 in case Ω and ψ as in [[lem:layer-remainder-past]] in case P, and
ψ_max := 2 + τ_end − τ0 ≥ ψ. In the proofs of [[lem:layer-remainder]] and [[lem:layer-remainder-past]] the tilt (2C1λ,
resp. 2C_Pλ) is used only to make the face {v + e ψ(τ) = V} have a conormal α = dv + e ψ′ dτ timelike for g_λ, and to
keep the region inside S(V). Let Δ(V) be the supremum over S(V) of the Euclidean operator norm of g_λ⁻¹ − g0⁻¹ on
covectors, weighted by t^(3/2) on P (where ψ′ = t^(−3/2); ψ′ = 1 on Ω). Since g0⁻¹(dv, dv) = 0, g0⁻¹(dv, dτ) = −1 and
g0⁻¹(dτ, dτ) = −(1 + μ/r²), g0⁻¹(α, α) = −2eψ′ − e²ψ′²(1 + μ/r²); and α = (1 + eψ′) dτ + x̂·dx has the Euclidean
norm |α|_e² ≤ 13/4 for eψ′ ≤ 1/2. So for every e with 2Δ(V) ≤ e ≤ 2C1λ (resp. 2C_Pλ), g_λ⁻¹(α, α) ≤ ψ′(−2e + (13/4) Δ(V))
< 0, and the proofs run on R(V, e) := S(V) ∩ {v + eψ(τ) ≤ V} with the same constants (the slices still shrink), and so
does their form with four derivatives in step (2) of [[lem:edge-degree-two]]. Every boundary point X with v(X) + e ψ_max
≤ V lies in R(V, e), so the bound holds there with reach e ψ_max.

(2) *Stage 0* is [[lem:layer-remainder]] (case Ω; |w| ≤ C λ^(N−5) ε_(M*)) or [[lem:layer-remainder-past]] (case P;
there |w| ≤ C λ^(N_P−3) ε_(M_P)) itself, with e_0 := 2C1λ (resp. 2C_Pλ) and reach e_0 ψ_max. Let y_0 be the depth at
which κ(v_s + y_0) e_0 ψ_max = 1; by [[lem:edge-kappa]] (a), κ is nonincreasing and tends to ∞ at v_s, so y_0 exists for
λ small, and y_0 → 0 as λ → 0. At depths x ≥ y_0 the reach of stage 0 is at most 1/κ(v). By [[lem:edge-kappa]] (a),
κ(v_s + y) y → ∞ as y ↓ 0, so 1/κ(v_s + y) ≤ y for y small; in particular e_0 ψ_max ≤ y_0.

(3) *Stage 1* [[pending:issue-1]]. On S(v_s + 4y_0), |g_app − g0| ≤ C λ ε_c(v_s + 4y_0) (with the weight t^(−3/2) on P)
and |w| ≤ C λ^(K−3) (step 1 of the proof of [[thm:uniform-existence]]; item 3 of [[thm:past-construction]], with the
weight t^(−2) on P), so Δ(v_s + 4y_0) ≤ δ_1 := C(λ ε_c(v_s + 4y_0) + λ^(K−3)). Put e_1 := 2δ_1 ≤ e_0 and let y_1 be
the least y with 1/κ(v_s + y) ≥ e_1 ψ_max. By (1), at every boundary point of depth at most 4y_0 − e_1 ψ_max the
bound holds with reach e_1 ψ_max, which is at most 1/κ(v) at depths x ≥ y_1; and 4y_0 − e_1 ψ_max ≥ 3y_0.

(4) *Stage k ≥ 2.* Given stage k − 1, valid at every depth up to 3y_(k−1) with reach e_(k−1) ψ_max ≤ y_(k−1) (for
k = 2 by (3), as e_1 ψ_max ≤ 1/κ(v_s + y_1) ≤ y_1), put

    δ_k := C (λ ε_c(v_s + 4y_(k−1)) + λ^(N−5) ε_M(v_s + 4y_(k−1)))

(λ^(N_P−3) in case P), which bounds Δ(v_s + 3y_(k−1)): |g_app − g0| as in (3), and |w| by stage k − 1 at depths at
most 3y_(k−1), whose reach is at most y_(k−1). Put e_k := 2δ_k and let y_k be the least y with 1/κ(v_s + y) ≥ e_k
ψ_max. Stage k holds at every boundary point of depth at most 3y_(k−1) − e_k ψ_max, with reach e_k ψ_max, which is at
most 1/κ(v) at depths x ≥ y_k. By (B_(c′)) and the second hypothesis, ε_c(V) + ε_M(V) ≤ C κ(V)^(c′) env(V), so δ_k ≤
C′ κ(v_s + 4y_(k−1))^(c′) env(v_s + 4y_(k−1)); by (H_D) this is below 1/(2ψ_max κ(v_s + y_(k−1)/2)) once y_(k−1) is
small, which holds for λ small since y_(k−1) ≤ y_0; so y_k ≤ y_(k−1)/2. Moreover e_k ψ_max ≤ 1/κ(v_s + y_k) ≤ y_k,
so stage k is valid up to 3y_(k−1) − y_k ≥ 3y_k with reach at most y_k, which is the hypothesis at k + 1. So every
depth in [y_k, y_(k−1)] is covered locally by stage k, y_k → 0, and the depths in [y_1, y_0] by stage 1 and those in
[y_0, x_D] by stage 0.

(5) Where the hypothesis of [[lem:edge-degree-two]] holds with v1 = v + ρ_v, ρ_v ≤ 1/κ(v), its bound applies. Under
the further hypotheses, ε_c(v) ≤ C κ(v)^c env(v); κ(v + 1/κ(v)) ≤ κ(v) and env(v + 1/κ(v)) ≤ e env(v), since log env
increases by at most κ(v) · (1/κ(v)) on [v, v + 1/κ(v)]; so η(v1) ≤ C κ(v)^M env(v), and [[eq:edge-degree-two]] gives
[[eq:edge-localised]]. ∎

**Remark {#rem:edge-localisation-numbers}** (Numerical observation.) The descent of [[lem:edge-localisation]] was run
with unit constants (C = 10³, cost 30) from the depth 10⁻⁴: the depths y_k fell as log10 y_k = −4, −439,
−5.96·10^437 for exp(−1/x), and −4, −325.3, −8.57·10^323 for the envelope of the numerical point, faster than any
geometric sequence, while for env = x^40, which is not flat, the descent stalled at once. At x = λ/10, λ = 10⁻⁶, for
exp(−1/x), the square of the remainder bound with the tilt of order λ exceeded the first-degree term by a factor
10^3553353, and the localised bound was below it by a factor 10^(−4342893). No proof uses these figures.


### The very edge for the solutions from past null infinity {#sec:edge-past}

In this section g_λ is the metric of [[thm:past-construction]] (case P of [[sec:edge-degree-two]]). Let 𝒫 and Q be as
in [[eq:edge-p-q]]. For a profile f(r, ϑ) let 𝒫_∞⁻¹ f be the solution Z of 𝒫 Z = f along every generator of ℓ with
r^(3/2) |Z|_cart → 0; by [[lem:layer-profiles-past]] (a) it is unique, and it exists for f in E_q, q > 5/2, by the
integral formula in the proof of [[lem:decay-calculus]] (d). Put B := 𝒫_∞⁻¹ Q and b_n := B^n b_0, b_0 = r^(1/2) T,
as long as this is defined. B acts in (r, ϑ) at fixed v and commutes with ∂_v.

**Lemma {#lem:edge-resummation}** (Exact re-summation.) (a) b_n is defined for every n ≥ 0; b_n lies in E_2 for n ≥
1, and Q b_n in E_3 for every n. The profiles of [[lem:layer-profiles-past]] are H_2^∞ = −i B H_1 and H_(j+1)^∞ =
i(∂_v − B) H_j^∞ for j ≥ 2, so that, as formal series in λ,

    Σ_(j≥1) λ^j H_j^∞ = λ (s − B)⁻¹ s H_1 = λ Σ_(n≥0) s^(−n) B^n H_1.                              {#eq:edge-resummation}

(b) For M ≥ 1 put h_M := Re[λ e^(iv/λ) A Σ_(n≤M) I_n(v) b_n(r, ϑ)] and e_M := h^(1) − h_M. Then

    dRic^H(e_M) = −Re[λ e^(iv/λ) A I_M(v) (Q b_M)(r, ϑ)],      e_M = 0 on {v ≤ v_s},

e_M has nothing coming in, and at every X ∈ Ω with v(X) ≤ v_♯, |e_M(X)| ≤ C_M λ sup_(v′≤v(X)) |I_M(v′)|.

(c) b_0 and b_1 have no vv, vr or rr component, and b_2,vv(√μ0, ϑ) = −ν_∞ d(ϑ), with ν_∞ of
[[eq:layer-nu-infinity]].

*Proof.* (a) By [[eq:edge-p-q]] with the derivative in v taken on H, [[lem:layer-profiles-past]]'s transport 𝒯
H_(j+1)^∞ = −R_X H_j^∞ reads 𝒫 H_(j+1)^∞ = i𝒫 ∂_v H_j^∞ − i Q H_j^∞. The H_j^∞ are linear in env, Σ_k env^(k)(v)
c_(j,k)(r, ϑ), with coefficients independent of v and of τ0 ([[lem:layer-profiles-past]]), and the transport acts at
fixed v; in it, i𝒫 ∂_v H_j^∞ contributes only to the coefficients of env^(k), k ≥ 1. So if the coefficient of env in
H_n^∞ is (−i)^(n−1) A b_(n−1), that of H_(n+1)^∞ is the decaying solution of 𝒫Z = −i Q((−i)^(n−1) A b_(n−1)), which
exists: b_n = B b_(n−1) is defined and equals i^n/A times it. It lies in E_2 for n ≥ 1, as H_(n+1)^∞ does
([[lem:layer-flat-past]] (a), (c)), and Q b_n in E_3, as the forcing terms of these transports do (the proof of
[[lem:layer-flat-past]] (a)); the induction starts from H_1 = A env b_0, where Q b_0 is the coefficient of A env in
R_X H_1 ([[prop:layer-linear]] (a)). For j ≥ 2, ∂_v H_j^∞ decays like H_j^∞, so
𝒫_∞⁻¹ 𝒫 ∂_v H_j^∞ = ∂_v H_j^∞ and H_(j+1)^∞ = i(∂_v − B) H_j^∞. For j = 1, 𝒫 ∂_v H_1 = 0, since H_1 is the
homogeneous transport, and H_2^∞ = −i B H_1. For the series, put G := Σ_(j≥1) λ^j H_j^∞. The recursion gives G =
λH_1 − iλ²BH_1 + iλ(∂_v − B)(G − λH_1) = λH_1 + iλ(∂_v − B)G − iλ²∂_v H_1, that is (1 − iλ∂_v + iλB) G = λ(1 −
iλ∂_v) H_1. As 1 − iλ∂_v = −iλ s, this is −iλ(s − B) G = −iλ² s H_1, which is [[eq:edge-resummation]]; the last
form follows since B commutes with s.

(b) d/dv (e^(iv/λ) X) = e^(iv/λ) s X, and 𝒫, Q contain no derivative in v, so dRic^H(e^(iv/λ) X) = e^(iv/λ)(−𝒫(sX) +
QX). For X = λA Σ_(n≤M) I_n b_n, 𝒫(s I_n b_n) = (s I_n) 𝒫 b_n, with 𝒫 b_0 = 0, s I_n = I_(n−1) and 𝒫 b_n = Q b_(n−1)
for n ≥ 1 (the definition of B), so

    −𝒫(sX) + QX = λA [−Σ_(n=1)^M I_(n−1) Q b_(n−1) + Σ_(n=0)^M I_n Q b_n] = λA I_M Q b_M.

So dRic^H(h_M) = Re[λ e^(iv/λ) A I_M Q b_M], and dRic^H(h^(1)) = 0 gives the equation for e_M. h_M carries the wave as
its term n = 0, its other terms decay, and h^(1) has nothing coming in but the wave, so e_M has nothing coming in; I_n
and h^(1) vanish on {v ≤ v_s}.

For the bound: (1) *The operator.* In Cartesian components dRic^H(h) = −(1/2) g0°^(ab) ∂_a ∂_b h + 𝔅(∂h) + ℭh, with
𝔅, ℭ smooth on P ∪ Ω and, on P, O(r⁻³) and O(r⁻⁴) with their derivatives (the Christoffel symbols and the curvature of
g0° = η + (μ0/r²) L0 ⊗ L0); and dRic^H commutes with the Lie derivatives along the rotations Ω_ab, which are Killing
for g0°, the operator being natural under the isometries of g0° and the gauge being relative to g0°.

(2) *Energy on S(v) with the null face kept.* For u := Ω^β e_M, |β| ≤ 2, run [[lem:past-energy]] on P and
[[lem:energy]] on Ω, as in [[lem:layer-energy-null]], on S(v) ∩ {τ ≤ τ′}, with 𝔅∂u + ℭu moved to the right. The face
N_v has the flux density T(L0, Y) = (1/2)(1 + μ0/r²)(ℓu)² + |∇̊u|²/(2r²) ≥ 0 ([[lem:layer-energy-null]] at μ = μ0),
kept on the left; {r = a} is spacelike with the region to its past ([[lem:domain]] (b)); nothing comes in, that is, e_M
is the limit of the solutions with zero data on Σ̂_(τ_n), τ_n → −∞, as in [[prop:far-region]], and the estimate below
is uniform in n. The first-order terms on the right are absorbed by Gronwall's inequality with the kernel C t^(−3/2) on
P, which is integrable, and C on Ω. So

    sup_τ ‖∂u(τ)‖ + F_v(u)^(1/2) ≤ C ∫_(−∞)^(τ_end) ‖Ω^β dRic^H(e_M)(τ)‖_(L²(Σ_τ ∩ S(v))) dτ.

(3) *The source.* On Σ_τ ∩ S(v) the L² norm of −Re[λ e^(iv/λ) A I_M Ω^β Q b_M] is at most λ A sup_(v′≤v) |I_M(v′)|
‖Ω^β Q b_M‖_(L²(Σ_τ ∩ S(v))). As Q b_M lies in E_3, that norm is at most C t^(−3/2) on the slices of P
([[sec:past-approximant]]) and bounded on Ω, where τ ∈ [τ0, τ_end].

(4) *Pointwise.* Along the generator of N_v from r = ∞, where r^(3/2) |Ω^β e_M| → 0, to r(X),
‖Ω^β e_M(r, ·)‖_(L²(S³)) ≤ ∫_r^∞ ‖ℓ Ω^β e_M(r′, ·)‖ dr′ ≤ (2 F_v(Ω^β e_M))^(1/2) (∫_r^∞ r′⁻³ dr′)^(1/2), by the
Cauchy–Schwarz inequality and T(L0, Y) ≥ (1/2)(ℓu)²; and H²(S³) ⊂ L^∞ ([[thm:std-bh-embedding]], as in
[[lem:layer-null-pointwise]]) gives |e_M(X)| ≤ C Σ_(|β|≤2) F_v(Ω^β e_M)^(1/2) ≤ C_M λ sup_(v′≤v(X)) |I_M(v′)|.

(c) b_0 = r^(1/2) T is angular. By (a), b_1 = i H_2^∞/(A env), which lies in 𝔖 ([[lem:layer-profiles-past]] (b)).
By (a) again, H_3^∞ = i(∂_v − B)(−iA env b_1) = A env′ b_1 − A env b_2; as b_1 has no vv component,
H_3,vv^∞(v, √μ0, ϑ) = −A env b_2,vv(√μ0, ϑ), and [[eq:layer-nu-infinity]] gives b_2,vv(√μ0, ϑ) = −ν_∞ d(ϑ). ∎

**Theorem {#thm:edge-past}** (The very edge for the solutions from past null infinity.) Let μ0 = √72 l5², K ≥ 6, and
let g_λ be the metric of [[thm:past-construction]], with A, τ0 as in [[thm:layer]]. Let env be positive and log-concave
on (v_s, v_s + x0], with |κ′| ≤ c_R κ^(1+α) for some α ∈ (0, 1), (H_D), and (B_J) with J := max(c, M_P), c the cost
of [[lem:edge-degree-two]]. There are λ_E > 0, x0′ ∈ (0, x0] and P0, depending on K, these constants and the costs,
such that for λ ≤ λ_E, every v ∈ (v_s, v_s + x0′] with env(v + 4πλ) ≤ λ^(P0) and every x̂ ∈ S³, the boundary
{x_K = 1} has, on [v, v + 4πλ] and at x̂, points where it is timelike for g_λ and points where it is spacelike. This
holds in particular for every v ∈ (v_s, v_s + x0′] with λκ(v + 4πλ) ≥ 1, down to v_s.

*Proof.* Take x0′ ≤ x_j of [[lem:edge-kappa]] (c) for j ≤ J, so that the hypotheses of [[lem:edge-kernel]] (c) and of
[[lem:edge-localisation]] hold on (v_s, v_s + x0′]. Fix x̂ and a point X = (v′, r_q(v′), x̂) with v′ ∈ J_v := [v, v +
4πλ]. By [[lem:layer-inverse]], g_λ⁻¹(dΦ0, dΦ0) = −m0 − k(Φ0♯, Φ0♯) + q with k = g_λ − g0 = h^(1) + r2 − (g0 −
g0°). By [[lem:edge-resummation]] with M = 3,

    −h^(1)(Φ0♯, Φ0♯) = λ A ν_∞ Re[d(ϑ) e^(iv′/λ) I_2(v′)] + ρ′,
    |ρ′| ≤ C λ (|I_3(v′)| + sup_(v″≤v′) |I_3(v″)| + ε_0(v′)² |I_2(v′)|),

since the terms n = 0, 1 have no vv, vr or rr component, b_2,vv(r_q, ϑ) = −ν_∞ d + O(r_q − √μ0) with r_q − √μ0 ≤ C ε_0²,
and β_Φ = O(ε_0²) ([[cor:layer-expansion]]). env is increasing and κ nonincreasing, so by [[lem:edge-kernel]] (a),
(c), |ρ′| ≤ C λ env(v′) min(λ, 1/κ(v′))³ + C λ ε_0² |I_2|. By [[lem:edge-kernel]] (b) and ν_∞ < 0, the main term is λ
A |ν_∞| |d| env |s̃|^(−2) Re[e^(iΘ)(1 + ρ″)], where Θ := v′/λ + arg(ν_∞ d) − 2 arg s̃ and ρ″ := ρ_2 + ρ′ e^(−iΘ)/(λ
A |ν_∞| |d| env |s̃|^(−2)). Since |s̃|^(−2) ≥ min(λ, 1/κ)²/2 and |d| ≥ 8/3, |ρ″| ≤ R_2 + C min(λ, 1/κ) + C ε_0², and by
[[eq:edge-r2-bound]], κ → ∞ ([[lem:edge-kappa]] (a)), and T_2 → 0 (by [[lem:edge-kappa]] (c) with j = 2, |κ′| ≤ c_R κ²,
and κ U_* → ∞), |ρ″| ≤ 1/4 for x0′ small and λ ≤ λ_E.

The phase Θ increases: arg s̃ = arctan(1/(λκ)), so |d arg s̃/dv′| = λ|κ′|/(1 + λ²κ²) ≤ |κ′|/(λκ²), and dΘ/dv′ ≥
λ⁻¹(1 − 2|κ′|/κ²) ≥ 1/(2λ), since |κ′|/κ² ≤ c_R κ^(α−1) ≤ 1/4 for x0′ small. So Θ increases by at least 2π on J_v
and meets 0 and π modulo 2π. As |ρ″| ≤ 1/4, |arg(1 + ρ″)| ≤ arcsin(1/4) < 0.253, and at those points Re[e^(iΘ)(1 + ρ″)]
is at least (3/4) cos 0.253 > 0.72, resp. at most −0.72: the main term is at least 0.72 λ A |ν_∞| |d| env |s̃|^(−2),
resp. at most minus that.

The remaining terms are of degree two: m0, r2(Φ0♯, Φ0♯), (g0 − g0°)(Φ0♯, Φ0♯) and q. By [[lem:edge-localisation]], whose
hypothesis ε_(M_P)(v′ + 1/κ(v′)) ≤ λ⁵ holds since env(v′ + 1/κ(v′)) ≤ e env(v′) ≤ e λ^(P0) and (B_J) holds, |r2| ≤ C
κ^(2c′) env²; by [[eq:edge-degree-two]], |g0 − g0°| ≤ C ε_0² ≤ C κ^(2c′) env²; m0 ≤ C (env² + ∫_(v_s)^(v′) env²) ≤ C env²
by [[cor:layer-expansion]] and [[lem:edge-kappa]] (d); and |q| is smaller. Their ratio to λ env min(λ, 1/κ)² is at most C
λ^(−2c′−3) env on {λκ ≤ 1}, which is at most C λ³ once env ≤ λ^(P0), P0 := 2c′ + 6, and at most C κ^(2c′+3) env on {λκ >
1}, which tends to 0 as v′ ↓ v_s by [[lem:edge-kappa]] (e). So for x0′ and λ small the degree-two terms are below a tenth
of the main term's bound, and g_λ⁻¹(dΦ0, dΦ0) takes both signs on J_v.

For the last statement: if λκ(v + 4πλ) ≥ 1, then by [[lem:edge-kappa]] (e) with p := P0 + 1, env(v + 4πλ) ≤ κ(v +
4πλ)^(−P0−1) ≤ λ^(P0+1) ≤ λ^(P0) once x0′ is small. ∎

**Lemma {#lem:edge-past-levels}** (The levels for the solutions from past null infinity.) The conclusion (ii) of
[[prop:layer-regions]] holds for the metric g_λ of [[thm:past-construction]], with M_P in place of M*: for δ ∈ (0, 1/2]
and P > 4 there is λ_UP > 0 such that for λ ≤ λ_UP, at every first-reach point v of the layer with λ^P ≤ env(v) ≤
λ^(3+δ) and every x̂, the boundary has, on [v, v + 4πλ] and at x̂, points where it is timelike and points where it is
spacelike.

*Proof.* The proof of [[prop:layer-regions]] (ii) is that of [[thm:layer]] at the level y := env(v) = λ^p, p ∈ [3 + δ,
P], with v in place of v*; for these solutions [[thm:layer-past]] runs the proof of [[thm:layer]] with ν_∞ in place of
ν, so that only the generic case occurs, and with the remainder of [[lem:layer-remainder-past]]. Take m := max(56M_P,
4PM_P, ⌈4M_P/δ⌉) and κ as in [[prop:layer-regions]]. The hypothesis ε_(M_P)(v1) ≤ λ³ of [[lem:layer-remainder-past]]
holds, since ε_(M_P)(v1) ≤ C y^(1−M_P/m) and p(1 − M_P/m) ≥ (3 + δ)(1 − δ/4) = 3 + δ/4 − δ²/4 > 3. The exponent
conditions after [[thm:layer]], with N − 5 replaced by N_P − 3 ≥ K + 9 and M by M_P, hold uniformly in p as in the proof
of [[prop:layer-regions]] (ii). ∎

So, for an envelope increasing on (v_s, v_s + x0] with the hypotheses of [[thm:edge-past]], [[lem:edge-past-levels]]
at P := P0 + 1 and [[thm:edge-past]] together give both signs on every interval [v, v + 4πλ] near v_s with env(v) ≤
λ^(3+δ), for λ small: if env(v) ≥ λ^(P0+1), every point being a first-reach point, the lemma applies; if env(v) <
λ^(P0+1) and λκ(v) ≤ 1, then env(v + 4πλ) ≤ e^(4π) env(v) ≤ λ^(P0) for λ ≤ e^(−4π); and if λκ(v) > 1, then κ ≥
2^(−1/α) κ(v) on [v, v + 4πλ] by [[lem:edge-kappa]] (b), as 4πλ ≤ 4π κ(v)^(−1) ≤ κ(v)^(−α)/(α c_R) near v_s, so
env(v + 4πλ) ≤ (2^(−1/α)/λ)^(−P0−1) ≤ λ^(P0) by [[lem:edge-kappa]] (e), for λ small.

**Remark {#rem:edge-past-numbers}** (Numerical observation.) The bounds of [[lem:edge-kernel]] were sampled on
exp(−1/x), exp(−1/x²) and the envelope of the numerical point at λ = 10⁻³ and 10⁻⁶, with λκ from 10⁻² to 10⁴: the
ratios |I_n| κ^n/env, |I_n|/(env min(λ, 1/κ)^n) and |ρ_2|/R_2 stayed at most 1.0000, 1.0002 and 0.9999, and R_2
κ^(1−α) at most 9.33. The frozen local form s̃ := i/λ, the leading term of the expansion in λ, was off by more than 1 at
the very edge. A model of the proof of [[thm:edge-past]] with unit constants (|ν_∞ d| = 1/9, μ0 = A = 1, a degree-two
term 10(1 + λκ)² env² of either sign), over three carrier periods at five depths from env = λ⁴ to λκ = 1000, λ = 10⁻⁶,
and three phases of d, found timelike and spacelike points in every period of all thirty cases; without the
first-degree term, or with a degree-two term 10⁶ λ⁻³ times larger, it found none. No proof uses these figures.

### The part of first degree on the horizon, for the metric of the main theorem {#sec:edge-first-degree}

In this section g_λ is the metric of [[thm:main]] (case Ω), N = K + 3, F° := 1 − μ0/r², and L := ∂_v + (F°/2) ∂_r is
the outgoing null direction of the seed.

**Lemma {#lem:edge-characteristic}** (The seed's operator along the null directions.) (a) For every symmetric
2-tensor h(v, r, ϑ) of the class of [[lem:layer-seed-operators]], dRic^H(h) = −𝒫(Lh) + Q̃h, where Q̃ contains no
derivative in v and no second derivative in r: it is of first order in r and of second order in the angles. At the
horizon r = √μ0, L = ∂_v.

(b) In the coordinates (u, r), u := v − 2r* with dr* = dr/F°, dRic^H(h) = −𝒫′ ∂_u h + Q′ h, with 𝒫′ of first order in r
and Q′ containing no derivative in u.

(c) If Z solves 𝒯Z = 0 along ℓ with Z = X at r = r0 > √μ0, then

    Z_vv(√μ0) = μ0^(−3/4) r0^(3/2) [X_vv + F°(r0) X_vr + F°(r0)² X_rr/4].                           {#eq:edge-transport}

(d) On Σ_τ0 the null covectors of g0° whose part tangent to Σ_τ0 is s dr are s dv = s(dτ + dr) and s(dr − (F°/(2 −
F°)) dτ).

*Proof.* (a) By [[eq:edge-p-q]], dRic^H(h) = −𝒫 ∂_v h + Q h with Q free of ∂_v. In □h = g0°^(ab) ∇_a ∇_b h a second
derivative in r occurs only through g0°^(rr) ∂_r² = F° ∂_r², so the part of Q of second order in r is −(F°/2) ∂_r². As
𝒫 = ∇_ℓ + 3/(2r) is ∂_r plus a term of order zero, 𝒫(Lh) = 𝒫 ∂_v h + 𝒫((F°/2) ∂_r h), and the second has the part
(F°/2) ∂_r² h of second order in r. So Q̃ := Q + 𝒫 ∘ ((F°/2) ∂_r) has no ∂_r² and no ∂_v. At r = √μ0, F° = 0.

(b) In (u, r), g0° = −F° du² − 2 du dr + r² γ, its Christoffel symbols do not depend on u and g0°^(uu) = 0; the proof
of [[prop:layer-structure]] (a), with u in place of v and g0°⁻¹ du = −∂_r in place of ℓ, gives the form stated.

(c) By [[eq:layer-components]], 𝒯Z = 0 gives (∂_r + 3/(2r)) Z_rr = 0, (∂_r + 3/(2r)) Z_vr = −μ0 Z_rr/r³ and (∂_r +
3/(2r)) Z_vv = −2μ0 Z_vr/r³. So r^(3/2) Z_rr = c := r0^(3/2) X_rr, r^(3/2) Z_vr = r0^(3/2) X_vr + (μ0 c/2)(r⁻² − r0⁻²),
and ∂_r(r^(3/2) Z_vv) = −2μ0 r⁻³ r^(3/2) Z_vr. Integrating from r0 to √μ0, with μ0(μ0⁻¹ − r0⁻²) = F°(r0) =: F and
μ0/r0² = 1 − F,

    μ0^(3/4) Z_vv(√μ0) = r0^(3/2) X_vv + F (r0^(3/2) X_vr − μ0 c/(2r0²)) + (μ0² c/4)(μ0⁻² − r0⁻⁴),

and −F(1 − F)/2 + (1 − (1 − F)²)/4 = F²/4 gives [[eq:edge-transport]].

(d) In (τ, r) the inverse of the seed has g^(ττ) = −(1 + m), g^(τr) = m, g^(rr) = 1 − m, m := μ0/r² ([[lem:eq-seed]]).
For ξ = c dτ + dr, g0°⁻¹(ξ, ξ) = −(1 + m) c² + 2mc + (1 − m) vanishes exactly for c = 1 and c = −(1 − m)/(1 + m) =
−F°/(2 − F°). ∎

**Lemma {#lem:edge-ingoing}** (The ingoing projection.) Let x0 > 0, and let Ψ solve dRic^H(Ψ) = f on Ω with data (Ψ_Σ,
∂_τΨ_Σ) on Σ_τ0, all of them zero on {v ≤ v_s}, invariant under T² and both reflections, and of the form e^(iv/λ) times
amplitudes Â: Ψ_Σ = e^(iv/λ) Â_Ψ and ∂_τ Ψ_Σ = e^(iv/λ) Â_∂Ψ as functions of v = τ0 + r on Σ_τ0, and f = e^(iv/λ) Â_f(v,
r, ϑ). Let 𝒟 be positive and log-concave on (v_s, v_s + x0], with κ_𝒟 := (log 𝒟)′, |κ_𝒟′| ≤ c_R κ_𝒟^(1+α) for some α < 1,
and with the hypotheses of [[lem:edge-kernel]] (c) for n = 2 with 𝒟 in place of env; put s̃_𝒟 := κ_𝒟 + i/λ. Assume
that |Â_Ψ| + |Â_∂Ψ|/|s̃_𝒟(v)| + |Â_f|/|s̃_𝒟(v)|, and the same with Ω^β, |β| ≤ 6, applied to the amplitudes, is at most
𝒟(v) at the points of Σ_τ0 ∩ {v′ ≤ v} for the data and of Ω ∩ {v′ ≤ v} for f, and that |∂_v Â| ≤ C κ_𝒟 𝒟 for every
amplitude. Let G(r ← r′) be the propagator of 𝒯Z = 0 along ℓ. Then at P = (v, √μ0, x̂), v_s < v ≤ v_s + x0,

    Ψ(P) = e^(iv/λ) s⁻¹[ G(√μ0 ← r0) y + ∫_(√μ0)^(r0) G(√μ0 ← r′) Â_f(·, r′, ·) dr′ ](v) + O(𝒟(v)/|s̃_𝒟(v)|),
    y := (1/2)(2 − F°(r0)) Â_∂Ψ + (1/2) F°(r0) s Â_Ψ,      r0 = v′ − τ0 inside s⁻¹.                  {#eq:edge-ingoing}

*Proof.* (1) *Characteristic form.* By [[lem:edge-characteristic]] (a), Y := LΨ obeys 𝒫Y = Q̃Ψ − f along each
generator of ℓ, and at the horizon Y = ∂_vΨ.

(2) Along ℓ from Σ_τ0, where r = r0, to √μ0, Y(v, √μ0) = G(√μ0 ← r0) Y(v, r0) − ∫_(√μ0)^(r0) G(√μ0 ← r′) (Q̃Ψ −
f)(v, r′) dr′.

(3) The horizon is a generator of L, and Ψ = 0 there for v ≤ v_s, so Ψ(v, √μ0) = ∫_(v_s)^v Y(v′, √μ0) dv′.

(4) *An a priori bound:* |Ω^β Ψ| ≤ C 𝒟(v′) and |Ω^β (∂_v − i/λ) Ψ| ≤ C κ_𝒟 𝒟(v′) on Ω ∩ {v ≤ v′}, |β| ≤ 2. Take the
leading two-sided parametrix: h_in := e^(iv/λ) G(r ← r0(v)) X_in(v), and h_out := e^(iψ(u)/λ) H(r ← r_Σ(u))
X_out(r_Σ(u)), where ψ(u(τ0, r)) = τ0 + r, H is the propagator of the outgoing transport 𝒫′ of
[[lem:edge-characteristic]] (b), r_Σ(u) is where the outgoing ray meets Σ_τ0, and (X_in, X_out) is the solution, from
zero at r_b := v_s − τ0, of the matching system on Σ_τ0 (equal values and τ-derivatives). By
[[lem:edge-characteristic]] (d) the τ-components of the two phases' differentials on Σ_τ0 are 1 and −F°/(2 − F°), so
the system reads s X_in + ((2 − F°)/2) Ã X_in = ((2 − F°)/2) Â_∂Ψ + (F°/2)(s + A_out) Â_Ψ, X_in + X_out = Â_Ψ, with
bounded Ã and A_out; and |X_in| + |X_out| ≤ C 𝒟 by [[lem:edge-kernel]] applied to 𝒟. 𝒫 annihilates G(r ← r0(v))
X_in(v), so the residual of h_in is e^(iv/λ) Q G X_in, free of 1/λ; that of h_out is e^(iψ/λ) Q′(H X_out), by
[[lem:edge-characteristic]] (b). The source is taken up by the ingoing particular solution h_f := e^(iv/λ) Z_f with zero
data: Y_f := −∫_(r0(v))^r G(r ← r′) Â_f(v, r′) dr′ along ℓ and Z_f(v, r) := ∫_(τ0+r)^v e^(−i(v−v′)/λ) Y_f(v′, r) dv′,
so that s Z_f = Y_f, 𝒫(s Z_f) = −Â_f, Z_f = s Z_f = 0 on Σ_τ0 and |Z_f| ≤ C 𝒟; its residual is e^(iv/λ) Q Z_f. The
difference e := Ψ − h_in − h_out − h_f has zero data and the source minus the three residuals, at most C 𝒟 in the strip
of v-width x that carries the amplitudes; so [[lem:layer-energy-null]] and [[lem:layer-null-pointwise]] give |Ω^β e| ≤
C x^(1/2) 𝒟. h_out vanishes for u > u(r_b), a neighbourhood of the horizon's part of the strip. The same holds for (∂_v
− i/λ)Ψ, the solution with data and source (∂_v − i/λ) of those of Ψ (∂_v is Killing for g0° and commutes with dRic^H),
whose amplitudes are ∂_v Â.

(5) *The error terms of (2)–(3).* The ∂_rΨ terms of Q̃Ψ are integrated by parts along the ray, leaving boundary terms
and integrals of Ψ, so |∫ G Q̃Ψ dr′| ≤ C 𝒟(v′) by (4), with angular derivatives up to two. For their integral in v′:
if λκ_𝒟 ≤ 1, one integration by parts against e^(iv′/λ), with the bound on (∂_v − i/λ)Ψ, gives at most C λ 𝒟(v); if
λκ_𝒟 ≥ 1, ∫_(v_s)^v 𝒟 ≤ 𝒟(v)/κ_𝒟 by [[lem:edge-kappa]] (d). Either way it is O(𝒟/|s̃_𝒟|).

(6) *The main terms.* On Σ_τ0, ∂_v|_r = ∂_τ and ∂_r|_v = ∂_r|_τ − ∂_τ, and Ψ_Σ = e^(i(τ0+r)/λ) Â_Ψ(τ0 + r), so LΨ =
(1 − F°/2) ∂_τΨ + (F°/2) ∂_r|_τ Ψ = e^(iv/λ) y exactly. So ∫_(v_s)^v G(√μ0 ← r0(v′)) Y(v′, r0(v′)) dv′ = e^(iv/λ)
s⁻¹(Gy) by [[eq:edge-sinv]], and the term of f in (2) gives the second term of [[eq:edge-ingoing]] in the same way. ∎

**Lemma {#lem:edge-constraint}** (The constraint correction at first degree.) Write D_X H_(N+1) = Σ_k env^(k) D_k,
with D_k functions of (r, r0, ϑ) (r0 = v − τ0), and put c_N := N μ0/(r0² + μ0), α(r) := 3r³/(r² + μ0)² and

    Ξ := ((1 − c_N) T − i c_N)/(T + i),      T = λκ_(N−1).                                         {#eq:edge-xi}

(i) dD(h_app^(1)) = λ^(N+1) Re[D_X H_(N+1) e^(iv/λ)] and dRic^H(h_app^(1)) = λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)] on Ω.

(ii) On Σ_τ0, D_N = i^N A d_1 r^(−3/2) dϑ, and the components (v, r) of D_(N−1) are N i^N A d (−r^(−7/2)/2,
r^(−7/2)).

Assume (H_N) on (v_s, v_s + x0]. Then there is x0′ ∈ (0, x0] such that for v_s < v ≤ v_s + x0′:

(iii) the ρ-component of Φ^(1) at the point of Σ_τ0 with r = r0 = v − τ0 is

    F_ρ = λ^(N+1) Re{ e^(iv/λ) i^N A d(ϑ) r0^(−7/2) [env^(N) − c_N s env^(N−1)] } (1 + O(1/κ + λ));

(iv) a^(1)(r0) = −λ^(N+1) Re{ e^(iv/λ) i^N A d(ϑ) α(r0)⁻¹ r0^(−7/2) env^(N−1) Ξ } (1 + O(ϵ′ + 1/κ + λ)), with ϵ′ of
[[lem:edge-sinv]] (a); and |Ξ|² = ((1 − c_N)² T² + c_N²)/(T² + 1) ≥ min(c_N², (1 − c_N)²), Ξ = −c_N − iT + O(T²);

(v) the vv component on the horizon of the part of [[eq:edge-ingoing]] that the data of a^(1) induce is K_R a^(1) +
O(λ |a^(1)|), K_R := μ0^(−3/4) r0^(3/2)/4 > 0; (ϖ^(1), q^(1)) and the data of h_app^(1) enter the vv component on the
horizon at relative order O(1/κ + 1/|s̃|).

The relative errors in (iii) and (iv) are relative to the bracket of (iii) and to Ξ env^(N−1), also where c_N = 1.

*Proof.* (i) Let Z_j := 𝒯H_j + R_X H_(j−1) and G_j := i Pol(H_(j+1)) + D_X H_j as in [[lem:layer-bianchi]], with
H_(N+2) := 0. By [[def:layer-profiles]], Z_j = 0 for j ≤ N + 1 and, as Pol Pol⁺ = 1, G_j = 0 at Σ_τ0 for j ≤ N; so
[[lem:layer-bianchi]] (b) with J = N + 1 gives G_j = 0 on Ω for j ≤ N. By [[lem:layer-seed-operators]] (b),
dD(Σ_(j≤N+1) λ^j H_j e^(iv/λ)) = e^(iv/λ) (Σ_(m≤N) λ^m G_m + λ^(N+1) D_X H_(N+1)) and dRic^H(Σ_j λ^j H_j e^(iv/λ)) =
e^(iv/λ) (Σ_(j≤N+1) λ^(j−1) Z_j + λ^(N+1) R_X H_(N+1)); take real parts.

(ii) By [[prop:layer-structure]] (a), D_X H = Pol(∂_v H) + qH with q free of ∂_v. Write H_j = Σ_k env^(k) c_(j,k) as
in [[prop:layer-structure]] (b), so that the family k of D_X H_j is Pol(c_(j,k−1)) + Pol(∂_(r0) c_(j,k)) + q c_(j,k).
The top family of D_X H_(N+1) is Pol(c_(N+1,N−1)) = i^(N−1) Pol(c_(2,0)), and Pol(H_2) = H_2,rϑ dϑ = i A env d_1
r^(−3/2) dϑ by [[prop:layer-linear]] (b), so D_N = i^N A d_1 r^(−3/2) dϑ. On Σ_τ0 the data of [[def:layer-profiles]]
give Pol(H_(j+1)) = i D_X H_j, family by family: Pol(c_(j+1,k)) = i [D_X H_j]_k. Let x_j be the (v, r) part of [D_X
H_j]_(j−2) on Σ_τ0. By [[prop:layer-structure]] (b), c_(j,j−2) = i^(j−2) c_(2,0), and the (v, r) part of Pol(Y)
vanishes for Y in 𝔖 ([[eq:layer-components]]), so Pol(∂_(r0) c_(2,0)) contributes nothing, and

    x_j = i x_(j−1) + i^(j−2) (q c_(2,0))_(v,r),      x_2 = (q c_(2,0))_(v,r);

by induction x_j = (j − 1) i^(j−2) (q c_(2,0))_(v,r). By [[prop:layer-linear]] (c), (q H_2)_(v,r) = (D_X H_2)_(v,r) =
i A env d (r^(−5/2) β_2(r), r^(−7/2)), and β_2(r0) = −1/(2r0); so x_(N+1) = N i^N A d (−r0^(−7/2)/2, r0^(−7/2)).

(iii) By [[eq:data-constraint-map]] and [[sec:data-identities]], ρ = 2G(n, n) with G = Gt(E) + Gt(S(D)), n the future
unit normal of Σ_τ0, and Gt(Y)(n, n) = Y(n, n) + (1/2) tr Y. Its part of first degree is that of g_app, by (i), with
E = λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)] and D = λ^(N+1) Re[D_X H_(N+1) e^(iv/λ)]. At the seed S(D) is the symmetrised
derivative of D, and for D = e^(iv/λ) V, V = Σ_k env^(k) D_k, ∇(e^(iv/λ) V) = e^(iv/λ)(dv ⊗ sV + ∇′V), ∇′ the
covariant derivative with ∂_v not acting on the env^(k). For a covector W, 2Gt(sym(dv ⊗ W))(n, n) = 2 dv(n) W(n) +
g0°⁻¹(dv, W), and 2Gt(sym ∇′W)(n, n) = 2(∇′_n W)(n) + div′ W. In (v, r), n = (∂_v − m ∂_r)/(1 + m)^(1/2) and dv(n) =
(1 + m)^(−1/2), m = μ0/r².

The top family W = D_N env^(N) is angular, so W(n) = 0 and g0°⁻¹(dv, W) = 0; and (∇′_n W)(n) = 0, as no Christoffel
symbol Γ^ϑ_ab with a, b ∈ {v, r} is nonzero ([[eq:layer-christoffel]]); its divergence is r⁻² div_γ(A d_1 dϑ) i^N
r^(−3/2) env^(N) = i^N A d r^(−7/2) env^(N). The family N − 1 contributes through its (v, r) part (D_v, D_r) =
N i^N A d (−r^(−7/2)/2, r^(−7/2)) the term s env^(N−1) times

    2 dv(n) W(n) + g0°⁻¹(dv, W) = (2D_v + (1 − m) D_r)/(1 + m) = −m D_r/(1 + m) = −c_N i^N A d r^(−7/2),

as D_v = −D_r/2 and Nμ0/(r² + μ0) = N m/(1 + m). The other terms of S(D) are smaller relative to the bracket: the
∇′-part of the family N − 1 and the families below by O(1/κ + λ), one derivative of env fewer or no factor 1/λ (the
bracket has size at least c_N env^(N−1)/λ, and env^(N) ≍ κ env^(N−1) by (H_N)). E contributes at relative order O(λ),
as it carries λ^(N+1) without a factor s: its top family is −i 𝒯 c_(N+1,N−1) env^(N) = i^N (R_X c_(1,0)) env^(N), with
R_X c_(1,0) in 𝔖 without vϑ part ([[prop:layer-linear]] (a)), so Y(n, n) = 0 and tr Y = 0 for it.

(iv) By [[lem:constraints-evolution]] at the seed's data, the ρ-equation of the linear system for U^(1) is α ∂_r a −
Δ_α a + b′·∂_S a + c a + e·(ϖ, q) = −F_ρ, with α = p = 3r³/(r² + μ0)². On Σ_τ0, r ↦ v = τ0 + r, and ∂_r acts on
e^(iv/λ) times an amplitude as s on the amplitude. The solution from zero at r = a with this oscillating forcing term
is a = −(α s)⁻¹ F_ρ plus terms of relative order 1/|s̃| (from Δ_α a, b′·∂_S a, c a and e·(ϖ, q), the last through the
J-equations, where ϖ is of order (F_J,r + 2r⁻² ∂_ϑ q)/(6 s̃)); the remainder after two terms of this expansion has a
forcing term of relative order |s̃|⁻², and [[lem:linear-evolution]] on [a, r] makes it O(x^(1/2)/|s̃|) relative. The
smooth coefficients α⁻¹ r^(−7/2) and c_N commute with s⁻¹ up to O(λ) relative, by one integration by parts with
[[eq:edge-sinv-parts]]. By [[eq:edge-sinv-parts]], s⁻¹(env^(N) − c_N s env^(N−1)) = (1 − c_N) env^(N−1) − (i/λ) s⁻¹
env^(N−1), and by [[lem:edge-sinv]] (a) for g := env^(N−1), s⁻¹ env^(N−1) = env^(N−1) (κ_(N−1) + i/λ)⁻¹ (1 + ρ_g), |ρ_g|
≤ C ϵ′. Its hypotheses hold near v_s by (H_N): g is positive and log-concave with κ_g = κ_(N−1) ∈ [κ/2, 2κ] and the c_R
bound, and |g^(j)| = |env^(N−1+j)| ≤ c_(N−1+j) κ^(N−1+j) env ≤ c 2^(N−1) κ^j g for j ≤ 3, since env = env^(N−1)/Π_(k<N−1)
κ_k ≤ 2^(N−1) κ^(−(N−1)) env^(N−1). As (i/λ)/(κ_(N−1) + i/λ) = i/(T + i), the bracket becomes env^(N−1)[(1 − c_N) −
i/(T + i)] (1 + O(ϵ′)) = env^(N−1) Ξ (1 + O(ϵ′)). The formulas for |Ξ|² and its expansion are direct: (T + i) = i(1 −
iT) gives Ξ = (−c_N − i(1 − c_N)T)(1 + iT + O(T²)).

*At c_N = 1*, Ξ = −i/(T + i) and |Ξ| = (1 + T²)^(−1/2) → 0 for large T, so the errors must be relative to the bracket
and not to env^(N−1). They are: the two terms of the top family cancel exactly to −(i/λ) s⁻¹ env^(N−1), the
coefficients 1 and c_N being exact; the next family contributes s⁻¹(φ_1 env^(N−1) + φ_2 s env^(N−2)) with smooth φ_i,
of size env^(N−1)(λ + 1/κ_(N−2))(1 + O(ϵ′)) against |T + i|⁻¹ env^(N−1) for the bracket, and |T + i|/κ_(N−2) ≤ 2/κ +
4λ, so it is O(λ + 1/κ) relative for every T; the commutator with c_N′ is O(λ) relative; and the corrections of the
solve are relative by construction.

(v) At first degree the data that a := a^(1) induce have, in the coordinates (τ, r), the components h_rr = a, h_τr = a b
and h_ττ = a b², b := dr(β) = m/(1 + m) the seed's shift (g0°_τr = m and γ_rr = 1 + m); the angular components and their
τ-derivatives are unchanged. As dτ = dv − dr, a tensor with components X_ττ, X_τr, X_rr in (τ, r) has the components
X_ττ, X_τr − X_ττ and X_ττ − 2X_τr + X_rr in (v, r), in the order vv, vr, rr. In the notation of [[lem:edge-ingoing]] let
ĥ be the amplitude of these data and k̂ that of their τ-derivative, k̂_rr =: k being any value. The linearised condition
D = 0 at the leading order in s, with ∂_τ h ↦ k̂ and ∂_r|_τ h ↦ s ĥ, reads g^(aτ) k̂_ab + g^(ar) s ĥ_ab − (1/2) δ^τ_b
g^(ac) k̂_ac − (1/2) δ^r_b s g^(ac) ĥ_ac = 0 for b = τ, r, with g^(ab) as in [[lem:edge-characteristic]] (d); its
solution is

    k̂_τr = (a s + 2k m(1 + m))/(2(1 + m)²),      k̂_ττ = 2a m s/(1 + m)³ − k(1 − m)/(1 + m).

With F° = 1 − m, y = (1 − F°/2) k̂ + (F°/2) s ĥ has, in (v, r), the components

    y_vv = (a s m(2 − m) − k(1 − m²))/(2(1 + m)),      y_vr = (a s(1 − 2m) + 2k(1 + m))/(4(1 + m)),      y_rr = 0,

so that y_vv + F° y_vr + F°² y_rr/4 = a s/4, free of k. The terms of y without a factor s (derivatives of the
coefficients, the Christoffel terms of D) are O(|a|). So y = s(Φa) + Φ_0 a with Φ, Φ_0 smooth in r0, and the horizon
combination [[eq:edge-transport]] of Φa is r0^(3/2) a/4 times μ0^(−3/4), that is K_R a. Then s⁻¹(G s(Φa)) = GΦa −
s⁻¹(G′Φa), so s⁻¹(Gy) = GΦa − s⁻¹(G′Φa − GΦ_0 a), and the last term is O(λ|a|): by [[eq:edge-sinv-parts]], |s⁻¹h| ≤
λ|h| + λ ∫_(v_s)^v |h′| ≤ C λ |h| for h a smooth multiple of a, since ∫_(v_s)^v κ_(N−1) env^(N−1) = env^(N−1)(v).
(ϖ^(1), q^(1)) change the second fundamental form; their amplitudes after division by s̃ are of relative order 1/|s̃|
and lie in the vector sector and the γ-trace, which the transport 𝒯Z = 0 does not take to vv. The scalar sector of the
data of h_app^(1) is a family lower: κ^(N−2) env against κ^(N−1) env. ∎

**Proposition {#prop:edge-horizon-value}** (The first-degree horizon value.) Assume (H_N) on (v_s, v_s + x0]. There
are x0′ ∈ (0, x0] and C such that for v_s < v ≤ v_s + x0′, with r0 = v − τ0,

    h^(1)_vv(v, √μ0, ϑ) = Re[S(v, ϑ) e^(iv/λ)],      S = S_st + S_U + E_S,
    S_st := λ³ A ν(r0) d(ϑ) env (1 + 2iλκ) 𝟙_(λκ≤1),      S_U := −λ^(N+1) A Γ_R(r0) i^N d(ϑ) Ξ env^(N−1),
    Γ_R(r0) := K_R r0^(−7/2)/α(r0) = (r0² + μ0)²/(12 μ0^(3/4) r0⁵) > 0,
    |E_S| ≤ C [λ³ env (|ν(r0)| (λκ)² + λ) 𝟙_(λκ≤1) + λ^(N+1) κ^(N−2) env 𝟙_(λκ>1) + (ϵ′ + 1/κ + λ) |S_U|],     {#eq:edge-s}

and |∂_v^k E_S| ≤ C κ^k times the same bound, k ≤ 2.

*Proof.* h^(1) = h_app^(1) + e. *The stage part.* By [[prop:layer-structure]] (c), Σ_(j≤N+1) λ^j H_j,vv(v, √μ0) = λ³ A d
ν Σ_(k≤N−2) (k + 1)(iλ)^k env^(k) + Σ_(j≥4) λ^j Σ_(k≤j−4) c_(j,k),vv env^(k). By (H_N), |env^(k)| = env Π_(i<k) κ_i ≤ 2^k
κ^k env for k ≤ N + 1. For λκ ≤ 1 the first sum is λ³ A d ν env (1 + 2iλκ) + O(|ν| λ³ (λκ)² env), the sum being finite,
and the second is O(λ⁴ env); for λκ > 1 every term λ^j κ^k env with k ≤ j − 3 and j ≤ N + 1 is at most λ^(N+1) κ^(N−2)
env, the vv components having no family above j − 3 (c_(j,j−2) = i^(j−2) c_(2,0) is in 𝔖). *The part e.* By
[[eq:edge-e-equation]], e solves dRic^H(e) = −λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)] with the data induced by U^(1). Apply
[[lem:edge-ingoing]] to the complex form, with 𝒟 := C λ^(N+1) env^(N−1), which is of the size of the amplitudes of the
data and of the source divided by |s̃| (the source's top family is env^(N) times a profile, and env^(N) = κ_(N−1)
env^(N−1)), and whose hypotheses hold near v_s by (H_N), as for g = env^(N−1) in the proof of [[lem:edge-constraint]]
(iv): by [[lem:edge-constraint]] (iv) and (v) the data of a^(1) give K_R a^(1)(1 + O(λ)) = Re[S_U e^(iv/λ)](1 + O(ϵ′ +
1/κ + λ)), the rest of the data at relative order O(1/κ + 1/|s̃|); the source's top family lies in 𝔖, so its scalar
sector is a family below, and its term in [[eq:edge-ingoing]] is at most C λ^(N+1) κ^(N−1) env/|s̃| in the vv component;
and the remainder O(𝒟/|s̃|) is of the same order, at most C(1/κ + λ)|S_U| (|s̃| ≥ κ, and where |Ξ| is small, T/|s̃| ≤ λ).
*The derivatives.* ∂_v commutes with dRic^H, and by (H_N) every amplitude's derivative is at most C κ times the
amplitude; so the derivatives of E_S obey the same bounds with the factor κ^k. ∎

