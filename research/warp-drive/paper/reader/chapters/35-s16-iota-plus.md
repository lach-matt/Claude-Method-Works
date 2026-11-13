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

The method differs from [Hin26] in four places. For fixed λ, the estimates of [Vas13], [Hin25a] and [HV15] used there
are replaced by those of [[ch:s01]] and [[ch:s03]], whose proofs use only properties that are verified for N_sf(λ)
here: it is the spectral family, in the dilation-invariant time T = log |x|, of a stationary operator whose principal
symbol is the dual of the metric |x|⁻²ḡ ([[lem:iii-g-1-2]] (g)); its light cone {v = 0} is a Killing horizon of ∂_T,
at whose conormal bundle the radial estimate runs with an explicit threshold ([[lem:iii-g-2-2]]); v is a time function
on {−2 < v < 0} ([[lem:iii-g-2-3]]); and v = ∞ is a b-elliptic end. The b-regularity at the light cone ([HV15,
Theorem 6.3] in [Hin26]) is proved by commuting with the dilation and with the Lie derivatives along the rotations
([[prop:iii-g-2-7]]). Injectivity is the argument of [[lem:ii-f-5-8]], with the tf-admissibility of
[[prop:iii-f1-3-3]]. The index is 0 because the family is invertible for |Im λ| large in every vertical strip, by a
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

**Remark {#rem:iii-g-1-scalar}** (The scalar wave operator.) Let □ = ∂_t² − Δ_(ℝ⁴) on ℝ^(1+4), and write it in (t_*, r, ω),
t_* = t − r, r = |x|. Then ∂_t = ∂_(t_*) and ∂_r|_t = ∂_r|_(t_*) − ∂_(t_*), so

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
principal symbol is |x|²ḡ⁻¹ = ĝ⁻¹ by [[lem:iii-f-2-1]] (1). The operator □_ĝ Id is T-independent with the same
principal symbol, so P_c − □_ĝ Id is of first order with T-independent coefficients. Finally
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

So ∂ℛ_± is a source for 𝖧 in the sense of [[sec:i-a-4-1]] (the conclusion of [[lem:i-a-4-1]] holds with q̃).

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
is a differential operator with principal symbol G_0 Id, G_0 real; that ∂ℛ is a source of 𝖧 with 𝖧ρ_∞ = β_0ρ_∞,
β_0 > 0; a quadratic defining function q̃ of ∂ℛ with 𝖧q̃ ≥ c′q̃ (the conclusion of [[lem:i-a-4-1]]); and the bound
[[eq:i-a-4-1]], β_0⁻¹p_1 ≤ ϑ Id on ∂ℛ, where p_1 := ±ρ_∞σ_1(Im_h(·)). Its kernels are compactly supported, so the decay
order is immaterial. Here G_0 = p_2 ([[lem:iii-g-1-2]] (a); M is of first order), and [[lem:iii-g-2-1]] (b) gives the
source structure with β_0 = 2(1 + v) and q̃. It remains to compute p_1 on ∂ℛ_±.

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

    σ_1(Im_h N_M) = ξ(3 + 2Re_h S̄ − 2Re λ),     p_1 = 3 + 2Re_h S̄ − 2Re λ,     β_0⁻¹p_1 = 3/2 + Re_h S̄ − Re λ,   {#eq:iii-g-2-3}

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

    ‖w‖_(H̄^(1−s,−μ)_b) ≤ C(‖N_sf(λ)^(*h)w‖_(H̄^(−s,−μ)_b) + ‖w‖_(H̄^(−N_1,−μ−1)_b)),                       {#eq:iii-g-2-9}

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

    N_sf(λ)(v∂_v) = (v∂_v + 1)N_sf(λ) − M_1(v∂_v) − Σ_a M_aℒ_(Ω_a) − M_0,                                  {#eq:iii-g-2-11}

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

    N_sf(λ)W^α = W̃^αN_sf(λ) − Σ_(|β|=j) M_(αβ)W^β − Σ_(|β|<j) M′_(αβ)W^β,                                 {#eq:iii-g-2-12}

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
