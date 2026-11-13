### The margins of the angle-localised families {#sec:margins}

This section proves the inequalities on which [[pending:thm-bent-slice]] and [[pending:cor-charge-seed]] rest, for the
two-dust background of [[pending:sec-two-dust-background]] with its stated characteristic data, at those data's own
parameters. Three results are proved. [[prop:margins-bend]] and [[cor:margins-lens]] describe the bend of the slice Σ′
and the lens between Σ′ and Σ_τ0. [[thm:margins-hyperbolic]] proves that Rácz's split is hyperbolic on Σ′ ∩ {R ≥ R_*}
with an explicit margin, and locates the band of Σ_τ0 where it fails. [[prop:margins-seed]] bounds Γ/E² from below on
the seed region, for a reference profile and for every profile in a tube around it. Each inequality is reduced to a
finite list of rows, printed in [[sec:table-margins]], and each row is checked by a rule stated here.

*The background.* We recall what is used. The metric is g = −2e^(2s) du dv + R² dΩ₃² on the quotient by the T² action,
the ingoing dust has profile α(v) := 3.6 b(v; 3, 4.5) on 𝒩 := {u = 0}, the outgoing dust has profile B(u) := 1.7 b(u;
5.7, 7.2) on 𝒩′ := {v = 0}, e^(2s) = 1/2 on both cones, and at the corner R = 5, R_u = −0.47, R_v = 1/2, with mass 3/2.
Here b(x; a, c) := β((2x − a − c)/(c − a)) with the bump β of [[sec:table-bump]]. The mass function is μ := R²(1 +
2e^(−2s) R_u R_v). The time v̂ on 𝒩 is fixed by v̂ = 0 at the corner and dv̂/dv = −e^(2s)/R_u on 𝒩, and ψ :=
ln(−e^(2s)/(R_u dv̂/dv)). Then τ := v̂ − R, τ0 := −0.68 and Σ_τ0 := {τ = τ0}. Region I is {u ≤ 5.7}. The proofs use four
identities of the background ([[pending:two-dust-identities]]):

    (S1)  μ_u = −(2/3) B e^(−2s) R_v,   μ_v = −(2/3) α e^(−2s) R_u;      (S2)  R_uv = −e^(2s) μ/R³;
    (S3)  R_vv = −α/(3R²) on 𝒩 and R_uu = −B/(3R²) on 𝒩′;                (S4)  ψ_u = B/(3R² R_u),

and R_u < 0 on the domain. We use the time orientation in which u and v increase to the future. Rácz's quantities on a
round slice are κ (the radial extrinsic curvature) and K^l_l (the trace on the spheres), with the sign conventions of
[[pending:lem-racz-split-formulas]]. The split is hyperbolic where κK^l_l < 0 ([[thm:std-racz-hyperbolic]]). It is not
hyperbolic where κK^l_l > 0: by [Rac16, (4.22), p. 13], the characteristic roots ξ_n of the split at a leaf covector
ξ_S solve K^l_l ξ_n² − 2ξ_n (k·ξ_S) + κ|ξ_S|² = 0, where k is the mixed part of the extrinsic curvature; the leaves are
three-dimensional, so there is ξ_S ≠ 0 with k·ξ_S = 0, and for it the discriminant is −4κK^l_l|ξ_S|² < 0, so the roots
are not real.

### Enclosures and quadrature {#sec:margins-tools}

**Lemma {#lem:margins-enclosure}** (Enclosures and quadrature.)

(a) Let e be an expression in real variables x_1, …, x_n built from constants, +, −, ×, ÷, positive integer powers, exp
and √, and let I_1, …, I_n be closed bounded intervals. Evaluate e with each x_i replaced by I_i and each operation by
its form on intervals: [a, b] + [c, d] = [a + c, b + d]; [a, b] − [c, d] = [a − d, b − c]; [a, b]·[c, d] is the interval
between the least and the greatest of ac, ad, bc, bd; [a, b]/[c, d] = [a, b]·[1/d, 1/c] when 0 ∉ [c, d]; a power [a, b]ⁿ
is the range of t ↦ tⁿ on [a, b]; exp and √ act on the endpoints. If every step is defined, the resulting interval
contains e(x) for every x ∈ I_1 × ⋯ × I_n. This remains true when the lower end of any intermediate interval is
decreased and its upper end increased.

(b) If f ∈ C²[a, b], h := b − a and 0 ≤ s ≤ 1, then |f(a + sh) − (1 − s) f(a) − s f(b)| ≤ (h²/8) sup|f″|. In particular
f ≥ min(f(a), f(b)) − (h²/8) sup|f″| and f ≤ max(f(a), f(b)) + (h²/8) sup|f″| on [a, b].

(c) If f ∈ C²[a, b], then |∫_a^b f − (h/2)(f(a) + f(b))| ≤ (h³/12) sup|f″|. If f ∈ C⁴[a, b], then

    |∫_a^b f − (h/2)(f(a) + f(b)) + (h²/12)(f′(b) − f′(a))| ≤ (h⁴/384) ∫_a^b |f⁗|.   {#eq:margins-hermite}

(d) If α ≥ 0 is continuous, w ∈ C²[a, b], A0 := ∫_a^b α and A1 := ∫_a^b (x − a) α, then

    |∫_a^b α w − w(a) A0 − (w(b) − w(a)) A1/h| ≤ (h²/8) sup|w″| A0.

*Proof.* (a) By induction on e. Each rule returns exactly the set of values of its operation on the product of its
arguments' intervals: a product is bilinear, so its extreme values on a rectangle are at corners; t ↦ 1/t, exp and √ are
monotone on the intervals where they are applied; the power rule is the definition. Enlarging an intermediate interval
keeps the inclusion. (b) Let L be the linear interpolant of f at a and b. For x ∈ (a, b) choose c with F := f − L − c(t
− a)(t − b) vanishing at x; F vanishes at a, x, b, so F″(ξ) = 0 for some ξ, that is f(x) − L(x) = (f″(ξ)/2)(x − a)(x −
b), and (x − a)(b − x) ≤ h²/4. (c) Two integrations by parts give ∫_a^b f − (h/2)(f(a) + f(b)) = −(1/2) ∫_a^b (x − a)(b
− x) f″(x) dx, and ∫_a^b (x − a)(b − x) dx = h³/6. Four integrations by parts give the left side of
[[eq:margins-hermite]] without modulus as (1/24) ∫_a^b (x − a)²(b − x)² f⁗(x) dx, and (x − a)²(b − x)² ≤ h⁴/16. (d) The
function w(a) + (w(b) − w(a))(x − a)/h is the linear interpolant of w; integrate (b) against α ≥ 0. ∎

### The bump {#sec:margins-bump}

**Lemma {#lem:margins-bump}** (The bump.) Let z := 1/(1 − y²) for |y| < 1, and

    q3(z) := z³ − 7z² + (21/2) z − 3,     q4(z) := 4z⁵ − 56z⁴ + 232z³ − 348z² + 195z − 30.

(a) On (−1, 1), β′ = −2yz²β, β″ = 2z²(2z² − 6z + 3)β, β‴ = −8yz³ q3(z) β and β⁗ = 4z³ q4(z) β. Every derivative of β
tends to 0 at ±1, so β ∈ C^∞(ℝ). β is even, 0 ≤ β ≤ 1, and β is increasing on [−1, 0].

(b) β″ vanishes on (−1, 1) exactly at ±y_1, y_1 := 3^(−1/4). So β′ is monotone on [−1, −y_1], [−y_1, y_1] and [y_1, 1],
sup|β′| = |β′(y_1)| ≤ 2.17036, and ∫_(−1)^1 |β″| = 4 sup|β′| ≤ 8.6815.

(c) β‴ vanishes on (−1, 1) exactly at 0, ±y_2 and ±y_3, where z(y_2) ∈ (1.594, 1.595) and z(y_3) ∈ (5.031, 5.032), and
β″ is monotone between consecutive points of −1, −y_3, −y_2, 0, y_2, y_3, 1. Further β″(0) = −2, β″(±y_2) ∈ [−4.181,
−4.136] and β″(±y_3) ∈ [21.039, 21.093]; so sup|β″| ≤ 21.093 and ∫_(−1)^1 |β‴| ≤ 97.1.

(d) β⁗ vanishes on (−1, 1) exactly at ±y_4, ±y_5 and ±y_6, where z(y_4) ∈ (1.300, 1.301), z(y_5) ∈ (3.597, 3.598) and
z(y_6) ∈ (8.039, 8.040), and β‴ is monotone between consecutive points of −1, −y_6, −y_5, −y_4, y_4, y_5, y_6, 1. Its
values satisfy β‴(y_4) ∈ [−6.49, −6.24], β‴(y_5) ∈ [216.8, 219.7] and β‴(y_6) ∈ [−507.6, −505.7]; so sup|β‴| ≤ 507.6 and
∫_(−1)^1 |β⁗| ≤ 2936.

*Proof.* (a) Differentiate β = e^(1−z) with z′ = 2yz² and remove even powers of y by y² = 1 − 1/z; for instance β″ =
(4y²z⁴ − 2z² − 8y²z³)β = 2z²(2z² − 6z + 3)β, and the third and fourth derivatives follow in the same way. Each
derivative is a polynomial in y and z times e^(1−z), and z^m e^(1−z) → 0 as z → ∞. Evenness, the bounds and the
monotonicity follow from β = e^(1−z) with z increasing in |y|.

(b) 2z² − 6z + 3 has the roots (3 ± √3)/2, and only (3 + √3)/2 exceeds 1; it gives y² = 1 − 2/(3 + √3) = 3^(−1/2).
There |β′| = 2·3^(−1/4)·((3 + √3)/2)²·e^(−(1+√3)/2) = 2.170357…. On the three pieces β′ runs from 0 to its maximum, from
its maximum to its minimum −sup|β′|, and back to 0; its total variation, which is ∫|β″|, is 4 sup|β′|.

(c) q3(0) = −3, q3(1/2) = 5/8, q3(1.594) = 0.0012406 > 0, q3(1.595) = −0.0029551 < 0, q3(5.031) = −0.0117822 < 0 and
q3(5.032) = 0.0042248 > 0, so the cubic q3 has exactly one root in each of (0, 1/2), (1.594, 1.595) and (5.031, 5.032);
only the last two exceed 1. With y = 0 (the factor y of β‴) these give the zeros. On z ∈ [1.594, 1.595] and z ∈ [5.031,
5.032], [[lem:margins-enclosure]] (a) applied to 2z²(2z² − 6z + 3)e^(1−z) gives the stated intervals. As β″ is even and
monotone on the pieces, its total variation on [−1, 1] is 2(|β″(y_2) − β″(0)| + |β″(y_3) − β″(y_2)| + |β″(y_3)|) ≤
2(2.181 + 25.274 + 21.093) ≤ 97.1.

(d) q4(0) = −30, q4(1/2) = 49/8, q4(1) = −3, q4(1.300) = −0.00588, q4(1.301) = 0.025631, q4(3.597) = 0.052921,
q4(3.598) = −0.327578, q4(8.039) = −5.84132 and q4(8.040) = 0.897867: five sign changes of a quintic, so exactly one
root in each interval and no other. On the three z-intervals [[lem:margins-enclosure]] (a) applied to −8yz³q3(z)e^(1−z),
y = (1 − 1/z)^(1/2), gives the stated values. They alternate in sign, and β‴ is odd with β‴(0) = β‴(±1) = 0, so its
total variation on [0, 1] is |e_4| + (|e_4| + |e_5|) + (|e_5| + |e_6|) + |e_6| with e_i := β‴(y_i), at most 2(6.49 +
219.7 + 507.6) ≤ 1467.6, and on [−1, 1] at most 2936. ∎

**Lemma {#lem:margins-bump-table}** (The bump table.) Let C, D, C̃_j and D̃_j be as in [[sec:table-bump]], δ = 1/20, and
K := ∫_(−1)^1 β.

(a) |C(y_j) − C̃_j| ≤ 5 × 10⁻⁵ and |D(y_j) − D̃_j| ≤ 10⁻⁴ for 0 ≤ j ≤ 40; in particular |K − 1.2069048544| ≤ 5 × 10⁻⁵.

(b) For y_j ≤ y ≤ y_(j+1),

    |C(y) − C̃_j − (y − y_j)(β(y_j) + β(y))/2| ≤ 2.7 × 10⁻⁴,
    |D(y) − D̃_j − (y − y_j) C̃_j − (y − y_j)² β(y_j)/2| ≤ 1.5 × 10⁻⁴,

and for y ≥ 1, C(y) = K and D(y) = yK.

(c) Let φ be the bend of [[prop:margins-bend]] and, for its three lobes X with half-width h_X, centre c_X and weight ε_X
(ε = 1 for the central lobe, −l1 and −l2 for the others), y_X := (R − c_X)/h_X. Then φ′(R) = 0.01 Σ_X ε_X h_X C(y_X) and
φ(R) = 0.01 Σ_X ε_X h_X² D(y_X). Evaluating C and D by (b) gives φ′(R) to within 1.7 × 10⁻⁶ and φ(R) to within 10⁻⁶.

*Proof.* (a) The recursion for C̃ applies [[eq:margins-hermite]] to f = β on each [y_j, y_(j+1)]. Summing, |C(y_j) −
C̃_j| ≤ (δ⁴/384) ∫|β⁗| + 40 × 5 × 10⁻¹¹ ≤ 2936/(384 × 20⁴) + 2 × 10⁻⁹ ≤ 4.8 × 10⁻⁵ by [[lem:margins-bump]] (d), the
second term accounting for the rounding of the printed values. The recursion for D̃ applies [[eq:margins-hermite]] to
f = C, with f′ = β and f⁗ = β‴, but with C̃ in place of C. So |D(y_j) − D̃_j| is at most (δ⁴/384) ∫|β‴| plus δ times the
sum over i < j of the larger error of C̃ at y_i and y_(i+1), that is at most 1.6 × 10⁻⁶ + 40δ × 4.8 × 10⁻⁵ ≤ 10⁻⁴, using
[[lem:margins-bump]] (c).

(b) By [[lem:margins-enclosure]] (c), |∫_(y_j)^y β − (y − y_j)(β(y_j) + β(y))/2| ≤ (δ³/12) × 21.093 ≤ 2.2 × 10⁻⁴; add
(a). Next D(y) = D(y_j) + (y − y_j) C(y_j) + ∫_(y_j)^y (y − s) β(s) ds, and |∫_(y_j)^y (y − s)(β(s) − β(y_j)) ds| ≤
sup|β′| ∫_(y_j)^y (y − s)(s − y_j) ds ≤ 2.1704 δ³/6 ≤ 4.6 × 10⁻⁵; add (a) and δ × 5 × 10⁻⁵. For y ≥ 1, C(y) = K, and
D(y) = yK − ∫ sβ(s) ds = yK because β is even. (c) The formulas follow from φ(R) = ∫_(3.5)^R (R − t) φ″(t) dt and the
substitution t = c_X + h_X s. The error in φ′ is at most 0.01 (h_P + l1 h_L + l2 h_R) × 2.7 × 10⁻⁴ ≤ 1.7 × 10⁻⁶. For φ,
a lobe in progress contributes at most 0.01 h_X² × 1.5 × 10⁻⁴ and a completed lobe, where D = y_X K with |y_X| ≤ 7.2, at
most 0.01 h_X² × 7.2 × 5 × 10⁻⁵; in all at most 0.01 (0.09 × 2.3 × 10⁻⁴ + 0.0487 × 3.6 × 10⁻⁴ + 0.05533 × 1.5 × 10⁻⁴) ≤
10⁻⁶. ∎

### The bend {#sec:margins-bend}

**Proposition {#prop:margins-bend}** (The bend.) Let l1 := 432/671, l2 := 50/183, and let φ be the function with φ(R) =
0 for R ≤ 3.5 and

    φ″(R) = 0.01 (b(R; 4.1, 4.7) − l1 b(R; 3.5, 4.05) − l2 b(R; 4.85, 5.75)).   {#eq:margins-bend}

(a) The three lobes have half-widths h_L = 11/40, h_P = 3/10, h_R = 9/20 and centres c_L = 151/40, c_P = 22/5, c_R =
53/10. The numbers l1, l2 are the unique ones for which ∫φ″ = ∫ R φ″ dR = 0, namely

    l1 = (h_P/h_L)(c_R − c_P)/(c_R − c_L) = 0.6438152011922503…,
    l2 = (h_P/h_R)(c_P − c_L)/(c_R − c_L) = 0.27322404371584699….

Hence φ = φ′ = 0 outside [3.5, 5.75].

(b) φ ≤ 0. There is x* ∈ (4.415, 4.445) with φ′ < 0 on (3.5, x*) and φ′ > 0 on (x*, 5.75), and

    0.0011590 ≤ max|φ| = −φ(x*) ≤ 0.0011596;

so max|φ| = 0.00116 to three significant figures.

(c) |φ′| ≤ 0.0021370, |φ″| ≤ 0.01, |φ‴| ≤ 0.072346 and |φ⁗| ≤ 2.3437.

*Proof.* (a) Each lobe is a translate and dilate of the even bump β, so ∫ b(R; a, c) dR = hK and ∫ R b(R; a, c) dR =
c′hK for the lobe of half-width h and centre c′. The two conditions read l1 h_L + l2 h_R = h_P and l1 c_L h_L + l2 c_R
h_R = c_P h_P; K cancels. The determinant is h_L h_R (c_R − c_L) ≠ 0, and Cramer's rule gives the formulas: l1 = (12/11)
(9/10)(40/61) = 432/671 and l2 = (2/3)(5/8)(40/61) = 50/183. For R ≥ 5.75, φ′(R) = ∫φ″ = 0 and φ(R) = ∫ (R − t) φ″(t)
dt = R ∫φ″ − ∫ t φ″ = 0.

(b) The lobes have disjoint supports, so φ″ < 0 on (3.5, 4.05) and on (4.85, 5.75), φ″ > 0 on (4.1, 4.7), and φ″ = 0
elsewhere. Hence φ′ falls from 0 to −0.01 l1 h_L K < 0 on [3.5, 4.05], is constant up to 4.1, rises on [4.1, 4.7] to
0.01(h_P − l1 h_L)K = 0.01 h_P (25/61) K > 0, is constant up to 4.85, and falls to φ′(5.75) = 0. So φ′ has a single zero
x* ∈ (4.1, 4.7), φ falls from 0 to φ(x*) and rises back to φ(5.75) = 0, and φ ≤ 0. On [4.1, 4.7] the left lobe is
complete, so

    φ(R) = 0.01 (h_P² D(y_P) − l1 h_L K (R − c_L)),     y_P := (R − c_P)/h_P,

with l1 h_L = 54/305. At R = 4.415, 4.43 and 4.445 (y_P = y_21, y_22, y_23) the table gives, with K̃ := C̃_40,

    0.01 (0.09 D̃_j − (54/305) K̃ (R − c_L)) = −0.0011576361,  −0.0011591651,  −0.0011584676,

and by [[lem:margins-bump-table]] (a) the true values differ from these by at most 0.01(0.09 × 10⁻⁴ + (54/305) × 0.67 ×
5 × 10⁻⁵) ≤ 1.5 × 10⁻⁷. So φ(4.43) < min(φ(4.415), φ(4.445)), and as φ is convex on [4.1, 4.7] its minimum point x* lies
in (4.415, 4.445). There [[lem:margins-enclosure]] (b), with h = 0.015 and sup|φ″| ≤ 0.01, so that (h²/8) sup|φ″| ≤
2.82 × 10⁻⁷, gives φ ≥ −0.0011591651 − 1.5 × 10⁻⁷ − 2.82 × 10⁻⁷ = −0.0011595971 ≥ −0.0011596, while φ(4.43) ≤
−0.0011591651 + 1.5 × 10⁻⁷ ≤ −0.0011590.

(c) By the description of φ′ in (b), |φ′| ≤ 0.01 (54/305) K ≤ 0.0021370 by [[lem:margins-bump-table]] (a). Since the
lobes are disjoint, |φ^(k)| on the lobe of half-width h and weight c ∈ {1, l1, l2} is at most 0.01 c
sup|β^(k−2)|/h^(k−2); by [[lem:margins-bump]] the largest of these is 0.01 × 2.17036 × (10/3) for k = 3 and 0.01 ×
21.093 × (100/9) for k = 4. ∎

### Region I and the data on the shell {#sec:margins-region-one}

**Lemma {#lem:margins-region-one}** (Region I.)

(a) On region I the background is ingoing Vaidya in the chart (v̂, R):

    g = −f dv̂² + 2 dv̂ dR + R² dΩ₃²,     f := 1 − μ(v̂)/R²,   {#eq:margins-vaidya}

where μ(v̂) is the mass at the point of 𝒩 with time v̂. The function μ is nondecreasing; μ = 3/2 for v ≤ 3, μ is
constant for v ≥ 4.5, and μ ≤ 3.6059 everywhere.

(b) Let F(r) := 2r + √(3/2) ln((r − √(3/2))/(r + √(3/2))) and τ_ray(R) := F(R) − F(2.321) − R. Where v̂ ≤ v̂(v = 3) the
null ray u = 5.7 is {τ = τ_ray(R)}. Since τ_ray(3.43718) = −0.68000009 and τ_ray(3.43719) = −0.67998718, it crosses Σ_τ0
at a single radius R_* ∈ (3.43718, 3.43719), with v̂ = τ0 + R_* < 2.7572 < v̂(v = 3) = 3.14533. This R_* is the radius
of [[lem:bg-rstar]], which encloses it in [3.43718006, 3.43718007].

(c) Every point with R ≥ R_* and τ ≤ τ0 lies in region I. In particular Σ_τ0 ∩ {R ≥ R_*}, Σ′ ∩ {R ≥ R_*} and every point
with R ≥ R_* between Σ′ and Σ_τ0 do.

*Proof.* (a) In region I, B = 0, so μ_u = 0 by (S1) and ψ_u = 0 by (S4). Thus μ is constant along ingoing rays, equal to
its value on 𝒩, and ψ = 0, its value on 𝒩. With dv̂ = −(e^(2s)/R_u) dv (which is ψ = 0) and du = (dR − R_v dv)/R_u, the
quotient metric is −2e^(2s) du dv = 2 dv̂ dR + 2e^(−2s) R_u R_v dv̂², and 2e^(−2s) R_u R_v = μ/R² − 1 by the definition
of μ. On 𝒩, μ_v = −(2/3)α e^(−2s) R_u ≥ 0 with α = 0 outside (3, 4.5); the bound μ ≤ 3.6059 is
[[lem:margins-shell-data]] (c) at v = 4.5.

(b) For v̂ ≤ v̂(v = 3), μ = 3/2. The ray u = 5.7 starts on 𝒩′, where v̂ = 0 and, by (S3) with B = 0 for u ≤ 5.7, R = 5 −
0.47 u, so R = 2.321. Outgoing null rays of [[eq:margins-vaidya]] satisfy dv̂/dR = 2/f, and F′(r) = 2r²/(r² − 3/2) is
2/f for μ = 3/2; so v̂ = F(R) − F(2.321) on the ray. The values of τ_ray are direct evaluations, and τ_ray is increasing
by (c) below. Finally v̂(v = 3) is v̂_0 of [[sec:table-shell]].

(c) Along an outgoing null ray of [[eq:margins-vaidya]], dτ/dR = 2/f − 1 > 0 where 0 < f < 2. On the ray u = 5.7 at R ≥
R_*, f ≥ 1 − 3.6059/R_*² > 0 since R_*² > 11.81. So the ray's τ, as a function of R, is increasing on [R_*, ∞) and at
least τ0 there; equivalently its time v̂_ray(R) satisfies v̂_ray(R) ≥ τ0 + R. Let p have R_p ≥ R_* and τ_p ≤ τ0. Then
v̂_ray(R_p) ≥ τ0 + R_p ≥ v̂_p, so the ingoing ray v̂ = v̂_p meets u = 5.7 at a radius R_1 ≤ R_p. Along an ingoing ray u
decreases as R increases (R_u < 0), so u(p) ≤ 5.7. Points of Σ′ have τ = τ0 + φ(R) ≤ τ0 by [[prop:margins-bend]] (b),
and points between the two slices have τ0 + φ(R) ≤ τ ≤ τ0. ∎

**Corollary {#cor:margins-lens}** (The lens.) Let Σ′ := {v̂ − R − φ(R) = τ0}. Then Σ′ = Σ_τ0 outside R ∈ [3.5, 5.75],
and Σ′ lies to the past of Σ_τ0 where they differ, at τ-distance at most max|φ| ≤ 0.0011596. Let γ be a causal curve
joining a point p of Σ′ with R_p ≥ R_* to a point q of Σ_τ0. Then γ lies in region I. If γ is not constant, it runs to
the future from p to q, every point of γ other than q has R ∈ (3.5, 5.75), and the angular displacement of γ on the
unit sphere S³ is at most 3.25 × 10⁻⁴. A causal curve joining a point of Σ′ with R < R_* to a point q of Σ_τ0 has R_q <
R_*, and there Σ′ = Σ_τ0. So carrying a domain of influence from one slice to the other widens its angular support by
at most 3.3 × 10⁻⁴ rad.

*Proof.* On Σ′, τ = τ0 + φ(R). By [[prop:margins-bend]], φ = 0 outside [3.5, 5.75], and φ < 0 on (3.5, 5.75), since φ
strictly decreases from φ(3.5) = 0 on [3.5, x*] and strictly increases to φ(5.75) = 0 on [x*, 5.75]. This gives the
first two statements.

*Time functions in region I.* With τ = v̂ − R, [[eq:margins-vaidya]] reads g = −f dτ² + 2(1 − f) dτ dR + (2 − f) dR² +
R² dΩ₃², whose inverse on the (τ, R) plane has g^(ττ) = −(2 − f), g^(τR) = 1 − f and g^(RR) = f. So g⁻¹(dτ, dτ) = −(2 −
f) < 0, since f < 1. Where φ′ ≠ 0, R ∈ (3.5, 5.75) and 0 < f < 1 (μ ≤ 3.6059 < 3.5²), so with |φ′| ≤ 0.0022,
g⁻¹(d(τ − φ), d(τ − φ)) = −(2 − f) − 2(1 − f)φ′ + fφ′² ≤ −1 + 2 × 0.0022 + 0.0022² < 0; where φ′ = 0 it is −(2 − f).
So dτ and d(τ − φ) are timelike on region I. The vector −∂_R of the chart (v̂, R) is null and future directed: it is
tangent to an ingoing ray, along which u increases as R decreases, because R_u < 0. On it dτ and d(τ − φ) take the
values 1 and 1 + φ′, both positive. A timelike covector does not vanish on a nonzero causal vector, so it has one sign
on the future causal vectors; hence τ and τ − φ(R) increase strictly along every future causal curve in region I that
is not constant.

*Where γ lies.* Along a future causal curve u and v do not decrease, and v̂ is an increasing function of v (dv̂/dv =
−e^(2s)/R_u > 0); so v̂ does not decrease. Let γ join p ∈ Σ′, R_p ≥ R_*, to q ∈ Σ_τ0. The point p lies in region I by
[[lem:margins-region-one]] (c), which settles a constant γ; suppose γ is not constant. If γ runs to the future from q to
p, then u ≤ u(p) ≤ 5.7 along γ, so γ lies in region I; there τ increases strictly from τ(q) = τ0 to τ(p) = τ0 +
φ(R_p) ≤ τ0, which is impossible. So γ runs to the future from p to q. Then τ0 + R_q = v̂(q) ≥ v̂(p) = τ0 + R_p +
φ(R_p). If R_p ≥ 3.5, this gives R_q ≥ 3.5 − 0.0011596 > R_*; if R_* ≤ R_p < 3.5, then φ(R_p) = 0 and R_q ≥ R_p ≥ R_*.
In either case q lies in region I by [[lem:margins-region-one]] (c), so u(q) ≤ 5.7, and u ≤ u(q) along γ: γ lies in
region I. There τ − φ(R) increases strictly from τ0 at p, and τ increases strictly to τ0 at q. So at every point of γ
other than q, φ(R) ≤ τ − τ0 < 0, which forces R ∈ (3.5, 5.75).

*The angular displacement.* A causal vector (τ̇, Ṙ, Ω̇) satisfies

    R²|Ω̇|² ≤ f τ̇² − 2(1 − f) τ̇ Ṙ − (2 − f) Ṙ² ≤ τ̇²/(2 − f),

the right-hand bound being the maximum over Ṙ. At the points of γ other than q, μ ≥ 3/2 and 3.5 < R < 5.75, so 2 − f
= 1 + μ/R² ≥ 1 + 1.5/5.75² ≥ 1.045368 and √(2 − f) ≥ 1.02243. Hence |Ω̇| ≤ τ̇/(3.5 × 1.02243) ≤ τ̇/3.5785, and the
angular displacement is at most (τ0 − τ(p))/3.5785 = −φ(R_p)/3.5785 ≤ 0.0011596/3.5785 ≤ 3.25 × 10⁻⁴.

*Below R_*.* Let a causal curve join p ∈ Σ′ with R_p < R_* to q ∈ Σ_τ0; then φ(R_p) = 0, so p ∈ Σ_τ0. Suppose R_q ≥
R_*, so that q lies in region I. If the curve runs to the future from p to q, then u ≤ u(q) ≤ 5.7 along it, it lies in
region I, and τ(p) = τ0 = τ(q) forces it to be constant, against R_p ≠ R_q. If it runs to the future from q to p, then
v̂(p) ≥ v̂(q) gives R_p ≥ R_q ≥ R_*, again a contradiction. So R_q < R_*. ∎

**Lemma {#lem:margins-shell-data}** (The data on the shell.) On 𝒩 put P := R_v, write ′ for d/dv, and let f_N := 1 −
μ/R², w := f_N/(3P) and g := 2P/f_N along 𝒩. For 3 ≤ v ≤ 4.5,

    R′ = P,    P′ = −α/(3R²),    μ′ = α w,    v̂′ = g,   {#eq:margins-ode}

with R = 13/2, P = 1/2, μ = 3/2 and v̂ = v̂_0 at v = 3 (v̂_0 as in [[sec:table-shell]]). Moreover

    w′ = 2μ/(3R³),    g′ = −4μP²/(f_N² R³),    dμ/dv̂ = (3/2) α w².   {#eq:margins-rates}

(a) For 3 ≤ v ≤ 4.5: 0.47428 ≤ P ≤ 1/2, 13/2 ≤ R ≤ 29/4, 3/2 ≤ μ ≤ 3.79034, 0.91028 ≤ f_N ≤ 0.97147 and 0.60685 ≤ w ≤
0.70282.

(b) Let h := 1/80, v_k := 3 + kh, α_k := α(v_k), α′_k := α′(v_k), and

    Ã0_k := (h/2)(α_k + α_(k+1)) − (h²/12)(α′_(k+1) − α′_k),
    Ã1_k := (h²/2) α_(k+1) − (h²/12)(α_(k+1) − α_k + h α′_(k+1)).

The rows (R_k, P_k, μ_k, v̂_k) of [[sec:table-shell]] satisfy

    R_(k+1) = R_k + (h/2)(P_k + P_(k+1)),
    P_(k+1) = P_k − (1/3)(Ã0_k/R_k² + (1/R_(k+1)² − 1/R_k²) Ã1_k/h),
    μ_(k+1) = μ_k + w_k Ã0_k + (w_(k+1) − w_k) Ã1_k/h,   {#eq:margins-scheme}
    v̂_(k+1) = v̂_k + (h/2)(g_k + g_(k+1)),

with w_k, g_k evaluated on row k, up to residuals r_k of modulus at most 10⁻⁸ in each line, whose sums over k = 0, …,
119 are at most 5 × 10⁻⁷ in each line.

(c) For every k, |R(v_k) − R_k| ≤ 4 × 10⁻⁶, |P(v_k) − P_k| ≤ 6 × 10⁻⁷, |μ(v_k) − μ_k| ≤ 10⁻⁵ and |v̂(v_k) − v̂_k| ≤ 4 ×
10⁻⁶.

*Proof.* Put Q := R_u on 𝒩, where e^(2s) = 1/2. Then (S3) gives P′ = −α/(3R²); the definition of μ gives μ = R²(1 +
4QP), so Q = −f_N/(4P); (S1) gives μ′ = −(4/3)αQ = αw; and dv̂/dv = −e^(2s)/R_u = −1/(2Q) = g. Before the shell α = 0,
so R = 5 + v/2, P = 1/2 and μ = 3/2, and v̂(3) = ∫_5^(13/2) 2/f_N dR = F(13/2) − F(5) = v̂_0. Next, f_N′ = −αw/R² +
2μP/R³ gives w′ = (f_N′ P − f_N P′)/(3P²) = −αw/(3PR²) + 2μ/(3R³) + f_N α/(9P²R²), and the first and last terms cancel
because f_N/(3P) = w. Likewise g′ = 2P′/f_N − 2P f_N′/f_N² = −2α/(3R² f_N) + 2Pαw/(R² f_N²) − 4μP²/(R³ f_N²), and
2Pw/f_N² = 2/(3f_N) cancels the first term. Finally dμ/dv̂ = μ′/g = αw f_N/(2P) = (3/2)αw².

(a) P′ ≤ 0, so P ≤ 1/2, and while P > 0, R ≥ 13/2. Then P ≥ 1/2 − (1/3) ∫α/R² ≥ 1/2 − 2.7K/126.75 ≥ 0.47428, because
∫α = 3.6 × 0.75 K and K ≤ 1.2069549 by [[lem:margins-bump-table]] (a). So R ≤ 13/2 + (3/2)(1/2) = 29/4. While f_N > 0,
μ′ ≥ 0 and w ≤ 1/(3 × 0.47428) ≤ 0.70282, so μ ≤ 3/2 + 0.70282 × 3.25878 ≤ 3.79034 and f_N ≥ 1 − 3.79034/42.25 ≥
0.91028 > 0; this closes the argument. The remaining bounds follow from f_N ≤ 1 − 1.5/R² ≤ 1 − 1.5/(29/4)².

(b) is a row-by-row check of [[sec:table-shell]], with α_k and α′_k from [[lem:margins-bump]] (a).

(c) For the true solution, let A0_k := ∫ α and A1_k := ∫ (v − v_k) α over [v_k, v_(k+1)]. By [[lem:margins-enclosure]]
(c) and (d), the true values satisfy the four lines of [[eq:margins-scheme]] with A0_k, A1_k in place of Ã0_k, Ã1_k, up
to errors τ^R_k, τ^P_k, τ^μ_k, τ^v_k with

    |τ^R_k| ≤ (h³/12) sup|P″|,   |τ^P_k| ≤ (h²/24) sup|(R⁻²)″| A0_k,
    |τ^μ_k| ≤ (h²/8) sup|w″| A0_k,   |τ^v_k| ≤ (h³/12) sup|g″|.

On the box (a), P″ = −α′/(3R²) + 2αP/(3R³) gives |P″| ≤ 10.4178/126.75 + 3.6/823.875 ≤ 0.0866 (sup|α′| = 4.8 sup|β′| ≤
10.4178); (R⁻²)″ = 6P²/R⁴ + 2α/(3R⁵) ≤ 0.00105; w″ = 2αw/(3R³) − 2μP/R⁴ gives |w″| ≤ 0.00827; and differentiating g′
with [[eq:margins-ode]] gives |g″| ≤ 4(0.6326 + 0.1077 + 0.1535 + 0.2187)/(0.9102² × 274.625) ≤ 0.0196, the four terms
bounding μ′P², 2μP|P′|, 2μP²|f_N′|/f_N and 3μP³/R. By [[eq:margins-hermite]] applied to α and to (v − v_k)α, |A0_k −
Ã0_k| ≤ (h⁴/384) ∫|α⁗| and |A1_k − Ã1_k| ≤ (h⁴/384)(4 ∫|α‴| + h ∫|α⁗|), integrals over the cell; summed over k, with
∫|α⁗| = 3.6 (4/3)³ ∫|β⁗| ≤ 25054 and ∫|α‴| = 3.6 (4/3)² ∫|β‴| ≤ 622, these are at most 1.6 × 10⁻⁶ and 1.8 × 10⁻⁷. Let
e^X_k be the true value minus the row value, for X = R, P, μ, v̂, so e_0 = 0. On the box (a), which contains the rows,
the Lipschitz bounds are |Δ(R⁻²)| ≤ 0.0072827|ΔR|, |Δw| ≤ 0.016635|Δμ| + 0.019401|ΔR| + 1.43959|ΔP| and |Δg| ≤
2.19713|ΔP| + 0.028565|Δμ| + 0.033314|ΔR|; also R⁻² ≤ 1/42.25, |(R⁻²)′| ≤ 0.0036414 and |w′| ≤ 0.00921. Subtracting the
row relations from the true ones,

    |e^R_(k+1)| ≤ |e^R_k| + (h/2)(|e^P_k| + |e^P_(k+1)|) + |τ^R_k| + |r^R_k|,
    |e^P_(k+1)| ≤ |e^P_k| + 0.0024276 ((|Ã0_k| + |Ã1_k|/h)|e^R_k| + (|Ã1_k|/h)|e^R_(k+1)|) + m^P_k + |τ^P_k| + |r^P_k|,
    |e^μ_(k+1)| ≤ |e^μ_k| + (|Ã0_k| + |Ã1_k|/h)|Δw_k| + (|Ã1_k|/h)|Δw_(k+1)| + m^μ_k + |τ^μ_k| + |r^μ_k|,
    |e^v_(k+1)| ≤ |e^v_k| + (h/2)(|Δg_k| + |Δg_(k+1)|) + |τ^v_k| + |r^v_k|,

where m^P_k := (1/3)(|A0_k − Ã0_k|/42.25 + 0.0036414 |A1_k − Ã1_k|) and m^μ_k := 0.70282 |A0_k − Ã0_k| + 0.00921 |A1_k −
Ã1_k|. Let E^X be the largest |e^X_k|. Summing from 0 and using Σ_k (|Ã0_k| + 2|Ã1_k|/h) ≤ 6.52 (from the table) and Σ_k
h = 3/2, the sources are S^R ≤ 1.70 × 10⁻⁶ + 5 × 10⁻⁷, S^P ≤ 3.6 × 10⁻⁸ + 5 × 10⁻⁷, S^μ ≤ 1.66 × 10⁻⁶ + 5 × 10⁻⁷ and
S^v ≤ 3.9 × 10⁻⁷ + 5 × 10⁻⁷, and

    E^R ≤ S^R + 1.5 E^P,   E^P ≤ S^P + 0.015828 E^R,   E^μ ≤ S^μ + 6.52 (0.016635 E^μ + 0.019401 E^R + 1.43959 E^P),
    E^v ≤ S^v + 1.5 (2.19713 E^P + 0.028565 E^μ + 0.033314 E^R).

The first two give E^P ≤ (S^P + 0.015828 S^R)/(1 − 0.023742) ≤ 5.9 × 10⁻⁷ and E^R ≤ 3.1 × 10⁻⁶; then E^μ ≤ (S^μ +
6.52(0.019401 E^R + 1.43959 E^P))/(1 − 0.108461) ≤ 9.1 × 10⁻⁶ and E^v ≤ 3.4 × 10⁻⁶. ∎

### Rácz's quantities in region I {#sec:margins-racz}

**Lemma {#lem:margins-racz}** (Round slices of region I.) In the chart [[eq:margins-vaidya]], let v̂ = V(R) be a round
slice with V′ > 0 and fV′ < 2, write μ̇ := dμ/dv̂, and put

    Ξ := V″ + (μ/R³) V′²(3 − fV′) − μ̇ V′³/(2R²).   {#eq:margins-xi}

Then κ′ = Ξ/(V′(2 − fV′))^(3/2) and K′^l_l = 3(fV′ − 1)/(R (V′(2 − fV′))^(1/2)), so

    κ′ K′^l_l = −c Ξ,     c := 3(1 − fV′)/(R V′² (2 − fV′)²).

On Σ_τ0 (V′ = 1, V″ = 0) this is κ = −N_κ/(2 − f)^(3/2) and K^l_l = 3(f − 1)/(R(2 − f)^(1/2)), with

    N_κ := (μ/R³)(f − 3) + μ̇/(2R²) = −2μ/R³ − μ²/R⁵ + μ̇/(2R²).

*Proof.* With T := V′∂_v̂ + ∂_R tangent to the slice, g(T, T) = V′(2 − fV′) > 0 and the normal covector dv̂ − V′dR has
g⁻¹-norm −V′(2 − fV′); let n be the unit normal with n_♭ = −(dv̂ − V′dR)/(V′(2 − fV′))^(1/2). The Christoffel symbols of
the (v̂, R) part are Γ_(v̂,v̂v̂) = −f_v̂/2, Γ_(v̂,v̂R) = −f_R/2, Γ_(R,v̂v̂) = f_R/2 and zero otherwise (first index
lowered), with f_v̂ = −μ̇/R² and f_R = 2μ/R³. With n^v̂ = V′/(V′(2 − fV′))^(1/2) and n^R = (fV′ − 1)/(V′(2 −
fV′))^(1/2), κ′ := −g(∇_T T, n)/g(T, T) has numerator V″ + f_v̂ V′³/2 + f_R V′² − (fV′ − 1) f_R V′²/2 = Ξ, divided by
(V′(2 − fV′))^(1/2) g(T, T). The trace on the spheres is K′^l_l = 3n^R/R. At V′ = 1, V″ = 0 these are the formulas of
[[pending:lem-racz-split-formulas]] with ψ = 0, which fixes the signs. ∎

On Σ′ the slice is V(R) = τ0 + R + φ(R), so V′ = 1 + φ′ ∈ [0.99786, 1.00149] and V″ = φ″ by [[prop:margins-bend]], and Ξ
= φ″ + (μ/R³)V′²(3 − fV′) − μ̇V′³/(2R²). On Σ′ ∩ {R ≥ R_*}, which lies in region I by [[lem:margins-region-one]] (c), μ
≥ 3/2, so f ≤ 1 − 3/(2R²); with V′ ≤ 1.00149, and V′ = 1 for R ≥ 5.75, this gives fV′ < 1 on Σ′ ∩ {R ≥ R_*}, so K′^l_l <
0 there, and κ′ > 0 exactly where Ξ > 0.

### Hyperbolicity on R ≥ R_* {#sec:margins-hyperbolic}

For 3 ≤ v ≤ 4.5, the ingoing ray v meets Σ_τ0 at R0(v) := v̂(v) − τ0 and Σ′ at the radius R′(v) with R′ + φ(R′) = R0(v);
both are increasing in v. Write N_κ(v) and Ξ(v) for N_κ and Ξ at these points, with μ = μ(v) and μ̇ = (3/2)α w² by
[[eq:margins-rates]].

**Lemma {#lem:margins-curvature}** (Second derivatives along the slices.) On a cell [v_k, v_(k+1)] let S_i be the
supremum of |α^(i)| (i = 0, 1, 2) and Φ4 the supremum of |φ⁗| over [R′(v_k), R′(v_(k+1))]. Then on the cell

    (a)  |d²N_κ/dv²| ≤ M := 0.024 S_2 + 0.059 S_1 + 0.072 S_0 + 0.0013 S_0² + 0.17,
    (b)  |d²Ξ/dv²| ≤ M′ := 1.21 Φ4 + 0.024 S_2 + 0.061 S_1 + 0.075 S_0 + 0.0013 S_0² + 0.23.

*Proof.* By [[lem:margins-shell-data]] (c) and the monotonicity of R, P and μ in v, along 𝒩 the true values satisfy
0.4769 ≤ P ≤ 1/2, 13/2 ≤ R ≤ 7.2325 and 3/2 ≤ μ ≤ 3.6059; hence 0.91465 ≤ f_N ≤ 0.97133, 0.60976 ≤ w ≤ 0.67892, μ/R³ ≤
0.013131 and 0 ≤ μ̇ ≤ (3/2)(0.67892)² S_0 ≤ 0.6914 S_0 ≤ 2.49. By [[eq:margins-ode]] and [[eq:margins-rates]],

    μ′ = αw,   μ″ = α′w + 2αμ/(3R³),   μ̇′ = (3/2)α′w² + 2αwμ/R³,
    μ̇″ = (3/2)α″w² + 4α′wμ/R³ + (4/3)αμ²/R⁶ + 2α²w²/R³ − 6αwμP/R⁴,

with R the radius on 𝒩, so |μ′| ≤ 0.67892 S_0, |μ″| ≤ 0.67892 S_1 + 0.008754 S_0, |μ̇′| ≤ 0.6914 S_1 + 0.01783 S_0
and |μ̇″| ≤ 0.6914 S_2 + 0.03566 S_1 + 0.004345 S_0 + 0.003357 S_0². Also R0′ = g ≤ 1.09332 and |R0″| = |g′| ≤
0.015696.

(a) N_κ = H(μ, μ̇, R0) with H := −2μR⁻³ − μ²R⁻⁵ + (1/2)μ̇R⁻², linear in μ̇. For R ≥ 3.825, μ ≤ 3.6059 and μ̇ ≤ 2.49,
the partial derivatives obey |H_μ| ≤ 0.044547, H_μ̇ ≤ 0.034175, |H_R| ≤ 0.12184 + 0.01787μ̇, |H_μμ| ≤
0.0024428, |H_μR| ≤ 0.039545, |H_μ̇R| ≤ 0.01787 and |H_RR| ≤ 0.13827 + 0.014016μ̇, each a sum of the moduli of its terms
at R = 3.825 and the largest μ. The chain rule,

    N_κ″ = H_μ μ″ + H_μ̇ μ̇″ + H_R R0″ + H_μμ μ′² + 2H_μR μ′ R0′ + 2H_μ̇R μ̇′ R0′ + H_RR R0′²,

and the bounds above give |N_κ″| ≤ 0.02363 S_2 + 0.05848 S_1 + 0.07172 S_0 + 0.00125 S_0² + 0.1672 ≤ M.

(b) Ξ = φ″(R′) + Y(μ, μ̇, R′, V) with Y := μR⁻³V²(3 − V) + μ²R⁻⁵V³ − (1/2)μ̇R⁻²V³ and V := 1 + φ′(R′). Differentiating
R′ + φ(R′) = R0 gives R′_v = g/V, R′_vv = g′/V − g²φ″/V³, V_v = φ″R′_v and V_vv = φ‴R′_v² + φ″R′_vv, so with
[[prop:margins-bend]] (c), R′_v ≤ 1.09567, R′_v² ≤ 1.20049, |R′_vv| ≤ 0.027761, |V_v| ≤ 0.010957 and |V_vv| ≤ 0.08713;
and (φ″(R′))_vv = φ⁗R′_v² + φ‴R′_vv. For 3.825 ≤ R ≤ 5.373, μ ≤ 3.6059, μ̇ ≤ 2.49 and V ∈ [0.99786, 1.00149],

    |Y_μ| ≤ 0.044666,  Y_μ̇ ≤ 0.034328,  |Y_R| ≤ 0.12216 + 0.01795μ̇,  |Y_V| ≤ 0.24109 + 0.10284μ̇,  |Y_μμ| ≤ 0.0024537,
    |Y_μR| ≤ 0.039659,  |Y_μV| ≤ 0.080112,  |Y_μ̇R| ≤ 0.01795,  |Y_μ̇V| ≤ 0.10284,  |Y_RR| ≤ 0.13865 + 0.014078μ̇,
    |Y_RV| ≤ 0.21408 + 0.053768μ̇,  |Y_VV| ≤ 0.096254 + 0.20536μ̇,

each again a sum of the moduli of its terms (using V²(3 − V) ≤ 2.00447, V³ ≤ 1.00448 and 3V(2 − V) ≤ 3). The chain rule
for Y in the four variables (Y is linear in μ̇) and the bounds above give |Ξ_vv| ≤ 1.2005 Φ4 + 0.02374 S_2 + 0.06031
S_1 + 0.08062 S_0 + 0.00125 S_0² + 0.19801, and 0.08062 S_0 + 0.19801 ≤ 0.075 S_0 + 0.23 because S_0 ≤ 3.6. ∎

**Theorem {#thm:margins-hyperbolic}** (Hyperbolicity margins on R ≥ R_*.) Let R_* ∈ (3.43718, 3.43719) be as in
[[lem:margins-region-one]] (b). For the background:

(a) on Σ′, κ′ > 0, K′^l_l < 0 and κ′K′^l_l ≤ −2.96 × 10⁻⁴ for R_* ≤ R ≤ 5.75, and κ′K′^l_l < 0 for R ≥ 5.75;

(b) on Σ_τ0, N_κ < 0 for R ∈ [R_*, 4.2882] ∪ [4.5310, ∞), and N_κ > 0 for R ∈ [4.2955, 4.5258].

So Rácz's split is hyperbolic on all of Σ′ ∩ {R ≥ R_*}; on Σ_τ0 ∩ {R ≥ R_*} it is hyperbolic outside [4.2882, 4.5310]
and is not hyperbolic on [4.2955, 4.5258], and each of the two remaining intervals, of widths 0.0073 and 0.0052,
contains a point where N_κ = 0.

*Proof.* By [[lem:margins-region-one]] every point concerned lies in region I, so [[lem:margins-racz]] applies, with μ
and μ̇ those of 𝒩 at the point's time v̂.

*Σ′ before the shell.* The points of Σ′ with R ≤ R′(3) = 3.8254920 have v̂ ≤ v̂(3), so μ = 3/2 and μ̇ = 0. On [R_*,
3.5], φ = 0 and Ξ = (1.5/R³)(2 + 1.5/R²) ≥ 0.074254, while c ≥ 3(1.5/3.5²)/(3.5 (1 + 1.5/R_*²)²) ≥ 0.082639, so
κ′K′^l_l ≤ −6.1 × 10⁻³. On [3.5, 3.82550], φ″ ≥ −0.01 l1 ≥ −0.0064382, V′ ∈ [0.99786, 1] (φ′ ≤ 0 there) and f ∈
[0.877551, 0.897504], so Ξ ≥ −0.0064382 + 0.026793 × 0.995724 × 2.102496 ≥ 0.049653 and c ≥ 0.307488/(3.8255 ×
1.124327²) ≥ 0.063585, so κ′K′^l_l ≤ −3.1 × 10⁻³.

*Σ′ over the shell.* For v ∈ [3, 4.5] use [[sec:table-sigma-bent]]. The map R ↦ R + φ(R) has derivative 1 + φ′ ≥
0.9978; it sends R′(v_k) to v̂(v_k) + 0.68, which is within 4 × 10⁻⁶ of v̂_k + 0.68 by [[lem:margins-shell-data]] (c),
and it sends R′_k to within 2 × 10⁻⁷ of v̂_k + 0.68 (the residual 10⁻⁷ of the table and the roundings of R0_k and φ_k).
So |R′(v_k) − R′_k| ≤ (4 × 10⁻⁶ + 2 × 10⁻⁷)/0.9978 ≤ 5.3 × 10⁻⁶. The true value Ξ(v_k) then differs from Ξ_k by at most

    0.0447 × 10⁻⁵ + 0.0344 × 8.4 × 10⁻⁶ + 0.24 × 5.3 × 10⁻⁶ + 0.50 × 0.01 × 5.3 × 10⁻⁶ + 5 × 10⁻⁸ ≤ 5 × 10⁻⁶.

The terms come from μ (|Δμ| ≤ 10⁻⁵), from μ̇ (|Δμ̇| ≤ 3αw|Δw| ≤ 7.34 (0.016635 × 10⁻⁵ + 0.019401 × 4 × 10⁻⁶ + 1.43959
× 6 × 10⁻⁷) ≤ 8.4 × 10⁻⁶, by [[lem:margins-shell-data]] (c)), from the radius R′, from V′ = 1 + φ′(R′) (|φ″| ≤ 0.01
times the change of radius) and from the rounding of Ξ_k. The coefficients bound the partial derivatives of Ξ by the
bounds of the proof of [[lem:margins-curvature]]: |Y_μ| ≤ 0.0447, Y_μ̇ ≤ 0.0344, |Y_R| + |φ‴| ≤ 0.12216 + 0.01795 ×
2.49 + 0.072346 ≤ 0.24 and |Y_V| ≤ 0.24109 + 0.10284 × 2.49 ≤ 0.50. By [[lem:margins-enclosure]] (b) and
[[lem:margins-curvature]] (b), on the cell [v_k, v_(k+1)], Ξ ≥ L_k := min(Ξ_k, Ξ_(k+1)) − 5 × 10⁻⁶ − M′_k/51200, where
h²/8 = 1/51200; here Φ4_k bounds |φ⁗| on the cell, because R′ increases with v and so the cell's radii lie in [R′_k −
5.3 × 10⁻⁶, R′_(k+1) + 5.3 × 10⁻⁶]. On the cell, R lies in that interval, μ in [μ_k − 10⁻⁵, μ_(k+1) + 10⁻⁵] (μ
increases with v), and V′ in [min(V_k, V_(k+1)) − 2 × 10⁻⁴, max(V_k, V_(k+1)) + 2 × 10⁻⁴] with V_k := 1 + φ′_k, since
φ′_k is within 5 × 10⁻⁷ of φ′(R′_k), |φ″| ≤ 0.01 and R′_(k+1) − R′_k ≤ 0.013. So f lies between 1 − (μ_(k+1) +
10⁻⁵)/(R′_k − 5.3 × 10⁻⁶)² and 1 − (μ_k − 10⁻⁵)/(R′_(k+1) + 5.3 × 10⁻⁶)², and c ≥ c_k, the value of c with the largest
f and V′ in the numerator and the largest R, V′ and smallest fV′ in the denominator. Every row has L_k > 0, and the
bound column gives κ′K′^l_l ≤ −c_k L_k ≤ −3.041 × 10⁻⁴ on every cell.

*Σ′ after the shell.* For R ∈ [R′(4.5), 5.75], R′(4.5) ≥ 5.372519, μ = μ(4.5) ∈ [3.60579, 3.60582] and μ̇ = 0; φ″ ≥
−0.01 l2 ≥ −0.0027323 and V′ ∈ [1, 1.0014840] (φ′ ≥ 0 there), and f ∈ [0.875075, 0.890941]. So Ξ ≥ −0.0027323 +
(3.60579/5.75³)(3 − 0.890941 × 1.0014840) ≥ 0.037244 and c ≥ 0.32321/(5.75 × 1.0014840² × 1.124925²) ≥ 0.044287, so
κ′K′^l_l ≤ −1.6 × 10⁻³. For R ≥ 5.75, Σ′ = Σ_τ0, μ is constant and μ̇ = 0, so N_κ = −2μ/R³ − μ²/R⁵ < 0; hence κ > 0,
K^l_l < 0 and κK^l_l < 0. This proves (a).

*The band on Σ_τ0.* Where v̂ ≤ v̂(3) or v̂ ≥ v̂(4.5), that is R ≤ R0(3) = 3.8253316 or R ≥ R0(4.5) = 5.3724596, μ̇ = 0
and N_κ < 0. For v ∈ [3, 4.5] use [[sec:table-sigma0]]. The true N_κ(v_k) differs from N_k by at most

    0.044547 × 10⁻⁵ + 0.034175 × 8.4 × 10⁻⁶ + 0.16634 × 4 × 10⁻⁶ + 5 × 10⁻⁹ ≤ 1.5 × 10⁻⁶ ≤ 5 × 10⁻⁶,

the terms coming from μ, μ̇ and the radius v̂ + 0.68 (as above, by [[lem:margins-shell-data]] (c)) and from the
rounding of N_k, with |H_μ| ≤ 0.044547, H_μ̇ ≤ 0.034175 and |H_R| ≤ 0.12184 + 0.01787 × 2.49 ≤ 0.16634 from the proof
of [[lem:margins-curvature]]. On each cell [[lem:margins-enclosure]] (b) and [[lem:margins-curvature]] (a) give the
sign column. Cells 0–34 and 55–119 are negative, cells 37–53 positive. On the remaining cells write v = v_k + s/80. By
[[lem:margins-enclosure]] (b), with |g′| ≤ 0.0157 and [[lem:margins-shell-data]] (c), R0(v) is within 4.5 × 10⁻⁶ of (1 −
s)R0_k + sR0_(k+1), and N_κ(v) is within 5 × 10⁻⁶ + M_k/51200 of (1 − s)N_k + sN_(k+1). Hence:

- cell 35, s ∈ [0, 0.762]: N_κ ≤ max(−0.00049105, 0.238 × (−0.00049105) + 0.762 × 0.00000012) + 5 × 10⁻⁶ + 1.17/51200 ≤
  −8.8 × 10⁻⁵, and at s = 0.762, R0 ≥ 4.2783783 + 0.762 × 0.0129271 − 4.5 × 10⁻⁶ ≥ 4.288224;
- cell 36, s ∈ [0.323, 1]: N_κ ≥ min(0.323 × 0.00042441 + 0.677 × 0.00000012, 0.00042441) − 5 × 10⁻⁶ − 1.14/51200 ≥
  1.09 × 10⁻⁴, and at s = 0.323, R0 ≤ 4.2913054 + 0.323 × 0.0129260 + 4.5 × 10⁻⁶ ≤ 4.295486;
- cell 54, s ∈ [0, 0.156]: N_κ ≥ min(0.00012015, 0.844 × 0.00012015 − 0.156 × 0.00021986) − 5 × 10⁻⁶ − 0.82/51200 ≥
  4.6 × 10⁻⁵, and at s = 0.156, R0 ≥ 4.5238047 + 0.156 × 0.0129054 − 4.5 × 10⁻⁶ ≥ 4.525813;
- cell 54, s ∈ [0.556, 1]: N_κ ≤ max(0.444 × 0.00012015 − 0.556 × 0.00021986, −0.00021986) + 5 × 10⁻⁶ + 0.82/51200 ≤
  −4.7 × 10⁻⁵, and at s = 0.556, R0 ≤ 4.5238047 + 0.556 × 0.0129054 + 4.5 × 10⁻⁶ ≤ 4.530985.

Since R0 is increasing, N_κ < 0 on R ∈ [R_*, 4.288224] ⊃ [R_*, 4.2882] and on [4.530985, ∞) ⊃ [4.5310, ∞), and N_κ > 0
on [4.295486, 4.525813] ⊃ [4.2955, 4.5258]. On Σ_τ0, K^l_l < 0 and κ = −N_κ/(2 − f)^(3/2), so the split is hyperbolic
where N_κ < 0 and not hyperbolic where N_κ > 0. By continuity N_κ vanishes in each of the two intervals left over. ∎

The rows give more than the statement: κ′K′^l_l ≤ −3.04 × 10⁻⁴ on Σ′ ∩ {R_* ≤ R ≤ 5.75}. The largest cell bounds occur
on the cells around R = 4.66, where the bend's central lobe is on its falling side. For 0.68 ≤ R ≤ R_*, where Σ′ =
Σ_τ0, the margin is that of [[thm:bg-margins]] (c).

### Γ on the seed region {#sec:margins-seed}

On a vacuum region of the background, in the chart (v̂, R), g = −e^(2ψ) f dv̂² + 2e^ψ dv̂ dR + R² dΩ₃² with f = 1 −
μ/R², μ constant and ψ = ψ(v̂), the slice Σ_τ0 (v̂ = τ0 + R) has γ = G dR² + R² dΩ₃² with G = e^ψ(2 − e^ψ f), and
N_s√G = 1. Along it write ψ, ψ′ and ψ″ for ψ(τ0 + R) and its derivatives, q := e^ψ, u := 1 − q, m := μ/R² and w := qf =
q(1 − m). The quantities ν, β, a, E, P and Γ of [[pending:thm-charge-identity]] are then ν = R³, β = R N_κ/(3(2 − w)(w −
1)) with N_κ = (q f′/2)(w − 3) − ψ′ and f′ = 2μ/R³ (from κ0 and Y0 of [[pending:lem-racz-split-formulas]]; N_κ is the
quantity of [[lem:margins-racz]], here with ψ ≠ 0 and μ̇ = 0), a = −3(1 − β)/R, E = e^(∫a), P = 8νE²R/G − (2νER/√G)′
RE/√G and Γ = 4νE² − P′.

**Lemma {#lem:margins-gamma-form}** (Γ/E² in closed form.) On such a region, wherever w < 1,

    Γ/E² = A0 + A1 ψ′ + A2 ψ′² + A3 ψ″,   {#eq:margins-gamma-form}

    A0 := 4R³ n0/(q(2 − w)(1 − w)²),
    n0 := m³ − 2m(2m² − m + 1)u + (2m + 1)(3m² − 5m + 4)u² − 4m(m − 1)²u³ + (m − 1)³u⁴,
    A1 := 2R⁴ (m(5 − m) − (1 − m)(7 + m)u)/((2 − w)(1 − w)²),
    A2 := 2R⁵ (1 − m)(1 + 2w)/((2 − w)(1 − w)²),     A3 := 2R⁵ (1 − m)/((2 − w)(1 − w)).

Where ψ = 0 this is Γ/E² = 4R³μ/(R² + μ), that is Γ = 4μ/R for the normalisation E = √G/R.

*Proof.* Since E′ = aE and ν = R³, (2νER/√G)′ = E((2R⁴/√G)′ + 2aR⁴/√G), so P = E²p with p := 8R⁴/G − R(2R⁴/√G)′/√G −
2aR⁵/G = (R⁵/G)(G′/G − 2a), and Γ/E² = 4R³ − 2ap − p′. Here G′/G = ψ′ − w′/(2 − w) with w′ = q(ψ′f + f′), and a = −3/R +
N_κ/((2 − w)(w − 1)). Substituting, p′ contains ψ″ linearly through ψ″ in (G′/G)′ and in N_κ′ = (q/2)(ψ′f′ + f″)(w − 3)
+ (qf′/2)w′ − ψ″, f″ = −6μ/R⁴. Clearing the common denominator qR⁶(2 − w)(1 − w)² and collecting the coefficients of 1,
ψ′, ψ′² and ψ″, the numerator of the ψ′⁰ term becomes 4R⁹n0 after the substitution q = 1 − u, m = μ/R², which gives the
stated A0, A1, A2, A3. At ψ = 0, u = 0 and ψ′ = ψ″ = 0, so Γ/E² = A0 = 4R³m³/((1 + m)m²) = 4R³μ/(R² + μ). Since E′ = aE
fixes E only up to a constant factor, and Γ scales with E², the last statement is for the normalisation E = √G/R, which
solves E′ = aE where ψ = 0; there E² = (R² + μ)/R⁴, and Γ = 4μ/R. ∎

**Lemma {#lem:margins-profile-monotone}** (The reference profile.) On [0.02, 1.181], ψ_s is increasing, ψ_s′ is positive
and decreasing, and ψ_s″ is negative and increasing.

*Proof.* ψ_s‴(v̂) = 60c_5 v̂² + 24c_4 v̂ + 6c_3 has positive leading coefficient and discriminant (24c_4)² − 4(60c_5)
(6c_3) = 2.6861 × 10⁻⁴ − 3.1207 × 10⁻⁴ < 0, so ψ_s‴ > 0. Hence ψ_s″ increases, and ψ_s″(1.181) = −0.0325045 < 0. So ψ_s′
decreases, and ψ_s′(1.181) = 0.0617566 > 0. So ψ_s increases. ∎

**Proposition {#prop:margins-seed}** (Γ on the seed region.) Let (ψ_s, μ_s) be the reference profile of
[[sec:table-seed-profile]] and let Γ/E² be given by [[eq:margins-gamma-form]] on R ∈ [0.70, 1.861].

(a) For ψ = ψ_s, ψ′ = ψ_s′, ψ″ = ψ_s″ (at τ0 + R) and μ = μ_s, Γ/E² ≥ 0.4475.

(b) For every μ with |μ − μ_s| ≤ 10⁻⁴ and every (ψ, ψ′, ψ″) with |ψ − ψ_s| ≤ 10⁻³, |ψ′ − ψ_s′| ≤ 10⁻³ and |ψ″ − ψ_s″| ≤
3 × 10⁻² at τ0 + R, Γ/E² ≥ 0.048. In particular Γ > 0 on the seed region for every background whose profile ψ past the
outgoing packet is within (10⁻³, 10⁻³, 3 × 10⁻²) of ψ_s in C² there and whose mass there is within 10⁻⁴ of μ_s.

*Proof.* Cover [0.70, 1.861] by the thirty-two cells of [[sec:table-seed-cells]]. On a cell, by
[[lem:margins-profile-monotone]], ψ_s, ψ_s′ and ψ_s″ range over the intervals between their values at the ends of the
cell, which lie within 5 × 10⁻⁸ of the printed end values. For (a) take the intervals between the printed end values,
each end moved outward by 5 × 10⁻⁸, and μ = μ_s; for (b) widen these intervals further by 10⁻³, 10⁻³ and 3 × 10⁻², and
take μ ∈ [μ_s − 10⁻⁴, μ_s + 10⁻⁴]. Evaluate [[eq:margins-gamma-form]] in the written form by [[lem:margins-enclosure]]
(a), with R the cell, q = e^ψ, u = 1 − q, m = μ/R², w = q(1 − m) and 2 − w, 1 − w positive on every cell. The resulting
lower ends are columns (a) and (b); their least values are 0.456 and 0.438, which exceed 0.4475 and 0.048. ∎

By [[prop:bg-seed]] (c), the background itself lies in the tube of (b), which gives Γ > 0 on its seed region
and so [[pending:cor-charge-seed]] there.
