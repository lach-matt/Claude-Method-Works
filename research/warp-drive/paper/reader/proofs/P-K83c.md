<!-- Proofs for chapter 83 (ch:localised-data). Block 1 closes the marker pending:class-domain-of-dependence in the
proof of thm:loc-bent-slice (c); Blocks 2 and 3 are the matching changes to the statement (c) and to the end of its
proof. Block 4 settles item m4 of the first reading (the cone development for data with null dust). Blocks 5 and 6
concern [Rac16, (4.21)]: Block 6 is the Appendix A entry (chapter 95), Block 5 a small change in the proof of
thm:loc-bent-slice (b). Old
texts are quoted from chapters 83 and 95 as they stand; they contain no label definition, so each occurs once. The
blocks use only results that the edition states. -->

<!-- Block 1. Item 1. Chapter 81 does not give this by itself. def:class-adapted concerns admissible domains, whose
slices are annuli, and lateral boundaries adapted to a family; the domain-of-dependence argument inside the proof of
thm:class-stability is made for the adapted domain only, and it compares two solutions of the augmented system with
the cut-offs of that proof, whose non-local zones near the axes are not saturated by the leaves for the regions needed
here. lem:class-volterra supplies one ingredient, the uniqueness of the leaf issued from an axis point, and
lem:class-leaf-differences (b) another. The lemma below proves the needed uniqueness on non-annular regions near an
axis, by an energy estimate on a region whose three lateral pieces are spacelike. Insert it after the end of the proof
of thm:loc-bent-slice (the line ending "3.25 × 10⁻⁴ < 3.3 × 10⁻⁴ for ε small. ∎", which Block 3 replaces) and before
rem:loc-band-grid. Its statement fixes the constant 3.3 × 10⁻⁴ of thm:loc-bent-slice (c); the causal-curve argument
of the old paragraph "The angular widening" is no longer needed and Block 3 removes it. New labels:
lem:loc-lens-dependence, eq:loc-lens-region, eq:loc-lens-shear. -->

**Lemma {#lem:loc-lens-dependence}** (Dependence across the lens.) Let Ω_L, t and δ1 be as in the proof of
[[thm:loc-bent-slice]] (c), and let (g, u_A, q_A) be the development constructed there. Let 3.3 × 10⁻⁴ < α < π/2, and
let the data of [[thm:loc-bent-slice]] (b), the metric and second fundamental form and the densities of all families,
equal the background's at the points of Σ′ with 3.44 ≤ R ≤ 5.85 and ϑ < α. Then for ε small, depending also on α, at
every point of the lens with ϑ < α − 3.3 × 10⁻⁴ the metric g and its first derivatives equal those of g0, the
differential of the ingoing family's phase equals the background's, and every density equals the background's. The
same holds, for 0 < β < π/2 − 3.3 × 10⁻⁴, with ϑ > β and ϑ > β + 3.3 × 10⁻⁴ in place of ϑ < α and
ϑ < α − 3.3 × 10⁻⁴.

*Proof.* We prove the first statement; the second is proved in the same way, with axis 1 in place of axis 2.

*Notation.* By [[thm:class-stability]] the development solves [[eq:class-system]] on Ω_L in the gauge D(g) = 0 relative
to g0, and its norm 𝒩_k of [[eq:class-energy]] is at most Cε. Fix k ≥ 6 and apply that theorem with k + 2 in place of
k: the data are ε-close in C^∞, and by its uniqueness the development is the same. Let u_in be the development's phase
of the ingoing family, with the sign of [[sec:class-augmented]], so that P := g⁻¹p, p := du_in, is future directed;
put v_in := −u_in, Θ := □_g u_in and let q be the ingoing density. Then v_in = v̂ on Σ′, by (b), and the derivatives of
v_in − v̂ of order at most k − 1 are at most Cε on Ω_L. For the background write ů_in := −v̂, p̊, P̊, Θ̊ and q̊. Put
M := 0.0011596, t1 := M/(δ1 + M), W := 1.015 (δ1 + M)/3.5756 (3.5756 = 3.5 × 1.0216), α′ := α − 4 × 10⁻⁷,
c_a := τ0 + 3.44, c_b := τ0 + 5.85, λ := 0.05, and

    𝒟 := {y ∈ Ω_L : t ≤ t1, ϑ ≤ α′ − W t, c_a + λ t ≤ v_in ≤ c_b − λ t}.                       {#eq:loc-lens-region}

Then W t1 = 1.015 M/3.5756 ≤ 3.2918 × 10⁻⁴, and on 𝒟, ϑ ≤ α′ < π/2 and on its angular face ϑ ≥ α − 3.2958 × 10⁻⁴ > 0.

(1) *Where 𝒟 lies.* On Ω_L, τ = τ0 + (1 − t)φ(R) + tδ1 and −M ≤ φ ≤ 0 ([[prop:margins-bend]] (b)); so on 𝒟,
−M ≤ τ − τ0 ≤ tδ1 ≤ t1δ1 < M, and as |v_in − v̂| ≤ Cε, R = v̂ − τ satisfies

    3.44 + t(λ − δ1) − Cε ≤ R ≤ 5.85 + M + Cε < 5.86.

Every point of 𝒟 lies in region I. Where τ ≤ τ0 this is [[lem:margins-region-one]] (c), as R ≥ 3.4399 > R_*. Where
τ > τ0, the ray u = 5.7 is {τ = τ_ray(R)} with dτ_ray/dR = 2/f − 1 ≥ 1 ([[lem:margins-region-one]] (b), (c), its time
v̂ ≤ τ0 + M + 3.4384 < v̂(v = 3) there), so it meets the slice {τ = const} at a radius at most R_* + (τ − τ0), which is
at most 3.43719 + tδ1 < 3.44 + t(λ − δ1) − Cε, since λ ≥ 2δ1; and u decreases strictly in R along that slice (proof of
[[cor:class-two-dust]]), so u < 5.7 at the points of 𝒟. Hence on 𝒟, by [[lem:margins-region-one]] (a),

    g0 = −f dτ² + 2(1 − f) dτ dR + (2 − f) dR² + R² dΩ₃²,      f = 1 − μ/R²,      3/2 ≤ μ ≤ 3.6059,

so 0.69 < f ≤ 1 − 1.5/5.86² ≤ 0.95632; the inverse has g0^(ττ) = −(2 − f), g0^(τR) = 1 − f, g0^(RR) = f,
g0^(ϑϑ) = R⁻² and no other entry pairing dϑ with dτ or dR. The background's outgoing density vanishes on 𝒟, as ℬ = 0
in region I. 𝒟 lies in the interior of Ω_L, since R > 0.70, v̂ + τ = 2τ + R < 2τ0 + 6 and t1 < 1. On 𝒟 the coordinate
field ∂_t of the chart (t, x) is (δ1 − φ)∂_τ, with g0(∂_τ, ∂_τ) = −f < 0 and dτ(∂_τ) = 1: it is future timelike, for g
as well when ε is small.

A point y of the lens with ϑ(y) < α − 3.3 × 10⁻⁴ lies in 𝒟. Indeed τ(y) ≤ τ0 gives t(y) ≤ |φ|/(δ1 + |φ|) ≤ t1, so
ϑ(y) < α′ − 3.2958 × 10⁻⁴ ≤ α′ − W t(y); and v̂(y) = τ + R lies in [τ0 + 3.5 − M, τ0 + 5.75], so c_a + λ t(y) ≤ τ0 +
3.49 < v_in(y) < τ0 + 5.8 ≤ c_b − λ t(y) for ε small.

(2) *The lateral faces.* 𝒟 = {y ∈ Ω_L : t ≤ t1, F_1 ≤ 0, F_2 ≤ 0, F_3 ≤ 0} with F_1 := ϑ + W t − α′, F_2 := c_a + λ t −
v_in and F_3 := v_in + λ t − c_b. We show that at the points of 𝒟 each dF_i is timelike for g and positive on the
nonzero future causal vectors of g. A covector positive on these is timelike: otherwise its kernel would contain a
nonzero causal vector. As in the proof of [[thm:loc-bent-slice]] (c), dt = η/(δ1 − φ) with η := dτ − κ dR,
κ := (1 − t)φ′, |κ| ≤ 0.0021370 ([[prop:margins-bend]] (c)), δ1 − φ ≤ δ1 + M ≤ 0.0111596, and

    −g0⁻¹(η, η) = (2 − f) + 2κ(1 − f) − κ²f ≥ 1.0216²:

where φ′ ≠ 0, so 3.5 < R < 5.75, the left side is at least 1 + 1.5/5.75² − 2 × 0.002137 × 3.6059/3.5² − 0.002137² ≥
1.04410; elsewhere it is 2 − f = 1 + μ/R² ≥ 1 + 1.5/5.86² ≥ 1.04368; and 1.0216² ≤ 1.04367. A nonzero future causal
vector Y of g0 has τ̇ := dτ(Y) > 0 and x := dR(Y)/τ̇ between the roots −1 and f/(2 − f) of (2 − f)x² + 2(1 − f)x − f,
so that η(Y) = τ̇(1 − κx) ≥ (1 − |κ|)τ̇ and dv̂(Y) = (1 + x)τ̇ ≤ 2τ̇/(2 − f).

For F_1: since g0⁻¹(dϑ, dϑ) = R⁻² and g0⁻¹(dϑ, η) = 0,

    g0⁻¹(dF_1, dF_1) = R⁻² + (W/(δ1 − φ))² g0⁻¹(η, η) ≤ R⁻² − (1.0216 W/(δ1 − φ))².

Where R ≥ 3.5, 1.0216 W/(δ1 − φ) ≥ 1.015/3.5 ≥ 1.015/R; where R < 3.5, φ = 0 and 1.0216 W/δ1 = 1.015 (1 + M/δ1)/3.5 ≥
0.3236 ≥ 1.1/R, as δ1 ≤ 0.01 and R ≥ 3.43. So g0⁻¹(dF_1, dF_1) ≤ −0.03 R⁻², and dF_1(∂_t) = W > 0. For F_2: dv̂(Y) ≤
1.9164 τ̇ ≤ 1.9205 η(Y), while λ dt(Y) = λ η(Y)/(δ1 − φ) ≥ 4.48 η(Y); so (λ dt − dv̂)(Y) ≥ 2.5 η(Y) > 0. These bounds
for F_1 and F_2 are strict, uniformly on the compact 𝒟, and g − g0 and dv_in − dv̂ are at most Cε there; so for ε small
they hold for g and v_in. For F_3: dF_3 = dv_in + λ dt, where dv_in is null for g and dv_in(Y) = −g(P, Y) ≥ 0 for future
causal Y; so dF_3 is positive on the nonzero future causal vectors, dt being so.

Consequently a past directed causal curve γ of g that starts in 𝒟 stays in 𝒟 while t > 0. Let y = γ(s*) be its last
point with γ([0, s*]) ⊂ 𝒟, and suppose t(y) > 0. Along γ, t decreases, so t ≤ t1 continues to hold; the F_i negative
at y stay negative near s*; and each F_i with F_i(y) = 0 has derivative dF_i(γ̇) < 0 there, γ̇ being past directed.
So γ(s) ∈ 𝒟 for s a little beyond s* (𝒟 lying in the interior of Ω_L), against the choice of s*.

(3) *Only the ingoing family carries dust in 𝒟.* The background has no further families, and its outgoing density
vanishes on 𝒟 by (1). For the development, let A be the outgoing family or a further one and y ∈ 𝒟. The integral curve
of P_A through y, followed to the past, is a past directed causal curve of g along which t decreases at a rate bounded
below on the compact Ω_L; by (2) it stays in 𝒟 until it reaches a point y0 of 𝒟 ∩ Σ′. On Σ′, v̂ = τ0 + R + φ(R)
increases with R and equals c_a at R = 3.44 and c_b at R = 5.85, where φ = 0; so y0 has 3.44 ≤ R ≤ 5.85 and ϑ ≤ α′ < α,
and q_A(y0) is the background's, 0. The conservation law of [[eq:class-system]] reads P_A(q_A) = −(□_g u_A) q_A, a
linear ordinary differential equation along the curve; so q_A(y) = 0. On 𝒟 the stress of either solution is therefore
that of its ingoing family alone.

(4) *The equations compared.* On 𝒟 both (g, u_in, q) and (g0, ů_in, q̊) satisfy, by [[eq:class-system]], the gauge
condition and (3):

(i) Ric^H(g) = q p ⊗ p, Ric^H the reduced Ricci tensor relative to g0 ([[eq:gauge]]);
(ii) P^b ∂_b p_a = P^b Γ[g]^c_ba p_c, as ∇_P p = ½ d g⁻¹(p, p) = 0;
(iii) P(Θ) = −|∇²u_in|²_g, which is [[eq:class-raychaudhuri]] with Ric(P, P) = q g⁻¹(p, p)² = 0;
(iv) P(q) = −Θ q.

In (iii), by [[eq:class-identity]], |∇²u_in|² = S_loc := (Θ − κ1 − κ2)² + κ1² + κ2² off the axes, and by
[[eq:class-x]] and continuity ([[prop:class-axis]] (d)), |∇²u_in|² = S_ax := κ1² + ½(Θ − κ1)² + ½σ² near axis 2,
where σ is the planar shear of the level sets of u_in in the slices {t = s}. Fix δ := 1/2 and the points p_i of axis 2
in a slice with ρ1(p_i) = 3.4, 3.8, …, 5.8; then δ ≤ ρ1(p_i)/4, and [[lem:class-leaf-differences]], for the background
and the ingoing family, holds near each p_i, with balls 𝔅, 𝔅′ and a constant C common to these points and to
0 ≤ s ≤ t1. Let χ_Z be a G-invariant function of ρ2 equal to 1 for ρ2 ≤ 1/8 and to 0 for ρ2 ≥ 1/4. Then |∇²u_in|² = χ_Z S_ax + (1 − χ_Z) S_loc on 𝒟. Where χ_Z ≠ 1, S_loc is a smooth
function of (g, ∂g, p, Θ), since there g(K2, K2) ≥ c and, ϑ ≤ α′ < π/2 on 𝒟, g(K1, K1) ≥ c(α′) > 0 (proof of
[[prop:class-augmented]] (a)); where χ_Z ≠ 0, S_ax is a smooth function of (g, ∂g, p, Θ, σ), κ1 being smooth near
axis 2.

Put w := g − g0 and 𝔡 := (w, ∂_t w, ∂_x w, p − p̊, Θ − Θ̊, q − q̊). Write (i) in the first-order form of Step 9 of the
proof of [[thm:class-stability-off-axes]], in the chart (t, x), with the difference of the principal parts taken as
in Step 4 there, ½(g^(ab) − g0^(ab)) ∂_a ∂_b g0, and (ii)–(iv) as transports along P. Subtracting the background's
equations from the development's gives on 𝒟 a linear system 𝐀^0 ∂_t 𝔡 + 𝐀^j ∂_j 𝔡 = F_𝔡, with 𝐀^0 = diag(1, −g^(tt),
g^(ab)) on the wave block and P^t on the transports, 𝐀^j its other matrices, all symmetric and evaluated at the
development, and with F_𝔡 bounded at every point of 𝒟 by C |𝔡| + C χ_Z |σ − σ̊|, σ̊ the background's: C bounds the
derivatives of the smooth functions concerned on the compact 𝒟, where both solutions are smooth. On 𝒟, dt is timelike and ∂_t future timelike for g; so −g^(tt) > 0, g^(ab), the restriction of
g⁻¹ to the covectors vanishing on ∂_t, is positive definite, P^t = dt(P) > 0, and 𝐀^0 ≥ c0 I with c0 > 0.

(5) *𝔡 vanishes on 𝒟 ∩ Σ′.* The development's datum on Σ′ is built at each point from the constraint data, the
background's lapse and shift and the gauge condition D(g) = 0 solved for the transversal derivatives ([[thm:data]]);
its ingoing phase on Σ′ is −v̂ by (b); p is fixed on Σ′ by its spatial part and g⁻¹(p, p) = 0; and Θ = □_g u_in on Σ′
is computed from g, ∂g, the derivatives of u_in along Σ′ and the transversal derivative of p that (ii) gives. All of
these equal the background's at the points of Σ′ with 3.44 < R < 5.85 and ϑ < α, by hypothesis, hence on the closure
of that set, which contains 𝒟 ∩ Σ′.

(6) *The planar shear.* Let 𝒟_s := 𝒟 ∩ {t = s}, a subset of the x-space. We show that, for 0 ≤ s ≤ t1,

    ‖χ_Z (σ − σ̊)‖_(L²(𝒟_s)) ≤ C ‖𝔡(s)‖_(L²(𝒟_s)).                                            {#eq:loc-lens-shear}

*The leaves stay in 𝒟_s.* Let y ∈ 𝒟_s with ρ2(y) ≤ 1/4. On M3 := {t = s, φ1 = 0} use the coordinates (z, y′) :=
(ρ1, x3, x4) of [[lem:class-leaf]] and r := |y′| = ρ2; there R = (z² + r²)^(1/2) and z ≥ 3.39. On the slice, v̂ is a
function V(R) := τ0 + (1 − s)φ(R) + sδ1 + R with 0.997 ≤ V′ ≤ 1.003 and |V″| ≤ 0.01, so ∂_z v̂ = V′z/R ≥ 0.98 and
∂_r² v̂ = V″r²/R² + V′z²/R³ ≤ 0.31 for r ≤ 1/2; v_in differs from v̂ by Cε in C². So, near the axis, the level set
{v_in = v_in(y)} of the slice meets M3 in a graph z = h(r), 0 ≤ r ≤ 1/4. As v_in is invariant, ∂_r v_in vanishes at
r = 0, so |h′(r)| = |∂_r v_in/∂_z v_in| ≤ r sup |∂_r² v_in|/0.97 ≤ r. Then tan ϑ = r/h(r) has the derivative
(h − rh′)/h² > 0, since rh′ ≤ r² < h. So along the leaf from the axis to y, ϑ increases and v_in is constant: the arc
{(h(r), r) : 0 ≤ r ≤ ρ2(y)}, with its images under G, lies in 𝒟_s.

*An extension.* The map Φ_s(x) := (v_in(s, x), x/|x|) is a G-equivariant diffeomorphism of a neighbourhood of 𝒟_s onto
its image in R × S³, under which 𝒟_s is [c_a + λs, c_b − λs] × {ϑ ≤ α′ − Ws}; at s = 0, v_in = v̂. Let A_s be the
affine map of [c_a, c_b] onto [c_a + λs, c_b − λs], and m_s the flow on S³, for the time Ws, of a G-invariant vector
field equal to −∂_ϑ on {α′ − W t1 ≤ ϑ ≤ α′} and to 0 near the axes. Then ψ_s := Φ_s⁻¹ ∘ (A_s × m_s) ∘ Φ_0 is a
G-equivariant diffeomorphism near 𝒟_0, C¹-close to the identity, with ψ_s(𝒟_0) = 𝒟_s, whose derivatives of order at
most k − 1, and those of its inverse, are bounded independently of s and of ε by the bound on v_in − v̂; we extend it
to a diffeomorphism of R⁴ equal to the identity outside a compact set. 𝒟_0 = Σ′ ∩ {3.44 ≤ R ≤ 5.85, ϑ ≤ α′} is a
bounded Lipschitz domain of the x-space. Let E be its extension operator of [[thm:std-sy-extension]] and 𝔼_s f the
average over G of (E(f ∘ ψ_s)) ∘ ψ_s⁻¹. By [[thm:std-sy-extension]] and [[thm:std-ly-extension]] (Lemma 27 there),
𝔼_s is bounded on L² and on H^(k−1), with a bound C_E depending on α but not on s or ε; and 𝔼_s f = f on 𝒟_s for
invariant f, 𝒟_s being invariant.

*The bound.* Let U be the development's state (g, ∂g, p, Θ, q) on 𝒟_s, with Θ = □_g u_in, ů the background's state on
the slice, which the background defines on the sets 𝒰_2δ(p_i) as well, and Ŭ := ů + 𝔼_s 𝔡(s). Then Ŭ = U on 𝒟_s, and
the distance of Ŭ from ů in the norm 𝒩_(k−1) is at most C_E ‖𝔡(s)‖_(H^(k−1)(𝒟_s)) ≤ C_E C ε; so Ŭ lies in the ball 𝔅′
of [[lem:class-leaf-differences]] for ε small, depending also on α. Let y ∈ 𝒟_s with ρ2(y) ≤ 1/4 and let h be the
level set of u_in through y found above, issued from the axis point (h(0), 0). As Θ = □_g u_in, H_L[Θ] is the mean
curvature of the leaf (step (1) of the proof of [[lem:class-planar-shear]]), so h solves [[eq:class-leaf-volterra]]
for U on [0, ρ2(y)] ([[lem:class-leaf]] (c)). That equation uses U only along the arc of h, where Ŭ = U together with
∂g; so h solves it for Ŭ, and by the uniqueness in [[lem:class-volterra]] the leaf of Ŭ issued from (h(0), 0) is h on
[0, ρ2(y)]: it is the leaf of Ŭ through y. The planar shear at y is determined by h and h′ at ρ2(y), by H_L there,
which fixes h″ through the leaf equation, and by the values of Ŭ = U and the 1-jet of γ3 at y
([[eq:class-shear-leaf]]); so σ[Ŭ](y) = σ(y), and likewise σ[ů] = σ̊. The sets 𝒰_δ(p_i) cover {ρ2 ≤ 1/4} ∩ 𝒟_s, where
3.39 ≤ ρ1 ≤ 5.86, and [[lem:class-leaf-differences]] (b) gives

    ‖χ_Z (σ − σ̊)‖_(L²(𝒟_s)) ≤ Σ_i ‖σ[Ŭ] − σ[ů]‖_(L²(𝒰_δ(p_i))) ≤ C Σ_i ‖Ŭ − ů‖_(L²(𝒰_2δ(p_i)))
                              ≤ C C_E ‖𝔡(s)‖_(L²(𝒟_s)),

which is [[eq:loc-lens-shear]].

(7) *The energy.* For 0 ≤ s ≤ t1 put e(s) := ∫_(𝒟_s) ⟨𝐀^0 𝔡, 𝔡⟩ dx. On 𝒟 away from the axes, dt, dv_in and dϑ are
independent: in the coordinates (t, R) the differential of v̂ is (δ1 − φ) dt + (1 + (1 − t)φ′) dR. So the faces
{F_i = 0} meet one another and the slices transversally, and 𝒟 ∩ {t ≤ s} is a Lipschitz domain, bounded by 𝒟_0, 𝒟_s
and pieces of the faces. The field (⟨𝐀^μ 𝔡, 𝔡⟩)_μ is smooth, with divergence ⟨(∂_μ 𝐀^μ) 𝔡, 𝔡⟩ + 2⟨F_𝔡, 𝔡⟩ by the
symmetry of the 𝐀^μ, and the divergence theorem on 𝒟 ∩ {t ≤ s}, as in the proof of [[thm:class-kato]] (b) (i), gives

    e(s) + ∫ ⟨(ν_μ 𝐀^μ) 𝔡, 𝔡⟩ |ν|⁻¹ dS = e(0) + ∫_0^s ∫_(𝒟_s′) (⟨(∂_μ 𝐀^μ) 𝔡, 𝔡⟩ + 2⟨F_𝔡, 𝔡⟩) dx ds′,

the middle integral taken over the pieces of the faces, ν being a positive multiple of dF_i on {F_i = 0}. By (2) and
(1), ν_t = ν(∂_t) > 0, g⁻¹(ν, ν) < 0 and ν(P) > 0 there; so the boundary matrix is nonnegative, on the wave block by
Step 9 of the proof of [[thm:class-stability-off-axes]] and on the transports, where it is ν(P). We drop that
integral. e(0) = 0 by (5). By the bound on F_𝔡 in (4) and by [[eq:loc-lens-shear]], the right side is at most
C ∫_0^s ‖𝔡(s′)‖²_(L²(𝒟_s′)) ds′ ≤ (C/c0) ∫_0^s e. By Gronwall's inequality e = 0, so 𝔡 = 0 on 𝒟. With (1) and (3) this
is the first statement.

For the second, use 𝒟 := {y ∈ Ω_L : t ≤ t1, ϑ ≥ β + 4 × 10⁻⁷ + W t, c_a + λ t ≤ v_in ≤ c_b − λ t}, the face function
β + 4 × 10⁻⁷ + W t − ϑ, whose differential has the norm and the sign of dF_1, axis 1 in place of axis 2, the
coordinates (ρ2, x1, x2) of M3 := {t = s, φ2 = 0}, and the results of [[sec:class-planar-shear]] at axis 1, where they
hold with the two planes exchanged and the same proofs. ∎

<!-- Block 2. Replaces statement (c) of thm:loc-bent-slice in chapter 83. Old text, exactly:

(c) The development of these data across the lens between Σ′ and Σ_τ0 exists and induces on Σ_τ0 constraint data
equal to the background's outside the domain of influence of 𝒫; on Σ_τ0 the angular support is wider than on Σ′ by at
most 3.3 × 10⁻⁴ rad.

New text: -->

(c) The development of these data across the lens between Σ′ and Σ_τ0 exists, and the constraint data it induces on
Σ_τ0 are those of (b) for R ∉ (3.5, 5.75), where Σ_τ0 = Σ′. Let 0 ≤ α ≤ β ≤ π/2, with α < π/2 and β > 0, be such
that every point of the domain of influence of 𝒫 in (b) with 3.44 ≤ R ≤ 5.85 has α ≤ ϑ ≤ β. Then for ε small,
depending also on α and β, the data induced on Σ_τ0 equal the background's at the points with 3.5 < R < 5.75 and
ϑ < α − 3.3 × 10⁻⁴ or ϑ > β + 3.3 × 10⁻⁴: across the lens the angular support widens by at most 3.3 × 10⁻⁴ rad on
each side.

<!-- The domain of influence of (b) is the complement of the union of the sets Ω of cor:class-kato-sphere (c) on which
P = P̄; that condition involves P̄, ū and r0 only, so the domain, and α and β with it, do not depend on ε. This is
why "ε small, depending also on α and β" is a legitimate order of choice. What is no longer claimed, compared with
the old wording: inside the lens, localisation in R, and the gaps between the components of the angular support
(only its smallest closed interval [α, β] is used); outside the lens the data are those of (b), so nothing is lost
there. The paragraph after the theorem ("So data localised in an angle exist ...") stands unchanged. -->

<!-- Block 3. Replaces the end of the proof of (c) in chapter 83, from the second sentence of the paragraph "The
development." to the end of the proof. Old text, exactly:

and Σ_τ0 = Σ′ elsewhere, it induces constraint data on the whole of Σ_τ0. The development equals the background's
outside the domain of influence of 𝒫 by the uniqueness of class Einstein–null-dust developments on domains of
dependence [[pending:class-domain-of-dependence]].

*The angular widening.* The development's metric g is within Cε of g0 in C⁰ on Ω_L. The proof of [[cor:margins-lens]]
uses of g0, on the lens, only that dτ and d(τ − φ) are timelike, which holds for g when ε is small, and the bound
R²|Ω̇|² ≤ τ̇²/(2 − f) for causal vectors, which for g holds with τ̇²/(2 − f) replaced by (1 + Cε)τ̇²/(2 − f), the
quadratic form of g differing from that of g0 by at most Cε(τ̇² + Ṙ² + R²|Ω̇|²); and Σ_τ0 is acausal for g, τ increasing
along its causal curves. So a causal curve of g joining Σ′ to Σ_τ0 has angular displacement at most (1 + Cε)^(1/2) ×
3.25 × 10⁻⁴ < 3.3 × 10⁻⁴ for ε small. ∎

New text: -->

and Σ_τ0 = Σ′ elsewhere, it induces constraint data on the whole of Σ_τ0; for R ∉ (3.5, 5.75) these are the data of
(b), which the development attains on Σ′.

*Localisation across the lens.* At a point of Σ_τ0 the induced metric and second fundamental form, and the matter
part ℋ/2 and ℳ of [[eq:loc-constraints]], are computed from g and its first derivatives and from the differentials of
the phases and the densities at that point. Let α and β be as in (c). By the last statement of (b), the data of (b)
equal the background's at the points of Σ′ with 3.44 ≤ R ≤ 5.85 and ϑ < α, and at those with 3.44 ≤ R ≤ 5.85 and
ϑ > β. If α > 3.3 × 10⁻⁴, [[lem:loc-lens-dependence]] below gives, for ε small, depending also on α, that g with its
first derivatives, the differential of the ingoing phase and every density equal the background's at the points of
the lens with ϑ < α − 3.3 × 10⁻⁴; if α ≤ 3.3 × 10⁻⁴ there are no such points. The same holds for ϑ > β + 3.3 × 10⁻⁴.
At these points of Σ_τ0 the induced data are therefore the background's. ∎

<!-- Block 4. Item m4 of the first reading of chapter 83: the cone development for data with null dust. Neither route
closes it.

(a) No published theorem covers it. Each candidate was read at its source. [Ren90] (Rendall, Proc. R. Soc. Lond. A 427
(1990), 221–239) proves well-posedness of the characteristic problem "for the Einstein equations in vacuum or with
perfect fluid source" (abstract); null dust is not a perfect fluid, its stress q du ⊗ du having a null eigenvector.
Luk's theorem (Int. Math. Res. Not. 2012, 4625–4678) is the neighbourhood theorem "for the vacuum Einstein equations
in four space-time dimensions" ([CCTW16, p. 5]). [CCTW16], Section 5.2, pp. 56–57, treats sources whose matter
fields satisfy wave equations, its (5.24)–(5.25), in four space-time dimensions; the density of a null dust obeys a transport
equation that loses a derivative (chapter 81, the discussion after def:class-system). The closest result, Luk and
Rodnianski, "High-frequency limits and null dust shell solutions in general relativity", arXiv 2009.08968, Theorem 4.6,
p. 28, gives local existence and uniqueness for the Einstein-null-dust system with two families of null dust moving
along a double null foliation, which is the structure of the background's two dusts, but on M = [0, u_*] × [0, u̲_*] ×
S²: in 3 + 1 dimensions only. The present cones are five-dimensional with S³ sections, so it does not apply. [CTG23]
is a vacuum theorem.

(b) A proof in this edition is out of reach of a block: it would need a characteristic existence theory for the class
Einstein-null-dust system near the two cones, in five dimensions, with the derivative loss of the dust handled at the
axes as chapter 81 handles it for the Cauchy problem; chapter 81's Cauchy theory does not reduce to it without a
reduction of Rendall's type, which itself needs domain-of-dependence results across null boundaries for that system.

(c) The narrowest true statement is the one the chapter already makes: cone data with dust exist by
prop:loc-cones; a development is asserted only for dust-free data, by [CTG23, Theorem 1.1]. What is lost: every
spacetime statement about cone data that carry dust, among them every perturbation of the shell (𝒞_out, 3 < v < 4.5)
or of the packet (𝒞_in, 5.7 < u < 7.2) and every density added in the band. Nothing else in the edition uses a
development of cone data: prop:loc-cones is cited only in the opening paragraph of chapter 83, for the existence of the
data. The replacement below only makes the loss explicit; the present text is already true. It replaces, in the
paragraph after the proof of prop:loc-cones, the last sentence. Old text, exactly:

sphere. [CTG23, Theorem 1.1] concerns vacuum data only, and for cone data that carry dust no development is asserted
here.

New text: -->

sphere. [CTG23, Theorem 1.1] concerns vacuum data only. For cone data that carry dust, among them every perturbation
of the shell on 𝒞_out ∩ {3 < v < 4.5} or of the packet on 𝒞_in ∩ {5.7 < u < 7.2} and every density added in the band,
no development is asserted here: [[prop:loc-cones]] gives the cone data only, and no result of this paper uses their
development.

<!-- Block 5. Proof of thm:loc-bent-slice (b) in chapter 83: what it uses of [Rac16, (4.21)] matches the source (Block
6): H is rational in k, K^E_E, κ and γ̂ with powers of κ as its only denominators, symmetric, positive definite exactly
where κK^E_E < 0, and HB^(K) is symmetric there. The change below only points to the place where positivity is shown.
Old text, exactly (two whole lines):

graph of (ū, P̄) it is a smooth function of (ρ, ω, u, P), symmetric, positive definite at ū, and HB^(K) is
symmetric. With t := R2 − ρ the system reads ∂_tu − B^(K)∂_Ku − C = 0, which is [[eq:class-kato-sphere]] with n =

New text (three lines; the next line of the chapter, beginning "3, A^0 := H,", follows unchanged): -->

graph of (ū, P̄) it is a smooth function of (ρ, ω, u, P), symmetric, positive definite at ū, where κK^E_E < 0
([[thm:std-racz-hyperbolic]]), and HB^(K) is symmetric. With t := R2 − ρ the system reads ∂_tu − B^(K)∂_Ku − C = 0,
which is [[eq:class-kato-sphere]] with n =

<!-- Block 6. Item 3, the Appendix A entry (chapter 95). Source: I. Rácz, Constraints as evolutionary systems, arXiv
1508.01810v3, page 12 (printed page number 12), equations (4.20) and (4.21), the sentence after (4.21), and footnote
6; read from the arXiv text of that version, and every symbol of (4.20) and (4.21) checked against the author's
typeset formulas. The consequence drawn at the end (the block form and its Schur complement) was checked for n = 3, 4, 5 with
generic entries; the leaves of chapter 83 have n = 4. Two changes to thm:std-racz-hyperbolic.

First, its opening. Old text, exactly:

([Rac16, Lemma 4.1, p. 12; Theorem 4.3, p. 14].) In the notation of [Rac16,
Sections 3–4]: the slice Σ is foliated by the level surfaces S_ρ; κ is given algebraically by (4.17); and (4.16) and
(3.2) are the evolution equations for (k_i, K^l_l) in ρ.

New text: -->

([Rac16, (4.20), (4.21) and Lemma 4.1, p. 12; Theorem 4.3, p. 14].) In the
notation of [Rac16, Sections 3–4]: the slice Σ is foliated by the level surfaces S_ρ; κ is given algebraically by
(4.17); and (4.16) and (3.2) are the evolution equations for (k_i, K^l_l) in ρ.

<!-- Second, a new paragraph after that opening and before the paragraph "Lemma 4.1: ...". New text: -->

Written as (4.19) ([[rem:std-racz-characteristic]]), with u = (k_B, K^E_E)ᵀ, the system has "the coefficients B^(K) of
∂_K, with K = 2, 3, …, n," given by

    B^(K)_ij = −N̂^K δ_ij − N̂ γ̂^(KL) δ_in δ_j(L−1) + (κ N̂/K^E_E) δ_i(K−1) δ_jn
               − 2 (N̂ k_L/K^E_E) γ̂^(LM) δ_i(K−1) δ_(j+1)M,   (4.20)

"where the lowercase and uppercase Latin indices take the value 1, 2, …, n and 2, 3, …, n, respectively"; with a
common symmetrizer as defined in [[rem:std-racz-characteristic]], "It may be verified by a direct calculation that the
matrix of the form

    H_ij = δ_in δ_jn − (2/κ) k_P γ̂^(PQ) [δ_in δ_(j+1)Q + δ_(i+1)Q δ_jn] +
           (1/κ²) [4 (k_P γ̂^(PQ) δ_(i+1)Q) (k_S γ̂^(ST) δ_(j+1)T) − κ · K^E_E γ̂^(PQ) δ_(i+1)P δ_(j+1)Q]   (4.21)

is indeed a common symmetrizer to (4.19) in a subset of Σ where neither κ nor K^l_l vanishes and in which they are of
opposite sign." By footnote 6 (p. 12), "in evaluating a term of the form δ_(j+1)M, here and also in (4.21), one needs
to refer to the (n + 1)-dimensional Kronecker delta"; so u_i = k_(i+1) for i < n and u_n = K^E_E. With a^Q := k_P
γ̂^(PQ), H has the entry 1 at (n, n), the entries −2a^(j+1)/κ elsewhere in the last row and column, and the block
(4a^(i+1)a^(j+1) − κK^E_E γ̂^((i+1)(j+1)))/κ² for i, j < n. Subtracting from that block the product of the last column
with the last row leaves −(K^E_E/κ) γ̂^((i+1)(j+1)), and γ̂ is positive definite; so H is positive definite exactly
where κK^E_E < 0. H is a rational function of k_P, K^E_E, κ and γ̂ whose only denominators are powers of κ.
