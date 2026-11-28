### One leaf constant for every rank, and the products over the words {#sec:tl5-hfd}

This section makes two changes. First, the Sobolev inequality on the leaves of [[lem:tl5-hft-leaf]] and
[[lem:tl5-hfp-leaf]] bounds |A(ω)|₀ through the functions Σ_k |s_k(ω)|₀² of the isotypic subspaces V_π, that is through
the traces of their kernels at ω. The trace counts every copy of every representation of the isotropy group in the fibre
at ω, whose dimension is 5^r. The kernel itself commutes with the isotropy group, so on each isotypic component of the
fibre it is a multiple of the identity, and the largest of these multiples, summed over π with the weights, is at most
the constant of the functions ([[lem:tl5-hfd-leaf]]). So the inequality holds for tensors of every rank with the
constant C_(E,0)(𝔶) of the functions, which is also the best constant for each rank, and every constant formed with a
Sobolev inequality on a face takes it. Second, in the products with a factor at a point, the monomials of 2𝔮̂ whose two
factors are first derivatives D̂Ψ are summed over the words of each length before they are bounded: the factor in the
energies is then counted by 𝒥_g once for all its words, and the factor at a point by the number of its own words, in
place of the count 7^(j′/2) of all the words of the level, and these monomials need no recovery constant
([[lem:tl5-hfd-words]]). Both changes enter the constants with index d ([[def:tl5-hfd-constants]], [[thm:tl5-hfd]]). The
closing condition is [[eq:tl5-hfd-closing]]; every new constant is at most the one it replaces, for all weights, and the
earlier closing conditions remain valid. The notation is that of [[sec:tl5-hfp]] and, for N = 4, of [[sec:tl5-hfu]].

**Lemma {#lem:tl5-hfd-leaf}** (One leaf constant for every rank.) In the setting of [[lem:tl5-hfp-leaf]] let 𝔶₀, 𝔶₁ > 0
and 𝔶₂ := 1, and for j ∈ ℕ put

    𝔖_j(𝔶) := (1/(2π²(2j + 1))) Σ_((j₁,j₂)) (2j₁ + 1)(2j₂ + 1)/(𝔶₀ + 𝔶₁ c_(j₁j₂) + c_(j₁j₂)²),

the sum over the j₁, j₂ ∈ (1/2)ℕ with j₁ + j₂ − j ∈ ℕ and |j₁ − j₂| ≤ j ≤ j₁ + j₂. Then 𝔖_j(𝔶) ≤ 𝔖_0(𝔶) = C_(E,0)(𝔶)²,
C_(E,r)(𝔶)² = Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶), and for every r ≥ 0, every C² covariant tensor field A of rank r on S_(u,v)
and every ω ∈ S³

    |A(ω)|₀² ≤ C_(E,0)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀² dω,                                     {#eq:tl5-hfd-leaf}

where C_(E,0)(𝔶)² = (1/(2π²)) Σ_(n≥0) (n + 1)²/(𝔶₀ + 𝔶₁ n(n + 2) + n²(n + 2)²). In particular C_(E,0)(𝔶) ≤ C_(E,r)(𝔶)
and C_(E,0)^♯ ≤ C_(E,r)^♯ for every r, and C_(E,r)(𝔶)² ≤ 5^r C_(E,0)(𝔶)².

*Proof.* Let E, the action of SO(4), the point o, the V_π and c_π be as in the proof of [[lem:tl5-hft-leaf]],
complexified, and put w_π := 𝔶₀ + 𝔶₁ c_π + c_π² and CG(π) := {|j₁ − j₂|, …, j₁ + j₂} for π = (j₁, j₂). Write the fibre
E_o as an orthogonal sum of subspaces U on which the isotropy group SO(3) acts irreducibly, of spin j_U, and let E^U be
the subbundle with fibre g·U at g·o, g ∈ SO(4). It is well defined, as U is invariant under the isotropy group; it is
invariant under SO(4); and the E^U are orthogonal, as SO(4) preserves h₀. So L²(S³, E) is the orthogonal sum of the
invariant subspaces L²(S³, E^U), and V_π the orthogonal sum of their π-isotypic parts V_π^U. By Frobenius reciprocity,
as in that proof, dim V_π^U = dim π · dim Hom_(SO(3))(π, U), which is dim π if j_U ∈ CG(π) and 0 otherwise, as (j₁, j₂)
restricted to the diagonal SU(2) contains each [j] at most once. For an orthonormal basis (s_k) of V_π^U the operator
K_π^U(ω) := Σ_k s_k(ω) ⟨·, s_k(ω)⟩₀ on the fibre at ω does not depend on the basis, so K_π^U(g·ω) = g K_π^U(ω) g⁻¹ for
g ∈ SO(4). At o it maps into U, vanishes on the orthogonal complement of U and commutes with the isotropy group, so by
Schur's lemma it is a multiple of the orthogonal projection P_U onto U; its trace is Σ_k |s_k(o)|₀² = dim V_π^U/(2π²),
as in that proof. Hence K_π^U(o) = dim π P_U/(2π²(2j_U + 1)) if j_U ∈ CG(π), and 0 otherwise.

Let A = Σ_π A_π as in that proof, and expand each A_π in an orthonormal basis of V_π made of bases of the V_π^U. For a
unit vector u in the fibre at ω, the Cauchy–Schwarz inequality over π and over these basis vectors gives |⟨A(ω), u⟩₀|² ≤
Σ_π w_π ‖A_π‖² · Σ_π w_π⁻¹ Σ_U ⟨K_π^U(ω) u, u⟩₀. By the invariance it suffices to bound the second factor at ω = o,
where Σ_π w_π⁻¹ Σ_U K_π^U(o) = Σ_U 𝔖_(j_U)(𝔶) P_U, an operator of norm at most the largest 𝔖_j(𝔶). In the proof of
[[lem:tl5-hfp-leaf]], Σ_π w_π ‖A_π‖² = Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖², and taking the supremum over u gives
[[eq:tl5-hfd-leaf]] with the largest 𝔖_j(𝔶) in place of C_(E,0)(𝔶)². It remains to compare the 𝔖_j(𝔶). The (j₁, j₂) of
the sum defining 𝔖_j(𝔶) have d := j₁ − j₂ ∈ {−j, −j + 1, …, j}, as j₁ + j₂ − j ∈ ℕ, and for fixed d the number κ :=
(j₁ + j₂)/2, with 2κ ∈ ℕ, determines (j₁, j₂). As (2j₁ + 1)(2j₂ + 1) ≤ (2κ + 1)², 2j₁(j₁ + 1) + 2j₂(j₂ + 1) ≥
4κ(κ + 1) = c_(κκ) because j₁² + j₂² ≥ 2κ², and 𝔶₀ + 𝔶₁ c + c² is increasing in c ≥ 0, the terms with a fixed d add up
to at most Σ_κ (2κ + 1)²/(𝔶₀ + 𝔶₁ c_(κκ) + c_(κκ)²) = 2π² 𝔖_0(𝔶); with the 2j + 1 values of d this gives 𝔖_j(𝔶) ≤
𝔖_0(𝔶). The representations with 0 ∈ CG(π) are the (κ, κ), with c_(κκ) = n(n + 2) for n := 2κ, so 𝔖_0(𝔶) = C_(E,0)(𝔶)²,
which is the value of the sum in [[eq:tl5-hfd-leaf]]. Finally m_(j₁j₂)(r) = Σ_(j∈CG(j₁,j₂)) e_j(r) gives C_(E,r)(𝔶)² =
Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶), which is at least 𝔖_0(𝔶) as e_0(r) ≥ 1 (the tensor du ⊗ ⋯ ⊗ du is invariant) and at most 5^r
𝔖_0(𝔶) as Σ_j e_j(r) (2j + 1) = dim E_o = 5^r. ∎

**Lemma {#lem:tl5-hfd-words}** (The products over the words of one length.) In the setting of [[lem:tl5-hfs-products]],
with the notation of [[def:tl5-hfs-bounds]], put λ̂^♮₀(ν′) := √5 and λ̂^♮_k(ν′) := ν′^(k/2) λ^♮_k for k ≥ 1, and for
0 ≤ n ≤ N and ν′ > 0

    𝔠^D_n(ν′) := 16 Σ⁴_n λ̂^♮_(k₁)(ν′) λ̂^♮_(k₂)(ν′),
    𝔠^(D,7)_n(ν′) := 16 Σ⁴_n λ̂^♮_(k₁)(7ν′) λ̂^♮_(k₂)(7ν′) 7^(min(k₃,k₄)/2) χ(k),

with χ(k) := 0 if N = 4 and k = (0, 0, 2, 2), and χ(k) := 1 otherwise. Let 𝔡_n be the part with ϱ(p) of the right side
of the first inequality of [[eq:tl5-hfs-products]] and 𝔡′_(j′) that of the second for |J| = j′, in the forms that the
lemma in use gives them. Then at every point of Q(a, b), the sums being over the words of the lengths shown,

    (Σ_(|I|=n) μ^n |𝔑^L_I|²)^(1/2) ≤ μ^(−3/2) (𝔠^(D,7)_n(μ) 𝔰_P + 7^(n/2) (𝔠^♮_n(μ) − 𝔠^D_n(μ)) 𝔓) 𝒥_g + 7^(n/2) 𝔡_n,
    (Σ_(|J|=j′) μ^n |ℒ^J N(h)|²)^(1/2) ≤ μ^((n−j′−3)/2) (𝔠^(D,7)_(j′)(μ) 𝔰_P
        + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔓) 𝒥_g + 7^(j′/2) 𝔡′_(j′)      (j′ < n).          {#eq:tl5-hfd-words}

Moreover 𝔠^D_n(ν′) ≤ 𝔠^(2♮)_n(ν′) and 𝔠^(D,7)_n(ν′) ≤ 7^(n/2) 𝔠^D_n(ν′).

*Proof.* Use the second expansion of the proof of [[lem:tl5-hfg-quadratic]]. Call a monomial of ℒ^I(2𝔮̂) one of type D
if both its factors D̂h give it the leading term D̂Ψ_K of their expansions ℒ^K D̂h = D̂Ψ_K + ⋯ of
[[lem:tl5-hfs-quadratic]] (a). For a term c_m 𝒯_m of 2𝔮̂ and a decomposition of the positions of the letters of I into
four sets, on ĝ⁻¹, ĝ⁻¹, D̂h, D̂h, carrying the subwords I₁, I₂, I₃, I₄ with k₁, …, k₄ letters, the monomial of type D is
c_m 𝒯_m(X₁, X₂, D̂Ψ_(I₃), D̂Ψ_(I₄)), X_i := ℒ^(I_i) ĝ⁻¹ (ĝ⁻¹ if I_i is empty), its background factors carry b := k₁ + k₂
letters, and |X_i| ≤ λ̂^♮_(k_i)(1) as counted there. In the count of [[lem:tl5-hfs-quadratic]] (b) the sum 16 Σ⁴_n λ̂^♮
λ̂^♮ β₁^♮ β₁^♮ of 𝔠^(2♮)_n is that of 2𝔮̂, the norms of the terms of the expansion of each ℒ^K D̂h adding up to at most
β₁^♮(|K|), whose term 1 is that of D̂Ψ_K. So the sum of ν ν′^(b/2) over the monomials of type D is at most 𝔠^D_n(ν′),
and that of ν ν′^(b/2) 𝔰^(q−2) over the other monomials is at most 𝔠^♮_n(ν′) − 𝔠^D_n(ν′); and 𝔠^D_n ≤ 𝔠^(2♮)_n, as
β₁^♮ ≥ 1 and the other sums of 𝔠^(2♮)_n are nonnegative. The other monomials are bounded word by word as in the proof of
[[lem:tl5-hfs-products]], with 𝔠^♮_n(μ) − 𝔠^D_n(μ) in place of 𝔠^♮_n(μ) in the part with 𝒥_g and as there in the part
with ϱ(p), and the Euclidean norm over the 7^n words I is at most 7^(n/2) times the largest; this gives the terms with 𝔓
and with 𝔡_n.

Let a monomial of type D belong to 𝔑^L_I. Its solution factors D̂Ψ_(I₃) and D̂Ψ_(I₄) have k₃ + k₄ = n − b letters; for
N = 4 the decomposition with k = (0, 0, 2, 2) gives two high factors and belongs to 𝔑^M_I, and two factors D̂Ψ_C of
order at least N − 1 would need 2N − 4 letters, more than N for N ≥ 5. So the one with fewer letters, Φ₁ := D̂Ψ_(I_P)
with k_P := min(k₃, k₄), is low, as the other would then be high as well; let Φ₂ := D̂Ψ_(I_E) be the other, with k_E :=
n − b − k_P letters. As in the proof of [[lem:tl5-hfs-products]], |Φ₁| ≤ μ^(−(k_P+3)/2) 𝔰_P and μ^(n/2) μ^(−(k_P+3)/2)
μ^(−k_E/2) = μ^(−3/2) μ^(b/2). Fix m and the four sets of positions. As I runs over the words of length n, the four
subwords run independently over all words of their lengths, so the Euclidean norm over I of the monomial, times μ^(n/2),
is at most |c_m| μ^(−3/2) μ^(b/2) times the product of (Σ_(I₁) |X₁|²)^(1/2) ≤ 7^(k₁/2) λ̂^♮_(k₁)(1), the same for X₂,
(Σ_(I_P) μ^(k_P+3) |Φ₁|²)^(1/2) ≤ 7^(k_P/2) 𝔰_P and (Σ_(I_E) μ^(k_E) |D̂Ψ_(I_E)|²)^(1/2) ≤ 𝒥_g, the words I_E being
distinct. As 7^(k/2) μ^(k/2) λ̂^♮_k(1) = λ̂^♮_k(7μ), Minkowski's inequality over m, with Σ_m |c_m| = 16, and over the
n!/(k₁! k₂! k₃! k₄!) decompositions for each k gives μ^(−3/2) 𝔠^(D,7)_n(μ) 𝔰_P 𝒥_g. These monomials carry no second
derivative, so they have no part with ϱ(p); and k₁ + k₂ + min(k₃, k₄) ≤ n gives 𝔠^(D,7)_n(ν′) ≤ 7^(n/2) 𝔠^D_n(ν′).
Minkowski's inequality over the two kinds of monomials gives the first inequality. For |J| = j′ < n, ℒ^J N(h) = 𝔑_J +
H^(αβ) D̂_αD̂_βΨ_J with 𝔑_J = 𝔑^L_J, also for N = 4, as j′ ≤ 3; the first inequality for the words of length j′, times
μ^((n−j′)/2), bounds the family of the 𝔑_J, and H^(αβ) D̂_αD̂_βΨ_J is bounded word by word as in the proof of
[[lem:tl5-hfs-products]], which gives the second inequality. ∎

**Definition {#def:tl5-hfd-constants}** (The constants with index d.) The constants with index d are the constants with
index p of [[def:tl5-hfp-constants]] and, for N = 4, those with index u of [[def:tl5-hfu-constants]], formed, first,
with C_(E,0)(𝔶) in place of C_(E,r)(𝔶) and with C_(E,0)^♯ in place of C_(E,r)^♯, for every rank r: in C_S^p (r = 2), in
C₁(𝔚) and C₁^p (r = 3), in C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p with their factors 𝔗(𝔶)², in 𝔛^u_(1,t), 𝔛^u_(2,t) and
𝔛′^u_(2,t) (r = 3 and 4), and in every other constant formed with a Sobolev inequality on a face, and in the constants
formed from these, 𝔨_rec^(·,p) and 𝔐_p^(m) among them. They are formed, second, with 𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ in place of the
products 𝔤_(𝒥,s) 𝔎, 𝔤_(𝒥,s) 𝔎_ϱ and 𝔤_(𝒥,s) 𝔎₀ in 𝔞_(o,s), 𝔞_(i,s), 𝔟_(o,s) and 𝔟_(i,s) of [[def:tl5-hfs-constants]], in
their forms with index p, where, with 𝔠^D and 𝔠^(D,7) as in [[lem:tl5-hfd-words]],

    𝔎^D := (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) (𝔠^(D,7)_(j′)(μ) C_P
           + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔎))²)^(1/2),

and 𝔎^D_ϱ and 𝔎^D₀ are formed in the same way with C_(P,ϱ), 𝔎_ϱ and with C_(P,0), 𝔎₀ in place of C_P, 𝔎; here C_P,
C_(P,ϱ), C_(P,0), 𝔎, 𝔎_ϱ and 𝔎₀ are C_P^♮, C_(P,ϱ)^♮, C_(P,0)^♮ and the 𝔎 of [[def:tl5-hfs-constants]] in their forms
with index d (for N = 4, C_P^v, C_(P,ϱ)^v and C_(P,0)^v of [[lem:tl5-hfv-rec]]). The number 𝔤_(𝒥,s) in the minimum of
ε_(w,q) is kept. For N ≥ 6 let S_F^d and 𝔯^d be S_F^p and 𝔯^p of [[thm:tl5-hfp]] formed with the constants with index d,
and S_M^d := ε_M^d := 0; for N = 4 let S_F^d, S_M^d, ε_M^d and 𝔯^d be S_F^p, S_M^u, ε_M^u and 𝔯^u of [[thm:tl5-hfu]] so
formed. Put

    η_d := 1 − max(ϑ₁, ϑ₂) − 𝔯^d,      A_d := η_d^(−1/2) δ_w + η_d⁻¹ (ε^z + ε_M^d),      B_d := η_d⁻¹ (S_F^d + S_M^d),

and let 𝔰_*^d be 𝔰_*^p (N ≥ 6) or 𝔰_*^u (N = 4) formed with the constants with index d and with A_d in place of A_p or
A_u.

**Theorem {#thm:tl5-hfd}** (Existence with one leaf constant for every rank and the products over the words.) In the
setting of [[thm:tl5-hfp]] (N ≥ 6) or of [[thm:tl5-hfu]] (N = 4), suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1
− ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_d > 0, 𝔰_*^d < 𝔰₁^v and the closing condition

    4 A_d B_d = 4 η_d^(−3/2) (δ_w + η_d^(−1/2) (ε^z + ε_M^d)) (S_F^d + S_M^d) < 1.                 {#eq:tl5-hfd-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_d and 𝔰_*^d in place of A_w (or
A_(w,4)) and 𝔰_*. For all admissible weights each constant with index d is at most the one it replaces, η_d ≥ η_p (or
η_u), and A_d, B_d and 𝔰_*^d are at most A_p, B_p and 𝔰_*^p (or A_u, B_u and 𝔰_*^u); so the hypotheses of
[[thm:tl5-hfp]] and of [[thm:tl5-hfu]] imply these.

*Proof.* By [[lem:tl5-hfd-leaf]], [[eq:tl5-hfp-leaf]] holds for every rank r and all weights with C_(E,0)(𝔶) in place of
C_(E,r)(𝔶), and so with C_(E,0)^♯ in place of C_(E,r)^♯ for 𝔶₀ = 𝔶₁ = 1. The proofs of [[lem:tl5-hft-face]],
[[lem:tl5-hfp-abs]] (a) and [[lem:tl5-hfu-face]] use [[eq:tl5-hfp-leaf]] only through its form, so these lemmas hold
with C_(E,0)(𝔶) and C_(E,0)^♯ in place of C_(E,r)(𝔶) and C_(E,r)^♯; the lemmas of [[sec:tl5-hfp]] and [[sec:tl5-hfu]]
use the Sobolev constants only through these, and so hold with the constants with index d. Then the proof of
[[thm:tl5-hfp]] (N ≥ 6) or of [[thm:tl5-hfu]] (N = 4) applies with the constants with index d, η_d, A_d, B_d, 𝔰_*^d and
[[eq:tl5-hfd-closing]], with one change in Step 2 of the proof of [[prop:tl5-hfs-bootstrap]], on which it rests. There
the family over |I| = j of the nonlinear terms other than 𝔑^M_I, which are −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I with |J| < |I|
in the sum, is bounded by [[eq:tl5-hfd-words]] and the definition of 𝔮_(jj′), in place of [[eq:tl5-hfs-products]] and
the Cauchy–Schwarz inequality over the 7^(j′) words: its norm is at most μ^(−j/2) Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′)
(𝔠^(D,7)_(j′)(μ) 𝔰_P + 7^(j′/2) (𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔓) μ^(−3/2) 𝒥_g plus the part with ϱ that the proof
uses. The rest of Step 2 holds as written, and in Step 3, at each point, 𝔰_P ≤ C_P e^(φ/2) Y_s + C_(P,ϱ) ϱ + C_(P,0) η₀
and 𝔓 ≤ 𝔎 e^(φ/2) Y_s + 𝔎_ϱ ϱ + 𝔎₀ η₀; Minkowski's inequality in the Euclidean norm over j then gives the terms with
𝔎^D, 𝔎^D_ϱ and 𝔎^D₀ in place of those with 𝔤_(𝒥,s) 𝔎, 𝔤_(𝒥,s) 𝔎_ϱ and 𝔤_(𝒥,s) 𝔎₀. For the last claim, C_(E,0)(𝔶) ≤
C_(E,r)(𝔶) and C_(E,0)^♯ ≤ C_(E,r)^♯ by [[lem:tl5-hfd-leaf]], and every constant of [[thm:tl5-hfp]] and [[thm:tl5-hfu]]
is nondecreasing in the Sobolev constants. By [[lem:tl5-hfd-words]], 𝔠^(D,7)_(j′)(μ) ≤ 7^(j′/2) 𝔠^D_(j′)(μ), and C_P ≤
𝔎, C_(P,ϱ) ≤ 𝔎_ϱ and C_(P,0) ≤ 𝔎₀, as the number 𝔨_B in 𝔎, 𝔎_ϱ and 𝔎₀ is at least 1; so each term of the inner sum of
𝔎^D is at most the corresponding term of 𝔤_(𝒥,s) 𝔎, and 𝔎^D ≤ 𝔤_(𝒥,s) 𝔎, 𝔎^D_ϱ ≤ 𝔤_(𝒥,s) 𝔎_ϱ and 𝔎^D₀ ≤ 𝔤_(𝒥,s) 𝔎₀. So
𝔯^d ≤ 𝔯^p (or 𝔯^u) and S_F^d ≤ S_F^p, and the rest follows as in the proof of [[thm:tl5-hfu]]. ∎

**Remark {#rem:tl5-hfd-what}** (What changes.) In [[lem:tl5-hft-leaf]] the bound |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖²
takes the trace of the kernel at ω, the sum of its eigenvalues over the 5^r dimensions of the fibre, where the pointwise
bound needs only the largest; the kernel is a multiple of the identity on each isotypic component of the fibre for the
isotropy group, so the largest eigenvalue, summed over π with the weights, is 𝔖_j(𝔶) for some spin j of the fibre, and
𝔖_j(𝔶) ≤ 𝔖_0(𝔶). So C_(E,r)(𝔶)² = Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶) becomes 𝔖_0(𝔶) = C_(E,0)(𝔶)², a factor between 1 and 5^r;
the rank enters the Sobolev constants on the faces only through the comparison factors 𝔳₀^r and 𝔴₀^r and the coefficient
1 + 2r²|D̂∂_γ|² of the step along the curves. No smaller constant holds for any rank with these weights: for A := f du ⊗
⋯ ⊗ du, whose Lie derivatives along the rotations are (Kf) du ⊗ ⋯ ⊗ du, [[eq:tl5-hfd-leaf]] is the inequality for the
function f, and for the functions f := Σ_(c_π≤M) (𝔶₀ + 𝔶₁ c_π + c_π²)⁻¹ K_π(·, o), K_π(·, o) the kernel at o of the
π-isotypic functions, the left side divided by the sum on the right tends to C_(E,0)(𝔶)² as M → ∞. The split of the
derivatives between the leaves and the curves is unchanged: the leaves need the words of length two in the six
rotations, and the curves one derivative. In S_F the products with a factor at a point were counted word by word, each
word I bounded through 𝒥_g, which already sums over all the words, and the family over the 7^(j′) words of a length then
counted 7^(j′/2) times; in [[eq:tl5-hfd-words]] the monomials of type D, which give the term 16 λ̂₀² 2^n = 80 · 2^n of
𝔠^♮_n at Λ = 0, are summed over the words first, so the factor in the energies is counted once, the factor at a point by
the 7^(k_P) words of its own length, and the background factors by theirs, which the argument 7ν′ of λ̂^♮ carries. At
Λ = 0 the coefficient 7^(n/2) 𝔠^D_n of these monomials, 7^(n/2) 80 · 2^n, becomes 80 Σ_(k₃+k₄=n) C(n, k₃)
7^(min(k₃,k₄)/2) χ, for n = 4 and N = 4 80 (2 + 8 · 7^(1/2)) in place of 49 · 1280, and they enter with C_P in place of
𝔎, as their factor in the energies is a first derivative, for which no recovery constant and no 𝔷 is needed. The other
monomials keep the count 7^(j′/2), and the parts with ϱ keep 𝔤_(ϱ,s). As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfd]] are established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD b6df4c77, where sec:tl5-hfu is merged (Section 57.26,
merge 01727fdd). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfd) through the last line of
[[rem:tl5-hfd-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfu-what]] (line 7078,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfu-what]] (lines 7076–7077).* Old:

nor a power is gained there. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfu]] are
established in this paper for no background at 10 l5.

New (one line added, of 105 characters; the two old lines are unchanged):

nor a power is gained there. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfu]] are
established in this paper for no background at 10 l5.
[[sec:tl5-hfd]] gives the Sobolev inequality on the leaves one constant for every rank ([[thm:tl5-hfd]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfd acts at every level: at N ≥ 6 on thm:tl5-hfp, at N = 4 on thm:tl5-hfu. It makes two
changes, and every new factor is at most the old one for all admissible weights, so it contains both theorems.
Unchanged: ε^z and 𝔤_(ϱ,s) (the coefficients of ϱ, which carry no Sobolev constant and keep the count 7^(j′/2)), 𝔰₀,
𝔰₁^v and the cap, k₁^D, 𝔨_♯, K_rec, k₂^z, 𝔵^z, the recovery and family numbers 𝔩, 𝔩(𝔙), 𝔞_𝔄, the counts 𝔠^Mq of S_M,
𝔤_(𝒥,s) inside the minimum of ε_(w,q), and the rates.

1. The leaf constant (lem:tl5-hfd-leaf). For every rank r and all weights,
       C_(E,0)(𝔶)² = (1/(2π²)) Σ_(n≥0) (n + 1)²/(𝔶₀ + 𝔶₁ n(n + 2) + n²(n + 2)²)
   replaces
       C_(E,r)(𝔶)² = (1/(2π²)) Σ_(j₁,j₂) (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r)/(𝔶₀ + 𝔶₁ c + c²) = Σ_j e_j(r) (2j + 1) 𝔖_j(𝔶),
   and C_(E,0)^♯ = C_(E,0)(1, 1) replaces C_(E,r)^♯. It enters:
   - C_S^p (r = 2) and C₁(𝔚), C₁^p, C₁^Γ (r = 3);
   - C_(1,ϱ)^p, C_(1,0)^p (r = 3) and C_(0,0)^p (r = 2), with their 𝔗(𝔶)²;
   - 𝔛^u_(1,t) (r = 3) and 𝔛^u_(2,t), 𝔛′^u_(2,t) (r = 4) of S_M, 𝔯_M, ε_M;
   - every other face constant, and through these 𝔨_rec^(·,p), C_P^v, C_(P,ϱ)^v, C_(P,0)^v, 𝔐_p^(m), C_(∞,μ)^(m), 𝔎, S_F,
     𝔯 and 𝔰_*.
   Proved: 𝔖_j(𝔶) ≤ 𝔖_0(𝔶) = C_(E,0)(𝔶)² for every j, so C_(E,0)(𝔶)² ≤ C_(E,r)(𝔶)² ≤ 5^r C_(E,0)(𝔶)².
   Summed (2j₁ < 80000, the tail extrapolated in 1/j₁):
       𝔶                     C_(E,0)(𝔶)²    C_(E,0)(𝔶)/C_(E,r)(𝔶) for r = 2, 3, 4
       1                     0.08725        0.3022 (−0.52)   0.1499 (−0.82)   0.0722 (−1.14)
       (μ⁻², μ⁻¹), μ = 10⁻⁴   4.5946 × 10⁻⁴  0.2000 (−0.70)   0.0894 (−1.05)   0.0400 (−1.40)
       μ = 10⁻⁵              1.4529 × 10⁻⁴  the same to four digits, 5^(−r/2)
       μ = 10⁻⁶              4.5944 × 10⁻⁵  the same to four digits
   with 𝔖_j(1) = 0.0873, 0.0291, 0.0165, 0.0116, 0.0090 for j = 0, …, 4. Against the original 6C_(E,3)² of
   lem:tl5-hft-leaf, C_(E,0)^♯ is (0.0873/21.825)^(1/2) = 0.0632 times (6C_(E,3)²)^(1/2), −1.20 decades.
2. The products over the words (lem:tl5-hfd-words). In 𝔞_(o,s), 𝔞_(i,s), 𝔟_(o,s) and 𝔟_(i,s), in their forms with
   index p,
       𝔎^D = (Σ_j (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) (𝔠^(D,7)_(j′)(μ) C_P
             + 7^(j′/2)(𝔠^♮_(j′)(μ) − 𝔠^D_(j′)(μ) + 1) 𝔎))²)^(1/2)
   replaces
       𝔤_(𝒥,s) 𝔎 = (Σ_j (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2)(𝔠^♮_(j′)(μ) + 1) 𝔎)²)^(1/2),
   and 𝔎^D_ϱ, 𝔎^D₀ (with C_(P,ϱ), 𝔎_ϱ and C_(P,0), 𝔎₀) replace 𝔤_(𝒥,s)𝔎_ϱ, 𝔤_(𝒥,s)𝔎₀. The two new counts are:
   - 𝔠^D_n(μ) = 16 Σ⁴_n λ̂^♮_(k₁)(μ) λ̂^♮_(k₂)(μ), the part of the 2𝔮̂ term of eq:tl5-hfs-cn with β₁^♮ → 1;
   - 𝔠^(D,7)_n(μ) = 16 Σ⁴_n λ̂^♮_(k₁)(7μ) λ̂^♮_(k₂)(7μ) 7^(min(k₃,k₄)/2) χ, with χ = 0 only for N = 4, k = (0, 0, 2, 2).
   At Λ = 0 (b = 0) the type-D counts are:
       n                             0     1     2      3       4 (N = 4)   4 (N = 6)   5        6
       7^(n/2) 𝔠^D_n = 7^(n/2) 80·2^n 80    423   2240   11853   62720       62720       331883   1756160
       𝔠^(D,7)_n                      80    160   583    1430    1853        5213        13477    49132
       decades                       0     −0.42 −0.58  −0.92   −1.53       −1.08       −1.39    −1.55
   The rest, 𝔠^♮_n − 𝔠^D_n, is 2^n − 1 at Λ = 0 (15 at n = 4); the type-D terms carry C_P where the old carried
   𝔎 = max(2C_S 𝔨_A, C_P 𝔨_B), 𝔨_B = max(𝔷, 𝔤₁).
3. The closing condition eq:tl5-hfd-closing is eq:tl5-hfp-closing (N ≥ 6) or eq:tl5-hfu-closing (N = 4) formed with the
   constants with index d.

What it gives, deduced, not evaluated. At G0n's level-4 optima (G0n.0) and G0m's level-6 optima. Assumptions:
- the optima's 𝔶 = (μ⁻², μ⁻¹);
- 𝔨_rec^p leads C_P^v, 1.6–1.9 decades above 2C_S (G0n);
- 𝔨_B = 𝔷 ≈ 10^0.6–0.75 (G0g);
- 𝔠^♮₄(μ) = 1337–1401 with the floor 1303 (G0n). How its part above the floor divides between type D and the rest is
  not known here, so both extremes are taken.

Level 4:
- The leaf constant:
  - C₁, C₁^Γ, 𝔨_rec^p and so C_P^v fall 1.05 decades.
  - 2C_S falls 0.70, so C_P^v still leads (1.25–1.55 above).
  - The parts with ϱ and η₀ fall 1.05 (rank 3) and 0.70 (rank 2).
  - S_M falls 1.05 and 1.40 on its two terms.
  - S_F falls about 1.05 through C_P and 𝔎 (led by C_P 𝔨_B).
  - Both ε limits carry C_P^v, and G0n measures them at 1:1. So up to about +1.0 on min(f, ϱ), until C_S or the part of
    S_F without C_P leads.
- The words, on the j′ = 4 term of 𝔤_(𝒥,s)𝔎:
  - Old: 49 (𝔠^♮₄ + 1) 𝔎 ≈ (6.6–6.9) × 10⁴ 𝔎.
  - New: 1853 C_P + 49 (𝔠^♮₄ − 𝔠^D₄ + 1) 𝔎 ≈ (1853/𝔨_B + 49 · (24 to 122)) 𝔎 ≈ (1.5–6.4) × 10³ 𝔎, the rest
    𝔠^♮₄ − 𝔠^D₄ lying between 15 + 𝔰_♭𝔠^(3♮)₄ ≈ 23 and 1401 − 1280 = 121.
  - That is −1.0 to −1.7 decades. The j′ = 3 term falls −0.9 to −1.5 on the same reckoning.
  - So S_F falls about 1.0–1.7 decades beyond the leaf lever's fall, if these terms lead 𝔤_(𝒥,s)𝔎.
  - 𝔰_* binds here (G0n.1), so this acts as G0n's priced "word count 7² in S_F" (+0.28 / +0.44 / 0.00 / +0.34 for
    −1.69 on that term), through a larger ϑ.
Level 6:
- The leaf constant lowers C₁ and C_S in the leading term of C_(∞,μ)^(2) by 1.05 and 0.70.
- ϱ binds there with ε set by 𝔰_* (G0m.4), and ϱ ∝ 1/(sup C_(∞,μ) k₂^z). So up to about +0.7 to +1.05.
- The word sums act on S_F only, which does not bind at level 6.

Target 1, "a sharper intrinsic rank-3 step":
- Yes, and the same holds for every rank. lem:tl5-hft-leaf bounds the kernel at a point by its trace, which sums over
  the 5^r dimensions of the fibre. The largest eigenvalue is enough, and it is the scalar one.
- C_(E,0)(𝔶) is the best constant of the leaf step for each rank: f du ⊗ ⋯ ⊗ du reduces to the functions, where the
  kernel is extremal.
- "A different split between the curves and the leaves": no.
  - Two rotation derivatives are the fewest whole number with a pointwise bound on S³ (the order must exceed 3/2), and
    the curves need one.
  - With the sharp leaf constant, the split leaves nothing more in this step.

Not done.
- 1/z̲ at the supremum: not attempted. G0m found the split worth 0.00 at the supremum, and G0n prices it at ≤ +0.15
  (D_A).
- The k-term 𝔩 and k₁^D = 𝔨_♯K_rec: no further lever in this argument. K_rec is sharp for its step (P-GRD10), and
  𝔨_♯ → √5.
- Target 3, ε's coefficient of ϱ: not attempted. It carries no Sobolev constant, and the parts with ϱ of the products
  keep 𝔤_(ϱ,s).
- The word sums for the other monomials keep the count 7^(j′/2). These are H₁D̂²h, the curvature terms, the terms of
  2𝔮̂ with a background letter inside β₁, and those of R₃.
  - For them Φ₂ may be a second derivative, whose family needs 𝔩(𝔙_k) ≤ 7^(k/2) 𝔨_A, or a Ψ_C, whose family needs
    (Σ_Z 𝔷_Z²)^(1/2) ≤ √7 𝔷 in place of 𝔷.
  - The gain there would be partly paid back in 𝔨_A and 𝔨_B.
- The split with 𝒟_g in S_M: not done (G0m: worth nothing at the supremum).

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfd	paper/reader/proofs/P-GRD12.md@PENDING:1	P-GRD12, section	new; at the end of ch:ten-l5, after rem:tl5-hfu-what; one leaf constant C_(E,0)(y) for every rank, and the products of type D summed over the words in S_F
    lem:tl5-hfd-leaf	paper/reader/proofs/P-GRD12.md@PENDING:18	P-GRD12, Lemma	the leaf kernel is a multiple of the identity on each isotypic part of the fibre; S_j(y) <= S_0(y) = C_(E,0)(y)^2, so the leaf inequality holds with C_(E,0)(y) for every rank; C_(E,r)^2 <= 5^r C_(E,0)^2
    eq:tl5-hfd-leaf	paper/reader/proofs/P-GRD12.md@PENDING:27	P-GRD12, display	new
    lem:tl5-hfd-words	paper/reader/proofs/P-GRD12.md@PENDING:60	P-GRD12, Lemma	products over the words of one length: the monomials of 2q-hat with both factors DPsi counted with c^(D,7)_n and s_P, the others with 7^(n/2)(c_n - c^D_n) and P
    eq:tl5-hfd-words	paper/reader/proofs/P-GRD12.md@PENDING:73	P-GRD12, display	new
    def:tl5-hfd-constants	paper/reader/proofs/P-GRD12.md@PENDING:108	P-GRD12, Definition	constants with index d: C_(E,0)(y), C_(E,0)^# in every face constant; K^D, K^D_rho, K^D_0 in place of g_(J,s)K, g_(J,s)K_rho, g_(J,s)K_0 in S_F and r_(w,s); eta_d, A_d, B_d, s_*^d
    thm:tl5-hfd	paper/reader/proofs/P-GRD12.md@PENDING:132	P-GRD12, Theorem	thm:tl5-hfp (N >= 6) and thm:tl5-hfu (N = 4) with the constants with index d; contains both for all weights
    eq:tl5-hfd-closing	paper/reader/proofs/P-GRD12.md@PENDING:136	P-GRD12, display	closing condition: 4 eta_d^(-3/2)(delta_w + eta_d^(-1/2)(eps^z + eps_M^d))(S_F^d + S_M^d) < 1
    rem:tl5-hfd-what	paper/reader/proofs/P-GRD12.md@PENDING:163	P-GRD12, Remark	what changes
