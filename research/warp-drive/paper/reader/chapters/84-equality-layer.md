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
character in the rest of the layer, down to the level where the expansion in λ stops being ordered
([[prop:layer-regions]]), record the structure of that expansion ([[prop:layer-structure]]), and give the threshold
λ_L of [[thm:layer]] as an explicit formula. The very edge of the layer is the subject of [[ch:equality-edge]].

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
g_λ are those of the approximant, and the τ-derivatives of lapse and shift are fixed by D(g) = 0 with invertible
coefficient ([[sec:data-proof]]), which g0 satisfies.

By items 4 and 5 of [[thm:main]], |g_λ − g0| ≤ C λ, D(g_λ) = 0 and Ric(g_λ) = 0 on Ω. Since g0⁻¹ is bounded on the
compact Ω and inversion is smooth, after shrinking λ0 there is C1 with

    |(g_λ⁻¹ − g0⁻¹)(α, α)| ≤ C1 λ |α|_e²     on Ω, for every covector α,                                {#eq:eq-c1}

|α|_e the Euclidean norm of the Cartesian components of α. The covector field Y := −g0⁻¹ dτ is uniformly timelike for
g0 on Ω, and, λ0 being shrunk once more, future timelike for g_λ. Put B := 1 + sup |r_q′|, the supremum over the
v-range of D_T. For a covector α = dr − β dv with |β| ≤ B, the Cartesian components are α = −β dτ + (1 − β) x̂·dx,
since dv = dτ + x̂·dx and dr = x̂·dx, so |α|_e² = β² + (1 − β)² ≤ B² + (1 + B)², and by [[eq:eq-c1]]

    |g_λ⁻¹(α, α) − g0⁻¹(α, α)| ≤ C_Φ λ,      C_Φ := C1 (B² + (1 + B)²).                                 {#eq:eq-c-phi}

**Lemma {#lem:eq-seed}** (g0 at equality.) (a) For Φ = r − ρ(v), on {r = ρ}, g0⁻¹(dΦ, dΦ) = F(ρ) − 2ρ′. For ρ = r_q
this is [[eq:boundary-margin]], and

    m0(v) := −g0⁻¹(dΦ0, dΦ0) = √(μ/μ0) − 1 + r_q μ′/(2μ),      2 r_q′ = r_q μ′/(2μ).                       {#eq:eq-margin}

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

(d) Write X = X^v ∂_v + X^r ∂_r + X_ang. Then g0(X, X) = −F (X^v)² + 2 X^v X^r + r² |X_ang|²_γ ≤ 0, and dτ(X) = X^v − X^r
> 0, since dτ = dv − dr and X is future directed. If X^v = 0, then |X_ang| = 0 and X^r < 0. If X^v < 0, then X^r < X^v
< 0, so 2 X^v X^r > 2 (X^v)² > F (X^v)², as F < 1, and g0(X, X) > 0, a contradiction. So X^v ≥ 0, with X^v = 0 only for
X a positive multiple of −∂_r; and for X^v > 0 the inequality 2 X^v X^r ≤ F (X^v)² gives X^r ≤ F X^v/2. The bound is
attained by the outgoing null direction ∂_v + (F/2) ∂_r.

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
([[sec:eq-setting]]) and, by continuity, at r = v_s − τ0. Now run the proof of [[lem:energy]] on R in place of Ω, with
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

So the λ-dependent profiles of g_app, whatever they are near v_s, cancel exactly against the remainder w there: g_λ =
g_app + w = g0 on R. Here the principal part of the difference equation is g0 and the face {v = v_s} is exactly null
for it, so no tilt of that face is needed.

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
v_s). If v(p) > v_s: the maximum of two functions strictly decreasing along γ near p is strictly decreasing, so Φ_σ(γ(s))
> 0 for s < s* close to s*, a contradiction. If v(p) < v_s: γ cannot pass from {v > v_s} into {v < v_s}, since on {v ≤
v_s}, where g_λ = g0, v does not decrease ([[lem:eq-seed]] (d)); so γ lies in {v < v_s} on an interval before s*, where
Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there ([[prop:eq-boundary]] (a)): r(p) < √μ0, a contradiction.
If v(p) = v_s: g_λ⁻¹(dΦ1, dΦ1) = −2 c_σ λ < 0 at p (m0 = 0, σ = 0 and g_λ = g0 there), so Φ1 decreases strictly along
γ near p. Points of γ before p with v > v_s would have Φ_σ = Φ1 > Φ1(p) = 0, which is impossible; so γ approaches p
within {v ≤ v_s}, where Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there: r(p) < √μ0, a contradiction. ∎

The statement concerns the inner boundary only; the face {v = v_end + T} of D_T^λ is not treated.

**Remark {#rem:eq-why-layer}** (What the bounds of [[thm:main]] leave open.) On v_s < v < v_s + η_λ the margin m0 and
the perturbation g_λ⁻¹ − g0⁻¹ both vanish to every order at v = v_s ([[lem:eq-seed]] (c), [[prop:eq-seed-region]]).
[[thm:main]] bounds the perturbation by C λ, uniformly in v, while deciding the sign of g_λ⁻¹(dΦ0, dΦ0) needs a bound by
a fraction of m0, pointwise in v near v_s. The sections from [[sec:layer-setting]] on obtain the part of the
perturbation of first degree in the waves exactly and bound the rest by the margin's own order.

### The spheres' horizon at equality {#sec:eq-horizon}

Let C_θ be the constant C3 of [[eq:theta-plus-close]] in the proof of [[prop:one-zero]], so that |θ⁺_λ − θ⁺_0| and
|∂_r(θ⁺_λ − θ⁺_0)| are at most C_θ λ on the columns, θ⁺_0 := θ⁺(g0); let R_max be the largest r on the columns, c_θ :=
3/(R_max² + μ(v_end)), and C_h := C_θ/c_θ.

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

holds: −θ⁺_0(r_q) = 3 d_h (√μ + r_q)/(r_q (r_q² + μ)), and (√μ + r_q) μ − r_q (r_q² + μ) = μ√μ − r_q³ = d_h (μ + √μ r_q
+ r_q²). The right side is nonnegative, so θ⁺_λ(r_q) ≤ −3 d_h/μ + C_θ λ ≤ −3 C′ λ/μ(v_end) + C_θ λ < 0, while θ⁺_λ > 0
at √μ + C_h λ; the intermediate value theorem and (a) give exactly one zero. ∎

So at equality item 6 of [[thm:main]] holds in this form: exactly one zero on the columns with v ≤ v_s (at the boundary
itself) and on those with √μ(v) − r_q(v) ≥ C′ λ, a condition that fails only on a set of v whose width tends to 0 with
λ; at most one zero, within C_h λ of √μ(v), everywhere.

