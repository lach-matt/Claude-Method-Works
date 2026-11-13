## The loss of the tame estimates and the constants of the settling theorem {#ch:explicit-constants}

The proof of [[thm:settling]] applies the Nash–Moser theorem [[thm:ii-g-2-1]] to the gauge-fixed Einstein equation
with the tame estimates of [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]]. Those estimates hold with a loss d of
b-regularity that does not depend on the order, and [[thm:ii-g-2-1]] then asks smallness in the regularity
N_NM = 21d + 6. The threshold λ1 on the wavelength and the threshold δ on the data in [[thm:settling]] are produced by
the proof, and are positive. This chapter states what the proof makes explicit about d, N_NM, δ and λ1.

The loss d is a number assigned by the rules of [[lem:iii-j2-1-2]] to the composition of model inverses, transforms
and differential operators that the proofs of [[ch:s19]]–[[ch:s23]] perform ([[def:ec-accounted-loss]]). Its
elementary losses have closed forms in the weights, the threshold quantities of the operators and the index sets
([[lem:ec-closed-forms]]); three nested iterations contribute their numbers of steps; and at one parameter point of
the gauge and damping parameters two of these iterations alone make d larger than 7.959 × 10¹⁵ and N_NM larger than
1.671 × 10¹⁷ ([[thm:loss-d]]). That parameter point lies outside the set on which [[thm:settling]] is proved
([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not the optimal loss. The same
formulas bound δ and λ1 from above ([[prop:ec-delta-cap]]). The chapter ends with the parts of the first constants of
the linear theory that are in hand, and with the places where explicit evaluation stops ([[rem:ec-not-evaluated]]).
No result of this chapter is used in the proof of any theorem of this paper.

### The computational point {#sec:ec-point}

**Definition {#def:ec-point}** (The computational point.) The *computational point* is the choice of the gauge and
constraint damping parameters of [[ch:s14]]

    γ_C = 10⁶  (h = 1/γ_C = 10⁻⁶),     γ_Υ = e_Υ = 1/100,     (v, e) = (1/2, 1/102400),

the last pair as in [[sec:s14-model]]. At it

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

The gap condition (G) of [[def:iii-i10-1-3]] excludes exponents in two windows just above 2 and 3. This section shows
that at the gauge parameters of the computational point the exponents built from the class roots stay out of those
windows by a margin larger than δ_50, so that (G) imposes nothing beyond ε_K < ε_ind. The elementary bounds, for a > 0
and 0 ≤ y ≤ 8a²,

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
w₂ := (4 + A)^(1/2) − 2 = A/(2 + (4 + A)^(1/2)), A := z + z²/4 = 4.000004·10⁻⁶. By [[eq:ec-sqrt]],
4 + A/4 − A²/64 ≤ 2 + (4 + A)^(1/2) ≤ 4 + A/4, with A/4 = 1.000001·10⁻⁶ and A²/64 < 2.6·10⁻¹³; so

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
[[thm:settling]], has three windows: no λ in the exponent set Λ of [[def:iii-i10-1-1]] has real part in
(2, 2 + ε_K] or in (3, 3 + ε_K], and no λ + d_c0 or λ + d_c1, λ ∈ Λ, has real part in (2, 2 + ε_K]; here
d_c0 = 𝔡₀ and d_c1 = 𝔡₁. The set Λ contains 2, 3 and λ_♯ and is closed under the increments
π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1}. If these increments include 𝔡₁, 1 + 𝔡₀, 1 + δ₂ and 1 + δ′₁, then 𝒮 ⊂ Λ: 𝒮 is the set of
sums of one of the generators 2, 3, λ_♯, any number of increments 𝔡₁ and at most one increment of integer part 1,
and a sum with two increments of integer part 1 is at least λ_♯ + 2 > 3 + ε_K, so it misses all three windows. By
[[prop:gap-sums]] no element of 𝒮 lies in the first two windows when ε_K < 5.019·10⁻⁸. The third window adds
nothing: for λ = g + n𝔡₁ ∈ 𝒮 (t = 0), λ + 𝔡₁ − 2 = s − 2 and λ + 𝔡₀ − 2 = s′ − 3 with s = g + (n + 1)𝔡₁ and
s′ = g + (1 + 𝔡₀) + n𝔡₁ in 𝒮, so by [[prop:gap-sums]] again neither λ + 𝔡₁ nor λ + 𝔡₀ lies in (2, 2 + ε_K] when
ε_K < 5.019·10⁻⁸; every other λ ∈ 𝒮 is at least λ_♯ + 1 > 5/2, so that λ + d_c0 and λ + d_c1 exceed 2 + ε_K.
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

By [[lem:iii-j2-1-2]], [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d := d_acc, and then [[thm:ii-g-2-1]], as
applied in the proof of [[thm:iii-k-4-3]], asks smallness in H^(N_NM) with N_NM = 21d_acc + 6. Every rule of
[[lem:iii-j2-1-2]] gives an upper bound, so d_acc bounds the least loss with which the estimates hold from above, and
may exceed it. Each elementary loss is a non-negative integer, so d_acc is at least the sum of the losses of any
family of steps that are composed one after another in the construction.

The losses of the following model inverses and transforms are given by their proofs in closed form. For a weight β
and an index set E, n(E, β) denotes the number of pairs (z, m′) ∈ E with Re z ≤ β. ϑ_in and ϑ_ℋ are the thresholds of
[[eq:i-a-1-5]] of the operator concerned, and s_c > ½ + ϑ_ℋ is the constant regularity order its proof fixes.

**Lemma {#lem:ec-closed-forms}** (Closed forms of the elementary losses.) The proofs of the cited results give them
with the following losses.

(a) [[lem:ii-g1-4-1]]: ℓ = max(⌈sup 𝗋 − 𝗋_out⌉, ⌈(s − 1)_+⌉) and ℓ̃ = max(⌈𝗋_out − inf 𝗋⌉, ⌈(−s)_+⌉).

(b) [[cor:ii-g1-4-2]]: if s_c ≥ 0, ℓ = max(⌈(ϑ_in/2 + 3 − β_scf)_+⌉, ⌈(s_c − 1)_+⌉); statement (1) then loses j + ℓ
for ∂^j_σ.

(c) [[prop:ii-g1-4-7]], and so [[lem:iii-i2-4-2]] for L̃_b: if s_c ≥ 0,

    ℓ = max(⌈(ϑ_in/2 + 5/2 + ε/2 − β_scf)_+⌉, ⌈(s_c − 1)_+⌉).                                           {#eq:ec-low-loss}

(d) [[cor:iii-f1-3-4]]: ℓ_tf := max(⌈sup 𝗋 − 𝗋_out⌉, ⌈(s − 1)_+⌉) + max(⌈𝗋_out − inf 𝗋⌉, ⌈(−s)_+⌉), for the orders
(s, 𝗋) of its proof, with 𝗋_out = β_sctf − 2 − ϵ/2. If the incoming threshold ϑ_in of N_tf(L_b, ±1) is non-negative,
then ℓ_tf ≥ 1.

(e) [[thm:iii-g1-3-1]] (2), at a spectral parameter ϰ with Re ϰ < ℓ_I: with δ > 0 the small number of Step 5 of its
proof,

    d_ι(ϰ) = 6 + ⌈max(0, Re ϰ − 2 + δ)⌉ + ⌈max(0, Re ϰ − 3/2) + δ⌉ + 2⌈ℓ_I − Re ϰ⌉.                    {#eq:ec-iota-loss}

That is 7 + 2⌈ℓ_I − Re ϰ⌉ for Re ϰ < 2 − δ, and, when 3 < ℓ_I < 3.5 and δ < 3.5 − ℓ_I, at most 12 for
2 ≤ Re ϰ < ℓ_I. Over a strip λ₋ ≤ Re ϰ ≤ ℓ_I − ε with λ₋ < 3/2, sup d_ι ≤ max(7 + 2⌈ℓ_I − λ₋⌉, 12); if moreover
λ₋ > ℓ_I − 2, sup d_ι = 12.

(f) [[prop:iii-g3-2-4]] at finite regularity, and so [[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1): l′ = 2⌈ℓ_I⌉ + 10
+ sup d_ι over the strip; l′ = 30 when 3 < ℓ_I < 3.5, λ₋ ∈ (ℓ_I − 2, 3/2) and δ < 3.5 − ℓ_I.

(g) [[prop:iii-a-4-2]]: with n_ι := n(E_ι, β_ι), n_K := n(E_K, β_K), n_I := n(E_I, β_I),
B := max(β_K, β_ι + max(0, −min Re π_1E_I)) and ℓ_F := ⌈(max(β_ι − β_scf, β_K) + ε − ½)_+⌉,

    (1):  l = 1 + n_ι + 2 max(n_K + ⌊β_K⌋, n_I + ⌊B⌋),        (2):  l = n_ι + n_K + ℓ_F.                {#eq:ec-fourier-loss}

*Proof.* (a) is the statement of [[lem:ii-g1-4-1]].

(b) The proof of [[cor:ii-g1-4-2]] takes ℓ := ℓ_a + ℓ̃ with ℓ_a := max(⌈(½(−1 + ϑ_in) + 7/2 − β_scf)_+⌉,
⌈(s_c − 1)_+⌉) and ℓ̃ := ⌈(−s_c)_+⌉. The proof needs only s_c > ½ + ϑ_ℋ, so s_c ≥ 0 may be imposed as a further
choice; then ℓ̃ = 0 and ½(−1 + ϑ_in) + 7/2 = ϑ_in/2 + 3. The loss j + ℓ for ∂^j_σ is statement (1).

(c) The proof of [[prop:ii-g1-4-7]] takes 𝗋_out := β_scf − 2 − ε/2, 𝗋_in := max(𝗋_out, ½(−1 + ϑ_in) + 1) and s = s_c
as in [[cor:ii-g1-4-2]], decay orders with values in [𝗋_out, 𝗋_in], and ℓ := ℓ_a + ℓ̃ from [[lem:ii-g1-4-1]]. So
ℓ_a = max(⌈𝗋_in − 𝗋_out⌉, ⌈(s_c − 1)_+⌉) with 𝗋_in − 𝗋_out = (ϑ_in/2 + 5/2 + ε/2 − β_scf)_+, and ℓ̃ = 0 for s_c ≥ 0.
[[lem:iii-i2-4-2]] is the proof of [[prop:ii-g1-4-7]] for L̃_b.

(d) The proof of [[cor:iii-f1-3-4]] obtains the bound near sctf from [[eq:ii-g1-4-1a]] and [[eq:ii-g1-4-1b]] with the
losses ℓ, ℓ̃ of (a), replaces k by k + ℓ̃ and enlarges ℓ; so its loss is at least ℓ + ℓ̃ as displayed. Its orders are
those of [[lem:i-a-7-1]] at σ_* = ±1, with 𝗋 = 𝗋_in at the incoming radial sets, where 𝗋_in > (−1 + ϑ_in)/2 (the
weight α₊ being 0); and 𝗋_out = β_sctf − 2 − ϵ/2 < −½ − δ with δ = ¼(3/2 − β_sctf) > 0, as β_sctf < 3/2. If ϑ_in ≥ 0,
then sup 𝗋 ≥ 𝗋_in > −½ > 𝗋_out, so ⌈sup 𝗋 − 𝗋_out⌉ ≥ 1 and ℓ_tf ≥ 1.

(e) Step 5 of the proof of [[thm:iii-g1-3-1]] extends v^(−2−ϰ)f by 0 to F, which lies in Ḣ^((s−1;k+d),μ)_(b;b) at the
same order k + d, with s := min(½, 2 − Re ϰ) − δ, s − ½ ∉ ℤ, and inverts N_sf(ϰ) at that order. It then applies
[[lem:iii-g1-2-1]], which loses m(s) = 2 + ⌈max(0, −s)⌉ + j, with j the least integer with s + j > ½, that is
j = ⌈½ − s⌉; and then at most ⌈ℓ_I − Re ϰ⌉ + 2 steps, each losing two b-derivatives. So

    d_ι = m(s) + 2(⌈ℓ_I − Re ϰ⌉ + 2) = 6 + ⌈max(0, −s)⌉ + ⌈½ − s⌉ + 2⌈ℓ_I − Re ϰ⌉

suffices. Here −s = max(−½, Re ϰ − 2) + δ, so max(0, −s) = max(0, Re ϰ − 2 + δ) for δ < ½, and
½ − s = max(0, Re ϰ − 3/2) + δ. This is [[eq:ec-iota-loss]]. For Re ϰ < 2 − δ the first ceiling vanishes and the second
is 1 (its argument lies in (0, 1)), which gives 7 + 2⌈ℓ_I − Re ϰ⌉. Let 3 < ℓ_I < 3.5, δ < 3.5 − ℓ_I and
2 ≤ Re ϰ < ℓ_I. If Re ϰ < ℓ_I − 1, then ⌈ℓ_I − Re ϰ⌉ = 2, Re ϰ − 2 + δ < ℓ_I − 3 + δ < 1 and
Re ϰ − 3/2 + δ < ℓ_I − 5/2 + δ < 1, so d_ι = 6 + 1 + 1 + 4 = 12. If ℓ_I − 1 ≤ Re ϰ < ℓ_I, then
⌈ℓ_I − Re ϰ⌉ = 1, Re ϰ − 2 + δ < 3/2 + δ < 2 and Re ϰ − 3/2 + δ < 2, so d_ι ≤ 6 + 2 + 2 + 2 = 12. On the strip,
d_ι is at most 7 + 2⌈ℓ_I − λ₋⌉ where Re ϰ < 2 − δ, as ⌈ℓ_I − Re ϰ⌉ ≤ ⌈ℓ_I − λ₋⌉, and at most 12 where Re ϰ ≥ 2 − δ
(between 2 − δ and 2 the value is 6 + 1 + 1 + 2⌈ℓ_I − Re ϰ⌉ ≤ 12); and the value 12 is attained at Re ϰ = 2, as
ℓ_I − 1 > 2. If λ₋ > ℓ_I − 2, then 7 + 2⌈ℓ_I − λ₋⌉ ≤ 7 + 4 = 11, so sup d_ι = 12.

(f) The proof of [[prop:iii-g3-2-4]] at finite regularity applies [[lem:iii-g3-2-2]], with the loss
l = 2⌈ℓ_I⌉ + 10 of its statement, and then [[thm:iii-g1-3-1]] (2) on the strip, and takes l′ := l + sup d_ι.
[[prop:iii-g3-3-7]] and [[cor:iii-g3-3-1]] (1) use [[prop:iii-g3-2-4]] on a strip containing their exponent, and the
rest of their constructions is a finite-rank assembly with continuous functionals, which adds nothing by
[[lem:iii-j2-1-2]] (c) (the functionals are counted where their values are used). For 3 < ℓ_I < 3.5, ⌈ℓ_I⌉ = 4 and
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
costs nothing more; for general E_K, R_zf costs n_K and [[lem:iii-a-1-3]] at K nothing more. This gives
[[eq:ec-fourier-loss]] (2). ∎

**Remark {#rem:ec-other-losses}** (The other elementary losses.) The remaining elementary losses of
[[lem:iii-j2-2-1]] are fixed in its statement: 0 for finite-dimensional maps and for the integrations (d) there, 1 for
[[prop:ii-g1-3-3]] (1) and [[prop:iii-h-3-2]], 2 for second-order operators (L_b, L̃_b, and the background terms
applied to a solution), ℓ + 1 for [[cor:ii-g1-4-5]] at every order, where ℓ = 2ℓ_3 + ℓ_4 + ℓ_5 is assembled from the
losses of [[prop:ii-g1-3-5]] (2), [[prop:ii-g1-4-4]] and [[prop:ii-g1-3-3]] (2), each a closed form in the weights, and
d_ι + 2 for [[cor:iii-g2-4-3]]. The order of choices behind ℓ + 1 is: d_acc first, then N_NM, then the trapping data
at the orders k ≤ N_NM ([[cor:iii-h2-1-2]]); the constants of the smallness conditions are used at those orders only,
the tame estimates themselves at every order. The statement "d_acc is an explicit number" needs, besides these closed
forms, numbers for the weights at the parameters in question, the index sets n(E, β) and the numbers of steps of the
iterations; the next section bounds two of these iterations from below.

### Two long iterations, and a lower bound for d {#sec:ec-floor}

Three constructions of [[ch:s21]]–[[ch:s23]] repeat one step many times.

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

(a) a transition face round below 3, or a level-3 round above 3, is charged at least 2 + ℓ_tf, with ℓ_tf the loss of
[[cor:iii-f1-3-4]] in [[lem:ec-closed-forms]] (d);

(b) a round of the iteration at ι⁺ of [[prop:iii-i5-2-1]], which applies [[cor:iii-g2-4-3]] to the terms of the
forcing at one exponent ϰ_0 and removes the error by [[prop:iii-i1-3-1]], is charged at least 4 + d_ι(ϰ_0). If
3 < ℓ_I < 3.5 and λ_♯ ≤ Re ϰ_0 < 2 − δ, this is at least 15.

*Proof.* (a) The round maps its forcing to v_i by a construction that composes N_tf(L_b, ±1)⁻¹ with maps of non-negative
loss, and v_i to the next forcing by L̂_b(σ), of loss 2 ([[lem:iii-j2-2-1]]); the next round takes that forcing as its
input. By the composition rule the round is charged at least 2 + ℓ_tf. (b) [[lem:iii-j2-2-1]] (g) charges
[[cor:iii-g2-4-3]] the loss d_ι + 2 of [[thm:iii-g1-3-1]] (2) composed with L_b, and [[prop:iii-i1-3-1]] a loss that
includes one application of L̃, of loss 2; the next forcing is formed from their outputs. So a round is charged at
least 4 + d_ι(ϰ_0). For 3 < ℓ_I < 3.5 and λ_♯ ≤ Re ϰ_0 < 2 − δ, 1 < ℓ_I − Re ϰ_0 < 2, so d_ι(ϰ_0) = 11 by
[[lem:ec-closed-forms]] (e). ∎

