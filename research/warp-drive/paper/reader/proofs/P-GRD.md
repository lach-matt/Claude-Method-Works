### The sharpened constants {#sec:tl5-hfg}

This section sharpens the constants of [[thm:tl5-hf]] and [[thm:tl5-hf4]] in three ways and proves both theorems with
the sharpened constants. First, each background factor of a quadratic term is bounded by a bound for the derivatives of
ĝ of its own order, instead of the uniform bound Λ, and the constant of the recovery of second derivatives is taken at
the level where it is used ([[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]]). Second, in Step 2 of the proof of
[[prop:tl5-hf-bootstrap]] the low quantities are bounded through the unweighted face energy of level N, at the cost
μ^(−N/2), and the high factor through 𝒥₁, at the cost μ^(−N/2) again; here each factor is bounded by the energies of
the lowest level that controls it, and in every term of level n the two levels used add up to at most n + 3, so that
the factor becomes μ^(−3/2) at every level N ≥ 4 ([[lem:tl5-hfg-products]]). Third, the quadratic part of N(h) is
expanded with its own coefficients, the terms of higher order carrying a factor 𝔰 ([[lem:tl5-hfg-quadratic]]), and the
factor bounded at a point is never a second derivative of a word of length two or more ([[lem:tl5-hfg-products]]). The
closing conditions are [[eq:tl5-hfg-closing]] at level N ≥ 6 and [[eq:tl5-hf4g-closing]] at level four
([[thm:tl5-hfg]], [[thm:tl5-hf4g]]); those of [[thm:tl5-hf]] and [[thm:tl5-hf4]] remain valid, and either may be used.
Throughout, N ≥ 4 and μ ∈ (0, 1]; for N = 4 the quantities 𝔰, 𝔧 and 𝔭_M are those of [[def:tl5-hf4-levels]], and
[[lem:tl5-hf4-linfty]] takes the place of [[lem:tl5-hf-linfty]].

**Definition {#def:tl5-hfg-graded}** (Graded quantities.) Let h be a C^(N+2) symmetric 2-tensor field with g = ĝ + h
Lorentzian. At a point let Λ₀ := 0 ≤ Λ₁ ≤ ⋯ ≤ Λ_N be numbers such that, for k ≥ 1, Λ_k bounds the norms of ℒ^B π^Z, ℒ^B
Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] for |B| ≤ k − 1 and Z ∈ Γ; for 0 ≤ k ≤ N let Λ^R_k bound the norms of ℒ^B R̂ for
the words B with |B| = k, and for 1 ≤ k ≤ N let λ_k bound those of ℒ^K ĝ⁻¹ for the words K with |K| = k; and put Λ̄_k :=
max(Λ_k, Λ_k²), λ₀ := 1, λ̂₀ := √5 and λ̂_k := λ_k for k ≥ 1. A background factor ℒ^B R̂ carries the |B| letters of B,
and ℒ^B π^Z, ℒ^B Γ′[π^Z], ℒ^B D̂Γ′[π^Z] and D̂ℒ^B Γ′[π^Z] carry the |B| + 1 letters of B and Z; so a factor of the last
four kinds that carries at most k letters has norm at most Λ_k. For m ≥ 1 and a function f on ℕ^m write

    Σ^m_n f := Σ_(k∈ℕ^m, k₁+⋯+k_m=n) (n!/(k₁! ⋯ k_m!)) f(k),

and put, with 𝔤₀ and the ordered Bell numbers F_k of [[def:tl5-hf-levels]],

    β₁^g(0) := β₂^g(0) := 1,   β₁^g(k) := 1 + (2^(k+1) − 2) Λ_k,   β₂^g(k) := 1 + (7/3)(4^k − 1) Λ̄_k,
    b_g^g(0) := 𝔤₀,   b_g^g(k) := F_k 𝔤₀^(k+1) (Λ_k + 1)^k,   b_H^g(0) := 1,   b_H^g(k) := (2k + 1) b_g^g(k),
    𝔠^g_n := Σ²_n b_H^g(k₁) β₂^g(k₂) − 1 + 5 Σ³_n b_H^g(k₁) Λ^R_(k₂) + 16 Σ⁴_n b_g^g(k₁) b_g^g(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^Q_n := Σ⁴_n λ_(k₁) λ_(k₃) β₂^g(k₄) − 1 + 5 Σ⁵_n λ_(k₁) λ_(k₃) Λ^R_(k₄) + 16 Σ⁴_n λ̂_(k₁) λ̂_(k₂) β₁^g(k₃) β₁^g(k₄),
    𝔠^(3)_n := Σ⁶_n b_g^g(k₁) λ_(k₃) λ_(k₅) β₂^g(k₆) − 𝔤₀ + 5 Σ⁷_n b_g^g(k₁) λ_(k₃) λ_(k₅) Λ^R_(k₆)
               + 16 Σ⁶_n b_g^g(k₁) λ_(k₃) (b_g^g(k₄) + λ̂_(k₄)) β₁^g(k₅) β₁^g(k₆),                       {#eq:tl5-hfg-cn}

k ≥ 1 where not stated. Fix 𝔰_♭ ∈ (0, 1/8] and one of the two choices 𝔠^⋆_n := 𝔠^g_n, the first expansion, or 𝔠^⋆_n :=
𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n, the second expansion, for all n ≤ N; with the first choice 𝔰_♭ = 1/8 may be taken. Finally put

    𝒥_g := (Σ_(|C|≤N) μ^|C| (|Ψ_C|² + |D̂Ψ_C|²))^(1/2),      M_g^(j) := max_(|C|≤j) μ^((|C|+1)/2) |D̂²Ψ_C|,
    𝔰_g^(m) := max(μ |H|, μ^((|B|+2)/2) |Ψ_B| (|B| ≤ N − 2), μ^((|B|+3)/2) |D̂Ψ_B| (|B| ≤ N − 3),
               μ^((|B|+4)/2) |D̂²Ψ_B| (|B| ≤ m)),
    𝔷 := max_(Z∈Γ) (|Z|² + 4|D̂Z|²)^(1/2),      m_P := min(1, N − 4),

for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4, the maxima over words B and C in Γ, M_g := M_g^(N−1), and for p ∈ D^κ, with a :=
τ₁(p) and b := τ₂(p),

    ℰ_g(p) := Σ_(|I|≤N) μ^|I| ∫_(Σ₁(a,b)) ε₁[Ψ_I] dμ dτ₂.

The order of a solution factor H, Ψ_B, D̂Ψ_B or D̂²Ψ_B is 0, |B|, |B| + 1 or |B| + 2, as in [[def:tl5-hf4-levels]]; a
low quantity of order o enters 𝔰_g^(m) with the weight μ^((o+2)/2), and o + 2 ≤ N, so 𝔰_g^(N−4) ≤ 𝔰 ≤ μ^(−N/2)
𝔰_g^(N−4). For μ = 1, 𝒥_g, M_g, 𝔰_g^(N−4) and ℰ_g(p) are 𝒥₁, M₂, 𝔰 and ℰ⁰_N(p) of [[lem:tl5-hf-linfty]].

Every Λ as in [[def:tl5-hf-levels]] or [[def:tl5-hf4-levels]] may be taken for every Λ_k, k ≥ 1, and every Λ^R_k, as
it bounds the five kinds of factors for words of length at most N; so 𝔠^g_n ≤ 𝔠_n, by Λ ≥ 1 and Σ_(j≤n−k) C(n − k, j)
Λ^R_j ≤ 2^(n−k) Λ, with the binomial coefficients C(·, ·). And λ_k := Σ_(r=1)^k r! S(k, r) 5^((r+1)/2) Λ_k^r may be
taken, S(k, r) the Stirling numbers of the second kind: by (iv) of the proof of [[lem:tl5-hf-quadratic]] with h = 0,
ℒ^K ĝ⁻¹ is a sum of r! S(k, r) products of r + 1 factors ĝ⁻¹, of norm √5, and r factors ℒ^(B′) π^Z, each carrying at
most k letters.

**Lemma {#lem:tl5-hfg-quadratic}** (The quadratic terms with graded background bounds.) Let h be as in
[[def:tl5-hfg-graded]], p a point with 𝔰(p) ≤ 𝔰_♭, and I a word with n := |I| ≤ N. Then ℒ^I N(h) − H^(αβ) D̂_αD̂_β Ψ_I
is a sum of monomials, each a contraction of background factors and of q ≥ 2 solution factors of the forms and orders
of [[lem:tl5-hf4-quadratic]] (a), whose background norms ν, with the coefficients, satisfy

    Σ ν 𝔰(p)^(q−2) ≤ 𝔠^⋆_n,                                                                             {#eq:tl5-hfg-sum}

the sum over the monomials. Consequently [[eq:tl5-hf-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N ≥ 5, and
[[eq:tl5-hf4-g]] holds with 𝔠^⋆_(|I|) in place of 𝔠_(|I|) if N = 4, 𝔑^L_I and 𝔑^M_I being formed from the chosen
expansion.

*Proof.* *The first expansion.* It is that of the proof of [[lem:tl5-hf-quadratic]]. In (i) there, ℒ^J R̂ has norm at
most Λ^R_(|J|). In (ii), with k := |J|, each monomial of R′_J has one coefficient
ℒ^B Γ′[π^Z] whose letters are among those of J, so its norm is at most Λ_k, and ℒ^J D̂h is a sum of monomials of total
background norm at most β₁^g(k). In (iii) each monomial of R_J has at most two background factors, carrying letters of
J, so their product is at most Λ̄_k, and the total is at most β₂^g(k). In (iv) each factor ℒ^B ĝ = ℒ^(B′) π^Z carries
the |B| ≤ k letters of B, so ℒ^J g⁻¹ has total background norm at most b_g^g(k) and ℒ^J H at most b_H^g(k), the
number of factors in the telescoping sums being 2r + 1 ≤ 2k + 1 as there. Summing as in that proof, over the
distributions of the letters of I over the factors of each term of N(h), gives the three sums of 𝔠^g_n: Σ²_n from
H^(λσ) D̂_λD̂_σ h, the letters going to H and to D̂²h, less 1 for the subtracted term H^(αβ) D̂_αD̂_βΨ_I; Σ³_n from the
five terms of 2𝔠(H)h, the letters going to H, R̂ and h; Σ⁴_n from the sixteen units of coefficient of 2𝔮. Every
monomial has q ≥ 2 solution factors and 𝔰(p) ≤ 1, which gives [[eq:tl5-hfg-sum]].

*The second expansion.* Let H₁ := −ĝ⁻¹ h ĝ⁻¹, that is H₁^(αβ) = −ĝ^(αμ) h_μν ĝ^(νβ), and H₂ := H − H₁. Since g⁻¹ −
ĝ⁻¹ = −g⁻¹ h ĝ⁻¹, applied twice, H₂ = g⁻¹ h ĝ⁻¹ h ĝ⁻¹. By [[lem:tl5-hf-reduced]], 2𝔮 = Σ_m c_m 𝒯_m(g⁻¹, g⁻¹, D̂h, D̂h)
with Σ_m |c_m| = 16, each 𝒯_m a contraction, linear in each argument; let 2𝔮̂ := Σ_m c_m 𝒯_m(ĝ⁻¹, ĝ⁻¹, D̂h, D̂h). Then
2𝔮 − 2𝔮̂ = Σ_m c_m (𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹, H, D̂h, D̂h)) with H = −g⁻¹ h ĝ⁻¹, and, 𝔠 being linear in its first
argument, N(h) = Q + R₃ with

    Q := H₁^(λσ) D̂_λD̂_σ h − 2𝔠(H₁)h − 2𝔮̂,      R₃ := H₂^(λσ) D̂_λD̂_σ h − 2𝔠(H₂)h − (2𝔮 − 2𝔮̂).

So ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I is the sum of ℒ^I Q − H₁^(αβ) D̂_αD̂_βΨ_I and ℒ^I R₃ − H₂^(αβ) D̂_αD̂_βΨ_I. Expand
ℒ^I of each term by Leibniz's rule over its factors, as in the proof of [[lem:tl5-hf-quadratic]]: ℒ^J h = Ψ_J;
ℒ^J D̂h, ℒ^J D̂²h and ℒ^J g⁻¹ by (ii), (iii) and (iv) there, with the bounds β₁^g, β₂^g and b_g^g of the first part;
ℒ^J R̂ with norm at most Λ^R_(|J|); and ℒ^K ĝ⁻¹, for K ≠ ∅, as one background factor of norm at most λ_(|K|). The factors
ĝ⁻¹ that carry no letter in H₁, in H₂ and in H = −g⁻¹ h ĝ⁻¹ join an index of h to an index of another factor; in the
frame F, where ĝ^MN = η^MN, such a contraction is bounded by the product of the norms of the two factors, by the
Cauchy–Schwarz inequality, so these factors count λ₀ = 1. A factor ĝ⁻¹ of 𝒯_m that carries no letter may join two
indices of one factor, and counts |ĝ⁻¹| = √5 = λ̂₀. A full contraction of the factors is bounded by the product of
their norms. Summing over the distributions of the letters gives, for the terms of Q, the three sums of 𝔠^Q_n: Σ⁴_n
over the factors ĝ⁻¹, h, ĝ⁻¹, D̂²h of H₁^(λσ) D̂_λD̂_σ h, less 1 for the subtracted term H₁^(αβ) D̂_αD̂_βΨ_I; Σ⁵_n over
ĝ⁻¹, h, ĝ⁻¹, R̂, h for the five terms of 2𝔠(H₁)h; and Σ⁴_n over ĝ⁻¹, ĝ⁻¹, D̂h, D̂h for 2𝔮̂. Likewise the terms of R₃
give the three sums of 𝔠^(3)_n: Σ⁶_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, D̂²h, less b_g^g(0) = 𝔤₀ for H₂^(αβ) D̂_αD̂_βΨ_I;
Σ⁷_n over g⁻¹, h, ĝ⁻¹, h, ĝ⁻¹, R̂, h; and Σ⁶_n over g⁻¹, h, ĝ⁻¹, X, D̂h, D̂h with X = g⁻¹ or X = ĝ⁻¹. In the terms of
Q each of the two factors among h, D̂h and D̂²h keeps exactly one solution factor in its expansion, and the factors ĝ⁻¹
and R̂ none, so q = 2; in the terms of R₃ three such factors keep one each, so q ≥ 3, and 𝔰(p)^(q−2) ≤ 𝔰_♭. This gives
[[eq:tl5-hfg-sum]].

*The forms and the consequences.* In both expansions every term of N(h) carries at most two derivatives D̂ on its
solution factors, the expansions (ii)–(iv) do not increase this number, and the letters of I are distributed over
distinct factors; so the argument of [[lem:tl5-hf4-quadratic]] (a) applies: the orders of the solution factors of a
monomial add up to at most n + 2, and each is at most n + 1, the factor D̂²Ψ_I occurring only in the subtracted terms.
A solution factor is high, in the sense of [[lem:tl5-hf-quadratic]] (N ≥ 5) or of [[lem:tl5-hf4-quadratic]] (N = 4),
exactly when its order is at least N − 1. If N ≥ 5, two high factors would have orders adding up to at least 2N − 2 >
N + 2; so each monomial has at most one, and is bounded by ν 𝔰^(q−1) 𝔧 at p, which by [[eq:tl5-hfg-sum]] gives
[[eq:tl5-hf-g]] with 𝔠^⋆_n. If N = 4, two high factors have orders 3 and 3 and n = 4; with at most two derivatives D̂
and at most four letters they are D̂Ψ_B and D̂Ψ_(B′) with |B| = |B′| = 2, or Ψ_B and D̂²Ψ_Z with |B| = 3 and Z ∈ Γ, and
the other solution factors carry no letter and no derivative, so they are H or h, of norm at most 𝔰(p). With 𝔑^M_I the
sum of these monomials, each is bounded by ν 𝔰^(q−2) times one of the products whose squares are the terms of 𝔭_M²,
and the others by ν 𝔰^(q−1) 𝔧; [[eq:tl5-hfg-sum]] gives [[eq:tl5-hf4-g]] with 𝔠^⋆_n, and 𝔑^M_I = 0 if n ≤ 3. ∎

**Lemma {#lem:tl5-hfg-linfty}** (The low quantities, graded.) Let g be a solution of the reduced problem on D^κ_s, h :=
g − ĝ and p ∈ D^κ_s, with ϱ(p), η₀(p), k₂, C_S, C_(S,0), C_(0,0), C_(1,ϱ), 𝔯₀ and 𝔐 as in [[lem:tl5-hf-linfty]]. Put,
for 0 ≤ j ≤ N − 1 and 0 ≤ m ≤ N − 4,

    α_𝔄^(j) := √2 max_(|C|≤j) Σ_J ‖𝔄_CJ‖,
    k₁^(j) := (6/5) ((√3 + 8/3) K_rec (1 + √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + 𝔯₀ + (4/3) α_𝔄^(j)),
    k₃^⋆ := (8/5) max_(|C|≤N−1) (𝔠^⋆_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠^⋆_(|J|) + 1)),      𝔐^(m) := Σ_(j≤m+1) 7^j,
    C_∞^(m) := 2 max(2C_S, C₁^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_S, C₁^g)),
    C_(∞,ϱ)^(m) := 2 max(C_(1,ϱ), k₁^(m) (2𝔐^(m))^(1/2) C_(1,ϱ) + k₂),
    C_(∞,0)^(m) := 2 max(2C_(0,0), C_(1,0)^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_(0,0), C_(1,0)^g)),          {#eq:tl5-hfg-cinf}

with the maps of [[def:tl5-hf-coupling]] and their norms as in [[lem:tl5-hf-linfty]], C₁^g and C_(1,0)^g the constants
C₁ and C_(1,0) of [[lem:tl5-hf-linfty]] with Λ₂ in place of Λ, and the Λ_k evaluated at the point of the supremum in
C₁^g; so k₁^(N−1) = k₁, 𝔐^(N−4) = 𝔐 and k₃^⋆ ≤ k₃ when 𝔠^⋆_n ≤ 𝔠_n. None of these constants depends on μ. If 𝔰 ≤
𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^⋆)) on Q(a, b), a := τ₁(p), b := τ₂(p), then for every μ ∈ (0, 1], at every point
of Q(a, b)

    M_g^(j) ≤ 2(k₁^(j) + 1) 𝒥_g + 2k₂ ϱ(p)      (0 ≤ j ≤ N − 1),                                         {#eq:tl5-hfg-m2}

and at p, for 0 ≤ m ≤ N − 4,

    𝔰_g^(m)(p) ≤ C_∞^(m)(p) ℰ_g(p)^(1/2) + C_(∞,ϱ)^(m)(p) ϱ(p) + C_(∞,0)^(m)(p) η₀(p),               {#eq:tl5-hfg-linfty}

*Proof.* We follow the proof of [[lem:tl5-hf-linfty]], multiplying each bound by the weight of the quantity it bounds;
for N = 4 that proof applies as in [[lem:tl5-hf4-linfty]]. The bounds of [[lem:tl5-hf-quadratic]] it uses, for words of
length at most N − 1, hold with 𝔠^⋆ by [[lem:tl5-hfg-quadratic]], as 𝔰 ≤ 𝔰_♭ and, for N = 4, 𝔑^M_J = 0 for |J| ≤ 3; so
its inequalities hold with k₃^⋆ in place of k₃, and k₃^⋆ 𝔰 ≤ 1/2. By [[lem:tl5-hfg-quadratic]] the solution factors of a
monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J are H, Ψ_C or D̂Ψ_C with |C| ≤ |J|, or D̂²Ψ_C with |C| ≤ |J| − 1.

*Second derivatives.* Let q ∈ Q(a, b), j ≤ N − 1 and |C| ≤ j, and multiply the bound of [[lem:tl5-hf-recovery]] for Ψ_C,
as used in that proof, by μ^((|C|+1)/2). The words ZC have length |C| + 1, so μ^((|C|+1)/2) (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤
𝒥_g. The terms with D̂Ψ_C and Ψ_C, and those of the maps 𝔄_CJ, |J| ≤ |C|, are bounded by the multiples of 𝒥_g that bound
them by 𝒥₁ there, as μ^((|C|+1)/2) ≤ μ^(|J|/2), with α_𝔄^(j) in place of α_𝔄 as |C| ≤ j; the residual terms by k₂ ϱ(p),
as μ ≤ 1. In the nonlinear terms, each monomial of ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ |C|, has at most one high factor,
the others being at most 𝔰, and the factor Φ bounded by 𝔧 there satisfies μ^((|C|+1)/2) |Φ| ≤ 2𝒥_g + M_g^(j): for Φ = H
as |H| ≤ 2|h|, for Ψ_(C′) and D̂Ψ_(C′), |C′| ≤ |J|, as μ^((|C|+1)/2) ≤ μ^(|C′|/2), and for D̂²Ψ_(C′), |C′| ≤ |J| − 1 ≤ j,
as μ^((|C|+1)/2) ≤ μ^((|C′|+1)/2). Likewise μ^((|C|+1)/2) |H| |D̂²Ψ_J| ≤ 𝔰 M_g^(j) for |J| < |C|. So
μ^((|C|+1)/2) |D̂²Ψ_C| ≤ k₁^(j) 𝒥_g + k₂ ϱ(p) + k₃^⋆ 𝔰 (2𝒥_g + M_g^(j)), and taking the maximum over C, with k₃^⋆ 𝔰 ≤
1/2, M_g^(j)/2 ≤ (k₁^(j) + 1) 𝒥_g + k₂ ϱ(p).

*Zeroth order.* For |B| ≤ N − 2, [[lem:tl5-hf-sobolev]] with A := Ψ_B involves the words JB, |J| ≤ 2, of length at
most |B| + 2, so μ^(|B|+2) Σ_J ∫ ε₁[Ψ_(JB)] dμ dτ₂ ≤ ℰ_g(p); with μ ≤ 1 in the term on S_a, μ^((|B|+2)/2) |Ψ_B(p)| ≤ C_S
ℰ_g(p)^(1/2) + C_(0,0) η₀(p). And μ |H(p)| ≤ 2μ |h(p)|.

*First order.* For |B| ≤ N − 3 apply [[eq:tl5-hf-cs-r]] to A := D̂Ψ_B, as in that proof. For a word J of rotations
with |J| ≤ 2 the coefficients of the remainder R′ in ℒ^J A = D̂Ψ_(JB) + R′ carry at most two letters, so their norms and
those of their derivatives D̂ are at most Λ₂. The words JB have length at most |B| + 2 ≤ N − 1, and the factors Ψ_(C′) of
the remainders have |C′| ≤ |B| + 1, so the bounds |ℒ^J A| ≤ (1 + 6Λ) 𝒥₁ and |D̂ℒ^J A| ≤ M₂ + 6√2 Λ 𝒥₁ there become
μ^((|B|+3)/2) |ℒ^J A| ≤ (1 + 6Λ₂) 𝒥_g and μ^((|B|+3)/2) |D̂ℒ^J A| ≤ M_g + 6√2 Λ₂ 𝒥_g. By [[eq:tl5-hf-coercive]] and
[[lem:tl5-hf-densities]], ∫_(Σ₁(a,b)) 𝒥_g² dμ dτ₂/(1 − κκ′) ≤ sup 𝔨₂ ℰ_g(p), 𝔨₂ as in [[lem:tl5-hf-linfty]], and
[[eq:tl5-hfg-m2]] with j = N − 1 replaces the bound for M₂; the term on S_a is as there, with μ ≤ 1 and Λ₂ in place of Λ.
The argument of that proof then gives μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^g ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + C_(1,0)^g η₀(p).

*Second order at low levels.* Let |B| ≤ m and multiply the bound at p of that proof by μ^((|B|+4)/2). Its first-order
terms involve Ψ_C and D̂Ψ_C with |C| ≤ |B| + 1 ≤ m + 1 ≤ N − 3, which by the two previous steps are bounded with the
weights μ^((|C|+2)/2) and μ^((|C|+3)/2); so L is replaced by L_g := (Σ_(|C|≤m+1) (μ^(|C|+2) |Ψ_C|² +
μ^(|C|+3) |D̂Ψ_C|²))^(1/2) ≤ (2𝔐^(m))^(1/2) (max(C_S, C₁^g) ℰ_g(p)^(1/2) + C_(1,ϱ) ϱ(p) + max(C_(0,0), C_(1,0)^g) η₀(p)),
there being 𝔐^(m) words of length at most m + 1, and k₁ by k₁^(m), as |B| ≤ m. Its nonlinear terms come from the words J
with |J| ≤ |B|: in each monomial the factor of largest order o ≤ |B| + 1 is H, Ψ_C or D̂Ψ_C with |C| ≤ |B|, or D̂²Ψ_C
with |C| ≤ |B| − 1, and in H^(αβ) D̂_αD̂_βΨ_J, |J| < |B|, the factor D̂²Ψ_J; each enters 𝔰_g^(m) with a weight at least
μ^((|B|+4)/2), and bounding it by 𝔰_g^(m) and the others by 𝔰 gives at most k₃^⋆ 𝔰(p) 𝔰_g^(m)(p) ≤ 𝔰_g^(m)(p)/2. So
μ^((|B|+4)/2) |D̂²Ψ_B(p)| ≤ k₁^(m) L_g + k₂ ϱ(p) + 𝔰_g^(m)(p)/2.

Taking the largest of the four bounds and absorbing 𝔰_g^(m)(p)/2 gives [[eq:tl5-hfg-linfty]]. ∎

**Lemma {#lem:tl5-hfg-products}** (The quadratic terms, graded.) In the setting of [[lem:tl5-hfg-linfty]] let I be a
word with n := |I| ≤ N, 𝔑_I := ℒ^I N(h) − H^(αβ) D̂_αD̂_βΨ_I, and 𝔑^L_I := 𝔑_I if N ≥ 5, 𝔑^L_I as in
[[lem:tl5-hfg-quadratic]] if N = 4. Put 𝔨_g := max(𝔷, 2k₁ + 2) and 𝔰_P := 𝔰_g^(m_P). Then at every point of Q(a, b)

    μ^(n/2) |𝔑^L_I| ≤ 𝔠^⋆_n (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p)),
    μ^(n/2) |ℒ^J N(h)| ≤ (𝔠^⋆_(|J|) + 1) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p))      for |J| < n.     {#eq:tl5-hfg-products}

*Proof.* For a low solution factor Φ of order o put ℓ_P(Φ) := o + 2. For any solution factor Φ let ℓ_E(Φ) be 0 for
H and h, |C| − 1 for Ψ_C with |C| ≥ 1, |C| for D̂Ψ_C and |C| + 1 for D̂²Ψ_C. For every factor Φ of a monomial of
ℒ^J N(h) − H^(αβ) D̂_αD̂_βΨ_J, |J| ≤ n, and for Φ = D̂²Ψ_J with |J| < n,

    μ^(ℓ_E(Φ)/2) |Φ| ≤ 𝔨_g 𝒥_g + 2k₂ ϱ(p).                                                               (∗)

Indeed |H| ≤ 2|h| ≤ 2𝒥_g and |h| ≤ 𝒥_g; for Ψ_C = ℒ_Z Ψ_(C′) with |C| ≥ 1, by [[eq:tl5-hf-lie]], |Ψ_C| ≤ |Z| |D̂Ψ_(C′)| +
2|D̂Z| |Ψ_(C′)| ≤ 𝔷 (|D̂Ψ_(C′)|² + |Ψ_(C′)|²)^(1/2), so μ^((|C|−1)/2) |Ψ_C| ≤ 𝔷 𝒥_g, as |C′| = |C| − 1 ≤ N;
μ^(|C|/2) |D̂Ψ_C| ≤ 𝒥_g; and D̂²Ψ_C has |C| ≤ N − 1 by [[lem:tl5-hfg-quadratic]], so μ^((|C|+1)/2) |D̂²Ψ_C| ≤ M_g,
which [[eq:tl5-hfg-m2]] with j = N − 1 bounds.

Take a monomial of 𝔑^L_I, with solution factors of orders o_i, q ≥ 2 of them; by [[lem:tl5-hfg-quadratic]] it has at
most one high factor, and at most one factor is a second derivative, as there are at most two derivatives D̂ on the
solution factors. Let Φ₂ be the high factor if there is one; otherwise a factor D̂²Ψ_C if there is one; and otherwise a
factor of largest order. Let Φ₁ be another factor, not a second derivative if there is such a choice. By
[[lem:tl5-hfg-quadratic]], o₁ + o₂ ≤ n + 2 and o₂ ≤ n + 1. If o₂ ≥ 1, ℓ_E(Φ₂) ≤ o₂ − 1; if o₂ = 0, Φ₂ is neither high
nor a second derivative, so all factors have order 0 and o₁ = 0. In both cases

    ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3,      ℓ_E(Φ₂) ≤ n.                                                      {#eq:tl5-hfg-count}

Φ₁ is low. If Φ₁ = D̂²Ψ_B, then Φ₂ is high and not a second derivative, and it is not D̂Ψ_C either, as the derivatives D̂
would then number three; so Φ₂ = Ψ_C with |C| ≥ N − 1, every other factor would offer another choice, so q = 2, and |B| +
2 + N − 1 ≤ o₁ + o₂ ≤ N + 2 gives |B| ≤ 1; with |B| ≤ N − 4, as Φ₁ is low, |B| ≤ m_P. So Φ₁ is one of the quantities of
𝔰_P, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P. With |Φ_i| ≤ 𝔰 ≤ 1 for the other factors, (∗) for Φ₂, and |Φ₁| bounded by
μ^(−ℓ_P(Φ₁)/2) 𝔰_P in the term with 𝒥_g and by 𝔰 in the term with ϱ(p), the monomial times μ^(n/2) is at most ν 𝔰^(q−2)
times

    μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔨_g 𝔰_P 𝒥_g + μ^((n − ℓ_E(Φ₂))/2) 2k₂ 𝔰 ϱ(p) ≤ μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p),

ν its background norm with the coefficient. By [[eq:tl5-hfg-sum]] this gives the first inequality. For |J| < n,
ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J, and 𝔑_J = 𝔑^L_J also for N = 4, as |J| ≤ 3; the first inequality for J, with
μ^(n/2) ≤ μ^(|J|/2), bounds μ^(n/2) |𝔑_J|. In the last term ℓ_P(H) = 2, H is a quantity of 𝔰_P, ℓ_E(D̂²Ψ_J) = |J| + 1
≤ n and 2 + |J| + 1 ≤ n + 2; the same splitting bounds μ^(n/2) |H| |D̂²Ψ_J| by μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ(p). ∎

**Lemma {#lem:tl5-hfg-mixed}** (The products of level four, graded.) Let N = 4, and let g, h, t, b, Σ, ϱ and η₀ be as
in [[lem:tl5-hf4-mixed]], with 𝔰 ≤ 𝔰₀^⋆ on Q(t, b). With the notation of that lemma, 𝔍_g := ‖𝒥_g‖_Σ and

    𝔛_t^g := max((𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2), (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t + 789 [Λ̄₂]_t),
                 (𝔭₄ 𝔵₄(t)/2)^(1/2) √602 ς_t),

    μ^(7/2) ‖𝔭_M‖_Σ ≤ 2 e^(φ(t,b)/2) 𝔪(t) 𝔛_t^g 𝔜_t (𝔍_g + ϱ) (𝔍_g + ϱ + η₀),
    𝔍_g² ≤ [𝔨₂]_t Σ_(|I|≤4) μ^|I| ∫_Σ e^(−φ) ε₁[Ψ_I] dμ dτ₂.                                          {#eq:tl5-hfg-mixed}

*Proof.* The second inequality follows from [[eq:tl5-hf-coercive]] and [[lem:tl5-hf-densities]], as in the proof of
[[lem:tl5-hf4-mixed]]. By [[eq:tl5-hfg-m2]] with j = 3 at the points of Σ, ‖M_g‖_Σ ≤ λ_t 𝔍_g + ς_t ϱ. In the proof of
[[lem:tl5-hf4-mixed]], ‖𝔭_M‖_Σ² ≤ e^(φ(t,b)) 𝔪(t)² (X₁² Y₁² + X₂² Y₂²); we bound μ² X₁, μ² X₂, μ^(3/2) Y₁ and
μ^(3/2) Y₂. The coefficients of the remainders R′ and R there belong to words J of rotations with |J| ≤ 2, so they and
the products of two of them are at most [Λ₂]_t and [Λ̄₂]_t on Σ.

*μ² X₁.* The factors of Σ_B Σ_J |ℒ^J D̂Ψ_B|² there are D̂Ψ_(JB), |JB| ≤ 4, and Ψ_C, |C| ≤ 3, and μ⁴ ≤ μ^(|JB|), μ^(|C|);
so μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2 · 49 · 1320 [Λ₂]_t² 𝒥_g², and μ² X₁ ≤ (𝔭₃ 𝔵₃(t) (1 + 64680 [Λ₂]_t²))^(1/2) 𝔍_g.

*μ² X₂.* The factors of Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² there are D̂²Ψ_(JZ), |JZ| ≤ 3, with μ² ≤ μ^((|JZ|+1)/2), and D̂Ψ_C, Ψ_C
with |C| ≤ 2; so μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 621516 [Λ̄₂]_t² 𝒥_g², and μ² X₂ ≤ (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602
‖M_g‖_Σ + 789 [Λ̄₂]_t 𝔍_g).

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* In the bounds of Y₁² and Y₂² there, μ³ Σ_(|B|=2) |D̂²Ψ_B|² ≤ 49 M_g², μ³ Σ_(|B|=2) |D̂Ψ_B|²
≤ 𝒥_g², μ³ Σ_(|B|=3) (|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², and μ³ ≤ 1 in the terms with η₀; so

    μ³ Y₁² ≤ 98π² [𝔳⁶]_t η₀² + 𝔱₃(t) (𝔍_g² + 49 ‖M_g‖_Σ²),      μ³ Y₂² ≤ 686π² [𝔳⁴]_t η₀² + 𝔱₂(t) 𝔍_g².

As there, μ² X_i ≤ 𝔛_t^g (𝔍_g + ϱ) and μ^(3/2) Y_i ≤ 𝔜_t (𝔍_g + ϱ + η₀) for i = 1, 2, and μ^(7/2) (X₁² Y₁² +
X₂² Y₂²)^(1/2) ≤ μ² X₁ μ^(3/2) Y₁ + μ² X₂ μ^(3/2) Y₂ gives the first inequality. ∎

**Definition {#def:tl5-hfg-constants}** (The sharpened constants.) Let N ≥ 5 and the setting be that of
[[def:tl5-hf-constants]], or N = 4 and the setting that of [[def:tl5-hf4-constants]], with δ_w, ϰ₀, 𝔰_θ, ϱ and η₀ as
there and 𝒮 of [[eq:tl5-hf-source]] for a = u*, b = v*. With the constants of [[lem:tl5-hfg-linfty]] and
[[lem:tl5-hfg-products]], C_P := C_∞^(m_P), C_(P,ϱ) := C_(∞,ϱ)^(m_P) and C_(P,0) := C_(∞,0)^(m_P), put

    𝔰₀^⋆ := min(𝔰_♭, 1/(2 sup_(D^κ) k₃^⋆)),      𝔰₁^⋆ := min(𝔰₀^⋆/2, c_* κ_m/2, 𝔰_θ),
    𝔤_(N,g) := (Σ_(j≤N) (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^⋆_(j′) + 1))²)^(1/2),
    𝔞_(o,g) := ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c) + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    𝔞_(i,g) := ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖ + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2),
    S_(F,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) C_P e^(φ/2)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) C_P e^(φ/2)) dt),
    𝔯_(w,g) := μ^(−3/2) (∫_(−10)^(u*) sup_(Σ₁(t,v*)) (𝔞_(o,g) (C_(P,ϱ) ϱ + C_(P,0) η₀)) dt
              + ∫_(1/2)^(v*) sup_(Σ₂(u*,t)) (𝔞_(i,g) (C_(P,ϱ) ϱ + C_(P,0) η₀)) dt),
    ε_(w,g) := 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ],

the functions of p being evaluated at the point of the supremum. For N = 4 put, with the notation of
[[lem:tl5-hf4-mixed]] and [[lem:tl5-hfg-mixed]] and with [𝔠^⋆₄]_t the number 𝔠^⋆₄ formed with the suprema over
Σ₁(t, v*) of the Λ_k and the λ_k,

    m_t^g := 98 e^(φ(t,v*)/2) [2Ω̂² (1 + c/κ′)^(1/2)]_t [𝔠^⋆₄]_t 𝔪(t) 𝔛_t^g 𝔜_t,
    S_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t^g [𝔨₂]_t dt,
    𝔯_(M,g) := μ^(−3/2) ∫_(−10)^(u*) m_t^g [𝔨₂]_t^(1/2) (2ϱ + η₀) dt,
    ε_(M,g) := μ^(−3/2) ϱ (ϱ + η₀) ∫_(−10)^(u*) m_t^g dt,

the graded triple, or let S_(M,g), 𝔯_(M,g) and ε_(M,g) be S_M, 𝔯_M and ε_M of [[def:tl5-hf4-constants]] with m_t^g in
place of m_t, the ungraded triple, the same triple throughout; for N ≥ 5 let S_(M,g) = 𝔯_(M,g) = ε_(M,g) := 0. Finally

    A_g := √2 δ_w + 2ε_(w,g) + 2ε_(M,g),      B_g := 2 (S_(F,g) + S_(M,g)),      𝔯_g := 𝔯_(w,g) + 𝔯_(M,g),
    𝔰_(*,g) := sup_(p∈D^κ) (2 C_∞^(N−4)(p) μ^(−N/2) e^(φ(p)/2) A_g
               + C_(∞,ϱ)^(N−4)(p) ϱ(p) + C_(∞,0)^(N−4)(p) η₀).                                    {#eq:tl5-hfg-constants}

**Proposition {#prop:tl5-hfg-bootstrap}** (The a priori estimate with the sharpened constants.) In the setting of
[[def:tl5-hfg-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N) and that

    𝔯_g ≤ 1/4,      η₀ < 𝔰₁^⋆,      𝔰_(*,g) < 𝔰₁^⋆.                                               {#eq:tl5-hfg-smallness}

Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_g for every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,g) on
D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_g + B_g Y_s(g)².                                                                          {#eq:tl5-hfg-h1}

*Proof.* *Step 1.* As in Step 1 of the proof of [[prop:tl5-hf-bootstrap]], with 𝔰₀^⋆, 𝔰₁^⋆ and A_g in place of 𝔰₀,
𝔰₁ and A_w, and with [[eq:tl5-hfg-linfty]] for m = N − 4 and μ = 1 in place of [[eq:tl5-hf-linfty]]: if 𝔰 ≤ 𝔰₀^⋆ on
D^κ_σ and p ∈ D^κ_σ, then ℰ⁰_N(p) ≤ μ^(−N) e^(φ(p)) Y_σ(g)² ≤ 4μ^(−N) e^(φ(p)) A_g², so 𝔰(p) ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤
𝔰₀^⋆/2. That argument gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ on D^κ_s, |h|_k̂ < κ_m/2 by [[lem:tl5-hf-conversions]] (a), and
θ_H ≤ ϑ. So [[lem:tl5-hfg-quadratic]], [[lem:tl5-hfg-linfty]] and [[lem:tl5-hfg-products]] apply at every point of
D^κ_s, and their ϱ(p) and η₀(p) are at most the ϱ and η₀ of [[def:tl5-hfg-constants]].

*Step 2.* Step 2 of the proof of [[prop:tl5-hf-bootstrap]] (for N = 4, of the proof of [[prop:tl5-hf4-bootstrap]])
holds up to the bound of the nonlinear terms, which we replace as follows. The nonlinear terms of L̂Ψ_I +
H^(αβ) D̂_αD̂_βΨ_I other than 𝔑^M_I are −Σ_(J≠I) 𝔔_IJ ℒ^J N(h) − 𝔑^L_I, and 𝔔_IJ ≠ 0 with J ≠ I only for |J| < |I|. By
[[eq:tl5-hfg-products]], by the definition of 𝔮_(jj′) and the Cauchy–Schwarz inequality over the 7^(j′) words of each
length j′ ≤ |I| ([[def:tl5-hf-coupling]]), the family of these terms over |I| = j has norm at most

    μ^(−j/2) Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^⋆_(j′) + 1) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g + 2k₂ 𝔰 ϱ),

with 𝔮_(jj) = 1. As for the forcing terms in the proof of [[prop:tl5-hf-linear-n]], with the weights μ^|I| and the
Cauchy–Schwarz inequality over j, their contribution to the bulk is at most 2Ω̂² 𝔤_(N,g) (μ^(−3/2) 𝔨_g 𝔰_P 𝒥_g +
2k₂ 𝔰 ϱ)(√e_o + √c √e_i), e_o and e_i being the weighted sums. By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ (1/z̲ + 1/c) e_o +
e_i, so, with √e_o + √c √e_i ≤ √2 (e_o + e_i)^(1/2), 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 2Ω̂ (1 + 1/z̲ + 1/c)^(1/2) (e_o + e_i);
and 2k₂ 𝔰 ϱ ≤ (1/4) k₂ ϱ, as 𝔰 ≤ 1/8. By (a) of [[lem:tl5-hf-quasilinear]], with |D̂H| = |g⁻¹ (D̂h) g⁻¹| ≤ 𝔤₀² |D̂h| ≤
𝔤₀² μ^(−3/2) 𝔰_P, |H| ≤ μ^(−1) 𝔰_P ≤ μ^(−3/2) 𝔰_P and |D̂Ψ|² ≤ (e_o/c + e_i)/(2Ω̂²) for each field, the weighted sum of
2Ω̂² |𝔮_H| is at most μ^(−3/2) 𝔰_P times the first two terms of 𝔞_(o,g) e_o + 𝔞_(i,g) e_i. For N = 4 the terms 𝔑^M_I
are bounded as in the proof of [[prop:tl5-hf4-bootstrap]], with [[eq:tl5-hf4-g]] for 𝔠^⋆₄ and [[lem:tl5-hfg-mixed]] in
place of [[lem:tl5-hf4-mixed]]: the factors there become 49 [𝔠^⋆₄]_t ‖𝔭_M‖_Σ and at most μ^(−2) Y_s, and 𝔍_g ≤
[𝔨₂]_t^(1/2) Y_s, so the term is at most ∫_(−10)^(u*) m_t^g μ^(−3/2) (𝔍_g + ϱ)(𝔍_g + ϱ + η₀) Y_s dt ≤ S_(M,g) Y_s³ +
𝔯_(M,g) Y_s² + ε_(M,g) Y_s for the graded triple. For the ungraded triple, [[lem:tl5-hfg-mixed]] with μ = 1, where
𝔍_g = 𝔍, gives the first inequality of [[eq:tl5-hf4-mixed]] with 𝔛_t^g in place of 𝔛_t, and the argument of the
proof of [[prop:tl5-hf4-bootstrap]], with [𝔠^⋆₄]_t in place of [𝔠₄]_t, bounds the term by S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² +
ε_(M,g) Y_s. Hence the bulk of the weighted sum over I is at most

    ∫ e^(−φ) (2Ω̂² (s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ)(√e_o + √c √e_i) + μ^(−3/2) 𝔰_P (𝔞_(o,g) e_o + 𝔞_(i,g) e_i)) dμ du dv

plus, for N = 4, S_(M,g) Y_s³ + 𝔯_(M,g) Y_s² + ε_(M,g) Y_s.

*Step 3.* Step 3 of that proof applies with μ^(−3/2) 𝔰_P in place of 𝔰: by [[eq:tl5-hfg-linfty]] for m = m_P, as
ℰ_g(p) ≤ e^(φ(p)) Y_s², φ being at most φ(p) on Σ₁(τ₁(p), τ₂(p)), 𝔰_P ≤ C_P e^(φ/2) Y_s + C_(P,ϱ) ϱ + C_(P,0) η₀ at
every point; so for every a′ ≤ u*, b′ ≤ s

    (1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,g) + ε_(M,g)) + 𝔯_g Y_s² + (S_(F,g) + S_(M,g)) Y_s³,

and with ϑ ≤ 1/4 and 𝔯_g ≤ 1/4 the conclusion follows as there. ∎

**Theorem {#thm:tl5-hfg}** (Existence close to an explicit background, with the sharpened constants.) In the setting
of [[thm:tl5-hf]] (N ≥ 6) let the bounds Λ_k, Λ^R_k, λ_k, the number 𝔰_♭ and the choice of 𝔠^⋆ be as in
[[def:tl5-hfg-graded]], and suppose:

(a) the quantity η₀ of [[def:tl5-hf-constants]] satisfies η₀ < 𝔰₁^⋆;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅_N, E_o^N, E_i^N);

(c) the constants of [[def:tl5-hfg-constants]] satisfy 𝔯_(w,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁^⋆ and the closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g)) S_(F,g) < 1.                                                  {#eq:tl5-hfg-closing}

Then the conclusions of [[thm:tl5-hf]] hold with A_g and 𝔰_(*,g) in place of A_w and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]], [[eq:tl5-hfg-h1]] and
[[eq:tl5-hfg-closing]] in place of A_w, B_w, [[prop:tl5-hf-bootstrap]], [[eq:tl5-hf-h1]] and [[eq:tl5-hf-closing]].
For (H2), the proof of [[lem:tl5-hf-persistence]] uses [[prop:tl5-hf-bootstrap]] only through its conclusion 𝔰 ≤ 𝔰_*
on D^κ_s, which gives |H| ≤ 1/8 and θ_H ≤ ϑ, and through the bound Y_σ ≤ 2A_w; [[prop:tl5-hfg-bootstrap]] gives
𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤ min(1/16, 𝔰_θ) under Y_σ ≤ 2A_g, so that proof gives (H2) with A_g in place of A_w. The bound
for ε is [[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_(*,g). ∎

**Theorem {#thm:tl5-hf4g}** (Level four, with the sharpened constants.) In the setting of [[thm:tl5-hf4]] let the
bounds Λ_k, Λ^R_k, λ_k, the number 𝔰_♭ and the choice of 𝔠^⋆ be as in [[def:tl5-hfg-graded]] with N = 4, and suppose:

(a) the quantity η₀ of [[def:tl5-hf4-constants]] satisfies η₀ < 𝔰₁^⋆;

(b) a_o, a_i are admissible rates for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴);

(c) the constants of [[def:tl5-hfg-constants]] with N = 4 satisfy 𝔯_(w,g) + 𝔯_(M,g) ≤ 1/4, 𝔰_(*,g) < 𝔰₁^⋆ and the
closing condition

    4 A_g B_g = 8 (√2 δ_w + 2ε_(w,g) + 2ε_(M,g)) (S_(F,g) + S_(M,g)) < 1.                          {#eq:tl5-hf4g-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_g and 𝔰_(*,g) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4]] applies with A_g, B_g, [[prop:tl5-hfg-bootstrap]] for N = 4,
[[eq:tl5-hfg-h1]] and [[eq:tl5-hf4g-closing]] in place of A_(w,4), B_(w,4), [[prop:tl5-hf4-bootstrap]],
[[eq:tl5-hf4-h1]] and [[eq:tl5-hf4-closing]]. For (H2), the proof of [[lem:tl5-hf4-persistence]] uses
[[prop:tl5-hf4-bootstrap]] only through its conclusion 𝔰 ≤ 𝔰_* on D^κ_s, which gives |H| ≤ 1/8 and θ_H ≤ ϑ, through
the bound Y_σ ≤ 2A_(w,4) and through [[eq:tl5-hf4-m2]], which holds by [[eq:tl5-hfg-m2]] with μ = 1 and j = 3;
[[prop:tl5-hfg-bootstrap]] gives 𝔰 ≤ 𝔰_(*,g) < 𝔰₁^⋆ ≤ min(1/16, 𝔰_θ) under Y_σ ≤ 2A_g. The bound for ε is
[[eq:tl5-hf-eps]] with 𝔰 ≤ 𝔰_(*,g). ∎

**Remark {#rem:tl5-hfg-powers}** (What the sharpened constants contain.) In S_(F,g) and 𝔯_(w,g), and with the graded
triple in S_(M,g), 𝔯_(M,g) and ε_(M,g), the only power of μ is μ^(−3/2), at every level N ≥ 4, against μ^(−N) in S_F
and μ^(−2) in S_M of [[thm:tl5-hf]] and [[thm:tl5-hf4]]:
𝔤_(N,g), 𝔨_g, 𝔞_(o,g), 𝔞_(i,g), C_P, C_(P,ϱ), C_(P,0) and m_t^g do not depend on μ. The power is that of the count
[[eq:tl5-hfg-count]], which gives exactly n + 3 for the term D̂Ψ_B · D̂Ψ_(B′) of 2𝔮 with |B| + |B′| = n and |B| ≤ N − 3:
D̂Ψ_B is bounded at a point through the energies of level |B| + 3, and D̂Ψ_(B′) through those of level |B′|. The
smallness 𝔰_(*,g) < 𝔰₁^⋆ keeps the factor μ^(−N/2), as the recovery of second derivatives absorbs the ungraded 𝔰.

The recovery constant of the highest level, k₁ = k₁^(N−1), enters S_(F,g) through 𝔨_g and through C₁^g in C_P; in C_P
it is otherwise replaced by k₁^(m_P), which involves the couplings 𝔄_CJ with |C| ≤ 1 only, and for N = 4 none, as
𝔄_∅J = 0 by [[def:tl5-hf-coupling]]; and 𝔐^(m_P) = 57 for N ≥ 5 and 8 for N = 4, against 𝔐 = Σ_(j≤N−3) 7^j. The
smallness constants C_∞^(N−4), C_(∞,ϱ)^(N−4) and C_(∞,0)^(N−4) contain k₁^(N−4) in place of the third k₁ of C_∞. The
background bounds enter graded: 𝔠^⋆_n through Λ_k, Λ^R_k and λ_k with k ≤ n, C₁^g, C_(1,0)^g and 𝔛_t^g through Λ₂ only.
If π^Z = 0 for every Z ∈ Γ, as for the seed, then ℒ^K ĝ⁻¹ = 0 and ℒ^K R̂ = 0 for K ≠ ∅, the choices Λ_k = λ_k = 0 for
k ≥ 1, Λ^R_0 = |R̂| and Λ^R_k = 0 for k ≥ 1 are admissible, and

    𝔠^Q_n = (81 + 5|R̂|) 2^n − 1,

the number of distributions of n letters over the two solution factors of each quadratic term, 2^n, times the norms of
its coefficients.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The sections sec:tl5-hf (level six) and sec:tl5-hf4 (level four) stay as they are, and their closing conditions remain
valid: the sharpened constants are added beside them, not in their place, because the new constants interlock (the
choice of expansion, 𝔰_♭, 𝔰₀^⋆ and 𝔰₁^⋆ enter hypothesis (a) as well as (c)), and a rewrite of the merged lemmas would
change numbered statements that other text cites. Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD
1fb4b941, unchanged since the merge 8ceedd0e of the level-4 section; the level-6 parts are those of sec:tl5-hf and the
level-4 parts those of sec:tl5-hf4 as merged (with the symbols 𝔛_t, 𝔜_t). Line numbers serve only to find the place.
Each new text replaces its old text as a whole, with the line breaks shown.

*1. Where the section goes.* The section above, from its heading ("The sharpened constants", label sec:tl5-hfg) through
the last line of [[rem:tl5-hfg-powers]], is inserted at the end of [[ch:ten-l5]], after the last line of
[[rem:tl5-hf4-level]] (line 5006, "at 10 l5."), with one blank line before it. It is a sibling of sec:tl5-hf and
sec:tl5-hf4 (a "###" heading) and comes after both. It cites results of sec:tl5-hf and sec:tl5-hf4 as they stand,
and the proofs of prop:tl5-hf-bootstrap, prop:tl5-hf4-bootstrap, lem:tl5-hf-persistence, lem:tl5-hf4-persistence,
thm:tl5-hf and thm:tl5-hf4 with the replacements it states. It defines the labels listed in the crosswalk rows, none
defined elsewhere. No number already printed changes.

*2. The end of the paragraph after [[thm:tl5-hf]] (lines 4594–4596).* Old:

those of [[thm:tl5-dn]], are conditions on the background of the same kind. The derivatives of G^♯ − ĝ on N₀ transverse
to N₀ need not vanish, so η₀ and the terms on N₀ in δ_w are small only for a background whose transverse derivatives on
N₀ of order at most N are close to those of G^♯.

New:

those of [[thm:tl5-dn]], are conditions on the background of the same kind. The derivatives of G^♯ − ĝ on N₀ transverse
to N₀ need not vanish, so η₀ and the terms on N₀ in δ_w are small only for a background whose transverse derivatives on
N₀ of order at most N are close to those of G^♯. [[thm:tl5-hfg]] gives the conclusions of [[thm:tl5-hf]] under
sharpened constants, with graded background bounds and the factor μ^(−3/2) in place of μ^(−N) ([[sec:tl5-hfg]]).

*3. The fifth sentence of [[rem:tl5-hf4-level]] (lines 4992–4994).* Old:

explicit in the jets of ĝ of order at most N + 3 = 7, against 9 at N = 6; they involve the Σ_(j≤4) 7^j = 2801 words of
length at most 4, against 137,257 at N = 6, the derivatives of R̂ic along Γ of order at most 4, against 6, and the
factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2). On N₀ they involve the derivatives of

New:

explicit in the jets of ĝ of order at most N + 3 = 7, against 9 at N = 6; they involve the Σ_(j≤4) 7^j = 2801 words of
length at most 4, against 137,257 at N = 6, the derivatives of R̂ic along Γ of order at most 4, against 6, and the
factor μ^(−N) = μ^(−4) of S_F, against μ^(−6), while S_M carries μ^(−2); with the sharpened constants of
[[thm:tl5-hf4g]] both carry μ^(−3/2) ([[rem:tl5-hfg-powers]]). On N₀ they involve the derivatives of

*4. Nothing else changes.* No other text of the chapters changes. The opening paragraph of sec:tl5-hf,
rem:tl5-beyond and lem:tl5-continuation need no change: [[thm:tl5-hfg]] and [[thm:tl5-hf4g]] give (H1), (H2) and
(H4) of [[lem:tl5-continuation]] and reduce (H3) to [[eq:tl5-hfg-closing]] and [[eq:tl5-hf4g-closing]], as
[[thm:tl5-hf]] and [[thm:tl5-hf4]] do.

### Comparison and the factors for the evaluation

Not chapter text. "Proved" refers to the section above; "deduced" marks statements about the method that no proof in
the file establishes; "computed" marks numbers I evaluated (floating point).

*The closing conditions (proved).*

    level 6 as merged:  8 (√2 δ_w + 2ε_w) S_F < 1                              (thm:tl5-hf, eq:tl5-hf-closing)
    level 6 sharpened:  8 (√2 δ_w + 2ε_(w,g)) S_(F,g) < 1                      (thm:tl5-hfg, eq:tl5-hfg-closing)
    level 4 as merged:  8 (√2 δ_w + 2ε_w + 2ε_M) (S_F + S_M) < 1               (thm:tl5-hf4, eq:tl5-hf4-closing)
    level 4 sharpened:  8 (√2 δ_w + 2ε_(w,g) + 2ε_(M,g)) (S_(F,g) + S_(M,g)) < 1   (thm:tl5-hf4g, eq:tl5-hf4g-closing)

with, beside each sharpened one, 𝔯_(w,g) (+ 𝔯_(M,g) at level 4) ≤ 1/4, η₀ < 𝔰₁^⋆ and 𝔰_(*,g) < 𝔰₁^⋆. The merged
conditions stay valid; either set may be used. δ_w is unchanged.

*Leading μ-powers (proved).* S_(F,g): μ^(−3/2) at both levels (against μ^(−6) at level 6 and μ^(−4) at level 4).
S_(M,g), 𝔯_(M,g), ε_(M,g) with the graded triple: μ^(−3/2) each (against μ^(−2), μ⁰, μ² in the merged level 4); the
ungraded triple keeps μ^(−2), μ⁰, μ² with the sharpened m_t^g, and either triple may be used. 𝔯_(w,g): μ^(−3/2)
(against μ^(−N/2) through 𝔞_o, 𝔞_i). 𝔰_(*,g): μ^(−N/2), unchanged, as the recovery absorbs the ungraded 𝔰. The weights
μ^j inside 𝔤_N are absorbed: 𝔤_(N,g) has none.

*Every factor, as a formula.* At a point, for words in Γ:

    Λ₀ = 0;  Λ_k (1 ≤ k ≤ N) ≥ |ℒ^B π^Z|, |ℒ^B Γ′[π^Z]|, |ℒ^B D̂Γ′[π^Z]|, |D̂ℒ^B Γ′[π^Z]| for |B| ≤ k − 1, nondecreasing;
    Λ^R_k ≥ |ℒ^B R̂| for |B| = k;  λ_k ≥ |ℒ^K ĝ⁻¹| for |K| = k (k ≥ 1), admissible λ_k = Σ_r r! S(k,r) 5^((r+1)/2) Λ_k^r;
    λ₀ = 1, λ̂₀ = √5, λ̂_k = λ_k;  Λ̄_k = max(Λ_k, Λ_k²);  𝔤₀ = √5 + 1/4;  F_k ordered Bell numbers (1, 1, 3, 13, 75,
    541, 4683);  Σ^m_n f = Σ over k ∈ ℕ^m, Σk_i = n, of n!/(k₁!⋯k_m!) f(k);

    β₁^g(k) = 1 + (2^(k+1) − 2) Λ_k,  β₂^g(k) = 1 + (7/3)(4^k − 1) Λ̄_k  (both 1 at k = 0);
    b_g^g(k) = F_k 𝔤₀^(k+1) (Λ_k + 1)^k (𝔤₀ at k = 0),  b_H^g(k) = (2k + 1) b_g^g(k) (1 at k = 0);
    𝔠^g_n = Σ²_n b_H^g(k₁)β₂^g(k₂) − 1 + 5Σ³_n b_H^g(k₁)Λ^R_(k₂) + 16Σ⁴_n b_g^g(k₁)b_g^g(k₂)β₁^g(k₃)β₁^g(k₄);
    𝔠^Q_n = Σ⁴_n λ_(k₁)λ_(k₃)β₂^g(k₄) − 1 + 5Σ⁵_n λ_(k₁)λ_(k₃)Λ^R_(k₄) + 16Σ⁴_n λ̂_(k₁)λ̂_(k₂)β₁^g(k₃)β₁^g(k₄);
    𝔠^(3)_n = Σ⁶_n b_g^g(k₁)λ_(k₃)λ_(k₅)β₂^g(k₆) − 𝔤₀ + 5Σ⁷_n b_g^g(k₁)λ_(k₃)λ_(k₅)Λ^R_(k₆)
              + 16Σ⁶_n b_g^g(k₁)λ_(k₃)(b_g^g(k₄) + λ̂_(k₄))β₁^g(k₅)β₁^g(k₆);
    𝔠^⋆_n = 𝔠^g_n (with 𝔰_♭ ≤ 1/8), or 𝔠^⋆_n = 𝔠^Q_n + 𝔰_♭ 𝔠^(3)_n (with a chosen 𝔰_♭ ∈ (0, 1/8]), one choice throughout;

    α_𝔄^(j) = √2 max_(|C|≤j) Σ_J ‖𝔄_CJ‖;  k₁^(j) = (6/5)((√3 + 8/3)K_rec(1 + √7(3 max|D̂Z| + 2 max|D̂²Z|)) + 𝔯₀
              + (4/3)α_𝔄^(j));  k₁ = k₁^(N−1);  k₁^(0) has α_𝔄^(0) = 0;
    k₂ = (8/5) q₁;  k₃^⋆ = (8/5) max_(|C|≤N−1) (𝔠^⋆_(|C|) + Σ_(J≠C) ‖𝔔_CJ‖ (𝔠^⋆_(|J|) + 1))  (𝔠^⋆_n for n ≤ N − 1);
    𝔰₀^⋆ = min(𝔰_♭, 1/(2 sup k₃^⋆));  𝔰₁^⋆ = min(𝔰₀^⋆/2, c_* κ_m/2, 𝔰_θ);

    C₁^g² = 258 C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + 6Λ₂)² + 4|∂_γ|² (72Λ₂² + 8(k₁ + 1)²));
    C_(1,0)^g² = 516π² C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ₂)²;  C_S, C_(0,0), C_(1,ϱ) as in lem:tl5-hf-linfty;
    𝔐^(m) = Σ_(j≤m+1) 7^j;  m_P = min(1, N − 4)  (𝔐^(m_P) = 57 for N ≥ 5, 8 for N = 4; 𝔐^(N−4) = 𝔐);
    C_∞^(m) = 2 max(2C_S, C₁^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_S, C₁^g));
    C_(∞,ϱ)^(m) = 2 max(C_(1,ϱ), k₁^(m) (2𝔐^(m))^(1/2) C_(1,ϱ) + k₂);
    C_(∞,0)^(m) = 2 max(2C_(0,0), C_(1,0)^g, k₁^(m) (2𝔐^(m))^(1/2) max(C_(0,0), C_(1,0)^g));
    C_P = C_∞^(m_P) (in S_(F,g)),  C_(P,ϱ), C_(P,0) likewise (in 𝔯_(w,g));  C_∞^(N−4) etc. (in 𝔰_(*,g));

    𝔷 = max_Z (|Z|² + 4|D̂Z|²)^(1/2);  𝔨_g = max(𝔷, 2k₁ + 2);
    𝔤_(N,g) = (Σ_(j≤N) (Σ_(j′≤j) 𝔮_(jj′) 7^(j′/2) (𝔠^⋆_(j′) + 1))²)^(1/2);
    𝔞_(o,g) = ϰ₀/c + (1/2)|T| ‖𝒞_(·0)‖ (1/z̲ + 1/c) + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2);
    𝔞_(i,g) = ϰ₀ + (1/2)|T| ‖𝒞_(·0)‖ + 2Ω̂ 𝔤_(N,g) 𝔨_g (1 + 1/z̲ + 1/c)^(1/2);
    S_(F,g) = μ^(−3/2) (∫ sup_(Σ₁(t,v*)) 𝔞_(o,g) C_P e^(φ/2) dt + ∫ sup_(Σ₂(u*,t)) 𝔞_(i,g) C_P e^(φ/2) dt);
    𝔯_(w,g) = μ^(−3/2) (the same with C_(P,ϱ) ϱ + C_(P,0) η₀ in place of C_P e^(φ/2));
    ε_(w,g) = 𝒮[s_N[2R̂ic] + (1/4) 𝔤_(N,g) k₂ ϱ];
    𝔰_(*,g) = sup_p (2C_∞^(N−4) μ^(−N/2) e^(φ/2) A_g + C_(∞,ϱ)^(N−4) ϱ + C_(∞,0)^(N−4) η₀);
    level 4:  𝔛_t^g = max((𝔭₃ 𝔵₃(t)(1 + 64680[Λ₂]_t²))^(1/2), (𝔭₄𝔵₄(t)/2)^(1/2)(√602 λ_t + 789[Λ̄₂]_t),
              (𝔭₄𝔵₄(t)/2)^(1/2) √602 ς_t),  λ_t = 2([k₁]_t + 1),  𝔜_t as merged;
              m_t^g = 98 e^(φ(t,v*)/2) [2Ω̂²(1 + c/κ′)^(1/2)]_t [𝔠^⋆₄]_t 𝔪(t) 𝔛_t^g 𝔜_t;
              graded triple S_(M,g) = μ^(−3/2) ∫ m_t^g [𝔨₂]_t dt, 𝔯_(M,g) = μ^(−3/2) ∫ m_t^g [𝔨₂]_t^(1/2)(2ϱ + η₀) dt,
              ε_(M,g) = μ^(−3/2) ϱ(ϱ + η₀) ∫ m_t^g dt.

Here [f]_t is the supremum over the face Σ₁(t, v*), also in [𝔳⁴]_t and [𝔳⁶]_t of 𝔜_t (they are face suprema, not leaf
suprema), and [𝔠^⋆₄]_t is 𝔠^⋆₄ with the face suprema of the Λ_k, Λ^R_k and λ_k.

*The three levers, item by item.*

1. Graded background bounds (proved). Each background factor carrying k letters is bounded by Λ_k (Λ^R_k for R̂,
   λ_k for ℒ^K ĝ⁻¹); in the convention of the G0c variant ("Λ_(k−1) for a factor with k letters") the objects are the
   same and only the index differs. Graded in 𝔠^g_n (so in 𝔤_(N,g), k₃^⋆, 𝔰₀^⋆, 𝔰₁^⋆ and [𝔠^⋆₄]_t), in C₁^g and
   C_(1,0)^g (Λ₂: the Sobolev step uses two rotations only), and in 𝔛_t^g (Λ₂). k₁ is graded by level: the recovery of
   D̂²Ψ_C uses k₁^(|C|); C_∞^(m) uses k₁^(m). Computed check: at Λ_k = Λ^R_k = 1 the graded 𝔠^g_n equals 𝔠_n at Λ = 1
   (104, 1.82e3, 4.14e4, 1.22e6, 4.44e7, 1.93e9, 9.75e10 for n = 0…6), so the gain is entirely in Λ_k against Λ.
2. Level-matched μ (proved, as in the earlier draft): μ^(−3/2) for every quadratic term at every level, by the count
   ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n + 3 (eq:tl5-hfg-count), sharp for D̂Ψ_B · D̂Ψ_(B′).
3. The sharper chain.
   (a) k₁ (proved in part). The factor at a point is never a second derivative of a word of length two or more
   (lem:tl5-hfg-products), so S_(F,g) uses C_P with k₁^(m_P) (couplings of words of length ≤ 1; none at level 4) and
   𝔐^(m_P) in place of the third k₁ and 𝔐 of C_∞. The top-level k₁ still enters S_(F,g) twice: in 𝔨_g (the high
   factor D̂²Ψ_C, |C| ≤ N − 1) and in C₁^g (the ∂_γ-derivative of D̂Ψ_(JB) on the face, |JB| ≤ N − 1). What remains
   (deduced): in C₁^g only the component D̂²Ψ(E₁, E₁) needs the equation, the other components being recovered from
   the fields Γ alone; it enters D̂_(∂_γ)D̂Ψ with the coefficient (c + κ′)Ω̂/√c, comparable to |∂_γ|, so splitting it
   off would not remove k₁ from C₁. The k₁ of 𝔨_g is the recovery at level N − 1 and is needed by this way of bounding.
   (b) C₁ against C_S (not sharpened beyond Λ → Λ₂). What remains (deduced): 𝔳⁶ 𝔴⁶ and 𝔭₃ come from passing to the
   Euclidean components on 𝒱 in the Sobolev lemma; a component-free inequality on the leaves (Kato-type, |K|A|| ≤
   |ℒ_K A|) would remove them but needs the rotations to act isometrically on the norm |·|, which holds for round
   leaves only; the factor 258 = 6 · 43 counts the 43 rotation words each against the whole 𝒥₁.
   (c) The nonlinear constant (proved). 𝔠^Q_n expands the exact quadratic part of N(h) with its own coefficient
   tensors, Leibniz over its factors (no ordered Bell numbers, no 𝔤₀ powers), and puts the cubic remainder behind the
   factor 𝔰_♭. Computed at all bounds equal to 1: 𝔠^Q_n = 85, 587, 3.74e3, 2.27e4, 1.35e5, 7.87e5, 4.58e6 (n = 0…6)
   against 𝔠_n above (4.3 decades at n = 6); 𝔠^(3)_n = 200 … 1.21e11, entering with 𝔰_♭. For the seed (π^Z = 0),
   𝔠^Q_n = (81 + 5|R̂|) 2^n − 1 exactly, that is (81 + 5|R̂|)/9 times G0's c_NL = 9 · 2^N at n = N (computed check:
   85, 171, …, 5503 at |R̂| = 1). What remains in 𝔤_(N,g) against c_NL (deduced): the word count 7^(j′/2) (an ℓ² count
   over words would remove it, as the distribution of letters is a bijection between words and tuples of subwords, but
   needs ℓ² versions of the bounds at a point and of the recovery, with the ℓ² operator norm of the coupling family in
   place of the row sums of α_𝔄); the cross-level 𝔔-couplings 𝔮_(jj′), which G0's count does not have; and the
   coefficient normalisation 81 + 5|R̂| against 9 (the 16 units of 2𝔮 count √5 for each inverse metric that may be a
   trace; a monomial-by-monomial count would lower the 80).
   (d) (2𝔐)^(1/2) (proved for S_(F,g)): √114 ≈ 10.7 for N ≥ 5 (√800 ≈ 28.3 at N = 6 before), √16 = 4 at level 4
   (unchanged). The smallness constants keep 𝔐. What remains (deduced): an ℓ² count at the point gives √3 for the
   undifferentiated part, each word arising as JC in at most three ways.

*Notes for the evaluation.* (i) Whichever 𝔠^⋆ is chosen, it enters k₃^⋆ only through n ≤ N − 1 and 𝔤_(N,g) through
n ≤ N; at level 4 [𝔠^⋆₄]_t enters m_t^g. (ii) The second expansion requires 𝔰 ≤ 𝔰_♭, so 𝔰₁^⋆ ≤ 𝔰_♭/2 and η₀ < 𝔰₁^⋆:
𝔰_♭ trades the size of the cubic term against the smallness targets. (iii) C₁^g still contains the top-level k₁,
which G0c's variant did not grade; the level-graded k₁ enters only C_∞^(m) and the recovery of each level.
(iv) The merged conditions remain the fallback and are unchanged by this file.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfg	paper/reader/proofs/P-GRD.md@PENDING:1	P-GRD, section	new; at the end of ch:ten-l5, after rem:tl5-hf4-level, beside sec:tl5-hf and sec:tl5-hf4 (author: sharpen the constants); graded background bounds, level-matched mu, sharper chain
    def:tl5-hfg-graded	paper/reader/proofs/P-GRD.md@PENDING:18	P-GRD, Definition	graded bounds Lambda_k, Lambda^R_k, lambda_k; nonlinear constants c^g_n, c^Q_n, c^(3)_n, choice c*_n and s_flat; weighted quantities J_g, M_g^(j), s_g^(m), E_g
    eq:tl5-hfg-cn	paper/reader/proofs/P-GRD.md@PENDING:35	P-GRD, display	new
    lem:tl5-hfg-quadratic	paper/reader/proofs/P-GRD.md@PENDING:61	P-GRD, Lemma	Lemma G with graded background bounds (first expansion) and with the exact quadratic part plus a cubic remainder behind s_flat (second expansion)
    eq:tl5-hfg-sum	paper/reader/proofs/P-GRD.md@PENDING:66	P-GRD, display	new
    lem:tl5-hfg-linfty	paper/reader/proofs/P-GRD.md@PENDING:122	P-GRD, Lemma	lem:tl5-hf-linfty weighted by level, k1 graded by level k1^(j), Lambda_2 in C1, C_inf^(m) for the low second derivatives up to level m
    eq:tl5-hfg-cinf	paper/reader/proofs/P-GRD.md@PENDING:131	P-GRD, display	new
    eq:tl5-hfg-m2	paper/reader/proofs/P-GRD.md@PENDING:139	P-GRD, display	new
    eq:tl5-hfg-linfty	paper/reader/proofs/P-GRD.md@PENDING:143	P-GRD, display	new
    lem:tl5-hfg-products	paper/reader/proofs/P-GRD.md@PENDING:187	P-GRD, Lemma	the graded count: two levels add to at most n + 3, so mu^(-3/2); factor at a point never D^2 Psi_B with |B| >= 2
    eq:tl5-hfg-products	paper/reader/proofs/P-GRD.md@PENDING:192	P-GRD, display	new
    eq:tl5-hfg-count	paper/reader/proofs/P-GRD.md@PENDING:212	P-GRD, display	new
    lem:tl5-hfg-mixed	paper/reader/proofs/P-GRD.md@PENDING:228	P-GRD, Lemma	lem:tl5-hf4-mixed weighted, with Lambda_2
    eq:tl5-hfg-mixed	paper/reader/proofs/P-GRD.md@PENDING:235	P-GRD, display	new
    def:tl5-hfg-constants	paper/reader/proofs/P-GRD.md@PENDING:258	P-GRD, Definition	sharpened constants at levels 6 and 4: s0*, s1*, g_(N,g), a_(o,g), a_(i,g), S_(F,g), r_(w,g), eps_(w,g), m_t^g and the two level-4 triples, A_g, B_g, s_(*,g)
    eq:tl5-hfg-constants	paper/reader/proofs/P-GRD.md@PENDING:287	P-GRD, display	new
    prop:tl5-hfg-bootstrap	paper/reader/proofs/P-GRD.md@PENDING:289	P-GRD, Proposition	(H1) with the sharpened constants, levels N >= 4
    eq:tl5-hfg-smallness	paper/reader/proofs/P-GRD.md@PENDING:292	P-GRD, display	new
    eq:tl5-hfg-h1	paper/reader/proofs/P-GRD.md@PENDING:297	P-GRD, display	new
    thm:tl5-hfg	paper/reader/proofs/P-GRD.md@PENDING:341	P-GRD, Theorem	thm:tl5-hf (N >= 6) with the sharpened constants; (a) eta0 < s1*
    eq:tl5-hfg-closing	paper/reader/proofs/P-GRD.md@PENDING:351	P-GRD, display	closing condition at level N >= 6: 8 (sqrt2 delta_w + 2 eps_(w,g)) S_(F,g) < 1
    thm:tl5-hf4g	paper/reader/proofs/P-GRD.md@PENDING:362	P-GRD, Theorem	thm:tl5-hf4 with the sharpened constants; (a) eta0 < s1*
    eq:tl5-hf4g-closing	paper/reader/proofs/P-GRD.md@PENDING:372	P-GRD, display	closing condition at level 4: 8 (sqrt2 delta_w + 2 eps_(w,g) + 2 eps_(M,g)) (S_(F,g) + S_(M,g)) < 1
    rem:tl5-hfg-powers	paper/reader/proofs/P-GRD.md@PENDING:384	P-GRD, Remark	mu^(-3/2) at every level; where k1, k1^(m_P), M^(m_P) and the graded bounds enter; seed value of c^Q_n

Note to change in the existing rows of the crosswalk of [[ch:ten-l5]]: thm:tl5-hf, add "; sharpened constants in
thm:tl5-hfg (P-GRD item 2)"; rem:tl5-hf4-level, add "; points to rem:tl5-hfg-powers (P-GRD item 3)".
