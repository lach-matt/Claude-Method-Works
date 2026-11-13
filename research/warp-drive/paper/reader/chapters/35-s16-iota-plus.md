## Future timelike infinity: the spectral family, the ι⁺-normal operator, grafting {#ch:s16}

This chapter analyses the linearised gauge-fixed Einstein operator L_b of [[ch:s15]] at future timelike infinity ι⁺.
Near ι⁺ the operator is modelled by its Minkowski model L̄, which is homogeneous of degree −2 under the dilations
(t_*, x) ↦ (st_*, sx). The Mellin transform in the scaling turns L̄ into the *spectral family* N_sf(λ), a family of
operators on the quotient sf = ℝ_v × 𝕊³ of {x ≠ 0} by the dilations, and into the *ι⁺-normal operator* N_ι⁺(λ), the
same operator in coordinates adapted to ι⁺. The chapter proves three things. First, N_sf(λ) is Fredholm of index 0 on
spaces of distributions supported in {v ≥ −1}, invertible for Re λ < 2 and for all but finitely many λ in every half
plane {Re λ ≤ C}, with a finite-meromorphic inverse, and its solutions gain b-regularity at the light cone {v = 0}
with their right sides ([[thm:iii-g-5-1]]). Second, the inverse of N_ι⁺(λ), built from that of N_sf(λ), has an
expansion of radiation-field type at 𝓘⁺ ∩ ι⁺, with exponents 3/2 plus the small eigenvalues of the endomorphism S̄,
and is polyhomogeneous at K⁺ ∩ ι⁺ ([[thm:iii-g1-3-1]]); the poles of N_sf(λ)⁻¹ that are invisible on ι⁺ are located
([[lem:iii-g1-4-2]], [[lem:iii-g1-4-3]]). Third, the expansion at K⁺ ∩ ι⁺ consists, term by term, of formal solutions
built from zero energy states ([[thm:iii-g2-3-1]]), and a solution of the ι⁺-normal operator can be grafted into
spacetime as an approximate solution of L_b on the Myers–Perry family ([[thm:iii-g2-4-2]], [[cor:iii-g2-4-3]]).

These results are [Hin26, Section 9.1] in dimension 4 + 1: Proposition 9.2, Definition 9.3, Proposition 9.4,
Definition 9.6 and Remark 9.7, Definitions 9.8 and 9.10, Propositions 9.9 and 9.11 and Corollary 9.12 (pp. 164–179).
The dimension enters through the radiative constant c = (n − 1)/2 = 3/2, which is 1 in dimension 3 + 1, and through
the indicial roots of [[prop:iii-f1-2-3]]. Its consequences are these. The regularity threshold at the light cone is
s < 2 − Re λ (against 3/2 − Re λ in dimension 3 + 1). The spectral family is invertible for Re λ < 2 (against
1 + ε_ind): at n = 4 the indicial gap of L̃(0) contains (0, 1], and L̂_b is tf-admissible with every weight in (0, 1]
([[prop:iii-f1-3-3]]). The exponents at 𝓘⁺ ∩ ι⁺ are 3/2 + s, s a small eigenvalue of S̄. The poles of N_sf(λ)⁻¹ that
are invisible on ι⁺ lie in 5/2 + spec S̄ + ℕ_0. And the expansion at K⁺ is needed only below R³, which requires no zero
energy state at −3.

The method is that of [Hin26], with these changes. For fixed λ, the estimates of [Vas13], [Hin25a] and [HV15] used there
are replaced by those of [[ch:s01]] and [[ch:s03]], whose proofs use only properties that are verified for N_sf(λ)
here: it is the spectral family, in the dilation-invariant time T = log |x|, of a stationary operator whose principal
symbol is the dual of the metric |x|⁻²ḡ ([[lem:iii-g-1-2]] (g)); its light cone {v = 0} is a Killing horizon of ∂_T,
at whose conormal bundle the radial estimate runs with an explicit threshold ([[lem:iii-g-2-2]]); v is a time function
on {−2 < v < 0} ([[lem:iii-g-2-3]]); and v = ∞ is a b-elliptic end. The b-regularity at the light cone ([HV15,
Theorem 6.3] in [Hin26]) is proved by commuting with the dilation and with the Lie derivatives along the rotations
([[prop:iii-g-2-7]]). Injectivity is the argument of [[lem:ii-f-5-8]], which contains the Fourier transform and the
tf-normal operator of [Hin26], with the tf-admissibility of [[prop:iii-f1-3-3]]. The index is 0 because the family is
invertible for |Im λ| large in every vertical strip, by a
semiclassical estimate; across the light cone that estimate is written out with an escape function
([[lem:iii-g-4-1]] (b)), which also serves as the variable semiclassical order ([[lem:iii-g-4-2]]).

*Notation.* Throughout the chapter λ ∈ ℂ is the spectral parameter at ι⁺, dual to the scaling, and is related to the
parameter σ of [[ch:s08]] by σ = −iλ; it is not the wavelength of the approximant. The indicial roots of the operators
of [[ch:s13]] and [[ch:s15]] keep their names λ^Υ_(…) and λ^C_(…) ([[lem:iii-d-4-1]], [[sec:iii-f1-1]]). As an index
(^(*h), Re_h, Im_h) the letter h denotes a fibre inner product; in [[sec:iii-g-4]] the letter h alone is the
semiclassical parameter, and from [[sec:iii-g1-3]] on it denotes sections (solutions of N_ι⁺(λ)h = f, and metric
perturbations). The faces 𝓘⁺, ι⁺ and K⁺ of the compactified spacetime are those of [[ch:s04]]. The inner radius of the
artificial boundary plays no role in this chapter: the spectral family lives on Minkowski space, and the grafting of
[[sec:iii-g2-4]] takes place near infinity. Throughout, condition (C1) of [[sec:iii-f1-1]] is assumed, which
[[thm:iii-e-1-1]] (3) provides, and γ_Υ is small as in [[prop:iii-f1-3-3]].

### The spectral family: the operator and the spaces {#sec:iii-g-1}

This section and the next four are [Hin26, Proposition 9.2] in dimension 4 + 1.

#### The operator {#sec:iii-g-1-1}

The parameters and the operator L_b are those of [[sec:iii-f-1]] and [[sec:iii-f1-1]]. The Minkowski model L̄ is
[[eq:iii-f-2-1]]; by [[lem:iii-f-2-1]] (2), on {|x| > 0},

    2L̄ = −2∂_(t_*) ρ(ρ∂_ρ − 3/2 − S̄) + 2L̄̂(0),     2L̄̂(0) = ρ² L̃(0)(ω, ρ∂_ρ, ∂_ω),                 {#eq:iii-g-1-1}

where ρ = |x|⁻¹, S̄ is the bundle endomorphism of [[eq:iii-f-2-2]], homogeneous of degree 0, with spec S̄ ⊂ [0, ∞) and
min spec S̄ = 0 ([[eq:iii-f-3-1]]), and L̃(0) is dilation invariant. By [[lem:ii-c-1-2]], applied to P_0 = 2L_b, whose
operator P^(0) frozen at ρ = 0 is L̃(0) ([[lem:iii-f-2-1]] (3)),

    L̃(0)(ω, x, ∂_ω) = −x² + a(ω)x + Δ_(𝕊³) + V(ω, ∂_ω) + b(ω),                                         {#eq:iii-g-1-2}

with a, b smooth endomorphisms, V a first-order operator on 𝕊³ and Δ_(𝕊³) ≥ 0 acting componentwise; sections of
S²T*ℝ^(1+4) (rank 15) are trivialised by the symmetric products of dt_*, dx¹, …, dx⁴. An *indicial root* of L̃(0) is
r ∈ ℂ with ker L̃(0)(ω, r, ∂_ω) ≠ 0; these are the roots of [[prop:iii-f1-2-3]], none of which has real part in (0, 1].

On ℝ^(1+4) ∖ {x = 0} use ρ, v := ρt_* = (t − |x|)/|x| and ω. Then ∂_(t_*)|_ρ = ρ∂_v and
ρ∂_ρ|_(t_*) = ρ∂_ρ|_v + v∂_v, so [[eq:iii-g-1-1]] reads

    2ρ⁻²L̄ = −2∂_v(ρ∂_ρ + v∂_v − 3/2 − S̄) + L̃(0)(ω, ρ∂_ρ + v∂_v, ∂_ω),

whose coefficients do not depend on ρ; it commutes with ρ∂_ρ.

**Definition {#def:iii-g-1-1}** (The spectral family; [Hin26, (9.2)] in dimension 4 + 1.) For λ ∈ ℂ,

    N_sf(λ) := −2∂_v(v∂_v + λ − 3/2 − S̄) + L̃(0)(ω, v∂_v + λ, ∂_ω).                                    {#eq:iii-g-1-3}

It acts on sections over sf := ℝ_v × 𝕊³; we write R := v⁻¹ near v = +∞. Conjugation of the last display by ρ^λ
replaces ρ∂_ρ by ρ∂_ρ + λ, and ρ∂_ρ annihilates functions of (v, ω), so 2ρ⁻²L̄(ρ^λ u) = ρ^λ N_sf(λ)u for u = u(v, ω).

**Remark {#rem:iii-g-1-scalar}** (The scalar wave operator.) Let □ = ∂_t² − Δ_(ℝ⁴) on ℝ^(1+4), and write it in
(t_*, r, ω), t_* = t − r, r = |x|. Then ∂_t = ∂_(t_*) and ∂_r|_t = ∂_r|_(t_*) − ∂_(t_*), so

    □ = 2∂_(t_*)∂_r + 3r⁻¹∂_(t_*) − ∂_r² − 3r⁻¹∂_r + r⁻²Δ_(𝕊³)
      = −2∂_(t_*)ρ(ρ∂_ρ − 3/2) + ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_(𝕊³)),

using ∂_r = −ρ(ρ∂_ρ) and r²∂_r² + 3r∂_r = (r∂_r)² + 2r∂_r with r∂_r = −ρ∂_ρ. This is [[eq:iii-g-1-1]] with S̄ = 0 and
L̃(0)(x) = −x² + 2x + Δ_(𝕊³), and ρ^(−2−λ)□ρ^λ = N_sf(λ) on functions of (v, ω). The constant 3/2 is (n − 1)/2 at
n = 4; in dimension 3 + 1 it is 1.

**Lemma {#lem:iii-g-1-2}** (Structure.) (a) The principal symbol of N_sf(λ) is p_2 Id, with

    p_2(v, ω; ξ, η) := v(v + 2)ξ² + |η|²

(ξ dual to v, |η| the round norm). So N_sf(λ) is elliptic over {v > 0} ∪ {v < −2}, and on {−2 < v < 0}, p_2 is the
dual of a Lorentzian metric for which dv is timelike.

(b) Near v = ∞, with R = v⁻¹,

    N_sf(λ) = 2R(R∂_R)(−R∂_R + λ − 3/2 − S̄) + L̃(0)(ω, λ − R∂_R, ∂_ω),                                 {#eq:iii-g-1-4}

an operator L of the form of [[sec:i-c-2-5]] at the end at 0 (ϱ = R), b-elliptic on {R < 2} (its b-principal symbol
is (1 + 2R)ζ² + |η|²), with normal operator L̃(0)(ω, λ − R∂_R, ∂_ω) and Mellin symbol

    J_λ(ζ) = L̃(0)(ω, λ − ζ, ∂_ω) = −ζ² + (2λ − a)ζ + Δ_(𝕊³) + V + (b + aλ − λ²),                        {#eq:iii-g-1-5}

of the form of [[lem:i-c-2-4]]; ζ is the variable of the Mellin transform of [[sec:i-c-2-3]]. The roots of J_λ are
{λ − r}, r over the indicial roots of L̃(0).

(c) N_sf(λ) = R^(2+λ) N_ι⁺(λ) R^(−λ) on {v > 0}, with

    N_ι⁺(λ) = −2R⁻¹(R∂_R + λ)(R∂_R + 3/2 + S̄) + R⁻² L̃(0)(ω, −R∂_R, ∂_ω),                              {#eq:iii-g-1-6}

which is [Hin26, (9.10)–(9.11)] at n = 4. N_ι⁺(λ) is the operator N⁰(σ) of [[eq:ii-f-1-6]] ([[def:ii-f-1-1]]) for
P_0 = 2L_b, c = 3/2, S_0 = S̄ and P^(0)(0) = L̃(0), at σ = −iλ.

(d) N_sf(λ) commutes with the Lie derivatives ℒ_Ω along the rotation fields Ω of 𝕊³ (acting on sections of
S²T*ℝ^(1+4)).

(e) [v∂_v, N_sf(λ)] = −N_sf(λ) + L̃(0)(ω, v∂_v + λ, ∂_ω), and N_sf(λ + 1)∂_v = ∂_v N_sf(λ).

(f) N_sf(λ) − N_sf(λ′) = (λ − λ′)(−2∂_v − 2v∂_v + a − λ − λ′), a first-order operator polynomial in λ, λ′; near
v = ∞ it lies in Diff¹_b, as ∂_v = −R(R∂_R).

(g) Let ĝ := |x|⁻²ḡ on ℝ_T × sf, T := log |x|. Then

    ĝ⁻¹ = ∂_T² − 2(v + 1)∂_T∂_v + v(v + 2)∂_v² + g̸⁻¹,

g̸ the round metric; dT is spacelike, and dv is timelike exactly on {−2 < v < 0}. N_sf(λ) is the spectral family
e^(iσT) P_c e^(−iσT) at σ = −iλ of the T-independent operator P_c := 2|x|²L̄, whose principal symbol at
−σ dT + ξ dv + η is ĝ⁻¹(−σ dT + ξ dv + η) = σ² + 2(v + 1)σξ + p_2, and P_c − □_ĝ Id is a first-order operator with
T-independent coefficients.

*Proof.* (a) The second-order part of [[eq:iii-g-1-3]] is −2∂_v v∂_v − (v∂_v)² + Δ_(𝕊³), whose principal symbol is
2vξ² + v²ξ² + |η|². It is positive definite where v(v + 2) > 0, and on {−2 < v < 0} it has one negative direction, with
p_2(dv) = v(v + 2) < 0.

(b) v∂_v = −R∂_R and ∂_v = −R²∂_R = −R(R∂_R), so −2∂_v(v∂_v + λ − 3/2 − S̄) = 2R(R∂_R)(−R∂_R + λ − 3/2 − S̄). The term
−2R(R∂_R)² has b-symbol 2Rζ², and −(R∂_R)² in L̃(0) gives ζ². On R^ζ, v∂_v + λ acts as λ − ζ, and expanding
[[eq:iii-g-1-2]] at x = λ − ζ gives [[eq:iii-g-1-5]]; its roots are the ζ with λ − ζ an indicial root of L̃(0).

(c) Conjugating [[eq:iii-g-1-4]] by R^λ replaces R∂_R by R∂_R + λ: R^(−λ)N_sf(λ)R^λ =
−2R(R∂_R + λ)(R∂_R + 3/2 + S̄) + L̃(0)(ω, −R∂_R, ∂_ω). Multiplying by R⁻² gives [[eq:iii-g-1-6]], which is
[[eq:ii-f-1-6]] with these data at iσ = λ.

(d) ḡ, t_*, |x|, dt̄ and d|x| are invariant under the rotations of the spatial factor, so L̄, built from them
([[eq:iii-f-2-1]], [[sec:iii-d-2]]), commutes with ℒ_Ω; so does ρ, and ℒ_Ω preserves v.

(e) S̄ and the coefficients of L̃(0) do not depend on v, so v∂_v commutes with B := v∂_v + λ − 3/2 − S̄ and with
L̃(0)(ω, v∂_v + λ, ∂_ω), and [v∂_v, ∂_v] = −∂_v gives [v∂_v, −2∂_vB] = 2∂_vB = −(N_sf(λ) − L̃(0)(ω, v∂_v + λ, ∂_ω)).
For the second identity, ∂_v F(v∂_v) = F(v∂_v + 1)∂_v for every polynomial F, as ∂_v v∂_v = (v∂_v + 1)∂_v. So
∂_v N_sf(λ) = −2∂_v(v∂_v + 1 + λ − 3/2 − S̄)∂_v + L̃(0)(ω, v∂_v + λ + 1, ∂_ω)∂_v = N_sf(λ + 1)∂_v.

(f) By [[eq:iii-g-1-2]] with x = v∂_v, L̃(0)(ω, x + λ, ∂_ω) − L̃(0)(ω, x + λ′, ∂_ω) = (λ − λ′)(−2x − λ − λ′ + a), and
the first terms of [[eq:iii-g-1-3]] differ by −2(λ − λ′)∂_v.

(g) With r := |x| = e^T and t = r(v + 1), dt = e^T((v + 1)dT + dv) and dr = e^T dT, so

    ĝ = r⁻²(−dt² + dr² + r²g̸) = −v(v + 2) dT² − 2(v + 1) dT dv − dv² + g̸.

The (T, v)-block has determinant −1, and inverting it gives the stated ĝ⁻¹. Then ĝ⁻¹(dT, dT) = 1 > 0 and
ĝ⁻¹(dv, dv) = v(v + 2), negative exactly on (−2, 0). Next, ρ^λ = e^(−λT) = e^(−iσT) for σ = −iλ, so
N_sf(λ) = e^(iσT)P_c e^(−iσT) on T-independent sections by [[def:iii-g-1-1]]. The operator 2L̄ is homogeneous of degree
−2 under the dilations ([[eq:iii-g-1-1]]: S̄ is homogeneous of degree 0 and 2L̄̂(0) is ρ² times a dilation-invariant
operator), so P_c = 2|x|²L̄ is invariant under them, that is, its coefficients in (T, v, ω) do not depend on T; and its
principal symbol is |x|²ḡ⁻¹ = ĝ⁻¹, since 2L̄ is the wave operator of ḡ plus terms of order at most 1
([[eq:iii-f-2-1]]). The operator □_ĝ Id is T-independent with the same principal symbol, so P_c − □_ĝ Id is of first
order with T-independent coefficients. Finally
ĝ⁻¹(−σ dT + ξ dv + η) = σ² + 2(v + 1)σξ + v(v + 2)ξ² + |η|². ∎

At σ = −iλ, Im σ = −Re λ. The region {v > 0} is where ∂_T is timelike for ĝ (inside the light cone of the origin);
{v = 0} is a Killing horizon of ∂_T; {v = −2} is past null infinity; and v = ∞ is the timelike line {x = 0}, a conic
singularity of the dilation-reduced space.

#### The spaces {#sec:iii-g-1-2}

Let sf_(≥−1) := [−1, ∞]_v × 𝕊³, compactified at v = ∞ by R = v⁻¹, with the density

    μ_sf := |dv/(2 + v) dg̸|

of [Hin26, Proposition 9.2], smooth and positive on {v > −2} and a b-density at R = 0, as |dv|/(2 + v) =
|dR|/(R(1 + 2R)). Fix χ_∂ ∈ C^∞(ℝ_v) with χ_∂ = 0 on {v ≤ 2} and χ_∂ = 1 on {v ≥ 4}.

**Definition {#def:iii-g-1-3}** ([Hin26, Definition 9.1] in dimension 4 + 1.) For s, μ ∈ ℝ, Ḣ^(s,μ)_b(sf_(≥−1)) is the
space of distributions u on ℝ_v × 𝕊³ supported in {v ≥ −1} with

    ‖u‖²_(Ḣ^(s,μ)_b) := ‖(1 − χ_∂)u‖²_(H^s) + ‖χ_∂u‖²_(H^s_(b,μ)) < ∞,                                    {#eq:iii-g-1-7}

where H^s is the Sobolev space on (−2, 5) × 𝕊³ and H^s_(b,μ) is the space of [[def:i-c-2-1]] at the end at 0 with
ϱ = R. At s = 0 the second norm is that of R^(−μ)L²(μ_sf), so near v = ∞, Ḣ^(s,μ)_b = ⟨v⟩^(−μ)H^s_b, as in [Hin26].
H̄^(s,μ)_b(sf_(≥−1)) is the space of restrictions to {v > −1} of such distributions without the support condition
(extendible at v = −1), with the quotient norm. For k ∈ ℕ_0, Ḣ^((s;k),μ)_(b;b) consists of the u ∈ Ḣ^(s,μ)_b with
(v∂_v)^j ℒ_Ω^α u ∈ Ḣ^(s,μ)_b for j + |α| ≤ k, where ℒ_Ω^α are the words of length |α| in the Lie derivatives along the
six rotation fields Ω_1, …, Ω_6 of 𝕊³; Ḣ^((s;∞),μ)_(b;b) is the intersection over k.

Since ℒ_Ω differs from Ω acting componentwise by a constant matrix, the same space results with componentwise Ω. On
compact subsets of {v ≠ 0}, v∂_v and the Ω_a span the vector fields, so there Ḣ^((s;k),μ)_(b;b) is H^(s+k); near R = 0
it is H^(s+k)_(b,μ) ([[lem:i-c-2-2]] (h)).

*Duality and calculi.* With the pairing of L²(μ_sf) and a fibre inner product h (below),
(Ḣ^(s,μ)_b)* = H̄^(−s,−μ)_b: near v = −1 by [[lem:i-a-6-1]] (b), near R = 0 by [[lem:i-c-2-2]] (d), glued with χ_∂. For
Re λ in a compact set, N_sf(λ): Ḣ^(s,μ)_b → Ḣ^(s−2,μ)_b is bounded ([[lem:i-c-2-2]] (c) near R = 0, by
[[eq:iii-g-1-4]]). On {−3/2 < v < 5} we use the diffeomorphism (v, ω) ↦ x = e^v ω onto an annulus of ℝ⁴, so that the
pseudodifferential operators of [[sec:i-a-2]] and the semiclassical ones of [[sec:i-b-2]] with kernels supported there
act; the decay orders are then immaterial. Near R = 0 we use x = Rω, the end at 0 of [[ch:s03]].

**Lemma {#lem:iii-g-1-4}** (Fibre inner products.) For every δ > 0 there is a smooth fibre inner product h on
𝕊³ × ℂ¹⁵, independent of v, with Re_h S̄ := ½(S̄ + S̄^(*h)) ≥ −δ everywhere.

*Proof.* This is the construction in the proof of [[cor:iii-f1-3-4]]: at each ω, rescale a Jordan basis of S̄(ω) so
that the strict inequality holds at ω, hence near ω; the condition is convex in h, so a partition of unity on 𝕊³ glues
the local choices. It applies as min spec S̄ = 0. ∎

### Fixed λ: the Fredholm property and b-regularity {#sec:iii-g-2}

This section is [Hin26, Proposition 9.2 (1) and (3)] in dimension 4 + 1.

#### The dynamics and the radial set {#sec:iii-g-2-1}

Write ℛ_± := {v = 0, η = 0, ±ξ > 0} ⊂ T*sf ∖ o, the two halves of N*{v = 0} ∖ o, ∂ℛ_± for their images at fibre
infinity, Σ_0 := {p_2 = 0} at fibre infinity, ρ_∞ := |ξ|⁻¹ near ∂ℛ_±, η̂ := ρ_∞η, and 𝖧 := ±ρ_∞H_(p_2) near ∂ℛ_±,
the convention of [[sec:i-a-4-1]].

**Lemma {#lem:iii-g-2-1}** (Dynamics at fibre infinity.) (a) Over {v ≥ 0}, Σ_0 = ∂ℛ_+ ∪ ∂ℛ_−; over {v > 0} and over
{v < −2}, Σ_0 = ∅.

(b) Near ∂ℛ_±, 𝖧ρ_∞ = β_0ρ_∞ with β_0 = 2(1 + v), 𝖧 vanishes on ∂ℛ_±, and q̃ := v² + |η̂|² is a quadratic defining
function of ∂ℛ_± at fibre infinity with

    𝖧q̃ = 4(v + 2)v² + 4(1 + v)|η̂|² ≥ 2q̃     on {|v| ≤ ½}.

So, in the sense of [[sec:i-a-4-1]], ∂ℛ_± is a source, and the conclusion of [[lem:i-a-4-1]] holds with q̃.

(c) Over {−2 < v < 0}, 𝖧v = 2v(v + 2) < 0 on Σ_0. Every integral curve of 𝖧 in Σ_0 over {−2 < v < 0} has v strictly
decreasing, tends to ∂ℛ_+ ∪ ∂ℛ_− in the backward direction, and reaches {v < −1} in the forward direction.

*Proof.* (a) Over v = 0, p_2 = |η|², so p_2 = 0 forces η = 0; over v > 0 and v < −2, p_2 is positive definite.

(b) p_2 is the sum of v(v + 2)ξ², a function of (v, ξ), and |η|², a function of (ω, η); so {p_2, |η|²} = 0 and

    H_(p_2) = 2v(v + 2)ξ∂_v − 2(v + 1)ξ²∂_ξ + H_(|η|²).

Near ∂ℛ_±, ± = sgn ξ, so ±ρ_∞ξ = 1 and ∂_ξρ_∞ = ∓ξ⁻². Hence 𝖧v = 2v(v + 2), 𝖧ρ_∞ = ±ρ_∞ · (−2(v + 1)ξ²)(∓ξ⁻²) =
2(v + 1)ρ_∞, 𝖧|η|² = 0, and 𝖧|η̂|² = 𝖧(ρ_∞²|η|²) = 2ρ_∞(𝖧ρ_∞)|η|² = 4(v + 1)|η̂|². This gives the formula for 𝖧q̃,
and on {|v| ≤ ½}, 4(v + 2) ≥ 6 and 4(1 + v) ≥ 2. In the coordinates (ρ_∞, v, ω, η̂) the ρ_∞-, v- and η̂-components of 𝖧
are 2(v + 1)ρ_∞, 2v(v + 2) and 2(v + 1)η̂ plus a term quadratic in η̂ (from the rescaled H_(|η|²)), and its
ω-component is linear in η̂; all vanish at ρ_∞ = 0, v = 0, η̂ = 0, that is on ∂ℛ_±.

(c) On Σ_0 over (−2, 0), ξ ≠ 0 (else η = 0 too), and 𝖧v = ±ρ_∞ · 2v(v + 2)ξ = 2v(v + 2). Backward, v increases and is
bounded by 0; if its limit were v_1 < 0, then 𝖧v ≤ −c < 0 near v_1 would contradict the boundedness of the backward
time. So v → 0, and then |η̂|² = −v(v + 2) → 0 on Σ_0, so the curve tends to {v = 0, η̂ = 0} = ∂ℛ_+ ∪ ∂ℛ_−. Forward,
𝖧v ≤ −c(v_0) < 0 on {v ≤ v_0}, v_0 < 0, so v reaches every value in (−2, v_0). ∎

**Lemma {#lem:iii-g-2-2}** (Radial estimate at the light cone.) Let 𝒟 ⊂ ℂ be compact, δ > 0, h as in
[[lem:iii-g-1-4]], and M a first-order differential operator on a neighbourhood of {v = 0}, with smooth coefficients,
whose principal symbol vanishes on ℛ_±, acting on ℂ¹⁵ ⊗ ℂ^m (the case M = 0, m = 1 being N_sf(λ) itself). Put
N_M := N_sf(λ) ⊗ Id + M. Let U be a neighbourhood of ∂ℛ_±.

(1) (*Below threshold.*) Let s < 2 − δ − sup_𝒟 Re λ. There are B, G, E ∈ Ψ⁰, microsupported in U, with kernels
supported near {v = 0}, B elliptic at ∂ℛ_± and WF′(E) ∩ ∂ℛ_± = ∅, such that for λ ∈ 𝒟 and all N_1, in the strong
sense,

    ‖Bu‖_(H^s) ≤ C(‖GN_Mu‖_(H^(s−1)) + ‖Eu‖_(H^s) + ‖u‖_(H^(−N_1))).                                     {#eq:iii-g-2-1}

(2) (*Above threshold, the adjoint.*) Let s′ > s_0 > δ − 1 + sup_𝒟 Re λ. There are B, G as in (1) such that for
λ ∈ 𝒟, in the strong sense,

    ‖Bw‖_(H^(s′)) ≤ C(‖GN_M^(*h)w‖_(H^(s′−1)) + ‖Gw‖_(H^(s_0)) + ‖w‖_(H^(−N_1))),                         {#eq:iii-g-2-2}

the adjoint taken for L²(μ_sf) and h (or for any other fibre inner product, as [[prop:i-a-4-2]] notes).

*Proof.* The proof of [[prop:i-a-4-2]] uses of the operator and of the hypotheses of [[ch:s01]] only: that the operator
is a differential operator with principal symbol G_0 Id, G_0 real; that ∂ℛ is a source, with 𝖧ρ_∞ = β_0ρ_∞ and
β_0 > 0; a quadratic defining function q̃ of ∂ℛ with 𝖧q̃ ≥ c′q̃ (the conclusion of [[lem:i-a-4-1]]); and the bound
[[eq:i-a-4-1]], β_0⁻¹p_1 ≤ ϑ Id on ∂ℛ, where p_1 := ±ρ_∞σ_1(Im_h(·)). Its kernels are compactly supported, so the decay
order is immaterial. Here G_0 = p_2 ([[lem:iii-g-1-2]] (a); M is of first order), and [[lem:iii-g-2-1]] (b) shows that
∂ℛ_± is a source, with β_0 = 2(1 + v) and q̃. It remains to compute p_1 on ∂ℛ_±.

*The subprincipal symbol at the light cone.* The first-order terms of N_M are −2(λ − 3/2 − S̄)∂_v; the terms
a v∂_v, −2λ v∂_v and V of [[eq:iii-g-1-2]]–[[eq:iii-g-1-3]]; M; and the first-order part of Im_h of the second-order
part D := −2∂_v v∂_v − (v∂_v)² + Δ_(𝕊³). The symbols of v∂_v, of V and of M vanish on ℛ_± (where v = 0, resp. η = 0).
For D: the density μ_sf = m|dv dg̸|, m := (2 + v)⁻¹, and h do not depend on v except through m. For an operator
Q = q_2(v)∂_v² + q_1(v)∂_v with real coefficients, its formal adjoint for m|dv| is m⁻¹Q^t m, Q^t the transpose for
|dv|, with second-order coefficient q_2 and first-order coefficient 2q_2′ + 2q_2m′/m − q_1. The (v, ∂_v)-part of D is
Q = −v(v + 2)∂_v² − (v + 2)∂_v, with 2q_2′ + 2q_2m′/m − q_1 = −4(v + 1) + 2v + (v + 2) = −(v + 2) = q_1; so the first-
order coefficient of D − D^(*h) in ∂_v vanishes identically. And Δ_(𝕊³) − Δ_(𝕊³)^(*h) = H⁻¹[H, Δ_(𝕊³)], h = ⟨H·, ·⟩,
has symbol linear in η, which vanishes on ℛ_±. Finally, with A := λ − 3/2 − S̄, the principal symbols of −2A∂_v and of
its h-adjoint are −2iξA and 2iξA^(*h), so σ_1(Im_h(−2A∂_v)) = (2i)⁻¹(−2iξA − 2iξA^(*h)) = −ξ(A + A^(*h)). So on ℛ_±

    σ_1(Im_h N_M) = ξ(3 + 2Re_h S̄ − 2Re λ),   p_1 = 3 + 2Re_h S̄ − 2Re λ,   β_0⁻¹p_1 = 3/2 + Re_h S̄ − Re λ,
                                                                                                      {#eq:iii-g-2-3}

as ±ρ_∞ξ = 1 and β_0 = 2 at v = 0.

*(2).* For N_M^(*h), Re_h is the same and Im_h changes sign, so by [[lem:iii-g-1-4]]
β_0⁻¹p_1(N_M^(*h)) = −(3/2 + Re_h S̄ − Re λ) ≤ (Re λ − 3/2 + δ) Id: this is the bound [[eq:i-a-4-1]] with
ϑ := sup_𝒟 Re λ − 3/2 + δ. (No Im σ term enters: the proof uses [[eq:i-a-4-1]] only through the lower bound
2β_0(s_0 − ½ − ϑ) of the commutator.) [[prop:i-a-4-2]] (1) for N_M^(*h) gives [[eq:iii-g-2-2]] for s′ > s_0 > ½ + ϑ,
which is the stated condition.

*(1).* N_M = (N_M^(*h))^(*h), and [[prop:i-a-4-2]] (2), with N_M^(*h) in place of P̂(σ) and the ϑ just found, gives
[[eq:iii-g-2-1]] at every order 1 − s″ with s″ > ½ + ϑ, that is at every s < ½ − ϑ = 2 − δ − sup_𝒟 Re λ, with the
control operator E microsupported in supp ψ′(ς_R q̃), away from ∂ℛ_±. The iteration runs from −N_1 with no threshold,
which is the strong sense. The constants are uniform for λ ∈ 𝒟, the symbols being polynomial in λ. ∎

In (1) the threshold is s < 2 + min spec S̄ − Re λ, up to δ. [Hin26] derives it from the characteristic exponents 0
and 3/2 + α − λ, α ∈ spec S̄, of vN_sf(λ) at v = 0, whose indicial operator there is −2(v∂_v)(v∂_v + λ − 3/2 − S̄),
and from v_+^w ∈ H^(Re w + 1/2 − ε)_loc for every ε > 0; the two derivations give the same number.

#### The artificial boundary and the hyperbolic region {#sec:iii-g-2-2}

**Lemma {#lem:iii-g-2-3}** (Slab estimates.) On the slabs Ω_(a,b) := {a < −v < b} × 𝕊³ with 0 < a < b < 2, the
statements of [[prop:i-a-6-3]], [[prop:i-a-6-4]] and [[cor:i-a-6-5]] hold for L = N_sf(λ) and for L = N_sf(λ)^(*h),
uniformly for λ in compact sets, with r := −v (so that the spaces H^s(Ω_(a,b))^(•,−), supported at r = b, are supported
at v = −b). In particular, with the cut-offs of [[cor:i-a-6-5]] placed at r = ½ and r = ¼ (that is, at v = −½ and
v = −¼),

    ‖u|_({−1<v<−1/4})‖_(H^s) ≤ C‖N_sf(λ)u|_({−1<v<−1/4})‖_(H^(s−1)),     u ∈ Ḣ^s near {v = −1},           {#eq:iii-g-2-4}

    ‖χw‖_(H̄^(1−s)) ≤ C(‖N_sf(λ)^(*h)w‖_(H̄^(−s)({−1<v<−1/4})) + ‖χ_1w‖_(H^(1−s))),     w ∈ H̄^(1−s) near {v = −1},
                                                                                                      {#eq:iii-g-2-5}

with χ = 1 on {v ≤ −½}, χ = 0 near {v ≥ −¼}, and χ_1 supported in {−½ < v < −¼} and equal to 1 near supp dχ.

*Proof.* The proofs of [[prop:i-a-6-3]] and [[prop:i-a-6-4]] use of L only: order 2, principal symbol G_0 Id with G_0
the dual of a Lorentzian metric 𝔤 on the slab for which dr is timelike; bounds for the coefficients and for
inf(−G_0(dr)); that L* is of the same form; and that the null bicharacteristics of G_0 move strictly monotonically in r
([[sec:i-a-6-2]] and (H4) of [[sec:i-a-1]]), used with [[prop:i-a-5-1]] and [[prop:i-a-5-2]]. For N_sf(λ) on
{−2 < v < 0}: G_0 = p_2 is the dual of a Lorentzian metric with dv timelike, and
−p_2(dv) = −v(v + 2) ≥ min(a(2 − a), b(2 − b)) > 0 on the closure of Ω_(a,b) ([[lem:iii-g-1-2]] (a)); its adjoint has
the same principal symbol; and v is strictly monotone along the bicharacteristics there ([[lem:iii-g-2-1]] (c); at
finite frequencies likewise, as H_(p_2)v = 2v(v + 2)ξ ≠ 0 on {p_2 = 0} ∖ o). Time-orient 𝔤 so that v increases to
the future; then r = −v decreases to the future, as in [[ch:s01]]. [[eq:iii-g-2-4]] is [[eq:i-a-6-2]] with the roles of
L and L* exchanged ([[prop:i-a-6-4]] (i) for the forward problem, with the support at r = 1), and [[eq:iii-g-2-5]] is
[[eq:i-a-6-1]] ([[prop:i-a-6-4]] (ii) applied to χw, the commutator [L, χ] being supported in supp dχ). ∎

#### The Fredholm property {#sec:iii-g-2-3}

Fix λ ∈ ℂ, and call (s, μ) *admissible for* λ if

    s < 2 − Re λ,     μ ∈ (Re λ − 1, Re λ).                                                              {#eq:iii-g-2-6}

Then μ is not the real part of a root of J_λ ([[eq:iii-g-1-5]]): Re(λ − r) = μ would give Re r ∈ (0, 1), which
[[prop:iii-f1-2-3]] (a) excludes. Put

    𝒳 := {u ∈ Ḣ^(s,μ)_b : N_sf(λ)u ∈ Ḣ^(s−1,μ)_b},     𝒴 := Ḣ^(s−1,μ)_b,
    𝒳* := {w ∈ H̄^(1−s,−μ)_b : N_sf(λ)^(*h)w ∈ H̄^(−s,−μ)_b},                                           {#eq:iii-g-2-7}

Hilbert spaces with the graph norms; 𝒴* = H̄^(1−s,−μ)_b. By [[lem:iii-g-1-2]] (f), 𝒳 is the same space for every λ′
near λ, with equivalent norms.

**Proposition {#prop:iii-g-2-4}** (The Fredholm property; [Hin26, Proposition 9.2 (1)] in dimension 4 + 1.) Let (s, μ)
be admissible for λ, and μ_0 < μ.

(1) For every N_1 there is C such that for u ∈ 𝒳 and w ∈ 𝒳*

    ‖u‖_(Ḣ^(s,μ)_b) ≤ C(‖N_sf(λ)u‖_(Ḣ^(s−1,μ)_b) + ‖u‖_(Ḣ^(−N_1,μ_0)_b)),                                 {#eq:iii-g-2-8}

    ‖w‖_(H̄^(1−s,−μ)_b) ≤ C(‖N_sf(λ)^(*h)w‖_(H̄^(−s,−μ)_b) + ‖w‖_(H̄^(−N_1,−μ−1)_b)),                     {#eq:iii-g-2-9}

uniformly for λ in a compact set on which (s, μ) stays admissible. [[eq:iii-g-2-8]] holds in the strong sense: if
u ∈ Ḣ^(−N_1,μ)_b has N_sf(λ)u ∈ Ḣ^(s−1,μ)_b, then u ∈ Ḣ^(s,μ)_b.

(2) N_sf(λ): 𝒳 → 𝒴 is Fredholm, and the annihilator of its range in 𝒴* is ker_(𝒳*) N_sf(λ)^(*h).

(3) Its kernel and the annihilator of its range do not depend on the admissible pair (s, μ); nor, therefore, does its
index. Kernel elements lie in Ḣ^(s′,μ′)_b for every admissible (s′, μ′), are smooth on {v ≠ 0} and, near R = 0, lie in
𝒜^c for every c < Re λ. Elements of the annihilator are smooth on (−1, ∞) × 𝕊³ up to {v = −1}, and lie in 𝒜^c near
R = 0 for every c < 1 − Re λ.

*Proof.* (1) *Near v = −1.* [[eq:iii-g-2-4]] bounds u on {−1 < v < −¼} in H^s by N_sf(λ)u there, with no error term.

*The hyperbolic region and the light cone.* Let B_*, E be the operators of [[lem:iii-g-2-2]] (1) at ∂ℛ_+ ∪ ∂ℛ_−, with
U so small that the closed set K_E ⊃ WF′(E) lies over {−⅛ < v < ⅛}. Every point of K_E is either elliptic for p_2
([[lem:iii-g-2-1]] (a), and p_2 ≠ 0 off Σ_0) or a point of Σ_0 over {v < 0}, whose forward 𝖧-curve reaches {v < −½}
by [[lem:iii-g-2-1]] (c) (v decreases along it). Along these curves, which have bounded length outside the neighbourhood
U_* of ∂ℛ_±, [[prop:i-a-5-2]] applies at fibre infinity (the subprincipal part there is unrestricted and the order is
constant), with control from {v < −½}, where [[eq:iii-g-2-4]] applies. Finitely many such estimates, [[prop:i-a-5-1]]
off Σ_0, and compactness give ‖Eu‖_(H^s) ≤ C(‖N_sf(λ)u‖_(H^(s−1)) + ‖φu‖_(H^(−N_1))), φ a cut-off to {v < 5}. With
[[eq:iii-g-2-1]], [[prop:i-a-5-1]] on the rest of fibre infinity over {−1 ≤ v ≤ 5} (elliptic by [[lem:iii-g-2-1]] (a)
and (c), with the curves of [[lem:iii-g-2-1]] (c) for Σ_0 over {−1 < v < 0}), and the fact that at finite frequencies
over a compact set every operator of order −∞ is bounded by ‖u‖_(H^(−N_1)) there,

    ‖(1 − χ_∂)u‖_(H^s) ≤ C(‖N_sf(λ)u‖_(H^(s−1)({v<5})) + ‖φu‖_(H^(−N_1))).                              {#eq:iii-g-2-10}

*Near R = 0.* N_sf(λ) is of the form of [[sec:i-c-2-5]] at the end at 0, b-elliptic ([[lem:iii-g-1-2]] (b)).
[[lem:i-c-2-5]] at the b-weight μ gives ‖χ_∂u‖_(H^s_(b,μ)) ≤ C(‖χ̃_∂N_sf(λ)u‖_(H^(s−2)_(b,μ)) +
‖χ̃_∂u‖_(H^(−N_1)_(b,μ))), and [[lem:i-c-2-6]] at c = μ (not the real part of a root of J_λ) with [[lem:i-c-2-2]] (g),
exactly as in the proof of [[thm:i-c-3-1]] (1) near ∂X, bounds the last term by
C‖N_sf(λ)u‖_(H^(−N_1−2)_(b,μ)) + C‖u‖_(Ḣ^(−N_1,μ_0)_b) plus a term that is absorbed. With [[eq:iii-g-2-10]] this is
[[eq:iii-g-2-8]]; the overlap {2 < v < 5} is in the interior, where the norms agree.

*The adjoint.* For w ∈ 𝒳*: [[eq:iii-g-2-5]] near v = −1, its last term controlled by the estimates that follow on
{−½ < v < −¼}. [[lem:iii-g-2-2]] (2) at ∂ℛ_± at the order 1 − s, with s_0 ∈ (Re λ − 1 + δ, 1 − s) (δ small;
1 − s > Re λ − 1 is [[eq:iii-g-2-6]]); then [[prop:i-a-5-2]] along the 𝖧-curves of [[lem:iii-g-2-1]] (c) forwards,
from a neighbourhood of ∂ℛ_± to {v < −½} (the adjoint chain of [[sec:i-a-7-1]], the curves starting in the region
controlled by the radial estimate); and [[prop:i-a-5-1]] elsewhere. The term ‖Gw‖_(H^(s_0)) is bounded by
δ′‖w‖_(H^(1−s)) + C_(δ′)‖w‖_(H^(−N_1)) on a compact set (Ehrling, as s_0 < 1 − s). Near R = 0, N_sf(λ)^(*h) is
b-elliptic with Mellin symbol H_0⁻¹J_λ(−ζ̄)^†H_0 up to lower-order terms on 𝕊³, whose roots are
{−ζ̄ : ζ a root of J_λ}, for the b-density μ_sf (as (R∂_R)^† = −R∂_R; this is [[eq:i-c-3-5]] without the shift by 2,
which there comes from the density |dx|); −μ is not the real part of one. [[lem:i-c-2-5]], [[lem:i-c-2-6]] and
[[lem:i-c-2-2]] (g) give [[eq:iii-g-2-9]] as there.

(2) The inclusions Ḣ^(s,μ)_b ↪ Ḣ^(−N_1,μ_0)_b and H̄^(1−s,−μ)_b ↪ H̄^(−N_1,−μ−1)_b are compact for
−N_1 < min(s, 1 − s) ([[lem:i-c-2-2]] (e) at R = 0, Rellich on the compact remainder), so [[eq:iii-g-2-8]] and
[[eq:iii-g-2-9]] give finite-dimensional kernels and closed ranges. *Green's formula*
⟨N_sf(λ)u, w⟩ = ⟨u, N_sf(λ)^(*h)w⟩ for u ∈ 𝒳 and w ∈ 𝒳*: split with χ_∂ and a cut-off near v = −1; near v = −1 it
is [[lem:i-a-6-1]] (d) with the density of C_c^∞({v > −1}) in Ḣ^s ([[lem:i-a-6-1]] (a)); near R = 0 it is the argument
of the proof of [[thm:i-c-3-1]]; in between, Friedrichs mollifiers J_ε serve: [N_sf(λ), J_ε] is bounded H^s → H^(s−1)
uniformly and tends to 0 strongly, so J_εu → u in 𝒳 locally. The cokernel is then the kernel of N_sf(λ)^(*h) on 𝒳*,
as in the proof of [[thm:i-c-3-1]].

(3) *Kernel.* Let u ∈ 𝒳 with N_sf(λ)u = 0. The estimates of (1) hold in the strong sense at every order
s′ < 2 − Re λ: [[eq:iii-g-2-1]] needs no a priori regularity beyond H^(−N_1), and the propagation estimates, the
elliptic estimates and [[eq:iii-g-2-4]] hold at every order. So u ∈ H^(s′) on {v < 5} for all such s′, and u ∈ H^∞ on
compact subsets of {v ≠ 0} (there the radial estimate is not needed: ellipticity on {v > 0}, propagation from
[[eq:iii-g-2-4]] on {v < 0}). Near R = 0, [[lem:i-c-2-5]] at every order and [[lem:i-c-2-7]], with
(c_−, c_+) := (Re λ − 1, Re λ) containing no real part of a root of J_λ and c = μ, give χ_∂u ∈ H^∞_(b,c′) for every
c′ < Re λ, so u ∈ 𝒜^(c′) there ([[lem:i-c-2-2]] (f)). So u lies in the kernel for every admissible pair.
*Annihilator.* Let w ∈ 𝒳* with N_sf(λ)^(*h)w = 0. [[lem:iii-g-2-2]] (2) in the strong sense at every order s′ ≥ 1 − s
(with the a priori order 1 − s above threshold), propagation and ellipticity give w ∈ H^∞ on (−1, ∞) × 𝕊³ away from
R = 0, and [[eq:iii-g-2-5]] at every order gives smoothness up to v = −1. Near R = 0, [[lem:i-c-2-7]] for
N_sf(λ)^(*h), whose root-free strip containing −μ is (−Re λ, 1 − Re λ), gives w ∈ H^∞_(b,c′) for every
c′ < 1 − Re λ, which contains the b-weight −μ′ of every admissible μ′. So w is an annihilator for every admissible pair.
∎

#### b-regularity at the light cone {#sec:iii-g-2-4}

Let 𝒟^m be the operators Σ_(j+|α|≤m) c_(jα)(v, ω)(v∂_v)^j ℒ_Ω^α on (−½, 2) × 𝕊³, c_(jα) smooth matrix functions.
Since v∂_v commutes with each ℒ_Ω, [ℒ_(Ω_a), ℒ_(Ω_b)] is a combination of the ℒ_(Ω_c), and derivatives of the
coefficients are smooth, [𝒟^p, 𝒟^q] ⊂ 𝒟^(p+q−1) and 𝒟^p𝒟^q ⊂ 𝒟^(p+q). A *word* W^α is a product of |α| factors from
𝒢 := {v∂_v, ℒ_(Ω_1), …, ℒ_(Ω_6)}; every element of 𝒟^m is a combination of words of length at most m with smooth
coefficients on the left. For u supported in (−½, 2) × 𝕊³, u ∈ Ḣ^((s;k),μ)_(b;b) if and only if W^αu ∈ H^s for
|α| ≤ k; and then Du ∈ H^s for D ∈ 𝒟^k and Du ∈ H^(s−1) for D ∈ 𝒟^(k+1) (one factor being a first-order differential
operator).

**Lemma {#lem:iii-g-2-5}** (Commuting with the dilation and the rotations.) N_sf(λ)ℒ_Ω = ℒ_ΩN_sf(λ), and

    N_sf(λ)(v∂_v) = (v∂_v + 1)N_sf(λ) − M_1(v∂_v) − Σ_a M_aℒ_(Ω_a) − M_0,                                {#eq:iii-g-2-11}

with M_1, M_a, M_0 ∈ 𝒟¹ (on all of {v > −2}, with coefficients independent of v), the principal symbols of M_1 and
M_a (as first-order differential operators) vanishing on N*{v = 0}.

*Proof.* The first identity is [[lem:iii-g-1-2]] (d). By [[lem:iii-g-1-2]] (e),
N_sf(λ)(v∂_vu) = (v∂_v + 1)N_sf(λ)u − L̃(0)(ω, v∂_v + λ, ∂_ω)u. The six rotation fields Z_(ij) = x_i∂_(x_j) − x_j∂_(x_i)
of 𝕊³ ⊂ ℝ⁴ satisfy Δ_(𝕊³) = −Σ_a Ω_a² on functions. Write Ω_a = ℒ_(Ω_a) − A_a with constant matrices A_a (the Lie
derivative of the frame dt_*, dx¹, …, dx⁴ along a rotation is constant), and V = Σ_a V_aΩ_a + V_0 with V_a, V_0 smooth.
From −Ω_a² = −Ω_aℒ_(Ω_a) + Ω_aA_a and Ω_aA_a = A_aℒ_(Ω_a) − A_a², [[eq:iii-g-1-2]] gives

    L̃(0)(ω, v∂_v + λ, ∂_ω)u = M_1(v∂_vu) + Σ_a M_a(ℒ_(Ω_a)u) + M_0u,

with M_1 := −v∂_v − 2λ + a, M_a := −Ω_a + A_a + V_a and M_0 := aλ − λ² + b + V_0 − Σ_a(V_a + A_a)A_a. The principal
symbol of M_1 is −ivξ and that of M_a is −iη(Ω_a); both vanish on {v = 0, η = 0}. ∎

**Proposition {#prop:iii-g-2-6}** (Commuted equations.) For every word W^α, |α| = j ≥ 1, on (−½, 2) × 𝕊³,

    N_sf(λ)W^α = W̃^αN_sf(λ) − Σ_(|β|=j) M_(αβ)W^β − Σ_(|β|<j) M′_(αβ)W^β,                               {#eq:iii-g-2-12}

with W̃^α ∈ 𝒟^j, M_(αβ) ∈ 𝒟¹ with principal symbols vanishing on N*{v = 0}, and M′_(αβ) ∈ 𝒟^(j−|β|) a combination of
products D_1D_2 with D_1 ∈ 𝒟¹ and D_2 ∈ 𝒟^(j−1−|β|).

*Proof.* Induction on j. For j = 1 it is [[lem:iii-g-2-5]] (W̃ = v∂_v + 1 or ℒ_Ω; M′_(·,∅) = M_0, of the form D_1 with
D_2 = Id). Suppose [[eq:iii-g-2-12]] holds for α, and let W ∈ 𝒢. Then
N_sf(λ)WW^α = (W̃N_sf(λ) − Σ_(W′) M_(WW′)W′ − M_W)W^α, and
W̃N_sf(λ)W^α = W̃W̃^αN_sf(λ) − Σ_β W̃M_(αβ)W^β − Σ_β W̃M′_(αβ)W^β. Write
W̃M_(αβ)W^β = M_(αβ)W̃W^β + [W̃, M_(αβ)]W^β. The first is M_(αβ) (with vanishing symbol) times WW^β (of length j + 1),
plus terms M_(αβ)cW^β of length j (as W̃ − W is a constant c), which are of the second kind with D_1 = cM_(αβ) and
D_2 = Id ∈ 𝒟^((j+1)−1−j); the commutator lies in 𝒟¹ and multiplies W^β, |β| = j, a term of the same kind. For |β| < j
and M′_(αβ) = D_1D_2, W̃D_1D_2W^β = D_1(W̃D_2)W^β + [W̃, D_1]D_2W^β, with W̃D_2 ∈ 𝒟^(j−|β|) = 𝒟^((j+1)−1−|β|) and
[W̃, D_1] ∈ 𝒟¹: of the second kind for the length j + 1. M_(WW′)W′W^α is of the first kind (W′W^α of length j + 1), and
M_WW^α is of the second kind (D_1 = M_W, D_2 = Id, |β| = j). ∎

**Proposition {#prop:iii-g-2-7}** (b-regularity at the light cone; [Hin26, Proposition 9.2 (3)] in dimension 4 + 1.)
Let (s, μ) be admissible for λ, k ∈ ℕ_0, and u ∈ Ḣ^(s,μ)_b with N_sf(λ)u ∈ Ḣ^((s−1;k),μ)_(b;b). Then
u ∈ Ḣ^((s;k),μ)_(b;b).

*Proof.* Put f := N_sf(λ)u. *Away from v = 0.* On {v < −¼}, f ∈ H^(s−1+k), and [[eq:iii-g-2-4]] and propagation at
order s + k give u ∈ H^(s+k) there ([[prop:iii-g-2-4]] (1) in the strong sense, which on {v < 0} uses no radial
estimate). On compact subsets of {v > 0}, ellipticity gives u ∈ H^(s+1+k)_loc; near R = 0, [[lem:i-c-2-5]] gives
χ_∂u ∈ H^(s+k)_(b,μ). Each of these is the module regularity there ([[sec:iii-g-1-2]]).

*Near v = 0.* Let χ ∈ C_c^∞((−½, 2)) equal 1 on [−¼, 1], and u_0 := χu. Then N_sf(λ)u_0 = χf + [N_sf(λ), χ]u, and
[N_sf(λ), χ]u is supported where u ∈ H^(s+k); so N_sf(λ)u_0 ∈ Ḣ^((s−1;k)), with support in (−½, 2) × 𝕊³. We show by
induction on j ≤ k that W^αu_0 ∈ H^s for |α| ≤ j. For j = 0 it is the hypothesis. Let it hold for j − 1, and let
U := (W^αu_0)_(|α|=j), a priori in H^(s−1) (one factor of each word is a first-order operator applied to
W^(α′)u_0 ∈ H^s). By [[eq:iii-g-2-12]],

    (N_sf(λ) ⊗ Id + M)U = F,     M := (M_(αβ))_(|α|=|β|=j),
    F := (W̃^αN_sf(λ)u_0 − Σ_(|β|<j) M′_(αβ)W^βu_0)_α,

and F ∈ H^(s−1): W̃^αN_sf(λ)u_0 ∈ H^(s−1), as W̃^α ∈ 𝒟^j, j ≤ k, and N_sf(λ)u_0 ∈ Ḣ^((s−1;k)); and in each term
D_1D_2W^βu_0 of M′_(αβ)W^βu_0, D_2W^β ∈ 𝒟^(j−1), so D_2W^βu_0 ∈ H^s by the induction hypothesis (the remark before
[[lem:iii-g-2-5]], with k = j − 1), and D_1 ∈ 𝒟¹ maps H^s to H^(s−1). The operator N_sf(λ) ⊗ Id + M satisfies
[[lem:iii-g-2-2]] (1) at ∂ℛ_±, with the threshold of N_sf(λ) (the symbol of M vanishes there); along Σ_0 over
{−½ < v < 0}, [[prop:i-a-5-2]] applies to it (principal symbol p_2 Id; M enters the subprincipal part, on which no sign
is imposed), with control from {v < −¼}, where U ∈ H^s by the first step; and it is elliptic elsewhere over supp u_0.
The estimates in the strong sense, as in [[prop:iii-g-2-4]] (1), give U ∈ H^s. ∎

### Injectivity for Re λ < 2 {#sec:iii-g-3}

This section is the first half of [Hin26, Proposition 9.2 (2)] in dimension 4 + 1.

**Lemma {#lem:iii-g-3-1}** (Conormality at the light cone.) Let s ∈ ℝ with s − ½ ∉ ℤ, and let u ∈ H^s(ℝ × 𝕊³) be
supported in {v ≥ 0} near {v = 0}, with W^αu ∈ H^s near {v = 0} for every word W^α. Then for every α there is C with
|W^αu(v, ω)| ≤ C v^(s−½) on (0, 1) × 𝕊³.

*Proof.* Localise with a cut-off in v, which commutes with the rotations, and with v∂_v up to a smooth compactly
supported function. With the Fourier transform in v and the expansion in spherical harmonics (eigenvalues κ_k of
Δ_(𝕊³)), ‖u‖²_(H^s) = ∫ Σ_k (1 + ξ² + κ_k)^s |û_k(ξ)|² dξ ≥ ‖u‖²_(H^s(ℝ;L²(𝕊³))) for s ≥ 0, and the same applied to
Ω^γu, |γ| ≤ m, gives u ∈ H^s(ℝ; H^m(𝕊³)) for every m; likewise for each W^αu. Let ℋ := H^m(𝕊³) with m ≥ 2, so that
ℋ ⊂ C⁰(𝕊³). Write s = k_0 + ½ + a_1 with k_0 ∈ ℕ_0 and a_1 ∈ (0, 1). For g ∈ H^s(ℝ; ℋ), g^(k_0) ∈ H^(½+a_1)(ℝ; ℋ)
and ‖g^(k_0)(x) − g^(k_0)(y)‖_ℋ ≤ C|x − y|^(a_1)‖g‖_(H^s): by Fourier inversion and Cauchy–Schwarz this difference is
at most (2π)⁻¹‖⟨τ⟩^(½+a_1)(g^(k_0))^∧‖_(L²) times (∫ min(4, |x − y|²τ²)⟨τ⟩^(−1−2a_1) dτ)^(1/2), and the integral is at
most C|x − y|^(2a_1) (split at |τ| = |x − y|⁻¹; 0 < a_1 < 1); and g^(i), i ≤ k_0, are continuous. If g is supported in
{v ≥ 0}, then g^(i)(0) = 0 for i ≤ k_0, and Taylor's formula gives ‖g(v)‖_ℋ ≤ Cv^(k_0+a_1) = Cv^(s−½) for v ∈ (0, 1).
Applied to g = W^αu this proves the case s > ½. For s < 0 the first step uses (1 + ξ²)^s ≤ (1 + ξ² + κ_k)^s(1 + κ_k)^(−s)
instead, at the cost of ⌈−s⌉ more rotations.

*The case s < ½.* Let j ∈ ℕ with s + j > ½, and let I be the primitive in v vanishing on {v < 0}, cut off beyond the
support. It maps H^σ(ℝ; ℋ) to H^(σ+1)(ℝ; ℋ) for compactly supported elements, satisfies v∂_vI = I(v∂_v + 1), and
commutes with the rotations. So U := I^ju satisfies the hypotheses at order s + j, and the case s > ½ gives
|W^αU| ≤ Cv^(s+j−½). On (0, 1), u = ∂_v^jU = v^(−j) ∏_(i=0)^(j−1)(v∂_v − i)U, and W^αv^(−j) = v^(−j)W^α_((−j)), where
W^α_((−j)) is W^α with every v∂_v replaced by v∂_v − j; so |W^αu| ≤ Cv^(s−½). The number of words this uses is counted
in [[lem:iii-g1-2-1]]. ∎

**Proposition {#prop:iii-g-3-2}** (Injectivity.) Let Re λ < 2 and (s, μ) be admissible for λ. Then N_sf(λ): 𝒳 → 𝒴 is
injective.

*Proof.* Let u ∈ 𝒳 with N_sf(λ)u = 0. By [[prop:iii-g-2-4]] (3) we may change (s, μ): take
s ∈ (max(−½, ½ − Re λ), 2 − Re λ), which is possible as Re λ < 2, with s − ½ ∉ ℤ, and μ ∈ (Re λ − 1, Re λ). Put
a_0 := s − ½ > −1, so that a_0 + Re λ > 0.

*Step 1: support and regularity.* By [[prop:iii-g-2-7]], u ∈ Ḣ^((s;∞),μ)_(b;b). On {−1 < v < 0}, u solves
N_sf(λ)u = 0, is supported in {v ≥ −1}, and v is a time function there; by the uniqueness step of [[prop:i-a-6-4]] on
the slabs {−1 − ε′ < v < −ε} ([[lem:iii-g-2-3]]), u = 0 on {v < −ε} for every ε > 0. So u is supported in {v ≥ 0}. It
is smooth on {v > 0} (by ellipticity), satisfies |W^αu| ≤ Cv^(a_0) on (0, 1) by [[lem:iii-g-3-1]], and
|W^αu| ≤ Cv^(−(Re λ−ε)) on {v ≥ ½} for every ε > 0 by [[prop:iii-g-2-4]] (3) (u ∈ 𝒜^(Re λ−ε) near R = 0, R = v⁻¹,
the b-fields being v∂_v = −R∂_R and the rotations).

*Step 2: the Fourier transform.* u is the extension by zero of u|_(v>0). Indeed, let φ be smooth with compact support
and χ ∈ C_c^∞(ℝ) equal to 1 near 0. Then ⟨u, φχ(·/ε)⟩ → 0 as ε → 0, since ‖φχ(·/ε)‖_(H^(−s)) = O(ε^(min(½,½+s))) and
s > −½; and ⟨u, φ(1 − χ(·/ε))⟩ → ∫_(v>0) uφ by dominated convergence (|u| ≤ Cv^(a_0), a_0 > −1). So [[lem:ii-f-5-7]]
applies to f := u|_(v>0), with a := a_0 and b := Re λ − ε. The equation holds
across v = 0 by hypothesis, so the step of the proof of [[lem:ii-f-5-8]] that establishes it there is not needed. So
û(r̂, ω) := ∫ e^(ir̂v)u dv is smooth on {r̂ ≠ 0}, with

    |(r̂∂_r̂)^j ∂_ω^α û| ≤ C(1 + |r̂|)^(−1−a_0) (|r̂|/(1 + |r̂|))^(min(Re λ−1−ε, 0)−ε).

By [[lem:iii-g-1-2]] (c), N_sf(λ) is the operator of [[eq:ii-f-5-11]] at iσ = λ, with c = 3/2, S_0 = S̄ and
P^(0)(0) = L̃(0). The transformed equation follows from ℱ(∂_vg) = −ir̂ℱg and ℱ(vg) = −i∂_r̂ℱg, which give
ℱ(v∂_vg) = −(r̂∂_r̂ + 1)ℱg: the equation N_sf(λ)u = 0 on ℝ × 𝕊³ becomes

    [2ir̂(−r̂∂_r̂ + λ − 5/2 − S̄) + L̃(0)(ω, −r̂∂_r̂ − 1 + λ, ∂_ω)]û = 0,

which is [[eq:ii-f-5-12]] at iσ = λ. For r̂ > 0 put w^♭_±(r̂, ω) := r̂^(1−λ)û(±r̂, ω). Conjugation by r̂^(1−λ) replaces
r̂∂_r̂ by r̂∂_r̂ + λ − 1, and r̂ ↦ −r̂ changes the sign of the first term only; so on {r̂ > 0}, with ρ̂ := r̂⁻¹
(r̂∂_r̂ = −ρ̂∂_ρ̂) and after multiplication by ρ̂²,

    [±2iρ̂(ρ̂∂_ρ̂ − 3/2 − S̄) + ρ̂²L̃(0)(ω, ρ̂∂_ρ̂, ∂_ω)]w^♭_± = N_tf(±1)w^♭_± = 0,

with N_tf of [[eq:i-c-4-1]] for these data, which is the operator N_tf(L̂_b, ±1) of [[sec:iii-f1-3]]; this is
[[eq:ii-f-5-13]].

*Step 3: the weights.* As |r̂^(1−λ)| = r̂^(1−Re λ) is conormal,

    w^♭_± ∈ 𝒜^(a_0+Re λ, −β)(tf),     β := max(2ε, Re λ − 1 + 2ε),                                       {#eq:iii-g-3-1}

in the notation of [[ch:s03]] (ρ_sctf first): at r̂ → ∞ the exponent is −1 − a_0 + 1 − Re λ, and at r̂ → 0 it is
1 − Re λ + min(Re λ − 1 − ε, 0) − ε ≥ −β. Take ε so small that β < 1, which is possible as Re λ < 2; then β ∈ (0, 1).

*Step 4: tf-admissibility.* By [[prop:iii-f1-3-3]], L̂_b is tf-admissible with every weight in (0, 1]. Fix
β* ∈ (β, 1] and q := 2 − β*, and in the spaces of [[sec:i-c-4-3]] take orders 𝗋_± admissible as there whose value
near R_out, the zero section over sctf, is below a_0 + Re λ − 2 (admissibility imposes only an upper bound there,
[[lem:i-a-7-1]]). Then w^♭_+ ∈ 𝒳_(tf,0) and w^♭_− ∈ 𝒳_(tf,π), exactly as in the proof of [[lem:ii-f-5-8]], with the
weight γ_I there replaced by a_0 + Re λ > 0: near sctf by [[lem:i-a-7-4]] (a), near ztf as
𝒜^(−β) ⊂ H^∞_(b,q−2) ([[lem:i-c-2-2]] (f)), and smooth in between. By [[cor:i-c-5-2]] (a), N_tf(e^(iθ)) is invertible
on these spaces at θ = 0 and θ = π, so w^♭_± = 0 and û = 0 on {r̂ ≠ 0}.

*Step 5.* As at the end of the proof of [[lem:ii-f-5-8]]: for ψ ∈ C^∞(𝕊³; ℂ¹⁵), ⟨û, ψ⟩ is supported in {0}, so ⟨u, ψ⟩
is a polynomial in v, vanishing for v < 0; so u = 0. ∎

In dimension 3 + 1, [Hin26, Proposition 9.2] obtains injectivity for Re λ < 1 + ε_ind; its bound comes from the
tf-weights, which there must lie in (0, ε_ind). At n = 4 the gap (0, 1] and the tf-admissibility on all of it leave as
the only constraint the tf-weight β < 1 of Step 3, that is Re λ < 2.

### High frequencies: the semiclassical estimate {#sec:iii-g-4}

This section is [Hin26, (9.9)] in dimension 4 + 1.

#### The family {#sec:iii-g-4-1}

Fix C_λ ≥ 1. For λ with |Re λ| ≤ C_λ and |Im λ| ≥ 1 put σ := −iλ, h := |Im λ|⁻¹ and z := hσ = ±1 + iy, with
y = −h Re λ and ± = sgn Im λ; so z ∈ 𝒵_h := {±1 + iy : |y| ≤ C_λh} and λ = iz/h. As in [Hin26], let
R̃ ∈ C^∞((0, ∞)) with R̃(R) = R for R < ½, R̃ ≥ ½ on [½, 1] and R̃ = 1 for R ≥ 1, and put

    N_h := R̃^(−λ)R̃^(−2)N_sf(λ)R̃^λ,   P := P_(h,z) := h²N_h.                                            {#eq:iii-g-4-1}

By [[lem:iii-g-1-2]] (c), on {R < ½}, P = h²N⁰(h⁻¹z) = P_(ι,h,z) of [[eq:ii-f-1-11]] for P_0 = 2L_b; on {R ≥ 1}
({v ≤ 1}), P = h²N_sf(λ). On {½ ≤ R ≤ 1} conjugation by R̃^λ = e^((iz/h) log R̃) is the semiclassical conjugation by
e^(iφ/h), φ := z log R̃: it translates the fibres by (Re z) d log R̃ and multiplies by R̃^(−Re λ), a smooth function
bounded above and below, with O(y/h) derivatives.

*The spaces.* On {R < ½} we use the spaces of [[sec:ii-f-3-1]], H^((𝗌′;·,γ_cf,γ_cf;𝖻)), for functions supported in
{R < ½} (the weight at 0f does not enter); on {v < 4}, the semiclassical Sobolev spaces H^(s,𝖻)_h of [[sec:i-b-2]]
(differential order s, constant, and semiclassical order 𝖻, a function on phase space), with supports at v = −1. With
a partition of unity in v these define ℋ_𝐨, 𝐨 := (s; γ_cf, γ_cf; 𝖻), and 𝒴_𝐨 := ℋ_((s−1;γ_cf−2,γ_cf;𝖻+1)); on
{¼ < R < 1} the spaces of [[ch:s08]] are the semiclassical ones of the interior (h𝒱(ι⁺), [[sec:ii-f-2-1]]), so the two
descriptions agree there, uniformly in h. The differential order of the spaces of [[ch:s08]] is chosen equal to s on
{R > ¼}, which is allowed, P being elliptic at fibre infinity over {R < ½} ([[sec:ii-f-3-1]]). The weight
γ_cf ∈ (−1, 0) is fixed, and α_+ := −γ_cf − 2, so that α_+ + 2 ∈ (0, 1) is a weight with which P_0 = 2L_b is
tf-admissible ([[prop:iii-f1-3-3]]).

For fixed h, ℋ_𝐨 is Ḣ^(s,γ_cf)_b with an equivalent norm ([[sec:ii-f-2-1]]), and u ↦ R̃^λu maps it onto
Ḣ^(s,γ_cf+Re λ)_b (|R̃^λ| = R^(Re λ) near R = 0, and R∂_R R̃^(i Im λ) is bounded); with
N_sf(λ) = R̃^(2+λ)N_hR̃^(−λ), the weight of the target matches: (γ_cf − 2) + 2 + Re λ.

#### Symbols and dynamics across the light cone {#sec:iii-g-4-2}

**Lemma {#lem:iii-g-4-1}** (Symbols and dynamics.) On {v < 4}:

(a) The principal symbol of P is p_z := (vξ + z)((v + 2)ξ + z) + |η|² on {R ≥ 1} ({v ≤ 1}), and on {½ ≤ R ≤ 1} the
transport of R̃⁻²p_z by the fibre translation of [[sec:iii-g-4-1]]. With z = ±1 + iy,

    Re p_z = p_(±1) − y²,     Im p_z = 2y((v + 1)ξ ± 1),

so h⁻¹Im P is a semiclassical operator of first order with coefficients bounded by C_λ: in [[eq:i-b-1-3]] the
coefficient ℓ of the term in 𝒬 may be taken to be 0 and every imaginary term is part of 𝒫_1 ([[rem:i-b-4-7]] (a), which
holds also at fibre infinity over this compact region, where ℓ𝒬 and 𝒫_1 have the same order).

(b) Let z_0 = 1 and p := p_1. With ξ̃ := −(v + 2)(vξ + 1),

    H_pξ̃ = 2(v + 1)(|η|² − p),     H_p|η|² = 0.

On Σ := {p = 0} (finite frequencies), ξ ≠ 0, and ξ̃ is non-decreasing along H_p over {v > −1}, strictly where η ≠ 0; on
Σ ∩ {η = 0}, ξ̃ ∈ {−2, 0}.

(c) Σ = Σ_+ ∪ Σ_−, ±ξ > 0. With w := v + 1, t := |ξ| and L := |η| (constant along the flow): Σ_+ lies over
{−1 − δ_1 ≤ v < 0} for small δ_1 > 0, with ξ ≥ −1/v there and H_pv ≤ −2 on {−1 < v < 0} (and H_pv < 0 on
[−1 − δ_1, −1]). Σ_− over {−1 − δ_1 ≤ v ≤ 0} has H_pv > 0 and

    t = [−w + (1 + L²(1 − w²))^(1/2)]/(1 − w²),

bounded by a constant depending on L (with the limit (1 + L²)/2 at v = 0). Over {v > 0}, Σ_− lies in
{1/(v + 2) ≤ t ≤ 1/v} ∩ {w² ≤ 1 + L⁻²}, so for L > 0 in {v ≤ v_max(L) := (1 + L⁻²)^(1/2) − 1}.

(d) Every maximal integral curve of H_p in Σ over {v < 4} is one of the following. (i) A curve in Σ_+, which tends to
∂ℛ_+ at fibre infinity backwards (with v ↑ 0 and t → ∞) and reaches {v < −1} forwards. (ii) A curve in Σ_− with
L > 0, which comes from {v < −1}, crosses {v = 0} at t = (1 + L²)/2, has one turning point of v, and tends to ∂ℛ_− at
fibre infinity forwards, with v ↓ 0 and t → ∞ (if v_max(L) ≥ 4, part of it lies in {R < ¼}, where the description of
[[ch:s08]] applies). (iii) The incoming ray {η = 0, ξ = −1/(v + 2)}, from {v < −1} to the cone point v → ∞ (in the
coordinates of [[ch:s08]] it tends to R_(cf,1,in)), and the outgoing ray {η = 0, ξ = −1/v} over {v > 0}, from the
cone point (R_(cf,out)) to ∂ℛ_−.

(e) In the coordinates of [[ch:s08]] over {R < ½} (R = v⁻¹ and, for z = 1, ξ_cħ = −v(vξ + 1), η_cħ = vη under the
conjugation), the symbol of P is [[eq:ii-f-1-13]], G_(ι,1) = v²p, and ξ̃ = (1 + 2R)ξ_cħ. With the field 𝖧 of
[[eq:ii-f-3-12]],

    𝖧ξ̃ = −2(1 + R)ξ_cħ(ξ̃ + 2) ≥ 0     on {G_(ι,1) = 0} over sf,

with equality only at ξ_cħ = 0 and at ξ̃ = −2. The future flow of [[ch:s08]] (its ς = +1) is the flow of H_p, up to a
positive factor.

(f) For z_0 = −1 everything holds after (ξ, η) ↦ (−ξ, −η), with the flow reversed, as
p_(−z)(v, ω; −ξ, −η) = p_z(v, ω; ξ, η) (the symmetry of [[sec:ii-f-3-2]]).

*Proof.* (a) The semiclassical principal symbol of h²N_sf(iz/h) is obtained from [[eq:iii-g-1-3]] with h∂_v ↦ iξ,
hλ = iz and h²Δ_(𝕊³) ↦ |η|², the terms carrying a further factor h dropping out:

    −2(iξ)(ivξ + iz) − (ivξ + iz)² + |η|² = 2ξ(vξ + z) + (vξ + z)² + |η|² = (vξ + z)((v + 2)ξ + z) + |η|².

The transport on {½ ≤ R ≤ 1} is that of the conjugation. With A := vξ ± 1 and B := (v + 2)ξ ± 1,
(A + iy)(B + iy) = AB − y² + iy(A + B), and A + B = 2((v + 1)ξ ± 1); here |y| ≤ C_λh.

(b) The function ξ̃ does not depend on (ω, η), so H_pξ̃ = ∂_ξp ∂_vξ̃ − ∂_vp ∂_ξξ̃, with

    ∂_ξp = 2(v(v + 2)ξ + v + 1),   ∂_vp = 2ξ((v + 1)ξ + 1),   ∂_vξ̃ = −(2(v + 1)ξ + 1),   ∂_ξξ̃ = −v(v + 2).

With w = v + 1 and v(v + 2) = w² − 1 this gives

    H_pξ̃ = −2((w² − 1)ξ + w)(2wξ + 1) + 2(w² − 1)ξ(wξ + 1) = −2w((w² − 1)ξ² + 2wξ + 1) = −2w(p − |η|²),

as p − |η|² = (vξ + 1)((v + 2)ξ + 1) = (w² − 1)ξ² + 2wξ + 1. H_p|η|² = {p, |η|²} = 0 as in [[lem:iii-g-2-1]] (b). If
ξ = 0 then p = 1 + |η|² > 0. On Σ, H_pξ̃ = 2(v + 1)|η|². With a := vξ + 1 and b := (v + 2)ξ + 1, p = ab + |η|², and
η = 0 forces a = 0 (ξ̃ = 0) or b = 0 (ξ = −1/(v + 2), a = 2/(v + 2), ξ̃ = −2).

(c) With k := wξ + 1 we have a = k − ξ, b = k + ξ, so p = k² − ξ² + |η|²; and H_pv = ∂_ξp = 2(v(v + 2)ξ + v + 1),
H_pξ = −∂_vp = −2ξk. On Σ_+ over {v ≥ −1}, k ≥ 1 and ξ² ≥ k² give ξ ≥ wξ + 1, so v < 0 and ξ ≥ −1/v, whence
v(v + 2)ξ ≤ −(v + 2) and H_pv ≤ −2; near v = −1 the same expression is negative by continuity. On Σ_− (ξ = −t) over
[−1, 0], H_pv = 2(w + (1 − w²)t) > 0 (at w = 0 it is 2t > 0), and near v = −1 likewise by continuity; in these
variables p = 0 is (1 − w²)t² + 2wt − (1 + L²) = 0, whose positive root is the stated t (at w = 1 the equation is
2t = 1 + L²). Over v > 0: t ≥ |1 − wt| gives 1/(v + 2) ≤ t ≤ 1/v, and real roots of the same quadratic need
1 + L²(1 − w²) ≥ 0.

(d) Along a curve, L is constant and, by (b), ξ̃ is monotone. (i) and the first half of (ii) follow from the signs of
H_pv in (c). On Σ_− over {v > 0} with L > 0, the curve stays in the compact set {0 < v ≤ v_max(L)} while t stays
bounded, and ξ̃ increases strictly. It cannot stay in a compact subset of {v > 0} at bounded t for all time (there
H_pξ̃ ≥ c > 0, and ξ̃ is bounded), so it leaves through v → 0. There the only points of Σ_− are at t ≤ 1/v → ∞ with
a = 1 − vt → 0 (the branch near t = 1/(v + 2) lies over v < 0 backwards, by the sign of H_pv there, and is the
incoming part); in the rescaled coordinates (ρ_∞, v, η̂) = (t⁻¹, v, η/t) → (0, 0, 0), that is to ∂ℛ_−. The turning
point is unique: at a critical point of v over {v > 0}, ξ = −w/(w² − 1), so (v + 1)ξ + 1 = −1/(w² − 1),
H_pξ = −2ξ((v + 1)ξ + 1) = −2w/(w² − 1)², and

    H_p²v = 2(2(v + 1)ξ + 1)H_pv + 2v(v + 2)H_pξ = 2(w² − 1)H_pξ = −4(v + 1)/(v(v + 2)) < 0;

so every critical point is a strict maximum, and there is at most one. (iii) On {η = 0}, Σ is the two curves named; on
the first H_pv = 2 and on the second H_pv = −2; [[sec:ii-f-1-3]] identifies their limits at R = 0.

(e) The correspondence is the conjugation of [[sec:iii-g-4-1]] on {R < ½}, where R̃ = R and φ = log R = −log v at
z = 1, so dφ = −dv/v. The semiclassical conjugation by e^(iφ/h) evaluates symbols at the covector translated by dφ: the
covector ζ of h²N⁰ corresponds to the covector ξ = ζ_v − 1/v of P. The dR-component of ζ is −v²ζ_v = −v(vξ + 1), which
is ξ_cħ over sf, and η_cħ = R⁻¹η = vη. With a := vξ + 1, ξ_cħ = −va, and [[eq:ii-f-1-13]] at z = 1 gives

    G_(ι,1) = 2(1 + Rξ_cħ)ξ_cħ + ξ_cħ² + |η_cħ|² = 2va(a − 1) + v²a² + v²|η|² = v²p,

as v²p = v²a(a + 2(a − 1)/v) + v²|η|² (since (v + 2)ξ + 1 = a + 2ξ and ξ = (a − 1)/v). Also
ξ̃ = −(v + 2)(vξ + 1) = (1 + 2/v)ξ_cħ = (1 + 2R)ξ_cħ. The conjugation carries p to R⁻² times the symbol of h²N⁰, that
is v²p = G_(ι,1), and preserves the Hamilton field up to the factor v² > 0 on Σ. Finally, at ĥ = 0 and z = 1,
[[eq:ii-f-3-12]] gives, with ξ := ξ_cħ, η := η_cħ,

    𝖧ξ̃ = (2(1 + 2R)ξ + 2) · 2Rξ + 2(|η|² − Rξ²)(1 + 2R),

and on {G_(ι,1) = 0}, |η|² = −2ξ − (1 + 2R)ξ², so

    𝖧ξ̃ = 4R(1 + 2R)ξ² + 4Rξ − 2(1 + 2R)(2ξ + (1 + 3R)ξ²) = −2(1 + R)ξ((1 + 2R)ξ + 2) = −2(1 + R)ξ_cħ(ξ̃ + 2).

On {G_(ι,1) = 0} over sf, 2ξ_cħ + (1 + 2R)ξ_cħ² = −|η_cħ|² ≤ 0 gives −2/(1 + 2R) ≤ ξ_cħ ≤ 0, that is ξ_cħ ≤ 0 and
ξ̃ + 2 ≥ 0; so 𝖧ξ̃ ≥ 0, with equality only where ξ_cħ = 0 or ξ̃ = −2.

(f) Complex conjugation of the coefficients exchanges z_0 = 1 and z_0 = −1, and the symbol identity is immediate. ∎

The function ξ̃ is the escape function of the problem: it increases along every bicharacteristic that is not one of the
two rays through the cone point, and on those it is −2 and 0; through the cone point it rises from −2 to 0 along the
curves of the face F_K of [[ch:s08]].

**Lemma {#lem:iii-g-4-2}** (The semiclassical order.) Let b_in > b_out with b_in + α_+ > ½(−1 + ϑ_in) and
b_out + α_+ < −½ + S̄ − ε_0 (here S̄ = min spec S̄ = 0 and ε_0 > 0 is small), the thresholds [[eq:ii-f-1-17]] at
R_(cf,1,in) and R_(cf,out). Let f_1 ∈ C^∞(ℝ) be non-increasing with f_1 = 1 on (−∞, −2 + δ′] and f_1 = 0 on [−δ′, ∞);
f_2 ∈ C_c^∞(ℝ) with 0 ≤ f_2 ≤ 1, f_2 = 1 on [0, L_0²] and f_2 = 0 on [4L_0², ∞); ψ a smooth compactly supported function
on the finite-frequency semiclassical phase space over sf (including the faces of [[ch:s08]] over R = 0), with
0 ≤ ψ ≤ 1, equal to 1 on a neighbourhood of 𝒞 := Σ ∩ supp(f_1(ξ̃)f_2(|η|²)), which is compact; and g ∈ C^∞(ℝ)
non-increasing with g = 1 on (−∞, −¼] and g = 0 on [−⅛, ∞). Here ξ̃, |η|² and the functions below are defined in the
frame of N_sf over {v < 4}, pulled back to the frame of P on {½ ≤ R ≤ 1} by the fibre translation of
[[sec:iii-g-4-1]], and over {R < ½} expressed in the variables of [[ch:s08]] ([[lem:iii-g-4-1]] (e)). Put

    𝖻 := b_out + (b_in − b_out)(1 − (1 − g(v))(1 − Φ)),   Φ := ψ f_1(ξ̃) f_2(|η|²)   (z_0 = 1),           {#eq:iii-g-4-2}

and its reflection for z_0 = −1. Then 𝖻 is smooth; it equals the constant b_in over {v ≤ −¼} at all frequencies;
it equals b_out near fibre infinity over {v ≥ −⅛} and near R_(cf,out); it equals b_in near R_(cf,1,in); and, on a
neighbourhood of Σ, it is non-increasing in the directions of propagation of [[prop:iii-g-4-6]]. These are: along H_p
(the future flow of [[ch:s08]]) on Σ_− and over {v > 0}; and in the direction of increasing v on Σ_+ over {v ≤ 0}
(backward along H_p) and at fibre infinity over {−1 < v < 0}. Its restriction to the face F_K of [[ch:s08]] is a decay
order admissible at σ_0 = ±1 with weight α_+ in the sense of [[sec:i-a-1-4]], as [[lem:ii-f-3-5]] requires of the
restriction of its order to F_K.

*Proof.* *Compactness of 𝒞.* In the cone region Σ is compact over sf ([[sec:ii-f-1-3]]: |ξ_cħ| and |η_cħ| are bounded
on {G_(ι,1) = 0}). Over {v ≤ 0}, f_1 ≠ 0 excludes Σ_+ (there a ≤ 0, so ξ̃ ≥ 0), and on Σ_− with L ≤ 2L_0,
[[lem:iii-g-4-1]] (c) bounds t. Over {0 < v ≤ 1}, on Σ_− write c := vt ∈ [0, 1], so a = 1 − c and
|η|² = t² − (1 − t − c)² = (1 − c)(2t − 1 + c); f_1(ξ̃) ≠ 0 gives (v + 2)(1 − c) ≥ δ′, so 1 − c ≥ δ′/3 and
|η|² ≥ (δ′/3)(2t − 1), and f_2 ≠ 0 bounds t. Over {1 ≤ v < 4}, t ≤ 1/v ≤ 1.

*Values.* Near fibre infinity ψ = 0. Near R_(cf,out), ξ̃ = (1 + 2R)ξ_cħ is near 0, so f_1 = 0. Near R_(cf,1,in), ξ̃ is
near −2 and |η|² = R²|η_cħ|² is near 0, and ψ = 1, so 𝖻 = b_in.

*The factor g.* Over {v ≤ −¼}, g = 1 and 𝖻 = b_in. Over {v ≥ −⅛}, g = 0 and 𝖻 = b_out + (b_in − b_out)Φ, treated
below. Near fibre infinity Φ = 0 (ψ = 0), and on a neighbourhood of Σ_+ ∩ {v ≤ 0}, Φ = 0 (ξ̃ ≥ 0 there, so f_1 = 0 on
{ξ̃ > −δ′}); there 𝖻 = b_out + (b_in − b_out)g(v) is non-increasing in v. On a neighbourhood of Σ_− over
{−¼ < v < −⅛}, H_pv > 0 ([[lem:iii-g-4-1]] (c)), and

    H_p(1 − (1 − g)(1 − Φ)) = g′(v)(H_pv)(1 − Φ) + (1 − g)H_pΦ ≤ 0,

as g′ ≤ 0, 0 ≤ Φ ≤ 1 and H_pΦ ≤ 0 (below).

*Monotonicity of Φ.* H_pΦ = ψf_2f_1′(ξ̃)H_pξ̃ + f_1f_2H_pψ, as H_p|η|² = 0 identically on {v < 4}
([[lem:iii-g-4-1]] (b)) and, in the cone region, {G_(ι,1), R²|η_cħ|²} = {v²p, |η|²} = 0 likewise. The second term
vanishes on a neighbourhood of Σ: supp dψ ∩ supp(f_1(ξ̃)f_2(|η|²)) is compact, as ψ has compact support, and does not
meet Σ, as ψ = 1 near 𝒞. For the first, f_1′ ≤ 0, and H_pξ̃ > 0 on
𝒞′ := Σ ∩ supp f_1′(ξ̃) ∩ supp f_2(|η|²), a compact set: over {v < 4} by [[lem:iii-g-4-1]] (b), as η ≠ 0 on 𝒞′
(there ξ̃ ∈ [−2 + δ′, −δ′], while ξ̃ ∈ {−2, 0} where η = 0); over the cone region by [[lem:iii-g-4-1]] (e), as
−ξ_cħ = −ξ̃/(1 + 2R) ≥ δ′/(1 + 2R) and ξ̃ + 2 ≥ δ′, so 𝖧ξ̃ ≥ 2δ′²/(1 + 2R). By continuity H_pξ̃ > 0 on a
neighbourhood O′ of 𝒞′. The compact set (supp ψ ∩ supp f_1′(ξ̃) ∩ supp f_2(|η|²)) ∖ O′ does not meet Σ, so on a
neighbourhood of Σ the first term is ≤ 0.

*The face F_K.* At R = 0, |η|² = 0, and on a neighbourhood of Σ ∩ F_K, ψ = 1, so
𝖻 = b_out + (b_in − b_out)f_1(ξ_cħ). This is non-increasing along the boundary flow on a neighbourhood of Σ ∩ F_K,
since at R = 0, 𝖧ξ_cħ = 2|η_cħ|² ≥ 0 everywhere ([[eq:ii-f-3-12]]), as [[eq:i-b-4-4]] requires (g = 0 there); and it is
constant near R_in (ξ_cħ = −2) and R_out (ξ_cħ = 0), with the thresholds there, which are those of [[eq:ii-f-1-17]] at
F_K (the proof of [[lem:ii-f-3-5]]). ∎

#### The estimates {#sec:iii-g-4-3}

**Lemma {#lem:iii-g-4-3}** (The semiclassical radial estimate at the light cone.) Let δ > 0, the fibre inner product
of [[lem:iii-g-1-4]], s < 2 − δ − C_λ constant, and 𝖻 as in [[lem:iii-g-4-2]]. For each sign there are neighbourhoods
U_* ⊂ U_0 of ∂ℛ_± at fibre infinity and a compact K_E ⊂ Ū_0 ∖ ∂ℛ_± such that, uniformly for z ∈ 𝒵_h and h < h_0, with
B_* microsupported in U_*, G elliptic on Ū_0, E′ elliptic on K_E, and all N_1, K:

    ‖B_*u‖_𝐨 ≤ C(h⁻¹‖GPu‖_(𝐨−(1,1,0)) + ‖E′u‖_𝐨 + h^(N_1)‖Gu‖_𝐨 + ‖u‖_(−K𝟏)),     𝐨 = (s, 𝖻),             {#eq:iii-g-4-3}

    ‖B_*v‖_(𝐨*) ≤ C(h⁻¹‖GP^(*h)v‖_(𝐨*−(1,1,0)) + h^(N_1)‖Gv‖_(𝐨*) + ‖v‖_(−K𝟏)),   𝐨* = (1 − s, 𝖻*),       {#eq:iii-g-4-4}

for any 𝖻* constant near ∂ℛ_± (in the notation of [[ch:s02]] for orders, the decay order being immaterial).

*Proof.* We verify the hypotheses of [[lem:i-b-5-1]] with F fibre infinity and Λ := ∂ℛ_±. (i): Re_hP has principal
symbol p_(±1) up to terms of the class of 𝒫_1 ([[lem:iii-g-4-1]] (a)), and with μ := |ξ|, 𝖧^𝐏 := μ⁻¹H_(p_(±1))
vanishes on Λ ([[lem:iii-g-2-1]] (b): Λ consists of radial points of the homogeneous part, and at fibre infinity the
field is that of p_2). Take ς := −sgn ξ for P (ε_♭ = 1), so that ς𝖧^𝐏 = −𝖧 near Λ and β_ϱ = −β_0 = −2(1 + v): a
sink; and for P^(*h) (ε_♭ = −1), ς := sgn ξ: a source. (ii): ℓ := 0, by [[lem:iii-g-4-1]] (a). (iii): g := ρ_∞²p_(±1)
and φ := q̃ of [[lem:iii-g-2-1]] (b); ς𝖧^𝐏φ = ∓𝖧q̃ + O(ρ_∞), which is [[eq:i-b-5-1]] by [[lem:iii-g-2-1]] (b). (iv):
s is constant, and 𝖻 = b_out near fibre infinity ([[lem:iii-g-4-2]]). (v): at fibre infinity
μ⁻¹p_1^𝐏 = sgn ξ (3 + 2Re_h S̄ − 2Re λ) by [[eq:iii-g-2-3]], with Re λ = −y/h: the term −2λh²∂_v = −2iz(h∂_v)
contributes 2(y/h)ξ = −2(Re λ)ξ to the symbol of h⁻¹Im_hP and its large part Re z only to Re_hP, the remaining terms
being as in [[lem:iii-g-2-2]]. So for P, κ̃ = s − ½ and, at Λ (v = 0),

    𝒯 = 2(s − ½)(−2(1 + v)) + 2(3 + 2Re_h S̄ − 2Re λ) = 4(2 + Re_h S̄ − Re λ − s) ≥ 4(2 − δ − C_λ − s) > 0;

for P^(*h) at 𝐨*, κ̃ = ½ − s and ε_♭ = −1, which gives the same condition, as in the proof of [[prop:i-b-5-2]].
[[lem:i-b-5-1]] gives [[eq:iii-g-4-3]] with the control term (the sink case) and [[eq:iii-g-4-4]] without it. ∎

**Lemma {#lem:iii-g-4-4}** (Semiclassical slab estimates.) [[prop:i-b-7-1]], [[prop:i-b-7-2]] and [[cor:i-b-7-3]] hold
for P = h²N_sf(λ) on the slabs {a < −v < b}, 0 < a < b < 2, for z ∈ 𝒵_h and h < h_0, with r replaced by −v, t by T,
and g by ĝ of [[lem:iii-g-1-2]] (g). In particular, with the cut-offs of [[lem:iii-g-2-3]],

    ‖u‖_(H^s_h({−1<v<−1/4})) ≤ Ch⁻¹‖Pu‖_(H^(s−1)_h({−1<v<−1/4}))     (u supported in {v ≥ −1}),
    ‖χv‖_(H̄^(1−s)_h) ≤ C(h⁻¹‖P^(*h)v‖_(H̄^(−s)_h) + ‖χ_1v‖_(H^(1−s)_h)).                                {#eq:iii-g-4-5}

*Proof.* By [[lem:iii-g-1-2]] (g), N_sf(λ) is the spectral family at σ = −iλ = z/h of the stationary operator P_c on
ℝ_T × sf° with metric ĝ, with P_c − □_ĝ of first order with T-independent coefficients, and dv timelike on the slab.
The proof of [[prop:i-b-7-1]] uses the hypotheses of [[ch:s02]] on the time function only through this, except at two
places. First, it uses Im z ≥ 0 and T[u′](−∇t, X) ≥ 0 to drop the term 2h⁻¹(Im z)T[u′](−∇t, X) of ^(W)K[u′]. Here ∇T
is spacelike, but |h⁻¹Im z| ≤ C_λ and |T[u′](∇T, X)| ≤ C|du′|²_R, so the term is bounded by C′|du′|²_R and is absorbed
by ℓT[u′](X, X) ≥ ℓc_0|du′|²_R for the weight parameter ℓ large. The flux identity E(1) = E(0) uses only the
T-independence. Second, the adjoint estimate is obtained there by t ↦ −t, to keep Im z ≥ 0; here the first argument
applies directly to P^(*h), the spectral family at z̄/h of the formal adjoint of P_c (|Im z̄| ≤ C_λh), with the ends of
the slab exchanged (the backward case of [[prop:i-a-6-3]], with the weight e^(−ℓr)) and X unchanged. The proof of
[[prop:i-b-7-2]] uses [[prop:i-a-6-4]] (iii) at fixed h ([[lem:iii-g-2-3]]), the monotonicity of v along every
characteristic point over the slab, at finite frequencies and at fibre infinity (H_(Ĝ)v = 2ĝ⁻¹(ν, dv) ≠ 0 for ĝ-null
ν ≠ 0, dv being timelike), and [[cor:i-b-4-6-prime]], valid here by [[rem:i-b-4-7]] (a) ([[lem:iii-g-4-1]] (a)); it
does not use the statement for Im z > 0 that there is no characteristic point at finite frequencies, which serves there
only as an alternative. [[cor:i-b-7-3]] follows as there. ∎

**Lemma {#lem:iii-g-4-5}** (The cone point.) On {R < ½}, [[prop:ii-f-2-4]], [[prop:ii-f-2-5]], [[prop:ii-f-2-6]] and
items (R3)–(R4) of [[lem:ii-f-3-3]] hold for P with z ∈ 𝒵_h and the order 𝖻 of [[lem:iii-g-4-2]], and [[lem:ii-f-3-5]]
and [[lem:ii-f-3-6]] hold for u supported in {R < ½}, with the proofs given there and these changes: in (R3), for
0 < y ≤ C_λh the term −yQ_1 is put into 𝒫_1 as for y ≤ 0 (its contribution ϖ⁻¹(−y)σ(Q_1) = 2yξ_cħ(1 + ĥ)²R/h is
bounded by 2C_λR and vanishes at R = 0); in (R4) and in the propagation along o_sf, the term with 𝒜, whose coefficient
has modulus |Im z|/|z|² ≤ C_λh, is part of 𝒫_1 for either sign (its symbol vanishes at R_(cf,out)); and in step (4) of
the proof of [[lem:ii-f-3-6]], |Im z| ≤ C_λh replaces |Im z| ≤ γ_+h. The constants depend on C_λ.

*Proof.* The three places listed are the only ones where the proofs of [[ch:s08]] use the range of Im z near the cone
point; elsewhere they use it only at 𝓘⁺ (the face F_I, items (R1)–(R2)), which does not occur here ([Hin26, footnote
86]). The order 𝖻 enters through [[eq:ii-f-1-17]] at R_(cf,1,in) and R_(cf,out), constancy near them, monotonicity along
the future flow, and its restriction to F_K in [[lem:ii-f-3-5]], all of which [[lem:iii-g-4-2]] provides. P_0 = 2L_b is
tf-admissible with the weight α_+ + 2 ∈ (0, 1) ([[prop:iii-f1-3-3]]), which is the hypothesis of [[lem:ii-f-3-5]]. ∎

**Proposition {#prop:iii-g-4-6}** ([Hin26, (9.9)] in dimension 4 + 1.) Let C_λ ≥ 1, δ > 0 small, s < 2 − δ − C_λ,
γ_cf ∈ (−1, 0), and 𝖻 as in [[lem:iii-g-4-2]]. There are h_0 > 0 and C such that for h < h_0 and z ∈ 𝒵_h

    ‖u‖_𝐨 ≤ C‖Pu‖_(𝒴_𝐨),     u ∈ ℋ_𝐨, Pu ∈ 𝒴_𝐨,                                                         {#eq:iii-g-4-6}

the dual estimate holds for P^(*h) on the dual spaces, and P: {u ∈ ℋ_𝐨 : Pu ∈ 𝒴_𝐨} → 𝒴_𝐨 is invertible.

*Proof.* *Step 1: the symbolic estimate.* We show ‖u‖_𝐨 ≤ C(‖Pu‖_(𝒴_𝐨) + ‖u‖_(𝐨_♭)),
𝐨_♭ := (−N_1; γ_cf, γ_cf; 𝖻 − ¼), first for u smooth and compactly supported in {v > −1} × 𝕊³ with R bounded below on
its support, then by density ([[lem:i-b-3-1]] in {v < 4}, [[lem:ii-f-2-2]] (g) near the cone, [[lem:i-a-6-1]] (a) at
v = −1). Cover the characteristic set, at finite frequencies over sf and at fibre infinity, by finitely many open sets
on which one of the following holds, in this order (for z_0 = 1; z_0 = −1 by [[lem:iii-g-4-1]] (f)).

(1) {v < −¼}: [[lem:iii-g-4-4]] at the constant semiclassical order 𝖻 = b_in there ([[lem:iii-g-4-2]]), which controls
u there in h^(−b_in)H^s_h by h^(−1−b_in)‖Pu‖_(H^(s−1)_h), at all frequencies, with no error term.

(2) Points of Σ, at finite frequencies or at fibre infinity, over {−½ < v < 4}, that are reached from {v < −¼} along the
direction of propagation: forward along H_p on Σ_− and on the fibre-infinity part of Σ over {−1 < v < 0} with ξ < 0;
backward along H_p on Σ_+ and on the part with ξ > 0. Here [[prop:i-b-4-5]] with [[cor:i-b-4-6-prime]] and
[[rem:i-b-4-7]] (a) (in either direction, as ℓ = 0) applies over {v < 4}, and [[prop:ii-f-2-5]] over {R < ¼} away from
the cone saddles, from (1); 𝖻 is non-increasing in these directions of propagation on a neighbourhood of Σ
([[lem:iii-g-4-2]]). By [[lem:iii-g-4-1]] (d) this covers: Σ_+ outside a neighbourhood of ∂ℛ_+; the curves (ii) up to
neighbourhoods of the cone saddles and of ∂ℛ_−; the incoming ray (iii) up to a neighbourhood of R_(cf,1,in); and fibre
infinity over {−1 < v < 0} outside neighbourhoods of ∂ℛ_±.

(3) Neighbourhoods of ∂ℛ_+ and ∂ℛ_−: [[eq:iii-g-4-3]], whose control sets K_E consist of elliptic points and of points
of Σ near ∂ℛ_± and off it, covered by (2) (on the curves (i) and (ii) and at fibre infinity) or by (6) below (on the
outgoing ray (iii) and the curves (ii) near it). For ∂ℛ_− this step is taken after (6).

(4) A neighbourhood U_3 of R_(cf,1,in), by (R3) ([[lem:iii-g-4-5]]), whose K_E ⊂ {R ≥ δ_1} lies in the set covered by
(2) (the points of Σ near R_(cf,1,in) with R > 0 lie on curves (ii) or (iii) from {v < −1}; the others are elliptic).

(5) The curves in F_K from R_(cf,1,in) to R_(cf,out), by [[prop:ii-f-2-5]] from U_3; then a neighbourhood U_5 of
R_(cf,out) by (R4), whose control set K_E ⊂ {φ ≥ δ_2} consists of points of Σ ∩ F_K on these curves, of points of Σ
over R > 0 near them, which lie on curves (ii) and so are covered by (2) or by [[prop:ii-f-2-5]] once more from (4), and
of elliptic points. This is steps (3)–(5) of the proof of [[lem:ii-f-3-4]], with "curves from R_(I⁺,1,in)" read as
"curves from {v < −1}".

(6) The outgoing ray (iii) and the curves (ii) near it, from U_5 to a neighbourhood of ∂ℛ_−: over {R < ½}
[[prop:ii-f-2-5]] (for P or for z⁻¹P, the term with 𝒜 being part of 𝒫_1), over {R > ¼} [[prop:i-b-4-5]] with
[[rem:i-b-4-7]] (a); 𝖻 is non-increasing along them ([[lem:iii-g-4-2]]), and equal to b_out near them away from the
cone.

(7) Elsewhere, the elliptic estimates ([[prop:i-b-2-10]] in {v < 4}, [[prop:ii-f-2-6]] near the cone), at finite
frequencies off Σ, at fibre infinity over {v ≥ 0} off ∂ℛ_±, and at the fibre infinity of the cone calculus.

Each estimate has its term h⁻¹‖GPu‖ bounded by C‖Pu‖_(𝒴_𝐨) (in {v < 4} the differential order of 𝒴_𝐨 is s − 1 and
its semiclassical order 𝖻 + 1, which is h⁻¹ times the order 𝖻; near the cone, [[sec:ii-f-3-4]] (d)), its term
‖E′u‖_𝐨 by an earlier one, and its errors h^(N_1)‖Gu‖_𝐨 + ‖u‖_(−K𝟏) in {v < 4}, and ‖Gu‖_(𝐨−¼𝐞) near the cone, by
C‖u‖_(𝐨_♭) + Ch‖u‖_𝐨. A microlocal partition of unity gives the claim, the last term being absorbed for h small. The
constants are uniform in z ∈ 𝒵_h: each estimate is uniform on neighbourhoods of z_* ∈ {±1}, the dependence on y being
through 𝒫_1, with |y/h| ≤ C_λ.

*Step 2: the transition face.* [[lem:ii-f-3-6]] ([[lem:iii-g-4-5]]) applied to χ_tf u, which is supported in
{R < Ch^(1/2)} ⊂ {R < ½}, with the commutator [P, χ_tf] estimated there, and on the support of 1 − χ_tf the bound
‖(1 − χ_tf)u‖_(𝐨_♭) ≤ Ch^(δ_♭)‖u‖_𝐨 of its proof, which in {v < 4} is the trivial bound for semiclassical orders
(ρ_sf ∼ h there), give ‖u‖_(𝐨_♭) ≤ C‖Pu‖_(𝒴_𝐨) + Ch^(δ_♭)‖u‖_𝐨, with 𝖻_♭ := 𝖻 − 2δ_♭ still satisfying the
conditions of [[lem:iii-g-4-2]]. With Step 1, [[eq:iii-g-4-6]] follows for h small.

*Step 3: the adjoint.* The same steps apply to P^(*h) on the dual spaces, with the directions of propagation reversed
and sources and sinks interchanged: [[eq:iii-g-4-4]] at ∂ℛ_±, this time without the control term; propagation backwards
along
the curves (ii)–(iii) to the cone point and through it ([[sec:ii-f-3-6]], the adjoint, for (R3)–(R4) and F_K); on Σ_+
and at fibre infinity, propagation from ∂ℛ_± to {v < −¼}; and near v = −1 the second estimate of [[eq:iii-g-4-5]],
whose term ‖χ_1v‖ lies over {−½ < v < −¼} and is controlled by the propagation just described. The dual semiclassical
order −𝖻 − 1 is non-increasing in these reversed directions, and is the constant −b_in − 1 over {v ≤ −¼}, where the
second estimate of [[eq:iii-g-4-5]] is used. Step 2 uses the second estimate of [[eq:ii-f-3-15]].

*Step 4: invertibility.* For fixed h < h_0, [[eq:iii-g-4-6]] gives injectivity and closed range, and the dual estimate
the triviality of the annihilator of the range (by the pairing ⟨Pu, v⟩ = ⟨u, P^(*h)v⟩ for u in a dense set, as in
[[sec:ii-f-3-6]]). ∎

### The spectral family: the theorem {#sec:iii-g-5}

**Theorem {#thm:iii-g-5-1}** ([Hin26, Proposition 9.2] in dimension 4 + 1.) Assume (C1) of [[sec:iii-f1-1]] and the
parameters of [[prop:iii-f1-3-3]], and let λ ∈ ℂ and (s, μ) be admissible for λ ([[eq:iii-g-2-6]]).

(1) (*Fredholm property.*) N_sf(λ): 𝒳 → 𝒴 of [[eq:iii-g-2-7]] is Fredholm of index 0, with kernel and cokernel
independent of the admissible pair.

(2) (*Invertibility.*) It is invertible for Re λ < 2. For every C it is invertible for all but finitely many λ with
Re λ ≤ C, and the inverse is finite-meromorphic: in every vertical strip on which one admissible pair serves,
λ ↦ N_sf(λ)⁻¹ ∈ ℒ(𝒴, 𝒳) is meromorphic with finite-rank principal parts, and for f in the targets of two admissible
pairs the two inverses agree.

(3) (*b-regularity at the light cone.*) If u ∈ Ḣ^(s,μ)_b and N_sf(λ)u ∈ Ḣ^((s−1;k),μ)_(b;b), k ∈ ℕ_0, then
u ∈ Ḣ^((s;k),μ)_(b;b).

*Proof.* (3) is [[prop:iii-g-2-7]]. (1): The Fredholm property and the independence are [[prop:iii-g-2-4]].

*Index.* Let ind(λ) be the index, which does not depend on the admissible pair. Near any λ_1, fix a pair admissible for
every λ in a disc D_1 around λ_1 (shrink the intervals of [[eq:iii-g-2-6]] by a margin). On D_1, 𝒳 is fixed
([[lem:iii-g-1-2]] (f)) and λ ↦ N_sf(λ) ∈ ℒ(𝒳, 𝒴) is holomorphic (a polynomial), so ind is constant on D_1, hence
constant on ℂ. By [[prop:iii-g-4-6]] with C_λ := |Re λ_1| + 1, N_h is invertible on ℋ_𝐨 for |Im λ| large, and by
[[sec:iii-g-4-1]] N_sf(λ) is then invertible from {u ∈ Ḣ^(s′,γ_cf+Re λ)_b : N_sf(λ)u ∈ Ḣ^(s′−1,γ_cf+Re λ)_b}, an
admissible pair (s′ < 2 − δ − C_λ ≤ 2 − Re λ and γ_cf + Re λ ∈ (Re λ − 1, Re λ)). So ind = 0.

(2): For Re λ < 2 the kernel is trivial ([[prop:iii-g-3-2]]) and the index is 0, so the operator is invertible.

*Meromorphy.* Let S be a vertical strip on which one admissible pair serves (its width is less than 1, by
[[eq:iii-g-2-6]]). On S the spaces 𝒳 and 𝒴 are fixed, and λ ↦ N_sf(λ) ∈ ℒ(𝒳, 𝒴) is a holomorphic family of Fredholm
operators of index 0. Near λ_1 ∈ S choose a finite-rank K_1: 𝒳 → 𝒴 with N_sf(λ_1) + K_1 invertible (the index is 0);
then N_sf(λ) + K_1 is invertible on a disc D_1 around λ_1, and there
N_sf(λ) = (N_sf(λ) + K_1)(Id − (N_sf(λ) + K_1)⁻¹K_1), the second factor being the identity minus a holomorphic family of
finite-rank operators. By (K5) of [[sec:i-c-2-1]]
(the analytic Fredholm theorem, [RS1, Theorem VI.14]), on D_1 either N_sf(λ) is invertible at no point, or it is
invertible off a discrete set, with an inverse that is meromorphic with finite-rank principal parts. The set of λ_1 ∈ S
at which the second alternative holds is open, and so is its complement; S is connected and contains points of
invertibility (those with |Im λ| large, by [[prop:iii-g-4-6]]), so the second alternative holds on all of S.

*Finiteness.* For 2 ≤ Re λ ≤ C, [[prop:iii-g-4-6]] with C_λ := C gives invertibility for |Im λ| ≥ M; the set where
N_sf(λ) is not invertible is discrete, so it meets the compact set {2 ≤ Re λ ≤ C, |Im λ| ≤ M} in finitely many points.

*Agreement.* If f ∈ 𝒴 ∩ 𝒴′ for two admissible pairs and λ is not a pole, the two solutions u, u′ both lie in the larger
domain (the spaces are nested in s and μ, and by [[eq:iii-g-2-6]] one may pass to the minimum of the two values of s
and of μ), where the kernel is trivial ([[prop:iii-g-2-4]] (3)); so u = u′. ∎

### The ι⁺-normal operator: setting {#sec:iii-g1-1}

This section and the next three are [Hin26, Definition 9.3, Proposition 9.4, Definition 9.6 and Remark 9.7] in
dimension 4 + 1 (pp. 169–172). They construct the inverse of the ι⁺-normal operator from that of the spectral family
([[thm:iii-g-5-1]]), describe its asymptotics at 𝓘⁺ ∩ ι⁺ (of radiation-field type, with exponents 3/2 plus the small
eigenvalues of S̄) and at K⁺ ∩ ι⁺ (polyhomogeneous, with an index set generated by the indicial roots of
[[prop:iii-f1-2-3]]), prove a version at finite regularity, and identify the boundary spectrum.

#### The operator {#sec:iii-g1-1-1}

We use the notation of [[sec:iii-g-1]]: v ∈ ℝ, ω ∈ 𝕊³, R := v⁻¹ near v = ∞, N_sf(λ) of [[eq:iii-g-1-3]], the spaces of
[[def:iii-g-1-3]], and the admissible pairs of [[eq:iii-g-2-6]]. Let ι⁺ := [0, ∞]_v × 𝕊³, a compact manifold with two
boundary hypersurfaces, 𝓘⁺ ∩ ι⁺ = {v = 0} and K⁺ ∩ ι⁺ = {R = 0}, which do not meet; their defining functions are
ρ_I := v/(1 + v) and ρ_K := R/(1 + R). On ι⁺ we use the unweighted b-density |dv/v dg̸| = |dR/R dg̸| and
H^(k,α_I,α_K)_b(ι⁺) := ρ_I^(α_I)ρ_K^(α_K)H^k_b(ι⁺) ([Hin26, Definition 2.6], as in [[sec:iii-a-1]]). Ċ^∞(ι⁺) is the
space of smooth sections vanishing to infinite order at ∂ι⁺. The *ι⁺-normal operator* ([Hin26, (9.10)–(9.11)] at
n = 4) is

    N_ι⁺(λ) := R^(−2−λ)N_sf(λ)R^λ = −2v(v∂_v − λ)(v∂_v − 3/2 − S̄) + v²L̃(0)(ω, v∂_v, ∂_ω)               {#eq:iii-g1-1-1}

on (0, ∞)_v × 𝕊³. This is [[eq:iii-g-1-6]] in the coordinate v. Indeed R^λ = v^(−λ) and v^λ(v∂_v)v^(−λ) = v∂_v − λ,
so with ∂_v = v⁻¹(v∂_v),

    v^λN_sf(λ)v^(−λ) = −2v⁻¹(v∂_v − λ)(v∂_v − 3/2 − S̄) + L̃(0)(ω, v∂_v, ∂_ω),

and R^(−2) = v². So on {0 < v < ∞}, N_ι⁺(λ)h = f is equivalent to

    (v∂_v − λ)(v∂_v − 3/2 − S̄)h = −(2v)⁻¹f + (v/2)L̃(0)(ω, v∂_v, ∂_ω)h,                                 {#eq:iii-g1-1-2}

which is [Hin26, (9.22)] at n = 4. Near R = 0, by [[eq:iii-g-1-6]],

    R²N_ι⁺(λ) = A_0 + RA_1,   A_0 := L̃(0)(ω, −R∂_R, ∂_ω),   A_1 := −2(R∂_R + λ)(R∂_R + 3/2 + S̄).       {#eq:iii-g1-1-3}

Since R²N_ι⁺(λ) = R^(−λ)N_sf(λ)R^λ, it is b-elliptic at R = 0 ([[lem:iii-g-1-2]] (b); conjugation by R^λ preserves
b-ellipticity). Its indicial family is N(R²N_ι⁺(λ), ζ) = L̃(0)(ω, −ζ, ∂_ω), which does not depend on λ. So its boundary
spectrum is {−μ}, μ over the indicial roots of [[prop:iii-f1-2-3]]: those of L̂_b(0), whose b-normal operator at ∂X is
^bL̄(0) = ρ²L̃(0)(ω, ρ∂_ρ, ∂_ω).

#### The endomorphism {#sec:iii-g1-1-2}

**Lemma {#lem:iii-g1-1-1}** (S̄ is semisimple.) Let γ_Υ < min(½s_C, ⅜), s_C := γ_C(1 − e_C)(1 − v_C). At every
ω ∈ 𝕊³, S̄(ω) is diagonalisable, with the eigenvalues of [[eq:iii-f-3-1]], which do not depend on ω. So
S̄ = Σ_(s∈σ_S) sΠ_s, σ_S := spec S̄, where the spectral projections Π_s are smooth on 𝕊³, Π_sΠ_(s′) = δ_(ss′)Π_s and
Σ_sΠ_s = Id.

*Proof.* The proof of [[lem:iii-f-3-1]] writes ρS̄ = UV, with U: T* ⊕ T* → S²T* and V: S²T* → T* ⊕ T*, and

    T_S := VU = [ ρS̄^C     0    ]
                [ V_2U_1   ρS̄^Υ ],

where S̄^C and S̄^Υ are the endomorphisms of the constraint propagation operator and of the gauge potential operator.
Both leave the angular covectors invariant and act on them as γ_C(1 − v_C), resp. γ_Υ, times the identity; and both
leave the span of dt_* and k := dt̄ + d|x| invariant, acting on it by triangular matrices with the diagonal entries
γ_C(1 − e_C)(1 − v_C) and 2γ_C(1 − v_C), resp. 2γ_Υ and γ_Υ(1 − e_Υ). As 0 < e_C, e_Υ, v_C < 1, the three eigenvalues of
each are distinct, so each is annihilated by a product of distinct linear factors and is diagonalisable. Their spectra
are disjoint, since spec S̄^Υ ⊂ (0, 2γ_Υ], spec S̄^C ⊂ [s_C, ∞) and 2γ_Υ < s_C. Let m_1 and m_2 be the minimal
polynomials of the diagonal blocks B_1 := ρS̄^C and B_2 := ρS̄^Υ of T_S. They have simple roots and no common root;
m_1(T_S) has first block row 0, and m_2(T_S) has second block column 0. So m_2(T_S)m_1(T_S) = 0, and T_S is
diagonalisable. All its eigenvalues are non-zero, so VU is invertible; let q be its minimal polynomial, so q(0) ≠ 0.
From (UV)^(j+1) = U(VU)^jV we get UV q(UV) = U q(VU) V = 0. Hence the minimal polynomial of UV divides t q(t), which has
simple roots, so UV and S̄ = ρ⁻¹UV are diagonalisable. Their eigenvalues are those of [[eq:iii-f-3-1]], independent of
ω. The projections are Π_s = ∏_(s′≠s)(S̄ − s′)/(s − s′), polynomials in S̄ with constant coefficients, hence
smooth. ∎

We write

    σ_Υ := {0, (1 − e_Υ)γ_Υ, γ_Υ, 2γ_Υ},   σ_C := γ_C{(1 − e_C)(1 − v_C), 1 − v_C, 2(1 − v_C)},   Π_C := Σ_(s∈σ_C)Π_s,
                                                                                                      {#eq:iii-g1-1-4}

so σ_S = σ_Υ ∪ σ_C, σ_Υ ⊂ [0, 2γ_Υ] ⊂ [0, ¾) and min σ_C = s_C. [Hin26] works in the splitting of its (5.27), where S̄
is lower triangular ([Hin26, (8.8)]) and one component carries two small exponents; in the eigenbasis each component
carries one, and the counterpart of that splitting at n = 4 is not needed here.

#### Index sets {#sec:iii-g1-1-3}

As in [Hin26, Definition 2.7] ([[sec:iii-a-1]]), (z, k) denotes the smallest index set containing (z, k), that is
{(z + j, l) : j ∈ ℕ_0, 0 ≤ l ≤ k}, π_1 denotes the projection of an index set to its exponents, and ∪̄ is the extended
union.

**Definition {#def:iii-g1-1-2}** ([Hin26, Definition 9.3] in dimension 4 + 1.) (1) (*Index sets at 𝓘⁺ ∩ ι⁺.*)

    ℰ^tot_(ι⁺,𝓘) := ⋃_(s∈σ_Υ)(3/2 + s, 0),   ℰ^C_(ι⁺,𝓘) := ℰ^tot_(ι⁺,𝓘) + 1,   ℰ_s := ℰ^C_(ι⁺,𝓘) ∪ (3/2 + s, 0)
                                                                                                      {#eq:iii-g1-1-5}

for s ∈ σ_Υ.

(2) (*Function spaces.*) For an index set ℰ_K at K⁺ ∩ ι⁺ and ℓ_I ∈ ℝ, 𝒜^((⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),ℰ_K)(ι⁺) is the space of
sections h with Π_Ch ∈ 𝒜^((ℰ^C_(ι⁺,𝓘),ℓ_I),ℰ_K) and Π_sh ∈ 𝒜^((ℰ_s,ℓ_I),ℰ_K) for s ∈ σ_Υ. Here [Hin26, Definition 2.8
and Notation 2.9] are used, with the index sets referring to {v = 0} and {R = 0}, in this order.
H^(k,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺) is defined in the same way. The sets ℰ_(ι⁺,𝓘,01), ℰ_(ι⁺,𝓘,1/) and
ℰ_(ι⁺,𝓘,0/) of [Hin26] are the ℰ_s for s = (1 − e_Υ)γ_Υ, γ_Υ and 0, its ℰ_(ι⁺,𝓘,11) is the union of those for 2γ_Υ
and (1 − e_Υ)γ_Υ, and 3/2 replaces its 1 throughout.

(3) (*The index set at K⁺ ∩ ι⁺.*) Fix α ∈ (−1, 0) and put A := R²N_ι⁺(λ). ℰ_K is the index set ℰ = ⋃_jℰ_j of
[[lem:iii-a-1-4]] for A with F = ∅, that is

    ℰ_0 := ℰ(α),   ℰ_(j+1) := ℰ(α) ∪̄ (ℰ_j + 1),                                                         {#eq:iii-g1-1-6}

where ℰ(α) is the smallest index set containing the (ζ, k) ∈ Spec_b(A) with Re ζ > α.

**Lemma {#lem:iii-g1-1-3}** (The index set at K⁺.) (a) ℰ_K depends neither on λ nor on α ∈ (−1, 0).

(b) ℰ_K ⊂ {Re z ≥ 0} and ℰ_K ∩ {Re z = 0} = {(0, 0)}. The exponents of ℰ(α) in (0, 1) are
λ^Υ_(s0,2) − 2 ∈ (0, z_Υ/3] and λ^Υ_(s1,2) − 2 ∈ (0, ¼), so min Re(ℰ_K ∖ {(0, 0)}) > 0.

(c) All exponents of ℰ(α) with real part at most 101 are real.

*Proof.* (a) Spec_b(A) is determined by N(A, ζ) = L̃(0)(ω, −ζ, ∂_ω), which does not depend on λ
([[sec:iii-g1-1-1]]). Its elements are the (−μ, k) with μ a root of [[prop:iii-f1-2-3]] and k below the order of the
root. No root has real part in (0, 1] ([[prop:iii-f1-2-3]] (a)), so Re(−μ) > α holds exactly when Re μ ≤ 0, for every
α ∈ (−1, 0).

(b), (c) The roots with Re μ ≤ 0 are those before the semicolons in [[prop:iii-f1-2-3]]. They are: 0 at s0 and s2;
the λ^C_(·,≪,·) − 1, with real part < −101 ([[prop:iii-f1-2-3]] (d)); −l, 1 − l and 2 − l at the types listed; −1 at
s1 and v1; −2 − 2γ_Cv_C at v1; and 2 − λ^Υ_(sl,l+j) (j = 1, 2) and 2 − λ^Υ_(s0,2). By [[lem:iii-d-4-1]] the last are
real, with λ^Υ_(s0,2) ∈ (2, 2 + z_Υ/3] and λ^Υ_(sl,l+j) ∈ (l + j, l + j + ¼) for 0 < z_Υ ≤ ½, where
z_Υ := 4e_Υγ_Υ². So every root with Re μ ≤ 0 other than 0 has Re μ < 0. The root 0 occurs only at s0 and s2 and is
simple there ([[prop:iii-f1-2-3]] (c)), giving (0, 0) only. The exponents −μ ∈ (0, 1) are λ^Υ_(s0,2) − 2 and
λ^Υ_(s1,2) − 2; the next ones are ≥ 1. The iterates ℰ_j + 1 only add points with real part ≥ 1. ∎

### Two lemmas at the light cone {#sec:iii-g1-2}

Words W^α and the modules 𝒟^m are those of [[sec:iii-g-2-4]] (products of v∂_v and the Lie derivatives ℒ_(Ω_a)).

**Lemma {#lem:iii-g1-2-1}** (Conormality at the light cone, every order.) Let s ∈ ℝ with s − ½ ∉ ℤ. There is
m(s) ∈ ℕ such that the following holds for every k ∈ ℕ_0. Let u ∈ H^s(ℝ × 𝕊³) be supported in [0, M] × 𝕊³, with
W^βu ∈ H^s for |β| ≤ k + m(s). Then for |α| ≤ k

    |W^αu(v, ω)| ≤ C v^(s−½) Σ_(|β|≤k+m(s)) ‖W^βu‖_(H^s)   on (0, 1) × 𝕊³,                               {#eq:iii-g1-2-1}

with C depending on s, k and M. In particular, if W^βu ∈ H^s for every word, then u is conormal at {v = 0⁺} with the
bound v^(s−½).

*Proof.* (i) *Values in ℋ := H²(𝕊³; ℂ^N) ⊂ C⁰.* Expand in spherical harmonics, with eigenvalues κ_j of Δ_(𝕊³). For
s ≥ 0, (1 + ξ² + κ_j)^s ≥ (1 + ξ²)^s. For s < 0, (1 + ξ²)^s ≤ (1 + ξ² + κ_j)^s(1 + κ_j)^(−s), since
(1 + ξ² + κ_j)/(1 + ξ²) ≤ 1 + κ_j. In both cases

    ‖g‖_(H^s(ℝ;H²(𝕊³))) ≤ C Σ_(|γ|≤2+⌈max(0,−s)⌉) ‖ℒ_Ω^γ g‖_(H^s).

This uses Δ_(𝕊³) = −Σ_aΩ_a² and Ω_a = ℒ_(Ω_a) − A_a with constant A_a (the proof of [[lem:iii-g-2-5]]). So
W^αu ∈ H^s(ℝ; ℋ) for |α| ≤ k + m(s) − 2 − ⌈max(0, −s)⌉.

(ii) *s > ½.* The Taylor argument of the proof of [[lem:iii-g-3-1]], applied to g = W^αu ∈ H^s(ℝ; ℋ) supported in
{v ≥ 0}, gives ‖g(v)‖_ℋ ≤ Cv^(s−½)‖g‖_(H^s(ℝ;ℋ)) on (0, 1); this is [[eq:iii-g1-2-1]].

(iii) *s < ½.* Let j ∈ ℕ with s + j > ½. For g ∈ H^σ(ℝ; ℋ) supported in [0, M′], let Ig be the distribution with
∂_vIg = g and Ig = 0 on {v < 0}, and let ζ ∈ C^∞(ℝ) equal 1 on (−∞, M′ + ½] and 0 on [M′ + 1, ∞). Then:

(α) ζIg is supported in [0, M′ + 1], and ∂_v(ζIg) = g + ζ′c with c := ⟨g, 1⟩ ∈ ℋ, since Ig = c on {v ≥ M′}. Its
Fourier transform is entire and equals the transform of ∂_v(ζIg) divided by iξ. This gives
‖ζIg‖_(H^(σ+1)(ℝ;ℋ)) ≤ C‖g‖_(H^σ(ℝ;ℋ)): use the quotient for |ξ| ≥ 1, and for |ξ| ≤ 1 the maximum principle on the
complex unit disc with the Paley–Wiener bound for compactly supported elements of H^σ.

(β) v∂_vIg = I((v∂_v + 1)g) and ℒ_ΩIg = I(ℒ_Ωg), since both sides vanish on {v < 0} and have the same v-derivative
(∂_v(v∂_vIg) = g + v∂_vg). So W^α(ζIg) = ζI(W̃^αg) + r, where W̃^α is W^α with every v∂_v replaced by v∂_v + 1, and r
is supported in [M′ + ½, M′ + 1] and built from v^iζ^(i) and I(W^γg) with |γ| < |α|.

Applying (α)–(β) j times, U := ζ_jI ⋯ ζ_1Iu satisfies W^αU ∈ H^(s+j)(ℝ; ℋ) for the same α, with bounds. By (ii) at
order s + j (with s + j − ½ ∉ ℕ_0), ‖W^αU(v)‖_ℋ ≤ Cv^(s+j−½) on (0, 1). On (0, 1), where every ζ_i equals 1, we have
u = ∂_v^jU = v^(−j)∏_(i=0)^(j−1)(v∂_v − i)U. Also W^αv^(−j) = v^(−j)W^α_((−j)), with v∂_v shifted by −j. So W^αu is
v^(−j) times a combination of words of length at most |α| + j applied to U. This gives [[eq:iii-g1-2-1]] with
m(s) := 2 + ⌈max(0, −s)⌉ + j. ∎

This is [[lem:iii-g-3-1]] with the number of words counted. It replaces the identifications [Hin26, (9.5) and (9.21)]
of supported and extendible Sobolev spaces with b-spaces, which [Hin26] takes from [Hin26c, Lemma 13.4]; as it holds
for every s ∉ ½ + ℤ and with the module regularity, the case distinction Re λ < 2 / Re λ > 1 of [Hin26] is not needed.

For an index set G and γ ∈ ℝ, 𝒜^((G,γ))([0, 1)_v × 𝕊³) consists of the sums

    Σ_((z,k)∈G, Re z<γ) v^z(log v)^k g_(z,k)(ω) + r,

with g_(z,k) smooth and |W^αr| ≤ C_αv^γ for all α. The statements below hold for all orders in open ranges, so this
L^∞-based version and the L²-based one of [Hin26, Definition 2.8] can be used interchangeably
(H^(∞,γ)_b ⊂ 𝒜^γ ⊂ H^(∞,γ−δ)_b near {v = 0}).

**Lemma {#lem:iii-g1-2-2}** (Integration at the light cone.) Let a ∈ ℂ, γ_0 < γ with γ ≠ Re a, G an index set with no
exponent of real part γ, and w on (0, 1) × 𝕊³ with |W^αw| ≤ C_αv^(γ_0) for all α. If (v∂_v − a)w = g ∈ 𝒜^((G,γ)), then
w ∈ 𝒜^((G ∪̄ {(a,0)}, γ)). If moreover Re a < γ_0 and a ∉ π_1G, then w ∈ 𝒜^((G,γ)). The same holds with H^(k,(G,γ))_b in
place of 𝒜^((G,γ)) and w ∈ ρ_I^(γ_0)H^k_b.

*Proof.* Since (v∂_v − a)(v^z(log v)^j) = (z − a)v^z(log v)^j + jv^z(log v)^(j−1), each term v^z(log v)^kφ of g has a
particular solution v^zP(log v)φ, where P is a polynomial of degree k if z ≠ a and of degree k + 1 if z = a.
Subtracting these leaves (v∂_v − a)w′ = r with |W^αr| ≤ C_αv^γ and w′ conormal. If Re a < γ, put
w″ := v^a∫_0^v t^(−a)r(t) dt/t; if Re a > γ, put w″ := −v^a∫_v^1 t^(−a)r(t) dt/t. In both cases |w″| ≤ Cv^γ. Also
v∂_vw″ = aw″ + r, and the rotations pass through the integral, so by induction |W^αw″| ≤ C_αv^γ. Then
(v∂_v − a)(w′ − w″) = 0, so w′ − w″ = c(ω)v^a, with c = v^(−a)(w′ − w″) at any fixed v, smooth in ω. If Re a > γ, cv^a
is of order γ. This proves the first claim. If Re a < γ_0 and a ∉ π_1G, the term cv^a is the only term of order v^a in
the expansion of w = O(v^(γ_0)), so c = 0. In the L² version the two integrals are bounded on ρ_I^γH^k_b by Hardy's
inequality: after the Mellin transform in v they are multiplication by (κ − a)⁻¹ on the line Re κ = γ. They commute
with the rotations and intertwine v∂_v, so the b-regularity is preserved. ∎

### The inverse of the ι⁺-normal operator {#sec:iii-g1-3}

**Theorem {#thm:iii-g1-3-1}** ([Hin26, Proposition 9.4] in dimension 4 + 1.) Assume the hypotheses of
[[thm:iii-g-5-1]] and γ_Υ < min(½s_C, ⅜) (the smallness 0 < γ_Υ ≪ 1 of [Hin26]). Let λ ∈ ℂ be such that N_sf(λ) is
invertible; by [[thm:iii-g-5-1]] this does not depend on the admissible pair. For f ∈ Ċ^∞(ι⁺; S²T*), extend R^(2+λ)f by
0 to {v ≤ 0} and set

    h := N_ι⁺(λ)⁻¹f := R^(−λ)N_sf(λ)⁻¹(R^(2+λ)f)|_((0,∞)_v×𝕊³).                                          {#eq:iii-g1-3-1}

Then N_ι⁺(λ)h = f, and:

(1) (*Conormality and polyhomogeneity.*) For every ℓ_I < 3/2 + s_C and every ℓ < 5/2 + s_C, with ℰ_K of
[[def:iii-g1-1-2]] (3),

    h ∈ 𝒜^((⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),ℰ_K)(ι⁺),     (v∂_v − 3/2 − S̄)h ∈ 𝒜^((ℰ^C_(ι⁺,𝓘),ℓ))([0, 1)_v × 𝕊³).      {#eq:iii-g1-3-2}

(2) (*Finite regularity.*) Let ℓ_I < 3/2 + s_C with ℓ_I ∉ Re π_1ℰ^tot_(ι⁺,𝓘), and let ℓ_K > −1 with
ℓ_K ∉ Re π_1ℰ_K. For Re λ < ℓ_I there is d ∈ ℕ_0, depending only on Re λ, ℓ_I and the parameters, such that for every
k ∈ ℕ_0 the map f ↦ h extends to a continuous linear map

    N_ι⁺(λ)⁻¹: H^(k+d,ℓ_I+1,ℓ_K−2)_b(ι⁺; S²T*) → H^(k,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),(ℰ_K,ℓ_K))_b(ι⁺; S²T*),         {#eq:iii-g1-3-3}

with (v∂_v − 3/2 − S̄)h ∈ H^(k,(ℰ^C_(ι⁺,𝓘),ℓ_I))_b([0, 1)_v × 𝕊³); the order here is ℓ_I and not ℓ_I + 1, as the
term −(2v)⁻¹f of [[eq:iii-g1-1-2]] has order ℓ_I only. On {Re λ < ℓ_I}, [[eq:iii-g1-3-3]] is finite-meromorphic in λ.
Its principal parts at poles do not depend on k, ℓ_I or ℓ_K, and their ranges lie in the space of (1).

*Proof.* *Step 0: h solves.* Let F := R^(2+λ)f, extended by 0. As f vanishes to infinite order at v = 0 and at R = 0,
F is smooth on ℝ_v × 𝕊³, supported in {v ≥ 0}, and O(R^∞) with all b-derivatives at R = 0. So F ∈ Ḣ^((s−1;∞),μ)_(b;b)
for every (s, μ). By [[thm:iii-g-5-1]] (2)–(3), h̃ := N_sf(λ)⁻¹F lies in Ḣ^((s;∞),μ)_(b;b) for every pair admissible
for λ, and the inverses agree. For 0 < a < 1, N_sf(λ)h̃ = 0 on {−1 < v < −a}, so [[lem:iii-g-2-3]] on the slab
Ω_(a,1), with the support at v = −1, gives h̃ = 0 there. Hence supp h̃ ⊂ {v ≥ 0} and h = v^λh̃|_(v>0). By
[[eq:iii-g1-1-1]], N_ι⁺(λ)h = v^(2+λ)N_sf(λ)h̃ = v^(2+λ)F = f.

*Step 1: a priori bounds.* Fix ε ∈ (0, ¼) with 3/2 − Re λ − ε ∉ ℤ, and put s := 2 − Re λ − ε; then (s, μ) is
admissible for μ ∈ (Re λ − 1, Re λ). *At v = 0:* take χ ∈ C_c^∞((−1, 2)) equal to 1 on [−½, 3/2]. On supp χ the norm of
Ḣ^(s,μ)_b is that of H^s, so χh̃ satisfies the hypotheses of [[lem:iii-g1-2-1]] for every k. Hence
|W^αh̃| ≤ C_αv^(3/2−Re λ−ε) on (0, 1). Since W^αv^λ = v^λW^α_((λ)) (with v∂_v shifted by λ),

    |W^αh| ≤ C_αv^(3/2−ε)   on (0, 1) × 𝕊³.                                                              {#eq:iii-g1-3-4}

*At R = 0:* R∂_R = −v∂_v and the rotations span the b-vector fields there. So h̃ ∈ R^μH^∞_b near R = 0
([[def:iii-g-1-3]]), and h = R^(−λ)h̃ ∈ R^αH^∞_b with α := μ − Re λ ∈ (−1, 0). [[lem:iii-a-1-4]] applies with
A := R²N_ι⁺(λ) (b-elliptic, [[sec:iii-g1-1-1]]), Ah = R²f ∈ Ċ^∞, F = ∅ and every β. It gives h ∈ H^(∞,(ℰ_K,β))_b near
R = 0 for every β ∉ Re spec_b(A); that is, h is polyhomogeneous at R = 0 with index set ℰ_K
([[lem:iii-g1-1-3]] (a)).

*Step 2: the expansion at v = 0 for Re λ < 3/2 − ε.* Π_s commutes with v∂_v and with S̄, so [[eq:iii-g1-1-2]] gives,
for each s ∈ σ_S,

    (v∂_v − λ)(v∂_v − 3/2 − s)Π_sh = Π_sg,   g := −(2v)⁻¹f + (v/2)L̃(0)(ω, v∂_v, ∂_ω)h.                  {#eq:iii-g1-3-5}

L̃(0)(ω, v∂_v, ∂_ω) is a combination of words with smooth coefficients (the proof of [[lem:iii-g-2-5]]). Fix
ℓ_I < 3/2 + s_C with ℓ_I ∉ Re π_1ℰ^tot_(ι⁺,𝓘); it suffices to prove [[eq:iii-g1-3-2]] for such ℓ_I, since
𝒜^((ℰ,ℓ′)) ⊂ 𝒜^((ℰ,ℓ)) for ℓ < ℓ′. Let ϑ_j := min(3/2 − ε + j, ℓ_I), and write ℰ^C := ℰ^C_(ι⁺,𝓘). We show by
induction that h ∈ 𝒜^((⟨ℰ^C⟩,ϑ_j)) at v = 0. For j = 0 this is [[eq:iii-g1-3-4]], as min Re ℰ_s = 3/2 > ϑ_0.

For the step: ℰ^C and the ℰ_s lie in ℰ^tot_(ι⁺,𝓘), and words preserve 𝒜^((ℰ^tot_(ι⁺,𝓘),ϑ_j)). So
g ∈ 𝒜^((ℰ^C,ϑ_j+1)), the f-term vanishing to infinite order. Apply [[lem:iii-g1-2-2]] to w_1 := (v∂_v − 3/2 − s)Π_sh,
which is O(v^(3/2−ε)) by [[eq:iii-g1-3-4]], with a = λ. Here Re λ < 3/2 − ε (the γ_0 of [[lem:iii-g1-2-2]]) and
λ ∉ π_1ℰ^C (whose real parts are ≥ 5/2), so w_1 ∈ 𝒜^((ℰ^C,ϑ_(j+1))). Apply [[lem:iii-g1-2-2]] again, to Π_sh with
a = 3/2 + s. For s ∈ σ_Υ, 3/2 + s ∉ π_1ℰ^C = 5/2 + σ_Υ + ℕ_0, as |s − s′| ≤ 2γ_Υ < 1; so
Π_sh ∈ 𝒜^((ℰ^C ∪ (3/2+s,0), ϑ_(j+1))) = 𝒜^((ℰ_s,ϑ_(j+1))). For s ∈ σ_C, Re(3/2 + s) ≥ 3/2 + s_C > ℓ_I ≥ ϑ_(j+1), so
Π_sh ∈ 𝒜^((ℰ^C,ϑ_(j+1))). (Each use has ϑ_(j+1) ≠ Re a, since ε + s ∈ (0, 1) for s ∈ σ_Υ, and ℓ_I is chosen, as the
monotonicity allows, with ℓ_I ≠ Re λ, ℓ_I + 1 ≠ Re λ and ℓ_I ∉ Re π_1ℰ^tot_(ι⁺,𝓘).) After finitely many steps
ϑ_j = ℓ_I. At that step g ∈ 𝒜^((ℰ^C,ℓ_I+1)), and the first application of [[lem:iii-g1-2-2]] gives
(v∂_v − 3/2 − S̄)h = Σ_s w_1 ∈ 𝒜^((ℰ^C,ℓ_I+1)). With Step 1 this proves (1) for Re λ < 3/2 − ε, and so for
Re λ < 3/2.

*Step 3: general λ, no v^λ-terms.* Let 𝒫 be the set of poles of N_sf(·)⁻¹. It is closed and discrete, with finitely
many points in each half plane {Re ≤ C} ([[thm:iii-g-5-1]] (2)). Let Λ_0 := 𝒫 ∪ (3/2 + σ_S + ℕ_0), also closed and
discrete; so 𝒪 := ℂ ∖ Λ_0 is open and connected. For ν ∉ 𝒫 put h(ν) := N_ι⁺(ν)⁻¹f.

(a) *Holomorphy.* Let ν_0 ∉ 𝒫. Choose a disc D ∋ ν_0 disjoint from 𝒫, and a pair (s, μ) admissible for every ν ∈ D,
with s − ½ ∉ ℤ (as in the proof of [[thm:iii-g-5-1]]). Let 𝒳_k := {u ∈ Ḣ^((s;k),μ)_(b;b) :
N_sf(ν)u ∈ Ḣ^((s−1;k),μ)_(b;b)} and 𝒴_k := Ḣ^((s−1;k),μ)_(b;b). The difference N_sf(ν) − N_sf(ν_0) is (ν − ν_0)
times −2∂_v plus a module element ([[lem:iii-g-1-2]] (f)). Since [v∂_v, ∂_v] = −∂_v, ∂_v commutes with the rotations,
and ∂_v = −R²∂_R at R = 0, this difference maps Ḣ^((s;k),μ)_(b;b) to 𝒴_k. So 𝒳_k does not depend on ν ∈ D. By
[[thm:iii-g-5-1]] (3), N_sf(ν): 𝒳_k → 𝒴_k is a holomorphic family of bijections, so ν ↦ N_sf(ν)⁻¹ ∈ ℒ(𝒴_k, 𝒳_k) is
holomorphic; so is ν ↦ R^(2+ν)f ∈ 𝒴_k. With [[lem:iii-g1-2-1]], whose bound is linear in the norms,
ν ↦ v^(−(s−½))W^αh̃(ν) ∈ L^∞((0, 1) × 𝕊³) is holomorphic on D, and h(ν) = v^νh̃(ν).

(b) *The Mellin recursion.* Let χ ∈ C_c^∞([0, 1)) equal 1 on [0, ½], and ℳ(u)(κ) := ∫_0^∞ v^(−κ)u(v) dv/v. By (a),
shrinking D, (ν, κ) ↦ ℳ(χh(ν))(κ) is holomorphic on D × {Re κ < 3/2 − 2ε_0} for some ε_0 > 0. We have
ℳ(v∂_vu) = κℳ(u) and ℳ(vu)(κ) = ℳ(u)(κ − 1). Applying ℳ to [[eq:iii-g1-3-5]] for χh(ν) gives

    (κ − ν)(κ − 3/2 − s)Π_sℳ(χh(ν))(κ) = ½Π_sL̃(0)(ω, κ − 1, ∂_ω)ℳ(χh(ν))(κ − 1) + H_s(ν, κ).            {#eq:iii-g1-3-6}

Here H_s is the transform of −χΠ_sf/(2v) and of the commutator of the operators in [[eq:iii-g1-3-5]] with χ; apart from
the term vanishing to infinite order it is supported in [½, 1). So H_s is entire in κ and holomorphic in ν ∈ D. By
induction on the strips {Re κ < 3/2 − 2ε_0 + j}, [[eq:iii-g1-3-6]] continues ℳ(χh(ν))(κ) meromorphically to D × ℂ. Its
singularities lie on {κ ∈ ν + ℕ_0} ∪ {κ ∈ 3/2 + σ_S + ℕ_0}, and it decays rapidly as |Im κ| → ∞ on vertical lines away
from them, since ℳ(χ(v∂_v)^Nh) = κ^Nℳ(χh) plus terms supported in [½, 1). By Mellin inversion and the circle
integrals of [[lem:iii-a-1-5]], the expansion of χh(ν) at v = 0 is read off from the principal parts: a term
c v^z(log v)^k corresponds to the principal part −k! c (κ − z)^(−k−1) at κ = z, since
ℳ(χv^z)(κ) = −(κ − z)⁻¹ + (an entire function).

(c) *The v^ν-coefficient vanishes on 𝒪.* Let ν_0 ∈ 𝒪. Choose r ∈ (0, ½) smaller than the distance from ν_0 to
3/2 + σ_S + ℕ_0, and let |ν − ν_0| < r/2. Inside the circle ∂D_r(ν_0) := {|κ − ν_0| = r}, the only singularity of
ℳ(χh(ν)) is at κ = ν. It is at most simple: in [[eq:iii-g1-3-6]] at κ = ν, ℳ(χh(ν))(ν − 1) is finite, because
ν − 1 ∉ ν + ℕ_0 and ν − 1 ∉ 3/2 + σ_S + ℕ_0, as ν_0 ∈ 𝒪. So

    c(ν) := (2πi)⁻¹ ∮_(∂D_r(ν_0)) Π_sℳ(χh(ν))(κ) dκ                                                      {#eq:iii-g1-3-7}

is minus the coefficient of v^ν in Π_sh(ν), and is holomorphic in ν, the integrand being jointly holomorphic near the
circle. If Re ν < 3/2 − 2ε_0, then ℳ(χh(ν)) is holomorphic at κ = ν, so c(ν) = 0. As 𝒪 is connected and c is
intrinsically the residue at κ = ν, c ≡ 0 on 𝒪. Then [[eq:iii-g1-3-6]] has no singularity at κ = ν, and so none at
κ ∈ ν + ℕ_0 either. For λ ∈ 𝒪 the induction of Step 2 therefore goes through with Re λ arbitrary: in
[[lem:iii-g1-2-2]] with a = λ, the possible term c_1v^λ in w_1 equals (λ − 3/2 − s) times the v^λ-coefficient of Π_sh,
which is 0; and no logarithm arises at λ, as λ ∉ 3/2 + σ_S + ℕ_0 ⊃ π_1ℰ^C. So (1) holds for λ ∈ 𝒪.

*Step 4: λ ∈ (3/2 + σ_S + ℕ_0) ∖ 𝒫, no extra logarithms.* Choose r ∈ (0, ½) such that the closed disc D̄_r(λ) meets
Λ_0 only at λ, and let 0 < |ν − λ| < r/2. Then ν ∈ 𝒪, and by Step 3 the only singularity of Π_sℳ(χh(ν)) inside
∂D_r(λ) is at κ = λ. Its order is at most some k_s for all such ν: at κ = λ the recursion [[eq:iii-g1-3-6]] involves ν
only through (κ − ν)⁻¹, which is regular there. Its Laurent coefficient of order k_s is the coefficient of the generic
expansion of Π_sh(ν), of the form found in Step 3. The map (ν, κ) ↦ ℳ(χh(ν))(κ) is jointly holomorphic on
D_(r/2)(λ) × (a neighbourhood of ∂D_r(λ)), by (a)–(b): the singular sets κ = ν and 3/2 + σ_S + ℕ_0 stay away from the
circle. So for every j ≥ 0

    ∮_(∂D_r(λ)) (κ − λ)^jΠ_sℳ(χh(ν))(κ) dκ → ∮_(∂D_r(λ)) (κ − λ)^jΠ_sℳ(χh(λ))(κ) dκ   (ν → λ).           {#eq:iii-g1-3-8}

For j ≥ k_s the left side vanishes, so the pole of Π_sℳ(χh(λ)) at κ = λ has order at most k_s. With j = k_s − 1, its
leading Laurent coefficient is the limit of the generic ones. So Π_sh(λ) carries, at the exponent λ, no logarithm and
no component beyond those that Π_sh(ν) carries. For Re λ < ℓ_I (respectively < ℓ), λ ∈ 3/2 + σ_Υ + ℕ_0 =
π_1ℰ^tot_(ι⁺,𝓘) (respectively also λ = 3/2 + s, s ∈ σ_C, for the second statement). At such λ the generic exponent
structure is that of [[eq:iii-g1-3-2]], and the remaining exponents of the expansions are unaffected (Step 3). So (1)
holds at λ. Exponents with real part beyond the order of [[eq:iii-g1-3-2]] do not enter.

*Step 5: finite regularity.* Let f ∈ H^(k+d,ℓ_I+1,ℓ_K−2)_b(ι⁺) and Re λ < ℓ_I.

(i) *Near v = 0:* v^(−2−λ)f ∈ ρ_I^(ℓ_I−1−Re λ)H^(k+d)_b with ℓ_I − 1 − Re λ > −1, so it is in L¹ near v = 0 with values
in H^(k+d)(𝕊³). Its extension F by 0 lies in H^(−½−δ)(ℝ; H^(k+d)(𝕊³)) ⊂ H^(−½−δ)(ℝ × 𝕊³) (the inclusion as in
[[lem:iii-g1-2-1]] (i), for negative order). Moreover v∂_vF is the extension of v∂_v(v^(−2−λ)f): the boundary term
vuφ at v = 0 vanishes because |u| ≤ Cv^(ℓ_I−1−Re λ), by b-Sobolev embedding in v.

(ii) *Near R = 0:* F ∈ R^(ℓ_K+Re λ)H^(k+d)_b. Choose δ > 0 and s := min(½, 2 − Re λ) − δ with s − ½ ∉ ℤ, and
μ ∈ (Re λ − 1, min(Re λ, ℓ_K + Re λ)), which is non-empty as ℓ_K > −1. Then (s, μ) is admissible, and
F ∈ Ḣ^((s−1;k+d),μ)_(b;b): near v = 0 by (i), as s − 1 ≤ −½ − δ and v∂_v and the rotations pass to the extension by 0;
near R = 0 as μ < ℓ_K + Re λ. So h̃ := N_sf(λ)⁻¹F ∈ Ḣ^((s;k+d),μ)_(b;b) ([[thm:iii-g-5-1]] (3)), vanishing on
{v < 0} as in Step 0.

(iii) *The expansion at v = 0:* [[lem:iii-g1-2-1]] gives |W^αh| ≤ C‖f‖v^(Re λ+s−½) for |α| ≤ k + d − m(s), hence the
weighted L² bound with a loss δ in the weight. The induction of Step 2 then runs with the L² version of
[[lem:iii-g1-2-2]]. Each step loses two b-derivatives (through L̃(0)), and the number of steps is at most
⌈ℓ_I − Re λ⌉ + 2; this fixes d in terms of Re λ and ℓ_I. Here the f-term of g stops the expansion at ℓ_I. In the first
application of [[lem:iii-g1-2-2]], this time with γ_0 = Re λ + s − ½ − δ < Re λ, terms c_λ(f)v^λ and, when
λ ∈ π_1ℰ^C_(ι⁺,𝓘), c′_λ(f)v^λ log v may appear, with c_λ and c′_λ continuous linear functionals. By Steps 3–4, c′_λ(f)
and c_λ(f) vanish (or c_λ(f) is a coefficient permitted by [[eq:iii-g1-3-2]], when λ ∈ π_1ℰ^tot_(ι⁺,𝓘)) for
f ∈ Ċ^∞(ι⁺). That space is dense, so the same holds for all f.

(iv) *At R = 0:* the proof of [[lem:iii-a-1-4]] applies at finite order. b-ellipticity gains two b-derivatives, and
the expansion terms have smooth coefficients (they come from residues of N(A, ·)⁻¹ and from RA_1, with F = ∅). It gives
h ∈ H^(k+d+2,(ℰ_K,ℓ_K))_b near R = 0, as ℓ_K ∉ Re π_1ℰ_K. This proves [[eq:iii-g1-3-3]], and the statement on
(v∂_v − 3/2 − S̄)h is the last application of [[lem:iii-g1-2-2]] in (iii), with γ = ℓ_I, for λ ∉ 𝒫.

*Meromorphy.* f ↦ F is holomorphic in λ, and λ ↦ N_sf(λ)⁻¹ ∈ ℒ(𝒴_k, 𝒳_k) is finite-meromorphic ([[thm:iii-g-5-1]] (2),
and (a) above). Multiplication by v^λ is holomorphic into weights reduced by any δ > 0. The expansion coefficients of
(iii)–(iv) are holomorphic in λ as well, although the decomposition of [[lem:iii-g1-2-2]] is not (its particular
solutions have poles where λ ∈ π_1G): each coefficient at an exponent z, Re z < ℓ_I, is
(2πi)⁻¹∮(κ − z)^jΠ_sℳ(χh(λ))(κ) dκ over a fixed small circle around z, and is holomorphic by the joint holomorphy of
Step 3 (b), which for f in the weighted space holds on {Re κ < ℓ_I}: there H_s is the transform of
−χΠ_sf/(2v) ∈ ρ_I^(ℓ_I)H_b and of terms supported in [½, 1). The remainder, h minus the finite expansion, is
holomorphic in the weaker weight in which h(λ) is, and bounded in the ℓ_I-weighted space locally uniformly in λ, the
constants of Steps 1–5 being built from N_sf(λ)⁻¹ and fixed-circle integrals. A locally bounded map from an open subset
of ℂ into a Banach space X such that x* ∘ f is holomorphic for every x* in a subspace of X* that separates the points
of X is holomorphic ([AN00, Theorem 3.1]); applied with X the ℓ_I-weighted space and the functionals of the larger
space, this shows that the remainder is holomorphic in the ℓ_I-weighted space. So [[eq:iii-g1-3-3]] is
finite-meromorphic on {Re λ < ℓ_I}. Its principal part at λ_0 is obtained by expanding R^(±λ) about λ_0: its Laurent
coefficients are finite combinations of R^(−λ_0)(log R)^iA_(−j)(log R)^(i′)R^(2+λ_0), with A_(−j) those of N_sf⁻¹.
These have finite rank and do not depend on (s, μ), as the inverses agree ([[thm:iii-g-5-1]] (2)); so they do not
depend on k, ℓ_I or ℓ_K. For f ∈ Ċ^∞(ι⁺), the coefficient of order j is
(2πi)⁻¹∮(λ − λ_0)^(j−1)N_ι⁺(λ)⁻¹f dλ over a small circle in 𝒪. By (1), with expansion coefficients and remainders
continuous in λ on the circle, it lies in the space of (1). The coefficients have finite rank and Ċ^∞(ι⁺) is dense,
so their ranges lie there for all f. ∎

### The boundary spectrum {#sec:iii-g1-4}

**Definition {#def:iii-g1-4-1}** ([Hin26, Definition 9.6] in dimension 4 + 1.) spec_ι⁺(L̄) is the set of poles of
λ ↦ N_ι⁺(λ)⁻¹ acting on Ċ^∞(ι⁺; S²T*), that is, of the λ_0 at which λ ↦ N_ι⁺(λ)⁻¹f ∈ C^∞((0, ∞) × 𝕊³) fails to be
holomorphic for some f. Spec_ι⁺(L̄) is the set of pairs (λ, k) with λ a pole of order k + 1.

**Lemma {#lem:iii-g1-4-2}** (a) spec_ι⁺(L̄) ⊂ 𝒫 ⊂ {Re z ≥ 2}, with finitely many points in every half plane
{Re z ≤ C}.

(b) For ℓ_I, ℓ_K as in [[thm:iii-g1-3-1]] (2), Spec_ι⁺(L̄) ∩ {Re λ < ℓ_I} is the divisor of [[eq:iii-g1-3-3]] on
H^(∞,ℓ_I+1,ℓ_K−2)_b.

(c) ([Hin26, Remark 9.7] in dimension 4 + 1.) Let λ_0 ∈ 𝒫 ∖ spec_ι⁺(L̄), and suppose that the principal part of
N_sf(λ)⁻¹ at λ_0 does not vanish on the extensions by 0 of Ċ^∞(ι⁺). Then ker N_sf(λ_0) contains a non-zero
distribution supported in {v = 0}. By [[lem:iii-g1-4-3]] this forces λ_0 ∈ 5/2 + spec S̄ + ℕ_0.

*Proof.* (a) N_ι⁺(λ)⁻¹ = R^(−λ)N_sf(λ)⁻¹R^(2+λ) is holomorphic off 𝒫 ([[thm:iii-g1-3-1]]), and
𝒫 ⊂ {Re ≥ 2} with finitely many points in each half plane, by [[thm:iii-g-5-1]] (2).

(b) Ċ^∞(ι⁺) is dense in H^(∞,ℓ_I+1,ℓ_K−2)_b (in its Fréchet topology). The Laurent coefficients of [[eq:iii-g1-3-3]]
are continuous and of finite rank, and they agree with those on Ċ^∞, so the pole orders agree.

(c) Let N_sf(λ)⁻¹ = Σ_(i=1)^m A_(−i)(λ − λ_0)^(−i) + (holomorphic), and let j be the largest i with A_(−i)F ≠ 0 for
some F in the extensions by 0 of Ċ^∞(ι⁺). Write R^(2+λ)f = Σ_i ((λ − λ_0)^i/i!)(log R)^iR^(2+λ_0)f, and use
(log R)^iR^(2+λ_0)f ∈ Ċ^∞(ι⁺). Then the coefficient of (λ − λ_0)^(−j) in R^(−λ)N_sf(λ)⁻¹R^(2+λ)f is
R^(−λ_0)A_(−j)(R^(2+λ_0)f). As λ_0 ∉ spec_ι⁺(L̄), this vanishes on {v > 0}. Further
A_(−j)F = (2πi)⁻¹∮(λ − λ_0)^(j−1)N_sf(λ)⁻¹F dλ is supported in {v ≥ 0} (Step 0 of the proof of [[thm:iii-g1-3-1]]),
so A_(−j)F is supported in {v = 0}. The coefficient of (λ − λ_0)^(−j) in N_sf(λ)N_sf(λ)⁻¹ = Id is
N_sf(λ_0)A_(−j) + ∂_λN_sf(λ_0)A_(−j−1) + ½∂_λ²N_sf(λ_0)A_(−j−2) = 0 (N_sf is quadratic in λ). Applied to such F, with
A_(−i)F = 0 for i > j, this gives N_sf(λ_0)A_(−j)F = 0. ∎

**Lemma {#lem:iii-g1-4-3}** (Kernels supported at the light cone.) If 0 ≠ u ∈ ker N_sf(λ), in 𝒳 for an admissible
pair, is supported in {v = 0}, then λ ∈ 5/2 + spec S̄ + ℕ_0.

*Proof.* A distribution supported in {0} × 𝕊³ and lying in H^s is u = Σ_(i=0)^j δ^(i)(v) ⊗ a_i, with distributions
a_i on 𝕊³; take a_j ≠ 0. As distributions, vδ^(i) = −iδ^(i−1) (for ⟨vδ^(i), φ⟩ = (−1)^i(vφ)^(i)(0) = (−1)^i iφ^(i−1)(0)),
so v∂_vδ^(i) = vδ^(i+1) = −(i + 1)δ^(i), and every polynomial F satisfies F(v∂_v)δ^(i) = F(−i − 1)δ^(i). Hence, by
[[eq:iii-g-1-3]],

    N_sf(λ)(δ^(i) ⊗ a) = −2δ^(i+1) ⊗ (λ − i − 5/2 − S̄)a + δ^(i) ⊗ L̃(0)(ω, λ − i − 1, ∂_ω)a:            {#eq:iii-g1-4-1}

the first term is −2∂_v applied to (λ − i − 1 − 3/2 − S̄)(δ^(i) ⊗ a), and the second is L̃(0)(ω, v∂_v + λ, ∂_ω) at
v∂_v = −i − 1. The coefficient of δ^(j+1) in N_sf(λ)u = 0 is −2(λ − j − 5/2 − S̄)a_j = 0. By [[lem:iii-g1-1-1]],
(λ − j − 5/2 − s)Π_sa_j = 0 for every s, and Π_sa_j ≠ 0 for some s; so λ = j + 5/2 + s. ∎

In dimension 3 + 1 the same argument gives 2 + spec S̄ + ℕ_0, which fits the observation of [Hin26] that its (9.5)
is available for Re λ < 2. Such poles are invisible on ι⁺ and belong to the radiation field ([BVW15, Remarks 7.5 and
8.2], as [Hin26] notes).

### Formal solutions at K⁺: the window and its states {#sec:iii-g2-1}

This section and the next three are [Hin26, Definitions 9.8 and 9.10, Propositions 9.9 and 9.11 and Corollary 9.12] in
dimension 4 + 1 (pp. 172–179). [[thm:iii-g2-3-1]] describes the solutions of [[thm:iii-g1-3-1]] at ι⁺ ∩ K⁺, term by
term, as formal solutions built from zero energy states. [[thm:iii-g2-4-2]] grafts such a solution into spacetime as an
approximate solution of L_b on the Myers–Perry family, accurate at ι⁺ and at K⁺, and [[cor:iii-g2-4-3]] does the same
for sources with logarithms in t_* and at ι⁺-resonances.

*The window.* [Hin26] expands at R = 0 up to R^(ℓ_K) with ℓ_K < 3 + ε_ind, which keeps the indicial roots in [−3, 0],
each with generalised companions to the orders of [Hin26, (9.32)], because the smallest ι⁺-order it grafts is λ = 1
and the remainder must have K⁺-order λ + ℓ_K > 4. What the uses of grafting require is λ + ℓ_K ≥ 4 + ε, with ε the
ε_K or ε_ind of [Hin26, (12.21), p. 308]. In dimension 4 + 1 the expansion is carried to ℓ_K < ℓ_K^max ≤ 3
([[eq:iii-g2-1-1]]); [[thm:iii-g2-3-1]] and [[thm:iii-g2-4-2]] hold for every ℓ_K < ℓ_K^max, so a graft at ι⁺-order λ
meets the requirement whenever Re λ > 1 + ε and ℓ_K^max = 3. The pure ι⁺-resonances have real part at least 2
([[thm:iii-g-5-1]] (2)), and [[cor:iii-g2-4-3]] grafts at orders Re λ_0 > 1. The window (−3, 0] needs no zero energy
state at −3, and every state it needs is constructed in [[ch:s13]] and [[ch:s15]], with at least the companions
required ([[def:iii-g2-table-1-1]]).

Throughout this section and the next three we assume (Dyn), the dynamical hypotheses of [[ch:s13]], which hold
for g_b, b near b_0, by [[thm:vi-a-6-1]] and [[thm:vi-b1-5-1]]; the parameters of [[prop:iii-f1-3-3]] with γ_Υ <
min(½s_C, ⅜) ([[lem:iii-g1-1-1]]); (C1) of
[[sec:iii-f1-1]]; and (C2)–(C3) of [[sec:iii-f1-1]] with z_Υ := 4e_Υγ_Υ² outside the exceptional set Z_exc of
[[prop:iii-f1-2-3]] (e), so that every indicial root of L̂_b(0) is simple. We fix

    ℓ_K^max := min(3, 2 + 2γ_Cv_C),                                                                     {#eq:iii-g2-1-1}

so that the vector type 1 root −2 − 2γ_Cv_C of [[prop:iii-f1-2-3]] lies below the window; the other roots from □^C with
real part ≤ 0 lie below −101 ([[prop:iii-f1-2-3]] (d)). Under the condition

(C5) γ_Cv_C ≥ ½,

ℓ_K^max = 3. The choice of parameters in [[thm:vi-c-2-1]] satisfies (C5), as there v_C = ½ and γ_C > 10⁶. Without
(C5) every statement below holds with ℓ_K^max = 2 + 2γ_Cv_C, which still serves every graft with
Re λ > 2 − 2γ_Cv_C + ε.

For ℓ_K < ℓ_K^max let 𝒲(ℓ_K) be the set of indicial roots μ of L̂_b(0) ([[prop:iii-f1-2-3]]) with
−ℓ_K < Re μ ≤ 0. All are real ([[lem:iii-g1-1-3]] (c)). For a root μ of type τ and degree l, let 𝒴_τ be the space of
harmonics of [[sec:iii-a1-1]] that parametrises that type: 𝒮_l for scalar, 𝒱_l for vector and 𝒯_l for tensor types.

**Definition {#def:iii-g2-table-1-1}** (The roots of 𝒲(ℓ_K), ℓ_K < 3, and their states; Table 1.1.) For each root μ in
the window we list its types; its origin in the factorisation [[eq:iii-f1-2-1]]; the state whose leading term spans
its indicial solutions ([[lem:iii-g2-1-2]]); the number m_0 of generalised companions constructed; and the number k_μ
used below.

(1) μ = 0, type s0: the gauge-invariant root −l of [[eq:iii-f1-2-1]] at l = 0; the time translation h^(0)_(b,s0) of
[[prop:iii-d3-3-1]] (1); m_0 = 3; k_μ = 2.

(2) μ = 0, type s2: the root −l + 1 of □^Υ at scalar type l = 2; [[prop:iii-d3-3-1]] (4)–(7); m_0 = 3; k_μ = 2.

(3) μ = −1, type s1: the boosts; h^(≤k)_(b,s1) of [[prop:iii-d2-3-1]] and [[prop:iii-d3-3-1]] (2); m_0 = 4; k_μ = 3,
with the indexing of the s1 chain below.

(4) μ = −1, type v1: the rotations; h^(≤k)_(b,v1) of [[prop:iii-d2-3-1]] and [[prop:iii-d3-3-1]] (3); m_0 = 3; k_μ = 2,
with the indexing of the v1 chain below.

(5) μ = −1, types s3 and v2: the roots −l + 1 (l = 3) and −l (l = 2) of □^Υ; [[prop:iii-d3-3-1]] (4)–(7); m_0 = 2
for each; k_μ = 1.

(6) μ = −2, types s4 and v3: the roots −l + 1 (l = 4) and −l (l = 3) of □^Υ; [[prop:iii-d3-3-1]] (4)–(7); m_0 = 1
for each; k_μ = 0.

(7) μ = −2, types s2, v2 and t2: the gauge-invariant root −l of [[eq:iii-f1-2-1]] at l = 2; the states h^(−2)_(b,τ) of
[[prop:iii-f4-5-1]]; m_0 = 0; k_μ = 0.

(8) μ = 2 − λ^Υ_(s0,2) ∈ [−z_Υ/3, 0), type s0: a class root; [[prop:iii-d3-3-1]] (4)–(7); m_0 = 2; k_μ = 2.

(9) μ = 2 − λ^Υ_(s1,2) ∈ (−¼, 0), type s1: a class root; [[prop:iii-d3-3-1]] (4)–(7); m_0 = 2; k_μ = 2.

(10) μ = 2 − λ^Υ_(s2,3) ∈ (−5/4, −1), type s2, and μ = 2 − λ^Υ_(s1,3) ∈ (−5/4, −1), type s1: class roots;
[[prop:iii-d3-3-1]] (4)–(7); m_0 = 2; k_μ = 1.

(11) μ = 2 − λ^Υ_(s2,4) and μ = 2 − λ^Υ_(s3,4), in (−9/4, −2), types s2 and s3: class roots; [[prop:iii-d3-3-1]]
(4)–(7); m_0 = 2; k_μ = 0.

A root μ of L̂_b(0) in the rows from □^Υ is the root μ − 1 of the list of □^Υ in [[prop:iii-d3-3-1]], and the state is
h^(μ)_b := δ*_(g_b)ω^(μ−1)_b, whose leading term δ̄*(0)ω̄ is of degree μ ([[prop:iii-d3-3-1]] (4)–(7)). Only the rows
with −μ < ℓ_K are used.

*Completeness of the list.* The roots of [[prop:iii-f1-2-3]] with real part in (−3, 0] are those listed and the
excluded ones. Excluded are the λ^C_(·,≪,·) − 1 (real part < −101); −2 − 2γ_Cv_C (below −ℓ_K^max); and −l, 2 − l,
1 − l and 2 − λ^Υ_(sl,l+j) with real part ≤ −3. With the ranges of [[lem:iii-d-4-1]],
λ^Υ_(sl,l+j) − 2 ∈ (l + j − 2, l + j − 7/4) is less than 3 only for l + j ≤ 4; and λ^Υ_(s0,2) − 2 ∈ (0, z_Υ/3].

**Lemma {#lem:iii-g2-1-2}** (The indicial solutions are the leading terms of the states.) For every μ ∈ 𝒲(ℓ_K) and
every type τ at which μ is a root, the kernel of the indicial family N_τ(L̄̂(0), μ) on the type-τ sections of degree l
is {h̄_τ(Y) : Y ∈ 𝒴_τ}. Here h̄_τ(Y) is the ρ^μ-leading term of the state of [[def:iii-g2-table-1-1]] (for s1 and v1 at
−1, of h̆²_(b,s1)(S) and h̆¹_(b,v1)(V)), and Y ↦ h̄_τ(Y) is injective.

*Proof.* On the type-τ sections given by a harmonic Y, the indicial family is a matrix polynomial in μ whose
determinant has μ as a simple zero (the hypothesis on z_Υ). So its kernel is one-dimensional for each Y in a basis of
𝒴_τ, and depends linearly on Y. The leading term h̄ = ρ^μφ(ω) of the state lies in the kernel. Indeed it satisfies
L̄̂(0)h̄ = 0: for the base of a chain this is the leading order of [[eq:iii-g2-2-1]] at m = 0, since
L̂_b(0) − L̄̂(0) ∈ ρ⁴Diff²_b ([[lem:iii-f-2-1]] (3)); for s1 and v1 it is [[eq:iii-g2-2-4]] at the first index of the
chain. As 2L̄̂(0) = ρ²L̃(0)(ω, ρ∂_ρ, ∂_ω) ([[eq:iii-g-1-1]]) is dilation invariant, this is N(L̄̂(0), μ)φ = 0. The
leading term is non-zero for Y ≠ 0: for the roots from □^Υ by (R5) of [[sec:iii-d3-1]], as N(δ̄*(0), μ − 1) is
injective on these types at μ − 1 ∉ {0, −1}, or (at s0 and s2 with μ = 0) by [[lem:iii-f1-2-5]]; for the boosts and
rotations by [[prop:iii-d3-3-1]] (2)–(3); and for the physical states by [[prop:iii-f4-5-1]], whose leading terms span
the kernel. ∎

In particular, within the window the leading terms of the states of [[prop:iii-d3-3-1]] span the kernels of the
indicial families of L̄̂(0).

### Formal solutions {#sec:iii-g2-2}

#### Towers {#sec:iii-g2-2-1}

Let L be a stationary operator of order at most 2 in ∂_(t_*). For stationary h and functions a of t_*,
L(a(t_*)h) = aL̂(0)h + a′[L, t_*]h + ½a″[[L, t_*], t_*]h: with L = L_0 + L_1∂_(t_*) + L_2∂_(t_*)², L_j stationary,
[L, t_*]h = L_1h and [[L, t_*], t_*] = 2L_2.

**Lemma {#lem:iii-g2-2-1}** (Towers.) (a) For stationary h̆⁰, …, h̆^(m_0), the following are equivalent:
L(Σ_(i=0)^k (k!/(k − i)!)t_*^(k−i)h̆^i) = 0 for k = 0, …, m_0; and

    L̂(0)h̆^m + [L, t_*]h̆^(m−1) + ½[[L, t_*], t_*]h̆^(m−2) = 0,   m = 0, …, m_0                         {#eq:iii-g2-2-1}

(with h̆^(−1) = h̆^(−2) = 0). (b) If [[eq:iii-g2-2-1]] holds, then for k ≤ m_0 and every smooth a,

    L(Σ_(j=0)^k a^(j)(t_*)h̆^j) = a^(k+1)([L, t_*]h̆^k + ½[[L, t_*], t_*]h̆^(k−1)) + ½a^(k+2)[[L, t_*], t_*]h̆^k.
                                                                                                         {#eq:iii-g2-2-2}

*Proof.* (b) Expanding by the rule for L(ah), the coefficient of a^(m) is the left side of [[eq:iii-g2-2-1]] for m ≤ k;
for m = k + 1, k + 2 it is what remains. (a) With a = t_*^k/k!, [[eq:iii-g2-2-2]] shows that [[eq:iii-g2-2-1]] implies
the polynomial identities. Conversely, by induction on k: the identity for k minus t_* times k times the one for k − 1
leaves the t_*⁰-coefficient, which is k! times the left side of [[eq:iii-g2-2-1]] at m = k, plus terms that vanish by
[[eq:iii-g2-2-1]] at smaller m. ∎

For L = L_b, [[lem:iii-f-2-1]] (3) gives near infinity

    [L_b, t_*] = −ρ(ρ∂_ρ − 3/2 − S̄) − g_b^(00)∂_(t_*) + ½Q_b,   [[L_b, t_*], t_*] = −g_b^(00) ∈ ρ²C^∞,  {#eq:iii-g2-2-3}

and for L̄ ([[eq:iii-g-1-1]], which has no ∂_(t_*)² term), [L̄, t_*] = −ρ(ρ∂_ρ − 3/2 − S̄) and [[L̄, t_*], t_*] = 0.
Indeed by [[eq:iii-f-2-3]], L_b = L̄ − ½g_b^(00)∂_(t_*)² + ½Q_b∂_(t_*) + ½R_b, and [∂_(t_*)², t_*] = 2∂_(t_*).

The states of [[def:iii-g2-table-1-1]] satisfy [[eq:iii-g2-2-1]] for L = L_b. [[prop:iii-d3-3-1]] gives
ω^(≤k) ∈ ker □^Υ_b as polynomials in t_*, so δ*_(g_b)ω^(≤k) ∈ ker D_(g_b)Ric ∩ ker δ_(g_b,E_Υ)G_(g_b) ⊂ ker L_b; here
D_(g_b)Ric(ℒ_Xg_b) = ℒ_XRic(g_b) = 0 and 2δ_(g_b,E_Υ)G_(g_b)δ*_(g_b) = □^Υ_b. The physical states lie in ker L̂_b(0)
(m_0 = 0).

#### The Minkowski formal solutions {#sec:iii-g2-2-2}

This is [Hin26, Definition 9.8] in dimension 4 + 1. Let (h̆^i_b)_(i≤m_0) be a tower of [[def:iii-g2-table-1-1]] for
L_b, with h̆^i_b ∈ 𝒜^((μ−i,0) ∪ (μ−i+ℰ_ind)), min Re ℰ_ind > 0, and with ρ^(μ−i)-leading terms h̄̆^i, homogeneous of
degree μ − i. For s1 and v1 the indexing of [Hin26] is used. The s1 tower is h_(b,s1) ∈ 𝒜^((3,0)∪…),
h̆¹_(b,s1) ∈ 𝒜^((2,0)∪…), then h̆^k_(b,s1) ∈ 𝒜^((−k+1,0)∪…) for k ≥ 2, and its homogeneous part starts at
h̄̆²_s1 =: h̄²_s1, of degree −1. The v1 tower is h_(b,v1) ∈ 𝒜^((3,0)∪…), then h̆^k_(b,v1) ∈ 𝒜^((−k,0)∪…) for k ≥ 1,
starting at h̄¹_v1, of degree −1 ([[eq:iii-d2-3-4]], [[prop:iii-d3-3-1]] (2)–(3)).

**Lemma {#lem:iii-g2-2-2}** (The Minkowski towers.) The leading terms satisfy [[eq:iii-g2-2-1]] for L̄:

    L̄̂(0)h̄̆^m + [L̄, t_*]h̄̆^(m−1) = 0,                                                                {#eq:iii-g2-2-4}

for the s1 chain from m = 2 and for the v1 chain from m = 1 (the earlier terms being omitted).

*Proof.* Under the dilations (t_*, x) ↦ (st_*, sx), t_*^(k−i)h̆^i has leading degree k − μ for every i (for s1,
k − 1 for i ≥ 2 and k − 3 for i = 0, 1; for v1, k for i ≥ 1 and k − 3 for i = 0). L̄ is homogeneous of degree −2.
L_b − L̄ = −½g_b^(00)∂_(t_*)² + ½Q_b∂_(t_*) + ½R_b ([[eq:iii-f-2-3]]) lowers the degree by at least 2, and the
corrections h̆^i_b − χh̄̆^i lower it by min Re ℰ_ind > 0. So the top-degree part of
L_b(Σ (k!/(k − i)!)t_*^(k−i)h̆^i_b) = 0 is L̄(Σ (k!/(k − i)!)t_*^(k−i)h̄̆^i) = 0, over the indices of top degree.
[[lem:iii-g2-2-1]] (a) for L̄, with [[L̄, t_*], t_*] = 0, gives [[eq:iii-g2-2-4]]. ∎

**Definition {#def:iii-g2-2-3}** ([Hin26, Definition 9.8] in dimension 4 + 1.) For a function a = a(t_*) (valued in 𝒴_τ
where the state is linear in Y) and k ≤ m_0,

    h̄^((μ),≤k)(a) := Σ_(j=0)^k a^(j)(t_*)h̄̆^((μ),j),   h̄^(≤k)_s1(a) := Σ_(j=2)^k h̄̆^j_s1(a^(j−2)),
    h̄^(≤k)_v1(a) := Σ_(j=1)^k h̄̆^j_v1(a^(j−1)).                                                        {#eq:iii-g2-2-5}

**Lemma {#lem:iii-g2-2-4}** ([Hin26, (9.28)–(9.31)] in dimension 4 + 1.) (a)
L̄h̄^((μ),≤k)(a) = a^(k+1)[L̄, t_*]h̄̆^((μ),k), and likewise for s1 (with a^(k−1) and h̄̆^k_s1) and for v1 (with a^(k)
and h̄̆^k_v1).

(b) For a = t_*^(−λ+μ) (for s1 and for v1, a = t_*^(−λ−1)), the tensor t_*^λh̄^((μ),≤k)(a) is independent of t_* in
the coordinates (t_*, R, ω), R = (ρt_*)⁻¹. It is a finite sum Σ_j c_jR^(−μ+j)φ_j(ω), without logarithms. Moreover

    t_*^λt_*²L̄(h̄^((μ),≤k)(t_*^(−λ+μ))) ∈ R^(−μ+k−1)C^∞([0, 1)_R × 𝕊³)                                  {#eq:iii-g2-2-6}

is independent of t_*. The same holds for s1 with R^(k−2), and for v1 with R^(k−1), in place of R^(−μ+k−1).

*Proof.* (a) is [[eq:iii-g2-2-2]] for L̄, with [[L̄, t_*], t_*] = 0, by [[lem:iii-g2-2-2]]. (b) a^(j) = c_jt_*^(−λ+μ−j)
and h̄̆^j = ρ^(μ−j)φ_j(ω), so t_*^λa^(j)h̄̆^j = c_j(ρt_*)^(μ−j)φ_j = c_jR^(−μ+j)φ_j. By (a) and
[L̄, t_*] = −ρ(ρ∂_ρ − 3/2 − S̄), the left side of [[eq:iii-g2-2-6]] is
t_*^(λ+2)c_(k+1)t_*^(−λ+μ−k−1)ρ^(1+μ−k)ψ(ω) = c_(k+1)(ρt_*)^(1+μ−k)ψ = c_(k+1)R^(k−1−μ)ψ. For s1,
a^(k−1) = ct_*^(−λ−k) and h̄̆^k_s1 has degree 1 − k, which gives R^(k−2); for v1, a^(k) = ct_*^(−λ−1−k) and degree −k
give R^(k−1). ∎

#### The Myers–Perry formal solutions {#sec:iii-g2-2-3}

This is [Hin26, Definition 9.10] in dimension 4 + 1.

**Definition {#def:iii-g2-2-5}** With the towers of [[def:iii-g2-table-1-1]] for L_b,

    h^((μ),≤k)_b(a) := Σ_(j=0)^k a^(j)(t_*)h̆^((μ),j)_b,
    h^(≤k)_(b,s1)(a) := h_(b,s1)(a) + Σ_(j=1)^k h̆^j_(b,s1)(a^(j)),
    h^(≤k)_(b,v1)(a) := h_(b,v1)(a) + Σ_(j=1)^k h̆^j_(b,v1)(a^(j)).
                                                                                                      {#eq:iii-g2-2-7}

**Lemma {#lem:iii-g2-2-6}** ([Hin26, (9.37)] in dimension 4 + 1.) L_bh^((μ),≤k)_b(a) is given by [[eq:iii-g2-2-2]] with
h̆^j = h̆^((μ),j)_b, and likewise for s1 and v1. For a = t_*^(−λ+μ) it is, near K⁺ (at bounded r),
O(t_*^(−λ+μ−k−1)) with all stationary derivatives, that is of K⁺-order λ − μ + k + 1. For s1 with a = a_s1 of
[[eq:iii-g2-4-2]] the order is λ + k, and for v1 with a = a_v1 it is λ + k + 1. With k = k_μ of
[[def:iii-g2-table-1-1]], every one of these orders is at least λ + 3.

*Proof.* [[eq:iii-g2-2-2]] and the tower property ([[sec:iii-g2-2-1]]). The coefficients [L_b, t_*]h̆^k_b and
[[L_b, t_*], t_*]h̆^(k−1)_b are stationary and smooth; a^(k+1) ∼ t_*^(−λ+μ−k−1), and for s1
a_s1^(k+1) ∼ t_*^(−λ−k), for v1 a_v1^(k+1) ∼ t_*^(−λ−k−1). The bound λ − μ + k_μ + 1 ≥ λ + 3 is k_μ ≥ 2 + μ, which the
k_μ of [[def:iii-g2-table-1-1]] satisfy: k_μ = 2 + μ at the integer roots; at the class roots
μ ∈ (−¼, 0), (−5/4, −1), (−9/4, −2), k_μ = 2, 1, 0; for s1, k = 3 gives λ + 3; for v1, k = 2 gives λ + 3. ∎

### The expansion at K⁺ {#sec:iii-g2-3}

**Theorem {#thm:iii-g2-3-1}** ([Hin26, Proposition 9.9] in dimension 4 + 1.) Let λ ∈ ℂ, k ∈ ℕ_0, ℓ_K < ℓ_K^max with
ℓ_K ≠ −Re μ for every root μ, and α ∈ (−1, 0). Suppose N_ι⁺(λ)u = f on [0, 1)_R × 𝕊³, with f ∈ H^(k,ℓ_K−2)_b and
u ∈ H^(k+2,α)_b (for the b-density |dR/R dg̸|). Then u = u_0 + ũ, ũ ∈ H^(k+2,ℓ_K)_b, with

    u_0 = Σ_(μ∈𝒲(ℓ_K)) Σ_τ t_*^λ h̄^((μ),≤k_μ)_τ(t_*^(−λ+μ)Y^((μ))_τ),                                   {#eq:iii-g2-3-1}

for suitable Y^((μ))_τ ∈ 𝒴_τ. The sum runs over the types of [[def:iii-g2-table-1-1]] at which μ is a root. At μ = −1
the s1 and v1 terms are t_*^λh̄^(≤3)_s1(t_*^(−λ−1)S^((−1))_1) and t_*^λh̄^(≤2)_v1(t_*^(−λ−1)V^((−1))_1). Each term is a
t_*-independent function of (R, ω) ([[lem:iii-g2-2-4]] (b)) and is free of logarithms. The coefficients Y^((μ))_τ are
continuous linear functionals of (u, f) in these spaces.

*Proof.* [[eq:iii-g2-3-1]] is [Hin26, (9.32)] at n = 4, with the window 𝒲(ℓ_K) and the orders k_μ of
[[def:iii-g2-table-1-1]]. By [[eq:iii-g1-1-3]], R²N_ι⁺(λ) = A_0 + RA_1 with A_0 = L̃(0)(ω, −R∂_R, ∂_ω) b-elliptic. So

    A_0u = R²f − RA_1u.                                                                                {#eq:iii-g2-3-2}

By [[lem:iii-a-1-4]] (its proof at finite order, as in Step 5 (iv) of the proof of [[thm:iii-g1-3-1]]),
u ∈ H^(k+2,(ℰ,ℓ_K))_b with ℰ generated by Spec_b(A_0) above α. So u is a finite sum of terms R^z(log R)^jc_(z,j)(ω),
Re z < ℓ_K, plus an element of H^(k+2,ℓ_K)_b. We remove the terms in order of increasing real part.

*The lowest term.* Suppose some coefficient is non-zero, and let z_0 be the least real part of an exponent present. In
[[eq:iii-g2-3-2]] the right side has exponents of real part ≥ min(ℓ_K, z_0 + 1) > z_0. So the terms of A_0u at real part
z_0 vanish: for each z with Re z = z_0 and J the top power of log R, N(A_0, z)c_(z,J) = 0 and
N(A_0, z)c_(z,J−1) + J∂_zN(A_0, z)c_(z,J) = 0. Hence z = −μ for a root μ, which is real, so z = z_0. As μ is a simple
root, ∂_zN(A_0, z) maps ker N(A_0, z) injectively into a complement of the range of N(A_0, z). So Jc_(z,J) = 0, J = 0,
and c := c_(z,0) ∈ ker N(A_0, −μ) = ker N(L̄̂(0), μ). The kernel is finite-dimensional (A_0 is elliptic on 𝕊³) and
splits by type and harmonic. By [[lem:iii-g2-1-2]], c = Σ_τ h̄_τ(Y_τ) with unique Y_τ ∈ 𝒴_τ, and μ ∈ 𝒲(ℓ_K) as z_0 < ℓ_K.

*Subtraction.* Let w := Σ_τ t_*^λh̄^((μ),≤k_μ)_τ(t_*^(−λ+μ)Y_τ), a function of (R, ω) ([[lem:iii-g2-2-4]] (b)). Its
R^(−μ)-coefficient is c, since t_*^λa h̄̆⁰ = R^(−μ)h̄_τ(Y); for s1 and v1 the lowest terms are R¹h̄²_s1(S) and
R¹h̄¹_v1(V). Its other terms have exponents −μ + j, j ≥ 1. On t_*-independent functions w = w(R, ω),
2L̄(t_*^(−λ)w) = t_*^(−λ−2)N_ι⁺(λ)w ([[eq:iii-g-1-6]], [[def:iii-g-1-1]]: t_*^(−λ)w = ρ^λ(R^λw)). By
[[eq:iii-g2-2-6]],

    N_ι⁺(λ)w ∈ R^(−μ+k_μ−1)C^∞ ⊂ H^(∞,ℓ_K−2)_b     near R = 0,

as −μ + k_μ − 1 ≥ 1 > ℓ_K − 2 ([[lem:iii-g2-2-6]]); the same holds for s1 and v1, with R¹. So u′ := u − w satisfies the
hypotheses with f′ := f − N_ι⁺(λ)w, and has no term R^(−μ) of the types removed. Doing this for every type and root at
real part z_0, the least real part of an exponent of u′ exceeds z_0. By the first step, every new least exponent is −μ′
for a root μ′ with −μ′ ∈ (z_0, ℓ_K). There are finitely many such roots, so after finitely many steps no term remains,
and ũ := u − u_0 ∈ H^(k+2,ℓ_K)_b. Each Y_τ is read off from the coefficient c, which is a continuous functional of
(u, f) (the circle integrals of [[lem:iii-a-1-5]]), and the subtractions are continuous. ∎

**Corollary {#cor:iii-g2-3-2}** (The index set at K⁺.) In [[thm:iii-g1-3-1]], below the order ℓ_K^max, the expansion of
h at R = 0 has no logarithms. Its exponents are −μ + j (μ ∈ 𝒲(ℓ_K), 0 ≤ j ≤ k_μ, with the conventions for s1 and v1).
So h ∈ 𝒜^((⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),(ℰ^♭_K,ℓ_K)) for every ℓ_K < ℓ_K^max, with

    ℰ^♭_K := ⋃_(μ∈𝒲(ℓ_K^max)) ⋃_(j≤k_μ) (−μ + j, 0).

This is the counterpart at n = 4 of the index set ℰ_K of [Hin26].

*Proof.* [[thm:iii-g2-3-1]] with f = R² times a function vanishing to infinite order, and u = h near R = 0. ∎

### Grafting {#sec:iii-g2-4}

This section is [Hin26, Proposition 9.11 and Corollary 9.12] in dimension 4 + 1. Let M be the compactified spacetime
of [[sec:iii-b-2]] ([Hin26, (3.3)]), with its faces 𝓘⁺, ι⁺ and K⁺, and Ω_* := cl_M{t_* ≥ 1} ([Hin26, (9.38)]); the
b-spaces on Ω_* carry three orders, listed for 𝓘⁺, ι⁺ and K⁺ ([Hin26, Definitions 2.6–2.8]). Let χ_K ∈ C^∞(M) equal 1
near K⁺ and 0 near t_*⁻¹(1) ∪ 𝓘⁺, and be a function of R alone near ι⁺. Let χ_ι := χ(t_*), with χ ∈ C^∞(ℝ) equal to 0
on (−∞, 1] and 1 on [2, ∞); it equals 1 near ι⁺ and is supported in Ω_*.

**Lemma {#lem:iii-g2-4-1}** (2L̄ is the ι⁺-normal operator of 2L_b.) For w = w(R, ω) conormal on ι⁺ near {R > 0}
(equivalently w(v, ω), v = R⁻¹), on {|x| > 3R_1},

    2L_b(t_*^(−λ)w) = t_*^(−λ−2)N_ι⁺(λ)w + t_*^(−λ−4)v²Bw,                                               {#eq:iii-g2-4-1}

with B = B_0 + vB_1 + v²B_2, each B_i a second-order b-operator in (v∂_v, ∂_ω) whose coefficients are smooth functions
of (ρ, ω) = (v/t_*, ω); B_1 and B_2 come from Q_b and R_b.

*Proof.* 2L̄(t_*^(−λ)w) = t_*^(−λ−2)N_ι⁺(λ)w is the definition of N_ι⁺ ([[eq:iii-g1-1-1]]; [[lem:iii-g-1-2]] (c),
P_0 = 2L_b). For the rest use [[eq:iii-f-2-3]], stated for 2L_b, with
∂_(t_*)(t_*^(−λ)w(ρt_*)) = t_*^(−λ−1)(v∂_v − λ)w and ρ∂_ρ = v∂_v at fixed t_*. The term g_b^(00)∂_(t_*)² gives
ρ²t_*^(−λ−2)(…)w = t_*^(−λ−4)v²(…)w. The term Q_b∂_(t_*) gives ρ³t_*^(−λ−1)(…), and R_b gives ρ⁴(…); both are
t_*^(−λ−4)v² times v or v². ∎

**Theorem {#thm:iii-g2-4-2}** ([Hin26, Proposition 9.11] in dimension 4 + 1.) Let λ ∉ spec_ι⁺(L̄) with Re λ > 0. Let
ℓ_K < ℓ_K^max, with ℓ_K ≠ −Re μ for all roots and ℓ_K ∉ Re π_1ℰ_K. Let ℓ_I < 3/2 + s_C with
ℓ_I ∉ Re π_1ℰ^tot_(ι⁺,𝓘), and Re λ < ℓ_I. Let f_+ ∈ H^(∞,ℓ_I+1,ℓ_K−2)_b(ι⁺; S²T*) and u_+ := N_ι⁺(λ)⁻¹(2f_+)
([[thm:iii-g1-3-1]] (2), extended holomorphically to λ ∉ spec_ι⁺(L̄)). Write u_+ = χ_K|_ι⁺u_0 + ũ by
[[thm:iii-g2-3-1]], with ũ ∈ H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),ℓ_K)_b(ι⁺). Define

    a_s1(t_*) := t_*^(−λ+1)/(λ(λ − 1)) if λ ≠ 1,   a_s1(t_*) := −log t_* if λ = 1,   a_v1(t_*) := −t_*^(−λ)/λ,
                                                                                                         {#eq:iii-g2-4-2}

and let u_(b,0) be [[eq:iii-g2-3-1]] with every Minkowski formal solution replaced by its Myers–Perry version
([[def:iii-g2-2-5]]), at the same orders, and with the s1 and v1 terms h^(≤3)_(b,s1)(a_s1S^((−1))_1) and
h^(≤2)_(b,v1)(a_v1V^((−1))_1):

    u_(b,0) := h^(≤3)_(b,s1)(a_s1S^((−1))_1) + h^(≤2)_(b,v1)(a_v1V^((−1))_1)
               + Σ′_(μ,τ) h^((μ),≤k_μ)_(b,τ)(t_*^(−λ+μ)Y^((μ))_τ),
                                                                                                      {#eq:iii-g2-4-3}

the primed sum running over the other rows. Let u := χ_Ku_(b,0) + χ_ιt_*^(−λ)ũ. Then

    χ_ιt_*^(−λ−2)f_+ − L_bu ∈ H^(∞,(ℰ^tot_(ι⁺,𝓘)+2, ℓ_I+1), λ+2+ℰ_ind, λ+ℓ_K)_b(Ω_*; S²T*)^(•,−)         {#eq:iii-g2-4-4}

for an index set ℰ_ind with min Re ℰ_ind > 0, depending only on L̄ and on whether λ = 1. Moreover
(t_*^λu)|_ι⁺ = u_+, and

    u ∈ H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I), (λ,0)∪(λ+ℰ_ind), (ℰ^gr_K(λ),ℓ_K))_b(Ω_*)^(•,−),

where ℰ^gr_K(λ) contains the index sets of a_s1 and a_v1 and (κ, 0) for every exponent κ of t_*⁻¹ in
[[eq:iii-g2-4-3]].

*Proof.* *The restriction.* At (ι⁺)°, ρ ∼ t_*⁻¹. The leading term at ρ = 0 of each Myers–Perry tensor is the Minkowski
one. So t_*^λh^((μ),≤k)_b(t_*^(−λ+μ)Y) → t_*^λh̄^((μ),≤k)(t_*^(−λ+μ)Y) at ι⁺, and the corrections are
O(t_*^(−min Re ℰ_ind)) there. In the s1 and v1 terms, h_(b,s1)(a_s1S), h̆¹_(b,s1)(a′_s1S) and h_(b,v1)(a_v1V) are of
size ρ³t_*^(−λ+1) (or ρ³log t_*), ρ²t_*^(−λ) and ρ³t_*^(−λ) ([[eq:iii-d2-3-4]]); these are O(t_*^(−λ−2)) at (ι⁺)°.
The next terms reproduce the Minkowski ones: the coefficient of h̆²_(b,s1) is a″_s1S = t_*^(−λ−1)S, and that of
h̆¹_(b,v1) is a′_v1V = t_*^(−λ−1)V, as in [[thm:iii-g2-3-1]]. With χ_K|_ι⁺ and χ_ι = 1 near ι⁺,
(t_*^λu)|_ι⁺ = χ_Ku_0 + ũ = u_+.

*Away from K⁺.* Near ι⁺, u = t_*^(−λ)u_+ up to terms supported near K⁺. [[lem:iii-g2-4-1]] gives
t_*^(−λ−2)f_+ − L_b(t_*^(−λ)u_+) = −½t_*^(−λ−4)v²Bu_+, as N_ι⁺(λ)u_+ = 2f_+. As u_+ ∈ 𝒜^((⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I)) at v = 0
([[thm:iii-g1-3-1]]), v²Bu_+ has 𝓘⁺-index set in ℰ^tot_(ι⁺,𝓘) + 2 to order ℓ_I + 2. Its ι⁺-orders are λ + 4 + ℕ_0,
from the Taylor expansion of the coefficients in ρ = v/t_*. The commutator
[L_b, χ_ι] = χ′(t_*)[L_b, t_*] + ½χ″(t_*)[[L_b, t_*], t_*] is supported in {1 ≤ t_* ≤ 2}. By [[eq:iii-g2-2-3]], at
fixed t_* (where ρ = v/t_* and ρ∂_ρ = v∂_v), its main part on t_*^(−λ)ũ is −χ′t_*^(−λ−1)v(v∂_v − 3/2 − S̄)ũ. Near 𝓘⁺,
ũ = u_+, and (v∂_v − 3/2 − S̄)u_+ ∈ H^(∞,(ℰ^C_(ι⁺,𝓘),ℓ_I))_b by [[thm:iii-g1-3-1]] (2). So this part has 𝓘⁺-index set
ℰ^C_(ι⁺,𝓘) + 1 = ℰ^tot_(ι⁺,𝓘) + 2 to order ℓ_I + 1, which is the order [[eq:iii-g2-4-4]] asks. The other parts carry
ρ² = v²t_*⁻² or ρ³ and give ℰ^tot_(ι⁺,𝓘) + 2 as well.

*Near K⁺.* Each term of [[eq:iii-g2-4-4]] has K⁺-order at least λ + ℓ_K: χ_ιt_*^(−λ−2)f_+, as f_+ has weight ℓ_K − 2
at R = 0 and t_*^(−λ−2)R^(ℓ_K−2) = t_*^(−λ−ℓ_K)r^(ℓ_K−2); L_b(χ_ιt_*^(−λ)ũ), as ũ has weight ℓ_K, L_b is stationary,
and ∂_(t_*) only adds decay; [L_b, χ_K]u_(b,0), which is supported away from K⁺; and L_bu_(b,0) on supp χ_K, as by
[[lem:iii-g2-2-6]] each term has K⁺-order at least λ + 3 > λ + ℓ_K.

*The ι⁺-order of the remainder near K⁺ ∩ ι⁺.* t_*^(λ+2)L_bu restricted to ι⁺ is ½N_ι⁺(λ)u_+ = f_+, by
[[lem:iii-g2-4-1]] and (t_*^λu)|_ι⁺ = u_+. The Myers–Perry corrections in u_(b,0) and the terms of [[lem:iii-g2-4-1]]
contribute at ι⁺-orders in λ + 2 + ℰ_ind, with ℰ_ind collecting the index sets of the states of [[ch:s13]] and
[[ch:s15]], 2 + ℕ_0, and (2, 1) when λ = 1: the term h_(b,s1)(−log t_* S) has size ρ³log t_* = v³t_*⁻³log t_*. No
t_*-dependence of χ_K enters, as χ_K is a function of R near ι⁺. So the ι⁺-index set of the remainder is
λ + 2 + ℰ_ind. The membership of u follows term by term: t_*^(−λ)ũ, and [[eq:iii-g2-4-3]], whose t_*-exponents are
those collected in ℰ^gr_K(λ). ∎

As in [Hin26], a right side of size O(t_*^(−λ−2)) can set the black hole in motion. The s1 term is a centre-of-mass
motion
of size O(t_*^(−λ+1)), or O(log t_*) at λ = 1; at n = 4 there are four directions. In the v1 term, the summand
h_(b,v1)(a_v1V) is invisible at ι⁺ and is non-zero only for A ≠ 0 ([[prop:iii-d2-3-1]] (3)), an O(|A|) change of the
rotation in 𝔰𝔬(4); the summand h̆¹_(b,v1)(a′_v1V) is visible there and reproduces h̄¹_v1. At n = 4 the boost and
rotation states decay one order faster than in dimension 3 + 1 (ρ³, ρ², ρ³ against ρ², ρ, ρ; [[eq:iii-d2-3-4]]), so
their invisibility at ι⁺ holds with room.

**Remark {#rem:iii-g2-4-maps}** (The graft as a holomorphic family.) For fixed ε > 0 and λ near λ_0 ≠ 1 with
λ ∉ spec_ι⁺(L̄) (a_s1 has a pole at λ = 1), [[thm:iii-g2-4-2]] defines Φ_(ι,b)(λ)f_+ := u and
F_(ι,b)(λ)f_+ := χ_ιt_*^(−λ−2)f_+ − L_bΦ_(ι,b)(λ)f_+ on H^(∞,ℓ_I+1,ℓ_K−2)_b(ι⁺). These are holomorphic in λ, with
values in H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),λ_0−ε,λ_0−1−ε)_b(Ω_*)^(•,−) and in
H^(∞,(ℰ^tot_(ι⁺,𝓘)+2,ℓ_I+1),λ_0+2+min Re ℰ_ind−ε,λ_0+ℓ_K−ε)_b(Ω_*)^(•,−) respectively ([Hin26, (9.42a)–(9.42b)]).
Holomorphy holds because f_+ ↦ u_+ is holomorphic ([[thm:iii-g1-3-1]] (2)), the coefficients Y^((μ))_τ are continuous
functionals of u_+ ([[thm:iii-g2-3-1]]), t_*^(−λ), a_s1 and a_v1 are holomorphic in λ with values in these weighted
spaces, and the states do not depend on λ.

**Corollary {#cor:iii-g2-4-3}** ([Hin26, Corollary 9.12] in dimension 4 + 1.) Let Re λ_0 > 1, and let l_0 be the order
of the pole of N_ι⁺(L̄, ·)⁻¹ at λ_0 (l_0 = 0 if λ_0 ∉ spec_ι⁺(L̄)). Let ℓ_K and ℓ_I be as in [[thm:iii-g2-4-2]], with
Re λ_0 < ℓ_I. Let k ∈ ℕ_0 and

    f = Σ_(j≤k) χ_ιt_*^(−λ_0−2)(log t_*)^jf^((j))_+ + f′,

with f^((j))_+ ∈ ⋂_ε H^(∞,ℓ_I+1,ℓ_K−2−ε)_b(ι⁺) and f′ ∈ ⋂_ε H^(∞,ℓ_I+1,∞,λ_0+ℓ_K−ε)_b(Ω_*; S²T*)^(•,−). Then there
are u^((j))_(b,0) of the form [[eq:iii-g2-4-3]], with λ_0 for λ and a factor (log t_*)^j in each argument, and
ũ^((j)) ∈ ⋂_ε H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I),ℓ_K−ε)_b(ι⁺), j = 0, …, k + l_0, such that
u := Σ_j χ_Ku^((j))_(b,0) + χ_ιt_*^(−λ_0)(log t_*)^jũ^((j)) satisfies

    f − L_bu ∈ ⋂_(ε>0) H^(∞,(ℰ^tot_(ι⁺,𝓘)+2,ℓ_I+1), λ_0+2+ℰ_ind+(0,k+l_0), λ_0+ℓ_K−ε)_b(Ω_*; S²T*)^(•,−),
                                                                                                         {#eq:iii-g2-4-5}

and u ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_(ι⁺,𝓘)⟩,ℓ_I), (λ_0,k+l_0)∪(λ_0+ℰ_ind+(0,k+l_0)), (ℰ^gr_K(λ_0)+(0,k+l_0),ℓ_K−ε))_b(Ω_*)^(•,−)
([Hin26, (9.43)]).

*Proof.* As in [Hin26]. The quasi-homogeneous part is
f − f′ = (2πi)⁻¹∮ Σ_j (−1)^j j! (λ − λ_0)^(−j−1)χ_ιt_*^(−λ−2)f^((j))_+ dλ, over a small circle around λ_0 on which
λ ∉ spec_ι⁺(L̄). Put u := (2πi)⁻¹∮ Σ_j (−1)^j j! (λ − λ_0)^(−j−1)Φ_(ι,b)(λ)f^((j))_+ dλ ([[rem:iii-g2-4-maps]]). Then
f − L_bu is f′ plus the same integral of F_(ι,b)(λ)f^((j))_+, of the stated orders by the holomorphy of
[[rem:iii-g2-4-maps]]. Expanding in t_* gives the polyhomogeneity: the power of log t_* is at most the order of the pole
of the integrand at λ_0 minus 1, that is k + l_0. ∎

### Remarks on the comparison with [Hin26] {#sec:s16-remarks}

The following points concern [Hin26, Section 9.1] itself and are recorded for a reader comparing the two texts.
[Hin26, Proposition 9.11] does not state the hypothesis Re λ < ℓ_I, which its use of [Hin26, Proposition 9.4 (2)]
(finite decay at 𝓘⁺) needs; [Hin26, Corollary 9.12] states it, and [[thm:iii-g2-4-2]] assumes it. The statement of
[Hin26, (9.17)], (v∂_v − 1 − S̄)h ∈ 𝒜^(ℰ^tot+1) without an order, holds in dimension 4 + 1 up to the order
5/2 + s_C of [[eq:iii-g1-3-2]]; beyond it the large eigenvalues of S̄ enter through the coupling by L̃(0), as they do in
h beyond ℓ_I. The hypothesis of [Hin26, Corollary 9.12] also allows terms t_*^(−λ_0−2−j), j ≥ 1, which its proof does
not remove; the hypothesis of [[cor:iii-g2-4-3]] excludes them. In the proof of [[thm:iii-g2-4-2]], the step of [Hin26]
that bounds L_b − N_ι⁺(L_b) through the class of L_b and [Hin26, (9.17)] is replaced by the exact identity
[[eq:iii-g2-4-1]], and [Hin26, (9.17)] enters only through the commutator with χ_ι, to the finite order of
[[eq:iii-g1-3-2]]. In [[thm:iii-g2-3-1]] the ordering of the iteration in [Hin26] (the roots at s0 and s2 first) is
replaced by an induction on the least exponent present, which also shows that the expansion is free of logarithms
below ℓ_K^max. Finally, the expansion of the inverse of the ι⁺-normal operator at v^λ is controlled through the Mellin
recursion [[eq:iii-g1-3-6]], which gives the joint meromorphy in (λ, κ) used tacitly in [Hin26, (9.23)–(9.24)] and,
with [[eq:iii-g1-3-8]], excludes logarithms of every order at v^λ.
