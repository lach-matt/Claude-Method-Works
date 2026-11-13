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
modulus of e^(−s̃u) is e^(−κu)), and f′ = −ψ′ e^(−ψ) on (0, x), f′ = 0 beyond. So the right side is −s̃^(−2) ∫_0^x G_1 e^(−s̃u)
du − s̃^(−1) ∫_0^x G_2 e^(−s̃u) du with G_1 := ψ′ e^(−ψ) and G_2 := u ψ′ e^(−ψ). Both vanish at u = 0 and as u ↑ x
(G_1 = −f′), so a second integration by parts gives ∫_0^x G_m e^(−s̃u) du = s̃^(−1) ∫_0^x G_m′ e^(−s̃u) du, and

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
μ′/(2r²) + F μ/r³, every component of Γ[g0] − Γ[g0°] is a polynomial of degree at most two in (μ − μ0, μ′), without constant
term, with coefficients functions of r and of the angles. So Ric^H relative to g0 equals Ric^H relative to g0° plus a
term 𝒜(g) with |𝒜| ≤ C (|μ − μ0| + |μ′| + |μ″|) for (g, ∂g) bounded, and |∂^k Ω^β 𝒜| ≤ C ε_(k+1)(v)² at points with
that v, since 0 ≤ μ − μ0 ≤ (2/9) A² (v − v_s) ε_0², μ′ = (2/9) A² env² and μ″ = (4/9) A² env env′. With u := g_λ − g0°,
g0° vacuum and D(g0°) = 0, Ric^H(g0° + u) = dRic^H(u) + 𝒩(u), and by the quasilinear form [[eq:gauge]] (second
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
ψ_max := 2 + τ_end − τ0 ≥ ψ. In the proofs of [[lem:layer-remainder]] and [[lem:layer-remainder-past]] the tilt
(2C1λ, resp. 2C_Pλ) is used only to make the face {v + e ψ(τ) = V} have a conormal α = dv + e ψ′ dτ timelike for g_λ,
and to keep the region inside S(V). Let Δ(V) be the supremum over S(V) of the Euclidean operator norm of g_λ⁻¹ −
g0⁻¹ on covectors, weighted by t^(3/2) on P (where ψ′ = t^(−3/2); ψ′ = 1 on Ω). Since g0⁻¹(dv, dv) = 0, g0⁻¹(dv,
dτ) = −1 and g0⁻¹(dτ, dτ) = −(1 + μ/r²), g0⁻¹(α, α) = −2eψ′ − e²ψ′²(1 + μ/r²); and α = (1 + eψ′) dτ + x̂·dx has the
Euclidean norm |α|_e² ≤ 13/4 for eψ′ ≤ 1/2. So for every e with 2Δ(V) ≤ e ≤ 2C1λ (resp. 2C_Pλ), g_λ⁻¹(α, α) ≤ ψ′(−2e + (13/4) Δ(V))
< 0, and the proofs run on R(V, e) := S(V) ∩ {v + eψ(τ) ≤ V} with the same constants (the slices still shrink), and so
does their form with four derivatives in step (2) of [[lem:edge-degree-two]]. Every boundary point X with v(X) + e
ψ_max ≤ V lies in R(V, e), so the bound holds there with reach e ψ_max.

(2) *Stage 0* is [[lem:layer-remainder]] (case Ω; |w| ≤ C λ^(N−5) ε_(M*)) or [[lem:layer-remainder-past]] (case P;
there |w| ≤ C λ^(N_P−3) ε_(M_P)) itself, with e_0 := 2C1λ (resp. 2C_Pλ) and reach e_0 ψ_max. Let y_0 be the depth at which
κ(v_s + y_0) e_0 ψ_max = 1; by [[lem:edge-kappa]] (a), κ is nonincreasing and tends to ∞ at v_s, so y_0 exists for λ
small, and y_0 → 0 as λ → 0. At depths x ≥ y_0 the reach of stage 0 is at most 1/κ(v). By [[lem:edge-kappa]] (a),
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

