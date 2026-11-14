## Setting {#ch:setting}

This chapter fixes the symmetry class, the background, the domain, the gauge, the profiles and their norms, and the
waves. Every identity is derived in full.

### The class and the reduction {#sec:class}

Let g5 be a Lorentzian metric on a five-manifold, invariant under an effective T² action and under both reflections
of its orbits. Invariance under each reflection removes the cross terms, so locally

    g5 = g3 + e^(2A) dφ1² + e^(2B) dφ2²,                                                          {#eq:class-metric}

with g3 a Lorentzian metric and A, B functions on the three-dimensional orbit space. On R⁴ = R² × R² we write
G := O(2) × O(2), acting by the rotations of the two planes and the reflections x2 ↦ −x2, x4 ↦ −x4; the class is the
class of G-invariant metrics, and we call it the T²-mirror class.

**Lemma {#lem:warped-ricci}** (Ricci tensor of the class). Let a, b, … be indices on the orbit space, ∇ and □ the
connection and wave operator of g3, and write R11, R22 for the φ1φ1 and φ2φ2 components of Ric[g5]. Then

    Ric[g5]_ab = Ric[g3]_ab − ∇_a∇_b A − ∂_aA ∂_bA − ∇_a∇_b B − ∂_aB ∂_bB,
    R11 = −e^(2A) (□A + |dA|² + ⟨dA, dB⟩),      R22 = −e^(2B) (□B + |dB|² + ⟨dA, dB⟩),

with |·| and ⟨·,·⟩ taken in g3, and the components Ric[g5]_(aφi) and Ric[g5]_(φ1φ2) vanish identically.

*Proof.* The mixed components vanish because the reflection φi ↦ −φi is an isometry of g5 that changes the sign of
every component with exactly one index φi. Since A and B do not depend on φ1, φ2, the Christoffel symbols of g5 are
those of g3 on the orbit space together with

    Γ^a_(φ1φ1) = −e^(2A) ∇^aA,   Γ^(φ1)_(aφ1) = ∂_aA,   Γ^a_(φ2φ2) = −e^(2B) ∇^aB,   Γ^(φ2)_(aφ2) = ∂_aB,

all others vanishing. We use R_bd = ∂_μΓ^μ_bd − ∂_dΓ^μ_bμ + Γ^μ_μνΓ^ν_bd − Γ^μ_dνΓ^ν_bμ. For b, d on the orbit
space, Γ^μ_bμ = Γ^a_ba + ∂_bA + ∂_bB and Γ^μ_μe = Γ^a_ae + ∂_eA + ∂_eB, while the φ-indices add to Γ^μ_dνΓ^ν_bμ
exactly ∂_dA ∂_bA + ∂_dB ∂_bB. Hence R_bd = Ric[g3]_bd − ∂_b∂_dA + Γ^e_bd ∂_eA − ∂_b∂_dB + Γ^e_bd ∂_eB − ∂_bA ∂_dA −
∂_bB ∂_dB, which is the first formula. For R11, the terms are ∂_aΓ^a_(φ1φ1) = −∂_a(e^(2A)∇^aA), then
Γ^μ_μaΓ^a_(φ1φ1) = −(Γ^b_ba + ∂_aA + ∂_aB) e^(2A)∇^aA, and Γ^μ_(φ1ν)Γ^ν_(φ1μ) = 2 Γ^(φ1)_(φ1a)Γ^a_(φ1φ1) =
−2 e^(2A)|dA|²; the term ∂_(φ1)Γ^μ_(φ1μ) is zero. Summing,
R11 = −e^(2A)(2|dA|² + ∇_a∇^aA + |dA|² + ⟨dA, dB⟩ − 2|dA|²), which is the second formula; R22 is the same with A
and B exchanged. ∎

**Lemma {#lem:conformal}** (conformal change in three dimensions). Let g be a metric on a three-manifold, ψ a
function and h := e^(2ψ) g. Then, with ∇ and □ those of g,

    Ric[h] = Ric[g] − ∇∇ψ + dψ ⊗ dψ − (□ψ + |dψ|²) g,      □_h u = e^(−2ψ) (□u + ⟨dψ, du⟩).

*Proof.* Let m be the dimension. The difference of the connections is C^a_bc = δ^a_b ∂_cψ + δ^a_c ∂_bψ − g_bc ∇^aψ,
and Ric[h]_bc − Ric[g]_bc = ∇_aC^a_bc − ∇_cC^a_ba + C^a_adC^d_bc − C^a_cdC^d_ba. Here C^a_ba = m ∂_bψ, so
∇_aC^a_bc = 2∇_b∇_cψ − g_bc □ψ, ∇_cC^a_ba = m ∇_b∇_cψ and C^a_adC^d_bc = m (2 ∂_bψ∂_cψ − g_bc|dψ|²). Expanding
the nine products in C^a_cdC^d_ba gives (m + 2) ∂_bψ∂_cψ − 2 g_bc|dψ|². Altogether

    Ric[h] − Ric[g] = −(m − 2)(∇∇ψ − dψ ⊗ dψ) − (□ψ + (m − 2)|dψ|²) g.

For the wave operator, □_h u = h^(bc)(∇_b∇_c u − C^a_bc ∂_a u) = e^(−2ψ)(□u + (m − 2)⟨dψ, du⟩), because
g^(bc)C^a_bc = (2 − m)∇^aψ. Put m = 3. ∎

**Proposition {#prop:reduction}** (the reduction). Put ψ := A + B, ω := (B − A)/2 and h := e^(2ψ) g3. Then

    Ric[h]_ab = Ric[g5]_ab + (3/2) ∂_aψ ∂_bψ + 2 ∂_aω ∂_bω + (e^(−2A) R11 + e^(−2B) R22) (g3)_ab,
    e^(2ψ) □_h ψ = −(e^(−2A) R11 + e^(−2B) R22),      e^(2ψ) □_h ω = (e^(−2A) R11 − e^(−2B) R22)/2.

Hence g5 is vacuum if and only if

    Ric[h] = (3/2) dψ² + 2 dω²,      □_h ψ = 0,      □_h ω = 0.                                     {#eq:reduced}

*Proof.* By [[lem:warped-ricci]], e^(−2A) R11 + e^(−2B) R22 = −(□ψ + |dψ|²), since |dA|² + |dB|² +
2⟨dA, dB⟩ = |dψ|²; and e^(−2A) R11 − e^(−2B) R22 = □(B − A) + ⟨d(B − A), dψ⟩ = 2(□ω + ⟨dψ, dω⟩). Since A = (ψ − 2ω)/2 and
B = (ψ + 2ω)/2, dA ⊗ dA + dB ⊗ dB = (1/2) dψ ⊗ dψ + 2 dω ⊗ dω, so [[lem:warped-ricci]] reads
Ric[g3] = Ric[g5] + ∇∇ψ + (1/2) dψ² + 2 dω². By [[lem:conformal]],

    Ric[h] = Ric[g5] + ∇∇ψ + (1/2) dψ² + 2 dω² − ∇∇ψ + dψ² − (□ψ + |dψ|²) g3,

which is the first formula, and e^(2ψ) □_h u = □u + ⟨dψ, du⟩ gives the other two. If g5 is vacuum, all three
right-hand sides reduce to (3/2) dψ² + 2 dω² and 0. Conversely, if (3/2) dψ² + 2 dω² = Ric[h] and both waves vanish,
then e^(−2A) R11 ± e^(−2B) R22 = 0, so R11 = R22 = 0, then Ric[g5]_ab = 0, and the mixed components vanish by
[[lem:warped-ricci]]. ∎

With ψ̃ := (√3/2) ψ, [[eq:reduced]] reads Ric[h] = 2 (dψ̃² + dω²), □_h ψ̃ = □_h ω = 0: Huneau and Luk's system [HL18]
(1.3), quoted in [[ch:introduction]], with the scalar φ replaced by the pair (ψ̃, ω), whose target is the flat Euclidean
plane.

### The background {#sec:background}

We use coordinates X = (τ, x) ∈ R × R⁴, r = |x|, x̂ = x/r, v := τ + r, and on R⁴ the coordinates

    x1 + i x2 = r cos ϑ e^(iφ1),      x3 + i x4 = r sin ϑ e^(iφ2),      ϑ ∈ [0, π/2],

in which the flat metric is dr² + r² (dϑ² + c² dφ1² + s² dφ2²), c := cos ϑ, s := sin ϑ. The polar angle is ϑ; the
letter θ is reserved for the phase. The T² action rotates the planes (x1, x2) and (x3, x4); its axes {c = 0} and
{s = 0} are regular points of R⁴, and every tensor below is an array of Cartesian components. Let

    g0 := η + (μ(v)/r²) dv ⊗ dv,   g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0,   L0 := ∂_τ − x̂·∂_x,   det g0 = −1,    {#eq:background}

with μ smooth and nondecreasing, μ = μ0 > 0 for v ≤ v_start and μ constant for v ≥ v_end; we write
μ_end := μ(v_end). The inverse and the determinant hold because dv = dτ + x̂·dx satisfies η⁻¹(dv, dv) = 0 and
η⁻¹dv = −L0: for a rank-one change by a covector null for η, the inverse changes by the opposite rank-one term and
the determinant does not change. We write □̃ := g0^(ab) ∂_a ∂_b acting on each Cartesian component, and ∂_r := x̂·∂_x.

In the coordinates (v, r, ϑ, φ1, φ2), with γ := dϑ² + c² dφ1² + s² dφ2² the round metric of S³, the background is

    g0 = −f dv² + 2 dv dr + r² γ,      f := 1 − μ(v)/r²,                                            {#eq:vr-form}

since −(dv − dr)² + dr² = −dv² + 2 dv dr. Its inverse has g^(vv) = 0, g^(vr) = 1, g^(rr) = f, g^(ij) = r⁻² γ^(ij)
on S³.

**Lemma {#lem:vr-curvature}** (curvature of the (v, r) form). Let f = f(v, r) be any smooth function and
g = −f dv² + 2 dv dr + r² γ, with i, j, k, l indices on S³. The nonzero Christoffel symbols are

    Γ^v_vv = f_r/2,  Γ^r_vv = (f f_r − f_v)/2,  Γ^r_vr = −f_r/2,  Γ^v_ij = −r γ_ij,  Γ^r_ij = −r f γ_ij,
    Γ^i_rj = δ^i_j / r,  Γ^i_jk = Γ[γ]^i_jk,

and the nonzero components of the Riemann tensor, up to its symmetries, are

    R_vrvr = f_rr/2,   R_vivj = (r/2)(f f_r − f_v) γ_ij,   R_virj = −(r/2) f_r γ_ij,
    R_ijkl = r² (1 − f)(γ_ik γ_jl − γ_il γ_jk).

Consequently

    Ric_vv = (f/2)(f_rr + 3 f_r/r) − 3 f_v/(2r),   Ric_vr = −(1/2)(f_rr + 3 f_r/r),   Ric_rr = 0,
    Ric_ij = (2(1 − f) − r f_r) γ_ij,   Ric_vi = Ric_ri = 0,

and the Kretschmann scalar 𝒦 is

    𝒦 = R_abcd R^abcd = f_rr² + 6 f_r²/r² + 12 (1 − f)²/r⁴,                                       {#eq:kretschmann-f}

in which f_v does not appear.

*Proof.* The Christoffel symbols follow from Γ_(c,ab) = (∂_a g_bc + ∂_b g_ac − ∂_c g_ab)/2 and the inverse above:
the only nonzero lowered symbols with no index on S³ are Γ_(r,vv) = f_r/2, Γ_(v,vv) = −f_v/2 and Γ_(v,vr) = −f_r/2,
and those with indices on S³ are Γ_(r,ij) = −r γ_ij, Γ_(j,ri) = r γ_ij and Γ[r² γ]_(k,ij); raising with g^(vr) = 1,
g^(rr) = f, g^(ij) = r⁻² γ^(ij) gives the list.

The isometries of γ act on g by isometries fixing v and r, and the isotropy group of a point of S³ is O(3), acting on
its tangent space; it contains reflections. An O(3)-invariant tensor on R³ of odd rank vanishes, and one of rank two
is a multiple of the metric. So, with A, B, C ∈ {v, r}, every component with an odd number of indices on S³ vanishes,
R_ABij vanishes (it is a multiple of γ_ij and antisymmetric in i, j), R_AiBj = r S_AB γ_ij for some S_AB, and the
components with four indices on S³ are determined by R^i_jkl, computed below. We use
R^a_bcd = ∂_cΓ^a_bd − ∂_dΓ^a_bc + Γ^a_ceΓ^e_bd − Γ^a_deΓ^e_bc and R_abcd = g_ae R^e_bcd.
Since Γ^v_rr = Γ^v_vr = Γ^r_rr = 0 and Γ^v_re = 0 for every e,

    R^v_rvr = 0,   R^r_rvr = −∂_rΓ^r_vr − Γ^r_rvΓ^v_vr = f_rr/2,   so R_vrvr = g_vr R^r_rvr = f_rr/2.

For the mixed components,

    R^v_irj = ∂_rΓ^v_ij − Γ^v_jkΓ^k_ir = −γ_ij + γ_ij = 0,
    R^r_irj = ∂_rΓ^r_ij + Γ^r_rvΓ^v_ij − Γ^r_jkΓ^k_ir = −(f + r f_r) γ_ij + (r f_r/2) γ_ij + f γ_ij = −(r/2) f_r γ_ij,
    R^v_ivj = Γ^v_vvΓ^v_ij = −(r/2) f_r γ_ij,
    R^r_ivj = ∂_vΓ^r_ij + Γ^r_vvΓ^v_ij + Γ^r_vrΓ^r_ij = (−r f_v − (r/2)(f f_r − f_v) + (r/2) f f_r) γ_ij
            = −(r/2) f_v γ_ij,

so R_virj = g_vr R^r_irj = −(r/2) f_r γ_ij, R_rirj = g_rv R^v_irj = 0, and R_vivj = g_vv R^v_ivj + g_vr R^r_ivj =
(r/2)(f f_r − f_v) γ_ij. On the spheres, the only
Christoffel symbols with an upper index on S³ and a lower index v or r are Γ^i_rj = δ^i_j/r, so

    R^i_jkl = R[γ]^i_jkl + Γ^i_krΓ^r_jl − Γ^i_lrΓ^r_jk = (δ^i_k γ_jl − δ^i_l γ_jk) − f (δ^i_k γ_jl − δ^i_l γ_jk),

using R[γ]^i_jkl = δ^i_k γ_jl − δ^i_l γ_jk on the unit sphere; lowering with r² γ gives R_ijkl. The Ricci components
are the contractions Ric_bd = g^(ac) R_abcd, with g^(vv) = 0, g^(vr) = 1, g^(rr) = f; for instance
Ric_vv = f R_rvrv + r⁻² γ^(ij) R_ivjv = (f/2) f_rr + (3/(2r))(f f_r − f_v), and
Ric_ij = g^(vr)(R_virj + R_rivj) + r⁻² γ^(kl) R_kilj = −r f_r γ_ij + 2(1 − f) γ_ij.

For 𝒦, group the components by their index pairs. The pair (vr) contributes 4 R_vrvr R^vrvr; raising the
antisymmetric pair (vr) with the (v, r) block of g⁻¹, [[0, 1], [1, f]], multiplies by its determinant −1, twice, so
the contribution is 4 (f_rr/2)² = f_rr². The components R_AiBj, A, B ∈ {v, r}, are r S_AB γ_ij with
S_vv = (f f_r − f_v)/2, S_vr = S_rv = −f_r/2 and S_rr = 0. Counting the four orderings of each pair, they contribute
4 r² r⁻⁴ (γ^(ij)γ_ij) tr((g2⁻¹ S)²), g2⁻¹ the (v, r) block of the inverse. Now

    g2⁻¹ S = [[0, 1], [1, f]] [[S_vv, S_vr], [S_vr, 0]] = [[S_vr, 0], [S_vv + f S_vr, S_vr]]

is triangular, so tr((g2⁻¹ S)²) = 2 S_vr² = f_r²/2, and S_vv, the only entry that contains f_v, drops out. With
γ^(ij)γ_ij = 3 this gives 6 f_r²/r². The components R_ijkl are those of a three-sphere of radius r times the
factor 1 − f, and contribute (1 − f)² r⁻⁴ · 2·3·2 = 12 (1 − f)²/r⁴. There are no other nonzero components. ∎

**Proposition {#prop:vaidya}** (the background).
(a) g0 is five-dimensional Vaidya: Ric(g0) = (3 μ'(v)/(2 r³)) dv ⊗ dv, and its (τ, r) block has determinant −1.
(b) The Kretschmann scalar is 𝒦 = 72 μ(v)²/r⁸, also where μ' ≠ 0; the round spheres {v, r = const} have exactly
one apparent horizon, r = √μ(v).
(c) ℓ := g0⁻¹ dv = −L0 is null and geodesic, with L0(v) = 0, L0(τ) = 1, L0(r) = −1; the phase v is an exact eikonal
of g0 and its level sets are the ingoing null cones.
(d) g0⁻¹(dτ, dτ) = −1 − μ/r², g0⁻¹(dr, dr) = 1 − μ/r², g0⁻¹(dr, dτ) = μ/r², g0⁻¹(d(v + τ), d(v + τ)) =
−3 − μ/r²; the slices {τ = const} are spacelike everywhere, and the lines of constant x are spacelike where r² < μ.
(e) For every function u,

    [L0, □̃] u = (2/r)(□̃ u + (∂_τ + ∂_r) L0 u) − (3/r²) ∂_r u,                                     {#eq:commutator}

the mass dropping out.
(f) H0^ρ := g0^(ab) Γ[g0]^ρ_ab = (−μ/r³, μ x^i/r⁴), smooth on r > 0.

*Proof.* (a) In the form [[eq:vr-form]], f = 1 − μ/r², so f_v = −μ'/r², f_r = 2μ/r³ and f_rr = −6μ/r⁴. Then
f_rr + 3 f_r/r = 0 and 2(1 − f) − r f_r = 0, so by [[lem:vr-curvature]] the only nonzero Ricci component is
Ric_vv = −3 f_v/(2r) = 3μ'/(2r³). In the coordinates (τ, r) the block is [[−1 + m, m], [m, 1 + m]], m := μ/r², of
determinant (m − 1)(m + 1) − m² = −1.

(b) By [[eq:kretschmann-f]], 𝒦 = 36 μ²/r⁸ + 6 · 4μ²/r⁸ + 12 μ²/r⁸ = 72 μ²/r⁸, for every μ(v). For the spheres
S_(v,r) := {v, r = const}, the null normals lie in the span of ∂_v and ∂_r of the (v, r) form; ∂_r is null, and
n⁺ := ∂_v + (f/2) ∂_r is null. We time-orient g0 by dτ, which is timelike by (d): a causal vector Y is future directed
when dτ(Y) > 0. In Cartesian terms ∂_r of the (v, r) form is ℓ = −∂_τ + x̂·∂_x = −L0, and ∂_v is ∂_τ; so −∂_r = L0 is
future directed, since L0(τ) = 1, and n⁺ is future directed, since dτ(n⁺) = 1 − f/2 = (1 + μ/r²)/2 > 0. The expansion
of a normal N of S_(v,r) is (3/r) N(r), so the future ingoing normal −∂_r has expansion −3/r and the future outgoing
normal n⁺ has expansion 3f/(2r). Normalised by n(τ) = 1, that is divided by dτ(n⁺) = (1 + μ/r²)/2, the outgoing
expansion is

    θ⁺ = (2r²/(r² + μ)) · 3(1 − μ/r²)/(2r),

whose one zero, r = √μ, is simple; the spheres with r < √μ are trapped and those with r > √μ untrapped.

(c) η⁻¹dv = −∂_τ + x̂·∂_x = −L0, and L0(v) = 0, so ℓ = η⁻¹dv − (μ/r²) L0(v) L0 = −L0. Then
g0⁻¹(dv, dv) = dv(ℓ) = −L0(v) = 0: v is an exact eikonal. A gradient field of a function whose gradient is null
is geodesic: ℓ^a ∇_a ∇_b v = ℓ^a ∇_b ∇_a v = (1/2) ∂_b (g0⁻¹(dv, dv)) = 0. The values L0(τ) = 1 and
L0(r) = −x̂·x̂ = −1 are immediate.

(d) Contract g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 with L0(τ) = 1, L0(r) = −1, L0(v + τ) = 1; for instance
η⁻¹(2dτ + dr, 2dτ + dr) = −4 + 1. The covector dτ is timelike, so the slices are spacelike, and
g0(∂_τ, ∂_τ) = −1 + μ/r² because dv(∂_τ) = 1.

(e) Write g0^(ab) = η^(ab) − m L0^a L0^b, m = μ/r². Then

    [L0, □̃] u = (L0 g0^(ab)) ∂_a∂_b u − 2 g0^(ab) (∂_a L0^c) ∂_b∂_c u − g0^(ab) (∂_a∂_b L0^c) ∂_c u.

First, L0(L0^c) = 0, since L0^i = −x^i/r and x̂^j ∂_j(x^i/r) = 0; and L0(m) = μ'(v) L0(v)/r² + 2μ/r³ = 2μ/r³.
So L0 g0^(ab) = −(2μ/r³) L0^a L0^b, and L0^a L0^b ∂_a∂_b u = L0 L0 u. Second, ∂_j L0^i = −(δ_ij − x̂_i x̂_j)/r and
L0^j ∂_j L0^i = 0, so g0^(ab)(∂_a L0^c) ∂_b∂_c u = −(1/r)(Δu − ∂_r²u), Δ the flat Laplacian of R⁴, using
x̂_i x̂_j ∂_i∂_j u = ∂_r² u. Third, L0^a L0^b ∂_a∂_b L0^c = L0(L0(L0^c)) = 0, and in R⁴, Δ(x^i/r) = −3 x^i/r³, so
g0^(ab) ∂_a∂_b L0^i = 3 x^i/r³. Hence

    [L0, □̃] u = −(2μ/r³) L0 L0 u + (2/r)(Δu − ∂_r² u) − (3/r²) ∂_r u.

On the other side, □̃ u = −∂_τ² u + Δu − m L0 L0 u and (∂_τ + ∂_r)(∂_τ − ∂_r) u = ∂_τ² u − ∂_r² u, so
(2/r)(□̃ u + (∂_τ + ∂_r) L0 u) = (2/r)(Δu − ∂_r² u) − (2μ/r³) L0 L0 u, which is the same.

(f) Since det g0 = −1, g0^(ab) Γ[g0]^ρ_ab = −∂_a g0^(aρ) = ∂_a(m L0^a L0^ρ) = L0^ρ ∂_a(m L0^a), because
m L0^a ∂_a L0^ρ = m L0(L0^ρ) = 0 by the proof of (e). With
∂_i μ(v) = μ' x̂_i, ∂_a(m L0^a) = μ'/r² − μ'/r² − μ ∂_i(x^i/r³) = −μ/r³, because ∂_i(x^i/r³) = 4/r³ − 3/r³ in R⁴.
So H0^ρ = −(μ/r³) L0^ρ. ∎

The identity [[eq:commutator]] is the five-dimensional form of Touati's commutator lemma ([Tou23a] Lemma 3.1, p. 21,
which bounds [L0, □]f by ∂L0 f, □f and ∂f); here it is an exact identity.

### The curvature boundary and the domain {#sec:domain}

Fix a length l5 > 0 and put x_K := l5² √𝒦. By [[prop:vaidya]] (b), the surface x_K = 1 is r = r_q(v),

    r_q(v) := (√72 μ(v) l5²)^(1/4),

and r_q ≤ √μ, so that it lies inside or on the horizon, exactly when r_q⁴ = √72 μ l5² ≤ μ², that is when
μ ≥ √72 l5². The seed condition is μ0 ≥ √72 l5². Fix T > 0 and let

    D_T := { v ≤ v_end + T,  r ≥ r_q(v) },                                                          {#eq:dt}

the region from past null infinity to the curvature boundary, up to the time T after the shell has passed. Put
V := v_end + T and q0 := (√72 μ0 l5²)^(1/4), the value of r_q for v ≤ v_start, so q0 ≤ √μ0. Fix 0 < δ0 < q0,
a := q0 − δ0, τ0 with v_start − τ0 > √μ0 + 1 (on the slice {τ = τ0} the shell lies outside the seed's horizon: the
slice is before the shell reaches the hole), and τ_end := max_(v ≤ V) (v − r_q(v)). Let

    Ω := { τ0 ≤ τ ≤ τ_end,  |x| ≥ a,  v + (τ − τ_end) ≤ V + 1 },                                   {#eq:omega}

and Σ_τ := Ω ∩ {τ} = A(τ) := { a ≤ |x| ≤ b(τ) }, b(τ) := V + 1 − τ + (τ_end − τ). Ω is bounded by Σ_τ0, Σ_τ_end,
the inner sphere r = a and the outer surface {v + τ = V + 1 + τ_end}.

**Lemma {#lem:domain}** (the domain). (a) Each Σ_τ is spacelike: g0⁻¹(dτ, dτ) = −1 − μ/r².
(b) {r = a} is spacelike and r decreases along future causal curves near it: g0⁻¹(dr, dr) = 1 − μ/r² ≤
1 − μ0/a² < 0 and g0⁻¹(dr, dτ) = μ/r² > 0.
(c) {v + τ = const} is spacelike and v + τ increases along future causal curves: g0⁻¹(d(v + τ), d(v + τ)) =
−2 − (1 + μ/r²) < 0, g0⁻¹(dv, dτ) = −1.
(d) L0 is future null with L0(τ) = 1, L0(v) = 0, L0(r) = −1; the integral curve of L0 through any point of Ω,
followed to the past, stays in Ω and meets Σ_τ0.
(e) There is ε1 > 0 such that for every Lorentzian g with |g − g0| ≤ ε1 on Ω, J⁻(p; g) ∩ {τ ≥ τ0} lies in Ω for
every p in Ω, Σ_τ and the two lateral boundaries stay spacelike for g, and L0 is transverse to Σ_τ for every metric,
since L0(τ) = 1.
(f) b(τ) − a ≥ 1 + δ0, b ≤ b(τ0), and D_T ∩ {τ ≥ τ0} lies in Ω.

*Proof.* (a)–(c) are the contractions of g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 with L0(τ) = 1, L0(r) = −1, L0(v) = 0:
g0⁻¹(dτ, dτ) = −1 − μ/r², g0⁻¹(dr, dr) = 1 − μ/r², g0⁻¹(dr, dτ) = 0 − (μ/r²)(−1)(1), and g0⁻¹(dv, ·) = ℓ = −L0.
For (b): at r = a < q0 ≤ √μ0 ≤ √μ, dr and dτ are timelike with g0⁻¹(dr, dτ) > 0, so grad r lies in the cone
opposite to grad τ, which is past directed; hence grad r is future directed and dr(Y) = g0(grad r, Y) < 0 for future
causal Y. (c): dv(Y) = −g0(L0, Y) ≥ 0 and dτ(Y) > 0 for future causal Y. (d): along −L0, τ decreases, r increases
and v is fixed, so r ≥ a and v + (τ − τ_end) ≤ V + 1 are kept. (e): the strict inequalities in (a)–(c) and
L0(τ) = 1 are open conditions in g on the compact set Ω; a past causal curve from p cannot cross {r = a} or
{v + τ = const} outward, by (b) and (c), nor Σ_τ_end. (f): b decreases in τ, and b(τ_end) = V + 1 − τ_end =
min_(v ≤ V) (V − v + r_q(v)) + 1 ≥ q0 + 1; a point of D_T has v ≤ V, r ≥ r_q(v) ≥ q0 > a and τ = v − r ≤
v − r_q(v) ≤ τ_end, hence also v + (τ − τ_end) ≤ v ≤ V < V + 1. ∎

So every part of the boundary of Ω other than Σ_τ0 is spacelike with Ω to its past, and Ω is a domain of dependence
of Σ_τ0, for g0 and for every Lorentzian metric within ε1 of g0.

### The gauge {#sec:gauge}

The gauge is the wave-map gauge relative to g0 itself. For a Lorentzian metric g put

    D^ρ(g) := g^(ab) (Γ[g]^ρ_ab − Γ[g0]^ρ_ab),
    Ric^H(g)_mn := Ric(g)_mn − (1/2)(g_mρ ∇̂_n D^ρ + g_nρ ∇̂_m D^ρ)
                 = −(1/2) g^(ab) ∂_a ∂_b g_mn + Q_mn(X; g)(∂g, ∂g),                                  {#eq:gauge}

∇̂ the connection of g0. In n + 1 dimensions, with H = D and D̂ = ∇̂, Choquet-Bruhat, Chruściel and Martín-García
give ([CBCM10] (2.7)–(2.9), p. 8) "R_(αβ) = R^(H)_(αβ) + 1/2 (g_(αλ) D̂_β H^λ + g_(βλ) D̂_α H^λ)" and
"R^(H)_(αβ) = −1/2 g^(λμ) D̂_λ D̂_μ g_(αβ) + f̂[g, D̂g]_(αβ)", with f̂ "independent of the second derivatives of g".
In the coordinates of [[sec:background]], D̂_a D̂_b g − ∂_a ∂_b g is Γ[g0] and its first derivatives times (g, ∂g),
which gives the second line of [[eq:gauge]]: Q is a quadratic polynomial in ∂g, with a linear and a constant part, whose
coefficients are rational in g and smooth in X through Γ[g0] and its first derivatives, hence smooth on r > 0; the
trace g0^(ab) Γ[g0]^ρ_ab is H0 of [[prop:vaidya]] (f). Second derivatives of g enter [[eq:gauge]] only through
−(1/2) g^(ab) ∂_a ∂_b g.

D is a vector field and Ric^H a tensor, built from g and g0 alone, so both are invariant under the isometries of g0,
which include O(4) acting on x and so contain G, and they may be computed in any coordinates. D(g0) = 0, so Ric^H(g0) =
Ric(g0), which is not zero; this is why Q needs a constant part. Ric^H(g) = 0 is a quasilinear wave system, and a
solution with D = 0 is vacuum.

### Profiles and scaled norms {#sec:profiles}

A *profile* is a smooth function or tensor f(X, θ) on Ω × S¹, S¹ = R/2πZ; we write [f](X) := f(X, v(X)/λ), and
⟨f⟩ for its θ-mean. The variable θ is the phase. For a function or tensor f on Σ_τ, with ∂^j all spacetime coordinate
derivatives of order j and ‖·‖ the flat L²(Σ_τ) norm, the λ-scaled norm is

    |f|_j := Σ_(i≤j) λ^i ‖∂^i f‖.                                                                   {#eq:scaled-norm}

Chain rule: ∂_a [f] = λ⁻¹ (∂_a v)[∂_θ f] + [∂_a f], so |[f]|_j ≤ C_j sup_(i≤j) |∂^i_(X,θ) f|_(L^∞): the oscillation
costs nothing in the scaled norms; and ‖∂^i [f]‖_(L^∞) ≤ C λ^(−i).

For pointwise bounds on symmetric 2-tensors of Cartesian components, |·| is the Euclidean operator norm (the largest
absolute eigenvalue); for arrays of higher rank (|∂w|, |∂g|), |·| is the Frobenius norm, and ‖·‖ always integrates the
Euclidean sum of squares. Any other norm on arrays changes only constants.

The eigenvalues of g0 are explicit. In Cartesian components g0 = η + m U Uᵀ, with U the array of dv, |U|² = 2 and
m := μ/r². On the orthogonal complement of the span of (1, 0) and (0, x̂), g0 is the identity, and on that span it is
the matrix [[−1 + m, m], [m, 1 + m]], whose eigenvalues are m ± (m² + 1)^(1/2). So the eigenvalues of g0 are 1 (three
times), m + (m² + 1)^(1/2) and m − (m² + 1)^(1/2) < 0.

**Lemma {#lem:eigen}** (the margins of the boundaries). Restricted to ker dτ, to ker dr on {r = a}, and to
ker d(v + τ), the form g0 has least eigenvalues, relative to the Euclidean inner product on each subspace,

    1,      min(1, μ/a² − 1),      min(1, (3 + μ/r²)/5).

Hence [[lem:domain]] (e) holds for every ε1 ≤ 3/5 with ε1 < μ0/a² − 1, and every Lorentzian g with |g − g0| ≤ ε1 on Ω
is time-oriented by dτ. Where μ = μ0 on {r = a}, the Lorentzian metric g := g0 − (μ0/a² − 1) dτ ⊗ dτ
has |g − g0| = μ0/a² − 1 and makes {r = a} null.

*Proof.* On ker dτ, vectors (0, Y′), g0 = |Y′|² + (μ/r²)(x̂·Y′)², with eigenvalues 1 (three times) and 1 + μ/r². On
ker dr at r = a, vectors (Y⁰, Y′) with x̂·Y′ = 0, g0 = −(Y⁰)² + |Y′|² + (μ/a²)(Y⁰)² = (μ/a² − 1)(Y⁰)² + |Y′|². On
ker d(v + τ) = ker(2dτ + dr), write Y′ = Y′⊥ + s x̂ with x̂·Y′⊥ = 0; then Y⁰ = −s/2 and

    g0 = −s²/4 + |Y′⊥|² + s² + (μ/r²)(s/2)² = |Y′⊥|² + s² (3 + μ/r²)/4,

while the Euclidean norm squared of (Y⁰, Y′) is |Y′⊥|² + (5/4) s²; the ratio on the s-direction is (3 + μ/r²)/5 ≥ 3/5.

Let g be Lorentzian with |g − g0| ≤ ε on Ω, where ε ≤ 3/5 and ε < μ0/a² − 1, and put g₋ := g0 − ε I, I the
Euclidean identity. Then g ≥ g₋ as quadratic forms. The eigenvalues of g₋ are 1 − ε (three times),
m + (m² + 1)^(1/2) − ε > 0 and m − (m² + 1)^(1/2) − ε < 0, so g₋ is Lorentzian, and its nonzero causal vectors form
two convex cones, each the negative of the other. Subtracting ε I lowers each restricted eigenvalue by exactly ε, so
g₋ restricted to ker dτ, to ker dr at r = a and to ker d(v + τ) has least eigenvalues 1 − ε, min(1, μ/a² − 1) − ε and
min(1, (3 + μ/r²)/5) − ε, all positive: the first because ε ≤ 3/5 < 1; the second because moreover μ ≥ μ0, μ being
nondecreasing, and ε < μ0/a² − 1; the last because (3 + μ/r²)/5 > 3/5 ≥ ε. So dτ, dr (at r = a) and d(v + τ)
vanish on no nonzero g₋-causal vector, and each has one sign on each of the two cones. Every g0-causal vector is
g₋-causal, since g₋ ≤ g0; so the cone that contains the future causal vectors of g0 has dτ > 0, dr < 0 at r = a and
d(v + τ) > 0, by [[lem:domain]] (a)–(c). Every g-causal vector is g₋-causal, since g ≥ g₋. Hence dτ vanishes on no
nonzero g-causal vector, so g is time-oriented by dτ, and its future causal vectors, a convex set on which dτ > 0, lie
in that cone. So for g the hypersurfaces Σ_τ, {r = a} and {v + τ = const} are spacelike, g being bounded below by g₋,
which is positive definite on the three kernels; and along future causal curves of g, τ and v + τ increase and, at
r = a, r decreases. These are the properties (a)–(c) that the proof of [[lem:domain]] (e) uses, so (e) holds for g.

For the last claim, g0 − α dτ ⊗ dτ, α > 0, agrees with g0 on the four-dimensional subspace ker dτ, where g0 is
positive definite, and is ≤ g0, so it has exactly one negative eigenvalue and no zero one, and |α dτ ⊗ dτ| = α; on
ker dr at r = a it is ((μ0/a² − 1) − α)(Y⁰)² + |Y′|² where μ = μ0, degenerate at α = μ0/a² − 1. Such points exist: on
Σ_τ0, v = τ0 + a < v_start at r = a. ∎

[[lem:domain]] (e) is not the only requirement on ε1. The energy inequality of [[ch:inequalities]] needs ε1 < s0, where

    s0 := inf over Ω of g0's least absolute eigenvalue = (m*² + 1)^(1/2) − m*,   m* := sup_Ω μ/r² ≤ μ_end/a²,

since, by the eigenvalues of g0 found above, its least absolute eigenvalue at a point is (m² + 1)^(1/2) − m, which
decreases in m.

**Lemma {#lem:lorentz-margin}** (Lorentzian metrics near g0). Every symmetric g̃ with |g̃ − g0| ≤ ε1 < s0 on Ω is
Lorentzian with |g̃⁻¹| ≤ (s0 − ε1)⁻¹. For ε1 ≥ s0, at a point of Ω where μ/r² = m*, there are Lorentzian forms g̃
with |g̃ − g0| ≤ ε1 and |g̃⁻¹| arbitrarily large.

*Proof.* Every eigenvalue of g0 has absolute value at least s0, so |g̃ x| ≥ |g0 x| − |(g̃ − g0) x| ≥ (s0 − ε1)|x|,
which bounds |g̃⁻¹|. Moreover x·g̃ x ≥ (s0 − ε1)|x|² on the four-dimensional span of g0's eigenvectors with positive
eigenvalues, while e·g̃ e ≤ −s0 + ε1 < 0 for the unit eigenvector e of its negative eigenvalue; so g̃ has exactly one
negative eigenvalue, since a second non-positive direction would meet that span. This is Weyl's inequality in the case
used. For ε1 ≥ s0, at a point where m = m* (there is one, Ω being compact), let e be the unit eigenvector of g0 with
eigenvalue −s0 and put g̃_t := g0 + t s0 e eᵀ for t ∈ [0, 1): g̃_t is Lorentzian, within s0 ≤ ε1 of g0, and its
eigenvalue −(1 − t) s0 tends to 0, so |g̃_t⁻¹| is unbounded. ∎

Since μ/a² > 1 on {r = a}, s0 < 2^(1/2) − 1 < 3/5. From here on ε1 is one fixed number with

    0 < ε1 < min(s0, μ0/a² − 1),

so that both [[lem:eigen]] and [[lem:lorentz-margin]] apply to it.

At the numerical point of [[ch:lambda0]] (μ0 = 1, l5 = 1/10, a = δ0 = q0/2, A = 1, [v_start, v_end] = [1/2, 7/2],
∫ env² = 105/128, T = 1, τ0 = −2) the three thresholds are as follows. They use the envelope only through its support
and ∫ env², so they hold for every env ∈ C_c^∞([1/2, 7/2]) with ∫ env² = 105/128, an envelope that [[thm:main]]
admits (a nonzero smooth function supported in [1/2, 7/2], multiplied by a suitable constant, is one).

(i) μ0/a² − 1 > 12, so every ε1 ≤ 3/5 serves for [[lem:domain]] (e) there: q0⁸ = 72 μ0² l5⁴ = 9/1250, so
μ0/a² = 4/q0² = 4 (1250/9)^(1/4), and 1250/9 > 28561/256 = (13/4)⁴ gives μ0/a² > 13.

(ii) No ε1 ≥ 0.6013096 serves for [[lem:domain]] (e) there. On the outer boundary v = V + 1 + τ_end − τ ≥ V + 1 > v_end,
so μ = μ_end there, and r ≤ b(τ0), with equality at its corner with Σ_τ0; so the least value of (3 + μ/r²)/5 on it is
ε_out := (3 + μ_end/b(τ0)²)/5, attained at the corner. Here μ_end = 1 + (2/9)(105/128) = 227/192 and V = 9/2. With
q_end := (√72 μ_end l5²)^(1/4), the value of r_q at v = V, one has τ_end ≥ V − q_end, so b(τ0) = V + 1 + τ_end − 2τ0 ≥
14 − q_end. Since q_end⁸ = 72 μ_end² l5⁴ = 51529/5120000 = 0.0100642… is less than 0.5628⁸ = 0.0100654…,
q_end < 0.5628, b(τ0) > 13.4372 and ε_out < (3 + (227/192)/13.4372²)/5 = 0.60130959… < 0.6013096. Now let
ν := (1, −2x̂)/√5, a Euclidean unit vector field, ν ⊗ ν the tensor of Cartesian components ν_a ν_b, and
g := g0 − ε_out ν ⊗ ν, so that |g − g0| = ε_out. The vector ν lies in ker d(v + τ), being the case s = −2/√5 of the
proof of [[lem:eigen]], so g0(ν, ν) = (3 + m)/5, and g0(ν, (0, Y′⊥)) = 0 when x̂·Y′⊥ = 0. In the Euclidean orthonormal
basis of ker d(v + τ) formed by ν and three vectors (0, Y′⊥), g0 is diag((3 + m)/5, 1, 1, 1) and g is
diag((3 + m)/5 − ε_out, 1, 1, 1), which at the corner is diag(0, 1, 1, 1): the outer boundary is null for g there. And
g is Lorentzian on Ω. In the plane of the τ- and x̂-directions the Cartesian block of g0 is [[−1 + m, m], [m, 1 + m]],
with inverse [[−1 − m, m], [m, 1 − m]], so νᵀ g0⁻¹ ν = (3 − 9m)/5, and the rank-one determinant formula with
det g0 = −1 gives det g = det g0 (1 − ε_out νᵀ g0⁻¹ ν) = −(1 − ε_out (3 − 9m)/5) < 0, since ε_out < 1 and m > 0.
Since g is the identity on the three directions (0, Y′⊥), it has at least three positive eigenvalues, and, its
determinant being negative, exactly one negative one. So (e) fails for every ε1 ≥ ε_out, in particular for every
ε1 ≥ 0.6013096.

(iii) s0 lies between 0.030768559 and 0.030768560, so there ε1 < 0.0308. On the inner sphere of Σ_τ_end,
v = τ_end + a ≥ V − q_end + a > v_end, as V − v_end = 1 > q_end, so μ = μ_end there and m* = μ_end/a² =
(227/48)(1250/9)^(1/4). Since s0 = (m*² + 1)^(1/2) − m* is the positive root of s² + 2m* s = 1, a number x > 0 lies
below s0 exactly when x² + 2m* x < 1, that is when (24(1 − x²)/(227 x))⁴ > 1250/9 = 138.88888…; at x = 0.030768559 the
left side is 138.88889948…, larger, and at x = 0.030768560 it is 138.88888139…, smaller.

### The waves and their average {#sec:waves}

The waves are two polarizations a quarter turn apart, with amplitude A > 0, envelope env ∈ C_c^∞([v_start, v_end]),
angular profile

    h(ζ) := √(2/(1 + ζ²)),      ζ := cos 2ϑ,      c² = (1 + ζ)/2,      s² = (1 − ζ)/2,

on the orbit space, and phase v/λ. As profiles,

    F := λ A env(v) h(ζ) sin θ,      G := λ A env(v) h(ζ) cos θ,

and at past null infinity their free data are [F] and [G]. The leading wave is the profile

    λ W_TT := 2 r^(1/2) (c² p1 dφ1² + s² p2 dφ2² − (p1 + p2) dϑ²),
    p1 := (2c² G − s² F)/3,      p2 := (2s² F − c² G)/3.                                            {#eq:waves}

**Lemma {#lem:waves}** (the leading wave). (a) In Cartesian components,

    λ W_TT = 2 r^(−3/2) ( G (x1 dx2 − x2 dx1)²/r² + F (x3 dx4 − x4 dx3)²/r²
                          − ((c² G + s² F)/3) (|dx|² − (x̂·dx)²) ),

with c² = (x1² + x2²)/r², s² = (x3² + x4²)/r², ζ = c² − s². In particular W_TT is smooth on {r > 0} × S¹, both axes
included, and |W_TT| ≤ C A env r^(−3/2).
(b) W_TT has no dτ component and W_TT(L0, ·) = 0, so W_TT(ℓ, ·) = 0; it has no dv or dr component in the (v, r)
coordinates, and tr_(g0) W_TT = 0: the wave is transverse to ℓ and traceless on the spheres.
(c) Its g0-norm is |W_TT|²_(g0) = 8 r⁻³ λ⁻² (p1² + p1 p2 + p2²).

*Proof.* (a) Since γ = dϑ² + c² dφ1² + s² dφ2²,

    c² p1 dφ1² + s² p2 dφ2² − (p1 + p2) dϑ² = c²(2p1 + p2) dφ1² + s²(p1 + 2p2) dφ2² − (p1 + p2) γ,

and 2p1 + p2 = c² G, p1 + 2p2 = s² F, p1 + p2 = (c² G + s² F)/3. With ρ1² := x1² + x2² = r² c², ρ1² dφ1 =
x1 dx2 − x2 dx1, so r² c⁴ dφ1² = c² ρ1² dφ1² = (x1 dx2 − x2 dx1)²/r², and likewise r² s⁴ dφ2² = (x3 dx4 − x4 dx3)²/r²;
and r² γ = |dx|² − (x̂·dx)². This gives the formula. Each term is smooth on r > 0: c², s² and ζ are, h is smooth on
[−1, 1], env(v) is smooth with v = τ + r, and the quadratic forms in dx have coefficients bounded by r² (for instance
the Euclidean norm of (x1 dx2 − x2 dx1)² is ρ1² ≤ r²). (b) No term contains dτ. Contracting with x̂ gives
(x1 x2 − x2 x1)/r = 0 in the first two forms and x̂·dx − x̂·dx = 0 in the third, so W_TT(L0, ·) = 0. Since
g0⁻¹ = η⁻¹ − (μ/r²) L0 ⊗ L0 and W_TT(L0, L0) = 0, the g0-trace is the Euclidean trace of the spatial array, which is
2 r^(−3/2) λ⁻¹ (G c² + F s² − (c² G + s² F)) = 0, the traces of the three forms being ρ1²/r² = c², s² and 4 − 1 = 3.
(c) In the frame dϑ, c dφ1, s dφ2, orthonormal for γ, the bracket of [[eq:waves]] is diagonal with entries −(p1 + p2),
p1, p2; on the spheres of radius r, with g0 = r² γ there and W_TT transverse, the norm squared is
4 r λ⁻² r⁻⁴ (p1² + p2² + (p1 + p2)²) = 8 r⁻³ λ⁻² (p1² + p1 p2 + p2²). ∎

The next lemma computes the mean of the leading equation of the two-scale expansion of [[ch:approximant]]. For a
profile k, |k|²_(g0) := g0^(ac) g0^(bd) k_ab k_cd.

**Lemma {#lem:mean-leading}** (the averaged leading equation). Let g1, …, g_N be profiles, bounded with all their
derivatives on Ω × S¹, and g := g0 + λ[g1] + Σ_(j=2)^N λ^j [g_j]. Suppose (g1 − ⟨g1⟩)(ℓ, ·) = 0. Then, for λ small,
Ric^H(g) = [R⁽⁰⁾] + λ[R⁽¹⁾] + …, with no term of order λ⁻¹, and the θ-mean of the λ⁰ coefficient is

    ⟨R⁽⁰⁾⟩ = ( 3μ'/(2r³) − (1/4) ⟨|∂_θ g1|²_(g0)⟩ ) dv ⊗ dv.                                       {#eq:mean-leading}

*Proof.* Write k := ∂_θ g1, so k(ℓ, ·) = ∂_θ(g1(ℓ, ·)) = ∂_θ(⟨g1⟩(ℓ, ·)) = 0, and v_a := ∂_a v, so ℓ^a = g0^(ab) v_b
and v_a ℓ^a = 0. Let C := Γ[g] − Γ[g0], a tensor, so that

    Ric(g)_ab = Ric(g0)_ab + ∇̂_ρ C^ρ_ab − ∇̂_b C^ρ_aρ + C^ρ_ρσ C^σ_ab − C^ρ_bσ C^σ_aρ,
    C^ρ_ab = (1/2) g^(ρσ) (∇̂_a δg_bσ + ∇̂_b δg_aσ − ∇̂_σ δg_ab),   δg := g − g0.

By the chain rule, ∇̂_a [u] = λ⁻¹ v_a [∂_θ u] + [∇̂_a u], and g⁻¹ = g0⁻¹ + O(λ), so C = [C⁽⁰⁾] + λ[C⁽¹⁾] + … with

    C⁽⁰⁾ρ_ab = (1/2)(v_a k_b^ρ + v_b k_a^ρ − ℓ^ρ k_ab),

indices raised by g0. Every term of C⁽⁰⁾ is linear in k, and ⟨k⟩ = 0, so ⟨C⁽⁰⁾⟩ = 0. Using k(ℓ, ·) = 0 and
v·ℓ = 0: v_ρ C⁽⁰⁾ρ_ab = 0, C⁽⁰⁾ρ_ρσ = (1/2) v_σ tr k, and so C⁽⁰⁾ρ_ρσ C⁽⁰⁾σ_ab = (1/2) tr k · v_σ C⁽⁰⁾σ_ab = 0.
Expanding C⁽⁰⁾ρ_bσ C⁽⁰⁾σ_aρ into nine products, every product but v_b v_a k_σ^ρ k_ρ^σ contains k(ℓ, ·) or v·ℓ, so

    C⁽⁰⁾ρ_bσ C⁽⁰⁾σ_aρ = (1/4) v_a v_b |k|²_(g0).

The λ⁰ coefficient of ∇̂_ρ C^ρ_ab − ∇̂_b C^ρ_aρ is v_ρ ∂_θ C⁽¹⁾ρ_ab − v_b ∂_θ C⁽¹⁾ρ_aρ + ∇̂_ρ C⁽⁰⁾ρ_ab −
∇̂_b C⁽⁰⁾ρ_aρ; the first two terms are θ-derivatives of profiles and the last two are linear in k with coefficients
independent of θ, so all four have θ-mean zero. The λ⁰ coefficient of C C is C⁽⁰⁾C⁽⁰⁾. Hence the θ-mean of the λ⁰
coefficient of Ric(g) is Ric(g0) − (1/4)⟨|k|²⟩ dv ⊗ dv, and its λ⁻¹ coefficient is v_ρ ∂_θ C⁽⁰⁾ρ_ab −
v_b ∂_θ C⁽⁰⁾ρ_aρ = −(1/2) v_a v_b ∂_θ tr k.

For the gauge term, D = g^(ab) C^ρ_ab = [D⁽⁰⁾] + λ[D⁽¹⁾] + … with D⁽⁰⁾ρ = g0^(ab) C⁽⁰⁾ρ_ab = k(ℓ)^ρ −
(1/2) ℓ^ρ tr k = −(1/2) ℓ^ρ tr k. The λ⁻¹ coefficient of −(1/2)(g_mρ ∇̂_n D^ρ + g_nρ ∇̂_m D^ρ) is
−(1/2)(v_m v_n + v_n v_m)(−1/2) ∂_θ tr k = (1/2) v_m v_n ∂_θ tr k, which cancels that of Ric(g). Its λ⁰ coefficient
is −(1/2) of the symmetrisation of

    g0_mρ (v_n ∂_θ D⁽¹⁾ρ + ∇̂_n D⁽⁰⁾ρ) + g1_mρ v_n ∂_θ D⁽⁰⁾ρ.

The first two terms have θ-mean zero as before. In the third, g1_mρ ℓ^ρ = g1(m, ℓ) = ⟨g1⟩(m, ℓ) does not depend on θ,
so ⟨g1_mρ ∂_θ D⁽⁰⁾ρ⟩ = −(1/2) ⟨g1⟩(m, ℓ) ⟨∂_θ² tr g1⟩ = 0. The gauge term has θ-mean zero at order λ⁰. With
Ric(g0) = (3μ'/(2r³)) dv ⊗ dv from [[prop:vaidya]] (a), this is [[eq:mean-leading]]. ∎

**Proposition {#prop:limit}** (the limit). Let g1 be a profile whose oscillating part g1 − ⟨g1⟩ is W_TT, evaluated at
a phase θ + κ(X), plus χ dv ⊗ dv, with κ a function of X and χ a profile. Then ⟨∂_θ g1⟩ = 0,

    ⟨|∂_θ g1|²_(g0)⟩ = (4/3) A² env² h² (c⁴ + s⁴) r⁻³,      h² (c⁴ + s⁴) = 1,                       {#eq:wave-energy}

and the θ-mean of the leading equation vanishes exactly when μ' = (2/9) A² env² h² (c⁴ + s⁴), that is, when

    dμ/dv = (2/9) A² env².                                                                          {#eq:mu-rate}

The averaged stress of the waves is round, and it is a multiple of dv ⊗ dv: the defect is null dust along dv.

*Proof.* (dv ⊗ dv)(ℓ, ·) = dv(ℓ) dv = 0 and its g0-trace is g0⁻¹(dv, dv) = 0, so by [[lem:waves]] (b) the
oscillating part is transverse to ℓ and [[lem:mean-leading]] applies. Moreover ⟨W_TT, dv ⊗ dv⟩_(g0) = W_TT(ℓ, ℓ) = 0
and |dv ⊗ dv|²_(g0) = g0⁻¹(dv, dv)² = 0, so χ does not contribute to |∂_θ g1|², and a phase shift does not change a
θ-mean. Since ∂_θ F = G and ∂_θ G = −F, [[lem:waves]] (c) gives |∂_θ W_TT|² = 8 r⁻³ (q1² + q1 q2 + q2²) with

    q1 := λ⁻¹ ∂_θ p1 = −(2c² F̂ + s² Ĝ)/3,      q2 := λ⁻¹ ∂_θ p2 = (c² F̂ + 2s² Ĝ)/3,

F̂ := â sin θ, Ĝ := â cos θ, â := A env h. With ⟨F̂²⟩ = ⟨Ĝ²⟩ = â²/2 and ⟨F̂ Ĝ⟩ = 0,

    ⟨q1²⟩ = (4c⁴ + s⁴) â²/18,   ⟨q2²⟩ = (c⁴ + 4s⁴) â²/18,   ⟨q1 q2⟩ = −(2c⁴ + 2s⁴) â²/18,

so ⟨q1² + q1 q2 + q2²⟩ = (c⁴ + s⁴) â²/6 and ⟨|∂_θ W_TT|²⟩ = (4/3) â² (c⁴ + s⁴) r⁻³. Next,
c⁴ + s⁴ = ((1 + ζ)² + (1 − ζ)²)/4 = (1 + ζ²)/2, so h² (c⁴ + s⁴) = 1. By [[eq:mean-leading]] the mean of the leading
equation is (3μ'/(2r³) − (1/3) A² env² h² (c⁴ + s⁴) r⁻³) dv ⊗ dv, which vanishes exactly when
μ' = (2/9) A² env² h² (c⁴ + s⁴), that is [[eq:mu-rate]]. ∎

This is Isaacson's effective stress as a five-dimensional null dust along dv ([Isa68a], [Isa68b]). The quadratic form
q1² + q1 q2 + q2² of the proof is positive definite: 4(q1² + q1 q2 + q2²) = (2q1 + q2)² + 3q2².

The same structure holds exactly, with no expansion in λ, in the Bondi-type variables of [[thm:bondi-law]]. Let
β, W, U, P1, P2 be smooth functions of (v, r, ϑ), put y = (y¹, y², y³) := (ϑ, φ1, φ2), U^k := (U, 0, 0),

    ξ^k := dy^k − U^k dv,      γ_P := diag(e^(−2(P1+P2)), c² e^(2P1), s² e^(2P2)),
    g := −e^(2β) W dv² + 2 e^(2β) dv dr + r² (γ_P)_kl ξ^k ξ^l,                                       {#eq:bondi-type}

which is the form [[eq:bondi-form]]. We regard each component of Ric(g) in the coordinates (v, r, y) as a function of
the derivatives of β, W, U, P1, P2 at a point, and call ∂_vP1 and ∂_vP2 the rates; the other derivatives, among them
∂_v²P_i and ∂_r∂_vP_i, are separate variables.

**Lemma {#lem:bondi-rates}** (the rates in Bondi-type variables). With S := diag(−∂_vP1 − ∂_vP2, ∂_vP1, ∂_vP2),

    Ric(g)_ab = R̊_ab + L_ab − δ^v_a δ^v_b tr(S²),      tr(S²) = 2((∂_vP1)² + ∂_vP1 ∂_vP2 + (∂_vP2)²),  {#eq:bondi-rates}

where R̊_ab does not involve the rates and L_ab is linear in them. So the part of R_vv quadratic in the rates is
−2((∂_vP1)² + ∂_vP1 ∂_vP2 + (∂_vP2)²), and no other component of the Ricci tensor contains a product of two rates.

*Proof.* Step 1 (the inverse metric). In the coframe (dv, dr, ξ^k), with dual frame (e_v, ∂_r, ∂_k), e_v := ∂_v +
U^k ∂_k, the metric is block diagonal: [[−e^(2β) W, e^(2β)], [e^(2β), 0]] on (dv, dr) and r² γ_P on (ξ^k). Inverting
each block,

    g⁻¹ = e^(−2β)(e_v ⊗ ∂_r + ∂_r ⊗ e_v) + e^(−2β) W ∂_r ⊗ ∂_r + r⁻² γ_P^(kl) ∂_k ⊗ ∂_l.

Since dv(e_v) = 1, ξ^k(e_v) = U^k − U^k = 0, ξ^k(∂_r) = 0 and ξ^k(∂_l) = δ^k_l, this gives

    g^(av) = e^(−2β) δ^a_r,      g^(ad) ξ^k_d = r⁻² γ_P^(kl) δ^a_l,                                   {#eq:bondi-inverse}

where ξ^k_d are the components of ξ^k: ξ^k_v = −U^k, ξ^k_r = 0, ξ^k_l = δ^k_l.

Step 2 (where the rates enter). The functions P_i enter g only through γ_P, and (γ_P)_kl ξ^k_a ξ^l_b is the only part of
g_ab that contains them. Since γ_P is diagonal, ∂_v γ_P = 2 γ_P S, and det γ_P = c² s² does not depend on v, so tr S = 0.
Hence the rates enter the first derivatives of g only through ∂_v g_ab, whose part containing them is

    2 r² 𝒮_ab,      𝒮_ab := (γ_P S)_kl ξ^k_a ξ^l_b,                                          {#eq:bondi-cals}

and the derivatives ∂_r g, ∂_y g do not contain them. A second derivative of g contains a rate only through ∂_v∂_v γ_P =
2(∂_v γ_P) S + 2γ_P ∂_v S = 4γ_P S² + 2γ_P ∂_v S and ∂_c∂_v γ_P = 2(∂_c γ_P) S + 2γ_P ∂_c S for c ≠ v, where ∂_v S and
∂_c S consist of second derivatives of P_i and contain no rate.

Step 3 (the Christoffel symbols). Since Γ^a_bc = (1/2) g^(ad)(∂_b g_dc + ∂_c g_db − ∂_d g_bc) is linear in the first
derivatives of g, with coefficients g⁻¹ free of rates, Γ = Γ̊ + Σ with Γ̊ free of rates and Σ the part linear in them:

    Σ^a_bc = r² ( g^(ad)(δ^v_b 𝒮_dc + δ^v_c 𝒮_db) − g^(av) 𝒮_bc ).

By [[eq:bondi-inverse]], g^(ad) 𝒮_dc = δ^a_l r⁻² γ_P^(lk)(γ_P S)_km ξ^m_c = r⁻² δ^a_l S^l_m ξ^m_c, so

    Σ^v_bc = 0,      Σ^r_bc = −e^(−2β) r² 𝒮_bc,      Σ^l_bc = S^l_m (δ^v_b ξ^m_c + δ^v_c ξ^m_b).       {#eq:bondi-sigma}

Since ξ^m_r = 0, every Σ with a lower index r vanishes: Σ^d_ar = Σ^d_ra = 0 for all a, d. The traces vanish:
Σ^c_ac = Σ^r_ar + Σ^l_al = 0 + δ^v_a S^l_l = δ^v_a tr S = 0.

Step 4 (the Ricci tensor). We use R_ab = ∂_cΓ^c_ab − ∂_bΓ^c_ac + Γ^c_cdΓ^d_ab − Γ^c_bdΓ^d_ac. A product of two
rates can arise in three ways only.
(i) From ∂_cΓ̊: Γ̊ is a function of rate-free quantities, so a single derivative of it contains each rate at most
linearly, by Step 2.
(ii) From ∂_cΣ^c_ab − ∂_bΣ^c_ac: by Step 3, Σ^v_ab = 0 and Σ^c_ac = 0 for every value of the fields, so these terms
are ∂_rΣ^r_ab + ∂_lΣ^l_ab, in which no derivative is taken in v; by Step 2 they are linear in the rates.
(iii) From the products: Γ̊Γ̊ is free of rates and Γ̊Σ is linear in them, so the quadratic part is
Σ^c_cdΣ^d_ab − Σ^c_bdΣ^d_ac. The first term vanishes because Σ^c_cd = 0.
In the second, Σ^v = 0 and Σ^d_ar = 0 leave only c = l and d = m on S³:

    Σ^c_bdΣ^d_ac = Σ^l_bm Σ^m_al = (δ^v_b S^l_m)(δ^v_a S^m_l) = δ^v_a δ^v_b tr(S²),

by [[eq:bondi-sigma]] with ξ^k_m = δ^k_m. Finally tr(S²) = (∂_vP1 + ∂_vP2)² + (∂_vP1)² + (∂_vP2)² =
2((∂_vP1)² + ∂_vP1 ∂_vP2 + (∂_vP2)²). ∎

At leading order in λ this is [[eq:mean-leading]]: the linearised angular perturbation
r²(−2(P1 + P2) dϑ² + 2c² P1 dφ1² + 2s² P2 dφ2²) has v-derivative of g0-norm squared
4((∂_vP1 + ∂_vP2)² + (∂_vP1)² + (∂_vP2)²) = 4 tr(S²), and −1/4 of it is −tr(S²).
