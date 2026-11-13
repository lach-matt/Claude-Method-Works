<!-- Placement: a section of its own at the end of sec:s14-model, just before sec:iv4-1; not before prop:np-10-54. -->
### The scalar type l ≥ 1 for every h ∈ (0, 10⁻⁶] {#sec:s14-every-h}

This section proves the statements of [[prop:np-10-54]] (i)–(ii) about the polynomials P_l, l ≥ 1, at every
h ∈ (0, 10⁻⁶]. As in [[sec:s14-model]], (v, e) = (1/2, 1/102400). The exact value of e enters only through
[[lem:s14-small-h]] (a), which is proved at this value: there the roots ι₊, ι₋ of Q_5 are distinct by [[lem:s14-q5]]
(b), whose proof uses it. Every inequality proved below uses of e only 10⁻⁶ < e < 10⁻⁵.
We let κ be any real number ≥ 0 and write P(ι; κ, h) for the determinant of the matrix [[eq:s14-nl]] at v = 1/2 with
this κ, so that P_l(ι) = P(ι; l(l + 2), h). It is a polynomial in (ι, κ, h), of degree 6 in ι with leading coefficient
−h³: this is f₆ of [[eq:s14-f-two]] below, and for κ = l(l + 2) it is [[prop:np-10-12]] (iii).

The argument has three steps. As (κ, h) varies, no root of P(·; κ, h) meets the line Re ι = 2, except the root ι = 2
at κ = 3 ([[lem:s14-line-two]]); no root meets the line Re ι = −1/(2h) ([[lem:s14-line-far]]); and the number of roots
on each side of these lines is read off in the limit h → 0⁺ from [[lem:s14-small-h]].

**Lemma {#lem:s14-half-plane-count}** (Counting roots in a half-plane.) Let Ω ⊂ ℝ² be connected, and for ω ∈ Ω let
p_ω(z) = a_n(ω)zⁿ + … + a_0(ω) be a polynomial whose coefficients are continuous functions on Ω, with a_n(ω) ≠ 0. Let
H ⊂ ℂ be an open half-plane with boundary line L. If no p_ω has a root on L, then the number of roots of p_ω in H,
counted with multiplicity, is the same for every ω ∈ Ω.

*Proof.* Fix ω₀ ∈ Ω. Every root z of p_ω satisfies |z| ≤ 1 + max_(j<n) |a_j(ω)/a_n(ω)|, and the right side is
continuous in ω. So there are a neighbourhood V of ω₀ in Ω and a number R, larger than the distance from 0 to L, such
that every root of p_ω, ω ∈ V, has modulus less than R. Let G := H ∩ {|z| < R}, a bounded convex open set whose
boundary Γ consists of a segment of L and an arc of the circle |z| = R. As p_(ω₀) has no root on Γ,
m₀ := min_Γ |p_(ω₀)| > 0, and after shrinking V, |p_ω − p_(ω₀)| < m₀ on Γ for ω ∈ V, since Γ is bounded and the
coefficients are continuous. By Rouché's theorem p_ω and p_(ω₀) have equally many roots in G, and these are all their
roots in H. So the number is locally constant on Ω, hence constant, Ω being connected. ∎

#### The line Re ι = 2 {#sec:s14-every-h-two}

At ι = 2 + w the matrix [[eq:s14-nl]] at v = 1/2 is, with a := κ − 2w − w²,

    ( ha − w,        2w,                          2κ               )
    ( 2e(w + 3),     h(a + 3) + e(w + 3) − 2w,    −(1 + 2h)κ       )
    ( −2e,           −(e + 2h),                   h(a − 1) + 1 − w ).                                    {#eq:s14-hn-two}

Write it as M₀ + hM₁, where M₀ is its value at h = 0 and M₁ has rows (a, 0, 0), (0, a + 3, −2κ), (0, −2, a − 1). The
determinant is multilinear in the columns, so P(2 + w; κ, h) = P⁽⁰⁾ + hP⁽¹⁾ + h²P⁽²⁾ + h³P⁽³⁾, where P⁽⁰⁾ = det M₀,
P⁽³⁾ = det M₁, P⁽¹⁾ is the sum of the three determinants of M₀ with one column replaced by the same column of M₁, and
P⁽²⁾ is the sum of the three determinants of M₁ with one column replaced by the same column of M₀. Expanding,

    P⁽⁰⁾ = w(e(5w² + 10w − 15 − 3κ) − 2w² + 2w),
    P⁽¹⁾ = e(6w⁴ + 29w³ + 36w² + 9w − 9κw² − 21κw + 3κ² − 9κ) − 5w⁴ − 7w³ + (5κ + 7)w² − (κ + 3)w,
    P⁽²⁾ = e(w⁵ + 7w⁴ + 17w³ + 17w² + 6w − 2κw³ − 8κw² − 9κw + κ²w + κ² − 3κ)
           − 4w⁵ − 15w⁴ + (8κ − 9)w³ + (16κ + 7)w² − (4κ² − κ + 3)w − κ² + 3κ,
    P⁽³⁾ = −(w² + 2w − κ)(w² + 4w + 3 − κ)(w² − 1 − κ),                                               {#eq:s14-ph-two}

the last because det M₁ = a((a + 3)(a − 1) − 4κ), a = −(w² + 2w − κ) and
a² + 2a − 3 − 4κ = (w² + 4w + 3 − κ)(w² − 1 − κ). (P⁽⁰⁾ = 4wQ_5(2 + w), in accordance with [[eq:s14-q5]].) Collecting
the powers of w, P(2 + w; κ, h) = f₀ + f₁w + … + f₆w⁶ with

    f₀ = hκ(κ − 3)(3e − (1 − e)h + (κ + 1)h²),
    f₁ = −3e(κ + 5) − h(κ + 3 + 21eκ − 9e) − h²((4 − e)κ² − (1 − 9e)κ + 3 − 6e) − 6h³(κ² − 1),
    f₂ = 2 + 10e + h(5κ + 7 − 9eκ + 36e) + h²(16κ + 7 − 8eκ + 17e) − h³(3κ² − 12κ − 11),
    f₃ = −2 + 5e − h(7 − 29e) + h²(8κ − 9 − 2eκ + 17e) + 12h³κ,
    f₄ = −h(5 − 6e) − h²(15 − 7e) + h³(3κ − 10),
    f₅ = −h²(4 − e) − 6h³,
    f₆ = −h³.                                                                                            {#eq:s14-f-two}

**Lemma {#lem:s14-line-two}** (The line Re ι = 2.) Let κ ≥ 3 and 0 < h ≤ 10⁻⁶.

(a) P(2; κ, h) = f₀, which is positive for κ > 3 and zero for κ = 3; and ∂_ιP(2; κ, h) = f₁ < 0.

(b) P(2 + iy; κ, h) ≠ 0 for every real y ≠ 0.

Hence for κ > 3 no root of P(·; κ, h) has real part 2, and for κ = 3 the only one is ι = 2, which is simple.

*Proof.* (a) As h < e, 3e − (1 − e)h > 2e > 0, so f₀ has the sign of κ − 3. In f₁ the brackets are positive:
κ + 3 + 21eκ − 9e > κ, (4 − e)κ² − (1 − 9e)κ + 3 − 6e > 3κ² − κ > 0 and κ² − 1 > 0; so f₁ < −3e(κ + 5) < 0.

(b) The f_j are real, so P(2 + iy; κ, h) = A(y²) + iyB(y²) with the real polynomials

    A(s) := f₀ − f₂s + f₄s² − f₆s³,     B(s) := f₁ − f₃s + f₅s².

Then −A(s) − h(κ + s)B(s) = D₀ + D₁s + D₂s² + D₃s³ with D₀ = −f₀ − hκf₁, D₁ = f₂ + hκf₃ − hf₁,
D₂ = −f₄ − hκf₅ + hf₃ and D₃ = f₆ − hf₅, and inserting [[eq:s14-f-two]] and collecting terms,

    D₀ = hκ(24e + h(2κ + 20eκ − 6e) + h²((3 − e)κ² + (1 + 9e)κ + 6 − 6e) + 6h³(κ² − 1)),
    D₁ = 2 + 10e + h((3 − e)κ + 7 + 51e) + h²((10 + 42e)κ + 10 + 8e)
         + h³((9 − 3e)κ² + (2 + 26e)κ + 14 − 6e) + 6h⁴(3κ² − 1),
    D₂ = h(3 − e) + h²(8 + 22e) + h³((9 − 3e)κ + 1 + 17e) + 18h⁴κ,
    D₃ = h³(3 − e) + 6h⁴.                                                                                {#eq:s14-d-two}

For instance, in D₀ the terms of order e give −3e(κ − 3) + 3e(κ + 5) = 24e, those of order h give
(1 − e)(κ − 3) + κ + 3 + 21eκ − 9e = 2κ + 20eκ − 6e, and those of order h² give
−(κ − 3)(κ + 1) + (4 − e)κ² − (1 − 9e)κ + 3 − 6e = (3 − e)κ² + (1 + 9e)κ + 6 − 6e. For κ ≥ 1 and 0 < e < 1/3 every
bracket in [[eq:s14-d-two]] is positive, so D₀, D₂, D₃ > 0 and D₁ > 2. If P(2 + iy; κ, h) = 0 with y ≠ 0, then
A(y²) = B(y²) = 0, so −A(y²) − h(κ + y²)B(y²) = 0, while D₀ + D₁y² + D₂y⁴ + D₃y⁶ ≥ D₁y² > 0. ∎

#### The line Re ι = −1/(2h) {#sec:s14-every-h-far}

**Lemma {#lem:s14-line-far}** (The line Re ι = −1/(2h).) Let κ ≥ 0 and 0 < h ≤ 10⁻⁶. Then P(·; κ, h) has no root
with real part −1/(2h).

*Proof.* Put K := h²κ and F(σ) := h³P(σ/h; κ, h). Multiply the matrix [[eq:s14-nl]] at v = 1/2 by h, put ι = σ/h and
κ = K/h², then multiply its third column by h and divide its third row by h. The determinant becomes F(σ), and the
matrix becomes, with M := K − σ − σ²,

    Y := ( M + 2h(σ + 1),   2σ − 4h,                                2K                 )
         ( 2e(σ + h),       M − σ + 2hσ + 4h + 3h² + e(σ + h),      −(1 + 2h)K         )
         ( −2e,             −(e + 2h),                              M + 2hσ + 3h − h² ).                  {#eq:s14-y}

A root ι of P(·; κ, h) with real part −1/(2h) gives the root σ = hι = −1/2 + iy of F = det Y, y real. On this line
M = K + 1/4 + y² is real, |σ|² = 1/4 + y² ≤ M and K ≤ M. Put m := M^(1/2) ≥ 1/2; then |σ| ≤ m, K ≤ m², 1 ≤ 2m and
m ≤ 2m². Write Y = Y⁰ + Z, where Y⁰ is the upper triangular matrix with rows (M, 2σ, 2K), (0, M − σ, −K) and
(0, 0, M). Then

    det Y⁰ = M²(M − σ),     |det Y⁰| ≥ M² Re(M − σ) = m⁴(m² + 1/2) > m⁶.

The rows of Z are (2h(σ + 1), −4h, 0), (2e(σ + h), 2hσ + 4h + 3h² + e(σ + h), −2hK) and (−2e, −(e + 2h),
2hσ + 3h − h²). Let r_i and ρ_i be the sums of the moduli of the entries of row i of Y⁰ and of Z. With the bounds
above,

    r₁ ≤ m² + 2m + 2m² ≤ 7m²,     r₂ ≤ (m² + m) + m² ≤ 4m²,     r₃ = m²,
    ρ₁ ≤ 2h(m + 1) + 4h ≤ 14hm ≤ 28hm²,
    ρ₂ ≤ 2e(m + h) + (2hm + 4h + 3h² + e(m + h)) + 2hm² ≤ (6e + 22h + 12eh + 12h²)m² ≤ (6e + 23h)m²,
    ρ₃ ≤ 2e + (e + 2h) + (2hm + 3h + h²) ≤ (12e + 24h + 4h²)m² ≤ (12e + 25h)m²,

where 1 ≤ 4m² and m ≤ 2m² were used to bring every term to a multiple of m². The determinant is multilinear in the
rows, so det Y − det Y⁰ is the sum, over the seven nonempty sets S ⊂ {1, 2, 3}, of the determinants of the matrices
whose rows i ∈ S are those of Z and whose other rows are those of Y⁰. By Hadamard's inequality, and since the
euclidean norm of a vector is at most the sum of the moduli of its entries, such a determinant has modulus at most
the product of ρ_i over i ∈ S and of r_i over i ∉ S. Hence, the expression in the middle being increasing in each r_i
and each ρ_i,

    |det Y − det Y⁰| ≤ (r₁ + ρ₁)(r₂ + ρ₂)(r₃ + ρ₃) − r₁r₂r₃ ≤ 28m⁶((1 + 4h)(1 + (6e + 23h)/4)(1 + 12e + 25h) − 1).

As e < 10⁻⁵ and h ≤ 10⁻⁶, the numbers 4h, (6e + 23h)/4 and 12e + 25h are below 1.5·10⁻⁴, and the right side is
below 28m⁶((1 + 1.5·10⁻⁴)³ − 1) < 0.02m⁶ < |det Y⁰|. So det Y ≠ 0 on the line Re σ = −1/2. ∎

#### The count {#sec:s14-every-h-count}

**Lemma {#lem:s14-limit-sides}** (The limits as h → 0⁺.) Let l ≥ 1.

(a) The roots ι₊, ι₋ of Q_5 have real part greater than 2.

(b) The three numbers 1/τ_j of [[lem:s14-small-h]] (a) are real and less than −1/2.

*Proof.* (a) By [[eq:s14-q5]] at v = 1/2, 4Q_5(ι) = e(5(ι − 3)(ι + 1) − 3κ) − 2(ι − 2)(ι − 3), a quadratic with
leading coefficient 5e − 2 < 0, and 4Q_5(2) = −e(15 + 3κ) < 0, 4Q_5(3) = −3eκ < 0. The midpoint of its roots is
c := (5 + 1/13653)/2 ∈ (2, 3) by [[lem:s14-q5]] (b). If the roots are not real, their real part is c. If they are
real, Q_5 ≥ 0 exactly on the closed interval between them, which contains c and neither 2 nor 3, so it lies in (2, 3).

(b) The factor τ + 1 of [[eq:s14-ttau]] gives 1/τ = −1. The quadratic factor q(τ) := (5e − 2)τ² + (e − 3)τ − 1 has
q(−2) = 18e − 3 < 0, q(−1) = 4e > 0, q(−1/2) = 3e/4 > 0 and q(0) = −1 < 0; so its roots lie in (−2, −1) and
(−1/2, 0), and their reciprocals in (−1, −1/2) and (−∞, −2). ∎

**Proposition {#prop:s14-scalar-every-h}** (The scalar type l ≥ 1 for every h ∈ (0, 10⁻⁶].) Let l ≥ 1 and
0 < h ≤ 10⁻⁶. Counted with multiplicity, P_l has three roots with real part less than −1/(2h) ≤ −5·10⁵ and three
roots with real part at least 2. For l ≥ 2 the latter three have real part greater than 2. For l = 1 one of them is
ι = 2, a simple root, and the other two have real part greater than 2. In particular no root of P_l has real part in
[−1/(2h), 2), and the only root with real part 2 is ι = 2 at l = 1.

*Proof.* *The roots on the left.* On Ω₁ := [3, ∞) × (0, 10⁻⁶] ∋ (κ, h) consider F(σ) = h³P(σ/h; κ, h) = det Y of
[[eq:s14-y]]. Its coefficients in σ are polynomials in K = h²κ and h, hence continuous on Ω₁; its leading coefficient
is −1, that of P being −h³; and its roots are the numbers hι, ι a root of P(·; κ, h), with the same multiplicities. By
[[lem:s14-line-far]] F has no root with real part −1/2, so by [[lem:s14-half-plane-count]] with H = {Re σ < −1/2} the
number N of roots of P(·; κ, h) with real part less than −1/(2h) is the same at every point of Ω₁. At κ = 3, that is
l = 1, [[lem:s14-small-h]] (a) gives, as h → 0⁺, three roots with hι → 1/τ_j, which are less than −1/2 by
[[lem:s14-limit-sides]] (b), and three roots converging to finite limits, for which hι → 0. So N = 3 for small h, hence
N = 3 on all of Ω₁.

*Degrees l ≥ 2.* On Ω₂ := (3, ∞) × (0, 10⁻⁶] the polynomial P(·; κ, h) has leading coefficient −h³ ≠ 0 and, by
[[lem:s14-line-two]], no root with real part 2. By [[lem:s14-half-plane-count]] with H = {Re ι > 2} the number N′ of
its roots with real part greater than 2 is the same at every point of Ω₂, and we find it at κ = 8, that is l = 2, for
small h. By [[lem:s14-small-h]] (a), three roots of P_2 converge to the pairwise distinct numbers 2, ι₊, ι₋, and the
real parts of the other three tend to −∞. The roots converging to ι₊ and ι₋ have real part greater than 2 for small h,
by [[lem:s14-limit-sides]] (a). For the third, choose δ > 0 smaller than |ι₊ − 2| and |ι₋ − 2| and such that Q_5 < 0
on [2, 2 + δ], which is possible as Q_5(2) < 0 ([[lem:s14-q5]] (a)). For small h exactly one root ρ_h of P_2 lies in
the disc |ι − 2| < δ; its complex conjugate is also a root in that disc, so ρ_h is real. Now P_2(2) = f₀ > 0 by
[[lem:s14-line-two]] (a), while P_2(2 + δ/2) tends to 4(δ/2)Q_5(2 + δ/2) < 0 as h → 0⁺, by [[eq:s14-q5]]. So for small
h, P_2 has a root in (2, 2 + δ/2), which is ρ_h, and ρ_h > 2. Hence N′ = 3, at every point of Ω₂. As P(·; κ, h) has
six roots and N = 3, no root lies in the strip −1/(2h) ≤ Re ι ≤ 2 when (κ, h) ∈ Ω₂, in particular when κ = l(l + 2)
with l ≥ 2.

*Degree l = 1.* P_1(2) = 0 for every h, so P_1 = (ι − 2)R with R a polynomial of degree 5 in ι, of leading coefficient
−h³, whose coefficients are polynomials in h. By [[lem:s14-line-two]], R(2 + iy) = P_1(2 + iy)/(iy) ≠ 0 for real
y ≠ 0, and R(2) = ∂_ιP_1(2) = f₁ ≠ 0; so R has no root with real part 2, and by [[lem:s14-half-plane-count]] with
Ω = {3} × (0, 10⁻⁶] the number of its roots with real part greater than 2 does not depend on h. As h → 0⁺, three roots
of P_1 converge to the pairwise distinct numbers 2, ι₊, ι₋ and the real parts of the other three tend to −∞
([[lem:s14-small-h]] (a)). For small h exactly one root of P_1 lies in a small disc about 2, and ι = 2 is a root
there; so the five roots of R are the other five. Two of them converge to ι₊ and ι₋ and have real part greater than 2
for small h ([[lem:s14-limit-sides]] (a)), and three have real parts tending to −∞. So R has exactly two roots with
real part greater than 2, for every h ∈ (0, 10⁻⁶]. Its roots with real part less than −1/(2h) are those of P_1, three
by the first part. So R has no root with real part in [−1/(2h), 2], and the roots of P_1 are ι = 2, simple as
R(2) ≠ 0, two with real part greater than 2, and three with real part less than −1/(2h). ∎

Since −1/(2h) ≤ −5·10⁵ < −100 and 2 > 19/10, [[prop:s14-scalar-every-h]] is the part of [[prop:np-10-54]] (i)–(ii)
that concerns the scalar types l ≥ 1. It holds at every h ∈ (0, 10⁻⁶] and every l ≥ 1, with no exceptional value of h;
as h_* ≤ 10⁻⁶, this includes every h ∈ 𝖧 of [[eq:iv4-0-1]].

**Corollary {#cor:s14-remote-point}** (The remote roots at γ_C = 10⁶.) Let h = 10⁻⁶, l ≥ 1 and hκ ≤ 70. The three
roots of P_l in |ι| < 1000 given by [[lem:s14-sextic-count]] (a) are its three roots with real part at least 2, and
its other three roots have real part less than −5·10⁵.

*Proof.* By [[prop:s14-scalar-every-h]], three roots of P_l have real part less than −5·10⁵, hence modulus greater
than 1000, and the other three have real part at least 2. The three roots in |ι| < 1000 of [[lem:s14-sextic-count]] (a)
are therefore the latter. ∎
