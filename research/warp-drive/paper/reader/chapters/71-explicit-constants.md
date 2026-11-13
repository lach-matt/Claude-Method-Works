## The loss of the tame estimates and the constants of the settling theorem {#ch:explicit-constants}

The proof of [[thm:settling]] applies the Nash–Moser theorem [[thm:ii-g-2-1]] to the gauge-fixed Einstein equation
with the tame estimates of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]. It applies it with one loss d of b-regularity
that does not depend on the order, at least the loss with which those estimates are proved ([[thm:iii-k-3-2]],
[[thm:loss-d]]), and [[thm:ii-g-2-1]] then asks smallness in the regularity N_NM = 21d + 6. The threshold λ1 on the
wavelength and the threshold δ on the data in [[thm:settling]] are produced by the proof, and are positive. This
chapter states what the proof makes explicit about d, N_NM, δ and λ1.

The loss of the tame estimates is a number d_acc assigned by the rules of [[lem:iii-j2-1-2]] to the composition of
model inverses, transforms and differential operators that the proofs of [[ch:s19]]–[[ch:s23]] perform
([[def:ec-accounted-loss]]), and d ≥ d_acc. Its elementary losses other than that of the forward solution operators
have closed forms in the weights, the threshold quantities of the operators, the index sets and the order of the
bounds of the background terms ([[lem:ec-closed-forms]], [[rem:ec-other-losses]]); the iterations of the
construction contribute their numbers of steps, among them three nested ones; and at one parameter point of the gauge
and damping parameters two of these iterations alone make d_acc, and so d, larger than 7.959 × 10¹⁵ and N_NM larger
than 1.671 × 10¹⁷, each of their steps being charged at least one derivative for the inverse of the model at the
transition face, whose incoming threshold is non-negative ([[lem:ec-theta-in]], [[thm:loss-d]]). That parameter point
lies outside the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds bound what this
proof's choices produce, not the optimal loss. No upper bound for d is proved: the loss of the forward solution
operators is fixed by its proof without a value ([[rem:ec-other-losses]]), and the upper bound for d_acc at one choice
of the weights in [[rem:ec-integer-bound]] is an observation. The same formulas bound δ and λ1 from above in terms of
d ([[prop:ec-delta-cap]]). The chapter ends with
the parts of the first constants of the linear theory that are in hand, and with the places where explicit evaluation
stops ([[rem:ec-not-evaluated]]).
No result of this chapter is used in the proof of any theorem of this paper.

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
at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and so does the lower bound of
[[thm:loss-d]] (see its proof).

### Sums of the gauge potential offsets {#sec:ec-gap-sums}

The gap condition (G) of [[def:iii-i10-1-3]] excludes exponents in windows just above 2 and 3. This section shows
that at the gauge parameters of the computational point the numbers of the set 𝒮 of [[prop:gap-sums]], built from 2,
3, λ_♯ and the gauge potential offsets defined below, stay out of those windows by a margin larger than δ_50, so that, on
these exponents, (G) imposes nothing beyond ε_K < ε_ind ([[rem:gap-sums]]). The elementary bounds, for a > 0 and
0 ≤ y ≤ 8a²,

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
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶. By [[prop:np-10-52]] (i), δ₂ = z(1 + θ₂)/15 and δ′₁ = 3z(1 + θ₁)/20 with
|θ₁|, |θ₂| ≤ z by [[eq:s14-theta]], so 2.666655·10⁻⁷ < δ₂ < 2.666678·10⁻⁷ and 5.999975·10⁻⁷ < δ′₁ < 6.000025·10⁻⁷.
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
those of [[thm:settling]]. No other result of this paper uses [[prop:gap-sums]].

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
symbols linear in η, p_in = i Re_h(A)(−i)(−2) = −2 Re_h(A) at ρ = 0. With S + S^(∗h) = 2 Re_h S this is [[eq:ec-theta-in]]. If
(A + S)v = μv with v ≠ 0 at a point of ∂X, then h(Re_h(A + S)v, v) = Re h((A + S)v, v) = (Re μ) h(v, v); so the
h-self-adjoint Re_h(A + S) has an eigenvalue at most Re μ there, p_in − (S + S^(∗h)) has one at least −2 Re μ, and
ϑ_in ≥ −2 Re μ.

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

(f) [[prop:iii-g3-2-4]] at finite regularity, and so [[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1): l′ = 2⌈ℓ_I⌉ + 10
+ sup d_ι over the strip; l′ = 30 when 3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ_ι < 3.5 − ℓ_I.

(g) [[prop:iii-a-4-2]]: with n_ι := n(E_ι, β_ι), n_K := n(E_K, β_K), n_I := n(E_I, β_I),
B := max(β_K, β_ι + max(0, −min Re π_1E_I)) and ℓ_F := ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉,

    (1):  l = 1 + n_ι + 2 max(n_K + ⌊β_K⌋, n_I + ⌊B⌋),     (2):  l = n_ι + n_K + ℓ_F.  {#eq:ec-fourier-loss}

(h) [[lem:iii-i2-3-1]]: with γ > 0 the number of its proof (β_ι − β_I when this is not an integer, β_ι − β_I − ε′
with the ε′ of that proof when it is) and ε ∈ (0, 1) the loss at which that proof applies [[prop:ii-g1-3-5]] (1),

    ℓ = max(⌈(β_K + ½ + ε)_+⌉, ⌈γ + ½⌉).                                                                {#eq:ec-moment-loss}

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

(f) The proof of [[prop:iii-g3-2-4]] at finite regularity applies [[lem:iii-g3-2-2]], with the loss
l = 2⌈ℓ_I⌉ + 10 of its statement, and then [[thm:iii-g1-3-1]] (2) on the strip, and takes l′ := l + sup d_ι. Here,
as in [[ch:s17]], λ ∈ ℂ is an exponent at ι⁺ with Re λ < ℓ_I (not the wavelength), and z is the variable of the
ι⁺-normal operator N_(ι⁺)(z).
The map of [[prop:iii-g3-3-7]] is continuous by [[prop:iii-g3-2-4]] on a strip containing λ, with the loss l′, and the
l of its statement is this l′ (that of [[lem:iii-g3-3-5]]). Its right inverse applies the map u ↦ f of the proof of
[[lem:iii-g3-3-5]], which applies the second-order operator N_(ι⁺) (loss 2), splits f = f₁ + f₂, keeps f₂, and maps
f₁ to res_(z=λ)(t_*^(−z)N_(ι⁺)(z)⁻¹f₁(z)): a map of finite rank into the finite-dimensional space Res_(ι⁺)(L̄, λ) of
[[def:iii-g3-3-6]], whose coefficients are integrals of the inverse of [[thm:iii-g1-3-1]] (2) over a small circle
about λ in the strip, so bounded by the norm of order sup d_ι of f₁. So the right inverse costs at most
2 + sup d_ι < l′ ([[lem:iii-j2-1-2]] (b), (c)), and the loss of [[prop:iii-g3-3-7]] is l′. [[cor:iii-g3-3-1]] (1)
comes from [[prop:iii-g3-2-4]] on a strip
containing its exponent, with the loss l′; its expansion (2) costs nothing beyond, and its continuous functionals are
counted where a construction that uses them adds its losses. For 3 < ℓ_I < 3.5, ⌈ℓ_I⌉ = 4 and sup d_ι = 12 by (e),
so l′ = 8 + 10 + 12 = 30.

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
k − j derivatives, this costs ℓ_+(γ + 1) = ⌈γ + ½⌉, as γ > 0. The same proof needs ℓ ≥ 1 for the bound
|ℱf_1(σ)| ≤ C|σ|^γ, which ⌈γ + ½⌉ ≥ 1 gives. Every other step, the integrations of [[lem:iii-i2-2-1]] and
[[lem:iii-a-1-2]] and the multiplication by χ, keeps the order k. This is [[eq:ec-moment-loss]]. ∎

**Remark {#rem:ec-other-losses}** (The other elementary losses.) The remaining elementary losses of
[[lem:iii-j2-2-1]] are fixed in its statement:

- 0 for finite-dimensional maps (its (c)), for the integrations along faces of [[lem:iii-a-1-2]], [[lem:iii-a-3-2]]
  and [[lem:iii-i2-2-1]] (its (d)), for [[cor:iii-h-4-2]] on |σ| < c_k (its (e)) and for [[lem:iii-i2-4-3]] (its (g));
- 1 for [[prop:ii-g1-3-3]] (1) and [[prop:iii-h-3-2]];
- where they are applied outside [[prop:iii-a-4-2]], the losses printed in their statements:
  ⌈(½ − min(β_K, β_ι − β_I))_+⌉ for [[prop:ii-g1-3-3]] (2), ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉ for
  [[prop:ii-g1-3-5]] (1) and ⌈(3/2 − δ)_+⌉ + ⌈(β′ − ½)_+⌉ for [[prop:ii-g1-3-5]] (2), each at the weights of the
  application;
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

[[lem:ec-closed-forms]] (h) gives the loss of [[lem:iii-i2-3-1]]. The forward solution operators of
[[lem:iii-j2-2-1]] (a) lose the d of
[[thm:iii-i-5-3]], which its proof takes from [[thm:ii-f1-1-1]] and raises by 6. There d = D_0 + D_1 + d′ + d″
([[eq:ii-f1-3-3]]): d′ and d″ are read off the order 𝗌, while D_0 and D_1 are maxima of the orders d_0 and d of the
energy estimates of [[ch:s07]] and of [[lem:ii-f1-2-8]] ([[eq:ii-f1-3-2]]), whose existence is proved and whose values
are not determined in this paper. The order of choices behind ℓ + 1 is: d_acc and d_NM first, then N_NM, then the
trapping data at the orders k ≤ N_NM ([[cor:iii-h2-1-2]]); the constants of the smallness conditions are used at those
orders only, the tame estimates themselves at every order. The statement "d_acc is an explicit number" needs, besides
these closed forms, values of D_0 and D_1 and of the order d_BG, numbers for the weights at the parameters in
question, the index sets n(E, β) and the numbers of steps of the iterations of the inventory of [[sec:iii-j2-3]]; the
next section bounds two of these iterations from below. The forward solution operators are a factor of the
construction of [[thm:iii-i14-3-1]] (Step 0 of its proof), so d_acc is at least their loss, and an upper bound for
d_acc would bound D_0 + D_1. An upper bound for d_NM would need upper bounds for the losses of [[lem:iii-k-2-2]] and
[[prop:iii-j2-4-3]] and for that of [[lem:iii-k-2-3]], which is at least d_acc. None is proved here;
[[rem:ec-integer-bound]] records one for d_acc at one choice of the weights.

### Two long iterations, and a lower bound for d {#sec:ec-floor}

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

**Proposition {#prop:ec-rounds}** (The number of rounds.) At the computational point, for every choice of ε_K, ε_+,
η_2, α, the levels and the losses ε, ε′ admissible for [[thm:iii-i14-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i13-2-1]], the transition face rounds at the levels below 3 and the level-3 rounds at the levels in (3, 4)
number together

    R > (1 − 6δ̄)/(ε_K δ_50) > (1 − 6δ̄)/δ̄² > 2.6532 × 10¹⁵.

The same bound holds at every h ∈ 𝖧, with the same (γ_Υ, e_Υ).

*Proof.* The weights satisfy 0 < ε_K < ε_g ≤ ε_ind ≤ δ_50: the first inequality is the hypothesis ε_K < ε_+ < ε_ind
together with ε_K < ε_Υ of [[thm:settling]], and ε_ind ≤ δ_50 is [[prop:np-10-52]] (iii) (with equality at h = 10⁻⁶,
[[cor:s14-eps-ind-point]]). Also η_2 < ε_+ < ε_ind. The loss ε′ of [[lem:iii-i8-3-2]] satisfies ε′ ≤ ε: Steps 4–5
of its proof give ũ the K⁺-weight α − 2 − ε′, while its conclusion at the output loss ε, at which the tame accounting
takes it ([[sec:iii-j2-1]]), is the K⁺-weight α − 2 − ε, so a run of the proof that gives it has ε′ ≤ ε. And
ε ≤ ε_1 < ε_+/5 ([[sec:iii-j2-1]]). So ε, ε′ and η_2 are below δ_50. The level spacing is below α − 4 ≤ ε_K, and each
round raises the tf-weight by ε_g − ε < δ_50.

*Below 3.* At a level β ∈ (2, 3), τ_i < 2 + δ_50 + iδ_50, and the rounds run for every i with τ_i ≤ β − ε′, the τ_i
being increasing; so their number is at least the number of i ≥ 0 with 2 + δ_50 + iδ_50 ≤ β − δ_50, which is at
least g_1(β)/δ_50 with g_1(x) := (x − 2 − 2δ_50)_+. The levels in (2, 3) form a sequence b_1 < ⋯ < b_m with
b_1 = α_1 < α − 2 ≤ 2 + ε_K, and b_m > 3 − ε_K, because the next level exceeds 3 and lies within ε_K of b_m. By
[[lem:ec-level-sum]] with c = ε_K, and as g_1 vanishes below 2 + 2δ_50 > b_1,

    Σ_j g_1(b_j)/δ_50 ≥ (1/(ε_Kδ_50))(∫_(2+2δ_50)^(3−ε_K) (x − 2 − 2δ_50) dx − ε_K/2)
                      = (1/(ε_Kδ_50))((1 − ε_K − 2δ_50)²/2 − ε_K/2) > (½ − 3.5δ̄)/(ε_Kδ_50).

*Between 3 and 4.* At a level β ∈ (3, 4), κ_i := κ_3 + i(ε_g − ε) < 1 + δ_50 + iδ_50, and the rounds run for every i
with κ_i ≤ β − 2; their number is at least g_2(β)/δ_50 with g_2(x) := (x − 3 − δ_50)_+. The levels in (3, 4) form a
sequence c_1 < ⋯ < c_p with c_1 < 3 + ε_K (the previous level lies below 3 within ε_K) and c_p > 4 − ε_K (the next
level is at least 4, as β_(K−1) > 4, and lies within ε_K). By [[lem:ec-level-sum]],

    Σ_j g_2(c_j)/δ_50 ≥ (1/(ε_Kδ_50))((1 − ε_K − δ_50)²/2 − ε_K/2) > (½ − 2.5δ̄)/(ε_Kδ_50).

Adding, R > (1 − 6δ̄)/(ε_Kδ_50); with ε_K < δ_50 < δ̄ this exceeds (1 − 6δ̄)/δ̄² = 2.65327…·10¹⁵. Nothing in the proof
used h beyond ε_ind(h) ≤ δ_50. ∎

**Theorem {#thm:loss-d}** (The loss d and the regularity N_NM.) Let d_acc be the accounted loss of
[[def:ec-accounted-loss]], and d_NM the loss with which the proof of [[thm:iii-k-3-2]] applies the Nash–Moser theorem
[[thm:ii-g-2-1]]: the largest of the losses of [[lem:iii-k-2-2]], [[lem:iii-k-2-3]] and [[prop:iii-j2-4-3]], that of
[[lem:iii-k-2-3]] accounted by [[def:ec-accounted-loss]]. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with
d = d_acc, [[thm:ii-g-2-1]] is applied at the regularity N_NM = 21d_NM + 6, d_NM ≥ d_acc, and:

(i) d_acc is composed, by the rules of [[def:ec-accounted-loss]], of elementary losses and of the numbers of steps of
the iterations of the inventory of [[sec:iii-j2-3]], among them the three of [[sec:ec-floor]], each round of those
three and of the iteration at ι⁺ of [[prop:iii-i5-2-1]] being charged at least the loss of [[lem:ec-round-loss]]; the
elementary losses are closed forms in the weights, the small numbers that the proofs choose, the thresholds ϑ_in,
ϑ_ℋ, the regularity orders s_c, the counts n(E, β) of the index sets and the order d_BG of the bounds of the
background terms ([[lem:ec-closed-forms]], [[rem:ec-other-losses]]), except the loss of the forward solution
operators, which the proof of [[thm:iii-i-5-3]] fixes without a value ([[rem:ec-other-losses]]);

(ii) at the computational point, for every admissible choice of the weights there,

    d_acc ≥ Σ_rounds (2 + ℓ_tf) ≥ 3R > 7.959 × 10¹⁵,        N_NM ≥ 21d_acc + 6 > 1.671 × 10¹⁷,

with R the number of rounds of [[prop:ec-rounds]], the sum over those rounds, and ℓ_tf ≥ 1 the lower bound of
[[lem:ec-closed-forms]] (d) for the loss of [[cor:iii-f1-3-4]] at the weights of each round.

These are lower bounds for the loss that this proof's choices produce, not for the least loss with which the tame
estimates hold. No upper bound for d_acc or d_NM is proved in this paper ([[rem:ec-other-losses]]).

*Proof.* [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d_acc by [[lem:iii-j2-1-2]], which gives the tame
estimates with any loss at least the accounted one; N_NM = 21d_NM + 6 is the regularity of [[thm:ii-g-2-1]] at the
loss d_NM ([[eq:ii-g-2-5]]). *d_NM ≥ d_acc.* Hypothesis (iii) of [[thm:ii-g-2-1]] asks [[eq:ii-g-2-4]], with the loss
d_NM, of the right inverse Zℛ(U) of the proof of [[thm:iii-k-3-2]], where ℛ(U) is that of [[lem:iii-k-2-3]] and the
multiplication Z loses nothing; so the loss of ℛ(U), the loss of [[eq:iii-j2-4-2]] for it, is one of the three whose
largest is d_NM. By the proof of [[lem:iii-k-2-3]], ℛ(U) is the construction of [[thm:iii-j2-4-2]] at the base point
Ψ(U), with two more terms, linear in the finite-dimensional boost and translation components, added to the forcing
of Step 2 of the proof of [[thm:iii-i14-3-1]] and entering its Steps 1 and 3 as terms of the same kind; and the
construction of [[thm:iii-j2-4-2]] applies that of [[thm:iii-j2-4-1]] to the right side and assembles U′ from its
output by maps of non-negative loss (Step 0 of the proof of [[thm:iii-j1-2-1]]). The elementary losses do not depend
on the base point ([[lem:iii-j2-2-1]]: only its constants do). By [[def:ec-accounted-loss]], a further summand does not lower the
largest of the losses of a sum, and a further factor of non-negative loss does not lower the loss of a composition;
so the loss of ℛ(U) is at least the numbers assigned to both constructions, and d_NM ≥ d_acc. (i) is
[[def:ec-accounted-loss]] with [[lem:ec-closed-forms]], [[rem:ec-other-losses]] and [[lem:ec-round-loss]].

(ii) Level k + 1 of [[thm:iii-i14-3-1]] takes the solution of level k as input through R_qu, and at each level the
rounds of [[sec:ec-floor]] are composed one after another, each round's output being the next round's forcing, and
the level's solution being assembled from the outputs of all its rounds and from the inverse applied to the last
forcing. So all the rounds of all the levels lie on one chain of compositions, and by [[def:ec-accounted-loss]] and
[[lem:ec-round-loss]] (a), d_acc ≥ Σ_rounds(2 + ℓ_tf). By [[lem:ec-closed-forms]] (d), whose proof uses
[[lem:ec-theta-in]], ℓ_tf ≥ 1 at every round; so by [[prop:ec-rounds]], d_acc ≥ 3R > 3(1 − 6δ̄)/δ̄² = 7.9598…·10¹⁵,
and N_NM = 21d_NM + 6 ≥ 21d_acc + 6 > 21 · 7.959 × 10¹⁵ > 1.671 × 10¹⁷. Every lower bound of this chapter is a lower
bound for d_acc, and holds for d_NM and N_NM because d_NM ≥ d_acc and N_NM increases with d_NM. ∎

### What the proof's formulas give for δ and λ1 {#sec:ec-delta}

**Proposition {#prop:ec-delta-cap}** (Upper bounds for δ and λ1.) In the proof of [[thm:settling]], let d be the loss
d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] (d ≥ d_acc, [[thm:loss-d]]), and let the Nash–Moser
threshold be ε_NM = θ_0^(−(8d+2)), with θ_0 as chosen in the proof of [[thm:ii-g-2-1]]. Let C_(2d) and ω_(2d) be the
constant and the modulus of [[lem:iii-k-2-2]] (d) at the order 2d, in the norm of H^(2d+k′_(2d)), enlarged if
necessary so that C_(2d) ≥ 1 and ω_(2d)(s) ≥ s, and let the data threshold ε of [[cor:s27-rate]] satisfy
C_(2d)ω_(2d)(ε) ≤ ε_NM; and let C_R ≥ 1 be the constant of [[cor:vii-2-3]]. Then δ = ½ε and λ1 satisfy

    δ ≤ 2^(−(32d+9)),        λ1 < δ,        log₁₀ δ < −(59/196)(32d + 9).

As d ≥ d_acc, the bound of [[thm:loss-d]] (ii) gives log₁₀ δ < −7.666 × 10¹⁶; the same bound holds for λ1.

*Proof.* Replacing ω_(2d) by s ↦ max(ω_(2d)(s), s) and C_(2d) by max(C_(2d), 1) keeps [[lem:iii-k-2-2]] (d) true and
keeps ω_(2d) non-decreasing with limit 0 at 0, so the proof of [[thm:iii-k-3-2]] runs with them unchanged. Then
ε ≤ ω_(2d)(ε) ≤ C_(2d)ω_(2d)(ε) ≤ ε_NM. The proof of [[thm:ii-g-2-1]] chooses θ_0 ≥ 16η_0^(−2) with η_0 ≤ 1, so
θ_0 ≥ 16 and ε_NM ≤ 16^(−(8d+2)) = 2^(−(32d+8)). So δ = ½ε ≤ ½ε_NM ≤ 2^(−(32d+9)). The proof of [[thm:settling]]
([[sec:vii-4]]) takes λ1 with C_Rλ1 < ½ε = δ, so λ1 < δ/C_R ≤ δ. Next, 2^10 = 1.024·10³, so
2^196 = 2^190·2^6 = 1.024^19·10^57·64, and by the binomial expansion, all of whose terms are positive,
1.024^19 > 1 + 19x + 171x² + 969x³ > 1.5678 > 100/64 with x = 0.024; so 2^196 > 10^59 and log₁₀ 2 > 59/196, which
gives the third bound. With d ≥ d_acc > 7.959 × 10¹⁵, (59/196)(32d + 9) > 7.666 × 10¹⁶. ∎

The bounds hold whatever the other constants are, once C_(2d), ω_(2d) and C_R are enlarged as above, which keeps the
estimates in which they enter true. A lower bound for δ or λ1 would need lower bounds for θ_0^(−1), for the inverse of
the modulus s ↦ C_(2d)ω_(2d)(s) and for 1/C_R, that is, upper bounds for every constant of the proof that enters them;
[[rem:ec-not-evaluated]] says where those stop.

### The loss at the computational point {#sec:ec-integer}

The numbers of steps of the iterations depend on the weights, which the proof fixes only by inequalities. At one
choice of the weights at the computational point the bookkeeping of [[def:ec-accounted-loss]] has been carried to an
integer. The following two remarks report it; no proof uses them.

**Remark {#rem:ec-weights-observed}** (Numerical observation.) At the computational point take ε_ind = 19·10⁻⁹,
ε_+ = 189·10⁻¹⁰, ε_K = 188·10⁻¹⁰, ε = ε′ = 10⁻¹², η_2 = ε_+ − 3ε, ℓ_I = a_I = 13/4, α = 4 + ε_K, α_1 = 2 + ε_K/2 and
the levels β_k = α_1 + k·(0.999ε_K), k < K = 106,489,469, with β_K = α, so 106,489,470 levels counting the top
(53,244,734 below 3, 53,244,734 in (3, 4) and two above 4); all are rational with common denominator 5·10¹², the
transition face rounds start at τ_0 = 2 + ε_ind − 2ε and the level-3 rounds at τ_3 = 1 + η_2 − 2ε, both rising by
ε_ind − ε, which are the increments ε_g − ε of [[sec:ec-floor]] when ε_g = ε_ind. Summed exactly as floor sums over the
levels, the transition face rounds below 3 number 1,401,250,931,461,121 and the level-3 rounds above 3 number
1,401,251,031,977,897, so that three times their sum is 8,407,505,890,317,054 ≈ 8.41 × 10¹⁵, the exact value at these
weights of the lower bound 3R of [[thm:loss-d]] (ii). At these weights every admissibility condition checked holds:
the levels and the round weights are rational, every indicial root of L̂_(b_0)(0) they can meet is an integer or
irrational (one family of roots of the damping operator could have a fixed fractional part, which no level or round
weight has), the rational coincidences that remain are not levels, and the least distance of a level from the excluded
values is at least 3.18·10⁻¹⁶; the gap condition (G) holds by [[prop:gap-sums]], also with the least index set of
the class data adding 23 chains, none coming nearer than 3 + 5.019·10⁻⁸. These were decided in exact rational
arithmetic and by certified enclosures of the irrational roots, at the scale of 10⁸ levels; they are not proved in
this paper.

**Remark {#rem:ec-integer-bound}** (Numerical observation.) At the weights of [[rem:ec-weights-observed]], with the
least index sets E^C_I and E_+ that the proof admits, the base level's starting values a_K − 2, s_0, τ, t and
α_0 := α_1, the order 14 for the error terms of the calculus (any order at least 10 serves), the class window taken
wide and the window loop at its ceiling, every step of the construction was charged an upper bound: the elementary
losses by [[lem:ec-closed-forms]], with ℓ_tf = 1 (the transition face model's incoming threshold being 0 there), the
forward solution operators D_0 + D_1 + d′ + d″ + 6 ≤ 766 + 88 + 8 + 9 + 6 = 877 ([[rem:ec-other-losses]]), with D_0
and D_1 bounded over the orders at which the calculus of [[ch:s04]] is used, the round of the iteration at ι⁺ charged
15 derivatives when ℓ_I ∈ (3, 3.5) and 4 more for each further unit of ℓ_I (19 on (3.5099, 4.5), then 23, 27 and 31
up to ℓ_I = 7.5, with 17, 21, 25 and 29 on the short windows [k + 1/2, k + 0.5099] where a step is added before d_ι
rises), the steps of each level taken from the families that the inventory of
[[sec:iii-j2-3]] lists (212 uses in the levels and 89 in the base level's loops), the logarithmic orders of the index
sets by induction over the construction's steps, and the index set at ι⁺ left unlisted by the construction computed
from the constructions that define it (it adds no exponent). The applications of the level-2 step at one exponent act
on separate terms of one forcing and none on another's output, so their losses do not add, and the count is the same
whether that step is read once per exponent or once per exponent and power of the logarithm. The result is
d_acc ≤ 46,236,517,538,883,361 ≈ 4.624 × 10¹⁶ and N_NM ≤ 970,966,868,316,550,587 ≈ 9.710 × 10¹⁷ (of which the base
level's loops contribute 5.75 × 10¹⁴; with the calculus at order 10, d_acc = 46,236,501,332,809,678), against the
lower bound 8.41 × 10¹⁵ at the same weights; at d = 46,236,517,538,883,361 the bound of [[prop:ec-delta-cap]] reads
log₁₀ δ < −4.45 × 10¹⁷. The count depends on the point: the windows of one construction step,
⌈(2 − ε − λ_♯)/𝔡₁⌉ = 1,470,302 at the computational point, become about a hundred times as many at e_Υ = 1/10000,
where 𝔡₁ ≈ 3.33·10⁻⁹, so the bookkeeping gives no bound uniform over the admissible parameters. The integer was
obtained by exact rational arithmetic over the 1.065 × 10⁸ levels and the 8.0 × 10⁷ steps of the base level; it is
not proved in this paper, and no proof uses it.

### The first constants of the linear theory {#sec:ec-linear}

For the scalar wave operator on five-dimensional Tangherlini of mass 1, [[ch:resolvent-bounds]] gives explicit
constants: the resolvent cut off to I = {6/5 ≤ r ≤ 4} is bounded for every harmonic and every real 0 < |σ| ≤ 3
([[prop:morawetz-resolvent-l-ge-1]], [[prop:morawetz-l-zero]]) and by 11.477 on 3 ≤ |σ| ≤ 384 ([[thm:band]]), with
the values of [[prop:band-points]] at sampled frequencies; there the constant bounding the radial derivative is at
most 283.06 for every l ≥ 1 and 305.31 at l = 0, and 308.46 bounds the radial and angular derivatives summed over the
harmonics ([[cor:band-one-derivative]]). The same chapter makes explicit the factor of the interpolation step of the
high-energy inverses ([[lem:rb-interpolation]]: at most 1.002659), replaces one of the inverse bounds by a parametrix
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
(minimal expansion rate ν_min = 4·2^(−1/2), q^Γ = 4, β_0^Γ = 2), where, for the graded fibre inner products h_Γ(η)
of the trapping estimate of 2L_(b_0), the largest eigenvalue of the relevant symbol is η²(γ_C − 80·2^(1/2))²/(192γ_C)
to leading order in η, matched by enclosures at twelve points (γ_C = 10⁶, 10⁷, 10⁸; η = 10⁻¹, …, 10⁻⁴), so that the
estimate's condition needs η below about 16.48γ_C^(−1/2) and the condition number of h_Γ(η) is η^(−16). No proof uses
them.

**Remark {#rem:ec-not-evaluated}** (Where explicit evaluation stops.) The values of λ1 and δ are not determined in this
paper; [[prop:ec-delta-cap]] bounds them from above, and they are positive by the proof of [[thm:settling]]. Explicit
values stop first upstream of every constant: the proof fixes the gauge and damping parameters only below thresholds
whose existence it proves ([[thm:vi-c-2-1]]), and the cut-offs and orders of its function spaces only up to
admissibility, so explicit constants need those choices made with numbers, which [[def:ec-point]] does only at a point
outside the proved set. Among the inputs that depend on those choices are the gauge reconstruction, the inverse of the
absorbed problem in the norms of [[ch:s01]] (invertible by a Fredholm argument, [[lem:rb-absorbed]], which gives no
bound), and a lower bound, uniform in the harmonic, for the least singular value of the scalar-type blocks at zero
energy ([[lem:rb-quasimode]] bounds it from above). Four kinds of argument give a constant without a value: a compact
error removed by injectivity, by contradiction (the low-energy and Fredholm estimates of [[ch:s01]]–[[ch:s03]] and
their analogues later); uniformity in the spectral parameter and in the black hole parameters near the final one, by
sequences and compactness; the trapping estimate, by a defect-measure argument by contradiction ([[ch:s02]]), with the
a priori constants built on it; and finite covers of compact parameter sets. Bounds obtained from the closed graph,
open mapping and uniform boundedness theorems, among them the tame constants C_k of the membership statements
([[lem:iii-j2-1-2]] (f)), also give no value until each is read off from the explicit estimates behind the statement.
The parametrix norms at ι⁺ are not given by the construction of the parametrix, and the tame constants to the order
N_NM, the Nash–Moser thresholds of the exterior and slab problems and the constants of the gluing are not evaluated.
This is a limit of the explicit evaluation, not of [[thm:settling]].
