### The graded count {#sec:tl5-hfg}

In the constants of [[thm:tl5-hf]] and [[thm:tl5-hf4]] the factor S_F carries μ^(−N): in Step 2 of the proof of
[[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again. This section bounds each factor of a quadratic
term by the energies of the lowest level that controls it. In every term of level n the two levels used add up to at
most n + 3 ([[lem:tl5-hfg-products]]), so that the factor becomes μ^(−3/2) at every level N ≥ 4. The resulting closing
conditions are [[eq:tl5-hfg-closing]] at level N ≥ 6 and [[eq:tl5-hf4g-closing]] at level four ([[thm:tl5-hfg]],
[[thm:tl5-hf4g]]); those of [[thm:tl5-hf]] and [[thm:tl5-hf4]] remain valid, and either may be used. Throughout,
N ≥ 4 and μ ∈ (0, 1]; for N = 4, the quantities 𝔰, 𝔧, Λ and 𝔠_n are those of [[def:tl5-hf4-levels]], and
[[lem:tl5-hf4-linfty]] takes the place of [[lem:tl5-hf-linfty]].

**Definition {#def:tl5-hfg-graded}** (Graded quantities.) Let h be a C^(N+2) symmetric 2-tensor field with g = ĝ + h
Lorentzian, and 𝔰 as in [[def:tl5-hf-levels]]. Put at each point

    𝒥_g := (Σ_(|C|≤N) μ^|C| (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),      M_g := max_(|C|≤N−1) μ^((|C|+1)/2) |D̂²Ψ_C|,
    𝔰_g := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2), μ^((|B|+3)/2) |D̂Ψ_B| (|B| ≤ N − 3),
               μ^((|B|+4)/2) |D̂²Ψ_B| (|B| ≤ N − 4)),
    𝔷 := max_(Z∈Γ) (|Z|² + 4|D̂Z|²)^(1/2),

the maxima over words B and C in Γ, and for p ∈ D^κ, with a := τ₁(p) and b := τ₂(p),

    ℰ_g(p) := Σ_(|I|≤N) μ^|I| ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂.

Each low quantity Φ, of order o as in [[def:tl5-hf4-levels]], enters 𝔰_g with the weight μ^((o+2)/2), and o + 2 ≤ N;
so 𝔰_g ≤ 𝔰 ≤ μ^(−N/2) 𝔰_g.

**Lemma {#lem:tl5-hfg-linfty}** (The low quantities, graded.) Let g be a solution of the reduced problem on D^κ_s, h :=
g − ĝ and p ∈ D^κ_s, and suppose that 𝔰 ≤ 𝔰₀ on Q(τ₁(p), τ₂(p)), with 𝔰₀, k₁, k₂, k₃, C_∞, C_(∞,ϱ), C_(∞,0), ϱ(p) and
η₀(p) as in [[lem:tl5-hf-linfty]]. Then at every point of Q(τ₁(p), τ₂(p))

    M_g ≤ 2(k₁ + 1) 𝒥_g + 2k₂ ϱ(p),                                                                       {#eq:tl5-hfg-m2}

and at p

    𝔰_g(p) ≤ C_∞(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀(p).                                    {#eq:tl5-hfg-linfty}

*Proof.* We follow the proof of [[lem:tl5-hf-linfty]], multiplying each bound by the weight of the quantity it bounds.
That proof uses [[lem:tl5-hf-quadratic]] for words of length at most N − 1, where for N = 4 [[lem:tl5-hf4-quadratic]]
(b) gives the same, 𝔑^M vanishing there. By [[lem:tl5-hf4-quadratic]] (a), the solution factors of a monomial of
ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J are H, or Ψ_C or D̂Ψ_C with |C| ≤ |J|, or D̂²Ψ_C with |C| ≤ |J| − 1.

*Second derivatives.* Let q ∈ Q(τ₁(p), τ₂(p)) and |C| ≤ N − 1, and multiply the bound of [[lem:tl5-hf-recovery]] for
Ψ_C, as used in that proof, by μ^((|C|+1)/2). The words ZC have length |C| + 1, so μ^((|C|+1)/2) (Σ_Z |D̂Ψ_(ZC)|²)^(1/2)
≤ 𝒥_g. The terms with D̂Ψ_C and Ψ_C, and those of the maps 𝔄_CJ, |J| ≤ |C|, are bounded by the multiples of 𝒥_g that
bound them by 𝒥₁ there, as μ^((|C|+1)/2) ≤ μ^(|J|/2); the residual terms by k₂ ϱ(p), as μ ≤ 1. In the nonlinear terms,
each monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, has at most one high factor, the others being at most 𝔰,
and the factor Φ bounded by 𝔧 there satisfies μ^((|C|+1)/2) |Φ| ≤ 2𝒥_g + M_g: for Φ = H as |H| ≤ 2|h|, for Ψ_(C′) and
D̂Ψ_(C′), |C′| ≤ |J|, as μ^((|C|+1)/2) ≤ μ^(|C′|/2), and for D̂²Ψ_(C′), |C′| ≤ |J| − 1, as μ^((|C|+1)/2) ≤
μ^((|C′|+1)/2). Likewise μ^((|C|+1)/2) |H| |D̂²Ψ_J| ≤ 𝔰 M_g for |J| < |C|. So μ^((|C|+1)/2) |D̂²Ψ_C| ≤ k₁ 𝒥_g + k₂ ϱ(p) +
k₃ 𝔰 (2𝒥_g + M_g), and taking the maximum over C, with k₃ 𝔰 ≤ 1/2, M_g/2 ≤ (k₁ + 1) 𝒥_g + k₂ ϱ(p).

*Zeroth order.* For |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] with A := Ψ_B involves the words JB, |J| ≤ 2, of length at most
|B| + 2, so μ^(|B|+2) Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂ ≤ ℰ_g(p); with μ ≤ 1 in the term on S_a, μ^((|B|+2)/2) |Ψ_B(p)| ≤
C_S ℰ_g(p)^(1/2) + C_(0,0) η₀(p). And μ |H(p)| ≤ 2μ |h(p)|.

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] to A := D̂Ψ_B, as in that proof. The words JB have length at
most |B| + 2 ≤ N − 1, and the factors Ψ_(C′) of the remainders have |C′| ≤ |B| + 1, so the bounds |ℒ^J A| ≤ (1 + 6Λ)
𝒥₁ and |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁ there become μ^((|B|+3)/2) |ℒ^J A| ≤ (1 + 6Λ) 𝒥_g and μ^((|B|+3)/2) |D̂ℒ^J A| ≤ M_g +
6√2 Λ 𝒥_g. By [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], ∫_(Σ₁(a,b)) 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g(p),
𝔨₂ as in [[lem:tl5-hf-linfty]], and [[eq:tl5-hfg-m2]] replaces the bound for M₂; the term on S_a is as there, with μ ≤
1. The computation of that proof then gives μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p).

*Second order at low levels.* For |B| ≤ N − 4 multiply the bound at p of that proof by μ^((|B|+4)/2). Its first-order
terms involve Ψ_C and D̂Ψ_C with |C| ≤ |B| + 1 ≤ N − 3, which by the two previous steps are bounded with the weights
μ^((|C|+2)/2) and μ^((|C|+3)/2); so L is replaced by L_g := (Σ_(|C|≤N−3) (μ^(|C|+2) |Ψ_C|² + μ^(|C|+3)
|D̂Ψ_C|²))^(1/2) ≤ (2𝔐)^(1/2) (max(C_S, C₁) ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)) η₀(p)). Its nonlinear
terms come from the words J with |J| ≤ |B|; their solution factors are low, and in each monomial the factor of largest
order o ≤ |B| + 1, and in H^(αβ) D̂_αD̂_βΨ_J, |J| < |B|, the factor D̂²Ψ_J, has weight at least μ^((|B|+4)/2) in 𝔰_g;
bounding it by 𝔰_g and the others by 𝔰 gives at most k₃ 𝔰(p) 𝔰_g(p) ≤ 𝔰_g(p)/2. So μ^((|B|+4)/2) |D̂²Ψ_B(p)| ≤ k₁ L_g +
k₂ ϱ(p) + 𝔰_g(p)/2.

Taking the largest of the four bounds and absorbing 𝔰_g(p)/2 gives [[eq:tl5-hfg-linfty]] with the constants of
[[lem:tl5-hf-linfty]]. ∎

**Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] let I be a
word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I if N ≥ 5, 𝔑^L_I as in
[[lem:tl5-hf4-quadratic]] (b) if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2). Then at every point of Q(τ₁(p), τ₂(p))

    μ^(n/2) |𝔑^L_I| ≤ 𝔠_n (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p)),
    μ^(n/2) |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p))      for |J| < n.           {#eq:tl5-hfg-products}

*Proof.* For a low solution factor Φ of order o put ℓ_P(Φ) := o + 2, so that |Φ| ≤ μ^(−ℓ_P(Φ)/2) 𝔰_g. For any solution
factor Φ let ℓ_E(Φ) be 0 for H and h, |C| − 1 for Ψ_C with |C| ≥ 1, |C| for D̂Ψ_C and |C| + 1 for D̂²Ψ_C. For every
factor Φ of a monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ n, and for Φ = D̂²Ψ_J with |J| < n,

    μ^(ℓ_E(Φ)/2) |Φ| ≤ 𝔨_g 𝒥_g + 2k₂ ϱ(p).                                                               (∗)

Indeed |H| ≤ 2|h| ≤ 2𝒥_g and |h| ≤ 𝒥_g; for Ψ_C = ℒ_Z Ψ_(C′) with |C| ≥ 1, by [[eq:tl5-hf-lie]], |Ψ_C| ≤ |Z| |D̂Ψ_(C′)|
+ 2|D̂Z| |Ψ_(C′)| ≤ 𝔷 (|D̂Ψ_(C′)|² + |Ψ_(C′)|²)^(1/2), so μ^((|C|−1)/2) |Ψ_C| ≤ 𝔷 𝒥_g, as |C′| = |C| − 1 ≤ N; μ^(|C|/2)
|D̂Ψ_C| ≤ 𝒥_g; and D̂²Ψ_C has |C| ≤ N − 1 by [[lem:tl5-hf4-quadratic]] (a), so μ^((|C|+1)/2) |D̂²Ψ_C| ≤ M_g, which
[[eq:tl5-hfg-m2]] bounds.

Take a monomial of 𝔑^L_I, with solution factors Φ₁, …, Φ_q, q ≥ 2, and orders o_i. It has at most one high factor, by
[[lem:tl5-hf-quadratic]] for N ≥ 5 and by the definition of 𝔑^L_I for N = 4. Let Φ₂ be the high factor if there is
one, and otherwise a factor of largest order, and Φ₁ another factor; Φ₁ and the others are low. By
[[lem:tl5-hf4-quadratic]] (a), o₁ + o₂ ≤ n + 2 and o₂ ≤ n + 1. If o₂ ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1, and if o₂ = 0 then o₁ = 0;
so in both cases

    ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3,      ℓ_E(Φ₂) ≤ n.                                                         {#eq:tl5-hfg-count}

With |Φ_i| ≤ 𝔰 ≤ 1 for i ≥ 3, (∗), and |Φ₁| bounded by μ^(−ℓ_P(Φ₁)/2) 𝔰_g in the term with 𝒥_g and by 𝔰 in the term
with ϱ(p), the monomial times μ^(n/2) is at most its background norm times

    μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔨_g 𝔰_g 𝒥_g + μ^((n − ℓ_E(Φ₂))/2) 2k₂ 𝔰 ϱ(p) ≤ μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p).

The total background norm is at most 𝔠_n, by the proof of [[lem:tl5-hf-quadratic]], which gives the first inequality.
For |J| < n, ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J, and 𝔑_J = 𝔑^L_J also for N = 4, as |J| ≤ 3; the first inequality for
J, with μ^(n/2) ≤ μ^(|J|/2), bounds μ^(n/2) |𝔑_J|. In the last term ℓ_P(H) = 2 and ℓ_E(D̂²Ψ_J) = |J| + 1 ≤ n, and 2 +
|J| + 1 ≤ n + 2; the same splitting bounds μ^(n/2) |H| |D̂²Ψ_J| by μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p). ∎

