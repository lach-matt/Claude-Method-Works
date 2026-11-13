## The normal operator at future timelike infinity {#ch:s08}

This chapter studies the normal operator of a stationary wave-type operator P_0 at future timelike infinity ι⁺, and its
Mellin-transformed family N⁰(σ), in dimension 4 + 1. It writes out the part of [Hin26c, Section 10.1] that precedes the
forward problem: the ι⁺-normal operator and its family ([Hin26c, Definition 10.3 and Lemma 10.5]); the estimates and
invertibility of N⁰(σ) at high frequencies, without and with b-regularity ([Hin26c, Proposition 10.6 (2) and Lemma
10.7]); and at bounded frequencies ([Hin26c, Proposition 10.6 (1) and Lemmas 10.9–10.10]). The forward problems for
N_(ι⁺)(P_0), for the modified operator P_+ and for P_0 on e3b-spaces, which rest on these results, are solved in
[[ch:s09]]. [[sec:ii-f-1-4]] proves in addition a uniqueness lemma for hyperbolic equations with smooth coefficients
([[lem:ii-f-1-3]]), and the functions monotone along causal curves that supply the compact sets it asks for
([[lem:ii-f-1-4]]); later chapters use both.

*What changes in dimension 4 + 1.* The dimension enters through the constant c := (n − 1)/2 of the normal form
[[eq:ii-c-1-1]], which is 3/2 here ([[rem:ii-f-minkowski]]), and through the volume densities, which shift weights by
n/2 = 2 and (n + 1)/2 = 5/2 ([[eq:ii-f-density]]). Every threshold below is a sum of these, and each is evaluated at n =
4 where it occurs.

*Method.* The analysis at high frequencies is semiclassical, in the parameterised scaled bounded geometry calculus on ι⁺
of [[sec:ii-a-6-2]], whose properties from [Hin26d] are listed in [[sec:ii-a-3]]. [Hin26c, Section 10.1.2] runs the
positive commutator arguments in that calculus briefly and leaves "the statements of standalone propagation estimates to
the reader". Here the positive commutator scheme of [[ch:s02]] is carried over to that calculus ([[sec:ii-f-2]]); each
radial estimate then reduces to an evaluation of symbols at the radial set, which is written out. At bounded frequencies
the model at ℐ⁺ is handled with the parametrix of the 0-calculus with bounds [Hin23e, Theorem 3.4], used only through
the Fredholm property it gives on a compact manifold, and b-regularity is proved by difference quotients. Uniqueness for
second-order hyperbolic equations with smooth coefficients is taken from [BGP].

*Radii.* The radii 0 < r_0 < r^♮ := (r_0 + r_2)/2 < r_2 < r′_0 are those of [[sec:i-a-1-1]] and [[lem:ii-c-3-2]].
Nothing in this chapter depends on their values beyond these inequalities; in particular every result holds for every
inner radius r_0 at which the hypotheses of [[ch:s01]] and [[ch:s05]] hold.

*Notation.* As in [[ch:s02]], the rank of the bundle is N_E, so that sections take values in ℂ^(N_E); the largest
eigenvalue of an endomorphism that is self-adjoint for a fibre inner product is written max spec; and large integers
bounding orders of Sobolev spaces are written M. The constant that multiplies the absorbing operator 𝒜 in the
decompositions of [[sec:ii-f-2-2]] is written ℓ, and the localisation constant of (D9) below is written δ_s. Variable
orders are written in sans-serif letters 𝗌, 𝖻, 𝗋, and multi-orders in bold letters 𝐨, 𝐞, 𝐦, 𝐤, 𝐭.

### Setting {#sec:ii-f-1}

#### Coordinates and weights {#sec:ii-f-1-1}

Throughout, n = 4, and c := 3/2 except where c is introduced as a level ([[lem:ii-f-1-3]], [[lem:ii-f-1-4]]) or as
the weight at cf of an order ([[sec:ii-f-2-1]]). Near (ι⁺)° we use τ := t_*⁻¹ and R := r/t_* ([[lem:ii-a-2-11]]), so
that ρ = r⁻¹ = τ/R; we put v := R⁻¹ = t_*/r, and near ι⁺ ∩ ℐ⁺

    x_I := R^(−1/2) = (t_*/r)^(1/2),

which is the x′_I of [[sec:ii-b-7]] and [[ch:s06]] (it differs from the x_I = r^(−1/2) of [[sec:ii-e-1]] by the factor
t_*^(1/2)). ι⁺ = [0, ∞]_R × 𝕊³, with boundary faces ι⁺ ∩ K⁺ = {R = 0} and ι⁺ ∩ ℐ⁺ = {x_I = 0}; ρ_K := R/(1 + R) and x_I
(or (1 + R)^(−1/2)) are defining functions of them. In (t_*, r) and (τ, R),

    t_*∂_(t_*)|_r = −τ∂_τ − R∂_R,      r∂_r|_(t_*) = R∂_R = −½ x_I∂_(x_I),      ρ∂_ρ|_(t_*) = −R∂_R.      {#eq:ii-f-1-1}

Indeed τ = 1/t_* and R = r/t_* give t_*∂_(t_*)τ = −τ and t_*∂_(t_*)R = −R at fixed r, and x_I = R^(−1/2) gives R∂_R = −½
x_I∂_(x_I).

*Weights.* Let μ_b be a smooth positive b-density on ι⁺, for instance |(dR/R) dg̸|, with g̸ the round metric of 𝕊³.
Since t = t_* + r and dx = r³ dr dg̸ on ℝ⁴, and t_* = τ⁻¹, r = Rτ⁻¹ give dt_* ∧ dr = −τ⁻³ dτ ∧ dR,

    |dt dx| = r³ |dt_* dr dg̸| = R³τ⁻⁶ |dτ dR dg̸| = R⁴τ⁻⁵ |dτ/τ| μ_b.                              {#eq:ii-f-density}

So L²(|dt dx|) = R⁻²τ^(5/2) L²(|dτ/τ| μ_b). Near ι⁺ ∩ ℐ⁺, R⁻² = x_I⁴ and τ is a defining function of ι⁺ comparable to
ρ_+; near ι⁺ ∩ K⁺, R ∼ ρ_K and τ ∼ ρ_+ρ_K, so R⁻²τ^(5/2) ∼ ρ_+^(5/2)ρ_K^(1/2). This is [[lem:ii-a-6-1]] near ι⁺ (on the
support of a cut-off χ to cl{r ≥ 1, t_* ≥ 1}): H^(0,(2α_I,α_+,α_K))_e3b(|dt dx|) =
H^(0,(2(α_I+2),α_++5/2,α_K+1/2))_e3b(|dτ/τ| μ_b). As τ ∼ ρ_+ρ_K near ι⁺, the weights ρ_+^(α_++5/2)ρ_K^(α_K+1/2) are
τ^(α_++5/2)ρ_K^(α_K−α_+−2). So, with b-densities on [0, ∞)_τ × ι⁺, the weights of this chapter are

    γ_I := α_I + 2 at ℐ⁺,    γ_+ := α_+ + 5/2 at τ = 0,    γ_cf := −(α_+ + 2) at ι⁺ ∩ K⁺ (for α_K = 0).   {#eq:ii-f-1-2}

In dimension 3 + 1, [Hin26c] has α_I + 3/2, α_+ + 2 and −(α_+ + 3/2). The weight α_sf + 2 with which P_0 is
tf-admissible ([[def:ii-c-2-7]] (2), with α_sf = α_+) is −γ_cf.

*Indicial gap.* (β_−, β_+) is the indicial gap of P̂_0(0) that contains −γ_cf = α_+ + 2 ([[def:ii-c-2-3]],
[[def:ii-c-2-7]] (2) and [[def:i-c-1-1]]). By [[sec:ii-c-2-4]], α_+ + 2 is the b-weight at ∂X that corresponds to the
spatial weight α_+ of an L²(|dx|)-based space in dimension 4.

*The Mellin transform.* In this chapter, as in [Hin26c, Section 10],

    (ℳu)(σ, ·) := ∫_0^∞ τ^(−iσ) u(τ, ·) dτ/τ,      ℳ(τ∂_τ u) = iσ ℳu.                                   {#eq:ii-f-1-3}

This is the transform of [[sec:ii-a-6-2]] at −σ. For u = τ^γ w, (ℳu)(σ − iγ) = (ℳw)(σ) for real σ, as τ^(−i(σ−iγ))τ^γ =
τ^(−iσ): the Plancherel line of the weight τ^γ is Im σ = −γ ([[lem:ii-a-6-2]] with σ ↦ −σ; its line Im σ = +β_+ is for
τ^(iσ)).

#### The normal operator at ι⁺ {#sec:ii-f-1-2}

By [[def:ii-c-1-1]], on {ρ < ρ_1},

    P_0 = −2∂_(t_*)ρ(ρ∂_ρ − c − S) + ρ²P⁽⁰⁾(ρ, ω, ρ∂_ρ, ∂_ω) + Q∂_(t_*) − g_00∂²_(t_*),   {#eq:ii-f-1-4}

with S ∈ C^∞(X̄; End ℂ^(N_E)), P⁽⁰⁾ ∈ Diff²_b(X̄; E), P⁽⁰⁾ ≡ ((ρD_ρ)² + Δ_(𝕊³)) Id modulo Diff¹_b + ρ Diff²_b
([[lem:ii-c-1-2]]), Q ∈ ρ³Diff¹_b and g_00 ∈ ρ²C^∞(X̄). We write P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω) for the operator whose
coefficients are those of P⁽⁰⁾ frozen at ρ = 0 (its normal operator at ∂X, N(P⁽⁰⁾) of [[eq:i-c-4-1]]), and S_0 :=
S|_(∂X).

**Definition {#def:ii-f-1-1}** (The ι⁺-normal operator; [Hin26c, Definition 10.3] in dimension 4 + 1.) The *ι⁺-normal
operator* of P_0 is N_(ι⁺)(P_0) := t_*⁻² N⁰ on (0, ∞)_τ × (ι⁺)°, with

    N⁰ := −2R⁻¹(τ∂_τ + R∂_R)(R∂_R + c + S_0) + R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω).                                 {#eq:ii-f-1-5}

Its *Mellin-transformed family* is

    N⁰(σ) := −2R⁻¹(iσ + R∂_R)(R∂_R + c + S_0) + R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω)
           = x_I²[−½(x_I∂_(x_I) − 2iσ)(x_I∂_(x_I) − 2(c + S_0)) + x_I²P⁽⁰⁾(0, ω, ½x_I∂_(x_I), ∂_ω)],   {#eq:ii-f-1-6}

so that ℳ(N⁰u)(σ) = N⁰(σ)(ℳu)(σ) by [[eq:ii-f-1-3]].

The second form of [[eq:ii-f-1-6]] follows from R∂_R = −½x_I∂_(x_I) and R⁻¹ = x_I²: iσ + R∂_R = −½(x_I∂_(x_I) − 2iσ) and
R∂_R + c + S_0 = −½(x_I∂_(x_I) − 2(c + S_0)). [Hin26c, Definition 10.3] prints the factor t_*² in place of t_*⁻²; the
factor t_*⁻² is the one that its use in [Hin26c, Proposition 10.12] ("N⁰_(ι⁺)(P_0)u = t_*²f") and the homogeneity of
degree −2 require.

In (t_*, r, ω), by [[eq:ii-f-1-1]], τ∂_τ + R∂_R = −t_*∂_(t_*) and R⁻¹ = t_*/r, so

    N_(ι⁺)(P_0) = 2r⁻¹∂_(t_*)(r∂_r + c + S_0) + r⁻²P⁽⁰⁾(0, ω, −r∂_r, ∂_ω):                                 {#eq:ii-f-1-7}

the operator [[eq:ii-f-1-4]] with Q = 0, g_00 = 0 and its coefficients frozen at ρ = 0. It is invariant under
translations in t_*, homogeneous of degree −2 under (t_*, x) ↦ (at_*, ax), a > 0, and its principal symbol is the dual
metric function of the Minkowski metric ḡ: by [[lem:ii-c-1-2]], σ_2(ρ²P⁽⁰⁾) = ḡ⁻¹ on spatial covectors up to ρ²P^[2],
and σ_2(−2∂_(t_*)ρ ρ∂_ρ) = σ_2(2∂_(t_*)∂_r), which with the frozen part gives −2ζ_(t_*)ζ_r + ζ_r² + r⁻²|η|² = ḡ⁻¹(ζ, ζ)
(the proof of [[lem:ii-e-2-4]]). In (τ, R) this is the dual metric

    g⁻¹_(ι⁺) = τ⁻²ḡ⁻¹ = 2R⁻¹(τ∂_τ + R∂_R) ⊗_s R∂_R + R⁻²((R∂_R)² + g̸⁻¹),   {#eq:ii-f-1-8}

with a ⊗_s b := ½(a ⊗ b + b ⊗ a), and d(log τ) = −dt_*/t_* is null for it, as dt_* is for ḡ.

**Remark {#rem:ii-f-minkowski}** (The constant c.) For the wave operator of Minkowski space, P_0 = −□_ḡ Id on ℝ^(1+4),
[[eq:ii-f-1-7]] holds exactly with S_0 = 0, and it shows where c = 3/2 comes from. In (t_*, r, ω), ḡ = −dt_*² − 2dt_*
dr + r²g̸, so ḡ⁻¹(dt_*, dt_*) = 0, ḡ⁻¹(dt_*, dr) = −1, ḡ⁻¹(dr, dr) = 1, and |det ḡ|^(1/2) = r³ |det g̸|^(1/2). With
Δ_(𝕊³) ≥ 0 the Laplacian of g̸,

    −□_ḡ = 2∂_(t_*)∂_r + 3r⁻¹∂_(t_*) − ∂_r² − 3r⁻¹∂_r + r⁻²Δ_(𝕊³)
         = 2r⁻¹∂_(t_*)(r∂_r + 3/2) + r⁻²(−(r∂_r)² − 2r∂_r + Δ_(𝕊³)),

since r²(∂_r² + 3r⁻¹∂_r) = (r∂_r)² − r∂_r + 3r∂_r. With ρ∂_ρ = −r∂_r the last bracket is (ρD_ρ)² + 2ρ∂_ρ + Δ_(𝕊³). So
−□_ḡ is [[eq:ii-f-1-7]] with c = 3/2, S_0 = 0 and P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω) = (ρD_ρ)² + 2ρ∂_ρ + Δ_(𝕊³), whose principal part
is that of [[lem:ii-c-1-2]]; as its coefficients do not depend on ρ and Q = 0, g_00 = 0, N_(ι⁺)(−□_ḡ) = −□_ḡ. In
dimension n + 1 the same steps give 3 ↦ n − 1, so c = (n − 1)/2, and the term (n − 2)ρ∂_ρ; c = 1 in dimension 3 + 1.

**Lemma {#lem:ii-f-1-2}** ([Hin26c, Lemma 10.5] in dimension 4 + 1.) Let χ ∈ C^∞(M) equal 1 near ι⁺, supported in a
small collar of ι⁺. Then

    χN_(ι⁺)(P_0) ∈ x_I²ρ_+²Diff²_e3b(M),    χ(P_0 − N_(ι⁺)(P_0)) ∈ x_I²ρ_+³Diff²_e3b(M).   {#eq:ii-f-1-9}

*Proof.* The first membership is checked as in [[lem:ii-c-1-4]] (b), which uses of P_0 only the form [[eq:ii-f-1-4]],
and N_(ι⁺)(P_0) has that form. For the second, t_*²(P_0 − N_(ι⁺)(P_0)) = t_*²P_0 − N⁰, and by [[eq:ii-f-1-1]],
t_*²·(−2∂_(t_*)ρ(ρ∂_ρ − c − S_0)) and t_*²ρ²P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω) are the two terms of [[eq:ii-f-1-5]]: ∂_(t_*) =
−τ(τ∂_τ + R∂_R), which commutes with ρ = τ/R, and ρ∂_ρ = −R∂_R, so −2ρ∂_(t_*)(ρ∂_ρ − c − S_0) = −2τ²R⁻¹(τ∂_τ +
R∂_R)(R∂_R + c + S_0), and t_*²ρ² = R⁻². The remaining terms are, near ℐ⁺ with x_I = v^(1/2): (i) −2t_*²∂_(t_*)ρ(S_0 −
S), the difference of the S-terms of [[eq:ii-f-1-4]] and [[eq:ii-f-1-7]], with S − S_0 ∈ ρC^∞, so that ρ(S_0 − S) ∈
ρ²C^∞ and, ρ² = τ²R⁻² being annihilated by τ∂_τ + R∂_R, it is of the form τR⁻²(τ∂_τ + R∂_R)·C^∞, which vanishes at τ = 0
and to order R⁻² = x_I⁴ at ℐ⁺; (ii) t_*²ρ²(P⁽⁰⁾(ρ, ·) − P⁽⁰⁾(0, ·)) ∈ t_*²ρ³Diff²_b(X̄), of the schematic form
τR⁻³(R∂_R, ∂_ω)^(≤2), hence x_I⁴τ(x_I∂_(x_I), x_I∂_ω)^(≤2), as R⁻³∂_ω² = x_I⁴(x_I∂_ω)²; (iii) t_*²Q∂_(t_*) ∈
t_*²ρ³Diff¹_b(X̄)∂_(t_*), of the form τ²R⁻³(τ∂_τ + R∂_R)(R∂_R, ∂_ω)^(≤1); (iv) t_*²g_00∂²_(t_*), g_00 ∈ ρ²C^∞, of the
form τ²R⁻²(τ∂_τ + R∂_R)^(≤2). Each lies in τx_I⁴Diff² of the fields τ∂_τ, x_I∂_(x_I), x_I∂_ω near ι⁺ ∩ ℐ⁺, and in
τDiff²_b near ι⁺ ∩ K⁺, where R ≤ C. Multiplying by t_*⁻² = τ² and using τ ∼ ρ_+ near ι⁺ ∩ ℐ⁺ and τ ∼ ρ_+ρ_K near ι⁺ ∩
K⁺, together with the e3b-spanning sets of [[sec:ii-a-2-4]], gives [[eq:ii-f-1-9]]. The powers of ρ in (i)–(iv) do not
depend on n. ∎

#### The family on ι⁺ and its semiclassical rescaling {#sec:ii-f-1-3}

By [[eq:ii-f-1-6]], N⁰(σ) ∈ x_I²ρ_K⁻²Diff²_(0,b)(ι⁺): near ι⁺ ∩ K⁺ it is R⁻² times a b-differential operator in (R, ω),
and near ι⁺ ∩ ℐ⁺ it is x_I² times a 0-differential operator in the fields x_I∂_(x_I), x_I∂_ω ([[sec:ii-a-6-2]]:
C^∞_b𝒱_(0,b)(ι⁺)). Its 0,b-principal symbol is, with 0-covectors ξ_0 dx_I/x_I + η_0 dω/x_I,

    x_I²(½ξ_0² + |η_0|² + ¼x_I²ξ_0²) Id,   {#eq:ii-f-1-10}

since −½(x_I∂_(x_I))² ↦ ½ξ_0² and x_I²P⁽⁰⁾(0, ω, ½x_I∂_(x_I), ∂_ω) ↦ x_I²(¼ξ_0²) + |η_0|² (Δ_(𝕊³) ≥ 0); near ι⁺ ∩ K⁺ the
b-principal symbol is R⁻² times that of (RD_R)² + Δ_(𝕊³) plus the term −2R⁻¹(R∂_R)² ↦ 2R⁻¹ξ_b², positive definite. So
N⁰(σ) is elliptic in the 0,b-sense, for every σ ∈ ℂ.

For h ∈ (0, 1] and z ∈ ℂ with |z| ∈ [½, 2] put

    P_(ι,h,z) := h²N⁰(h⁻¹z)
               = x_I²[−½(hx_I∂_(x_I) − 2iz)(hx_I∂_(x_I) − 2h(c + S_0))
                      + h²x_I²P⁽⁰⁾(0, ω, ½x_I∂_(x_I), ∂_ω)]   {#eq:ii-f-1-11}
               = −2R⁻¹(iz + hR∂_R)(hR∂_R + h(c + S_0)) + h²R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω).   {#eq:ii-f-1-12}

It is a family in the semiclassical 0- and cone calculus on ι⁺_(0ħ,cħ) of [[sec:ii-a-6-2]], of differential order 2,
with weights x_I² at the face over ι⁺ ∩ ℐ⁺ and ρ_cf⁻² at cf, and orders 0 at sf and tf ([Hin26c, (3.55a)–(3.55b)]). Near
ι⁺ ∩ ℐ⁺ we use semiclassical 0-covectors ξ dx_I/(hx_I) + η dω/(hx_I), and near ι⁺ ∩ K⁺ semiclassical cone covectors ξ_cħ
((h + R)/h)(dR/R) + ((h + R)/h)η_cħ; over sf (h = 0) near cf these are ξ_cħ dR/h + (R/h)η_cħ. The principal symbol at sf
is

    G_(ι,z) = x_I²[½(ξ − 2z)ξ + |η|² + ¼x_I²ξ²] = 2(z + Rξ_cħ)ξ_cħ + ξ_cħ² + |η_cħ|²,   {#eq:ii-f-1-13}

from [[eq:ii-f-1-11]] with hx_I∂_(x_I) ↦ iξ, hx_I∂_ω ↦ iη, and from [[eq:ii-f-1-12]] with hR∂_R ↦ iRξ_cħ, h∂_ω ↦ iRη_cħ
over sf: −2R⁻¹(iz + iRξ_cħ)(iRξ_cħ) = 2(z + Rξ_cħ)ξ_cħ and h²R⁻²((RD_R)² + Δ) ↦ ξ_cħ² + |η_cħ|². The term ¼x_I²ξ², which
[Hin26c, (10.21)] omits, vanishes at ℐ⁺ and changes none of the conclusions drawn there. At fibre infinity of the
semiclassical phase space the symbol is that of [[eq:ii-f-1-10]], positive definite, so the semiclassical characteristic
set is a compact subset of the face sf over ι⁺, away from fibre infinity ([Hin26c, Section 10.1.1]).

*Real z.* For z = ±1 the characteristic set and the flow over sf are the pull-back of [[prop:ii-b-8-1]] ([Hin26c,
Proposition 4.24]) along the identification of the semiclassical phase space with the e3b-phase space over ι⁺ at the
time frequency ∓1 ([Hin26c, Section 10.1.1]). Its radial sets are

    R_(I⁺,±1,in) := {x_I = 0, ξ = ±2, η = 0},              R_(I⁺,out) := {x_I = 0, ξ = 0, η = 0},
    R_(cf,±1,in) := {R = 0, ξ_cħ = ∓2, η_cħ = 0},    R_(cf,out) := {R = 0, ξ_cħ = 0, η_cħ = 0},   {#eq:ii-f-1-14}

all over sf. At z = 1: on {x_I = 0}, G_(ι,1)/x_I² = ½(ξ − 1)² − ½ + |η|²; its Hamilton field in the coordinates (x_I, ω;
ξ, η) is

    𝖧_I := H_(x_I⁻²G_(ι,1)) = (ξ − 1)(x_I∂_(x_I) + η·∂_η) − 2|η|²∂_ξ + x_I H_(|η|²)
           at x_I = 0 to first order,                                                                     {#eq:ii-f-1-15}

with H_(|η|²) = 2η·∂_ω at the centre of normal coordinates ([Hin26c, Section 10.1.2]; the evaluation is that of
[[eq:ii-b-7-4]] at the time frequency −1). It vanishes exactly at R_(I⁺,±1,in) and R_(I⁺,out) on the characteristic set
over {x_I = 0}, where ξ(ξ − 2) = −2|η|². Near ι⁺ ∩ K⁺, with ĥ := h/R, the field of G_(ι,1) in the covectors ξ_cħ dR/h +
η_cħ R dω/h is ([Hin26c, Section 10.1.2], by the change of variables)

    𝖧_cf := ĥ((2(1 + 2R)ξ_cħ + 2)(R∂_R − η_cħ·∂_(η_cħ)) + 2(|η_cħ|² − Rξ_cħ²)∂_(ξ_cħ) + H_(|η_cħ|²)).   {#eq:ii-f-1-16}

Up to the factor ĥ, it vanishes over {R = 0} on the characteristic set exactly at R_(cf,1,in) and R_(cf,out). The future
flow has the types (A, B) (A the α-limit set, B the ω-limit set): A = R_(I⁺,±1,in) and B = R_(I⁺,out) or R_(cf,±1,in);
A = R_(cf,±1,in) and B = R_(cf,out); A = R_(cf,out) and B = R_(I⁺,out) ([[prop:ii-b-8-1]], the entries over ι⁺, pulled
back). R_(I⁺,±1,in) is a source, R_(I⁺,out) a sink, and R_(cf,±1,in), R_(cf,out) are saddles: the stable manifold of
R_(cf,±1,in) lies over R > 0 (the curves from R_(I⁺,±1,in)), its unstable manifold over R = 0, which is the stable
manifold of R_(cf,out), whose unstable manifold lies over R > 0 (the curves to R_(I⁺,out)).

*Complex z.* If Im z ≠ 0, Im G_(ι,z) = 2(Im z)ξ_cħ (resp. −x_I²(Im z)ξ) vanishes only where ξ_cħ = 0, and then Re
G_(ι,z) = |η_cħ|² forces η_cħ = 0; likewise in the 0-variables. So the characteristic set is the zero section over sf,
and the flow of the Hamilton field of Re(z⁻¹G_(ι,z)) on it, 2ĥR∂_R = 2h∂_R near R = 0 and −x_I∂_(x_I) near x_I = 0 (up
to positive factors), runs from R_(cf,out), now a source, to the sink R_(I⁺,out) ([Hin26c, (10.22) and Figure 10.1]).

*Orders.* Let 𝗌 be an order function admissible for P_0 with weights α_+, 0 and margin 0 ([[def:ii-c-5-2]]). As in
[Hin26c, Section 10.1.1] (by pull-back along the identifications above) it induces a differential order 𝗌_(0,b) on
^(0,b)S*ι⁺, a differential order 𝗌_(0ħ,cħ) at fibre infinity of the semiclassical phase space, and semiclassical orders
𝖻_± on the face sf for σ → ±∞ ([Hin26c, (10.12)–(10.13)]). By [[prop:ii-c-5-1]] and [[def:ii-c-2-4]], pulled back: 𝖻_±
is non-increasing along the future flow over sf, constant near the radial sets [[eq:ii-f-1-14]], and

    𝖻_± + α_+ > ½(−1 + ϑ_in) at R_(cf,±1,in),    𝖻_± + α_+ < −½ + S̄ at R_(cf,out),   {#eq:ii-f-1-17}

with the fibre inner products chosen as in [[def:ii-c-2-4]] and [[lem:ii-c-2-6]] (up to any margin): these are
[[def:ii-c-2-4]] (5)–(6) with α_sf = α_+ and α_K = 0, as the 3b-regularity order at the radial sets over ∂K⁺ is the
semiclassical order here ([Hin26c, (10.28) and after]).

#### Uniqueness for hyperbolic equations with smooth coefficients {#sec:ii-f-1-4}

Several steps of [[ch:s09]] and of the later chapters show that a solution of a wave equation vanishes, or identify two
solutions, on regions of M° or of Minkowski space ℝ^(1+4) where the operator has smooth coefficients. They use one
statement, proved here from [BGP]. A *time function* on a time-oriented Lorentzian manifold X is τ ∈ C^∞(X) with dτ past
timelike; then dτ(V) > 0 for every future directed causal V, so τ is strictly increasing along future directed causal
curves. J⁻_X(p) is the set of points reached from p by past directed causal curves in X, together with p ([BGP, p. 18]).

**Lemma {#lem:ii-f-1-3}** (Uniqueness of solutions supported to the future.) Let X be a time-oriented Lorentzian
manifold with metric g, P a second-order operator with smooth coefficients on a vector bundle over X with principal
symbol g⁻¹(ζ, ζ) Id, τ a time function on X and c ∈ ℝ. Assume that for every p ∈ X with τ(p) > c there is a compact set
L_p ⊂ X containing J⁻_X(p) ∩ {τ ≥ c}. If w ∈ 𝒟′(X), Pw = 0 and supp w ⊂ {τ > c}, then w = 0.

*Proof.* We use the following from [BGP]. Theorem 3.1.1 (p. 68): on a connected time-oriented Lorentzian manifold with
no causal loops, a closed causal relation and a finite continuous time separation, a distribution with past or future
compact support solving Pu = 0, P normally hyperbolic, vanishes. Remark 3.1.3 (p. 72): these assumptions hold on
globally hyperbolic manifolds. Definition 1.3.8 (p. 23): global hyperbolicity is strong causality with J⁺(p) ∩ J⁻(q)
compact for all p, q. A set A is past compact if A ∩ J⁻(p) is compact for every p, and a curve is inextendible if no
piecewise C¹ reparametrisation extends continuously to an end point (p. 18). The Cauchy development D(S) of S is the set
of points through which every inextendible causal curve meets S (Definition 1.3.5, p. 22), and the causal future of a
Cauchy hypersurface is past compact (p. 22). Lemma A.5.9 (p. 176): for an acausal hypersurface S, D(S) is an open,
causally compatible, globally hyperbolic subset; and S is a Cauchy hypersurface of D(S) (the end of the proof of Lemma
A.5.9, p. 176). P or −P is normally hyperbolic in the sense of [BGP, Section 1.5], its principal part being ∓ the
d'Alembertian of g, and Pw = 0 if and only if −Pw = 0. Working on each connected component, we may assume X connected.

If {τ > c} is empty there is nothing to prove. Let p ∈ X with τ(p) > c, and γ a past directed causal curve from p, past
inextendible in X, along which τ > c. Then γ ⊂ L_p. τ is strictly monotone along γ, so it is a piecewise C¹ parameter on
γ, in which, the curve being run towards the future, the tangent lies in {V causal : dτ(V) = 1} over L_p; this set is
compact, as a sequence in it with |V_j|_k → ∞, k a Riemannian metric, would have a normalised limit V, causal with
|V|_k = 1 and dτ(V) = 0. So γ is Lipschitz in τ for the distance of k, and as τ decreases to inf_γ τ it converges in the
compact set L_p: γ extends continuously to its past end point, a contradiction. Hence τ reaches c along every past
inextendible causal curve from p, and every inextendible causal curve through p meets S := {τ = c}, a smooth
hypersurface (dτ ≠ 0) which is acausal (τ is strictly increasing along causal curves). So {τ > c} ⊂ D := D(S).

D is globally hyperbolic with Cauchy hypersurface S. A point q ∈ D with τ(q) > c lies in J⁺_D(S): an inextendible
timelike curve in D through q (the maximal integral curve of −∇τ, which has no zeros) meets S, where τ = c < τ(q), so in
the past of q. Hence supp(w|_D) ⊂ J⁺_D(S), and for x ∈ D, supp(w|_D) ∩ J⁻_D(x) is a closed subset of the compact set
J⁺_D(S) ∩ J⁻_D(x): supp(w|_D) is past compact. On each connected component D_1 of D, which is open and globally
hyperbolic (a causal curve in D starting in D_1 stays in D_1, so the causal sets of D_1 are those of D), [BGP, Theorem
3.1.1] with [BGP, Remark 3.1.3] gives w = 0. So w vanishes on D ⊃ {τ > c} ⊃ supp w, and w = 0. ∎

The compact sets L_p are produced by functions that are monotone along causal curves. Let Ḡ be the dual Minkowski metric
and G_0 that of g_0, time-oriented so that dt_* is past timelike ([[lem:ii-b-1-1]]); let r′_0, C′, C and R̃ be as in
[[lem:ii-c-3-2]] and its proof (R̃ a smooth maximum of r and r′_0, equal to r′_0 for r ≤ r′_0 − 1 and to r for r ≥
r′_0 + 1, with R̃′ ∈ [0, 1]; C ≥ 4, [[lem:ii-e-1-2]] (iv)), and t^♭_* the time function of [[lem:ii-c-3-2]]. For a
smooth θ with values in [0, 1] put G_θ := (1 − θ)G_0 + θḠ on a region where it is Lorentzian.

**Lemma {#lem:ii-f-1-4}** (Monotone functions.) Along future directed causal curves of G_θ:

(a) if θ = 0 on {r ≤ r′_0 + 1}: t_* is non-decreasing; B := t_* + R̃(r) is a time function; and on {r_0 ≤ r ≤ r^♮}, r is
strictly decreasing, so that a past directed causal curve from a point p with r(p) > r_0 stays in {r ≥ min(r(p), r^♮)}.
Consequently, let X be an open set on which G_θ is defined and Lorentzian, τ′ a time function on X with τ′ ≤ t_* on X, c
∈ ℝ, and p ∈ X with τ′(p) > c and r(p) > r_0. Then J⁻_X(p) ∩ {τ′ ≥ c} lies in

    L_p := {q ∈ X : c ≤ τ′(q) ≤ τ′(p), t_*(q) ≤ t_*(p), B(q) ≤ B(p), r(q) ≥ min(r(p), r^♮)},             {#eq:ii-f-lp}

on which c ≤ t_* ≤ t_*(p) and min(r(p), r^♮) ≤ r ≤ max(r′_0 + 1, B(p) − c). If the closure of L_p lies in X, then L_p is
compact, and it is a set as in [[lem:ii-f-1-3]] for τ := τ′ at p. For τ′ = t_* and for τ′ = t^♭_* (where it is a time
function; C′t_* ≤ t^♭_* ≤ t_* by [[lem:ii-c-3-2]] (b)) the condition t_*(q) ≤ t_*(p) in [[eq:ii-f-lp]] may be replaced
by t_*(q) ≤ τ′(p)/C′, with the same conclusions;

(b) if θ = χ(R) with χ as in [[def:ii-f-7-1]], on {t_* > t_1}, where t_1 ≥ r′_0 + 1 is so large that G_χ is Lorentzian
there: t_* is non-decreasing, t = t_* + r is a time function, and so is t^♭_+, defined as C′t on {r ≤ ½Ct_*} and as
t^♭_* on {r ≥ r′_0 + 1}, with C′t_* ≤ t^♭_+ ≤ t_*;

(c) if θ = 1, on ℝ^(1+4): t is a time function, and t_* = t − r and t + r are non-decreasing.

*Proof.* At a point, the past causal cones C_0 of G_0 and C̄ of Ḡ are closed convex cones, so C_0 ∩ C̄ is convex and G_θ
≤ 0 on it. In (a) and (b), θ ∈ (0, 1) only on {r ≥ r′_0 + 1}, and there dt is past timelike for Ḡ and for G_0: by
[[lem:ii-b-1-1]] (1), g_0⁻¹ − ḡ⁻¹ ∈ r⁻²C^∞(M; S²𝒯), so G_0(dt) ≤ −1 + Cr⁻² < 0 for r′_0 large, as in the proof of
[[lem:ii-c-3-2]]. So (C_0 ∩ C̄) ∖ 0, connected and containing the G_θ-timelike dt, lies in the past causal cone of G_θ;
we orient G_θ by it (by dt_* where θ = 0, by dt where θ = 1). A covector in C_0 ∩ C̄ is then ≥ 0 on future causal
vectors of G_θ, and > 0 if it is timelike for G_0 where θ < 1 and for Ḡ where θ > 0. dt_* lies in C_0 ∩ C̄: it is past
timelike for G_0 ([[lem:ii-b-1-1]]), and null for Ḡ with dt_*(V) = V^t − V^r ≥ 0 for Ḡ-future causal V. This gives the
claims on t_*.

(a) dB = (1 − R̃′)dt_* + R̃′dt is past timelike for G_0 everywhere (R̃′ > 0 only on {r ≥ r′_0 − 1}, where dt is) and
equals dt where θ > 0; so B is a time function. θ = 0 on {r_0 ≤ r ≤ r^♮} (r^♮ < r_2 < r′_0), where dr is future timelike
for g_0 ([[lem:ii-c-3-2]] (1) with h = 0), so dr(V) < 0 for future causal V: followed towards the past, r increases
while it lies in (r_0, r^♮], and so cannot pass below min(r(p), r^♮).

For the sets: let q ∈ J⁻_X(p) with τ′(q) ≥ c, reached by a past directed causal curve γ in X from p. Along γ, run
towards the past, τ′ and B decrease, t_* does not increase and r stays ≥ min(r(p), r^♮); so c ≤ τ′(q) ≤ τ′(p), t_*(q) ≤
t_*(p), B(q) ≤ B(p) and r(q) ≥ min(r(p), r^♮), that is q ∈ L_p. On L_p, t_* ≥ τ′ ≥ c; so R̃(r) = B − t_* ≤ B(p) − c, and
as R̃(r) = r for r ≥ r′_0 + 1, r ≤ max(r′_0 + 1, B(p) − c). The closure of L_p in the spacetime therefore lies in the
compact set {c ≤ t_* ≤ t_*(p), min(r(p), r^♮) ≤ r ≤ max(r′_0 + 1, B(p) − c)}; if it lies in X, the four conditions,
which are closed in X, hold on it, so it equals L_p, and L_p is compact. For τ′ = t^♭_*, t_* ≤ t^♭_*/C′ ≤ τ′(p)/C′ on
L_p, which bounds t_* in the same way.

(b) Where θ ∈ (0, 1), 1 < R < 2, so r > t_* > t_1 ≥ r′_0 + 1; where R ≤ 1, G_χ = Ḡ; where R ≥ 2, G_χ = G_0. So dt is
past timelike for G_χ. On {r′_0 + 1 ≤ r ≤ ½Ct_*}, t^♭_* = C′(t_* + R̃(r)) = C′t (the proof of [[lem:ii-c-3-2]]), so the
two definitions of t^♭_+ agree, and the two sets cover {t_* > t_1}. On {r ≤ ½Ct_*}, dt^♭_+ = C′dt; on {r ≥ ½Ct_*} ⊂ {R ≥
2}, G_χ = G_0 and dt^♭_+ = dt^♭_* is past timelike by [[lem:ii-c-3-2]] (2) with h = 0. On {r ≤ ½Ct_*}, C′t_* ≤ C′t ≤
C′(1 + ½C)t_* ≤ t_* (the proof of [[lem:ii-c-3-2]] (b)); on the rest, [[lem:ii-c-3-2]] (b).

(c) For Ḡ-future causal V, V^t ≥ |V^x| ≥ |V^r| (where r is differentiable along the curve, which is almost everywhere),
so dt(V) > 0 and (dt ∓ dr)(V) ≥ 0. ∎
### The semiclassical calculus on ι⁺, and the positive commutator scheme {#sec:ii-f-2}

[Hin26c, Section 10.1.2] runs positive commutator arguments in the semiclassical 0- and cone calculus on ι⁺ and
"leave[s] the statements of standalone propagation estimates to the reader". This section supplies them. The calculus is
a parameterised scaled b.g. calculus ([[sec:ii-a-3]]); the positive commutator scheme of [[sec:i-b-2]]–[[sec:i-b-5]],
proved there for the semiclassical scattering calculus on ℝⁿ, uses of its calculus only a short list of properties, and
each holds here. The one structural difference is that remainders gain only at the semiclassical face sf and in the
differential order, not at the faces 0f, cf, tf; the dictionary (D1)–(D9) below records what changes.

#### The space, the calculus and the orders {#sec:ii-f-2-1}

ι⁺_ħ := ι⁺_(0ħ,cħ) = [[0, 1)_h × ι⁺; {0} × (ι⁺ ∩ K⁺)] ([[sec:ii-a-6-2]]) has four boundary hypersurfaces: sf, the lift
of {h = 0}; tf, the front face; cf, the lift of [0, 1) × (ι⁺ ∩ K⁺); and 0f, the lift of [0, 1) × (ι⁺ ∩ ℐ⁺). With ρ_K =
R/(1 + R) as in [[sec:ii-f-1-1]] we use the defining functions

    ρ_sf := h/(h + ρ_K),    ρ_tf := h + ρ_K,    ρ_cf := ρ_K/(h + ρ_K),    ρ_0f := (1 + R)^(−1/2).   {#eq:ii-f-2-1}

ρ_0f = x_I(1 + x_I²)^(−1/2) near ι⁺ ∩ ℐ⁺. Near sf ∩ tf the functions ĥ := h/R and R are local defining functions of sf
and tf, and ρ_sf/ĥ = (R/ρ_K)·(1 + ĥR/ρ_K)⁻¹ is smooth and positive, equal to 1 at ĥ = R = 0; near sf ∩ 0f, h and x_I
are, and ρ_sf/h, ρ_0f/x_I are smooth and positive, equal to 1 at h = x_I = 0. The face sf is a copy of ι⁺: the centre
{0} × (ι⁺ ∩ K⁺) of the blow-up is a boundary hypersurface of {0} × ι⁺, and blowing one up does not change a manifold
with corners.

*The structure.* By [[sec:ii-a-6-2]] ([Hin26c, Section 3.2.4]), for h ∈ (0, 1] the semiclassical 0- and cone structure
is the parameterised scaled b.g. structure (S7) of [[sec:ii-a-3]] on (ι⁺)°, with the cells U_(2,jk±), U_(3,jk±) of
[[sec:ii-a-6-2]] (and finitely many cells covering a compact subset of (ι⁺)°), the coefficient Lie algebra C^∞_b𝒱_b(ι⁺),
which does not depend on h, and the scalings (1 + ρ_K|σ|)⁻¹, resp. (⟨σ⟩⁻¹, x_I⟨σ⟩⁻¹) at |σ| = h⁻¹: up to factors bounded
above and below, h/(h + 2^(−j)) in every direction on U_(2,jk±), h in x_I and 2^(−j)h in ω on U_(3,jk±), and h on the
interior cells. Its operator Lie algebra 𝒱_ħ is spanned over C^∞_b(ι⁺), uniformly in h, by (h/(h + ρ_K))ρ_K∂_(ρ_K) and
(h/(h + ρ_K))∂_ω near ι⁺ ∩ K⁺, by hx_I∂_(x_I) and hx_I∂_ω near ι⁺ ∩ ℐ⁺, and by h𝒱(ι⁺) in between.

**Lemma {#lem:ii-f-2-1}** (a) The scaling weight ρ̄ of this structure ((S1) of [[sec:ii-a-3]]) satisfies C⁻¹ρ_sf ≤ ρ̄ ≤
Cρ_sf with C independent of h. (b) For a, c, l ∈ ℝ, ρ_0f^a ρ_cf^c ρ_tf^l and ρ_sf are weights in the sense of (S2),
uniformly in h. (c) P_(ι,h,z) ∈ ρ_0f²ρ_cf⁻²Diff²_(𝒱_ħ), with coefficients affine in z and bounded uniformly for |z| ≤ 2
and h ∈ (0, 1].

*Proof.* (a) On U_(2,jk±), ρ_K ∈ (2^(−j−2), 2^(−j+2)), so h/(h + 2^(−j)) and ρ_sf agree up to a factor in [¼, 4]. On
U_(3,jk±) the largest scaling is h, and ρ_K ∈ [½, 1] there, so h ≤ 2ρ_sf ≤ 2h; likewise on the interior cells. (b) Note
ρ_cf = ρ_K/(h + ρ_K) ∈ [0, 1]. Then ρ_K∂_(ρ_K) log ρ_tf = ρ_cf, ρ_K∂_(ρ_K) log ρ_cf = 1 − ρ_cf, ρ_K∂_(ρ_K) log ρ_sf =
−ρ_cf and ρ_K∂_(ρ_K)ρ_cf = ρ_cf(1 − ρ_cf), so every derivative of the logarithms of these functions along C^∞_b𝒱_b(ι⁺)
is a polynomial in ρ_cf with coefficients bounded uniformly in h; log ρ_0f is log x_I plus a smooth function near ℐ⁺,
and x_I∂_(x_I) log x_I = 1. So Ww/w ∈ C^∞_uni uniformly for each of these w and every W in the coefficient Lie algebra.
(c) Near ι⁺ ∩ K⁺ (where we may use R in place of ρ_K, the two being smooth multiples of each other) put V_1 := (h/(h +
R))R∂_R and V_ω := (h/(h + R))∂_ω. Then hR∂_R = (h + R)V_1, R⁻¹(h + R) = ρ_cf⁻¹ and R⁻¹h = ρ_sfρ_cf⁻¹ up to smooth
positive factors, and V_1(h + R) = ρ_sfR; so in [[eq:ii-f-1-12]], R⁻¹(iz + hR∂_R) ∈ ρ_cf⁻¹Diff¹_(𝒱_ħ), hR∂_R + h(c +
S_0) ∈ Diff¹_(𝒱_ħ) and h²R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω) ∈ ρ_cf⁻²Diff²_(𝒱_ħ). Near ι⁺ ∩ ℐ⁺, [[eq:ii-f-1-11]] is x_I² times a
polynomial of degree 2 in hx_I∂_(x_I), hx_I∂_ω with coefficients bounded uniformly (h²x_I²(x_I∂_(x_I))² =
x_I²(hx_I∂_(x_I))², h²x_I²∂_ω² = (hx_I∂_ω)², h²x_I²∂_ω = hx_I·hx_I∂_ω). ∎

*Orders and spaces.* An *order* is 𝐨 = (𝗌; a, c, l; 𝖻): a, c, l ∈ ℝ are the weights at 0f, cf and tf, and 𝗌 (the
differential order) and 𝖻 (the order at sf) are smooth functions on the fibre-radially compactified phase space
^(0ħ,cħ)T̄*ι⁺_ħ of the structure, variable orders in the sense of (S8). Put

    w_𝐨 := ⟨ζ⟩^𝗌 ρ_0f^(−a) ρ_cf^(−c) ρ_tf^(−l) ρ_sf^(−𝖻),    𝐞 := (1; 0, 0, 0; 1),    𝐞_1 := (1; 0, 0, 0; 0),
    𝐦 := (2; −2, 2, 0; 0),                                                                                {#eq:ii-f-2-2}

⟨ζ⟩ the fibre weight of the structure. Ψ^𝐨 is the class of (S4)–(S5) and (S8) with the weight
ρ_0f^(−a)ρ_cf^(−c)ρ_tf^(−l), differential order 𝗌 and decay order 𝖻 at the scaling weight ρ̄ ≍ ρ_sf ([[lem:ii-f-2-1]]),
acting on ℂ^(N_E)-valued functions componentwise, and taken in the subalgebra of (S10); S^𝐨 is its symbol class. H^𝐨 :=
ρ_0f^a ρ_cf^c ρ_tf^l ρ_sf^𝖻 H^𝗌_ħ, with norm ‖·‖_𝐨, is the space H^(𝗌,(a,c,l,𝖻))_(0ħ,cħ,h)(ι⁺) of [[sec:ii-a-6-2]] and
[Hin26c, (3.56)], with L² := L²(ι⁺, μ_b; ℂ^(N_E)) for the b-density μ_b of [[sec:ii-f-1-1]] and a fibre inner product 𝔢
on ℂ^(N_E), smooth on ι⁺; adjoints A* and the parts Re A := ½(A + A*), Im A := (1/2i)(A − A*) are taken in this L². By
[[lem:ii-f-2-1]] (c), P_(ι,h,z) ∈ Ψ^𝐦. Orders are compared componentwise; 𝐨 − K𝐞 lowers the differential and sf orders
by K and keeps the weights. For fixed h > 0, H^𝐨 is the space H^(𝗌,(a,c))_(0,b)(ι⁺) with an h-dependent equivalent norm
([Hin26c, after (10.31)]): ρ_sf and ρ_tf are then bounded above and below, and ρ_cf ≍ ρ_K.

*Phase space.* 𝒫_ι := ^(0ħ,cħ)T̄*_(sf)ι⁺_ħ ∪ ^(0ħ,cħ)S*ι⁺_ħ is the fibre-compactified phase space over sf together with
fibre infinity over all of ι⁺_ħ; it is compact. The part over sf is a manifold with corners whose boundary hypersurfaces
are fibre infinity, F_I (over sf ∩ 0f = {x_I = 0}) and F_K (over sf ∩ tf = {R = 0}); F_I ∩ F_K = ∅. On it we use the
semiclassical 0-covectors ξ dx_I/(hx_I) + η dω/(hx_I) near F_I and the semiclassical cone covectors of [[sec:ii-f-1-3]]
near F_K, over sf ξ_cħ dR/h + η_cħ R dω/h. WF′(A) and Ell(A) ⊂ 𝒫_ι are defined as in [[def:i-b-2-9]], with S^(−K𝐞) in
place of S^(−K𝟏): ϖ ∉ WF′(A) if the symbol of A lies in S^(−K𝐞) on a neighbourhood of ϖ in ^(0ħ,cħ)T̄*ι⁺_ħ for every K.
The principal symbol of A ∈ Ψ^𝐨 is its symbol modulo S^(𝐨−(1−ϵ)𝐞), ϵ > 0 small (S8); over sf at finite frequencies it is
determined by its restriction to 𝒫_ι, as a symbol w_𝐨a with a smooth and vanishing at sf lies in S^(𝐨−(0;0,0,0;1)),
which at finite frequencies is S^(𝐨−𝐞).

**Lemma {#lem:ii-f-2-2}** (The calculus.) Uniformly for h ∈ (0, 1]:

(a) A ∈ Ψ^(𝐨′) maps H^𝐨 → H^(𝐨−𝐨′) with norm bounded by a seminorm of A.

(b) Ψ^𝐨Ψ^(𝐨′) ⊂ Ψ^(𝐨+𝐨′) with multiplicative principal symbols; (Ψ^𝐨)* ⊂ Ψ^𝐨, the principal symbol of A* being the
𝔢-adjoint of that of A; and if A ∈ Ψ^𝐨, B ∈ Ψ^(𝐨′) have scalar principal symbols, A − Op(a Id) ∈ Ψ^(𝐨−(1−ϵ)𝐞) and B −
Op(b Id) ∈ Ψ^(𝐨′−(1−ϵ)𝐞), then i[A, B] − Op(H_a b Id) ∈ Ψ^(𝐨+𝐨′−(2−2ϵ)𝐞), where H_a is the Hamilton field of the
canonical symplectic form of T*(ι⁺)° and H_a b ∈ S^(𝐨+𝐨′−(1−ϵ)𝐞).

(c) (Elliptic estimate.) If A ∈ Ψ^(𝐦′), B, G ∈ Ψ⁰ and WF′(B) ⊂ Ell(A) ∩ Ell(G), then ‖Bu‖_𝐨 ≤ C(‖GAu‖_(𝐨−𝐦′) +
‖u‖_(𝐨−K𝐞)) for every K.

(d) [[lem:i-b-2-2]] holds for the classes S^𝐨, with the gains (|β|, |α|, 0) of its (d) replaced by |β|𝐞_1 for fibre
derivatives and 0 for derivatives along the coefficient Lie algebra; a smooth function of finitely many symbols in S⁰,
defined on a neighbourhood of the closure of their joint range, lies in S⁰.

(e) [[lem:i-b-2-12]] holds with L_h replaced by L := 1 + log⟨ζ⟩ + log ρ_sf⁻¹.

(f) (Localisation near sf.) (i) If a ∈ S^𝐨 is supported in {ρ_sf ≥ δ_s, |ζ| ≤ C_0}, then a ∈ S^(𝐨−K𝐞) for every K, with
seminorms bounded by C_Kδ_s^(−K) times seminorms of a. (ii) Let χ_0 ∈ C^∞(ℝ), χ_0 = 1 on (−∞, 1], χ_0 = 0 on [2, ∞), and
φ := χ_0(ρ_sf/δ_s). For δ ∈ (0, 1], every order 𝐭 and every K there is C, independent of δ_s ∈ (0, ⅛], with ‖φv‖_(𝐭−δ𝐞)
≤ Cδ_s^δ‖v‖_𝐭 + C‖v‖_(𝐭−K𝐞).

(g) (Density.) For fixed h > 0, z and orders 𝐨, C^∞_c((ι⁺)°) is dense in {u ∈ H^𝐨 : P_(ι,h,z)u ∈ H^(𝐨−𝐦+𝐞)} with the
graph norm, and likewise for P*_(ι,h,z) and the orders −𝐨 + 𝐦 − 𝐞.

*Proof.* (a) is (S5) with (S7), (S8) and (S11), the weights by [[lem:ii-f-2-1]] (b) and the decay order at ρ̄ ≍ ρ_sf by
[[lem:ii-f-2-1]] (a). The density μ_b is ρ̄⁴ρ_0f³ times a uniformly positive 𝒱_ħ-density: near cf the scalings multiply
to ρ̄⁴ up to bounded factors, as dim ι⁺ = 4, and near 0f the density dual to hx_I∂_(x_I), hx_IZ_a is h⁻⁴x_I⁻³μ_b, with h
∼ ρ_sf there. So L²(μ_b) is ρ_sf⁻²ρ_0f^(−3/2) times the L² space of (S3), up to an equivalent norm: a constant shift of
the sf order and of the 0f weight, both weights by [[lem:ii-f-2-1]] (b).

(b) is (S5) and (S8): the principal symbol is taken modulo ⋂_δ ρ̄^(−𝖻+1−2δ)S^(𝗌−1+2δ), and σ(i[A_1, A_2]) =
H_(σ(A_1))σ(A_2). Adjoints with respect to μ_b and 𝔢 differ from those of (S5) (the 𝒱_ħ-density and the Euclidean inner
product) by conjugation with the weight ρ_sf⁻⁴ρ_0f⁻³ and with the matrix of 𝔢, which preserve Ψ^𝐨 and the principal
symbol, by (b) itself and [[lem:ii-f-2-1]] (b). For the commutators, with A′ := A − Op(a Id) and B′ := B − Op(b Id):
[Op(a Id), Op(b Id)] is a commutator of scalar operators acting componentwise, with principal symbol −iH_a b (S5); [Op(a
Id), B′] and [A′, Op(b Id)] are, entry by entry, commutators of scalar operators, so gain (1 − ϵ)𝐞 beyond the product
order 𝐨 + 𝐨′ − (1 − ϵ)𝐞; and A′B′, B′A′ are each of order 𝐨 + 𝐨′ − (2 − 2ϵ)𝐞. In the scaled charts, H_a = Σ_i
ρ̄_i(∂_(ξ_i)a ∂_(x^i) − ∂_(x^i)a ∂_(ξ_i)), with ρ̄_i ≤ ρ̄ the scalings and (x, ξ) the chart coordinates of (S4), whence
H_a b ∈ S^(𝐨+𝐨′−𝐞).

(c) is the microlocal elliptic estimate of (S5), with (S8) for variable orders, localised by the composition calculus as
in the proof of [[prop:i-b-2-10]].

(d) The proof of [[lem:i-b-2-2]] uses only the form log w_𝐨 = 𝗌 log⟨ζ⟩ + … + 𝖻 log ρ_sf⁻¹ and the chain rule;
derivatives along the coefficient Lie algebra of log ρ_F are bounded ([[lem:ii-f-2-1]] (b)), and fibre derivatives of
log⟨ζ⟩ gain ⟨ζ⟩⁻¹. A smooth function of S⁰ symbols is in S⁰ by the chain rule.

(e) The proof of [[lem:i-b-2-12]] uses (d) and the Cauchy formula only; (S8) admits the logarithmic factors.

(f) (i) On the support, w_(𝐨−K𝐞)/w_𝐨 = ⟨ζ⟩^(−K)ρ_sf^K ≥ (1 + C_0)^(−K)δ_s^K, and the derivatives are handled by (d).
(ii) φ is a function on ι⁺ depending on h whose derivatives along C^∞_b𝒱_b(ι⁺) are bounded uniformly in h and δ_s (on
supp χ_0′(ρ_sf/δ_s), ρ_sf/δ_s ∈ [1, 2], and the derivatives of log ρ_sf are bounded by [[lem:ii-f-2-1]] (b)); so φ ∈ S⁰
with seminorms uniform in δ_s, and Op(φ) is multiplication by φ, the quantisation of (S4) being a left quantisation with
ψ(0) = 1. Let φ_1 := χ_0(ρ_sf/(2δ_s)), which is 1 on supp φ, is supported in {ρ_sf ≤ 4δ_s} and has the same uniformity.
With W_𝐭 := Op(w_𝐭) and φ_1φ = φ,

    W_(𝐭−δ𝐞)φv = ρ_sf^δφ_1·W_(𝐭−δ𝐞)ρ_sf^(−δ)φv + T′φv,      T′ := [W_(𝐭−δ𝐞), ρ_sf^δφ_1]ρ_sf^(−δ).

Multiplication by ρ_sf^δφ_1 has L² norm at most (4δ_s)^δ; W_(𝐭−δ𝐞)ρ_sf^(−δ)φ ∈ Ψ^(𝐭−δ𝐞_1) maps H^𝐭 to L² with norm C by
(a); and T′ ∈ Ψ^(𝐭−(δ+1−ϵ)𝐞) by (b), as ρ_sf^δφ_1 ∈ S^((0;0,0,0;−δ)) and ρ_sf^(−δ) ∈ S^((0;0,0,0;δ)); all seminorms are
uniform in δ_s. So ‖φv‖_(𝐭−δ𝐞) ≤ C(4δ_s)^δ‖v‖_𝐭 + C‖φv‖_(𝐭′−𝐞), 𝐭′ := 𝐭 − (δ − ϵ)𝐞 ≤ 𝐭 after decreasing ϵ < δ. The same
inequality with δ = 1 at the order 𝐭′ bounds the last norm by C(4δ_s)‖v‖_𝐭 + C‖φv‖_(𝐭′−(2−ϵ)𝐞); after m ≥ K/(1 − ϵ) such
steps what remains is C‖φv‖_(𝐭−K𝐞) ≤ C‖v‖_(𝐭−K𝐞), and 4δ_s ≤ (4δ_s)^δ as 4δ_s ≤ 1.

(g) For fixed h, P_(ι,h,z) = h²N⁰(h⁻¹z) is elliptic in x_I²ρ_K⁻²Diff²_(0,b)(ι⁺) ([[sec:ii-f-1-3]]), and the spaces are
weighted 0,b-Sobolev spaces with fixed weights. Let J_ϵ ∈ Ψ^(−∞)_(0,b), ϵ ∈ (0, 1], be uniformly bounded in Ψ⁰_(0,b),
with J_ϵ → I strongly on every weighted 0,b-Sobolev space and [N⁰(σ), J_ϵ] uniformly bounded in x_I²ρ_K⁻²Ψ¹_(0,b) and
tending to 0 in x_I²ρ_K⁻²Ψ^(1+δ)_(0,b) (quantisations of χ(ϵ|ζ|), (S5)); and let χ_j := χ_0(−j⁻¹ log ρ_K)χ_0(−j⁻¹ log
x_I), whose b-, resp. 0-derivatives are O(j⁻¹), so that [N⁰(σ), χ_j] tends to 0 in x_I²ρ_K⁻²Diff¹_(0,b) with uniformly
bounded coefficients. Then u_(j,ϵ) := χ_jJ_ϵu ∈ C^∞_c((ι⁺)°) converges to u in the graph norm as ϵ → 0 and then j → ∞,
as in the proof of [[lem:i-b-3-1]]; the weights x_I^aρ_K^c commute with χ_j and conjugate J_ϵ into a family with the
same properties. ∎

#### The positive commutator scheme {#sec:ii-f-2-2}

*Dictionary.* [[sec:i-b-2]]–[[sec:i-b-5]] are written for the semiclassical scattering calculus. We read them in the
semiclassical calculus on ι⁺ with the following replacements.

(D1) The phase space 𝒫 is 𝒫_ι; "Schwartz u" is u ∈ C^∞_c((ι⁺)°), and estimates proved for such u extend to the graph
spaces of [[lem:ii-f-2-2]] (g), every term being continuous there.

(D2) Orders (s, 𝗋, 𝖻) are orders 𝐨 as above, with w_𝐨 from [[eq:ii-f-2-2]]; 𝟏 is 𝐞; 𝐦 is [[eq:ii-f-2-2]]; "Ψ⁰" means
Ψ^((0;0,0,0;0)).

(D3) The commutator carries no factor h⁻¹: [[eq:i-b-3-1]] is replaced by

    2 Im⟨ǍPu, Ǎu⟩ = ⟨Cu, u⟩,      C := i[Re P, Ǎ²] + Ǎ² Im P + Im P Ǎ²,                                  {#eq:ii-f-2-3}

the gain (1, 1, 0) of h⁻¹[·, ·] is 𝐞, so [[eq:i-b-3-2]] becomes 𝐤 := 𝐨 − ½(𝐦 − 𝐞), and every term h⁻¹‖GPu‖_(𝐨−𝐦+(1,1,0))
becomes ‖GPu‖_(𝐨−𝐦+𝐞). In [[eq:i-b-4-3]] and [[lem:i-b-5-1]] (ii) the decomposition of h⁻¹Im_h 𝐏 as ε_♭(𝒫_1 − ℓ𝒜)
becomes Im 𝐏 = ε_♭(𝒫_1 − ℓ𝒜), with 𝒫_1 ∈ Ψ^(𝐦−𝐞), ℓ ∈ [0, 2] a constant and 𝒜 ∈ Ψ^(𝐦−𝐞_1) (in [[ch:s02]], ℓ ∈ [0, 2h⁻¹]
and 𝒜 is one order h⁻¹ above 𝒫_1; here 𝒜 is one order ρ_sf⁻¹ above).

(D4) The residual error ‖u‖_(−K𝟏) is ‖u‖_(𝐨−K𝐞) (the weights at 0f, cf, tf are never lowered).

(D5) Iteration lowers all of 𝐨: in place of [[lem:i-b-3-4]], which lowers only the semiclassical order, the iteration of
[[cor:i-b-4-6-prime]] (the form of [[cor:i-b-4-6]] with all orders lowered) is used, applying
[[lem:i-b-3-3]] at the orders 𝐨 − ((J − j)/4)𝐞, j = 1, …, J; it needs the decomposition [[eq:i-b-3-3]] at each of these
orders, on the same nested sets, and leaves the error ‖Gu‖_(𝐨−(J/4)𝐞) in place of h^M‖Gu‖_𝐨. The constant semiclassical
scaling used in [[sec:i-b-3-3]] is not available here: ρ_sf is not constant on ι⁺ at fixed h.

(D6) The rescaled Hamilton field is 𝖧 := w_(𝐦−𝐞)⁻¹H_(Re G_(ι,z)) in place of μ⁻¹H, so that w_(𝐦−𝐞)w_𝐤² = w_(2𝐨), as
μw_𝐤² = w_(2𝐨) in [[ch:s02]]. It is a smooth vector field on ^(0ħ,cħ)T̄*ι⁺_ħ near 𝒫_ι, tangent to sf, to fibre infinity
and to the lifts of 0f and tf (its component along ρ_sf is ρ_sf𝖧 log ρ_sf, as H acts at fixed h); [[lem:i-b-4-1]] (c) is
replaced by this statement, which is checked in [[sec:ii-f-3-2]].

(D7) Logarithms: log w_𝐤 = 𝗌_𝐤 log⟨ζ⟩ + k_0f log ρ_0f⁻¹ + k_cf log ρ_cf⁻¹ + k_tf log ρ_tf⁻¹ + 𝖻_𝐤 log ρ_sf⁻¹. In the
proofs of [[prop:i-b-4-5]] and [[lem:i-b-5-1]], the term 2(𝗋 + ½)ς𝖧 log⟨x⟩ of β becomes 2Σ_F k_Fς𝖧 log ρ_F⁻¹ + 2𝖻_𝐤ς𝖧
log ρ_sf⁻¹ (the sum over 0f, cf, tf), smooth near 𝒫_ι by (D6); the weights a, c, l are constants, so the term (𝖧𝗋)
log⟨x⟩ and the nonnegative term built from it in the proof of [[prop:i-b-4-5]] are absent; and log(1/h) is log ρ_sf⁻¹,
so the nonnegative term built from 𝖻 there becomes −2χ̃(ς𝖧𝖻) log ρ_sf⁻¹ ≥ 0, which satisfies the hypotheses of
[[lem:ii-f-2-2]] (e).

(D8) The principal symbol G_(ι,z) of P_(ι,h,z) is affine in z ([[eq:ii-f-1-13]]), so the field of Re G_(ι,z) depends
only on Re z: 𝖧_z = 𝖧_(Re z) in [[eq:i-b-4-1]], and the term c_b of [[prop:i-b-4-5]] vanishes.

(D9) (Localisation near sf.) Every commutant is multiplied by φ = χ_0(ρ_sf/δ_s), with δ_s ∈ (0, ⅛] fixed small; so every
commutant is supported in {ρ_sf ≤ 2δ_s}, where the functions used to build it need only be defined. Near F_I and over
compact subsets of the interior of sf, ρ_sf ≤ 2h, so φ = 1 there once h < δ_s/2. The new terms in 2φ ς𝖧φ produced by
χ_0′ are supported in {δ_s ≤ ρ_sf ≤ 2δ_s} at finite frequencies, and, whatever their sign, contribute at most
C_(δ_s)‖u‖²_(𝐨−K𝐞), by [[lem:ii-f-2-2]] (f) (i) and (a). Where [[ch:s02]] absorbs a term because it carries a positive
power of h (the middle term in *Positivity of absorbing terms*, [[sec:i-b-3-3]]), [[lem:ii-f-2-2]] (f) (ii) is used
instead, with δ_s small. Constants below depend on δ_s.

**Proposition {#prop:ii-f-2-3}** (Transfer.) Under (D1)–(D9), the following statements of [[ch:s02]] hold for the
semiclassical calculus on ι⁺, for every family of operators 𝐏 in Ψ^𝐦 with real scalar principal symbol for Re 𝐏,
uniformly for the parameters in compact sets as there, with the proofs given there: [[prop:i-b-2-10]] (with
[[lem:ii-f-2-2]] (c)), [[lem:i-b-2-11]] and [[lem:i-b-2-12]], [[lem:i-b-3-2]] and the paragraph after it,
[[lem:i-b-3-3]], the iteration of (D5), the paragraph *Positivity of absorbing terms* of [[sec:i-b-3-3]] (with (D9)),
[[lem:i-b-4-3]] and [[lem:i-b-4-4]], [[prop:i-b-4-5]] with [[rem:i-b-4-7]], [[cor:i-b-4-6]] and its form with all orders
lowered, and [[lem:i-b-5-1]].

*Proof.* The proofs in [[ch:s02]] use of the calculus: the mapping property ([[prop:i-b-2-8]]), the composition and
adjoint theorems with the principal symbols of products, adjoints and commutators ([[thm:i-b-2-4]], [[thm:i-b-2-5]] and
[[eq:i-b-2-5]]), the elliptic estimate ([[prop:i-b-2-10]]), the symbol properties of [[lem:i-b-2-2]], the square roots
of [[lem:i-b-2-11]] and [[lem:i-b-2-12]], and the L² pairing of H^𝐨 with H^(−𝐨). These are [[lem:ii-f-2-2]] (a)–(e)
here, the pairing being (S3) and (S11) with the weight shift of the proof of [[lem:ii-f-2-2]] (a). [[lem:i-b-4-3]] and
[[lem:i-b-4-4]] are statements about vector fields on a manifold with corners of codimension at most 2 and about one
function of one variable; 𝒫_ι over sf has codimension at most 2 (F_I ∩ F_K = ∅). The remainder classes of [[ch:s02]] are
of the form Ψ^(2𝐨−θ𝟏+ϵ𝟏), θ ∈ {½, 1}; here they are Ψ^(2𝐨−θ𝐞+ϵ𝐞), by [[lem:ii-f-2-2]] (b) with (D3), and every place
where [[ch:s02]] bounds such a remainder uses only its order in the scale 𝟏, now 𝐞, against the error ‖Gu‖_(𝐨−¼𝐞), which
the iteration (D5) carries down to ‖Gu‖_(𝐨−(J/4)𝐞). Two places use more. (1) In *Positivity of absorbing terms* the
middle term C‖Ǎw‖²_(𝐭−½(1−ϵ)𝐞) is bounded, after the factor φ of (D9) is put into Ǎ (so that (1 − φ_1)Ǎ is residual,
φ_1 = χ_0(ρ_sf/(2δ_s))), by C(C_1(2δ_s)^((1−ϵ)/2)‖Ǎw‖_𝐭 + C_2‖Ǎw‖_(𝐭−K𝐞))² ([[lem:ii-f-2-2]] (f) (ii) applied to φ_1Ǎw);
for δ_s small the first part is absorbed by (c/2)‖Ǎw‖²_𝐭, and the second is bounded by C‖Gw‖²_(𝐤+𝐭−K𝐞). With ℓ ≤ 2 (D3),
⟨Fw, w⟩ ≥ −C‖Gw‖²_(𝐤+𝐭−K𝐞), which is of the class of the residual errors for K large. (2) In [[prop:i-b-4-5]] and
[[lem:i-b-5-1]] the semiclassical weight h^(−𝖻) is a constant on phase space at fixed h; here ρ_sf^(−𝖻) is not, and its
derivative along 𝖧 is the term 2𝖻_𝐤ς𝖧 log ρ_sf⁻¹ of (D7), smooth near 𝒫_ι: it is part of β, bounded on U_1 in
[[prop:i-b-4-5]] (absorbed by M there) and evaluated at the radial set in [[lem:i-b-5-1]], exactly as the term with
log⟨x⟩ is in [[ch:s02]]. Nothing else in those proofs depends on 𝖻 being multiplied by a constant. ∎

We state the consequences used in [[sec:ii-f-3]] and [[sec:ii-f-4]]. Let Z ⊂ {|z| ∈ [½, 2]} be compact, c_z ∈ {1, z⁻¹},
J ≥ 1, and P′ := P_(ι,h,z) ⊗ Id_(ℂ^J) + P″ with P″ ∈ Ψ^(𝐦−𝐞) (acting on ℂ^(N_E) ⊗ ℂ^J, with the fibre inner product
𝔢^(⊕J)), continuous in z; let 𝐏 be one of c_zP′, (c_zP′)*, with ε_♭ := 1, resp. −1. (P″ = 0 and J = 1 in
[[sec:ii-f-3]].)

**Proposition {#prop:ii-f-2-4}** (Radial estimate; [[lem:i-b-5-1]].) Let F ∈ {F_I, F_K} with defining function ϱ (x_I,
resp. R) on 𝒫_ι, Z′ ⊂ Z compact, Λ ⊂ F compact, U_0 ⊂ 𝒫_ι a neighbourhood of Λ at finite frequencies with compact
closure, and ς ∈ {1, −1}. Suppose, uniformly for z ∈ Z′:

(i) Re 𝐏 − Op(p_z Id) ∈ Ψ^(𝐦−𝐞) with p_z real and continuous in z; 𝖧^𝐏_z := w_(𝐦−𝐞)⁻¹H_(p_z) vanishes on Λ; and β_ϱ :=
ϱ⁻¹ς𝖧^𝐏_zϱ satisfies β_ϱ ≥ β_* on U_0 (*ϱ-source*) or β_ϱ ≤ −β_* on U_0 (*ϱ-sink*), β_* > 0.

(ii) Im 𝐏 = ε_♭(𝒫_1 − ℓ𝒜) as in (D3), 𝒫_1 self-adjoint with principal symbol p_1, and either (A) ε_♭ς𝒜 is self-adjoint
with principal symbol ≥ c_0w_(𝐦−𝐞_1) Id on U_0; or (B) ε_♭ς = 1 and 𝒜 = Σ_(j,k) W_j*M̃_(jk)W_k + 𝒜_0 + 𝒜_1 with W_j ∈
Diff¹_(𝒱_ħ) scalar, acting componentwise, M̃ = (M̃_(jk)) ≥ 0 and 𝒜_0 ≥ 0 matrix functions (for 𝔢^(⊕J), resp. 𝔢,
pointwise), and 𝒜_1 a differential operator whose coefficients vanish near the base projection of Ū_0.

(iii) There are real g, ϕ, smooth near 𝒫_ι and continuous in z, ϕ ≥ 0, with Λ = Ū_0 ∩ {ϱ = 0, ϕ = 0, g = 0}, |w_𝐦⁻¹𝐠_z|
≥ c|g| − Cϱ on U_0 (𝐠_z the principal symbol of 𝐏), and, on U_0, either ς𝖧^𝐏_zϕ ≥ c_1ϕ − C_1(ϱ + g²) (*ϕ-source*) or
ς𝖧^𝐏_zϕ ≤ −c_1ϕ + C_1(ϱ + g²) (*ϕ-sink*).

(iv) 𝖻 is constant on U_0. Let κ̃ be the exponent with w_𝐤 = ϱ^(−κ̃)f near Λ, f > 0 smooth near Λ up to a factor
depending on h only (κ̃ = k_0f = a + 1 at F_I, where ρ_sf ≍ h; κ̃ = k_tf − 𝖻_𝐤 = l − 𝖻 − ½ at F_K, where
ρ_tf^(−k_tf)ρ_sf^(−𝖻_𝐤) = R^(𝖻_𝐤−k_tf)h^(−𝖻_𝐤) times a smooth positive factor).

(v) (Threshold.) On Λ, 𝒯 := 2κ̃β_ϱ Id − 2ςε_♭w_(𝐦−𝐞)⁻¹p_1 ≥ c_𝒯 Id, c_𝒯 > 0.

Then for every J ∈ ℕ such that (iv)–(v) also hold with 𝖻 replaced by 𝖻 − j/4, 0 ≤ j ≤ J − 1 (only 𝖻 moves κ̃, and only
at F_K; for J = 1 this is no further condition), there are a neighbourhood U_* of Λ and a compact K_E ⊂ Ū_0 ∖ Λ such
that for B_* microsupported in U_*, G elliptic on Ū_0, E′ elliptic on K_E, all K, z ∈ Z′, h < h_0 and u ∈ C^∞_c((ι⁺)°),

    ‖B_*u‖_𝐨 ≤ C(‖G𝐏u‖_(𝐨−𝐦+𝐞) + δ‖E′u‖_𝐨 + ‖Gu‖_(𝐨−(J/4)𝐞) + ‖u‖_(𝐨−K𝐞)),                         {#eq:ii-f-2-4}

with δ := 0 if the ϱ-part and the ϕ-part of Λ are both sources, and δ := 1 otherwise; K_E lies in {ϱ ≥ δ_1} when only
the ϱ-part is a sink, and in {ϕ ≥ δ_2} when only the ϕ-part is.

*Proof.* This is [[lem:i-b-5-1]] under the dictionary ([[prop:ii-f-2-3]]), with one generalisation: there the ϱ-part and
the ϕ-part are both sources or both sinks; here they may differ. In that proof the derivative of the cut-off is k_1 +
k_2 + k_3, and k_1 (from χ_0(ϱ/δ_1)) has the sign of −β_ϱϱ, k_2 (from χ_0(ϕ/δ_2)) that of ∓1, each on its own support;
each is written as −f_i² or e_i² according to its own sign, with the same square roots. The threshold uses only β_ϱ (the
derivative of w_𝐤 at Λ, where 𝖧^𝐏_z vanishes), so (v) is unchanged; the sets carrying e_i are supp k_i, closed and
disjoint from Λ. The iteration (D5) needs the commutant at each order 𝐨 − ((J − j)/4)𝐞, 1 ≤ j ≤ J, that is at 𝖻 − i/4, 0
≤ i ≤ J − 1: the cut-offs do not depend on the order, 𝗌 does not enter at finite frequencies, and the threshold at the
lowered orders is the hypothesis on J. ∎

**Proposition {#prop:ii-f-2-5}** (Propagation; [[prop:i-b-4-5]], [[cor:i-b-4-6]] and [[rem:i-b-4-7]].) Let ς be a sign,
z_* ∈ Z, and γ : [−T, 0] → 𝒫_ι an integral curve of ς𝖧_(z_*), at finite frequencies, on which 𝖧_(z_*) ≠ 0, where 𝖧_z :=
w_(𝐦−𝐞)⁻¹H_(Re(c_zG_(ι,z))). Let U_0 be a neighbourhood of γ([−T, 0]) on which ς𝖧_z𝖻 ≤ 0 for z ∈ Z. Suppose Im 𝐏 =
ε_♭(𝒫_1 − ℓ𝒜) as in (D3) with either |ℓ| ≤ Ch (then ℓ𝒜 ∈ Ψ^(𝐦−𝐞), as h ≤ 2ρ_sf, and is part of 𝒫_1), or (A) of
[[prop:ii-f-2-4]] on U_0, or (B) of [[prop:ii-f-2-4]] on U_0. Then for every neighbourhood W of γ(−T) there are a
neighbourhood Z_0 of z_* in Z, a neighbourhood U_* of γ(0) and a compact K_E ⊂ W such that for all J, K, B_*
microsupported in U_*, E′ elliptic on K_E, G elliptic on Ū_0, z ∈ Z_0, h < h_0 and u ∈ C^∞_c((ι⁺)°),

    ‖B_*u‖_𝐨 ≤ C(‖G𝐏u‖_(𝐨−𝐦+𝐞) + ‖E′u‖_𝐨 + ‖Gu‖_(𝐨−(J/4)𝐞) + ‖u‖_(𝐨−K𝐞)).                              {#eq:ii-f-2-5}

*Proof.* [[prop:i-b-4-5]], [[cor:i-b-4-6]] and its form with all orders lowered, under the dictionary; [[rem:i-b-4-7]]
(a) for |ℓ| ≤ Ch and (b) for case (B). In case (A) the hypothesis ε_♭ςq̂_(z_*) > 0 of [[prop:i-b-4-5]] is the positivity
in (A). By (D8), 𝖧_z depends on z only through Re z when c_z = 1; when c_z = z⁻¹ it is a polynomial in Re z⁻¹ and Im
z⁻¹, smooth in z, and the flow boxes of [[lem:i-b-4-3]] are taken with the parameter (Re z, Im z), as there. The
monotonicity is needed for 𝖻 only, the weights being constant (D7). ∎

**Proposition {#prop:ii-f-2-6}** (Elliptic estimate; [[prop:i-b-4-2]].) If K ⊂ 𝒫_ι is compact, w_𝐦⁻¹c_zG_(ι,z) is
bounded away from 0 on K for z ∈ Z, WF′(B) ⊂ K and G is elliptic on K, then ‖Bu‖_𝐨 ≤ C(‖G𝐏u‖_(𝐨−𝐦) + ‖u‖_(𝐨−K𝐞)),
uniformly for z ∈ Z and h < h_0. Fibre infinity of 𝒫_ι lies in Ell(P′) for every z, by [[eq:ii-f-1-10]], P″ being of
lower order.

*Proof.* [[lem:ii-f-2-2]] (c) and the compactness argument of [[prop:i-b-4-2]]. At fibre infinity the principal symbol
of P_(ι,h,z) is h² times that of N⁰(h⁻¹z) in the rescaled fibre variables, which is [[eq:ii-f-1-10]], positive definite
and independent of z; the terms involving z are of lower differential order, and the principal symbol of 𝐏 is c_zG_(ι,z)
(or its conjugate) times the identity, P″ being of lower order. ∎
### High frequencies without b-regularity {#sec:ii-f-3}

This section proves [Hin26c, Proposition 10.6 (2)] with no b-derivatives.

#### The statement {#sec:ii-f-3-1}

Throughout this section and the next we assume

    γ_I < 3/2 + S̄,    γ_+ < γ_I,   {#eq:ii-f-3-1}

with γ_I, γ_+ and γ_cf = −(α_+ + 2) as in [[eq:ii-f-1-2]]. (As γ_I = α_I + 2, the first condition is α_I < −½ + S̄.) The
orders are those of [[sec:ii-f-1-3]]: an order 𝗌′ at fibre infinity (any variable order; P_(ι,h,z) is elliptic there),
and at sf the orders 𝖻_± with [[eq:ii-f-1-17]], together with a constant 𝖻_mid with 𝖻_mid + α_+ < −½ + S̄. The
parameters are

    𝒵^±_h := {±1 + iy : −hγ_+ ≤ y ≤ 1},    𝒵^i := {x + i : |x| ≤ 1},   {#eq:ii-f-3-2}

with 𝖻 := 𝖻_± for z ∈ 𝒵^±_h and 𝖻 := 𝖻_mid for z ∈ 𝒵^i (a point ±1 + i of both families is taken with either order), and

    𝐨 := (𝗌′; 2γ_I, γ_cf, γ_cf; 𝖻),    Y_𝐨 := H^((𝗌′−2; 2γ_I+2, γ_cf−2, γ_cf; 𝖻+1)).   {#eq:ii-f-3-3}

Every σ ∈ ℂ with Im σ ≥ −γ_+ and |σ| ≥ √2h_0⁻¹ is h⁻¹z with h ∈ (0, h_0) and z in one of the families: if |Re σ| ≥ Im σ,
take h := |Re σ|⁻¹ and z := ±1 + ih Im σ; otherwise h := (Im σ)⁻¹ and z := h Re σ + i.

**Proposition {#prop:ii-f-3-1}** ([Hin26c, Proposition 10.6 (2)] in dimension 4 + 1, k = 0.) Assume [[eq:ii-f-3-1]].
There are h_0 > 0 and C such that for h ∈ (0, h_0) and z in 𝒵^±_h or 𝒵^i, with the orders above,

    ‖u‖_𝐨 ≤ C‖P_(ι,h,z)u‖_(Y_𝐨),   {#eq:ii-f-3-4}

and P_(ι,h,z) : H^𝐨 → Y_𝐨 is invertible. Equivalently, N⁰(h⁻¹z) : H^(𝗌′,(2γ_I,γ_cf))_(0,b)(ι⁺) →
H^(𝗌′−2,(2γ_I+2,γ_cf−2))_(0,b)(ι⁺) is invertible (for fixed h these are the same spaces, [[sec:ii-f-2-1]]).

**Remark {#rem:ii-f-families}** [Hin26c, Proposition 10.6 (2)] is stated for all |z| ∈ [½, 2] with Im z ≥ −hγ_+, with
𝖻 = 𝖻_± where |z ∓ 1| ≤ ½ and 𝖻 "an arbitrary constant otherwise". The argument given there does not reach that
statement. 𝖻_± is adapted to the radial sets of the real part at Re z = ±1, [[eq:ii-f-1-14]]; for real z ≠ ±1 these sets
lie at ξ_cħ = ∓2z, where 𝖻_± need be neither constant nor monotone (the order adapted there is 𝖻_± dilated by z, by the
scaling P_(ι,h,z) = z²P_(ι,h/z,1), z > 0). And a constant order must satisfy the threshold at R_(cf,out), which for Im z
≥ ν is, for the flow on the zero section, a source; see [[lem:ii-f-3-3]] (R4). The families [[eq:ii-f-3-2]] keep Re z =
±1 near the real axis and cover every σ; this is what [[sec:ii-f-6]] uses.

#### Symbols {#sec:ii-f-3-2}

μ_b := |(dR/R) dg̸| on all of ι⁺ (a b-density at both ends, as dR/R = −2 dx_I/x_I), and fibre inner products 𝔢 are taken
to depend on ω only near both ends; each radial estimate below uses its own 𝔢 (the norms are equivalent). Write Re S_0
:= ½(S_0 + S_0^(*𝔢)), P := P_(ι,h,z) and P̃ := z⁻¹P.

**Lemma {#lem:ii-f-3-2}** (a) N⁰(σ) = N⁰(0) + σ∂_σN⁰ with ∂_σN⁰ = −2iR⁻¹(R∂_R + c + S_0), so P = h²N⁰(0) + hz∂_σN⁰. With
Q_0 := Im ∂_σN⁰ and Q_1 := −h Re ∂_σN⁰,

    Im P = 𝒫_1(Re z) − (Im z)Q_1,    𝒫_1(x) := h² Im N⁰(0) + x hQ_0,   {#eq:ii-f-3-5}

    Im P̃ = 𝒫̃_1(z) − (Im z/|z|²)𝒜,    𝒫̃_1(z) := hQ_0 + Re(z⁻¹)h² Im N⁰(0),    𝒜 := h² Re N⁰(0).   {#eq:ii-f-3-6}

(b) Q_0 = −R⁻¹(4 + 2 Re S_0) exactly, on all of ι⁺ (R⁻¹ = x_I² near ℐ⁺). Q_1 ∈ Ψ^(𝐦−𝐞_1), 𝒫_1, 𝒫̃_1 ∈ Ψ^(𝐦−𝐞) and 𝒜 ∈
Ψ^𝐦, uniformly for |z| ≤ 2, and |z| ≥ ½ in [[eq:ii-f-3-6]].

(c) Over sf: σ(Q_1) = −2ξ_cħ near F_K and x_I²ξ near F_I (consistently: ξ_cħ = −½x_I²ξ where both are defined); σ(𝒜) =
(1 + 2R)ξ_cħ² + |η_cħ|² near F_K and x_I²(½ξ² + |η|² + ¼x_I²ξ²) near F_I. Moreover 𝒜 = Σ_(j,k) W_j*M̃_(jk)W_k + 𝒜′ with
W_j ∈ Diff¹_(𝒱_ħ) scalar, acting componentwise, M̃ ≥ 0 a scalar matrix function, and 𝒜′ ∈ Ψ^(𝐦−𝐞) self-adjoint with
principal symbol vanishing on the zero section over sf.

(d) With ϖ := hx_I² near F_I and ϖ := ρ′ := h/(h + R) near F_K, at R = 0, resp. x_I = 0, over sf, and Re z = 1:

    ϖ⁻¹σ(𝒫_1(1)) = (5/2 + Re S_0)ξ − (4 + 2 Re S_0)    near F_I,   {#eq:ii-f-3-7}

    ϖ⁻¹σ(𝒫_1(1)) = −(½p_in + 4)ξ_cħ + b·η_cħ − (4 + 2 Re S_0)    near F_K,   {#eq:ii-f-3-8}

and ϖ⁻¹σ(𝒫̃_1(z)) = −(4 + 2 Re S_0) on the zero section at F_I and at F_K, for every z. Here p_in(ω) is the endomorphism
of [[eq:i-a-1-5]] ([[lem:ii-c-2-6]]), ξa with a = −½p_in being the scattering symbol at ∂X, at ξ dr, of ρ⁻¹ Im P̂(0) for
the Euclidean density, and b(ω) is an endomorphism-valued covector.

*Proof.* (a) [[eq:ii-f-1-6]] is affine in σ. Im(zA) = Re z Im A + Im z Re A gives [[eq:ii-f-3-5]]; for [[eq:ii-f-3-6]],
P̃ = z⁻¹h²N⁰(0) + h∂_σN⁰, and Im(z⁻¹) = −Im z/|z|².

(b) ∂_σN⁰ = iY with Y := −2R⁻¹(R∂_R + c + S_0), so Q_0 = Re Y. For μ_b, (R∂_R)* = −R∂_R and [R∂_R, R⁻¹] = −R⁻¹, so
Re(R⁻¹R∂_R) = ½(R⁻¹R∂_R − R∂_R R⁻¹) = ½R⁻¹; 𝔢 does not depend on R, so Re(R⁻¹S_0) = R⁻¹ Re S_0. Hence Q_0 = −R⁻¹(1 +
2c + 2 Re S_0), and 1 + 2c = 4. The classes follow from [[lem:ii-f-2-1]] (c) and the factor h ≤ 2ρ_sf in hQ_0 and in the
terms of h² Im N⁰(0), which are h times semiclassical operators of first order (the imaginary part of a second-order
operator with real scalar principal symbol has first order).

(c) Q_1 = h Im Y (Re(iY) = −Im Y), and h(−2R⁻¹R∂_R) = −2R⁻¹(hR∂_R) with hR∂_R ↦ i(h + R)ξ_cħ = iR(1 + ĥ)ξ_cħ in the
covectors of [[sec:ii-f-1-3]], so its symbol is −2i(1 + ĥ)ξ_cħ, whose imaginary part is −2(1 + ĥ)ξ_cħ, = −2ξ_cħ over sf.
Near F_I, ∂_σN⁰ = ix_I²(x_I∂_(x_I) − 2(c + S_0)) by [[eq:ii-f-1-6]], and hx_I∂_(x_I) ↦ iξ gives x_I²ξ. σ(𝒜) is the real
part of the symbol of h²N⁰(0), which is [[eq:ii-f-1-13]] with z = 0. For the decomposition: by [[lem:ii-c-1-2]], P⁽⁰⁾(0,
ω, ρ∂_ρ, ∂_ω) = ((ρD_ρ)² + Δ_(𝕊³)) Id + P⁽⁰⁾_1 with P⁽⁰⁾_1 ∈ Diff¹_b, so near ι⁺ ∩ K⁺

    h²N⁰(0) = h²R⁻²((1 + 2R)(RD_R)² + Δ_(𝕊³)) Id − 2h²R⁻¹(R∂_R)(c + S_0) + h²R⁻²P⁽⁰⁾_1.

With V_1 := (h/(h + R))R∂_R and V_a := (h/(h + R))Z_a, Z_a the six rotation fields of 𝕊³ (Δ_(𝕊³) = Σ Z_a*Z_a), hRD_R =
−iρ_cf⁻¹RV_1 and hZ_a = ρ_cf⁻¹RV_a up to the factor R/ρ_K → 1, so the first term is Σ W_j*M̃_(jk)W_k with W = (V_1, V_a)
and M̃ = diag((1 + 2R)ρ_cf⁻², ρ_cf⁻², …) ≥ 0, modulo terms in which a derivative falls on a coefficient or on the matrix
of 𝔢 (in W_j*); these are first-order operators with an extra factor ρ_sf, in Ψ^(𝐦−𝐞), with symbols linear in (ξ_cħ,
η_cħ). The other two terms are h times first-order semiclassical operators, also linear in the fibre variables at the
level 𝐦 − 𝐞 (the term −2h²R⁻¹R∂_R(c + S_0) = −2ĥR(1 + ĥ)iV_1(…) even vanishes at R = 0), plus zeroth-order terms in
Ψ^(𝐦−2𝐞). The real part of all this is 𝒜′. Near ℐ⁺ the same holds with [[eq:ii-f-1-11]]: h²x_I²[−½(x_I∂_(x_I))² +
x_I²(¼(x_I∂_(x_I))² + Δ)] is a sum of squares of hx_I∂_(x_I), hx_IZ_a with the factors x_I²(½ + ¼x_I²), x_I².

(d) *Near F_I.* With D := x_I∂_(x_I), D* = −D for μ_b, and (x_I²D²)* = D²x_I² = x_I²(D + 2)², so Im(−½x_I²D²) =
(1/2i)·½x_I²((D + 2)² − D²) = −ix_I²(D + 1), and h² times it has symbol hx_I²ξ. For X := x_I²(hD)(c + S_0), of principal
symbol x_I²iξ(c + S_0), the principal symbol of Im X is (1/2i)(x_I²iξ(c + S_0) + x_I²iξ(c + S_0^(*𝔢))) = x_I²(c + Re
S_0)ξ, and h² Im(x_I²D(c + S_0)) = h Im X. The term h²x_I⁴P⁽⁰⁾(0, ω, ½x_I∂_(x_I), ∂_ω) contributes O(hx_I³): its
second-order part has imaginary part x_I⁴ times a first-order b-operator (the conjugation of (x_I∂_(x_I))² by x_I⁴, and
of Δ_(𝕊³) by the matrix of 𝔢), and its first-order part is x_I⁴Diff¹_b ⊂ x_I³Diff¹_0. As N⁰(0) = −½x_I²D² + x_I²D(c +
S_0) + x_I⁴P⁽⁰⁾(0, ω, ½x_I∂_(x_I), ∂_ω) near ℐ⁺ by [[eq:ii-f-1-6]], σ(h² Im N⁰(0)) = hx_I²(1 + c + Re S_0)ξ + O(hx_I³),
and with (b), σ(hQ_0) = −hx_I²(4 + 2 Re S_0); 1 + c = 5/2. Adding the two gives [[eq:ii-f-3-7]].

*Near F_K.* The term −2h²R⁻¹R∂_R(R∂_R + c + S_0) of h²N⁰(0) is R·O(1) in Ψ^𝐦 (as h²R⁻¹(R∂_R)² = R(1 + ĥ)²V_1² up to
bounded factors), so its imaginary part has symbol O(Rĥ), which vanishes at R = 0 relative to ϖ. For h²R⁻²P⁽⁰⁾(0, ω,
−R∂_R, ∂_ω): at t_* = 1, R = r and this is h² times the frozen operator N(P̂(0)) = ρ²P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω), ρ = r⁻¹. For
the Euclidean density R⁴μ_b, ρ⁻¹ Im N(P̂(0)) ∈ ρDiff¹_b = Diff¹_sc has scattering symbol at ∂X linear in (ξ, η) (the
zeroth-order part of ρDiff¹_b vanishes at ∂X), say ξa + b·η, and p_in = −2a by the definition of p_in (the proof of
[[lem:ii-c-2-6]] (iii); the symbol is that of P̂(0), the two differing by ρDiff²_b at ∂X, [[sec:i-c-4-1]] (a)). Over sf
the canonical covector is ζ_R = ξ_cħ/h, so h²ρξ_sc a ↦ h²R⁻¹aξ_cħ/h = ĥaξ_cħ, and likewise ĥb·η_cħ. For μ_b instead of
R⁴μ_b, A^(*μ_b) = R⁴A*R⁻⁴, so Im_(μ_b)A = Im A − (1/2i)R⁴[A*, R⁻⁴]. For A = h²R⁻²(RD_R)², [RD_R, R⁻⁴] = 4iR⁻⁴, hence
[(RD_R)², R⁻⁴] = RD_R[RD_R, R⁻⁴] + [RD_R, R⁻⁴]RD_R = 8iR⁻⁴RD_R − 16R⁻⁴, and R⁴[A*, R⁻⁴] = 8ih²R⁻²RD_R modulo Ψ^(𝐦−2𝐞);
the correction −(1/2i)·8ih²R⁻²RD_R = −4h²R⁻²RD_R has symbol −4h²R⁻²Rζ_R = −4ĥξ_cħ (it is −nĥξ_cħ in dimension n;
[Hin26c] has −3ĥξ_cħ in dimension 3 + 1). With σ(hQ_0) = −ĥ(4 + 2 Re S_0) and ρ′/ĥ → 1 at R = 0, ϖ⁻¹σ(𝒫_1(1)) =
−½p_inξ_cħ + b·η_cħ − 4ξ_cħ − (4 + 2 Re S_0), which is [[eq:ii-f-3-8]]. For 𝒫̃_1(z): on the zero section the first-order
symbols vanish, leaving σ(hQ_0). ∎

*The Hamilton fields.* Let p be the real principal symbol of Re P or Re P̃ over sf: p = Re G_(ι,z), resp.
Re(z⁻¹G_(ι,z)). w_(𝐦−𝐞) is ϖ times a smooth positive function at finite frequencies near F_I, resp. F_K, so replacing
w_(𝐦−𝐞) by ϖ in [[prop:ii-f-2-4]] multiplies 𝖧^𝐏_z and w_(𝐦−𝐞)⁻¹p_1 by the same positive function and changes none of
the signs in its (i), (iii) and (v); we work with 𝖧 := ϖ⁻¹H_p. Near F_I, in the coordinates (x_I, ω; ξ, η) of the
semiclassical 0-covectors, the canonical coordinates are ζ_x = ξ/(hx_I), ζ_ω = η/(hx_I), and for a function g(x_I, ω, ξ,
η) (in local coordinates on 𝕊³; H^(𝕊³)_g := ∂_ηg·∂_ω − ∂_ωg·∂_η)

    h⁻¹H_g = ∂_ξg (x_I∂_(x_I) + η·∂_η) − (x_I∂_(x_I)g + η·∂_ηg)∂_ξ + x_IH^(𝕊³)_g.   {#eq:ii-f-3-9}

For p = x_I²g, H_p = x_I²H_g + gH_(x_I²) and H_(x_I²) = −2hx_I²∂_ξ, so 𝖧 = h⁻¹H_g − 2g∂_ξ; on {p = 0} this is
[[eq:ii-f-1-15]] up to O(x_I²). For Re z = 1, g = ½ξ² − ξ + |η|² + ¼x_I²ξ², and at x_I = 0

    𝖧 = (ξ − 1)(x_I∂_(x_I) + η·∂_η) + (2ξ − ξ² − 4|η|²)∂_ξ   (x_I = 0),    x_I⁻¹𝖧x_I = ξ − 1 + ½x_I²ξ.   {#eq:ii-f-3-10}

Near F_K the canonical coordinates are ζ_R = ξ_cħ(h + R)/(hR), ζ_ω = η_cħ(h + R)/h (the covectors of [[sec:ii-f-1-3]]),
and 𝖧 = ρ′⁻¹H_p is, in the coordinates (ĥ, R, ω, ξ_cħ, η_cħ) of the phase-space family,

    𝖧 = ∂_ξp V − (Vp)∂_ξ + H^(𝕊³)_p,    V := R∂_R − ĥ∂_ĥ + ρ′ξ∂_ξ − (1 − ρ′)η·∂_η   {#eq:ii-f-3-11}

(ξ = ξ_cħ, η = η_cħ), as ∂_(ζ_R) = Rρ′∂_ξ, ∂_(ζ_ω) = ρ′∂_η and R∂_R|_(ζ,h) = R∂_R|_(ξ,η,h) + ρ′ξ∂_ξ − (1 − ρ′)η·∂_η,
with R∂_R|_h = R∂_R|_ĥ − ĥ∂_ĥ. It is a smooth b-vector field, tangent to {ĥ = 0} (sf) and to {R = 0}; this is (D6). At
ĥ = 0, for Re z = 1, p = 2ξ + (1 + 2R)ξ² + |η|², and [[eq:ii-f-3-11]] is [[eq:ii-f-1-16]] divided by ĥ:

    𝖧 = (2(1 + 2R)ξ + 2)(R∂_R − η·∂_η) + 2(|η|² − Rξ²)∂_ξ + H^(𝕊³)_(|η|²),    R⁻¹𝖧R = 2(1 + 2R)ξ + 2.   {#eq:ii-f-3-12}

For P̃ with Re z = 1 or z ∈ 𝒵^i: p = 2ξ + Re(z⁻¹)((1 + 2R)ξ² + |η|²) near F_K and p = x_I²(−ξ + Re(z⁻¹)(½ξ² + |η|² +
¼x_I²ξ²)) near F_I.

*Symmetry.* G_(ι,−z)(R, ω; −ξ, −η) = G_(ι,z)(R, ω; ξ, η); σ(Q_1) and [[eq:ii-f-3-7]]–[[eq:ii-f-3-8]] are odd under (ξ,
η, Re z) ↦ (−ξ, −η, −Re z) (with p_in at ξ = +2 for z = −1, [[eq:i-a-1-5]]); and the fibre reflection reverses Hamilton
fields. So every statement below for 𝒵^+_h and its radial sets holds for 𝒵^−_h with ξ ↦ −ξ, η ↦ −η and ς ↦ −ς; we write
out 𝒵^+_h.

#### The radial estimates {#sec:ii-f-3-3}

We apply [[prop:ii-f-2-4]] with J = 1 (one application of [[lem:i-b-3-3]]), so only the thresholds at 𝖻 itself are
needed; the error is ‖Gu‖_(𝐨−¼𝐞).

**Lemma {#lem:ii-f-3-3}** For z ∈ 𝒵^+_h with y = Im z ≤ ν, ν ∈ (0, 1] small, the estimate [[eq:ii-f-2-4]] holds at:

(R1) Λ = R_(I⁺,1,in), for 𝐏 = P, ς = +1, as a source, with δ = 0;

(R2) Λ = R_(I⁺,out), for 𝐏 = P̃, ς = +1, as a sink (δ = 1, K_E in a punctured neighbourhood of Λ), and this for every z
∈ 𝒵^+_h ∪ 𝒵^i;

(R3) Λ = R_(cf,1,in), for 𝐏 = P, ς = +1, with K_E ⊂ {R ≥ δ_1} (ϱ-sink, ϕ-source);

(R4) Λ = R_(cf,out), for 𝐏 = P̃, ς = +1, with K_E ⊂ {ϕ ≥ δ_2} (ϱ-source, ϕ-sink), and this for every z ∈ 𝒵^+_h ∪ 𝒵^i;

where Im z ≥ ν, K_E lies in the elliptic set of P̃.

*Proof.* In each case 𝖻 is constant near Λ ([[eq:ii-f-1-17]]; 𝖻_mid is constant), and 𝖧 vanishes on Λ, by
[[eq:ii-f-3-10]], [[eq:ii-f-3-12]] and their analogues for P̃ (for P̃ at the zero section ∂_ξp = −x_I², resp. 2, and the
∂_ξ-component is quadratic in (ξ, η)). We check (i)–(v) of [[prop:ii-f-2-4]]. Write Re S_0 ≥ S̄ − ϵ for the inner
product of [[lem:ii-c-2-5]] (used at (R2) and (R4)), and use at (R3) the inner product in which ϑ_in is evaluated.

(R1) ϱ = x_I, and β_ϱ = ξ − 1 + ½x_I²ξ → 1 at Λ = {x_I = 0, ξ = 2, η = 0}: a ϱ-source. (ii): for y ∈ [−hγ_+, hν_1], with
ν_1 := 1 + max(0, −γ_I), put −yQ_1 into 𝒫_1: it is h·(y/h)Q_1 ∈ Ψ^(𝐦−𝐞) with |y/h| ≤ max(γ_+, ν_1), and ℓ = 0. For y ∈
[hν_1, ν] put −hν_1Q_1 into 𝒫_1 and take (A) with ℓ := y − hν_1 ∈ [0, 1] and 𝒜 := Q_1, whose principal symbol x_I²ξ ≥
x_I² near ξ = 2 is ≥ c_0w_(𝐦−𝐞_1) there. (iii): g := ½ξ² − ξ + |η|² + ¼x_I²ξ² (|x_I⁻²G_(ι,z)| ≥ |g|) and ϕ := (ξ − 2)² +
|η|². By [[eq:ii-f-3-10]] at x_I = 0, 𝖧ϕ = −2ξ(ξ − 2)² − 8(ξ − 2)|η|² + 2(ξ − 1)|η|²; from g = ½ξ(ξ − 2) + |η|² +
O(x_I²), (ξ − 2)² ≤ C(g² + |η|⁴ + x_I⁴) near Λ, so 𝖧ϕ ≥ |η|² − C(g² + x_I) ≥ ½ϕ − C_1(ϱ + g²) near Λ (the x_I-dependent
terms are O(x_I)): a ϕ-source. (iv) κ̃ = 2γ_I + 1. (v) p_1 = σ(𝒫_1(1)) − (y/h)·hx_I²ξ in the first case and σ(𝒫_1(1)) −
ν_1hx_I²ξ in the second. At ξ = 2, [[eq:ii-f-3-7]] gives (5/2 + Re S_0)·2 − (4 + 2 Re S_0) = 1, and ϖ⁻¹·hx_I²ξ = ξ = 2,
so ϖ⁻¹p_1 = 1 − 2y/h, resp. 1 − 2ν_1, and with β_ϱ = 1,

    𝒯 = 2(2γ_I + 1) − 2(1 − 2y/h) = 4(γ_I + y/h) ≥ 4(γ_I − γ_+),      resp.      𝒯 = 4(γ_I + ν_1) ≥ 4,

positive by [[eq:ii-f-3-1]]. [Hin26c, Section 10.1.2] has the total −4x_I^(−4γ_I)(γ_I + h⁻¹ Im z), which is
−x_I^(−4γ_I)𝒯 in the first case.

(R2) ϱ = x_I, p = x_I²g with g := −ξ + Re(z⁻¹)(½ξ² + |η|² + ¼x_I²ξ²), Λ = {x_I = 0, ξ = η = 0}, and β_ϱ = ∂_ξg → −1: a
ϱ-sink. (ii): by [[eq:ii-f-3-6]] and [[lem:ii-f-3-2]] (c), Im P̃ = (𝒫̃_1 − ℓ𝒜′) − ℓΣ W_j*M̃_(jk)W_k with ℓ := Im z/|z|²:
case (B) when ℓ ≥ 0; when ℓ < 0, |ℓ| ≤ hγ_+ and ℓ𝒜 is part of 𝒫_1, its symbol (ℓ/h)ϖ·½ξ² + … vanishing at Λ. In both
cases ℓ𝒜′ lies in Ψ^(𝐦−𝐞) with symbol vanishing at Λ. (iii): |x_I⁻²z⁻¹G_(ι,z)| ≥ |g|, and ϕ := ξ² + |η|². At x_I = 0,
𝖧 = ∂_ξg(x_I∂_(x_I) + η·∂_η) − (η·∂_ηg + 2g)∂_ξ by [[eq:ii-f-3-9]], and 𝖧ϕ = −4ξ Re(z⁻¹)|η|² − 4ξg + 2∂_ξg|η|² =
−2|η|² + O(|ξ||η|²) − 4ξg. From ξ = Re(z⁻¹)(½ξ² + |η|²) − g, |ξ| ≤ C(|η|² + |g|) near Λ (Re(z⁻¹) ∈ [−½, 1]), so 𝖧ϕ ≤
−|η|² + Cg² ≤ −½ϕ + C_1(g² + ϱ): a ϕ-sink. (iv) κ̃ = 2γ_I + 1. (v) By [[lem:ii-f-3-2]] (d), ϖ⁻¹p̃_1 = −(4 + 2 Re S_0) at
Λ, so with β_ϱ = −1,

    𝒯 = 2(2γ_I + 1)(−1) + 2(4 + 2 Re S_0) = 6 − 4γ_I + 4 Re S_0 ≥ 4(3/2 + S̄ − ϵ − γ_I),

positive by [[eq:ii-f-3-1]] for ϵ small. (In dimension 3 + 1, [Hin26c, Section 10.1.2] has (4γ_I + 2) − 4(1 + Re S) − 2
< 0; in dimension 4 + 1 the middle term is −4(3/2 + Re S).)

(R3) ϱ = R, Λ = {R = 0, ξ_cħ = −2, η_cħ = 0} over sf, and β_ϱ = 2(1 + 2R)ξ + 2 → −2 by [[eq:ii-f-3-12]]: a ϱ-sink. (ii):
for y ≤ 0, −yQ_1 is part of 𝒫_1, with ϖ⁻¹(−y)σ(Q_1) = 2yξ(1 + ĥ)²R/h, which is bounded by Cγ_+R (|y| ≤ hγ_+) and
vanishes at R = 0; for y ∈ [0, ν], (A) with ℓ := y and 𝒜 := Q_1, σ(Q_1) = −2ξ ≥ 3 near Λ, and w_(𝐦−𝐞_1) bounded above
and below there. (iii): g := 2ξ + (1 + 2R)ξ² + |η|² and ϕ := (ξ + 2)² + |η|². At R = 0, by [[eq:ii-f-3-12]], 𝖧ϕ = 2(ξ +
2)·2|η|² − 2(2ξ + 2)|η|² = 4|η|² (with H^(𝕊³)_(|η|²)|η|² = 0), and (ξ + 1)² = 1 − |η|² + g there gives |ξ + 2| ≤
C(|η|² + |g|); so 𝖧ϕ ≥ 4|η|² − CR ≥ c_1ϕ − C_1(ϱ + g²): a ϕ-source. (iv) w_𝐤 at F_K: ρ_tf^(−k_tf)ρ_sf^(−𝖻_𝐤) =
R^(𝖻_𝐤−k_tf)h^(−𝖻_𝐤) times a smooth positive factor (ρ_tf/R and ρ_sf/ĥ are smooth and positive near ĥ = R = 0), with
k_tf = γ_cf and 𝖻_𝐤 = 𝖻 + ½: κ̃ = γ_cf − 𝖻 − ½. (v) By [[eq:ii-f-3-8]] at ξ = −2, η = 0: ϖ⁻¹p_1 = (½p_in + 4)·2 − (4 + 2
Re S_0) = 4 + p_in − (S_0 + S_0^(*𝔢)), so, with γ_cf = −(α_+ + 2) and β_ϱ = −2,

    𝒯 = 2(γ_cf − 𝖻 − ½)(−2) − 2(4 + p_in − (S_0 + S_0^(*𝔢)))
      = 4(𝖻 + α_+) + 8 + 2 − 8 − 2(p_in − (S_0 + S_0^(*𝔢))) = 4(𝖻 + α_+) + 2 − 2(p_in − (S_0 + S_0^(*𝔢))),

and max spec(p_in − (S_0 + S_0^(*𝔢))) ≤ ϑ_in on ∂X ([[lem:ii-c-2-6]]), so 𝒯 ≥ 4(𝖻 + α_+) + 2 − 2ϑ_in > 0 by
[[eq:ii-f-1-17]]. (In dimension 3 + 1 the total of [Hin26c] is −4𝖻 + 4γ_cf − 2 + 2(3 + ϑ_in) with γ_cf = −(α_+ + 3/2),
the same condition [Hin26c, (10.28)]; the dimension cancels.) In case (A) the commutant carries the factor χ_0(ρ_sf/δ_s)
of (D9).

(R4) ϱ = R, Λ = {R = 0, ξ_cħ = η_cħ = 0}, p = 2ξ + Re(z⁻¹)((1 + 2R)ξ² + |η|²), and β_ϱ = ∂_ξp → 2: a ϱ-source. (ii) as
in (R2). (iii): g := p (|z⁻¹G_(ι,z)| ≥ |p|) and ϕ := ξ² + |η|²; at R = 0, 𝖧ϕ = 2ξ·2 Re(z⁻¹)|η|² − 2∂_ξp|η|² = −4|η|²,
and |ξ| ≤ C(|g| + |η|²) near Λ, so 𝖧ϕ ≤ −2ϕ + C(g² + |η|⁴) + CR ≤ −c_1ϕ + C_1(ϱ + g²): a ϕ-sink. (iv) κ̃ = γ_cf − 𝖻 − ½.
(v) ϖ⁻¹p̃_1 = −(4 + 2 Re S_0) at Λ, so with β_ϱ = 2,

    𝒯 = 2(γ_cf − 𝖻 − ½)·2 + 2(4 + 2 Re S_0) = −4(𝖻 + α_+) − 8 − 2 + 8 + 4 Re S_0
      = −4(𝖻 + α_+) − 2 + 4 Re S_0 ≥ −4(𝖻 + α_+) − 2 + 4(S̄ − ϵ) > 0

by [[eq:ii-f-1-17]] for 𝖻_± and by the choice of 𝖻_mid, for ϵ small. [Hin26c, Section 10.1.2] prints the total as 4𝖻 +
4α_+ + 2 + 4 Re S and requires it to be negative, which would give 𝖻 + α_+ < −½ − Re S; the next sentence there states
𝖻 + α_+ < −½ + Re S, which is what the evaluation above gives. Where Im z ≥ ν: on {ϕ ≥ δ_2} near Λ, |Im(z⁻¹G_(ι,z))| =
(Im z/|z|²)((1 + 2R)ξ² + |η|²) ≥ (ν/2)δ_2 − CR, so K_E is in the elliptic set; likewise in (R2). ∎

#### Step 1: the symbolic estimate {#sec:ii-f-3-4}

**Lemma {#lem:ii-f-3-4}** Fix M ≥ 1 − inf 𝗌′. There are h_0 and C such that for h < h_0, z ∈ 𝒵^+_h ∪ 𝒵^i (with the
orders of [[sec:ii-f-3-1]]) and u ∈ C^∞_c((ι⁺)°),

    ‖u‖_𝐨 ≤ C(‖Pu‖_(Y_𝐨) + ‖u‖_((−M; 2γ_I, γ_cf, γ_cf; 𝖻−1/4))).                                          {#eq:ii-f-3-13}

*Proof.* (a) *Fibre infinity and the elliptic set.* By [[prop:ii-f-2-6]], fibre infinity of 𝒫_ι lies in Ell(P), and so
does every point over sf where G_(ι,z) ≠ 0, uniformly for z in compact sets: for z ∈ 𝒵^+_h, |G_(ι,z)| ≥ |Re G_(ι,z)| =
|G_(ι,1)| (G is affine in z), so the elliptic set contains the complement of Σ_1 := {G_(ι,1) = 0}; for Im z ≥ ν and on
𝒵^i, |Im(z⁻¹G_(ι,z))| = (Im z/|z|²)σ(𝒜) shows that the characteristic set over sf is the zero section o_sf.

(b) *The dynamics.* For Re z = 1 the Hamilton field of Re G_(ι,z) = G_(ι,1) is that of [[sec:ii-f-1-3]]; on Σ_1, q :=
σ(Q_1) = −2ξ_cħ (= x_I²ξ near F_I) satisfies q ≥ 0 with equality exactly on o_sf, since G_(ι,1) = 0 gives 2ξ_cħ = −((1 +
2R)ξ_cħ² + |η_cħ|²) over sf. The future flow is 𝖧 (ς = +1), and every integral curve in Σ_1 has its α-limit in
R_(I⁺,1,in) ∪ R_(cf,1,in) ∪ R_(cf,out) and its ω-limit in R_(cf,1,in) ∪ R_(cf,out) ∪ R_(I⁺,out), with the types of
[[sec:ii-f-1-3]]. The curves from R_(cf,out) to R_(I⁺,out) are the fibres of o_sf over (ι⁺)°: o_sf ⊂ Σ_1, and on it 𝖧 =
2R∂_R near F_K and −x_I∂_(x_I) near F_I by [[eq:ii-f-3-11]]–[[eq:ii-f-3-12]] and [[eq:ii-f-3-9]], as the unstable
manifold of the saddle R_(cf,out) is one-dimensional over each ω (its linearisation is 2R∂_R − 2η·∂_η plus terms
quadratic in (ξ, η)). The curves from R_(cf,1,in) to R_(cf,out) lie in F_K. For Im z ≥ ν and on 𝒵^i, the field of
Re(z⁻¹G_(ι,z)) on o_sf is the same, 2R∂_R, resp. −x_I∂_(x_I), since the quadratic part does not contribute there.

(c) *Propagation.* Along curves in Σ_1 ∖ o_sf use [[prop:ii-f-2-5]] for 𝐏 = P, ς = +1: for y ≤ hν_1 with |ℓ| ≤ Ch (the
term −yQ_1 in 𝒫_1), for y ∈ [hν_1, ν] with (A), ℓ = y and 𝒜 = Q_1, as q > 0 there; 𝖻_+ is non-increasing along 𝖧 on a
neighbourhood of these curves by [[eq:ii-f-1-17]] ([[def:ii-c-2-4]] (1) pulled back). Along o_sf use [[prop:ii-f-2-5]]
for 𝐏 = P̃, ς = +1, with (B) for Im z ≥ 0 and |ℓ| ≤ Ch for Im z < 0 ([[lem:ii-f-3-3]], the proof of (R2)); 𝖻_+ is
non-increasing along 𝖧 = 2R∂_R on o_sf (the same flow as at z = 1), and 𝖻_mid is constant.

(d) *Assembly for y ≤ ν.* Cover the compact set Σ_1 over sf by finitely many open sets in which [[eq:ii-f-2-4]] or
[[eq:ii-f-2-5]] holds, in this order. (1) A neighbourhood U_1 of R_(I⁺,1,in), by (R1), with no control term. (2) For
each point of Σ_1 ∖ o_sf over sf° ∪ F_I° whose backward curve enters U_1: [[prop:ii-f-2-5]] from U_1. These cover a
neighbourhood of the stable manifold of R_(cf,1,in) over R > 0, minus a neighbourhood of Λ, and of the incoming curves
to R_(I⁺,out) in Σ_1 ∖ o_sf. (3) A neighbourhood U_3 of R_(cf,1,in) by (R3), whose control set K_E ⊂ {R ≥ δ_1} near Λ
lies in the set covered in (2), after shrinking δ_1 (points of Σ_1 near Λ with R > 0 lie on curves from R_(I⁺,1,in), and
points off Σ_1 are elliptic). (4) The curves in F_K from R_(cf,1,in) to R_(cf,out), by [[prop:ii-f-2-5]] from U_3, with
(D9) for (A). (5) A neighbourhood U_5 of R_(cf,out) by (R4), whose K_E ⊂ {ϕ ≥ δ_2} near Λ consists of points of Σ_1 ∩
F_K on the curves of (4), of points of Σ_1 over R > 0 near them, which lie on curves from R_(I⁺,1,in) or from
R_(cf,1,in) and so are covered by (2), or by (4) with [[prop:ii-f-2-5]] once more, and of elliptic points. (6) o_sf over
(ι⁺)°, by [[prop:ii-f-2-5]] for P̃ from U_5. (7) A neighbourhood of R_(I⁺,out) by (R2), whose punctured control set lies
in the sets of (2) and (6) and in the elliptic set. The finitely many operators B_* so obtained, together with elliptic
ones, are jointly elliptic on 𝒫_ι; a microlocal partition of unity gives ‖u‖_𝐨 ≤ C(Σ_i‖B_(*,i)u‖_𝐨 + ‖u‖_(𝐨−K𝐞)). Each
estimate has its ‖G𝐏u‖_(𝐨−𝐦+𝐞) (or ‖GPu‖_(𝐨−𝐦) for elliptic ones) bounded by C‖Pu‖_(Y_𝐨) (|z|⁻¹ ≤ 1 for P̃; the
operators G at finite frequencies see only the sf order 𝖻 + 1 of Y_𝐨, those at fibre infinity only its differential
order 𝗌′ − 2), its ‖E′u‖_𝐨 by an earlier estimate, and its error ‖Gu‖_(𝐨−¼𝐞), with G microsupported at finite
frequencies, by C‖u‖_((−M;…;𝖻−1/4)) + C‖u‖_(𝐨−K𝐞). The constants are uniform in z: [[prop:ii-f-2-4]]–[[prop:ii-f-2-5]]
give them on neighbourhoods of each z_* in the compact set {1 + iy : 0 ≤ y ≤ ν} (the h-dependent points y ∈ [−hγ_+, 0)
are covered by the case |ℓ| ≤ Ch near y = 0).

(e) *Assembly for Im z ≥ ν and on 𝒵^i.* The characteristic set is o_sf: (R4) at R_(cf,out) with its K_E in the elliptic
set, [[prop:ii-f-2-5]] for P̃ with (B) along o_sf, (R2) at R_(I⁺,out), and the elliptic estimate elsewhere, uniformly
for z in the compact sets {1 + iy : ν ≤ y ≤ 1} and 𝒵^i.

Finally ‖u‖_(𝐨−K𝐞) ≤ ‖u‖_((−M;…;𝖻−1/4)) for K ≥ max(M + sup 𝗌′, ¼). ∎

#### Step 2: the transition face {#sec:ii-f-3-5}

The error term in [[eq:ii-f-3-13]] is not small as h → 0: its weight at tf is that of the left side. It is improved by
the transition face normal operator.

*The face.* In the coordinate R̂ := R/h, by [[eq:ii-f-1-12]],

    P_(ι,h,z) = N_tf(z) − 2h²R⁻¹R∂_R(R∂_R + c + S_0),
    N_tf(z) := −2izR̂⁻¹(R̂∂_R̂ + c + S_0) + R̂⁻²P⁽⁰⁾(0, ω, −R̂∂_R̂, ∂_ω),   {#eq:ii-f-3-14}

since −2R⁻¹(iz + hR∂_R)h(R∂_R + c + S_0) = −2izhR⁻¹(…) − 2h²R⁻¹R∂_R(…), and hR⁻¹ = R̂⁻¹, R∂_R = R̂∂_R̂, h²R⁻² = R̂⁻².
With ρ̂ := R̂⁻¹, N_tf(z) = 2izρ̂(ρ̂∂_ρ̂ − 3/2 − S_0) + ρ̂²N(P⁽⁰⁾) is [[eq:i-c-4-1]] at σ̂ = z on tf = [0, ∞]_R̂ × 𝕊³
([[sec:i-c-4-1]], with ztf at R̂ = 0 and sctf at R̂ = ∞). The remainder lies in ρ_tfρ_cf⁻¹Diff²_(𝒱_ħ): h²R⁻¹(R∂_R)² =
R⁻¹(h + R)²V_1² up to lower terms of the same class, and R⁻¹(h + R)² = ρ_tfρ_cf⁻¹ near K⁺ (up to smooth positive
factors).

*Orders.* Let 2δ_♭ ∈ (0, ¼] be so small that 𝖻_♭ := 𝖻 − 2δ_♭ still satisfies [[eq:ii-f-1-17]] (𝖻_± is constant near the
radial sets with strict inequalities, and a constant shift keeps the monotonicity); for 𝖻_mid any δ_♭ will do. Put 𝐨_♭
:= (−M; 2γ_I, γ_cf, γ_cf; 𝖻_♭); then ‖u‖_((−M;…;𝖻−1/4)) ≤ ‖u‖_(𝐨_♭).

**Lemma {#lem:ii-f-3-5}** (The tf-normal operator in dimension 4 + 1.) Assume P_0 tf-admissible with weight α_+ + 2
([[def:ii-c-2-3]]; α_+ + 2 = −γ_cf lies in the gap (β_−, β_+)), and let q := −α_+. For σ̂ ∈ {±1 + iy : 0 ≤ y ≤ 1} let 𝗋
:= 𝖻_♭|_(F_K) (for 𝖻 = 𝖻_±), and for σ̂ ∈ 𝒵^i let 𝗋 := 𝖻_mid − 2δ_♭. Then N_tf(σ̂) is invertible between the spaces of
[[thm:i-c-4-3]] with these orders, any s, and

    ‖w‖_(H^(s,(𝗋+α_+,q))_(sc,b)) ≤ C‖N_tf(σ̂)w‖_(H^(s−2,(𝗋+α_++1,q−2))_(sc,b)),
    ‖w‖_(H^(−s+2,(−𝗋−α_+−1,−q+2))_(sc,b)) ≤ C‖N_tf(σ̂)*w‖_(H^(−s,(−𝗋−α_+,−q))_(sc,b)),                    {#eq:ii-f-3-15}

uniformly in σ̂ in each family.

*Proof.* *The order.* F_K, the face of 𝒫_ι over sf ∩ tf, is the face of the scattering phase space of tf over sctf
([[sec:ii-a-6-2]], the paragraph on the tf-normal operator: the 0ħ,cħ-fields become the b,sc-fields of tf), with the
same fibre variables, and at R = 0 the symbol [[eq:ii-f-1-13]] is 2σ̂ξ + ξ² + |η|², the boundary symbol of
[[lem:i-b-4-1]] at σ = σ̂. So for σ̂ = ±1 + iy the real part of the symbol is that at σ_0 = ±1, and 𝗋 is a decay order
admissible at σ_0 = ±1 with weight α_+ in the sense of [[sec:i-a-1-4]]: non-increasing along the boundary flow (the
restriction to F_K of the flow over sf) and constant near R_in, R_out with the thresholds 𝗋 + α_+ > ½(−1 + ϑ_in), 𝗋 +
α_+ < −½ + S̄, which are [[eq:ii-f-1-17]] at F_K. *Fredholm estimates.* The proof of [[thm:i-c-4-3]] (1) with σ̂ in
place of e^(iθ): near sctf it uses [[thm:i-a-7-2]] (1), which applies with I = {±1}, ν = 1 and the order pair (s, 𝗋),
admissible for σ_0 = ±1, to σ = ±1 + iy; near ztf [[lem:i-c-2-5]]–[[lem:i-c-2-6]], which hold for σ̂ in compact sets; in
the interior, ellipticity. So [[eq:i-c-4-3]]–[[eq:i-c-4-4]] hold uniformly for y ∈ [0, 1]. For σ̂ ∈ 𝒵^i, Im σ̂ = 1 and
[[thm:i-a-7-2]] (2) applies with the constant order. *Kernel and index.* By [[eq:i-c-4-2]], N_tf(σ̂) =
|σ̂|²S_(|σ̂|)⁻¹N_tf(e^(iθ))S_(|σ̂|), θ = arg σ̂. An element of the kernel lies in 𝒜^(3/2+S̄−ϵ,−β)(tf) for all ϵ > 0 and
β ∈ (β_−, β_+) ([[thm:i-a-7-2]] (5) near sctf at σ = σ̂, [[lem:i-c-2-7]] near ztf, as in [[thm:i-c-4-3]] (5)); S_(|σ̂|)
preserves that space, which lies in 𝒳_(tf,θ), so the kernel is trivial by [[cor:i-c-5-2]] (a). The index is independent
of y ∈ [0, 1] (local constancy, as in [[thm:i-c-4-3]] (3), with the uniform estimates), and at y = 0, σ̂ = ±1 = e^(iθ)
with θ ∈ {0, π}, where it is 0 by [[cor:i-c-5-2]] (a), the index not depending on the admissible orders. So N_tf(σ̂) is
invertible, and [[eq:ii-f-3-15]] holds uniformly by the contradiction argument of [[cor:i-c-5-2]] (b). For 𝒵^i, θ ∈
[π/4, 3π/4] = Σ_m and |σ̂| ∈ [1, √2]; S_(|σ̂|) is an isomorphism of the spaces with constant orders, with norms bounded
uniformly (r̂^(q−2) and ρ̂^(𝗋+α_+) are homogeneous, and dilations preserve the b- and sc-structures), so
[[eq:ii-f-3-15]] is [[cor:i-c-5-2]] (b) on Σ_m with 𝗋_mid := 𝗋. ∎

**Lemma {#lem:ii-f-3-6}** There are h_0 and C such that for h < h_0, z as in [[lem:ii-f-3-4]], and u ∈ C^∞_c((ι⁺)°),

    ‖u‖_(𝐨_♭) ≤ C‖Pu‖_(Y_𝐨) + Ch^(δ_♭)‖u‖_𝐨.   {#eq:ii-f-3-16}

*Proof.* Let χ ∈ C^∞(ℝ), χ = 1 on (−∞, ½] and χ = 0 on [1, ∞), and (as in [Hin26c, the proof of Proposition 10.6, Step
2])

    χ_tf := χ(ρ_tf) χ(ρ_tf/ρ_sf).

On its support ρ_tf < 1 and ρ_tf < ρ_sf; near cf, for h < ½, χ_tf = 1. It is a function on ι⁺ depending on h, with
derivatives along C^∞_b𝒱_b(ι⁺) bounded uniformly (ρ_K∂_(ρ_K) log(ρ_tf/ρ_sf) = 2ρ_cf, [[lem:ii-f-2-1]] (b)). Note
ρ_tfρ_sf = h.

*Away from tf.* On supp(1 − χ_tf), either ρ_tf ≥ ½, so ρ_sf = h/ρ_tf ≤ 2h, or ρ_tf ≥ ½ρ_sf, so ρ_sf² ≤ 2h. In both cases
ρ_sf^(2δ_♭) ≤ (2h)^(δ_♭), and m_h := h^(−δ_♭)ρ_sf^(2δ_♭)(1 − χ_tf) ∈ S⁰ with seminorms bounded uniformly in h (its
derivatives are of the same form, or carry derivatives of χ_tf, supported where the same bounds hold). As ‖(1 −
χ_tf)u‖_(𝐨_♭) = ‖ρ_sf^(2δ_♭)(1 − χ_tf)u‖_((−M;…;𝖻)), [[lem:ii-f-2-2]] (a) gives ‖(1 − χ_tf)u‖_(𝐨_♭) ≤ Ch^(δ_♭)‖u‖_𝐨.

*Near tf.* By [[sec:ii-a-6-2]] ([Hin26c, (3.60)]), for functions supported in supp χ_tf,
‖w‖_(H^(s,(2α_I,α_cf,l,𝖻))_(0ħ,cħ,h)) ∼ h^(−l)‖w‖_(H^(s,(α_cf,𝖻−l))_(b,sc)(tf)) uniformly (the weight at 0f is
immaterial there), where on the right 𝖻 is read on the b,sc phase space of tf. Our sf orders depend on R; on supp χ_tf,
ρ_tf² ≤ ρ_tfρ_sf = h, so R ≤ Ch^(1/2), and 𝖻_♭ differs from its restriction to F_K by O(h^(1/2)) with all derivatives;
ρ_sf^(±O(h^(1/2))) is then a symbol of order 0 with bounded seminorms (h^(1/2) log h⁻¹ → 0), so the norms with 𝖻_♭ and
with 𝗋 := 𝖻_♭|_(F_K) are equivalent there, uniformly. The b-density on tf is R̂⁻⁴ times the Euclidean one (|dx̂| = R̂³
dR̂ dg̸ = R̂⁴|(dR̂/R̂) dg̸|), so ‖w‖_(L²(|(dR̂/R̂) dg̸|)) = ‖R̂⁻²w‖_(L²(R̂⁴|(dR̂/R̂) dg̸|)), and R̂ = ρ_cf/ρ_sf on tf up
to smooth positive factors; so the b,sc weights (α_cf, 𝗋 − l) for the b-density are (α_cf + 2, 𝗋 − l − 2) for the
Euclidean one (in dimension 3 + 1 the shift is 3/2). With l = γ_cf and α_cf = γ_cf, the Euclidean weights (at cf, at sf)
are (γ_cf + 2, 𝗋 − γ_cf − 2) = (−α_+, 𝗋 + α_+) = (q, 𝗋 + α_+), which in the notation of [[ch:s03]] (sctf first) is the
space H^(s,(𝗋+α_+,q))_(sc,b). [[lem:ii-f-3-5]] then gives, with all differential orders −M, resp. −M − 2,

    ‖χ_tfu‖_(𝐨_♭) ≤ Ch^(−γ_cf)‖χ_tfu‖_(H^(−M,(𝗋+α_+,q))_(sc,b))
                 ≤ Ch^(−γ_cf)‖N_tf(σ̂)χ_tfu‖_(H^(−M−2,(𝗋+α_++1,q−2))_(sc,b)) ≤ C‖N_tf(σ̂)χ_tfu‖_(Y_♭),

Y_♭ := H^((−M−2; −M, γ_cf−2, γ_cf; 𝖻_♭+1)), converting back: the Euclidean weights (at cf, at sf) (q − 2, 𝗋 + α_+ + 1)
are the b-weights (q − 4, 𝗋 + α_+ + 3) = (γ_cf − 2, 𝗋 − γ_cf + 1), which are (α_cf, 𝖻′ − l) for α_cf = γ_cf − 2, l =
γ_cf and 𝖻′ = 𝗋 + 1. ([Hin26c] interchanges cf and tf in the orders of this last space.) Here σ̂ := z if Im z ≥ 0 and σ̂
:= Re z = ±1 if Im z < 0.

*From N_tf to P.* N_tf(σ̂)χ_tfu = χ_tfPu + [P, χ_tf]u − (P − N_tf(z))χ_tfu + (N_tf(σ̂) − N_tf(z))χ_tfu. (1)
‖χ_tfPu‖_(Y_♭) ≤ C‖Pu‖_(Y_𝐨), as Y_♭ has lower orders. (2) By [[eq:ii-f-3-14]], P − N_tf(z) ∈ ρ_tfρ_cf⁻¹Diff²_(𝒱_ħ), so
its contribution is bounded by C‖χ_tfu‖_((−M; ·, γ_cf−1, γ_cf−1; 𝖻_♭+1)). On supp χ_tf, ρ_tf < ρ_sf, so
ρ_tfρ_sf^(2δ_♭−1) = ρ_tf^(2δ_♭)ρ_tf^(1−2δ_♭)ρ_sf^(2δ_♭−1) ≤ (ρ_tfρ_sf)^(2δ_♭) = h^(2δ_♭), and ρ_cf ≤ 1; the weight of
this norm divided by that of 𝐨 is ρ_cfρ_tfρ_sf^(2δ_♭−1) ≤ h^(2δ_♭), and, as for m_h above, the contribution is bounded
by Ch^(2δ_♭)‖u‖_𝐨. (3) χ_tf = 1 near cf, and the derivatives of χ_tf along 𝒱_ħ = ρ_sfC^∞_b𝒱_b are ρ_sf times bounded
functions supported where ρ_tf ∈ [½, 1] (there ρ_sf ≤ 2h) or ρ_tf/ρ_sf ∈ [½, 1] (there ρ_sf² ≤ 2h). So [P, χ_tf] ∈
ρ_sfDiff¹_(𝒱_ħ) with coefficients supported there and vanishing near cf, and its contribution is at most
C‖ρ_sf^(2δ_♭)χ̃u‖_((−M;…;𝖻)) ≤ C(2h)^(δ_♭)‖u‖_𝐨, χ̃ a cut-off to that support. (4) If Im z < 0, N_tf(σ̂) − N_tf(z) = −i
Im z ∂_zN_tf with |Im z| ≤ γ_+h = γ_+ρ_tfρ_sf and ∂_zN_tf = −2iR̂⁻¹(R̂∂_R̂ + c + S_0) = h∂_σN⁰ ∈ Ψ^(𝐦−𝐞_1) near tf with
weight ρ_cf⁻¹; its contribution is bounded by C‖χ_tfu‖_((−M+1; ·, γ_cf−1, γ_cf−1; 𝖻_♭)), and ρ_cfρ_tfρ_sf^(2δ_♭) ≤
h^(2δ_♭) (ρ_tf ≤ ρ_tf^(2δ_♭)). Summing, ‖u‖_(𝐨_♭) ≤ ‖χ_tfu‖_(𝐨_♭) + ‖(1 − χ_tf)u‖_(𝐨_♭) gives [[eq:ii-f-3-16]]. ∎

#### Proof of Proposition 3.1 {#sec:ii-f-3-6}

*Proof of [[prop:ii-f-3-1]].* By [[lem:ii-f-3-4]] and [[lem:ii-f-3-6]], ‖u‖_𝐨 ≤ C‖Pu‖_(Y_𝐨) + Ch^(δ_♭)‖u‖_𝐨 for u ∈
C^∞_c((ι⁺)°), and for h small the last term is absorbed: this is [[eq:ii-f-3-4]] for such u, and by [[lem:ii-f-2-2]] (g)
for every u ∈ H^𝐨 with Pu ∈ Y_𝐨 (the norm of Y_𝐨 is that of H^(𝐨−𝐦+𝐞) at finite frequencies and of H^(𝐨−𝐦) at fibre
infinity, and [[lem:ii-f-2-2]] (g) at the two orders, with a microlocal partition of unity, gives the density). For
𝒵^−_h use the symmetry of [[sec:ii-f-3-2]].

*The adjoint.* The same steps apply to P* = P*_(ι,h,z) on the dual spaces: with 𝐨* := −𝐨 + 𝐦 − 𝐞 + 𝐞_1, so that H^(𝐨*) =
(Y_𝐨)* and H^(−𝐨) is the dual of H^𝐨 ((S3) and (S11)),

    ‖v‖_(𝐨*) ≤ C‖P*v‖_(−𝐨).   {#eq:ii-f-3-17}

Every radial estimate of [[lem:ii-f-3-3]] holds for 𝐏* (ε_♭ = −1) with ς ↦ −ς at the dual order: the dual of the order 𝐤
of (D3) is −𝐤, so κ̃ ↦ −κ̃, while β_ϱ ↦ −β_ϱ and ςε_♭ is unchanged; so 𝒯 is the same, and sources and sinks (in ϱ and in
ϕ) are interchanged. The absorbing terms keep their sign (ε_♭ς unchanged); the dual sf order −𝖻 − 1 is non-increasing
along −𝖧. So the assembly runs backwards: from R_(I⁺,out) (now a source), along o_sf and Σ_1 ∖ o_sf backwards, to
R_(cf,out), R_(cf,1,in) and R_(I⁺,1,in); at the saddles the roles of ϱ and ϕ interchange, and the control sets are the
unstable manifolds, reached from the earlier steps. In Step 2 the second estimate of [[eq:ii-f-3-15]] replaces the
first, with [P*, χ_tf] and P* − N_tf(z)* bounded as before; Y_♭ and 𝐨_♭ are replaced by their duals shifted in the same
way.

*Invertibility.* For fixed small h, [[eq:ii-f-3-4]] shows that P : H^𝐨 → Y_𝐨 is injective with closed range. If v ∈
(Y_𝐨)* = H^(𝐨*) annihilates the range, then P*v = 0 in H^(−𝐨) (the pairing ⟨Pu, v⟩ = ⟨u, P*v⟩ holds for u ∈
C^∞_c((ι⁺)°), dense in H^𝐨), so v = 0 by [[eq:ii-f-3-17]] and [[lem:ii-f-2-2]] (g) for P*. So P is surjective. ∎
### High frequencies with b-regularity {#sec:ii-f-4}

This section proves [Hin26c, Proposition 10.6 (2)] with k b-derivatives.

#### The b-vector fields and the commuted operator {#sec:ii-f-4-1}

Let W_1 := R∂_R (= −½x_I∂_(x_I) near ℐ⁺) and W_(1+a) := Z_a, a = 1, …, 6, the rotation fields y_i∂_(y_j) − y_j∂_(y_i), 1
≤ i < j ≤ 4, of 𝕊³ ⊂ ℝ⁴. The Z_a span T𝕊³ at every point: for ω ∈ 𝕊³ and v ⊥ ω, Σ_(i,j) ω_iv_j(y_i∂_(y_j) −
y_j∂_(y_i))|_ω = |ω|²v − (ω·v)ω = v, the sum running over all ordered pairs. So W_1, …, W_7 span 𝒱_b(ι⁺) over C^∞(ι⁺) at
both ends and in between (R∂_R and ∂_ω near ι⁺ ∩ K⁺, x_I∂_(x_I) and ∂_ω near ι⁺ ∩ ℐ⁺). For a word α = (α_1, …, α_k) ∈
{1, …, 7}^k put W^α := W_(α_1)⋯W_(α_k), |α| := k, j_α := #{i : α_i = 1}, and let W^α_♯ be the same product with each W_1
replaced by W_1 + 2. For v on ι⁺ and orders 𝐨 put

    ‖v‖_(𝐨;k) := Σ_(|α|≤k) ‖W^αv‖_𝐨,    ‖v‖_(𝐨;k,+) := Σ_(j=0)^k h^(−j)‖v‖_(𝐨;k−j).   {#eq:ii-f-4-1}

‖·‖_(𝐨;k) is the norm of H^((𝗌;k),(a,c,l,𝖻))_((0ħ,cħ,h);b) (k orders of b-regularity, (S3) of [[sec:ii-a-3]] with 𝒲 =
C^∞_b𝒱_b(ι⁺)), up to equivalence uniform in h. The norm ‖·‖_(𝐨;k,+), with the constant factors h^(−j), is the one
[[prop:ii-f-6-2]] ([Hin26c, Proposition 10.12]) needs: under the Mellin transform τ∂_τ becomes iσ, |σ| = |z|h⁻¹, which
is the factor |σ|^j of [Hin26c, (10.47)].

With L := 2hR⁻¹(iz + hR∂_R), and the decomposition P⁽⁰⁾(0, ω, ρ∂_ρ, ∂_ω) = ((ρD_ρ)² + Δ_(𝕊³)) Id + P⁽⁰⁾_1 of
[[sec:ii-f-3-2]], P⁽⁰⁾_1 = A(ω)ρ∂_ρ + Σ_b B_b(ω)Z_b + C(ω) (∂_ω written in the spanning family Z_b, with smooth
coefficients):

**Lemma {#lem:ii-f-4-1}** (a) [W_1, P_(ι,h,z)] = −2P_(ι,h,z) − L(W_1 + c + S_0) and [W_1, L] = −L. (b) [Z_a,
P_(ι,h,z)] = −L(Z_aS_0) + h²R⁻²(Σ_b c_(ab)W_b + c_(a0)) with c_(ab), c_(a0) ∈ C^∞(𝕊³; End ℂ^(N_E)), and [Z_a, L] = 0.
(c) For every word α with |α| = k ≥ 1 and u ∈ C^∞_c((ι⁺)°),

    (P − j_αL)W^αu = W^α_♯Pu + Σ_(|β|=k) 𝒞_(αβ)W^βu + Σ_(|β|≤k−1) ℛ_(αβ)W^βu,    P := P_(ι,h,z),   {#eq:ii-f-4-2}

where each 𝒞_(αβ) is multiplication by an element of h²R⁻¹C^∞(𝕊³) + h²R⁻²C^∞(𝕊³) and each ℛ_(αβ) by an element of
hR⁻¹C^∞(𝕊³) + h²R⁻¹C^∞(𝕊³) + h²R⁻²C^∞(𝕊³) (endomorphism-valued, polynomial in z). In particular 𝒞_(αβ) ∈ Ψ^(𝐦−2𝐞) and
ℛ_(αβ) ∈ Ψ^(𝐦−𝐞).

*Proof.* (a) P = −2R⁻¹B + h²R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω) with B := (iz + hR∂_R)(hR∂_R + h(c + S_0)) by [[eq:ii-f-1-12]]; B
and P⁽⁰⁾(…) commute with R∂_R, and [R∂_R, R^(−m)] = −mR^(−m). So [W_1, P] = 2R⁻¹B − 2h²R⁻²P⁽⁰⁾ = −2P − 2R⁻¹B, and
−2R⁻¹B = −L(R∂_R + c + S_0). Also [W_1, L] = [R∂_R, 2hR⁻¹](iz + hR∂_R) = −L. (b) Z_a commutes with R, R∂_R and Δ_(𝕊³);
[Z_a, −2R⁻¹B] = −2R⁻¹(iz + hR∂_R)h(Z_aS_0) = −L(Z_aS_0), and [Z_a, P⁽⁰⁾_1] = (Z_aA)ρ∂_ρ + Σ_b((Z_aB_b)Z_b + B_b[Z_a,
Z_b]) + Z_aC, a first-order operator in the W's with coefficients in C^∞(𝕊³), as [Z_a, Z_b] is a combination of the Z's.
(c) Induction on k. Write α = (α_1, α′) and v := W^(α′)u. By (a), P(W_1v) = (W_1 + 2)Pv + LW_1v + L(c + S_0)v; by (b),
P(Z_av) = Z_aPv + L(Z_aS_0)v − h²R⁻²(Σ_b c_(ab)W_bv + c_(a0)v). Insert [[eq:ii-f-4-2]] for Pv (v = u for k = 1). The
term j_(α′)LW^(α′)u becomes (W_1 + 2)j_(α′)LW^(α′)u = j_(α′)L(W_1 + 1)W^(α′)u (by [W_1, L] = −L), resp.
j_(α′)LZ_aW^(α′)u; together with LW_1v this gives j_αLW^αu, plus j_(α′)LW^(α′)u. Write L = 2izhR⁻¹ + 2h²R⁻¹W_1: acting
on a word of length k − 1, the first part is of ℛ-type and the second of 𝒞-type (a word of length k with the coefficient
h²R⁻¹); likewise L(c + S_0)v and L(Z_aS_0)v, after commuting the coefficient past W_1 (which produces ℛ-type terms). The
terms h²R⁻²c_(ab)W_bv are of 𝒞-type and h²R⁻²c_(a0)v of ℛ-type. Applying W_1 + 2 or Z_a to the 𝒞- and ℛ-terms of level k
− 1: W(𝒞w) = 𝒞(Ww) + (W𝒞)w, and likewise for ℛ, where W𝒞, Wℛ are of the same type (R∂_R(h^aR^(−b)c) = −bh^aR^(−b)c,
Z_a(h^aR^(−b)c) = h^aR^(−b)Z_ac); the ℛ-terms of level k − 1 act on words of length at most k − 2, so after one more
letter at most k − 1; the 𝒞-terms of level k − 1 act on words of length k − 1, giving 𝒞-terms on words of length k and
terms W𝒞, of ℛ-type (𝒞-type coefficients lie in the ℛ-type class), on words of length k − 1. The classes: near F_K,
hR⁻¹ = ĥ ≍ ρ_sf, h²R⁻¹ = ĥ²R and h²R⁻² = ĥ²; near F_I, hR⁻¹ = hx_I², h²R⁻¹ = h²x_I² and h²R⁻² = h²x_I⁴; and w_(𝐦−𝐞) = ϖ
(ĥ, resp. hx_I²) and w_(𝐦−2𝐞) at differential order 0 is ϖρ_sf, up to smooth positive factors at finite frequencies; as
multiplication operators they have differential order 0. ∎

*The commuted system.* For k ≥ 1 let U_k := (W^αu)_(|α|=k), with values in ℂ^(N_E) ⊗ ℂ^(7^k) and the fibre inner product
𝔢^(⊕7^k), and

    P^(k) := diag_α(P − j_αL) − (𝒞_(αβ))_(αβ) ∈ P ⊗ Id + Ψ^(𝐦−𝐞),
    P^(k)U_k = F_k := (W^α_♯Pu + Σ_(|β|≤k−1) ℛ_(αβ)W^βu)_α.   {#eq:ii-f-4-3}

**Lemma {#lem:ii-f-4-2}** (The thresholds of the system.) Let p^(k)_1 and p̃^(k)_1 be the principal symbols (at the
level 𝐦 − 𝐞) of the imaginary parts of P^(k) and z⁻¹P^(k), decomposed as in [[lem:ii-f-3-3]] with the same ℓ and 𝒜. At
the four radial sets (Re z = 1, resp. on the zero section),

    ϖ⁻¹p^(k)_1 = ϖ⁻¹p_1 ⊗ Id                    at R_(I⁺,1,in),
    ϖ⁻¹p^(k)_1 = ϖ⁻¹p_1 ⊗ Id − 2 diag(j_α)      at R_(cf,1,in),
    ϖ⁻¹p̃^(k)_1 = ϖ⁻¹p̃_1 ⊗ Id − 2 diag(j_α)      at R_(I⁺,out) and at R_(cf,out).

So the threshold quantities 𝒯^(k) of [[prop:ii-f-2-4]] satisfy 𝒯^(k) ≥ 𝒯 ⊗ Id at each of the four radial sets, and
(R1)–(R4) of [[lem:ii-f-3-3]] hold for P^(k), resp. z⁻¹P^(k), with the same orders.

*Proof.* 𝒞 is in Ψ^(𝐦−2𝐞), so does not contribute at the level 𝐦 − 𝐞. Near F_K, hR∂_R ↦ iR(1 + ĥ)ξ_cħ, so L has symbol
2iĥ(z + R(1 + ĥ)ξ_cħ) and z⁻¹L has symbol 2iĥ(1 + z⁻¹R(1 + ĥ)ξ_cħ); at R = 0 their imaginary parts are 2ĥ Re z = 2ĥ and
2ĥ. Near F_I, hR∂_R = −½hx_I∂_(x_I) ↦ −(i/2)ξ, so L has symbol ihx_I²(2z − ξ), with imaginary part hx_I²(2 Re z − ξ),
which is 0 at ξ = 2, Re z = 1; and z⁻¹L has symbol ihx_I²(2 − z⁻¹ξ), with imaginary part 2hx_I² at ξ = 0. The parts of
case (A) (ℓQ_1) and of case (B) (ℓ𝒜) are untouched; L and its imaginary part lie in Ψ^(𝐦−𝐞), so enter 𝒫_1, resp. 𝒫̃_1,
only. In 𝒯 = 2κ̃β_ϱ − 2ςε_♭ϖ⁻¹p_1 (ς = ε_♭ = 1), lowering ϖ⁻¹p_1 by 2j_α raises 𝒯 by 4j_α. ∎

#### The estimate {#sec:ii-f-4-2}

**Proposition {#prop:ii-f-4-3}** ([Hin26c, Proposition 10.6 (2)] in dimension 4 + 1.) Assume [[eq:ii-f-3-1]], and let
h_0, the families [[eq:ii-f-3-2]] and the orders be as in [[prop:ii-f-3-1]]. For every k ∈ ℕ_0 there is C_k such that
for h < h_0 (after decreasing h_0 depending on k) and z in the families,

    ‖u‖_(𝐨;k) ≤ C_k‖P_(ι,h,z)u‖_(Y_𝐨;k),    ‖u‖_(𝐨;k,+) ≤ C_k‖P_(ι,h,z)u‖_(Y_𝐨;k,+),   {#eq:ii-f-4-4}

and P_(ι,h,z) : {u ∈ H^𝐨 : ‖u‖_(𝐨;k) < ∞} → {f ∈ Y_𝐨 : ‖f‖_(Y_𝐨;k) < ∞} is invertible. Equivalently, N⁰(h⁻¹z) is
invertible between the spaces H^((𝗌′;k),(2γ_I,γ_cf))_(0,b;b)(ι⁺) and H^((𝗌′−2;k),(2γ_I+2,γ_cf−2))_(0,b;b)(ι⁺).

The second estimate of [[eq:ii-f-4-4]] follows from the first at the levels 0, …, k: h^(−j)‖u‖_(𝐨;k−j) ≤
C_(k−j)h^(−j)‖Pu‖_(Y_𝐨;k−j), and the sum of the right sides is ‖Pu‖_(Y_𝐨;k,+) up to the constants.

**Lemma {#lem:ii-f-4-4}** (Regularity at fixed h.) For fixed h ∈ (0, h_0) and z, if u ∈ H^𝐨 and ‖Pu‖_(Y_𝐨;k) < ∞, then
‖u‖_(𝐨;k) < ∞.

*Proof.* It suffices to take the fibre order 𝗌′ of 𝐨 constant, equal to s_1 := inf 𝗌′. Indeed, if W^αu lies in the space
of fibre order s_1 for |α| ≤ k, then by induction on |α|, PW^αu = W^αPu − [W^α, P]u, where [W^α, P] = Σ_(|β|<|α|)
A_(αβ)W^β with A_(αβ) ∈ x_I²ρ_K⁻²Diff²_(0,b)(ι⁺) (each [W_i, P] is of that class, and b-fields normalise 0,b-fields; at
fixed h no semiclassical order is tracked, unlike in [[eq:ii-f-4-3]]); so PW^αu ∈ Y_𝐨, and elliptic regularity at fibre
infinity ([[lem:ii-f-2-2]] (c), at this fixed h) puts W^αu in H^𝐨. So let 𝗌′ be constant. For fixed h, H^𝐨 and Y_𝐨 are
then weighted 0,b-Sobolev spaces with fixed weights and a constant order ([[sec:ii-f-2-1]]), on which the dilations
(D_κv)(R, ω) := v(κR, ω), κ ∈ [½, 2], and the rotations of 𝕊³ act boundedly, uniformly: they preserve ι⁺, its faces and
the 0,b-structure (x_I = R^(−1/2) is multiplied by κ^(−1/2)), and multiply the weights x_I^aρ_K^c and the density by
functions bounded above and below. For each letter let G^(i)_θ be the group it generates (D_(e^θ) for W_1, the rotations
e^(θZ_a) for W_(1+a)) and T^(i)_θ := θ⁻¹(G^(i)_θ − 1), 0 < |θ| ≤ 1; for a word α and θ = (θ_1, …, θ_k) with 0 < |θ_i| ≤
1 put T^α_θ := T^(α_1)_(θ_1)⋯T^(α_k)_(θ_k). By [[eq:ii-f-1-12]], G_θPG_θ⁻¹ is e^(−θ)(−2R⁻¹B) + e^(−2θ)h²R⁻²P⁽⁰⁾ for
dilations, and P with S_0, P⁽⁰⁾_1 transported by the rotation for rotations; in both cases a family of second-order
operators of the class of P depending smoothly on θ. Hence [T^(i)_θ, X] = θ⁻¹(G_θXG_θ⁻¹ − X)G_θ, for X of that class, is
again uniformly of that class composed with G_θ, and so are the iterated commutators; all are bounded H^𝐨 → Y_𝐨
uniformly (for fixed h the sf orders are immaterial, and the weights at 0f and cf of P are those of 𝐨 − Y_𝐨). By the
Leibniz rule for these commutators, PT^α_θu = T^α_θPu + Σ X_(α,θ,S)T^(α_S)_(θ_S)u, the sum over proper subsets S ⊊ {1,
…, k}, α_S the subword, with X_(α,θ,S) uniformly bounded H^𝐨 → Y_𝐨. Induction on k: if W^βu ∈ H^𝐨 for |β| < k, then
T^(α_S)_(θ_S)u is an average of transported copies of W^(α_S)u (by T_θv = θ⁻¹∫_0^θ G_(θ′)Wv dθ′), so is bounded in H^𝐨,
and T^α_θPu is bounded in Y_𝐨 as W^αPu ∈ Y_𝐨. So PT^α_θu is bounded in Y_𝐨, and by [[eq:ii-f-3-4]] (at this fixed h,
T^α_θu ∈ H^𝐨), T^α_θu is bounded in H^𝐨; a weak limit point as θ → 0 is W^αu, which therefore lies in H^𝐨. ∎

*Proof of [[prop:ii-f-4-3]].* The case k = 0 is [[prop:ii-f-3-1]]. Let k ≥ 1 and assume [[eq:ii-f-4-4]] at the levels
below k. By density ([[lem:ii-f-2-2]] (g) for the norms ‖·‖_(𝐨;k), whose proof is the same: the mollifiers J_ϵ and the
cut-offs χ_j commute with the W's up to operators of the same kind, uniformly bounded and tending to 0) it suffices to
take u ∈ C^∞_c((ι⁺)°).

*Step 1.* [[lem:ii-f-3-4]] holds for the system [[eq:ii-f-4-3]] in place of P: its proof uses
[[prop:ii-f-2-4]]–[[prop:ii-f-2-6]] for 𝐏 = c_zP^(k) (with P″ := P^(k) − P ⊗ Id ∈ Ψ^(𝐦−𝐞)), whose hypotheses hold at the
four radial sets by [[lem:ii-f-4-2]], along the flow because P″ is of lower order (it enters only β in
[[prop:ii-f-2-5]]), and at fibre infinity and on the elliptic set because the principal symbol is G_(ι,z) Id. So

    ‖U_k‖_𝐨 ≤ C(‖F_k‖_(Y_𝐨) + ‖U_k‖_((−M; 2γ_I, γ_cf, γ_cf; 𝖻−1/4))).

By [[eq:ii-f-4-3]], ‖F_k‖_(Y_𝐨) ≤ C‖Pu‖_(Y_𝐨;k) + CΣ_(|β|≤k−1)‖ℛ_(αβ)W^βu‖_(Y_𝐨), and ℛ_(αβ) ∈ Ψ^(𝐦−𝐞) maps H^(𝐨−𝐞_1) →
H^(𝐨−𝐦+𝐞−𝐞_1) = Y_𝐨 ([[lem:ii-f-2-2]] (a)), so these terms are at most C‖u‖_(𝐨;k−1) ≤ C‖Pu‖_(Y_𝐨;k−1) by the induction
hypothesis. And ‖U_k‖_((−M;…;𝖻−1/4)) ≤ Σ_(|α|=k)‖W^αu‖_(𝐨_♭).

*Step 2.* [[lem:ii-f-3-6]] holds with k b-derivatives:

    ‖u‖_(𝐨_♭;k) ≤ C‖Pu‖_(Y_𝐨;k) + Ch^(δ_♭)‖u‖_(𝐨;k).                                                       {#eq:ii-f-4-5}

Indeed, [[lem:ii-f-3-5]] holds with k b-derivatives on both sides of [[eq:ii-f-3-15]], with constants uniform as there:
for σ̂ = ±1 + iy by [[thm:i-a-7-2]] (4) near sctf (at σ_0 = ±1) and [[lem:i-c-2-5]] at the order s + k near ztf, as in
the proof of [[thm:i-c-4-3]] (4), and the contradiction argument of [[cor:i-c-5-2]] (b) with [[eq:i-c-4-5]]; for 𝒵^i by
[[cor:i-c-5-2]] (b) with k. The b-vector fields of tf are spanned by R̂∂_R̂ = R∂_R and the Z_a, the same W's, so the
norms of [[ch:s03]] with k b-derivatives are those of [[eq:ii-f-4-1]] on functions supported near tf. In the proof of
[[lem:ii-f-3-6]], apply W^α, |α| ≤ k: [W, χ_tf] and [W, 1 − χ_tf] are multiplications by functions of the same kind as
the derivatives of χ_tf (b-derivatives of ρ_tf, ρ_tf/ρ_sf are bounded multiples of them, [[lem:ii-f-2-1]] (b)); W^α
applied to P − N_tf(z) = −2h²R⁻¹W_1(W_1 + c + S_0), to [P, χ_tf] and to ∂_zN_tf gives sums of operators of the same
classes applied to W^β, |β| ≤ |α| (by [[lem:ii-f-4-1]] (a)–(b) and [W_1, R⁻¹] = −R⁻¹); and m_h commutes with W up to an
element of the same symbol class. Each estimate of that proof therefore holds with ‖·‖_(·;k) on both sides.

*Conclusion.* Combining, ‖u‖_(𝐨;k) ≤ ‖u‖_(𝐨;k−1) + ‖U_k‖_𝐨 ≤ C‖Pu‖_(Y_𝐨;k) + Ch^(δ_♭)‖u‖_(𝐨;k), and for h small the last
term is absorbed. Invertibility: injectivity is [[eq:ii-f-4-4]]; given f with ‖f‖_(Y_𝐨;k) < ∞, u := P⁻¹f ∈ H^𝐨 by
[[prop:ii-f-3-1]], and ‖u‖_(𝐨;k) < ∞ by [[lem:ii-f-4-4]]. ∎

**Remark {#rem:ii-f-b-regularity}** At ℐ⁺, [Hin26c] commutes with the e3b-fields of its Lemma 7.12 and reads the result
on the Mellin side, where the lower-order terms carry no factor h and each b-derivative costs h⁻¹. Here the b-fields
R∂_R, Z_a are used on all of ι⁺; the lower-order terms of [[eq:ii-f-4-2]] carry hR⁻¹ or h²R⁻², which is the level 𝐦 − 𝐞
at both ends, and the estimate [[eq:ii-f-4-4]] holds without loss. Near ι⁺ ∩ K⁺ this is [Hin26c, Lemma 10.7] in
dimension 4 + 1, with 𝒱 = (R∂_R, Z_1, …, Z_6, I) there, and [[eq:ii-f-4-2]] is [Hin26c, (10.32)–(10.33)], its term
−2ikzhR⁻¹δ_(α,(k,0,…,0)) being the part −2ij_αzhR⁻¹ of −j_αL.
### Bounded frequencies {#sec:ii-f-5}

This section proves [Hin26c, Proposition 10.6 (1)] and [Hin26c, Lemmas 10.9–10.10].

#### The statement {#sec:ii-f-5-1}

Throughout this section γ_I < 3/2 + S̄, γ_cf = −(α_+ + 2), and (β_−, β_+) is the indicial gap of P̂_0(0) that contains
−γ_cf ([[sec:ii-f-1-1]]). We write I(ζ) := P⁽⁰⁾(0, ω, ζ, ∂_ω), ζ ∈ ℂ, for the Mellin symbol of P̂_0(0) at ∂X, and spec_b
for the set of ζ at which I(ζ) is not invertible on 𝕊³ ([[sec:i-c-1]] and [[sec:i-c-2-5]]); so (β_−, β_+) ∩ Re spec_b =
∅. For an order 𝗌 (a real number or a variable order on ^(0,b)S*ι⁺) and k ∈ ℕ_0 put

    𝒳^𝗌_k := H^((𝗌;k),(2γ_I,γ_cf))_(0,b;b)(ι⁺),      𝒴^𝗌_k := H^((𝗌;k),(2γ_I+2,γ_cf−2))_(0,b;b)(ι⁺),
    𝒳^𝗌 := 𝒳^𝗌_0,      𝒴^𝗌 := 𝒴^𝗌_0,                                                                       {#eq:ii-f-5-1}

with the b-density μ_b of [[sec:ii-f-1-1]] ([[sec:ii-a-6-2]]). The index k counts b-derivatives along W_1 = R∂_R and
W_(1+a) = Z_a, a = 1, …, 6, the rotation fields of 𝕊³ ([[sec:ii-f-4-1]]), which span the b-vector fields of ι⁺ over
C^∞(ι⁺). By [[eq:ii-f-1-6]], N⁰(σ) ∈ x_I²ρ_K⁻²Diff²_(0,b)(ι⁺), and its commutators with the W_i are of the same class
(the proof of [[lem:ii-f-4-4]]); so N⁰(σ) : 𝒳^𝗌_k → 𝒴^(𝗌−2)_k is bounded.

**Proposition {#prop:ii-f-5-1}** ([Hin26c, Proposition 10.6 (1)] in dimension 4 + 1.) For every order 𝗌, every k ∈ ℕ_0
and every σ ∈ ℂ with Im σ > −γ_I,

    N⁰(σ) : 𝒳^𝗌_k → 𝒴^(𝗌−2)_k                                                                              {#eq:ii-f-5-2}

is Fredholm of index 0. If moreover Im σ > −1 − β_+, it is invertible.

The dimension enters only through c = 3/2. The upper bound γ_I < c + S̄ (1 + S̄ in dimension 3 + 1) is the upper end of
the weight interval I_σ = (−2 Im σ, 2(c + S̄)) of the 0-normal operator at ℐ⁺ ([[lem:ii-f-5-4]]), whose lower end gives
Im σ > −γ_I in every dimension, as 2γ_I ∈ I_σ means exactly −γ_I < Im σ and γ_I < c + S̄. The bound −1 − β_+ comes from
the one-dimensional Fourier transform in v of [[lem:ii-f-5-8]], whose shifts by 1 ([[eq:ii-f-5-12]] and
[[eq:ii-f-5-13]]) are those of that transform, also in every dimension.

**Remark {#rem:ii-f-bounded}** (Relation to [Hin26c].) [Hin26c] builds a local left parametrix at ι⁺ ∩ ℐ⁺ from [Hin23e,
Theorem 1.5], which assumes a boundary spectrum independent of the boundary point, and uses the structure of its
Schwartz kernel for b-regularity. Here the parametrix is that of [Hin23e, Theorem 3.4] (the 0-calculus with bounds,
which needs no such constancy), used only through the Fredholm property it gives on a compact manifold
([[lem:ii-f-5-5]]), and b-regularity is proved by difference quotients as in [[lem:ii-f-4-4]]. The positivity argument
of [Hin26c] for the reduced normal operator is replaced by the asymptotics of modified Bessel functions
([[lem:ii-f-5-4]]), and the bound on the Fourier transform that [Hin26c, (10.41)] quotes from [Hin23d, Lemma 2.25] is
proved ([[lem:ii-f-5-7]]). The proof of [Hin26c, Lemma 10.10] asks "1 + Im σ < β_+"; the condition its argument uses,
and its statement asserts, is −1 − Im σ < β_+.

#### Two general facts {#sec:ii-f-5-2}

**Lemma {#lem:ii-f-5-2}** (Fredholm estimates with a weak remainder.) Let T : X → Y be a Fredholm operator between
Banach spaces and j : X → W a continuous injective linear map into a Banach space W. Then there is C with ‖x‖_X ≤
C(‖Tx‖_Y + ‖jx‖_W) for all x ∈ X.

*Proof.* Let e_1, …, e_m be a basis of ker T. Since j is injective, je_1, …, je_m are linearly independent in W, and the
Hahn–Banach theorem gives ℓ_1, …, ℓ_m ∈ W* with ℓ_i(je_k) = δ_(ik). Then Πx := Σ_i ℓ_i(jx)e_i is a continuous projection
of X onto ker T, with ‖Πx‖_X ≤ C‖jx‖_W. T is injective on the closed subspace ker Π, and T(ker Π) = T(X) is closed, so
by the open mapping theorem ‖x′‖_X ≤ C‖Tx′‖_Y for x′ ∈ ker Π. Apply this to x′ := x − Πx, for which Tx′ = Tx, and add
‖Πx‖_X. ∎

**Lemma {#lem:ii-f-5-3}** (Compact inclusions.) Let 𝗌′ < 𝗌 (orders with sup(𝗌′ − 𝗌) < 0), a′ < a and c′ < c. Then
H^(𝗌,(a,c))_(0,b)(ι⁺) ↪ H^(𝗌′,(a′,c′))_(0,b)(ι⁺) is compact. The same holds for x^aH^𝗌_0(X̂) ↪ x^(a′)H^(𝗌′)_0(X̂) on the
compact manifold X̂ of [[sec:ii-f-5-3]].

*Proof.* Let χ ∈ C^∞([0, ∞)) vanish on [0, 1] and equal 1 on [2, ∞), and for ϵ ∈ (0, ¼) let χ_ϵ := χ(x_I/ϵ)χ(ρ_K/ϵ). Its
0,b-derivatives are bounded uniformly in ϵ (x_I∂_(x_I) and ρ_K∂_(ρ_K) of χ(·/ϵ) are (tχ′)(·/ϵ)). With w :=
x_I^(−a)ρ_K^(−c)u, x_I^(−a′)ρ_K^(−c′)(1 − χ_ϵ)u = f_ϵw, f_ϵ := (1 − χ_ϵ)x_I^(a−a′)ρ_K^(c−c′), and every C^∞_b-seminorm
of f_ϵ is at most C(2ϵ)^δ, δ := min(a − a′, c − c′), because 1 − χ_ϵ is supported where x_I ≤ 2ϵ or ρ_K ≤ 2ϵ and x_I,
ρ_K ≤ 1 on ι⁺ (after normalising the defining functions). Multiplication by f_ϵ is bounded on H^(𝗌′)_(0,b) with norm
bounded by finitely many such seminorms ((S5)–(S6) of [[sec:ii-a-3]]), so ‖(1 − χ_ϵ)u‖_(H^(𝗌′,(a′,c′))) ≤
Cϵ^δ‖u‖_(H^(𝗌,(a,c))). And u ↦ χ_ϵu maps into distributions supported in a fixed compact subset of (ι⁺)°, where all
these norms are the standard ones, so it is compact by Rellich's theorem. The inclusion is the norm limit of compact
operators as ϵ → 0. On X̂ the same argument with χ(x/ϵ). ∎

#### The model at ℐ⁺ {#sec:ii-f-5-3}

Near ι⁺ ∩ ℐ⁺ use (x, ω) := (x_I, ω) ∈ [0, 4) × 𝕊³, which covers {R > 1/16}. By [[eq:ii-f-1-6]],

    L_σ := x⁻²N⁰(σ) = −½(x∂_x − 2iσ)(x∂_x − 2(c + S_0)) + x²P⁽⁰⁾(0, ω, ½x∂_x, ∂_ω) ∈ Diff²_0   {#eq:ii-f-5-3}

there, with 0-principal symbol (½ + ¼x²)ξ_0² + |η_0|² ([[sec:ii-f-1-3]]), positive definite.

*The compact model.* Let X̂ := {y ∈ ℝ⁴ : |y| ≤ 8}, and identify {4 < |y| ≤ 8} with [0, 4)_x × 𝕊³ by x = 8 − |y|, ω =
y/|y|; so ∂X̂ = {x = 0}, and X̂ is a compact manifold with boundary of dimension 4. Let χ_3 ∈ C^∞_c([0, 4)) equal 1 on
[0, 3], read as a function on X̂ vanishing on {|y| ≤ 4}, and put

    P̂ := χ_3L_σ + (1 − χ_3)Δ_(ℝ⁴) ∈ Diff²_0(X̂; ℂ^(N_E)).   {#eq:ii-f-5-4}

Its principal symbol is a convex combination of positive definite forms, so P̂ is 0-elliptic, and P̂ = L_σ on {x < 3}.
Fix a smooth positive density ν_0 on X̂° equal to x⁻⁴|dx dω| on {x < 4} (a 0-density) and put μ_b := x³ν_0 there (a
b-density, a constant multiple of that of ι⁺, as |dR/R| = 2|dx/x|). The spaces x^αH^m_0(X̂) are taken with μ_b. Near ∂X̂
they coincide with the 0,b-spaces of ι⁺ near ι⁺ ∩ ℐ⁺ ([[sec:ii-a-6-2]], the cells U_(3,jk±)), and with the spaces of
[Hin23e, Section 3.1] under the identification g ↦ gν_0^(1/2) of functions with 0-half-densities: as ∫|x^(−α)g|²μ_b =
∫|x^(−α+3/2)g|²ν_0, x^αL²(μ_b) corresponds to x^(α−3/2)L²(X̂, ⁰Ω^(1/2)), which is the space of [Hin23e, (3.23)] at the
weight α (with n − 1 = 3, n = dim X̂); and for integer m both families of norms are equivalent to
Σ_(|γ|≤m)‖x^(−α)V^γu‖_(L²(μ_b)) over products of the 0-fields x∂_x, xZ_a (elliptic regularity in either calculus),
negative orders being the duals. Under this identification P̂ is an operator on 0-half-densities with the coefficients
[Hin23e, (1.3)] it has on functions. Only integer orders are used in this section's appeals to X̂.

*Full ellipticity* ([Hin23e, (1.3)–(1.5), (1.7) and Definition 1.2, pp. 4–5]). Near a boundary point (0, y_0), in local
coordinates, a 0-differential operator of order m on 0-half-densities is P = Σ_(j+|β|≤m) a_(jβ)(x, y)(xD_x)^j(xD_y)^β.
Its reduced normal operator at y_0 is N̂(P, y_0, η̂) = Σ_(j+|β|≤m) a_(jβ)(0, y_0)(tD_t)^j(tη̂)^β on [0, ∞)_t, η̂ a unit
covector; its indicial family is I(P, y_0, σ′) := Σ_(j≤m) a_(j0)(0, y_0)σ′^j, and Spec_b(P, y_0) is the set of (z, k) ∈
ℂ × ℕ_0 such that I(P, y_0, σ′)⁻¹ has a pole at σ′ = −iz of order at least k + 1. For P with elliptic principal symbol
and α ∈ ℝ, N̂(P, y_0, η̂) is *invertible at the weight α* if (1) α ≠ Re z for all (z, k) ∈ Spec_b(P, y_0); (2) if u ∈
t^αL²([0, ∞], |dt/t|) solves N̂(P, y_0, η̂)u = 0, then u = 0; (3) if v ∈ t^(−α)L²([0, ∞], |dt/t|) solves N̂(P, y_0,
η̂)*v = 0, then v = 0, the adjoint being taken with respect to |dt/t|. P is *fully elliptic at the weight α* if this
holds for all y_0 and η̂.

**Lemma {#lem:ii-f-5-4}** (The reduced normal operator.) Let σ ∈ ℂ, ω_0 ∈ 𝕊³ and α ∈ I_σ := (−2 Im σ, 2(c + S̄)). Then
P̂ is fully elliptic at the weight α in the sense of [Hin23e, Definition 1.2], at every boundary point.

*Proof.* In normal coordinates y on 𝕊³ centred at ω_0, write P̂ near (0, ω_0) in the form [Hin23e, (1.3)]. The
coefficients of the terms with |β| ≤ 1 or with factors (x∂_x)^jx² vanish at x = 0, except those of the first term of
[[eq:ii-f-5-3]]: x²P⁽⁰⁾(0, ω, ½x∂_x, ∂_ω) equals g^(ij)(y)(xD_(y_i))(xD_(y_j)) plus terms with a factor x, because
P⁽⁰⁾(0, ·) − ((ρD_ρ)² + Δ_(𝕊³)) Id ∈ Diff¹_b ([[lem:ii-c-1-2]]) and x²∂_ω = x·x∂_ω, x²(x∂_x) = x·x(x∂_x). So [Hin23e,
(1.4)–(1.5)] give the reduced normal operator

    N̂(P̂, ω_0, η̂) = −½(t∂_t − 2iσ)(t∂_t − 2(c + S_*)) + κ²t²,      S_* := S_0(ω_0),  κ² := g^(ij)(ω_0)η̂_iη̂_j > 0.

(1) The indicial operator is the first term, and det[−½(z − 2iσ)(z − 2(c + S_*))] = 0 exactly for z = 2iσ and z ∈ 2(c +
spec S_*), with real parts −2 Im σ and 2(c + Re d) ≥ 2(c + S̄), d ∈ spec S_* (S̄ as in [[eq:i-a-1-2]]). With the
convention of [Hin23e] (xD_x ↦ σ′, poles at σ′ = −iz) these are the points of Spec_b, and none has real part α.

(2) Let u ∈ t^αL²((0, ∞), |dt/t|; ℂ^(N_E)) with N̂u = 0; u is smooth, the equation being a regular linear ODE on (0, ∞).
Choose a unitary U with U⁻¹S_*U upper triangular, with diagonal entries d_1, …, d_(N_E). The components u_(N_E),
u_(N_E−1), … of U⁻¹u satisfy, in this order, scalar equations −½(t∂_t − 2iσ)(t∂_t − 2μ)u_i + κ²t²u_i = f_i, μ := c +
d_i, where f_i is a combination of the (t∂_t − 2iσ)u_j, j > i; so by induction it suffices that the scalar equation with
f = 0 has no nonzero solution in t^αL². Put u = t^pw, p := iσ + μ. Since (t∂_t − 2iσ)(t∂_t − 2μ)t^p = t^p(t∂_t + ν)(t∂_t
− ν) with ν := μ − iσ (as p − 2iσ = μ − iσ = ν and p − 2μ = −ν), the equation becomes ((t∂_t)² − ν² − 2κ²t²)w = 0, which
in s := √2κt is the modified Bessel equation s²w″ + sw′ − (s² + ν²)w = 0 ([DLMF, (10.25.1)]). Here Re ν = Re μ + Im σ,
and w ∈ t^aL²(|dt/t|) with a := α + Im σ − Re μ; α < 2(c + S̄) ≤ 2 Re μ gives a < Re ν, and α > −2 Im σ gives a > −Re ν.
So Re ν > |a| ≥ 0. The solutions are w = AI_ν(s) + BK_ν(s): the Wronskian is 𝒲{K_ν, I_ν}(s) = 1/s ([DLMF, (10.28.2)]),
so this is the general solution for every ν. As s → ∞, I_ν(s) = (2πs)^(−1/2)e^s(1 + O(s⁻¹)) and K_ν(s) =
(π/(2s))^(1/2)e^(−s)(1 + O(s⁻¹)) ([DLMF, (10.40.1)–(10.40.2)]), so w ∈ t^aL² near ∞ forces A = 0. As s → 0, for Re ν >
0, K_ν(s) ∼ ½Γ(ν)(s/2)^(−ν) ([DLMF, (10.30.2)]), and Γ(ν) ≠ 0; so |w| ≥ c|B|s^(−Re ν) near 0, which lies in
s^aL²(|ds/s|) near 0 only if −Re ν > a. Hence B = 0.

(3) The adjoint for |dt/t| and the standard Hermitian form is N̂* = −½(t∂_t + 2(c + S_*^*))(t∂_t − 2iσ̄) + κ²t², as
(t∂_t)* = −t∂_t. In the same basis U⁻¹S_*^*U is lower triangular with diagonal d̄_i, so the components are solved in the
order 1, 2, …, and the scalar equation −½(t∂_t + 2μ̄)(t∂_t − 2iσ̄)v = −κ²t²v becomes, with v = t^pw, p := iσ̄ − μ̄, the
modified Bessel equation of order ν̄, Re ν̄ = Re ν. Now v ∈ t^(−α)L² gives w ∈ t^(−a)L², as Re p = Im σ − Re μ, and |−a|
< Re ν̄; the argument of (2) gives v = 0. ∎

**Lemma {#lem:ii-f-5-5}** (The model's Fredholm property.) Let Im σ > −γ_I. (a) For every m ∈ ℤ, P̂ : x^(2γ_I)H^m_0(X̂)
→ x^(2γ_I)H^(m−2)_0(X̂) is Fredholm, and so is the formal adjoint P̂* (for μ_b and the standard Hermitian form) :
x^(−2γ_I)H^(2−m)_0(X̂) → x^(−2γ_I)H^(−m)_0(X̂). (b) For m ∈ ℤ, M′ ∈ ℕ, β < 2γ_I and β′ < −2γ_I there is C with

    ‖w‖_(x^(2γ_I)H^m_0) ≤ C(‖P̂w‖_(x^(2γ_I)H^(m−2)_0) + ‖w‖_(x^βH^(−M′)_0)),
    ‖w‖_(x^(−2γ_I)H^(2−m)_0) ≤ C(‖P̂*w‖_(x^(−2γ_I)H^(−m)_0) + ‖w‖_(x^(β′)H^(−M′)_0)).   {#eq:ii-f-5-5}

*Proof.* (a) 2γ_I ∈ I_σ: 2γ_I > −2 Im σ by assumption and 2γ_I < 2(c + S̄). Choose α_0 < 2γ_I < α_1 and ϵ > 0 with [α_0
− ϵ, α_1 + ϵ] ⊂ I_σ. By [[lem:ii-f-5-4]], P̂ is fully elliptic at every weight there. [Hin23e, Theorem 3.4, p. 33]
states: for α_0 < α_1 and P ∈ Ψ^m_0(X, ⁰Ω^(1/2)) fully elliptic at all weights in [α_0 − ϵ, α_1 + ϵ] for some small ϵ >
0, there exist Q, Q′ ∈ Ψ^(−m)_0 + Ψ_0^(−∞,(α_1,−α_0+(n−1))) + Ψ^(−∞,(α_1,−α_0+(n−1))) with PQ = I − R and Q′P = I − R′,
R ∈ Ψ^(−∞,(∞,−α_0+(n−1))) and R′ ∈ Ψ^(−∞,(α_1,∞)), n = dim X. Here n = dim X̂ = 4, so n − 1 = 3, and we obtain Q, Q′ ∈
Ψ^(−2)_0 + Ψ_0^(−∞,(α_1,3−α_0)) + Ψ^(−∞,(α_1,3−α_0)) with P̂Q = I − R, Q′P̂ = I − R′, R ∈ Ψ^(−∞,(∞,3−α_0)) and R′ ∈
Ψ^(−∞,(α_1,∞)) (fully residual operators on X̂²). Put α := 2γ_I. A Schwartz kernel kπ_L*ν_0^(1/2)π_R*ν_0^(1/2) acts on
functions by g ↦ ∫k(·, z′)g(z′)ν_0(z′), so T_(α_L,α_R) := x^(−α_L)Tx^(α_R) has the kernel κ := x^(−α_L)k x′^(α_R−3)
against μ_b(z′).

(i) *Fully residual kernels.* If |k| ≤ Cx^ax′^b on X̂² with a > α_L and b > 3 − α_R, then ∫|κ|μ_b(z′) ≤
Cx^(a−α_L)∫x′^(b+α_R−3)μ_b(z′) ≤ C and ∫|κ|μ_b(z) ≤ Cx′^(b+α_R−3)∫x^(a−α_L)μ_b(z) ≤ C, as ∫_0 x^δ dx/x < ∞ for δ > 0; by
Schur's test T_(α_L,α_R) is bounded on L²(μ_b).

(ii) *Kernels on the 0-double space.* Let k satisfy |k| ≤ Cρ_lb^aρ_rb^b on X̂²_0 with a > α, b > 3 − α and α_L = α_R =
α. Near the boundary diagonal, in coordinates (x, y, x′, y′), ρ_lb ∼ x/r and ρ_rb ∼ x′/r, r := x + x′ + |y − y′|. For
fixed z = (x, y) substitute z′ = (xs, y + xY): μ_b(z′) = x³s⁻¹ds dY, r = x(1 + s + |Y|), and ∫|κ|μ_b(z′) ≤ C∫_0^∞∫_(ℝ³)
s^(α+b−4)(1 + s + |Y|)^(−a−b)dY ds; the Y-integral is C(1 + s)^(3−a−b) (as a + b > 3), and ∫_0 s^(α+b−4)ds < ∞ (as α +
b > 3), ∫^∞ s^(α−a−1)ds < ∞ (as a > α). For fixed z′ substitute z = (x′s, y′ + x′Y): μ_b(z) = x′³s⁻¹ds dY, and
∫|κ|μ_b(z) ≤ C∫s^(a−α−1)(1 + s + |Y|)^(−a−b)dY ds < ∞, as a > α and α + b > 3. Away from the boundary diagonal |k| ≤
Cx^ax′^b, which is covered by (i). So T_(α,α) is bounded.

With a = α_1 and b = 3 − α_0, (i) and (ii) bound the residual parts of Q and Q′ on x^αL²(μ_b). Their kernels are
conormal ([Hin23e, Section 2]: 𝒜^(α_lb,α_rb) is stable under the vector fields tangent to lb and rb), and the 0-fields
of either factor lift to X̂²_0 tangent to lb, rb and ff ([Hin23e, Section 1]); so the same bounds hold after applying
them on either side, and these parts map x^αH^(m−2)_0 to x^αH^m_0 for every integer m. The part in Ψ^(−2)_0 does so by
the boundedness of the small 0-calculus on weighted 0-Sobolev spaces ([MM87], which [Hin23e, Corollary 3.3] uses in the
same way). By (i) with α_R = α and α < α_L < α_1, R′ maps x^αH^m_0 boundedly into x^(α_L)H^(m+1)_0, which embeds
compactly in x^αH^m_0 ([[lem:ii-f-5-3]]); likewise R (a = ∞, b = 3 − α_0 > 3 − α) is compact on x^αH^(m−2)_0. So Q′P̂ =
I − R′ and P̂Q = I − R make P̂ Fredholm at the weight α = 2γ_I: finite-dimensional kernel and closed range from the
first, finite codimension from the second. This is [Hin23e, Corollary 3.6, p. 34] at α = 2γ_I, whose proof [Hin23e]
leaves to the reader. Under the L²(μ_b) pairing the duals of x^(2γ_I)H^m_0 and x^(2γ_I)H^(m−2)_0 are x^(−2γ_I)H^(−m)_0
and x^(−2γ_I)H^(2−m)_0 ([[lem:ii-a-7-1]]), and the Banach adjoint of P̂ acts on them as the formal adjoint P̂* (test
against C^∞_c(X̂°), which is dense). The adjoint of a Fredholm operator is Fredholm.

(b) [[lem:ii-f-5-2]] with the injections x^(2γ_I)H^m_0 ↪ x^βH^(−M′)_0 and x^(−2γ_I)H^(2−m)_0 ↪ x^(β′)H^(−M′)_0. ∎

#### The Fredholm property {#sec:ii-f-5-4}

Under the L²(μ_b) pairing ([[lem:ii-a-7-1]]), (𝒳^𝗌)* = H^(−𝗌,(−2γ_I,−γ_cf))_(0,b) and (𝒴^(𝗌−2))* =
H^(2−𝗌,(−2γ_I−2,2−γ_cf))_(0,b); N⁰(σ)* denotes the formal adjoint for μ_b and the standard Hermitian form on ℂ^(N_E),
which is the Banach adjoint of [[eq:ii-f-5-2]] at k = 0 on these spaces.

**Lemma {#lem:ii-f-5-6}** ([Hin26c, Lemma 10.9] in dimension 4 + 1.) Let Im σ > −γ_I, let 𝗌 be an order and M ∈ ℕ with
M > sup|𝗌| + 1. Put 𝒵_M := H^(−M,(2γ_I−1,γ_cf−1))_(0,b) and 𝒵*_M := H^(−M,(−2γ_I−3,1−γ_cf))_(0,b).

(a) There is C with

    ‖u‖_(𝒳^𝗌) ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒵_M)),    u ∈ 𝒳^𝗌,   {#eq:ii-f-5-6}

    ‖v‖_((𝒴^(𝗌−2))*) ≤ C(‖N⁰(σ)*v‖_((𝒳^𝗌)*) + ‖v‖_(𝒵*_M)),    v ∈ (𝒴^(𝗌−2))*,   {#eq:ii-f-5-7}

and the inclusions 𝒳^𝗌 ↪ 𝒵_M and (𝒴^(𝗌−2))* ↪ 𝒵*_M are compact.

(b) N⁰(σ) : 𝒳^𝗌 → 𝒴^(𝗌−2) is Fredholm of index 0.

(c) If u ∈ 𝒳^𝗌 and N⁰(σ)u ∈ 𝒴^(𝗌′−2)_k with 𝗌′ ≥ 𝗌 and k ∈ ℕ_0, then u ∈ 𝒳^(𝗌′)_k.

*Proof.* (a) *Step 1: the elliptic estimate.* N⁰(σ) is elliptic in x_I²ρ_K⁻²Diff²_(0,b) ([[sec:ii-f-1-3]]), so
microlocal elliptic regularity in the calculus of the structure of [[sec:ii-a-6-2]] ((S5) of [[sec:ii-a-3]], with (S8)
for variable orders, and B = I) gives, as in [[lem:ii-a-8-4]] (c),

    ‖u‖_(𝒳^𝗌) ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒳^(−M)))                                                     {#eq:ii-f-5-8}

(the remainder of (S5) is bounded by ‖u‖_(𝒳^(−M))). Let χ ∈ C^∞_c([0, 2)) equal 1 on [0, 1], read as χ(R), and χ_1(x_I)
the same function of x_I. Since 1 − χ(R) is supported in {R ≥ 1} = {x_I ≤ 1}, where χ_1(x_I) = 1, ‖u‖_(𝒳^(−M)) ≤
‖χ(R)u‖_(𝒳^(−M)) + C‖χ_1(x_I)u‖_(𝒳^(−M)).

*Step 2: near ι⁺ ∩ K⁺.* There the 0,b-structure is the b-structure of the end ϱ = R, t = −log R, in the sense of
[[sec:i-c-2-2]] ([[sec:ii-a-6-2]], the cells U_(2,jk±)), and ‖χu‖_(𝒳^(−M)) ∼ ‖χu‖_(H^(−M)_(b,γ_cf)). The operator L_K :=
R²N⁰(σ) = −2R(iσ + R∂_R)(R∂_R + c + S_0) + P⁽⁰⁾(0, ω, −R∂_R, ∂_ω) is of the form of [[sec:i-c-2-5]] on {R < 4}, with B_j
polynomial in R, normal operator P⁽⁰⁾(0, ω, −R∂_R, ∂_ω), Mellin symbol J(ζ) = I(−ζ) and spec_J = −spec_b, as for the
operator at ztf in [[sec:i-c-4-1]] (c); and it is b-elliptic, its principal symbol in (t, ω) being (1 + 2R)τ_t² + |η|²,
τ_t the covector dual to t. As −γ_cf ∈ (β_−, β_+), γ_cf ∉ Re spec_J, and [[lem:i-c-2-6]] ([[eq:i-c-2-3]]) with m = −M
and c = γ_cf gives, with χ̃ ∈ C^∞_c([0, 3)) equal to 1 on [0, 2],

    ‖χu‖_(H^(−M)_(b,γ_cf)) ≤ C(‖χ̃L_Ku‖_(H^(−M−2)_(b,γ_cf)) + ‖χ̃u‖_(H^(−M)_(b,γ_cf−1)))
                         ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒵_M)),

since R² moves the weight γ_cf − 2 of 𝒴 to γ_cf and −M − 2 ≤ 𝗌 − 2.

*Step 3: near ι⁺ ∩ ℐ⁺.* χ_1u is supported in {x < 2} and lies in x^(2γ_I)H^(−M)_0(X̂), transplanted. On {x < 3}, P̂ =
L_σ = x⁻²N⁰(σ), so P̂(χ_1u) = x⁻²(χ_1N⁰(σ)u + [N⁰(σ), χ_1]u), the commutator being a first-order operator with
coefficients supported in {1 ≤ x_I ≤ 2}, a compact subset of (ι⁺)°. [[lem:ii-f-5-5]] (b) with m = −M, M′ = M and β =
2γ_I − 1 gives

    ‖χ_1u‖_(𝒳^(−M)) ≤ C(‖χ_1N⁰(σ)u‖_(𝒴^(−M−2)) + ‖u‖_(H^(−M−1)({1≤x_I≤2})) + ‖χ_1u‖_(𝒵_M))
                    ≤ C(‖N⁰(σ)u‖_(𝒴^(𝗌−2)) + ‖u‖_(𝒵_M)),

using that on a compact subset of (ι⁺)° all weights are equivalent.

Steps 1–3 give [[eq:ii-f-5-6]]. For [[eq:ii-f-5-7]] the same three steps apply to N⁰(σ)*, which is elliptic with the
same (real, scalar) principal symbol. Near K⁺: N⁰(σ)* = L_K*R⁻², and w := R⁻²v has the b-weight −γ_cf when v has 2 −
γ_cf. L_K* (for μ_b = |(dR/R) dω|, under which (R∂_R)* = −R∂_R) is of the same form, with Mellin symbol J(−ζ̄)*, so
spec_(J*) is the complex conjugate of spec_b, and −γ_cf ∉ Re spec_b; [[lem:i-c-2-6]] at c = −γ_cf applies (as [[ch:s03]]
applies it to adjoints in [[sec:i-c-3-1]] and [[sec:i-c-4-4]]), with remainder ‖χ̃R⁻²v‖_(H^(−M)_(b,−γ_cf−1)) =
‖χ̃v‖_(H^(−M)_(b,1−γ_cf)). Near ℐ⁺: N⁰(σ)* = L_σ*x², and w := x²v lies in x^(−2γ_I)H_0 when v lies in x^(−2γ_I−2)H_0;
the second estimate of [[eq:ii-f-5-5]] with m = M + 2 (so 2 − m = −M) and β′ = −2γ_I − 1 gives the remainder
‖χ_1x²v‖_(x^(−2γ_I−1)H^(−M)_0) ∼ ‖χ_1v‖_(x^(−2γ_I−3)H^(−M)_0), which is the weight of 𝒵*_M.

The inclusions are compact by [[lem:ii-f-5-3]]: every weight drops by 1, and the orders drop from 𝗌, resp. 2 − 𝗌, to −M,
below both as M > sup|𝗌| + 1.

(b) By [[eq:ii-f-5-6]] and the compact inclusion, N⁰(σ) has finite-dimensional kernel and closed range (Peetre's lemma,
as in [[sec:i-a-7-3]]). By [[eq:ii-f-5-7]], the kernel of N⁰(σ)* on (𝒴^(𝗌−2))*, which is the annihilator of the range,
is finite-dimensional. So [[eq:ii-f-5-2]] is Fredholm at k = 0. *Index.* The kernel does not depend on 𝗌: if N⁰(σ)u = 0
with u ∈ 𝒳^𝗌, then u ∈ 𝒳^(𝗌′) for every 𝗌′ by (c); likewise the kernel of the adjoint, by the same elliptic regularity
for N⁰(σ)*. So the index does not depend on 𝗌, and we may take 𝗌 constant. For σ, σ′ in the half-plane {Im σ > −γ_I},
N⁰(σ) − N⁰(σ′) = −2i(σ − σ′)R⁻¹(R∂_R + c + S_0), which maps 𝒳^𝗌 → 𝒴^(𝗌−2) with norm at most C|σ − σ′| (R⁻¹ is x_I² near
ℐ⁺, and near K⁺ it changes the weight γ_cf to γ_cf − 1, which is stronger than γ_cf − 2). So σ ↦ N⁰(σ) is continuous
into the Fredholm operators on the connected half-plane, and the index is constant there. At σ = i/h, with h small,
[[prop:ii-f-3-1]] (with z = i ∈ 𝒵^i, any γ_+ < γ_I, and the constant fibre order 𝗌) gives invertibility on these spaces.
So the index is 0.

(c) The elliptic parametrix of [[lem:ii-a-8-4]] (b), whose proof uses only (S5) and applies verbatim to the structure of
[[sec:ii-a-6-2]] with B = I, gives I = QN⁰(σ) + R_J with Q of order −2 (weights x_I⁻²ρ_K²) and R_J of order −J; so u =
QN⁰(σ)u + R_Ju ∈ 𝒳^(min(𝗌′,𝗌+J)), and, repeating, u ∈ 𝒳^(𝗌′). For k ≥ 1 put s_1 := inf 𝗌′, a constant; then u ∈ 𝒳^(s_1)
and N⁰(σ)u ∈ 𝒴^(s_1−2)_k. *b-regularity at the constant order s_1.* Argue by induction on k exactly as in the proof of
[[lem:ii-f-4-4]], with [[eq:ii-f-5-6]] at the order s_1 (and M > |s_1| + 2) in place of [[eq:ii-f-3-4]]. The dilations
D_κ, κ ∈ [½, 2], and the rotations act boundedly and uniformly on 𝒳^(s_1), 𝒴^(s_1−2) and 𝒵_M (constant orders; the
weights x_I^aρ_K^c and μ_b change by factors bounded above and below). G_θN⁰(σ)G_θ⁻¹ is e^(−θ)(−2R⁻¹(iσ + R∂_R)(R∂_R +
c + S_0)) + e^(−2θ)R⁻²P⁽⁰⁾(0, ω, −R∂_R, ∂_ω) for dilations and the transported operator for rotations, so the
commutators [T_θ, N⁰(σ)] and their iterates are uniformly bounded 𝒳^(s_1) → 𝒴^(s_1−2) after composition with G_θ. In the
inductive step T^α_θu is an average of transported copies of W^(α_1)T^(α′)_(θ′)u with T^(α′)_(θ′)u bounded in 𝒳^(s_1),
hence bounded in H^(s_1−1,(2γ_I−1,γ_cf))_(0,b) ⊂ 𝒵_M, because a b-field maps 𝒳^(s_1) there (Z_a = x_I⁻¹·x_IZ_a near ℐ⁺).
So [[eq:ii-f-5-6]] bounds T^α_θu in 𝒳^(s_1), and a weak limit point as θ → 0 is W^αu; thus u ∈ 𝒳^(s_1)_k. *The order
𝗌′.* For |α| ≤ k, [W^α, N⁰(σ)] = Σ_(|β|<|α|) A_(αβ)W^β with A_(αβ) ∈ x_I²ρ_K⁻²Diff²_(0,b), as each [W_i, N⁰(σ)] is of
that class and the b-fields normalise the 0,b-fields ([∂_ω, x_I∂_ω] ∈ x_I𝒱(𝕊³), [x_I∂_(x_I), x_I∂_ω] = x_I∂_ω). By
induction on |α|, N⁰(σ)W^αu = W^αN⁰(σ)u − Σ A_(αβ)W^βu ∈ 𝒴^(𝗌′−2) and W^αu ∈ 𝒳^(s_1), so the elliptic regularity just
proved puts W^αu in 𝒳^(𝗌′). ∎

#### The kernel {#sec:ii-f-5-5}

**Lemma {#lem:ii-f-5-7}** (The Fourier transform of conormal functions.) Let a > −1, b ∈ ℝ, and let f ∈ C^∞((0, ∞)_v ×
𝕊³; ℂ^(N_E)) satisfy, for all j and α, |(v∂_v)^j∂^α_ωf| ≤ C_(jα)v^a on {v ≤ 2} and ≤ C_(jα)v^(−b) on {v ≥ ½}. Let f^♯ be
its extension by 0 to v ≤ 0, a tempered distribution on ℝ × 𝕊³, and f̂(r̂, ω) := (ℱf^♯)(r̂, ω) = ∫e^(ir̂v)f^♯(v, ω) dv.
Then f̂ is smooth on {r̂ ≠ 0}, and for every ϵ > 0, j and α,

    |(r̂∂_r̂)^j∂^α_ωf̂(r̂, ω)| ≤ C(1 + |r̂|)^(−1−a)(|r̂|/(1 + |r̂|))^(min(b−1,0)−ϵ),    r̂ ≠ 0.   {#eq:ii-f-5-9}

*Proof.* Let ψ ∈ C^∞_c((½, 2)) with Σ_(l∈ℤ) ψ(2^(−l)v) = 1 for v > 0, and f_l := ψ(2^(−l)v)f. Then f^♯ = Σ_l f_l in 𝒮′
(f^♯ is locally integrable, as a > −1, and polynomially bounded; dominated convergence). On supp f_l, v ∼ 2^l, and as
∂_v^m = v^(−m)p_m(v∂_v) for a polynomial p_m, |∂_v^m∂^α_ωf_l| ≤ C2^(−lm)M_l with M_l := 2^(la) for l ≤ 0 and 2^(−lb) for
l ≥ 0. Hence |∂^α_ωℱf_l(r̂)| ≤ ∫|∂^α_ωf_l| dv ≤ C2^lM_l and, integrating by parts m times, ≤ C|r̂|^(−m)2^(l(1−m))M_l; so
|∂^α_ωℱf_l(r̂)| ≤ C2^lM_l min(1, (2^l|r̂|)^(−m)). Since ℱ(∂_v(vg)) = −r̂∂_r̂ℱg (ℱ∂_v = −ir̂ℱ, ℱv = −i∂_r̂ℱ),
(r̂∂_r̂)^jℱf_l = ℱ((−v∂_v − 1)^jf_l), and (v∂_v + 1)^jf_l is a sum of terms of the same dyadic form with the same
bounds; so the bound holds for (r̂∂_r̂)^j∂^α_ωℱf_l too. Fix r̂ ≠ 0 and K ∈ ℤ with 2^(−K) ≤ |r̂| < 2^(1−K), and take m >
max(1 + a, 1 − b). If |r̂| ≥ 1 (K ≤ 0): Σ_(l≤K) 2^(l(1+a)) ≤ C2^(K(1+a)); Σ_(K<l≤0) 2^(l(1+a))(2^l|r̂|)^(−m) ≤
C|r̂|^(−m)2^(K(1+a−m)); Σ_(l>0) 2^(l(1−b))(2^l|r̂|)^(−m) ≤ C|r̂|^(−m); all are ≤ C|r̂|^(−1−a). If |r̂| < 1 (K ≥ 1):
Σ_(l≤0) 2^(l(1+a)) ≤ C; Σ_(0<l≤K) 2^(l(1−b)) ≤ C(1 + 2^(K(1−b)) + K) ≤ C|r̂|^(min(b−1,0)−ϵ); Σ_(l>K)
2^(l(1−b))(2^l|r̂|)^(−m) ≤ C|r̂|^(−m)2^(K(1−b−m)) ≤ C|r̂|^(b−1), which is ≤ C|r̂|^(min(b−1,0)). So Σ_l ℱf_l converges
with all these derivatives locally uniformly on {r̂ ≠ 0}, to a smooth function satisfying [[eq:ii-f-5-9]], which is f̂
there because ℱ is continuous on 𝒮′. ∎

The proof uses a > −1 only, for the local integrability of f^♯ and the sums Σ_(l≤K) 2^(l(1+a)), and [[prop:iii-g-3-2]]
uses the lemma so. [[lem:ii-f-5-7]] is the bound [Hin26c, (10.41)], which [Hin26c] quotes from [Hin23d, Lemma 2.25]; it
is one-dimensional in v, the sphere being a parameter, and so does not depend on n.

**Lemma {#lem:ii-f-5-8}** ([Hin26c, Lemma 10.10] in dimension 4 + 1.) Let Im σ > −γ_I and Im σ > −1 − β_+. Then N⁰(σ)
has trivial kernel on 𝒳^𝗌.

*Proof.* Let N⁰(σ)u = 0, u ∈ 𝒳^𝗌. By [[lem:ii-f-5-6]] (c), u ∈ 𝒳^(s′)_k for all s′ and k; so ρ_0f^(−2γ_I)ρ_K^(−γ_cf)W^αu
∈ L²(μ_b) for every product W^α of b-fields (the weights commute with b-fields up to bounded factors; the weight at ℐ⁺
of the spaces is the bounded defining function ρ_0f = (1 + R)^(−1/2), which near ℐ⁺ is x_I times a smooth positive
function), and Sobolev embedding on the unit cells of the b-structure of ι⁺ (dimension 4; as in the proof of
[[lem:i-a-7-4]] (b)) gives u ∈ ρ_0f^(2γ_I)ρ_K^(γ_cf)C^∞_b(ι⁺). In v := R⁻¹ ∈ [0, ∞], ρ_0f² = v/(1 + v) and ρ_K = (1 +
v)⁻¹, so u ∈ v^(γ_I)(1 + v)^(−γ_I−γ_cf)C^∞_b, and the b-fields are spanned by v∂_v = −R∂_R and the Z_a. So u_0 :=
v^(−iσ)u satisfies the hypotheses of [[lem:ii-f-5-7]] with

    a := γ_I + Im σ > 0,    b := γ_cf − Im σ,   {#eq:ii-f-5-10}

as |v^(−iσ)| = v^(Im σ) and v∂_v(v^(−iσ)g) = v^(−iσ)(v∂_v − iσ)g.

*The operator in v.* Conjugation by R^(iσ) replaces R∂_R by R∂_R − iσ, as R^(iσ)R∂_R(R^(−iσ)g) = (R∂_R − iσ)g. So
R^(iσ)R²N⁰(σ)R^(−iσ) = −2R(R∂_R)(R∂_R − iσ + c + S_0) + P⁽⁰⁾(0, ω, −R∂_R + iσ, ∂_ω), the factor iσ + R∂_R of
[[eq:ii-f-1-6]] becoming R∂_R. With R∂_R = −v∂_v and R(R∂_R) = R²∂_R = −∂_v,

    N¹(σ) := R^(iσ)R²N⁰(σ)R^(−iσ) = −2∂_v(v∂_v + iσ − c − S_0) + P⁽⁰⁾(0, ω, v∂_v + iσ, ∂_ω)   {#eq:ii-f-5-11}

([Hin26c, before (10.40)], with c = 1 there), and N¹(σ)u_0 = R^(iσ)R²N⁰(σ)u = 0 on {v > 0}. Let u^♯ be the extension of
u_0 by 0 to v ≤ 0. Then N¹(σ)u^♯ = 0 on ℝ × 𝕊³: for φ ∈ C^∞_c(ℝ × 𝕊³; ℂ^(N_E)), ⟨u^♯, N¹(σ)^tφ⟩ = lim_(ϵ↓0) ∫_(v>ϵ)
u_0·N¹(σ)^tφ dv dω, and Green's formula on {v > ϵ} turns this into ∫_(v>ϵ)(N¹(σ)u_0)·φ + B_ϵ = B_ϵ, where B_ϵ is an
integral over {ϵ} × 𝕊³ of products of (v∂_v)^l∂^γ_ωu_0, l ≤ 1, |γ| ≤ 2, with derivatives of φ, with bounded coefficients
(each v-integration by parts of ∂_v or of v∂_v leaves one boundary term, and the ω-integrations by parts none). So |B_ϵ|
≤ C_φϵ^a → 0. u^♯ is tempered, and ℱ(∂_vg) = −ir̂ℱg, ℱ(vg) = −i∂_r̂ℱg, hence ℱ(v∂_vg) = −i∂_r̂(−ir̂ℱg) = −(r̂∂_r̂ +
1)ℱg. As P⁽⁰⁾(0, ω, ·, ∂_ω) is a polynomial with coefficients that are operators on 𝕊³, which commute with ℱ, the
substitutions ∂_v ↦ −ir̂ and v∂_v ↦ −(r̂∂_r̂ + 1) in [[eq:ii-f-5-11]] give, for û := ℱu^♯ in 𝒮′(ℝ × 𝕊³),

    [2ir̂(−r̂∂_r̂ + iσ − (c + 1) − S_0) + P⁽⁰⁾(0, ω, −r̂∂_r̂ − 1 + iσ, ∂_ω)]û = 0:   {#eq:ii-f-5-12}

indeed −2(−ir̂)(−(r̂∂_r̂ + 1) + iσ − c − S_0) = 2ir̂(−r̂∂_r̂ + iσ − (c + 1) − S_0). This is [Hin26c, (10.40)], with iσ −
2 − S there (c = 1) and iσ − 5/2 − S_0 here.

*Reduction to the transition face.* For r̂ > 0 put w_±(r̂, ω) := û(±r̂, ω) and w^♭_± := r̂^(1−iσ)w_±. Conjugation by
r̂^(1−iσ) replaces r̂∂_r̂ by r̂∂_r̂ − 1 + iσ, and r̂ ↦ −r̂ changes the sign of the first term of [[eq:ii-f-5-12]] only;
under the replacement, −r̂∂_r̂ + iσ − (c + 1) − S_0 becomes −r̂∂_r̂ − c − S_0 and −r̂∂_r̂ − 1 + iσ becomes −r̂∂_r̂. So
on {r̂ > 0}, with ρ̂ := r̂⁻¹ (r̂∂_r̂ = −ρ̂∂_ρ̂) and after multiplication by ρ̂²,

    [±2iρ̂(ρ̂∂_ρ̂ − c − S_0) + ρ̂²P⁽⁰⁾(0, ω, ρ̂∂_ρ̂, ∂_ω)]w^♭_± = N_tf(±1)w^♭_± = 0,   {#eq:ii-f-5-13}

with N_tf of [[eq:i-c-4-1]] (see [[eq:ii-f-3-14]]), on tf° = ℝ⁴_x̂ ∖ 0, x̂ = r̂ω. By [[lem:ii-f-5-7]] with
[[eq:ii-f-5-10]], |w_±| ≤ C(1 + r̂)^(−1−γ_I−Im σ)(r̂/(1 + r̂))^(min(γ_cf−Im σ−1,0)−ϵ), with the same bound for
(r̂∂_r̂)^jZ^αw_±; as |r̂^(1−iσ)| = r̂^(1+Im σ) = (1 + r̂)^(1+Im σ)(r̂/(1 + r̂))^(1+Im σ) is conormal,

    w^♭_± ∈ 𝒜^(γ_I,−β)(tf),    β := max(−γ_cf, −1 − Im σ) + ϵ,   {#eq:ii-f-5-14}

in the notation of [[sec:i-c-4-1]] (ρ_sctf = (1 + r̂)⁻¹, ρ_ztf = r̂/(1 + r̂)). Indeed the exponent at sctf is 1 + γ_I +
Im σ − (1 + Im σ) = γ_I, and at ztf it is min(γ_cf − Im σ − 1, 0) − ϵ + 1 + Im σ = min(γ_cf, 1 + Im σ) − ϵ = −β. Take
ϵ > 0 so small that β < β_+; this uses −γ_cf < β_+ and −1 − Im σ < β_+, the second hypothesis. Also β > −γ_cf > β_−.

*tf-admissibility.* Fix β* ∈ (β, β_+), q := 2 − β* ∈ (2 − β_+, 2 − β_−), and in the spaces of [[sec:i-c-4-3]] take the
real parameter α_+ there equal to 0 and orders 𝗋_± admissible as there whose value near R_out, the zero section over
sctf, is below γ_I − 2: this is allowed, admissibility imposing only an upper bound at R_out ([[lem:i-a-7-1]], as used
in the proof of [[thm:i-a-7-2]] (5)). Then w^♭_+ ∈ 𝒳_(tf,0) and w^♭_− ∈ 𝒳_(tf,π): near sctf, φ_∞w^♭_± ∈ H^(s,𝗋_±)_sc for
every s by [[lem:i-a-7-4]] (a) with a = γ_I, which concerns a neighbourhood of the boundary face of ℝ̄⁴ only (as in the
converse of [[thm:i-c-4-3]] (5)); near ztf, (1 − φ_∞)w^♭_± ∈ 𝒜^(−β) ⊂ H^∞_(b,q−2) as q − 2 = −β* < −β ([[lem:i-c-2-2]]
(f)); in between w^♭_± is smooth; and N_tf(±1)w^♭_± = 0. P̂_0 is tf-admissible with the weight α_+ + 2 = −γ_cf ∈ (β_−,
β_+) ([[def:ii-c-2-7]] (2)), so by [[cor:i-c-5-2]] (a), N_tf(e^(iθ)) : 𝒳_(tf,θ) → 𝒴_(tf,θ) is invertible at θ = 0 and
θ = π for these q and orders. Hence w^♭_± = 0, and û = 0 on {r̂ ≠ 0}.

*Conclusion.* For ψ ∈ C^∞(𝕊³; ℂ^(N_E)), g := ⟨û, ψ⟩_(𝕊³) ∈ 𝒮′(ℝ) is supported in {0}, hence a finite sum Σ_l c_lδ^((l));
so its inverse transform ⟨u^♯, ψ⟩_(𝕊³) is a polynomial in v. It vanishes on {v < 0}, so it vanishes identically. As ψ is
arbitrary, u^♯ = 0, and u = 0. ∎

#### Proof of Proposition 5.1 {#sec:ii-f-5-6}

*Proof of [[prop:ii-f-5-1]].* For k = 0, [[lem:ii-f-5-6]] (b) gives the Fredholm property with index 0, and if also Im
σ > −1 − β_+, [[lem:ii-f-5-8]] gives a trivial kernel, so [[eq:ii-f-5-2]] is invertible. Let k ≥ 1. By [[lem:ii-f-5-6]]
(c) with N⁰(σ)u = 0, the kernel on 𝒳^𝗌_k is the kernel on 𝒳^𝗌; and by [[lem:ii-f-5-6]] (c), N⁰(σ)(𝒳^𝗌_k) = 𝒴^(𝗌−2)_k ∩
N⁰(σ)(𝒳^𝗌), which is closed in 𝒴^(𝗌−2)_k since the inclusion 𝒴^(𝗌−2)_k ↪ 𝒴^(𝗌−2) is continuous. The map 𝒴^(𝗌−2)_k →
𝒴^(𝗌−2)/N⁰(σ)(𝒳^𝗌) has exactly this kernel, and it is onto: its image is dense, as C^∞_c((ι⁺)°) ⊂ 𝒴^(𝗌−2)_k is dense in
𝒴^(𝗌−2), and the quotient is finite-dimensional. So the cokernels at k and at 0 have the same dimension, [[eq:ii-f-5-2]]
is Fredholm of index 0, and it is invertible when the operator at k = 0 is. ∎

**Corollary {#cor:ii-f-5-9}** On {Im σ > max(−γ_I, −1 − β_+)}, σ ↦ N⁰(σ)⁻¹ ∈ ℒ(𝒴^(𝗌−2)_k, 𝒳^𝗌_k) is holomorphic.

*Proof.* N⁰(σ) = N⁰(σ_0) − 2i(σ − σ_0)R⁻¹(R∂_R + c + S_0) is affine in σ with values in ℒ(𝒳^𝗌_k, 𝒴^(𝗌−2)_k) (the second
term commutes with the W_i up to terms of its own class), and invertible there by [[prop:ii-f-5-1]]; near each σ_0 the
inverse is the Neumann series Σ_(j≥0)((σ − σ_0)A)^jN⁰(σ_0)⁻¹, A := 2iN⁰(σ_0)⁻¹R⁻¹(R∂_R + c + S_0), convergent for |σ −
σ_0|‖A‖ < 1. ∎

