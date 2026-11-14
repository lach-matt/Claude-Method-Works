### The exponents of the index sets at the computational point {#sec:is}

This section carries out, at the computational point of [[def:ec-point]], the constructions that fix the index sets of
[[sec:uc-index-sets]], keeping the exponents. It lists the exponents of real part at most 5 of ℰ_ind
([[prop:is-ind]]), of ℰ^ι_ind ([[prop:is-iota]]), of the least ℰ^C_I and of the least ℰ_++ ([[prop:is-ci-pp]]), with
bounds for their logarithmic orders ([[prop:is-logs]]), and the multiplicities of the indicial roots of L̂_b(0)
([[prop:is-mult]]): this is the statement (IS) of [[rem:uc-missing]]. From these it determines Λ ∩ {Re ≤ 3 + ε_+}
([[prop:is-lambda]]); it shows that (G) holds exactly for ε_K < μ_G, where

    1.64160217197·10⁻¹⁴ < μ_G < 1.64160217198·10⁻¹⁴                                                   {#eq:is-mu}

([[thm:is-gap]]); and it gives 1.6206·10¹³ < N_Λ < 1.6748·10¹³, k̄_0 = 3 and J_* = 15,000,015 ([[prop:is-count]]).
Finally it decides how far ℰ_ind can be made smaller ([[thm:is-d0]]): an admissible ℰ_ind that omits 𝔡₀ exists if and
only if one explicit family of coefficients c_b vanishes at every b near b₀; c_b vanishes at b₀, at every
non-rotating b and on the image of ad_(A(b)), and this paper does not determine it elsewhere. If c_b vanishes, (G)
holds for every ε_K < 5.0190·10⁻⁸, so for every ε_K that [[eq:iii-i9-1-1]] allows ([[cor:is-flat]]).

Throughout, z = 4·10⁻⁶ = 1/250000, h = 10⁻⁶, λ_♯ = 15099/10000, and ε_+ < δ̄ = 1.94137057·10⁻⁸ ([[def:ec-point]],
[[eq:iii-i9-1-1]]). An index set *as constructed* is the one that the lemma cited in the construction returns when its
rule is applied as stated; for [[lem:iii-a-1-4]] this is the set E = ⋃_k E_k there, and for [[lem:iii-a-1-5]] the set E
there. An index set containing it serves in every membership that the construction asserts. For an index set X and
w ∈ ℂ we write k(X, w) for the logarithmic order of X at w, and ℓ̂_X(w) := k(X, w) + 1 if w ∈ π_1X, ℓ̂_X(w) := 0
otherwise.

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
being the largest, as (u + 1)/(u(2u + 1)) decreases; d₂ < d₁ is [[prop:np-10-52]] (i).

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

*Proof.* *Each construction.* By [[lem:is-roots]] (a), every root of real part above a weight α ∈ (−ε_Υ, 2) is in R,
and E(α) = R + ℕ₀ for every α ∈ [0, ι^Υ_(s1,2)); in (F1), [[lem:iii-f3-2-1]] and the step u₂ of [[lem:iii-d3-2-1]] the
weights lie there. By [[eq:is-l1]], π_1E = (π_1F + ℕ₀) ∪ (R + ℕ₀) in (F1) and [[lem:iii-f3-2-1]], and in
[[lem:iii-d3-2-1]] the solution u₀ + χ_∂u₁ + u₂ has the exponents m, those of ℱ₁ + ℕ₀ (u₁, by [[lem:iii-a-1-5]]), and
those of (𝒢 + ℕ₀) ∪ (R + ℕ₀) with 𝒢 ⊂ π_1ℱ₁ + ℕ₀ (u₂). So every exponent of a construction at leading order m is m + j,
an exponent of its right side plus j, or r + j (r ∈ R, j ∈ ℕ₀). The right sides: in (c1), (c3), (c4), the first step
of (1) and the first step of each class, they are smooth with exponents m + ℕ₀ (ρ⁴C^∞, ρ³C^∞, ρ³C^∞ and ρ^(μ+4)C^∞
divided by ρ²); in (c2), m + ℕ₀ and E_(c1) − 1; at a later step at the order m, the exponents of the step before minus 1
(the term A₁, which raises the order by one, divided by ρ²) and of the step two before (A₂ ∈ ρ²C^∞, divided by ρ²),
together with m + ℕ₀ (u₀ and A − N(A)). Relative to its own leading order a later step inherits the exponents of the
earlier steps relative to theirs, shifted by 0 or by an integer, as the leading orders differ by integers. Hence every
offset z − m is a non-negative integer or r − m′ + j with r ∈ R, j ∈ ℕ₀ and m′ the leading order of a first step: 2,
1 or μ + 2 with μ a class root, or the integer leading orders of the first steps of the integer classes. As
r − m′ + j = r − 2 + (j + 2 − m′) for integer m′ ≤ 2, and the non-integer μ + 2 are the elements of M* ∖ {2}
(μ_s0 + 2 = 1 − 𝔡₀, μ_(1,0) + 2 = 1 − 𝔡₁, μ_(1,1) + 2 = −δ′₁, μ_(2,0) + 2 = −δ₂, μ_(2,1) + 2 = −1 − d₁(2),
μ_(3,0) + 2 = −1 − d₂(3), μ_(3,1) + 2 = −2 − d₁(3)), π_1ℰ_ind ⊂ [[eq:is-ind]].

*Equality.* (c1) contains every r ∈ R with its translates, so π_1ℰ_ind ⊃ (R − 2) + ℕ₀; the first step of the class μ,
at m = μ + 2, contains R + ℕ₀ (u₂), so π_1ℰ_ind ⊃ (R − m) + ℕ₀ for m ∈ M* ∖ {2}; and the integers: (1, 0) + 2 lies in
E_(c1) at the root 3 with logarithmic order 2 ([[prop:is-logs]]), so (1, 2) ∈ ℰ_ind. All of this holds at every b, as
the roots do not depend on b.

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

at 2 + 𝔡₁ the count is ℓ̂_F(2 + 𝔡₁) + ℓ̂_F(1 + 𝔡₁) + 1 = 2 + 1 + 1, so k = 3, and likewise at 2 + 𝔡₀; at 2 + δ′₁ and
2 + δ₂, ℓ̂_F = 1 and no root lies at or below, so k = 0. The classes: at m = 1 − 𝔡₀ the exponent 2 + 𝔡₀ comes from u₂
alone, with no term of 𝒢 ⊂ {Re ≥ 3} below it, so k = 0; the same at 2 + 𝔡₁ for m = 1 − 𝔡₀ and m = 1 − 𝔡₁. At the
integer offset 1 of a step at m ≤ 0 the exponent m + 1 comes from u₁ alone; for the class first steps with m ∈ {0, −1,
−2} this gives at most ord(m + 1) ≤ 1, and for the later steps the order is that of the step before at offset 1 plus
ord(m + 1) ≤ 1, which along a chain of at most three later steps starting from order 0 gives at most 3. So the largest
order at real part at most 3/2 is 3, at 1, 1 + 𝔡₁ and 1 + 𝔡₀, and (a) follows, the other exponents of [[eq:is-low]]
having order 0.

(b) *A step bound.* Let a step of [[lem:iii-d3-2-1]] at the order m have a right side of order at most K at offsets of
real part at most t ≤ 5. By [[lem:is-count]] (b), u₁ has order at most K + ⌊t⌋ + 1 there, as a ladder of length at
most t carries at most ⌊t⌋ + 1 roots. u₂ has exponents only at real part at least 2 + 𝔡₁, and by [[eq:is-l1]] at most
p(K + ⌊t⌋ + 2) + p′ − 1, with p ≤ ⌊m + t⌋ − 2 the number of terms of 𝒢 ⊂ {Re ≥ 3} and p′ ≤ ⌊m + t − 2⌋ + 1 that of
E(α) on the ladder below. For m ≤ −2 this is p ≤ 1 (only the exponent 3) and p′ ≤ 1, so the step has order at most
K + ⌊t⌋ + 2 ≤ K + 7. For a first step (K = 0) it is at most 11 at m ∈ (0, 1], t ≤ 3, at most 5 at m ∈ (−1, 0], t ≤ 3,
and at most 31 at t ≤ 5.

*The chains.* (c1), (c3), (c4): 2j ≤ 10 and j + (j − 1)₊ ≤ 9. (c2): j² + 3j − 1 ≤ 39 at j ≤ 5, the value 39 at 6 = 1 + 5.
The first steps of (5): at most 31. The s1 tower: the step k = 2 inherits from the boost at offsets t − 2 ≤ 3, of order
at most 17, and from the translation at t − 4 ≤ 1, so it has order at most 24; then 31 and 38. The s0 tower: the first
step has order at most 11 at offsets ≤ 3, which the step k = 2 inherits at t − 2, so 18, 25, 32. The v1 tower: the
rotation correction at offsets ≤ 2 has order at most 4, inherited at t − 3, so 11, 18, 25. The class companions inherit
the first step at offsets ≤ 3 (at most 11), so at most 18, 25, 32. All are at most 39.

(c) ℰ^ι_ind collects the index sets of the states of [[ch:s13]] and [[ch:s15]], 2 + ℕ₀ and (2, 1) ([[thm:iii-g2-4-2]]).
The states of [[ch:s13]] and ġ^Υ_b are the constructions above. The physical states of [[prop:iii-f4-5-1]], relative to
−2: h^(−2)_b − χh̄ has the offsets 1 (from (−1, 0), order 0) and 1 + (offsets of h̆²_(b,s1), h̆¹_(b,v1)), each at least
2; h′_(b,1) from (0, 0) by [[lem:iii-a-1-5]] (order at most 3 at offsets ≤ 5, the roots of L̂_b(0) on [0, 3] being 0,
2, 3); h_(b,(0)) from the exponent 0 of order k₀ ≤ 2 (the order of h̆²_(b,s1) and h̆¹_(b,v1) at the exponent 0, which
comes from the first step of the s1 and v1 towers at offset 1, at most 2), so of order at most 5; and u_b, by
[[lem:iii-a-1-4]] with E(α) the roots of L̂_b(0) of positive real part and F the exponents of positive real part of the
other terms. At an exponent w of real part at most 3 at most three terms w, w − 1, w − 2 of positive real part enter
[[eq:is-l1]], each of F of order at most 15 (h̆²_(b,s1) at offsets ≤ 4: the boost at offsets ≤ 2, order 9, and the
step k = 2 of the s1 tower at offsets ≤ 4, order at most 9 + 6) and of E(α) of order 0; so u_b has order at most
3·16 + 3 − 1 = 50. At real part at most 3/2 (relative to −2: offsets ≤ 3/2) only the offset 1, of order 0, occurs. The
exponents ι + 1 of [[prop:is-iota]] carry no term of F on their ladder, since ι is non-real or a real number more than
2.93·10⁻⁶ from ℤ, while every exponent of F is real and within 1.34·10⁻⁶ of ℤ ([[lem:is-roots]] (b): the exponents of
the s1 and v1 towers and of h_(b,(0)) are integers plus at most one of 𝔡₀, d₂(l), d₁(l)); and at most two terms of E(α)
of real part greater than 1 lie on their ladder below real part 3, so their order is at most 1. ∎

#### The other index sets {#sec:is-others}

**Proposition {#prop:is-iota}** (The exponents of ℰ^ι_ind.) Let Z be the set of the roots ι of C (with ι > 2), of
P_l (l ≥ 1, Re ι > 19/10, ι ≠ 2) and of p_(v) (l ≥ 2, the larger root) of [[prop:np-10-12]] at (v, e, h) =
(1/2, 1/102400, 10⁻⁶). The exponents of ℰ^ι_ind of real part at most 5, as constructed, are those of ℰ_ind except
𝔡₀ + d₁(3) + 4 and 𝔡₁ + d₁(3) + 4 (from the class μ_(3,1), which no row of [[def:iii-g2-table-1-1]] uses), together
with the integers 1, …, 5 and the numbers ι + 1 + j of real part at most 5 (ι ∈ Z, j ∈ ℕ₀). Every ι ∈ Z has real
part greater than 2; no ι ∈ Z of real part at most 6 is an integer, and every real one has distance from ℤ greater
than 2.93·10⁻⁶. At b₀ the physical states have types s2, v2 and t2 only, and the numbers ι + 1
that they meet are those of the three roots of P₂ in (2 + 2.93h, 2 + 2.94h), (2 + 8h, a(8h)) and (a(8h), 3 − δ_C) of
[[lem:s14-sextic-small]] (b), and of the root (250002000009)^(1/2) − 499999 = 3.0000090… of p_(v) at l = 2.

*Proof.* The states entering [[thm:iii-g2-4-2]] are those of [[def:iii-g2-table-1-1]] and the s1 and v1 terms; their
index sets are those of [[sec:is-ind]], except the rows outside the window (μ_(3,1) − 1 + … below −3). The physical
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

**Proposition {#prop:is-mult}** (The multiplicities of the roots of L̂_b(0).) Every indicial root of L̂_b(0) of real
part in [−101, 5] is a simple root of each type at which it occurs, so N(L̂_b(0), ·)⁻¹ has at most simple poles on that
strip. The roots of real part below −101 are the ι^C_(·,≪) − 1 and the gauge roots −l, 1 − l, 2 − l, 2 − ι^Υ of large
degree; this paper does not decide their multiplicities at h = 10⁻⁶ ((C2)–(C3) of [[sec:iii-f1-1]] are proved for
h ∈ 𝖧, which does not contain 10⁻⁶).

*Proof.* By [[prop:iii-f1-2-3]] (list and proof) the roots of each type are, with multiplicity, −l, l + 2, the roots of
(□^Υ_b)^(0) plus 1 and the roots of □^C_b minus 1, less those of D. Those from □^Υ_b and the integers are distinct
within each type (the disjoint intervals of the proof of (e) there). The roots ι^C − 1 of real part at most 5 that
come from □^C_b are ι − 1, ι ∈ Z, as by [[prop:np-10-54]] (i) the other roots of C, P_l and p_(v) have real part below
−100. Each ι ∈ Z is a simple root of its polynomial: of C, as the other two roots have real part below −100; of P_l, as
the three roots in |ι| < 1000 lie in disjoint sets and are all of them, counted with multiplicity
([[lem:s14-sextic-small]], [[lem:s14-sextic-large]], [[lem:s14-sextic-count]] (a)); of p_(v), as its two roots are
real and of opposite signs. So ι − 1 is simple unless it equals an entry from □^Υ_b or an integer entry of its type.
The integer entries are excluded as ι ∉ ℤ ([[prop:is-iota]]). An entry from □^Υ_b is real and either an integer or
within 1.34·10⁻⁶ of ℤ ([[lem:is-roots]] (b)), while a real ι − 1 is more than 2.93·10⁻⁶ from ℤ. ∎

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
holds as the least element is 2. With n/2 + c the sum of n elements of T′, 1 + n/2 + c ≤ 5 forces n ≤ 8; below 3.02
only n = 2, 3 and 4 with c = 0 occur, since n = 4 gives 3 + c and the least non-zero c is a. Listing σ^(2), σ^(3) in
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
p𝔡₀ + q𝔡₁ − y, p, q ∈ ℕ₀. Put N := ⌊y/𝔡₁⌋ and M := ⌊4y/𝔡₀⌋, and assume y/𝔡₁, 4y/𝔡₀ ∉ ℤ. For an integer n with
M < n ≤ N put θ_n := y − n𝔡₁ and p_n := ⌊θ_n/ε₀⌋ + 1. Then

    m(y) = min({(N + 1)𝔡₁ − y} ∪ {p_n𝔡₀ + (n − 4p_n)𝔡₁ − y : M < n ≤ N, 4p_n ≤ n}),

each element of the second set lying in (0, ε₀] and the first above (N + 1 − y/𝔡₁)𝔡₁.

*Proof.* For p, q ∈ ℕ₀ put n := 4p + q; then p𝔡₀ + q𝔡₁ = n𝔡₁ + pε₀ with 0 ≤ p ≤ n/4, and every pair n, p with these
bounds occurs. Fix n. If n𝔡₁ > y, the least value above y is n𝔡₁ − y (p = 0), least for n = N + 1. If n𝔡₁ ≤ y, that
is n ≤ N, the values exceed y exactly when pε₀ > θ_n ≥ 0, that is p ≥ p_n, and such a p with 4p ≤ n exists exactly
when 4p_n ≤ n; the least value is then p_nε₀ − θ_n ∈ (0, ε₀]. If 4p_n ≤ n, then θ_n < p_nε₀ ≤ nε₀/4, so
y < n(𝔡₁ + ε₀/4) = n𝔡₀/4 and n > M. ∎

**Theorem {#thm:is-gap}** (The admissible ε_K.) For Λ of [[prop:is-lambda]] (ℰ_ind and ℰ^ι_ind as constructed), (G)
of [[def:iii-i10-1-3]] holds if and only if ε_K < μ_G, where

    μ_G := λ_♯ + 1109655𝔡₀ + 31682𝔡₁ − 3

satisfies [[eq:is-mu]]. The next smallest excesses are 2.3181480·10⁻¹⁴ (above 3, from λ_♯ + 1 + δ′₁) and
8.0959353·10⁻¹⁴ (from λ_♯ + 1 + δ₂); every other element of Λ ∪ (Λ + 𝔡₀) ∪ (Λ + 𝔡₁) lies outside (2, 2 + 4.2·10⁻¹³]
∪ (3, 3 + 4.2·10⁻¹³]. As μ_G < δ_50 = ε_ind, the other conditions of [[def:iii-i10-1-3]] on ε_K leave every
ε_K ∈ (0, μ_G) available for a suitable ε_+, and ε_K = 1.6416·10⁻¹⁴ is admissible.

*Proof.* *The windows.* By [[prop:is-lambda]] every element of Λ below 3 + 10⁻⁸ is β + p𝔡₀ + q𝔡₁ with β ∈ ℬ. As 𝔡₀ and
𝔡₁ are increments, Λ + 𝔡₀ and Λ + 𝔡₁ lie in Λ, so the third window of (G) is contained in the first. An element in
(2, 2 + ε] with ε < 𝔡₁ has β ∈ {λ_♯, 2}, and β = 2 gives excess 0 or at least 𝔡₁; so β = λ_♯, with excess
p𝔡₀ + q𝔡₁ − y, y = 2 − λ_♯ = 0.4901. An element in (3, 3 + ε]
with β ∈ {2, 3} has excess at least 𝔡₁ unless p = q = 0, when it is 2 or 3; with β = 2 + c, c ≠ 0, excess
p𝔡₀ + q𝔡₁ − (1 − c); with β = 5/2 + c, p𝔡₀ + q𝔡₁ − (1/2 − c); with β = λ_♯, y = 1.4901; with β = λ_♯ + 1 + δ′₁ or
λ_♯ + 1 + δ₂, y = 0.4901 − δ′₁ or 0.4901 − δ₂. So the least excess is the least m(y) over the 28 numbers y = 1 − c
(c ∈ σ^(2)), 1/2 − c (c ∈ σ^(3)), 1.4901, 0.4901 − δ′₁ and 0.4901 − δ₂ (1/2 − a = 0.4901 being the target near 2
also).

*The values.* The table gives, for each y, N = ⌊y/𝔡₁⌋, the fractional part "frac" of y/𝔡₁ rounded to four digits,
M = ⌊4y/𝔡₀⌋, all the integers n with M < n ≤ N, p = p_n, q = n − 4p ≥ 0, and bounds for p𝔡₀ + q𝔡₁ − y; each entry
follows from [[lem:is-offsets]] (b) by multiplying the bounds exactly. In every row y/𝔡₁ and 4y/𝔡₀ are at distance
more than 0.01 from ℤ, the bounds for θ_n/ε₀ lie strictly between p − 1 and p, and the printed excess lies in (0, ε₀);
by [[lem:is-reduction]] it is the least excess with that n.

| y | N | frac | M | n | p | q | p𝔡₀ + q𝔡₁ − y |
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

The candidate with p = 0 gives (N + 1)𝔡₁ − y ≥ (0.99995 − frac)𝔡₁ ≥ 0.1505·𝔡₁ > 5.01·10⁻⁸ in every row. The three
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
ε_K < μ_G. Finally μ_G < 1.95·10⁻⁸ < δ_50 by [[lem:s14-delta50]], and ε_+ may be taken in (ε_K, δ_50). ∎

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
numbers 3 − β are 1.4901, 1 − c (c ∈ σ^(2), c ≠ 0, and c = 0) and 1/2 − c (c ∈ σ^(3)), with
Σ (3 − β)² = 14.40589434 and Σ (3 − β) = 17.832; by [[lem:is-offsets]] (b), 1/(2𝔡₀𝔡₁) = 1125001468750.4…. So
N_Λ ≥ 14.40589434·1125001468750.4 > 1.62066·10¹³. For the upper bound, ε_+ + 𝔡₀ + 𝔡₁ < 1.69·10⁻⁶ =: κ₀, the two
irrational β contribute at most 2(0.4901 + κ₀)²/(2𝔡₀𝔡₁), and β = 3 contributes T(ε_+) = 1, as ε_+ < 𝔡₁; so
N_Λ ≤ (14.40589434 + 2κ₀·17.832 + 26κ₀² + 2(0.4901 + κ₀)²)·1125001468750.5 + 1 < 1.67472·10¹³.

(b) By [[def:iii-i10-1-1]], k̄_0 bounds the orders of ℰ⁰_src ∪ ℰ_++ ∪ 𝒢 ∪ (2 + ℰ_col) below 2λ_♯ = 3.0198. There,
ℰ⁰_src is 𝒢 together with ℰ_rows ∩ {Re < 2} ⊂ ℰ_++ (the parts involving ℰ_+ lie above 2λ_♯, (H1)); 𝒢 = (2, 0) ∪
(2 + ℰ_ind) has order 3 at 3 = 2 + 1 ([[prop:is-logs]] (a)) and at most 3 elsewhere below 3.0198, as the exponents of
ℰ_ind below 1.0198 are those of [[eq:is-low]] below it; 2 + ℰ_col = (2 + ({(0, 0), (1, 0)} ∪ ℰ_ind ∪ (1 + ℰ_ind))) + ℕ₀
has the same orders; ℰ_++ has orders at most 3, with 3 at λ_♯ + 1 ([[prop:is-ci-pp]] (b)).

(c) The least real part of π_1(ℰ_ind ∪ ℰ^ι_ind) ∪ {1} is 𝔡₁ ([[eq:is-low]], [[prop:is-iota]]). By the row y = 1 of the
table, 1/𝔡₁ = 3000002.583…, so 5/𝔡₁ = 15000012.91…, whose ceiling is 15000013. ∎

[[lem:uc-fourier-count]] bounded J_* through η_0 ≥ ε_Υ; with η_0 = 𝔡₁ the bound becomes J_* = 15,000,015.

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
m ≤ 1 give offsets 2 + 𝔡₀ − m ≥ 1 + 𝔡₀. The rotation corrections have no scalar type 0 term at 2 + 𝔡₀
([[lem:is-rot-s0]]). At b = (m, 0) the projections onto the types apply: ω̇_b(0, Ȧ) is of vector type 1
([[prop:iii-f3-2-2]] (4) at b₀, and at (m, 0) the same argument), and so is every correction of a construction of one
type; the exponents below 3/2 then come from the translations (s1: 𝔡₁, 1 + δ′₁), ω̇_b(0, ·) (v1: 1), the boosts
(s1: 1 + 𝔡₁), ω̇_b(1, 0) and the time translation tower (s0: 1 + 𝔡₀), and the class roots μ_s0 and μ_(1,0) (1 + 2𝔡₀,
1 + 2𝔡₁); at b = (m, 0) the rotations are Killing and have no correction.

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
(b). At a rotating b, c_b(Ȧ) for Ȧ ∈ ker ad_A is the pairing of η_b(0, Ȧ) with the element of the cokernel of P_b at a
weight in (2 + 𝔡₀, 3) that the scalar type 0 root carries, a global quantity that no statement of this paper evaluates;
the symmetry above makes X ↦ c_b(X) a linear form whose dual vector lies in ker ad_A, and imposes no more. ∎

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
[3, 3 + ε_+); the first 28 are pairwise disjoint by [[lem:is-offsets]] (c); the sums with and without the last two
give the bounds. ∎

#### What is determined {#sec:is-summary}

**Remark {#rem:is-summary}** (What (IS) gives and what it leaves.) At the computational point, for the index sets as
constructed: the exponents of real part at most 5 are [[eq:is-ind]] and [[prop:is-iota]], [[prop:is-ci-pp]]; the
logarithmic orders there are at most 39 for ℰ_ind (attained), 50 for ℰ^ι_ind and 0 for the least ℰ^C_I; the roots of
L̂_b(0) of real part in [−101, 5] are simple. So the part of l_* that (IS) fixes is at most 50, and (G), N_Λ, k̄_0 and
J_* are [[thm:is-gap]] and [[prop:is-count]]. Three things are not determined by this paper. (1) The orders of the poles
of N_ι⁺(L̄, ·)⁻¹, statement (SP) of [[rem:uc-missing]]; l_* depends on them. (2) The multiplicities at h = 10⁻⁶ of the
roots of L̂_b(0) of real part below −101 ([[prop:is-mult]]); no construction of this paper meets them. (3) The
coefficient c_b of [[def:is-cb]] at a rotating b; it decides whether ε_K may be taken up to μ♭ ([[cor:is-flat]]) or
only below μ_G ([[thm:is-gap]]). The individual roots ι ∈ Z of [[prop:is-iota]] are fixed by the polynomials of
[[prop:np-10-12]] and located by [[sec:s14-pa]]; they lie above 3 as exponents of ℰ^ι_ind and do not enter Λ below
3 + ε_+.
