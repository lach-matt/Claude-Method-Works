### The poles of the inverse of the ι⁺-normal operator {#sec:sp}

This section determines the poles of ϰ ↦ N_sf(ϰ)⁻¹ ([[thm:iii-g-5-1]]) and of ϰ ↦ N_ι⁺(L̄, ϰ)⁻¹ ([[def:iii-g1-4-1]])
in the half plane {Re ϰ ≥ 2}, with their orders. Of these poles [[lem:iii-g1-4-2]] (a) states that they lie in
{Re ≥ 2}, finitely many below each bound. Their orders at real part at most 5 enter the number l_* of
[[def:iii-i10-1-1]], the bound K_ι(λ) ≤ 2l_* + 1 of [[lem:iii-j-1-2]] and the logarithmic orders that the maps 𝒮_(λ₀)
of [[sec:s23-step]] raise.

There are two results. The first holds wherever the hypotheses of [[ch:s16]] hold. Integrating the equation
N_sf(ϰ)u = f against the powers v^k reduces the poles at a point ϰ_0 with Re ϰ_0 ≥ 2, on the isotypic components of
one type, to those of the inverse of an explicit matrix polynomial built from the indicial matrix of L̃(0) and from S̄
alone ([[thm:sp-reduction]]). In particular the poles in {Re ϰ ≥ 2} are exactly the numbers μ + j, μ an indicial root
of L̂_b(0) with Re μ > 1 and j ≥ 1 an integer, and the order of each is at most the number of such roots of one type,
with multiplicity, among ϰ_0 − 1, ϰ_0 − 2, …. The second is the evaluation at the computational point of
[[def:ec-point]]: every pole of real part at most 5 is simple and lies in spec_ι⁺(L̄), and the poles are listed
([[thm:sp-spectrum]]). The orders of these poles therefore contribute exactly 1 to l_* ([[cor:sp-lstar]]). Nothing
depends on the black hole parameter, as N_ι⁺(2L_b) = N_ι⁺(2L̄) for every b ([[lem:iii-h2-3-2]]).

*Setting.* The hypotheses of [[thm:iii-g-5-1]] and of [[thm:iii-g1-3-1]] are assumed throughout, as in [[ch:s16]]; at
the computational point they are the hypotheses under which its formulas are evaluated ([[rem:ec-point-outside]]).
𝒫 is the set of poles of N_sf(·)⁻¹. By [[thm:iii-g-5-1]] (1)–(2) it is the set of ϰ at which N_sf(ϰ) is not
injective, and it does not meet {Re < 2}. Admissible pairs, 𝒳 and 𝒴 are those of [[eq:iii-g-2-6]]–[[eq:iii-g-2-7]].
For a pair admissible for every ϰ in a disc, 𝒳 does not depend on ϰ in the disc, and ϰ ↦ N_sf(ϰ) ∈ ℒ(𝒳, 𝒴) is a
polynomial of degree 2 ([[lem:iii-g-1-2]] (f)). On ℝ⁴ we write r = |x| = ρ⁻¹ and n = x/r, and t̄ is the Cartesian time.

For a type and degree τ ([[sec:iii-f1-1]]) let n_τ be the size of its indicial matrices on symmetric 2-tensors and
N_τ(ι) the matrix N_L(ι) of [[sec:iii-f1-2]], the indicial matrix of ρ⁻²(2L̄)^(0) = L̃(0)(ω, ρ∂_ρ, ∂_ω): on an
isotypic component W_π = ℂ^(n_τ) ⊗ π of type τ, L̃(0)(ω, ι, ∂_ω) acts as N_τ(ι) ⊗ Id_π. The endomorphism S̄ is
pointwise and invariant under SO(4) ([[eq:iii-f-2-2]]), so by Schur's lemma it acts on W_π as S_τ ⊗ Id_π for an
n_τ × n_τ matrix S_τ. Further N_τ(ι) = −ι² Id + ιA_τ + B_τ, and det N_τ(ι) = (−1)^(n_τ)∏(ι − μ), the product over the
roots μ of type τ listed in [[prop:iii-f1-2-3]], with multiplicity. A root is *singular* if its real part exceeds 1;
these are the entries after the semicolons of [[prop:iii-f1-2-3]], and no root has real part in (0, 1] ((a) there).
Let d_τ be the sum of dim π over the irreducible representations π of type τ: (l + 1)² at scalar type l, 2l(l + 2)
at vector type l and 2(l − 1)(l + 3) at tensor type l. For Re ϰ_0 ≥ 2 put

    K(ϰ_0) := ⌊Re ϰ_0⌋ − 2 ∈ ℕ_0.                                                                        {#eq:sp-k}

#### Jordan chains {#sec:sp-chains}

**Definition {#def:sp-chains}** (Jordan chains.) Let X, Y be Banach spaces, A(ϰ) = A_0 + ϰA_1 + ϰ²A_2 with
A_i ∈ ℒ(X, Y), and A^(i) := ∂_ϰ^iA. For ϰ_0 ∈ ℂ and N ≥ 1 let 𝒦_N(A, ϰ_0) be the space of the tuples
(u_0, …, u_(N−1)) ∈ X^N with

    Σ_(i=0)^j (i!)⁻¹ A^(i)(ϰ_0) u_(j−i) = 0,     0 ≤ j < N,                                             {#eq:sp-chain}

that is, A(ϰ)Σ_(j<N)(ϰ − ϰ_0)^ju_j = O((ϰ − ϰ_0)^N). A tuple of 𝒦_N(A, ϰ_0) with u_0 ≠ 0 is a *Jordan chain of
length N*, and p(A, ϰ_0) is the largest length of a Jordan chain (0 if A(ϰ_0) is injective). The same definitions
apply to square matrix polynomials, with X = Y a finite-dimensional space.

**Lemma {#lem:sp-pole-order}** (Pole order and chains.) Let A be as in [[def:sp-chains]], invertible for
0 < |ϰ − ϰ_0| < r, and let ϰ ↦ A(ϰ)⁻¹ ∈ ℒ(Y, X) have a pole of order p_0 at ϰ_0 (p_0 = 0 if it is holomorphic
there). Then p(A, ϰ_0) = p_0.

*Proof.* Write A(ϰ)⁻¹ = Σ_(i=1)^(p_0)(ϰ − ϰ_0)^(−i)A_(−i) + H(ϰ) with H holomorphic and A_(−p_0) ≠ 0. If p_0 ≥ 1,
choose f ∈ Y with A_(−p_0)f ≠ 0. Then U(ϰ) := (ϰ − ϰ_0)^(p_0)A(ϰ)⁻¹f is holomorphic near ϰ_0, U(ϰ_0) = A_(−p_0)f ≠ 0
and A(ϰ)U(ϰ) = (ϰ − ϰ_0)^(p_0)f. As A is a polynomial, the coefficient of (ϰ − ϰ_0)^j in A(ϰ)U(ϰ) is the left side
of [[eq:sp-chain]] for the Taylor coefficients u_j of U, and it vanishes for j < p_0; so (u_0, …, u_(p_0−1)) is a
Jordan chain and p(A, ϰ_0) ≥ p_0. Conversely, let (u_0, …, u_(N−1)) be a Jordan chain and
U(ϰ) := Σ_(j<N)(ϰ − ϰ_0)^ju_j. By [[eq:sp-chain]], g(ϰ) := (ϰ − ϰ_0)^(−N)A(ϰ)U(ϰ) is a polynomial, and
U(ϰ) = (ϰ − ϰ_0)^NA(ϰ)⁻¹g(ϰ) for 0 < |ϰ − ϰ_0| < r. The right side is O(|ϰ − ϰ_0|^(N−p_0)) and U(ϰ_0) = u_0 ≠ 0;
so N ≤ p_0. ∎

**Lemma {#lem:sp-block}** (Block triangular matrices.) Let 𝔐(ϰ) be a square matrix polynomial, block lower
triangular with square diagonal blocks D_0(ϰ), …, D_K(ϰ), and let each det D_k be a non-zero polynomial with at most
a simple zero at ϰ_0. Then dim 𝒦_N(𝔐, ϰ_0) ≤ Σ_k dim ker D_k(ϰ_0) for every N ≥ 1. If
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0), then p(𝔐, ϰ_0) ≤ 1.

*Proof.* First let K = 0 and D := D_0. As D(ϰ)⁻¹ = adj D(ϰ)/det D(ϰ) has at most a simple pole at ϰ_0,
[[lem:sp-pole-order]] gives p(D, ϰ_0) ≤ 1. Let (m_0, …, m_(N−1)) ∈ 𝒦_N(D, ϰ_0) with N ≥ 2. Then m_0 = 0, since
otherwise (m_0, m_1) would be a Jordan chain of length 2; and then [[eq:sp-chain]] for (m_j) is [[eq:sp-chain]] for
(m_1, …, m_(N−1)) ∈ 𝒦_(N−1)(D, ϰ_0). By induction on N, 𝒦_N(D, ϰ_0) consists of the tuples (0, …, 0, w) with
w ∈ ker D(ϰ_0), and has dimension dim ker D(ϰ_0). In general write each vector as (x, y), x its first block. The
block rows of [[eq:sp-chain]] belonging to the first block involve only the first blocks, 𝔐 being block lower
triangular; so (x_j) ∈ 𝒦_N(D_0, ϰ_0), and if every x_j vanishes, (y_j) ∈ 𝒦_N(𝔐′, ϰ_0), 𝔐′ the matrix formed by the
blocks 1, …, K. Hence dim 𝒦_N(𝔐, ϰ_0) ≤ dim 𝒦_N(D_0, ϰ_0) + dim 𝒦_N(𝔐′, ϰ_0), and induction on K gives the bound.
If p(𝔐, ϰ_0) ≥ 2, a Jordan chain (m_0, m_1) and the tuples (0, w), w ∈ ker 𝔐(ϰ_0), span a subspace of 𝒦_2(𝔐, ϰ_0)
of dimension dim ker 𝔐(ϰ_0) + 1, since its elements with first entry 0 are the (0, w). When
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0) this exceeds the bound. ∎

#### Moments {#sec:sp-moments}

**Definition {#def:sp-moments}** (Moments.) Let k ∈ ℕ_0, c > k + 1 and s′ ∈ ℝ. For u ∈ Ḣ^(s′,c)_b(sf_(≥−1)) the
*k-th moment* 𝔪_k(u) is the distribution on 𝕊³, with values in ℂ^15 in the frame of [[sec:iii-g-1-1]], given by

    ⟨𝔪_k(u), ψ⟩ := ⟨u, v^k ψ⟩,     ψ ∈ C^∞(𝕊³; ℂ^15),                                                   {#eq:sp-moment}

the pairing of distributions on ℝ_v × 𝕊³ with the measure |dv| dg̸ (componentwise, bilinear). It is well defined and
continuous on Ḣ^(s′,c)_b: (1 − χ_∂)u is supported in [−1, 4] × 𝕊³, where v^kψ is smooth; and near R = 0, where
v^k|dv| dg̸ = R^(−k−1)μ_b with μ_b = |dR/R| dg̸, χ_∂u lies in H^(s′)_(b,c), while R^(−k−1)ψ ∈ 𝒜^(−k−1) lies in
H^∞_(b,−k−1−ϵ) ⊂ H^(−s′)_(b,−c) for 0 < ϵ ≤ c − k − 1 ([[lem:i-c-2-2]] (f)), so [[lem:i-c-2-2]] (d) applies. For u
in C_c^∞((−1, ∞) × 𝕊³), 𝔪_k(u) = ∫ v^k u dv. Operators acting on 𝕊³ alone (multiplication by smooth endomorphisms
of ω, derivatives in ω) commute with 𝔪_k.

**Lemma {#lem:sp-moments}** (Moments of the spectral family.) Let k ∈ ℕ_0, c > k + 1, s′ ∈ ℝ and
u ∈ Ḣ^(s′,c)_b. Then for every ϰ ∈ ℂ

    𝔪_k(N_sf(ϰ)u) = L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔪_k(u) + 2k(ϰ − k − 3/2 − S̄)𝔪_(k−1)(u),                    {#eq:sp-moments}

the last term being absent for k = 0. The identity obtained by applying ∂_ϰ^i to both sides holds, with N_sf^(i)(ϰ)
on the left.

*Proof.* N_sf(ϰ) maps Ḣ^(s′,c)_b to Ḣ^(s′−2,c)_b boundedly ([[sec:iii-g-1-2]]), and 𝔪_k and 𝔪_(k−1) are continuous
on these spaces; so both sides of [[eq:sp-moments]] are continuous in u. C_c^∞((−1, ∞) × 𝕊³) is dense in
Ḣ^(s′,c)_b, near v = −1 by [[lem:i-a-6-1]] (a) and near R = 0 by [[lem:i-c-2-2]] (d), glued with χ_∂. For such u,
integration by parts in v at fixed ω gives, for every g smooth with compact support in v,

    ∫ v^k ∂_v g dv = −k ∫ v^(k−1) g dv,     ∫ v^k (v∂_v) g dv = −(k + 1) ∫ v^k g dv,

and the second gives ∫ v^k F(v∂_v)g dv = F(−k − 1)∫ v^k g dv for every polynomial F whose coefficients act on 𝕊³
alone. In [[eq:iii-g-1-3]] put g := (v∂_v + ϰ − 3/2 − S̄)u. The first term −2∂_vg contributes
2k∫ v^(k−1)g dv = 2k(ϰ − 3/2 − S̄ − k)𝔪_(k−1)(u), and the second, L̃(0)(ω, v∂_v + ϰ, ∂_ω)u, contributes
L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔪_k(u). For fixed u both sides are polynomials in ϰ, which gives the last statement. ∎

**Lemma {#lem:sp-primitive}** (Integration in v.) Let Re ϰ_0 ≥ 2, let (s, c) be admissible for every ϰ in a disc about
ϰ_0, with c > 1, and let (u_0, …, u_(N−1)) ∈ 𝒦_N(N_sf, ϰ_0) in the space 𝒳 of (s, c), with 𝔪_0(u_j) = 0 for every j.
Let Iu_j be the distribution on ℝ_v × 𝕊³ with ∂_v Iu_j = u_j that vanishes on {v < −1}. Then for every c′ < c − 1:

(a) u_j ∈ Ḣ^((s;∞),c)_(b;b) and Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b);

(b) (Iu_0, …, Iu_(N−1)) ∈ 𝒦_N(N_sf, ϰ_0 − 1) in the space 𝒳 of the pair (s + 1, c′), which is admissible for ϰ_0 − 1
when c′ > Re ϰ_0 − 2;

(c) 𝔪_k(Iu_j) = −(k + 1)⁻¹𝔪_(k+1)(u_j) for every integer k with 0 ≤ k < c − 2.

*Proof.* (a) By [[eq:sp-chain]], N_sf(ϰ_0)u_j = −N_sf′(ϰ_0)u_(j−1) − ½N_sf″(ϰ_0)u_(j−2), where by [[eq:iii-g-1-2]] and
[[eq:iii-g-1-3]] N_sf′(ϰ) = −2∂_v − 2(v∂_v + ϰ) + a(ω) and N_sf″ = −2. These operators map Ḣ^((s;k),c)_(b;b) into
Ḣ^((s−1;k),c)_(b;b) for every k: near v = 0 because ∂_v(v∂_v) = (v∂_v + 1)∂_v and ∂_v commutes with the ℒ_Ω, so
that words pass through ∂_v, and near R = 0 because ∂_v = −R(R∂_R). By induction on j, [[thm:iii-g-5-1]] (3) gives
u_j ∈ Ḣ^((s;∞),c)_(b;b). Near R = 0 this space is H^∞_(b,c) ([[sec:iii-g-1-2]]), so |W^αu_j| ≤ C_αv^(−c) on
{v ≥ 4} for every word W^α in v∂_v and the ℒ_Ω ([[lem:i-c-2-2]] (f)). Take χ ∈ C^∞(ℝ) equal to 1 on (−∞, 3] and to 0
on [4, ∞). Then I(χu_j) is constant on {v ≥ 4}, equal to ⟨χu_j, 1⟩, and so, on {v ≥ 4},

    Iu_j(v) = ⟨χu_j, 1⟩ + ∫_3^v (1 − χ)u_j dv′ = 𝔪_0(u_j) − ∫_v^∞ u_j dv′ = −∫_v^∞ u_j dv′.

As v∂_vI = I(v∂_v + 1) (both sides vanish on {v < −1} and have the same v-derivative) and the ℒ_Ω commute with I,
|W^αIu_j| ≤ C_αv^(1−c) on {v ≥ 4}; so Iu_j ∈ 𝒜^(c−1) ⊂ H^∞_(b,c′) near R = 0 ([[lem:i-c-2-2]] (f)). On {v < 5},
W^αIu_j = I(W̃^αu_j), with every v∂_v of W^α replaced by v∂_v + 1 in W̃^α; by (i) of the proof of [[lem:iii-g1-2-1]]
each W̃^αu_j lies in H^s(ℝ; H^m(𝕊³)) for every m, the primitive maps this space into H^(s+1)(ℝ; H^m(𝕊³)) locally
((iii) (α) there), and the latter lies in H^(s+1) for m large, as in (i) there. So Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b).

(b) By [[lem:iii-g-1-2]] (e), N_sf(ϰ + 1)∂_v = ∂_vN_sf(ϰ) for every ϰ; differentiating in ϰ,
N_sf^(i)(ϰ_0)∂_v = ∂_vN_sf^(i)(ϰ_0 − 1). So F_j := Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) has
∂_vF_j = Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i) = 0; F_j vanishes on {v < −1} and does not depend on v, hence F_j = 0.
By (a), Iu_j ∈ Ḣ^(s+1,c′)_b, and N_sf(ϰ_0 − 1)Iu_j = −Σ_(i≥1)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) lies in Ḣ^(s,c′)_b, the
operator N_sf′ being of first order; so Iu_j lies in 𝒳 for (s + 1, c′). The pair is admissible for ϰ_0 − 1: s + 1 <
2 − Re(ϰ_0 − 1) as s < 2 − Re ϰ_0, and c′ ∈ (Re ϰ_0 − 2, Re ϰ_0 − 1) as c′ < c − 1 < Re ϰ_0 − 1.

(c) Both moments are defined, choosing c′ ∈ (k + 1, c − 1). Let φ ∈ C_c^∞(ℝ) equal 1 on [−2, 1], put φ_T(v) := φ(v/T)
for T > 4, and let ψ ∈ C^∞(𝕊³; ℂ^15). As ∂_vIu_j = u_j,

    ⟨Iu_j, (k + 1)φ_Tv^kψ⟩ + ⟨Iu_j, φ_T′v^(k+1)ψ⟩ = −⟨u_j, φ_Tv^(k+1)ψ⟩.

As T → ∞ the first and last terms tend to (k + 1)⟨𝔪_k(Iu_j), ψ⟩ and −⟨𝔪_(k+1)(u_j), ψ⟩ (dominated convergence on
{v ≥ 4}, with the bounds of (a)), and the middle one is O(T^(−1)·T^(k+1)·T^(1−c)·T) = O(T^(k+2−c)), which tends to 0. ∎

#### The moment matrix {#sec:sp-matrix}

**Definition {#def:sp-matrix}** (The moment matrix.) For a type τ and K ∈ ℕ_0 let 𝔐^K_τ(ϰ) be the matrix polynomial
of size (K + 1)n_τ, block lower bidiagonal with blocks of size n_τ, whose blocks are

    (𝔐^K_τ)_(kk)(ϰ) = N_τ(ϰ − k − 1)  (0 ≤ k ≤ K),     (𝔐^K_τ)_(k,k−1)(ϰ) = 2k(ϰ − k − 3/2 − S_τ)  (1 ≤ k ≤ K),
                                                                                                      {#eq:sp-matrix}

all other blocks being 0. So det 𝔐^K_τ(ϰ) = ∏_(k=0)^K det N_τ(ϰ − k − 1). For Re ϰ_0 ≥ 2 write 𝔐_τ := 𝔐^(K(ϰ_0))_τ,
and let c_τ(ϰ_0) be the order of the zero of det 𝔐_τ at ϰ_0: the number of roots μ of type τ, with multiplicity,
with ϰ_0 − μ ∈ {1, …, K(ϰ_0) + 1}. Each such root has Re μ ≥ Re ϰ_0 − K(ϰ_0) − 1 = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 ≥ 1, and is
therefore singular.

By [[eq:sp-moments]], the moments (𝔪_k(u))_(k≤K) of N_sf(ϰ)u are obtained from those of u by the operator 𝔐(ϰ) on
𝒟′(𝕊³; ℂ^15)^(K+1) defined by the right side of [[eq:sp-moments]]; on W_π^(K+1) it acts as 𝔐^K_τ(ϰ) ⊗ Id_π.

**Theorem {#thm:sp-reduction}** (The poles of the spectral family in {Re ≥ 2}.) Let Re ϰ_0 ≥ 2 and K := K(ϰ_0), and
let 𝒳, 𝒴 be the spaces of a pair admissible for every ϰ in a disc about ϰ_0.

(a) For every N ≥ 1 the map (u_j)_(j<N) ↦ ((𝔪_k(u_j))_(k≤K))_(j<N) is a bijection from 𝒦_N(N_sf, ϰ_0) onto
𝒦_N(𝔐, ϰ_0) = ⊕_π 𝒦_N(𝔐_τ(π) ⊗ Id_π, ϰ_0), τ(π) the type of π; only finitely many summands are non-zero.

(b) dim ker N_sf(ϰ_0) = Σ_τ d_τ dim ker 𝔐_τ(ϰ_0), and the order of the pole of N_sf(·)⁻¹ at ϰ_0 is the largest of the
numbers p(𝔐_τ, ϰ_0), each of which is at most c_τ(ϰ_0).

(c) ϰ_0 ∈ 𝒫 if and only if ϰ_0 = μ + j with μ a singular root and j ≥ 1 an integer. So
𝒫 ∩ {Re ≥ 2} = {μ + j : μ a singular root of some type, j ∈ ℕ, j ≥ 1}.

(d) If c_τ(ϰ_0) ≤ 1 for every type, then ϰ_0 is at most a simple pole of N_sf(·)⁻¹.

*Proof.* Choose the pair (s, c) with c ∈ (Re ϰ_0 − 1, Re ϰ_0); the poles and their orders do not depend on the pair
([[thm:iii-g-5-1]] (2)). Then c > K + 1, as K + 1 ≤ Re ϰ_0 − 1. By [[lem:sp-primitive]] (a) the elements of a tuple
of 𝒦_N(N_sf, ϰ_0) lie in Ḣ^(s,c)_b, so their moments of order at most K are defined, and by [[lem:sp-moments]] (with
its derivatives) they form a tuple of 𝒦_N(𝔐, ϰ_0). The components on the W_π are tuples of
𝒦_N(𝔐_τ(π) ⊗ Id_π, ϰ_0), which vanish unless det 𝔐_τ(π)(ϰ_0) = 0, that is unless π has a root among ϰ_0 − 1, …,
ϰ_0 − K − 1; by [[lem:iii-f1-2-4]] with X := Re ϰ_0 this holds for a finite set F of representations only.

*Injectivity.* Let (u_j) ∈ 𝒦_N(N_sf, ϰ_0) have all moments of order at most K equal to 0. Choose η > 0 with
(K + 1)η < c − Re ϰ_0 + 1 and put c_i := c − i(1 + η). We show by induction on i ≤ K + 1 that (I^iu_j) ∈
𝒦_N(N_sf, ϰ_0 − i) in the space 𝒳 of the pair (s + i, c_i), admissible for ϰ_0 − i, with 𝔪_k(I^iu_j) = 0 for
k ≤ K − i. For i = 0 this is the hypothesis. If it holds for i ≤ K, then 𝔪_0(I^iu_j) = 0, c_i > Re ϰ_0 − 1 − i ≥
K + 1 − i ≥ 1, and [[lem:sp-primitive]] with c′ := c_(i+1) ∈ (Re ϰ_0 − i − 2, c_i − 1) gives the statement for i + 1,
the moments by its part (c) (k ≤ K − i − 1 < c_i − 2). At i = K + 1, Re(ϰ_0 − K − 1) = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 < 2, so
N_sf(ϰ_0 − K − 1) is injective ([[prop:iii-g-3-2]]); by [[eq:sp-chain]] and induction on j, I^(K+1)u_j = 0 for every
j. As ∂_v^(K+1)I^(K+1)u_j = u_j, every u_j vanishes.

*Surjectivity.* Let T_N: 𝒳^N → 𝒴^N, (u_j) ↦ (Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i))_j, so that 𝒦_N(N_sf, ϰ_0) = ker T_N.
N_sf(ϰ_0) is Fredholm of index 0 ([[thm:iii-g-5-1]] (1)); choose a finite-rank K_1: 𝒳 → 𝒴 with N_sf(ϰ_0) + K_1
invertible, as in the proof of [[thm:iii-g-5-1]]. T_N + diag(K_1, …, K_1) is block lower triangular with invertible
diagonal blocks, hence invertible (solve row by row); so T_N = B(Id − G) with B invertible and G of finite rank. For
such an operator dim ker T_N = codim ran T_N. Indeed, let E ⊃ ran G be finite-dimensional; A := Id − G maps E into
E, every x with Ax = 0 lies in E, A induces the identity on 𝒳^N/E, and if Ax ∈ E then x ∈ E. So ran A + E = 𝒳^N
and ran A ∩ E = A(E), whence codim ran A = dim E − dim A(E) = dim ker(A|_E) = dim ker A. Now let V := ⊕_(π∈F) W_π^(K+1)
and Ψ: 𝒴^N → V^N the map taking (f_j) to the components in V of the moments (𝔪_k(f_j))_(k≤K). It is onto: for
χ_0, …, χ_K ∈ C_c^∞((1, 2)) with ∫ v^iχ_k dv = δ_(ik) (they exist, the powers being linearly independent on (1, 2)),
the sources Σ_k χ_k(v)w_k, w_k ∈ V, lie in 𝒴 and have moments w_k. By [[lem:sp-moments]],
Ψ(T_Nu) = T^𝔐_N(moments of u), T^𝔐_N the operator of [[eq:sp-chain]] for 𝔐 on V^N, a square matrix. So Ψ maps
ran T_N into ran T^𝔐_N, and

    dim ker T_N = codim ran T_N ≥ dim V^N − rank T^𝔐_N = dim ker T^𝔐_N = dim 𝒦_N(𝔐, ϰ_0).

With the injectivity, the map is a bijection. This proves (a).

(b) The case N = 1 of (a) gives the dimension, as dim(ker 𝔐_τ(ϰ_0) ⊗ π) summed over the π of type τ is
d_τ dim ker 𝔐_τ(ϰ_0). A tuple of 𝒦_N(N_sf, ϰ_0) has u_0 ≠ 0 exactly when the moments of u_0 do not all vanish (the
case N = 1 of (a)), so the bijection maps Jordan chains onto Jordan chains, and p(N_sf, ϰ_0) is the largest of the
p(𝔐_τ ⊗ Id_π, ϰ_0) = p(𝔐_τ, ϰ_0). By [[lem:sp-pole-order]], applied on a disc about ϰ_0 on which 𝒫 has no other point,
p(N_sf, ϰ_0) is the order of the pole of N_sf(·)⁻¹. And 𝔐_τ(ϰ)⁻¹ = adj 𝔐_τ(ϰ)/det 𝔐_τ(ϰ) has a pole of order at most
c_τ(ϰ_0), so p(𝔐_τ, ϰ_0) ≤ c_τ(ϰ_0) by [[lem:sp-pole-order]].

(c) By (b), ϰ_0 ∈ 𝒫 if and only if det 𝔐_τ(ϰ_0) = 0 for some type, that is ϰ_0 − j is a root for some j ∈
{1, …, K + 1}; such a root is singular ([[def:sp-matrix]]). Conversely, if μ is singular and j ≥ 1, then ϰ_0 := μ + j
has Re ϰ_0 > j + 1, so K(ϰ_0) ≥ j − 1, and det 𝔐_τ(ϰ_0) = 0. (d) follows from (b). ∎

On spacetime the moments have a direct meaning. For u ∈ ker N_sf(ϰ_0), U := ρ^(ϰ_0)u is a solution of 2L̄U = 0,
homogeneous of degree −ϰ_0 and supported in {t̄ ≥ |x|} ([[sec:iii-g-1-1]], Step 1 of the proof of [[prop:iii-g-3-2]]);
as dt̄ = r dv at fixed x, its integral in t̄ along each line {x = const} is r^(1−ϰ_0)𝔪_0(u), and by [[eq:sp-moments]]
at k = 0 this is a stationary solution of (2L̄)^(0), which vanishes unless ϰ_0 − 1 is a root. The poles thus come from
the stationary solutions r^(−μ)m, m ∈ ker L̃(0)(ω, μ, ∂_ω), that are singular at x = 0, and from their images under
∂_v, which maps ker N_sf(ϰ) into ker N_sf(ϰ + 1) ([[lem:iii-g-1-2]] (e)).

**Proposition {#prop:sp-visible}** (The poles are visible on ι⁺.) Let ϰ_0 ∈ 𝒫 with Re ϰ_0 ≥ 2 and
ϰ_0 ∉ 5/2 + spec S̄ + ℕ_0. Then ϰ_0 ∈ spec_ι⁺(L̄), and the order of the pole of ϰ ↦ N_ι⁺(L̄, ϰ)⁻¹ at ϰ_0, the largest
over the f ∈ Ċ^∞(ι⁺; S²T*), equals the order p of the pole of N_sf(·)⁻¹ at ϰ_0.

*Proof.* By [[thm:sp-reduction]] (b) there is a type τ with p(𝔐_τ, ϰ_0) = p, and by [[lem:sp-pole-order]] 𝔐_τ(·)⁻¹
has a pole of order p at ϰ_0; take π of type τ and ν ∈ W_π^(K+1) such that (ϰ − ϰ_0)^(p−1)𝔐(ϰ)⁻¹ν is unbounded near
ϰ_0. As in the proof of [[thm:sp-reduction]] choose g ∈ C_c^∞((1, 2) × 𝕊³; ℂ^15) whose moments of order at most
K(ϰ_0) are ν, and put f_ϰ := v^(2+ϰ)g, an element of Ċ^∞(ι⁺; S²T*) holomorphic in ϰ with R^(2+ϰ)f_ϰ = g. Let
u(ϰ) := N_sf(ϰ)⁻¹g, so that N_ι⁺(ϰ)⁻¹f_ϰ = R^(−ϰ)u(ϰ)|_(v>0) by [[eq:iii-g1-3-1]]. For ϰ ≠ ϰ_0 near ϰ_0,
[[eq:sp-moments]] gives 𝔐(ϰ)(moments of u(ϰ)) = ν; the moments being continuous on 𝒳, u has a pole of order at least
p, hence exactly p. By Step 0 of the proof of [[thm:iii-g1-3-1]], u(ϰ) is supported in {v ≥ 0}, and so are its
Laurent coefficients. Let c_(−p) be the leading one. As N_sf(ϰ)u(ϰ) = g is holomorphic, N_sf(ϰ_0)c_(−p) = 0. If
c_(−p) vanished on {v > 0}, it would be a non-zero element of ker N_sf(ϰ_0) supported in {v = 0}, and
[[lem:iii-g1-4-3]] would give ϰ_0 ∈ 5/2 + spec S̄ + ℕ_0. So R^(−ϰ)u(ϰ)|_(v>0) has a pole of order p at ϰ_0 (as a
distribution, hence in C^∞((0, ∞) × 𝕊³)). Write f_ϰ = Σ_(j<p)(ϰ − ϰ_0)^jf_j + (ϰ − ϰ_0)^pr(ϰ) with
f_j = (j!)⁻¹(log v)^jv^(2+ϰ_0)g ∈ Ċ^∞(ι⁺) and R^(2+ϰ)r(ϰ) holomorphic in 𝒴; then
N_ι⁺(ϰ)⁻¹f_ϰ − Σ_(j<p)(ϰ − ϰ_0)^jN_ι⁺(ϰ)⁻¹f_j = (ϰ − ϰ_0)^pR^(−ϰ)N_sf(ϰ)⁻¹(R^(2+ϰ)r(ϰ)) is holomorphic at ϰ_0. So
some N_ι⁺(ϰ)⁻¹f_j has a pole of order at least p. No f gives a larger order, as N_ι⁺(ϰ)⁻¹f = R^(−ϰ)N_sf(ϰ)⁻¹(R^(2+ϰ)f)
and R^(2+ϰ)f is holomorphic in 𝒴. ∎

#### The computational point {#sec:sp-point}

At the computational point let h := 10⁻⁶ (so γ_C = h⁻¹), κ := l(l + 2), x := hκ, a(x) := (3x + 10)/4 and
δ_C := 2.94·10⁻⁶, as in [[sec:s14-pa]]. Let ι₁ ∈ (2 + δ_C, 5/2) be the root of C of [[lem:s14-scalar-zero]],
ι_v(l) := (250002000000 + (l + 1)²)^(1/2) − 499999 the larger root of p_(v) ([[lem:s14-vector-distance]]), and
𝔡₀ := ι^Υ_(s0,2) − 2 and 𝔡₁ := ι^Υ_(s1,2) − 2 the offsets of [[sec:ec-gap-sums]], with
1.3333327·10⁻⁶ < 𝔡₀ < 1.3333334·10⁻⁶ and 3.3333·10⁻⁷ < 𝔡₁ < 3.3334·10⁻⁷ ([[prop:gap-sums]]). Further
σ_Υ = {0, 99/10000, 1/100, 1/50} ([[eq:iii-g1-1-4]]).

**Lemma {#lem:sp-roots}** (The singular roots of real part at most 4.) At the computational point, for a type τ let 𝒮_τ
be the set of its roots μ with 1 < Re μ ≤ 4.

(a) 𝒮_s0 = {2, 3 + 𝔡₀, ι₁ − 1, 4}; 𝒮_s1 = {3, 3 + 𝔡₁, ι − 1, ι′ − 1}, where ι, ι′ are the roots of P_1 in
(2 + 3h, a(3h)) and in (a(3h), 3 − δ_C); 𝒮_s2 = {4} ∪ {ι − 1 : P_2(ι) = 0, Re ι > 2}, the last three numbers lying in
(1, 2); 𝒮_sl = {ι − 1 : P_l(ι) = 0, 2 < Re ι ≤ 5} for l ≥ 3; 𝒮_v1 = {3, 4}; 𝒮_v2 = {4, ι_v(2) − 1}, with
ι_v(2) ∈ (3, 4); 𝒮_vl = {ι_v(l) − 1} for 3 ≤ l ≤ 1413 and 𝒮_vl = ∅ for l ≥ 1414; 𝒮_t2 = {4}; 𝒮_tl = ∅ for l ≥ 3.

(b) Every element of 𝒮_τ is a simple root of type τ.

(c) Two distinct elements of one set 𝒮_τ differ by an integer only for {2, 4} ⊂ 𝒮_s0 and for {3, 4} ⊂ 𝒮_v1.

*Proof.* (a) By [[prop:iii-f1-2-3]] the singular roots of type τ are the entries after its semicolon. Those that do
not come from □^C are: at s0, 2, 4 and 1 + ι^Υ_(s0,2) = 3 + 𝔡₀; at sl, l ≥ 1, the integers l + 2 and l + 4 (3 and 5
at l = 1) and the numbers 1 + ι^Υ_(sl,l+j) ∈ (l + j + 1, l + j + 5/4), j = 1, 2 (the bounds of the proof of
[[prop:iii-f1-2-3]]); at vl, l + 2 and l + 3; at tl, l + 2. Of these, real part at most 4 have exactly 2, 3 + 𝔡₀, 4
at s0; 3 and 1 + ι^Υ_(s1,2) = 3 + 𝔡₁ at s1; 4 = l + 2 at s2, v2 and t2; and 3, 4 at v1. The entries from □^C are the
numbers ι − 1, ι a root of □^C with real part at least 2 that the factor D of [[eq:iii-f1-2-1]] does not remove: at
s0 the root ι₁ of C, the root 2 of P_0 = −(ι − 2)C being removed and the other roots of C having real part below −100
(proof of [[prop:np-10-54]]); at sl the roots of P_l of real part at least 2 other than ι = 2 at l = 1
([[prop:s14-scalar-every-h]]); at vl the root ι_v(l), which equals 3 at l = 1, is removed there, and increases with
l. The roots of P_1 other than 2 and those of P_2 lie in the stated intervals ([[lem:s14-sextic-small]] (a), (b)).
ι_v(2) ∈ (3, 4) as 500002² = 250002000004 < 250002000009 < 500003²; and ι_v(l) ≤ 5 exactly when
(l + 1)² ≤ 500004² − 250002000000 = 2000016, that is l ≤ 1413, as 1414² = 1999396 and 1415² = 2002225.

(c) At s0, 𝔡₀ < δ_C. The differences (3 + 𝔡₀) − 2 = 1 + 𝔡₀ and 4 − (3 + 𝔡₀) = 1 − 𝔡₀ are not integers, and
3 − ι₁, 4 + 𝔡₀ − ι₁ and 5 − ι₁ lie in (1/2, 1 − δ_C), (3/2 + 𝔡₀, 2 − (δ_C − 𝔡₀)) and (5/2, 3 − δ_C), intervals
without integers. At s1, ι − 1 and ι′ − 1 are distinct points of (1 + 3h, 2 − δ_C); 3 − (ι − 1) lies in
(1 + δ_C, 2 − 3h) and (3 + 𝔡₁) − (ι − 1) in (1 + δ_C + 𝔡₁, 2 − (3h − 𝔡₁)), with 𝔡₁ < 3h, and likewise for ι′; and
(3 + 𝔡₁) − 3 = 𝔡₁. At s2, the three numbers in (1, 2) are distinct, the intervals of [[lem:s14-sextic-small]] (b)
being disjoint, and 4 − (ι − 1) ∈ (2, 3). At v2, 4 − (ι_v(2) − 1) ∈ (1, 2).

At sl with l ≥ 3 the elements of 𝒮_sl are ι − 1 for the roots ι of P_l with real part in (2, 5]. If x ≤ 70, these are
among the three roots of real part at least 2, which by [[cor:s14-remote-point]] are the roots of
[[lem:s14-sextic-count]] (a): for 3 ≤ l ≤ 133, three distinct real roots in (2, 3) ([[lem:s14-sextic-small]] (c));
for l ≥ 134 (x ≥ 0.018), a real root ι_B and two more, which for x ≤ 0.03 have real parts in (2.06, 2.98) while
ι_B ∈ (2.0179, 2.03], and which for x ≥ 0.03 are non-real and conjugate, ι_P and ι̅_P, in disjoint discs
([[lem:s14-sextic-large]] and the proof of [[prop:s14-damping-distance]]). In each case the three roots are distinct
and no two differ by a non-zero integer: their real parts differ by less than 1, or the difference is not real, or it
is the non-zero imaginary number ι_P − ι̅_P. If x > 70, no root of P_l satisfies |ι − 1| ≤ 50
([[lem:s14-sextic-count]] (b)), so no real root lies in (2, 5]; the three roots of real part at least 2
([[prop:s14-scalar-every-h]]) form a set closed under conjugation, so its non-real elements form at most one
conjugate pair, and two of its elements of real part at most 5 neither coincide nor differ by a real number.

(b) An element μ of 𝒮_τ is an entry of the list of type τ, and the list gives the roots with multiplicity. μ differs
from the entries of real part at most 0 or greater than 4 by its real part, and from the other elements of 𝒮_τ by (c)
and the distinctness shown there. So μ is a simple root. ∎

**Lemma {#lem:sp-two-roots}** (The chains at ϰ_0 = 5.) Let W = Σ_i W_i dx^i with W_i linear, Σ_i x_iW_i = 0 and
∂_iW_j + ∂_jW_i = 0 (a rotation 1-form, of vector type 1), and V̂ := r⁻¹W. Put

    K_s0 := Σ_i (dx^i)² − 4 dr²,     K_v1 := dr ⊗_s V̂,     Z := −6e_Υ dt̄² + (4 − e_Υ)Σ_i (dx^i)² − (4 + 2e_Υ) dr².

(a) For K = K_s0 and K = K_v1, and every ι ∈ ℂ,

    L̃(0)(ω, ι, ∂_ω)K = (ι − 4)(2S̄ − ι − 2)K.                                                            {#eq:sp-gauge}

(b) L̃(0)(ω, 2, ∂_ω)Z = 4(e_Υ + 2)K_s0.

(c) For every value of the parameters with 1, 3 not roots of type s0 and 1, 2 not roots of type v1, and the roots 2,
4 of type s0 and 3, 4 of type v1 simple, dim ker 𝔐_τ(5) = 2 and p(𝔐_τ, 5) = 1 for τ = s0 and τ = v1. At the
computational point these conditions hold.

*Proof.* L̃(0)(ω, ι, ∂_ω)K is defined by (2L̄)^(0)(r^(−ι)K) = r^(−ι−2)L̃(0)(ω, ι, ∂_ω)K, and (2L̄)^(0) is 2L̄ on
stationary sections ([[lem:iii-f-2-1]] (2)): by [[eq:iii-f-2-1]], (2L̄)^(0)h = □̄h + 2Ē^Cδ̄Ḡh + 2(δ̄* + Ē^C)Ē^ΥḠh, where
on stationary sections □̄ acts in the Cartesian frame as −Δ on each component and (δ̄k)_μ = −Σ_j ∂_jk_(μj). We use, on
ℝ⁴ and for real or complex a,

    Δr^a = a(a + 2)r^(a−2),     Δ(r^an_in_j) = r^(a−2)((a − 2)(a + 4)n_in_j + 2δ_(ij)),
    ∂_j(r^aδ_(ij)) = a r^(a−1)n_i,     ∂_j(r^an_in_j) = (a + 3)r^(a−1)n_i,
    ∂_j(r^ax_iW_j) = r^aW_i,     ∂_j(r^ax_jW_i) = (a + 5)r^aW_i,     Δ(r^a(x_iW_j + x_jW_i)) = a(a + 6)r^(a−2)(x_iW_j + x_jW_i).

The second and the last follow from Δ(fg) = (Δf)g + 2∇f·∇g + fΔg with x·∇(x_ix_j) = 2x_ix_j, Δ(x_ix_j) = 2δ_(ij),
x·∇(x_iW_j) = 2x_iW_j and Δ(x_iW_j) = 2∂_iW_j, the Killing equation removing the last term after symmetrising; the
fifth and sixth from x·W = 0, ∂_jW_j = 0 and x·∇W_i = W_i.

(a) Let h := r^(−ι)K. Then tr h = 0 (tr Σ(dx^i)² = 4, tr dr² = 1, ⟨dr, V̂⟩ = 0) and ι_(∂_t̄)h = 0, so Ḡh = h and,
as c̄_Υ^♯ = −r⁻¹∂_t̄, Ē^ΥḠh = −γ_Υ(2ι_(c̄_Υ^♯)h − e_Υc̄_Υ tr h) = 0 ([[sec:iii-f1-1]]). For K_s0, h_(ij) =
r^(−ι)(δ_(ij) − 4n_in_j), and the identities give Δh = (ι + 2)(ι − 4)r^(−2)h and δ̄h = −3(ι − 4)r^(−ι−1)dr. For K_v1,
h_(ij) = ½r^(−ι−2)(x_iW_j + x_jW_i), and they give Δh = (ι + 2)(ι − 4)r^(−2)h and δ̄h = ½(ι − 4)r^(−ι−1)V̂. In both cases
δ̄h = −(ι − 4)r⁻¹ι_Xh with X := ḡ⁻¹dt_* = −∂_t̄ − ∂_r, since ι_Xh = −ι_(∂_r)h equals 3r^(−ι)dr for K_s0 and −½r^(−ι)V̂
for K_v1. By [[eq:iii-f-2-2]], ρS̄h = −Ē^Cι_XḠh + (dt_* ⊗_s ·)Ē^ΥḠh = −Ē^C(ι_Xh). Hence

    (2L̄)^(0)h = −(ι + 2)(ι − 4)r^(−2)h − 2(ι − 4)r⁻¹Ē^C(ι_Xh) = (ι − 4)r^(−2)(2S̄ − ι − 2)h,

which is [[eq:sp-gauge]].

(b) Let h := r^(−2)Z. Then tr Z = 6e_Υ + 4(4 − e_Υ) − (4 + 2e_Υ) = 12 and ι_(∂_t̄)Z = −6e_Υ dt̄, so
Ē^ΥḠh = −γ_Υ(2·6e_Υ − 12e_Υ)r^(−3)dt̄ = 0. Next Ḡh = r^(−2)((6 − 6e_Υ)dt̄² − (2 + e_Υ)Σ(dx^i)² − (4 + 2e_Υ)dr²) has
no mixed time–space components, and by the identities
Σ_j∂_j(r^(−2)((2 + e_Υ)δ_(ij) + (4 + 2e_Υ)n_in_j)) = (−2(2 + e_Υ) + (4 + 2e_Υ))r^(−3)n_i = 0; so δ̄Ḡh = 0.
Finally Δ(r^(−2)) = 0, so Δ(r^(−2)dt̄²) = 0 and Δ(r^(−2)δ_(ij)) = 0, while Δ(r^(−2)n_in_j) = r^(−4)(2δ_(ij) −
8n_in_j). So (2L̄)^(0)h = □̄h = (4 + 2e_Υ)r^(−4)(2δ_(ij) − 8n_in_j)dx^idx^j = 4(e_Υ + 2)r^(−4)K_s0.

(c) Let k_τ ∈ ℂ^(n_τ) be the coefficient vector of K_τ, which by (a) satisfies N_τ(ι)k_τ = (ι − 4)(2S_τ − ι − 2)k_τ,
so k_τ spans ker N_τ(4), the root 4 being simple. K(5) = 3, and by [[eq:sp-matrix]] a vector (μ_0, μ_1, μ_2, μ_3)
lies in ker 𝔐_τ(5) exactly when

    N_τ(4)μ_0 = 0,  N_τ(3)μ_1 = −2(5/2 − S_τ)μ_0,  N_τ(2)μ_2 = −4(3/2 − S_τ)μ_1,  N_τ(1)μ_3 = −6(1/2 − S_τ)μ_2.

*Type s0.* N_s0(3) and N_s0(1) are invertible. By (a) at ι = 3, N_s0(3)k_s0 = 2(5/2 − S_s0)k_s0, so μ_0 := k_s0
gives μ_1 = −k_s0. By (a) at ι = 2, N_s0(2)k_s0 = 4(2 − S_s0)k_s0, so −4(3/2 − S_s0)μ_1 = N_s0(2)k_s0 − 2k_s0, which
by (b) equals N_s0(2)(k_s0 − z/(2(e_Υ + 2))), z the coefficient vector of Z. So μ_2 := k_s0 − z/(2(e_Υ + 2)) and
μ_3 := −6N_s0(1)⁻¹(1/2 − S_s0)μ_2 complete a kernel vector with μ_0 ≠ 0. A second one is (0, 0, w, μ_3), w spanning
ker N_s0(2) and μ_3 := −6N_s0(1)⁻¹(1/2 − S_s0)w. *Type v1.* N_v1(2) and N_v1(1) are invertible. For μ_0 := a k_v1
and w ∈ ker N_v1(3), μ_1 := −a k_v1 + w solves the second equation, by (a) at ι = 3, and μ_2, μ_3 are then determined;
this gives kernel vectors for every (a, w). In both cases dim ker 𝔐_τ(5) ≥ 2 = Σ_k dim ker N_τ(4 − k), and
[[lem:sp-block]] gives equality and p(𝔐_τ, 5) ≤ 1. The conditions hold at the computational point by
[[lem:sp-roots]] (a), (b): the roots of type s0 of real part in [1, 4] are 2, 3 + 𝔡₀, ι₁ − 1 and 4, and those of type
v1 are 3 and 4. ∎

**Lemma {#lem:sp-exceptional}** (No pole at the exceptional points.) Let Q := {5/2, 7/2, 9/2} + σ_Υ, twelve numbers. At
the computational point, P_l(q) ≠ 0 and ι_v(l) ≠ q for every q ∈ Q and l ≥ 1. Hence no singular root of real part at
most 4 lies in 3/2 + σ_Υ + ℤ, and no point of 𝒫 of real part at most 5 lies in 5/2 + spec S̄ + ℕ_0.

*Proof.* *The vector type.* ι_v(l) = q would make (q + 499999)² = 250002000000 + (l + 1)² an integer. Each q ∈ Q is
a fraction p′/d in lowest terms with d > 1, and then (q + 499999)² = (p′ + 499999d)²/d² with p′ + 499999d prime to d,
which is not an integer.

*The scalar type.* By [[eq:s14-nl]], P_l(ι) = c_0(ι) + c_1(ι)κ + c_2(ι)κ² + c_3κ³. At κ = 0 the third column of the
matrix there is (0, 0, h(2ι − 1 − ι²) − 2v(ι − 3))ᵀ and its upper left 2 × 2 block is hN_0(ι); so, at v = 1/2,
c_0(ι) = (−h(ι − 1)² − (ι − 3))P_0(ι), with P_0 = −(ι − 2)C of [[eq:s14-c0]]. Expanding the determinant at the
computational point,

    c_3 = 10⁻¹⁸,     c_2(ι) = 10⁻¹⁸(−3ι² − (255998991/64)ι + 2322999247/64),
    c_1(ι) = 10⁻¹⁸(3ι⁴ + (255998991/32)ι³ + (79998081750817/16)ι² − (3218988513000625/64)ι + 5157998188999183/64).

For a prime p let v_p denote the p-adic valuation of a non-zero rational number. If q ∈ Q and p is a prime with
v_p(c_0(q)) < v_p(c_i(q)) for i = 1, 2, 3, then P_l(q) ≠ 0 for every integer κ, since each c_i(q)κ^i has valuation at
least v_p(c_i(q)) and a sum whose term of least valuation is unique has that valuation. The valuations of the
coefficients of c_1, from ι⁴ to ι⁰, are −18, −23, −22, −24, −24 for p = 2 and −18, −18, −18, −14, −18 for p = 5
(3218988513000625 = 5⁴·5150381620801); those of c_2, from ι² to ι⁰, are −18, −24, −24 for p = 2 and −18, −18, −18 for
p = 5; v_p(c_3) = −18. Hence v_p(c_i(q)) ≥ min_j(v_p(coefficient of ι^j) + j·v_p(q)), which gives the lower bounds in
the table below. The values of c_0 are

    c_0(5/2) = 102382116069206441391/(2¹²·10¹⁷),     c_0(7/2) = −184309587192075727923/(2¹³·10¹⁶),
    c_0(9/2) = −7679697448702749433821/(2¹²·10¹⁷),
    c_0(25099/10000) = 1019224980784674272031997531559760391559271/(4·10⁴²),
    c_0(35099/10000) = −9299228494721864136714649149276457696950729/(4·10⁴²),
    c_0(45099/10000) = −76091116104307206847501599126784137785460729/(4·10⁴²),
    c_0(251/100) = 4077667112282805096193344619959/(16·10³⁰),
    c_0(351/100) = −37209137195213265101596444677141/(16·10³⁰),
    c_0(451/100) = −304408877927380731996608663774241/(16·10³⁰),
    c_0(63/25) = 126728556223578619714117857/(5¹¹·10¹⁹),     c_0(88/25) = −2346368372779440282518355711/(5¹⁰·10²⁰),
    c_0(113/25) = −2356501507010040363609315267/(5¹³·10¹⁷),

with numerators odd in the first nine and prime to 5 in the last three. So:

    q                                 p    v_p(q)    v_p(c_0(q))    v_p(c_1(q)) ≥    v_p(c_2(q)) ≥    v_p(c_3)
    q ∈ {5/2, 7/2, 9/2}               2    −1        −29            −26              −25              −18
    q ∈ {5/2, 7/2, 9/2} + 99/10000    2    −4        −44            −35              −28              −18
    q ∈ {5/2, 7/2, 9/2} + 1/100       2    −2        −34            −29              −26              −18
    q ∈ {5/2, 7/2, 9/2} + 1/50        5    −2        −30            −26              −22              −18

and in every row v_p(c_0(q)) is the least. So P_l(q) ≠ 0 for every l ≥ 1.

*The consequences.* By [[lem:sp-roots]] (a) the singular roots of real part at most 4 are: integers; 3 + 𝔡₀ and
3 + 𝔡₁, whose distance from ℤ is below 1.34·10⁻⁶; ι₁ − 1 ∈ (1, 3/2); ι − 1 for roots ι of P_l with real part in
(2, 5]; and ι_v(l) − 1 ≤ 4. A number of 3/2 + σ_Υ + ℤ has distance from ℤ at least 12/25 and real part in (1, 4] only
in 3/2 + σ_Υ + {0, 1, 2}; ι₁ − 1 < 3/2; and ι − 1 ∈ 3/2 + σ_Υ + ℤ with Re ι ∈ (2, 5] means ι ∈ Q, which is excluded
for the roots of P_l (for non-real ι trivially) and for ι_v(l). Finally spec S̄ = σ_Υ ∪ σ_C with σ_C ⊂ [s_C, ∞), s_C > 100 ([[eq:iii-g1-1-4]],
[[sec:iii-f-1]]), so a point of 5/2 + spec S̄ + ℕ_0 of real part at most 5 lies in 5/2 + σ_Υ + {0, 1, 2}; a point
μ + j of 𝒫 there ([[thm:sp-reduction]] (c), with Re μ ≤ 4) would have μ ∈ 3/2 + σ_Υ + ℤ. ∎

**Theorem {#thm:sp-spectrum}** (The ι⁺-spectrum at real part at most 5.) At the computational point, and for every b
near b₀:

(a) spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} = 𝒫 ∩ {Re ϰ ≤ 5} is the union of

    {3, 4, 5},     {4 + 𝔡₀, 4 + 𝔡₁},     {ι₁, ι₁ + 1, ι₁ + 2},
    {ι + j : l ≥ 1, P_l(ι) = 0, Re ι > 2, j ∈ ℕ_0, Re ι + j ≤ 5},
    {ι_v(l) + j : 2 ≤ l ≤ 1413, j ∈ ℕ_0, ι_v(l) + j ≤ 5}.

It is finite and lies in {Re ϰ > 2}.

(b) Every point of (a) is a simple pole of N_sf(·)⁻¹ and of N_ι⁺(L̄, ·)⁻¹: Spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} consists of the
pairs (ϰ, 0), ϰ in (a). The order m_ι of [[prop:iii-g3-2-4]] equals 1 at these points and 0 at every other point of
{Re ϰ ≤ 5}.

(c) dim ker N_sf(ϰ_0) = Σ_τ d_τ c_τ(ϰ_0) at every point of (a): 1 at ϰ_0 = 3 (type s0), 11 at ϰ_0 = 4 (s0, s1, v1:
1 + 4 + 6) and 53 at ϰ_0 = 5 (s0, s1, s2, v1, v2, t2: 2 + 4 + 9 + 12 + 16 + 10).

*Proof.* By [[lem:iii-h2-3-2]], N_ι⁺(2L_b) = N_ι⁺(2L̄), and the indicial roots of L̂_b(0) do not depend on b
([[lem:iii-f-2-1]] (3)); so nothing below depends on b.

(a) By [[thm:sp-reduction]] (c), 𝒫 ∩ {Re ≤ 5} is the set of μ + j with μ singular, j ≥ 1 and Re(μ + j) ≤ 5, so
Re μ ≤ 4 and μ ∈ 𝒮_τ for some τ. [[lem:sp-roots]] (a) gives: from 𝒮_s0, 3, 4, 5, 4 + 𝔡₀ and ι₁, ι₁ + 1, ι₁ + 2
(ι₁ + 3 > 5); from 𝒮_s1, 4, 5, 4 + 𝔡₁ (5 + 𝔡₁ > 5) and ι + j for the two roots of P_1 in (2, 3), j ≤ 2; from 𝒮_s2,
5 and ι + j for the roots of P_2, j ≤ 2; from 𝒮_sl, l ≥ 3, the ι + j with Re ι + j ≤ 5; from 𝒮_v1, 4 and 5; from
𝒮_v2, 5, ι_v(2) and ι_v(2) + 1; from 𝒮_vl, l ≥ 3, the ι_v(l) + j ≤ 5; from 𝒮_t2, 5. This is the union, as the roots of
P_l with real part greater than 2 are those of real part at least 2 other than ι = 2 at l = 1
([[prop:s14-scalar-every-h]]). By [[lem:sp-exceptional]] no point of it lies in 5/2 + spec S̄ + ℕ_0, so
[[prop:sp-visible]] puts it in spec_ι⁺(L̄); and spec_ι⁺(L̄) ⊂ 𝒫 ([[lem:iii-g1-4-2]] (a)). The set is finite by
[[thm:iii-g-5-1]] (2), and every singular root has real part greater than 1.

(b) Let ϰ_0 be a point of (a) and τ a type. The roots counted by c_τ(ϰ_0) lie in 𝒮_τ and are simple
([[lem:sp-roots]] (b)), and any two of them differ by an integer, both lying in ϰ_0 − {1, …, K(ϰ_0) + 1}; so by
[[lem:sp-roots]] (c), c_τ(ϰ_0) ≤ 1, except c_s0(5) = 2 (the roots 4 and 2) and c_v1(5) = 2 (the roots 4 and 3). By [[thm:sp-reduction]] (b) and
[[lem:sp-two-roots]] (c), N_sf(·)⁻¹ has a simple pole at ϰ_0, and by [[prop:sp-visible]] so has N_ι⁺(L̄, ·)⁻¹. The
order of the pole of [[eq:iii-g1-3-3]] is that of N_ι⁺(L̄, ·)⁻¹ on Ċ^∞(ι⁺) ([[lem:iii-g1-4-2]] (b)).

(c) [[thm:sp-reduction]] (b), with dim ker 𝔐_τ(ϰ_0) = c_τ(ϰ_0): when c_τ(ϰ_0) = 1, det 𝔐_τ has a simple zero, so the
kernel is non-zero, and [[lem:sp-block]] bounds its dimension by 1; when c_τ(ϰ_0) = 2 it is [[lem:sp-two-roots]] (c).
At ϰ_0 = 3, 4, 5 the types with c_τ(ϰ_0) ≥ 1 are read off from [[lem:sp-roots]] (a); the values of d_τ are 1, 4 and 9
at s0, s1, s2, 6 and 16 at v1, v2, and 10 at t2. ∎

**Corollary {#cor:sp-lstar}** (The contribution of the poles to l_*.) At the computational point:

(a) The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 are all equal to 1. Of the quantities that the
number l_* of [[def:iii-i10-1-1]] bounds at real part at most 5, these orders contribute exactly 1, and the
multiplicities of the indicial roots of L̂_b(0) with real part in (1, 4] are all 1 ([[lem:sp-roots]] (b)). So
l_* = max(1, L, M), where L is the largest logarithmic order of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part at most 5 and M
the largest multiplicity of an indicial root of L̂_b(0) of real part at most 5; l_* = 1 exactly when L ≤ 1 and M = 1,
and otherwise l_* is attained by L or M.

(b) For λ ∈ Σ ([[def:iii-j-1-1]]), K_ι(λ) ≤ m_ι(λ) + m_♯(λ) ([[prop:iii-g3-2-4]]) with m_ι(λ) ∈ {0, 1}, equal to 1
exactly when λ is a point of [[thm:sp-spectrum]] (a); so K_ι(λ) ≤ 2 + k(ℰ^C_(I,♯), λ) ≤ l_* + 2, which is at most
2l_* + 1 as l_* ≥ 1, and K_ι(λ) ≤ 3 when l_* = 1.

(c) In the step at λ₀ ([[sec:s23-step]]), 𝒮_(λ₀) raises the logarithmic order by m_ι(λ₀) ([[cor:iii-g2-4-3]], l_0 =
m_ι(λ₀)): by 1 at the points of [[thm:sp-spectrum]] (a) and by 0 at every other λ₀ with Re λ₀ ≤ 5. Likewise each raise
"by a pole order of N_ι⁺(L̄, ·)⁻¹" in [[lem:iii-i10-1-2]] (c) is at most 1.

(d) On {2 ≤ Re ϰ ≤ 3 + ε_+}, ε_+ < 1/4, the poles are 3; ι₁, and ι₁ + 1 if ι₁ ≤ 2 + ε_+; the roots ι of P_l (l ≥ 1)
with 2 < Re ι ≤ 3 + ε_+, and ι + 1 for those with Re ι ≤ 2 + ε_+; and the ι_v(l), l ≥ 2, with ι_v(l) ≤ 3 + ε_+. All
are simple. The numbers λ_♯ + j, 3/2 + γ_Υ + j and 3/2 + 2γ_Υ + j (j = 1, 2, 3) are not poles.

*Proof.* (a) is [[thm:sp-spectrum]] (b) and [[lem:sp-roots]] (b); the set of poles at real part at most 5 is not
empty, so the pole orders require l_* ≥ 1. (b) is the bound of [[prop:iii-g3-2-4]] with (a), and k(ℰ^C_(I,♯), λ) ≤ l_*
as in the proof of [[lem:iii-j-1-2]]. (c): by [[cor:iii-g2-4-3]], the logarithmic powers produced are at most k + l_0, l_0 the order of
the pole of N_ι⁺(L̄, ·)⁻¹ at the exponent. (d) is [[thm:sp-spectrum]] (a) restricted to the strip (4 + 𝔡₀, 4 + 𝔡₁ and
the integers 4, 5 lie beyond it), with [[lem:sp-exceptional]] for the last statement: these numbers lie in
3/2 + σ_Υ + {1, 2, 3} ⊂ Q, are not integers, are not 4 + 𝔡₀, 4 + 𝔡₁ or ι₁ + j (ι₁ + j ∈ (j + 2, j + 5/2)), and are not
of the form ι + j or ι_v(l) + j with ι, ι_v(l) of real part greater than 2, as these would lie in Q. ∎

**Remark {#rem:sp-scope}** (What the evaluation leaves open.) [[thm:sp-spectrum]] describes the poles exactly, by the
roots of the explicit polynomials P_l and p_(v). The vector type is in closed form, and for the scalar types with
x ≤ 70 the roots are enclosed by [[lem:s14-sextic-small]] and [[lem:s14-sextic-large]]; for x > 70 this paper locates
the roots of P_l only in {Re ι > 2} with no real root in (2, 5], which suffices for every statement above but leaves
the largest l contributing a pole below real part 5 unevaluated. The multiplicities of the indicial roots of real part
at most 0 or in (4, 5], and the logarithmic orders L of [[cor:sp-lstar]] (a), belong to the index sets and are not
determined here.
