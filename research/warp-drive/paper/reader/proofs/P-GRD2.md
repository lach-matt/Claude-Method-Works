### The constants sharpened a second time {#sec:tl5-hfs}

This section sharpens the constants of [[sec:tl5-hfg]] further and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with them.
Four changes are made, each a proved restatement. First, every background factor is bounded by a bound of its own order,
also inside the iterated Lie derivatives of ĝ⁻¹, of g⁻¹, of D̂h and of D̂²h, so that in every product of bounds the
orders add up to at most the number of letters of the term ([[def:tl5-hfs-bounds]], [[lem:tl5-hfs-quadratic]]). Second,
the letters that a quadratic term of level n places on
background factors cost no power of μ: a term whose background factors carry b letters is bounded with the factor
μ^((b−3)/2), and the forcing of level j′ in the equation of level j keeps the weight μ^((j−j′)/2)
([[lem:tl5-hfs-products]]). Third, the recovery of second derivatives keeps the weights of the levels it couples, so
its constant k₁ becomes k₁^(j,μ), and the top-level recovery constant enters each quadratic term once: a term whose
factor in the energies is a second derivative has no derivative on the factor at a point ([[lem:tl5-hfs-linfty]],
[[lem:tl5-hfs-products]]). Fourth, at level four the products with no factor at a point are summed over the words
before the Hölder inequality, which removes the word count and the coefficient 𝔠₄ from their terms of second order, the
terms of higher order keeping 49 𝔰_♭ 𝔠^(3♮)₄ ([[lem:tl5-hfs-quadratic]], [[lem:tl5-hfs-mixed]]).
The closing conditions are [[eq:tl5-hfs-closing]] and [[eq:tl5-hf4s-closing]]; those of [[thm:tl5-hf]],
[[thm:tl5-hf4]], [[thm:tl5-hfg]] and [[thm:tl5-hf4g]] remain valid, and any of them may be used. Throughout, N ≥ 4,
μ ∈ (0, 1], the notation is that of [[sec:tl5-hfg]] with the second expansion of [[def:tl5-hfg-graded]], and for N = 4
the quantities 𝔰, 𝔧 and 𝔭_M are those of [[def:tl5-hf4-levels]].

**Definition {#def:tl5-hfs-bounds}** (Bounds of their own order.) Let Λ_k, Λ^R_k (0 ≤ k ≤ N) and 𝔰_♭ ∈ (0, 1/8] be as
in [[def:tl5-hfg-graded]], and put 𝔤₁ := 1 + 2𝔰_♭. For 1 ≤ k ≤ N let A(k) be the set of the finite sequences a = (a₁,
…, a_r) of positive integers with a₁ + ⋯ + a_r = k, and put, with the binomial coefficients C(·, ·),

    λ^♮_k := Σ_(a∈A(k)) (k!/(a₁! ⋯ a_r!)) Λ_(a₁) ⋯ Λ_(a_r),
    b^♮_g(k) := Σ_(a∈A(k)) (k!/(a₁! ⋯ a_r!)) 𝔤₁^(r+1) (Λ_(a₁) + 1) ⋯ (Λ_(a_r) + 1),
    β₁^♮(k) := 1 + 2 Σ_(j=1)^k C(k, j) Λ_j,
    β₂^♮(k) := 1 + Σ_(l=1)^k Σ_(j=1)^l C(l − 1, j − 1) Λ_j (7 + 10 Σ_(i=1)^(l−j) C(l − j, i) Λ_i),

r being the length of a, and λ^♮₀ := 1, λ̂^♮₀ := √5, λ̂^♮_k := λ^♮_k (k ≥ 1), b^♮_g(0) := 𝔤₀, β₁^♮(0) := β₂^♮(0) := 1.
With Σ^m_n of [[def:tl5-hfg-graded]] put

    𝔠^(2♮)_n := Σ⁴_n λ^♮_(k₁) λ^♮_(k₃) β₂^♮(k₄) − 1 + 5 Σ⁵_n λ^♮_(k₁) λ^♮_(k₃) Λ^R_(k₄)
                + 16 Σ⁴_n λ̂^♮_(k₁) λ̂^♮_(k₂) β₁^♮(k₃) β₁^♮(k₄),
    𝔠^(3♮)_n := Σ⁶_n b^♮_g(k₁) λ^♮_(k₃) λ^♮_(k₅) β₂^♮(k₆) − 𝔤₀ + 5 Σ⁷_n b^♮_g(k₁) λ^♮_(k₃) λ^♮_(k₅) Λ^R_(k₆)
                + 16 Σ⁶_n b^♮_g(k₁) λ^♮_(k₃) (b^♮_g(k₄) + λ̂^♮_(k₄)) β₁^♮(k₅) β₁^♮(k₆),                  {#eq:tl5-hfs-cn}

and 𝔠^♮_n := 𝔠^(2♮)_n + 𝔰_♭ 𝔠^(3♮)_n. For ν ∈ (0, 1] let 𝔠^♮_n(ν) be 𝔠^♮_n formed with ν^(a/2) Λ_a and ν^(a/2) Λ^R_a in
place of Λ_a and Λ^R_a for every a, the other numbers being formed from these; so 𝔠^♮_n(1) = 𝔠^♮_n, and λ^♮_k is
replaced by ν^(k/2) λ^♮_k. For 0 ≤ j ≤ N − 1, with the notation of [[lem:tl5-hf-linfty]] and [[lem:tl5-hfg-linfty]],
put

    α_𝔄^(j,μ) := √2 max_(|C|≤j) Σ_J μ^((|C|+1−|J|)/2) ‖𝔄_CJ‖,
    k₁^(j,μ) := (6/5) ((√3 + 8/3) K_rec (1 + μ^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + μ^(1/2) 𝔯₀
                + (4/3) α_𝔄^(j,μ)),      k₁^μ := k₁^(N−1,μ),      Λ₂^μ := max(μ Λ₁, μ^(3/2) Λ₂),

the sum over the words J with |J| ≤ |C|, and

    𝔰_P⁰ := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2)).

So k₁^(j,1) = k₁^(j), and k₁^(j,μ) ≤ k₁^(j). The number λ^♮_k is the norm bound of ℒ^K ĝ⁻¹, |K| = k, that the
expansion of the proof of [[lem:tl5-hf-quadratic]] (iv) gives when each factor ℒ^B ĝ is bounded by Λ_(|B|) and each
factor ĝ⁻¹ by 1; λ_k := λ^♮_k is admissible in [[def:tl5-hfg-graded]], by [[lem:tl5-hfs-quadratic]] (a).

**Lemma {#lem:tl5-hfs-quadratic}** (The quadratic terms with bounds of their own order.) Let h be as in
[[def:tl5-hfg-graded]], p a point with 𝔰(p) ≤ 𝔰_♭, and I a word with n := |I| ≤ N.

(a) For words J, K with |J| = |K| = k at p: ℒ^J D̂h − D̂Ψ_J is a sum of monomials, each the contraction of one factor
ℒ^B Γ′[π^Z] with one Ψ_C, of which 2C(k, j) have a factor carrying j letters; ℒ^J D̂²h − D̂²Ψ_J is a sum of monomials
of total background norm at most β₂^♮(k) − 1; |ℒ^K ĝ⁻¹| ≤ λ^♮_k; and ℒ^K g⁻¹ is a sum of monomials of total background
norm at most b^♮_g(k). In each monomial the background factors carry disjoint letters, and the norm of the background
part is a product of the bounds Λ_a of its factors, a the number of letters each carries, and of numbers that carry no
letter (𝔤₀, 𝔤₁, the counts).

(b) In the second expansion of the proof of [[lem:tl5-hfg-quadratic]], ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I is a sum of
monomials with q ≥ 2 solution factors whose orders add up to at most n − b + 2, b the number of letters carried by the
background factors of the monomial, and whose background norms ν, with the coefficients, satisfy for every ν′ ∈ (0, 1]

    Σ ν ν′^(b/2) 𝔰(p)^(q−2) ≤ 𝔠^♮_n(ν′).                                                                {#eq:tl5-hfs-sum}

(c) For N = 4 and |I| = 4 let 𝔑^M_I be as in [[lem:tl5-hfg-quadratic]] for the second expansion, and put P₁² :=
Σ_(|B|=|B′|=2) |D̂Ψ_B|² |D̂Ψ_(B′)|² and P₂² := Σ_(|B|=3) Σ_(Z∈Γ) |Ψ_B|² |D̂²Ψ_Z|², so that 𝔭_M² = P₁² + P₂². Then at p

    𝔠^M₁ := 480 + 49 𝔰_♭ 𝔠^(3♮)₄,      𝔠^M₂ := 4 + 49 𝔰_♭ 𝔠^(3♮)₄,
    (Σ_(|I|=4) |𝔑^M_I|²)^(1/2) ≤ 𝔠^M₁ P₁ + 𝔠^M₂ P₂.                                                       {#eq:tl5-hfs-m}

*Proof.* (a) By [[eq:tl5-hf-lie-d]] and induction on k, ℒ^J D̂h = D̂Ψ_J − Σ_(l=1)^k Σ_S (ℒ^(Z_S) Γ′[π^(Z_l)]) ⋆
Ψ_(J(l,S)), the inner sum over S ⊂ {1, …, l − 1}, Z_S the subword with indices in S, J(l, S) the word J with the letters
of S and Z_l deleted, and ⋆ the contraction of [[eq:tl5-hf-lie-d]], which has two terms on a 2-tensor and commutes with
Lie derivatives, as it involves no metric. The factor ℒ^(Z_S) Γ′[π^(Z_l)] carries j = |S| + 1 letters, and Σ_l 2C(l − 1,
j − 1) = 2C(k, j). Next, ℒ_Z D̂²A = D̂² ℒ_Z A + [ℒ_Z, D̂²]A, so ℒ^J D̂²h = D̂²Ψ_J + Σ_(l=1)^k ℒ^(Z₁⋯Z_(l−1)) ([ℒ_(Z_l),
D̂²] Ψ_(Z_(l+1)⋯Z_k)), and [ℒ_Z, D̂²]Ψ consists, by (iii) of the proof of [[lem:tl5-hf-quadratic]], of five contractions
of Γ′[π^Z] with D̂Ψ and two of D̂Γ′[π^Z] with Ψ. By Leibniz's rule the coefficient receives j − 1 of the letters Z₁, …,
Z_(l−1), in C(l − 1, j − 1) ways, and carries j letters; the solution factor receives the other l − j, and ℒ^T Ψ_C =
Ψ_(TC), while ℒ^T D̂Ψ_C − D̂Ψ_(TC) has, as just shown, 2C(l − j, i) monomials whose coefficient carries i letters. So the
background norms add up to at most Σ_l Σ_j C(l − 1, j − 1) Λ_j (2 + 5(1 + 2 Σ_i C(l − j, i) Λ_i)) = β₂^♮(k) − 1. By (iv)
of that proof with h = 0, ℒ^K ĝ⁻¹ = Σ (−1)^r ĝ⁻¹ (ℒ^(B₁) ĝ) ĝ⁻¹ ⋯ (ℒ^(B_r) ĝ) ĝ⁻¹, the sum over the ordered sequences of
disjoint nonempty subwords B_i of K covering K; there are k!/(a₁! ⋯ a_r!) of them with |B_i| = a_i. Each ℒ^(B_i) ĝ =
ℒ^(B′) π^Z, B_i = (B′, Z), carries a_i letters, so its norm is at most Λ_(a_i); in the frame F, where ĝ^MN = η^MN, each
factor ĝ⁻¹ joins indices of two distinct factors or raises a free index, which by the Cauchy–Schwarz inequality costs the
factor 1. This gives |ℒ^K ĝ⁻¹| ≤ λ^♮_k. For g⁻¹ the same expansion holds with g⁻¹ and ℒ^(B_i) g = ℒ^(B_i) ĝ + Ψ_(B_i), of
norm sum at most Λ_(a_i) + 1, the second part a solution factor carrying the letters of B_i; and a factor g⁻¹ = ĝ⁻¹ + H
joining two factors or raising an index costs at most 1 + |H| ≤ 1 + 2𝔰 ≤ 𝔤₁, by [[lem:tl5-wg-norms]] (a). This gives
b^♮_g(k).

(b) The second expansion of the proof of [[lem:tl5-hfg-quadratic]] distributes the letters of I over the factors of the
terms of Q and R₃ by Leibniz's rule, and expands ℒ^J D̂h, ℒ^J D̂²h, ℒ^J g⁻¹ and ℒ^K ĝ⁻¹ as in (a). By (a), a monomial
whose background factors carry b letters has a background norm that is a product of bounds Λ_a and Λ^R_a with the a
adding up to b, times numbers carrying no letter; replacing each Λ_a and Λ^R_a by ν′^(a/2) Λ_a and ν′^(a/2) Λ^R_a
multiplies it by ν′^(b/2). The counts of that proof, with the bounds of (a) in place of β₁^g, β₂^g, b_g^g and λ_k, give
[[eq:tl5-hfs-sum]], the terms of Q having q = 2 and those of R₃ q ≥ 3. The order of a solution factor is the number of
its letters plus the number of its derivatives D̂; the solution factors of a monomial carry the n − b letters not on
background factors, disjointly, and at most two derivatives D̂, as in [[lem:tl5-hf4-quadratic]] (a).

(c) Of the monomials of 𝔑^M_I, two high factors carry all four letters, so b = 0. Those of Q are, by the argument of
[[lem:tl5-hfg-quadratic]], the monomials of H₁^(λσ) D̂_λD̂_σ h with three letters, in the positions S ⊂ {1, 2, 3, 4}, on
h and one on D̂²h, which are bounded by |Ψ_(I_S)| |D̂²Ψ_(I_(S^c))| with coefficient λ^♮₀² = 1, I_S the subword of I in
the positions S; and the monomials of 2𝔮̂ with two letters on each factor D̂h, bounded by 16
λ̂^♮₀² |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))| = 80 |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))|, |S| = 2. For fixed S the map I ↦ (I_S, I_(S^c)) is a
bijection from the words of length 4 onto the pairs of words of lengths |S| and 4 − |S|; so, by Minkowski's inequality
over the six sets S with |S| = 2 and the four with |S| = 3, these monomials contribute at most 6 · 80 P₁ + 4 P₂ to the
left side of [[eq:tl5-hfs-m]]. Each monomial of R₃ in 𝔑^M_I is bounded by ν 𝔰^(q−2) times one of the products whose
squares are the terms of 𝔭_M², with Σ ν 𝔰^(q−2) ≤ 𝔰_♭ 𝔠^(3♮)₄ over them by (b); as there are 7⁴ = 49² words of length 4,
they contribute at most 49 𝔰_♭ 𝔠^(3♮)₄ 𝔭_M ≤ 49 𝔰_♭ 𝔠^(3♮)₄ (P₁ + P₂). ∎

Since Λ_(a_i) ≤ Λ_k, 𝔤₁ ≤ 𝔤₀ and r ≤ k, and the number of the ordered sequences in (a) with r blocks is r! S(k, r),
λ^♮_k, b^♮_g(k), β₁^♮(k) and β₂^♮(k) are at most the numbers λ_k (with the admissible choice of
[[def:tl5-hfg-graded]]), b_g^g(k), β₁^g(k) and β₂^g(k); so 𝔠^♮_n ≤ 𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n.

**Lemma {#lem:tl5-hfs-linfty}** (The low quantities with the weights kept.) Let g, h, p, a, b, ϱ(p) and η₀(p) be as in
[[lem:tl5-hfg-linfty]], let k₃^♮ be k₃^⋆ of [[eq:tl5-hfg-cinf]] with 𝔠^♮_n in place of 𝔠^⋆_n, 𝔰₀^♮ := min(𝔰_♭, 1/(2
sup_(Q(a,b)) k₃^♮)), and C₁^♮ and C_(1,0)^♮ the constants C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂^μ in place of
Λ and k₁^μ in place of k₁, Λ₂^μ evaluated at the points of their suprema. Let C_(∞,μ)^(m), C_((∞,ϱ),μ)^(m) and
C_((∞,0),μ)^(m) be the constants C_∞^(m), C_(∞,ϱ)^(m) and C_(∞,0)^(m) of [[eq:tl5-hfg-cinf]] with k₁^(m,μ), C₁^♮ and
C_(1,0)^♮ in place of k₁^(m), C₁^g and C_(1,0)^g. If 𝔰 ≤ 𝔰₀^♮ on Q(a, b), then at every point of Q(a, b), for every
word C with |C| ≤ j ≤ N − 1,

    |D̂²Ψ_C| ≤ 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ϱ(p),                                            {#eq:tl5-hfs-m2}

so that M_g^(j) ≤ 2(k₁^(j,μ) + 1) 𝒥_g + 2k₂ ϱ(p); and at p, for 0 ≤ m ≤ N − 4,

    𝔰_P⁰(p) ≤ 2C_S ℰ_g(p)^(1/2) + 2C_(0,0) η₀(p),
    𝔰_g^(m)(p) ≤ C_(∞,μ)^(m) ℰ_g(p)^(1/2) + C_((∞,ϱ),μ)^(m) ϱ(p) + C_((∞,0),μ)^(m) η₀(p).            {#eq:tl5-hfs-linfty}

*Proof.* We follow the proof of [[lem:tl5-hfg-linfty]], whose bounds of [[lem:tl5-hf-quadratic]] hold with 𝔠^♮_n by
[[lem:tl5-hfs-quadratic]] (b) with ν′ = 1, as 𝔰 ≤ 𝔰_♭; so k₃^♮ takes the place of k₃^⋆, and k₃^♮ 𝔰 ≤ 1/2.

*Second derivatives.* Let q ∈ Q(a, b) and R_C := 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ϱ(p); we prove
[[eq:tl5-hfs-m2]] by induction on |C| ≤ j. In the bound of [[lem:tl5-hf-recovery]] for Ψ_C, as used in the proof of
[[lem:tl5-hf-linfty]], the words ZC have length |C| + 1, so (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤ μ^(−(|C|+1)/2) 𝒥_g; the terms
with D̂Ψ_C and Ψ_C, among them 𝔯₀ |Ψ_C|, are at most μ^(1/2) μ^(−(|C|+1)/2) 𝒥_g times their coefficients there, as
μ^(|C|/2) (|D̂Ψ_C|² + |Ψ_C|²)^(1/2) ≤ 𝒥_g; and the jets of level |J| ≤ |C| in the maps 𝔄_CJ are at most
μ^((|C|+1−|J|)/2) μ^(−(|C|+1)/2) 𝒥_g. With the residual terms, at most k₂ ϱ(p), this gives the linear part
k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p). In the nonlinear part, the factor of a monomial bounded by 𝔧 there is H, Ψ_(C′)
or D̂Ψ_(C′) with |C′| ≤ |C|, at most 2μ^(−(|C|+1)/2) 𝒥_g, or D̂²Ψ_(C′) with |C′| ≤ |C| − 1, at most R_C by the induction
hypothesis, as μ^(−(|C′|+1)/2) ≤ μ^(−(|C|+1)/2); and H^(αβ) D̂_αD̂_βΨ_J with |J| < |C| is at most 𝔰 R_C. So |D̂²Ψ_C| ≤
k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p) + k₃^♮ 𝔰 (2μ^(−(|C|+1)/2) 𝒥_g + R_C) ≤ R_C, by k₃^♮ 𝔰 ≤ 1/2. Multiplying by
μ^((|C|+1)/2) ≤ 1 gives the bound of M_g^(j).

*Zeroth order.* This is the step of that proof: μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p) for |B| ≤
N − 2, and μ |H(p)| ≤ 2μ |h(p)|; this gives the bound of 𝔰_P⁰(p).

*First order.* In the step of that proof for A := D̂Ψ_B, |B| ≤ N − 3, a coefficient of the remainder R′ in ℒ^J A, J a
word of rotations with |J| ≤ 2, carries a ≤ 2 letters and is contracted with Ψ_C or, after D̂, with D̂Ψ_C,
where |C| = |J| + |B| − a ≤ |B| + 2 − a; so μ^((|B|+3)/2) times its contribution is at most μ^((1+a)/2) Λ_a μ^(|C|/2)
(|Ψ_C| + |D̂Ψ_C|), and μ^((1+a)/2) Λ_a ≤ Λ₂^μ; on S_a it is at most μ^((1+a)/2) Λ_a η₀(p). By [[eq:tl5-hfs-m2]]
with |JB| + 1 ≤ |B| + 3, μ^((|B|+3)/2) |D̂²Ψ_(JB)| ≤ 2(k₁^μ + 1) 𝒥_g + 2k₂ ϱ(p). The argument of that step then gives
μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^♮ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^♮ η₀(p).

*Second order at low levels.* In the step of that proof for |B| ≤ m, multiplied by μ^((|B|+4)/2), the terms with D̂Ψ_(ZB)
are bounded by L_g as there; those with D̂Ψ_B, Ψ_B and 𝔯₀ Ψ_B carry the factor μ^(1/2) more than their weights in L_g,
and the jets of level |J| ≤ |B| in 𝔄_BJ the factor μ^((|B|+1−|J|)/2), as μ^((|B|+4)/2) = μ^((|B|+1−|J|)/2) μ^((|J|+3)/2)
and μ^((|B|+4)/2) ≤ μ^((|B|+1−|J|)/2) μ^((|J|+2)/2). So k₁^(m) is replaced by k₁^(m,μ), and C₁^g and C_(1,0)^g by C₁^♮
and C_(1,0)^♮ through the first-order step. Taking the largest of the bounds and absorbing 𝔰_g^(m)/2 as there gives
[[eq:tl5-hfs-linfty]]. ∎

**Lemma {#lem:tl5-hfs-products}** (The quadratic terms with the letters on the background free.) In the setting of
[[lem:tl5-hfs-linfty]] suppose that 𝔰 ≤ 𝔰₀^♮ on Q(a, b), and let I be a word with n := |I| ≤ N, 𝔑_I and 𝔑^L_I as in
[[lem:tl5-hfg-products]], for N = 4 with the second expansion. Put 𝔨_A := 2k₁^μ + 2, 𝔨_B := max(𝔷, 2), 𝔰_P :=
𝔰_g^(m_P) and 𝔓 := max(𝔨_A 𝔰_P⁰, 𝔨_B 𝔰_P). Then at every point of Q(a, b), for every word J with |J| < n,

    μ^(n/2) |𝔑^L_I| ≤ μ^(−3/2) 𝔠^♮_n(μ) 𝔓 𝒥_g + μ^(n/2) 𝔠^♮_n 2k₂ 𝔰 ϱ(p),
    μ^(n/2) |ℒ^J N(h)| ≤ μ^((n−|J|−3)/2) (𝔠^♮_(|J|)(μ) + 1) 𝔓 𝒥_g
                         + μ^(n/2) (𝔠^♮_(|J|) + 1) 2k₂ 𝔰 ϱ(p).                                     {#eq:tl5-hfs-products}

*Proof.* Take a monomial of 𝔑^L_I with q solution factors, ν its background norm with the coefficient and b the number of
letters on its background factors, and choose Φ₁ and Φ₂ as in the proof of [[lem:tl5-hfg-products]], with ℓ_P and ℓ_E as
there. By [[lem:tl5-hfs-quadratic]] (b) the orders satisfy o₁ + o₂ ≤ n − b + 2, so the argument of that proof gives
ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n − b + 3. If Φ₂ = D̂²Ψ_C, then |Φ₂| ≤ 𝔨_A μ^(−ℓ_E(Φ₂)/2) 𝒥_g + 2k₂ ϱ(p) by [[eq:tl5-hfs-m2]], and Φ₁
carries no derivative D̂, as there are at most two in all, so it is H, h or Ψ_B with |B| ≤ N − 2 and |Φ₁| ≤
μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰. Otherwise μ^(ℓ_E(Φ₂)/2) |Φ₂| ≤ 𝔨_B 𝒥_g, by the proof of (∗) there, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P, by
that proof. With |Φ₁| ≤ 𝔰 in the term with ϱ(p) and |Φ_i| ≤ 𝔰 for the other factors, the monomial times μ^(n/2) is at
most ν 𝔰^(q−2) (μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔓 𝒥_g + μ^(n/2) 2k₂ 𝔰 ϱ(p)), and μ^((n − ℓ_P − ℓ_E)/2) ≤ μ^(−3/2) μ^(b/2).
By [[eq:tl5-hfs-sum]] with ν′ = μ and with ν′ = 1 this gives the first inequality. For |J| < n, 𝔑_J = 𝔑^L_J, also for
N = 4 as |J| ≤ 3, and μ^(n/2) |𝔑_J| = μ^((n−|J|)/2) μ^(|J|/2) |𝔑_J| is bounded by the first inequality for J; in
H^(αβ) D̂_αD̂_βΨ_J the factor D̂²Ψ_J is
the factor Φ₂ of the first kind, with Φ₁ = H, b = 0 and ℓ_P(H) + ℓ_E(D̂²Ψ_J) = |J| + 3. ∎

**Lemma {#lem:tl5-hfs-mixed}** (The products of level four, summed over the words.) Let N = 4, and let g, h, t, b, Σ,
ϱ, η₀, 𝔍_g, ς_t, X₁, X₂, Y₁ and Y₂ be as in [[lem:tl5-hfg-mixed]] and its proof, with 𝔰 ≤ 𝔰₀^♮ on Q(t, b). Put
λ_t^μ := 2([k₁^μ]_t + 1),

    ϖ₁ := 6 (2μ^(1/2) Λ₁)² + 36 (4μ^(1/2) Λ₁ + 2μ Λ₂)²,
    ϖ₂ := 6 (7μ^(1/2) Λ₁)² + 36 (14μ^(1/2) Λ₁ + 10μ Λ₁² + 7μ Λ₂)²,
    𝔛_(1,t) := (𝔭₃ 𝔵₃(t) (1 + 49 [ϖ₁]_t))^(1/2),
    𝔛_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (14 [ϖ₂]_t)^(1/2)),      𝔛′_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t,
    𝔜_(1,t) := 𝔱₃(t)^(1/2) (1 + 7λ_t^μ),   𝔜′_(1,t) := 7 𝔱₃(t)^(1/2) ς_t,   𝔜″_(1,t) := π (98 [𝔳⁶]_t)^(1/2),
    𝔜_(2,t) := 𝔱₂(t)^(1/2),   𝔜″_(2,t) := π (686 [𝔳⁴]_t)^(1/2).

Then, with P₁ and P₂ as in [[lem:tl5-hfs-quadratic]] (c),

    ‖P₁‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) X₁ Y₁,      ‖P₂‖_Σ ≤ e^(φ(t,b)/2) 𝔪(t) X₂ Y₂,
    μ² X₁ ≤ 𝔛_(1,t) 𝔍_g,   μ^(3/2) Y₁ ≤ 𝔜_(1,t) 𝔍_g + 𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀,
    μ² X₂ ≤ 𝔛_(2,t) 𝔍_g + 𝔛′_(2,t) ϱ,   μ^(3/2) Y₂ ≤ 𝔜_(2,t) 𝔍_g + 𝔜″_(2,t) η₀.                       {#eq:tl5-hfs-mixed}

*Proof.* ‖P₁‖_Σ² is the sum of ‖|D̂Ψ_B| |D̂Ψ_(B′)|‖_Σ² over the pairs (B, B′), and ‖P₂‖_Σ² that of ‖|Ψ_B| |D̂²Ψ_Z|‖_Σ²
over the pairs (B, Z); [[eq:tl5-hf4-holder]] for each pair, with X := D̂Ψ_B, Y := D̂Ψ_(B′) and X := D̂²Ψ_Z, Y := Ψ_B,
gives the first line. In the proof of [[lem:tl5-hfg-mixed]], replace the bounds of the remainders R′ and R as follows. By
[[lem:tl5-hfs-quadratic]] (a) with Ψ_B in place of h, R′ for a rotation word J has 2 monomials whose coefficient carries
one letter if |J| = 1, and 4 with one letter and 2 with two letters if |J| = 2; each is contracted with a Ψ_C, |C| = |JB|
− a for a coefficient with a letters, and μ² ≤ μ^(a/2) μ^(|C|/2) as |JB| ≤ 4. So μ² |R′| ≤ ρ′_(|J|) 𝒥_g with ρ′₁ :=
2μ^(1/2) Λ₁ and ρ′₂ := 4μ^(1/2) Λ₁ + 2μ Λ₂, and Σ_(|J|≤2) ρ′_(|J|)² = ϖ₁ over the 6 words of length one and 36 of length
two; with the 49 words B, μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 98 ϖ₁ 𝒥_g², which with [[lem:tl5-hf4-face]] (b) for r = 3
gives the bound of μ² X₁. Likewise R for ℒ^J D̂²Ψ_Z has background norm at most β₂^♮(|J|) − 1, that is 7Λ₁ for |J| = 1
and 14Λ₁ + 10Λ₁² + 7Λ₂ for |J| = 2, each monomial contracted with Ψ_C or D̂Ψ_C, |C| = |JZ| − a ≤ 3 − a, and μ² ≤ μ^(a/2)
μ^(|C|/2); with the 7 fields Z, μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 14 ϖ₂ 𝒥_g², and ‖M_g‖_Σ ≤ λ_t^μ 𝔍_g + ς_t ϱ by
[[eq:tl5-hfs-m2]] with j = 3, which with [[lem:tl5-hf4-face]] (b) for r = 4 gives the bound of μ² X₂. The bounds of μ³
Y₁² and μ³ Y₂² of that proof, with ‖M_g‖_Σ ≤ λ_t^μ 𝔍_g + ς_t ϱ and (x + y + z)^(1/2) ≤ x^(1/2) + y^(1/2) + z^(1/2), give
those of μ^(3/2) Y₁ and μ^(3/2) Y₂; the bound of Y₂ contains no second derivative. ∎

**Definition {#def:tl5-hfs-constants}** (The constants sharpened a second time.) Let N ≥ 5 and the setting be that of
[[def:tl5-hf-constants]], or N = 4 and the setting that of [[def:tl5-hf4-constants]], with δ_w, ϰ₀, 𝔰_θ, ϱ, η₀ and 𝒮
as there, and with the constants of [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]] put C_P^♮ := C_(∞,μ)^(m_P),
C_(P,ϱ)^♮ := C_((∞,ϱ),μ)^(m_P), C_(P,0)^♮ := C_((∞,0),μ)^(m_P), 𝔣₀ := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c), 𝔣₁ := ϰ₀ +
(1/2)|T| ‖𝒞_(·0)‖ and 𝔣₂ := 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2). Put

    𝔰₀^♮ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮)),      𝔰₁^♮ := min(𝔰₀^♮/2, c_* κ_m/2, 𝔰_θ),
    𝔤_(𝒥,s) := (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1))²)^(1/2),
    𝔤_(ϱ,s) := (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′) + 1))²)^(1/2),
    𝔎 := max(2C_S 𝔨_A, C_P^♮ 𝔨_B),   𝔎_ϱ := C_(P,ϱ)^♮ 𝔨_B,   𝔎₀ := max(2C_(0,0) 𝔨_A, C_(P,0)^♮ 𝔨_B),
    𝔞_(o,s) := 𝔣₀ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎,      𝔞_(i,s) := 𝔣₁ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎,
    𝔟_(o,s) := 𝔣₀ (C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀) + 𝔣₂ 𝔤_(𝒥,s) (𝔎_ϱ ϱ + 𝔎₀ η₀),
    𝔟_(i,s) := 𝔣₁ (C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀) + 𝔣₂ 𝔤_(𝒥,s) (𝔎_ϱ ϱ + 𝔎₀ η₀),
    S_(F,s) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,s) e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,s) e^(φ/2)) dt),
    𝔯_(w,s) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) 𝔟_(o,s) dt + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) 𝔟_(i,s) dt),
    ε_(w,s) := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(ϱ,s) k₂ ϱ],

the functions of p being evaluated at the point of the supremum. For N = 4 put, with the notation of
[[lem:tl5-hfs-mixed]], [𝔠^M_i]_t the number 𝔠^M_i formed with the suprema over Σ₁(t, v*) of the Λ_k and the Λ^R_k, and
w_t := e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t 𝔪(t),

    S_(M,s) := μ^(−3/2) ∫_(−10)^(u*) w_t ([𝔠^M₁]_t 𝔛_(1,t) 𝔜_(1,t) + [𝔠^M₂]_t 𝔛_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_(M,s) := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) ([𝔠^M₁]_t 𝔛_(1,t) (𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀)
               + [𝔠^M₂]_t (𝔛_(2,t) 𝔜″_(2,t) η₀ + 𝔛′_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_(M,s) := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t [𝔠^M₂]_t 𝔛′_(2,t) 𝔜″_(2,t) dt,

and for N ≥ 5 let S_(M,s) = 𝔯_(M,s) = ε_(M,s) := 0. Finally, with the constants of [[eq:tl5-hfg-cinf]],

    A_s := √2 δ_w + 2ε_(w,s) + 2ε_(M,s),      B_s := 2 (S_(F,s) + S_(M,s)),      𝔯_s := 𝔯_(w,s) + 𝔯_(M,s),
    𝔰_(*,s) := sup_(p∈D^κ) (2 C_∞^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_s
               + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀).                                    {#eq:tl5-hfs-constants}

**Proposition {#prop:tl5-hfs-bootstrap}** (The a priori estimate with the constants sharpened a second time.) In the
setting of [[def:tl5-hfs-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N)
and that

    𝔯_s ≤ 1/4,      η₀ < 𝔰₁^♮,      𝔰_(*,s) < 𝔰₁^♮.                                               {#eq:tl5-hfs-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_s for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,s) on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_s + B_s Y_s(g)².                                                                          {#eq:tl5-hfs-h1}

*Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hfg-bootstrap]], with 𝔰₀^♮, 𝔰₁^♮ and A_s in place of 𝔰₀^⋆,
𝔰₁^⋆ and A_g, and [[eq:tl5-hfs-linfty]] for m = N − 4 and μ = 1, whose constants are then those of
[[eq:tl5-hfg-cinf]], in place of [[eq:tl5-hfg-linfty]]: this gives 𝔰 ≤ 𝔰_(*,s) < 𝔰₁^♮ on D^κ_s, |h|_k̂ < κ_m/2 and
θ_H ≤ ϑ, and [[lem:tl5-hfs-quadratic]], [[lem:tl5-hfs-linfty]] and [[lem:tl5-hfs-products]] apply at every point of
D^κ_s, with ϱ(p) ≤ ϱ and η₀(p) ≤ η₀.

*Step 2.* Step 2 of the proof of [[prop:tl5-hfg-bootstrap]] holds up to the bounds of the nonlinear terms, which we
replace as follows. By [[eq:tl5-hfs-products]], the definition of 𝔮_(jj′) and the Cauchy–Schwarz inequality over the
7^(j′) words of each length j′ ≤ j, the family over |I| = j of the nonlinear terms other than 𝔑^M_I has norm at most
μ^(−j/2) (A_j + B_j), with A_j := Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1) μ^(−3/2) 𝔓 𝒥_g and B_j :=
μ^(j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′) + 1) 2k₂ 𝔰 ϱ. As for the forcing terms in the proof of
[[prop:tl5-hf-linear-n]], with the weights μ^|I| and Minkowski's and the Cauchy–Schwarz inequalities over j, their
contribution to the bulk is at most 2Ω̂² (𝔤_(𝒥,s) μ^(−3/2) 𝔓 𝒥_g + 𝔤_(ϱ,s) 2k₂ 𝔰 ϱ)(√e_o + √c √e_i); with 2Ω̂² 𝒥_g
(√e_o + √c √e_i) ≤ 𝔣₂ (e_o + e_i), as there, and 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ, it is at most 2Ω̂² (1/4) 𝔤_(ϱ,s) k₂ ϱ (√e_o +
√c √e_i) + μ^(−3/2) 𝔣₂ 𝔤_(𝒥,s) 𝔓 (e_o + e_i). The terms 2Ω̂² |𝔮_H| are bounded as there, with 𝔰_P ≥ 𝔰_P⁰: at most
μ^(−3/2) 𝔰_P (𝔣₀ e_o + 𝔣₁ e_i). For N = 4, the terms 𝔑^M_I contribute, by the proof of [[prop:tl5-hf4-bootstrap]], at
most ∫ [2Ω̂² (1 + c/κ′)^(1/2)]_t μ⁴ ‖(Σ_(|I|=4) |𝔑^M_I|²)^(1/2)‖_Σ μ^(−2) Y_s dt over the faces Σ := Σ₁(t, b′), the
Cauchy–Schwarz inequality over I being taken at each point; by [[eq:tl5-hfs-m]] and [[eq:tl5-hfs-mixed]], μ²
‖(Σ_I |𝔑^M_I|²)^(1/2)‖_Σ ≤ μ^(−3/2) e^(φ(t,v*)/2) 𝔪(t) ([𝔠^M₁]_t (μ² X₁)(μ^(3/2) Y₁) + [𝔠^M₂]_t (μ² X₂)(μ^(3/2) Y₂)),
and expanding with 𝔍_g ≤ [𝔨₂]_t^(1/2) Y_s bounds the term by S_(M,s) Y_s³ + 𝔯_(M,s) Y_s² + ε_(M,s) Y_s.

*Step 3.* By [[eq:tl5-hfs-linfty]] for m = m_P and ℰ_g(p) ≤ e^(φ(p)) Y_s², at every point 𝔰_P ≤ C_P^♮ e^(φ/2) Y_s +
C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀ and 𝔰_P⁰ ≤ 2C_S e^(φ/2) Y_s + 2C_(0,0) η₀, so 𝔓 ≤ 𝔎 e^(φ/2) Y_s + 𝔎_ϱ ϱ + 𝔎₀ η₀. Foliating
as in Step 3 of the proof of [[prop:tl5-hf-bootstrap]], for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,s) + ε_(M,s)) + 𝔯_s Y_s² + (S_(F,s) + S_(M,s)) Y_s³,

and with ϑ ≤ 1/4 and 𝔯_s ≤ 1/4 the conclusion follows as there. ∎

**Theorem {#thm:tl5-hfs}** (Existence close to an explicit background, with the constants sharpened a second time.) In
the setting of [[thm:tl5-hf]] (N ≥ 6) let Λ_k, Λ^R_k and 𝔰_♭ be as in [[def:tl5-hfs-bounds]], and suppose: (a) η₀ <
𝔰₁^♮; (b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N); (c) the constants of
[[def:tl5-hfs-constants]] satisfy 𝔯_(w,s) ≤ 1/4, 𝔰_(*,s) < 𝔰₁^♮ and the closing condition

    4 A_s B_s = 8 (√2 δ_w + 2ε_(w,s)) S_(F,s) < 1.                                                  {#eq:tl5-hfs-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_s and 𝔰_(*,s) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hfg]] applies with A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]],
[[eq:tl5-hfs-h1]] and [[eq:tl5-hfs-closing]] in place of A_g, B_g, 𝔰_(*,g), 𝔰₁^⋆, [[prop:tl5-hfg-bootstrap]],
[[eq:tl5-hfg-h1]] and [[eq:tl5-hfg-closing]]; it uses only 𝔰 ≤ 𝔰_(*,s) < 𝔰₁^♮ ≤ min(1/16, 𝔰_θ) and the bound
Y_σ ≤ 2A_s. ∎

**Theorem {#thm:tl5-hf4s}** (Level four, with the constants sharpened a second time.) In the setting of
[[thm:tl5-hf4]] let Λ_k, Λ^R_k and 𝔰_♭ be as in [[def:tl5-hfs-bounds]] with N = 4, and suppose: (a) η₀ < 𝔰₁^♮; (b)
a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) the constants of [[def:tl5-hfs-constants]] with N = 4
satisfy 𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4, 𝔰_(*,s) < 𝔰₁^♮ and the closing condition

    4 A_s B_s = 8 (√2 δ_w + 2ε_(w,s) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1.                          {#eq:tl5-hf4s-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_s and 𝔰_(*,s) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4g]] applies with A_s, B_s, 𝔰_(*,s), 𝔰₁^♮, [[prop:tl5-hfs-bootstrap]] for N = 4,
[[eq:tl5-hfs-h1]] and [[eq:tl5-hf4s-closing]] in place of A_g, B_g, 𝔰_(*,g), 𝔰₁^⋆, [[prop:tl5-hfg-bootstrap]],
[[eq:tl5-hfg-h1]] and [[eq:tl5-hf4g-closing]]; [[eq:tl5-hf4-m2]] holds by [[eq:tl5-hfs-m2]] with μ = 1 and j = 3. ∎

**Remark {#rem:tl5-hfs-what}** (What the second sharpening changes.) A background factor that carries a letters enters
𝔤_(𝒥,s) as μ^(a/2) Λ_a or μ^(a/2) Λ^R_a, and the forcing of level j′ in the equation of level j as μ^((j−j′)/2) 𝔮_(jj′),
the weights of the coupling 𝔒 of [[eq:tl5-hf-bn]]; a product of bounds Λ_(a₁) ⋯ Λ_(a_r) occurs only with a₁ + ⋯ + a_r
at most the number of letters of the term, against the powers Λ_k^r of [[def:tl5-hfg-graded]]. The constant of the term
with ϱ in ε_(w,s), 𝔤_(ϱ,s), has the weights μ^j of 𝔤_N of [[def:tl5-hf-constants]]; in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s), ϱ
carries μ^(−3/2) as in [[sec:tl5-hfg]]. The recovery constant of the highest level enters 𝔎 through 𝔨_A
in the first entry and through C₁^♮ in the second, not as a product; it enters as k₁^μ, whose couplings 𝔄_CJ carry
the weights μ^((|C|+1−|J|)/2) ≤ μ^(1/2), as do its terms with 𝔯₀ and with D̂Z and D̂²Z. At level four,
S_(M,s) contains the coefficients 𝔠^M₁ = 480 + 49 𝔰_♭ 𝔠^(3♮)₄ and 𝔠^M₂ = 4 + 49 𝔰_♭ 𝔠^(3♮)₄ in place of 49 [𝔠^⋆₄]_t, and
k₁^μ once in each of the two products 𝔛_(1,t) 𝔜_(1,t) and 𝔛_(2,t) 𝔜_(2,t). The smallness 𝔰_(*,s) < 𝔰₁^♮ keeps the
constants of [[eq:tl5-hfg-cinf]] and the factor μ^(−N/2), for the reasons given in [[rem:tl5-hfg-powers]]. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfs]] and [[thm:tl5-hf4s]] are established in this
paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The sections sec:tl5-hf, sec:tl5-hf4 and sec:tl5-hfg stay as they are, and all four of their closing conditions remain
valid: the constants of this section are added beside them, for the reason recorded for sec:tl5-hfg (the constants
interlock with hypothesis (a) through 𝔰₁^♮, and the merged numbered statements are cited elsewhere). Old texts are quoted
exactly from chapters/87-ten-l5.md at HEAD cea4ff8f, where sec:tl5-hfg is merged (last change to the chapter at
82e04d11). Line numbers serve only to find the place. Each new text replaces its old text as a whole, with the line
breaks shown.

*1. Where the section goes.* The section above, from its heading ("The constants sharpened a second time", label
sec:tl5-hfs) through the last line of [[rem:tl5-hfs-what]], is inserted at the end of [[ch:ten-l5]], after the last line
of [[rem:tl5-hfg-powers]] (line 5424 once item 2 is applied), with one blank line before it. It is a sibling of
sec:tl5-hf, sec:tl5-hf4 and sec:tl5-hfg (a "###" heading) and comes after them. It cites results of those three sections
as they stand and the proofs of prop:tl5-hfg-bootstrap, prop:tl5-hf4-bootstrap, thm:tl5-hfg and thm:tl5-hf4g with the
replacements it states. It defines the labels listed in the crosswalk rows, none defined elsewhere. No number already
printed changes.

*2. The last sentence of [[rem:tl5-hfg-powers]] (lines 5422–5423).* Old:

its coefficients, less 1 for the subtracted term. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
[[thm:tl5-hfg]] and [[thm:tl5-hf4g]] are established in this paper for no background at 10 l5.

New:

its coefficients, less 1 for the subtracted term. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
[[thm:tl5-hfg]] and [[thm:tl5-hf4g]] are established in this paper for no background at 10 l5. [[sec:tl5-hfs]]
sharpens these constants a second time ([[thm:tl5-hfs]], [[thm:tl5-hf4s]]).

*3. Nothing else changes.* No other text of the chapters changes; [[thm:tl5-hfs]] and [[thm:tl5-hf4s]] give (H1), (H2)
and (H4) of [[lem:tl5-continuation]] and reduce (H3) to [[eq:tl5-hfs-closing]] and [[eq:tl5-hf4s-closing]], as the
earlier theorems do.

### Comparison and the factors for the evaluation

Not chapter text. "Proved" refers to the section above; "deduced" marks statements about the method that no proof here
establishes; "computed" marks numbers I evaluated (floating point).

*Closing conditions (proved).*

    level ≥ 6:  8 (√2 δ_w + 2ε_(w,s)) S_(F,s) < 1,  with 𝔯_(w,s) ≤ 1/4, η₀ < 𝔰₁^♮, 𝔰_(*,s) < 𝔰₁^♮   (thm:tl5-hfs)
    level 4:    8 (√2 δ_w + 2ε_(w,s) + 2ε_(M,s)) (S_(F,s) + S_(M,s)) < 1,  with 𝔯_(w,s) + 𝔯_(M,s) ≤ 1/4 and
                η₀ < 𝔰₁^♮, 𝔰_(*,s) < 𝔰₁^♮   (thm:tl5-hf4s)

The closing conditions of thm:tl5-hf, thm:tl5-hf4, thm:tl5-hfg and thm:tl5-hf4g stay valid; δ_w is unchanged.

*Every new factor, as a formula.* At a point, Λ_k, Λ^R_k, 𝔰_♭, 𝔤₀ = √5 + 1/4 and Σ^m_n as in def:tl5-hfg-graded;
A(k) the compositions a = (a₁, …, a_r) of k; ν^(a/2)-weighted numbers by replacing Λ_a, Λ^R_a by ν^(a/2) Λ_a,
ν^(a/2) Λ^R_a:

    𝔤₁ = 1 + 2𝔰_♭;  λ^♮_k = Σ_(a∈A(k)) (k!/Πa_i!) Π Λ_(a_i);  b^♮_g(k) = Σ_(a∈A(k)) (k!/Πa_i!) 𝔤₁^(r+1) Π (Λ_(a_i) + 1);
    β₁^♮(k) = 1 + 2 Σ_j C(k, j) Λ_j;  β₂^♮(k) = 1 + Σ_(l≤k) Σ_(j≤l) C(l−1, j−1) Λ_j (7 + 10 Σ_(i≤l−j) C(l−j, i) Λ_i);
    λ^♮₀ = 1, λ̂^♮₀ = √5, b^♮_g(0) = 𝔤₀;  𝔠^(2♮)_n, 𝔠^(3♮)_n by eq:tl5-hfs-cn;  𝔠^♮_n = 𝔠^(2♮)_n + 𝔰_♭ 𝔠^(3♮)_n;
    𝔠^♮_n(μ): the same with μ^(a/2) Λ_a, μ^(a/2) Λ^R_a (so λ^♮_k → μ^(k/2) λ^♮_k);
    k₃^♮ = (8/5) max_(|C|≤N−1) (𝔠^♮_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠^♮_(|J|) + 1));  𝔰₀^♮ = min(𝔰_♭, 1/(2 sup k₃^♮));
    𝔰₁^♮ = min(𝔰₀^♮/2, c_* κ_m/2, 𝔰_θ);
    α_𝔄^(j,μ) = √2 max_(|C|≤j) Σ_(|J|≤|C|) μ^((|C|+1−|J|)/2) ‖𝔄_CJ‖;
    k₁^(j,μ) = (6/5)((√3 + 8/3) K_rec (1 + μ^(1/2) √7 (3 max|D̂Z| + 2 max|D̂²Z|)) + μ^(1/2) 𝔯₀ + (4/3) α_𝔄^(j,μ));
    k₁^μ = k₁^(N−1,μ);  Λ₂^μ = max(μ Λ₁, μ^(3/2) Λ₂);
    C₁^♮² = 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ₂^μ)²
              + 4|∂_γ|² (72 (Λ₂^μ)² + 8(k₁^μ + 1)²));
    C_(1,0)^♮² = 516π² C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ₂^μ)²;
    C_(∞,μ)^(m) = 2 max(2C_S, C₁^♮, k₁^(m,μ) (2𝔐^(m))^(1/2) max(C_S, C₁^♮)), likewise C_((∞,ϱ),μ)^(m), C_((∞,0),μ)^(m)
              (eq:tl5-hfg-cinf with k₁^(m,μ), C₁^♮, C_(1,0)^♮);  C_P^♮ = C_(∞,μ)^(m_P), m_P = min(1, N − 4);
    𝔨_A = 2k₁^μ + 2;  𝔨_B = max(𝔷, 2);  𝔎 = max(2C_S 𝔨_A, C_P^♮ 𝔨_B);  𝔎_ϱ = C_(P,ϱ)^♮ 𝔨_B;
    𝔎₀ = max(2C_(0,0) 𝔨_A, C_(P,0)^♮ 𝔨_B);
    𝔤_(𝒥,s) = (Σ_(j≤N) (Σ_(j′≤j) μ^((j−j′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(μ) + 1))²)^(1/2);
    𝔤_(ϱ,s) = (Σ_(j≤N) μ^j (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′) + 1))²)^(1/2);
    𝔣₀ = ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c);  𝔣₁ = ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖;  𝔣₂ = 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2);
    𝔞_(o,s) = 𝔣₀ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎;  𝔞_(i,s) = 𝔣₁ C_P^♮ + 𝔣₂ 𝔤_(𝒥,s) 𝔎;
    S_(F,s) = μ^(−3/2) (∫ sup_(Σ₁(t,v*)) 𝔞_(o,s) e^(φ/2) dt + ∫ sup_(Σ₂(u*,t)) 𝔞_(i,s) e^(φ/2) dt);
    𝔯_(w,s) = μ^(−3/2) (∫ sup 𝔟_(o,s) dt + ∫ sup 𝔟_(i,s) dt),  𝔟 = 𝔣₀ or 𝔣₁ times (C_(P,ϱ)^♮ ϱ + C_(P,0)^♮ η₀)
              plus 𝔣₂ 𝔤_(𝒥,s) (𝔎_ϱ ϱ + 𝔎₀ η₀);
    ε_(w,s) = 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(ϱ,s) k₂ ϱ];
    𝔰_(*,s) = sup_p (2C_∞^(N−4) μ^(−N/2) e^(φ/2) A_s + C_(∞,ϱ)^(N−4) ϱ + C_(∞,0)^(N−4) η₀)  (P-GRD's μ-free constants);
    level 4:  λ_t^μ = 2([k₁^μ]_t + 1),  ς_t as merged;
              ϖ₁ = 6(2μ^(1/2)Λ₁)² + 36(4μ^(1/2)Λ₁ + 2μΛ₂)²,  ϖ₂ = 6(7μ^(1/2)Λ₁)² + 36(14μ^(1/2)Λ₁ + 10μΛ₁² + 7μΛ₂)²;
              𝔛₁ = (𝔭₃ 𝔵₃(t)(1 + 49[ϖ₁]_t))^(1/2),  𝔛₂ = (𝔭₄𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (14[ϖ₂]_t)^(1/2)),
              𝔛′₂ = (𝔭₄𝔵₄(t)/2)^(1/2) √602 ς_t;
              𝔜₁ = 𝔱₃(t)^(1/2)(1 + 7λ_t^μ),  𝔜′₁ = 7𝔱₃(t)^(1/2) ς_t,  𝔜″₁ = π(98[𝔳⁶]_t)^(1/2),  𝔜₂ = 𝔱₂(t)^(1/2),
              𝔜″₂ = π(686[𝔳⁴]_t)^(1/2);
              𝔠^M₁ = 480 + 49 𝔰_♭ [𝔠^(3♮)₄]_t,  𝔠^M₂ = 4 + 49 𝔰_♭ [𝔠^(3♮)₄]_t;
              w_t = e^(φ(t,v*)/2) [2Ω̂²(1 + c/κ′)^(1/2)]_t 𝔪(t);
              S_(M,s) = μ^(−3/2) ∫ w_t (𝔠^M₁ 𝔛₁𝔜₁ + 𝔠^M₂ 𝔛₂𝔜₂) [𝔨₂]_t dt;
              𝔯_(M,s) = μ^(−3/2) ∫ w_t [𝔨₂]_t^(1/2) (𝔠^M₁ 𝔛₁ (𝔜′₁ϱ + 𝔜″₁η₀) + 𝔠^M₂ (𝔛₂𝔜″₂η₀ + 𝔛′₂𝔜₂ϱ)) dt;
              ε_(M,s) = μ^(−3/2) ϱ η₀ ∫ w_t 𝔠^M₂ 𝔛′₂ 𝔜″₂ dt.

[f]_t is the supremum over the face Σ₁(t, v*); [𝔳⁴]_t, [𝔳⁶]_t are face suprema.

*The briefed items, one by one.*

1. The r-fold Λ_k powers (proved, no hypothesis on the background). Every iterated Lie derivative is expanded exactly
   (lem:tl5-hfs-quadratic (a)): ℒ^K ĝ⁻¹ over ordered set partitions with block sizes a, k!/Πa_i! of each, each block
   bounded by its own Λ_(a_i); likewise ℒ^K g⁻¹ (b^♮_g, with 𝔤₁ ≈ 1 for an inner g⁻¹ in place of 𝔤₀), ℒ^J D̂h (β₁^♮:
   2C(k, j) monomials with a j-letter coefficient) and ℒ^J D̂²h (β₂^♮). The only products of Λ's left are Π Λ_(a_i)
   over a composition of the letters of one factor (Σ a_i ≤ k) and Λ_j Λ_i (j + i ≤ k) in β₂^♮. G0d's variant
   hypothesis Λ_a Λ_b ≤ Λ₁ Λ_(a+b−1) is not needed; the formulas take the measured Λ_a as they are. Computed: at
   Λ_a = Λ^R_a = 1, 𝔠^(2♮)_n = 85, 587, 3.90e3, 2.68e4, 2.01e5, 1.73e6, 1.71e7 (n = 0…6).
2. The μ weights (proved). Two separate weights are restored. (i) The letters on background factors are free: a
   monomial of level n with b background letters gets μ^((b−3)/2), so 𝔤_(𝒥,s) uses 𝔠^♮(μ) with μ^(a/2)Λ_a; this
   suppresses exactly the single-factor Λ_N growth (the factor carrying all letters gets μ^(N/2)). (ii) The forcing of
   level j′ in the equation of level j keeps μ^((j−j′)/2) on 𝔮_(jj′). Computed illustration (not a background): with
   Λ_a = Λ^R_a = 10^(a+1) and μ = 10⁻⁵, 𝔠^(2♮)_6(μ) = 1.44e5 against 𝔠^(2♮)_6 = 1.47e18. The ϱ-part of ε_(w,s) keeps
   the merged weights μ^j (𝔤_(ϱ,s), the target ϱ of the merged set, m4); in 𝔯_(w,s), 𝔯_(M,s) and ε_(M,s), ϱ and η₀
   carry μ^(−3/2) as in P-GRD, and 𝔰_* is as in P-GRD.
3. The top-level k₁ (proved in part). (i) It enters each quadratic term once: 𝔎 = max(2C_S 𝔨_A, C_P^♮ 𝔨_B), and at
   level 4 the products are 𝔛₁𝔜₁ (k₁ only in 𝔜₁) and 𝔛₂𝔜₂ (k₁ only in 𝔛₂). (ii) It enters as k₁^μ, whose couplings
   carry μ^((|C|+1−|J|)/2) ≤ μ^(1/2) and whose 𝔯₀ and 𝔷-terms carry μ^(1/2); only (6/5)(√3 + 8/3)K_rec is unweighted.
   Why not fewer (deduced): in branch B the factor at a point is D̂Ψ_B, whose Sobolev bound needs the ∂_γ-derivative of
   D̂Ψ_(JB) on the face, and its component D̂²Ψ(E₁, E₁) comes only from the equation, i.e. through k₁^μ; in branch A the
   factor in the energies is D̂²Ψ_C with |C| up to N − 1 and needs k₁^μ itself.
4. C_P against a sharper C_S (not done; what blocks it). The factors 𝔭₃ = 11,773, 𝔳⁶𝔴⁶ and 258 = 6 · 43 come from the
   Sobolev inequality via Euclidean components on 𝒱. An intrinsic inequality on the leaves would use that the six
   rotations act on the tensors over S³ by a representation of SO(4), with Σ ℒ_(K_ab)² a Casimir operator: the bound
   |A(ω)|² ≤ Σ_π (dim π)(mult_π)/(2π² (1 + c_π)²) · ‖(1 + Casimir)A‖² needs the decomposition of the bundle (ℝ² ⊕
   TS³)^(⊗r), r ≤ 4, into SO(4)-isotypic parts (Frobenius reciprocity over SO(3)) with their Casimir eigenvalues c_π
   and multiplicities, and a norm comparison of the round metric with k on the leaves (which brings back a condition
   number, R and the shift). That branching computation, with explicit constants, is not carried out here; the k₁^μ
   inside C₁^♮ is item 3.
5. The 𝔮 couplings and the word count. The couplings now carry μ^((j−j′)/2) (item 2 (ii); proved). The count 7^(j′/2)
   remains (not done): an ℓ² sum over the words removes the count of the letters on the factor in the energies only;
   the letters on the factor at a point and on background factors keep √7 each, and the choice of the energy factor
   would have to enter the Leibniz count. At level 4 the terms of second order of the products with no factor at a
   point have no count left: they are summed over the words exactly (lem:tl5-hfs-quadratic (c)), which replaces
   49 [𝔠^⋆₄]_t in S_M by 480 and 4; the terms of higher order keep 49 𝔰_♭ [𝔠^(3♮)₄]_t (proved).
6. O1 (proved): λ^♮_k has no factor 5^((r+1)/2); λ^♮_1 = Λ₁; at Λ ≡ 1, λ^♮_k = F_k.

*Notes for the evaluation.* (i) 𝔠^♮_n(μ) at μ < 1 is computed by weighting each Λ_a, Λ^R_a by μ^(a/2) before forming
λ^♮, b^♮_g, β^♮; in b^♮_g the "+ 1" (solution part) is not weighted. (ii) k₃^♮, 𝔰₀^♮, 𝔰₁^♮ and 𝔤_(ϱ,s) use 𝔠^♮ at
μ = 1. (iii) 𝔰_♭ multiplies 𝔠^(3♮) in 𝔠^♮ and in 𝔠^M_i, and caps 𝔰₁^♮ ≤ 𝔰_♭/2. (iv) The previous sets remain valid
fallbacks.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfs	paper/reader/proofs/P-GRD2.md@PENDING:1	P-GRD2, section	new; at the end of ch:ten-l5, after rem:tl5-hfg-powers, beside sec:tl5-hf, sec:tl5-hf4, sec:tl5-hfg (author: keep tightening by hand); second sharpening
    def:tl5-hfs-bounds	paper/reader/proofs/P-GRD2.md@PENDING:21	P-GRD2, Definition	bounds of their own order: lambda^nat, b_g^nat, beta^nat (no Lambda_k^r), c^nat_n and its mu-weighted form, weighted recovery constant k1^(j,mu), Lambda_2^mu, s_P^0
    eq:tl5-hfs-cn	paper/reader/proofs/P-GRD2.md@PENDING:36	P-GRD2, display	new
    lem:tl5-hfs-quadratic	paper/reader/proofs/P-GRD2.md@PENDING:55	P-GRD2, Lemma	exact expansions of the iterated Lie derivatives with per-factor bounds; background letters weighted; level-4 products with no point factor summed over words (coefficients 480, 4)
    eq:tl5-hfs-sum	paper/reader/proofs/P-GRD2.md@PENDING:69	P-GRD2, display	new
    eq:tl5-hfs-m	paper/reader/proofs/P-GRD2.md@PENDING:75	P-GRD2, display	new
    lem:tl5-hfs-linfty	paper/reader/proofs/P-GRD2.md@PENDING:120	P-GRD2, Lemma	lem:tl5-hfg-linfty with the level weights kept in the recovery (k1^(j,mu)); pointwise split bound of D^2 Psi_C
    eq:tl5-hfs-m2	paper/reader/proofs/P-GRD2.md@PENDING:128	P-GRD2, display	new
    eq:tl5-hfs-linfty	paper/reader/proofs/P-GRD2.md@PENDING:133	P-GRD2, display	new
    lem:tl5-hfs-products	paper/reader/proofs/P-GRD2.md@PENDING:167	P-GRD2, Lemma	background letters cost no mu (mu^((b-3)/2)); top-level k1 once per term (branches A and B)
    eq:tl5-hfs-products	paper/reader/proofs/P-GRD2.md@PENDING:174	P-GRD2, display	new
    lem:tl5-hfs-mixed	paper/reader/proofs/P-GRD2.md@PENDING:189	P-GRD2, Lemma	level-4 mixed products with separate constants X_1 Y_1, X_2 Y_2 (k1 once in each)
    eq:tl5-hfs-mixed	paper/reader/proofs/P-GRD2.md@PENDING:204	P-GRD2, display	new
    def:tl5-hfs-constants	paper/reader/proofs/P-GRD2.md@PENDING:221	P-GRD2, Definition	second sharpened constants at levels 6 and 4: g_(J,s) with mu^((j-j')/2), g_(rho,s) with mu^j, K, a_(o,s), a_(i,s), S_(F,s), r_(w,s), eps_(w,s), S_(M,s), r_(M,s), eps_(M,s), A_s, B_s, s_(*,s)
    eq:tl5-hfs-constants	paper/reader/proofs/P-GRD2.md@PENDING:252	P-GRD2, display	new
    prop:tl5-hfs-bootstrap	paper/reader/proofs/P-GRD2.md@PENDING:254	P-GRD2, Proposition	(H1) with the second sharpened constants, levels N >= 4
    eq:tl5-hfs-smallness	paper/reader/proofs/P-GRD2.md@PENDING:258	P-GRD2, display	new
    eq:tl5-hfs-h1	paper/reader/proofs/P-GRD2.md@PENDING:263	P-GRD2, display	new
    thm:tl5-hfs	paper/reader/proofs/P-GRD2.md@PENDING:294	P-GRD2, Theorem	thm:tl5-hf (N >= 6) with the second sharpened constants; (a) eta0 < s1^nat
    eq:tl5-hfs-closing	paper/reader/proofs/P-GRD2.md@PENDING:299	P-GRD2, display	closing condition at level N >= 6: 8 (sqrt2 delta_w + 2 eps_(w,s)) S_(F,s) < 1
    thm:tl5-hf4s	paper/reader/proofs/P-GRD2.md@PENDING:308	P-GRD2, Theorem	thm:tl5-hf4 with the second sharpened constants; (a) eta0 < s1^nat
    eq:tl5-hf4s-closing	paper/reader/proofs/P-GRD2.md@PENDING:313	P-GRD2, display	closing condition at level 4: 8 (sqrt2 delta_w + 2 eps_(w,s) + 2 eps_(M,s)) (S_(F,s) + S_(M,s)) < 1
    rem:tl5-hfs-what	paper/reader/proofs/P-GRD2.md@PENDING:321	P-GRD2, Remark	what the second sharpening changes: mu^(a/2) per background letter, mu^((j-j')/2) on q, k1 once per term, 480/4 in place of 49 c_4

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfg-powers, add "; points to sec:tl5-hfs
(P-GRD2 item 2)".
