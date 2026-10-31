# EQUALITY5 -- the boundary and the horizon at μ0 = √72 l5²

Status: written (D346); verified (D347): verifier 163 found no blocking or major gap, and its findings (four minor,
nine nits) are seated (EQ6). Check script: `checks/eq5.py` E1–E6 (computed), all pass, every control fails.

The paper (`paper/RESPONSE-HL-5D.md`) proves Theorem 1 for μ0 ≥ √72 l5², but its Proposition 3.2 (the boundary
x_K = 1 is spacelike for g_λ) and Proposition 3.3 (one zero of the outgoing expansion per column) assume μ0 > √72 l5²,
and section 9 lists "the boundary at equality" as not proved. This note settles what can be settled at equality,
μ0 = √72 l5² throughout:

1. g_λ equals the seed exactly on Ω ∩ {v ≤ v_s}, v_s := inf supp env (Proposition E.2). So on that portion the
   boundary is the seed's horizon, null for g_λ, and no future causal curve crosses it outward.
2. After the shell has started, the boundary is spacelike for g_λ on {v ≥ v_s + η} once λ ≤ λ_η (Proposition E.3);
   the layer v_s < v < v_s + η_λ in between, whose width η_λ tends to 0 with λ, is not decided by the bounds of
   Theorem 1, and Remark E.6 says why.
3. A domain D_T^λ ⊂ D_T, within cλη* of D_T, inside {x_K ≤ 1}, whose inner boundary no future causal curve of g_λ
   enters (Proposition E.4): at equality, the inner-boundary property that Proposition 3.2 gives D_T when μ0 >
   √72 l5² (no entry, hence no return) holds for a domain O(λ)-close to D_T.
4. The spheres' horizon at equality (Proposition E.5): at most one zero per column, within Cλ of √μ(v); exactly one,
   R_λ = √μ0 exactly, on the columns with v ≤ v_s; exactly one on the columns that reach across √μ(v) + Cλ and have
   √μ(v) − r_q(v) ≥ C'λ.

## 0. Setting

Notation as in the paper, sections 2.2–2.5 and 3. In the coordinates (v, r, angles), v = τ + r, the metric (2.3) is

    g0 = −F dv² + 2 dv dr + r² (round metric of S³),     F := 1 − μ(v)/r²                                      (0.1)

(computed: eq5 E1). μ(v) = μ0 + (2/9) A² ∫_(−∞)^v env², so μ' = (2/9) A² env² ≥ 0. At equality r_q(v) = (μ0 μ(v))^(1/4),
Φ0 := r − r_q(v), and the boundary is {Φ0 = 0}. Put v_s := inf supp env; v_s ≥ v_start, and μ = μ0 on {v ≤ v_s}.

Theorem 1's hypotheses hold with v_start replaced by v_s: env ∈ C_c^∞([v_s, v_end]), μ = μ0 on {v ≤ v_s}, and v_s −
τ0 ≥ v_start − τ0 > √μ0 + 1; Ω (supplement (1.1)) and λ0, C do not involve v_start. The construction uses v_start only
through supp env: the stage data of the supplement's Lemma 6.2 (iii) and the correction U of its Proposition 6.5 are
solved radially from zero data at r = a, with sources that vanish where the waves do, and the oscillating profiles and
the means vanish for v < v_s (the supplement's Proposition 8.2's proof). So the g_λ that Theorem 1 builds is the same
whether v_start or v_s is used, and λ0, C and Ω are its constants and domain (verifier 163's MINOR-1). Its data on
Σ_τ0 ∩ {r < v_s − τ0} are the seed's as a metric with its first τ-derivative, not only as Cauchy data: there U = 0 and
g_app = g0, the lapse and shift are those of g_app, and the τ-derivatives of lapse and shift are fixed by D(g) = 0
with invertible coefficient, which g0 satisfies (the proof of Theorem D, supplement section 6.4; MINOR-2). Item 4
gives |g_λ − g0| ≤ C λ on Ω; item 5 gives D(g_λ) = 0 and Ric(g_λ) = 0. Shrinking λ0, |g_λ⁻¹ − g0⁻¹| ≤ C1 λ on Ω (C1
from C and the bound of g0⁻¹ on the compact Ω), and Y := −g0⁻¹ dτ, uniformly timelike for g0 on Ω, is future
timelike for g_λ too (NIT-7). For a covector α = dr − β(v) dv with |β| ≤ B,
the difference of g_λ⁻¹(α, α) and g0⁻¹(α, α) is at most C_Φ λ in absolute value, C_Φ depending on C1 and B only;
below B := 1 + sup |r_q'|, sup over the v-range of D_T.

**Lemma E.1 (g0 at equality; computed eq5 E1–E2, E4).**

(a) For Φ = r − ρ(v), on {r = ρ}: g0⁻¹(dΦ, dΦ) = F(ρ) − 2ρ'. For ρ = r_q this is (3.1), and at equality

    m0(v) := −g0⁻¹(dΦ0, dΦ0) = √(μ/μ0) − 1 + r_q μ'/(2μ),     2 r_q' = r_q μ'/(2μ).                          (0.2)

(b) m0 = 0 on {v ≤ v_s}; m0 > 0 on {v > v_s}; and m0 ≥ δ_η := √(μ(v_s + η)/μ0) − 1 > 0 on {v ≥ v_s + η}, η > 0.

(c) m0 and every derivative of m0 vanish at v = v_s.

(d) For every future causal vector X of g0: dv(X) ≥ 0 and dr(X) ≤ (F/2) dv(X).

(e) Y := −g0⁻¹ dτ is future timelike, and for Φ = r − ρ(v) with ρ' ≥ 0, dΦ(Y) = −μ/r² − ρ' < 0.

*Proof.* (a) is computed (E1, E2). (b): on v ≤ v_s, μ = μ0 and μ' = 0. For v > v_s, env does not vanish identically on
(v_s, v): otherwise env = 0 on (−∞, v), an open set, and v_s ∉ supp env. So μ(v) − μ0 = (2/9) A² ∫_(v_s)^v env² > 0;
μ' ≥ 0, μ is nondecreasing, and m0(v) ≥ √(μ(v)/μ0) − 1 ≥ δ_η for v ≥ v_s + η. (c): env vanishes on (−∞, v_s), so env
and all its derivatives vanish at v_s; hence μ − μ0 and μ' and all their derivatives vanish there. (d): with X =
X^v ∂_v + X^r ∂_r + (angular), g0(X, X) = −F (X^v)² + 2 X^v X^r + r² |X_ang|² ≤ 0 and dτ(X) = X^v − X^r > 0. If X^v = 0,
then |X_ang| = 0 and X^r < 0. If X^v < 0, then X^r < X^v < 0 (as X^v − X^r > 0), so 2 X^v X^r > 2 (X^v)² > F (X^v)²
(F < 1), and g0(X, X) > 0, a contradiction. So X^v ≥ 0 (= 0 only for X proportional to −∂_r), and for X^v > 0,
2 X^v X^r ≤ F (X^v)² gives X^r ≤ F X^v/2. E4 samples the cone and finds no exception; the bound is attained on the
outgoing null direction ∂_v + (F/2) ∂_r. (e): g0⁻¹(dτ, dτ) = −1 − μ/r² (Prop. 2.2 (d)), dτ(Y) = 1 + μ/r² > 0, and
dΦ(Y) = −g0⁻¹(dτ, dr) + ρ' g0⁻¹(dτ, dv) = −μ/r² − ρ' (g0⁻¹(dτ, dv) = dτ(ℓ) = −1, Prop. 2.2 (c)). ∎

## 1. The seed region is exact

**Proposition E.2.** g_λ = g0 on Ω ∩ {v ≤ v_s}. In particular g_λ − g0 and all its derivatives vanish on Ω ∩
{v = v_s}, and on Ω ∩ {v ≤ v_s} the metric g_λ is five-dimensional Schwarzschild–Tangherlini of mass μ0, the seed.

*Proof.* Let R := Ω ∩ {v ≤ v_s}, compact, and u := g_λ − g0 on R. On R, μ' = 0, so Ric(g0) = 0 and Ric^H(g0) =
Ric(g0) = 0 (section 2.5: D(g0) = 0). D(g_λ) = 0 and Ric(g_λ) = 0 give Ric^H(g_λ) = 0. Subtracting (2.7) for the two
metrics,

    −(1/2) g0^(ab) ∂_a ∂_b u = (1/2) (g_λ^(ab) − g0^(ab)) ∂_a ∂_b g_λ − Q(X; g_λ)(∂g_λ, ∂g_λ) + Q(X; g0)(∂g0, ∂g0) =: f.

g_λ⁻¹ − g0⁻¹ = −g_λ⁻¹ u g0⁻¹, and Q is a polynomial in ∂g with coefficients rational in g and smooth in X; writing the
Q-difference as ∫_0^1 (d/ds) Q(X; g0 + s u)(∂(g0 + s u), ∂(g0 + s u)) ds, with g0 + s u Lorentzian and in a compact set
for λ ≤ λ0 (|u| ≤ C λ), gives |f| ≤ K_λ (|u| + |∂u|) on R, K_λ finite for each λ (∂²g_λ is bounded on the compact R).

The data vanish: Σ_τ0 ∩ R = {τ = τ0, a ≤ r ≤ v_s − τ0}, where (g_λ, ∂_τ g_λ) = (g0, ∂_τ g0) for r < v_s − τ0
(Theorem 1 item 2) and, by continuity, at r = v_s − τ0. Now run the proof of the supplement's Lemma 2.3
(`N1STAR-PROOF.md`, the energy inequality) on R in place of Ω, with gt := g0 and the multiplier Y := −g0⁻¹ dτ. The
boundary of R ∩ {τ0 ≤ τ' ≤ τ} consists of Σ_τ0 ∩ R, Σ_τ ∩ R, parts of ∂Ω other than Σ_τ0 (spacelike with Ω, hence R,
to their past: Lemma 1.1 there), and a part of the hypersurface {v = v_s}. The last is null for g0 (dv is null: Prop.
2.2 (c)) with R to its past (v increases along future causal curves, Lemma E.1 (d)); the flux of the energy current
J = T(Y, ·) through it is ∫ T(Y, N) ≥ 0, N its future null generator, by the dominant energy property of T_ab = ∂_a u
∂_b u − (1/2) g0_ab g0(du, du) for future causal Y and N. So, as there, this flux is dropped. The L² term: the slice
R ∩ Σ_τ is {a ≤ r ≤ v_s − τ} (R does not meet Ω's outer face), whose outer radius decreases with τ, so the boundary
term in d_τ ‖u‖² is ≤ 0. Hence (2.2) holds on R:

    ‖∂u(τ)‖ + ‖u(τ)‖ ≤ C ( ‖∂u(τ0)‖ + ‖u(τ0)‖ + ∫_(τ0)^τ ‖f‖ ) ≤ C K_λ ∫_(τ0)^τ (‖∂u‖ + ‖u‖),

norms on R ∩ Σ_τ, and Gronwall's lemma gives u = 0 on R. The derivatives of u vanish on Ω ∩ {v = v_s} because u is
smooth on Ω and vanishes on the set {v < v_s} ∩ Ω, whose closure contains Ω ∩ {v = v_s}. ∎

So the λ-dependent profiles of g_app, whatever they are near v_s, cancel exactly against the remainder w there: g_λ =
g_app + w = g0 on R. The supplement's Lemma 9.2 proves the same on its domain P, with the solution's own metric as
principal part and so with an ε-tilted spacelike face; here the principal part is g0, the face {v = v_s} is exactly
null for it, and no tilt is needed (NIT-4).

## 2. The boundary

**Proposition E.3 (the boundary at equality).**

(a) On {v ≤ v_s} the boundary {Φ0 = 0} is {r = √μ0}, the seed's horizon, null for g_λ. A future causal curve of g_λ
that starts in {r ≤ √μ0} stays there while v ≤ v_s: nothing crosses this portion from inside to outside.

(b) For η > 0 put λ_η := min(λ0, δ_η/(2 C_Φ)). For λ ≤ λ_η the boundary is spacelike for g_λ on {v ≥ v_s + η}, with
g_λ⁻¹(dΦ0, dΦ0) ≤ −δ_η/2, and every future causal curve that meets it there leaves D_T there (Proposition 3.2's
argument).

(c) For each λ, the portion of the boundary on which these bounds do not decide its causal character lies in v_s < v <
v_s + η_λ, η_λ := inf{η > 0 : δ_η ≥ 2 C_Φ λ}, that is μ(v_s + η_λ) = μ0 (1 + 2 C_Φ λ)²; η_λ → 0 as λ → 0.

*Proof.* (a) By Proposition E.2, g_λ = g0 there, r_q = √μ0 (μ = μ0) and (0.2) gives m0 = 0: null. By Lemma E.1 (d), along
a future causal curve in Ω ∩ {v ≤ v_s}, dr ≤ (F/2) dv with dv ≥ 0 and F = 1 − μ0/r² < 0 for r < √μ0. So where r < √μ0,
r does not increase; a curve from {r < √μ0} therefore stays in {r ≤ r(start)}. From a point with r = √μ0: put f := r −
√μ0; where f > 0 and f is small, F ≤ 2f/√μ0, so df ≤ (f/√μ0) dv, and f₊ e^(−v/√μ0) does not increase; it starts at 0,
so f ≤ 0 while v ≤ v_s. (b) For v ≥ v_s + η, g_λ⁻¹(dΦ0, dΦ0) ≤ −m0 + C_Φ λ ≤ −δ_η + δ_η/2 (Lemma E.1 (b)). A covector
timelike for g_λ has one sign on g_λ's future causal cone, and the sign is that of dΦ0(Y) < 0 (Lemma E.1 (e); Y is
future timelike for g_λ too, λ being small): Φ0 decreases strictly along future causal curves near that portion,
which is Proposition 3.2's statement. (c) δ_η is continuous, nondecreasing in η and tends to 0 as η ↓ 0,
because μ is continuous, nondecreasing and μ(v_s) = μ0; η_λ is finite once 2 C_Φ λ ≤ δ at η = v_end − v_s, which
λ ≤ λ0 may be assumed to give. ∎

**Proposition E.4 (a domain of dependence at equality).** Put κ* := 2 μ(v_end)^(1/4)/μ0^(3/4), η* := 1/κ*, c :=
2 C_Φ, and for λ ≤ λ* := min(λ0, 1/c, δ_η*/(6 C_Φ))

    σ_λ(v) := c λ min((v − v_s)₊, η*),     D_T^λ := {v ≤ v_end + T, r ≥ r_q(v) + σ_λ(v)}.                         (2.1)

Then D_T^λ ⊂ D_T ⊂ {x_K ≤ 1}, D_T ∖ D_T^λ ⊂ {r_q(v) ≤ r < r_q(v) + c λ η*}, and no future causal curve of g_λ in Ω
enters D_T^λ through its inner boundary {Φ_σ = 0}, Φ_σ := r − r_q(v) − σ_λ(v): its portion on {v ≤ v_s} is the seed's
horizon (E.3 (a)), and on {v > v_s} it is spacelike for g_λ, uniformly on {v ≥ v_s + η*}.

*Proof.* B bounds |r_q' + σ_λ'| since σ_λ' ≤ c λ ≤ 1, so the constant C_Φ applies to dΦ_σ. On the pieces where σ_λ is
smooth, Lemma E.1 (a) with ρ = r_q + σ gives

    g0⁻¹(dΦ_σ, dΦ_σ) = −m0(v) + μ (1/r_q² − 1/ρ²) − 2σ' ≤ −m0(v) + κ* σ − 2σ',                                   (2.2)

since μ (1/r_q² − 1/ρ²) ≤ 2μσ/r_q³ and 2μ/r_q³ = 2 μ^(1/4)/μ0^(3/4) ≤ κ* at equality (E3). On v_s < v < v_s + η*:
σ' = c λ and κ* σ ≤ κ* c λ η* = c λ, so g_λ⁻¹(dΦ_σ, dΦ_σ) ≤ −m0 + c λ − 2 c λ + C_Φ λ = −m0 − C_Φ λ ≤ −C_Φ λ. On v >
v_s + η*: σ' = 0 and κ* σ = c λ, so g_λ⁻¹(dΦ_σ, dΦ_σ) ≤ −δ_η* + 3 C_Φ λ ≤ −δ_η*/2 (E5). On v ≤ v_s, σ = 0 and E.3 (a)
applies.

No entry. Let γ be a future causal curve of g_λ in Ω with Φ_σ < 0 at its start and Φ_σ ≥ 0 at some later parameter;
let s* be the first such parameter and p := γ(s*), so Φ_σ(p) = 0 and Φ_σ < 0 on γ before s*. Each smooth piece of
Φ_σ, extended a little past its v-interval, keeps a g_λ-timelike differential near p when v(p) > v_s (by continuity
of the margins above), with dΦ(X) < 0 for future causal X (the sign of dΦ(Y), Lemma E.1 (e)); near the corner v =
v_s + η*, Φ_σ is the larger of its two pieces, and near v = v_s, r = √μ0 it is the smaller of Φ0 and Φ1 := Φ0 − c λ
(v − v_s). If v(p) > v_s: the maximum of two functions strictly decreasing along γ near p is strictly decreasing, so
Φ_σ(γ(s)) > 0 for s < s* close to s*, a contradiction. If v(p) < v_s: γ cannot pass from {v > v_s} into {v < v_s},
since on {v ≤ v_s} (where g_λ = g0) v does not decrease (Lemma E.1 (d)); so γ lies in {v < v_s} on an interval before
s*, where Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there (E.3 (a)): r(p) < √μ0, a contradiction. If
v(p) = v_s: g_λ⁻¹(dΦ1, dΦ1) = −2 c λ < 0 at p (m0 = 0, σ = 0, g_λ = g0 there), so Φ1
decreases strictly along γ near p. Points of γ before p with v > v_s have Φ_σ = Φ1 > Φ1(p) = 0, impossible; so γ
approaches p within {v ≤ v_s}, where Φ_σ = Φ0 < 0, that is r < √μ0, and r does not increase there (E.3 (a)): r(p) <
√μ0, a contradiction. ∎

**Remark E.6 (why the layer is not decided).** On v_s < v < v_s + η_λ the margin m0 and the perturbation g_λ⁻¹ −
g0⁻¹ both vanish to every order at v = v_s (Lemma E.1 (c), Proposition E.2). Theorem 1 bounds the perturbation by C λ,
uniformly in v; deciding the sign needs a bound by a fraction of m0, pointwise in v near v_s. The expansion does not
give one: m0 is of the order of env² + ∫_(v_s)^v env² there (the term r_q μ'/(2μ) and √(μ/μ0) − 1), while the
profiles of g_app are not shown to have (Φ0♯, Φ0♯) components bounded by C (env² + ∫ env²) near v_s (the higher
profiles contain derivatives of env, which near v_s are not so bounded), and the remainder w is bounded only by
C λ^(K−3), uniformly in v. The sign of g_λ⁻¹(dΦ0, dΦ0) in the layer is a property of the exact solution near v_s that
Theorem 1's estimates do not reach. Proposition E.4 is the replacement: a domain O(λ)-close to D_T whose inner
boundary nothing crosses. A refinement, heuristic and recorded by verifier 163: W_TT is tangent to the spheres
(`ansatz5.py` A3), so the order-λ term reaches g⁻¹(dΦ0, dΦ0) only as λχ, of the order of λ A² env², a fraction of m0;
the obstruction starts at order λ², with profiles linear in the wave and its derivatives (the stage transports,
supplement sections 5.2–5.4), of both signs. Where such a component dominates m0 and the remainder, the sign would be
decided negatively (timelike patches), which strengthens the case for Proposition E.4 as the replacement.

## 3. The spheres' horizon at equality

**Proposition E.5.** Let K ≥ 6 and λ ≤ λ1 (Proposition 3.3). Let C_θ be the constant of Proposition 3.3's proof
(|θ⁺_λ − θ⁺_0| and |∂_r(θ⁺_λ − θ⁺_0)| ≤ C_θ λ on the columns), R_max the largest r on the columns, c_θ := 3/(R_max² +
μ(v_end)), and C := C_θ/c_θ (Proposition 3.3's C, not Theorem 1's).

(a) On every column (v and ω fixed, within D_T ∩ {τ ≥ τ0}), θ⁺_λ has at most one zero, positive above it and negative
below; every zero lies within C λ of √μ(v); the spheres with r ≥ √μ(v) + C λ are untrapped and those with r_q(v) ≤ r ≤
√μ(v) − C λ trapped. This strengthens the paper's own equality caveat (Proposition 3.3's last sentence: "the others on
the columns with μ(v) ≥ μ0 + δ1") to location and trapping on every column.

(b) On the columns with v ≤ v_s, θ⁺_λ = θ⁺_0 exactly: its one zero is r = √μ0, the column's lower end on the boundary,
and every sphere of the column above it is untrapped.

(c) On the columns that reach across √μ(v) + C λ and have √μ(v) − r_q(v) ≥ C' λ, for any C' > C_θ μ(v_end)/3, θ⁺_λ has
exactly one zero.

*Proof.* θ⁺_0 = (2r²/(r² + μ)) · 3(1 − μ/r²)/(2r) = 3(r² − μ)/(r(r² + μ)), so |θ⁺_0(r)| = 3|r − √μ| (r + √μ)/(r(r² +
μ)) ≥ c_θ |r − √μ| on the column ((r + √μ)/r ≥ 1). (a): θ⁺_λ ≥ c_θ (r − √μ) − C_θ λ > 0 for r > √μ + C λ, and ≤
−c_θ (√μ − r) + C_θ λ < 0 for r < √μ − C λ; near √μ, ∂_r θ⁺_0 = 3/μ at √μ, so ∂_r θ⁺_0 ≥ 3/(2μ(v_end)) on a fixed
neighbourhood of √μ, which contains [√μ − C λ, √μ + C λ] for λ small, and there ∂_r θ⁺_λ ≥ 3/(2μ(v_end)) − C_θ λ > 0:
at most one zero, and the signs as stated. Nothing in this uses r_q < √μ. (b) is Proposition E.2: on Ω ∩ {v ≤ v_s},
g_λ = g0. (c): with d := √μ − r_q ∈ [0, √μ], −θ⁺_0(r_q) − 3d/μ = 3d²(μ + √μ r_q + r_q²)/(μ r_q (μ + r_q²)) ≥ 0
exactly (verifier 163, symbolically), so θ⁺_λ(r_q) ≤ −3d/μ + C_θ λ ≤ −3C'λ/μ(v_end) + C_θ λ < 0; θ⁺_λ > 0 at √μ + C λ;
the intermediate value theorem and (a). ∎

So at equality, Theorem 1 item 6 holds in the form E.5: exactly one zero on the columns with v ≤ v_s (at the boundary
itself) and on those with √μ(v) − r_q(v) ≥ C' λ, a condition that fails only on a layer of v whose width tends to 0
with λ; at most one zero, within C λ of √μ(v), everywhere.

## 4. Findings, labels and sources

- EQ1. At equality the seed region is exact: g_λ = g0 on Ω ∩ {v ≤ v_s} (Proposition E.2, deduced: the supplement's
  Lemma 2.3 run on R, with the null face's flux nonnegative).

- EQ2. The boundary is null on the seed portion and spacelike on v ≥ v_s + η for λ ≤ λ_η; the undecided layer has width
  η_λ → 0 (Proposition E.3, deduced; eq5 E1, E2, E4).

- EQ3. A domain D_T^λ, within c λ η* of D_T and inside {x_K ≤ 1}, that no future causal curve enters from inside
  (Proposition E.4, deduced; eq5 E3, E5).

- EQ4. Theorem 1 item 6 at equality (Proposition E.5, deduced from Proposition 3.3's proof and E.2).

- EQ5. Not decided: the causal character of {x_K = 1} itself for g_λ in the layer (Remark E.6).

- EQ6. Verifier 163 (D347): no blocking or major gap. MINOR-1, the identification of the family built with v_start :=
  v_s with the paper's (the construction uses v_start only through supp env); MINOR-2, E.2 needs the data as a metric
  with its τ-derivative, which the proof of Theorem D gives, not only Theorem 1 item 2's Cauchy data; MINOR-3, "within
  cλ" corrected to cλη* (η* exceeds 1 once μ0 is large); MINOR-4, E.4 is the inner-boundary property, not a full
  domain-of-dependence statement (the face {v = v_end + T} is not treated). Nits: E.5 (c) by an exact inequality (E6);
  E.5 (a) proved with an explicit c_θ and said to strengthen the paper's caveat; E.1 (e) stated; Lemma 9.2 of the
  supplement cross-referenced; eq5's E3 given a control, E4's sample count and its "attained" test corrected;
  "nondecreasing"; η_λ finite for λ small; Y future timelike for g_λ put into λ0; E.5 (c)'s reach-across condition in
  the summary; X^v ≥ 0. All seated.

Labels: computed (eq5 E1–E6; random sampling in E4, seed fixed), deduced (E.1–E.5). Sources: the paper, sections 2.2–2.5,
Theorem 1, Propositions 3.2–3.3; the supplement `N1STAR-PROOF.md` Lemma 1.1 and Lemma 2.3. No reading outside the
record.
