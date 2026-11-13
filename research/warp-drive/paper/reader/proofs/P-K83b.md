<!-- Closes three open items of chapter 83 (ch:localised-data).
Part 1 closes computational-1: the tensor charge identity on every round slice of a Tangherlini region. Block 1.1 is
inserted after lem:loc-harmonics, before thm:loc-tensor. Block 1.2 replaces "(iii) [[pending:computational-1]]" in
the proof of thm:loc-tensor (chapter line 493). The statement of thm:loc-tensor is unchanged.
Part 2 closes computational-2: the scalar modes on the static slice. Block 2.1 replaces lem:loc-scalar-reduction, its
statement and its proof (chapter lines 594-619); it keeps the labels eq:loc-ek and eq:loc-ev and the formulas the rest
of the chapter cites, and adds the formulas the proof uses. Block 2.2 replaces, in the proof of thm:loc-outside, the
parenthesis "(orthogonality of the class harmonics of different type and degree, [[lem:loc-harmonics]], the mode sums
converging for smooth data)" by "([[lem:loc-scalar-reduction]])".
Part 3 closes the scope gap: Gamma > 0 on the whole of region III. Block 3.1 is a new proposition, inserted in
sec:bg-seed after prop:bg-seed. Blocks 3.2-3.6 replace the statements that used the seed region in place of region III:
cor:loc-charge-seed, thm:charge-sign (a), the last sentence of the first paragraph of sec:loc-setting, and the
endpoint printed in thm:bg-margins (b). -->

<!-- Part 1. Block 1.1: after lem:loc-harmonics, before thm:loc-tensor. -->

**Lemma {#lem:loc-tt-second}** (The second variation of the scalar curvature of S³.) Let T be a smooth transverse
trace-free symmetric 2-tensor on the unit S³ with Δ̂T = −k_T²T, and put D²Scal_γ̂[T, T] := d²/dε² Scal(γ̂ + εT) at
ε = 0. Then

    ∫_(S³) D²Scal_γ̂[T, T] dvol_γ̂ = (1 − k_T²/2) ∫_(S³) |T|²_γ̂ dvol_γ̂.                                {#eq:loc-tt-second}

*Proof.* For a family g + εh of metrics on a closed manifold, the Levi-Civita connection varies by δΓ^k_ij =
½(∇_ih_j^k + ∇_jh_i^k − ∇^kh_ij), and Palatini's identity Ric′[h]_ij = ∇_kδΓ^k_ij − ∇_jδΓ^k_ki gives

    Ric′[h]_ij = ½(∇^k∇_ih_jk + ∇^k∇_jh_ik − ∇^k∇_kh_ij − ∇_i∇_j tr h),

whose trace gives the first variation DScal[h] = div div h − Δ tr h − ⟨h, Ric⟩ of the scalar curvature. Integrating,
the divergences drop out and

    d/dε ∫ Scal(g_ε) dvol_(g_ε) = ∫ (DScal_(g_ε)[h] + ½ Scal(g_ε) tr_(g_ε) h) dvol_(g_ε) = ∫ ⟨𝒢(g_ε), h⟩_(g_ε) dvol_(g_ε),

g_ε := g + εh, 𝒢(g) := ½ Scal(g) g − Ric(g). Take g = γ̂ and h = T, and let E(ε) := ∫ Scal(γ̂ + εT) dvol_(γ̂+εT); all
integrals below are over S³ against dvol_γ̂, and |T|² := |T|²_γ̂. Since Ric(γ̂) = 2γ̂ and Scal(γ̂) = 6, 𝒢(γ̂) = γ̂ and
DScal[T] = −⟨T, Ric(γ̂)⟩ = −2 tr T = 0. The Riemann tensor of the unit S³ is γ̂_ikγ̂_jl − γ̂_ilγ̂_jk, and the Ricci
identity gives, for trace-free T, ∇^k∇_iT_jk = ∇_i∇^kT_jk + 3T_ij = 3T_ij; so Ric′[T] = ½(6T − Δ̂T) = ½(6 + k_T²)T.
Differentiating E′(ε) = ∫⟨𝒢(γ̂ + εT), T⟩_(γ̂+εT) dvol_(γ̂+εT) at ε = 0, the derivative of 𝒢 is ½DScal[T]γ̂ + ½Scal(γ̂)T −
Ric′[T] = −(k_T²/2)T, the two inverse metrics in ⟨γ̂, T⟩ contribute −2|T|², and the variation ½ tr T dvol_γ̂ of the
volume contributes ½⟨γ̂, T⟩ tr T = 0; so E″(0) = −(k_T²/2 + 2)∫|T|². On the other hand

    dvol_(γ̂+εT) = (1 + ½ε tr T + ε²(⅛(tr T)² − ¼|T|²) + O(ε³)) dvol_γ̂ = (1 − ¼ε²|T|² + O(ε³)) dvol_γ̂

and Scal(γ̂ + εT) = 6 + ½ε² D²Scal_γ̂[T, T] + O(ε³), so E″(0) = ∫ D²Scal_γ̂[T, T] − 3∫|T|². Comparing the two values of
E″(0) gives [[eq:loc-tt-second]]. ∎

**Lemma {#lem:loc-tensor-variations}** (Second variations for tensor data on a round slice.) Let γ = G dR² + R²γ̂ and
K0 = κ0 G dR² + Y0 R² γ̂ be round data on a band, with G > 0, κ0 and Y0 smooth functions of R. Let T be as in
[[lem:loc-tt-second]], H and Π smooth functions of R, h := 2R²H T and k := R²(Π + 2Y0H) T. For a function X of the
data write [X]_2 for the ε² coefficient of X(γ + εh, K0 + εk), write ′ := d/dR, and let |T|² := |T|²_γ̂, a function on
S³. Then, with ℳ_R := ℳ(∂_R) the radial component of the momentum constraint,

    [(tr K)² − |K|²]_2 = −(Π² + 4(κ0 + 2Y0)HΠ) |T|²,
    [ℳ_R]_2 = (2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′) |T|²,
    ∫_(S³) [Scal]_2 dvol_γ̂ = ((2 − k_T²)H²/R² + (16HH′/R − H′²)/G + 4G^(−1/2)(G^(−1/2)HH′)′) ∫_(S³) |T|² dvol_γ̂.
                                                                                             {#eq:loc-tensor-variations}

*Proof.* Let T^♯ be the endomorphism of the tangent spaces of the spheres with γ̂(T^♯X, Z) = T(X, Z); then tr T^♯ = 0
and tr (T^♯)² = |T|². The tensors h and k have no radial components, and on the spheres γ⁻¹h = 2HT^♯ and γ⁻¹k = (Π +
2Y0H)T^♯. Let A_ε := (γ + εh)⁻¹(K0 + εk), as an endomorphism. It is κ0 on ∂_R, and on the spheres, since (1 + 2εHT^♯)⁻¹
= 1 − 2εHT^♯ + 4ε²H²(T^♯)² + O(ε³),

    A_ε = Y0 + εΠT^♯ − 2ε²HΠ(T^♯)² + O(ε³).

So tr A_ε = κ0 + 3Y0 − 2ε²HΠ|T|² + O(ε³) and tr A_ε² = κ0² + 3Y0² + ε²(Π² − 4Y0HΠ)|T|² + O(ε³), the terms of order ε
vanishing with tr T^♯. Since (tr K)² − |K|² = (tr A_ε)² − tr A_ε², this gives the first identity.

For the second, let γ = G dR² + g with g = g(R) a family of metrics on S³, and K with K(∂_R, ∂_A) = 0, K(∂_R, ∂_R) =
κG for a function κ of R, and spherical part 𝒦. The Christoffel symbols Γ^R_RR = G′/(2G), Γ^R_AB = −g′_AB/(2G),
Γ^A_RB = ½(g⁻¹g′)^A_B and Γ^A_RR = Γ^R_RA = 0 give (div K)_R = κ′ + ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′g⁻¹𝒦), and tr K = κ +
tr(g⁻¹𝒦), so that

    ℳ_R = ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′ g⁻¹𝒦) − (tr g⁻¹𝒦)′.

Along the family, g = R²(γ̂ + 2εHT), g⁻¹g′ = 2/R + 2εH′T^♯ − 4ε²HH′(T^♯)² + O(ε³), and g⁻¹𝒦 is A_ε on the spheres. The
ε² coefficients of the three terms are −2κ0HH′|T|², −½(−4HΠ/R + 2H′Π − 4Y0HH′)|T|² and 2(HΠ)′|T|², whose sum is the
second identity.

For the third, consider a metric G dR² + R²ĝ with ĝ = ĝ(R) a family of metrics on S³. The lapse G^(1/2) of its
foliation by the spheres {R = const} is constant on each sphere, so the Gauss equation and the Riccati equation of the
foliation give

    Scal = R⁻² Scal(ĝ) − (tr L)² − |L|² − 2G^(−1/2)(tr L)′,      L := ½G^(−1/2) ∂_R(R²ĝ),

L the second fundamental form of the spheres with respect to the unit normal G^(−1/2)∂_R. For ĝ = γ̂ + 2εHT, as an
endomorphism L = G^(−1/2)(1/R + εH′T^♯ − 2ε²HH′(T^♯)²) + O(ε³), so that tr L = G^(−1/2)(3/R − 2ε²HH′|T|²) + O(ε³) and
|L|² = G⁻¹(3/R² + ε²(H′² − 4HH′/R)|T|²) + O(ε³). The ε² coefficients of the last three terms of Scal are therefore
12HH′|T|²/(RG), −(H′² − 4HH′/R)|T|²/G and 4G^(−1/2)(G^(−1/2)HH′)′|T|². The ε² coefficient of the first term is R⁻²
times half of D²Scal_γ̂[2HT, 2HT] = 4H²D²Scal_γ̂[T, T], whose integral over S³ is, by [[lem:loc-tt-second]],
R⁻²(2 − k_T²)H²∫|T|². Adding gives the third identity. ∎

<!-- Part 1. Block 1.2: replaces "(iii) [[pending:computational-1]]" in the proof of thm:loc-tensor. -->

(iii) By [[lem:racz-split-formulas]] (b), K^l_l = 3n^R/R = 3Y0, so n^R = RY0 and δ = (h, k) is the variation of
[[lem:loc-tensor-variations]]. In [[eq:loc-charge]], D² = 2[ ]_2, Y_s·ℳ = Y_s^R ℳ_R and dvol = √G R³ dR dvol_γ̂, and
∫_(S³) |T|²_γ̂ dvol_γ̂ = (2π)²|T|². So [[eq:loc-tensor-variations]] and G⁻¹ = N_s² ((ii)) give, with ′ := d/dR,

    Q(δ) = (2π)²|T|² ∫ R³√G (N_s 𝔥 + 2Y_s^R 𝔪) dR,
    𝔥 := (2 − k_T²)H²/R² + N_s²(16HH′/R − H′²) + 4N_s(N_sHH′)′ − 4(κ0 + 2Y0)HΠ − Π²,
    𝔪 := 2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′.                                             {#eq:loc-tensor-density}

Since ξ is a Killing field, for X, Z tangent to Σ, 0 = g(∇_Xξ, Z) + g(∇_Zξ, X) = 2N_sK0(X, Z) + (L_(Y_s)γ)(X, Z),
because g(∇_X(N_sn), Z) = N_sK0(X, Z) and the tangential part of ∇_XY_s is D_XY_s. The components of this equation
on the spheres and on ∂_R are 2RY_s^R = −2N_sY0R² and Y_s^R G′ + 2G(Y_s^R)′ = −2N_sκ0G. With y_s := Y_s^R/N_s =
√G Y_s^R they read

    Y0 = −y_s/R,        κ0 = −y_s′,                                                             {#eq:loc-tensor-kid}

and (ii) reads N_s² − y_s² = f. Now collect the integrand of [[eq:loc-tensor-density]], using N_s√G = 1 and √G Y_s^R
= y_s. The terms in Π², ΠH′ and H′² are −R³Π², −2R³y_sΠH′ and −R³N_s²H′². The terms in HΠ and HΠ′ are

    −4R³(κ0 + 2Y0)HΠ + 4R²y_sHΠ + 4R³y_s(HΠ)′ = (4R³y_sHΠ)′ − 4R³(κ0 + y_s′ + 2Y0 + 2y_s/R)HΠ = (4R³y_sHΠ)′,

by [[eq:loc-tensor-kid]]. Writing 4R³N_s(N_sHH′)′ = (4R³N_s²HH′)′ − 4N_s(R³N_s)′HH′, the terms in H², HH′ and HH″ are

    (2 − k_T²)RH² + (16R²N_s² − 4N_s(R³N_s)′ + 4R³y_s(Y0 − κ0))HH′ + (4R³N_s²HH′)′,

and by [[eq:loc-tensor-kid]] the coefficient of HH′ is 4R²(N_s² − y_s²) − 2R³(N_s² − y_s²)′ = 4R²f − 2R³f′ = 4R² − 8μ,
since f = 1 − μ/R². With (4R² − 8μ)HH′ = ((2R² − 4μ)H²)′ − 4RH², these terms are −(k_T² + 2)RH² + (4R³N_s²HH′ +
(2R² − 4μ)H²)′. Altogether

    R³√G (N_s 𝔥 + 2Y_s^R 𝔪) = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH² + 𝔅_T′,
    𝔅_T := 4R³N_s²HH′ + 4R³y_sHΠ + 2(R² − 2μ)H².                                            {#eq:loc-tensor-flux}

On the other hand, ξ(H) = N_sΠ + Y_s^RH′, |dH|² = −Π² + N_s²H′² and g(ξ, n) = −N_s give

    −2T_m(ξ, n)√G = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH².

Since 𝔅_T has compact support in (R1, R2), integrating [[eq:loc-tensor-flux]] in R gives [[eq:loc-tensor-charge]].
