<!-- Closes three open items of chapter 83 (ch:localised-data).
Part 1 closes computational-1: the tensor charge identity on every round slice of a Tangherlini region. Block 1.1 is
inserted after lem:loc-harmonics, before thm:loc-tensor. Block 1.2 replaces item (iii) of the proof of thm:loc-tensor
(chapter line 493, the marker computational-1). The statement of thm:loc-tensor is unchanged.
Part 2 closes computational-2: the scalar modes on the static slice. Block 2.1 replaces lem:loc-scalar-reduction, its
statement and its proof (chapter lines 594-619); it keeps the labels eq:loc-ek and eq:loc-ev and the formulas the rest
of the chapter cites, and adds the formulas the proof uses. Block 2.2 replaces, in the proof of thm:loc-outside, the
parenthesis "(orthogonality of the class harmonics of different type and degree, [[lem:loc-harmonics]], the mode sums
converging for smooth data)" by "([[lem:loc-scalar-reduction]], the splitting)".
Part 3 closes the scope gap: Gamma > 0 on the whole of region III, which ends at 1.8614372 <= R_u2 <= 1.8614410.
Block 3.1 is a new subsection with one proposition, inserted in sec:bg-below after prop:bg-slice and the paragraph that
follows it, before sec:bg-theorem. Blocks 3.2-3.6 replace the statements that used the seed region in place of region
III: cor:loc-charge-seed, thm:charge-sign (a), a sentence of sec:loc-setting, thm:bg-margins (b) and the sentence after
the proof of prop:margins-seed. -->

<!-- Part 1. Block 1.1: after lem:loc-harmonics, before thm:loc-tensor. -->

**Lemma {#lem:loc-tt-second}** (The second variation of the scalar curvature of S³.) Let T be a smooth transverse
trace-free symmetric 2-tensor on the unit S³ with Δ̂T = −k_T²T, and put D²Scal_γ̂[T, T] := d²/dε² Scal(γ̂ + εT) at ε = 0.
Then

    ∫_(S³) D²Scal_γ̂[T, T] dvol_γ̂ = (1 − k_T²/2) ∫_(S³) |T|²_γ̂ dvol_γ̂.                             {#eq:loc-tt-second}

*Proof.* For a family g + εh of metrics on a closed manifold, the Levi-Civita connection varies by δΓ^k_ij = ½(∇_ih_j^k +
∇_jh_i^k − ∇^kh_ij), and Palatini's identity Ric′[h]_ij = ∇_kδΓ^k_ij − ∇_jδΓ^k_ki gives

    Ric′[h]_ij = ½(∇^k∇_ih_jk + ∇^k∇_jh_ik − ∇^k∇_kh_ij − ∇_i∇_j tr h),

whose trace gives the first variation DScal[h] = div div h − Δ tr h − ⟨h, Ric⟩ of the scalar curvature. Integrating, the
divergences drop out and

    d/dε ∫ Scal(g_ε) dvol_(g_ε) = ∫ (DScal_(g_ε)[h] + ½ Scal(g_ε) tr_(g_ε) h) dvol_(g_ε)
                                = ∫ ⟨𝒢(g_ε), h⟩_(g_ε) dvol_(g_ε),

g_ε := g + εh, 𝒢(g) := ½ Scal(g) g − Ric(g). Take g = γ̂ and h = T, and let E(ε) := ∫ Scal(γ̂ + εT) dvol_(γ̂+εT); all
integrals below are over S³ against dvol_γ̂. Since Ric(γ̂) = 2γ̂ and Scal(γ̂) = 6, 𝒢(γ̂) = γ̂ and DScal[T] = −⟨T,
Ric(γ̂)⟩ = −2 tr T = 0. The Riemann tensor of the unit S³ is γ̂_ikγ̂_jl − γ̂_ilγ̂_jk, and the Ricci identity gives, for
trace-free T, ∇^k∇_iT_jk = ∇_i∇^kT_jk + 3T_ij = 3T_ij; so Ric′[T] = ½(6T − Δ̂T) = ½(6 + k_T²)T. Differentiating E′(ε) =
∫⟨𝒢(γ̂ + εT), T⟩_(γ̂+εT) dvol_(γ̂+εT) at ε = 0, the derivative of 𝒢 is ½DScal[T]γ̂ + ½Scal(γ̂)T − Ric′[T] = −(k_T²/2)T,
the two inverse metrics in ⟨γ̂, T⟩ contribute −2|T|²_γ̂, and the variation ½ tr T dvol_γ̂ of the volume contributes ½⟨γ̂,
T⟩ tr T = 0; so E″(0) = −(k_T²/2 + 2)∫|T|²_γ̂. On the other hand

    dvol_(γ̂+εT) = (1 + ½ε tr T + ε²(⅛(tr T)² − ¼|T|²_γ̂) + O(ε³)) dvol_γ̂ = (1 − ¼ε²|T|²_γ̂ + O(ε³)) dvol_γ̂

and Scal(γ̂ + εT) = 6 + ½ε² D²Scal_γ̂[T, T] + O(ε³), so E″(0) = ∫ D²Scal_γ̂[T, T] − 3∫|T|²_γ̂. Comparing the two values
of E″(0) gives [[eq:loc-tt-second]]. ∎

**Lemma {#lem:loc-tensor-variations}** (Second variations for tensor data on a round slice.) Let γ = G dR² + R²γ̂ and
K0 = κ0 G dR² + Y0 R² γ̂ be round data on a band, with G > 0, κ0 and Y0 smooth functions of R. Let T be as in
[[lem:loc-tt-second]], H and Π smooth functions of R, h := 2R²H T and k := R²(Π + 2Y0H) T. For a function X of the data
write [X]_2 for the ε² coefficient of X(γ + εh, K0 + εk), and write ′ := d/dR. Then, with ℳ_R := ℳ(∂_R) the radial
component of the momentum constraint and |T|²_γ̂ the pointwise norm, a function on S³,

    [(tr K)² − |K|²]_2 = −(Π² + 4(κ0 + 2Y0)HΠ) |T|²_γ̂,
    [ℳ_R]_2 = (2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′) |T|²_γ̂,
    ∫_(S³) [Scal]_2 dvol_γ̂ = ((2 − k_T²)H²/R² + (16HH′/R − H′²)/G + 4G^(−1/2)(G^(−1/2)HH′)′) ∫_(S³) |T|²_γ̂ dvol_γ̂.
                                                                                             {#eq:loc-tensor-variations}

*Proof.* Let T^♯ be the endomorphism of the tangent spaces of the spheres with γ̂(T^♯X, Z) = T(X, Z); then tr T^♯ = 0 and
tr (T^♯)² = |T|²_γ̂. The tensors h and k have no radial components, and on the spheres γ⁻¹h = 2HT^♯ and γ⁻¹k = (Π +
2Y0H)T^♯. Let A_ε := (γ + εh)⁻¹(K0 + εk), as an endomorphism. It is κ0 on ∂_R, and on the spheres, since (1 + 2εHT^♯)⁻¹ =
1 − 2εHT^♯ + 4ε²H²(T^♯)² + O(ε³),

    A_ε = Y0 + εΠT^♯ − 2ε²HΠ(T^♯)² + O(ε³).

So tr A_ε = κ0 + 3Y0 − 2ε²HΠ|T|²_γ̂ + O(ε³) and tr A_ε² = κ0² + 3Y0² + ε²(Π² − 4Y0HΠ)|T|²_γ̂ + O(ε³), the terms of order
ε vanishing with tr T^♯. Since (tr K)² − |K|² = (tr A_ε)² − tr A_ε², this gives the first identity.

For the second, let γ = G dR² + g with g = g(R) a family of metrics on S³, and K with K(∂_R, ∂_A) = 0, K(∂_R, ∂_R) = κG
for a function κ of R, and spherical part 𝒦. The Christoffel symbols Γ^R_RR = G′/(2G), Γ^R_AB = −g′_AB/(2G), Γ^A_RB =
½(g⁻¹g′)^A_B and Γ^A_RR = Γ^R_RA = 0 give (div K)_R = κ′ + ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′g⁻¹𝒦), and tr K = κ + tr(g⁻¹𝒦), so
that

    ℳ_R = ½κ tr(g⁻¹g′) − ½tr(g⁻¹g′ g⁻¹𝒦) − (tr g⁻¹𝒦)′.

Along the family, g = R²(γ̂ + 2εHT), g⁻¹g′ = 2/R + 2εH′T^♯ − 4ε²HH′(T^♯)² + O(ε³), and g⁻¹𝒦 is A_ε on the spheres. The ε²
coefficients of the three terms are −2κ0HH′|T|²_γ̂, −½(−4HΠ/R + 2H′Π − 4Y0HH′)|T|²_γ̂ and 2(HΠ)′|T|²_γ̂, whose sum is the
second identity.

For the third, consider a metric G dR² + R²ĝ with ĝ = ĝ(R) a family of metrics on S³. For a foliation by hypersurfaces
S with unit normal ν, lapse N and second fundamental form L, the Gauss equation Scal = Scal_S + 2Ric(ν, ν) −
(tr L)² + |L|² and the Riccati equation Ric(ν, ν) = −ν(tr L) − |L|² − N⁻¹Δ_S N hold, as in the proof of
[[lem:constraints-evolution]] (a). The lapse G^(1/2) of the foliation by the spheres {R = const} is constant on each
sphere, so the last term vanishes and

    Scal = R⁻² Scal(ĝ) − (tr L)² − |L|² − 2G^(−1/2)(tr L)′,      L := ½G^(−1/2) ∂_R(R²ĝ),

L the second fundamental form of the spheres with respect to the unit normal G^(−1/2)∂_R. For ĝ = γ̂ + 2εHT, as an
endomorphism L = G^(−1/2)(1/R + εH′T^♯ − 2ε²HH′(T^♯)²) + O(ε³), so that tr L = G^(−1/2)(3/R − 2ε²HH′|T|²_γ̂) + O(ε³)
and |L|² = G⁻¹(3/R² + ε²(H′² − 4HH′/R)|T|²_γ̂) + O(ε³). The ε² coefficients of the last three terms of Scal are therefore
12HH′|T|²_γ̂/(RG), −(H′² − 4HH′/R)|T|²_γ̂/G and 4G^(−1/2)(G^(−1/2)HH′)′|T|²_γ̂. The ε² coefficient of the first term is
R⁻² times half of D²Scal_γ̂[2HT, 2HT] = 4H²D²Scal_γ̂[T, T], whose integral over S³ is, by [[lem:loc-tt-second]], R⁻²(2 −
k_T²)H²∫|T|²_γ̂. Adding gives the third identity. ∎

<!-- Part 1. Block 1.2: replaces item (iii) of the proof of thm:loc-tensor (the marker computational-1). -->

(iii) By [[lem:racz-split-formulas]] (b), K^l_l = 3n^R/R = 3Y0, so n^R = RY0 and δ = (h, k) is the variation of
[[lem:loc-tensor-variations]]. In [[eq:loc-charge]], D²ℋ[δ, δ] = 2[ℋ]_2, D²ℳ[δ, δ] = 2[ℳ]_2, Y_s·ℳ = Y_s^R ℳ_R and dvol =
√G R³ dR dvol_γ̂, and ∫_(S³) |T|²_γ̂ dvol_γ̂ = (2π)²|T|². So [[eq:loc-tensor-variations]] and G⁻¹ = N_s² ((ii)) give,
with ′ := d/dR,

    Q(δ) = (2π)²|T|² ∫ R³√G (N_s 𝔥 + 2Y_s^R 𝔪) dR,
    𝔥 := (2 − k_T²)H²/R² + N_s²(16HH′/R − H′²) + 4N_s(N_sHH′)′ − 4(κ0 + 2Y0)HΠ − Π²,
    𝔪 := 2(HΠ)′ + 2HΠ/R − H′Π + 2(Y0 − κ0)HH′.                                             {#eq:loc-tensor-density}

Since ξ is a Killing field, for X, Z tangent to Σ, 0 = g(∇_Xξ, Z) + g(∇_Zξ, X) = 2N_sK0(X, Z) + (L_(Y_s)γ)(X, Z), because
g(∇_X(N_sn), Z) = N_sK0(X, Z) and the tangential part of ∇_XY_s is D_XY_s. The components of this equation on the spheres
and on ∂_R are 2RY_s^R = −2N_sY0R² and Y_s^R G′ + 2G(Y_s^R)′ = −2N_sκ0G. With y_s := Y_s^R/N_s = √G Y_s^R they read

    Y0 = −y_s/R,        κ0 = −y_s′,                                                             {#eq:loc-tensor-kid}

and (ii) reads N_s² − y_s² = f. Now collect the integrand of [[eq:loc-tensor-density]], using N_s√G = 1 and √G Y_s^R =
y_s. The terms in Π², ΠH′ and H′² are −R³Π², −2R³y_sΠH′ and −R³N_s²H′². The terms in HΠ and HΠ′ are

    −4R³(κ0 + 2Y0)HΠ + 4R²y_sHΠ + 4R³y_s(HΠ)′ = (4R³y_sHΠ)′ − 4R³(κ0 + y_s′ + 2Y0 + 2y_s/R)HΠ = (4R³y_sHΠ)′,

by [[eq:loc-tensor-kid]]. Writing 4R³N_s(N_sHH′)′ = (4R³N_s²HH′)′ − 4N_s(R³N_s)′HH′, the terms in H², HH′ and HH″ are

    (2 − k_T²)RH² + (16R²N_s² − 4N_s(R³N_s)′ + 4R³y_s(Y0 − κ0))HH′ + (4R³N_s²HH′)′,

and by [[eq:loc-tensor-kid]] the coefficient of HH′ is 4R²(N_s² − y_s²) − 2R³(N_s² − y_s²)′ = 4R²f − 2R³f′ = 4R² − 8μ,
since f = 1 − μ/R². With (4R² − 8μ)HH′ = ((2R² − 4μ)H²)′ − 4RH², these terms are −(k_T² + 2)RH² + (4R³N_s²HH′ + (2R² −
4μ)H²)′. Altogether

    R³√G (N_s 𝔥 + 2Y_s^R 𝔪) = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH² + 𝔅_T′,
    𝔅_T := 4R³N_s²HH′ + 4R³y_sHΠ + 2(R² − 2μ)H².                                            {#eq:loc-tensor-flux}

On the other hand, ξ(H) = N_sΠ + Y_s^RH′, |dH|² = −Π² + N_s²H′² and g(ξ, n) = −N_s give

    −2T_m(ξ, n)√G = −R³(Π² + 2y_sΠH′ + N_s²H′²) − (k_T² + 2)RH².

Since 𝔅_T has compact support in (R1, R2), integrating [[eq:loc-tensor-flux]] in R gives [[eq:loc-tensor-charge]].

<!-- Part 2. Block 2.1: replaces lem:loc-scalar-reduction, statement and proof. -->

**Lemma {#lem:loc-scalar-reduction}** (The scalar modes.) On the static slice put x := μ/R², so that f = 1 − x and Rf′ =
2x, and write ′ := d/dR. A class seed is a sum of scalar modes, tensor modes and an l = 0 part, and 𝔈_V, 𝔈_K and the
constraints split mode by mode. Write a scalar mode of degree l = 2j ≥ 2 as h_RR = aS, h_Rϑ = R b ∂_ϑS, h|_(S³) =
R²(cSγ̂ + eŜ), its other components vanishing, with S := P_j(cos 2ϑ), k² := l(l + 2), Ŝ := D̂D̂S + (k²/3)γ̂S, and k
likewise with (p, q_k, w, z) in place of (a, b, c, e); put ‖S‖² := ∫_0^(π/2) S² sc dϑ, m := k² − 3 and H_KI := m + 6x.

(a) The vector field X = αS∂_R + β̃ ∂_ϑS ∂_ϑ shifts (a, b, c, e) by ((1/f)′α + 2α′/f, α/(Rf) + Rβ̃′, 2α/R − (2k²/3)β̃,
2β̃), so that b = e = 0 is reached by β̃ = −e/2 and α = −Rf(b − Re′/2); the quantities A := a + (1/f)′α + 2α′/f and F :=
c/2 − fb + k²e/6 + fRe′/2 are gauge invariant. The direction k_ψ with ψ_g = ψS has trace-free angular part ψŜ, so z = 0
is reached by ψ = −R²z. Both gauges are local in R.

(b) For z = 0 the momentum constraint of the mode is ℳ = 𝔪_R S dR + 𝔪_ϑ ∂_ϑS dϑ, with

    𝔪_R := (3fp − 3w − k²q_k)/R − 3w′,        𝔪_ϑ := (4 − 3x)q_k − fp + Rf q_k′ − 2w.                {#eq:loc-mom-modes}

With Z := R³(w − fq_k), the map Z ↦ (q_k, w, p) = (−3Z′/(R²H_KI), Z/R³ + fq_k, ((4 − 3x)q_k + Rf q_k′ − 2w)/f) solves the
constraint, every compactly supported solution is the image of its own Z, and on the constraint

    𝔈_K = (2π)² ‖S‖² ∫ 6k²m Z²/(R³H_KI²) dR.                                                           {#eq:loc-ek}

(c) For b = e = 0 put A := a and F := c/2. Then DScal[h] = C(A, F) S, with

    C(A, F) := R⁻²((k² + 6 + 6x)fA + 3Rf²A′ + 4(k² − 3)F − 6R(1 + 3f)F′ − 6R²fF″),                       {#eq:loc-c}

and 𝔈_V(h) = (2π)² ‖S‖² ∫ E_V(A, F) dR, with

    E_V(A, F) := Rf²(k²/2 + 6 + 12x)A² + 6R²f³AA′ − 3R³f²A′F′ − 6R³f²AF″ − 12R²f(1 + f)AF′
                 + 3k²RfAF + (10k² − 24)RF² − 12R³fFF″ − 12R²(1 + 3f)FF′.                                {#eq:loc-ev-af}

With ℓ := A − (2R/f)F′ + (2H_KI/(3f²))F and κ_M := (k² + 6 + 6x)/(3Rf),

    ℓ′ + κ_Mℓ − (2k²H_KI/(9Rf³)) F = (R/(3f²)) C(A, F),                                                {#eq:loc-moncrief}

so the map ℓ ↦ (A, F), F = 9Rf³(ℓ′ + κ_Mℓ)/(2k²H_KI), A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F, solves C = 0, and every
compactly supported solution is the image of its own ℓ. With Φ_M := R^(3/2)f²ℓ/H_KI, on the constraint,

    𝔈_V = (2π)² ‖S‖² (27m/(2k²)) ∫ (f Φ_M′² + Qp Φ_M²/(16R²H_KI²)) dR,
    Qp := 1296x³ + (624m − 144)x² + 36m(m − 12)x + 16m³ + 60m².                                          {#eq:loc-ev}

(d) The l = 0 part of a seed is a gauge seed and contributes nothing to 𝔈_V and 𝔈_K: on the constraint, h_(l=0) =
L_(RF∂_R)γ for a compactly supported F, and k_(l=0) = k_ψ with ψ_g := −N_s ∫_R^∞ R′w(R′)/(f(R′)N_s(R′)) dR′, where
k_(l=0)|_(S³) = R²wγ̂; ψ_g vanishes beyond the support and is a constant multiple of N_s on its inner side.

*Proof.* *The static slice.* Here γ = f⁻¹dR² + R²γ̂, N_s = √f, K0 = 0 and Y_s = 0. The Christoffel symbols of γ are
Γ^R_RR = −x/(Rf), Γ^R_AB = −Rf γ̂_AB, Γ^A_RB = δ^A_B/R and Γ^A_BC = Γ̂^A_BC, the others vanishing; Ric(γ) = −(3x/(R²f))
dR² + x γ̂ and Scal(γ) = 0; and N_s dvol = R³ dR dvol_γ̂. Integrals over S³ are against dvol_γ̂; for a class harmonic S
of degree l, Δ̂S = −k²S, ∫S² = (2π)²‖S‖² and ∫|D̂S|² = k²∫S², and ∫Δ̂φ = 0 for every function φ on S³.

*The splitting.* The isometries SO(4) of the round S³ act on the static slice by isometries fixing N_s, so the constraint
maps are SO(4)-equivariant and 𝔈_V and 𝔈_K are invariant quadratic forms. Under SO(4) ≅ (SU(2) × SU(2))/{±1} the
scalar harmonics of degree l span the irreducible representation of highest weights (l/2, l/2), and the transverse
trace-free tensor harmonics of degree l the sum of those of highest weights ((l ± 2)/2, (l ∓ 2)/2) ([[sec:iii-f1-1]]);
for different types or degrees these representations are pairwise inequivalent. A scalar mode of degree l is the image
of the scalar harmonics of degree l under the equivariant linear map u ↦ a u dR² + 2R b du dR + R²(c uγ̂ + e(D̂D̂u +
(k²/3)γ̂u)), and likewise for k, so it lies in the isotypic component of (l/2, l/2); a tensor mode of degree l lies in
that of ((l ± 2)/2, (l ∓ 2)/2), and the l = 0 part in that of the trivial representation. An invariant bilinear form pairs isotypic components of inequivalent
representations to zero, and an equivariant linear map takes each isotypic component into the isotypic component of the
same representation (Schur's lemma). So the polarisations of 𝔈_V and 𝔈_K vanish between different modes, and the
constraints of a seed hold exactly when those of each mode hold. The mode expansions of smooth data converge with all
their derivatives, so 𝔈_V and 𝔈_K of a seed are the sums of those of its modes.

*(a) The gauges.* The vector field X has X^R = αS and X^ϑ = β̃∂_ϑS, so X_R = αS/f and X_A = R²β̃∂_AS. Then (L_Xγ)_RR =
(α(1/f)′ + 2α′/f)S, (L_Xγ)_RA = (α/f + R²β̃′)∂_AS and (L_Xγ)_AB = 2RαSγ̂_AB + 2R²β̃D̂_AD̂_BS = R²((2α/R − (2k²/3)β̃)Sγ̂ +
2β̃Ŝ)_AB, which are the stated shifts. The shifts are linear in (α, β̃), and b = e = 0 is reached by exactly one (α, β̃),
the stated one; A and F are the a and c/2 of the representative so reached. Adding to the data the shifts of another
vector field X′ of this form changes the (α, β̃) that reaches b = e = 0 by −X′ and leaves that representative unchanged,
so A and F are gauge invariant. For ψ_g = ψ(R)S, the spherical part of D²ψ_g is ψD̂D̂S + Rfψ′Sγ̂, since Γ^R_AB =
−Rfγ̂_AB, and Ric(γ) is round; so the trace-free spherical part of k_ψ = D²ψ_g − ψ_g Ric(γ) is ψ(D̂D̂S + (k²/3)γ̂S) = ψŜ,
which shifts z by ψ/R². The gauge functions α, β̃ and ψ are built pointwise from the data and their R-derivatives, so
they have compact support with the data.

*(b) The momentum constraint.* For z = 0, k_RR = pS, k_RA = Rq_k ∂_AS and k_AB = R²wSγ̂_AB, and tr k = (fp + 3w)S. With
the Christoffel symbols above, (div k)_R = (fp′ + f′p + (3fp − 3w − k²q_k)/R)S and (div k)_A = (Rf q_k′ + (4 − 3x)q_k +
w)∂_AS, and ℳ = div k − d tr k gives [[eq:loc-mom-modes]]. Expanding, with Rf′ = 2x,

    Z′ + (R²H_KI/3) q_k + R² 𝔪_ϑ + (R³/3) 𝔪_R = 0                                                    {#eq:loc-z-identity}

identically. If 𝔪_R = 𝔪_ϑ = 0, then [[eq:loc-z-identity]] gives q_k = −3Z′/(R²H_KI) (H_KI ≥ m > 0), w = Z/R³ + fq_k by
the definition of Z, and p from 𝔪_ϑ = 0 (f > 0): the data are the image of their Z. Conversely, for the image of a Z,
𝔪_ϑ = 0 by the definition of p, and then 𝔪_R = 0 by [[eq:loc-z-identity]]. Since |k|² = (f²p² + 3w²)S² + 2fq_k²|D̂S|² and
(tr k)² = (fp + 3w)²S², 𝔈_K = (2π)²‖S‖² ∫ 𝔢_K dR with 𝔢_K := R³(2k²fq_k² − 6w² − 6fpw). On 𝔪_ϑ = 0, inserting fp from
𝔪_ϑ = 0 and then w = Z/R³ + fq_k, and using (R⁴f²)′ = 4R³f and (Rf)′ = 1 + x, an expansion gives

    𝔢_K = 6Z²/R³ + (12x − 6) Z q_k + 2R³fH_KI q_k² + 6RfZ′q_k + (−3R⁴f²q_k² − 6RfZq_k)′.

On 𝔪_R = 0 as well, [[eq:loc-z-identity]] gives 6RfZ′q_k = −2R³fH_KI q_k², and q_k = −3Z′/(R²H_KI) gives (12x − 6)Zq_k =
−9(2x − 1)(Z²)′/(R²H_KI). Since ((2x − 1)/(R²H_KI))′ = 2(m − 4mx − 12x²)/(R³H_KI²) and 6H_KI² + 18(m − 4mx − 12x²) =
6m(m + 3) = 6k²m,

    𝔢_K = 6k²m Z²/(R³H_KI²) + 𝔅_K′,        𝔅_K := −3R⁴f²q_k² − 6RfZq_k − 9(2x − 1)Z²/(R²H_KI).

𝔅_K has compact support, which gives [[eq:loc-ek]].

*(c) The Hamiltonian constraint.* Let α and β be smooth functions of R and the angles, and γ_ε := f⁻¹e^(2α)dR² +
R²e^(2β)γ̂. Then, with ζ := α − β,

    R²e^(2β) Scal(γ_ε) = 6 − 2Δ̂ζ − 2|D̂ζ|² − 6Δ̂β − 6D̂α·D̂β − 6√f e^(−α) ∂_R(R√f e^(2β−α)(1 + R∂_Rβ)).
                                                                                                    {#eq:loc-scal-exact}

Indeed, γ_ε = Λ²ĝ with Λ := Re^β and ĝ := ã²dR² + γ̂, ã := e^(α−β)/(R√f). The spheres {R = const} carry the metric γ̂ in
ĝ for every R, so their second fundamental form vanishes, and the Gauss and Riccati equations of the proof of
[[lem:constraints-evolution]] (a), with lapse ã and second fundamental form 0, give Scal(ĝ) = 6 − 2ã⁻¹Δ̂ã. Tracing the
formula for Ric[h] − Ric[g] in the proof of [[lem:conformal]] with m = 4, g = ĝ and h = Λ²ĝ (so that ψ = ln Λ and □ =
Δ_ĝ there) gives Scal(Λ²ĝ) = Λ⁻²(Scal(ĝ) − 6Δ_ĝ ln Λ − 6|d ln Λ|²_ĝ) = Λ⁻²(Scal(ĝ) − 6Λ⁻¹Δ_ĝΛ), since Δ_ĝ ln Λ +
|d ln Λ|²_ĝ = Λ⁻¹Δ_ĝΛ; and Δ_ĝΛ = ã⁻¹∂_R(ã⁻¹∂_RΛ) + ã⁻¹D̂·(ãD̂Λ), the volume form of ĝ being ã dR dvol_γ̂. Inserting
ã⁻¹Δ̂ã = Δ̂ζ + |D̂ζ|², Λ⁻¹ã⁻¹∂_R(ã⁻¹∂_RΛ) = √f e^(−α)∂_R(R√f e^(2β−α)(1 + R∂_Rβ)) and Λ⁻¹ã⁻¹D̂·(ãD̂Λ) = Δ̂β + D̂α·D̂β
gives [[eq:loc-scal-exact]].

For b = e = 0, γ + εh = f⁻¹(1 + εfAS)dR² + R²(1 + 2εFS)γ̂, so α = εα_1 + ε²α_2 + O(ε³) and β = εβ_1 + ε²β_2 + O(ε³) with
α_1 = fAS/2, α_2 = −f²A²S²/4, β_1 = FS and β_2 = −F²S². Write Y := R√f e^(2β−α)(1 + R∂_Rβ) = Y_0 + εy_1S + ε²y_2S² +
O(ε³) and Ξ := R²e^(2β)Scal(γ + εh) = εΞ_1 + ε²Ξ_2 + O(ε³). Then Y_0 = R√f and Y_0′ = (f + Rf′/2)/√f = 1/√f, so that the
term of order ε⁰ of Ξ is 6 − 6 = 0;

    y_1 = R√f (2F − fA/2 + RF′),        y_2 = R√f (3f²A²/8 − fAF − RfAF′/2);

and, from [[eq:loc-scal-exact]] with e^(−α) = 1 − α + α²/2 + O(α³),

    Ξ_1 = −2Δ̂(α_1 − β_1) − 6Δ̂β_1 + 6α_1 − 6√f y_1′S,
    Ξ_2 = −2Δ̂(α_2 − β_2) − 2|D̂(α_1 − β_1)|² − 6Δ̂β_2 − 6D̂α_1·D̂β_1 − 6√f (y_2′S² − α_1y_1′S) − 6(α_1²/2 − α_2).

With Δ̂S = −k²S, Ξ_1 = ((k² + 3)fA + 4k²F − 6√f y_1′)S. Since DScal[h] = R⁻²Ξ_1 and 6√f y_1′ = 6Z_1 + 6RfZ_1′ with Z_1 :=
2F − fA/2 + RF′, this is [[eq:loc-c]]. Next, D²Scal[h, h] is twice the ε² coefficient of Scal(γ + εh), R³Scal =
Re^(−2β)Ξ, and N_s dvol = R³ dR dvol_γ̂; so 𝔈_V(h) = −∫∫ R(Ξ_2 − 2β_1Ξ_1) dvol_γ̂ dR. Integrating over S³, the four
Laplacians drop out, ∫|D̂(α_1 − β_1)|² = k²(fA/2 − F)²∫S², ∫D̂α_1·D̂β_1 = (k²fAF/2)∫S², α_1²/2 − α_2 = 3f²A²S²/8, and
∫β_1Ξ_1 = R²F C(A, F)∫S²; so 𝔈_V(h) = (2π)²‖S‖² ∫ E_V(A, F) dR with

    E_V(A, F) = R(2k²(fA/2 − F)² + 3k²fAF + 6√f (y_2′ − (fA/2) y_1′) + (9/4)f²A²) + 2R³F C(A, F),

and expanding the derivatives of y_1 and y_2 gives [[eq:loc-ev-af]].

Five identities, each checked by expanding both sides with Rf′ = 2x, x′ = −2x/R, k² = m + 3 and H_KI = m + 6x, reduce 𝔈_V
on the constraint. First,

    E_V(A, F) = E_red + R⁴F′C(A, F) + 𝔅_1′,
    E_red := (k²/2)Rf²A² + 3k²RfAF − R²f(k² + 12f)AF′ + (14k² − 24)RF² + 24R³fF′²,
    𝔅_1 := 3R²f³A² − 6R³f²AF′ + (12μ − 2k²R²)F² − 12R³fFF′ + 3R⁴fF′².                                   {#eq:loc-ev-red}

Second, [[eq:loc-moncrief]]; it gives the statement about the map ℓ ↦ (A, F): for (A, F) with C = 0 and compact support,
F = 9Rf³(ℓ′ + κ_Mℓ)/(2k²H_KI) by [[eq:loc-moncrief]] and A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F by the definition of ℓ;
conversely, for (A, F) built from a given ℓ, the variable ℓ of (A, F) is the given one, and [[eq:loc-moncrief]] gives
C(A, F) = 0. Third, substituting A = ℓ + (2R/f)F′ − (2H_KI/(3f²))F into E_red, the terms in F′² cancel (24R³f − 2R³(k² +
12f) + 2k²R³ = 0), and

    E_red = (k²/2)Rf²ℓ² + c_1ℓF + c_2ℓF′ + c_3F² + c_4FF′,
    c_1 := −(k²R/3)(2m − 9 + 21x),        c_2 := R²f(m − 9 + 12x),
    c_3 := (2R/(9f²))(m³ − 6m² + 36m + 81 + 21m²x − 117mx − 324x + 153mx² + 351x²),
    c_4 := −(2R²/(3f))(m² − 18m − 27 + 27mx − 27x + 72x²).

Fourth, with c_2ℓF′ = (c_2ℓF)′ − c_2′ℓF − c_2ℓ′F and c_4FF′ = (½c_4F²)′ − ½c_4′F²,

    E_red = (k²/2)Rf²ℓ² + F(e_1ℓ − c_2ℓ′) + e_0F² + (c_2ℓF + ½c_4F²)′,
    e_1 := c_1 − c_2′ = −(R/3)(2m² + 3m − 81 + 21mx + 63x + 72x²),
    e_0 := c_3 − ½c_4′ = (2k²R/(9f²))(m² − 6m + 15mx − 54x + 72x²).

Fifth, on the constraint F = λ(ℓ′ + κ_Mℓ) with λ := 9Rf³/(2k²H_KI), so that E_red = P_2ℓ′² + P_1ℓℓ′ + P_0ℓ² + (c_2ℓF +
½c_4F²)′ with

    P_2 := −λc_2 + λ²e_0 = 27mR³f⁵/(2k²H_KI²),
    P_1 := λe_1 − λκ_Mc_2 + 2λ²κ_Me_0 = −3R²f³(m³ − 3m² − 54m + 15m²x + 45mx + 54mx² + 54x²)/(2k²H_KI²),
    P_0 := (k²/2)Rf² + λκ_Me_1 + λ²κ_M²e_0
        = −3Rf²(m³ − 12m² − 81m + 2m³x + 24m²x + 18mx + 24m²x² + 126mx² + 54x² + 72mx³ + 108x³)/(2k²H_KI²).

With P_1ℓℓ′ = (½P_1ℓ²)′ − ½P_1′ℓ²,

    E_red = P_2ℓ′² + P̃_0ℓ² + 𝔅_2′,        𝔅_2 := c_2ℓF + ½c_4F² + ½P_1ℓ²,
    P̃_0 := P_0 − ½P_1′ = 27mRf³(m² + 3m − m²x − 9mx − 54x − 10mx² − 18x² − 24x³)/(2k²H_KI³).

Finally, ℓ = ρΦ_M with ρ := H_KI/(R^(3/2)f²), for which ρ′/ρ = −(3m + 5mx + 42x + 6x²)/(2RfH_KI), gives

    P_2ℓ′² + P̃_0ℓ² = P_2ρ²Φ_M′² + (P_2ρ′² + P̃_0ρ² − (P_2ρρ′)′)Φ_M² + (P_2ρρ′Φ_M²)′,
    P_2ρ² = 27mf/(2k²),        P_2ρρ′ = −27m(3m + 5mx + 42x + 6x²)/(4k²RH_KI),
    P_2ρ′² + P̃_0ρ² − (P_2ρρ′)′ = 27m Qp/(32k²R²H_KI²).

On the constraint R⁴F′C(A, F) = 0, and 𝔅_1, 𝔅_2 and P_2ρρ′Φ_M² have compact support; so the five identities give
[[eq:loc-ev]].

*(d) The l = 0 part.* For l = 0, S = 1, Ŝ = 0 and D̂S = 0, so h_(l=0) = a dR² + R²cγ̂ and k_(l=0) = p dR² + R²wγ̂ with a,
c, p, w functions of R. The derivation of [[eq:loc-c]] in (c) uses neither b nor e, so [[eq:loc-c]] holds with k² = 0, A
:= a and F := c/2. By (a) with S = 1 and β̃ = 0, X := RF∂_R gives L_Xγ = ((1/f)′RF + 2(RF)′/f)dR² + 2R²Fγ̂, and
DScal[L_Xγ] = X(Scal(γ)) = 0. So on the constraint A_r := a − (1/f)′RF − 2(RF)′/f satisfies C(A_r, 0) = 0 with k² = 0,
that is 6(1 + x)fA_r + 3Rf²A_r′ = 0, whose solutions are the constant multiples of x/f², since (ln(x/f²))′ = −2/R −
4x/(Rf) = −2(1 + x)/(Rf); these vanish nowhere unless the constant is 0. Compact support gives A_r = 0, so h_(l=0) =
L_(RF∂_R)γ with F compactly supported. By (b) with k² = 0 and q_k = 0, the momentum constraint of the l = 0 part is fp =
Rw′ + w. For ψ_g = ψ(R), k_ψ has spherical part R²w_ψγ̂ with w_ψ = fψ′/R − xψ/R² = (fN_s/R)(ψ/N_s)′, since N_s′/N_s =
x/(Rf); and k_ψ solves the momentum constraint (proof of [[lem:loc-gauge-invariance]]), so its RR component is (Rw_ψ′ +
w_ψ)/f. The ψ_g of (d) has (ψ_g/N_s)′ = Rw/(fN_s), so w_ψ = w and k_(l=0) = k_ψ. Hence the l = 0 part is the first
variation of the data along the generator ψ_g n + RF∂_R, a gauge seed. Its energies vanish: 𝔈_V(L_Xγ) = 𝔈_V(0) = 0 by
[[lem:loc-gauge-invariance]], and 𝔈_K(k_(l=0)) = 2π² ∫ R³(−6w² − 6fpw) dR = −6π² ∫ (R⁴w²)′ dR = 0. ∎

<!-- Part 2. Block 2.2: in the proof of thm:loc-outside, the parenthesis "(orthogonality of the class harmonics of
different type and degree, [[lem:loc-harmonics]], the mode sums converging for smooth data)" becomes: -->

([[lem:loc-scalar-reduction]], the splitting)

<!-- Part 3. Block 3.1: a new subsection of sec:bg-below, after prop:bg-slice and the paragraph that follows it
("Near R = R_* the packet's slice points approach region I ..."), before sec:bg-theorem. -->

#### The end of region III {#sec:bg-region-three-end}

**Proposition {#prop:bg-region-three-end}** (The end of region III.) Let ρ_u2 and R_u2 be as in [[prop:bg-seed]] (a), so
that region III meets Σ_τ0 in the points with 0.70 ≤ R ≤ R_u2.

(a) 2.773631 < ρ_u2 < 2.7736325 and 1.8614372 ≤ R_u2 ≤ 1.8614410.

(b) At every point of Σ_τ0 with 1.861 ≤ R ≤ R_u2, the quantity Γ/E² of [[eq:margins-gamma-form]] for the background (ψ =
ψ_III and μ = μ3) satisfies Γ/E² ≥ 10.40.

(c) Γ > 0 at every point of Σ_τ0 in region III: Γ/E² ≥ 0.048 on the seed region 0.70 ≤ R ≤ 1.861, and Γ/E² ≥ 10.40 for
1.861 ≤ R ≤ R_u2.

(d) No point of Σ_τ0 with R_u2 < R < R_* is a vacuum point of the background. So every band of Σ_τ0 on which the
background is vacuum lies in region III, {0.70 ≤ R ≤ R_u2}, or in {R ≥ R_*}.

*Proof.* (a) As in the proof of [[prop:bg-seed]] (a), g(ρ) := Φ(ρ) − v̂(ρ) − 0.68 is decreasing on [2.32, 3.44] with the
single zero ρ_u2, and R_u2 = v̂(ρ_u2) + 0.68. By direct evaluation of the polynomial Φ̃ of [[sec:tab-bg-ray]] and of
[[eq:bg-tangherlini]], Φ̃(2.773631) − v̂(2.773631) − 0.68 ≥ 1.3949 × 10⁻⁶ and Φ̃(2.7736325) − v̂(2.7736325) − 0.68 ≤
−1.1149 × 10⁻⁶. Since |Φ − Φ̃| ≤ ε₀ = 8.69 × 10⁻⁷ at u = u2 ([[prop:bg-rays]]), g(2.773631) > 0 > g(2.7736325), so
2.773631 < ρ_u2 < 2.7736325. As v̂ is increasing, R_u2 lies between v̂(2.773631) + 0.68 ≥ 1.86143720 and v̂(2.7736325) +
0.68 ≤ 1.86144094.

(b) Let P be a point of Σ_τ0 with 1.861 ≤ R ≤ R_u2. It lies in region III, on the ray ρ with v̂(ρ) + 0.68 = R
([[lem:bg-reduction]] (f), [[prop:bg-seed]] (a)), and there ψ_III^(k)(v̂(ρ)) = Ψ_k(ρ, Φ(ρ), …, Φ‴(ρ), μ3) for k ≤ 2
([[eq:bg-psi3]]). Since v̂ is increasing, v̂(2.7734) + 0.68 ≤ 1.8608633 < 1.861 and ρ ≤ ρ_u2 < 2.7737, the ray has ρ ∈
[2.7734, 2.7737]. Put ρ_m := 2.77355 and h := 1.5 × 10⁻⁴. For such ρ and j ≤ 3, |Φ̃^(j)(ρ) − Φ̃^(j)(ρ_m)| ≤ h
sup|Φ̃^(j+1)|, the supremum over [2.32, 3.44]. For j + 1 = 1, 2, 3 the supremum is at most 0.9442, 0.344 and 0.376, the
bounds of the absolute values of J̃, K̃ and L̃ in the row [7.17, 7.2] of [[sec:tab-bg-ray-defects]] (at u = 7.2, J̃, K̃
and L̃ are Φ̃′, Φ̃″ and Φ̃‴), and for j + 1 = 4 it is at most 0.3182, the sum of the absolute values of the Chebyshev
coefficients of Φ̃⁗ on [2.32, 3.44] ([[lem:bg-tools]] (a)). By direct evaluation, to within 10⁻¹⁰,

    Φ̃(ρ_m) = 1.8613729013,   Φ̃′(ρ_m) = 0.8111250646,   Φ̃″(ρ_m) = 0.2026504300,   Φ̃‴(ρ_m) = −0.2475621243,

and |Φ^(j) − Φ̃^(j)| ≤ ε_j, (ε₀, ε₁, ε₂, ε₃) = (8.69 × 10⁻⁷, 1.68 × 10⁻⁶, 6.10 × 10⁻⁶, 3.65 × 10⁻⁵) at u = u2
([[prop:bg-rays]]). This gives the first four rows of the table below. Each later row follows from the rows above it,
from ρ ∈ [2.7734, 2.7737], μ3 ∈ [0.82211214, 0.82211297] ([[prop:bg-nprime]] (ii)) and R ∈ [1.861, 1.861441] (by (a)), by
the enclosure rule of [[lem:bg-tools]] (d), applied to f1 = 1 − 3/(2ρ²), a = f1/2, a′ = 3/(2ρ³), a″ = −9/(2ρ⁴), f3(Φ) = 1
− μ3/Φ², h3(Φ) := 1/(Φ³ − μ3Φ), h3′(Φ) = −(3Φ² − μ3)h3(Φ)²,

    ψ_III = ln Φ′ + ln f1 − ln f3(Φ),        ψ_III′ = aΦ″/Φ′ + a′ − 2μ3aΦ′h3(Φ),
    ψ_III″ = a(a′Φ″/Φ′ + a(Φ‴/Φ′ − (Φ″/Φ′)²) + a″ − 2μ3(a′Φ′h3(Φ) + aΦ″h3(Φ) + aΦ′²h3′(Φ)))

(the derivatives in v̂, Ψ_0, Ψ_1 and Ψ_2 = a𝒟Ψ_1 of [[eq:bg-psi3]] written out), q = e^(ψ_III), u = 1 − q, m = μ3/R², w =
q(1 − m), and n0, A0, A1, A2, A3 and Γ/E² = A0 + A1ψ_III′ + A2ψ_III′² + A3ψ_III″ in the form written in
[[eq:margins-gamma-form]]. Every entry is rounded outward, and later rows use the printed entries.

| quantity | enclosure | quantity | enclosure |
|---|---|---|---|
| Φ | [1.861230, 1.861516] | ψ_III | [−0.1555110, −0.1552307] |
| Φ′ | [0.8110717, 0.8111784] | ψ_III′ | [0.06163544, 0.06183038] |
| Φ″ | [0.2025879, 0.2027130] | ψ_III″ | [−0.03252944, −0.03228970] |
| Φ‴ | [−0.2476464, −0.2474778] | q | [0.8559776, 0.8562177] |
| f1 | [0.8049857, 0.8050280] | u | [0.1437823, 0.1440225] |
| a | [0.4024928, 0.4025140] | m | [0.2372643, 0.2373771] |
| a′ | [0.07029311, 0.07031594] | w | [0.6527881, 0.6530679] |
| a″ | [−0.07606108, −0.07602817] | n0 | [0.04255919, 0.04307245] |
| f3(Φ) | [0.7626815, 0.7627548] | (2 − w)(1 − w)² | [0.1621192, 0.1624147] |
| h3(Φ) | [0.2032328, 0.2033656] | A0 | [7.890107, 8.007751] |
| h3′(Φ) | [−0.3959414, −0.3952924] | A1 | [49.47565, 49.91199] |
|  |  | A2 | [483.3100, 484.9544] |
|  |  | A3 | [72.78488, 72.95588] |
|  |  | Γ/E² | [10.40240, 10.59761] |

Since w < 1 and 2 − w > 0 on the box, [[eq:margins-gamma-form]] applies at P, and Γ/E² ≥ 10.4024.

(c) On the seed region Γ/E² ≥ 0.048 by [[prop:bg-seed]] (c) and [[prop:margins-seed]] (b); the rest is (b).

(d) By [[lem:bg-reduction]] (f), a point of Σ_τ0 with R ≤ R_* lies on a ray ρ ∈ [2.321, R_*] with R = T(ρ) := v̂(ρ) +
0.68, and T is increasing. By the proof of [[prop:bg-slice]], for ρ ∈ [ρ_u2, R_*] the point lies at the parameter u =
u_s(ρ) ∈ [u1, u2] of its ray, u_s is strictly decreasing (∂_u(Ψ − T) = G < 0 and ∂_ρ(Ψ − T) < 0), u_s(ρ_u2) = u2 since
g(ρ_u2) = 0, and u_s(R_*) = u1 by the definition of R_*. So a point with R_u2 < R < R_* has u1 < u < u2, where ℬ(u) > 0,
and there Ric(g0) ≠ 0 by [[eq:two-dust-limit]]. A band {R1 < R < R2} on which the background is vacuum therefore does not
meet {R_u2 < R < R_*}, and it lies in {0.70 ≤ R ≤ R_u2} or in {R ≥ R_*}. ∎

<!-- Part 3. Block 3.2: replaces cor:loc-charge-seed, statement and proof (chapter lines 390-404). -->

**Corollary {#cor:loc-charge-seed}** (Momentum seeds on Σ_τ0.) Let U be a band of Σ_τ0 on which the background is vacuum.
Then Γ > 0 on U, so Q(δ) < 0 for every nonzero momentum seed δ on U, and for ε small no vacuum data on Σ_τ0 of the form
bg + εδ + O(ε²), equal to the background's outside a compact subset of U, exist.

*Proof.* On Σ_τ0, qf < 1, so Y0 = K^l_l/3 < 0 ([[lem:racz-split-formulas]] (b)). By [[prop:bg-region-three-end]] (d), U
lies in region III, {0.70 ≤ R ≤ R_u2}, or in {R ≥ R_*}. In region III, Γ > 0 by [[prop:bg-region-three-end]] (c). On {R ≥
R_*} the points lie in region I ([[lem:margins-region-one]] (c)), where ψ = 0 and Γ/E² = 4R³μ/(R² + μ) > 0
([[lem:margins-gamma-form]]). Then [[cor:loc-charge-momentum]] and [[prop:loc-projection]] (a) apply; a band of Σ_τ0 on
which the background is vacuum has closure in a vacuum region after shrinking it slightly around the compact support. ∎

<!-- Part 3. Block 3.3: in thm:charge-sign, item (a) (chapter lines 651-653) becomes: -->

(a) *Momentum seeds.* If δ ≠ 0 has δγ = 0, then Q(δ) < 0 and no such vacuum data exist for ε small. With matter obeying
the dominant energy condition none exist if f ≥ 0 on U; if U meets {f < 0}, such data exist with outgoing radial null
dust.

<!-- Part 3. Block 3.4: in sec:loc-setting (chapter lines 31-32), the sentence "Its *seed region* is {0.70 ≤ R ≤
1.861}; it lies in region III ([[prop:bg-seed]] (a)), and there f < 0 exactly where R < √μ3, and √μ3 ∈ (0.9066,
0.9068)." becomes: -->

Region III meets Σ_τ0 in {0.70 ≤ R ≤ R_u2}, 1.8614372 ≤ R_u2 ≤ 1.8614410 ([[prop:bg-seed]] (a),
[[prop:bg-region-three-end]] (a)); there f < 0 exactly where R < √μ3, and √μ3 ∈ (0.9066, 0.9068). Its part {0.70 ≤ R ≤
1.861} is the *seed region*.

<!-- Part 3. Block 3.5: in thm:bg-margins (b) (chapter lines 1112-1114), "where 1.861394 ≤ R_u2 ≤ 1.861466" becomes
"where 1.8614372 ≤ R_u2 ≤ 1.8614410", the last clause "and Γ > 0 on the seed region." becomes "and Γ > 0 on the whole
of region III ∩ Σ_τ0, with Γ/E² ≥ 10.40 for 1.861 ≤ R ≤ R_u2.", and the proof's "(b) is [[prop:bg-seed]]" becomes: -->

(b) is [[prop:bg-seed]] and [[prop:bg-region-three-end]]

<!-- Part 3. Block 3.6: the paragraph after the proof of prop:margins-seed (chapter lines 1702-1703) becomes: -->

By [[prop:bg-seed]] (c), the background itself lies in the tube of (b), which gives Γ > 0 on its seed region; with
[[prop:bg-region-three-end]] this gives Γ > 0 on all of region III, and so [[cor:loc-charge-seed]] there.
