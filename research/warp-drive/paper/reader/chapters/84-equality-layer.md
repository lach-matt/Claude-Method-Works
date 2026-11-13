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

    E(v) := sup_(v′≤v) env(v′),      ε_c(v) := Σ_(i≤c) sup_(v′≤v) |env^(i)(v′)|,                     {#eq:layer-costs}

both continuous, nondecreasing and zero for v ≤ v_s. A quantity is *of degree at least two* if, with μ − μ0 counted as
of degree two, it is a sum of products of at least two factors of the form A env^(i) times smooth coefficients. A
profile H(v, r, ϑ) e^(iθ), H complex, is the complex form of a first harmonic of the phase, and its real part is meant.
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
independently of λ), the numbers M and C of [[thm:uniform-existence]] and C1 of [[eq:eq-c1]]; never on λ, v, v1 or
the point.

### The seed's operators on one harmonic {#sec:layer-operators}

In (v, r, ϑ, φ1, φ2), with F° := 1 − μ0/r² and Γ̊ the Christoffel symbols of the round metric γ, the Christoffel
symbols of g0° that do not vanish are

    Γ^v_vv = μ0/r³,   Γ^r_vv = F° μ0/r³,   Γ^r_rv = −μ0/r³,   Γ^v_AB = −r γ_AB,   Γ^r_AB = −r F° γ_AB,
    Γ^A_rB = δ^A_B/r,   Γ^A_BC = Γ̊^A_BC;                                                              {#eq:layer-christoffel}

in particular Γ^A_(av) = 0 for every index a, and Γ^v_(rv) = Γ^v_(rr) = Γ^r_(rr) = 0. Each is read from Γ^σ_ab = (1/2)
g^(σd)(∂_a g_db + ∂_b g_da − ∂_d g_ab) with g_vv = −F°, g_vr = 1, g_rr = 0, g_AB = r² γ_AB and g^vv = 0, g^vr = 1,
g^rr = F°; for instance Γ^r_rv = (1/2) ∂_r g_vv = −μ0/r³ and Γ^v_AB = −(1/2) ∂_r g_AB.

For a symmetric 2-tensor h let

    Pol(h) := h(ℓ, ·) − (1/2) dv tr h,      D_X(h) := div h − (1/2) d tr h,      𝒯 h := −i (∇_ℓ h + (3/(2r)) h),
    R_X(h) := −(1/2) □h + 𝔚(h),      𝔚(h)_mn := −R_m^a_n^b h_ab,                                       {#eq:layer-operators}

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
    Pol(H)_v = −(1/2)(F° H_rr + r⁻² γ^(AB) H_AB),   Pol(H)_r = H_rr,   Pol(H)_ϑ = H_rϑ.               {#eq:layer-components}

(d) If h is in 𝔖, then (dRic^H h)_vv = 0 and tr dRic^H h = 0; the same holds for R_X h.

(e) If h has only angular components, then (□h)_vA = 0 and 𝔚(h)_vA = 0 for every angular A.

*Proof.* (a) At a vacuum metric, with D(g0°) = 0 and the gauge relative to g0°, the variation of the Christoffel symbols
is δΓ^ρ_ab = (1/2)(∇_a h^ρ_b + ∇_b h^ρ_a − ∇^ρ h_ab), so dD^ρ = g0°^(ab) δΓ^ρ_ab = ∇_a h^(aρ) − (1/2) ∇^ρ tr h. The
variation of Ricci is ∇_ρ δΓ^ρ_mn − ∇_n δΓ^ρ_(ρm). Commuting the derivatives in ∇_ρ ∇_m h^ρ_n by the Ricci identity, and
using Ric(g0°) = 0, it equals (1/2)(∇_m dD_n + ∇_n dD_m) − (1/2) □h_mn − R_m^a_n^b h_ab. The variation of the gauge term
of [[eq:gauge]] at D = 0 is (1/2)(∇_m dD_n + ∇_n dD_m), since ∇̂ = ∇ at g0°. The difference is (a).

(b) For h = H e^(ikv/λ), ∇_a h = (∇_a H + i k λ⁻¹ (∂_a v) H) e^(ikv/λ), and g0°⁻¹(dv, dv) = 0, ∇ dv being symmetric with
ℓ^a ∇_a ∂_b v = 0 ([[prop:vaidya]] (c)), and □v = 3/r ([[sec:stage-zero]]). Hence

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

(e) By the same parity, R_(vAϑB) h^(AB) = 0, three indices being angular, so 𝔚(h)_vA = 0. For h with only angular
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

    i Pol(Z_j) + div Gt(Z_(j−1)) = −i (∇_ℓ + 3/(2r)) G_(j−1) − (1/2) □G_(j−2),                         {#eq:layer-bianchi}

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
    Y_AB = (1/3)(−F V_r − 2 V_v) r² γ_AB,   tr_(g0) Y = −V_r − 2 V_v,                                 {#eq:layer-pol-plus}

F := 1 − μ/r² at the point; in particular Pol Y = V, and the γ-traceless angular part of Y vanishes.

*Proof.* Pol is onto ([[lem:stage-data]] (i)), so Pol Pol^T is invertible, Pol⁺ maps onto the range of Pol^T, and Pol
is injective there. So it suffices to show Pol Y = V and that Y lies in the range of Pol^T. First, by
[[eq:layer-components]] (which hold at g0 as well, with F in place of F°): Pol(Y)_r = Y_rr = V_r, Pol(Y)_ϑ = Y_rϑ = V_ϑ,
and Pol(Y)_v = Y_rv − (1/2) tr Y = −V_r/2 + (V_r + 2 V_v)/2 = V_v, with tr Y = 2 Y_vr + F Y_rr + r⁻² γ^(AB) Y_AB = −V_r
+ F V_r − F V_r − 2 V_v. Second, rotate the Cartesian coordinates so that at the point x̂ = e1 and ∂_ϑ = r ∂_(x2); then
ℓ = −∂_τ + ∂_1, dv = dτ + dx1, and g0⁻¹ = η⁻¹ − m L0 ⊗ L0, m := μ/r², L0 = ∂_τ − ∂_1. The Frobenius pairing of Pol(Y)
with β is Σ_(a,b) Y_ab ((1/2)(ℓ^a β_b + ℓ^b β_a) − (1/2)(β_0 + β_1) g0^(ab)), so the range of Pol^T consists of the arrays

    Z_00 = −β_0 + s(1 + m)/2,   Z_01 = (β_0 − β_1)/2 − s m/2,   Z_11 = β_1 − s(1 − m)/2,
    Z_02 = −β_2/2,   Z_12 = β_2/2,   Z_22 = Z_33 = Z_44 = −s/2,   Z_0j = −β_j/2,  Z_1j = β_j/2  (j = 3, 4),

s := β_0 + β_1, all other entries zero. The Cartesian components of Y follow from ∂_v = ∂_τ, ∂_r = −∂_τ + ∂_1,
∂_ϑ = r ∂_2: Y_00 = V_r/4, Y_01 = −V_r/4, Y_11 = V_r/4, Y_02 = −V_ϑ/(2r), Y_12 = V_ϑ/(2r), Y_22 = Y_33 = Y_44 =
((m − 1) V_r − 2 V_v)/3, and no other entries. This is of the form above with β_2 = V_ϑ/r, β_3 = β_4 = 0, s :=
−2((m − 1) V_r − 2 V_v)/3, β_0 := s(1 + m)/2 − V_r/4 and β_1 := V_r/4 + s(1 − m)/2, whose sum is s as required; the
entries Z_00, Z_11, Z_22 then hold by construction, and Z_01 = (β_0 − β_1)/2 − s m/2 = −V_r/4. ∎

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

    𝒯 H_(j+1) = −R_X H_j   along ℓ,      H_(j+1) = i Pol⁺(D_X H_j)   on Σ_τ0, at r = r0 := v − τ0,    {#eq:layer-profiles}

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

    tr H_3 = 0,   H_3,rr = −a_2 r^(−7/2),   H_3,vr = −a_2 r^(−5/2) β_2(r),   H_3,vv = −a_2 r^(−3/2) β_2(r)².   {#eq:layer-h3}

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
H_1)_AB is (tr R_X H_1 = 0). So H_2 is in 𝔖. By [[lem:layer-bianchi]] (b) with J = 2 (Z_1 = Z_2 = 0, G_0 = 0, and G_1
= 0 at r0 since Pol Pol⁺ = 1), G_1 = i Pol(H_2) + D_X H_1 = 0 on Ω.

(c) For h in 𝔖 the same computation as in (a) gives (div h)_v = r⁻² div_γ(h_(v·)) and (div h)_r = r⁻² div_γ(h_(r·)),
the divergences on S³ of the covectors h_(vA) and h_(rA): the terms with Γ^A_(·v) vanish, h_vv = h_vr = h_rr = 0, and
the term −Γ^E_(Ar) h_(BE) contracted with g0°^(AB) is a trace. With tr H_2 = 0 and div_γ(d_1 dϑ) = d, this is the
stated form of D_X H_2. By (b) and [[lem:layer-seed-operators]] (d), (R_X H_2)_vv = 0 and tr R_X H_2 = 0. Let H_3 be
given by [[eq:layer-profiles]]. Its data at r0 are, by [[eq:layer-pol-plus]] with V_v = i a_2 r0^(−5/2) β_2(r0) and V_r
= i a_2 r0^(−7/2): H_3,vv = i V_r/4 = −a_2 r0^(−7/2)/4 and tr H_3 = i(−V_r − 2 V_v) = a_2 (r0^(−7/2) − r0^(−7/2)) = 0.
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

The admissible values are r0 = v − τ0 ≥ v_s − τ0 > √μ0 + 1, that is ρ > 1 + μ0^(−1/2). The coefficient ν depends on
τ0, through r0, and on the Euclidean structure used to define Pol⁺; the one fixed in [[lem:stage-data]] is used
throughout. A tensor T with d = 0 gives no λ³ term: for instance (a, b) = ((1 + 3 cos 2ϑ)/2, (1 − 3 cos 2ϑ)/2) has d_1 = 0.

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

    g_λ⁻¹(dΦ0, dΦ0) = −m0 − k(Φ0♯, Φ0♯) + q,      |q| ≤ C |k(Φ0♯, ·)| (|k(Φ0♯, ·)| + |k|²),             {#eq:layer-inverse}

where C depends on the bounds of g0⁻¹ and g_λ⁻¹ on Ω, and |k| ≤ 1.

*Proof.* From g_λ = g0 + k, g_λ⁻¹ − g0⁻¹ = −g0⁻¹ k g_λ⁻¹, and substituting this once more for g_λ⁻¹ on the right,
g_λ⁻¹ = g0⁻¹ − g0⁻¹ k g0⁻¹ + g0⁻¹ k g0⁻¹ k g_λ⁻¹. Contract with dΦ0 twice: the first two terms give −m0 − k(Φ0♯, Φ0♯),
and the third is q := k(Φ0♯, g0⁻¹ k g_λ⁻¹ dΦ0). The same identity applied to g_λ⁻¹ dΦ0 gives |k(g_λ⁻¹ dΦ0, ·)| ≤
|k(Φ0♯, ·)| + C |k| |k(Φ0♯, ·)| + C |k|³, and |k|³ ≤ |k|². ∎

