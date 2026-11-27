## Appendix. The certified approximant {#app:approximant}

This appendix defines the explicit metric ĝ that serves as the background of the continuation argument of
[[sec:tl5-beyond]], states and proves the procedure by which its residual is bounded, and records the bounds obtained.
The coefficients of ĝ are not printed. They are defined by an exactly specified rule ([[sec:appc-rule]]): a finite
sequence of operations on integers, each stated with its rounding, so that every correct execution of it gives the same
integers. [[sec:appc-digest]] fixes a canonical form of these integers and a digest of it, and [[sec:appc-spot]] gives
the digests and values at which an execution of the rule can be checked. The paper thus contains the complete
definition of the approximant, though not its coefficients. A reader who carries out the rule, and has the formulas of
[[ch:ten-l5]] and of this appendix and any arithmetic of intervals with exact rational end points, can repeat every
step.

The metric is defined at each seed of [[def:tl5-seeds]] on one of two regions,

    D_A := [−10, −2] × [1/2, 7/2],      D* := [−10, −11/10] × [1/2, 7/2],                              {#eq:appc-regions}

in the coordinates (u, v), times S³. The cases are named by the seed and the region: (1, D_A), (2, D*) and (1, D*); the
case (2, D_A) is defined in the same way, and the approximant of (2, D*) serves on D_A as well. Everything below is
stated for a case; the seed enters through the constant λ̂ of the rule and through the targets.

### The approximant {#sec:appc-definition}

We use the chart of [[def:tl5-chart]] in the u-direction, ξ := arsinh((u + 1)/a) with a = 1/500, and v itself. The
region D_A is [ξ₀, ξ_A] × [1/2, 7/2] in (ξ, v), with ξ₀ := −arsinh 4500 and ξ_A := −arsinh 500, and D* is
[ξ₀, ξ*] × [1/2, 7/2] with ξ* := −arsinh 50; here ξ₀ = −9.10498…, ξ_A = −6.90776… and ξ* = −4.60527….

**Definition {#def:appc-layout}** (Elements.) A layout consists of integers n_ξ, n_v ≥ 1, rational numbers
c₁ < … < c_(n_ξ−1) and d > 0 (the breakpoints in ξ and the half-width of their transitions), rational numbers
c′₁ < … < c′_(n_v−1) and d′ > 0 (the same in v), and for every i ≤ n_ξ and j ≤ n_v rational numbers m_i, h_i, m′_j,
h′_j > 0. Element (i, j) is the box

    B_ij := [m_i − h_i, m_i + h_i] × [m′_j − h′_j, m′_j + h′_j]   in (ξ, v),
    t := (ξ − m_i)/h_i,   σ := (v − m′_j)/h′_j,                                                        {#eq:appc-element}

so that (t, σ) ∈ [−1, 1]² on B_ij. With c₀ − d := ξ₀ and c_(n_ξ) + d the upper end of the region in ξ, and likewise
c′₀ − d′ := 1/2 and c′_(n_v) + d′ := 7/2, the use interval of the element is

    U_ij := [c_(i−1) − d, c_i + d] × [c′_(j−1) − d′, c′_j + d′].

The layout is admissible if c_i + d < c_(i+1) − d and c′_j + d′ < c′_(j+1) − d′ for all i and j, and if for every
element U_ij lies in [α_i, m_i + (9/10)h_i] × [α′_j, m′_j + (9/10)h′_j], where α_i := m_i − (9/10)h_i for i ≥ 2,
α₁ := m₁ − h₁, and likewise α′_j := m′_j − (9/10)h′_j for j ≥ 2 and α′₁ := m′₁ − h′₁.

So each element is used only on the inner nine tenths of its box in t and σ, except at the two characteristic edges
ξ = ξ₀ (u = −10) and v = 1/2, where the first boxes begin and are used up to their ends.

**Definition {#def:appc-layouts}** (The layouts.) In every case n_v = 2, c′₁ = 2, d′ = 3/80, and the v-boxes are
[1/2, 21231/10000] and [18769/10000, 7171/2000]. The ξ-parameters are:

    case        n_ξ   breakpoints c_i     d        ξ-boxes [m_i − h_i, m_i + h_i]
    (1, D_A)    2     −801/100            11/200   [−1821/200, −7891/1000], [−813/100, −3421/500]
    (2, D_A)    2     −801/100            11/200   [−1821/200, −7891/1000], [−813/100, −3421/500]
    (2, D*)     2     −343/50             14/125   [−1821/200, −827/125], [−1421/200, −4473/1000]
    (1, D*)     3     −761/100, −611/100  3/40     [−1821/200, −7447/1000], [−7777/1000, −5943/1000],
                                                   [−6273/1000, −4517/1000]

The first ξ-box of every case begins at −1821/200, 2.02 × 10⁻⁵ below ξ₀ = −9.104979…. In u the ξ-boxes of D_A are
[−10.000, −3.673] and [−4.395, −1.936] to three decimals; those of the second seed on D* are [−10.000, −1.747] and
[−2.218, −1.088], and those of the first seed on D* are [−10.000, −2.715], [−3.385, −1.381] and [−1.530, −1.092]. At
u = −10 and v = 1/2 the boxes begin at the edge of the region (the first ξ-box 2 × 10⁻⁴ before it in u); at the other
edges they extend beyond the region by about one twentieth of their length, and the approximant is only required to be
small in the region. Each layout is admissible, as the numbers show.

**Definition {#def:appc-pou}** (The partition of unity.) Let

    Φ(s) := 0 for s ≤ 0,   Φ(s) := e^(−1/s)/(e^(−1/s) + e^(−1/(1−s))) for 0 < s < 1,   Φ(s) := 1 for s ≥ 1,

and for a layout put Φ_i(ξ) := Φ((ξ − c_i + d)/(2d)) for 1 ≤ i ≤ n_ξ − 1, Φ₀ := 1 and Φ_(n_ξ) := 0, and

    χ_i := Φ_(i−1) − Φ_i  (1 ≤ i ≤ n_ξ),      ψ_j := Φ′_(j−1) − Φ′_j  (1 ≤ j ≤ n_v),                   {#eq:appc-pou}

where Φ′_j(v) := Φ((v − c′_j + d′)/(2d′)), Φ′₀ := 1 and Φ′_(n_v) := 0.

**Lemma {#lem:appc-pou}** (Properties of the partition.) (a) Φ is smooth on ℝ, 0 ≤ Φ ≤ 1, Φ(s) + Φ(1 − s) = 1, and
sup |Φ^(k)| ≤ φ_k with (φ₀, …, φ₆) = (1, 2, 9.853, 111.3, 2345, 8.527 × 10⁴, 7.565 × 10⁶). (b) For an admissible
layout the χ_i and ψ_j are smooth, nonnegative, Σ_i χ_i = 1 and Σ_j ψ_j = 1; χ_i vanishes outside [c_(i−1) − d,
c_i + d], equals 1 on [c_(i−1) + d, c_i − d], and on [c_i − d, c_i + d] the only nonzero ones are χ_i = 1 − Φ_i and
χ_(i+1) = Φ_i. The same holds for the ψ_j.

*Proof.* (a) e^(−1/s) is smooth on ℝ when extended by 0 for s ≤ 0, with all derivatives vanishing at 0; the
denominator is positive on ℝ since the two terms do not vanish together; so Φ is smooth, and the stated values outside
(0, 1) agree with the formula's limits. The symmetry is immediate from the formula. For the bounds, by the symmetry it
suffices to take s ∈ (0, 1/2]. On [1/100, 1/2], cover the interval by 20,000 equal closed intervals and enclose the
Taylor coefficients of order at most 6 of Φ on each by the rules of [[def:tl5-jets]] (series of order 6), the
exponential and the reciprocal being applied to series whose constant term is an interval; the largest end points,
times k!, are at most φ_k. On (0, 1/100] use Cauchy's estimate on the disc |z − s| ≤ s/2: there Re(1/z) ≥ 2/(3s),
since inversion maps the disc onto the disc with diameter [2/(3s), 2/s], and Re(1/(1 − z)) ≤ 1/(1 − 3s/2),
so |Φ(z)| ≤ e^(−2/(3s))/(e^(−1/(1−3/200)) − e^(−2/(3s))) and |Φ^(k)(s)| ≤ k!(2/s)^k sup |Φ|, which at s = 1/100 is far
below φ_k and increases in s on (0, 1/100]. (b) The Φ_i are nonincreasing in i at each point, because the transitions
are disjoint by admissibility, and the sums telescope. The supports follow from those of the Φ_i. ∎

**Definition {#def:appc-approximant}** (The approximant.) For each element (i, j) and each F ∈ {R, m, n, W, s} the
rule of [[sec:appc-rule]] gives an integer p = p_(ij,F) and integers z_abk = z^(ij,F)_abk for (a, b, k) in a finite set
I_(ij,F) of triples of nonnegative integers. Put

    G^F_ij(t, σ, x) := Σ_((a,b,k) ∈ I_(ij,F)) z_abk 10^(−p) T_a(t) T_b(σ) T_k(x)                        {#eq:appc-fields}

with t and σ the variables of [[eq:appc-element]] on B_ij, and

    R := R_s + (v − 1/2)^κ Σ_ij χ_i ψ_j G^R_ij,      W := W_s + (v − 1/2)^κ Σ_ij χ_i ψ_j G^W_ij,
    F := (v − 1/2)^κ Σ_ij χ_i ψ_j G^F_ij   (F ∈ {m, n, s}),                                           {#eq:appc-seedform}

where R_s and W_s are the seed's R and W of [[lem:tl5-seed]] and κ = 4 is the order of contact with the seed on N₀
([[rem:appc-contact]]). The approximant ĝ of the case is the metric
[[eq:tl5-metric]] with these fields, P := (2(1 + x)m − (1 − x)n)/3, Q := (2(1 − x)n − (1 + x)m)/3 and b = (1 − x²)s.

Each term of the sum is defined where χ_iψ_j ≠ 0, which is inside B_ij by [[lem:appc-pou]] (b), so the fields are
defined on the region and on a neighbourhood of it in the union of the boxes.

**Lemma {#lem:appc-approximant}** (Properties of ĝ.) Let ĝ be the approximant of a case, and suppose R > 0 on
an open set 𝒪 ⊂ ⋃ B_ij containing the region. Then:

(a) ĝ is a smooth Lorentzian metric of the class on 𝒪 × S³, in double-null form, invariant under the T² action and
under the reflections φ1 ↦ −φ1 and φ2 ↦ −φ2;

(b) on N₀ = {v = 1/2}, each of the five fields and its partial derivatives of all orders in u and x, and of order at
most κ − 1 in v, take the values of the seed: R − R_s, W − W_s, m, n and s vanish to order κ at v = 1/2;

(c) the coefficients are exact rational numbers, and ĝ and all its derivatives are given by finitely many arithmetic
operations, exponentials and the seed's R_s from these numbers.

*Proof.* (a) The fields are smooth on 𝒪, since the seed's are ([[lem:tl5-seed]] (b)), the polynomials are, and so
are χ_i, ψ_j and the chart. The metric of the class with smooth fields and R > 0 is smooth on 𝒪 × S³, axes included,
because 2P + Q = (1 + x)m and P + 2Q = (1 − x)n vanish at x = −1 and x = 1 and b = (1 − x²)s
([[pending:lem-tl5-cip-axis]]); its form is the double-null form, and the invariances hold for every metric of the
class. (b) Each correction is (v − 1/2)^κ times a smooth function, and m, n, s vanish for the seed. (c) is the
definition. ∎

The form [[eq:appc-seedform]] makes the agreement with the seed's (κ − 1)-jet on N₀ exact, whatever the integers.

**Remark {#rem:appc-contact}** (The order of contact on N₀.) The integer κ ≥ 1 is a parameter of the definition: for
every κ the approximant agrees with the seed on N₀ to order κ − 1 in v, whatever the integers. The rule is
stated for κ = 4. A contact of higher order with a metric other than the seed, as a hypothesis on N₀ may require,
needs a reference part in place of R_s, W_s and the zero functions in [[eq:appc-seedform]] that carries that metric's
v-derivatives on N₀ of the orders between 4 and κ − 1.

### The rule {#sec:appc-rule}

This section defines, for a case, the integers p and z_abk of [[def:appc-approximant]]. The definition is a finite
sequence of operations on integers in which every operation, its rounding and its order are stated, so that its result
does not depend on how it is carried out. The rule follows the characteristic initial value problem of
[[def:tl5-problem]] cell by cell; how close its output is to the solution plays no part in the definition, since
[[sec:appc-certification]] bounds the residual of whatever the rule gives.

#### The arithmetic {#sec:appc-arith}

**Definition {#def:appc-arith}** (The arithmetic of the rule.) Put B := 320 and 𝔽 := 2^(−B) ℤ, the multiples of 2^(−B).
For a real number y let ⌊y⌋_B := 2^(−B) ⌊2^B y⌋, the largest element of 𝔽 not exceeding y, and ⌊y⌋ the largest integer
not exceeding y. A rational number q written in the rule stands for ⌊q⌋_B. For x, y ∈ 𝔽, an integer n ≠ 0 and finite
families a = (a_l), g = (g_l) in 𝔽 of equal length, the rule uses:

    x + y, x − y, n x   (exact),       x ⊙ y := ⌊x y⌋_B,       x ⊘ y := ⌊x/y⌋_B  (y ≠ 0),       x ⊘ n := ⌊x/n⌋_B,
    √x := ⌊√x⌋_B  (x ≥ 0),       ⟨a, g⟩ := ⌊Σ_l a_l g_l⌋_B.                                            {#eq:appc-arith}

In ⟨a, g⟩ the sum is formed exactly and rounded once, so it does not depend on the order of summation. For a matrix
A = (A_rl) with entries in 𝔽 and a family g = (g_(…l…)) with one index l of the same range, A ⋆_l g denotes the family
whose entry with r in place of l is ⟨(A_rl)_l, (g_(…l…))_l⟩. In an expression ⊙ and ⊘ bind equally and more strongly
than + and −, and they are applied from the left: x ⊙ y ⊙ z := (x ⊙ y) ⊙ z and x ⊘ y ⊙ z := (x ⊘ y) ⊙ z. A product
n y with an integer n written before a bracket or a symbol, such as 4 (e₃ ⊙ G) or 2q, is the exact integer multiple. A
minus sign before a single symbol negates it, and −(…) negates the value of the bracket; both are exact. Every other
grouping is shown by brackets.

Negative values are rounded down, not toward zero: ⌊−1/3⌋_B = −⌊1/3⌋_B − 2^(−B).

#### Elementary functions and constants {#sec:appc-functions}

**Definition {#def:appc-functions}** (Elementary functions.) For y ∈ 𝔽:

(a) exp y. Let k ≥ 0 be the least integer with 8|y| ≤ 2^k and z := y ⊘ 2^k. Put E₄₅ := 1 and E_(n−1) := 1 + (z ⊙ E_n) ⊘ n
for n = 45, 44, …, 1; then exp y is the result of k squarings E ↦ E ⊙ E applied to E₀.

(b) sin y and cos y. With k and z as in (a) and u := z ⊙ z, put S₂₂ := 1, S_(j−1) := 1 − (u ⊙ S_j) ⊘ (2j(2j + 1)), and
C₂₂ := 1, C_(j−1) := 1 − (u ⊙ C_j) ⊘ ((2j − 1)2j), for j = 22, 21, …, 1, and (s, c) := (z ⊙ S₀, C₀). Then k times
(s, c) := (2 (s ⊙ c), c ⊙ c − s ⊙ s), both components formed from the previous pair; sin y := s and cos y := c.

(c) log y, for y > 0. Let m be the integer with 2^m ≤ y < 2^(m+1), and w := y ⊘ 2^m (for m ≤ 0 the exact product
2^(−m) y). If w ≥ 3/2, replace w by w ⊘ 2 and m by m + 1. Put t := (w − 1) ⊘ (w + 1), u := t ⊙ t, P₇₀ := 1/141 and
P_j := 1/(2j + 1) + u ⊙ P_(j+1) for j = 69, 68, …, 0. Then log y := m L̂₂ + 2 (t ⊙ P₀), with

    L̂₂ := 2 Σ_(j=0)^(110) ⌊1/((2j + 1) 3^(2j+1))⌋_B.

(d) π̂ := 16 A₅ − 4 A₂₃₉ with A_q := Σ_(j=0)^(J_q) (−1)^j ⌊1/((2j + 1) q^(2j+1))⌋_B, J₅ := 70 and J₂₃₉ := 20.

(e) For integers n ≥ 1 and 0 ≤ j < 2n put ĉ(0, n) := 1, ĉ(n, n) := −1, ĉ(j, n) := cos((j π̂) ⊘ n) for 0 < j < n and
ĉ(j, n) := ĉ(2n − j, n) for n < j < 2n; for other integers j, ĉ(j, n) := ĉ(j′, n) with 0 ≤ j′ < 2n and j′ ≡ j
(mod 2n). It stands for cos(πj/n).

(f) sinh y := (exp y − exp(−y)) ⊘ 2 and cosh y := (exp y + exp(−y)) ⊘ 2.

(g) The constants â := 1/500 (that is, ⌊1/500⌋_B), ξ̂₀ := −log(4500 + √20250001), which stands for −arsinh 4500, and
λ̂ := 1 at the first seed and λ̂ := √(1/10) at the second (that is, √(⌊1/10⌋_B)).

The accuracy of these functions plays no part in the definition.

#### Nodes and matrices {#sec:appc-nodes}

**Definition {#def:appc-nodes}** (Nodes and matrices.) For an integer p ≥ 1 the Lobatto nodes of degree p are
τ^L_j := −ĉ(j, p), and the Radau nodes of degree p are τ^R_j := ĉ(2(p − j), 2p + 1), for j = 0, 1, …, p; both families
increase with j, τ^L_0 = −1, τ^L_p = τ^R_p = 1, and the Radau nodes do not contain −1. For the integer M of the case the
angular nodes are x_k := ĉ(k, M), k = 0, 1, …, M; they decrease, x₀ = 1 and x_M = −1.

For a family τ₀, …, τ_p of distinct elements of 𝔽 let ℓ_j(τ) := Π_(i≠j) (τ − τ_i)/(τ_j − τ_i) be its Lagrange basis.
Its matrices have the entries below; each entry is ⌊e⌋_B of the exact rational number e shown, which the rational
nodes determine:

    Q_ij := ∫_(−1)^(τ_i) ℓ_j(s) ds,     D_ij := ℓ′_j(τ_i),     (QQ)_ij := ⟨(Q_il)_l, (Q_lj)_l⟩,      {#eq:appc-matrices}

the last formed from the rounded entries of Q by [[eq:appc-arith]]. For the Radau family put σ_i := (τ_i + 1)/2 and
λ_j(σ) := ℓ_j(2σ − 1), and

    W_ij := σ_i^(−4) ∫_0^(σ_i) s³ λ_j(s) ds,       V_ij := σ_i^(−4) ∫_0^(σ_i) (σ_i − s) s² λ_j(s) ds.

For the angular family put D¹_kl := ℓ′_l(x_k) and D²_kl := ℓ″_l(x_k). For a point τ ∈ 𝔽, ℓ_j(τ) also denotes ⌊ℓ_j(τ)⌋_B;
where τ is a node τ_i this is 1 for j = i and 0 otherwise. Finally, for an integer N ≥ 1, with ω₀ = ω_N := 1/2 and
ω_n := 1 for 0 < n < N,

    Ĉ^N_na := ⌊2 ω_n ω_a ĉ(n(N − a), N)/N⌋_B,       Ĉ^(x,M)_nk := ⌊2 ω_n ω_k ĉ(nk, M)/M⌋_B   (0 ≤ n, a, k ≤ N or M).

They map values at increasing nodes −ĉ(a, N) and at the angular nodes to Chebyshev coefficients (the discrete cosine
transform of the first kind).

#### The seed at a point {#sec:appc-rule-seed}

**Definition {#def:appc-rule-seed}** (The seed at a point.) For (ξ, v) ∈ 𝔽² put u₁ := â ⊙ sinh ξ, u := u₁ − 1 and

    H := v − 2u + log(u₁ ⊘ (u₁ − 2)).

Let r₀ := 1 + 2^(−32) and r₁ := max(H, 0) ⊘ 2 + 3, and repeat eighty times: q := (r₀ + r₁) ⊘ 2; if
2q + log((q − 1) ⊘ (q + 1)) < H then r₀ := q, otherwise r₁ := q. Then put R := r₀ and repeat six times

    R := R − (2R + log((R − 1) ⊘ (R + 1)) − H) ⊘ (2 + 2 ⊘ (R ⊙ R − 1)).

With f := 1 − 1 ⊘ (R ⊙ R) and g := 1 − 1 ⊘ (u ⊙ u), the seed's values at the point are

    R_s := R,   ∂_vR_s := f ⊘ 2,   ∂_uR_s := −(f ⊘ g),   Ω_s² := f ⊘ (2g),   ∂_vW_s := 1 ⊘ (2 (R ⊙ R ⊙ R)),
    and   u_ξ := â ⊙ cosh ξ.                                                                     {#eq:appc-rule-seed}

These stand for the seed's R, its derivatives and Ω² of [[lem:tl5-seed]] and [[eq:appc-seed-jets]], and for du/dξ.

#### The grid {#sec:appc-grid}

**Definition {#def:appc-grid}** (The grid of cells.) Let n_c, n_r, p_ξ, p_v and the segments be the parameters of the
case ([[sec:appc-parameters]]), and ξ_e and v_e the largest right ends of the ξ-boxes and the v-boxes of its layout
([[def:appc-layouts]]). The breakpoints are

    ξ^(i) := ξ̂₀ + (i (ξ_e − ξ̂₀)) ⊘ n_c  (0 ≤ i ≤ n_c),       v^(j) := 1/2 + (j (v_e − 1/2)) ⊘ n_r  (0 ≤ j ≤ n_r),

and cell (i, j), 0 ≤ i < n_c, 0 ≤ j < n_r, is [ξ^(i), ξ^(i+1)] × [v^(j), v^(j+1)]. A segment is a set of consecutive
columns i; each segment has its own angular degree M and iteration counts N_o, N_i, and a cell takes those of its
segment. In cell (i, j) put h_ξ := (ξ^(i+1) − ξ^(i)) ⊘ 2 and h_v := (v^(j+1) − v^(j)) ⊘ 2, and let its nodes be

    ξ_a := ξ^(i) + h_ξ ⊙ (τ^L_a + 1)  (0 ≤ a ≤ p_ξ),       v_b := v^(j) + h_v ⊙ (τ_b + 1)  (0 ≤ b ≤ p_v),

and x_k (0 ≤ k ≤ M), where τ^L are the Lobatto nodes of degree p_ξ, and τ_b := τ^R_b, the Radau nodes of degree p_v, in
row j = 0 and τ_b := τ^L_b, the Lobatto nodes of degree p_v, in rows j ≥ 1. At each v-node put ε := v_b − 1/2,
e₂ := ε ⊙ ε, e₃ := e₂ ⊙ ε and e₄ := e₃ ⊙ ε, and in rows j ≥ 1 also η := v^(j) − 1/2 and η₄ := η ⊙ η ⊙ η ⊙ η. The
cell's matrices are Q_ξ and D_ξ of the Lobatto family of degree p_ξ; Q_v and D_v of its v-family (Radau in row 0,
Lobatto otherwise); W and V of the Radau family (row 0) and QQ_v of the Lobatto family (rows j ≥ 1), all of degree p_v;
and D¹, D² of the angular family of its M.

The seed's values of [[def:appc-rule-seed]] are taken at each node (ξ_a, v_b) of each cell.

#### The data on N₁ {#sec:appc-rule-data}

**Definition {#def:appc-rule-data}** (The data on the cone u = −10.) In each row j, at each v-node v_b of that row and
each angular node x_k of the first segment, let r, ∂_vW_s be the seed's values R_s, ∂_vW_s at (ξ̂₀, v_b), put
ε, e₂, e₃, e₄ as in [[def:appc-grid]], x := x_k, and

    z := (π̂ ⊙ ε) ⊘ 3,   q₁ := (π̂ ⊘ 3) ⊙ (sin z ⊘ z),   q₂ := q₁ ⊙ q₁,   q₃ := q₂ ⊙ q₁,   q₄ := q₂ ⊙ q₂,
    θ := v_b ⊘ λ̂,   h := √(2 ⊘ (1 + x ⊙ x)),   κ := ((h ⊙ λ̂) ⊘ 2) ⊙ (1 ⊘ (r ⊙ √r)),   f_r := 1 − 1 ⊘ (r ⊙ r),
    G_m := κ ⊙ q₄ ⊙ cos θ,      G_n := κ ⊙ q₄ ⊙ sin θ,
    α₁ := −(((3 f_r) ⊘ 4) ⊘ r ⊙ ε ⊙ q₄),   α₂ := ((4π̂) ⊘ 3) ⊙ q₃ ⊙ cos z,   α₃ := (ε ⊙ q₄) ⊘ λ̂,
    m₃ := κ ⊙ ((α₁ + α₂) ⊙ cos θ − α₃ ⊙ sin θ),      n₃ := κ ⊙ ((α₁ + α₂) ⊙ sin θ + α₃ ⊙ cos θ),
    P₃ := ((2(1 + x)) ⊙ m₃ − (1 − x) ⊙ n₃) ⊘ 3,      Q₃ := ((2(1 − x)) ⊙ n₃ − (1 + x) ⊙ m₃) ⊘ 3,
    σ₆ := P₃ ⊙ P₃ + Q₃ ⊙ Q₃ + (P₃ + Q₃) ⊙ (P₃ + Q₃).                                             {#eq:appc-rule-cone}

(Here ε > 0, since the Radau nodes exclude −1, so z ≠ 0.) In exact arithmetic G_m and G_n are m and n of [[eq:cone-data]]
divided by (v − 1/2)⁴, with env(v) = sin⁴(π(v − 1/2)/3) for every v (also beyond 7/2), and m₃, n₃ are ∂_v m and ∂_v n
divided by (v − 1/2)³; σ₆ (v − 1/2)⁶ is the shear |∂_vP|² + |∂_vQ|² + |∂_v(P + Q)|² of the data. The function G_R of the
row is defined by N_Ray sweeps of the Raychaudhuri equation: starting from

    G_R := 0  (j = 0),       G_R := (η₄ ⊙ Γ_k + (v_b − v^(j)) ⊙ Υ_k) ⊘ e₄  (j ≥ 1),

each sweep forms g := (D_v ⋆_b G_R) ⊙ (1 ⊘ h_v), Δ := 4 (e₃ ⊙ G_R) + e₄ ⊙ g, R_t := r + e₄ ⊙ G_R and

    ρ := 2 (∂_vW_s ⊙ Δ) − (R_t ⊙ σ₆ ⊙ e₄ ⊙ e₂) ⊘ 3,                                                {#eq:appc-rule-ray}

and replaces G_R by V ⋆_b (ρ ⊙ (1 ⊘ e₂)) in row 0 and by (η₄ ⊙ Γ_k + (v_b − v^(j)) ⊙ Υ_k + (h_v ⊙ h_v) ⊙ (QQ_v ⋆_b ρ))
⊘ e₄ in rows j ≥ 1. After the last sweep, with ρ that of the last sweep, the row passes to row j + 1 the values
Γ_k := G_R at b = p_v and Υ_k := Υ′_k + h_v ⊙ ⟨((Q_v)_(p_v b))_b, (ρ_(bk))_b⟩, where Υ′_k is the value Υ_k that the
row received from row j − 1 (Υ′_k := 0 in row 0). The left edge of the cells (0, j) is
(G^R, G^m, G^n, G^W) := (G_R, G_m, G_n, 0) at the nodes (v_b, x_k): W equals the seed's on the cone.

In exact arithmetic the sweep is the Picard iteration of ∂_v² D_R = 2 ∂_vW_s ∂_v D_R − (R_s + D_R) σ₆ (v − 1/2)⁶/3 for
D_R := R − R_s = (v − 1/2)⁴ G_R along the row, the equation of [[eq:cone-raychaudhuri]].

#### The cell problem {#sec:appc-cells}

The unknowns of a cell are the numbers G^F_abk ∈ 𝔽 at its nodes, F ∈ {R, m, n, W, s}; they stand for
(F − F_s)/(v − 1/2)⁴, F_s the seed's field (zero for m, n and s). The cells are treated column by column, from i = 0
upward, and in each column row by row from j = 0 upward. Cell (i, j) receives a left edge L^F_bk (F ≠ s) and, for
j ≥ 1, a lower edge T^F_ak (all F) and lower values s_ak^bot:
- the left edge of cell (0, j) is the data of [[def:appc-rule-data]]; that of cell (i, j), i ≥ 1, is the right edge of
  cell (i − 1, j), resampled by [[def:appc-resample]] when cell (i − 1, j) belongs to another segment;
- the lower edge and the lower values of cell (i, j), j ≥ 1, are the top edge and the top values of cell (i, j − 1).

**Definition {#def:appc-cell}** (The cell map.) Let (i, j) be a cell with the notation of [[def:appc-grid]].

(a) The boundary term. In row 0, B^F_abk := L^F_bk for F ≠ s and B^s_abk := 0. In rows j ≥ 1,

    B^F_abk := (η₄ ⊙ T^F_ak + e₄ ⊙ L^F_bk − η₄ ⊙ T^F_0k) ⊘ e₄   (F ≠ s),
    B^s_abk := (η₄ ⊙ T^s_ak + (v_b − v^(j)) ⊙ s_ak^bot) ⊘ e₄,

with e₄ that of the node v_b.

(b) The jets. For a family G = (G^F_abk) put, for each node (a, b, k),

    G^F_v := (D_v ⋆_b G^F) ⊙ (1 ⊘ h_v),   G^F_ξ := (D_ξ ⋆_a G^F) ⊙ (1 ⊘ h_ξ)  (F = R, m, n),
    G^F_x := D¹ ⋆_k G^F,   G^F_xx := D² ⋆_k G^F  (F ≠ s),   G^F_vx := D¹ ⋆_k G^F_v,

and, with e₃, e₄ of the node v_b and u_ξ of [[eq:appc-rule-seed]] at (ξ_a, v_b),

    D^F := e₄ ⊙ G^F,   D^F_x := e₄ ⊙ G^F_x,   D^F_xx := e₄ ⊙ G^F_xx,   D^F_u := e₄ ⊙ G^F_ξ ⊙ (1 ⊘ u_ξ),
    D^F_v := 4 (e₃ ⊙ G^F) + e₄ ⊙ G^F_v,   D^F_vx := 4 (e₃ ⊙ G^F_x) + e₄ ⊙ G^F_vx,                   {#eq:appc-rule-d}

D^F_xx for F ≠ s and D^F_u for F = R, m, n. With the seed's values at (ξ_a, v_b) and x := x_k, the jets J(G) at the
node are the thirty-one numbers

    R := R_s + D^R,   R⁻¹ := 1 ⊘ R,   e^S := exp S,   e^(−S) := exp(−S),
    with S := (D^m + x ⊙ D^m + D^n − x ⊙ D^n) ⊘ 3,
    Ω² := Ω_s² ⊙ exp(2 D^W),   Ω⁻² := (1 ⊘ Ω_s²) ⊙ exp(−2 D^W),
    R_u := ∂_uR_s + D^R_u,   R_v := ∂_vR_s + D^R_v,   R_x := D^R_x,   R_xx := D^R_xx,   R_vx := D^R_vx,
    W_v := ∂_vW_s + D^W_v,   W_x := D^W_x,   W_xx := D^W_xx,   W_vx := D^W_vx,
    m := D^m,   m_u := D^m_u,   m_v := D^m_v,   m_x := D^m_x,   m_xx := D^m_xx,   m_vx := D^m_vx,
    n, n_u, n_v, n_x, n_xx, n_vx  likewise from D^n,      s := D^s,   s_v := D^s_v,   s_x := D^s_x,   s_vx := D^s_vx.

The names stand for the fields of [[eq:appc-seedform]], their derivatives, 1/R, e^(±S) and Ω^(±2); each is the
number just defined, not an exact value. J_s denotes the jets with every D
equal to 0.

(c) The right-hand side. For jets J and the node's x, the five numbers X(J) = (X_R, X_m, X_n, X_W, X_s) are given by
the following sequence of definitions, read from top to bottom, each line with the conventions of [[def:appc-arith]]: a
product a ⊙ b ⊙ c is (a ⊙ b) ⊙ c, a minus sign before a single symbol negates it, the sums are exact, and every rational
constant q stands for ⌊q⌋_B. The symbols t₀, …, t₂₂₅ and r₁, …, r₅ are local to one evaluation.

    t₀ := Ω⁻² ⊙ s_v
    t₁ := (1/4) ⊙ t₀
    t₂ := Ω⁻² ⊙ s
    t₃ := m_v ⊙ t₂
    t₄ := m_vx ⊙ t₂
    t₅ := (1/2) ⊙ t₀
    t₆ := m ⊙ t₅
    t₇ := Ω⁻² ⊙ s_x
    t₈ := (1/2) ⊙ t₇
    t₉ := m_v ⊙ t₈
    t₁₀ := m_x ⊙ t₅
    t₁₁ := Ω⁻² ⊙ s_vx
    t₁₂ := (1/2) ⊙ t₁₁
    t₁₃ := t₁₂ ⊙ x
    t₁₄ := e^S ⊙ e^S
    t₁₅ := R⁻¹ ⊙ R⁻¹
    t₁₆ := t₁₄ ⊙ t₁₅
    t₁₇ := 4 ⊙ t₁₆
    t₁₈ := W_x ⊙ t₁₇
    t₁₉ := R⁻¹ ⊙ R⁻¹ ⊙ R⁻¹
    t₂₀ := t₁₄ ⊙ t₁₉
    t₂₁ := 2 ⊙ R_x
    t₂₂ := t₂₀ ⊙ t₂₁
    t₂₃ := (32/3) ⊙ t₁₆
    t₂₄ := n_x ⊙ t₂₃
    t₂₅ := (4/3) ⊙ t₁₆
    t₂₆ := m_xx ⊙ t₂₅
    t₂₇ := (8/3) ⊙ t₁₆
    t₂₈ := m ⊙ t₂₇
    t₂₉ := n_xx ⊙ t₂₇
    t₃₀ := m ⊙ m
    t₃₁ := (8/9) ⊙ t₁₆
    t₃₂ := t₃₀ ⊙ t₃₁
    t₃₃ := m_x ⊙ m_x
    t₃₄ := t₃₁ ⊙ t₃₃
    t₃₅ := (16/3) ⊙ t₁₆
    t₃₆ := n ⊙ t₃₅
    t₃₇ := n ⊙ n
    t₃₈ := (32/9) ⊙ t₁₆
    t₃₉ := t₃₇ ⊙ t₃₈
    t₄₀ := n_x ⊙ n_x
    t₄₁ := t₃₈ ⊙ t₄₀
    t₄₂ := x ⊙ x
    t₄₃ := 8 ⊙ t₁₆
    t₄₄ := W_xx ⊙ t₄₃
    t₄₅ := t₄₄ ⊙ x
    t₄₆ := t₄₃ ⊙ (W_x ⊙ W_x)
    t₄₇ := t₄₆ ⊙ x
    t₄₈ := 4 ⊙ t₂₀
    t₄₉ := R_xx ⊙ t₄₈
    t₅₀ := t₄₉ ⊙ x
    t₅₁ := 2 ⊙ x
    t₅₂ := 8 ⊙ t₁₄
    t₅₃ := t₅₂ ⊙ (R_x ⊙ R_x) ⊙ (R⁻¹ ⊙ R⁻¹ ⊙ R⁻¹ ⊙ R⁻¹)
    t₅₄ := t₅₃ ⊙ x
    t₅₅ := (64/9) ⊙ t₁₆
    t₅₆ := n ⊙ n_x
    t₅₇ := t₅₅ ⊙ t₅₆
    t₅₈ := t₂₃ ⊙ t₄₀
    t₅₉ := x ⊙ x ⊙ x
    t₆₀ := W_x ⊙ t₃₆
    t₆₁ := t₃₅ ⊙ x
    t₆₂ := R_x ⊙ t₂₀
    t₆₃ := (8/3) ⊙ t₆₂
    t₆₄ := n ⊙ t₆₃
    t₆₅ := (4/3) ⊙ t₆₂
    t₆₆ := m ⊙ t₆₅
    t₆₇ := m_x ⊙ t₆₅
    t₆₈ := (3/2) ⊙ R⁻¹
    t₆₉ := R_u ⊙ Ω⁻²
    t₇₀ := t₆₈ ⊙ t₆₉
    t₇₁ := R_v ⊙ t₆₈
    t₇₂ := Ω⁻² ⊙ t₇₁
    t₇₃ := R⁻¹ ⊙ t₂
    t₇₄ := R_v ⊙ t₇₃
    t₇₅ := (3/4) ⊙ t₇₄
    t₇₆ := n_x ⊙ t₆₃
    t₇₇ := W_x ⊙ t₃₅
    t₇₈ := n_x ⊙ t₇₇
    t₇₉ := (16/9) ⊙ t₁₆
    t₈₀ := m ⊙ m_x
    t₈₁ := t₇₉ ⊙ t₈₀
    t₈₂ := t₂₄ ⊙ x
    t₈₃ := 16 ⊙ W_x ⊙ t₆₂
    t₈₄ := t₈₃ ⊙ x
    t₈₅ := n ⊙ t₃₈
    t₈₆ := m ⊙ t₈₅
    t₈₇ := t₈₆ ⊙ x
    t₈₈ := n_x ⊙ t₃₈
    t₈₉ := m ⊙ t₈₈
    t₉₀ := t₄₂ ⊙ t₈₉
    t₉₁ := m_x ⊙ t₈₅
    t₉₂ := t₄₂ ⊙ t₉₁
    t₉₃ := m_x ⊙ t₈₈
    t₉₄ := t₅₉ ⊙ t₉₃
    t₉₅ := (16/3) ⊙ t₆₂ ⊙ x
    t₉₆ := R ⊙ R
    t₉₇ := e^(−S) ⊙ e^(−S)
    t₉₈ := Ω⁻² ⊙ Ω⁻²
    t₉₉ := s_v ⊙ s_v
    t₁₀₀ := (1/32) ⊙ t₉₆ ⊙ t₉₇ ⊙ t₉₈ ⊙ t₉₉
    t₁₀₁ := t₁₀₀ ⊙ x
    t₁₀₂ := (3/2) ⊙ t₇₄
    t₁₀₃ := m_x ⊙ t₁₀₂
    t₁₀₄ := t₇ ⊙ t₇₁
    t₁₀₅ := t₁₀₄ ⊙ x
    t₁₀₆ := R_x ⊙ t₆₈
    t₁₀₇ := t₁₀₆ ⊙ t₃
    t₁₀₈ := W_x ⊙ t₂₈
    t₁₀₉ := t₉₃ ⊙ x
    t₁₁₀ := t₅₅ ⊙ x
    t₁₁₁ := (128/9) ⊙ t₁₆ ⊙ x
    t₁₁₂ := t₇₄ ⊙ x
    t₁₁₃ := (3/2) ⊙ t₁₁₂
    t₁₁₄ := W_x ⊙ t₂₇
    t₁₁₅ := m_x ⊙ t₁₁₄
    t₁₁₆ := t₁₁₅ ⊙ t₄₂
    t₁₁₇ := t₁₁₆ − t₁₀₈ − t₁₁₅
    t₁₁₈ := t₄₄ + t₄₆ − t₁₂ − t₅₃
    t₁₁₉ := t₁₀₀ + t₁₁₈ + t₄₉ + t₈₆ + t₉₁ − t₁₀₄ − t₈₃ − t₈₉ − t₉₃ + t₄₂ ⊙ t₉₃
    t₁₂₀ := n_vx ⊙ t₂
    t₁₂₁ := n_v ⊙ t₈
    t₁₂₂ := n_x ⊙ t₅
    t₁₂₃ := n_v ⊙ t₂
    t₁₂₄ := n_xx ⊙ t₂₅
    t₁₂₅ := n ⊙ t₅
    t₁₂₆ := m_xx ⊙ t₂₇
    t₁₂₇ := n ⊙ t₂₇
    t₁₂₈ := t₃₁ ⊙ t₃₇
    t₁₂₉ := t₃₁ ⊙ t₄₀
    t₁₃₀ := m ⊙ t₃₅
    t₁₃₁ := m_x ⊙ t₂₃
    t₁₃₂ := t₃₀ ⊙ t₃₈
    t₁₃₃ := t₃₃ ⊙ t₃₈
    t₁₃₄ := t₅₆ ⊙ t₇₉
    t₁₃₅ := n_x ⊙ t₆₅
    t₁₃₆ := n ⊙ t₆₅
    t₁₃₇ := m ⊙ t₆₃
    t₁₃₈ := m_x ⊙ t₆₃
    t₁₃₉ := W_x ⊙ t₁₃₀
    t₁₄₀ := m_x ⊙ t₇₇
    t₁₄₁ := t₁₃₁ ⊙ x
    t₁₄₂ := t₂₃ ⊙ t₃₃
    t₁₄₃ := t₅₅ ⊙ t₈₀
    t₁₄₄ := n_x ⊙ t₁₀₂
    t₁₄₅ := t₁₀₆ ⊙ t₁₂₃
    t₁₄₆ := W_x ⊙ t₁₂₇
    t₁₄₇ := n_x ⊙ t₁₁₄
    t₁₄₈ := t₁₄₇ ⊙ t₄₂
    t₁₄₉ := t₁₄₆ + t₁₄₈ − t₁₄₇
    t₁₅₀ := t₅ ⊙ x
    t₁₅₁ := n ⊙ t₁₇
    t₁₅₂ := t₁₉ ⊙ t₅₂
    t₁₅₃ := (1/3) ⊙ t₃
    t₁₅₄ := (1/3) ⊙ t₄
    t₁₅₅ := (1/3) ⊙ t₁₂₀
    t₁₅₆ := (1/6) ⊙ t₀
    t₁₅₇ := (1/6) ⊙ t₇
    t₁₅₈ := m_v ⊙ t₁₅₇
    t₁₅₉ := m_x ⊙ t₁₅₆
    t₁₆₀ := n_v ⊙ t₁₅₇
    t₁₆₁ := n_x ⊙ t₁₅₆
    t₁₆₂ := (20/3) ⊙ t₁₆
    t₁₆₃ := (1/2) ⊙ R⁻¹
    t₁₆₄ := t₁₆₃ ⊙ t₆₉
    t₁₆₅ := m_v ⊙ t₁₆₄
    t₁₆₆ := R_v ⊙ Ω⁻² ⊙ t₁₆₃
    t₁₆₇ := m_u ⊙ t₁₆₆
    t₁₆₈ := W_x ⊙ t₄₃ ⊙ x
    t₁₆₉ := t₄₂ ⊙ t₄₆
    t₁₇₀ := R_x ⊙ t₄₈
    t₁₇₁ := m_x ⊙ t₁₇₀
    t₁₇₂ := n_x ⊙ t₁₇₀
    t₁₇₃ := x ⊙ x ⊙ x ⊙ x
    t₁₇₄ := t₁₅₃ ⊙ x
    t₁₇₅ := (1/3) ⊙ t₁₂₃
    t₁₇₆ := t₁₇₅ ⊙ x
    t₁₇₇ := t₁₅₈ ⊙ t₄₂
    t₁₇₈ := t₁₅₈ ⊙ t₅₉
    t₁₇₉ := t₁₆₀ ⊙ x
    t₁₈₀ := t₁₆₀ ⊙ t₄₂
    t₁₈₁ := t₁₅₈ ⊙ x
    t₁₈₂ := t₁₆₀ ⊙ t₅₉
    t₁₈₃ := m_x ⊙ t₁₂₇
    t₁₈₄ := m_x ⊙ t₁₃₀
    t₁₈₅ := R_vx ⊙ t₇₃
    t₁₈₆ := (1/2) ⊙ t₇₄
    t₁₈₇ := n_x ⊙ t₁₈₆
    t₁₈₈ := R_x ⊙ R⁻¹
    t₁₈₉ := (1/2) ⊙ t₁₈₈
    t₁₉₀ := t₁₈₉ ⊙ t₃
    t₁₉₁ := t₁₂₃ ⊙ t₁₈₉
    t₁₉₂ := t₁₀₈ ⊙ t₄₂
    t₁₉₃ := t₁₁₅ ⊙ t₅₉
    t₁₉₄ := t₁₄₇ ⊙ x
    t₁₉₅ := t₁₁₅ ⊙ x
    t₁₉₆ := t₁₄₆ ⊙ t₄₂
    t₁₉₇ := t₁₄₇ ⊙ t₅₉
    t₁₉₈ := n_x ⊙ t₂₈
    t₁₉₉ := n_x ⊙ t₃₆
    t₂₀₀ := t₁₀₀ − (1/32) ⊙ t₄₂ ⊙ t₉₆ ⊙ t₉₇ ⊙ t₉₈ ⊙ t₉₉
    t₂₀₁ := (1/3) ⊙ Ω⁻²
    t₂₀₂ := m_u ⊙ m_v
    t₂₀₃ := t₂₀₁ ⊙ t₂₀₂
    t₂₀₄ := n_u ⊙ n_v ⊙ t₂₀₁
    t₂₀₅ := (1/6) ⊙ Ω⁻²
    t₂₀₆ := (1/6) ⊙ n ⊙ t₃
    t₂₀₇ := (2/3) ⊙ x
    t₂₀₈ := (1/6) ⊙ m ⊙ t₁₂₃
    t₂₀₉ := e^S ⊙ R⁻¹
    t₂₁₀ := (2/3) ⊙ t₂₀₉
    t₂₁₁ := m_vx ⊙ t₂₁₀
    t₂₁₂ := (4/3) ⊙ t₂₀₉
    t₂₁₃ := m_v ⊙ t₂₁₂
    t₂₁₄ := m ⊙ t₂₁₃
    t₂₁₅ := m_x ⊙ t₂₁₃
    t₂₁₆ := m_v ⊙ t₂₁₀
    t₂₁₇ := n ⊙ t₂₁₆
    t₂₁₈ := n_v ⊙ t₂₁₂
    t₂₁₉ := n_x ⊙ t₂₁₈
    t₂₂₀ := e^S ⊙ t₁₅
    t₂₂₁ := n_v ⊙ t₂₁₀
    t₂₂₂ := m_v ⊙ x
    t₂₂₃ := (1/12) ⊙ R ⊙ e^(−S) ⊙ t₀
    t₂₂₄ := t₂₁ ⊙ t₂₂₀
    t₂₂₅ := m_v ⊙ t₂₂₄
    r₁ := t₁ + t₁₀ + t₁₀₃ + t₁₀₅ + t₁₀₇ + t₁₀₉ + t₁₁₇ + t₁₁₉ + t₁₃ + t₂₈ + t₂₉ + t₃ + t₃₂ + t₃₄ + t₃₆ + t₃₉ + t₄
            + t₄₁ + t₅₄ + t₆ + t₇₅ + t₇₆ + t₇₈ + t₈₁ + t₈₂ + t₈₄ + t₉ − t₁₀₁ − t₁₈ − t₂₂ − t₂₄ − t₂₆ − t₄₅ − t₄₇
            − t₅₀ − t₅₇ − t₆₀ − t₆₄ − t₆₆ − t₆₇ − t₈₇ − t₉₀ − t₉₂ − t₉₄ + m ⊙ t₁₀₂ + m_u ⊙ t₇₂ + m_v ⊙ t₇₀
            + m_x ⊙ t₆₁ + t₁₀₈ ⊙ x + t₁₁₁ ⊙ t₅₆ + t₂₆ ⊙ t₄₂ + t₂₉ ⊙ t₄₂ + t₃₄ ⊙ x + t₄₂ ⊙ t₅₈ + t₄₂ ⊙ t₆₇ + t₄₂ ⊙ t₇₆
            + t₄₂ ⊙ t₇₈ + t₆₀ ⊙ x + t₆₄ ⊙ x + t₆₆ ⊙ x − W_x ⊙ t₈₂ − m ⊙ t₁₁₃ − n_x ⊙ t₉₅ − n_xx ⊙ t₆₁ − t₁₀ ⊙ t₄₂
            − t₁₀₃ ⊙ t₄₂ − t₁₀₇ ⊙ t₄₂ − t₃ ⊙ t₅₁ − t₃₂ ⊙ x − t₃₄ ⊙ t₄₂ − t₃₄ ⊙ t₅₉ − t₃₉ ⊙ x − t₄ ⊙ t₄₂ − t₄₁ ⊙ t₅₉
            − t₄₂ ⊙ t₅₇ − t₄₂ ⊙ t₈₁ − t₄₂ ⊙ t₉ − t₅₈ ⊙ x − t₆ ⊙ x + m ⊙ n_x ⊙ t₁₁₀
    r₂ := t₁₀₁ + t₁₁₉ + t₁₂₀ + t₁₂₁ + t₁₂₂ + t₁₂₆ + t₁₂₇ + t₁₂₈ + t₁₂₉ + t₁₃₀ + t₁₃₁ + t₁₃₂ + t₁₃₃ + t₁₃₆ + t₁₃₇
            + t₁₃₈ + t₁₃₉ + t₁₄₀ + t₁₄₁ + t₁₄₃ + t₁₄₄ + t₁₄₅ + t₁₄₉ + t₁₈ + t₂₂ + t₄₅ + t₄₇ + t₅₀ + t₈₇ + t₉₀ + t₉₂
            + t₉₄ − t₁ − t₁₀₅ − t₁₀₉ − t₁₂₃ − t₁₂₄ − t₁₂₅ − t₁₃ − t₁₃₄ − t₁₃₅ − t₅₄ − t₇₅ − t₈₄ + W_x ⊙ t₁₄₁
            + m_x ⊙ t₉₅ + m_xx ⊙ t₆₁ + n_u ⊙ t₇₂ + n_v ⊙ t₇₀ + n_x ⊙ t₆₁ + t₁₁₁ ⊙ t₈₀ + t₁₂₄ ⊙ t₄₂ + t₁₂₆ ⊙ t₄₂
            + t₁₂₈ ⊙ x + t₁₂₉ ⊙ t₅₉ + t₁₃₂ ⊙ x + t₁₃₃ ⊙ t₅₉ + t₁₃₄ ⊙ t₄₂ + t₁₃₅ ⊙ t₄₂ + t₁₃₆ ⊙ x + t₁₃₇ ⊙ x
            + t₁₃₈ ⊙ t₄₂ + t₁₃₉ ⊙ x + t₁₄₀ ⊙ t₄₂ + t₁₄₂ ⊙ t₄₂ + t₁₄₂ ⊙ x + t₁₄₃ ⊙ t₄₂ + t₁₄₆ ⊙ x − n ⊙ t₁₀₂
            − n ⊙ t₁₁₃ − t₁₂₀ ⊙ t₄₂ − t₁₂₁ ⊙ t₄₂ − t₁₂₂ ⊙ t₄₂ − t₁₂₃ ⊙ t₅₁ − t₁₂₅ ⊙ x − t₁₂₉ ⊙ t₄₂ − t₁₂₉ ⊙ x
            − t₁₄₄ ⊙ t₄₂ − t₁₄₅ ⊙ t₄₂ + m_x ⊙ n ⊙ t₁₁₀
    r₃ := t₁₁₆ + t₁₄₆ + t₁₄₈ + t₁₆₈ + t₁₆₉ + t₁₇₄ + t₁₇₆ + t₁₇₇ + t₁₇₈ + t₁₇₉ + t₁₈₀ + t₁₉₂ + t₁₉₃ + t₁₉₄ − t₁₀₈
            − t₁₁₅ − t₁₁₈ − t₁₂₄ − t₁₄₇ − t₁₅₀ − t₁₅₁ − t₁₅₃ − t₁₅₄ − t₁₅₅ − t₁₅₈ − t₁₅₉ − t₁₆₀ − t₁₆₁ − t₁₆₅ − t₁₆₇
            − t₁₇₁ − t₁₇₂ − t₁₈₁ − t₁₈₂ − t₁₈₃ − t₁₈₄ − t₁₈₇ − t₁₉₀ − t₁₉₁ − t₁₉₅ − t₁₉₆ − t₁₉₇ − t₂₀₀ − t₂₆
            − (5/2) ⊙ t₁₁₂ − R_xx ⊙ t₁₅₂ − m ⊙ t₁₅₆ − m ⊙ t₁₇ − m ⊙ t₁₇₀ − m ⊙ t₁₈₆ − m_x ⊙ t₁₆₂ − m_x ⊙ t₁₈₆
            − n ⊙ t₂₈ − n_u ⊙ t₁₆₆ − n_v ⊙ t₁₆₄ − t₁₂ ⊙ t₄₂ − t₁₂₄ ⊙ t₅₉ − t₁₅₁ ⊙ x − t₁₅₄ ⊙ x − t₁₅₅ ⊙ t₅₉
            − t₁₅₉ ⊙ x − t₁₆₁ ⊙ t₅₉ − t₁₆₅ ⊙ x − t₁₆₇ ⊙ x − t₁₇₁ ⊙ x − t₁₇₂ ⊙ t₅₉ − t₁₈₃ ⊙ x − t₁₈₄ ⊙ x − t₁₈₅ ⊙ t₄₂
            − t₁₈₇ ⊙ t₅₉ − t₁₉₀ ⊙ x − t₁₉₁ ⊙ t₅₉ − t₁₉₈ ⊙ t₄₂ − t₁₉₈ ⊙ x − t₁₉₉ ⊙ t₄₂ − t₁₉₉ ⊙ x − t₂₆ ⊙ x
            − t₂₇ ⊙ t₃₀ − t₂₇ ⊙ t₃₃ − t₂₇ ⊙ t₃₇ − t₂₇ ⊙ t₄₀ − t₃₃ ⊙ t₆₁ − t₄₂ ⊙ t₅₃ + 2 ⊙ t₁₄ ⊙ t₁₅
            − (2/3) ⊙ t₁₂₃ ⊙ t₄₂ − (1/2) ⊙ m_x ⊙ t₁₁₂ − n ⊙ t₁₅₆ ⊙ t₄₂ − n ⊙ t₁₇₀ ⊙ t₄₂ − n ⊙ t₁₈₆ ⊙ t₄₂
            − n_x ⊙ t₁₆₂ ⊙ t₄₂ − t₁₈₈ ⊙ t₄₂ ⊙ t₅ − t₃₅ ⊙ t₄₀ ⊙ t₅₉ + (1/3) ⊙ Ω⁻² ⊙ n_v ⊙ s + (1/6) ⊙ Ω⁻² ⊙ n ⊙ s_v
            + (20/3) ⊙ n_x ⊙ t₁₄ ⊙ t₁₅ + R_vx ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s + (1/2) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s_v
            − R_x ⊙ W_x ⊙ t₁₅₂ ⊙ t₄₂ − m_x ⊙ n_x ⊙ t₃₅ ⊙ t₄₂ − 2 ⊙ R_v ⊙ R⁻¹ ⊙ t₄₂ ⊙ t₇ + 2 ⊙ R_u ⊙ R_v ⊙ Ω⁻² ⊙ t₁₅
            + 2 ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s_x + 4 ⊙ R_x ⊙ n ⊙ t₁₄ ⊙ t₁₉ + 4 ⊙ m ⊙ t₁₄ ⊙ t₁₅ ⊙ x + 8 ⊙ R_x ⊙ W_x ⊙ t₁₄ ⊙ t₁₉
            + 8 ⊙ R_xx ⊙ t₁₄ ⊙ t₁₉ ⊙ t₄₂ + 8 ⊙ W_xx ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂ + 12 ⊙ R_x ⊙ t₁₄ ⊙ t₁₉ ⊙ x
            + (1/3) ⊙ Ω⁻² ⊙ m_vx ⊙ s ⊙ t₄₂ + (1/3) ⊙ Ω⁻² ⊙ m_vx ⊙ s ⊙ t₅₉ + (1/3) ⊙ Ω⁻² ⊙ n_vx ⊙ s ⊙ t₄₂
            + (1/3) ⊙ Ω⁻² ⊙ n_vx ⊙ s ⊙ x + (1/6) ⊙ Ω⁻² ⊙ m ⊙ s_v ⊙ t₄₂ + (1/6) ⊙ Ω⁻² ⊙ m_x ⊙ s_v ⊙ t₄₂
            + (1/6) ⊙ Ω⁻² ⊙ m_x ⊙ s_v ⊙ t₅₉ + (1/6) ⊙ Ω⁻² ⊙ n_x ⊙ s_v ⊙ t₄₂ + (1/6) ⊙ Ω⁻² ⊙ n_x ⊙ s_v ⊙ x
            + (2/3) ⊙ Ω⁻² ⊙ m_v ⊙ s ⊙ t₄₂ + (4/3) ⊙ m_xx ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂ + (4/3) ⊙ m_xx ⊙ t₁₄ ⊙ t₁₅ ⊙ t₅₉
            + (4/3) ⊙ n_xx ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂ + (4/3) ⊙ n_xx ⊙ t₁₄ ⊙ t₁₅ ⊙ x + (8/3) ⊙ m ⊙ n_x ⊙ t₁₄ ⊙ t₁₅
            + (8/3) ⊙ m_x ⊙ n_x ⊙ t₁₄ ⊙ t₁₅ + (8/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₁₇₃ ⊙ t₃₃ + (8/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₁₇₃ ⊙ t₄₀
            + (8/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₃₀ ⊙ t₄₂ + (8/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₃₇ ⊙ t₄₂ + (16/3) ⊙ n ⊙ n_x ⊙ t₁₄ ⊙ t₁₅
            + (16/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₃₃ ⊙ t₅₉ + (16/3) ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₀ ⊙ x + (20/3) ⊙ m_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂
            + (1/2) ⊙ R_u ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_v ⊙ x + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n ⊙ s + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_u ⊙ x
            − R_v ⊙ t₁₅ ⊙ t₂ ⊙ t₂₁ ⊙ t₄₂ + 2 ⊙ R_v ⊙ R_x ⊙ Ω⁻² ⊙ s ⊙ t₁₅ + 4 ⊙ R_x ⊙ m ⊙ t₁₄ ⊙ t₁₉ ⊙ t₄₂
            + 4 ⊙ R_x ⊙ m_x ⊙ t₁₄ ⊙ t₁₉ ⊙ t₄₂ + 4 ⊙ R_x ⊙ m_x ⊙ t₁₄ ⊙ t₁₉ ⊙ t₅₉ + 4 ⊙ R_x ⊙ n_x ⊙ t₁₄ ⊙ t₁₉ ⊙ t₄₂
            + 4 ⊙ R_x ⊙ n_x ⊙ t₁₄ ⊙ t₁₉ ⊙ x + (8/3) ⊙ m ⊙ n ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂ + (8/3) ⊙ m ⊙ n_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₅₉
            + (8/3) ⊙ m_x ⊙ n ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂ + (8/3) ⊙ m_x ⊙ n ⊙ t₁₄ ⊙ t₁₅ ⊙ t₅₉
            + (8/3) ⊙ m_x ⊙ n_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₁₇₃ + (16/3) ⊙ m ⊙ m_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₄₂
            + (16/3) ⊙ m ⊙ m_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₅₉ + (16/3) ⊙ n ⊙ n_x ⊙ t₁₄ ⊙ t₁₅ ⊙ t₅₉
            + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ m ⊙ s ⊙ t₄₂ + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ m_x ⊙ s ⊙ t₄₂
            + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ m_x ⊙ s ⊙ t₅₉ + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_x ⊙ s ⊙ t₄₂
            + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_x ⊙ s ⊙ x + (1/2) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ m_v ⊙ s ⊙ t₄₂
            + (1/2) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ m_v ⊙ s ⊙ t₅₉ + (1/2) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_v ⊙ s ⊙ t₄₂
            + (1/2) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ n_v ⊙ s ⊙ x
    r₄ := t₁₅₀ + t₁₅₈ + t₁₆₀ + t₁₈₁ + t₁₈₂ + t₁₉₅ + t₁₉₆ + t₁₉₇ + t₄₆ − t₁₁₇ − t₁₄₉ − t₁₆₈ − t₁₆₉ − t₁₇₄ − t₁₇₆
            − t₁₇₇ − t₁₇₈ − t₁₇₉ − t₁₈₀ − t₁₉₂ − t₁₉₃ − t₁₉₄ − t₂₀₀ − t₂₀₃ − t₂₀₄ − t₂₀₆ − (3/2) ⊙ t₁₈₅ − (1/4) ⊙ t₁₁
            − (1/4) ⊙ t₃ − W_vx ⊙ t₂ − W_x ⊙ t₅ − m ⊙ t₁₅₃ − m ⊙ t₁₇₄ − m_x ⊙ t₁₅₃ − n ⊙ t₁₇₆ − n_x ⊙ t₁₇₅
            − t₂₀₃ ⊙ t₄₂ − t₂₀₄ ⊙ t₄₂ − t₂₀₆ ⊙ x − t₂₀₈ ⊙ t₄₂ − t₂₀₈ ⊙ x − (3/4) ⊙ t₀ ⊙ t₁₈₈ − (1/12) ⊙ t₃ ⊙ t₄₂
            − R_v ⊙ R⁻¹ ⊙ t₈ − W_x ⊙ t₁₇₀ ⊙ t₄₂ − W_xx ⊙ t₁₇ ⊙ t₄₂ − Ω⁻² ⊙ t₂₀₂ ⊙ t₂₀₇ − m_x ⊙ t₁₇₅ ⊙ t₄₂
            − m_x ⊙ t₂₀₇ ⊙ t₃ − n ⊙ t₁₇₅ ⊙ t₄₂ − n_x ⊙ t₁₅₃ ⊙ t₄₂ + 4 ⊙ W_xx ⊙ t₁₄ ⊙ t₁₅ − (2/3) ⊙ n_x ⊙ t₁₂₃ ⊙ t₅₉
            + (1/4) ⊙ Ω⁻² ⊙ n_v ⊙ s + (1/4) ⊙ Ω⁻² ⊙ s_vx ⊙ t₄₂ + (1/6) ⊙ Ω⁻² ⊙ m_u ⊙ n_v + (1/6) ⊙ Ω⁻² ⊙ m_v ⊙ n_u
            + W_vx ⊙ Ω⁻² ⊙ s ⊙ t₄₂ + (1/2) ⊙ W_x ⊙ Ω⁻² ⊙ s_v ⊙ t₄₂ − m_u ⊙ n_v ⊙ t₂₀₅ ⊙ t₄₂ − m_v ⊙ n_u ⊙ t₂₀₅ ⊙ t₄₂
            + 4 ⊙ R_x ⊙ W_x ⊙ t₁₄ ⊙ t₁₉ + (1/3) ⊙ Ω⁻² ⊙ n ⊙ n_v ⊙ s + (1/6) ⊙ Ω⁻² ⊙ m ⊙ n_v ⊙ s
            + (1/6) ⊙ Ω⁻² ⊙ m_v ⊙ n_x ⊙ s + (1/6) ⊙ Ω⁻² ⊙ m_x ⊙ n_v ⊙ s + (1/12) ⊙ Ω⁻² ⊙ n_v ⊙ s ⊙ t₄₂
            + (2/3) ⊙ Ω⁻² ⊙ n_u ⊙ n_v ⊙ x + R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s ⊙ x + (1/2) ⊙ R_v ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s_x ⊙ t₄₂
            + (1/3) ⊙ Ω⁻² ⊙ m ⊙ m_v ⊙ s ⊙ t₄₂ + (1/3) ⊙ Ω⁻² ⊙ m ⊙ m_v ⊙ s ⊙ t₅₉ + (1/3) ⊙ Ω⁻² ⊙ m_v ⊙ m_x ⊙ s ⊙ t₁₇₃
            + (1/3) ⊙ Ω⁻² ⊙ n ⊙ n_v ⊙ s ⊙ t₅₉ + (1/3) ⊙ Ω⁻² ⊙ n_v ⊙ n_x ⊙ s ⊙ t₁₇₃ + (1/6) ⊙ Ω⁻² ⊙ m ⊙ n_v ⊙ s ⊙ t₅₉
            + (1/6) ⊙ Ω⁻² ⊙ m_v ⊙ n ⊙ s ⊙ t₄₂ + (1/6) ⊙ Ω⁻² ⊙ m_v ⊙ n ⊙ s ⊙ t₅₉ + (1/6) ⊙ Ω⁻² ⊙ m_v ⊙ n_x ⊙ s ⊙ t₁₇₃
            + (1/6) ⊙ Ω⁻² ⊙ m_x ⊙ n_v ⊙ s ⊙ t₁₇₃ + (2/3) ⊙ Ω⁻² ⊙ m_v ⊙ m_x ⊙ s ⊙ t₅₉
            + (2/3) ⊙ Ω⁻² ⊙ n_v ⊙ n_x ⊙ s ⊙ x + (3/2) ⊙ R_vx ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s ⊙ t₄₂
            + (3/4) ⊙ R_x ⊙ Ω⁻² ⊙ R⁻¹ ⊙ s_v ⊙ t₄₂
    r₅ := −t₂₁₁ − t₂₁₄ − t₂₁₅ − t₂₁₇ − t₂₁₉ − t₂₂₅ − m_v ⊙ t₂₂₃ − n_v ⊙ t₂₂₃ − n_v ⊙ t₂₂₄ − n_vx ⊙ t₂₁₀ − t₂₁₁ ⊙ x
            − t₂₁₄ ⊙ x − t₂₁₅ ⊙ t₄₂ − t₂₁₇ ⊙ x − t₂₁₉ ⊙ t₄₂ − t₂₂₂ ⊙ t₂₂₃ − t₂₂₅ ⊙ x − 4 ⊙ R_vx ⊙ t₂₂₀
            − 2 ⊙ W_vx ⊙ t₂₀₉ − (5/3) ⊙ m_v ⊙ t₂₀₉ − m ⊙ t₂₂₁ ⊙ x − m_x ⊙ t₂₂₁ ⊙ t₄₂ − n ⊙ t₂₁₈ ⊙ x
            − n_x ⊙ t₂₁₆ ⊙ t₄₂ − (8/3) ⊙ m_x ⊙ t₂₀₉ ⊙ t₂₂₂ + (5/3) ⊙ e^S ⊙ R⁻¹ ⊙ n_v − R ⊙ W_v ⊙ e^(−S) ⊙ t₁
            + 4 ⊙ e^S ⊙ R_v ⊙ R_x ⊙ t₁₉ + 6 ⊙ e^S ⊙ R_v ⊙ W_x ⊙ t₁₅ + (2/3) ⊙ e^S ⊙ R⁻¹ ⊙ m ⊙ n_v
            + (2/3) ⊙ e^S ⊙ R⁻¹ ⊙ m_v ⊙ n_x + (2/3) ⊙ e^S ⊙ R⁻¹ ⊙ m_x ⊙ n_v + (2/3) ⊙ e^S ⊙ R⁻¹ ⊙ n_vx ⊙ x
            + (4/3) ⊙ e^S ⊙ R⁻¹ ⊙ n ⊙ n_v + (5/8) ⊙ R_v ⊙ e^(−S) ⊙ Ω⁻² ⊙ s_v + 2 ⊙ e^S ⊙ R_x ⊙ n_v ⊙ t₁₅ ⊙ x
            + (8/3) ⊙ e^S ⊙ R⁻¹ ⊙ n_v ⊙ n_x ⊙ x + (1/12) ⊙ R ⊙ e^(−S) ⊙ Ω⁻² ⊙ n_v ⊙ s_v ⊙ x
    X_m := −(Ω² ⊙ r₁)
    X_n := −(Ω² ⊙ r₂)
    X_R := R ⊙ ((1 + x) ⊙ X_m ⊙ (1/3) + (1 − x) ⊙ X_n ⊙ (1/3) − Ω² ⊙ r₃)
    X_W := Ω² ⊙ r₄ − (3/2) ⊙ R⁻¹ ⊙ X_R
    X_s := −(8 ⊙ e^S ⊙ Ω² ⊙ R⁻¹ ⊙ r₅)                    {#eq:appc-rhs}

The outputs are X_R, X_m, X_n, X_W and X_s; they stand for ∂_u∂_vR, ∂_u∂_vm, ∂_u∂_vn, ∂_u∂_vW and ∂_v²s
([[rem:appc-rhs-origin]]).
(d) The map. For a family G put, at each node, with J := J(G) and u_ξ at (ξ_a, v_b),

    Ψ^F := u_ξ ⊙ (X_F(J) − X_F(J_s))   (F = R, m, n, W),       Φ := X_s(J) − X_s(J_s),

and define I(G) by

    row 0:        I^F := h_ξ ⊙ (Q_ξ ⋆_a (W ⋆_b (Ψ^F ⊙ (1 ⊘ e₃)))),      I^s := V ⋆_b (Φ ⊙ (1 ⊘ e₂)),
    rows j ≥ 1:   I^F := (h_ξ ⊙ h_v ⊙ (Q_ξ ⋆_a (Q_v ⋆_b Ψ^F))) ⊘ e₄,     I^s := (h_v ⊙ h_v ⊙ (QQ_v ⋆_b Φ)) ⊘ e₄,
                                                                                                      {#eq:appc-rule-int}

for F = R, m, n, W, the factors e₂, e₃, e₄ being those of the node v_b of the entry. The cell map is
P(G) := B + I(G).

(e) The edges. When the cell's values G are fixed ([[def:appc-iteration]]), its right edge is G^F_(p_ξ b k) for
F = R, m, n, W, its top edge is G^F_(a p_v k) for all F, and its top values are

    s_ak^top := s_ak^bot + h_v ⊙ ⟨((Q_v)_(p_v b))_b, (Φ_abk)_b⟩,

with s^bot := 0 in row 0 and Φ that of the last evaluation of P in [[def:appc-iteration]].

In exact arithmetic I is the Goursat integration of the cell: the double integral of Ψ in ξ and v and the double integral
of Φ in v, in the form that divides nothing by (v − 1/2)⁴ near N₀, since W and V are the operators
q ↦ σ⁻⁴ ∫_0^σ s³ q and φ ↦ σ⁻⁴ ∫_0^σ (σ − s) s² φ on the interpolating polynomials. A fixed point of P solves the
collocation equations of the cell, and B carries the data of its left and lower edges.

**Remark {#rem:appc-rhs-origin}** (What the sequence evaluates.) In exact arithmetic, with exact jets of a metric of the
class, X_R, X_m, X_n, X_W and X_s are the values of ∂_u∂_vR, ∂_u∂_vm, ∂_u∂_vn, ∂_u∂_vW and ∂_v²s determined by the five
equations f̃_11 − f̃_xx = 0, f̃_22 − f̃_xx = 0, f̃_xx = 0, f̃_ln = 0 and f̃_lx = 0 of [[eq:appc-regular]], the first two
divided by 1 + x and 1 − x, which divide them as polynomials [[pending:appc-evolution-identity]]. This is why a fixed
point of the cell maps approximates the solution of the characteristic problem. Neither the definition of ĝ nor its
certificate uses it.

#### The iteration in a cell {#sec:appc-iteration}

The fixed point of P is approached by outer steps: each forms the defect of P in 𝔽 and corrects it by sweeps of the
linearised map in a short arithmetic whose rounding is relative.

**Definition {#def:appc-short}** (The short arithmetic.) Let 𝔻 be the set of the numbers 0 and ±m 2^e with integers
1 ≤ m < 2^53 and −1074 ≤ e ≤ 971. Each nonzero element of 𝔻 has exactly one such form with 2^52 ≤ m < 2^53, or with
e = −1074 and m < 2^52; m is its mantissa. For a real number y with |y| ≤ (2^53 − 1) 2^971, rd y is the element of 𝔻
nearest to y, and of two equally near the one with even mantissa; rd y is not defined for larger |y|. For x, y ∈ 𝔻 and
finite families a, g in 𝔻 of equal length n,

    x ⊕ y := rd(x + y),   x ⊖ y := rd(x − y),   x ⊗ y := rd(x y),   x ⊘_𝔻 y := rd(x/y),
    ⟨a, g⟩_𝔻 := ((⋯((a₁ ⊗ g₁) ⊕ (a₂ ⊗ g₂)) ⊕ ⋯) ⊕ (a_n ⊗ g_n)),                                          {#eq:appc-short}

the sum taken in the order of the index; A ⋆^𝔻_l g is formed from ⟨·,·⟩_𝔻 as A ⋆_l g from ⟨·,·⟩. Negation is exact.
A sum of more than two terms written in the rule is formed from the left, in the order written. These are the
operations of the binary64 format of the IEEE standard [[pending:ref-ieee-754]], with rounding to nearest and ties to
even, each operation rounded once.

**Definition {#def:appc-iteration}** (The iteration.) In a cell with the counts N_o and N_i of its segment, start from
G := B and carry out N_o outer steps; the cell's values are G after the last one. An outer step is:

(i) the defect r := P(G) − G, formed in 𝔽 by [[def:appc-cell]]; if r = 0 the step leaves G unchanged, and otherwise ν
is the integer with 2^(−ν) ≤ max |r^F_abk| < 2^(1−ν), the maximum over all entries of r;

(ii) the scaled defect r̃ := rd(2^ν r) entrywise, d := r̃, and then N_i times d := r̃ ⊕ I_𝔻(d) entrywise, with I_𝔻 of
(iv);

(iii) the update G := G + ⌊2^(−ν) d⌋_B entrywise (2^(−ν) d is a rational number).

(iv) The linearised map. For a family d in 𝔻, I_𝔻(d) is formed in 𝔻 by the operations of [[eq:appc-short]], from the
jets J̄ := rd J(G) of the current G at each node (each of the thirty-one numbers rounded by rd), and from the cell's
numbers of [[def:appc-grid]] and [[def:appc-cell]], each replaced by its rd (the matrices, h_ξ, h_v, 1 ⊘ h_ξ, 1 ⊘ h_v,
e₂, e₃, e₄, 1 ⊘ e₂, 1 ⊘ e₃, u_ξ, 1 ⊘ u_ξ and the angular nodes; a rational constant q stands for rd q):
- the D-quantities Ḋ^F, Ḋ^F_x, Ḋ^F_xx, Ḋ^F_v, Ḋ^F_vx and Ḋ^F_u are those of (b) of [[def:appc-cell]] with d in place
  of G, ⊗ in place of ⊙, ⊕ in place of +, ⊘_𝔻 in place of ⊘ and ⋆^𝔻 in place of ⋆ (the integer multiple 4(·) is 4 ⊗ (·));
- the tangent jets are Ṙ := Ḋ^R, (R⁻¹)˙ := −((R̄⁻¹ ⊗ R̄⁻¹) ⊗ Ḋ^R), Ṡ := (((Ḋ^m ⊕ (x̄ ⊗ Ḋ^m)) ⊕ Ḋ^n) ⊖ (x̄ ⊗ Ḋ^n)) ⊘_𝔻 3,
  (e^S)˙ := ē^S ⊗ Ṡ, (e^(−S))˙ := −(ē^(−S) ⊗ Ṡ), (Ω²)˙ := Ω̄² ⊗ (2 ⊗ Ḋ^W), (Ω⁻²)˙ := −(Ω̄⁻² ⊗ (2 ⊗ Ḋ^W)), where R̄⁻¹,
  ē^(±S), Ω̄^(±2) and x̄ are the rd of R⁻¹, e^(±S), Ω^(±2) and x, and for each of the other twenty-four jets the
  corresponding Ḋ (for R_u it is Ḋ^R_u, for m_vx it is Ḋ^m_vx, and so on);
- the sequence of (c) is evaluated in 𝔻 for pairs: each symbol carries a value ā and a tangent ȧ, the jets carry the
  values J̄ and the tangent jets, x and the rational constants carry tangent 0; a product a ⊙ b gives the value ā ⊗ b̄
  and the tangent (ȧ ⊗ b̄) ⊕ (ā ⊗ ḃ), a sum or difference of terms gives the values and the tangents summed with ⊕ and
  ⊖ from the left in the order written, and a negation negates both;
- with the tangents Ẋ_F of the outputs, Ψ̇^F := ū_ξ ⊗ Ẋ_F (F = R, m, n, W) and Φ̇ := Ẋ_s, and I_𝔻(d) is the right side
  of [[eq:appc-rule-int]] with Ψ̇, Φ̇ in place of Ψ, Φ, the operations of [[eq:appc-short]] in place of those of
  [[eq:appc-arith]], and the rounded numbers.

In exact arithmetic I_𝔻 is the derivative of I at G, so an outer step is a Newton step whose linear system is solved
approximately by N_i sweeps; the scaling by 2^ν places the defect where 𝔻 resolves it. The rounding of each outer step
is fixed by (i)–(iv), so the iteration is part of the definition like every other step.

#### Segments, resampling and the hand-off {#sec:appc-segments}

**Definition {#def:appc-resample}** (Resampling in angle.) Let L = (L_k)_(0≤k≤M) be values at the angular nodes of
degree M and M′ ≥ 1. The values of L at the angular nodes of degree M′ are

    L′_k′ := ⟨(ĉ(n k′, M′))_(0≤n≤M), (c_n)_(0≤n≤M)⟩   (0 ≤ k′ ≤ M′),   where   c := Ĉ^(x,M) ⋆_k L.

In exact arithmetic c are the Chebyshev coefficients of the polynomial of degree M through the values L, and L′ its
values at the nodes cos(πk′/M′), since T_n(cos(πk′/M′)) = cos(πnk′/M′).

When a cell of one segment receives its left edge from a cell of another segment, each field of the edge is resampled,
for each node v_b, from the M of the sending segment to the M of the receiving one.

**Definition {#def:appc-handoff}** (The hand-off state.) The hand-off state of a segment is the right edge of its last
column: the numbers G^F_(p_ξ b k) of the cells (i, j), 0 ≤ j < n_r, of that column, for F = R, m, n, W, before any
resampling. With the data of [[def:appc-rule-data]] for the cone u = −10 it determines the rule's values in all later
columns, since a cell uses nothing from the columns before it but its left edge. Its canonical string is formed as in
[[def:appc-canonical]]: for each row j, each F in the order R, m, n, W and each b in increasing order, one line made of
the word "edge", the numbers j and b, the letter of F, and the M + 1 integers 2^B G^F_(p_ξ b k), k = 0, …, M.

**Remark {#rem:appc-segments}** (Why segments.) The angular resolution the solution needs grows toward u*, most of all
for the first seed near the horizon, and the segments let each part of the region carry its own M. A segment's
hand-off state is the characteristic data on its last outgoing cone u = const for everything after it; together with
the element values of [[def:appc-element-values]] formed so far it is all an execution needs to continue, and its
digest ([[sec:appc-spot]]) lets an execution check itself at the end of each segment. The outcome of the rule does not
depend on how its execution is divided.

#### Values and coefficients on the elements {#sec:appc-rule-output}

**Definition {#def:appc-element-values}** (The element coefficients.) Let (i, j) be an element of the layout, with
ξ-box [m_i − h_i, m_i + h_i], v-box [m′_j − h′_j, m′_j + h′_j] and degrees N_t, N_s ([[sec:appc-parameters]]), and let
M_e be the largest M of the segments that contain a column whose cells contain one of the element's nodes below. The
nodes of the element are

    ξ_a := m_i − h_i ⊙ ĉ(a, N_t)  (0 ≤ a ≤ N_t),       v_b := m′_j − h′_j ⊙ ĉ(b, N_s)  (0 ≤ b ≤ N_s),

with m_i, h_i, m′_j, h′_j standing for their floors ⌊·⌋_B. The cell of a node (ξ_a, v_b) is (i_c, j_c), where i_c is the
least i with ξ_a ≤ ξ^(i+1), or n_c − 1 if there is none, and j_c the least j with v_b ≤ v^(j+1), or n_r − 1 if there is
none; so a node outside the grid (the first ξ-node of the first boxes lies below ξ̂₀) takes the nearest cell. In that
cell, with its local coordinates τ* := (ξ_a − ξ^(i_c)) ⊘ h_ξ − 1 and ς* := (v_b − v^(j_c)) ⊘ h_v − 1 and the Lagrange
bases ℓ^ξ of its ξ-nodes (Lobatto, degree p_ξ) and ℓ^v of its v-nodes (Radau or Lobatto, degree p_v), the value of a
field at (ξ_a, v_b, x_k), x_k an angular node of the cell's M, is

    Γ^F_abk := ⟨(ℓ^ξ_a′(τ*))_(a′), (⟨(ℓ^v_b′(ς*))_(b′), (G^F_(a′b′k))_(b′)⟩)_(a′)⟩,

the inner dot product over b′ formed for each a′ first. If the cell's M differs from M_e, the values Γ^F_ab· are
resampled from M to M_e by [[def:appc-resample]]. The coefficients of the element are

    C^F := Ĉ^(N_t) ⋆_a (Ĉ^(N_s) ⋆_b (Ĉ^(x,M_e) ⋆_k Γ^F)),       z^F_abk := ⌊10^p C^F_abk + 1/2⌋,       {#eq:appc-rule-z}

the transform in x first, then in σ, then in t, and p the quantum of the case. These are the integers p and z^(ij,F)_abk
of [[def:appc-approximant]]; I_(ij,F) is the set of (a, b, k) with z^F_abk ≠ 0, so the degrees of G^F_ij are at most
N_t, N_s and M_e.

#### The parameters {#sec:appc-parameters}

The parameters of the three cases are below [[pending:computational-appc-parameters]]. In every case B = 320, the counts
of [[def:appc-functions]] and [[def:appc-rule-seed]] are as stated there, and N_Ray := 40. The columns form the segments
listed, each with its angular degree M and its counts N_o and N_i of [[def:appc-iteration]].

    case       n_c × n_r   (p_ξ, p_v)   segments (columns: M)                          (N_o, N_i)   (N_t, N_s)    p
    (1, D_A)   32 × 30     (26, 39)     0–15, 16–23, 24–27, 28–29, 30, 31: M = 184     (9, 25)      (104, 136)    56
    (2, D*)    64 × 30     (28, 42)     0–31, 32–47, 48–55, 56–59, 60–61, 62, 63:      (10, 25)     (152, 184)    61
                                        M = 184
    (1, D*)    64 × 30     (30, 45)     0–31, 32–47: M = 200;                          (10, 25)     (136, 200)    64
                                        48–55, 56–59, 60–61, 62, 63: M = 328

For the case (2, D_A) the parameters of (1, D_A) serve, with M = 168 and p = 55.

#### Properties {#sec:appc-rule-properties}

**Remark {#rem:appc-rule-defined}** (Where the rule is defined.) Every quantity of the rule is an element of 𝔽 or of 𝔻
([[def:appc-short]]), a rational number held by integers, every operation of [[eq:appc-arith]] and [[eq:appc-short]] is
exact rational arithmetic followed by one rounding, and every loop has a fixed length; so the rule defines integers p
and z^(ij,F)_abk, and with them the approximant ĝ of [[def:appc-approximant]], as soon as no divisor vanishes, no
logarithm or square root meets a nonpositive argument and no rounding rd meets a number beyond the range of 𝔻. The
divisors and arguments that depend on the values the rule forms, and not on the parameters alone, are R_s + D^R, Ω_s²,
u_ξ and the arguments of the logarithms in [[def:appc-rule-seed]]; the others are the differences of nodes, h_ξ, h_v,
e₂, e₃, e₄ and η₄, fixed by the parameters. For the parameters of [[sec:appc-parameters]] all of them are nonzero, and
the arguments positive, at every step [[pending:computational-appc-parameters]].

**Remark {#rem:appc-rule}** (What the rule does not need.) The result of the rule does not depend on the order of the
summations in the dot products of [[eq:appc-arith]], which are exact before their one rounding; the order of every sum
in 𝔻 is fixed by [[def:appc-short]]. It does not depend on how the loops over nodes are distributed among processors or
on how the execution is divided into segments. It uses no rounding but those of [[eq:appc-arith]] and [[eq:appc-short]]
and no function but those of [[def:appc-functions]]. Its accuracy as an approximation plays no part in what follows; the
certificate of [[sec:appc-certification]] is a theorem about its exact output. With zero cone data (m = n = 0 on u =
−10) every G is 0 and every z is 0, since then B = 0 and P(0) = 0 exactly.

**Remark {#rem:appc-picard}** (The plain iteration.) Replacing [[def:appc-iteration]] by N_P plain steps G := P(G)
also defines a rule, with one arithmetic, a shorter statement, the same fixed points of P and other integers. The outer
steps of [[def:appc-iteration]] are used for the cost of carrying out the rule; nothing that follows depends on the
choice.


### The output and its digest {#sec:appc-digest}

The integers of a case are not printed. This section fixes a canonical form of them, a digest of that form, and three
exact checks per block.

**Definition {#def:appc-canonical}** (The canonical string.) A block is the set of integers z^(ij,F)_abk of one element
(i, j) and one field F, with its p. The canonical string of a block consists of ASCII characters: the digits, the
letters, the space (character 32), the hyphen-minus (character 45) and the line feed (character 10). It is the
following lines, each ended by a line feed:
- a header line: the word "block", then i, j, the letter R, m, n, W or s of F, p, N_t, N_s and M_e;
- for each pair (a, b) for which some z_abk ≠ 0, in the order of a and then b, a line with a, b and then
  z_ab0, z_ab1, …, z_abK, where K is the largest k with z_abk ≠ 0 (entries with k ≤ K that are zero are written 0).

Integers are written in decimal without leading zeros (zero as 0), a negative integer with a hyphen-minus before it, and
consecutive items of a line are separated by one space. The canonical string of the case is the concatenation of the
canonical strings of its blocks, in the order of i, then j, then F in the order R, m, n, W, s.

The canonical string carries the same information as the integers, and the integers can be read back from it.

**Definition {#def:appc-digest}** (The digest.) The digest of a string of ASCII characters is the hash function SHA-256
of the Secure Hash Standard [[pending:ref-fips-180-4]] applied to the sequence of its character numbers, one byte per
character, written as 64 hexadecimal digits 0–9, a–f (the 32 bytes of the hash, each as two digits). The digest of a
case, of a block and of a hand-off state ([[def:appc-handoff]]) is the digest of its canonical string.

The three block sums of a block are the integers

    S₁ := Σ z_abk = 10^p G(1, 1, 1),      S₂ := Σ (−1)^(a+b+k) z_abk = 10^p G(−1, −1, −1),
    S₀ := Σ_(a, b, k even) (−1)^((a+b+k)/2) z_abk = 10^p G(0, 0, 0),                                     {#eq:appc-sums}

the identities holding because T_n(1) = 1, T_n(−1) = (−1)^n and T_n(0) = cos(nπ/2); G is the block's G^F_ij of
[[eq:appc-fields]].

**Remark {#rem:appc-digest}** (What the digest and the sums check.) SHA-256 is a fixed function, so the equation
"digest of the canonical string of Z = the printed digest" is a definite statement about a set Z of integers, which
anyone can test. If it fails, Z is not the rule's output. If it holds, Z equals the rule's output unless the two collide
under SHA-256; no collision of SHA-256 is known, but a digest of 256 bits cannot separate all sets of integers, and the
inference is not a theorem. Nothing in this appendix rests on it: the certificate of [[sec:appc-certification]] is a
theorem about the rule's exact output, and whoever carries out the rule and the certification on its output has the
whole argument, digest or not. The digest says that the certified numbers printed in [[sec:appc-outcomes]] belong to
the integers in hand, and the block digests and hand-off digests locate a discrepancy. The block sums are exact
checks: they are values of the block's polynomial at three points, a match proves those three values equal, and a
mismatch proves that the blocks differ.

### The residual in a form regular at the axes {#sec:appc-regular}

The formula of [[sec:tl5-formula]] contains 1/(1 + x), 1/(1 − x), x/w and (1 + x²)/w² with w = (1 + x)(1 − x), and the
factor μ = e^(−ζ) = 2√w e^S/R ([[eq:tl5-derivatives]]); the components are bounded at the axes, but the individual
terms are not. An enclosure that reaches x = ±1 needs the cancellations made explicit. We write them out.

For ψ ∈ {ζ, A, B} and every index a ∈ {u, v, x, uu, uv, vv, ux, vx, xx} let ψ°_a be ψ_a of [[eq:tl5-derivatives]] with
the terms x/w, 1/(2(1 + x)), −1/(2(1 − x)), (1 + x²)/w², −1/(2(1 + x)²) and −1/(2(1 − x)²) omitted:

    ζ°_a := ℓ_a − S_a,   A°_a := ℓ_a + P_a,   B°_a := ℓ_a + Q_a     (ℓ_a or ℓ_ab as in [[eq:tl5-derivatives]]).

So ψ_a = ψ°_a for a ≠ x, xx. Put

    ζ̌ := wζ°_x + x,   Ǎ := wA°_x + (1 − x)/2,   B̌ := wB°_x − (1 + x)/2,
    ζ̌₂ := w²ζ°_xx + 1 + x²,   Ǎ₂ := w²A°_xx − (1 − x)²/2,   B̌₂ := w²B°_xx − (1 + x)²/2,              {#eq:appc-checked}

which are wψ_x and w²ψ_xx, and

    μ̂ := 2e^S/R,   τ̂ := R s_v/(8e^S Ω²),   η̂ := μ̂ W_x,   λ := ℓ_x + 2S_x,
    α₁ := (1 + x)A°_x + 1/2,   β₁ := (1 − x)B°_x − 1/2,                                                  {#eq:appc-hat}

so that μ = √w μ̂, τ = √w τ̂ and η = √w η̂. Define further

    Σ_EE := w(A°_xx + B°_xx + A°_xA°_x + B°_xB°_x − ζ°_x(A°_x + B°_x)) + (1 − 2x)A°_x − (1 + 2x)B°_x + xζ°_x − 1/2,
    Σ₁₁ := w(A°_xx + A°_x λ) − 2xA°_x + ((1 − x)/2)λ − 1/2,
    Σ₂₂ := w(B°_xx + B°_x λ) − 2xB°_x − ((1 + x)/2)λ − 1/2,
    Θ_A := w(A°_x(A°_x − ζ°_x) + A°_xx) + ((1 − x)/2)(A°_x − ζ°_x) + ((1 − 3x)/2)A°_x − 1/4,
    Θ_B := w(B°_x(B°_x − ζ°_x) + B°_xx) − ((1 + x)/2)(B°_x − ζ°_x) − ((1 + 3x)/2)B°_x − 1/4.          {#eq:appc-sigma}

**Lemma {#lem:appc-regular}** (The residual regular at the axes.) For every metric of the class with C² fields and
R > 0, at every point with |x| < 1, the eight components of [[eq:tl5-components]] are

    f_ll = ρ N(L, L),   f_ln = ρ N(L, Y)/(2Ω²),   f_nn = ρ N(Y, Y)/(4Ω⁴),
    f_lx = ρ √w (−L̂η + L̂τ + 2kτ̂ − Σ_LE),   f_nx = ρ √w (−Ŷη − Ŷτ − 2k̲τ̂ − Σ_YE)/(2Ω²),
    f_xx = ρ (Ric(E, E) − h°_A − h°_B − μ̂²Σ_EE),
    f_11 = −ρ (□°A + ⟨dA, dA⟩° + ⟨dA, dB⟩° + μ̂²Σ₁₁),   f_22 = −ρ (□°B + ⟨dB, dB⟩° + ⟨dA, dB⟩° + μ̂²Σ₂₂),
                                                                                                       {#eq:appc-regular}

where N(X, Z) := Ric(X, Z) − M_A(X, Z) − M_B(X, Z) for XZ ∈ {LL, YY, LY}, and all quantities are the following
polynomials in x, in the values and first and second derivatives of R, m, n, W, s, and in 1/R, e^(±S) and 1/Ω²:

    Y(ζ) := ζ°_u + sζ̌,   ω := W_v,   ω̲ := W_u + bW_x,   k := ζ°_v,   k̲ := ζ°_u + sζ̌ + b_x,
    L(k̲) := ζ°_uv + s_vζ̌ + bζ°_vx + b_vx,   Y(k) := ζ°_uv + bζ°_vx,   L(ω̲) := W_uv + b_vW_x + bW_vx,
    Y(k̲) := ζ°_uu + s_uζ̌ + 2bζ°_ux + b_ux + s b_x ζ̌ + s²ζ̌₂ + b b_xx,
    L̂η := μ̂(W_vx − ζ°_vW_x),   Ŷη := μ̂(W_ux + bW_xx − Y(ζ)W_x),   E(η) := μ̂²(wW_xx − ζ̌W_x),
    L̂τ := τ̂(ζ°_v − 2ω) + R s_vv/(8e^S Ω²),   Ŷτ := τ̂(Y(ζ) − 2ω̲) + R (s_uv + s(ws_vx − 2xs_v))/(8e^S Ω²),
    E(τ) := μ̂τ̂(ζ̌ − 2wW_x) + b_vx/(4Ω²),
    Ric(L, L) := −ζ°_vv + 2ωk − kk,   Ric(Y, Y) := −Y(k̲) + 2ω̲k̲ − k̲k̲,
    Ric(L, Y) := −L(k̲) − 2L(ω̲) − kk̲ + Ω²(2E(η) + 2E(τ) + w(4η̂η̂ + 8η̂τ̂ − 4τ̂τ̂)),
    Ric(E, E) := −2E(η) − 2w(η̂η̂ + τ̂τ̂) + (L(k̲) + Y(k) + 2kk̲)/(2Ω²),

and, for ψ ∈ {A, B} with ψ̌ and ψ̌₂ from [[eq:appc-checked]],

    ψ_L := ψ°_v,   ψ_Y := ψ°_u + sψ̌,   L(ψ_Y) := ψ°_uv + s_vψ̌ + bψ°_vx,
    Y(ψ_Y) := ψ°_uu + s_uψ̌ + 2bψ°_ux + s b_x ψ̌ + s²ψ̌₂,   h_ψ(L, Y) := L(ψ_Y) − 2Ω²(η̂ + τ̂)μ̂ψ̌,
    M_ψ(L, L) := ψ°_vv − 2ωψ_L + ψ_Lψ_L,   M_ψ(Y, Y) := Y(ψ_Y) − 2ω̲ψ_Y + ψ_Yψ_Y,
    M_ψ(L, Y) := h_ψ(L, Y) + ψ_Lψ_Y,   h°_ψ := −(k̲ψ_L + kψ_Y)/(2Ω²),
    □°ψ := −h_ψ(L, Y)/Ω² + h°_ψ,   ⟨dψ, dχ⟩° := −(ψ_Lχ_Y + ψ_Yχ_L)/(2Ω²),
    Σ_LE := μ̂(A°_vx + B°_vx + α₁m_v + β₁n_v) − (η̂ + τ̂)(A°_v + B°_v),
    Σ_YE := μ̂(A°_ux + B°_ux + α₁m_u + β₁n_u + s(Θ_A + Θ_B)) − (η̂ − τ̂)(A_Y + B_Y).

In particular every f_ab, and f_lx/√w and f_nx/√w, extends continuously to x = ±1, by these expressions; the only
divisions in them are by R, Ω², e^S and the integers 2, 3, 4 and 8.

*Proof.* Write ψ = ψ° + σ_ψ with σ_ζ := −(1/2) log(4w), σ_A := (1/2) log((1 + x)/2) and σ_B := (1/2) log((1 − x)/2),
which depend on x alone. Their derivatives are σ′_ζ = x/w, σ″_ζ = (1 + x²)/w², σ′_A = 1/(2(1 + x)),
σ″_A = −1/(2(1 + x)²), σ′_B = −1/(2(1 − x)) and σ″_B = −1/(2(1 − x)²), the omitted terms above; so ψ_x = ψ°_x + σ′_ψ,
ψ_xx = ψ°_xx + σ″_ψ, and [[eq:appc-checked]] states wσ′_ζ = x, wσ′_A = (1 − x)/2, wσ′_B = −(1 + x)/2, w²σ″_ζ = 1 + x²,
w²σ″_A = −(1 − x)²/2 and w²σ″_B = −(1 + x)²/2. Six further identities are checked by putting each over the common
denominator 4w and expanding: with σ′_A + σ′_B − σ′_ζ = −2x/w,

    w(σ″_A + σ′_A(σ′_A + σ′_B − σ′_ζ)) = −1/2 = w(σ″_B + σ′_B(σ′_A + σ′_B − σ′_ζ)),
    w(σ″_A + σ″_B + σ′_Aσ′_A + σ′_Bσ′_B − σ′_ζ(σ′_A + σ′_B)) = −1/2,
    w(σ″_A + σ′_A(σ′_A − σ′_ζ)) = −1/4 = w(σ″_B + σ′_B(σ′_B − σ′_ζ)),
    (1 + x)σ′_A = 1/2,   (1 − x)σ′_B = −1/2.                                                            {#eq:appc-sing}

For instance the first reads −(1 − x)/(2(1 + x)) − x/(1 + x) = −1/2. Finally, by the definitions of S, P and Q,
A°_a − ζ°_a = P_a + S_a = (2P + Q)_a = ((1 + x)m)_a and B°_a − ζ°_a = ((1 − x)n)_a, so that

    A°_v − ζ°_v = (1 + x)m_v,   B°_v − ζ°_v = (1 − x)n_v,   A°_u − ζ°_u = (1 + x)m_u,   B°_u − ζ°_u = (1 − x)n_u.

Take the chapter's formula ([[eq:tl5-components]], [[eq:tl5-derivatives]], [[eq:tl5-frame-derivatives]] and the
lines after it) term by term. A first derivative ψ_x occurs multiplied by b, b_u, b_v or b·b_x, which carry the factor
w, so bψ_x = sψ̌, b_uψ_x = s_uψ̌, b_vψ_x = s_vψ̌ and b b_xψ_x = s b_xψ̌; ψ_xx occurs only as b²ψ_xx = s²ψ̌₂, and in
the factors E(ψ_E) = μ²(ψ_xx − ζ_xψ_x), μ²ψ_x and μ ψ_x treated below. With μ = √w μ̂, ϑ = e^(ζ−2W)/4 = 1/(4√w μ̂Ω²)
and b_v = ws_v one has τ = ϑb_v = √w τ̂, η = μW_x = √w η̂, and ϑb_vv, ϑ(b_uv + bb_vx) and μ(τ(ζ_x − 2W_x) + ϑb_vx)
equal √w R s_vv/(8e^S Ω²), √w R(s_uv + s(ws_vx − 2xs_v))/(8e^SΩ²) and E(τ) as defined. This gives every quantity
of [[eq:tl5-ricci3]] in the stated form: L(η) = √w L̂η, Y(η) = √w Ŷη, L(τ) = √w L̂τ, Y(τ) = √w Ŷτ, and E(η), E(τ),
η², ητ, τ² = w(·) as written, so that Ric[g3](L, E) = √w(−L̂η + L̂τ + 2kτ̂) and Ric[g3](Y, E) = √w(−Ŷη − Ŷτ − 2k̲τ̂).

It remains to treat the terms with ψ_E = μψ_x and with E(ψ_E) in M_ψ and ⟨dψ, dχ⟩. In h_ψ(L, Y) the term
2Ω²(η + τ)ψ_E = 2Ω²(η̂ + τ̂)μ̂ wψ_x = 2Ω²(η̂ + τ̂)μ̂ψ̌. The terms μ²ψ_xχ_x of M_ψ(E, E), □ψ and ⟨dψ, dχ⟩ combine with
μ²(ψ_xx − ζ_xψ_x) as follows. In N(E, E) they give −μ̂²w(A_xx + B_xx + A_xA_x + B_xB_x − ζ_x(A_x + B_x)); in f_11
they give −μ̂²w(A_xx + A_x(A_x + B_x − ζ_x)), and in f_22 the same with A and B interchanged, where
A_x + B_x − ζ_x = λ + σ′_A + σ′_B − σ′_ζ because A° + B° − ζ° = log R + 2S. Expanding each with ψ_x = ψ°_x + σ′_ψ
and ψ_xx = ψ°_xx + σ″_ψ, the products of two regular parts and the terms ψ°_x · wσ′_χ are polynomials, and the purely
singular parts are the left sides of [[eq:appc-sing]]; collecting gives w times these brackets equal to Σ_EE, Σ₁₁ and
Σ₂₂. For example w(A_xx + A_x(A_x + B_x − ζ_x)) = w(A°_xx + A°_xλ) + A°_x · w(−2x/w) + wσ′_A λ + w(σ″_A +
σ′_A(−2x/w)) = Σ₁₁ by the first identity of [[eq:appc-sing]]. Next, M_A(L, E) + M_B(L, E) = Σ_ψ (L(ψ_E) −
(η + τ)ψ_L + ψ_Lψ_E) = √w Σ_ψ (μ̂(ψ°_vx + ψ_x(ψ°_v − ζ°_v)) − (η̂ + τ̂)ψ°_v), and with the last display and the fifth and
sixth identities of [[eq:appc-sing]], ψ_x(ψ°_v − ζ°_v) is α₁m_v for ψ = A and β₁n_v for ψ = B; this is √w Σ_LE.
Likewise M_A(Y, E) + M_B(Y, E) = √w Σ_ψ (μ̂(ψ°_ux + bψ_xx + ψ_x(ψ_Y − Y(ζ))) − (η̂ − τ̂)ψ_Y), and with
ψ_Y − Y(ζ) = (ψ°_u − ζ°_u) + s(ψ̌ − ζ̌) one gets μ̂(ψ°_ux + ψ_x(ψ°_u − ζ°_u)) + μ̂ s w(ψ_xx + ψ_x(ψ_x − ζ_x)), where
the first is μ̂(A°_ux + α₁m_u) or μ̂(B°_ux + β₁n_u) and the second is μ̂sΘ_ψ by the third and fourth identities of
[[eq:appc-sing]]; this is √w Σ_YE. Substituting in [[eq:tl5-components]], with l = L, n̂ = Y/(2Ω²) and e_x = E,
gives [[eq:appc-regular]]. Every quantity in it is a polynomial in x and the jets, divided at most by R, Ω², e^S and
the integers named, so it is defined and continuous at x = ±1; since the left sides are continuous on the metric's
domain, axes included, the identities extend to x = ±1. ∎

So f_lx and f_nx vanish at the axes like √(1 − x²), and |f_ab| ≤ |f̃_ab| for the regular parts f̃_lx := f_lx/√w,
f̃_nx := f_nx/√w and f̃_ab := f_ab otherwise. The certification below bounds the f̃_ab.

### Certification {#sec:appc-certification}

The residual is bounded on each element's use interval in two steps: the residual of the element's own polynomial
approximant, by interpolation in ball arithmetic and an analyticity bound on a polyellipse
([[prop:appc-element-bound]]); and the effect of the partition of unity on the overlaps, by a perturbation bound
([[prop:appc-overlap]]). Every number used is either exact or an interval that contains the exact value, formed by the
rules of [[def:tl5-jets]] (real intervals) and the same rules for complex rectangles; the exponential, logarithm,
sine, cosine and square root of an interval are enclosed by their power series with an explicit tail bound, in any
of the standard ways.

#### Exact operations on the coefficients {#sec:appc-exact}

The coefficients z 10^(−p) are rational. Derivatives in t, σ and x of a field [[eq:appc-fields]] have rational
Chebyshev coefficients, obtained by [[eq:tl5-cheb-derivative]] ([[lem:tl5-chebyshev]]).

**Lemma {#lem:appc-reexpand}** (Affine change of variable.) Let c and h ≠ 0 be rational. There are rational numbers
A_jk, 0 ≤ k ≤ j, with T_j(c + hτ) = Σ_k A_jk T_k(τ) for all τ; they are given by A₀₀ = 1, (A₁₀, A₁₁) = (c, h) and
T_(j+1)(c + hτ) = 2c T_j(c + hτ) + 2h τT_j(c + hτ) − T_(j−1)(c + hτ), with τT_k = (T_(k+1) + T_(|k−1|))/2.

*Proof.* The recurrence T_(j+1)(y) = 2yT_j(y) − T_(j−1)(y) at y = c + hτ and the product formula
2T_1T_k = T_(k+1) + T_(|k−1|) give the stated recursion; it involves only rational operations. ∎

So the polynomial G^F_ij restricted to a sub-box [t_c − t_h, t_c + t_h] × [σ_c − σ_h, σ_c + σ_h] × [−1, 1] has exact
rational Chebyshev coefficients in the variables τ₁ := (t − t_c)/t_h, τ₂ := (σ − σ_c)/σ_h and τ₃ := x.

#### The seed in complex arithmetic {#sec:appc-seed}

On u < −1 the seed's radius solves G(R) = H(u, v), where

    G(R) := 2R + log((R − 1)/(R + 1)),      H(u, v) := v − 2u + log((u + 1)/(u − 1)),                  {#eq:appc-seed-eq}

by [[eq:tl5-seed-radius]] after taking logarithms; and by [[lem:tl5-seed]] (b) and the chain rule, with f(r) = 1 − r⁻²
and g(u) := f(−u) = 1 − u⁻²,

    ∂_vR_s = f/2,   ∂_uR_s = −f/g,   ∂_v²R_s = f′∂_vR_s/2,   ∂_u∂_vR_s = f′∂_uR_s/2,
    ∂_u²R_s = −f′∂_uR_s/g + fg′/g²,   Ω_s² = e^(2W_s) = f/(2g),   ∂_vW_s = f′∂_vR_s/(2f),
    ∂_uW_s = (f′∂_uR_s/f − g′/g)/2,                                                                  {#eq:appc-seed-jets}

and the second derivatives of W_s by differentiating the last two once more; here f = f(R_s), f′ = 2R_s⁻³,
g′ = 2u⁻³. In [[eq:appc-seedform]] W enters the residual only through its derivatives and through
Ω² = Ω_s² e^(2(v−1/2)^κ Σχψ G^W).

**Lemma {#lem:appc-seed-holo}** (The inverse of G.) On the half plane {Re R > 3/2}, G is holomorphic and injective, and
G′ = 2 + 2/(R² − 1) does not vanish; so G has a holomorphic inverse on G({Re R > 3/2}).

*Proof.* There |R| > 3/2, hence |R² − 1| ≥ |R|² − 1 > 5/4 and Re G′ ≥ 2 − 2/|R² − 1| > 2/5. Also (R − 1)/(R + 1) has
positive real part, since its real part is (|R|² − 1)/|R + 1|², so the principal logarithm is holomorphic. If
G(R₁) = G(R₂) with R₁ ≠ R₂ in the convex half plane, then 0 = (R₂ − R₁)∫₀¹ G′(R₁ + θ(R₂ − R₁)) dθ, whose real part is
positive; so G is injective, and its inverse is holomorphic since G′ ≠ 0. ∎

**Lemma {#lem:appc-newton}** (One step of interval Newton.) Let X be a closed rectangle in {Re R > 3/2}, r_c ∈ X,
𝐇 a closed rectangle, and Q a closed rectangle containing G′(X), with 0 ∉ Q. If

    N := r_c − (G(r_c) − 𝐇)/Q ⊂ X

in rectangle arithmetic, then for every H₀ ∈ 𝐇 the equation G(R) = H₀ has exactly one solution in {Re R > 3/2}, and it
lies in N.

*Proof.* For r ∈ X put q(r) := ∫₀¹ G′(r_c + θ(r − r_c)) dθ, which lies in the closed convex hull of G′(X), hence in
Q. The map r ↦ r_c − (G(r_c) − H₀)/q(r) is continuous on X and takes values in N ⊂ X, so by Brouwer's theorem it has a
fixed point r*, and q(r*)(r* − r_c) = H₀ − G(r_c) says G(r*) = H₀. Uniqueness is [[lem:tl5-seed]] (a) on the reals and
[[lem:appc-seed-holo]] in the half plane. ∎

#### The residual of one polynomial approximant on a box {#sec:appc-box}

Fix an element (i, j) and a sub-box 𝔅 = [t_c − t_h, t_c + t_h] × [σ_c − σ_h, σ_c + σ_h] × [−1, 1] of [−1, 1]³ in
(t, σ, x), with rational centre and half-widths; in this appendix 𝔅 is the element's use interval U_ij, rounded
outward to multiples of 1/1000, in (t, σ). Let F_ij be the fields [[eq:appc-seedform]] with χ_iψ_j replaced by 1 and
all other terms by 0, and let g_ab(τ) := f̃_ab(F_ij) at (t, σ, x) = (t_c + t_hτ₁, σ_c + σ_hτ₂, τ₃), for τ ∈ [−1, 1]³.
The polynomial parts of F_ij are Q^F := (v − 1/2)^κ G^F_ij; since v − 1/2 = α + βτ₂ with rational α, β, they are
polynomials in τ whose Chebyshev coefficients are exact rationals, by [[lem:appc-reexpand]] and κ multiplications by
α + βτ₂ (with τ₂T_k = (T_(k+1) + T_(|k−1|))/2).

For ρ > 1 let E_ρ be the closed region bounded by the ellipse {(ω + ω⁻¹)/2 : |ω| = ρ}, as in [[lem:cone-ellipse]],
and for ρ = (ρ₁, ρ₂, ρ₃) let ℰ_ρ := E_ρ₁ × E_ρ₂ × E_ρ₃ ⊂ ℂ³ and ∂₀ℰ_ρ := ∂E_ρ₁ × ∂E_ρ₂ × ∂E_ρ₃ its distinguished
boundary.

On E_ρ every Chebyshev polynomial satisfies |T_n(τ)| ≤ ρ^n, since τ = (ω + ω⁻¹)/2 with 1 ≤ |ω| ≤ ρ and
T_n(τ) = (ω^n + ω^(−n))/2. Hence a polynomial Σ c_ijk T_i(τ₁)T_j(τ₂)T_k(τ₃) is bounded on ℰ_ρ by its weighted
coefficient sum Σ |c_ijk| ρ₁^i ρ₂^j ρ₃^k, and so is each derivative, with the coefficients of [[eq:tl5-cheb-derivative]].

**Lemma {#lem:appc-analytic}** (Analyticity on a polyellipse.) Suppose that: (i) on a covering of E_ρ₁ by closed
rectangles, the enclosures of cosh ξ, of Re((u + 1)/(u − 1)) and of Re u + 1, with ξ = m_i + h_i(t_c + t_hτ₁) and
u = −1 + a sinh ξ, are respectively of positive real part, positive and negative; (ii) a rectangle in ℂ that contains
H(u, v) for all τ₁ ∈ E_ρ₁, τ₂ ∈ E_ρ₂ (with v = m′_j + h′_j(σ_c + σ_hτ₂)) is covered by rectangles 𝐇 on each of which
[[lem:appc-newton]] applies, the least real part of the enclosures N so obtained being r_s; (iii) r_s exceeds the
weighted coefficient sum q_R of Q^R. Then every g_ab extends holomorphically to a neighbourhood of ℰ_ρ, and there
Re R ≥ r_s − q_R > 0.

*Proof.* By (i), ξ and u are holomorphic in τ₁, cosh ξ ≠ 0 (so dt/du and its derivative are holomorphic), u ∉ [−1, 1]
and the logarithm in H is holomorphic; so H is holomorphic on E_ρ₁ × E_ρ₂. By (ii) and [[lem:appc-newton]] every value
of H there is G(R) for a unique R with Re R > 3/2, so R_s = G⁻¹ ∘ H is holomorphic by [[lem:appc-seed-holo]], with
Re R_s ≥ r_s, hence f(R_s) ≠ 0; and g(u) ≠ 0. So the seed's jets [[eq:appc-seed-jets]] are holomorphic. The
polynomial parts are entire, and so are e^S and Ω²/Ω_s². Since |Q^R| ≤ q_R, Re R ≥ r_s − q_R > 0 by (iii). Hence 1/R,
1/e^S and 1/Ω² are holomorphic, and by [[lem:appc-regular]] so is every g_ab. ∎

**Lemma {#lem:appc-majorant}** (The bound M.) Under the hypotheses of [[lem:appc-analytic]], replace in
[[eq:appc-regular]] every quantity by an upper bound of its modulus on ℰ_ρ, and every operation by the bound of its
result: a ± b by |a| + |b|, ab by |a||b|, and a/b, for b ∈ {R, Ω², e^S, μ̂} and integers, by |a| divided by a lower
bound of |b|. The inputs are: the weighted coefficient sums of Q^F and of its derivatives, multiplied by the bounds of
the chart factors dt/du and d²t/du² on a covering of E_ρ₁ ([[eq:tl5-chain]], with the element's h_i) and by 1/t_h,
1/(h′_jσ_h); the bounds of [[eq:appc-seed-jets]] obtained from r_s ≤ |R_s| ≤ (|H| + 2.35)/2 and from the bounds of |u| on
the covering of (i); (ρ₃ + ρ₃⁻¹)/2 for |x|; e^(±s_S) for e^(±S), with s_S the bound of |S|; and
Ω_s² e^(±2q_W) for Ω². The result, times the bound of ρ = R⁴/√72, is a number M ≥ max_ab sup_(ℰ_ρ) |g_ab|.

*Proof.* Each replacement is the triangle inequality or multiplicativity of the modulus, and every input bounds the
modulus of the quantity it replaces, on all of ℰ_ρ. For |R_s|: the map R ↦ (R − 1)/(R + 1) sends {Re R > 3/2} into
the disc with diameter [1/5, 1], so |log((R − 1)/(R + 1))| ≤ log 5 + arcsin(2/3) < 2.35 there, and
2R_s = H − log((R_s − 1)/(R_s + 1)) gives |R_s| ≤ (|H| + 2.35)/2. ∎

**Lemma {#lem:appc-coefficients}** (Coefficients and interpolation.) Let g be holomorphic on a neighbourhood of ℰ_ρ
with |g| ≤ M there, and let g = Σ a_ijk T_i(τ₁)T_j(τ₂)T_k(τ₃) be its Chebyshev expansion on [−1, 1]³.
Then |a_ijk| ≤ 8Mρ₁^(−i)ρ₂^(−j)ρ₃^(−k). For N = (N₁, N₂, N₃) let p be the polynomial of degree at most N_d in τ_d that
interpolates g at the points (cos(πl₁/N₁), cos(πl₂/N₂), cos(πl₃/N₃)), 0 ≤ l_d ≤ N_d. Then for every multi-index
α = (α₁, α₂, α₃),

    sup_([−1,1]³) |∂^α (g − p)| ≤ E_α := 16M Σ_(d=1..3) S^(>N_d)_d(α_d) ∏_(d′≠d) S_(d′)(α_(d′)),        {#eq:appc-ealpha}

where S_d(l) := Σ_(n≥0) ρ_d^(−n) T_n^(l)(1) and S^(>N)_d(l) := Σ_(n>N) ρ_d^(−n) T_n^(l)(1), with T_n^(l)(1) as in
[[lem:tl5-rounding]].

*Proof.* In one variable, with τ = (z + z⁻¹)/2, the function z ↦ g((z + z⁻¹)/2) is holomorphic on the annulus
ρ⁻¹ ≤ |z| ≤ ρ, and a_n = (1/(πi)) ∮_(|z|=1) g((z + z⁻¹)/2) z^(−n−1) dz for n ≥ 1 (half that for n = 0). Moving the
contour to |z| = ρ gives |a_n| ≤ 2Mρ^(−n). Applied in each variable in turn, with the other two fixed in their
ellipses, this gives the first claim, the factor 8 = 2³ being an upper bound for every (i, j, k). The series converges
absolutely and uniformly on [−1, 1]³ with all its derivatives. At the points cos(πl/N), T_n takes the value of T_(n′),
n′ ∈ [0, N] with n′ ≡ ±n (mod 2N), since cos(nπl/N) depends on n only through that class; so the interpolant of each
T_iT_jT_k is T_(i′)T_(j′)T_(k′), and p = Σ a_ijk T_(i′)T_(j′)T_(k′), with i′ = i when i ≤ N₁ and likewise. Hence
g − p = Σ over the triples with i > N₁ or j > N₂ or k > N₃ of a_ijk (T_iT_jT_k − T_(i′)T_(j′)T_(k′)). By
[[lem:tl5-rounding]], |T_n^(l)| ≤ T_n^(l)(1) on [−1, 1], and T_n^(l)(1) is nondecreasing in n, while n′ ≤ n; so each
difference has its α-derivative bounded by 2∏_d T^(α_d)(1) at the larger indices. Summing over the union of the three
sets {i > N₁}, {j > N₂}, {k > N₃} gives [[eq:appc-ealpha]]. ∎

The sums S are explicit: T_n^(l)(1) ≤ n^(2l)/(1 · 3 ⋯ (2l − 1)), and the tail of Σ n^(2l)ρ^(−n) beyond n₀ is at most
n₀^(2l)ρ^(−n₀)/(1 − ((n₀ + 1)/n₀)^(2l)/ρ) when the denominator is positive.

**Proposition {#prop:appc-element-bound}** (The element's own residual.) Under the hypotheses of
[[lem:appc-analytic]], let M be as in [[lem:appc-majorant]], let c^(ab)_ijk be the Chebyshev coefficients of the
interpolant p_ab of [[lem:appc-coefficients]], and c^(ab,α) those of ∂^αp_ab ([[lem:tl5-chebyshev]]). Then for every
ab and every α,

    sup_𝔅 |∂_t^(α₁)∂_σ^(α₂)∂_x^(α₃) f̃_ab(F_ij)| ≤ (Σ_ijk |c^(ab,α)_ijk| + E_α)/(t_h^(α₁) σ_h^(α₂)).
                                                                                                 {#eq:appc-element-bound}

The coefficients c^(ab) are the exact discrete transform of the values at the nodes,
c_ijk = (2/N₁)(2/N₂)(2/N₃) Σ″ g(τ_l) T_i(τ_l₁)T_j(τ_l₂)T_k(τ_l₃) with the end terms of each sum and the coefficients of
index 0 and N_d halved; with the values enclosed in intervals they are enclosed in intervals.

*Proof.* |∂^αp| ≤ Σ|c^(α)| on [−1, 1]³ since |T_n| ≤ 1, and [[lem:appc-coefficients]] bounds ∂^α(g − p); the
chain rule for τ₁ = (t − t_c)/t_h and τ₂ = (σ − σ_c)/σ_h gives the division. The transform is the inverse of the
evaluation at the Chebyshev–Lobatto points, which is the standard identity for interpolation at those points. ∎

The values g_ab(τ_l) at the nodes are obtained from the 2-jets of the fields there, which by [[lem:appc-reexpand]] and
[[eq:tl5-cheb-derivative]] are exact rational combinations of the integers z evaluated at the nodes, the seed's
jets by [[lem:appc-newton]] and [[eq:appc-seed-jets]], and the chart's derivatives by [[eq:tl5-chain]] with the
element's h_i in place of h_ξ; then [[eq:appc-regular]] is evaluated by the rules for intervals.

#### The overlaps {#sec:appc-overlaps}

On U_ij the fields [[eq:appc-seedform]] differ from those of F_ij by

    δF := (v − 1/2)^κ Σ_((i′,j′) ≠ (i,j)) χ_(i′)ψ_(j′) (G^F_(i′j′) − G^F_ij),                            {#eq:appc-delta}

because Σχ_(i′)ψ_(j′) = 1 ([[lem:appc-pou]] (b)), and by [[lem:appc-pou]] (b) the sum has at most three nonzero terms,
all on the transition strips of width 2d in ξ or 2d′ in v.

**Lemma {#lem:appc-lipschitz}** (A perturbation bound.) Let 𝒥 ⊂ ℝ^50 be a convex set of 2-jets of the five fields at
a point (values and the nine derivatives of order one and two), on which R, Ω² and e^S are bounded below by positive
numbers, and let E be one of the expressions of [[eq:appc-regular]] (with f_lx, f_nx divided by √w), a polynomial in x
and the jets over a monomial in R, Ω² and e^S. Then for J, J + δJ ∈ 𝒥,

    |E(J + δJ) − E(J)| ≤ Σ_(q=1..50) L_q |δJ_q|,      L_q := sup_(𝒥) |∂E/∂J_q|.

The same holds with 2-jets replaced by (K + 2)-jets and E by any derivative of order at most K of a component in
(t, σ, x), which is again a polynomial in x and the (K + 2)-jets over a monomial in R, Ω² and e^S.

*Proof.* The mean value theorem on the segment from J to J + δJ, which lies in 𝒥. ∎

**Proposition {#prop:appc-overlap}** (The blended residual.) On U_ij, sup |f̃_ab(ĝ)| ≤ sup_𝔅 |f̃_ab(F_ij)| + Λ_ab,
where Λ_ab := Σ_q L_q D_q, D_q is an upper bound on U_ij of the q-th component of the 2-jet of δF, and the L_q are
taken over the convex hull of the 2-jets of F_ij + θδF, 0 ≤ θ ≤ 1, on U_ij. The D_q are bounded by Leibniz's rule from
the bounds φ_k of [[lem:appc-pou]] (a) for the derivatives of χ_(i′) and ψ_(j′) (with the factors (1/(2d))^k and
(1/(2d′))^k of the chain rule), the derivatives of (v − 1/2)^κ, and the sums of the absolute values of the Chebyshev
coefficients of the derivatives of G^F_(i′j′) − G^F_ij on the strips, which are exact by [[lem:appc-reexpand]] (both
polynomials re-expanded in the variables of the strip). The same holds for the derivatives of order at most K, with
(K + 2)-jets.

*Proof.* [[lem:appc-lipschitz]] with J the jet of F_ij and δJ that of δF, at each point of U_ij. ∎

Away from the strips δF = 0 and Λ_ab = 0. On the strips Λ_ab is small because G_(i′j′) − G_ij is: both approximate the
same field to the accuracy of the rule, and the derivatives of the blend, of size φ_k(2d)^(−k), multiply this
difference.

#### The bound in the norm of the continuation argument {#sec:appc-norm}

The certificate of an element is the family of numbers

    B^(ab)_(ij,α) ≥ sup_(U_ij) |∂_t^(α₁)∂_σ^(α₂)∂_x^(α₃) f̃_ab(ĝ)|,   |α| ≤ K,                     {#eq:appc-certificate}

given by [[prop:appc-element-bound]] and [[prop:appc-overlap]], stated rounded upward, where K is the number of
derivatives of the residual that the norm of the continuation argument contains (K = N for a level-N norm). They bound
every quantity that argument uses: the derivatives in (u, v, x) follow by [[eq:tl5-chain]] with the element's chart, and
the Lie derivatives of Ric(ĝ) along the commutation fields of the level-K estimate, weighted by μ^(|I|/2), are explicit
combinations of these derivatives, of f_ab themselves and of the fields' jets, as [[pending:lem-tl5-f3-residual]] states.
With the weight φ of the weighted norm, whose rates are those of [[pending:lem-tl5-l7-rates]], the target of element (i,
j) is

    f_ij := f e^(φ_ij/2),   φ_ij := min over U_ij of φ,                                                 {#eq:appc-target}

where f is the target of the case ([[sec:appc-outcomes]]); since e^(−φ/2) ≤ e^(−φ_ij/2) on U_ij, a pointwise bound f_ij
on U_ij for every element gives the weighted norm of the residual at most the bound that f gives with φ ≡ 0 on the
whole region.

### Certified outcomes {#sec:appc-outcomes}

The targets of a case are one tenth of the bounds its closing needs: for the residual f̃_ab and its derivatives of
order at most 3, unweighted, the target ϱ_t; for the weighted derivatives of order at most 4 of [[sec:appc-norm]], the
target f. The allocated targets f_ij are [[eq:appc-target]], and B_ij is the largest of the weighted certificates
[[eq:appc-certificate]] of element (i, j); B^ϱ_ij is the largest of its unweighted certificates of order at most 3.

    case        ϱ_t          f            elements   B^ϱ_ij against ϱ_t; B_ij against f_ij
    (1, D_A)    10^(−32.3)   10^(−32.2)   2 × 2      ⟨to be entered⟩ [[pending:computational-appc-1a]]
    (2, D*)     10^(−36.9)   10^(−36.4)   2 × 2      ⟨to be entered⟩ [[pending:computational-appc-2d]]
    (1, D*)     10^(−39.6)   10^(−39.5)   3 × 2      ⟨to be entered⟩ [[pending:computational-appc-1d]]

The targets are those of the closing conditions of [[thm:tl5-hfv]] at level four with the constants evaluated for the
three cases [[pending:computational-appc-targets]]. For each element [[sec:appc-spot]] also gives the parameters of its
certificate: the box 𝔅, ρ, N, the coverings of [[lem:appc-analytic]] (i) and (ii), the numbers r_s, q_R and M, and the
numbers B^(ab)_(ij,α).

### Digests and spot values {#sec:appc-spot}

This section gives, for each case, the digests of the rule's output and values at which an execution of the rule can be
checked step by step. Numbers of 𝔽 are given as the integers 2^B x, in decimal.

**The constants of [[def:appc-functions]] and a seed value.** These do not depend on the case:

    π̂              6710401180212168915155840974220003240804194089427148950727106424351713218671805380099500388914024
    L̂₂             1480553391661173448385607439722553250922680800745876974795605978609098082859138712941075737848892
    ξ̂₀             −19448118961787249758697770489485831636681758074956717866260933794473903397724388444760307232329194
    â               4271974071841820164790043412339104229205409044713305539894083215644439451561281100045924173873
    λ̂, 2nd seed    675458408610196755069319590639326181096577024839629319426598901845226755435630329500406877694759
    R_s(ξ̂₀, 1/2)   21888656143208885654860655435538253598689032092399723165933380653658105854163583805362726430717098
    exp 1           5806214745567907793827207199747154474831678955875791827999719186332486788515497861603488166640596
    log 3           2346621606098482852055627154088321384887989782142662884852067216869972863699088419254417012201366
    sin 1           1797371114653268017783996239609576730065324537593303590338720915492505199919304178104972334650448

The last three are values of the functions of [[def:appc-functions]] at 1 and at 3; R_s(ξ̂₀, 1/2) is the radius R_s of
[[def:appc-rule-seed]] at (ξ̂₀, 1/2), the areal radius r_s = 10.2475603901… of the seed at u = −10, v = 1/2 in
[[eq:cone-v]].

**Per case.** For each of the cases (1, D_A), (2, D*) and (1, D*):
- the digest of the case ⟨to be entered⟩;
- for each segment, the digest of its hand-off state ([[def:appc-handoff]]) ⟨to be entered⟩;
- for each block (i, j, F): its digest, the number of nonzero z, the sums S₁, S₂, S₀ of [[eq:appc-sums]], and z₀₀₀,
  z₁₀₀, z₀₁₀, z₀₀₁ ⟨to be entered⟩;
- values in the first cells, as integers 2^B x: R_s at the first node (ξ₀, v₀) of cell (0, 0); G_m and G_R of
  [[def:appc-rule-data]] at the nodes (v_0, x_0) and (v_(p_v), x_0) of row 0, the latter after the N_Ray sweeps; the
  maximum of |r| in each outer step of [[def:appc-iteration]] in cell (0, 0); G^m_(p_ξ p_v 0) of cell (0, 0) and of
  cell (0, 1); and the value Γ^m_000 of the first element ⟨to be entered⟩ [[pending:computational-appc-spot]];
- the parameters of each element's certificate (see [[sec:appc-outcomes]]) ⟨to be entered⟩.

### Placement

This part and the crosswalk rows below are instructions for merging; they are not appendix text. This file revises
the draft Appendix C (P-APPC, unmerged): the tables are not printed, and each case's approximant is defined by the
rule of sec:appc-rule.

*1. Where the appendix goes.* The sections above, from "## Appendix. The certified approximant {#app:approximant}"
through the last line of [[sec:appc-spot]], form a new appendix file placed after the file of Appendix B
([[app:tables]]) and before the references. Its heading has the form "## Appendix. Title {#app:key}" that the assembler
numbers (the draft's "## Appendix C." is not recognised by it). There is no part after the references: the final part
"Tables of the approximant" of the earlier plan does not exist. The appendix defines the labels of the crosswalk rows,
none defined elsewhere; it was checked in a scratch tree with this placement (lint: only the pending markers listed in
item 2; assembler check: no problems).

*2. Pending items.*
- [[pending:lem-tl5-cip-axis]], [[pending:lem-tl5-f3-residual]] and [[pending:lem-tl5-l7-rates]]: as in the draft.
- [[pending:appc-evolution-identity]] (in [[rem:appc-rhs-origin]]): the identity that the sequence of (c) of
  [[def:appc-cell]] evaluates, in exact arithmetic, the solution of the five equations named there for the five second
  derivatives. Neither the definition nor the certificate uses it; it needs a written derivation from [[eq:appc-regular]]
  (exact divisions by 1 ± x and the solution of a 4 × 4 system of determinant −1/(Ω⁸R)), or the remark can be reduced
  to its last two sentences.
- [[pending:computational-appc-parameters]]: the parameters of [[sec:appc-parameters]] are provisional. They are fixed
  once the ratio of the order-3 certificate to the quantum is measured on certified output, and N_o, N_i once
  the iteration's convergence is measured at the production M in every row; the remark [[rem:appc-rule-defined]] is
  then checked by the execution itself.
- [[pending:computational-appc-targets]]: the targets of [[sec:appc-outcomes]] are the level-four rule targets of the
  constants of [[thm:tl5-hfv]] (the stricter of f and ϱ, ϱ in every case), divided by ten. With sec:tl5-hfw merged the
  ϱ coefficient falls by 3.8–5 decades and the stricter target becomes f, near 10^−29.5, 10^−32.6 and 10^−36.0 for
  (1, D_A), (2, D*) and (1, D*); the evaluation of sec:tl5-hfw settles them, the table and the theorem cited are then
  replaced, and the parameters of [[sec:appc-parameters]] are resized to them.
- [[pending:computational-appc-1a]], [[pending:computational-appc-2d]], [[pending:computational-appc-1d]] and
  [[pending:computational-appc-spot]]: the certified outcomes and every ⟨to be entered⟩ slot of [[sec:appc-spot]]
  (digests of the cases, blocks and hand-off states, block sums, spot coefficients, the intermediate values of the first
  cells, and the parameters of each element's certificate). The case-independent spot values are entered.
- [[pending:ref-ieee-754]]: a bibliography entry for the IEEE standard, for example "[IEEE19] IEEE Standard for
  Floating-Point Arithmetic, IEEE Std 754-2019", cited as [IEEE19]. (A title quoted in the references is exempt from the
  word list of the lint; elsewhere the text says "binary64 format" and defines the arithmetic itself.)
- [[pending:ref-fips-180-4]]: a bibliography entry for the Secure Hash Standard, for example "[NIST15] National Institute
  of Standards and Technology, *Secure Hash Standard (SHS)*, Federal Information Processing Standards Publication 180-4
  (2015)", added to the references and cited as [NIST15].

*3a. The level and the contact order.* As in the draft: the bootstrap is at level N ≥ 6 or at level four, the
certificate order K and the contact order κ are parameters, and hypothesis (a) of [[thm:tl5-hf]] on N₀ is either
weakened to a certified mismatch or met by a reference part carrying the solution's v-derivatives of orders 4 to N + 1
on N₀. In the second case the rule must also define those derivatives, by the transport hierarchy along N₀ in the same
arithmetic; that adds one definition to sec:appc-rule.

*3. Other texts.* The introduction lists the appendices; when this appendix is merged, its sentence on [[app:tables]]
(chapter 01, lines 198–200) gains a clause. Old:

[[app:standard-results]] states the results of the literature that the proofs use, each cited with its number and
page where the cited work gives them; [[app:tables]] prints the coefficients of the explicit polynomials, approximants
and enclosures that the proofs use.

New:

[[app:standard-results]] states the results of the literature that the proofs use, each cited with its number and
page where the cited work gives them; [[app:tables]] prints the coefficients of the explicit polynomials, approximants
and enclosures that the proofs use; and [[app:approximant]] defines the approximant of the continuation argument by an
exactly specified rule, with digests of its output, and bounds its residual.

No chapter refers to the final part or to the tables of the approximant. [[rem:tl5-beyond]] and the closing remarks of
[[sec:tl5-beyond]] will cite [[app:approximant]] when the continuation theorem is stated; that change belongs to the
file that states it.

*4. What was dropped from the draft.* sec:appc-format, eq:appc-linecheck and lem:appc-checks (the printed format and
its line checks) and sec:appc-specimen. eq:appc-sums is kept, in [[sec:appc-digest]].

### Crosswalk rows

Rows for the crosswalk of the appendix, in its four columns, separated by tabs, in order. They replace the rows of the
draft; the draft's rows for sec:appc-format, eq:appc-linecheck, lem:appc-checks and sec:appc-specimen are dropped.

    app:approximant	paper/reader/proofs/P-APPC2.md@PENDING:1	P-APPC2, appendix	Appendix C revised: the approximant defined by a rule, no printed tables (author 2026-11-27); S-RULE
    eq:appc-regions	paper/reader/proofs/P-APPC2.md@PENDING:15	P-APPC2, display	D_A and D*; cases (1, D_A), (2, D*), (1, D*)
    sec:appc-definition	paper/reader/proofs/P-APPC2.md@PENDING:21	P-APPC2, section	retitled "The approximant"
    def:appc-layout	paper/reader/proofs/P-APPC2.md@PENDING:27	P-APPC2, Definition	inner nine tenths except at u = -10 and v = 1/2 (layout B)
    eq:appc-element	paper/reader/proofs/P-APPC2.md@PENDING:33	P-APPC2, display	kept from P-APPC
    def:appc-layouts	paper/reader/proofs/P-APPC2.md@PENDING:47	P-APPC2, Definition	layout B: first boxes begin at xi = -1821/200 and v = 1/2
    def:appc-pou	paper/reader/proofs/P-APPC2.md@PENDING:64	P-APPC2, Definition	kept from P-APPC
    eq:appc-pou	paper/reader/proofs/P-APPC2.md@PENDING:70	P-APPC2, display	kept from P-APPC
    lem:appc-pou	paper/reader/proofs/P-APPC2.md@PENDING:74	P-APPC2, Lemma	kept from P-APPC
    def:appc-approximant	paper/reader/proofs/P-APPC2.md@PENDING:92	P-APPC2, Definition	integers given by the rule of sec:appc-rule
    eq:appc-fields	paper/reader/proofs/P-APPC2.md@PENDING:96	P-APPC2, display	kept from P-APPC
    eq:appc-seedform	paper/reader/proofs/P-APPC2.md@PENDING:101	P-APPC2, display	kept from P-APPC
    lem:appc-approximant	paper/reader/proofs/P-APPC2.md@PENDING:110	P-APPC2, Lemma	unchanged in substance
    rem:appc-contact	paper/reader/proofs/P-APPC2.md@PENDING:131	P-APPC2, Remark	rule stated for kappa = 4
    sec:appc-rule	paper/reader/proofs/P-APPC2.md@PENDING:137	P-APPC2, section	new; S-RULE 3.1-3.8
    sec:appc-arith	paper/reader/proofs/P-APPC2.md@PENDING:145	P-APPC2, section	new
    def:appc-arith	paper/reader/proofs/P-APPC2.md@PENDING:147	P-APPC2, Definition	B = 320 fixed point, floor rounding, exact dot products, order conventions
    eq:appc-arith	paper/reader/proofs/P-APPC2.md@PENDING:153	P-APPC2, display	the operations of the rule
    sec:appc-functions	paper/reader/proofs/P-APPC2.md@PENDING:165	P-APPC2, section	new
    def:appc-functions	paper/reader/proofs/P-APPC2.md@PENDING:167	P-APPC2, Definition	exp, sin, cos, log, pi, c(j,n), sinh, cosh, constants a, xi0, lambda
    sec:appc-nodes	paper/reader/proofs/P-APPC2.md@PENDING:195	P-APPC2, section	new
    def:appc-nodes	paper/reader/proofs/P-APPC2.md@PENDING:197	P-APPC2, Definition	Lobatto, Radau, angular nodes; Q, D, W, V, QQ, D1, D2, DCT matrices
    eq:appc-matrices	paper/reader/proofs/P-APPC2.md@PENDING:206	P-APPC2, display	integration and differentiation matrices as floors of exact rationals
    sec:appc-rule-seed	paper/reader/proofs/P-APPC2.md@PENDING:222	P-APPC2, section	new
    def:appc-rule-seed	paper/reader/proofs/P-APPC2.md@PENDING:224	P-APPC2, Definition	seed at a point: bisection and Newton on G(R) = H
    eq:appc-rule-seed	paper/reader/proofs/P-APPC2.md@PENDING:236	P-APPC2, display	seed values R_s, its derivatives, Omega_s^2, d_vW_s, u_xi
    sec:appc-grid	paper/reader/proofs/P-APPC2.md@PENDING:240	P-APPC2, section	new
    def:appc-grid	paper/reader/proofs/P-APPC2.md@PENDING:242	P-APPC2, Definition	cells, breakpoints, segments, nodes, eps powers
    sec:appc-rule-data	paper/reader/proofs/P-APPC2.md@PENDING:263	P-APPC2, section	new
    def:appc-rule-data	paper/reader/proofs/P-APPC2.md@PENDING:265	P-APPC2, Definition	cone data in G-form; Raychaudhuri sweeps for G_R
    eq:appc-rule-cone	paper/reader/proofs/P-APPC2.md@PENDING:275	P-APPC2, display	G_m, G_n, m_3, n_3, shear sigma_6
    eq:appc-rule-ray	paper/reader/proofs/P-APPC2.md@PENDING:286	P-APPC2, display	one Raychaudhuri sweep
    sec:appc-cells	paper/reader/proofs/P-APPC2.md@PENDING:297	P-APPC2, section	new
    def:appc-cell	paper/reader/proofs/P-APPC2.md@PENDING:307	P-APPC2, Definition	boundary term, jets, right-hand side, map, edges
    eq:appc-rule-d	paper/reader/proofs/P-APPC2.md@PENDING:324	P-APPC2, display	the D-quantities
    eq:appc-rhs	paper/reader/proofs/P-APPC2.md@PENDING:650	P-APPC2, display	the right-hand side as a sequence of 236 definitions
    eq:appc-rule-int	paper/reader/proofs/P-APPC2.md@PENDING:662	P-APPC2, display	Goursat integration (row 0 with W, V; rows >= 1 with Q, QQ)
    rem:appc-rhs-origin	paper/reader/proofs/P-APPC2.md@PENDING:679	P-APPC2, Remark	the sequence is the axis-regular evolution system (pending identity); not used
    sec:appc-iteration	paper/reader/proofs/P-APPC2.md@PENDING:686	P-APPC2, section	new
    def:appc-short	paper/reader/proofs/P-APPC2.md@PENDING:691	P-APPC2, Definition	binary64 arithmetic: rounding to nearest even, ordered sums
    eq:appc-short	paper/reader/proofs/P-APPC2.md@PENDING:698	P-APPC2, display	the operations of the short arithmetic
    def:appc-iteration	paper/reader/proofs/P-APPC2.md@PENDING:705	P-APPC2, Definition	defect correction: outer defect steps in B = 320, inner linearised sweeps in binary64
    sec:appc-segments	paper/reader/proofs/P-APPC2.md@PENDING:738	P-APPC2, section	new
    def:appc-resample	paper/reader/proofs/P-APPC2.md@PENDING:740	P-APPC2, Definition	Chebyshev resampling in x between segments
    def:appc-handoff	paper/reader/proofs/P-APPC2.md@PENDING:751	P-APPC2, Definition	hand-off state of a segment and its canonical string
    rem:appc-segments	paper/reader/proofs/P-APPC2.md@PENDING:758	P-APPC2, Remark	why segments
    sec:appc-rule-output	paper/reader/proofs/P-APPC2.md@PENDING:765	P-APPC2, section	new
    def:appc-element-values	paper/reader/proofs/P-APPC2.md@PENDING:767	P-APPC2, Definition	element nodes, cell of a node, interpolation, DCT, z
    eq:appc-rule-z	paper/reader/proofs/P-APPC2.md@PENDING:786	P-APPC2, display	coefficients and the integers z
    sec:appc-parameters	paper/reader/proofs/P-APPC2.md@PENDING:792	P-APPC2, section	new; parameters provisional (pending)
    sec:appc-rule-properties	paper/reader/proofs/P-APPC2.md@PENDING:807	P-APPC2, section	new
    rem:appc-rule-defined	paper/reader/proofs/P-APPC2.md@PENDING:809	P-APPC2, Remark	where the rule is defined
    rem:appc-rule	paper/reader/proofs/P-APPC2.md@PENDING:819	P-APPC2, Remark	order-free, integer-only; zero data give zero
    rem:appc-picard	paper/reader/proofs/P-APPC2.md@PENDING:827	P-APPC2, Remark	plain Picard as an alternative rule
    sec:appc-digest	paper/reader/proofs/P-APPC2.md@PENDING:833	P-APPC2, section	new; replaces sec:appc-format
    def:appc-canonical	paper/reader/proofs/P-APPC2.md@PENDING:838	P-APPC2, Definition	canonical ASCII string of a block and a case
    def:appc-digest	paper/reader/proofs/P-APPC2.md@PENDING:852	P-APPC2, Definition	SHA-256 digests; block sums
    eq:appc-sums	paper/reader/proofs/P-APPC2.md@PENDING:860	P-APPC2, display	moved to sec:appc-digest: the exact block checks
    rem:appc-digest	paper/reader/proofs/P-APPC2.md@PENDING:865	P-APPC2, Remark	what the digest and the sums check
    sec:appc-regular	paper/reader/proofs/P-APPC2.md@PENDING:876	P-APPC2, section	kept from P-APPC
    eq:appc-checked	paper/reader/proofs/P-APPC2.md@PENDING:890	P-APPC2, display	kept from P-APPC
    eq:appc-hat	paper/reader/proofs/P-APPC2.md@PENDING:895	P-APPC2, display	kept from P-APPC
    eq:appc-sigma	paper/reader/proofs/P-APPC2.md@PENDING:903	P-APPC2, display	kept from P-APPC
    lem:appc-regular	paper/reader/proofs/P-APPC2.md@PENDING:905	P-APPC2, Lemma	kept from P-APPC
    eq:appc-regular	paper/reader/proofs/P-APPC2.md@PENDING:912	P-APPC2, display	kept from P-APPC
    eq:appc-sing	paper/reader/proofs/P-APPC2.md@PENDING:950	P-APPC2, display	kept from P-APPC
    sec:appc-certification	paper/reader/proofs/P-APPC2.md@PENDING:988	P-APPC2, section	kept from P-APPC
    sec:appc-exact	paper/reader/proofs/P-APPC2.md@PENDING:998	P-APPC2, section	retitled (no printed coefficients)
    lem:appc-reexpand	paper/reader/proofs/P-APPC2.md@PENDING:1003	P-APPC2, Lemma	kept from P-APPC
    sec:appc-seed	paper/reader/proofs/P-APPC2.md@PENDING:1013	P-APPC2, section	kept from P-APPC
    eq:appc-seed-eq	paper/reader/proofs/P-APPC2.md@PENDING:1017	P-APPC2, display	kept from P-APPC
    eq:appc-seed-jets	paper/reader/proofs/P-APPC2.md@PENDING:1024	P-APPC2, display	kept from P-APPC
    lem:appc-seed-holo	paper/reader/proofs/P-APPC2.md@PENDING:1030	P-APPC2, Lemma	kept from P-APPC
    lem:appc-newton	paper/reader/proofs/P-APPC2.md@PENDING:1038	P-APPC2, Lemma	kept from P-APPC
    sec:appc-box	paper/reader/proofs/P-APPC2.md@PENDING:1051	P-APPC2, section	kept from P-APPC
    lem:appc-analytic	paper/reader/proofs/P-APPC2.md@PENDING:1069	P-APPC2, Lemma	kept from P-APPC
    lem:appc-majorant	paper/reader/proofs/P-APPC2.md@PENDING:1084	P-APPC2, Lemma	kept from P-APPC
    lem:appc-coefficients	paper/reader/proofs/P-APPC2.md@PENDING:1098	P-APPC2, Lemma	kept from P-APPC
    eq:appc-ealpha	paper/reader/proofs/P-APPC2.md@PENDING:1104	P-APPC2, display	kept from P-APPC
    prop:appc-element-bound	paper/reader/proofs/P-APPC2.md@PENDING:1124	P-APPC2, Proposition	kept from P-APPC
    eq:appc-element-bound	paper/reader/proofs/P-APPC2.md@PENDING:1130	P-APPC2, display	kept from P-APPC
    sec:appc-overlaps	paper/reader/proofs/P-APPC2.md@PENDING:1145	P-APPC2, section	kept from P-APPC
    eq:appc-delta	paper/reader/proofs/P-APPC2.md@PENDING:1149	P-APPC2, display	kept from P-APPC
    lem:appc-lipschitz	paper/reader/proofs/P-APPC2.md@PENDING:1154	P-APPC2, Lemma	kept from P-APPC
    prop:appc-overlap	paper/reader/proofs/P-APPC2.md@PENDING:1166	P-APPC2, Proposition	kept from P-APPC
    sec:appc-norm	paper/reader/proofs/P-APPC2.md@PENDING:1181	P-APPC2, section	kept from P-APPC
    eq:appc-certificate	paper/reader/proofs/P-APPC2.md@PENDING:1185	P-APPC2, display	unchanged; certificate numbers stated rounded upward
    eq:appc-target	paper/reader/proofs/P-APPC2.md@PENDING:1195	P-APPC2, display	kept from P-APPC
    sec:appc-outcomes	paper/reader/proofs/P-APPC2.md@PENDING:1201	P-APPC2, section	targets rho_t and f per case (G0h rule targets / 10); outcomes pending
    sec:appc-spot	paper/reader/proofs/P-APPC2.md@PENDING:1218	P-APPC2, section	new; replaces sec:appc-specimen: constants entered, per-case slots pending
