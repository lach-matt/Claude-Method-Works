### The constant ε_Υ at the computational point {#sec:ec-gauge-gap}

The transition face rounds and the level-3 rounds of [[sec:ec-floor]] raise their weights by ε_g − ε, and ε_g =
min(ε_Υ, ε_ind) ([[def:s21-eps-g]]). The constant ε_Υ of [[sec:iii-d2-1]] is fixed below half the least distance
between distinct points of the set ℳ of the real parts of the indicial roots of (□^Υ_b)^(0) shifted by integers, cut
to [−10, 10]. At the computational point that distance is set by two roots of high angular order, and it is much
smaller than δ_50. Throughout, z = 4·10⁻⁶ and, for l ≥ 1, d₂(l) and d₁(l) are the numbers d₂ and d₁ of
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
([[cor:s14-eps-ind-point]]), so ε_Υ < δ_50/132, and ε_g = ε_Υ whenever ε_ind is taken at least ε_Υ, as it may be. In
every case ε_g ≤ ε_Υ < 1.46214·10⁻¹⁰. The construction of [[ch:s21]] and [[ch:s22]] advances its transition face and
level-3 weights by ε_g − ε and asks ε_K < ε_Υ ([[def:iii-i10-1-3]]); both long iterations of [[sec:ec-floor]] are
therefore governed by ε_Υ, the separation of the shifted roots of the gauge potential operator, and not by ε_ind.

**Proposition {#prop:ec-rounds}** (The number of rounds.) At the computational point, for every choice of ε_K, ε_+,
η_2, α, the levels and the losses ε, ε′ admissible for [[thm:iii-i14-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i13-2-1]], the transition face rounds at the levels below 3 and the level-3 rounds at the levels in (3, 4)
number together

    R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_K δ̂) > (1 − 5δ̂ − δ̄)/δ̂² > 4.6775 × 10¹⁹,     δ̂ := 1.46214·10⁻¹⁰.

The same bound holds at every h ∈ 𝖧, with the same (γ_Υ, e_Υ).

*Proof.* The weights satisfy 0 < ε_K < ε_Υ < δ̂ ([[def:iii-i10-1-3]] and [[lem:ec-gauge-gap]], as ½ · 2.92428·10⁻¹⁰ <
δ̂), and ε_g ≤ ε_Υ. The proof of [[lem:iii-i8-3-2]] takes ε < ½ε_g, and ε′ ≤ ε ([[sec:iii-j2-1]]); so the increments
ε_g − ε of the rounds lie in (0, δ̂), and ε, ε′ < δ̂. Also η_2 < ε_+ < ε_ind ≤ δ_50 < δ̄ ([[prop:np-10-52]] (iii)).
The level spacing is below α − 4 ≤ ε_K.

*Below 3.* At a level β ∈ (2, 3), τ_0 = 2 + ε_g − 2ε < 2 + δ̂ and τ_i < 2 + (i + 1)δ̂, and the rounds run for every i
with τ_i ≤ β − ε′, the τ_i being increasing; so their number is at least the number of i ≥ 0 with 2 + (i + 1)δ̂ ≤ β −
δ̂, which is at least g_1(β)/δ̂ with g_1(x) := (x − 2 − 2δ̂)_+. The levels in (2, 3) form a sequence b_1 < ⋯ < b_m
with b_1 = α_1 < α − 2 ≤ 2 + ε_K and b_m > 3 − ε_K. By [[lem:ec-level-sum]] with c = ε_K, and as g_1 vanishes below 2 +
2δ̂ > b_1,

    Σ_j g_1(b_j)/δ̂ ≥ (1/(ε_Kδ̂))((1 − ε_K − 2δ̂)²/2 − ε_K/2).

*Between 3 and 4.* At a level β ∈ (3, 4), κ_i := κ_3 + i(ε_g − ε) < 1 + δ̄ + iδ̂, as κ_3 = 1 + η_2 − 2ε; the rounds
run for every i with κ_i ≤ β − 2, and their number is at least g_2(β)/δ̂ with g_2(x) := (x − 3 − δ̄)_+. The levels in
(3, 4) form a sequence c_1 < ⋯ < c_p with c_1 < 3 + ε_K and c_p > 4 − ε_K, and by [[lem:ec-level-sum]]

    Σ_j g_2(c_j)/δ̂ ≥ (1/(ε_Kδ̂))((1 − ε_K − δ̄)²/2 − ε_K/2).

Adding, and using (1 − a)²/2 ≥ ½ − a, R > (1 − 3ε_K − 2δ̂ − δ̄)/(ε_Kδ̂); with ε_K < δ̂ this exceeds (1 − 5δ̂ −
δ̄)/δ̂², and δ̂² < 2.13786·10⁻²⁰, 1 − 5δ̂ − δ̄ > 1 − 2.1·10⁻⁸, so the quotient exceeds 4.6775·10¹⁹. Nothing in the
proof used h beyond the bounds ε_g ≤ ε_Υ < δ̂ and ε_ind(h) ≤ δ_50, which hold at every h. ∎

**Theorem {#thm:loss-d}** (The loss d and the regularity N_NM.) Let d_acc be the accounted loss of
[[def:ec-accounted-loss]]. Then [[thm:iii-j2-4-1]] and [[thm:iii-j2-4-2]] hold with d = d_acc, the Nash–Moser theorem
[[thm:ii-g-2-1]] is applied in the proof of [[thm:iii-k-3-2]] at the regularity N_NM = 21d_NM + 6 with d_NM ≥ d_acc,
and:

(i) d_acc is composed, by the rules of [[def:ec-accounted-loss]], of elementary losses and of the numbers of steps of
the iterations of [[sec:ec-floor]], each round being charged at least the loss of [[lem:ec-round-loss]]; the
elementary losses are closed forms in the weights, the thresholds ϑ_in, ϑ_ℋ, the regularity orders s_c and the counts
n(E, β) of the index sets ([[lem:ec-closed-forms]], [[rem:ec-other-losses]]), and the loss of the forward solution
operators, which is at most 20,180 ([[thm:fwd-loss]]);

(ii) at the computational point, for every admissible choice of the weights there,

    d_NM ≥ d_acc ≥ (2 + ℓ_tf) R ≥ 3R > 1.403 × 10²⁰,        N_NM = 21d_NM + 6 > 2.946 × 10²¹,

with R the number of rounds of [[prop:ec-rounds]] and ℓ_tf ≥ 1 the loss of [[cor:iii-f1-3-4]];

(iii) d_acc is bounded above by [[prop:ec-upper]], explicitly in the counts of the long iterations and in finitely
many losses of single steps.

The bound (ii) is a lower bound for the loss that this proof's choices produce, not for the least loss with which the
tame estimates hold.

*Proof.* The first assertions are [[lem:iii-j2-1-2]] with [[lem:ec-split-loss]], which give the tame estimates with
any loss at least the accounted one, the parameters of [[thm:ii-g-2-1]] ([[eq:ii-g-2-5]]) and d_NM ≥ d_acc
([[def:ec-accounted-loss]] and the paragraph after it). (i) is [[def:ec-accounted-loss]] with [[lem:ec-closed-forms]],
[[rem:ec-other-losses]] and [[lem:ec-round-loss]].

(ii) Level k + 1 of [[thm:iii-i14-3-1]] takes the solution of level k as input through R_qu, and at each level the
rounds of [[sec:ec-floor]] are composed one after another, each round's output being the next round's forcing, and the
level's solution being assembled from the outputs of all its rounds and from the inverse applied to the last forcing.
So all the rounds of all the levels lie on one chain of compositions, and by [[def:ec-accounted-loss]] and
[[lem:ec-round-loss]] (a), d_acc ≥ (2 + ℓ_tf)R. By [[lem:ec-closed-forms]] (d), whose proof uses [[lem:ec-theta-in]],
ℓ_tf ≥ 1; so by [[prop:ec-rounds]], d_NM ≥ d_acc ≥ 3R > 3 · 4.6775·10¹⁹ > 1.403·10²⁰, and N_NM = 21d_NM + 6 > 21 ·
1.403·10²⁰ > 2.946·10²¹. (iii) is [[prop:ec-upper]]. ∎

**Proposition {#prop:ec-delta-cap}** (The thresholds δ and λ1.) In the proof of [[thm:settling]], let the Nash–Moser
threshold be ε_NM = θ_0^(−(8d+2)), with θ_0 as chosen in the proof of [[thm:ii-g-2-1]] and d = d_NM the loss of the
proof of [[thm:iii-k-3-2]]; let ε be the data threshold of [[cor:s27-rate]], chosen, as in the proof of
[[thm:iii-k-3-2]], with ε ≤ s_(2d) and C_(2d)ω_(2d)(ε) ≤ ε_NM, where C_(2d) ≥ 1, s_(2d) and the modulus ω_(2d) are
those of [[lem:iii-k-2-2]] (d) at the order 2d ([[prop:iii-k-1-2]] (3)); and let C_R ≥ 1 be the constant of
[[cor:vii-2-3]]. Then δ = ½ε and λ1 satisfy

    λ1 < δ,        ω_(2d)(2δ) ≤ 2^(−(32d+8)),        log₁₀ ω_(2d)(2δ) < −(59/196)(32d + 8).

As d = d_NM ≥ d_acc, [[thm:loss-d]] (ii) gives log₁₀ ω_(2d)(2δ) < −1.351 × 10²¹. If moreover ω_(2d)(s) ≥ s/A on [0,
s_(2d)] for some A ≥ 1, then δ ≤ A·2^(−(32d+9)).

*Proof.* The proof of [[thm:ii-g-2-1]] chooses θ_0 ≥ 16η_0^(−2) with η_0 ≤ 1, so θ_0 ≥ 16 and ε_NM ≤ 16^(−(8d+2)) =
2^(−(32d+8)). So ω_(2d)(2δ) = ω_(2d)(ε) ≤ ε_NM/C_(2d) ≤ 2^(−(32d+8)). The proof of [[thm:settling]] ([[sec:vii-4]])
takes λ1 with C_Rλ1 < ½ε = δ, so λ1 < δ/C_R ≤ δ. Next, 2^10 = 1.024·10³, so 2^196 = 2^190·2^6 = 1.024^19·10^57·64, and
by the binomial expansion, all of whose terms are positive, 1.024^19 > 1 + 19x + 171x² + 969x³ > 1.5678 > 100/64 with
x = 0.024; so 2^196 > 10^59 and log₁₀ 2 > 59/196, which gives the third bound. With d > 1.403·10²⁰, (59/196)(32d + 8) >
1.351·10²¹. Under the last hypothesis, ε/A ≤ ω_(2d)(ε) ≤ 2^(−(32d+8)), so δ = ½ε ≤ A·2^(−(32d+9)). ∎

The bounds hold whatever the other constants are, once each constant of an upper bound is taken at least 1, which
enlarging it allows. A lower bound for δ or λ1 would need lower bounds for θ_0^(−1), the inverse of ω_(2d) and 1/C_R,
that is, upper bounds for every constant of the proof that enters them; [[rem:ec-not-evaluated]] says where those
stop.

### An upper bound for d {#sec:ec-upper}

This section bounds d_acc from above. The bound is explicit in the numbers of steps of the long iterations, which it
counts from above, and in the losses of their single steps; the remaining steps of the construction enter through
finitely many losses of single steps, each finite and charged once per level or once in all. First, the rule by which
the background terms are charged.

**Lemma {#lem:ec-split-loss}** (Families with a split loss.) Call a family (T_β), E → G, *tame with split loss* (a; c,
b), a, c, b ∈ ℕ₀, if for every k there is C_k with

    ‖T_β e‖_(G^k) ≤ C_k (‖e‖_(E^(k+a)) + ‖β‖_(k+c) ‖e‖_(E^b)),     β ∈ 𝔹, e ∈ E^∞.             {#eq:ec-split-loss}

Let δ_𝔹 ≤ 1. (a) Such a family is tame with loss max(a, c, b) in the sense of [[def:iii-j2-1-1]]. (b) If (T_β) has
split loss (a; c, b), (S_β), G → H, has split loss (a′; c′, b′), and d_0 ≥ b′ + c, then (S_βT_β) has split loss (a +
a′; max(c′, a′ + c), max(b, a + b′)). (c) Let T_1, …, T_m have split losses (a_i; c_i, b_i), and let d_0 ≥ Σ_i a_i +
max_i c_i + max_i b_i. Then T_m ⋯ T_1 is tame with loss

    Σ_i a_i + max_i (max(c_i, b_i) − a_i)_+,

and a sum of families with split losses (a_i; c_i, b_i) has split loss (max a_i; max c_i, max b_i).

*Proof.* (a) The norms are non-decreasing in k, so ‖e‖_(k+a) ≤ ‖e‖_(k+d), ‖β‖_(k+c) ≤ ‖β‖_(k+d) and ‖e‖_b ≤ ‖e‖_d for
d := max(a, c, b). (b) By [[eq:ec-split-loss]] for S and then for T,

    ‖S_βT_βe‖_k ≤ C_k (‖T_βe‖_(k+a′) + ‖β‖_(k+c′) ‖T_βe‖_(b′))
               ≤ C_k (‖e‖_(k+a+a′) + ‖β‖_(k+a′+c) ‖e‖_b + ‖β‖_(k+c′) (‖e‖_(b′+a) + ‖β‖_(b′+c) ‖e‖_b)),

and ‖β‖_(b′+c) ≤ ‖β‖_(d_0) < 1 and ‖e‖_b, ‖e‖_(a+b′) ≤ ‖e‖_(max(b,a+b′)) give the split loss stated. (c) By (b) and
induction, T_m ⋯ T_1 has split loss (Σ_i a_i; max_i(c_i + Σ_(j>i) a_j), max_i(b_i + Σ_(j<i) a_j)), the hypotheses d_0
≥ b′ + c of the steps holding by that on d_0. Each of c_i + Σ_(j>i) a_j and b_i + Σ_(j<i) a_j is at most Σ_j a_j +
(max(c_i, b_i) − a_i)_+, and (a) gives the loss. Sums: as in [[lem:iii-j2-1-2]] (a). ∎

The families of [[lem:iii-j2-2-1]] fall into this frame. A linear map independent of β bounded E^(k+m) → G^k has split
loss (m; 0, 0) ([[lem:iii-j2-1-2]] (d)). The forward solution operators have split loss (d_F; d_F, d_F), d_F the loss
d of [[thm:iii-i-5-3]] ([[eq:iii-i-5-2]]), at most 20,180 ([[thm:fwd-loss]]). The background terms of
[[lem:iii-j2-2-1]] (b), and the operator L̃ of [[lem:iii-j2-2-1]] (g) where its coefficients depend on h, have split
loss (2; d_BG, d_BG), d_BG the order in the background of their bound ‖Au‖_k ≤ C_k(‖u‖_(k+2) + ‖β‖_(k+d_BG)‖u‖_(d_BG));
in the sense of [[def:iii-j2-1-1]] they are tame with loss max(2, d_BG), the charge of [[rem:ec-other-losses]]. By (c)
the excess over 2 need only be paid once: a composition in which every background term is charged 2 and every other
family its loss is tame with that sum plus (d_BG − 2)_+, whatever the number of background terms in it. The fixed
operators L_b, L̂_b(σ) and L̃_b at the background 0, which alone enter the rounds and windows of the long iterations,
have split loss (2; 0, 0), so the excess does not enter those iterations either way. A finite-rank map e ↦ Σ_i (ℓ_βe)_i v^i with |ℓ_βe| ≤ C‖e‖_(d_ℓ) and
fixed sections v^i, as the rows and the coefficient maps of the construction are ([[lem:iii-j2-2-1]] (c)), has split
loss (d_ℓ; 0, d_ℓ), so it adds no excess.

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

**Lemma {#lem:ec-round-charges}** (The losses of single rounds, from above.) In the accounting of
[[def:ec-accounted-loss]], with ℓ_tf the loss of [[cor:iii-f1-3-4]]:

(a) a transition face round of the proof of [[lem:iii-i8-3-2]], and a level-3 round of the proof of
[[prop:iii-i13-2-1]] at a level β < 4, map the current forcing to the next one with a loss at most ℓ_tf + 2; a level-3
round of the proof of [[prop:iii-i11-3-1]] at a level β > 4 does so with a loss at most ℓ_tf + 4;

(b) one application of [[prop:iii-g4-4-4]] at level 1 or 2 of the proof of [[prop:iii-i11-3-1]], to the term of the
forcing at one exponent with all its logarithmic powers, maps that term to u and to the remainder [[eq:iii-g4-4-3]]
with a loss at most ℓ_tf + 2;

(c) one window of Step 2 of the proofs of [[prop:iii-i5-2-1]], [[lem:iii-i8-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i10-3-1]] maps the current forcing to the next one with a loss at most d^max_ι + 2 + 2⌈ℓ_I − 5/2⌉, where
d^max_ι is the largest value of d_ι(ϰ) of [[eq:ec-iota-loss]] on λ_♯ ≤ Re ϰ < 2. If 3 < ℓ_I < 3.5 and δ < 3.5 − ℓ_I,
then d^max_ι ≤ 12, and the loss is at most d^max_ι + 4 ≤ 16.

*Proof.* We read the proofs at a finite b-regularity k and charge each map with its loss. Multiplication by smooth
functions, by powers of σ and by the cut-offs, the coefficients of a partial expansion, the stationary states and the
formal solutions with their coefficients, and holomorphic families evaluated or differentiated in a parameter on a
fixed circle cost nothing. Two facts are used. First, if R ∈ H^(k,b)_b near ztf and the contour shift of
[[lem:iii-g4-3-4]] is made, then ℳR on the new line is N₀(λ)⁻¹Φ(λ), where Φ involves ℳ(PR) at the order k − 2 and
N₁ℳR(λ − 1) at the order k − 1; by (E1) and (E2) of [[sec:iii-a-1-1]], N₀(λ)⁻¹ gains two orders jointly in λ and on
𝕊³, so R̃ and the residues lie at the order k: each step of the expansions of [[thm:iii-g4-3-1]] and of Step 2 of the
proof of [[prop:iii-g4-5-1]] costs nothing. Second, N_tf does not depend on σ and commutes with σ∂_σ, so the loss ℓ_tf
of [[cor:iii-f1-3-4]] holds in the joint b-regularity in (σ, r̂, ω).

(a) In Step 3.4′ of the proof of [[lem:iii-i8-3-2]], [[prop:iii-g4-5-1]] is applied with k₀ = 1 > ⌊ℓ_zf⌋ (ℓ_zf < 0),
so Step 1 of its proof is empty: f₁ is the forcing cut off, u₁ = N_tf⁻¹(|σ|^(−α)f₁) costs ℓ_tf, the expansion
[[eq:iii-g4-5-5]] and u₂ cost nothing, and the remainder f₁ − L̂_b(σ)u₂ costs 2 more, L̂_b(σ) being of second order
and fixed. The next forcing f̂^((i+1)) = f̂^((i)) − σL̂_b(σ)v_i is σ times that remainder. So the round costs at most
ℓ_tf + 2. At a level β ∈ (3, 4), Step 4 of the proof of [[prop:iii-i13-2-1]] applies [[prop:iii-g4-5-1]] with ℓ_zf =
ℓ_3 < 0 and the order 0 of the zf-index set, so again ⌊ℓ_zf⌋ < 0, Step 1 is empty, and the round costs at most ℓ_tf +
2. At β > 4, ℓ_3 ∈ (0, ε_K), and Step 1 runs for j = 0 only: v_0 solves 𝒩v_0 = ρ^(α−2)χ₃f^((0)) by Mellin inversion on
a line free of roots, which costs nothing (𝒩 is elliptic and dilation invariant, (E1)–(E2) of [[sec:iii-a-1-1]]), and
the terms e_0, which apply to U_0 the operators L̂_b(σ) − L̄̂(σ), ρ(ρ∂_ρ − 3/2 − S̄) and the commutators with the
cut-offs, cost at most 2; then f₁ costs at most 2, and the round at most ℓ_tf + 4.

(b) In the proof of [[prop:iii-g4-4-4]], f₀ is a coefficient of the term (no loss), u_(tf,α) = N_tf⁻¹(ρ_ztf^(−α)f₀)
costs ℓ_tf, its expansion [[eq:iii-g4-3-3]] costs nothing (the first fact), W_α and u_α are built from it and from the
states (no loss), and F_α = χ_tf ρ_tf^α f₀ − L̂_b(σ)u_α costs 2 more. Step 2 takes ∂^k_α at α₀, a Cauchy integral over
a small circle of holomorphic families bounded at each order, which costs nothing. So u costs at most ℓ_tf and the
remainder at most ℓ_tf + 2.

(c) In a window, [[cor:iii-g2-4-3]] is applied to the terms of the forcing F at each λ_0 of the window, in parallel.
By [[lem:iii-j2-2-1]] (g) its error, which is the terms of F at λ_0 minus L_bu_(λ_0), has the loss d_ι(λ_0) + 2. The
expansion at 𝓘⁺ of that error is removed by [[prop:iii-i1-3-1]]: its 𝓘⁺-exponents are those of ℰ^tot_(ι⁺,𝓘) + 2 to the
order ℓ_I + 1, with no ρ_I^(z+1)-term for Re z < 5/2 (Step 2 of the proof of [[prop:iii-i5-2-1]]); as ℰ^tot_(ι⁺,𝓘) =
⋃_(s∈σ_Υ)(3/2 + s, 0) has no logarithms, the terms to be removed sit at z ∈ 5/2 + σ_Υ + ℕ₀ with Re z ≤ ℓ_I, all of
logarithmic order 0, and they lie in the ⌈ℓ_I − 5/2⌉ windows [5/2 + j, 7/2 + j) of the proof of [[prop:iii-i1-3-1]].
That proof treats the terms of one window in parallel, each by [[lem:iii-a-1-2]] and the fixed inverse (z − 3/2 −
Ā)⁻¹, at no cost, and passes to the next window the remainder f − L_b(χρ_I^z u^((z,0))), which costs 2 and creates
only terms of logarithmic order 0 at z + j, j ≥ 1. So u′_(λ_0) costs at most 2(⌈ℓ_I − 5/2⌉ − 1) beyond the error. The
next forcing is F − Σ_(λ_0) L_b(u_(λ_0) + u′_(λ_0)), that is, the terms of F outside the window, unchanged, plus the
errors minus L_bu′_(λ_0), which costs 2 more. So a window costs at most d_ι(λ_0) + 2 + 2⌈ℓ_I − 5/2⌉. The bound d^max_ι
≤ 12 is [[lem:ec-closed-forms]] (e) on λ_♯ ≤ Re ϰ < 2 < ℓ_I, and ⌈ℓ_I − 5/2⌉ = 1 for 3 < ℓ_I < 3.5. ∎

**Lemma {#lem:ec-counts}** (The lengths of the long iterations, from above.) Make admissible choices of the weights of
[[thm:iii-i14-3-1]] and of the results it uses, and put

    ι := ε_g − ε,     s := min_k (β_(k+1) − β_k),

with ε the loss of [[lem:iii-i8-3-2]] and [[prop:iii-i13-2-1]] (so ε < ½ε_g and ι > ½ε_g) and β_0 = α_1 < β_1 < ⋯ <
β_K = α the levels of Step 2 of the proof of [[thm:iii-i14-3-1]]. Let a_K ∈ (α_1, α − 2) be the K⁺-order with which
Step 1 of that proof uses the background h + h_rem(q). Then:

(a) at most N_< := (3 − α_1)/s of the levels β_1, …, β_K lie in (2, 3), at most N_> := (α − 3)/s + 1 lie in (3, α],
and, if s > ½(α − 4), at most two lie in (4, α];

(b) at a level β ∈ (2, 3) the transition face rounds number at most (β − 2)/ι + 1, and summed over the levels in (2,
3) at most

    T_< := (1 + s/2)²/(2sι) + N_<;

(c) at a level β ∈ (3, α] the level-3 rounds number at most (β − 3)/ι + 2, and summed over the levels in (3, α] at
most

    T_> := (α − 3 + s/2)²/(2sι) + 2N_>;

(d) at a level β ∈ (3, α], the applications of [[prop:iii-g4-4-4]] at level 1 act on separate terms of g_1 and none on
the output of another, and at level 2 every exponent treated is reached from an exponent of g_2 through at most (1 +
η_2 − η_1)/ε_Υ remainders of earlier applications;

(e) every window loop (Step 2 of the proofs of [[prop:iii-i5-2-1]], [[lem:iii-i8-3-1]], [[lem:iii-i8-3-2]] and
[[prop:iii-i10-3-1]]) has at most W := (2 − λ_♯)/ε_Υ + 1 windows;

(f) in the base, the rounds of [[prop:iii-i5-2-1]] that Step 0 of the proof of [[lem:iii-i8-3-1]] runs number at most
N_b := 1/(a_K − 2) + 1, and the steps of [[prop:iii-i2-5-1]] that the start of its proof runs at most N_b + 1.

*Proof.* (a) The levels are increasing, at least s apart, and β_1 > α_1. Those in (2, 3) lie in (α_1 + s, 3), so there
are at most (3 − α_1)/s of them; those in (3, α] lie in an interval of length α − 3 closed at the top, so there are at
most (α − 3)/s + 1; those in (4, α] lie in an interval of length α − 4 < 2s.

(b) In Step 3.4′ of the proof of [[lem:iii-i8-3-2]] at the level β, τ_0 = 2 + ε_g − 2ε > 2 and τ_(i+1) = τ_i + ι, and
the rounds run for the i with τ_i ≤ β − ε′; so i ≤ (β − 2)/ι, and there are at most (β − 2)/ι + 1 of them. Let b_1 < ⋯
< b_m be the levels in (2, 3). Then b_j < 3 − (m − j)s, so

    Σ_j (b_j − 2) < Σ_(i=0)^(m−1) (1 − is) = m − s m(m − 1)/2 ≤ (1 + s/2)²/(2s),

the last as the quadratic −(s/2)(m − 1/s − ½)² + (s/2)(1/s + ½)² in m is at most its maximum. Summing the bound on the
rounds over the m ≤ N_< levels gives T_<.

(c) At a level β ∈ (3, 4), Step 4 of the proof of [[prop:iii-i13-2-1]] starts at κ_3 = 1 + η_2 − 2ε > 1, raises κ by ι
per round, and runs while κ ≤ β − 2; so there are at most (β − 3)/ι + 1 rounds. At a level β ∈ (4, α], Step 4 of the
proof of [[prop:iii-i11-3-1]] takes α_κ = min(κ, 2 − δ); while κ < 2 − δ each round raises κ by ι, and the first round
with κ ≥ 2 − δ ends the loop; so there are at most (2 − δ − κ_3)/ι + 2 < (β − 3)/ι + 2 rounds. As in (b), for levels
c_1 < ⋯ < c_p in (3, α], Σ_j (c_j − 3) ≤ (α − 3 + s/2)²/(2s), and summing gives T_>.

(d) At level 1 (Step 2 of the proof of [[prop:iii-i11-3-1]]) the remainders have tf-exponents of real part at least 2 +
ε_g > 2 + η_1, outside the window [2, 2 + η_1) of level 1; so no application acts on the output of another. At level
2 (Step 3) the window is [1 + η_1, 2 + η_2), and the application at (α_0, k) leaves its remainder at the exponents
(α_0, k) + ℰ_ind and (4, k + 1) + ((0, 0) ∪ ℰ_ind) ([[eq:iii-g4-4-3]]), with min Re ℰ_ind ≥ ε_Υ; the second lie above
the window, and the first have real part at least Re α_0 + ε_Υ. So along a sequence of applications each of which acts
on a remainder of the previous one, the real parts increase by at least ε_Υ inside a window of length 1 + η_2 − η_1,
and there are at most (1 + η_2 − η_1)/ε_Υ + 1 applications in it.

(e) In each window loop the least real part c_0 of the ι⁺-exponents to be treated starts at least at λ_♯, each window
raises it by at least ε^ι_ind ≥ ε_Υ ([[lem:ec-iota-gap]]; Step 2 of the proof of [[prop:iii-i5-2-1]]), and the loop
ends once c_0 ≥ α^♯_+, where α^♯_+ < 2 (in [[prop:iii-i10-3-1]], once no u-exponent below 2 is left). So there are at
most (2 − λ_♯)/ε_Υ + 1 windows.

(f) Each round of [[prop:iii-i5-2-1]] raises α′_K to min(α′_K + a_K − 2, α_K), from α′_K > 1 to α_K < 2; so there are
at most (α_K − 1)/(a_K − 2) + 1 < N_b rounds. Each step of [[prop:iii-i2-5-1]] raises α′_K by min(a_K − 2, α_K −
α′_K), from α′_K ≥ ½ to α_K < 3/2; so there are at most 1/(a_K − 2) + 1 < N_b + 1 steps. ∎

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

**Proposition {#prop:ec-upper}** (An upper bound for the accounted loss.) In the setting of [[lem:ec-counts]], with s >
½(α − 4) and with the background terms charged by [[lem:ec-split-loss]],

    d_acc ≤ (ℓ_tf + 2)(T_< + T_> + C_2) + 4(1/ι + 2) + r_ι W (N_< + N_> + N_b + 3)
            + Σ_(k=1)^K c(β_k) + N_b c_b + (N_b + 1) c′_b + c_0,                                        {#eq:ec-upper}

where C_2 := N_>((1 + η_2 − η_1)/ε_Υ + 2) and r_ι := d^max_ι + 2 + 2⌈ℓ_I − 5/2⌉. If s ≥ σ_0, ι ≥ ι_0 and a_K − 2 ≥ σ_0
for some σ_0 ∈ (0, 1] and ι_0 > 0, then

    N_< ≤ 1/σ_0,     N_> ≤ (1 + ε_K)/σ_0 + 1,     N_b ≤ 1/σ_0 + 1,     T_< ≤ (1 + σ_0/2)²/(2σ_0ι_0) + 1/σ_0,
    T_> ≤ (1 + ε_K + σ_0/2)²/(2σ_0ι_0) + 2(1 + ε_K)/σ_0 + 2.                                       {#eq:ec-upper-counts}

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

*The second kind.* Along a chain the charges other than those of the counted iterations are, by the definitions above,
at most Σ_k c(β_k) over the level steps, c_b per round of [[prop:iii-i5-2-1]] in the base and c′_b per step of
[[prop:iii-i2-5-1]] there, and c_0 for the rest; the background terms, charged 2 among them, add (d_B − 2)_+ once by
[[lem:ec-split-loss]] (c). By [[lem:ec-counts]] (f) this is the second line of [[eq:ec-upper]].

*The first kind.* A level step at β ∈ (2, 3) runs one window loop (Steps 1–2 of the proof of [[lem:iii-i8-3-2]]) and
its transition face rounds, one after another; a level step at β ∈ (3, α] runs one window loop (Step 2 of the proof of
[[prop:iii-i10-3-1]], through [[lem:iii-i13-2-2]]), the applications at level 1, those at level 2 and the level-3
rounds (Steps 2–4 of the proof of [[prop:iii-i11-3-1]], through [[prop:iii-i13-2-1]]). By [[lem:ec-counts]] (d) and
[[lem:ec-round-charges]] (b), a chain passes through at most one application at level 1 and at most (1 + η_2 −
η_1)/ε_Υ + 1 at level 2 in a level step, each charged at most ℓ_tf + 2; this gives C_2(ℓ_tf + 2) over the levels in
(3, α]. By [[lem:ec-counts]] (b), (c) and [[lem:ec-round-charges]] (a) the rounds give at most (ℓ_tf + 2)(T_< + T_>),
plus 2 for each level-3 round at the at most two levels in (4, α], at most 2 · 2(1/ι + 2) in all. The window loops
counted are one per level step, one per round of [[prop:iii-i5-2-1]] in the base, and those of Steps 0 and 2 of the
proof of [[lem:iii-i8-3-1]] and of the level step α_0 → α_1 of [[prop:iii-i8-4-1]] in the base (the choice α_1 − α_0 <
a_K − 2 makes that level step one): at most N_< + N_> + N_b + 3 of them, each of at most W windows charged at most r_ι
([[lem:ec-counts]] (e), [[lem:ec-round-charges]] (c)). This is the first line of [[eq:ec-upper]].

*The counts.* N_< ≤ (3 − α_1)/s ≤ 1/s, as α_1 > 2; N_> ≤ (α − 3)/s + 1 ≤ (1 + ε_K)/s + 1, as α ≤ 4 + ε_K; and N_b ≤
1/(a_K − 2) + 1. For L > 0 the function s ↦ (L + s/2)²/(2s) = L²/(2s) + L/2 + s/8 decreases on (0, 2L], and s < α − 4
≤ ε_K < 2; so the bounds of [[lem:ec-counts]] (b), (c) decrease in s and in ι, which gives [[eq:ec-upper-counts]]. ∎

**Remark {#rem:ec-upper-point}** (The upper bound at the computational point.) At the computational point take ε_Υ =
1.4619·10⁻¹⁰ ([[lem:ec-gauge-gap]]), ε_ind ≥ ε_Υ (so ε_g = ε_Υ), 3 < ℓ_I < 3.5 and δ < 3.5 − ℓ_I (so d^max_ι ≤ 12 and
r_ι ≤ 16), η_2 < ε_+ ≤ 2·10⁻⁸ and θ := 10⁻³, and suppose that the gap condition (G) of [[def:iii-i10-1-3]] holds with
ε_K = 1.46·10⁻¹⁰. As the admissible values are dense, one may take α − 4 ≥ (1 − θ)ε_K, levels with s ≥ (1 − θ)(α − 4) >
½(α − 4), a_K − 2 ≥ (1 − θ)(α − 4) and ε ≤ θε_g; then [[eq:ec-upper-counts]] holds with σ_0 = (1 − θ)²ε_K and ι_0 =
(1 − θ)ε_Υ, and exact arithmetic gives

    T_< ≤ 2.3497·10¹⁹,     T_> ≤ 2.3497·10¹⁹,     C_2 ≤ 4.6946·10¹⁹,     W ≤ 3.3525·10⁹,
    N_< + N_> ≤ 1.3727·10¹⁰,     N_b ≤ 6.864·10⁹,

so that [[eq:ec-upper]] reads

    d_acc ≤ 9.394·10¹⁹ ℓ_tf + 1.2923·10²¹ + 1.3727·10¹⁰ max_k c(β_k)
            + 6.864·10⁹ (c_b + c′_b) + c′_b + c_0 + (d_B − 2)_+.

The coefficient of ℓ_tf, 9.394·10¹⁹, and the constant 1.2923·10²¹ (of which 1.10·10²¹ comes from the window loops at
ι⁺, through the bound ε^ι_ind ≥ ε_Υ) are the explicit part. Against the lower bound 3R > 1.403·10²⁰ of [[thm:loss-d]]
(ii), the explicit part at ℓ_tf = 1 is 1.386·10²¹, about 9.9 times larger. The remaining terms are finite losses of
single steps multiplied by at most 1.38·10¹⁰.

**Remark {#rem:ec-upper-open}** (What the upper bound leaves open.) Four inputs separate [[prop:ec-upper]] from an
integer. (1) ε_K: (G) asks ε_K below the least distance above 2 and above 3 of the set Λ of [[def:iii-i10-1-1]], whose
generators and increments this paper bounds only by their least real parts; [[prop:gap-sums]] gives that distance for
the part of Λ generated by the class roots, more than 5.019·10⁻⁸, but not for the rest, so no lower bound for the
admissible ε_K, and with it no upper bound for the number of levels, follows from the statements of this paper. (2)
ℓ_tf: [[lem:ec-closed-forms]] (d) gives ℓ_tf in closed form in the orders of the proof of [[cor:iii-f1-3-4]], whose
regularity s is taken large and whose incoming order exceeds a threshold computed in a fibre inner product that this
paper does not fix; ℓ_tf ≥ 1 is proved, no value. (3) The single-step losses c(β), c_b, c′_b and c_0: each is a finite
composition of the elementary losses of [[lem:ec-closed-forms]] and [[rem:ec-other-losses]] and of the forward loss
d_F ≤ 20,180 ([[thm:fwd-loss]]), charged at each forward solution they apply, but their step counts and the counts
n(E, β) of the index sets entering [[eq:ec-fourier-loss]] are not evaluated here; c_0 contains, besides, the
iterations of Steps 4′ and 4 at the top level, each bounded as in [[lem:ec-counts]], and the loss of
[[thm:iii-j-2-4]], which its proof takes as the sum of the losses of its steps over the exponents of Λ ∩ {Re < 3 +
ε_+}, a number of steps not evaluated here. (4) d_B, the background order in [[lem:iii-j2-2-1]] (b), fixed by the
product estimates there and not evaluated. An upper bound for N_NM needs besides upper bounds for the losses of
[[lem:iii-k-2-2]] and [[prop:iii-j2-4-3]], which enter d_NM; their proofs fix them through the loss of
[[thm:iii-j-2-4]] and the product orders of [[lem:iii-j2-2-4]], not evaluated here. Given ε_K, the bound
[[eq:ec-upper]] is of the order 1/(ε_Kε_g), the order of the lower bound of [[prop:ec-rounds]]; ℓ_tf multiplies terms
of that order, and the losses of (3) and (4) enter at most about 3/ε_K times.
