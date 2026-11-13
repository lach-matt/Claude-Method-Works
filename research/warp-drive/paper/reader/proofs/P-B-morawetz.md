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
