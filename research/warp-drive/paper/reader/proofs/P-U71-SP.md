### The poles of the inverse of the ι⁺-normal operator {#sec:sp}

This section determines the poles of ϰ ↦ N_sf(ϰ)⁻¹ ([[thm:iii-g-5-1]]) and of ϰ ↦ N_ι⁺(L̄, ϰ)⁻¹ ([[def:iii-g1-4-1]])
in the half plane {Re ϰ ≥ 2}, with their orders. Of these poles [[lem:iii-g1-4-2]] (a) states that they lie in
{Re ≥ 2}, finitely many below each bound. Their orders at real part at most 5 enter the number l_* of
[[def:iii-i10-1-1]], the bound K_ι ≤ 2l_* + 1 of [[lem:iii-j-1-2]] and the logarithmic orders that the solution maps
of the steps of [[sec:s23-step]] raise.

There are two results. The first holds wherever the hypotheses of [[ch:s16]] hold. Integrating the equation
N_sf(ϰ)u = f against the powers v^k reduces the poles at a point ϰ_0 with Re ϰ_0 ≥ 2, on the isotypic components of
one type, to those of the inverse of an explicit matrix polynomial built from the indicial matrix of L̃(0) and from S̄
alone ([[thm:sp-reduction]]). In particular the poles in {Re ϰ ≥ 2} are exactly the numbers μ + j, μ an indicial root
of L̂_b(0) with Re μ > 1 and j ≥ 1 an integer, and the order of each is at most the number of such roots of one type,
with multiplicity, among ϰ_0 − 1, ϰ_0 − 2, …. The second is the evaluation at the computational point of
[[def:ec-point]]: every pole of real part at most 5 is simple and lies in spec_ι⁺(L̄), and the poles are listed
([[thm:sp-spectrum]]). The orders of these poles therefore contribute exactly 1 to l_*; with the logarithmic orders and
the multiplicities that the index sets carry, l_* = 50 is admissible, and, with the least ℰ^C_I, K_ι ≤ 2 on the set Σ
of [[def:iii-j-1-1]] ([[cor:sp-lstar]]). Nothing depends on the black hole parameter, as N_ι⁺(2L_b) = N_ι⁺(2L̄) for
every b ([[lem:iii-h2-3-2]]).

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
A_i ∈ ℒ(X, Y), and A^(i) := ∂_ϰ^iA. For ϰ_0 ∈ ℂ and 𝔫 ≥ 1 let 𝒦_𝔫(A, ϰ_0) be the space of the tuples
(u_0, …, u_(𝔫−1)) ∈ X^𝔫 with

    Σ_(i=0)^j (i!)⁻¹ A^(i)(ϰ_0) u_(j−i) = 0,     0 ≤ j < 𝔫,                                             {#eq:sp-chain}

that is, A(ϰ)Σ_(j<𝔫)(ϰ − ϰ_0)^ju_j = O((ϰ − ϰ_0)^𝔫). A tuple of 𝒦_𝔫(A, ϰ_0) with u_0 ≠ 0 is a *Jordan chain of
length 𝔫*, and p(A, ϰ_0) is the largest length of a Jordan chain (0 if A(ϰ_0) is injective). The same definitions
apply to square matrix polynomials, with X = Y a finite-dimensional space.

**Lemma {#lem:sp-pole-order}** (Pole order and chains.) Let A be as in [[def:sp-chains]], invertible for
0 < |ϰ − ϰ_0| < r, and let ϰ ↦ A(ϰ)⁻¹ ∈ ℒ(Y, X) have a pole of order p_0 at ϰ_0 (p_0 = 0 if it is holomorphic
there). Then p(A, ϰ_0) = p_0.

*Proof.* Write A(ϰ)⁻¹ = Σ_(i=1)^(p_0)(ϰ − ϰ_0)^(−i)A_(−i) + H(ϰ) with H holomorphic and A_(−p_0) ≠ 0. If p_0 ≥ 1,
choose f ∈ Y with A_(−p_0)f ≠ 0. Then U(ϰ) := (ϰ − ϰ_0)^(p_0)A(ϰ)⁻¹f is holomorphic near ϰ_0, U(ϰ_0) = A_(−p_0)f ≠ 0
and A(ϰ)U(ϰ) = (ϰ − ϰ_0)^(p_0)f. As A is a polynomial, the coefficient of (ϰ − ϰ_0)^j in A(ϰ)U(ϰ) is the left side
of [[eq:sp-chain]] for the Taylor coefficients u_j of U, and it vanishes for j < p_0; so (u_0, …, u_(p_0−1)) is a
Jordan chain and p(A, ϰ_0) ≥ p_0. Conversely, let (u_0, …, u_(𝔫−1)) be a Jordan chain and
U(ϰ) := Σ_(j<𝔫)(ϰ − ϰ_0)^ju_j. By [[eq:sp-chain]], g(ϰ) := (ϰ − ϰ_0)^(−𝔫)A(ϰ)U(ϰ) is a polynomial, and
U(ϰ) = (ϰ − ϰ_0)^𝔫A(ϰ)⁻¹g(ϰ) for 0 < |ϰ − ϰ_0| < r. The right side is O(|ϰ − ϰ_0|^(𝔫−p_0)) and U(ϰ_0) = u_0 ≠ 0;
so 𝔫 ≤ p_0. ∎

**Lemma {#lem:sp-block}** (Block triangular matrices.) Let 𝔐(ϰ) be a square matrix polynomial, block lower
triangular with square diagonal blocks D_0(ϰ), …, D_q(ϰ), and let each det D_k be a non-zero polynomial with at most
a simple zero at ϰ_0. Then dim 𝒦_𝔫(𝔐, ϰ_0) ≤ Σ_k dim ker D_k(ϰ_0) for every 𝔫 ≥ 1. If
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0), then p(𝔐, ϰ_0) ≤ 1.

*Proof.* First let q = 0 and D := D_0. As D(ϰ)⁻¹ = adj D(ϰ)/det D(ϰ) has at most a simple pole at ϰ_0,
[[lem:sp-pole-order]] gives p(D, ϰ_0) ≤ 1. Let (m_0, …, m_(𝔫−1)) ∈ 𝒦_𝔫(D, ϰ_0) with 𝔫 ≥ 2. Then m_0 = 0, since
otherwise (m_0, m_1) would be a Jordan chain of length 2; and then [[eq:sp-chain]] for (m_j) is [[eq:sp-chain]] for
(m_1, …, m_(𝔫−1)) ∈ 𝒦_(𝔫−1)(D, ϰ_0). By induction on 𝔫, 𝒦_𝔫(D, ϰ_0) consists of the tuples (0, …, 0, w) with
w ∈ ker D(ϰ_0), and has dimension dim ker D(ϰ_0). In general write each vector as (x, y), x its first block. The
block rows of [[eq:sp-chain]] belonging to the first block involve only the first blocks, 𝔐 being block lower
triangular; so (x_j) ∈ 𝒦_𝔫(D_0, ϰ_0), and if every x_j vanishes, (y_j) ∈ 𝒦_𝔫(𝔐′, ϰ_0), 𝔐′ the matrix formed by the
blocks 1, …, q. Hence dim 𝒦_𝔫(𝔐, ϰ_0) ≤ dim 𝒦_𝔫(D_0, ϰ_0) + dim 𝒦_𝔫(𝔐′, ϰ_0), and induction on q gives the bound.
If p(𝔐, ϰ_0) ≥ 2, a Jordan chain (m_0, m_1) and the tuples (0, w), w ∈ ker 𝔐(ϰ_0), span a subspace of 𝒦_2(𝔐, ϰ_0)
of dimension dim ker 𝔐(ϰ_0) + 1, since its elements with first entry 0 are the (0, w). When
dim ker 𝔐(ϰ_0) = Σ_k dim ker D_k(ϰ_0) this exceeds the bound. ∎

#### Moments {#sec:sp-moments}

**Definition {#def:sp-moments}** (Moments.) Let k ∈ ℕ_0, c > k + 1 and s′ ∈ ℝ. For u ∈ Ḣ^(s′,c)_b(sf_(≥−1)) the
*k-th moment* 𝔮_k(u) is the distribution on 𝕊³, with values in ℂ^15 in the frame of [[sec:iii-g-1-1]], given by

    ⟨𝔮_k(u), ψ⟩ := ⟨u, v^k ψ⟩,     ψ ∈ C^∞(𝕊³; ℂ^15),                                                   {#eq:sp-moment}

the pairing of distributions on ℝ_v × 𝕊³ with the measure |dv| dg̸ (componentwise, bilinear). It is well defined and
continuous on Ḣ^(s′,c)_b: (1 − χ_∂)u is supported in [−1, 4] × 𝕊³, where v^kψ is smooth; and near R = 0, where
v^k|dv| dg̸ = R^(−k−1)μ_b with μ_b = |dR/R| dg̸, χ_∂u lies in H^(s′)_(b,c), while R^(−k−1)ψ ∈ 𝒜^(−k−1) lies in
H^∞_(b,−k−1−ϵ) ⊂ H^(−s′)_(b,−c) for 0 < ϵ ≤ c − k − 1 ([[lem:i-c-2-2]] (f)), so [[lem:i-c-2-2]] (d) applies. For u
in C_c^∞((−1, ∞) × 𝕊³), 𝔮_k(u) = ∫ v^k u dv. Operators acting on 𝕊³ alone (multiplication by smooth endomorphisms
of ω, derivatives in ω) commute with 𝔮_k.

**Lemma {#lem:sp-moments}** (Moments of the spectral family.) Let k ∈ ℕ_0, c > k + 1, s′ ∈ ℝ and
u ∈ Ḣ^(s′,c)_b. Then for every ϰ ∈ ℂ

    𝔮_k(N_sf(ϰ)u) = L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔮_k(u) + 2k(ϰ − k − 3/2 − S̄)𝔮_(k−1)(u),                    {#eq:sp-moments}

the last term being absent for k = 0. The identity obtained by applying ∂_ϰ^i to both sides holds, with N_sf^(i)(ϰ)
on the left.

*Proof.* N_sf(ϰ) maps Ḣ^(s′,c)_b to Ḣ^(s′−2,c)_b boundedly ([[sec:iii-g-1-2]]), and 𝔮_k and 𝔮_(k−1) are continuous
on these spaces; so both sides of [[eq:sp-moments]] are continuous in u. C_c^∞((−1, ∞) × 𝕊³) is dense in
Ḣ^(s′,c)_b, near v = −1 by [[lem:i-a-6-1]] (a) and near R = 0 by [[lem:i-c-2-2]] (d), glued with χ_∂. For such u,
integration by parts in v at fixed ω gives, for every g smooth with compact support in v,

    ∫ v^k ∂_v g dv = −k ∫ v^(k−1) g dv,     ∫ v^k (v∂_v) g dv = −(k + 1) ∫ v^k g dv,

and the second gives ∫ v^k F(v∂_v)g dv = F(−k − 1)∫ v^k g dv for every polynomial F whose coefficients act on 𝕊³
alone. In [[eq:iii-g-1-3]] put g := (v∂_v + ϰ − 3/2 − S̄)u. The first term −2∂_vg contributes
2k∫ v^(k−1)g dv = 2k(ϰ − 3/2 − S̄ − k)𝔮_(k−1)(u), and the second, L̃(0)(ω, v∂_v + ϰ, ∂_ω)u, contributes
L̃(0)(ω, ϰ − k − 1, ∂_ω)𝔮_k(u). For fixed u both sides are polynomials in ϰ, which gives the last statement. ∎

**Lemma {#lem:sp-primitive}** (Integration in v.) Let Re ϰ_0 ≥ 2, let (s, c) be admissible for every ϰ in a disc about
ϰ_0, with c > 1, and let (u_0, …, u_(𝔫−1)) ∈ 𝒦_𝔫(N_sf, ϰ_0) in the space 𝒳 of (s, c), with 𝔮_0(u_j) = 0 for every j.
Let Iu_j be the distribution on ℝ_v × 𝕊³ with ∂_v Iu_j = u_j that vanishes on {v < −1}. Then for every c′ < c − 1:

(a) u_j ∈ Ḣ^((s;∞),c)_(b;b) and Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b);

(b) (Iu_0, …, Iu_(𝔫−1)) ∈ 𝒦_𝔫(N_sf, ϰ_0 − 1) in the space 𝒳 of the pair (s + 1, c′), which is admissible for ϰ_0 − 1
when c′ > Re ϰ_0 − 2;

(c) 𝔮_k(Iu_j) = −(k + 1)⁻¹𝔮_(k+1)(u_j) for every integer k with 0 ≤ k < c − 2.

*Proof.* (a) By [[eq:sp-chain]], N_sf(ϰ_0)u_j = −N_sf′(ϰ_0)u_(j−1) − ½N_sf″(ϰ_0)u_(j−2), where by [[eq:iii-g-1-2]] and
[[eq:iii-g-1-3]] N_sf′(ϰ) = −2∂_v − 2(v∂_v + ϰ) + a(ω) and N_sf″ = −2. These operators map Ḣ^((s;k),c)_(b;b) into
Ḣ^((s−1;k),c)_(b;b) for every k: near v = 0 because ∂_v(v∂_v) = (v∂_v + 1)∂_v and ∂_v commutes with the ℒ_Ω, so
that words pass through ∂_v, and near R = 0 because ∂_v = −R(R∂_R). By induction on j, [[thm:iii-g-5-1]] (3) gives
u_j ∈ Ḣ^((s;∞),c)_(b;b). Near R = 0 this space is H^∞_(b,c) ([[sec:iii-g-1-2]]), so |W^αu_j| ≤ C_αv^(−c) on
{v ≥ 4} for every word W^α in v∂_v and the ℒ_Ω ([[lem:i-c-2-2]] (f)). Let W̃^α be W^α with every v∂_v replaced by
v∂_v + 1 (W̃^α = Id for the empty word). Then W^αI = IW̃^α, as v∂_vI = I(v∂_v + 1) (both sides vanish on {v < −1}
and have the same v-derivative) and the ℒ_Ω commute with I. Put g := W̃^αu_j. It lies in Ḣ^(s−|α|,c)_b, |α| the
length of the word, and |g| ≤ C′_αv^(−c) on {v ≥ 4}. Moreover 𝔮_0(g) = 0. Indeed 𝔮_0 commutes with the ℒ_Ω,
𝔮_0(u_j) = 0, and 𝔮_0((v∂_v + 1)w) = 0 for every w ∈ Ḣ^(s′,c)_b, s′ ∈ ℝ: for w ∈ C_c^∞((−1, ∞) × 𝕊³) it is
∫ ∂_v(vw) dv = 0, such w are dense ([[lem:i-a-6-1]] (a), [[lem:i-c-2-2]] (d), as in the proof of [[lem:sp-moments]]),
and w ↦ 𝔮_0((v∂_v + 1)w) is continuous, v∂_v + 1 mapping Ḣ^(s′,c)_b into Ḣ^(s′−1,c)_b ([[def:sp-moments]], c > 1).
Moving the ℒ_Ω at the left end of W̃^α through 𝔮_0, one reaches either a factor
v∂_v + 1, which gives 0, or, if W̃^α has none, 𝔮_0(u_j) = 0. Take χ ∈ C^∞(ℝ) equal to 1 on (−∞, 3] and to 0 on
[4, ∞). Then I(χg) is constant on {v ≥ 4}, equal to ⟨χg, 1⟩, and so, on {v ≥ 4},

    W^αIu_j(v) = Ig(v) = ⟨χg, 1⟩ + ∫_3^v (1 − χ)g dv′ = 𝔮_0(g) − ∫_v^∞ g dv′ = −∫_v^∞ g dv′.

So |W^αIu_j| ≤ C′_αv^(1−c)/(c − 1) on {v ≥ 4}, for every word W^α; hence Iu_j ∈ 𝒜^(c−1) ⊂ H^∞_(b,c′) near R = 0
([[lem:i-c-2-2]] (f)). On {v < 5} we use W^αIu_j = I(W̃^αu_j) again. By (i) of the proof of
[[lem:iii-g1-2-1]] each W̃^αu_j lies in H^s(ℝ; H^m(𝕊³)) for every m; the primitive maps this space into
H^(s+1)(ℝ; H^m(𝕊³)) locally ((iii) (α) there); and the latter lies in H^(s+1) for m large, as in (i) there. So
Iu_j ∈ Ḣ^((s+1;∞),c′)_(b;b).

(b) By [[lem:iii-g-1-2]] (e), N_sf(ϰ + 1)∂_v = ∂_vN_sf(ϰ) for every ϰ; differentiating in ϰ,
N_sf^(i)(ϰ_0)∂_v = ∂_vN_sf^(i)(ϰ_0 − 1). So F_j := Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) has
∂_vF_j = Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i) = 0; F_j vanishes on {v < −1} and does not depend on v, hence F_j = 0.
By (a), Iu_j ∈ Ḣ^(s+1,c′)_b, and N_sf(ϰ_0 − 1)Iu_j = −Σ_(i≥1)(i!)⁻¹N_sf^(i)(ϰ_0 − 1)Iu_(j−i) lies in Ḣ^(s,c′)_b, the
operator N_sf′ being of first order; so Iu_j lies in 𝒳 for (s + 1, c′). The pair is admissible for ϰ_0 − 1: s + 1 <
2 − Re(ϰ_0 − 1) as s < 2 − Re ϰ_0, and c′ ∈ (Re ϰ_0 − 2, Re ϰ_0 − 1) as c′ < c − 1 < Re ϰ_0 − 1.

(c) Both moments are defined, choosing c′ ∈ (k + 1, c − 1). Let φ ∈ C_c^∞(ℝ) equal 1 on [−2, 1], put φ_T(v) := φ(v/T)
for T > 4, and let ψ ∈ C^∞(𝕊³; ℂ^15). As ∂_vIu_j = u_j,

    ⟨Iu_j, (k + 1)φ_Tv^kψ⟩ + ⟨Iu_j, φ_T′v^(k+1)ψ⟩ = −⟨u_j, φ_Tv^(k+1)ψ⟩.

As T → ∞ the first and last terms tend to (k + 1)⟨𝔮_k(Iu_j), ψ⟩ and −⟨𝔮_(k+1)(u_j), ψ⟩ (dominated convergence on
{v ≥ 4}, with the bounds of (a)), and the middle one is O(T^(−1)·T^(k+1)·T^(1−c)·T) = O(T^(k+2−c)), which tends to 0. ∎

#### The moment matrix {#sec:sp-matrix}

**Definition {#def:sp-matrix}** (The moment matrix.) For a type τ and K ∈ ℕ_0 let 𝔐^K_τ(ϰ) be the matrix polynomial
of size (K + 1)n_τ, block lower bidiagonal with blocks of size n_τ, whose blocks are

    (𝔐^K_τ)_(kk)(ϰ) = N_τ(ϰ − k − 1)  (0 ≤ k ≤ K),     (𝔐^K_τ)_(k,k−1)(ϰ) = 2k(ϰ − k − 3/2 − S_τ)  (1 ≤ k ≤ K),
                                                                                                      {#eq:sp-matrix}

all other blocks being 0. So det 𝔐^K_τ(ϰ) = ∏_(k=0)^K det N_τ(ϰ − k − 1). For Re ϰ_0 ≥ 2 write 𝔐_τ := 𝔐^(K(ϰ_0))_τ,
and let c_τ(ϰ_0) be the order of the zero of det 𝔐_τ at ϰ_0: the number of roots μ of type τ, with multiplicity,
with ϰ_0 − μ ∈ {1, …, K(ϰ_0) + 1}. Each such root has Re μ ≥ Re ϰ_0 − K(ϰ_0) − 1 = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 ≥ 1,
hence Re μ > 1, as no root has real part in (0, 1], and is therefore singular.

By [[eq:sp-moments]], the moments (𝔮_k(u))_(k≤K) of N_sf(ϰ)u are obtained from those of u by the operator 𝔐(ϰ) on
𝒟′(𝕊³; ℂ^15)^(K+1) defined by the right side of [[eq:sp-moments]]; on W_π^(K+1) it acts as 𝔐^K_τ(ϰ) ⊗ Id_π.

**Theorem {#thm:sp-reduction}** (The poles of the spectral family in {Re ≥ 2}.) Let Re ϰ_0 ≥ 2 and K := K(ϰ_0), and
let 𝒳, 𝒴 be the spaces of a pair admissible for every ϰ in a disc about ϰ_0.

(a) For every 𝔫 ≥ 1 the map (u_j)_(j<𝔫) ↦ ((𝔮_k(u_j))_(k≤K))_(j<𝔫) is a bijection from 𝒦_𝔫(N_sf, ϰ_0) onto
𝒦_𝔫(𝔐, ϰ_0) := ⊕_π 𝒦_𝔫(𝔐_τ(π) ⊗ Id_π, ϰ_0), τ(π) the type of π, the space of the chains of 𝔐 in
𝒟′(𝕊³; ℂ^15)^(K+1): the tuples there that satisfy [[eq:sp-chain]] for 𝔐, which commutes with the projections onto the
W_π^(K+1). Only finitely many summands are non-zero.

(b) dim ker N_sf(ϰ_0) = Σ_τ d_τ dim ker 𝔐_τ(ϰ_0), and the order of the pole of N_sf(·)⁻¹ at ϰ_0 is the largest of the
numbers p(𝔐_τ, ϰ_0), each of which is at most c_τ(ϰ_0).

(c) ϰ_0 ∈ 𝒫 if and only if ϰ_0 = μ + j with μ a singular root and j ≥ 1 an integer. So
𝒫 ∩ {Re ≥ 2} = {μ + j : μ a singular root of some type, j ∈ ℕ, j ≥ 1}.

(d) If c_τ(ϰ_0) ≤ 1 for every type, then ϰ_0 is at most a simple pole of N_sf(·)⁻¹.

*Proof.* Write (s, c) for the pair; c ∈ (Re ϰ_0 − 1, Re ϰ_0) by [[eq:iii-g-2-6]], and the poles of N_sf(·)⁻¹ and their
orders do not depend on the pair ([[thm:iii-g-5-1]] (2)). Then c > K + 1, as K + 1 ≤ Re ϰ_0 − 1. By [[lem:sp-primitive]]
(a) the elements of a tuple of 𝒦_𝔫(N_sf, ϰ_0) lie in Ḣ^(s,c)_b, so their moments of order at most K are defined, and by
[[lem:sp-moments]] (with its derivatives) they form a tuple of 𝒦_𝔫(𝔐, ϰ_0). The components on the W_π are tuples of
𝒦_𝔫(𝔐_τ(π) ⊗ Id_π, ϰ_0), which vanish unless det 𝔐_τ(π)(ϰ_0) = 0, that is unless π has a root among ϰ_0 − 1, …, ϰ_0 − K −
1; by [[lem:iii-f1-2-4]] with X := Re ϰ_0 this holds for a finite set F of representations only.

*Injectivity.* Let (u_j) ∈ 𝒦_𝔫(N_sf, ϰ_0) have all moments of order at most K equal to 0. Choose η > 0 with
(K + 1)η < c − Re ϰ_0 + 1 and put c_i := c − i(1 + η). We show by induction on i ≤ K + 1 that (I^iu_j) ∈
𝒦_𝔫(N_sf, ϰ_0 − i) in the space 𝒳 of the pair (s + i, c_i), admissible for ϰ_0 − i, with 𝔮_k(I^iu_j) = 0 for
k ≤ K − i. For i = 0 this is the hypothesis. If it holds for i ≤ K, then 𝔮_0(I^iu_j) = 0, c_i > Re ϰ_0 − 1 − i ≥
K + 1 − i ≥ 1, and [[lem:sp-primitive]] with c′ := c_(i+1) ∈ (Re ϰ_0 − i − 2, c_i − 1) gives the statement for i + 1,
the moments by its part (c) (k ≤ K − i − 1 < c_i − 2). At i = K + 1, Re(ϰ_0 − K − 1) = Re ϰ_0 − ⌊Re ϰ_0⌋ + 1 < 2, so
N_sf(ϰ_0 − K − 1) is injective ([[prop:iii-g-3-2]]); by [[eq:sp-chain]] and induction on j, I^(K+1)u_j = 0 for every
j. As ∂_v^(K+1)I^(K+1)u_j = u_j, every u_j vanishes.

*Surjectivity.* Let T_𝔫: 𝒳^𝔫 → 𝒴^𝔫, (u_j) ↦ (Σ_(i≤j)(i!)⁻¹N_sf^(i)(ϰ_0)u_(j−i))_j, so that 𝒦_𝔫(N_sf, ϰ_0) = ker T_𝔫.
N_sf(ϰ_0) is Fredholm of index 0 ([[thm:iii-g-5-1]] (1)); choose Φ: 𝒳 → 𝒴 of finite rank with N_sf(ϰ_0) + Φ
invertible, as in the proof of [[thm:iii-g-5-1]]. T_𝔫 + diag(Φ, …, Φ) is block lower triangular with invertible
diagonal blocks, hence invertible (solve row by row); so T_𝔫 = B(Id − G) with B invertible and G of finite rank. For
such an operator dim ker T_𝔫 = codim ran T_𝔫. Indeed, let E ⊃ ran G be finite-dimensional; A := Id − G maps E into
E, every x with Ax = 0 lies in E, A induces the identity on 𝒳^𝔫/E, and if Ax ∈ E then x ∈ E. So ran A + E = 𝒳^𝔫
and ran A ∩ E = A(E), whence codim ran A = dim E − dim A(E) = dim ker(A|_E) = dim ker A. Now let V := ⊕_(π∈F) W_π^(K+1)
and Ψ: 𝒴^𝔫 → V^𝔫 the map taking (f_j) to the components in V of the moments (𝔮_k(f_j))_(k≤K). It is onto: for
χ_0, …, χ_K ∈ C_c^∞((1, 2)) with ∫ v^iχ_k dv = δ_(ik) (they exist, the powers being linearly independent on (1, 2)),
the sources Σ_k χ_k(v)w_k, w_k ∈ V, lie in 𝒴 and have moments w_k. By [[lem:sp-moments]],
Ψ(T_𝔫u) = T^𝔐_𝔫(moments of u), T^𝔐_𝔫 the operator of [[eq:sp-chain]] for 𝔐 on V^𝔫, a square matrix. So Ψ maps
ran T_𝔫 into ran T^𝔐_𝔫, and

    dim ker T_𝔫 = codim ran T_𝔫 ≥ dim V^𝔫 − rank T^𝔐_𝔫 = dim ker T^𝔐_𝔫 = dim 𝒦_𝔫(𝔐, ϰ_0).

With the injectivity, the map is a bijection. This proves (a).

(b) The case 𝔫 = 1 of (a) gives the dimension, as dim(ker 𝔐_τ(ϰ_0) ⊗ π) summed over the π of type τ is
d_τ dim ker 𝔐_τ(ϰ_0). A tuple of 𝒦_𝔫(N_sf, ϰ_0) has u_0 ≠ 0 exactly when the moments of u_0 do not all vanish (the
case 𝔫 = 1 of (a)), so the bijection maps Jordan chains onto Jordan chains, and p(N_sf, ϰ_0) is the largest of the
p(𝔐_τ ⊗ Id_π, ϰ_0) = p(𝔐_τ, ϰ_0). By [[lem:sp-pole-order]], applied on a disc about ϰ_0 on which 𝒫 has no other point,
p(N_sf, ϰ_0) is the order of the pole of N_sf(·)⁻¹. And 𝔐_τ(ϰ)⁻¹ = adj 𝔐_τ(ϰ)/det 𝔐_τ(ϰ) has a pole of order at most
c_τ(ϰ_0), so p(𝔐_τ, ϰ_0) ≤ c_τ(ϰ_0) by [[lem:sp-pole-order]].

(c) By (b), ϰ_0 ∈ 𝒫 if and only if det 𝔐_τ(ϰ_0) = 0 for some type, that is ϰ_0 − j is a root for some j ∈
{1, …, K + 1}; such a root is singular ([[def:sp-matrix]]). Conversely, if μ is singular and j ≥ 1, then ϰ_0 := μ + j
has Re ϰ_0 > j + 1, so K(ϰ_0) ≥ j − 1, and det 𝔐_τ(ϰ_0) = 0. (d) follows from (b). ∎

On spacetime the moments have a direct meaning. For u ∈ ker N_sf(ϰ_0), U := ρ^(ϰ_0)u is a solution of 2L̄U = 0,
homogeneous of degree −ϰ_0 and supported in {t̄ ≥ |x|} ([[sec:iii-g-1-1]], Step 1 of the proof of [[prop:iii-g-3-2]]);
as dt̄ = r dv at fixed x, its integral in t̄ along each line {x = const} is r^(1−ϰ_0)𝔮_0(u), and by [[eq:sp-moments]]
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

**Lemma {#lem:sp-two-roots}** (The chains at ϰ_0 = 5.) Let W = Σ_i W_i dx^i with W_i linear, Σ_i x_iW_i = 0 and
∂_iW_j + ∂_jW_i = 0 (a rotation 1-form, of vector type 1), and V̂ := r⁻¹W. Put

    K_s0 := Σ_i (dx^i)² − 4 dr²,     K_v1 := dr ⊗_s V̂,     Z := −6e_Υ dt̄² + (4 − e_Υ)Σ_i (dx^i)² − (4 + 2e_Υ) dr².

(a) For K = K_s0 and K = K_v1, and every ι ∈ ℂ,

    L̃(0)(ω, ι, ∂_ω)K = (ι − 4)(2S̄ − ι − 2)K.                                                            {#eq:sp-gauge}

(b) L̃(0)(ω, 2, ∂_ω)Z = 4(e_Υ + 2)K_s0.

(c) For every value of the parameters with 1, 3 not roots of type s0 and 1, 2 not roots of type v1, and the roots 2,
4 of type s0 and 3, 4 of type v1 simple, dim ker 𝔐_τ(5) = 2 and p(𝔐_τ, 5) = 1 for τ = s0 and τ = v1.

*Proof.* L̃(0)(ω, ι, ∂_ω)K is defined by (2L̄)^(0)(r^(−ι)K) = r^(−ι−2)L̃(0)(ω, ι, ∂_ω)K, and (2L̄)^(0) is 2L̄ on
stationary sections ([[lem:iii-f-2-1]] (2)): by [[eq:iii-f-2-1]], (2L̄)^(0)u = □̄u + 2Ē^Cδ̄Ḡu + 2(δ̄* + Ē^C)Ē^ΥḠu, where
on stationary sections □̄ acts in the Cartesian frame as −Δ on each component and (δ̄k)_μ = −Σ_j ∂_jk_(μj). We use, on
ℝ⁴ and for real or complex a,

    Δr^a = a(a + 2)r^(a−2),     Δ(r^an_in_j) = r^(a−2)((a − 2)(a + 4)n_in_j + 2δ_(ij)),
    ∂_j(r^aδ_(ij)) = a r^(a−1)n_i,     ∂_j(r^an_in_j) = (a + 3)r^(a−1)n_i,
    ∂_j(r^ax_iW_j) = r^aW_i,     ∂_j(r^ax_jW_i) = (a + 5)r^aW_i,
    Δ(r^a(x_iW_j + x_jW_i)) = a(a + 6)r^(a−2)(x_iW_j + x_jW_i).

The second and the last follow from Δ(fg) = (Δf)g + 2∇f·∇g + fΔg with x·∇(x_ix_j) = 2x_ix_j, Δ(x_ix_j) = 2δ_(ij),
x·∇(x_iW_j) = 2x_iW_j and Δ(x_iW_j) = 2∂_iW_j, the Killing equation removing the last term after symmetrising; the
third and fourth are direct, as ∂_j(x_ix_j) = 5x_i; the fifth and sixth follow from x·W = 0, ∂_jW_j = 0 (a consequence
of the Killing equation) and x·∇W_i = W_i.

(a) Let u := r^(−ι)K. Then tr u = 0 (tr Σ(dx^i)² = 4, tr dr² = 1, ⟨dr, V̂⟩ = 0) and ι_(∂_t̄)u = 0, so Ḡu = u and,
as c̄_Υ^♯ = −r⁻¹∂_t̄, Ē^ΥḠu = −γ_Υ(2ι_(c̄_Υ^♯)u − e_Υc̄_Υ tr u) = 0 ([[sec:iii-f1-1]]). For K_s0, u_(ij) =
r^(−ι)(δ_(ij) − 4n_in_j), and the identities give Δu = (ι + 2)(ι − 4)r^(−2)u and δ̄u = −3(ι − 4)r^(−ι−1)dr. For K_v1,
u_(ij) = ½r^(−ι−2)(x_iW_j + x_jW_i), and they give Δu = (ι + 2)(ι − 4)r^(−2)u and δ̄u = ½(ι − 4)r^(−ι−1)V̂. In both cases
δ̄u = −(ι − 4)r⁻¹ι_Xu with X := ḡ⁻¹dt_* = −∂_t̄ − ∂_r, since ι_Xu = −ι_(∂_r)u equals 3r^(−ι)dr for K_s0 and −½r^(−ι)V̂
for K_v1. By [[eq:iii-f-2-2]], ρS̄u = −Ē^Cι_XḠu + (dt_* ⊗_s ·)Ē^ΥḠu = −Ē^C(ι_Xu). Hence

    (2L̄)^(0)u = −(ι + 2)(ι − 4)r^(−2)u − 2(ι − 4)r⁻¹Ē^C(ι_Xu) = (ι − 4)r^(−2)(2S̄ − ι − 2)u,

which is [[eq:sp-gauge]].

(b) Let u := r^(−2)Z. Then tr Z = 6e_Υ + 4(4 − e_Υ) − (4 + 2e_Υ) = 12 and ι_(∂_t̄)Z = −6e_Υ dt̄, so
Ē^ΥḠu = −γ_Υ(2·6e_Υ − 12e_Υ)r^(−3)dt̄ = 0. Next Ḡu = r^(−2)((6 − 6e_Υ)dt̄² − (2 + e_Υ)Σ(dx^i)² − (4 + 2e_Υ)dr²) has
no mixed time–space components, and by the identities
Σ_j∂_j(r^(−2)((2 + e_Υ)δ_(ij) + (4 + 2e_Υ)n_in_j)) = (−2(2 + e_Υ) + (4 + 2e_Υ))r^(−3)n_i = 0; so δ̄Ḡu = 0.
Finally Δ(r^(−2)) = 0, so Δ(r^(−2)dt̄²) = 0 and Δ(r^(−2)δ_(ij)) = 0, while Δ(r^(−2)n_in_j) = r^(−4)(2δ_(ij) −
8n_in_j). The terms of (2L̄)^(0)u other than □̄u vanish, so
(2L̄)^(0)u = □̄u = (4 + 2e_Υ)r^(−4)(2δ_(ij) − 8n_in_j)dx^idx^j = 4(e_Υ + 2)r^(−4)K_s0.

(c) K_s0 and Z are invariant under SO(4), of type s0. The rotation 1-forms are the sum of the two irreducible
representations π of vector type 1; for W in one of them, K_v1 lies in W_π = ℂ² ⊗ π. Let k_τ ∈ ℂ^(n_τ) be the vector
with K_s0 = k_s0, resp. K_v1 = k_v1 ⊗ W, and z the one of Z. By (a), N_τ(ι)k_τ = (ι − 4)(2S_τ − ι − 2)k_τ, so k_τ
spans ker N_τ(4), the root 4 being simple. K(5) = 3, and by [[eq:sp-matrix]] a vector (μ_0, μ_1, μ_2, μ_3)
lies in ker 𝔐_τ(5) exactly when

    N_τ(4)μ_0 = 0,  N_τ(3)μ_1 = −2(5/2 − S_τ)μ_0,  N_τ(2)μ_2 = −4(3/2 − S_τ)μ_1,  N_τ(1)μ_3 = −6(1/2 − S_τ)μ_2.

*Type s0.* N_s0(3) and N_s0(1) are invertible. By (a) at ι = 3, N_s0(3)k_s0 = 2(5/2 − S_s0)k_s0, so μ_0 := k_s0
gives μ_1 = −k_s0. By (a) at ι = 2, N_s0(2)k_s0 = 4(2 − S_s0)k_s0, so −4(3/2 − S_s0)μ_1 = N_s0(2)k_s0 − 2k_s0, which
by (b) equals N_s0(2)(k_s0 − z/(2(e_Υ + 2))). So μ_2 := k_s0 − z/(2(e_Υ + 2)) and
μ_3 := −6N_s0(1)⁻¹(1/2 − S_s0)μ_2 complete a kernel vector with μ_0 ≠ 0. A second one is (0, 0, w, μ_3), w spanning
ker N_s0(2) and μ_3 := −6N_s0(1)⁻¹(1/2 − S_s0)w. *Type v1.* N_v1(2) and N_v1(1) are invertible. For μ_0 := a k_v1
and w ∈ ker N_v1(3), μ_1 := −a k_v1 + w solves the second equation, by (a) at ι = 3, and μ_2, μ_3 are then determined;
this gives kernel vectors for every (a, w). In both cases dim ker 𝔐_τ(5) ≥ 2 = Σ_k dim ker N_τ(4 − k). The
diagonal blocks of 𝔐_τ(ϰ) are N_τ(ϰ − k − 1), k ≤ 3, whose determinants are non-zero polynomials with at most a
simple zero at ϰ = 5, as 4 − k is a simple root of type τ or not a root, by the hypotheses. So [[lem:sp-block]]
gives equality and p(𝔐_τ, 5) ≤ 1, and p(𝔐_τ, 5) = 1 as the kernel is non-zero. ∎

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

At sl with l ≥ 3 the elements of 𝒮_sl are ι − 1 for the roots ι of P_l with real part in (2, 5], and the list
carries such an entry as often as the multiplicity of ι as a root of P_l. If x ≤ 70, these roots are among the three
roots of real part at least 2, counted with multiplicity, which by [[cor:s14-remote-point]] are the roots of
[[lem:s14-sextic-count]] (a): for 3 ≤ l ≤ 133, three distinct real roots in (2, 3) ([[lem:s14-sextic-small]] (c));
for l ≥ 134 (x ≥ 0.018), a real root ι_B and two more, which for x ≤ 0.03 lie in |ι − a| < 0.45, a disc disjoint
from the disc of ι_B, and have real parts in (2.06, 2.98) while ι_B ∈ (2.0179, 2.03], and which for x ≥ 0.03 are
non-real and conjugate, ι_P and ι̅_P, in disjoint discs ([[lem:s14-sextic-large]] and the proof of
[[prop:s14-damping-distance]]).

For 0.018 ≤ x ≤ 0.03, that is 134 ≤ l ≤ 172 (x = 0.018224 at l = 134 and x = 0.029928 at l = 172), the two roots in |ι −
a| < 0.45 are distinct. By [[lem:s14-majorant]], the bound |hW| ≤ h(M̄_a(0.45, 0.03) + hN̄(2.98, 0.03)) < 9.4·10⁻⁵ of the
proof of [[lem:s14-sextic-large]] (b) holds on the whole closed disc |ι − a| ≤ 0.45, as there |ι| ≤ a + 0.45 ≤ 2.9725 <
2.98. For real ι in that disc, 2 + x − ι ≤ 2 + x − a + 0.45 = x/4 − 0.05 ≤ −0.0425. As 3x + 10 = 4a and Δ_𝒬 is the
discriminant of 𝒬(·, x) ([[lem:s14-sextic-split]] (iii)), completing the square gives 𝒬(ι, x) = 2(ι − a)² − Δ_𝒬(x)/8.
Further Δ_𝒬 decreases on [0, 107], its derivative being 2x − 1715/8, and its smaller root x₋ lies in (0.01866, 0.01867)
(loc. cit.). If l = 134 or 135, then x = 0.018224 or 0.018495 lies below x₋, and Δ_𝒬(x) = 0.093562114176 or
0.035476440025. As 2 + x − a = −(2 − x)/4, U(a, x) = (2 − x)Δ_𝒬(x)/32, which is 0.0057943… or 0.0021967…, so U(a, x) >
2·10⁻³; while 𝒬(a ± 0.45, x) = 0.405 − Δ_𝒬(x)/8 > 0.39, so U(a ± 0.45, x) < −0.0425·0.39 < −0.016. Hence P_l = U + hW is
negative at a − 0.45, positive at a and negative at a + 0.45, and it has a real root in each of (a − 0.45, a) and (a, a +
0.45): these are the two roots in the disc, and they are distinct. If 136 ≤ l ≤ 172, then x ≥ 0.018768 > x₋, so Δ_𝒬(x) ≤
Δ_𝒬(0.018768) = −0.023037762176, and for real ι 𝒬(ι, x) ≥ −Δ_𝒬(0.018768)/8 = 0.002879720272 > 2.87·10⁻³. On the real
diameter of the disc, then, |U| > 0.0425·2.87·10⁻³ > 1.2·10⁻⁴ > |hW|, and P_l has no real root in the disc. As P_l has
real coefficients and the disc is symmetric about ℝ, conjugation permutes the roots in the disc with their
multiplicities, and a non-real root of multiplicity 2 would bring its conjugate with the same multiplicity, four roots in
the disc in all. So the two roots are a non-real conjugate pair, and they are distinct.

In each case, therefore, the three roots of real part at least 2 are distinct, so each is a simple root of P_l, and no
two differ by a non-zero integer: for any two, either their real parts differ by less than 1 or their difference is
not real. If x > 70, no root of P_l satisfies |ι − 1| ≤ 50 ([[lem:s14-sextic-count]] (b)), so a real root of real
part at least 2 exceeds 51. The three roots of real part at least 2, counted with multiplicity
([[prop:s14-scalar-every-h]]), are permuted by conjugation with their multiplicities, P_l having real coefficients; a
non-real one of multiplicity at least 2 would bring its conjugate with the same multiplicity, four roots in all. So the
non-real ones are simple, and, three being odd, they form at most one conjugate pair. Those of real part at most 5 are
therefore non-real simple roots, at most two; if there are two, they are ι and ι̅ with Im ι ≠ 0, which neither
coincide nor differ by a real number, ι − ι̅ = 2i Im ι.

(b) An element μ of 𝒮_τ is an entry of the list of type τ, and the list gives the roots with multiplicity. μ differs
from the entries of real part at most 0 or greater than 4 by its real part, and from the entries for the other
elements of 𝒮_τ by (c). An entry ι − 1 from □^C occurs as often as the multiplicity of ι as a root of C, P_l or p_(v),
and that multiplicity is 1: ι₁ is a simple root of C, whose other two roots have real part below −100; ι_v(l) is one of
the two distinct real roots of the quadratic p_(v) ([[lem:s14-vector-distance]]); the roots of P_1 and P_2 concerned
lie one in each of three disjoint intervals, of three roots counted with multiplicity ([[lem:s14-sextic-small]] (a),
(b)); and those of P_l, l ≥ 3, are simple by the proof of (c). So μ is a simple root. ∎

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

    c_0(5/2) = 102,382,116,069,206,441,391/(2¹²·10¹⁷),
    c_0(7/2) = −184,309,587,192,075,727,923/(2¹³·10¹⁶),
    c_0(9/2) = −7,679,697,448,702,749,433,821/(2¹²·10¹⁷),
    c_0(25099/10000) = 1,019,224,980,784,674,272,031,997,531,559,760,391,559,271/(4·10⁴²),
    c_0(35099/10000) = −9,299,228,494,721,864,136,714,649,149,276,457,696,950,729/(4·10⁴²),
    c_0(45099/10000) = −76,091,116,104,307,206,847,501,599,126,784,137,785,460,729/(4·10⁴²),
    c_0(251/100) = 4,077,667,112,282,805,096,193,344,619,959/(16·10³⁰),
    c_0(351/100) = −37,209,137,195,213,265,101,596,444,677,141/(16·10³⁰),
    c_0(451/100) = −304,408,877,927,380,731,996,608,663,774,241/(16·10³⁰),
    c_0(63/25) = 126,728,556,223,578,619,714,117,857/(5¹¹·10¹⁹),
    c_0(88/25) = −2,346,368,372,779,440,282,518,355,711/(5¹⁰·10²⁰),
    c_0(113/25) = −2,356,501,507,010,040,363,609,315,267/(5¹³·10¹⁷),

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
for the roots of P_l (for non-real ι trivially) and for ι_v(l). Finally spec S̄ = σ_Υ ∪ σ_C with σ_C ⊂ [s_C, ∞) and
s_C > 100 ([[eq:iii-g1-1-4]], [[sec:iii-f-1]]), so a point of 5/2 + spec S̄ + ℕ_0 of real part at most 5 lies in
5/2 + σ_Υ + {0, 1, 2}; a point μ + j of 𝒫 there ([[thm:sp-reduction]] (c), with Re μ ≤ 4) would have
μ ∈ 3/2 + σ_Υ + ℤ. ∎

**Theorem {#thm:sp-spectrum}** (The ι⁺-spectrum at real part at most 5.) At the computational point, and for every b
near b₀:

(a) spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} = 𝒫 ∩ {Re ϰ ≤ 5} is the union of

    {3, 4, 5},     {4 + 𝔡₀, 4 + 𝔡₁},     {ι₁, ι₁ + 1, ι₁ + 2},
    {ι + j : l ≥ 1, P_l(ι) = 0, Re ι > 2, j ∈ ℕ_0, Re ι + j ≤ 5},
    {ι_v(l) + j : 2 ≤ l ≤ 1413, j ∈ ℕ_0, ι_v(l) + j ≤ 5}.

It is finite and lies in {Re ϰ > 2}.

(b) Every point of (a) is a simple pole of N_sf(·)⁻¹ and of N_ι⁺(L̄, ·)⁻¹: Spec_ι⁺(L̄) ∩ {Re ϰ ≤ 5} consists of the
pairs (ϰ, 0), ϰ in (a). The order m_ι of [[prop:iii-g3-2-4]], that of the pole of [[eq:iii-g1-3-3]], equals 1 at
these points and 0 at every other point of {Re ϰ ≤ 5}, for every ℓ_I > 5 allowed in [[thm:iii-g1-3-1]] (2) (the
principal parts do not depend on ℓ_I, so for a smaller ℓ_I the same holds on {Re ϰ < ℓ_I}).

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
[[lem:sp-roots]] (c), c_τ(ϰ_0) ≤ 1, except c_s0(5) = 2 (the roots 4 and 2) and c_v1(5) = 2 (the roots 4 and 3).
The conditions of [[lem:sp-two-roots]] (c) hold at the computational point: by [[lem:sp-roots]] (a) the roots of
type s0 of real part in (1, 4] are 2, 3 + 𝔡₀, ι₁ − 1 ∈ (1, 3/2) and 4, and those of type v1 are 3 and 4, no root has
real part in (0, 1] ([[prop:iii-f1-2-3]] (a)), and these roots are simple ([[lem:sp-roots]] (b)). By
[[thm:sp-reduction]] (b) and [[lem:sp-two-roots]] (c), N_sf(·)⁻¹ has a simple pole at ϰ_0, and by [[prop:sp-visible]]
so has N_ι⁺(L̄, ·)⁻¹. The order of the pole of [[eq:iii-g1-3-3]], for every ℓ_I allowed in [[thm:iii-g1-3-1]] (2) with
Re ϰ_0 < ℓ_I, is that of N_ι⁺(L̄, ·)⁻¹ on Ċ^∞(ι⁺) ([[lem:iii-g1-4-2]] (b)); this gives m_ι, which vanishes at the
other points of {Re ϰ ≤ 5}, these lying outside spec_ι⁺(L̄) by (a).

(c) [[thm:sp-reduction]] (b), with dim ker 𝔐_τ(ϰ_0) = c_τ(ϰ_0): when c_τ(ϰ_0) = 1, det 𝔐_τ has a simple zero, so the
kernel is non-zero, and [[lem:sp-block]] bounds its dimension by 1; when c_τ(ϰ_0) = 2 it is [[lem:sp-two-roots]] (c).
At ϰ_0 = 3, 4, 5 the types with c_τ(ϰ_0) ≥ 1 are read off from [[lem:sp-roots]] (a); the values of d_τ are 1, 4 and 9
at s0, s1, s2, 6 and 16 at v1, v2, and 10 at t2. ∎

**Corollary {#cor:sp-lstar}** (The contribution of the poles to l_*.) At the computational point:

(a) The orders of the poles of N_ι⁺(L̄, ·)⁻¹ at real part at most 5 are all equal to 1. Of the quantities that the
number l_* of [[def:iii-i10-1-1]] bounds at real part at most 5, these orders contribute exactly 1, and the
multiplicities of the indicial roots of L̂_b(0) with real part in (1, 4] are all 1 ([[lem:sp-roots]] (b)). So the
least admissible l_* is max(1, L, M), where L is the largest logarithmic order of ℰ_ind ∪ ℰ^ι_ind ∪ ℰ^C_I at real part
at most 5 and M the largest multiplicity of an indicial root of L̂_b(0) of real part at most 5. Here M ≤ 7; and for
the index sets as constructed, with the least ℰ^C_I, 39 ≤ L ≤ 50. Hence max(1, L, M) = L: the least admissible l_* is
L ∈ [39, 50], and l_* = 50 is admissible.

(b) For ϰ ∈ Σ ([[def:iii-j-1-1]]), K_ι(ϰ) ≤ m_ι(ϰ) + m_♯(ϰ) ([[prop:iii-g3-2-4]]) with m_ι(ϰ) ∈ {0, 1}, equal to 1
exactly when ϰ is a point of [[thm:sp-spectrum]] (a); so K_ι(ϰ) ≤ 2 + k(ℰ^C_(I,♯), ϰ) ≤ l_* + 2, which is at most
2l_* + 1 as l_* ≥ 1 (52 and 101 at l_* = 50). With the least ℰ^C_I, whose logarithmic orders are all 0, m_♯(ϰ) ≤ 1;
so K_ι(ϰ) ≤ 2 for every ϰ ∈ Σ, and K_ι(ϰ) ≤ 1 unless ϰ ∈ spec_ι⁺(L̄) ∩ π_1ℰ^C_I, a set that contains 3. The pole at λ_♯
has K_ι(λ_♯) = 1; whether the value 2 is taken is not decided here.

(c) In the step of [[sec:s23-step]] at an exponent ϰ₀, the solution map 𝒮_(ϰ₀) raises the logarithmic order by at
most m_ι(ϰ₀): by at most 1 at the points of [[thm:sp-spectrum]] (a), and not at all at every other ϰ₀ with
Re ϰ₀ ≤ 5. Likewise each raise "by a pole order of N_ι⁺(L̄, ·)⁻¹" in [[lem:iii-i10-1-2]] (c) is at most 1.

(d) On {2 ≤ Re ϰ ≤ 3 + ε_+}, ε_+ < 1/4, the poles are 3; ι₁; and the roots ι of P_l (l ≥ 1) with 2 < Re ι ≤ 3 + ε_+,
together with ι + 1 for those with Re ι ≤ 2 + ε_+. All are simple. Of these poles, 3 lies in Λ ([[def:iii-i10-1-1]]);
whether any other lies in Λ, which [[prop:is-lambda]] describes on {Re ≤ 3 + ε_+}, is not decided here, and no bound
depends on it, each raise being at most 1 by (c). The numbers λ_♯ + j, 3/2 + γ_Υ + j and 3/2 + 2γ_Υ + j (j = 1, 2, 3) are
not poles.

*Proof.* (a) The orders are [[thm:sp-spectrum]] (b) and the multiplicities [[lem:sp-roots]] (b); the set of poles at
real part at most 5 is not empty, so the pole orders require l_* ≥ 1. That M ≤ 7 is stated in [[prop:is-mult]];
directly, (C1) holds at the computational point ([[prop:np-10-54]] (i), (ii)), so by [[prop:iii-f1-2-3]] (a), (b), at
each type and degree n_τ ≤ 7 roots, counted with multiplicity, have real part at most 0, and n_τ have real part above
1, and no root has multiplicity above 7. For L: every exponent of ℰ_ind of real part at most 5 has logarithmic order
at most 39, and (5, 39) ∈ ℰ_ind; those of ℰ^ι_ind have orders at most 50 there ([[prop:is-logs]] (b), (c)); and the
least ℰ^C_I has all orders 0 ([[prop:is-ci-pp]] (a)). So 39 ≤ L ≤ 50, and L ≥ 39 > 7 ≥ M.

(b) The first bound is that of [[prop:iii-g3-2-4]] with (a), as Σ ⊂ {Re < 3 + ε_+}: m_♯(ϰ) = k(ℰ^C_(I,♯), ϰ) + 1 if
ϰ ∈ π_1ℰ^C_(I,♯) and m_♯(ϰ) = 0 otherwise, and k(ℰ^C_(I,♯), ϰ) ≤ l_* as in the proof of [[lem:iii-j-1-2]]. With the
least ℰ^C_I, ℰ^C_(I,♯) = (λ_♯, 0) ∪ ℰ^C_I ([[eq:iii-g3-2-1]]) has all logarithmic orders 0, so m_♯(ϰ) ∈ {0, 1}, equal
to 1 exactly on {λ_♯} ∪ π_1ℰ^C_I. So K_ι(ϰ) ≤ 2, with K_ι(ϰ) = 2 possible only where m_ι(ϰ) = m_♯(ϰ) = 1, that is on
spec_ι⁺(L̄) ∩ ({λ_♯} ∪ π_1ℰ^C_I) = spec_ι⁺(L̄) ∩ π_1ℰ^C_I, as λ_♯ < 2 and spec_ι⁺(L̄) ⊂ {Re ≥ 2}
([[lem:iii-g1-4-2]] (a)). The point 3 is in
[[thm:sp-spectrum]] (a) and 3 = 1 + 4/2 ∈ π_1ℰ^C_I ([[prop:is-ci-pp]] (a), with n = 4 and c = 0). (λ_♯, 0) ∈
Spec^(<ℓ_I)_(ι⁺)(L̄, ℰ^C_I) by [[cor:iii-g3-2-6]], so the pole at λ_♯ is simple.

(c) 𝒮_(ϰ₀)(f) is the solution that [[cor:iii-g3-3-1]] (1) gives, whose logarithmic powers are at most J + K, J the
largest power of log t_* in f and K the order at ϰ₀ of the pole of [[eq:iii-g3-2-2]]; its proof uses K only as the
order of the pole of ϰ ↦ N_ι⁺(ϰ)⁻¹ on the coefficients of f. As f has no ℐ⁺-expansion, [[eq:iii-g3-2-2]] acts on
these as the inverse of [[thm:iii-g1-3-1]] (2), as [[sec:s23-step]] notes, so that order is at most m_ι(ϰ₀), and
m_ι(ϰ₀) is given by [[thm:sp-spectrum]] (b). The raises of [[lem:iii-i10-1-2]] (c) are those of [[cor:iii-g2-4-3]],
whose logarithmic powers are at most k + l_0, l_0 the order of the pole of N_ι⁺(L̄, ·)⁻¹ at the exponent, at most 1
by [[thm:sp-spectrum]] (b).

(d) This is [[thm:sp-spectrum]] (a) restricted to the strip. Beyond it lie 4 + 𝔡₀, 4 + 𝔡₁ and the integers 4, 5, and
also ι₁ + 1 > 3 + δ_C and every ι_v(l) ≥ ι_v(2) > 3 + 4·10⁻⁶, since ε_+ < ε_ind = δ_50 < δ̄ < 2·10⁻⁸
([[eq:iii-i9-1-1]], [[def:ec-point]]) and (500002 + 4·10⁻⁶)² < 250002000009; ι_v increases with l. The number 3 is
one of the generators of Λ in [[def:iii-i10-1-1]]. For the last statement, by [[lem:sp-exceptional]]: these numbers
lie in 3/2 + σ_Υ + {1, 2, 3} ⊂ Q; they are not integers, not 4 + 𝔡₀ or 4 + 𝔡₁, and not ι₁ + j, as
ι₁ + j ∈ (j + 2, j + 5/2); and a number q ∈ Q equal to ι + j or ι_v(l) + j, with Re ι > 2 or ι_v(l) > 2, would give
ι = q − j ∈ Q or ι_v(l) = q − j ∈ Q, which [[lem:sp-exceptional]] excludes. ∎

**Remark {#rem:sp-scope}** (What the evaluation leaves open.) [[thm:sp-spectrum]] describes the poles exactly, by the
roots of the explicit polynomials P_l and p_(v). The vector type is in closed form, and for the scalar types with
x ≤ 70 the roots are enclosed by [[lem:s14-sextic-small]] and [[lem:s14-sextic-large]]; for x > 70 this paper locates
the roots of P_l only in {Re ι > 2} with no real root in (2, 5], and shows those of real part at most 5 simple, which
suffices for every statement above but leaves the largest l contributing a pole below real part 5 unevaluated. This
section does not determine the multiplicities of the indicial roots of real part at most 0 or in (4, 5]: they are 1
at real part in [−101, 5] ([[prop:is-mult]]) and at most 7 everywhere ([[prop:iii-f1-2-3]] (b)). Nor does it
determine L of [[cor:sp-lstar]] (a), which lies in [39, 50] ([[prop:is-logs]]); l_* = 50 serves in either case.
