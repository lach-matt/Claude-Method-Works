### The constants sharpened a third time {#sec:tl5-hft}

This section sharpens the constants of [[sec:tl5-hfs]] in two ways and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with
them. First, the smallness condition is weighted: the low quantities at a point are bounded by the weighted energies
with the weighted recovery constant, the terms with ϱ and η₀ being kept apart ([[lem:tl5-hft-small]] (a)), or the
absorption of the nonlinear terms in the recovery is weighted as well ([[lem:tl5-hft-small]] (b)). Second, the Sobolev
inequalities on the faces are proved intrinsically on the leaves, through the action of the rotations on the tensors
over S³, without passing to Euclidean components ([[lem:tl5-hft-leaf]], [[lem:tl5-hft-face]]). The closing conditions are
[[eq:tl5-hft-closing]] and [[eq:tl5-hf4t-closing]]; those of the earlier theorems remain valid, and any of them may be
used. Throughout, N ≥ 4, μ ∈ (0, 1] and the notation is that of [[sec:tl5-hfs]].

**Lemma {#lem:tl5-hft-leaf}** (An intrinsic Sobolev inequality on the leaves.) Let α, β, ρ > 0 be numbers, h₀ := α² du² +
β² dv² + ρ² γ₀, and |·|₀ the norm it induces on tensors at the points of a leaf S_(u,v) := {(u, v)} × S³. For r ≥ 0 and j
∈ ℕ let e_j(r) be the multiplicity of the irreducible representation [j] of spin j of SU(2) in (2[0] ⊕ [1])^(⊗r), and for
j₁, j₂ ∈ (1/2)ℕ with j₁ + j₂ ∈ ℕ put m_(j₁j₂)(r) := Σ_(j=|j₁−j₂|)^(j₁+j₂) e_j(r) and

    C_(E,r)² := (1/(2π²)) Σ_(j₁,j₂) (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r) / (1 + 2j₁(j₁ + 1) + 2j₂(j₂ + 1))².   {#eq:tl5-hft-ce}

The series converges, and C_(E,0)² = C_(S³)² = 1/12. For every C² covariant tensor field A of rank r on S_(u,v) and every
ω ∈ S³, with the sum over the words J of length at most two in the six rotations,

    |A(ω)|₀² ≤ 6 C_(E,r)² Σ_(|J|≤2) ∫_(S³) |ℒ^J A|₀² dω.                                               {#eq:tl5-hft-leaf}

*Proof.* Let E be the bundle over S³ of the covariant r-tensors at the points of S_(u,v), with the metric h₀. The group
SO(4) acts on S³ by rotations, and on E by pullback, as its elements fix ∂_u and ∂_v and preserve γ₀; the action
preserves h₀ and the measure dω, so it is unitary on L²(S³, E), which we complexify. The fields K_ab generate the
rotations in the planes of X_a, X_b, and ℒ_(K_ab) is the derivative of this action along K_ab; it is skew-adjoint on
L²(S³, E). The fiber at the point o = (1, 0, 0, 0) is E_o = (ℝ du ⊕ ℝ dv ⊕ T*_o S³)^(⊗r), on which the isotropy group
SO(3) acts trivially on du and dv and by its standard representation, of spin one, on T*_o S³; so E_o ≅ (2[0] ⊕ [1])^(⊗r)
as a representation of SO(3).

The irreducible representations of SO(4) are the π = (j₁, j₂) of SU(2) × SU(2) with j₁ + j₂ ∈ ℕ, of dimension (2j₁ +
1)(2j₂ + 1), and the isotropy group of o is the diagonal SU(2), on which (j₁, j₂) restricts, by the Clebsch–Gordan
rule, to [|j₁ − j₂|] ⊕ ⋯ ⊕ [j₁ + j₂]. By the Peter–Weyl theorem and Frobenius reciprocity, L²(S³, E) is the orthogonal
sum of the isotypic subspaces V_π, each finite-dimensional, made of smooth sections, of dimension dim π · dim
Hom_(SO(3))(π, E_o) = (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r). The operator Ω := −Σ_(a<b) ℒ_(K_ab)² is the Casimir operator of
the invariant form for which the K_ab are orthonormal; on V_π it is the number c_π := 2j₁(j₁ + 1) + 2j₂(j₂ + 1).
Indeed, with L₁ := K₂₃, L₂ := −K₁₃, L₃ := K₁₂ and M_i := K_(i4), the fields J_i^± := (L_i ± M_i)/2 satisfy
[J₁^±, J₂^±] = −J₃^± and the cyclic relations, and [J_i⁺, J_l⁻] = 0; so they span the two copies of su(2) in so(4),
of spins j₁ and j₂ on π, −Σ_i (J_i⁺)² and −Σ_i (J_i⁻)² are j₁(j₁ + 1) and j₂(j₂ + 1) on V_π, and Σ_(a<b) K_ab² =
Σ_i (L_i² + M_i²) = 2 Σ_i ((J_i⁺)² + (J_i⁻)²). (On the representation ℝ⁴ = (1/2, 1/2) both sides are −3, each K_ab²
being minus the projection onto its plane, and on the functions of degree n, (n/2, n/2), they are −n(n + 2), the
eigenvalue of the Laplacian of γ₀.)

For an orthonormal basis (s_k) of V_π the function Σ_k |s_k(ω)|₀² does not depend on the basis, so it is invariant under
SO(4), which acts transitively on S³; its integral is dim V_π, so it is dim V_π/(2π²). Hence for A_π ∈ V_π, by the
Cauchy–Schwarz inequality, |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖², ‖·‖ the norm of L²(S³, E). Writing A = Σ_π A_π and using
the Cauchy–Schwarz inequality over π,

    |A(ω)|₀ ≤ Σ_π (dim V_π/(2π²))^(1/2) (1 + c_π)⁻¹ ‖(1 + Ω) A_π‖ ≤ C_(E,r) ‖(1 + Ω) A‖,

the series C_(E,r)² converging because m_(j₁j₂)(r) ≤ 5^r and vanishes unless |j₁ − j₂| ≤ r, so that its terms with
j₁ ≥ 1 are at most 5^r (2j₁ + 2r + 1)² / (2j₁²)² for at most 2r + 1 values of j₂. As ℒ_(K_ab) is skew-adjoint, ‖(1 + Ω)
A‖² = ‖A‖² + 2 Σ ‖ℒ_(K_ab) A‖² + ‖Σ ℒ_(K_ab)² A‖² ≤ 6 Σ_(|J|≤2) ‖ℒ^J A‖², by the Cauchy–Schwarz inequality over the six
fields. For r = 0, m_(j₁j₂)(0) = 1 if j₁ = j₂ and 0 otherwise, and with n := 2j₁ the series is Σ_n 1/(2π²(n + 1)²) =
1/12. ∎

**Lemma {#lem:tl5-hft-face}** (The Sobolev inequalities on the faces, intrinsic.) Let h₀ be as in [[lem:tl5-hft-leaf]],
with numbers α, β, ρ fixed for each face Σ₁(a, b), in (c) the same for all the faces Σ₁(t, b) with one t, and at each
point let 𝔳₀ := sup |X|/|X|₀ and 𝔴₀ := sup |X|₀/|X| over the nonzero vectors X, |X| the norm of k. Then:

(a) [[eq:tl5-hf-cs-r]] holds with 6 C_(E,r)², 𝔳₀ and 𝔴₀ in place of 6 C_(S³)² 𝔭_r, 𝔳 and 𝔴;

(b) [[lem:tl5-hf-sobolev]] holds with C_S and C_(S,0) replaced by C_S^E and C_(S,0)^E, where

    C_S^E(p)² := 6 C_(E,2)² 𝔴₀(p)⁴ sup_(Σ₁(a,b)) 𝔳₀⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),
    C_(S,0)^E(p)² := 6 C_(E,2)² 𝔴₀(p)⁴ sup_(S_a) 𝔳₀⁴;                                                    {#eq:tl5-hft-cs}

(c) [[lem:tl5-hf4-face]] holds with |A|₀ in place of |A_e| in ⟦·⟧_(2,∞) and ⟦·⟧_(∞,2), with 6 C_(E,r)² in place of
𝔭_r/2 in (b), and with 𝔳₀ and 𝔴₀ in place of 𝔳 and 𝔴 in 𝔵_r(t), 𝔱_r(t), 𝔪(t) and in (a).

*Proof.* For a tensor A of rank r at a point, the components of A in a frame orthonormal for h₀ and in one orthonormal
for k differ by the action of a matrix in each slot, whose operator norm is 𝔴₀ in one direction and 𝔳₀ in the other;
so |A| ≤ 𝔴₀^r |A|₀ and |A|₀ ≤ 𝔳₀^r |A|, as in the proof of [[lem:tl5-hf-khat]]. The coefficients of h₀ are constant,
so ℒ_(∂_γ) h₀ = 0 and ℒ_K h₀ = 0 for the rotations K; and ∂_γ commutes with the rotations. So along the curves γ_ω of the
proof of [[lem:tl5-hf-sobolev]], (d/dv)|B|₀² = 2⟨B, ℒ_(∂_γ) B⟩₀ ≤ |B|₀² + |ℒ_(∂_γ) B|₀² for every tensor field B, and
ℒ_(∂_γ) commutes with ℒ^J. In the proofs of [[lem:tl5-hf-sobolev]], of [[eq:tl5-hf-cs-r]] and of [[lem:tl5-hf4-face]],
replace the components A_e, the inequality [[eq:tl5-hf-sphere]] for each component and the passage from K(A_e) to
(ℒ_K A)_e, which produce 6C_(S³)² 𝔭_r and the factors 𝔳 and 𝔴, by |A|₀, by [[eq:tl5-hft-leaf]] applied to A and to
ℒ_(∂_γ) A on the leaf through γ_ω(v), and by the two comparisons above; the rest of each proof holds as written. For
(c), |f| ≤ |X| |Y| ≤ 𝔴₀^(r_X + r_Y) |X|₀ |Y|₀ ≤ max(1, 𝔴₀)⁶ |X|₀ |Y|₀. ∎

In what follows, C_S, C_(S,0), C₁, C_(1,ϱ), C_(1,0), C_(0,0) and their variants of [[sec:tl5-hfg]] and [[sec:tl5-hfs]],
and at level four 𝔵_r(t), 𝔱_r(t), 𝔪(t) and [𝔳^(2r)]_t, denote either the merged constants or those formed by
[[lem:tl5-hft-face]], that is with 6 C_(E,r)² in place of 6 C_(S³)² 𝔭_r (so 258 C_(E,3)² in place of 258 C_(S³)² 𝔭₃ in
C₁, 516π² C_(E,3)² in place of 516π² C_(S³)² 𝔭₃ in C_(1,0), 6 C_(E,r)² in place of 𝔭_r/2 in the bounds of ⟦·⟧_(2,∞))
and with 𝔳₀, 𝔴₀ in place of 𝔳, 𝔴; the same choice throughout. Every statement below holds for either choice, as their
proofs use the Sobolev inequalities only through their forms.

**Lemma {#lem:tl5-hft-small}** (The low quantities for the smallness.) Let g, h, p, a, b, ϱ(p) and η₀(p) be as in
[[lem:tl5-hfs-linfty]].

(a) If 𝔰 ≤ 𝔰₀^♮ on Q(a, b), with 𝔰₀^♮ as there, then, with the constants of [[eq:tl5-hfg-cinf]] and
[[eq:tl5-hfs-linfty]],

    𝔰(p) ≤ μ^(−N/2) C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀(p).   {#eq:tl5-hft-small}

(b) Let k₃^♮(μ) := (8/5) max_(|C|≤N−1) (𝔠^♮_(|C|)(μ) + Σ_(J≠C) μ^((|C|−|J|)/2) ‖𝔔_CJ‖ (𝔠^♮_(|J|)(μ) + 1)) and 𝔰₀^μ :=
min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^♮(μ))). If 𝔰 ≤ 𝔰₀^μ on Q(a, b), then at every point of Q(a, b) and for 0 ≤ j ≤ N − 1,
M_g^(j) ≤ 2(k₁^(j,μ) + 1) 𝒥_g + 2k₂ ϱ(p), the second inequality of [[eq:tl5-hfs-linfty]] holds at p for 0 ≤ m ≤ N − 4,
and

    𝔰(p) ≤ μ^(−N/2) (C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2) + C_((∞,ϱ),μ)^(N−4)(p) ϱ(p)
                     + C_((∞,0),μ)^(N−4)(p) η₀(p)).                                                  {#eq:tl5-hft-smallb}

*Proof.* (a) Every low quantity Φ of order o, other than H, satisfies |Φ(p)| ≤ μ^(−(o+2)/2) E_Φ + R_Φ, with E_Φ, R_Φ as
follows. For Ψ_B, |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] gives |Ψ_B(p)| ≤ C_S (Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂)^(1/2) + C_(0,0)
η₀(p) ≤ μ^(−(|B|+2)/2) C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p), as μ^(|B|+2) ≤ μ^(|JB|); and |H(p)| ≤ 2|h(p)|. For D̂Ψ_B, |B| ≤
N − 3, apply the first-order step of the proof of [[lem:tl5-hfs-linfty]] without the weight: at the points of the face,
by [[eq:tl5-hfs-m2]] and the bounds of the remainders there, |ℒ^J D̂Ψ_B| ≤ μ^(−(|B|+3)/2) (1 + 6Λ₂^μ) 𝒥_g and |D̂ℒ^J
D̂Ψ_B| ≤ μ^(−(|B|+3)/2) (2(k₁^μ + 1) + 6√2 Λ₂^μ) 𝒥_g + 2k₂ ϱ(p), and on S_a, |ℒ^J D̂Ψ_B| ≤ (1 + 6Λ₂) η₀(p); with (x + y)²
≤ 2x² + 2y² as there this gives |D̂Ψ_B(p)| ≤ μ^(−(|B|+3)/2) C₁^♮ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^g η₀(p). For
D̂²Ψ_B, |B| ≤ N − 4, the bound at p of [[lem:tl5-hf-recovery]], as used in the proof of [[lem:tl5-hf-linfty]], is a
linear combination of jets Ψ_C, D̂Ψ_C with |C| ≤ |B| + 1, plus k₂ ϱ(p), plus the nonlinear terms, which are at most k₃^♮
𝔰(p)². Inserting the bounds just found for the jets, their parts with ℰ_g(p) give at most μ^(−(|B|+4)/2) k₁^(N−4,μ)
(2𝔐)^(1/2) max(C_S, C₁^♮) ℰ_g(p)^(1/2), with the weights counted as in the proof of [[lem:tl5-hfs-linfty]], and their
parts with ϱ(p) and η₀(p) at most k₁^(N−4) (2𝔐)^(1/2) (C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)^g) η₀(p)), the coefficients
being those of k₁^(N−4). As μ^(−(o+2)/2) ≤ μ^(−N/2) for every low quantity, the maximum over them gives 𝔰(p) ≤
(1/2)(μ^(−N/2) C_(∞,μ)^(N−4) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(N−4) ϱ(p) + C_(∞,0)^(N−4) η₀(p)) + k₃^♮ 𝔰(p)², and k₃^♮ 𝔰(p) ≤ 1/2
gives [[eq:tl5-hft-small]].

(b) In the proof of [[lem:tl5-hfs-linfty]], the nonlinear terms of the bound of μ^((|C|+1)/2) |D̂²Ψ_C| are sums over the
monomials of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, multiplied by 𝔔_CJ, and of H^(αβ) D̂_αD̂_βΨ_J, |J| < |C|. In a
monomial whose background factors carry b letters, the factor Φ bounded there by 𝔧 has order at most |J| − b + 2, and at
most |J| − b + 1 unless Φ = D̂²Ψ_(C′) with |C′| = |J| − b; so μ^((|C|+1)/2) |Φ| ≤ μ^(b/2) (2𝒥_g + M_g^(j)) for |C| ≤ j,
as |C| ≥ |J|, and μ^((|C|+1)/2) = μ^((|C|−|J|)/2) μ^((|J|+1)/2). By [[eq:tl5-hfs-sum]] with ν′ = μ these terms are at
most k₃^♮(μ) 𝔰 (2𝒥_g + M_g^(j)), and k₃^♮(μ) 𝔰 ≤ 1/2 gives the bound of M_g^(j) as there. In the step on second
derivatives at low levels the same count gives k₃^♮(μ) 𝔰(p) 𝔰_g^(m)(p) for the nonlinear terms; the other steps do not
use the smallness, and the first-order step uses M_g in place of [[eq:tl5-hfs-m2]], μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ M_g. So
the second inequality of [[eq:tl5-hfs-linfty]] holds, and [[eq:tl5-hft-smallb]] follows from 𝔰 ≤ μ^(−N/2) 𝔰_g^(N−4). ∎

**Lemma {#lem:tl5-hft-products}** (The quadratic terms under the weighted absorption.) In the setting of
[[lem:tl5-hft-small]] (b), with 𝔰 ≤ 𝔰₀^μ on Q(a, b), [[lem:tl5-hfs-products]] holds with μ^(−1/2) 𝔠^♮_n(μ) in place
of μ^(n/2) 𝔠^♮_n and μ^(−1/2) (𝔠^♮_(|J|)(μ) + 1) μ^((n−|J|)/2) in place of μ^(n/2) (𝔠^♮_(|J|) + 1) in the terms with
ϱ(p), and [[lem:tl5-hfs-mixed]] holds as stated.

*Proof.* In the proof of [[lem:tl5-hfs-products]], the bound of a factor Φ₂ = D̂²Ψ_C becomes |Φ₂| ≤ μ^(−ℓ_E(Φ₂)/2)
(𝔨_A 𝒥_g + 2k₂ ϱ(p)), by [[lem:tl5-hft-small]] (b); the other bounds hold as there, [[lem:tl5-hft-small]] (b) giving
those of 𝔰_P⁰ and 𝔰_P. The term with ϱ(p) of a monomial whose background factors carry b letters is then at most ν
𝔰^(q−1) μ^((n − ℓ_E(Φ₂))/2) 2k₂ ϱ(p). If b = 0, ℓ_E(Φ₂) ≤ n; if b ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1 ≤ n − b + 1; so μ^((n −
ℓ_E(Φ₂))/2) ≤ μ^(−1/2) μ^(b/2), and [[eq:tl5-hfs-sum]] with ν′ = μ gives the first inequality. For |J| < n the term
with ϱ(p) of μ^(n/2) |H| |D̂²Ψ_J| is at most μ^((n−|J|−1)/2) 𝔰 2k₂ ϱ(p). In the proof of [[lem:tl5-hfs-mixed]], ‖M_g‖_Σ
≤ λ_t^μ 𝔍_g + ς_t ϱ follows from the bound of M_g^(3) in [[lem:tl5-hft-small]] (b). ∎

**Definition {#def:tl5-hft-constants}** (The constants sharpened a third time.) In the setting of
[[def:tl5-hfs-constants]], with its constants formed with the choice of Sobolev constants made above, fix one of the
two options (a), (b) of [[lem:tl5-hft-small]], and put, with k₃^♮(μ) as there,

    option (a):  𝔰₁^t := 𝔰₁^♮,   ε_(w,t) := ε_(w,s),
                 𝔰_(*,t) := sup_(p∈D^κ) (2 C_(∞,μ)^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_t + C_(∞,ϱ)^(N−4)(p) ϱ(p)
                            + C_(∞,0)^(N−4)(p) η₀);
    option (b):  𝔰₀^μ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮(μ))),   𝔰₁^t := min(𝔰₀^μ/2, c_* κ_m/2, 𝔰_θ),
                 ε_(w,t) := 𝒮[s_N[2R̂ic] + (1/4) μ^(−1/2) 𝔤_(𝒥,s) k₂ ϱ],
                 𝔰_(*,t) := sup_(p∈D^κ) μ^(−N/2) (2 C_(∞,μ)^(N−4)(p) e^(φ(p)/2) A_t + C_((∞,ϱ),μ)^(N−4)(p) ϱ(p)
                            + C_((∞,0),μ)^(N−4)(p) η₀);
    A_t := √2 δ_w + 2ε_(w,t) + 2ε_(M,s),      B_t := B_s,      𝔯_t := 𝔯_s.                        {#eq:tl5-hft-constants}

**Proposition {#prop:tl5-hft-bootstrap}** (The a priori estimate with the constants sharpened a third time.) In the
setting of [[def:tl5-hft-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N)
and that 𝔯_t ≤ 1/4, η₀ < 𝔰₁^t and 𝔰_(*,t) < 𝔰₁^t. Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤
2A_t for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,t) on D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_t + B_t Y_s(g)².                                                                          {#eq:tl5-hft-h1}

*Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hfs-bootstrap]], with 𝔰₁^t, A_t and 𝔰_(*,t) in place of
𝔰₁^♮, A_s and 𝔰_(*,s), and with [[eq:tl5-hft-small]] (option (a)) or [[eq:tl5-hft-smallb]] (option (b)) in place of the
bound at μ = 1: for p ∈ D^κ_σ, ℰ_g(p) ≤ e^(φ(p)) Y_σ(g)² ≤ 4 e^(φ(p)) A_t², as φ is at most φ(p) on Σ₁(τ₁(p), τ₂(p)),
so 𝔰(p) ≤ 𝔰_(*,t) < 𝔰₁^t, which is at most half the threshold of [[lem:tl5-hft-small]] in either option. The argument
there gives 𝔰 ≤ 𝔰_(*,t) on D^κ_s, |h|_k̂ < κ_m/2 and θ_H ≤ ϑ.

*Steps 2 and 3.* Option (a): 𝔰 ≤ 𝔰₀^♮ on D^κ_s, so Steps 2 and 3 of the proof of [[prop:tl5-hfs-bootstrap]] apply as
written. Option (b): 𝔰 ≤ 𝔰₀^μ on D^κ_s, and those steps apply with [[lem:tl5-hft-small]] (b) and [[lem:tl5-hft-products]]
in place of [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]]: the terms with ϱ of the family of level j become
μ^(−j/2) μ^(−1/2) Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1) 2k₂ 𝔰 ϱ, which with the weights μ^|I|
contribute at most 2Ω̂² (1/4) μ^(−1/2) 𝔤_(𝒥,s) k₂ ϱ (√e_o + √c √e_i), and so give ε_(w,t) in place of ε_(w,s). In both
options this gives (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,t) + ε_(M,s)) + 𝔯_t Y_s² + (S_(F,s) + S_(M,s)) Y_s³,
and the conclusion follows as there. ∎

**Theorem {#thm:tl5-hft}** (Existence close to an explicit background, with the constants sharpened a third time.) In
the setting of [[thm:tl5-hfs]] (N ≥ 6), with the choices of [[def:tl5-hft-constants]], suppose: (a) η₀ < 𝔰₁^t; (b) the
rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N); (c) 𝔯_(w,s) ≤ 1/4, 𝔰_(*,t) < 𝔰₁^t and the closing
condition

    4 A_t B_t = 8 (√2 δ_w + 2ε_(w,t)) S_(F,s) < 1.                                                  {#eq:tl5-hft-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_t and 𝔰_(*,t) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hfs]] applies with A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]], [[eq:tl5-hft-h1]]
and [[eq:tl5-hft-closing]] in place of A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]], [[eq:tl5-hfs-h1]] and
[[eq:tl5-hfs-closing]]; it uses only 𝔰 ≤ 𝔰_(*,t) < 𝔰₁^t ≤ min(1/16, 𝔰_θ) and the bound Y_σ ≤ 2A_t. ∎

**Theorem {#thm:tl5-hf4t}** (Level four, with the constants sharpened a third time.) In the setting of
[[thm:tl5-hf4s]], with the choices of [[def:tl5-hft-constants]] for N = 4, suppose: (a) η₀ < 𝔰₁^t; (b) the rates a_o,
a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) 𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4, 𝔰_(*,t) < 𝔰₁^t and the closing condition

    4 A_t B_t = 8 (√2 δ_w + 2ε_(w,t) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1.                          {#eq:tl5-hf4t-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_t and 𝔰_(*,t) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4s]] applies with A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]] for N = 4,
[[eq:tl5-hft-h1]] and [[eq:tl5-hf4t-closing]] in place of A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]],
[[eq:tl5-hfs-h1]] and [[eq:tl5-hf4s-closing]]. In option (b), the bound [[eq:tl5-hf4-m2]] used in the proof of
[[lem:tl5-hf4-persistence]] is replaced by |D̂²Ψ_B| ≤ μ^(−2) (2(k₁^μ + 1) 𝒥₁ + 2k₂ ϱ), |B| ≤ 3, from the bound of
M_g^(3) in [[lem:tl5-hft-small]] (b), as 𝒥_g ≤ 𝒥₁; that proof needs only some such bound by a constant. ∎

**Remark {#rem:tl5-hft-what}** (What the third sharpening changes.) In option (a) the smallness 𝔰_(*,t) < 𝔰₁^t carries
the weighted constant C_(∞,μ)^(N−4), with k₁^(N−4,μ) and C₁^♮, in its term with A_t, and the constants of
[[eq:tl5-hfg-cinf]] only in its terms with ϱ and η₀; the factor μ^(−N/2) remains, as the low quantities of order N − 2
are bounded through the energies of level N. In option (b) the threshold 𝔰₁^t is formed with k₃^♮(μ), whose
nonlinear constants carry the weights μ^(b/2) of the background letters and μ^((|C|−|J|)/2) of the couplings 𝔔_CJ, at
the cost of the factor μ^(−N/2) on the terms with ϱ and η₀ of 𝔰_(*,t) and of μ^(−1/2) 𝔤_(𝒥,s) in place of 𝔤_(ϱ,s) in
ε_(w,t). With the Sobolev constants of [[lem:tl5-hft-face]], every constant formed from the Sobolev inequality on a
face, at level four also 𝔛, carries 6C_(E,r)² in place of 6C_(S³)² 𝔭_r, and these constants, 𝔜 and 𝔪 carry the operator
norms 𝔳₀, 𝔴₀ of the comparison of k with h₀ in place of the Euclidean component norms 𝔳, 𝔴; the numbers α, β, ρ of h₀
are free for each face, in (c) for each t. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hft]] and [[thm:tl5-hf4t]] are established in this
paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The sections sec:tl5-hf, sec:tl5-hf4, sec:tl5-hfg and sec:tl5-hfs stay as they are, and all their closing conditions
remain valid; this section is added beside them, for the reason recorded for sec:tl5-hfg. Old texts are quoted exactly
from chapters/87-ten-l5.md at HEAD f754985f, where sec:tl5-hfs is merged (87:5426–5758, merge 53bd18fb). Line numbers
serve only to find the place. Each new text replaces its old text as a whole, with the line breaks shown.

*1. Where the section goes.* The section above, from its heading ("The constants sharpened a third time", label
sec:tl5-hft) through the last line of [[rem:tl5-hft-what]], is inserted at the end of [[ch:ten-l5]], after the last line
of [[rem:tl5-hfs-what]] (line 5759 once item 2 is applied), with one blank line before it, as a sibling "###" section
after sec:tl5-hfs. It cites results of the four earlier sections as they stand and the proofs of prop:tl5-hfs-bootstrap,
thm:tl5-hfs, thm:tl5-hf4s and lem:tl5-hf4-persistence with the replacements it states. It defines the labels listed in
the crosswalk rows, none defined elsewhere. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfs-what]] (lines 5757–5758).* Old:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfs]] and [[thm:tl5-hf4s]] are established in this
paper for no background at 10 l5.

New:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfs]] and [[thm:tl5-hf4s]] are established in this
paper for no background at 10 l5. [[sec:tl5-hft]] sharpens the smallness condition and the Sobolev constants further
([[thm:tl5-hft]], [[thm:tl5-hf4t]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. "Proved" refers to the section above; "deduced" marks statements about the method that no proof here
establishes; "computed" marks numbers I evaluated (floating point).

*Closing conditions and smallness (proved).*

    level ≥ 6:  8 (√2 δ_w + 2ε_(w,t)) S_(F,s) < 1,   𝔯_(w,s) ≤ 1/4,   η₀ < 𝔰₁^t,   𝔰_(*,t) < 𝔰₁^t       (thm:tl5-hft)
    level 4:    8 (√2 δ_w + 2ε_(w,t) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1,   𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4,
                η₀ < 𝔰₁^t,   𝔰_(*,t) < 𝔰₁^t   (thm:tl5-hf4t)

S_(F,s), S_(M,s), 𝔯_(w,s), 𝔯_(M,s), ε_(M,s) are those of def:tl5-hfs-constants, formed with either Sobolev choice. The
earlier closing conditions stay valid.

*Every new factor, as a formula.*

    option (a):  𝔰₁^t = 𝔰₁^♮ (unchanged; k₃^♮ at μ = 1);  ε_(w,t) = ε_(w,s);
                 𝔰_(*,t) = sup_p (2 C_(∞,μ)^(N−4) μ^(−N/2) e^(φ/2) A_t + C_(∞,ϱ)^(N−4) ϱ + C_(∞,0)^(N−4) η₀),
                 C_(∞,μ)^(N−4) = 2 max(2C_S, C₁^♮, k₁^(N−4,μ) (2𝔐)^(1/2) max(C_S, C₁^♮))  (weighted, from sec:tl5-hfs),
                 C_(∞,ϱ)^(N−4), C_(∞,0)^(N−4) of eq:tl5-hfg-cinf (unweighted, k₁^(N−4), C₁^g, C_(1,0)^g);
    option (b):  k₃^♮(μ) = (8/5) max_(|C|≤N−1) (𝔠^♮_(|C|)(μ) + Σ_(J≠C) μ^((|C|−|J|)/2) ‖𝔔_CJ‖ (𝔠^♮_(|J|)(μ) + 1));
                 𝔰₀^μ = min(𝔰_♭, 1/(2 sup k₃^♮(μ)));  𝔰₁^t = min(𝔰₀^μ/2, c_* κ_m/2, 𝔰_θ);
                 ε_(w,t) = 𝒮[s_N[2R̂ic] + (1/4) μ^(−1/2) 𝔤_(𝒥,s) k₂ ϱ];
                 𝔰_(*,t) = sup_p μ^(−N/2) (2 C_(∞,μ)^(N−4) e^(φ/2) A_t + C_((∞,ϱ),μ)^(N−4) ϱ + C_((∞,0),μ)^(N−4) η₀);
    both:        A_t = √2 δ_w + 2ε_(w,t) + 2ε_(M,s),  B_t = 2(S_(F,s) + S_(M,s)),  𝔯_t = 𝔯_s;

    Sobolev choice E:  e_j(r) = multiplicity of spin j in (2[0] ⊕ [1])^(⊗r):
                 r = 2: (e₀, e₁, e₂) = (5, 5, 1);  r = 3: (15, 21, 8, 1);  r = 4: (51, 86, 46, 11, 1)  (computed);
                 m_(j₁j₂)(r) = Σ_(j=|j₁−j₂|)^(j₁+j₂) e_j(r);
                 C_(E,r)² = (1/(2π²)) Σ_(j₁,j₂∈ℕ/2, j₁+j₂∈ℕ) (2j₁+1)(2j₂+1) m_(j₁j₂)(r) / (1 + 2j₁(j₁+1) + 2j₂(j₂+1))²;
                 C_(E,2)² ≤ 0.8942, C_(E,3)² ≤ 3.6375, C_(E,4)² ≤ 15.710, C_(E,0)² = 1/12: the sums over 2j₁ < 3000
                 are 0.89374, 3.63536, 15.6992 (computed), and the tail is at most 5^r/(2π²(3000 − 2r)), as each term
                 is at most m_(j₁j₂)(r)/((2j₁ + 1)(2j₂ + 1)), Σ_(j₂) m_(j₁j₂)(r) ≤ 5^r, m_(j₁j₂)(r) = 0 unless
                 |j₁ − j₂| ≤ r, so that 2j₂ + 1 ≥ 2j₁ + 1 − 2r, and Σ_(n≥3000) 1/((n + 1)(n + 1 − 2r)) ≤ 1/(3000 − 2r)
                 (the values are 0.894166, 3.637471, 15.70976, computed); against C_(S³)² 𝔭_r = 196.1, 981.1, 3088.1:
                 factors 219, 270, 197 in the squares;
                 h₀ = α² du² + β² dv² + ρ² γ₀ with constants α, β, ρ chosen per face (per t at level four in (c));
                 𝔳₀² = λ_max(M), 𝔴₀² = 1/λ_min(M), M the matrix of k in the h₀-orthonormal basis (∂_u/α, ∂_v/β,
                 e_x/ρ, e_1/ρ, e_2/ρ), e_x = 2(1 − x²)^(1/2) ∂_x, e_1, e_2 the γ₀-unit fields along ∂_φ1, ∂_φ2:
                   M_uu = (2Ω̂²/c + b̂² e^(2ζ))/α²,  M_vv = 2cΩ̂²/β²,  M_ux = −b̂ e^ζ R e^(−(P+Q))/(αρ),
                   M_xx = R² e^(−2(P+Q))/ρ²,  M_11 = R² e^(2P)/ρ²,  M_22 = R² e^(2Q)/ρ²,  other entries 0;
                 the condition number of the comparison is (λ_max(M)/λ_min(M))^(1/2); it is 1 at a point where b̂ = 0,
                 P = Q = 0, α² = 2Ω̂²/c, β² = 2cΩ̂², ρ = R (the seed), and on a face it measures the variation of Ω̂, c
                 and R over the face and the departure of the leaves from roundness;
                 C_S^E² = 6 C_(E,2)² 𝔴₀(p)⁴ sup_(Σ₁(a,b)) 𝔳₀⁴ R⁻³ ((1 + 8|D̂∂_γ|²)/(2Ω̂² z̲) + 2𝔨₁),
                 C_(S,0)^E² = 6 C_(E,2)² 𝔴₀(p)⁴ sup_(S_a) 𝔳₀⁴,  C_(0,0)^E² = 86π² C_(S,0)^E²;
                 C₁^E² = 258 C_(E,3)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ₂^μ)²
                         + 4|∂_γ|² (72 (Λ₂^μ)² + 8(k₁^μ + 1)²))  (with Λ₂, k₁ at μ = 1 for the unweighted C₁^g);
                 C_(1,0)^E² = 516π² C_(E,3)² 𝔴₀(p)⁶ sup_(S_a) 𝔳₀⁶ (1 + 6Λ₂)²  (with Λ₂^μ for C_(1,0)^♮, option (b));
                 C_(1,ϱ)^E² = 258 C_(E,3)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) (𝔳₀⁶ R⁻³ 32 |∂_γ|² k₂²) ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′);
                 level 4:  𝔵_r(t) = [𝔳₀^(2r) R⁻³]_t,  𝔱_r(t) = [𝔳₀^(2r) R⁻³ max(1 + 2r²|D̂∂_γ|², 2|∂_γ|²)]_t,
                           𝔪(t) = [max(1, 𝔴₀)⁶ R^(3/2)]_t,  [𝔳⁴]_t → [𝔳₀⁴]_t,  [𝔳⁶]_t → [𝔳₀⁶]_t,
                           and 12 C_(E,r)² in place of 𝔭_r in 𝔛_(1,t), 𝔛_(2,t), 𝔛′_(2,t) (which carry (𝔭_r 𝔵_r)^(1/2)
                           or (𝔭_r 𝔵_r/2)^(1/2): 𝔭_r/2 → 6 C_(E,r)²).

*The briefed items, one by one.*

1. The smallness (proved, two options). (a) is G0e's variant: the term with A_t of 𝔰_* carries C_(∞,μ)^(N−4) (k₁^μ,
   Λ₂^μ) instead of C_∞^(N−4) (k₁, Λ₂), proved by keeping the terms with ϱ and η₀ apart at each step (the split of
   eq:tl5-hfs-m2 extended to all low quantities); 𝔰₁ is unchanged. (b) weights k₃ as well: 𝔰₁^t uses k₃^♮(μ), at the
   price of μ^(−N/2) on the ϱ- and η₀-terms of 𝔰_* and of μ^(−1/2) 𝔤_(𝒥,s) in ε_(w,t). The two cannot be combined in
   this proof (deduced): the split form needs the absorption k₃^♮ 𝔰 ≤ 1/2 at μ = 1 for the parts with ϱ, which carry
   no weight. The factor μ^(−N/2) in the term with A_t remains in both: Ψ_B with |B| = N − 2 at a point is bounded
   through energies of level N. The reader's observation on the ϱ-parts of 𝔰_P and ‖M_g‖: they enter 𝔯_(w,s), 𝔯_(M,s)
   and ε_(M,s), not the binding conditions, and are left as in sec:tl5-hfs.
2. The intrinsic Sobolev inequality (proved): lem:tl5-hft-leaf and lem:tl5-hft-face, with the SO(4)-isotypic
   decomposition, multiplicities m_(j₁j₂)(r), Casimir eigenvalues 2j₁(j₁+1) + 2j₂(j₂+1), all explicit; the comparison of
   the round norm with k is the operator-norm pair 𝔳₀, 𝔴₀ above (the condition number formula is given; its values
   need the background).
3. The word count 7^(j′/2) in 𝔤_(𝒥,s) and 𝔠^M₁ (not done). The word count: an ℓ² sum over the words frees only the
   letters on the factor in the energies, the letters on the factor at a point and on background factors keeping √7
   each, so the count would have to enter the Leibniz sums per factor; not carried out. 𝔠^M₁ = 480 + 49𝔰_♭𝔠^(3♮)₄: the
   480 is 6 · 16 · λ̂^♮₀² with λ̂^♮₀ = √5 for an inverse metric that may close a trace; a count, term by term of 2𝔮̂,
   of which inverse metrics join two distinct factors D̂h would lower it (at most to 6 · 16), and was not carried out.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hft	paper/reader/proofs/P-GRD3.md@PENDING:1	P-GRD3, section	new; at the end of ch:ten-l5, after rem:tl5-hfs-what (author: keep tightening by hand); third sharpening: weighted smallness, intrinsic Sobolev
    lem:tl5-hft-leaf	paper/reader/proofs/P-GRD3.md@PENDING:12	P-GRD3, Lemma	Sobolev on S^3 for tensor bundles via the SO(4)-isotypic decomposition; constant C_(E,r) as an explicit series
    eq:tl5-hft-ce	paper/reader/proofs/P-GRD3.md@PENDING:17	P-GRD3, display	new
    eq:tl5-hft-leaf	paper/reader/proofs/P-GRD3.md@PENDING:22	P-GRD3, display	new
    lem:tl5-hft-face	paper/reader/proofs/P-GRD3.md@PENDING:58	P-GRD3, Lemma	face Sobolev inequalities with 6 C_(E,r)^2 and the operator norms v0, w0 of k against h0 = a^2 du^2 + b^2 dv^2 + r^2 gamma0
    eq:tl5-hft-cs	paper/reader/proofs/P-GRD3.md@PENDING:67	P-GRD3, display	new
    lem:tl5-hft-small	paper/reader/proofs/P-GRD3.md@PENDING:90	P-GRD3, Lemma	low quantities for the smallness: (a) weighted energy constant, rho/eta0 apart; (b) weighted absorption k3(mu)
    eq:tl5-hft-small	paper/reader/proofs/P-GRD3.md@PENDING:96	P-GRD3, display	new
    eq:tl5-hft-smallb	paper/reader/proofs/P-GRD3.md@PENDING:104	P-GRD3, display	new
    lem:tl5-hft-products	paper/reader/proofs/P-GRD3.md@PENDING:132	P-GRD3, Lemma	lem:tl5-hfs-products and lem:tl5-hfs-mixed under the weighted absorption
    def:tl5-hft-constants	paper/reader/proofs/P-GRD3.md@PENDING:145	P-GRD3, Definition	third sharpened constants: options (a), (b) for s1^t, s_(*,t), eps_(w,t); A_t, B_t
    eq:tl5-hft-constants	paper/reader/proofs/P-GRD3.md@PENDING:156	P-GRD3, display	new
    prop:tl5-hft-bootstrap	paper/reader/proofs/P-GRD3.md@PENDING:158	P-GRD3, Proposition	(H1) with the third sharpened constants
    eq:tl5-hft-h1	paper/reader/proofs/P-GRD3.md@PENDING:163	P-GRD3, display	new
    thm:tl5-hft	paper/reader/proofs/P-GRD3.md@PENDING:179	P-GRD3, Theorem	thm:tl5-hf (N >= 6) with the third sharpened constants
    eq:tl5-hft-closing	paper/reader/proofs/P-GRD3.md@PENDING:184	P-GRD3, display	closing condition at level N >= 6: 8 (sqrt2 delta_w + 2 eps_(w,t)) S_(F,s) < 1
    thm:tl5-hf4t	paper/reader/proofs/P-GRD3.md@PENDING:192	P-GRD3, Theorem	thm:tl5-hf4 with the third sharpened constants
    eq:tl5-hf4t-closing	paper/reader/proofs/P-GRD3.md@PENDING:196	P-GRD3, display	closing condition at level 4: 8 (sqrt2 delta_w + 2 eps_(w,t) + 2 eps_(M,s)) (S_(F,s) + S_(M,s)) < 1
    rem:tl5-hft-what	paper/reader/proofs/P-GRD3.md@PENDING:206	P-GRD3, Remark	what the third sharpening changes; options (a), (b); intrinsic Sobolev constants

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfs-what, add "; points to sec:tl5-hft
(P-GRD3 item 2)".
