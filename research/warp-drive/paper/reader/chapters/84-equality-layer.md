## The boundary at equality, I: the seed region and the layer {#ch:equality-layer}

This chapter treats the curvature boundary x_K = 1 of [[thm:main]] when the seed sits exactly at the threshold, μ0 =
√72 l5². There the margin of [[prop:boundary-spacelike]] vanishes before the shell, and the boundary is the seed's
horizon. We show that g_λ is the seed exactly on {v ≤ v_s}, v_s := inf supp env; that the boundary is spacelike for
g_λ on {v ≥ v_s + η} once λ is small; that a domain within O(λ) of D_T has an inner boundary which no future causal
curve enters; and that the spheres' horizon holds in a form valid at equality. In the layer v_s < v < v_s + η_λ
between, whose width tends to zero with λ, the boundary is not spacelike throughout: [[thm:layer]] shows that on every
column it has points where it is timelike for g_λ, alternating with points where it is spacelike on the scale of the
wavelength, and [[cor:layer]] draws the consequence that future timelike curves cross it into D_T. The mechanism is
the part of g_λ⁻¹(dΦ0, dΦ0) of first degree in the waves: its terms of order λ and λ² vanish identically, and its
term of order λ³ is a first harmonic of the phase that exceeds the margin near the edge of the envelope. The same
holds for the solutions of [[thm:past-construction]] ([[thm:layer-past]]). The last sections decide the boundary's
character in most of the rest of the layer ([[prop:layer-regions]]): for fixed δ ∈ (0, 1/2] and P > 4, where the
level sup_(v′≤v) |env(v′)| is at least λ^(3−δ), near every point where it first reaches a value between λ^P and
λ^(3+δ), and, in the band between, wherever the ratio of the first-degree term to the margin is not within 2λ^(1/10)
of 1. They also give the structure of the expansion in λ ([[prop:layer-structure]]) and write the threshold λ_L of
[[thm:layer]] as an explicit formula. The very edge of the layer is the subject of [[ch:equality-edge]].

Throughout, μ0 = √72 l5², and the notation is that of [[ch:setting]], [[ch:approximant]], [[ch:inequalities]],
[[ch:uniform-existence]] and [[ch:data]]. The phase is θ and the polar angle of S³ is ϑ.

### The setting at equality {#sec:eq-setting}

In the coordinates (v, r, ϑ, φ1, φ2) of [[eq:vr-form]],

    g0 = −F dv² + 2 dv dr + r² γ,      F := 1 − μ(v)/r²,                                              {#eq:eq-g0}

F being the function f of [[eq:vr-form]], and μ(v) = μ0 + (2/9) A² ∫_(−∞)^v env², so μ′ = (2/9) A² env² ≥ 0
([[eq:mu-rate]]). Since √72 l5² = μ0, the curvature boundary is r = r_q(v) with

    r_q(v) = (μ0 μ(v))^(1/4),      Φ0 := r − r_q(v),

and the boundary is {Φ0 = 0}. Put v_s := inf supp env. Then v_s ≥ v_start and μ = μ0 on {v ≤ v_s}.

*The construction depends on v_start only through the support of env.* The hypotheses of [[thm:main]] hold with
v_start replaced by v_s: env ∈ C_c^∞([v_s, v_end]), μ = μ0 on {v ≤ v_s}, and v_s − τ0 ≥ v_start − τ0 > √μ0 + 1. The
domain Ω of [[eq:omega]] and the constants λ0, C of [[thm:main]] do not involve v_start. The stage data of
[[lem:stage-data]] and the correction U of [[prop:exact-correction]] are solved outward in r from zero data at r = a,
with forcing terms that vanish where the earlier stages and the waves vanish, and every stage of the approximant
vanishes on {v ≤ v_s}; both facts are contained in the bounds of [[lem:layer-flat]] below, whose right sides carry a
factor ε_c(v), zero for v ≤ v_s. So the metric g_λ of [[thm:main]] is the same whether v_start or v_s is used, and λ0,
C and Ω are its constants and domain. Its data on Σ_τ0 ∩ {r < v_s − τ0} are those of the seed, as a metric together
with its first τ-derivative, and not only as Cauchy data: there U = 0 and the approximant is g0, the lapse and shift of
g_λ are those of G(X, u/λ), which is g0 there, and the τ-derivatives of lapse and shift are fixed by D(g) = 0 with
invertible coefficient ([[sec:data-proof]]), which g0 satisfies.

By items 4 and 5 of [[thm:main]], |g_λ − g0| ≤ C λ, D(g_λ) = 0 and Ric(g_λ) = 0 on Ω. Since g0⁻¹ is bounded on the
compact Ω and inversion is smooth, after shrinking λ0 so that C λ0 ≤ 1 there is C1 with

    |(g_λ⁻¹ − g0⁻¹)(α, α)| ≤ C1 λ |α|_e²     on Ω, for every covector α,                                {#eq:eq-c1}

|α|_e the Euclidean norm of the Cartesian components of α. The vector field Y := −g0⁻¹ dτ is uniformly timelike for
g0 on Ω, and, λ0 being shrunk once more, future timelike for g_λ. Put B := 1 + sup |r_q′|, the supremum over the
v-range of D_T. For a covector α = dr − β dv with |β| ≤ B, the Cartesian components are α = −β dτ + (1 − β) x̂·dx,
since dv = dτ + x̂·dx and dr = x̂·dx, so |α|_e² = β² + (1 − β)² ≤ B² + (1 + B)², and by [[eq:eq-c1]]

    |g_λ⁻¹(α, α) − g0⁻¹(α, α)| ≤ C_Φ λ,      C_Φ := C1 (B² + (1 + B)²).                                 {#eq:eq-c-phi}

**Lemma {#lem:eq-seed}** (g0 at equality.) (a) For Φ = r − ρ(v), on {r = ρ}, g0⁻¹(dΦ, dΦ) = F(ρ) − 2ρ′. For ρ = r_q
this is [[eq:boundary-margin]], and

    m0(v) := −g0⁻¹(dΦ0, dΦ0) = √(μ/μ0) − 1 + r_q μ′/(2μ),      2 r_q′ = r_q μ′/(2μ).                      {#eq:eq-margin}

(b) m0 = 0 on {v ≤ v_s}, m0 > 0 on {v > v_s}, and m0 ≥ δ_η := √(μ(v_s + η)/μ0) − 1 > 0 on {v ≥ v_s + η}, for η > 0.

(c) m0 and all its derivatives vanish at v = v_s.

(d) For every future causal vector X of g0, dv(X) ≥ 0 and dr(X) ≤ (F/2) dv(X).

(e) Y = −g0⁻¹ dτ is future timelike for g0, and for Φ = r − ρ(v), dΦ(Y) = −μ/r² − ρ′; so dΦ(Y) < 0 when ρ′ ≥ 0.

*Proof.* (a) The inverse of [[eq:eq-g0]] has g0^(vv) = 0, g0^(vr) = 1 and g0^(rr) = F, so for dΦ = dr − ρ′ dv,
g0⁻¹(dΦ, dΦ) = F − 2ρ′. At equality μ/r_q² = μ/(μ0 μ)^(1/2) = (μ/μ0)^(1/2), so F(r_q) = 1 − √(μ/μ0), and r_q′ =
(1/4)(μ0 μ)^(−3/4) μ0 μ′ = r_q μ′/(4μ).

(b) On {v ≤ v_s}, μ = μ0 and μ′ = 0, so m0 = 0. For v > v_s, env does not vanish identically on (v_s, v): otherwise
env = 0 on the open set (−∞, v), and v_s ∉ supp env. So μ(v) − μ0 = (2/9) A² ∫_(v_s)^v env² > 0. As μ′ ≥ 0, μ is
nondecreasing, and m0(v) ≥ √(μ(v)/μ0) − 1 ≥ δ_η for v ≥ v_s + η.

(c) env vanishes on (−∞, v_s), so env and all its derivatives vanish at v_s; hence so do μ − μ0, μ′ and all their
derivatives, and with them every derivative of m0.

(d) Write X = X^v ∂_v + X^r ∂_r + X_ang. Then g0(X, X) = −F (X^v)² + 2 X^v X^r + r² |X_ang|²_γ ≤ 0, and
dτ(X) = X^v − X^r > 0, since dτ = dv − dr and X is future directed. If X^v = 0, then |X_ang| = 0 and X^r < 0. If
X^v < 0, then X^r < X^v < 0, so 2 X^v X^r > 2 (X^v)² > F (X^v)², as F < 1, and g0(X, X) > 0, a contradiction. So
X^v ≥ 0, with X^v = 0 only for X a positive multiple of −∂_r; and for X^v > 0 the inequality 2 X^v X^r ≤ F (X^v)² gives
X^r ≤ F X^v/2. The bound is attained by the outgoing null direction ∂_v + (F/2) ∂_r.

(e) By [[prop:vaidya]] (d), g0⁻¹(dτ, dτ) = −1 − μ/r² < 0, so Y is timelike, and dτ(Y) = 1 + μ/r² > 0. With
g0⁻¹(dτ, dr) = μ/r² and g0⁻¹(dτ, dv) = −1 ([[lem:domain]] (c)), dΦ(Y) = −g0⁻¹(dτ, dr) + ρ′ g0⁻¹(dτ, dv) = −μ/r² − ρ′. ∎

### The seed region is exact {#sec:eq-seed-region}

**Proposition {#prop:eq-seed-region}** (The seed region.) g_λ = g0 on Ω ∩ {v ≤ v_s}. In particular g_λ − g0 and all
its derivatives vanish on Ω ∩ {v = v_s}, and on Ω ∩ {v ≤ v_s} the metric g_λ is the five-dimensional
Schwarzschild–Tangherlini metric of mass μ0, the seed.

*Proof.* Let R := Ω ∩ {v ≤ v_s}, a compact set, and u := g_λ − g0 on R. On R, μ′ = 0, so Ric(g0) = 0, and Ric^H(g0) =
Ric(g0) = 0 since D(g0) = 0 ([[sec:gauge]]). D(g_λ) = 0 and Ric(g_λ) = 0 give Ric^H(g_λ) = 0. Subtracting the
equations [[eq:gauge]] for the two metrics,

    −(1/2) g0^(ab) ∂_a ∂_b u = (1/2)(g_λ^(ab) − g0^(ab)) ∂_a ∂_b g_λ − Q(X; g_λ)(∂g_λ, ∂g_λ) + Q(X; g0)(∂g0, ∂g0) =: f.

Here g_λ⁻¹ − g0⁻¹ = −g_λ⁻¹ u g0⁻¹, and Q is a polynomial in ∂g with coefficients rational in g and smooth in X. Writing
the difference of the Q-terms as ∫_0^1 (d/ds) Q(X; g0 + s u)(∂(g0 + s u), ∂(g0 + s u)) ds, with g0 + s u Lorentzian
and in a compact set for λ ≤ λ0 (|u| ≤ C λ), gives |f| ≤ K_λ (|u| + |∂u|) on R, with K_λ finite for each λ, since ∂²g_λ
is bounded on the compact R.

The data vanish: Σ_τ0 ∩ R = {τ = τ0, a ≤ r ≤ v_s − τ0}, where (g_λ, ∂_τ g_λ) = (g0, ∂_τ g0) for r < v_s − τ0
([[sec:eq-setting]]) and, by continuity, at r = v_s − τ0. Run the proof of [[lem:energy]] on R in place of Ω, with
g̃ := g0 and the multiplier Y = −g0⁻¹ dτ. The boundary of R ∩ {τ0 ≤ τ′ ≤ τ} consists of Σ_τ0 ∩ R, Σ_τ ∩ R, parts of
∂Ω other than Σ_τ0, which are spacelike with Ω, hence R, to their past ([[lem:domain]]), and a part of the hypersurface
{v = v_s}. That part is null for g0 (dv is null, [[prop:vaidya]] (c)), and R lies to its past, since v does not
decrease along future causal curves ([[lem:eq-seed]] (d)). The flux of the energy current J = T(Y, ·) through it is
∫ T(Y, N) ≥ 0, N its future null generator, by the dominant energy property of T_ab = ∂_a u ∂_b u − (1/2) g0_ab
g0(du, du) for the future causal vectors Y and N; so this flux is dropped, as the fluxes through the spacelike parts
are. The slice R ∩ Σ_τ is {a ≤ r ≤ v_s − τ}, since R does not meet the outer face of Ω, and its outer radius decreases
with τ, so the boundary term in ∂_τ ‖u‖² is at most 0. Hence [[eq:energy]] holds on R:

    ‖∂u(τ)‖ + ‖u(τ)‖ ≤ C (‖∂u(τ0)‖ + ‖u(τ0)‖ + ∫_(τ0)^τ ‖f‖) ≤ C K_λ ∫_(τ0)^τ (‖∂u‖ + ‖u‖),

the norms on R ∩ Σ_τ, and Gronwall's inequality gives u = 0 on R. The derivatives of u vanish on Ω ∩ {v = v_s} because
u is smooth on Ω and vanishes on Ω ∩ {v < v_s}, whose closure contains Ω ∩ {v = v_s}. ∎

So g_app = g0 and w = 0 on R. Here the principal part of the difference equation is g0 and the face {v = v_s} is
exactly null for it, so no tilt of that face is needed.

### The boundary {#sec:eq-boundary}

**Proposition {#prop:eq-boundary}** (The boundary at equality.) (a) On {v ≤ v_s} the boundary {Φ0 = 0} is {r = √μ0},
the seed's horizon, null for g_λ. A future causal curve of g_λ that starts in {r ≤ √μ0} stays there while v ≤ v_s:
nothing crosses this portion from inside to outside.

(b) For η > 0 put λ_η := min(λ0, δ_η/(2 C_Φ)). For λ ≤ λ_η the boundary is spacelike for g_λ on {v ≥ v_s + η}, with
g_λ⁻¹(dΦ0, dΦ0) ≤ −δ_η/2, and every future causal curve of g_λ that meets it there leaves D_T there.

(c) For each λ, the portion of the boundary on which these bounds do not decide its causal character lies in the
*layer* v_s < v < v_s + η_λ, where η_λ := inf{η > 0 : δ_η ≥ 2 C_Φ λ}, that is μ(v_s + η_λ) = μ0 (1 + 2 C_Φ λ)²; and
η_λ → 0 as λ → 0.

*Proof.* (a) By [[prop:eq-seed-region]], g_λ = g0 there; r_q = √μ0 since μ = μ0, and [[eq:eq-margin]] gives m0 = 0:
the boundary is null. By [[lem:eq-seed]] (d), along a future causal curve in Ω ∩ {v ≤ v_s}, dr ≤ (F/2) dv with dv ≥ 0
and F = 1 − μ0/r² < 0 for r < √μ0. So where r < √μ0, r does not increase, and a curve from {r < √μ0} stays in {r ≤
r(start)}. From a point with r = √μ0, put f := r − √μ0; where f > 0 and f is small, F ≤ 2f/√μ0, so df ≤ (f/√μ0) dv,
and f₊ e^(−v/√μ0) does not increase along the curve. It starts at 0, so f ≤ 0 while v ≤ v_s.

(b) For v ≥ v_s + η, by [[eq:eq-c-phi]] with β = r_q′ and [[lem:eq-seed]] (b), g_λ⁻¹(dΦ0, dΦ0) ≤ −m0 + C_Φ λ ≤ −δ_η +
δ_η/2. A covector timelike for g_λ has one sign on the future causal cone of g_λ, and the sign is that of dΦ0(Y) < 0
([[lem:eq-seed]] (e), with ρ′ = r_q′ ≥ 0; Y is future timelike for g_λ). So Φ0 decreases strictly along every future
causal curve near that portion of the boundary, and a future causal curve that meets it there leaves D_T = {Φ0 ≥ 0} ∩
{v ≤ v_end + T}.

(c) δ_η is continuous, nondecreasing in η, and tends to 0 as η ↓ 0, because μ is continuous and nondecreasing with
μ(v_s) = μ0. So η_λ is well defined once 2 C_Φ λ ≤ δ_η at η = v_end − v_s, which λ ≤ λ0 may be assumed to give, and
η_λ → 0 as λ → 0. ∎

**Proposition {#prop:eq-domain}** (A domain whose inner boundary nothing enters.) Put κ* := 2 μ(v_end)^(1/4)/μ0^(3/4),
η* := 1/κ*, c_σ := 2 C_Φ, and for λ ≤ λ* := min(λ0, 1/c_σ, δ_(η*)/(6 C_Φ))

    σ_λ(v) := c_σ λ min((v − v_s)₊, η*),      D_T^λ := {v ≤ v_end + T, r ≥ r_q(v) + σ_λ(v)}.            {#eq:eq-domain}

Then D_T^λ ⊂ D_T ⊂ {x_K ≤ 1}, D_T ∖ D_T^λ ⊂ {r_q(v) ≤ r < r_q(v) + c_σ λ η*}, and no future causal curve of g_λ in Ω
enters D_T^λ through its inner boundary {Φ_σ = 0}, Φ_σ := r − r_q(v) − σ_λ(v). The portion of that boundary on {v ≤ v_s}
is the seed's horizon ([[prop:eq-boundary]] (a)), and on {v > v_s} it is spacelike for g_λ, uniformly on
{v ≥ v_s + η*}.

*Proof.* Since σ_λ′ ≤ c_σ λ ≤ 1, B bounds |r_q′ + σ_λ′|, so [[eq:eq-c-phi]] applies to dΦ_σ. On the pieces where σ_λ
is smooth, [[lem:eq-seed]] (a) with ρ = r_q + σ, σ := σ_λ, gives at Φ_σ = 0

    g0⁻¹(dΦ_σ, dΦ_σ) = F(ρ) − 2 r_q′ − 2σ′ = −m0(v) + μ (1/r_q² − 1/ρ²) − 2σ′ ≤ −m0(v) + κ* σ − 2σ′.   {#eq:eq-sigma}

Indeed 1/r_q² − 1/ρ² = σ(ρ + r_q)/(r_q² ρ²) ≤ 2σ/r_q³, since (ρ + r_q)/ρ² ≤ 2/ρ ≤ 2/r_q; and at equality 2μ/r_q³ =
2μ/(μ0 μ)^(3/4) = 2 μ^(1/4)/μ0^(3/4) ≤ κ*. On v_s < v < v_s + η*: σ′ = c_σ λ and κ* σ ≤ κ* c_σ λ η* = c_σ λ, so
g_λ⁻¹(dΦ_σ, dΦ_σ) ≤ −m0 + c_σ λ − 2 c_σ λ + C_Φ λ = −m0 − C_Φ λ ≤ −C_Φ λ. On v > v_s + η*: σ′ = 0 and κ* σ = c_σ λ, so
g_λ⁻¹(dΦ_σ, dΦ_σ) ≤ −δ_(η*) + 2 C_Φ λ + C_Φ λ ≤ −δ_(η*)/2, by λ ≤ δ_(η*)/(6 C_Φ). On v ≤ v_s, σ = 0 and
[[prop:eq-boundary]] (a) applies.

*No entry.* Let γ be a future causal curve of g_λ in Ω with Φ_σ < 0 at its start and Φ_σ ≥ 0 at some later parameter;
let s* be the first such parameter and p := γ(s*), so Φ_σ(p) = 0 and Φ_σ < 0 on γ before s*. Each smooth piece of Φ_σ,
extended a little past its v-interval, keeps a g_λ-timelike differential near p when v(p) > v_s, by continuity of the
margins above, with dΦ(Z) < 0 for future causal Z (the sign of dΦ(Y), [[lem:eq-seed]] (e)). Near the corner v = v_s +
η*, Φ_σ is the larger of its two pieces; near v = v_s, r = √μ0, it is the smaller of Φ0 and Φ1 := Φ0 − c_σ λ (v −
v_s). If v(p) > v_s: the maximum of two functions strictly decreasing along γ near p is strictly decreasing, so
Φ_σ(γ(s)) > 0 for s < s* close to s*, a contradiction. If v(p) < v_s: γ cannot pass from {v > v_s} into {v < v_s},
since on {v ≤ v_s}, where g_λ = g0, v does not decrease ([[lem:eq-seed]] (d)); so γ lies in {v < v_s} on an interval
before s*, where Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there ([[prop:eq-boundary]] (a)): r(p) < √μ0,
a contradiction. If v(p) = v_s: g_λ⁻¹(dΦ1, dΦ1) = −2 c_σ λ < 0 at p (m0 = 0, σ = 0 and g_λ = g0 there), so Φ1
decreases strictly along γ near p. Points of γ before p with v > v_s would have Φ_σ = Φ1 > Φ1(p) = 0, which is
impossible; so γ approaches p within {v ≤ v_s}, where Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there:
r(p) < √μ0, a contradiction. ∎

The statement concerns the inner boundary only; the face {v = v_end + T} of D_T^λ is not treated.

**Remark {#rem:eq-why-layer}** (What the bounds of [[thm:main]] leave open.) On v_s < v < v_s + η_λ the margin m0 and
the perturbation g_λ⁻¹ − g0⁻¹ both vanish to every order at v = v_s ([[lem:eq-seed]] (c), [[prop:eq-seed-region]]).
[[thm:main]] bounds the perturbation by C λ, uniformly in v, while deciding the sign of g_λ⁻¹(dΦ0, dΦ0) needs a bound by
a fraction of m0, pointwise in v near v_s. The sections from [[sec:layer-setting]] on obtain the part of the
perturbation of first degree in the waves exactly and bound the rest by the margin's own order.

### The spheres' horizon at equality {#sec:eq-horizon}

Let C_θ be the constant C3 of [[eq:theta-plus-close]] in the proof of [[prop:one-zero]], so that on the columns the
functions θ⁺_λ − θ⁺_0 and ∂_r(θ⁺_λ − θ⁺_0) are at most C_θ λ in absolute value, θ⁺_0 := θ⁺(g0); let R_max be the
largest r on the columns, c_θ := 3/(R_max² + μ(v_end)), and C_h := C_θ/c_θ.

**Proposition {#prop:eq-horizon}** (The spheres' horizon at equality.) Let K ≥ 6 and λ ≤ λ_H ([[prop:one-zero]]), λ
small.

(a) On every column (v and x̂ fixed, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero, positive above it and negative
below; every zero lies within C_h λ of √μ(v); the spheres with r ≥ √μ(v) + C_h λ are untrapped and those with r_q(v)
≤ r ≤ √μ(v) − C_h λ are trapped.

(b) On the columns with v ≤ v_s, θ⁺_λ = θ⁺_0 exactly: its one zero is r = √μ0, the lower end of the column on the
boundary, and every sphere of the column above it is untrapped.

(c) On the columns that reach across √μ(v) + C_h λ and have √μ(v) − r_q(v) ≥ C′ λ, for any C′ > C_θ μ(v_end)/3,
θ⁺_λ has exactly one zero.

*Proof.* By [[eq:round-expansions]], θ⁺_0 = 3(r² − μ)/(r(r² + μ)), so |θ⁺_0(r)| = 3 |r − √μ| (r + √μ)/(r(r² + μ)) ≥
c_θ |r − √μ| on the column, as (r + √μ)/r ≥ 1. (a) θ⁺_λ ≥ c_θ (r − √μ) − C_θ λ > 0 for r > √μ + C_h λ, and θ⁺_λ ≤
−c_θ (√μ − r) + C_θ λ < 0 for r < √μ − C_h λ. Near √μ, ∂_r θ⁺_0 = 3/μ at r = √μ, so ∂_r θ⁺_0 ≥ 3/(2μ(v_end)) on a fixed
neighbourhood of √μ, which contains [√μ − C_h λ, √μ + C_h λ] for λ small; there ∂_r θ⁺_λ ≥ 3/(2μ(v_end)) − C_θ λ > 0.
So θ⁺_λ has at most one zero, with the signs stated. Nothing in this uses r_q < √μ. (b) is [[prop:eq-seed-region]]: on
Ω ∩ {v ≤ v_s}, g_λ = g0. (c) With d_h := √μ − r_q ∈ [0, √μ], the identity

    −θ⁺_0(r_q) − 3 d_h/μ = 3 d_h² (μ + √μ r_q + r_q²)/(μ r_q (μ + r_q²))

holds: −θ⁺_0(r_q) = 3 d_h (√μ + r_q)/(r_q (r_q² + μ)), and (√μ + r_q) μ − r_q (r_q² + μ) = μ√μ − r_q³ =
d_h (μ + √μ r_q + r_q²). The right side is nonnegative, so θ⁺_λ(r_q) ≤ −3 d_h/μ + C_θ λ ≤ −3 C′ λ/μ(v_end) + C_θ λ < 0,
while θ⁺_λ > 0 at √μ + C_h λ; the intermediate value theorem and (a) give exactly one zero. ∎

So at equality item 6 of [[thm:main]] holds in this form: exactly one zero on the columns with v ≤ v_s (at the boundary
itself) and on those with √μ(v) − r_q(v) ≥ C′ λ, a condition that fails only on a set of v whose width tends to 0 with
λ; at most one zero, within C_h λ of √μ(v), everywhere.

### The layer: setting {#sec:layer-setting}

We use the coordinates (v, r, ϑ, φ1, φ2) of [[eq:eq-g0]]; there ∂_v is the Cartesian ∂_τ (v = τ + r) and ℓ = g0⁻¹ dv =
∂_r ([[sec:stage-zero]]). Put

    Φ0♯ := g0⁻¹ dΦ0 = ∂_v + β_Φ ∂_r,      β_Φ := F(r_q) − r_q′ = 1 − √(μ/μ0) − r_q μ′/(4μ).

The hypersurface {Φ0 = 0} is timelike at a point exactly when dΦ0 is spacelike there, g_λ⁻¹(dΦ0, dΦ0) > 0. The *seed*
is g0° := g0 with μ replaced by μ0, the Schwarzschild–Tangherlini metric of mass μ0; it is vacuum, and g0 = g0° on
{v ≤ v_s}.

The metric g_λ of [[thm:main]] is g_app + w, with g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j], N = K + 3, the
fixed-phase form of [[thm:approximant]] built with the stage data of [[lem:stage-data]] (stage N's included). Write
k := g_λ − g0 and, for an integer c ≥ 0,

    E(v) := sup_(v′≤v) |env(v′)|,      ε_c(v) := Σ_(i≤c) sup_(v′≤v) |env^(i)(v′)|,                   {#eq:layer-costs}

both continuous, nondecreasing and zero for v ≤ v_s. E is the *level* of the envelope, and E = ε_0; no sign of env is
assumed. A quantity is *of degree at least two* if, with μ − μ0 counted as of degree two, it is a sum of products of at
least two factors of the form A env^(i) times smooth coefficients. A profile H(v, r, ϑ) e^(iθ), H complex, is the
complex form of a first harmonic of the phase, and its real part is meant.
We write ĝ_1 := W = W_TT + χ dv ⊗ dv, so that the oscillating profiles of the ansatz [[eq:ansatz]] are ĝ_1, …, ĝ_(N+1).

**Definition {#def:layer-class}** (The class 𝔖.) A symmetric 2-tensor h, invariant under T² and both reflections, is
in the class 𝔖 if h_vv = h_vr = h_rr = 0 and γ^(AB) h_AB = 0, A, B running over the angular coordinates. Its remaining
components are h_vϑ, h_rϑ and the γ-traceless angular ones; every h in 𝔖 has tr_(g0) h = 0.

Put v_♯ := v_s + min(1, T). For v ≤ v_♯ let Ω_v := Ω ∩ {v′ ≤ v} and N_v := Ω ∩ {v′ = v}. On Ω ∩ {v ≤ v_♯} the outer
face of Ω is not met, since there v = V + 1 + τ_end − τ ≥ V + 1. N_v is null for g0 (dv is null, [[prop:vaidya]] (c)),
and Ω_v lies to its past ([[lem:eq-seed]] (d)). For X ∈ Ω let γ_X be the integral curve of ℓ from X: in (v, r, x̂) it
is r ↦ (v(X), r, x̂(X)), r ≥ r(X), and it meets Σ_τ0 at X_Σ := (v(X), v(X) − τ0, x̂(X)) inside Ω ([[lem:domain]] (d)).
Since v is constant along γ_X, every bound weighted by ε_c(v) holds with the same weight along the whole curve.

*Constants.* In this and the following sections C denotes a constant depending on N, the order of differentiation, Ω
(through a, δ0, b(τ0) and τ_end − τ0), μ0, A, finitely many norms sup |env^(i)|, the bounds of the profiles of
[[thm:approximant]] and of the stage data of [[lem:stage-data]] on Ω × S¹ (each smooth with all derivatives bounded
independently of λ), the constants of [[thm:uniform-existence]] and of Step 1 of its proof, and C1 of [[eq:eq-c1]];
never on λ, v, v1 or the point.

### The seed's operators on one harmonic {#sec:layer-operators}

In (v, r, ϑ, φ1, φ2), with F° := 1 − μ0/r² and Γ̊ the Christoffel symbols of the round metric γ, the Christoffel
symbols of g0° that do not vanish are

    Γ^v_vv = μ0/r³,   Γ^r_vv = F° μ0/r³,   Γ^r_rv = −μ0/r³,   Γ^v_AB = −r γ_AB,   Γ^r_AB = −r F° γ_AB,
    Γ^A_rB = δ^A_B/r,   Γ^A_BC = Γ̊^A_BC;                                                         {#eq:layer-christoffel}

in particular Γ^A_(av) = 0 for every index a, and Γ^v_(rv) = Γ^v_(rr) = Γ^r_(rr) = 0. Each is read from Γ^σ_ab = (1/2)
g^(σd)(∂_a g_db + ∂_b g_da − ∂_d g_ab) with g_vv = −F°, g_vr = 1, g_rr = 0, g_AB = r² γ_AB and g^vv = 0, g^vr = 1,
g^rr = F°; for instance Γ^r_rv = (1/2) ∂_r g_vv = −μ0/r³ and Γ^v_AB = −(1/2) ∂_r g_AB.

For a symmetric 2-tensor h let

    Pol(h) := h(ℓ, ·) − (1/2) dv tr h,      D_X(h) := div h − (1/2) d tr h,      𝒯 h := −i (∇_ℓ h + (3/(2r)) h),
    R_X(h) := −(1/2) □h + 𝔚(h),      𝔚(h)_mn := −R_m^a_n^b h_ab,                                    {#eq:layer-operators}

∇, □ = ∇^a ∇_a, div, tr and the Riemann tensor R being those of g0°, indices moved by g0°.

**Lemma {#lem:layer-seed-operators}** (The seed's operators.) Let dRic^H and dD be the linearisations at g0° of Ric^H and
D, with the gauge taken relative to g0° ([[sec:gauge]]). Let H be a symmetric 2-tensor whose components in (v, r, ϑ,
φ1, φ2) are functions of (v, r, ϑ) and with H_(vφi) = H_(rφi) = H_(ϑφi) = H_(φ1φ2) = 0, and let k ≥ 1 be an integer.

(a) dRic^H(h) = −(1/2) □h + 𝔚(h) and dD(h) = div h − (1/2) d tr h, the latter with its index lowered.

(b) dRic^H(H e^(ikv/λ)) = e^(ikv/λ) (λ⁻¹ k 𝒯H + R_X H) and dD(H e^(ikv/λ)) = e^(ikv/λ) (λ⁻¹ i k Pol(H) + D_X H): there
is no term of order λ⁻².

(c) Componentwise, with Λ := 3/(2r),

    (𝒯H)_vv = −i(∂_r H_vv + Λ H_vv + 2μ0 H_vr/r³),     (𝒯H)_vr = −i(∂_r H_vr + Λ H_vr + μ0 H_rr/r³),
    (𝒯H)_rr = −i(∂_r + Λ) H_rr,      (𝒯H)_vϑ = −i(∂_r H_vϑ + H_vϑ/(2r) + μ0 H_rϑ/r³),
    (𝒯H)_rϑ = −i(∂_r + 1/(2r)) H_rϑ,      (𝒯H)_AB = −i(∂_r − 1/(2r)) H_AB   (A, B angular);
    Pol(H)_v = −(1/2)(F° H_rr + r⁻² γ^(AB) H_AB),   Pol(H)_r = H_rr,   Pol(H)_ϑ = H_rϑ.            {#eq:layer-components}

(d) If h is in 𝔖, then (dRic^H h)_vv = 0 and tr dRic^H h = 0; the same holds for R_X h.

(e) If h has only angular components, then (□h)_vA = 0 and 𝔚(h)_vA = 0 for every angular A.

*Proof.* (a) At a vacuum metric, with D(g0°) = 0 and the gauge relative to g0°, the variation of the Christoffel symbols
is δΓ^ρ_ab = (1/2)(∇_a h^ρ_b + ∇_b h^ρ_a − ∇^ρ h_ab), so dD^ρ = g0°^(ab) δΓ^ρ_ab = ∇_a h^(aρ) − (1/2) ∇^ρ tr h. The
variation of Ricci is ∇_ρ δΓ^ρ_mn − ∇_n δΓ^ρ_(ρm). Commuting the derivatives in ∇_ρ ∇_m h^ρ_n by the Ricci identity, and
using Ric(g0°) = 0, it equals (1/2)(∇_m dD_n + ∇_n dD_m) − (1/2) □h_mn − R_m^a_n^b h_ab. The variation of the gauge term
of [[eq:gauge]] at D = 0 is (1/2)(∇_m dD_n + ∇_n dD_m), since ∇̂ = ∇ at g0°. The difference is (a).

(b) For h = H e^(ikv/λ), ∇_a h = (∇_a H + i k λ⁻¹ (∂_a v) H) e^(ikv/λ), and g0°⁻¹(dv, dv) = 0 ([[prop:vaidya]] (c)) and
□v = 3/r ([[sec:stage-zero]]). Hence

    □(H e^(ikv/λ)) = e^(ikv/λ) (□H + i k λ⁻¹ (2 ∇_ℓ H + (3/r) H)),

with no λ⁻² term, and the zeroth-order term 𝔚 and the first-order dD are expanded in the same way; dD(h) has λ⁻¹ part
i k (H(ℓ, ·) − (1/2) dv tr H). This is (b).

(c) For an angular index A, B, and a, b ∈ {v, r}, (∇_ℓ H)_ab = ∂_r H_ab − Γ^c_(ra) H_cb − Γ^c_(rb) H_ac. By
[[eq:layer-christoffel]] the only symbols with a lower index r are Γ^r_rv = −μ0/r³ and Γ^A_rB = δ^A_B/r. So (∇_ℓ H)_vv =
∂_r H_vv + 2μ0 H_vr/r³, (∇_ℓ H)_vr = ∂_r H_vr + μ0 H_rr/r³, (∇_ℓ H)_rr = ∂_r H_rr, (∇_ℓ H)_vϑ = ∂_r H_vϑ + μ0 H_rϑ/r³ −
H_vϑ/r, (∇_ℓ H)_rϑ = ∂_r H_rϑ − H_rϑ/r and (∇_ℓ H)_AB = ∂_r H_AB − 2 H_AB/r; adding (3/(2r)) H gives the list. For Pol,
H(ℓ, ·) = H(∂_r, ·), and tr H = 2 H_vr + F° H_rr + r⁻² γ^(AB) H_AB, since g0°^(vv) = 0, g0°^(vr) = 1, g0°^(rr) = F°.

(d) The component (𝔚 h)_vv is −R_(vavb) h^(ab). For h in 𝔖 the raised components h^(vv), h^(vr), h^(rr) vanish (they
are built from h_rr, h_vr, h_vv through g^vv = 0), so only h^(vA), h^(rA), h^(AB) remain. g0° is a warped product of
the (v, r) plane with the round S³, invariant under O(4) acting on the spheres; at a point, the isotropy group O(3)
acts on the angular indices, and −1 ∈ O(3) changes the sign of a component with an odd number of angular indices. So
R_(vvvA) = R_(vrvA) = 0, and R_(vAvB) is an O(3)-invariant bilinear form on the tangent space of the sphere, a multiple
of γ_AB. Hence (𝔚 h)_vv = −R_(vAvB) h^(AB) = 0, since h^(AB) is γ-traceless. For □: (∇_b h)_vv = ∂_b h_vv − 2 Γ^c_(bv)
h_cv = −2 Γ^A_(bv) h_Av = 0, and (∇_b h)_rv = −Γ^A_(br) h_Av − Γ^A_(bv) h_rA, which vanishes for b ∈ {v, r}. Then
(∇_a ∇_b h)_vv = −2 Γ^c_(av) (∇_b h)_cv, since (∇h)_vv vanishes identically. The symbols Γ^c_(av) vanish unless a and
c lie in {v, r}, and then g0°^(ab) ≠ 0 forces b ∈ {v, r}, where (∇_b h)_vv = (∇_b h)_rv = 0. So (□h)_vv = 0.
For the trace: g0° is parallel, so tr □h = □ tr h = 0 for h in 𝔖, and tr 𝔚(h) = −Ric(g0°)^(ab) h_ab = 0. These are
statements about every h in 𝔖, so they hold for dRic^H(h) and, applied to H e^(iv/λ) with H in 𝔖, order by order in λ:
for R_X H as well as for 𝒯H.

(e) By the same parity, (𝔚h)_vA = −R_(vBAC) h^(BC) = 0, three of its four indices being angular. For h with only angular
components, (∇_c h)_(vA) = −Γ^E_(cv) h_EA = 0 for every c; (∇_b h)_(vv) = (∇_b h)_(vr) = 0; and (∇_b h)_(rA) =
−Γ^E_(br) h_EA vanishes unless b is angular. In (∇_a ∇_b h)_vA = −Γ^d_(av) (∇_b h)_dA − Γ^d_(aA) (∇_b h)_vd every term
then vanishes after contraction with g0°^(ab): the first because Γ^d_(av) ≠ 0 only for a ∈ {v, r}, where g^(ab) has no
angular b, and the second because (∇_b h)_vd = 0. So (□h)_vA = 0. ∎

Write R_X H also for the λ⁰ part of dRic^H(H e^(iv/λ)) when H depends on v; then ∂_v acts on H, and R_X contains the
derivative ∂_v H through −(1/2) □H ([[prop:layer-structure]] (a)).

**Lemma {#lem:layer-bianchi}** (The Bianchi identity at one harmonic, and propagation of the gauge.) Let H_1, …, H_J be
as in [[lem:layer-seed-operators]], put H_0 := H_(J+1) := 0 and

    Z_j := 𝒯H_j + R_X H_(j−1),      G_j := i Pol(H_(j+1)) + D_X H_j.

(a) For every j ≥ 1, with H_(−1) := 0 and G_(−1) := 0,

    i Pol(Z_j) + div Gt(Z_(j−1)) = −i (∇_ℓ + 3/(2r)) G_(j−1) − (1/2) □G_(j−2),                        {#eq:layer-bianchi}

where Gt(Y) := Y − (1/2)(tr Y) g0° and G_j is a covector.

(b) If Z_j = 0 for j ≤ J and G_j = 0 at Σ_τ0 (at r = v − τ0, on every generator) for j ≤ J − 1, then G_j = 0 on Ω
for j ≤ J − 1.

*Proof.* (a) For every metric, div_g Gt(Ric^H(g)) = −B_g[D(g)] by [[eq:data-bianchi]]. Linearise at g0°, where
Ric^H(g0°) = 0 and D(g0°) = 0: div Gt(dRic^H(h)) = −B_(g0°)[dD(h)], and at g0°, with S(V)_mn = (1/2)(∇_m V_n + ∇_n
V_m), B_(g0°)[V]_n = div Gt(S(V))_n = (1/2) □V_n + (1/2)(∇^m ∇_n V_m − ∇_n ∇^m V_m) = (1/2) □V_n + (1/2) Ric_nm V^m =
(1/2) □V_n. Apply this to h := Σ_(j=1)^J λ^j H_j e^(iv/λ). By [[lem:layer-seed-operators]] (b), dRic^H(h) = e^(iv/λ)
Σ_j λ^(j−1) Z_j and dD(h) = e^(iv/λ) Σ_j λ^(j−1) G_(j−1). For a symmetric Y, div Gt(Y e^(iv/λ)) = e^(iv/λ)(div Gt(Y) +
i λ⁻¹ Pol(Y)), since Gt(Y)(ℓ, ·) = Pol(Y); and □(G e^(iv/λ)) = e^(iv/λ)(□G + i λ⁻¹ (2∇_ℓ + 3/r) G), as in the proof of
[[lem:layer-seed-operators]] (b). Both sides are polynomials in λ⁻¹ and λ with coefficients independent of λ, equal for
every λ > 0; the coefficient of λ^(j−2) is [[eq:layer-bianchi]].

(b) G_0 = i Pol(H_1) + D_X H_0 = i Pol(H_1). Suppose G_(j−2) = 0 with j ≤ J. By (a) and Z_j = Z_(j−1) = 0,
(∇_ℓ + 3/(2r)) G_(j−1) = 0: along every generator γ_X, a linear ordinary differential equation in r, with G_(j−1) = 0 at
X_Σ. So G_(j−1) = 0, and induction from j = 1, where G_(−1) = 0 and G_0 = 0 at Σ_τ0, gives the claim. ∎

**Lemma {#lem:layer-pol-plus}** (Pol⁺ at a point.) Let Pol⁺ := Pol^T (Pol Pol^T)⁻¹ be the right inverse of
[[lem:stage-data]] (i), the transposes taken in the Euclidean structure of the Cartesian components in (τ, x), and let
V = V_v dv + V_r dr + V_ϑ dϑ. Then Y := Pol⁺ V has, in (v, r, ϑ, φ1, φ2),

    Y_vv = V_r/4,   Y_vr = −V_r/2,   Y_rr = V_r,   Y_vϑ = −V_ϑ/2,   Y_rϑ = V_ϑ,
    Y_AB = (1/3)(−F V_r − 2 V_v) r² γ_AB,   tr_(g0) Y = −V_r − 2 V_v,                                {#eq:layer-pol-plus}

F := 1 − μ/r² at the point; in particular Pol Y = V, and the γ-traceless angular part of Y vanishes.

*Proof.* Pol is onto ([[lem:stage-data]] (i)), so Pol Pol^T is invertible, Pol⁺ maps onto the range of Pol^T, and Pol is
injective there. So it suffices to show Pol Y = V and that Y lies in the range of Pol^T. First, by
[[eq:layer-components]] (which hold at g0 as well, with F in place of F°): Pol(Y)_r = Y_rr = V_r, Pol(Y)_ϑ = Y_rϑ = V_ϑ,
and Pol(Y)_v = Y_rv − (1/2) tr Y = −V_r/2 + (V_r + 2 V_v)/2 = V_v, with tr Y = 2 Y_vr + F Y_rr + r⁻² γ^(AB) Y_AB = −V_r +
F V_r − F V_r − 2 V_v. Second, rotate the Cartesian coordinates so that at the point x̂ = e1 and ∂_ϑ = r ∂_(x2); then ℓ =
−∂_τ + ∂_1, dv = dτ + dx1, and g0⁻¹ = η⁻¹ − m L0 ⊗ L0, m := μ/r², L0 = ∂_τ − ∂_1. The Frobenius pairing of Pol(Y) with a
covector ξ is Σ_(a,b) Y_ab ((1/2)(ℓ^a ξ_b + ℓ^b ξ_a) − (1/2)(ξ_0 + ξ_1) g0^(ab)), so the range of Pol^T consists of the
arrays

    Z_00 = −ξ_0 + s(1 + m)/2,   Z_01 = (ξ_0 − ξ_1)/2 − s m/2,   Z_11 = ξ_1 − s(1 − m)/2,
    Z_02 = −ξ_2/2,   Z_12 = ξ_2/2,   Z_22 = Z_33 = Z_44 = −s/2,   Z_0j = −ξ_j/2,  Z_1j = ξ_j/2  (j = 3, 4),

s := ξ_0 + ξ_1, all other entries zero. The Cartesian components of Y follow from ∂_v = ∂_τ, ∂_r = −∂_τ + ∂_1,
∂_ϑ = r ∂_2: Y_00 = V_r/4, Y_01 = −V_r/4, Y_11 = V_r/4, Y_02 = −V_ϑ/(2r), Y_12 = V_ϑ/(2r), Y_22 = Y_33 = Y_44 =
((m − 1) V_r − 2 V_v)/3, and no other entries. This is of the form above with ξ_2 = V_ϑ/r, ξ_3 = ξ_4 = 0, s :=
−2((m − 1) V_r − 2 V_v)/3, ξ_0 := s(1 + m)/2 − V_r/4 and ξ_1 := V_r/4 + s(1 − m)/2, whose sum is s as required; the
entries Z_00, Z_11, Z_22 then hold by construction, and Z_01 = (ξ_0 − ξ_1)/2 − s m/2 = −V_r/4. ∎

### The part of first degree {#sec:layer-linear}

The leading wave is W_TT = Re[A env(v) r^(1/2) T e^(iθ)], with T the angular tensor

    T := −(a + b) dϑ² + c² a dφ1² + s² b dφ2²,      a := (2h/3)(2c² + i s²),      b := −(2h/3)(c² + 2i s²),

c = cos ϑ, s = sin ϑ, h = h(cos 2ϑ) as in [[eq:waves]]: indeed (2h/3)(2c² cos θ − s² sin θ) = Re[a e^(iθ)] and
(2h/3)(2s² sin θ − c² cos θ) = Re[b e^(iθ)], which with [[eq:waves]] gives the claim. T is γ-traceless. Put

    d_1 := (div_γ T)_ϑ = ((a − b) − 3(a + b) cos 2ϑ)/sin 2ϑ − (a + b)′,      d := div_γ div_γ T = (cs)⁻¹ (cs d_1)′,
                                                                                                   {#eq:layer-divergence}

′ := d/dϑ; d_1 dϑ is the divergence of T on the round S³ (its φ-components vanish by the symmetries), and d its
divergence, the volume density of γ being cs.

**Definition {#def:layer-profiles}** (The first-degree profiles.) H_1 := A env(v) r^(1/2) T, and for j ≥ 1, H_(j+1) is
the solution of

    𝒯 H_(j+1) = −R_X H_j   along ℓ,      H_(j+1) = i Pol⁺(D_X H_j)   on Σ_τ0, at r = r0 := v − τ0,   {#eq:layer-profiles}

with the operators of [[eq:layer-operators]] at the seed and Pol⁺ of [[lem:layer-pol-plus]] at the seed's F°.

**Proposition {#prop:layer-linear}** (The profiles of first degree.) Put a_1 := A env(v) d_1(ϑ), a_2 := A env(v) d(ϑ),
and

    β_2(r) := −1/(2r0) + (μ0/3)(r⁻³ − r0⁻³).

(a) 𝒯H_1 = 0, Pol(H_1) = 0, D_X H_1 = a_1 r^(−3/2) dϑ, and R_X H_1 = a_1 r^(−5/2)(dr ⊗ dϑ + dϑ ⊗ dr) + (a γ-traceless
angular part); in particular R_X H_1 has no vv, vr, rr or vϑ component.

(b) H_2 has the components

    H_2,rϑ = i a_1 r^(−3/2),   H_2,vϑ = i a_1 r^(−1/2) β_2(r),   H_2,AB = −i r^(1/2) ∫_(r0)^r s^(−1/2) (R_X H_1)_AB ds,
    H_2,vv = H_2,vr = H_2,rr = 0,                                                                     {#eq:layer-h2}

and H_1, H_2 lie in 𝔖. Moreover i Pol(H_2) + D_X H_1 = 0 on Ω.

(c) D_X H_2 = i a_2 (r^(−5/2) β_2(r) dv + r^(−7/2) dr) + (a dϑ term), and the components vv, vr, rr and the trace of
H_3 are

    tr H_3 = 0,   H_3,rr = −a_2 r^(−7/2),   H_3,vr = −a_2 r^(−5/2) β_2(r),   H_3,vv = −a_2 r^(−3/2) β_2(r)².
                                                                                                           {#eq:layer-h3}

(d) At the horizon r = √μ0, H_3,vv(v, √μ0, ϑ) = A env(v) d(ϑ) ν(r0), where

    ν(r0) := −μ0^(−3/4) β_2(√μ0)² = −μ0^(−7/4) (2ρ³ − 3ρ² − 2)²/(36 ρ⁶),      ρ := r0/√μ0.              {#eq:layer-nu}

ν ≤ 0; it vanishes only at the one real root ρ* ∈ (1.80, 1.81) of 2ρ³ − 3ρ² − 2, where it has a double zero with
d²ν/dρ² ≠ 0; dν/dρ = −μ0^(−7/4) (ρ² + 2)(2ρ³ − 3ρ² − 2)/(6ρ⁷); and ν → −μ0^(−7/4)/9 as ρ → ∞.

*Proof.* (a) H_1 has only angular components, r^(1/2) times functions of (v, ϑ), so (𝒯H_1)_AB = −i(∂_r − 1/(2r))
r^(1/2)(…) = 0, and Pol(H_1) = 0 by [[eq:layer-components]] (H_1,rr = H_1,rϑ = 0, γ^(AB) T_AB = 0). For D_X H_1 =
div H_1 (tr H_1 = 0): in (div h)_n = g0°^(ab)(∂_a h_bn − Γ^d_(ab) h_dn − Γ^d_(an) h_bd) with h angular, the symbols of
[[eq:layer-christoffel]] give (div h)_v = 0, (div h)_r = −r⁻³ γ^(AB) h_AB = 0, and (div h)_ϑ = r⁻² (div_γ h)_ϑ; with
h = H_1 this is a_1 r^(−3/2). For R_X H_1: H_1 is in 𝔖, so (R_X H_1)_vv = 0 and tr R_X H_1 = 0
([[lem:layer-seed-operators]] (d)), and (R_X H_1)_vϑ = 0 by (e) there. Apply [[eq:layer-bianchi]] at j = 2 to J = 1, H_1
alone: Z_1 = 𝒯H_1 = 0, Z_2 = R_X H_1, G_0 = 0 and G_1 = D_X H_1, so Pol(R_X H_1) = −(∇_ℓ + 3/(2r)) D_X H_1. For the
covector ω := a_1 r^(−3/2) dϑ, (∇_ℓ ω)_ϑ = ∂_r ω_ϑ − ω_ϑ/r and (∇_ℓ ω)_v = (∇_ℓ ω)_r = 0, so −(∇_ℓ + 3/(2r)) ω =
a_1 r^(−5/2) dϑ. Hence (R_X H_1)_rr = 0, (R_X H_1)_rϑ = a_1 r^(−5/2), and (R_X H_1)_rv = (1/2) tr R_X H_1 = 0.

(b) The data: by (a) and [[eq:layer-pol-plus]] with V = D_X H_1 = a_1 r0^(−3/2) dϑ, H_2 = i Pol⁺ V has at r0 the
components rϑ = i a_1 r0^(−3/2), vϑ = −(i/2) a_1 r0^(−3/2) = i a_1 r0^(−1/2) β_2(r0), and no other. The transport:
by (a) and [[eq:layer-components]], the vv, vr, rr components of 𝒯H_2 = −R_X H_1 are homogeneous with zero data, so
they vanish; (∂_r + 1/(2r)) H_2,rϑ = −i a_1 r^(−5/2) gives H_2,rϑ = i a_1 r^(−3/2), since (∂_r + 1/(2r)) r^(−3/2) =
−r^(−5/2); (∂_r + 1/(2r)) H_2,vϑ = −μ0 H_2,rϑ/r³ reads i a_1 r^(−1/2) β_2′ = −i μ0 a_1 r^(−9/2), which β_2′ = −μ0 r⁻⁴
satisfies; and (∂_r − 1/(2r)) H_2,AB = −i (R_X H_1)_AB with zero data gives the integral, γ-traceless because (R_X
H_1)_AB is (tr R_X H_1 = 0). So H_2 is in 𝔖. By [[lem:layer-bianchi]] (b) with J = 2 (Z_1 = Z_2 = 0, G_0 = 0, and
G_1 = 0 at r0 since Pol Pol⁺ = 1), G_1 = i Pol(H_2) + D_X H_1 = 0 on Ω.

(c) For h in 𝔖 the same calculation as in (a) gives (div h)_v = r⁻² div_γ(h_(v·)) and (div h)_r = r⁻² div_γ(h_(r·)),
the divergences on S³ of the covectors h_(vA) and h_(rA): the terms with Γ^A_(·v) vanish, h_vv = h_vr = h_rr = 0, and
the term −Γ^E_(Ar) h_(BE) contracted with g0°^(AB) is a trace. With tr H_2 = 0 and div_γ(d_1 dϑ) = d, this is the
stated form of D_X H_2. By (b) and [[lem:layer-seed-operators]] (d), (R_X H_2)_vv = 0 and tr R_X H_2 = 0. Let H_3 be
given by [[eq:layer-profiles]]. Its data at r0 are, by [[eq:layer-pol-plus]] with V_v = i a_2 r0^(−5/2) β_2(r0) and
V_r = i a_2 r0^(−7/2): H_3,vv = i V_r/4 = −a_2 r0^(−7/2)/4 and tr H_3 = i(−V_r − 2 V_v) = 0, since β_2(r0) = −1/(2r0)
gives 2 V_v = −V_r.
The trace of 𝒯H_3 is −i(∂_r + 3/(2r)) tr H_3, as ∇_ℓ commutes with the trace, and equals −tr R_X H_2 = 0; so r^(3/2)
tr H_3 is constant along ℓ, and tr H_3 = 0. By [[lem:layer-bianchi]] (b) with J = 3, i Pol(H_3) = −D_X H_2 on Ω, that is
H_3,rr = i (D_X H_2)_r = −a_2 r^(−7/2) and H_3,vr − (1/2) tr H_3 = i (D_X H_2)_v = −a_2 r^(−5/2) β_2. The vv component of
𝒯H_3 = −R_X H_2 is ∂_r H_3,vv + (3/(2r)) H_3,vv + 2 μ0 H_3,vr/r³ = 0, that is ∂_r (r^(3/2) H_3,vv) = 2 μ0 a_2 r⁻⁴ β_2.
Since ∂_r(−a_2 β_2²) = −2 a_2 β_2 β_2′ = 2 μ0 a_2 r⁻⁴ β_2 and −a_2 β_2(r0)² = −a_2/(4 r0²) = r0^(3/2) H_3,vv(r0), we get
r^(3/2) H_3,vv = −a_2 β_2² on the whole generator.

(d) At r = √μ0, (c) gives H_3,vv = −a_2 μ0^(−3/4) β_2(√μ0)², and β_2(√μ0) = −1/(2r0) + 1/(3√μ0) − μ0/(3r0³) =
μ0^(−1/2) (2ρ³ − 3ρ² − 2)/(6ρ³), which gives [[eq:layer-nu]]. Put p(ρ) := 2ρ³ − 3ρ² − 2. Since p′(ρ) = 6ρ(ρ − 1),
p has its local maximum p(0) = −2 < 0 and its local minimum p(1) = −3 < 0, so it has exactly one real root ρ*, in
(1, ∞); p(1.80) = −0.056 < 0 < p(1.81) = 0.031182. ν = −μ0^(−7/4) p²/(36 ρ⁶) has a double zero there, with d²ν/dρ² =
−μ0^(−7/4) p′(ρ*)²/(18 ρ*⁶) ≠ 0 since p′(ρ*) ≠ 0. Differentiating, dν/dρ = −μ0^(−7/4) p (ρ p′ − 3p)/(18 ρ⁷) and ρ p′ −
3p = 3(ρ² + 2). Finally p²/ρ⁶ → 4. ∎

The admissible values are r0 = v − τ0 ≥ v_s − τ0 > √μ0 + 1, that is ρ > 1 + μ0^(−1/2). The coefficient ν depends on τ0,
through r0, and on the Euclidean structure used to define Pol⁺; the one fixed in [[lem:stage-data]] is used throughout. A
tensor T with d = 0 gives no λ³ term: for instance (a, b) = ((1 + 3 cos 2ϑ)/2, (1 − 3 cos 2ϑ)/2) has d_1 = 0.

**Lemma {#lem:layer-angular}** (The angular factor of the waves.) With ζ := cos 2ϑ,

    d_1 = sin 2ϑ · √2 ((3ζ² − 2ζ + 5) + i (3ζ² + 2ζ + 5)) / (3 (1 + ζ²)^(3/2)),
    d = (2√2/3) ((3ζ⁵ + 10ζ³ − 10ζ² + 19ζ + 2) + i (3ζ⁵ + 10ζ³ + 10ζ² + 19ζ − 2)) / (1 + ζ²)^(5/2),    {#eq:layer-d}

and |d| ≥ 8/3 at every angle, the axes included, with equality only at ζ = 0.

*Proof.* With c² = (1 + ζ)/2, s² = (1 − ζ)/2 and h = √2 (1 + ζ²)^(−1/2),

    a + b = √2 (ζ + 1 + i(ζ − 1)) / (3 √(1 + ζ²)),      a − b = √2 (1 + ζ + i(1 − ζ)) / √(1 + ζ²).

So (a − b) − 3ζ(a + b) = √2 (1 − ζ²)(1 + i)/√(1 + ζ²). With d/dϑ = −2 sin 2ϑ d/dζ and sin 2ϑ = √(1 − ζ²),
−(a + b)′ = 2 sin 2ϑ (d/dζ)(a + b) = (2√2/3) sin 2ϑ ((1 + i) − (1 − i) ζ)/(1 + ζ²)^(3/2). Adding the two terms of
[[eq:layer-divergence]] gives d_1 = sin 2ϑ · q(ζ) with the q displayed. Then cs d_1 = (1/2)(1 − ζ²) q and d =
(cs)⁻¹ (cs d_1)′ = −2 (d/dζ)((1 − ζ²) q), which is the stated d. For the bound, write the two numerators of d as o + e
and o − e, with the odd part o := 3ζ⁵ + 10ζ³ + 19ζ and the even part e := 2 − 10ζ². Then |d|² = (8/9)((o + e)² + (o −
e)²)/(1 + ζ²)⁵ = (16/9)(o² + e²)/(1 + ζ²)⁵, and with u := ζ²,

    o² + e² − 4 (1 + u)⁵ = 5u⁵ + 40u⁴ + 174u³ + 440u² + 301u ≥ 0,

so |d|² ≥ (16/9) · 4 = 64/9, with equality only at u = 0. ∎

**Lemma {#lem:layer-inverse}** (The inverse metric on the boundary.) On the boundary,

    g_λ⁻¹(dΦ0, dΦ0) = −m0 − k(Φ0♯, Φ0♯) + q,      |q| ≤ C |k(Φ0♯, ·)| (|k(Φ0♯, ·)| + |k|²),           {#eq:layer-inverse}

where C depends on the bounds of g0⁻¹ and g_λ⁻¹ on Ω; here |k| ≤ C λ ≤ 1 on Ω, by item 4 of [[thm:main]] and the choice
of λ0 in [[sec:eq-setting]].

*Proof.* From g_λ = g0 + k, g_λ⁻¹ − g0⁻¹ = −g0⁻¹ k g_λ⁻¹, and substituting this once more for g_λ⁻¹ on the right, g_λ⁻¹ =
g0⁻¹ − g0⁻¹ k g0⁻¹ + g0⁻¹ k g0⁻¹ k g_λ⁻¹. Contract with dΦ0 twice: the first two terms give −m0 − k(Φ0♯, Φ0♯), and the
third is q := k(Φ0♯, g0⁻¹ k g_λ⁻¹ dΦ0), so that the absolute value of q is at most C |k(Φ0♯, ·)| times |k(g_λ⁻¹ dΦ0, ·)|.
The same identity applied to g_λ⁻¹ dΦ0 bounds the latter by |k(Φ0♯, ·)| + C |k| |k(Φ0♯, ·)| + C |k|³, which is at most C
(|k(Φ0♯, ·)| + |k|²) since |k| ≤ 1. ∎

### Flat-edge bounds {#sec:layer-flat}

*Two structural facts.* (F1) Every monomial of the forcing term −Π_osc(𝒲(m_m, φ_m) + 𝒦_m) of [[eq:stage-system]] (c),
and of the known part of the data of ĝ_(m+1) in [[lem:stage-data]] (i), contains an oscillating factor among W, χ and
ĝ_l (l ≤ m), carrying at most two derivatives in the first case and at most one in the second; its other factors are
profiles of [[thm:approximant]], bounded globally, or coefficients built from g0. Indeed a monomial without an
oscillating factor does not depend on θ, and Π_osc removes it; and the data of [[lem:stage-data]] (i) come from the
oscillating part of D, which has one derivative.

(F2) Every monomial of the mean forcing terms (𝒮_m, q_m, ⟨T̂ ĝ_(m+1)⟩ and the coefficient of dφ_m in ⟨𝒲_φ⟩), of the
forcing terms S_m and the coefficient B_m of [[lem:stage-data]] (iii), of Ric^H(g_app) − Ric(g0) and of the
difference between the constraint map of g_app's data and that of g0's data contains two oscillating factors, or a
factor among the means and phases of earlier stages, μ − μ0 and μ^(k), k ≥ 1. For every oscillating factor has θ-mean
zero, so the θ-mean of a monomial with exactly one oscillating factor and all other factors independent of θ is zero;
and each of these quantities is a polynomial in the profiles and in μ − μ0, μ^(k), with coefficients built from the
seed, whose constant term is the seed's own value, zero (at A = 0 the construction returns the seed). For ⟨T̂ ĝ_(m+1)⟩
more holds: by [[lem:layer-seed-operators]] (b) with k = 1, 2, …, the seed's part T̂_0 of T̂ maps the k-th harmonic to
k 𝒯 of it, an operator in X composed with ∂_θ, of θ-mean zero on every profile; so ⟨T̂ ĝ_(m+1)⟩ = ⟨(T̂ − T̂_0)
ĝ_(m+1)⟩, whose coefficients are built from W, χ, m_1, φ_1 and μ − μ0.

The μ-factors carry the weight at every point: 0 ≤ μ − μ0 ≤ (2/9) A² (v − v_s) ε_0(v)² and |μ^(k)| ≤ C ε_(k−1)(v)².

**Lemma {#lem:layer-energy-null}** (Energy on Ω_v, the null face kept.) Let v ≤ v_♯ and let u, a function or a
Cartesian array, satisfy −(1/2) g0^(ab) ∂_a ∂_b u = f on Ω_v. Put e(τ) := ‖∂u(τ)‖ + ‖u(τ)‖, the flat L² norms on Σ_τ ∩
Ω_v, and F_v(u) := ∫_(N_v) T(L0, Y) r³ dr dω, with T the energy tensor of u for g0, Y = −g0⁻¹ dτ and L0 = −ℓ. Then

    sup_(τ0≤τ≤τ_end) e(τ) + F_v(u)^(1/2) ≤ C_E (e(τ0) + ∫_(τ0)^(τ_end) ‖f‖),                      {#eq:layer-energy-null}

C_E depending on Ω and μ(v_end) only, not on v; and T(L0, Y) = (1/2)(1 + μ/r²)(ℓu)² + |∇̊u|²/(2r²), ∇̊ the gradient on
the unit S³.

*Proof.* Run the proof of [[lem:energy]] on Ω_v ∩ {τ0 ≤ τ′ ≤ τ} with g̃ := g0 and J := T(Y, ·). Its boundary is
Σ_τ0 ∩ Ω_v, Σ_τ ∩ Ω_v, part of {r = a}, spacelike with Ω_v to its past ([[lem:domain]] (b)), whose flux is
nonnegative and dropped, and part of N_v. In (v, r, ω) the volume form of g0 is r³ dv dr dω and the outward conormal of
N_v is dv, so the outward flux through it is ∫ J(dv) r³ dr dω = ∫ T(ℓ, Y) r³ dr dω = −∫ T(L0, Y) r³ dr dω; moved to the
left it is the part of F_v(u) with τ′ ≤ τ. Its density: g0(L0, Y) = −dτ(L0) = −1, Y = ∂_v − (μ/r²) ∂_r, L0 u = −∂_r u,
and g0⁻¹(du, du) = 2 ∂_v u ∂_r u + F (∂_r u)² + r⁻² |∇̊u|², so T(L0, Y) = (L0 u)(Y u) + (1/2) g0⁻¹(du, du) = (1/2)(1 +
μ/r²)(∂_r u)² + |∇̊u|²/(2r²): no transverse derivative ∂_v u enters, and it is nonnegative. The bulk is at most C(e² +
‖f‖ e) as in [[lem:energy]], and ∂_τ ‖u‖² = 2⟨u, ∂_τ u⟩ − ∫_(r=v−τ) |u|² r³ dω, the outer radius v − τ of Σ_τ ∩ Ω_v
decreasing at rate one. Gronwall's inequality, then τ = τ_end for the flux. The constant is that of [[lem:energy]],
which depends on the bounds of g0 and Y on Ω only. ∎

**Lemma {#lem:layer-transport}** (Transport on Ω_v and along the generators.) (a) If L0 φ − c φ = f on Ω_v with c
bounded, then ‖φ(τ)‖ ≤ e^(C(τ−τ0)) (‖φ(τ0)‖ + ∫_(τ0)^τ ‖f‖), the norms on Σ_τ ∩ Ω_v. (b) Let Z(X, θ) ∈ ℝ^d solve
−(ℓ·∂_X) Z + 𝓜 Z = F on Ω × S¹, with 𝓜(X) a linear operator on C(S¹; ℝ^d) of norm at most M1. Then for X ∈ Ω

    sup_θ |Z(X, ·)| ≤ e^(M1 L) (sup_θ |Z(X_Σ, ·)| + L sup_(γ_X × S¹) |F|),      L := r(X_Σ) − r(X) ≤ b(τ0) − a.

The derivatives (∂^α_X ∂_θ^p Z)_(|α|+p≤i) solve a system of the same kind (the commutator of ∂_X with ℓ·∂_X is
(∂ℓ)·∂_X, of the same order), with data on Σ_τ0 the tangential derivatives of Z|_(Σ_τ0) and the transverse ones read
from the equation, since dτ(ℓ) = −1.

*Proof.* (a) is the proof of [[lem:transport]] with outer radius b(τ) := v − τ, whose outer boundary term carries the
factor 1 + b′ = 0: L0 is tangent to N_v. (b) In (v, r, ω), ℓ = ∂_r and γ_X is r ↦ (v(X), r, ω(X)), so the equation is a
linear ordinary differential equation in r with values in the Banach space C(S¹; ℝ^d), and Gronwall's inequality gives
the bound. ∎

For the stage transports, 𝓜 := Π_osc ℳ ∂_θ⁻¹ on zero-mean profiles ([[lem:first-stage-operator]]), with ∂_θ⁻¹ the
zero-mean primitive. For a zero-mean continuous Z its zero-mean primitive Y vanishes somewhere, and the integral of Z
over the shorter of the two arcs from that point is at most π sup |Z|, the integral over the whole circle being zero;
so ‖∂_θ⁻¹‖ ≤ π, and ‖Π_osc‖ ≤ 2. Hence ‖𝓜‖ ≤ C by the global bounds of [[thm:approximant]].

**Lemma {#lem:layer-null-pointwise}** (Pointwise bounds from the null face.) For u smooth on Ω_v and Y ∈ N_v,

    |u(Y)| ≤ C_N Σ_(|β|≤2) (sup_(N_v ∩ Σ_τ0) |Ω^β u| + F_v(Ω^β u)^(1/2)),                      {#eq:layer-null-pointwise}

Ω^β products of the rotations Ω_ab := x_a ∂_b − x_b ∂_a, C_N depending on a and b(τ0) only.

*Proof.* In (v, r, ω), γ_Y runs in N_v from r(Y) ≥ a to r_Σ := v − τ0, and the rotations commute with ℓ = ∂_r. On the
unit S³, |u(r, ·)|_∞ ≤ C Σ_(|β|≤2) ‖Ω^β u(r, ·)‖_(L²(S³)): H² ⊂ L^∞ in dimension three [[thm:std-bh-embedding]], the
rotations spanning every tangent space. And ‖Ω^β u(r, ·)‖ ≤ ‖Ω^β u(r_Σ, ·)‖ + ∫_r^(r_Σ) ‖ℓ Ω^β u(r′, ·)‖ dr′ ≤
C sup |Ω^β u|_(r_Σ) + (r_Σ − a)^(1/2) a^(−3/2) (∫∫ (ℓ Ω^β u)² r′³ dr′ dω)^(1/2), and the last double integral is at
most 2 F_v(Ω^β u) by the formula for T(L0, Y). ∎

The flux through N_v controls exactly the derivatives tangent to N_v, which is what an integration along γ_Y and a
Sobolev inequality on the spheres need; the slices Σ_τ ∩ Ω_v = {a ≤ r ≤ v − τ} are arbitrarily thin as v − τ ↓ a,
and no Sobolev inequality on them is used.

**Lemma {#lem:layer-flat}** (Flat-edge bounds of the construction.) Let N ≥ 3, and let H_j (1 ≤ j ≤ N + 1) be the
profiles of [[def:layer-profiles]]. For every X ∈ Ω with v := v(X) ≤ v_♯ and every order i:

(a) *oscillating, degree one:* |∂^i_(X,θ) ĝ_j(X)| ≤ C ε_(i+2j−2)(v), 1 ≤ j ≤ N + 1;

(b) *means and phases, degree two:* |∂^i m_j(X)| + |∂^i φ_j(X)| ≤ C ε_(i+2j+1)(v)² and |∂^i Ψ_j(X)| ≤ C ε_(i+2j+3)(v)²,
1 ≤ j ≤ N, with Ψ_j = □̃φ_j;

(c) *oscillating, the remainder of degree two:* |∂^i_(X,θ)(ĝ_j − Re[H_j e^(iθ)])(X)| ≤ C ε_(i+2j+1)(v)², and |∂^i
H_j(X)| ≤ C ε_(i+2j−2)(v), 1 ≤ j ≤ N + 1;

(d) *residual:* |∂^i Ric^H(g_app)(X)| ≤ C λ^(N−1−i) ε_(i+2N+3)(v);

(e) *slice data:* on Σ_τ0 at radius r with τ0 + r ≤ v_♯, the stage-m data (α_m, ϖ_m, q′_m, ∂_τ (m_m)_(τ·)) of
[[lem:stage-data]], with their angular derivatives and i radial derivatives, are at most C ε_(i+2m)(τ0 + r)², and the
correction U of [[prop:exact-correction]] obeys sup_(r′≤r) ‖∂_r^j U(r′)‖_(H^s(S³)) ≤ C λ^(N−2−j) ε_(j+2N+3)(τ0 + r) for
j ≤ 3 and the s of [[prop:exact-correction]].

Every cost that [[prop:layer-identification]], [[lem:layer-remainder]] and [[lem:layer-remainder-weak]] use, at orders
i ≤ 4 and j ≤ 3, is at most 2N + 6 ≤ M* := 2N + 8.

*Proof.* Induction on the stage m = 0, 1, …, N. At stage m the steps run in the order (e) for the stage-m slice data,
(a) for ĝ_(m+1), (b) for (m_m, φ_m, Ψ_m), (c) for ĝ_(m+1); each uses only the global bounds of [[thm:approximant]] and
what the earlier steps proved.

*Stage 0.* The Cartesian components of W_TT are A env(v) times smooth functions of (r, x̂, θ) ([[lem:waves]] (a)): cost
i at order i. χ solves [[eq:chi-transport]] along ℓ, zero on Σ_τ0; its forcing term F_2 is quadratic in ∂_θ W_TT, with
no slow derivative. So [[lem:layer-transport]] (b) gives |∂^i χ| ≤ C ε_i(v)²: (a) and (c) at j = 1, since ĝ_1 −
Re[H_1 e^(iθ)] = χ dv ⊗ dv.

*Stage m ≥ 1, (e).* The data (α_m, ϖ_m, q′_m) solve the system of [[lem:linear-evolution]] on [a, b1] from zero data at
r = a, with forcing S_m. Its restriction to [a, r] solves the same problem on [a, r], whose solution is unique
([[lem:linear-evolution]] on [a, r]), and the bound of [[lem:linear-evolution]] holds on [a, r] with its constant for
[a, b1]: the proof integrates an energy inequality in r from a, and Gronwall's inequality over a shorter interval gives
a smaller constant. By (F2) and the induction hypothesis, |∇̊^β S_m| ≤ C ε_(2m)(τ0 + r′)² on the sphere of radius r′
(on Σ_τ0, v = τ0 + r′ on that sphere, so angular derivatives cost nothing). Hence sup_(r′≤r) (‖α_m‖_(H^(s+1)) +
‖(ϖ_m, q′_m)‖_(H^s)) ≤ C ε_(2m)(τ0 + r)², pointwise by Sobolev's inequality on S³. Radial derivatives follow from the
equations, each costing one radial derivative of the forcing terms, that is one derivative of env. ∂_τ (m_m)_(τ·) is
algebraic in these and in known quantities ([[lem:stage-data]] (ii)).

*(a).* Z_(m+1) := ∂_θ ĝ_(m+1) solves the transport of [[lem:layer-transport]] (b) with the 𝓜 above and F :=
−Π_osc(𝒲(m_m, φ_m) + 𝒦_m). By (F1) each monomial of F has an oscillating factor among W, χ, ĝ_l (l ≤ m), with at most
two derivatives, the other factors bounded globally: F has cost i + 2m at order i. Its data, −Pol⁺(Λ_m(γ_m) + known),
are bilinear in γ_m (bounded globally) and ∂_θ W, and the known part has an oscillating factor with at most one
derivative (F1); Pol⁺ is smooth and pointwise: cost i + 2m − 1. [[lem:layer-transport]] (b), commuted to order i, gives
cost i + 2m = i + 2(m + 1) − 2.

*(b).* m_m solves [[eq:stage-system]] (a), a wave equation with g0's principal part. Commute with ∂^α (|α| ≤ i) and Ω^β
(|β| ≤ 2; the rotations are Killing for g0 and commute with □̃, which acts on Cartesian components). The forcing terms
𝒮_m and q_m are at most C ε_(i+2m)(v)² by (F2) and the induction hypothesis; ⟨T̂ ĝ_(m+1)⟩ = ⟨(T̂ − T̂_0) ĝ_(m+1)⟩ is at
most C ε_(i+2m)(v)² through its coefficients W, χ, μ − μ0 and (a), while its coefficients m_1, φ_1 give, at m = 1,
terms linear in the stage's own unknowns and, at m ≥ 2, terms of size ε²·ε; ⟨𝒲_φ(φ_m)⟩ is linear in dφ_m. The data on
Σ_τ0 ∩ Ω_v are (m_m)_(τ·) = 0 and those of (e); the energy of ∂^α Ω^β m_m involves them at order i + 1, of cost
i + 1 + 2m. Apply [[lem:layer-energy-null]] to ∂^α Ω^β m_m on Ω_(v′) for each v′ ≤ v, together with
[[lem:layer-transport]] (a) for ∂^α Ω^β ∂φ_m (L0 ∂φ_m = −(1/2) ∂(m_m(ℓ, ℓ) + q_m) + [L0, ∂] φ_m, φ_m = 0 on Σ_τ0), and
Gronwall's inequality: the energies and the fluxes F_(v′)(∂^α Ω^β m_m)^(1/2) are at most C ε_(i+2m+1)(v′)².
[[lem:layer-null-pointwise]] at every point of N_(v′) gives |∂^α m_m| ≤ C ε_(i+2m+1)(v′)² there, and every Y ∈ Ω with
v(Y) ≤ v_♯ lies on N_(v(Y)). φ_m: L0 φ_m = −(1/2)(m_m(ℓ, ℓ) + q_m) with φ_m = 0 on Σ_τ0, integrated along γ_Y, gives the
same bound. Ψ_m: its transport ([[lem:stage-system]]) uses two more derivatives of m_m: cost i + 2m + 3.

*(c).* Put δ_(m+1) := ĝ_(m+1) − Re[H_(m+1) e^(iθ)]. By [[lem:layer-seed-operators]] (b) the seed's operators on one
harmonic are exactly λ⁻¹ k 𝒯 + R_X and λ⁻¹ i k Pol + D_X, so [[eq:layer-profiles]] is [[eq:stage-system]] (c) and
[[lem:stage-data]] (i) with every coefficient at the seed and every forcing term cut to its part linear in the
oscillating profiles; Pol Pol⁺ = 1. Hence ∂_θ δ_(m+1) solves the transport of [[lem:layer-transport]] (b) with the
seed's 𝓜_0 and the forcing term

    −[Π_osc(𝒲 + 𝒦_m) − R_X(Re[H_m e^(iθ)])] − (𝓜 − 𝓜_0) Z_(m+1),

whose bracket is R_X(δ_m) + (R_X^(g0) − R_X)(ĝ_m) + (the monomials of Π_osc 𝒦_m with two or more oscillating
factors) + Π_osc 𝒲(m_m, φ_m), R_X^(g0) the operator with g0's coefficients. By (c), (a) at the earlier stages, by (b)
at stage m and |μ − μ0| ≤ C ε², each part is at most C ε_(i+2m+3)(v)²; 𝓜 − 𝓜_0 has coefficients W, χ, m_1, φ_1,
μ − μ0, so (𝓜 − 𝓜_0) Z_(m+1) is at most C ε². The data differ by (Pol⁺_(g0) − Pol⁺_seed)(·) + Pol⁺(Λ_m(γ_m)) +
Pol⁺(D_X δ_m + (D_X^(g0) − D_X) ĝ_m + monomials with two oscillating factors), at most C ε² by (e).
[[lem:layer-transport]] (b): cost i + 2m + 3 = i + 2(m + 1) + 1. The bound on H_(m+1) itself is the proof of (a) with
the seed's coefficients.

*(d).* Ric^H(g_app) is ℱ(X, λ, θ) at θ = v/λ, ℱ := λ⁻² 𝒜_2 + λ⁻¹ 𝒜_1 + 𝒜_0 the two-scale operator on the profile of
g_app. ℱ − Ric(g0) =: ℱ_p is a smooth function of λ ∈ [0, λ0] and of finitely many jets of the profiles, vanishing when
they vanish: 𝒜_2 carries g_app⁻¹(dv, dv) ∂_θ²(·) and 𝒜_1 carries ∂_θ, both only on profiles (g0⁻¹(dv, dv) = 0), and
Ric(g0) = (3μ′/(2r³)) dv ⊗ dv is the only monomial free of profiles. By the proof of [[thm:approximant]], ∂_λ^n ℱ = 0
at λ = 0 for n ≤ N − 2 ((E3) with K = N − 1). So ℱ = λ^(N−1) ((N − 2)!)⁻¹ ∫_0^1 (1 − s)^(N−2) ∂_λ^(N−1) ℱ_p(X, sλ, θ)
ds, and by the mean value theorem in the jets, with (a), (b) for the profiles up to ĝ_(N+1), m_N, φ_N and two
derivatives, the integrand is at most C ε_(2N+3)(v). Each derivative of [·] costs λ⁻¹, through ∂_θ
([[eq:two-scale-derivative]]), and one more derivative of env.

*(e) for U.* On [a, r] with τ0 + r ≤ v_♯: the constraint map 𝒞(γ, κ) of g_app's data on Σ_τ0 has profiles that vanish
below order N − 2 ([[lem:gauge-hierarchy]]), so, by Taylor's formula in λ as in (d), its difference from the seed's
value vanishing with the profiles, and by (F2), (a), (b), sup_(r′≤r) ‖𝒞(γ, κ)(r′)‖_(H^s) ≤ C λ^(N−2) ε_(2N+3)(τ0 + r),
angular derivatives being free on Σ_τ0. Run the iteration of [[prop:exact-correction]] on [a, r]: its inputs are
[[lem:linear-evolution]] on [a, r], with constant at most that on [a, b1], and the coefficient bounds, restrictions of
those on [a, b1]. The iterates stay in the ball of radius 2 C0 λ^(N−2) ε_(2N+3)(τ0 + r), C0 the constant of the
iteration, since the quadratic remainder is at most C λ⁻¹ (2 C0 λ^(N−2) ε)² ≤ C0 λ^(N−2) ε for λ small and N ≥ 4, and
they contract in the weaker norm. The limit and the restriction of the U of [[prop:exact-correction]] both solve the
problem on [a, r] and lie in the ball of radius 2 C0 λ^(N−2), where the difference estimate of the iteration gives
uniqueness: they coincide. The r-derivatives come from the equations, each costing at most λ⁻¹ and one derivative of
env.

*The count.* The costs at order i are i + 2j − 2 for ĝ_j, i + 2j + 1 for m_j, φ_j and ĝ_j − Re[H_j e^(iθ)], i + 2j + 3
for Ψ_j, i + 2N + 3 for the residual and j + 2N + 3 for U. With i ≤ 4 in [[prop:layer-identification]] (j ≤ N) and
i ≤ 2, j ≤ 3 in [[lem:layer-remainder]], the largest is 3 + 2N + 3 = 2N + 6. ∎

Since every cost carries a factor ε_c(v), zero for v ≤ v_s, the lemma contains the facts used in [[sec:eq-setting]]:
every stage vanishes on Ω ∩ {v ≤ v_s}, and the stage data and U vanish on Σ_τ0 ∩ {r ≤ v_s − τ0}.

**Proposition {#prop:layer-identification}** (The part of first degree of the approximant.) For X ∈ Ω with v :=
v(X) ≤ v_♯ and 1 ≤ j ≤ N, the profiles g_j of [[eq:approximant]] satisfy

    |∂^i_(X,θ) (g_j − Re[H_j e^(iθ)])(X)| ≤ C ε_(i+2j+1)(v)².                                  {#eq:layer-identification}

That is, the part of first degree of Σ_j λ^j [g_j] is Re Σ_j λ^j H_j e^(iv/λ), and the rest is of degree two in the
sense of [[eq:layer-identification]].

*Proof.* (i) *[[eq:layer-profiles]] is the first-degree system.* By [[lem:layer-seed-operators]] (b), the seed's
linearised Ric^H on H e^(ikθ) is exactly λ⁻¹ k 𝒯H + R_X H, with no λ⁻² part and R_X independent of k, and its linearised
D is λ⁻¹ i k Pol(H) + D_X H. So the order-m coefficient of the two-scale expansion, restricted to the terms linear in the
oscillating profiles and with the seed's coefficients, is Re[(𝒯H_(m+1) + R_X H_m) e^(iθ)] (the term T̂ ĝ_(m+1) of
[[eq:stage-m]] and the part of 𝒦_m linear in ĝ_m), and the order-m oscillating part of D is Re[(i Pol H_(m+1) + D_X H_m)
e^(iθ)]; [[lem:stage-data]] (i) solves the latter on Σ_τ0 by i Pol⁺(D_X H_m). (ii) *The means and phases have no part of
first degree:* this is [[lem:layer-flat]] (b), which rests on (F2). (iii) *The fixed-phase rewriting.* By the proof of
[[thm:approximant]], g_j is the λ^j coefficient of the means and of the sum Σ_l λ^l ĝ_l(X, θ + φ1 + λΨ), Ψ := Σ_(i≥2)
λ^(i−2) φ_i; so g_j = m_j + ĝ_j(X, θ + φ1) + T_j, T_j a sum of products of ∂_θ^p ĝ_l (p ≥ 1, l < j) with monomials of
positive degree in φ_2, …, φ_j (for instance T_2 = φ_2 ∂_θ ĝ_1(X, θ + φ1)). By [[lem:layer-flat]] (b), |m_j|, |φ_i| ≤ C
ε²; by (a) there, the absolute value of ∂_θ^p ĝ_l is at most C ε; so |T_j| ≤ C ε³ and |ĝ_j(θ + φ1) − ĝ_j(θ)| ≤ |φ1|
sup |∂_θ ĝ_j| ≤ C ε³; and |ĝ_j − Re[H_j e^(iθ)]| ≤ C ε² by (c) there. The derivatives follow by Leibniz's rule and
[[eq:two-scale-derivative]], with costs at most i + 2j + 1. ∎

**Corollary {#cor:layer-expansion}** (The expansion on the boundary.) At X = (v, r_q(v), x̂), v_s < v ≤ v_♯, with ε :=
ε_(M*)(v) and θ = v/λ,

    −k(Φ0♯, Φ0♯) = −λ³ A env(v) ν(v − τ0) Re[d(ϑ) e^(iθ)] + O(λ⁴ ε + λ ε² + |w(X)|),
    |k(Φ0♯, ·)| ≤ C (λ² ε + λ ε² + |w(X)|),      |k| ≤ C (λ ε + |w(X)|),
    0 ≤ m0(v) ≤ C (ε_0(v)² + ∫_(v_s)^v env²),                                                       {#eq:layer-expansion}

the O(·) with constants as in [[sec:layer-setting]]. Moreover |β_Φ| ≤ (μ − μ0)/(2μ0) + r_q μ′/(4μ0) and 0 ≤ r_q − √μ0
≤ (μ − μ0)/(4√μ0).

*Proof.* For x ≥ 1, √x − 1 ≤ (x − 1)/2 and x^(1/4) − 1 ≤ (x − 1)/4, by concavity; with x = μ/μ0 these give the bounds
on β_Φ, on r_q − √μ0 = √μ0 ((μ/μ0)^(1/4) − 1) and, with μ′ = (2/9) A² env², on m0. k = Σ_j λ^j [g_j] + w, and by
[[eq:layer-identification]] Σ_j λ^j g_j = Σ_j λ^j Re[H_j e^(iθ)] + O(λ ε²). H_1, H_2 lie in 𝔖
([[prop:layer-linear]]): H_1(∂_v, ·) = 0, H_2(∂_v, ∂_v) = 0 and |H_2(∂_v, ·)| ≤ C ε. H_3,vv(v, √μ0, ϑ) = A env(v) d(ϑ)
ν(v − τ0) ([[prop:layer-linear]] (d)), and |H_3,vv(v, r_q) − H_3,vv(v, √μ0)| ≤ sup |∂_r H_3| (r_q − √μ0) ≤ C ε · ε²
([[lem:layer-flat]] (c)). The orders λ^j, j ≥ 4, give C λ⁴ ε, and the β_Φ-terms |β_Φ| |k| ≤ C ε² (λ ε + |w|). ∎

**Lemma {#lem:layer-remainder}** (The weighted remainder.) Let K ≥ 6 and N = K + 3. Let λ be so small that s := C1 λ ≤
1/2, with C1 of [[eq:eq-c1]], and put ε_t := 2 C1 λ. Let v1 ≤ v_♯ with ε_(M*)(v1) ≤ λ³, and R := Ω ∩ {v + ε_t (τ − τ0)
≤ v1}. Then for every X ∈ R with r(X) ≥ q0,

    |w(X)| ≤ C λ^(N−5) ε_(M*)(v1),                                                                  {#eq:layer-remainder}

C depending on the quantities of [[sec:layer-setting]] and not on λ, v1 or X.

*Proof.* **1. The region.** R ⊂ Ω ∩ {v ≤ v1}, since τ ≥ τ0. Its face {v + ε_t(τ − τ0) = v1} has conormal α = dv + ε_t dτ,
with g0⁻¹(α, α) = −2 ε_t − ε_t²(1 + μ/r²) and |α|_e² = (1 + ε_t)² + 1, the Cartesian components being
α = (1 + ε_t) dτ + x̂·dx. By [[eq:eq-c1]],

    g_λ⁻¹(α, α) ≤ −4s − 4s²(1 + μ/r²) + s((1 + 2s)² + 1) = −2s + 4s³ − 4s² μ/r² < 0,

since −2s + 4s³ = −2s(1 − 2s²) < 0 for 0 < s ≤ 1/2: α is timelike for g_λ. α(Y) = 1 + ε_t(1 + μ/r²) > 0, with Y =
−g0⁻¹ dτ future timelike for g_λ, so v + ε_t(τ − τ0) increases along future causal curves of g_λ and R lies to the past
of its face. R does not meet the outer face of Ω, where v ≥ V + 1 > v1. Its slices are {a ≤ r ≤ ρ(τ)}, ρ(τ) := v1 −
ε_t(τ − τ0) − τ < b(τ), with ρ′ = −1 − ε_t < 0.

**2. The equation.** From [[eq:gauge]] for g_λ and for g_app, with Ric^H(g_λ) = 0 and g_λ = g_app + w,

    −(1/2) g_λ^(ab) ∂_a ∂_b w = f := −Ric^H(g_app) + (1/2)(g_λ^(ab) − g_app^(ab)) ∂_a ∂_b g_app
                                     − [Q(g_λ)(∂g_λ, ∂g_λ) − Q(g_app)(∂g_app, ∂g_app)].            {#eq:layer-w-equation}

**3. Coefficients on R.** For X ∈ R and j ≤ 4, by [[eq:two-scale-derivative]], |∂^j (g_app − g0)(X)| ≤ C Σ_(l≤N)
Σ_(p≤j) λ^(l−p) |∂_θ^p ∂_X^(j−p) g_l|. A θ-derivative removes the means, so for p ≥ 1 the factor is at most C ε_(M*)(v1)
by [[lem:layer-flat]] (a) and [[prop:layer-identification]]; for p = 0 it is bounded globally. Hence |∂^j (g_app − g0)|
≤ C (λ + λ^(1−j) ε_(M*)(v1)) ≤ C for j ≤ 4, by the hypothesis ε_(M*)(v1) ≤ λ³. Step 1 of the proof of
[[thm:uniform-existence]] gives |∂^j w| ≤ C λ^(K−3−j) ≤ C on Ω for j ≤ 3, K ≥ 6. So |∂^j g_λ| ≤ C on R for j ≤ 3,
and |g_λ − g0| ≤ C λ.

**4. The forcing term.** On R, |(g_λ⁻¹ − g_app⁻¹) ∂²g_app| ≤ C |w| (step 3), and the Q-difference is at most
C (|w| + |∂w|) by the mean value theorem in (g, ∂g), as in the proof of [[prop:eq-seed-region]]. Differentiating, for
i ≤ 2, the bound |∂^i f| ≤ |∂^i Ric^H(g_app)| + C Σ_(p≤i+1) |∂^p w| holds, using ∂^q g_app for q ≤ 4 and ∂^q w for
q ≤ 3, bounded by step 3; and the term |∂^i Ric^H(g_app)| is at most C λ^(N−1−i) ε_(M*)(v1) on R
([[lem:layer-flat]] (d)).

**5. The data.** On Σ_τ0 ∩ R = {a ≤ r ≤ v1 − τ0}, by the construction of [[sec:data-proof]]: the difference of g_λ from
G(X, u/λ) has spatial part α dr ⊗ dr, components (τ ·) algebraic in α and the shift, and a τ-derivative of its spatial
part that is a combination of U and its tangential derivatives; the τ-derivatives of its (τ ·) components solve D(g_λ)
− D(G(X, u/λ)) = −D(G(X, u/λ)) with invertible coefficient, where D(G(X, u/λ)) = λ^(N−1) [D^(N−1)] + O(λ^N) with
profiles weighted by (F2) ([[lem:gauge-hierarchy]]); and G(X, u/λ) − g_app is λ^(N+1) times profiles with an
oscillating factor. The higher τ-derivatives on Σ_τ0 follow from [[eq:layer-w-equation]] solved for ∂_τ² (g_λ^(ττ) ≠ 0),
whose coefficients are bounded by step 3. With [[lem:layer-flat]] (e), |∂^p w| ≤ C λ^(N−2−p) ε_(M*)(v1) on Σ_τ0 ∩ R for
p ≤ 3, so that

    E_2(τ0) ≤ C λ^(N−5) ε_(M*)(v1),      E_2(τ) := Σ_(i≤2) (‖∂ ∂^i w(τ)‖ + ‖∂^i w(τ)‖),   norms on R ∩ Σ_τ.

**6. Energy on R.** Apply ∂^α, |α| ≤ 2, to [[eq:layer-w-equation]]. The commutator (1/2)[∂^α, g_λ^(ab)] ∂_a ∂_b w has
terms ∂^p g_λ⁻¹ · ∂^(|α|−p+2) w, 1 ≤ p ≤ 2, at most C Σ_(q≤3) |∂^q w| (step 3). Run the proof of [[lem:energy]] with
g̃ := g_λ on R in place of Ω: the tilted face is spacelike for g_λ with R to its past (step 1), so its flux is
nonnegative and dropped; {r = a} likewise ([[lem:domain]] (b), (e)); the L² boundary term carries ρ′ < 0. So E_2(τ) ≤
C (E_2(τ0) + ∫_(τ0)^τ (E_2 + Σ_(i≤2) ‖∂^i Ric^H(g_app)‖)), and Gronwall's inequality gives E_2(τ) ≤ C (λ^(N−5) +
λ^(N−3)) ε_(M*)(v1) on [τ0, τ_end].

**7. Pointwise.** For X ∈ R with r(X) ≥ q0, the slice R ∩ Σ_(τ(X)) = {a ≤ r ≤ ρ(τ(X))} contains X, so ρ(τ(X)) ≥ r(X) ≥
q0 = a + δ0, and ρ(τ(X)) ≤ b(τ0): its width lies in [δ0, b(τ0) − a]. Sobolev's inequality with a uniform constant on
such annuli (the proof of [[lem:sobolev]]: images of a fixed annulus under radial maps with bounded derivatives)
gives |w(X)| ≤ C Σ_(p≤3) ‖∂_x^p w(τ(X))‖ ≤ C E_2(τ(X)). ∎

**Lemma {#lem:layer-remainder-weak}** (The weighted remainder under a weaker hypothesis.) [[lem:layer-remainder]] holds
with its hypothesis ε_(M*)(v1) ≤ λ³ replaced by ε_4(v1) ≤ λ: for X ∈ R with r(X) ≥ q0,

    |w(X)| ≤ C_L4 λ^(N−5) ε_(M*)(v1),

C_L4 depending on the quantities of [[sec:layer-setting]] and not on λ, v1 or X.

*Proof.* Steps 1, 2, 5 and 7 of the proof of [[lem:layer-remainder]] do not use the hypothesis, step 5 using the
coefficients of step 3 only as below. In step 3, the terms with l = 1 and p ≥ 1 cost j, those with l ≥ 2 are bounded by C
λ^(l−p) through the global bounds of the profiles, and those with p = 0 by C λ; so |∂^j (g_app − g0)| ≤ C (λ + λ^(1−j)
ε_j(v1) + λ^(2−j)), which is bounded for j ≤ 2, since ε_2 ≤ λ, and at most C λ^(2−j) for j = 3, 4, since ε_4 ≤ λ. Order
the energies E^(0), E^(1), E^(2), E^(i) controlling ∂^(i+1) w and ∂^i w. In ∂^i of [[eq:layer-w-equation]], every
coefficient of a w-factor of the same level is a derivative of order at most 2 of g_λ or at most 1 of g_app, bounded;
∂³g_app and ∂⁴g_app occur only in ∂^(i−p) w ∂^(p+2) g_app (p ≥ 1), in ∂^(1+a) g_app ∂^(1+b) w and in the cubic Q-terms,
each multiplying a w-factor of a strictly lower level. So E^(0) obeys [[lem:energy]] with bounded coefficients, E^(0) ≤ C
λ^(N−3) ε_(M*)(v1), and E^(i) ≤ C (E^(i)(τ0) + ∫ (‖∂^i Ric^H(g_app)‖ + Σ_(j<i) L_ij E^(j))) with L_ij ≤ C λ^(j−i);
inductively E^(i) ≤ C λ^(N−3−i) ε_(M*)(v1). In the data of step 5 the coefficients of the same level are bounded and the
large ones multiply lower levels, so the same triangular argument applies there. Step 7 as written. ∎

### The window {#sec:layer-window}

**Lemma {#lem:layer-interpolation}** (Interpolation on a half-line.) Let f be smooth on ℝ with f = 0 on (−∞, v_s], and
m ≥ 2. Put E_f(v) := sup_(v′≤v) |f(v′)| and M_m(v) := sup_(v′≤v) |f^(m)(v′)|. For 0 < i < m and every v,

    sup_(v′≤v) |f^(i)(v′)| ≤ C_(i,m) E_f(v)^(1−i/m) M_m(v)^(i/m),
    C_(i,m) := min_(κ>0) [Λ_(i,m) κ^(−i) + ((m − 1) κ)^(m−i)/(m − i)!],                         {#eq:layer-interpolation}

where Λ_(i,m) := Σ_k |l_k^(i)(0)| for the Lagrange basis (l_k) on the nodes 0, −1, …, −(m − 1). In particular
C_(i,m) ≤ Λ_(i,m) + (m − 1)^(m−i).

*Proof.* If M_m(v) = 0, f is a polynomial of degree less than m on (−∞, v] vanishing on (−∞, v_s], hence zero there,
and so is the left side; likewise if E_f(v) = 0. Otherwise let u ≤ v and h > 0, and let P be the polynomial of degree
at most m − 1 interpolating f at u, u − h, …, u − (m − 1)h, all in (−∞, v]. Then P^(i)(u) = h^(−i) Σ_k f(u − kh)
l_k^(i)(0), so |P^(i)(u)| ≤ Λ_(i,m) E_f(v) h^(−i). The difference g := f − P vanishes at the m nodes, which lie in an
interval I of length (m − 1)h, so by Rolle's theorem g^(i) vanishes at m − i distinct points of I; and (g^(i))^(m−i) =
f^(m), since P has degree at most m − 1. A function with m − i zeros x_1, …, x_(m−i) in I equals, at a point x of I,
its divided difference on the points x_1, …, x_(m−i), x times Π(x − x_j), and that divided difference is a value of its
(m − i)-th derivative divided by (m − i)!. So |g^(i)(u)| ≤ M_m(v) ((m − 1)h)^(m−i)/(m − i)!. With h := κ (E_f(v)/
M_m(v))^(1/m), |f^(i)(u)| ≤ E_f^(1−i/m) M_m^(i/m) (Λ_(i,m) κ^(−i) + ((m − 1)κ)^(m−i)/(m − i)!); minimise over κ.
κ = 1 gives the last claim. ∎

**Corollary {#cor:layer-interpolation-band}** (The costs against the level.) Let c ≥ 1 and m ≥ 2c. Wherever E(v) ≤ 1,

    ε_c(v) ≤ C_c E(v)^(1−c/m),      C_c := Σ_(i≤c) C_(i,m) M_m^(i/m),      M_m := sup |env^(m)|    {#eq:layer-cost-level}

(with C_(0,m) := 1). Let δ ∈ (0, 1/2] and m = 56c. Wherever λ^(3+δ) ≤ E(v) ≤ 1,

    ε_c(v)² ≤ C_c² λ^(−1/8) E(v)².                                                                  {#eq:layer-cost-band}

And for m ≥ 84c and λ ≤ 1, wherever λ^(3+δ) ≤ E(v) ≤ 1,

    ε_c(v)² ≤ C λ^(−1/8) m0(v),                                                                   {#eq:layer-cost-margin}

with C depending on c, m, A, μ0, μ(v_end) and M_m.

*Proof.* By [[lem:layer-interpolation]] for f = env, sup_(v′≤v) |env^(i)| ≤ C_(i,m) E^(1−i/m) M_m^(i/m) ≤ C_(i,m)
M_m^(i/m) E^(1−c/m) for E ≤ 1 and i ≤ c; summing gives [[eq:layer-cost-level]]. For [[eq:layer-cost-band]],
E^(2−2c/m) = E² E^(−1/28) ≤ E² λ^(−(3+δ)/28) and (3 + δ)/28 ≤ 1/8. For [[eq:layer-cost-margin]] we first bound m0
below at every v with E(v) > 0, with no hypothesis on E or λ. The supremum E(v) =: E is attained, env being continuous
and zero on (−∞, v_s]: let v_m ≤ v with |env(v_m)| = E, and put ε_1 := sup_(v′≤v) |env′| > 0. Then |env| ≥ E/2 on
[v_m − E/(2ε_1), v_m], an interval inside (v_s, v] since env = 0 on (−∞, v_s], so ∫_(v_s)^v env² ≥ E³/(8 ε_1), and
ε_1 ≤ C_(1,m) E^(1−1/m) M_m^(1/m) by [[lem:layer-interpolation]], so ∫_(v_s)^v env² ≥ E^(2+1/m)/(8 C_(1,m) M_m^(1/m)).
With √x − 1 = (x − 1)/(√x + 1) ≥ (x − 1)/(1 + √(μ(v_end)/μ0)) for 1 ≤ x ≤ μ(v_end)/μ0, and μ − μ0 = (2/9) A² ∫ env²,

    m0(v) ≥ √(μ/μ0) − 1 ≥ c_m E(v)^(2+1/m),      c_m := A²/(36 μ0 (1 + √(μ(v_end)/μ0)) C_(1,m) M_m^(1/m)).
                                                                                                 {#eq:layer-margin-lower}

So ε_c² ≤ C_c² E^(2−2c/m) ≤ (C_c²/c_m) m0 E^(−(2c+1)/m), and E^(−(2c+1)/m) ≤ λ^(−(3+δ)(2c+1)/m) ≤ λ^(−1/8), since
(2c + 1)/m ≤ 3c/(84c) = 1/28 and (3 + δ)/28 ≤ 1/8. ∎

**Lemma {#lem:layer-levels}** (First reach of a level.) For 0 < y ≤ sup |env| put v*(y) := min{v : E(v) = y}. Then
v_s < v*, |env(v*)| = y, E < y on (−∞, v*), and v* ≤ v′ whenever E(v′) ≥ y. If L > 0 and
L C_(1,m) (2y)^(1−1/m) M_m^(1/m) ≤ y/4, then on [v*, v* + L] env has the sign of env(v*), |env| lies in [3y/4, 5y/4]
and E ≤ 5y/4; and, for M ≤ m/2 and y ≤ 4/5, ε_M(v* + L) ≤ C y^(1−M/m) by [[eq:layer-cost-level]]. Moreover
v* − v_s ≥ (y/C_κ)^(1/κ) for every κ ≥ 1, C_κ := sup |env^(κ)|/κ!.

*Proof.* E is continuous and nondecreasing, E = 0 on (−∞, v_s] and E(v) = sup |env| for v ≥ v_end. If E(v′) ≥ y, the
intermediate value theorem on [v_s, v′] gives a point of (v_s, v′] where E = y. So {E = y} is a nonempty closed set
contained in (v_s, ∞); v* is its least element, v_s < v*, v* ≤ v′ whenever E(v′) ≥ y, and E < y on (−∞, v*). Since
E(v*) = y is the maximum of |env| over (−∞, v*] and |env| ≤ E < y on (−∞, v*), the maximum is taken at v*: |env(v*)| = y.
Let v_+ be the largest point of [v*, v* + L] such that E ≤ 2y on [v*, v_+]; it exists, E being continuous with E(v*) = y
< 2y. On (−∞, v_+], E ≤ 2y, so [[lem:layer-interpolation]] at i = 1 gives |env′| ≤ C_(1,m) (2y)^(1−1/m) M_m^(1/m),
and |env − env(v*)| ≤ L C_(1,m) (2y)^(1−1/m) M_m^(1/m) ≤ y/4 on [v*, v_+]. Since |env(v*)| = y, env keeps the sign of
env(v*) on [v*, v_+], with |env| ∈ [3y/4, 5y/4], and then E ≤ max(y, 5y/4) < 2y on [v*, v_+]. If v_+ < v* + L, the
continuity of E would give E ≤ 2y on a longer interval; so v_+ = v* + L. The bound on ε_M is [[eq:layer-cost-level]] with
E ≤ 5y/4 ≤ 1. Finally all derivatives of env vanish at v_s, so Taylor's formula gives y = |env(v*)| ≤ C_κ (v* − v_s)^κ. ∎

No regularity of env at its edge beyond smoothness is used: the lemmas hold for every C_c^∞ envelope.

### The theorem {#sec:layer-theorem}

**Theorem {#thm:layer}** (Timelike points of the boundary in the layer.) Let μ0 = √72 l5², A > 0, env ∈
C_c^∞([v_start, v_end]) not identically zero, of either sign, v_s := inf supp env, τ0 with v_s − τ0 > √μ0 + 1, K ≥ 6,
and let g_λ, 0 < λ ≤ λ0, be the metric of [[thm:main]]: built with the approximant of [[thm:approximant]] with
N = K + 3 stages and the stage data of [[lem:stage-data]], the correction of [[prop:exact-correction]], and
[[thm:uniform-existence]]. There are λ_L ∈ (0, λ0] and, for every λ ≤ λ_L, an interval W_λ = [v*_λ, v*_λ + 4πλ],
v*_λ the point where |env| first reaches the level λ^14, with v_s < v*_λ, v*_λ → v_s as λ → 0, env of one sign on
W_λ, and W_λ inside the layer v_s < v < v_s + η_λ of [[prop:eq-boundary]] (c), such that for every λ ≤ λ_L and every
x̂ ∈ S³, with ϑ the polar angle of x̂,

    g_λ⁻¹(dΦ0, dΦ0)(v, r_q(v), x̂) = −λ³ A env(v) ν(v − τ0) Re[d(ϑ) e^(iv/λ)] + ρ_λ(v, x̂)   on W_λ,
    sup_(W_λ × S³) |ρ_λ| ≤ δ(λ) λ³ A inf_(W_λ) (|env| |ν(· − τ0)|) inf_ϑ |d(ϑ)|,                       {#eq:layer-main}

where δ(λ) ≤ 1/2 for λ ≤ λ_L and δ(λ) → 0 as λ → 0, with d of [[eq:layer-divergence]], |d| ≥ 8/3 at every angle
([[lem:layer-angular]]), and ν of [[eq:layer-nu]]. So on every column the boundary {x_K = 1} has, in every half of
W_λ, points where it is timelike for g_λ (g_λ⁻¹(dΦ0, dΦ0) > 0) and points where it is spacelike. The boundary is not
spacelike throughout the layer, and not timelike throughout it. The statement holds for every C_c^∞ envelope,
whatever its sign, and every admissible τ0, including (v_s − τ0)/√μ0 = ρ*.

*Proof.* Put M := M* = 2N + 8, m := 56 M, p := 14, κ := 64, y := λ^p, Δτ := τ_end − τ0, ε_t := 2 C1 λ and
L := (4π + 2 C1 Δτ) λ. Fix η1 ∈ (0, min(1, T)] as follows. If (v_s − τ0)/√μ0 ≠ ρ*, then ν(v_s − τ0) ≠ 0
([[prop:layer-linear]] (d)), and η1 is so small that ν_* := min_(v_s≤v≤v_s+η1) |ν(v − τ0)| > 0. If
(v_s − τ0)/√μ0 = ρ*, then ν, as a function of ρ = (v − τ0)/√μ0, has a double zero at ρ* with ν″ := d²ν/dρ² ≠ 0
there, so Taylor's formula gives ν(v − τ0) = (ν″(ρ*)/(2μ0)) (v − v_s)² (1 + o(1)) as v ↓ v_s, and η1 is so small
that the bound |ν(v − τ0)| ≥ ν_2 (v − v_s)² holds on [v_s, v_s + η1], with ν_2 := |ν″(ρ*)|/(4μ0). Each step below
needs λ ≤ Λ for a number Λ > 0 that does not depend on λ; [[sec:layer-threshold]] lists them, and λ_L is their minimum.

*The window.* Let λ ≤ 1 and λ ≤ Λ_0 := min(E(v_s + η1/2)^(1/p), η1/(2(4π + 2 C1 Δτ))), a positive number since
v_s = inf supp env. Then y ≤ E(v_s + η1/2), so v* := v*(y) of [[lem:layer-levels]] exists and v_s < v* ≤ v_s + η1/2;
and L ≤ η1/2. Put W_λ := [v*, v* + 4πλ] and v1 := v* + L = v* + 4πλ + ε_t Δτ. Then W_λ ⊂ [v*, v1] ⊂ (v_s, v_s + η1],
v1 ≤ v_♯ and v1 − v_s ≤ 1. The hypothesis L C_(1,m) (2y)^(1−1/m) M_m^(1/m) ≤ y/4 of [[lem:layer-levels]] reads
8 · 2^(−1/m) C_(1,m) M_m^(1/m) (4π + 2 C1 Δτ) λ^(1−p/m) ≤ 1, which is λ ≤ Λ_4, as p/m < 1. So on [v*, v1] env has
one sign σ ∈ {1, −1}, |env| ∈ [3y/4, 5y/4], and E ≤ 5y/4. By [[lem:layer-interpolation]] and y ≤ 1, for c ≤ M,

    ε_c(v1) ≤ Σ_(i≤c) C_(i,m) (5y/4)^(1−i/m) M_m^(i/m) ≤ y^(1−c/m) Σ_(i≤c) C_(i,m) (5/4)^(1−i/m) M_m^(i/m).

So ε := ε_M(v1) ≤ C_ε y^(1−M/m), C_ε := Σ_(i≤M) C_(i,m) (5/4)^(1−i/m) M_m^(i/m); and each of the five terms of
ε_4(v1) is at most λ/5 when λ ≤ Λ_5′, as p(1 − i/m) > 1 for i ≤ 4, so ε_4(v1) ≤ λ, the hypothesis of
[[lem:layer-remainder-weak]]. As λ → 0, v* → v_s: E(v_s + x) > 0 for every x > 0, and v* ≤ v_s + x once
y ≤ E(v_s + x).

*The boundary points of W_λ.* Every boundary point X = (v, r_q(v), x̂) with v ∈ W_λ lies in the region R of
[[lem:layer-remainder]] with this v1, since τ(X) ≤ τ_end gives v + ε_t (τ(X) − τ0) ≤ v* + 4πλ + ε_t Δτ = v1, and
r(X) = r_q(v) ≥ q0. It lies in the layer: E ≤ 5y/4 on (−∞, v1] by [[lem:layer-levels]], so
μ(v1) − μ0 = (2/9) A² ∫_(v_s)^(v1) env² ≤ (2/9) A² (v1 − v_s) (5y/4)² ≤ (25/72) A² λ^(2p), which is at most 4 μ0 C_Φ λ
when λ ≤ Λ_6, while μ(v_s + η_λ) − μ0 = μ0((1 + 2 C_Φ λ)² − 1) > 4 μ0 C_Φ λ; μ is nondecreasing, so v1 < v_s + η_λ.

*The expansion.* At X, [[lem:layer-inverse]] with k = Σ_j λ^j [g_j] + w, [[cor:layer-expansion]] and
[[lem:layer-remainder-weak]] give

    g_λ⁻¹(dΦ0, dΦ0) = −λ³ A env ν Re[d e^(iθ)] + ρ_λ,      ρ_λ := −m0 + e + q,
    |e| ≤ C_L11 (λ⁴ ε + λ ε² + C_L4 λ^(N−5) ε),      |q| ≤ C_q |k(Φ0♯, ·)| (|k(Φ0♯, ·)| + |k|²),

with C_L11 a constant for which the three bounds of [[eq:layer-expansion]] hold, C_L4 the constant of
[[lem:layer-remainder-weak]] and C_q that of [[eq:layer-inverse]]. The margin satisfies 0 ≤ m0 ≤ C_m0 (5y/4)²,
C_m0 := (A²/(9μ0))(1 + (μ0 μ(v_end))^(1/4)): by [[eq:eq-margin]], concavity of the square root and v − v_s ≤ 1,
√(μ/μ0) − 1 ≤ (μ − μ0)/(2μ0) = (A²/(9μ0)) ∫_(v_s)^v env² ≤ (A²/(9μ0)) E(v)², and
r_q μ′/(2μ) = (A²/9) (μ0 μ)^(1/4) env²/μ ≤ (A²/(9μ0)) (μ0 μ(v_end))^(1/4) E(v)².

*Domination.* On W_λ, |env| ≥ 3y/4 and |d| ≥ d_* := 8/3 ([[lem:layer-angular]]). In the generic case
|ν(v − τ0)| ≥ ν_* on W_λ, since W_λ ⊂ [v_s, v_s + η1]. At ρ*, by [[lem:layer-levels]], the absolute value of
ν(v − τ0) is at least ν_2 (v − v_s)² ≥ ν_2 (v* − v_s)² ≥ ν_2 (y/C_κ)^(2/κ). So in both cases

    λ³ A |env| |ν(v − τ0)| |d(ϑ)| ≥ 10 G λ^(3+z)   on W_λ × S³,      G := 3 A ν_♭ d_*/40,           {#eq:layer-signal}

with z := p and ν_♭ := ν_* in the generic case, and z := p(1 + 2/κ) and ν_♭ := ν_2 C_κ^(−2/κ) at ρ*. When
λ ≤ min(Λ_8a, Λ_8b, Λ_8c, Λ_8d), each of m0, C_L11 λ⁴ ε, C_L11 λ ε² and C_L11 C_L4 λ^(N−5) ε is at most G λ^(3+z), by
the bounds on m0 and ε above. Then, by [[eq:layer-expansion]] and |w| ≤ C_L4 λ^(N−5) ε, the norm of k(Φ0♯, ·) is at
most C_L11 (λ² ε + λ ε² + |w|) ≤ G (λ^(1+z) + 2 λ^(3+z)) ≤ 3 G λ^(1+z), and that of k at most
C_L11 (λ ε + |w|) ≤ 2 G λ^z; so |q| ≤ C_q (9 G² λ^(2+2z) + 12 G³ λ^(1+3z)) ≤ C_q G² (9 + 12 G) λ^(2+2z), as z ≥ 1,
and this is at most G λ^(3+z) when λ ≤ Λ_8e. Hence |ρ_λ| ≤ 5 G λ^(3+z), and by [[eq:layer-signal]] the bound of
[[eq:layer-main]] holds with δ(λ) ≤ 1/2. As λ → 0, each of the five terms divided by λ^(3+z) tends to zero: with
ε ≤ C_ε λ^(p(1−M/m)) and M/m = 1/56, the quotients are at most constant multiples of λ to the powers 2p − 3 − z,
1 + p(1 − M/m) − z, 2p(1 − M/m) − 2 − z, N − 8 + p(1 − M/m) − z and z − 1, which are 11, 0.75, 11.5, N − 8.25 and 13 in
the generic case and 10.5625, 0.3125, 11.0625, N − 8.6875 and 13.4375 at ρ*, all positive since N ≥ 9. So
δ(λ) → 0.

*Sign change.* ν ≤ 0, so −ν = |ν|, and env = σ |env| on W_λ; so the first term of [[eq:layer-main]] is
λ³ A |env| |ν| Re[σ d(ϑ) e^(iv/λ)]: an envelope of the other sign shifts the phase by π. The phase v/λ turns twice on
W_λ, and in each half of W_λ there are points where Re[σ d(ϑ) e^(iv/λ)] = |d(ϑ)| and points where it equals −|d(ϑ)|.
At the former, by [[eq:layer-main]], g_λ⁻¹(dΦ0, dΦ0) ≥ λ³ A |env| |ν| |d| (1 − δ(λ)) > 0: timelike; at the latter it
is at most −λ³ A |env| |ν| |d| (1 − δ(λ)) < 0: spacelike. ∎

The exponent conditions used are, with z := p in the generic case and z := p(1 + 2/κ) at ρ*: 2p > 3 + z (the margin);
4 + p(1 − M/m) > 3 + z (the term λ⁴ ε); 1 + 2p(1 − M/m) > 3 + z (degree two); N − 5 + p(1 − M/m) > 3 + z (the
remainder, which needs N ≥ 9, that is K ≥ 6); z > 1 (the term q); p/m < 1 (the window); p(1 − 4/m) > 1 (the
hypothesis of [[lem:layer-remainder-weak]]); 2p > 1 (the layer); and, for [[thm:layer-past]], p(1 − M/m) > 3 (the
hypothesis of [[lem:layer-remainder-past]]). They are linear in p.

**Corollary {#cor:layer}** (Timelike curves cross the boundary.) Under the hypotheses of [[thm:layer]], at each point of
W_λ where {x_K = 1} is timelike for g_λ, some future timelike curves of g_λ cross it from {x_K > 1} into D_T. So at
equality D_T lacks, inside the layer, the property that [[prop:boundary-spacelike]] gives it for μ0 > √72 l5²: that
every future causal curve which meets the boundary leaves D_T there and does not return.

*Proof.* At such a point p, g_λ⁻¹(dΦ0, dΦ0) > 0, so the hyperplane ker dΦ0 is timelike and dΦ0 takes both signs on the
future timelike cone of g_λ at p. Let γ be the g_λ-geodesic through p with a future timelike velocity X with dΦ0(X) > 0.
Then Φ0 ∘ γ is negative just before p and positive just after: γ passes from {r < r_q}, where x_K = l5² √𝒦 > 1 since
𝒦 = 72 μ²/r⁸ decreases in r, into {r > r_q}, which near p lies in D_T because v(p) < v_s + η_λ < v_end + T. ∎

[[cor:layer]] shows that D_T itself lacks the inner-boundary property at equality; it does not show that the
particular domain of [[prop:eq-domain]] is needed in its place.

**Remark {#rem:layer-mechanism}** (The mechanism.) Expanding around the seed in the amplitude, the margin m0 is of
second degree in the waves (it is the mass increase), while the term of first degree of g_λ⁻¹(dΦ0, dΦ0) on the
boundary is −k(Φ0♯, Φ0♯) with Φ0♯ = ∂_v up to terms of second degree. Its λ¹ part vanishes because W_TT is tangent to
the spheres, and its λ² part vanishes because H_2 lies in 𝔖, by the polarisation of the gauge and the isotropy of Pol⁺
([[prop:layer-linear]]). The first nonzero part is of order λ³: a first harmonic of the phase, proportional to the
double divergence d of the angular tensor of the waves and, through the coupling 2μ0 H_vr/r³ of the vv transport, to
the mass. Near the point where |env| first reaches λ^14 this term exceeds m0 and every error term, and it changes sign
with the phase.

### The solutions from past null infinity {#sec:layer-past}

Here g_λ, 0 < λ ≤ λ_P, is the metric of [[thm:past-construction]], built in [[ch:past-construction]] from the
approximant of [[thm:past-approximant]] with N_P := K + 4 + ⌈4β0⌉ stages, β0 ≥ 2 the number of [[prop:near-region]],
with nothing coming in from past null infinity; A, env, v_s and τ0 are as in [[thm:layer]]. P is the past domain of
[[eq:past-domain]], t = 1 + τ0 − τ, and for v ≤ v_♯ we write P_v := P ∩ {v′ ≤ v}.

**Proposition {#prop:layer-seed-past}** (The seed region for these solutions.) g_λ = g0 on (P ∪ Ω) ∩ {v ≤ v_s}. Hence
[[prop:eq-boundary]] and [[prop:eq-domain]] hold for this g_λ.

*Proof.* The stages of [[thm:past-approximant]] vanish for v ≤ v_s: on P they are transport solutions along ℓ at fixed
v that vanish at past null infinity, and means whose energy on P ∩ {v′ ≤ v} is fixed by their forcing terms there, the
null face {v′ = v} having a flux of one sign as in [[lem:layer-energy-null]]; all forcing terms vanish where env and the
earlier stages vanish. On Ω they continue by [[lem:stage-system]] with these traces. So g_app = g0 on (P ∪ Ω) ∩ {v ≤
v_s}. The solutions g_n of [[prop:far-region]] equal g_app, with their τ-derivative, on Σ̂_(τ_n); the proof of
[[lem:seed-region]] uses only that g0 is vacuum on the region considered, so it applies with v_s in place of v_start and
gives g_n = g0 on P ∩ {τ ≥ τ_n, v ≤ v_s}, and so for g_λ, their limit. On Ω ∩ {v ≤ v_s}, the data of g_λ on Σ_τ0 are
those of g0 together with their τ-derivative (g_λ is smooth on P ∪ Ω), and the proof of [[prop:eq-seed-region]] runs as
written. [[prop:eq-boundary]] and [[prop:eq-domain]] use only [[lem:eq-seed]], [[prop:eq-seed-region]] and the bound
[[eq:eq-c1]] on Ω, which item 4 of [[thm:past-construction]] gives. ∎

**Lemma {#lem:layer-profiles-past}** (The first-degree profiles with nothing coming in.) Let H_1^∞ := H_1, and let
H_(j+1)^∞ solve 𝒯 H_(j+1)^∞ = −R_X H_j^∞ along ℓ with r^(3/2) |H_(j+1)^∞|_cart → 0 along every generator, |·|_cart the
norm of the Cartesian components. Put β_∞(r) := (μ0/3) r⁻³.

(a) In every component the homogeneous solutions of the transport have r^(3/2) |h|_cart tending to a constant that is
zero only for h = 0; so the decay condition determines H_(j+1)^∞.

(b) H_2^∞ is [[eq:layer-h2]] with β_2 replaced by β_∞ and the angular part i r^(1/2) ∫_r^∞ s^(−1/2) (R_X H_1)_AB ds;
it lies in 𝔖, and i Pol(H_2^∞) + D_X H_1 = 0.

(c) The vv, vr, rr components and the trace of H_3^∞ are tr = 0, rr = −a_2 r^(−7/2), vr = −(μ0/3) a_2 r^(−11/2),
vv = −(μ0²/9) a_2 r^(−15/2), with a_2 = A env(v) d(ϑ) as in [[prop:layer-linear]]. At the horizon,

    H_3,vv^∞(v, √μ0, ϑ) = A env(v) d(ϑ) ν_∞,      ν_∞ := −μ0^(−7/4)/9.                            {#eq:layer-nu-infinity}

The H_j^∞ do not depend on τ0. On Ω the profiles of [[thm:past-approximant]] continue by the same transports, so these
formulas hold there.

*Proof.* (a) By [[eq:layer-components]] the homogeneous transports are triangular: (∂_r + 3/(2r)) h_rr = 0, then the vr
and vv equations with h_rr, h_vr as forcing; (∂_r + 1/(2r)) h_rϑ = 0, then the vϑ equation; (∂_r − 1/(2r)) h_AB = 0.
Their solutions are c r^(−3/2) for rr, then for vr and vv c′ r^(−3/2) plus terms decaying faster; c r^(−1/2) for rϑ and
vϑ (plus faster terms); and c r^(1/2) for AB. The Cartesian norm of dv, dr is bounded above and below, and that of dϑ,
of dφ_i over their coefficients, is of order r⁻¹, so in every case r^(3/2) |h|_cart tends to a multiple of |c|.

(b) As in the proof of [[prop:layer-linear]] (b): (R_X H_1) has only rϑ and angular components; H_2,rϑ^∞ = i a_1 r^(−3/2)
is the decaying solution of (∂_r + 1/(2r)) h = −i a_1 r^(−5/2); i a_1 r^(−1/2) β_∞ solves the vϑ equation, since β_∞′ =
−μ0 r⁻⁴, and decays; R_X H_1 contains no derivative ∂_v H_1 (𝒯H_1 = 0 for every v, [[prop:layer-structure]] (a)), so its
angular part is O(r^(−3/2)) and the integral converges, giving a decaying angular part, γ-traceless. The vv, vr, rr
components vanish by (a). Directly, i Pol(H_2^∞)_ϑ = i · i a_1 r^(−3/2) = −(D_X H_1)_ϑ, and the v and r components of
Pol(H_2^∞) vanish.

(c) D_X H_2^∞ = i a_2 (r^(−5/2) β_∞ dv + r^(−7/2) dr) + (a dϑ term), as in [[prop:layer-linear]] (c), and (R_X
H_2^∞)_vv = tr R_X H_2^∞ = 0 since H_2^∞ ∈ 𝔖. The trace of H_3^∞ solves (∂_r + 3/(2r)) tr = 0 and decays, so it vanishes.
By [[eq:layer-bianchi]] at j = 3, with Z_2 = Z_3 = 0 and G_1 = 0, G_2 := i Pol(H_3^∞) + D_X H_2^∞ solves (∇_ℓ + 3/(2r))
G_2 = 0; r^(3/2) |G_2|_cart → 0, since H_3^∞ decays and D_X H_2^∞ = O(r^(−5/2)), while the nonzero solutions of that
transport have r^(3/2) |G|_cart tending to a nonzero constant; so G_2 = 0. Hence H_3,rr^∞ = i (D_X H_2^∞)_r = −a_2
r^(−7/2) and H_3,vr^∞ = i (D_X H_2^∞)_v = −a_2 r^(−5/2) β_∞. The vv equation gives ∂_r (r^(3/2) H_3,vv^∞) = 2μ0 a_2 r⁻⁴
β_∞ = ∂_r(−a_2 β_∞²), and decay fixes r^(3/2) H_3,vv^∞ = −a_2 β_∞² = −(μ0²/9) a_2 r⁻⁶. At r = √μ0 this is −a_2 μ0^(−3/4)
(μ0/3)² μ0⁻³ = a_2 ν_∞. The construction of [[thm:past-approximant]] solves every transport with r^(3/2) Z → 0
([[lem:decay-calculus]] (d)), so the first-degree parts of its profiles are the H_j^∞ (as in
[[prop:layer-identification]] (i)), and on Ω they continue along the same generators. ∎

ν_∞ is the limit of ν(r0) as r0 → ∞, obtained here without that limit; it does not depend on the choice of Pol⁺,
which these solutions do not use.

*Weighted classes.* For c, d ≥ 0 and p real, E_p(ε_c^d) denotes the profiles f on P_v (v ≤ v_♯) with |∂_X^α Ω^β ∂_θ^n
f| ≤ C ε_c(v)^d r^(−p); the classes E_p, L_p, O_p of [[sec:past-approximant]] are the case d = 0.

**Lemma {#lem:layer-flat-past}** (Flat-edge bounds from past null infinity.) With the costs c of [[lem:layer-flat]]:

(a) W_TT ∈ E_(3/2)(ε), χ ∈ E_2(ε²), ĝ_j ∈ E_2(ε) for j ≥ 2;

(b) m_j = r⁻² M_j + m̃_j with |M_j| ≤ C ε², |m̃_j| ≤ C ε² r⁻¹ and |m̃_j| ≤ C ε r^(−7/4), with their derivatives; the
phases and Ψ_j satisfy |∂φ̃_j| ≤ C ε r^(−3/4) and |Ψ̃_j| ≤ C ε r^(−7/4) beyond their leading terms, which are built from
M_j and are O(ε²);

(c) ĝ_j − Re[H_j^∞ e^(iθ)] ∈ E_2(ε²);

(d) ‖∂^i Ric^H(g_app)‖_(L²(P_v ∩ Σ̂_τ)) ≤ C λ^(N_P−1−i) ε_c(v) t^(−3/2);

and on Ω ∩ {v ≤ v_♯} the bounds (a)–(d) of [[lem:layer-flat]] hold, with (e) there replaced by the traces on Σ_τ0 of
(a)–(c) here, except that φ_j and Ψ_j are bounded by C ε, not ε², which is all that [[prop:layer-identification]] and
[[lem:layer-flat]] (c) use of them, every use multiplying them by an oscillating factor or squaring them in q_m.

*Proof.* (a) Induction over the stages as in [[lem:layer-flat]] (a). W_TT = r^(−3/2) F_W with F_W linear in env
([[lem:decay-calculus]] (c)); χ is r⁻² times a function of (v, x̂, θ), quadratic in env (the proof of
[[thm:past-approximant]], stage 0). At stage m the forcing term of [[eq:stage-system]] (c) is in L_3 without the
unknowns and contains them through coefficients in E_(3/2) and E_(5/2) (the count in that proof); by (F1) each monomial
has an oscillating factor, so the forcing term is in E_3(ε), and the transport from infinity, Z = −r^(−3/2) e^(−I)
∫_r^∞ r′^(3/2) e^(I(r′)) S dr′ along the generator at fixed v ([[lem:decay-calculus]] (d)), maps E_3(ε) into E_2(ε),
the weight being that of the generator's v.

(b) M_j := 2 ∫_(−∞)^v 𝒮_(j,3) dv′, with 𝒮_(j,3) the coefficient of r⁻³ in 𝒮_j of the proof of [[thm:past-approximant]],
evaluated at v′; it is of degree two by (F2), so |M_j| ≤ C (v − v_s) ε². The remainders (m̃, φ̃, Ψ̃) solve the remainder
system of the proof of [[thm:past-approximant]], whose estimates are linear in the forcing terms and run on P_v:
[[lem:past-energy]] and [[lem:past-transport]] on P_v, with the null face {v′ = v} to the future of P_v and its flux
kept, as in [[lem:layer-energy-null]]; L0 is tangent to it, so the transport's boundary term vanishes; and the Poincaré
inequality of [[lem:past-sobolev]] (b) holds on the thinner slices with the same constant. With the oscillating remainder
taken as a known forcing term by (a), all forcing terms lie in E_(7/2)(ε²), so the energies and the flux through {v′ = v}
carry ε² with the t-rates of that proof. The flux gives, as in [[lem:layer-null-pointwise]] but integrating from infinity
along γ_Y, with ∫_r^∞ r′⁻³ dr′ = 1/(2r²), the bound |∂^α Ω^β m̃_j| ≤ C ε² r⁻¹; the proof of [[thm:past-approximant]]
gives |m̃_j| ≤ C r^(−5/2); and min(x, y) ≤ (xy)^(1/2) gives C ε r^(−7/4). Then σ̃_j := m̃_j(ℓ, ℓ) + q_j is at most C ε
r^(−7/4) (q_j is quadratic in (m_i, dφ_i), i < j, with no product ∂_v φ_i ∂_v φ_k since g^vv = 0), φ̃_j = −(1/2) ∫_r^∞
σ̃_j gives |φ̃_j|, |∂_v φ̃_j| ≤ C ε r^(−3/4), and Ψ̃_j, by its transport, is at most C ε r^(−7/4).

(c) As in [[lem:layer-flat]] (c), the forcing term of the transport of the difference is a sum of products of two
oscillating factors (E_3(ε²)), of mean-type factors with coefficients carrying an oscillating factor (by (b) and the
coefficient classes E_(3/2), E_(5/2): at most C ε² r^(−13/4)), of R_X(δ_m) (E_3(ε²) by the induction and
[[lem:decay-calculus]] (c)), and of (μ − μ0) times oscillating factors; so it lies in E_3(ε²), and the transport from
infinity, with q = 3 > 5/2 ([[lem:decay-calculus]] (d), and at q = 13/4 the same integral), gives E_2(ε²).

(d) As [[lem:layer-flat]] (d), bounding each monomial in L² on the slices by one weighted factor in L², whose norm has
the t-rate of its class, or in L^∞ (oscillating factors), and the others in L^∞ by their classes; the classes of each
monomial add to at least 3 (R_N, R′_N ∈ E_3, [[thm:past-approximant]]), and a profile of class E_3 has L² norm at most
C t^(−3/2) on a slice of P_v ([[sec:past-approximant]]). On Ω: the proof of [[lem:layer-flat]] with the data on Σ_τ0
replaced by these traces, which are of the stated sizes at the bounded radii of Σ_τ0 ∩ Ω. ∎

**Lemma {#lem:layer-remainder-past}** (The weighted remainder from past null infinity.) Let C_P be such that the
absolute value of (g_λ⁻¹ − g0⁻¹)(α, α) is at most C_P λ t^(−3/2) |α|_e² on P and at most C_P λ |α|_e² on Ω
([[thm:past-approximant]]: g_app⁻¹ − g0⁻¹ is λ times a profile of class E_(3/2); items 3 and 4 of
[[thm:past-construction]]), s := C_P λ ≤ 1/2, ε_t := 2 C_P λ, and
ψ(τ) := 2 t^(−1/2) for τ ≤ τ0, ψ(τ) := 2 + τ − τ0 for τ ≥ τ0. For v1 ≤ v_♯ with ε_(M_P)(v1) ≤ λ³, M_P := 2 N_P + 8,
and R_P := (P ∪ Ω) ∩ {v + ε_t ψ(τ) ≤ v1}: for every X ∈ R_P ∩ Ω with r(X) ≥ q0,

    |w(X)| ≤ C λ^(N_P−3) ε_(M_P)(v1).                                                          {#eq:layer-remainder-past}

*Proof.* As [[lem:layer-remainder]], with four differences. (1) ψ is C¹ and increasing, with ψ′ = t^(−3/2) on P (dt/dτ =
−1) and ψ′ = 1 on Ω, both sides giving ψ = 2 and ψ′ = 1 at τ0. The face {v + ε_t ψ(τ) = v1} has conormal dv + ε_t ψ′ dτ,
and as in step 1 of that proof g_λ⁻¹ of it is at most −2sψ′ + 4s³ψ′³ − 4s²ψ′² μ/r² < 0: the tilt decays exactly as the
perturbation does. ψ ≤ 2 on P, so R_P ⊂ {v ≤ v1} and R_P does not reach the outer boundary B of P, since on R_P, v +
h_P(τ) ≤ v1 + 1/2 < V_P. (2) There are no data: by [[prop:layer-seed-past]], w = 0 on {v ≤ v_s}, and the energy of w on
A_P(τ1) tends to zero as τ1 → −∞ (item 5 of [[thm:past-construction]]), so the energy inequality on R_P ∩ {τ ≤ τ′}
([[lem:past-energy]] on P, [[lem:energy]] on Ω, the tilted face's flux dropped) starts from zero at −∞. (3) On P the
coefficients decay: ∂g_λ and the factor ∂²g_app of (g_λ⁻¹ − g_app⁻¹) ∂²g_app are at most C t^(−3/2), the latter because
its one large part, λ⁻¹ dv dv [∂_θ² g1], carries the waves' amplitude, at most λ⁻¹ ε_(M_P)(v1) t^(−3/2) ≤ C t^(−3/2) on
R_P ([[lem:layer-flat-past]] (a)); so the Gronwall kernel is C t^(−3/2) on P, integrable (∫_(−∞)^(τ0) t^(−3/2) dτ = 2),
and C on Ω. No decomposition of w into a mean and a phase part is needed on R_P: the coefficient of order λ⁻¹ is small
there. The bounds of item 3 of [[thm:past-construction]] on w and ∂w, with those of [[thm:uniform-existence]] on Ω, bound
the nonlinear terms. (4) The forcing term: ‖∂^i Ric^H(g_app)‖_(L²) ≤ C λ^(N_P−1−i) ε t^(−3/2) on R_P ∩ Σ̂_τ
([[lem:layer-flat-past]] (d)), integrable in τ. Gronwall's inequality gives E_2(τ) ≤ C λ^(N_P−3) ε_(M_P)(v1), and step 7
of the proof of [[lem:layer-remainder]] gives [[eq:layer-remainder-past]]. ∎

**Theorem {#thm:layer-past}** (Timelike points for the solutions from past null infinity.) Let μ0 = √72 l5², K ≥ 6, and
let g_λ, 0 < λ ≤ λ_P, be the metric of [[thm:past-construction]]; A, env, v_s and τ0 as in [[thm:layer]]. Then the
conclusions of [[thm:layer]] hold for g_λ with ν(v − τ0) replaced by the constant ν_∞ = −μ0^(−7/4)/9, so with no
exceptional value of τ0, and [[cor:layer]] holds for g_λ.

*Proof.* By [[prop:layer-seed-past]] the layer of [[prop:eq-boundary]] (c) is defined for this g_λ.
[[cor:layer-expansion]] holds at the boundary points with N_P, M_P := 2N_P + 8 and H_j^∞ in place of N, M* and H_j
([[lem:layer-flat-past]] (c) and the continuation on Ω), and with ν_∞ in place of ν(v − τ0) ([[lem:layer-profiles-past]]
(c)). Run the proof of [[thm:layer]] with M := M_P, m := 56 M_P, C_P in place of C1, Δτ replaced by 2 + τ_end − τ0, and
the other parameters as there; so ε_t = 2 C_P λ and v1 := v* + 4πλ + ε_t(2 + τ_end − τ0), which puts every boundary point
X of W_λ in R_P, since ψ(τ(X)) ≤ 2 + τ_end − τ0. The window is that of [[thm:layer]], and on it ε_(M_P)(v1) ≤ C_ε
y^(1−M/m) with p(1 − M/m) = 13.75 > 3, so the hypothesis ε_(M_P)(v1) ≤ λ³ of [[lem:layer-remainder-past]] holds for λ
small; the remainder term is then O(λ^(N_P−3) ε_(M_P)(v1)) by [[lem:layer-remainder-past]], in place of that of
[[lem:layer-remainder-weak]]. Since |ν| = |ν_∞| is constant, only the generic case occurs, with ν_* := |ν_∞|, and the
domination and the sign change are those of the proof of [[thm:layer]]; the exponent conditions listed after
[[thm:layer]] hold with N − 5 replaced by N_P − 3 ≥ K + 9. ∎

### The layer, region by region {#sec:layer-regions}

Put x := v − v_s, and call v a *first-reach point* if |env(v)| = E(v) > E(v′) for every v′ < v. Let

    R(v, x̂) := λ³ A |env(v)| |ν(v − τ0)| |d(ϑ)| / m0(v),

the ratio of the amplitude of the first-degree term to the margin. In the layer, m0 < 2 C_Φ λ + r_q μ′/(2μ).

**Proposition {#prop:layer-regions}** (The layer outside the window.) Let K ≥ 6, N = K + 3, M := M* = 2N + 8, δ ∈ (0,
1/2], P > 4, m := max(56 M, 4 P M, ⌈4 M/δ⌉) and κ := max(64, 8 P, ⌈8/δ⌉), and put γ := 1/10. There is λ_U > 0,
depending on δ and P, such that for λ ≤ λ_U, every v in the layer v_s < v < v_s + η_λ and every x̂ ∈ S³:

(i) (*upper layer*) if E(v) ≥ λ^(3−δ), the boundary is spacelike for g_λ at (v, x̂), whether or not env vanishes at v;

(ii) (*every level*) if v is a first-reach point with λ^P ≤ |env(v)| ≤ λ^(3+δ), then on [v, v + 4πλ] the boundary has,
at x̂, points where it is timelike and points where it is spacelike, also when (v_s − τ0)/√μ0 = ρ*;

(iii) (*the band*) if λ^(3+δ) ≤ E(v) ≤ λ^(3−δ), then g_λ⁻¹(dΦ0, dΦ0) = −m0 − λ³ A env ν Re[d e^(iv/λ)] + ρ with |ρ| ≤
λ^γ m0; where R ≥ 1 + 2λ^γ the boundary has, at x̂, timelike points within [v − πλ, v + πλ], and where R ≤ 1 − 2λ^γ it
is spacelike at (v, x̂).

*Proof.* Throughout, ε := ε_M, and [[lem:layer-inverse]] and [[cor:layer-expansion]] hold on v_s < v ≤ v_♯ with w a
free remainder; in the layer E(v) ≤ 1 for λ small, since by [[eq:layer-margin-lower]] c_m E^(2+1/m) ≤ √(μ/μ0) − 1 ≤
2 C_Φ λ there. Put v1 := v + 4πλ + ε_t (τ_end − τ0). Wherever E(v) ≥ λ^P, the argument of [[lem:layer-levels]] gives
E(v1) ≤ (5/4) E(v), since |env′| ≤ C E^(1−1/m) while E ≤ 2E(v) and λ E(v)^(−1/m) ≤ λ^(1−P/m) → 0; so ε(v1) ≤ C
E(v)^(1−M/m) and ε_4(v1) ≤ C E(v)^(1−4/m) ([[eq:layer-cost-level]]). The margin is controlled by E, not by env(v):
[[eq:layer-margin-lower]] gives m0 ≥ c_m E^(2+1/m). The first-degree term is at most C λ³ E.

(i) Since the region {E ≥ λ^(3−δ)} shrinks as δ grows, it suffices to take δ ≤ 1/4. If ε_4(v1) ≤ λ, which holds where E
≤ λ^(s_A), s_A := (1 + δ)/(1 − 4/m), [[lem:layer-remainder-weak]] bounds w by C λ^(N−5) E^(1−M/m). Each term against
c_m E^(2+1/m), with E ≥ λ^(3−δ): λ³ E is smaller because (3 − δ)(1 + 1/m) < 3, as m ≥ 4M/δ > 3/δ; λ⁴ ε ≤ C λ⁴ E^(1−M/m)
because (3 − δ)(1 + (M + 1)/m) < 4; λ ε² ≤ C λ E^(2−2M/m) because (3 − δ)(2M + 1)/m < 1; and the remainder because
(3 − δ)(1 + (M + 1)/m) < 4 ≤ N − 5. Where E ≥ λ^(s_A), use instead |w| ≤ C λ^(K−3) of [[thm:uniform-existence]]
against c_m E^(2+1/m) ≥ c_m λ^(s_A(2+1/m)): s_A(2 + 1/m) ≤ (5/4)(2 + 1/m)/(1 − 4/m) < 3 ≤ K − 3; the other terms are
handled as before, E ≤ 1. The term q of [[lem:layer-inverse]] is smaller than these. So g_λ⁻¹(dΦ0, dΦ0) ≤ −m0/2 < 0.

(ii) The proof of [[thm:layer]] at the level y := |env(v)| = λ^p, p ∈ [3 + δ, P], in place of λ^14, with v in place of
v* and the m, κ above: since v is a first-reach point, v = v*(y) of [[lem:layer-levels]]; and v lies in the layer,
whose width tends to 0, so the bounds v1 ≤ v_s + η1 that Λ_0 gives in that proof hold for λ small. Its exponent
conditions hold uniformly in p: with z = p or z = p(1 + 2/κ), 2p > 3 + z since p(1 − 2/κ) ≥ (3 + δ)(1 − δ/4) > 3;
4 + p(1 − M/m) > 3 + z since pM/m ≤ 1/4 and 2p/κ ≤ 1/4; 1 + 2p(1 − M/m) > 3 + z since
p(1 − 2M/m − 2/κ) ≥ 3 · 0.93 > 2; N − 5 + p(1 − M/m) > 3 + z since N − 8 ≥ 1 > 1/2; z > 1; p/m < 1; p(1 − 4/m) > 1;
and 2p > 1. At a first-reach point at level λ^p, Taylor's formula gives v − v_s ≥ (λ^p/C_κ)^(1/κ), which is what the
double root uses, and v → v_s as λ → 0.

(iii) Here ε_4(v1) ≤ C λ^((3−δ)(1−4/m)) ≤ λ, so [[lem:layer-remainder-weak]] applies, and every error term is compared
with λ^γ c_m E^(2+1/m) at the same level, E ≥ λ^(3+δ), using M/m ≤ 1/56 and (M + 1)/m, (2M + 1)/m ≤ 1/27: λ⁴ ε ≤ C λ⁴
E^(1−M/m), as 4 − γ > (3 + δ)(1 + (M + 1)/m); λ ε² ≤ C λ E^(2−2M/m), as 1 − γ > (3 + δ)(2M + 1)/m; and the remainder
C λ^(N−5) E^(1−M/m), as N − 5 − γ > (3 + δ)(1 + (M + 1)/m), N − 5 ≥ 4; each with (3 + δ) ≤ 7/2, (7/2)(28/27) < 3.9 and
(7/2)/27 < 0.9. Each comparison is strict in the exponent of λ, so it holds with room for a constant factor in E: for
λ small, |ρ| ≤ λ^γ m0 at every v′ of the layer with λ^(3+δ)/2 ≤ E(v′) ≤ 2 λ^(3−δ).

Now let R(v) ≥ 1 + 2λ^γ, and put I := [v − πλ, v + πλ]. Then env(v) ≠ 0; let σ be its sign. Since R(v) ≥ 1, |env(v)| ≥
m0(v)/(λ³ A |ν| |d|) ≥ c λ⁻³ E(v)^(2+1/m), c := c_m/(A ν_max d_max), where |ν| ≤ ν_max := μ0^(−7/4)/4 for ρ ≥ 1 by
[[eq:layer-nu]], as |2 − 3/ρ − 2/ρ³| ≤ 3 there, and d_max := sup |d| < ∞ by [[eq:layer-d]]. On I, E ≤ (5/4) E(v)
and |env′| ≤ C E(v)^(1−1/m), so over I env changes by a relative amount at most πλ C E(v)^(1−1/m)/|env(v)| ≤ C λ⁴
E(v)^(−1−2/m) ≤ C λ^(4−(3+δ)(1+2/m)) ≤ C λ^(0.49), which is o(λ^γ); in particular env keeps the sign σ on I. Also E(v −
πλ) ≥ E(v) − πλ C E(v)^(1−1/m) = E(v)(1 − o(1)), since |env| reaches E(v) at a point of (−∞, v] and moves by at most πλ C
E(v)^(1−1/m) on I; so every point of I satisfies the bound on ρ above. The margin changes over I by a relative amount at
most C λ E(v)^(−2/m) = o(λ^γ), since |m0′| ≤ C (env² + |env| |env′|) ≤ C E(v)^(2−1/m) on I and m0 ≥ c_m E^(2+1/m) ≥ c_m
(E(v)/2)^(2+1/m) there; and |ν(· − τ0)| by at most C λ/(v − v_s), ν having at most a double zero near v_s, which is
o(λ^γ) since v − v_s ≥ (E(v)/C_κ)^(1/κ) by Taylor's formula at v_s and (3 + δ)/κ < 1/10. So R ≥ 1 + (3/2)λ^γ on I. The
phase v′/λ runs over an interval of length 2π on I, so there are points v′ of I where Re[σ d e^(iv′/λ)] = |d|, and at
them, using ν ≤ 0,

    g_λ⁻¹(dΦ0, dΦ0) = −m0 + λ³ A |env| |ν| Re[σ d e^(iv′/λ)] + ρ ≥ m0 (R − 1 − λ^γ) > 0.

If R(v) ≤ 1 − 2λ^γ, then g_λ⁻¹(dΦ0, dΦ0) ≤ −m0 + R m0 + λ^γ m0 = m0 (R − 1 + λ^γ) < 0. ∎

For the C_c^∞ envelope env_C of [[eq:envelope]], which increases on [1/2, 2] (both factors of β increase on (−1, 0)),
every v with env_C(v) small is a first-reach point, so (ii) covers all levels between λ^P and λ^(3+δ) at the edge
v_s = 1/2.

**Remark {#rem:layer-regions-model}** (Numerical observation.) In a model with every constant equal to one, the
envelope exp(−1/x) at its edge and the derivative count M* of [[lem:layer-flat]], parts (i)–(iii) of
[[prop:layer-regions]], with [[lem:layer-remainder-weak]], covered for K = 6, at λ = 10^(−1000) and λ = 10^(−3000),
every depth from the deepest point at which the error terms fall below the first-degree term up to the depth at which
m0 = 2λ; with the hypothesis of [[lem:layer-remainder]] in place of the weaker one a gap remained for K = 6. No proof
uses this.

**Proposition {#prop:layer-structure}** (The structure of the expansion.) (a) R_X H = −i 𝒯(∂_v H) + Q H and D_X H =
Pol(∂_v H) + q H, where ∂_v is the coordinate derivative of (v, r, ϑ) and Q, q contain no derivative in v.

(b) Write H_j = Σ_k env^(k)(v) c_(j,k)(r, r0, ϑ), r0 = v − τ0, with ∂_v acting both on env and on r0. Then for j ≥ 2,
c_(j,k) = 0 for k > j − 2 and c_(j,j−2) = i^(j−2) c_(2,0); and c_(j,j−3) = (j − 2) i^(j−3) c_(3,0) for j ≥ 3.

(c) On the boundary, for j ≥ 3,

    H_j,vv(v, √μ0, ϑ) = (j − 2) i^(j−3) A d(ϑ) ν(v − τ0) env^(j−3)(v) + Σ_(k<j−3) c_(j,k),vv(√μ0, r0, ϑ) env^(k)(v),

so the top terms of Σ_j λ^j H_j,vv at the horizon are λ³ A d ν Σ_(k≥0) (k + 1)(iλ)^k env^(k), the formal expansion of
λ (i/s)² [A d ν env], where i/s := i(∂_v + i/λ)⁻¹ = λ Σ_(k≥0) (iλ ∂_v)^k.

*Proof.* (a) At the seed the Christoffel symbols [[eq:layer-christoffel]] do not depend on v, and g0°^(vv) = 0, so in
□H = g0°^(ab) ∇_a ∇_b H the derivative ∂_v occurs only in 2 ∂_v ∂_r H from g^vr = 1, in −g0°^(ab) Γ^v_ab ∂_v H =
(3/r) ∂_v H, and in −2 Γ^d_(r·) ∂_v H_(d·), from the connection acting on the indices of ∇_v H with g^vr; together
these are 2 ∂_v (∇_ℓ + 3/(2r)) H = 2i ∂_v 𝒯H. So −(1/2) □H = −i 𝒯(∂_v H) + (terms without ∂_v), and 𝔚 has none. In
D_X H = div H − (1/2) d tr H, ∂_v occurs in g^vr ∂_v H_(r·) = ∂_v H(ℓ, ·) and in −(1/2) dv ∂_v tr H, which is
Pol(∂_v H).

(b) Put K_(j+1) := H_(j+1) − i ∂_v H_j. By (a), 𝒯 K_(j+1) = −Q H_j, and by [[eq:layer-profiles]] K_(j+1) = −i (1 − Π) ∂_v
H_j + i Pol⁺ q H_j at r = r0, Π := Pol⁺ Pol, a projector onto the range of Pol⁺ since Pol Pol⁺ = 1. As 𝒯, Q, q and Pol⁺
contain no ∂_v, they act on each c_(j,k) with r0 as a parameter, and ∂_v H_j = Σ_k env^(k) (∂_(r0) c_(j,k) + c_(j,k−1)).
Writing K_(j+1) = Σ_k env^(k) κ_(j+1,k), we get 𝒯 κ_(j+1,k) = −Q c_(j,k), κ_(j+1,k) = −i(1 − Π)(∂_(r0) c_(j,k) +
c_(j,k−1)) + i Pol⁺ q c_(j,k) at r = r0, and c_(j+1,k) = κ_(j+1,k) + i(∂_(r0) c_(j,k) + c_(j,k−1)). For j ≥ 1 the data
give c_(j+1,k)(r0, r0) = i Π (∂_(r0) c_(j,k) + c_(j,k−1))(r0) + i Pol⁺ q c_(j,k)(r0), in the range of Π. H_1 = env
c_(1,0) and H_2 = env c_(2,0) (the transport of [[eq:layer-profiles]] contains no ∂_v of H_1, as 𝒯H_1 = 0). Induction on
j: if c_(j,k) = 0 for k > j − 2, then for k = j − 1 the forcing −Q c_(j,j−1) is zero and the data are −i(1 − Π)
c_(j,j−2)(r0) = 0, so κ_(j+1,j−1) = 0 and c_(j+1,j−1) = i c_(j,j−2); for k > j − 1 everything vanishes. For the next
family, c_(j+1,j−2) = κ_(j+1,j−2) + i ∂_(r0) c_(j,j−2) + i c_(j,j−3). By the induction hypothesis c_(j,j−2) = i^(j−2)
c_(2,0) and c_(j,j−3) = (j − 2) i^(j−3) c_(3,0); and c_(3,0) = κ_(3,0) + i ∂_(r0) c_(2,0). Then κ_(j+1,j−2) − i^(j−2)
κ_(3,0) solves 𝒯(·) = 0 with data at r0 equal to −(j − 2) i^(j−2) (1 − Π) c_(3,0)(r0) = 0, so κ_(j+1,j−2) = i^(j−2)
κ_(3,0), and c_(j+1,j−2) = i^(j−2)(c_(3,0) − i ∂_(r0) c_(2,0)) + i^(j−1) ∂_(r0) c_(2,0) + (j − 2) i^(j−2) c_(3,0) = (j −
1) i^(j−2) c_(3,0). The motion of r0 cancels.

(c) c_(2,0) has no vv component (H_2 ∈ 𝔖), and c_(3,0),vv(√μ0) = A d ν by [[prop:layer-linear]] (c), (d), where
H_3,vv = env c_(3,0),vv, c_(3,1) = i c_(2,0) having no vv component. With (b) this is the formula, and
λ (i/s)² = λ³ Σ_k (k + 1)(iλ ∂_v)^k since i/s = i/((i/λ)(1 − iλ ∂_v)). ∎

**Remark {#rem:layer-expansion-edge}** (Numerical observation.) Let x_b(λ) be the depth x = v − v_s at which
λ |env′/env| = 1; for env = exp(−1/x^k) near the edge, x_b = (kλ)^(1/(k+1)). Write (i/s) f(v) :=
i ∫_(−∞)^v e^(−i(v−v′)/λ) f(v′) dv′, the operator whose formal expansion is the one in [[prop:layer-structure]] (c).
For env = exp(−1/x) and λ = 10⁻⁶, the top terms of [[prop:layer-structure]] (c), summed to successive orders, agreed
in the window of [[thm:layer]] with the re-summed value λ (i/s)² [env] to 1.6·10⁻⁸; at x = 0.3 λ^(1/2) they were off
by a factor 1.3·10⁸, two consecutive truncations differed by 13 times the first, and the local form λ (i/s̃)² env,
s̃ := env′/env + i/λ, agreed with the re-summed value to 1.8·10⁻³. Below x_b/2 the top terms increased with the order,
above 3 x_b they decreased. No proof uses these observations; the very edge is treated in [[ch:equality-edge]].

**Remark {#rem:layer-edge-data}** (Numerical observation.) Below x_b the vv component of the first-degree data on
Σ_τ0 at r0 = v − τ0 is led by the term λ^(N+1) (N − 1) i^(N−2) env^(N−2) c_(3,0),vv of [[prop:layer-structure]] (b),
taken at r = r0, which comes from stage N's data. With env = exp(−1/x), λ = 10⁻⁶ and N = 9, at x = 0.3 λ^(1/2), this
term, transported along ℓ to the horizon without forcing, exceeded the re-summed first-degree value λ (i/s)² [env] by
a factor of about 2·10⁷ (1.7·10⁻¹³, with the transported coefficient taken at μ0 = 1 and r0 = 5/2, against 8.0·10⁻²¹
for the re-summed term with unit coefficient, per unit of env). No proof uses this.

### The threshold {#sec:layer-threshold}

The proof of [[thm:layer]] uses λ ≤ λ_L, where, with p = 14, m = 56 M, κ = 64, Δτ := τ_end − τ0, the number η1
fixed at the start of that proof, z and ν_♭ as in [[eq:layer-signal]] (z = p and ν_♭ = ν_* :=
min_(v_s≤v≤v_s+η1) |ν(v − τ0)| in the generic case, z = p(1 + 2/κ) and ν_♭ = ν_2 C_κ^(−2/κ) at ρ*), d_* := 8/3,
G := 3 A ν_♭ d_*/40, C_m0 := (A²/(9μ0))(1 + (μ0 μ(v_end))^(1/4)), C_ε := Σ_(i≤M) C_(i,m) (5/4)^(1−i/m) M_m^(i/m),
C_L11 a constant for which the three bounds of [[eq:layer-expansion]] hold, C_L4 the constant of
[[lem:layer-remainder-weak]] and C_q that of [[eq:layer-inverse]],

    λ_L := min{ 1, λ0, 1/(2 C1), Λ_0, Λ_4, Λ_5′, Λ_6, Λ_8a, Λ_8b, Λ_8c, Λ_8d, Λ_8e },
    Λ_0 := min( E(v_s + η1/2)^(1/p), η1/(2(4π + 2 C1 Δτ)) ),
    Λ_4 := [8 · 2^(−1/m) C_(1,m) M_m^(1/m) (4π + 2 C1 Δτ)]^(−m/(m−p)),
    Λ_5′ := min_(i≤4) [5 C_(i,m) (5/4)^(1−i/m) M_m^(i/m)]^(−1/(p(1−i/m)−1)),
    Λ_6 := (288 μ0 C_Φ/(25 A²))^(1/(2p−1)),      Λ_8a := (16 G/(25 C_m0))^(1/(2p−3−z)),
    Λ_8b := (G/(C_L11 C_ε))^(1/(1+p(1−M/m)−z)),      Λ_8c := (G/(C_L11 C_ε²))^(1/(2p(1−M/m)−2−z)),
    Λ_8d := (G/(C_L11 C_L4 C_ε))^(1/(N−8+p(1−M/m)−z)),      Λ_8e := (C_q G (9 + 12 G))^(−1/(z−1)).
                                                                                                    {#eq:layer-threshold}

In the generic case the exponents of Λ_8a, …, Λ_8e are 1/11, 4/3, 1/11.5, 1/(N − 8.25) and −1/13, and
Λ_8a = (6 A ν_* d_*/(125 C_m0))^(1/11); at ρ* they are 1/10.5625, 1/0.3125, 1/11.0625, 1/(N − 8.6875) and −1/13.4375.
Every exponent is defined and every base is positive, E(v_s + η1/2) being positive since v_s = inf supp env; so each Λ
is a positive number, which does not depend on λ. Λ_0 and ν_♭ depend on env and τ0 through η1 and through the level
E(v_s + η1/2), and not only through the norms of env that the other constants involve.

Indeed λ ≤ 1 gives y ≤ 1 and orders the powers of λ that the proof compares; λ ≤ λ0 is [[thm:main]], with the choice
of λ0 in [[sec:eq-setting]]; λ ≤ 1/(2 C1) is the hypothesis s ≤ 1/2 of [[lem:layer-remainder]]; Λ_0 gives
v_s < v* ≤ v_s + η1/2 and L ≤ η1/2, hence v1 ≤ v_s + η1 ≤ v_♯, v1 − v_s ≤ 1 and W_λ ⊂ [v_s, v_s + η1], where ν_♭
bounds |ν| as in [[eq:layer-signal]]; Λ_4 is the hypothesis of [[lem:layer-levels]] with L = (4π + 2 C1 Δτ) λ and
y = λ^p; Λ_5′ makes each term of ε_4(v1) at most λ/5, the hypothesis of [[lem:layer-remainder-weak]]; Λ_6 puts W_λ in
the layer, (25/72) A² λ^(2p) ≤ 4 μ0 C_Φ λ; and each of Λ_8a, …, Λ_8e makes one error term (the margin, at most
C_m0 (5y/4)²; C_L11 λ⁴ ε; C_L11 λ ε²; the remainder C_L11 C_L4 λ^(N−5) ε; the term q) at most G λ^(3+z), a tenth of
the signal's lower bound [[eq:layer-signal]]. When (v_s − τ0)/√μ0 > ρ*, |ν| increases with ρ on ρ > ρ*, by the
formula for dν/dρ in [[prop:layer-linear]] (d); then η1 := min(1, T) may be taken, and ν_* = |ν(v_s − τ0)|.

**Remark {#rem:layer-threshold-size}** (The size of λ_L.) λ0, C1, C_Φ, C_L11, C_L4 and C_q are not evaluated, and η1
depends on env and τ0, so the threshold [[eq:layer-threshold]] is not evaluated either; it is the threshold that the
proof delivers, not the largest λ for which [[thm:layer]] holds. For the envelope env_C of [[eq:envelope]], however, it
is at most 10^(−430) whatever those constants are, for every l5, A, τ0, T and K that [[thm:layer]] admits. Indeed
m ≥ 56 · 26 = 1456, as N ≥ 9. The envelope env_C has support [1/2, 7/2], so v_s = 1/2, and its maximum c_e > 1 is taken
at v = 2 = v_s + 3/2 ([[lem:envelope-constant]]); all its derivatives vanish at v_s, so Taylor's formula gives
c_e ≤ M_m (3/2)^m/m!, that is M_m ≥ m! c_e (2/3)^m, and with m! ≥ (m/e)^m, M_m^(1/m) ≥ (2/3)(m/e) ≥ 357. For the
constant of [[eq:layer-interpolation]] at i = 1: by Lagrange's formula |l_k′(0)| = C(m − 1, k)/k for 1 ≤ k ≤ m − 1, so
Λ_(1,m) ≥ C(m − 1, ⌊(m − 1)/2⌋)/m ≥ 2^(m−1)/m² ≥ 10^430. In the minimum of [[eq:layer-interpolation]], for κ ≤ 1 the
first term is at least Λ_(1,m), and for κ ≥ 1 the second is at least (m − 1)^(m−1)/(m − 1)! ≥ e^(m−2)/(m − 1) ≥ 10^600,
using n! ≤ n^(n+1) e^(1−n). So C_(1,m) ≥ 10^430, the base of Λ_4 exceeds 10^430, and since m/(m − p) ≥ 1,
λ_L ≤ Λ_4 ≤ 10^(−430).
