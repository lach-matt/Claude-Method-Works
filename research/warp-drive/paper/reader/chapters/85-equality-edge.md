## The boundary at equality, II: the very edge and the dips {#ch:equality-edge}

This chapter continues [[ch:equality-layer]] at the left edge v_s of the envelope, where the window argument of
[[thm:layer]] stops. There the margin m0, the first-degree term and the degree-two terms of g_λ⁻¹(dΦ0, dΦ0) on the
boundary all vanish to every order, and the expansion in λ of [[ch:equality-layer]] stops being ordered: on the *very
edge*, where λκ ≥ 1 with κ := (log env)′, every derivative of env costs more than the phase does. We decide the causal
character of the boundary there in three steps. First, for the solutions of [[thm:past-construction]], the part of g_λ of
first degree in the waves is written exactly, as a convolution of env with an explicit kernel against the phase, and a
kernel lemma evaluates it for every λ ([[thm:edge-past]]). Second, for the metric g_λ of [[thm:main]], the first-degree
part on the very edge is carried by the constraint correction of [[ch:data]] at first degree; its value on the horizon is
determined to leading order ([[prop:edge-horizon-value]]), and [[thm:very-edge]] shows that on every interval of length
4πλ below a fixed power of λ, down to v_s, the boundary has timelike and spacelike points on every column, for every
admissible τ0. The degree-two terms are bounded at every depth of the edge by a localisation of the remainder estimates
([[lem:edge-localisation]]). Third, in the band λ^(3+δ) ≤ E ≤ λ^(3−δ) of [[prop:layer-regions]] the ratio of the
first-degree amplitude to the margin crosses 1 once per column, and the boundary switches from timelike points to
spacelike once ([[thm:l-24]]). The hypotheses on the envelope are properties of its edge; we prove them, for every order,
for the envelope env_C of [[eq:envelope]] and for the edges exp(−a/x) ([[sec:edge-envelope]]). For some C_c^∞ envelopes
whose intervals of zeros accumulate at the edge, intervals of length 4πλ below λ^(3+δ) on which the boundary is spacelike
throughout occur for every small λ ([[prop:edge-dips]]): some regularity of the edge is needed.

Throughout, μ0 = √72 l5², and the notation is that of [[ch:equality-layer]]: g0, the seed g0°, r_q, Φ0, Φ0♯ = ∂_v + β_Φ
∂_r, the margin m0 of [[eq:eq-margin]], the coefficient ν of [[eq:layer-nu]], the angular factors d_1, d of
[[eq:layer-divergence]], the operators 𝒯, R_X, D_X, Pol and Pol⁺ of [[sec:layer-operators]], the profiles H_j of
[[def:layer-profiles]], the level E(v) and the costs ε_c(v) of [[eq:layer-costs]], M* := 2N + 8, and the ratio R(v,
x̂) := λ³ A |env(v)| |ν(v − τ0)| |d(ϑ)|/m0(v) of [[sec:layer-regions]]. A boundary point is X = (v, r_q(v), x̂), x̂ ∈ S³
with polar angle ϑ. The phase is θ.

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
intervals at the edge, for the envelope env_C and for exp(−a/(v − v_s)).

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
[[lem:edge-kappa]] on (v_s, v_s + x0]. Let g be smooth on ℝ, zero on (−∞, v_s], positive and log-concave on (v_s, v_s +
x0], with κ_g := (log g)′ ∈ [κ/2, 2κ], |κ_g′| ≤ c_R κ_g^(1+α) and |g^(j)| ≤ c_j κ^j g for j ≤ 3 there. Put s̃_g := κ_g +
i/λ, T_g := λκ_g, and define ρ_g by

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

(A) If S ≠ 0 on J, a continuous determination of arg S varies by at most 3π/2 on J and |ε(t)| ≤ |S(t)|/4 for every t ∈ J,
then f takes both signs on J.

(B) If |S′| ≥ L0 > 0 and |S″| ≤ L0/(80πλ) on J, and |ε| ≤ πλL0/5 on J, then f takes both signs on J.

*Proof.* (A) With that determination, t/λ + arg S(t) increases by at least 4π − 3π/2 > 2π over J, so, being continuous,
it meets 0 and π modulo 2π at points t₁, t₂ ∈ J; f(t₁) ≥ |S(t₁)| − |S(t₁)|/4 > 0 and f(t₂) ≤ −|S(t₂)| + |S(t₂)|/4 < 0.

(B) By Taylor's formula, S(t) = S(v) + S′(v)(t − v) + R(t) with |R(t)| ≤ (4πλ)² L0/(2 · 80πλ) = πλL0/10. Put t0 := v −
S(v)/S′(v) = α0 + iβ0 (S′(v) ≠ 0), so S(t) = S′(v)(t − t0) + R(t). At the points t_k ∈ J where e^(i(t/λ + arg S′(v))) =
±1, which are πλ apart with alternating signs, S′(v) e^(it_k/λ) = ±|S′(v)| is real, so Re[S′(v)(t_k − t0) e^(it_k/λ)] =
±|S′(v)| (t_k − α0), the β0-part vanishing; hence |f(t_k) ∓ |S′(v)|(t_k − α0)| ≤ πλL0/10 + πλL0/5 = 3πλL0/10. Where |t_k
− α0| ≥ πλ/2, |S′(v)| |t_k − α0| ≥ πλL0/2 > 3πλL0/10, so f(t_k) has the sign ±sign(t_k − α0). Remove from J the gap (α0 −
πλ/2, α0 + πλ/2), of length πλ. If one of the two remaining sides has length at least 2πλ, it contains two consecutive
t_k, of opposite types and with t_k − α0 of one sign: f takes both signs. Otherwise both sides have length in (πλ, 2πλ),
since their lengths add up to at least 3πλ, and each contains a t_k. If the gap contains no t_k, its end points are
t_k's, and the left side, of length more than πλ, contains two consecutive t_k, of opposite types and both left of α0: f
takes both signs. Otherwise the gap contains exactly one t_k, so the last t_k of the left side and the first of the right
side are two steps apart, of the same type, and on opposite sides of α0: f takes both signs. ∎

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

*Proof.* Write the constraint map of (γ_U, κ_U) as 𝒞(γ, κ) + 𝔏 U + 𝒬(U), as in the proof of [[prop:exact-correction]],
and let 𝔏_0 be the linearisation at the seed's data. Then U − U^(1) solves 𝔏_0(U − U^(1)) = −(𝒞(γ, κ) − Φ^(1)) − 𝒬(U) −
(𝔏 − 𝔏_0) U with zero data at r = a. (i) The profiles of 𝒞(γ, κ) vanish below order N − 2 ([[lem:gauge-hierarchy]]); its
part of degree at least two has every monomial with two factors of degree one or one factor of degree two ((F2) of
[[sec:layer-flat]], [[lem:layer-flat]] (b), (c)), each radial derivative costing λ⁻¹ through the phase on Σ_τ0; so, by
Taylor's formula in λ as in the proof of [[lem:layer-flat]] (e), it is at most C λ^(N−2−j) ε_c² with j radial
derivatives. (ii) 𝒬(U) is at most C λ⁻¹ |U|²_(C¹), and |∂_r^j U| ≤ C λ^(N−2−j) ε ([[lem:layer-flat]] (e)): at most C
λ^(2N−7−j) ε², below λ^(N−2−j) ε² for N ≥ 5. (iii) 𝔏 − 𝔏_0 has coefficients of degree one, with j radial derivatives at
most C λ^(−j) ε; times U this is C λ^(N−2−j) ε². [[lem:linear-evolution]] on [a, r], with its constant on [a, b1], and
the derivative count of [[lem:layer-flat]] (e) give the bound. ∎

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

(2) *Bounds on u* = (g_app − g0°) + w. By [[lem:layer-flat]] (a)–(c) (case Ω), [[lem:layer-flat-past]] (a)–(c) (case P)
and [[cor:layer-expansion]], |∂^k Ω^β (g_app − g0°)| ≤ C λ^(1−k) ε_c(v′) at points with v = v′, k ≤ 2, each derivative of
a profile [g_j] costing λ⁻¹ only through ∂_θ and the rotations costing nothing, since Ω_ab v = 0; on P with the decay of
the classes E_(3/2), E_2. For w, run [[lem:layer-remainder]] (case Ω), [[lem:layer-remainder-past]] (case P) with
∂^α, |α| ≤ 4, in place of |α| ≤ 2. The coefficients ∂^j g_app, j ≤ 6, are bounded on the region, since ε_M(v1) ≤ λ⁵ gives
λ^(1−j) ε_j ≤ 1 there; ∂^j w, j ≤ 3, are bounded by step 1 of the proof of [[thm:uniform-existence]], resp. item 3 of
[[thm:past-construction]]; so every coefficient of the energy inequality for the derivatives of order at most four is
bounded, while the forcing term and the data cost λ⁻¹ per derivative ([[lem:layer-flat]] (d), (e),
[[lem:layer-flat-past]] (d)). Hence E_4(τ) ≤ C λ^(N−7) ε_M(v1), and Sobolev's inequality on the slices (step 7 of
[[lem:layer-remainder]]) gives |∂^k Ω^β w| ≤ C λ^(N−5−k) ε_M(v1) ≤ C λ^(1−k) η(v1) for k + |β| ≤ 2, and E_4 bounds the
higher orders in L² on the slices.

(3) *The forcing term.* By (2), |u| ≤ C(λε_c + λη), |∂u| ≤ C(ε_c + η) and |∂²u| ≤ C λ⁻¹(ε_c + η), so |𝒩(u)| ≤ C(ε_c +
η)², and |f_2| ≤ C(ε_c(v′)² + ε_c(v′) η(v1) + η(v1)²) at points with v = v′ ≤ v. For Ω^β f_2, |β| ≤ 2, Leibniz's rule
writes each term as a product in which at most one factor carries more than two derivatives and rotations; that factor is
bounded in L² on the slices, by E_4, and the others pointwise. On P each product carries the decay of two factors, at
least t^(−3), so ‖Ω^β f_2(τ)‖_(L²(Σ̂_τ ∩ S(v))) ≤ C (…) t^(−3/2), integrable in τ.

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
x0], with κ := (log env)′ > 0, |κ′| ≤ c_R κ^(1+α) for some α ∈ (0, 1), (H_D), and (B_(c′)) with c′ := max(c, M), c the
cost of [[lem:edge-degree-two]], there. There are λ_D, x_D > 0, given in the proof, such that for λ ≤ λ_D the bounds of
[[lem:edge-degree-two]] hold with a reach ρ_v ≤ 1/κ(v) at every boundary point X with x = v − v_s ≤ x_D at which
ε_M(v + 1/κ(v)) ≤ λ⁵, and at those points

    |r2(X)| ≤ C κ(v)^(2c′) env(v)².                                                                  {#eq:edge-localised}

*Proof.* Put N_* := N − 5 in case Ω and N_* := N_P − 3 in case P, so that [[lem:layer-remainder]], resp.
[[lem:layer-remainder-past]], bounds w by C λ^(N_*) ε_M(v1). Let ψ(τ) := τ − τ0 in case Ω and ψ be the function of
[[lem:layer-remainder-past]] in case P, ψ_max := 2 + τ_end − τ0 ≥ ψ, and e_0 := 2C1λ, resp. e_0 := 2C_Pλ. Let
ϖ := t^(3/2) on P and ϖ := 1 on Ω, so that ψ′ = 1/ϖ. For a covector α let |α|_e be the Euclidean norm of its
Cartesian components, and for a symmetric form B let ‖B‖ be its norm as a bilinear form for |·|_e. For V ≤ v_s + 1
and e > 0 put

    Δ(V) := sup_(X ∈ S(V)) ϖ(X) ‖(g_λ⁻¹ − g0⁻¹)(X)‖,      R(V, e) := S(V) ∩ {v + e ψ(τ) ≤ V}.

By [[eq:eq-c1]], resp. the choice of C_P in [[lem:layer-remainder-past]], 2Δ(V) ≤ e_0 for every V.

(1) *A tilted remainder estimate.* Let V ≤ v_♯, ε_M(V) ≤ λ³ and 2Δ(V) ≤ e ≤ e_0. Then the bound E_2(τ) ≤ C_w λ^(N_*)
ε_M(V) of step 6 of the proof of [[lem:layer-remainder]] (case Ω), resp. of the proof of [[lem:layer-remainder-past]]
(case P), holds on R(V, e) in place of the region there, for every τ, with the constant C_w of those proofs and the norms
taken on R(V, e) ∩ Σ̂_τ. In case P also

    E^Ω(τ) := Σ_(i+|β|≤2) (‖∂ ∂^i Ω^β w(τ)‖ + ‖∂^i Ω^β w(τ)‖) ≤ C_w λ^(N_*) ε_M(V),

C_w enlarged once. If ε_M(V) ≤ λ⁵, the form with four derivatives of step (2) of the proof of [[lem:edge-degree-two]]
holds on R(V, e) as well.

Indeed, the face {v + eψ(τ) = V} has the conormal α := dv + eψ′ dτ, with g0⁻¹(α, α) = −2eψ′ − e²ψ′²(1 + μ/r²)
([[prop:vaidya]] (d)) and |α|_e² = (1 + eψ′)² + 1, as α = (1 + eψ′) dτ + x̂·dx. Since eψ′ ≤ e_0 ≤ 1 and the absolute
value of (g_λ⁻¹ − g0⁻¹)(α, α) is at most Δ(V) ψ′ |α|_e² ≤ (e/2) ψ′ |α|_e²,

    g_λ⁻¹(α, α) ≤ ψ′ (−2e − e²ψ′(1 + μ/r²) + e + e²ψ′ + e³ψ′²/2) = e ψ′ (−1 − eψ′ μ/r² + e²ψ′²/2) ≤ −eψ′/2 < 0.

So α is timelike for g_λ, and α(Y) = 1 + eψ′(1 + μ/r²) > 0 for Y := −g0⁻¹ dτ, which is future timelike for g_λ
([[sec:eq-setting]]); hence v + eψ increases along future causal curves of g_λ and R(V, e) lies to the past of its face.
The slices of R(V, e) are {r ≤ ρ(τ)} ∩ S(V), ρ(τ) := V − eψ(τ) − τ, and ρ decreases. R(V, e) lies in {v ≤ V}, and V ≤
v_s + 1 < v_end + 1, so it does not meet the outer face of Ω, where v ≥ v_end + T + 1, nor the outer boundary of P,
where v = V_P − h_P(τ) ≥ V_P − 1/2 > v_end + 1; in case Ω, R(V, e) ∩ Σ_τ0 = Σ_τ0 ∩ {v ≤ V} is the same set as for the
tilt e_0, since ψ(τ0) = 0. The proofs of [[lem:layer-remainder]] and [[lem:layer-remainder-past]] use their tilted face
only through its flux, which is nonnegative and is dropped, their slices only through the decrease of ρ, and their
hypothesis ε_M(v1) ≤ λ³ only at points with v ≤ v1; so they run on R(V, e) with V in place of v1 and with the same
constants, and so does their form with four derivatives. For E^Ω in case P, apply ∂^i Ω^β, i + |β| ≤ 2, to
[[eq:layer-w-equation]] and write its principal part as −(1/2) □̃ − (1/2)(g_λ^(ab) − g0^(ab)) ∂_a ∂_b, □̃ := g0^(ab)
∂_a ∂_b. The rotations commute with □̃ ([[sec:past-inequalities]]), and [Ω_ab, ∂_c] is a coordinate derivative, so the
commutators are sums of products of ∂^j Ω^γ (g_λ⁻¹ − g0⁻¹), j + |γ| ≥ 1, with second derivatives of ∂^(i′) Ω^(β′) w of
a lower total order, as in step (iii) of the proof of [[prop:far-region]]. On P, g_app⁻¹ − g0⁻¹ is λ times a profile of
class E_(3/2) ([[thm:past-approximant]]), and w with its coordinate derivatives and rotations to the total order three
is at most C t^(−2) by [[eq:far-energy]], [[eq:near-bootstrap]] and [[lem:past-sobolev]] (a), as in the proof of
(P-iii) in [[sec:past-proof]]; so these commutators are at most C t^(−3/2) times energies of lower order, and the
Gronwall kernel stays integrable on P. The forcing term ∂^i Ω^β Ric^H(g_app) obeys the bound of [[lem:layer-flat-past]]
(d), since that proof bounds each monomial through the classes E_p(ε^d), which are defined with the rotations; the
nonlinear terms are bounded as in step (3) of the proof of [[lem:layer-remainder-past]], every factor with at most one
rotation by the same global bounds. On Ω the rotations have coefficients at most b(τ0), so they cost a constant there.
The induction on i + |β| gives the bound.

(2) *Pointwise bounds.* Let V and e be as in (1), and 0 < y ≤ 1. Then

    (i)  |w(X)| ≤ C_S y^(−1/2) E^♭(τ(X))   at every X ∈ Ω with v(X) + eψ_max + y ≤ V,
    (ii) t^(3/2) |w(X)| ≤ C_S E^Ω(τ(X))    at every X ∈ P with v(X) + eψ_max ≤ V   (case P),

with E^♭ := E_2 in case Ω and E^♭ := E^Ω in case P, and C_S depending on a, b(τ0) only. For (i), let τ := τ(X); the
slice R(V, e) ∩ Σ_τ is {a ≤ r ≤ ρ(τ)}, and ρ(τ) ≥ V − eψ_max − v(X) + r(X) ≥ r(X) + y, so I := [r(X), r(X) + y] lies in
it. For |β| ≤ 2 put f_β(r) := ‖Ω^β w(τ, r, ·)‖_(L²(S³)), a Lipschitz function with |f_β′(r)| ≤
‖∂_r Ω^β w(τ, r, ·)‖_(L²(S³)) almost everywhere. For r ∈ I, f_β(r(X)) ≤ f_β(r) + ∫_I |f_β′|; the mean over r ∈ I and
the Cauchy–Schwarz inequality give

    f_β(r(X)) ≤ y^(−1/2) (∫_I f_β²)^(1/2) + y^(1/2) (∫_I f_β′²)^(1/2) ≤ a^(−3/2) (y^(−1/2) ‖Ω^β w(τ)‖ + ‖∂_r Ω^β w(τ)‖),

the norms on the slice, since r³ ≥ a³ on it. H²(S³) ⊂ L^∞ with the rotations, as in the proof of
[[lem:layer-null-pointwise]], gives |w(X)| ≤ C Σ_(|β|≤2) f_β(r(X)); on Ω, |x| ≤ b(τ0), so ‖Ω^β w‖ + ‖∂_r Ω^β w‖ ≤ C
Σ_(p≤3) ‖∂^p w‖ ≤ C E_2; and y ≤ 1. For (ii), let τ := τ(X) ≤ τ0 and r1 := v_s − τ ≥ v_start − τ = r_in(τ). The points
(τ, r, x̂(X)) with r1 ≤ r ≤ r(X) have v ∈ [v_s, v(X)], so they lie in R(V, e) ∩ P⁺, and w = 0 where v = v_s
([[prop:layer-seed-past]]). Hence f_β(r(X)) ≤ ∫_(r1)^(r(X)) |f_β′| ≤ (v(X) − v_s)^(1/2) r1^(−3/2) ‖∂_r Ω^β w(τ)‖,
with r1 ≥ r_in(τ) ≥ t ([[lem:past-domain]] (d)) and v(X) − v_s ≤ 1; ∂_r = x̂·∂_x commutes with the rotations, so
‖∂_r Ω^β w‖ ≤ ‖∂ Ω^β w‖ ≤ E^Ω, and H²(S³) ⊂ L^∞ as before gives (ii).

(3) *Constants and thresholds.* Let n_0 be the supremum of ‖g0⁻¹‖ over Ω, resp. P ∪ Ω; it is finite, as g0⁻¹ =
η⁻¹ − (μ/r²) L0 ⊗ L0 with μ/r² ≤ μ(v_end)/a² and |L0|_e² = 2. Let C_h bound |g_λ − g0|/λ there (item 4 of [[thm:main]],
resp. items 3 and 4 of [[thm:past-construction]] with [[thm:past-approximant]]). Where n_0 |g_λ − g0| ≤ 1/2, ‖g_λ⁻¹‖ ≤
2n_0 and g_λ⁻¹ − g0⁻¹ = −g0⁻¹ (g_λ − g0) g_λ⁻¹, so ‖g_λ⁻¹ − g0⁻¹‖ ≤ C_g |g_λ − g0| with C_g := 2n_0². Let C_app be a
constant with ϖ |g_app − g0| ≤ C_app λ ε_(c′)(v) at every point of S(v_s + 1) with that v: by [[lem:layer-flat]] (a)–(c)
and [[prop:layer-identification]] in case Ω (|g_j| ≤ C ε_(2j+1)(v) for ε ≤ 1, and 2N + 1 ≤ c′), and by
[[lem:layer-flat-past]] (a)–(c) on P (each profile of g_app − g0 in E_(3/2)(ε), r ≥ t on P⁺, g_app = g0 on P ∖ P⁺). Let
C_G be one with ϖ |w| ≤ C_G λ^(K−3), by step 1 of the proof of [[thm:uniform-existence]] on Ω and item 3 of
[[thm:past-construction]] on P (there |w| ≤ C_G λ^(K−3) t^(−2) and t ≥ 1). Let C_w and C_S be those of (1) and (2), and
C_B := Σ_(i≤c′) c_i (c_0 := 1), so that, by (B_(c′)), [[lem:edge-kappa]] (c) and κ ≥ 1,

    ε_(c′)(V) = Σ_(i≤c′) sup_(v′≤V) |env^(i)(v′)| ≤ Σ_(i≤c′) c_i κ(V)^i env(V) ≤ C_B κ(V)^(c′) env(V)

for v_s < V ≤ v_s + 4x_D, with x_D as below.

Put θ_D := (4 ψ_max C_g C_B (C_app + 2C_S C_w + C_G))⁻¹. Let x_D > 0 be so small that 4x_D ≤ min(x0, v_♯ − v_s, 1),
4x_D ≤ x_j of [[lem:edge-kappa]] (c) for every j ≤ c′, and, for every y ∈ (0, 4x_D], κ(v_s + y) ≥ 1 and y κ(v_s + y) ≥ 4
([[lem:edge-kappa]] (a)), and

    κ(v_s + y/2) κ(v_s + 4y)^(c′+1) env(v_s + 4y) ≤ θ_D      for every y ∈ (0, x_D],                    (D)

which (H_D) with c = c′ + 1 allows. Let λ_D := min{1, λ0, 1/(2C1), 1/(2 n_0 C_h), (8 ψ_max C_g C_G κ(v_s +
x_D/2))^(−1/(K−3))} in case Ω, with λ_P and 1/(2C_P) in place of λ0 and 1/(2C1) in case P. Let λ ≤ λ_D. Then e_0 ≤ 1,
‖g_λ⁻¹ − g0⁻¹‖ ≤ C_g |g_λ − g0| everywhere, and

    Λ_D := (4 ψ_max C_g C_G λ^(K−3))⁻¹ ≥ 2κ(v_s + x_D/2).

κ is continuous, nonincreasing and tends to ∞ at v_s ([[lem:edge-kappa]] (a)), so y_* := sup{y ∈ (0, x_D] : κ(v_s + y)
≥ Λ_D} satisfies 0 < y_* < x_D/2 and κ(v_s + y_*) = Λ_D. Put x̄ := 2y_*.

(4) *The tilt at every depth.* For 0 < x ≤ x_D put e(x) := min(e_0, 1/(ψ_max κ(v_s + x))), and consider the claim

    (Δ_x)      2Δ(v_s + 2x) ≤ e(x).

As 2Δ ≤ e_0 always, (Δ_x) says 2Δ(v_s + 2x) ψ_max κ(v_s + x) ≤ 1. In both steps below we use, for v_s < V ≤ v_s +
4x_D, 2Δ(V) ≤ 2C_g sup_(S(V)) ϖ (|g_app − g0| + |w|), and C_app λ ε_(c′) ≤ C_app ε_(c′) as λ ≤ 1.

*(Δ_x) for x̄/2 ≤ x ≤ x_D.* Here the bound C_G λ^(K−3) of the whole remainder suffices: 2Δ(v_s + 2x) ψ_max κ(v_s + x)
is at most

    2C_g ψ_max C_app C_B κ(v_s + 2x)^(c′) env(v_s + 2x) κ(v_s + x/4) + 2C_g ψ_max C_G λ^(K−3) Λ_D ≤ 1/2 + 1/2,

the first term by κ(v_s + x) ≤ κ(v_s + x/4), κ ≥ 1 and (D) at y = x/2, the second by κ(v_s + x) ≤ κ(v_s + y_*) = Λ_D.

*(Δ_(2x)) implies (Δ_x) for 0 < x < x̄/2.* Put V := v_s + 4x and e′ := e(2x). Then 2Δ(V) ≤ e′ ≤ e_0 by (Δ_(2x)), and

    ε_M(V) ≤ ε_(c′)(v_s + 4y_*) ≤ C_B κ(v_s + 4y_*)^(c′) env(v_s + 4y_*) ≤ C_B θ_D/κ(v_s + y_*/2)
           ≤ C_B θ_D/Λ_D ≤ λ^(K−3) ≤ λ³,

by V < v_s + 2x̄ = v_s + 4y_*, (D) at y = y_*, κ(v_s + y_*/2) ≥ Λ_D, 4C_B θ_D ψ_max C_g C_G ≤ 1 and K ≥ 6. So (1)
applies on R(V, e′). Every X ∈ S(v_s + 2x) satisfies v(X) + e′ψ_max + x ≤ v_s + 2x + 1/κ(v_s + 2x) + x ≤ V, as
2x κ(v_s + 2x) ≥ 4; so (2) with y := x ≤ 1 gives ϖ |w| ≤ C_S C_w x^(−1/2) λ^(N_*) ε_M(V) on S(v_s + 2x). With
x^(−1/2) = 2(4x)^(−1/2) ≤ 2κ(V)^(1/2) ≤ 2κ(V) (as 4x κ(V) ≥ 4 and κ ≥ 1), λ ≤ 1 and ε_M ≤ ε_(c′), 2Δ(v_s + 2x) ψ_max
κ(v_s + x) is at most

    2C_g ψ_max (C_app + 2C_S C_w) C_B κ(V)^(c′+1) env(V) κ(v_s + x/2) ≤ 2C_g ψ_max (C_app + 2C_S C_w) C_B θ_D ≤ 1/2,

by κ(v_s + x) ≤ κ(v_s + x/2) and (D) at y = x. This is (Δ_x).

Every x ∈ (0, x̄/2) is covered: if m ≥ 1 is the least integer with 2^m x ≥ x̄/2, then 2^m x < x̄ ≤ x_D, so (Δ_(2^m x))
holds by the first step, and (Δ_(2^j x)) for j = m − 1, …, 0 by the second, as 2^j x < x̄/2 for j < m. So (Δ_x) holds
for every x ∈ (0, x_D].

(5) *The reach.* Let X be a boundary point with x = v − v_s ≤ x_D and ε_M(v + 1/κ(v)) ≤ λ⁵. Put e := e(x), ρ_v :=
eψ_max ≤ 1/κ(v) and v1 := v + ρ_v ≤ v_s + 2x, since x κ(v_s + x) ≥ 4. Then 2Δ(v1) ≤ 2Δ(v_s + 2x) ≤ e by (Δ_x),
ε_M(v1) ≤ λ⁵ ≤ λ³, and X ∈ R(v1, e), as v(X) + eψ(τ(X)) ≤ v + eψ_max = v1. By (1), the form with four derivatives of
step (2) of the proof of [[lem:edge-degree-two]] holds on R(v1, e), and steps (3) and (4) of that proof use nothing
else of the region: the bounds of [[lem:edge-degree-two]] hold at X with this v1 and reach ρ_v ≤ 1/κ(v). Moreover
ε_c(v) ≤ C_B κ(v)^(c′) env(v); κ(v1) ≤ κ(v) and env(v1) ≤ exp(κ(v)(v1 − v)) env(v) ≤ 3 env(v), as log env is concave
with slope κ(v) at v and v1 − v ≤ 1/κ(v); so η(v1) ≤ ε_(c′)(v1) ≤ 3 C_B κ(v)^(c′) env(v), and [[eq:edge-degree-two]]
gives [[eq:edge-localised]] with C := 13 C_2 C_B². ∎

**Remark {#rem:edge-localisation-numbers}** (Numerical observation.) A descent by depths y_k, each the least depth at
which the reach of the stage before is at most 1/κ, was run with unit constants (C = 10³, cost 30) from the depth 10⁻⁴:
the depths y_k fell as log10 y_k = −4, −439, −5.96·10^437 for exp(−1/x), and −4, −325.3, −8.57·10^323 for env_C, faster
than any geometric sequence, while for env = x^40, which is not flat, the descent stalled at once. At x = λ/10, λ = 10⁻⁶,
for exp(−1/x), the square of the remainder bound with the tilt of order λ exceeded the first-degree term by a factor
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

(3) *The forcing term.* On Σ_τ ∩ S(v) the L² norm of −Re[λ e^(iv/λ) A I_M Ω^β Q b_M] is at most λ A sup_(v′≤v) |I_M(v′)|
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

*Proof.* Take x0′ ≤ x_D of [[lem:edge-localisation]] and x0′ ≤ x_j of [[lem:edge-kappa]] (c) for j ≤ J, so that the
hypotheses of [[lem:edge-kernel]] (c) hold on (v_s, v_s + x0′], and λ_E ≤ λ_D. Fix x̂ and a point X = (v′, r_q(v′), x̂)
with v′ ∈ J_v := [v, v + 4πλ]. By [[lem:layer-inverse]], g_λ⁻¹(dΦ0, dΦ0) = −m0 − k(Φ0♯, Φ0♯) + q with k = g_λ − g0 =
h^(1) + r2 − (g0 − g0°). By [[lem:edge-resummation]] with M = 3,

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
κ^(2c′) env² with c′ = J; by [[eq:edge-degree-two]], |g0 − g0°| ≤ C ε_0² ≤ C κ^(2c′) env²; m0 ≤ C (env² + ∫_(v_s)^(v′)
env²) ≤ C env² by [[cor:layer-expansion]] and [[lem:edge-kappa]] (d); and |q| is smaller. Their ratio to λ env min(λ,
1/κ)² is at most C λ^(−2c′−3) env on {λκ ≤ 1}, which is at most C λ³ once env ≤ λ^(P0), P0 := 2c′ + 6, and at most C
κ^(2c′+3) env on {λκ > 1}, which tends to 0 as v′ ↓ v_s by [[lem:edge-kappa]] (e). So for x0′ and λ small the degree-two
terms are below a tenth of the main term's bound, and g_λ⁻¹(dΦ0, dΦ0) takes both signs on J_v.

For the last statement: if λκ(v + 4πλ) ≥ 1, then by [[lem:edge-kappa]] (e) with p := P0 + 1, env(v + 4πλ) ≤ κ(v +
4πλ)^(−P0−1) ≤ λ^(P0+1) ≤ λ^(P0) once x0′ is small. ∎

**Lemma {#lem:edge-past-levels}** (The levels for the solutions from past null infinity.) The conclusion (ii) of
[[prop:layer-regions]] holds for the metric g_λ of [[thm:past-construction]], with M_P in place of M*: for δ ∈ (0, 1/2]
and P > 4 there is λ_UP > 0 such that for λ ≤ λ_UP, at every first-reach point v of the layer with λ^P ≤ |env(v)| ≤
λ^(3+δ) and every x̂, the boundary has, on [v, v + 4πλ] and at x̂, points where it is timelike and points where it is
spacelike.

*Proof.* The proof of [[prop:layer-regions]] (ii) is that of [[thm:layer]] at the level y := |env(v)| = λ^p, p ∈ [3 + δ,
P], with v in place of v*; for these solutions [[thm:layer-past]] runs the proof of [[thm:layer]] with ν_∞ in place of ν,
so that only the generic case occurs, and with the remainder of [[lem:layer-remainder-past]]. Take m := max(56M_P, 4PM_P,
⌈4M_P/δ⌉) and κ as in [[prop:layer-regions]]. The hypothesis ε_(M_P)(v1) ≤ λ³ of [[lem:layer-remainder-past]] holds,
since ε_(M_P)(v1) ≤ C y^(1−M_P/m) and p(1 − M_P/m) ≥ (3 + δ)(1 − δ/4) = 3 + δ/4 − δ²/4 > 3. The exponent conditions after
[[thm:layer]], with N − 5 replaced by N_P − 3 ≥ K + 9 and M by M_P, hold uniformly in p as in the proof of
[[prop:layer-regions]] (ii). ∎

So, for an envelope increasing on (v_s, v_s + x0] with the hypotheses of [[thm:edge-past]], [[lem:edge-past-levels]]
at P := P0 + 1 and [[thm:edge-past]] together give both signs on every interval [v, v + 4πλ] near v_s with env(v) ≤
λ^(3+δ), for λ small: if env(v) ≥ λ^(P0+1), every point being a first-reach point, the lemma applies; if env(v) <
λ^(P0+1) and λκ(v) ≤ 1, then env(v + 4πλ) ≤ e^(4π) env(v) ≤ λ^(P0) for λ ≤ e^(−4π); and if λκ(v) > 1, then κ ≥
2^(−1/α) κ(v) on [v, v + 4πλ] by [[lem:edge-kappa]] (b), as 4πλ ≤ 4π κ(v)^(−1) ≤ κ(v)^(−α)/(α c_R) near v_s, so
env(v + 4πλ) ≤ (2^(−1/α)/λ)^(−P0−1) ≤ λ^(P0) by [[lem:edge-kappa]] (e), for λ small.

**Remark {#rem:edge-past-numbers}** (Numerical observation.) The bounds of [[lem:edge-kernel]] were sampled on exp(−1/x),
exp(−1/x²) and env_C at λ = 10⁻³ and 10⁻⁶, with λκ from 10⁻² to 10⁴: the ratios |I_n| κ^n/env, |I_n|/(env min(λ, 1/κ)^n)
and |ρ_2|/R_2 stayed at most 1.0000, 1.0002 and 0.9999, and R_2 κ^(1−α) at most 9.33. The frozen local form s̃ := i/λ,
the leading term of the expansion in λ, was off by more than 1 at the very edge. A model of the proof of
[[thm:edge-past]] with unit constants (|ν_∞ d| = 1/9, μ0 = A = 1, a degree-two term 10(1 + λκ)² env² of either sign),
over three carrier periods at five depths from env = λ⁴ to λκ = 1000, λ = 10⁻⁶, and three phases of d, found timelike and
spacelike points in every period of all thirty cases; without the first-degree term, or with a degree-two term 10⁶ λ⁻³
times larger, it found none. No proof uses these figures.

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
𝒟(v) at the points of Σ_τ0 ∩ {v′ ≤ v} for the data and of Ω ∩ {v′ ≤ v} for f, and that the same holds with ∂_v applied to
the amplitudes and C κ_𝒟 𝒟 in place of 𝒟. Let G(r ← r′) be the propagator of 𝒯Z = 0 along ℓ. Then at P = (v, √μ0, x̂),
v_s < v ≤ v_s + x0,

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
zero at r_b := v_s − τ0, of the matching system on Σ_τ0 (equal values and τ-derivatives). By [[lem:edge-characteristic]]
(d) the τ-components of the two phases' differentials on Σ_τ0 are 1 and −F°/(2 − F°), so the system reads s X_in + ((2 −
F°)/2) Ã X_in = ((2 − F°)/2) Â_∂Ψ + (F°/2)(s + A_out) Â_Ψ, X_in + X_out = Â_Ψ, with bounded Ã and A_out;
and |X_in| + |X_out| ≤ C 𝒟, by one integration by parts against e^(iv/λ) where λκ_𝒟 ≤ 1, using the bound on the
derivatives of the amplitudes, and by [[lem:edge-kappa]] (d) for 𝒟 where λκ_𝒟 ≥ 1. 𝒫 annihilates G(r ← r0(v)) X_in(v), so
the residual of h_in is e^(iv/λ) Q G X_in, free of 1/λ; that of h_out is e^(iψ/λ) Q′(H X_out), by
[[lem:edge-characteristic]] (b). The forcing term is taken up by the ingoing particular solution h_f := e^(iv/λ) Z_f with
zero data: Y_f := −∫_(r0(v))^r G(r ← r′) Â_f(v, r′) dr′ along ℓ and Z_f(v, r) := ∫_(τ0+r)^v e^(−i(v−v′)/λ) Y_f(v′, r)
dv′, so that s Z_f = Y_f, 𝒫(s Z_f) = −Â_f, Z_f = s Z_f = 0 on Σ_τ0 and |Z_f| ≤ C 𝒟; its residual is e^(iv/λ) Q Z_f. The
difference e := Ψ − h_in − h_out − h_f has zero data and the forcing term minus the three residuals, at most C 𝒟 in the
strip of v-width x that carries the amplitudes; so [[lem:layer-energy-null]] and [[lem:layer-null-pointwise]] give |Ω^β
e| ≤ C x^(1/2) 𝒟. h_out vanishes for u > u(r_b), a neighbourhood of the horizon's part of the strip. The same holds for
(∂_v − i/λ)Ψ, the solution with data and forcing term (∂_v − i/λ) of those of Ψ (∂_v is Killing for g0° and commutes with
dRic^H), whose amplitudes are ∂_v Â.

(5) *The error terms of (2)–(3).* The ∂_rΨ terms of Q̃Ψ are integrated by parts along the ray, leaving boundary terms
and integrals of Ψ, so |∫ G Q̃Ψ dr′| ≤ C 𝒟(v′) by (4), with angular derivatives up to two. For their integral in v′:
if λκ_𝒟 ≤ 1, one integration by parts against e^(iv′/λ), with the bound on (∂_v − i/λ)Ψ, gives at most C λ 𝒟(v); if
λκ_𝒟 ≥ 1, ∫_(v_s)^v 𝒟 ≤ 𝒟(v)/κ_𝒟 by [[lem:edge-kappa]] (d). Either way it is O(𝒟/|s̃_𝒟|).

(6) *The main terms.* On Σ_τ0, ∂_v|_r = ∂_τ and ∂_r|_v = ∂_r|_τ − ∂_τ, and Ψ_Σ = e^(i(τ0+r)/λ) Â_Ψ(τ0 + r), so LΨ =
(1 − F°/2) ∂_τΨ + (F°/2) ∂_r|_τ Ψ = e^(iv/λ) y exactly. So ∫_(v_s)^v G(√μ0 ← r0(v′)) Y(v′, r0(v′)) dv′ = e^(iv/λ)
s⁻¹(Gy) by [[eq:edge-sinv]], and the term of f in (2) gives the second term of [[eq:edge-ingoing]] in the same way. ∎

**Lemma {#lem:edge-constraint}** (The constraint correction at first degree.) Write D_X H_(N+1) = Σ_k env^(k) D_k, with
D_k functions of (r, r0, ϑ) (r0 = v − τ0), and put c_N := N μ0/(r0² + μ0), p(r) := 3r³/(r² + μ0)² (the coefficient p of
[[lem:constraints-evolution]] at the seed's data) and

    Ξ := ((1 − c_N) T − i c_N)/(T + i),      T = λκ_(N−1).                                         {#eq:edge-xi}

(i) dD(h_app^(1)) = λ^(N+1) Re[D_X H_(N+1) e^(iv/λ)] and dRic^H(h_app^(1)) = λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)] on Ω.

(ii) On Σ_τ0, D_N = i^N A d_1 r^(−3/2) dϑ, and the components (v, r) of D_(N−1) are N i^N A d (−r^(−7/2)/2,
r^(−7/2)).

Assume (H_N) on (v_s, v_s + x0]. Then there is x0′ ∈ (0, x0] such that for v_s < v ≤ v_s + x0′:

(iii) the ρ-component of Φ^(1) at the point of Σ_τ0 with r = r0 = v − τ0 is

    F_ρ = λ^(N+1) Re{ e^(iv/λ) i^N A d(ϑ) r0^(−7/2) [env^(N) − c_N s env^(N−1)] } (1 + O(1/κ + λ));

(iv) a^(1)(r0) = −λ^(N+1) Re{ e^(iv/λ) i^N A d(ϑ) p(r0)⁻¹ r0^(−7/2) env^(N−1) Ξ } (1 + O(ϵ′ + 1/κ + λ)), with ϵ′ of
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

(iv) By [[lem:constraints-evolution]] at the seed's data, the ρ-equation of the linear system for U^(1) is p ∂_r a − Δ_p
a + b′·∂_S a + c a + e·(ϖ, q) = −F_ρ, with p = 3r³/(r² + μ0)². On Σ_τ0, r ↦ v = τ0 + r, and ∂_r acts on e^(iv/λ) times an
amplitude as s on the amplitude. The solution from zero at r = a with this oscillating forcing term is a = −(p s)⁻¹ F_ρ
plus terms of relative order 1/|s̃| (from Δ_p a, b′·∂_S a, c a and e·(ϖ, q), the last through the J-equations, where ϖ is
of order (F_J,r + 2r⁻² ∂_ϑ q)/(6 s̃)); the remainder after two terms of this expansion has a forcing term of relative
order |s̃|⁻², and [[lem:linear-evolution]] on [a, r] makes it O(x^(1/2)/|s̃|) relative. The smooth coefficients p⁻¹
r^(−7/2) and c_N commute with s⁻¹ up to O(λ) relative, by one integration by parts with [[eq:edge-sinv-parts]]. By
[[eq:edge-sinv-parts]], s⁻¹(env^(N) − c_N s env^(N−1)) = (1 − c_N) env^(N−1) − (i/λ) s⁻¹ env^(N−1), and by
[[lem:edge-sinv]] (a) for g := env^(N−1), s⁻¹ env^(N−1) = env^(N−1) (κ_(N−1) + i/λ)⁻¹ (1 + ρ_g), |ρ_g| ≤ C ϵ′. Its
hypotheses hold near v_s by (H_N): g is positive and log-concave with κ_g = κ_(N−1) ∈ [κ/2, 2κ] and the c_R bound,
and |g^(j)| = |env^(N−1+j)| ≤ c_(N−1+j) κ^(N−1+j) env ≤ c 2^(N−1) κ^j g for j ≤ 3, since env = env^(N−1)/Π_(k<N−1) κ_k ≤
2^(N−1) κ^(−(N−1)) env^(N−1). As (i/λ)/(κ_(N−1) + i/λ) = i/(T + i), the bracket becomes env^(N−1)[(1 − c_N) − i/(T + i)]
(1 + O(ϵ′)) = env^(N−1) Ξ (1 + O(ϵ′)). The formulas for |Ξ|² and its expansion are direct: (T + i) = i(1 − iT) gives Ξ =
(−c_N − i(1 − c_N)T)(1 + iT + O(T²)).

*At c_N = 1*, Ξ = −i/(T + i) and |Ξ| = (1 + T²)^(−1/2) → 0 for large T, so the errors must be relative to the bracket
and not to env^(N−1). They are: the two terms of the top family cancel exactly to −(i/λ) s⁻¹ env^(N−1), the
coefficients 1 and c_N being exact; the next family contributes s⁻¹(φ_1 env^(N−1) + φ_2 s env^(N−2)) with smooth φ_i,
of size env^(N−1)(λ + 1/κ_(N−2))(1 + O(ϵ′)) against |T + i|⁻¹ env^(N−1) for the bracket, and |T + i|/κ_(N−2) ≤ 2/κ +
4λ, so it is O(λ + 1/κ) relative for every T; the commutator with c_N′ is O(λ) relative; and the corrections of the
solve are relative by construction.

(v) Write a for a^(1) in this step. At first degree the data that a induces have, in the coordinates (τ, r), the
components h_rr = a, h_τr = a b and h_ττ = a b², b := dr(β) = m/(1 + m) the seed's shift (g0°_τr = m and γ_rr = 1 + m);
the angular components and their τ-derivatives are unchanged. As dτ = dv − dr, a tensor with components X_ττ, X_τr, X_rr
in (τ, r) has the components X_ττ, X_τr − X_ττ and X_ττ − 2X_τr + X_rr in (v, r), in the order vv, vr, rr. In the
notation of [[lem:edge-ingoing]] let ĥ be the amplitude of these data and k̂ that of their τ-derivative, k̂_rr =: k being
any value. The linearised condition D = 0 at the leading order in s, with ∂_τ h ↦ k̂ and ∂_r|_τ h ↦ s ĥ, reads g^(aτ)
k̂_ab + g^(ar) s ĥ_ab − (1/2) δ^τ_b g^(ac) k̂_ac − (1/2) δ^r_b s g^(ac) ĥ_ac = 0 for b = τ, r, with g^(ab) as in
[[lem:edge-characteristic]] (d); its solution is

    k̂_τr = (a s + 2k m(1 + m))/(2(1 + m)²),      k̂_ττ = 2a m s/(1 + m)³ − k(1 − m)/(1 + m).

With F° = 1 − m, y = (1 − F°/2) k̂ + (F°/2) s ĥ has, in (v, r), the components

    y_vv = (a s m(2 − m) − k(1 − m²))/(2(1 + m)),      y_vr = (a s(1 − 2m) + 2k(1 + m))/(4(1 + m)),      y_rr = 0,

so that y_vv + F° y_vr + F°² y_rr/4 = a s/4, free of k. The terms of y without a factor s (derivatives of the
coefficients, the Christoffel terms of D) are O(|a|). So y = s(Φa) + Φ_0 a with Φ, Φ_0 smooth in r0, and the horizon
combination [[eq:edge-transport]] of Φa is r0^(3/2) a/4 times μ0^(−3/4), that is K_R a. Then s⁻¹(G s(Φa)) = GΦa −
s⁻¹(G′Φa), so s⁻¹(Gy) = GΦa − s⁻¹(G′Φa − GΦ_0 a), and the last term is O(λ|a|): by [[eq:edge-sinv-parts]], |s⁻¹h| ≤
λ|h| + λ ∫_(v_s)^v |h′| for h a smooth multiple of a, whose amplitude is Ξ env^(N−1) up to a smooth factor by (iv), and
∫_(v_s)^v (|(Ξ env^(N−1))′| + |Ξ env^(N−1)|) ≤ C |Ξ env^(N−1)|(v). If T(v) ≤ 1, then |Ξ(v)| ≥ c_N/√2 by (iv), and this
follows from ∫_(v_s)^v κ_(N−1) env^(N−1) = env^(N−1)(v) and |Ξ′| ≤ |c_N′| + |T′|/|T + i|² ≤ C κ_(N−1), as |T′| ≤ c_R λ
κ_(N−1)^(1+α) by (H_N). If T(v) ≥ 1, write Ξ = (1 − c_N) − i/(T + i), so that |Ξ| ≥ max(|1 − c_N|, c_N/T)/√2 at v, and
use, at v, ∫ κ_(N−1) env^(N−1)/T = λ⁻¹ ∫ env^(N−1) ≤ env^(N−1)/T ([[lem:edge-kappa]] (d) for env^(N−1)); ∫ κ_(N−1)
env^(N−1) |1 − c_N| ≤ |1 − c_N| env^(N−1) + C λ env^(N−1)/T, as |c_N′| ≤ C and ∫_(v_s)^v κ_(N−1)(v′) env^(N−1)(v′) (v −
v′) dv′ = ∫_(v_s)^v env^(N−1); and ∫ (|c_N′| + |T′|/T²) env^(N−1) ≤ C env^(N−1)/T, as |T′|/T² ≤ c_R κ_(N−1)^(α−1)/λ. This
covers the points near c_N = 1 with T large, where |Ξ| is of order 1/T. (ϖ^(1), q^(1)) change the second fundamental
form; their amplitudes after division by s̃ are of relative order 1/|s̃| and lie in the vector sector and the γ-trace,
which the transport 𝒯Z = 0 does not take to vv. The scalar sector of the data of h_app^(1) is a family lower: κ^(N−2) env
against κ^(N−1) env. ∎

**Proposition {#prop:edge-horizon-value}** (The first-degree horizon value.) Assume (H_N) on (v_s, v_s + x0]. There
are x0′ ∈ (0, x0] and C such that for v_s < v ≤ v_s + x0′, with r0 = v − τ0,

    h^(1)_vv(v, √μ0, ϑ) = Re[S(v, ϑ) e^(iv/λ)],      S = S_st + S_U + E_S,
    S_st := λ³ A ν(r0) d(ϑ) env (1 + 2iλκ) 𝟙_(λκ≤1),      S_U := −λ^(N+1) A Γ_R(r0) i^N d(ϑ) Ξ env^(N−1),
    Γ_R(r0) := K_R r0^(−7/2)/p(r0) = (r0² + μ0)²/(12 μ0^(3/4) r0⁵) > 0,
    |E_S| ≤ C [λ³ env (|ν(r0)| (λκ)² + λ) 𝟙_(λκ≤1) + λ^(N+1) κ^(N−2) env 𝟙_(λκ>1) + (ϵ′ + 1/κ + λ) |S_U|].  {#eq:edge-s}

and |∂_v^k E_S| ≤ C κ^k times the same bound, k ≤ 2.

*Proof.* h^(1) = h_app^(1) + e. *The stage part.* By [[prop:layer-structure]] (c), Σ_(j≤N+1) λ^j H_j,vv(v, √μ0) = λ³ A d
ν Σ_(k≤N−2) (k + 1)(iλ)^k env^(k) + Σ_(j≥4) λ^j Σ_(k≤j−4) c_(j,k),vv env^(k). By (H_N), |env^(k)| = env Π_(i<k) κ_i ≤ 2^k
κ^k env for k ≤ N + 1. For λκ ≤ 1 the first sum is λ³ A d ν env (1 + 2iλκ) + O(|ν| λ³ (λκ)² env), the sum being finite,
and the second is O(λ⁴ env); for λκ > 1 every term λ^j κ^k env with k ≤ j − 3 and j ≤ N + 1 is at most λ^(N+1) κ^(N−2)
env, the vv components having no family above j − 3 (c_(j,j−2) = i^(j−2) c_(2,0) is in 𝔖). *The part e.* By
[[eq:edge-e-equation]], e solves dRic^H(e) = −λ^(N+1) Re[R_X(H_(N+1)) e^(iv/λ)] with the data induced by U^(1). Apply
[[lem:edge-ingoing]] to the complex form, with 𝒟 := C λ^(N+1) env^(N−1), which is of the size of the amplitudes of the
data and of the forcing term divided by |s̃| (the forcing term's top family is env^(N) times a profile, and env^(N) =
κ_(N−1) env^(N−1)), and whose hypotheses hold near v_s by (H_N), as for g = env^(N−1) in the proof of
[[lem:edge-constraint]] (iv): by [[lem:edge-constraint]] (iv) and (v) the data of a^(1) give K_R a^(1)(1 + O(λ)) = Re[S_U
e^(iv/λ)](1 + O(ϵ′ + 1/κ + λ)), the rest of the data at relative order O(1/κ + 1/|s̃|); the forcing term's top family
lies in 𝔖, so its scalar sector is a family below, and its term in [[eq:edge-ingoing]] is at most C λ^(N+1) κ^(N−1)
env/|s̃| in the vv component; and the remainder O(𝒟/|s̃|) is of the same order, at most C(1/κ + λ)|S_U| (|s̃| ≥ κ, and
where |Ξ| is small, T/|s̃| ≤ λ). *The derivatives.* ∂_v commutes with dRic^H, and by (H_N) every amplitude's derivative
is at most C κ times the amplitude; so the derivatives of E_S obey the same bounds with the factor κ^k. ∎

### The crossover {#sec:edge-crossover}

In this section and the next, g_λ is the metric of [[thm:main]], N = K + 3, K ≥ 6, τ0 is admissible, ρ0 := (v_s −
τ0)/√μ0, and (H_N), (H_D) and (B_(c′)) hold on (v_s, v_s + x0], c′ := max(c, M*) with c the cost of
[[lem:edge-degree-two]]. With S of [[prop:edge-horizon-value]] put

    σ := S/(λ³ A d env),      Λ := λ^(N−2) env^(N−1)/env,      ê := E_S/(λ³ A d env),               {#eq:edge-sigma}

so that σ = ν(1 + 2iT0) 𝟙_(T0≤1) − Γ_R i^N Ξ Λ + ê, and by [[eq:edge-s]]

    |ê| ≤ C [(|ν| T0² + λ) 𝟙_(T0≤1) + (Λ/κ) 𝟙_(T0>1) + (ϵ′ + 1/κ + λ) Γ_R |Ξ| Λ].

Two facts are used throughout. First, T = T0(1 + O(κ^(α−1))): κ − κ_(N−1) = Σ_(k<N−1) (κ_k − κ_(k+1)) and κ_(k+1) − κ_k =
κ_k′/κ_k ([[lem:edge-logderivatives]] (c)), each at most c_R (2κ)^α in modulus by (H_N). Second, Λ = λ^(N−2) Π_(k<N−1)
κ_k = Π_(k<N−1) (λκ_k)/λ lies between 2^(−(N−1)) T0^(N−2) κ and 2^(N−1) T0^(N−2) κ. Where ρ0 = ρ*, r0 − ρ*√μ0 = x and, by
[[prop:layer-linear]] (d), ν(r0) = −c_ν x² (1 + O(x)), ν′ = −2c_ν x (1 + O(x)) and |ν″| ≤ 3c_ν near v_s, with c_ν > 0;
elsewhere ν_* := inf |ν| > 0 near v_s. ε(v′) denotes the part of g_λ⁻¹(dΦ0, dΦ0) other than −Re[S e^(iv′/λ)] at a
boundary point; by the proof of [[thm:very-edge]] below, |ε| ≤ C κ^(2c′) env².

**Proposition {#prop:l-26}** (The crossover windows.) Assume in addition (H_N+2) and (H_t) on (v_s, v_s + x0], and, if
ρ0 = ρ*, (H_*). There is M_26 such that for every M ≥ M_26 there are λ_26, x0′ and P1 such that for λ ≤ λ_26, every
window J = [v, v + 4πλ] ⊂ (v_s, v_s + x0′] with env(v + 4πλ) ≤ λ^(P1) on which |ν|/M ≤ Γ_R |Ξ| Λ ≤ M |ν| |1 + 2iT0| has,
at every x̂, points where g_λ⁻¹(dΦ0, dΦ0) is positive and points where it is negative. This holds for every N and every
value of c_N(ρ0), c_N = 1/2 included.

*Proof.* (1) *Splitting.* σ = A_s + B_s + ê, where A_s is the whole stage sum Σ_(j≤N+1) λ^j H_j,vv(v, √μ0) divided by
λ³ A d env, which by [[prop:layer-structure]] (c) is ν(r0) st(v) + λ a₁(r0, v), st := Σ_(k≤N−2) (k + 1)(iλ)^k
env^(k)/env, a₁ a finite sum of smooth coefficients times λ^k env^(k)/env, so that |a₁| ≤ C and |a₁′| ≤ C(1 + T0 κ^α);
B_s := −Γ_R i^N Ξ_ex Λ with the exact Ξ_ex := (1 − c_N) − (i/λ) s⁻¹env^(N−1)/env^(N−1), no replacement of s⁻¹ being
made; and ê the rest, every term of which is O((1/κ + λ)|B_s|) with |∂_v^k ê| ≤ C κ^k (1/κ + λ)|B_s|, k ≤ 2, by the
proofs of [[lem:edge-constraint]] and [[prop:edge-horizon-value]] (the lower families of F_ρ, the corrections of the
solve, the commutators with c_N, p and r^(−7/2), the remainder of [[lem:edge-ingoing]] and its forcing term's part).
The term ϵ′ |S_U| of [[eq:edge-s]] does not occur, as s⁻¹ is kept.

(2) *Derivatives.* By [[lem:edge-sinv]] (b) for g = env^(N−1), Ξ_ex′ = −c_N′ + (i/λ) ρ_g, and by [[lem:edge-sinv]] (c),
whose hypotheses are (H_N+2), |Ξ_ex′| ≤ C(1 + λκ^(1+α)). With Λ′/Λ = κ_(N−1) − κ, (H_t) and |Ξ_ex| ≥ c_N/2 (T0 ≤ 1),
B_s′ = −B_s (κ − κ_(N−1))(1 + O(T0 + κ^(−α))). And A_s′ = ν′ st + ν st′ + λ a₁′ with |st′| ≤ C T0 κ^α, since
(env^(k)/env)′ = (env^(k)/env)(κ_k − κ), |κ_k − κ| ≤ C k κ^α and |env^(k)/env| ≤ (2κ)^k. For the second
derivatives, |B_s″| ≤ C |B_s| κ^(1+α), by (H_N) and ρ_g′ = κ_g′(1 + ρ_g)/s̃_g − s̃_g ρ_g, |ρ_g′|/λ ≤ C κ^(1+α)
([[lem:edge-sinv]] (b), (c)); |A_s″| ≤ C(|ν| + λ) κ^(1+α) (at ρ*, |ν″| ≤ 3c_ν ≤ C|ν|κ as κx² ≥ c_* and |ν| ≥ c_ν x²/2,
and |ν′| ≤ C|ν|κ^α, see (4)); and |ê″| ≤ C(κ + λκ²)|B_s|.

(3) *|A_s| at a near-cancellation.* Off ρ*, |ν| ≥ ν_*. At ρ*, x² ≥ Mλ on J: if x² < Mλ, then κ ≥ c_*/(Mλ) by (H_*),
T0 ≥ c_*/M and Λ ≥ 2^(−(N−1)) T0^(N−2) κ ≫ M|ν|, against the hypothesis on J. So |A_s − ν| ≤ C(|ν| T0 + λ) ≤ |ν|/8
for λ small and M large, using λ ≤ 2|ν|/(c_ν M) at ρ*.

(4) *The dichotomy.* Put τ := c_t κ^(α−1) |ν|/16, κ at v. Over J, |σ′| ≤ C|ν|κ^α by (2): at ρ*, |ν′| ≤ 2c_ν x(1 + o(1))
≤ C|ν|κ^α, since κ^(−α) ≤ α c_R x ([[lem:edge-kappa]] (a)); off ρ*, |ν′| ≤ C ≤ C|ν|/ν_*.

If |A_s + B_s| ≥ τ on J, then |σ| ≥ τ/2, since |ê| ≤ C(1/κ + λ)M|ν| is much smaller than τ (κ^(α−1) ≫ 1/κ, and λ ≪
κ^(α−1) as T0 → 0); arg σ moves over J by at most 4πλ C|ν|κ^α/(τ/2) = 128πC T0/c_t ≤ π/6; and |ε| ≤ C κ^(2c′) env²
≤ |S|/4 pointwise once env ≤ λ^(P1). [[lem:edge-two-signs]] (A) applies to f = Re[−S e^(i·/λ)] + ε.

Otherwise |A_s + B_s| < τ at some t₀ ∈ J, hence |A_s + B_s| ≤ τ + 4πλC|ν|κ^α ≤ 2τ on J, as λκ = T0 → 0. Then B_s = −A_s +
O(τ) = |ν|(1 + O(1/8 + τ/|ν|)) lies near the positive real axis, ν being negative. So Re B_s′ ≤ −|ν| c_t κ^α/2 by (2) and
(H_t); and Re A_s′ ≤ C(|ν| T0 κ^α + λ(1 + T0κ^α)) + C 𝟙_(ρ0≠ρ*), because Re(ν′ st) ≤ 0 at ρ* (ν′ < 0 and Re st ≥ 1/2)
and |ν′| ≤ C ≪ |ν|κ^α off ρ*. With |ê′| ≤ C(1 + T0)M|ν|, Re σ′ ≤ −|ν| c_t κ^α/3. As S = λ³ A d env σ, S′ = λ³ A d env
(κσ + σ′) and |κσ| ≤ 2κτ = c_t |ν| κ^α/8, so

    |S′| ≥ λ³ A |d| env |ν| c_t κ^α/5 =: L0      on J

(env changes by a factor at most e^(8πT0) ≤ 2 across J), while |S″| = λ³ A |d| env |κ²σ + κ′σ + 2κσ′ + σ″| ≤ C λ³ A |d|
env |ν| κ^(1+α) ≤ L0/(80πλ) once λκ ≤ c_t/(400πC), which holds as T0 → 0; and |ε| ≤ πλL0/5 once env ≤ λ^(P1), since |ν| ≥
ν_* off ρ* and |ν| ≥ c_ν Mλ/2 at ρ*. [[lem:edge-two-signs]] (B) applies. ∎

Nothing in (4) depends on c_N(ρ0) or on N modulo 4: the transversality is Λ′/Λ = κ_(N−1) − κ with (H_t), and the sign
of B_s′ against A_s′ is fixed by ν ≤ 0, ν′ ≤ 0 at ρ* and Λ decreasing. No lower bound for |σ| is used where |σ| is small.
At ρ* the stage family below the top, λa₁, is kept in A_s exactly, and only its smallness against ν, step (3), is used;
that is (H_*).

At ρ0 = ρ* without (H_*) the family below the top is needed. Write, with ρ*√μ0 the value of r0 at the edge,

    b̂4(r0, ϑ) := c_(4,0),vv(√μ0; r0, ϑ)/(A d(ϑ)),      b̂5(r0, ϑ) := c_(5,1),vv(√μ0; r0, ϑ)/(i A d(ϑ)),

with c_(j,k) of [[prop:layer-structure]] (b), the derivative ∂_v acting on r0 as well; so the family contributes λ(b̂4 +
i T0 b̂5 + …) to a₁.

**Lemma {#lem:edge-next-family}** (The family below the top at the horizon.) For every wave, every r0 > √μ0 and every
ϑ, with ρ := r0/√μ0 and Δ the Laplacian of S³ (Δf = (cos ϑ sin ϑ)⁻¹ ∂_ϑ(cos ϑ sin ϑ ∂_ϑ f)),

    c_(4,0),vv(√μ0; r0, ϑ) = A μ0^(−9/4) [α4(ρ) d(ϑ) + β4(ρ) Δd(ϑ)],
    α4(ρ) := −i (6376ρ⁹ − 26460ρ⁸ + 58590ρ⁷ − 74865ρ⁶ + 132300ρ⁵ − 122661ρ⁴ + 8400ρ³ + 4320ρ² + 25340)/(90720 ρ⁹),
    β4(ρ) := i (ρ − 1)(2ρ³ − 3ρ² − 2)²/(72 ρ⁷).                                                  {#eq:edge-next-family}

In particular β4(ρ*) = 0, and at every ϑ with d(ϑ) ≠ 0

    b̂4(ρ*√μ0, ϑ) = μ0^(−9/4) α4(ρ*) = μ0^(−9/4) i (366ρ*² − 153ρ* − 934)/420,
    −0.038203 < (366ρ*² − 153ρ* − 934)/420 < −0.038174.

So b̂4 is purely imaginary and nonzero at ρ*, the same at every angle, and δ_* := inf_ϑ dist(b̂4(ρ*√μ0, ϑ), [0, ∞)) >
0.03817 μ0^(−9/4). Moreover b̂4(r0, ϑ) and b̂5(r0, ϑ) are smooth in r0 for the waves of [[sec:layer-linear]], as |d| ≥
8/3 ([[lem:layer-angular]]) and c_(5,1) is smooth.

*Proof.* We use the recursion of [[prop:layer-structure]] (b) for c_(j+1,l) itself: as c_(j+1,l) = κ_(j+1,l) + i(∂_(r0)
c_(j,l) + c_(j,l−1)) and Π = Pol⁺ Pol,

    𝒯 c_(j+1,l) = −[−i 𝒯(∂_(r0) c_(j,l) + c_(j,l−1)) + Q c_(j,l)],
    c_(j+1,l) = i Pol⁺[Pol(∂_(r0) c_(j,l) + c_(j,l−1)) + q c_(j,l)]      at r = r0,                       (R)

the brackets being the families l of R_X H_j and of D_X H_j ([[prop:layer-structure]] (a)); c_(1,0) = A r^(1/2) T and
c_(j,−1) := 0.

(1) *Scaling.* Put σ := √μ0 and Φ(v, r, x̂) := (σv, σr, x̂). By [[eq:eq-g0]] with μ ≡ μ0, Φ*g0° = σ² g̃, where g̃ is the
seed of mass 1, and Φ multiplies the Cartesian coordinates (τ, x) by σ. Ric^H is unchanged when the metric and the
reference metric are multiplied by one constant, and so is the lowered gauge D, while both are natural under Φ; so for
𝒮h := σ⁻² Φ*h, Φ*(dRic^H(h)) = dRic̃^H(𝒮h) and Φ*(dD(h)) = dD̃(𝒮h), the tilde marking the objects of g̃. For h = H
e^(iv/λ), Φ*h = (Φ*H) e^(iṽ/λ̃) with λ̃ := λ/σ, and comparing the coefficients of the powers of λ⁻¹ in
[[lem:layer-seed-operators]] (b) gives 𝒮(𝒯H) = σ⁻¹ 𝒯̃(𝒮H), 𝒮(R_X H) = σ⁻² R̃_X(𝒮H), Φ*(Pol H) = σ Pol̃(𝒮H) and
Φ*(D_X H) = D̃_X(𝒮H). The matrix of Pol at a point depends only on F°(r) = 1 − μ0/r², which takes the same value at
corresponding points, and Φ* multiplies the Cartesian components of covectors by σ and of 2-tensors by σ²; so Pol̃ and
Pol̃⁺ have the matrices of Pol and Pol⁺, and 𝒮(Pol⁺V) = σ⁻¹ Pol̃⁺(Φ*V). Since ∂_(r0) = σ⁻¹ ∂_ρ, (R) and induction on j
give 𝒮c_(j,l) = σ^(l−j−1/2) c̃_(j,l), with c̃_(j,l) the coefficients of mass 1 at r̃0 = ρ, starting from 𝒮c_(1,0) =
σ⁻² σ^(1/2) A r̃^(1/2) T. The vv component of 𝒮c is the vv component of c at the corresponding point, as v is scaled by
σ. So c_(4,0),vv(√μ0; r0) = μ0^(−9/4) c̃_(4,0),vv(1; ρ), and it suffices to prove [[eq:edge-next-family]] at μ0 = 1,
which we assume from now on; r0 = ρ, F := 1 − r⁻².

(2) *Reduction to one harmonic.* Let 𝔴(ϑ) := ∫_0^ϑ d_1; 𝔴 is a smooth T²-invariant function on S³, as d_1 dϑ = div_γ T is
a smooth closed form. For a smooth T²-invariant 𝔲 put 𝕊(𝔲)_AB := ∇_A ∇_B 𝔲 − (1/3) γ_AB Δ𝔲, on the unit S³. Its
divergence is (2/3) d((Δ + 3)𝔲), by ∇^A ∇_A ∇_B 𝔲 = ∇_B Δ𝔲 + 2 ∇_B 𝔲 (the Ricci tensor of S³ is 2γ); so div div 𝕊(𝔲) =
(2/3) Δ(Δ + 3)𝔲. The kernel of Δ + 3 consists of the restrictions of linear functions of ℝ⁴, of which none but 0 is
T²-invariant; so 𝔲 := (3/2)(Δ + 3)⁻¹ 𝔴 is smooth and T²-invariant, and T_tt := T − 𝕊(𝔲) is γ-traceless with div_γ T_tt =
0, and d = (2/3) Δ(Δ + 3) 𝔲.

The part T_tt contributes nothing to any component of the profiles but the angular traceless ones. Indeed let h = f(v, r)
𝔗 with 𝔗 angular, γ-traceless and divergence-free. Then Pol h = 0 and D_X h = 0, by [[eq:layer-components]] and the
divergence formula in the proof of [[prop:layer-linear]] (a). In −(1/2)□h + 𝔚(h), written with [[eq:layer-christoffel]]
and the curvature of g0° (whose nonzero components are, up to symmetries, R_vrvr = −3/r⁴, R_vAvB = F γ_AB/r², R_vArB =
−γ_AB/r² and R_ABCD = γ_AC γ_BD − γ_AD γ_BC), every component with an index v or r is a combination, with coefficients
depending on (v, r), of γ^(AB) 𝔗_AB, of div_γ 𝔗 and of div_γ div_γ 𝔗, so it vanishes; and the angular part is a
combination of 𝔗 and of the rough Laplacian Δ̊𝔗 of the unit S³, with the same kind of coefficients, plus terms in γ
tr_γ 𝔗 and in the symmetrised gradient of div_γ 𝔗, which vanish. On S³, of constant curvature, div_γ Δ̊𝔗 − Δ̊ div_γ 𝔗
is a combination of div_γ 𝔗 and of d tr_γ 𝔗 (Ricci identity), so Δ̊𝔗 is again traceless and divergence-free; and
𝒯h = −i(∂_r − 1/(2r)) h is of the same form. So, by (R), the T_tt-part of every c_(j,l) is of this form, and its vv
component vanishes. By linearity it remains to treat T = 𝕊(𝔲), and, expanding 𝔲 in T²-invariant eigenfunctions of Δ
(the series converges with all derivatives, 𝔲 being smooth, and c_(4,0),vv(1) is a linear differential operator in the
angles applied to 𝔲), to treat 𝔲 = Y with ΔY = −kY. Then d = ω_k Y and d_1 = ω_(1,k) Y′ with

    ω_k := (2/3) k (k − 3),      ω_(1,k) := (2/3)(3 − k),      Y″ = −kY − 2 cot(2ϑ) Y′,

and [[eq:edge-next-family]] reads c_(4,0),vv(1) = A ω_k Y (α4 − k β4).

(3) *The operators on one harmonic.* Write [f_vv, f_vr, f_rr; f_v, f_r; f_P, f_S] for the tensor with h_vv = f_vv Y,
h_vr = f_vr Y, h_rr = f_rr Y, h_vϑ = f_v Y′, h_rϑ = f_r Y′ and h_AB = f_P γ_AB Y + f_S 𝕊(Y)_AB, the f functions of r;
and write a covector V = V_v Y dv + V_r Y dr + V_t Y′ dϑ as (V_v, V_r, V_t). The operators keep this form, and the rows
used below are, with ′ = ∂_r,

    (Qh)_vv = (r⁻² − 1) f_vv″/2 + (5/(2r³) − 3/(2r)) f_vv′ + (k/(2r²) + 3/r⁴) f_vv + (6/r⁴ − 4/r⁶) f_vr
              + (3/r⁴ − 5/r⁶ + 2/r⁸) f_rr + (3/r⁸ − 3/r⁶) f_P,
    (Qh)_vr = (r⁻² − 1) f_vr″/2 + (1/(2r³) − 3/(2r)) f_vr′ + ((k + 3)/(2r²) − 9/(2r⁴)) f_vr + 3 f_vv/(2r²)
              + (2/r⁶ − 3/r⁴) f_rr + 3 f_P/r⁶ − k f_v/r³,
    (Qh)_rr = (r⁻² − 1) f_rr″/2 − (3/(2r) + 3/(2r³)) f_rr′ + (k/(2r²) + 3/r²) f_rr + 3 f_vr/r² − 3 f_P/r⁴ − 2k f_r/r³,
    (Qh)_v  = (r⁻² − 1) f_v″/2 + (1/(2r³) − 1/(2r)) f_v′ + (k/(2r²) − 2/r⁴) f_v + (1/r³ − 1/r) f_vr − f_vv/r,
    (Qh)_S  = (r⁻² − 1) f_S″/2 + (1/(2r) − 3/(2r³)) f_S′ + ((k − 4)/(2r²) + 2/r⁴) f_S + (2/r³ − 2/r) f_r − 2 f_v/r,
    (qh)_r  = (1 − r⁻²) f_rr′/2 + (3/r − 1/r³) f_rr + 3 f_vr/r − 3 f_P′/(2r²) − k f_r/r²,
    (qh)_t  = (1 − r⁻²) f_r′ + (3/r − 1/r³) f_r + f_v′ + 3 f_v/r − f_vr − F f_rr/2 − f_P/(2r²) + 2(3 − k) f_S/(3r²).

Each row is −(1/2)□h + 𝔚(h), resp. div h − (1/2) d tr h ([[lem:layer-seed-operators]] (a)), written in components with
[[eq:layer-christoffel]] and the curvature listed in (2), after Y″ is replaced by −kY − 2 cot(2ϑ) Y′ and 𝕊(Y)_ϑϑ =
Y″ + kY/3, 𝕊(Y)_φ1φ1 = −cs Y′ + c²kY/3, 𝕊(Y)_φ2φ2 = cs Y′ + s²kY/3 (c = cos ϑ, s = sin ϑ) are used. 𝒯 is
[[eq:layer-components]] row by row, tr h = F f_rr + 2 f_vr + 3 f_P/r², and Pol⁺ is [[eq:layer-pol-plus]]: it maps
(V_v, V_r, V_t) to [V_r/4, −V_r/2, V_r; −V_t/2, V_t; −(F V_r + 2V_v) r²/3, 0]. As a check, (q c_(1,0))_t = A ω_(1,k)
r^(−3/2) is the D_X H_1 of [[prop:layer-linear]] (a).

(4) *The null component.* Let L := ∂_v + (F/2) ∂_r. Then ∇_ℓ L = Γ^r_rv ∂_r + (F′/2) ∂_r = (−r⁻³ + r⁻³) ∂_r = 0 by
[[eq:layer-christoffel]], so for every symmetric Z, ∂_r(Z(L, L)) = (∇_ℓ Z)(L, L) and

    ∂_r (r^(3/2) Z(L, L)) = i r^(3/2) (𝒯Z)(L, L),      Z(L, L) = Z_vv + F Z_vr + F² Z_rr/4,

with Z(L, L) = Z_vv at r = 1, where F = 0. Apply this to Z := c_(4,0), with 𝒯Z from (R), and integrate from 1 to r0;
the term of 𝒯 ∂_(r0) c_(3,0) integrates to boundary values by the same identity, and Pol⁺V(L, L) = V_r (1 − F)²/4 =
V_r/(4r⁴). With [D_X H_3]_0 := Pol(∂_(r0) c_(3,0)) + q c_(3,0) this gives

    c_(4,0),vv(1) = t1 + t2 + t3 + t4,      t1 := i r0^(−5/2) [D_X H_3]_(0,r)(r0)/4,
    t2 := −i r0^(3/2) (∂_(r0) c_(3,0))(L, L)|_(r=r0),      t3 := i ∂_(r0) c_(3,0),vv(1),
    t4 := i ∫_1^(r0) r^(3/2) (Q c_(3,0))(L, L) dr.

(5) *The coefficients c_(2,0) and c_(3,0).* By (R) with c_(1,0) = [0, 0, 0; 0, 0; 0, A r^(1/2)]: (Q c_(1,0))_S = A((4k −
13) r² + 9)/(8 r^(7/2)), (q c_(1,0))_t = A ω_(1,k) r^(−3/2), and the transport gives c_(2,0) = [0, 0, 0; f_v, f_r; 0,
f_S] with

    f_r = i A ω_(1,k) r^(−3/2),      f_v = i A ω_(1,k) r^(−1/2) β_2(r),      β_2 = −1/(2r0) + (r⁻³ − r0⁻³)/3,
    f_S = −i A (r − r0)((4k − 13) r² r0² + 3(r² + r r0 + r0²))/(8 r^(5/2) r0³),

as in [[eq:layer-h2]] (the last from −i r^(1/2) ∫_(r0)^r s^(−1/2) (Q c_(1,0))_S ds). For c_(3,0): its components vv, vr,
rr are those of H_3/env in [[eq:layer-h3]], as c_(3,1) = i c_(2,0) has none ([[prop:layer-structure]] (b)), and its
trace is 0, so

    f_rr = −A ω_k r^(−7/2),   f_vr = −A ω_k r^(−5/2) β_2,   f_vv = −A ω_k r^(−3/2) β_2²,
    f_P = −(r²/3)(F f_rr + 2 f_vr) = −A ω_k (3r³r0² + 2r³ − 3r²r0³ + r0³)/(9 r^(7/2) r0³).

By [[lem:layer-bianchi]] (b), i Pol(H_3) + D_X H_2 = 0, whose ϑ-component in family 0 is f_r = i (q c_(2,0))_t (as
∂_(r0) of the f_r of c_(2,0) vanishes):

    f_r = −A (k − 3)(12k r³r0² − 12k r²r0³ − 9r³r0² + 29r³ + 3r²r0³ − 17r0³)/(36 r^(9/2) r0³).

The ϑ-component v solves, by (R), (∂_r + 1/(2r)) f_v + f_r/r³ = −i (Q c_(2,0))_v, with f_v(r0) = −f_r(r0)/2 from Pol⁺
(the v-row of 𝒯 ∂_(r0) c_(2,0) is zero, as ∂_(r0)(r^(−1/2) β_2) = r^(−1/2)(r0² + 2)/(2r0⁴) is annihilated by
∂_r + 1/(2r) and ∂_(r0) of the f_r of c_(2,0) vanishes), where

    (Q c_(2,0))_v = i A (k − 3)(12k r⁵r0² + 8k r⁵ − 8k r²r0³ − 3r⁵r0² − 2r⁵ − 45r³r0² − 30r³ + 98r²r0³ − 66r0³)
                    /(72 r^(15/2) r0³);

its solution is

    f_v = A (k − 3)(36k r⁶r0⁴ + 24k r⁶r0² − 36k r⁵r0⁵ − 24k r⁵r0³ − 24k r³r0⁵ + 24k r²r0⁶ − 27r⁶r0⁴ + 45r⁶r0²
          − 22r⁶ + 9r⁵r0⁵ + 6r⁵r0³ + 63r³r0⁵ − 28r³r0³ − 78r²r0⁶ + 50r0⁶)/(216 r^(13/2) r0⁶),

which one checks by substituting it into the equation and at r = r0.

(6) *The four terms.* By (3) and (5), with the factor A ω_k taken out,

    (Q c_(3,0))_vv/(A ω_k) = −(36k r⁸r0⁴ + 48k r⁸r0² + 16k r⁸ − 48k r⁵r0⁵ − 32k r⁵r0³ + 16k r²r0⁶ + 27r⁸r0⁴ + 36r⁸r0²
                           + 12r⁸ + 81r⁶r0⁴ + 108r⁶r0² + 36r⁶ − 612r⁵r0⁵ − 408r⁵r0³ + 1152r⁴r0⁶ + 468r³r0⁵
                           + 312r³r0³ − 1908r²r0⁶ + 804r0⁶)/(288 r^(23/2) r0⁶),
    (Q c_(3,0))_vr/(A ω_k) = −(36k r⁶r0⁴ + 24k r⁶r0² − 72k r⁵r0⁵ − 48k r⁵r0³ − 24k r³r0⁵ + 48k r²r0⁶ + 27r⁶r0⁴
                           + 117r⁶r0² + 2r⁶ − 54r⁵r0⁵ − 36r⁵r0³ + 234r³r0⁵ + 86r³r0³ − 1044r²r0⁶ + 920r0⁶)
                           /(144 r^(19/2) r0⁶),
    (Q c_(3,0))_rr/(A ω_k) = (24k r³r0² − 36k r²r0³ + 42r³r0² + 98r³ − 27r²r0³ − 365r0³)/(24 r^(15/2) r0³),
    [D_X H_3]_(0,r)/(A ω_k) = (q c_(3,0))_r/(A ω_k)
                          = (12k r³r0² − 12k r²r0³ + 21r³r0² + 49r³ − 9r²r0³ − 73r0³)/(24 r^(13/2) r0³),

the f_rr of c_(3,0) not depending on r0. Hence r^(3/2) (Q c_(3,0))(L, L)/(A ω_k) = I(r)/(288 r¹⁰ r0⁶) with

    I(r) := −(108k r0⁴ + 96k r0² + 16k + 81r0⁴ + 270r0² + 16) r⁸ + (216k r0⁵ + 96k r0³ + 234r0⁵ + 366r0³) r⁷
            − (108k r0⁶ − 72k r0⁴ − 48k r0² + 81r0⁶ + 27r0⁴ − 126r0² + 32) r⁶ − (192k r0⁵ + 64k r0³ + 216r0⁵
            + 424r0³) r⁵ + (120k r0⁶ + 3r0⁶) r⁴ + (24k r0⁵ + 126r0⁵ + 154r0³) r³ − (28k r0⁶ − 89r0⁶) r² − 59r0⁶,

which has no term in r⁹, so its quotient by r¹⁰ has an antiderivative without logarithm: G(r) := J(r)/(90720 r⁹ r0⁶),

    J(r) := (34020k r0⁴ + 30240k r0² + 5040k + 25515r0⁴ + 85050r0² + 5040) r⁸ − (34020k r0⁵ + 15120k r0³ + 36855r0⁵
            + 57645r0³) r⁷ + (11340k r0⁶ − 7560k r0⁴ − 5040k r0² + 8505r0⁶ + 2835r0⁴ − 13230r0² + 3360) r⁶
            + (15120k r0⁵ + 5040k r0³ + 17010r0⁵ + 33390r0³) r⁵ − (7560k r0⁶ + 189r0⁶) r⁴
            − (1260k r0⁵ + 6615r0⁵ + 8085r0³) r³ + (1260k r0⁶ − 4005r0⁶) r² + 2065r0⁶,

satisfies G′(r) = I(r)/(288 r¹⁰ r0⁶) (differentiate term by term), and t4/(A ω_k) = i(G(r0) − G(1)), with

    G(r0) = (11340k r0⁶ + 15120k r0⁴ + 5040k r0² − 2835r0⁶ + 47061r0⁴ + 14580r0² − 2660)/(90720 r0⁹),
    G(1) = (2520k r0⁶ − 10080k r0⁵ + 13230k r0⁴ − 5040k r0³ + 12600k r0² + 2520k + 3188r0⁶ − 13230r0⁵ + 14175r0⁴
           − 16170r0³ + 35910r0² + 4200)/(45360 r0⁶).

With (5), the other three terms are

    t1/(A ω_k) = i (r0² − 2)/(8 r0⁹),      t2/(A ω_k) = −i (r0² + 2)/(2 r0⁷),
    t3/(A ω_k) = −i (r0² + 2)(2r0³ − 3r0² − 2)/(6 r0⁷),

t1 from [D_X H_3]_(0,r)(r0) = A ω_k (r0² − 2)/(2 r0^(13/2)), t2 from (∂_(r0) c_(3,0))(L, L) = A ω_k (r0² + 2)/(2
r0^(17/2)) at r = r0, and t3 from ∂_(r0) β_2 = (r0² + 2)/(2r0⁴) and β_2(1) = (2r0³ − 3r0² − 2)/(6r0³). Over the
denominator 90720 r0⁹, G(r0) − G(1) gives

    t4/(A ω_k) = −i (r0 − 1)(5040k r0⁸ − 15120k r0⁷ + 11340k r0⁶ − 10080k r0⁵ + 15120k r0⁴ + 5040k r0² + 6376r0⁸
               − 20084r0⁷ + 8266r0⁶ − 21239r0⁵ + 50581r0⁴ + 3520r0³ + 11920r0² − 2660r0 − 2660)/(90720 r0⁹).

The terms with k come from t4 alone; as 5040r0⁸ − 15120r0⁷ + 11340r0⁶ − 10080r0⁵ + 15120r0⁴ + 5040r0² = 1260 r0² (2r0³ −
3r0² − 2)², they add up to −i k (r0 − 1)(2r0³ − 3r0² − 2)²/(72 r0⁷) = −k β4. The terms free of k, from the sum t1 + t2 +
t3 + t4 over 90720 r0⁹, add up to α4. So c_(4,0),vv(1) = A ω_k Y (α4 − k β4), which is [[eq:edge-next-family]] at μ0 = 1.

(7) *At ρ*.* β4(ρ*) = 0 as 𝔭(ρ) := 2ρ³ − 3ρ² − 2 vanishes at ρ*. With 𝔫(ρ) the numerator of α4, the identity

    −𝔫(ρ) − 216 ρ⁹ (366ρ² − 153ρ − 934) = 𝔭(ρ) (−39528ρ⁸ − 42768ρ⁷ + 33532ρ⁶ + 24000ρ⁵ − 36063ρ⁴ + 16870ρ³
                                                 − 16845ρ² + 12670)

holds (multiply out), so at ρ* α4(ρ*) = −i 𝔫(ρ*)/(90720 ρ*⁹) = i · 216 (366ρ*² − 153ρ* − 934)/90720 = i (366ρ*² − 153ρ* −
934)/420. Since 𝔭(1.80644) < −3 · 10⁻⁵ < 0 < 5 · 10⁻⁵ < 𝔭(1.80645) and 𝔭 increases on (1, ∞), 1.80644 < ρ* < 1.80645; and
366ρ² − 153ρ − 934 increases there, and is above −16.04480 at 1.80644 and below −16.03310 at 1.80645, which gives the
enclosure. At ρ*, c_(4,0),vv(√μ0) = A μ0^(−9/4) α4(ρ*) d, so b̂4 = μ0^(−9/4) α4(ρ*) wherever d ≠ 0. ∎

**Lemma {#lem:edge-rho-star}** (ρ* without (H_*).) Let ρ0 = ρ*, and assume (H_N+2), (H_D) and (H_t) on (v_s, v_s + x0].
There are λ_28, x0′ and P1 such that for λ ≤ λ_28 every window J = [v, v + 4πλ] ⊂ (v_s, v_s + x0′] with env(v + 4πλ) ≤
λ^(P1) has, at every x̂, points where g_λ⁻¹(dΦ0, dΦ0) is positive and points where it is negative, for every N.

*Proof.* If (H_*) holds, this is the proof of [[thm:very-edge]] below at ρ*; so let liminf κ(v)(v − v_s)² = 0. Let M be
the constant fixed in that proof; δ_* > 0 is that of [[lem:edge-next-family]]. Then α > 1/2, since α ≤ 1/2 gives κx² ≥
(αc_R)^(−1/α) x^(2−1/α) ≥ c > 0 by [[lem:edge-kappa]] (a). Split by the size of ν at the left end t₀ of J; ν moves over J
by at most 8πc_ν x λ ≪ λ. Let C_a bound |a₁| and put M′ := 16 C_a.

(1) *|ν(t₀)| ≥ 2M′λ.* Then |λa₁| ≤ |ν|/8 on J, which is all that step (3) of [[prop:l-26]] and the cases of the proof of
[[thm:very-edge]] take from (H_*) at ρ*: the bound λ ≪ Λ of Case 1 (Λ ≥ M|ν|/(Γ_R|Ξ|) ≥ c M M′ λ), the bound λ ≪ |ν| of
Case 2 and of Case 3 (i), and, for N ≡ 0 modulo 4, [[prop:l-26]] itself. The other use of (H_*) in [[prop:l-26]], |ν″| ≤
C|ν|κ, is replaced by |ν″| ≤ 3c_ν ≤ |ν| κ^(1+α), which holds near v_s since x² κ^(1+α) ≥ κx/(α c_R) → ∞ (κ^α ≥ 1/(α c_R
x)); the phase bounds use |ν′| ≤ 3c_ν x ≤ C|ν|κ^α and λ/x ≤ (λc_ν/M′)^(1/2).

(2) *|ν(t₀)| < 2M′λ.* Then |ν| ≤ 3M′λ on J. With a₁ = b̂4(r0, ϑ) + iT0 b̂5 + O(T0² + λ) and b̂4(r0) − b̂4(ρ*√μ0) =
O(x),

    A_s = ν(1 + 2iT0) + λ b̂4(ρ*√μ0, ϑ) + O(λ(T0 + x + λ)),      dist(A_s, [0, ∞)) ≥ λδ_*/2

for T0, x and λ small, because dist(z + ν, [0, ∞)) = dist(z, [|ν|, ∞)) ≥ dist(z, [0, ∞)) for ν ≤ 0. Three cases, those
of the proof of [[thm:very-edge]] with |ν| replaced by λ.

*R1:* Γ_R|Ξ|Λ ≥ Mλ or T0 > 1. Then |σ| ≥ Γ_R|Ξ|Λ/2, the phase moves as in Case 1, and [[lem:edge-two-signs]] (A)
applies.

*R2:* Γ_R|Ξ|Λ ≤ λδ_*/M. Then T0 → 0 (Λ ≥ 2^(−(N−1)) T0^(N−2) κ and Λ ≤ Cλ), |σ| ≥ λδ_*/4, and arg σ moves over J by at
most 4πλ(|ν′| + C|ν|T0κ^α + Cλ(1 + T0κ^α) + |B_s′| + |ê′|)/(λδ_*/4). Here |ν′| ≤ C x ≤ Cλ^(1/2), |B_s′| ≤ Γ_R
Λ(|Ξ_ex′| + |Ξ_ex| |κ − κ_(N−1)|) ≤ C λδ_* κ^α/M by step (2) of [[prop:l-26]], |Ξ_ex| ≥ c_N/2 and κ ≥ 1, and |ê′| ≤ C(1 +
T0)Γ_R|Ξ|Λ ≤ Cλδ_*/M by step (1) there. So the motion is at most C(λ^(1/2) + λ^(1−α) T0^(1+α))/δ_* + 16πC(T0 κ^(α−1) +
λ)/M → 0, and [[lem:edge-two-signs]] (A) applies.

*R3:* otherwise. Then Λ ≍ λ, so T0 ≍ λ^(2/(N−1)) → 0 and λκ^(1+α) = T0^(1+α) λ^(−α) ≍ λ^(2(1+α)/(N−1)−α) → ∞, as α >
1/2 > 2/(N − 3) for N ≥ 9. Put τ := c_t δ_* λ κ^(α−1)/16; |ê| ≤ C(1/κ + λ)Mλ ≪ τ, as κ^(−α) → 0 and λκ^(1−α) = T0 κ^(−α)
→ 0. If |A_s + B_s| ≥ τ on J, then |σ| ≥ τ/2, and arg σ moves by at most 8πλ C(λ^(1/2) + λκ^α)/τ ≤ C′(λ^(1/2) κ^(1−α) +
T0)/δ_* ≤ C′(λ^(α−1/2) + T0)/δ_* → 0, using κ ≤ 1/λ and α > 1/2: [[lem:edge-two-signs]] (A). Otherwise |A_s + B_s| ≤ 2τ
on J, and with B_s′ = −B_s(κ − κ_(N−1))(1 + O(T0 + κ^(−α))) ([[prop:l-26]] (2)),

    σ′ = [ν′ + A_s(κ − κ_(N−1))] − (A_s + B_s)(κ − κ_(N−1)) + O(λκ^α (T0 + κ^(−α))) + ν′(st − 1) + ν st′ + λa₁′ + ê′.

Since ν′ ≤ 0 and κ − κ_(N−1) ≥ c_t κ^α > 0 by (H_t), and |s + cz| ≥ c dist(z, [0, ∞)) for real s ≤ 0 and c > 0, |ν′ +
A_s(κ − κ_(N−1))| ≥ (κ − κ_(N−1)) dist(A_s, [0, ∞)) ≥ c_t δ_* λ κ^α/2. The rest is at most C(τκ^α + λκ^α(T0 + κ^(−α)) +
λ^(1/2) T0 + M′λ T0 κ^α + λ(1 + T0κ^α) + (1 + T0)Mλ), which is much smaller than λκ^α (for instance λ^(1/2) T0/(λκ^α) =
λ^(1/2) κ^(1−α) ≤ λ^(α−1/2) → 0, as κ ≤ 1/λ). So |σ′| ≥ c_t δ_* λ κ^α/3, while |σ″| ≤ C(1 + λκ^(1+α)) ≤ 2Cλκ^(1+α) by
step (2) of [[prop:l-26]] with |ν″| ≤ 3c_ν, and |σ′| ≤ C(λ^(1/2) + λκ^α). [[lem:edge-two-signs]] (B) applies as in step
(4) of [[prop:l-26]], with L0 := λ³ A |d| env c_t δ_* λ κ^α/5: |κσ| ≤ 2κτ = c_t δ_* λκ^α/8; |S″| ≤ L0/(80πλ) once T0 ≤
c(δ_*, c_t), the terms of S″ (2κ|σ′| ≤ Cκ(λ^(1/2) + λκ^α), κ²|σ| ≤ 2κ²τ, |σ″|) being small against κ^α times λ³A|d|env
δ_*; and |ε| ≤ πλL0/5 once env ≤ λ^(P1). ∎

The phase of b̂4 decides this case: nothing in step (2) uses N modulo 4 or c_N, the transversality being (H_t), and the
direction of A_s is held away from [0, ∞) by b̂4. b̂5 is not used. If b̂4 were a positive real number of small modulus,
with N ≡ 2 modulo 4, the real parts of ν′ + A_s(κ − κ_(N−1)) could cancel and λ T0′ b̂5 the rest, and the argument
would not decide such windows.

**Remark {#rem:edge-crossover-numbers}** (Numerical observation.) The crossover was modelled with unit constants (N = 12,
c_N = 6/5, ν = −1/9, Γ_R = 1, exact derivatives of exp(−1/x) and of env_C): over the whole crossover 1/4 ≤ |S_U|/|S_st| ≤
4 the least ratio of |σ_main| to the error bound of Case 3 below was 11.7, 95.3, 6.27·10³ and 2.71·10⁷ at λ = 10⁻¹⁰,
10⁻²⁰, 10⁻⁴⁰ and 10⁻⁸⁰, and arg σ_main moved by at most 0.009 over 4πλ. At c_N = 1/2 (ρ0² = 23, N = 12), with ρ_g of
[[eq:edge-rho-sharp]] in Ξ_ex, every window of the crossover was decided at λ = 10⁻⁴⁰ and 10⁻⁸⁰, by (A) on a logarithmic
grid and by (B) on the windows around the minimum of |σ|, which was below 1.8·10⁻¹³ |ν| T0². At ρ*, with exp(−1/x^(1/2))
(κx² → 0) and N = 9, …, 13 at λ = 10⁻⁴⁰, with b̂4 of [[lem:edge-next-family]] and b̂5 = 3b̂4 (a relation found by
computation and not proved here), every one of the 122 windows of each run was decided, while adversarial values (|b̂4| =
0.0033, |b̂5| = 1.0·10⁻⁴, chosen so that σ and σ′ vanish together) left a window undecided. No proof uses these figures.

### The very edge for the metric of the main theorem {#sec:edge-theorem}

**Theorem {#thm:very-edge}** (The very edge.) Let μ0 = √72 l5², K ≥ 6, N = K + 3, and let g_λ be the metric of
[[thm:main]], as in [[thm:layer]]. Let τ0 be admissible, ρ0 := (v_s − τ0)/√μ0, and let env satisfy (H_N), (H_D) and
(B_(c′)), c′ := max(c, M*) with c the cost of [[lem:edge-degree-two]], on (v_s, v_s + x0] for some x0 > 0, and
moreover

    if N ≡ 0 mod 4 and ρ0² = 2N − 1:   (H_N+2) and (H_t);
    if ρ0 = ρ*:                         (H_N+2) and (H_t), except when N ≢ 0 mod 4 and (H_*) holds.

Then there are λ_1E > 0, x0′ ∈ (0, x0] and P1 such that for λ ≤ λ_1E, every v ∈ (v_s, v_s + x0′] with env(v + 4πλ) ≤
λ^(P1) and every x̂ ∈ S³, the boundary {x_K = 1} has, on [v, v + 4πλ] and at x̂, points where it is timelike for g_λ
and points where it is spacelike. This holds in particular for every v ∈ (v_s, v_s + x0′] with λκ(v + 4πλ) ≥ 1, down
to v_s. If env is increasing on (v_s, v_s + x0], then, with [[prop:layer-regions]] (ii) at P := P1 + 1, for λ ≤
min(λ_U(P1 + 1), λ_1E) the same holds on every interval [v, v + 4πλ] with v_s < v ≤ v_s + x0′ and env(v) ≤ λ^(3+δ).

When ρ0 = ρ* and (H_*) fails, the proof uses [[lem:edge-rho-star]], and with it the value of b̂4 of
[[lem:edge-next-family]].

*Proof.* Take x0′ so small that [[prop:edge-horizon-value]], [[lem:edge-localisation]], [[lem:edge-kappa]] (c) for j ≤ c′
and the conclusions of [[lem:edge-kappa]] (a), (b), (e) used below hold on (v_s, v_s + x0′], and λ_1E ≤ λ_D, x0′ ≤ x_D
for [[lem:edge-localisation]]. Fix x̂ and let J := [v, v + 4πλ]. At a boundary point X = (v′, r_q(v′), x̂), v′ ∈ J,
[[lem:layer-inverse]] with k = h^(1) + r2 − (g0 − g0°) gives

    g_λ⁻¹(dΦ0, dΦ0) = −Re[S(v′) e^(iv′/λ)] + ε(v′),

where S is that of [[prop:edge-horizon-value]] and ε(v′) := −m0 − r2(Φ0♯, Φ0♯) + (g0 − g0°)(Φ0♯, Φ0♯) + q − [h^(1)(Φ0♯,
Φ0♯) − h^(1)_vv(v′, √μ0)]. The last bracket is the shift from √μ0 to r_q, at most C ε_0² |∂_r h^(1)|, plus the β_Φ-terms,
at most C ε_0² |h^(1)|, with β_Φ and r_q − √μ0 at most C ε_0² ([[cor:layer-expansion]]) and |h^(1)| + |∂h^(1)| ≤ C ε_c.
So |ε| ≤ C κ^(2c′) env², by [[lem:edge-localisation]], [[eq:edge-degree-two]], m0 ≤ C(env² + ∫_(v_s)^(v′) env²) ≤ C env²
([[cor:layer-expansion]], [[lem:edge-kappa]] (d)) and κ^p env → 0 ([[lem:edge-kappa]] (e)). The hypothesis of
[[lem:edge-localisation]] holds since env(v′ + 1/κ(v′)) ≤ e env(v′) ≤ e λ^(P1).

Use σ, Λ, ê of [[eq:edge-sigma]], so that f := g_λ⁻¹(dΦ0, dΦ0) = Re[−S e^(i·/λ)] + ε, to which [[lem:edge-two-signs]]
applies as to S. Fix M ≥ max(8, M_26), large against the constants, and split by the values at v: Case 1 is Γ_R|Ξ|Λ ≥
M|ν||1 + 2iT0| or T0 > 1, Case 2 is Γ_R|Ξ|Λ ≤ |ν|/M, and Case 3 is the rest. These conditions persist on J with M
replaced by M/C_0, for a constant C_0, which we absorb into M. Indeed, if λκ(v)^α > 1, then for t ∈ J, κ(t)^(−α) ≤
κ(v)^(−α) + α c_R 4πλ ≤ (1 + 4πα c_R)λ, so λκ(t) ≥ c λ^(1−1/α) > 1 for λ small: Case 1 on all of J. Otherwise 4πλ ≤
4πκ(v)^(−α); κ is nonincreasing and κ(t)^(−α) ≤ (1 + 4πα c_R) κ(v)^(−α) on J, so κ, T0 and T change over J by bounded
factors, and so do |1 + 2iT0| and |Ξ|; log Λ changes by at most 4πλ C κ(v)^α ≤ C, as Λ′/Λ = κ_(N−1) − κ; and x changes by
a factor at most 1 + 4πα c_R (κ^(−α) ≤ α c_R x), so ν by a bounded factor.

*Case 1.* |σ| ≥ (1 − 1/M) Γ_R|Ξ|Λ − |ê| ≥ Γ_R|Ξ|Λ/2 for λ and x0′ small. Indeed ϵ′ + 1/κ + λ → 0, as ϵ′ ≤ κ^(α−1) for
every λ. Where T0 ≤ 1, |ν| T0² ≤ |ν| ≤ Γ_R|Ξ|Λ/M, and λ ≪ Λ: off ρ*, Λ ≥ M ν_*/(Γ_R|Ξ|); at ρ*, if x² < Mλ then κ ≥
c_*/(Mλ) by (H_*), T0 ≥ c_*/M and Λ ≥ 2^(−(N−1)) T0^(N−2) κ ≫ λ, and if x² ≥ Mλ then Λ ≥ M|ν|/(Γ_R|Ξ|) ≥ c M x² ≥ c M² λ.
Where T0 > 1, the term Λ/κ of ê is small against Γ_R|Ξ|Λ: by [[eq:edge-xi]], |Ξ| ≥ c_N (1 + T²)^(−1/2), so Γ_R|Ξ|Λ/(Λ/κ)
≥ Γ_R c_N κ (1 + T²)^(−1/2) ≥ Γ_R c_N/(2√2 λ) for T ≥ 1, also where c_N = 1 and Ξ = −i/(T + i); the other terms of ê are
relative to |Ξ| by [[lem:edge-constraint]]. The phase: arg(−Γ_R i^N Ξ Λ) = const + arg Ξ, and Im Ξ = −T/(1 + T²) < 0, so
a continuous determination of arg Ξ varies over J by less than π (c_N varies with r0, and at ρ0² = N − 1 this variation
need not be small on windows deep in the edge); the rest moves arg σ by at most 2 arcsin(2/M) < π/2, so arg σ varies by
less than 3π/2. The pointwise ratio |ε|/|S| ≤ C κ^(2c′) env/(λ³ Γ_R|Ξ|Λ) is small: where T0 ≤ 1, Γ_R|Ξ|Λ ≥ cλ and the
ratio is at most C λ^(−2c′−4) env, small once env ≤ λ^(P1); where T0 > 1, |Ξ|Λ ≥ c κ/T ≥ c/λ and the ratio is at most C
κ^(2c′+2) env, small for x0′ small by [[lem:edge-kappa]] (e). [[lem:edge-two-signs]] (A).

*Case 2.* Λ ≥ 2^(−(N−1)) T0^(N−2) κ and Λ ≤ C|ν| ≤ C, with κ → ∞, so T0 → 0. |σ| ≥ |ν|(1 − 1/M) − |ê| ≥ |ν|/2,
since λ ≪ |ν|: off ρ* because |ν| ≥ ν_*; at ρ* because x² ≥ Mλ (otherwise, as in Case 1, Λ ≫ λ ≥ x²/M ≥ c|ν|/M,
against Case 2), so |ν| ≥ c_ν M λ/2. The phase: arg σ stays within 2 arcsin(2/M) + o(1) of arg(ν(1 + 2iT0)), which
moves over J by O(λ²|κ′|) = O(λ^(1−α) T0^(1+α)). [[lem:edge-two-signs]] (A), with ε ≤ |S|/4 once env ≤ λ^(P1) (κ ≤ 1/λ
here).

*Case 3.* Here Λ ≍ |ν|, so κ ≍ (|ν| λ^(−(N−2)))^(1/(N−1)), T0 → 0 and λκ² → ∞: off ρ*, λκ² ≍ λ^(−(N−3)/(N−1)); at
ρ*, T0^(N−2) κ ≍ |ν| ≥ c x² ≥ c c_*/κ gives T0 κ ≥ c κ^(1−2/(N−2)) → ∞. With −Ξ = c_N + iT + O(T²),

    σ_main := ν(1 + 2iT0) + Γ_R i^N (c_N + iT) Λ,      σ = σ_main + O(|ν| T0²) + ê.

(i) N ≢ 0 mod 4. If N is odd, Γ_R i^N c_N Λ is imaginary and Re σ_main = ν(1 + O(T0)); if N ≡ 2 mod 4, Re σ_main = ν −
Γ_R c_N Λ, of modulus at least |ν|. So |σ_main| ≥ |ν|/2, and |ê| ≤ C|ν|(T0² + λ/|ν| + M(ϵ′ + 1/κ + λ)) ≪ |ν|, λ ≪ |ν| at
ρ* as in Case 2. The real and imaginary parts of σ move over J by O(|ν| λ(κ^α + |ν′/ν|) + |ν| λ² κ^(1+α)), which is
o(|ν|) (λ/x ≤ (λ/M)^(1/2) at ρ*). [[lem:edge-two-signs]] (A).

(ii) N ≡ 0 mod 4, ρ0² ≠ 2N − 1 and ρ0 ≠ ρ*. With X_c := Γ_R c_N Λ/|ν| and ν < 0, Re σ_main = |ν|(X_c − 1) and Im σ_main =
2νT0 + Γ_R T Λ = |ν| T0 (X_c/c_N − 2) + O(|ν| T0 κ^(α−1)). Put η_c := |1 − 2c_N|/4, positive near the edge as c_N(ρ0) ≠
1/2. If |X_c − 1| ≥ η_c, |σ_main| ≥ |ν| η_c; if |X_c − 1| < η_c, then |X_c/c_N − 2| ≥ |1/c_N − 2| − η_c/c_N = (3/4)|1 −
2c_N|/c_N, so |Im σ_main| ≥ |ν| T0 |1 − 2c_N|/(2c_N). Either way |σ_main| ≥ c₃ |ν| T0, c₃ := min(η_c, |1 − 2c_N|/(2c_N)).
And |ê| + O(|ν| T0²) ≤ C|ν|[T0² + λ/|ν| + M(T0² + T0 κ^(α−1) + 1/κ + λ)] ≤ c₃ |ν| T0/2 for λ small: T0² ≪ T0; λκ^α = T0
κ^(α−1) ≪ T0 for every α < 1, which bounds the part λκ^α of ϵ′; 1/κ ≪ T0, as λκ² → ∞; λ ≪ T0; and λ/|ν| ≪ T0, as |ν| ≥
ν_*. Over J, Re σ_main moves by O(|ν| λ(κ^α + |ν′/ν|)), Im σ_main by O(|ν| λ² κ^(1+α)), and ê by O(λκ)|ê|, by
[[eq:edge-s]]; against |σ| ≥ c₃ |ν| T0/2 these are O(κ^(α−1) + 1/κ + λκ^α) → 0. [[lem:edge-two-signs]] (A) applies,
as |S| ≥ c₃ |ν| T0 λ³ A |d| env/2 and |ε| ≤ C κ^(2c′) env² ≤ |S|/4 once env ≤ λ^(P1) (κ ≤ 1/λ here).

(iii) N ≡ 0 mod 4, and ρ0² = 2N − 1 or ρ0 = ρ* (with (H_*)): the windows of Case 3 are those of [[prop:l-26]], whose
hypotheses, (H_N+2), (H_t) and at ρ* (H_*), are those of the theorem in these cases.

*ρ0 = ρ* without (H_*).* Every window is decided by [[lem:edge-rho-star]].

*The very edge.* If λκ(v + 4πλ) ≥ 1, then by [[lem:edge-kappa]] (e), env(v + 4πλ) ≤ κ(v + 4πλ)^(−P1−1) ≤ λ^(P1+1) ≤
λ^(P1) once x0′ is small.

*The levels.* Let env be increasing and env(v) ≤ λ^(3+δ). Every point is a first-reach point, and points with env(v) ≤
λ^(3+δ) near v_s lie in the layer (as in the proof of [[thm:layer]]). If env(v) ≥ λ^(P1+1), [[prop:layer-regions]] (ii)
applies. If env(v) < λ^(P1+1) and λκ(v) ≤ 1, then env(v + 4πλ) ≤ e^(4πλκ(v)) env(v) ≤ e^(4π) λ^(P1+1) ≤ λ^(P1). If
λκ(v) > 1, then 4πλ ≤ 4πκ(v)^(−1) ≤ κ(v)^(−α)/(α c_R) near v_s, so κ ≥ 2^(−1/α) κ(v) on J by [[lem:edge-kappa]] (b),
and env(v + 4πλ) ≤ κ(v + 4πλ)^(−P1−1) ≤ (2^(−1/α)/λ)^(−P1−1) ≤ λ^(P1) for λ small. In the last two cases the first part
applies. ∎

For the envelope env_C every hypothesis holds, for every K ≥ 6 and every admissible τ0, by [[cor:edge-envelope]] below;
and env_C satisfies (H_*), so [[lem:edge-next-family]] is not used for it.

**Remark {#rem:edge-carried}** (What carries the first-degree term.) Once Λ ≫ |ν|, the first-degree amplitude S is
carried by S_U, that is by the constraint correction U^(1) of the data at first degree, and not by the approximant's
profiles: on the very edge of the metric of [[thm:main]] the causal character of the boundary is decided by the solution
of the constraint equations of [[sec:data-evolution]] at first degree. At ρ0² = N − 1, where c_N = 1 at the edge, Ξ = (1
− c_N(r0)) − i/(T + i) with 1 − c_N(r0) of order x, and |S_U| can fall like 1/T; the argument still closes, because the
errors of [[lem:edge-constraint]] are relative to the bracket there and Im Ξ = −T/(1 + T²) < 0.

**Remark {#rem:edge-very-edge-numbers}** (Numerical observation.) The two-term formula S_st + S_U was run with unit
constants (exp(−1/x), λ = 10⁻⁶, r0 = 3, ν = −1/9), with the cut-off of S_st at λκ > 1, for N = 9, where the two
amplitudes are in quadrature, and N = 12, where their real parts cancel at the crossover, over 1200 windows each from
env = λ⁴ to x = 0.2 λ^(1/2): every window had both signs, while with S_U removed some windows had one sign only. No
proof uses this observation.

### The hypotheses for the envelope env_C {#sec:edge-envelope}

This section proves every hypothesis of [[def:edge-hypotheses]] that [[thm:very-edge]], [[prop:l-26]] and
[[thm:edge-past]] place on the envelope, for every K ≥ 6 and every order J, for the envelope env_C of [[eq:envelope]]
([[lem:envelope-constant]]),

    env(v) = c_e cos¹²(πξ/2) exp(−ξ²/(1 − ξ²)),   ξ := (2v − 4)/3,   for 1/2 < v < 7/2,              {#eq:edge-envelope}

env = 0 elsewhere, with c_e the constant of [[eq:envelope]] (its value is not used below) and v_s = 1/2, and for the
model edge env(v) = exp(−1/(v − v_s)) for v > v_s. We write x := v − v_s and κ := (log env)′ (a prime is d/dv = d/dx),
and where env^(k) > 0, κ_k := (log env^(k))′ = env^(k+1)/env^(k), so κ_0 = κ. All of them reduce to one recursion for
x²κ_k, controlled on complex discs.

**Lemma {#lem:edge-logderivatives}** (The logarithmic derivatives.) Let env be smooth and positive on an interval
I ⊂ (v_s, ∞), put R_0 := x²κ, and as long as R_k has no zero on I put

    R_(k+1) := R_k − 2x + x² R_k′/R_k.                                                              {#eq:edge-recursion}

Suppose R_0, …, R_m are positive on I. Then on I: (a) env^(k) = env x^(−2k) R_0 R_1 ⋯ R_(k−1) > 0 for k ≤ m + 1, and
κ_k = R_k/x² for k ≤ m; (b) κ_k/κ = R_k/R_0 for k ≤ m, and env^(j)/(κ^j env) = Π_(i<j) R_i/R_0 for j ≤ m + 1; (c) for k ≤
m − 1, κ_k′ = R_k (R_(k+1) − R_k)/x⁴; so env^(k) is strictly log-concave where R_(k+1) < R_k, and there |κ_k′| ≤ c
κ_k^(3/2) exactly where R_k − R_(k+1) ≤ c x R_k^(1/2); (d) κ′ = −(2R_0 − xR_0′)/x³, so |κ′|/κ^(3/2) = |2R_0 −
xR_0′|/R_0^(3/2), and κ′ < 0 where 2R_0 − xR_0′ > 0; (e) if 1 ≤ n ≤ m − 1 and env^(k) is strictly log-concave for every k
≤ n − 1, then κ − κ_n ≥ κ − κ_1 = |κ′|/κ.

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

**Lemma {#lem:edge-a}** (The function x²κ.) For exp(−1/x), R_0 = x²κ = 1. For [[eq:edge-envelope]], on 0 < x < 3,

    R_0(x) = x²κ = 3/4 − (3/4)(x/(3 − x))² + 4πx² cot(πx/3),                                       {#eq:edge-a}

and R_0 extends holomorphically to the disc |z| < 3. With ê_0(r) := (3/4)(r/(3 − r))² + (4π²/9) r³/(1 − r²/9), for
complex z with |z| ≤ r ≤ 1/100,

    |R_0(z) − 3/4 − 12z| ≤ ê_0(r) ≤ r²/7,      |R_0′(z) − 12| ≤ ê_0′(r) ≤ r/2,                       {#eq:edge-a-disc}

and for real 0 < x ≤ 1/100,

    3/4 + 12x − x²/7 ≤ R_0(x) ≤ 3/4 + 12x,      12 − x/2 ≤ R_0′(x) ≤ 12.                          {#eq:edge-a-real}

*Proof.* Put t := 2x/3 = 1 + ξ. Then cos(πξ/2) = sin(πt/2) = sin(πx/3), and ξ²/(1 − ξ²) = 1/(t(2 − t)) − 1, since
t(2 − t) + (1 − t)² = 1; moreover 1/(t(2 − t)) = (1/2)(1/t + 1/(2 − t)) = (3/4)(1/x + 1/(3 − x)). So for 0 < x < 3

    log env = log c_e + 1 + 12 log sin(πx/3) − (3/4)(1/x + 1/(3 − x)),                               {#eq:edge-log}

and κ = 4π cot(πx/3) + (3/4)(1/x² − 1/(3 − x)²), which is [[eq:edge-a]] after multiplication by x². For exp(−1/x),
κ = 1/x². Put w := πz/3 and e_0(z) := 3/4 + 12z − R_0(z) = (3/4)(z/(3 − z))² + 4πz²(1/w − cot w), using 12z = 4πz²/w.
For |w| < π the partial fractions of the cotangent give

    1/w − cot w = Σ_(j≥1) 2w/(j²π² − w²) = Σ_(n≥1) (2ζ(2n)/π^(2n)) w^(2n−1),

so R_0 is holomorphic on |z| < 3, and every Taylor coefficient of e_0 at 0 is nonnegative, (z/(3 − z))² being
Σ_(m≥2) (m − 1) z^m/3^m. Since 2ζ(2n) ≤ 2ζ(2) = π²/3, the coefficients of 1/w − cot w are at most those of
Σ_(n≥1) (π²/3) w^(2n−1)/π^(2n) = (w/3)/(1 − w²/π²); with w = πz/3, those of 4πz²(1/w − cot w) are at most those of
(4π²/9) z³/(1 − z²/9). So the Taylor coefficients of e_0 lie between 0 and those of ê_0. Hence |e_0(z)| ≤ ê_0(|z|)
and |e_0′(z)| ≤ ê_0′(|z|) for |z| < 3, and 0 ≤ e_0(x) ≤ ê_0(x), 0 ≤ e_0′(x) ≤ ê_0′(x) for 0 < x < 3. It remains to
bound ê_0 and ê_0′ for r ≤ 1/100. There (3 − r)² ≥ 8.94, (3 − r)³ ≥ 26.7, 1 − r²/9 ≥ 0.9999, and π² ≤ 10, so 4π²/9 ≤
4.45 and

    ê_0(r) ≤ (0.75/8.94) r² + (4.45/0.9999) r³ ≤ 0.0839 r² + 0.0446 r² < r²/7,
    ê_0′(r) = (9/2) r/(3 − r)³ + (4π²/9)(3r² − r⁴/9)/(1 − r²/9)² ≤ 0.1686 r + 13.4 r² ≤ 0.303 r < r/2.  ∎

**Lemma {#lem:edge-disc}** (The recursion on a disc.) Let a ∈ [3/4, 1], 0 ≤ c_d ≤ 13 and n ≥ 1 an integer, and put
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

Here 8(n + 2)ϱ ℬ_k/(3a) = ℬ_k/(9a(n + 2)) = 2k(c_d + k)/(9a²(n + 2)) ≤ (8/27)(c_d + k)/a, since k < n + 2 and 1/a ≤ 4/3.
So |𝒯_(k+1)| ≤ ℬ_k + (44/27)(c_d + 2k)/a ≤ ℬ_k + 2(c_d + 2k + 1)/a = ℬ_(k+1). Finally, on 𝔻_(k+1), |R_(k+1)| ≥ |R_0| −
2(k + 1)ϱ − ℬ_(k+1) ϱ², and since k + 1 ≤ n + 1, a ≥ 3/4 and c_d ≤ 13,

    2(k + 1)ϱ ≤ (n + 1)/(12(n + 2)²) ≤ 1/36,      ℬ_(k+1) ϱ² ≤ (n + 1)(n + 14)/(216(n + 2)⁴) ≤ 15/(216 · 27) < 1/388,

so |R_(k+1)| ≥ 7a/8 − 1/36 − 1/388 > 7a/8 − 0.031 ≥ 7a/8 − a/8 = 3a/4, as a/8 ≥ 3/32 > 0.031. ∎

### The hypotheses, for every order {#sec:edge-envelope-every-k}

**Proposition {#prop:edge-envelope}** (The hypotheses for the envelope env_C.) Let env be [[eq:edge-envelope]], or
exp(−1/(v − v_s)); let n ≥ 1 be an integer and x_n := 1/(96(n + 2)²). Then: (a) on (v_s, v_s + x_n], env^(k) > 0 for k ≤
n + 2, and |env^(j)| ≤ κ^j env for j ≤ n + 2; (b) on (v_s, v_s + x_n], for every k ≤ n, env^(k) is strictly log-concave,
99/100 ≤ κ_k/κ ≤ 1 and |κ_k′| ≤ c_R κ_k^(3/2), with c_R = 12/5 for [[eq:edge-envelope]] and c_R = 21/10 for exp(−1/(v −
v_s)); (c) on (v_s, v_s + 1/200], |κ′| ≥ c_t κ^(3/2) with c_t = 2.13951, resp. c_t = 2, and 3/4 ≤ κx² ≤ 81/100, resp.
κx² = 1; (d) (H_D) holds for every c > 0.

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

**Corollary {#cor:edge-envelope}** (Every hypothesis, for every order.) Let env be [[eq:edge-envelope]] or exp(−1/(v −
v_s)), N ≥ 2, J ≥ N + 4, and x0 := x_(J−2) = 1/(96 J²). On (v_s, v_s + x0], (H_N) and (H_N+2) hold with α = 1/2, the
c_R of [[prop:edge-envelope]] and c_j = 1; (B_J) holds with c_j = 1; for v_s < v′ ≤ v ≤ v_s + x0 and j ≤ J

    κ(v′)^j env(v′) ≤ κ(v)^j env(v) e^(−κ(v)(v − v′)/2);                                           {#eq:edge-decay}

(H_t) holds with c_t = 2.13951, resp. 2; (H_*) holds with c_* = 3/4, resp. 1; and (H_D) holds. So every hypothesis that
[[thm:very-edge]], [[prop:l-26]] and [[thm:edge-past]] place on the envelope holds for these two envelopes, for every K
≥ 6 (N = K + 3), with J the largest order those results use.

*Proof.* [[prop:edge-envelope]] with n = J − 2 ≥ N + 2: (a) and (b) give, for k ≤ N + 2, env^(k) > 0, strictly
log-concave, κ_k/κ ∈ [99/100, 1] ⊂ [1/2, 2] and |κ_k′| ≤ c_R κ_k^(1+1/2), and for j ≤ J, |env^(j)| ≤ κ^j env; this is
(H_N+2), which contains (H_N), and (B_J). For [[eq:edge-decay]]: as x0 ≤ 1/200, (c) gives κx² ≥ 3/4, resp. κx² = 1, on
(v_s, v_s + x0], so κ^(−1/2) ≤ 2x0/√3 there; κ′ < 0 there since env is strictly log-concave; and, as c_R ≤ 12/5,
j c_R κ^(−1/2) ≤ J (12/5)(2/√3) x0 = √3/(60 J) < 1/2. Hence (log(κ^j env))′ = κ + jκ′/κ ≥ κ − j c_R κ^(1/2) ≥ κ/2 ≥
κ(v)/2 on [v′, v], and integrating over [v′, v] gives [[eq:edge-decay]]. (c) also gives c_t and c_*. By
[[lem:edge-logderivatives]] (e) with n = N − 1, which uses the strict log-concavity of env^(k) for k ≤ N − 2,
κ − κ_(N−1) ≥ |κ′|/κ ≥ c_t κ^(1/2): this is (H_t) with α = 1/2. (H_D) is (d). ∎

The hypotheses are thus proved on (v_s, v_s + 1/(96 J²)], an interval that shrinks as N and J grow; [[thm:very-edge]],
[[prop:l-26]] and [[thm:edge-past]] take their interval (v_s, v_s + x0] as given and use the hypotheses only on
subintervals (v_s, v_s + x0′] with x0′ ≤ x0, so this interval is all they need.

**Remark {#rem:edge-envelope-limits}** (The constants at the edge.) By [[eq:edge-disc]], as x ↓ 0, R_k → R_0(0),
x R_k′ → 0 and (R_k − R_(k+1))/(x R_k^(1/2)) → 2R_0(0)^(−1/2); so κ_k/κ → 1 and env^(j)/(κ^j env) → 1. Hence, as
x0 ↓ 0, the best constants c on (v_s, v_s + x0] in |κ_k′| ≤ c κ_k^(3/2) and in |κ′| ≥ c κ^(3/2) tend to
2R_0(0)^(−1/2), which is 4/√3 = 2.309… for [[eq:edge-envelope]] and 2 for exp(−1/x); in (H_t) with α = 1/2 the best
constant tends to 2(N − 1)R_0(0)^(−1/2), since κ − κ_(N−1) = Σ_(k<N−1) (R_k − R_(k+1))/x² with each term ~ 2/x and
κ^(1/2) = R_0^(1/2)/x. The values 12/5 and 21/10 of c_R exceed these limits by 3.9 % and 5 %. The value 2.13951 of
the constant in |κ′| ≥ c κ^(3/2) is 7.4 % below its limit 4/√3, because it holds on all of (v_s, v_s + 1/200]: the
lower bound h in the proof of [[prop:edge-envelope]] (c) decreases from h(0) = 4/√3 to h(1/200) = 2.13990….

**Remark {#rem:edge-scaled}** (The edges exp(−a/x).) Let a > 0 and env(v) = exp(−a/(v − v_s)) for v > v_s. As a function
of x̃ := x/a, env is exp(−1/x̃), and d/dx = a⁻¹ d/dx̃; so κ_k = a⁻¹ κ̃_k, where κ̃_k are the logarithmic derivatives of
exp(−1/x̃) in x̃. Hence κ_k/κ, env^(j)/(κ^j env) and κ(v)(v − v′) are those of exp(−1/x̃) at x̃ = x/a, |κ_k′|/κ_k^(3/2)
and |κ′|/κ^(3/2) are those multiplied by a^(−1/2), and κx² = a. So [[cor:edge-envelope]] holds for this envelope on (v_s,
v_s + a x0], with c_R = (21/10)a^(−1/2), c_j = 1, c_t = 2a^(−1/2) and c_* = a, (H_D) included.

**Remark {#rem:edge-sin4}** (An envelope outside the class.) The envelope sin⁴(π(v − v_s)/3) for v ≥ v_s, 0 for
v < v_s, is C³ and not C⁴ at v_s: near v_s it is (πx/3)⁴(1 + O(x²)), so env^(4)(v_s+) = 4!(π/3)⁴ = 8π⁴/27, while
env^(4) = 0 for v < v_s. So it lies outside the class of [[thm:main]]. It also satisfies no (H_N) with N ≥ 3, since
κ = 4/x + O(x) and κ_3 = env^(4)/env^(3) = 1/x + O(x) give κ_3/κ → 1/4 < 1/2.

### One switch per column {#sec:edge-switch}

In the band λ^(3+δ) ≤ E ≤ λ^(3−δ) of [[prop:layer-regions]] (iii) the ratio R decides the boundary's character up to
the factor 1 ± 2λ^γ, γ = 1/10. For an envelope increasing at its edge, the ratio crosses 1 once per column, and the
boundary switches once.

**Theorem {#thm:l-24}** (One switch per column.) Let K ≥ 6, N = K + 3, δ ∈ (0, 1/2], γ = 1/10, and let g_λ be the metric
of [[thm:main]]. Let env be increasing on (v_s, v_s + x0] and satisfy (H_N) there. There is λ_24 > 0 such that for λ ≤
λ_24 and every x̂ ∈ S³ the following holds. Divide the band λ^(3+δ) ≤ E ≤ λ^(3−δ) into consecutive carrier periods I_k
of length 2πλ, starting at its left end, and put M_k := max_(I_k) g_λ⁻¹(dΦ0, dΦ0) at x̂. Then M_k > 0 for every period
whose midpoint has R ≥ 1 + 2λ^γ, M_k < 0 for every period on which R ≤ 1 − 2λ^γ, and M_(k+1) < M_k for every two
consecutive periods one of which meets {|R − 1| ≤ 2λ^γ}; periods of the first kind exist and precede all others, and
periods of the second kind exist and follow all others. So the sequence (M_k) changes sign exactly once: before the
switch every carrier period has points where the boundary is timelike at x̂, and after it the boundary is spacelike
throughout every period at x̂.

The proof is given at the end of [[sec:l-24-margin]], where the margin and the first-degree amplitude are compared. It
also uses a bound for the remainder beyond the first degree.

**Lemma {#lem:edge-w-minus-e}** (The remainder beyond the first degree.) Let v1 ≤ v_♯ with ε_4(v1) ≤ λ, and let R be the
region of [[lem:layer-remainder]]. At every boundary point X ∈ R, with a fixed cost c,

    |(w − e)(X)| ≤ C (λ^(N−6) ε_c(v1)² + λ^(N−2) ε_c(v1)),                                         {#eq:edge-w-minus-e}

where w = g_λ − g_app and e = h^(1) − h_app^(1).

*Proof.* By [[eq:layer-w-equation]] and [[eq:edge-e-equation]], w − e solves −(1/2) g_λ^(ab) ∂_a ∂_b (w − e) = f′, the
operator of [[eq:layer-w-equation]] being written around the seed, where f′ is the sum of four parts. (i) The part of
degree at least two of Ric^H(g_app), at most C λ^(N−1) ε_c² with each derivative costing λ⁻¹, by (F2) of
[[sec:layer-flat]] and the argument of [[lem:layer-flat]] (d). (ii) The part of first degree of Ric^H(g_app) minus that
of [[eq:edge-e-equation]]: as g_app stops at λ^N, the part of first degree of Ric^H(g_app) is λ^N Re[R_X(H_N) e^(iv/λ)]
as in the proof of [[lem:edge-constraint]] (i), so this part is λ^N Re[(R_X H_N + λ R_X H_(N+1)) e^(iv/λ)], at most C λ^N
ε_c. (iii) The differences between the coefficients of [[eq:layer-w-equation]] and those of dRic^H, which are of degree
at least one, acting on w and on e: the coefficient of a derivative of order q is at most C λ^(q−1) ε, each of its
derivatives costing λ⁻¹, and the order q = 2 occurs only on e, the operator on the left being that of w. (iv) The terms
quadratic in w, smaller still.

Step 6 of the proof of [[lem:layer-remainder]] needs Σ_(i≤2) ‖∂^i f′‖ on the slices. Put ε := ε_c(v1), c ≥ M*. By the
graded energies of the proof of [[lem:layer-remainder-weak]], E^(i) ≤ C λ^(N−3−i) ε, so ‖∂^p w‖ ≤ C λ^(N−3) ε for p ≤ 1
and ‖∂^p w‖ ≤ C λ^(N−2−p) ε for 1 ≤ p ≤ 3. The same bounds hold for e, and for e also at p = 4: e solves an equation with
the seed's coefficients, its data, those induced by U^(1), are of size λ^(N−2−j) ε with j derivatives, and its forcing
term is of size λ^(N+1) ε, each derivative costing λ⁻¹. A term of ∂^i of (iii), i ≤ 2, is a derivative of order m of a
coefficient of order q times ∂^(q+i−m) u, u = w or e, so it is at most C λ^(q−1−m) ε ‖∂^(q+i−m) u‖: at most C λ^(N−3−i)
ε² if q + i − m ≥ 1, and at most C λ^(N−4−i) ε² if q + i − m = 0. So Σ_(i≤2) ‖∂^i f′‖ ≤ C (λ^(N−6) ε² + λ^(N−2) ε): from
(iii) the largest term is ∂²(coefficient) · w, at most λ^(−3) ε · λ^(N−3) ε; (i) gives λ^(N−3) ε² and (ii) λ^(N−2) ε. The
data of w − e on Σ_τ0 are those induced by U − U^(1), at most C λ^(N−2−j) ε² with j derivatives
([[lem:edge-u-difference]]), and those of G(X, u/λ) − g_app, which is λ^(N+1) times profiles with an oscillating factor
([[sec:data-proof]]); they contribute C λ^(N−5) ε² + C λ^(N−2) ε to E_2(τ0). Steps 1, 5, 6 and 7 of the proof of
[[lem:layer-remainder]], with these forcing terms and data, then give [[eq:edge-w-minus-e]]. ∎

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

*Setting.* As in [[ch:equality-layer]], μ0 > 0 is the seed's mass, A > 0 the amplitude of the waves and v_s := inf supp
env; no sign of the envelope env is assumed, and in the results below it is positive on an interval (v_s, v_s + x0]. The
margin of the boundary {r = r_q} at equality is

    μ(v) := μ0 + (2/9) A² ∫_(v_s)^v env²,    r_q := (μ0 μ)^(1/4),    m0 := √(μ/μ0) − 1 + r_q μ′/(2μ),  {#eq:l-24-margin}

so that μ′ = (2/9) A² env² and μ ≥ μ0. A prime is d/dv. Where env > 0 we write κ := (log env)′. We put E(v) :=
sup_(v′≤v) |env(v′)|, the level of [[eq:layer-costs]]; the band is the set of v with λ^(3+δ) ≤ E(v) ≤ λ^(3−δ), where 0 <
δ ≤ 1/2; at a point (v, x̂) of the boundary, R(v, x̂) := λ³ A |env(v)| |ν(v − τ0)| |d(ϑ)|/m0(v), with ν and d as in
[[ch:equality-layer]]; and S is the first-degree amplitude of [[thm:l-24]] at fixed x̂, a continuously differentiable
complex function of v. In this section only, p := (μ/μ0)^(1/2) ≥ 1.

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

The next lemma uses one more part of (H_N): the bound on κ′ ([[def:edge-hypotheses]], k = 0).

**Lemma {#lem:l-24-kappa}** (The size of κ in the band.) Let x0 > 0, let env be positive and log-concave on
(v_s, v_s + x0] with env′ > 0 and |κ′| ≤ c_R κ^(1+α) there, where c_R > 0 and 0 < α < 1, and let env(v) → 0 as v ↓ v_s.
For v_s < v ≤ v_s + x0 put x := v − v_s. Then

    κ(v) ≥ (α c_R x)^(−1/α),                                                                       {#eq:l-24-kappa-low}

and if moreover v ≤ v_s + x0/2,

    κ(v) ≤ max{(2/(α c_R x0))^(1/α), (2^(1/α) α c_R log(env(v_s + x0)/env(v)))^(1/(1−α))}.          {#eq:l-24-kappa-up}

Let 0 < δ ≤ 1/2 and 0 < λ < 1 with λ^(5/2) < env(v_s + x0/2) and env(v_s + x0) ≤ λ^(−1/2), and let x_λ ∈ (0, x0/2) be
defined by env(v_s + x_λ) = λ^(5/2). Then every point v of the band satisfies v_s < v ≤ v_s + x_λ and

    (α c_R x_λ)^(−1/α) ≤ κ(v) ≤ κ̄_λ := max{(2/(α c_R x0))^(1/α), (2^(2+1/α) α c_R log(1/λ))^(1/(1−α))},
    κ(v) (v − v_s) ≥ (α c_R)^(−1/α) x_λ^(1−1/α).                                                   {#eq:l-24-kappa-band}

As λ → 0, x_λ → 0 and λ κ̄_λ^j → 0 for every j ≥ 1. So κ and κ(v − v_s) tend to ∞ uniformly on the band, and for every
δ′ ∈ (0, 1) there is a threshold on λ below which λκ ≤ λ^(δ′) at every point of the band.

*Proof.* As log env is concave and differentiable, κ is nonincreasing and κ′ ≤ 0; and κ > 0 since env′ > 0. If κ
were bounded by a number B on (v_s, v_s + x0], then log env(v) ≥ log env(v_s + x0) − B x0 for every v there, against
env(v) → 0; so κ(t) → ∞ as t ↓ v_s. Now (κ^(−α))′ = −α κ^(−α−1) κ′ = α κ^(−α−1) |κ′| lies in [0, α c_R]. For v_s < t < v,
κ(v)^(−α) ≤ κ(t)^(−α) + α c_R (v − t), and letting t ↓ v_s gives [[eq:l-24-kappa-low]].
For [[eq:l-24-kappa-up]] put h := κ(v)^(−α)/(α c_R). If h > x0/2, then κ(v) < (2/(α c_R x0))^(1/α). Otherwise
v + h ≤ v_s + x0, and for v ≤ t ≤ v + h, κ(t)^(−α) ≤ κ(v)^(−α) + α c_R h = 2κ(v)^(−α), so κ(t) ≥ 2^(−1/α) κ(v). As env
is increasing,

    log(env(v_s + x0)/env(v)) ≥ ∫_v^(v+h) κ ≥ 2^(−1/α) κ(v) h = 2^(−1/α) κ(v)^(1−α)/(α c_R),

which is [[eq:l-24-kappa-up]] in this case.
Let v be a point of the band. Then E(v) ≥ λ^(3+δ) > 0, so v > v_s. If v_s + x_λ < v ≤ v_s + x0, then E(v) ≥ env(v) >
env(v_s + x_λ) = λ^(5/2); if v > v_s + x0, then E(v) ≥ env(v_s + x0) > λ^(5/2). Both contradict E(v) ≤ λ^(3−δ) ≤ λ^(5/2),
so v ≤ v_s + x_λ, and env(v) = E(v) ≥ λ^(3+δ), as env is increasing on (v_s, v]. Hence log(env(v_s + x0)/env(v)) ≤
(1/2 + 3 + δ) log(1/λ) ≤ 4 log(1/λ), and [[eq:l-24-kappa-up]] gives κ(v) ≤ κ̄_λ. The lower bounds of
[[eq:l-24-kappa-band]] follow from [[eq:l-24-kappa-low]] with x ≤ x_λ, since −1/α < 0 and 1 − 1/α < 0. Finally, env is
continuous and positive on (v_s, v_s + x0], so for every y in (0, x0/2) we have x_λ < y once λ^(5/2) < env(v_s + y);
and κ̄_λ grows like a power of log(1/λ), so λ κ̄_λ^j → 0 and λ^(1−δ′) κ̄_λ → 0. ∎

**Proposition {#prop:l-24-transition}** (The first-degree term against the margin.) Let (v, x̂) be a point at which
[[lem:l-24-margin]] applies with ς ≤ 10⁻³ (by [[prop:l-24-band]], every point of the band once λ is below the thresholds
there), and suppose that

    |S′| ≤ 1.001 κ |S|,      |S| ≤ 1.001 R m0      at (v, x̂)                                         {#eq:l-24-s-bounds}

(by [[prop:l-24-s-bounds]], at every point of the band with R ≥ 1/2 once λ is small). Then at (v, x̂)

    m0′ − |S′| ≥ (2 − 3ς/4 − 1.002001 R) κ m0 ≥ (1.99925 − 1.002001 R) κ m0;                       {#eq:l-24-transition}

in particular m0′ − |S′| ≥ 0.89 κ m0 where R ≤ 1.1, m0′ − |S′| ≥ 0.93 κ m0 where R ≤ 1.06, and m0′ − |S′| ≥ 0.99 κ m0
where R ≤ 1.005.

*Proof.* By [[eq:l-24-s-bounds]], |S′| ≤ 1.001² κ R m0 = 1.002001 κ R m0, and by [[lem:l-24-margin]],
m0′ ≥ (2 − 3ς/4) κ m0; subtracting gives the first inequality, and 3ς/4 ≤ 0.00075 gives the second. Finally
1.99925 − 1.002001 · 1.1 = 0.8970489, 1.99925 − 1.002001 · 1.06 = 0.93712894 and 1.99925 − 1.002001 · 1.005 =
0.992238995. ∎

The two bounds [[eq:l-24-s-bounds]] are the properties of S that the proof of [[thm:l-24]] uses. They are needed only at
points where R lies near 1, and they follow there, for λ small, from the first-degree horizon value. We use it in the
following form. Let N ≥ 9 and let (H_N) of [[def:edge-hypotheses]] hold on (v_s, v_s + x0], with constants c_R > 0 and α
∈ (0, 1), and with x0 at most the x0′ of [[prop:edge-horizon-value]]; put r0 := v − τ0, T := λ κ_(N−1), c_N := N
μ0/(r0² + μ0) and Λ := λ^(N−2) env^(N−1)/env. The first-degree horizon value, [[prop:edge-horizon-value]], gives, with a
constant C independent of λ, v and x̂, at every point (v, x̂) with v_s < v ≤ v_s + x0 and λκ(v) ≤ 1 (the factor ϵ′ +
1/κ + λ of [[eq:edge-s]] being bounded),

    S = S_st + S_U + E_S,      S_st := λ³ A ν(r0) d(ϑ) env (1 + 2iλκ),
    S_U := −λ^(N+1) A i^N d(ϑ) Γ_R(r0) Ξ env^(N−1),      Ξ := ((1 − c_N) T − i c_N)/(T + i),
    |E_S| + |E_S′|/κ ≤ C [λ³ env (|ν(r0)| (λκ)² + λ) + |S_U|],                                    {#eq:l-24-s-split}

where ν and Γ_R > 0 are real functions of r0, smooth near r0 = v_s − τ0, d is a bounded function of the polar angle ϑ,
and either ν(v_s − τ0) ≠ 0 or ν(v_s − τ0) = ν′(v_s − τ0) = 0 ≠ ν″(v_s − τ0). The factor |1 + 2iλκ| makes |S_st| = R m0
(1 + 4λ²κ²)^(1/2), so S_st carries R exactly; the work is to show that S_U and E_S, and their derivatives, are small
against R m0 and κ R m0.

**Proposition {#prop:l-24-s-bounds}** (The first-degree amplitude where R ≥ 1/2.) Assume [[eq:l-24-s-split]] with the
properties stated after it, and let 0 < δ ≤ 1/2. There is λ_S ∈ (0, 1), independent of v and x̂, such that for
0 < λ < λ_S, at every point (v, x̂) of the band with R(v, x̂) ≥ 1/2,

    0.999 κ |S| ≤ |S′| ≤ 1.001 κ |S|,      0.999 R m0 ≤ |S| ≤ 1.001 R m0.                          {#eq:l-24-s-two-sided}

In particular [[eq:l-24-s-bounds]] holds at these points, and Λ ≤ λ and λκ ≤ λ^(δ′) (any fixed δ′ < 1) hold at every
point of the band once λ is small.

*Proof.* Put x := v − v_s. As Γ_R, ν and c_N are smooth near r0 = v_s − τ0 and d is bounded, there are x_1 > 0 and C such
that Γ_R, |Γ_R′|, |ν|, |c_N′| and |d| are at most C for 0 < x ≤ x_1, and c_N ≤ N everywhere. Moreover, after decreasing
x_1, |ν′(r0)| ≤ C (1 + 1/x) |ν(r0)| for 0 < x ≤ x_1: if ν(v_s − τ0) ≠ 0, take x_1 so small that |ν(r0)| ≥ |ν(v_s −
τ0)|/2; otherwise r0 − (v_s − τ0) = x, and Taylor's formula gives ν(r0) = (ν″(v_s − τ0)/2) x² (1 + O(x)) and ν′(r0) =
ν″(v_s − τ0) x (1 + O(x)), so x ν′/ν → 2 and |ν′/ν| ≤ 3/x for x small. Take λ below the thresholds of [[prop:l-24-band]]
and [[lem:l-24-kappa]], with x_λ ≤ min(x_1, 1), α c_R x_λ ≤ 1 and λ κ̄_λ ≤ 1. Let (v, x̂) be a point of the band with R ≥
1/2. By [[lem:l-24-kappa]], 0 < x ≤ x_λ, env(v) = E(v) lies in [λ^(3+δ), λ^(3−δ)] and 1 ≤ κ ≤ κ̄_λ, so λκ ≤ 1 and
[[eq:l-24-s-split]] applies; by [[prop:l-24-band]], ς ≤ 10⁻³. Put

    ε_λ := λ^(1−δ) (1 + λ κ̄_λ² + λ^(N−3) κ̄_λ^(N−1)) + λ κ̄_λ + x_λ^(1/α − 1),

which depends on λ alone and tends to 0 with λ, by [[lem:l-24-kappa]]. By [[eq:l-24-kappa-low]] and x ≤ x_λ ≤ 1, 1/κ and
1/(κx) are at most (α c_R)^(1/α) x_λ^(1/α − 1); so 1/κ, 1/(κx) and λκ are at most Cε_λ. Below, C is independent of λ, v
and x̂ and may change from line to line.

*The size of |ν| |d|.* By [[eq:l-24-m0]], m0 ≥ a_2/κ = A² env²/(9 √μ0 p^(3/2)), and p^(3/2) ≤ (1 + ς/2)^(3/4) ≤ 10/9
by the proof of [[lem:l-24-margin]]; so m0 ≥ A² env²/(10 √μ0). As R m0 = λ³ A env |ν(r0)| |d(ϑ)| and R ≥ 1/2,

    |ν(r0)| |d(ϑ)| ≥ A env/(20 √μ0 λ³) ≥ (A/(20 √μ0)) λ^δ,

and, |ν| and |d| being at most C, both |ν(r0)| and |d(ϑ)| are at least λ^δ/C. In particular ν(r0) ≠ 0.

*The size of S − S_st.* By (H_N), env^(N−1) = κ_0 κ_1 ⋯ κ_(N−2) env with 0 < κ_k ≤ 2κ, so Λ ≤ 2^(N−1) λ^(N−2) κ^(N−1) ≤
2^(N−1) λ^(N−2) κ̄_λ^(N−1) ≤ C ε_λ λ^δ, which is also at most λ for λ small. As |T + i| ≥ max(T, 1), |Ξ| ≤ |1 − c_N| +
c_N ≤ C, and Γ_R ≤ C; hence, with |ν| ≥ λ^δ/C,

    |S_U| ≤ C Λ λ³ A |d| env = C (Λ/|ν|) R m0 ≤ C ε_λ R m0.

Dividing the bound on E_S in [[eq:l-24-s-split]] by R m0 = λ³ A env |ν| |d| and using the lower bounds on |d|
and |ν| |d|,

    |E_S| ≤ C [(λκ)²/|d| + λ/(|ν| |d|)] R m0 + C |S_U| ≤ C [λ^(2−δ) κ̄_λ² + λ^(1−δ) + ε_λ] R m0 ≤ C ε_λ R m0.

So |S − S_st| ≤ C ε_λ R m0. As R m0 ≤ |S_st| = R m0 (1 + 4λ²κ²)^(1/2) ≤ (1 + 2ε_λ²) R m0,

    (1 − C ε_λ) R m0 ≤ |S| ≤ (1 + 2ε_λ² + C ε_λ) R m0.                                                  {#eq:l-24-s-size}

*The derivative.* At fixed x̂, d(ϑ) does not depend on v, and r0′ = 1. So S_st′ = S_st (κ + ν′/ν + 2iλκ′/(1 + 2iλκ)),
and with |ν′/ν| ≤ C (1 + 1/x) and |κ′| ≤ c_R κ^(1+α) ≤ c_R κ² (κ ≥ 1),

    |S_st′ − κ S_st| ≤ (C (1 + 1/x) + 2 c_R λκ²) |S_st| ≤ C ε_λ κ |S_st|,

since 1 + 1/x = κ (1/κ + 1/(κx)) and λκ² ≤ ε_λκ. In S_U, (env^(N−1))′ = κ_(N−1) env^(N−1) with κ_(N−1) ≤ 2κ; Ξ is affine
in c_N with ∂Ξ/∂c_N = −1, and ∂Ξ/∂T = i/(T + i)², so |Ξ′| ≤ |c_N′| + |T′| ≤ C + c_R λ (2κ)^(1+α) ≤ Cκ, by (H_N) for
κ_(N−1) and λκ^α ≤ λκ ≤ 1. Hence |(Γ_R Ξ env^(N−1))′| ≤ Cκ |env^(N−1)|, and |S_U′| ≤ C κ Λ λ³ A |d| env ≤ C ε_λ κ R m0.
By [[eq:l-24-s-split]], |E_S′| is at most κ times the bound on |E_S| used above, so |E_S′| ≤ C ε_λ κ R m0. Since R m0
≤ |S_st| and, by [[eq:l-24-s-size]], |S_st| ≤ |S| + C ε_λ R m0 ≤ |S| + C ε_λ |S_st|,

    | |S′| − κ |S| | ≤ |S′ − κ S| ≤ |S_st′ − κ S_st| + |S_U′| + κ |S_U| + |E_S′| + κ |E_S| ≤ C ε_λ κ |S|/(1 − C ε_λ).

As ε_λ → 0 with λ, this and [[eq:l-24-s-size]] give [[eq:l-24-s-two-sided]] once λ is small. The bound Λ ≤ λ was shown
above, and λκ ≤ λ^(δ′) is [[lem:l-24-kappa]]. ∎

Where R is small the bounds are not claimed. The bound on E_S in [[eq:l-24-s-split]] keeps the term C λ⁴ env, which
carries no factor |ν| |d|, while R m0 = λ³ A env |ν| |d|; so E_S need not be small against R m0 at points where |ν| |d|
is of order λ or smaller. The proof of [[thm:l-24]] uses [[eq:l-24-s-bounds]] only where R ∈ [1 − 2λ^γ, 1 + 2λ^γ], which
lies in [1/2, 1.1] once 2λ^γ ≤ 1/10. So, for λ small, the conclusions of [[prop:l-24-transition]] hold at every point of
the band with 1/2 ≤ R ≤ 1.1.

On the band, for λ small, R is strictly decreasing in v and varies little over two carrier periods. At fixed x̂ with
d(ϑ) ≠ 0, (log R)′ = κ + ν′/ν − m0′/m0. By [[lem:l-24-margin]] with ς ≤ 10⁻³ and √μ0 κ ≥ 2, 1.99925 κ ≤ m0′/m0 ≤
2.6 κ. As in the proof of [[prop:l-24-s-bounds]], |ν′/ν| ≤ C(1 + 1/x) ≤ κ/10. So −1.7 κ ≤ (log R)′ ≤ −0.89 κ, and
log R varies by at most 7πλκ̄_λ on every interval of length 4πλ. Hence two consecutive carrier periods, one of which
meets {1 − 2λ^γ ≤ R ≤ 1 + 2λ^γ}, lie where 1/2 ≤ R ≤ 1.1 once λ is small. Along the band, the points with
R ≥ 1 + 2λ^γ precede those with |R − 1| < 2λ^γ, and these precede those with R ≤ 1 − 2λ^γ.

**Remark {#rem:l-24-sharp}** (The factor 2 − R.) The constant 2 of [[lem:l-24-margin]] is approached as v ↓ v_s. Let env
be positive and log-concave on (v_s, v_s + x0] with env(v) → 0 as v ↓ v_s. Then κ is nonincreasing there and κ(v) → ∞ as
v ↓ v_s, since a finite limit B would give log env(v) ≥ log env(v_s + x0) − B x0 for every v in (v_s, v_s + x0]; so ς →
0, and both bounds of [[eq:l-24-margin-bounds]] tend to 2. So the constant 2 in [[eq:l-24-transition]] cannot be raised;
nor can the coefficient of R be lowered, as follows. If at (v, x̂) also |S′| ≥ 0.999 κ |S| (as for any constant multiple
of env, for which |S′| = κ|S|) and |S| ≥ 0.999 R m0, with ς ≤ 10⁻³ and √μ0 κ ≥ 10³, then (1 + ς/8)/(√μ0 κ) ≤ 1.001 ·
10⁻³, 0.999² ≥ 0.998, and the upper bound of [[eq:l-24-margin-bounds]] gives

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
[[prop:l-24-s-bounds]]; and by [[lem:l-24-kappa]], (α c_R x_λ)^(−1/α) ≤ κ ≤ κ̄_λ on I, so √μ0 κ ≥ 2 and κ ≥ 1 once
x_λ is small, and 2π (c_R + 3) λ κ̄_λ ≤ 1/26 once λ is small.

*Proof.* By [[lem:l-24-margin]] with ς ≤ 10⁻³ and √μ0 κ ≥ 2,
0 < m0′/m0 ≤ (2 + 1.000125/2) κ ≤ 3κ. So |(log(κ m0))′| = |κ′/κ + m0′/m0| ≤ |κ′|/κ + 3κ, and by [[eq:l-24-period-cond]]
log(κ m0) varies by at most 1/26 on I. As e^y < 1/(1 − y) for 0 < y < 1, e^(1/26) < 26/25, so κ m0 ≥ (25/26) κ(t) m0(t)
on I. The left side of [[eq:l-24-period]] is ∫_I (m0′(s) + Re[S′(s) e^(it/λ)]) ds ≥ ∫_I (m0′ − |S′|) ds, and by
[[prop:l-24-transition]] this is at least 0.89 · 2πλ · (25/26) κ(t) m0(t) ≥ 1.71 πλ κ(t) m0(t). ∎

**Remark {#rem:l-24-eps}** (The degree-two terms against the margin.) The proof of [[thm:l-24]] bounds the degree-two
terms at the boundary through the costs ε_c(v) := Σ_(i≤c) sup_(v′≤v) |env^(i)(v′)| for fixed c ≥ 1, among them
c = M* := 2N + 8, the cost of the expansion on the boundary in [[ch:equality-layer]]. No bound m0 ≥ c′ ε_c² with c′ > 0
independent of λ holds in the band: there ε_c ≥ env′ = κ env, while by [[eq:l-24-m0]] and [[eq:l-24-logconcave]]
m0 = (a_1 + a_2)/κ ≤ (A² env²/(9 √μ0)) (1 + 1/(2 √μ0 κ)), so m0/ε_c² ≤ C/κ², which tends to 0 with λ by
[[lem:l-24-kappa]]. What holds, and suffices, is [[eq:layer-cost-margin]] of [[cor:layer-interpolation-band]], applied
with m := 84c: its hypotheses are c ≥ 1, m ≥ 84c, λ ≤ 1 and λ^(3+δ) ≤ E(v) ≤ 1, and at a point of the band E(v) ≤
λ^(3−δ) ≤ 1. So at every point v of the band

    ε_c(v)² ≤ C λ^(−1/8) m0(v),                                                                    {#eq:l-24-eps}

with C depending on c, A, μ0, μ(v_end) and sup |env^(84c)|, and not on λ or v.

*Proof of [[thm:l-24]].* Take x0 at most the x0′ of [[prop:edge-horizon-value]], and λ below the thresholds of
[[prop:layer-regions]] (iii), [[prop:l-24-band]], [[lem:l-24-kappa]], [[prop:l-24-s-bounds]] and [[cor:l-24-period]].
By [[prop:l-24-band]] the band lies in (v_s, v_s + x0), and as env is increasing it is the interval on which λ^(3+δ) ≤
env ≤ λ^(3−δ), with E = env there. By [[prop:l-24-s-bounds]], λκ ≤ λ^(δ′) and Λ ≤ λ on the band.

*The decomposition.* From g_λ = g_app + w and h^(1) = h_app^(1) + e, g_λ − g0 = h^(1) + (g_app − g0 − h_app^(1)) + (w −
e). At a boundary point X = (t, r_q(t), x̂), [[lem:layer-inverse]] and [[prop:edge-horizon-value]] give

    g_λ⁻¹(dΦ0, dΦ0) = −m0 − Re[S(t) e^(it/λ)] + ρ_s + ρ_r,      ρ_r := −(w − e)(Φ0♯, Φ0♯),

where ρ_s is the rest: −(g_app − g0 − h_app^(1))(Φ0♯, Φ0♯), the difference between h^(1)(Φ0♯, Φ0♯) and h^(1)_vv(t,
√μ0) (the shift from √μ0 to r_q and the β_Φ-terms), and q of [[lem:layer-inverse]]. S has the form
[[eq:l-24-s-split]], as λκ ≤ 1.

*The increments.* For t ∈ I_k write Δf := f(t + 2πλ) − f(t). As e^(i(t+2πλ)/λ) = e^(it/λ),

    Δ g_λ⁻¹(dΦ0, dΦ0) = −[Δm0 + Re(ΔS e^(it/λ))] + Δρ_s + Δρ_r.

Let I_k or I_(k+1) meet {|R − 1| ≤ 2λ^γ}. By the last paragraph of [[sec:l-24-margin]] both lie where 1/2 ≤ R ≤ 1.1,
and [[cor:l-24-period]] gives Δm0 + Re(ΔS e^(it/λ)) ≥ 1.7πλκ(t) m0(t). We show |Δρ_s| + |Δρ_r| ≤ πλκ(t) m0(t)/2.
Then Δ g_λ⁻¹(dΦ0, dΦ0) ≤ −1.2πλκ m0 < 0 for every t ∈ I_k, so every value on I_(k+1) is below a value on I_k, and
M_(k+1) < M_k.

The points t, t + 2πλ and t + O(λ) used below lie in the band, R varying by o(1) over O(λ) there, and m0 varies by a
factor at most 2 over O(λ), since 0 < m0′/m0 ≤ 3κ ([[lem:l-24-margin]], as in the proof of [[cor:l-24-period]]) and
λκ → 0. By [[eq:l-24-eps]] at those points, ε_c² ≤ C λ^(−1/8) m0(t) for every fixed cost c. Moreover ε_c ≥ E ≥ λ^(3+δ)
and ε_c ≤ C E^(1−c/m) ≤ C λ² by [[eq:layer-cost-level]].

(a) g_app − g0 − h_app^(1) = Σ_(j≤N) λ^j([g_j] − Re[H_j e^(iθ)]) − λ^(N+1) Re[H_(N+1) e^(iθ)] at θ = t/λ is a sum of λ^j
G_j(X, θ), G_j 2π-periodic in θ. At a fixed phase its increment is G_j(X(t + 2πλ), θ) − G_j(X(t), θ), at most 2πλ
sup |∂_X G_j| |dX/dt|, with |dX/dt| ≤ C on the boundary. By [[eq:layer-identification]] with i = 1 and [[lem:layer-flat]]
(c), |∂_X G_j| ≤ C ε_c² for j ≤ N and |∂_X H_(N+1)| ≤ C ε_c. So this increment is at most C λ² ε_c² + C λ^(N+2) ε_c ≤ C
λ^(15/8) m0 + C λ^(N+2−3−δ−1/8) m0, using ε_c ≤ ε_c²/λ^(3+δ). The shift and the β_Φ-terms are at most C ε_0² ε_c ≤ C λ²
ε_c² ([[cor:layer-expansion]]), and q at most C (λ² ε_c + λ ε_c² + |w|)², with |w| ≤ C λ^(N−5) ε_c
([[lem:layer-remainder-weak]]); their increments are at most twice their sizes, C λ^(15/8) m0 at most.

(b) By [[lem:edge-w-minus-e]], |Δρ_r| ≤ 2 sup |w − e| ≤ C(λ^(N−6) ε_c² + λ^(N−2) ε_c) ≤ C(λ^(N−6−1/8) + λ^(N−5.5−1/8))
m0.

As N ≥ 9 and κ ≥ 1 in the band, each of these is below πλκ m0/8 for λ small.

*The signs.* By [[prop:layer-regions]] (iii), if R ≥ 1 + 2λ^γ at the midpoint of I_k, the boundary has timelike points
in I_k at x̂, so M_k > 0; and if R ≤ 1 − 2λ^γ on I_k, it is spacelike there, so M_k < 0.

*Exactly once.* Every period is of the first kind, or of the second, or meets {|R − 1| ≤ 2λ^γ}, by continuity of R. As R
is strictly decreasing along the band (the last paragraph of [[sec:l-24-margin]]), the periods of the first kind precede
the others and those of the second kind follow them. Both kinds occur. At the left end of the band env = λ^(3+δ), and on
the first period env ≤ 2λ^(3+δ), as λκ → 0; there m0 ≤ (2A²/(9√μ0)) env² by the bound in [[rem:l-24-eps]], so R ≥
(9√μ0 |ν| |d|/(2A)) λ³/env ≥ (6√μ0 |ν|/A) λ^(−δ), using |d| ≥ 8/3. Off ρ*, |ν| ≥ ν_*; at ρ*, |ν| ≥ c x² and x ≥ κ^(−α)/(α
c_R) ≥ κ̄_λ^(−α)/(α c_R) by [[lem:edge-kappa]] (a) and [[lem:l-24-kappa]], a power of 1/log(1/λ). So R ≥ 2 on the first
period for λ small. At the right end env = λ^(3−δ), and on the last period env ≥ λ^(3−δ)/2; there m0 ≥ A² env²/(10√μ0)
(the proof of [[prop:l-24-s-bounds]]), so R ≤ (10√μ0 |ν| |d|/A) λ³/env ≤ C λ^δ ≤ 1/2. So the sequence (M_k) is positive
on the periods of the first kind, strictly decreasing from the last of them to the first period of the second kind, and
negative from there on: it changes sign exactly once. ∎

**Remark {#rem:l-24-numbers}** (Numerical observation.) In a model of the band with exp(−1/x), λ = 10⁻⁶, a slowly
varying degree-two term of size λ^(1/10) m0 and an unstructured one of size λ³ m0, the maxima over 80 consecutive
carrier periods around R = 1 decreased strictly and changed sign once; with an unstructured term of size m0/3 they
changed sign more than once. No proof uses this observation.

### Dips {#sec:edge-dips}

Some regularity of the edge is needed for the conclusions of [[thm:very-edge]] and [[thm:edge-past]] at every level
below λ^(3+δ): for an envelope whose intervals of zeros accumulate at v_s the boundary is spacelike throughout some
intervals of length 4πλ below that level, for every small λ.

**Proposition {#prop:edge-dips}** (Dips.) Let ϕ(t) := e^(−1/(1−t²)) for |t| < 1 and ϕ(t) := 0 otherwise, and near v_s
let

    env(v) := Σ_(n≥n0) h_n ϕ(s_n (v − v_s − 2^(−n))),      h_n := e^(−n²),      s_n := 2^(n+2),           {#eq:edge-dips}

continued to a C_c^∞ envelope; it is smooth and flat at v_s, as h_n s_n^k → 0 for every k. The bump n lives on v − v_s
∈ [3/4, 5/4] · 2^(−n), so env = 0 on J_n := v_s + (5/4, 3/2) · 2^(−n). Let δ ∈ (0, 1/2]. There is λ_25(δ) > 0 such that
for λ ≤ λ_25(δ), with n the least index with h_n ≤ λ^(3+δ), at every x̂ ∈ S³ and every v ∈ J_n′ := v_s + [(5/4)2^(−n),
(3/2)2^(−n) − ρ_w], ρ_w = O(λ) the reach of [[lem:layer-remainder-weak]] (resp. [[lem:layer-remainder-past]]),

    g_λ⁻¹(dΦ0, dΦ0)(v, r_q(v), x̂) ≤ −m0(v)/2 < 0,

for the metric of [[thm:main]], K ≥ 6, and for that of [[thm:past-construction]]. J_n′ lies in the layer, below the
level λ^(3+δ) (E = h_n/e there), and is longer than 4πλ. So for this envelope, for every small λ, intervals of length
4πλ below λ^(3+δ) on which the boundary is spacelike throughout occur on every column.

*Proof.* Fix v ∈ J_n′ and x̂, and put X := (v, r_q(v), x̂), v1 := v + ρ_w and L := log(1/λ).

(1) *The oscillating profiles vanish at X.* W, χ, the ĝ_m and the phase terms of the fixed-phase rewriting solve, at
fixed v, transports along ℓ whose forcing terms and data at that v are polynomials in env^(k)(v) and in the oscillating
profiles at that v, every monomial with an oscillating factor ((F1) of [[sec:layer-flat]], and step (i) of the proof of
[[lem:stage-data]]); this is the argument of the proof of [[prop:mean-mass]] outside the shell, applied at a v with
env^(k)(v) = 0 for every k. By induction on the order they vanish at X. The phases φ_m, which the means drive, enter
g_app only through the phase of the oscillating profiles. So at X, g_λ − g0 = Σ_(j≥1) λ^j m_j + w. The same holds for
the stages of [[thm:past-approximant]], which are transports at fixed v from past null infinity.

(2) *Bounds.* With B_k := Σ_(i≤k) sup |ϕ^(i)|, ε_k(v1) ≤ 2 h_n s_n^k B_k: the bump n − 1 starts at (3/2)2^(−n), beyond
v1, and the bumps m > n add at most h_n s_n^k B_k, as h_(m+1) s_(m+1)^k ≤ h_m s_m^k/2 once e^(2m+1) ≥ 2^(k+1). By
[[lem:layer-flat]] (b) (by [[lem:layer-flat-past]] for the metric of [[thm:past-construction]]), |m_j| ≤ C ε_(2j+1)(v)².
By [[lem:layer-remainder-weak]], for the metric of [[thm:main]], |w| ≤ C λ^(N−5) ε_(M*)(v1) given ε_4(v1) ≤ λ; by
[[lem:layer-remainder-past]], for the metric of [[thm:past-construction]], |w| ≤ C λ^(N_P−3) ε_(M_P)(v1) given
ε_(M_P)(v1) ≤ λ³. Both hypotheses hold for λ small, since h_n ≤ λ^(3+δ) and s_n^k B_k = e^(O(L^(1/2))).

(3) *The margin.* m0 ≥ √(μ/μ0) − 1 ≥ (μ − μ0)/(3μ0), as √x − 1 = (x − 1)/(√x + 1) and μ ≤ 4μ0 in the layer, so

    m0(v) ≥ (2A²/(27μ0)) ∫_(v_s)^v env² ≥ (2A²/(27μ0)) h_n² s_n⁻¹ I_ϕ,      I_ϕ := ∫_(−1)^1 ϕ².

(4) *The ratio.* [[lem:layer-inverse]] with k = g_λ − g0 gives |g_λ⁻¹(dΦ0, dΦ0) + m0| ≤ C|k| ≤ C′(max_(j≤N) λ^j
ε_(2j+1)(v)² + λ^(N−5) ε_(M*)(v1)) for the metric of [[thm:main]], and the same with N_P, M_P and λ^(N_P−3) for the
metric of [[thm:past-construction]]. Its ratio to the bound of (3) is at most

    C″ (max_(j≤N) λ^j s_n^(4j+3) B_(2j+1)² + λ^(N−5) h_n⁻¹ s_n^(M*+1) B_(M*)).

Since h_(n−1) > λ^(3+δ), h_n = h_(n−1) e^(−(2n−1)) > λ^(3+δ) e^(−(2n−1)), and n ≤ ((3 + δ)L)^(1/2) + 1; so h_n ≥
λ^(3.4+δ) once 2((3 + δ)L)^(1/2) + 1 ≤ 0.4L, that is for λ ≤ λ_h(δ) := exp(−y_h²), y_h := (2(3 + δ)^(1/2) + (4(3 + δ) +
1.6)^(1/2))/0.8; for instance λ_h(1/10) = 10^(−35.79…) and λ_h(1/2) = 10^(−40.14…). Then the ratio is at most C″ (max_j
λ^j s_n^(4j+3) B_(2j+1)² + λ^(N−8.4−δ) s_n^(M*+1) B_(M*)), which tends to 0 as λ → 0, since N − 8.4 − δ ≥ 0.1 for N ≥ 9
and δ ≤ 1/2, and s_n = 2^(n+2) grows slower than every power of 1/λ; for the metric of [[thm:past-construction]] the
exponent is N_P − 6.4 − δ. Let λ_25(δ) be the least of λ_h(δ) and the thresholds below which the hypotheses of (2) and
(4)'s ratio ≤ 1/2 hold. Then g_λ⁻¹(dΦ0, dΦ0) ≤ −m0 + m0/2.

Finally, sup_(v′≤v) env = h_n ϕ(0) = h_n/e ≤ λ^(3+δ) on J_n′, the layer contains J_n′ for λ small (μ − μ0 there is
of order h_n², against 4μ0 C_Φ λ, as in the proof of [[thm:layer]]), and J_n′ has length at least 2^(−n−3) ≫ 4πλ. ∎

**Remark {#rem:edge-criterion}** (Where the ratio decides.) At a boundary point in the deep layer write g_λ⁻¹(dΦ0, dΦ0) =
−m0 − Re[S e^(iv/λ)] + ρ with |ρ| ≤ D(v), where (S, D) is the following: on a zero interval as in [[prop:edge-dips]],
S := 0 and D the bound of its step (4), the first-degree terms being part of w there; in the band λ^(3+δ) ≤ E ≤
λ^(3−δ), S the first-degree amplitude of [[prop:layer-regions]] (iii) and D ≤ λ^γ m0; on an edge where (H_N) and (H_D)
hold, S of [[prop:edge-horizon-value]] (for the metric of [[thm:main]]) or of [[lem:edge-resummation]] (for that of
[[thm:past-construction]]) and D = C κ^(2c′) env². On an interval J = [v, v + 4πλ] on which S varies little, the
boundary has timelike points at x̂ if max_J (|S| − m0) ≥ C(λ^γ m0 + D), and none if max_J (|S| + D) < min_J m0, since
g_λ⁻¹(dΦ0, dΦ0) ≤ −m0 + |S| + D. So the ratio |S|/m0 decides up to the factor 1 ± 2λ^γ in the band, a zero interval
as in [[prop:edge-dips]] is spacelike, and the very edge of [[thm:edge-past]] and [[thm:very-edge]] has timelike
points; where env > 0 and no listed D is below m0, at a dip of a general envelope, the criterion decides nothing.

**Remark {#rem:edge-dips-numbers}** (Numerical observation.) The three terms of step (4) of the proof of
[[prop:edge-dips]] were evaluated in log10 with unit constants (A = μ0 = 1, every constant of the lemmas 1). At δ = 1/10
the ratio for the metric of [[thm:main]] was +221, −86, −6544, −82950 and −877515 in log10 at λ = 10^(−10²), …,
10^(−10⁶), and at δ = 1/2 it was +286, +335, −2578, −42399 and −476461: the decay λ^(0.1) wins only from λ about
10^(−10⁴) on. The ratios for the metric of [[thm:past-construction]] and of the means were negative throughout. With the
zero intervals removed, or with the bump heights h_n near λ⁴, the ratio became large. No proof uses these figures.

### The thresholds {#sec:edge-thresholds}

**Remark {#rem:edge-thresholds}** (What the thresholds are.) The thresholds λ_E, λ_1E, λ_26, λ_28 and λ_24 of this
chapter depend only on the constants of [[ch:data]], [[ch:uniform-existence]] and [[ch:past-construction]], on the bounds
of the stage profiles, and on the envelope's constants of [[def:edge-hypotheses]], and so does λ_D, which the proof of
[[lem:edge-localisation]] writes in terms of them; they are not evaluated. The constants C_L11 and C_L4 of the threshold
λ_L of [[thm:layer]] ([[eq:layer-threshold]]) are not evaluated ([[rem:layer-threshold-size]]);
[[lem:edge-layer-constants]] writes them, and the threshold λ_P of [[thm:past-construction]], in terms of the constants
of the results they come from.

The threshold λ_25(δ) of [[prop:edge-dips]] is explicit. Write λ = 10^(−E) and s := ((3 + δ) ln 10)^(1/2), so that n +
2 ≤ s E^(1/2) + 3. With h_n ≥ λ^(3.4+δ) (for λ ≤ λ_h(δ)) and ε_k(v1) ≤ 2h_n s_n^k B_k, each condition of the proof
reads −aE + b E^(1/2) + c + γ ≤ log10 τ and holds for every E ≥ E_i := y₊², y₊ := (b + (b² + 4a(c + γ − log10
τ))^(1/2))/(2a). For the remainder of the metric of [[thm:main]], a = N − 8.4 − δ, b = (M* + 1) s log10 2, c =
log10(27/I_ϕ) + log10 B_(M*) + 3(M* + 1) log10 2 and τ = 1/4; for its means, each j ≤ N, a = j and τ = 1/(4N); the
same for the metric of [[thm:past-construction]] with N_P and M_P; for the hypotheses ε_4(v1) ≤ λ and ε_(M_P)(v1) ≤ λ³
of the remainder lemmas, a = 2 + δ and a = δ; and λ ≤ λ_h(δ), e^(2n+1) ≥ 2^(M_P+1), and the length of J_n′. Here γ is
log10 of a product of the constant of [[lem:layer-inverse]], that of the remainder lemma or of [[lem:layer-flat]] (b),
μ0 and A⁻², and for the length of J_n′ γ = log10(4π + C_ρ), C_ρ λ := ρ_w. Then

    λ_25(δ) = min(λ_rec, 10^(−E_25(δ))),      E_25(δ) := max_i E_i(δ),

λ_rec the threshold below which the lemmas used hold. The constants in γ and λ_rec are not evaluated, but the condition
ε_(M_P)(v1) ≤ λ³ involves none of them: there a = δ ≤ 1/2, b = M_P s log10 2 and c = 3M_P log10 2 + log10(2B_(M_P)), with
τ = 1 and γ = 0. Its threshold gives an upper bound for λ_25(δ) whatever the other constants are
([[prop:edge-lambda-25]]); no proof uses it.

**Lemma {#lem:edge-layer-constants}** (The constants of the layer.) Let N = K + 3, ε := ε_(M*)(v) and Δτ := τ_end − τ0.

(a) Let C_H(j) and C_I(j), 1 ≤ j ≤ N, be constants with |H_j| ≤ C_H(j) ε and |g_j − Re[H_j e^(iθ)]| ≤ C_I(j) ε² at
the points of Ω with v ≤ v_♯ ([[lem:layer-flat]] (c) and [[eq:layer-identification]] at order zero), C′_H one with the
bound C′_H ε for |∂_r H_3| there, and put C_β := (A²/(9μ0))(1 + (μ0 μ(v_end))^(1/4)/2) and C_r := A²/(18√μ0). Then the
three bounds of [[eq:layer-expansion]] hold with

    C_L11 := (1 + 2C_β)² max{ Σ_(j=1)^N λ0^(j−1) (C_H(j) + C_I(j)),  Σ_(j=2)^N λ0^(j−2) C_H(j),
                              Σ_(j=4)^N λ0^(j−4) C_H(j),
                              Σ_(j=1)^N λ0^(j−1) C_I(j) + λ0² (C′_H C_r + (2 + C_β) C_β C_H(3)),  1 }.

(b) Let C_en be the constant of the energy inequality of step 6 of the proof of [[lem:layer-remainder]] (that of
[[lem:energy]] with the coefficient bounds of step 3, Gronwall's inequality included), C_L a constant with L_ij ≤ C_L
λ^(j−i) in the proof of [[lem:layer-remainder-weak]], C_D(i) constants with E^(i)(τ0) ≤ C_D(i) λ^(N−3−i) ε_(M*)(v1) for
the data of step 5, C_d one with |∂^i Ric^H(g_app)| ≤ C_d λ^(N−1−i) ε_(M*)(v1) ([[lem:layer-flat]] (d), i ≤ 2), V_Σ the
largest volume of a slice Σ_τ, and C_S the constant of step 7. Put Ĉ_0 := C_en (C_D(0) + Δτ V_Σ^(1/2) C_d) and, for i =
1, 2, Ĉ_i := C_en (C_D(i) + Δτ V_Σ^(1/2) C_d + Δτ C_L Σ_(j<i) Ĉ_j). Then [[lem:layer-remainder-weak]] holds with

    C_L4 := C_S (Ĉ_0 + Ĉ_1 + Ĉ_2).

(c) λ_P is the least of λ1 and d0/20 ([[sec:past-inequalities]]), of the thresholds of [[prop:far-region]], of
[[prop:near-region]] and of the limit, and of the threshold of [[thm:uniform-existence]] with this K applied on Ω in
[[sec:past-proof]]. Written out with the constants named in those proofs: λ ≤ 1/C in the data bound of
[[prop:far-region]], C λ ≤ ε_P/2 for the margin of [[lem:past-domain]] (f) under the bootstrap bound there, and λ^(K′−5)
≤ (4 C² e^(6C) M_F)⁻¹, which closes C e^(6C) C M_F² λ^(2K′−5) ≤ M_F λ^(K′)/4 there; in [[prop:near-region]], C″ λ ≤ 1/8
for the nonlinear terms, the absorption of the terms with a profile g_j, j ≥ 3, each carrying a factor λ, and the
margin; and in [[sec:past-proof]], the hypothesis Data(w_n) ≤ C M_N λ^(K′−2β0−1) of [[thm:uniform-existence]].

*Proof.* (a) At a boundary point X, k = Σ_(j≤N) λ^j [g_j] + w ([[cor:layer-expansion]]). By concavity of the root, the
modulus of β_Φ is at most (μ − μ0)/(2μ0) + r_q μ′/(4μ0) ≤ C_β ε², since μ − μ0 ≤ (2/9) A² (v − v_s) ε_0² with v − v_s ≤
1, μ′ = (2/9) A² env² and r_q ≤ (μ0 μ(v_end))^(1/4); and r_q − √μ0 ≤ (μ − μ0)/(4√μ0) ≤ C_r ε². In Cartesian components
Φ0♯ = (1 − β_Φ) ∂_τ + β_Φ x̂·∂_x, so |Φ0♯|_e ≤ 1 + 2|β_Φ| ≤ 1 + 2C_β, as ε ≤ 1. The bound for |k| is Σ_j λ^j (C_H(j) ε +
C_I(j) ε²) + |w| ≤ λε Σ_j λ0^(j−1) (C_H(j) + C_I(j)) + |w|. For k(Φ0♯, ·): H_1 has only angular components, so H_1(Φ0♯,
·) = 0, and |H_j(Φ0♯, ·)| ≤ (1 + 2C_β) C_H(j) ε for j ≥ 2; the rest is as for |k|, times 1 + 2C_β. For k(Φ0♯, Φ0♯): H_1
and H_2 lie in 𝔖 ([[prop:layer-linear]]), so H_j(Φ0♯, Φ0♯) = 0 for j ≤ 2; and H_3(Φ0♯, Φ0♯) is H_3,vv(v, √μ0) +
(H_3,vv(v, r_q) − H_3,vv(v, √μ0)) + 2β_Φ H_3,vr + β_Φ² H_3,rr, where the first term is A env d ν(v − τ0)
([[prop:layer-linear]] (d)), the second is at most C′_H ε C_r ε², and the last two at most (2 + C_β) C_β C_H(3) ε³; the
terms j ≥ 4 are at most λ⁴ ε Σ_(j≥4) λ0^(j−4) C_H(j) (1 + 2C_β)²; and the degree-two parts and w contribute λ ε² Σ_j
λ0^(j−1) C_I(j) (1 + 2C_β)² + (1 + 2C_β)² |w|. Each coefficient is at most C_L11.

(b) In the triangular argument of the proof of [[lem:layer-remainder-weak]], E^(i)(τ) ≤ C_en (E^(i)(τ0) + ∫_(τ0)^(τ)
(‖∂^i Ric^H(g_app)‖ + Σ_(j<i) L_ij E^(j))), with ‖∂^i Ric^H(g_app)‖ ≤ V_Σ^(1/2) C_d λ^(N−1−i) ε_(M*)(v1). By induction
on i, E^(i) ≤ Ĉ_i λ^(N−3−i) ε_(M*)(v1), since λ^(N−1−i) ≤ λ^(N−3−i) and L_ij λ^(N−3−j) ≤ C_L λ^(N−3−i). Step 7
gives |w(X)| ≤ C_S Σ_(i≤2) E^(i) ≤ C_S (Ĉ_0 λ² + Ĉ_1 λ + Ĉ_2) λ^(N−5) ε_(M*)(v1) ≤ C_L4 λ^(N−5) ε_(M*)(v1), as λ ≤ 1.

(c) Each condition listed is the place where the proof named says "for λ small" or "for λ ≤ λ_N", written as the
inequality it needs; the other steps of those proofs hold for every λ ≤ min(λ1, d0/20). ∎

**Proposition {#prop:edge-lambda-25}** (An upper bound for the threshold of the dips.) For every δ ∈ (0, 1/2] and every
K ≥ 6, λ_25(δ) ≤ 10^(−6282).

*Proof.* Let E_H be the threshold E_i of the condition ε_(M_P)(v1) ≤ λ³ in [[rem:edge-thresholds]], so that λ_25(δ) ≤
10^(−E_25(δ)) ≤ 10^(−E_H). As a = δ, τ = 1 and γ = 0, E_H = y₊² with

    y₊ = b/(2δ) + (b²/(4δ²) + c/δ)^(1/2),      b = M_P log10 2 (ln 10)^(1/2) (3 + δ)^(1/2),
    c = 3M_P log10 2 + log10 2 + log10 B_(M_P).

(1) *Reduction to δ = 1/2 and M_P = 44.* y₊ increases with b and with c. M_P = 2N_P + 8 with N_P = K + 4 + ⌈4β0⌉ and
β0 ≥ 2 ([[prop:near-region]], [[sec:past-proof]]), so N_P ≥ K + 12 ≥ 18 and M_P ≥ 44; b and c increase with M_P, B_k
being nondecreasing in k. The function (3 + δ)^(1/2)/(2δ) decreases on (0, 1/2], its derivative being (δ − 2(3 + δ))/
(4δ²(3 + δ)^(1/2)) < 0, so b/(2δ) is at least its value at δ = 1/2; and c/δ ≥ 2c. Hence

    y₊ ≥ b₁ + (b₁² + 2c₁)^(1/2),      b₁ := 44 log10 2 (3.5 ln 10)^(1/2),      c₁ := 133 log10 2 + log10 B_44.

(2) *A lower bound for B_44.* ϕ vanishes on [1, ∞), so ϕ and all its derivatives vanish at t = 1, and Taylor's formula
at 1 with integral remainder gives, for 0 < t < 1, ϕ(t) = ∫_1^t ((t − u)^43/43!) ϕ^(44)(u) du, hence ϕ(t) ≤
sup|ϕ^(44)| (1 − t)^44/44!. At t = 87/88, 1 − t² = 175/7744, and so

    B_44 ≥ sup|ϕ^(44)| ≥ 44! 88^44 e^(−7744/175).

Here 44! = 2658271574788448768043625811014615890319638528000000000 ≥ 2.6582 · 10^54, so log10 44! ≥ 54 + log10 2.6582 ≥
54.4245; 44 log10 88 ≥ 85.5572; and 7744/(175 ln 10) ≤ 19.2182, as ln 10 ≥ 2.302585. So log10 B_44 ≥ 120.7635.

(3) *The number.* With log10 2 ≥ 0.301029, c₁ ≥ 40.0368 + 120.7635 ≥ 160.79; with (3.5 ln 10)^(1/2) ≥ 2.838846 (its
square is below 8.059047 < 3.5 · 2.302585 = 8.0590475), b₁ ≥ 44 · 0.301029 · 2.838846 ≥ 37.601. Then

    y₊ ≥ 37.601 + (37.601² + 2 · 160.79)^(1/2) ≥ 37.601 + (1735.415)^(1/2) ≥ 37.601 + 41.6583 = 79.2593,

as 41.6583² ≤ 1735.414, and E_H ≥ 79.2593² ≥ 6282.03. ∎
