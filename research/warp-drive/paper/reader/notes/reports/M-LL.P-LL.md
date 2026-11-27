### Interpolation on Chebyshev points and the size of λ_L {#sec:ll-chebyshev}

This text gives the interpolation lemma of [[sec:layer-window]] on the Chebyshev points, the theorem of the literature
it rests on, and the size of the threshold λ_L of [[thm:layer]] for the envelope env_C. The thresholds of
[[eq:layer-threshold]] keep their forms, with the constants C_(i,m) of the lemma below.

**Lemma {#lem:layer-interpolation}** (Interpolation on a half-line.) Let f be smooth on ℝ with f = 0 on (−∞, v_s], and
m ≥ 2. Put E_f(v) := sup_(v′≤v) |f(v′)| and M_m(v) := sup_(v′≤v) |f^(m)(v′)|. For 0 < i < m and every v,

    sup_(v′≤v) |f^(i)(v′)| ≤ C_(i,m) E_f(v)^(1−i/m) M_m(v)^(i/m),
    C_(i,m) := min_(κ>0) [2^i T_(m−1)^(i)(1) κ^(−i) + κ^(m−i)/(m − i)!],                    {#eq:layer-interpolation}

where T_n, T_n(cos θ) = cos nθ, is the Chebyshev polynomial of degree n, and
T_n^(i)(1) = Π_(j=0)^(i−1) (n² − j²)/(2j + 1) ([[thm:std-duffin-schaeffer]]). The minimum is attained: with
a := 2^i T_(m−1)^(i)(1),

    C_(i,m) = (m a/(m − i))^(1−i/m) (m/(i (m − i)!))^(i/m),   so   C_(1,m) = m ((2m − 2)^(m−1)/(m − 1)!)^(1/m).

*Proof.* If M_m(v) = 0, f is a polynomial of degree less than m on (−∞, v] vanishing on (−∞, v_s], hence zero there,
and so is the left side; likewise if E_f(v) = 0. Otherwise put n := m − 1, let u ≤ v and H > 0, and let P be the
polynomial of degree at most n interpolating f at the m points x_k := u − H/2 + (H/2) cos(kπ/n), k = 0, …, n. They are
distinct, they lie in I := [u − H, u] ⊂ (−∞, v], and x_0 = u. The polynomial Q(s) := P(u − H/2 + (H/2) s)/E_f(v) has
degree at most n and real coefficients, and |Q(cos(kπ/n))| = |f(x_k)|/E_f(v) ≤ 1 for k = 0, …, n; so by
[[thm:std-duffin-schaeffer]], |Q^(i)(s)| ≤ T_n^(i)(1) for −1 ≤ s ≤ 1 and 1 ≤ i ≤ n. If Q has degree less than n, the
theorem applies instead to (Q + εT_n)/(1 + ε) for ε > 0, which has degree n and modulus at most 1 at the points
cos(kπ/n), since |T_n| = 1 there; letting ε → 0 gives the same bound. Since P^(i)(u) = (2/H)^i E_f(v) Q^(i)(1), the
bound at s = 1 is |P^(i)(u)| ≤ 2^i T_n^(i)(1) E_f(v) H^(−i). The difference g := f − P vanishes at the m nodes, so by
Rolle's theorem g^(i) vanishes at m − i distinct points of I; and (g^(i))^(m−i) = f^(m), since P has degree at most n.
A function with m − i zeros x′_1, …, x′_(m−i) in I equals, at a point x of I, its divided difference on the points
x′_1, …, x′_(m−i), x times Π(x − x′_j), and that divided difference is a value of its (m − i)-th derivative at a point
of I divided by (m − i)!. So |g^(i)(u)| ≤ M_m(v) H^(m−i)/(m − i)!. With H := κ (E_f(v)/M_m(v))^(1/m),

    |f^(i)(u)| ≤ E_f(v)^(1−i/m) M_m(v)^(i/m) (2^i T_n^(i)(1) κ^(−i) + κ^(m−i)/(m − i)!)

for every κ > 0 and u ≤ v. The bracket is a κ^(−i) + b κ^(m−i) with b := 1/(m − i)!. By the weighted arithmetic and
geometric mean inequality with weights (m − i)/m and i/m, in which the powers of κ cancel,

    a κ^(−i) + b κ^(m−i) ≥ (m a κ^(−i)/(m − i))^((m−i)/m) (m b κ^(m−i)/i)^(i/m) = (m a/(m − i))^(1−i/m) (m b/i)^(i/m),

with equality at the one κ > 0 where m a κ^(−i)/(m − i) = m b κ^(m−i)/i. This gives the inequality of the lemma and the
value of C_(i,m). At i = 1, a = 2(m − 1)², so C_(1,m) = (2m(m − 1))^((m−1)/m) (m/(m − 1)!)^(1/m), which is
m ((2m − 2)^(m−1)/(m − 1)!)^(1/m). ∎

**Remark {#rem:layer-threshold-size}** (The size of λ_L.) λ0, C1, C_Φ, C_L11, C_L4 and C_q are not evaluated, and η1
depends on env and τ0, so the threshold [[eq:layer-threshold]] is not evaluated either; it is the threshold that the
proof delivers, not the largest λ for which [[thm:layer]] holds. For the envelope env_C of [[eq:envelope]], however, it
is below 2.71·10⁻¹² whatever those constants are, for every l5, A, τ0, T and K that [[thm:layer]] admits: with
Δτ = τ_end − τ0,

    λ_L ≤ Λ_4 < 2.709·10⁻¹² (1 + C1 Δτ/(2π))^(−1456/1442)   for K = 6,      λ_L ≤ Λ_4 < 2.3·10⁻¹²   for K ≥ 7.

Indeed λ_L ≤ Λ_4 by [[eq:layer-threshold]]. Here p = 14 and m = 56 M = 112 K + 784, as M = 2N + 8 and N = K + 3; so
m = 1456 for K = 6 and m ≥ 1568 for K ≥ 7. Since 4π + 2 C1 Δτ = 4π (1 + C1 Δτ/(2π)), and C1 Δτ ≥ 0, as C1 ≥ 0 and
τ_end ≥ v_start − q0 > τ0,

    Λ_4 = (1 + C1 Δτ/(2π))^(−m/(m−p)) B_m^(−m/(m−p)) ≤ B_m^(−m/(m−p)),      B_m := 32π 2^(−1/m) C_(1,m) M_m^(1/m).
                                                                                                 {#eq:layer-size-base}

*The interpolation constant.* Put n := m − 1. By [[lem:layer-interpolation]], C_(1,m) = m ((2n)^n/n!)^(1/m). The
trapezoidal rule for the concave function ln on each interval [k, k + 1], 1 ≤ k ≤ n − 1, gives
ln n! − (1/2) ln n ≤ ∫_1^n ln x dx = n ln n − n + 1. Hence, using n < m for the second form,

    ln C_(1,m) ≥ ln m + (n ln 2 + n − 1 − (1/2) ln n)/m ≥ ln(2e m) − (ln(2e²) + (1/2) ln m)/m.        {#eq:layer-size-c}

At m = 1456, as ln 1456 = 7.2834482…, 1455 ln 2 = 1008.5291477… and (1/2) ln 1455 = 3.6413805…, the first form gives
ln C_(1,1456) ≥ 7.283448 + 2458.887766/1456 > 8.972244.

*The derivative bound.* All derivatives of env_C vanish at v_s = 1/2, env_C being smooth and zero on (−∞, 1/2]
([[lem:envelope-constant]] (a)). So Taylor's formula with Lagrange's remainder gives, for 0 < x < 3, a point ξ with
env_C(1/2 + x) = env_C^(m)(ξ) x^m/m!, and

    M_m ≥ m! env_C(1/2 + x) x^(−m)      for 0 < x < 3.                                            {#eq:layer-size-taylor}

Put t := 2x/3 ∈ (0, 2). At v = 1/2 + x the argument of β in [[eq:envelope]] is y = t − 1, so cos(πy/2) = sin(πt/2),
1 − y² = t(2 − t) and y²/(1 − y²) = 1/(t(2 − t)) − 1 = 1/(2t) + 1/(4 − 2t) − 1. With c_e > 1
([[lem:envelope-constant]] (b)),

    env_C(1/2 + x) ≥ sin¹²(πt/2) exp(1 − 1/(2t) − 1/(4 − 2t)).                                      {#eq:layer-size-edge}

*K = 6.* Take x = 3/5776 in [[eq:layer-size-taylor]], so t = 1/2888, 1/(2t) = 1444 and 1/(4 − 2t) = 1444/5775. With
s := π/5776 and w := s²/6 < 4.94·10⁻⁸, sin s ≥ s − s³/6 = s (1 − w) and ln(1 − w) ≥ −w/(1 − w) > −10⁻⁷. The midpoint
rule for the concave function ln on each interval [k − 1/2, k + 1/2], 2 ≤ k ≤ 1456, gives
ln 1456! ≥ ∫_(3/2)^(1456.5) ln x dx = 1456.5 ln 1456.5 − 1455 − 1.5 ln 1.5. So [[eq:layer-size-taylor]] and
[[eq:layer-size-edge]] give

    ln M_1456 ≥ (1456.5 ln 1456.5 − 1455 − 1.5 ln 1.5) + (12 ln s − 12·10⁻⁷) − (1443 + 1444/5775) + 1456 ln(5776/3).

As 1456.5 ln 1456.5 = 10608.842431…, 1.5 ln 1.5 = 0.6081976…, ln s = −7.5167367…, 1444/5775 = 0.2500432… and
1456 ln(5776/3) = 11011.515994…, the four groups exceed 9153.2342, −90.200843, −1443.250044 and 11011.515994; so
ln M_1456 > 18631.299 and (1/1456) ln M_1456 > 12.796221. With ln(32π) = 4.6104657… and (ln 2)/1456 = 0.0004760…,

    ln B_1456 > 4.610465 − 0.000477 + 8.972244 + 12.796221 = 26.378453,

and (1456/1442) · 26.378453 > 26.63455, while ln(2.709·10⁻¹²) = −26.634441…. So B_1456^(−1456/1442) < 2.709·10⁻¹², and
[[eq:layer-size-base]] gives the bound for K = 6.

*K ≥ 7.* Here m ≥ 1568. Take x = 3/(4m), so t = 1/(2m) ≤ 1, 1/(2t) = m and 1/(4 − 2t) ≤ 1/2; and sin(πt/2) ≥ t, sin
being concave on [0, π/2]. So env_C(1/2 + x) ≥ (2m)^(−12) e^(1/2 − m) by [[eq:layer-size-edge]], and with m! ≥ (m/e)^m,
which follows from e^m ≥ m^m/m!, [[eq:layer-size-taylor]] gives M_m ≥ e^(1/2) (2m)^(−12) (4m²/(3e²))^m. With the second
form of [[eq:layer-size-c]],

    ln B_m ≥ β(m) := ln(256π/(3e)) + 3 ln m − (14 ln 2 + 3/2 + (25/2) ln m)/m,

and β′(m) ≥ 3/m − 25/(2m²) > 0 for m ≥ 5. As ln(256π/(3e)) = 4.5912950…, ln 2 = 0.6931471…, ln 1568 = 7.3575562… and
ln 1680 = 7.4265490…, β(1568) > 26.598 and β(1680) > 26.809. For K = 7, m = 1568, and [[eq:layer-size-base]] gives
Λ_4 ≤ e^(−(1568/1554) · 26.598) < e^(−26.837) < 2.22·10⁻¹². For K ≥ 8, m ≥ 1680, so ln B_m ≥ β(1680) > 26.809 > 0 and
m/(m − p) > 1, and Λ_4 ≤ B_m^(−1) < e^(−26.809) < 2.28·10⁻¹². The three bounds 2.709·10⁻¹², 2.22·10⁻¹² and 2.28·10⁻¹²
are below 2.71·10⁻¹².

### The result of the literature {#sec:ll-literature}

The lemma uses one published theorem. It belongs in the appendix, in [[sec:std-chebyshev]] after
[[thm:std-chebyshev]]:

**Theorem {#thm:std-duffin-schaeffer}** (Derivatives of a polynomial bounded at the Chebyshev points; [DS41, p. 517;
Theorem III and its proof, p. 525].) In [DS41], T_n(x) = cos(n cos⁻¹ x) is "the Tchebychef polynomial" (p. 517).
Theorem III: "Let f(z) be a polynomial of degree n satisfying |f(cos(νπ/n))| ≤ 1; ν = 0, 1, 2, ⋯, n. Then for
p = 1, 2, 3, ⋯, n,

    |f^(p)(x)| ≤ n²(n² − 1)(n² − 2²) ⋯ (n² − (p − 1)²)/(1 · 3 · 5 ⋯ (2p − 1)).      (19)

The equality occurs only if f(z) ≡ γT_n(z), |γ| = 1." The variable x of (19) ranges over −1 ≤ x ≤ 1: the proof
obtains (19) from "|cf^(p)(x)| ≤ |T_n^(p)(1)|, −1 ≤ x ≤ 1", c > 1 a constant, and ends: "Now T_n(1) = 1 so, using
induction, we find that T_n^(p)(1) is equal to the right-hand side of (19)." The points cos(νπ/n) are the Chebyshev
points x_j of [[thm:std-chebyshev]].

### Placement {#sec:ll-placement}

Each item names the place, the old text and the new text. Line numbers are those of the current chapter sources.

*1. [[ch:equality-layer]], [[sec:layer-window]]: the lemma [[lem:layer-interpolation]] (lines 844–862).* Replace the
whole statement and proof, from the result heading to the end of the proof, by the lemma in [[sec:ll-chebyshev]] above,
verbatim. The heading keeps its key and title, and [[eq:layer-interpolation]] keeps its key. The old text, after the
heading's label marker, is:

    (Interpolation on a half-line.) Let f be smooth on ℝ with f = 0 on (−∞, v_s], and
    m ≥ 2. Put E_f(v) := sup_(v′≤v) |f(v′)| and M_m(v) := sup_(v′≤v) |f^(m)(v′)|. For 0 < i < m and every v,

        sup_(v′≤v) |f^(i)(v′)| ≤ C_(i,m) E_f(v)^(1−i/m) M_m(v)^(i/m),
        C_(i,m) := min_(κ>0) [Λ_(i,m) κ^(−i) + ((m − 1) κ)^(m−i)/(m − i)!],      (its equation label)

    where Λ_(i,m) := Σ_k |l_k^(i)(0)| for the Lagrange basis (l_k) on the nodes 0, −1, …, −(m − 1). In particular
    C_(i,m) ≤ Λ_(i,m) + (m − 1)^(m−i).

    *Proof.* If M_m(v) = 0, f is a polynomial of degree less than m on (−∞, v] vanishing on (−∞, v_s], hence zero
    there, and so is the left side; likewise if E_f(v) = 0. Otherwise let u ≤ v and h > 0, and let P be the
    polynomial of degree at most m − 1 interpolating f at u, u − h, …, u − (m − 1)h, all in (−∞, v]. Then
    P^(i)(u) = h^(−i) Σ_k f(u − kh) l_k^(i)(0), so |P^(i)(u)| ≤ Λ_(i,m) E_f(v) h^(−i). The difference g := f − P
    vanishes at the m nodes, which lie in an interval I of length (m − 1)h, so by Rolle's theorem g^(i) vanishes at
    m − i distinct points of I; and (g^(i))^(m−i) = f^(m), since P has degree at most m − 1. A function with m − i
    zeros x_1, …, x_(m−i) in I equals, at a point x of I, its divided difference on the points x_1, …, x_(m−i), x
    times Π(x − x_j), and that divided difference is a value of its (m − i)-th derivative divided by (m − i)!.
    So |g^(i)(u)| ≤ M_m(v) ((m − 1)h)^(m−i)/(m − i)!. With h := κ (E_f(v)/ M_m(v))^(1/m), |f^(i)(u)| ≤
    E_f^(1−i/m) M_m^(i/m) (Λ_(i,m) κ^(−i) + ((m − 1)κ)^(m−i)/(m − i)!); minimise over κ. κ = 1 gives the last
    claim. ∎

(The old text is quoted with its line breaks moved and its equation label marker written as "(its equation label)";
its words are otherwise unchanged.)

*2. [[ch:equality-layer]], [[sec:layer-threshold]]: the remark [[rem:layer-threshold-size]] (lines 1354–1365).*
Replace the whole remark by the remark in [[sec:ll-chebyshev]] above, verbatim, with its four new equation keys
[[eq:layer-size-base]], [[eq:layer-size-c]], [[eq:layer-size-taylor]] and [[eq:layer-size-edge]], which no other place
cites. The old text, after the heading's label marker and with its line breaks moved, is:

    (The size of λ_L.) λ0, C1, C_Φ, C_L11, C_L4 and C_q are not evaluated, and η1 depends on env and τ0, so the
    threshold [[eq:layer-threshold]] is not evaluated either; it is the threshold that the proof delivers, not the
    largest λ for which [[thm:layer]] holds. For the envelope env_C of [[eq:envelope]], however, it is at most
    10^(−430) whatever those constants are, for every l5, A, τ0, T and K that [[thm:layer]] admits. Indeed
    m ≥ 56 · 26 = 1456, as N ≥ 9. The envelope env_C has support [1/2, 7/2], so v_s = 1/2, and its maximum c_e > 1
    is taken at v = 2 = v_s + 3/2 ([[lem:envelope-constant]]); all its derivatives vanish at v_s, so Taylor's
    formula gives c_e ≤ M_m (3/2)^m/m!, that is M_m ≥ m! c_e (2/3)^m, and with m! ≥ (m/e)^m,
    M_m^(1/m) ≥ (2/3)(m/e) ≥ 357. For the constant of [[eq:layer-interpolation]] at i = 1: by Lagrange's
    formula |l_k′(0)| = C(m − 1, k)/k for 1 ≤ k ≤ m − 1, so Λ_(1,m) ≥ C(m − 1, ⌊(m − 1)/2⌋)/m ≥ 2^(m−1)/m² ≥ 10^430. In
    the minimum of [[eq:layer-interpolation]], for κ ≤ 1 the first term is at least Λ_(1,m), and for κ ≥ 1 the
    second is at least (m − 1)^(m−1)/(m − 1)! ≥ e^(m−2)/(m − 1) ≥ 10^600, using n! ≤ n^(n+1) e^(1−n). So
    C_(1,m) ≥ 10^430, the base of Λ_4 exceeds 10^430, and since m/(m − p) ≥ 1, λ_L ≤ Λ_4 ≤ 10^(−430).

*3. [[ch:scope]], [[sec:scope-constants]], lines 97–98.* Old: "threshold that the proof delivers, not the largest λ
for which [[thm:layer]] holds, and for the envelope env_C it is at most 10^(−430) ([[rem:layer-threshold-size]])."
New, as two lines:

    threshold that the proof delivers, not the largest λ for which [[thm:layer]] holds, and for the envelope env_C it is
    below 2.71·10⁻¹² ([[rem:layer-threshold-size]]).

*4. The appendix of results from the literature, its opening paragraph, lines 8–12.* Old: "[See64] and [MM87] are
cited by their journal pages". New: "[See64], [MM87] and [DS41] are cited by their journal pages". The old lines 8–12,
from "the arXiv text of [BGP]" to "the letters are the source's.", become:

    the arXiv text of [BGP] carries the book's page numbers, [See64], [MM87] and [DS41] are cited by their journal pages,
    [Mel93] by the page of the author's online edition (version 5.0E, 1993), [Hö90], [RS1] and [Tre19] by the pages of
    the printed books, and [DLMF] by equation number. Quotation marks enclose the source's own wording, transcribed into
    this edition's typography; an ellipsis marks words of the statement left out because no proof here depends on them.
    Inside each item the letters are the source's.

*5. The appendix of results from the literature, [[sec:std-chebyshev]].* Old: the section ends with
[[thm:std-chebyshev]], whose last line is "…". Here log is the natural logarithm." New: after that line, a blank line
and [[thm:std-duffin-schaeffer]] as stated in [[sec:ll-literature]] above, verbatim, from its result heading to its last
sentence "The points cos(νπ/n) are the Chebyshev points x_j of [[thm:std-chebyshev]]."

*6. The references.* Old: the entry [DS23] is followed directly by the entry [Dya16]. New: between them, the entry

    - [DS41] R. J. Duffin, A. C. Schaeffer, *A refinement of an inequality of the brothers Markoff*, Trans. Amer. Math.
      Soc. 50 (1941), 517–528. doi:10.1090/S0002-9947-1941-0005942-4

*7. Unchanged.* [[eq:layer-threshold]] and the rest of [[sec:layer-threshold]]: every form stays, Λ_4, Λ_5′, C_ε and
Λ_8b–Λ_8d taking the new values of C_(i,m). [[cor:layer-interpolation-band]], [[lem:layer-levels]], the statement and
proof of [[thm:layer]], [[thm:layer-past]] and [[prop:layer-regions]], which use the lemma only through its inequality.
The sentence of [[ch:lambda0]] saying that the lower end c_e > 1 is also what [[rem:layer-threshold-size]] uses stays
true, as the new remark uses only c_e > 1. The sentence of [[rem:edge-thresholds]] citing [[rem:layer-threshold-size]]
states no size and stays.
