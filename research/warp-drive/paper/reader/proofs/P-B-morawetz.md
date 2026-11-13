This part makes the multiplier bounds of [[ch:resolvent-bounds]] explicit on five-dimensional
Schwarzschild–Tangherlini with mass parameter m = 1, so that f = 1 − 1/r² and the horizon is r = 1. Every multiplier
is algebraic in r, every weight is (1 − r⁻²)r⁻³ times a rational function of r⁻², and every constant is obtained from
exact rational inequalities.

### The multiplier identity {#sec:morawetz-identity}

Throughout, y := 1/r² ∈ (0, 1), z := 1 − 2y ∈ (−1, 1) and η(y) := (1 − y)y^(3/2) = (r² − 1)/r⁵. The tortoise coordinate
r_* has dr_*/dr = 1/f, and g′ := dg/dr_*. Since dy/dr = −2y^(3/2),

    d/dr_* = −2η(y) d/dy.                                                                            {#eq:pb-tortoise}

As r_* → −∞, y → 1 and 1 − y decays like e^(2r_*); as r_* → ∞, r_* = r + O(log r). The interval I := {6/5 ≤ r ≤ 4} is
{1/16 ≤ y ≤ 25/36} = {−7/18 ≤ z ≤ 7/8}. With r_* = r + ½ log((r − 1)/(r + 1)), its length is
Λ := 14/5 + ½ log(33/5) < 3.7436. We write ‖·‖ for the norm of L²(ℝ, dr_*) and ‖·‖_I for that of L²(I, dr_*).

Since η_y = y^(1/2)(3/2 − 5y/2), η increases on [0, 3/5] and decreases on [3/5, 1]; so on an interval of y its least
value is attained at an end. We use η(1/16) = 15/1024, η(1/2) = 2^(−5/2), η(25/36) = 1375/7776 > 2^(−5/2) (as
32 · 1375² > 7776²) and max η = η(3/5) = 6√15/125. At a rational r, η = (r² − 1)/r⁵ is rational.

The potentials. Put U := f/r² = (1 − y)y, Q := f/r⁴ = (1 − y)y² and V_(a,b) := aU + bQ = (1 − y)(ay + by²). With
κ := l(l + 2), the potentials V_0, V_1, V_2 of [[prop:np-10-16]] are V_(κ+3/4,b) with b = 9/4, 5/4 and −7/4 (V_0 is the
scalar wave, V_1 the vector-type and V_2 the scalar-type 1-forms); those of [[thm:s15-ki]] are V_T = V_0 and
V_V = V_(κ+3/4,−27/4), and V_S = (1 − y)yQ_S/(16H²), with Q_S the polynomial [[eq:s15-ki-q]] at ς = y, p := κ − 3 and
H := p + 6y.

**Lemma {#lem:morawetz-identity}** (The multiplier identity.) Let V be a real smooth function on ℝ with V, V′ integrable
and V, V′ → 0 at ±∞. Let φ and q be real smooth functions on ℝ with |φ| ≤ 1, φ → ±1 at ±∞, and φ′, φ″, φ‴, q, q′, q″
integrable and tending to 0 at ±∞. Let σ ≠ 0 be real, f ∈ L²(ℝ) vanish outside I, and let u be a C² solution of
−u″ + (V − σ²)u = f with u − c_±e^(±iσr_*) → 0 and u′ ∓ iσu → 0 as r_* → ±∞. Then, with integrals over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2σ²∫q|u|² = Re∫f(2φū′ + (φ′ − 2q)ū) + 2σ²(|c_+|² + |c_−|²),
    W := −φV′ − ½φ‴ + q″ − 2qV,                                                                      {#eq:pb-identity}

and σ(|c_+|² + |c_−|²) = −Im∫fū. Suppose moreover that φ′ − q ≥ 0, q ≥ 0 and W ≥ 0 on ℝ, and put
m′ := min_I (φ′ − q) > 0, M′ := max_I |φ′ − 2q| and w_I := min_I W > 0. Then X := ‖u′‖_I and Y := ‖u‖_I satisfy

    Y ≤ B‖f‖,     B := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2);                                       {#eq:pb-bound}

for every B̃ with Y ≤ B̃‖f‖, X ≤ X(B̃)‖f‖ with X(B̃) := (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′); and for every
decomposition W = W_0 + W_1 with W_0, W_1 ≥ 0 on ℝ, ∫_I W_1|u|² ≤ (2X(B̃) + (M′ + 2|σ|)B̃)‖f‖².

*Proof.* The hypotheses make u and u′ bounded, and every integral in [[eq:pb-identity]] absolutely convergent. With
Re(u″ū) = ½(|u|²)″ − |u′|² and Re(u′ū) = ½(|u|²)′, one checks term by term:

    Re(−u″ · 2φū′) = −(φ|u′|²)′ + φ′|u′|²,
    Re(−u″ · φ′ū) = −(φ′Re(u′ū))′ + φ′|u′|² + (½φ″|u|²)′ − ½φ‴|u|²,
    Re((V − σ²)u · 2φū′) = ((V − σ²)φ|u|²)′ − (φV′ + (V − σ²)φ′)|u|²,
    Re((V − σ²)u · φ′ū) = (V − σ²)φ′|u|²,
    Re((−u″ + (V − σ²)u) · (−2qū)) = (q(|u|²)′ − q′|u|²)′ + q″|u|² − 2q|u′|² − 2qV|u|² + 2σ²q|u|².

Adding, Re(f(2φū′ + (φ′ − 2q)ū)) = 2(φ′ − q)|u′|² + W|u|² + 2σ²q|u|² + E′, where
E := −φ|u′|² − φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² + q(|u|²)′ − q′|u|². At ±∞, |u′|² → σ²|c_±|², |u|² → |c_±|² and
φ′, φ″, q, q′, V → 0, so E → −2σ²φ(±∞)|c_±|² = ∓2σ²|c_±|². Integrating over ℝ gives [[eq:pb-identity]]. Next,
Im(fū) = −Im(u″ū) = −(Im(u′ū))′, and Im(u′ū) → ±σ|c_±|² at ±∞; integrating gives the flux identity.

Under the sign conditions every integrand on the left of [[eq:pb-identity]] is nonnegative. Dropping the term with q and
restricting the other two to I, the left side is at least 2m′X² + w_IY². On the right, f vanishes off I and |φ| ≤ 1, so
the integral is at most ‖f‖(2X + M′Y), and 2σ²(|c_+|² + |c_−|²) = −2σIm∫fū ≤ 2|σ|‖f‖Y. Hence

    2m′X² + w_IY² ≤ ‖f‖(2X + (M′ + 2|σ|)Y).                                                          {#eq:pb-energy}

By the Cauchy–Schwarz inequality, 2X + (M′ + 2|σ|)Y ≤ (2/m′ + (M′ + 2|σ|)²/w_I)^(1/2)(2m′X² + w_IY²)^(1/2), so
(2m′X² + w_IY²)^(1/2) ≤ (2/m′ + (M′ + 2|σ|)²/w_I)^(1/2)‖f‖ and w_I^(1/2)Y ≤ (2m′X² + w_IY²)^(1/2), which is
[[eq:pb-bound]]. Dropping w_IY² in [[eq:pb-energy]] and using Y ≤ B̃‖f‖ gives 2m′X² − 2‖f‖X − (M′ + 2|σ|)B̃‖f‖² ≤ 0, so
X is at most the positive root, X(B̃)‖f‖. Finally the left side of [[eq:pb-identity]] is at least ∫_I W_1|u|², and the
right side is at most ‖f‖(2X + (M′ + 2|σ|)Y) ≤ (2X(B̃) + (M′ + 2|σ|)B̃)‖f‖². ∎

For a multiplier φ = F(y) and a Lagrangian term q = ηg(y), [[eq:pb-tortoise]] gives φ′ = −2ηF_y,
−½φ‴ = 4η(η(ηF_y)_y)_y, −φV′ = 2ηFV_y and, with h := (3/2 − 5y/2)g + y(1 − y)g_y, q′ = −2(1 − y)y²h and
q″ = 4ηy((2 − 3y)h + y(1 − y)h_y). So W = ηG with

    G = 2FV_y + 4(η(ηF_y)_y)_y + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV.                              {#eq:pb-weight-general}

Every φ and q below is a rational function of y (with g a polynomial), so φ′, φ″, φ‴, q, q′, q″ are η or (1 − y)y²
times bounded functions; they are O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

### The weight of the multiplier 1 − 2/r² {#sec:morawetz-algebraic-weight}

**Proposition {#prop:morawetz-weight}** (The Morawetz weight of φ = 1 − 2/r².) Let φ := z = 1 − 2/r². Then φ is
increasing, φ → ±1 at ±∞, φ′ = 4η, and for q = 0 and V = V_(a,b) the weight of [[lem:morawetz-identity]] is
W = ηP_(a,b)(z) with

    P_(a,b)(z) := 2 + (b/2 − 6)z + (2a + b − 6)z² + (10 − 3b/2)z³.                                     {#eq:pb-weight}

P_(a,b) is affine in b and nondecreasing in a, with ∂_aP_(a,b) = 2z², and ψ := −φU′ = 2ηz² ≥ 0. For the scalar wave at
harmonic l (a = κ + 3/4, b = 9/4) the weight is w_l := ηP_l with

    P_l(z) = P_0(z) + c_l z²,     P_0(z) := 2 − (39/8)z + (53/8)z³,     c_l := 2κ − 9/4,          {#eq:pb-weight-scalar}

so that w_l = w_1 + (κ − 3)ψ. In the variable y, P_1 = ½p with

    p(y) := 15 − 90y + 189y² − 106y³ = 15(1 − y)(1 − 3y)² + y(29y² − 36y + 15).                   {#eq:pb-p-certificate}

Hence w_l ≥ w_1 > 0 on ℝ for every l ≥ 1, and φ satisfies the hypotheses of [[lem:morawetz-identity]] with q = 0
for every V_(κ+3/4,9/4), l ≥ 1.

*Proof.* With F = 1 − 2y, F_y = −2 and ηF_y = −2η, so 4(η(ηF_y)_y)_y = −8(η_y² + ηη_yy). From η_y = (y^(1/2)/2)(3 − 5y)
and η_yy = (3/4)y^(−1/2)(1 − 5y), η_y² + ηη_yy = (y/4)((3 − 5y)² + 3(1 − y)(1 − 5y)) = y(10y² − 12y + 3). So by
[[eq:pb-weight-general]], G = 2zV_y − 8y(10y² − 12y + 3). For V = V_(a,b), V_y = a(1 − 2y) + by(2 − 3y), and with
y = (1 − z)/2 one has y(2 − 3y) = (1 − z)(1 + 3z)/4 and 10y² − 12y + 3 = −½ + z + (5/2)z². Hence
2zV_y = 2az² + (b/2)(z + 2z² − 3z³) and −8y(10y² − 12y + 3) = −4(1 − z)(−½ + z + (5/2)z²) = 2 − 6z − 6z² + 10z³; the sum
is [[eq:pb-weight]]. U = V_(1,0) gives U_y = z, U′ = −2ηz and −φU′ = 2ηz². At a = κ + 3/4, b = 9/4 the coefficients
are 2, −39/8, 2κ − 9/4 and 53/8, which is [[eq:pb-weight-scalar]]; and c_l − c_1 = 2(κ − 3) gives w_l − w_1 = (κ − 3)ψ.
Substituting z = 1 − 2y in P_1 gives ½p, and expanding the right side of [[eq:pb-p-certificate]] gives p. Its first term
is nonnegative on [0, 1] and its second is positive on (0, 1], since 29y² − 36y + 15 has discriminant 1296 − 1740 < 0;
at y = 0, p = 15. So p > 0 on [0, 1], w_1 > 0 on ℝ, and w_l ≥ w_1 because κ ≥ 3 and ψ ≥ 0. φ is increasing as φ′ = 4η
> 0, and |φ| < 1. ∎

**Lemma {#lem:morawetz-weight-interval}** (The weight on I.) Let l ≥ 1 and c := c_l. On I:

(i) for 6/5 ≤ r ≤ √2, w_l ≥ 2^(−3/2) = √2/4;

(ii) for √2 ≤ r ≤ 8/5, with λ := 1677/2048 and d := λc − 9/16, w_l ≥ 2^(−5/2)(2 − (47/8)z + dz²); hence w_l is at least
2^(−5/2)(2 − 2209/(256d)) when d ≥ 94/7, and at least 2^(−5/2)(2 − 329/256 + 49d/1024) otherwise;

(iii) for 2 ≤ r ≤ 3, w_l ≥ 25/1944 + (392/19683)c; for 17/10 ≤ r ≤ 2, w_l ≥ 0.03658 + 0.012624c; and for
8/5 ≤ r ≤ 17/10, w_l ≥ 0.09213 + 0.0071190c;

(iv) for 3 ≤ r ≤ 4, w_l ≥ w_l(4) = (15/1024)(8899/4096 + (49/64)c).

Consequently min_I w_l ≥ ω_l, where ω_1 := 0.07388, ω_2 := 0.1860, ω_3 := 0.2847, ω_4 := 0.3122, ω_5 := 0.3257,
ω_l := 0.3335 for 6 ≤ l ≤ 19 and ω_l := 0.3514 for l ≥ 20.

*Proof.* Write A := ηP_0 and K := ηz², so that w_l = A + cK by [[eq:pb-weight-scalar]], with c ≥ 15/4. P_0′(z) =
−39/8 + (159/8)z² vanishes on [0, 1] only at z_0 := (39/159)^(1/2) < 0.4953, and P_0(z_0) = 2 − (13/4)z_0 > 0.3902;
P_0 decreases on [0, z_0] and increases on [z_0, 1]. In the variable z, η = (1 + z)(1 − z)^(3/2)2^(−5/2) decreases on
[0, 7/8] (that is y ∈ [1/16, 1/2] ⊂ [0, 3/5]), and K is unimodal on [0, 1], since
d log K/dz = 1/(1 + z) − 3/(2(1 − z)) + 2/z is decreasing.

(i) Here z ∈ [−7/18, 0], so −(39/8)z = (39/8)|z|, cz² ≥ 0 and (53/8)z³ ≥ −(53/8)(49/324)|z| > −1.002|z|; thus P_l ≥ 2.
Also y ∈ [1/2, 25/36], where η ≥ min(η(1/2), η(25/36)) = 2^(−5/2). So w_l ≥ 2^(−3/2).

(ii) Here z ∈ [0, 7/32]. First, P_l ≥ Q_c := 2 − (39/8)z + cz², as (53/8)z³ ≥ 0, and Q_c > 0 because its
discriminant (39/8)² − 8c is negative for c ≥ 15/4. Second, (1 − z)^(1/2) ≥ (1 − z)(1 + z/2) on [0, 1]: with
t := (1 − z)^(1/2) ∈ [0, 1] this is 2 ≥ t(3 − t²), that is (t − 1)²(t + 2) ≥ 0. Hence
η ≥ 2^(−5/2)(1 + z)(1 − z)²(1 + z/2) ≥ 2^(−5/2)(1 − z/2 − 3z²/2) ≥ 0, the middle step dropping (z³ + z⁴)/2 ≥ 0.
Multiplying,

    w_l ≥ 2^(−5/2)(1 − z/2 − 3z²/2)Q_c = 2^(−5/2)(2 − (47/8)z + (c − 9/16)z² + (117/16)z³ − c(z/2 + 3z²/2)z²),

and z/2 + 3z²/2 ≤ 7/64 + 147/2048 = 1 − λ on [0, 7/32]. Dropping (117/16)z³ ≥ 0 gives the bound. Its minimum over
z ∈ [0, 7/32] is at z = 47/(16d) when that lies in [0, 7/32], that is d ≥ 94/7, and at z = 7/32 otherwise.

(iii) On 2 ≤ r ≤ 3, y ∈ [1/9, 1/4] and z ∈ [1/2, 7/9] ⊂ [z_0, 1]: η ≥ η(1/9) = 8/243 and P_0 ≥ P_0(1/2) = 25/64, so
A ≥ 25/1944; and K ≥ min(K at r = 3, K at r = 2) = min(392/19683, 3/128). On 17/10 ≤ r ≤ 2, y ∈ [1/4, 100/289]:
η ≥ η(1/4) = 3/32 and P_0 ≥ P_0(z_0) > 0.3902, so A ≥ 0.03658; K ≥ K(17/10) = (189000/1419857)(89/289)² > 0.012624, as
K(2) = 3/128 is larger. On 8/5 ≤ r ≤ 17/10, z ∈ [7/32, 89/289] ⊂ [0, z_0]: η ≥ η(17/10) = 189000/1419857 and
P_0 ≥ P_0(89/289) = 66831535/96550276, so A > 0.09213; K ≥ K(8/5) = (4875/32768)(49/1024) = 238875/33554432.

(iv) We show that A and K increase with y on [1/16, 1/9], so that w_l, an increasing combination, does too. There
z ∈ [7/9, 7/8] ⊂ [z_0, 1], so P_0 decreases with y, and |dP_0/dy| = 2P_0′(z) = (159/4)z² − 39/4. Now
d log K/dy = 3/(2y) − 1/(1 − y) − 4/(1 − 2y) ≥ 27/2 − 9/8 − 36/7 > 0, and
d log A/dy = 3/(2y) − 1/(1 − y) + (dP_0/dy)/P_0.
On y ∈ [1/16, 1/12] the last expression is at least 18 − 12/11 − (5295/256)/(3061/1728) > 5.2, using P_0(5/6) = 3061/1728
and (159/4)(7/8)² − 39/4 = 5295/256; on [1/12, 1/10] it is at least 15 − 10/9 − (857/48)/(373/250) > 1.9, using
P_0(4/5) = 373/250; on [1/10, 1/9] it is at least 27/2 − 9/8 − 15.69/P_0(7/9) > 0.53, using P_0(7/9) > 1.3254. Finally
η(1/16) = 15/1024, P_0(7/8) = 8899/4096 and (7/8)² = 49/64.

Evaluating (i)–(iv): at l = 1 and l = 2, (iv) gives 309885/4194304 > 0.07388 and 780285/4194304 > 0.1860, (ii) more
than 0.147 and 0.216, the three bounds of (iii) more than 0.0839 and 0.190, and (i) more than 0.3535. For
l = 3, 4, 5, 6 and 20, d ≥ 94/7, and the vertex value in (ii) exceeds 0.2847, 0.3122, 0.3257, 0.3335 and 0.3514; the
bounds of (iii) are at least 0.2896, 0.4178, 0.5744, 0.7595 and 6.33, and those of (iv) at least 0.3430, 0.5449, 0.7916,
1.083 and 9.87. As w_l is nondecreasing in l ([[prop:morawetz-weight]]), the bounds at l = 6 and l = 20 hold for every
larger l. ∎

**Proposition {#prop:morawetz-resolvent-l-ge-1}** (Morawetz bounds for every harmonic l ≥ 1.) For every l ≥ 1 and every
real σ ≠ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ B_l(σ) := ((512/15 + (M′ + 2|σ|)²/ω_l)/ω_l)^(1/2),     M′ := 0.74362,

with ω_l of [[lem:morawetz-weight-interval]]. At σ → 0, 1, 3 and 10 these are at most:

| l | B_l(0+) | B_l(1) | B_l(3) | B_l(10) |
|---|---|---|---|---|
| 1 | 23.74 | 42.91 | 93.78 | 281.60 |
| 2 | 14.13 | 20.03 | 38.71 | 112.35 |
| 3 | 11.26 | 14.59 | 26.10 | 73.68 |
| 4 | 10.73 | 13.66 | 24.00 | 67.27 |
| 5 | 10.49 | 13.26 | 23.10 | 64.51 |
| every l ≥ 6 | 10.36 | 13.04 | 22.62 | 63.02 |
| every l ≥ 20 | 10.09 | 12.58 | 21.58 | 59.85 |

Each B_l is even in σ, increasing in |σ| and bounded as σ → 0.

*Proof.* [[prop:morawetz-weight]] gives the hypotheses of [[lem:morawetz-identity]] with φ = z, q = 0. On I, φ′ = 4η
has least value 4 min(η(1/16), η(25/36)) = 15/256, so 2/m′ = 512/15, and greatest value 4η(3/5) = 24√15/125 < 0.74362,
since 3.873² > 15. So w_I ≥ ω_l by [[lem:morawetz-weight-interval]], and [[eq:pb-bound]] gives the bound; it decreases in
w_I and increases in M′. The table evaluates the formula, rounding up. ∎

### The harmonic l = 0 {#sec:morawetz-l-zero}

**Proposition {#prop:morawetz-l-zero}** (The harmonic l = 0.) Let φ := 1 − 2/r² and q := ½η(1 + 3y/2). Then
0 ≤ q ≤ (5/16)φ′, and for V = V_0 at l = 0 (a = 3/4, b = 9/4) the weight of [[lem:morawetz-identity]] is

    W = (3/8)ηQ_4,     Q_4(y) := 149y⁴ − 280y³ + 177y² − 42y + 4
                               = (2 − (21/2)y + 11y²)² + y²(28(y − 7/8)² + 21/16) > 0.          {#eq:pb-lzero-weight}

On I, m′ = min_I(φ′ − q) = 3315/65536, M′ = max_I|φ′ − 2q| < 0.3999 and w_I = W(4) = 5899185/536870912 > 0.010988. So
for every real σ ≠ 0, ‖χ_I R_0(σ) χ_I‖ ≤ B_0(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2), which is at most 70.17,
226.50, 585.53 and 1857.54 at σ → 0, σ = 1, 3 and 10. In the form of [[ch:resolvent-bounds]] off the real axis,
max q = 2√6/27 < 0.18145, attained at y = 2/3.

*Proof.* q = ηg with g = (2 + 3y)/4 ≥ 0, and φ′ = 4η, so q/φ′ = (2 + 3y)/16 ≤ 5/16. In [[eq:pb-weight-general]],
h = (6 + 5y − 21y²)/8 and (2 − 3y)h + y(1 − y)h_y = (12 − 3y − 104y² + 105y³)/8, so the q″-term is
½y(12 − 3y − 104y² + 105y³). By [[prop:morawetz-weight]] the φ-terms give P_(3/4,9/4) = 3/2 − 21y + (141/2)y² − 53y³ in
the variable y, and −2gV_0 = −(3/8)y(1 − y)(2 + 3y)(1 + 3y) = −(3/4)y − (21/8)y² + (27/8)y⁴. The sum is (3/8)Q_4, and
the second form of Q_4 is checked by expansion. In it, 28y² − 49y + 22.75 = 28(y − 7/8)² + 21/16 > 0, and the two terms
do not vanish together, since the second vanishes only at y = 0, where the first is 4.

The constants. φ′ − q = η(14 − 3y)/4. On [1/16, 1/4], d log(η(14 − 3y))/dy = 3/(2y) − 1/(1 − y) − 3/(14 − 3y) ≥
6 − 4/3 − 3/13 > 0, so the least value there is at y = 1/16: (15/1024)(221/64) = 3315/65536; on [1/4, 25/36],
φ′ − q ≥ (3/32)(14 − 25/12)/4 > 0.27. Next φ′ − 2q = (3/2)η(2 − y) ≥ 0, whose derivative in y is
(3/2)y^(1/2)(3 − (15/2)y + (7/2)y²); its only zero in (0, 1) is y_* = (15 − √57)/14 ∈ (0.5321, 0.5322), and
(3/2)η(y_*)(2 − y_*) < 0.3999.

For w_I, Q_4 has the Taylor expansion at 1/5, with s := y − 1/5,

    Q_4 = 424/625 − (4/125)s + s²(149s² − (804/5)s + 1119/25),

and the last bracket is positive, its discriminant (804/5)² − 4 · 149 · 1119/25 being negative. So Q_4 ≥ 0.6784 −
0.032s, which is at least 0.6768 on [3/20, 1/4] and 0.6625 on [1/4, 25/36]. Also Q_4″ = 1788y² − 1680y + 354 > 0 on
[0, 1/5] (it decreases there to 89.52), so Q_4′ increases there to Q_4′(1/5) = −0.032, and Q_4 decreases on [0, 1/5].
Then:

- on [1/16, 5/64], d log W/dy = 3/(2y) − 1/(1 − y) + Q_4′/Q_4 ≥ 19.2 − 64/59 − |Q_4′(1/16)|/Q_4(5/64) ≥
  19.2 − 1.085 − 23.011/1.6711 > 0, and on [5/64, 3/32] it is at least 16 − 32/29 − 19.187/1.3989 > 0, so W ≥ W(4) on
  [1/16, 3/32];
- on [3/32, 7/64], [7/64, 1/8] and [1/8, 3/20], W ≥ (3/8)η(left end)Q_4(right end), that is at least
  (3/8)(0.026013)(1.1786), (3/8)(0.032216)(1.0051) and (3/8)(0.038669)(0.81293), all above 0.0114;
- on [3/20, 1/4], W ≥ (3/8)(0.049380)(0.6768) > 0.0125, and on [1/4, 25/36], W ≥ (3/8)(3/32)(0.6625) > 0.023.

Here Q_4(1/16) = 131093/65536, so W(4) = (3/8)(15/1024)(131093/65536). [[lem:morawetz-identity]] applies, and the bounds
follow from [[eq:pb-bound]]. For max q: d/dy(η(2 + 3y)) = y^(1/2)(3 + (5/2)y − (21/2)y²), which vanishes on (0, 1) only
at y = 2/3, where q = (1/3)(2/3)^(3/2) = 2√6/27. ∎

### One derivative {#sec:morawetz-one-derivative}

**Corollary {#cor:morawetz-one-derivative}** (The H¹ constants.) Let σ ≠ 0 be real, f ∈ L²(I), and u = R_l(σ)f, with
ψ = 2ηz² the weight of [[prop:morawetz-weight]], which vanishes on ℝ only at the photon sphere r = √2, to second order.

(a) For l ≥ 1, with m′ = 15/256, M′ = 0.74362 and B_l = B_l(σ) of [[prop:morawetz-resolvent-l-ge-1]],
‖u′‖_I ≤ X_l‖f‖ and (κ − 3)∫_I ψ|u|² ≤ K_l‖f‖², where X_l := (1 + (1 + 2m′(M′ + 2|σ|)B_l)^(1/2))/(2m′) and
K_l := 2X_l + (M′ + 2|σ|)B_l. With A_l := κK_l/(κ − 3) for l ≥ 2, A_1 := 3B_1² and C_l² := X_l² + A_l, at σ = 3:

| l | 1 | 2 | 3 | 4 | 5 | ≥ 6 |
|---|---|---|---|---|---|---|
| B_l(3) | 93.78 | 38.71 | 26.10 | 24.00 | 23.10 | 22.62 |
| X_l | 82.49 | 56.50 | 48.22 | 46.67 | 45.98 | 45.61 |
| A_l | 26,381.1 | 598.4 | 340.6 | 291.7 | 271.0 | 260.0 |
| C_l | 182.17 | 61.57 | 51.63 | 49.69 | 48.84 | 48.37 |

(b) For l = 0, with the constants of [[prop:morawetz-l-zero]], ‖u′‖_I ≤ X_0‖f‖ with
X_0 := (1 + (1 + 2m′(M′ + 2|σ|)B_0)^(1/2))/(2m′); X_0(3) < 202.6.

(c) Summed over the harmonics, which are orthogonal on 𝕊³: for every real 0 < |σ| ≤ 3,

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖f‖²,     C ≤ 182.17 over l ≥ 1 and C ≤ 202.6 over l ≥ 0,

the angular part at l = 1 taken unweighted. At |σ| = 1/2, 1, 2 and 3, C_1 is at most 63.86, 85.06, 132.46, 182.17 and
X_0 at most 55.13, 83.85, 142.96, 202.6.

(d) Without the weight: for every real 0 < |σ| ≤ 3, ‖∂_(r_*)u‖_I² + Σ_l κ‖u_l‖_I² ≤ C_u²‖f‖² with C_u < 1079.4.

*Proof.* (a) and (b) are [[lem:morawetz-identity]] with B̃ = B_l. In (a), W_1 := (κ − 3)ψ and W_0 := w_1 are
nonnegative ([[prop:morawetz-weight]]); so (κ − 3)∫_Iψ|u|² ≤ K_l‖f‖², and κ∫_Iψ|u|² ≤ A_l‖f‖² for l ≥ 2. At l = 1,
3‖u‖_I² ≤ 3B_1²‖f‖². For l ≥ 6, B_l ≤ B_6, X_l ≤ X_6, K_l ≤ K_6, and κ/(κ − 3) decreases, so C_l ≤ C_6. The table
evaluates the formulas at σ = 3, rounding up.

(c) Every quantity in (a) and (b) is an explicit function increasing in |σ|, so the values at |σ| = 3 bound the band.
The harmonics are orthogonal, so the sum is at most max_l C_l² (and X_0² at l = 0) times ‖f‖², and C_l ≤ C_1 for every
l ≥ 1 by the table. The values at |σ| = 1/2, 1, 2 evaluate the same formulas.

(d) The left side is at most max_l (X_l² + κB_l²)‖f‖², with any valid B_l. For l ≥ 50 we use the closed-form bound of
[[ch:resolvent-bounds]], ‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)(κ + 3/4) − σ²), valid when its three conditions hold. At
l = 50 (κ + 3/4 = 2600.75) and σ = 3 they read 152.38 > 9 and 373.0 > 9; 0.32727(313.45 − 9)^(1/2) > 5.71 >
(2 + 3.3744)/√2; and, with c := (15/16)(2600.75) > 2438.2, c^(1/2) > 49.37 > 24 and
(√3/2)(49.37)log(49.37/24) > 30.8 > 29.99 > (2 + 0.79217 · 51)/√2. Each condition becomes easier as l grows or |σ|
decreases, so the bound holds for l ≥ 50 and 0 < |σ| ≤ 3; there B_l ≤ 0.006975, X_l² + κB_l² < 17.1², and both terms
decrease in κ. For 1 ≤ l ≤ 49 we use B_l(3) of [[prop:morawetz-resolvent-l-ge-1]]: (X_l² + κB_l²)^(1/2) is at most
182.2, 123.2, 112.0, 126.5, 144.2 for l = 1, …, 5, at most 454.0 for 6 ≤ l ≤ 19 (using ω_6 and κ ≤ 399) and at most
1079.4 for 20 ≤ l ≤ 49 (using ω_20 and κ ≤ 2499). At l = 0 the term is X_0² < 202.6². ∎

### The master operators {#sec:morawetz-master}

**Lemma {#lem:bernstein-lower-bound}** (Bernstein lower bound.) Let p be a polynomial of degree at most n and α < β.
Write p(α + (β − α)t) = Σ_(j≤n) c_j t^j and b_k := Σ_(j≤k) (C(k, j)/C(n, j))c_j for 0 ≤ k ≤ n. Then
min_([α,β]) p ≥ min_k b_k.

*Proof.* Expanding t^j = t^j(t + (1 − t))^(n−j) by the binomial theorem gives
t^j = Σ_(k≥j) (C(k, j)/C(n, j))C(n, k)t^k(1 − t)^(n−k), as C(n − j, k − j)/C(n, k) = C(k, j)/C(n, j). So
p(α + (β − α)t) = Σ_k b_k C(n, k)t^k(1 − t)^(n−k), a combination of the b_k with nonnegative weights of sum 1 on
t ∈ [0, 1]. ∎

In the proposition below a weight is W = ηN/D with N a polynomial and D a product of powers of positive increasing linear
functions of y. A lower bound on a piece r ∈ [r_2, r_1] (y ∈ [1/r_1², 1/r_2²]) is the product of η at the end where it is
least and of the least Bernstein coefficient of N on the piece divided by the value of D at its right end in y. Each
piece below is written "r_1–r_2: e · g ≥ v" with e and g such lower bounds. Positivity on (0, 1) is shown by the
Bernstein coefficients of N on the listed subintervals of [0, 1], whose least values are given.

**Proposition {#prop:morawetz-master-potentials}** (Every master operator at every harmonic.) Let m′, M′ and w_I be as
listed, and B(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2). For the operator −∂²_(r_*) + V − σ² of each of the following
rows, every real σ ≠ 0 and every harmonic of the row, ‖χ_I R(σ) χ_I‖ ≤ B(σ), with the values at σ → 0, σ = 1, 3, 10:

| row | operators and harmonics | multiplier | w_I ≥ | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|---|
| A | V_0, V_1, every l ≥ 1 | z | 0.064 | 25.86 | 48.70 | 107.88 | 324.95 |
| B | V_0, V_1, V_2, V_T, every l ≥ 2 | z | 0.1393 | 16.54 | 25.16 | 50.88 | 149.74 |
| C | V_V, every l ≥ 3 | z | 0.1413 | 16.41 | 24.88 | 50.20 | 147.63 |
| S4 | V_S, every l ≥ 4 | z | 0.1874 | 14.07 | 19.92 | 38.44 | 111.52 |
| S3 | V_S, l = 3 | z | 0.106 | 19.27 | 31.50 | 66.11 | 196.52 |
| T1 | V_2, l = 1 | z, q = (5/3)ηy | 0.0455 | 29.22 | 59.91 | 143.71 | 449.56 |
| T2 | V_V, l = 2 | z, q = 2ηy² | 0.0687 | 23.62 | 43.09 | 97.67 | 299.71 |
| T3 | V_S, l = 2 | (1 − 4y)/(1 + 2y), q = ½ηy(1 + y) | 0.0413 | 23.15 | 64.82 | 160.01 | 498.25 |

with m′ = 15/256, M′ = 0.74362 in rows A–S3, and (m′, M′) = (2805/49152, 0.4157), (7665/131072, 0.5324) and
(0.1384, 0.563) in rows T1, T2, T3. The largest values over all rows are 29.22, 64.82, 160.01 and 498.25. Multiplied by
15/16, the transfer of [[ch:resolvent-bounds]], rows A and B bound the vector-type 1-form blocks at l = 1 (24.24, 45.66,
101.13, 304.64) and at l ≥ 2 (15.51, 23.59, 47.70, 140.38), and row B the tensor-type blocks, every l ≥ 2 (the same).

*Proof.* In each row we give G = N/D of [[eq:pb-weight-general]], its positivity on (0, 1), which with the conditions on
φ′ − q, q and |φ| gives the hypotheses of [[lem:morawetz-identity]], and the lower bound for w_I. Then [[eq:pb-bound]]
gives the bound; the table evaluates it, rounding up.

Families. By [[prop:morawetz-weight]], for φ = z and q = 0 the weight of V_(a,b) is ηP_(a,b), affine in b and
nondecreasing in a; so for a ≥ a_0 and b_− ≤ b ≤ b_+ it is at least the smaller of the weights at (a_0, b_−) and
(a_0, b_+), on ℝ and on I. Row A is the family a ≥ 15/4, 5/4 ≤ b ≤ 9/4; row B the family a ≥ 35/4, −7/4 ≤ b ≤ 9/4; row C
the family a ≥ 63/4, b = −27/4. The corners (15/4, 9/4) and (35/4, 9/4) are the scalar wave at l = 1 and l = 2, with
w_I ≥ 0.07388 and 0.1860 by [[lem:morawetz-weight-interval]]. For the others, in the variable y, G = N with:

- (15/4, 5/4): N = 15/2 − 49y + (217/2)y² − 65y³; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 1]: at least 1.01, 0.437, 2.
  Pieces: 4–37/10: 0.01464 · 4.474 ≥ 0.0654; 37/10–31/10: 0.0183 · 3.502 ≥ 0.064; 31/10–5/2: 0.03007 · 2.171 ≥ 0.0652;
  5/2–21/10: 0.05376 · 1.209 ≥ 0.0649; 21/10–9/5: 0.08349 · 0.8011 ≥ 0.0668; 9/5–6/5: 0.1185 · 0.7239 ≥ 0.0857.
- (35/4, −7/4): N = 35/2 − 101y + (381/2)y² − 101y³; Bernstein: at least 2.57, 0.52, 2 on the same subintervals.
  Pieces: 4–33/10: 0.01464 · 9.753 ≥ 0.1427; 33/10–5/2: 0.02527 · 5.803 ≥ 0.1466; 5/2–21/10: 0.05376 · 3.215 ≥ 0.1728;
  21/10–19/10: 0.08349 · 1.993 ≥ 0.1663; 19/10–9/5: 0.1054 · 1.504 ≥ 0.1585; 9/5–17/10: 0.1185 · 1.176 ≥ 0.1393;
  17/10–8/5: 0.1331 · 1.071 ≥ 0.1425; 8/5–6/5: 0.1487 · 1.094 ≥ 0.1626.
- (63/4, −27/4): N = 63/2 − 177y + (633/2)y² − 161y³; Bernstein: at least 4.51, 0.437, 2. Pieces: 4–49/20:
  0.01464 · 10.05 ≥ 0.1471; 49/20–37/20: 0.05667 · 2.787 ≥ 0.1579; 37/20–17/10: 0.1117 · 1.478 ≥ 0.165; 17/10–33/20:
  0.1331 · 1.208 ≥ 0.1607; 33/20–31/20: 0.1408 · 1.004 ≥ 0.1413; 31/20–6/5: 0.1567 · 1.05 ≥ 0.1645.

Row S4. Here κ ≥ 24, p = κ − 3 = 21 + t with t ≥ 0, a = κ + 3/4 and H = H_0 + t, H_0 := 21 + 6y. With
G = 2zV_(S,y) − 8y(10y² − 12y + 3), expanding gives 16H³G = Σ_(j≤4) c_j(y)t^j with

    c_0 = −216(848y⁶ + 7008y⁵ + 16392y⁴ + 18376y³ − 205275y² + 159348y − 33957),
    c_1 = −72(1144y⁵ + 5868y⁴ + 10226y³ − 103203y² + 84042y − 18669),
    c_2 = −24(508y⁴ + 1828y³ − 19269y² + 16608y − 3843),
    c_3 = −8(106y³ − 1581y² + 1458y − 351),     c_4 = 32(2y − 1)².

The Bernstein coefficients of c_0 on [0, 1/2], [1/2, 1] are at least 53568 and 442368; those of c_1, c_2, c_3 on
[0, 1/4], [1/4, 1/2], [1/2, 1] at least 282590, 25776, 55296; 20754, 750, 2304; and 669, 3, 32. So c_0, …, c_3 > 0 and
c_4 ≥ 0 on [0, 1], and G > 0 on (0, 1) for every l ≥ 4. Moreover (H_0 + t)³ = Σ_(j≤3) C(3, j)H_0^(3−j)t^j, so
G ≥ λ(y) := min_(j≤3) c_j/(16C(3, j)H_0^(3−j)) for every t ≥ 0, uniformly in l. On pieces, with λ bounded below by
the least Bernstein coefficients of the c_j and the largest H_0: 4–23/10: 0.014648 · 13.722 ≥ 0.2009; 23/10–9/5:
0.066652 · 4.0959 ≥ 0.2729; 9/5–8/5: 0.11854 · 1.5817 ≥ 0.1874; 8/5–3/2: 0.14877 · 1.2656 ≥ 0.1882; 3/2–7/5:
0.1646 · 1.2626 ≥ 0.2078; 7/5–6/5: 0.17682 · 1.9338 ≥ 0.3419.

Row S3. At l = 3, p = 12 and H = 6(2 + y): N = 504 − 2652y + 3786y² − 161y³ − 420y⁴ − 447y⁵ − 106y⁶, D = 2(2 + y)³;
Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 1]: at least 73, 12.1, 62.5. Pieces: 4–12/5: 0.01464 · 7.614 ≥ 0.1114;
12/5–37/20: 0.05977 · 1.837 ≥ 0.1097; 37/20–17/10: 0.1117 · 0.9511 ≥ 0.1062; 17/10–33/20: 0.1331 · 0.8221 ≥ 0.1094;
33/20–31/20: 0.1408 · 0.7532 ≥ 0.106; 31/20–5/4: 0.1567 · 0.6989 ≥ 0.1095; 5/4–6/5: 0.1768 · 4.844 ≥ 0.8564.

Row T1 (a = 15/4, b = −7/4; here a + b < 4, and q is needed at the horizon). g = (5/3)y gives
N = 15/2 − 61y + 188y² − (728/3)y³ + (665/6)y⁴; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 1]: at least 0.641,
0.292, 0.193, 0.101. Pieces: 4–16/5: 0.01464 · 3.119 ≥ 0.0456; 16/5–13/5: 0.02753 · 1.857 ≥ 0.0511; 13/5–11/5:
0.04847 · 0.9837 ≥ 0.0476; 11/5–2: 0.07451 · 0.6412 ≥ 0.0477; 2–19/10: 0.09375 · 0.5229 ≥ 0.049; 19/10–17/10:
0.1054 · 0.432 ≥ 0.0455; 17/10–13/10: 0.1331 · 0.4373 ≥ 0.0582; 13/10–6/5: 0.1768 · 0.3101 ≥ 0.0548. Also
φ′ − q = η(12 − 5y)/3 > 0; d log(η(12 − 5y))/dy ≥ 3 − 2 − 5/9.5 > 0 on [1/16, 1/2] and η(12 − 5y)/3 > 0.5 on
[1/2, 25/36], so m′ = (15/1024)(187/48) = 2805/49152; φ′ − 2q = (2/3)η(6 − 5y) has its maximum on (0, 1) at the root
y = (55 − √505)/70 of 35y² − 55y + 18, where it is less than 0.4157.

Row T2 (a = 35/4, b = −27/4). g = 2y² gives N = 35/2 − 121y + (521/2)y² − 84y³ − 258y⁴ + 189y⁵; Bernstein on the same
four subintervals: at least 1.39, 0.316, 1.06, 0.0906. Pieces: 4–13/5: 0.01464 · 4.919 ≥ 0.072; 13/5–21/10:
0.04847 · 1.908 ≥ 0.0924; 21/10–19/10: 0.08349 · 0.9747 ≥ 0.0813; 19/10–9/5: 0.1054 · 0.6879 ≥ 0.0725; 9/5–17/10:
0.1185 · 0.5801 ≥ 0.0687; 17/10–6/5: 0.1331 · 0.5729 ≥ 0.0762. Also φ′ − q = 2η(2 − y²) > 0, increasing in y on
[1/16, 1/2] (log-derivative at least 3 − 2 − 2/3.5) and above 0.5 on [1/2, 25/36], so m′ = (15/1024)(511/128) =
7665/131072; φ′ − 2q = 4η(1 − y²) has its maximum on (0, 1) at y = (2√7 − 1)/9, the root of 9y² + 2y − 3 there,
where it is less than 0.5324.

Row T3 (V_S at l = 2, p = 5, H = 5 + 6y). Here F = (1 − 4y)/(1 + 2y) decreases from 1 to −1 on [0, 1], so |φ| ≤ 1,
φ → ±1 at ±∞, and φ′ = 12η/(1 + 2y)² > 0. With g = ½y(1 + y), [[eq:pb-weight-general]] gives G = N/D with
D = 4(1 + 2y)⁴(5 + 6y)³ and

    N = 8750 − 52800y − 52305y² + 661453y³ + 1153253y⁴ − 668761y⁵ − 2258994y⁶ − 1768052y⁷ − 1623176y⁸
        + 831312y⁹ + 3571104y¹⁰ + 2896704y¹¹ + 777600y¹²;

Bernstein on [0, 1/2], [1/2, 3/4], [3/4, 1]: at least 228, 27800, 34900. Pieces: 4–33/10: 0.01464 · 3.014 ≥ 0.0441;
33/10–29/10: 0.02527 · 1.742 ≥ 0.044; 29/10–27/10: 0.03612 · 1.243 ≥ 0.0448; 27/10–13/5: 0.04383 · 1.048 ≥ 0.0459;
13/5–5/2: 0.04847 · 0.9003 ≥ 0.0436; 5/2–12/5: 0.05376 · 0.793 ≥ 0.0426; 12/5–23/10: 0.05977 · 0.7024 ≥ 0.0419;
23/10–11/5: 0.06665 · 0.6601 ≥ 0.0439; 11/5–2: 0.07451 · 0.5544 ≥ 0.0413; 2–17/10: 0.09375 · 0.4985 ≥ 0.0467;
17/10–13/10: 0.1331 · 0.3475 ≥ 0.0462; 13/10–6/5: 0.1768 · 0.3621 ≥ 0.064. Also
φ′ − q = η(24 − y − 5y² − 8y³ − 4y⁴)/(2(1 + 2y)²) > 0; its logarithmic derivative is positive on [1/16, 1/4] (at least
6 − 4/3 − 0.23 − 3.56) and it exceeds 0.14 on [1/4, 25/36], so m′ is its value at y = 1/16, more than 0.1384. And
0 < φ′ − 2q = η(12 − y − 5y² − 8y³ − 4y⁴)/(1 + 2y)² ≤ 12η/(1 + 2y)², whose maximum on (0, 1) is at the root
y = (√73 − 7)/4 of 2y² + 7y − 3, where it is less than 0.563.

In every row q ≥ 0, and φ′ − q > 0 on ℝ. ∎

### Large frequencies with a fixed multiplier {#sec:morawetz-large-frequency}

**Proposition {#prop:morawetz-large-frequency}** (Every harmonic at a given frequency.) Let B_l be as in
[[prop:morawetz-resolvent-l-ge-1]]. For every real σ with |σ| ≥ 3 and every l ≥ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 6.521), B_5(σ)),

and for |σ| ≥ 6 also ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 9.271), B_6(σ)). In particular, for every l ≥ 0, the norm is at
most 23.10, 39.53, 74.89, 146.51, 290.27 and 578.04 at σ = 3, 6, 12, 24, 48 and 96.

*Proof.* max V_(a,b) ≤ a max U + b max Q = a/4 + 4b/27 for a, b ≥ 0, since U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27.
With b = 9/4 this is a/4 + 1/3: at most 6.521 for l ≤ 4 and 9.271 for l ≤ 5. When σ² exceeds max V_l, the bound above
the barrier of [[ch:resolvent-bounds]] gives ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_l). So for |σ| ≥ 3 the harmonics
l ≤ 4 are bounded by Λ|σ|/(σ² − 6.521), and for |σ| ≥ 6 the harmonics l ≤ 5 by Λ|σ|/(σ² − 9.271); the others are
bounded by B_5(σ), respectively B_6(σ), as ω_l ≥ ω_5 for l ≥ 5 and ω_l ≥ ω_6 for l ≥ 6. At σ = 3 the first term is
at most 3.7436 · 3/2.479 < 4.54 and B_5(3) < 23.10; for σ ≥ 6 the first term is at most 3.7436 · 6/26.729 < 0.85, as
Λσ/(σ² − c) decreases for σ² > c, and the values given are B_6(σ), rounded up. ∎
