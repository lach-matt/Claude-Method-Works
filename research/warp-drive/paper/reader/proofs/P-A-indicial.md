### The indicial roots at the damping point γ_C = 10⁶ {#sec:s14-pa}

This section determines the number ε_ind(h) of [[prop:np-10-52]] (iii) at h = 10⁻⁶, that is at γ_C = 10⁶, and shows
that there the roots of the constraint damping polynomials P_l, P_0 and p_(v) keep a distance of more than
2.93·10⁻⁶ from the integers. The point h = 10⁻⁶ is the right end of the interval (0, 10⁻⁶] on which
[[prop:np-10-52]] (iii) defines ε_ind; it does not lie in the set 𝖧 of [[eq:iv4-0-1]] on which the theorems of this
paper are stated, and [[rem:s14-eps-ind-scope]] says what this section gives for h ∈ 𝖧. As in [[sec:s14-model]],
(v, e) = (1/2, 1/102400), κ = l(l + 2), and P_l, P_0, p_(v) and C are the polynomials of [[prop:np-10-12]] at this
point. Throughout this section

    h := 10⁻⁶,     ε₀ := e/h = 625/64,     x := hκ,     δ_C := 2.94·10⁻⁶,

and z = 4e_Υγ_Υ² = 4·10⁻⁶ as in [[sec:s14-simple]]. An entry of the lists of [[prop:np-10-52]] that comes from a
root ι of P_l, P_0 or p_(v) is ι − 1, and its modulus is at most 50 exactly when |ι − 1| ≤ 50. The tables this
section uses are in [[sec:tab-a]].

The elementary bounds, for a > 0 and 0 ≤ y ≤ 8a²,

    a + y/(2a) − y²/(8a³) ≤ (a² + y)^(1/2) ≤ a + y/(2a),                                                {#eq:s14-pa-sqrt}

follow from (a + y/(2a))² = a² + y + y²/(4a²) and (a + y/(2a) − y²/(8a³))² = a² + y − (y³/(8a⁴))(1 − y/(8a²)).

#### The number δ_50 {#sec:s14-pa-delta}

**Lemma {#lem:s14-delta50}** (The value of δ_50.) The number δ_50 of [[prop:np-10-52]] (iii), which depends on z
only and not on h, satisfies

    1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸,

so δ_50 = 1.94137056846·10⁻⁸ to twelve significant figures; and δ_50 < 2·10⁻⁴/10302 < 1.9413707·10⁻⁸ < 1.94138·10⁻⁸.

*Proof.* By [[prop:np-10-52]] (i) at u = 51, δ_50 = d₂ = ½((101² + B)^(1/2) − 101) = B/(2(101 + (10201 + B)^(1/2))),
where B := 2z − 4w, w := (2601 + A)^(1/2) − 51 = A/(51 + (2601 + A)^(1/2)) and A := z + z²/4 = 4.000004·10⁻⁶. By
[[eq:s14-pa-sqrt]] with a = 51, the denominator of w lies between 102 + A/102 − A²/(8·51³) and 102 + A/102, where
A/102 = 3.921572549019…·10⁻⁸ and A²/(8·51³) < 1.6·10⁻¹⁷. Dividing,

    3.921572547511889·10⁻⁸ < w < 3.921572547511890·10⁻⁸,     7.843137098099524·10⁻⁶ < B < 7.843137098099525·10⁻⁶.

By [[eq:s14-pa-sqrt]] with a = 101,

    B/(404 + B/101) ≤ δ_50 ≤ B/(404 + B/101 − B²/(4·101³)),

with 7.7654·10⁻⁸ < B/101 < 7.7655·10⁻⁸ and B²/(4·101³) < 1.5·10⁻¹⁷. With the bounds on B the left quotient exceeds
1.94137056846335·10⁻⁸ and the right one is below 1.94137056846336·10⁻⁸, which gives the first claim. For the second,
w > z/102: indeed A·102 > z(102 + A/102) because 102(A − z) = 25.5z² > zA/102. So δ_50 < B/404 < (2z − 4z/102)/404 =
50z/10302 = 2·10⁻⁴/10302 = 1.94137060764…·10⁻⁸. ∎

#### The vector type and the scalar type 0 {#sec:s14-pa-vector}

**Lemma {#lem:s14-vector-distance}** (The vector type at γ_C = 10⁶.) Let l ≥ 1 and Γ := 250002000000. The roots of
p_(v) are −499999 ± (Γ + (l + 1)²)^(1/2). The smaller is below −10⁶. The larger, ι_v, is at least 3, and if ι_v ≤ 51
and ι_v ∉ ℤ then

    dist(ι_v, ℤ) ≥ 3/1000100 > 2.9997·10⁻⁶.

*Proof.* At h = 10⁻⁶ and v = 1/2, −h⁻¹p_(v)(ι) = ι² + 999998ι − κ − 3·10⁶ ([[prop:np-10-12]] (ii)). Since
499999² = 249999000001 and κ = (l + 1)² − 1, (ι + 499999)² = Γ + (l + 1)² at a root, which gives the roots; ι_v
increases with l and equals (250002000004)^(1/2) − 499999 = 500002 − 499999 = 3 at l = 1.

Let ι_v ≤ 51 and let n be the integer nearest ι_v; then 3 ≤ n ≤ 51. Put k := n − 1. Expanding,
(n + 499999)² − Γ = n² + 999998n − 2999999 = X_k, where X_k := k² + 10⁶(k − 2). Hence

    (ι_v − n)(ι_v + n + 999998) = (ι_v + 499999)² − (n + 499999)² = (l + 1)² − X_k,

and if ι_v ≠ n the integer (l + 1)² − X_k is not 0. We show that its modulus is at least 3. As 10⁶ = 2⁶·5⁶,
X_k ≡ k² modulo 64 and modulo 25. Modulo 4, (l + 1)² − X_k ≡ (l + 1)² − k² ∈ {0, 1, −1}, so it is not ±2. Suppose
(l + 1)² − X_k = f with f = ±1, that is X_k + f = (l + 1)² is a square. Modulo 8 the squares are 0, 1, 4: if k is
odd, k² + 1 ≡ 2, so f = −1; if k ≡ 2 (mod 4), k² ± 1 ≡ 5 or 3, impossible; if 4 | k, k² − 1 ≡ 7, so f = +1. Modulo
5 the squares are 0, 1, 4: f = +1 excludes k ≡ ±1 and f = −1 excludes k ≡ ±2 (mod 5). If k² + f ≡ 0 (mod 5) it must
be ≡ 0 (mod 25), a square divisible by 5 being divisible by 25; among 2 ≤ k ≤ 50 this leaves, of
k ∈ {8, 12, 28, 32, 48} with f = +1, only k = 32 (k² + 1 = 65, 145, 785, 1025, 2305), and of the odd k ≡ ±1 (mod 5)
with f = −1 only k = 49 (k² − 1 = 2400). What remains is f = +1 with k ∈ {20, 32, 40} and f = −1 with
k ∈ {5, 15, 25, 35, 45, 49}; for these nine, X_k + f lies strictly between two consecutive squares
([[sec:tab-a-vector]]). So |(l + 1)² − X_k| ≥ 3, and since ι_v ≤ 51 and n ≤ 51,
|ι_v − n| = |(l + 1)² − X_k|/(ι_v + n + 999998) ≥ 3/1000100. The smaller root is −499999 − (Γ + (l + 1)²)^(1/2) <
−10⁶. ∎

**Lemma {#lem:s14-scalar-zero}** (The scalar type 0 at γ_C = 10⁶.) The root ι₁ > 2 of C (proof of
[[prop:np-10-54]]) satisfies 2 + δ_C < ι₁ < 5/2.

*Proof.* With C₀(ι) = (5e − 2)ι + 5e + 4 and C_h = 3h(1 + 2ι − ι²) + h²ι(3 + 2ι − ι²) + ehι(ι + 1), as in the proof
of [[prop:np-10-54]], C₀(2 + δ_C) = 15e − (2 − 5e)δ_C > 1.46·10⁻⁴ − 5.9·10⁻⁶ > 0 and C_h(2 + δ_C) > 0, as
1 + 2ι − ι² and 3 + 2ι − ι² are positive at ι = 2 + δ_C. At ι = 5/2, C₀ = −1 + 35e/2 < 0 and
C_h = −3h/4 + 35h²/8 + 35eh/4 < 0. C has exactly one root in (2, ∞), with C(2) > 0, so C > 0 on (2, ι₁) and C < 0 on
(ι₁, ∞), and the two signs place ι₁ in (2 + δ_C, 5/2). ∎

#### The sextic: decomposition, majorants and counting {#sec:s14-pa-sextic}

**Lemma {#lem:s14-sextic-split}** (The sextic at γ_C = 10⁶.) Let l ≥ 1.

(i) P_l(ι) = U(ι, x) + hW(ι, x), where

    U := (2 + x − ι)𝒬(ι, x),   𝒬(ι, x) := 2ι² − (3x + 10)ι + x² + (5 + 3ε₀)x + 12,   W := R₁ + hR₂ + h²R₃,
                                                                                                   {#eq:s14-pa-split}

with R₁, R₂, R₃ the polynomials of [[sec:tab-a-split]]; the coefficients of 64·10¹⁸P_l in ι are those of
[[sec:tab-a-sextic]].

(ii) 𝒬(2 + x, x) = 3(ε₀ − 1)x = 1683x/64, ∂_ι𝒬 = 4ι − 3x − 10, and W(2 + x, x) = −(1683/64)x c(x), with
c = c⁰ + hc₁ + h²c₂,

    c⁰(x) := x² + 5866x/1683 + 5000/561,     c₁(x) := 64x⁴/1683 − 2308x³/1683 − 4439x²/561 − 1019x/99 − 2,
    c₂(x) := 64x⁵/1683 − 241x⁴/1683 − 415x³/187 − 625x²/99 − 11329x/1683 − 1378/561.

One has |hc₁ + h²c₂| < 0.011, 0.43 and 1.43 on [0, 16], [0, 50] and [0, 70]; hence c > 0 on [0, 70], and c ≤ 11, 39,
321, 2684, 5155 on [0, 0.5], [0, 4], [0, 16], [0, 50], [0, 70].

(iii) The discriminant of 𝒬(·, x) is Δ_𝒬(x) := x² − 1715x/8 + 4, with roots x₋ ∈ (0.01866, 0.01867) and x₊ > 214.
For x₋ < x < x₊ the roots of 𝒬(·, x) are ζ and ζ̄,

    ζ := a + ib,     a = a(x) := (3x + 10)/4,     b = b(x) := (−Δ_𝒬(x))^(1/2)/4 > 0,

with |2 + x − ζ|² = 𝒬(2 + x, x)/2 = 1683x/128, |ζ|² = (8x² + 2195x/8 + 96)/16, and b increasing on (x₋, 107].

(iv) For 0 < x ≤ x₋ the roots of 𝒬(·, x) are real, a ± Δ_𝒬(x)^(1/2)/4, and for 0.018 ≤ x ≤ 0.5 both roots of 𝒬(·, x)
lie at distance more than 0.40 from 2 + x.

(v) Let Λ(x) be −½ times the coefficient of ι² in the remainder of W(·, x) on division by U(·, x). Then
Λ = Λ⁰ + hΛ₁ + h²Λ₂ with

    Λ⁰ = 17x²/8 − 5851x/128 − 9055/128,     Λ₁ = 47x³/8 − 2587x²/16 − 1079831x/8192 − 43031/128,
    Λ₂ = 129x⁴/32 − 36419x³/512 − 157055x²/32768 + 1864635x/16384 − 12933/64,

and for x₋ < x < x₊, with Π := Λ − c,

    Re(W(ζ, x)/∂_ιU(ζ, x)) = Π(x)/2.                                                                    {#eq:s14-pa-re}

Here Π⁰ := Λ⁰ − c⁰ = 9x²/8 − 10598081x/215424 − 5719855/71808; |Π − Π⁰| < 0.57 on [0, 35] and < 4.17 on [0, 70];
|Π⁰| ≤ 618 and |Π⁰′| ≤ 49.2 on [0, 35], |Π⁰| ≤ 1990 and |Π⁰′| ≤ 108.4 on [0, 70].

*Proof.* (i) Put e = ε₀h and κ = x/h in the matrix [[eq:s14-nl]], multiply its third column by h and divide its
third row by h. This leaves the determinant unchanged and gives M⁰ + hM¹, where

    M⁰ := ( 2 + x − ι      2(ι − 2)        2x        )      M¹ := ( 2ι − ι²         0                       0           )
          ( 0              4 + x − 2ι      −x        ),           ( 2ε₀(ι + 1)      (ι + 1)(ε₀ + 3 − ι)     −2x         )
          ( −2ε₀           −(ε₀ + 2)       3 + x − ι )            ( 0               0                       2ι − ι² − 1 )

(the middle entry of M¹ is 3 + 2ι − ι² + ε₀(ι + 1)). Since the determinant is linear in each row, P_l is a
polynomial of degree at most 3 in h: its coefficient of h⁰ is det M⁰, that of h¹ the sum of the three determinants
of M⁰ with one row replaced by the same row of M¹, that of h² the sum of the three determinants of M¹ with one row
replaced by the same row of M⁰, and that of h³ is det M¹. Expanding det M⁰ along its first column and det M¹ along
its first row,

    det M⁰ = (2 + x − ι)((4 + x − 2ι)(3 + x − ι) − (ε₀ + 2)x) + 4ε₀x(2 + x − ι) = (2 + x − ι)𝒬(ι, x) = U,
    det M¹ = (2ι − ι²)(ι + 1)(ε₀ + 3 − ι)(2ι − ι² − 1) = ι(ι − 2)(ι − 1)²(ι + 1)(ε₀ + 3 − ι) = R₃.

The first and the third rows of M¹ have one nonzero entry each; expanding along them, and expanding along its first
column the determinant D₂ of M⁰ with its second row replaced by that of M¹,

    R₁ = (2ι − ι²)((4 + x − 2ι)(3 + x − ι) − (ε₀ + 2)x) + D₂ − (ι − 1)²(2 + x − ι)(4 + x − 2ι),
    D₂ = (2 + x − ι)((ι + 1)(ε₀ + 3 − ι)(3 + x − ι) − 2(ε₀ + 2)x) − 4ε₀(ι + 1)((ι − 2)(3 + x − ι) + (ε₀ + 2)x)
         + 4ε₀x(2(ι − 2) + (ι + 1)(ε₀ + 3 − ι)),

and likewise, replacing the first, the second and the third row of M¹ by that of M⁰,

    R₂ = −(ι − 1)²(ι + 1)((2 + x − ι)(ε₀ + 3 − ι) − 4ε₀(ι − 2)) − (2ι − ι²)(ι − 1)²(4 + x − 2ι)
         + (2ι − ι²)((ι + 1)(ε₀ + 3 − ι)(3 + x − ι) − 2(ε₀ + 2)x).

Multiplying out gives the polynomials R₁ and R₂ of [[sec:tab-a-split]]; these are identities in (ι, x, h, ε₀).
Substituting x = hκ, ε₀ = 625/64 and h = 10⁻⁶ gives the coefficients of [[sec:tab-a-sextic]].

(ii) 𝒬(2 + x, x) = 8 + 8x + 2x² − (3x + 10)(2 + x) + x² + 5x + 3ε₀x + 12 = (3ε₀ − 3)x. The value of W at ι = 2 + x is
the s-free part of R₁(2 + x + s, x) ([[sec:tab-a-split]]), −1683x³/64 − 2933x²/32 − 1875x/8 = −(1683/64)x c⁰(x), plus
h R₂(2 + x, x) + h² R₃(2 + x). From the formulas of (i),

    R₂(2 + x, x) = −x(x⁴ + 3x³ − 3x² − 7x + 6 − ε₀(4x³ + 21x² + 27x + 6)),
    R₃(2 + x) = x(2 + x)(1 + x)²(3 + x)(ε₀ + 1 − x),

which at ε₀ = 625/64 are −(1683/64)x c₁(x) and −(1683/64)x c₂(x); indeed c₂ = (2 + x)(1 + x)²(3 + x)(64x − 689)/1683.
The bounds on hc₁ + h²c₂ follow by summing the absolute values of the terms at the right end of each interval, and
the bounds on c from c⁰(0.5) < 10.92, c⁰(4) < 38.86, c⁰(16) < 320.69, c⁰(50) < 2683.2 and c⁰(70) < 5153, c⁰ being
increasing on [0, ∞).

(iii) The discriminant is (3x + 10)² − 8(x² + (5 + 3ε₀)x + 12) = x² − (24ε₀ − 20)x + 4, and 24ε₀ − 20 = 1715/8;
Δ_𝒬(0.01866) > 0 > Δ_𝒬(0.01867). For complex roots |2 + x − ζ|² = (2 + x − ζ)(2 + x − ζ̄) = 𝒬(2 + x, x)/2, and
|ζ|² = a² + b² = ((3x + 10)² − x² + 1715x/8 − 4)/16. b² = −Δ_𝒬/16 has derivative (1715/8 − 2x)/16 > 0 for x < 107.

(iv) On [0.018, x₋], Δ_𝒬 decreases from Δ_𝒬(0.018) < 0.1416, so the smaller root a − Δ_𝒬^(1/2)/4 exceeds
2 + x + (1/2 − x/4) − 0.0941 > 2 + x + 0.401; the larger one is farther. On [x₋, 0.5], |2 + x − ζ| = (1683x/128)^(1/2)
≥ (1683·0.01866/128)^(1/2) > 0.49.

(v) For x₋ < x < x₊ the roots of U(·, x) are 2 + x, ζ and ζ̄, distinct since 𝒬(2 + x, x) ≠ 0 and b > 0, and U has
leading coefficient −2 in ι. For a cubic U with leading coefficient −2 and distinct roots r₁, r₂, r₃, and any
polynomial F, Σ_j F(r_j)/U′(r_j) = −½·(coefficient of ι² in the remainder of F modulo U), because F and its
remainder agree at the roots, and for the polynomials 1, ι, ι² the sum is 0, 0, −½ (Lagrange interpolation of the
remainder at the three roots). So Λ(x) = Σ_j W(r_j)/∂_ιU(r_j). W and U have real coefficients, so
2 Re(W(ζ)/∂_ιU(ζ)) = W(ζ)/∂_ιU(ζ) + W(ζ̄)/∂_ιU(ζ̄) = Λ(x) − W(2 + x, x)/∂_ιU(2 + x, x), and
∂_ιU(2 + x, x) = −𝒬(2 + x, x), so by (ii) the last quotient is c(x). The quotient of W by U is the polynomial 𝒲 of
[[sec:tab-a-split]]: multiplying out, W − 𝒲U has degree at most 2 in ι, and its coefficient of ι² is
−2(Λ⁰ + hΛ₁ + h²Λ₂). The bounds on Π − Π⁰ = h(Λ₁ − c₁) + h²(Λ₂ − c₂) follow by summing the absolute values of the
terms at x = 35 and x = 70; those on the quadratic Π⁰ and on Π⁰′ = 9x/4 − 10598081/215424 from its vertex value
−617.5 at x = 21.87 and its values −79.66, −423.4 and 1989.1 at x = 0, 35, 70. ∎

**Lemma {#lem:s14-majorant}** (Majorants.) Let g(s, x) = Σ_(j,k) g_jk s^j x^k be a polynomial, p a function of x (the
centre), and f(ι, x) := g(ι − p(x), x). Put ḡ(S, T) := Σ_(j,k) |g_jk| S^j T^k. Then |f(ι, x)| ≤ ḡ(S, T) whenever
|ι − p(x)| ≤ S and 0 ≤ x ≤ T, and ḡ increases in S and in T.

*Proof.* The triangle inequality, term by term. ∎

We write N̄ := R̄₂ + hR̄₃ and N̄′ := R̄₂′ + hR̄₃′, which bound R₂ + hR₃ and its ι-derivative on |ι| ≤ S, 0 ≤ x ≤ T
(centre p = 0), and M̄_B, M̄_a (with M̄_B′, M̄_a′ for the s-derivatives) for the majorants of the re-expansions
R₁(2 + x + s, x) and R₁(a(x) + s, x), polynomials in (s, x) with the centres p = 2 + x and p = a(x); all are listed
in [[sec:tab-a-split]]. By the lemma, on |ι − p| ≤ ϱ with p = 2 + x, resp. p = ζ (so that |ι − a| ≤ b + ϱ and
|ι| ≤ |ζ| + ϱ), and x_a ≤ x ≤ x_b for an interval [x_a, x_b] of [[sec:tab-a-pieces]],

    |W| ≤ M̄_B(ϱ, x_b) + hN̄(2 + x_b + ϱ, x_b),   resp.   |W| ≤ M̄_a(b + ϱ, x_b) + hN̄(|ζ| + ϱ, x_b),

and likewise for ∂_ιW with the primed majorants.

**Lemma {#lem:s14-fixed-point}** (A perturbed simple root.) Let p ∈ ℂ, ϱ > 0 and D := {|ι − p| ≤ ϱ}; let V and W be
polynomials with V ≠ 0 on D, and put Ξ := −hW/V. If |Ξ| ≤ ϱ and |Ξ′| ≤ L_Ξ < 1 on D, then (ι − p)V + hW has exactly
one zero ι* in D, and

    |ι* − p| ≤ |Ξ(p)|/(1 − L_Ξ),     |ι* − p − Ξ(p)| ≤ L_Ξ|Ξ(p)|/(1 − L_Ξ).

If p is real and V, W have real coefficients, ι* is real. On D, |Ξ′| ≤ h(sup|W′|/inf|V| + sup|W|·sup|V′|/inf|V|²).

*Proof.* The zeros of (ι − p)V + hW in D are the fixed points of ι ↦ p + Ξ(ι), which maps the closed convex set D into
itself and is a contraction with constant L_Ξ there; so there is exactly one, ι*. Then |ι* − p| = |Ξ(ι*)| ≤ |Ξ(p)| +
L_Ξ|ι* − p|, and |ι* − p − Ξ(p)| = |Ξ(ι*) − Ξ(p)| ≤ L_Ξ|ι* − p|. In the real case the conjugate of ι* is a zero in D,
so equals ι*. The last bound is the quotient rule. ∎

**Lemma {#lem:s14-sextic-count}** (Counting the roots.) (a) For 0 < x ≤ 70, P_l has exactly three roots, counted with
multiplicity, in |ι| < 1000. (b) For x ≥ 70, P_l has no root with |ι − 1| ≤ 50.

*Proof.* (a) For x ≤ 70 the roots of U(·, x) are 2 + x ≤ 72 and the roots of 𝒬(·, x), which by
[[lem:s14-sextic-split]] (iii)–(iv) have modulus at most (3657)^(1/2) < 61. On |ι| = 1000, therefore,
|U| ≥ 928·2·939² > 1.63·10⁹, while by [[lem:s14-majorant]] with p = 0

    |hW| ≤ h(R̄₁(1000, 70) + hR̄₂(1000, 70) + h²R̄₃(1000)) < 10⁻⁶(5.67·10¹² + 4.3·10⁹ + 1.02·10⁶) < 5.7·10⁶.

By Rouché's theorem P_l = U + hW has three zeros in |ι| < 1000, as U has.

(b) If |ι − 1| ≤ 50, then |ι| ≤ 51, Re ι ≤ 51 and |2 + x − ι| ≥ x − 49, and |hW| ≤ h(R̄₁ + hR̄₂ + h²R̄₃)(51, x) ≤
0.00862x² + 1.3823x + 45.381. If 70 ≤ x < x₊, both roots of 𝒬 have real part a = (3x + 10)/4, so they lie at
distance at least y := (3x − 194)/4 ≥ 4 from ι, and |U| ≥ 2(x − 49)y² ≥ 42y²; with x = (4y + 194)/3 the bound on
|hW| becomes at most 0.0156y² + 3.36y + 172, which is less than 42y² for y ≥ 4. If x ≥ x₊, the roots of 𝒬 are real
and at least (3x + 10 − x)/4, as Δ_𝒬(x)^(1/2) < x, so they lie at distance at least y′ := (2x − 194)/4 ≥ 58 from ι,
and |U| ≥ 330y′², while with x = 2y′ + 97 the bound on |hW| becomes at most 0.0345y′² + 6.2y′ + 261 < 330y′². In both
cases |hW| < |U| on the disc, so P_l has no zero there. ∎

#### Degrees with κ ≤ 18000 {#sec:s14-pa-small}

**Lemma {#lem:s14-sextic-small}** (The roots near 2 and 3.) Let 1 ≤ l ≤ 133, so that 3 ≤ κ ≤ 17955 and
3h ≤ x < 0.018 < x₋. The three roots of P_l in |ι| < 1000 are real, and:

(a) for l = 1 they are 2 and one root in each of (2 + 3h, a(x)) and (a(x), 3 − δ_C);

(b) for l = 2 they lie one in each of (2 + 2.93h, 2 + 2.94h), (2 + 8h, a(x)) and (a(x), 3 − δ_C);

(c) for 3 ≤ l ≤ 133 they lie one in each of (2 + δ_C, 2 + x), (2 + x, a(x)) and (a(x), 3 − δ_C).

*Proof.* We use four signs.

(α) P_l(2 + x) = hW(2 + x, x) = −(1683/64)h x c(x) < 0, by [[lem:s14-sextic-split]] (ii), as U(2 + x, x) = 0.

(β) P_l(a(x)) > 0. Indeed 2 + x − a = −(2 − x)/4 and 𝒬(a, x) = −Δ_𝒬(x)/8, so U(a, x) = (2 − x)Δ_𝒬(x)/32 ≥
1.982·0.1415/32 > 0.0087, Δ_𝒬 being decreasing on [0, 0.018]; and |W(a, x)| ≤ M̄_a(0, 0.018) + hN̄(2.52, 0.018) < 49,
the s-free part of R₁(a + s, x) being at most 47.6 in modulus there. So |hW| < 5·10⁻⁵.

(γ) P_l(3 − δ_C) < 0. By [[sec:tab-a-expansions]] with ξ = −2.94, P_l(3 − δ_C) = h(L₀(−2.94, κ) + E) with
L₀(−2.94, κ) = −1619κ/64 − 2.12 and |E| ≤ h(10⁻⁶κ³ + 24.3κ² + 414κ + 1290) ≤ 0.439κ + 0.0013 for κ ≤ 18000.

(δ) By [[sec:tab-a-expansions]], P_l(2 + hξ) = h²(G₀(ξ, κ) + E) with |E| ≤ h(κ³ + 20κ² + 690κ + 1251) for |ξ| ≤ 3.
At κ = 8, |E| ≤ 0.0086, G₀(2.93, 8) = 0.8968… and G₀(2.94, 8) = −2.9043…, so P_2(2 + 2.93h) > 0 > P_2(2 + 2.94h).
For 15 ≤ κ ≤ 18000, G₀(2.94, κ) = (1811κ² − 11133.66κ)/64 − 422.1968… ≥ 28.29κ² − 174κ − 422.2, while hκ³ ≤ 0.018κ²
gives |E| ≤ 0.0181κ² + 0.0007κ + 0.0013; the difference exceeds 3300 at κ = 15 and increases, so P_l(2 + δ_C) > 0.

In (c), 2 + δ_C < 2 + x < a(x) < 3 − δ_C and the signs of P_l at these points are +, −, +, −; so P_l has a root in
each of the three open intervals. These are three distinct roots in |ι| < 1000, hence all of them by
[[lem:s14-sextic-count]]. In (b), the signs at 2 + 2.93h, 2 + 2.94h give the first root, and the signs −, +, − at
2 + 8h = 2 + x, a(x), 3 − δ_C the other two. In (a), P_1(2) = 0 ([[prop:np-10-12]] (iii)), and the signs −, +, − at
2 + 3h = 2 + x, a(x), 3 − δ_C give two more roots; so the root 2 is simple. ∎

#### Degrees with κ ≥ 18000 {#sec:s14-pa-large}

**Lemma {#lem:s14-sextic-large}** (Location of the roots.) Let l ≥ 134, so that x ≥ 0.018, and let x ≤ 70. Each
statement uses the row of [[sec:tab-a-pieces]] whose interval [x_a, x_b] contains x.

(a) P_l has exactly one root ι_B with |ι_B − (2 + x)| ≤ ϱ; it is real, and |ι_B − 2 − x + hc(x)| ≤ e_B.

(b) If x ≤ 0.03, the other two roots of P_l in |ι| < 1000 lie in |ι − a(x)| < 0.45.

(c) If x ≥ 0.03, P_l has exactly one root ι_P with |ι_P − ζ| ≤ ϱ, its conjugate is the only root with
|ι − ζ̄| ≤ ϱ, and

    |ι_P − ζ| ≤ Ξ_ζ/(1 − L_Ξ),     |Re ι_P − a(x) + hΠ(x)/2| ≤ e_P,

with Ξ_ζ, L_Ξ and e_P from the row. The roots ι_B, ι_P and ῑ_P are the three roots of P_l in |ι| < 1000.

*Proof.* (a) U = (ι − (2 + x))V_B with V_B := −𝒬, so [[lem:s14-fixed-point]] applies with p = 2 + x, V = −𝒬 and
Ξ_B = hW/𝒬. On the disc, |𝒬| ≥ 2(d_* − ϱ)² ≥ 𝒬_min with d_* the distance bound of the row (from
[[lem:s14-sextic-split]] (iv) in the first row and from |2 + x − ζ| = (1683x/128)^(1/2) ≥ (1683x_a/128)^(1/2) in the
others), and |∂_ι𝒬| = |4(ι − 2 − x) + x − 2| ≤ 4ϱ + max(2, x_b − 2) ≤ 𝒬′_max. With the majorant bounds M₀, M₁ of
the row, |Ξ_B| ≤ hM₀/𝒬_min ≤ ϱ and |Ξ_B′| ≤ L_Ξ < 1. As Ξ_B(2 + x) = hW(2 + x, x)/𝒬(2 + x, x) = −hc(x) by
[[lem:s14-sextic-split]] (ii), the lemma gives the root, real, with |ι_B − 2 − x + hc(x)| ≤ L_Ξhc(x)/(1 − L_Ξ) ≤ e_B.

(b) For 0.018 ≤ x ≤ 0.03, |Δ_𝒬(x)| ≤ max(Δ_𝒬(0.018), −Δ_𝒬(0.03)) < 2.4304, so the roots of 𝒬 lie within 0.3898 of a.
On |ι − a| = 0.45 they are at distance at least 0.0602 from ι, and |2 + x − ι| ≥ (1/2 − x/4) − 0.45 ≥ 0.0425, so
|U| ≥ 0.0425·2·0.0602² > 3.08·10⁻⁴, while |hW| ≤ h(M̄_a(0.45, 0.03) + hN̄(2.98, 0.03)) < 10⁻⁶·94. By Rouché's theorem
P_l has two zeros in |ι − a| < 0.45, as U has (2 + x lies outside, |2 + x − a| = 1/2 − x/4 > 0.49).

(c) U = (ι − ζ)V with V(ι) := 2(2 + x − ι)(ι − ζ̄). On |ι − ζ| ≤ ϱ, |V| ≥ 2(d⁻ − ϱ)(2b⁻ − ϱ) ≥ V_min and
|V′| = |2(2 + x − ι) − 2(ι − ζ̄)| ≤ 2(d⁺ + ϱ) + 2(2b⁺ + ϱ) ≤ V′_max, with the bounds d^±, b^±, r⁺ of the row from
[[lem:s14-sextic-split]] (iii). With M₀, M₁ of the row, |Ξ| ≤ hM₀/V_min ≤ ϱ and |Ξ′| ≤ L_Ξ < 1, and |Ξ(ζ)| =
h|W(ζ)|/|V(ζ)| ≤ hM_ζ/(4d⁻b⁻) ≤ Ξ_ζ, as |V(ζ)| = 2|2 + x − ζ|·2b. [[lem:s14-fixed-point]] gives ι_P and the first
bound. Since V(ζ) = ∂_ιU(ζ), [[eq:s14-pa-re]] gives Re Ξ(ζ) = −hΠ(x)/2, and
|Re(ι_P − ζ − Ξ(ζ))| ≤ L_Ξ|Ξ(ζ)|/(1 − L_Ξ) ≤ e_P. The conjugate statement follows from the real coefficients.
Finally, with ϱ_B and ϱ_P the radii of the two tables, ϱ_P < b⁻ and ϱ_B + ϱ_P < d⁻ for every pair of rows,
so the discs about 2 + x, ζ and ζ̄, resp. the disc of (b) and the disc about 2 + x (as 0.45 + 0.001 < 0.49), are
disjoint and lie in |ι| < 1000; by [[lem:s14-sextic-count]] they hold all three roots there. ∎

**Lemma {#lem:s14-crossings}** (The crossings of the integers.) Let l ≥ 1 with 0.5 ≤ x ≤ 70, and let 3 ≤ n ≤ 51 be an
integer. With K_n and K′_n as in [[sec:tab-a-crossings]]:

(a) if |ι_B − n| ≤ δ_C, then |κ − K_n| < 3.1 when n ≤ 17 and |κ − K_n| < 33 when n ≥ 18;

(b) if |Re ι_P − n| ≤ δ_C, then |κ − K′_n| < 27 when n ≤ 28 and |κ − K′_n| < 103 when n ≥ 29.

*Proof.* (a) By [[lem:s14-sextic-large]] (a), ι_B = 2 + x − hc(x) + ξ_B with |ξ_B| ≤ e_B ≤ 29h. If |ι_B − n| ≤ δ_C,
then |x − (n − 2) − hc(x)| ≤ δ_C + e_B; dividing by h,

    |κ − (n − 2)/h − c(x)| ≤ (δ_C + e_B)/h,     |x − (n − 2)| ≤ hc(x) + δ_C + e_B.

As c ≤ 5155, |x − (n − 2)| < 0.006; so n ≤ 17 gives x < 15.01, where e_B ≤ 0.1h, c ≤ 321 and |x − (n − 2)| ≤ 325h,
and n ≥ 18 gives x ≤ 49.01, where e_B ≤ 29h, c ≤ 2684 and |x − (n − 2)| ≤ 2716h. Since K_n = (n − 2)/h + c⁰(n − 2),

    |κ − K_n| ≤ (δ_C + e_B)/h + |c(x) − c⁰(x)| + |c⁰(x) − c⁰(n − 2)|,

and c⁰′(y) = 2y + 5866/1683 is at most 35.5 on [0, 16] and 103.5 on [0, 50]. By [[lem:s14-sextic-split]] (ii) this is
at most 2.94 + 0.1 + 0.011 + 35.5·325·10⁻⁶ < 3.1 for n ≤ 17, and 2.94 + 29 + 0.43 + 103.5·2716·10⁻⁶ < 33 for n ≥ 18.

(b) By [[lem:s14-sextic-large]] (c), Re ι_P = a(x) − hΠ(x)/2 + ξ_P with |ξ_P| ≤ e_P. Put x_n := (4n − 10)/3, so that
a(x) − n = 3(x − x_n)/4. If |Re ι_P − n| ≤ δ_C, then |x − x_n − 2hΠ(x)/3| ≤ 4(δ_C + e_P)/3, so

    |κ − x_n/h − 2Π(x)/3| ≤ 4(δ_C + e_P)/(3h),     |x − x_n| ≤ 2h|Π(x)|/3 + 4(δ_C + e_P)/3,

and, as K′_n = x_n/h + 2Π⁰(x_n)/3,

    |κ − K′_n| ≤ 4(δ_C + e_P)/(3h) + (2/3)(|Π(x) − Π⁰(x)| + |Π⁰(x) − Π⁰(x_n)|).

If n ≤ 28 then x ≤ 35 (as |x − x_n| < 0.002 and x₂₈ = 34), so e_P ≤ 17h, |Π| ≤ 619, |x − x_n| ≤ 440h, and by
[[lem:s14-sextic-split]] (v) the right side is at most (4/3)(19.94) + (2/3)(0.57 + 49.2·440·10⁻⁶) < 27. If n ≥ 29
then x ≥ 35, e_P ≤ 72h, |Π| ≤ 1995, |x − x_n| ≤ 1430h, and the right side is at most
(4/3)(74.94) + (2/3)(4.17 + 108.4·1430·10⁻⁶) < 103. ∎

#### The distance from the integers, and ε_ind at γ_C = 10⁶ {#sec:s14-pa-distance}

**Proposition {#prop:s14-damping-distance}** (The roots of the constraint damping polynomials at γ_C = 10⁶.) Let
h = 10⁻⁶, and let ι be a root of P_l (l ≥ 1), of P_0 or of p_(v) (l ≥ 1) with |ι − 1| ≤ 50 and ι ∉ ℤ. Then

    dist(Re ι, ℤ) > 2.94·10⁻⁶,

except for the root of P_2 near 2, which satisfies 2.93·10⁻⁶ < ι − 2 < 2.94·10⁻⁶. In particular every such root has
dist(Re ι, ℤ) > 2.93·10⁻⁶ > 2.9·10⁻⁶, the least distance occurring at scalar type l = 2. The only roots of P_l
(l ≥ 1) and of P_0 that are integers and satisfy |ι − 1| ≤ 50 are ι = 2 at l = 0 and at l = 1.

*Proof.* *Vector type.* By [[lem:s14-vector-distance]], the smaller root of p_(v) has |ι − 1| > 50, and a non-integer
larger root ι_v ≤ 51 has distance at least 2.9997·10⁻⁶ > δ_C from ℤ.

*Scalar type 0.* P_0 = −(ι − 2)C; the roots of C other than ι₁ have real part below −100 (proof of
[[prop:np-10-54]]), and ι₁ ∈ (2 + δ_C, 5/2) by [[lem:s14-scalar-zero]].

*Scalar type l ≥ 1, κ ≤ 18000.* By [[lem:s14-sextic-count]] (a) three roots have |ι| > 1000, and by
[[lem:s14-sextic-small]] the other three lie in (2, 3) at distance more than δ_C from 2 and from 3, except ι = 2 at
l = 1 and the root of P_2 in (2 + 2.93h, 2 + 2.94h).

*Scalar type l ≥ 1, 0.018 ≤ x ≤ 70.* Three roots have |ι| > 1000; the others are those of
[[lem:s14-sextic-large]]. For x ≤ 0.5, ι_B lies between 2 + x − hc(x) − e_B > 2.0179 and 2 + x ≤ 2.5; for
x ≤ 0.03 the other two have real parts in (a − 0.45, a + 0.45) ⊂ (2.06, 2.98); and for 0.03 ≤ x ≤ 0.5,
|ι_P − ζ| ≤ 0.0023, so Re ι_P ∈ (2.52, 2.88). For 0.5 ≤ x ≤ 70, ι_B > 2.49 and Re ι_P > 2.87. If one of them lies in
|ι − 1| ≤ 50, its real part is at most 51, so an integer n with |Re ι − n| ≤ δ_C satisfies 3 ≤ n ≤ 51, and for such
an n [[lem:s14-crossings]] gives |κ − K_n| < 3.1, resp. 33, or |κ − K′_n| < 27, resp. 103. By
[[sec:tab-a-crossings]], every value l(l + 2) differs from K_n by more than 14.39 for n ≤ 17 and by more than 321.67
for n ≥ 18, and from K′_n by more than 141.07 for n ≤ 28 and by more than 392.12 for n ≥ 29. So no such n exists,
and the real part is more than δ_C from every integer.

*Scalar type l ≥ 1, x ≥ 70.* No root has |ι − 1| ≤ 50, by [[lem:s14-sextic-count]] (b).

The cases show that a root within δ_C of an integer, with |ι − 1| ≤ 50, is ι = 2 at l = 0 or l = 1 or the root of
P_2 near 2. ∎

**Corollary {#cor:s14-eps-ind-point}** (ε_ind at γ_C = 10⁶.) ε_ind(10⁻⁶) = δ_50, where the infimum of
[[prop:np-10-52]] (iii) is taken over all the lists ℛ^sc_l (l ≥ 0), ℛ^v_l (l ≥ 1) and ℛ^t_l (l ≥ 2), the scalar types
0 and 1 included. It is attained by the entry −49 − δ_50 of ℛ^sc_50, and
1.941370568463·10⁻⁸ < δ_50 < 1.941370568464·10⁻⁸. Every entry of these lists at h = 10⁻⁶ that comes from a root of
P_l, of C or of p_(v), is not an integer and has modulus at most 50 lies at distance more than 2.93·10⁻⁶ from ℤ.

*Proof.* The entries that do not depend on h are the integers −l, l + 2, 2 − l, l + 4, 1 − l and l + 3, the four
roots of Q_l(ι − 1) for each l ≥ 1 (at l = 1 these are 2 − ι^Υ_(s1,j) and 1 + ι^Υ_(s1,j), j = 2, 3), and at scalar
type 0 the numbers 2 − ι^Υ_(s0,2) and 1 + ι^Υ_(s0,2). By [[prop:np-10-52]] (iii) and its proof, the least distance
from ℤ of such an entry that is not an integer and has |ι| ≤ 50 is δ_50, attained by 1 − l − d₂ at l = 50, which is
−49 − δ_50. At the scalar types 0 and 1 these distances are ι^Υ_(s0,2) − 2 = z/(3/2 + (9/4 + z)^(1/2)) >
z/(3 + z/3) > 1.33·10⁻⁶, and, at u = 2, d₂ = z(1 + θ₂)/12 > 3.3·10⁻⁷ and d₁ = 3z(1 + θ₁)/20 > 5.9·10⁻⁷ by
[[eq:s14-theta]]; all exceed δ_50. The remaining entries are ι − 1 for the roots ι of P_l and of p_(v), l ≥ 1, and of
C at scalar type 0, those that [[ch:s15]] removes left out. The roots of C are roots of P_0 = −(ι − 2)C, so
dist(Re(ι − 1), ℤ) = dist(Re ι, ℤ) > 2.93·10⁻⁶ > δ_50 by [[prop:s14-damping-distance]] whenever ι − 1 ∉ ℤ and
|ι − 1| ≤ 50. So the infimum is a minimum, equal to δ_50, and [[lem:s14-delta50]] gives its value. ∎

**Remark {#rem:s14-eps-ind-scope}** (The point h = 10⁻⁶ and the set 𝖧.) The theorems of this paper take h in
𝖧 = (0, h_*) ∖ 𝖹 ([[eq:iv4-0-1]]), and h_* = min(10⁻⁶, h_0, h_tf) ≤ 10⁻⁶; so h = 10⁻⁶ is not in 𝖧, and
[[prop:s14-damping-distance]] and [[cor:s14-eps-ind-point]] are used by none of them. For h ∈ 𝖧 the theorems use only
0 < ε_ind(h) ≤ δ_50, which [[prop:np-10-52]] (iii) gives for every such h. [[lem:s14-delta50]] and
[[prop:gap-sums]] concern numbers that depend on z only, so they hold whatever h is. What changes for h ∈ 𝖧 is
the location of the roots of P_l, P_0 and p_(v): the arguments of this section use h = 10⁻⁶ in every constant, and
this paper does not determine ε_ind(h) for h ∈ 𝖧 beyond 0 < ε_ind(h) ≤ δ_50. The corollary shows that this upper
bound is attained at the end h = 10⁻⁶ of the interval on which ε_ind is defined.

#### Sums of the gauge potential offsets {#sec:pa-gap-sums}

Let z = 4e_Υγ_Υ² = 4·10⁻⁶ and λ_♯ = 3/2 + (1 − e_Υ)γ_Υ = 15099/10000 ([[ch:s20]]) at (e_Υ, γ_Υ) = (1/100, 1/100).
For l ≥ 1 let d₁(l) and d₂(l) be the numbers d₁ and d₂ of [[prop:np-10-52]] (i) at u = l + 1, so that
ι^Υ_(sl,l+1) = l + 1 + d₂(l) and ι^Υ_(sl,l+2) = l + 2 + d₁(l), and recall ι^Υ_(s0,2) = ½ + (9/4 + z)^(1/2)
([[sec:s14-simple]]). Put

    𝔡₀ := ι^Υ_(s0,2) − 2 = (9/4 + z)^(1/2) − 3/2,     𝔡₁ := ι^Υ_(s1,2) − 2 = d₂(1),
    δ₂ := d₂(2),     δ′₁ := d₁(1).

By [[def:iii-i9-gap]], 𝔡₀ = −μ_c0 = d_c0 and 𝔡₁ = −μ_c1 = d_c1 are the offsets of the two class roots.

**Proposition {#prop:gap-sums}** (Sums of the offsets above 2 and 3.) Let 𝒮 be the set of the numbers g + t + n𝔡₁
with g ∈ {2, 3, λ_♯}, t ∈ {0, 1, 1 + 𝔡₀, 1 + δ₂, 1 + δ′₁} and n = 0, 1, 2, …. The least positive number of the form
s − k with s ∈ 𝒮 and k ∈ {2, 3} is

    λ_♯ + 4470304𝔡₁ − 3 ∈ (5.0190·10⁻⁸, 5.0193·10⁻⁸),

and every other positive s − k exceeds 1.3888·10⁻⁷. In particular no element of 𝒮 lies in (2, 2 + ε] ∪ (3, 3 + ε]
when ε < 5.019·10⁻⁸, a bound more than 2.5 times δ_50.

*Proof.* *The offsets.* By [[eq:s14-pa-sqrt]], 𝔡₀ = z/(3/2 + (9/4 + z)^(1/2)) lies between z/(3 + z/3) and z/3, so
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶. By [[prop:np-10-52]] (i), δ₂ = z(1 + θ₂)/15 and δ′₁ = 3z(1 + θ₁)/20 with
|θ₁|, |θ₂| ≤ z by [[eq:s14-theta]], so 2.666655·10⁻⁷ < δ₂ < 2.666678·10⁻⁷ and 5.999975·10⁻⁷ < δ′₁ < 6.000025·10⁻⁷.
For 𝔡₁, at u = 2, 𝔡₁ = ½((9 + B₂)^(1/2) − 3) = B₂/(2(3 + (9 + B₂)^(1/2))) with B₂ := 2z − 4w₂ and w₂ := (4 + A)^(1/2) − 2 =
A/(2 + (4 + A)^(1/2)), A = 4.000004·10⁻⁶. By [[eq:s14-pa-sqrt]], 4 + A/4 − A²/64 ≤ 2 + (4 + A)^(1/2) ≤ 4 + A/4, with
A/4 = 1.000001·10⁻⁶ and A²/64 < 2.6·10⁻¹³; so

    1.00000074999956·10⁻⁶ < w₂ < 1.00000074999963·10⁻⁶,     3.99999700000147·10⁻⁶ < B₂ < 3.99999700000177·10⁻⁶,

and, again by [[eq:s14-pa-sqrt]], B₂/(12 + B₂/3) ≤ 𝔡₁ ≤ B₂/(12 + B₂/3 − B₂²/108), whence

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
ε_K < 5.019·10⁻⁸;
every other λ ∈ 𝒮 is at least λ_♯ + 1 > 5/2, so that λ + d_c0 and λ + d_c1 exceed 2 + ε_K. [[thm:settling]] takes
ε_K < ε_ind(h) ≤ δ_50 < 5.019·10⁻⁸ for every h ∈ 𝖧; so these sums impose no condition beyond those of
[[thm:settling]]. No other result of this paper uses [[prop:gap-sums]].
