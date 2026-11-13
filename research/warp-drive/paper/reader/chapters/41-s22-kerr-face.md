## The expansion at the Kerr face {#ch:s22}

This chapter proves, in dimension 4 + 1, [Hin26, Theorem 11.59] and its proof (pp. 278–292). With the correction
terms of the fourth kind of [[ch:s21]], the forward solution of the linearised gauge-fixed Einstein equation, for a
forcing of K⁺-order α ≤ 4 + ε_K, is made to decay at K⁺ at the order α − 2 by a unique choice of the modification
parameters ([[thm:iii-i11-4-1]], the form of [Hin26, (11.222)] in dimension 4 + 1). The solution so obtained is,
modulo a remainder of K⁺-order α, a sum of towers of the zero energy states whose coefficients are functions of t_*:
partially polyhomogeneous, except for a conormal boost coefficient of order α − 2 and a conormal black hole parameter of
order α − 1; and it is partially polyhomogeneous at ι⁺ with an index set ℰ_♯ to the order 3 + η_2, where η_2 < ε_+ is
as close to ε_+ as desired ([[thm:iii-i12-3-1]], the form of [Hin26, (11.196)] in dimension 4 + 1). The expansion is
also obtained at every level β ∈ (3, 4 + ε_K], and for the enlarged sources that the linearisation in the black hole
parameters of [[ch:s23]] produces ([[sec:iii-i13-2]]).

The argument has two phases. In spacetime ([[sec:iii-i10-3]]) the ι⁺-terms of the forcing of u-exponent below 2 are
solved by the ι⁺-normal operator up to the K⁺-order α ≤ 4 + ε_K, and the K⁺-terms this produces below the order α − 2
are identified as rows. What is left is a forward problem whose forcing is partially polyhomogeneous at ι⁺ from the order
4 on; it is solved on the spectral side ([[sec:iii-i11-3]]), through four zero energy solves, at the Taylor levels 0 to
3 at zero frequency, and the transition face model between them. The rows are then eliminated by the choice of the
parameters ([[sec:iii-i11-4]]), and the solution is expanded at K⁺ modulo the order α ([[sec:iii-i12-3]]).

The dimension changes the scheme of [Hin26] in these places. (1) Under the hypothesis (C5) below, the K⁺-range of the
ι⁺-normal operator is ℓ^max_K = 3, so [[cor:iii-g2-4-3]] solves the term at a u-exponent λ_0 with Re λ_0 < 2 with
ℓ_K = α − Re λ_0 for every α ≤ 4 + ε_K; [Hin26] uses its Proposition 9.11 at the exponent 1 only (Steps 2.A.2 and 4.1
of its proof). The rows this produces are all the rows of [[sec:iii-i9-1]] with Re λ < 2, and they are identified
through the towers ([[lem:iii-i10-2-1]]). (2) The parameter exponents, which [Hin26] builds after the proof by the
procedure of its (11.186), are fixed in advance ([[def:iii-i10-1-1]]), with logarithmic orders that grow with the real
part. The rows' own sources never enter the construction, since f^ν = Lm_ν + r^ν exactly ([[lem:iii-i9-2-6]]);
this is how the self-consistency of [Hin26, Remark 11.62] enters. (3) Two further conditions are needed: (H4),
ℓ_I > 3 + ε_+, and the gap condition (G) on ε_K. (4) The zero frequency Taylor expansion of the transformed forcing has
four terms (orders σ⁰ to σ³, as α − 1 > 3); the four zero energy solves are written out, with the polyhomogeneous
transition face model [[prop:iii-g4-4-4]] at the levels 1 and 2 and its conormal form [[prop:iii-g4-5-1]] at the level
3. (5) The spectral solution is written directly as a sum of physical pieces ([[lem:iii-i11-2-5]]): L̂_b(σ) is
injective on 𝒳′_σ ([[lem:iii-i6-1-2]]), so the rows of the augmented operator and the column moves of
[[lem:iii-i6-1-4]] are needed only at zero energy and at the last level. (6) The K⁺-terms below α − 2 come on the
spectral side only from the pieces of [[prop:iii-g4-4-4]] at the levels 1 and 2, which are homogeneous functions of σ
times spectral towers ([[lem:iii-i11-2-3]]); a lemma on forward tails ([[lem:iii-i10-2-4]]) turns them into rows,
among them the boost rows at the exponent 3 that the zero energy mass state produces. (7) The elimination is a
perturbation of the identity ([[lem:iii-i9-2-6]] (c), [[cor:iii-i10-2-3]]), where [Hin26, Step 2.B] has ± the identity
plus o(1); rows of different types at one rate are told apart by the degree of their spherical type and, within a
degree, by the order of their states at ∂X. (8) The expansion modulo the order α uses the equation itself: below that
order every coefficient section is a stationary solution of moderate growth ([[lem:iii-i12-2-3]]), so the
polyhomogeneous part at K⁺ is a sum of towers whatever the individual pieces are ([[lem:iii-i12-2-4]]). (9) The
spectral cut-off is an approximate identity with vanishing moments ([[lem:iii-i12-2-1]]), so each spectral piece is,
near K⁺, the spacetime tower of the inverse transform of its scalar coefficient. (10) Below the order 4 the forcing of
the last Taylor level has a negative zero frequency weight; the zero energy solve of that level then drops out
([[prop:iii-i13-2-1]]).

The steps that [Hin26, Part 3 (5) of the proof of Theorem 11.59] calls analogous are written out: the order
4 + ε_K needs four zero energy solves, of which [Hin26] writes three (its Steps 2.A.3, 2.A.5, 2.A.7), the fourth, at
σ³, being implicit there as well.

### The setting at a base point {#sec:s22-setting}

The notation is that of [[ch:s11]]–[[ch:s21]]; n = 4 throughout. The black hole parameters are b = (m, A), b_0 =
(m_0, 0), with tangent space 𝔟 = ℝ ⊕ 𝔰𝔬(4). In this chapter λ denotes an exponent at ι⁺ (an element of the projection
π_1 of an index set), as in [Hin26]; the wavelength of the main argument does not occur. Weights and index sets are
listed at (ℐ⁺, ι⁺, K⁺), with the defining functions ρ_I, ρ_+, ρ_K; Ω_* = cl_M{t^♭_* ≥ 1}, the spaces
H^(k,(…),(…),…)_b(Ω_*)^(•,−) and the class 𝒳^k of perturbations are those of [[sec:iii-i-1]] and [[eq:iii-i-1-4]].
On the spectral side, X̄, M′, X^±_(sc-b) with the faces scf, tf, zf and the spaces on them are those of
[[sec:iii-i2-4]] and [[sec:ii-g1-3-1]]; ρ = ⟨x⟩⁻¹ near ∂X, r̂ := |σ|r, and ℱ is the Fourier transform in t_*,
ŵ(σ) = ∫ e^(iσt_*) w dt_*. For an index set E, π_1E is the set of its exponents; "order w−" means order w − ε for every
ε > 0.

*The base point.* The base points of the linearisation are pairs (h, p⃗) as in [[sec:iii-i9-2]], whose black hole
parameter b lies in the closed ball ℬ̄_* about b_0 of [[sec:iii-h2-0]], shrunk as in [[lem:iii-i15-1-2]]. On ℬ̄_* the
model objects are uniform in b ([[lem:iii-i15-1-1]]): the forward problem at b with continuity in (b, S, h) (property
(P1) there); the ι⁺-normal operator, the transition face normal operator and the indicial roots of L̂_b(0) at ∂X, which
do not depend on b (P2); the zero energy states of the table of roots of [[sec:iii-g2-1]] for L_b, their companions,
the 1-form towers of [[prop:iii-d3-3-1]], the physical states of [[prop:iii-f4-5-1]] and ġ_b, which are real and smooth
in b, with index sets in (μ − j) + ℰ_ind, ℰ_ind independent of b (P3); the augmented low energy theory of [[ch:s18]]
at b (P4); and the time translation, Killing for every g_b (P5). The rows are built at the base point's b, and the
correction terms and their counterterms are the tensors built from b_0 (P6). Every statement below is the statement at
b: L_(b_0), g_(b_0) near K⁺, the states, towers and companions at b_0 and ℰ_ind are replaced by those at b, and the
splitting L_(h,p⃗) = L_b + (L_(h,p⃗) − L_b) near K⁺, which moves a perturbation into the source, has the same K⁺-gain as
at b_0, since the background equals g_b near K⁺ ([[lem:iii-i-3-6]]). Every constant is uniform on ℬ̄_*.

At b_0 every rotation is Killing, so the rotation state vanishes, h_(b_0,v1) = 0. At a rotating b the rotation state
h_(b,v1) ∈ 𝒜³ is smooth in b and O(|b − b_0|) but need not vanish ([[lem:iii-i15-1-1]] (P3)). The v1 terms of the
expansion then decay at K⁺ one order less than at b_0. The coefficient space of the v1 rows stays 𝒲_v1 = 𝒱′ = 0 at
every b ([[sec:iii-i9-1]]). The statements below keep these v1 terms explicit where h_(b,v1) ≠ 0 matters, and say so;
[[prop:iii-i15-2-2]] writes them as rotation rows whose coefficients are read from the construction, without inverting
the map V ↦ h_(b,v1)(V), which degenerates as b → b_0.

*The inner radius.* The chapter works on Ω_* with the spaces of [[ch:s09]] and the forward solutions of [[ch:s19]],
which hold with the inner radius r_0 of the artificial boundary as a parameter. Its own radii are scale-free
({r ≤ 2}, {r ≥ 1}, {r ≤ R} for arbitrary R), and its levels, loops and windows are fixed by weights at infinity and at
K⁺. So every result of this chapter holds with r_0 as a parameter.

### The parameter exponents {#sec:iii-i10-1}

Everything of [[sec:iii-i9-1]] is kept, at b: the enlarged index set ℰ_ind, ℱ = (0, 0) ∪ ℰ_ind, the index sets ℰ_++,
ℳ ([[eq:iii-i8-1-2]]), 𝒢 = (2, 0) ∪ (2 + ℰ_ind), ℰ̃_+ = 𝒢 ∪ (ℰ_+ + 𝒢) and 2ℰ_+ = ℰ_+ + ℰ_+, the number
δ_♯ = λ_♯ − 3/2 ∈ (0, 1/4), the constants [[eq:iii-i9-1-1]],

    0 < ε_K < ε_+ < min(δ_♯, ε_ind),     w_+ := 5 + ε_+,

the hypotheses (H1)–(H3) on the class, the types 𝒯 = {s1, v1, s0, s2, c0, c1} with the shifts d_τ, the rows
ν = (τ, λ, k) with K⁺-exponent e_ν = λ + d_τ and the finite set 𝒩 of the rows with Re e_ν ≤ 2, the coefficient spaces
𝒲_τ (with 𝒲_v1 = 0), the index sets ℰ_rows and ℰ_src with [[eq:iii-i9-1-3]], and the forcing spaces 𝒴_1(α), 𝒴_2(α),
𝒴(α). From [[sec:iii-i9-2]] are kept the tower lengths K_τ, the stationary 1-forms ω̆^i_τ, the identity
[[eq:iii-i9-2-1]], the states h_τ, the functions r_ν, a_ν, the rows m_ν, the corrections h_ν and counterterms ϑ_ν, the
operator P_4, its linearisation L_(h,p⃗) and the tensors f^ν_(h,p⃗), r^ν_(h,p⃗). ℰ^♯_+ is the set [[eq:iii-i1-3-2]],

    λ_♯ = 3/2 + (1 − e_Υ)γ_Υ = min Re ℰ^♯_+,

ℰ^ι_ind is the index set of [[thm:iii-g2-4-2]] ([[eq:iii-g2-4-4]]), and ε_ind is the constant of [[prop:iii-g4-5-1]].
[[def:iii-i9-2-1]] and [[lem:iii-i9-2-2]] (b), (e) extend verbatim to every triple (τ, λ, k) with τ ∈ 𝒯,
Re λ ≥ λ_♯ and k ∈ ℕ₀; m_ν and r_ν denote these also for ν ∉ 𝒩. Two further hypotheses are made:

(C5) γ_C v_C ≥ 1/2 ([[sec:iii-g2-1]]), so that ℓ^max_K = min(3, 2 + 2γ_C v_C) = 3 ([[eq:iii-g2-1-1]]).

(H4) ℓ_I > 3 + ε_+, with ℓ_I off the discrete exclusion sets of [[prop:iii-i1-3-1]] and [[thm:iii-g2-4-2]]. As
ℓ_I ≤ a_I ([[sec:iii-i8-1]]; this is used in [[lem:iii-i9-2-6]] (a), on which this section relies), (H4) asks
a_I > 3 + ε_+ of the class; the class of [Hin26] has the ℐ⁺-order 3 + ε_I. The condition ℓ_I < 3/2 + s_C of
[[thm:iii-g2-4-2]] is no restriction, s_C being large by (C1) of [[ch:s15]].

*The sources.* Fix ℰ_src as the least choice in [[eq:iii-i9-1-3]], and put

    ℰ⁰_src := ℰ̃_+ ∪ 2ℰ_+ ∪ (ℰ_rows ∩ {Re < 2}),          ℰ_src = ℰ⁰_src ∪ ℰ_rows.                    {#eq:iii-i10-1-1}

𝒴⁰_1(α), 𝒴⁰_2(α), 𝒴⁰(α) are 𝒴_1(α), 𝒴_2(α), 𝒴(α) with ℰ⁰_src in place of ℰ_src. They hold the sources of the
theorems below (the form of [Hin26, (11.195)] in dimension 4 + 1) and the derivatives f^S_(h,p⃗), f^(s1)_(h,p⃗)
(in 𝒴⁰(α)) and f^b_(h,p⃗) (in 𝒴⁰_2(α)) of [[lem:iii-i9-2-6]] (a): the term (∂δ*_(g_0,E_C))ϑ_rows there has plain
ι⁺-weight λ_♯ + 4 > w_+ (by its proof), and the rest is that of [[lem:iii-i7-3-1]], with the index sets ℰ̃_+ and
2ℰ_+. The row exponents of real part at least 2 enter only through f^ν_(h,p⃗) = L_(h,p⃗)m_ν + r^ν_(h,p⃗), where
r^ν_(h,p⃗) carries no index set ([[eq:iii-i9-2-5]]).

*The parameter exponents.* The index set ℰ_par of [[sec:iii-i9-1]], which [Hin26] calls Ẽ′_++ and builds after the
proof of its Theorem 11.59 by the procedure of its (11.186), is fixed here in advance.

**Definition {#def:iii-i10-1-1}** (The parameter exponents.) Let Λ ⊂ ℂ be the smallest set, closed under conjugation,
that contains

    π_1(ℰ_++ ∪ 𝒢 ∪ ℰ^C_I) ∪ {λ_♯, 3} ∪ (2 + π_1ℰ_col)

and satisfies Λ + w ⊂ Λ for every w ∈ π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}. Here ℰ_++ is the least choice in [[eq:iii-i8-1-1]],
and ℰ_col ⊂ {Re ≥ 0} is the index set at ∂X of the column terms ([[lem:iii-i11-1-1]]), independent of b. Let

    η_0 := min Re(π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}) > 0,          J_* := ⌈5/η_0⌉ + 2;

let l_* ∈ ℕ₀ bound, at real part at most 5, the logarithmic orders of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I, the orders of the
poles of N_ι⁺(L̄, ·)⁻¹ ([[lem:iii-g1-4-2]]) and the multiplicities of the indicial roots of L̂_b(0)
([[prop:iii-f1-2-3]]); and let k̄_0 ∈ ℕ bound the logarithmic orders of ℰ⁰_src ∪ ℰ_++ ∪ 𝒢 ∪ (2 + ℰ_col) at real part
below 2λ_♯, and only there. For λ ∈ Λ let n(λ) be the number of λ′ ∈ Λ with Re λ′ < Re λ, and

    k̄(λ) := k̄_0 + (J_* + 1)(l_* + 1)(n(λ) + 1).

Put

    ℰ_par := ℳ ∪ {(λ + j, k) : λ ∈ Λ, 2 ≤ Re λ ≤ 3, k ≤ k̄(λ), j ∈ ℕ₀}.                                 {#eq:iii-i10-1-2}

The number 3 ∈ Λ is the u-exponent of the boost row that the zero energy mass state produces ([[sec:iii-i11-3]]); the
increment 1 accounts for the Taylor levels of the spectral construction, and 2 + π_1ℰ_col for the column terms at its
first Taylor level.

**Lemma {#lem:iii-i10-1-2}** (a) Λ ∩ {Re ≤ R} is finite for every R, Λ ⊂ {Re ≥ λ_♯}, and Λ ∩ {Re < 2} = π_1ℳ.

(b) ℰ_par is an index set, closed under conjugation, satisfying [[eq:iii-i9-1-2]], and

    ℰ_par ∩ {Re ≤ 3} = ℳ ∪ {(λ, k) : λ ∈ Λ, 2 ≤ Re λ ≤ 3, k ≤ k̄(λ)}.

ℰ_par does not depend on ℰ_+. Hence (H3), which asks ℰ_+ ⊃ (λ, k) + ℱ for the rows, can be imposed on the class
together with (H1): this is the form of [Hin26, Remark 11.62] in dimension 4 + 1.

(c) (The logarithmic count.) Applied to sources in 𝒴⁰(α), the constructions of [[sec:iii-i10-3]] and
[[sec:iii-i11-3]] change index sets only by: adding (w, l) ∈ ℰ_ind ∪ ℰ^ι_ind ∪ {(1, 0)} to an exponent; unions with
the column exponents (2 + j, 0) + ℰ_col at the Taylor level j + 1 ([[lem:iii-i11-2-2]]), of logarithmic orders at most
k̄_0; extended unions with ℰ^C_I ([[eq:iii-i1-3-2]]) or with the indicial roots ([[lem:iii-a-1-4]]), each raising the
logarithmic order at one exponent by at most l_* + 1; and raising the logarithmic order at a treated exponent by a pole
order of N_ι⁺(L̄, ·)⁻¹ ([[cor:iii-g2-4-3]]) or by 1 ([[prop:iii-g4-4-4]] at α_0 = 2, [[rem:iii-g4-4-5]]). At an
exponent of real part at most 3 + ε_+ at most J_* such raises occur: each belongs to one window of the iteration of
[[sec:iii-i10-3]], of width at least η_0 below 2, or to one Taylor level of [[sec:iii-i11-3]], of which there are
four. Hence every exponent (λ, k) produced with 2 ≤ Re λ ≤ 3 + ε_+ has λ ∈ Λ and k ≤ k̄(λ). These are all the
exponents recorded: the ι⁺-data of 𝒴⁰(α) stop at the weight w_+ − ε, that is, at the u-exponent 3 + ε_+ − ε.

*Proof.* (a) The generators are index sets of real parts at least λ_♯ (ℰ_++ ⊂ ℰ_+ by (H1); min Re ℰ^C_I >
3/2 + 2γ_Υ > λ_♯, by Step 1 of the proof of [[prop:iii-i5-2-1]]), finitely many below every bound, and the increments
have real part at least η_0; so below R only sums with at most R/η_0 increments occur. Below 2 the generators lie in
π_1ℰ_++: λ_♯ does, and so does every element of π_1ℰ^C_I below 2, since [[eq:iii-i1-3-2]] puts it into ℰ^♯_+ and
ℰ_++ ⊃ ℰ^♯_+ ∩ {Re < 2} by (H1); 𝒢, 3 and 2 + π_1ℰ_col have real part at least 2. And π_1ℰ_++ ∩ {Re < 2} is closed
under the increments below 2 ([[eq:iii-i8-1-1]]; adding 1 leaves {Re < 2}, as λ_♯ + 1 > 2). So
Λ ∩ {Re < 2} = π_1ℳ.

(b) ℰ_par is an index set: by (a) it has finitely many exponents below each bound, with finitely many logarithms at
each, and it is closed under (z, k) ↦ (z + 1, k), as Λ + 1 ⊂ Λ, k̄(λ + 1) ≥ k̄(λ) (since n(λ + 1) > n(λ)), and, for
(z, k) ∈ ℳ, z + 1 ∈ Λ has real part in [2, 3) and k ≤ k̄_0 ≤ k̄(z + 1) (as ℳ ⊂ ℰ_++). The part below 3: if
Re(λ + j) ≤ 3 with j ≥ 1, then Re λ = 2, j = 1 and k̄(λ) ≤ k̄(λ + 1). Conjugation: Λ is closed under it,
n(λ̄) = n(λ), and ℳ = ℳ̄. [[eq:iii-i9-1-2]]: min Re ℰ_par ≥ λ_♯, and ℰ_par ∩ {Re < 2} = ℳ.

*Independence of ℰ_+.* The increments have positive real parts, so Λ ∩ {Re < R} is determined by the generators of real
part below R, and ℰ_par by Λ ∩ {Re ≤ 3} and k̄_0. Below 2λ_♯ = 3 + 2δ_♯ > 3 + ε_+ ([[eq:iii-i9-1-1]]) nothing used
involves ℰ_+: 𝒢, ℰ^C_I and ℰ_col do not; the parts of ℰ⁰_src (and of ℰ_rows) that involve ℰ_+, namely ℰ_+ + 𝒢, 2ℰ_+
and (λ, k) + ℱ + ℰ_+, have real part at least 2λ_♯ by (H1); and the least ℰ_++ of [[eq:iii-i8-1-1]] agrees below 2λ_♯
with the least index set that contains ℰ^♯_+ ∩ {Re < 2} and is closed under the addition of ℰ^ι_ind ∪ ℰ_ind, since
adding an element of ℰ_+ lands at real part at least 2λ_♯. So Λ ∩ {Re ≤ 3}, k̄_0 and ℰ_par do not depend on ℰ_+. The
conditions on ℰ_+ ((H1); (H3), which with [[eq:iii-i8-1-1]] gives ℰ_+ ⊃ ℰ_par + ℱ; ℰ_+ ⊃ ℰ^♯_+ ∩ {Re < 2}; and
ℰ_+ + (ℰ^ι_ind ∪ ℰ_ind ∪ ℰ_+) ⊂ ℰ_+ there) are therefore conditions on ℰ_+ alone, and the least index set that contains
ℰ_par + ℱ and ℰ^♯_+ ∩ {Re < 2} and is closed under these additions meets them, its exponents being sums of exponents of
real part at least λ_♯.

(c) The exponents produced lie in Λ, which contains the generators and is closed under the additions listed (the
exponent 4 of [[eq:iii-g4-4-3]], at the Taylor level j of [[sec:iii-i11-3]], is the u-exponent 3 + j). Logarithmic
orders, by induction on n(λ): the logarithmic order at λ is the largest over its contributions, each either a
generator's or a column exponent's (at most k̄_0, as Re λ ≤ 3 + ε_+ < 2λ_♯) or (λ′, k′) + (w, l) with
Re λ′ < Re λ, k′ ≤ k̄(λ′) and l ≤ l_*, plus at most J_*(l_* + 1) from the raises at λ. As n(λ) ≥ n(λ′) + 1,

    k̄(λ) − k̄(λ′) ≥ (J_* + 1)(l_* + 1) ≥ l_* + J_*(l_* + 1),     and     k̄_0 + J_*(l_* + 1) ≤ k̄(λ).     ∎

**Definition {#def:iii-i10-1-3}** (The gap and admissible orders.) (G) ε_K is so small that no λ ∈ Λ has real part in
(2, 2 + ε_K] ∪ (3, 3 + ε_K], and no λ + d_c0 or λ + d_c1, λ ∈ Λ, has real part in (2, 2 + ε_K]. This is possible by
[[lem:iii-i10-1-2]] (a), as Λ does not depend on ε_K; it implies d_c0, d_c1 > ε_K, since 2 ∈ Λ. The constants
[[eq:iii-i9-1-1]] may be kept, decreasing ε_K. A number α ∈ (2, 4 + ε_K] is *admissible* if: for α < 3, it is
admissible in the sense of [[sec:iii-i8-1]]; for α ≥ 3, α > 4 + ε_K − ε′_0, with

    ε′_0 := ½ min(ε_K, ε_+ − ε_K),

and α avoids the finite set of values for which α − Re λ_0, λ_0 ∈ Λ, Re λ_0 < 2, equals −Re μ for a root μ of
L̂_b(0) or lies in Re π_1ℰ_K ([[lem:iii-g1-1-3]]), and the finite exclusion set of [[sec:iii-i11-1]].

For admissible α ≥ 3 the rows of K⁺-rate below α − 2 are exactly those of 𝒩: a row with (λ, k) ∈ ℰ_par has the rate
Re λ − 1 ≤ 2 (s1), Re λ (s0, s2) or Re λ + d_τ (c0, c1), and by (G) no such rate lies in (2, 2 + ε_K] ⊃ (2, α − 2).

### Towers, row expansions and forward tails {#sec:iii-i10-2}

**Lemma {#lem:iii-i10-2-1}** (Towers.) Let τ ∈ 𝒯, W ∈ 𝒲_(τ,ℂ), and put

    h̆^i_τ(W) := δ̂*_(g_b)(0) ω̆^i_τ(W) + dt_* ⊗_s ω̆^(i−1)_τ(W),     i ≥ 0,

with ω̆^(−1)_τ := 0 and ω̆^i_τ := 0 for i > K_τ.

(a) For every function a = a(t_*) and K ≤ K_τ,

    δ*_(g_b)(Σ_(i=0)^K a^((i)) ω̆^i_τ(W))
        = Σ_(i=0)^K a^((i)) h̆^i_τ(W) + a^((K+1)) dt_* ⊗_s ω̆^K_τ(W).                                   {#eq:iii-i10-2-1}

So m_ν(W) = χ_K(Σ_(i≤K_τ) a_ν^((i)) h̆^i_τ(W) + a_ν^((K_τ+1)) dt_* ⊗_s ω̆^(K_τ)_τ(W)) for ν = (τ, λ, k); and
h̆⁰_τ = h_τ for τ ≠ s0, while h̆⁰_s0 = 0 and h̆¹_s0 = h_s0.

(b) The towers of [[def:iii-g2-2-5]] at b for the types of 𝒯 are these:

    h^(≤k)_(b,s1)(aS) = Σ_(i≤k) a^((i)) h̆^i_s1(S),     h^((0),≤k)_(b,s0)(aY) = Σ_(i≤k) a^((i)) h̆^(i+1)_s0(Y),

and h^((μ),≤k)_(b,τ)(aY) = Σ_(i≤k) a^((i)) h̆^i_τ(Y) for τ = s2, c0, c1 (with μ = 0, μ_c0, μ_c1), for k up to the
lengths of the table of roots of [[sec:iii-g2-1]].

(c) Let λ_0 ∈ ℂ with Re λ_0 ≥ λ_♯, j ∈ ℕ₀, and let u_(b,0) be [[eq:iii-g2-4-3]] at b with λ_0 for λ, a factor
(log t_*)^j in each argument, and coefficients S^(−1)_1, V^(−1)_1, Y^(μ)_τ. For τ ∈ 𝒯 ∖ {v1} let
ν_τ := (τ, λ_τ, j) with λ_τ := λ_0, and W_s1 := (λ_0(λ_0 − 1))⁻¹S^(−1)_1, W_τ := Y^(μ_τ)_τ otherwise
(μ_s0 = μ_s2 := 0). Put V := −λ_0⁻¹V^(−1)_1. Then

    χ_K u_(b,0) − Σ_(τ∈𝒯∖{v1}) m_(ν_τ)(W_τ) − χ_K t_*^(−λ_0)(log t_*)^j h_(b,v1)(V)
        has K⁺-weight Re λ_0 + 1 − ε for every ε > 0.                                                   {#eq:iii-i10-2-2}

The last term on the left vanishes when h_(b,v1) = 0, in particular at b_0.

(d) For a tempered a with Fourier transform â(σ) = ∫ e^(iσt_*) a dt_*, the Fourier transform in t_* of
δ*_(g_b)(Σ_(i≤K) a^((i)) ω̆^i_τ(W)) is â(σ)T^K_τ(σ, W), with the polynomial

    T^K_τ(σ, W) := Σ_(i=0)^K (−iσ)^i h̆^i_τ(W) + (−iσ)^(K+1) dt_* ⊗_s ω̆^K_τ(W)
                 = δ̂*_(g_b)(σ) Σ_(i=0)^K (−iσ)^i ω̆^i_τ(W).                                           {#eq:iii-i10-2-3}

*Proof.* (a) δ*_(g_b)(φ(t_*)v) = φ δ̂*_(g_b)(0)v + φ′ dt_* ⊗_s v for stationary v ([[eq:iii-i4-1-2]]); sum over i and
collect the terms with a^((i)). For s0, ω̆⁰_s0 is Killing ([[lem:iii-i15-1-1]] (P5)), so h̆⁰_s0 = 0, and
h̆¹_s0 = δ*(t_*ω̆⁰ + ω̆¹) = h_s0 ([[sec:iii-i9-2]]).

(b) The state column of the table of roots of [[sec:iii-g2-1]] takes the states and their companions from
[[prop:iii-d2-3-1]] and [[prop:iii-d3-3-1]] (1)–(7), the same 1-form towers as [[def:iii-i9-2-1]] (whose list cites
the same items), under δ*_(g_b): the tower of L_b-solutions δ*ω^(≤k), with ω^(≤k) = Σ_(i≤k) (k!/(k − i)!) t_*^(k−i)
ω̆^i, is by [[eq:iii-i10-2-1]] with a = t_*^k the polynomial Σ_(i≤k) (k!/(k − i)!) t_*^(k−i) h̆^i, which is the
description of a tower with companions h̆^i in [[lem:iii-g2-2-1]] (a). For s0 the state is h^((0))_(b,s0) = h̆¹, and the
index is shifted by one.

(c) By (b), the term of u_(b,0) of type τ ∈ 𝒯 ∖ {v1} is the sum over i ≤ k_τ (the lengths k_μ of the table: 3 for s1,
2 for s0, s2, c0, c1) of a^((i)) times companions, with a = c r_(ν_τ): for s1,
a_s1(log t_*)^j = (λ_0(λ_0 − 1))⁻¹ t_*^(−λ_0+1)(log t_*)^j ([[eq:iii-g2-4-2]]; λ_0 ≠ 1); for s0, s2, c0, c1,
t_*^(−λ_0+μ)(log t_*)^j = r_(ν_τ) (for s0, a = r_ν = A′_ν, [[def:iii-i9-2-1]]). By (a), m_(ν_τ)(W_τ) is the same sum
with K_τ ≥ k_τ in place of k_τ, plus a^((K_τ+1)) dt_* ⊗_s ω̆^(K_τ) (for s0, K_s0 − 1 = 3 ≥ k_s0 after the shift of
index), times χ_K. The difference carries only a^((i)) with i ≥ k_τ + 1 ≥ 3, of K⁺-weight
Re e_(ν_τ) + 3 − ε ≥ Re λ_0 + 2 − ε. The v1 term is h^(≤2)_(b,v1)(a_v1 V^(−1)_1), times (log t_*)^j, with
a_v1 = −λ_0⁻¹ t_*^(−λ_0) ([[eq:iii-g2-4-2]]); its bottom is the last term subtracted in [[eq:iii-i10-2-2]], and the
rest carries a_v1^((i)), i ≥ 1, of K⁺-weight Re λ_0 + 1 − ε. At b_0 the bottom vanishes, every V ∈ 𝒱_1 being
Killing ([[sec:iii-i9-1]]). The rows of [[eq:iii-g2-4-3]] outside 𝒯 have roots μ with Re μ ≤ −1 and rate
Re(λ_0 − μ) ≥ Re λ_0 + 1. On compact spatial sets χ_K = 1 for large t_*, and the stationary companions are smooth
there.

(d) ∫ e^(iσt) a^((i)) dt = (−iσ)^i â(σ), and [[eq:iii-i10-2-1]]. ∎

**Lemma {#lem:iii-i10-2-2}** (Joint injectivity of the states.) For each τ ∈ 𝒯 ∖ {v1} let W_τ ∈ 𝒲_(τ,ℂ). If
Σ_τ h_τ(W_τ) = 0, then every W_τ = 0. This holds at every b ∈ ℬ̄_*, for the states at b.

*Proof.* At the static, spherically symmetric b_0, every construction of [[prop:iii-d2-3-1]] and
[[prop:iii-d3-3-1]] stays in its isotypic component (the types in the proof of [[prop:iii-d3-3-1]]), and ω̆⁰_τ(W) is of
scalar type of degree l_τ: 0 for s0 and c0, 1 for s1 and c1, 2 for s2 ([[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]] (1),
(4)–(7)). For s0, whose state is δ*(t_*ω̆⁰ + ω̆¹), ω̆¹_s0 is of degree 0 as well ([[prop:iii-d3-3-1]] (1)). So h_τ(W)
lies in the isotypic component of degree l_τ, and these components are independent. Degree 2: h_s2 is injective
([[lem:iii-i9-2-2]] (f)). Degree 0: h_c0(W_c0) ∈ 𝒜^((μ_c0,0)+ℱ) has a nonzero ρ^(μ_c0)-coefficient if W_c0 ≠ 0 (the
proof of [[lem:iii-i9-2-2]] (f)), while h_s0(W_s0) ∈ 𝒜^((0,0)+ℱ) ([[eq:iii-d3-3-1]], with (2, 0) ∈ ℰ_ind,
[[sec:iii-i9-1]]) and μ_c0 < 0 ≤ min Re ℱ; so W_c0 = 0, and then W_s0 = 0. Degree 1: the same, with
h_s1(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)) ([[eq:iii-f3-4-2]]) and μ_c1 < 0. At b ∈ ℬ̄_* the statement is [[lem:iii-i15-1-2]],
which deduces it from the case b_0 by perturbation, with a lower bound uniform in b. ∎

**Corollary {#cor:iii-i10-2-3}** (Uniqueness of row expansions.) Let 𝒩′ be a finite set of rows ν = (τ, λ, k),
τ ≠ v1, and W_ν ∈ 𝒲_(τ,ℂ). If Σ_(ν∈𝒩′) m_ν(W_ν) has K⁺-weight w > max_(𝒩′) Re e_ν, then every W_ν = 0. This holds at
every b ∈ ℬ̄_*.

*Proof.* Suppose not, and let e_0 be the least real part of e_ν over the ν with W_ν ≠ 0. By [[lem:iii-i9-2-2]] (e),
m_ν(W) − χ_K r_ν h_τ(W) has K⁺-weight Re e_ν + 1 − ε; this follows from the tower relations, which hold at b
([[lem:iii-i15-1-1]] (P3)). So on every compact spatial set, for large t_*,

    Σ_((e,k): Re e = e_0) t_*^(−e)(log t_*)^k Σ_τ h_τ(W_((τ,e−d_τ,k))) = O(t_*^(−e_0−δ))

for some δ > 0, the inner sum over the τ with (τ, e − d_τ, k) ∈ 𝒩′. The functions t_*^(−e)(log t_*)^k, finitely many
and distinct, with Re e = e_0, are linearly independent modulo O(t_*^(−e_0−δ)): with s = log t_*, a nonzero
Σ_(e,k) c_(e,k) s^k e^(−is Im e) does not tend to 0 as s → ∞. So each inner sum vanishes on X°, and
[[lem:iii-i10-2-2]] gives W_ν = 0 for those ν, a contradiction. ∎

**Lemma {#lem:iii-i10-2-4}** (Forward tails.) Let V be a Fréchet space, β > −1, β ∉ ℕ₀, E ⊂ ℂ × ℕ₀ finite with
−1 < Re z < β for (z, m) ∈ E, a^±_(z,m) ∈ V for (z, m) ∈ E, and r^± ∈ C^∞(±(0, c]; V) with
(σ∂_σ)^j r^± = O(|σ|^β) for all j. Let χ ∈ C_c^∞((−c, c)) equal 1 near 0,

    v(σ) := χ(σ) Σ_± 1_(±σ>0)(Σ_((z,m)∈E) |σ|^z(log|σ|)^m a^±_(z,m) + r^±(σ)),          w := ℱ⁻¹v,

and suppose that w(t) = O(|t|^(−β−1)) as t → −∞. Then:

(a) for z ∈ ℕ₀, with M the largest m such that (z, m) ∈ E: a^−_(z,M) = (−1)^z a^+_(z,M), that is, the coefficients of
σ^z(log|σ|)^M on the two sides agree; this is the matching condition [[eq:iii-a-4-4]] of [[prop:iii-a-4-2]] at z;

(b) as t → +∞, for every δ > 0,

    w(t) = Σ_((z,m)∈E) Σ_(j≤m) t^(−z−1)(log t)^j b_(z,j) + O(t^(−β−1+δ)),

where b_(z,j) is a linear combination, with coefficients depending only on z, m and j, of the a^+_(z,m′) with m′ ≥ j,
and with m′ ≥ j + 1 if z ∈ ℕ₀. In particular the log-free terms |σ|^z a^±_(z,0) with z ∈ ℕ₀ contribute nothing.

*Proof.* We use ŵ(σ) = ∫ e^(iσt) w dt. For Re z > −1 let s^±_z := (σ ± i0)^z, the boundary values from ±Im σ > 0 of σ^z
(principal branch, arg σ ∈ (0, π), resp. (−π, 0)), and s^±_(z,m) := ∂^m_z s^±_z = (σ ± i0)^z(log(σ ± i0))^m. On σ > 0
both equal σ^z(log σ)^m; on σ < 0 they equal |σ|^z(log|σ| ± iπ)^m e^(±iπz). As

    ∫_0^∞ e^(iσt) t^a dt = Γ(a + 1) e^(iπ(a+1)/2) (σ + i0)^(−a−1)     (Re a > −1),

continued analytically, ℱ⁻¹s^+_z = c(z) t_+^(−z−1) with c(z) := e^(iπz/2)/Γ(−z), an entire function with simple zeros
exactly at ℕ₀ (where s^+_z = s^−_z = σ^z is a polynomial), and ℱ⁻¹s^−_z = c̄(z̄) t_−^(−z−1) likewise, with t_− := −t
on t < 0. Differentiating in z: ℱ⁻¹s^+_(z,m) = ∂^m_z(c(z)t_+^(−z−1)) is supported in t ≥ 0 and equal for t > 0 to
Σ_(j≤m) C(m, j) c^((m−j))(z)(−log t)^j t^(−z−1), C(m, j) the binomial coefficient; its top power of log t is m, with
coefficient (−1)^m c(z) ≠ 0, if z ∉ ℕ₀, and m − 1, with coefficient (−1)^(m−1) m c′(z) ≠ 0, if z ∈ ℕ₀ and m ≥ 1. The
same holds for s^−_(z,m) on t < 0, with |t|. Multiplying by χ changes the inverse transforms by ℱ⁻¹((1 − χ)s), which
is smooth on t ≠ 0 and O(|t|^(−∞)), as (1 − χ)s is smooth and a symbol in σ. And ℱ⁻¹(χ1_± r^±) = O(|t|^(−β−1+δ)): on
|σ| < |t|⁻¹ the integrand is O(|σ|^β); on |σ| > |t|⁻¹ we integrate by parts ⌈β⌉ + 1 times, using
|∂^j_σ r^±| ≤ C|σ|^(β−j), the boundary terms at |σ| = |t|⁻¹ being of the same size.

Fix z with (z, m) ∈ E for some m, and let M be the largest such m. If z ∉ ℤ, the 2(M + 1) functions
1_(±σ>0)|σ|^z(log|σ|)^m, m ≤ M, and s^±_(z,m), m ≤ M, span the same space: the change of basis is block triangular in m
with the diagonal blocks

    ( 1         1        )
    ( e^(iπz)   e^(−iπz) ),

invertible as e^(2iπz) ≠ 1. If z ∈ ℕ₀, then s^+_(z,0) = s^−_(z,0), and the space spanned by the
1_(±σ>0)σ^z(log|σ|)^m, m ≤ M, is spanned by σ^z, the s^±_(z,m) with 1 ≤ m ≤ M, and s^+_(z,M+1) − s^−_(z,M+1), which on
σ < 0 is 2πi(M + 1)σ^z(log|σ|)^M plus lower powers of the logarithm and which vanishes on σ > 0; its coefficient in the
expansion of v is ((−1)^z a^−_(z,M) − a^+_(z,M))/(2πi(M + 1)), the data on σ < 0 being
a^−_(z,M)|σ|^z = (−1)^z a^−_(z,M)σ^z. So

    v = χ Σ_z (Σ_m B^+_(z,m) s^+_(z,m) + Σ_m B^−_(z,m) s^−_(z,m)) + χ Σ_± 1_± r^±,

with B^−_(z,M+1) = −B^+_(z,M+1) = (a^+_(z,M) − (−1)^z a^−_(z,M))/(2πi(M + 1)) for z ∈ ℕ₀, the polynomial σ^z
counted with s^+. As t → −∞ only the s^−-terms and r^± contribute beyond O(|t|^(−∞)):

    w(t) = Σ_(z,m) B^−_(z,m) ∂^m_z(c̄(z̄)|t|^(−z−1)) + O(|t|^(−β−1+δ)) = O(|t|^(−β−1)).

The functions |t|^(−z−1)(log|t|)^j, finitely many and distinct with Re z < β, are independent modulo
O(|t|^(−β−1+δ)) for small δ, and for each z the top powers of the logarithm computed above are strictly increasing in m
(for z ∈ ℕ₀ from m = 1 on); so by descending induction on m every B^−_(z,m) with z ∉ ℕ₀, or with z ∈ ℕ₀ and m ≥ 1,
vanishes. For z ∈ ℕ₀ this includes m = M + 1, which is (a). On σ > 0 the s^+_(z,m) are σ^z(log σ)^m, so
B^+_(z,m) = a^+_(z,m) for m ≥ 1, and for m = 0 when z ∉ ℕ₀; and (b) follows from the formula for ℱ⁻¹s^+_(z,m) on t > 0,
σ^z (z ∈ ℕ₀) contributing O(t^(−∞)). ∎

The point of (b) is that the tail of a forward supported function is read off from the side σ > 0 alone, and that the
log-free pieces of integer degree (jumps, and the parts of the solutions of the transition face model that depend on
ρ, [[sec:iii-i11-3]]) do not reach K⁺.

### The spacetime phase {#sec:iii-i10-3}

This section is [Hin26, Theorem 11.59, Part 1 of the proof, with Steps 2.A.1–2.A.2 and 4.1] in dimension 4 + 1. Let

    𝒩_ι := {ν ∈ 𝒩 : λ_ν ∈ π_1ℳ},

the rows with Re λ < 2 (the s1 rows among them are the motions of [[ch:s21]]), and 𝒩_σ := 𝒩 ∖ 𝒩_ι, the rows with
2 ≤ Re λ ≤ 3. By [[sec:iii-i10-1]] these are the s1 rows with (λ, k) ∈ ℰ_par and 2 ≤ Re λ ≤ 3, the s0 and s2 rows
with Re λ = 2, and the v1 rows with Re λ = 2, which carry no parameter; by (G), a row of type c0 or c1 with Re λ ≥ 2 has
rate at least 2 + d_τ > 2 + ε_K.

**Proposition {#prop:iii-i10-3-1}** (The spacetime phase.) Let α ∈ (2, 4 + ε_K] be admissible, and let f = f_1 + f_2
with f_j ∈ 𝒴⁰_j(α), real and vanishing for t_* < 1. There are real u_I, u_ι, vanishing for t_* < 1, coefficients
S_ν ∈ 𝒲_(τ,ℂ), ν ∈ 𝒩_ι, and V_(λ_0,j) ∈ 𝒱_(1,ℂ), (λ_0, j) ∈ ℳ, all linear and continuous in f, the S_ν and the
V_(λ_0,j) conjugation-symmetric, such that, with

    u^rot_ι := Σ_((λ_0,j)∈ℳ) χ_K t_*^(−λ_0)(log t_*)^j h_(b,v1)(V_(λ_0,j)),

which vanishes when h_(b,v1) = 0, in particular at b_0:

(a) u_I ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_I,3+ε_+−ε),∞)_b(Ω_*)^(•,−) vanishes on {ρ_I > ½c_I}, so near K⁺;

(b) u_ι − Σ_(ν∈𝒩_ι) m_ν(S_ν) − u^rot_ι ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),λ_♯−ε,α−2−ε)_b(Ω_*)^(•,−);

(c) f^♭ := f − L_b(u_I + u_ι) ∈ ⋂_(ε>0) H^(∞,ℓ_I+1,(ℰ^♭+2,w_+−ε),α−ε)_b(Ω_*; S²T*)^(•,−), vanishing for t_* < 1,
where ℰ^♭ is an index set with π_1(ℰ^♭ ∩ {Re < 3 + ε_+}) ⊂ Λ ∩ {Re ≥ 2} and logarithmic order at most k̄(λ) at λ, and
ℰ_I in (a) is an index set with π_1(ℰ_I ∩ {Re < 3 + ε_+}) ⊂ Λ.

For α < 3 this is Steps 1–2 of the proof of [[lem:iii-i8-3-2]], with the ι⁺-expansion recorded to the weight w_+; the
point here is α ≤ 4 + ε_K.

*Proof.* The construction is that of Steps 1–2 of the proof of [[prop:iii-i5-2-1]] ([[eq:iii-i5-2-3]]–[[eq:iii-i5-2-5]]),
as [[lem:iii-i8-3-1]] and [[lem:iii-i8-3-2]] use it, with three changes: the step at ℐ⁺ goes to
ℓ̆_+ := w_+ − 2 − ε = 3 + ε_+ − ε; the K⁺-order of the steps at ι⁺ is c_K := α; and the identification of the K⁺-terms
below α − 2 includes all of 𝒯.

*Step 1 (ℐ⁺; [Hin26, Step 2.A.1]).* [[prop:iii-i1-3-1]] with Ĕ_+ := (ℰ⁰_src)_(≥2) (the u-exponents of the ι⁺-index set
of f_1) and ℓ̆_+ := 3 + ε_+ − ε (below ℓ_I by (H4), and off the exclusions there for all but finitely many ε) gives
u⁽⁰⁾_I, vanishing on {t_* < 1} ∪ {ρ_I > ½c_I}, with ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I), ι⁺-data (ℰ^♯_+, ℓ̆_+) for this Ĕ_+, and
f_1 − L_b u⁽⁰⁾_I ∈ H^(∞,ℓ_I+1,(ℰ^♯_++2,w_+−ε))_b; near K⁺ it is f_1, of K⁺-weight α. f_2 is supported in supp χ^♯_K,
away from ℐ⁺, with ι⁺-index set ℰ⁰_src + 2. So f⁽⁰⁾ := f − L_b u⁽⁰⁾_I has plain ℐ⁺-weight ℓ_I + 1, an ι⁺-index set below
w_+ − ε with u-exponents in π_1(ℰ^♯_+ ∪ ℰ⁰_src) ⊂ Λ (by [[eq:iii-i1-3-2]], π_1ℰ^♯_+ ⊂ π_1Ĕ_+ ∪ {λ_♯} ∪ π_1ℰ^C_I; and
π_1ℰ⁰_src ∩ {Re ≤ 3 + ε_+} ⊂ π_1(𝒢 ∪ ℳ) by the proof of [[lem:iii-i10-1-2]] (b)), and K⁺-weight α − ε.

*Step 2 (ι⁺, the u-exponents below 2; [Hin26, Steps 2.A.2 and 4.1]).* Step 2 of the proof of [[prop:iii-i5-2-1]] with
c_K := α is applied to the terms of f⁽⁰⁾ of u-exponent λ_0 with Re λ_0 < 2, in increasing order of the real part,
window by window. For each such λ_0, ℓ_K(λ_0) := α − Re λ_0 ∈ (α − 2, α − λ_♯]; as α ≤ 4 + ε_K < 3 + λ_♯ (since
ε_K < δ_♯ + ½), ℓ_K(λ_0) < 3 = ℓ^max_K by (C5), and ℓ_K(λ_0) > α − 2 > 0; it avoids the roots and Re π_1ℰ_K by
admissibility. The other hypotheses of [[cor:iii-g2-4-3]] at b hold as in that step: Re λ_0 ≥ λ_♯ > 1; the pole order of
N_ι⁺(L̄, ·)⁻¹ at λ_0 is 0, as spec_ι⁺(L̄) ⊂ {Re ≥ 2} ([[lem:iii-g1-4-2]] (a)); ℓ_I < 3/2 + s_C,
ℓ_I ∉ Re π_1ℰ^tot_(ι⁺,ℐ) and Re λ_0 < 2 < ℓ_I; and the coefficients at λ_0 have R-weight at least
α − ε − Re λ_0 − 2 = ℓ_K(λ_0) − 2 − ε, the current forcing having K⁺-weight α − ε (each error of [[cor:iii-g2-4-3]] has
K⁺-weight Re λ_0 + ℓ_K(λ_0) − ε = α − ε, by [[eq:iii-g2-4-4]], and the solutions at ℐ⁺ vanish near K⁺).
[[cor:iii-g2-4-3]] gives

    u_(λ_0) = Σ_(j≤k) χ_K u^((j))_(b,0) + χ_ι t_*^(−λ_0)(log t_*)^j ũ^((j)),

of K⁺-index set ℰ^gr_K(λ_0) + (0, k) at the weight ℓ_K(λ_0) − ε > α − 2. The expansion at ℐ⁺ of the error is removed by
[[prop:iii-i1-3-1]] as in Step 2 of the proof of [[prop:iii-i5-2-1]]; its solution u′_(λ_0) vanishes near K⁺, and its
new ι⁺-exponents lie in λ_0 + ℰ^ι_ind + (0, k) or have real part at least 5/2 (there is no ρ_I^(z+1)-term with
Re z < 5/2). Every exponent created lies in Λ with logarithmic order at most k̄ ([[lem:iii-i10-1-2]] (c)), and the
exponents below 2 lie in π_1ℳ with the logarithmic orders of ℰ_++ ([[eq:iii-i8-1-1]], as in [[lem:iii-i8-3-1]]). After
finitely many windows no term of u-exponent below 2 is left. Put u_I := u⁽⁰⁾_I + Σ u′_(λ_0) and u_ι := Σ u_(λ_0). Then
(a) and (c) hold, (c) with ℰ^♭ the remaining u-exponents (at least 2), and u_I has its ι⁺-exponents in Λ.

*The rows.* By [[lem:iii-i10-2-1]] (c), with the (log t_*)^j-versions, each χ_K u^((j))_(b,0) equals

    Σ_(τ∈𝒯∖{v1}) m_((τ,λ_0,j))(W^((j))_τ) + χ_K t_*^(−λ_0)(log t_*)^j h_(b,v1)(V^((j)))

up to K⁺-weight Re λ_0 + 1 − ε > α − 2 − ε (as λ_♯ + 1 > 5/2 > 2 + ε_K), V^((j)) being −λ_0⁻¹ times the v1
coefficient of [[eq:iii-g2-4-3]] in the j-th term. The rows (τ, λ_0, j) so produced have (λ_0, j) ∈ ℳ; those of rate at
most 2 are in 𝒩_ι, and by (G) the others (c0 and c1 with Re λ_0 + d_τ > 2) have rate above 2 + ε_K ≥ α − 2, so that
m_((τ,λ_0,j)) has K⁺-weight at least α − 2 − ε ([[lem:iii-i9-2-2]] (e)) and joins the remainder. The rest of u_(λ_0)
has K⁺-weight ℓ_K(λ_0) − ε > α − 2. Summing, with S_ν the sum of the W^((j))_τ for ν = (τ, λ_0, j) and V_(λ_0,j) the
sum of the V^((j)), gives (b); the ι⁺-weight λ_♯ − ε holds for u_ι and, by [[lem:iii-i9-2-2]] (b), for each m_ν and
each term of u^rot_ι (h_(b,v1) ∈ 𝒜³).

*Reality and linearity.* Every map used is linear and continuous. f and L_b are real, and conjugation maps the
construction for λ_0 to that for λ̄_0; so u_I, u_ι may be taken real (or replaced by their real parts, which satisfy
(a)–(c) with the real parts of the identities), and the S_ν and V_(λ_0,j) are conjugation-symmetric
(m_ν̄(W̄) is the conjugate of m_ν(W), and h_(b,v1) is real, [[lem:iii-i15-1-1]] (P3)). ∎

So for f ∈ 𝒴⁰(α) the forward solution u of L_b u = f is

    u = Σ_(ν∈𝒩_ι) m_ν(S_ν) + u^rot_ι + u_rem + v,

with u_rem of K⁺-weight α − 2 − ε and v the forward solution of L_b v = f^♭, a forcing partially polyhomogeneous at ι⁺
from the order 4 on, with plain ℐ⁺-weight ℓ_I + 1. [[sec:iii-i11-3]] expands v at K⁺: its terms of rate below α − 2
are the rows of 𝒩_σ, together, at a rotating b, with v1 terms of exponent of real part 2. At a rotating b the terms of
u^rot_ι are the bottoms of the rotation rows of [[prop:iii-i15-2-2]] (a).

### The spectral setting {#sec:iii-i11-1}

Everything of [[sec:iii-i10-1]] is kept: (C5), (H4), Λ, k̄(λ), ℰ_par, (G), ℰ⁰_src and 𝒴⁰(α), and the rows
𝒩 = 𝒩_ι ∪ 𝒩_σ of [[sec:iii-i10-3]].

*Spectral notation* ([[sec:iii-i2-4]], [[sec:iii-i6-1]], [[sec:iii-i6-2]]). X^±_(sc-b) carries the faces scf, tf, zf,
with |σ| = ρ_tf ρ_zf and r̂ = |σ|r; χ_zf, χ_tf and χ^♯_tf are the cut-offs there. L̂_b(σ) = L_0 − iσL_1 − σ²L_2, with
L_1 of one order of decay at ∂X ([[lem:iii-i6-1-1]]). L̃_b(σ) is the augmented operator of [[ch:s18]],
L̃_b(σ)(u, ḃ, S) = (L̂_b(σ)u + f̂_ḃ(σ) + f̂_S(σ), r(u)), with ĝ^aug(σ)(ḃ) = iσ⁻¹G_1(σ)(ḃ) and
ĥ^aug(σ)(S) = −σ⁻²G_2(σ)(S), where

    G_1(σ)(ḃ) := Ψ ġ(ḃ),          G_2(σ)(S) := Ψ h(S) − σ∂_σΨ h(S) − iσΨ h̆(S)                          {#eq:iii-i11-1-1}

([[lem:iii-h-2-5]], [[eq:iii-h-2-6]]); here Ψ(σ, x) = ∫ e^(iσt_*) ∂_(t_*)χ_K dt_* is entire in σ with Ψ(0, ·) = 1,
L̂_b(σ)ĝ^aug(σ)(ḃ) = f̂_ḃ(σ), L̂_b(σ)ĥ^aug(σ)(S) = f̂_S(σ), and for Im σ > 0 these are the Fourier transforms of
χ_K ġ(ḃ) and of h^aug(S). Here ġ = ġ_b, h = h_(b,s1) and h̆ = h̆¹_(b,s1) are the states at b.

*Dictionary* ([[prop:iii-a-4-2]] and Steps 3–5 of the proof of [[prop:iii-i6-2-1]]). A zf-term |σ|^z(log|σ|)^m
corresponds to the K⁺-term t_*^(−z−1)(log t_*)^(≤m), and a zf-weight w to the K⁺-weight w + 1; a tf-weight (exponent) w
of û to the ι⁺-weight (exponent) w + 1 of u; the ι⁺-exponent ζ + 2 of a forcing to the tf-exponent ζ + 1 of its
transform; and the Taylor coefficient of order m at zf of a function of tf-weight w has weight w − m at ∂X. *Levels.*
At the Taylor level j (after j divisions by σ), a tf-exponent ζ of the current forcing corresponds to the u-exponent
ζ + j − 1, and a zero energy solution at level j with the exponent w at ∂X to the u-exponent w + j + 1. A row of
u-exponent λ has the K⁺-rate λ − 1 (s1), λ (s0, s2) or λ + d_τ (c0, c1).

*Constants.* Let α = 4 + ε_K − ε′ be admissible ([[def:iii-i10-1-3]]; 0 < ε′ < ε′_0 < ε_K, so α > 4). Fix
η_1, η_2 ∈ (ε_K, ε_+) with η_1 < η_2 such that no λ ∈ Λ has real part 2 + η_1 or 3 + η_2; they lie below ε_+, so that
every exponent treated has u-exponent below 3 + ε_+, where the forcing is polyhomogeneous and [[lem:iii-i10-1-2]] (c)
counts the logarithms. *The exclusion set of [[def:iii-i10-1-3]]* is the finite set of ε′ for which one of the
conditions [[eq:iii-g4-4-2]] of [[prop:iii-g4-4-4]] fails at the levels 1 and 2 below (for the finitely many α_0 treated
there, with ℓ_zf = α − 1 − j − ε), one of the conditions of [[prop:iii-g4-5-1]] fails at level 3 (finitely many rounds),
or α − 4 − ε is a real part excluded in [[lem:iii-i2-4-2]] or in [[eq:iii-h-1-1]]. Then ε > 0 is taken small, with
2ε < ε_+ − η_2, and off a finite set as well. The orders q_j ∈ (2, 3) of the zero energy solves are chosen off the real
parts of the exponents at hand.

*The a priori facts.* f^♭ is the forcing of [[prop:iii-i10-3-1]] (c) for f ∈ 𝒴⁰(α), and v is the forward solution of
L_b v = f^♭. In [[sec:iii-i11-3]], v = u − u_I − u_ι with u as in the hypothesis of [[lem:iii-i11-3-2]], so v has a
K⁺-weight w_v > 0 and the ι⁺-weight β′_+ ([[prop:iii-i10-3-1]] (a)–(b): u_I vanishes near K⁺, the rows of 𝒩_ι have
rates at least λ_♯ − 1 > 0, and the terms of u^rot_ι have K⁺-weight Re λ_0 − ε > 0).

**Lemma {#lem:iii-i11-1-1}** (The column terms.) On {r ≥ 1},

    f̂_ḃ(σ) = r⁻³G(σr, x),          f̂_S(σ) = r⁻³G(σr, x),

with G = G_ḃ, resp. G_S, linear in ḃ, resp. S, where G(ξ, x) = ∫_2^4 e^(iξs) F(s, x) ds and F is smooth in s, supported
in s ∈ [2, 4], and polyhomogeneous at ∂X with all its s-derivatives, with an index set ℰ_col ⊂ {Re ≥ 0} that depends
neither on ḃ, S nor on b ∈ ℬ̄_*. (On {r ≥ 1}, f_ḃ and f_S are supported in {2r ≤ t_* ≤ 4r}, by the proof of
[[lem:iii-h-2-2]] (b), and G is the function of [[eq:iii-h-2-3]] with f in place of f_∞.) Hence G(ξ, ·) is
polyhomogeneous with the index set ℰ_col, with coefficients and remainders entire in ξ and O(⟨ξ⟩^(−N)) on {Im ξ ≥ 0}
for every N; f̂_ḃ(0), f̂_S(0) ∈ 𝒜^(3+ℰ_col) near ∂X; and on X^±_(sc-b) near tf, where ρ_tf = r⁻¹ up to a factor smooth in
r̂ and σr = ±r̂, f̂_ḃ and f̂_S are polyhomogeneous at tf with the index set 3 + ℰ_col, smooth in r̂ up to zf, and rapidly
decaying at scf.

*Proof.* On {r ≥ 1}, χ_K = χ_c(r/t_*) ([[eq:iii-h-1-2]]), and L_b ġ(ḃ) = 0, L_b(t_*h(S) + h̆(S)) = 0
([[sec:iii-h-2]]); so there f = L_b(χ_K w) = [L_b, χ_K]w, with w = ġ(ḃ), resp. t_*h(S) + h̆(S). On sections a(t_*)w(x),
L_b = L_0 + L_1∂_(t_*) + L_2∂²_(t_*), with L_1 = [L_b, t_*] and L_2 = ½[[L_b, t_*], t_*] ([[sec:iii-i6-1]]), and
L_k ∈ ρ^(2−k)Diff^(2−k)_b(X̄) has smooth coefficients ([[lem:iii-i3-1-1]], as it is applied to them there). The
t_*-derivatives and the b-derivatives in x of χ_c(r/t_*) are sums of terms r^(−k)φ(t_*/r), k ∈ {0, 1, 2}, with φ smooth
and, when at least one derivative falls on χ_c, supported in [2, 4]; for instance r∂_r[χ_c(r/t_*)] =
(r/t_*)χ′_c(r/t_*) and ∂_(t_*)[χ_c(r/t_*)] = −r⁻¹(r/t_*)²χ′_c(r/t_*). So [L_b, χ_K]w is a finite sum of terms
r^(−k)φ(t_*/r)t_*^m (Qw_m)(x) with m ∈ {0, 1}, Q ∈ ρ^q Diff_b of smooth coefficients, and w_m among ġ(ḃ), h(S), h̆(S),
which are polyhomogeneous at ∂X: ġ_b(1, 0) ∈ 𝒜^((2,0)∪(2+ℰ_ind)) and ġ_b(0, Ȧ) ∈ 𝒜^((3,0)∪(3+ℰ_ind))
([[eq:iii-f3-2-2]]), h(S) ∈ 𝒜^((3,0)∪(3+ℰ_ind)) ([[eq:iii-f3-4-2]]), and h̆(S) is built from the tower of
[[prop:iii-d3-3-1]] (2) ([[lem:iii-i10-2-1]] (b)), whose index sets ℰ_ind contains ([[sec:iii-i8-1]]). With t_* = sr,
F(s, x) = r⁴f(sr, x) is a finite sum of terms φ(s)s^m r^(4−k+m)(Qw_m)(x): smooth in s, supported in [2, 4], and
polyhomogeneous in x with an index set E independent of ḃ and S. The index sets of the states do not depend on b
([[lem:iii-i15-1-1]] (P3)), and E is obtained from them by finitely many shifts by integers (the factors r^(4−k+m) and
the smooth coefficients of the L_k, which are smooth in b); so E can be taken independent of b ∈ ℬ̄_*. F is bounded
(by [[lem:iii-h-2-4]] (a) and its proof), so its coefficients at the exponents of real part below 0 vanish, and
ℰ_col := E ∩ {Re ≥ 0} serves. The statements on G follow by integrating the expansion of F against e^(iξs), with
integrations by parts in s for the decay in ξ (Im ξ ≥ 0, s > 0), and r⁻³G(σr, x) = ρ³_tf G(±r̂, x). ∎

### The lemmas of the spectral phase {#sec:iii-i11-2}

**Lemma {#lem:iii-i11-2-1}** (Zero energy with expansions.) Let q ∈ (2, 3), q′ ∈ (q, 5], and let
F ∈ H^(∞,(E,q′))_b(X̄) be partially polyhomogeneous at ∂X with an index set E, min Re E > q. Then
(û, ḃ, S) := L̃_b(0)⁻¹(F, 0, 0) ([[prop:iii-h-3-2]] at b, with its weight α_H := q − 4, so that α_H + 2 = q − 2 ∈ (0, 1)
is the L²-b-weight of a forcing of conormal order q) has û ∈ H^(∞,(E′,q′−2))_b(X̄), where E′ is the index set that
[[lem:iii-a-1-4]] builds from (E − 2) ∪ (1 + ℰ_col) and the indicial roots of L̂_b(0) ([[prop:iii-f1-2-3]]) with real
part in (q − 2, q′ − 2). Below the real part 3 the only such root is 2 (of type s0: the mass), so E′ lies in the extended
union of (E − 2) ∪ (1 + ℰ_col) and (2, l_*), plus ℕ₀; in u-exponents at level j these are Λ-valued
([[lem:iii-i10-1-2]]).

*Proof.* [[prop:iii-h-3-2]] at b ([[lem:iii-i15-1-1]] (P4)) gives û ∈ H^(∞,q−2)_b (conormal order q − 2, as in Step 3.1
of the proof of [[prop:iii-i6-2-1]]). Near ∂X, L̂_b(0) = ρ²A with A an elliptic b-operator ([[sec:iii-f1-2]], as the
proof of [[prop:iii-f4-5-1]] uses it), and L̂_b(0)û = F − f̂_ḃ(0) − f̂_S(0) there, with
f̂_ḃ(0), f̂_S(0) ∈ 𝒜^(3+ℰ_col) ([[lem:iii-i11-1-1]]). [[lem:iii-a-1-4]] with the weight q − 2 and with F replaced by ρ⁻²
times the right side (index set (E − 2) ∪ (1 + ℰ_col), remainder q′ − 2), applied finitely many times, each time from
the remainder order the previous application gave (each gains less than 1), gives the expansion up to q′ − 2. The
roots, which do not depend on b ((P2)): [[prop:iii-f1-2-3]] (a) (none in (0, 1]) and its list of decaying roots: 2 for
s0; 3, 1 + λ^Υ_(s1,2), 1 + λ^Υ_(s1,3) and 5 for s1; 3 and 4 for v1; l + 2 ≥ 4 and above for l ≥ 2; and
1 + λ^Υ_(s0,2) ∈ (3, 3 + z_Υ/3] and 4 for s0. ∎

**Lemma {#lem:iii-i11-2-2}** (One level.) Let j ∈ {0, 1, 2, 3} and g ∈ H^(∞,(5/2−ε,(E,κ),((0,0),z)))_b(X^±_(sc-b))
with z > 0, its zf-coefficient g(0) ∈ H^(∞,(E,κ))_b(X̄), and let (û, ḃ, S) be as in [[lem:iii-i11-2-1]] for F = g(0)
and q′ = κ (the same for both signs, or separately). Put

    g^(+1) := σ⁻¹(g − L̂_b(σ)(χ_zf û) − f̂_ḃ(σ) − f̂_S(σ)).                                             {#eq:iii-i11-2-1}

Then g^(+1) ∈ H^(∞,(5/2−ε,(E^(+1),κ−1),((0,0),z−1)))_b and

    E^(+1) ⊂ (E − 1) ∪ (E′ + 1) ∪ (2 + ℰ_col),

E′ the index set of û; its zf-coefficient is g_1 + iL_1û + (…), where g_1 is the σ¹-coefficient of g, and the exact
formula is

    g^(+1) = σ⁻¹(g − χ_zf g(0)) − σ⁻¹[L_0, χ_zf]û + iχ_zf L_1û + i[L_1, χ_zf]û + σχ_zf L_2û
             − σ⁻¹(f̂_ḃ(σ) + f̂_S(σ) − χ_zf(f̂_ḃ(0) + f̂_S(0))).

*Proof.* Exactly,

    L̂_b(σ)(χ_zf û) = χ_zf L_0û + [L_0, χ_zf]û − iσ(χ_zf L_1û + [L_1, χ_zf]û) − σ²χ_zf L_2û,

and L_0û + f̂_ḃ(0) + f̂_S(0) = g(0); this gives the formula. The terms: σ⁻¹(g − χ_zf g(0)) has the tf-index set E − 1
(division by σ = ρ_tf ρ_zf) and the zf-data ((0, 0), z − 1); the commutators are supported where r̂ ∼ 1, away from zf,
and by [[lem:iii-i3-1-1]] (b) both have the tf-index set E′ + 1 (E′ + 2 − 1 for σ⁻¹[L_0, χ_zf]û, and E′ + 1 for
[L_1, χ_zf]û, as L_1 ∈ ρDiff¹_b); χ_zf L_1û has E′ + 1, and σχ_zf L_2û has E′ + 1 (L_2 has no decay, and σ adds one at
tf); all are polynomial in σ at zf. The column terms: by [[lem:iii-i11-1-1]], on {r ≥ 1},
σ⁻¹(f̂(σ) − χ_zf f̂(0)) = r⁻²H(σr, x) with H(ξ, x) := (G(ξ, x) − χ(|ξ|)G(0, x))/ξ and χ_zf = χ(r̂), which is smooth in ξ
up to 0 (G is entire), polyhomogeneous in x with the index set ℰ_col, and rapidly decaying as |ξ| → ∞; near tf,
r⁻² = ρ²_tf and ξ = ±r̂, so this has the tf-index set 2 + ℰ_col, Taylor expansions at zf and rapid decay at scf. On
{r ≤ 2}, f̂_c is entire ([[lem:iii-h-2-4]] (a)), and χ_zf = 1 there for small |σ|, so that part is polynomial at zf.
The tf-weights: κ − 1, and q′_û + 1 = κ − 1, with q′_û = κ − 2 the remainder order of û; the columns are
polyhomogeneous. ∎

**Lemma {#lem:iii-i11-2-3}** (The pieces of the transition face model in compact sets.) Let u be the solution of
[[prop:iii-g4-4-4]] at b for a forcing whose leading term at tf is at (α_0, k) with k = 0 (for k > 0 apply the following
to the α_0-derivatives). Let R < 2/ρ_0. On {r ≤ R} and for 0 < ±σ ≤ c_R, χ_zf = 1 and χ_tf = χ_2(ρ + |σ|) = 0
([[sec:iii-g4-1]]), so u = |σ|^(α_0−2)u_b there, and

    |σ|^(α_0−2) u_b = Σ_τ c_τ(σ) T_τ(σ) + P_int(σ),                                                     {#eq:iii-i11-2-2}

where:

- T_s1(σ) := h^(≤3)_(b,s1)(σ, S^(−1)_1) = Σ_(i≤3) (−iσ)^i h̆^i_s1(S^(−1)_1) and c_s1(σ) := |σ|^(α_0−1)σ⁻²/(2 − α_0)
  (−|σ|⁻¹ log|σ| at α_0 = 2);
- T_v1(σ) := h^(≤2)_(b,v1)(σ, V^(−1)_1) = Σ_(i≤2) (−iσ)^i h̆^i_(b,v1)(V^(−1)_1), whose bottom h̆⁰_(b,v1) = h_(b,v1)
  vanishes at b_0 (every V Killing), and c_v1(σ) := −i sgn(σ)|σ|^(α_0−2)/(2 − α_0) (i sgn(σ) log|σ| at α_0 = 2): this
  is the term l_(2−α_0)(r̂)G_v1 of [[eq:iii-g4-4-4]] [[pending:issue-2]];
- for the other rows (μ, τ) of the table of roots of [[sec:iii-g2-1]], T_τ(σ) := h^((μ),≤c_μ)_(b,τ)(σ, Y^(μ)_τ) and
  c_τ(σ) := −|σ|^(α_0−2−μ)/β_μ(α_0), with |σ|^(⌊−μ⌋) log|σ| in place of the latter if β_μ(α_0) = 0, which for c0, c1
  happens at α_0 = 2 + μ ∈ (1, 2), and for the class rows in (−5/4, −1) and (−9/4, −2) at α_0 = 3 + μ and 4 + μ; here
  β_μ(α_0) = 2 − α_0 − {−μ} ([[eq:iii-g4-3-2]]);
- P_int is a finite sum of terms |σ|^m sgn(σ)^δ q(σ, x) with m ∈ ℤ, δ ∈ {0, 1} and q polynomial in σ (and in log r),
  without log|σ|: namely −|σ|⁻¹h(S^(−1)_1)/(2 − α_0) (for α_0 ≠ 2; at α_0 = 2 it is part of c_s1),
  i sgn(σ) r^(2−α_0) (h̆^(≤3)_(b,s1)(σ, S^(−1)_1) + T_v1(σ))/(2 − α_0) (with log r in place of r^(2−α_0)/(2 − α_0) at
  α_0 = 2), and |σ|^(⌊−μ⌋) r^(β_μ) T_τ(σ)/β_μ (with log r |σ|^(⌊−μ⌋) T_τ when β_μ = 0).

For larger R the tf-part adds log-free terms σ^j|σ|^k c(x) of integer degree and a zf-remainder of weight ℓ_zf + j; the
total χv̂ leaves no K⁺-tail from them by [[lem:iii-i10-2-4]] (b), although a sign-odd term σ^j|σ|^k c(x) alone has a
two-sided one, which is recorded in item (vi) of the proof of [[thm:iii-i12-3-1]]; so the conclusions below are
unchanged. The towers T_τ(σ) are the first sum of [[eq:iii-i10-2-3]] for the corresponding 1-form towers, without its
top term (−iσ)^(K+1) dt_* ⊗_s ω̆^K; the rows are unaffected, as that term has the rate e_ν + K + 1.

*Proof.* [[eq:iii-g4-4-4]] with l_β(r̂) = (|σ|^β r^β − 1)/β ([[def:iii-g4-2-3]]) and G^exc_s1 = −|σ|σ⁻²h(S),
G_s1 = |σ|iσ⁻¹h̆^(≤3)_(b,s1)(σ, S), G_v1 = |σ|iσ⁻¹h^(≤2)_(b,v1)(σ, V), G_(μ,τ) = |σ|^(−μ)h^((μ),≤c_μ)_(b,τ)(σ, Y)
([[lem:iii-g4-4-3]], which holds at b by (P4)). The s1 and v1 terms: |σ|^(α_0−2)(−l_(2−α_0)(|σ|)|σ|σ⁻²h +
l_(2−α_0)(r̂)|σ|iσ⁻¹(h̆^(≤3) + T_v1)) equals (2 − α_0)⁻¹ times

    −|σ|⁻¹h + |σ|^(α_0−1)σ⁻²h + i sgn(σ) r^(2−α_0)(h̆^(≤3) + T_v1) − i|σ|^(α_0−1)σ⁻¹(h̆^(≤3) + T_v1),

as |σ|σ⁻¹ = sgn(σ); and |σ|^(α_0−1)σ⁻²(h − iσh̆^(≤3)) = c_s1(2 − α_0)h^(≤3)(σ, S) (the definition in
[[eq:iii-g4-5-2]]), while −i|σ|^(α_0−1)σ⁻¹ = (2 − α_0)c_v1. At α_0 = 2, l_0(r̂) = log|σ| + log r. The other rows:

    |σ|^(α_0−2−μ) l_(β_μ)(r̂) = (|σ|^(α_0−2−μ+β_μ) r^(β_μ) − |σ|^(α_0−2−μ))/β_μ,     α_0 − 2 − μ + β_μ = ⌊−μ⌋.

At β = 0, l_0(r̂) = log|σ| + log r. The towers: [[def:iii-g4-4-1]] defines them as Σ_j (−iσ)^j h̆^((μ),j)_b with the
companions of [[sec:iii-g2-2]], which are those of [[lem:iii-i10-2-1]] (b) (for s0 with the shift of index). ∎

**Lemma {#lem:iii-i11-2-4}** (The column pieces.) For ḃ ∈ 𝔟_ℂ, S ∈ 𝒮_(1,ℂ) and j ∈ ℕ₀, the distributions
σ^j ĝ^aug(σ)(ḃ) and σ^j ĥ^aug(σ)(S) on ℝ (boundary values from Im σ > 0) are the Fourier transforms of
(i∂_(t_*))^j(χ_K ġ(ḃ)) and (i∂_(t_*))^j h^aug(S). In {r ≤ R}, for large t_*: the first is χ_K ġ(ḃ) for j = 0 and
vanishes for j ≥ 1; the second is t_*h(S) + h̆(S) for j = 0, ih(S) for j = 1, and vanishes for j ≥ 2. If ḃ(σ), S(σ) lie
in H^(∞,a)_b(±(0, c], |dσ/σ|), then χσ^j ĝ^aug(ḃ(σ)) and χσ^j ĥ^aug(S(σ)) have inverse transforms of K⁺-weight a + j and
a + j − 1, and of ι⁺-weight 3/2 − ε.

*Proof.* [[lem:iii-h-2-5]] (a) and ∂_(t_*) ↔ −iσ; χ_K = 1 near K⁺ in {r ≤ R}, and h^aug(S) = χ_K(t_*h(S) + h̆(S))
([[sec:iii-h-2]]). The last statement is [[lem:iii-i2-4-3]] with a for their classes on X^±_(sc-b), and
[[prop:iii-a-4-2]] (2) for the inverse transforms: ĝ^aug carries σ⁻¹ and ĥ^aug carries σ⁻², which give the weights
a + j − 1 + 1 and a + j − 2 + 1. ∎

**Lemma {#lem:iii-i11-2-5}** (The decomposition.) Let f̂ ∈ H^(∞,(5/2−ε,κ,((0,0),z)))_b on ±(0, c], and suppose that
f̂ = Σ_(i∈I) L̂_b(σ)P_i + σ^J g_J on 0 < |σ| ≤ c, where each P_i(σ) lies in the space 𝒳′_σ of [[lem:iii-i6-1-2]] for
σ ≠ 0 (a section smooth on X° and b-conormal at ∂X, or a sum of terms ĝ^aug and ĥ^aug), and let
(û_f, ḃ_f, S_f) := L̃_b(σ)⁻¹(g_J, 0, 0). Then the outgoing inverse satisfies, for 0 < |σ| ≤ c,

    L̂_b(σ)⁻¹f̂ = Σ_i P_i + σ^J(û_f + ĝ^aug(σ)(ḃ_f) + ĥ^aug(σ)(S_f)).                                   {#eq:iii-i11-2-3}

*Proof.* Apply L̂_b(σ): the right side maps to Σ_i L̂_b P_i + σ^J(L̂_b û_f + f̂_(ḃ_f) + f̂_(S_f)) = f̂, by
[[lem:iii-h-2-5]] (c) and the first component of L̃_b(σ)(û_f, ḃ_f, S_f) = (g_J, 0). Every term lies in 𝒳′_σ
([[lem:iii-h-2-5]] (b), [[lem:iii-i6-1-2]]), on which L̂_b(σ) is injective, and L̂_b(σ)⁻¹f̂ is the element of
𝒳_σ ⊂ 𝒳′_σ with this image. ∎

The rows r(·) and the columns of L̃_b thus enter only through the zero energy solves ([[lem:iii-i11-2-1]]) and the last
level; no assembly of the augmented components, as in [[eq:iii-i6-2-8]] and [[eq:iii-i8-3-3]], is needed.

### The spectral phase and the expansion below the order α − 2 {#sec:iii-i11-3}

This section is [Hin26, Theorem 11.59, Steps 2.A.3–2.A.8 and Part 3 of the proof] in dimension 4 + 1.

**Proposition {#prop:iii-i11-3-1}** (The spectral phase.) Let α > 4 be admissible, and let f^♭ and v be as in
[[sec:iii-i11-1]]. There are S_ν ∈ 𝒲_(τ,ℂ), ν ∈ 𝒩_σ, linear and continuous in f, and a finite sum v^rot of v1 towers
χ_K Σ_(i≤2) a^((i)) h̆^i_(b,v1)(Y), with a polyhomogeneous of exponents (α_0, l), Re α_0 = 2, and Y ∈ 𝒱_(1,ℂ) linear
and continuous in f, such that

    v − Σ_(ν∈𝒩_σ) m_ν(S_ν) − v^rot ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,α−2−ε)_b(Ω_*)^(•,−).               {#eq:iii-i11-3-1}

The terms of v^rot have K⁺-weight 2 − ε, and 3 − ε > α − 2 when h_(b,v1) = 0; in that case, in particular at b_0,
v^rot may be put into the remainder.

*Proof.* *Step 0 (decomposition and transform; Step 3 of the proof of [[prop:iii-i6-2-1]]).* Write
v = v_hi + v_low with ℱv_low = χ(|σ|)v̂. [[lem:iii-i2-4-1]] (with β^f_I = ℓ_I, β_ι = w_+ − 2 − ε, β_K = α − ε;
ℓ_I + 1 ≥ w_+ − ε − (1 − ε_1) by (H4)) gives v_hi ∈ H^(∞,(3/2−ε,j,j))_b(M′) for every j. [[prop:iii-a-4-2]] (1) with
β_I = ℓ_I + 1, β_ι = w_+ − ε, E_ι = ℰ^♭ + 2, E_I = ∅, β_K = α − ε, E_K = ∅ (its condition [[eq:iii-a-4-2]],
ℓ_I + 1 > w_+ − 1 − ε, holds by (H4)) gives

    g_0 := f̂^♭|_(±(0,c]) ∈ H^(∞,(5/2−ε,(ℰ^♭+1,w_+−1−ε),((0,0),α−1−ε)))_b,

with tf-exponents of real part at least 3 and u-exponents (level 0) in Λ. We construct pieces P_i and g_J, J = 3, as in
[[lem:iii-i11-2-5]].

*Step 1 (level 0; [Hin26, Step 2.A.3]).* [[lem:iii-i11-2-1]] with q_0 := 3 − ε, q′ := w_+ − 1 − ε and F = g_0(0) gives
(û_0, ḃ_0, S_0), the same for both signs; û_0 has the exponents (ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·) (and their
ℕ₀-shifts) below q′ − 2 = 2 + ε_+ − ε, the root 2 being the mass. S_0 = 0 by the argument of Step 3.1 of the proof of
[[prop:iii-i6-2-1]] (f^♭ lies in the space of Step 3 of the proof of [[prop:iii-i5-2-1]], and v has K⁺-weight above
−1). Pieces: χ_zf û_0 and ĝ^aug(ḃ_0). [[lem:iii-i11-2-2]] gives g_1, with tf-exponents of real part at least 2,
u-exponents in Λ (level 1), tf-weight 3 + ε_+ − ε, and zf-data ((0, 0), α − 2 − ε).

*Step 2 (level 1; [Hin26, Steps 2.A.4–2.A.5]).* For each tf-exponent (α_0, k) of g_1 with 2 ≤ Re α_0 < 2 + η_1 (finitely
many), [[prop:iii-g4-4-4]] with ℓ_zf := α − 2 − ε and ℓ_scf := 3/2 − ε applies (admissibility) to the corresponding
term, with its whole tf-coefficient, and gives u_((α_0,k)); the pieces are σu_((α_0,k)). The remainder
g_1 − Σ L̂_b(σ)u_((α_0,k)) has tf-exponents in ((α_0, k) + ℰ_ind) ∪ ((4, k + 1) + ℱ) ([[eq:iii-g4-4-3]]), of real part
at least 2 + ε_ind > 2 + η_1, and the other exponents of g_1, at least 2 + η_1 by the choice of η_1; the zf-data are
unchanged. [[lem:iii-i11-2-1]] with q_1 := 2 + η_1 and q′ := 3 + ε_+ − ε on its zf-coefficient (both signs separately)
gives (û_1, ḃ_1, S_1)^±, with the pieces σ(χ_zf û_1 + ĝ^aug(ḃ_1) + ĥ^aug(S_1)); and [[lem:iii-i11-2-2]] gives g_2, with
tf-exponents of real part at least 1 + η_1 (those of û_1, at least η_1, plus one; those of the remainder, at least
2 + η_1, minus one; the columns' 2 + ℰ_col), tf-weight 2 + ε_+ − ε, and zf-data ((0, 0), α − 3 − ε).

*Step 3 (level 2; [Hin26, Steps 2.A.6–2.A.7]).* For each tf-exponent (α_0, k) of g_2 with
1 + η_1 ≤ Re α_0 < 2 + η_2, [[prop:iii-g4-4-4]] with ℓ_zf := α − 3 − ε; its remainder exponents α_0 + ℰ_ind may again
lie below 2 + η_2, and are treated in turn (finitely many rounds, the real parts rising by at least ε_ind); (4, k + 1)
lies above. The pieces are σ²u_((α_0,k)). Then [[lem:iii-i11-2-1]] with q_2 := 2 + η_2 and q′ := 2 + ε_+ − ε gives the
pieces σ²(χ_zf û_2 + ĝ^aug(ḃ_2) + ĥ^aug(S_2)), and [[lem:iii-i11-2-2]] gives g_3, of tf-weight κ_3 := 1 + η_2 − 2ε
(conormal; its expansion is not needed) and zf-data ((0, 0), ℓ_3), ℓ_3 := α − 4 − ε ∈ (0, ε_K).

*Step 4 (level 3; [Hin26, Step 2.A.8 and Part 3]).* Fix δ > 0 with δ + ℓ_3 + 2ε < ε_ind. While the tf-weight κ of the
current level-3 forcing is at most 2 + ℓ_3 + ε, apply [[prop:iii-g4-5-1]] with α_κ := min(κ, 2 − δ) ∈ (1, 2) (the
forcing has the tf-weight α_κ), ℓ_zf := ℓ_3, the order 0 of the zf-index set there, and w = ℓ_3 − α_κ + 2 ∈ (0, 1)
(α_κ ≥ κ_3 > 1 + ℓ_3, as η_2 > ε_K > ℓ_3). Its conditions w ≠ −μ and 2 − α_κ + j ≠ −μ hold for ε off a finite set
(admissibility) and, when α_κ = 2 − δ, for δ off the finite set {−μ − j}, which we impose on δ. It gives

    u = χ_zf u_b + χ^♯_tf ũ ∈ H^(∞,(3/2−2ε,α_κ−2,α_κ−3))_b

with a remainder of tf-weight α_κ + ε_ind − ε, which exceeds κ by ε_ind − ε when α_κ = κ, and, when α_κ = 2 − δ < κ,
exceeds 2 + ℓ_3 + ε (as δ + ℓ_3 + 2ε < ε_ind), after which the loop ends; the pieces are σ³u. After finitely many
rounds κ > 2 + ℓ_3 + ε; lowering κ if necessary (a forcing of tf-weight κ has every smaller tf-weight),
κ ∈ (2 + ℓ_3 + ε, 3). [[lem:iii-i11-2-1]] with q_3 := κ − ε, q′ := κ and E = ∅ gives (û_3, ḃ_3, S_3)^± and the pieces
σ³(χ_zf û_3 + ĝ^aug(ḃ_3) + ĥ^aug(S_3)). The rest,

    g_J := (the level-3 source) − L̂_b(σ)(χ_zf û_3) − f̂_(ḃ_3) − f̂_(S_3) ∈ H^(∞,(5/2−ε,κ−ε,ℓ_3))_b

(the zf-coefficient is removed, the next Taylor order being 1; tf as in the proof of [[lem:iii-i11-2-2]], without
the division), is inverted by [[lem:iii-i2-4-2]] with β_scf := 3/2 − 2ε, β_tf := κ − 2 − ε, β_zf := ℓ_3,
β_tf − β_zf ∈ (0, 1):

    û_f ∈ H^(∞,(3/2−3ε,κ−2−ε,ℓ_3))_b,          ḃ_f, S_f ∈ H^(∞,ℓ_3)_b(±(0, c], |dσ/σ|).

*Step 5 (matching, and the pieces at K⁺).* By [[lem:iii-i11-2-5]], on 0 < |σ| ≤ c, v̂ is the sum of the pieces and of
σ³(û_f + ĝ^aug(ḃ_f) + ĥ^aug(S_f)). The data at the levels 1–3 were found for each sign; write S^±_1 = S_e ± S_o.

*Matching* (as in Step 5 of the proof of [[prop:iii-i6-2-1]], and [Hin26, p. 287]). Multiplied by σ, every piece is
bounded near σ = 0: σ · σĥ^aug(S^±_1) = −G_2(σ)(S^±_1) and σ · σĝ^aug(ḃ^±_1) = iσΨġ(ḃ^±_1) by [[eq:iii-i11-1-1]];
σĝ^aug(ḃ_0) = iΨġ(ḃ_0); the columns of the levels 2–3 carry σ^(≥2); and the other pieces have degree at least 0
([[lem:iii-i11-2-3]]: σ^(j+1)c_τ(σ) has degree at least α_0 − 2 + j ≥ 0, and σ^(j+1)P_int degree at least j ≥ 1) or
zf-weight above 0 (Step 4, the last level). So ℱ(∂_(t_*)v_low) = −iσχv̂ and −iσχ times the sum differ by a
distribution supported at 0, whose inverse transform, a polynomial, tends to 0 as t_* → −∞
(∂_(t_*)v_low = −∂_(t_*)v_hi = O(|t_*|^(−∞)) there, as v = 0 for t_* < 1; the other by the Riemann–Lebesgue lemma), and
so vanishes. Near σ = 0, −iσχ times the sum is iχ sgn(σ)h(S_o) (G_2(0) = h, [[lem:iii-h-2-5]] (b)) plus terms whose
inverse transforms have K⁻-weight above 1 in {r ≤ R}: the sign-even part of iG_2(σ)(S^±_1) and Ψġ(ḃ_0) (the
−iσ-multiples of the terms above) are smooth in σ; every other piece times σ is, in {r ≤ R}, a sum of terms
sgn(σ)^δ|σ|^z(log|σ|)^m times smooth sections with Re z > 0 ([[lem:iii-i11-2-3]], with χ_zf = 1 there for
|σ| ≤ c_R), whose inverse transforms are O(|t_*|^(−1−Re z) log^m), or of zf-weight above 0 ([[prop:ii-g1-3-5]] (1)).
The inverse transform of χ sgn(σ) is c t_*⁻¹(1 + o(1)) as t_* → −∞, with c ≠ 0. Hence h(S_o) = 0 on {r ≤ R}, so S_o = 0
([[eq:iii-h-3-1]]), and S_1 is the same for both signs. We then read the pieces of v̂ itself, the column pieces with
constant coefficients as boundary values ([[lem:iii-i11-2-4]]) and the others as locally integrable functions: as
before, χv̂ and χ times their sum differ by a distribution supported at 0, a polynomial in t_* after inverse transform,
which tends to 0 as t_* → −∞ (v_low = −v_hi there, the column pieces with constant coefficients vanish there as
χ_K = 0, and the others by Riemann–Lebesgue), and so vanishes. We sort the inverse transforms in {r ≤ R}, for large
t_*:

(i) *Zero energy pieces* σ^j χ_zf û^±_j: in {r ≤ R}, χ_zf = 1 for |σ| ≤ c_R, so they are sgn(σ)^δ times polynomials in
σ there (the data of the levels 1–3 may depend on the sign): of integer degree, with no log|σ|.

(ii) *Column pieces* ([[lem:iii-i11-2-4]]): χ_K ġ(ḃ_0) from level 0; ih(S_1) from σĥ^aug(S_1) at level 1 (S_1 being
independent of the sign); σĝ^aug(ḃ^±_1) = iΨġ(ḃ_e) ± iΨġ(ḃ_o), whose first part contributes nothing for large t_* and
whose second is sgn(σ) times a function smooth in σ (integer degree, no log|σ|); and at the levels 2 and 3 the
sign-even parts contribute nothing for large t_*, the sign-odd parts being again sgn(σ) times smooth functions of σ.

(iii) *The last level.* σ³û_f has zf-weight ℓ_3 + 3; σ³ĝ^aug(ḃ_f) and σ³ĥ^aug(S_f) give the K⁺-weights ℓ_3 + 3 and
ℓ_3 + 2 = α − 2 − ε ([[lem:iii-i11-2-4]]); the level-3 pieces of Step 4 have zf-weight α_κ − 3 + 3 ≥ κ_3 =
1 + η_2 − 2ε, so K⁺-weight at least 2 + η_2 − 2ε > α − 2 (η_2 > ε_K), by [[prop:iii-a-4-2]] (2) (on {r ≤ R},
[[prop:ii-g1-3-5]] (1)).

(iv) *The transition face pieces at the levels 1 and 2*, by [[lem:iii-i11-2-3]]: σ^j(Σ_τ c_τ(σ)T_τ(σ) + P_int(σ)).
The terms of σ^jP_int are, in {r ≤ R}, finite sums of |σ|^m sgn(σ)^δ times polynomials in σ, with m + j ≥ 0 (m ≥ −1,
j ≥ 1): of integer degree, with no log|σ|. The terms σ^jc_τ(σ)(−iσ)^i h̆^i_τ have the degree α_0 − 3 + j + i for s1
(c_s1 has degree α_0 − 3), α_0 − 2 + j + i for v1 (c_v1 has degree α_0 − 2), and α_0 − 2 − μ + j + i for the other
rows, with log|σ| at integer degree when α_0 or β_μ is critical.

Now apply [[lem:iii-i10-2-4]] to χv̂ in {r ≤ R} (V = C^∞({r ≤ R})), with β := α − 3 − 2ε (ε off a finite set, so that
β ∉ ℕ₀); the hypothesis as t_* → −∞ holds as above (v is forward). The terms of (i), the sign-odd column pieces of
(ii), those with j ≥ 1 in ĝ^aug and j ≥ 2 in ĥ^aug, and σ^jP_int have integer degree and no log|σ|, so they contribute
no tail (its (b)); (iii) contributes O(t_*^(−α+2+3ε)), as σ³ĥ^aug(S_f) has zf-weight ℓ_3 + 1 = α − 3 − ε > β. So, for
large t_* in {r ≤ R},

    v = χ_K ġ(ḃ_0) + ih(S_1) + Σ_(pieces (iv)) Σ_i (𝒯_+c_τ)^((i))(t_*) h̆^i_τ + O(t_*^(−α+2+3ε)),

where 𝒯_+c is the tail as t_* → +∞ of the forward part of σ^jc(σ) ([[lem:iii-i10-2-4]] (b): a combination of
t_*^(−z−1)(log t_*)^l, with z = α_0 − 3 + j for s1, α_0 − 2 + j for v1 and α_0 − 2 − μ + j otherwise), and the
derivatives come from (−iσ)^i ↔ ∂^i_(t_*), as (σ + i0)^z σ^i = (σ + i0)^(z+i): the tail of a tower piece is the tower
Σ_i a^((i)) h̆^i_τ of a := 𝒯_+c.

*Step 6 (the stationary terms and the rows).* v has K⁺-weight w_v > 0, and every other term above decays
(Re z + 1 > 0); so the stationary tensor ġ(ḃ_0) + h(iS_1) (S_1 being independent of the sign by Step 5) vanishes, and
ḃ_0 = 0, S_1 = 0 ([[eq:iii-h-3-1]]), as in Step 6 of the proof of [[lem:iii-i8-3-2]]. The towers: at level 1 (j = 1,
2 ≤ Re α_0 < 2 + η_1, u-exponent α_0) the s1 tower has the rate α_0 − 1 and is the row (s1, α_0, ·); the s0 and s2
towers have the rate α_0, below α − 2 only for Re α_0 = 2 by (G) (the rows (s0, 2, ·), (s2, 2, ·)); the c0, c1 towers
have the rate α_0 + d_τ > 2 + ε_K by (G); the rows outside 𝒯 have rate at least α_0 + 1; and the v1 tower, whose
coefficient a = 𝒯_+c_v1 has the exponents (α_0 + j − 1, ·) = (α_0, ·), has the rate α_0 through its bottom
a h_(b,v1)(V^(−1)_1), and the rate α_0 + 1 when h_(b,v1) = 0. By (G) the v1 towers with Re α_0 > 2 have rate above
2 + ε_K ≥ α − 2; those with Re α_0 = 2 form v^rot. At level 2 (u-exponent α_0 + 1, of real part in [2 + η_1, 3 + η_2))
only the s1 tower can have a rate α_0 < 2 + ε_K, and by (G) then Re(α_0 + 1) ≤ 3; the s0, s2 and v1 towers have rate
at least α_0 + 1 ≥ 2 + η_1 > 2 + ε_K. So the towers of rate below α − 2, other than those of v^rot, are those of the
rows of 𝒩_σ, with (λ, k) ∈ ℰ_par by [[lem:iii-i10-1-2]] (c). By [[lem:iii-i10-2-1]], each such tower is m_ν(S_ν) in
{r ≤ R} for large t_*, up to the terms with a^((i)), i ≥ 4 (s1), i ≥ 3 (s0, s2), of rate at least
Re e_ν + 3 > α − 2; and the towers of rate at least α − 2 are O(t_*^(−α+2+3ε)). Hence
v − Σ_(ν∈𝒩_σ) m_ν(S_ν) − v^rot = O(t_*^(−α+2+3ε)) in {r ≤ R}, with all t_*∂_(t_*)- and spatial derivatives.

*Step 7 (joint weights).* The sum of the pieces other than the columns with constant coefficients lies, on each half, in
a space H^(∞,(3/2−3ε,(E_tf,β′_+−1),((0,0)∪̄(E_K−1),α−3−ε)))_b, with E_K the K⁺-exponents of Step 5 (the polyhomogeneous
zf-terms of the u of [[prop:iii-g4-4-4]], with coefficients polyhomogeneous at tf by [[lem:iii-g4-4-3]] and
[[eq:iii-g4-4-4]], and the zero energy pieces), and the matching condition [[eq:iii-a-4-4]] of [[prop:iii-a-4-2]] holds,
by [[lem:iii-i10-2-4]] (a) applied to the zf-coefficients in {r ≤ R} for every R. [[prop:iii-a-4-2]] (2) gives v_low
(minus the stationary columns, which vanish) in H^(∞,3/2−4ε,(E_ι,β′_+),(E_K,α−2−ε))_b(M′). Its K⁺-coefficients are
functions on K⁺ determined in K⁺ ∩ {r ≤ R} by Step 6, where they equal those of Σ_(𝒩_σ) m_ν(S_ν) + v^rot, which is
itself partially polyhomogeneous at K⁺ with these coefficients ([[lem:iii-i9-2-2]] (b), (e), [[eq:iii-i9-2-1]]). So
v − Σ m_ν(S_ν) − v^rot has K⁺-weight α − 2 − ε. Its ι⁺-weight is β′_+ (v, the m_ν and the terms of v^rot have it), and
its ℐ⁺-data are those of v: near ℐ⁺, χ_K = 0, and [[prop:iii-i1-2-1]] applies as in Step 8 of the proof of
[[lem:iii-i8-3-2]]. *Linearity and continuity:* every map used is linear and bounded ([[lem:iii-i11-2-1]]–
[[lem:iii-i11-2-5]], [[prop:iii-g4-4-4]], [[prop:iii-g4-5-1]], [[lem:iii-i2-4-1]]–[[lem:iii-i2-4-3]],
[[prop:iii-a-4-2]]), and the S_ν and the coefficients of v^rot are coefficients of the tails. ∎

**Lemma {#lem:iii-i11-3-2}** (The expansion; [Hin26, Theorem 11.59, Parts 1–3, the extraction].) Let α > 4 be
admissible, let (h, p⃗) be a base point with black hole parameter b ∈ ℬ̄_*, with p⃗ ∈ 𝒫 and h ∈ 𝒳^∞ small, and let
G ∈ 𝒴⁰(α). Suppose that the forward solution u of L_(h,p⃗)u = G lies in
⋂_ε H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,w_0−ε)_b(Ω_*)^(•,−) with w_0 > 0, w_0 + a_K > α and β′_+ ∈ (3/2 − (δ_♯ − ε_+), 3/2). Then

    u = Σ_(ν∈𝒩) m_ν(S_ν) + u^rot + ũ,     ũ ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α−2−ε)_b(Ω_*)^(•,−)        {#eq:iii-i11-3-2}

for every β_+ < min(3/2, min Re ℰ_+). Here u^rot := u^rot_ι + v^rot is the sum of the v1 terms of
[[prop:iii-i10-3-1]] and [[prop:iii-i11-3-1]] for the forcing f′ of the proof, and the coefficients
S_ν = S^(h,p⃗)_ν(G) ∈ 𝒲_(τ,ℂ) are determined by u − u^rot ([[cor:iii-i10-2-3]]); u^rot and the S_ν are
conjugation-symmetric, linear and continuous in G, with bounds uniform for (h, p⃗) small and b ∈ ℬ̄_*. When h_(b,v1) = 0,
in particular at b_0, u^rot has K⁺-weight α − 2 − ε and is put into ũ.

*Proof.* *Step 0.* Put f′ := G − (L − L_b)u, which equals L_b u. By [[prop:iii-i-4-1]] ([[eq:iii-i-4-2]]), for
L = L_(h,p⃗) ([[lem:iii-i9-2-5]]), (L − L_b)u has the ℐ⁺-data (⟨ℰ^C_I + 1⟩′, ℓ_I + 1), the plain ι⁺-weight
β′_+ + 2 + λ_♯ − ε > w_+ (as β′_+ > 3/2 − δ_♯ + ε_+, and m_+ = λ_♯ by (H1)), and the K⁺-weight
w_0 − ε + a_K ≥ α − ε. So f′ ∈ 𝒴⁰(α) for ε < w_0 + a_K − α, and L_b u = f′.

*Steps 1–2.* [[prop:iii-i10-3-1]] gives u_I, u_ι, (S_ν)_(𝒩_ι), u^rot_ι and f^♭; v := u − u_I − u_ι is the forward
solution of L_b v = f^♭ and has the K⁺-weight min(w_0, λ_♯ − 1) − ε > 0.

*Step 3.* [[prop:iii-i11-3-1]] gives (S_ν)_(𝒩_σ) and v^rot. Summing gives [[eq:iii-i11-3-2]] with the ι⁺-weight
min(β′_+, λ_♯) − ε; the weight β_+ for every β_+ < min(3/2, min Re ℰ_+) follows as in [[lem:iii-i8-3-2]] (the ι⁺-terms
of ũ below 3/2 are those of u, by Step 1 of the proof of [[prop:iii-i5-2-1]] with ℓ̆_+ < 3/2).

*Determination.* If two such expansions hold with the same u^rot, their difference is a sum of m_ν of K⁺-weight
α − 2 − ε, which is 0 by [[cor:iii-i10-2-3]] (Re e_ν ≤ 2 < α − 2). *Reality:* u is real, m_ν̄(W̄) is the conjugate of
m_ν(W), and the expansion is unique. *Bounds:* every map is linear and bounded, uniformly by [[lem:iii-i9-2-5]]. ∎

Since f′ = L_b u, the coefficients S_ν and u^rot are linear functions of u.

**Lemma {#lem:iii-i11-3-3}** (The coefficients near the reference point.) Fix b ∈ ℬ̄_* and let p⃗_b ∈ 𝒫 be the
parameter whose only nonzero component is b − b_0. In [[lem:iii-i11-3-2]], if (h_j, p⃗_j) → (0, p⃗_b), G_j → G in
𝒴⁰(α), and the forward solutions u_j of L_(h_j,p⃗_j)u_j = G_j and u of L_(0,p⃗_b)u = G satisfy the hypothesis with the
same w_0 and β′_+, the u_j being bounded there, then S^(h_j,p⃗_j)_ν(G_j) → S^(0,p⃗_b)_ν(G). At b_0, p⃗_(b_0) = 0 and
L_(0,0) = L_(b_0).

*Proof.* As in [[lem:iii-i8-3-3]], with L_(0,p⃗_b) as the reference operator: u_j − u is the forward solution of
L_(0,p⃗_b)(u_j − u) = R_j := G_j − G − (L_j − L_(0,p⃗_b))u_j, and R_j → 0 in 𝒴⁰(α) (the count of Step 0 of the proof of
[[lem:iii-i11-3-2]], with coefficients o(1); near K⁺ both backgrounds equal g_b, [[lem:iii-i-3-6]], so
L_j − L_(0,p⃗_b) gains a_K there). The coefficients are linear functions of the solution, so
S^(h_j,p⃗_j)_ν(G_j) − S^(0,p⃗_b)_ν(G) = S^(0,p⃗_b)_ν(R_j) → 0. ∎

### Elimination {#sec:iii-i11-4}

This section is [Hin26, Theorem 11.59, Step 2.B and Part 3 of the proof, (11.222)] in dimension 4 + 1, at base points
with black hole parameter b_0. For an admissible α′ ∈ (2, 3) ([[sec:iii-i8-1]]), 𝒫_(α′) is the space of
[[sec:iii-i8-4]] (the parameters p⃗_(≤0) and the motions of K⁺-rate below α′ − 2), and

    𝒩′ := 𝒩 ∖ {(s1, λ, k) : (λ, k) ∈ ℳ_(α′)},

the rows of [[sec:iii-i9-1]] not in 𝒫_(α′). For W⃗ = (W_ν)_(ν∈𝒩′), conjugation-symmetric, write
D_(p⃗)P_4(h, p⃗)(W⃗) := Σ_(ν∈𝒩′) f^ν_(h,p⃗)(W_ν), and 𝒫^full for 𝒫_(α′) ⊕ {W⃗}, which is the space 𝒫 of
[[sec:iii-i9-1]].

**Theorem {#thm:iii-i11-4-1}** ([Hin26, Theorem 11.59, Parts 1–3: (11.222)], in dimension 4 + 1.) Let α > 4 be
admissible, and let (h, p⃗) be a base point with black hole parameter b_0, with p⃗ ∈ 𝒫 and h ∈ 𝒳^∞ small. For every
F ∈ 𝒴⁰(α) there is a unique p⃗′ = p⃗′_(h,p⃗)(F) ∈ 𝒫 such that the forward solution of

    L_(h,p⃗)u = F − D_(p⃗)P_4(h, p⃗)(p⃗′)                                                               {#eq:iii-i11-4-1}

satisfies

    u ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,α−2−ε)_b(Ω_*; S²T*)^(•,−)
        for every β_+ < min(3/2, min Re ℰ_+).                                                           {#eq:iii-i11-4-2}

Moreover p⃗′_(h,p⃗) is linear, with bounds uniform for (h, p⃗) small, and continuous at (0, 0) as in
[[prop:iii-i8-4-1]] (ii). In compact spatial sets u = O(t_*^(−2−ε_K+ε′+ε)); letting ε′ → 0 along admissible values,
this is [Hin26, (11.222)] at K⁺, with the plain ι⁺-weight β_+. Its ι⁺-index set is part of [[thm:iii-i12-3-1]].

*Proof.* Fix an admissible α′ ∈ (2, 3). [[eq:iii-i8-4-2]] holds for every β_+ < 3/2, so β′_+ can be taken in
(3/2 − (δ_♯ − ε_+), 3/2), and w_0 := min(α′ − 2, λ_♯ − 1) satisfies w_0 + a_K > α (a_K ≥ 4 + ε_K by (H2), and
w_0 > 0).

*[[prop:iii-i8-4-1]] for P_4.* That proposition is stated for P_3 at (h, p⃗_3). For p⃗ ∈ 𝒫 with row components
(W_ν)_(ν∉ℳ) put h′ := h + Σ_(ν∉ℳ) h_ν(W_ν), in 𝒳^∞ and small ([[lem:iii-i9-2-5]]). Then L_(h,p⃗) is the linearised
operator of P_3 at (h′, p⃗_3) ([[lem:iii-i9-2-5]]), and in the directions S, b, S⁽⁰⁾_1 the derivatives D_(p⃗)P_4(h, p⃗)
and D_(p⃗)P_3(h′, p⃗_3) differ by (∂δ*_(g_0,E_C))ϑ_rows ([[lem:iii-i9-2-6]] (a)), which is linear in the direction,
lies in 𝒴_2(α) ⊂ 𝒴(α′) and is O(|W⃗|); in the directions of the motions they agree. So the finite-dimensional maps of
the base and induction steps of [[prop:iii-i8-4-1]] stay within O(|W⃗|) of ± the identity, and that proposition, with
(i)–(ii), holds for (L_(h,p⃗), D_(p⃗)P_4) at small p⃗; this is the form used below.

*The map.* For W⃗ put F(W⃗) := F − D_(p⃗)P_4(h, p⃗)(W⃗); by [[lem:iii-i9-2-6]] (b) it lies in the space 𝒴(α′) of
[[sec:iii-i8-1]], so [[prop:iii-i8-4-1]] gives q⃗(W⃗) := p⃗′_(h,p⃗,α′)(F(W⃗)) ∈ 𝒫_(α′), and the forward solution u(W⃗) of

    L_(h,p⃗)u(W⃗) = F(W⃗) − D_(p⃗)P_4(h, p⃗)(q⃗(W⃗))

lies in [[eq:iii-i8-4-2]] at α′. Write D_(p⃗)P_4(q⃗) = f^S(q_S) + f^b(q_b) + f^s1(q_s1) + Σ_(ν∈ℳ_(α′)) f^ν(q_ν), and use
[[lem:iii-i9-2-6]] (c), f^ν = L_(h,p⃗)m_ν + r^ν, for every row. Then

    u(W⃗) = u_0(W⃗) − Σ_(ν∈𝒩′) m_ν(W_ν) − Σ_(ν∈ℳ_(α′)) m_ν(q_ν(W⃗)),

where u_0(W⃗) is the forward solution of L_(h,p⃗)u_0 = G(W⃗),

    G(W⃗) := F − Σ_(ν∈𝒩′) r^ν(W_ν) − f^S(q_S) − f^b(q_b) − f^s1(q_s1) − Σ_(ν∈ℳ_(α′)) r^ν(q_ν) ∈ 𝒴⁰(α)

([[sec:iii-i10-1]]: r^ν ∈ 𝒴_2(α) without index set, f^S, f^s1 ∈ 𝒴⁰(α), f^b ∈ 𝒴⁰_2(α)). u_0(W⃗) = u(W⃗) + Σ m_ν has
the K⁺-weight min(α′ − 2, λ_♯ − 1) − ε > 0 and the other properties of the hypothesis of [[lem:iii-i11-3-2]] (the m_ν
have ι⁺-weight λ_♯ > 3/2). By [[lem:iii-i11-3-2]] (at b_0, where u^rot is put into ũ),

    u(W⃗) = Σ_(ν∈𝒩) m_ν(C_ν(W⃗)) + ũ,

with C_ν(W⃗) := S^(h,p⃗)_ν(G(W⃗)) − W_ν for ν ∈ 𝒩′ and C_ν(W⃗) := S^(h,p⃗)_ν(G(W⃗)) − q_ν(W⃗) for ν ∈ ℳ_(α′). As u(W⃗)
lies in [[eq:iii-i8-4-2]] at α′, the coefficients C_ν(W⃗), ν ∈ ℳ_(α′), vanish by [[cor:iii-i10-2-3]]: the rows of
K⁺-rate below α′ − 2 are exactly those of ℳ_(α′) (the s0, s2, c0, c1 rows have rates at least λ_♯ > 1 > α′ − 2, every
s1 row of rate above α′ − 2 is in 𝒩′, and none has rate α′ − 2, by admissibility in the sense of [[sec:iii-i8-1]]), so
Σ_(ν∈ℳ_(α′)) m_ν(C_ν(W⃗)), the difference of u(W⃗) and terms of K⁺-weight above α′ − 2, has K⁺-weight α′ − 2 − ε. So
u(W⃗) satisfies [[eq:iii-i11-4-2]] at α if and only if C_ν(W⃗) = 0 for ν ∈ 𝒩′ (by [[cor:iii-i10-2-3]] again, all rates
being at most 2 < α − 2; ũ and the m_ν have the ι⁺- and ℐ⁺-data of [[eq:iii-i11-4-2]]).

*At (0, 0).* Here r^ν = 0, and q⃗(W⃗) does not depend on W⃗: F(W⃗) = F − Σ L_(b_0)m_ν(W_ν), and the forward solution
m_ν(W_ν) of L_(b_0)m = L_(b_0)m_ν(W_ν) lies in [[eq:iii-i8-4-2]] at α′ for ν ∈ 𝒩′ (its rate is at least α′ − 2 and
differs from it, by admissibility; [[lem:iii-i9-2-2]]), so p⃗′_(0,0,α′)(L_(b_0)m_ν(W_ν)) = 0 by the uniqueness at α′.
Hence G(W⃗) = G(0) and C(W⃗) = C(0) − W⃗ on 𝒩′: the equation has the unique solution W⃗ = S^(0,0)(G(0)).

*Near (0, 0).* C(W⃗) = C(0) − T_(h,p⃗)W⃗ with T_(h,p⃗)W⃗ := W⃗ − S^(h,p⃗)(G(W⃗) − G(0)), linear on the
finite-dimensional space of the W⃗. G(W⃗) − G(0) = −Σ r^ν(W_ν) − (the q⃗-terms of q⃗(W⃗) − q⃗(0)); the first is
O(|W⃗|(‖h‖ + |p⃗|)) in 𝒴_2(α) ([[eq:iii-i9-2-5]]), and q⃗(W⃗) − q⃗(0) = −p⃗′_(h,p⃗,α′)(D_(p⃗)P_4(h, p⃗)(W⃗)) tends to
−p⃗′_(0,0,α′)(Σ L_(b_0)m_ν(W_ν)) = 0 as (h, p⃗) → (0, 0), for fixed W⃗ ([[prop:iii-i8-4-1]] (ii), with
[[lem:iii-i9-2-6]] (b)–(d) for the convergence of the sources in 𝒴(α′)). With the uniform bounds of
[[lem:iii-i11-3-2]] and of [[prop:iii-i8-4-1]] (i), T_(h,p⃗) → id, so T_(h,p⃗) is invertible for (h, p⃗) small; put
W⃗ := T_(h,p⃗)⁻¹C(0) and p⃗′ := q⃗(W⃗) ⊕ W⃗. The conjugation symmetry is preserved, as L and F are real and T commutes
with the conjugation of [[sec:iii-i9-1]].

*Uniqueness.* If p⃗″ also gives [[eq:iii-i11-4-2]] at α, its solution lies in [[eq:iii-i8-4-2]] at α′, so its
𝒫_(α′)-part is q⃗(W⃗″) by the uniqueness at α′ ([[prop:iii-i8-4-1]]), where W⃗″ is its 𝒩′-part; then C(W⃗″) = 0, so
W⃗″ = W⃗. *Linearity, bounds, continuity:* by construction, from those of [[prop:iii-i8-4-1]], [[lem:iii-i11-3-2]] and
T⁻¹_(h,p⃗); continuity at (0, 0) as in [[prop:iii-i8-4-1]] (ii), with [[lem:iii-i11-3-3]]. ∎

At a base point with black hole parameter b ∈ ℬ̄_*, the elimination is [[prop:iii-i15-2-5]] with q = 0: when
h_(b,v1) ≠ 0 the v1 terms u^rot of [[lem:iii-i11-3-2]] are not removed by the parameters of 𝒫, whose v1 rows carry the
coefficient space 0, and the parameter space is enlarged by the rotation rows of [[def:iii-i14-1-3]], whose coordinates
are assigned ([[def:iii-i15-2-3]]).

### Towers with coefficients {#sec:iii-i12-1}

From here on α ∈ (4, 4 + ε_K] is admissible, ℓ_3 = α − 4 − ε, and η_1 < η_2 in (ε_K, ε_+), ℰ_col and the pieces of
[[prop:iii-i11-3-1]] are as in [[sec:iii-i11-1]]–[[sec:iii-i11-4]]. We take η_2 ∈ (ε_+ − δ_+, ε_+) for a number
δ_+ ∈ (0, ε_+ − ε_K) fixed in advance ([[sec:iii-i11-1]] allows any η_2 ∈ (ε_K, ε_+) off a finite set), so that the
ι⁺-order 3 + η_2 − 2ε below is as close to 3 + ε_+ as desired.

**Definition {#def:iii-i12-1-1}** (Coefficients; [Hin26, Definition 11.58].) For an index set E ⊂ ℂ × ℕ₀, w ∈ ℝ and a
finite-dimensional space Z, Ḣ^(∞,𝒬(E,w))_b([1, ∞]; Z) is the space of the a ∈ C^∞(ℝ; Z) supported in [1, ∞) with

    a − χ_+(t_*) Σ_((z,k)∈E, Re z<w) c_(z,k) t_*^(−z)(log t_*)^k ∈ t_*^(−w) H^∞_b([1, ∞), |dt_*/t_*|; Z),
    c_(z,k) ∈ Z,                                                                                        {#eq:iii-i12-1-1}

where χ_+ ∈ C^∞(ℝ) vanishes on (−∞, 1] and equals 1 on [2, ∞); Ḣ^(∞,w)_b := Ḣ^(∞,𝒬(∅,w))_b. As t_*∂_(t_*) preserves
these spaces, a^((j)) ∈ Ḣ^(∞,𝒬(E+j,w+j))_b.

*Towers.* The rows of the table of roots of [[sec:iii-g2-1]] are the pairs ψ = (μ, τ) with roots μ ∈ (−3, 0] and
coefficient spaces 𝒴_ψ (the spaces of the coefficients Y^(μ)_τ). Let ℛ be the set of these rows and ℛ′ the set without
the boost row (−1, s1). For a valued in 𝒴_ψ let T_ψ(a) := h^((μ),≤k_μ)_(b,τ)(a) ([[def:iii-g2-2-5]]), with

    T_v1(a) := h^(≤2)_(b,v1)(a) = Σ_(j≤2) a^((j)) h̆^j_(b,v1),     h̆⁰_(b,v1) := h_(b,v1),

for the rotations, and h^(≤1)_(b,s1)(a) = h_(b,s1)(a) + h̆¹_(b,s1)(a′) for the boosts. The *spectral tower* of ψ is
T_ψ(σ)Y := Σ_(j≤k_μ) (−iσ)^j h̆^((μ),j)_(b,τ)(Y), so that ℱ(T_ψ(a)) = T_ψ(σ)â(σ) for a independent of x. By
[[sec:iii-g2-2]] and [[lem:iii-i15-1-1]] (P3), h̆^((μ),j)_(b,τ) is polyhomogeneous at ∂X with the leading order ρ^(μ−j)
(it grows like r^(j−μ)), independent of b, the Myers–Perry corrections being smaller by min Re ℰ_ind > 0. For the
boosts h_(b,s1) ∈ 𝒜³ and h̆¹_(b,s1) ∈ 𝒜² ([[sec:iii-h-2]]), and h̆^j_(b,s1), j ≥ 2, has the leading order ρ^(1−j). For
the rotations h̆^j_(b,v1), j ≥ 1, has the leading order ρ^(−j), and h_(b,v1) ∈ 𝒜³ vanishes when b = b_0. We write
d_ψ := μ for the rows other than the boosts and rotations, d_v1 := 0, and d_s1 := 1 for h^(≤k)_(b,s1), k ≥ 2. Then for
a = t_*^(−z) the leading part of T_ψ(a) is homogeneous of degree −z − d_ψ in (t_*, r), so that its K⁺-rate is z (for
v1, z when h_(b,v1) ≠ 0 and z + 1 when h_(b,v1) = 0) and its order at ι⁺ is z + d_ψ; for h^(≤1)_(b,s1)(a) the order at
ι⁺ is z + 3.

*Rates.* For a ∈ Ḣ^(∞,w)_b and ψ ≠ v1, χ_K T_ψ(a) has K⁺-order w, and the term with a^((j)) has K⁺-order w + j; so the
terms with j ≥ 2 of a coefficient of order above α − 2 are of order above α, and the lengths k_μ are immaterial for the
statements below ([Hin26, Remark 11.60 (2)]).

*The index set at ι⁺.* Let

    ℰ_♯ := {(λ, k) : λ ∈ Λ, Re λ ≥ 2, k ≤ k̄(λ)} ∪ ℳ

([[def:iii-i10-1-1]]; ℳ is [[eq:iii-i8-1-2]], the part of ℰ_++ below 2). It is an index set closed under conjugation,
with min Re ℰ_♯ ≥ λ_♯ and ℰ_♯ ∩ {Re < 2} = ℳ. Below 2 it keeps the logarithmic orders of ℰ_++, which the exponents below
2 produced in [[sec:iii-i10-3]] carry ([[lem:iii-i10-1-2]] (c)); k̄(λ) > k̄_0 would admit more. As ℰ_++ is closed under
the addition of ℰ_ind ∪ ℰ^ι_ind ([[eq:iii-i8-1-1]]), ℳ + (ℰ_ind ∪ ℰ^ι_ind) lies in ℳ below 2, and above 2 its
logarithmic orders are at most k̄_0 + l_* ≤ k̄. By [[lem:iii-i10-1-2]] (b) the part of ℰ_♯ of real part below 3 + ε_+
does not depend on ℰ_+, so ℰ_+ ⊃ ℰ_♯ ∩ {Re < 3 + ε_+} can be required together with (H1)–(H3) ([Hin26, Remark 11.62]).
ℰ_♯ does not depend on b.

### The lemmas of the expansion {#sec:iii-i12-2}

Let χ ∈ C_c^∞((−1, 1)) be the low frequency cut-off of [[sec:iii-i11-3]] (equal to 1 near [−½, ½]), and
χ_zf = χ_0(r̂) with χ_0 ∈ C_c^∞([0, 1)) equal to 1 near 0, so that k := ℱ⁻¹[χ_0(|ζ|)] is a Schwartz function with
∫ k = 1 and ∫ s^m k(s) ds = 0 for m ≥ 1 (these are the derivatives at 0 of χ_0(|ζ|), which is 1 near 0). A *profile*
of *degree* d is a section p on X, conormal at ∂X, with |p| ≲ r^(−d)⟨log r⟩^l for r ≥ 1 and some l, with
b-derivatives; it is *polyhomogeneous* if it is so at ∂X, with leading order ρ^d. The profiles of [[thm:iii-i12-3-1]]
are in general only polyhomogeneous to a finite order (for instance û_2 and û_3 of [[prop:iii-i11-3-1]], and v_0 below),
and some carry a factor log r.

**Lemma {#lem:iii-i12-2-1}** (The cut-off as an approximate identity.) Let p_0, …, p_k be profiles of degrees
d_j ≥ d − j, P(σ, x) := Σ_j (−iσ)^j p_j(x), and let c = Σ_± 1_(±σ>0)c^± with either (a) c^± ∈
H^(∞,w)_b(±(0, 1), |dσ/σ|), w > −1, or (b) c = |σ|^z(log|σ|)^m sgn(σ)^δ, Re z > −1 (and then w := Re z). Put
y := ℱ⁻¹(χc). Then on {t_* ≥ 1}

    ℱ⁻¹[χ(|σ|)χ_zf(|σ|r)c(σ)P(σ, x)] = χ_K Σ_j (χ_+y)^((j))(t_*) p_j(x) + R,                            {#eq:iii-i12-2-1}

where R has K⁺-order ∞ (for every N, |R| ≲ (r/t_*)^N t_*^(−w−1)⟨r⟩^(−d) on {r ≤ t_*/8}, up to logarithms, with
b-derivatives) and, near ι⁺, the order w + 1 + d. In case (b), if the p_j are polyhomogeneous, R and
χ_K Σ_j (χ_+y)^((j))p_j are polyhomogeneous at ι⁺, with the exponents z + 1 + d plus those of the expansions of the p_j
(and logarithms up to m); and if p_j = p^ph_j + p^c_j with p^ph_j polyhomogeneous and p^c_j of degree at least d′ − j,
the part from the p^c_j has the order Re z + 1 + d′ at ι⁺; and χ_+y ∈ Ḣ^(∞,𝒬((z+1,m),∞))_b. In case (a),
χ_+y ∈ Ḣ^(∞,w+1)_b.

*Proof.* y satisfies the symbol estimates |(t∂_t)^l y^((j))(t)| ≲ ⟨t⟩^(−w−1−j) ([[prop:ii-g1-3-5]] (1) in case (a);
in case (b), y is c_±|t|^(−z−1) times polynomials in log|t| plus a Schwartz function as t → ±∞), so χ_+y lies in the
stated classes. For every x the left side of [[eq:iii-i12-2-1]] is Σ_j (y^((j)) + e_(j,r))(t_*)p_j(x) (as
ℱ(a′) = −iσâ), with e_(j,r) := ℱ⁻¹[(−iσ)^j χc(χ_0(|σ|r) − 1)]. Let χ_0 = 1 on [0, c_0]. The symbol of e_(j,r) vanishes
for |σ| ≤ c_0/r, so e_(j,r) = 0 for r < c_0; for r ≥ c_0 it satisfies
|∂^l_σ[(−iσ)^j χc(χ_0(|σ|r) − 1)]| ≲ |σ|^(j+w−l) on its support, as ∂^l_σ[χ_0(|σ|r)] = r^l χ_0^((l))(|σ|r) sgn(σ)^l lives
where |σ|r ≤ 1, and the jump of c at σ = 0 lies outside the support. Integrating by parts M > j + w + 1 times,

    |e_(j,r)(t)| ≲ |t|^(−M) ∫_(|σ|≥c_0/r) |σ|^(j+w−M) dσ ≲ |t|^(−M) r^(M−j−w−1) = (r/|t|)^(M−j−w−1)|t|^(−j−w−1),

and likewise with b-derivatives (t∂_t and r∂_r preserve this symbol class). On {r ≤ t_*/8}, where χ_K = χ_+ = 1 for
t_* ≥ 2, R = Σ_j e_(j,r)p_j for t_* ≥ 2; with |p_j| ≲ ⟨r⟩^(j−d) (up to logarithms) this gives
|R| ≲ (r/t)^N t^(−w−1)⟨r⟩^(−d) for every N, and the b-derivatives alike. For r ≥ 2, χ = 1 on the support of
χ_0(|σ|r), and the left side is Σ_j (y^((j)) ∗ k_r)(t_*)p_j(x), with k_r(s) := r⁻¹k(s/r). On {r ≥ t_*/8}, r ≥ 2, the
substitution σ = ζ/r gives

    (y^((j)) ∗ k_r)(t) = r^(−1−j) ∫ e^(−iζt/r) χ_0(|ζ|)(−iζ)^j c(ζ/r) dζ/(2π),

of size r^(−1−j−w) uniformly in t/r (by the symbol estimates of c); so the left side is O(r^(−1−w−d)) there, and so is
χ_K Σ_j (χ_+y)^((j))p_j (χ_K vanishes for r ≥ t_*/2, and |y^((j))p_j| ≲ t^(−w−1−j)r^(j−d)); this is the order
w + 1 + d at ι⁺. In case (b) the left side is, for r ≥ 2, r^(−1−z) times a smooth function of t/r (with factors log r
up to the power m) times the p_j (the conormal parts p^c_j giving the order Re z + 1 + d′), and
χ_K Σ_j (χ_+y)^((j))p_j is a function of t_*, polyhomogeneous at t_* = ∞, times χ_c(r/t_*) and the p_j; both are
polyhomogeneous at ι⁺ (in the coordinates t_*⁻¹, r/t_*) with the stated exponents. ∎

**Lemma {#lem:iii-i12-2-2}** (The columns at the last level.) Let a > −1, S ∈ H^(∞,a)_b(±(0, 1), |dσ/σ|; 𝒮_(1,ℂ)),
ḃ ∈ H^(∞,a)_b(±(0, 1), |dσ/σ|; 𝔟_ℂ), and put A := χ_+ℱ⁻¹[−χσS] ∈ Ḣ^(∞,a+2)_b and B := χ_+ℱ⁻¹[iχσ²ḃ] ∈
Ḣ^(∞,a+3)_b. Then on {t_* ≥ 1}

    ℱ⁻¹[χσ³ĥ^aug(σ)(S)] = χ_K h^(≤1)_(b,s1)(A) + R_S,          ℱ⁻¹[χσ³ĝ^aug(σ)(ḃ)] = χ_K ġ(B) + R_b,    {#eq:iii-i12-2-2}

with R_S, R_b of K⁺-order a + 4 and of order a + 5 at ι⁺.

*Proof.* By [[eq:iii-h-2-6]], σ³ĥ^aug(S) = −σΨh(S) + σ²(∂_σΨ)h(S) + iσ²Ψh̆(S) and σ³ĝ^aug(ḃ) = iσ²Ψġ(ḃ), where
Ψ(σ, x) = ∫ e^(iσt)φ_x(t) dt, φ_x := ∂_(t_*)χ_K(·, x), ∫ φ_x = 1; for r ≥ 1, φ_x(t) = r⁻¹φ(t/r) with
φ(s) = ∂_s[χ_c(1/s)] supported in [2, 4] ([[lem:iii-h-2-5]] (b)), and for r ≤ 1, φ_x is supported in [1, 4]. Products
with Ψ and ∂_σΨ are convolutions in t with φ_x and with itφ_x(t). With a_0 := ℱ⁻¹[−χσS] (so that
ℱ⁻¹[χσ²S] = −ia′_0), the left side of the first identity is

    h(S)(∫ (a_0(t − τ) + τa′_0(t − τ))φ_x(τ) dτ) + h̆(S)(∫ a′_0(t − τ)φ_x(τ) dτ)

(S applied to the scalar coefficients). By Taylor's formula, a_0(t − τ) + τa′_0(t − τ) =
a_0(t) − τ² ∫_0^1 s a″_0(t − sτ) ds (the first moments cancel) and a′_0(t − τ) = a′_0(t) − τ ∫_0^1 a″_0(t − sτ) ds; as
τ ≤ 4 max(r, 1) on supp φ_x, on {r ≤ t_*/8} the remainder is bounded by
max(r, 1)²t^(−a−4)|h| + max(r, 1)t^(−a−4)|h̆| ≲ t^(−a−4)r⁻¹ (h ∈ 𝒜³, h̆ ∈ 𝒜²), with b-derivatives: K⁺-order a + 4. On
{r ≥ t_*/8}, r ≥ 2, the right side is O(t^(−a−2)r⁻³ + t^(−a−3)r⁻²) (χ_K vanishes for r ≥ t_*/2), and the left side is
O(r^(−a−5)): for r ≥ 1, Ψ = Φ(σr) and ∂_σΨ = rΦ′(σr) with Φ a Schwartz function ([[lem:iii-h-2-5]] (b)), and the
substitution σ = ζ/r gives

    ℱ⁻¹[χσΦ(σr)S], ℱ⁻¹[χσ²rΦ′(σr)S] = O(r^(−2−a)),          ℱ⁻¹[χσ²Φ(σr)S] = O(r^(−3−a))

uniformly in t/r (by the symbol estimates of S, as in the proof of [[lem:iii-i12-2-1]]), with h ∈ 𝒜³, h̆ ∈ 𝒜²: the
order a + 5 at ι⁺. Replacing a_0 by A = χ_+a_0 changes the right side only for t_* ≤ 2, where χ_K is supported in
{r ≤ 1}. The second identity is proved in the same way, with b_0 := ℱ⁻¹[iχσ²ḃ] and ġ ∈ 𝒜²:

    ∫ b_0(t − τ)φ_x(τ) dτ = b_0(t) − ∫ τ ∫_0^1 b′_0(t − sτ) ds φ_x(τ) dτ,

the remainder being O(max(r, 1)t^(−a−4)r⁻²), and ℱ⁻¹[iχσ²Φ(σr)ḃ] = O(r^(−3−a)) on {r ≥ t_*/8}. ∎

*Stationary solutions.* Let L_0 := L̂_b(0), L_1 = [L_b, t_*] and L_2 = ½[[L_b, t_*], t_*] ([[sec:iii-i6-1]]), so that
L_b(a(t_*)p) = aL_0p + a′L_1p + a″L_2p for stationary p, and a tower Σ_j a^((j)) h̆^j satisfies

    L_0h̆^m + L_1h̆^(m−1) + L_2h̆^(m−2) = 0

for m up to its length ([[eq:iii-g2-2-2]]). In particular the bottom h̆^((μ),0)_(b,τ)(Y) of each row of ℛ′ other than
v1 lies in ker L_0, and so do h_(b,s1)(S) and ġ(ḃ); at b_0 so does h̆¹_(b_0,v1)(V), as h_(b_0,v1) = 0. The following two
lemmas are stated at b_0; their forms at every b ∈ ℬ̄_* are [[lem:iii-i15-2-9]].

**Lemma {#lem:iii-i12-2-3}** (Stationary solutions of moderate growth.) Let b = b_0. Let 𝒢_* be the space of sections on
X that are conormal at ∂X of some order above −3 (in 𝒜^a, a > −3); write h := h_(b_0,s1) and h̆^j := h̆^j_(b_0,s1).

(a) If p ∈ 𝒢_* and L_0p = 0, then p = Σ_ψ h̆^((μ_ψ),0)_(b_0,τ_ψ)(Y_ψ) + h̆¹_(b_0,v1)(V) + ġ(ḃ) + h(S), the sum over the
rows of ℛ′ other than v1, with unique coefficients; the rows with μ_ψ < −s do not occur if p = O(r^s).

(b) If X ∈ 𝒢_*, ḃ ∈ 𝔟_ℂ, S ∈ 𝒮_(1,ℂ) and L_0X = L_1ġ(ḃ) + L_1h̆¹(S) + L_2h(S), then ḃ = 0, and the s1-component of
the ρ⁻¹-coefficient of the reduced section (below: X after the subtraction of the states of lower root) is that of
h̆²(−S). In particular L_1ġ(ḃ) ∈ L_0(𝒢_*) only for ḃ = 0, and the reduction of an element of ker L_0 ∩ 𝒢_* subtracts no
growing boost section h̆²(S′), S′ ≠ 0.

*Proof.* *The reduction.* Let X ∈ 𝒢_* with L_0X ∈ 𝒜³. As L_0 = ρ²A with A b-elliptic ([[sec:iii-f1-2]]) and
ρ⁻²L_0X ∈ 𝒜¹, [[lem:iii-a-1-4]] (stated on H^(∞,α)_b; passing from 𝒜^a costs an ε in the weight, which is immaterial
here) makes X polyhomogeneous modulo 𝒜^(1−ε), with exponents in the indicial roots of real part in (a, 1) plus ℕ₀; a
logarithm can occur only where a root meets a lower one plus an integer, so the lowest exponent carries none, the roots
being simple. Let μ_0 be the least real part of an exponent of X, and suppose μ_0 ≤ 0. As every indicial root is simple
([[sec:iii-g2-1]]), the argument of the proof of [[thm:iii-g2-3-1]] (the lowest term) applies: the top logarithm at μ_0
vanishes, μ_0 is a root in 𝒲 (real), and the ρ^(μ_0)-coefficient is Σ_τ h̄_τ(Y_τ) ([[lem:iii-g2-1-2]]). Subtract, for
every type, the element of ker L_0 listed above with this leading term (for v1 at −1, h̆¹_(b_0,v1)(V)), and for s1 at −1
the section h̆²(S′), h̄_s1(S′) being the s1-component; then μ_0 rises (the corrections of the states are smaller by
min Re ℰ_ind), and L_0 of the new section is the old one plus L_1h̆¹(S′) + L_2h(S′) (the tower relation
L_0h̆² + L_1h̆¹ + L_2h = 0). After finitely many steps all exponents have real part above 0; as there are no roots in
(0, 1] ([[prop:iii-f1-2-3]] (a)) and ρ⁻²L_0X ∈ 𝒜¹, the result lies in 𝒜¹.

(b) By the reduction, X = X_1 + (elements of ker L_0 ∩ 𝒢_*) + h̆²(S′) with X_1 ∈ 𝒜¹ and
L_0X_1 = L_1ġ(ḃ) + L_1h̆¹(S + S′) + L_2h(S + S′), h̄_s1(S′) being the s1-component of the ρ⁻¹-coefficient of the
section reached at the root −1. By [[eq:iii-h-2-2]], f̂_ḃ(0) = L_1ġ(ḃ) + L_0w_ḃ and f̂_(S″)(0) = L_2h(S″) +
L_1h̆¹(S″) + L_0w_(S″) with w_ḃ, w_(S″) ∈ 𝒜¹ ([[lem:iii-h-2-3]]); so f̂_ḃ(0) + f̂_(S+S′)(0) = L_0Q with
Q := X_1 + w_ḃ + w_(S+S′) ∈ 𝒜¹, which lies in the space 𝒳_0 of [[ch:s18]] (conormal order q − 2 ∈ (0, 1)). Choose
u_e ∈ ker L_0 ∩ 𝒳_0 with r(u_e) = −r(Q) (possible by the normalisation [[eq:iii-h-3-1]] of the rows f*_1, f*_2 of
L̃_(b_0)(0)). Then L̃_(b_0)(0)(−Q − u_e, ḃ, S + S′) = (0, 0), and [[prop:iii-h-3-2]] gives ḃ = 0 and S′ = −S.

(a) The reduction of p ends in p_1 ∈ 𝒜¹ ∩ ker L_0 once S′ = 0, which is (b) with ḃ = 0 and S = 0. Then p_1 ∈ 𝒜^(2−)
(the next roots are at least 2) lies in the domain of [[prop:iii-f3-4-1]] for small α, whose nullspace (1) is spanned by
ġ(ḃ) and h(S). Uniqueness: Y ↦ h̄_τ(Y) is injective ([[lem:iii-g2-1-2]]), and that nullspace is eleven-dimensional. The
last statement: a state of root μ grows like r^(−μ). ∎

**Lemma {#lem:iii-i12-2-4}** (Formal solutions at K⁺.) Let b = b_0, β ∈ (α − 1, α], and

    w = χ_K Σ_(i∈I) y_i(t_*)p_i(x) + w′,                                                                {#eq:iii-i12-2-3}

with I finite, conormal profiles p_i of degrees d_i (not necessarily in 𝒢_*: the companions h̆^((μ),1) of the rows with
μ ∈ (−3, −2] have degree at most −3), y_i ∈ Ḣ^(∞,𝒬(E_i,∞))_b with every (z, k) ∈ E_i satisfying Re z ≥ β − 2 and
Re z + d_i ≥ λ_♯ (*compatibility*), and w′ of K⁺-order β. If L_(b_0)w has K⁺-order β, then

    χ_K Σ_i y_i p_i = χ_K(Σ_(ψ∈ℛ′) T_ψ(a_ψ) + h^(≤1)_(b_0,s1)(a_s) + ġ(a_b)) + w″,                      {#eq:iii-i12-2-4}

where a_ψ, a_s, a_b are finite sums of terms χ_+t_*^(−z)(log t_*)^k, with exponents in ⋃_i E_i + ℕ₀ (for a_v1,
⋃_i E_i + ℕ₀ − 1), those of a_ψ satisfying Re z + d_ψ ≥ λ_♯ and those of a_b of real part at least β − 1, and w″ has
K⁺-order β; all are linear in (y_i). *Exponents.* Let ℐ_* be the set of the (z + e, k + l), (z, k) ∈ E_i, (e, l) an
exponent of the polyhomogeneous part of p_i (i ∈ I). For every exponent (z, k) of a_ψ such that d_ψ lies below the
degree of the conormal (non-polyhomogeneous) part of every p_i whose coefficient c^((i))_(z,k) in the proof is nonzero,
(z + d_ψ, k) is an element of ℐ_* plus finitely many elements of ℰ_ind.

*Proof.* We remove the pairs (z, k) with Re z < β one at a time, in order of increasing real part and, at equal
exponent, of decreasing k. Let (z_0, k_0) be the first pair whose coefficient section P := Σ_i c^((i))_(z_0,k_0)p_i is
nonzero, c^((i))_(z,k) being the coefficient of t_*^(−z)(log t_*)^k in y_i. In {r ≤ R}, for large t_*, χ_K = 1 and
L_(b_0)(yp) = yL_0p + y′L_1p + y″L_2p, and y′, y″ have the exponents (z + 1, ·), (z + 2, ·); so the coefficient of
t_*^(−z_0)(log t_*)^(k_0) in L_(b_0)w is L_0P, which vanishes, L_(b_0)w and w′ being of K⁺-order β > Re z_0 on every
{r ≤ R}. By compatibility P = O(r^(Re z_0−λ_♯)), with Re z_0 − λ_♯ < β − λ_♯ < 3, so P ∈ 𝒢_*, and
[[lem:iii-i12-2-3]] (a) gives P = Σ_ψ h̆^((μ_ψ),0)(Y_ψ) + h̆¹_(b_0,v1)(V) + ġ(ḃ) + h_(b_0,s1)(S) with only rows
μ_ψ ≥ λ_♯ − Re z_0.

*If Re z_0 + 1 < β, then ḃ = 0.* The coefficient of t_*^(−z_0−1)(log t_*)^(k_0) in L_(b_0)w is L_0P_1 − z_0L_1P, P_1
being the coefficient section of (z_0 + 1, k_0) (the pairs (z_0, k), k > k_0, have zero coefficient, and none has real
part below Re z_0), and it vanishes. With the tower relations L_1h̆^((μ),0) = −L_0h̆^((μ),1),
L_1h_(b_0,s1) = −L_0h̆¹_(b_0,s1) and L_1h̆¹_(b_0,v1) = −L_0h̆²_(b_0,v1) (all these rows have k_μ ≥ 1, below),
z_0L_1ġ(ḃ) ∈ L_0(𝒢_*), and z_0 ≠ 0; [[lem:iii-i12-2-3]] (b) gives ḃ = 0.

*Subtraction.* Let a := χ_+t_*^(−z_0)(log t_*)^(k_0), and let ã be the polyhomogeneous antiderivative with ã′ = a on
[2, ∞) (exponents (z_0 − 1, ≤ k_0); z_0 ≠ 1 as Re z_0 ≥ β − 2 > 1), and subtract

    w_1 := χ_K(Σ_ψ T_ψ(aY_ψ) + T_v1(ãV) + h^(≤1)_(b_0,s1)(aS) + ġ(aḃ)).

Then w − w_1 is again of the form [[eq:iii-i12-2-3]]: the pair (z_0, k_0) is gone, and the new terms a^((j))h̆^((μ),j),
j ≥ 1, have the exponents (z_0 + j, ≤ k_0), later in the order, and are compatible (z_0 + j with degree μ − j;
h_(b_0,s1) and h̆¹_(b_0,s1) have the degrees 3 and 2). And L_(b_0)w_1 has K⁺-order β: by the tower relations,
L_(b_0)T_ψ(aY) consists of the terms with a^((k_μ+1)) and a^((k_μ+2)) ([[lem:iii-g2-2-6]]), of K⁺-order
Re z_0 + k_μ + 1; the rows with μ > −2 have k_μ ≥ 1 (the table of [[sec:iii-g2-1]]), and Re z_0 + 2 ≥ β; rows with
μ ≤ −2 occur only if Re z_0 ≥ λ_♯ + 2 > β − 1; L_(b_0)h^(≤1)_(b_0,s1)(aS) and L_(b_0)T_v1(ãV) involve a″ and higher;
L_(b_0)ġ(aḃ) = a′L_1ġ + a″L_2ġ, with ḃ = 0 unless Re z_0 + 1 ≥ β; and [L_(b_0), χ_K] is supported in
{t_*/4 ≤ r ≤ t_*/2}, away from K⁺. There are finitely many pairs with real part below β, so the process ends;
collecting the subtracted coefficients gives [[eq:iii-i12-2-4]].

*Exponents.* The ρ^(μ_ψ)-coefficient of P is that of Σ_i c^((i))_(z_0,k_0)p_i less the corrections of the states of
lower root removed in the reduction of [[lem:iii-i12-2-3]], which lie at those roots plus elements of ℰ_ind; so
(z_0 + μ_ψ, k_0) is (z_0 + e, k_0) for an exponent e of some p_i, or of a companion subtracted earlier, plus elements of
ℰ_ind (a companion a^((j))h̆^((μ),j) has the exponent z + j and the degree μ − j, so the same sum z + μ); for v1 the
exponent of ã is z_0 − 1, with d_v1 = 0 and μ_v1 = −1. ∎

### The expansion modulo the order α {#sec:iii-i12-3}

This section is [Hin26, Theorem 11.59, Part 4 of the proof, (11.196), and the ι⁺-part of (11.222)] in dimension 4 + 1.
In it, b = b_0: F ∈ 𝒴⁰(α), (h, p⃗) is a small base point with black hole parameter b_0, p⃗′ is as in
[[thm:iii-i11-4-1]], and u is the forward solution of L_(h,p⃗)u = F − D_(p⃗)P_4(h, p⃗)(p⃗′). The form at every
b ∈ ℬ̄_* is [[cor:iii-i15-2-10]].

**Theorem {#thm:iii-i12-3-1}** (The expansion at K⁺.) For every small ε > 0,

    u = χ_K u_exp + ũ,     u_exp = h^(≤1)_(b_0,s1)(Ṡ_rem) + ġ(ḃ_rem) + Σ_(ψ∈ℛ′) T_ψ(Ẏ_ψ),               {#eq:iii-i12-3-1}

with

    Ṡ_rem ∈ Ḣ^(∞,α−2−ε)_b([1, ∞]; 𝒮_(1,ℂ)),     ḃ_rem ∈ Ḣ^(∞,α−1−ε)_b([1, ∞]; 𝔟_ℂ),
    Ẏ_ψ ∈ Ḣ^(∞,𝒬(ℰ_♯−d_ψ, w_ψ))_b([1, ∞]; 𝒴_ψ),                                                         {#eq:iii-i12-3-2}

w_ψ := 3 + η_2 − 2ε − d_ψ for every ψ ∈ ℛ′ (d_v1 = 0), and

    ũ ∈ H^(∞,(⟨ℰ^C_I⟩,ℓ_I),(ℰ_♯,3+η_2−2ε),α−ε)_b(Ω_*)^(•,−).                                            {#eq:iii-i12-3-3}

The coefficients are conjugation-symmetric (u being real), linear and continuous in F, with bounds uniform for (h, p⃗)
small. Each term of χ_K u_exp has K⁺-order at least α − 2 − ε, so [[eq:iii-i12-3-1]] contains the bound
u = O(t_*^(−α+2+ε)) in compact sets of [[thm:iii-i11-4-1]]; and L_(b_0)(χ_K u_exp) has K⁺-order α − ε ([Hin26, Remark
11.60 (1) and (11.232)]).

The polyhomogeneous parts of the Ẏ_ψ come from the ι⁺-terms of u: an ι⁺-exponent λ gives the coefficient t_*^(−λ+d_ψ)
([[lem:iii-i12-2-1]] (b), [[eq:iii-g2-4-3]]), hence the index set ℰ_♯ − d_ψ. Their conormal parts, present only for the
rows with μ ∈ (−1, 0] (d_ψ = μ), come from the last Taylor level and have order at least 3 + η_2 − 2ε − μ. The boosts
and the black hole parameters carry only conormal coefficients, of the orders α − 2 − ε and α − 1 − ε, as in [Hin26].
The coefficients of v1 and of the rows with μ ≤ −1 are finite sums of terms χ_+t_*^(−z)(log t_*)^k, so they lie in
these spaces for every w_ψ; the choice of w_ψ makes the ι⁺-order of every χ_K T_ψ(Ẏ_ψ) at least 3 + η_2 − 2ε, as in
[Hin26, (11.227b)].

*Proof.* *Step 0 (the decomposition).* As in the proof of [[thm:iii-i11-4-1]], u = u_0 − Σ_ν m_ν(S_ν), where u_0 is
the forward solution of L_(h,p⃗)u_0 = G(W⃗) ∈ 𝒴⁰(α) and the S_ν are its coefficients of [[lem:iii-i11-3-2]] (the C_ν
vanish). By the proof of that lemma, u_0 = u_I + u_ι + v ([[prop:iii-i10-3-1]] for f′ := G(W⃗) − (L_(h,p⃗) − L_(b_0))u_0,
which lies in 𝒴⁰(α) with K⁺-order α − ε), L_(b_0)v = f^♭, and v = v_hi + v_low with v̂ on 0 < |σ| ≤ c the sum of the
pieces of [[prop:iii-i11-3-1]], in which S_0 = 0, ḃ_0 = 0 and S_1 = 0 (its Steps 1 and 6). Moreover
L_(b_0)u = f′ − Σ_ν L_(b_0)m_ν(S_ν) has K⁺-order α − ε: by the tower relations L_(b_0)m_ν consists, near K⁺, of terms
with a_ν^((K_τ+1)) and a_ν^((K_τ+2)), of K⁺-order at least Re e_ν + K_τ + 1 ([[sec:iii-i9-2]], [[lem:iii-i9-2-2]],
[[lem:iii-g2-2-6]]), which exceeds 9/2 > α: for s1, K_τ ≥ k_s1 = 3 ([[lem:iii-i10-2-1]] (c)) and
Re e_ν ≥ λ_♯ − 1 > ½; for the other rows the rate is at least λ_♯ > 3/2 and K_τ ≥ 2.

*Step 1 (the pieces near K⁺).* We write each part of u, on {t_* ≥ 1}, as χ_K times (polyhomogeneous coefficients
times profiles), plus conormal towers, plus a term of K⁺-order α − ε whose order at ι⁺ is at least 3 + η_2 − 2ε or
which is polyhomogeneous there with exponents in ℰ_♯.

(i) u_I, which contains the solutions u′_(λ_0) at ℐ⁺ of Step 2 of the proof of [[prop:iii-i10-3-1]], vanishes near K⁺
([[prop:iii-i10-3-1]] (a)).

(ii) u_ι = Σ_(λ_0) Σ_j (χ_K u^((j))_(b_0,0) + χ_ι t_*^(−λ_0)(log t_*)^j ũ^((j))); u^((j))_(b_0,0) is
[[eq:iii-g2-4-3]] at λ_0, a sum of towers with coefficients t_*^(−λ_0+μ)(log t_*)^j (and a_s1, a_v1), and
χ_ι t_*^(−λ_0)ũ^((j)) has K⁺-order Re λ_0 + ℓ_K(λ_0) − ε = α − ε (by the proof of [[thm:iii-g2-4-2]], near K⁺:
t_*^(−λ)R^(ℓ_K) = t_*^(−λ−ℓ_K)r^(ℓ_K)).

(iii) m_ν(S_ν) = χ_K T_ν(a_ν S_ν) up to K⁺-order at least Re e_ν + k_μ + 1 > α ([[def:iii-i9-2-1]],
[[lem:iii-i10-2-1]] (c)).

(iv) v_hi has K⁺- and ι⁺-order j for every j ([[lem:iii-i2-4-1]]).

(v) The zero energy pieces σ^j χ_zf û^±_j, j ≤ 3: by [[lem:iii-i12-2-1]] (b) with c = σ^j sgn(σ)^δ (the sign-even and
sign-odd parts of û^±_j) and the single profile û_(j,e) or û_(j,o); for δ = 0, y is a Schwartz function at +∞.
[[lem:iii-i11-2-1]] makes û_j polyhomogeneous only to a finite order (û_2 to ε_+ − ε, û_3 conormal); its polyhomogeneous
part gives ι⁺-exponents in Λ ([[lem:iii-i12-2-1]] (b)), and its conormal part the ι⁺-order at least 3 + η_2 − 2ε
(3 + ε_+ − ε at the levels 0–2, κ + 2 at level 3).

(vi) The pieces of [[prop:iii-g4-4-4]] at the levels 1 and 2: σ^j χ_zf |σ|^(α_0−2)u_b is by [[eq:iii-g4-4-4]] a finite
sum of terms c(σ)P(σ, x) with c homogeneous and P a spectral tower (G_(μ,τ), G_s1, G_v1, G^exc_s1) or a tower whose
profiles are multiplied by r^β or log r (from l_β(r̂) = (|σ|^β r^β − 1)/β), to which [[lem:iii-i12-2-1]] (b) applies.
χ_tf ρ^(α_0−2)_tf u_tf does not vanish near zf: χ_tf = χ_2(ρ + |σ|) is 1 at tf ∩ zf and nonzero at zf over
{r > 2/ρ_0} ([[sec:iii-g4-1]]), ρ_tf = |σ| + ⟨x⟩⁻¹ ([[sec:iii-h-1]]), and u_tf has the zf-class ((0, 0), ℓ_zf)
([[prop:iii-g4-4-4]]). We expand σ^j χ_tf ρ^(α_0−2)_tf u_tf at zf to the order ℓ_zf + j, the zf-exponents being j plus
ℕ₀ (from χ_2, from ρ_tf and, if the zf-index set (0, 0) of u_tf is read with its ℕ₀-shifts, from u_tf itself, all in
|σ| and of the same form). Its zf-terms σ^j|σ|^k c^±_k(x), cut off by χ_zf, are pieces of the type (v)
([[lem:iii-i12-2-1]] (b) with c = σ^j|σ|^k sgn(σ)^δ and the single profile c_(k,e) or c_(k,o)), and the zf-remainder,
of weight ℓ_zf + j = α − 1 − ε (the choice of the level in [[prop:iii-i11-3-1]]), has K⁺-order α − ε
([[prop:iii-a-4-2]] (2)), with ι⁺-exponents the tf-index set plus 1.

(vii) The columns at the levels 1–3 with constant data (ḃ^±_1, and ḃ^±_j, S^±_j for j = 2, 3):
σ^jĝ^aug(ḃ) = iσ^(j−1)Ψġ(ḃ) and σ^jĥ^aug(S) = −σ^(j−2)G_2(σ)(S) are, as in the proof of [[lem:iii-i12-2-2]],
convolutions in t_* of ℱ⁻¹[χσ^m sgn(σ)^δ] with φ_x and tφ_x; Taylor's formula to a finite order writes them as finitely
many terms y(t_*)r^l ġ, y r^l h, y r^l h̆ (y polyhomogeneous, from the moments of φ) plus a remainder of K⁺-order at
least α. Near ι⁺, where χ_K = 0 for r ≥ t_*/2, the piece itself is what is recorded: for r ≥ 1, Ψ = Φ(σr) and
∂_σΨ = rΦ′(σr) ([[lem:iii-h-2-5]] (b)), and σ = ζ/r gives ℱ⁻¹[χσ^m sgn(σ)^δ Φ(σr)] = r^(−1−m)G(t_*/r) + O(r^(−∞)) with
G smooth (and likewise with rΦ′(σr)); so each piece is polyhomogeneous at ι⁺ with the exponent m + 1 plus the degree of
the state (ġ: 2 or 3; h: 3; h̆: 2) and the exponents of its expansion, for instance 3 or 4 at level 1; these lie in Λ
(3 ∈ Λ, Λ + 1 ⊂ Λ, Λ + ℰ_ind ⊂ Λ).

(viii) The pieces of [[prop:iii-g4-5-1]] at level 3: σ³χ_zf u_b is by [[eq:iii-g4-5-2]] a sum of spectral towers times
the conormal scalars σ³|σ|^(α_κ−3)S(σ), σ³|σ|^(α_κ−2)V(σ), σ³|σ|^(α_κ−2−μ)Y(σ), of the zf-weights α_κ, α_κ + 1,
α_κ + 1 − μ; [[lem:iii-i12-2-1]] (a) gives conormal towers with coefficients of the orders α_κ + 1 (boosts, tower
h^(≤3)_(b_0,s1)), α_κ + 2 (rotations, tower rate α_κ + 3 > α) and α_κ + 2 − μ, the last of K⁺-order above α unless
μ ∈ (−1, 0]; their order at ι⁺ is α_κ + 2 ≥ κ_3 + 2 = 3 + η_2 − 2ε. In the boost tower the terms with a″, a‴ have
K⁺-order α_κ + 3 > α, and it is truncated to h^(≤1)_(b_0,s1). For σ³χ^♯_tf ũ: [[prop:iii-g4-5-1]] gives ũ the zf-class
((0, 0), ℓ_zf), its proof putting χ_zf χ_tf v_0 into ũ with v_0 stationary and conormal of order α_κ − 2 ∈ (−1, 0) (its
other part, |σ|^(α_κ−2)ũ_1, times σ³, joins the zf-remainder of weight ℓ_3 + 3); so σ³χ^♯_tf ũ is
σ³χ^♯_tf χ_zf χ_tf v^±_0, expanded at zf as in (vi) into pieces of the type (v) with the single profiles v_(0,e), v_(0,o)
(of degree α_κ − 2; their sign-odd parts reach the K⁺-exponent 4), plus a zf-remainder of weight ℓ_3 + 3 = α − 1 − ε,
of K⁺-order α − ε ([[prop:iii-a-4-2]] (2)).

(ix) The last level: σ³û_f has zf-weight ℓ_3 + 3 and tf-weight κ + 1 − ε, so K⁺-order α − ε and ι⁺-order
κ + 2 − ε > 4 ([[prop:iii-a-4-2]] (2)); the columns give χ_K h^(≤1)_(b_0,s1)(A) + χ_K ġ(B) with
A ∈ Ḣ^(∞,α−2−ε)_b and B ∈ Ḣ^(∞,α−1−ε)_b, up to K⁺-order ℓ_3 + 4 = α − ε ([[lem:iii-i12-2-2]] with a = ℓ_3).

*Step 2 (assembly).* By Step 1, on {t_* ≥ 1},

    u = χ_K Σ_(i∈I) y_i p_i + χ_K C + w′,                                                               {#eq:iii-i12-3-4}

where C consists of the conormal towers of (viii) (the truncated boost tower h^(≤1)_(b_0,s1)(A_5),
A_5 ∈ Ḣ^(∞,α_κ+1)_b, and T_ψ(Y^c_ψ) for the rows with μ ∈ (−1, 0], Y^c_ψ of order at least 3 + η_2 − 2ε − μ) and of
(ix) (h^(≤1)_(b_0,s1)(A) + ġ(B)); w′ has K⁺-order α − ε; and the y_i p_i are the polyhomogeneous terms of (ii), (iii)
and (v)–(viii) (with the zf-terms of (vi) and (viii)). Every exponent (z, k) of y_i satisfies Re z + d_i ≥ λ_♯: z + d_i
is the leading ι⁺-exponent of the piece ([[lem:iii-i12-2-1]] (b); [[eq:iii-g2-4-3]] for (ii)), and these lie in ℰ_♯
([[lem:iii-i10-1-2]] (c), [[prop:iii-i10-3-1]] and [[lem:iii-i11-2-1]]: all exponents produced are Λ-valued with
logarithmic orders at most k̄, and those below 2 lie in ℰ_++, so in ℳ). As u ([[thm:iii-i11-4-1]]) and χ_K C have
K⁺-order at least α − 2 − ε, so has χ_K Σ_i y_i p_i; in {r ≤ R} its lowest term dominates, so the coefficient section
Σ_i c^((i))_(z,k)p_i of every exponent with Re z < α − 2 − ε vanishes, and we drop these exponents from the y_i (the sum
is unchanged).

*Step 3 (formal solutions).* [[lem:iii-i12-2-4]] applies to w := u − χ_K C with β := α − ε: the hypotheses on the y_i
are those of Step 2; L_(b_0)u has K⁺-order α − ε (Step 0); and L_(b_0)(χ_K C) has K⁺-order α − ε, as by the tower
relations it consists of [L_(b_0), χ_K]C (supported away from K⁺) and of terms with A″_5 (of order α_κ + 3 > α),
(Y^c_ψ)^((3)) (of order above 3 + η_2 − μ + 2 > α), A″ and B′ (of order α − ε). It gives [[eq:iii-i12-2-4]] with a_b of
exponents at least α − 1 − ε.

*Step 4 (the coefficients).* Put Ṡ_rem := A + A_5 + a_s, ḃ_rem := B + a_b, and Ẏ_ψ := a_ψ + Y^c_ψ (with Y^c_ψ := 0
unless μ_ψ ∈ (−1, 0]). Then Ṡ_rem ∈ Ḣ^(∞,α−2−ε)_b (α_κ + 1 ≥ 2 + η_2 − 2ε > α − 2, and a_s has exponents of real part at
least α − 2 − ε), ḃ_rem ∈ Ḣ^(∞,α−1−ε)_b, and Ẏ_ψ ∈ Ḣ^(∞,𝒬(ℰ_♯−d_ψ,w_ψ))_b: a_ψ is a finite sum of terms
χ_+t_*^(−z)(log t_*)^k; those with Re z < w_ψ have (z + d_ψ, k) ∈ ℰ_♯, by [[lem:iii-i12-2-4]] (*Exponents*), as the
polyhomogeneous parts of the pieces have their ι⁺-exponents in ℰ_♯ (Step 2) and their conormal parts the order at least
3 + η_2 − 2ε ((v)), while Λ + ℰ_ind ⊂ Λ and k̄(λ + w) ≥ k̄(λ) + l_* for (w, l) ∈ ℰ_ind (the proof of
[[lem:iii-i10-1-2]] (c)), and ℳ + ℰ_ind lies in ℳ below 2 ([[sec:iii-i12-1]]); those with Re z > w_ψ, and Y^c_ψ, lie in
t_*^(−w_ψ)H^∞_b; and none has Re z = w_ψ for ε off a finite set, the exponents of a_ψ lying in ⋃_i E_i + ℕ₀, whose
elements do not depend on ε, while w_ψ does. So ũ := u − χ_K u_exp = w″ + w′ has K⁺-order α − ε.

*Step 5 (ℐ⁺ and ι⁺).* Near ℐ⁺, χ_K = 0 and ũ = u, which has the ℐ⁺-data of [[eq:iii-i11-4-2]]. Near ι⁺, u is partially
polyhomogeneous with the index set ℰ_♯ up to the order 3 + η_2 − 2ε: u_I and u_ι by [[prop:iii-i10-3-1]] (a)–(b) (index
sets Λ-valued below 3 + ε_+, logarithmic orders at most k̄, in ℳ below 2 by Step 2 of its proof, the term
χ_ι t_*^(−λ_0)(log t_*)^j ũ^((j)) being the ι⁺-term (λ_0, j) itself, with the ℐ⁺-weight ℓ_I on ι⁺,
[[cor:iii-g2-4-3]]); the m_ν, with exponents in ℰ_par ⊂ ℰ_♯ (k̄(λ + j) ≥ k̄(λ)); the pieces (v)–(vii), polyhomogeneous
with the exponents the tf-exponents plus 1 ([[lem:iii-i12-2-1]] (b); (vii) as stated there) up to the order
3 + η_2 − 2ε, in ℰ_♯; the pieces (viii)–(ix), of order at least 3 + η_2 − 2ε ([[lem:iii-i12-2-1]] (a),
[[lem:iii-i12-2-2]], and the tf-weights α_κ + 1, κ + 1 − ε); and v_hi. The same holds for χ_K u_exp: its
polyhomogeneous coefficients give the exponents z + d_ψ ∈ ℰ_♯ plus those of the expansions of the profiles (Λ is closed
under the addition of ℰ_ind, k̄(λ + w) ≥ k̄(λ) + l_*, and ℳ + ℰ_ind lies in ℳ below 2), and its conormal coefficients
have the order at least 3 + η_2 − 2ε at ι⁺ (α_κ + 2 for (viii); at least α + 1 − ε for h^(≤1)_(b_0,s1)(Ṡ_rem) and
ġ(ḃ_rem), as h_(b_0,s1) ∈ 𝒜³ and h̆¹_(b_0,s1), ġ ∈ 𝒜²). So ũ satisfies [[eq:iii-i12-3-3]].

*Step 6 (the rest).* Every map used is linear and bounded, uniformly for (h, p⃗) small ([[lem:iii-i11-3-2]],
[[thm:iii-i11-4-1]], [[lem:iii-i12-2-1]]–[[lem:iii-i12-2-4]]). Reality: u is real and the towers are real (the
conjugate of T_ψ(Y) is T_ψ(Ȳ)), so replacing every coefficient and ũ by their real parts keeps
[[eq:iii-i12-3-1]]–[[eq:iii-i12-3-3]], ℰ_♯ being closed under conjugation. L_(b_0)(χ_K u_exp) has K⁺-order α − ε by the
tower relations, as in Step 3. ∎

The proof uses its setting only through the following: u has the K⁺-weight α − 2 − ε and the ι⁺- and ℐ⁺-data of
[[eq:iii-i11-4-2]]; and u = u_0 − Σ_(ν∈𝒩″) m_ν(W_ν) for a finite set 𝒩″ of rows, with u_0 the forward solution of
L_(h,p⃗)u_0 = G for a forcing G ∈ 𝒴⁰(α) and with L_b m_ν of K⁺-order above α for ν ∈ 𝒩″. Step 1 (iii) treats the
m_ν(W_ν) as it treats the m_ν(S_ν).

### Admissible levels and enlarged sources {#sec:iii-i13-1}

[[lem:iii-i11-3-2]] reaches the order α > 4 in one step from an admissible level α′ ∈ (2, 3), which needs the K⁺-order
a_K ≥ 4 + ε_K of the background. [Hin26, Remark 11.61] uses only 2 + ε_K orders of K⁺-decay of h, at the price of
passing through every level ([Hin26, Parts 2–3 of the proof of Theorem 11.59]). The linearisation in the black hole
parameters of [[ch:s23]] carries the difference to the background h + h_(b,rem)(q), of K⁺-order only α − 2 − ε, as a
source, so it passes through every level in steps shorter than α − 4. This section and the next supply those levels,
and the sources that the linearisation produces.

Everything of [[sec:iii-i11-1]] is kept except its constant α: (H1)–(H4), (C5), Λ, k̄(λ), ℰ_par, (G), ℰ⁰_src, 𝒴⁰(·),
the rows 𝒩 = 𝒩_ι ∪ 𝒩_σ, the spectral notation and the dictionary; ℰ_♯ is that of [[sec:iii-i12-1]]. The *rate* of a
triple (τ, λ, k), τ ∈ 𝒯, λ ∈ Λ, is λ − 1 (s1), λ (s0, s2, v1) or λ + d_τ (c0, c1) ([[sec:iii-i9-1]]); by
[[lem:iii-i10-1-2]] (a) the real parts of the rates form a discrete set.

**Definition {#def:iii-i13-1-1}** (Admissible levels.) A level β ∈ (3, 4 + ε_K] is *admissible* if (a) β − 2 is not the
real part of a rate; (b) β avoids the finite set of [[def:iii-i10-1-3]], the values for which β − Re λ_0, λ_0 ∈ Λ,
Re λ_0 < 2, equals −Re μ for a root μ of L̂_b(0) or lies in Re π_1ℰ_K; and (c) β avoids the exclusion set of
[[sec:iii-i11-1]] with β in place of α: the values for which a condition [[eq:iii-g4-4-2]] of [[prop:iii-g4-4-4]] fails
at the levels 1 and 2 with ℓ_zf = β − 1 − j − ε, a condition of [[prop:iii-g4-5-1]] fails at level 3, or a value
excluded in [[lem:iii-i2-4-2]] or [[eq:iii-h-1-1]] is met at level 3 (for β > 4 as in [[sec:iii-i11-1]]; for β < 4 by
β_tf − β_zf = κ − β + 2 + ε, κ the final tf-weight of Step 4 of the proof of [[prop:iii-i13-2-1]]), with ε taken small
and off a finite set as there. In particular β ≠ 4, by (a), as 2 ∈ Λ is the rate of (s0, 2, 0). The small ε is moreover
taken with ε < β − 3, with ε < β − 4 if β > 4, and with no rate of real part in [β − 2 − 3ε, β − 2). For β ∈ (2, 3),
admissibility is that of [[sec:iii-i8-1]]. The excluded values near any level are finitely many, so the admissible
levels are dense in (3, 4 + ε_K]; and every admissible α ≥ 3 of [[def:iii-i10-1-3]] is admissible here, as by (G) no
rate has real part in (2 + ε_K − ε′_0, 2 + ε_K]. Put 𝒩_β := {ν ∈ 𝒩 : Re e_ν < β − 2}; 𝒩_β = 𝒩 for β > 4, as every row
of 𝒩 has rate at most 2.

**Definition {#def:iii-i13-1-2}** (The enlarged sources.) Let ℰ^♮ be the set of the pairs

    (λ + w_1 + ⋯ + w_m, k + l_1 + ⋯ + l_m)

with m ≥ 1, (λ, k) ∈ ℰ_♯ and (w_i, l_i) ∈ ℰ_ind ∪ ℰ^ι_ind ∪ {(1, 0)}, of real part below 3 + ε_+. For
β ∈ (2, 4 + ε_K], 𝒴^♮_2(β) is the space of the sections supported in supp χ^♯_K ([[eq:iii-i-1-2]]) lying in
⋂_ε H^(∞,∞,((ℰ⁰_src∪ℰ^♮)+2, w_+−ε),β)_b(Ω_*; S²T*), and 𝒴^♮(β) := 𝒴⁰(β) + 𝒴^♮_2(β), real sections.

**Lemma {#lem:iii-i13-1-3}** (The logarithmic count for the enlarged sources.) (a) π_1(ℰ^♮) ⊂ Λ; at
λ′ := λ + w_1 + ⋯ + w_m the logarithmic order k + l_1 + ⋯ + l_m is at most k̄(λ′) − J_*(l_* + 1) − 1; and
ℰ^♮ ∩ {Re < 2} ⊂ ℰ_++.

(b) [[lem:iii-i10-1-2]] (c) holds for sources in 𝒴^♮(β): every exponent (λ, k) produced with 2 ≤ Re λ ≤ 3 + ε_+ has
λ ∈ Λ and k ≤ k̄(λ), and those below 2 lie in ℰ_++.

*Proof.* (a) Λ + w ⊂ Λ for the increments ([[def:iii-i10-1-1]]), and π_1ℰ_♯ ⊂ Λ ∪ π_1ℳ ⊂ Λ ([[lem:iii-i10-1-2]] (a)).
The increments have real part at least η_0 > 0, so λ, λ + w_1, …, λ′ are m + 1 elements of Λ with increasing real
parts, and n(λ′) ≥ n(λ) + m; hence k̄(λ′) − k̄(λ) ≥ m(J_* + 1)(l_* + 1), while k ≤ k̄(λ) (for (λ, k) ∈ ℳ,
k ≤ k̄_0 ≤ k̄(λ)) and l_i ≤ l_*; so k + Σ l_i ≤ k̄(λ′) − m(J_*(l_* + 1) + 1). Below 2: ℰ_♯ ∩ {Re < 2} = ℳ ⊂ ℰ_++
([[sec:iii-i12-1]], where ℰ_♯ is ℳ below 2, with the logarithmic orders of ℰ_++); the pairs from ℰ_♯ ∩ {Re ≥ 2} stay
above 2; ℰ_++ is closed under the addition of ℰ_ind ∪ ℰ^ι_ind below 2 ([[eq:iii-i8-1-1]]); and adding 1 leaves
{Re < 2} (λ_♯ + 1 > 2).

(b) In the induction of the proof of [[lem:iii-i10-1-2]] (c), the logarithmic order at λ is the largest over its
contributions plus at most J_*(l_* + 1) from the raises at λ. A forcing exponent of ℰ^♮ is a further contribution, of
logarithmic order at most k̄(λ) − J_*(l_* + 1) − 1 by (a); so the bound k̄(λ) survives, and the induction runs as
there. Below 2 the exponents of the forcing lie in ℰ_++ by (a), as [[eq:iii-i8-1-1]] and Step 2 of the proof of
[[prop:iii-i10-3-1]] require. ∎

The constructions of [[sec:iii-i10-3]], [[sec:iii-i11-3]] and [[sec:iii-i12-3]] see the ι⁺-index set of a forcing only
through this count, the plain weight w_+ − ε and, for the part not supported in supp χ^♯_K, the step at ℐ⁺ (Step 1 of
the proof of [[prop:iii-i10-3-1]], which acts on f_1 ∈ 𝒴⁰_1 only; a section of 𝒴^♮_2 enters there as f_2 does, being
supported away from ℐ⁺). This is used in [[prop:iii-i13-2-4]].

### The expansion at every level {#sec:iii-i13-2}

**Proposition {#prop:iii-i13-2-1}** (The spectral phase at every level.) Let β ∈ (3, 4 + ε_K] be admissible and
f ∈ 𝒴^♮(β), and let f^♭ and v be as in [[sec:iii-i11-1]] with β in place of α (f^♭ is the forcing of
[[prop:iii-i10-3-1]] (c) for f, and v the forward solution of L_b v = f^♭, of K⁺-weight w_v > 0). Then there are
S_ν ∈ 𝒲_(τ,ℂ), ν ∈ 𝒩_σ ∩ 𝒩_β, linear and continuous in f, with

    v − Σ_(ν∈𝒩_σ∩𝒩_β) m_ν(S_ν) − v^rot_β ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,β−2−ε)_b(Ω_*)^(•,−),         {#eq:iii-i13-2-1}

where v^rot_β := 0 for β < 4, and v^rot_β is the v^rot of [[prop:iii-i11-3-1]] at β for β > 4.

*Proof.* [[prop:iii-i10-3-1]] holds at the admissible β as stated: its proof uses of α only α ≤ 4 + ε_K (for
ℓ_K(λ_0) < 3), ℓ_K(λ_0) = α − Re λ_0 > α − 2 > 0, the conditions of [[def:iii-i13-1-1]] (b), and (G) for the rows of
𝒩_ι, all of which hold for β; for f ∈ 𝒴^♮(β) it holds by [[lem:iii-i13-1-3]]. Then the proof of
[[prop:iii-i11-3-1]] applies with β in place of α, with the following changes.

*Constants.* ℓ_j := β − 1 − j − ε at the level j ∈ {1, 2, 3}, so ℓ_1 ∈ (1, 2 + ε_K), ℓ_2 ∈ (0, 1 + ε_K) and
ℓ_3 ∈ (−1, ε_K); η_1, η_2 as there.

*Steps 0–3* are unchanged; Step 0 uses β_K = β − ε. At level 1 the conditions [[eq:iii-g4-4-2]] of
[[prop:iii-g4-4-4]] hold for 2 ≤ Re α_0 < 2 + η_1 and ℓ_zf = ℓ_1: ℓ_1 − Re α_0 + 2 > β − 2 − η_1 − ε > 0 and ℓ_1 < 3, the
rest by [[def:iii-i13-1-1]] (c). At level 2, for 1 + η_1 ≤ Re α_0 < 2 + η_2 and ℓ_zf = ℓ_2:
ℓ_2 − Re α_0 + 2 > β − 3 − η_2 − ε > −ε_ind (η_2 + ε < ε_ind) and ℓ_2 − min(Re α_0 − 2, 0) < ℓ_2 + 1 − η_1 < 3; the
remainder exponents α_0 + ℰ_ind are treated in turn as there. [[lem:iii-i11-2-2]] at level 2 needs only the zf-weight
ℓ_2 > 0 of g_2, and gives g_3 the zf-weight ℓ_3.

*Step 4 for ℓ_3 > 0* (β > 4, where ℓ_3 = β − 4 − ε > 0 by [[def:iii-i13-1-1]]) is that of [[prop:iii-i11-3-1]].
*For ℓ_3 < 0* (β < 4), g_3 has no zf-term to remove, and the zero energy solve of level 3 ([[lem:iii-i11-2-1]] with
q_3) is omitted. While the tf-weight κ of the current level-3 forcing is at most β − 2 = 2 + ℓ_3 + ε, apply
[[prop:iii-g4-5-1]] with α_κ := κ ∈ (1, 2) (κ ≥ κ_3 = 1 + η_2 − 2ε > 1 and κ ≤ β − 2 < 2), ℓ_zf := ℓ_3 ∉ ℕ₀, the order
0 of the zf-index set, and w = ℓ_3 − κ + 2 ∈ [−ε, 1) ⊂ (−ε_ind, ℓ^max_K); its conditions w ≠ −μ and 2 − κ + j ≠ −μ hold
for ε off a finite set, the values of κ being κ_3 + i(ε_ind − ε). Each round leaves a remainder of tf-weight
κ + ε_ind − ε and the pieces σ³u; after finitely many rounds κ > β − 2, and, lowering κ if necessary,
κ ∈ (β − 2, β − 1 − ε). The rest, g_J (the level-3 forcing after the rounds), lies in H^(∞,(5/2−ε,κ,ℓ_3))_b and is
inverted by [[lem:iii-i2-4-2]] with β_scf := 3/2 − 2ε, β_tf := κ − 2, β_zf := ℓ_3,
β_tf − β_zf = κ − β + 2 + ε ∈ (0, 1) (ε off a finite set, [[def:iii-i13-1-1]] (c)):

    û_f ∈ H^(∞,(3/2−3ε,κ−2,ℓ_3))_b,          ḃ_f, S_f ∈ H^(∞,ℓ_3)_b(±(0, c], |dσ/σ|),     ℓ_3 > −1.

*Step 5.* The matching and the sorting are unchanged. In (iii), σ³û_f has zf-weight ℓ_3 + 3 = β − 1 − ε, and
σ³ĝ^aug(ḃ_f), σ³ĥ^aug(S_f) give the K⁺-weights ℓ_3 + 3 and ℓ_3 + 2 = β − 2 − ε ([[lem:iii-i11-2-4]] with a = ℓ_3 > −1);
the level-3 pieces of Step 4 have zf-weight at least α_κ > 1, so K⁺-weight above 2 ≥ β − 2 for β ≤ 4 (and as there for
β > 4). [[lem:iii-i10-2-4]] applies with β_tail := β − 3 − 2ε ∈ (−1, 1 + ε_K), not in ℕ₀ for ε off a finite set, and
(iii) contributes O(t_*^(−β+2+3ε)), as σ³ĥ^aug(S_f) has zf-weight ℓ_3 + 1 = β − 3 − ε > β_tail.

*Step 6.* The stationary columns vanish as there (w_v > 0). Of the towers listed there, those of rate below β − 2 are
the rows of 𝒩_σ ∩ 𝒩_β and, for β > 4, the towers of v^rot: for β ≤ 4 the s0, s2 and v1 towers of rate at least
Re α_0 ≥ 2 ≥ β − 2 are not among them; every tower of rate at least β − 2 has rate above β − 2
([[def:iii-i13-1-1]] (a)), so is O(t_*^(−β+2+3ε)); and the identification with m_ν(S_ν) holds up to terms of rate at
least Re e_ν + 3 > β − 2.

*Step 7* is unchanged, with β in place of α; it gives [[eq:iii-i13-2-1]]. ∎

**Lemma {#lem:iii-i13-2-2}** (The expansion at every level.) Let β ∈ (3, 4 + ε_K] be admissible, let (h, p⃗) be a base
point with black hole parameter b ∈ ℬ̄_*, with p⃗ ∈ 𝒫 and h ∈ 𝒳^∞ small, and let G ∈ 𝒴^♮(β). Suppose that the forward
solution u of L_(h,p⃗)u = G lies in ⋂_ε H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β′_+,w_0−ε)_b(Ω_*)^(•,−) with w_0 > 0, w_0 + a_K > β and
β′_+ ∈ (3/2 − (δ_♯ − ε_+), 3/2). Then

    u = Σ_(ν∈𝒩_β) m_ν(S_ν) + u^rot_β + ũ,     ũ ∈ ⋂_(ε>0) H^(∞,(⟨ℰ^C_I⟩,ℓ_I),β_+,β−2−ε)_b(Ω_*)^(•,−)    {#eq:iii-i13-2-2}

for every β_+ < min(3/2, min Re ℰ_+). Here u^rot_β is the sum of the terms of u^rot_ι ([[prop:iii-i10-3-1]]) with
Re λ_0 < β − 2 and of v^rot_β, for the forcing f′ of the proof; the coefficients S_ν = S^(h,p⃗,β)_ν(G) ∈ 𝒲_(τ,ℂ) are
determined by u − u^rot_β; u^rot_β and the S_ν are conjugation-symmetric, linear and continuous in G, with bounds
uniform for (h, p⃗) small and b ∈ ℬ̄_*. When h_(b,v1) = 0, in particular at b_0, u^rot_β is put into ũ. For β ∈ (2, 3),
[[lem:iii-i8-3-2]] holds for G ∈ 𝒴^♮(β).

*Proof.* The proof of [[lem:iii-i11-3-2]], with [[prop:iii-i10-3-1]] at β (as in the proof of [[prop:iii-i13-2-1]])
and [[prop:iii-i13-2-1]] in place of [[prop:iii-i11-3-1]]. Step 0 gives f′ ∈ 𝒴^♮(β) (the 𝒴^♮_2-part of G is
untouched, and (L − L_b)u lies in 𝒴⁰(β) as there). The rows of 𝒩_ι of rate at least β − 2 have rate above β − 2
([[def:iii-i13-1-1]] (a)), so their m_ν(S_ν) have K⁺-weight at least β − 2 − ε ([[lem:iii-i9-2-2]] (e)) and join ũ; so
do the terms χ_K t_*^(−λ_0)(log t_*)^j h_(b,v1)(V) of u^rot_ι with Re λ_0 > β − 2, whose rate Re λ_0 is that of the
triple (v1, λ_0, j). *Determination:* by [[cor:iii-i10-2-3]] on 𝒩_β, all rates there being below β − 2. For β ∈ (2, 3):
the space 𝒴(β) of [[sec:iii-i8-1]] records the ι⁺-exponents below 4 in ℰ_++ + 2 and has the plain weight 4 − ε above,
and 𝒴^♮_2(β) lies in it by [[lem:iii-i13-1-3]] (a). ∎

**Lemma {#lem:iii-i13-2-3}** (The coefficients near the reference point, at every level.) Fix b ∈ ℬ̄_*, and let p⃗_b be
as in [[lem:iii-i11-3-3]]. In [[lem:iii-i13-2-2]], if (h_j, p⃗_j) → (0, p⃗_b), G_j → G in 𝒴^♮(β), and the forward
solutions u_j of L_(h_j,p⃗_j)u_j = G_j and u of L_(0,p⃗_b)u = G satisfy the hypothesis of [[lem:iii-i13-2-2]] with
uniform bounds, then S^(h_j,p⃗_j,β)_ν(G_j) → S^(0,p⃗_b,β)_ν(G).

*Proof.* The proof of [[lem:iii-i11-3-3]], with [[lem:iii-i13-2-2]] in place of [[lem:iii-i11-3-2]]. ∎

**Proposition {#prop:iii-i13-2-4}** (The enlarged sources at the top level.) [[thm:iii-i11-4-1]] and
[[thm:iii-i12-3-1]] hold with F ∈ 𝒴^♮(α) in place of F ∈ 𝒴⁰(α), with the same conclusions.

*Proof.* Their proofs use F through [[prop:iii-i10-3-1]], [[prop:iii-i11-3-1]], [[lem:iii-i11-3-2]] and
[[lem:iii-i11-3-3]], [[prop:iii-i8-4-1]] at a level α′ ∈ (2, 3), and, in Steps 2 and 5 of the proof of
[[thm:iii-i12-3-1]], the statement that the ι⁺-exponents produced lie in ℰ_♯. Each holds for F ∈ 𝒴^♮ by
[[lem:iii-i13-1-3]], [[prop:iii-i13-2-1]] and [[lem:iii-i13-2-2]] (with β = α), and the class of [[sec:iii-i8-1]]
contains 𝒴^♮(α′) (the last sentence of [[lem:iii-i13-2-2]]). ∎

At a base point with black hole parameter b ∈ ℬ̄_*, [[prop:iii-i13-2-4]] is used inside [[prop:iii-i15-2-5]], as
[[thm:iii-i11-4-1]] is.

### The expansion at a general base point {#sec:iii-i15-2-7}

[[lem:iii-i12-2-3]] and [[lem:iii-i12-2-4]] use h_(b_0,v1) = 0: they put h̆¹_(b_0,v1)(V) in ker L_0, and they remove the
v1 content through an antiderivative. At a rotating b both steps change. This section gives their forms at every
b ∈ ℬ̄_*, with the rotation tower T_(v1,b) in place of the antiderivative, and with them the expansion of
[[thm:iii-i12-3-1]] at b.

*The rotation state at b.* h_(b,v1)(V) is δ*_(g_b) of a 1-form in ker □^Υ_b ([[eq:iii-d2-3-4]]), so it lies in
ker L̂_b(0) in the space 𝒳_0 of [[ch:s18]], and it is O(|b − b_0||V|) ([[lem:iii-i15-1-1]] (P3)). Near b_0 that
nullspace has the dimension it has at b_0, with the continuous basis ġ_b(ḃ), the gauge-corrected state of
[[eq:iii-f3-2-1]], and h_b(S) (the proof of [[prop:iii-h-3-2]], where the matrix B(b) is invertible). So
h_(b,v1)(V) = ġ_b(ḃ_V) + h_b(S_V), with |ḃ_V| + |S_V| = O(|b − b_0||V|). Moreover S_V = 0: the pullback by the
element −1 of SO(4) fixes h_(b,v1)(V) and ġ_b(ḃ_V) and reverses h_b(S_V) ((P3)), so h_b(S_V) = 0, and S_V = 0 by the
injectivity of S ↦ h_b(S) ([[lem:iii-i10-2-2]] at b, for the s1 states alone). Hence

    h_(b,v1)(V) = ġ_b(ḃ_V),          ker h_(b,v1) = 𝒱⁰_b := {V : ḃ_V = 0}.

*Notation.* In this section L_0 := L̂_b(0), L_1 := [L_b, t_*], L_2 := ½[[L_b, t_*], t_*]; h := h_(b,s1),
h̆^j := h̆^j_(b,s1); 𝒢_* is the space of sections conormal at ∂X of order above −3 ([[lem:iii-i12-2-3]]); and

    T_(v1,b)(aV) := Σ_j a^((j)) h̆^j_(b,v1)(V),     h̆⁰_(b,v1) := h_(b,v1),

is the v1 tower T_v1 of [[sec:iii-i12-1]] at b, the tower of the rotation rows of [[def:iii-i14-1-3]]. Put

    κ_b(V) := h̆¹_(b,v1)(V),          L_0κ_b(V) = −L_1ġ_b(ḃ_V).                                         {#eq:iii-i15-2-6}

The identity holds by the tower relation L_0h̆¹_(b,v1)(V) = −L_1h_(b,v1)(V) and the formula for h_(b,v1) above. At b_0,
κ_(b_0)(V) = h̆¹_(b_0,v1)(V) lies in ker L_0.

**Lemma {#lem:iii-i15-2-9}** ([[lem:iii-i12-2-3]] and [[lem:iii-i12-2-4]] at b.) Let b ∈ ℬ̄_*.

(a) If p ∈ 𝒢_* and L_0p = 0, then p = Σ_ψ h̆^((μ_ψ),0)_(b,τ_ψ)(Y_ψ) + κ_b(V) + ġ_b(ḃ) + h(S), the sum over the rows
of ℛ′ other than v1, with V ∈ 𝒱⁰_b and unique coefficients.

(b) If X ∈ 𝒢_* and L_0X = L_1ġ_b(ḃ) + L_1h̆¹(S) + L_2h(S), then ḃ + ḃ_(V_X) = 0, where V_X is the v1 coefficient that
the reduction of X in the proof of [[lem:iii-i12-2-3]] removes at the root −1. The statement on s1 is as at b_0.

(c) [[lem:iii-i12-2-4]] holds at b, with [[eq:iii-i12-2-4]] read as

    χ_K Σ_i y_i p_i = χ_K(Σ_(ψ≠v1) T_(ψ,b)(a_ψ) + T_(v1,b)(a_v1) + h^(≤1)_(b,s1)(a_s) + ġ_b(a_b)) + w″.

The exponents are as there; those of a_v1 lie in ⋃_i E_i + ℕ₀ − 1, and those of a_b have real part at least β − 1. The
constants are uniform on ℬ̄_*, and no map V ↦ h_(b,v1)(V) is inverted.

*Proof.* (a) and (b). Run the reduction of the proof of [[lem:iii-i12-2-3]] at b, with the states at b ((P3)). At the
v1 root −1, subtract κ_b(V), whose leading coefficient is h̄_v1(V), independent of b ((P3)). By [[eq:iii-i15-2-6]] this
adds L_1ġ_b(ḃ_V) to the right side. So the reduced section X_1 ∈ 𝒜¹ satisfies

    L_0X_1 = L_1ġ_b(ḃ + ḃ_(V_X)) + L_1h̆¹(S + S′) + L_2h(S + S′).

[[eq:iii-h-2-2]] and [[prop:iii-h-3-2]] at b ((P4)), applied as in the proof of [[lem:iii-i12-2-3]] (b), give
ḃ + ḃ_(V_X) = 0 and S′ = −S. This is (b). For (a), p is (b) with ḃ = 0 and S = 0, so ḃ_V = 0. The rest is as at b_0,
the nullspace of [[prop:iii-f3-4-1]] at b being spanned by ġ_b and h_b.

(c) The removal of pairs proceeds as at b_0. By (a), the coefficient section of the first pair (z_0, k_0) is

    P = Σ_ψ h̆^((μ_ψ),0)_(b,τ_ψ)(Y_ψ) + κ_b(V) + ġ_b(ḃ) + h(S),     V ∈ 𝒱⁰_b.

Two steps change. Write a := χ_+t_*^(−z_0)(log t_*)^(k_0), and let ã be its antiderivative.

*The v1 part of P.* Subtract T_(v1,b)(ãV). Its bottom ã h_(b,v1)(V) vanishes, as V ∈ 𝒱⁰_b = ker h_(b,v1), and its next
term is aκ_b(V). It is a tower, so L_b of it involves a″ and higher only, and has K⁺-order Re z_0 + 2 ≥ β. Its
coefficient ãV enters a_v1 at the exponent z_0 − 1, and a_s is unchanged; this is why the exponents are as at b_0.

*The ġ part of P.* If Re z_0 + 1 ≥ β, subtract ġ_b(aḃ) as at b_0. Otherwise the next coefficient gives L_0P_1 = z_0L_1P,
and with the tower relations L_0X = z_0L_1ġ_b(ḃ) for a section X ∈ 𝒢_*. By (b), z_0ḃ = −ḃ_(V_X). Put V″ := −V_X/z_0,
so that ḃ_(V″) = ḃ, and subtract T_(v1,b)(aV″) instead of ġ_b(aḃ). Its bottom is a h_(b,v1)(V″) = aġ_b(ḃ_(V″)) =
aġ_b(ḃ), as required, and L_b of it involves a″ and higher. Its next term, a′κ_b(V″), carries the v1 content V_X that
the reduction at the next pair would remove; that content is therefore removed here, at the earlier pair.

The new terms are again compatible: a companion a^((j))h̆^j has the exponent z + j and the degree μ − j, as at b_0.
|V″| ≤ C|V_X|, with C depending only on |z_0|⁻¹, and Re z_0 ≥ β − 2 > 1. The coefficients are read off leading
coefficients, which are independent of b ((P3)) or, for ġ_b, smooth in b; so the bounds are uniform on ℬ̄_*. ∎

**Corollary {#cor:iii-i15-2-10}** ([[thm:iii-i12-3-1]] at b.) Let α > 4 be admissible, b ∈ ℬ̄_*, and (h, p⃗) a small
base point with black hole parameter b. Let G ∈ 𝒴^♮(α), let u_0 be the forward solution of L_(h,p⃗)u_0 = G, and let
u = u_0 − Σ_(ν∈𝒩″) m_ν(W_ν), where 𝒩″ is a finite set of rows of 𝒩 and of rotation rows
m_ν(W) = χ_K T_(v1,b)(a_ν W), a_ν = t_*^(−λ)(log t_*)^k, (λ, k) ∈ ℰ_♯ ∩ {Re ≤ 2}, W ∈ 𝒱_(1,ℂ) ([[def:iii-i14-1-3]]).
Suppose that u has the K⁺-weight α − 2 − ε and the ι⁺- and ℐ⁺-data of [[eq:iii-i11-4-2]]. Then
[[eq:iii-i12-3-1]]–[[eq:iii-i12-3-3]] hold at b, uniformly in b, with h^(≤1)_(b,s1), ġ_b and the towers T_(ψ,b) at b in
place of those at b_0, the v1 tower being T_(v1,b). Two changes are needed:

- Step 2 of the proof uses [[lem:iii-i15-2-9]] (c) in place of [[lem:iii-i12-2-4]], so that the v1 coefficients and
  the early ġ terms enter through the rotation towers T_(v1,b).

- The conormal towers C of Step 1 (viii) include T_(v1,b)(Y^c_v1), and Ẏ_v1 := a_v1 + Y^c_v1. At b the level-3
  conormal rotation tower has the K⁺-rate α_κ + 2 ∈ [3 + η_2 − 2ε, 4), below α, since its bottom h_(b,v1) need not
  vanish. The space [[eq:iii-i12-3-2]] admits this coefficient (w_v1 = 3 + η_2 − 2ε), and L_b of it has K⁺-order
  α_κ + 5 > α.

The solution of [[thm:iii-i11-4-1]] at b_0 and the solution of [[prop:iii-i15-2-5]] with q = 0 at b are of this form,
by [[lem:iii-i9-2-6]] (c) and [[eq:iii-i15-1-1]].

*Proof.* The proof of [[thm:iii-i12-3-1]] uses its setting only through the hypothesis stated here (the remark after
that proof), with [[prop:iii-i13-2-4]] for G ∈ 𝒴^♮(α). Step 0 at b: [[lem:iii-i13-2-2]] at β = α gives
u_0 = u_I + u_ι + v as there, the spacetime and spectral v1 terms u^rot_ι and v^rot being polyhomogeneous towers of the
types (ii) and (vi) of Step 1; and L_b u has K⁺-order α − ε by the tower relations, L_b m_ν involving only the top of
the tower for the rotation rows as for the other rows (of K⁺-order Re λ + 4 > α). Step 1 is unchanged at b: its pieces
are those of (P2)–(P4). Step 2 is the assembly, with [[lem:iii-i15-2-9]] (c) in place of [[lem:iii-i12-2-4]]. Steps 3–6
are unchanged, with the conormal rotation tower of the second change in C. ∎
