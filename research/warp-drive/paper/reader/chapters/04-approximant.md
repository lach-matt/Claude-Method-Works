# Part. The approximant {#part:approximant}

## The two-scale expansion and the approximant {#ch:approximant}

This chapter constructs, for every number of stages N, a metric g_app that solves the reduced equations Ric^H = 0 up to
an error of order λ^(N−1) in the scaled norms. Its leading oscillation is the pair of waves of
[[eq:waves]], shifted in phase and completed by a second harmonic along dv ⊗ dv, and its mean at leading
order is the five-dimensional Vaidya metric g0 with the mass law [[eq:mu-rate]]. The construction is the
two-scale expansion of geometric optics, carried to every order: each order is a linear hyperbolic system with smooth
coefficients for a mean correction, a phase correction and the next oscillating profile. The uniform existence theorem
[[thm:uniform-existence]] takes g_app as its input, in the form fixed by [[def:approximant]].

Throughout, the background g0, the phase v, the null geodesic generator ℓ = g0⁻¹dv = −L0, the operator □̃ := g0^(ab)
∂_a ∂_b acting componentwise and the commutator identity [[eq:commutator]] for [L0, □̃] are those of [[prop:vaidya]]; the
gauge field D and the reduced Ricci tensor Ric^H are those of [[sec:gauge]]; Ω, its slices Σ_τ, τ0 and
τ_end are those of [[sec:domain]]; and profiles f(X, θ) on Ω × S¹, their evaluation [f](X) = f(X, v(X)/λ),
their θ-mean ⟨f⟩ and the scaled norms |f|_j are those of [[sec:profiles]] and
[[eq:scaled-norm]]. Tensors are arrays of components in the Cartesian coordinates X = (τ, x) unless
another chart is named.

### Two-scale operators {#sec:two-scale}

Let u be a smooth function on Ω, a phase. For a profile f write [f]_u(X) := f(X, u(X)/λ), so that [f]_v = [f]. The chain
rule gives

    ∂_a [f]_u = [∂^u_a f]_u,        ∂^u_a := ∂_a + λ⁻¹ (∂_a u) ∂_θ.                            {#eq:two-scale-derivative}

In the coordinates X the reduced Ricci tensor is an expression

    Ric^H(g)_mn = F_mn(X, g, ∂g, ∂²g),

polynomial in g, g⁻¹, ∂g and ∂²g, whose explicit dependence on X is through the Christoffel symbols of g0 and their first
derivatives [[sec:gauge]]; second derivatives of g enter it only through −(1/2) g^(ab) ∂_a ∂_b g_mn.

**Definition {#def:two-scale}** (The two-scale operator.) For a profile G of symmetric 2-tensors with det G ≠ 0, the
two-scale operator is

    R_u[G](X, θ) := F(X, G, ∂^u G, ∂^u ∂^u G)(X, θ),

that is, Ric^H with g replaced by G and every derivative ∂_a by ∂^u_a. We write R := R_v.

By [[eq:two-scale-derivative]], Ric^H([G]_u) = [R_u[G]]_u. The operator R_u[G] is a polynomial in λ⁻¹ whose coefficients
are built from G and its X- and θ-derivatives, from g0 and its derivatives at X, and from the derivatives of u; it
contains θ only through G.

**Lemma {#lem:phase-shift-symmetry}** (Equivariance under shifts of the phase.) (a) For every profile G and every
constant c,

    R[G(·, · + c)](X, θ) = R[G](X, θ + c).                                                       {#eq:phase-equivariance}

(b) If Φ is a smooth function on Ω, possibly depending on λ, and u = v + λΦ, then for each λ R[G(·, · + Φ)](X, θ) = R_u[G](X, θ + Φ(X)).

*Proof.* (b) contains (a): for Φ = c, ∂u = ∂v, so R_u = R. For a profile f put f_Φ(X, θ) := f(X, θ + Φ(X)). Then

    ∂^v_a f_Φ = (∂_a f + (∂_a Φ) ∂_θ f + λ⁻¹ (∂_a v) ∂_θ f)(X, θ + Φ(X)) = (∂^u_a f)_Φ,

since ∂_a u = ∂_a v + λ ∂_a Φ. Applied to the profile ∂^u_b f, the same identity gives ∂^v_a ∂^v_b f_Φ = (∂^u_a ∂^u_b
f)_Φ. So R[G_Φ](X, θ) = F(X, G_Φ, ∂^v G_Φ, ∂^v ∂^v G_Φ) = F(X, G, ∂^u G, ∂^u ∂^u G)(X, θ + Φ(X)) = R_u[G](X, θ + Φ(X)),
because the explicit dependence of F on X does not involve θ. ∎

Let G = g0 + λ g1 + Σ_(j≥2) λ^j g_j be a finite sum of profiles bounded with all their derivatives. Then R[G] is a
polynomial in λ⁻¹ and, through G⁻¹, a smooth function of λ near 0 with profile coefficients, and we write its expansion

    R[G] = λ⁻¹ R^(−1) + R^(0) + λ R^(1) + … .                                                   {#eq:two-scale-expansion}

The term of order λ⁻¹ is

    R^(−1) = −(1/2) g0⁻¹(dv, dv) ∂_θ² g1 = 0.

Indeed ∂^v_a ∂^v_b (λ g1) = λ⁻¹ (∂_a v)(∂_b v) ∂_θ² g1 + O(1), and every other term of Ric^H contains at most first
derivatives, while ∂^v G = O(1); and g0⁻¹(dv, dv) = 0 because dv is null for g0 [[prop:vaidya]].

### Approximants {#sec:approximants}

**Definition {#def:approximant}** (Approximant.) Let N ≥ 1, K and k be integers. An approximant with N stages is a metric

    g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j],                                                        {#eq:approximant}

with profiles g_j such that every derivative ∂^i_(X,θ) g_j is bounded on Ω × S¹ independently of λ. It is of order K at
regularity k if it has the following three properties.

- (E1) *Transversality of the wave*: (g1 − ⟨g1⟩)(ℓ, ·) = 0 for all (X, θ). The mean ⟨g1⟩ is unrestricted.
- (E2) *The leading equation*: the coefficient R^(0)(X, θ) of λ⁰ in the two-scale expansion
  [[eq:two-scale-expansion]] of Ric^H(g_app), that is of R[g0 + λ g1 + Σ_(j≥2) λ^j g_j], vanishes identically in
  (X, θ).
- (E3) *The residual*: |Ric^H(g_app)|_k (τ) ≤ C_R λ^K for every τ ∈ [τ0, τ_end], with C_R independent of λ.

### The leading coefficient {#sec:leading-coefficient}

The leading coefficient R^(0) of a wave on g0 has a closed form once the wave is transverse to ℓ and traceless.

**Lemma {#lem:leading-coefficient}** (The leading coefficient.) Let W be a profile of symmetric 2-tensors with W(ℓ, ·) =
0 and tr W := g0^(ab) W_ab = 0 at every (X, θ). Then the two-scale expansion of R[g0 + λ W] has R^(−1) = 0 and

    R^(0) = Ric(g0) − ∇_ℓ ∂_θ W − (1/2)(□_(g0) v) ∂_θ W − (1/4) |∂_θ W|² dv ⊗ dv,               {#eq:leading-coefficient}

where ∇ is the Levi-Civita connection of g0 acting on W at fixed θ, □_(g0) the wave operator of g0 on functions, and
|∂_θ W|² := g0^(ac) g0^(bd) ∂_θ W_ab ∂_θ W_cd.

*Proof.* We compute with profiles. The formulas below for Ric(g), C, D and S are polynomial identities in the 2-jet of
h := g − g0 at a point, with coefficients from the 2-jet of g0, and they hold for every symmetric array of second
derivatives. The two-scale derivative ∂^v_a := ∂_a + λ⁻¹ v_a ∂_θ satisfies ∂^v_a ∂^v_b = ∂^v_b ∂^v_a, and ∂_a [F] = [∂^v_a
F] in every chart, since v is a scalar. So the identities hold for profiles, with ∂_a replaced by ∂^v_a and the
covariant derivative of g0 by ∇^v_a := ∇_a + λ⁻¹ v_a ∂_θ, where ∇_a acts at fixed θ; R[g0 + λ W] is Ric^H(g0 + λ W)
computed in this way, in any chart, and we identify the coefficients of the powers of λ, which are profiles. Write ∂ :=
∂_θ and v_a := ∂_a v, raise and lower indices with g0, so that ℓ^a = g0^(ab) v_b, and put h := λ W, g := g0 + h.
The hypotheses give, at every (X, θ),

    W_ab ℓ^b = 0,   ∂W_ab ℓ^b = 0,   ℓ^a v_a = 0,   g0^(ab) W_ab = 0,   g0^(ab) ∂W_ab = 0.

The tensor C := Γ[g] − Γ[g0] satisfies

    C^c_ab = (1/2) g^(cd) (∇_a h_bd + ∇_b h_ad − ∇_d h_ab),
    Ric(g)_ab = Ric(g0)_ab + ∇_c C^c_ab − ∇_b C^c_ac + C^c_cd C^d_ab − C^c_bd C^d_ac,

and the gauge field is D^ρ = g^(ab) C^ρ_ab, so that Ric^H(g)_mn = Ric(g)_mn − S_mn with S_mn := (1/2)(g_mρ ∇_n D^ρ + g_nρ
∇_m D^ρ) [[sec:gauge]], with ∇ read as ∇^v. Now ∇^v_a h = v_a ∂W + λ ∇_a W, and g⁻¹ = g0⁻¹ − λ W^♯ + O(λ²) with W^♯ :=
g0⁻¹ W g0⁻¹. So C = C_0 + λ C_1 + O(λ²) with the profiles

    C_0^c_ab = (1/2)(v_a ∂W_b^c + v_b ∂W_a^c − ℓ^c ∂W_ab),
    C_1^c_ab = (1/2)(∇_a W_b^c + ∇_b W_a^c − ∇^c W_ab) − (1/2) W^(cd) (v_a ∂W_bd + v_b ∂W_ad − v_d ∂W_ab).

Their traces are C_0^c_ac = (1/2) v_a g0^(cd) ∂W_cd = 0 and, writing W·∂W := W^(cd) ∂W_cd and using g0^(cd) ∇_a W_cd =
∇_a (tr W) = 0 and W^(cd) v_c = 0,

    C_1^c_ac = −(1/2) v_a W·∂W.

The gauge field. At order λ⁰, D is g0^(ab) C_0^ρ_ab = (1/2)(ℓ^b ∂W_b^ρ + ℓ^a ∂W_a^ρ − ℓ^ρ g0^(ab) ∂W_ab) = 0. At order λ,
D_1^ρ := g0^(ab) C_1^ρ_ab − W^(ab) C_0^ρ_ab. In the first term the linear part is (div W)^ρ − (1/2) ∇^ρ tr W = (div W)^ρ,
with (div W)_b := ∇^a W_ab, and the quadratic part is −(1/2) W^(ρd)(2 ℓ^b ∂W_bd − v_d g0^(ab) ∂W_ab) = 0; the second term
is −(1/2)(2 W^(ab) v_a ∂W_b^ρ − ℓ^ρ W·∂W) = (1/2) ℓ^ρ W·∂W. So D = λ D_1 + O(λ²) with

    D_1^ρ = (div W)^ρ + (1/2) ℓ^ρ W·∂W.

The order λ⁻¹. The only terms of size λ⁻¹ come from the derivatives of C_0 in phase: ∇^v_c C^c_ab − ∇^v_b C^c_ac
contains λ⁻¹ (v_c ∂C_0^c_ab − v_b ∂C_0^c_ac). Since C_0^c_ac = 0, this is λ⁻¹ v_c ∂C_0^c_ab = λ⁻¹ (1/2) ∂(v_a v_c
∂W_b^c + v_b v_c ∂W_a^c − v_c ℓ^c ∂W_ab) = 0, because v_c ∂W_b^c = ∂W_bc ℓ^c = 0. The products C C are O(1), and S = O(1) because D = O(λ). So R^(−1) = 0.

The order λ⁰ of Ric(g) − Ric(g0) has four parts.

(i) From ∇^v_c C^c_ab: the term ∇_c C_0^c_ab and the phase derivative v_c ∂C_1^c_ab. First,

    ∇_c C_0^c_ab = (1/2)(∇_c v_a ∂W_b^c + ∇_c v_b ∂W_a^c + v_a ∇_c ∂W_b^c + v_b ∇_c ∂W_a^c − (∇_c ℓ^c) ∂W_ab
                   − ∇_ℓ ∂W_ab).

Second, v_c W^(cd) = 0 removes the quadratic part of C_1, and differentiating W_bd ℓ^d = 0 gives ℓ^d ∇_a W_bd = −W_bd
∇_a ℓ^d, so

    v_c ∂C_1^c_ab = (1/2)(−∂W_bd ∇_a ℓ^d − ∂W_ad ∇_b ℓ^d − ∇_ℓ ∂W_ab).

Since ℓ is the gradient of v, ∇_a ℓ^d = ∇^d ∇_a v, and so ∇_c v_a ∂W_b^c = ∂W_bd ∇^d ∇_a v = ∂W_bd ∇_a ℓ^d: these terms
cancel in pairs. With ∇_c ℓ^c = □_(g0) v the sum of (i) is

    −∇_ℓ ∂W_ab − (1/2)(□_(g0) v) ∂W_ab + (1/2)(v_a (div ∂W)_b + v_b (div ∂W)_a).

(ii) From −∇^v_b C^c_ac: −∇_b C_0^c_ac − v_b ∂C_1^c_ac = 0 + (1/2) v_a v_b ∂(W·∂W).

(iii) From C^c_cd C^d_ab: at order λ⁰ this is C_0^c_cd C_0^d_ab = 0.

(iv) From −C^c_bd C^d_ac: at order λ⁰ this is −C_0^c_bd C_0^d_ac. Of the nine products in

    (v_b ∂W_d^c + v_d ∂W_b^c − ℓ^c ∂W_bd)(v_a ∂W_c^d + v_c ∂W_a^d − ℓ^d ∂W_ac),

eight contain a contraction of ∂W with v or with ℓ, or the contraction v_c ℓ^c, and vanish; the ninth is v_a v_b ∂W_d^c
∂W_c^d = v_a v_b |∂W|². So (iv) is −(1/4) v_a v_b |∂W|².

The term S at order λ⁰. As D = λ D_1 + O(λ²), ∇^v_n D^ρ = v_n ∂D_1^ρ + O(λ), and g_mρ = (g0)_mρ + O(λ). So S has the
λ⁰ coefficient

    (1/2)(v_n ∂D_1m + v_m ∂D_1n) = (1/2)(v_n (div ∂W)_m + v_m (div ∂W)_n) + (1/2) v_m v_n ∂(W·∂W),

since ℓ lowered is v. Subtracting it from (i)–(iv), the divergence terms and the terms in ∂(W·∂W) cancel, and what
remains is [[eq:leading-coefficient]]. The parts of C and D of order λ² contribute at order λ only. ∎

### Stage 0 {#sec:stage-zero}

Since [[eq:leading-coefficient]] is tensorial we evaluate it in ingoing Eddington–Finkelstein coordinates (v, r, ϑ, φ1,
φ2), where x1 + i x2 = r cos ϑ e^(iφ1), x3 + i x4 = r sin ϑ e^(iφ2), ϑ ∈ [0, π/2], and c := cos ϑ, s := sin ϑ. With
τ = v − r the Minkowski metric is −dτ² + dr² + r² dΩ² = −dv² + 2 dv dr + r² dΩ², so

    g0 = −(1 − μ(v)/r²) dv² + 2 dv dr + r² (dϑ² + c² dφ1² + s² dφ2²).                                  {#eq:eddington}

Its inverse has g0^(vv) = 0, g0^(vr) = 1, g0^(rr) = 1 − μ/r², no mixed component between (v, r) and the angles, and on
the angular coordinates A, B ∈ {ϑ, φ1, φ2} the inverse of the round metric of radius r. Hence ℓ = g0⁻¹dv = ∂_r, the
derivative at fixed (v, ϑ, φ1, φ2); it agrees with −L0 = −∂_τ + x̂·∂_x. The density is |det g0|^(1/2) = r³ c s, so

    □_(g0) v = (r³ c s)⁻¹ ∂_a (r³ c s g0^(ab) ∂_b v) = (r³ c s)⁻¹ ∂_r (r³ c s) = 3/r.

The Christoffel symbols with one lower index r are read from Γ^σ_(ra) = (1/2) g0^(σd)(∂_r g_da + ∂_a g_dr − ∂_d g_ra),
where g_vr = 1 and g_rr = g_rA = 0: for an angular index A, Γ^B_(rA) = r⁻¹ δ^B_A and Γ^v_(rA) = Γ^r_(rA) = 0; further
Γ^B_(rv) = Γ^B_(rr) = 0 and Γ^v_(ra) = (1/2) ∂_a g_rr = 0 for every a. Consequently ∇_ℓ dv = 0, and for a symmetric
tensor Y with only angular components, ∇_ℓ Y has only angular components, equal to

    (∇_ℓ Y)_AB = ∂_r Y_AB − (2/r) Y_AB.                                                           {#eq:transport-angular}

The Ricci tensor of g0 is Ric(g0) = (3 μ'(v)/(2 r³)) dv ⊗ dv [[prop:vaidya]].

In these coordinates the leading wave W_TT of [[eq:waves]] reads, with y_i := r^(−3/2) p_i/λ,

    W_TT = 2 r² (−(y1 + y2) dϑ² + c² y1 dφ1² + s² y2 dφ2²),
    y1 = (α/3)(2 c² cos θ − s² sin θ),     y2 = (α/3)(2 s² sin θ − c² cos θ),     α := A env(v) h r^(−3/2),

with h = h(cos 2ϑ) of [[sec:waves]]. The chart (v, r, ϑ, φ1, φ2) is singular on the axes c = 0 and s = 0. Every
identity below holds off the axes between tensors smooth on r > 0 ([[lem:waves]] (a), and the smoothness of χ shown
after [[lem:stage-zero]]), so it holds on the axes by continuity.

**Lemma {#lem:stage-zero}** (Stage 0.) Let χ be a smooth function on Ω × S¹ and W := W_TT + χ dv ⊗ dv. Then:

(a) W(ℓ, ·) = 0 and tr W = 0;

(b) R^(−1) = 0 in the two-scale expansion of R[g0 + λ W], and

    R^(0) = (3 μ'/(2 r³) − 2 ((∂_θ y1)² + ∂_θ y1 ∂_θ y2 + (∂_θ y2)²) − (∂_r + 3/(2r)) ∂_θ χ) dv ⊗ dv;    {#eq:stage-zero}

(c) the θ-mean of R^(0) vanishes in every component exactly when μ' = (2/9) A² env² h² (c⁴ + s⁴), and h² (c⁴ + s⁴) = 1,
so exactly when μ' = (2/9) A² env²;

(d) with χ = 0, the oscillating part R^(0) − ⟨R^(0)⟩ is a second harmonic in θ (a combination of cos 2θ and sin 2θ) in
the vv component, and every other component of R^(0) vanishes;

(e) χ enters R^(0) only through the term −(∂_r + 3/(2r)) ∂_θ χ in the vv component.

*Proof.* (a) W_TT has only angular components and ℓ = ∂_r, so W_TT(ℓ, ·) = 0, and its trace is r⁻²(−2 r² (y1 + y2)) +
(r c)⁻²(2 r² c² y1) + (r s)⁻²(2 r² s² y2) = 0. For the second term, (dv ⊗ dv)(ℓ, ·) = dv(ℓ) dv = g0⁻¹(dv, dv) dv = 0, and
its trace is g0⁻¹(dv, dv) = 0.

(b) By (a), [[lem:leading-coefficient]] applies and gives R^(−1) = 0 and R^(0) = Ric(g0) − ∇_ℓ ∂_θ W − (3/(2r)) ∂_θ W −
(1/4)|∂_θ W|² dv ⊗ dv. The angular components of ∂_θ W_TT are r^(1/2) times functions of (v, ϑ, θ), so by
[[eq:transport-angular]] ∇_ℓ ∂_θ W_TT = (1/2 − 2) r⁻¹ ∂_θ W_TT, that is

    ∇_ℓ ∂_θ W_TT + (3/(2r)) ∂_θ W_TT = 0.

Since ∇_ℓ dv = 0, ∇_ℓ (∂_θ χ dv ⊗ dv) = (∂_r ∂_θ χ) dv ⊗ dv. For the quadratic term, the contraction of dv ⊗ dv with a
symmetric tensor Y is Y(ℓ, ℓ), so |∂_θ W|² = |∂_θ W_TT|² + 2 (∂_θ χ) ∂_θ W_TT(ℓ, ℓ) + (∂_θ χ)² g0⁻¹(dv, dv)² = |∂_θ
W_TT|². In the frame r⁻¹ ∂_ϑ, (r c)⁻¹ ∂_φ1, (r s)⁻¹ ∂_φ2, orthonormal for the round metric of radius r, ∂_θ W_TT is
diagonal with entries −2 ∂_θ(y1 + y2), 2 ∂_θ y1, 2 ∂_θ y2, so

    (1/4)|∂_θ W_TT|² = (∂_θ y1 + ∂_θ y2)² + (∂_θ y1)² + (∂_θ y2)² = 2 ((∂_θ y1)² + ∂_θ y1 ∂_θ y2 + (∂_θ y2)²).

With Ric(g0) = (3 μ'/(2 r³)) dv ⊗ dv this is [[eq:stage-zero]].

(c) The χ term is a θ-derivative and has mean zero. By the formula for (1/4)|∂_θ W_TT|² in (b) and [[eq:wave-energy]],
2 ⟨(∂_θ y1)² + ∂_θ y1 ∂_θ y2 + (∂_θ y2)²⟩ = (1/4) ⟨|∂_θ W_TT|²⟩ = (1/3) A² env² h² (c⁴ + s⁴) r⁻³, so

    ⟨R^(0)⟩ = r⁻³ ((3/2) μ' − (1/3) A² env² h² (c⁴ + s⁴)) dv ⊗ dv,

which vanishes exactly when μ' = (2/9) A² env² h² (c⁴ + s⁴); and h² (c⁴ + s⁴) = 1 by [[eq:wave-energy]]. This is
[[prop:limit]], here with the oscillating part of R^(0) in full.

(d) ∂_θ y1 and ∂_θ y2 are combinations of sin θ and cos θ, so the quadratic expression in [[eq:stage-zero]] is a
combination of 1, cos 2θ and sin 2θ, and its oscillating part is a second harmonic. By (b) every component of R^(0)
other than vv vanishes.

(e) is read from (b). ∎

*The choice at stage 0.* Assume the mass law μ' = (2/9) A² env² [[eq:mu-rate]]. By [[lem:stage-zero]],
R^(0) = (F_2 − (∂_r + 3/(2r)) ∂_θ χ) dv ⊗ dv with

    F_2 := −2 ((∂_θ y1)² + ∂_θ y1 ∂_θ y2 + (∂_θ y2)²) + (1/3) α² (c⁴ + s⁴),

the vv second harmonic of R^(0) at χ = 0. Let χ be the profile with zero θ-mean that vanishes on Σ_τ0 and solves the
transport

    (∂_r + 3/(2r)) ∂_θ χ = F_2                                                                        {#eq:chi-transport}

along ℓ = ∂_r: first ∂_θ χ, a second harmonic, is found by integrating along the integral curves of ℓ, which from every
point of Ω reach Σ_τ0 inside Ω [[lem:domain]] (d), and χ is its primitive in θ with zero mean. Then R^(0)
≡ 0 identically in (X, θ). The function χ is smooth on Ω × S¹, at the axes of the T² action included: ℓ has no angular
component, so the transport preserves smoothness on S³, and its right-hand side F_2 is built from g0 and W_TT, which is smooth at both axes ([[lem:waves]] (a)); explicitly F_2 is r⁻³ env(v)² h² times a polynomial in sin θ, cos θ, c² =
(x1² + x2²)/r² and s² = (x3² + x4²)/r², with h² = 2/(1 + cos² 2ϑ) and cos 2ϑ = (x1² + x2² − x3² − x4²)/r², which is
smooth on r > 0.

### The ansatz {#sec:ansatz}

The unknowns are the means m_j (j ≥ 1), the phases φ_j (j ≥ 1) and the oscillating profiles ĝ_j (j ≥ 2, of zero θ-mean).
With the mean metric ḡ := g0 + Σ_(j=1)^N λ^j m_j, the phase u := v + Σ_(j=1)^N λ^j φ_j, W := W_TT + χ dv ⊗ dv as in
[[sec:stage-zero]], and

    G := ḡ + λ W + Σ_(j=2)^(N+1) λ^j ĝ_j(X, θ),        g_app := G(X, u/λ) = [G]_u,                    {#eq:ansatz}

we have Ric^H(g_app) = [R_u[G]]_u, and λ⁻¹ du = λ⁻¹ dv + Σ_j λ^(j−1) dφ_j. Expand R_u[G] = Σ_m λ^m ℛ^(m). The phase is
the eikonal of the mean metric to each order: in −(1/2) g^(ab) ∂_a ∂_b (λ W), the terms in which both derivatives fall on
the phase sum to −(1/2) λ⁻¹ ḡ⁻¹(du, du) ∂_θ² W plus terms with an oscillating factor of g⁻¹, and

    ḡ⁻¹(du, du) = Σ_(j≥1) λ^j e_j,        e_j = 2 ℓ·dφ_j − m_j(ℓ, ℓ) − q_j,                    {#eq:eikonal-coefficients}

with q_j a polynomial in (m_i, dφ_i), i < j: q_1 = 0 and q_2 = −(m1 m1)(ℓ, ℓ) − |dφ1|² + 2 m1(ℓ, dφ1), indices moved by
g0. Indeed ḡ⁻¹ = g0⁻¹ − λ m1^♯ + λ² ((m1 m1)^♯ − m2^♯) + O(λ³), du = dv + λ dφ1 + λ² dφ2 + O(λ³) and g0⁻¹(dv, dv) = 0,
which gives e_1 = 2 ℓ·dφ1 − m1(ℓ, ℓ) and the stated q_2; the higher q_j are read off in the same way.

*Weights.* In the expansion of R_u[G] every monomial carries at most two derivatives. A derivative is ∂_X, of weight
0; λ⁻¹ (∂v) ∂_θ, of weight −1; or λ^(i−1) (∂φ_i) ∂_θ, of weight i − 1. The derivative ∂_θ acts only on oscillating
factors: W, of weight 1, and ĝ_i, of weight i. The mean m_i has weight i, and g0 weight 0; G⁻¹ is expanded in powers of
λ, its term of order λ^i having weight i. The order in λ of a monomial is the sum of the weights of its factors and its
derivatives.

**Definition {#def:first-stage-operator}** (The operator T̂.) Let G1 := g0 + λ (m1 + W) and u1 := v + λ φ1. For a
profile Y with zero θ-mean let T̂Y be the coefficient of λ⁰ in the two-scale expansion of

    (d/dε)|_(ε=0) R_(u1)[G1 + ε λ Y].

The coefficient of λ⁻¹ in this expansion is −(1/2) g0⁻¹(dv, dv) ∂_θ² Y = 0, so T̂ is the leading part of the linearised
two-scale operator at the first stage, applied to λY.

**Lemma {#lem:first-entry}** (Where each unknown first enters.) ℛ^(−1) = 0. ℛ^(0) is the coefficient of λ⁰ of R[g0 + λ W]
at (X, θ), minus (1/2) e_1 ∂_θ² W. For m ≥ 1,

    ℛ^(m) = T̂ ĝ_(m+1) − (1/2) e_(m+1) ∂_θ² W + 𝒲(m_m, φ_m) + 𝒦_m,                                     {#eq:stage-m}

where 𝒲 is linear in m_m and in φ_m: in m_m to second order, its θ-mean part being −(1/2) □̃ m_m plus terms of first
order; in φ_m through dφ_m and □̃φ_m, the latter only as −(1/2)(□̃φ_m) ∂_θ W. 𝒦_m depends only on m_i, φ_i (i < m) and
ĝ_i (i ≤ m).

*Proof.* We count weights. A factor of stage m + 1 has weight m + 1 (ĝ_(m+1), m_(m+1)) or contributes the derivative λ^m
(∂φ_(m+1)) ∂_θ of weight m. In a monomial of order m containing ĝ_(m+1), the other factors and the derivatives therefore
have weights summing to −1. Every weight is at least 0 except that of λ⁻¹ (∂v) ∂_θ, and there are at most two
derivatives. Let n be the number of derivatives λ⁻¹ (∂v) ∂_θ in the monomial; then n ∈ {1, 2}, and the other factors
and derivatives have weights summing to n − 1. If n = 1, they all have weight 0, and the derivative λ⁻¹ (∂v) ∂_θ hits
ĝ_(m+1), since ∂_θ needs an oscillating factor and the only factor of weight 0 is g0. If n = 2, exactly one other
factor has weight 1 and every other factor and derivative weight 0; the two derivatives λ⁻¹ (∂v) ∂_θ both hit
ĝ_(m+1), or one hits ĝ_(m+1) and the other W, or both hit W while ĝ_(m+1) stands undifferentiated in g⁻¹ (the term
(1/2) ĝ_(m+1)(ℓ, ℓ) ∂_θ² W). In every case ĝ_(m+1) appears linearly, since two such factors have
weight at least 2(m + 1) − 2 > m, and the other factors have weight at most 1: they are g0, v, W, m1 and φ1 (the
derivative (∂φ1) ∂_θ having weight 0). These are the factors of weight at most 1 of G1 and u1, and the same count
applies to λ Y in R_(u1)[G1 + ε λ Y], which has weight 1; so these terms are T̂ ĝ_(m+1). A monomial of order m
containing m_(m+1) or ∂φ_(m+1) has the remaining weights summing to −1 or 0 respectively; they arise only in the phase
contraction [[eq:eikonal-coefficients]], where both derivatives of λ W fall on the phase, and give −(1/2) e_(m+1) ∂_θ²
W. Two factors among m_m and ∂φ_m have weights at least
m − 1 each (m_m has weight m, and the derivative λ^(m−1) (∂φ_m) ∂_θ weight m − 1), and every ∂_θ needs an oscillating
factor, of weight at least 1; so they reach order m only when m = 1, in the phase contraction, through the q_2 terms, which [[eq:eikonal-coefficients]] places in
e_2. The second harmonic of W hit twice by λ⁻¹ (∂v) ∂_θ is contracted with ḡ⁻¹(dv, dv), of weight at least 1, since
g0⁻¹(dv, dv) = 0.

Apart from the q_2 terms, which [[eq:eikonal-coefficients]] places in e_2, the stage-m unknowns m_m and φ_m therefore
appear linearly at order m. The mean m_m, of weight m, reaches order m undifferentiated in θ; its second derivatives
enter only through the principal term, as −(1/2) g0^(ab) ∂_a ∂_b m_m = −(1/2) □̃ m_m, the corrections to g⁻¹ having
positive weight, and its other terms carry at most one derivative of m_m. The phase φ_m enters only through the
derivative λ^(m−1) (∂φ_m) ∂_θ, of weight m − 1, which must act on an oscillating factor; at order m it appears through
dφ_m, or, when the second derivative of the principal term falls on ∂φ_m, as −(1/2) g0^(ab) (∂_a ∂_b φ_m) ∂_θ W =
−(1/2)(□̃φ_m) ∂_θ W; no other term of Ric^H contains a second derivative. At order m − 1 the stage-m unknowns appear only
in −(1/2) e_m ∂_θ² W and in −(1/2) g0⁻¹(dv, dv) ∂_θ² ĝ_(m+1) = 0, and at order m − 2 or lower not at all. This gives
the form of ℛ^(m) for m ≥ 1 and ℛ^(−1) = 0. At order 0, the terms containing m1 or φ1 are those of −(1/2) e_1 ∂_θ² W;
ĝ_2 enters order 0 only through −(1/2) g0⁻¹(dv, dv) ∂_θ² ĝ_2 = 0; the rest is the coefficient of λ⁰ of R[g0 + λ W].
At order −1 the only term is −(1/2) g0⁻¹(dv, dv) ∂_θ² W = 0. ∎

**Lemma {#lem:first-stage-operator}** (The operator T̂.) If e_1 = 0, then on profiles Y of zero θ-mean

    T̂ Y = −(ℓ·∂_X) ∂_θ Y + ℳ Y,

with ℳ algebraic in X and of first order in θ, its coefficients smooth bounded profiles built from g0, its
derivatives, v and W alone. In particular, when e_1 = 0, T̂ does not depend on m1 or φ1.

*Proof.* We take the terms of R_(u1)[G1 + ε λ Y] linear in ε at order λ⁰. Here ∂^(u1)_a = ∂_a + λ⁻¹ v_a ∂_θ + (∂_a φ1)
∂_θ, so

    ∂^(u1)_a ∂^(u1)_b (λ Y) = λ⁻¹ v_a v_b ∂_θ² Y + v_a ∂_b ∂_θ Y + v_b ∂_a ∂_θ Y + (∂_a ∂_b v) ∂_θ Y
                    + (v_a ∂_b φ1 + v_b ∂_a φ1) ∂_θ² Y + O(λ),

and G1⁻¹ = g0⁻¹ − λ (m1 + W)^♯ + O(λ²). The principal term −(1/2) G1^(ab) ∂^(u1)_a ∂^(u1)_b (λ Y) therefore contributes at order
λ⁰

    −(ℓ·∂_X) ∂_θ Y − (1/2)(□̃v) ∂_θ Y − (ℓ·dφ1) ∂_θ² Y + (1/2)(m1 + W)(ℓ, ℓ) ∂_θ² Y
        = −(ℓ·∂_X) ∂_θ Y − (1/2)(□̃v) ∂_θ Y − (1/2) e_1 ∂_θ² Y,

since W(ℓ, ℓ) = 0 and e_1 = 2 ℓ·dφ1 − m1(ℓ, ℓ). The variation of G⁻¹ in the principal term, −λ Y^♯ + O(λ²), meets
∂^(u1)_a ∂^(u1)_b G1 = λ⁻¹ v_a v_b ∂_θ² W + O(1) and gives (1/2) Y(ℓ, ℓ) ∂_θ² W. The remaining terms of Ric^H are of first order
in g [[sec:gauge]]; their variation contains ∂^(u1)(λ Y) = dv ⊗ ∂_θ Y + O(λ) times coefficients built from G1, ∂^(u1) G1 and g0,
bounded profiles whose parts of order λ⁰ are built from g0, ∂g0 and dv ⊗ ∂_θ W (m1 has zero θ-derivative, and φ1
enters ∂^(u1) G1 only at order λ), and λ Y times bounded profiles, which is O(λ). So T̂ Y = −(ℓ·∂_X) ∂_θ Y −
(1/2) e_1 ∂_θ² Y + ℳ Y with ℳ Y := −(1/2)(□̃v) ∂_θ Y + (1/2) Y(ℓ, ℓ) ∂_θ² W + B·(dv ⊗ ∂_θ Y), B a bounded profile built from g0, ∂g0, v and
W. With e_1 = 0 this is the claim; m1 and φ1 entered only through e_1. ∎

**Lemma {#lem:linear-wave}** (Linear wave equations on Ω.) Let d ≥ 1, and let B^a and C be smooth d × d matrices of
functions on Ω, smooth meaning that all their derivatives extend continuously to the boundary. For every smooth f on Ω
with values in ℝ^d and smooth u0, u1 on Σ_τ0 there is a unique smooth u on Ω with

    −(1/2) □̃ u + B^a ∂_a u + C u = f   on Ω,      u = u0  and  ∂_τ u = u1   on Σ_τ0.                {#eq:linear-wave}

*Proof.* Uniqueness. The difference w of two solutions solves −(1/2) □̃ w = −B^a ∂_a w − C w with zero data, so
[[lem:energy]] with g̃ = g0 gives ‖∂w(τ)‖ + ‖w(τ)‖ ≤ C ∫_(τ0)^τ (‖∂w(s)‖ + ‖w(s)‖) ds, and w = 0 by Gronwall's
inequality.

Existence. (i) The domain. Let M := {(τ, x) : |x| > a/2} with the metric g0, time-oriented so that τ increases to the
future, and S := Σ_τ0 ∩ M. Since g0⁻¹(dτ, dτ) = −1 − μ/r² < 0 ([[prop:vaidya]] (d)), τ is strictly increasing along
future causal curves, so S is a smooth spacelike hypersurface which every causal curve meets at most once: S is
acausal. By [[thm:std-bgp-development]] its Cauchy development D, the set of points of M through which every
inextendible causal curve meets S, is open and globally hyperbolic, with S as a Cauchy hypersurface. We show Ω ⊂ D.
Let p ∈ Ω, and follow an inextendible causal curve γ of M through p to the past. While τ ≥ τ0 along γ, γ stays in Ω,
by [[lem:domain]] (e) applied to g0. Suppose τ > τ0 along all of it. Parametrised by τ ∈ (τ*, τ(p)], τ* ≥ τ0, its
velocity V has dτ(V) = 1. At the points of the compact set Ω the causal vectors V with dτ(V) = 1 form a compact set:
a sequence of them with Euclidean norms tending to infinity would have, after normalisation, a causal limit V ≠ 0
with dτ(V) = 0, which the timelike covector dτ excludes. So γ is Lipschitz in τ and converges, as τ decreases to τ*,
to a point of Ω ⊂ M, and γ is extendible, a contradiction. Hence γ reaches {τ = τ0}, at a point of Ω ∩ Σ_τ0 ⊂ S, and
p ∈ D. Ω is connected and meets S, so it lies in the connected component of D that contains the connected set S. This
component is open and globally hyperbolic with Cauchy hypersurface S, since an inextendible causal curve in it is one
of D; we call it D again.

(ii) The extension. The interior of Ω is a bounded Lipschitz domain in ℝ⁵: near each point of its boundary it is
bounded by at most two of the hypersurfaces Σ_τ0, Σ_τ_end, {r = a} and {v + τ = V + 1 + τ_end}, which are smooth and
have linearly independent normals where two of them meet. Stein's operator of [[thm:std-sy-extension]], applied to
B^a, C and f, which lie in W^(k,∞) of the interior for every k, gives extensions to ℝ⁵ with bounded derivatives of
every order, hence smooth. Likewise extend u0 and u1 from the annulus Σ_τ0 ∩ Ω to smooth functions on {τ = τ0}. Let
ψ be a smooth function with compact support in D, equal to 1 on a neighbourhood of Ω, which exists since Ω is compact
and D open; multiply the extensions of f, u0 and u1 by ψ.

(iii) The solution. The operator P := □̃ − 2 B^a ∂_a − 2 C acts on sections of the trivial bundle D × ℝ^d and has
principal symbol ∓ g0⁻¹(ξ, ξ) id, so P or −P is normally hyperbolic for g0 ([[def:std-normally-hyperbolic]]); we take
that one, changing the sign of the right-hand side with it. With n the future unit normal of S and ∇ the connection
of [[thm:std-bgp-cauchy]], prescribing u and ∇_n u on S is equivalent to prescribing u and ∂_τ u on S, since dτ(n) > 0
and the other terms of ∇_n u are tangential derivatives of u and multiples of u. [[thm:std-bgp-cauchy]] therefore
gives u ∈ C^∞(D) solving P u = −2 ψ f̃, f̃ the extension of f, with the data ψ ũ0, ψ ũ1, the extensions of u0 and u1.
On Ω the cut-off equals 1 and the extensions agree with B^a, C, f, u0 and u1, so u restricted to Ω solves
[[eq:linear-wave]]. ∎

**Lemma {#lem:stage-system}** (Each stage is a linear hyperbolic system.) Let m ≥ 1 and let everything of earlier stages
be given and smooth. Write the θ-mean of 𝒲(m_m, 0) as −(1/2) □̃ m_m + B̄·∂m_m + C̄ m_m, put 𝒲_φ(φ_m) := 𝒲(0, φ_m),
𝒮_m := −⟨𝒦_m⟩, and let Π_osc := 1 − ⟨·⟩ be the projection onto zero θ-mean. Impose e_m = 0, the θ-mean of
[[eq:stage-m]], and its oscillating part without the e_(m+1) term:

    (a) −(1/2) □̃ m_m + B̄·∂m_m + C̄ m_m = 𝒮_m − ⟨𝒲_φ(φ_m)⟩ − ⟨T̂ ĝ_(m+1)⟩,
    (b) L0 φ_m = −(1/2) m_m(ℓ, ℓ) − (1/2) q_m,
    (c) Π_osc T̂ ĝ_(m+1) = −Π_osc (𝒲(m_m, φ_m) + 𝒦_m),                                                {#eq:stage-system}

with data (m_m, ∂_τ m_m), φ_m and ĝ_(m+1) on Σ_τ0. This system has a unique smooth solution on Ω.

*Proof.* Equation (b) is e_m = 0, since ℓ·dφ_m = −L0 φ_m. ⟨T̂ ĝ⟩ contains no X-derivative of ĝ, because the term −(ℓ·∂_X)
∂_θ ĝ of [[lem:first-stage-operator]] has θ-mean zero; and ⟨𝒲_φ⟩ contains only dφ_m, because □̃φ_m multiplies ∂_θ W,
whose mean is zero. For Z := ∂_θ ĝ_(m+1), equation (c) is the transport

    −(ℓ·∂_X) Z + ℳ' Z = F

along ℓ, with ℳ' := Π_osc ℳ ∂_θ⁻¹ a bounded operator on smooth zero-mean profiles ([[lem:first-stage-operator]]; ∂_θ⁻¹ the
zero-mean primitive): an ordinary differential equation along the integral curves of ℓ, which reach Σ_τ0 inside Ω
[[lem:domain]] (d). Its right-hand side contains □̃φ_m. Put Ψ_m := □̃φ_m. By the commutator identity for
[L0, □̃] [[eq:commutator]] applied to (b), Ψ_m satisfies the transport

    L0 Ψ_m − (2/r) Ψ_m = −(1/2) □̃(m_m(ℓ, ℓ) + q_m) − (1/r)(∂_τ + ∂_r)(m_m(ℓ, ℓ) + q_m) − (3/r²) ∂_r φ_m,

and □̃(m_m(ℓ, ℓ)) = (□̃ m_m)(ℓ, ℓ) + first order, with □̃ m_m from (a): first order in (m_m, φ_m) and algebraic in
ĝ_(m+1). The datum of Ψ_m on Σ_τ0 is □̃φ_m computed from the data: φ_m is given there, ∂_τ φ_m = L0 φ_m + x̂·∂_x φ_m
with L0 φ_m from (b), and ∂_τ² φ_m follows from the τ-derivative of (b), which involves ∂_τ m_m on Σ_τ0. The system for
(m_m, φ_m, Ψ_m, Z) is then linear with smooth coefficients and closes without loss: m_m in H^(s+1), φ_m in H^(s+1),
Ψ_m and Z in H^s.

We solve it by Picard iteration on Ω. Given an iterate, the next one takes m_m from (a) by [[lem:linear-wave]], with
the right-hand side evaluated at the given iterate, and φ_m, Ψ_m and Z from their transports, which are ordinary
differential equations with smooth coefficients along the integral curves of ℓ, solved from Σ_τ0 ([[lem:domain]] (d)).
Every iterate is smooth. The difference of two successive iterates solves the same linear system with zero data and
with the previous difference in its right-hand sides. So the energy and transport estimates [[lem:energy]] and
[[lem:transport]], in which λ plays no role, give for the sum e_n(τ) of the norms of the n-th difference, at the
regularities just stated, e_(n+1)(τ) ≤ C ∫_(τ0)^τ e_n(s) ds, hence e_n(τ) ≤ (C (τ − τ0))^n sup e_0 / n!. The iterates
converge and the limit solves the system; the same estimate, for zero data and zero right-hand side, gives uniqueness.
Ψ_m = □̃φ_m holds because, by [[eq:commutator]] applied to (b), □̃φ_m solves the same transport as Ψ_m, so their
difference solves a homogeneous transport with zero data. Smooth data give smooth solutions, the iteration closing at
every s. ∎

### The approximant {#sec:approximant}

**Theorem {#thm:approximant}** (The approximant to every order.) For every N ≥ 1 and every smooth choice of stage data
there are profiles g1, …, g_N, independent of λ, such that g_app = g0 + λ [g1] + Σ_(j=2)^N λ^j [g_j] is an approximant
with N stages of order K = N − 1 ([[def:approximant]]), at every regularity k, with C_R depending on k. Its oscillating
part of g1 is the wave W_TT of [[eq:waves]] with the second harmonic χ dv ⊗ dv of [[eq:chi-transport]],
shifted in phase: g1 = m1 + W(X, θ + φ1(X)), W = W_TT + χ dv ⊗ dv. The background is g0 with μ' = (2/9) A² env².

Here the stage data are the data on Σ_τ0 of [[lem:stage-system]], (m_m, ∂_τ m_m), φ_m and ĝ_(m+1) for m = 1, …, N, each
smooth and ĝ_(m+1) of zero θ-mean.

*Proof.* Solve stage 0 ([[sec:stage-zero]]) and the stages m = 1, …, N ([[lem:stage-system]]), with ĝ_(N+1) from stage
N. The unknowns φ_(N+1) and m_(N+1) are not included, so e_(N+1) = −q_(N+1) need not vanish; this is harmless, since
only ℛ^(m) with m ≤ N − 1 is used. By [[lem:first-entry]], ℛ^(m) = 0 for m ≤ N − 1: ℛ^(0) = 0 by the choice at stage 0
and e_1 = 0, and for 1 ≤ m ≤ N − 1 the mean and oscillating parts of [[eq:stage-m]] vanish by [[eq:stage-system]] and
e_(m+1) = 0. So R_u[G] = Σ_(m≥N) λ^m ℛ^(m) is λ^N times a profile bounded uniformly in λ, rational in λ through
G⁻¹. Since the scaled norm of an evaluated profile is bounded by the bounds of the profile and its derivatives, with no
loss for the oscillation [[sec:profiles]], |Ric^H([G]_u)|_k ≤ C λ^N for every k.

Rewrite with the fixed phase v. With Ψ := Σ_(j≥2) λ^(j−2) φ_j, [G]_u(X) = G(X, v/λ + φ1 + λ Ψ). Expanding in λΨ by
Taylor's formula about θ + φ1 to order N gives profiles g_j(X, θ) independent of λ, with g1 = m1 + W(X, θ + φ1(X)), and a
remainder O(λ^(N+1)) in scaled norms. Ric^H contains at most two derivatives, each costing at most λ⁻¹ in the scaled
norms, so this remainder changes Ric^H by O(λ^(N−1)) in |·|_k.

(E1) holds because W is transverse ([[lem:stage-zero]] (a)) and ⟨g1⟩ = m1. (E2) holds: by [[lem:phase-shift-symmetry]]
(b) with Φ = φ1 + λΨ, the two-scale operator with the fixed phase satisfies R[G(·, · + Φ)](X, θ) = R_u[G](X, θ + Φ),
whose coefficient of λ⁰ is ℛ^(0)(X, θ + φ1) = 0, since ℛ^(−1) = 0. The coefficient R^(0) depends on the profiles only
through g1, because the coefficient of ∂_θ² g2 at that order is −(1/2) g0⁻¹(dv, dv) = 0, and the coefficient of λ in the
expansion of G(·, · + Φ) is g1; so R^(0) of g_app vanishes identically. (E3) holds with K
= N − 1. ∎

So the uniform existence theorem [[thm:uniform-existence]] applies to the approximant of any order, built from any smooth
stage data.

**Remark {#rem:stage-data}** Stage data for which the approximant's Cauchy data satisfy the constraints and the gauge
condition D = 0 to order N − 2 exist; they are chosen in [[lem:stage-data]], in the proof of [[thm:data]].
