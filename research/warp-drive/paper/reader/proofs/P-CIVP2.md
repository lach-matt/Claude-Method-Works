### Developments of cone data without smallness {#sec:civp-large}

This section develops the cone data of [[prop:loc-cones]] without smallness; for data near the background's the
development is that of [[thm:loc-cone-development]]. For cone data of any size that equal the background's outside a
band away from the axes, with or without dust, a development in the gauge [[eq:loc-double-null]] exists on a
neighbourhood {min(u, v) ≤ δ} of the two cones, which contains {uv ≤ δ²}; it equals the background outside a slightly
wider band, and it is unique in the gauge among solutions that equal the background near the axes ([[thm:civp-large]]).
The number δ depends on the data. The route is that of Cabet, Chruściel and Tagne Wafo [CCTW16]. Off the axes,
[[prop:reduction]] turns the class system into a three-dimensional one for the conformal orbit metric h, two waves ψ and
ω and the two densities. In three dimensions the curvature is determined by the Ricci tensor, and the reduction
expresses the Ricci tensor through the densities and the first derivatives of ψ and ω. So in a double-null frame of h
the connection coefficients obey transport equations along the two null directions with no angular derivative of an
unknown on the right, and the waves become first-order systems of the same kind ([[lem:civp-large-frame]]). The
resulting evolution system has the doubly-null form of [CCTW16, (2.7)–(2.8)] ([[prop:civp-large-system]]), and once it
is localised in angle their theorem ([[thm:std-cctw-existence]], [[thm:std-cctw-strips]]) gives a solution on two strips
along the cones. That this solution solves the Einstein equations is shown by the device of the proof of [CCTW16,
Theorem 5.3, pp. 55–56], which builds the development up in the time u + v; where that proof solves Cauchy and mixed
problems, the local developments here are those near corner spheres ([[prop:civp-large-corner]]), each of which
coincides with the strip solution by an energy estimate ([[lem:civp-large-energy]]).

*Notation.* The background g0, the cones 𝒞_out = {u = 0} and 𝒞_in = {v = 0}, the corner sphere S = 𝒞_out ∩ 𝒞_in and the
gauge [[eq:loc-double-null]] are those of [[sec:loc-cones]], and R is the area radius of g0. We fix u_1, v_1 > 0 such
that the background is defined and smooth on [0, u_1′] × [0, v_1′] for some u_1′ > u_1 and v_1′ > v_1, and put Q1 := [0,
u_1] × [0, v_1]; every u_1 ≤ 7.2 and every v_1 > 0 will do ([[lem:civp-large-rectangle]] (a)). On Q1 × S³, in the gauge
[[eq:loc-double-null]], b = 0, γ_ϑ = R², A_c = ln(R cos ϑ) and A_s = ln(R sin ϑ), Ω is a function of (u, v), and
Ric(g0) = q̊_in dv ⊗ dv + q̊_out du ⊗ du ([[eq:two-dust-limit]]). We extend Ω and R smoothly across the two cones, as in
[[lem:civp-large-rectangle]] (a), to an open set 𝒪 of the (u, v)-plane that contains Q1 and on which Ω, R > 0; so g0 =
−4Ω² du dv + R² dΩ₃² is given on 𝒪 × S³ and solves [[eq:two-dust-limit]] at the points of 𝒪 with u, v ≥ 0. We fix a band
0 < ϑ_a < ϑ_b < π/2 and put

    η0 := (1/3) min(ϑ_a, π/2 − ϑ_b),      J0 := [ϑ_a − 2η0, ϑ_b + 2η0] ⊂ [η0, π/2 − η0].  {#eq:civp-large-band}

A set D ⊂ Q1 is a *past set* if [0, u] × [0, v] ⊂ D for every (u, v) ∈ D. Class solutions in the gauge on D × S³, D ⊂
Q1, are those of [[sec:loc-cone-setting]], with the corner at S and g0 as the background; their metrics equal g0 near
the axes, and so extend smoothly to them.

**Definition {#def:civp-large-data}** (Cone data on Q1.) *Cone data on Q1* consist of smooth functions Ω > 0, γ_ϑ > 0,
b, A_c, A_s and q_in ≥ 0 of (v, ϑ) ∈ [0, v_1] × (0, π/2) on 𝒞_out, and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ)
∈ [0, u_1] × (0, π/2) on 𝒞_in, with b = 0 on 𝒞_in, such that:

(i) the two sets of functions agree on S;

(ii) for the metric [[eq:loc-double-null]] that they define, Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on 𝒞_out, and
Ric(∂_u, ∂_u) = q_out on 𝒞_in (each side involves only the functions given on that cone: on 𝒞_out by
[[lem:loc-cone-equations]], on 𝒞_in by (F1′) of [[lem:civp-large-frame]] and [[prop:reduction]], since b vanishes
there);

(iii) they equal the background's outside compact sets K_out ⊂ [0, v_1] × (ϑ_a, ϑ_b) and K_in ⊂ [0, u_1] × (ϑ_a, ϑ_b).

[[prop:loc-cones]] and [[lem:loc-cone-in]] produce cone data on Q1 from free data whenever the conformal factors e^ϕ
that they determine stay positive, and no smallness is needed for that ([[lem:civp-large-free]]).

**Lemma {#lem:civp-large-free}** (Cone data on Q1 from free data.) Let free data (ℓ_1, ℓ_2, ℓ_3) and q_in ≥ 0 on 𝒞_out ∩
{v ≤ v_1} be given as in [[prop:loc-cones]], and (ℓ_1, ℓ_2, ℓ_3) and q_out ≥ 0 on 𝒞_in ∩ {u ≤ u_1} as in
[[lem:loc-cone-in]], smooth, agreeing on S, and equal to the background's outside compact subsets of [0, v_1] × (ϑ_a,
ϑ_b) and of [0, u_1] × (ϑ_a, ϑ_b). On a generator of either cone let y := e^ϕ be the factor that the constraint
determines, ′ the derivative along the generator, L := v_1 on 𝒞_out and L := u_1 on 𝒞_in, ρ := Ω^(−2) and p := (1/3)(Σ_i
(ℓ_i′)² + q), with q := q_in on 𝒞_out and q := q_out on 𝒞_in, and let ẙ := e^(ϕ̊) and p̊ be the background's.

(a) If y > 0 on [0, L] on every generator of both cones, then the functions so determined, Ω, γ_ϑ = e^(2ϕ + 2ℓ_1), b,
A_c = ϕ + ℓ_2, A_s = ϕ + ℓ_3 and q_in on 𝒞_out, and Ω, γ_ϑ, A_c, A_s and q_out on 𝒞_in, with b = 0 there, are cone data
on Q1.

(b) On a generator put

    I := ∫_0^L ρ(s) (p − p̊)_+(s) ẙ(s)² ∫_s^L ρ(t)⁻¹ ẙ(t)^(−2) dt ds,      (p − p̊)_+ := max(p − p̊, 0).

If I < 1, then y ≥ (1 − I) ẙ > 0 on [0, L]. In particular y ≥ ẙ on a generator on which p ≤ p̊.

*Proof.* (b) By the first line of [[eq:loc-cone]] and by [[eq:loc-cone-in]], as in the proof of [[prop:loc-cones]], y
solves y″ − 2(ln Ω)′y′ + py = 0, that is (ρy′)′ + ρpy = 0, since ρ′ = −2(ln Ω)′ρ; the background's ẙ solves (ρẙ′)′ +
ρp̊ẙ = 0, Ω being the background's; and y and ẙ have the same value and the same derivative at the corner. Put p̃ :=
p̊ + (p − p̊)_+, so that p ≤ p̃, let z solve (ρz′)′ + ρp̃z = 0 with the same initial values, and put w := z/ẙ. Then
ρẙ²w′ = ρ(z′ẙ − zẙ′), so (ρẙ²w′)′ = −ρ(p − p̊)_+ẙ²w, with w(0) = 1 and w′(0) = 0. On an interval [0, t_0] on which w ≥ 0
this gives ρẙ²w′ ≤ 0, so w ≤ 1, and, exchanging the order of integration, for t ≤ t_0

    w(t) = 1 − ∫_0^t (ρẙ²)⁻¹(τ) ∫_0^τ (ρ(p − p̊)_+ẙ²w)(s) ds dτ
         ≥ 1 − ∫_0^t ρ(s) (p − p̊)_+(s) ẙ(s)² ∫_s^t (ρẙ²)⁻¹(τ) dτ ds ≥ 1 − I.

If w vanished somewhere on [0, L], this bound at its first zero would contradict I < 1; so w ≥ 1 − I on [0, L]. Next, W
:= ρ(y′z − yz′) vanishes at 0 and has W′ = (ρy′)′z − y(ρz′)′ = ρ(p̃ − p)yz. On an interval [0, t_1) on which y > 0,
therefore, W ≥ 0, (y/z)′ = W/(ρz²) ≥ 0 and y ≥ z. If y had a first zero t_1 ∈ (0, L], continuity would give y(t_1) ≥
z(t_1) > 0, which is absurd. So y ≥ z = wẙ ≥ (1 − I)ẙ on [0, L]. If p ≤ p̊, then I = 0.

(a) By [[prop:loc-cones]] and [[lem:loc-cone-in]], the constraints determine ϕ and b on 𝒞_out, and ϕ on 𝒞_in, on every
generator on which y > 0, as solutions of linear ordinary differential equations along the generators whose coefficients
and initial values depend smoothly on the angle; so the functions are smooth on [0, v_1] × (0, π/2) and on [0, u_1] ×
(0, π/2), and Ω, γ_ϑ > 0. Condition (i) of [[def:civp-large-data]] holds: on S the free data agree, ϕ and Ω are the
background's on both cones, and b vanishes on both, being the background's at v = 0 on 𝒞_out. Condition (ii) holds by
construction, since T = q_in dv ⊗ dv + q_out du ⊗ du gives T(∂_v, ∂_v) = q_in, T(∂_v, ∂_ϑ) = 0 and T(∂_u, ∂_u) = q_out.
For (iii) let [ϑ_a″, ϑ_b″] ⊂ (ϑ_a, ϑ_b) contain in its interior the angles of the two compact sets. [[prop:loc-cones]]
and [[lem:loc-cone-in]], applied with the band (ϑ_a″, ϑ_b″), give the background's functions at every ϑ ∉ [ϑ_a″, ϑ_b″];
so K_out := [0, v_1] × [ϑ_a″, ϑ_b″] and K_in := [0, u_1] × [ϑ_a″, ϑ_b″] serve. ∎

**Lemma {#lem:civp-large-rectangle}** (The background on a rectangle of the two cones.) Use the coordinates (u, v) of
[[sec:loc-setting]], let v_1 > 0, and let V1 in [[prop:two-dust-background]] be chosen so large that V1′ > v_1 + 1, as
in the proof of [[lem:loc-cone-strips]] (a).

(a) The rectangle [0, 7.2] × [0, v_1] lies in the set G of [[prop:two-dust-background]] (d), and R_v > 0 and R ≥
1.519357 on it. There is δ ∈ (0, 1/2) such that the background is defined and smooth on [0, 7.2 + 2δ] × [0, v_1 + 2δ],
and Ω and R extend to smooth positive functions on [−δ, 7.2 + δ] × [−δ, v_1 + δ].

(b) Let free data be given as in [[lem:civp-large-free]], with u_1 ≤ 7.2. On 𝒞_out the number I of
[[lem:civp-large-free]] (b) is at most ∫_0^(v_1) (v_1 − s) (p − p̊)_+(s) ds, and on 𝒞_in it is at most R(7.2, 0)^(−2)
∫_0^(u_1) R(s, 0)² (u_1 − s) (p − p̊)_+(s) ds, with R(7.2, 0)² ≥ 2.308; and p − p̊ = (1/3)(Σ_i (ℓ_i′)² + q − q̊), q̊ the
background's density. So e^ϕ stays positive on every generator of a cone in each of the following cases, and when it
does on both cones the free data give cone data on Q1 ([[lem:civp-large-free]] (a)), the conformal data (ℓ_1, ℓ_2, ℓ_3)
being the background's and c a smooth function of ϑ with compact support in (ϑ_a, ϑ_b): a density q − q̊ ≥ 0 added on
𝒞_out with supremum A on an interval of v of length l, if v_1 A l < 3, or on 𝒞_in with supremum A on an interval of u of
length l, if 26 A l ≤ 1; the density of the shell multiplied by 1 + c with −1 ≤ c ≤ 76, if v_1 = 4.5; and the density of
the packet multiplied by 1 + c with −1 ≤ c ≤ 4.5, if u_1 = 7.2. In particular there are such data with densities of
every amplitude.

*Proof.* (a) Let σ be the function of [[eq:bg-field]], e^(2σ) = 2Ω². By [[lem:two-dust-reparametrisation]] (b),
[[prop:two-dust-background]] holds in these coordinates (proof of [[lem:loc-cone-strips]] (a)): G is closed in Q = [0,
∞) × [0, V1′], its boundary in Q lies in {R = a}, a = 0.70, the background is smooth on G, and μ ≥ μ0 > 0 on G. G is a
past set, 𝒟 being one: for p ∈ G and p′ ∈ J⁻(p) = [0, u_p] × [0, v_p], p′ ∈ 𝒟 and J⁻(p′) ⊂ J⁻(p). By
[[eq:two-dust-evolution]] and [[eq:two-dust-mass]], which hold in these coordinates, σ_uv = 3(e^(2σ) + 2R_uR_v)/(2R²) =
(3/2)e^(2σ)μ/R⁴ > 0 on G, and σ = −(1/2) ln 2 on both cones; so σ(u, v) = −(1/2) ln 2 + ∫_0^u ∫_0^v σ_uv ≥ −(1/2) ln 2
on every rectangle J⁻(p), p ∈ G, that is 1/2 ≤ e^(2σ) and e^(−2σ) ≤ 2. Put λ := e^(−2σ)R_v. Then λ_v = −𝒜e^(−2σ)/(3R²)
([[lem:bg-identities]]) and λ(u, 0) = 2R_v(u, 0) = ℓ_v(u) ([[lem:bg-reduction]] (a)).

*On 𝒞_in.* There R″ = −ℬ/(3R²) ≤ 0, and R′ = −0.47 on [0, u1], u1 = 5.7 ([[lem:bg-reduction]] (a)), so R(·, 0)
decreases, and R(u, 0) ≥ R(u2, 0) ≥ 1.519357 for u ≤ u2 = 7.2 ([[prop:bg-nprime]] (i)). μ(·, 0) is 3/2 on [0, u1]
([[lem:bg-reduction]] (b)) and
at least μ3 > 0 on [u1, u2] ([[prop:bg-nprime]] (iii)), so ℓ_v′ = −μ/R³ < 0 on [0, 7.2] ([[eq:bg-nprime]]) and ℓ_v(u) ≥
ℓ_v(u2) ≥ 0.529533 for u ≤ 7.2 ([[prop:bg-nprime]] (iii)).

*At a point of G.* Let p ∈ G with u_p ≤ 7.2 and v_p ≤ v_1, and (u, v) ∈ J⁻(p). For v ≤ 3, 𝒜 = 0, so λ(u, v) = ℓ_v(u) ≥
0.529533 and R_v = e^(2σ)λ ≥ 0.264766. Hence R(u, v) ≥ R(u, 0) ≥ 1.519357 for v ≤ min(v_p, 3), and R(u, 3) ≥ 1.519357 +
3 × 0.264766 ≥ 2.3136 if v_p ≥ 3. If v_p > 3, let w be the supremum of the v ∈ [3, v_p] such that λ(u, ·) > 0 on [3, v];
λ(u, 3) > 0, so w > 3. On [3, w], R(u, ·) is nondecreasing, so R ≥ 2.3136, and since 𝒜 ≥ 0 vanishes outside [3, 4.5] and
∫_3^4.5 𝒜 = 2.7 K ≤ 3.25878, K := ∫_(−1)^1 β ≤ 1.2069549 ([[lem:margins-bump-table]] (a)),

    λ(u, v) = ℓ_v(u) − (1/3) ∫_3^v 𝒜 e^(−2σ)/R² ≥ 0.529533 − (2 × 3.25878)/(3 × 2.3136²) ≥ 0.1236.

By continuity w = v_p. So R_v = e^(2σ)λ > 0 on J⁻(p), and R ≥ R(u, 0) ≥ 1.519357 > a there; in particular R(p) > a, p is
not on the boundary of G in Q, and G contains a neighbourhood of p in Q.

*Conclusion.* So G ∩ Q_*, Q_* := [0, 7.2] × [0, v_1], is open in Q_*; it is closed in Q_*, G being closed in Q; and it
contains the corner, which lies in G, R being 5 there. Q_* is connected, so Q_* ⊂ G, and by the previous paragraph R_v >
0 and R ≥ 1.519357 on Q_*. The points of G with R > a are interior points of G in Q, so they form a set open in Q that
contains the compact Q_*, hence [0, 7.2 + 2δ] × [0, v_1 + 2δ] for some δ ∈ (0, 1/2); there the background is smooth,
solves [[eq:two-dust-limit]] and has R > a. [[lem:loc-cone-borel]], with r := 0, applied as in the proof of
[[lem:loc-cone-strips]] (b) to the derivatives of σ and of R on {0} × [0, v_1 + 2δ] and on [0, 7.2 + 2δ] × {0}, which do
not depend on ϑ, extends σ and R to smooth functions on (−∞, 7.2 + 2δ] × (−∞, v_1 + 2δ]; after decreasing δ, R > 0 on
[−δ, 7.2 + δ] × [−δ, v_1 + δ] by continuity, and Ω = e^σ/√2 > 0.

(b) On the cones e^(2σ) = 1/2, so Ω² = 1/4 and ρ = 4; and ẙ = R (sin ϑ cos ϑ)^(1/3), since ϕ̊ = (ϰ̊_1 + ϰ̊_2 + ϰ̊_3)/3
with ϰ̊_1 = ln R, ϰ̊_2 = ln(R cos ϑ), ϰ̊_3 = ln(R sin ϑ). So ρ and the angular factor cancel in I, and I = ∫_0^L (p −
p̊)_+(s) ∫_s^L (R(s)/R(t))² dt ds, R taken on the cone. On 𝒞_out, R increases and R ≥ 5 (proof of
[[lem:loc-cone-strips]] (c)), so the inner integral is at most L − s. On 𝒞_in, R decreases, so for s ≤ t ≤ u_1 ≤ 7.2 it
is at least R(7.2, 0) ≥ 1.519357, and the inner integral is at most (u_1 − s)R(s, 0)²/R(7.2, 0)². The background's
ℓ̊_i = ϰ̊_i − ϕ̊ depend on ϑ only, so ℓ̊_i′ = 0 and p − p̊ = (1/3)(Σ_i (ℓ_i′)² + q − q̊). With the conformal data the
background's, (p − p̊)_+ = (q − q̊)_+/3. For an added density on 𝒞_out, I ≤ v_1 · A l/3 < 1. On 𝒞_in, R(s, 0) ≤ 5, so I
≤ (25/2.308) · 7.2 · A l/3 ≤ 25.997 A l < 1. For the shell, q̊_in = 𝒜/R³ ≤ 𝒜/125 on 𝒞_out; at an angle with c ≤ 0, p ≤
p̊, and at one with 0 < c ≤ 76, I ≤ (1.5/3) · 76 · ∫_3^4.5 𝒜/125 ≤ 0.5 × 76 × 3.25878/125 < 0.991, since (q − q̊)_+ = c
q̊_in vanishes outside [3, 4.5] and v_1 − s ≤ 1.5 there. For the packet, q̊_out = ℬ/R³ with ℬ supported in [u1, u2] and
∫ ℬ = 1.275 K ≤ 1.53887; at an angle with 0 < c ≤ 4.5, I ≤ (4.5/3) · 1.5 · ∫ ℬ/(R(s, 0) R(7.2, 0)²) ds ≤ 2.25 ×
1.53887/(1.519357 × 2.308) < 0.988, and where c ≤ 0, p ≤ p̊. In each case [[lem:civp-large-free]] (b) gives e^ϕ > 0. A
density added on 𝒞_out with supremum A on an interval of length l < 3/(v_1 A) has amplitude A, for every A > 0. ∎

No step of the proof of [[thm:civp-large]] uses the two lemmas, the theorem taking cone data on Q1 as given. Data with
q_in = q_out = 0 are vacuum data.

*The small-data theorem.* [[thm:loc-cone-development]] is used only for comparison, in [[rem:civp-large-domain]] and
[[rem:civp-large-beyond]]. Its data are cone data on Q1 in the sense of [[def:civp-large-data]], with Ω the background's
on both cones, obtained by [[prop:loc-cones]] and [[lem:loc-cone-in]] from free data within ε_0 of the background's in
C^(6k+21) that equal the background's outside compact subsets of [0, v_1) × (ϑ_a, ϑ_b) and [0, u_1) × (ϑ_a, ϑ_b), with
u_1, v_1 as in that theorem; it gives a class solution in the gauge [[eq:loc-double-null]] on the explicit past set {uv
≤ δ_*²} ∩ Q1, times S³, that induces the data and equals (g0, q̊_in, q̊_out) where ϑ ≤ ϑ_a − 3η0/4 or ϑ ≥ ϑ_b + 3η0/4,
with an estimate of the solution, and its uniqueness in the gauge is stated near the background only.

#### The reduced system in a double-null frame {#sec:civp-large-frame}

Off the axes write a metric of the form [[eq:loc-double-null]] as g = g3 + e^(2A_c) dφ1² + e^(2A_s) dφ2², with
g3 := −2Ω² (du ⊗ dv + dv ⊗ du) + γ_ϑ (dϑ − b du)². With ψ := A_c + A_s, ω := (A_s − A_c)/2 and h := e^(2ψ) g3 as in
[[prop:reduction]],

    h = −2e^(2α) (du ⊗ dv + dv ⊗ du) + e^(2β) (dϑ − b du)²,      α := ψ + ln Ω,      β := ψ + (1/2) ln γ_ϑ.
                                                                                                 {#eq:civp-large-h}

We use the frame

    e3 := e^(−α) (∂_u + b ∂_ϑ),      e4 := e^(−α) ∂_v,      e1 := e^(−β) ∂_ϑ,

for which h(e3, e4) = −2, h(e1, e1) = 1 and all other products vanish: h(e3, e3) = e^(−2α)(e^(2β) b² − 2b e^(2β) b +
b² e^(2β)) = 0, h(e1, e3) = e^(−α−β)(−e^(2β) b + b e^(2β)) = 0, and h(e4, e4) = h(e1, e4) = 0 because h_vv = h_vϑ = 0.
Its *connection coefficients* are

    χ := h(∇_1 e4, e1),   χ̲ := h(∇_1 e3, e1),   η := (1/2) h(e1, ∇_3 e4),   η̲ := (1/2) h(e1, ∇_4 e3),
    ϖ := (1/4) h(e3, ∇_4 e4),   ϖ̲ := (1/4) h(e4, ∇_3 e3),   ζ := (1/2) h(∇_1 e4, e3),

with ∇ the connection of h and ∇_i := ∇_(e_i). These are not the quantities of the same names in [[sec:loc-cone-proof]].
We write Ric_ij := Ric[h](e_i, e_j) and, for a function F, e_iF for its derivative. The *exchange* is the map e3 ↔ e4, χ
↔ χ̲, η ↔ η̲, ϖ ↔ ϖ̲, ζ ↔ −ζ; it maps each definition above to another one.

**Lemma {#lem:civp-large-frame}** (The double-null frame of h.) (a) The coefficients are

    χ = e4β,   χ̲ = e3β + e^(−α) ∂_ϑb,   ϖ = −(1/2) e4α,   ϖ̲ = −(1/2) e3α,
    ζ = −(1/4) e^(β−2α) ∂_vb,   η = ζ + e1α,   η̲ = −ζ + e1α.  {#eq:civp-large-coefficients}

(b) The following hold for every metric of the form [[eq:civp-large-h]], together with their images (F1′)–(F5′) under
the exchange:

    (F1)  e4χ = −χ² − 2ϖχ − Ric_44,
    (F2)  e4η = −Ric_41 − χ(η − η̲),
    (F3)  e3ϖ = 2ϖϖ̲ + (1/2)η̲² − ηη̲ + (1/4)(Ric_34 + Ric_11),
    (F4)  e3χ = 2 e1η + 2η² + 2ϖ̲χ − χχ̲ + Ric_11,
    (F5)  e3η = Ric_31 − 2χ̲η − 4 e1ϖ̲ − 2ϖ̲(η + η̲).  {#eq:civp-large-null}

(c) For every function F,

    □_h F = −e3e4F + e1e1F + (2ϖ̲ − (1/2)χ̲) e4F − (1/2)χ e3F + 2η e1F,                              {#eq:civp-large-box}

and the image of the right side under the exchange is also □_h F. For every function q,

    div_h(q h⁻¹dv) = −(1/2) e^(−α) (e3q + χ̲ q),      div_h(q h⁻¹du) = −(1/2) e^(−α) (e4q + χ q).  {#eq:civp-large-dust}

(d) Let g be a metric of the form [[eq:loc-double-null]] off the axes and q a function of (u, v, ϑ). Then
div_g(q g⁻¹du) = e^(2ψ) div_h(q h⁻¹du) and div_g(q g⁻¹dv) = e^(2ψ) div_h(q h⁻¹dv).

In (F1)–(F5) only (F4), (F5) and their images contain an e1-derivative of a connection coefficient; (F1)–(F3) and
(F1′)–(F3′) contain none, and the only curvature in them is the Ricci tensor of h.

*Proof.* *The connection table.* Since u is a null coordinate, h⁻¹du = −(1/2) e^(−α) e4 is the gradient of a solution
of h⁻¹(du, du) = 0, so ∇_(h⁻¹du) h⁻¹du = (1/2) ∇(h⁻¹(du, du)) = 0, and ∇_4 e4 is a multiple of e4; likewise h⁻¹dv =
−(1/2) e^(−α) e3, and ∇_3 e3 is a multiple of e3. (The formulas for h⁻¹du and h⁻¹dv follow from du(e3) = dv(e4) =
e^(−α), du(e4) = dv(e3) = du(e1) = dv(e1) = 0 and h(e3, e4) = −2.) A vector V is −(1/2)h(V, e4) e3 − (1/2)h(V, e3) e4 +
h(V, e1) e1. With the definitions, h(∇_X e_i, e_j) = −h(e_i, ∇_X e_j), h(∇_X e3, e3) = h(∇_X e4, e4) = h(∇_X e1, e1) =
0, and the two geodesic facts, this gives

    ∇_4e4 = −2ϖ e4,   ∇_4e3 = 2ϖ e3 + 2η̲ e1,   ∇_4e1 = η̲ e4,   ∇_3e3 = −2ϖ̲ e3,   ∇_3e4 = 2ϖ̲ e4 + 2η e1,
    ∇_3e1 = η e3,   ∇_1e4 = χ e1 − ζ e4,   ∇_1e3 = χ̲ e1 + ζ e3,   ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4.
                                                                                                   {#eq:civp-large-table}

For instance h(∇_4e3, e4) = −h(e3, ∇_4e4) = −4ϖ, h(∇_4e3, e3) = 0 and h(∇_4e3, e1) = 2η̲, so ∇_4e3 = 2ϖ e3 + 2η̲ e1;
and h(∇_1e1, e4) = −χ, h(∇_1e1, e3) = −χ̲, h(∇_1e1, e1) = 0, so ∇_1e1 = (1/2)χ e3 + (1/2)χ̲ e4. The table is invariant
under the exchange.

(a) Since ∇ has no torsion, the table gives

    [e4, e3] = 2ϖ e3 − 2ϖ̲ e4 + 2(η̲ − η) e1,   [e4, e1] = (η̲ + ζ) e4 − χ e1,   [e3, e1] = (η − ζ) e3 − χ̲ e1.

From the coordinate expressions, with ∂_v and ∂_u + b∂_ϑ and ∂_ϑ commuting up to [∂_v, ∂_u + b∂_ϑ] = (∂_vb)∂_ϑ and
[∂_u + b∂_ϑ, ∂_ϑ] = −(∂_ϑb)∂_ϑ,

    [e4, e3] = −(e4α) e3 + (e3α) e4 + e^(β−2α)(∂_vb) e1,   [e4, e1] = (e1α) e4 − (e4β) e1,
    [e3, e1] = (e1α) e3 − (e3β + e^(−α)∂_ϑb) e1.

Comparing coefficients gives ϖ, ϖ̲, χ, χ̲, η̲ + ζ = e1α = η − ζ, and 2(η̲ − η) = e^(β−2α) ∂_vb; since η − η̲ = 2ζ by
the previous relation, ζ = −(1/4) e^(β−2α) ∂_vb. This is [[eq:civp-large-coefficients]]. We use below

    [e4, e3] = 2ϖ e3 − 2ϖ̲ e4 − 4ζ e1,   [e4, e1] = (e1α) e4 − χ e1,   [e3, e1] = (e1α) e3 − χ̲ e1,   e1α = (η + η̲)/2.

*The Ricci tensor in the frame.* With the dual frame, Ric(X, Y) = h(R(e1, X)Y, e1) − (1/2)h(R(e3, X)Y, e4) −
(1/2)h(R(e4, X)Y, e3), where R(X, Y) = ∇_X∇_Y − ∇_Y∇_X − ∇_[X,Y]. By the antisymmetries of h(R(X, Y)Z, W) in (X, Y)
and in (Z, W), the pair symmetry and the first Bianchi identity, this gives

    Ric_44 = h(R(e1, e4)e4, e1),   Ric_41 = −(1/2) h(R(e4, e3)e4, e1),   Ric_11 = h(R(e3, e1)e4, e1),
    Ric_34 + Ric_11 = (1/2) K,   K := h(R(e3, e4)e4, e3).

Indeed Ric_11 = −(1/2)(h(R(e3, e1)e1, e4) + h(R(e4, e1)e1, e3)), and by the pair symmetry and the Bianchi identity both
terms equal L := h(R(e1, e3)e4, e1), so Ric_11 = −L = h(R(e3, e1)e4, e1); and Ric_34 = h(R(e1, e3)e4, e1) −
(1/2)h(R(e4, e3)e4, e3) = L + (1/2)K. For Ric_41 the terms h(R(e1, e4)e1, e1) and h(R(e4, e4)e1, e3) vanish and
h(R(e3, e4)e1, e4) = −h(R(e3, e4)e4, e1) = h(R(e4, e3)e4, e1).

(F1) By the table, ∇_4∇_1e4 = (e4χ) e1 + χη̲ e4 − (e4ζ) e4 + 2ζϖ e4, ∇_1∇_4e4 = −2(e1ϖ) e4 − 2ϖ(χ e1 − ζ e4) and
∇_[e4,e1] e4 = −2ϖ(η̲ + ζ) e4 − χ(χ e1 − ζ e4). The e1-component of R(e4, e1)e4 is therefore e4χ + 2ϖχ + χ², and
Ric_44 = −h(R(e4, e1)e4, e1).

(F2) 2e4η = e4 h(∇_3e4, e1) = h(∇_4∇_3e4, e1) + h(∇_3e4, ∇_4e1), and the last term vanishes since ∇_4e1 = η̲ e4 and
h(e4, e1) = h(e4, e4) = 0. Here ∇_4∇_3e4 = R(e4, e3)e4 + ∇_3∇_4e4 + ∇_[e4,e3] e4; the e1-component of ∇_3∇_4e4 =
∇_3(−2ϖ e4) is −4ϖη, and that of ∇_[e4,e3] e4 = 2ϖ∇_3e4 − 2ϖ̲∇_4e4 − 4ζ∇_1e4 is 4ϖη − 4ζχ. So
2e4η = h(R(e4, e3)e4, e1) − 4ζχ = −2Ric_41 − 2χ(η − η̲).

(F3) 4e3ϖ = e3 h(e3, ∇_4e4) = h(∇_3e3, ∇_4e4) + h(e3, ∇_3∇_4e4), and h(∇_3e3, ∇_4e4) = 4ϖϖ̲ h(e3, e4) = −8ϖϖ̲. Write
∇_3∇_4e4 = R(e3, e4)e4 + ∇_4∇_3e4 + ∇_[e3,e4] e4. Then h(e3, R(e3, e4)e4) = K; h(e3, ∇_4∇_3e4) = e4 h(e3, ∇_3e4) −
h(∇_4e3, ∇_3e4) = −4e4ϖ̲ + 8ϖϖ̲ − 4ηη̲, since h(e3, ∇_3e4) = −h(∇_3e3, e4) = −4ϖ̲; and with [e3, e4] = −2ϖ e3 + 2ϖ̲
e4 + 4ζ e1, the e4-coefficient of ∇_[e3,e4] e4 = −2ϖ∇_3e4 + 2ϖ̲∇_4e4 + 4ζ∇_1e4 is −8ϖϖ̲ − 4ζ², so that h(e3, ∇_[e3,e4]
e4) = 16ϖϖ̲ + 8ζ². Hence

    e3ϖ + e4ϖ̲ = (1/4) K + 4ϖϖ̲ + 2ζ² − ηη̲.

On the other hand ϖ = −(1/2)e4α and ϖ̲ = −(1/2)e3α give e3ϖ − e4ϖ̲ = −(1/2)[e3, e4]α = −(1/2)(4ϖϖ̲ − 4ϖ̲ϖ + 4ζ e1α) =
−2ζ e1α = −(1/2)(η² − η̲²). Half the sum of the two relations, with ζ = (η − η̲)/2 and K = 2(Ric_34 + Ric_11), is (F3).

(F4) e3χ = h(∇_3∇_1e4, e1) + h(∇_1e4, ∇_3e1) = h(∇_3∇_1e4, e1) + 2ζη, since h(χ e1 − ζ e4, η e3) = 2ζη. Here
∇_3∇_1e4 = R(e3, e1)e4 + ∇_1∇_3e4 + ∇_[e3,e1] e4. The e1-component of ∇_1∇_3e4 = ∇_1(2ϖ̲ e4 + 2η e1) is 2ϖ̲χ + 2e1η,
and that of ∇_[e3,e1] e4 = (η − ζ)∇_3e4 − χ̲∇_1e4 is 2η(η − ζ) − χχ̲. With h(R(e3, e1)e4, e1) = Ric_11 this is (F4).

(F5) By (a), e3η + e3η̲ = 2e3e1α = 2e1e3α + 2[e3, e1]α = −4e1ϖ̲ + 2(e1α)(e3α) − 2χ̲ e1α = −4e1ϖ̲ − (2ϖ̲ + χ̲)(η + η̲).
Subtracting (F2′), e3η̲ = −Ric_31 − χ̲(η̲ − η), gives (F5).

The images under the exchange hold by the same derivations with the roles of e3 and e4 exchanged, since the table and
the formula for Ric are invariant; for (F3′) and (F5′) one uses ϖ = −(1/2)e4α, ϖ̲ = −(1/2)e3α and e1α = (η + η̲)/2,
which are also invariant.

(c) □_h F = h^(ab)∇_a∇_bF = −(1/2)(∇²F(e3, e4) + ∇²F(e4, e3)) + ∇²F(e1, e1), with ∇²F(X, Y) = X(YF) − (∇_XY)F. By the
table, ∇²F(e3, e4) = e3e4F − 2ϖ̲ e4F − 2η e1F, ∇²F(e4, e3) = e4e3F − 2ϖ e3F − 2η̲ e1F and ∇²F(e1, e1) = e1e1F −
(1/2)χ e3F − (1/2)χ̲ e4F. Replacing e4e3F by e3e4F + [e4, e3]F = e3e4F + 2ϖ e3F − 2ϖ̲ e4F + 2(η̲ − η) e1F gives
[[eq:civp-large-box]]; replacing instead e3e4F by e4e3F − [e4, e3]F gives its image. For the densities, h⁻¹dv =
−(1/2)e^(−α) e3, so div_h(q h⁻¹dv) = −(1/2)(e3(e^(−α) q) + e^(−α) q div_h e3), and div_h e3 = −(1/2)h(∇_3e3, e4) −
(1/2)h(∇_4e3, e3) + h(∇_1e3, e1) = −2ϖ̲ + χ̲; with e3(e^(−α)) = 2ϖ̲ e^(−α) this is the first formula, and the second is
its image.

(d) In coordinates (u, v, ϑ, φ1, φ2), √|det g| = e^ψ √|det g3| and √|det h| = e^(3ψ) √|det g3|, and since q and u do
not depend on φ1, φ2, g⁻¹du = g3⁻¹du = e^(2ψ) h⁻¹du has no φ-components. Hence div_g(q g⁻¹du) = e^(−ψ) |det g3|^(−1/2)
∂_a(e^ψ |det g3|^(1/2) q e^(2ψ) (h⁻¹du)^a) = e^(−ψ) |det g3|^(−1/2) ∂_a(|det h|^(1/2) q (h⁻¹du)^a) = e^(2ψ)
div_h(q h⁻¹du), and the same for dv. ∎

**Lemma {#lem:civp-large-reduction}** (The class system off the axes.) Let g be a metric of the form
[[eq:loc-double-null]] on an open set of D × (0, π/2) × T², D ⊂ Q1, and q_in, q_out ≥ 0 functions of (u, v, ϑ), and let
h, ψ, ω be as in [[eq:civp-large-h]]. Then (g, v, u, q_in, q_out) solves [[eq:class-system]] if and only if

    Ric[h] = q_in dv ⊗ dv + q_out du ⊗ du + (3/2) dψ ⊗ dψ + 2 dω ⊗ dω,      □_hψ = □_hω = 0,
    e3q_in = −χ̲ q_in,      e4q_out = −χ q_out.  {#eq:civp-large-reduced}

*Proof.* g⁻¹(du, du) = g⁻¹(dv, dv) = 0 holds for every metric of the form [[eq:loc-double-null]]. T := q_in dv ⊗ dv +
q_out du ⊗ du has no φ-components, so in the notation of [[prop:reduction]] the equations Ric(g) = T are R11 = R22 = 0,
vanishing mixed components and Ric[g]_ab = T_ab on the orbit space; the mixed components vanish for every class metric
([[lem:warped-ricci]]). By [[prop:reduction]], R11 = R22 = 0 is equivalent to □_hψ = □_hω = 0, and then
Ric[h]_ab = Ric[g]_ab + (3/2)∂_aψ∂_bψ + 2∂_aω∂_bω, so Ric[g] = T on the orbit space is the first equation. The dust
equations are div_g(q_in g⁻¹dv) = 0 and div_g(q_out g⁻¹du) = 0, equivalent by [[lem:civp-large-frame]] (d) and
[[eq:civp-large-dust]] to the last two. ∎

In the frame, T(e4, e4) = e^(−2α) q_in, T(e3, e3) = e^(−2α) q_out and the other components of T vanish, since
dv(e4) = du(e3) = e^(−α) and dv(e3) = du(e4) = dv(e1) = du(e1) = 0. Only Ric_44 and Ric_33 carry a density.

*The evolution system.* Its unknown is f = (f₃, f₄), in the notation of [CCTW16] f = (ϕ, ψ) with ϕ = f₃ and ψ = f₄
(the letters f₃, f₄ avoid a clash with the function ψ), with

    f₃ := (χ̲, η̲, ϖ, q_in, ψ°, ψ_4, ψ_1, ω°, ω_4, ω_1),
    f₄ := (α, β, b, χ, η, ϖ̲, q_out, ψ, ψ_3, ψ′_1, ω, ω_3, ω′_1),

twenty-three real functions of (u, v, ϑ). For Ψ ∈ {ψ, ω}, the unknowns Ψ°, Ψ_4, Ψ_1, Ψ_3, Ψ′_1 stand for Ψ, e4Ψ, e1Ψ, e3Ψ
and e1Ψ; the others for the quantities of the same name. We put D_3 := ∂_u + b∂_ϑ, k := e^(α−β) and

    M_44 := e^(−2α) q_in + (3/2)ψ_4² + 2ω_4²,      M_33 := e^(−2α) q_out + (3/2)ψ_3² + 2ω_3²,
    M_34 := (3/2)ψ_3ψ_4 + 2ω_3ω_4,   M_41 := (3/2)ψ_4ψ′_1 + 2ω_4ω′_1,   M_31 := (3/2)ψ_3ψ_1 + 2ω_3ω_1,
    M_11 := (3/2)ψ′_1² + 2ω′_1²,                                                                  {#eq:civp-large-m}

the frame components of q_in dv² + q_out du² + (3/2)dψ² + 2dω² written with the unknowns. The *evolution system*,
each equation multiplied by e^α, is, for Ψ ∈ {ψ, ω},

    ∂_vα = −2e^α ϖ,   ∂_vβ = e^α χ,   ∂_vb = −2e^(2α−β) (η − η̲),
    ∂_vχ = −e^α (χ² + 2ϖχ + M_44),   ∂_vη = −e^α (M_41 + χ(η − η̲)),
    ∂_vϖ̲ = e^α (2ϖϖ̲ + (1/2)η² − ηη̲ + (1/4)(M_34 + M_11)),   ∂_vq_out = −e^α χ q_out,   ∂_vΨ = e^α Ψ_4,
    ∂_vΨ_3 − k ∂_ϑΨ_1 = e^α ((2ϖ − (1/2)χ)Ψ_3 − (1/2)χ̲Ψ_4 + 2η̲Ψ_1),
    ∂_vΨ′_1 − k ∂_ϑΨ_4 = e^α ((1/2)(η + η̲)Ψ_4 − χΨ′_1),
    D_3χ̲ = −e^α (χ̲² + 2ϖ̲χ̲ + M_33),   D_3η̲ = −e^α (M_31 + χ̲(η̲ − η)),
    D_3ϖ = e^α (2ϖϖ̲ + (1/2)η̲² − ηη̲ + (1/4)(M_34 + M_11)),   D_3q_in = −e^α χ̲ q_in,   D_3Ψ° = e^α Ψ_3,
    D_3Ψ_4 − k ∂_ϑΨ′_1 = e^α ((2ϖ̲ − (1/2)χ̲)Ψ_4 − (1/2)χΨ_3 + 2ηΨ′_1),
    D_3Ψ_1 − k ∂_ϑΨ_3 = e^α ((1/2)(η + η̲)Ψ_3 − χ̲Ψ_1).                                           {#eq:civp-large-system}

The equations of the first five lines have ∂_v and govern f₄; those of the last four have D_3 and govern f₃.

**Proposition {#prop:civp-large-system}** (The doubly-null form.) Write [[eq:civp-large-system]] as A^u∂_uf + A^v∂_vf +
A^ϑ∂_ϑf = G(f) on ℝ² × Y, Y an interval or a circle, with the Euclidean scalar product on ℝ²³ and the flat connection
∂. Then A^u, A^v, A^ϑ are symmetric and smooth functions of f, G is a smooth function of f, and

    A^u = diag(I₁₀, 0),      A^v = diag(0, I₁₃),      A^ϑ = (b I₁₀, Q; Qᵀ, 0),  {#eq:civp-large-form}

in the splitting f = (f₃, f₄), where the 10 × 13 matrix Q has exactly four nonzero entries, each equal to −k =
−e^(α−β), at the pairs (ψ_4, ψ′_1), (ψ_1, ψ_3), (ω_4, ω′_1), (ω_1, ω_3), so that |Q| = e^(α−β) in the operator norm. In
particular the system has the form (2.7)–(2.8) of [CCTW16] ([[thm:std-cctw-existence]]), with A^u_ϕϕ = I₁₀ > 0 and
A^v_ψψ = I₁₃ > 0, the scalar product, and the flat connection as both ∇ and ∇̊, preserving the splitting. Moreover:

(a) if (g, v, u, q_in, q_out) is a class solution in the gauge on D × S³, its *reduced fields* (the connection
coefficients of h, the densities, α, β, b, and Ψ° = Ψ, Ψ_4 = e4Ψ, Ψ_3 = e3Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}) solve
[[eq:civp-large-system]] on D × (0, π/2);

(b) conversely, let f be a smooth solution of [[eq:civp-large-system]] on an open set U ⊂ D × (0, π/2) that is
*geometric* there: χ, χ̲, η, η̲, ϖ, ϖ̲ are the connection coefficients of the metric h of [[eq:civp-large-h]] built
from (α, β, b), Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ, and Ric[h] equals the tensor with the frame components
[[eq:civp-large-m]]; and let q_in, q_out ≥ 0 on U. Then g := e^(−2ψ) h + e^(ψ−2ω) dφ1² + e^(ψ+2ω) dφ2², with v, u,
q_in, q_out, is a solution of [[eq:class-system]] on U × T², of the form [[eq:loc-double-null]] with Ω = e^(α−ψ), γ_ϑ =
e^(2β−2ψ), A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2.

*Proof.* The coefficients of the derivatives are read off [[eq:civp-large-system]]: each f₃-equation has the operator
D_3 = ∂_u + b∂_ϑ on its own unknown and no ∂_v, each f₄-equation has ∂_v on its own unknown and no ∂_u, and the only
other derivatives are −k∂_ϑΨ_1 in the Ψ_3-equation and −k∂_ϑΨ_3 in the Ψ_1-equation, −k∂_ϑΨ_4 in the Ψ′_1-equation and
−k∂_ϑΨ′_1 in the Ψ_4-equation. So A^ϑ is symmetric with the stated blocks, and A^u, A^v are as stated. The coefficients
and G are polynomials in f, e^(±α), e^(±β), hence smooth for all values of f; positivity of A^u_ϕϕ, A^v_ψψ needs no
restriction on f.

(a) Multiplied by e^(−α), the equations are, line by line: [[eq:civp-large-coefficients]] for ϖ, χ and ζ = (η − η̲)/2;
(F1), (F2), (F3′) and the second formula of [[eq:civp-large-dust]] with [[lem:civp-large-reduction]]; e4Ψ = Ψ_4;
[[eq:civp-large-box]] (image) with □_hΨ = 0; the commutator [e4, e1]Ψ = (e1α) e4Ψ − χ e1Ψ with e1α = (η + η̲)/2; then
(F1′), (F2′), (F3) and the first formula of [[eq:civp-large-dust]]; e3Ψ = Ψ_3; [[eq:civp-large-box]] with □_hΨ = 0;
and [e3, e1]Ψ = (e1α) e3Ψ − χ̲ e1Ψ. In each, Ric[h] is replaced by the tensor of [[eq:civp-large-m]], which is the right
side of the first equation of [[eq:civp-large-reduced]] in the frame.

(b) By hypothesis the first equation of [[eq:civp-large-reduced]] holds; the equations of [[eq:civp-large-system]] for
Ψ_3 and Ψ_4, with the geometric identifications and [[eq:civp-large-box]], give □_hψ = □_hω = 0; those for q_in and
q_out give the dust equations. [[lem:civp-large-reduction]] concludes, and [[eq:civp-large-h]] gives the form. ∎

The equations for χ, η, ϖ̲, χ̲, η̲, ϖ are (F1), (F2), (F3′), (F1′), (F2′), (F3): each connection coefficient is
transported along e3 or e4, with no angular derivative of an unknown, and the densities enter only the two Raychaudhuri
equations, through M_44 and M_33. The wave block is the first-order form of [CCTW16, (4.47)–(4.50), p. 47], with their
ℓ and ω in the roles of e3 and e4; there the first equations of (4.48) and (4.50) are misprinted, and with ϕ0 = ψ0 = h
they read ℓ(ϕ0) = ψ₋ and ω(ψ0) = ϕ₊, the forms used here. The equations (F4), (F5), their images and the relations of
[[eq:civp-large-coefficients]] for χ̲, ϖ̲ and η + η̲ are not part of the system; they hold for the reduced fields of a
solution, and they determine the data on the cones.

#### Data on the two cones {#sec:civp-large-data}

**Lemma {#lem:civp-large-data}** (The data of the evolution system.) (a) Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂
Q1 and let g, g′ be class solutions in the gauge on neighbourhoods of the two edges N_o := {u_c} × [v_c, v_c + l_v] and
N_i := [u_c, u_c + l_u] × {v_c} (times S³) that induce the same functions Ω, γ_ϑ, b, A_c, A_s, q_in on N_o and the same
Ω, γ_ϑ, b, A_c, A_s, q_out on N_i. Then their reduced fields have the same f₃-components on N_o and the same
f₄-components on N_i. More precisely, for the reduced fields of a class solution in the gauge: the values at the corner
sphere of all reduced fields are given by [[eq:civp-large-coefficients]] in the functions on N_o and N_i near it; on
N_o the f₃-components other than χ̲ are the functions on N_o and their derivatives along N_o, ϖ and η̲ through
[[eq:civp-large-coefficients]], and χ̲ solves (F4′) along N_o with M_11 in place of Ric_11; on N_i the f₄-components
other than η and χ are the functions on N_i and their derivatives along N_i, ϖ̲ through [[eq:civp-large-coefficients]],
and η and χ solve (F5) (with η̲ = 2e1α − η) and (F4) along the integral curves of e3 in N_i with M_31, M_11 in place of
Ric_31, Ric_11.

(b) Let cone data on Q1 be given. Define on 𝒞_out, from its functions and with α, β, ψ, ω as in [[eq:civp-large-h]],

    ϖ := −(1/2) e4α,   η̲ := (1/4) e^(β−2α) ∂_vb + e1α,   Ψ° := Ψ,   Ψ_4 := e4Ψ,   Ψ_1 := e1Ψ,

q_in as given, and χ̲ the solution of the linear equation (F4′), e4χ̲ = 2e1η̲ + 2η̲² + 2ϖχ̲ − χχ̲ + M_11 with χ := e4β
and M_11 := (3/2)(e1ψ)² + 2(e1ω)², whose value at v = 0 is e^(−α)∂_uβ computed on 𝒞_in. Define on 𝒞_in, where b = 0 and
e3 = e^(−α)∂_u,

    ϖ̲ := −(1/2) e3α,   Ψ_3 := e3Ψ,   Ψ′_1 := e1Ψ,

α, β, b = 0, Ψ and q_out as given, η the solution of the linear equation (F5), e3η = M_31 − 2χ̲η − 4e1ϖ̲ − 4ϖ̲ e1α with
χ̲ := e3β and M_31 := (3/2)e3ψ e1ψ + 2e3ω e1ω, whose value at u = 0 is (−1/4) e^(β−2α)∂_vb + e1α computed on 𝒞_out, and
χ the solution of the linear equation (F4), e3χ = 2e1η + 2η² + 2ϖ̲χ − χχ̲ + M_11, whose value at u = 0 is e4β computed
on 𝒞_out. Let f̄₃ be the first list on 𝒞_out and f̄₄ the second on 𝒞_in. Then:

(i) the restriction of [[eq:civp-large-system]] to 𝒞_out, the f₄-equations with f₃ = f̄₃, with the values of f̄₄ at S
as initial values, has a solution on all of 𝒞_out ∩ (Q1 × (0, π/2)), and the restriction to 𝒞_in, the f₃-equations
with f₄ = f̄₄, with the values of f̄₃ at S, has one on all of 𝒞_in ∩ (Q1 × (0, π/2));

(ii) f̄ and the two solutions of (i) equal the background's reduced fields at every point with ϑ ∉ (ϑ_a, ϑ_b);

(iii) the reduced fields of every class solution in the gauge on D × S³, D ⊂ Q1 a past set, that induces the cone data
have f₃ = f̄₃ on 𝒞_out ∩ D and f₄ = f̄₄ on 𝒞_in ∩ D, and solve the two restricted problems of (i) there.

*Proof.* (a) On N_o the fields e4 and e1 are tangent, and on N_i the fields e3 and e1 are. So on N_o the components ϖ,
η̲ = −ζ + e1α (by [[eq:civp-large-coefficients]], ζ holding ∂_vb), q_in, Ψ°, Ψ_4, Ψ_1 of either solution are given by
the induced functions, and χ̲ solves (F4′) along the generators of N_o, with Ric_11 = M_11 by
[[lem:civp-large-reduction]], a linear equation whose coefficients are given by the induced functions; its value at
the corner is e3β + e^(−α)∂_ϑb, given by the functions on N_i. On N_i, α, β, b, ϖ̲, q_out, Ψ, Ψ_3, Ψ′_1 are given by
the induced functions, and η and χ solve (F5) and (F4) along the integral curves of e3, with Ric_31 = M_31 and
Ric_11 = M_11, linear transport equations with initial values at u = u_c given by the functions on N_o (η = ζ + e1α
and χ = e4β there). Each integral curve of D_3 = ∂_u + b∂_ϑ in N_i starts on the corner circle, so these values are
determined.

(b) (iii) is (a) for g and the data, together with [[prop:civp-large-system]] (a); the values at u = 0 or v = 0 used in
(b) are those of the reduced fields at S. For (i) on 𝒞_out, take for (α, β, b, χ, η, Ψ, Ψ′_1) the functions given by
the data, with χ := e4β, η := ζ + e1α, ζ := −(1/4)e^(β−2α)∂_vb and Ψ′_1 := e1Ψ. They solve the corresponding equations
of [[eq:civp-large-system]]: those for α, β, b, Ψ by [[eq:civp-large-coefficients]]; that for χ by (F1) and the
constraint Ric(∂_v, ∂_v) = q_in, which by [[prop:reduction]] (the term with R11, R22 being multiplied by g3(∂_v, ∂_v) =
0) reads Ric[h](∂_v, ∂_v) = q_in + (3/2)(∂_vψ)² + 2(∂_vω)², that is Ric_44 = M_44; that for η by (F2) and the
constraint Ric(∂_v, ∂_ϑ) = 0, which reads Ric_41 = M_41 (g3(∂_v, ∂_ϑ) = 0); and that for Ψ′_1 by the commutator [e4,
e1]. The remaining equations, for Ψ_3, then ϖ̲, then q_out, are linear in these unknowns with coefficients defined on
all of 𝒞_out, so they have solutions there. On 𝒞_in, take χ̲ := e3β, η̲ := 2e1α − η, Ψ° := Ψ and Ψ_1 := e1Ψ. The
equation for χ̲ holds by (F1′) and the constraint Ric(∂_u, ∂_u) = q_out (g3(∂_u, ∂_u) = γ_ϑ b² = 0 on 𝒞_in), that for
Ψ°, Ψ_1 by the definitions and [e3, e1]; that for η̲ holds because, by the equation defining η and 2e3e1α = −4e1ϖ̲ −
(2ϖ̲ + χ̲)(η + η̲) (proof of (F5)), D_3η̲ = e^α(2e3e1α − e3η) = −e^α(M_31 + χ̲(η̲ − η)). The equations for Ψ_4, then ϖ,
then q_in are linear and have solutions on all of 𝒞_in. In each case the initial values at S are those of f̄, so these
are the solutions of (i).

(ii) Every formula and every coefficient of the equations above at an angle ϑ is built from the functions of the data
and their derivatives at ϑ, and so are the initial values at S; the equations are ordinary differential equations along
the lines {ϑ = const}, since b = 0 on 𝒞_in and the f₄-equations contain no ∂_ϑ of an f₄-unknown. At ϑ ∉ (ϑ_a, ϑ_b) the
data are the background's on a neighbourhood of ϑ, the background's reduced fields solve all the equations used
([[prop:civp-large-system]] (a)), and by uniqueness for these equations f̄ and the solutions of (i) are the
background's there. ∎

#### An energy identity {#sec:civp-large-energy}

**Lemma {#lem:civp-large-energy}** (Energy for systems in doubly-null form.) Let 𝒬 := [u_c, u_c + l_u] × [v_c, v_c +
l_v], let J = [ϑ₋, ϑ₊] be an interval, or an arc of a circle with a coordinate ϑ on it, and let z = (z₃, z₄), of class
C¹ on 𝒬 × J with values in ℝ^(N₃) × ℝ^(N₄), solve

    ∂_u z₃ + P ∂_ϑ z₃ + Q ∂_ϑ z₄ = B₃ z,      ∂_v z₄ + Qᵀ ∂_ϑ z₃ = B₄ z,  {#eq:civp-large-linear}

with P symmetric, P and Q of class C¹ and B₃, B₄ continuous on 𝒬 × J. Assume z₃ = 0 on {u_c} × [v_c, v_c + l_v] × J
and z₄ = 0 on [u_c, u_c + l_u] × {v_c} × J.

(a) Let |P| ≤ p and |Q| ≤ q on 𝒬 × J (operator norms), let t > 0, c1 := p + t, c2 := q²/t and w(u, v) := c1(u − u_c) +
c2(v − v_c). Then z = 0 at every point of 𝒬 × J with ϑ₋ + w(u, v) ≤ ϑ ≤ ϑ₊ − w(u, v).

(b) If z = 0 on 𝒬 × ([ϑ₋, ϑ₋ + ε] ∪ [ϑ₊ − ε, ϑ₊]) for some ε > 0, then z = 0 on 𝒬 × J.

*Proof.* Put A^u := diag(I, 0), A^v := diag(0, I) and A^ϑ := (P, Q; Qᵀ, 0), so that [[eq:civp-large-linear]] reads
A^μ∂_μz = Bz with B := (B₃; B₄), and for λ ≥ 0 let X^μ := e^(−λ(u+v)) ⟨z, A^μz⟩, μ ∈ {u, v, ϑ}, a C¹ vector field in
the coordinates (u, v, ϑ). Since the A^μ are symmetric and A^u, A^v are constant,

    ∂_μX^μ = e^(−λ(u+v)) (−λ ⟨z, (A^u + A^v)z⟩ + ⟨z, (∂_ϑA^ϑ)z⟩ + 2⟨z, Bz⟩) ≤ e^(−λ(u+v)) (C₁ − λ) |z|²,

with C₁ := sup_(𝒬×J) (|∂_ϑA^ϑ| + 2|B|), finite since 𝒬 × J is compact, and A^u + A^v = I. Fix λ > C₁.

(a) Fix (u′, v′) ∈ 𝒬 with ϑ₋ + w(u′, v′) ≤ ϑ₊ − w(u′, v′), and let W be the set of (u, v, ϑ) with u_c ≤ u ≤ u′,
v_c ≤ v ≤ v′ and ϑ₋ + w(u, v) ≤ ϑ ≤ ϑ₊ − w(u, v); since w increases in u and v, its sections are nonempty intervals,
and W is compact with a piecewise smooth boundary. By the divergence theorem ∫_W ∂_μX^μ = ∫_(∂W) X^μ ν_μ dS, with ν the
outer unit conormal. On the face u = u′, X^μν_μ = e^(−λ(u+v)) |z₃|² ≥ 0; on v = v′ it is e^(−λ(u+v)) |z₄|² ≥ 0; on
u = u_c and v = v_c it vanishes, since these faces lie in the sets where z₃, respectively z₄, vanish. On the face
ϑ = ϑ₊ − w the conormal is a positive multiple of dϑ + c1 du + c2 dv, and on ϑ = ϑ₋ + w one of −dϑ + c1 du + c2 dv, so
X^μν_μ is a positive multiple of e^(−λ(u+v)) ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩, and

    ⟨z, (±A^ϑ + c1A^u + c2A^v)z⟩ ≥ (c1 − p)|z₃|² − 2q|z₃||z₄| + c2|z₄|² = (t^(1/2)|z₃| − q t^(−1/2)|z₄|)² ≥ 0.

Hence 0 ≤ ∫_(∂W) X^μν_μ dS = ∫_W ∂_μX^μ ≤ (C₁ − λ) ∫_W e^(−λ(u+v)) |z|², so z = 0 on W, and in particular at (u′, v′)
for every ϑ with ϑ₋ + w ≤ ϑ ≤ ϑ₊ − w.

(b) Take W := [u_c, u′] × [v_c, v′] × J. The faces u = u′, v = v′, u = u_c, v = v_c contribute as in (a), and on the
faces ϑ = ϑ± the field X vanishes, since z does. The same inequality gives z = 0 on W. ∎

#### Local developments {#sec:civp-large-local}

**Proposition {#prop:civp-large-corner}** (Developments near a corner sphere, without smallness.) Let m := 114, the
regularity index m_1 = 12k + 42 of [[prop:loc-cone-local]] for k = 6, and κ ∈ (0, π/8]. For every Λ > 0 there is σ > 0
with the following property. Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ Q1, N_o := {u_c} × [v_c, v_c + l_v] and N_i
:= [u_c, u_c + l_u] × {v_c}. Let smooth functions Ω > 0, γ_ϑ > 0, b, A_c, A_s and q_in ≥ 0 of (v, ϑ) ∈ [v_c, v_c + l_v]
× (0, π/2), and Ω > 0, γ_ϑ > 0, A_c, A_s and q_out ≥ 0 of (u, ϑ) ∈ [u_c, u_c + l_u] × (0, π/2), with b = 0 on N_i, be
given that agree on the corner sphere, satisfy Ric(∂_v, ∂_v) = q_in and Ric(∂_v, ∂_ϑ) = 0 on N_o and Ric(∂_u, ∂_u) =
q_out on N_i, equal the background's at the points with ϑ ∉ [2κ, π/2 − 2κ], and whose differences from the background's,
with ln Ω, ln γ_ϑ in place of Ω, γ_ϑ, have C^m norms at most Λ. Then there is a class solution in the gauge on [u_c,
u_c + min(l_u, σ)] × [v_c, v_c + min(l_v, σ)] × S³ that induces these functions on the two edges and equals (g0, q̊_in,
q̊_out) at the points with ϑ ∉ [κ, π/2 − κ].

*Proof.* Choose d ∈ (0, 1] such that the open set 𝒪 of the notation at the beginning of this section contains the points
within 4d of Q1 in each coordinate. In the notation of [[prop:loc-cone-local]], with Q := Q1, k := 6, η := κ, λ_u := l_u
and λ_v := l_v, the background is g_e = −2e^(2σ_e) du dv + R_e² dΩ₃² with e^(2σ_e) := 2Ω² and R_e := R, solving
[[eq:two-dust-limit]] on 𝒪 ∩ {u ≥ 0, v ≥ 0}, and the given functions are data of that proposition, with ϰ_1 = ½ ln γ_ϑ,
ϰ_2 = A_c, ϰ_3 = A_s: the C^m norm of ϰ_1 − ϰ̊_1 is half that of ln γ_ϑ − ln γ̊_ϑ, so each difference has C^m norm at
most Λ. That proposition gives the solution, with σ depending only on κ, Λ, d and bounds for the background on the
points within 4d of Q1. ∎

#### The theorem {#sec:civp-large-theorem}

**Theorem {#thm:civp-large}** (Developments of cone data without smallness.) Let cone data on Q1 be given
([[def:civp-large-data]]), with η0 and J0 as in [[eq:civp-large-band]]; no smallness is assumed. There is δ > 0 such
that, with 𝒮_δ := {(u, v) ∈ Q1 : min(u, v) ≤ δ}, the following hold.

(a) *Existence.* There is a class solution (g, v, u, q_in, q_out) in the gauge on 𝒮_δ × S³ that induces the cone data.
So v and u are the phases of the ingoing and the outgoing family of [[eq:class-system]] with N_f = 2, and the
development contains the strips {u ≤ δ} along 𝒞_out and {v ≤ δ} along 𝒞_in, a future neighbourhood of both cones.

(b) *Localisation.* g = g0, q_in = q̊_in and q_out = q̊_out at the points of 𝒮_δ × S³ with ϑ ∉ [ϑ_a − η0, ϑ_b + η0].

(c) *Uniqueness in the gauge.* Let D′ ⊂ Q1 be a past set and (g′, v, u, q′_in, q′_out) a class solution in the gauge
on D′ × S³ that induces the cone data on 𝒞_out ∩ D′ and 𝒞_in ∩ D′ and equals (g0, q̊_in, q̊_out) at the points with
ϑ ∉ [η′, π/2 − η′], for some η′ > 0. Then it equals (g, q_in, q_out) on (D′ ∩ 𝒮_δ) × S³.

(d) *The neighbourhood.* 𝒮_δ ⊃ {(u, v) ∈ Q1 : uv ≤ δ²}, and δ = min(s1, s2) with s1, s2 of [[eq:civp-large-delta]]:
they are given by constants a*, b* that [[thm:std-cctw-strips]] provides for the localised system
[[eq:civp-large-localised]] with the data of [[lem:civp-large-data]], for any choice of the cut-off and the extension
in its definition, and by three suprema of its solution, and they depend on the cone data through these. No lower bound
for δ in terms of norms of the cone data is asserted.

The proof of (a) uses [[prop:civp-large-corner]]; (b), (c) and (d) do not.

*Proof.* Since uv ≤ δ² implies u ≤ δ or v ≤ δ, 𝒮_δ contains {uv ≤ δ²}.

*Step 1: the localised system.* Let Y := ℝ/πℤ, which contains J0 ⊂ (0, π/2) as an arc. Fix ϱ ∈ C^∞(Y) with 0 ≤ ϱ ≤ 1,
ϱ = 1 on [ϑ_a − η0, ϑ_b + η0] and supp ϱ ⊂ (ϑ_a − 2η0, ϑ_b + 2η0). Let f̊ be the reduced fields of the background on
Q1 × (0, π/2), and f̊_e ∈ C^∞(Q1 × Y; ℝ²³) a function that equals f̊ on Q1 × J0 and whose b-component vanishes (b̊ = 0).
With A^u, A^v, A^ϑ and G of [[prop:civp-large-system]], the *localised system* is

    A^u∂_uf + A^v∂_vf + ϱ A^ϑ(f) ∂_ϑf = ϱ G(f) + (1 − ϱ)(A^u∂_u + A^v∂_v) f̊_e      on Q1 × Y.
                                                                                               {#eq:civp-large-localised}

It has the form (2.7)–(2.8) of [CCTW16]: A^u = diag(I₁₀, 0) and A^v = diag(0, I₁₃) are unchanged, ϱA^ϑ(f) is symmetric,
and the coefficients and the right side are smooth functions of f and of (u, v, ϑ). It coincides with
[[eq:civp-large-system]] where ϱ = 1. The function f̊_e solves it: where ϱ = 0 trivially, and on supp ϱ ⊂ J0 because
there f̊_e = f̊ solves [[eq:civp-large-system]] ([[prop:civp-large-system]] (a) for g0), so that both sides equal
A^u∂_uf̊ + A^v∂_vf̊ + ϱA^ϑ(f̊)∂_ϑf̊. Its data are ϕ̄ := f̄₃ on {u = 0} × J0 and f̊_e,₃ on the rest of {u = 0} × Y, and
ψ̄ := f̄₄ on {v = 0} × J0 and f̊_e,₄ on the rest, with f̄ of [[lem:civp-large-data]] (b); they are smooth, because f̄ =
f̊ at the points of J0 with ϑ ∉ (ϑ_a, ϑ_b) ([[lem:civp-large-data]] (b) (ii)). The transport equations [CCTW16,
(3.100)–(3.101)] of [[thm:std-cctw-existence]] for this system are its f₃-equations restricted to {v = 0} and its
f₄-equations restricted to {u = 0}. They have global solutions: on J0 take the solutions of [[lem:civp-large-data]] (b)
(i), and on the rest of Y the restrictions of f̊_e. Where ϱ = 1 these are the equations of [[lem:civp-large-data]] (b)
(i); at the other points of J0 those solutions equal f̊ ([[lem:civp-large-data]] (b) (ii)), which solves the localised
system; and the two pieces agree near the ends of J0.

*Step 2: the strip solution.* [[thm:std-cctw-existence]] and [[thm:std-cctw-strips]] apply with n = 2, a0 := u_1, b0 :=
v_1 and any integer ℓ ≥ 6 (ℓ > (n + 9)/2): Y is a compact one-dimensional manifold without boundary, the system has the
form (2.7)–(2.8) with the scalar product, and the flat connection as both ∇ and ∇̊, preserving the splitting, the data
are smooth, and the transport equations have global solutions. They give a* ∈ (0, u_1], b* ∈ (0, v_1] and a solution f of
[[eq:civp-large-localised]] with these data on 𝒰 := ([0, a*] × [0, v_1] ∪ [0, u_1] × [0, b*]) × Y, unique among C¹
solutions and smooth, the data being smooth.

*Step 3: localisation and δ.* Put z := f − f̊_e on 𝒰. Subtracting the equations for f and f̊_e,

    A^u∂_uz + A^v∂_vz + ϱA^ϑ(f)∂_ϑz = ϱ(G(f) − G(f̊_e)) − ϱ(A^ϑ(f) − A^ϑ(f̊_e))∂_ϑf̊_e,

whose right side is B z with B := ϱ∫_0^1 (dG − (dA^ϑ)∂_ϑf̊_e)(f̊_e + s z) ds continuous. This is [[eq:civp-large-linear]]
with P := ϱb I₁₀ and Q := ϱQ(f), b and Q(f) evaluated on f. Its data vanish on the arc I := Y ∖ (ϑ_a, ϑ_b). Let

    p1 := sup |b| over [0, a*] × [0, v_1] × Y,      β1 := sup |∂_vb| over [0, u_1] × [0, b*] × Y,
    q1 := sup e^(α−β) over 𝒰,      s1 := min(a*, η0²/(2p1η0 + 4q1²v_1)),
    s2 := min(b*, η0/(4u_1β1), η0²/(8q1²u_1)),      δ := min(s1, s2),
                                                                                             {#eq:civp-large-delta}

with the middle term of s2 omitted if β1 = 0, the components b, α, β being those of f. On [0, s1] × [0, v_1] apply
[[lem:civp-large-energy]] (a) with J := I, p := p1, q := q1 and t := 2q1²v_1/η0: then c2 = η0/(2v_1), c1 = p1 + t, and
w = c1u + c2v ≤ c1s1 + η0/2 ≤ η0. On [0, u_1] × [0, s2] the b-component of f vanishes at v = 0, both on J0 (b = 0 on
𝒞_in) and elsewhere (f̊_e has b = 0), so |b| ≤ β1 v ≤ β1 s2 ≤ η0/(4u_1) =: p there; with t := η0/(4u_1), c1 = p + t ≤
η0/(2u_1) and c2 = 4q1²u_1/η0, so w ≤ η0/2 + c2s2 ≤ η0. On both strips, therefore, z = 0 at the points of I at distance
at least η0 from its ends, that is

    f = f̊_e  at the points of 𝒮 × Y with ϑ ∉ (ϑ_a − η0, ϑ_b + η0),   𝒮 := [0, s1] × [0, v_1] ∪ [0, u_1] × [0, s2] ⊃ 𝒮_δ.

Define F on 𝒮_δ × (0, π/2) by F := f on J0 and F := f̊ off J0. It is smooth, since f = f̊_e = f̊ near the ends of J0; it
equals f̊ at the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0]; and it solves [[eq:civp-large-system]], since ϱ = 1 on [ϑ_a − η0,
ϑ_b + η0] and f̊ solves [[eq:civp-large-system]]. On 𝒞_out its f₃-components are f̄₃, and its f₄-components solve the
restriction of Step 1 with the same initial values at S; that restriction is a system of ordinary differential equations
in v along the lines {ϑ = const} (A^ϑ has no f₄f₄-block), so they are the solution of [[lem:civp-large-data]] (b) (i),
whose components α, β, b, ψ, ω are the functions of the data. Likewise on 𝒞_in its f₄-components are f̄₄ and its
f₃-components the solution of [[lem:civp-large-data]] (b) (i), b vanishing there.

*The signs of the densities.* The components q_in and q_out of F are nonnegative on 𝒮_δ × (0, π/2). Let (u′, v′) ∈ 𝒮_δ
and ϑ′ ∈ (0, π/2). Since 𝒮_δ is a past set, the segments [0, u′] × {v′} and {u′} × [0, v′] lie in it. The component b of
F is smooth on 𝒮_δ × (0, π/2) and vanishes at the angles outside [ϑ_a − η0, ϑ_b + η0], where F = f̊; so the constant
functions ϑ_a − η0 and ϑ_b + η0 solve dϑ/du = b(u, v′, ϑ), and by uniqueness the solution ϑ(·) with ϑ(u′) = ϑ′ stays in
[ϑ_a − η0, ϑ_b + η0] if ϑ′ lies there, and is constant otherwise. It therefore exists on all of [0, u′], with values in
(0, π/2), and c(u) := (u, v′, ϑ(u)) is an integral curve of D_3 = ∂_u + b∂_ϑ. By the equation D_3q_in = −e^α χ̲ q_in of
[[eq:civp-large-system]], (q_in ∘ c)′ = −(e^α χ̲ q_in) ∘ c, so

    q_in(u′, v′, ϑ′) = q_in(0, v′, ϑ(0)) exp(−∫_0^(u′) (e^α χ̲)(c(u)) du).

At u = 0, q_in is a component of f̄₃, the q_in of the data, which is nonnegative; so q_in(u′, v′, ϑ′) ≥ 0. Likewise the
equation ∂_vq_out = −e^α χ q_out gives q_out(u′, v′, ϑ′) = q_out(u′, 0, ϑ′) exp(−∫_0^(v′) (e^α χ)(u′, v, ϑ′) dv), and
q_out(u′, 0, ϑ′) is a component of f̄₄, the q_out of the data, which is nonnegative.

*Step 4: F is geometric.* Let h_F and g_F be the metrics built from the components α, β, b, ψ, ω of F as in
[[prop:civp-large-system]] (b); they are defined on all of 𝒮_δ × (0, π/2), times T² for g_F. F is geometric on a set
when the identities of [[prop:civp-large-system]] (b) hold at its points; on the closure of a set where they hold they
hold too, F being smooth. Where F is geometric, (g_F, v, u, q_in, q_out), extended by (g0, q̊_in, q̊_out) to the axes,
is a class solution in the gauge, by that proposition, the densities being nonnegative and F being f̊ off [ϑ_a − η0,
ϑ_b + η0]. We say that F is *geometric to first order* at a point if there its components χ, χ̲, η, η̲, ϖ, ϖ̲ are the
connection coefficients of h_F and Ψ° = Ψ, Ψ_3 = e3Ψ, Ψ_4 = e4Ψ, Ψ_1 = Ψ′_1 = e1Ψ for Ψ ∈ {ψ, ω}. We show that F is
geometric on 𝒮_δ × (0, π/2). As 𝒮_δ = 𝒯₁ ∪ 𝒯₂, 𝒯₁ := [0, δ] × [0, v_1], 𝒯₂ := [0, u_1] × [0, δ], it suffices to treat
one of them, 𝒯 = [0, l1] × [0, l2].

*Constants.* F is smooth on 𝒮_δ × (0, π/2) and equals f̊ off [ϑ_a − η0, ϑ_b + η0] ⊂ [2η0, π/2 − 2η0]. So the functions
Ω = e^(α−ψ), γ_ϑ = e^(2β−2ψ), b, A_c = (ψ − 2ω)/2, A_s = (ψ + 2ω)/2, q_in, q_out formed from F on segments {u_c} ×
[v_c, v_c + l_v] and [u_c, u_c + l_u] × {v_c} in 𝒯, transformed by the change of angle described below, have
differences from the background's whose C^m norms are bounded by one Λ, for all such segments, because F and its
derivatives are bounded on 𝒯 × [η0, π/2 − η0] and the change of angle has derivatives bounded by those of b. Let σ be
given by [[prop:civp-large-corner]] for this Λ and κ := η0, and L := σ/2.

*The corner step.* Let 𝒬 = [u_c, u_c + l_u] × [v_c, v_c + l_v] ⊂ 𝒯 with l_u, l_v ≤ σ and edges N_o, N_i, and assume: F
is geometric to first order at the points of the corner circle {(u_c, v_c)} × (0, π/2); N_o × (0, π/2) is contained in
a set on which F is geometric, or u_c = 0; and N_i × (0, π/2) is contained in a set on which F is geometric, or v_c =
0. We show that F is geometric on 𝒬 × (0, π/2). On N_o take the functions Ω, γ_ϑ, b, A_c, A_s, q_in formed from F, and
on N_i the functions Ω, γ_ϑ, b, A_c, A_s, q_out. Where an edge lies in 𝒞_out or 𝒞_in these are the cone data (Step 3),
and they satisfy the constraints by [[def:civp-large-data]] (ii); where F is geometric they are induced by the class
solution g_F, and the constraints are components of Ric(g_F) = q_in dv² + q_out du². They agree at the corner and equal
the background's off [2η0, π/2 − 2η0]. If b does not vanish on N_i, let Φ(u, ϑ) solve (∂_u + b(u, v_c, ϑ)∂_ϑ)Φ = 0 with
Φ(u_c, ϑ) = ϑ; for each u it is a diffeomorphism of (0, π/2) equal to the identity off [ϑ_a − η0, ϑ_b + η0], where b =
0. The change of angle (u, v, ϑ) ↦ (u, v, Φ(u, ϑ)) maps a metric of the form [[eq:loc-double-null]] to one of the same
form, with γ_ϑ replaced by γ_ϑ/(∂_ϑΦ)², b by ∂_uΦ + b∂_ϑΦ, and Ω, A_c, A_s unchanged, since Φ does not depend on v and
dϑ − b du = (dΦ − (∂_uΦ + b∂_ϑΦ) du)/∂_ϑΦ; it commutes with the T² action and the reflections, it is the identity on
N_o, and after it b = 0 on N_i, while b on N_o becomes b − b(u_c, v_c, ·). [[prop:civp-large-corner]] applies to the
transformed functions and gives a class solution in the gauge on 𝒬 × S³; changing the angle back gives a class solution
g_c in the gauge on 𝒬 × S³ that induces the functions above on N_o and N_i and equals (g0, q̊_in, q̊_out) off [η0, π/2
− η0]. Let f_c be its reduced fields, a solution of [[eq:civp-large-system]] on 𝒬 × (0, π/2)
([[prop:civp-large-system]] (a)). By [[lem:civp-large-data]] (a), the f₃-components of f_c on N_o and its f₄-components
on N_i are given by the functions on the edges, through [[eq:civp-large-coefficients]] and the equations (F4′) on N_o
and (F5), (F4) on N_i, with the values of f_c at the corner, which are given by [[eq:civp-large-coefficients]] in the
functions near the corner. The same holds for F. At the corner F is geometric to first order, and h_F, ψ, ω induce the
same functions on the edges as g_c, so F has the same values there as f_c. On an edge on which F is geometric, the
proof of [[lem:civp-large-data]] (a) applies to F, since it uses only identities that hold at the points of the edge.
On an edge in 𝒞_out or 𝒞_in it holds by the definition of f̄ in [[lem:civp-large-data]] (b), the linear equations there
being those used here, with the same coefficients, and the values at the corner being those of F. By uniqueness for
these linear equations, z := f_c − F has z₃ = 0 on N_o and z₄ = 0 on N_i. It solves the linear system A^μ(F)∂_μz =
G(f_c) − G(F) − (A^ϑ(f_c) − A^ϑ(F))∂_ϑf_c, of the form [[eq:civp-large-linear]] on 𝒬 × [η0/2, π/2 − η0/2], and z = 0 at
the points with ϑ ≤ η0 or ϑ ≥ π/2 − η0, where f_c = f̊ = F. By [[lem:civp-large-energy]] (b), z = 0 on 𝒬 × (0, π/2). So
F is the reduced fields of g_c on 𝒬 × (0, π/2) and is geometric there.

*Continuation in u + v.* For t > 0 let D_t := {(u, v) ∈ 𝒯 : u + v < t}, and let t* be the supremum of the t ∈ (0, l1 +
l2] such that F is geometric on D_t × (0, π/2), with t* := 0 if there is none. The corner step with 𝒬 = [0, min(L, l1)]
× [0, min(L, l2)] applies: its corner is S, where F is geometric to first order, because the values of f̄ at S are
those of [[eq:civp-large-coefficients]] in the cone data, and its edges lie in 𝒞_out and 𝒞_in. So t* ≥ min(L, l1, l2) >
0. Suppose t* < l1 + l2. F is geometric on the closure of D_t* × (0, π/2). Let Γ := {(u, v) ∈ 𝒯 : u + v = t*}, and for
p = (u_p, v_p) ∈ Γ let u_c := max(u_p − L/2, 0), v_c := max(v_p − L/2, 0) and 𝒬_p := [u_c, min(u_p + L/2, l1)] × [v_c,
min(v_p + L/2, l2)], whose sides are at most L < σ. Its corner satisfies u_c + v_c ≤ t*. If v_c > 0, the edge N_i =
[u_c, min(u_p + L/2, l1)] × {v_c} satisfies u + v ≤ u_p + L/2 + v_p − L/2 = t*, so it lies in the closure of D_t*;
likewise N_o if u_c > 0. So the corner step applies, and F is geometric on 𝒬_p × (0, π/2). Every (u, v) ∈ 𝒯 with t* ≤
u + v < t* + L/4 lies in some 𝒬_p: with s := (u + v − t*)/2 < L/8, take p := (u − s, v − s) if this point lies in 𝒯, and
otherwise the end point of Γ on the side of 𝒯 that it leaves; in both cases u_p − L/4 ≤ u ≤ u_p + L/4 and v_p − L/4 ≤ v
≤ v_p + L/4. Hence F is geometric on D_(t*+L/4) × (0, π/2), contrary to the choice of t*. So t* = l1 + l2, and F is
geometric on 𝒯 × (0, π/2).

*Step 5: the solution.* By Step 4 and [[prop:civp-large-system]] (b), g_F with v, u, q_in, q_out is a class solution in
the gauge on 𝒮_δ × (0, π/2) × T². At the points with ϑ ∉ [ϑ_a − η0, ϑ_b + η0] it equals (g0, q̊_in, q̊_out), since
F = f̊ there; extended by (g0, q̊_in, q̊_out) to the axes it is a class solution in the gauge on 𝒮_δ × S³, which gives
(a) and (b). It induces the cone data: on 𝒞_out the components α, β, b, ψ, ω of F are the functions of the data and its
q_in is the data's (Step 3), and on 𝒞_in its f₄-components are f̄₄. By [[eq:civp-large-h]] the functions Ω, γ_ϑ, b, A_c,
A_s are therefore the data's on both cones.

*Step 6: uniqueness.* Let (g′, q′_in, q′_out) be as in (c) and f′ its reduced fields on D′ × (0, π/2), a solution of
[[eq:civp-large-system]] ([[prop:civp-large-system]] (a)) with f′₃ = f̄₃ on 𝒞_out ∩ D′ and f′₄ = f̄₄ on 𝒞_in ∩ D′
([[lem:civp-large-data]] (b) (iii)), and equal to f̊ off [η′, π/2 − η′]. Put η″ := min(η′, η0). D′ ∩ 𝒮_δ is a past
set; for (u, v) in it, z := f′ − F solves on [0, u] × [0, v] × [η″/2, π/2 − η″/2] a linear system of the form
[[eq:civp-large-linear]] as in Step 4, with z₃ = 0 at u = 0, z₄ = 0 at v = 0 (Step 3), and z = 0 at ϑ ≤ η″ and at
ϑ ≥ π/2 − η″, where f′ = f̊ = F. By [[lem:civp-large-energy]] (b), f′ = F on (D′ ∩ 𝒮_δ) × (0, π/2). The metric and the
densities are determined by α, β, b, ψ, ω, q_in, q_out through [[prop:civp-large-system]] (b), so (g′, q′_in, q′_out) =
(g, q_in, q_out) there, and both equal (g0, q̊_in, q̊_out) near the axes.

(d) is [[eq:civp-large-delta]] with Steps 2 and 3. ∎

**Remark {#rem:civp-large-domain}** (How the neighbourhood depends on the data.) In [[eq:civp-large-delta]], a* and b*
are the constants of [[thm:std-cctw-strips]] for the localised system with the data of [[lem:civp-large-data]]; that
theorem asserts their existence and gives no bound for them (a* does not depend on ℓ by [[thm:std-cctw-existence]], nor
b* by that theorem with u and v exchanged). p1, q1 and β1 are suprema of the strip solution, the shift, the ratio
e^(α−β) = Ω γ_ϑ^(−1/2) and ∂_vb, and are not bounded here in terms of the data. So δ depends on the data, on the band
through η0, on u_1, v_1 and on the choice of the cut-off and the extension, and no lower bound for it in terms of norms
of the data is asserted. For data near the background's, [[thm:loc-cone-development]] gives a development on the
explicit set {uv ≤ δ_*²}; it equals g0 near the axes, so by [[thm:civp-large]] (c) the two developments agree where both
are defined. The data must equal the background's near the axes: the band lies in (0, π/2), and cone data that differ
from the background's at the axes are not treated, nor are data of finite regularity or densities that are only bounded
or measure-valued.

**Remark {#rem:civp-large-beyond}** (What the theorem adds.) With [[thm:civp-large]], the cone data of [[sec:loc-cones]]
that are localised in a band away from the axes have developments without any smallness. With u_1 = 7.2 and v_1 = 4.5,
which are admissible ([[lem:civp-large-rectangle]] (a)), every perturbation of the shell on 𝒞_out ∩ {3 < v < 4.5} and of
the packet on 𝒞_in ∩ {5.7 < u < 7.2}, together or apart, and every density added in the band, of any amplitude for which
the factors e^ϕ stay positive on [0, 4.5] and on [0, 7.2], gives cone data on Q1 ([[lem:civp-large-free]] (a)) and so
has a development. Such data exist with densities of every amplitude: the density of the shell may be multiplied by 1 +
c with −1 ≤ c ≤ 76, and that of the packet by 1 + c with −1 ≤ c ≤ 4.5, c a smooth function of ϑ with compact support in
the band, and densities of any supremum may be added on short enough intervals ([[lem:civp-large-rectangle]] (b)). The
development contains the strip {u ≤ δ} along all of 𝒞_out ∩ {v ≤ v_1} and the strip {v ≤ δ} along all of 𝒞_in ∩ {u ≤
u_1}, so the dust on the cones lies in it; it is in the double-null gauge of the class, with u and v the phases of the
two families; it is localised, equal to the background outside {ϑ_a − η0 ≤ ϑ ≤ ϑ_b + η0}, so that localisation on the
cones is localisation of a spacetime; and it is unique in the gauge among solutions that equal the background near the
axes. For vacuum cone data (v_1 < 3 and u_1 < 5.7, the densities zero), [CTG23, Theorem 1.1]
([[thm:std-ctg-neighbourhood]]) gives a vacuum development for data of any size; the theorem adds the double-null gauge,
uniqueness in it, and localisation. Compared with [[thm:loc-cone-development]], smallness is dropped and uniqueness
holds among all solutions that equal the background near the axes, not only near the background; the neighbourhood is
not explicit and no estimate of the solution is given.

### Placement

Each item names the place, the old text and the new text. Old and new texts are given as the lines of the chapter
source, unindented except where the chapter indents them, each preceded by a line ending "Old:" or "New:"; every old
text occurs exactly once in its chapter. Line numbers are those of the current chapter sources and serve only to find
the place. The section above follows [[sec:loc-cone-proof]] and uses four of its results: [[thm:loc-cone-development]],
for comparison; [[lem:loc-cone-in]], the analogue of [[prop:loc-cones]] on 𝒞_in in the gauge b = 0; the class solutions
in the gauge of [[sec:loc-cone-setting]]; and [[prop:loc-cone-local]], for [[prop:civp-large-corner]]. The sites that
both sections change, those of items 2, 3, 5 and 6 and of the second pair of item 4 below, are changed once, by the
merged texts of items 3 to 7 of the placement of [[sec:loc-cone-proof]], which name [[thm:civp-large]],
[[def:civp-large-data]], [[lem:civp-large-free]] and [[lem:civp-large-rectangle]] of this section.

*1. Where the section goes.* The section above, from its heading through [[rem:civp-large-beyond]], is inserted in
[[ch:localised-data]] after [[sec:loc-cone-proof]], which follows [[sec:loc-cones]], and before the heading
"### The static Killing field and the charge {#sec:loc-kid}" (line 602), with one blank line before and one
after. It defines sec:civp-large, eq:civp-large-band, def:civp-large-data, lem:civp-large-free,
lem:civp-large-rectangle, sec:civp-large-frame, eq:civp-large-h, lem:civp-large-frame, eq:civp-large-coefficients,
eq:civp-large-null, eq:civp-large-box, eq:civp-large-dust, eq:civp-large-table, lem:civp-large-reduction,
eq:civp-large-reduced, eq:civp-large-m, eq:civp-large-system, prop:civp-large-system, eq:civp-large-form,
sec:civp-large-data, lem:civp-large-data, sec:civp-large-energy, lem:civp-large-energy, eq:civp-large-linear,
sec:civp-large-local, prop:civp-large-corner, sec:civp-large-theorem, thm:civp-large, eq:civp-large-localised,
eq:civp-large-delta, rem:civp-large-domain and rem:civp-large-beyond, none of which is defined elsewhere; the prefix may
be changed to the chapter's prefix loc- without other changes. Numbers are resolved at assembly.

*2. [[ch:localised-data]], its opening paragraph (lines 8–9).* Changed by item 3 of the placement of
[[sec:loc-cone-proof]], whose new text is the merged text for both sections; no separate change.

*3. [[ch:localised-data]], the paragraph after [[prop:loc-cones]] (lines 593–600).* Changed by item 4 of the placement
of [[sec:loc-cone-proof]], whose new text is the merged text for both sections; no separate change.

*4. [[ch:scope]], the paragraph on localised data (lines 201–202).* Its opening sentence changes; its last line (line
210) is changed by item 7 of the placement of [[sec:loc-cone-proof]], whose new text is the merged text for both
sections. Old:

The results on localised data concern the explicit two-dust background of [[sec:bg-data]], on its slice Σ_τ0 or on a
slice bent from it, and invariant data near the background's data ([[ch:localised-data]]). Data localised in angle away

New:

The results on localised data concern the explicit two-dust background of [[sec:bg-data]]: invariant data near the
background's data on its slice Σ_τ0 or on a slice bent from it, and data of any size on the two null cones through its
corner sphere ([[ch:localised-data]]). Data localised in angle away

*5. [[ch:introduction]], the paragraph on [[part:further]] (lines 192–193).* Changed by item 5 of the placement of
[[sec:loc-cone-proof]], whose old text (lines 191–193) contains these lines and whose new text names the development
from two null cones; no separate change.

*6. [[ch:theorems]], the item *More families* (line 376).* Changed by item 6 of the placement of [[sec:loc-cone-proof]],
whose old text is this item's and whose new text is the merged text for both sections; no separate change.

*7. [[app:standard-results]], [[sec:std-characteristic]].* Insert before [[thm:std-ctg-neighbourhood]] (line 467), with
one blank line after each item; this defines thm:std-cctw-existence and thm:std-cctw-strips. New:

**Theorem {#thm:std-cctw-existence}** ([CCTW16, (2.1)–(2.2), p. 6; (2.7)–(2.9), p. 7; (3.2), p. 11; Theorem 3.9, pp.
32–33].) The authors consider "quasi-linear first order symmetric hyperbolic systems of the form Lf = G, (2.1) on
subsets of M̃ := {u ∈ [0, ∞), v ∈ [0, ∞), y ∈ Y}. (2.2) In (2.1), f is assumed to be a section of a real vector bundle
over M̃, equipped with a scalar product, similarly for G. … Both the scalar product and the connection coefficients are
allowed to depend upon f, and we assume that ∇ is compatible with ⟨·, ·⟩. … L is a first order operator of the form L =
A^μ∇_μ, where the A^μ's are self-adjoint, and are smooth functions of f and of the space-time coordinates" (p. 6), with
G = G(f, ·) (p. 11); here Y is "a (n − 1)-dimensional compact manifold without boundary" and ∇̊ "a fixed, arbitrarily
chosen, smooth connection which is f, u, and v–independent" (p. 6). They "specialise to f's which are of the form f =
(ϕ, ψ), (2.7) with A^v and A^u satisfying A^u = (A^u_ϕϕ, 0; 0, 0), A^v = (0, 0; 0, A^v_ψψ), and A^v_ψψ > 0, A^u_ϕϕ > 0.
(2.8) It is further assumed that the connections ∇ and ∇̊ preserve the splitting (2.7). We will write G = (G_ϕ, G_ψ).
(2.9)" (p. 7). With N₋ = {0} × [0, b0] × Y and N₊ = [0, a0] × {0} × Y (p. 32), a bar denoting restriction to N₋ ∪ N₊
(p. 11), Theorem 3.9 reads: "Let Y be a (n − 1)−dimensional compact manifold without boundary, let a0 and b0 two
positive real numbers and set Ω0 = [0, a0] × [0, b0] × Y Consider the symmetric hyperbolic system (2.1) on Ω0 with the
splitting (2.7) and assume that (2.8) holds. Let ϕ̄ and ψ̄ be defined respectively on N₋ and N₊, providing Cauchy data
for (2.1): ϕ = ϕ̄ on N₋, ψ = ψ̄ on N₊. (3.98) Let ℓ ∈ ℕ, ℓ > (n + 9)/2 and suppose that ϕ̄ ∈ ∩_(0≤j≤ℓ) C^j([0, b0];
H^(ℓ−j)(Y)) and ψ̄ ∈ ∩_(0≤j≤ℓ) C^j([0, a0]; H^(ℓ−j)(Y)). (3.99) Assume that the transport equations A^μ_ϕϕ|_(v=0)
∂_μϕ|_(v=0) = (−A^μ_ϕψ ∂_μψ + G_ϕ)|_(v=0), (3.100) A^μ_ψψ|_(u=0) ∂_μψ|_(u=0) = (−A^μ_ψϕ ∂_μϕ + G_ψ)|_(u=0), (3.101)
with initial data ϕ|_(u=v=0) = ϕ̄|_(v=0) and ψ|_(u=v=0) = ψ̄|_(u=0), have a global solution on ([0, a0] × Y) ∪ ([0, b0]
× Y). Then there exists an ℓ-independent constant a* ∈ (0, a0] such that the Cauchy problem (2.1), (3.98) has a
solution f defined on [0, a*] × [0, b0] × Y satisfying (3.88)-(3.90) with k = ℓ − 1. … The solution f is unique within
the class of C¹ solutions, and is smooth if ϕ̄ and ψ̄ are." The omitted sentence states further regularity for ℓ > (n +
12)/2.

**Theorem {#thm:std-cctw-strips}** ([CCTW16, Corollary 3.11, p. 35].) "Under the hypotheses of Theorem 3.9, there
exists two constants 0 < a* ≤ a0 and 0 < b* ≤ b0 and a unique solution f of the Cauchy problem (2.1), (3.98) defined on
the neighborhood ([0, a*] × [0, b0] × Y) ∪ ([0, a0] × [0, b*] × Y) of N = N₊ ∪ N₋ such that f ∈ L^∞([0, a*] × [0, b0];
H^(ℓ−2)(Y)) ∩ ⋂_(0<3i≤ℓ−(n+9)/2) W^(i,∞)([0, a*] × [0, b0]; H^(ℓ−1−3i)(Y)) similarly on [0, a0] × [0, b*]." The
corollary follows from Theorem 3.9 by "the symmetry of the problem under the interchange of u and v" (p. 35). Theorem
3.9 applied to the system with u and v exchanged therefore also gives that f is smooth on [0, a0] × [0, b*] × Y when ϕ̄
and ψ̄ are smooth; on the overlap of the two strips the two solutions agree, by the uniqueness in Theorem 3.9.

*8. The references, [CCTW16] (lines 26–28).* The publisher's page gives volume 515 and pages 1–67; the page numbers
cited in the edition are those of arXiv:1406.3009v2, as the appendix states for all arXiv versions. Old:

- [CCTW16] A. Cabet, P. T. Chruściel, R. Tagne Wafo, *On the characteristic initial value problem for nonlinear
  symmetric hyperbolic systems, including Einstein equations*, Dissertationes Math. (2016), 1–72.
  doi:10.4064/dm732-7-2015 arXiv:1406.3009v2

New:

- [CCTW16] A. Cabet, P. T. Chruściel, R. Tagne Wafo, *On the characteristic initial value problem for nonlinear
  symmetric hyperbolic systems, including Einstein equations*, Dissertationes Math. 515 (2016), 1–67.
  doi:10.4064/dm732-7-2015 arXiv:1406.3009v2

*9. No change.* [[ch:two-dusts]], [[ch:class-system]], [[ch:vlasov]] and [[ch:ten-l5]] need no change: no result there
uses the cone developments, and the section uses only results those chapters state. The crosswalk of
[[ch:localised-data]] receives one row for each label listed in item 1, and that of [[app:standard-results]] one row
each for thm:std-cctw-existence and thm:std-cctw-strips.
