This part makes the multiplier bounds of [[ch:resolvent-bounds]] explicit on five-dimensional
Schwarzschild–Tangherlini with mass parameter m₀ = 1, so that f = 1 − 1/r² and the horizon is r = 1. Every multiplier
is a polynomial or a rational function of r⁻², every weight is (1 − r⁻²)r⁻³ times a rational function of r⁻², and every
constant is obtained from exact rational inequalities. The coefficient lists that the Bernstein bounds below use are in
[[sec:tb-morawetz]].

### The multiplier identity {#sec:morawetz-identity}

Throughout, y := 1/r² ∈ (0, 1), z := 1 − 2y ∈ (−1, 1) and η(y) := (1 − y)y^(3/2) = (r² − 1)/r⁵. The tortoise coordinate
r_* has dr_*/dr = 1/f, and g′ := dg/dr_*. Since dy/dr = −2y^(3/2),

    d/dr_* = −2η(y) d/dy.                                                                            {#eq:pb-tortoise}

As r_* → −∞, y → 1 and 1 − y decays like e^(2r_*); as r_* → ∞, r_* = r + O(r⁻¹). The interval I := {6/5 ≤ r ≤ 4} is
{1/16 ≤ y ≤ 25/36} = {−7/18 ≤ z ≤ 7/8}. With r_* = r + ½ log((r − 1)/(r + 1)), its length is
Λ := 14/5 + ½ log(33/5) < 3.7436. We write ‖·‖ for the norm of L²(ℝ, dr_*), ‖·‖_I for that of L²(I, dr_*), and χ_I
for multiplication by the indicator function of I. For a potential V as below, a real σ ≠ 0 and f ∈ L²(ℝ) vanishing
outside I, R(σ)f is the outgoing solution of −u″ + (V − σ²)u = f ([[pending:resolvent-outgoing]]), whose form is
recalled in [[lem:morawetz-identity]]; R_l(σ) is R(σ) for the potential of the harmonic l, and ‖χ_I R(σ) χ_I‖ is the
norm of f ↦ χ_I R(σ)f on L²(I).

Since η_y = y^(1/2)(3/2 − 5y/2), η increases on [0, 3/5] and decreases on [3/5, 1]; so on an interval of y its least
value is attained at an end. We use η(1/16) = 15/1024, η(1/2) = 2^(−5/2), η(25/36) = 1375/7776 > 2^(−5/2) (as
32 · 1375² > 7776²) and max η = η(3/5) = 6√15/125 < 0.18591. At a rational r, η = (r² − 1)/r⁵ is rational.

The potentials. Put U := f/r² = (1 − y)y, Q := f/r⁴ = (1 − y)y² and V_(a,b) := aU + bQ = (1 − y)(ay + by²). With
κ := l(l + 2), the potentials V_0, V_1, V_2 of [[prop:np-10-16]] at m₀ = 1 are V_(κ+3/4,b) with b = 9/4, 5/4 and −7/4
(V_0 is the scalar wave, V_1 the vector-type and V_2 the scalar-type 1-forms); those of [[thm:s15-ki]] are V_T = V_0 and
V_V = V_(κ+3/4,−27/4), and V_S = (1 − y)yQ_S/(16H²), with Q_S the polynomial [[eq:s15-ki-q]] at ς = y, p := κ − 3 and
H := p + 6y, for l ≥ 2. Each of them is (1 − y)y times a rational function of y bounded on [0, 1] (for V_S, H ≥ p > 0),
so V and V′ = −2ηV_y are O(r⁻²) and O(r⁻³) as r_* → ∞ and O(e^(2r_*)) as r_* → −∞: they are integrable and tend to 0
at ±∞.

**Lemma {#lem:morawetz-identity}** (The multiplier identity.) Let V be a real smooth function on ℝ with V, V′ integrable
and V, V′ → 0 at ±∞. Let φ and q be real smooth functions on ℝ, φ bounded with limits φ(±∞) at ±∞, and φ′, φ″, φ‴, q,
q′, q″ integrable and tending to 0 at ±∞. Let σ ≠ 0 be real, f ∈ L²(ℝ) vanish outside I, and let u be a solution, with
u and u′ locally absolutely continuous, of −u″ + (V − σ²)u = f (almost everywhere), such that u − c_±e^(±iσr_*) → 0 and
u′ ∓ iσu → 0 as r_* → ±∞. Then, with integrals over ℝ,

    2∫(φ′ − q)|u′|² + ∫W|u|² + 2σ²∫q|u|² = Re∫f(2φū′ + (φ′ − 2q)ū) + 2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²),
    W := −φV′ − ½φ‴ + q″ − 2qV,                                                                      {#eq:pb-identity}

and σ(|c_+|² + |c_−|²) = −Im∫fū. The outgoing solution R(σ)f is a solution of this kind.

Suppose moreover that φ′ − q ≥ 0, q ≥ 0 and W ≥ 0 on ℝ, and let m′ > 0, M′, w_I > 0, p_I and p_∞ satisfy
m′ ≤ φ′ − q, |φ′ − 2q| ≤ M′, w_I ≤ W and |φ| ≤ p_I on I, and p_∞ ≥ max(φ(∞), −φ(−∞), 0). Then X := ‖u′‖_I and
Y := ‖u‖_I satisfy

    Y ≤ B‖f‖,     B := ((2p_I²/m′ + (M′ + 2p_∞|σ|)²/w_I)/w_I)^(1/2);                               {#eq:pb-bound}

for every B̃ with Y ≤ B̃‖f‖, X ≤ X(B̃)‖f‖ with X(B̃) := (p_I + (p_I² + 2m′(M′ + 2p_∞|σ|)B̃)^(1/2))/(2m′); and for every
decomposition W = W_0 + W_1 with W_0, W_1 ≥ 0 on ℝ, ∫_I W_1|u|² ≤ (2p_IX(B̃) + (M′ + 2p_∞|σ|)B̃)‖f‖². When |φ| ≤ 1 on
ℝ one may take p_I = p_∞ = 1; then B = ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2) and
X(B̃) = (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′).

*Proof.* First, R(σ)f is a solution of this kind. Let u_h and u_∞ be the solutions of the homogeneous equation with
u_h − e^(−iσr_*) → 0 and u_h′ + iσu_h → 0 as r_* → −∞, and u_∞ − e^(iσr_*) → 0 and u_∞′ − iσu_∞ → 0 as r_* → ∞, and
let 𝒲 := u_hu_∞′ − u_h′u_∞ be their Wronskian, a nonzero constant ([[pending:resolvent-outgoing]]). Then

    R(σ)f(x) = −𝒲⁻¹(u_∞(x)∫_(−∞)^x u_hf + u_h(x)∫_x^∞ u_∞f).

As f ∈ L² vanishes outside the bounded interval I and u_h, u_∞ are continuous, u_hf and u_∞f are integrable, and both
integrals are absolutely continuous in x. Differentiating, the two terms ±𝒲⁻¹u_∞u_hf cancel, so
u′ = −𝒲⁻¹(u_∞′∫_(−∞)^x u_hf + u_h′∫_x^∞ u_∞f), which is again absolutely continuous; differentiating once more,
u″ = (V − σ²)u − 𝒲⁻¹(u_hu_∞′ − u_h′u_∞)f = (V − σ²)u − f almost everywhere. To the right of I, u is a multiple of u_∞,
and to its left a multiple of u_h, which gives the stated behaviour at ±∞.

Now let u be any solution as in the statement. Since u and u′ are locally absolutely continuous and φ, q, V are smooth,
all the products below are locally absolutely continuous and the product rule holds for them almost everywhere. With
Re(u″ū) = ½(|u|²)″ − |u′|² and Re(u′ū) = ½(|u|²)′, one checks term by term, almost everywhere:

    Re(−u″ · 2φū′) = −(φ|u′|²)′ + φ′|u′|²,
    Re(−u″ · φ′ū) = −(φ′Re(u′ū))′ + φ′|u′|² + (½φ″|u|²)′ − ½φ‴|u|²,
    Re((V − σ²)u · 2φū′) = ((V − σ²)φ|u|²)′ − (φV′ + (V − σ²)φ′)|u|²,
    Re((V − σ²)u · φ′ū) = (V − σ²)φ′|u|²,
    Re((−u″ + (V − σ²)u) · (−2qū)) = (q(|u|²)′ − q′|u|²)′ + q″|u|² − 2q|u′|² − 2qV|u|² + 2σ²q|u|².

Adding, Re(f(2φū′ + (φ′ − 2q)ū)) = 2(φ′ − q)|u′|² + W|u|² + 2σ²q|u|² + E′ almost everywhere, where the locally
absolutely continuous function E is −φ|u′|² − φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² + q(|u|²)′ − q′|u|². The function u
is continuous with limits of modulus |c_±| at ±∞, and u′ continuous with limits of modulus |σc_±|; so both are bounded,
and every integral in [[eq:pb-identity]] converges absolutely, as f vanishes outside I and φ′, φ‴, q, q″, V′ and qV are
integrable. Integrate over [−R, R] and let R → ∞: at ±∞, |u′|² → σ²|c_±|², |u|² → |c_±|², Re(u′ū) → 0, φ → φ(±∞) and
φ′, φ″, q, q′, V → 0, so E → −2σ²φ(±∞)|c_±|², and [[eq:pb-identity]] follows. Next, almost everywhere,
Im(fū) = −Im(u″ū) = −(Im(u′ū))′, and Im(u′ū) → ±σ|c_±|² at ±∞; integrating gives the flux identity.

Under the sign conditions every integrand on the left of [[eq:pb-identity]] is nonnegative. Dropping the term with q and
restricting the other two to I, the left side is at least 2m′X² + w_IY². On the right, f vanishes outside I and
|φ| ≤ p_I on I, so the integral is at most ‖f‖(2p_IX + M′Y); and
2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²) ≤ 2σ²p_∞(|c_+|² + |c_−|²) = −2σp_∞Im∫fū ≤ 2|σ|p_∞‖f‖Y. Hence, with
M := M′ + 2p_∞|σ|,

    2m′X² + w_IY² ≤ ‖f‖(2p_IX + MY).                                                                {#eq:pb-energy}

By the Cauchy–Schwarz inequality, 2p_IX + MY ≤ (2p_I²/m′ + M²/w_I)^(1/2)(2m′X² + w_IY²)^(1/2), so
(2m′X² + w_IY²)^(1/2) ≤ (2p_I²/m′ + M²/w_I)^(1/2)‖f‖ and w_I^(1/2)Y ≤ (2m′X² + w_IY²)^(1/2), which is [[eq:pb-bound]].
Dropping w_IY² in [[eq:pb-energy]] and using Y ≤ B̃‖f‖ gives 2m′X² − 2p_I‖f‖X − MB̃‖f‖² ≤ 0, so X is at most the
positive root, X(B̃)‖f‖. Finally the left side of [[eq:pb-identity]] is at least ∫_I W_1|u|², and the right side is at
most ‖f‖(2p_IX + MY) ≤ (2p_IX(B̃) + MB̃)‖f‖². When |φ| ≤ 1 on ℝ, also |φ(±∞)| ≤ 1, so p_I = p_∞ = 1 serve. ∎

For a multiplier φ = F(y) and a Lagrangian term q = ηg(y), [[eq:pb-tortoise]] gives φ′ = −2ηF_y,
−½φ‴ = 4η(η(ηF_y)_y)_y, −φV′ = 2ηFV_y and, with h := (3/2 − 5y/2)g + y(1 − y)g_y, q′ = −2(1 − y)y²h and
q″ = 4ηy((2 − 3y)h + y(1 − y)h_y). So W = ηG with

    G = 2FV_y + 4(η(ηF_y)_y)_y + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV.                              {#eq:pb-weight-general}

Every φ below is a polynomial or a rational function of y with no pole on [0, 1], and every q is η times a polynomial g.
Since ηη_y = (1 − y)y²(3 − 5y)/2 and η² = (1 − y)²y³ are polynomials, φ′, φ″, φ‴, q, q′, q″ are η or (1 − y)y² times
bounded functions; they are O(r⁻³) as r_* → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

### The weight of the multiplier 1 − 2/r² {#sec:morawetz-algebraic-weight}

**Proposition {#prop:morawetz-weight}** (The Morawetz weight of φ = 1 − 2/r².) Let φ := z = 1 − 2/r². Then φ is
increasing, φ → ±1 at ±∞, φ′ = 4η, and for q = 0 and V = V_(a,b) the weight of [[lem:morawetz-identity]] is
W = ηP_(a,b)(z) with

    P_(a,b)(z) := 2 + (b/2 − 6)z + (2a + b − 6)z² + (10 − 3b/2)z³.                                     {#eq:pb-weight}

P_(a,b) is affine in b and nondecreasing in a, with ∂_aP_(a,b) = 2z², and ψ := −φU′ = 2ηz² ≥ 0. For the scalar wave at
harmonic l (a = κ + 3/4, b = 9/4) the weight is w_l := ηP_l with

    P_l(z) = P̄(z) + c_l z²,     P̄(z) := 2 − (39/8)z + (53/8)z³,     c_l := 2κ − 9/4,             {#eq:pb-weight-scalar}

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

(ii) for √2 ≤ r ≤ 8/5, with ρ := 1677/2048 and d := ρc − 9/16, w_l ≥ 2^(−5/2)(2 − (47/8)z + dz²); hence w_l is at least
2^(−5/2)(2 − 2209/(256d)) when d ≥ 94/7, and at least 2^(−5/2)(2 − 329/256 + 49d/1024) otherwise;

(iii) for 2 ≤ r ≤ 3, w_l ≥ 25/1944 + (392/19683)c; for 17/10 ≤ r ≤ 2, w_l ≥ 0.03658 + 0.012624c; and for
8/5 ≤ r ≤ 17/10, w_l ≥ 0.09213 + 0.0071190c;

(iv) for 3 ≤ r ≤ 4, w_l ≥ w_l(4) = (15/1024)(8899/4096 + (49/64)c).

Consequently min_I w_l ≥ ω_l, where ω_1 := 0.07388, ω_2 := 0.1860, ω_3 := 0.2847, ω_4 := 0.3122, ω_5 := 0.3257,
ω_l := 0.3335 for 6 ≤ l ≤ 19 and ω_l := 0.3514 for l ≥ 20.

*Proof.* Write A := ηP̄ and Z := ηz², so that w_l = A + cZ by [[eq:pb-weight-scalar]], with c ≥ 15/4. P̄′(z) =
−39/8 + (159/8)z² vanishes on [0, 1] only at z_0 := (39/159)^(1/2) < 0.4953, and P̄(z_0) = 2 − (13/4)z_0 > 0.3902;
P̄ decreases on [0, z_0] and increases on [z_0, 1]. In the variable z, η = (1 + z)(1 − z)^(3/2)2^(−5/2) decreases on
[0, 7/8] (that is y ∈ [1/16, 1/2] ⊂ [0, 3/5]), and Z is unimodal on [0, 1], since
d log Z/dz = 1/(1 + z) − 3/(2(1 − z)) + 2/z is decreasing.

(i) Here z ∈ [−7/18, 0], so −(39/8)z = (39/8)|z|, cz² ≥ 0 and (53/8)z³ ≥ −(53/8)(49/324)|z| > −1.002|z|; thus P_l ≥ 2.
Also y ∈ [1/2, 25/36], where η ≥ min(η(1/2), η(25/36)) = 2^(−5/2). So w_l ≥ 2^(−3/2).

(ii) Here z ∈ [0, 7/32]. First, P_l ≥ Q_c := 2 − (39/8)z + cz², as (53/8)z³ ≥ 0, and Q_c > 0 because its
discriminant (39/8)² − 8c is negative for c ≥ 15/4. Second, (1 − z)^(1/2) ≥ (1 − z)(1 + z/2) on [0, 1]: with
t := (1 − z)^(1/2) ∈ [0, 1] this is 2 ≥ t(3 − t²), that is (t − 1)²(t + 2) ≥ 0. Hence
η ≥ 2^(−5/2)(1 + z)(1 − z)²(1 + z/2) ≥ 2^(−5/2)(1 − z/2 − 3z²/2) ≥ 0, the middle step dropping (z³ + z⁴)/2 ≥ 0.
Multiplying,

    w_l ≥ 2^(−5/2)(1 − z/2 − 3z²/2)Q_c = 2^(−5/2)(2 − (47/8)z + (c − 9/16)z² + (117/16)z³ − c(z/2 + 3z²/2)z²),

and z/2 + 3z²/2 ≤ 7/64 + 147/2048 = 1 − ρ on [0, 7/32]. Dropping (117/16)z³ ≥ 0 gives the bound. Its minimum over
z ∈ [0, 7/32] is at z = 47/(16d) when that lies in [0, 7/32], that is d ≥ 94/7, and at z = 7/32 otherwise.

(iii) On 2 ≤ r ≤ 3, y ∈ [1/9, 1/4] and z ∈ [1/2, 7/9] ⊂ [z_0, 1]: η ≥ η(1/9) = 8/243 and P̄ ≥ P̄(1/2) = 25/64, so
A ≥ 25/1944; and Z ≥ min(Z at r = 3, Z at r = 2) = min(392/19683, 3/128). On 17/10 ≤ r ≤ 2, y ∈ [1/4, 100/289]:
η ≥ η(1/4) = 3/32 and P̄ ≥ P̄(z_0) > 0.3902, so A ≥ 0.03658; Z ≥ Z(17/10) = (189000/1419857)(89/289)² > 0.012624, as
Z(2) = 3/128 is larger. On 8/5 ≤ r ≤ 17/10, z ∈ [7/32, 89/289] ⊂ [0, z_0]: η ≥ η(17/10) = 189000/1419857 and
P̄ ≥ P̄(89/289) = 66831535/96550276, so A > 0.09213; Z ≥ Z(8/5) = (4875/32768)(49/1024) = 238875/33554432.

(iv) We show that A and Z increase with y on [1/16, 1/9], so that w_l, an increasing combination, does too. There
z ∈ [7/9, 7/8] ⊂ [z_0, 1], so P̄ decreases with y, and |dP̄/dy| = 2P̄′(z) = (159/4)z² − 39/4. Now
d log Z/dy = 3/(2y) − 1/(1 − y) − 4/(1 − 2y) ≥ 27/2 − 9/8 − 36/7 > 0, and
d log A/dy = 3/(2y) − 1/(1 − y) + (dP̄/dy)/P̄.
On y ∈ [1/16, 1/12] the last expression is at least 18 − 12/11 − (5295/256)/(3061/1728) > 5.2, using P̄(5/6) = 3061/1728
and (159/4)(7/8)² − 39/4 = 5295/256; on [1/12, 1/10] it is at least 15 − 10/9 − (857/48)/(373/250) > 1.9, using
P̄(4/5) = 373/250; on [1/10, 1/9] it is at least 27/2 − 9/8 − 15.69/P̄(7/9) > 0.53, using P̄(7/9) > 1.3254. Finally
η(1/16) = 15/1024, P̄(7/8) = 8899/4096 and (7/8)² = 49/64.

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

Each B_l is even in σ, increasing in |σ| and bounded as σ → 0. [[prop:morawetz-harmonics]] improves these values for
l ≥ 1 with the multipliers of [[sec:morawetz-polynomial]].

*Proof.* [[prop:morawetz-weight]] gives the hypotheses of [[lem:morawetz-identity]] with φ = z, q = 0, and |φ| ≤ 1, so
p_I = p_∞ = 1. On I, φ′ = 4η has least value 4 min(η(1/16), η(25/36)) = 15/256, so m′ = 15/256 and 2/m′ = 512/15, and
greatest value 4η(3/5) = 24√15/125 < 0.74362, since 3.873² > 15. So w_I ≥ ω_l by [[lem:morawetz-weight-interval]], and
[[eq:pb-bound]] gives the bound; it decreases in w_I and increases in M′. The table evaluates the formula, rounding up. ∎

### The harmonic l = 0 {#sec:morawetz-l-zero}

**Proposition {#prop:morawetz-l-zero}** (The harmonic l = 0.) Let φ := 1 − 2/r² and q := ½η(1 + 3y/2). Then
0 ≤ q ≤ (5/16)φ′, and for V = V_0 at l = 0 (a = 3/4, b = 9/4) the weight of [[lem:morawetz-identity]] is

    W = (3/8)ηQ_4,     Q_4(y) := 149y⁴ − 280y³ + 177y² − 42y + 4
                               = (2 − (21/2)y + 11y²)² + y²(28(y − 7/8)² + 21/16) > 0.          {#eq:pb-lzero-weight}

On I, m′ = min_I(φ′ − q) = 3315/65536, M′ = max_I|φ′ − 2q| < 0.3999 and w_I = W(4) = 5899185/536870912 > 0.010988. So
for every real σ ≠ 0, ‖χ_I R_0(σ) χ_I‖ ≤ B_0(σ) := ((2/m′ + (M′ + 2|σ|)²/w_I)/w_I)^(1/2), which is at most 70.17,
226.50, 585.53 and 1857.54 at σ → 0, σ = 1, 3 and 10. For the bound off the real axis
([[pending:resolvent-off-axis]]), which replaces 2|σ| by 4|σ| + 2 max q, max q = 2√6/27 < 0.18145, attained at y = 2/3.

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

Here Q_4(1/16) = 131093/65536, so W(4) = (3/8)(15/1024)(131093/65536). [[lem:morawetz-identity]] applies with
p_I = p_∞ = 1, as |φ| ≤ 1, and the bounds follow from [[eq:pb-bound]]. For max q: d/dy(η(2 + 3y)) =
y^(1/2)(3 + (5/2)y − (21/2)y²), which vanishes on (0, 1) only at y = 2/3, where q = (1/3)(2/3)^(3/2) = 2√6/27. ∎

### Polynomial multipliers {#sec:morawetz-polynomial}

**Lemma {#lem:bernstein-lower-bound}** (Bernstein lower bound.) Let p be a polynomial of degree at most n and α < β.
Write p(α + (β − α)t) = Σ_(j≤n) c_j t^j and b_k := Σ_(j≤k) (C(k, j)/C(n, j))c_j for 0 ≤ k ≤ n. Then
min_k b_k ≤ p ≤ max_k b_k on [α, β]; in particular |p| ≤ max_k |b_k| there.

*Proof.* Expanding t^j = t^j(t + (1 − t))^(n−j) by the binomial theorem gives
t^j = Σ_(k≥j) (C(k, j)/C(n, j))C(n, k)t^k(1 − t)^(n−k), as C(n − j, k − j)/C(n, k) = C(k, j)/C(n, j). So
p(α + (β − α)t) = Σ_k b_k C(n, k)t^k(1 − t)^(n−k), a combination of the b_k with nonnegative weights of sum 1 on
t ∈ [0, 1]. ∎

**Lemma {#lem:morawetz-polynomial-weight}** (The weight of a polynomial multiplier.) Let F be a real polynomial in z
and g a real polynomial in y, with g ≥ 0 and 4F_z(1 − 2y) − g(y) ≥ 0 for 0 ≤ y ≤ 1, and put φ := F(z) and q := ηg. Then
φ and q satisfy the hypotheses of [[lem:morawetz-identity]] on φ and q, with φ(±∞) = F(±1); and q ≥ 0, φ′ = 4ηF_z,
φ′ − q = η(4F_z − g) ≥ 0 and φ′ − 2q = η(4F_z − 2g) on ℝ, the derivatives of F taken at z = 1 − 2y. For V = V_(a,b) or
V = V_S the weight of [[lem:morawetz-identity]] is W = ηG with

    G = 2FV_y − 8y(10y² − 12y + 3)F_z + 24(1 − y)y²(3 − 5y)F_zz − 32(1 − y)²y³F_zzz
        + 4y((2 − 3y)h + y(1 − y)h_y) − 2gV,                                                        {#eq:pb-weight-poly}

with h as in [[eq:pb-weight-general]]. If g = 0 and F(0) = 0, then zF ≥ 0 on [−1, 1], and for V = V_(a,b) the polynomial
G is affine in b and nondecreasing in a, with ∂_aG = 2zF; the a-part of W is a(−φU′), with −φU′ = 2ηzF ≥ 0.

*Proof.* φ is smooth and bounded, and z → ±1 as r_* → ±∞, so φ(±∞) = F(±1). By the remark after
[[eq:pb-weight-general]], φ′, φ″, φ‴, q, q′, q″ are integrable and tend to 0 at ±∞. With F_y = −2F_z,
[[eq:pb-tortoise]] gives φ′ = 4ηF_z, and the identities for φ′ − q and φ′ − 2q follow. Next,
4(η(ηF_y)_y)_y = 4(η_y² + ηη_yy)F_y + 12ηη_yF_yy + 4η²F_yyy, since (η²)_y = 2ηη_y; substituting F_y = −2F_z,
F_yy = 4F_zz, F_yyy = −8F_zzz, η_y² + ηη_yy = y(10y² − 12y + 3) (proof of [[prop:morawetz-weight]]),
ηη_y = (1 − y)y²(3 − 5y)/2 and η² = (1 − y)²y³ gives the F-terms of [[eq:pb-weight-poly]]; the others are those of
[[eq:pb-weight-general]]. If F(0) = 0 and F_z ≥ 0 on [−1, 1] (which holds when g = 0), F(z) has the sign of z. With
g = 0, G is linear in (a, b) up to an a- and b-free term, and the coefficient of a is 2FU_y = 2zF, since U_y = z;
−φU′ = 2ηFU_y = 2ηzF. ∎

**Proposition {#prop:morawetz-polynomial}** (Five polynomial multipliers.) Let

    F_A := z + (3/16)z² − (7/40)z³,               F_B := z + (9/20)z² − (17/120)z³ − (1/12)z⁴,
    F_2 := z − z³/3,                               F_C := z + (11/24)z² − (9/40)z³ − (17/60)z⁴,
    F_T := z + (7/20)z² − (3/40)z⁴,

with g = 0 for F_A, F_B, F_2 and F_C, and g = y/2 for F_T, so that q = 0, respectively q = ηy/2. Each pair (F, g)
satisfies the hypotheses of [[lem:morawetz-polynomial-weight]], and the constants of [[lem:morawetz-identity]] may be
taken as follows:

| multiplier | m′ | M′ | p_I | p_∞ | max q |
|---|---|---|---|---|---|
| F_A | 0.0537 | 0.72 | 18459/20480 | 81/80 | 0 |
| F_B | 0.0718 | 0.735 | 264383/245760 | 49/40 | 0 |
| F_2 | 0.0135 | 0.735 | 1001/1536 | 2/3 | 0 |
| F_C | 0.0305 | 0.735 | 74473/81920 | 19/20 | 0 |
| F_T | 0.0814 | 0.65 | 180061/163840 | 51/40 | (1/7)(5/7)^(5/2) < 0.06161 |

For the operators of each row below, W > 0 on ℝ, w_I is at least the value listed, and so, for every real σ ≠ 0 and
every harmonic of the row, ‖χ_I R(σ) χ_I‖ ≤ B(σ) := ((2p_I²/m′ + (M′ + 2p_∞|σ|)²/w_I)/w_I)^(1/2) with the constants of
the row's multiplier; B is even in σ and increasing in |σ|, and its values at σ → 0, σ = 1, 3 and 10 are at most:

| row | operators | multiplier | w_I ≥ | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|---|
| A | V_(a,b), a ≥ 15/4, 5/4 ≤ b ≤ 9/4 | F_A | 0.0728 | 22.66 | 42.87 | 95.54 | 288.77 |
| A′ | V_(a,9/4), a ≥ 15/4 | F_A | 0.0756 | 22.16 | 41.46 | 92.09 | 278.11 |
| B | V_(a,b), a ≥ 35/4, −7/4 ≤ b ≤ 9/4 | F_B | 0.211 | 12.85 | 19.51 | 40.27 | 120.24 |
| B′ | V_(a,9/4), a ≥ 35/4 | F_B | 0.224 | 12.44 | 18.61 | 38.04 | 113.30 |
| E | V_(a,9/4), a ≥ 35/4 | F_2 | 0.139 | 21.93 | 25.97 | 40.17 | 103.43 |
| C | V_(a,b), a ≥ 63/4, −27/4 ≤ b ≤ 9/4 | F_C | 0.325 | 13.11 | 15.25 | 23.64 | 62.09 |
| C3 | V_(a,9/4), a ≥ 63/4 | F_C | 0.352 | 12.59 | 14.50 | 22.10 | 57.43 |
| C4 | V_(a,9/4), a ≥ 99/4 | F_C | 0.559 | 9.94 | 10.92 | 15.15 | 36.66 |
| C5 | V_(a,9/4), a ≥ 143/4 | F_C | 0.80 | 8.29 | 8.87 | 11.51 | 26.01 |
| C6 | V_(a,9/4), a ≥ 195/4 | F_C | 0.815 | 8.21 | 8.78 | 11.36 | 25.56 |
| S3 | V_S, l = 3 | F_C | 0.302 | 13.62 | 15.99 | 25.17 | 66.71 |
| S4 | V_S, every l ≥ 4 | F_C | 0.515 | 10.36 | 11.47 | 16.17 | 39.67 |
| T2 | V_V, l = 2 | F_T | 0.19 | 12.96 | 20.98 | 45.44 | 138.20 |

At the harmonic l the scalar wave is V_(a,9/4) with a = κ + 3/4, which is 15/4, 35/4, 63/4, 99/4, 143/4 and 195/4 at
l = 1, …, 6; so rows A′, B′ and E, C3, C4, C5 and C6 serve every l ≥ 1, 2, 3, 4, 5 and 6 respectively.

*Proof.* The hypotheses. F_2 has F_z = 1 − z² ≥ 0. For F_A, F_B, F_C and F_T the Bernstein coefficients of F_z on [−1, 1]
(on [−1, 0] and [0, 1] for F_C) are positive ([[sec:tb-morawetz-monotone]]), so F_z > 0 on [−1, 1] by
[[lem:bernstein-lower-bound]]. For F_T, g = y/2 ≥ 0, and the Bernstein coefficients of 4F_z(1 − 2y) − y/2 on [0, 1] are
positive. So [[lem:morawetz-polynomial-weight]] applies to each pair. Each F is increasing on [−1, 1], so on I,
|F| ≤ max(|F(7/8)|, |F(−7/18)|) = F(7/8), and φ(±∞) = F(±1); these values are listed in [[sec:tb-morawetz-monotone]] and
give p_I and p_∞. For F_T, q = ½(1 − y)y^(5/2), whose derivative ¼y^(3/2)(5 − 7y) vanishes on (0, 1) only at y = 5/7.

The weights. By [[lem:morawetz-polynomial-weight]], W = ηG with G of [[eq:pb-weight-poly]], a polynomial in y for
V = V_(a,b). [[sec:tb-morawetz-weights]] lists G at the corners A1 = (15/4, 5/4), A2 = (15/4, 9/4), B1 = (35/4, −7/4),
B2 = (35/4, 9/4), C1 = (63/4, −27/4), C3 = (63/4, 9/4), C4 = (99/4, 9/4), C5 = (143/4, 9/4) and C6 = (195/4, 9/4) of
their multipliers, G for F_2 at (35/4, 9/4) (E2), G for F_T and V_V at l = 2, that is (35/4, −27/4) (T2), and, for V_S
at l = 3, where p = 12 and H = 6(2 + y), the polynomial Π := 120(2 + y)³G (S3). Their Bernstein coefficients on the
subintervals of [0, 1] listed in [[sec:tb-morawetz-positivity]] are positive, so each is positive on [0, 1] by
[[lem:bernstein-lower-bound]], and W > 0 on ℝ. For F_A, F_B, F_2 and F_C, g = 0 and F(0) = 0, so G is nondecreasing in a
and affine in b: in row A, for a ≥ 15/4 and 5/4 ≤ b ≤ 9/4, G is at least the smaller of its values at A1 and A2, on ℝ
and on I; in the same way rows B and C reduce to the corners B1, B2 and C1, C3, and rows A′, B′, E, C3, C4, C5 and C6
to the single corners A2, B2, E2, C3, C4, C5 and C6.

Row S4. Here κ ≥ 24, p = κ − 3 = 21 + t with t := κ − 24 ≥ 0, and H = H_0 + t with H_0 := 21 + 6y. Expanding,
16H³G = Σ_(j≤4) c_j(y)t^j with the polynomials c_0, …, c_4 of [[sec:tb-morawetz-weights]]; c_4 = 32zF_C(z) ≥ 0 by
[[lem:morawetz-polynomial-weight]], and c_0, …, c_3 have positive Bernstein coefficients on [0, 1/2] and [1/2, 1]
([[sec:tb-morawetz-positivity]]), so they are positive on [0, 1]. Since (H_0 + t)³ = Σ_(j≤3) C(3, j)H_0^(3−j)t^j,

    G ≥ ζ(y) := min_(j≤3) c_j/(16C(3, j)H_0^(3−j)) > 0     for every t ≥ 0,

uniformly in l ≥ 4.

The lower bounds for w_I. In each row the pieces of [[sec:tb-morawetz-pieces]] cover I, and on a piece
w = ηG ≥ (least value of η)(least Bernstein coefficient of G) by [[lem:bernstein-lower-bound]], the least value of η
being attained at an end of the piece ([[sec:morawetz-identity]]); in rows with two corners this is done for each corner.
For S3 the least coefficient of Π is divided by 120(2 + y)³ at the right end of the piece, its largest value there; for
S4, ζ is bounded below by the least Bernstein coefficients of c_0, …, c_3 with H_0 at the right end of the piece. Every
product listed is at least the w_I of its row.

The constants m′ and M′. On the pieces of [[sec:tb-morawetz-mM]], η(4F_z − g) is bounded below by the least value of η
times the least Bernstein coefficient of 4F_z − g, and |η(4F_z − 2g)| above by the largest value of η times the largest
modulus of a Bernstein coefficient of 4F_z − 2g. Every product is at least m′, respectively at most M′.

Finally [[eq:pb-bound]] gives the bound for each operator of a row and every harmonic of it, and the table evaluates it
with the constants above, rounding up. ∎

### Every harmonic of the scalar wave {#sec:morawetz-harmonics}

**Proposition {#prop:morawetz-harmonics}** (The scalar wave at every harmonic.) (i) For l ≥ 1 let B*_l(σ) be the least of
B_l(σ) of [[prop:morawetz-resolvent-l-ge-1]] and the bounds B(σ) of the rows A′ (l ≥ 1), B′ and E (l ≥ 2), C3 (l ≥ 3),
C4 (l ≥ 4), C5 (l ≥ 5) and C6 (l ≥ 6) of [[prop:morawetz-polynomial]], each taken when l is in its range. Then for every
real σ ≠ 0, ‖χ_I R_l(σ) χ_I‖ ≤ B*_l(σ); B*_l is even in σ, increasing in |σ| and bounded as σ → 0; and for l ≥ 6,
B*_l is at most the least of B_6 and the bound of row C6, which the line "every l ≥ 6" below evaluates.

(ii) For l = 0 put B*_0(σ) := B_0(σ) of [[prop:morawetz-l-zero]] for 0 < |σ| < 1, and
B*_0(σ) := min(B_0(σ), Λ|σ|/(σ² − 25/48)) for |σ| ≥ 1. Then ‖χ_I R_0(σ) χ_I‖ ≤ B*_0(σ), and B*_0(σ) < 7.8128 for
|σ| ≥ 1.

At σ → 0 and |σ| = 1/2, 1, 2, 3 and 10, B*_l is at most:

| l | σ → 0 | 1/2 | 1 | 2 | 3 | 10 |
|---|---|---|---|---|---|---|
| 0 | 70.17 | 140.82 | 7.82 | 2.16 | 1.33 | 0.38 |
| 1 | 22.16 | 30.43 | 41.46 | 66.20 | 92.09 | 278.11 |
| 2 | 12.44 | 14.85 | 18.61 | 27.88 | 38.04 | 103.43 |
| 3 | 11.26 | 12.55 | 14.50 | 17.89 | 22.10 | 57.43 |
| 4 | 9.94 | 10.30 | 10.92 | 12.76 | 15.15 | 36.66 |
| 5 | 8.29 | 8.50 | 8.87 | 10.00 | 11.51 | 26.01 |
| every l ≥ 6 | 8.21 | 8.42 | 8.78 | 9.88 | 11.36 | 25.56 |

*Proof.* (i) By the last sentence of [[prop:morawetz-polynomial]], each listed row contains V_(κ+3/4,9/4) for the l in
its range, and each bound is even in σ and increasing in |σ|, hence so is their least. For l ≥ 6, rows C6 and
[[prop:morawetz-resolvent-l-ge-1]] give bounds independent of l. The entries come from row A′ at l = 1; from row B′ at
l = 2, except at σ = 10, from row E; from [[prop:morawetz-resolvent-l-ge-1]] at l = 3 for σ → 0 and |σ| = 1/2, and from
row C3 otherwise; and from rows C4, C5 and C6 at l = 4, 5 and every l ≥ 6. At |σ| = 1/2 and 2 they evaluate
[[eq:pb-bound]] with the constants of those rows, rounding up.

(ii) max V_(a,b) ≤ a max U + b max Q = a/4 + 4b/27 for a, b ≥ 0, since U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27; at
l = 0 this is 3/16 + 1/3 = 25/48 < 1. For σ² > max V_0 the bound above the barrier ([[pending:resolvent-above-barrier]])
gives ‖χ_I R_0(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_0) ≤ Λ|σ|/(σ² − 25/48). As Λt/(t² − 25/48) decreases for t² > 25/48, its value
for |σ| ≥ 1 is at most Λ/(23/48) < 3.7436 · 48/23 < 7.8128. The entries at l = 0 are B_0(0+) and B_0(1/2) of
[[prop:morawetz-l-zero]] and 3.7436|σ|/(σ² − 25/48) at |σ| = 1, 2, 3, 10, rounded up. ∎

At |σ| ≥ 3 the bound above the barrier also improves the entries for 1 ≤ l ≤ 4 ([[prop:morawetz-large-frequency]]); the
estimates below use B*_l for l ≥ 1 because it is increasing in |σ|.

### One derivative {#sec:morawetz-one-derivative}

**Corollary {#cor:morawetz-one-derivative}** (The H¹ constants.) Let σ ≠ 0 be real, f ∈ L²(I) and u = R_l(σ)f, with
ψ = 2ηz² the weight of [[prop:morawetz-weight]], which vanishes on ℝ only at the photon sphere r = √2, to second order.
Let B*_l be as in [[prop:morawetz-harmonics]].

(a) For l ≥ 1, with m′ = 15/256 and M′ = 0.74362, ‖u′‖_I ≤ X_l‖f‖ and (κ − 3)∫_Iψ|u|² ≤ J_l‖f‖², where
X_l := (1 + (1 + 2m′(M′ + 2|σ|)B*_l)^(1/2))/(2m′) and J_l := 2X_l + (M′ + 2|σ|)B*_l. Put A_l := κJ_l/(κ − 3) for
l ≥ 2, A_1 := 3(B*_1)² and C_l := (X_l² + A_l)^(1/2). At σ = 3, each line bounding its quantity from the lines above it:

| l | 1 | 2 | 3 | 4 | 5 | ≥ 6 |
|---|---|---|---|---|---|---|
| B*_l(3) ≤ | 92.081 | 38.036 | 22.095 | 15.149 | 11.509 | 11.351 |
| X_l ≤ | 81.826 | 56.090 | 45.198 | 39.268 | 35.647 | 35.479 |
| J_l ≤ | — | 368.69 | 239.40 | 180.70 | 148.91 | 147.51 |
| A_l ≤ | 25,436.8 | 590.0 | 299.3 | 206.6 | 162.9 | 157.4 |
| C_l ≤ | 179.26 | 61.13 | 48.40 | 41.82 | 37.87 | 37.64 |

(b) For l = 0, with m′_0 := 3315/65536 and M′_0 := 0.3999 of [[prop:morawetz-l-zero]], ‖u′‖_I ≤ X_0‖f‖ with
X_0 := (1 + (1 + 2m′_0(M′_0 + 2|σ|)B*_0)^(1/2))/(2m′_0). X_0 ≤ 83.85 for every real 0 < |σ| ≤ 3, and X_0(3) < 23.36.

(c) Summed over the harmonics, which are orthogonal on 𝕊³: let f ∈ L²(I × 𝕊³) have harmonic components f_l, and put
u_l := R_l(σ)f_l and u := Σ_l u_l. For every real 0 < |σ| ≤ 3,

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖f‖²,     C ≤ 179.26,

over every l ≥ 0, the angular part at l = 1 taken unweighted. At |σ| = 1/2, 1, 2 and 3 one may take C = C_1, that is
61.37, 82.61, 129.87 and 179.26: there max_(l≥2) C_l = C_2 is at most 27.98, 33.88, 47.07 and 61.13, and X_0 at most
55.13, 26.71, 23.72 and 23.36.

(d) Without the weight: for every real 0 < |σ| ≤ 3, ‖∂_(r_*)u‖_I² + Σ_l κ‖u_l‖_I² ≤ C_u²‖f‖² with C_u < 568.55.

*Proof.* (a) and (b) are [[lem:morawetz-identity]] with B̃ = B*_l, applied to φ = z with q = 0 for l ≥ 1 and to the
multiplier of [[prop:morawetz-l-zero]] for l = 0, both with p_I = p_∞ = 1. In (a), W_1 := (κ − 3)ψ and W_0 := w_1 are
nonnegative ([[prop:morawetz-weight]]); so (κ − 3)∫_Iψ|u|² ≤ J_l‖f‖², and κ∫_Iψ|u|² ≤ A_l‖f‖² for l ≥ 2. At l = 1,
3‖u‖_I² ≤ 3(B*_1)²‖f‖². For l ≥ 6, B*_l is at most the line "every l ≥ 6" of [[prop:morawetz-harmonics]], X_l and J_l
increase with B*_l, and κ/(κ − 3) decreases, so C_l ≤ C_6. In the table each entry is evaluated from the rounded entries
above it and rounded up. In (b), for 0 < |σ| ≤ 1, X_0 increases with |σ| and with B*_0 ≤ B_0 ≤ B_0(1) < 226.50, so
X_0 ≤ (1 + (1 + (3315/32768)(2.3999)(226.50))^(1/2))(32768/3315) < 83.85; for 1 ≤ |σ| ≤ 3, B*_0 < 7.8128 and |σ| ≤ 3
give X_0 ≤ (1 + (1 + (3315/32768)(6.3999)(7.8128))^(1/2))(32768/3315) < 34.22. At |σ| = 3, B*_0 < 1.3246 gives
X_0 < 23.36.

(c) For l ≥ 1 every quantity in (a) is an explicit function increasing in |σ|, so the values at |σ| = 3 bound the band;
X_0 ≤ 83.85 there by (b). The harmonics are orthogonal, so the sum is at most the largest of C_l² (l ≥ 1) and X_0²
times ‖f‖², and C_l ≤ C_1 for every l ≥ 1 by the table. At |σ| = 1/2, 1 and 2 the same evaluation of (a), with B*_l of
[[prop:morawetz-harmonics]] at that σ, gives C_1 = 61.37, 82.61, 129.87 and C_l ≤ C_2 for l ≥ 2, and (b) gives the X_0
listed.

(d) The left side is at most max_l (X_l² + κB_l²)‖f‖², with any valid bound B_l. For l ≥ 50 we use the closed-form
bound for large harmonics ([[pending:resolvent-closed-form]]): with c := (15/16)(κ + 3/4),
‖χ_I R_l(σ) χ_I‖ ≤ 1/((15/256)(κ + 3/4) − σ²) whenever (15/256)(κ + 3/4) > σ² and (0.21/1.4641)(κ + 3/4) > σ²;
0.32727(0.120523(κ + 3/4) − σ²)^(1/2) > (2 + 1.1248|σ|)/√2; and c^(1/2) > 8|σ| and
(√3/2)c^(1/2) log(c^(1/2)/(8|σ|)) > (2 + 0.79217(κ + 1)^(1/2))/√2. At l = 50 (κ + 3/4 = 2600.75) and |σ| = 3 these
read 152.38 > 9 and 373.0 > 9; 0.32727(313.45 − 9)^(1/2) > 5.71 > (2 + 3.3744)/√2; and c > 2438.2,
c^(1/2) > 49.37 > 24 and (√3/2)(49.37) log(49.37/24) > 30.8 > 29.99 > (2 + 0.79217 · 51)/√2. Each condition becomes
easier as l grows or |σ| decreases, so the bound holds for l ≥ 50 and 0 < |σ| ≤ 3; there B_l ≤ 0.006975,
X_l² + κB_l² < 17.1², and both terms decrease in κ. For 1 ≤ l ≤ 49 we use B*_l(3): (X_l² + κ(B*_l)²)^(1/2) is at most
179.26, 121.33, 96.78, 83.97 and 76.86 for l = 1, …, 5 (with the table's entries), and for 6 ≤ l ≤ 49, with
B*_l ≤ 11.351, X_l ≤ 35.479 and κ ≤ 2499, at most (35.479² + 2499 · 11.351²)^(1/2) < 568.55. At l = 0 the term is
X_0² ≤ 83.85². ∎

### The master operators {#sec:morawetz-master}

For rows T1 and T3 below the weight is W = ηΠ/D with Π a polynomial and D = 1 (T1) or D = 4(1 + 2y)⁴(5 + 6y)³ (T3),
positive and increasing in y. A lower bound on a piece r ∈ [r_2, r_1] (y ∈ [1/r_1², 1/r_2²]) is the product of η at
the end where it is least and of the least Bernstein coefficient of Π on the piece divided by the value of D at its
right end in y; this is a lower bound because that least coefficient is positive on every piece below. Each piece is
written "r_1–r_2: e · g ≥ v" with e and g such lower bounds; the Bernstein coefficients are listed in
[[sec:tb-morawetz-t1t3]].

**Proposition {#prop:morawetz-master-potentials}** (Every master operator at every harmonic.) For the operator
−∂²_(r_*) + V − σ² of each of the following rows, every real σ ≠ 0 and every harmonic of the row,
‖χ_I R(σ) χ_I‖ ≤ B(σ), the bound [[eq:pb-bound]] with the row's constants, whose values at σ → 0, σ = 1, 3 and 10 are:

| row | operators and harmonics | multiplier | B(0+) | B(1) | B(3) | B(10) |
|---|---|---|---|---|---|---|
| A | V_0, V_1, every l ≥ 1 | F_A | 22.66 | 42.87 | 95.54 | 288.77 |
| B | V_0, V_1, V_2, V_T, every l ≥ 2 | F_B | 12.85 | 19.51 | 40.27 | 120.24 |
| C | V_0, V_1, V_2, V_T, V_V, every l ≥ 3 | F_C | 13.11 | 15.25 | 23.64 | 62.09 |
| S4 | V_S, every l ≥ 4 | F_C | 10.36 | 11.47 | 16.17 | 39.67 |
| S3 | V_S, l = 3 | F_C | 13.62 | 15.99 | 25.17 | 66.71 |
| T1 | V_2, l = 1 | z, q = (5/3)ηy | 29.22 | 59.91 | 143.71 | 449.56 |
| T2 | V_V, l = 2 | F_T, q = ηy/2 | 12.96 | 20.98 | 45.44 | 138.20 |
| T3 | V_S, l = 2 | (1 − 4y)/(1 + 2y), q = ½ηy(1 + y) | 23.15 | 64.82 | 160.01 | 498.25 |

Rows A, B, C, S4, S3 and T2 are those of [[prop:morawetz-polynomial]]. In rows T1 and T3, p_I = p_∞ = 1, w_I ≥ 0.0455
and 0.0413, and (m′, M′) = (935/16384, 0.4157) and (0.1384, 0.563). The largest values over all rows are 29.22, 64.82,
160.01 and 498.25. With V_0 at l = 0 ([[prop:morawetz-harmonics]] (ii)), the largest values over every master operator
and every harmonic are 70.17, 64.82, 160.01 and 498.25. Multiplied by 15/16, the transfer of
[[pending:resolvent-transfer]], rows A and B bound the vector-type 1-form blocks at l = 1 (21.25, 40.20, 89.57, 270.73)
and at l ≥ 2 (12.05, 18.30, 37.76, 112.73), and row B the tensor-type blocks, every l ≥ 2 (the same). For the bound off
the real axis ([[pending:resolvent-off-axis]]), which adds 2 max q, max q is 0 in rows A to S3 and less than 0.20534,
0.06161 and 0.10659 in rows T1, T2 and T3.

*Proof.* Rows A, B, C, S4, S3 and T2: V_0 = V_(κ+3/4,9/4) and V_1 = V_(κ+3/4,5/4), and at l ≥ 1, κ + 3/4 ≥ 15/4, which is
row A of [[prop:morawetz-polynomial]]. At l ≥ 2, κ + 3/4 ≥ 35/4 and V_2 = V_(κ+3/4,−7/4), V_T = V_0 lie in its row B. At
l ≥ 3, κ + 3/4 ≥ 63/4 and b ∈ {9/4, 5/4, −7/4, −27/4} ⊂ [−27/4, 9/4], so V_0, V_1, V_2, V_T and V_V lie in its row C.
V_S at l = 3 and at l ≥ 4 are its rows S3 and S4, and V_V at l = 2 its row T2. The values are those of
[[prop:morawetz-polynomial]].

Row T1 (a = 15/4, b = −7/4). Here a + b = 2 < 4, so P_(a,b)(−1) = 2(a + b − 4) < 0: with q = 0 the weight of
[[prop:morawetz-weight]] is negative near the horizon, and the term q is needed there. g = (5/3)y gives
Π = 15/2 − 61y + 188y² − (728/3)y³ + (665/6)y⁴; Bernstein on [0, 1/4], [1/4, 1/2], [1/2, 3/4], [3/4, 1]: at least 0.641,
0.292, 0.193, 0.101. Pieces: 4–16/5: 0.01464 · 3.119 ≥ 0.0456; 16/5–13/5: 0.02753 · 1.857 ≥ 0.0511; 13/5–11/5:
0.04847 · 0.9837 ≥ 0.0476; 11/5–2: 0.07451 · 0.6412 ≥ 0.0477; 2–19/10: 0.09375 · 0.5229 ≥ 0.049; 19/10–17/10:
0.1054 · 0.432 ≥ 0.0455; 17/10–13/10: 0.1331 · 0.4373 ≥ 0.0582; 13/10–6/5: 0.1768 · 0.3101 ≥ 0.0548. Also
φ′ − q = η(12 − 5y)/3 > 0; d log(η(12 − 5y))/dy ≥ 3 − 2 − 5/9.5 > 0 on [1/16, 1/2] and η(12 − 5y)/3 > 0.5 on
[1/2, 25/36], so m′ = (15/1024)(187/48) = 935/16384; φ′ − 2q = (2/3)η(6 − 5y) has its maximum on (0, 1) at the root
y = (55 − √505)/70 of 35y² − 55y + 18, where it is less than 0.4157. q = (5/3)(1 − y)y^(5/2) has its maximum at y = 5/7,
(10/21)(5/7)^(5/2) < 0.20534.

Row T3 (V_S at l = 2, p = 5, H = 5 + 6y). Here F = (1 − 4y)/(1 + 2y) decreases from 1 to −1 on [0, 1], so |φ| ≤ 1,
φ → ±1 at ±∞, and φ′ = 12η/(1 + 2y)² > 0. With g = ½y(1 + y), [[eq:pb-weight-general]] gives G = Π/D with
D = 4(1 + 2y)⁴(5 + 6y)³ and

    Π = 8750 − 52800y − 52305y² + 661453y³ + 1153253y⁴ − 668761y⁵ − 2258994y⁶ − 1768052y⁷ − 1623176y⁸
        + 831312y⁹ + 3571104y¹⁰ + 2896704y¹¹ + 777600y¹²;

Bernstein on [0, 1/2], [1/2, 3/4], [3/4, 1]: at least 228, 27800, 34900. Pieces: 4–33/10: 0.01464 · 3.014 ≥ 0.0441;
33/10–29/10: 0.02527 · 1.742 ≥ 0.044; 29/10–27/10: 0.03612 · 1.243 ≥ 0.0448; 27/10–13/5: 0.04383 · 1.048 ≥ 0.0459;
13/5–5/2: 0.04847 · 0.9003 ≥ 0.0436; 5/2–12/5: 0.05376 · 0.793 ≥ 0.0426; 12/5–23/10: 0.05977 · 0.7024 ≥ 0.0419;
23/10–11/5: 0.06665 · 0.6601 ≥ 0.0439; 11/5–2: 0.07451 · 0.5544 ≥ 0.0413; 2–17/10: 0.09375 · 0.4985 ≥ 0.0467;
17/10–13/10: 0.1331 · 0.3475 ≥ 0.0462; 13/10–6/5: 0.1768 · 0.3621 ≥ 0.064. Also
φ′ − q = η(24 − y − 5y² − 8y³ − 4y⁴)/(2(1 + 2y)²) > 0; its logarithmic derivative is positive on [1/16, 1/4] (at least
6 − 4/3 − 0.23 − 3.56) and it exceeds 0.14 on [1/4, 25/36], so m′ is its value at y = 1/16, more than 0.1384. On I,
0 < φ′ − 2q = η(12 − y − 5y² − 8y³ − 4y⁴)/(1 + 2y)² ≤ 12η/(1 + 2y)²: the quartic decreases on [0, 1] and is more than
5.28 at y = 25/36. The maximum of 12η/(1 + 2y)² on (0, 1) is at the root y = (√73 − 7)/4 of 2y² + 7y − 3, where it is
less than 0.563. q = ½(1 − y²)y^(5/2) has its maximum at y = √5/3, (2/9)(5/9)^(5/4) < 0.10659.

In rows T1 and T3, q ≥ 0 and φ′ − q > 0 on ℝ, and [[eq:pb-bound]] with p_I = p_∞ = 1 gives the values listed. The
transfers are 15/16 times the values of rows A and B, rounded up. ∎

### Large frequencies with a fixed multiplier {#sec:morawetz-large-frequency}

**Proposition {#prop:morawetz-large-frequency}** (Every harmonic at a given frequency.) Let B_(C5) and B_(C6) be the
bounds of rows C5 and C6 of [[prop:morawetz-polynomial]]. For every real σ with |σ| ≥ 3 and every l ≥ 0,

    ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 6.521), B_(C5)(σ)),

and for |σ| ≥ 6 also ‖χ_I R_l(σ) χ_I‖ ≤ max(Λ|σ|/(σ² − 9.271), B_(C6)(σ)). In particular, for every l ≥ 0, the norm is
at most 11.51, 16.98, 30.01, 57.44, 113.10 and 224.86 at |σ| = 3, 6, 12, 24, 48 and 96.

*Proof.* As in the proof of [[prop:morawetz-harmonics]] (ii), max V_(κ+3/4,9/4) ≤ (κ + 3/4)/4 + 1/3: at most 6.521 for
l ≤ 4 and 9.271 for l ≤ 5. When σ² exceeds it, the bound above the barrier ([[pending:resolvent-above-barrier]]) gives
‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V). So for |σ| ≥ 3 the harmonics l ≤ 4 are bounded by Λ|σ|/(σ² − 6.521), and for
|σ| ≥ 6 the harmonics l ≤ 5 by Λ|σ|/(σ² − 9.271); the others are bounded by B_(C5)(σ), respectively B_(C6)(σ), as
row C5 serves every l ≥ 5 and row C6 every l ≥ 6. At |σ| = 3 the first term is at most 3.7436 · 3/2.479 < 4.54 and
B_(C5)(3) < 11.51; for |σ| ≥ 6 the first term is at most 3.7436 · 6/26.729 < 0.85, as Λt/(t² − c) decreases for
t² > c, and the values given are B_(C6)(σ), rounded up. ∎
