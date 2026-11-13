## The expansion at the Kerr face {#ch:s22}

This chapter proves, in dimension 4 + 1, [Hin26, Theorem 11.59] and its proof (pp. 278–292). With the correction
terms of the fourth kind of [[ch:s21]], the forward solution of the linearised gauge-fixed Einstein equation, for a
source of K⁺-order α ≤ 4 + ε_K, is made to decay at K⁺ at the order α − 2 by a unique choice of the modification
parameters ([[thm:iii-i11-4-1]], the form of [Hin26, (11.222)] in dimension 4 + 1). The solution so obtained is,
modulo a remainder of K⁺-order α, a sum of towers of the zero energy states whose coefficients are functions of t_*:
partially polyhomogeneous, except for a conormal boost coefficient of order α − 2 and a conormal black hole parameter of
order α − 1; and it is partially polyhomogeneous at ι⁺ with an index set ℰ_♯ to the order 3 + η_2, where η_2 < ε_+ is
as close to ε_+ as desired ([[thm:iii-i12-3-1]], the form of [Hin26, (11.196)] in dimension 4 + 1). The expansion is
also obtained at every level β ∈ (3, 4 + ε_K], and for the enlarged sources that the linearisation in the black hole
parameters of [[ch:s23]] produces ([[sec:iii-i13-2]]).

The argument has two phases. In spacetime ([[sec:iii-i10-3]]) the ι⁺-terms of the source of u-exponent below 2 are
solved by the ι⁺-normal operator up to the K⁺-order α ≤ 4 + ε_K, and the K⁺-terms this produces below the order α − 2
are identified as rows. What is left is a forward problem whose source is partially polyhomogeneous at ι⁺ from the order
4 on; it is solved on the spectral side ([[sec:iii-i11-3]]), through four zero energy solves, at the Taylor levels 0 to
3 at zero frequency, and the transition face model between them. The rows are then eliminated by the choice of the
parameters ([[sec:iii-i11-4]]), and the solution is expanded at K⁺ modulo the order α ([[sec:iii-i12-3]]).

The dimension changes the scheme of [Hin26] in these places. (1) Under the hypothesis (C5) below, the K⁺-range of the
ι⁺-normal operator is ℓ^max_K = 3, so [[cor:iii-g2-4-3]] solves the term at a u-exponent λ_0 with Re λ_0 < 2 with
ℓ_K = α − Re λ_0 for every α ≤ 4 + ε_K; [Hin26] uses its Proposition 9.11 at the exponent 1 only (Steps 2.A.2 and 4.1
of its proof). The rows this produces are all the rows of [[sec:iii-i9-1]] with Re λ < 2, and they are identified
through the towers ([[lem:iii-i10-2-1]]). (2) The parameter exponents, which [Hin26] builds after the proof by the
procedure of its (11.186), are fixed in advance ([[def:iii-i10-1-1]]), with logarithmic orders that grow with the real
part. The rows' own sources never pass through the construction, since f^ν = Lm_ν + r^ν exactly ([[lem:iii-i9-2-6]]);
this is how the self-consistency of [Hin26, Remark 11.62] enters. (3) Two further conditions are needed: (H4),
ℓ_I > 3 + ε_+, and the gap condition (G) on ε_K. (4) The zero frequency Taylor expansion of the transformed source has
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
near K⁺, the spacetime tower of the inverse transform of its scalar coefficient. (10) Below the order 4 the source of the
last Taylor level has a negative zero frequency weight; the zero energy solve of that level then drops out
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
𝒲_τ (with 𝒲_v1 = 0), the index sets ℰ_rows and ℰ_src with [[eq:iii-i9-1-3]], and the source spaces 𝒴_1(α), 𝒴_2(α),
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
2ℰ_+. The row exponents of real part at least 2 enter only through f^ν_(h,p⃗) = L_(h,p⃗)m_ν + r^ν_(h,p⃗), where r^ν_(h,p⃗)
carries no index set ([[eq:iii-i9-2-5]]).

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

    ℰ_par := ℳ ∪ {(λ + j, k) : λ ∈ Λ, 2 ≤ Re λ ≤ 3, k ≤ k̄(λ), j ∈ ℕ₀}.                                  {#eq:iii-i10-1-2}

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
