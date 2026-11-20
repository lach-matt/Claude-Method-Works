### The lower bound for the loss on the proved set {#sec:ec-lb-proved}

The lower bound of [[thm:loss-d]] (ii) is stated at the computational point, and that point lies outside the set on
which [[thm:settling]] is proved ([[rem:ec-point-outside]]). This section proves a lower bound for d_acc, and so for
d_NM, N_NM and δ, at every point of that set, as an explicit function of the gauge parameter z = 4e_Υγ_Υ² and of the
damping parameter h = γ_C⁻¹. The proof of [[prop:ec-rounds]] uses the point only through upper bounds for ε_g, ε_K and
η_2. Here ε_Υ is bounded at every z ∈ (0, ½] ([[lem:ec-lb-gauge]]) and ε_ind at every h ∈ (0, 10⁻⁶]
([[lem:ec-lb-ind]]), and the count of [[prop:ec-rounds]] is run with general bounds ([[lem:ec-lb-rounds]]);
[[thm:ec-lb-proved]] assembles them, and [[rem:ec-lb-conditions]] lists the conditions of [[thm:settling]] that the
proof uses. Throughout, (v_C, e_C) = (1/2, 1/102400) as in [[eq:iv4-0-1]], and e := e_C.

**Lemma {#lem:ec-lb-gauge}** (The least distance of ℳ at every gauge point.) Let 0 < z ≤ ½. For l ≥ 1 put u := l + 1
and let

    w := (u² + z + z²/4)^(1/2) − u,
    d₁(l) := ½((2u + 1)² + 2z + 4w)^(1/2) − ½(2u + 1),     d₂(l) := ½((2u − 1)² + 2z − 4w)^(1/2) − ½(2u − 1),

the numbers of [[prop:np-10-52]] (i) at this z. Then:

(a) ι^Υ_(sl,l+1) = l + 1 + d₂(l) and ι^Υ_(sl,l+2) = l + 2 + d₁(l), in the notation of [[lem:iii-d-4-1]];

(b) 7z/240 − z²/960 − 49z²/864000 ≤ d₂(7) ≤ 7z/240 and 5z/171 − z²/21600 < d₁(8) ≤ 5z/171 + z²/1368;

(c) z/13680 − z²/21600 < d₁(8) − d₂(7) ≤ z/13680 + z²/544; in particular d₁(8) > d₂(7);

(d) the least distance 𝔡_ℳ between distinct points of the set ℳ of [[sec:iii-d2-1]] at this z satisfies
𝔡_ℳ ≤ d₁(8) − d₂(7), so that every ε_Υ that [[sec:iii-d2-1]] admits at this z satisfies

    ε_Υ < ½𝔡_ℳ ≤ g(z) := z/27360 + z²/1088 = (z/27360)(1 + 27360z/1088).                                {#eq:ec-lb-g}

*Proof.* (a) The polynomial Q_l(s) = s² − (2 + 2κ + z)s + κ(κ + 1) + zκ of [[lem:iii-d-4-1]], κ = l(l + 2) = u² − 1, has
discriminant (2 + 2κ + z)² − 4κ(κ + 1) − 4zκ = (z + 2)² + 4κ = 4(u² + z + z²/4) = 4(u + w)², and 1 + κ + z/2 = u² +
z/2; so its roots are s_± = u² + z/2 ± (u + w), and 1 + 4s_± = (2u ± 1)² + 2z ± 4w. By [[eq:s13-dets]] the roots of
type sl other than l + 3 and 1 − l are the numbers ι with ι² − ι = s_±, and those above ½ are ½ + ½(1 + 4s_±)^(1/2),
that is u + 1 + d₁(l) = l + 2 + d₁(l) and u + d₂(l) = l + 1 + d₂(l). The first is the larger, as s_+ > s_−; and by
[[eq:iii-d-4-2]], ι^Υ_(sl,l+2) > l + 2 > l + 5/4 > ι^Υ_(sl,l+1). So the first is ι^Υ_(sl,l+2) and the second
ι^Υ_(sl,l+1). This is the argument of the proof of [[prop:np-10-52]] (i), which uses only z > 0.

(b) As w = (z + z²/4)/((u² + z + z²/4)^(1/2) + u), and 2u ≤ (u² + z + z²/4)^(1/2) + u ≤ 2u + (z + z²/4)/(2u) by
[[eq:ec-sqrt]],

    z/(2u) ≤ w ≤ z(1 + z/4)/(2u);

the lower bound holds because (z + z²/4)·2u − z(2u + (z + z²/4)/(2u)) = (z²/(2u))(u² − 1 − z/4) ≥ 0 for u ≥ 2 and
z ≤ ½. For A > 0 and 0 ≤ y ≤ 8A², [[eq:ec-sqrt]] gives y/(2A) − y²/(8A³) ≤ (A² + y)^(1/2) − A ≤ y/(2A); so
½((A² + y)^(1/2) − A) lies between y/(4A) − y²/(16A³) and y/(4A).

For d₂ take A = 2u − 1 and y = 2z − 4w, which by the bounds on w lies in [(2z/u)(u − 1 − z/4), (2z/u)(u − 1)], a
subinterval of [0, 8A²]. So d₂ ≤ z(u − 1)/(2uA) and d₂ ≥ z(u − 1 − z/4)/(2uA) − z²(u − 1)²/(4u²A³). At l = 7, u = 8,
A = 15, 2uA = 240 and 4u²A³ = 864000; this gives the bounds for d₂(7).

For d₁ take A = 2u + 1 and y = 2z + 4w, which lies in [(2z/u)(u + 1), (2z/u)(u + 1 + z/4)] ⊂ [0, 8A²]. So
d₁ ≤ z(u + 1 + z/4)/(2uA) and d₁ ≥ z(u + 1)/(2uA) − z²(u + 1 + z/4)²/(4u²A³). At l = 8, u = 9, A = 19, 2uA = 342 and
4u²A³ = 2222316; so d₁(8) ≤ z(10 + z/4)/342 = 5z/171 + z²/1368, and, as (10 + z/4)² ≤ (81/8)² = 6561/64 for z ≤ ½
and 6561 · 21600 = 141717600 < 142228224 = 64 · 2222316, d₁(8) ≥ 5z/171 − 6561z²/142228224 > 5z/171 − z²/21600.

(c) 5/171 − 7/240 = 3/41040 = 1/13680. By (b), d₁(8) − d₂(7) > z/13680 − z²/21600, which is positive for
0 < z < 21600/13680, so for z ≤ ½; and d₁(8) − d₂(7) ≤ z/13680 + cz² with c = 1/1368 + 1/960 + 49/864000 =
30031/16416000, and c < 1/544, as 30031 · 544 = 16336864 < 16416000.

(d) By (a) and [[lem:iii-d-4-1]], −7 − d₂(7) = 1 − ι^Υ_(s7,8) and −9 − d₁(8) = 1 − ι^Υ_(s8,10) are indicial roots of
(□^Υ_b)^(0). Their real parts lie in [−10, 10], as 0 < d₂(7), d₁(8) < 1 by (b). So −d₂(7) and −d₁(8), their shifts by
7 and by 9, lie in ℳ, and they are distinct by (c). Hence 𝔡_ℳ ≤ d₁(8) − d₂(7) ≤ z/13680 + z²/544. [[sec:iii-d2-1]]
fixes ε_Υ below ½𝔡_ℳ. ∎

At z = 4·10⁻⁶, (c) gives 2.92396·10⁻¹⁰ < d₁(8) − d₂(7) < 2.92428·10⁻¹⁰, in agreement with [[eq:ec-gauge-gap]], where
[[lem:ec-gauge-gap]] shows 𝔡_ℳ = d₁(8) − d₂(7); and g(4·10⁻⁶) < 1.46214·10⁻¹⁰, the number δ̂ of [[prop:ec-rounds]]. The
leading coefficient 1/13680 = 5/171 − 7/240 does not depend on z.

**Lemma {#lem:ec-lb-ind}** (The index distance at every damping point.) Let 0 < h ≤ 10⁻⁶. The polynomial P_2 of
[[prop:np-10-12]] (iii), at (v, e) = (1/2, 1/102400), has a real root ι₂(h) with

    (40/13)h(1 − 5·10⁴h) < ι₂(h) − 2 < (40/13)h.                                                            {#eq:ec-lb-root}

Hence the number ε_ind(h) of [[prop:np-10-52]] (iii) satisfies ε_ind(h) < (40/13)h. If moreover z ∈ (0, ½] and (C1)
holds, every constant ε_ind with [[eq:iii-f1-2-2]] satisfies ε_ind < (40/13)h.

*Proof.* At κ = 8, that is l = 2, put ι = 2 + hξ in [[eq:s14-f-two]], so that w = hξ there, and collect the powers of
h. Each f_j is a polynomial in h of degree at most 3, and

    P_2(2 + hξ) = Σ_(j=1)^9 p_j(ξ)h^j                                                                        {#eq:ec-lb-p}

with

    p₁ = −3e(13ξ − 40),     p₂ = (2 + 10e)ξ² − (11 + 159e)ξ − 40(1 − e),
    p₃ = (5e − 2)ξ³ + (47 − 36e)ξ² − (251 + 2e)ξ + 360,     p₄ = ξ((29e − 7)ξ² + (135 − 47e)ξ − 378),
    p₅ = ξ²((6e − 5)ξ² + (e + 55)ξ − 85),     p₆ = ξ³((7e − 15)ξ + 96),     p₇ = ξ⁴((e − 4)ξ + 14),
    p₈ = −6ξ⁵,     p₉ = −ξ⁶.

For instance, at κ = 8, f₀ = 40h(3e − (1 − e)h + 9h²) and f₁ = −39e − (11 + 159e)h − (251 + 2e)h² − 378h³; so the terms
of order h are 120e and −39eξ, which give p₁, and those of order h² are −40(1 − e), −(11 + 159e)ξ and (2 + 10e)ξ², the
last from f₂ = 2 + 10e + O(h). For 0 ≤ ξ ≤ 40/13 and 0 < e < 10⁻⁵, each p_j is bounded by the sum of the moduli of its
terms, taken at ξ = 40/13 and e = 10⁻⁵:

    |p₃| < 1636,   |p₄| < 2646,   |p₅| < 2856,   |p₆| < 4142,   |p₇| < 2359,   |p₈| < 1655,   |p₉| < 849.

So, for 0 < h ≤ 10⁻⁶ and 0 ≤ ξ ≤ 40/13,

    P_2(2 + hξ) = hp₁(ξ) + h²(p₂(ξ) + ϱ),     |ϱ| ≤ Σ_(j=3)^9 |p_j(ξ)|h^(j−2) < 0.0017.                        {#eq:ec-lb-rho}

*The upper end.* At ξ = 40/13, p₁ = 0 and p₂ = (2 + 10e)·1600/169 − (11 + 159e)·40/13 − 40(1 − e) =
−(9280 + 59920e)/169 < −54.9. So P_2(2 + (40/13)h) < h²(−54.9 + 0.0017) < 0.

*The lower end.* Let ξ₋ := (40/13)(1 − 5·10⁴h). Then 38/13 ≤ ξ₋ < 40/13 and 13ξ₋ − 40 = −2·10⁶h, so
hp₁(ξ₋) = 6·10⁶eh² = (1875/32)h², as e = 1/102400. On [38/13, 40/13], p₂′(ξ) = (4 + 20e)ξ − 11 − 159e ≥ 152/13 − 11 −
159e > 0.69; so p₂(ξ₋) ≥ p₂(38/13) = −(9306 + 57346e)/169 > −55.07. So P_2(2 + hξ₋) > h²(1875/32 − 55.07 − 0.0017) >
3.5h² > 0.

P_2 has real coefficients, so it has a real root ι₂(h) in (2 + hξ₋, 2 + (40/13)h), which is [[eq:ec-lb-root]].

*The consequences.* ι₂(h) − 1 lies in (1, 1 + (40/13)h) ⊂ (1, 3/2): it is not an integer, its modulus is below 50, and
its distance from ℤ is ι₂(h) − 2. It is an entry of the list ℛ^sc_2 of [[sec:s14-simple]], which contains ι − 1 for
the six roots ι of P_2; so ε_ind(h) ≤ ι₂(h) − 2 < (40/13)h. The indicial roots of □^C_b of scalar type 2 are the roots
of P_2 ([[lem:iv4-1-3]] and its proof), and ι₂(h) has real part greater than 2, so under (C1) it is one of the roots
ι^C_(s2,+,j). By [[prop:iii-f1-2-3]], which assumes z ∈ (0, ½] and (C1), ι₂(h) − 1 is then a non-integer indicial
root of L_b^(0) with |ι₂(h) − 1| ≤ 50, and [[eq:iii-f1-2-2]] gives ε_ind ≤ ι₂(h) − 2. ∎

**Remark {#rem:ec-lb-ind}** (The root ι₂(h).) At h = 10⁻⁶ the interval of [[eq:ec-lb-root]] is
(2 + (38/13)h, 2 + (40/13)h), which contains the interval (2 + 2.93h, 2 + 2.94h) of [[lem:s14-sextic-small]] (b), as
38/13 < 2.93 and 2.94 < 40/13; by that lemma, ι₂(10⁻⁶) is the root of P_2 that it locates there. As h → 0,
(ι₂(h) − 2)/h → 40/13 by [[eq:ec-lb-root]], so the bound ι₂(h) − 2 < (40/13)h is sharp for small h. For
h ≤ 6.309·10⁻⁹, (40/13)h < δ_50 ([[lem:s14-delta50]]), and the bound improves on ε_ind(h) ≤ δ_50 of
[[prop:np-10-52]] (iii).

**Lemma {#lem:ec-lb-rounds}** (The number of rounds, from bounds for the gaps.) Let δ̂ > 0 and δ̄ > 0 with
5δ̂ + δ̄ < 1. Let ε_K, ε_+, η_2, α, the levels and the losses ε, ε′ be admissible for [[thm:iii-i14-3-1]],
[[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]], and suppose that

    ε_g ≤ δ̂,     ε_K < δ̂,     ε_K < δ̄,     η_2 < δ̄.

Then the transition face rounds at the levels below 3 and the level-3 rounds at the levels in (3, 4) of
[[sec:ec-floor]] number together

    R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂) > (1 − 5δ̂ − δ̄)/δ̂².                                                    {#eq:ec-lb-rounds}

*Proof.* At every parameter point the admissible choices give: α ∈ (4, 4 + ε_K]; levels α_1 = β_0 < β_1 < ⋯ < β_K = α
with spacings below α − 4 ≤ ε_K, α_1 ∈ (2, α − 2) and no level equal to 3 ([[sec:ec-floor]]); the loss ε of
[[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] with 0 < ε < ½ε_g ([[lem:iii-i8-3-2]]); and the loss ε′ ≤ ε of
[[lem:iii-i8-3-2]] (the proof of [[prop:ec-rounds]]). So ε′ ≤ ε < ½ε_g < δ̂, and each round raises the tf-weight by
ε_g − ε < δ̂. As in the proof of [[prop:ec-rounds]], the count uses the increments only through this upper bound, so it
holds as well if a round raises the weight by less, a forcing of tf-weight κ having every smaller tf-weight.

*Below 3.* At a level β ∈ (2, 3) the rounds start from τ_0 = 2 + ε_g − 2ε < 2 + δ̂, so τ_i < 2 + (i + 1)δ̂, and they run
for every i ≥ 0 with τ_i ≤ β − ε′, the τ_i being increasing. As ε′ < δ̂, their number is at least the number of i ≥ 0
with 2 + (i + 1)δ̂ ≤ β − δ̂, which is at least g_1(β)/δ̂ with g_1(x) := (x − 2 − 2δ̂)_+. The levels in (2, 3) form a
sequence b_1 < ⋯ < b_m with b_1 = α_1 < α − 2 ≤ 2 + ε_K < 2 + 2δ̂, and b_m > 3 − ε_K, because the next level exceeds 3
and lies within ε_K of b_m. The function g_1 is non-decreasing, vanishes below 2 + 2δ̂ and satisfies
g_1(y) − g_1(x) ≤ y − x for x ≤ y; so by [[lem:ec-level-sum]] with c = ε_K, as b_m − b_1 < 1,

    Σ_j g_1(b_j)/δ̂ ≥ (1/(ε_Kδ̂))(∫_(2+2δ̂)^(3−ε_K) (x − 2 − 2δ̂) dx − ε_K/2) = (1/(ε_Kδ̂))((1 − ε_K − 2δ̂)²/2 − ε_K/2).

*Between 3 and 4.* At a level β ∈ (3, 4) the rounds start from κ_3 = 1 + η_2 − 2ε < 1 + δ̄, so κ_i < 1 + δ̄ + iδ̂, and
they run for every i ≥ 0 with κ_i ≤ β − 2; their number is at least the number of i ≥ 0 with 1 + δ̄ + iδ̂ ≤ β − 2,
which is at least g_2(β)/δ̂ with g_2(x) := (x − 3 − δ̄)_+. The levels in (3, 4) form a sequence c_1 < ⋯ < c_p with
c_1 < 3 + ε_K < 3 + δ̄, the previous level lying below 3 within ε_K, and c_p > 4 − ε_K, the next level being at least 4
(as β_(K−1) > α − (α − 4) = 4) and lying within ε_K of c_p. By [[lem:ec-level-sum]] again,

    Σ_j g_2(c_j)/δ̂ ≥ (1/(ε_Kδ̂))((1 − ε_K − δ̄)²/2 − ε_K/2).

*The sum.* Adding, and using (1 − a)²/2 > ½ − a for a > 0, R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂). The right side decreases
in ε_K on (0, δ̂], its numerator being positive there, as 3ε_K + 2δ̂ + δ̄ ≤ 5δ̂ + δ̄ < 1; so it exceeds its value
(1 − 5δ̂ − δ̄)/δ̂² at ε_K = δ̂. ∎

**Theorem {#thm:ec-lb-proved}** (The loss at every point of the proved set.) Let h ∈ 𝖧, γ_C = h⁻¹, the gauge
parameters (γ_(Υ,H), e_Υ, γ_Υ), the constants ε_Υ and ε_ind, and the weights be chosen as in [[thm:settling]], that is,
so that the conditions of [[sec:vi-c-1]] hold ([[thm:vi-c-2-1]]). Put z := 4e_Υγ_Υ², let g be the function of
[[eq:ec-lb-g]], and put

    δ̂ := min(g(z), 40h/13).

Then, for every admissible choice of η_2, α, the levels and the losses ε, ε′ of [[thm:iii-i14-3-1]], [[lem:iii-i8-3-2]]
and [[prop:iii-i13-2-1]], the number R of [[lem:ec-lb-rounds]] satisfies R > (1 − 2·10⁻⁵)/δ̂², and

    d_NM ≥ d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²),
    N_NM = 21d_NM + 6 > 63(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²).                                          {#eq:ec-lb-bound}

In particular

    d_acc > 2.2456·10⁹ z⁻²(1 + 25.15z)⁻²,       d_acc > 0.3168 γ_C²,
    N_NM > 4.7158·10¹⁰ z⁻²(1 + 25.15z)⁻²,       N_NM > 6.654 γ_C²,                                          {#eq:ec-lb-numbers}

and, in the gauge parameters, d_acc > 1.4035·10⁸ e_Υ⁻²γ_Υ⁻⁴(1 + 100.6e_Υγ_Υ²)⁻².

*Proof.* *The gaps.* By rows c1–c2 of [[sec:vi-c-1]], (v_C, e_C) = (1/2, 1/102400) and h ∈ 𝖧 ⊂ (0, h_*) with
h_* ≤ 10⁻⁶; by row u5, z ∈ (0, ½]. [[sec:iii-d2-1]] fixes ε_Υ below half the least distance between distinct points of
ℳ, so ε_Υ < g(z) by [[lem:ec-lb-gauge]]. By row c3, (C1) holds (it holds at every h ∈ (0, 10⁻⁶], by [[lem:iv4-1-3]]
(a)), and ε_ind is a constant with [[eq:iii-f1-2-2]] ([[eq:iii-i9-1-1]]); so ε_ind < 40h/13 by [[lem:ec-lb-ind]].
Hence ε_g = min(ε_Υ, ε_ind) < δ̂ ([[def:s21-eps-g]]). Row w1 asks ε_K < ε_+ < ε_ind ([[eq:iii-i9-1-1]]) and
ε_K < ε_Υ ([[def:iii-i10-1-3]]), so ε_K < ε_g < δ̂; and [[sec:iii-i11-1]] takes η_2 ∈ (ε_K, ε_+), so η_2 < ε_ind. Put
δ̄ := 40h/13. Then ε_K < δ̄, η_2 < δ̄ and δ̂ ≤ δ̄, and 5δ̂ + δ̄ ≤ 6δ̄ ≤ (240/13)·10⁻⁶ < 1.85·10⁻⁵.

*The rounds.* [[lem:ec-lb-rounds]] applies with these δ̂ and δ̄, and gives R > (1 − 5δ̂ − δ̄)/δ̂² > (1 − 2·10⁻⁵)/δ̂².

*The loss.* Level k + 1 of [[thm:iii-i14-3-1]] takes the solution of level k as input through R_qu, and at each level
the rounds of [[sec:ec-floor]] are composed one after another, each round's output being the next round's forcing; so
all the rounds lie on one chain of compositions, and by [[def:ec-accounted-loss]] and [[lem:ec-round-loss]] (a),
d_acc ≥ Σ_rounds(2 + ℓ_tf). By [[lem:ec-closed-forms]] (d), ℓ_tf ≥ 1 at every round, so d_acc ≥ 3R. This is the
argument of the proof of [[thm:loss-d]] (ii), and it does not use the computational point: [[lem:ec-round-loss]] holds
in the accounting at every parameter point, and [[lem:ec-closed-forms]] (d) uses only β_sctf < 3/2 and the
non-negativity of ϑ_in, which [[lem:ec-theta-in]] (b) proves for L_b at every value of the parameters. Finally
d_NM ≥ d_acc and N_NM = 21d_NM + 6 by [[thm:loss-d]], and 1/δ̂² = max(g(z)⁻², (13γ_C/40)²), as 1/(40h/13) = 13γ_C/40.
This gives [[eq:ec-lb-bound]].

*The numbers.* g(z) = (z/27360)(1 + 27360z/1088) and 27360/1088 < 25.15, so g(z)⁻² > 27360²z⁻²(1 + 25.15z)⁻²; and
3 · 27360² = 2245708800, so 3(1 − 2·10⁻⁵) · 27360² > 2.24566·10⁹. Also 3(13/40)² = 0.316875, and
0.316875(1 − 2·10⁻⁵) > 0.31686. Multiplying by 21 gives more than 4.7158·10¹⁰ and more than 6.654. With z = 4e_Υγ_Υ²,
z² = 16e_Υ²γ_Υ⁴ and 25.15z = 100.6e_Υγ_Υ², and 2.24566·10⁹/16 > 1.4035·10⁸. ∎

**Corollary {#cor:ec-lb-delta}** (The threshold δ on the proved set.) In the setting of [[thm:ec-lb-proved]], the
threshold δ of [[thm:settling]], as its proof chooses it, satisfies

    log₁₀ δ < −(472/49) · 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²),

so that log₁₀ δ < −2.163·10¹⁰ z⁻²(1 + 25.15z)⁻² and log₁₀ δ < −3.052 γ_C².

*Proof.* [[prop:ec-delta-cap]] gives log₁₀ δ < −(59/196)(32d + 9) with d = d_NM, and its proof uses no property of the
parameter point. As (59/196) · 32 = 472/49 and d_NM > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²) by
[[thm:ec-lb-proved]], the first bound follows; and (472/49) · 2.24566·10⁹ > 2.1631·10¹⁰ and
(472/49) · 0.31686 > 3.0522. ∎

**Remark {#rem:ec-lb-conditions}** (What the bound uses.) The proof of [[thm:ec-lb-proved]] uses exactly the following
conditions of [[thm:settling]], each of which holds at every point of the proved set:

- (v_C, e_C) = (1/2, 1/102400) (row c1 of [[sec:vi-c-1]]), through e in P_2;
- h ≤ 10⁻⁶ (row c2: 𝖧 ⊂ (0, h_*) with h_* ≤ 10⁻⁶), for [[lem:ec-lb-ind]] and for 6δ̄ < 2·10⁻⁵;
- (C1) (row c3), which holds at every h ∈ (0, 10⁻⁶] ([[lem:iv4-1-3]] (a)), to read ι₂(h) − 1 as an indicial root of
  L_b^(0);
- z ∈ (0, ½] (row u5), for [[lem:ec-lb-gauge]];
- the definitions of ε_Υ ([[sec:iii-d2-1]]), of ε_ind ([[eq:iii-f1-2-2]]) and of ε_g ([[def:s21-eps-g]]);
- ε_K < ε_+ < ε_ind and ε_K < ε_Υ (row w1), and α ∈ (4, 4 + ε_K] (row w2);
- the choices that the proofs of [[thm:iii-i14-3-1]], [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] make at every
  point: the levels, η_2 ∈ (ε_K, ε_+) ([[sec:iii-i11-1]]), and the losses 0 < ε < ½ε_g and ε′ ≤ ε.

It uses none of the thresholds that define the proved set: not h < h_0, h < h_tf or h ∉ 𝖹; not γ_(Υ,H) ≤ ε_0, nor the
bounds ε_1, ε_L and γ_1 on e_Υ and γ_Υ; not z ∉ 𝖹_exc; not (C2)–(C5); not (G) beyond ε_K < ε_Υ, nor (G⁺), (Ex1)–(Ex4)
or (A_J); and not the data classes, the parameter set ℬ_* or the smallness of rows d1–d2, b1–b4 and n1. So the bound
holds on the proved set without any of those thresholds being evaluated. It holds as well at every
(h, z) ∈ (0, 10⁻⁶] × (0, ½] at which the constructions of [[sec:ec-floor]] are run with constants satisfying the
conditions listed. At the computational point it gives d_acc > 3(1 − 2·10⁻⁵)g(4·10⁻⁶)⁻² > 1.4032·10²⁰, which is the
bound of [[thm:loss-d]] (ii).

**Remark {#rem:ec-lb-unbounded}** (No upper bound holds on all of the proved set.) The set 𝖧 = (0, h_*) ∖ 𝖹, with 𝖹
countable, contains numbers h arbitrarily close to 0, and at each of them [[thm:vi-c-2-1]] completes the choice of the
parameters; there [[thm:ec-lb-proved]] gives d_NM > 0.3168γ_C² = 0.3168h⁻². So d_NM is unbounded on the proved set, and
an explicit upper bound for it can hold at points of that set but not on all of it; in particular d_NM exceeds
1.57157·10⁵⁰, the bound of [[thm:uc-integer]], at every point of the proved set with h ≤ 4.48·10⁻²⁶. Likewise, at a
fixed h the conditions on (e_Υ, γ_Υ) are upper bounds together with z ∉ 𝖹_exc, 𝖹_exc countable, so z takes values
arbitrarily close to 0, where the first bound of [[eq:ec-lb-numbers]] grows like z⁻². If (γ_Υ, e_Υ) = (1/100, 1/100)
is admissible at some h ∈ 𝖧, the theorem gives d_NM > 1.4032·10²⁰ there, as at the computational point, and the larger
bound d_NM > 0.3168γ_C² when h < 4.75·10⁻¹¹. The bound 1.2497·10²⁴ of [[cor:uc-two-offsets]] rests on the gap
condition (G) for the index sets as constructed, evaluated at z = 4·10⁻⁶ ([[lem:uc-two-offsets]], [[thm:is-gap]]), and
is stated at that point only.

### Placement

This part and the crosswalk rows below are instructions for merging; they are not chapter text. Line numbers are those
of the chapter sources at the time of writing and serve only to find the place; each old text is quoted exactly, and
each new text is to replace it as a whole, with the line breaks shown.

*1. Where the section goes.* The section above, from its heading through [[rem:ec-lb-unbounded]], is inserted in
[[ch:explicit-constants]] after the paragraph that closes [[sec:ec-delta]], whose last line is "stop." (line 1527),
and before the heading "### An upper bound for the accounted loss {#sec:ec-upper}" (line 1529), with one blank line
before and one after. It defines sec:ec-lb-proved, lem:ec-lb-gauge, eq:ec-lb-g, lem:ec-lb-ind, eq:ec-lb-root,
eq:ec-lb-p, eq:ec-lb-rho, rem:ec-lb-ind, lem:ec-lb-rounds, eq:ec-lb-rounds, thm:ec-lb-proved, eq:ec-lb-bound,
eq:ec-lb-numbers, cor:ec-lb-delta, rem:ec-lb-conditions and rem:ec-lb-unbounded, none of which is defined elsewhere.
The section cites only labels that the chapters define. It changes no number already printed: the bounds 1.403 × 10²⁰,
2.946 × 10²¹, 1.351 × 10²¹, 1.2497 × 10²⁴, 2.624 × 10²⁵, 1.57157 × 10⁵⁰ and 3.30029 × 10⁵¹ at the computational point
stand, as do [[prop:ec-rounds]], [[thm:loss-d]] (ii), [[cor:uc-two-offsets]] and [[thm:uc-integer]] with their proofs.

*2. [[ch:explicit-constants]], the opening paragraph (lines 16–25).* Old, the ten lines:

construction contribute their numbers of steps, among them three nested ones; and at one parameter point of the gauge and
damping parameters two of these iterations alone make d_acc, and so d, larger than 1.403 × 10²⁰ and N_NM larger than
2.946 × 10²¹, each of their steps being charged at least one derivative for the
inverse of the model at the transition face, whose incoming threshold is non-negative ([[lem:ec-theta-in]],
[[thm:loss-d]]), and larger than 1.2497 × 10²⁴ and 2.624 × 10²⁵ for the index sets as the proofs construct them
([[cor:uc-two-offsets]]). At that point, at one admissible choice of the weights and of the free orders and inner
products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the latter the d of [[thm:iii-k-3-2]], at least the
orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at most an integer below 1.57157 × 10⁵⁰, and N_NM at
most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter point lies outside the set on which [[thm:settling]]
is proved ([[rem:ec-point-outside]]), and the bounds bound what this proof's choices produce, not the optimal loss. The

New, the thirteen lines:

construction contribute their numbers of steps, among them three nested ones. Two of these iterations alone, each of
their steps being charged at least one derivative for the inverse of the model at the transition face, whose incoming
threshold is non-negative ([[lem:ec-theta-in]], [[thm:loss-d]]), make d_acc, and so d, larger than
3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²) at every point of the set on which [[thm:settling]] is proved, where
z = 4e_Υγ_Υ² and γ_C are the gauge and damping parameters and g(z) = z/27360 + z²/1088; so d is unbounded on that set
([[thm:ec-lb-proved]]). At one parameter point of the gauge and damping parameters they make d_acc, and so d, larger
than 1.403 × 10²⁰ and N_NM larger than 2.946 × 10²¹ ([[thm:loss-d]]), and larger than 1.2497 × 10²⁴ and 2.624 × 10²⁵
for the index sets as the proofs construct them ([[cor:uc-two-offsets]]). At that point, at one admissible choice of
the weights and of the free orders and inner products ([[def:uc-choice]], [[def:cs-choices]]), d_acc and d_NM, the
latter the d of [[thm:iii-k-3-2]], at least the orders at which its lemmas ask U small ([[prop:uc-d-small]]), are at
most an integer below 1.57157 × 10⁵⁰, and N_NM at most one below 3.30029 × 10⁵¹ ([[thm:uc-integer]]). That parameter
point lies outside the set on which [[thm:settling]] is proved ([[rem:ec-point-outside]]), and the bounds at it bound
what this proof's choices produce, not the optimal loss. The

The next line, "same formulas bound λ1 by δ, …", is unchanged; the text that another proposal gives for lines 26–27
does not overlap this one.

*3. [[ch:explicit-constants]], [[rem:ec-point-outside]] (lines 49–57).* Old, the nine lines:

**Remark {#rem:ec-point-outside}** (The computational point and the proved set.) [[thm:settling]] takes h in the set 𝖧
of [[eq:iv4-0-1]], whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most 10⁻⁶; so h = 10⁻⁶ is not in 𝖧
([[rem:s14-eps-ind-scope]]). The parameters γ_Υ and e_Υ are required in [[thm:vi-c-2-1]] to lie below thresholds whose
existence is proved and whose values are not determined; whether (γ_Υ, e_Υ) = (1/100, 1/100) lies below them is not
decided. So the computational point is a point at which the formulas of the proof can be evaluated, not one at which
the hypotheses of [[thm:settling]] are shown to hold. Every number of this chapter that depends on the point is stated
at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50 ([[prop:np-10-52]] (iii)), and the lower bound of
[[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at every h, ε_Υ being fixed by (γ_Υ, e_Υ)
([[lem:ec-gauge-gap]], [[prop:ec-rounds]]).

New, the seventeen lines:

**Remark {#rem:ec-point-outside}** (The computational point and the proved set.) The computational point lies outside
the set on which [[thm:settling]] is proved, and it lies outside through h. [[thm:settling]] takes h in the set 𝖧 of
[[eq:iv4-0-1]], whose supremum h_* = min(10⁻⁶, h_0, h_tf) is at most 10⁻⁶ whatever the values of h_0 and h_tf, and 𝖧
is open at h_*; so h = 10⁻⁶ is not in 𝖧 ([[rem:s14-eps-ind-scope]]). Whether the gauge half of the point lies in the
proved set is not decided: the parameters γ_Υ and e_Υ are required in [[thm:vi-c-2-1]] to lie below thresholds whose
existence is proved and whose values are not determined, and whether (γ_Υ, e_Υ) = (1/100, 1/100) lies below them is
not decided. [[def:ec-point]] does not fix the parameter γ_(Υ,H) of the horizon modification (row u2 of
[[sec:vi-c-1]]), on which the threshold ε_1 of [[prop:iii-d1-4-1]] for γ_Υ and e_Υ depends, and no number of this
chapter depends on it: the horizon thresholds that enter do not involve it ([[lem:iii-d-5-1]], and [[lem:iii-f2-1-1]],
where y = 0 for the 1-form c_(Υ,H) = −½χ dr), and the indicial roots of (□^Υ_b)^(0), which fix ℳ and ε_Υ, do not
depend on the horizon modification ([[sec:iii-d2-1]]). So the computational point is a point at which the formulas of
the proof can be evaluated, not one at which the hypotheses of [[thm:settling]] are shown to hold. Every number of this
chapter that depends on the point is stated at it. For h ∈ 𝖧 the theorems use only 0 < ε_ind(h) ≤ δ_50
([[prop:np-10-52]] (iii)), and the lower bound of [[thm:loss-d]] uses besides only ε_Υ < 1.46214·10⁻¹⁰, which holds at
every h, ε_Υ being fixed by (γ_Υ, e_Υ) ([[lem:ec-gauge-gap]], [[prop:ec-rounds]]). At every point of the proved set the
lower bound holds as an explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated
([[thm:ec-lb-proved]]).

*4. [[ch:explicit-constants]], the paragraph after the statement of [[thm:loss-d]] (lines 1462–1464).* Old, the three
lines:

The bounds (ii) are lower bounds for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold; for the index sets as the proofs construct them, (G) asks ε_K < μ_G ([[thm:is-gap]]), and the lower
bound rises to 3R > 1.2497 × 10²⁴ ([[cor:uc-two-offsets]]). The bound (iii) is explicit in the numbers of steps, which

New, the five lines:

The bounds (ii) are lower bounds for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold; for the index sets as the proofs construct them, (G) asks ε_K < μ_G ([[thm:is-gap]]), and the lower
bound rises to 3R > 1.2497 × 10²⁴ ([[cor:uc-two-offsets]]). At every point of the set on which [[thm:settling]] is
proved, d_acc ≥ 3R > 3(1 − 2·10⁻⁵) max(g(z)⁻², (13γ_C/40)²), an explicit function of the gauge and damping parameters
([[thm:ec-lb-proved]]). The bound (iii) is explicit in the numbers of steps, which

*5. [[ch:explicit-constants]], [[prop:ec-delta-cap]] (line 1512).* Old, the line:

As d ≥ d_acc, the bound of [[thm:loss-d]] (ii) gives, at the computational point, log₁₀ δ < −1.351 × 10²¹.

New, the two lines:

As d ≥ d_acc, the bound of [[thm:loss-d]] (ii) gives, at the computational point, log₁₀ δ < −1.351 × 10²¹; at every
point of the proved set, [[cor:ec-lb-delta]] bounds log₁₀ δ by a function of the gauge and damping parameters.

*6. [[ch:explicit-constants]], [[rem:ec-not-evaluated]] (lines 4693–4695).* Old, the three lines:

orders of its function spaces only up to admissibility, so explicit constants need those choices made with numbers, which
this chapter does only at a point outside the proved set: [[def:ec-point]] for the gauge and damping parameters, and
[[def:uc-choice]] and [[def:cs-choices]] for the weights, orders and inner products on which d depends. Among the inputs

New, the six lines:

orders of its function spaces only up to admissibility, so explicit constants need those choices made with numbers, which
this chapter does only at a point outside the proved set: [[def:ec-point]] for the gauge and damping parameters, and
[[def:uc-choice]] and [[def:cs-choices]] for the weights, orders and inner products on which d depends. The lower bound
for d of [[thm:ec-lb-proved]] needs no such choice: it holds at every point of the proved set as an explicit function
of the gauge and damping parameters, and it tends to infinity as they tend to 0, so that no upper bound for d holds on
all of that set ([[rem:ec-lb-unbounded]]). Among the inputs

*7. The front matter, the abstract (lines 32–37).* Old, the six lines:

far as they are explicit, among them an upper bound for λ0 at a numerical point and, at a parameter point outside the set
on which settling is proved, for one admissible choice of the weights, orders and inner products and the index sets as
the proofs construct them, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰ for the loss d with which the settling proof applies the
Nash–Moser theorem; at equality, μ0 = √72 l5², timelike curves of g_λ cross the boundary in a layer whose width tends to
zero with λ; and at the physical wavelength 10 l5 there is no separation of scales, existence holding where the solution
is the seed.

New, the seven lines:

far as they are explicit, among them an upper bound for λ0 at a numerical point; for the loss d with which the settling
proof applies the Nash–Moser theorem, a lower bound at every point of the set on which settling is proved, which grows
like the inverse square of the gauge and damping parameters, so that d is unbounded on that set, and, at a parameter
point outside it, for one admissible choice of the weights, orders and inner products and the index sets as the proofs
construct them, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰; at equality, μ0 = √72 l5², timelike curves of g_λ cross the
boundary in a layer whose width tends to zero with λ; and at the physical wavelength 10 l5 there is no separation of
scales, existence holding where the solution is the seed.

*8. [[ch:introduction]], [[sec:introduction-scope]] (lines 150–154).* Old, the five lines:

evaluated; [[prop:lambda0]] bounds λ0 above at a numerical point, and [[ch:explicit-constants]] states where the explicit
evaluation of λ1 and δ stops and bounds the loss d with which the proof of [[thm:settling]] applies the Nash–Moser
theorem at a point of the gauge and damping parameters outside the set on which that theorem is proved: there
d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and
d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A

New, the seven lines:

evaluated; [[prop:lambda0]] bounds λ0 above at a numerical point, and [[ch:explicit-constants]] states where the explicit
evaluation of λ1 and δ stops and bounds the loss d with which the proof of [[thm:settling]] applies the Nash–Moser
theorem. At every point of the set on which that theorem is proved, d > 2.2456 × 10⁹ z⁻²(1 + 25.15z)⁻² and
d > 0.3168 γ_C², z = 4e_Υγ_Υ² and γ_C being the gauge and damping parameters of [[ch:s13]] and [[ch:s14]]
([[thm:ec-lb-proved]]), so that d is unbounded on that set. At a point of the gauge and damping parameters outside it,
d > 1.2497 × 10²⁴ at every admissible choice of the weights, for the index sets as the proofs construct them, and
d < 1.57157 × 10⁵⁰ at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]). A

*9. [[ch:theorems]], [[sec:further-results]], the item on the constants (lines 351–357).* Old, the seven lines:

- *The constants of [[thm:settling]].* The loss d with which the Nash–Moser step is applied, at least the loss that
  the proof assigns to the tame estimates, and its regularity N_NM = 21d + 6, with explicit lower bounds at a
  parameter point that lies outside the proved set ([[thm:loss-d]]) and, there, explicit upper bounds for d and N_NM
  at one admissible choice of the weights, orders and inner products ([[thm:uc-integer]]); through the lower bounds,
  upper bounds for δ and for the modulus of the initial family at 2δ (and λ1 < δ); explicit resolvent bounds on
  five-dimensional Tangherlini ([[ch:resolvent-bounds]]); and where explicit evaluation of λ1 and δ stops
  ([[ch:explicit-constants]]).

New, the nine lines:

- *The constants of [[thm:settling]].* The loss d with which the Nash–Moser step is applied, at least the loss that
  the proof assigns to the tame estimates, and its regularity N_NM = 21d + 6, with explicit lower bounds at every point
  of the proved set, as functions of the gauge parameter z = 4e_Υγ_Υ² and the damping parameter γ_C that grow like z⁻²
  and γ_C² ([[thm:ec-lb-proved]]); at a parameter point that lies outside the proved set, explicit lower bounds
  ([[thm:loss-d]]) and explicit upper bounds for d and N_NM at one admissible choice of the weights, orders and inner
  products ([[thm:uc-integer]]); through the lower bounds, upper bounds for δ and for the modulus of the initial family
  at 2δ (and λ1 < δ); explicit resolvent bounds on five-dimensional Tangherlini ([[ch:resolvent-bounds]]); and where
  explicit evaluation of λ1 and δ stops ([[ch:explicit-constants]]).

*10. [[ch:scope]], [[sec:scope-constants]] (lines 66–67).* Old, the two lines:

iterations of the construction ([[thm:loss-d]] (i)). At the
computational point of [[def:ec-point]], d > 1.403 × 10²⁰ and N_NM > 2.946 × 10²¹, so that log₁₀ δ < −1.351 × 10²¹

New, the six lines:

iterations of the construction ([[thm:loss-d]] (i)). At every point of the set on which [[thm:settling]] is proved,
with z = 4e_Υγ_Υ² and γ_C the gauge and damping parameters, d > 2.2456 × 10⁹ z⁻²(1 + 25.15z)⁻², d > 0.3168 γ_C²,
N_NM > 4.7158 × 10¹⁰ z⁻²(1 + 25.15z)⁻² and N_NM > 6.654 γ_C², so that log₁₀ δ < −2.163 × 10¹⁰ z⁻²(1 + 25.15z)⁻² and
log₁₀ δ < −3.052 γ_C² ([[thm:ec-lb-proved]], [[cor:ec-lb-delta]]); these bounds tend to infinity as z or γ_C⁻¹ tends
to 0, so that no upper bound for d holds on all of that set ([[rem:ec-lb-unbounded]]). At the
computational point of [[def:ec-point]], d > 1.403 × 10²⁰ and N_NM > 2.946 × 10²¹, so that log₁₀ δ < −1.351 × 10²¹

The text that another proposal gives for lines 72–73 of this section does not overlap this one.

*11. Unchanged.* [[def:ec-point]], [[lem:ec-gauge-gap]], [[rem:ec-gauge-gap]], [[prop:ec-rounds]] (whose last sentence,
on every h ∈ 𝖧 with the same (γ_Υ, e_Υ), stays true and is the case z = 4·10⁻⁶ of [[thm:ec-lb-proved]]), the statement
of [[thm:loss-d]], [[cor:uc-two-offsets]], [[thm:uc-reduction]], [[thm:uc-integer]] with [[eq:uc-lower]], and every
statement of [[ch:s14]] keep their texts. The numeric lower bound 1.2497 × 10²⁴ stays a statement at the computational
point: it needs the least excess μ_G of the gap condition, which [[thm:is-gap]] evaluates at z = 4·10⁻⁶ only.

### Crosswalk rows

Rows for the crosswalk of [[ch:explicit-constants]], in its four columns (label, source, source name, note), separated
by tabs; the line numbers are those of this file:

    sec:ec-lb-proved	paper/reader/proofs/P-LB.md:1	P-LB, section	new; after sec:ec-delta
    lem:ec-lb-gauge	paper/reader/proofs/P-LB.md:12	P-LB, Lemma (ℳ, every gauge point)	new: 𝔡_ℳ ≤ z/13680 + z²/544
    eq:ec-lb-g	paper/reader/proofs/P-LB.md:31	P-LB, display	g(z) = z/27360 + z²/1088 bounds ε_Υ
    lem:ec-lb-ind	paper/reader/proofs/P-LB.md:76	P-LB, Lemma (index distance, every h)	new: ε_ind(h) < 40h/13
    eq:ec-lb-root	paper/reader/proofs/P-LB.md:79	P-LB, display	root of P_2 near 2, two-sided
    eq:ec-lb-p	paper/reader/proofs/P-LB.md:87	P-LB, display	P_2(2 + hξ) in powers of h
    eq:ec-lb-rho	paper/reader/proofs/P-LB.md:106	P-LB, display	remainder below 0.0017
    rem:ec-lb-ind	paper/reader/proofs/P-LB.md:131	P-LB, Remark (root ι₂(h))	consistency at 10⁻⁶; sharpness
    lem:ec-lb-rounds	paper/reader/proofs/P-LB.md:138	P-LB, Lemma (rounds, general)	prop:ec-rounds with δ̂, δ̄
    eq:ec-lb-rounds	paper/reader/proofs/P-LB.md:148	P-LB, display	R > (1 − 5δ̂ − δ̄)/δ̂²
    thm:ec-lb-proved	paper/reader/proofs/P-LB.md:185	P-LB, Theorem (proved set)	new: functional lower bound
    eq:ec-lb-bound	paper/reader/proofs/P-LB.md:197	P-LB, display	d_acc, N_NM against 1/δ̂²
    eq:ec-lb-numbers	paper/reader/proofs/P-LB.md:202	P-LB, display	2.2456e9/z², 0.3168γ_C²
    cor:ec-lb-delta	paper/reader/proofs/P-LB.md:236	P-LB, Corollary (δ, proved set)	from prop:ec-delta-cap
    rem:ec-lb-conditions	paper/reader/proofs/P-LB.md:250	P-LB, Remark (what is used)	conditions used and unused
    rem:ec-lb-unbounded	paper/reader/proofs/P-LB.md:274	P-LB, Remark (unbounded)	d unbounded on the proved set

Notes to add to existing rows. Crosswalk of [[ch:explicit-constants]]: ch:explicit-constants, "opening states the
lower bound on the proved set (P-LB text 2)"; rem:ec-point-outside, "rewritten: outside through h, gauge half
undecided, γ_(Υ,H) not fixed and not used; last sentence cites thm:ec-lb-proved (P-LB text 3)"; thm:loss-d, "paragraph
after the statement cites thm:ec-lb-proved (P-LB text 4)"; prop:ec-delta-cap, "cites cor:ec-lb-delta (P-LB text 5)";
rem:ec-not-evaluated, "the lower bound needs no numeric choice (P-LB text 6)". Crosswalk of [[ch:introduction]]:
sec:introduction-scope, "lower bound on the proved set (P-LB text 8)". Crosswalk of [[ch:theorems]]:
sec:further-results, "constants item: lower bounds on the proved set (P-LB text 9)". Crosswalk of [[ch:scope]]:
sec:scope-constants, "lower bounds on the proved set, δ included (P-LB text 10)". The front matter has no labels and its
crosswalk no rows; text 7 changes the abstract only.
