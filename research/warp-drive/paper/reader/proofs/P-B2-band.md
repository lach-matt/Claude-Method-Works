## The resolvent bound on the band 3 ≤ |σ| ≤ 384 {#sec:band}

This part proves that the cut-off resolvent of the scalar wave operator on five-dimensional Schwarzschild–Tangherlini
with m = 1 is bounded by 11.477 for every harmonic and every real 3 ≤ |σ| ≤ 384, and derives from it the one-derivative
constants on that band. The notation is that of [[sec:morawetz-identity]]: y = 1/r², z = 1 − 2y, η = (1 − y)y^(3/2),
d/dr_* = −2η d/dy, I = {6/5 ≤ r ≤ 4} = {−7/18 ≤ z ≤ 7/8}, Λ < 3.7436 its length in r_*, U = (1 − y)y, Q = (1 − y)y²,
V_(a,b) = aU + bQ, κ = l(l + 2), and V_l = V_(κ+3/4,9/4) is the potential of the harmonic l. We also write v := 1/r, so
that y = v², η = (1 − v²)v³ and I = {1/4 ≤ v ≤ 5/6}.

For real σ ≠ 0, R_l(σ) is the outgoing resolvent of −∂²_(r_*) + V_l − σ² on L²(ℝ, dr_*) ([[ch:resolvent-bounds]]),
and χ_I is multiplication by the indicator function of I. Two results of that chapter are used, stated here exactly.
First ([[pending:resolvent-outgoing]]), for real σ ≠ 0 and f ∈ L²(ℝ) vanishing off I, u := R_l(σ)f is a solution,
with u and u′ locally absolutely continuous, of −u″ + (V_l − σ²)u = f almost everywhere, with u − c_±e^(±iσr_*) → 0
and u′ ∓ iσu → 0 as r_* → ±∞, as required in [[lem:morawetz-identity]]. Second ([[pending:resolvent-above-barrier]]),
the bound above the barrier: if σ² > max V_l, then ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − max V_l).

The route is the multiplier method of [[lem:morawetz-identity]], with two changes. The final inequality is solved exactly
and the flux term is combined with the pairing, which gives the constant B♯ of [[lem:band-sharp]]. And the multiplier is
allowed to depend on the frequency range: three multipliers polynomial in z serve 3 ≤ |σ| ≤ 14, and three members of
the algebraic family Φ(νz), Φ(x) = x(1 + x²)^(−1/2), serve 14 ≤ |σ| ≤ 384. A multiplier that is admissible for one
harmonic l_1 is admissible for every l ≥ l_1, and the harmonics below l_1 lie above their barrier, so one multiplier
covers a whole range of frequencies.

### The multiplier bound in sharp form {#sec:band-sharp}

**Lemma {#lem:band-sharp}** (The multiplier bound in sharp form.) Let V be as in [[lem:morawetz-identity]], σ ≠ 0 real,
f ∈ L²(ℝ) vanishing off I, and u a solution, with u and u′ locally absolutely continuous, of −u″ + (V − σ²)u = f
almost everywhere, with the asymptotics stated there. Let φ be a real smooth nondecreasing
function on ℝ with limits φ(±∞), with φ′, φ″, φ‴ integrable and tending to 0 at ±∞, and suppose that
w := −φV′ − ½φ‴ ≥ 0 on ℝ. Put

    m′ := min_I φ′ > 0,   M′ := max_I φ′,   w_I := min_I w > 0,   p_I := max_I |φ|,   p_∞ := max(|φ(∞)|, |φ(−∞)|).

Then ‖u‖_I ≤ B♯‖f‖, where

    B♯ := (c + (c² + 2p_I²w_I/m′)^(1/2))/(2w_I),     c := (M′² + 4σ²p_∞²)^(1/2).                    {#eq:band-sharp}

B♯ increases with |σ|, M′, p_I and p_∞, and decreases as m′ or w_I increases.

*Proof.* In the proof of [[lem:morawetz-identity]] take the Lagrangian term q = 0. The pointwise identity there,
Re(f(2φū′ + φ′ū)) = 2φ′|u′|² + w|u|² + E′, holds almost everywhere and does not use the values of φ at ±∞. Its
boundary term E = −φ|u′|² − φ′Re(u′ū) + ½φ″|u|² + (V − σ²)φ|u|² is locally absolutely continuous, since u and u′ are,
and it tends to −2σ²φ(±∞)|c_±|² at ±∞, since |u′|² → σ²|c_±|², |u|² → |c_±|² and φ′, φ″, V → 0. Integrating over
[−R, R], where ∫E′ = E(R) − E(−R), and letting R → ∞ (the integrand on the left is nonnegative, f vanishes off I),

    ∫(2φ′|u′|² + w|u|²) = Re∫f(2φū′ + φ′ū) + 2σ²(φ(∞)|c_+|² − φ(−∞)|c_−|²).                    {#eq:band-identity}

The last term is at most 2σ²p_∞(|c_+|² + |c_−|²), and by the flux identity σ(|c_+|² + |c_−|²) = −Im∫fū of
[[lem:morawetz-identity]] this equals −2σp_∞Im∫fū = Re∫f · conj(−2iσp_∞u). So, with X := ‖u′‖_I and Y := ‖u‖_I, since
both integrands on the left are nonnegative and f vanishes off I,

    2m′X² + w_IY² ≤ Re∫_I f · conj(2φu′ + (φ′ − 2iσp_∞)u) ≤ ‖f‖(2p_IX + cY),

because |φ| ≤ p_I on I and |φ′ − 2iσp_∞| = (φ′² + 4σ²p_∞²)^(1/2) ≤ c there. For every real X,
2m′X² − 2p_I‖f‖X ≥ −p_I²‖f‖²/(2m′); hence w_IY² − c‖f‖Y − p_I²‖f‖²/(2m′) ≤ 0, and Y is at most the positive root of
this quadratic, which is B♯‖f‖. Finally B♯ = c/(2w_I) + (c²/(4w_I²) + p_I²/(2m′w_I))^(1/2), which gives the
monotonicity. ∎

Since every hypothesis and the constant depend on σ only through |σ|, every bound below is even in σ.

**Lemma {#lem:band-barrier}** (Harmonics above the barrier.) For every l ≥ 0, max V_l ≤ κ/4 + 25/48. Consequently, if
σ² > κ/4 + 25/48, then ‖χ_I R_l(σ) χ_I‖ ≤ Λ|σ|/(σ² − κ/4 − 25/48), which decreases as |σ| increases; and if
σ² − κ/4 − 25/48 ≥ |σ|/2, then ‖χ_I R_l(σ) χ_I‖ ≤ 2Λ < 7.4872.

*Proof.* U = (1 − y)y ≤ 1/4 and Q = (1 − y)y² ≤ 4/27 on [0, 1], so V_l ≤ (κ + 3/4)/4 + (9/4)(4/27) = κ/4 + 25/48. The
bound above the barrier ([[pending:resolvent-above-barrier]]) then gives the first estimate, and t ↦ Λt/(t² − C)
decreases for t² > C, its derivative being −Λ(t² + C)/(t² − C)². The last statement is the first with
σ² − κ/4 − 25/48 ≥ |σ|/2. ∎

### The weight of a multiplier in the variable z {#sec:band-weights}

**Lemma {#lem:band-weight-z}** (The weight in the variable z.) Let F be a smooth function of z ∈ [−1, 1] and
φ := F(z(r_*)). Then φ′ = 4ηF_z, and for V = V_(a,b) the weight w := −φV′ − ½φ‴ is w = ηG with

    G = 2FV_y − ½Ξ_zzF_z − (3/2)Ξ_zF_zz − ΞF_zzz,     Ξ := (1 + z)²(1 − z)³,
    V_y = az + (b/4)(1 − z)(1 + 3z),
    Ξ_z = −(1 + z)(1 − z)²(1 + 5z),     Ξ_zz = 4(1 − z)(5z² + 2z − 1).                              {#eq:band-weight-z}

If F has the sign of z, then for a ≥ a′ the weights of V_(a,b) and V_(a′,b) satisfy G_(a,b) − G_(a′,b) = 2(a − a′)zF ≥ 0.

*Proof.* [[eq:pb-weight-general]] with g = 0 gives φ′ = −2ηF_y and G = 2FV_y + 4(η(ηF_y)_y)_y. Since
η(ηF_y)_y = ½(η²)_yF_y + η²F_yy, the second term is 2(η²)_yyF_y + 6(η²)_yF_yy + 4η²F_yyy. As y = (1 − z)/2 and
1 − y = (1 + z)/2, η² = (1 − y)²y³ = Ξ/32; and d/dy = −2 d/dz, so (η²)_y = −Ξ_z/16, (η²)_yy = Ξ_zz/8, F_y = −2F_z,
F_yy = 4F_zz and F_yyy = −8F_zzz. Substituting gives [[eq:band-weight-z]] and φ′ = 4ηF_z. The formulas for Ξ_z and
Ξ_zz follow by differentiating Ξ, and V_y = a(1 − 2y) + by(2 − 3y) with y(2 − 3y) = (1 − z)(1 + 3z)/4 (as in the proof
of [[prop:morawetz-weight]]). G is affine in a, and the coefficient of a is 2zF. ∎

### Polynomial multipliers for 3 ≤ |σ| ≤ 14 {#sec:band-polynomial}

**Proposition {#prop:band-polynomial}** (Three polynomial multipliers.) Let (l_1, Ψ, w_*, m_*, m^*) be one of the rows
Ψ_5, Ψ_7, Ψ_11 of [[sec:tb2-polynomial-multipliers]], put F := zΨ(z), and let p_I and p_∞ be the values listed there.
Then for every l ≥ l_1 the multiplier φ := F(z(r_*)) satisfies the hypotheses of [[lem:band-sharp]] with V = V_l, and
min_I w ≥ w_*, m′ ≥ m_*, M′ ≤ m^*. Hence, for every real σ ≠ 0 and every l ≥ l_1,

    ‖χ_I R_l(σ) χ_I‖ ≤ B♯(σ),   B♯ the constant [[eq:band-sharp]] with w_I = w_*, m′ = m_*, M′ = m^* and p_I, p_∞.

*Proof.* Every claim below is the positivity of one of the six polynomials (items 1–6) of [[sec:tb2-bernstein]] on an
interval, which that section cuts into pieces. Each polynomial is given there exactly, and on each piece the section
prints every Bernstein coefficient b_0, …, b_n of [[lem:bernstein-lower-bound]] (n the degree of the polynomial),
rounded down. Every printed coefficient is positive, so every b_k is positive, and by [[lem:bernstein-lower-bound]] the
polynomial is at least min_k b_k > 0 on the piece. The pieces of each item cover its interval.

The sign and the monotonicity. Ψ > 0 on [−1, 1] (item 1), so F has the sign of z. F_z ≥ 0 on [−1, 1] (item 2), so
φ′ = 4ηF_z ≥ 0 and φ is nondecreasing, with φ(∞) = F(1) = Ψ(1) and φ(−∞) = F(−1) = −Ψ(−1). As F is a polynomial in y,
φ′, φ″ and φ‴ are η times polynomials in y and y^(1/2); they are O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence
integrable and vanishing at ±∞.

Positivity of the weight. By [[lem:band-weight-z]], w_l = ηG_l with G_l the weight polynomial for a = κ + 3/4, and at
l = l_1 this is the polynomial G_(l_1) listed in [[sec:tb2-polynomial-multipliers]] (expanding [[eq:band-weight-z]] with
F = zΨ gives its coefficients). G_(l_1) ≥ 0 on [−1, 1] (item 3), and since F has the sign of z,
G_l ≥ G_(l_1) for l ≥ l_1 by [[lem:band-weight-z]]. So w_l ≥ w_(l_1) ≥ 0 on ℝ.

The constants on I. On I, v ∈ [1/4, 5/6], η = (1 − v²)v³ and z = 1 − 2v², so w_(l_1) − w_* and φ′ − m_*, m^* − φ′ are
the polynomials in v of items 4, 5 and 6. Their positivity gives min_I w_l ≥ min_I w_(l_1) ≥ w_* and
m_* ≤ φ′ ≤ m^* on I. Since F increases with z, on I it takes values in [F(−7/18), F(7/8)], so max_I |φ| = p_I; and
max(|φ(∞)|, |φ(−∞)|) = max(Ψ(1), Ψ(−1)) = p_∞. [[lem:band-sharp]] gives the bound. ∎

### The algebraic multipliers for 14 ≤ |σ| ≤ 384 {#sec:band-algebraic}

Let Φ(x) := x(1 + x²)^(−1/2), so that Φ′ = (1 + x²)^(−3/2), Φ″ = −3x(1 + x²)^(−5/2) and Φ‴ = (12x² − 3)(1 + x²)^(−7/2).
For ν > 0 put F_ν(z) := Φ(νz), x := νz and s := 1 + x². Φ is odd and increasing with |Φ| < 1.

**Lemma {#lem:band-algebraic-weight}** (The weight of F_ν.) For V = V_(a,9/4) the weight of F_ν is w = ηG with

    G = 2s^(−7/2)((a/ν)x²s³ + R_ν(x)),
    R_ν(x) := (9/16)(1 − z)(1 + 3z)xs³ + ν(1 − z)(1 − 2z − 5z²)s² − (9/4)ν²(1 + z)(1 − z)²(1 + 5z)xs
              + (ν³/2)(3 − 12x²)(1 + z)²(1 − z)³,     z = x/ν.                                       {#eq:band-r}

Expanding in powers of x,

    R_ν(x) = ν³(3/2 − 6x²) + (15/4)ν²(x³ − x) + ν(4x⁴ − 10x² + 1) + (1/16)(9x⁷ + 3x⁵ + 195x³ − 39x)
             + (1/(8ν))(9x⁸ + 27x⁶ + 63x⁴ − 15x²)
             − (1/(16ν²))(27x⁹ + 85x⁷ + 125x⁵ − 53x³).                                           {#eq:band-r-expanded}

*Proof.* F_z = νΦ′(x) = νs^(−3/2), F_zz = ν²Φ″(x) = −3ν²xs^(−5/2) and F_zzz = ν³(12x² − 3)s^(−7/2). Substituting
these, F = xs^(−1/2) and V_y = (a/ν)x + (9/16)(1 − z)(1 + 3z) into [[eq:band-weight-z]] and multiplying by s^(7/2),

    Gs^(7/2) = 2xs³V_y − ½νΞ_zz s² + (9/2)ν²xΞ_z s − ν³(12x² − 3)Ξ.

With the formulas for Ξ, Ξ_z and Ξ_zz of [[eq:band-weight-z]], the term 2xs³ · (a/ν)x is 2(a/ν)x²s³ and the remaining
terms are 2R_ν(x). Substituting z = x/ν into [[eq:band-r]] and collecting powers of x gives [[eq:band-r-expanded]]. ∎

**Lemma {#lem:band-positivity}** (Positivity of the core polynomial.) Let 2 ≤ ν ≤ 12 and A_ν := 6ν⁴ + (17/2)ν³. Then

    R_ν(x) + (A_ν/ν)x²(1 + x²)³ ≥ ν³     for every real x with |x| ≤ ν.                    {#eq:band-positivity}

*Proof.* Put μ := 1/ν ∈ [1/12, 1/2] and 𝒬 := ν⁻³(R_ν(x) + (A_ν/ν)x²(1 + x²)³) − 1. Since A_ν/ν = (6 + 17μ/2)ν³,
[[eq:band-r-expanded]] gives 𝒬 = e_0 + μe_1 + μ²e_2 + μ³e_3 + μ⁴e_4 + μ⁵e_5 with

    e_0 = 1/2 + 18x⁴ + 18x⁶ + 6x⁸,            e_1 = −(15/4)x + (17/2)x² + (15/4)x³ + (51/2)(x⁴ + x⁶) + (17/2)x⁸,
    e_2 = 1 − 10x² + 4x⁴,                      e_3 = (1/16)(−39x + 195x³ + 3x⁵ + 9x⁷),
    e_4 = (1/8)(−15x² + 63x⁴ + 27x⁶ + 9x⁸),    e_5 = (1/16)(53x³ − 125x⁵ − 85x⁷ − 27x⁹);

here e_0 = 3/2 − 6x² + 6x²(1 + x²)³ − 1 and e_1 = (15/4)(x³ − x) + (17/2)x²(1 + x²)³.

Case 0 ≤ x ≤ 1. Dropping nonnegative terms, e_0 ≥ 1/2 + 18x⁴, e_1 ≥ −(15/4)x + (17/2)x², e_2 ≥ 1 − 10x²,
e_3 ≥ −(39/16)x and e_4 ≥ −(15/8)x². As x ≤ 1, 125x⁵ + 85x⁷ + 27x⁹ − 53x³ ≤ 184x³ ≤ 184x², so e_5 ≥ −(23/2)x². Hence

    𝒬 ≥ 1/2 + μ² − β_1x + β_2x² + 18x⁴,
    β_1 := (15/4)μ + (39/16)μ³,     β_2 := (17/2)μ − 10μ² − (15/8)μ⁴ − (23/2)μ⁵.

β_1 increases with μ, so β_1 ≤ β_1(1/2) = 279/128. β_2 is concave in μ ≥ 0, so on [1/12, 1/2] it is at least
min(β_2(1/12), β_2(1/2)) = min(0.63875…, 1.2734…) > 0.6387. And 18x⁴ ≥ (9/4)x² − 9/128, since 18(x² − 1/16)² ≥ 0. So
𝒬 ≥ γ_0 − (279/128)x + γ_2x² with γ_0 := 1/2 + 1/144 − 9/128 > 0.4366 and γ_2 := 0.6387 + 9/4 = 2.8887. This quadratic
has positive leading coefficient and discriminant (279/128)² − 4γ_0γ_2 < 4.7512 − 5.0448 < 0, so 𝒬 > 0.

Case −1 ≤ x < 0. Put ξ := −x ∈ (0, 1]. Then e_0 ≥ 1/2, e_1 = (15/4)ξ(1 − ξ²) + (17/2)ξ² + (51/2)(ξ⁴ + ξ⁶) +
(17/2)ξ⁸ ≥ (17/2)ξ², e_2 ≥ 1 − 10ξ², e_3 = (ξ/16)(39 − 195ξ² − 3ξ⁴ − 9ξ⁶) ≥ −(207/16)ξ³ ≥ −(207/16)ξ²,
e_4 ≥ −(15/8)ξ² and e_5 = (ξ³/16)(−53 + 125ξ² + 85ξ⁴ + 27ξ⁶) ≥ −(53/16)ξ². Hence 𝒬 ≥ 1/2 + μ² − β_3ξ², with
β_3 := 10μ² + (207/16)μ³ + (15/8)μ⁴ + (53/16)μ⁵ − (17/2)μ. β_3 is convex in μ ≥ 0, so on [1/12, 1/2] it is at most
max(β_3(1/12), β_3(1/2)) = β_3(1/2) = 45/512, as β_3(1/12) < 0. As μ² ≥ 0 and ξ² ≤ 1,
𝒬 ≥ 1/2 − max(β_3, 0)ξ² ≥ 1/2 − 45/512 > 0.

Case 1 ≤ |x| ≤ ν. Here x² ≥ 1, μ ≤ 1/2 and μ|x| ≤ 1. First e_1 ≥ 0: for x ≥ 1, (15/4)(x³ − x) ≥ 0 and the other terms
are nonnegative; for x ≤ −1, with ξ = −x, e_1 ≥ (17/2)ξ² + (51/2)ξ⁴ − (15/4)ξ³ ≥ 0, as ξ³ ≤ (ξ² + ξ⁴)/2. Next, using
μ|x| ≤ 1 to trade a power of μ for a power of |x|, and μ ≤ 1/2,

    μ²e_2 ≥ −10μ²x² ≥ −(5/2)x²,                        μ⁴e_4 ≥ −(15/8)μ⁴x² ≥ −(15/128)x²,
    μ³|e_3| ≤ (μ²/16)(39 + 195x² + 3x⁴ + 9x⁶) ≤ (1/64)(39 + 195x² + 3x⁴ + 9x⁶),
    μ⁵|e_5| ≤ (μ⁴/16)(53x² + 125x⁴ + 85x⁶ + 27x⁸) ≤ (1/256)(53x² + 125x⁴ + 85x⁶ + 27x⁸).

Adding these to e_0,

    𝒬 ≥ 1/2 − 39/64 − (1503/256)x² + (18 − 137/256)x⁴ + (18 − 121/256)x⁶ + (6 − 27/256)x⁸ ≥ −7/64 − 6x² + 17x⁴,

and −7/64 − 6x² + 17x⁴ ≥ −7/64 + 11x² > 0 since x⁴ ≥ x². In every case 𝒬 > 0, which is [[eq:band-positivity]]. ∎

**Lemma {#lem:band-algebraic-constants}** (The algebraic multiplier on I.) Let 2 ≤ ν ≤ 12, let a ≥ A_ν + (7/2)ν⁴ and
put α := (a − A_ν)/ν ≥ (7/2)ν³. Then φ := F_ν(z(r_*)) satisfies the hypotheses of [[lem:band-sharp]] for
V = V_(a,9/4), with

    m′ = (15ν/256)(1 + 49ν²/64)^(−3/2),   M′ ≤ 0.74362ν,   p_I = Φ(7ν/8),   p_∞ = Φ(ν),

and, for every τ ∈ (0, 7/8), with h_ν(z) := ηz²(1 + ν²z²)^(−1/2) and η = 2^(−5/2)(1 + z)(1 − z)^(3/2),

    w_I ≥ min{2ν³ min(η(τ), 1375/7776), 2αν² min(h_ν(τ), h_ν(7/8))},   h_ν(7/8) = (735/65536)(1 + 49ν²/64)^(−1/2).
                                                                                                  {#eq:band-wi}

*Proof.* The hypotheses. φ′ = 4ηF_z = 4νηΦ′(νz) > 0 ([[lem:band-weight-z]]), so φ increases, from −Φ(ν) at −∞ to
Φ(ν) at ∞. F_ν is a smooth function of y on [0, 1], so φ′, φ″ and φ‴ are η times bounded functions of y; they are
O(r⁻³) as r → ∞ and O(e^(2r_*)) as r_* → −∞, hence integrable and vanishing at ±∞.

The weight. Since a/ν = A_ν/ν + α, [[lem:band-algebraic-weight]] and [[lem:band-positivity]] give, on ℝ,

    w = 2ηs^(−7/2)(αx²s³ + (A_ν/ν)x²s³ + R_ν(x)) ≥ 2ηk(x²),   k(u) := αu(1 + u)^(−1/2) + ν³(1 + u)^(−7/2),

as |x| = ν|z| ≤ ν. So w > 0 on ℝ. Moreover k′(u) = (1 + u)^(−9/2)(α(1 + u)³(1 + u/2) − (7/2)ν³) ≥ 0 because
α ≥ (7/2)ν³, so k ≥ k(0) = ν³; and k ≥ αu(1 + u)^(−1/2). Hence w ≥ 2η max(ν³, αν²z²(1 + ν²z²)^(−1/2)).

The weight on I. As a function of z, η increases on [−1, −1/5] and decreases on [−1/5, 1], since η increases with y
on [0, 3/5] and decreases on [3/5, 1] ([[sec:morawetz-identity]]). So on [−7/18, τ], η ≥ min(η(−7/18), η(τ)), and
η(−7/18) = η(y = 25/36) = 1375/7776; there w ≥ 2ν³ min(η(τ), 1375/7776). On [τ, 7/8], w ≥ 2αν²h_ν(z), and h_ν is
log-concave on (0, 1):

    (log h_ν)″ = −1/(1 + z)² − 3/(2(1 − z)²) − 2/z² + ν²(ζ − 1)/(1 + ζ)²,     ζ := ν²z²,

and ν²(ζ − 1)/(1 + ζ)² = z⁻²ζ(ζ − 1)/(1 + ζ)² < z⁻², so (log h_ν)″ < −z⁻² < 0. So on [τ, 7/8], h_ν ≥ min(h_ν(τ),
h_ν(7/8)). At z = 7/8, η = η(y = 1/16) = 15/1024 and z² = 49/64, which gives h_ν(7/8). This is [[eq:band-wi]].

The constants. φ′ = 4νη(1 + ν²z²)^(−3/2). On y ∈ [1/16, 1/2] (z ∈ [0, 7/8]),
d(log φ′)/dy = 3/(2y) − 1/(1 − y) + 6ν²z/(1 + ν²z²) ≥ 3 − 2 > 0, so there
φ′ ≥ φ′(y = 1/16) = 4ν(15/1024)(1 + 49ν²/64)^(−3/2).
On y ∈ [1/2, 25/36], η ≥ 2^(−5/2) ([[sec:morawetz-identity]]) and |z| ≤ 7/18, so φ′ ≥ 4ν2^(−5/2)(1 + 49ν²/324)^(−3/2),
which is larger, as 4 · 2^(−5/2) > 15/256 and 49/324 < 49/64. This gives m′. Next φ′ ≤ 4ν max η = 4ν · 6√15/125 <
0.74362ν (as in [[prop:morawetz-resolvent-l-ge-1]]). Since Φ is odd and increasing, max_I |φ| = max(Φ(7ν/8), Φ(7ν/18))
= Φ(7ν/8), and |φ(±∞)| = Φ(ν). ∎

### The band {#sec:band-theorem}

**Theorem {#thm:band}** (The resolvent on the band.) For every harmonic l ≥ 0 and every real σ with 3 ≤ |σ| ≤ 384,

    ‖χ_I R_l(σ) χ_I‖ ≤ 11.477.

*Proof.* All bounds used are even in σ, so let 3 ≤ σ ≤ 384. We cover [3, 384] by six ranges. In each, one multiplier
serves every harmonic from some l_1 on, and [[lem:band-barrier]] serves the harmonics below l_1. B♯ increases with σ
([[lem:band-sharp]]) and the barrier bound decreases, so on a range [σ_a, σ_b] it suffices to evaluate B♯ at σ_b and
the barrier bound at σ_a.

(a) 3 ≤ σ ≤ 15/4, the multiplier zΨ_5 of [[prop:band-polynomial]], l_1 = 5. With the constants of
[[sec:tb2-polynomial-multipliers]] (w_* = 0.87, m_* = 0.0455, m^* = 0.75, p_I < 0.99673, p_∞ = 43/40), B♯(15/4) < 10.51.
For l ≤ 4, κ ≤ 24 and the barrier bound at σ = 3 is 3.7436 · 3/(9 − 313/48) < 4.531.

(b) 15/4 ≤ σ ≤ 6, the multiplier zΨ_7, l_1 = 7. B♯(6) < 9.261 (w_* = 1.30, m_* = 0.031, m^* = 0.74, p_I < 0.83442,
p_∞ = 9/10). For l ≤ 6, κ ≤ 48 and the barrier bound at σ = 15/4 is 3.7436 · (15/4)/(225/16 − 601/48) < 9.107.

(c) 6 ≤ σ ≤ 14, the multiplier zΨ_11, l_1 = 11. B♯(14) < 9.544 (w_* = 1.80, m_* = 0.0210, m^* = 0.72, p_I < 0.50776,
p_∞ = 59/100). For l ≤ 10, κ ≤ 120 and the barrier bound at σ = 6 is 3.7436 · 6/(36 − 1465/48) < 4.100.

(d)–(f) 14 ≤ σ ≤ 384, the algebraic multipliers F_ν of [[lem:band-algebraic-constants]] with ν = 11/4 on [14, 28],
ν = 4 on [28, 108] and ν = 6 on [108, 384]. For σ in a range [σ_a, σ_b], let l_1(σ) be the least l with
κ/4 + 25/48 > σ² − σ/2. For l < l_1(σ), [[lem:band-barrier]] gives the bound 2Λ < 7.4872. For l ≥ l_1(σ),
κ > 4σ² − 2σ − 25/12, so a = κ + 3/4 > 4σ² − 2σ − 4/3 ≥ a_* := 4σ_a² − 2σ_a − 4/3, as 4σ² − 2σ increases for σ ≥ 1/4.
The rows of [[sec:tb2-algebraic-rows]] show a_* ≥ A_ν + (7/2)ν⁴ in each range, so [[lem:band-algebraic-constants]]
applies to every such l, with α ≥ (a_* − A_ν)/ν (the lower bound [[eq:band-wi]] increases with α). With the τ and the
constants listed there, B♯(σ_b) is less than 10.297, 10.579 and 10.381 in the three ranges.

So for every l ≥ 0 and 3 ≤ |σ| ≤ 384 the norm is at most
max(10.51, 9.261, 9.544, 10.297, 10.579, 10.381, 4.531, 9.107, 4.100, 7.4872) = 10.579 < 11.477. ∎

The six ranges, with the bound for the harmonics served by each multiplier and for those below it:

| range of σ | multiplier | harmonics it serves | multiplier bound ≤ | harmonics below: bound ≤ |
|---|---|---|---|---|
| [3, 15/4] | zΨ_5 | l ≥ 5 | 10.51 | 4.531 |
| [15/4, 6] | zΨ_7 | l ≥ 7 | 9.261 | 9.107 |
| [6, 14] | zΨ_11 | l ≥ 11 | 9.544 | 4.100 |
| [14, 28] | F_(11/4) | l ≥ l_1(σ) | 10.297 | 7.4872 |
| [28, 108] | F_4 | l ≥ l_1(σ) | 10.579 | 7.4872 |
| [108, 384] | F_6 | l ≥ l_1(σ) | 10.381 | 7.4872 |

Together with [[prop:morawetz-resolvent-l-ge-1]] and [[prop:morawetz-l-zero]], which bound every harmonic for
0 < |σ| ≤ 3, this bounds ‖χ_I R_l(σ) χ_I‖ uniformly in l for every real 0 < |σ| ≤ 384.

**Proposition {#prop:band-points}** (Sampled frequencies.) For every harmonic l ≥ 0, ‖χ_I R_l(σ) χ_I‖ is at most
8.878, 4.682, 5.990, 4.097, 3.022 and 2.252 at |σ| = 3, 6, 12, 24, 48 and 96; at most 2.024, 1.869 and 1.743 at
|σ| = 128, 160 and 192; and at most 1.677, 1.815 and 1.963 for every |σ| in [s − 1/20, s] with s = 256, 320 and 384.

*Proof.* At |σ| = 3, [[prop:band-polynomial]] with zΨ_5 gives B♯(3) < 8.878 for l ≥ 5, and [[lem:band-barrier]] gives
4.531 for l ≤ 4. At |σ| = 6, zΨ_11 gives B♯(6) < 4.682 for l ≥ 11 and [[lem:band-barrier]] gives 4.100 for l ≤ 10. At
the other frequencies, take the row of [[sec:tb2-points]]: the multiplier F_ν of [[lem:band-algebraic-constants]] with
the listed ν and τ, applied with a at l = l_1 (a larger a only increases α), serves every l ≥ l_1, and gives the listed
B♯ at the right end σ_+; [[lem:band-barrier]] at the left end σ_- gives the listed bound for every l < l_1. ∎

**Remark {#rem:band-observed}** (Numerical observation.) A numerical optimisation over multipliers that are narrow at
the photon sphere and wide in the flanks, one multiplier for each l_1 = 5, …, 768, with the bound evaluated in interval
arithmetic on the 7,620 subintervals of width 1/20 of [3, 384], gives for every l ≥ 0 the bounds 3.7719, 2.3724,
1.5222 and 0.99697 at |σ| = 12, 24, 48 and 96, and 0.83951, 0.73083, 0.66429, 0.56257, 0.49119 and 0.47635 on the
subintervals ending at |σ| = 128, 160, 192, 256, 320 and 384 (0.43792 at 384 when more multipliers are admitted); its
largest value on [3, 384] is 11.477, on [3.2, 3.25]. |σ|^(1/2) times these values is 9.77, 9.20 and 8.58 at
|σ| = 96, 192 and 384 (the last with 0.43792), so between |σ| = 96 and 384 they decay roughly like |σ|^(−0.6); the
scaling of the best multiplier at the trapped harmonic suggests |σ|^(−1/2) for larger |σ|. These values are not proved
here ([[prop:band-points]] proves weaker ones from |σ| = 12 on), and no proof uses them.

### One derivative on the band {#sec:band-one-derivative}

**Corollary {#cor:band-one-derivative}** (The one-derivative constants on the band.) Let 3 ≤ |σ| ≤ 384. For f ∈ L²(ℝ)
vanishing off I and u = R_l(σ)f,

    ‖u′‖_I ≤ 283.06‖f‖ for every l ≥ 1,        ‖u′‖_I ≤ 305.31‖f‖ for l = 0;

in particular ‖u′‖_I ≤ 963.4‖f‖ for l ≥ 1 and ≤ 1516‖f‖ for l = 0. For f ∈ L²(I × 𝕊³), extended by zero to
ℝ × 𝕊³, with harmonic components f_l (the components of f in the eigenspaces of the Laplacian of 𝕊³ with eigenvalue
−κ, which are orthogonal), put u_l := R_l(σ)f_l, acting in r_*, and u := Σ_l u_l; by [[thm:band]] and the first bound
the series and its r_*-derivative converge in L² on I × 𝕊³. Then, with the norms taken on I × 𝕊³, ψ = 2ηz² the weight
of [[prop:morawetz-weight]] and the angular term at l = 1 taken unweighted,

    ‖∂_(r_*)u‖_I² + Σ_l κ∫_I ψ|u_l|² ≤ C²‖f‖²,     C ≤ 308.46.

*Proof.* By [[thm:band]], B̃ := 11.477 bounds ‖u‖_I/‖f‖ for every l. [[lem:morawetz-identity]] then gives ‖u′‖_I ≤
X(B̃)‖f‖ with X(B̃) = (1 + (1 + 2m′(M′ + 2|σ|)B̃)^(1/2))/(2m′), where (m′, M′) = (15/256, 0.74362) for l ≥ 1, the
constants of φ = 1 − 2/r² and q = 0 ([[prop:morawetz-resolvent-l-ge-1]]), and (m′, M′) = (3315/65536, 0.3999) at
l = 0, those of φ = 1 − 2/r² and q = ½η(1 + 3y/2) ([[prop:morawetz-l-zero]]). X(B̃) increases with |σ|, so its value
at |σ| = 384 bounds the band: for l ≥ 1,
2m′(M′ + 768)B̃ = (15/128)(768.74362)(11.477) < 1033.94, whose increment by 1 has square root less than 32.171, so
X < (1 + 32.171)/(15/128) < 283.06; at l = 0, 2m′(M′ + 768)B̃ = (3315/32768)(768.3999)(11.477) < 892.18, whose
increment by 1 has square root less than 29.8862, so X_0 < (1 + 29.8862)(32768/3315) < 305.31.

For the sum, [[cor:morawetz-one-derivative]] (a) with B_l replaced by B̃ gives, for l ≥ 2,
κ∫_I ψ|u_l|² ≤ (κ/(κ − 3))J‖f_l‖², J := 2X(B̃) + (M′ + 2|σ|)B̃ < 566.12 + 8822.88 < 9389.0, and κ/(κ − 3) ≤ 8/5 as
κ ≥ 8. So for l ≥ 2 the harmonic contributes at most (283.06² + (8/5)(9389.0))‖f_l‖² < 308.46²‖f_l‖²; for l = 1 at
most (283.06² + 3B̃²)‖f_1‖² < 283.76²‖f_1‖²; and for l = 0 at most 305.31²‖f_0‖². Summing over l, with
‖∂_(r_*)u‖_I² = Σ_l‖u_l′‖_I² and ‖f‖² = Σ_l‖f_l‖² by the orthogonality of the harmonics, gives C ≤ 308.46. ∎
