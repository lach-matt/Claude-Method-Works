## The loss of the tame estimates and the constants of the settling theorem {#ch:explicit-constants}

The proof of [[thm:settling]] applies the Nash–Moser theorem [[thm:ii-g-2-1]] to the gauge-fixed Einstein equation
with the tame estimates of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]. It applies it with one loss d of b-regularity
that does not depend on the order, at least the loss with which those estimates are proved ([[thm:iii-k-3-2]],
[[thm:loss-d]]), and [[thm:ii-g-2-1]] then asks smallness in the regularity N_NM = 21d + 6. The threshold λ1 on the
wavelength and the threshold δ on the data in [[thm:settling]] are produced by the proof, and are positive. This
chapter states what the proof makes explicit about d, N_NM, δ and λ1.

The loss of the tame estimates is a number d_acc assigned by the rules of [[lem:iii-j2-1-2]] to the composition of
model inverses, transforms and differential operators that the proofs of [[ch:s19]]–[[ch:s23]] perform
([[def:ec-accounted-loss]]), and d ≥ d_acc. Its elementary losses have closed forms in the weights, the threshold
quantities of the operators, the index sets and the order of the bounds of the background terms ([[lem:ec-closed-forms]],
[[rem:ec-other-losses]]), and the loss of the forward solution operators is at most 20,180 ([[thm:fwd-loss]],
[[cor:fwd-near-b0]]); the iterations of the construction contribute their numbers of steps, among them three nested ones;
and at one parameter point of the gauge and damping parameters two of these iterations alone make d_acc, and so d, larger
than 1.403 × 10²⁰ and N_NM larger than 2.946 × 10²¹, each of their steps being charged at least one derivative for the
inverse of the model at the transition face, whose incoming threshold is non-negative ([[lem:ec-theta-in]],
[[thm:loss-d]]), and larger than 1.2497 × 10²⁴ and 2.624 × 10²⁵ for the index sets as the proofs construct them
([[cor:uc-two-offsets]]). At that point, at one admissible choice of the weights and of the free orders and inner
products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
is proved ([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not the optimal loss. The
same formulas bound λ1 by δ, δ by a power of 2 that decreases with d, and the modulus of the initial family
([[prop:iii-k-1-2]]) at 2δ by a power of 2 that decreases with d ([[prop:ec-delta-cap]]). The chapter ends with the parts
of the first constants of the linear theory that are in hand, and with the places where explicit evaluation stops
([[rem:ec-not-evaluated]]).
No result of this chapter is used in the proof of any theorem of this paper outside it. Other chapters state explicit
values that rest on it, the indices of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]], which [[prop:fwd-calculus]] proves, and
the value N′ = 13 of [[ch:s06]], which rests on [[lem:fwd-orders]]; these values are used only in this chapter.

### The computational point {#sec:ec-point}

**Definition {#def:ec-point}** (The computational point.) The *computational point* is the choice of the gauge and
constraint damping parameters of [[ch:s13]] and [[ch:s14]]

    γ_C = 10⁶  (h = 1/γ_C = 10⁻⁶),     γ_Υ = e_Υ = 1/100,     (v_C, e_C) = (1/2, 1/102400),

the last pair as fixed in [[eq:iv4-0-1]]. At it

    z := 4e_Υγ_Υ² = 4·10⁻⁶,     λ_♯ := 3/2 + (1 − e_Υ)γ_Υ = 15099/10000,

and, by [[cor:s14-eps-ind-point]], ε_ind(10⁻⁶) = δ_50, where 1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸
([[lem:s14-delta50]]). We write δ̄ := 1.94137057·10⁻⁸, so that δ_50 < δ̄.

**Remark {#rem:ec-point-outside}** (The computational point and the proved set.) [[thm:settling]] takes h in the set 𝖧
of [[eq:iv4-0-1]], whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most 10⁻⁶; so h = 10⁻⁶ is not in 𝖧
([[rem:s14-eps-ind-scope]]). The parameters γ_Υ and e_Υ are required in [[thm:vi-c-2-1]] to lie below thresholds whose
existence is proved and whose values are not determined; whether (γ_Υ, e_Υ) = (1/100, 1/100) lies below them is not
decided. So the computational point is a point at which the formulas of the proof can be evaluated, not one at which
the hypotheses of [[thm:settling]] are shown to hold. Every number of this chapter that depends on the point is stated
at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and the lower bound of
[[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ)
([[lem:ec-gauge-gap]], [[prop:ec-rounds]]).

### Sums of the gauge potential offsets {#sec:ec-gap-sums}

The gap condition (G) of [[def:iii-i10-1-3]] excludes exponents in windows just above 2 and 3. This section shows
that at the gauge parameters of the computational point the numbers of the set 𝒮 of [[prop:gap-sums]], built from
2, 3, λ_♯ and the gauge potential offsets defined below, stay out of those windows by a margin larger than δ_50, so
that, on these exponents, (G) imposes nothing beyond ε_K < ε_ind ([[rem:gap-sums]]). The elementary bounds, for
a > 0 and 0 ≤ y ≤ 8a²,

    a + y/(2a) − y²/(8a³) ≤ (a² + y)^(1/2) ≤ a + y/(2a),                                                {#eq:ec-sqrt}

follow from (a + y/(2a))² = a² + y + y²/(4a²) and (a + y/(2a) − y²/(8a³))² = a² + y − (y³/(8a⁴))(1 − y/(8a²)).

Let z = 4·10⁻⁶ and λ_♯ = 15099/10000 as in [[def:ec-point]]. For l ≥ 1 let d₁(l) and d₂(l) be the numbers d₁ and d₂ of
[[prop:np-10-52]] (i) at u = l + 1, so that ι^Υ_(sl,l+1) = l + 1 + d₂(l) and ι^Υ_(sl,l+2) = l + 2 + d₁(l), and recall
ι^Υ_(s0,2) = ½ + (9/4 + z)^(1/2) ([[sec:s14-simple]]). Put

    𝔡₀ := ι^Υ_(s0,2) − 2 = (9/4 + z)^(1/2) − 3/2,     𝔡₁ := ι^Υ_(s1,2) − 2 = d₂(1),
    δ₂ := d₂(2),     δ′₁ := d₁(1).

By [[def:iii-i9-gap]], 𝔡₀ = d_c0 and 𝔡₁ = d_c1 are the offsets of the two class roots.

**Proposition {#prop:gap-sums}** (Sums of the offsets above 2 and 3.) Let 𝒮 be the set of the numbers g + t + n𝔡₁
with g ∈ {2, 3, λ_♯}, t ∈ {0, 1, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁} and n = 0, 1, 2, …. The least positive number of the form
s − k with s ∈ 𝒮 and k ∈ {2, 3} is

    λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸),

and every other positive s − k exceeds 1.3888·10⁻⁷. In particular no element of 𝒮 lies in (2, 2 + ε] ∪ (3, 3 + ε]
when ε < 5.019·10⁻⁸, a bound more than 2.5 times δ_50.

*Proof.* *The offsets.* By [[eq:ec-sqrt]], 𝔡₀ = z/(3/2 + (9/4 + z)^(1/2)) lies between z/(3 + z/3) and z/3, so
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶. By [[prop:np-10-52]] (i), δ₂ = z(1 + θ₂)/15 and δ′₁ = 3z(1 + θ₁)/20
with |θ₁|, |θ₂| ≤ z by [[eq:s14-theta]], so 2.666655·10⁻⁷ < δ₂ < 2.666678·10⁻⁷ and 5.999975·10⁻⁷ < δ′₁ < 6.000025·10⁻⁷.
For 𝔡₁, at u = 2, 𝔡₁ = ½((9 + B₂)^(1/2) − 3) = B₂/(2(3 + (9 + B₂)^(1/2))) with B₂ := 2z − 4w₂ and
w₂ := (4 + A₂)^(1/2) − 2 = A₂/(2 + (4 + A₂)^(1/2)), A₂ := z + z²/4 = 4.000004·10⁻⁶. By [[eq:ec-sqrt]],
4 + A₂/4 − A₂²/64 ≤ 2 + (4 + A₂)^(1/2) ≤ 4 + A₂/4, with A₂/4 = 1.000001·10⁻⁶ and A₂²/64 < 2.6·10⁻¹³; so

    1.00000074999956·10⁻⁶ < w₂ < 1.00000074999963·10⁻⁶,     3.99999700000147·10⁻⁶ < B₂ < 3.99999700000177·10⁻⁶,

and, again by [[eq:ec-sqrt]], B₂/(12 + B₂/3) ≤ 𝔡₁ ≤ B₂/(12 + B₂/3 − B₂²/108), whence

    3.333330462964·10⁻⁷ < 𝔡₁ < 3.333330462967·10⁻⁷.

*The sums.* For g, t, k fixed put y := k − g − t. If y < 0, then s − k ≥ −y for every n. If y ≥ 0, the least
positive s − k is ⌈y/𝔡₁⌉𝔡₁ − y when y/𝔡₁ ∉ ℤ, and 𝔡₁ when y/𝔡₁ ∈ ℤ, in particular when y = 0. The triples are:

- y < 0: g = 3 with k = 2, or with k = 3 and t ≠ 0; g = 2 with t ≠ 0 and k = 2; g = λ_♯ with t ≠ 0 and k = 2. Then
  −y ≥ 0.5099. Further g = 2, k = 3 with t = 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁, giving −y = 𝔡₀, δ₂, δ′₁, all above
  2.6·10⁻⁷.
- y = 0: (g, t, k) = (2, 0, 2), (2, 1, 3), (3, 0, 3), giving 𝔡₁ > 3.3·10⁻⁷.
- y > 0: y = 1 for (2, 0, 3); y = 0.4901 for (λ_♯, 0, 2) and (λ_♯, 1, 3); y = 1.4901 for (λ_♯, 0, 3); and
  y = 0.4901 − 𝔡₀, 0.4901 − δ₂, 0.4901 − δ′₁ for (λ_♯, t, 3) with t = 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁.

With the bounds above, y/𝔡₁ lies in the following intervals, and ⌈y/𝔡₁⌉𝔡₁ − y in the last column:

| y | y/𝔡₁ | ⌈y/𝔡₁⌉ | ⌈y/𝔡₁⌉𝔡₁ − y |
|---|---|---|---|
| 1.4901 | (4470303.84942, 4470303.84943) | 4470304 | (5.0190·10⁻⁸, 5.0193·10⁻⁸) |
| 1 | (3000002.58333, 3000002.58334) | 3000003 | (1.38888·10⁻⁷, 1.38890·10⁻⁷) |
| 0.4901 | (1470301.26609, 1470301.26610) | 1470302 | (2.4463·10⁻⁷, 2.4464·10⁻⁷) |
| 0.4901 − 𝔡₀ | (1470297.26608, 1470297.26610) | 1470298 | (2.4463·10⁻⁷, 2.4464·10⁻⁷) |
| 0.4901 − δ₂ | (1470300.46608, 1470300.46610) | 1470301 | (1.7796·10⁻⁷, 1.7798·10⁻⁷) |
| 0.4901 − δ′₁ | (1470299.46608, 1470299.46610) | 1470300 | (1.7796·10⁻⁷, 1.7798·10⁻⁷) |

Each interval for y/𝔡₁ follows by dividing y, with the bounds on 𝔡₀, δ₂, δ′₁, by the two bounds on 𝔡₁; each lies
strictly between consecutive integers, so the ceiling is as listed, and the last column follows from the bounds on 𝔡₁
and on the offsets. The least value is the first, at g = λ_♯, t = 0, k = 3 and n = 4470304; every other value is at
least 1.38888·10⁻⁷. Finally 5.0190·10⁻⁸/δ_50 > 2.58 by [[lem:s14-delta50]]. ∎

**Remark {#rem:gap-sums}** (The gap condition.) The gap condition (G) of [[def:iii-i10-1-3]], assumed in
[[thm:settling]], has three windows: no ν in the exponent set Λ of [[def:iii-i10-1-1]] has real part in
(2, 2 + ε_K] or in (3, 3 + ε_K], and no ν + d_c0 or ν + d_c1, ν ∈ Λ, has real part in (2, 2 + ε_K]; here
d_c0 = 𝔡₀ and d_c1 = 𝔡₁. The set Λ contains 2, 3 and λ_♯ and is closed under the increments
π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}. If these increments include 𝔡₁, 1 + 𝔡₀, 1 + δ₂ and 1 + δ′₁, then 𝒮 ⊂ Λ: 𝒮 is the set of
sums of one of the generators 2, 3, λ_♯, any number of increments 𝔡₁ and at most one increment of integer part 1,
and a sum with two increments of integer part 1 is at least λ_♯ + 2 > 3 + ε_K, so it misses all three windows. By
[[prop:gap-sums]] no element of 𝒮 lies in the first two windows when ε_K < 5.019·10⁻⁸. The third window adds
nothing: for ν = g + n𝔡₁ ∈ 𝒮 (t = 0), ν + 𝔡₁ − 2 = s − 2 and ν + 𝔡₀ − 2 = s′ − 3 with s = g + (n + 1)𝔡₁ and
s′ = g + (1 + 𝔡₀) + n𝔡₁ in 𝒮, so by [[prop:gap-sums]] again neither ν + 𝔡₁ nor ν + 𝔡₀ lies in (2, 2 + ε_K] when
ε_K < 5.019·10⁻⁸; every other ν ∈ 𝒮 is at least λ_♯ + 1 > 5/2, so that ν + d_c0 and ν + d_c1 exceed 2 + ε_K.
[[thm:settling]] takes ε_K < ε_ind(h) ≤ δ_50 < 5.019·10⁻⁸ for every h ∈ 𝖧; so these sums impose no condition beyond
those of [[thm:settling]]. Besides this remark, [[cor:is-flat]] uses [[prop:gap-sums]], and [[lem:ec-gauge-gap]] and
[[lem:sp-roots]] use the bounds on the offsets that its proof gives. For the index sets as the proofs construct them, Λ
contains further sums, and (G) holds exactly for ε_K < μ_G ≈ 1.6416·10⁻¹⁴ ([[thm:is-gap]]).

### The accounted loss {#sec:ec-accounted}

[[lem:iii-j2-2-1]] lists the elementary tame families from which the inventory of [[sec:iii-j2-3]] builds the solution
map of [[thm:iii-i14-3-1]] and the right inverse of [[thm:iii-j1-2-1]], and [[lem:iii-j2-1-2]] gives the rules by which
losses combine. Applied as written, these rules assign a number to every construction.

**Definition {#def:ec-accounted-loss}** (The accounted loss.) Assign to each elementary family of [[lem:iii-j2-2-1]]
the loss that its statement, or the proof of the statement cited there, fixes; to a composition the sum of the losses
of its factors ([[lem:iii-j2-1-2]] (b), (e), (f)); to a sum, a finite-rank assembly or a family with several
components the largest of the losses of its parts ([[lem:iii-j2-1-2]] (a), (c)); and to a construction that composes
m applications of one step, each taking the previous output as input, the sum of the m losses. The *accounted loss*
d_acc is the number so assigned to the larger of the two constructions of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]],
for given choices of the weights, the orders and the inner products that the proofs leave free.

By [[lem:iii-j2-1-2]], [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d := d_acc. Every rule of
[[lem:iii-j2-1-2]] gives an upper bound, so d_acc bounds the least loss with which the estimates hold from above, and
may exceed it. Each elementary loss is a non-negative integer, so d_acc is at least the sum of the losses of any
family of steps that are composed one after another in the construction.

[[thm:ii-g-2-1]] is applied in the proof of [[thm:iii-k-3-2]] with N_NM = 21d_NM + 6, where d_NM is the largest of
the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]]: that of [[lem:iii-k-2-3]], a construction,
accounted by [[def:ec-accounted-loss]], and the other two as their proofs fix them. As (iii) of [[thm:ii-g-2-1]] asks
[[eq:ii-g-2-4]] of the right inverse of [[lem:iii-k-2-3]], whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc
([[thm:loss-d]]).

One threshold enters the lower bounds below: the incoming threshold ϑ_in of [[eq:i-a-1-5]] of the transition face
model N_tf(L_b^(·), ±1) of [[cor:iii-f1-3-4]], taken, as its proof takes it, for 2L_b, which has the form (H1)–(H2) of
[[sec:i-a-1-3]] ([[lem:iii-f-2-1]]). It bounds from below the decay orders that the proof takes at the incoming
radial sets, and its sign is fixed by the structure of L_b at infinity. For an operator with (H1)–(H2), a = A_1(0)
denotes the coefficient of ρ∂_ρ at ρ = 0 in [[eq:i-c-1-2]].

**Lemma {#lem:ec-theta-in}** (The incoming threshold of the transition face model.) (a) Let P̂ satisfy (H1)–(H2) and
put A := 2 Id − a. For every fibre inner product h, at every point of ∂X,

    p_in − (S + S^(∗h)) = −2 Re_h(A + S),                                                               {#eq:ec-theta-in}

and ϑ_in ≥ −2 Re μ for every eigenvalue μ of A + S at any point of ∂X.

(b) For P̂ = (2L_b)^(σ), with L_b the operator of [[ch:s15]], A + S is the endomorphism of the model 2L̄ of
[[ch:s15]]; extended to {|x| > 0} as homogeneous of degree 0, as S̄ is in [[eq:iii-f-2-2]], it satisfies there

    ρ(A + S) = −Ē^C ι_(ḡ⁻¹ζ) Ḡ + (ζ ⊗_s ·) Ē^Υ Ḡ,        ζ := dt̄ + d|x|,                             {#eq:ec-theta-in-l}

and at every point of ∂X it has a kernel of dimension at least 5. Hence the incoming threshold ϑ_in of (2L_b)^(σ),
and that of N_tf((2L_b)^(·), ±1), is non-negative in every fibre inner product.

*Proof.* (a) By (H2) and [[eq:i-c-1-2]], near ∂X,

    ρ⁻²P̂(0) = (−(ρ∂_ρ)² + 2ρ∂_ρ) Id − A ρ∂_ρ + B + ρR,

with A = A(ω), B a family of operators on 𝕊³ (angular derivatives of order at most 2 and terms of order 0) and
R ∈ Diff²_b. For the density ρ⁻⁵dρ dω the formal adjoint of ρ∂_ρ is −ρ∂_ρ + 4, so
(ρ²·ρ∂_ρ)^† = −ρ²·ρ∂_ρ + 2ρ² and (ρ²(ρ∂_ρ)²)^† = ρ²((ρ∂_ρ)² − 4ρ∂_ρ + 4), and ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ) is formally
self-adjoint. Let H be the matrix of h, smooth in (ρ, ω) up to ρ = 0. Then
Im_h(ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ) Id) = (2i)⁻¹H⁻¹[H, ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ)], each of whose terms carries ρ∂_ρH ∈ ρC^∞, so
it lies in ρ³(C^∞ρ∂_ρ + C^∞). Next (ρ²A ρ∂_ρ)^(∗h) = H⁻¹(−ρ²·ρ∂_ρ + 2ρ²)A^∗H = −ρ²A^(∗h)ρ∂_ρ + ρ²C^∞, so
Im_h(−ρ²A ρ∂_ρ) = iρ² Re_h(A) ρ∂_ρ + ρ²C^∞. The h-adjoint of ρ²B has no ρ∂_ρ-term. By [[rem:i-a-hypotheses]] (a),
Im_h P̂(0) ∈ ρ²Diff¹_b, and so are the imaginary parts of the other terms; hence Im_h(ρ³R) ∈ ρ³Diff²_b ∩ ρ²Diff¹_b,
which is ρ³Diff¹_b. Altogether ρ⁻¹Im_h P̂(0) is i Re_h(A) ρ²∂_ρ plus terms with angular derivatives and terms
vanishing at ρ = 0. As ρ²∂_ρ = −∂_r has symbol −iξ at ξ dr + rη ([[lem:i-a-4-4]] (a)), and the angular terms have
symbols linear in η, p_in = i Re_h(A)(−i)(−2) = −2 Re_h(A) at ρ = 0. With S + S^(∗h) = 2 Re_h S this is
[[eq:ec-theta-in]]. If (A + S)v = μv with v ≠ 0 at a point of ∂X, then
h(Re_h(A + S)v, v) = Re h((A + S)v, v) = (Re μ) h(v, v); so the h-self-adjoint Re_h(A + S) has an eigenvalue at most
Re μ there, p_in − (S + S^(∗h)) has one at least −2 Re μ, and ϑ_in ≥ −2 Re μ.

(b) By [[lem:iii-f-2-1]] (3), (H2) holds with S = S̄ near infinity, and (2L_b)^(0) − (2L̄)^(0) ∈ ρ⁴Diff²_b changes
only R; so A + S is that of 2L̄. As (2L̄)^(0) is homogeneous under dilations of x, in the Cartesian frame A has
coefficients that depend on ω = x/|x| alone, and so has S̄ ([[eq:iii-f-2-2]]); both extend to {|x| > 0} as
homogeneous of degree 0, and the value of A + S at a point of ∂X is their value at every x on the ray it ends. We
compute A and S̄ as endomorphisms of the fibres of S²T*: a change of frame by a matrix function of ω commutes with
ρ∂_ρ, conjugates A and S alike, and adds only terms that belong to B. In the Cartesian frame □̄ acts componentwise,
and its stationary part is −Σ_i ∂²_(x^i) = ρ²(−(ρ∂_ρ)² + 2ρ∂_ρ + Δ_(𝕊³)) on each component; so □̄ contributes nothing
to A. The other terms of [[eq:iii-f-2-1]] are of order at most 1. On stationary sections, in
(t_*, x), the Cartesian derivative ∂_(t̄) = ∂_(t_*) acts as 0 and ∂_(x^i) acts as ∂_(x^i)|_(t_*) =
(x^i/|x|)∂_r + (tangential derivatives); so the ∂_r-coefficient of ∂_μ is (d|x|)_μ. As in the proof of
[[lem:iii-f-2-1]] (2), the ∂_r-coefficient of δ̄*ω = sym ∂ω is d|x| ⊗_s ω, and that of δ̄h = −ḡ^(μν) ∂_μ h_(ν·) is
−ι_(ḡ⁻¹d|x|)h. So the ∂_r-coefficient of 2L̄ − □̄ on stationary sections is 2(−Ē^C ι_(ḡ⁻¹d|x|) Ḡ +
(d|x| ⊗_s ·) Ē^Υ Ḡ), and as ∂_r = −ρ²∂_ρ this term is −ρ²A ρ∂_ρ with

    ρA = 2(−Ē^C ι_(ḡ⁻¹d|x|) Ḡ + (d|x| ⊗_s ·) Ē^Υ Ḡ)     on {|x| > 0}.

Adding [[eq:iii-f-2-2]], ρS̄ = −Ē^C ι_(ḡ⁻¹dt_*) Ḡ + (dt_* ⊗_s ·) Ē^Υ Ḡ, and using dt_* + 2d|x| = dt̄ + d|x| = ζ gives
[[eq:ec-theta-in-l]]. Its first term is ι_(ḡ⁻¹ζ)Ḡ : S²T* → T* followed by −Ē^C, and its second is Ē^ΥḠ : S²T* → T*
followed by ζ ⊗_s ·. So at every x with |x| > 0, where ρ ≠ 0, A + S vanishes on the common kernel of two linear maps
from the fibre of S²T*, of dimension 15, to that of T*, of dimension 5, and that kernel has dimension at least
15 − 10 = 5. By homogeneity, so has the kernel of A + S at every point of ∂X. By (a) with μ = 0, ϑ_in ≥ 0 in every
fibre inner product. On {r̂ > 1}, N_tf((2L_b)^(·), σ̂) satisfies (H1)–(H2), with S_0 = S(0, ·) in place of S
and N(P⁽⁰⁾) in place of P⁽⁰⁾ ([[sec:i-c-4-1]] (a)), and the coefficient of ρ̂∂_ρ̂ in N(P⁽⁰⁾) is a ([[eq:i-c-1-3]]);
so its A + S is the same endomorphism, and (a) applies to it with ρ̂ for ρ. ∎

The losses of the following model inverses, transforms and integrations are given by their proofs in closed form, and
for one of them a lower bound in closed form. For a weight β and an index set E, n(E, β) denotes the number of pairs
(z, m′) ∈ E with Re z ≤ β. ϑ_in and ϑ_ℋ are the thresholds of [[eq:i-a-1-5]] of the operator concerned, and
s_c > ½ + ϑ_ℋ is the constant regularity order its proof fixes.

**Lemma {#lem:ec-closed-forms}** (Closed forms of the elementary losses.) The proofs of the cited results give them
the following losses, and in (d) a lower bound for the loss.

(a) [[lem:ii-g1-4-1]]: ℓ = max(⌈sup 𝗋 − 𝗋_out⌉, ⌈(s − 1)_+⌉) and ℓ̃ = max(⌈𝗋_out − inf 𝗋⌉, ⌈(−s)_+⌉).

(b) [[cor:ii-g1-4-2]]: if s_c ≥ 0, ℓ = max(⌈(ϑ_in/2 + 3 − β_scf)_+⌉, ⌈(s_c − 1)_+⌉); statement (1) then loses j + ℓ
for ∂^j_σ.

(c) [[prop:ii-g1-4-7]], and so [[lem:iii-i2-4-2]] for L̃_b: if s_c ≥ 0,

    ℓ = max(⌈(ϑ_in/2 + 5/2 + ε/2 − β_scf)_+⌉, ⌈(s_c − 1)_+⌉).                                           {#eq:ec-low-loss}

(d) [[cor:iii-f1-3-4]]: its loss is at least ℓ_tf := max(⌈sup 𝗋 − 𝗋_out⌉, ⌈(s − 1)_+⌉) + max(⌈𝗋_out − inf 𝗋⌉,
⌈(−s)_+⌉), for the orders (s, 𝗋) of its proof at each ϵ it takes, with 𝗋_out = β_sctf − 2 − ϵ/2; and ℓ_tf ≥ 1.

(e) [[thm:iii-g1-3-1]] (2), at a spectral parameter ϰ with Re ϰ < ℓ_I: with δ_ι > 0 the small number δ of Step 5 of
its proof,

    d_ι(ϰ) = 6 + ⌈max(0, Re ϰ − 2 + δ_ι)⌉ + ⌈max(0, Re ϰ − 3/2) + δ_ι⌉ + 2⌈ℓ_I − Re ϰ⌉.                {#eq:ec-iota-loss}

That is 7 + 2⌈ℓ_I − Re ϰ⌉ for Re ϰ < 2 − δ_ι. Let 3 < ℓ_I < 3.5 and δ_ι < 3.5 − ℓ_I. Then d_ι ≤ 12 for
2 − δ_ι ≤ Re ϰ < ℓ_I; over a strip λ₋ ≤ Re ϰ ≤ ℓ_I − ε with λ₋ < 3/2 and ε small,
sup d_ι ≤ max(7 + 2⌈ℓ_I − λ₋⌉, 12); and if moreover λ₋ > ℓ_I − 2, sup d_ι = 12.

(f) [[prop:iii-g3-2-4]] at finite regularity, and so [[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1):
l′ = 2⌈ℓ_I⌉ + 10 + sup d_ι over the strip; l′ = 30 when 3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ_ι < 3.5 − ℓ_I.

(g) [[prop:iii-a-4-2]]: with n_ι := n(E_ι, β_ι), n_K := n(E_K, β_K), n_I := n(E_I, β_I),
B := max(β_K, β_ι + max(0, −min Re π_1E_I)) and ℓ_F := ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉,

    (1):  l = 1 + n_ι + 2 max(n_K + ⌊β_K⌋, n_I + ⌊B⌋),     (2):  l = n_ι + n_K + ℓ_F.  {#eq:ec-fourier-loss}

(h) [[lem:iii-i2-3-1]]: with γ > 0 the number of its proof (β_ι − β_I when this is not an integer, β_ι − β_I − ε′
with the ε′ of that proof when it is) and ε ∈ (0, 1) the loss at which that proof applies [[prop:ii-g1-3-5]] (1),

    ℓ = max(⌈(β_K + ½ + ε)_+⌉, ⌈γ + ½⌉).                                                            {#eq:ec-moment-loss}

*Proof.* (a) is the statement of [[lem:ii-g1-4-1]].

(b) The proof of [[cor:ii-g1-4-2]] takes ℓ := ℓ_a + ℓ̃ with ℓ_a := max(⌈(½(−1 + ϑ_in) + 7/2 − β_scf)_+⌉,
⌈(s_c − 1)_+⌉) and ℓ̃ := ⌈(−s_c)_+⌉. The proof needs only s_c > ½ + ϑ_ℋ, so s_c ≥ 0 may be imposed as a further
choice; then ℓ̃ = 0 and ½(−1 + ϑ_in) + 7/2 = ϑ_in/2 + 3. The loss j + ℓ for ∂^j_σ is statement (1).

(c) The proof of [[prop:ii-g1-4-7]] takes 𝗋_out := β_scf − 2 − ε/2, 𝗋_in := max(𝗋_out, ½(−1 + ϑ_in) + 1) and s = s_c
as in [[cor:ii-g1-4-2]], decay orders with values in [𝗋_out, 𝗋_in], and ℓ := ℓ_a + ℓ̃ from [[lem:ii-g1-4-1]]. So
ℓ_a = max(⌈𝗋_in − 𝗋_out⌉, ⌈(s_c − 1)_+⌉) with 𝗋_in − 𝗋_out = (ϑ_in/2 + 5/2 + ε/2 − β_scf)_+, and ℓ̃ = 0 for s_c ≥ 0.
[[lem:iii-i2-4-2]] is the proof of [[prop:ii-g1-4-7]] for L̃_b.

(d) The proof of [[cor:iii-f1-3-4]] obtains the bound near sctf from [[eq:ii-g1-4-1a]] and [[eq:ii-g1-4-1b]] with the
losses ℓ, ℓ̃ of (a), replaces k by k + ℓ̃ and enlarges ℓ, so that it does not depend on ϵ; so its loss is at least
ℓ + ℓ̃ at each ϵ, which is ℓ_tf. Its orders are
those of [[lem:i-a-7-1]] at σ_* = ±1, with 𝗋 = 𝗋_in at the incoming radial sets, where 𝗋_in > (−1 + ϑ_in)/2 (the
weight α₊ being 0); and 𝗋_out = β_sctf − 2 − ϵ/2 < −½, as β_sctf < 3/2. By [[lem:ec-theta-in]] (b), ϑ_in ≥ 0 in
the fibre inner product in which the orders are chosen; so sup 𝗋 ≥ 𝗋_in > −½ > 𝗋_out, ⌈sup 𝗋 − 𝗋_out⌉ ≥ 1 and
ℓ_tf ≥ 1.

(e) Step 5 of the proof of [[thm:iii-g1-3-1]] extends v^(−2−ϰ)f by 0 to F, which lies in Ḣ^((s−1;k+d),μ)_(b;b) at the
same order k + d, with s := min(½, 2 − Re ϰ) − δ_ι, s − ½ ∉ ℤ, and inverts N_sf(ϰ) at that order. It then applies
[[lem:iii-g1-2-1]], which loses m(s) = 2 + ⌈max(0, −s)⌉ + j, with j the least integer with s + j > ½, that is
j = ⌈½ − s⌉; and then at most ⌈ℓ_I − Re ϰ⌉ + 2 steps, each losing two b-derivatives. So

    d_ι = m(s) + 2(⌈ℓ_I − Re ϰ⌉ + 2) = 6 + ⌈max(0, −s)⌉ + ⌈½ − s⌉ + 2⌈ℓ_I − Re ϰ⌉

suffices. Here −s = max(−½, Re ϰ − 2) + δ_ι, so max(0, −s) = max(0, Re ϰ − 2 + δ_ι) for δ_ι < ½, and
½ − s = max(0, Re ϰ − 3/2) + δ_ι. This is [[eq:ec-iota-loss]]. For Re ϰ < 2 − δ_ι the first ceiling vanishes and the
second is 1 (its argument lies in (0, 1)), which gives 7 + 2⌈ℓ_I − Re ϰ⌉. Let 3 < ℓ_I < 3.5, δ_ι < 3.5 − ℓ_I and
2 ≤ Re ϰ < ℓ_I. If Re ϰ < ℓ_I − 1, then ⌈ℓ_I − Re ϰ⌉ = 2, Re ϰ − 2 + δ_ι < ℓ_I − 3 + δ_ι < 1 and
Re ϰ − 3/2 + δ_ι < ℓ_I − 5/2 + δ_ι < 1, so d_ι = 6 + 1 + 1 + 4 = 12. If ℓ_I − 1 ≤ Re ϰ < ℓ_I, then
⌈ℓ_I − Re ϰ⌉ = 1, Re ϰ − 2 + δ_ι < 3/2 + δ_ι < 2 and Re ϰ − 3/2 + δ_ι < 2, so d_ι ≤ 6 + 2 + 2 + 2 = 12. On the
strip, d_ι is at most 7 + 2⌈ℓ_I − λ₋⌉ where Re ϰ < 2 − δ_ι, as ⌈ℓ_I − Re ϰ⌉ ≤ ⌈ℓ_I − λ₋⌉, and at most 12 where
Re ϰ ≥ 2 − δ_ι (between 2 − δ_ι and 2 the value is 6 + 1 + 1 + 2⌈ℓ_I − Re ϰ⌉ ≤ 12); and the value 12 is attained at
Re ϰ = 2, as ℓ_I − 1 > 2. If λ₋ > ℓ_I − 2, then 7 + 2⌈ℓ_I − λ₋⌉ ≤ 7 + 4 = 11, so sup d_ι = 12.

(f) The proof of [[prop:iii-g3-2-4]] at finite regularity applies [[lem:iii-g3-2-2]], with the loss l = 2⌈ℓ_I⌉ + 10 of
its statement, and then [[thm:iii-g1-3-1]] (2) on the strip, and takes l′ := l + sup d_ι. Here, as in [[ch:s17]], λ ∈ ℂ
is an exponent at ι⁺ with Re λ < ℓ_I (not the wavelength), and z is the variable of the ι⁺-normal operator N_(ι⁺)(z). The
map of [[prop:iii-g3-3-7]] is continuous by [[prop:iii-g3-2-4]] on a strip containing λ, with the loss l′, and the l of
its statement is this l′ (that of [[lem:iii-g3-3-5]]). Its right inverse applies the map u ↦ f of the proof of
[[lem:iii-g3-3-5]], which applies the second-order operator N_(ι⁺) (loss 2), splits f = f₁ + f₂, keeps f₂, and maps f₁ to
res_(z=λ)(t_*^(−z)N_(ι⁺)(z)⁻¹f₁(z)): a map of finite rank into the finite-dimensional space Res_(ι⁺)(L̄, λ) of
[[def:iii-g3-3-6]], whose coefficients are integrals of the inverse of [[thm:iii-g1-3-1]] (2) over a small circle about λ
in the strip, so bounded by the norm of order sup d_ι of f₁. So the right inverse costs at most 2 + sup d_ι < l′
([[lem:iii-j2-1-2]] (b), (c)), and the loss of [[prop:iii-g3-3-7]] is l′. [[cor:iii-g3-3-1]] (1) comes from
[[prop:iii-g3-2-4]] on a strip containing its exponent, with the loss l′; its expansion (2) costs nothing beyond, and its
continuous functionals are counted where a construction that uses them adds its losses. For 3 < ℓ_I < 3.5, ⌈ℓ_I⌉ = 4 and
sup d_ι = 12 by (e), so l′ = 8 + 10 + 12 = 30.

(g) In the proof of [[prop:iii-a-4-2]], the transform bounds (T1) and (T3) lose 1 ([[prop:ii-g1-3-3]] (1)) and ℓ_F
([[prop:ii-g1-3-5]] (1)). Each factor of the products R_ι, R_K, R_I, R_tf and R_zf, applied through the converse of
[[lem:iii-a-1-3]], costs one derivative, each factor σ∂_σ − j applied costs one, and each one-factor integration
step by [[lem:iii-a-1-2]] or [[lem:iii-a-3-3]] costs one; [[lem:iii-a-1-3]] in the direct direction loses nothing
beyond its a priori hypothesis. *Part (1), E_I = ∅.* (T1) on u costs 1. R_ιu has order k + l − n_ι, and (T1) on it
needs l ≥ n_ι + 1. R_Ku has order k + l − n_K, and the bound at the order of the previous step costs n_ι + 1 on it.
The product of the ⌊β_K⌋ factors σ∂_σ − j, j ≤ ⌊β_K − 1⌋, costs ⌊β_K⌋, and the n_K + ⌊β_K⌋ integrations cost one
each. So l₀ = 1 + n_ι + 2(n_K + ⌊β_K⌋). *Part (1), general E_I.* χ_Ku costs l₀. For u vanishing near K, E_K = ∅ and the
K-weight is raised to a non-integer β′_K in (B, ⌊B⌋ + 1), so ⌊β′_K⌋ = ⌊B⌋; R_Iu costs n_I, the case E_I = ∅ at the
weight β′_K costs 1 + n_ι + 2⌊B⌋, and the integrations from scf cost n_I. The larger of the two gives
[[eq:ec-fourier-loss]] (1). *Part (2).* With E_K = ∅, (T3) costs ℓ_F, R_tf costs n_ι, and [[lem:iii-a-1-3]] at ι
costs nothing more; for general E_K, R_zf costs n_K and [[lem:iii-a-1-3]] at K nothing more. The harmless terms that
the proof sets aside cost nothing more. The factors σ∂_σ + χ(ρ)ρ∂_ρ − (z − 1) of R_tf commute with one another and
with 1_(±σ>0), and the commutator of each with multiplication by a function ψ(σ) is multiplication by σ∂_σψ; so, by
induction over the factors, R_tf(χ(σ)w) − χ(σ)R_tf w is a sum of terms ((σ∂_σ)^mχ)(σ)Qw, m ≥ 1, with Q a product of
at most n_ι − 1 of the factors, and likewise for R_zf with at most n_K − 1. As χ = 1 near [−½, ½] and supp χ is a
compact subset of (−1, 1), each (σ∂_σ)^mχ, m ≥ 1, is supported in a compact subset of {½ < |σ| < 1}. So such a term,
with w = v^± on each side, vanishes near tf and zf: it lies in the space of (T3) at the weights
(β_scf, β_ι − 1, ((0, 0), β_K − 1)), with σ-Taylor coefficients 0, at an order at least one more than that of the
main term R_tf v^±, resp. R_zf v^±, and it is its own product with a cut-off in C^∞_c((−1, 1)) equal to 1 near
[−½, ½] and near supp χ, for which (T3) holds as for χ ([[prop:ii-g1-3-5]] (1)). (T3) at these weights gives its
inverse transform the weights (min(β_scf, β_ι) − ε, β_ι, β_K), at least those of [[eq:iii-a-4-5]] and of the step
before it, with the loss ℓ_F; so it reaches the order of the main term, which loses ℓ_F, resp. n_ι + ℓ_F, after R_tf,
resp. R_zf. This gives [[eq:ec-fourier-loss]] (2).

(h) In the proof of [[lem:iii-i2-3-1]], the piece f_2 comes from (1 − χ_scf)ℱf, which vanishes near scf, by
[[prop:ii-g1-3-5]] (1) with the scf-weight taken at least β_ι + 1 and the tf- and K-weights β_ι + 1 and β_K + 1 of
[[eq:iii-i2-3-3]]; its loss is ⌈(max(β_ι + 1 − β_scf, β_K + 1) + ε − ½)_+⌉ = ⌈(β_K + ½ + ε)_+⌉, as
β_ι + 1 − β_scf ≤ 0 < β_K + 1. The piece f_1 comes from ℱf_1 = ρ^(β_I)|σ|^γ w by [[prop:ii-g1-2-8]] (2) at
β = γ + 1, which takes X^(j+ℓ_+(β),γ) to H^(j,β)_b; with the b-vector fields of X̄ taking the remaining
k − j derivatives, this costs ℓ_+(γ + 1) = ⌈γ + ½⌉, as γ > 0. The same proof needs ℓ ≥ 1 for the bound by C|σ|^γ
of |ℱf_1(σ)|, which ⌈γ + ½⌉ ≥ 1 gives. Every other step, the integrations of [[lem:iii-i2-2-1]] and
[[lem:iii-a-1-2]] and the multiplication by χ, keeps the order k. This is [[eq:ec-moment-loss]]. ∎

**Remark {#rem:ec-other-losses}** (The other elementary losses.) The remaining elementary losses of
[[lem:iii-j2-2-1]] are fixed in its statement:

- 0 for finite-dimensional maps (its (c)), for the integrations along faces of [[lem:iii-a-1-2]], [[lem:iii-a-3-2]]
  and [[lem:iii-i2-2-1]] (its (d)), for [[cor:iii-h-4-2]] on |σ| < c_k (its (e)) and for [[lem:iii-i2-4-3]] (its (g));
- 1 for [[prop:ii-g1-3-3]] (1) and [[prop:iii-h-3-2]];
- where they are applied outside [[prop:iii-a-4-2]], the losses printed in their statements:
  ⌈(½ − min(β_K, β_ι − β_I))_+⌉ for [[prop:ii-g1-3-3]] (2), ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉ for
  [[prop:ii-g1-3-5]] (1) and ⌈(3/2 − δ_∞)_+⌉ + ⌈(β′ − ½)_+⌉ for [[prop:ii-g1-3-5]] (2), δ_∞ and β′ being the
  high-frequency weight δ and the number β′ of its statement, each at the weights of the application;
- 2 for the second-order operators L_b at a parameter b, a finite-dimensional component of p⃗, and L̃_b at the
  background 0;
- max(2, d_BG) for the families of its (b) applied to a solution, among them L^(g,g_0) − L_b, R_q and the remainder
  L̃ of [[lem:iii-i1-1-1]], whose coefficients depend on h; here d_BG is the order in the background of their bound
  ‖Au‖_k ≤ C_k(‖u‖_(k+2) + ‖β‖_(k+d_BG)‖u‖_(d_BG)), fixed by [[lem:ii-g-4-1]], [[lem:ii-a-9-5]] and
  [[cor:ii-a-9-7]], and this bound is tame with loss max(2, d_BG) ([[def:iii-j2-1-1]]), as ‖u‖_(k+2) ≤ ‖u‖_(k+d_BG)
  when d_BG ≥ 2 and ‖β‖_(k+d_BG)‖u‖_(d_BG) ≤ ‖β‖_(k+2)‖u‖_2 when d_BG < 2, the norms being non-decreasing in the
  order;
- ℓ + 1 for [[cor:ii-g1-4-5]] at every order, where ℓ = 2ℓ_3 + ℓ_4 + ℓ_5 is assembled from the losses of
  [[prop:ii-g1-3-5]] (2), [[prop:ii-g1-4-4]] and [[prop:ii-g1-3-3]] (2), each a closed form in the weights, and at most
  ℓ + 1 plus the losses of its (e) for [[lem:iii-i2-4-1]] (its (f));
- d_ι + 2 for [[cor:iii-g2-4-3]].

[[lem:ec-closed-forms]] (h) gives the loss of [[lem:iii-i2-3-1]]. The forward solution operators of [[lem:iii-j2-2-1]]
(a) lose the d of [[thm:iii-i-5-3]], which [[sec:fwd]] evaluates: [[thm:fwd-loss]] shows that d = 20,180 may be taken,
and [[cor:fwd-near-b0]] gives the same value at every base point with black hole parameter in ℬ̄_*. The order of choices
behind ℓ + 1 is: d_acc and d_NM first, then N_NM, then the trapping data at the orders k ≤ N_NM ([[cor:iii-h2-1-2]]); the
constants of the smallness conditions are used at those orders only, the tame estimates themselves at every order. An
explicit value of d_acc needs, besides these closed forms, the order d_BG, numbers for the weights at the parameters in
question, the counts n(E, β) of the index sets and the numbers of steps of the iterations of the inventory of
[[sec:iii-j2-3]]; two of these iterations bound d_acc from below ([[lem:ec-round-loss]], [[prop:ec-rounds]],
[[thm:loss-d]] (ii)), and at the computational point [[thm:uc-integer]] bounds d_acc, d_NM and N_NM from above.

### The loss of the forward solution operators, evaluated {#sec:fwd}

[[thm:iii-i-5-3]] asserts a loss d ∈ ℕ. Its proof takes the d of [[thm:ii-f1-1-1]] in the relaxed form of
[[rem:ii-f1-7-1]] with d_ℵ = 1 and raises it by 5, so that

    d = D_0 + D_1 + d′ + d″ + 1 + 5,                                                                   {#eq:fwd-split}

with D_0, D_1, d′, d″ of [[eq:ii-f1-3-2]]–[[eq:ii-f1-3-3]] taken for the orders of [[rem:ii-f1-7-1]]. This section
evaluates each term. The orders d′, d″ and the tame loss D_1 follow from closed forms already in the edition; D_0, the
number of coefficient derivatives, rests on the calculus of finite regularity of [[sec:ii-a1-2]], whose indices are
made explicit in [[prop:fwd-calculus]]. [[cor:fwd-near-b0]] carries the value to [[cor:iii-h2-5-1]], at every black
hole parameter near b₀.

**Theorem {#thm:fwd-loss}** (The forward loss.) In [[thm:iii-i-5-3]] one may take d = 20,180, for every
β_+ ∈ (½, 3/2) and β_I ∈ (β_+, 3/2). More precisely d′ = 10, d″ = 11, D_1 = 49 and D_0 ≤ 20,104 in [[eq:fwd-split]].

The proof occupies the rest of the section and is completed after [[lem:fwd-increments]]. It uses the following
statements of other sections with explicit values: [[prop:ii-a1-2-4]] with M + 2 = 200T + 100 in the form of
[[prop:fwd-calculus]]; [[lem:ii-a-8-5]] (a), (b) with d_0 = 200T + 100 under the conditions there; the a priori order
N′ = 13 of [[ch:s06]]; the choice s_in = 11, s_out = −10 in [[sec:ii-c-5-2]]; and the uniqueness steps of the proofs
of [[prop:ii-e-4-3]] and [[prop:ii-e-5-6]] (a) taken at s′ = inf 𝗌 − 1 ([[lem:fwd-box]], (Sb)).

#### The orders {#sec:fwd-orders}

**Lemma {#lem:fwd-orders}** (The orders.) For P_0 = 2L_(b₀), the weights α_+ = β_+ − 5/2, α_I = β_I − 2, ℵ = 2, δ = 0
of the proof of [[thm:iii-i-5-3]] and the margin m_0 + 2d̄_ℵ = 7 of [[rem:ii-f1-7-1]], the construction of
[[sec:ii-c-5-2]] can be carried out with s_in = 11 and s_out = −10, for every β_+ ∈ (½, 3/2). Hence inf 𝗌 = −10,
sup 𝗌 = 11, 𝗌_0 = 𝗌 − 3 has inf 𝗌_0 = −13, s_u = inf 𝗌 − 2 = −12, and

    d′ = max(0, ⌈−inf 𝗌⌉) = 10,        d″ = s_in = 11.                                                {#eq:fwd-dprime}

*Proof.* The construction allows every s_in ∈ ℕ with s_in ≥ 4 + d̄_ℵ = 5 and

    s_in > max(½ + ϑ_ℋ + η, ½(−1 + ϑ^(3b)_in) + α_K + η − α_+) + 1,
    s_out < min(s_in, ½(−1 + ϑ_out) + α_K − η − α_+) − 1,

with η = 7 and α_K = −2, each threshold in a fibre inner product chosen for its radial set ([[sec:ii-c-5-2]],
[[rem:ii-f1-7-1]]). We bound the three thresholds.

*The horizon.* By [[eq:iii-f2-1-1]] and the paragraph after it, ϑ_L = max(0, 2 − 2x) < 2 with x = a_v γ_C r_h > 0, and
for δ = ¼ there is a fixed fibre inner product with ϑ_ℋ < ϑ_L + ¼ < 9/4 at b₀.

*The incoming radial set over ∂K⁺.* By [[lem:ii-c-2-6]], ϑ^(3b)_in = ϑ_in, the threshold of [[eq:i-a-1-5]] at R_in.
By [[lem:ec-theta-in]] (a), p_in − (S + S^(∗h)) = −2 Re_h(A + S) at ∂X for every fibre inner product h, so that
ϑ_in computed in h is −2 inf_(∂X) λ_min(Re_h(A + S)) ([[eq:i-a-1-5]]). We show that every eigenvalue of A + S on ∂X
is real and ≥ 0. A + S is homogeneous of degree 0 ([[lem:ec-theta-in]] (b)), so it suffices to take it at a point x
with |x| > 0, where ρ(A + S) = −Ē^C ι_(ḡ⁻¹ζ) Ḡ + (ζ ⊗_s ·) Ē^Υ Ḡ by [[eq:ec-theta-in-l]]. Use the frame
(dx̄⁰, dx̄¹, |x|e^a) of the proof of [[lem:iii-c-4-2]], in which ζ = dt̄ + d|x| = dt_* + 2d|x| = dx̄⁰ and dt_* = dx̄¹,
and let Π be the linear map of the tensors at x that exchanges the frame indices 0 and 1. The components of ḡ and of
ḡ⁻¹ in this frame do not change under the exchange (ḡ⁻¹(dx̄⁰, dx̄¹) = −2, ḡ⁻¹(dx̄⁰, dx̄⁰) = ḡ⁻¹(dx̄¹, dx̄¹) = 0, and no
mixed null-tangential components). So Π commutes with raising and lowering indices, with contractions and traces, with
⊗_s and with Ḡ; and Π dx̄⁰ = dx̄¹, Π dt̄ = dt̄ and ΠY = Y for Y := ḡ⁻¹dt̄, while Π maps
ĉ = ½(1 − v_C)dx̄⁰ + ½(1 + v_C)dx̄¹ to ĉ with v_C replaced by −v_C. In that proof Ē^C and Ē^ΥḠ are written through
ĉ, ḡ, dt̄ and Y alone: Ē^Cω = γ_Cρ(2ĉ ⊗_s ω − ⅔(1 − e_C)ḡ⟨ĉ, ω⟩) and Ē^ΥḠh = −γ_Υρ(2ι_Y h − e_Υ(tr h) dt̄). Hence
Π ρ(A + S) Π⁻¹ = −Ē^C_− ι_(ḡ⁻¹dt_*) Ḡ + (dt_* ⊗_s ·) Ē^Υ Ḡ, with Ē^C_− the operator Ē^C with v_C replaced by −v_C;
this is ρS̄ of [[eq:iii-f-2-2]] with v_C replaced by −v_C. The proof of [[lem:iii-c-4-2]] computes the matrix of that
expression in the frame for any real constant in place of v_C (it uses v_C only through a = ½(1 − v_C) and
b = ½(1 + v_C)). So Π(A + S)Π⁻¹ is lower triangular, with the diagonal [[eq:iii-c-4-3]] with v_C replaced by −v_C,

    2(1 + v_C)γ_C,  (1 + v_C)γ_C,  (1 − e_C)(1 + v_C)γ_C,  (1 − e_Υ)γ_Υ,  γ_Υ,  0,  2γ_Υ,

each entry acting on its slot as a multiple of the identity. These are the eigenvalues of A + S, with the ranks of
the slots as multiplicities. As v_C ∈ (0, 1) ([[def:iii-b-6-1]]), 0 < e_C < 1, γ_C > 0, 0 < e_Υ < 1 and γ_Υ > 0
([[sec:iii-c-1]], [[eq:iii-c-1-1]]), all are ≥ 0, and 0 is one of them: inf_(∂X) min Re spec(A + S) = 0.
[[lem:ii-c-2-5]], applied to a smooth extension of A + S to X̄ in place of S (only its values on ∂X enter), gives for
every ϵ > 0 a fibre inner product h with λ_min(Re_h(A + S)) ≥ −ϵ on ∂X. With ϵ = 1/8, ϑ_in ≤ ¼.

*The outgoing radial set.* By [[lem:ii-c-2-6]] with the inner product of [[lem:ii-c-2-5]] at ϵ = 1/8,
ϑ_out ≥ 2S̄ − ¼ = −¼, as S̄ = 0 for 2L_(b₀) ([[eq:iii-c-4-3]]).

*The values.* With α_+ ∈ (−2, −1), the first condition reads s_in > max(½ + ϑ_ℋ + 7, −½ + ½ϑ_in + 5 − α_+) + 1, and
½ + 9/4 + 7 + 1 = 43/4 while −½ + 1/8 + 5 + 2 + 1 = 61/8 < 43/4. So s_in = 11 serves for every β_+. The second reads
s_out < min(11, ½(−1 − ¼) − 9 − α_+) − 1 = −85/8 − α_+, whose right side exceeds −77/8 for every α_+ < −1. So
s_out = −10 serves. As 𝗌 = s_in − (s_in − s_out)χ with 0 ≤ χ ≤ 1 taking both values 0 and 1 ([[sec:ii-c-5-2]]),
inf 𝗌 = −10 and sup 𝗌 = 11, and [[eq:fwd-dprime]] follows from [[eq:ii-f1-3-3]]. ∎

The error order used below is N := 13, the least integer with −N ≤ inf 𝗌_0, which is what the global estimates need of
their a priori term ‖χu‖_((−N;k)) ≤ ‖u‖_((𝗌_0;k)) ([[sec:ii-d1-7]]).

#### The tame losses {#sec:fwd-tame}

For variable orders 𝗍, 𝗍_0 write

    d̃(𝗍, 𝗍_0) := s̄ + 2 max(s̲, s̲_0) + 6,     s̄ := max(0, ⌈sup 𝗍⌉),  s̲ := max(0, ⌈−inf 𝗍⌉),
    s̲_0 := max(0, ⌈−inf 𝗍_0⌉),                                                                          {#eq:fwd-dtilde}

the d̃ of [[prop:ii-a-9-6]] at (𝗍, 𝗍_0) (there d_1 = s̄ + max(s̲, s̲_0) + 3 and d̃ = d_1 + max(s̲, s̲_0) + 3).

**Lemma {#lem:fwd-tame}** (The tame loss.) With the orders of [[lem:fwd-orders]] and N = 13, D_1 = 49 in
[[eq:ii-f1-3-2]].

*Proof.* D_1 = max(d^E, d^S, d̃), and every one of these is a closed form in [[eq:fwd-dtilde]] fixed by its proof.

(i) d̃ of [[lem:ii-f1-2-8]] for 𝗍 = 𝗌 is that of [[prop:ii-a-9-6]] at (𝗌 − 2, 𝗌 − 2) ([[cor:ii-a-9-7]] with m = 2):
s̄ = 9, s̲ = s̲_0 = 12, so d̃ = 9 + 24 + 6 = 39.

(ii) d^S. [[prop:ii-e-4-4]] at a slab order 𝗍 has d = d̃ + 3 with d̃ the larger of those of [[lem:ii-e-4-1]] (b) at
𝗍 + 1 and 𝗍 − 1, which is [[prop:ii-a-9-6]] at (𝗍 ± 1, 𝗍 ± 1). At 𝗍 = 𝗌: d̃(𝗌 + 1, 𝗌 + 1) = 12 + 18 + 6 = 36 and
d̃(𝗌 − 1, 𝗌 − 1) = 10 + 22 + 6 = 38, so d = 41. At 𝗍 = 𝗌 + 2 (the slab order 𝗌 + d̄_ℵ + 1 of [[rem:ii-f1-7-1]]):
d̃(𝗌 + 3, 𝗌 + 3) = 14 + 14 + 6 = 34 and d̃(𝗌 + 1, 𝗌 + 1) = 36, so d = 39. [[prop:ii-e-4-3]] and [[prop:ii-e-3-4]] carry
no tame loss. So d^S = 41.

(iii) d^E, the d of [[thm:ii-e-6-1]] at (𝗌_0, 𝗌) = (𝗌 − 3, 𝗌), is the largest of those of its pieces (A)–(C).
(A) [[prop:ii-e-4-4]] at 𝗌: 41. (C) [[prop:ii-e-5-6]] (b): d = d̃ + 3 with d̃ as in [[prop:ii-e-4-4]] at 𝗌: at most 41.
(B) [[thm:ii-d1-1-1]]: d is the largest of the d of [[lem:ii-d1-2-4]] for Steps 2–6 of [[sec:ii-d1-7]] and of
[[prop:ii-a-9-8]]–[[prop:ii-a-9-9]] at the orders 𝗌 + 1 and 𝗌, with error order −N.
[[lem:ii-d1-2-4]] has d = d̃ + 3 with d̃ the larger of [[prop:ii-a-9-6]] at (𝗍 + 1 + 𝔩, 𝗍_0) and (𝗍_0 − 2, 𝗍_0 − 2),
𝗍, 𝗍_0 the constant values of the orders at the set, 𝔩 ≤ 1. At the horizon, at ∂R_(ℐ⁺,in,+) and at ∂R_(∂K⁺,in) the
orders are (𝗌 + 1, 𝗌_0) = (12, 8) and 𝔩 = 0: d̃(13, 8) = 19, d̃(6, 6) = 12, d = 22. At the trapped set (11, 8),
𝔩 = 1: d̃(13, 8) = 19, d = 22. At ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out) the orders are (𝗌, 𝗌_0) = (−10, −13) and 𝔩 = 0:
d̃(−9, −13) = 0 + 26 + 6 = 32, d̃(−15, −15) = 36, d = 39. (𝔩 = 0 at the radial sets and 𝔩 = 1 at the trapped set,
[[sec:ii-d1-2]].)
[[prop:ii-a-9-9]] at the order 𝗍 has d = d̃ + 2 with [[prop:ii-a-9-6]] at (𝗍 − m + 1, −N − m), m = 2: at 𝗍 = 𝗌 + 1,
(𝗌, −15) gives s̄ = 11, max(s̲, s̲_0) = 15, d̃ = 47, d = 49; at 𝗍 = 𝗌, d̃ = 46, d = 48. [[prop:ii-a-9-8]] at
𝗍 ≤ 𝗌 + 1 has d = d̃ + 1 with (𝗍 − m, −N − m): d̃(𝗌 − 1, −15) = 46, d = 47. So d^E = 49.

Hence D_1 = max(49, 41, 39) = 49. ∎

#### A quantitative calculus of finite regularity {#sec:fwd-calculus}

The proofs of [[prop:ii-a1-2-4]] and [[lem:ii-a-8-5]] take their indices from the closed graph theorem, which gives no
value; the values stated there are proved here. We prove them again, every derivative counted. Throughout, n = 5, T ∈ ℕ
and 𝔐(T) := 200T + 100; Op denotes the left quantization on ℝⁿ, Op(p)u(x) = (2π)^(−n) ∫ e^(ix·ξ) p(x, ξ) û(ξ) dξ;
Q_4 := [−2, 2]ⁿ; and for an integer x, 𝔢(x) denotes the least even integer above x (so 𝔢(x) = x + 1 for odd x and x + 2
for even x). For an order function 𝗆 (smooth in (x, ξ), with |∂_x^β ∂_ξ^γ 𝗆| ≤ C_(βγ)⟨ξ⟩^(−|γ|), as the variable orders
of [[sec:ii-a1-1-1]] are in the charts of ρℬ) and K ∈ ℕ_0 put

    |p|^𝗆_K := max_(|β|+|γ|≤K) sup ⟨ξ⟩^(−𝗆(x,ξ)−ϰ(|β|+|γ|)+|γ|) |∂_x^β ∂_ξ^γ p(x, ξ)|,          {#eq:fwd-seminorm}

with ϰ := 1/(32𝔐(T)). By Leibniz's rule |pq|^(𝗆_1+𝗆_2)_K ≤ C|p|^(𝗆_1)_K |q|^(𝗆_2)_K; and the seminorm of order 𝗆
of ⟨ξ⟩^(𝗆(x,ξ)) is at most C_K for every K, its derivatives carrying factors log⟨ξ⟩ ≤ C⟨ξ⟩^ϰ. A symbol of
[[def:ii-a1-1-3]] of any
index ν, written in a chart of ρℬ, satisfies |a|^𝗆_M ≤ C‖a‖_((M);ν,𝗆): by [[lem:ii-a1-2-2]], ∂_ξ is e^(−τ) times
bounded combinations of ∂_ω, ∂_τ, and ⟨log ρ_∞⟩^(νj) ≤ C⟨ξ⟩^(ϰj). The constants depend on ϰ, ν and K, never on the
symbol beyond the seminorm; in particular the index ν enters no count. Every product estimated below is a product of at
most eight symbols (six factors of an expression and two auxiliary symbols λ, λ′), each differentiated at most 𝔐(T)
times (the counts of [[prop:fwd-calculus]]), so that the total loss ϰ·8𝔐(T) in any exponent is at most ¼. Every
statement below holds with the same counts for every smaller ϰ, which is how "order 𝗋 + δ for every δ > 0" is obtained.
A symbol "has order 𝗆" with "values in [−A, A]" when |𝗆| ≤ A; constant orders are included.

*The charts.* Let (U_α, φ_α) be the charts of ρℬ, onto (−2, 2)ⁿ, of finite multiplicity, with transition maps
φ_α ∘ φ_β⁻¹ bounded in C^j uniformly in (α, β) for every j ((S1), (S13)), and χ_α the partition of unity of (S4). As
all scalings of ρℬ equal 1, (S4) gives

    Op(a) = Σ_α O_α(a),     O_α(a) := φ_α^* Op_ψ(a_α) (φ_α)_*,     a_α := (φ_α)_*(χ_α a),             {#eq:fwd-chart-op}

where Op_ψ(b) has the kernel (2π)^(−n) ∫ e^(i(x−y)·ξ) ψ(x − y) b(x, ξ) dξ, ψ ∈ C_c^∞((−¼, ¼)ⁿ) equals 1 near 0, and
a_α vanishes for x ∉ (−5/4, 5/4)ⁿ. The adjoint is that of L²(|dt dx|), which in the chart α is the adjoint of
L²(μ_α dx), μ_α a positive function whose quotients μ_α(x)/μ_α(y) are bounded in C^j on (−2, 2)ⁿ × (−2, 2)ⁿ uniformly in
α ((S2), (S11)). For an order function 𝗆 on the bundle, 𝗆_α denotes its expression in the chart α, extended to
ℝⁿ × ℝⁿ with values in the same interval and with the same bounds; the variable-order Sobolev space H^(𝗆_α)(ℝⁿ) is
normed by ‖Op(⟨ξ⟩^(𝗆_α))w‖ + ‖w‖_(H^(−N_0)) for a fixed N_0 ≥ sup |𝗆_α|, different such N_0 giving equivalent norms
((S8); elliptic regularity of the smooth calculus).

**Lemma {#lem:fwd-crude}** (Boundedness from x-derivatives.) Let p vanish for x ∉ Q_4, let μ, s ∈ ℝ, and suppose that
the bound |∂_(x_l)^j p(x, ξ)| ≤ A⟨ξ⟩^μ for l = 1, …, n and j ≤ N, where N is an integer with N > n + |s − μ|. Then
‖Op(p)u‖_(H^(s−μ)) ≤ C A ‖u‖_(H^s), C depending on n, s − μ and N.

*Proof.* Let θ ∈ C_c^∞((−3, 3)ⁿ) equal 1 on Q_4 and e_k(x) := e^(iπk·x/3), k ∈ ℤⁿ. On [−3, 3]ⁿ,
p(x, ξ) = Σ_k e_k(x) p̂_k(ξ) with p̂_k(ξ) := 6^(−n) ∫ e_(−k)(x) p(x, ξ) dx, and integrating by parts N times in the
coordinate x_l with |k_l| = max_i |k_i| ≥ |k|/√n gives |p̂_k(ξ)| ≤ C⟨k⟩^(−N) A⟨ξ⟩^μ. So the series converges absolutely
(N > n) and Op(p)u = θ Σ_k e_k p̂_k(D)u, both sides vanishing off Q_4 by the choice of θ. The Fourier multiplier p̂_k(D)
maps H^s to H^(s−μ) with norm sup_ξ |p̂_k(ξ)|⟨ξ⟩^(−μ), and multiplication by θe_k has norm at most C⟨k⟩^(|s−μ|) on
H^(s−μ) (Peetre's inequality, as in [[ch:s03]]). The sum Σ_k ⟨k⟩^(|s−μ|−N) is finite as N − |s − μ| > n. ∎

**Lemma {#lem:fwd-l2}** (Boundedness on L² without loss.) Suppose that, for l = 1, …, n and j ≤ 12,
the pure derivatives satisfy |∂_(x_l)^j p| ≤ A⟨ξ⟩^(ϰj) and |∂_(ξ_l)^j p| ≤ A⟨ξ⟩^(−(1−ϰ)j). Then
‖Op(p)‖_(L²→L²) ≤ CA. In particular ‖Op(p)‖ ≤ C|p|^0_12.

*Proof.* Let ψ_0 + Σ_(j≥1) ψ_j = 1 be a dyadic partition, ψ_j supported in {2^(j−1) ≤ |ξ| ≤ 2^(j+1)} for j ≥ 1,
with derivatives bounded by C2^(−j|γ|). For the shell j put a_j := 2^(−ϰj) and b_j := 2^((1−ϰ)j), so a_jb_j ≥ 1.
With θ, Θ ∈ C_c^∞((−1, 1)ⁿ) such that Σ_m θ(· − m) = Σ_i Θ(· − i) = 1, let I = (j, m, i), p_I(x, ξ) :=
θ(x/a_j − m)Θ(ξ/b_j − i)ψ_j(ξ)p(x, ξ) and T_I := Op(p_I). On supp ψ_j, ⟨ξ⟩ ≤ 2^(j+2), so the hypotheses give
the bounds CAa_j^(−k) for ∂_(x_l)^k p_I and CAb_j^(−k) for ∂_(ξ_l)^k p_I, k ≤ 12. Op(p)u = Σ_I T_I u for u ∈ 𝒮, the sum
converging pointwise, so by the lemma of Cotlar and Stein it suffices to show
sup_I Σ_(I′) ‖T_I^*T_(I′)‖^(1/2) ≤ CA and sup_I Σ_(I′) ‖T_I T_(I′)^*‖^(1/2) ≤ CA.

*T_I T_(I′)^*.* The Fourier transform of T_(I′)^*v is supported in the ξ-support of p_(I′), and T_I w depends only on
ŵ there; so T_I T_(I′)^* = 0 unless the ξ-supports meet, which forces |j − j′| ≤ 1, comparable boxes and boundedly many
i′ for given I. Its kernel is K(x, y) = (2π)^(−n) ∫ e^(i(x−y)·ξ) p_I(x, ξ) \overline{p_(I′)(y, ξ)} dξ. Integrating by
parts twelve times in ξ_l, (x_l − y_l)^12 K is bounded by CA²b^(n−12), b := b_j; with 1 + Σ_l (b|x_l − y_l|)^12 ≥
c(1 + b|x − y|)^12 this gives |K| ≤ CA²bⁿ(1 + b|x − y|)^(−12), K vanishing unless x and y lie in the x-boxes of I and
I′ (side 2a, a := a_j). Schur's test gives ‖T_I T_(I′)^*‖ ≤ CA² when the boxes are within distance 3a, and
≤ CA²(ab)^(n−12)⟨m − m′⟩^(−12) ≤ CA²⟨m − m′⟩^(−12) otherwise. Since 12/2 > n, the sum over I′ is at most CA.

*T_I^*T_(I′).* On the Fourier side its kernel is L(ξ, η) = ∫ e^(ix·(η−ξ)) \overline{p_I(x, ξ)} p_(I′)(x, η) dx, which
vanishes unless the x-boxes meet. Integrating by parts twelve times in x_l, with a̲ := min(a_j, a_(j′)), we obtain the
bound CA²a̲ⁿ(1 + a̲|ξ − η|)^(−12) for |L|. If |j − j′| ≤ 2 the scales are comparable and Schur's test over the
ξ-boxes gives, as before, a bound CA²⟨i − i′⟩^(−12), summable to CA. If |j − j′| ≥ 3, |ξ − η| ≥
2^(J−2) with J := max(j, j′), so |L| ≤ CA²2^(−ϰJn)2^(−12(1−ϰ)J) and ‖T_I^*T_(I′)‖ ≤ CA²2^(−ϰJn)2^(−(1−ϰ)J(12−n)); the
number of I′ in the shell j′ meeting the x-box of I is at most C2^(2ϰJn). The contribution of the shell j′ is therefore
at most CA2^(J(2ϰn − (1−ϰ)(12−n)/2)) ≤ CA2^(−J), as 2ϰn ≤ 5/4 and (1 − ϰ)(12 − n)/2 ≥ 49/16. Summed over j′ this is
at most CA. ∎

**Lemma {#lem:fwd-composition}** (Composition with remainder.) Let p, q be symbols whose seminorms
[[eq:fwd-seminorm]] at the orders 𝗆_1, 𝗆_2 and the regularities K_1, K_2 are finite, μ_i := sup 𝗆_i, J ≥ 1 and B ≥ 0.
Then Op(p)Op(q) = Op(p ♯_J q) + Op(r_J) with

    p ♯_J q := Σ_(|α|<J) (α!)⁻¹ ∂_ξ^α p · D_x^α q,
    |∂_x^β r_J(x, ξ)| ≤ C|p|^(𝗆_1)_(K_1)|q|^(𝗆_2)_(K_2) ⟨ξ⟩^(μ_1+μ_2−J+½),   |β| ≤ B,         {#eq:fwd-remainder}

provided K_1 ≥ J + B + 6 and K_2 ≥ J + B + 2L′, where 2L′ := 𝔢(n + 1 + X) for an integer X ≥ |μ_1 − J|; if q
vanishes for x ∉ Q_4 the condition on K_1 is K_1 ≥ J + B. The term of p ♯_J q of index α has the pointwise order
𝗆_1 + 𝗆_2 − |α|, and its derivatives of order K are bounded by C|p|^(𝗆_1)_(K+|α|)|q|^(𝗆_2)_(K+|α|) with the loss
ϰ(K + 2|α|).

*Proof.* Op(p)Op(q) = Op(c) with c(x, ξ) = (2π)^(−n) ∫∫ e^(−iy·η) p(x, ξ + η) q(x + y, ξ) dy dη. Taylor's formula in η
to order J and η^α e^(−iy·η) = (i∂_y)^α e^(−iy·η), integrated by parts onto q, give the terms of p ♯_J q and

    r_J = Σ_(|α|=J) (J/α!) ∫_0^1 (1 − θ)^(J−1) r_(α,θ) dθ,
    r_(α,θ)(x, ξ) := (2π)^(−n) ∫∫ e^(−iy·η) ∂_ξ^α p(x, ξ + θη) D_x^α q(x + y, ξ) dy dη.

Apply ∂_x^β. Insert ⟨η⟩^(−2L′)(1 − Δ_y)^(L′) and ⟨y⟩^(−6)(1 − Δ_η)^3 (the latter only when q is not compactly supported
in x) acting on e^(−iy·η), and integrate by parts. The η-derivatives fall on ∂_ξ^α ∂_x^(β_1) p, at most J + 6 + B
derivatives, each bounded by C|p|⟨ξ + θη⟩^(μ_1 − J + ¼); the y-derivatives fall on ∂_x^(α+β_2) q, at most J + B + 2L′
derivatives, each bounded by C|q|⟨ξ⟩^(μ_2 + ¼). Peetre's inequality ⟨ξ + θη⟩^t ≤ 2^(|t|/2)⟨ξ⟩^t⟨η⟩^(|t|) and
2L′ > n + |μ_1 − J + ¼| make the η-integral at most C⟨ξ⟩^(μ_1−J+¼), and the y-integral is finite (over a bounded set
when q vanishes for x ∉ Q_4, and by ⟨y⟩^(−6), 6 > n, otherwise). This is [[eq:fwd-remainder]]. The statement on the
terms is Leibniz's rule. ∎

**Lemma {#lem:fwd-reduction}** (Reduction of an amplitude.) Let c(x, y, η) vanish unless x ∈ Q_4 and |x − y| ≤ 1, let
μ be a constant, and suppose |∂_x^β ∂_y^(β′) ∂_η^γ c| ≤ A⟨η⟩^(μ−|γ|+ϰ(|β|+|β′|+|γ|)) for |β| + |β′| + |γ| ≤ K_c.
Let R_c be the operator with the kernel (2π)^(−n) ∫ e^(i(x−y)·η) c(x, y, η) dη. For J ≥ 0 and B ≥ 0,

    R_c = Op(σ_J) + Op(ρ_J),     σ_J(x, η) := Σ_(|γ|<J) (γ!)⁻¹ ∂_η^γ D_y^γ c(x, y, η)|_(y=x),
    |∂_x^β ρ_J(x, η)| ≤ CA⟨η⟩^(μ−J+½),   |β| ≤ B,                                                 {#eq:fwd-reduction}

provided K_c ≥ 2J + B + 2L′ with 2L′ := 𝔢(n + 1 + X), X ≥ |μ − J| an integer. The term of σ_J of index γ is a sum of
products of derivatives of c of total order 2|γ|, evaluated at y = x; its derivatives of order K involve derivatives of
c of total order at most K + 2|γ|. If c vanishes near {x = y}, then σ_J = 0.

*Proof.* R_c u(x) = ∫ e^(ix·η) σ(x, η) û(η) dη with σ(x, η) = (2π)^(−n) ∫∫ e^(−iz·ζ) c(x, x + z, η + ζ) dz dζ, the
z-integral being over |z| ≤ 1. Taylor's formula in ζ to order J and ζ^γ e^(−iz·ζ) = (i∂_z)^γ e^(−iz·ζ), integrated by
parts in z, give σ = σ_J + ρ_J with

    ρ_J = Σ_(|γ|=J) (J/γ!) ∫_0^1 (1 − θ)^(J−1) (2π)^(−n) ∫∫ e^(−iz·ζ) ∂_η^γ D_z^γ [c(x, x + z, η + θζ)] dz dζ dθ.

Apply ∂_x^β, which falls on both arguments x and x + z, and insert ⟨ζ⟩^(−2L′)(1 − Δ_z)^(L′) acting on e^(−iz·ζ). In
all, c is differentiated J times in η, J + 2L′ times in z (that is, in its second argument) and |β| ≤ B times in its
first two arguments: at most 2J + B + 2L′ derivatives, each term bounded by CA⟨η + θζ⟩^(μ−J+¼) on |z| ≤ 1. Peetre's
inequality and 2L′ − |μ − J + ¼| > n bound the ζ-integral by C⟨η⟩^(μ−J+¼). The last claim: every term of σ_J contains
derivatives of c at y = x. ∎

The reduction serves three purposes below: the adjoint, the change of chart, and the parts of a kernel away from the
diagonal. In each, the derivatives of c that it consumes are counted as derivatives of the symbol from which c is built.

**Lemma {#lem:fwd-far}** (Away from the diagonal.) Let μ be a constant, let b vanish for x ∉ Q_4 and satisfy the
bounds |∂_x^β ∂_ξ^γ b| ≤ A⟨ξ⟩^(μ−|γ|) for |β| ≤ B and |γ| ≤ 2K, and let w ∈ C_c^∞(ℝⁿ) vanish near 0. The operator
with the kernel (2π)^(−n) ∫ e^(i(x−y)·ξ) w(x − y) b(x, ξ) dξ is Op(b_w) with |∂_x^β b_w| ≤ CA⟨ξ⟩^(μ−2K) for
every |β| ≤ B. It consumes 2K ξ-derivatives and B x-derivatives of b, and none in the other directions. Also
Op_ψ(b) = Op(b_ψ) with b_ψ(x, ξ) := (2π)^(−n) ∫ ψ̂(ζ) b(x, ξ − ζ) dζ, and |b_ψ|^𝗆_K ≤ C|b|^𝗆_K for every K and every
order function 𝗆 with values in [−3T, 3T]: the cut-off ψ consumes no derivative.

*Proof.* On supp w, |z|^(−2K)(−Δ_ξ)^K e^(iz·ξ) = e^(iz·ξ), z = x − y, so the kernel is that of the amplitude
w_K(x − y)(−Δ_ξ)^K b(x, ξ), w_K(z) := w(z)|z|^(−2K) ∈ C_c^∞. Multiplication of a kernel by a function of x − y is
convolution of the symbol in ξ with its Fourier transform: the operator is Op(b_w), b_w(x, ξ) = (2π)^(−n)
∫ ŵ_K(ζ)(−Δ_ξ)^K b(x, ξ − ζ) dζ. x-derivatives commute with the convolution, ŵ_K is rapidly decreasing, and Peetre's
inequality gives the bound. The same identity with ψ in place of w_K gives b_ψ. For the variable weight: if
the length of ζ is at most ⟨ξ⟩/2, then 𝗆(x, ξ − ζ) − 𝗆(x, ξ) is at most C|ζ|/⟨ξ⟩ in modulus, so
⟨ξ − ζ⟩^(𝗆(x,ξ−ζ)) ≤ C⟨ξ⟩^(𝗆(x,ξ)) when moreover |ζ| ≤ ⟨ξ⟩^(1/2), and ≤ C⟨ξ⟩^(𝗆(x,ξ))⟨ζ⟩^(C′) otherwise; for
larger ζ, both ⟨ξ⟩ and ⟨ξ − ζ⟩ are at most 3⟨ζ⟩, and the quotient of the weights ⟨·⟩^(𝗆+ϰk−|γ|) of
[[eq:fwd-seminorm]] at ξ − ζ and at ξ, k ≤ K and |γ| ≤ K, is at most C⟨ζ⟩^(6T+K+1). These polynomial factors are
integrable against ψ̂. ∎

*Near and far parts.* Fix ε ∈ (0, 1/8], depending only on the constants of (S1) and (S15), as below, and
η_0 ∈ C_c^∞((−ε, ε)ⁿ) equal to 1 near 0. Split O_β(g) = O^ε_β(g) + O^far_β(g), the near part having the kernel of
Op_ψ(g_β) multiplied by η_0(x − y), and split the adjoint O_β(g)^* likewise. By [[lem:fwd-far]] with
w := ψ(1 − η_0) and μ := sup 𝗆 + ¼ (which bounds 𝗆 plus the loss ϰ(B + 2K) of [[eq:fwd-seminorm]]), O^far_β(g) is
φ_β^* Op(b_w) (φ_β)_* with b_w of order sup 𝗆 + ¼ − 2K, at the cost of 2K ξ-derivatives and B x-derivatives of g;
(O^far_β(g))^* is its adjoint, bounded by duality between the dual spaces ((S3), (S8)), at the same cost. The near
kernels have ranges at most Cε in d_ℬ ((S15)).

**Lemma {#lem:fwd-transport}** (Change of chart, term by term.) Let α, β be charts, κ := φ_β ∘ φ_α⁻¹ (defined where
both are), θ ∈ C_c^∞((−13/8, 13/8)ⁿ), and g a symbol of order 𝗆 with values in [−T, T]. In the chart α the operators
θ O^ε_β(g) and θ O^ε_β(g)^* (the factor θ read in the chart α) are R_c for the amplitudes

    c(x, y, η) = θ(x) η̃(x, y) g_β(κ(x), Φ(x, y)^(−T) η) |det Φ(x, y)|⁻¹ |det Dκ(y)|,
    c^*(x, y, η) = θ(x) η̃^*(x, y) (μ_α(y)/μ_α(x)) g_β(κ(y), Φ(x, y)^(−T) η)^* |det Φ(x, y)|⁻¹
                   × |det Dκ(x)|,                                                                     {#eq:fwd-transport}

where Φ(x, y) := ∫_0^1 Dκ(y + t(x − y)) dt, so that κ(x) − κ(y) = Φ(x, y)(x − y), the star on g is the conjugate
transpose, and η̃(x, y) := (ψη_0)(Φ(x, y)(x − y)), η̃^*(x, y) := \overline{(ψη_0)(Φ(x, y)(y − x))}. Each derivative of
c or c^* in (x, y, η) costs at most one derivative of g, and the bounds of [[lem:fwd-reduction]] hold with μ := sup 𝗆
and A := C|g|^𝗆_(K_c). The transition map κ is differentiated at most K_c + 1 times. The term of σ_J of index 0 is
θ (χ_β g)_α, resp. θ ((χ_β g)^*)_α, the same function on phase space read in the chart α; the term of index γ has the
pointwise order 𝗆 − |γ| and consumes 2|γ| derivatives of g, the variable order being carried exactly, as every term is
evaluated at y = x, that is, at the point of phase space with the chart-α coordinates (x, η).

*Proof.* Let ε be so small that every pair (x, y) with x ∈ supp θ, |x − y| ≤ Cε and x or y in φ_α(supp χ_β) has the
segment from y to x inside the domain of κ and inside (−7/4, 7/4)ⁿ, and that ‖Φ(x, y) − Dκ(x)‖ ≤ ½‖Dκ(x)⁻¹‖⁻¹ for
these pairs; this is possible uniformly in (α, β), as supp χ_β ⊂ φ_β⁻¹([−5/4, 5/4]ⁿ) and by (S1), (S15). (For c^*
the symbol is evaluated at κ(y), with y in φ_α(supp χ_β).) The kernel of θO^ε_β(g) in the chart α is
θ(x)K(κ(x), κ(y))|det Dκ(y)| with K that of Op_(ψη_0)(g_β); substituting ξ = Φ(x, y)^(−T)η, as
(κ(x) − κ(y))·ξ = (x − y)·Φ^Tξ, gives c. For the adjoint of O^ε_β(g), the kernel is μ_α(x)⁻¹ \overline{K^#(y, x)}
μ_α(y) with K^#(y, x) = K(κ(y), κ(x))|det Dκ(x)|; as κ(y) − κ(x) = −Φ(x, y)(x − y), the same substitution gives c^*
after multiplication by θ(x). The variable η enters c and c^* only through the second argument of g. So a derivative
in η is a ξ-derivative of g times an entry of Φ^(−T) (one order lower); a derivative in x or y falls on θ, η̃, the
Jacobians and the quotient of densities (smooth, with derivatives of κ), on the first argument of g (an x-derivative of
g times an entry of Dκ), or on Φ^(−T)η (a ξ-derivative of g times a factor linear in η and in a derivative of Φ, which
leaves the order unchanged). By induction, a derivative of order K_c of c or c^* is a sum of products of one derivative
of g of order at most K_c with derivatives of κ of order at most K_c + 1 (k derivatives of Φ involve those of Dκ of
order k), and its bound is that of [[lem:fwd-reduction]] with A := C|g|^𝗆_(K_c), the constant depending on bounds of κ
in C^(K_c+1), uniform by (S1). At y = x, Φ(x, x) = Dκ(x), η̃ = 1 and the Jacobians cancel, which gives the term of
index 0. A term of index γ has |γ| derivatives in η and |γ| in y: 2|γ| derivatives of g, and the order 𝗆 − |γ| by the
count of orders just given, at the point (κ(x), Dκ(x)^(−T)η). ∎

Each change of chart thus consumes, of the transition map, one derivative more than it consumes of the symbol, and
of the symbol: 2|γ| derivatives in the term of index γ, K + 2|γ| when that term is differentiated K times later, and
2J + B + 2L′ in the remainder ρ_J of [[lem:fwd-reduction]]. The same holds for the adjoint in its own chart (α = β,
κ = id), where it is the reduction of the amplitude c^*.

**Lemma {#lem:fwd-local}** (Boundedness in a chart.) Let A, B ∈ ℕ_0 and put J_1 := 2A + 2B + 1, J_2 := 2A + 1 and

    K(A, B) := J_1 + 6 + 𝔢(n + 1 + J_1 + A + B).                                                       {#eq:fwd-local}

Let b vanish for x ∉ [−7/4, 7/4]ⁿ and have order 𝗆 with values in [−B, B], and let 𝗍 be an order function with values
in [−A, A]. Then ‖Op(b)w‖_(H^(𝗍−𝗆)(ℝⁿ)) ≤ C|b|^𝗆_(K(A,B)) ‖w‖_(H^𝗍(ℝⁿ)). For A = B = T, K(T, T) = 10T + 15.

*Proof.* Let λ := ⟨ξ⟩^(𝗍(x,ξ)−𝗆(x,ξ)), Λ := Op(⟨ξ⟩^(𝗍)) and λ′ ∈ S^(−𝗍) a smooth symbol with Op(λ′)Λ = I + R_∞,
R_∞ of order −∞ (smooth calculus). Norm H^(𝗍−𝗆) with N_0 := A + B + 1. Then
Op(λ)Op(b)w = QΛw − Op(λ)Op(b)R_∞w with Q := Op(λ)Op(b)Op(λ′). The x-derivatives of b of order j ≤ K(A, B) are
bounded by |b|^𝗆_(K(A,B))⟨ξ⟩^(B+¼), the loss ϰj being at most ¼; so [[lem:fwd-crude]] applies to b with μ := B + ¼ and
N := n + 1 + A + B whenever |s − μ| < A + B + 1.
Step 1. Fix θ_1 ∈ C_c^∞((−2, 2)ⁿ) equal to 1 on [−15/8, 15/8]ⁿ and θ_2 ∈ C_c^∞((−29/16, 29/16)ⁿ) equal to 1 on
[−7/4, 7/4]ⁿ. As Op(b) = θ_2Op(b), Op(λ)Op(b) = Op(θ_1λ)Op(b) + Op((1 − θ_1)λ)θ_2Op(b). The kernel of
Op((1 − θ_1)λ)θ_2 is k(x, y) := (2π)^(−n) ∫ e^(i(x−y)·ξ)(1 − θ_1(x))λ(x, ξ) dξ θ_2(y). On its support the distance
of x and y is at least 1/16, so that |x − y| ≥ c⟨x⟩ and |x − y|^(−2L)(−Δ_ξ)^L e^(i(x−y)·ξ) = e^(i(x−y)·ξ). Let
M ∈ ℕ. After L integrations by parts in ξ, 2L ≥ A + B + n + M + 2, the y-derivatives of k of order at most M are
bounded by C⟨x⟩^(−n) and vanish for y ∉ supp θ_2. So the value of Op((1 − θ_1)λ)θ_2w at x is at most
‖k(x, ·)‖_(H^M)‖w‖_(H^(−M)) ≤ C⟨x⟩^(−n)‖w‖_(H^(−M)) in modulus, for w ∈ 𝒮, and Op((1 − θ_1)λ)θ_2 maps H^(−M) to
L², with a norm that depends on λ and M only. With M := A + B + 1, as Op(λ′) maps L² to H^𝗍 ⊂ H^(−A) and Op(b) maps
H^(−A) to H^(−A−B−1) ([[lem:fwd-crude]], s = −A), the operator Op((1 − θ_1)λ)θ_2Op(b)Op(λ′) is bounded on L², at
the cost n + 1 + A + B.
[[lem:fwd-composition]] with p := θ_1λ (order with values in [−A − B, A + B]), q := b (vanishing off Q_4), J := J_1
and 6 x-derivatives of the remainder gives Op(θ_1λ)Op(b) = Op(c_1) + Op(r_1). Here c_1 = λ ♯_(J_1) b, as θ_1 = 1 near
the x-support of b, and r_1 vanishes for x ∉ Q_4, as p does, and has order at most (A + B) + B − J_1 + ½ = −A − ½.
Op(λ′) maps L² to H^𝗍 ⊂ H^(−A), and [[lem:fwd-crude]] (s = −A, μ = −A, N = 6) maps H^(−A) to L². Cost on b:
J_1 + 6 + 2L′ with 2L′ = 𝔢(n + 1 + J_1 + A + B), as |sup(𝗍 − 𝗆) − J_1| ≤ J_1 + A + B; this is K(A, B).
Step 2. [[lem:fwd-composition]] with p := c_1 (order 𝗍, values in [−A, A]), q := λ′ (not compactly supported), J := J_2
and 6 x-derivatives gives Op(c_1)Op(λ′) = Op(c) + Op(r_2), r_2 of order at most 2A − J_2 + ½ = −½ and vanishing for
x ∉ Q_4, as c_1 does; it is bounded on L² by [[lem:fwd-crude]] (N = 6). Cost on c_1: J_2 + 12, on b:
J_2 + 12 + (J_1 − 1) = 4A + 2B + 13 ≤ K(A, B).
Step 3. c = Σ ∂_ξ^(α′)(∂_ξ^α λ · D_x^α b) D_x^(α′) λ′/(α!α′!) has the pointwise order (𝗍 − 𝗆) + 𝗆 − 𝗍 − |α| − |α′|,
the variable orders cancelling at every point; [[lem:fwd-l2]] bounds Op(c) on L² by C|c|^0_12, at a cost on b of
12 + (J_1 − 1) + (J_2 − 1) = 4A + 2B + 12.
Step 4. ‖Op(b)w‖_(H^(−A−B−1)) ≤ C‖w‖_(H^(−A)), and ‖Op(λ)Op(b)R_∞w‖ ≤ C‖Op(b)R_∞w‖_(H^(A+B)) ≤
C‖R_∞w‖_(H^(A+2B+1)) ≤ C‖w‖_(H^(−N_0)), by [[lem:fwd-crude]] with μ := B + ¼ (s = −A, resp. s = A + 2B + 1), at most
n + 1 + A + B x-derivatives of b. Together with Steps 1–3 and ‖Λw‖ ≤ ‖w‖_(H^𝗍) this is the claim.
The largest count is that of Step 1. For A = B = T: J_1 = 4T + 1, 2L′ = 𝔢(6T + 7) = 6T + 8, K = 10T + 15. ∎

**Lemma {#lem:fwd-norms}** (Localisation of the norms.) Let 𝗋 be an order function, θ̃ ∈ C_c^∞((−13/8, 13/8)ⁿ) equal
to 1 on [−3/2, 3/2]ⁿ, and θ̃_α := φ_α^*θ̃. There is C such that, for all u and all functions v_α supported in
[−5/4, 5/4]ⁿ,

    ‖Σ_α φ_α^* v_α‖²_𝗋 ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)(ℝⁿ)),       Σ_α ‖(φ_α)_*(θ̃_α u)‖²_(H^(𝗋_α)(ℝⁿ)) ≤ C ‖u‖²_𝗋.

*Proof.* Only smooth symbols occur. The lemmas above apply to them with N_0 in place of T, every seminorm
[[eq:fwd-seminorm]] being finite, and no derivative is counted; the constants depend on 𝗋, on the cut-offs and on
(S1), (S15), never on the charts. Here N_0 is a fixed integer with N_0 ≥ sup |𝗋|. By (S1) ([Hin26d, Definition
1.1 (1), p. 2]) there is m_ℬ ∈ ℕ such that no point lies in more than m_ℬ of the sets U_α. Fix ℓ ∈ (7/4, 2) such
that the supports of the cut-offs χ° and θ̌ below lie in [−ℓ, ℓ]ⁿ, and let A_α be the set of the β with
φ_α⁻¹([−ℓ, ℓ]ⁿ) ∩ φ_β⁻¹([−ℓ, ℓ]ⁿ) ≠ ∅; so β ∈ A_α exactly when α ∈ A_β.

*The count.* There is N_ℬ ≥ m_ℬ with |A_α| ≤ N_ℬ for every α. Indeed, let C_1 ≥ 1 bound the norms of the first
derivatives of the transition maps τ_(βα) = φ_β ∘ φ_α⁻¹, uniformly in (α, β) ((S1)), and put r := (2 − ℓ)/(2C_1).
Let β ∈ A_α, p a point of φ_α⁻¹([−ℓ, ℓ]ⁿ) ∩ φ_β⁻¹([−ℓ, ℓ]ⁿ), x := φ_α(p), and W := φ_α(U_α ∩ U_β), an open set
that contains x, on which τ_(βα) is defined. Let x_t := x + tv for 0 ≤ t ≤ t_1, with |v| = 1 and t_1 < r. Each
coordinate of x_t differs from that of x by less than r < 2 − ℓ, so x_t ∈ (−2, 2)ⁿ. Suppose that some x_t lies
outside W, and let t_* be the least such t (it exists as W is open, and t_* > 0 as x ∈ W). For t, t′ < t_*, the
segment from x_t to x_(t′) lies in W, so that |τ_(βα)(x_t) − τ_(βα)(x_(t′))| ≤ C_1|t − t′|; with t′ = 0, as
τ_(βα)(x_0) = φ_β(p), the distance of τ_(βα)(x_t) from φ_β(p) is at most C_1t_* < C_1r = (2 − ℓ)/2. So τ_(βα)(x_t)
converges, as t ↑ t_*, to a point y whose coordinates have modulus at most ℓ + (2 − ℓ)/2 = (2 + ℓ)/2 < 2, that is,
y ∈ (−2, 2)ⁿ. The points φ_α⁻¹(x_t) = φ_β⁻¹(τ_(βα)(x_t)) then converge on the manifold both to φ_α⁻¹(x_(t_*)) and
to φ_β⁻¹(y) ∈ U_β. As the manifold is Hausdorff, φ_α⁻¹(x_(t_*)) lies in U_α ∩ U_β, that is, x_(t_*) ∈ W, a
contradiction. So the segment stays in W, and the ball of radius r about x lies in W. Cover [−ℓ, ℓ]ⁿ by N_1 balls
of radius r/2, N_1 depending only on n, ℓ and C_1. If A_α had more than m_ℬN_1 elements, then, choosing p and x as
above for each β ∈ A_α, the points x of m_ℬ + 1 of these β would lie in one of the balls. Its centre c lies within r/2
of each of these points x, hence in φ_α(U_α ∩ U_β) for each of these m_ℬ + 1 values of β, and the point φ_α⁻¹(c)
lies in m_ℬ + 1 of the sets U_β, against the choice of m_ℬ. So N_ℬ := m_ℬN_1 serves.

*Integer orders.* Let k ∈ ℤ, K ⊂ [−ℓ, ℓ]ⁿ compact, ϑ ∈ C_c^∞((−2, 2)ⁿ) with supp ϑ ⊂ [−ℓ, ℓ]ⁿ, and
ϑ_α := φ_α^*ϑ. We show

    ‖Σ_α φ_α^* w_α‖²_k ≤ C Σ_α ‖w_α‖²_(H^k(ℝⁿ))  (supp w_α ⊂ K),      Σ_α ‖(φ_α)_*(ϑ_α u)‖²_(H^k(ℝⁿ)) ≤ C ‖u‖²_k.

They are used below with K = [−5/4, 5/4]ⁿ or K = supp θ̃, and with ϑ = θ̃ or ϑ = θ̌; these lie in [−ℓ, ℓ]ⁿ, as
13/8 < ℓ and by the choice of ℓ. By (S3), ‖u‖²_k = Σ_β ‖(φ_β)_*(χ°_βu)‖²_(H^k(ℝⁿ)) with χ°_β := φ_β^*χ°,
where χ° ∈ C_c^∞((−2, 2)ⁿ) equals 1 on [−1, 1]ⁿ ([Hin26d, Definition 3.14, p. 34]) and is taken with 0 ≤ χ° ≤ 1,
which changes the norm only up to equivalence ([Hin26d, p. 36]); as the sets φ_β⁻¹((−1, 1)ⁿ) cover ((S1)) and no
point lies in more than m_ℬ ≤ N_ℬ of the U_β, 1 ≤ Σ_β χ°_β ≤ N_ℬ. For charts α, β and a function ϕ on (−2, 2)ⁿ that
vanishes outside φ_α(F), with F ⊂ U_α ∩ U_β compact, put T^ϕ_(βα)w := (ϕw) ∘ φ_α ∘ φ_β⁻¹ on φ_β(U_α ∩ U_β),
extended by 0. If the derivatives of ϕ of order at most |k| are bounded, then ‖T^ϕ_(βα)w‖_(H^k) ≤ C‖w‖_(H^k). For
k ≥ 0 this is Leibniz's rule, the chain rule and the change of variables, the transition maps and their inverses
having bounded derivatives ((S1)). For k < 0 it follows by duality, the L²-adjoint of T^ϕ_(βα) being T^(ϕ′)_(αβ)
with ϕ′ := (ϕ̄ |det D(φ_β ∘ φ_α⁻¹)|) ∘ φ_α ∘ φ_β⁻¹, a function of the same kind. Now
(φ_β)_*(χ°_βφ_α^*w_α) = T^ϕ_(βα)w_α with ϕ := χ̌ · (χ° ∘ φ_β ∘ φ_α⁻¹), where χ̌ ∈ C_c^∞((−2, 2)ⁿ) equals 1 on K and
χ° ∘ φ_β ∘ φ_α⁻¹, extended by 0, is smooth, as φ_β⁻¹(supp χ°) is compact; and it vanishes unless α ∈ A_β. So the
left side of the first bound is at most Σ_β N_ℬ Σ_(α∈A_β) C‖w_α‖², which is at most CN_ℬ² Σ_α ‖w_α‖². For the
second, ϑ_αu = Σ_(β∈A_α) ϑ_αζχ°_βu with ζ := (Σ_γ χ°_γ)⁻¹, whose derivatives in the charts are bounded, and
(φ_α)_*(ϑ_αζχ°_βu) = T^ϕ_(αβ)(φ_β)_*(χ°_βu) with ϕ := χ̌′ · ((ϑ_αζ) ∘ φ_β⁻¹), where χ̌′ ∈ C_c^∞((−2, 2)ⁿ) equals 1
on supp χ°; summing as before gives the second bound.

*Two facts.* Put Λ := Op(ρ_∞^(−𝗋)) ∈ Ψ̃^𝗋 and Λ′_0 := Op(ρ_∞^𝗋). By (S5) and (S8), Λ′_0Λ = I − R_1 with R_1 of
order −½, as the principal symbols multiply to 1 and Op(1) = I ([[eq:ii-a1-1-1]]). So Λ′ := Σ_(j<4N_0) R_1^jΛ′_0
satisfies Λ′Λ = I + R with R := −R_1^(4N_0) of order −2N_0, and Λ′ = Op(λ′) + R′, where λ′ is a smooth symbol of
order −𝗋 and R′ ∈ Ψ̃^(−∞) ((S4), (S8)). H^𝗋 is the space of the u ∈ H^(−N_0) with Λu ∈ L² ([[sec:ii-a1-1-1]],
(S8)), normed by ‖u‖_𝗋 := ‖Λu‖ + ‖u‖_(−N_0). On ℝⁿ, ‖w‖_(H^(𝗋_α)) ≤ C‖w‖_(H^(N_0)), as Op(⟨ξ⟩^(𝗋_α))⟨D⟩^(−N_0) is
Op(⟨ξ⟩^(𝗋_α−N_0)), bounded on L² by [[lem:fwd-l2]]. Let θ̌ ∈ C_c^∞((−2, 2)ⁿ) equal 1 on [−7/4, 7/4]ⁿ and
θ̌_α := φ_α^*θ̌. For a smooth symbol g of order 𝗆 with values in [−N_0, N_0], Op(g) = Σ_β O^ε_β(g) + Σ_β O^far_β(g)
([[eq:fwd-chart-op]] and the near and far parts above).

(P1) Σ_β O^far_β(g) maps H^(−N_0) to H^(N_0). Indeed, by [[lem:fwd-far]] with 2K ≥ 3N_0 + 1, and as the kernel of
O_β(g) joins points within ¼ in the chart β, O^far_β(g)u = φ_β^*Op(b^β)(φ_β)_*(θ̌_βu), with b^β vanishing for
x ∉ (−5/4, 5/4)ⁿ and of order at most −2N_0. By [[lem:fwd-crude]] (s = −N_0, μ = −2N_0) and the integer bounds at
the orders N_0 and −N_0, ‖Σ_β O^far_β(g)u‖²_(N_0) ≤ C Σ_β ‖(φ_β)_*(θ̌_βu)‖²_(H^(−N_0)) ≤ C‖u‖²_(−N_0).

(P2) For charts α, β, (φ_α)_*(θ̃_αO^ε_β(g)f) = (Op(σ) + Op(ρ))(φ_α)_*(θ̌_αf), where σ and ρ vanish for x ∉ supp θ̃
and unless β ∈ A_α, σ has order 𝗆_α, and every x-derivative of ρ is bounded by C⟨ξ⟩^(−2N_0). Indeed, by
[[lem:fwd-transport]] with θ := θ̃, the left side is R_c applied to (φ_α)_*f, whose amplitude c contains the factor
θ̃(x) and vanishes unless y ∈ (−7/4, 7/4)ⁿ (the choice of ε in that proof), so that θ̌_α may be inserted. As g_β
vanishes for x ∉ (−5/4, 5/4)ⁿ, c contains the factor θ̃(x)g_β(κ(x), ·), which vanishes unless φ_α⁻¹(x) lies in
φ_α⁻¹(supp θ̃) ∩ φ_β⁻¹([−5/4, 5/4]ⁿ); so c vanishes identically, and with it the σ and ρ below, unless β ∈ A_α. (In
other words, θ̃_α is supported in φ_α⁻¹(supp θ̃), and O^ε_β(g)f in φ_β⁻¹([−5/4, 5/4]ⁿ) by left quantization.) Then
[[lem:fwd-reduction]] with J := 3N_0 + 1 gives σ := σ_J, of order 𝗆_α as its terms of index γ have the pointwise
order 𝗆_α − |γ|, and ρ := ρ_J, of order at most N_0 − J + ½ < −2N_0. So, for every order 𝗍 with values in
[−N_0, N_0], Op(σ) maps H^(𝗍_α) to H^(𝗍_α−𝗆_α) by [[lem:fwd-local]], as σ vanishes for x ∉ [−7/4, 7/4]ⁿ, and Op(ρ)
maps H^(−N_0) to H^(N_0) by [[lem:fwd-crude]]; both uniformly in (α, β).

*The first bound.* Let u := Σ_α φ_α^*v_α, first with finitely many v_α ≠ 0, and λ_0 := ρ_∞^(−𝗋), so that
Λ = Op(λ_0). By the integer bound at −N_0, ‖u‖²_(−N_0) ≤ C Σ_α ‖v_α‖²_(H^(−N_0)) ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)), and by
(P1), ‖Σ_β O^far_β(λ_0)u‖ ≤ C‖u‖_(−N_0). The kernel of O^ε_β(λ_0) joins points within Cε in d_ℬ ((S15)), so for ε
small O^ε_β(λ_0)φ_α^*v_α is supported where θ̃_α = 1. By (P2) with 𝗍 := 𝗋, as θ̌ = 1 on supp v_α,
Σ_β O^ε_β(λ_0)φ_α^*v_α = φ_α^*V_α with V_α := Σ_(β∈A_α) (Op(σ_(αβ)) + Op(ρ_(αβ)))v_α, which vanishes outside
supp θ̃ and has ‖V_α‖ ≤ CN_ℬ‖v_α‖_(H^(𝗋_α)). The integer bound at the order 0 with K := supp θ̃ gives
‖Σ_α φ_α^*V_α‖² ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)). So ‖u‖²_𝗋 ≤ C Σ_α ‖v_α‖²_(H^(𝗋_α)). For infinitely many v_α, the partial
sums converge in H^(−N_0), by the integer bound, and are Cauchy in H^𝗋, by this bound; their limit is u.

*The second bound.* Let f := Λu, so ‖f‖ ≤ ‖u‖_𝗋, and u = Λ′f − Ru = Σ_β O^ε_β(λ′)f + h with
h := Σ_β O^far_β(λ′)f + R′f − Ru. By (P1), and as R′ is residual and R has order −2N_0,
‖h‖_(N_0) ≤ C(‖f‖ + ‖u‖_(−N_0)) ≤ C‖u‖_𝗋, and the integer bound at N_0 with ϑ := θ̃ gives
Σ_α ‖(φ_α)_*(θ̃_αh)‖²_(H^(𝗋_α)) ≤ C Σ_α ‖(φ_α)_*(θ̃_αh)‖²_(H^(N_0)) ≤ C‖u‖²_𝗋. By (P2) with g := λ′, of order −𝗋, and
𝗍 := 0, ‖(φ_α)_*(θ̃_αO^ε_β(λ′)f)‖_(H^(𝗋_α)) ≤ C‖(φ_α)_*(θ̌_αf)‖, and the left side vanishes unless β ∈ A_α. So, by
the integer bound at the order 0 with ϑ := θ̌, the sum over α of ‖(φ_α)_*(θ̃_α Σ_β O^ε_β(λ′)f)‖²_(H^(𝗋_α)) is at most
CN_ℬ² Σ_α ‖(φ_α)_*(θ̌_αf)‖² ≤ C‖f‖² ≤ C‖u‖²_𝗋. As θ̃_αu = θ̃_α Σ_β O^ε_β(λ′)f + θ̃_αh, the second bound follows. ∎

**Lemma {#lem:fwd-expansion}** (A product in a chart.) Let r ∈ {1, …, 6}, S ≥ 0 an integer, and F_1, …, F_r each of
the form Op(g_j) or Op(g_j)^*, the symbol g_j of order 𝗆_j with values in [−T, T] (smooth symbols, such as those of
localisers, are allowed). Put

    R := S + rT,   B := n + 1 + max((r + 1)T, S + (r − 1)T),   J_R := T + R + 1,   J_C := rT + R + 1,
    2K := the least even integer ≥ T + R + 1.                                                         {#eq:fwd-expansion}

For each chart α let s_j be the sum over β of the terms of index < J_R of the reductions of θ^(j) O^ε_β(g_j) (resp. of
the adjoints) in the chart α ([[lem:fwd-transport]]), θ^(1) := χ_α and θ^(j) := θ̂ for j ≥ 2, θ̂ ∈ C_c^∞((−13/8, 13/8)ⁿ)
equal to 1 on [−3/2, 3/2]ⁿ, and let t_α := s_1 ♯_(J_C) s_2 ♯_(J_C) ⋯ ♯_(J_C) s_r, computed from the left. Then

    F_1 ⋯ F_r = Σ_α φ_α^* Op(t_α) (φ_α)_* θ̃_α + E,                                                  {#eq:fwd-product}

where E maps H^𝗍 to H^S, for every order 𝗍 with values in [−T, T], with norm at most C ∏_j |g_j|^(𝗆_j)_(K_j), and the
derivatives of each g_j consumed in E are at most

    max( 2J_R + B + 𝔢(n + 1 + J_R + T),  2K + B,  B + 2(J_R − 1),  (J_C + B) + (r − 2)(J_C − 1) + 2(J_R − 1),
         J_C + B + 𝔢(n + 1 + J_C + (r − 1)T) + 2(J_R − 1) ),                                         {#eq:fwd-ecount}

the last two only if r ≥ 2. A derivative of order K′ of t_α consumes at most K′ + (r − 1)(J_C − 1) + 2(J_R − 1)
derivatives of each g_j. Each term of t_α is a product of derivatives of the terms of the s_j at one point (x, η); its
grade, the sum of the indices |γ| of the reductions and of the indices |α| of the compositions that produced it, lowers
the pointwise order Σ_j 𝗆_j by exactly that number.

*Proof.* Write F_j = F^ε_j + F^far_j, the sums over β of the near and far parts. The product of the near parts is
Σ_α χ_α F^ε_1 ⋯ F^ε_r, and the kernel of χ_α F^ε_1 ⋯ F^ε_r joins points within rCε ≤ 1/8 in d_ℬ of supp χ_α, inside
φ_α⁻¹([−3/2, 3/2]ⁿ) for ε small; so inserting θ̂ in front of F^ε_j, j ≥ 2, and θ̃_α on the right changes nothing. In the
chart α, by [[lem:fwd-reduction]] and [[lem:fwd-transport]] with J := J_R, each θ^(j)F^ε_j is Op(s_j) + Op(ρ_j), ρ_j of
order at most T − J_R + ½ = −R − ½. Only the β ∈ A_α of the proof of [[lem:fwd-norms]], at most N_ℬ of them,
contribute to s_j and ρ_j: the amplitude contains θ^(j)(x) and g_β at κ(x), resp. at κ(y) with y ∈ (−7/4, 7/4)ⁿ
([[eq:fwd-transport]] and the choice of ε there), and g_β vanishes for x ∉ (−5/4, 5/4)ⁿ. Expanding, the product is
Op(s_1)⋯Op(s_r) plus terms with a factor Op(ρ_j). By [[lem:fwd-composition]] (q vanishing off Q_4) with J := J_C
applied r − 1 times from the left,
Op(s_1)⋯Op(s_r) = Op(t_α) + Σ_(j≥2) Op(r_j) Op(s_(j+1)) ⋯ Op(s_r), r_j of order at most jT − J_C + ¾ ≤ −R − ¼. The far
terms are products with at least one factor F^far_j, of order at most T − 2K + ½ ≤ −R − ½ ([[lem:fwd-far]]).

So every term of E is a product of at most r operators, one of order at most −R (the gaining factor) and the others of
order at most T, which we bound between Sobolev spaces of constant order by [[lem:fwd-crude]], chart by chart, and on
the manifold by [[lem:fwd-norms]] at constant orders (not integers in general); adjoints by duality. Start from
H^𝗍 ⊂ H^(−T). The factors to the right of the gaining factor lower
the order by at most T each, the gaining factor raises it by R, the others lower it by at most T: the result lies in
H^(−T−(r−1)T+R) = H^S. The input orders s of the factors of order at most T lie in [−rT, R − T], so |s − T| ≤
max((r + 1)T, R − 2T); that of the gaining factor lies in [−rT, −T], so |s + R| ≤ R − T = S + (r − 1)T. So B
x-derivatives suffice in every application of [[lem:fwd-crude]]. The bounds that [[lem:fwd-crude]] needs carry the loss
ϰ. A factor of order at most T satisfies them with μ := T + 1/32, as its symbol is differentiated at most 𝔐(T) times
(the counts below) and ϰ𝔐(T) = 1/32. The bounds [[eq:fwd-reduction]], [[eq:fwd-remainder]] and those of
[[lem:fwd-far]] include the loss, so the gaining factor satisfies them with μ := −R − ¼. The at most five shifts by
1/32 lower the final order by less than ¼ and change each |s − μ| by less than 1; so the result lies in H^S, and
N := B satisfies N > n + |s − μ| in every application.

The counts, all derivatives of g_j: ρ_j costs 2J_R + B + 2L′ with 2L′ = 𝔢(n + 1 + J_R + T) ([[lem:fwd-reduction]], as
the distance from sup 𝗆_j to J_R is at most J_R + T); a far part costs 2K + B ([[lem:fwd-far]]); a factor Op(s_j)
bounded by [[lem:fwd-crude]] costs B + 2(J_R − 1) ([[lem:fwd-transport]]). In the composition of
t_(j−1) := s_1 ♯ ⋯ ♯ s_(j−1) with s_j, the left symbol needs J_C + B derivatives and the right one J_C + B + 2L′_C,
2L′_C = 𝔢(n + 1 + J_C + (j − 1)T), since the order of t_(j−1) has supremum within J_C + (j − 1)T of J_C. The symbol
t_(j−1) already contains, on s_i, at most (j − 2)(J_C − 1)
derivatives (ξ-derivatives from the j − 2 compositions in which it stood on the left, or x-derivatives from the one in
which it stood on the right and ξ-derivatives from the later ones), and s_i contains 2(J_R − 1) derivatives of g_i. With
j ≤ r this gives the last two entries of [[eq:fwd-ecount]], and the statement on t_α. The grades are those of
[[lem:fwd-composition]] and [[lem:fwd-transport]]. ∎

**Proposition {#prop:fwd-calculus}** (Explicit indices.) Let T ∈ ℕ. Let 𝗍 (the order of the space on which an item is
applied) and the orders 𝗆, 𝗆_1, 𝗆_2 of the symbols have values in [−T, T], of any index ν. Then [[prop:ii-a1-2-4]]
holds with M + 2 = 𝔐(T) = 200T + 100 in the following form.

(a)–(d) as stated there, with at most 10T + 15, 34T + 24, 18T + 23 and 34T + 32 derivatives of each symbol.

(e) For every N ≤ T and every expression S_1B_1𝒯B_2S_2 with at most six quantizations in each of its products (the
localisers and B_1, B_2 included), each quantized symbol of order with values in [−T, T]: at most 95T + 7 derivatives.

(f) For every expression 𝒯 with at most six quantizations in each product, each quantized symbol (a product of the a_i
included) of order with values in [−T, T], and every order function μ with values in [−6T − 3, 6T + 3] such that, in
every chart α, the symbol t_α of 𝒯 ([[lem:fwd-expansion]], the signed sum over the products of 𝒯) is a sum of products
of derivatives of pointwise order at most μ (up to the loss ϰ times the number of derivatives): 𝒯 has order μ + δ,
with at most 158T + 52 derivatives.

Here 𝒯 denotes an expression, and T the integer bounding the orders. [[lem:ii-a-8-5]] (a) holds with d_0 = 𝔐(T) when
𝗌 has values in [−T, T] (10T + 15 derivatives), and (b) when 𝗌_0 has values in [−T, T] and sup 𝗌 − inf 𝗌_0 ≤ T
(34T + 15 derivatives). For T = 100 the largest count is 15,852 ≤ 𝔐(100) − 2.

In this form the hypothesis of (f) is an identity of symbols, and it is checked at each use in [[lem:fwd-box]]: there
the terms above the order μ cancel because the leading terms of an adjoint and of the conjugate symbol agree, because
scalar symbols commute with all others, and by exact identities such as φ_0ǎ = ǎ.

*Proof.* Every symbol below is read in the charts of ρℬ, where |a_α|^𝗆_K ≤ C‖a‖_((K);ν,𝗆) (the beginning of this
section); the constants C depend on ϰ, ν, the orders, the bounds of (S1) for the transition maps (differentiated at
most 𝔐(T) + 1 times, by [[lem:fwd-transport]] and the counts below), and on the smooth symbols involved, never on
their supports beyond the identities used. The global estimate is assembled in the same way in every item: if
𝒯 = Σ_α φ_α^* Op(t_α)(φ_α)_*θ̃_α + E with t_α vanishing for x ∉ [−5/4, 5/4]ⁿ, |t_α|^(μ+δ)_(K(T,B_G)) ≤ C uniformly in
α, μ with values in [−B_G, B_G], and E bounded from H^𝗍 to H^S with S ≥ sup(𝗍 − μ), then by [[lem:fwd-local]] (with
A := T, B := B_G) and [[lem:fwd-norms]] (twice)

    ‖𝒯u‖_(𝗍−μ−δ) ≤ C(Σ_α ‖Op(t_α)(φ_α)_*(θ̃_αu)‖²_(H^((𝗍−μ−δ)_α)))^(1/2) + ‖Eu‖_S ≤ C‖u‖_𝗍.        {#eq:fwd-assembly}

So each item reduces to: the parameters (S, B_G) of [[lem:fwd-expansion]] and [[lem:fwd-local]], the check that t_α has
the stated order, and the counts. The integers in brackets are those for T = 100.

*(a).* By [[eq:fwd-chart-op]] and [[lem:fwd-far]], Op(a)u = Σ_α φ_α^* Op((a_α)_ψ)(φ_α)_*(θ̃_α u), the kernel of
Op_ψ(a_α) joining points within ¼, and |(a_α)_ψ|^𝗆_K ≤ C|a_α|^𝗆_K: no change of chart and no expansion is needed.
[[lem:fwd-local]] with A = B = T and [[lem:fwd-norms]] give (a) without loss, with K(T, T) = 10T + 15 [1,015]
derivatives: J_1 = 4T + 1 [401], 2L′ = 6T + 8 [608]. Multiplication by ℓ is Op(ℓ) ((S4), [[eq:ii-a1-1-1]]), with
𝗆 = 0 and ‖ℓ‖_((K);0,0) ≤ C‖ℓ‖_(C^K_e3b); so [[lem:ii-a-8-5]] (a) holds with d_0 = 10T + 15 [1,015], and its
b-regularity part follows by Leibniz's rule as there.

*The symbols of one operator in a chart.* For a symbol g let s^α_j(g), resp. s^α_j(g^*), be the symbol s_j of
[[lem:fwd-expansion]] for F_j = Op(g), resp. Op(g)^*, with the left cut-off θ^(j). By [[lem:fwd-transport]] its term
of index 0 is θ^(j) Σ_β χ_β g = θ^(j)g, resp. θ^(j)g^*, read in the chart α, and its term of index 1 is θ^(j)V_α(g),
resp. θ^(j)V^*_α(g), with V_α(g) the sum over β of the terms of index 1 of the reductions of the amplitudes of
[[eq:fwd-transport]] without the factor θ: a linear expression in g and its first and second derivatives with scalar
coefficients, so that V_α(g) is scalar when g is, and commutes with every matrix when g is scalar. Every term of
s^α_j(g) vanishes where all derivatives of g vanish, that is, outside the support of g read in the chart α.

*(b).* Here 𝒯 := Op(a_1)Op(a_2) − Op(a_1a_2). [[lem:fwd-expansion]] applies to Op(a_1)Op(a_2) with r = 2, and to
Op(a_1a_2) with r = 1 and T replaced by 2T (its symbol has order 𝗆_1 + 𝗆_2 with values in [−2T, 2T], and the
order 𝗍 has values in [−2T, 2T]), both with S := 3T + 1 [301] ≥ sup(𝗍 − 𝗆_1 − 𝗆_2 + 1). Then
t_α = s^α_1(a_1) ♯ s^α_2(a_2) − s^α_1(a_1a_2), and its terms of grade 0 are χ_αa_1 · θ̂a_2 − χ_αa_1a_2 = 0, as θ̂ = 1
on supp χ_α. So t_α is a sum of terms of grade at least 1, of pointwise order at most 𝗆_1 + 𝗆_2 − 1 up to the loss:
μ := 𝗆_1 + 𝗆_2 − 1, B_G := 2T + 1. Counts for Op(a_1)Op(a_2), from [[eq:fwd-expansion]]: R = 5T + 1 [501],
B = 4T + 7 [407], J_R = 6T + 2 [602], 2K = 6T + 2 [602], J_C = 7T + 2 [702]; by [[eq:fwd-ecount]] the remainder of
the reductions costs 2J_R + B + 𝔢(7T + 8) ≤ 23T + 21 [2,321], the far parts 10T + 9 [1,009], a factor Op(s_j)
16T + 9 [1,609], the compositions at most J_C + B + 𝔢(8T + 8) + 2(J_R − 1) ≤ 31T + 21 [3,121]; the main symbol costs
K(T, 2T + 1) + (J_C − 1) + 2(J_R − 1) ≤ (15T + 21) + (7T + 1) + (12T + 2) = 34T + 24 [3,424], with
K(T, 2T + 1) = J_1 + 6 + 𝔢(9T + 10), J_1 = 6T + 3 [603]. For Op(a_1a_2) (T replaced by 2T): R = 5T + 1, B = 4T + 6,
J_R = 7T + 2, the remainders cost at most 27T + 20 [2,720], 11T + 9 and 18T + 8, and the main symbol at most
K(T, 2T + 1) + 2(J_R − 1) ≤ 29T + 23 [2,923]; derivatives of a_1a_2 are derivatives of a_1 and a_2 in equal number.
So (b) holds with 34T + 24 [3,424] derivatives, by [[eq:fwd-assembly]].

*(c).* Here 𝒯 := Op(a)^* − Op(a^*), a^* the conjugate transpose (the conjugate for scalar a). [[lem:fwd-expansion]]
with r = 1 for both, S := 2T + 1 [201]. The terms of grade 0 of t_α = s^α_1(a^*) − s^α_1(a^*) (the first for the
adjoint, the second for the quantization of a^*) are χ_αa^* − χ_αa^* = 0 by [[lem:fwd-transport]]. μ := 𝗆 − 1,
B_G := T + 1. Counts: R = 3T + 1 [301], B = 2T + 7 [207], J_R = 4T + 2 [402]; the remainders cost at most
2J_R + B + 𝔢(5T + 8) ≤ 15T + 21 [1,521], 6T + 9 [609] and 10T + 9 [1,009]; the main symbol
K(T, T + 1) + 2(J_R − 1) = (10T + 21) + (8T + 2) = 18T + 23 [1,823], K(T, T + 1) = (4T + 3) + 6 + (6T + 12).

*(d).* Here 𝒯 := i[Op(a_1), Op(a_2)] − Op(H_(a_1)a_2), one of a_1, a_2 scalar. [[lem:fwd-expansion]] with r = 2 for
the two products and r = 1, T replaced by 2T + 1, for Op(H_(a_1)a_2), whose symbol consumes one derivative of each a_i;
S := 3T + 2 [302]. In t_α the terms of grade 0 are iχ_α(a_1a_2 − a_2a_1) = 0. The terms of grade 1 are, as θ̂ = 1 and
D_xθ̂ = 0 on supp χ_α and ∂_ξχ_α = 0,

    iχ_α(a_1V_α(a_2) − V_α(a_2)a_1 + V_α(a_1)a_2 − a_2V_α(a_1)) + χ_α Σ_j (∂_(ξ_j)a_1 ∂_(x_j)a_2 − ∂_(ξ_j)a_2 ∂_(x_j)a_1)
        − χ_α H_(a_1)a_2.

The first group vanishes as one of a_1, a_2, and then also its V_α, is scalar. The second is χ_α times the principal
symbol of i[Op(a_1), Op(a_2)] in the chart α, which is H_(a_1)a_2 by (S5) (entrywise when one symbol is a matrix). So
t_α has terms of grade at least 2 only: μ := 𝗆_1 + 𝗆_2 − 2, B_G := 2T + 2. Counts for the products: R = 5T + 2,
B = 4T + 8, J_R = 6T + 3, 2K ≤ 6T + 4, J_C = 7T + 3; remainders at most 23T + 25, 10T + 12, 16T + 12, 31T + 25; main
K(T, 2T + 2) + (J_C − 1) + 2(J_R − 1) ≤ (15T + 26) + (7T + 2) + (12T + 4) = 34T + 32 [3,431]. For Op(H_(a_1)a_2):
R = 5T + 3, B = 4T + 8, J_R = 7T + 5, counts at most 27T + 33, 11T + 15, 18T + 17 and 29T + 35, each including the
derivative taken by H. So (d) holds with 34T + 32 [3,431] ≤ M + 1 derivatives.

*(e).* Write B_i = Op(b_i) + R_i with supp b_i ⊂ K_i and R_i ∈ Ψ̃^(−∞) ([[sec:ii-a1-1-2]]), and expand the expression
into products. A product containing R_1 or R_2 is a product of at most six operators, R_i of every order and the others
of order at most T, bounded from H^𝗍 to H^(T+N) by [[lem:fwd-crude]] as in the proof of [[lem:fwd-expansion]], at the
cost B + 2(J_R − 1) below. For a product containing Op(b_1) and Op(b_2), [[lem:fwd-expansion]] applies with r ≤ 6 and
S := T + N ≤ 2T. Every term of its t_α contains a derivative of a term of s^α(b_1), which vanishes outside K_1 read in
the chart α, and one of a term of s^α(b_2), which vanishes outside K_2, both at the same point (x, η); as K_1 ∩ K_2 = ∅,
t_α = 0. So the operator is E of [[eq:fwd-product]], bounded from H^𝗍 to H^(T+N) ⊂ H^(𝗍+N): it has order −N. The counts
are largest for r = 6 and S = 2T: R = 8T [800], B = 7T + 6 [706], J_R = 9T + 1 [901], 2K ≤ 9T + 2 [902],
J_C = 14T + 1 [1,401]. By [[eq:fwd-ecount]]: 2J_R + B + 𝔢(10T + 7) = 35T + 16 [3,516]; 16T + 8 [1,608]; 25T + 6
[2,506]; (J_C + B) + 4(J_C − 1) + 2(J_R − 1) = 95T + 7 [9,507]; J_C + B + 𝔢(19T + 7) + 2(J_R − 1) ≤ 58T + 16 [5,815].
So (e) holds with 95T + 7 [9,507] derivatives. No auxiliary symbol y and no commutator expansion is needed: the
operators B_1, B_2 enter only the constants, through their symbols and the sets K_1, K_2.

*(f).* [[lem:fwd-expansion]] for each product, r ≤ 6, S := 7T + 3 [703] ≥ sup(𝗍 − μ), and [[eq:fwd-assembly]] with
B_G := 6T + 3, which the hypothesis on t_α allows. The counts are largest for r = 6: R = 13T + 3 [1,303],
B = 12T + 9 [1,209], J_R = 14T + 4 [1,404], 2K = 14T + 4 [1,404], J_C = 19T + 4 [1,904]; the remainders cost at most
2J_R + B + 𝔢(15T + 10) ≤ 55T + 29 [5,529], 26T + 13 [2,613], 40T + 15 [4,015],
(J_C + B) + 4(J_C − 1) + 2(J_R − 1) = 135T + 31 [13,531] and J_C + B + 𝔢(24T + 10) + 2(J_R − 1) ≤ 83T + 31
[8,331]; the main symbol K(T, 6T + 3) + 5(J_C − 1) + 2(J_R − 1) ≤ (35T + 31) + (95T + 15) + (28T + 6) = 158T + 52
[15,852], with K(T, 6T + 3) = (14T + 7) + 6 + 𝔢(21T + 16).

*[[lem:ii-a-8-5]] (b).* By [[sec:ii-a1-1-2]], B and I − B^♯ are microsupported in disjoint closed sets, near fibre
infinity. So Bℓ(I − B^♯), a product of three quantizations of order 0 (ℓ = Op(ℓ) as in (a)), is the case r = 3 of (e)
at the constant order 𝗍 := inf 𝗌_0 with N := max(0, ⌈sup 𝗌 − inf 𝗌_0⌉) ≤ T: it maps H^(𝗌_0) ⊂ H^(inf 𝗌_0) to
H^(inf 𝗌_0 + N) ⊂ H^𝗌. With S = 2T: R = 5T, B = 4T + 6, J_R = 6T + 1, J_C = 8T + 1, and the counts of
[[eq:fwd-ecount]] are at most 23T + 17, 10T + 8, 16T + 6, 32T + 7 and 34T + 15 [3,415]. So d_0 = 34T + 15 serves in
(b), and d_0 = 𝔐(T) a fortiori. The index does not depend on B and B^♯.

In every item the number of derivatives of any symbol is at most 158T + 52 ≤ 𝔐(T) − 2, and every product estimated
has at most eight factors, which justifies the choice of ϰ. ∎

#### The sites, the orders that occur, and the increments {#sec:fwd-box}

By [[eq:ii-f1-3-2]] and [[rem:ii-f1-7-1]] with d̄_ℵ = 1, D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) with: d^E_0 the d_0 of
[[thm:ii-e-6-1]] at (𝗌_0, 𝗌) = (𝗌 − 3, 𝗌); d^S_0 the largest d_0 of [[prop:ii-e-3-4]], [[prop:ii-e-4-3]] and
[[prop:ii-e-4-4]] at the slab orders 𝗌 and 𝗌 + 2; d^T_0 that of [[lem:ii-f1-2-8]] at 𝗍 = 𝗌; d^U_0 that of
[[prop:ii-e-3-4]] (i) at s′ = s_u = −12. By [[lem:fwd-orders]], 𝗌 has values in [−10, 11], equals 11 near the
horizon, the trapped set, ∂R_(∂K⁺,in) and ∂R_(ℐ⁺,in,+), and −10 near ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out); 𝗌_0 has values in
[−13, 8]. The a priori order of [[ch:s06]] is N′ := 13 = −inf 𝗌_0, which is all that its a priori terms
‖χu‖_(−N′) ≤ ‖u‖_(𝗌_0) require. A *site* is a result of [[ch:s04]] and [[ch:s06]]–[[ch:s09]] whose proof applies a
closed-graph index (an index of [[prop:ii-a1-2-4]] or of [[lem:ii-a-8-5]], directly or through another site), or
raises one. For s an order function write s⁺ := sup s and s⁻ := inf s. [[prop:fwd-calculus]] with T = 100 applies at
a site when (B1) every quantized symbol has order with values in [−100, 100], (B2) every Sobolev order on which an
item is applied has values in [−100, 100], (B3) every N in (e) and in [[lem:ii-a-8-5]] (b) is at most 100, (B4) every
product in (e), (f) has at most six quantizations, and (B5) each use of (f) has the form required there.

**Lemma {#lem:fwd-derived}** (The sites of [[ch:s04]].) Each site of [[ch:s04]] uses the items of
[[prop:fwd-calculus]] as follows, and satisfies (B1)–(B5) under the stated condition.

(D1) [[lem:ii-a-8-5]] (a) at 𝗌: item (a), 𝗆 = 0, 𝗍 = 𝗌. Condition |s^±| ≤ 100.

(D2) [[lem:ii-a-8-5]] (b) at (𝗌, 𝗌_0): (e), three factors, 𝗍 = s_0⁻, N = max(0, ⌈s⁺ − s_0⁻⌉). Condition |s_0⁻| ≤ 100,
s⁺ − s_0⁻ ≤ 100.

(D3) [[lem:ii-a-8-6]] at (𝗌, m, N): (D1) at 𝗌 − m and (D2) at (𝗌 − m, −N − m). Condition |𝗌 − m|, |N + m|,
s⁺ + N ≤ 100.

(D4) [[thm:ii-a1-3-1]] at (m, 𝗌, N), with J′ = ⌈2(s⁺ + N)⌉ steps of ½: (a) for Op(q) (order −m) and for the symbol of
order −1 in E_A; (b) for Op(q)Op(ℓ_f) − Op(qℓ_f) (orders −m, m); (e) for G_(i+1)Op(q)(I − G_(i+2))L and
G_(i+1)E_A(I − G_(i+2)), at most four factors, N ≤ s⁺ + N + |m| + 1, at 𝗍 = −N − |m|; (D1) for the a_j; (D3) (a) at
(−N, m, N). Symbol orders in [−|m| − 1, |m|]; Sobolev orders 𝗌 − j/2 − ½, 𝗌 − j/2 − m, j ≤ J′, in
[s⁻ − s⁺ − N − |m| − 2, s⁺ + |m|]. Condition s⁺ + N + |m| + 2 ≤ 100 and s⁺ − s⁻ + N + |m| + 2 ≤ 100.

(D5) [[thm:ii-a1-5-4]] at (m, 𝗌, N), with [[prop:ii-a1-5-3]], [[lem:ii-a1-4-1]], [[lem:ii-a1-4-2]], [[lem:ii-a1-2-6]]:
τ := max(1, s⁺ + N), 𝗌_j ∈ [s⁻ − τ, s⁺], σ_* := max(|s⁻ − τ|, |s⁺|), K′ := ⌈σ_*⌉ + m + 2. Symbols ǎ (order
𝗌_j − (m − 1)/2), b_ε, e_ε (𝗌_j + δ), b_ε², H_ℓ(ǎ²), φ_0b_ε²φ_0 (2𝗌_j + 2δ), ℓ_f (m), z_ε, λ_+, λ_+z_ε, τ_t,
localisers, and in the parametrix step q = χ̃ab⁻¹ (−𝗌_j): orders in [−2σ_* − m − 1, 2σ_* + m + 1]. Sobolev orders
𝗌_j − κ, 𝗌_j − ½ + δ_0, 𝗌_j − m + 1, ±(m − 1)/2, −N, −N − m, −δ, K′, and those of the parametrix iteration from 𝗌_j
down to −N − σ_* − 1: all in [−σ_* − N − m − 2, K′]. (e): Φ_0L(I − Φ), Φ_0T_t(I − Φ), Φ_0T_tL(I − Φ) and those of the
parametrix step, at most four factors, N ≤ s⁺ + N + σ_* + m + 2. (f): the expressions (F1)–(F4) of [[lem:fwd-box]],
at most five factors. With (D4) at (m, 𝗌, N) and (D3) (a) at (−N, m, N). Condition 2σ_* + m + 1 ≤ 100,
σ_* + N + m + 2 ≤ 100, K′ ≤ 100, s⁺ + N + σ_* + m + 2 ≤ 100.

(D6) [[prop:ii-a-9-1]] at (m, 𝗌, N): (D4) at (m, 𝗌, N), (D3) at (𝗌, m, N) and (−N, m, N). (D7) [[prop:ii-a-9-2]]:
(D5) at (m, 𝗌, N), (D3) (a) at (−N, m, N), and 2. (D8) [[prop:ii-a-9-6]] at (𝗌, 𝗌_0): (D1) at 𝗌, (D2) at (𝗌, 𝗌_0).
(D9) [[cor:ii-a-9-7]] at (𝗍, m): (D8) at (𝗍 − m, 𝗍 − m). (D10) [[prop:ii-a-9-8]] at (𝗌, m, N): (D8) at
(𝗌 − m, −N − m), (D6), (D9) at (−N, m). (D11) [[prop:ii-a-9-9]] at (𝗌, m, N): (D8) at (𝗌 − m + 1, −N − m), (D7),
(D9) at (−N, m). Conditions: those of the sites invoked.

[[lem:ii-a-8-4]], [[lem:ii-a1-1-1]], [[lem:ii-a1-1-2]], [[lem:ii-a1-2-3]], [[lem:ii-a1-2-5]], [[lem:ii-a-8-7]] and
[[lem:ii-a-9-5]] concern smooth operators or functions, or have explicit regularity, and are not sites. No index of
these results depends on k, on the auxiliary operators, on the cut-offs or on the finite sets of operators.

*Proof.* The lists are read from the proofs cited: for (D4) the steps *One step*, *Localisation* and *Iteration* of
[[thm:ii-a1-3-1]] with 𝗋 = 0, 𝗋′ = 𝗌 − j/2, δ = ½; for (D5) the steps 0–3 of [[lem:ii-a1-4-1]], the iteration of
[[lem:ii-a1-4-2]] over 𝗌_j = 𝗌 − τ + jκ with its parametrix step (q := χ̃ab⁻¹, B_0^((j)) of order 𝗌_j + δ in place
of L), the commutant, commutator and positivity paragraphs of [[prop:ii-a1-5-3]], and *The index* of
[[thm:ii-a1-5-4]], whose τ is max(1, s⁺ + N); for (D6)–(D11) the first sentences of their proofs, which take maxima.
The ranges follow from the orders listed, as 𝗌_j and 𝗌 − j/2 have values in [s⁻ − τ, s⁺], resp.
[s⁻ − s⁺ − N − 1, s⁺]. In (D2) the case (e) applies by [[sec:ii-a1-1-2]] (proof of [[prop:fwd-calculus]]). ∎

**Lemma {#lem:fwd-box}** (The sites of [[ch:s06]]–[[ch:s09]], and the orders that occur.) The sites of
[[ch:s06]]–[[ch:s09]] that enter D_0, the sites of [[ch:s04]] they invoke with their parameters, and their increments
are the following. The increment of a site is the number by which its own regularity requirement exceeds the index of
the items of [[prop:fwd-calculus]] and [[lem:ii-a-8-5]] that it applies; its index is the larger of that requirement
and the indices of the sites it invokes. [[ch:s08]] contains no site: its operators (the ι⁺-normal operator and its
Mellin family) have smooth coefficients, and no class C^((d_0;k)) occurs in it. In [[ch:s09]], [[sec:ii-f-6]]–
[[sec:ii-f-8]] apply [[thm:ii-a1-3-1]] and [[thm:ii-a1-5-4]] to the smooth operators P_+, P^ε_+ and P_0 only, and
[[lem:s09-off-star]], [[lem:ii-f1-2-5]] are explicit (Seeley's extension); they are not sites.

(R) The radial estimates [[prop:ii-d-3-1]], [[prop:ii-d-3-2]], [[prop:ii-d-3-3]], [[prop:ii-d-3-5]], [[prop:ii-d-3-6]]
at constant (s, s_0), with [[lem:ii-d-2-1]]–[[lem:ii-d-2-5]] and the localised form of [[sec:ii-d-2]]: the pattern is
(D5) at (2, s, N′) with τ := s − s_0 ≤ s + N′ and constant orders; increment 1, as the symbols b_ε, e, j_ε, f_ε of the
pattern lie in C^(d_0−1) (they contain ρ⁻¹𝖧ρ and σ_1(Im_h P), with one derivative of the coefficients). (F3), (F4).

(Γ) The trapped set [[prop:ii-d-4-2]] at (s, s_0): commutants of orders in [s_0 − 3, s + 3] (as stated there), the
symbol ã of order 2s′ + 1 ≤ 2s + 1, products of order at most 2s + 7: symbol orders in [2s_0 − 7, 2s + 7]; Sobolev
orders in [−N′ − 3, |s| + 6]; (e) for G_1R_2^♭, G″R_2^♭, Φ_0(I − Φ′), Φ_0L(I − Φ′), (I − Φ′)^*Op(j_ε)Φ_0, at most four
factors, N ≤ s + N′ + 3; (f) as (F3), (F4) and [Φ_u, A_ε] (four factors). Increment 4: the symbols lie in C^(d_0−4)
([[lem:ii-d-4-1]], from ϕ^u ∈ C^(d_0−1), ϕ^s ∈ C^(d_0−2) of [[prop:ii-c1-3-4]]), and [[lem:ii-d-4-1]] asks d_0 ≥ 5.

(G) [[thm:ii-d-1-2]] at (𝗌_0, 𝗌): (D4) and (D5) at (2, 𝗍, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}; (R) at (12, 8) (horizon,
∂R_(ℐ⁺,in,+), ∂R_(∂K⁺,in)) and (−10, −13) (∂R_(∂K⁺,out), ∂R_(ℐ⁺,out)); (Γ) at (11, 8). Increment 0.

(I) [[lem:ii-d1-2-3]] at (𝗍, 𝗍_0, 𝔩) and [[lem:ii-d1-2-5]]: (R), resp. (Γ), at (𝗍, 𝗍_0) for the systems L^(k), whose
coefficients keep d_0 e3b-derivatives ([[lem:ii-d1-2-1]]); (D1) at 𝗍_0 − 2; (D2) at (𝗍 − 1 + 𝔩, 𝗍_0 − 2); (D3) (b) at
(𝗍 + 1 + 𝔩, 2, −𝗍_0). Increment 0. (Tm) [[lem:ii-d1-2-4]]: (D8) at (𝗍 + 1 + 𝔩, 𝗍_0) and (𝗍_0 − 2, 𝗍_0 − 2), (D9) at
(𝗍_0, 2); increment 2 (d_0 ≥ d_1 + 2). Used at (12, 8, 0), (11, 8, 1), (−10, −13, 0) by [[prop:ii-d1-3-2]],
[[prop:ii-d1-4-2]], [[prop:ii-d1-5-2]], [[prop:ii-d1-6-2]].

(B) [[thm:ii-d1-1-1]] at (𝗌_0, 𝗌): (G); (D6) and (D7) at (2, 𝗍, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}; (I), (Tm) at the three triples
above; (D10) and (D11) at (𝗍, 2, N′), 𝗍 ∈ {𝗌, 𝗌 + 1}. Increment 0.

(Sl) [[lem:ii-e-3-3]] (a) at slab orders (𝗌_0, 𝗌), (b) at constants (s_0, s): (D4), (D5) at (2, 𝗌, −s_0⁻) and
[[prop:ii-e-3-2]] at the values near R, which is (R) with increment 2 (h̃_F ∈ C^(d_0−2), [[lem:ii-e-3-1]]).

(Sv) [[prop:ii-e-3-4]] at a slab order 𝗌 and s′: (i) is (Sl) (a) at the constants (s′, 2); (ii) is (Sl) (a) at
(min(0, s⁻) − 1, 𝗌) (Step 2) and at (−m, 𝗌), m the least integer with m > 1 − s⁻ (Step 4), and (Sl) (b) at (0, m + 1)
(Step 3). The energy estimates need d_0 = 2 ([[lem:ii-e-2-5]], [[prop:ii-e-2-7]]). Increment 0.

(W) [[lem:ii-e-4-1]] (a) at (𝗌, m): (D1) at 𝗌 − m; (b) at 𝗌: (D8) at (𝗌, 𝗌). (Sb) [[prop:ii-e-4-3]] at 𝗌: (Sv) at 𝗌 for
the systems P^(j), with (i) at s′ = s⁻ − 1, and (W) (a) at (𝗌, 1). The uniqueness step of the induction is taken at
s′ = s⁻ − 1 ([[prop:ii-e-4-3]], [[prop:ii-e-5-6]] (a)).

(St) [[prop:ii-e-4-4]] at 𝗌: (Sb), and (W) (b) at 𝗌 + 1 and 𝗌 − 1; increment 2 (d_0 ≥ d_1 + 2).

(K) [[lem:ii-e-5-3]], [[prop:ii-e-5-4]] and [[prop:ii-e-5-6]] at 𝗌 and s′: as (Sl), (Sv), (Sb), (St), with no radial
set; [[prop:ii-e-5-6]] (b) has increment 2.

(E) [[thm:ii-e-6-1]] at (𝗌_0, 𝗌): (Sv) (i) and (K) (i) at s′ = s_0⁻ = −13, (Sb) and (St) at 𝗌, (B) at (𝗌_0, 𝗌), (K) at
𝗌 with s′ = −13. Increment 0.

(T) [[lem:ii-f1-2-8]] at 𝗍: (D9) at (𝗍, 2), (D1) at 𝗍 − 2. (U) [[lem:ii-f1-2-2]]: (Sv) (i) at s′. (F) [[lem:ii-f1-2-9]]:
(St) at 𝗌 + 2, and [[thm:ii-f-8-1]] for the smooth P_0. Increment 0.

The expressions to which (f) is applied, each with at most five quantizations in a product, and the reason why its
symbol t_α in every chart has no term above the order stated: (F1) [D_a, Op(ǎ)] and [[D_a, Op(ǎ)], Op(ǎ)],
D_a = Op(a)^* − Op(a^*), orders m + 𝗄 − 2 and m + 2𝗄 − 3: the terms of index 0 of D_a cancel ((c)), and ǎ is scalar, so
the terms of the commutators that are not of positive grade in each commutator vanish. (F2) [D_R, Ǎ], [D_I, Ǎ],
Ǎ = Op(ǎ)Φ_0, i[L_R, D_ǎǍ] and Ǎ^*[Ǎ, D_I] in [[prop:ii-a1-5-3]], order m + 𝗄 − 2, resp. 2𝗌 − 1: as (F1), with
φ_0ǎ = ǎ, and the terms of positive index of the symbol of Φ_0 vanish near supp ǎ, as each carries a ξ-derivative of
φ_0 (η enters the amplitude only through φ_0, [[lem:fwd-transport]]) and φ_0 = 1 there. (F3)
L_IǍ_ε^*Ǎ_ε + Ǎ_ε^*Ǎ_εL_I − Op(2ǎ_ε²ℓ_I) and i[L_R, Ǎ_ε^*Ǎ_ε] − Op(H_ℓ(ǎ_ε²)) in [[lem:ii-d-2-3]], order 2s − 1:
ǎ_ε is scalar, φ_0ǎ_ε = ǎ_ε, and ℓ_I, the principal symbol of L_I, is in every chart the part of order m − 1 of the
symbol of L_I: for smooth coefficients this is (S5), and both sides are the same polynomial in finitely many
derivatives of the coefficients and of the transition maps, so the identity persists in finite regularity
([[lem:ii-a1-2-2]]); likewise H_ℓ(ǎ_ε²) is the principal symbol of i[L_R, Ǎ_ε^*Ǎ_ε] ((d)).
(F4) Op(ρ^(−𝗍)φ_εz)Φ_z − Op(ρ^(−𝗍)φ_εzφ_z) and the products of [[lem:ii-d-2-5]], [[lem:ii-a1-2-6]], [[lem:ii-d-2-4]],
order one below the sum: φ_zz = z and the terms of index 0 agree ((b)). [Φ_u, A_ε] in [[prop:ii-d-4-2]] is (b), (d)
for scalar symbols.

At the parameters of the operator of [[thm:iii-i-5-3]], (B1)–(B5) hold at every site, and the indices satisfy:
every symbol order lies in [−71, 71], every Sobolev order in [−51, 38], every N of (e) is at most 63.

*Proof.* The lists are read from the proofs cited, for (Sb) and (K) with the uniqueness step at s′ = s⁻ − 1 as said
there. The parameters at which (D4), (D5) are used:
(G), (B): (2, 𝗌 + 1, 13) with s⁺ = 12, s⁻ = −9, τ = 25, σ_* = 34; (2, 𝗌, 13) with τ = 24, σ_* = 34. (Sv) at 𝗌:
Step 2 at (2, 𝗌, 11), τ = 22, σ_* = 32; Step 4, m = 12, at (2, 𝗌, 12), τ = 23, σ_* = 33; Step 3 at (2, 13, 0), σ_* = 13;
(i) at (2, 2, −s′) with s′ ∈ {−9, −11, −12, −13}, σ_* ≤ 13. (Sv) at 𝗌 + 2 (s⁺ = 13, s⁻ = −8): Step 2 at (2, 𝗌 + 2, 9),
τ = 22, σ_* = 30; Step 4, m = 10, τ = 23, σ_* = 31; Step 3 at (2, 11, 0). (K): as (Sv) at 𝗌. (R) at constant
s ∈ {12, −10, 13, 2, ≤ 13}: σ_* ≤ 13. So σ_* ≤ 34, and (D5) gives symbol orders in [−2·34 − 3, 2·34 + 3] =
[−71, 71], Sobolev orders in [−34 − 13 − 4, 34 + 4] = [−51, 38], and N ≤ 12 + 13 + 34 + 4 = 63; (D4) gives
N ≤ 12 + 13 + 3 = 28 and Sobolev orders down to −9 − 12 − 13 − 4 = −38. (Γ) at (11, 8): symbol orders in [9, 29],
Sobolev orders in [−16, 17], N ≤ 27. The (D2)-instances: (D8) at (13, 8), (−9, −13), (6, 6), (−15, −15) and (𝗋, 𝗋)
for 𝗋 ∈ {𝗌 − 2, 𝗌 − 1, 𝗌 + 1, 𝗌 + 3} (N ≤ 21, s_0⁻ ≥ −15); (D10), (D11) at (𝗍, 2, 13): (D8) at (𝗌 − 2, −15),
(𝗌 − 1, −15), (𝗌, −15) with N ≤ 26; (I): (D2) at (11, 6) and (−11, −15), N ≤ 5; (D3) at (𝗍, 2, 13),
𝗍 ∈ {𝗌, 𝗌 + 1}: N ≤ 25. All lie in the box, and the expressions have at most five quantizations. ∎

**Lemma {#lem:fwd-increments}** (The increments.) Every coefficient index entering D_0 is at most 𝔐(100) + 4.

*Proof.* By [[lem:fwd-box]] and [[lem:fwd-derived]], every index entering D_0 is a maximum over sites, and each site's
index is the larger of 𝔐(100) plus its increment and the indices of the sites it invokes, ending at the items of
[[prop:fwd-calculus]] (index M + 2 = 𝔐(100) for [[prop:ii-a1-2-4]], d_0 = 𝔐(100) for [[lem:ii-a-8-5]]) at orders that
satisfy (B1)–(B5). The increments, site by site: (D1)–(D4), (D6), (D8)–(D11) have increment 0 (they take maxima);
(D5) has 2 ([[thm:ii-a1-5-4]], *The index*: the flow box of [[lem:ii-a1-5-2]] has d_0 − 1 derivatives, the commutant
symbols d_0 − 2, so d_0 − 2 ≥ M′ + 2, that is d_0 ≥ 𝔐(100) + 2); (D7) has 0 beyond (D5); (R) has 1; (Γ) has 4; (Sl),
through [[prop:ii-e-3-2]], has 2; (Tm), (St) and [[prop:ii-e-5-6]] (b) have 2 (d_0 ≥ d_1 + 2, d_1 = 𝔐(100) being the
index of (D8)); (G), (I), (B), (Sv), (W), (Sb), (K), (E), (T), (U), (F) have 0. Increments do not add along a chain:
(D5), (R), (Γ) and (Sl) raise the regularity required of the symbols they quantize, and (Tm), (St) the regularity of the
coefficients of P − P_0 above that of (D8), each above the index of the items it applies, and the site above takes the
maximum. So, by induction over the sites, every index is at most 𝔐(100) + 4, attained only at (Γ). The energy
estimates need d_0 = 2 ([[lem:ii-e-2-5]], [[prop:ii-e-2-7]]) and [[lem:ii-d-4-1]] asks d_0 ≥ 5. ∎

*Proof of [[thm:fwd-loss]].* By [[lem:fwd-increments]], D_0 = max(d^E_0, d^S_0, d^T_0, d^U_0) ≤ 𝔐(100) + 4 =
20,104. By [[lem:fwd-orders]] and [[lem:fwd-tame]], d′ = 10, d″ = 11 and D_1 = 49. So by [[eq:fwd-split]]
d ≤ 20,104 + 49 + 10 + 11 + 1 + 5 = 20,180, and the theorem holds with any larger d, in particular with d = 20,180. ∎

The same value serves at every black hole parameter near b₀, where the forward solution operators are those of
[[cor:iii-h2-5-1]], built on [[thm:iii-h2-4-1]]. Below, (B1), (B4) and (B5) are the conditions of [[sec:iii-h2-0]];
the conditions (B1)–(B5) of [[sec:fwd-box]] are called the box conditions.

**Corollary {#cor:fwd-near-b0}** (The forward loss near b₀.) Let the order 𝗌 of (B4), which is the order of
[[lem:ii-f1-2-3]] built for 2L_(b₀) that the proof of [[thm:iii-i-5-3]] uses, be that of [[lem:fwd-orders]] (s_in = 11,
s_out = −10), and let β_+ ∈ (½, 3/2), β_I ∈ (β_+, 3/2), with the weights α_+ = β_+ − 5/2 and α_I = β_I − 2 of the proof
of [[thm:iii-i-5-3]]. Then [[thm:iii-h2-4-1]], in the form of [[rem:ii-f1-7-1]] with margin 1, holds with d = 20,175 at
every b ∈ B̄_1, and [[cor:iii-h2-5-1]] holds with d = 20,180 at every b ∈ B̄_*. In particular, at every base point with
black hole parameter b ∈ ℬ̄_*, the forward solution operators of [[lem:iii-j2-2-1]] (a) satisfy [[eq:iii-i-5-2]], in the
form of [[lem:iii-j2-2-1]] (a), with d = 20,180.

*Proof.* By its proof, the d of [[thm:iii-h2-4-1]] at b is the d that the proof of [[thm:ii-f1-1-1]] fixes when it is run
with P_0 := 2L_b, the order 𝗌 of (B4) (input (iii) of the proof of [[thm:iii-h2-4-1]]) and the results it cites applied
relative to 2L_b (inputs (i), (iv) and (v)); in the form of [[rem:ii-f1-7-1]] with d̄_ℵ = 1 it is

    d = D_0 + D_1 + d′ + d″ + 1,

with D_0, D_1, d′, d″ of [[eq:ii-f1-3-2]]–[[eq:ii-f1-3-3]] for these orders. [[thm:fwd-loss]] bounds the four numbers
at b₀. Its proof uses P_0 = 2L_(b₀) at three places, and at each the statement at b ∈ B̄_1 is the statement at b₀.

(1) *The orders.* [[lem:fwd-orders]] checks the thresholds of the construction of [[sec:ii-c-5-2]] for 2L_(b₀). At b the
order is not built again: by (B4), the order built for 2L_(b₀) is admissible for 2L_b with the same weights and margin.
So inf 𝗌 = −10, sup 𝗌 = 11, 𝗌_0 = 𝗌 − 3, s_u = −12 and N = N′ = 13 at every b, and d′ = 10, d″ = 11, which are functions
of 𝗌 alone ([[eq:fwd-dprime]]). [[lem:fwd-tame]] and [[lem:fwd-box]] use 𝗌 also through its constant values 11 near the
horizon, the trapped set, ∂R_(∂K⁺,in) and ∂R_(ℐ⁺,in,+), and −10 near ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out). The four sets over ∂K⁺
and ℐ⁺ are given in the fibre coordinates of [[sec:ii-c-5-2]] and [[def:ii-b-7-1]] over the boundary faces, the same for
every b, and 𝗌 is the same function. By (3) and (4) of [[def:ii-c-2-4]] for 2L_b, which (B4) gives, 𝗌 is constant over a
set {r ≤ r_Γ} that contains the horizon and the trapped set Γ_b of 2L_b; the constant is s_in = 11, as 𝗌 = s_in on Ω_♮
([[lem:ii-f1-2-3]]), which meets that set in its points with r < min(r_Γ, r_0 + 4). So the constant orders (s, s_0) at
which the radial and trapping estimates are used, (12, 8) at the horizon, ∂R_(ℐ⁺,in,+) and ∂R_(∂K⁺,in), (11, 8) at the
trapped set and (−10, −13) at ∂R_(∂K⁺,out) and ∂R_(ℐ⁺,out), are those at b₀.

(2) *The cited results.* D_1 and D_0 are maxima of the losses d and of the coefficient indices d_0 of [[thm:ii-e-6-1]],
[[prop:ii-e-3-4]], [[prop:ii-e-4-3]], [[prop:ii-e-4-4]] and [[lem:ii-f1-2-8]] at the orders of (1), and of
[[prop:ii-e-3-4]] (i) at s′ = s_u. At b these results are applied relative to 2L_b, at the same orders. The losses d are
the closed forms [[eq:fwd-dtilde]] that their proofs fix in terms of the orders and of N ([[lem:fwd-tame]]), and P_0
enters none of them; so D_1 = 49 at b. For D_0: [[prop:fwd-calculus]] and [[lem:fwd-derived]] concern the calculus of
[[ch:s04]] alone, symbols and Sobolev spaces of variable order on ρℬ, and involve no operator. In [[lem:fwd-box]], the
proof of [[thm:ii-f1-1-1]] at b applies the same sites in the same pattern: the radial estimates (R) at the radial sets
of 2L_b, the estimate (Γ) at Γ_b, which is normally hyperbolic with the data of (B1) and strongly trapping admissible
([[prop:iii-h2-1-1]]), and its other sites, from (G) to (F), at the orders of (1), with N′ = 13 and the operator order
m = 2. So their parameters, and the symbol orders, Sobolev orders, numbers N and numbers of quantizations computed from
them, are those at b₀, and the box conditions hold at every site. The increments of [[lem:fwd-increments]] count the
coefficient derivatives that the constructions inside the sites consume: the symbols of the radial and trapping
estimates, the stable and unstable manifolds of [[prop:ii-c1-3-4]], the extension h̃_F of [[lem:ii-e-3-1]], the flow box
of [[lem:ii-a1-5-2]] and the tame bounds with d_0 ≥ d_1 + 2. Each is fixed by the proof of its site, for every P
admissible relative to a smooth stationary P_0, and does not depend on P_0. The results that use 2L_b only as a smooth
operator, [[thm:iii-h2-3-1]] (with [[sec:ii-f-6]] run with 2L_(b₀) inside it) and [[thm:iii-h2-2-1]], are not sites, as
at b₀. So D_0 ≤ 𝔐(100) + 4 = 20,104 at b.

(3) *The two raisings.* The margin d̄_ℵ = 1 of [[rem:ii-f1-7-1]] is that with which 2L_b is 2-admissible
([[thm:iii-h2-2-1]]), as at b₀. So the d of [[thm:iii-h2-4-1]] is at most 20,104 + 49 + 10 + 11 + 1 = 20,175 at
every b ∈ B̄_1, and every larger d serves. The proof of [[cor:iii-h2-5-1]] is that of [[thm:iii-i-5-3]] with
P_0 := 2L_b, and it raises this d by 5 as at b₀: (iii) of that proof takes h ∈ 𝒳^(k+d+5) by [[cor:iii-i-5-2]], the 5
being the two b-derivatives of the metric in the coefficients of P − P_0 and the three of Sobolev embedding in
dimension five. In the tame form, read with the reference metric g_b, the difference g_(b₀,b,−S) − g_b has every
seminorm O(|b − b₀| + |S|) ([[lem:iii-i-3-6]]), so ‖P − 2L_b‖_((0;k+d)) ≤ C_k(|b − b₀| + |S| + ‖h‖_(𝒳^(k+d+5))),
and the constant term contributes C_k(|b − b₀| + |S|)‖f‖_(H^d) ≤ C_k‖f‖_(H^(k+d)), as C_k|S|‖f‖_(H^d) does at b₀.
So [[cor:iii-h2-5-1]] holds with d = 20,175 + 5 = 20,180 at every b ∈ B̄_*, its proof using b only through b ∈ B̄_1
and (B5), which is a condition on B̄_*. The last statement follows, as [[lem:iii-j2-2-1]] (a) takes the forward
solution operators at a base point with parameter b from [[cor:iii-h2-5-1]], and ℬ̄_* ⊂ B̄_*. ∎

**Remark {#rem:fwd-sharpness}** (Sharpness.) Only the term D_0 is crude. The counts of [[prop:fwd-calculus]] at T = 100
are at most 15,852 (item (f) with six quantizations), so the same proof gives D_0 ≤ 15,858 and d ≤ 15,934; the value
𝔐(100) = 20,100 keeps a margin. Counting each application of the calculus at its own orders (symbol orders at most 71,
Sobolev orders in [−51, 38], at most five quantizations, by [[lem:fwd-box]]) would lower D_0 further. The terms d′, d″
and D_1 are the exact values that the proofs of [[sec:ii-f1-3-1]], [[thm:ii-e-6-1]] and [[prop:ii-e-4-4]] fix for
these orders.

### Two long iterations and the loss of a round {#sec:ec-floor}

Among the iterations of the inventory of [[sec:iii-j2-3]], three constructions of [[ch:s21]]–[[ch:s23]] repeat one
step many times.

- *The levels.* Step 2 of the proof of [[thm:iii-i14-3-1]] climbs through admissible levels
  α_1 = β_0 < β_1 < ⋯ < β_K = α with β_(k+1) − β_k < α − 4, where α ∈ (4, 4 + ε_K] and α_1 ∈ (2, α − 2). Level k + 1
  takes R_qu as part of its forcing, R_q of second order and u the solution at level k ([[eq:iii-i14-3-3]]). No level
  equals 3: below 3 the levels are those of [[sec:iii-i8-1]], above 3 those of [[def:iii-i13-1-1]].
- *The transition face rounds below 3.* At a level β < 3 the step is [[lem:iii-i8-3-2]] with β in place of α. Its proof
  runs, while τ_i ≤ β − ε′, rounds that apply [[prop:iii-g4-5-1]] and put f̂^((i+1)) := f̂^((i)) − σL̂_b(σ)v_i, with
  τ_0 = 2 + ε_g − 2ε and τ_(i+1) = τ_i + ε_g − ε, ε_g = min(ε_Υ, ε_ind) ([[def:s21-eps-g]]).
- *The level-3 rounds above 3.* At a level β ∈ (3, 4) Step 4 of the proof of [[prop:iii-i13-2-1]] runs, while the
  tf-weight κ of the level-3 forcing is at most β − 2, rounds that apply [[prop:iii-g4-5-1]] with α_κ := κ, each
  leaving a remainder of tf-weight κ + ε_g − ε as the next forcing, from κ_3 = 1 + η_2 − 2ε.

In each round of the last two kinds, the solution v_i of [[prop:iii-g4-5-1]] is built from the inverse N_tf(L_b, ±1)⁻¹
of [[cor:iii-f1-3-4]], and the next forcing is obtained from it by the second-order operator L̂_b(σ).

**Lemma {#lem:ec-round-loss}** (The loss of one round.) In the accounting of [[def:ec-accounted-loss]]:

(a) a transition face round below 3, or a level-3 round above 3, is charged at least 2 + ℓ_tf, with ℓ_tf the lower
bound of [[lem:ec-closed-forms]] (d) for the loss of [[cor:iii-f1-3-4]] at the weights of the round;

(b) a round of the iteration at ι⁺ of [[prop:iii-i5-2-1]], which applies [[cor:iii-g2-4-3]] to the terms of the
forcing at one exponent ϰ_0 and removes the error by [[prop:iii-i1-3-1]], is charged at least 4 + d_ι(ϰ_0). If
3 < ℓ_I < 3.5 and λ_♯ ≤ Re ϰ_0 < 2 − δ_ι, this is at least 15.

*Proof.* (a) The round maps its forcing to v_i by a construction that composes N_tf(L_b, ±1)⁻¹, of loss at least
ℓ_tf, with maps of non-negative loss, and v_i to the next forcing by L̂_b(σ), of loss 2 ([[rem:ec-other-losses]]); the
next round takes that forcing as its input. By the composition rule the round is charged at least 2 + ℓ_tf.
(b) [[lem:iii-j2-2-1]] (g) charges [[cor:iii-g2-4-3]] the loss d_ι + 2 of [[thm:iii-g1-3-1]] (2) composed with L_b,
and [[prop:iii-i1-3-1]] a loss that includes one application of L̃, of loss max(2, d_BG) ≥ 2
([[rem:ec-other-losses]]); the next forcing is formed from their outputs. So a round is charged at least
4 + d_ι(ϰ_0). For 3 < ℓ_I < 3.5 and λ_♯ ≤ Re ϰ_0 < 2 − δ_ι, 1 < ℓ_I − Re ϰ_0 < 2, so d_ι(ϰ_0) = 11 by
[[lem:ec-closed-forms]] (e). ∎

**Lemma {#lem:ec-level-sum}** (Sums over the levels.) Let g ≥ 0 be non-decreasing on ℝ with g(y) − g(x) ≤ y − x for
x ≤ y, let c > 0, and let x_1 < x_2 < ⋯ < x_m with x_(j+1) − x_j < c for every j. Then

    c Σ_(j=1)^(m) g(x_j) ≥ ∫_(x_1)^(x_m) g − (c/2)(x_m − x_1).                                        {#eq:ec-level-sum}

*Proof.* Put h_j := x_(j+1) − x_j < c. On [x_j, x_(j+1)], g(x) ≤ g(x_j) + (x − x_j), so
∫_(x_j)^(x_(j+1)) g ≤ h_j g(x_j) + h_j²/2 ≤ c g(x_j) + c h_j/2. Summing over j < m, and adding c g(x_m) ≥ 0, gives
[[eq:ec-level-sum]], as Σ_(j<m) h_j = x_m − x_1. ∎

### The constant ε_Υ, and a lower bound for d {#sec:ec-gauge-gap}

The transition face rounds and the level-3 rounds of [[sec:ec-floor]] raise their weights by ε_g − ε, and ε_g =
min(ε_Υ, ε_ind) ([[def:s21-eps-g]]). The constant ε_Υ of [[sec:iii-d2-1]] is fixed below half the least distance
between distinct points of the set ℳ of the numbers Re ι + j in [−10, 10], with j ∈ ℤ and ι an indicial root of
(□^Υ_b)^(0) with |Re ι| ≤ 10. At the computational point that distance is set by two roots of high angular order, and
it is much smaller than δ_50. Throughout, z = 4·10⁻⁶ and, for l ≥ 1, d₂(l) and d₁(l) are the numbers d₂ and d₁ of
[[prop:np-10-52]] (i) at u = l + 1, so that ι^Υ_(sl,l+1) = l + 1 + d₂(l) and ι^Υ_(sl,l+2) = l + 2 + d₁(l); 𝔡₀ =
ι^Υ_(s0,2) − 2 is as in [[sec:ec-gap-sums]].

**Lemma {#lem:ec-gauge-gap}** (The least distance of ℳ.) At the computational point let 𝔡_ℳ be the least distance
between distinct points of ℳ. Then 𝔡_ℳ = d₁(8) − d₂(7) and

    2.9239·10⁻¹⁰ < 𝔡_ℳ < 2.92428·10⁻¹⁰.                                                                {#eq:ec-gauge-gap}

Hence every admissible choice of ε_Υ satisfies ε_Υ < 1.46214·10⁻¹⁰, and so ε_g < 1.46214·10⁻¹⁰, at every h; and ε_Υ =
1.4619·10⁻¹⁰ is an admissible choice.

*Proof.* *The points of ℳ.* By [[lem:iii-d-4-1]] the indicial roots of (□^Υ_b)^(0) that are not integers are 2 + 𝔡₀
and −1 − 𝔡₀ (type s0), and l + 1 + d₂(l), −l − d₂(l), l + 2 + d₁(l), −l − 1 − d₁(l) (type sl, l ≥ 1); all the others
are integers, among them 0. As 0 < 𝔡₀, d₂(l), d₁(l) < 1 ([[prop:np-10-52]] (i), [[eq:iii-d-4-2]]), those with real
part in [−10, 10] are 2 + 𝔡₀, −1 − 𝔡₀, l + 1 + d₂(l) for l ≤ 8, −l − d₂(l) for l ≤ 9, l + 2 + d₁(l) for l ≤ 7 and −l −
1 − d₁(l) for l ≤ 8. Put

    S₊ := {𝔡₀} ∪ {d₂(l) : 1 ≤ l ≤ 8} ∪ {d₁(l) : 1 ≤ l ≤ 7},     S₋ := {𝔡₀} ∪ {d₂(l) : 1 ≤ l ≤ 9} ∪ {d₁(l) : 1 ≤ l ≤ 8}.

Then ℳ consists of the integers in [−10, 10] and of the numbers n + x and n − y in [−10, 10] with n ∈ ℤ, x ∈ S₊ and y
∈ S₋; and for every integer n ∈ [−9, 10] and every y ∈ S₋ the number n − y lies in ℳ, being one of the roots −1 − 𝔡₀,
−l − d₂(l), −l − 1 − d₁(l) shifted by an integer. By the table below every element of S₋ lies in (9·10⁻⁸, 1.4·10⁻⁶).
So two points of ℳ near different integers are at distance more than ½, and two distinct points near one integer n are
at one of the distances |x − x′| (x, x′ ∈ S₊), |y − y′| (y, y′ ∈ S₋), x + y, x or y. As S₊ ⊂ S₋ and x + y > y, and as
the pair n − y, n − y′ occurs for every y, y′ ∈ S₋ (take n = 0),

    𝔡_ℳ = min(min S₋, min{|y − y′| : y, y′ ∈ S₋, y ≠ y′}).

*The enclosures.* By [[eq:s14-theta]], d₂(l) = c z(1 + θ₂) with c = l/(2(l + 1)(2l + 1)) and −z/(4l) − z/(2(2l + 1)²)
≤ θ₂ ≤ 0, and d₁(l) = c z(1 + θ₁) with c = (l + 2)/(2(l + 1)(2l + 3)) and −2z/(2l + 3)² ≤ θ₁ ≤ z/(4(l + 2)); and
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶ (the proof of [[prop:gap-sums]]). Rounding the lower bounds down and the upper
bounds up gives the intervals of the following table, listed in increasing order; the last column is the lower bound
of the next row minus the upper bound of this row, rounded down. Every entry of that column is positive, so the
eighteen numbers are distinct and the order is as listed.

| number | c | lower bound (10⁻⁷) | upper bound (10⁻⁷) | gap to the next (10⁻¹⁰) |
|---|---|---|---|---|
| d₂(9) | 9/380 | 0.9473683105 | 0.9473684211 | 98.3830 |
| d₂(8) | 4/153 | 1.0457514960 | 1.0457516340 | 120.9148 |
| d₂(7) | 7/240 | 1.1666664896 | 1.1666666667 | 2.9239 |
| d₁(8) | 5/171 | 1.1695906173 | 1.1695907603 | 149.0903 |
| d₂(6) | 3/91 | 1.3186810832 | 1.3186813187 | 4.8480 |
| d₁(7) | 9/272 | 1.3235293751 | 1.3235295589 | 191.6216 |
| d₂(5) | 5/132 | 1.5151511870 | 1.5151515152 | 8.6579 |
| d₁(6) | 4/105 | 1.5238094696 | 1.5238097143 | 253.9675 |
| d₂(4) | 2/45 | 1.7777772894 | 1.7777777778 | 17.0939 |
| d₁(5) | 7/156 | 1.7948717099 | 1.7948720513 | 347.9842 |
| d₂(3) | 3/56 | 2.1428563411 | 2.1428571429 | 38.9608 |
| d₁(4) | 3/55 | 2.1818180375 | 2.1818185455 | 484.8465 |
| d₂(2) | 1/15 | 2.6666651200 | 2.6666666667 | 111.1108 |
| d₁(3) | 5/72 | 2.7777775034 | 2.7777783334 | 555.5509 |
| d₂(1) | 1/12 | 3.3333292592 | 3.3333333334 | 476.1898 |
| d₁(2) | 2/21 | 3.8095231875 | 3.8095247620 | 2190.4733 |
| d₁(1) | 3/20 | 5.9999980800 | 6.0000020000 | 7333.3250 |
| 𝔡₀ | 1/3 | 13.3333270000 | 13.3333340000 | — |

For instance, for d₂(7) the bounds on θ₂ are −z/28 − z/450 ≤ θ₂ ≤ 0, so 7z/240 · (1 − 1.5175·10⁻⁷) ≤ d₂(7) ≤ 7z/240,
with 7z/240 = 1.1666666666…·10⁻⁷; and for d₁(8), −2z/361 ≤ θ₁ ≤ z/40, so 5z/171 · (1 − 2.3·10⁻⁸) ≤ d₁(8) ≤ 5z/171 · (1 +
10⁻⁷), with 5z/171 = 1.1695906432…·10⁻⁷.

The least element of S₋ is d₂(9) > 9.47·10⁻⁸. The least distance between two elements of S₋ is the least entry of the
last column (the elements being ordered as listed), which is that between d₂(7) and d₁(8), more than 2.9239·10⁻¹⁰;
every other entry exceeds 4.84·10⁻¹⁰. So 𝔡_ℳ = d₁(8) − d₂(7) > 2.9239·10⁻¹⁰, and from the table d₁(8) − d₂(7) <
(1.1695907603 − 1.1666664896)·10⁻⁷ < 2.92428·10⁻¹⁰. (The leading coefficients differ by 5/171 − 7/240 = 1/13680, and
z/13680 = 2.92397…·10⁻¹⁰.)

*The constant.* ε_Υ is fixed below ½𝔡_ℳ < 1.46214·10⁻¹⁰, and any positive number below ½𝔡_ℳ may be taken; as ½ ·
2.9239·10⁻¹⁰ > 1.4619·10⁻¹⁰, the value 1.4619·10⁻¹⁰ is admissible. ε_Υ is fixed by the gauge parameters (γ_Υ, e_Υ)
alone, through z, so the bound holds at every h. ∎

**Remark {#rem:ec-gauge-gap}** (The two gaps.) At the computational point ε_ind(10⁻⁶) = δ_50 > 1.94·10⁻⁸
([[cor:s14-eps-ind-point]]), so ε_Υ < δ_50/132 (as 132 · 1.46214·10⁻¹⁰ < 1.9301·10⁻⁸), and ε_g = ε_Υ whenever ε_ind
is taken at least ε_Υ, as it may be. In every case ε_g ≤ ε_Υ < 1.46214·10⁻¹⁰. The construction of [[ch:s21]] and
[[ch:s22]] advances its transition face and level-3 weights by ε_g − ε and asks ε_K < ε_Υ ([[def:iii-i10-1-3]]); both
long iterations of [[sec:ec-floor]] are therefore governed by ε_Υ, the separation of the shifted roots of the gauge
potential operator, and not by ε_ind.

**Proposition {#prop:ec-rounds}** (The number of rounds.) At the computational point, for every choice of ε_K, ε_+,
η_2, α, the levels and the losses ε, ε′ admissible for [[thm:iii-i14-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i13-2-1]], the transition face rounds at the levels below 3 and the level-3 rounds at the levels in (3, 4)
number together

    R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_K δ̂) > (1 − 5δ̂ − δ̄)/δ̂² > 4.6775 × 10¹⁹,     δ̂ := 1.46214·10⁻¹⁰.

The same bound holds at every h ∈ 𝖧, with the same (γ_Υ, e_Υ).

*Proof.* The weights satisfy 0 < ε_K < ε_Υ < δ̂ and ε_g ≤ ε_Υ: ε_K < ε_Υ is asked with the gap condition of
[[thm:settling]] ([[def:iii-i10-1-3]]), ε_g = min(ε_Υ, ε_ind) ([[def:s21-eps-g]]), and ε_Υ < ½𝔡_ℳ <
½ · 2.92428·10⁻¹⁰ = δ̂ ([[lem:ec-gauge-gap]]). Also η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄ ([[prop:np-10-52]] (iii)). The proof of
[[lem:iii-i8-3-2]] takes ε < ½ε_g, so ε < δ̂. The loss ε′ of [[lem:iii-i8-3-2]] satisfies ε′ ≤ ε: Steps 4–5 of its
proof give ũ the K⁺-weight α − 2 − ε′, while its conclusion at the output loss ε, at which the tame accounting takes it
([[sec:iii-j2-1]]), is the K⁺-weight α − 2 − ε, so a run of the proof that gives it has ε′ ≤ ε. So ε′ < δ̂. Each
round raises the tf-weight by ε_g − ε < δ̂, and the level spacing is below α − 4 ≤ ε_K. The count below uses the
increments only through their upper bound δ̂, so it holds as well if a round raises the weight by less than ε_g − ε,
which a construction may do, a forcing of tf-weight κ having every smaller tf-weight.

*Below 3.* At a level β ∈ (2, 3), τ_0 = 2 + ε_g − 2ε < 2 + δ̂ and τ_i < 2 + (i + 1)δ̂, and the rounds run for every i
with τ_i ≤ β − ε′, the τ_i being increasing; so their number is at least the number of i ≥ 0 with 2 + (i + 1)δ̂ ≤ β −
δ̂, which is at least g_1(β)/δ̂ with g_1(x) := (x − 2 − 2δ̂)_+. The levels in (2, 3) form a sequence b_1 < ⋯ < b_m
with b_1 = α_1 < α − 2 ≤ 2 + ε_K, and b_m > 3 − ε_K, because the next level exceeds 3 and lies within ε_K of b_m. By
[[lem:ec-level-sum]] with c = ε_K, and as g_1 vanishes below 2 + 2δ̂ > b_1,

    Σ_j g_1(b_j)/δ̂ ≥ (1/(ε_Kδ̂))(∫_(2+2δ̂)^(3−ε_K) (x − 2 − 2δ̂) dx − ε_K/2)
                   = (1/(ε_Kδ̂))((1 − ε_K − 2δ̂)²/2 − ε_K/2).

*Between 3 and 4.* At a level β ∈ (3, 4), κ_i := κ_3 + i(ε_g − ε) < 1 + δ̄ + iδ̂, as κ_3 = 1 + η_2 − 2ε < 1 + δ̄,
and the rounds run for every i with κ_i ≤ β − 2; their number is at least g_2(β)/δ̂ with g_2(x) := (x − 3 − δ̄)_+.
The levels in (3, 4) form a sequence c_1 < ⋯ < c_p with c_1 < 3 + ε_K (the previous level lies below 3 within ε_K)
and c_p > 4 − ε_K (the next level is at least 4, as β_(K−1) > 4, and lies within ε_K). As ε_K < δ̄, g_2 vanishes
below 3 + δ̄ > c_1, and by [[lem:ec-level-sum]]

    Σ_j g_2(c_j)/δ̂ ≥ (1/(ε_Kδ̂))((1 − ε_K − δ̄)²/2 − ε_K/2).

Adding, and using (1 − a)²/2 > ½ − a for a > 0, R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂); with ε_K < δ̂ this exceeds
(1 − 5δ̂ − δ̄)/δ̂². Here 5δ̂ + δ̄ < 7.32·10⁻¹⁰ + 1.95·10⁻⁸ < 2.1·10⁻⁸ and δ̂² = 2.13785…·10⁻²⁰ < 2.13786·10⁻²⁰, and
4.6775 · 2.13786 = 9.9998… < 10 · (1 − 2.1·10⁻⁸), so the quotient exceeds 4.6775·10¹⁹. Nothing in the proof used h
beyond the bound ε_Υ < δ̂, which holds at every h as ε_Υ is fixed by (γ_Υ, e_Υ) alone ([[lem:ec-gauge-gap]]), and
ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)). ∎

**Theorem {#thm:loss-d}** (The loss d and the regularity N_NM.) Let d_acc be the accounted loss of
[[def:ec-accounted-loss]], and d_NM the loss with which the proof of [[thm:iii-k-3-2]] applies the Nash–Moser theorem
[[thm:ii-g-2-1]]: the largest of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of
[[lem:iii-k-2-3]] accounted by [[def:ec-accounted-loss]]. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with
d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:

(i) d_acc is composed, by the rules of [[def:ec-accounted-loss]], of elementary losses and of the numbers of steps of the
iterations of the inventory of [[sec:iii-j2-3]], among them the three of [[sec:ec-floor]], each round of those three and
of the iteration at ι⁺ of [[prop:iii-i5-2-1]] being charged at least the loss of [[lem:ec-round-loss]]; the elementary
losses are closed forms in the weights, the small numbers that the proofs choose, the thresholds ϑ_in, ϑ_ℋ, the
regularity orders s_c, the counts n(E, β) of the index sets and the order d_BG of the bounds of the background terms
([[lem:ec-closed-forms]], [[rem:ec-other-losses]]), except the loss of the forward solution operators, which is at most
20,180 at every base point ([[thm:fwd-loss]] at b₀, [[cor:fwd-near-b0]] at b ∈ ℬ̄_*);

(ii) at the computational point, for every admissible choice of the weights there,

    d_acc ≥ Σ_rounds (2 + ℓ_tf) ≥ 3R > 1.403 × 10²⁰,        N_NM ≥ 21d_acc + 6 > 2.946 × 10²¹,

with R the number of rounds of [[prop:ec-rounds]], the sum over those rounds, and ℓ_tf ≥ 1 the lower bound of
[[lem:ec-closed-forms]] (d) for the loss of [[cor:iii-f1-3-4]] at the weights of each round;

(iii) when the levels of [[thm:iii-i14-3-1]] are more than ½(α − 4) apart, d_acc is bounded from above by
[[prop:ec-upper]], explicitly in the numbers of steps of the long iterations, which [[lem:ec-counts]] counts, in the
losses of their single steps, and in finitely many further losses, each assigned to a finite composition.

The bounds (ii) are lower bounds for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold; for the index sets as the proofs construct them, (G) asks ε_K < μ_G ([[thm:is-gap]]), and the lower
bound rises to 3R > 1.2497 × 10²⁴ ([[cor:uc-two-offsets]]). The bound (iii) is explicit in the numbers of steps, which
[[lem:ec-counts]] bounds through the spacing of the levels, below ε_K, and in the further losses, which contain counts of
the index sets. At the computational point [[thm:uc-integer]] evaluates every number of steps and every such count: d_acc
and d_NM are at most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹.

*Proof.* [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d_acc by [[lem:iii-j2-1-2]], which gives the tame estimates
with any loss at least the accounted one; N_NM = 21d_NM + 6 is the regularity of [[thm:ii-g-2-1]] at the loss d_NM
([[eq:ii-g-2-5]]). *d_NM ≥ d_acc.* Hypothesis (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]], with the loss d_NM, of the
right inverse Zℛ(U) of the proof of [[thm:iii-k-3-2]], where ℛ(U) is that of [[lem:iii-k-2-3]] and the multiplication Z
loses nothing; so the loss of ℛ(U), the loss of [[eq:iii-j2-4-2]] for it, is one of the three whose largest is d_NM. By
the proof of [[lem:iii-k-2-3]], ℛ(U) is the construction of [[thm:iii-j2-4-2]] at the base point Ψ(U), with two more
terms, linear in the finite-dimensional boost and translation components, added to the forcing of Step 2 of the proof of
[[thm:iii-i14-3-1]] and entering its Steps 1 and 3 as terms of the same kind; and the construction of [[thm:iii-j2-4-2]]
applies that of [[thm:iii-j2-4-1]] to the right side and assembles U′ from its output by maps of non-negative loss (Step
0 of the proof of [[thm:iii-j1-2-1]]). The elementary losses do not depend on the base point ([[lem:iii-j2-2-1]]: only
its constants do). By [[def:ec-accounted-loss]], a further summand does not lower the largest of the losses of a sum, and
a further factor of non-negative loss does not lower the loss of a composition; so the loss of ℛ(U) is at least the
numbers assigned to both constructions, and d_NM ≥ d_acc. (i) is [[def:ec-accounted-loss]] with [[lem:ec-closed-forms]],
[[rem:ec-other-losses]], [[lem:ec-round-loss]], [[thm:fwd-loss]] and [[cor:fwd-near-b0]].

(ii) Level k + 1 of [[thm:iii-i14-3-1]] takes the solution of level k as input through R_qu, and at each level the
rounds of [[sec:ec-floor]] are composed one after another, each round's output being the next round's forcing, and
the level's solution being assembled from the outputs of all its rounds and from the inverse applied to the last
forcing. So all the rounds of all the levels lie on one chain of compositions, and by [[def:ec-accounted-loss]] and
[[lem:ec-round-loss]] (a), d_acc ≥ Σ_rounds(2 + ℓ_tf). By [[lem:ec-closed-forms]] (d), whose proof uses
[[lem:ec-theta-in]], ℓ_tf ≥ 1 at every round; so by [[prop:ec-rounds]], d_acc ≥ 3R > 3 · 4.6775 × 10¹⁹ = 1.40325 ×
10²⁰ > 1.403 × 10²⁰, and N_NM = 21d_NM + 6 ≥ 21d_acc + 6 > 21 · 1.403 × 10²⁰ = 2.9463 × 10²¹ > 2.946 × 10²¹. Every lower
bound for d_acc in this chapter holds for d_NM and N_NM as well, because d_NM ≥ d_acc and N_NM increases with d_NM.

(iii) is [[prop:ec-upper]]. ∎

### What the proof's formulas give for δ and λ1 {#sec:ec-delta}

**Proposition {#prop:ec-delta-cap}** (The thresholds δ and λ1.) In the proof of [[thm:settling]], let d be the loss
d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] (d ≥ d_acc, [[thm:loss-d]]), and let the Nash–Moser
threshold be ε_NM = θ_0^(−(8d+2)), with θ_0 as chosen in the proof of [[thm:ii-g-2-1]]. Let ε be the data threshold
of [[cor:s27-rate]], chosen, as in the proof of [[thm:iii-k-3-2]], with ε ≤ s̃ and C_(2d)ω̃(ε) < ε_NM, where C_(2d) is
the constant of [[lem:iii-k-2-2]] (d) at the order 2d, and ω̃ := ω_(2d+3) and s̃ := min(s_(2d+3), s_P) are the modulus
and the threshold with which (d) holds there (ω_(2d+3) and s_(2d+3) those of [[prop:iii-k-1-2]] (3) at the order 2d + 3,
and s_P that of [[lem:iii-k-2-2]] (d)), enlarged if necessary so that C_(2d) ≥ 1 and ω̃(t) ≥ t on [0, s̃]; and let
C_R ≥ 1 be the constant of [[cor:vii-2-3]]. Then δ = ½ε and λ1 satisfy

    λ1 < δ,     ω̃(2δ) ≤ 2^(−(32d+8)),     δ ≤ 2^(−(32d+9)),     log₁₀ δ < −(59/196)(32d + 9).

As d ≥ d_acc, the bound of [[thm:loss-d]] (ii) gives, at the computational point, log₁₀ δ < −1.351 × 10²¹.

*Proof.* Replacing C_(2d) by max(C_(2d), 1) and ω̃(t) by max(ω̃(t), t) keeps [[lem:iii-k-2-2]] (d) true,
and the modulus still tends to 0 with t, which is all that the proof of [[thm:iii-k-3-2]] uses of it; so these are
choices that proof allows. The proof of [[thm:ii-g-2-1]] chooses θ_0 ≥ 16η_0^(−2) with η_0 ≤ 1, so θ_0 ≥ 16 and
ε_NM ≤ 16^(−(8d+2)) = 2^(−(32d+8)). So ω̃(2δ) = ω̃(ε) < ε_NM/C_(2d) ≤ 2^(−(32d+8)), and as ε ≤ s̃,
ε ≤ ω̃(ε) ≤ 2^(−(32d+8)), that is, δ = ½ε ≤ 2^(−(32d+9)). The proof of [[thm:settling]] ([[sec:vii-4]]) takes λ1
with C_Rλ1 < ½ε = δ, so λ1 < δ/C_R ≤ δ. Next, 2^10 = 1.024·10³, so 2^196 = 2^190·2^6 = 1.024^19·10^57·64, and by the
binomial expansion, all of whose terms are positive, 1.024^19 > 1 + 19x + 171x² + 969x³ > 1.5678 > 100/64 with
x = 0.024; so 2^196 > 10^59 and log₁₀ 2 > 59/196, and log₁₀ δ ≤ −(32d + 9) log₁₀ 2 < −(59/196)(32d + 9). With
d ≥ d_acc > 1.403·10²⁰, (59/196)(32d + 9) > (59/196) · 32 · 1.403·10²⁰ = 1.35146…·10²¹ > 1.351·10²¹. ∎

The bounds hold whatever the other constants are, once each constant of an upper bound is taken at least 1, which
enlarging it allows. A lower bound for δ or λ1 would need lower bounds for θ_0^(−1), the inverse of ω̃ and 1/C_R,
that is, upper bounds for every constant of the proof that enters them; [[rem:ec-not-evaluated]] says where those
stop.

### An upper bound for the accounted loss {#sec:ec-upper}

This section bounds d_acc from above, at choices of the levels more than ½(α − 4) apart. The bound is explicit in the
numbers of steps of the long iterations, which it counts from above, and in the losses of their single steps; the
remaining steps of the construction enter through finitely many further losses, each finite and charged once per
level, once per step of the base or once in all. First, a rule for families whose loss differs in the two norms of
[[eq:iii-j2-1-1]], which shows how the background terms enter.

**Lemma {#lem:ec-split-loss}** (Families with a split loss.) Call a family (T_β), E → G, *tame with split loss* (a; c,
b), a, c, b ∈ ℕ₀, if for every k there is C_k with

    ‖T_β e‖_(G^k) ≤ C_k (‖e‖_(E^(k+a)) + ‖β‖_(k+c) ‖e‖_(E^b)),     β ∈ 𝔹, e ∈ E^∞.             {#eq:ec-split-loss}

Let δ_𝔹 ≤ 1. (a) Such a family is tame with loss max(a, c, b) in the sense of [[def:iii-j2-1-1]]. (b) If (T_β) has
split loss (a; c, b), (S_β), G → H, has split loss (a′; c′, b′), and d_0 ≥ b′ + c, then (S_βT_β) has split loss (a +
a′; max(c′, a′ + c), max(b, a + b′)). (c) Let T_1, …, T_m have split losses (a_i; c_i, b_i), and let d_0 ≥ Σ_i a_i +
max_i c_i + max_i b_i. Then T_m ⋯ T_1 is tame with loss

    Σ_i a_i + max_i (max(c_i, b_i) − a_i)_+,

and a sum of families with split losses (a_i; c_i, b_i) has split loss (max a_i; max c_i, max b_i). (d) Let X ∈ ℕ₀,
and let an expression be built by compositions and sums from families T_i with split losses (a_i; c_i, b_i), c_i,
b_i ≤ a_i + X. Let A be the number that the rules of [[def:ec-accounted-loss]] assign to the expression when each T_i
is charged a_i, and let d_0 ≥ A + 2X. Then the expression has a split loss (A; c, b) with c, b ≤ A + X, and so is
tame with loss A + X.

*Proof.* (a) The norms are non-decreasing in k, so ‖e‖_(k+a) ≤ ‖e‖_(k+d), ‖β‖_(k+c) ≤ ‖β‖_(k+d) and ‖e‖_b ≤ ‖e‖_d for
d := max(a, c, b). (b) By [[eq:ec-split-loss]] for S and then for T,

    ‖S_βT_βe‖_k ≤ C_k (‖T_βe‖_(k+a′) + ‖β‖_(k+c′) ‖T_βe‖_(b′))
               ≤ C_k (‖e‖_(k+a+a′) + ‖β‖_(k+a′+c) ‖e‖_b + ‖β‖_(k+c′) (‖e‖_(b′+a) + ‖β‖_(b′+c) ‖e‖_b)),

and ‖β‖_(b′+c) ≤ ‖β‖_(d_0) < 1 and ‖e‖_b, ‖e‖_(a+b′) ≤ ‖e‖_(max(b,a+b′)) give the split loss stated. (c) By (b) and
induction, T_m ⋯ T_1 has split loss (Σ_i a_i; max_i(c_i + Σ_(j>i) a_j), max_i(b_i + Σ_(j<i) a_j)), the hypotheses d_0
≥ b′ + c of the steps holding by that on d_0. Each of c_i + Σ_(j>i) a_j and b_i + Σ_(j<i) a_j is at most Σ_j a_j +
(max(c_i, b_i) − a_i)_+, and (a) gives the loss. Sums: as in [[lem:iii-j2-1-2]] (a). (d) By induction over the
expression. A family T_i has the property by hypothesis. The number assigned to a part of the expression is at most A,
the rules adding or taking the largest of non-negative numbers. Let the parts E_1, E_2 have split losses (A_1; c_1,
b_1), (A_2; c_2, b_2) with c_j, b_j ≤ A_j + X. Their sum has split loss (max(A_1, A_2); max(c_1, c_2), max(b_1, b_2))
by (c), and max(c_1, c_2), max(b_1, b_2) ≤ max(A_1, A_2) + X. For the composition E_2E_1, b_2 + c_1 ≤ A_1 + A_2 + 2X ≤
A + 2X ≤ d_0, so (b) gives the split loss (A_1 + A_2; max(c_2, A_2 + c_1), max(b_1, A_1 + b_2)), and both maxima are
at most A_1 + A_2 + X. At the top, (a) gives the loss max(A, c, b) ≤ A + X. ∎

The families of [[lem:iii-j2-2-1]] fall into this frame. A linear map independent of β bounded E^(k+m) → G^k has split
loss (m; 0, 0) ([[lem:iii-j2-1-2]] (d)). The forward solution operators have split loss (d_F; d_F, d_F), d_F the loss d
of [[thm:iii-i-5-3]] and of [[cor:iii-h2-5-1]] ([[eq:iii-i-5-2]]), at most 20,180 ([[thm:fwd-loss]],
[[cor:fwd-near-b0]]), at the backgrounds h, h + h^(−1)(S) and h + h_tot(p⃗). At h̃ = h + h_rem(q) + h_tot(p⃗), where
‖h̃‖_(𝒳^m) is bounded through ‖q‖_(𝒬^(m+3)), they have split loss (d_F; d_F + 3, d_F), and so (d_F + 3; d_F + 3,
d_F + 3), the charge of [[lem:cs-elem]] (e). The background terms of [[lem:iii-j2-2-1]] (b), and the operator L̃ of
[[lem:iii-j2-2-1]] (g) where its coefficients depend on h, have split loss (2; d_BG, d_BG), d_BG the order in the
background of their bound ‖Au‖_k ≤ C_k(‖u‖_(k+2) + ‖β‖_(k+d_BG)‖u‖_(d_BG)); in the sense of [[def:iii-j2-1-1]] they are
tame with loss max(2, d_BG), the charge of [[rem:ec-other-losses]]. A finite-rank map e ↦ Σ_i (ℓ_βe)_i v^i
with |ℓ_βe| ≤ C‖e‖_(d_ℓ) and fixed sections v^i, as the rows and the coefficient maps of the construction are
([[lem:iii-j2-2-1]] (c)), has split loss (d_ℓ; 0, d_ℓ). So every family other than the background terms has c, b ≤ a, and
the background terms have c, b ≤ 2 + (d_BG − 2)_+. By (d) with X := (d_BG − 2)_+, the excess over 2 need only be paid
once: an expression built by compositions and sums from these families, in which every background term is charged 2 and
every other family its loss, is tame with the number so assigned plus (d_BG − 2)_+, whatever the number of background
terms in it, once d_0 is at least that number plus 2(d_BG − 2)_+, which [[lem:iii-j2-2-1]], taking d_0 large, allows. The
fixed operators L_b, L̂_b(σ) and L̃_b at the background 0, which alone enter the rounds and windows of the long
iterations, have split loss (2; 0, 0), so the excess does not enter those iterations either way.

**Lemma {#lem:ec-iota-gap}** (The gaps of the index sets at ι⁺.) The index set ℰ^ι_ind of [[thm:iii-g2-4-2]]
([[eq:iii-g2-4-4]]) satisfies ε^ι_ind := min Re ℰ^ι_ind ≥ ε_Υ, and the number η_0 of [[def:iii-i10-1-1]] satisfies η_0
≥ ε_Υ.

*Proof.* By the proof of [[thm:iii-g2-4-2]] (its paragraph on the ι⁺-order of the remainder near K⁺ ∩ ι⁺), ℰ^ι_ind
collects the index sets of the corrections of the states of [[ch:s13]] and [[ch:s15]] relative to their leading terms,
the set 2 + ℕ₀, and (2, 1) when ϰ = 1. The first have least real part at least ε_Υ: this is the convention of
[[sec:iii-d2-1]] for ℰ_ind, kept in [[ch:s15]] for the states of L_b, and [[sec:iii-g4-1]] and [[lem:iii-g4-4-3]]
state it for the corrections of the states; the others have real part at least 2. So ε^ι_ind ≥ min(ε_Υ, 2) = ε_Υ. The
increments of [[def:iii-i10-1-1]] are π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}, the first being the index sets of the corrections of
the states ([[sec:iii-i10-1]]), of least real part at least ε_Υ; so η_0 ≥ min(ε_Υ, ε^ι_ind, 1) = ε_Υ. ∎

The loss of the inverse of the transition face model enters every round of the long iterations. Its incoming
threshold is non-negative in every fibre inner product ([[lem:ec-theta-in]]); in one inner product it is 0, and this
fixes the loss up to the regularity order.

**Lemma {#lem:ec-theta-in-zero}** (The incoming threshold is 0.) Let γ_Υ, γ_C > 0, 0 < e_Υ < 1, 0 < e_C < 1 and
v_C > −1, and let the sets γ_Υ{1, 2, 1 − e_Υ} and (1 + v_C)γ_C{1, 2, 1 − e_C} be disjoint, as they are at the
computational point. Then at every point of ∂X the endomorphism A + S of [[lem:ec-theta-in]] (b) is diagonalisable,
with eigenvalues in

    {0, γ_Υ, 2γ_Υ, (1 − e_Υ)γ_Υ, (1 + v_C)γ_C, 2(1 + v_C)γ_C, (1 − e_C)(1 + v_C)γ_C},

0 among them, and there is a smooth fibre inner product h in which A + S is h-self-adjoint and non-negative at every
point of ∂X. In h, the incoming thresholds ϑ_in of (2L_b)^(σ) and of N_tf((2L_b)^(·), ±1) are 0.

*Proof.* By [[lem:ec-theta-in]] (b) it suffices to work at a point x with |x| > 0, where ρ = |x|⁻¹. Write ⟨·, ·⟩ for
ḡ⁻¹ and put Z := ḡ⁻¹ζ and c := ρ⁻¹c̄_C = dt̄ − v_C d|x| ([[sec:iii-f-2]]). As ḡ = −dt̄² + Σ_i (dx^i)²,
⟨dt̄, dt̄⟩ = −1, ⟨d|x|, d|x|⟩ = 1 and ⟨dt̄, d|x|⟩ = 0; so ζ = dt̄ + d|x| is null, ⟨ζ, dt̄⟩ = −1, ⟨c, ζ⟩ = −(1 + v_C),
⟨c, dt̄⟩ = −1, ι_Zḡ = ζ and ω(Z) = ⟨ω, ζ⟩. Let Ang ⊂ T*_x be the 3-dimensional space of the ω with ⟨ω, dt̄⟩ =
⟨ω, d|x|⟩ = 0; then T*_x = Ang ⊕ span(ζ, dt̄), and ⟨ω, ζ⟩ = ⟨ω, dt̄⟩ = ⟨ω, c⟩ = 0 for ω ∈ Ang.

By [[eq:ec-theta-in-l]], A + S = U_1V_1 + U_2V_2 = UV with U_1 := −ρ⁻¹Ē^C and U_2 := ζ ⊗_s · from T* to S²T*, V_1 :=
ι_ZḠ and V_2 := ρ⁻¹Ē^ΥḠ from S²T* to T*, U := (U_1 U_2) : T* ⊕ T* → S²T* and V := (V_1; V_2). First, V_1U_2 = 0:
ι_Z(ζ ⊗_s ω) = ½(⟨ζ, ζ⟩ω + ⟨ω, ζ⟩ζ) = ½⟨ω, ζ⟩ζ and tr(ζ ⊗_s ω) = ⟨ζ, ω⟩, so ι_ZḠ(ζ ⊗_s ω) = ½⟨ω, ζ⟩ζ −
½⟨ζ, ω⟩ι_Zḡ = 0. Next, with ḠĒ^Cω = γ_C(2c̄_C ⊗_s ω − e_C ḡ⟨c̄_C, ω⟩) ([[eq:iii-b-6-5]], as in the proof of
[[lem:iii-f-3-1]]), T^C := V_1U_1 is

    γ_C⁻¹T^Cω = −(⟨c, ζ⟩ω + ⟨ω, ζ⟩c − e_C⟨c, ω⟩ζ) = (1 + v_C)ω − ⟨ω, ζ⟩c + e_C⟨c, ω⟩ζ,

which is (1 + v_C)ω on Ang, (1 − e_C)(1 + v_C)ζ on ζ, and (1 + v_C)dt̄ + c − e_Cζ = 2(1 + v_C)dt̄ − (v_C + e_C)ζ on
dt̄, as c = (1 + v_C)dt̄ − v_Cζ. With Ē^ΥḠh = −γ_Υρ(2ι_Yh − e_Υ dt̄ tr h), Y := ḡ⁻¹dt̄ (as in the proof of
[[lem:iii-f-3-1]]), T^Υ := V_2U_2 is

    γ_Υ⁻¹T^Υω = −(⟨ζ, dt̄⟩ω + ⟨ω, dt̄⟩ζ − e_Υ⟨ζ, ω⟩dt̄) = ω − ⟨ω, dt̄⟩ζ + e_Υ⟨ω, ζ⟩dt̄,

which is ω on Ang, 2ζ on ζ, and (1 − e_Υ)dt̄ + ζ on dt̄. Let p_C(ν) := (ν − (1 + v_C)γ_C)(ν − (1 − e_C)(1 + v_C)γ_C)
(ν − 2(1 + v_C)γ_C) and p_Υ(ν) := (ν − γ_Υ)(ν − 2γ_Υ)(ν − (1 − e_Υ)γ_Υ). The factors of p_C(T^C) commute and preserve
Ang and span ζ; the first vanishes on Ang, the second on ζ, and the third maps dt̄ into span ζ. So p_C(T^C) vanishes
on Ang, ζ and dt̄, that is, p_C(T^C) = 0; in the same way p_Υ(T^Υ) = 0.

In the splitting T* ⊕ T*, VU has the blocks V_1U_1 = T^C, V_1U_2 = 0 (first row) and V_2U_1, V_2U_2 = T^Υ (second
row). Lower block-triangular maps form an algebra, and the diagonal blocks of f(VU) are f(T^C) and f(T^Υ) for every
polynomial f. So p_C(VU) has the blocks 0, 0 (first row) and Q_1, Q_2 (second row), and p_Υ(VU) the blocks Q_3, 0
(first row) and Q_4, 0 (second row), for some maps Q_1, …, Q_4; and the product p_Υ(VU)p_C(VU) has the blocks
Q_3·0 + 0·Q_1, Q_3·0 + 0·Q_2 and Q_4·0 + 0·Q_1, Q_4·0 + 0·Q_2, that is, it is 0. As (UV)^(n+1) = U(VU)^nV,
UVf(UV) = Uf(VU)V for every polynomial f, so m(UV) = 0 for m(ν) := ν p_Υ(ν)p_C(ν). The seven roots of m are
distinct, real and non-negative: the six other than 0 are positive, those of each of the two sets of the statement
are distinct as 0 < e_Υ, e_C < 1, and the two sets are disjoint. Let P_μ := Π_(μ′≠μ)(UV − μ′)/(μ − μ′) for each root
μ, the product over the other roots. Then Σ_μ P_μ = Id (the polynomial Σ_μ Π_(μ′≠μ)(ν − μ′)/(μ − μ′) has degree at
most 6 and equals 1 at the seven roots), (UV − μ)P_μ and P_μP_μ′ (μ ≠ μ′) are multiples of m(UV) = 0, and so
P_μ² = P_μ and A + S = UV = Σ_μ μP_μ: A + S is diagonalisable with eigenvalues among the roots of m. By
[[lem:ec-theta-in]] (b) its kernel is non-zero.

The roots of m do not depend on the point, and A + S depends smoothly on it, so the P_μ, polynomials in A + S, are
smooth. Fix a smooth fibre inner product h_0 and put h(u, v) := Σ_μ h_0(P_μu, P_μv), at ∂X, extended to a smooth fibre
inner product near ∂X (homogeneous of degree 0, and glued to h_0 by a partition of unity, a convex combination of
inner products being one). If h(u, u) = 0, every P_μu vanishes and u = Σ_μ P_μu = 0. As P_μ′P_μ = 0 for μ′ ≠ μ and
P_μ² = P_μ, h(P_μu, v) = h_0(P_μu, P_μv) = h(u, P_μv); so A + S = Σ_μ μP_μ is h-self-adjoint, Re_h(A + S) = A + S,
and h((A + S)u, u) = Σ_μ μ h_0(P_μu, P_μu) ≥ 0. By [[eq:ec-theta-in]], p_in − (S + S^(∗h)) = −2(A + S) at every point
of ∂X, whose largest eigenvalue is −2 times the least eigenvalue of A + S, that is, 0. So ϑ_in = 0. The transition
face model has the same endomorphism (the end of the proof of [[lem:ec-theta-in]] (b)), so the same holds for it. At
the computational point the two sets are {10⁻², 2·10⁻², 0.99·10⁻²} and 1.5·10⁶{1, 2, 1 − 1/102400}. ∎

**Lemma {#lem:ec-tf-loss}** (The loss of the transition face inverse.) Let β_sctf ∈ [1, 3/2) and β_ztf ∈ [−1, 0), and
let s ≥ 1 be the integer regularity order of the spaces of [[thm:i-c-4-3]] at which the proof of [[cor:iii-f1-3-4]]
applies [[cor:i-c-5-2]]; the tf-admissibility of [[prop:iii-f1-3-3]] does not depend on it ([[def:i-c-5-1]]), so any
such s may be taken, s = 1 among them ([[prop:uc-ltf]]). In the proof of [[cor:iii-f1-3-4]] take, at the incoming
radial sets, the fibre inner product of [[lem:ec-theta-in-zero]] ((O3) of [[def:i-a-admissible]] chooses the inner
products separately for each radial set) and the incoming order 𝗋_in := −¼. Then that proof gives [[eq:iii-f1-3-3]]
with the loss

    ℓ_tf(s) := max(1, s − 1),

and the lower bound ℓ_tf of [[lem:ec-closed-forms]] (d) is ℓ_tf(s) at every ϵ the proof takes. Take ℓ_scf := 3/2 − ε
in every application of [[prop:iii-g4-4-4]] and [[prop:iii-g4-5-1]] at the levels and in the rounds of the proofs of
[[lem:iii-i8-3-2]], [[prop:iii-i11-3-1]] and [[prop:iii-i13-2-1]]; then all of them apply [[cor:iii-f1-3-4]] with the
loss ℓ_tf(s).

*Proof.* [[thm:i-c-4-3]] takes s ∈ ℝ, and [[cor:i-c-5-2]] (a)–(b) holds at every s ([[def:i-c-5-1]]). The face tf
carries no event horizon, and the orders of [[lem:i-a-7-1]] that [[thm:i-c-4-3]] uses concern only the boundary face;
so the condition s_c > ½ + ϑ_ℋ of (O3) of [[def:i-a-admissible]], which concerns the radial sets ∂ℛ_± over the
horizon, does not enter. The proof of [[cor:iii-f1-3-4]] takes α_+ := 0, ϵ < ϵ_0 := ¼(3/2 − β_sctf) ≤ 1/8 (the number
it calls δ), 𝗋_out := β_sctf − 2 − ϵ/2 < −½ and the orders of [[lem:i-a-7-1]] at σ_* = ±1. By [[lem:ec-theta-in-zero]]
the incoming threshold of N_tf((2L_b)^(·), ±1) is 0 in the inner product chosen, so [[lem:i-a-7-1]] asks 𝗋_in > −½
and 𝗋_in ≥ 𝗋_out, which 𝗋_in = −¼ satisfies. Its order 𝗋 = 𝗋_out + (𝗋_in − 𝗋_out)Θχ_c takes the values 𝗋_out and 𝗋_in
and no value outside [𝗋_out, 𝗋_in] (extended with values in that interval, as in the proof of [[cor:ii-g1-4-2]]), so
sup 𝗋 = 𝗋_in and inf 𝗋 = 𝗋_out. So in [[lem:ii-g1-4-1]], sup 𝗋 − 𝗋_out = 7/4 − β_sctf + ϵ/2 lies in (¼, 13/16), as
7/4 − β_sctf ∈ (¼, ¾] and ϵ/2 < 1/16; its ceiling is 1, and 𝗋_out − inf 𝗋 = 0. As s ≥ 1, ℓ = max(1, s − 1) and ℓ̃ = 0
for every ϵ ∈ (0, ϵ_0). They do not depend on ϵ, so the last step of the proof, which replaces k by k + ℓ̃ and enlarges
ℓ until it does not depend on ϵ, gives [[eq:iii-f1-3-3]] with the loss ℓ + ℓ̃ = ℓ_tf(s) for ϵ < ϵ_0, and so for every
ϵ > 0, a larger ϵ giving a weaker statement. Near ztf the proof's spaces have the orders s − 2 + k and s + k, and
s − 2 < ℓ and s ≥ 0, so nothing is lost there. The expression of [[lem:ec-closed-forms]] (d) is ℓ + ℓ̃ at these orders.

Finally, Step 3.4′ of the proof of [[lem:iii-i8-3-2]] and Step 2 of the proof of [[prop:iii-i11-3-1]] take ℓ_scf :=
3/2 − ε; at the levels 2 and 3 the forcings have scf-weight 5/2 − ε ([[lem:iii-i11-2-2]]), which allows ℓ_scf := 3/2 − ε
there too. [[prop:iii-g4-5-1]] and [[thm:iii-g4-3-1]], through which [[prop:iii-g4-4-4]] applies the inverse, take
β_sctf = ℓ_scf, and 3/2 − ε ∈ [1, 3/2) as 0 < ε < ½. ∎

**Lemma {#lem:ec-round-charges}** (The losses of single rounds, from above.) In the accounting of
[[def:ec-accounted-loss]], let ℓ⁺_tf be the largest of the losses with which the construction applies
[[cor:iii-f1-3-4]] in the rounds of (a) and the applications of (b), which are finitely many; at the choices of
[[lem:ec-tf-loss]], ℓ⁺_tf = ℓ_tf(s) = max(1, s − 1), which is 1 at s = 1 ([[prop:uc-ltf]]). Then:

(a) a transition face round of the proof of [[lem:iii-i8-3-2]], and a level-3 round of the proof of
[[prop:iii-i13-2-1]] at a level β < 4, map the current forcing to the next one with a loss at most ℓ⁺_tf + 2; a level-3
round of the proof of [[prop:iii-i11-3-1]] at a level β > 4 does so with a loss at most ℓ⁺_tf + 4;

(b) one application of [[prop:iii-g4-4-4]] at level 1 or 2 of the proof of [[prop:iii-i11-3-1]], to the term of the
forcing at one exponent with all its logarithmic powers, maps that term to u and to the remainder [[eq:iii-g4-4-3]]
with a loss at most ℓ⁺_tf + 2;

(c) one window of Step 2 of the proofs of [[prop:iii-i5-2-1]], [[lem:iii-i8-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i10-3-1]] maps the current forcing to the next one with a loss at most d^max_ι + 2 + 2(⌊ℓ_I − 5/2⌋ + 1),
where d^max_ι is the largest value of d_ι(ϰ) of [[eq:ec-iota-loss]] on λ_♯ ≤ Re ϰ < 2. If 3 < ℓ_I < 3.5 and
δ_ι < 3.5 − ℓ_I, then d^max_ι ≤ 12, and the loss is at most d^max_ι + 4 ≤ 16.

*Proof.* We read the proofs at a finite b-regularity k and charge each map with its loss. Multiplication by smooth
functions, by powers of σ and by the cut-offs, the coefficients of a partial expansion, the stationary states and the
formal solutions with their coefficients, and holomorphic families evaluated or differentiated in a parameter on a
fixed circle cost nothing. Two facts are used. First, if R ∈ H^(k,b)_b near ztf and the contour shift of
[[lem:iii-g4-3-4]] is made, then the Mellin transform of R on the new line is N₀(λ)⁻¹Φ(λ), where Φ involves the
Mellin transform of PR at the order k − 2 and that of N₁R, shifted by 1, at the order k − 1; by (E1) and (E2) of
[[sec:iii-a-1-1]], N₀(λ)⁻¹ gains two orders jointly in λ and on 𝕊³, so R̃ and the residues lie at the order k: each
step of the expansions of [[thm:iii-g4-3-1]] and of Step 2 of the proof of [[prop:iii-g4-5-1]] costs nothing. Second,
N_tf does not depend on σ and commutes with σ∂_σ, so the loss of [[cor:iii-f1-3-4]] holds in the joint b-regularity in
(σ, r̂, ω).

(a) In Step 3.4′ of the proof of [[lem:iii-i8-3-2]], [[prop:iii-g4-5-1]] is applied with k₀ = 1 > ⌊ℓ_zf⌋ (ℓ_zf < 0),
so Step 1 of its proof is empty: f₁ is the forcing cut off, u₁ = N_tf⁻¹(|σ|^(−α)f₁) costs at most ℓ⁺_tf, the
expansion [[eq:iii-g4-5-5]] and u₂ cost nothing, and the remainder f₁ − L̂_b(σ)u₂ costs 2 more, L̂_b(σ) being of
second order and fixed. The next forcing f̂^((i+1)) = f̂^((i)) − σL̂_b(σ)v_i is σ times that remainder. So the round
costs at most ℓ⁺_tf + 2. At a level β ∈ (3, 4), Step 4 of the proof of [[prop:iii-i13-2-1]] applies [[prop:iii-g4-5-1]]
with ℓ_zf = ℓ_3 < 0 and the order 0 of the zf-index set, so again ⌊ℓ_zf⌋ < 0, Step 1 is empty, and the round costs at
most ℓ⁺_tf + 2. At β > 4, ℓ_3 ∈ (0, ε_K), and Step 1 runs for j = 0 only: v_0 solves 𝒩v_0 = ρ^(α−2)χ₃f^((0)) by
Mellin inversion on a line free of roots, which costs nothing (𝒩 is elliptic and dilation invariant, (E1)–(E2) of
[[sec:iii-a-1-1]]), and the terms e_0, which apply to U_0 the operators L̂_b(σ) − L̄̂(σ), ρ(ρ∂_ρ − 3/2 − S̄) and the
commutators with the cut-offs, cost at most 2; then f₁ costs at most 2, and the round at most ℓ⁺_tf + 4.

(b) In the proof of [[prop:iii-g4-4-4]], f₀ is a coefficient of the term (no loss), u_(tf,α) = N_tf⁻¹(ρ_ztf^(−α)f₀)
costs at most ℓ⁺_tf, its expansion [[eq:iii-g4-3-3]] costs nothing (the first fact), W_α and u_α are built from it and
from the states (no loss), and F_α = χ_tf ρ_tf^α f₀ − L̂_b(σ)u_α costs 2 more. Step 2 takes ∂^k_α at α₀, a Cauchy
integral over a small circle of holomorphic families bounded at each order, which costs nothing. So u costs at most
ℓ⁺_tf and the remainder at most ℓ⁺_tf + 2.

(c) In a window, [[cor:iii-g2-4-3]] is applied to the terms of the forcing F at each λ_0 of the window, in parallel.
By [[lem:iii-j2-2-1]] (g) its error, which is the terms of F at λ_0 minus L_bu_(λ_0), has the loss d_ι(λ_0) + 2. The
expansion at 𝓘⁺ of that error is removed by [[prop:iii-i1-3-1]]: its 𝓘⁺-exponents are those of ℰ^tot_(ι⁺,𝓘) + 2 to the
order ℓ_I + 1, with no ρ_I^(z+1)-term for Re z < 5/2 (Step 2 of the proof of [[prop:iii-i5-2-1]]; here z is an
exponent at 𝓘⁺). As ℰ^tot_(ι⁺,𝓘) = ⋃_(μ∈σ_Υ)(3/2 + μ, 0) has no logarithms, the terms to be removed sit at
z ∈ 5/2 + σ_Υ + ℕ₀ with Re z ≤ ℓ_I, all of logarithmic order 0, and they lie in the ⌊ℓ_I − 5/2⌋ + 1 windows
[5/2 + j, 7/2 + j), 0 ≤ j ≤ ⌊ℓ_I − 5/2⌋, of the proof of [[prop:iii-i1-3-1]]. That proof treats the terms of one window
in parallel, each by [[lem:iii-a-1-2]] and the fixed inverse (z − 3/2 − Ā)⁻¹, at no cost, and passes to the next
window the remainder f − L_b(χρ_I^z u^((z,0))), which costs 2 and creates only terms of logarithmic order 0 at z + j,
j ≥ 1. So u′_(λ_0) costs at most 2⌊ℓ_I − 5/2⌋ beyond the error. The next forcing is F − Σ_(λ_0) L_b(u_(λ_0) +
u′_(λ_0)), that is, the terms of F outside the window, unchanged, plus the errors minus L_bu′_(λ_0), which costs 2 more.
So a window costs at most d_ι(λ_0) + 2 + 2(⌊ℓ_I − 5/2⌋ + 1). The bound d^max_ι ≤ 12 is [[lem:ec-closed-forms]] (e) on
λ_♯ ≤ Re ϰ < 2 < ℓ_I, and ⌊ℓ_I − 5/2⌋ + 1 = 1 for 3 < ℓ_I < 3.5. ∎

**Lemma {#lem:ec-counts}** (The lengths of the long iterations, from above.) Make admissible choices of the weights of
[[thm:iii-i14-3-1]] and of the results it uses, and put

    Δτ := ε_g − ε,     Δβ := min_k (β_(k+1) − β_k),

with ε the loss of [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] (so ε < ½ε_g and Δτ > ½ε_g) and β_0 = α_1 < β_1 < ⋯ <
β_K = α the levels of Step 2 of the proof of [[thm:iii-i14-3-1]]. Let a♭_K ∈ (α_1, α − 2) be the K⁺-order of the
background h + h_rem(q) with which Step 1 of that proof applies [[prop:iii-i8-4-1]], [[lem:iii-i8-3-1]] and
[[lem:iii-i8-3-2]] (their number a_K at that background, whose K⁺-order is (α − 2)−; it is not the K⁺-order
a_K ≥ 4 + ε_K of h in Step 2). Let α_0 be the admissible level from which the proof of [[prop:iii-i8-4-1]] at α_1
starts, taken, as that proof allows, with α_1 − α_0 < a♭_K − 2, so that it has the single level step α_0 → α_1. Then:

(a) at most N_< := (3 − α_1)/Δβ of the levels β_1, …, β_K lie in (2, 3), at most N_> := (α − 3)/Δβ + 1 lie in
(3, α], and, if Δβ > ½(α − 4), at most two lie in (4, α];

(b) at a level β ∈ (2, 3) the transition face rounds number at most (β − 2)/Δτ + 1, and summed over the levels in
(2, 3) at most

    T_< := (1 + Δβ/2)²/(2ΔβΔτ) + N_<;

(c) at a level β ∈ (3, α] the level-3 rounds number at most (β − 3)/Δτ + 2, and at a level β ∈ (4, α] less than
1/Δτ + 2; summed over the levels in (3, α] they number at most

    T_> := (α − 3 + Δβ/2)²/(2ΔβΔτ) + 2N_>;

(d) at a level β ∈ (3, α], the applications of [[prop:iii-g4-4-4]] at level 1 act on separate terms of g_1 and none on
the output of another, every exponent of the remainder of an application at level 2 has real part at least ε_Υ above
the exponent it is made at, and at level 2 every exponent treated is reached from an exponent of g_2 through at most
(1 + η_2 − η_1)/ε_Υ remainders of earlier applications;

(e) every window loop (Step 2 of the proofs of [[prop:iii-i5-2-1]], [[lem:iii-i8-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i10-3-1]]) has at most W := (2 − λ_♯)/ε_Υ + 1 windows;

(f) in the base, the rounds of [[prop:iii-i5-2-1]] that Step 0 of the proof of [[lem:iii-i8-3-1]] runs number at most
N_b := 1/(a♭_K − 2) + 1, and the steps of [[prop:iii-i2-5-1]] that the start of its proof runs at most N_b + 1.

*Proof.* (a) The levels are increasing, at least Δβ apart, and β_1 ≥ α_1 + Δβ. Those in (2, 3) lie in [α_1 + Δβ, 3),
so there are at most (3 − α_1)/Δβ of them; those in (3, α] lie in an interval of length α − 3 closed at the top, so
there are at most (α − 3)/Δβ + 1; those in (4, α] lie in an interval of length α − 4 < 2Δβ.

(b) In Step 3.4′ of the proof of [[lem:iii-i8-3-2]] at the level β, τ_0 = 2 + ε_g − 2ε > 2 and τ_(i+1) = τ_i + Δτ, and
the rounds run for the i with τ_i ≤ β − ε′; so i ≤ (β − 2)/Δτ, and there are at most (β − 2)/Δτ + 1 of them. Let
b_1 < ⋯ < b_m be the levels in (2, 3). Then b_j < 3 − (m − j)Δβ, so

    Σ_j (b_j − 2) < Σ_(i=0)^(m−1) (1 − iΔβ) = m − Δβ m(m − 1)/2 ≤ (1 + Δβ/2)²/(2Δβ),

the last as the quadratic −(Δβ/2)(m − 1/Δβ − ½)² + (Δβ/2)(1/Δβ + ½)² in m is at most its maximum. Summing the bound on
the rounds over the m ≤ N_< levels gives T_<.

(c) At a level β ∈ (3, 4), Step 4 of the proof of [[prop:iii-i13-2-1]] starts at κ_3 = 1 + η_2 − 2ε > 1, raises κ by
Δτ per round, and runs while κ ≤ β − 2; so there are at most (β − 3)/Δτ + 1 rounds. At a level β ∈ (4, α], Step 4 of
the proof of [[prop:iii-i11-3-1]] fixes a number δ₄ > 0 (its δ) and takes α_κ = min(κ, 2 − δ₄); while κ < 2 − δ₄ each
round raises κ by at least Δτ, and the first round with κ ≥ 2 − δ₄ ends the loop; so there are at most
(2 − δ₄ − κ_3)/Δτ + 2 rounds, which is less than 1/Δτ + 2 ≤ (β − 3)/Δτ + 2, as κ_3 > 1. As in (b), for levels
c_1 < ⋯ < c_p in (3, α], Σ_j (c_j − 3) ≤ (α − 3 + Δβ/2)²/(2Δβ), and summing gives T_>.

(d) At level 1 (Step 2 of the proof of [[prop:iii-i11-3-1]]) the remainders have tf-exponents of real part at least
2 + ε_g > 2 + η_1, outside the window [2, 2 + η_1) of level 1; so no application acts on the output of another. At
level 2 (Step 3) the window is [1 + η_1, 2 + η_2), and the application at (α_0, k) leaves its remainder at the
exponents (α_0, k) + ℰ_ind and (4, k + 1) + ((0, 0) ∪ ℰ_ind) ([[eq:iii-g4-4-3]]), with min Re ℰ_ind ≥ ε_Υ; the second
lie above the window, and the first have real part at least Re α_0 + ε_Υ. So along a sequence of applications each of
which acts on a remainder of the previous one, the real parts increase by at least ε_Υ inside a window of length
1 + η_2 − η_1, and there are at most (1 + η_2 − η_1)/ε_Υ + 1 applications in it.

(e) In each window loop the least real part m_ι of the ι⁺-exponents to be treated starts at least at λ_♯, each window
raises it by at least ε^ι_ind ≥ ε_Υ ([[lem:ec-iota-gap]]; Step 2 of the proof of [[prop:iii-i5-2-1]]), and the loop
ends once m_ι ≥ α^♯_+, where α^♯_+ < 2 (in [[prop:iii-i10-3-1]], once no u-exponent below 2 is left). So there are at
most (2 − λ_♯)/ε_Υ + 1 windows.

(f) Each round of [[prop:iii-i5-2-1]] raises α′_K to min(α′_K + a♭_K − 2, α_K), from α′_K > 1 to α_K < 2; so there
are at most (α_K − 1)/(a♭_K − 2) + 1 < N_b rounds. Each step of [[prop:iii-i2-5-1]] raises α′_K by
min(a♭_K − 2, α_K − α′_K), from α′_K ≥ ½ to α_K < 1; so there are at most (α_K − ½)/(a♭_K − 2) + 1 < N_b + 1 steps. ∎

To state the bound, set apart the losses of the remaining steps. Let c(β_k) be the loss that [[def:ec-accounted-loss]]
assigns to the step of [[thm:iii-i14-3-1]] that passes from the level β_(k−1) to β_k ([[lem:iii-i8-3-2]] or
[[lem:iii-i13-2-2]], with the background terms of Step 2 of its proof) when every transition face round, level-3
round, application of [[prop:iii-g4-4-4]] at levels 1 and 2 and window of its iterations is charged 0. Let c_b be the
largest loss of one round of [[prop:iii-i5-2-1]] in the base with its windows charged 0, and c′_b the largest loss of
one step of [[prop:iii-i2-5-1]] there. Let c_0 be the largest loss assigned to the remaining steps of the larger of
the two constructions of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]: Step 0 of the proof of [[thm:iii-i14-3-1]] (the
forward solution); the rest of Step 1 (the base), with the windows of Steps 0 and 2 of the proof of [[lem:iii-i8-3-1]]
and of the level step α_0 → α_1 of [[prop:iii-i8-4-1]] charged 0; Steps 3, 4′ and 4, with all their steps charged
(they apply [[thm:iii-i11-4-1]] and [[thm:iii-i12-3-1]] at the top level, finitely many times); and for
[[thm:iii-j2-4-2]] the map U ↦ Φ(U) and Steps 1–3 of the proof of [[thm:iii-j1-2-1]]. Each of these numbers is finite,
being assigned by the rules of [[def:ec-accounted-loss]] to a composition of finitely many elementary families.

**Proposition {#prop:ec-upper}** (An upper bound for the accounted loss.) In the setting of [[lem:ec-counts]], with
Δβ > ½(α − 4),

    d_acc ≤ (ℓ⁺_tf + 2)(T_< + T_> + T_2) + 4(1/Δτ + 2) + r_ι W (N_< + N_> + N_b + 3)
            + Σ_(k=1)^K c(β_k) + N_b c_b + (N_b + 1) c′_b + c_0,                                        {#eq:ec-upper}

where T_2 := N_>((1 + η_2 − η_1)/ε_Υ + 2) and r_ι := d^max_ι + 2 + 2(⌊ℓ_I − 5/2⌋ + 1). If Δβ ≥ Δβ_0, Δτ ≥ Δτ_0 and
a♭_K − 2 ≥ Δβ_0 for some Δβ_0 ∈ (0, 1] and Δτ_0 > 0, then

    N_< ≤ 1/Δβ_0,     N_> ≤ (1 + ε_K)/Δβ_0 + 1,     N_b ≤ 1/Δβ_0 + 1,
    T_< ≤ (1 + Δβ_0/2)²/(2Δβ_0Δτ_0) + 1/Δβ_0,
    T_> ≤ (1 + ε_K + Δβ_0/2)²/(2Δβ_0Δτ_0) + 2(1 + ε_K)/Δβ_0 + 2.                                    {#eq:ec-upper-counts}

*Proof.* *The chain.* By [[def:ec-accounted-loss]], a composition is charged the sum and a sum or an assembly the
largest of the charges of its parts; so d_acc is the largest total charge along a chain of maps in which each takes
the output of the previous one as input. Splitting the charges into those of the rounds, applications and windows
counted in [[lem:ec-counts]] and all others, d_acc is at most the largest total of the first kind along a chain plus
the largest total of the second kind along a chain. The construction of [[thm:iii-i14-3-1]] is the forward solution
(Step 0), the base (Step 1), the level steps in the order of the levels, each taking the solution of the previous
level through R_qu ([[eq:iii-i14-3-3]]) and the a priori membership of [[lem:iii-i8-3-2]] or [[lem:iii-i13-2-2]], and
Steps 3, 4′ and 4; the finite-dimensional data p⃗′ enter through finite-rank maps ([[lem:iii-j2-1-2]] (c)), which add
no charge beyond those of the maps their functionals are applied to ([[lem:ec-split-loss]]). [[thm:iii-j2-4-2]]
composes this with U ↦ Φ(U) and with Steps 1–3 of the proof of [[thm:iii-j1-2-1]].

*Levels 1 and 2.* In a level step at β ∈ (3, α], let α_1′, …, α_n′ be the exponents at which level 2 applies
[[prop:iii-g4-4-4]], in an order of non-decreasing real part, in which the construction may treat them, as every
exponent of the remainder of an application has larger real part than the exponent it is made at ([[lem:ec-counts]]
(d)). The application at α_i′ maps the current forcing F to F − B_iF, B_i := L̂_b(σ)A_i, with A_iF the solution that
[[prop:iii-g4-4-4]] gives for the term of F at α_i′ with all its logarithmic powers; B_iF is that term minus the
remainder [[eq:iii-g4-4-3]]. So for j ≠ i the term of B_iF at α_j′ is minus that of the remainder, and A_jB_i = 0
unless α_j′ is an exponent of the remainder of the application at α_i′; call (i, j) a link then. Expanding the
products, the forcing passed on is

    (1 − B_n) ⋯ (1 − B_1)F = F + Σ (−1)^r B_(i_r) ⋯ B_(i_1)F,

the sum over the chains i_1 < ⋯ < i_r whose consecutive pairs are links, and the solution
Σ_j A_j(1 − B_(j−1)) ⋯ (1 − B_1)F is the sum of the A_jF and of the terms ±A_jB_(i_r) ⋯ B_(i_1)F over the chains for
which (i_r, j) is a link too. Each term is a composition along a chain, each map taking the output of the previous one
as input, and this is how [[def:ec-accounted-loss]] applies to level 2, whose applications take as input only the term
of the forcing at their exponent; the rules charge a sum the largest of its terms, so the applications at level 2 are
charged at most the largest total along a chain of links. The map is the same in either form, so this charge also
gives a loss with which [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold ([[lem:iii-j2-1-2]]). At level 1 there are no
links ([[lem:ec-counts]] (d)), and every chain has one application.

*The second kind.* Along a chain the charges other than those of the counted iterations are, by the definitions above,
at most Σ_k c(β_k) over the level steps, c_b per round of [[prop:iii-i5-2-1]] in the base and c′_b per step of
[[prop:iii-i2-5-1]] there, and c_0 for the rest, the background terms being among them with the charge max(2, d_BG) of
[[rem:ec-other-losses]]. By [[lem:ec-counts]] (f) this is the second line of [[eq:ec-upper]]. (Charging the background
terms 2 and adding (d_BG − 2)_+ once instead, as [[lem:ec-split-loss]] (d) allows, gives a loss with which
[[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold, bounded by the same expression with c(β), c_b, c′_b and c_0 lowered by
the excess of their background terms, plus (d_BG − 2)_+; it is not d_acc, which charges every application of a
background term max(2, d_BG).)

*The first kind.* A level step at β ∈ (2, 3) runs one window loop (Steps 1–2 of the proof of [[lem:iii-i8-3-2]]) and
its transition face rounds, one after another; a level step at β ∈ (3, α] runs one window loop (Step 2 of the proof of
[[prop:iii-i10-3-1]], through [[lem:iii-i13-2-2]]), the applications at level 1, those at level 2 and the level-3
rounds (Steps 2–4 of the proof of [[prop:iii-i11-3-1]], through [[prop:iii-i13-2-1]]). By [[lem:ec-counts]] (d), the
paragraph on levels 1 and 2 and [[lem:ec-round-charges]] (b), a chain passes through at most one application at level 1
and at most (1 + η_2 − η_1)/ε_Υ + 1 at level 2 in a level step, each charged at most ℓ⁺_tf + 2; this gives
T_2(ℓ⁺_tf + 2) over the levels in (3, α]. By [[lem:ec-counts]] (b), (c) and [[lem:ec-round-charges]] (a) the rounds
give at most (ℓ⁺_tf + 2)(T_< + T_>), plus 2 for each level-3 round at the at most two levels in (4, α], at most
2 · 2(1/Δτ + 2) in all. The window loops counted are one per level step, one per round of [[prop:iii-i5-2-1]] in the
base, and those of Steps 0 and 2 of the proof of [[lem:iii-i8-3-1]] and of the level step α_0 → α_1 of
[[prop:iii-i8-4-1]] in the base (the choice of α_0 in [[lem:ec-counts]] makes that level step one): at most
N_< + N_> + N_b + 3 of them, each of at most W windows charged at most r_ι ([[lem:ec-counts]] (e),
[[lem:ec-round-charges]] (c)). This is the first line of [[eq:ec-upper]].

*The counts.* N_< ≤ (3 − α_1)/Δβ ≤ 1/Δβ, as α_1 > 2; N_> ≤ (α − 3)/Δβ + 1 ≤ (1 + ε_K)/Δβ + 1, as α ≤ 4 + ε_K; and
N_b ≤ 1/(a♭_K − 2) + 1. For L ≥ 1 the function x ↦ (L + x/2)²/(2x) = L²/(2x) + L/2 + x/8 decreases on (0, 2L], and
Δβ < α − 4 ≤ ε_K < 2; so the bounds of [[lem:ec-counts]] (b), (c) decrease in Δβ and in Δτ, which gives
[[eq:ec-upper-counts]]. ∎

**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point ε_g ≤ ε_Υ <
1.46214·10⁻¹⁰ ([[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]]), and for the index sets as the proofs construct them 𝔡₀ and 𝔡₁
are increments of Λ ([[cor:uc-two-offsets]], [[rem:uc-offset-d0]]) and (G) holds exactly for ε_K < μ_G, where μ_G <
1.64160217198·10⁻¹⁴ ([[thm:is-gap]]). The levels are then less than μ_G apart, and the first line of [[eq:ec-upper]] is
of the order 3/(ε_Kε_g), the order of the lower bound 3R of [[prop:ec-rounds]]. [[prop:uc-explicit]] evaluates it at the
admissible choice of [[def:uc-choice]], with ε_K = 1.6416·10⁻¹⁴ and ε_g = ε_Υ = 1.4619·10⁻¹⁰: it is less than
1.2587·10²⁴, of which less than 4.30775·10²¹ comes from the window loops at ι⁺ (bounded there through ε^ι_ind = 𝔡₁,
[[lem:uc-gaps]]), and less than 1.0072 times the lower bound 3R > 1.2498·10²⁴ at the same choice ([[thm:uc-integer]]).
The losses c(β_k), c_b and c′_b of single steps enter the second line with the multiplicities K < 1.22077·10¹⁴ and N_b,
N_b + 1 < 6.10383·10¹³, and c_0 once; [[prop:cs-cstar]] bounds their largest value c_* by 6.4368·10³⁵.

**Remark {#rem:ec-upper-open}** (The inputs of the upper bound.) Four inputs separate [[prop:ec-upper]] from an integer;
at the computational point all four are bounded: (1), (2) and (4) are evaluated, and (3) through one number, c_*, which
[[prop:cs-cstar]] bounds. (1) ε_K, N_Λ, k̄_0 and l_*: (G) asks that no element of the set Λ of [[def:iii-i10-1-1]] have
real part in (2, 2 + ε_K] or in (3, 3 + ε_K], and that no λ + d_c0 or λ + d_c1, λ ∈ Λ, have real part in (2, 2 + ε_K].
[[prop:gap-sums]] and [[rem:gap-sums]] settle the three windows for ε_K < 5.019·10⁻⁸ on the part of Λ built from 2, 3,
λ_♯ and the offsets 𝔡₁, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁. With ℰ_ind as the proofs construct it, 𝔡₀ and 𝔡₁ are themselves
increments, and (G) holds exactly for ε_K < μ_G, 1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ ([[thm:is-gap]],
[[cor:uc-two-offsets]]); [[prop:is-count]] and [[cor:sp-lstar]] give 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3, J_* =
15,000,015 and the admissible l_* = 50, and [[prop:uc-explicit]] the numbers of levels, rounds, applications and windows
at an admissible choice. (2) ℓ⁺_tf = 1 at the choices of [[lem:ec-tf-loss]] with s = 1 ([[prop:uc-ltf]]). (3) The
single-step losses c(β), c_b, c′_b and c_0: each is a finite composition of the elementary losses of
[[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the forward loss, at most 20,180 ([[thm:fwd-loss]],
[[cor:fwd-near-b0]]), charged at each forward solution they apply; they contain the counts n(E, β) of the index sets
entering [[eq:ec-fourier-loss]], which [[lem:uc-n-iota]] bounds through N_Λ, k̄_0, l_* and J_*; c_0 contains, besides,
the iterations of Steps 4′ and 4 at the top level, each bounded as in [[lem:ec-counts]], and the loss of
[[thm:iii-j-2-4]], which its proof takes as the sum of the losses of its steps over the exponents of Λ ∩ {Re < 3 + ε_+}
([[lem:uc-phi-loss]]). Their largest value c_* enters [[thm:uc-integer]] with the coefficient 2.44153·10¹⁴;
[[prop:cs-cstar]] bounds it by 6.4368·10³⁵. (4) d_BG = 11 serves ([[prop:uc-dbg]]); it enters c(β), c_b, c′_b and c_0
through the charge max(2, d_BG). For d_NM, and so for N_NM, the losses of [[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]] are
at most 62N_Λ + 10 < 1.04·10¹⁵ ([[lem:uc-phi-loss]], [[lem:uc-lambda]]), and that of [[lem:iii-k-2-3]] satisfies
[[eq:ec-upper]] in the form of [[lem:uc-dr]], so that d_NM equals it ([[thm:uc-integer]]). Given ε_K, the explicit part
of [[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower bound of [[prop:ec-rounds]]; ℓ⁺_tf multiplies terms
of that order, c(β) enters at most N_< + N_> times, about 2/ε_K, and c_b and c′_b at most about 1/ε_K times each. All
these numbers depend on the point through z, which fixes ε_Υ ([[rem:ec-gauge-gap]]), and through the index sets.

### The inputs of the upper bound for the accounted loss {#sec:uc-close}

This section takes the inputs that [[prop:ec-upper]] leaves free, evaluates them at the computational point, and
assembles the bound. Two are fixed by general statements of this paper. The loss of the inverse of the transition face
model is 1 at the weights at which the construction may use it, so ℓ_tf = 1 ([[prop:uc-ltf]]); and the order of the
background terms may be taken to be d_BG = 11 ([[prop:uc-dbg]]). The others are fixed by the index sets that define the
set Λ of [[def:iii-i10-1-1]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹: the admissible ε_K of the gap condition
(G), the counts n(E, β) of the index sets entering the Fourier steps of the levels ([[lem:uc-fourier-count]]), and the
loss of the map Φ of [[thm:iii-j-2-4]], which governs the two other components of d_NM ([[lem:uc-phi-loss]]). Memberships
and least real parts of the index sets alone fix no admissible ε_K ([[prop:uc-no-eps]]); and if both offsets of the class
roots are increments of Λ, as they are for the index sets that the proofs construct, every admissible ε_K lies below
1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). [[sec:is]] lists the exponents of the index sets as constructed, and [[sec:sp]]
the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all simple. With them (G) holds exactly for ε_K < μ_G
([[thm:is-gap]]), and N_Λ, k̄_0, l_* and J_* are explicit ([[prop:is-count]], [[cor:sp-lstar]]). [[sec:uc-eval]] fixes an
admissible choice of the weights, evaluates every count of [[eq:ec-upper]] at it, and proves [[thm:uc-integer]]: d_acc
and d_NM are at most an integer D_acc < 1.57157·10⁵⁰, the largest single-step loss being below 6.4368·10³⁵
([[prop:cs-cstar]]), against the lower bound 1.2497·10²⁴; [[rem:uc-missing]] states what the bound rests on. Throughout
we work at the computational point of [[def:ec-point]], so z = 4·10⁻⁶ = 1/250000 and λ_♯ = 15099/10000, and 𝔡₀ = d_c0,
𝔡₁ = d_c1 are the offsets of [[sec:ec-gap-sums]].

#### The index sets of the gap condition {#sec:uc-index-sets}

The gap condition (G) of [[def:iii-i10-1-3]] quantifies over the set Λ and over the offsets 𝔡₀ and 𝔡₁ of the two class
roots ([[def:iii-i9-gap]]). By [[def:iii-i10-1-1]], Λ is the smallest set, closed under conjugation, that contains the
generators

- π_1ℰ_++, with ℰ_++ the least index set of [[eq:iii-i8-1-1]]: the closure of ℰ^♯_+ ∩ {Re < 2} under the addition of
  ℰ^ι_ind ∪ ℰ_ind ∪ ℰ_+, where ℰ^♯_+ is the set [[eq:iii-i1-3-2]] of [[prop:iii-i1-3-1]] with Ĕ_+ = ∅
  ([[sec:iii-i8-1]]);
- π_1𝒢, with 𝒢 = (2, 0) ∪ (2 + ℰ_ind) ([[eq:iii-i7-1-1]]);
- π_1ℰ^C_I, the index set at 𝓘⁺ of the class, subject to (2)–(3) of [[def:iii-c-3-1]] ([[def:iii-i-1-1]]);
- λ_♯ and 3;
- 2 + π_1ℰ_col, with ℰ_col = ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind)) + ℕ₀ ([[lem:iii-i11-1-1]]), a subset of
  π_1𝒢 + ℕ₀;

and that is closed under the addition of the increments

- π_1ℰ_ind, where ℰ_ind is the union of the index sets of [[prop:iii-d2-3-1]] and [[prop:iii-f3-2-2]]
  ([[sec:iii-i7-1]]), of [[prop:iii-d3-3-1]] (2) ([[sec:iii-i8-1]]), and of [[prop:iii-d3-3-1]] (1), (3), (4)–(7)
  and (2, 0) ([[sec:iii-i9-1]]), taken at b₀ and serving at every b near b₀ ((P3) of [[lem:iii-i15-1-1]]);
- π_1ℰ^ι_ind, the index set of [[thm:iii-g2-4-2]] ([[eq:iii-g2-4-4]]);
- 1.

Each of these sets enters the statements of this paper through memberships of the form u ∈ 𝒜^E (or a partially
polyhomogeneous space with the index set E) and a lower bound for its real parts, and it is fixed by a construction.
ℰ_ind is built in the proofs of [[prop:iii-d2-3-1]] ((F1) there), [[lem:iii-f3-2-1]] and [[lem:iii-d3-2-1]] by
[[lem:iii-a-1-4]], from the indicial roots of (□^Υ_b)^(0), which [[lem:iii-d-4-1]] and [[prop:np-10-52]] (i) give in
closed form, and from exponents of the right sides that are integers or such roots shifted by integers. ℰ^ι_ind
collects the index sets of the states of [[ch:s13]] and [[ch:s15]], 2 + ℕ₀ and (2, 1) (the proof of
[[thm:iii-g2-4-2]]); the physical states of [[ch:s15]] are built by [[lem:iii-a-1-4]] from the roots of L_b^(0)
([[prop:iii-f1-2-3]]), among them ι^C − 1 for the roots ι^C of the polynomials of [[prop:np-10-12]] (the proof of
[[prop:iii-f4-5-1]]). The least ℰ^C_I is generated from σ_Υ by (3) of [[def:iii-c-3-1]], and the least ℰ_++ by
[[eq:iii-i8-1-1]]. So the exponents of these sets below the real part 5 are algebraic numbers fixed by this paper;
[[sec:is]] lists them. A space with an index set E is contained in the space with any index set E′ ⊃ E, the
coefficients at the added exponents being 0.

**Proposition {#prop:uc-no-eps}** (Memberships fix no admissible ε_K.) Let t > 0 and

    E_t := ℰ_ind ∪ {(3 − λ_♯ + t + j, 0) : j ∈ ℕ₀}.

Then E_t is an index set with min Re E_t ≥ ε_Υ, every membership that [[prop:iii-d2-3-1]], [[prop:iii-d3-3-1]] and
[[prop:iii-f3-2-2]] assert with ℰ_ind holds with E_t in its place, the conditions [[eq:iii-i7-1-2]], [[eq:iii-i8-1-1]]
and (H3) on ℰ_+ being met by enlarging ℰ_+, and for the set Λ_t that [[def:iii-i10-1-1]] builds from E_t, (G) fails for
every ε_K ≥ t. So no positive number can be shown to be an admissible ε_K from information about ℰ_ind that consists of
such memberships and of the bound min Re ℰ_ind ≥ ε_Υ; the exponents of ℰ_ind themselves are needed. The proposition
concerns enlargements of ℰ_ind: enlarging an admissible index set, like decreasing ε_K, only lowers the admissible ε_K,
so it bounds neither the admissible ε_K of the index sets that the proofs construct nor d from above.

*Proof.* E_t is a union of two index sets, so it has finitely many exponents below each bound, finitely many
logarithms at each, and is closed under (z, k) ↦ (z + 1, k); its new exponents have real part at least
3 − λ_♯ = 1.4901 > ε_Υ. A membership with ℰ_ind implies the same membership with E_t ⊃ ℰ_ind. The conditions
[[eq:iii-i7-1-2]], [[eq:iii-i8-1-1]] and (H3) involve ℰ_ind only through lower bounds for ℰ_+ and for ℰ_++ ⊂ ℰ_+, which
an enlargement of ℰ_ind only strengthens ([[sec:iii-i8-1]]). The proof of [[lem:iii-i10-1-2]] (b), which uses of ℰ_ind
only that its exponents have positive real parts, shows that they are conditions on ℰ_+ alone, met by the least index
set that contains ℰ_+, 2 + E_t and ℰ_par + ℱ, with ℰ_par built from Λ_t, and that is closed under the addition of
ℰ^ι_ind ∪ E_t and of itself. In Λ_t, λ_♯ is a generator and 3 − λ_♯ + t ∈ π_1E_t is an increment, so 3 + t ∈ Λ_t. Its
real part lies in (3, 3 + ε_K] as soon as ε_K ≥ t, which (G) excludes. ∎

Enlargements of the same kind, by finitely many exponents of real parts in [ε_Υ, 1), each with its translates by ℕ₀
and with any logarithmic orders, raise the number of points of Λ below 3 + ε_+ and the bounds l_* and k̄_0 of
[[def:iii-i10-1-1]] beyond any given bound: each such exponent z gives the point λ_♯ + z < 3 of Λ, and the exponent
2 + z < 2λ_♯ of 𝒢 with its logarithmic order. So memberships and least real parts alone do not bound these numbers
either.

**Lemma {#lem:uc-two-offsets}** (Two class offsets near 3.) Let a := 1,109,655 and b := 31,682. Then

    1.6415·10⁻¹⁴ < λ_♯ + a𝔡₀ + b𝔡₁ − 3 < 1.6417·10⁻¹⁴.                                               {#eq:uc-two-offsets}

*Proof.* *The offsets.* 𝔡₀ = (9/4 + z)^(1/2) − 3/2 ([[sec:ec-gap-sums]]), and 9/4 + z = 562501/250000, so
𝔡₀ = (√562501 − 750)/500. By [[lem:iii-d-4-1]] and its proof, ι^Υ_(s1,2) = ½ + (¼ + s_(1,1))^(1/2), where s_(1,1) is
the smaller root of Q_1(s) = s² − (8 + z)s + 12 + 3z (κ = 3), whose discriminant is 16 + 4z + z² = D/250000² with
D := 1000001000001. So 4(¼ + s_(1,1)) = 17 + 2z − √D/125000 =: I, ι^Υ_(s1,2) = ½ + ½√I, and 𝔡₁ = (√I − 3)/2.

*The square roots.* Squaring the decimal numbers below gives

    750.0006666663703706337445² = 562500.99999999999999999990500…,
    750.0006666663703706337446² = 562501.00000000000000000005500…,
    1000000.500000374999812500² = 1000001000000.99999999999995312…,
    1000000.500000374999812501² = 1000001000001.00000000000195312…,

so √562501 and √D lie strictly between the two numbers squared. With 2z = 0.000008 and
1000000.500000374999812500/125000 = 8.0000040000029999985, the second pair gives

    9.000003999997000001499992 < I < 9.0000039999970000015,

and, as 3.0000006666660925929701631² = 9.00000399999700000149999177…, which is below the lower bound for I, and
3.0000006666660925929701645² = 9.00000399999700000150000017…, which is above the upper one, √I lies strictly between
3.0000006666660925929701631 and 3.0000006666660925929701645.

*The sum.* Hence

    1.333332740741267489·10⁻⁶ < 𝔡₀ < 1.3333327407412674892·10⁻⁶,
    3.3333304629648508155·10⁻⁷ < 𝔡₁ < 3.3333304629648508225·10⁻⁷,

and, multiplying the four bounds exactly,

    1.479539342427251175506295 < a𝔡₀ < 1.479539342427251175728226,
    0.0105606575727652403536671 < b𝔡₁ < 0.0105606575727652403758445.

Adding, a𝔡₀ + b𝔡₁ − 1.4901 lies between 1.64158599…·10⁻¹⁴ and 1.64161040…·10⁻¹⁴. As 3 − λ_♯ = 1.4901, this is
[[eq:uc-two-offsets]]. (Also a𝔡₀ + (b − 1)𝔡₁ < 1.4901, by 𝔡₁ > 3.3·10⁻⁷, so b is the least integer that works with
this a.) ∎

**Corollary {#cor:uc-two-offsets}** (The gap condition when both offsets are increments.) (a) Suppose that 𝔡₀ and 𝔡₁
lie in π_1(ℰ_ind ∪ ℰ^ι_ind), as they do for ℰ_ind as constructed ((b) and [[rem:uc-offset-d0]]). Then every ε_K with
which (G) holds satisfies ε_K < 1.6417·10⁻¹⁴. For every admissible choice of the weights, the number R of
[[prop:ec-rounds]] then satisfies R > 4.1659·10²³, so that d_NM ≥ d_acc > 1.2497·10²⁴ and
N_NM = 21d_NM + 6 > 2.624·10²⁵.

(b) For ℰ_ind as the proof of [[prop:iii-d2-3-1]] constructs it, 𝔡₀ and 𝔡₁ lie in π_1ℰ_ind. So the hypothesis of (a)
holds for the index sets as constructed, and for them every ε_K with which (G) holds is below 1.6417·10⁻¹⁴.

*Proof.* (a) λ := λ_♯ + a𝔡₀ + b𝔡₁, with a and b of [[lem:uc-two-offsets]], is obtained from the generator λ_♯ by
a + b additions of increments, so λ ∈ Λ, and Re λ − 3 < 1.6417·10⁻¹⁴ by [[eq:uc-two-offsets]]. If
ε_K ≥ 1.6417·10⁻¹⁴, then Re λ ∈ (3, 3 + ε_K], against (G). By [[prop:ec-rounds]],
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) with δ̂ = 1.46214·10⁻¹⁰ and δ̄ = 1.94137057·10⁻⁸, and the right side decreases in ε_K.
At ε_K = 1.6417·10⁻¹⁴ the numerator exceeds 1 − 1.98·10⁻⁸ > 0.99999998 and ε_Kδ̂ = 2.400395…·10⁻²⁴ < 2.4004·10⁻²⁴, so
R > 4.16597·10²³. By [[thm:loss-d]] (ii), d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴, and 21 · 1.2497·10²⁴ > 2.624·10²⁵.

(b) The step of the proof of [[prop:iii-d2-3-1]] that corrects the translations applies the fact (F1) of that proof
with k = 2. There [[lem:iii-a-1-4]] is applied with a weight α ∈ (2 − ε_Υ, 2), and the index set ℰ it gives contains
E(α), the smallest index set that contains the elements (ι, 0) of the boundary spectrum of ρ⁻²(□^Υ_b)^(0), of every
type, with Re ι > α. By [[lem:iii-d-4-1]], ι^Υ_(s0,2) = 2 + 𝔡₀ (type s0) and ι^Υ_(s1,2) = 2 + 𝔡₁ (type s1) are simple
roots, and their real parts exceed 2 > α. (F1) writes ℰ as (2, 0) ∪ (2 + ℰ_ind), and 2 + 𝔡₀ and 2 + 𝔡₁ differ from 2;
so (𝔡₀, 0) and (𝔡₁, 0) lie in that ℰ_ind, which is part of the union ℰ_ind of [[sec:uc-index-sets]]. ∎

**Remark {#rem:uc-offset-d0}** (The offset 𝔡₀ as an increment.) [[rem:gap-sums]] lets 𝔡₀ enter Λ through the increment
1 + 𝔡₀ only, and [[prop:gap-sums]] shows that the windows of (G) are then not met by the sums it considers for
ε_K < 5.019·10⁻⁸. For ℰ_ind as the proof of [[prop:iii-d2-3-1]] constructs it, 𝔡₀ and 𝔡₁ are exponents: (F1) there,
with k = 2, takes the boundary spectrum above a weight in (2 − ε_Υ, 2), at every type ([[cor:uc-two-offsets]] (b)). So
with ℰ_ind as constructed, (G) fails at every ε_K ≥ 1.6417·10⁻¹⁴ ([[cor:uc-two-offsets]]). Whether a smaller
admissible ℰ_ind omits 𝔡₀ is not decided by this paper; [[thm:is-d0]] reduces it to the vanishing of one family of
coefficients. The root ι^Υ_(s0,2) = 2 + 𝔡₀ of (□^Υ_b)^(0) lies above the weights in (0, ι^Υ_(s1,2)) at which
[[prop:iii-d2-3-1]] solves for the corrections of the states, and these corrections start at the order (2, 0), so a
smaller admissible ℰ_ind keeps the exponent 𝔡₀ wherever a term at that root has a nonzero coefficient. At b₀ the
operator commutes with the rotations, and the corrections of the states of types s1 and v1 do not meet the roots of
type s0. At a rotating b the metric couples the angular types at the order |x|⁻³ ([[eq:iii-d2-2-2]]), and ℰ_ind is one
index set serving at every b near b₀. So (G) at an ε_K ≥ 1.6417·10⁻¹⁴ needs a smaller admissible ℰ_ind ∪ ℰ^ι_ind that
omits 𝔡₀ or 𝔡₁; omitting 𝔡₀ means the vanishing of these coefficients at every b near b₀.

#### The loss of the inverse of the transition face model {#sec:uc-ltf}

**Proposition {#prop:uc-ltf}** (The loss of [[cor:iii-f1-3-4]] is 1.) Let β_sctf ∈ [1, 3/2) and β_ztf ∈ [−1, 0). The
proof of [[cor:iii-f1-3-4]] runs with the regularity s := 1, the weight α_+ := 0, the incoming order 𝗋_in := −¼ and, at
the incoming radial sets, the inner product of [[lem:ec-theta-in-zero]], and gives [[eq:iii-f1-3-3]] with ℓ = 1, for
every k ∈ ℕ₀ and every ϵ ∈ (0, ¼(3/2 − β_sctf)). So with these choices the loss of [[cor:iii-f1-3-4]] is 1, which is
the value of ℓ_tf in [[lem:ec-closed-forms]] (d), and its least possible value there. Every application of
[[cor:iii-f1-3-4]] in the construction of [[thm:iii-i14-3-1]] and of [[thm:iii-j1-2-1]] can be made with
β_sctf = 3/2 − ε, with 0 < ε < ¼; so ℓ_tf = 1 at all of them, and in [[prop:ec-upper]] and [[lem:ec-round-charges]]
ℓ⁺_tf = 1.

*Proof.* *The regularity.* [[prop:iii-f1-3-3]] gives the tf-admissibility of L_b^(·) with every weight in (0, 1], in
particular with β := −β_ztf. By [[def:i-c-5-1]], tf-admissibility does not depend on the choices of s, α_+ and the
orders, and [[cor:i-c-5-2]] (a)–(b) holds with s and α_+ as in [[thm:i-c-4-3]], which takes s and α_+ in ℝ and uses
the order pair of [[lem:i-a-7-1]] only through its decay order at the boundary face of tf. The face tf carries no
event horizon, so the condition s > ½ + ϑ_ℋ that [[prop:iii-f1-3-3]] meets for the spectral families on X (whence its
"s large") does not enter the bound on tf. So [[eq:i-c-5-1]] holds at
s = 1 and α_+ = 0, and with [[thm:i-c-4-3]] (4) for k further b-derivatives, N_tf(±1)⁻¹ is bounded from
H^((s−2;k),(𝗋+1,q−2))_(sc,b;b) to H^((s;k),(𝗋,q))_(sc,b;b), as in the proof of [[cor:iii-f1-3-4]].

*The orders.* That proof takes δ_0 := ¼(3/2 − β_sctf) ∈ (0, 1/8], ϵ < δ_0, the outgoing order
𝗋_out := β_sctf − 2 − ϵ/2, and the orders 𝗋_± of [[lem:i-a-7-1]] at σ_* = ±1 with that outgoing value; it arranges
𝗋_out < −½ + S̄_L at R_out with an inner product there. [[lem:i-a-7-1]] also asks 𝗋_in > (−1 + ϑ_in)/2 − α_+ and
𝗋_in ≥ 𝗋_out, with ϑ_in in an inner product of our choice at the incoming radial sets ((O3) of [[sec:i-a-1-4]]). With
the inner product of [[lem:ec-theta-in-zero]], ϑ_in = 0, so (−1 + ϑ_in)/2 = −½ < −¼ = 𝗋_in; and
𝗋_out < −½ < 𝗋_in. The order of [[lem:i-a-7-1]] is 𝗋 = 𝗋_out + (𝗋_in − 𝗋_out)Θχ_c with 0 ≤ Θχ_c ≤ 1, equal to
𝗋_out near R_out and to 𝗋_in near the incoming radial sets; so inf 𝗋 = 𝗋_out and sup 𝗋 = 𝗋_in.

*The losses.* In [[lem:ii-g1-4-1]] at s = 1, ⌈(s − 1)_+⌉ = ⌈(−s)_+⌉ = 0, so ℓ = ⌈sup 𝗋 − 𝗋_out⌉ and
ℓ̃ = ⌈𝗋_out − inf 𝗋⌉ = 0. Here 0 < sup 𝗋 − 𝗋_out = 𝗋_in − 𝗋_out = 7/4 − β_sctf + ϵ/2 < 3/4 + 1/16 < 1, as β_sctf ≥ 1
and ϵ < 1/8; so ℓ = 1 for every such ϵ, and the last step of the proof of [[cor:iii-f1-3-4]] (k replaced by k + ℓ̃,
ℓ made independent of ϵ) changes nothing. Near ztf the two spaces are H^(s−2+k)_(b,β_ztf−2) = H^(k−1)_(b,β_ztf−2) and
H^(s+k)_(b,β_ztf) = H^(k+1)_(b,β_ztf), which the input order k + 1 and the output order k accommodate. So
[[eq:iii-f1-3-3]] holds with ℓ = 1. The expression of [[lem:ec-closed-forms]] (d) at these orders is ℓ + ℓ̃ = 1, and it
is at least 1 at every choice.

*The applications.* [[thm:iii-g4-3-1]] uses [[cor:iii-f1-3-4]] with β_sctf = ℓ_scf, and [[prop:iii-g4-4-4]] and
[[prop:iii-g4-5-1]] use it through [[thm:iii-g4-3-1]] or directly with β_sctf = ℓ_scf. The construction may apply them
with ℓ_scf := 3/2 − ε, as [[lem:ec-tf-loss]] takes it: in Step 3.2 of the proof of [[prop:iii-i6-2-1]], in Step 3.4′
of the proof of [[lem:iii-i8-3-2]], at level 1 of the proof of [[prop:iii-i11-3-1]], and at levels 2 and 3 there and in
[[prop:iii-i13-2-1]] and [[prop:iii-j3-4-3]], whose forcings keep the scf-order 5/2 − ε of Step 0
([[lem:iii-i11-2-2]]), which allows ℓ_scf := 3/2 − ε there. In each of them ε is a loss that the proof takes small, and
the bounds on it there give ε < ¼: ε < ½ε_g < ¼ in [[lem:iii-i8-3-2]], 2ε < ε_+ − η_2 in [[sec:iii-i11-1]], and
5ε ≤ 5ε_1 < ε_+ in [[sec:iii-j2-1]], with ε_+ < δ_♯ < ¼ ([[eq:iii-i9-1-1]]). So β_sctf = 3/2 − ε ∈ (1, 3/2) at every
application; and an application at another sctf-weight in [1, 3/2), such as the weight 3/2 − 2ε of the level-3
solution, has ℓ = 1 as well, by the first part of the proof. ∎

#### The order of the background terms {#sec:uc-dbg}

**Proposition {#prop:uc-dbg}** (d_BG = 11 serves.) For ‖β‖_(d_0) small, with d_0 ≥ 11, every family A of
[[lem:iii-j2-2-1]] (b) applied to a solution satisfies

    ‖Au‖_k ≤ C_k (‖u‖_(k+2) + ‖β‖_(k+11) ‖u‖_2),                                                       {#eq:uc-dbg}

and each family v_β of sources in [[lem:iii-j2-2-1]] (b) satisfies ‖v_β‖_k ≤ C_k(1 + ‖β‖_(k+11)). So the families of
[[lem:iii-j2-2-1]] (b) have split loss (2; 11, 2) in the sense of [[lem:ec-split-loss]], the bound of
[[lem:iii-j2-2-1]] (b) holds with d = 11, and the charge max(2, d_BG) of [[rem:ec-other-losses]] may be taken to be 11.

*Proof.* *The background as a metric.* The families depend on β = (h, p⃗, q) through h̃ := h + h_tot(p⃗) + h_(b,rem)(q)
and through p⃗. By [[lem:iii-i9-2-5]], ‖h_tot(p⃗)‖_(𝒳^k) ≤ C_k|p⃗|. By [[eq:iii-i14-1-2]] and [[def:iii-g2-2-5]],
h_(b,rem)(q) is a finite sum of fixed smooth tensors times the components of q and their t_*-derivatives of order at most
3 (the towers use the derivatives a^((j)), j ≤ k_μ ≤ 3, [[lem:iii-g2-2-6]]). On functions of t_*,
∂_(t_*) = t_*⁻¹(t_*∂_(t_*)), and t_*∂_(t_*) is the b-vector field of the spaces of [[eq:iii-i14-1-1]], while t_*⁻¹ only
adds decay; so ‖h_(b,rem)(q)‖_(𝒳^k) ≤ C_k‖q‖_(𝒬^(k+3)). Hence ‖h̃‖_m ≤ C_m‖β‖_(m+3) for every m.

*The coefficients.* By [[lem:iii-j2-2-1]] (b), A is a b-differential operator of order at most 2 whose coefficients, in
the frame and in local b-coordinates on a finite atlas, are polynomials in the metric, its inverse and their
derivatives, the background g_0 being smooth in p⃗; the derivatives of the metric are of order at most 2, A being a
difference of linearisations of the second-order operator P of [[eq:iii-b-6-4]], or such a difference applied to a
fixed section. Let A′ be A with h̃ replaced by 0; its coefficients are smooth in x and p⃗ alone, so
‖A′u‖_k ≤ C_k‖u‖_(k+2). Then A = A′ + Σ_(|γ|≤2) Φ_γ(x, p⃗, w) D^γ_b, where w := (h̃, D_b h̃, D²_b h̃) and Φ_γ is
smooth with Φ_γ(x, p⃗, 0) = 0.

*The estimates.* We use [[lem:ii-g-4-1]] on the five-dimensional manifold with corners, with d = 3 > 5/2, after a
finite partition of unity (on which the norms are equivalent) and after factoring the weights, whose powers of the
defining functions commute with b-derivatives up to smooth factors. The proof of its (3), by the chain rule and
[[eq:ii-g-4-1]], applies verbatim to a smooth function Φ(x, p⃗, w) of a vector w with Φ(x, p⃗, 0) = 0 and bounded
derivatives in x and p⃗ on the chart domains; so ‖Φ_γ(·, p⃗, w)‖_m ≤ C_m‖w‖_(m+3) ≤ C_m‖h̃‖_(m+5) for ‖w‖_3 small. By its
(2), with Φ_γ in the place of the factor measured at the high order,

    ‖Φ_γ D^γ_b u‖_k ≤ C_k (‖Φ_γ‖_3 ‖u‖_(k+2) + ‖Φ_γ‖_(k+3) ‖u‖_2) ≤ C_k (‖h̃‖_8 ‖u‖_(k+2) + ‖h̃‖_(k+8) ‖u‖_2),

and ‖h̃‖_8 ≤ C‖β‖_11 ≤ C‖β‖_(d_0), ‖h̃‖_(k+8) ≤ C_k‖β‖_(k+11). This is [[eq:uc-dbg]] on the remainders. At a face
where the spaces carry an expansion, the coefficients of a product are finite sums of products of coefficients, and
the coefficients of Φ_γ(·, p⃗, w) are polynomials in those of w, functions on a face of dimension at most 4, which
(2) and (3) of [[lem:ii-g-4-1]] bound with the same d = 3 > 4/2; so the coefficient norms obey the same bound. The
sources are the case of a fixed section u, or of a fixed operator applied to the background. ∎

#### The Fourier steps and the map Φ {#sec:uc-counts}

**Lemma {#lem:uc-fourier-count}** (The Fourier step of a level above 3.) At a level β ∈ (3, α] of
[[thm:iii-i14-3-1]], Step 0 of the proof of [[prop:iii-i11-3-1]] (through [[prop:iii-i13-2-1]] when β < 4) applies
[[prop:iii-a-4-2]] (1) with E_ι = ℰ^♭ + 2, β_ι = w_+ − ε, E_I = E_K = ∅ and β_K = β − ε. Its loss, by the case
E_I = ∅ of the proof of [[lem:ec-closed-forms]] (g), is

    l = 1 + n_ι + 2⌊β − ε⌋,     n_ι = n(ℰ^♭ + 2, w_+ − ε),                                         {#eq:uc-fourier-count}

and n_ι is the number of pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε. [[prop:iii-i10-3-1]] (c) states of ℰ^♭ that
π_1(ℰ^♭ ∩ {Re < 3 + ε_+}) ⊂ Λ ∩ {Re ≥ 2} and that its logarithmic order at λ is at most k̄(λ). So, with
N_Λ := |Λ ∩ {Re < 3 + ε_+}| and l_*, k̄_0, J_* of [[def:iii-i10-1-1]],

    n_ι ≤ N_Λ(k̄_0 + 1) + (J_* + 1)(l_* + 1)N_Λ²,     J_* ≤ ⌈5/ε_Υ⌉ + 2,

and at ε_Υ = 1.4619·10⁻¹⁰, J_* ≤ 34,202,065,807. The single-step loss c(β) of [[prop:ec-upper]] at such a level is at
least 1 + n_ι. (For the index sets as constructed, η_0 = 𝔡₁ and J_* = 15,000,015 ([[prop:is-count]] (c)), and
[[lem:uc-n-iota]] gives a sharper bound for n_ι.)

*Proof.* The data of Step 0 are those printed there. By the case E_I = ∅ of the proof of [[lem:ec-closed-forms]] (g)
(the formula (1) of (g), which holds for every E_I, gives 1 + n_ι + 10 here),
l = 1 + n_ι + 2(n_K + ⌊β_K⌋) with n_K = n(∅, β_K) = 0. By the definition of n(E, β) before [[lem:ec-closed-forms]],
n(E_ι, β_ι) counts the pairs (z, m′) ∈ ℰ^♭ + 2 with Re z ≤ w_+ − ε = 5 + ε_+ − ε. At an exponent λ of ℰ^♭ of
logarithmic order m there are m + 1 pairs, and m ≤ k̄(λ) = k̄_0 + (J_* + 1)(l_* + 1)(n(λ) + 1) with n(λ) ≤ N_Λ − 1; at
most N_Λ exponents occur. This gives the bound for n_ι. By [[lem:ec-iota-gap]], η_0 ≥ ε_Υ, so
J_* = ⌈5/η_0⌉ + 2 ≤ ⌈5/ε_Υ⌉ + 2, and 5/(1.4619·10⁻¹⁰) = 500000000000000/14619 = 34202065804.77…, whose ceiling is
34,202,065,805. The level step composes this map with maps of non-negative loss, so by [[def:ec-accounted-loss]] its
charge is at least l ≥ 1 + n_ι. ∎

**Lemma {#lem:uc-phi-loss}** (The loss of Φ and the two other components of d_NM.) Let 3 < ℓ_I < 3.5, and let the
strips of [[cor:iii-g3-3-1]] used in the proof of [[thm:iii-j-2-4]] be taken with λ₋ ∈ (ℓ_I − 2, 3/2) and
δ_ι < 3.5 − ℓ_I. The proof of [[thm:iii-j-2-4]] fixes its loss d as the sum, over its steps, one for each λ₀ in
Λ_* = Λ ∩ {Re < 3 + ε_+}, of the loss l′ of [[cor:iii-g3-3-1]], the loss 2 of the functionals of [[thm:iii-g2-3-1]] and
the loss l of [[prop:iii-g3-3-7]], plus 2; so it is

    d_Φ = 62N_Λ + 2.                                                                                  {#eq:uc-phi-loss}

The losses d_FM of [[prop:iii-j2-4-3]] and d_Ψ of [[lem:iii-k-2-2]], as their proofs fix them from d_Φ and
[[lem:ii-g-4-1]], are at most d_Φ + 8 = 62N_Λ + 10, and d_NM = max(d_R, d_FM, d_Ψ), with d_R ≥ d_acc the accounted loss
of [[lem:iii-k-2-3]], and N_NM = 21d_NM + 6.

*Proof.* By [[lem:ec-closed-forms]] (f), l′ = 30 under these conditions, and l = l′ ((f) and its proof), so each step
contributes 30 + 2 + 30 = 62, and the steps are indexed by Λ_*, which has N_Λ elements; this is [[eq:uc-phi-loss]]. The
proof of [[prop:iii-j2-4-3]] bounds P_5(Φ(U)) by [[lem:ii-g-4-1]]: P_5(h, p⃗, q) − P_5(0, p⃗, 0) is a smooth function,
vanishing at 0, of w = (h″, D_b h″, D²_b h″), h″ := h + h_(b,rem)(q), with coefficients smooth in p⃗, and P_5(0, p⃗, 0)
is a fixed tensor smooth in p⃗. As in the proof of [[prop:uc-dbg]], its order-k norm is at most
C_k‖w‖_(k+3) ≤ C_k‖h″‖_(k+5) ≤ C_k‖Φ(U)‖_(k+8), with [[lem:iii-j2-2-4]] for the coefficients at the faces, and
‖Φ(U)‖_(k+8) ≤ C_k‖U‖_(𝒟^(k+8+d_Φ)); its first two derivatives are bounded in the same way, being polynomial in the
derivatives of Φ by the chain rule. So d_FM ≤ d_Φ + 8. [[lem:iii-k-2-2]] (c) is the same bound for Ψ(U), which
differs from Φ(U) by fixed tensors smooth in the finite-dimensional components of U, on the exact scales, where
[[prop:iii-j3-5-4]] follows the proof of [[thm:iii-j-2-4]] step by step; so d_Ψ ≤ d_Φ + 8 as well. d_NM is the largest
of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of [[lem:iii-k-2-3]] accounted by
[[def:ec-accounted-loss]] and at least d_acc ([[thm:loss-d]]), and N_NM = 21d_NM + 6 is the regularity of
[[thm:ii-g-2-1]] at that loss ([[thm:loss-d]], [[eq:ii-g-2-5]]). ∎

#### What the statements give {#sec:uc-reduction}

**Theorem {#thm:uc-reduction}** (Bounds for d from the statements of this paper.) At the computational point:

(i) In [[prop:ec-upper]], [[lem:ec-round-charges]] and [[rem:ec-other-losses]] one may take ℓ⁺_tf = 1 and d_BG = 11
([[prop:uc-ltf]], [[prop:uc-dbg]]).

(ii) d_NM = max(d_R, d_FM, d_Ψ) with d_R ≥ d_acc and d_FM, d_Ψ ≤ 62N_Λ + 10, N_NM = 21d_NM + 6, and every term of the
bound of [[prop:ec-upper]] other than the single-step losses is explicit in ε_K and the other weights; the single-step
losses at the levels above 3 are at least 1 + n_ι, with n_ι bounded by [[lem:uc-fourier-count]] in N_Λ, l_* and k̄_0.

(iii) N_Λ, k̄_0, l_*, J_* and the admissible ε_K (through (G)) are fixed by the exponents and logarithmic orders of the
index sets of [[sec:uc-index-sets]] and by the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5. For the
index sets as constructed and the least ℰ^C_I, (G) holds exactly for ε_K < μ_G, where
1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴ ([[thm:is-gap]]); 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3 is the
least admissible bound and J_* = 15,000,015 ([[prop:is-count]]); and l_* = 50 is admissible ([[cor:sp-lstar]]).
Memberships and least real parts alone fix no admissible ε_K ([[prop:uc-no-eps]]).

So this paper gives the lower bound of [[thm:loss-d]] (ii), raised to 3R > 1.2497·10²⁴ for the index sets as constructed
([[cor:uc-two-offsets]]), and, at levels more than ½(α − 4) apart, the upper bound of [[thm:uc-integer]], in which every
number of steps of the long iterations and every count of an index set is explicit.

*Proof.* (i) is [[prop:uc-ltf]] and [[prop:uc-dbg]]. (ii) is [[lem:uc-phi-loss]], the counts of [[lem:ec-counts]] and
[[prop:ec-upper]], and [[lem:uc-fourier-count]]. (iii) [[def:iii-i10-1-1]] and [[def:iii-i10-1-3]] define N_Λ, l_*,
k̄_0, J_* and (G) from these index sets, from the orders of the poles of N_ι⁺(L̄, ·)⁻¹ and from ε_+; the values are those
of the results cited. The last assertion is [[cor:uc-two-offsets]] (a), whose hypothesis holds by (b) there, and
[[thm:uc-integer]]. ∎

#### The evaluation at the computational point {#sec:uc-eval}

With the exponents of [[sec:is]] and the poles of [[sec:sp]], every number of [[thm:uc-reduction]] (iii) is fixed. This
section makes an admissible choice of the weights, evaluates the counts of [[eq:ec-upper]] at it, and assembles the
bound. Each decimal bound below is rounded upward when it bounds from above and downward when it bounds from below, and
each follows by multiplying out the numbers printed.

**Definition {#def:uc-choice}** (An admissible choice.) At the computational point take ℰ_ind and ℰ^ι_ind as
constructed ([[sec:is]]), ℰ^C_I the least index set satisfying (2)–(3) of [[def:iii-c-3-1]], ℰ_++ the least choice in
[[eq:iii-i8-1-1]] ([[prop:is-ci-pp]]), and

    ε_Υ := 1.4619·10⁻¹⁰,     ε_K := 1.6416·10⁻¹⁴,     ε_+ := 1.64160217·10⁻¹⁴,     l_* := 50,     k̄_0 := 3.
                                                                                                    {#eq:uc-choice}

Take ℓ_I ∈ (3 + ε_+, 3.5) with ℓ_I ≤ a_I, off the exclusion sets of (H4) of [[sec:iii-i10-1]], and λ₋ ∈ (ℓ_I − 2, 3/2)
and δ_ι ∈ (0, 3.5 − ℓ_I) in [[lem:uc-phi-loss]] and [[lem:ec-closed-forms]] (e); η_1 < η_2 in (ε_K, ε_+) with η_1 < ε_g
such that no λ ∈ Λ has real part 2 + η_1 or 3 + η_2; the loss ε of [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] with 0 < ε
≤ 10⁻³ε_g, besides the conditions that [[sec:iii-j2-1]], [[sec:iii-i11-1]] and [[def:iii-i13-1-1]] place on it; α ≥ 3
admissible ([[def:iii-i10-1-3]]) and satisfying (A_J) of [[def:iii-j-a-j]] and (Ex3)–(Ex4) of [[def:iii-j3-1-3]]; levels
β_0 = α_1 < β_1 < ⋯ < β_K = α of Step 2 of the proof of [[thm:iii-i14-3-1]] with 0.999(α − 4) ≤ β_(k+1) − β_k < α − 4;
the number a♭_K of [[lem:ec-counts]] with a♭_K > α_1 and 0.999(α − 4) ≤ a♭_K − 2 < α − 4; and the base level α_0 of
[[lem:ec-counts]], admissible, with max(2, α_1 − (a♭_K − 2)) < α_0 < α_1.

**Lemma {#lem:uc-admissible}** (The choice is admissible.) The choice of [[def:uc-choice]] exists and is admissible
for [[thm:iii-i14-3-1]], [[prop:iii-i8-4-1]], [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]], for [[thm:iii-j-2-4]] and
[[thm:iii-j1-2-1]], and on the exact scales of [[cor:iii-j3-6-6]]. At it ε_g = ε_Υ, (G) and (G⁺) hold, and the
hypotheses of [[prop:ec-upper]] and of [[eq:ec-upper-counts]] hold with

    Δβ_0 := 0.999²ε_K = 1.6383184416·10⁻¹⁴,     Δτ_0 := 0.999ε_Υ = 1.4604381·10⁻¹⁰.                    {#eq:uc-deltas}

Moreover ℓ⁺_tf = 1 and r_ι ≤ 16 in [[eq:ec-upper]], and the hypotheses of [[lem:uc-phi-loss]] hold.

*Proof.* *The gaps.* ε_Υ is admissible by [[lem:ec-gauge-gap]], and ε_ind(10⁻⁶) = δ_50 > 1.9413·10⁻⁸ > ε_Υ
([[def:ec-point]]), so ε_g = min(ε_Υ, ε_ind) = ε_Υ ([[def:s21-eps-g]]). *The constants of [[eq:iii-i9-1-1]].* They ask
0 < ε_K < ε_+ < min(δ_♯, ε_ind), and 1.6416·10⁻¹⁴ < 1.64160217·10⁻¹⁴ < 1.9413·10⁻⁸ < δ_50, while
δ_♯ = λ_♯ − 3/2 = 0.0099. *(G).* By [[thm:is-gap]], for the set Λ that [[def:iii-i10-1-1]] builds from the index sets
of [[def:uc-choice]], (G) holds if and only if ε_K < μ_G, and μ_G > 1.64160217197·10⁻¹⁴ > 1.6416·10⁻¹⁴ = ε_K by
[[eq:is-mu]]. Also ε_K < ε_Υ, as [[def:iii-i10-1-3]] asks. *(G⁺) and the exactness conditions.* By [[thm:is-gap]] and
its proof, λ_♯ + 1109655𝔡₀ + 31682𝔡₁ = 3 + μ_G has the least real part above 3 of the elements of Λ, and
ε_+ < 1.64160217197·10⁻¹⁴ < μ_G ([[eq:is-mu]]); so no λ ∈ Λ has real part in (3, 3 + ε_+], which is (G⁺) of
[[def:iii-j-g-plus]] and (Ex1) of [[def:iii-j3-1-3]]. (Ex2) holds: near 3 the real parts of the exponents of ℰ^tot_I
([[eq:iii-c-3-1]]) are 3 and numbers at distance at least 0.0099 from 3 ([[prop:is-ci-pp]] (a)), so none is 3 + ε_+,
and λ_♯ < 2. *(H4) and the strips.* (H4) asks ℓ_I > 3 + ε_+ off discrete sets, with ℓ_I ≤ a_I ([[sec:iii-i8-1]]), and
so a_I > 3 + ε_+ of the class; so ℓ_I ∈ (3 + ε_+, 3.5) with ℓ_I ≤ a_I off those sets exists. [[lem:uc-phi-loss]] asks
3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ_ι < 3.5 − ℓ_I, which are imposed. *η_1 and η_2.* [[sec:iii-i11-1]] asks
η_1 < η_2 in (ε_K, ε_+), η_1 < ε_g, and that 2 + η_1 and 3 + η_2 be the real part of no element of Λ; as
Λ ∩ {Re ≤ 4} is finite ([[lem:iii-i10-1-2]] (a)), such η_1 and η_2 exist. *ε.* [[sec:iii-j2-1]], [[sec:iii-i11-1]],
[[def:iii-i13-1-1]] and the proofs of [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] ask ε small and off finite sets,
so ε ≤ 10⁻³ε_g may be imposed besides. Step 4 of the proof of [[prop:iii-i11-3-1]] asks a δ₄ > 0 with
δ₄ + ℓ_3 + 2ε < ε_g, where ℓ_3 = α − 4 − ε < ε_K; it exists, as ε_K + ε ≤ 1.6416·10⁻¹⁴ + 1.4619·10⁻¹³ < ε_g. *α.* An
admissible α ≥ 3 is a number in (4 + ε_K − ε′_0, 4 + ε_K], ε′_0 = ½ min(ε_K, ε_+ − ε_K) = ½(ε_+ − ε_K) =
1.085·10⁻²⁰, off a finite set ([[def:iii-i10-1-3]]), and (A_J), (Ex3) and (Ex4) exclude finitely many more
([[def:iii-j-a-j]], [[lem:iii-j3-1-4]]: (A_J) excludes the α with α − Re λ₀ one of the finitely many numbers −Re μ and
Re π_1ℰ_K in (0, 3), for the finitely many λ₀ ∈ Λ with Re λ₀ < 3 + ε_+); so such an α exists, and as
ε′_0 < 0.001ε_K, 0.999ε_K ≤ α − 4 ≤ ε_K. *The levels.* The excluded values near each level are finitely many
([[sec:iii-i8-1]], [[def:iii-i13-1-1]]). Choose the levels downward from β_K := α, each spacing in
[0.999(α − 4), α − 4) and each level admissible and different from 3, until the first level below α − 2 is reached; as
every spacing is less than α − 4, that level lies in (2, α − 2), and it is α_1. *a♭_K.* The background h + h_rem(q)
has the K⁺-order (α − 2)− ([[lem:ec-counts]]), so Step 1 of the proof of [[thm:iii-i14-3-1]] may apply its statements
with any a♭_K in (α_1, α − 2); the stated range meets that interval, as α_1 < α − 2 and 2 + 0.999(α − 4) < α − 2.
*α_0.* The proof of [[prop:iii-i8-4-1]] at the level α_1, at the background of K⁺-order a♭_K, starts from an
admissible α_0 ∈ (2, min(a♭_K, 2 + ε_g, 5/2)) below α_1; as α_1 < a♭_K, α_1 < 2 + ε_K < 2 + ε_g and the excluded
values are finitely many, an admissible α_0 ∈ (max(2, α_1 − (a♭_K − 2)), α_1) exists; as α_1 − α_0 < a♭_K − 2, that
proof then has the single level step α_0 → α_1.

*The hypotheses of [[prop:ec-upper]].* Δβ ≥ 0.999(α − 4) ≥ 0.999²ε_K = Δβ_0 and Δβ ≥ 0.999(α − 4) > ½(α − 4);
a♭_K − 2 ≥ 0.999(α − 4) ≥ Δβ_0; Δτ = ε_g − ε ≥ (1 − 10⁻³)ε_Υ = Δτ_0; and Δβ_0 ∈ (0, 1]. ℓ⁺_tf = 1 by [[prop:uc-ltf]]
and [[lem:ec-round-charges]], and r_ι = d^max_ι + 2 + 2(⌊ℓ_I − 5/2⌋ + 1) ≤ 12 + 4 = 16 by [[lem:ec-round-charges]] (c),
as 3 < ℓ_I < 3.5 and δ_ι < 3.5 − ℓ_I. ∎

**Lemma {#lem:uc-gaps}** (The least real parts of the increments.) For the index sets as constructed,
min Re ℰ_ind = min Re ℰ^ι_ind = η_0 = 𝔡₁. Hence [[lem:ec-counts]] (d) and (e) hold with 𝔡₁ in place of ε_Υ, and
[[prop:ec-upper]] holds with

    T_2 := N_>((1 + η_2 − η_1)/𝔡₁ + 2),     W := (2 − λ_♯)/𝔡₁ + 1.                                      {#eq:uc-t2-w}

*Proof.* By [[eq:is-low]] the least exponent of ℰ_ind is 𝔡₁; by [[prop:is-iota]] the exponents of ℰ^ι_ind of real part
at most 5 are those of ℰ_ind, the integers 1, …, 5 and numbers of real part greater than 3; so both least real parts
are 𝔡₁, and η_0 = 𝔡₁ ([[prop:is-count]] (c)). The proof of [[lem:ec-counts]] (d) uses ε_Υ only as a lower bound for
min Re ℰ_ind, through the exponents (α_0, k) + ℰ_ind of the remainder [[eq:iii-g4-4-3]], and that of (e) only as a lower
bound for ε^ι_ind = min Re ℰ^ι_ind, the least amount by which a window of Step 2 of the proof of [[prop:iii-i5-2-1]]
raises the least real part of the ι⁺-exponents still to be treated. So both hold with 𝔡₁. The proof of
[[prop:ec-upper]] uses (d) and (e) only through the bound (1 + η_2 − η_1)/ε_Υ + 1 for the applications at level 2 along
a chain in one level step, which gives T_2, and through the bound W for the windows of one loop; with 𝔡₁ in place of
ε_Υ these are the numbers of [[eq:uc-t2-w]]. ∎

**Lemma {#lem:uc-lambda}** (The numbers of [[def:iii-i10-1-1]].) At the choice of [[def:uc-choice]]:

(a) N_Λ = #(Λ ∩ {Re < 3 + ε_+}) is an integer with 16,206,600,000,000 < N_Λ ≤ 16,747,199,999,999;

(b) k̄_0 = 3, l_* = 50, η_0 = 𝔡₁ and J_* = 15,000,015, so that J′ := (J_* + 1)(l_* + 1) = 765,000,816;

(c) the elements of Λ ∩ {Re < 3 + ε_+} are real; listed in increasing order as λ_1 < ⋯ < λ_(N_Λ), they have
n(λ_i) = i − 1 and k̄(λ_i) = 3 + 765,000,816·i ≤ 12,811,621,665,714,434,999,187 < 1.28117·10²²;

(d) d_Φ = 62N_Λ + 2 ≤ 1,038,326,399,999,940, and d_FM, d_Ψ ≤ 62N_Λ + 10 ≤ 1,038,326,399,999,948.

*Proof.* (a) is [[prop:is-count]] (a): 1.62066·10¹³ = 16,206,600,000,000, and an integer below 1.67472·10¹³ is at most
16,747,199,999,999. (b) [[prop:is-count]] (b), (c) give k̄_0 = 3 as the least admissible bound, η_0 = 𝔡₁ and
J_* = 15,000,015; l_* = 50 is admissible by [[cor:sp-lstar]] (a); and 15,000,016 · 51 = 765,000,816. (c) By
[[prop:is-lambda]] the elements of Λ of real part at most 3 + ε_+ are real. The λ′ ∈ Λ with Re λ′ < λ_i lie in
Λ ∩ {Re < 3 + ε_+}, so they are λ_1, …, λ_(i−1), and n(λ_i) = i − 1; then [[def:iii-i10-1-1]] gives
k̄(λ_i) = k̄_0 + J′(n(λ_i) + 1) = 3 + 765,000,816·i, and for i ≤ 16,747,199,999,999 this is at most
3 + 765,000,816 · 16,747,199,999,999 = 12,811,621,665,714,434,999,187. (d) is [[lem:uc-phi-loss]] with (a), as
62 · 16,747,199,999,999 = 1,038,326,399,999,938. ∎

**Lemma {#lem:uc-n-iota}** (The counts of the Fourier steps.) At the choice of [[def:uc-choice]], let E be an index set
with π_1(E ∩ {Re < 3 + ε_+}) ⊂ Λ whose logarithmic order at each λ ∈ Λ with Re λ < 3 + ε_+ is at most k̄(λ); by
[[prop:iii-i10-3-1]] (c), ℰ^♭ is one. Then for every w < 3 + ε_+,

    n(E, w) ≤ 4N_Λ + 765,000,816·N_Λ(N_Λ + 1)/2 ≤ N_ι,
    N_ι := 107,279,395,180,026,392,909,234,131,199,999,996,                                               {#eq:uc-n-iota}

and N_ι < 1.07280·10³⁵. In particular the count n_ι of [[lem:uc-fourier-count]] is at most N_ι, and the Fourier step of
Step 0 of the proof of [[prop:iii-i11-3-1]] at a level β ∈ (3, α] loses at most 9 + N_ι.

*Proof.* A pair (z, m) ∈ E with Re z ≤ w has z ∈ Λ ∩ {Re < 3 + ε_+}, so z = λ_i for some i ≤ N_Λ, and m ≤ k̄(λ_i)
([[lem:uc-lambda]] (c)); at z = λ_i there are at most k̄(λ_i) + 1 = 4 + 765,000,816·i such pairs. Summing over i,
n(E, w) ≤ 4N_Λ + 765,000,816·N_Λ(N_Λ + 1)/2, which increases with N_Λ; at N_Λ = 16,747,199,999,999, where
(N_Λ + 1)/2 = 8,373,600,000,000, it equals

    4 · 16,747,199,999,999 + 765,000,816 · 16,747,199,999,999 · 8,373,600,000,000 = N_ι.

By [[lem:uc-fourier-count]], n_ι counts the pairs (λ, k) ∈ ℰ^♭ with Re λ ≤ 3 + ε_+ − ε, so n_ι = n(ℰ^♭, 3 + ε_+ − ε)
≤ N_ι, and the loss [[eq:uc-fourier-count]] is 1 + n_ι + 2⌊β − ε⌋ ≤ 1 + N_ι + 8, as β − ε < α ≤ 4 + ε_K < 5. ∎

**Proposition {#prop:uc-explicit}** (The counts of the long iterations.) At the choice of [[def:uc-choice]], in
[[lem:ec-counts]], [[eq:ec-upper-counts]] and [[eq:uc-t2-w]],

    N_<, N_>, N_b < 6.10382·10¹³,     T_<, T_> < 2.089723·10²³,     T_2 < 1.83115·10²⁰,     W < 1,470,302.27,
                                                                                                     {#eq:uc-counts}

and every window loop has at most 1,470,302 windows. The first line of [[eq:ec-upper]], with ℓ⁺_tf = 1, r_ι ≤ 16 and
the T_2 and W of [[eq:uc-t2-w]], is less than D_e := 1.2587·10²⁴; of it, the window loops at ι⁺ contribute less than
4.30775·10²¹. The number K of the levels β_1, …, β_K and the number N_b of [[lem:ec-counts]] (f) satisfy
K + 2N_b + 2 < M_c := 2.44153·10¹⁴.

*Proof.* By [[eq:uc-deltas]] and the lower bound for 𝔡₁ of [[lem:is-offsets]] (b),

    1/Δβ_0 < 6.1038195·10¹³,     1/Δτ_0 < 6.847261·10⁹,     1/(2Δβ_0Δτ_0) < 2.0897221·10²³,
    1/𝔡₁ < 3.0000026·10⁶,     0.4901/𝔡₁ < 1,470,301.27,

each by multiplying out (for instance 1.6383184416 · 6.1038195 > 10, and
3.333330462964850822194855 · 1.47030127 > 4.901). By [[eq:ec-upper-counts]], N_< ≤ 1/Δβ_0, and N_>, N_b ≤
(1 + ε_K)/Δβ_0 + 1 < 1/Δβ_0 + 3, as ε_K/Δβ_0 = 1/0.998001 < 2; so all three are less than
6.1038195·10¹³ + 3 < 6.10382·10¹³. As (1 + Δβ_0/2)² < 1 + 2·10⁻¹⁴, (1 + ε_K + Δβ_0/2)² < 1 + 6·10⁻¹⁴ and
2(1 + ε_K)/Δβ_0 + 2 < 1.3·10¹⁴,

    T_< < 2.0897221·10²³ · (1 + 2·10⁻¹⁴) + 6.2·10¹³ < 2.089723·10²³,
    T_> < 2.0897221·10²³ · (1 + 6·10⁻¹⁴) + 1.3·10¹⁴ < 2.089723·10²³.

As η_2 − η_1 < ε_+ < 10⁻¹³, (1 + η_2 − η_1)/𝔡₁ + 2 < (1 + 10⁻¹³) · 3.0000026·10⁶ + 2 < 3.000005·10⁶, and so
T_2 < 6.10382·10¹³ · 3.000005·10⁶ < 1.83115·10²⁰. W = 0.4901/𝔡₁ + 1 < 1,470,302.27, and the number of windows of a
loop, an integer at most W ([[lem:uc-gaps]]), is at most 1,470,302. In the first line of [[eq:ec-upper]],
1/Δτ ≤ 1/Δτ_0, so 4(1/Δτ + 2) < 4(6.847261·10⁹ + 2) < 2.74·10¹⁰; N_< + N_> + N_b + 3 < 3 · 6.10382·10¹³ + 3 <
1.831147·10¹⁴, so r_ιW(N_< + N_> + N_b + 3) < 16 · 1,470,302.27 · 1.831147·10¹⁴ < 4.30775·10²¹, and so is the
contribution of the window loops, each of at most 1,470,302 windows. Hence the first line is less than

    3 · (2 · 2.089723·10²³ + 1.83115·10²⁰) + 2.74·10¹⁰ + 4.30775·10²¹
        < 1.2543832·10²⁴ + 4.30775·10²¹ + 2.74·10¹⁰ < 1.2587·10²⁴.

Finally, at most N_< levels lie in (2, 3) and at most N_> in (3, α] ([[lem:ec-counts]] (a)), and no level equals 3; so
K ≤ N_< + N_>, and K + 2N_b + 2 < 4 · 6.10382·10¹³ + 2 < 2.44153·10¹⁴. ∎

**Lemma {#lem:uc-dr}** (The accounted loss of the right inverse for Ψ.) Let c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 be the
numbers defined before [[prop:ec-upper]] for the construction of ℛ(U) in the proof of [[lem:iii-k-2-3]], in place of
the constructions of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]. Each is finite, and d_R, the number that
[[def:ec-accounted-loss]] assigns to that construction, satisfies [[eq:ec-upper]] with c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0
in place of c(β_k), c_b, c′_b and c_0, and with the same first line. If d_R > 62N_Λ + 10, then d_NM = d_R.

*Proof.* By the proof of [[lem:iii-k-2-3]], ℛ(U) is the construction of the proof of [[thm:iii-j1-2-1]] at the base
point Ψ(U), with U ↦ Ψ(U) in place of U ↦ Φ(U), in which [[thm:iii-i14-3-1]] runs with the two further terms
e_S(S′) + e_(S⁰)(S⁰′) in the forcing of Step 2 of its proof, entering its Steps 1 and 3 as terms of the same kind; on the
exact scales, [[cor:iii-j3-6-6]] replaces weights, not maps, in these constructions. The base point enters the
elementary families only through their constants ([[lem:iii-j2-2-1]]), and the levels, the rounds, the applications at
the levels 1 and 2 and the windows of the long iterations are fixed by the weights and the index sets
([[lem:ec-counts]]); so they are those of [[lem:ec-counts]], with the charges of [[lem:ec-round-charges]]. The added
terms are summands of the forcings of the level steps and of the base, so their charges belong to the steps that contain
them. The proof of [[prop:ec-upper]], read for this construction, therefore splits its charges in the same way and gives
[[eq:ec-upper]] with the numbers c^Ψ in place of the c. Each of these numbers is assigned by [[def:ec-accounted-loss]] to
a composition of finitely many elementary families, so it is finite. By [[lem:uc-phi-loss]],
d_NM = max(d_R, d_FM, d_Ψ) with d_FM, d_Ψ ≤ 62N_Λ + 10. ∎

**Theorem {#thm:uc-integer}** (The loss d at the computational point.) At the computational point, with the index sets as
constructed, the admissible choice of the weights of [[def:uc-choice]] and the free orders and inner products of
[[def:cs-choices]], let c_* be the largest of the numbers c(β_k) (1 ≤ k ≤ K), c_b, c′_b and c_0 defined before
[[prop:ec-upper]] and c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]: the largest loss that [[def:ec-accounted-loss]]
assigns to a single step outside the long iterations. Then
c_* < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵ ([[prop:cs-cstar]]), and

    d_acc ≤ D_acc,     d_NM = d_R ≤ D_NM := D_acc,     N_NM = 21d_NM + 6 ≤ 21D_NM + 6,                  {#eq:uc-integer}

where, with D_e = 1.2587·10²⁴ = 1,258,700,000,000,000,000,000,000 and M_c = 2.44153·10¹⁴ = 244,153,000,000,000,

    D_acc := D_e + M_c C_* = 157,156,403,040,000,000,000,000,001,258,700,000,000,000,000,000,000 < 1.57157·10⁵⁰,
    21D_NM + 6 = 3,300,284,463,840,000,000,000,000,026,432,700,000,000,000,000,000,006 < 3.30029·10⁵¹.

The two other components of d_NM satisfy d_FM, d_Ψ ≤ 1,038,326,399,999,948. At a level β ∈ (3, α],
1 + n_ι ≤ c(β) ≤ 2N_ι + N̄_Λ + 529 = C_lev, with N_ι of [[eq:uc-n-iota]], N̄_Λ = 16,747,199,999,999 and C_lev of
[[eq:cs-clev]] ([[lem:cs-levels]]). Against these, for every admissible choice of the weights,

    d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴,     N_NM > 2.624·10²⁵,                                                {#eq:uc-lower}

and at the choice of [[def:uc-choice]], 3R > 1.2498·10²⁴, so that D_e < 1.0072 · 3R.

*Proof.* By [[prop:cs-cstar]], c_* < C_*. By [[lem:uc-admissible]] the hypotheses of [[prop:ec-upper]] hold, and by
[[lem:uc-gaps]] it holds with the T_2 and W of [[eq:uc-t2-w]]. Its first line is less than D_e by [[prop:uc-explicit]],
and its second line is at most Σ_k c(β_k) + N_b c_b + (N_b + 1)c′_b + c_0 ≤ (K + 2N_b + 2)c_* ≤ M_c C_*, again by
[[prop:uc-explicit]]. So d_acc ≤ D_e + M_c C_* = D_acc. Here M_c C_* = 244,153 · 64,368 · 10⁴⁰, which is
15,715,640,304 · 10⁴⁰ = 157,156,403,040 · 10³⁹; adding D_e = 1,258,700 · 10¹⁸ gives the integer printed, and
21D_acc + 6 is 21 · 157,156,403,040 · 10³⁹ + 21 · 1,258,700 · 10¹⁸ + 6, that is
3,300,284,463,840 · 10³⁹ + 26,432,700 · 10¹⁸ + 6.
[[lem:uc-dr]] gives the same bound for d_R, its first line being the same and its single-step losses being at most
c_* < C_*. As d_R ≥ d_acc ≥ 3R > 1.2497·10²⁴ ([[lem:uc-phi-loss]], [[thm:loss-d]], [[cor:uc-two-offsets]]), which
exceeds 1,038,326,399,999,948 ≥ 62N_Λ + 10 ([[lem:uc-lambda]] (d)), [[lem:uc-dr]] gives d_NM = d_R, and the bounds for
d_FM and d_Ψ are [[lem:uc-lambda]] (d). N_NM = 21d_NM + 6 by [[thm:loss-d]]. The statements at the levels above 3 are
[[lem:uc-fourier-count]] and [[lem:cs-levels]] (b). [[eq:uc-lower]] is [[cor:uc-two-offsets]] (a),
whose hypothesis holds by (b) there. At the choice of [[def:uc-choice]], [[prop:ec-rounds]] gives
R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂), where 3ε_K + 2δ̂ + δ̄ < 1.98·10⁻⁸ and ε_Kδ̂ = 2.400249024·10⁻²⁴ < 2.40025·10⁻²⁴; so
3R > 3(1 − 1.98·10⁻⁸)/(2.40025·10⁻²⁴) > 1.2498·10²⁴, and 1.0072 · 1.2498 > 1.2587. ∎

**Remark {#rem:uc-missing}** (What the integer bound rests on.) The counts of [[prop:ec-upper]] need two statements at
the computational point, and both are established. (IS): the exponents of real part at most 5 of ℰ_ind (with its
enlargements in [[sec:iii-i8-1]] and [[sec:iii-i9-1]]), ℰ^ι_ind and the least ℰ^C_I, and those of the least ℰ_++ below
2λ_♯, as the constructions of [[sec:uc-index-sets]] give them, with bounds for their logarithmic orders, and the
multiplicities of the indicial roots of L̂_b(0) ([[prop:is-ind]], [[prop:is-logs]], [[prop:is-iota]],
[[prop:is-ci-pp]], [[prop:is-mult]]). (SP): the orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, all equal
to 1 ([[thm:sp-spectrum]], [[cor:sp-lstar]]). With them (G), N_Λ, k̄_0, l_*, J_* and every number of steps of the long
iterations are explicit ([[thm:is-gap]], [[prop:is-count]], [[lem:uc-lambda]], [[prop:uc-explicit]]), and so is a bound
for the count n(E, w) of every index set whose exponents below 3 + ε_+ lie in Λ with the logarithmic orders k̄(λ)
([[lem:uc-n-iota]]), which [[lem:iii-i10-1-2]] (c) and [[lem:iii-i13-1-3]] (b) assert of every exponent that the level
steps produce.

The single-step losses are bounded in [[sec:cs]], which lists the factors of each composition: for the level steps
those of [[lem:iii-i8-3-2]] and [[lem:iii-i13-2-2]], with the steps of [[prop:iii-i10-3-1]], [[prop:iii-i11-3-1]] and
[[prop:iii-i13-2-1]] outside the long iterations, and the background terms of Step 2 of the proof of
[[thm:iii-i14-3-1]] ([[lem:cs-levels]]); one round of [[prop:iii-i5-2-1]] and one step of [[prop:iii-i2-5-1]]
([[lem:cs-base]]); and Steps 0, 1, 3, 4′ and 4 of that proof, U ↦ Φ(U) and Steps 1–3 of the proof of
[[thm:iii-j1-2-1]], with their counterparts for ℛ(U) ([[lem:cs-rest]]). The closed forms are evaluated at the free
choices of [[def:cs-choices]]: the regularity order s_c = 3 > ½ + ϑ_ℋ and the inner products in which ϑ_in = 0 and
ϑ_ℋ < 9/4 ([[lem:cs-transforms]]). The count of the K⁺-exponents in the application of [[prop:iii-a-4-2]] (2) in Step 7
of the proof of [[prop:iii-i11-3-1]] is at most N_ι + N_Λ ([[lem:cs-fourier]]). So M_c C_* is of the order of 10⁵⁰, far
above D_e: the bound counts every logarithmic term that k̄(λ) allows, and a bound for c_* of the order of D_e/M_c needs
the logarithmic orders that the level steps produce, which this paper bounds only by k̄(λ) ([[rem:cs-sharpness]]).

### The exponents of the index sets at the computational point {#sec:is}

This section carries out, at the computational point of [[def:ec-point]], the constructions that fix the index sets of
[[sec:uc-index-sets]], keeping the exponents. It lists the exponents of real part at most 5 of ℰ_ind
([[prop:is-ind]]), of ℰ^ι_ind ([[prop:is-iota]]) and of the least ℰ^C_I, and those of the least ℰ_++ below 2λ_♯
([[prop:is-ci-pp]]), with bounds for their logarithmic orders ([[prop:is-logs]]), and bounds for the multiplicities of
the indicial roots of L̂_b(0): every multiplicity is at most 7, and every root of real part in [−101, 5] is simple
([[prop:is-mult]]). This is the statement (IS) of [[rem:uc-missing]] (which asks the multiplicities on the half-plane
Re ≤ 5), except the exponents of the least ℰ_++ above 2λ_♯: these depend on ℰ_+, and nothing below uses them
([[rem:is-summary]]). From these it determines Λ ∩ {Re ≤ 3 + ε_+} ([[prop:is-lambda]]); it shows that (G) holds
exactly for ε_K < μ_G, where

    1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴                                                   {#eq:is-mu}

([[thm:is-gap]]); and it gives 1.62066·10¹³ < N_Λ < 1.67472·10¹³, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]).
Finally it decides when ℰ_ind can omit 𝔡₀ ([[thm:is-d0]]): an admissible ℰ_ind that omits 𝔡₀ exists if and
only if one explicit family of coefficients c_b vanishes at every b near b₀; c_b vanishes at b₀, at every
non-rotating b and on the image of ad_(A(b)), and this paper does not determine it elsewhere. If c_b vanishes, (G)
holds for every ε_K < 5.0190·10⁻⁸, so for every ε_K that [[eq:iii-i9-1-1]] allows ([[cor:is-flat]]). Whether an
admissible ℰ_ind can omit 𝔡₁ is not decided either. Neither question enters an upper bound for the loss d: the index
sets as constructed serve with every ε_K < μ_G, and the two questions decide only whether smaller index sets, with a
larger ε_K, are available.

Throughout, z = 4·10⁻⁶ = 1/250000, h = 10⁻⁶, λ_♯ = 15099/10000 (an exponent at ι⁺, not the wavelength), and
ε_+ < δ̄ = 1.94137057·10⁻⁸ ([[def:ec-point]], [[eq:iii-i9-1-1]]). An index set *as constructed* is the one that the
lemma cited in the construction returns when its rule is applied as stated, with F the index set of the terms of the
right side, computed from the constructions that those terms come from (the proofs of [[prop:iii-d2-3-1]] and
[[prop:iii-d3-3-1]] record the right sides through ℰ_ind itself, for the boosts as (1, 0) ∪ (1 + ℰ_ind), which names the
set being built); for [[lem:iii-a-1-4]] this is the set E = ⋃_k E_k there, and for [[lem:iii-a-1-5]] the set E
there. An index set containing it serves in every membership that the construction asserts. For an index set X and
w ∈ ℂ we write k(X, w) for the logarithmic order of X at w, and ℓ̂_X(w) := k(X, w) + 1 if w ∈ π_1X, ℓ̂_X(w) := 0
otherwise. We write N(L̂_b(0), ·) for the indicial family of ρ⁻²L̂_b(0).

#### The roots and the offsets {#sec:is-roots}

**Definition {#def:is-roots}** (The roots.) For l ≥ 1 let d₁(l) and d₂(l) be the numbers d₁ and d₂ of
[[prop:np-10-52]] (i) at u = l + 1, so that ι^Υ_(sl,l+1) = l + 1 + d₂(l) and ι^Υ_(sl,l+2) = l + 2 + d₁(l). Put
𝔡₀ := ι^Υ_(s0,2) − 2, 𝔡₁ := d₂(1), δ′₁ := d₁(1), δ₂ := d₂(2) ([[sec:ec-gap-sums]]), and

    R := {2 + 𝔡₀} ∪ {l + 1 + d₂(l), l + 2 + d₁(l) : l ≥ 1} ∪ {3, 4, 5, …}.

**Lemma {#lem:is-roots}** (The indicial roots of (□^Υ_b)^(0).) (a) R is the set of indicial roots of (□^Υ_b)^(0) with
positive real part, at every b near b₀. Every root of positive real part is at least ι^Υ_(s1,2) = 2 + 𝔡₁. The
integers that are roots, of some type, are exactly the integers other than 1 and 2.

(b) Every indicial root of (□^Υ_b)^(0) is a pole of order one of N(ρ⁻²(□^Υ_b)^(0), ·)⁻¹. The two roots 2 + 𝔡₀ (type s0)
and 2 + 𝔡₁ (type s1) are roots of no other type. 0 < d₂(l) < d₁(l) ≤ δ′₁ < 𝔡₀ < 1.34·10⁻⁶ for every l ≥ 1.

(c) The parity φ, the pullback by x ↦ −x, acts on the scalar, vector and tensor types of degree l by (−1)^l,
(−1)^(l+1) and (−1)^l. So s0, s2 and v1 are even, s1, s3 and v2 odd.

*Proof.* (a) By [[lem:iii-d-4-1]], which does not depend on b ([[lem:iii-d-2-1]] (3)), the roots are 1 − ι^Υ_(s0,2),
0, ι^Υ_(s0,2), 3 at s0; 1 − ι^Υ_(sl,l+2), 1 − ι^Υ_(sl,l+1), 1 − l, ι^Υ_(sl,l+1), ι^Υ_(sl,l+2), l + 3 at sl; −l, l + 2
at vl. Those of positive real part are ι^Υ_(s0,2), 3, ι^Υ_(sl,l+j), l + 3 and l + 2, which is R; by [[eq:iii-d-4-2]]
the least is ι^Υ_(s1,2). The integer roots are 3, l + 3, l + 2 (all integers ≥ 3), 0, 1 − l and −l (all integers
≤ 0).

(b) The indicial family of A := ρ⁻²(□^Υ_b)^(0) commutes with the rotations ([[lem:iii-d3-2-1]], proof), so it acts on
each isotypic component as a matrix N_τ(ι) ⊗ Id. Each root is a simple zero of det N_τ at each type τ at which it is a
root ([[lem:iii-d-4-1]]), so N_τ⁻¹ has at most a simple pole there. The Laurent coefficients of N(A, ·)⁻¹, which is
meromorphic ((E2) of [[sec:iii-a-1-1]]), commute with the projections onto the types, and the coefficient of
(ι − ι₁)^(−2) vanishes on every type; so it vanishes. 2 + 𝔡₀ ∈ (2, 2 + z/3] and 2 + 𝔡₁ lie in (2, 3), where by (a)
the only roots are 2 + 𝔡₀ and 2 + 𝔡₁, and 𝔡₁ < 𝔡₀ ([[eq:iii-d-4-2]]). By [[eq:s14-theta]],
d₂(l) = z(u − 1)(1 + θ₂)/(2u(2u − 1)) and d₁(l) = z(u + 1)(1 + θ₁)/(2u(2u + 1)) with |θ₁|, |θ₂| ≤ z, and
(u + 1)/(2u(2u + 1)) ≤ 3/20 at u ≥ 2, so d₁(l) ≤ (3z/20)(1 + z) < 6.1·10⁻⁷ < 𝔡₀ by [[lem:is-offsets]], d₁(1) = δ′₁
being the largest, as (u + 1)/(u(2u + 1)) ≤ 4/21 < (3/10)(1 − z)/(1 + z) for u ≥ 3 and |θ₁| ≤ z; d₂ < d₁ is
[[prop:np-10-52]] (i).

(c) A scalar harmonic of degree l is the restriction of a homogeneous harmonic polynomial of degree l, so S(−ω) =
(−1)^l S(ω); in the splitting (a S dx̄⁰ + b S dx̄¹ + c r d_𝕊S), dx̄⁰ and dx̄¹ are invariant, as t̄ and r are, and
φ(d_𝕊S) = d_𝕊(S ∘ (−1)) = (−1)^l d_𝕊S. The Cartesian components of r V, V ∈ 𝒱_l, are r^(−l) times harmonic polynomials
of degree l ([[prop:np-10-12]]), and φ(Σ f_i dx^i) = −Σ f_i(−x) dx^i, which gives (−1)^(l+1). A tensor harmonic of
degree l has components of degree l in two factors dx^i, which gives (−1)^l. ∎

**Lemma {#lem:is-offsets}** (Closed forms and enclosures.) (a) For l ≥ 1 put D_l := 4(l + 1)²·250000² + 1000001. Then

    d₂(l) = ½((1 + 4(l + 1)² + 2z − D_l^(1/2)/125000)^(1/2) − (2l + 1)),
    d₁(l) = ½((1 + 4(l + 1)² + 2z + D_l^(1/2)/125000)^(1/2) − (2l + 3)),     𝔡₀ = (562501^(1/2) − 750)/500.

In particular 𝔡₁ = ½(I^(1/2) − 3), δ′₁ = ½(I′^(1/2) − 5) and δ₂ = ½(I₂^(1/2) − 5), with D := D₁ = 1000001000001,
D₂ = 2250001000001, I := 17 + 2z − D^(1/2)/125000, I′ := 17 + 2z + D^(1/2)/125000, I₂ := 37 + 2z − D₂^(1/2)/125000.

(b) Squaring the decimal numbers on the left,

    750.000666666370370633744563329125² = 562500.9999999999999999999999999999530983670876…,
    750.000666666370370633744563329126² = 562501.0000000000000000000000000014530997004203…,
    1000000.500000374999812500023437² = 1000001000000.9999999999999999988828120527…,
    1000000.500000374999812500023438² = 1000001000001.0000000000000000008828130527…,
    1500000.333333629629563785993598² = 2250001000000.9999999999999999983408013448…,
    1500000.333333629629563785993599² = 2250001000001.0000000000000000013408020115…,

so 562501^(1/2), D^(1/2) and D₂^(1/2) lie strictly between the two numbers squared. Dividing by 125000 (multiplying by
8·10⁻⁶) and adding 17.000008, resp. 37.000008, gives

    9.000003999997000001499999812496 < I < 9.000003999997000001499999812504,
    25.000012000002999998500000187496 < I′ < 25.000012000002999998500000187504,
    25.000005333330962963489712051208 < I₂ < 25.000005333330962963489712051216,

and squaring again,

    3.000000666666092592970164438971² = 9.0000039999970000014999998124947498659…,
    3.000000666666092592970164438973² = 9.0000039999970000014999998125067498686…,
    5.000001200000155999812560061301² = 25.000012000002999998500000187490088641…,
    5.000001200000155999812560061303² = 25.000012000002999998500000187510088645…,
    5.000000533333067851932844769680² = 25.000005333330962963489712051203683886…,
    5.000000533333067851932844769682² = 25.000005333330962963489712051223683888…,

each below the lower or above the upper bound of the square that it brackets. Hence

    1.333332740741267489126658250·10⁻⁶ < 𝔡₀ < 1.333332740741267489126658252·10⁻⁶,
    3.333330462964850822194855·10⁻⁷ < 𝔡₁ < 3.333330462964850822194865·10⁻⁷,
    6.000000779999062800306505·10⁻⁷ < δ′₁ < 6.000000779999062800306515·10⁻⁷,
    2.666665339259664223848400·10⁻⁷ < δ₂ < 2.666665339259664223848410·10⁻⁷,

and ε₀ := 𝔡₀ − 4𝔡₁ satisfies 5.55555327160248712250·10⁻¹³ < ε₀ < 5.55555327160248716252·10⁻¹³.

(c) 1, 𝔡₀ and 𝔡₁ are linearly independent over ℚ.

*Proof.* (a) By [[prop:np-10-52]] (i), 1 + 4s_± = (2u ± 1)² + 2z ± 4w with w = (u² + z + z²/4)^(1/2) − u, so
(2u ± 1)² + 2z ± 4w = 1 + 4u² + 2z ± 4(u² + z + z²/4)^(1/2), and 4(u² + z + z²/4)^(1/2) = (16u² + 16z + 4z²)^(1/2) =
D_l^(1/2)/125000, as 125000²(16u² + 16z + 4z²) = 4u²·250000² + 1000000 + 1 = D_l with z = 1/250000. Then
d₂ = ½((1 + 4s_−)^(1/2) − (2u − 1)) and d₁ = ½((1 + 4s_+)^(1/2) − (2u + 1)). And 9/4 + z = 562501/250000.
(b) is exact arithmetic on the printed numbers; 𝔡₀ is the bracket of 562501^(1/2) minus 750, divided by 500.
(c) If r𝔡₀ + s𝔡₁ = t with r, s, t ∈ ℚ and s ≠ 0, then I^(1/2) ∈ ℚ(562501^(1/2)), so I ∈ ℚ(562501^(1/2)) ∩ ℚ(D^(1/2)).
3 divides D = 3·333333666667 exactly once (the digit sum of the cofactor is 55) and does not divide 562501 (digit
sum 19), so 562501·D is not a square and the two quadratic fields differ; their intersection is ℚ, so D^(1/2) ∈ ℚ,
which is false, as 3 ∥ D. If s = 0 and r ≠ 0, then 562501^(1/2) ∈ ℚ, false as 750² < 562501 < 751². ∎

#### Two counting rules {#sec:is-rules}

**Lemma {#lem:is-count}** (Logarithmic orders of the constructed index sets.) (a) In [[lem:iii-a-1-4]],

    ℓ̂_E(w) = Σ_(j≥0) (ℓ̂_F(w − j) + ℓ̂_(E(α))(w − j))     for every w ∈ ℂ.                               {#eq:is-l1}

(b) In [[lem:iii-a-1-5]], k(E, w) is the largest value of k + Σ_(q=0)^(w−ι) ord(ι + q) over (ι, k) ∈ F with
w − ι ∈ ℕ₀.

(c) For A = ρ⁻²(□^Υ_b)^(0), ℓ̂_(E(α))(w) = 1 if Re w > α and w ∈ r + ℕ₀ for a root r with Re r > α, and 0 otherwise;
and ord(w) = 1 if w is a root and 0 otherwise.

*Proof.* (a) For index sets, k(X ∪̄ Y, w) = k(X, w) + k(Y, w) + 1 when w lies in both projections, by the definition of
the extended union ([[def:s11-b-analysis]] (4)), and it is the order of the one that contains w otherwise; so
ℓ̂_(X∪̄Y) = ℓ̂_X + ℓ̂_Y. With g := ℓ̂_F + ℓ̂_(E(α)), the definitions give ℓ̂_(E₀) = g and ℓ̂_(E_(k+1))(w) = g(w) +
ℓ̂_(E_k)(w − 1), so ℓ̂_(E_k)(w) = Σ_(j≤k) g(w − j), which increases in k and is constant once w − k − 1 lies below the
least real part of F ∪ E(α). The union E has the supremum. (b) is the definition of E there. (c) The poles of
N(A, ·)⁻¹ are the roots, all of order one ([[lem:is-roots]] (b)), so Spec_b(A) consists of the (r, 0), and E(α) is the
union of the r + ℕ₀ with Re r > α, all of order 0. ∎

The rule [[eq:is-l1]] counts the translates by ℕ₀ of the right side's own exponents as meetings with the right side,
so that the orders of the constructed sets grow with the distance from the leading order even where no root is met.
The bounds below are those of the sets as constructed.

#### The exponents of ℰ_ind {#sec:is-ind}

ℰ_ind is the union ([[sec:uc-index-sets]]) of the index sets of: (c1) the corrections of the translations and
rotations, (F1) of the proof of [[prop:iii-d2-3-1]] with k = 2, leading order m = 2, right side F = (2, 0); (c2) the
correction of the boosts, (F1) with k = 1, m = 1, F = (1, 0) ∪ (E_(c1) − 1), as f̆_b contains [□^Υ_b, t_*]ω′_b;
(c3) ω̇_b(1, 0) and (c4) ω̇_b(0, Ȧ), [[lem:iii-f3-2-1]] with k = 1 and k = 2; (c5) the steps of the proof of
[[prop:iii-d3-3-1]] (1)–(7), each [[lem:iii-d3-2-1]] at a leading order m; (c6) (2, 0). The tensors built from these
(δ* of them, dt_* ⊗_s of them, and ġ^Υ_b) carry the same index sets shifted by 1, as b-derivatives do not raise
logarithmic orders. The leading orders in (c5) are m = 1 (the first step of (1)), m = −k (the later steps of (1) and
(2), k = 2, 3, 4), m = −k − 1 ((3), k = 1, 2, 3), and m = μ + 2 and m = μ − k (1 ≤ k ≤ K) for the class roots μ of
[[prop:np-10-30]] (iv): μ_s0 = −1 − 𝔡₀, μ_(l,0) = −l − d₂(l), μ_(l,1) = −l − 1 − d₁(l) (l = 1, 2, 3, K = 2), 1 − l
(2 ≤ l ≤ 5, K = 5 − l) and −l (2 ≤ l ≤ 4, K = 4 − l). Put

    M* := {2, 1 − 𝔡₀, 1 − 𝔡₁, −δ′₁, −δ₂, −1 − d₁(2), −1 − d₂(3), −2 − d₁(3)}.

**Proposition {#prop:is-ind}** (The exponents of ℰ_ind.) For ℰ_ind as constructed, at every b near b₀,

    π_1ℰ_ind = ℕ ∪ ⋃_(m∈M*) ((R − m) + ℕ₀),                                                            {#eq:is-ind}

where R − m := {r − m : r ∈ R}. Its exponents of real part at most 5 are the numbers n + f ≤ 5 with n ≥ n_f, f and
n_f as follows: f = 0, n_f = 1; f = 𝔡₀ or 𝔡₁, n_f = 0; f = δ′₁, δ₂, 2𝔡₀, 2𝔡₁ or 𝔡₀ + 𝔡₁, n_f = 1; f = d₁(2), d₂(3),
𝔡₀ + δ′₁, 𝔡₁ + δ′₁, 𝔡₀ + δ₂ or 𝔡₁ + δ₂, n_f = 2; f = d₁(3), d₂(4), 2δ′₁, 2δ₂, δ′₁ + δ₂, 𝔡₀ + d₁(2), 𝔡₁ + d₁(2),
𝔡₀ + d₂(3) or 𝔡₁ + d₂(3), n_f = 3; f = d₁(4), d₂(5), δ′₁ + d₁(2), δ′₁ + d₂(3), δ₂ + d₁(2), δ₂ + d₂(3),
𝔡₀ + d₁(3), 𝔡₁ + d₁(3), 𝔡₀ + d₂(4) or 𝔡₁ + d₂(4), n_f = 4. Those of real part at most 3/2 are

    𝔡₁ < 𝔡₀ < 1 < 1 + δ₂ < 1 + 𝔡₁ < 1 + δ′₁ < 1 + 2𝔡₁ < 1 + 𝔡₀ < 1 + 𝔡₀ + 𝔡₁ < 1 + 2𝔡₀.                    {#eq:is-low}

*Proof.* *Each construction.* By [[lem:is-roots]] (a), every root of real part above a weight α ≥ 0 is in R, and
E(α) = R + ℕ₀ for every α ∈ [0, ι^Υ_(s1,2)), as ι^Υ_(s1,2) is the least element of R; in (F1), [[lem:iii-f3-2-1]] and
the step u₂ of [[lem:iii-d3-2-1]] the weights lie there (in (k − ε_Υ, k), k = 1, 2, in (0, k), and just below
ι^Υ_(s1,2)). By [[eq:is-l1]], π_1E = (π_1F + ℕ₀) ∪ (R + ℕ₀) in (F1) and [[lem:iii-f3-2-1]], and in
[[lem:iii-d3-2-1]] the solution u₀ + χ_∂u₁ + u₂ has the exponents m, those of ℱ₁ + ℕ₀ (u₁, by [[lem:iii-a-1-5]]), and
those of (𝒢 + ℕ₀) ∪ (R + ℕ₀) with 𝒢 ⊂ π_1ℱ₁ + ℕ₀ (u₂). So every exponent of a construction at leading order m is m + j,
an exponent of its right side plus j, or r + j (r ∈ R, j ∈ ℕ₀). The right sides: in (c1), (c3), (c4), the first step
of (1) and the first step of each class, they are smooth with exponents m + ℕ₀ (ρ⁴C^∞, ρ³C^∞, ρ⁴C^∞, ρ³C^∞ and
ρ^(μ+4)C^∞ divided by ρ²); in (c2), m + ℕ₀ and E_(c1) − 1; at a later step at the order m, the exponents of the step
before minus 1 (the term A₁, which raises the order by one, divided by ρ²) and of the step two before (A₂ ∈ ρ²C^∞,
divided by ρ²), together with m + ℕ₀ (u₀ and A − N(A)). Relative to its own leading order a later step inherits the
exponents of the earlier steps relative to theirs, shifted by 0 or by an integer, as the leading orders differ by
integers. Hence every offset z − m is a non-negative integer or r − m′ + j with r ∈ R, j ∈ ℕ₀ and m′ the leading
order of a first step: 2, 1 or μ + 2 with μ a class root, or the integer leading orders of the first steps of the
integer classes. As r − m′ + j = r − 2 + (j + 2 − m′) for integer m′ ≤ 2, and the non-integer μ + 2 are the elements
of M* ∖ {2} (μ_s0 + 2 = 1 − 𝔡₀, μ_(1,0) + 2 = 1 − 𝔡₁, μ_(1,1) + 2 = −δ′₁, μ_(2,0) + 2 = −δ₂, μ_(2,1) + 2 = −1 − d₁(2),
μ_(3,0) + 2 = −1 − d₂(3), μ_(3,1) + 2 = −2 − d₁(3)), π_1ℰ_ind ⊂ [[eq:is-ind]].

*Equality.* (c1) contains every r ∈ R with its translates, so π_1ℰ_ind ⊃ (R − 2) + ℕ₀; the first step of the class μ,
at m = μ + 2, contains R + ℕ₀ (u₂), so π_1ℰ_ind ⊃ (R − m) + ℕ₀ for m ∈ M* ∖ {2}; and the integers: E_(c1) contains
(2 + j, 2j) for every j ∈ ℕ₀ ([[prop:is-logs]] (a), proof), so (j, 2j) ∈ ℰ_ind for every j ≥ 1. All of this holds at
every b, as the roots do not depend on b.

*The list.* By [[def:is-roots]], R ∩ {Re ≤ 7} consists of 2 + 𝔡₀, the l + 1 + d₂(l) (l ≤ 5), the l + 2 + d₁(l)
(l ≤ 4) and 3, …, 7. Writing r = n_r + f_r, r − m for m = 2, 1 − 𝔡₀, 1 − 𝔡₁, −δ′₁, −δ₂, −1 − d₁(2), −1 − d₂(3),
−2 − d₁(3) is (n_r − 2) + f_r, (n_r − 1) + f_r + 𝔡₀, (n_r − 1) + f_r + 𝔡₁, n_r + f_r + δ′₁, n_r + f_r + δ₂,
(n_r + 1) + f_r + d₁(2), (n_r + 1) + f_r + d₂(3), (n_r + 2) + f_r + d₁(3). Keeping those of real part at most 5 and the
least integer part for each f gives the table. The order [[eq:is-low]] follows from [[lem:is-offsets]] (b) and
δ₂ < 𝔡₁ < δ′₁ < 2𝔡₁ < 𝔡₀ < 𝔡₀ + 𝔡₁ < 2𝔡₀. ∎

**Proposition {#prop:is-logs}** (Logarithmic orders.) (a) At the exponents [[eq:is-low]] of real part at most 3/2 the
logarithmic orders of ℰ_ind as constructed are 0, 0, 3, 0, 3, 0, 0, 3, 0, 0, in that order.

(b) Every exponent of ℰ_ind of real part at most 5 has logarithmic order at most 39, and (5, 39) ∈ ℰ_ind. At the
integers j = 1, …, 5 the boost correction (c2) has the orders j² + 3j − 1 = 3, 9, 17, 27, 39.

(c) The logarithmic orders of ℰ^ι_ind are at most 3 at real part at most 3/2 and at most 50 at real part at most 5.

*Proof.* (a) and the exact values. (c1): F = (2, 0), E(α) = R + ℕ₀. At w = 2 + j, [[eq:is-l1]] counts j + 1 terms of F
(at 2, …, 2 + j) and j of E(α) (at 3, …, 2 + j), so k = 2j; at a non-integer w of real part 2 + t no term of F and
at most ⌊t⌋ + 1 terms of E(α) (those of real part at least 2 + 𝔡₁) enter, so k ≤ ⌊t⌋. At w = 3 + 𝔡₀, 3 + 𝔡₁ the terms
are w and w − 1, so k = 1; at 2 + 𝔡₀, 2 + 𝔡₁, 3 + δ′₁ and 3 + δ₂ only w itself, as no root of real part below 3
other than 2 + 𝔡₀ and 2 + 𝔡₁ is positive and 𝔡₀, 𝔡₁, δ′₁, δ₂ are distinct ([[lem:is-offsets]] (b)), so k = 0. (c4)
is (c1). (c3): F = (1, 0); at 1 + j the count is j + 1 + (j − 1)₊, so k = j + (j − 1)₊; at 2 + 𝔡₀, 2 + 𝔡₁, k = 0.
(c2): F = (1, 0) ∪ (E_(c1) − 1), so ℓ̂_F(1 + i) = 2i + 1 for i ≥ 1 and ℓ̂_F(1) = 1; at 1 + j,

    ℓ̂ = 1 + Σ_(i=1)^j (2i + 1) + (j − 1)₊ = j² + 2j + 1 + (j − 1)₊,     k = j² + 3j − 1 (j ≥ 1);

at 2 + 𝔡₁ the count is ℓ̂_F(2 + 𝔡₁) + ℓ̂_F(1 + 𝔡₁) + 1 = 2 + 1 + 1, so k = 3, and likewise at 2 + 𝔡₀; at 1 + 𝔡₀, 1 + 𝔡₁,
2 + δ′₁ and 2 + δ₂, ℓ̂_F = 1 and no root lies at or below, so k = 0. The classes: at m = 1 − 𝔡₀ the exponent 2 + 𝔡₀ comes
from u₂ alone, with no term of 𝒢 ⊂ {Re ≥ 3} below it, so k = 0; the same at 2 + 𝔡₁ for m = 1 − 𝔡₀ and m = 1 − 𝔡₁, and at
2 + 𝔡₀ for m = 1 − 𝔡₁. The two steps at m = 1, the first step of (1) and that of the class 1 − l at l = 2, have order 0
at the offsets 1, 1 + 𝔡₀ and 1 + 𝔡₁: the exponent 2 comes from u₁ alone, of order 0 by [[lem:is-count]] (b), as 1 and 2
are not roots ([[lem:is-roots]] (a)), and 2 + 𝔡₀ and 2 + 𝔡₁ come from u₂ alone, as for the classes. At the integer offset
1 of a step at m ≤ 0 the exponent m + 1 comes from u₁ alone; for the class first steps with m ∈ {0, −1, −2} this gives at
most ord(m + 1) ≤ 1, and for the later steps the order is that of the step before at offset 1 plus ord(m + 1) ≤ 1, which
along a chain of at most three later steps starting from order 0 gives at most 3. So the largest order at real part at
most 3/2 is 3, at 1, 1 + 𝔡₁ and 1 + 𝔡₀, and (a) follows, the other exponents of [[eq:is-low]] having order 0.

(b) *A step bound.* Let a step of [[lem:iii-d3-2-1]] at the order m have a right side of order at most k_R at offsets
of real part at most t ≤ 5. By [[lem:is-count]] (b), u₁ has order at most k_R + ⌊t⌋ + 1 there, as a ladder of length
at most t carries at most ⌊t⌋ + 1 roots. u₂ has exponents only at real part at least 2 + 𝔡₁, and by [[eq:is-l1]] at
most p(k_R + ⌊t⌋ + 2) + p′ − 1, with p ≤ ⌊m + t⌋ − 2 the number of terms of 𝒢 ⊂ {Re ≥ 3} and
p′ ≤ ⌊m + t − 2 − 𝔡₁⌋ + 1 that of E(α) ⊂ {Re ≥ 2 + 𝔡₁} on the ladder below. For m ≤ −2 this is p ≤ 1 (only the
exponent 3) and p′ ≤ 1, so the step has order at most k_R + ⌊t⌋ + 2 ≤ k_R + 7. For a first step (k_R = 0) it is at
most 11 at m ∈ (0, 1], t ≤ 3, at most 5 at m ∈ (−1, 0], t ≤ 3, and at most 31 at t ≤ 5.

*The chains.* (c1), (c3), (c4): 2j ≤ 10 and j + (j − 1)₊ ≤ 9 at the integers j ≤ 5, and at a non-integer offset t ≤ 5
of (c1) or (c4) at most ⌊t⌋ ≤ 4, by the count in (a). (c2): j² + 3j − 1 ≤ 39 at j ≤ 5, the value 39 at 6 = 1 + 5. At a
non-integer exponent 1 + t of (c2), t ≤ 5, the ladder carries terms of F at the at most ⌊t⌋ + 1 points 1 + t − i with
t − i ≥ 0, each with ℓ̂_F ≤ ⌊t − i⌋ + 1 by the bound k ≤ ⌊t⌋ of (c1), and at most ⌊t⌋ terms of E(α); so the order is at
most (⌊t⌋ + 1)(⌊t⌋ + 2)/2 + ⌊t⌋ − 1 ≤ 18. At a non-integer exponent 1 + t of (c3) only terms of E(α) enter, at most
⌊t⌋, so the order is at most 3. The first steps of the classes, (4)–(7): at most 31. The s1 tower: the step k = 2
inherits from the boost at offsets t − 2 ≤ 3, of order at most 17, and from the translation at t − 4 ≤ 1, so it has
order at most 24; then 31 and 38. The s0 tower: the first step has order at most 11 at offsets ≤ 3, which the step
k = 2 inherits at t − 2, so 18, 25, 32. The v1 tower: the rotation correction at offsets ≤ 2 has order at most 4,
inherited at t − 3, so 11, 18, 25. The class companions inherit the first step at offsets ≤ 3 (at most 11), so at most
18, 25, 32. All are at most 39.

(c) ℰ^ι_ind collects the index sets of the states of [[ch:s13]] and [[ch:s15]], 2 + ℕ₀ and (2, 1) ([[thm:iii-g2-4-2]]).
The states of [[ch:s13]] and ġ^Υ_b are the constructions above. The physical states of [[prop:iii-f4-5-1]], relative to
−2: h^(−2)_b − χh̄ has the offsets 1 (from (−1, 0), order 0) and 1 + (offsets of h̆²_(b,s1), h̆¹_(b,v1)), each at least
2; h′_(b,1) from (0, 0) by [[lem:iii-a-1-5]] (order at most 3 at offsets ≤ 5, the integer roots of L̂_b(0) in [0, 3]
being 0, 2, 3, each simple ([[prop:is-mult]]), and a ladder from 0 meeting no other root); h_(b,(0)) from the
exponent 0 of order k₀ ≤ 2 (the order of h̆²_(b,s1) and h̆¹_(b,v1) at the exponent 0, which comes from the first step
of the s1 and v1 towers at offset 1, at most 2), so of order at most 5; and u_b, by [[lem:iii-a-1-4]] with E(α) the
roots of L̂_b(0) of positive real part and F the exponents of positive real part of the other terms. At an exponent w
of u_b of real part at most 3 at most three terms w, w − 1, w − 2 of positive real part enter [[eq:is-l1]]. At a
real w each term of F has order at most 15 (h̆²_(b,s1) at offsets ≤ 4: the boost at offsets ≤ 2, order 9, and the
step k = 2 of the s1 tower at offsets ≤ 4, order at most 9 + 6), and each term of E(α) order 0, as the real roots of
L̂_b(0) of real part at most 3 are simple ([[prop:is-mult]]); so u_b has order at most 3·16 + 3 − 1 = 50 there. At
real part at most 3/2 (relative to −2: offsets ≤ 3/2) only the offset 1, of order 0, occurs. The exponents ι + 1 + j
of [[prop:is-iota]], that is w = ι − 1 + j for u_b, carry no term of F on their ladder, since ι is non-real or a real
number more than 2.93·10⁻⁶ from ℤ, while every exponent of F is real and within 1.34·10⁻⁶ of ℤ ([[lem:is-roots]] (b):
the exponents of the s1 and v1 towers and of h_(b,(0)) are integers plus at most one of 𝔡₀, d₂(l), d₁(l)). As every
root of L̂_b(0) of positive real part has real part greater than 1 ([[prop:iii-f1-2-3]] (a)), the terms of E(α) on
their ladder lie at w and w − 1 only, with ℓ̂_(E(α)) at most the largest order of a pole of N(L̂_b(0), ·)⁻¹ at w or
w − 1, resp. at w − 1. These poles are simple, w and w − 1 lying in the strip −101 ≤ Re ≤ 5 ([[prop:is-mult]]), as
1 < Re w ≤ 3; so [[eq:is-l1]] gives ℓ̂ ≤ 1 + 1 at w, and the order at ι + 1 + j is at most 1. ∎

#### The other index sets {#sec:is-others}

**Proposition {#prop:is-iota}** (The exponents of ℰ^ι_ind.) Let Z be the set of the roots ι of C (with ι > 2), of
P_l (l ≥ 1, Re ι > 19/10, ι ≠ 2) and of p_(v) (l ≥ 2, the larger root) of [[prop:np-10-12]] at (v, e, h) =
(1/2, 1/102400, 10⁻⁶). The exponents of ℰ^ι_ind of real part at most 5, as constructed, are those of ℰ_ind, together
with the integers 1, …, 5 and the numbers ι + 1 + j of real part at most 5 (ι ∈ Z, j ∈ ℕ₀). Every ι ∈ Z has real
part greater than 2; no ι ∈ Z of real part at most 6 is an integer, and every real one of real part at most 6 has
distance from ℤ greater than 2.93·10⁻⁶. At b₀ the physical states have types s2, v2 and t2 only, and the numbers ι + 1
that they meet are those of the three roots of P₂ in (2 + 2.93h, 2 + 2.94h), (2 + 8h, a(8h)) and (a(8h), 3 − δ_C) of
[[lem:s14-sextic-small]] (b), and of the root (250002000009)^(1/2) − 499999 = 3.00000499998… of p_(v) at l = 2.

*Proof.* The states entering [[thm:iii-g2-4-2]] are those of [[def:iii-g2-table-1-1]] and the s1 and v1 terms; their
index sets are those of [[sec:is-ind]] except the classes μ_(3,1), 1 − l at l = 5 and −l at l = 4, which no row uses.
These add no exponent of real part at most 5. By the proof of [[prop:is-ind]] their offsets are positive integers and
the elements of (R − m) + ℕ₀, with m = −2 − d₁(3) for μ_(3,1) and m = −2 for the two integer classes. For
m = −2 − d₁(3) those of real part at most 5 are 5 + d₁(3) and 4 + 𝔡_i + d₁(3) (i = 0, 1), which the first steps at
m = 2, 1 − 𝔡₀ and 1 − 𝔡₁ give with r = 5 + d₁(3) ∈ R; for m = −2 the set is R + 2 + ℕ₀ ⊂ (R − 2) + ℕ₀. The physical
states add, relative to −2, the integer offsets and the numbers r + 2 for the roots r of L̂_b(0) of positive real part
at most 3 ([[prop:iii-f4-5-1]], Step 3), with their translates; by [[prop:iii-f1-2-3]] these are 2, 3 and the
ι^C_(·,+) − 1 = ι − 1, ι ∈ Z, each of real part greater than 1 ([[prop:iii-f1-2-3]] (b)). By [[prop:np-10-54]] (ii)
every ι ∈ Z has Re ι > 2. A real ι ∈ Z with ι ≤ 51 has |ι − 1| ≤ 50, so by [[prop:s14-damping-distance]] its distance
from ℤ exceeds 2.93·10⁻⁶ unless ι ∈ ℤ. And no ι ∈ Z with Re ι ≤ 6 is an integer: for C and P_l this is
[[prop:s14-damping-distance]]; for p_(v), ι = n ∈ {3, …, 6} would need (l + 1)² = k² + 10⁶(k − 2) with
k = n − 1 ([[lem:s14-vector-distance]], proof), which for k = 2 gives l = 1, excluded, and for k = 3, 4, 5 fails, as
1000009, 2000016 and 3000025 lie strictly between 1000² and 1001², 1414² and 1415², 1732² and 1733². 2 + ℕ₀ and
(2, 1) are integers. At b₀ the types are those of [[prop:iii-f4-5-1]], and the roots are those cited; at l = 2,
(Γ + 9)^(1/2) − 499999 with Γ = 250002000000 is the larger root of p_(v) by [[lem:s14-vector-distance]]. ∎

**Proposition {#prop:is-mult}** (The multiplicities of the roots of L̂_b(0).) Every indicial root of L̂_b(0) has
multiplicity at most 7 at each type and degree at which it occurs. Every one of real part in [−101, 5] is a simple root
of each type and degree at which it occurs. So N(L̂_b(0), ·)⁻¹ has poles of order at most 7, and simple poles on the
strip −101 ≤ Re ≤ 5. (Whether P_l has a root of real part at most 6 for some l with hκ > 70, κ = l(l + 2), is not
decided here; such a root would be non-real and simple.) Whether the roots of real part below −101 (the
ι^C_(·,≪) − 1 and the gauge roots −l, 1 − l, 2 − l, 2 − ι^Υ of large degree) are simple at h = 10⁻⁶ is not decided
here ((C2)–(C3) of [[sec:iii-f1-1]] are proved for h ∈ 𝖧, which does not contain 10⁻⁶).

*Proof.* *The bound 7.* [[prop:iii-f1-2-3]] assumes z ∈ (0, ½], true for z = 4·10⁻⁶, and (C1), which holds at
h = 10⁻⁶: the indicial roots of □^C_b at scalar type l ≥ 1, scalar type 0 and vector type l are the roots of P_l, P_0
and p_(v) ([[prop:np-10-12]] (ii), (iii), with h = 1/γ_C), and by [[prop:np-10-54]] (i), (ii), every root of C, P_0,
P_l and p_(v) has real part at least 2 or below −100 = −C_0, the only one of real part 2 is the root 2 at l = 0 and
at l = 1, simple there, and the numbers of roots on the two sides are those that (C1) states. By (a) and (b) of
[[prop:iii-f1-2-3]], at each type and degree no root has real part in (0, 1], and n_L ≤ 7 roots, counted with
multiplicity, have real part at most 0 and n_L real part above 1; so every root has multiplicity at most 7 there.

*The poles.* The indicial family N(L̂_b(0), ·) of ρ⁻²L̂_b(0) is that of the model ([[lem:iii-f-2-1]] (3)) and commutes
with the rotations; on each isotypic component it acts as the type's indicial matrix tensored with the identity
([[sec:iii-f1-1]], [[sec:iii-f1-2]]), and the inverse of that matrix is its adjugate divided by its determinant. So, as
in the proof of [[lem:is-roots]] (b), the pole of N(L̂_b(0), ·)⁻¹ at a root has order at most the largest multiplicity
of the root at a type and degree.

*The strip.* By [[prop:iii-f1-2-3]] (list and proof) the roots of each type are, with multiplicity, −l, l + 2, the roots
of (□^Υ_b)^(0) plus 1 and the roots of □^C_b minus 1, less those of D. Those from □^Υ_b and the integers are distinct
within each type (the disjoint intervals of the proof of (e) there). The roots ι^C − 1 of real part in [−101, 5] that
come from □^C_b are the ι − 1 with ι ∈ Z and Re ι ≤ 6, as by [[prop:np-10-54]] (i) the other roots of C, P_l and p_(v)
have real part below −100. Such an ι is a simple root of its polynomial: of C, as the other two roots have real part
below −100; of p_(v), as its two roots are real and of opposite signs; of P_l with hκ ≤ 70, as the three roots
in |ι| < 1000 have real part at least 2, are all of them, counted with multiplicity ([[lem:s14-sextic-small]],
[[lem:s14-sextic-large]], [[lem:s14-sextic-count]] (a)), and are distinct, so that they are the three roots of real part
above 19/10, each simple. Those lemmas place the three in disjoint sets, except for 0.018 ≤ x ≤ 0.03, x := hκ
(134 ≤ l ≤ 172), where two of them lie in one disc |ι − ξ_x| < 0.45, ξ_x := (3x + 10)/4 ([[lem:s14-sextic-large]] (b));
these two are distinct. Indeed P_l = U + (P_l − U) with U(ι) := (2 + x − ι)(2(ι − ξ_x)² − Δ(x)/8) and
Δ(x) := x² − 1715x/8 + 4, whose smaller root x₋ lies in (0.01866, 0.01867) ([[lem:s14-sextic-split]] (i), (iii): U is
the cubic there, its quadratic factor written with the square completed, and Δ the discriminant of that factor). On the
closed disc |ι − ξ_x| ≤ 0.45, |P_l − U| < 9.4·10⁻⁵ (the majorant bound in the proof of [[lem:s14-sextic-large]] (b),
which holds on the closed disc by [[lem:s14-majorant]], as |ι| ≤ ξ_x + 0.45 ≤ 2.9725 < 2.98 there), and on its real
diameter 2 + x − ι ≤ x/4 − 0.05 ≤ −0.0425. If x < x₋, that is l = 134 or 135 (x = 0.018224, 0.018495), then Δ(x) is
0.093562114176, resp. 0.035476440025, so 0.035 < Δ(x) < 0.1, U(ξ_x) = (2 − x)Δ(x)/32 > 1.97·0.035/32 > 2·10⁻³, and
U(ξ_x ± 0.45) = (2 + x − ξ_x ∓ 0.45)(0.405 − Δ(x)/8) < −0.0425·0.39 < −0.016, as Δ(x)/8 < 0.0125.
Since |P_l − U| < 9.4·10⁻⁵ on the disc, P_l is negative, positive and negative at ξ_x − 0.45, ξ_x and ξ_x + 0.45, and
the two roots are real and separated by ξ_x. If x > x₋, that is l ≥ 136 and x ≥ 0.018768, then
Δ(x) ≤ Δ(0.018768) = −0.023037762176 < −0.023, Δ being decreasing on [0, 107], so 2(ι − ξ_x)² − Δ(x)/8 > 0.0028 and,
on the real diameter, U < −0.0425·0.0028 < −1.1·10⁻⁴ < −9.4·10⁻⁵: P_l has no real root in the disc, and the two roots
there are a non-real conjugate pair, P_l having real coefficients, so they are distinct. If hκ > 70, P_l has no root
with |ι − 1| ≤ 50 ([[lem:s14-sextic-count]] (b)); so a root ι ∈ Z of P_l with Re ι ≤ 6 is non-real, a real one having
19/10 < ι ≤ 6 and so |ι − 1| ≤ 5. It is simple: P_l has real coefficients, so ῑ ≠ ι is a root of the same
multiplicity m and the same real part, and P_l has three roots of real part above 19/10, counted with multiplicity
([[prop:np-10-54]] (i)); so 2m ≤ 3, and m = 1. So ι − 1 has at its type the multiplicity of ι in its polynomial,
unless it equals an entry from □^Υ_b or an integer entry of that type. A non-real ι − 1 equals neither, these being
real. The integer entries are excluded as ι ∉ ℤ ([[prop:is-iota]]). An entry from □^Υ_b is real and either an integer
or within 1.34·10⁻⁶ of ℤ ([[lem:is-roots]] (b)), while a real ι − 1 is more than 2.93·10⁻⁶ from ℤ ([[prop:is-iota]]).
With the poles, this gives the orders stated. ∎

**Proposition {#prop:is-ci-pp}** (The least ℰ^C_I and the least ℰ_++.) Put a := (1 − e_Υ)γ_Υ = 99/10000 and
γ := γ_Υ = 1/100, so σ_Υ = {0, a, γ, 2γ}, and let σ^(n) be the set of the sums of n elements of σ_Υ, with repetition.

(a) The least ℰ^C_I satisfying [[def:iii-c-3-1]] is {(1 + n/2 + c, 0) : n ≥ 2, c ∈ σ^(n)}, all of logarithmic order 0.
Its exponents of real part at most 5 are the 1 + n/2 + c ≤ 5 with 2 ≤ n ≤ 8; below 3 + ε_+ they are 2 + c with
c ∈ σ^(2) = {0, 0.0099, 0.01, 0.0198, 0.0199, 0.02, 0.0299, 0.03, 0.04}, 5/2 + c with
c ∈ σ^(3) = {0, 0.0099, 0.01, 0.0198, 0.0199, 0.02, 0.0297, 0.0298, 0.0299, 0.03, 0.0398, 0.0399, 0.04, 0.0499, 0.05,
0.06}, and 3.

(b) ℰ^♯_+ ∩ {Re < 2} = {(λ_♯, 0)}, and below 2λ_♯ = 3.0198 the least ℰ_++ is λ_♯ plus the sums of elements of
ℰ_ind ∪ ℰ^ι_ind ∪ {(0, 0)} of real part at most 1.5099: its exponents there are λ_♯ + p𝔡₀ + q𝔡₁ and
λ_♯ + t + p𝔡₀ + q𝔡₁ with t ∈ {1, 1 + δ′₁, 1 + δ₂} (p, q ∈ ℕ₀), of logarithmic order at most 3. Above 2λ_♯ its exponents
are λ_♯ plus the sums of exponents of ℰ_ind, ℰ^ι_ind and ℰ_+, and depend on the class through ℰ_+.

*Proof.* (a) Put T′ := {½ + s : s ∈ σ_Υ}. Condition (3) of [[def:iii-c-3-1]] asks x + y − 1 ∈ ℰ^C_I for x, y in
ℰ^tot_I = ℰ^C_I ∪ (1 + T′ + ℕ₀). In terms of U := π_1ℰ^C_I − 1 this asks U ⊃ T′ + T′ and U + T′ ⊂ U, U + U ⊂ U, with
U + 1 ⊂ U; the least such U is the set of sums of at least two elements of T′, which contains 1 = ½ + ½ and so is
closed under adding 1. Logarithmic orders enter neither condition, so they are 0. Condition (2), min Re > 3/2 + 2γ_Υ,
holds as the least element is 2. With n/2 + c the sum of n elements of T′, 1 + n/2 + c ≤ 5 forces n ≤ 8; below 3 + a
only n = 2, n = 3, and n = 4 with c = 0 occur, since n = 4 gives 3 + c, the least non-zero c is a, and n ≥ 5 gives at
least 7/2; and 3 + ε_+ < 3 + a. Listing σ^(2), σ^(3) in
units of 10⁻⁴ from {0, 99, 100, 200} gives the sets. (b) By [[eq:iii-i1-3-2]] with Ĕ_+ = ∅, ℰ^(♯,(1))_+ = {(λ_♯, 0)}
and the later rounds add elements of π_1ℰ^C_I, all at least 2. By the proof of [[lem:iii-i10-1-2]] (b), below 2λ_♯ the
least ℰ_++ is the least index set containing (λ_♯, 0) and closed under adding ℰ^ι_ind ∪ ℰ_ind; a sum with two
summands of real part at least 1 exceeds λ_♯ + 2 > 3.0198, and the summands of real part below 1 are 𝔡₀ and 𝔡₁, of order
0 ([[prop:is-ind]], [[prop:is-iota]]); the orders follow from [[prop:is-logs]] (a), (c). ∎

#### The set Λ below 3 + ε_+ {#sec:is-lambda}

**Proposition {#prop:is-lambda}** (Λ ∩ {Re ≤ 3 + ε_+}.) Let ℬ be the set of the 29 numbers

    λ_♯,   λ_♯ + 1 + δ′₁,   λ_♯ + 1 + δ₂,   2 + c (c ∈ σ^(2)),   5/2 + c (c ∈ σ^(3)),   3.

Then, for ε_+ < δ̄, Λ ∩ {Re ≤ 3 + ε_+} = {β + p𝔡₀ + q𝔡₁ ≤ 3 + ε_+ : β ∈ ℬ, p, q ∈ ℕ₀}. All its elements are real.

*Proof.* By [[def:iii-i10-1-1]], Λ is the set of g + w₁ + … + w_s and their conjugates, with g a generator and w_i
increments. Every generator and increment has real part at least λ_♯ > 3/2, resp. 𝔡₁ > 0, so below 3 + ε_+ only
generators below 3 + ε_+ and increments below 3 + ε_+ − λ_♯ < 1.5 enter, and all of these are real. The generators
there: π_1ℰ_++ gives λ_♯ plus increments ([[prop:is-ci-pp]] (b)); π_1𝒢 = {2} ∪ (2 + π_1ℰ_ind) + ℕ₀ gives 2 plus
increments; π_1ℰ^C_I gives 2 + c, 5/2 + c and 3 ([[prop:is-ci-pp]] (a)); λ_♯ and 3; and 2 + π_1ℰ_col ⊂ π_1𝒢 + ℕ₀.
The increments below 1.5 are those of [[eq:is-low]] ([[prop:is-ind]], [[prop:is-iota]]) and 1, each a sum of 𝔡₀, 𝔡₁,
1, 1 + δ′₁ and 1 + δ₂. A sum with an
increment of real part at least 1 added to a generator other than λ_♯ is at least 3, with equality only for 2 + 1;
added to λ_♯ it is λ_♯ + 1, λ_♯ + 1 + δ′₁ or λ_♯ + 1 + δ₂ plus 𝔡₀'s and 𝔡₁'s, and λ_♯ + 1 = 5/2 + a. Two such
increments give at least λ_♯ + 2. So every element below 3 + ε_+ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ, and each such sum lies
in Λ. ∎

#### The gap condition {#sec:is-gap}

**Lemma {#lem:is-reduction}** (The least excess.) Let y > 0, and let m(y) be the infimum of the positive numbers
p𝔡₀ + q𝔡₁ − y, p, q ∈ ℕ₀. Put n⁺ := ⌊y/𝔡₁⌋ and n⁻ := ⌊4y/𝔡₀⌋, and assume y/𝔡₁, 4y/𝔡₀ ∉ ℤ. For an integer n
with n⁻ < n ≤ n⁺ put θ_n := y − n𝔡₁ and p_n := ⌊θ_n/ε₀⌋ + 1. Then

    m(y) = min({(n⁺ + 1)𝔡₁ − y} ∪ {p_n𝔡₀ + (n − 4p_n)𝔡₁ − y : n⁻ < n ≤ n⁺, 4p_n ≤ n}),

each element of the second set lying in (0, ε₀] and the first equal to (n⁺ + 1 − y/𝔡₁)𝔡₁.

*Proof.* For p, q ∈ ℕ₀ put n := 4p + q; then p𝔡₀ + q𝔡₁ = n𝔡₁ + pε₀ with 0 ≤ p ≤ n/4, and every pair n, p with these
bounds occurs. Fix n. If n𝔡₁ > y, the least value above y is n𝔡₁ − y (p = 0), least for n = n⁺ + 1. If n𝔡₁ ≤ y,
that is n ≤ n⁺, the values exceed y exactly when pε₀ > θ_n ≥ 0, that is p ≥ p_n, and such a p with 4p ≤ n exists
exactly when 4p_n ≤ n; the least value is then p_nε₀ − θ_n ∈ (0, ε₀]. If 4p_n ≤ n, then θ_n < p_nε₀ ≤ nε₀/4, so
y < n(𝔡₁ + ε₀/4) = n𝔡₀/4 and n > n⁻. ∎

**Theorem {#thm:is-gap}** (The admissible ε_K.) For Λ of [[prop:is-lambda]] (ℰ_ind and ℰ^ι_ind as constructed), (G)
of [[def:iii-i10-1-3]] holds if and only if ε_K < μ_G, where

    μ_G := λ_♯ + 1109655𝔡₀ + 31682𝔡₁ − 3

satisfies [[eq:is-mu]]. The next smallest excesses are 2.3181480·10⁻¹⁴ (above 3, from λ_♯ + 1 + δ′₁) and
8.0959353·10⁻¹⁴ (from λ_♯ + 1 + δ₂); every other element of Λ ∪ (Λ + 𝔡₀) ∪ (Λ + 𝔡₁) lies outside (2, 2 + 4.2·10⁻¹³]
∪ (3, 3 + 4.2·10⁻¹³]. As μ_G < δ_50 = ε_ind and μ_G < ε_Υ for the admissible choice ε_Υ = 1.4619·10⁻¹⁰ of
[[lem:ec-gauge-gap]], the other conditions of [[def:iii-i10-1-3]] on ε_K leave every ε_K ∈ (0, μ_G) available for a
suitable ε_+, and ε_K = 1.6416·10⁻¹⁴ is admissible.

*Proof.* *The windows.* By [[prop:is-lambda]] every element of Λ below 3 + 10⁻⁸ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ. As 𝔡₀ and
𝔡₁ are increments, Λ + 𝔡₀ and Λ + 𝔡₁ lie in Λ, so the third window of (G) is contained in the first. An element in
(2, 2 + ε] with ε < 𝔡₁ has β ∈ {λ_♯, 2}, and β = 2 gives excess 0 or at least 𝔡₁; so β = λ_♯, with excess
p𝔡₀ + q𝔡₁ − y, y = 2 − λ_♯ = 0.4901. An element in (3, 3 + ε]
with β = 3 has excess at least 𝔡₁ unless p = q = 0, when it is 3; with β = 2 + c, c ∈ σ^(2), excess
p𝔡₀ + q𝔡₁ − (1 − c); with β = 5/2 + c, p𝔡₀ + q𝔡₁ − (1/2 − c); with β = λ_♯, y = 1.4901; with β = λ_♯ + 1 + δ′₁ or
λ_♯ + 1 + δ₂, y = 0.4901 − δ′₁ or 0.4901 − δ₂. So the least excess is the least m(y) over the 28 numbers y = 1 − c
(c ∈ σ^(2)), 1/2 − c (c ∈ σ^(3)), 1.4901, 0.4901 − δ′₁ and 0.4901 − δ₂ (1/2 − a = 0.4901 being the target near 2
also).

*The values.* The table gives, for each y, n⁺ = ⌊y/𝔡₁⌋, the fractional part "frac" of y/𝔡₁ rounded to four digits,
n⁻ = ⌊4y/𝔡₀⌋, all the integers n with n⁻ < n ≤ n⁺, p = p_n, q = n − 4p ≥ 0, and bounds for p𝔡₀ + q𝔡₁ − y; each entry
follows from [[lem:is-offsets]] (b) by multiplying the bounds exactly. In every row y/𝔡₁ and 4y/𝔡₀ are at distance
more than 0.01 from ℤ, the bounds for θ_n/ε₀ lie strictly between p − 1 and p, and the printed excess lies in (0, ε₀);
by [[lem:is-reduction]] it is the least excess with that n.

| y | n⁺ | frac | n⁻ | n | p | q | p𝔡₀ + q𝔡₁ − y |
|---|---|---|---|---|---|---|---|
| 0.5 | 1500001 | .2917 | 1500000 | 1500001 | 175001 | 799997 | (5.1172818·10⁻¹³, 5.1172819·10⁻¹³) |
| 0.4901 | 1470301 | .2661 | 1470300 | 1470301 | 159656 | 831677 | (5.0962596·10⁻¹³, 5.0962597·10⁻¹³) |
| 0.49 | 1470001 | .2658 | 1470000 | 1470001 | 159501 | 831997 | (5.0960473·10⁻¹³, 5.0960474·10⁻¹³) |
| 0.4802 | 1440601 | .2405 | 1440600 | 1440601 | 144311 | 863357 | (5.0752375·10⁻¹³, 5.0752376·10⁻¹³) |
| 0.4801 | 1440301 | .2403 | 1440300 | 1440301 | 144156 | 863677 | (5.0750251·10⁻¹³, 5.0750252·10⁻¹³) |
| 0.48 | 1440001 | .2400 | 1440000 | 1440001 | 144001 | 863997 | (5.0748128·10⁻¹³, 5.0748129·10⁻¹³) |
| 0.4703 | 1410901 | .2149 | 1410900 | 1410901 | 128966 | 895037 | (5.0542153·10⁻¹³, 5.0542154·10⁻¹³) |
| 0.4702 | 1410601 | .2147 | 1410600 | 1410601 | 128811 | 895357 | (5.0540030·10⁻¹³, 5.0540031·10⁻¹³) |
| 0.4701 | 1410301 | .2144 | 1410300 | 1410301 | 128656 | 895677 | (5.0537906·10⁻¹³, 5.0537907·10⁻¹³) |
| 0.47 | 1410001 | .2142 | 1410000 | 1410001 | 128501 | 895997 | (5.0535783·10⁻¹³, 5.0535784·10⁻¹³) |
| 0.4602 | 1380601 | .1889 | 1380600 | 1380601 | 113311 | 927357 | (5.0327685·10⁻¹³, 5.0327686·10⁻¹³) |
| 0.4601 | 1380301 | .1886 | 1380300 | 1380301 | 113156 | 927677 | (5.0325561·10⁻¹³, 5.0325562·10⁻¹³) |
| 0.46 | 1380001 | .1883 | 1380000 | 1380001 | 113001 | 927997 | (5.0323438·10⁻¹³, 5.0323439·10⁻¹³) |
| 0.4501 | 1350301 | .1628 | 1350300 | 1350301 | 97656 | 959677 | (5.0113216·10⁻¹³, 5.0113217·10⁻¹³) |
| 0.45 | 1350001 | .1625 | 1350000 | 1350001 | 97501 | 959997 | (5.0111093·10⁻¹³, 5.0111094·10⁻¹³) |
| 0.44 | 1320001 | .1367 | 1320000 | 1320001 | 82001 | 991997 | (4.9898748·10⁻¹³, 4.9898749·10⁻¹³) |
| 1 | 3000002 | .5833 | 3000001 | 3000002 | 350001 | 1599998 | (4.6790104·10⁻¹³, 4.6790105·10⁻¹³) |
| 0.9901 | 2970302 | .5578 | 2970301 | 2970302 | 334656 | 1631678 | (4.6579882·10⁻¹³, 4.6579883·10⁻¹³) |
| 0.99 | 2970002 | .5575 | 2970001 | 2970002 | 334501 | 1631998 | (4.6577759·10⁻¹³, 4.6577760·10⁻¹³) |
| 0.9802 | 2940602 | .5322 | 2940601 | 2940602 | 319311 | 1663358 | (4.6369661·10⁻¹³, 4.6369662·10⁻¹³) |
| 0.9801 | 2940302 | .5319 | 2940301 | 2940302 | 319156 | 1663678 | (4.6367537·10⁻¹³, 4.6367538·10⁻¹³) |
| 0.98 | 2940002 | .5317 | 2940001 | 2940002 | 319001 | 1663998 | (4.6365414·10⁻¹³, 4.6365415·10⁻¹³) |
| 0.9701 | 2910302 | .5061 | 2910301 | 2910302 | 303656 | 1695678 | (4.6155192·10⁻¹³, 4.6155193·10⁻¹³) |
| 0.97 | 2910002 | .5058 | 2910001 | 2910002 | 303501 | 1695998 | (4.6153069·10⁻¹³, 4.6153070·10⁻¹³) |
| 0.96 | 2880002 | .4800 | 2880001 | 2880002 | 288001 | 1727998 | (4.5940724·10⁻¹³, 4.5940725·10⁻¹³) |
| 1.4901 | 4470303 | .8494 | 4470301 | 4470302 | 1109655 | 31682 | (1.6416021719·10⁻¹⁴, 1.6416021720·10⁻¹⁴) |
| | | | | 4470303 | 509656 | 2431679 | (4.2197168·10⁻¹³, 4.2197169·10⁻¹³) |
| 0.4901 − δ′₁ | 1470299 | .4661 | 1470298 | 1470299 | 279654 | 351683 | (2.3181480·10⁻¹⁴, 2.3181481·10⁻¹⁴) |
| 0.4901 − δ₂ | 1470300 | .4661 | 1470299 | 1470300 | 279655 | 351680 | (8.0959353·10⁻¹⁴, 8.0959354·10⁻¹⁴) |

The candidate with p = 0 gives (n⁺ + 1)𝔡₁ − y ≥ (0.99995 − frac)𝔡₁ ≥ 0.1505·𝔡₁ > 5.01·10⁻⁸ in every row. The three
smallest entries in full: for y = 1.4901,

    1.47953934242725117564684196040 < 1109655𝔡₀ < 1.47953934242725117564684196263,
    0.01056065757276524037487773961 < 31682𝔡₁ < 0.01056065757276524037487777130,

so 1.6416021719700·10⁻¹⁴ < μ_G < 1.6416021719734·10⁻¹⁴, which is [[eq:is-mu]]; for y = 0.4901 − δ′₁,
0.37287183427925841840422648624 < 279654𝔡₀ < 0.37287183427925841840422648681,
0.11722756572068676317019531909 < 351683𝔡₁ < 0.11722756572068676317019567078, and y lies in
(0.49009939999992200009371996934, 0.49009939999992200009371996935), so the excess lies in
(2.3181480701·10⁻¹⁴, 2.3181480703·10⁻¹⁴); for y = 0.4901 − δ₂, 0.37287316761199915967171561290 < 279655𝔡₀ <
0.37287316761199915967171561347, 0.11722656572154787371494866063 < 351680𝔡₁ < 0.11722656572154787371494901233, and
y ∈ (0.49009973333346607403357761515, 0.49009973333346607403357761516), so the excess lies in
(8.0959353086·10⁻¹⁴, 8.0959353088·10⁻¹⁴). So the least excess over all windows is μ_G, and (G) holds exactly for
ε_K < μ_G. Finally μ_G < 10⁻¹³ < 1.94·10⁻⁸ < δ_50 by [[lem:s14-delta50]], and μ_G < ε_Υ = 1.4619·10⁻¹⁰, the choice of
[[lem:ec-gauge-gap]], so that every ε_K < μ_G meets the condition ε_K < ε_Υ of [[def:iii-i10-1-3]], and ε_+ may be taken
in (ε_K, μ_G), as [[eq:iii-i9-1-1]] and (G⁺) of [[def:iii-j-g-plus]] ask. ∎

**Proposition {#prop:is-count}** (N_Λ, k̄_0 and J_*.) For ℰ_ind and ℰ^ι_ind as constructed and every ε_+ ∈ (0, δ̄):

(a) 1.62066·10¹³ < N_Λ < 1.67472·10¹³;

(b) k̄_0 = 3 is the least bound that [[def:iii-i10-1-1]] admits;

(c) η_0 = 𝔡₁ and J_* = ⌈5/𝔡₁⌉ + 2 = 15,000,015.

*Proof.* (a) For X > 0 let T(X) := #{(p, q) ∈ ℕ₀² : p𝔡₀ + q𝔡₁ < X}. The triangle {u, v ≥ 0, u𝔡₀ + v𝔡₁ < X} has area
X²/(2𝔡₀𝔡₁), and each of its points lies in the unit square with lower left corner (⌊u⌋, ⌊v⌋), a counted point; the
squares [p, p + 1) × [q, q + 1) of the counted points are disjoint and lie in the triangle with X + 𝔡₀ + 𝔡₁. So

    X²/(2𝔡₀𝔡₁) ≤ T(X) ≤ (X + 𝔡₀ + 𝔡₁)²/(2𝔡₀𝔡₁).

By [[prop:is-lambda]], N_Λ = #(Λ ∩ {Re < 3 + ε_+}) ≤ Σ_(β∈ℬ) T(3 + ε_+ − β). The 26 rational β < 3 of ℬ (λ_♯, 2 + c and
5/2 + c, which include λ_♯ + 1 = 5/2 + a) give disjoint sets of points, since by [[lem:is-offsets]] (c) two of them
differ by no non-zero p𝔡₀ + q𝔡₁, and the points of one are distinct; so N_Λ ≥ Σ_(rational β<3) T(3 − β). The 26
numbers 3 − β are 1.4901, 1 − c (c ∈ σ^(2)) and 1/2 − c (c ∈ σ^(3)), with
Σ (3 − β)² = 14.40589434 and Σ (3 − β) = 17.832; by [[lem:is-offsets]] (b), 1/(2𝔡₀𝔡₁) = 1125001468750.4…. So
N_Λ ≥ 14.40589434·1125001468750.4 > 1.62066·10¹³. For the upper bound, ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶ =: ν₀, the two
irrational β contribute at most 2(0.4901 + ν₀)²/(2𝔡₀𝔡₁), and β = 3 contributes T(ε_+) = 1, as ε_+ < 𝔡₁; so
N_Λ ≤ (14.40589434 + 2ν₀·17.832 + 26ν₀² + 2(0.4901 + ν₀)²)·1125001468750.5 + 1 < 1.67472·10¹³.

(b) By [[def:iii-i10-1-1]], k̄_0 bounds the orders of ℰ⁰_src ∪ ℰ_++ ∪ 𝒢 ∪ (2 + ℰ_col) below 2λ_♯ = 3.0198. There,
ℰ⁰_src is 𝒢 together with ℰ_rows ∩ {Re < 2} ⊂ ℰ_++ (the parts involving ℰ_+ lie above 2λ_♯, (H1)); 𝒢 = (2, 0) ∪
(2 + ℰ_ind) has order 3 at 3 = 2 + 1 ([[prop:is-logs]] (a)) and at most 3 elsewhere below 3.0198, as the exponents of
ℰ_ind below 1.0198 are those of [[eq:is-low]] below it; 2 + ℰ_col = (2 + ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind))) + ℕ₀
has the same orders; ℰ_++ has orders at most 3, with 3 at λ_♯ + 1 ([[prop:is-ci-pp]] (b)).

(c) The least real part of π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1} is 𝔡₁ ([[eq:is-low]], [[prop:is-iota]]). By the row y = 1 of the
table, 1/𝔡₁ = 3000002.583…, so 5/𝔡₁ = 15000012.91…, whose ceiling is 15000013. ∎

[[lem:uc-fourier-count]] bounds J_* through η_0 ≥ ε_Υ; with η_0 = 𝔡₁, J_* = 15,000,015 ([[prop:is-count]] (c)).

#### How far ℰ_ind can be made smaller {#sec:is-smaller}

The index sets as constructed take the boundary spectrum at every type ([[cor:uc-two-offsets]] (b)). A smaller
index set serves wherever the coefficients at the omitted exponents vanish. Two symmetries give such vanishing.

**Lemma {#lem:is-typed}** (Boundary spectrum on an invariant subspace.) Let Π be a projection on the sections over ∂X,
acting pointwise in ρ, that commutes with A := ρ⁻²(□^Υ_b)^(0) near ∂X and with its indicial family. If Πu = u for the
solution u of [[lem:iii-a-1-4]], resp. of [[lem:iii-a-1-5]] with ΠF = F, the conclusions hold with E(α) built from
the poles of N(A, ·)⁻¹Π of real part above α, resp. with ord the order of the pole of N(A, ·)⁻¹Π.

*Proof.* In the proof of [[lem:iii-a-1-4]], v = χ̃u, χAu, w and (A − N(A))v lie in the range of Π, so f′ = Πf′ and
ℳv = Πℳv. Hence N(A, ι)⁻¹ℳf′ = N(A, ι)⁻¹Πℳf′, whose poles are those of N(A, ·)⁻¹Π, with the Laurent coefficients
R_kΠ ((E3) of [[sec:iii-a-1-1]]); the residues in the contour shift are therefore at those poles, with those orders,
and the iteration keeps every term in the range of Π. In [[lem:iii-a-1-5]] the circle integral [[eq:iii-a-1-4]] applied
to f₀ = Πf₀ involves N(A, ζ)⁻¹Π only. ∎

Two projections apply. At b = (m, 0) the operators commute with the rotations of x ([[lem:iii-e1-2-1]] at A = 0,
with c_Υ, c_(Υ,H) radial), so the projections onto the types commute with A. At every b the parity φ commutes with
□^Υ_b and with P_b ([[lem:iii-i15-1-1]] (P3)), so ½(1 ± φ) do. By [[lem:is-roots]] (c), N(A, ·)⁻¹½(1 + φ) has its
poles at the roots of the even types and N(A, ·)⁻¹½(1 − φ) at those of the odd types.

**Lemma {#lem:is-rot-s0}** (The rotation corrections carry no scalar type 0 term at a non-integer exponent.) For every
b = (m, A) near b₀, every V ∈ 𝒱_1 and every non-integer w, the scalar type 0 part of the coefficient of
ρ^w(log ρ)^k in ω^(−1)_(b,v1)(V) is 0.

*Proof.* Write V = V(W), W ∈ 𝔰𝔬(4) ([[eq:iii-e1-1-1]]), and let ℓ_A(W) be a fixed real linear functional of that
scalar type 0 part (the scalar type 0 sections of the splitting form a two-dimensional space of SO(4)-invariant
1-forms on 𝕊³). For O ∈ SO(4), [[lem:iii-e1-2-1]] gives φ_O*g_((m,OAOᵀ)) = g_((m,A)), with t_*, c_Υ and c_(Υ,H)
invariant, so φ_O* intertwines □^Υ at (m, OAOᵀ) and at (m, A), and P_b⁻¹ on the decaying spaces, which φ_O* preserves.
As φ_O*V(W) = V(OᵀWO), ω^(−1)_(b,v1)(V) = V − P_b⁻¹□^Υ_b V gives φ_O*ω^(−1)_((m,OAOᵀ),v1)(V(OWOᵀ)) =
ω^(−1)_((m,A),v1)(V(W)). The scalar type 0 part is fixed by φ_O*, so ℓ_(OAOᵀ)(OWOᵀ) = ℓ_A(W). Write
ℓ_A(W) = −tr(X_AW), X_A ∈ 𝔰𝔬(4). With O = e^(sA), OAOᵀ = A, so −tr(X_A e^(sA)We^(−sA)) = −tr(X_AW) for all W and
s, which gives [A, X_A] = 0. If [A, W] = 0, R_(V(W)) is Killing for g_b ([[lem:iii-e1-2-3]]), so
ω^(−1)_(b,v1)(V(W)) = g_b(R_(V(W)), ·) ([[prop:iii-d2-3-1]] (3)), whose components lie in ρ⁻¹C^∞(X̄) and have no
non-integer exponent; so ℓ_A(W) = 0. With W = X_A this gives tr(X_A²) = 0, X_A = 0. ∎

**Definition {#def:is-cb}** (The coefficient c_b.) For b = (m, A) near b₀ and Ȧ ∈ 𝔰𝔬(4), let c_b(Ȧ) be the
coefficient of ρ^(2+𝔡₀) in ω̇_b(0, Ȧ) ([[eq:iii-f3-2-1]]); it is a multiple of the indicial solution of type s0 at
2 + 𝔡₀ ([[lem:is-roots]] (b)), linear in Ȧ.

**Theorem {#thm:is-d0}** (When ℰ_ind can omit 𝔡₀.) (a) For ℰ_ind as constructed, 𝔡₀ ∈ π_1ℰ_ind
([[cor:uc-two-offsets]] (b)), at every b.

(b) Every construction of the union ℰ_ind other than ω̇_b(0, ·) and the tensors built from it (ġ^Υ_b(0, ·)) has, at every
b near b₀, no term at the exponent m + 𝔡₀, m its leading order. At b = b₀, and
at every b = (m, 0), the same holds for ω̇_b(0, ·), and an index set serving there is ℰ_ind with the boundary spectrum
taken at the type of each construction; its exponents below 3/2 are 𝔡₁, 1, 1 + 𝔡₁, 1 + δ′₁, 1 + 2𝔡₁, 1 + 𝔡₀ and
1 + 2𝔡₀.

(c) There is an index set ℰ′_ind serving in every membership of [[sec:uc-index-sets]] at every b near b₀, with
𝔡₀ ∉ π_1ℰ′_ind, if and only if c_b(Ȧ) = 0 for every b = (m, A) near b₀ and every Ȧ ∈ ker ad_A. c_b vanishes on im ad_A
and at every b with A = 0, and c_(m,OAOᵀ)(OȦOᵀ) = c_(m,A)(Ȧ) for O ∈ SO(4). This paper does not determine c_b at a
rotating b.

*Proof.* (b) The translations, boosts and their towers are odd, the rotations, ω̇_b, the time translation and its tower,
and ġ^Υ_b even ([[lem:iii-i15-1-1]] (P3); ω̄_s1 and ω̆̄¹_s1 are odd, V, ω_s0 and W̄ even, ∂_bg_b is even as φ fixes
every g_b); each class construction has the parity of its type. By [[lem:is-typed]] with ½(1 ± φ), an odd construction
meets only roots of odd types, so not 2 + 𝔡₀ (type s0, [[lem:is-roots]] (b)); its exponents congruent to 𝔡₀ do not
occur. An exponent 𝔡₀ + j relative to the leading order m arises in an even construction at the root 2 + 𝔡₀ only if
m = 2 − j with j ∈ ℕ₀; the even constructions with m = 2 are the rotation corrections and ω̇_b(0, ·), and those with
m ≤ 1 give offsets 2 + 𝔡₀ − m ≥ 1 + 𝔡₀. The rotation corrections have no term at 2 + 𝔡₀: they carry no logarithm
there (the count of (c1) in the proof of [[prop:is-logs]] (a)), and their coefficient there lies in the kernel of
N(A, 2 + 𝔡₀), which is of type s0, as the right side has integer exponents and no lower exponent differs from 2 + 𝔡₀
by an integer; and it has no scalar type 0 part ([[lem:is-rot-s0]]). At b = (m, 0) the projections onto the types apply:
ω̇_b(0, Ȧ) is of vector type 1 ([[prop:iii-f3-2-2]] (4) at b₀, and at (m, 0) the same argument), and so is every
correction of a construction of one type; the exponents below 3/2 then come from the translations (s1: 𝔡₁, 1 + δ′₁),
ω̇_b(0, ·) (v1: 1), the boosts (s1: 1 + 𝔡₁), ω̇_b(1, 0) and the time translation tower (s0: 1 + 𝔡₀), and the class roots
μ_s0 and μ_(1,0) (1 + 2𝔡₀, 1 + 2𝔡₁); at b = (m, 0) the rotations are Killing and have no correction.

(c) If c_b(Ȧ) ≠ 0 for some b and Ȧ, the term c_b(Ȧ)ρ^(2+𝔡₀) of ω̇_b(0, Ȧ), whose membership is
𝒜^((2,0)∪(2+ℰ_ind)) ([[prop:iii-f3-2-2]] (1)), needs (𝔡₀, 0) ∈ ℰ_ind. Conversely, if c_b = 0 on ker ad_A it vanishes
everywhere: by [[rem:iii-f3-2-3]], ω̇_b(0, [A, A_V]) = 2ω^(−1)_(b,v1)(V) − 2V_b with V_b = g_b(R_(A_V), ·), whose term at
2 + 𝔡₀ has no scalar type 0 part ([[lem:is-rot-s0]]; V_b has integer exponents), and ker ad_A + im ad_A = 𝔰𝔬(4), ad_A
being skew-symmetric for −tr. Then ω̇_b(0, Ȧ) has no term at 2 + 𝔡₀ + j for any j ∈ ℕ₀: comparing the coefficients of
ρ^(2+𝔡₀+j) in Aω̇ = −ρ⁻²η_b, whose right side has integer exponents, gives N(A, 2 + 𝔡₀ + j)ω̇_(2+𝔡₀+j) = 0 by induction
on j, and 2 + 𝔡₀ + j is no root for j ≥ 1. The same comparison at j = 0 puts the coefficient of a rotation correction
at 2 + 𝔡₀ in the kernel of N(A, 2 + 𝔡₀), which is of type s0 ([[lem:is-roots]] (b)); having no scalar type 0 part
([[lem:is-rot-s0]]), it vanishes, and so do those at 2 + 𝔡₀ + j. With (b), the index set ℰ′_ind built by
[[lem:is-typed]] with ½(1 ± φ), with the exponents 2 + 𝔡₀ + ℕ₀ removed for the rotation corrections and for
ω̇_b(0, ·), serves at every b and does not contain 𝔡₀; the offset 𝔡₀ + j with j ≥ 1 of the even constructions at
m ≤ 1 is not 𝔡₀. The equivariance is that of
[[lem:is-rot-s0]], with φ_O*ġ_((m,OAOᵀ))(0, OȦOᵀ) = ġ_((m,A))(0, Ȧ) by differentiating [[lem:iii-e1-2-1]]; at A = 0 it is
(b). At a rotating b no statement of this paper evaluates c_b(Ȧ), Ȧ ∈ ker ad_A; the symmetry above makes X ↦ c_b(X)
a linear form whose dual vector lies in ker ad_A. ∎

**Corollary {#cor:is-flat}** (The gap condition without 𝔡₀.) Suppose c_b = 0 for every b near b₀, and take ℰ′_ind of
[[thm:is-d0]] (c), with ℰ^ι_ind built from the same states. Then the increments of Λ below 3/2 are generated by 𝔡₁, 1,
1 + δ′₁, 1 + δ₂, 1 + 𝔡₀ and 1 + 2𝔡₀, and (G) holds if and only if ε_K < μ♭, where

    μ♭ := λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸)

([[prop:gap-sums]]). As μ♭ > δ_50 > ε_+ > ε_K, (G) then imposes nothing beyond [[eq:iii-i9-1-1]]. For such ε_+,
56,436,656 ≤ N_Λ ≤ 59,377,257.

*Proof.* The increments: the odd constructions give 𝔡₁ and 1 + δ′₁ (translations, roots 2 + 𝔡₁ and 3 + δ′₁ of type s1),
1 + 𝔡₁ (boosts) and 1 + 2𝔡₁ (μ_(1,0)); the even ones give 1 and 1 + δ₂ (rotations and ω̇_b(0, ·), roots 3 of types s0
and v1 and 3 + δ₂ of type s2), 1 + 𝔡₀ (ω̇_b(1, 0), the time translation tower, the class 1 − l at l = 2) and 1 + 2𝔡₀
(μ_s0); all other offsets are at least 2 or are sums of these. As in [[thm:is-gap]], the targets are y = 1.4901,
0.4901, 0.4901 − δ′₁, 0.4901 − δ₂, 0.4901 − 𝔡₀, 0.4901 − 2𝔡₀ (third window and λ_♯ + 1 + 𝔡₀ + ℕ₀𝔡₁ near 3), 1 − c and
1/2 − c, and the least excess is ⌈y/𝔡₁⌉𝔡₁ − y. By the column "frac" of the table of [[thm:is-gap]] and the values
1470297.2661 and 1470293.2661 of y/𝔡₁ at 0.4901 − 𝔡₀ and 0.4901 − 2𝔡₀, (1 − frac)𝔡₁ is least at y = 1.4901, where it
is μ♭, and every other is above 1.3888·10⁻⁷. For N_Λ: each β ∈ ℬ♭ (the 26 rational β < 3, λ_♯ + 1 + 𝔡₀,
λ_♯ + 1 + 2𝔡₀, λ_♯ + 1 + δ′₁, λ_♯ + 1 + δ₂ and 3) contributes ⌊(3 − β)/𝔡₁⌋ + 1 points, as no point lies in
[3, 3 + ε_+); the sets of the first 28 and of β = 3 are pairwise disjoint by [[lem:is-offsets]] (c); the sums with
and without λ_♯ + 1 + δ′₁ and λ_♯ + 1 + δ₂ give the bounds. ∎

#### What is determined {#sec:is-summary}

**Remark {#rem:is-summary}** (What (IS) gives and what it leaves.) At the computational point, for the index sets as
constructed: the exponents of real part at most 5 are [[eq:is-ind]], [[prop:is-iota]] and [[prop:is-ci-pp]] (a), with
logarithmic orders at most 39 for ℰ_ind (attained), 50 for ℰ^ι_ind and 0 for the least ℰ^C_I; those of the least ℰ_++
below 2λ_♯ are [[prop:is-ci-pp]] (b); above 2λ_♯ they depend on ℰ_+, and none of Λ ∩ {Re ≤ 3 + ε_+}, l_* and k̄_0
uses them. Every indicial root of L̂_b(0) has multiplicity at most 7, and is simple on [−101, 5] ([[prop:is-mult]]);
[[def:iii-i10-1-1]] asks l_* to bound them at real part at most 5, a half-plane that contains the roots below −101; for
these the bound 7 serves, and their exact multiplicities, which this paper does not decide, are not needed. So the
largest multiplicity M of an indicial root of L̂_b(0) of real part at most 5 satisfies M ≤ 7 ([[prop:iii-f1-2-3]] (b)),
the largest logarithmic order L of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part at most 5 satisfies 39 ≤ L ≤ 50, the order 39
being attained at (5, 39) ∈ ℰ_ind ([[prop:is-logs]], [[prop:is-ci-pp]] (a)), and the part of l_* that (IS) fixes,
max(L, M) = L, is at most 50: l_* = 50 is admissible for it. (G), N_Λ, k̄_0 and J_* are [[thm:is-gap]] and
[[prop:is-count]]. The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5, statement (SP) of [[rem:uc-missing]],
are all 1 ([[cor:sp-lstar]] (a)), so they do not raise l_* above L. Two further things are not determined by this paper:
the coefficient c_b of [[def:is-cb]] at a rotating b, which for index sets that keep 𝔡₁ decides whether ε_K may be
taken up to μ♭ ([[cor:is-flat]]) or only below μ_G ([[thm:is-gap]]), and whether an admissible ℰ_ind can omit 𝔡₁. Neither
enters an upper bound for d: the index sets as constructed serve with every ε_K < μ_G, and the two decide only whether
smaller index sets, with a larger ε_K, are available. The individual roots ι ∈ Z of [[prop:is-iota]] are fixed by the
polynomials of [[prop:np-10-12]] and located by [[sec:s14-pa]]; they lie above 3 as exponents of ℰ^ι_ind and do not enter
Λ below 3 + ε_+.

### The poles of the inverse of the ι⁺-normal operator {#sec:sp}

This section determines the poles of ϰ ↦ N_sf(ϰ)⁻¹ ([[thm:iii-g-5-1]]) and of ϰ ↦ N_ι⁺(L̄, ϰ)⁻¹ ([[def:iii-g1-4-1]])
in the half plane {Re ϰ ≥ 2}, with their orders. Of these poles [[lem:iii-g1-4-2]] (a) states that they lie in
{Re ≥ 2}, finitely many below each bound. Their orders at real part at most 5 enter the number l_* of
[[def:iii-i10-1-1]], the bound K_ι ≤ 2l_* + 1 of [[lem:iii-j-1-2]] and the logarithmic orders that the solution maps
of the steps of [[sec:s23-step]] raise.

There are two results. The first holds wherever the hypotheses of [[ch:s16]] hold. Integrating the equation
N_sf(ϰ)u = f against the powers v^k reduces the poles at a point ϰ_0 with Re ϰ_0 ≥ 2, on the isotypic components of
one type, to those of the inverse of an explicit matrix polynomial built from the indicial matrix of L̃(0) and from S̄
alone ([[thm:sp-reduction]]). In particular the poles in {Re ϰ ≥ 2} are exactly the numbers μ + j, μ an indicial root
of L̂_b(0) with Re μ > 1 and j ≥ 1 an integer, and the order of each is at most the number of such roots of one type,
with multiplicity, among ϰ_0 − 1, ϰ_0 − 2, …. The second is the evaluation at the computational point of
[[def:ec-point]]: every pole of real part at most 5 is simple and lies in spec_ι⁺(L̄), and the poles are listed
([[thm:sp-spectrum]]). The orders of these poles therefore contribute exactly 1 to l_*. With the logarithmic orders of
the index sets as constructed and the multiplicities of the indicial roots of L̂_b(0), the least admissible l_* is the
largest of those logarithmic orders, a number in [39, 50], and we take l_* = 50; with the least ℰ^C_I, K_ι ≤ 2 on the
set Σ of [[def:iii-j-1-1]] ([[cor:sp-lstar]]). Nothing depends on the black hole parameter, as N_ι⁺(2L_b) = N_ι⁺(2L̄)
for every b ([[lem:iii-h2-3-2]]).

*Setting.* The hypotheses of [[thm:iii-g-5-1]] and of [[thm:iii-g1-3-1]] are assumed throughout, as in [[ch:s16]]; at
the computational point they are the hypotheses under which its formulas are evaluated ([[rem:ec-point-outside]]).
𝒫 is the set of poles of N_sf(·)⁻¹. By [[thm:iii-g-5-1]] (1)–(2) it is the set of ϰ at which N_sf(ϰ) is not
injective, and it does not meet {Re < 2}. Admissible pairs, 𝒳 and 𝒴 are those of [[eq:iii-g-2-6]]–[[eq:iii-g-2-7]]; we
write c for the weight μ there, μ denoting indicial roots in this section. For a pair admissible for every ϰ in a disc, 𝒳
does not depend on ϰ in the disc, and ϰ ↦ N_sf(ϰ) ∈ ℒ(𝒳, 𝒴) is a polynomial of degree 2 ([[lem:iii-g-1-2]] (f)). On ℝ⁴ we
write r = |x| = ρ⁻¹ and n = x/r, and t̄ is the Cartesian time.

For a type and degree τ ([[sec:iii-f1-1]]) let n_τ be the size of its indicial matrices on symmetric 2-tensors and
N_τ(ι) the matrix N_L(ι) of [[sec:iii-f1-2]], the indicial matrix of ρ⁻²(2L̄)^(0) = L̃(0)(ω, ρ∂_ρ, ∂_ω): on an
isotypic component W_π = ℂ^(n_τ) ⊗ π of type τ, L̃(0)(ω, ι, ∂_ω) acts as N_τ(ι) ⊗ Id_π. The endomorphism S̄ is
pointwise and invariant under SO(4) ([[eq:iii-f-2-2]]), so by Schur's lemma it acts on W_π as S_τ ⊗ Id_π for an
n_τ × n_τ matrix S_τ. Further N_τ(ι) = −ι² Id + ιA_τ + B_τ, and det N_τ(ι) = (−1)^(n_τ)∏(ι − μ), the product over the
roots μ of type τ listed in [[prop:iii-f1-2-3]], with multiplicity. A root is *singular* if its real part exceeds 1;
these are the entries after the semicolons of [[prop:iii-f1-2-3]], and no root has real part in (0, 1] ((a) there).
Let d_τ be the sum of dim π over the irreducible representations π of type τ: (l + 1)² at scalar type l, 2l(l + 2)
at vector type l and 2(l − 1)(l + 3) at tensor type l. For Re ϰ_0 ≥ 2 put

    K(ϰ_0) := ⌊Re ϰ_0⌋ − 2 ∈ ℕ_0.                                                                        {#eq:sp-k}

#### Jordan chains {#sec:sp-chains}

**Definition {#def:sp-chains}** (Jordan chains.) Let X, Y be Banach spaces, A(ϰ) = A_0 + ϰA_1 + ϰ²A_2 with
A_i ∈ ℒ(X, Y), and A^(i) := ∂_ϰ^iA. For ϰ_0 ∈ ℂ and 𝔫 ≥ 1 let 𝒦_𝔫(A, ϰ_0) be the space of the tuples
(u_0, …, u_(𝔫−1)) ∈ X^𝔫 with

    Σ_(i=0)^j (i!)⁻¹ A^(i)(ϰ_0) u_(j−i) = 0,     0 ≤ j < 𝔫,                                             {#eq:sp-chain}

that is, A(ϰ)Σ_(j<𝔫)(ϰ − ϰ_0)^ju_j = O((ϰ − ϰ_0)^𝔫). A tuple of 𝒦_𝔫(A, ϰ_0) with u_0 ≠ 0 is a *Jordan chain of
length 𝔫*, and p(A, ϰ_0) is the largest length of a Jordan chain (0 if A(ϰ_0) is injective). The same definitions
apply to square matrix polynomials, with X = Y a finite-dimensional space.

**Lemma {#lem:sp-pole-order}** (Pole order and chains.) Let A be as in [[def:sp-chains]], invertible for
0 < |ϰ − ϰ_0| < r, and let ϰ ↦ A(ϰ)⁻¹ ∈ ℒ(Y, X) have a pole of order p_0 at ϰ_0 (p_0 = 0 if it is holomorphic
there). Then p(A, ϰ_0) = p_0.

*Proof.* Write A(ϰ)⁻¹ = Σ_(i=1)^(p_0)(ϰ − ϰ_0)^(−i)A_(−i) + H(ϰ) with H holomorphic and A_(−p_0) ≠ 0. If p_0 ≥ 1,
choose f ∈ Y with A_(−p_0)f ≠ 0. Then U(ϰ) := (ϰ − ϰ_0)^(p_0)A(ϰ)⁻¹f is holomorphic near ϰ_0, U(ϰ_0) = A_(−p_0)f ≠ 0
and A(ϰ)U(ϰ) = (ϰ − ϰ_0)^(p_0)f. As A is a polynomial, the coefficient of (ϰ − ϰ_0)^j in A(ϰ)U(ϰ) is the left side
of [[eq:sp-chain]] for the Taylor coefficients u_j of U, and it vanishes for j < p_0; so (u_0, …, u_(p_0−1)) is a
Jordan chain and p(A, ϰ_0) ≥ p_0. Conversely, let (u_0, …, u_(𝔫−1)) be a Jordan chain and
U(ϰ) := Σ_(j<𝔫)(ϰ − ϰ_0)^ju_j. By [[eq:sp-chain]], g(ϰ) := (ϰ − ϰ_0)^(−𝔫)A(ϰ)U(ϰ) is a polynomial, and
U(ϰ) = (ϰ − ϰ_0)^𝔫A(ϰ)⁻¹g(ϰ) for 0 < |ϰ − ϰ_0| < r. The right side is O(|ϰ − ϰ_0|^(𝔫−p_0)) and U(ϰ_0) = u_0 ≠ 0;
so 𝔫 ≤ p_0. ∎

**Lemma {#lem:sp-block}** (Block triangular matrices.) Let 𝔐(ϰ) be a square matrix polynomial, block lower
triangular with square diagonal blocks D_0(ϰ), …, D_q(ϰ), and let each det D_k be a non-zero polynomial with at most
a simple zero at ϰ_0. Then dim 𝒦_𝔫(𝔐, ϰ_0) ≤ Σ_k dim ker D_k(ϰ_0) for every 𝔫 ≥ 1. If
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0), then p(𝔐, ϰ_0) ≤ 1.

*Proof.* First let q = 0 and D := D_0. As D(ϰ)⁻¹ = adj D(ϰ)/det D(ϰ) has at most a simple pole at ϰ_0,
[[lem:sp-pole-order]] gives p(D, ϰ_0) ≤ 1. Let (m_0, …, m_(𝔫−1)) ∈ 𝒦_𝔫(D, ϰ_0) with 𝔫 ≥ 2. Then m_0 = 0, since
otherwise (m_0, m_1) would be a Jordan chain of length 2; and then [[eq:sp-chain]] for (m_j) is [[eq:sp-chain]] for
(m_1, …, m_(𝔫−1)) ∈ 𝒦_(𝔫−1)(D, ϰ_0). By induction on 𝔫, 𝒦_𝔫(D, ϰ_0) consists of the tuples (0, …, 0, w) with
w ∈ ker D(ϰ_0), and has dimension dim ker D(ϰ_0). In general write each vector as (x, y), x its first block. The
block rows of [[eq:sp-chain]] belonging to the first block involve only the first blocks, 𝔐 being block lower
triangular; so (x_j) ∈ 𝒦_𝔫(D_0, ϰ_0), and if every x_j vanishes, (y_j) ∈ 𝒦_𝔫(𝔐′, ϰ_0), 𝔐′ the matrix formed by the
blocks 1, …, q. Hence dim 𝒦_𝔫(𝔐, ϰ_0) ≤ dim 𝒦_𝔫(D_0, ϰ_0) + dim 𝒦_𝔫(𝔐′, ϰ_0), and induction on q gives the bound.
If p(𝔐, ϰ_0) ≥ 2, a Jordan chain (m_0, m_1) and the tuples (0, w), w ∈ ker 𝔐(ϰ_0), span a subspace of 𝒦_2(𝔐, ϰ_0)
of dimension dim ker 𝔐(ϰ_0) + 1, since its elements with first entry 0 are the (0, w). When
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0) this exceeds the bound. ∎

#### Moments {#sec:sp-moments}

**Definition {#def:sp-moments}** (Moments.) Let k ∈ ℕ_0, c > k + 1 and s′ ∈ ℝ. For u ∈ Ḣ^(s′,c)_b(sf_(≥−1)) the
*k-th moment* 𝔮_k(u) is the distribution on 𝕊³, with values in ℂ^15 in the frame of [[sec:iii-g-1-1]], given by

    ⟨𝔮_k(u), ψ⟩ := ⟨u, v^k ψ⟩,     ψ ∈ C^∞(𝕊³; ℂ^15),                                                   {#eq:sp-moment}

the pairing of distributions on ℝ_v × 𝕊³ with the measure |dv| dg̸ (componentwise, bilinear). It is well defined and
continuous on Ḣ^(s′,c)_b: (1 − χ_∂)u is supported in [−1, 4] × 𝕊³, where v^kψ is smooth; and near R = 0, where
v^k|dv| dg̸ = R^(−k−1)μ_b with μ_b = |dR/R| dg̸, χ_∂u lies in H^(s′)_(b,c), while R^(−k−1)ψ ∈ 𝒜^(−k−1) lies in
H^∞_(b,−k−1−ϵ) ⊂ H^(−s′)_(b,−c) for 0 < ϵ ≤ c − k − 1 ([[lem:i-c-2-2]] (f)), so [[lem:i-c-2-2]] (d) applies. For u
in C_c^∞((−1, ∞) × 𝕊³), 𝔮_k(u) = ∫ v^k u dv. Operators acting on 𝕊³ alone (multiplication by smooth endomorphisms
of ω, derivatives in ω) commute with 𝔮_k.

**Lemma {#lem:sp-moments}** (Moments of the spectral family.) Let k ∈ ℕ_0, c > k + 1, s′ ∈ ℝ and
u ∈ Ḣ^(s′,c)_b. Then for every ϰ ∈ ℂ

    𝔮_k(N_sf(ϰ)u) = L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔮_k(u) + 2k(ϰ − k − 3/2 − S̄)𝔮_(k−1)(u),                    {#eq:sp-moments}

the last term being absent for k = 0. The identity obtained by applying ∂_ϰ^i to both sides holds, with N_sf^(i)(ϰ)
on the left.

*Proof.* N_sf(ϰ) maps Ḣ^(s′,c)_b to Ḣ^(s′−2,c)_b boundedly ([[sec:iii-g-1-2]]), and 𝔮_k and 𝔮_(k−1) are continuous
on these spaces; so both sides of [[eq:sp-moments]] are continuous in u. C_c^∞((−1, ∞) × 𝕊³) is dense in
Ḣ^(s′,c)_b, near v = −1 by [[lem:i-a-6-1]] (a) and near R = 0 by [[lem:i-c-2-2]] (d), glued with χ_∂. For such u,
integration by parts in v at fixed ω gives, for every g smooth with compact support in v,

    ∫ v^k ∂_v g dv = −k ∫ v^(k−1) g dv,     ∫ v^k (v∂_v) g dv = −(k + 1) ∫ v^k g dv,

and the second gives ∫ v^k F(v∂_v)g dv = F(−k − 1)∫ v^k g dv for every polynomial F whose coefficients act on 𝕊³
alone. In [[eq:iii-g-1-3]] put g := (v∂_v + ϰ − 3/2 − S̄)u. The first term −2∂_vg contributes
2k∫ v^(k−1)g dv = 2k(ϰ − 3/2 − S̄ − k)𝔮_(k−1)(u), and the second, L̃(0)(ω, v∂_v + ϰ, ∂_ω)u, contributes
L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔮_k(u). For fixed u both sides are polynomials in ϰ, which gives the last statement. ∎

**Lemma {#lem:sp-primitive}** (Integration in v.) Let Re ϰ_0 ≥ 2, let (s, c) be admissible for every ϰ in a disc about
ϰ_0, with c > 1, and let (u_0, …, u_(𝔫−1)) ∈ 𝒦_𝔫(N_sf, ϰ_0) in the space 𝒳 of (s, c), with 𝔮_0(u_j) = 0 for every j.
Let Iu_j be the distribution on ℝ_v × 𝕊³ with ∂_v Iu_j = u_j that vanishes on {v < −1}. Then for every c′ < c − 1:

(a) u_j ∈ Ḣ^((s;∞),c)_(b;b) and Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b);

(b) (Iu_0, …, Iu_(𝔫−1)) ∈ 𝒦_𝔫(N_sf, ϰ_0 − 1) in the space 𝒳 of the pair (s + 1, c′), which is admissible for ϰ_0 − 1
when c′ > Re ϰ_0 − 2;

(c) 𝔮_k(Iu_j) = −(k + 1)⁻¹𝔮_(k+1)(u_j) for every integer k with 0 ≤ k < c − 2.

*Proof.* (a) By [[eq:sp-chain]], N_sf(ϰ_0)u_j = −N_sf′(ϰ_0)u_(j−1) − ½N_sf″(ϰ_0)u_(j−2), where by [[eq:iii-g-1-2]] and
[[eq:iii-g-1-3]] N_sf′(ϰ) = −2∂_v − 2(v∂_v + ϰ) + a(ω) and N_sf″ = −2. These operators map Ḣ^((s;k),c)_(b;b) into
Ḣ^((s−1;k),c)_(b;b) for every k: near v = 0 because ∂_v(v∂_v) = (v∂_v + 1)∂_v and ∂_v commutes with the ℒ_Ω, so that
words pass through ∂_v, and near R = 0 because ∂_v = −R(R∂_R). By induction on j, [[thm:iii-g-5-1]] (3) gives u_j ∈
Ḣ^((s;∞),c)_(b;b). Near R = 0 this space is H^∞_(b,c) ([[sec:iii-g-1-2]]), so |W^αu_j| ≤ C_αv^(−c) on {v ≥ 4} for every
word W^α in v∂_v and the ℒ_Ω ([[lem:i-c-2-2]] (f)). Let W̃^α be W^α with every v∂_v replaced by v∂_v + 1 (W̃^α = Id for
the empty word). Then W^αI = IW̃^α, as v∂_vI = I(v∂_v + 1) (both sides vanish on {v < −1} and have the same v-derivative)
and the ℒ_Ω commute with I. Put g := W̃^αu_j. It lies in Ḣ^(s−|α|,c)_b, |α| the length of the word, and |g| ≤ C′_αv^(−c)
on {v ≥ 4}. Moreover 𝔮_0(g) = 0. Indeed 𝔮_0 commutes with the ℒ_Ω, 𝔮_0(u_j) = 0, and 𝔮_0((v∂_v + 1)w) = 0 for every w ∈
Ḣ^(s′,c)_b, s′ ∈ ℝ: for w ∈ C_c^∞((−1, ∞) × 𝕊³) it is ∫ ∂_v(vw) dv = 0, such w are dense ([[lem:i-a-6-1]] (a),
[[lem:i-c-2-2]] (d), as in the proof of [[lem:sp-moments]]), and w ↦ 𝔮_0((v∂_v + 1)w) is continuous, v∂_v + 1 mapping
Ḣ^(s′,c)_b into Ḣ^(s′−1,c)_b ([[def:sp-moments]], c > 1). Moving the ℒ_Ω at the left end of W̃^α through 𝔮_0, one reaches
either a factor v∂_v + 1, which gives 0, or, if W̃^α has none, 𝔮_0(u_j) = 0. Take χ ∈ C^∞(ℝ) equal to 1 on (−∞, 3] and to
0 on [4, ∞). Then I(χg) is constant on {v ≥ 4}, equal to ⟨χg, 1⟩, and so, on {v ≥ 4},

    W^αIu_j(v) = Ig(v) = ⟨χg, 1⟩ + ∫_3^v (1 − χ)g dv′ = 𝔮_0(g) − ∫_v^∞ g dv′ = −∫_v^∞ g dv′.

So |W^αIu_j| ≤ C′_αv^(1−c)/(c − 1) on {v ≥ 4}, for every word W^α; hence Iu_j ∈ 𝒜^(c−1) ⊂ H^∞_(b,c′) near R = 0
([[lem:i-c-2-2]] (f)). On {v < 5} we use W^αIu_j = I(W̃^αu_j) again. By (i) of the proof of [[lem:iii-g1-2-1]] each
W̃^αu_j lies in H^s(ℝ; H^m(𝕊³)) for every m; the primitive maps this space into H^(s+1)(ℝ; H^m(𝕊³)) locally ((iii) (α)
there); and the latter lies in H^(s+1) for m large, as in (i) there. So Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b).

(b) By [[lem:iii-g-1-2]] (e), N_sf(ϰ + 1)∂_v = ∂_vN_sf(ϰ) for every ϰ; differentiating in ϰ,
N_sf^(i)(ϰ_0)∂_v = ∂_vN_sf^(i)(ϰ_0 − 1). So F_j := Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) has
∂_vF_j = Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i) = 0; F_j vanishes on {v < −1} and does not depend on v, hence F_j = 0.
By (a), Iu_j ∈ Ḣ^(s+1,c′)_b, and N_sf(ϰ_0 − 1)Iu_j = −Σ_(i≥1)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) lies in Ḣ^(s,c′)_b, the
operator N_sf′ being of first order; so Iu_j lies in 𝒳 for (s + 1, c′). The pair is admissible for ϰ_0 − 1: s + 1 <
2 − Re(ϰ_0 − 1) as s < 2 − Re ϰ_0, and c′ ∈ (Re ϰ_0 − 2, Re ϰ_0 − 1) as c′ < c − 1 < Re ϰ_0 − 1.

(c) Both moments are defined, choosing c′ ∈ (k + 1, c − 1). Let φ ∈ C_c^∞(ℝ) equal 1 on [−2, 1], put φ_T(v) := φ(v/T)
for T > 4, and let ψ ∈ C^∞(𝕊³; ℂ^15). As ∂_vIu_j = u_j,

    ⟨Iu_j, (k + 1)φ_Tv^kψ⟩ + ⟨Iu_j, φ_T′v^(k+1)ψ⟩ = −⟨u_j, φ_Tv^(k+1)ψ⟩.

As T → ∞ the first and last terms tend to (k + 1)⟨𝔮_k(Iu_j), ψ⟩ and −⟨𝔮_(k+1)(u_j), ψ⟩ (dominated convergence on
{v ≥ 4}, with the bounds of (a)), and the middle one is O(T^(−1)·T^(k+1)·T^(1−c)·T) = O(T^(k+2−c)), which tends to 0. ∎

#### The moment matrix {#sec:sp-matrix}

**Definition {#def:sp-matrix}** (The moment matrix.) For a type τ and K ∈ ℕ_0 let 𝔐^K_τ(ϰ) be the matrix polynomial
of size (K + 1)n_τ, block lower bidiagonal with blocks of size n_τ, whose blocks are

    (𝔐^K_τ)_(kk)(ϰ) = N_τ(ϰ − k − 1)  (0 ≤ k ≤ K),     (𝔐^K_τ)_(k,k−1)(ϰ) = 2k(ϰ − k − 3/2 − S_τ)  (1 ≤ k ≤ K),
                                                                                                      {#eq:sp-matrix}

all other blocks being 0. So det 𝔐^K_τ(ϰ) = ∏_(k=0)^K det N_τ(ϰ − k − 1). For Re ϰ_0 ≥ 2 write 𝔐_τ := 𝔐^(K(ϰ_0))_τ,
and let c_τ(ϰ_0) be the order of the zero of det 𝔐_τ at ϰ_0: the number of roots μ of type τ, with multiplicity,
with ϰ_0 − μ ∈ {1, …, K(ϰ_0) + 1}. Each such root has Re μ ≥ Re ϰ_0 − K(ϰ_0) − 1 = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 ≥ 1,
hence Re μ > 1, as no root has real part in (0, 1], and is therefore singular.

By [[eq:sp-moments]], the moments (𝔮_k(u))_(k≤K) of N_sf(ϰ)u are obtained from those of u by the operator 𝔐(ϰ) on
𝒟′(𝕊³; ℂ^15)^(K+1) defined by the right side of [[eq:sp-moments]]; on W_π^(K+1) it acts as 𝔐^K_τ(ϰ) ⊗ Id_π.

**Theorem {#thm:sp-reduction}** (The poles of the spectral family in {Re ≥ 2}.) Let Re ϰ_0 ≥ 2 and K := K(ϰ_0), and
let 𝒳, 𝒴 be the spaces of a pair admissible for every ϰ in a disc about ϰ_0.

(a) For every 𝔫 ≥ 1 the map (u_j)_(j<𝔫) ↦ ((𝔮_k(u_j))_(k≤K))_(j<𝔫) is a bijection from 𝒦_𝔫(N_sf, ϰ_0) onto
𝒦_𝔫(𝔐, ϰ_0) := ⊕_π 𝒦_𝔫(𝔐_τ(π) ⊗ Id_π, ϰ_0), τ(π) the type of π, the space of the chains of 𝔐 in
𝒟′(𝕊³; ℂ^15)^(K+1): the tuples there that satisfy [[eq:sp-chain]] for 𝔐, which commutes with the projections onto the
W_π^(K+1). Only finitely many summands are non-zero.

(b) dim ker N_sf(ϰ_0) = Σ_τ d_τ dim ker 𝔐_τ(ϰ_0), and the order of the pole of N_sf(·)⁻¹ at ϰ_0 is the largest of the
numbers p(𝔐_τ, ϰ_0), each of which is at most c_τ(ϰ_0).

(c) ϰ_0 ∈ 𝒫 if and only if ϰ_0 = μ + j with μ a singular root and j ≥ 1 an integer. So
𝒫 ∩ {Re ≥ 2} = {μ + j : μ a singular root of some type, j ∈ ℕ, j ≥ 1}.

(d) If c_τ(ϰ_0) ≤ 1 for every type, then ϰ_0 is at most a simple pole of N_sf(·)⁻¹.

*Proof.* Write (s, c) for the pair; c ∈ (Re ϰ_0 − 1, Re ϰ_0) by [[eq:iii-g-2-6]], and the poles of N_sf(·)⁻¹ and their
orders do not depend on the pair ([[thm:iii-g-5-1]] (2)). Then c > K + 1, as K + 1 ≤ Re ϰ_0 − 1. By [[lem:sp-primitive]]
(a) the elements of a tuple of 𝒦_𝔫(N_sf, ϰ_0) lie in Ḣ^(s,c)_b, so their moments of order at most K are defined, and by
[[lem:sp-moments]] (with its derivatives) they form a tuple of 𝒦_𝔫(𝔐, ϰ_0). The components on the W_π are tuples of
𝒦_𝔫(𝔐_τ(π) ⊗ Id_π, ϰ_0), which vanish unless det 𝔐_τ(π)(ϰ_0) = 0, that is unless π has a root among ϰ_0 − 1, …, ϰ_0 − K −
1; by [[lem:iii-f1-2-4]] with X := Re ϰ_0 this holds for a finite set F of representations only.

*Injectivity.* Let (u_j) ∈ 𝒦_𝔫(N_sf, ϰ_0) have all moments of order at most K equal to 0. Choose η > 0 with
(K + 1)η < c − Re ϰ_0 + 1 and put c_i := c − i(1 + η). We show by induction on i ≤ K + 1 that (I^iu_j) ∈
𝒦_𝔫(N_sf, ϰ_0 − i) in the space 𝒳 of the pair (s + i, c_i), admissible for ϰ_0 − i, with 𝔮_k(I^iu_j) = 0 for
k ≤ K − i. For i = 0 this is the hypothesis. If it holds for i ≤ K, then 𝔮_0(I^iu_j) = 0, c_i > Re ϰ_0 − 1 − i ≥
K + 1 − i ≥ 1, and [[lem:sp-primitive]] with c′ := c_(i+1) ∈ (Re ϰ_0 − i − 2, c_i − 1) gives the statement for i + 1,
the moments by its part (c) (k ≤ K − i − 1 < c_i − 2). At i = K + 1, Re(ϰ_0 − K − 1) = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 < 2, so
N_sf(ϰ_0 − K − 1) is injective ([[prop:iii-g-3-2]]); by [[eq:sp-chain]] and induction on j, I^(K+1)u_j = 0 for every
j. As ∂_v^(K+1)I^(K+1)u_j = u_j, every u_j vanishes.

*Surjectivity.* Let T_𝔫: 𝒳^𝔫 → 𝒴^𝔫, (u_j) ↦ (Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i))_j, so that 𝒦_𝔫(N_sf, ϰ_0) = ker T_𝔫.
N_sf(ϰ_0) is Fredholm of index 0 ([[thm:iii-g-5-1]] (1)); choose 𝔉: 𝒳 → 𝒴 of finite rank with N_sf(ϰ_0) + 𝔉
invertible, as in the proof of [[thm:iii-g-5-1]]. T_𝔫 + diag(𝔉, …, 𝔉) is block lower triangular with invertible
diagonal blocks, hence invertible (solve row by row); so T_𝔫 = B(Id − G) with B invertible and G of finite rank. For
such an operator dim ker T_𝔫 = codim ran T_𝔫. Indeed, let E ⊃ ran G be finite-dimensional; A := Id − G maps E into
E, every x with Ax = 0 lies in E, A induces the identity on 𝒳^𝔫/E, and if Ax ∈ E then x ∈ E. So ran A + E = 𝒳^𝔫
and ran A ∩ E = A(E), whence codim ran A = dim E − dim A(E) = dim ker(A|_E) = dim ker A. Now let V := ⊕_(π∈F) W_π^(K+1)
and Ψ: 𝒴^𝔫 → V^𝔫 the map taking (f_j) to the components in V of the moments (𝔮_k(f_j))_(k≤K). It is onto: for
χ_0, …, χ_K ∈ C_c^∞((1, 2)) with ∫ v^iχ_k dv = δ_(ik) (they exist, the powers being linearly independent on (1, 2)),
the sources Σ_k χ_k(v)w_k, w_k ∈ V, lie in 𝒴 and have moments w_k. By [[lem:sp-moments]],
Ψ(T_𝔫u) = T^𝔐_𝔫(moments of u), T^𝔐_𝔫 the operator of [[eq:sp-chain]] for 𝔐 on V^𝔫, a square matrix. So Ψ maps
ran T_𝔫 into ran T^𝔐_𝔫, and

    dim ker T_𝔫 = codim ran T_𝔫 ≥ dim V^𝔫 − rank T^𝔐_𝔫 = dim ker T^𝔐_𝔫 = dim 𝒦_𝔫(𝔐, ϰ_0).

With the injectivity, the map is a bijection. This proves (a).

(b) The case 𝔫 = 1 of (a) gives the dimension, as dim(ker 𝔐_τ(ϰ_0) ⊗ π) summed over the π of type τ is
d_τ dim ker 𝔐_τ(ϰ_0). A tuple of 𝒦_𝔫(N_sf, ϰ_0) has u_0 ≠ 0 exactly when the moments of u_0 do not all vanish (the
case 𝔫 = 1 of (a)), so the bijection maps Jordan chains onto Jordan chains, and p(N_sf, ϰ_0) is the largest of the
p(𝔐_τ ⊗ Id_π, ϰ_0) = p(𝔐_τ, ϰ_0). By [[lem:sp-pole-order]], applied on a disc about ϰ_0 on which 𝒫 has no other point,
p(N_sf, ϰ_0) is the order of the pole of N_sf(·)⁻¹. And 𝔐_τ(ϰ)⁻¹ = adj 𝔐_τ(ϰ)/det 𝔐_τ(ϰ) has a pole of order at most
c_τ(ϰ_0), so p(𝔐_τ, ϰ_0) ≤ c_τ(ϰ_0) by [[lem:sp-pole-order]].

(c) By (b), ϰ_0 ∈ 𝒫 if and only if det 𝔐_τ(ϰ_0) = 0 for some type, that is ϰ_0 − j is a root for some j ∈
{1, …, K + 1}; such a root is singular ([[def:sp-matrix]]). Conversely, if μ is singular and j ≥ 1, then ϰ_0 := μ + j
has Re ϰ_0 > j + 1, so K(ϰ_0) ≥ j − 1, and det 𝔐_τ(ϰ_0) = 0. (d) follows from (b). ∎

On spacetime the moments have a direct meaning. For u ∈ ker N_sf(ϰ_0), U := ρ^(ϰ_0)u is a solution of 2L̄U = 0,
homogeneous of degree −ϰ_0 and supported in {t̄ ≥ |x|} ([[sec:iii-g-1-1]], Step 1 of the proof of [[prop:iii-g-3-2]]);
as dt̄ = r dv at fixed x, its integral in t̄ along each line {x = const} is r^(1−ϰ_0)𝔮_0(u), and by [[eq:sp-moments]]
at k = 0 this is a stationary solution of (2L̄)^(0), which vanishes unless ϰ_0 − 1 is a root. The poles thus come from
the stationary solutions r^(−μ)m, m ∈ ker L̃(0)(ω, μ, ∂_ω), that are singular at x = 0, and from their images under
∂_v, which maps ker N_sf(ϰ) into ker N_sf(ϰ + 1) ([[lem:iii-g-1-2]] (e)).

**Proposition {#prop:sp-visible}** (The poles are visible on ι⁺.) Let ϰ_0 ∈ 𝒫 with Re ϰ_0 ≥ 2 and
ϰ_0 ∉ 5/2 + spec S̄ + ℕ_0. Then ϰ_0 ∈ spec_ι⁺(L̄), and the order of the pole of ϰ ↦ N_ι⁺(L̄, ϰ)⁻¹ at ϰ_0, the largest
over the f ∈ Ċ^∞(ι⁺; S²T*), equals the order p of the pole of N_sf(·)⁻¹ at ϰ_0.

*Proof.* By [[thm:sp-reduction]] (b) there is a type τ with p(𝔐_τ, ϰ_0) = p, and by [[lem:sp-pole-order]] 𝔐_τ(·)⁻¹
has a pole of order p at ϰ_0; take π of type τ and ν ∈ W_π^(K+1) such that (ϰ − ϰ_0)^(p−1)𝔐(ϰ)⁻¹ν is unbounded near
ϰ_0. As in the proof of [[thm:sp-reduction]] choose g ∈ C_c^∞((1, 2) × 𝕊³; ℂ^15) whose moments of order at most
K(ϰ_0) are ν, and put f_ϰ := v^(2+ϰ)g, an element of Ċ^∞(ι⁺; S²T*) holomorphic in ϰ with R^(2+ϰ)f_ϰ = g. Let
u(ϰ) := N_sf(ϰ)⁻¹g, so that N_ι⁺(ϰ)⁻¹f_ϰ = R^(−ϰ)u(ϰ)|_(v>0) by [[eq:iii-g1-3-1]]. For ϰ ≠ ϰ_0 near ϰ_0,
[[eq:sp-moments]] gives 𝔐(ϰ)(moments of u(ϰ)) = ν; the moments being continuous on 𝒳, u has a pole of order at least
p, hence exactly p. By Step 0 of the proof of [[thm:iii-g1-3-1]], u(ϰ) is supported in {v ≥ 0}, and so are its
Laurent coefficients. Let c_(−p) be the leading one. As N_sf(ϰ)u(ϰ) = g is holomorphic, N_sf(ϰ_0)c_(−p) = 0. If
c_(−p) vanished on {v > 0}, it would be a non-zero element of ker N_sf(ϰ_0) supported in {v = 0}, and
[[lem:iii-g1-4-3]] would give ϰ_0 ∈ 5/2 + spec S̄ + ℕ_0. So R^(−ϰ)u(ϰ)|_(v>0) has a pole of order p at ϰ_0 (as a
distribution, hence in C^∞((0, ∞) × 𝕊³)). Write f_ϰ = Σ_(j<p)(ϰ − ϰ_0)^jf_j + (ϰ − ϰ_0)^pr(ϰ) with
f_j = (j!)⁻¹(log v)^jv^(2+ϰ_0)g ∈ Ċ^∞(ι⁺) and R^(2+ϰ)r(ϰ) holomorphic in 𝒴; then
N_ι⁺(ϰ)⁻¹f_ϰ − Σ_(j<p)(ϰ − ϰ_0)^jN_ι⁺(ϰ)⁻¹f_j = (ϰ − ϰ_0)^pR^(−ϰ)N_sf(ϰ)⁻¹(R^(2+ϰ)r(ϰ)) is holomorphic at ϰ_0. So
some N_ι⁺(ϰ)⁻¹f_j has a pole of order at least p. No f gives a larger order, as N_ι⁺(ϰ)⁻¹f = R^(−ϰ)N_sf(ϰ)⁻¹(R^(2+ϰ)f)
and R^(2+ϰ)f is holomorphic in 𝒴. ∎

**Lemma {#lem:sp-two-roots}** (The chains at ϰ_0 = 5.) Let W = Σ_i W_i dx^i with W_i linear, Σ_i x_iW_i = 0 and
∂_iW_j + ∂_jW_i = 0 (a rotation 1-form, of vector type 1), and V̂ := r⁻¹W. Put

    K_s0 := Σ_i (dx^i)² − 4 dr²,     K_v1 := dr ⊗_s V̂,     Z := −6e_Υ dt̄² + (4 − e_Υ)Σ_i (dx^i)² − (4 + 2e_Υ) dr².

(a) For K = K_s0 and K = K_v1, and every ι ∈ ℂ,

    L̃(0)(ω, ι, ∂_ω)K = (ι − 4)(2S̄ − ι − 2)K.                                                            {#eq:sp-gauge}

(b) L̃(0)(ω, 2, ∂_ω)Z = 4(e_Υ + 2)K_s0.

(c) For every value of the parameters with 1, 3 not roots of type s0 and 1, 2 not roots of type v1, and the roots 2,
4 of type s0 and 3, 4 of type v1 simple, dim ker 𝔐_τ(5) = 2 and p(𝔐_τ, 5) = 1 for τ = s0 and τ = v1.

*Proof.* L̃(0)(ω, ι, ∂_ω)K is defined by (2L̄)^(0)(r^(−ι)K) = r^(−ι−2)L̃(0)(ω, ι, ∂_ω)K, and (2L̄)^(0) is 2L̄ on
stationary sections ([[lem:iii-f-2-1]] (2)): by [[eq:iii-f-2-1]], (2L̄)^(0)u = □̄u + 2Ē^Cδ̄Ḡu + 2(δ̄* + Ē^C)Ē^ΥḠu, where
on stationary sections □̄ acts in the Cartesian frame as −Δ on each component and (δ̄k)_β = −Σ_j ∂_jk_(βj). We use, on
ℝ⁴ and for real or complex a,

    Δr^a = a(a + 2)r^(a−2),     Δ(r^an_in_j) = r^(a−2)((a − 2)(a + 4)n_in_j + 2δ_(ij)),
    ∂_j(r^aδ_(ij)) = a r^(a−1)n_i,     ∂_j(r^an_in_j) = (a + 3)r^(a−1)n_i,
    ∂_j(r^ax_iW_j) = r^aW_i,     ∂_j(r^ax_jW_i) = (a + 5)r^aW_i,
    Δ(r^a(x_iW_j + x_jW_i)) = a(a + 6)r^(a−2)(x_iW_j + x_jW_i).

The second and the last follow from Δ(fg) = (Δf)g + 2∇f·∇g + fΔg with x·∇(x_ix_j) = 2x_ix_j, Δ(x_ix_j) = 2δ_(ij),
x·∇(x_iW_j) = 2x_iW_j and Δ(x_iW_j) = 2∂_iW_j, the Killing equation removing the last term after symmetrising; the
third and fourth are direct, as ∂_j(x_ix_j) = 5x_i; the fifth and sixth follow from x·W = 0, ∂_jW_j = 0 (a consequence
of the Killing equation) and x·∇W_i = W_i.

(a) Let u := r^(−ι)K. Then tr u = 0 (tr Σ(dx^i)² = 4, tr dr² = 1, ⟨dr, V̂⟩ = 0) and ι_(∂_t̄)u = 0, so Ḡu = u and,
as c̄_Υ^♯ = −r⁻¹∂_t̄, Ē^ΥḠu = −γ_Υ(2ι_(c̄_Υ^♯)u − e_Υc̄_Υ tr u) = 0 ([[sec:iii-f1-1]]). For K_s0, u_(ij) =
r^(−ι)(δ_(ij) − 4n_in_j), and the identities give Δu = (ι + 2)(ι − 4)r^(−2)u and δ̄u = −3(ι − 4)r^(−ι−1)dr. For K_v1,
u_(ij) = ½r^(−ι−2)(x_iW_j + x_jW_i), and they give Δu = (ι + 2)(ι − 4)r^(−2)u and δ̄u = ½(ι − 4)r^(−ι−1)V̂. In both cases
δ̄u = −(ι − 4)r⁻¹ι_Xu with X := ḡ⁻¹dt_* = −∂_t̄ − ∂_r, since ι_Xu = −ι_(∂_r)u equals 3r^(−ι)dr for K_s0 and −½r^(−ι)V̂
for K_v1. By [[eq:iii-f-2-2]], ρS̄u = −Ē^Cι_XḠu + (dt_* ⊗_s ·)Ē^ΥḠu = −Ē^C(ι_Xu). Hence

    (2L̄)^(0)u = −(ι + 2)(ι − 4)r^(−2)u − 2(ι − 4)r⁻¹Ē^C(ι_Xu) = (ι − 4)r^(−2)(2S̄ − ι − 2)u,

which is [[eq:sp-gauge]].

(b) Let u := r^(−2)Z. Then tr Z = 6e_Υ + 4(4 − e_Υ) − (4 + 2e_Υ) = 12 and ι_(∂_t̄)Z = −6e_Υ dt̄, so
Ē^ΥḠu = −γ_Υ(2·6e_Υ − 12e_Υ)r^(−3)dt̄ = 0. Next Ḡu = r^(−2)((6 − 6e_Υ)dt̄² − (2 + e_Υ)Σ(dx^i)² − (4 + 2e_Υ)dr²) has
no mixed time–space components, and by the identities
Σ_j∂_j(r^(−2)((2 + e_Υ)δ_(ij) + (4 + 2e_Υ)n_in_j)) = (−2(2 + e_Υ) + (4 + 2e_Υ))r^(−3)n_i = 0; so δ̄Ḡu = 0.
Finally Δ(r^(−2)) = 0, so Δ(r^(−2)dt̄²) = 0 and Δ(r^(−2)δ_(ij)) = 0, while Δ(r^(−2)n_in_j) = r^(−4)(2δ_(ij) −
8n_in_j). The terms of (2L̄)^(0)u other than □̄u vanish, so
(2L̄)^(0)u = □̄u = (4 + 2e_Υ)r^(−4)(2δ_(ij) − 8n_in_j)dx^idx^j = 4(e_Υ + 2)r^(−4)K_s0.

(c) K_s0 and Z are invariant under SO(4), of type s0. The rotation 1-forms are the sum of the two irreducible
representations π of vector type 1; for W in one of them, K_v1 lies in W_π = ℂ² ⊗ π. Let k_τ ∈ ℂ^(n_τ) be the vector
with K_s0 = k_s0, resp. K_v1 = k_v1 ⊗ W, and z the one of Z. By (a), N_τ(ι)k_τ = (ι − 4)(2S_τ − ι − 2)k_τ, so k_τ
spans ker N_τ(4), the root 4 being simple. K(5) = 3, and by [[eq:sp-matrix]] a vector (ν_0, ν_1, ν_2, ν_3)
lies in ker 𝔐_τ(5) exactly when

    N_τ(4)ν_0 = 0,  N_τ(3)ν_1 = −2(5/2 − S_τ)ν_0,  N_τ(2)ν_2 = −4(3/2 − S_τ)ν_1,  N_τ(1)ν_3 = −6(1/2 − S_τ)ν_2.

*Type s0.* N_s0(3) and N_s0(1) are invertible. By (a) at ι = 3, N_s0(3)k_s0 = 2(5/2 − S_s0)k_s0, so ν_0 := k_s0
gives ν_1 = −k_s0. By (a) at ι = 2, N_s0(2)k_s0 = 4(2 − S_s0)k_s0, so −4(3/2 − S_s0)ν_1 = N_s0(2)k_s0 − 2k_s0, which
by (b) equals N_s0(2)(k_s0 − z/(2(e_Υ + 2))). So ν_2 := k_s0 − z/(2(e_Υ + 2)) and
ν_3 := −6N_s0(1)⁻¹(1/2 − S_s0)ν_2 complete a kernel vector with ν_0 ≠ 0. A second one is (0, 0, w, ν_3), w spanning
ker N_s0(2) and ν_3 := −6N_s0(1)⁻¹(1/2 − S_s0)w. *Type v1.* N_v1(2) and N_v1(1) are invertible. For ν_0 := a k_v1
and w ∈ ker N_v1(3), ν_1 := −a k_v1 + w solves the second equation, by (a) at ι = 3, and ν_2, ν_3 are then determined;
this gives kernel vectors for every (a, w). In both cases dim ker 𝔐_τ(5) ≥ 2 = Σ_k dim ker N_τ(4 − k). The
diagonal blocks of 𝔐_τ(ϰ) are N_τ(ϰ − k − 1), k ≤ 3, whose determinants are non-zero polynomials with at most a
simple zero at ϰ = 5, as 4 − k is a simple root of type τ or not a root, by the hypotheses. So [[lem:sp-block]]
gives equality and p(𝔐_τ, 5) ≤ 1, and p(𝔐_τ, 5) = 1 as the kernel is non-zero. ∎

#### The computational point {#sec:sp-point}

At the computational point let h := 10⁻⁶ (so γ_C = h⁻¹), κ := l(l + 2), x := hκ, a(x) := (3x + 10)/4 and
δ_C := 2.94·10⁻⁶, as in [[sec:s14-pa]]. Let ι₁ ∈ (2 + δ_C, 5/2) be the root of C of [[lem:s14-scalar-zero]],
ι_v(l) := (250002000000 + (l + 1)²)^(1/2) − 499999 the larger root of p_(v) ([[lem:s14-vector-distance]]), and
𝔡₀ := ι^Υ_(s0,2) − 2 and 𝔡₁ := ι^Υ_(s1,2) − 2 the offsets of [[sec:ec-gap-sums]], with
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶ and 3.3333·10⁻⁷ < 𝔡₁ < 3.3334·10⁻⁷ (proof of [[prop:gap-sums]]).
Further σ_Υ = {0, 99/10000, 1/100, 1/50} ([[eq:iii-g1-1-4]]).

**Lemma {#lem:sp-roots}** (The singular roots of real part at most 4.) At the computational point, for a type τ let 𝒮_τ
be the set of its roots μ with 1 < Re μ ≤ 4.

(a) 𝒮_s0 = {2, 3 + 𝔡₀, ι₁ − 1, 4}; 𝒮_s1 = {3, 3 + 𝔡₁, ι − 1, ι′ − 1}, where ι, ι′ are the roots of P_1 in
(2 + 3h, a(3h)) and in (a(3h), 3 − δ_C); 𝒮_s2 = {4} ∪ {ι − 1 : P_2(ι) = 0, Re ι > 2}, the last three numbers lying in
(1, 2); 𝒮_sl = {ι − 1 : P_l(ι) = 0, 2 < Re ι ≤ 5} for l ≥ 3; 𝒮_v1 = {3, 4}; 𝒮_v2 = {4, ι_v(2) − 1}, with
ι_v(2) ∈ (3, 4); 𝒮_vl = {ι_v(l) − 1} for 3 ≤ l ≤ 1413 and 𝒮_vl = ∅ for l ≥ 1414; 𝒮_t2 = {4}; 𝒮_tl = ∅ for l ≥ 3.

(b) Every element of 𝒮_τ is a simple root of type τ.

(c) Two distinct elements of one set 𝒮_τ differ by an integer only for {2, 4} ⊂ 𝒮_s0 and for {3, 4} ⊂ 𝒮_v1.

*Proof.* (a) By [[prop:iii-f1-2-3]] the singular roots of type τ are the entries after its semicolon. Those that do
not come from □^C are: at s0, 2, 4 and 1 + ι^Υ_(s0,2) = 3 + 𝔡₀; at sl, l ≥ 1, the integers l + 2 and l + 4 (3 and 5
at l = 1) and the numbers 1 + ι^Υ_(sl,l+j) ∈ (l + j + 1, l + j + 5/4), j = 1, 2 (the bounds of the proof of
[[prop:iii-f1-2-3]]); at vl, l + 2 and l + 3; at tl, l + 2. Of these, real part at most 4 have exactly 2, 3 + 𝔡₀, 4
at s0; 3 and 1 + ι^Υ_(s1,2) = 3 + 𝔡₁ at s1; 4 = l + 2 at s2, v2 and t2; and 3, 4 at v1. The entries from □^C are the
numbers ι − 1, ι a root of □^C with real part at least 2 that the factor D of [[eq:iii-f1-2-1]] does not remove: at
s0 the root ι₁ of C, the root 2 of P_0 = −(ι − 2)C being removed and the other roots of C having real part below −100
(proof of [[prop:np-10-54]]); at sl the roots of P_l of real part at least 2 other than ι = 2 at l = 1
([[prop:s14-scalar-every-h]]); at vl the root ι_v(l), which equals 3 at l = 1, is removed there, and increases with
l. The roots of P_1 other than 2 and those of P_2 lie in the stated intervals ([[lem:s14-sextic-small]] (a), (b)).
ι_v(2) ∈ (3, 4) as 500002² = 250002000004 < 250002000009 < 500003²; and ι_v(l) ≤ 5 exactly when
(l + 1)² ≤ 500004² − 250002000000 = 2000016, that is l ≤ 1413, as 1414² = 1999396 and 1415² = 2002225.

(c) At s0, 𝔡₀ < δ_C. The differences (3 + 𝔡₀) − 2 = 1 + 𝔡₀ and 4 − (3 + 𝔡₀) = 1 − 𝔡₀ are not integers, and
3 − ι₁, 4 + 𝔡₀ − ι₁ and 5 − ι₁ lie in (1/2, 1 − δ_C), (3/2 + 𝔡₀, 2 − (δ_C − 𝔡₀)) and (5/2, 3 − δ_C), intervals
without integers. At s1, ι − 1 and ι′ − 1 are distinct points of (1 + 3h, 2 − δ_C); 3 − (ι − 1) lies in
(1 + δ_C, 2 − 3h) and (3 + 𝔡₁) − (ι − 1) in (1 + δ_C + 𝔡₁, 2 − (3h − 𝔡₁)), with 𝔡₁ < 3h, and likewise for ι′; and
(3 + 𝔡₁) − 3 = 𝔡₁. At s2, the three numbers in (1, 2) are distinct, the intervals of [[lem:s14-sextic-small]] (b)
being disjoint, and 4 − (ι − 1) ∈ (2, 3). At v2, 4 − (ι_v(2) − 1) ∈ (1, 2).

At sl with l ≥ 3 the elements of 𝒮_sl are ι − 1 for the roots ι of P_l with real part in (2, 5], and the list
carries such an entry as often as the multiplicity of ι as a root of P_l. If x ≤ 70, these roots are among the three
roots of real part at least 2, counted with multiplicity, which by [[cor:s14-remote-point]] are the roots of
[[lem:s14-sextic-count]] (a): for 3 ≤ l ≤ 133, three distinct real roots in (2, 3) ([[lem:s14-sextic-small]] (c));
for l ≥ 134 (x ≥ 0.018), a real root ι_B and two more, which for x ≤ 0.03 lie in |ι − a| < 0.45, a disc disjoint
from the disc of ι_B, and have real parts in (2.06, 2.98) while ι_B ∈ (2.0179, 2.03], and which for x ≥ 0.03 are
non-real and conjugate, ι_P and ι̅_P, in disjoint discs ([[lem:s14-sextic-large]] and the proof of
[[prop:s14-damping-distance]]).

For 0.018 ≤ x ≤ 0.03, that is 134 ≤ l ≤ 172 (x = 0.018224 at l = 134 and x = 0.029928 at l = 172), the two roots
in |ι − a| < 0.45 are distinct. By [[lem:s14-majorant]], the bound h(M̄_a(0.45, 0.03) + hN̄(2.98, 0.03)) < 9.4·10⁻⁵
on |hW| of the proof of [[lem:s14-sextic-large]] (b) holds on the whole closed disc |ι − a| ≤ 0.45, since
a + 0.45 ≤ 2.9725 < 2.98 bounds |ι| there. For real ι in that disc, 2 + x − ι ≤ 2 + x − a + 0.45 = x/4 − 0.05 and
so 2 + x − ι ≤ −0.0425. As 3x + 10 = 4a and Δ_𝒬 is the discriminant of 𝒬(·, x) ([[lem:s14-sextic-split]] (iii)),
completing the square gives 𝒬(ι, x) = 2(ι − a)² − Δ_𝒬(x)/8. Further Δ_𝒬 decreases on [0, 107], its derivative
being 2x − 1715/8, and its smaller root x₋ lies in (0.01866, 0.01867) (loc. cit.). If l = 134 or 135, then
x = 0.018224 or 0.018495 lies below x₋, and Δ_𝒬(x) = 0.093562114176 or 0.035476440025. As 2 + x − a = −(2 − x)/4,
the value U(a, x) = (2 − x)Δ_𝒬(x)/32 is 0.0057943… or 0.0021967…, so U(a, x) > 2·10⁻³; while
𝒬(a ± 0.45, x) = 0.405 − Δ_𝒬(x)/8 > 0.39, so U(a ± 0.45, x) < −0.0425·0.39 < −0.016. Hence P_l = U + hW is negative
at a − 0.45, positive at a and negative at a + 0.45, and it has a real root in each of (a − 0.45, a) and
(a, a + 0.45): these are the two roots in the disc, and they are distinct. If 136 ≤ l ≤ 172, then x ≥ 0.018768 > x₋,
so Δ_𝒬(x) ≤ Δ_𝒬(0.018768) = −0.023037762176, and 𝒬(ι, x) ≥ −Δ_𝒬(0.018768)/8 = 0.002879720272 > 2.87·10⁻³ for
real ι. On the real diameter of the disc, then, |U| > 0.0425·2.87·10⁻³ > 1.2·10⁻⁴ > |hW|, and P_l has no real root
in the disc. As P_l has real coefficients and the disc is symmetric about ℝ, conjugation permutes the roots in the
disc with their multiplicities, and a non-real root of multiplicity 2 would bring its conjugate with the same
multiplicity, four roots in the disc in all. So the two roots are a non-real conjugate pair, and they are distinct.

In each case, therefore, the three roots of real part at least 2 are distinct, so each is a simple root of P_l, and no
two differ by a non-zero integer: for any two, either their real parts differ by less than 1 or their difference is
not real. If x > 70, no root of P_l satisfies |ι − 1| ≤ 50 ([[lem:s14-sextic-count]] (b)), so a real root of real
part at least 2 exceeds 51. The three roots of real part at least 2, counted with multiplicity
([[prop:s14-scalar-every-h]]), are permuted by conjugation with their multiplicities, P_l having real coefficients; a
non-real one of multiplicity at least 2 would bring its conjugate with the same multiplicity, four roots in all. So the
non-real ones are simple, and, three being odd, they form at most one conjugate pair. Those of real part at most 5 are
therefore non-real simple roots, at most two; if there are two, they are ι and ι̅ with Im ι ≠ 0, which neither
coincide nor differ by a real number, ι − ι̅ = 2i Im ι.

(b) An element μ of 𝒮_τ is an entry of the list of type τ, and the list gives the roots with multiplicity. μ differs
from the entries of real part at most 0 or greater than 4 by its real part, and from the entries for the other
elements of 𝒮_τ by (c). An entry ι − 1 from □^C occurs as often as the multiplicity of ι as a root of C, P_l or p_(v),
and that multiplicity is 1: ι₁ is a simple root of C, whose other two roots have real part below −100; ι_v(l) is one of
the two distinct real roots of the quadratic p_(v) ([[lem:s14-vector-distance]]); the roots of P_1 and P_2 concerned
lie one in each of three disjoint intervals, of three roots counted with multiplicity ([[lem:s14-sextic-small]] (a),
(b)); and those of P_l, l ≥ 3, are simple by the proof of (c). So μ is a simple root. ∎

**Lemma {#lem:sp-exceptional}** (No pole at the exceptional points.) Let Q := {5/2, 7/2, 9/2} + σ_Υ, twelve numbers. At
the computational point, P_l(q) ≠ 0 and ι_v(l) ≠ q for every q ∈ Q and l ≥ 1. Hence no singular root of real part at
most 4 lies in 3/2 + σ_Υ + ℤ, and no point of 𝒫 of real part at most 5 lies in 5/2 + spec S̄ + ℕ_0.

*Proof.* *The vector type.* ι_v(l) = q would make (q + 499999)² = 250002000000 + (l + 1)² an integer. Each q ∈ Q is
a fraction p′/d in lowest terms with d > 1, and then (q + 499999)² = (p′ + 499999d)²/d² with p′ + 499999d prime to d,
which is not an integer.

*The scalar type.* By [[eq:s14-nl]], P_l(ι) = c_0(ι) + c_1(ι)κ + c_2(ι)κ² + c_3κ³. At κ = 0 the third column of the
matrix there is (0, 0, h(2ι − 1 − ι²) − 2v(ι − 3))ᵀ and its upper left 2 × 2 block is hN_0(ι); so, at v = 1/2,
c_0(ι) = (−h(ι − 1)² − (ι − 3))P_0(ι), with P_0 = −(ι − 2)C of [[eq:s14-c0]]. Expanding the determinant at the
computational point,

    c_3 = 10⁻¹⁸,     c_2(ι) = 10⁻¹⁸(−3ι² − (255998991/64)ι + 2322999247/64),
    c_1(ι) = 10⁻¹⁸(3ι⁴ + (255998991/32)ι³ + (79998081750817/16)ι² − (3218988513000625/64)ι + 5157998188999183/64).

For a prime p let v_p denote the p-adic valuation of a non-zero rational number. If q ∈ Q and p is a prime with
v_p(c_0(q)) < v_p(c_i(q)) for i = 1, 2, 3, then P_l(q) ≠ 0 for every integer κ, since each c_i(q)κ^i has valuation at
least v_p(c_i(q)) and a sum whose term of least valuation is unique has that valuation. The valuations of the
coefficients of c_1, from ι⁴ to ι⁰, are −18, −23, −22, −24, −24 for p = 2 and −18, −18, −18, −14, −18 for p = 5
(3218988513000625 = 5⁴·5150381620801); those of c_2, from ι² to ι⁰, are −18, −24, −24 for p = 2 and −18, −18, −18 for
p = 5; v_p(c_3) = −18. Hence v_p(c_i(q)) ≥ min_j(v_p(coefficient of ι^j) + j·v_p(q)), which gives the lower bounds in
the table below. The values of c_0 are

    c_0(5/2) = 102,382,116,069,206,441,391/(2¹²·10¹⁷),
    c_0(7/2) = −184,309,587,192,075,727,923/(2¹³·10¹⁶),
    c_0(9/2) = −7,679,697,448,702,749,433,821/(2¹²·10¹⁷),
    c_0(25099/10000) = 1,019,224,980,784,674,272,031,997,531,559,760,391,559,271/(4·10⁴²),
    c_0(35099/10000) = −9,299,228,494,721,864,136,714,649,149,276,457,696,950,729/(4·10⁴²),
    c_0(45099/10000) = −76,091,116,104,307,206,847,501,599,126,784,137,785,460,729/(4·10⁴²),
    c_0(251/100) = 4,077,667,112,282,805,096,193,344,619,959/(16·10³⁰),
    c_0(351/100) = −37,209,137,195,213,265,101,596,444,677,141/(16·10³⁰),
    c_0(451/100) = −304,408,877,927,380,731,996,608,663,774,241/(16·10³⁰),
    c_0(63/25) = 126,728,556,223,578,619,714,117,857/(5¹¹·10¹⁹),
    c_0(88/25) = −2,346,368,372,779,440,282,518,355,711/(5¹⁰·10²⁰),
    c_0(113/25) = −2,356,501,507,010,040,363,609,315,267/(5¹³·10¹⁷),

with numerators odd in the first nine and prime to 5 in the last three. So:

    q                                 p    v_p(q)    v_p(c_0(q))    v_p(c_1(q)) ≥    v_p(c_2(q)) ≥    v_p(c_3)
    q ∈ {5/2, 7/2, 9/2}               2    −1        −29            −26              −25              −18
    q ∈ {5/2, 7/2, 9/2} + 99/10000    2    −4        −44            −35              −28              −18
    q ∈ {5/2, 7/2, 9/2} + 1/100       2    −2        −34            −29              −26              −18
    q ∈ {5/2, 7/2, 9/2} + 1/50        5    −2        −30            −26              −22              −18

and in every row v_p(c_0(q)) is the least. So P_l(q) ≠ 0 for every l ≥ 1.

*The consequences.* By [[lem:sp-roots]] (a) the singular roots of real part at most 4 are: integers; 3 + 𝔡₀ and
3 + 𝔡₁, whose distance from ℤ is below 1.34·10⁻⁶; ι₁ − 1 ∈ (1, 3/2); ι − 1 for roots ι of P_l with real part in
(2, 5]; and ι_v(l) − 1 ≤ 4. A number of 3/2 + σ_Υ + ℤ has distance from ℤ at least 12/25 and real part in (1, 4] only
in 3/2 + σ_Υ + {0, 1, 2}; ι₁ − 1 < 3/2; and ι − 1 ∈ 3/2 + σ_Υ + ℤ with Re ι ∈ (2, 5] means ι ∈ Q, which is excluded
for the roots of P_l (for non-real ι trivially) and for ι_v(l). Finally spec S̄ = σ_Υ ∪ σ_C with σ_C ⊂ [s_C, ∞) and
s_C > 100 ([[eq:iii-g1-1-4]], [[sec:iii-f-1]]), so a point of 5/2 + spec S̄ + ℕ_0 of real part at most 5 lies in
5/2 + σ_Υ + {0, 1, 2}; a point μ + j of 𝒫 there ([[thm:sp-reduction]] (c), with Re μ ≤ 4) would have
μ ∈ 3/2 + σ_Υ + ℤ. ∎

**Theorem {#thm:sp-spectrum}** (The ι⁺-spectrum at real part at most 5.) At the computational point, and for every b
near b₀:

(a) spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} = 𝒫 ∩ {Re ϰ ≤ 5} is the union of

    {3, 4, 5},     {4 + 𝔡₀, 4 + 𝔡₁},     {ι₁, ι₁ + 1, ι₁ + 2},
    {ι + j : l ≥ 1, P_l(ι) = 0, Re ι > 2, j ∈ ℕ_0, Re ι + j ≤ 5},
    {ι_v(l) + j : 2 ≤ l ≤ 1413, j ∈ ℕ_0, ι_v(l) + j ≤ 5}.

It is finite and lies in {Re ϰ > 2}.

(b) Every point of (a) is a simple pole of N_sf(·)⁻¹ and of N_ι⁺(L̄, ·)⁻¹: Spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} consists of the
pairs (ϰ, 0), ϰ in (a). The order m_ι of [[prop:iii-g3-2-4]], that of the pole of [[eq:iii-g1-3-3]], equals 1 at
these points and 0 at every other point of {Re ϰ ≤ 5}, for every ℓ_I > 5 allowed in [[thm:iii-g1-3-1]] (2) (the
principal parts do not depend on ℓ_I, so for a smaller ℓ_I the same holds on {Re ϰ < ℓ_I}).

(c) dim ker N_sf(ϰ_0) = Σ_τ d_τ c_τ(ϰ_0) at every point of (a): 1 at ϰ_0 = 3 (type s0), 11 at ϰ_0 = 4 (s0, s1, v1:
1 + 4 + 6) and 53 at ϰ_0 = 5 (s0, s1, s2, v1, v2, t2: 2 + 4 + 9 + 12 + 16 + 10).

*Proof.* By [[lem:iii-h2-3-2]], N_ι⁺(2L_b) = N_ι⁺(2L̄), and the indicial roots of L̂_b(0) do not depend on b
([[lem:iii-f-2-1]] (3)); so nothing below depends on b.

(a) By [[thm:sp-reduction]] (c), 𝒫 ∩ {Re ≤ 5} is the set of μ + j with μ singular, j ≥ 1 and Re(μ + j) ≤ 5, so
Re μ ≤ 4 and μ ∈ 𝒮_τ for some τ. [[lem:sp-roots]] (a) gives: from 𝒮_s0, 3, 4, 5, 4 + 𝔡₀ and ι₁, ι₁ + 1, ι₁ + 2
(ι₁ + 3 > 5); from 𝒮_s1, 4, 5, 4 + 𝔡₁ (5 + 𝔡₁ > 5) and ι + j for the two roots of P_1 in (2, 3), j ≤ 2; from 𝒮_s2,
5 and ι + j for the roots of P_2, j ≤ 2; from 𝒮_sl, l ≥ 3, the ι + j with Re ι + j ≤ 5; from 𝒮_v1, 4 and 5; from
𝒮_v2, 5, ι_v(2) and ι_v(2) + 1; from 𝒮_vl, l ≥ 3, the ι_v(l) + j ≤ 5; from 𝒮_t2, 5. This is the union, as the roots of
P_l with real part greater than 2 are those of real part at least 2 other than ι = 2 at l = 1
([[prop:s14-scalar-every-h]]). By [[lem:sp-exceptional]] no point of it lies in 5/2 + spec S̄ + ℕ_0, so
[[prop:sp-visible]] puts it in spec_ι⁺(L̄); and spec_ι⁺(L̄) ⊂ 𝒫 ([[lem:iii-g1-4-2]] (a)). The set is finite by
[[thm:iii-g-5-1]] (2), and every singular root has real part greater than 1.

(b) Let ϰ_0 be a point of (a) and τ a type. The roots counted by c_τ(ϰ_0) lie in 𝒮_τ and are simple
([[lem:sp-roots]] (b)), and any two of them differ by an integer, both lying in ϰ_0 − {1, …, K(ϰ_0) + 1}; so by
[[lem:sp-roots]] (c), c_τ(ϰ_0) ≤ 1, except c_s0(5) = 2 (the roots 4 and 2) and c_v1(5) = 2 (the roots 4 and 3).
The conditions of [[lem:sp-two-roots]] (c) hold at the computational point: by [[lem:sp-roots]] (a) the roots of
type s0 of real part in (1, 4] are 2, 3 + 𝔡₀, ι₁ − 1 ∈ (1, 3/2) and 4, and those of type v1 are 3 and 4, no root has
real part in (0, 1] ([[prop:iii-f1-2-3]] (a)), and these roots are simple ([[lem:sp-roots]] (b)). By
[[thm:sp-reduction]] (b) and [[lem:sp-two-roots]] (c), N_sf(·)⁻¹ has a simple pole at ϰ_0, and by [[prop:sp-visible]]
so has N_ι⁺(L̄, ·)⁻¹. The order of the pole of [[eq:iii-g1-3-3]], for every ℓ_I allowed in [[thm:iii-g1-3-1]] (2) with
Re ϰ_0 < ℓ_I, is that of N_ι⁺(L̄, ·)⁻¹ on Ċ^∞(ι⁺) ([[lem:iii-g1-4-2]] (b)); this gives m_ι, which vanishes at the
other points of {Re ϰ ≤ 5}, these lying outside spec_ι⁺(L̄) by (a).

(c) [[thm:sp-reduction]] (b), with dim ker 𝔐_τ(ϰ_0) = c_τ(ϰ_0): when c_τ(ϰ_0) = 1, det 𝔐_τ has a simple zero, so the
kernel is non-zero, and [[lem:sp-block]] bounds its dimension by 1; when c_τ(ϰ_0) = 2 it is [[lem:sp-two-roots]] (c).
At ϰ_0 = 3, 4, 5 the types with c_τ(ϰ_0) ≥ 1 are read off from [[lem:sp-roots]] (a); the values of d_τ are 1, 4 and 9
at s0, s1, s2, 6 and 16 at v1, v2, and 10 at t2. ∎

**Corollary {#cor:sp-lstar}** (The contribution of the poles to l_*.) At the computational point:

(a) The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 are all equal to 1. Of the quantities that the
number l_* of [[def:iii-i10-1-1]] bounds at real part at most 5, these orders contribute exactly 1, and the
multiplicities of the indicial roots of L̂_b(0) with real part in (1, 4] are all 1 ([[lem:sp-roots]] (b)). So the
least admissible l_* is max(1, L, M), where L is the largest logarithmic order of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part
at most 5 and M the largest multiplicity of an indicial root of L̂_b(0) of real part at most 5. Here M ≤ 7; and for
the index sets as constructed, with the least ℰ^C_I (the least index set satisfying (2)–(3) of [[def:iii-c-3-1]], which
exists by [[lem:iii-c-3-2]] (e) with ℰ̃ = ∅), 39 ≤ L ≤ 50. Hence max(1, L, M) = L: the least admissible l_* is
L ∈ [39, 50], and we take l_* = 50, which is admissible.

(b) For ϰ ∈ Σ ([[def:iii-j-1-1]]), K_ι(ϰ) ≤ m_ι(ϰ) + m_♯(ϰ) ([[prop:iii-g3-2-4]]) with m_ι(ϰ) ∈ {0, 1}, equal to 1
exactly when ϰ is a point of [[thm:sp-spectrum]] (a). With the least ℰ^C_I, whose logarithmic orders are all 0,
m_♯(ϰ) ≤ 1; so K_ι(ϰ) ≤ 2 for every ϰ ∈ Σ, and K_ι(ϰ) ≤ 1 unless ϰ ∈ spec_ι⁺(L̄) ∩ π_1ℰ^C_I, a set that contains 3.
The bounds K_ι(ϰ) ≤ 2 + k(ℰ^C_(I,♯), ϰ) ≤ l_* + 2 and K_ι(ϰ) ≤ 2l_* + 1 ([[lem:iii-j-1-2]]) hold as well, for every
ℰ^C_I whose logarithmic orders l_* bounds; at l_* = 50 they give 52 and 101. The pole at λ_♯ has K_ι(λ_♯) = 1; whether
the value 2 is taken is not decided here.

(c) In the step of [[sec:s23-step]] at an exponent ϰ₀, the solution map 𝒮_(ϰ₀) raises the logarithmic order by at
most m_ι(ϰ₀) ([[cor:iii-g3-3-1]] (1)): by at most 1 at the points of [[thm:sp-spectrum]] (a), and not at all at every
other ϰ₀ with Re ϰ₀ ≤ 5. Likewise each raise "by a pole order of N_ι⁺(L̄, ·)⁻¹" in [[lem:iii-i10-1-2]] (c) is at
most 1.

(d) On {2 ≤ Re ϰ ≤ 3 + ε_+}, where ε_+ < δ_50 < 2·10⁻⁸ ([[eq:iii-i9-1-1]], [[def:ec-point]]), the poles are 3; ι₁;
and the roots ι of P_l (l ≥ 1) with 2 < Re ι ≤ 3 + ε_+, together with ι + 1 for those with Re ι ≤ 2 + ε_+. All are
simple. Of these poles, 3 lies in Λ ([[def:iii-i10-1-1]]); whether ι₁, a root ι of some P_l or such an ι + 1 lies in
Λ is not decided here, and no bound depends on it, each raise being at most 1 by (c). The numbers λ_♯ + j,
3/2 + γ_Υ + j and 3/2 + 2γ_Υ + j (j = 1, 2, 3) are not poles.

*Proof.* (a) The orders are [[thm:sp-spectrum]] (b) and the multiplicities [[lem:sp-roots]] (b); the set of poles at
real part at most 5 is not empty, so the pole orders require l_* ≥ 1. That M ≤ 7 is stated in [[prop:is-mult]];
directly, (C1) holds at the computational point, the indicial roots of □^C_b at scalar type l ≥ 1, scalar type 0 and
vector type l being the roots of P_l, P_0 and p_(v) ([[prop:np-10-12]] (ii), (iii)), which [[prop:np-10-54]] (i),
(ii) locates as (C1) requires; so by [[prop:iii-f1-2-3]] (a), (b), at each type and degree n_τ ≤ 7 roots, counted with
multiplicity, have real part at most 0, and n_τ have real part above 1, and no root has multiplicity above 7. For L:
[[prop:is-logs]] gives 39 ≤ L ≤ 50 for the index sets as constructed and the least ℰ^C_I, whose logarithmic orders are
all 0 (proof of (b)). So L ≥ 39 > 7 ≥ M.

(b) The first bound is that of [[prop:iii-g3-2-4]] with (a), as Σ ⊂ {Re < 3 + ε_+}: m_♯(ϰ) = k(ℰ^C_(I,♯), ϰ) + 1
if ϰ ∈ π_1ℰ^C_(I,♯) and m_♯(ϰ) = 0 otherwise. The least ℰ^C_I is the union of the index sets ℰ_((m)) of the proof
of [[lem:iii-c-3-2]] (e) with ℰ_((0)) = ℰ̃ = ∅, and every logarithmic order of each ℰ_((m)) is 0, by induction on m.
For m = 0 there is nothing to prove. If it holds for ℰ_((m)), it holds for ℰ′_m = ℰ_((m)) ∪ ⋃_(s∈σ_Υ)(3/2 + s, 0)
and for ℰ′_m + (ℰ′_m − 1), as logarithmic orders add in a sum of index sets ([[def:s11-b-analysis]] (4)); and the
smallest index set containing a set of pairs (z, 0) consists of the pairs (z + j, 0), j ∈ ℕ₀, so it holds for
ℰ_((m+1)). Hence ℰ^C_(I,♯) = (λ_♯, 0) ∪ ℰ^C_I ([[eq:iii-g3-2-1]]) has all logarithmic orders 0, and
m_♯(ϰ) ∈ {0, 1}, equal to 1 exactly on {λ_♯} ∪ π_1ℰ^C_I. So K_ι(ϰ) ≤ 2, with K_ι(ϰ) = 2 possible only where
m_ι(ϰ) = m_♯(ϰ) = 1, that is on spec_ι⁺(L̄) ∩ ({λ_♯} ∪ π_1ℰ^C_I) = spec_ι⁺(L̄) ∩ π_1ℰ^C_I, as λ_♯ < 2 and
spec_ι⁺(L̄) ⊂ {Re ≥ 2} ([[lem:iii-g1-4-2]] (a)). The point 3 is in [[thm:sp-spectrum]] (a), and (3, 0) ∈ ℰ^C_I by
[[lem:iii-c-3-2]] (a). For any ℰ^C_I whose logarithmic orders at real part at most 5 are bounded by l_*,
k(ℰ^C_(I,♯), ϰ) ≤ l_* as in the proof of [[lem:iii-j-1-2]], which gives K_ι(ϰ) ≤ 2 + k(ℰ^C_(I,♯), ϰ) ≤ l_* + 2;
and l_* + 2 ≤ 2l_* + 1 as l_* ≥ 1. Finally (λ_♯, 0) ∈ Spec^(<ℓ_I)_(ι⁺)(L̄, ℰ^C_I) by [[cor:iii-g3-2-6]], so the pole
at λ_♯ is simple: K_ι(λ_♯) = 1.

(c) 𝒮_(ϰ₀)(f) is the solution that [[cor:iii-g3-3-1]] (1) gives, whose logarithmic powers are at most J + K, J the
largest power of log t_* in f and K the order at ϰ₀ of the pole of [[eq:iii-g3-2-2]]; its proof uses K only as the
order of the pole of ϰ ↦ N_ι⁺(ϰ)⁻¹ on the coefficients of f. As f has no ℐ⁺-expansion, [[eq:iii-g3-2-2]] acts on
these as the inverse of [[thm:iii-g1-3-1]] (2), as [[sec:s23-step]] notes, so that order is at most m_ι(ϰ₀), and
m_ι(ϰ₀) is given by [[thm:sp-spectrum]] (b). The raises of [[lem:iii-i10-1-2]] (c) are those of [[cor:iii-g2-4-3]],
whose logarithmic powers are at most k + l_0, l_0 the order of the pole of N_ι⁺(L̄, ·)⁻¹ at the exponent, at most 1
by [[thm:sp-spectrum]] (b).

(d) This is [[thm:sp-spectrum]] (a) restricted to the strip. Beyond it lie 4 + 𝔡₀, 4 + 𝔡₁ and the integers 4, 5, and
also ι₁ + 1 > 3 + δ_C and every ι_v(l) ≥ ι_v(2) > 3 + 4·10⁻⁶, since ε_+ < ε_ind = δ_50 < δ̄ < 2·10⁻⁸
([[eq:iii-i9-1-1]], [[def:ec-point]]) and (500002 + 4·10⁻⁶)² < 250002000009; ι_v increases with l. The number 3 is
one of the generators of Λ in [[def:iii-i10-1-1]]; no statement of this section uses whether another pole on the strip
lies in Λ, the bound of (c) holding at every exponent. For the last statement, by [[lem:sp-exceptional]]: these
numbers lie in 3/2 + σ_Υ + {1, 2, 3} ⊂ Q; they are not integers, not 4 + 𝔡₀ or 4 + 𝔡₁, and not ι₁ + j, as
ι₁ + j ∈ (j + 2, j + 5/2); and a number q ∈ Q equal to ι + j or ι_v(l) + j, with Re ι > 2 or ι_v(l) > 2, would give
ι = q − j ∈ Q or ι_v(l) = q − j ∈ Q, which [[lem:sp-exceptional]] excludes. ∎

**Remark {#rem:sp-scope}** (What the evaluation leaves open.) [[thm:sp-spectrum]] describes the poles exactly, by the
roots of the explicit polynomials P_l and p_(v). The vector type is in closed form, and for the scalar types with
x ≤ 70 the roots are enclosed by [[lem:s14-sextic-small]] and [[lem:s14-sextic-large]]; for x > 70 this paper locates
the roots of P_l only in {Re ι > 2} with no real root in (2, 5], and shows those of real part at most 5 simple, which
suffices for every statement above but leaves the largest l contributing a pole below real part 5 unevaluated. This
section does not determine the multiplicities of the indicial roots of real part at most 0 or in (4, 5]: they are 1
at real part in [−101, 5] ([[prop:is-mult]]) and at most 7 everywhere ([[prop:iii-f1-2-3]] (b)). Nor does it
determine L of [[cor:sp-lstar]] (a), which lies in [39, 50] ([[prop:is-logs]]); l_* = 50 is admissible for every
value of L in that range.

### The single-step losses at the computational point {#sec:cs}

[[thm:uc-integer]] bounds d_acc and d_R by D_e + M_c c_*, where c_* is the largest of the numbers c(β_k), c_b, c′_b and
c_0 defined before [[prop:ec-upper]] and of their counterparts c^Ψ(β_k), c^Ψ_b, c′^Ψ_b and c^Ψ_0 of [[lem:uc-dr]]. Each
of these numbers is assigned by [[def:ec-accounted-loss]] to a finite composition of elementary families. This section
lists, step by step, the families that each of them composes, bounds the charge of every one of them at the choice of
[[def:uc-choice]], and adds the charges. Two counts of index sets dominate the result: the count n_ι of the Fourier
transform in Step 0 of the proof of [[prop:iii-i11-3-1]], at most N_ι by [[lem:uc-n-iota]], and the count n_K of the
K⁺-exponents of the inverse transform in its Step 7, at most N_ι + N_Λ ([[lem:cs-fourier]]). A level step below 3 is
charged at most 497, a round and a step of the base at most 469 and 466, a level step above 3 at most
C_lev = 2N_ι + N̄_Λ + 529, with the bound N̄_Λ ≥ N_Λ below ([[lem:cs-levels]], [[lem:cs-base]]), and c_0, whose bound
counts three runs of the top level, less than 6N_ι + 1.74·10²⁸ ([[lem:cs-rest]]). So c_* < 6.4368·10³⁵
([[prop:cs-cstar]]).

Throughout we write

    N̄_Λ := 16,747,199,999,999,     k̄_max := 3 + 765,000,816 · N̄_Λ = 12,811,621,665,714,434,999,187,

so that N_Λ ≤ N̄_Λ and k̄(λ) ≤ k̄_max for every λ ∈ Λ with Re λ < 3 + ε_+ ([[lem:uc-lambda]] (a), (c)), and N_ι is the
number of [[eq:uc-n-iota]]. Weights, levels and the loss ε are those of [[def:uc-choice]]; in particular
3 + ε_+ < ℓ_I < 3.5, α ≤ 4 + ε_K, and ε ≤ 10⁻³ε_g < 10⁻¹².

#### The rule of addition and the free choices {#sec:cs-rules}

**Lemma {#lem:cs-sum}** (Charges add.) (a) Let an expression be built by compositions, sums and finite-rank
assemblies from applications of elementary families, each charged a non-negative integer. The number that
[[def:ec-accounted-loss]] assigns to it is at most the sum of the charges of the applications it contains.

(b) Let M be a map built in this way, ℓ_1, …, ℓ_m functionals computed by maps built in this way, and v^i = M(s^i) for
sources s^i whose families are charged at most 11. Then e ↦ M(e) + Σ_i ℓ_i(e)v^i is assigned at most
max(A_ℓ, A_M + 11), where A_M and A_ℓ are the sums of the charges of the applications in M and in the maps that give
the ℓ_i; in particular at most A_M + 11 when each ℓ_i is a coefficient functional (charge 0) of the output of maps
whose applications are among those of M.

*Proof.* (a) By induction over the expression: a composition is assigned the sum of the numbers of its factors, and a
sum or an assembly the largest of the numbers of its parts, which is at most their sum, all numbers being non-negative.
(b) The map is a sum of M and of a finite-rank assembly; [[def:ec-accounted-loss]] assigns the assembly the largest of
the numbers of its parts, the functionals (at most A_ℓ by (a)) and the families v^i (at most A_M + 11 by (a)). So the
sum is assigned at most max(A_M, A_ℓ, A_M + 11) = max(A_ℓ, A_M + 11). In the particular case the maps that give the ℓ_i
are among those of M, so A_ℓ ≤ A_M. ∎

Every elimination of finitely many parameters in [[ch:s20]]–[[ch:s23]] has the form of (b): by linearity and the
uniqueness of forward solutions, the forward solution for the forcing F − D_(p⃗)P(p⃗′) is the solution for F plus
Σ_i p′_i times the solutions for the fixed directions −D_(p⃗)P(e_i), which are background sources
([[lem:iii-j2-2-1]] (b)), and p⃗′ is a finite-dimensional linear function of coefficients read from the expansion of
the solution, that is, of coefficient functionals of outputs of the maps that compose M. This is the way in which the
finite-dimensional data enter in the proof of [[prop:ec-upper]]. So, by the particular case of (b), each statement
whose proof eliminates parameters is charged at most the sum of the charges of the statements it applies, each counted
once, plus 11.

**Definition {#def:cs-choices}** (The free orders and inner products.) At the choice of [[def:uc-choice]] we take,
besides:

(a) at the incoming radial sets of (2L_b)^(σ) and of N_tf((2L_b)^(·), ±1), the fibre inner product of
[[lem:ec-theta-in-zero]], in which ϑ_in = 0; at the horizon the fixed fibre inner product of [[lem:iii-f2-1-1]] with
δ = ¼, the neighbourhood ℬ_* being taken inside the neighbourhood of b₀ that this lemma gives, so that
ϑ_ℋ < ϑ_L + ¼ < 9/4 on ℬ̄_*; and the regularity order s_c := 3 > ½ + 9/4;

(b) in [[prop:ii-g1-4-4]], as [[cor:ii-g1-4-5]] applies it, the incoming order 𝗋_in := −¼ and the semiclassical order
𝖻 ≡ 0, and in [[cor:ii-g1-4-5]] the weight β′_I := 3/2 − 2ε where it is applied with an ℐ⁺-weight below 3/2;

(c) in [[lem:iii-i2-4-1]] the weights N := 21/4 of u_hi at ι⁺ and K⁺;

(d) in the proofs of [[lem:iii-i1-2-2]] and [[prop:iii-i1-2-1]], at each step other than Step 2 of the proof of
[[lem:iii-i1-2-2]], an increment η ∈ [2/5, ½) off the finitely many excluded values, or the remaining distance to the
target weight when that is smaller;

(e) in every application of [[cor:iii-f1-3-4]], the choices of [[prop:uc-ltf]];

(f) in the proof of [[thm:iii-i11-4-1]], an admissible level α′ ∈ (2, 2 + ε_g − 2ε), and in the proof of
[[prop:iii-i8-4-1]] at α′ the levels α_0 < α′, with α_0 ∈ (2, α′) admissible;

(g) in each application of [[lem:iii-a-1-4]] in [[lem:iii-i11-2-1]], at each step of its proof, the decrease of γ and the
number δ′ with sum at most ¼;

(h) as the order 𝗌 of the proof of [[thm:iii-i-5-3]] and of (B4) of [[sec:iii-h2-0]], the order of [[lem:fwd-orders]]
(s_in = 11, s_out = −10).

These choices are allowed. (a): [[lem:ec-theta-in-zero]] gives the inner product at the incoming radial sets,
which (O3) of [[def:i-a-admissible]] chooses separately for each radial set; [[lem:iii-f2-1-1]] gives ϑ_ℋ < ϑ_L + δ on a
neighbourhood of b₀ with ϑ_L = max(0, 2 − 2x) < 2; and the proofs of [[cor:ii-g1-4-2]], [[prop:ii-g1-4-7]],
[[lem:iii-i2-4-2]] and [[cor:ii-g1-4-5]] ask only s_c > ½ + ϑ_ℋ ([[lem:ec-closed-forms]] (b)). (b): the admissible orders
before [[lem:ii-g1-4-3]] ask 𝗋_out < −½ + S̄ = −½ and 𝗋_in ≥ 𝗋_out with 𝗋_in > ½(−1 + ϑ_in) = −½, and 𝗋_out =
β_scf − 2 − ε/2 < −½ for β_scf < 3/2; [[cor:ii-g1-4-5]] allows every β′_I below min(β_I, 3/2). (c): [[lem:iii-i2-4-1]]
holds for every N; its proof reaches the weights (·, N, N) through [[prop:ii-g1-3-5]] (1) and (2) at the K⁺-weight N,
which asks N ∉ ℕ, as 21/4 is; and every use of u_hi below needs at ι⁺ and at K⁺ weights below 21/4 (the targets are at
most 3 + η_2 at ι⁺ and α − ε < 5 at K⁺). (d): each step there asks only η < ½, α_I + η below the target, and finitely
many exclusions. (e) is [[prop:uc-ltf]]. (f): that proof takes any admissible α′ ∈ (2, 3), and the admissible levels
are the points of (2, 3) outside a finite set ([[sec:iii-i8-1]]), so (2, 2 + ε_g − 2ε) contains some; α_0 lies in
(2, min(a_K, 2 + ε_g, 5/2)), and α′ − α_0 < 1 < a_K − 2 for the background of [[thm:iii-i11-4-1]], whose K⁺-order
a_K is at least 4 + ε_K, so α_0 < α′ are levels as the proof of [[prop:iii-i8-4-1]] asks, with one level step. The
statements built on [[thm:iii-i11-4-1]] use α′ only as an admissible level in (2, 3), through
w_(α′) = min(α′ − 2, λ_♯ − 1) > 0 (Step 6 of the proof of [[thm:iii-i12-3-1]]); at a rotating b the elimination of
[[thm:iii-i11-4-1]] is [[prop:iii-i15-2-5]] with q = 0, whose base is at the level α_1 of [[def:uc-choice]]. (g): in
the proof of [[lem:iii-a-1-4]] the decrease of γ need only make γ avoid the real parts of spec_b(A) ∪ π₁F, which has
finitely many points in every strip, and δ′ > 0 is any small number; so both may be taken with sum at most ¼. (h):
[[lem:fwd-orders]] carries out the construction of [[sec:ii-c-5-2]] with these values, and B_1 is chosen after the order
([[sec:iii-h2-0]]), so (B4) holds for it on B̄_1.

#### The elementary charges {#sec:cs-elem}

**Lemma {#lem:cs-elem}** (The charges of the elementary families.) At the choices of [[def:uc-choice]] and
[[def:cs-choices]], every application of the following families in the constructions of [[thm:iii-i14-3-1]],
[[thm:iii-j1-2-1]] and [[lem:iii-k-2-3]] is charged at most:

(a) 0: finite-dimensional maps, coefficient functionals and finite-rank maps with fixed sections, among them the
inverses and functionals of [[lem:iii-j2-2-1]] (c), the assigned rotation coordinates A_b and the states, rows and
towers; the integrations of [[lem:iii-a-1-2]], [[lem:iii-a-3-2]] and [[lem:iii-i2-2-1]];
[[cor:iii-h-4-2]] and [[lem:iii-i2-4-3]]; multiplication by smooth functions, by cut-offs and by powers of σ, |σ| and
sgn σ; the Mellin inversion of an elliptic dilation-invariant operator on a line free of indicial roots; Cauchy
integrals and residues over fixed circles; the expansions of [[thm:iii-g4-3-1]] and of Step 2 of the proof of
[[prop:iii-g4-5-1]]; the tails of [[lem:iii-i10-2-4]]; [[lem:iii-i12-2-1]] (b); and the subtractions of
[[lem:iii-i12-2-4]];

(b) 1: [[prop:ii-g1-3-3]] (1), [[prop:iii-h-3-2]] (L̃_b(0)⁻¹) and [[cor:iii-f1-3-4]];

(c) 2: the fixed second-order operators L_b, L̂_b(σ) and L̃_b at the background 0, their parts L_0, L_1, L_2, and their
commutators with cut-offs;

(d) 11: the families of [[lem:iii-j2-2-1]] (b) applied to a solution or to a fixed section, among them the sources
f^S, f^b, f^s1, f^ν, r^ν, Δ_q, R_q, the errors E^ν, the differences (L − L_b)u, the remainder L̃ of [[lem:iii-i1-1-1]]
for L = L^(g,g_0), and the sources e_S, e_(S⁰) of the proof of [[lem:iii-k-2-3]];

(e) 20,183: the forward solution operators of [[lem:iii-j2-2-1]] (a);

(f) 3: [[prop:iii-g4-4-4]], for the solution and for the remainder; 2(⌊ℓ_zf⌋ − k₀ + 1)_+ + 3 ≤ 9:
[[prop:iii-g4-5-1]]; 1: [[thm:iii-g4-3-1]];

(g) 8: the expansion of [[lem:iii-a-1-4]] as [[lem:iii-i11-2-1]] applies it; so [[lem:iii-i11-2-1]] is charged at
most 9, and the map g ↦ g^(+1) of [[lem:iii-i11-2-2]] at most 2;

(h) 30: the right inverse of [[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1).

*Proof.* (a) These are the losses 0 of [[rem:ec-other-losses]] (the finite-dimensional maps of [[lem:iii-j2-2-1]] (c),
the integrations of its (d), [[cor:iii-h-4-2]] of its (e) and [[lem:iii-i2-4-3]] of its (g)). Multiplications by smooth
functions with bounded b-derivatives, and by |σ|^z, σ^j, sgn σ (which shift weights only), keep the order k. The Mellin
inversion of [[eq:iii-g4-5-3]] and of [[lem:iii-a-1-4]] gains, by (E1)–(E2) of [[sec:iii-a-1-1]], as many orders as the
operator has, jointly in the Mellin variable and on the boundary. A Cauchy integral over a fixed circle on which a family
is holomorphic and bounded at each order keeps the order. The expansions of [[thm:iii-g4-3-1]] and of Step 2 of the proof
of [[prop:iii-g4-5-1]] cost nothing, by the first fact in the proof of [[lem:ec-round-charges]]. [[lem:iii-i10-2-4]],
[[lem:iii-i12-2-1]] (b) and [[lem:iii-i12-2-4]] read coefficients and subtract finitely many terms, each a function of
t_* with finite-dimensional coefficients times a fixed profile; in [[lem:iii-i12-2-1]] (b) the remainder R is a sum of
explicit kernels e_(j,r) times the profiles, with the b-derivatives of the profiles at the same order.

(b) and (c) are the losses 1 and 2 of [[rem:ec-other-losses]], and ℓ_tf = 1 is [[prop:uc-ltf]].

(d) By [[prop:uc-dbg]], these families have split loss (2; 11, 2), so they are tame with loss 11, which is the charge
max(2, d_BG) = 11 of [[rem:ec-other-losses]]. The sources e_S and e_(S⁰) are differences of the sources f^S, f^s1 at
the two base points Φ(U) and Ψ(U), and D_hP_5(Ψ(U)) applied to the fixed sections χ_−∂_S H(S′), χ_−∂_(S⁰) H(S⁰′);
each is a coefficient polynomial in the metric, its inverse and their derivatives of order at most two applied to a
fixed section, and the proof of [[prop:uc-dbg]] applies to it. The errors
E^ν(W) = L_(h,p⃗)(h^(b₀)_ν − h^b_ν)(W) + δ*_(g_0,E_C)(ϑ^(b₀)_(ν,♯) − ϑ^b_(ν,♯))(W) of [[lem:s25-p6]] are differential
operators of order at most two with coefficients polynomial in the background, applied to fixed sections and linear
in the finite-dimensional W; the proof of [[prop:uc-dbg]] applies to them, and they are charged at most 11.

(e) By [[thm:fwd-loss]], [[eq:iii-i-5-2]] holds with d = 20,180 for g = g_0 + h, g_0 = g_(b₀,b₀,−S). At a base point with
parameter b ∈ ℬ̄_* these operators are those of [[cor:iii-h2-5-1]] ([[lem:iii-j2-2-1]] (a)), for which [[eq:iii-i-5-2]]
holds with the same d = 20,180 by [[cor:fwd-near-b0]], the order of (B4) of [[sec:iii-h2-0]] being that of
[[lem:fwd-orders]] ([[def:cs-choices]] (h)), as in [[thm:fwd-loss]]. By [[lem:iii-j2-2-1]] (a), for the backgrounds
h̃ = h + h^(−1)(S), h + h_tot(p⃗) and h + h_rem(q) + h_tot(p⃗) it holds with ‖h̃‖_(𝒳^(k+d)) in place of ‖h‖_(𝒳^(k+d)),
the backgrounds g₀ and h_tot(p⃗) adding coefficients smooth in p⃗. By [[lem:iii-i4-2-5]], [[lem:iii-i9-2-5]] and the
first paragraph of the proof of [[prop:uc-dbg]], ‖h̃‖_(𝒳^m) ≤ C_m(‖h‖_(𝒳^m) + |S| + |p⃗| + ‖q‖_(𝒬^(m+3))). So these
families satisfy [[eq:iii-j2-1-1]] with the loss 20,180 + 3 = 20,183.

(f) For [[prop:iii-g4-4-4]] this is the proof of [[lem:ec-round-charges]] (b), which uses nothing particular to the
levels 1 and 2: the solution costs at most ℓ_tf = 1 and the remainder ℓ_tf + 2 = 3, and the derivatives in α₀ of
Step 2 of its proof are Cauchy integrals. In the proof of [[prop:iii-g4-5-1]], Step 1 runs for
j = k₀, …, ⌊ℓ_zf⌋, at most 3 values, as ℓ_zf < 3. Each v_j solves [[eq:iii-g4-5-3]] at no cost, by (a), from
f^((j)), which is a coefficient of f minus g_j; g_(j+1), the terms of the second kind and the commutators apply to U_j
operators of order at most 2, the parts of L̂_b(σ) − L̄̂(σ), ρ(ρ∂_ρ − 3/2 − S̄) and the commutators with the cut-offs
(charge 2 by (c)); f₁ collects them. In Step 2, u₁ = N_tf⁻¹(|σ|^(−α)f₁) costs 1 by (b), its expansion
[[eq:iii-g4-5-5]] and u₂ cost nothing by (a), and f₁ − L̂_b(σ)u₂ costs 2. Along a chain these add to at most
2(⌊ℓ_zf⌋ − k₀ + 1)_+ + 1 + 2. [[thm:iii-g4-3-1]] composes [[cor:iii-f1-3-4]] with its expansion.

(g) In [[lem:iii-i11-2-1]], [[prop:iii-h-3-2]] costs 1. The expansion from the conormal order q − 2 > 0 to q′ − 2 ≤ 3
is obtained by the iteration of the proof of [[lem:iii-a-1-4]] with A = ρ⁻²L̂_b(0) near ∂X. A step from a weight w
reaches the weight γ = min(q′ − 2, w + 1), decreased slightly unless it is the target q′ − 2, and the next step starts
at γ − δ′; so each step that does not reach the target raises the weight by at least ¾ when its two small numbers, the
decrease of γ and δ′, are taken with sum at most ¼ ([[def:cs-choices]] (g)). As the first weight is above 0 and the
target at most 3, a fourth step starts above 9/4 and reaches the target; so at most 4 steps occur, and each applies
A − N(A), of order 2 (charge 2), followed by N(A, ·)⁻¹ and a contour shift (charge 0 by (a)). This gives 8, and
1 + 8 = 9. In [[lem:iii-i11-2-2]], g^(+1) is the explicit sum of that lemma: L_0, L_1, L_2 and commutators applied to
û (charge 2), and divisions by σ and the column terms, of charge 0.

(h) is [[lem:ec-closed-forms]] (f) at 3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ_ι < 3.5 − ℓ_I, which
[[def:uc-choice]] imposes, with the bound 2 + sup d_ι < l′ for the right inverse given in its proof. ∎

**Lemma {#lem:cs-transforms}** (Transforms and stationary inverses.) At the choices of [[def:uc-choice]] and
[[def:cs-choices]]:

(a) [[prop:ii-g1-3-3]] (2), applied to a forcing of weights (β^f_I + 1, β_ι + 2, β_K) with β^f_I ≤ ℓ_I, β_ι ≥ ½ and
β_K > 0, is charged at most 3;

(b) [[prop:ii-g1-3-5]] (1), and the transform bound (T3) inside [[prop:iii-a-4-2]], are charged
ℓ_F = ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉, which is at most 5 when β_ι − β_scf ≤ 5 and β_K ≤ 5;

(c) [[prop:ii-g1-3-5]] (2) is charged at most 5 in [[lem:iii-i2-4-1]], and 6 in [[cor:ii-g1-4-5]] there;

(d) [[cor:ii-g1-4-2]] (2) at β_scf = 3/2 − ε, and [[prop:ii-g1-4-7]] and [[lem:iii-i2-4-2]] at β_scf ∈ [3/2 − 3ε, 3/2),
are charged 2;

(e) [[cor:ii-g1-4-5]], as [[lem:iii-i2-4-1]] applies it, is charged at most 20, and [[lem:iii-i2-4-1]] at most 30;

(f) [[lem:iii-i2-3-1]], at its applications in the proofs of [[prop:iii-i2-5-1]], [[prop:iii-i3-2-1]] and
[[prop:iii-i5-2-1]], is charged at most 2.

*Proof.* (a) The loss of [[prop:ii-g1-3-3]] (2) printed in [[rem:ec-other-losses]] is
⌈(½ − min(β_K, β_ι + 1 − β^f_I))_+⌉ for a forcing of weights (β^f_I + 1, β_ι + 2, β_K). Here β_ι + 1 − β^f_I ≥
½ + 1 − 3.5 = −2 and β_K > 0, so it is at most ⌈5/2⌉ = 3.

(b) is the loss printed in [[rem:ec-other-losses]] and [[lem:ec-closed-forms]] (g); under the two conditions its
argument is at most 5 + ε − ½ < 5.

(c) In [[lem:iii-i2-4-1]], (1 − χ′)w has every σ-weight, so δ may be taken 3/2, and
β′ = max(N, N − (3/2 − 2ε)) = 21/4; the loss ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ is 0 + ⌈19/4⌉ = 5. In [[cor:ii-g1-4-5]],
δ = 1 and the output weights are (β′_I, N, N), so ℓ_3 = 1 + ⌈19/4⌉ = 6.

(d) By [[lem:ec-closed-forms]] (b), (c) with ϑ_in = 0 and s_c = 3, the losses are max(⌈(3 − β_scf)_+⌉, 2) and
max(⌈(5/2 + ε/2 − β_scf)_+⌉, 2). At the stated β_scf the first ceilings are ⌈3/2 + ε⌉ = 2 and at most
⌈1 + 7ε/2⌉ = 2.

(e) By the proof of [[cor:ii-g1-4-5]] its loss is ℓ + 1 with ℓ = 2ℓ_3 + ℓ_4 + ℓ_5 (⌈kδ⌉ ≤ 1 by
[[lem:iii-j2-2-1]] (f)). ℓ_3 = 6 by (c). ℓ_5 is the loss of [[prop:ii-g1-3-3]] (2) at the weights of the forcing,
at most 3 by (a): [[lem:iii-i2-4-1]] states β_ι > ½ at its applications, and β^f_I = ℓ_I there. ℓ_4 is the loss
ℓ_1 + ℓ_2 + 2ν + ⌈(δ_2 − δ_1)_+⌉ of [[prop:ii-g1-4-4]] with δ_1 = δ_2 = 0. In [[lem:ii-g1-4-3]],
ℓ_1 = max(⌈(s_c − 1)_+⌉, ⌈sup 𝗋 − 𝗋_out⌉) with sup 𝗋 − 𝗋_out = 𝗋_in − 𝗋_out = −¼ − (β_scf − 2 − ε/2) =
¼ + 3ε/2 at β_scf = β′_I + ε = 3/2 − ε, so ℓ_1 = 2; ℓ_2 = max(⌈(−s_c)_+⌉, ⌈𝗋_out − inf 𝗋⌉) = 0; and with 𝖻 ≡ 0 the
numbers ν_0 = ⌈(−min(𝖻_out, inf 𝖻))_+ + 1⌉, ν_1 = ⌈(−inf 𝖻)_+⌉ and their counterparts ⌈(max(𝖻_out, sup 𝖻))_+ + 1⌉,
⌈(sup 𝖻)_+⌉ for [[eq:ii-g1-4-3a]] are 1, 0, 1, 0, so ν = 1. Hence ℓ_4 = 4, ℓ ≤ 12 + 4 + 3 = 19 and the loss is at
most 20. In [[lem:iii-i2-4-1]] the rest w is obtained by [[prop:ii-g1-3-3]] (1) and (2) (charges 1 and 3, on the two
frequency ranges of one sum, so at most 3), then [[cor:ii-g1-4-2]] (2) (charge 2 by (d)), then [[prop:ii-g1-3-5]] (1)
at the weights (3/2 − 2ε, N, N) (charge ⌈19/4 + ε⌉ = 5) or (2) (charge 5 by (c)); so at most 3 + 2 + 5 = 10, and
20 + 10 = 30.

(f) By [[eq:ec-moment-loss]] the loss is max(⌈(β_K + ½ + ε)_+⌉, ⌈γ + ½⌉) with γ ≤ β_ι − β_I. The three applications
have (β_I, β_ι, β_K) = (3/2, γ_+ + 1, α̃_K − 1) with γ_+ < 3/2 and α̃_K < 1; (3/2, α^♯_+ + 1, α_K − 1) with
α^♯_+ < 7/4 and α_K < 3/2; and (3/2, α^♯_+ + 1, α̃_K − 1) with α^♯_+ < 2 and α̃_K < 2. In each, β_K + ½ + ε < 2 and
γ + ½ ≤ β_ι − β_I + ½ < 2, so the loss is at most 2. ∎

#### Null infinity and the Fourier steps {#sec:cs-null}

**Lemma {#lem:cs-null}** (The constructions at null infinity.) (a) Every application of [[prop:iii-i1-3-1]] in the
constructions is charged at most 6. (b) An application of [[prop:iii-i1-2-1]] with ℓ_+ < 3/2 whose a priori
ℐ⁺-weight α_I is at least −3/2 is charged at most 37 · 11 = 407. Every application below has α_I > ½.

*Proof.* (a) The operator of [[prop:iii-i1-3-1]] is L_b, with ρ_I⁻¹ρ_+⁻²L_b = L_0 + L̃ fixed ([[lem:iii-i1-1-1]]).
Step 1 of its proof solves for u^♭ by [[lem:iii-a-1-2]] and a fixed scalar (charge 0) and subtracts L_b v (charge 2).
Step 2 treats the windows [m_j, m_j + 1), m_j = min Re ℰ^C_I + j − 1 = 1 + j ([[prop:is-ci-pp]] (a): the least
exponent of ℰ^C_I is 2), with Re z ≤ ℓ_I < 3.5; so j ∈ {1, 2}. ℰ^C_I has logarithmic order 0 ([[prop:is-ci-pp]] (a)),
so k(F_I, z) = 0 at every z, and each term is solved once, by (z − 3/2 − Ā)⁻¹ and [[lem:iii-a-1-2]] (charge 0); the
terms of one window are independent, as L̃ moves the exponents by positive integers, out of the window. Each window
passes f − L_b(Σ_z χρ_I^z u^((z,0))) to the next (charge 2). So a chain is charged at most 2 + 2 · 2 = 6.

(b) Each step of the proofs of [[lem:iii-i1-2-2]] and [[prop:iii-i1-2-1]] applies L̃ of L = L^(g,g_0) once (charge 11,
[[lem:cs-elem]] (d)), the products ρ_I⁻¹ρ_+⁻²f and the integrations of [[lem:iii-a-1-2]] and [[lem:iii-a-3-2]]
costing nothing; so it suffices to count the steps, with the increments of [[def:cs-choices]] (d). Step 1 of the proof
of [[lem:iii-i1-2-2]] is run until the weight exceeds 1 + η₂, η₂ < (1 − e_Υ)γ_Υ < 0.01 being the number of its Step 2
(Step 2 needs L̃u at the weight 3/2 + η₂, and L̃ gains any η′ < ½); from α_I ≥ −3/2 this takes at most
⌈2.51/0.4⌉ = 7 steps. Step 2 is one step. Step 3 goes from 3/2 + η₂ to ℓ_I < 3.5 in at most ⌈2/0.4⌉ = 5 steps.
Step 1 of the proof of [[prop:iii-i1-2-1]] goes from α_I to below ℓ_+ < 3/2 in at most ⌈3/0.4⌉ = 8 steps, and its
Step 2 from there to ℓ_I in at most ⌈5/0.4⌉ = 13 steps. In all 7 + 1 + 5 + 8 + 13 = 34 ≤ 37 steps. At the
applications below the a priori ℐ⁺-weights are: β^(0)_I > ½ at the start of [[prop:iii-i2-5-1]] (the weight of
[[thm:iii-i-5-3]]), γ_+ − ε > ½ in its Step 3, and at least 1 − 5ε in [[prop:iii-i3-2-1]], [[prop:iii-i6-2-1]],
[[lem:iii-i8-3-2]] and [[prop:iii-i11-3-1]], whose remainders are sums of pieces of ℐ⁺-weight at least
min(3/2, α^♯_+) − 5ε > 1 − 5ε and of u_I, which has the ℐ⁺-data (⟨ℰ^C_I⟩, ℓ_I). ∎

**Lemma {#lem:cs-fourier}** (The Fourier steps of a level above 3.) Let β ∈ (3, α] be a level of Step 2 of the proof of
[[thm:iii-i14-3-1]], and consider the proof of [[prop:iii-i11-3-1]] at β (through [[prop:iii-i13-2-1]] when β < 4).

(a) The application of [[prop:iii-a-4-2]] (1) in its Step 0 is charged at most 9 + N_ι.

(b) In the application of [[prop:iii-a-4-2]] (2) in its Step 7, n_ι = 0 and n_K ≤ N_ι + N_Λ, and it is charged at most
N_ι + N̄_Λ + 2.

(c) The inverse transforms of the column pieces in its Step 5 ([[lem:iii-i11-2-4]]) are charged at most 5 each.

*Proof.* (a) is [[lem:uc-n-iota]] with [[lem:uc-fourier-count]] (with β_K = β − ε when β < 4): the charge is
1 + n_ι + 2⌊β − ε⌋ ≤ 1 + N_ι + 8. For a forcing in 𝒴^♮(β), [[prop:iii-i10-3-1]] (c) and [[lem:iii-i13-1-3]] (b) give
ℰ^♭ the hypothesis of [[lem:uc-n-iota]].

(b) Step 7 applies [[prop:iii-a-4-2]] (2) on each half with β_scf = 3/2 − 3ε, the tf-data (E_tf, β′_+ − 1), so
E_ι = E_tf + 1 and β_ι = β′_+ < 3/2, and the zf-data ((0, 0) ∪̄ (E_K − 1), β − 3 − ε), so β_K = β − 2 − ε. By
[[eq:ec-fourier-loss]] (2) its charge is n_ι + n_K + ℓ_F, where n_ι counts the pairs of E_tf of real part at most
β′_+ − 1 < ½, and n_K the pairs (d, m) of E_K − 1 with Re d ≤ β − 3 − ε < 1 + ε_K; E_tf and E_K − 1 are the smallest
index sets containing the tf-terms, resp. the zf-terms below these weights, of the pieces other than the columns with
constant coefficients.

*tf.* The pieces at zero energy are σ^jχ_zf û_j. By [[lem:iii-i11-2-1]], û_0 has at ∂X the exponents of
(ℰ^♭ − 1) ∪ (1 + ℰ_col) ∪ (2, ·) and their ℕ₀-shifts, of real part at least 1, as ℰ^♭ ⊂ {Re ≥ 2} and ℰ_col ⊂ {Re ≥ 0}
([[lem:iii-i11-1-1]]); for j ≥ 1, û_j has exponents of real part at least η_1 > 0 (Step 2), and the factor σ^j adds j at
tf. The pieces σ^ju_((α_0,k)) of [[prop:iii-g4-4-4]] have tf-exponents in α_0 − 2 + j + ((0, 0) ∪ ℰ_ind) and, from the
term with G^exc_(s1), in 2 + j and α_0 + j with ℰ_ind added (Step 1.1 of the proof of [[prop:iii-g4-4-4]]), all of real
part at least 1 (level 1: Re α_0 ≥ 2; level 2: Re α_0 ≥ 1 + η_1; min Re ℰ_ind > 0). The pieces of level 3 and of the last
level are conormal at tf, of tf-weight above 2, and so are the column pieces with non-constant coefficients
([[lem:iii-i2-4-3]]: tf-weight at least ℓ_3 + 2 − ε plus the powers of σ they carry). So E_tf ⊂ {Re ≥ 1} and n_ι = 0.

*zf.* By Step 5 (i), (ii) and (iv) of the proof of [[prop:iii-i11-3-1]], and [[lem:iii-i11-2-3]], the zf-terms of the
pieces are: terms of integer degree without log|σ| (the zero energy pieces, the column pieces and σ^jP_int); and, for
an application of [[prop:iii-g4-4-4]] at a tf-exponent (α_0, k) at the level j ∈ {1, 2}, the terms
σ^jc_τ(σ)(−iσ)^ih̆^i_τ of degree α_0 − 3 + j + i (s1), α_0 − 2 + j + i (v1) and α_0 − 2 − μ + j + i (the other rows,
μ a root of the table of [[eq:iii-g4-3-5]], Re μ ≤ 0), i ≥ 0, with logarithmic order at most k + 1 (the derivatives in
α_0 give log|σ| up to the power k, and a critical α_0 or β_μ one power more). At level 1, Re α_0 ∈ [2, 2 + η_1) and
α_0 ∈ Λ is the u-exponent; at level 2, Re α_0 ∈ [1 + η_1, 2 + η_2) and α_0 + 1 ∈ Λ is the u-exponent; and the
logarithmic order k at the tf-exponent is at most k̄ of the u-exponent ([[lem:iii-i10-1-2]] (c),
[[lem:iii-i13-1-3]] (b)). As Λ ∩ {Re ≤ 3 + ε_+} is real ([[prop:is-lambda]]) and meets (2, 2 + ε_K] in no point ((G)),
and as the roots of the table are real, and those with −1 < μ < 0 have −μ ≥ ε_ind > ε_K by [[eq:iii-f1-2-2]]
([[sec:iii-g4-1]], [[eq:iii-i9-1-1]]), a term of real part below
1 + ε_K is one of: at level 1, the s1 term with i = 0, of degree α_0 − 2; at level 1 with α_0 = 2, the s1 term with
i = 1, the v1 term with i = 0 and the terms of the rows with μ = 0 and i = 0, all of degree 1 = 3 − 2; at level 2, the
s1 term with i = 0, of degree α_0 − 1 = (α_0 + 1) − 2; and the integer degrees 0 = 2 − 2 and 1 = 3 − 2. So every pair
of E_K − 1 of real part below 1 + ε_K is (λ − 2, m) with λ ∈ Λ, 2 ≤ λ < 3 + ε_+, and m ≤ k̄(λ) + 1, where at degree 1
we use k̄(2) ≤ k̄(3) and 2, 3 ∈ Λ. The ℕ₀-shifts add nothing below 1 + ε_K except at the degree 0 + 1 = 1, as every other
degree has real part above ε_K. Hence, with λ_1 < ⋯ < λ_(N_Λ) as in [[lem:uc-lambda]] (c),

    n_K ≤ Σ_(i≤N_Λ) (k̄(λ_i) + 2) = N_Λ + 4N_Λ + 765,000,816 · N_Λ(N_Λ + 1)/2 ≤ N_Λ + N_ι

by the proof of [[lem:uc-n-iota]]. Finally ℓ_F = ⌈(max(β′_+ − 3/2 + 3ε, β − 2 − ε) + ε − ½)_+⌉ ≤ ⌈3/2 + ε_K⌉ = 2.

(c) By [[lem:iii-i11-2-4]], these are [[prop:iii-a-4-2]] (2) with E_ι = E_K = ∅ and the weights 3/2 − ε at ι⁺ and at
most α at K⁺, so their charge is ℓ_F ≤ ⌈α + ε − ½⌉ = 4 ([[lem:cs-transforms]] (b)). ∎

#### The level steps and the base {#sec:cs-steps}

**Lemma {#lem:cs-levels}** (The level steps.) Let 1 ≤ k ≤ K. (a) If β_k < 3, then c(β_k) ≤ 497. (b) If β_k > 3, then

    c(β_k) ≤ C_lev := 2N_ι + N̄_Λ + 529 = 214,558,790,360,052,785,818,485,009,600,000,520.            {#eq:cs-clev}

The same bounds hold at a rotating black hole parameter and for c^Ψ(β_k).

*Proof.* By [[lem:cs-sum]] we add the charges of the applications of each step, the windows, the transition face
rounds, the applications of [[prop:iii-g4-4-4]] at the levels 1 and 2 and the level-3 rounds being charged 0.

*The background terms of Step 2 of the proof of [[thm:iii-i14-3-1]].* The forcing G′ of [[eq:iii-i14-3-4]] is F minus
Δ_q(p⃗′), R_q u and the defects f^S(S′), f^b(b′), f^s1(S^(0)′_1) and r^ν(W′_ν); u_0 adds the rows m_ν(W′_ν). These are
summands, each a family of [[lem:cs-elem]] (d) or a finite-rank map with such sections; so they are charged at most 11
beyond the steps that compute u and p⃗′, which are other steps of the chain. At a rotating b, [[prop:iii-i15-2-5]] adds
the errors E^ν (charge 11) to the same sum and the coordinates A_b (charge 0); for ℛ(U), [[lem:iii-k-2-3]] adds the
sources e_S(S′) + e_(S⁰)(S⁰′) (charge 11) to it. In every case this sum is charged at most 11.

(a) The step is [[lem:iii-i8-3-2]] at β_k. Its Step 0 applies (L − L_b)u (11). Steps 1–2 apply [[prop:iii-i1-3-1]] (6,
[[lem:cs-null]] (a)) and L_b u_I (2), the windows being charged 0. Step 3 runs Steps 3–3.3 of the proof of
[[prop:iii-i6-2-1]] with α − ε′ for α_K: [[lem:iii-i2-4-1]] at β_ι = 2 − ε (30, [[lem:cs-transforms]] (e)),
[[prop:ii-g1-3-3]] (1) (1), L̃_b(0)⁻¹ (1), the terms of f̂_2, which apply [L̂_b(0), χ_zf], L̂_b(σ) − L̂_b(0) and the
columns (2), the division by σ (0), [[prop:iii-g4-5-1]] (9, [[lem:cs-elem]] (f)), [[lem:iii-i6-1-4]] (0), f̂_4 (2),
L̃_b(0)⁻¹ (1) and f̂_5 (2). Step 3.4′ runs its rounds (charged 0) and applies [[lem:iii-i2-4-2]] at β_scf = 3/2 − 2ε (2,
[[lem:cs-transforms]] (d)); the row terms U^((i)), B^((i)), Σ^((i))_r of [[lem:iii-i6-1-3]] are fixed sections
L̃_b(σ)⁻¹(0, E_k) times the coefficients of the row functional (0), and [[eq:iii-i8-3-3]] is a sum; so is
[[eq:iii-i6-2-8]] of Step 3.5′, whose row term (U_r, B_r, Σ_r) of Step 3.5 is of the same kind (0). Steps 4–5 of the
proof of [[prop:iii-i6-2-1]] apply [[prop:ii-g1-3-5]] (1) twice, at the output weights (3/2 − 4ε, 2 − 2ε, α_K − 1) and
(3 − 2ε, 3 − ε, α_K − 1) (5 each, [[lem:cs-transforms]] (b)), [[lem:iii-i3-1-3]], [[lem:iii-i2-4-3]] and
[[lem:iii-i2-2-1]] (0). Steps 6–7 read coefficients (0). Step 8 applies [[prop:iii-i1-2-1]] (407, [[lem:cs-null]]
(b)). With the background terms,

    11 + 11 + 6 + 2 + (30 + 1 + 1 + 2 + 9 + 2 + 1 + 2) + 2 + (5 + 5) + 407 = 497.

(b) The step is [[lem:iii-i13-2-2]] (at a rotating b [[lem:iii-i15-2-4]], which adds the coordinates A_b, charge 0),
whose proof is that of [[lem:iii-i11-3-2]]. Its Step 0 applies (L − L_b)u (11). Steps 1–2 are [[prop:iii-i10-3-1]] at
β_k: its Step 1 applies [[prop:iii-i1-3-1]] (6) and L_b u⁽⁰⁾_I (2); its Step 2 is a window loop (0); the rows are read
by [[lem:iii-i10-2-1]] (c) (0). Step 3 is [[prop:iii-i11-3-1]] at β_k (through [[prop:iii-i13-2-1]] when β_k < 4). Its
Step 0 applies [[lem:iii-i2-4-1]] at β_ι = 3 + ε_+ − ε (30) and [[prop:iii-a-4-2]] (1) (9 + N_ι,
[[lem:cs-fourier]] (a)). Steps 1, 2 and 3 each apply [[lem:iii-i11-2-1]] (9) and [[lem:iii-i11-2-2]] (2), the
applications of [[prop:iii-g4-4-4]] being charged 0. Step 4 applies, besides its rounds, [[lem:iii-i11-2-1]] (9; only
when β_k > 4), the subtraction that forms g_J (2) and [[lem:iii-i2-4-2]] at β_scf = 3/2 − 2ε (2). Step 5 reads the
tails by [[lem:iii-i10-2-4]] (0) and transforms the column pieces back (5, in parallel, [[lem:cs-fourier]] (c)). Step 6
reads coefficients (0). Step 7 applies [[prop:iii-a-4-2]] (2) (N_ι + N̄_Λ + 2, [[lem:cs-fourier]] (b)) and, near ℐ⁺,
[[prop:iii-i1-2-1]] (407). With the background terms,

    11 + 11 + 6 + 2 + 30 + (9 + N_ι) + 3 · (9 + 2) + (9 + 2 + 2) + 5 + (N_ι + N̄_Λ + 2) + 407
        = 2N_ι + N̄_Λ + 529,

and 2N_ι + N̄_Λ + 529 is the integer of [[eq:cs-clev]]. ∎

**Lemma {#lem:cs-base}** (The base.) c′_b ≤ 466 and c_b ≤ 469, also at a rotating black hole parameter and for ℛ(U).

*Proof.* *One step of [[prop:iii-i2-5-1]].* Step 1 applies (L − L_b)u (11). Step 2a applies [[prop:iii-i1-3-1]] (6) and
L_b u_I (2). Step 2b applies [[prop:ii-g1-3-3]] (1) (1), [[lem:iii-i2-4-1]] at β_ι = γ_+ > ½ (30), [[lem:iii-i2-4-2]]
at β_scf = 3/2 − ε (2), [[prop:ii-g1-3-5]] (1) at the output weights (γ_+ − ε, γ_+, α̃_K) (at most 5),
[[lem:iii-i2-4-3]] (0), [[lem:iii-i2-3-1]] (2, [[lem:cs-transforms]] (f)) and [[lem:iii-i2-2-1]] (0). Step 3 applies
[[prop:iii-i1-2-1]] (407). So c′_b ≤ 11 + 6 + 2 + 1 + 30 + 2 + 5 + 2 + 407 = 466.

*One round of [[prop:iii-i5-2-1]].* Step 0 applies (L − L_b)u (11). Step 1 applies [[prop:iii-i1-3-1]] (6) and
L_b u_I (2). Step 2 is the window loop (0). Step 3 runs Steps 2–3 of the proof of [[prop:iii-i3-2-1]]:
[[lem:iii-i2-4-1]] at β_ι = α^♯_+ > 1 (30), [[prop:ii-g1-3-3]] (1) (1), L̃_b(0)⁻¹ (1), the terms of f̂_2 (2),
[[lem:iii-i2-4-2]] at β_scf = 3/2 − ε (2), [[prop:ii-g1-3-5]] (1) at the output weights
(min(3/2, α^♯_+) − 3ε, α^♯_+, α̃_K) (at most 5), [[lem:iii-i3-1-3]], [[lem:iii-i2-4-3]] and the multiplication by
−iσ (0), [[lem:iii-i2-3-1]] (2) and [[lem:iii-i2-2-1]] (0); the coefficient S_0 is read at no cost. Step 4 applies
[[prop:iii-i1-2-1]] (407). So c_b ≤ 11 + 6 + 2 + 30 + 1 + 1 + 2 + 2 + 5 + 2 + 407 = 469.

At a rotating b the statements are those at b ((BP1)–(BP5), [[prop:iii-i2-5-1-b]]), with the same families; for ℛ(U)
the base point is Ψ(U), which the base sees only through the class of its background ([[lem:iii-k-2-3]]). ∎

#### The remaining steps {#sec:cs-rest}

c_0 contains, besides finitely many steps of the kinds above, the iterations of the top level and of one further base,
which the definition before [[prop:ec-upper]] charges in full. We bound these first.

**Lemma {#lem:cs-iterations}** (Iterations charged in full.) Put R_b := 61,038,200,000,000 and

    I_lev := 16 · 1,470,302 + 3 + 3 · 3,000,004 + 5 · 6,847,261,001 = 34,268,829,852,
    I_base := 469 R_b + 466 (R_b + 1) + 16 · 1,470,302 · (R_b + 3)
            = 1,435,970,471,299,470,574,962.                                                          {#eq:cs-iterations}

(a) A level step at β ∈ (3, α] ([[lem:iii-i13-2-2]] or [[lem:iii-i11-3-2]] at β), with its window loop, its
applications of [[prop:iii-g4-4-4]] at the levels 1 and 2 and its level-3 rounds charged as well, is charged at most
C_lev − 11 + I_lev along every chain.

(b) A base, that is, [[prop:iii-i8-4-1]] at a level in (2, 3) for a background of K⁺-order above a♭_K, with all its
rounds of [[prop:iii-i5-2-1]], steps of [[prop:iii-i2-5-1]] and windows charged as well, is charged at most
B + I_base along every chain, where B is the sum of the charges of its other applications.

*Proof.* (a) [[lem:cs-levels]] (b), without the 11 of the background terms of [[thm:iii-i14-3-1]], bounds the other
applications. By [[lem:ec-counts]] (e), [[lem:uc-gaps]] and [[prop:uc-explicit]], the window loop has at most 1,470,302
windows, each charged at most r_ι ≤ 16 ([[lem:ec-round-charges]] (c), [[lem:uc-admissible]]). By [[lem:ec-counts]] (d)
and the paragraph on the levels 1 and 2 in the proof of [[prop:ec-upper]], a chain meets at most one application at
level 1 and at most (1 + η_2 − η_1)/𝔡₁ + 1 < 3,000,004 at level 2 ([[prop:uc-explicit]]: (1 + η_2 − η_1)/𝔡₁ + 2 <
3.000005·10⁶), each charged at most ℓ⁺_tf + 2 = 3 ([[lem:ec-round-charges]] (b)). By [[lem:ec-counts]] (c) there are
fewer than 1/Δτ + 2 level-3 rounds, and 1/Δτ ≤ 1/Δτ_0 < 6.847261·10⁹ ([[prop:uc-explicit]]), so at most
6,847,261,001; each is charged at most ℓ⁺_tf + 4 = 5 ([[lem:ec-round-charges]] (a)).

(b) By [[lem:ec-counts]] (f) and [[prop:uc-explicit]], the rounds number at most N_b < R_b and the steps at most
N_b + 1, charged at most 469 and 466 by [[lem:cs-base]]; the window loops of the base are one per round and three more
(the proof of [[prop:ec-upper]]), each of at most 1,470,302 windows charged at most 16. For a background of larger
K⁺-order the rounds are fewer. The values in [[eq:cs-iterations]] are the products and sums written out. ∎

**Lemma {#lem:cs-rest}** (The remaining steps.) Put X_12 := 4k̄_max + 24 and

    T_11 := 20,183 + 1,914 + I_base + 22 + C_lev + I_lev,     T_12 := C_lev + I_lev + X_12.

Then

    c_0 ≤ 20,183 + 1,914 + T_11 + 2T_12 + 11 + d_Φ + (N̄_Λ + 2)(d_Φ + 30)                              {#eq:cs-c0}

with d_Φ = 62N_Λ + 2 ≤ 1,038,326,399,999,940, and the same bound holds for c^Ψ_0 and at a rotating black hole parameter.

*Proof.* c_0 is the largest charge along a chain of the remaining steps of the larger construction, that of
[[thm:iii-j2-4-2]]; we add the charges of all their applications, each statement counted once ([[lem:cs-sum]] and the
paragraph after it).

*Step 0* is one forward solution operator (20,183, [[lem:cs-elem]] (e)).

*Step 1, the base, its iterations of [[lem:ec-counts]] (f) and windows charged 0.* (1) The start of the proof of
[[prop:iii-i2-5-1]] applies [[prop:iii-i1-2-1]] to the forward solution (407). (2) [[prop:iii-i3-2-1]], outside the
steps of [[prop:iii-i2-5-1]] in its Step 0: (L − L_b)u (11), [[prop:iii-i1-3-1]] and L_b u_I (6 + 2), Steps 2–3 (the
43 of the round in the proof of [[lem:cs-base]]) and Step 4 (407): 469. (3) [[prop:iii-i4-4-1]] (1) and
[[cor:iii-i4-4-3]]: the parameter S″ (0), the forcing term f_(h,S)(S″) (11) and the recentring of [[lem:iii-i4-1-2]] (0):
11. (4) [[lem:iii-i8-3-1]], that is [[prop:iii-i6-2-1]] with its Steps 0–2 changed: Step 0 applies (L − L_b)u_F and
(L − L_b)u (22), its windows and the rounds of [[prop:iii-i5-2-1]] being charged 0; Steps 1–2 apply
[[prop:iii-i1-3-1]] and L_b u_I (8); Step 3 applies the 48 of Step 3 in the proof of [[lem:cs-levels]] (a); Step 3.4
applies [[lem:iii-i2-4-2]] (2), the row term being of finite rank (0); Steps 4 and 5 apply [[prop:ii-g1-3-5]] (1)
(5 + 5); Step 6 applies [[prop:iii-i1-2-1]] (407): 497. (5) [[sec:iii-i7-4]]: the parameters (0) and the sources f^S,
f^b, f^s1 (11): 11. (6) [[prop:iii-i8-4-1]] at α_1, whose levels are α_0 < α_1 (α_1 − α_0 < a♭_K − 2): the sources
f^ν and D_(p⃗)P_3 (11), the inverse T⁻¹ (0), and [[lem:iii-i8-3-2]] from α_0 to α_1, at most 497 by the proof of
[[lem:cs-levels]] (a) (its windows charged 0; it has no transition face round, as τ_0 = 2 + ε_g − 2ε exceeds
α_1 − ε′, α_1 − 2 < ε_K < ε_g − 2ε): 508. (7) Step 1 of the proof of [[thm:iii-i14-3-1]]: the terms by which P_5
differs from P_3, D_(W⃗)P_5 and Δ_q (11). In all 407 + 469 + 11 + 497 + 11 + 508 + 11 = 1,914.

*Steps 3, 4′ and 4, every step charged.* Step 3 inverts finite-dimensional maps (0). Step 4′ forms G̃_0 = F − Δ_q(p⃗′) −
R_q u − Σ_(ν∈𝒩_rot) f^ν(W′_ν), a sum of background terms (11), identifies p⃗′_0 through [[thm:iii-i11-4-1]] and expands u
by [[thm:iii-i12-3-1]]; Step 4 applies [[thm:iii-i12-3-1]] again. We charge each in full. G̃_0 is affine in the
finite-dimensional W⃗′^rot, and [[thm:iii-i11-4-1]] and [[thm:iii-i12-3-1]] are linear in F; so the applications in Step
4 are those of Step 4′, with W⃗′^rot entering by a finite-rank assembly, and no further application of
[[thm:iii-i11-4-1]] lies on a chain. [[thm:iii-i11-4-1]] applies [[prop:iii-i8-4-1]] at the level α′ of
[[def:cs-choices]] (f), a base whose level step α_0 → α′ has no transition face round (τ_0 = 2 + ε_g − 2ε exceeds α′ −
ε′, as in (6) of Step 1), at most 20,183 + 1,914 + I_base by [[lem:cs-iterations]] (b) (its forward solution, and the
1,914 of the base with the forward solutions at (h, p⃗)), the sources of F(W⃗) and G(W⃗) (11 + 11), and
[[lem:iii-i11-3-2]] at α, at most C_lev − 11 + I_lev by [[lem:cs-iterations]] (a); this is at most T_11.
[[thm:iii-i12-3-1]] applies, in its Step 0, the decomposition of the proof of [[lem:iii-i11-3-2]] at α (at most C_lev −
11 + I_lev), and beyond it at most X_12, as follows. In Step 1, the pieces (i)–(v) and (vii) are read by
[[lem:iii-i12-2-1]] (b) and Taylor's formula with fixed moments (0). In (vi) the zf-expansion of σ^jχ_tfρ_tf^(α_0−2)u_tf
costs nothing, and its zf-remainder is transformed back by [[prop:iii-a-4-2]] (2) with E_K = ∅ and with E_ι the tf-index
set plus 1, counted up to the ι⁺-order 3 + η_2 − 2ε: these are the exponents α_0 − 1 + j + m, m ∈ ℕ₀, with logarithmic
order at most k ≤ k̄_max, and at most 4 of them lie below 3 + η_2 (Re α_0 ≥ 2 at level 1, Re α_0 ≥ 1 + η_1 at level 2);
so n_ι ≤ 4(k̄_max + 1) and the charge is at most 4k̄_max + 4 + 5 (ℓ_F ≤ 5 by [[lem:cs-transforms]] (b), the output
weights being at most 3 + η_2 at ι⁺ and α − ε at K⁺). In (viii) the conormal coefficients are transformed by
[[lem:iii-i12-2-1]] (a), that is [[prop:ii-g1-3-5]] (1) (5), and the zf-remainder by [[prop:iii-a-4-2]] (2) with plain
tf-weight (5). In (ix), σ³û_f is transformed back with plain weights (5), and the columns by [[lem:iii-i12-2-2]], whose A
and B are [[prop:ii-g1-3-5]] (1) (5) and whose convolutions cost nothing. Steps 2–5 assemble, subtract by
[[lem:iii-i12-2-4]] and read coefficients (0). The pieces (i)–(ix) are summands of u, so by [[def:ec-accounted-loss]]
they are charged the largest of these charges, 4k̄_max + 9 < X_12; so [[thm:iii-i12-3-1]] is charged at most C_lev − 11 +
I_lev + X_12 < T_12. In all, Steps 3, 4′ and 4 are charged at most 11 + T_11 + 2T_12.

*The map U ↦ Φ(U)* has the loss d_Φ of [[lem:uc-phi-loss]], at most 1,038,326,399,999,940 ([[lem:uc-lambda]] (d)).

*Steps 1–3 of the proof of [[thm:iii-j1-2-1]].* Step 1 subtracts D_UΦ(U′_0 ⊕ 0), whose loss is at most d_Φ, Φ being
affine in U_1 with the loss d_Φ and smooth in U_0 ([[thm:iii-j-2-4]], [[rem:iii-j-2-5]]). Step 2 treats the exponents
of Λ_* in increasing real part, those of equal real part independently; at each it reads G′(λ₀) from the current
(h′, p⃗′, q′) (0), applies the right inverse of [[prop:iii-g3-3-7]] (30) in Case B, and subtracts D_UΦ(U′_(λ₀)) (at most
d_Φ), and the next exponent is read from the result. So a chain through Step 2 meets at most N_Λ exponents, each
charged at most d_Φ + 30. Step 3 subtracts D_UΦ(U′_c) (at most d_Φ). So Steps 1–3 are charged at most
(N_Λ + 2)(d_Φ + 30) ≤ (N̄_Λ + 2)(d_Φ + 30).

Adding gives [[eq:cs-c0]]. For ℛ(U) the base point is Ψ(U) and U ↦ Ψ(U) replaces U ↦ Φ(U); Ψ(U) − Φ(U) =
(χ_−h_(−S,−S⁰), 0, 0) is a smooth function of the finite-dimensional components (S, S⁰) of U ([[lem:iii-k-2-3]]), so
U ↦ Ψ(U) has the loss of U ↦ Φ(U), and D_UΨ(U′) − D_UΦ(U′) is a finite-rank map with fixed sections; the sources
e_S(S′) + e_(S⁰)(S⁰′) enter the forcings of Steps 1 and 2 as summands charged 11 ([[lem:cs-elem]] (d)), beside the
sources counted there. At a rotating b, [[prop:iii-i15-2-5]] adds the coordinates A_b (0) and the errors E^ν (11) as
summands of the same sums. So the bound holds for c^Ψ_0 and at every b ∈ ℬ̄_*. ∎

#### The bound {#sec:cs-bound}

**Proposition {#prop:cs-cstar}** (The largest single-step loss.) At the computational point, with the index sets as
constructed and the choices of [[def:uc-choice]] and [[def:cs-choices]],

    c_* ≤ 6N_ι + 3N̄_Λ + 17,389,163,815,025,371,354,557,103,786
        = 643,676,388,469,322,172,480,826,383,357,103,759
        < C_* := 643,680,000,000,000,000,000,000,000,000,000,000 = 6.4368·10³⁵.                        {#eq:cs-cstar}

*Proof.* By [[lem:cs-levels]] and [[lem:cs-base]], c(β_k), c^Ψ(β_k) ≤ max(497, C_lev) = C_lev and c_b, c^Ψ_b ≤ 469,
c′_b, c′^Ψ_b ≤ 466. By [[lem:cs-rest]], c_0 and c^Ψ_0 are at most the right side of [[eq:cs-c0]]. With
C_lev = 2N_ι + N̄_Λ + 529, this is

    2 · 20,183 + 2 · 1,914 + 33 + 3C_lev + 3I_lev + 2X_12 + I_base + d_Φ + (N̄_Λ + 2)(d_Φ + 30)
        = 6N_ι + 3N̄_Λ + 1,587 + 44,227 + 102,806,489,556 + 102,492,973,325,715,479,993,544
          + 1,435,970,471,299,470,574,962 + 1,038,326,399,999,940 + 17,389,059,886,080,535,910,399,999,970,

with 3I_lev = 102,806,489,556, 2X_12 = 8k̄_max + 48 = 102,492,973,325,715,479,993,544 and
(N̄_Λ + 2)(d_Φ + 30) ≤ 16,747,200,000,001 · 1,038,326,399,999,970 = 17,389,059,886,080,535,910,399,999,970. The seven
numbers after 6N_ι + 3N̄_Λ add up to 17,389,163,815,025,371,354,557,103,786, and with
6N_ι = 643,676,371,080,158,357,455,404,787,199,999,976 and 3N̄_Λ = 50,241,599,999,997 the sum is the integer of
[[eq:cs-cstar]], which is less than C_*. This bound exceeds C_lev, 469 and 466, so it bounds c_*. ∎

**Remark {#rem:cs-sharpness}** (What the bound counts.) Of the bound of [[eq:cs-cstar]], all but less than 1.74·10²⁸
is 6N_ι (C_* itself exceeds 6N_ι by less than 3.63·10³⁰): two counts of the logarithmic terms of Λ below 3 + ε_+ in
each of the three runs of the top level counted in the bound for c_0, each count being taken at the bound k̄(λ) of
[[def:iii-i10-1-1]] for the logarithmic orders. The next term,
(N̄_Λ + 2)(d_Φ + 30) < 1.739·10²⁸, comes from Step 2 of the proof of [[thm:iii-j1-2-1]], whose chain passes through
every exponent of Λ_* and composes the map Φ at each. A level step above 3 is charged at most C_lev ≈ C_*/3, and c_0
enters the second line of [[eq:ec-upper]] once; bounding that line by K·C_lev + 469N_b + 466(N_b + 1) + C_*, with
K < 1.22077·10¹⁴ ([[rem:ec-upper-point]]), instead of by M_c C_*, gives d_acc < 2.62·10⁴⁹. The bound is crude in
another way as well: n_ι and n_K count every pair (λ, k) with k ≤ k̄(λ), while the logarithmic orders that the
constructions produce are bounded in this paper only by k̄(λ).

### The first constants of the linear theory {#sec:ec-linear}

For the scalar wave operator on five-dimensional Tangherlini of mass 1, [[ch:resolvent-bounds]] gives explicit
constants: the resolvent cut off to I = {6/5 ≤ r ≤ 4} is bounded for every harmonic and every real 0 < |σ| ≤ 3
([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]]) and by 11.477 on 3 ≤ |σ| ≤ 384 ([[thm:band]]), with
the values of [[prop:band-points]] at sampled frequencies; there the constant bounding the radial derivative is at
most 283.06 for every l ≥ 1 and 305.31 at l = 0, and 308.46 bounds the radial derivative together with the angular
derivatives weighted by ψ, the weight of [[prop:morawetz-weight]], which vanishes at the photon sphere (unweighted at
l = 1), summed over the harmonics ([[cor:band-one-derivative]]). The same chapter makes explicit the factor of the
interpolation step of the high-energy inverses ([[lem:rb-interpolation]]: at most 1.002659 at b_0, the final black
hole, where κ_Γ = 2^(−3/2), with h_0 ≤ 1), replaces one of the inverse bounds by a parametrix
([[lem:rb-parametrix]]), bounds the resolvent of every master operator behind the mode stability of the 1-form wave
operator and of the linearised operator at every harmonic and every real frequency, carried exactly to the
tensor-type and vector-type blocks ([[prop:morawetz-master-potentials]], [[lem:rb-transfer]]), and writes out the
scalar-type blocks of the linearised operator at zero energy, with an upper bound for their least singular value that
obstructs a good constant at a weight next to an indicial root ([[sec:rb-scalar-blocks]], [[lem:rb-quasimode]]).

How far the upper bound of [[thm:band]] lies above the norm can be measured from below, since a test function supported
in I is its own resolvent.

**Lemma {#lem:ec-test-function}** (Lower bounds by test functions.) Let σ be real and nonzero, l ≥ 0, and let
u ≠ 0 be a function of r_*, supported in I, with u and u′ absolutely continuous and u″ ∈ L². Put
F := −u″ + (V_l − σ²)u. Then F ≠ 0, R_l(σ)F = u, and

    ‖χ_I R_l(σ) χ_I‖ ≥ ‖u‖/‖F‖.                                                                 {#eq:ec-test-function}

*Proof.* F lies in L² and vanishes outside I, V_l being bounded on I. If F were 0, u would solve the homogeneous
equation and vanish on an interval, so u = 0. The function u solves −u″ + (V_l − σ²)u = F and vanishes near −∞ and
near +∞, where it is the zero multiple of u_h and of u_∞; by the uniqueness in [[prop:resolvent-outgoing]] (a),
u = R_l(σ)F. As F = χ_IF and u = χ_Iu, ‖χ_I R_l(σ) χ_I F‖ = ‖u‖, which gives [[eq:ec-test-function]]. ∎

**Remark {#rem:ec-lower-bounds-observed}** (Numerical observation.) Polynomial test functions in the radial variable
on I, of degree up to 159 and vanishing to high order at the ends of I, evaluated in exact rational arithmetic with
the resolvent inverted exactly as in [[lem:ec-test-function]], give ‖χ_I R_l(σ) χ_I‖ ≥ 0.450, 0.250, 0.147, 0.0827,
0.0448 and 0.0241 at |σ| = 3, 6, 12, 24, 48 and 96, each at one harmonic; these are about 40 to 46 per cent of the
values of [[rem:rb-large-frequency-observed]]. With them, the bounds of [[prop:band-points]] would lie at most 19.8,
18.8, 40.8, 49.6, 67.5 and 93.5 times above the norm at these frequencies. The test functions are not printed here,
and no proof uses these values.

**Remark {#rem:ec-linear-observed}** (Numerical observation.) Three further constants of the linear theory at the
final black hole (mass 1, at rest) were evaluated, from exact identities with bounds in exact rational arithmetic and
certified enclosures, and are not proved in this paper: the zero-energy inverse bound of the scalar model, carried
into the low-energy norm of order 1 and weight −1 on the domain extended through the horizon, with constant 2.81; the
zero-energy inverse bound of the tensor-type blocks of the linearised gauge-fixed operator, at every harmonic and
through the horizon, with constant 3.94; and the data of the trapping estimate at the trapped set {r² = 2, ξ = 0}
(minimal expansion rate ν_min = 4·2^(−1/2), q^Γ = 4, β_Γ = 2), where, for the graded fibre inner products h_Γ(η)
of the trapping estimate of 2L_(b_0), the largest eigenvalue of the relevant symbol is η²(γ_C − 80·2^(1/2))²/(192γ_C)
to leading order in η, matched by enclosures at twelve points (γ_C = 10⁶, 10⁷, 10⁸; η = 10⁻¹, …, 10⁻⁴), so that the
estimate's condition needs η below about 16.48γ_C^(−1/2) and the condition number of h_Γ(η) is η^(−16). No proof uses
them.

**Remark {#rem:ec-not-evaluated}** (Where explicit evaluation stops.) The values of λ1 and δ are not determined in this
paper; [[prop:ec-delta-cap]] bounds λ1 by δ, δ by a power of 2 that decreases with d, and the modulus at 2δ, and they are
positive by the proof of [[thm:settling]]. Explicit values stop first upstream of every constant: the proof fixes the
gauge and damping parameters only below thresholds whose existence it proves ([[thm:vi-c-2-1]]), and the cut-offs and
orders of its function spaces only up to admissibility, so explicit constants need those choices made with numbers, which
this chapter does only at a point outside the proved set: [[def:ec-point]] for the gauge and damping parameters, and
[[def:uc-choice]] and [[def:cs-choices]] for the weights, orders and inner products on which d depends. Among the inputs
that depend on those choices are the gauge reconstruction, the inverse of the absorbed problem in the norms of [[ch:s01]]
(invertible by a Fredholm argument, [[lem:rb-absorbed]], which gives no bound), and a lower bound, uniform in the
harmonic, for the least singular value of the scalar-type blocks at zero energy ([[lem:rb-quasimode]] bounds it from
above). Four kinds of argument give a constant without a value: a compact error removed by injectivity, by contradiction
(the low-energy and Fredholm estimates of [[ch:s01]]–[[ch:s03]] and their analogues later); uniformity in the spectral
parameter and in the black hole parameters near the final one, by sequences and compactness; the trapping estimate, by a
defect-measure argument by contradiction ([[ch:s02]]), with the a priori constants built on it; and finite covers of
compact parameter sets. Bounds obtained from the closed graph, open mapping and uniform boundedness theorems, among them
the tame constants C_k of the membership statements ([[lem:iii-j2-1-2]] (f)), also give no value until each is read off
from the explicit estimates behind the statement. The parametrix norms at ι⁺ are not given by the construction of the
parametrix, and the tame constants to the order N_NM, the Nash–Moser thresholds of the exterior and slab problems and the
constants of the gluing are not evaluated. This is a limit of the explicit evaluation, not of [[thm:settling]].
