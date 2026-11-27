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

    M_g ≤ 2(k₁ + 1) 𝒥_g + 2k₂ ϱ(p),                                                                      {#eq:tl5-hfg-m2}

and at p

    𝔰_g(p) ≤ C_∞(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀(p).                               {#eq:tl5-hfg-linfty}

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

*Zeroth order.* For |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] with A := Ψ_B involves the words JB, |J| ≤ 2, of length at
most |B| + 2, so μ^(|B|+2) Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂ ≤ ℰ_g(p); with μ ≤ 1 in the term on S_a, μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S
ℰ_g(p)^(1/2) + C_(0,0) η₀(p). And μ |H(p)| ≤ 2μ |h(p)|.

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] to A := D̂Ψ_B, as in that proof. The words JB have length at
most |B| + 2 ≤ N − 1, and the factors Ψ_(C′) of the remainders have |C′| ≤ |B| + 1, so the bounds |ℒ^J A| ≤ (1 + 6Λ)
𝒥₁ and |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁ there become μ^((|B|+3)/2) |ℒ^J A| ≤ (1 + 6Λ) 𝒥_g and μ^((|B|+3)/2) |D̂ℒ^J A| ≤ M_g +
6√2 Λ 𝒥_g. By [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], ∫_(Σ₁(a,b)) 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g(p),
𝔨₂ as in [[lem:tl5-hf-linfty]], and [[eq:tl5-hfg-m2]] replaces the bound for M₂; the term on S_a is as there, with μ ≤
1. The computation of that proof then gives μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁ ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p).

*Second order at low levels.* For |B| ≤ N − 4 multiply the bound at p of that proof by μ^((|B|+4)/2). Its first-order
terms involve Ψ_C and D̂Ψ_C with |C| ≤ |B| + 1 ≤ N − 3, which by the two previous steps are bounded with the weights
μ^((|C|+2)/2) and μ^((|C|+3)/2); so L is replaced by L_g := (Σ_(|C|≤N−3) (μ^(|C|+2) |Ψ_C|² + μ^(|C|+3) |D̂Ψ_C|²))^(1/2) ≤
(2𝔐)^(1/2) (max(C_S, C₁) ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)) η₀(p)). Its nonlinear terms come from the
words J with |J| ≤ |B|; their solution factors are low, and in each monomial the factor of largest order o ≤ |B| + 1, and
in H^(αβ) D̂_αD̂_βΨ_J, |J| < |B|, the factor D̂²Ψ_J, has weight at least μ^((|B|+4)/2) in 𝔰_g; bounding it by 𝔰_g and the
others by 𝔰 gives at most k₃ 𝔰(p) 𝔰_g(p) ≤ 𝔰_g(p)/2. So μ^((|B|+4)/2) |D̂²Ψ_B(p)| ≤ k₁ L_g + k₂ ϱ(p) + 𝔰_g(p)/2.

Taking the largest of the four bounds and absorbing 𝔰_g(p)/2 gives [[eq:tl5-hfg-linfty]] with the constants of
[[lem:tl5-hf-linfty]]. ∎

**Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] let I be a
word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I if N ≥ 5, 𝔑^L_I as in
[[lem:tl5-hf4-quadratic]] (b) if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2). Then at every point of Q(τ₁(p), τ₂(p))

    μ^(n/2) |𝔑^L_I| ≤ 𝔠_n (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p)),
    μ^(n/2) |ℒ^J N(h)| ≤ (𝔠_(|J|) + 1) (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p))      for |J| < n.       {#eq:tl5-hfg-products}

*Proof.* For a low solution factor Φ of order o put ℓ_P(Φ) := o + 2, so that |Φ| ≤ μ^(−ℓ_P(Φ)/2) 𝔰_g. For any solution
factor Φ let ℓ_E(Φ) be 0 for H and h, |C| − 1 for Ψ_C with |C| ≥ 1, |C| for D̂Ψ_C and |C| + 1 for D̂²Ψ_C. For every
factor Φ of a monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ n, and for Φ = D̂²Ψ_J with |J| < n,

    μ^(ℓ_E(Φ)/2) |Φ| ≤ 𝔨_g 𝒥_g + 2k₂ ϱ(p).                                                               (∗)

Indeed |H| ≤ 2|h| ≤ 2𝒥_g and |h| ≤ 𝒥_g; for Ψ_C = ℒ_Z Ψ_(C′) with |C| ≥ 1, by [[eq:tl5-hf-lie]], |Ψ_C| ≤ |Z| |D̂Ψ_(C′)| +
2|D̂Z| |Ψ_(C′)| ≤ 𝔷 (|D̂Ψ_(C′)|² + |Ψ_(C′)|²)^(1/2), so μ^((|C|−1)/2) |Ψ_C| ≤ 𝔷 𝒥_g, as |C′| = |C| − 1 ≤ N;
μ^(|C|/2) |D̂Ψ_C| ≤ 𝒥_g; and D̂²Ψ_C has |C| ≤ N − 1 by [[lem:tl5-hf4-quadratic]] (a), so μ^((|C|+1)/2) |D̂²Ψ_C| ≤ M_g,
which [[eq:tl5-hfg-m2]] bounds.

Take a monomial of 𝔑^L_I, with solution factors Φ₁, …, Φ_q, q ≥ 2, and orders o_i. It has at most one high factor, by
[[lem:tl5-hf-quadratic]] for N ≥ 5 and by the definition of 𝔑^L_I for N = 4. Let Φ₂ be the high factor if there is
one, and otherwise a factor of largest order, and Φ₁ another factor; Φ₁ and the others are low. By
[[lem:tl5-hf4-quadratic]] (a), o₁ + o₂ ≤ n + 2 and o₂ ≤ n + 1. If o₂ ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1, and if o₂ = 0 then o₁ = 0;
so in both cases

    ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3,      ℓ_E(Φ₂) ≤ n.                                                      {#eq:tl5-hfg-count}

With |Φ_i| ≤ 𝔰 ≤ 1 for i ≥ 3, (∗), and |Φ₁| bounded by μ^(−ℓ_P(Φ₁)/2) 𝔰_g in the term with 𝒥_g and by 𝔰 in the term
with ϱ(p), the monomial times μ^(n/2) is at most its background norm times

    μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔨_g 𝔰_g 𝒥_g + μ^((n − ℓ_E(Φ₂))/2) 2k₂ 𝔰 ϱ(p) ≤ μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p).

The total background norm is at most 𝔠_n, by the proof of [[lem:tl5-hf-quadratic]], which gives the first inequality.
For |J| < n, ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J, and 𝔑_J = 𝔑^L_J also for N = 4, as |J| ≤ 3; the first inequality for J,
with μ^(n/2) ≤ μ^(|J|/2), bounds μ^(n/2) |𝔑_J|. In the last term ℓ_P(H) = 2 and ℓ_E(D̂²Ψ_J) = |J| + 1 ≤ n, and 2 + |J| +
1 ≤ n + 2; the same splitting bounds μ^(n/2) |H| |D̂²Ψ_J| by μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ(p). ∎

**Lemma {#lem:tl5-hfg-mixed}** (The products of level four, graded.) Let N = 4, and let g, h, t, b, Σ, ϱ and η₀ be as
in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀ on Q(t, b). With 𝔵_t, 𝔶_t and the notation of that lemma, and 𝔍_g := ‖𝒥_g‖_Σ,

    μ^(7/2) ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔵_t 𝔶_t (𝔍_g + ϱ) (𝔍_g + ϱ + η₀),
    𝔍_g² ≤ [𝔨₂]_t Σ_(|I|≤4) μ^|I| ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                          {#eq:tl5-hfg-mixed}

*Proof.* The second inequality follows from [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], as in the proof of
[[lem:tl5-hf4-mixed]]. By [[eq:tl5-hfg-m2]] at the points of Σ, ‖M_g‖_Σ ≤ λ_t 𝔍_g + ς_t ϱ. In the proof of
[[lem:tl5-hf4-mixed]], ‖𝔭_M‖_Σ² ≤ e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²); we bound μ² X₁, μ² X₂, μ^(3/2) Y₁ and μ^(3/2) Y₂.

*μ² X₁.* The factors of Σ_B Σ_J |ℒ^J D̂Ψ_B|² there are D̂Ψ_(JB), |JB| ≤ 4, and Ψ_C, |C| ≤ 3, and μ⁴ ≤ μ^(|JB|), μ^(|C|);
so μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2 · 49 · 1320 Λ² 𝒥_g², and μ² X₁ ≤ (𝔭₃ 𝔵₃(t) (1 + 64680 [Λ]_t²))^(1/2) 𝔍_g.

*μ² X₂.* The factors of Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² there are D̂²Ψ_(JZ), |JZ| ≤ 3, with μ² ≤ μ^((|JZ|+1)/2), and D̂Ψ_C, Ψ_C
with |C| ≤ 2; so μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 621516 Λ⁴ 𝒥_g², and μ² X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 ‖M_g‖_Σ +
789 [Λ]_t² 𝔍_g).

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* In the bounds of Y₁² and Y₂² there, μ³ Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M_g², μ³ Σ_(|B|=2) |D̂Ψ_B|²
≤ 𝒥_g², μ³ Σ_(|B|=3) (|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², and μ³ ≤ 1 in the terms with η₀; so

    μ³ Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍_g² + 49 ‖M_g‖_Σ²),      μ³ Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍_g².

As there, μ² X_i ≤ 𝔵_t (𝔍_g + ϱ) and μ^(3/2) Y_i ≤ 𝔶_t (𝔍_g + ϱ + η₀) for i = 1, 2, and μ^(7/2) (X₁² Y₁² + X₂² Y₂²)^(1/2)
≤ μ² X₁ μ^(3/2) Y₁ + μ² X₂ μ^(3/2) Y₂ gives the first inequality. ∎

**Definition {#def:tl5-hfg-constants}** (The graded constants.) Let N ≥ 5 and the setting be that of
[[def:tl5-hf-constants]], or N = 4 and the setting that of [[def:tl5-hf4-constants]], with δ_w, ϰ₀, ϱ, η₀, 𝔰₁, the
constants of [[lem:tl5-hf-linfty]] (for N = 4, of [[lem:tl5-hf4-linfty]]) and 𝒮 of [[eq:tl5-hf-source]] for a = u*,
b = v* as there. With 𝔨_g as in [[lem:tl5-hfg-products]], put

    𝔤_(N,g) := (Σ_(j≤N) (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠_(j′) + 1))²)^(1/2),
    𝔞_(o,g) := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c) + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    𝔞_(i,g) := ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖ + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    S_(F,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) C_∞ e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) C_∞ e^(φ/2)) dt),
    𝔯_(w,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) (C_(∞,ϱ) ϱ + C_(∞,0) η₀)) dt),
    ε_(w,g) := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ],

C_∞, C_(∞,ϱ), C_(∞,0) and k₁ being evaluated at the point of the supremum. For N = 4 put, with m_t of
[[def:tl5-hf4-constants]],

    S_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t [𝔨₂]_t dt,      𝔯_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_(M,g) := μ^(−3/2) ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t dt,

and for N ≥ 5 let S_(M,g) = 𝔯_(M,g) = ε_(M,g) := 0. Finally

    A_g := √2 δ_w + 2ε_(w,g) + 2ε_(M,g),      B_g := 2 (S_(F,g) + S_(M,g)),      𝔯_g := 𝔯_(w,g) + 𝔯_(M,g),
    𝔰_(*,g) := sup_(p∈D^κ) (2 C_∞(p) μ^(−N/2) e^(φ(p)/2) A_g + C_(∞,ϱ)(p) ϱ(p) + C_(∞,0)(p) η₀).  {#eq:tl5-hfg-constants}

**Proposition {#prop:tl5-hfg-bootstrap}** (The graded a priori estimate.) In the setting of [[def:tl5-hfg-constants]],
suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N) and that

    𝔯_g ≤ 1/4,      η₀ < 𝔰₁,      𝔰_(*,g) < 𝔰₁.                                                   {#eq:tl5-hfg-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_g for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,g) on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_g + B_g Y_s(g)².                                                                          {#eq:tl5-hfg-h1}

*Proof.* Step 1 of the proof of [[prop:tl5-hf-bootstrap]], with A_g in place of A_w and, for N = 4,
[[lem:tl5-hf4-linfty]] in place of [[lem:tl5-hf-linfty]], uses only η₀ < 𝔰₁, 𝔰_(*,g) < 𝔰₁ and Y_σ(g) ≤ 2A_g, and
gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁ ≤ 𝔰₀/2 on D^κ_s, |h|_k̂ < κ_m/2 and θ_H ≤ ϑ. So [[lem:tl5-hfg-linfty]] and
[[lem:tl5-hfg-products]] apply at every point of D^κ_s, and their ϱ(p) and η₀(p) are at most the ϱ and η₀ of
[[def:tl5-hfg-constants]].

Step 2 of that proof (for N = 4, of the proof of [[prop:tl5-hf4-bootstrap]]) holds up to the bound of the nonlinear
terms, which we replace as follows. With 𝔑^L_I as in [[lem:tl5-hfg-products]], the nonlinear terms of L̂Ψ_I +
H^(αβ) D̂_αD̂_βΨ_I other than 𝔑^M_I are −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I, and 𝔔_IJ ≠ 0 with J ≠ I only for |J| < |I|. By
[[eq:tl5-hfg-products]], by the definition of 𝔮_(jj′) and the Cauchy–Schwarz inequality over the 7^(j′) words of each
length j′ ≤ |I| ([[def:tl5-hf-coupling]]), the family of these terms over |I| = j has norm at most

    μ^(−j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠_(j′) + 1) (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g + 2k₂ 𝔰 ϱ),

with 𝔮_(jj) = 1. As for the forcing terms in the proof of [[prop:tl5-hf-linear-n]], with the weights μ^|I| and the
Cauchy–Schwarz inequality over j, their contribution to the bulk is at most 2Ω̂² 𝔤_(N,g) (μ^(−3/2) 𝔨_g 𝔰_g 𝒥_g +
2k₂ 𝔰 ϱ)(√e_o + √c √e_i), e_o and e_i being the weighted sums. By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ (1/z̲ + 1/c) e_o +
e_i, so, with √e_o + √c √e_i ≤ √2 (e_o + e_i)^(1/2), 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2) (e_o + e_i);
and 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ, as 𝔰 ≤ 1/8. By (a) of [[lem:tl5-hf-quasilinear]], with |D̂H| = |g⁻¹ (D̂h) g⁻¹| ≤ 𝔤₀² |D̂h| ≤
𝔤₀² μ^(−3/2) 𝔰_g, |H| ≤ μ^(−1) 𝔰_g ≤ μ^(−3/2) 𝔰_g and |D̂Ψ|² ≤ (e_o/c + e_i)/(2Ω̂²) for each field, the weighted sum of
2Ω̂² |𝔮_H| is at most μ^(−3/2) 𝔰_g times the first two terms of 𝔞_(o,g) e_o + 𝔞_(i,g) e_i. For N = 4 the terms
𝔑^M_I are bounded as in the proof of [[prop:tl5-hf4-bootstrap]], with [[lem:tl5-hfg-mixed]] in place of
[[lem:tl5-hf4-mixed]]: the two factors there are 49 [𝔠₄]_t ‖𝔭_M‖_Σ and at most μ^(−2) Y_s, and 𝔍_g ≤ [𝔨₂]_t^(1/2) Y_s,
so the term is at most ∫_(−10)^(u*) m_t μ^(−3/2) (𝔍_g + ϱ)(𝔍_g + ϱ + η₀) Y_s dt ≤ S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² + ε_(M,g)
Y_s. Hence the bulk of the weighted sum over I is at most

    ∫ e^(−φ) (2Ω̂² (s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ)(√e_o + √c √e_i) + μ^(−3/2) 𝔰_g (𝔞_(o,g) e_o + 𝔞_(i,g) e_i)) dμ du dv

plus, for N = 4, S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² + ε_(M,g) Y_s.

Step 3 of that proof applies with 𝔰_g in place of 𝔰: by [[eq:tl5-hfg-linfty]], as ℰ_g(p) ≤ e^(φ(p)) Y_s², φ being at
most φ(p) on Σ₁(τ₁(p), τ₂(p)), 𝔰_g ≤ C_∞ e^(φ/2) Y_s + C_(∞,ϱ) ϱ + C_(∞,0) η₀ at every point; so for every a′ ≤ u*,
b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,g) + ε_(M,g)) + 𝔯_g Y_s² + (S_(F,g) + S_(M,g)) Y_s³,

and with ϑ ≤ 1/4 and 𝔯_g ≤ 1/4 the conclusion follows as there. ∎

**Theorem {#thm:tl5-hfg}** (Existence close to an explicit background, with the graded constants.) In the setting of
[[thm:tl5-hf]] (N ≥ 6) suppose (a) and (b) of that theorem, and, with the constants of [[def:tl5-hfg-constants]],

(c) 𝔯_(w,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁ and the closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g)) S_(F,g) < 1.                                                  {#eq:tl5-hfg-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_g and 𝔰_(*,g) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]], [[eq:tl5-hfg-h1]] and
[[eq:tl5-hfg-closing]] in place of A_w, B_w, [[prop:tl5-hf-bootstrap]], [[eq:tl5-hf-h1]] and [[eq:tl5-hf-closing]]. For
(H2), the proof of [[lem:tl5-hf-persistence]] uses [[prop:tl5-hf-bootstrap]] only through 𝔰 ≤ 𝔰_* < 𝔰₁ on D^κ_s, which
its Step 1 gives, and the bound Y_σ ≤ 2A_w; [[prop:tl5-hfg-bootstrap]] gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁ under Y_σ ≤ 2A_g, so that
proof gives (H2) with A_g in place of A_w. The bound for ε is [[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_(*,g). ∎

**Theorem {#thm:tl5-hf4g}** (Level four, with the graded constants.) In the setting of [[thm:tl5-hf4]] suppose (a) and
(b) of that theorem, and, with the constants of [[def:tl5-hfg-constants]] for N = 4,

(c) 𝔯_(w,g) + 𝔯_(M,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁ and the closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g) + 2ε_(M,g)) (S_(F,g) + S_(M,g)) < 1.                          {#eq:tl5-hf4g-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_g and 𝔰_(*,g) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]] for N = 4, [[eq:tl5-hfg-h1]] and
[[eq:tl5-hf4g-closing]] in its place; for (H2), the proof of [[lem:tl5-hf4-persistence]] uses
[[prop:tl5-hf4-bootstrap]] only through 𝔰 ≤ 𝔰_* on D^κ_s and the bound Y_σ ≤ 2A_(w,4), and [[prop:tl5-hfg-bootstrap]]
gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁ under Y_σ ≤ 2A_g. ∎

**Remark {#rem:tl5-hfg-powers}** (The powers of μ.) In S_(F,g), S_(M,g) and 𝔯_g the only power of μ is μ^(−3/2), at every
level N ≥ 4: 𝔤_(N,g), 𝔨_g, 𝔞_(o,g), 𝔞_(i,g), C_∞, C_(∞,ϱ), C_(∞,0) and m_t do not depend on μ. In S_F of [[thm:tl5-hf]]
and [[thm:tl5-hf4]] the factor is μ^(−N), and S_M of [[thm:tl5-hf4]] carries μ^(−2). The power μ^(−3/2) is that of the
count [[eq:tl5-hfg-count]], which gives exactly n + 3 for the term D̂Ψ_B · D̂Ψ_(B′) of 2𝔮 with |B| + |B′| = n and
|B| ≤ N − 3: D̂Ψ_B is bounded at a point through the energies of level |B| + 3, and D̂Ψ_(B′) through those of level |B′|.
The smallness 𝔰_(*,g) < 𝔰₁ keeps the factor μ^(−N/2), as the ungraded 𝔰 is what the recovery of second derivatives
absorbs; ε_(w,g) involves μ only through the weights of s_N, and ε_(M,g), which is of second order in ϱ and η₀, carries
μ^(−3/2).
