### The parts with ϱ through the bound at a point, and the zeroth order through the shorter words {#sec:tl5-hff}

This section makes two changes. First, in the products with a factor at a point the part with ϱ of a monomial is the
residual of the recovery of its factor D̂²Ψ_C times its factor Φ₁, which is H, h or a Ψ_B, and Step 2 of the bootstrap
bounds Φ₁ by 𝔰 ≤ 𝔰₁^v, which puts the part into ε. At the levels N ≥ 6 with option (b) of [[def:tl5-hft-constants]], Φ₁
is a quantity of 𝔰_P⁰, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰ leaves the factor μ^(−3/2) μ^(b/2) that the parts with 𝒥_g carry,
so these parts hold with μ^(−1) 𝔰_P⁰ in place of 𝔰 ([[lem:tl5-hff-rho]]). Step 3 bounds 𝔰_P⁰ by C_P⁰ e^(φ/2) Y_s +
C_(P,0)⁰ η₀, which has no part with ϱ; the weight e^(−φ) of 𝒮 takes up the factor e^(φ/2), so the part with ϱ gives a
term 𝔯_ϱ^f Y_s², which enters 𝔯, and a part of ε with ϱ η₀. The two routes put the part in different places, and the
theorem takes either. Second, the zeroth-order step bounds the part |Ψ_(JB)|² of the density of each word JB through the
energy of JB itself, whose weight 𝔶_(|J|) μ^(|B|+2) is at most μ^(|JB|), with equality at the largest weights. For JB =
ZC, Z its first letter, the bound |Ψ_(ZC)| ≤ 𝔷 (|D̂Ψ_C|² + |Ψ_C|²)^(1/2) of (∗) in the proof of [[lem:tl5-hfg-products]]
passes it to the energy of the shorter word C, whose weight leaves a factor μ; its coefficient 1/(2Ω̂² z̲) becomes 6μ 𝔷²
𝔨₂, six words ZC sharing each C, or at most 7μ 𝔷² 𝔨₂ for the words that the first letters of a family share, and at each
point of the face the smaller of the two bounds is taken ([[lem:tl5-hff-zero]]). The word h has no shorter word; its
step takes its own leaf weight 𝔶₀^h, which multiplies its own part by 𝔶₀^h μ². Both changes enter the constants with
index f ([[def:tl5-hff-constants]], [[thm:tl5-hff]]). The closing condition is [[eq:tl5-hff-closing]]; with 𝔶₀^h = 𝔶₀
and the first route every new constant is at most the one it replaces, and the earlier closing conditions remain valid.
The notation is that of [[sec:tl5-hfc]].

**Lemma {#lem:tl5-hff-rho}** (The parts with ϱ through the bound of 𝔰_P⁰.) Let N ≥ 6, with option (b) of
[[def:tl5-hft-constants]], and let the setting be that of [[lem:tl5-hft-products]] with 𝔰 ≤ 𝔰₁^v on Q(a, b) and the
replacements of [[lem:tl5-hfy-abs]] and [[lem:tl5-hfz-abs]], so that the bounds of the second derivatives carry k₂^z
ϱ(p)/(1 − 𝔵^z) in place of 2k₂ ϱ(p). Then at every point of Q(a, b), for every word I with n := |I| ≤ N and every word J
with |J| < n, the two inequalities of [[lem:tl5-hft-products]], with 𝔠^ϱ in their terms with ϱ(p) as in
[[lem:tl5-hfe-rho]] (b), hold with

    μ^(−3/2) 𝔠^ϱ_n(μ) (1 − 𝔵^z)⁻¹ k₂^z 𝔰_P⁰ ϱ(p),
    μ^((n−|J|−3)/2) (𝔠^ϱ_(|J|)(μ) + 1) (1 − 𝔵^z)⁻¹ k₂^z 𝔰_P⁰ ϱ(p)                                      {#eq:tl5-hff-rho}

in place of their terms with ϱ(p), that is with μ^(−1) 𝔰_P⁰ in place of 𝔰 there; and the parts 𝔡_n and 𝔡′_(j′) of
[[eq:tl5-hfd-words]] take these forms.

*Proof.* By [[lem:tl5-hfe-rho]] (b) and the proofs of [[lem:tl5-hfs-products]] and [[lem:tl5-hft-products]], a monomial
of 𝔑^L_I has a term with ϱ(p) only if its factor Φ₂ is a second derivative D̂²Ψ_C, and then Φ₁ carries no derivative D̂,
as there are at most two in all, so it is H, h or Ψ_B with |B| ≤ N − 2, and |Φ₁| ≤ μ^(−ℓ_P(Φ₁)/2) 𝔰_P⁰, with ℓ_P as in
the proof of [[lem:tl5-hfg-products]]. The part with ϱ(p) of the bound of Φ₂ is μ^(−ℓ_E(Φ₂)/2) k₂^z ϱ(p)/(1 − 𝔵^z), by
[[lem:tl5-hft-small]] (b) with the replacements. With |Φ_i| ≤ 𝔰 for the other factors, the term with ϱ(p) of the
monomial times μ^(n/2) is at most ν 𝔰^(q−2) μ^((n − ℓ_P(Φ₁) − ℓ_E(Φ₂))/2) 𝔰_P⁰ k₂^z ϱ(p)/(1 − 𝔵^z), with ν its
background norm with the coefficient, q the number of its solution factors and b the number of letters on its background
factors; and ℓ_P(Φ₁) + ℓ_E(Φ₂) ≤ n − b + 3, as in the proof of [[lem:tl5-hfs-products]], so μ^((n − ℓ_P(Φ₁) −
ℓ_E(Φ₂))/2) ≤ μ^(−3/2) μ^(b/2). The proof of [[lem:tl5-hft-products]] bounds the same term by ν 𝔰^(q−2) 𝔰 μ^(−1/2)
μ^(b/2) times the same factor k₂^z ϱ(p)/(1 − 𝔵^z), through |Φ₁| ≤ 𝔰; so the new bound is that one with μ^(−1) 𝔰_P⁰ in
place of 𝔰, and the sum over the monomials with a factor D̂²Ψ_C, by [[lem:tl5-hfe-rho]] (a) with ν′ = μ, gives the first
term of [[eq:tl5-hff-rho]]. For |J| < n, ℒ^J N(h) = 𝔑_J + H^(αβ) D̂_αD̂_βΨ_J. As there, μ^(n/2) |𝔑_J| = μ^((n−|J|)/2)
μ^(|J|/2) |𝔑_J|, and the first term for J bounds the part with ϱ(p) of μ^(|J|/2) |𝔑_J|. In H^(αβ) D̂_αD̂_βΨ_J the factor
Φ₁ is H, with ℓ_P(H) = 2 and |H| ≤ μ⁻¹ 𝔰_P⁰, and the part with ϱ(p) of the bound of D̂²Ψ_J is μ^(−(|J|+1)/2) k₂^z
ϱ(p)/(1 − 𝔵^z); so μ^(n/2) times their product is at most μ^((n−|J|−3)/2) 𝔰_P⁰ k₂^z ϱ(p)/(1 − 𝔵^z), where the proof of
[[lem:tl5-hft-products]] has μ^((n−|J|−1)/2) 𝔰. Adding the two gives the second term. The parts 𝔡_n and 𝔡′_(j′) are
those of the lemma in use, so they take these forms. ∎

**Lemma {#lem:tl5-hff-zero}** (The zeroth-order step through the shorter words.) In the setting of [[lem:tl5-hfp-abs]]
(c), with the weights 𝔶₀, 𝔶₁ and 𝔲₀ and the constants with index l of [[def:tl5-hfe-constants]], let 𝔶₀^h ∈ (0, μ⁻²] and
𝔶^h := (𝔶₀^h, 𝔶₁), let 𝔷 be as in [[def:tl5-hfg-graded]], 𝔨₁ as in [[lem:tl5-hf-sobolev]] and 𝔨₂ as in
[[lem:tl5-hf-linfty]], put 𝔲₀^♯ := 𝔲₀ + 8𝔲₀⁻¹ |D̂∂_γ|², and, with the suprema over Σ₁(a, b),

    C_S^f(p)² := C_(E,0)(𝔶)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ min(𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁,
                  max(6μ 𝔷² 𝔨₂ 𝔲₀^♯ + 2𝔲₀⁻¹ 𝔨₁, 7μ 𝔷² 𝔨₂ 𝔲₀^♯)),
    C_S^h(p)² := C_(E,0)(𝔶^h)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ min(𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁,
                  6μ 𝔷² 𝔨₂ 𝔲₀^♯ + max(2𝔲₀⁻¹ 𝔨₁, 𝔶₀^h μ² (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁))),                  {#eq:tl5-hff-cs}

and let C_(0,0)^h be the constant C_(0,0) of the lemma in use, in its form with index l, formed with 𝔶^h in place of
(𝔶₀, 𝔶₁). Then the zeroth-order step of the lemma in use gives its bound of Ψ_B(p) for 1 ≤ |B| ≤ N − 2, and its bound of
(Σ_(B∈𝔚) |Ψ_B(p)|²)^(1/2) for a family 𝔚 of n distinct such words of one length, with C_S^f in place of C_S^l and the
same parts with η₀; and it gives its bound of h(p) with C_S^h and C_(0,0)^h in place of C_S^l and C_(0,0). Moreover
C_S^f ≤ C_S^l, and for 𝔶₀^h = 𝔶₀, C_S^h ≤ C_S^l and C_(0,0)^h = C_(0,0).

*Proof.* In the proof of [[lem:tl5-hfp-abs]] (c), in the form that the proof of [[thm:tl5-hfe]] gives it with
[[lem:tl5-hfe-face]] (b) and 𝔲 = 𝔲₀, the step for a word B multiplies by μ^(|B|+2) the inequality of
[[lem:tl5-hfe-face]] (b) for A := Ψ_B, and for a family it adds these over B ∈ 𝔚. As ℒ^J Ψ_B = Ψ_(JB), the face term of
that inequality is, by its proof, Σ_(|J|≤2) 𝔶_(|J|) ∫_Σ 𝔳₀⁴ R⁻³ (𝔲₀^♯ |Ψ_(JB)|² + 2𝔲₀⁻¹ |D̂_(∂_γ)Ψ_(JB)|²) dμ dτ₂/(1 −
κκ′), Σ := Σ₁(a, b). There, at each point, |D̂_(∂_γ)Ψ_(JB)|² ≤ 𝔨₁ (e_o + κ′ e_i)[Ψ_(JB)] and |Ψ_(JB)|² ≤ (e_o + κ′
e_i)[Ψ_(JB)]/(2Ω̂² z̲), and (e_o + κ′ e_i)/(1 − κκ′) = ε₁; with 𝔶_(|J|) μ^(|B|+2) ≤ μ^(|JB|) every word JB, these words
being distinct, carries at most 𝔳₀⁴ R⁻³ (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁) times μ^(|JB|) ε₁[Ψ_(JB)] dμ dτ₂, which gives C_S^l,
as Σ_W μ^(|W|) ∫_Σ ε₁[Ψ_W] dμ dτ₂ ≤ ℰ_g(p) for distinct words W of length at most N. Call this the first way of bounding
the parts with |Ψ_(JB)|².

Let 1 ≤ |B| ≤ N − 2. Each word JB is ZC with Z its first letter: Z is the first letter of J and C = J′B if J = ZJ′, and
Z ∈ Γ and C = B′ if J = ∅ and B = ZB′. As in the proof of (∗) of [[lem:tl5-hfg-products]], [[eq:tl5-hf-lie]] and the
Cauchy–Schwarz inequality give |Ψ_(ZC)|² ≤ 𝔷² (|D̂Ψ_C|² + |Ψ_C|²), and |D̂Ψ_C|² + |Ψ_C|² ≤ 𝔨₂ (e_o + κ′ e_i)[Ψ_C], as in
the proof of [[lem:tl5-hf-linfty]]. As 𝔶_k ≤ μ^(k−2) and 𝔶₂ = 1, 𝔶_(|J|) μ^(|B|+2) ≤ μ μ^(|C|) in each case. Bound the
part with |Ψ_(JB)|² in this way for every pair (J, B), the second way, and the part with |D̂_(∂_γ)Ψ_(JB)|² as before.
Then the word JB with |J| = 2 carries 2𝔲₀⁻¹ 𝔨₁ at most; the word JB with |J| ≤ 1 carries at most 2𝔲₀⁻¹ 𝔨₁ + 6μ 𝔷² 𝔨₂
𝔲₀^♯, the words ZJB with Z a rotation being six; and the word B′ with |B′| = |B| − 1 carries at most 7μ 𝔷² 𝔨₂ 𝔲₀^♯, the
words ZB′ in 𝔚 being at most seven, as Z ∈ Γ, and one for a single word; each times 𝔳₀⁴ R⁻³ and μ^(|W|) ε₁[Ψ_W] dμ dτ₂
for the word W. These three classes have the lengths |B| + 2, |B| + 1 or |B|, and |B| − 1, so they are disjoint, and in
each the words are distinct, as the B ∈ 𝔚 have one length. At each point of the face use, for all the pairs at once, the
way for which the largest of the coefficients is the smaller; the set of the points where the first way is used is
closed, as all the functions are continuous. Every word then carries at most 𝔳₀⁴ R⁻³ times the minimum in C_S^f(p)², so
the face term, times μ^(|B|+2), is at most C_S^f(p)² ℰ_g(p) divided by C_(E,0)(𝔶)² 𝔴₀(p)⁴. The terms on S_a are those of
the proof of [[lem:tl5-hfp-abs]] (c), and the rest of the step gives its bounds with C_S^f in place of C_S^l.

For the word h, B = ∅, apply the step with the weights 𝔶^h: [[lem:tl5-hfe-face]] (b) holds with them and C_(E,0)(𝔶^h),
its proof using [[lem:tl5-hfd-leaf]], which holds for all weights, and the step holds with them, as 𝔶₀^h μ² ≤ 1. The
words of the step are the J with |J| ≤ 2. For J = ZJ′ put C := J′; then 𝔶_(|J|) μ² ≤ μ μ^(|J′|), as above. The word h
itself has no shorter word, and its part with |h|² is bounded as before, with the weight 𝔶₀^h μ². In the second way the
word J with |J| = 2 carries at most 2𝔲₀⁻¹ 𝔨₁, the word J with |J| = 1 at most 2𝔲₀⁻¹ 𝔨₁ + 6μ 𝔷² 𝔨₂ 𝔲₀^♯, and h at most
𝔶₀^h μ² (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁) + 6μ (𝔶₁ μ) 𝔷² 𝔨₂ 𝔲₀^♯, with 𝔶₁ μ ≤ 1; each of these is at most the second entry of
the minimum in C_S^h(p)². In the first way every word carries at most 𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁, as 𝔶₁ μ ≤ 1 and 𝔶₀^h μ²
≤ 1, each times 𝔳₀⁴ R⁻³. Choosing at each point as above gives C_S^h, and the terms on S_a, formed with 𝔶^h by the proof
of [[lem:tl5-hfp-abs]] (c), give C_(0,0)^h.

Finally, the first entry of the minimum in C_S^f(p)² is the function whose supremum gives C_S^l(p)², so C_S^f ≤ C_S^l.
For 𝔶₀^h = 𝔶₀, C_(E,0)(𝔶^h) = C_(E,0)(𝔶), so C_S^h ≤ C_S^l for the same reason, and C_(0,0)^h = C_(0,0). ∎

**Definition {#def:tl5-hff-constants}** (The constants with index f.) In the setting of [[def:tl5-hfc-constants]], let
𝔶₀^h ∈ (0, μ⁻²], let C_S^f, C_S^h and C_(0,0)^h be as in [[lem:tl5-hff-zero]], and put C_P⁰ := max(𝔤₁ C_S^h, C_S^f) and
C_(P,0)⁰ := max(𝔤₁ C_(0,0)^h, C_(0,0)). The constants with index f are the constants with index c formed with C_P⁰ and
C_(P,0)⁰ in place of 𝔤₁ C_S^l and 𝔤₁ C_(0,0) at the sites of [[lem:tl5-hfc-h]] and in 𝔎 and 𝔎₀, with C_S^h and C_(0,0)^h
in place of C_S^p and C_(0,0)^p in 𝔨_rec^p and 𝔨_rec^(0,p), and with C_S^h for b = 0 and C_S^f for b ≥ 1 in place of
C_S^p in 𝔐_p^(m), each in its form with index l, and in every constant formed from these. Fix one of the two routes
below for the parts with ϱ, the second only for N ≥ 6 with option (b) of [[def:tl5-hft-constants]]:

    route (𝔰):  ε^f := ε^l,   𝔯_ϱ^f := 0;
    route (𝔯):  ε^f := 𝒮[s_N[2R̂ic] + μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_(P,0)⁰ η₀ ϱ],
                𝔯_ϱ^f := ϱ 𝒮[μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰ e^(φ/2)],                          {#eq:tl5-hff-routes}

with 𝒮 of [[eq:tl5-hf-source]] for a = u*, b = v* and the functions of the point evaluated at it. Let S_F^f, S_M^f and
ε_M^f be S_F^c, S_M^c and ε_M^c formed with the constants with index f, let 𝔯^f be 𝔯^c so formed plus 𝔯_ϱ^f, and put

    η_f := 1 − max(ϑ₁, ϑ₂) − 𝔯^f,      A_f := η_f^(−1/2) δ_w + η_f⁻¹ (ε^f + ε_M^f),      B_f := η_f⁻¹ (S_F^f + S_M^f).

For a number 𝔜 ≥ 0 let 𝔰_*^f[𝔜] be 𝔰_*^c[𝔜] formed with the constants with index f, and, when 4A_f B_f < 1, put

    Y_f := 2A_f/(1 + (1 − 4A_f B_f)^(1/2)),      𝔰_*^f := 𝔰_*^f[Y_f].                            {#eq:tl5-hff-constants}

**Theorem {#thm:tl5-hff}** (Existence with the parts with ϱ through the bound at a point and the zeroth order through
the shorter words.) In the setting of [[thm:tl5-hfc]], with 𝔶₀^h ∈ (0, μ⁻²], one of the routes of [[eq:tl5-hff-routes]]
and the constants with index f of [[def:tl5-hff-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 −
ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_f > 0, the closing condition

    4 A_f B_f = 4 η_f^(−3/2) (δ_w + η_f^(−1/2) (ε^f + ε_M^f)) (S_F^f + S_M^f) < 1,                 {#eq:tl5-hff-closing}

and 𝔰_*^f < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_f for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with 𝔰_*^f in place of 𝔰_*. For
𝔶₀^h = 𝔶₀ and route (𝔰) each constant with index f is at most the one with index c it replaces, ε^f = ε^c, η_f ≥ η_c,
A_f ≤ A_c, B_f ≤ B_c, Y_f ≤ Y_c and 𝔰_*^f ≤ 𝔰_*^c; so the hypotheses of [[thm:tl5-hfc]] imply these.

*Proof.* The proof of [[thm:tl5-hfc]] applies with the constants with index f, ε^f, 𝔯^f, η_f, A_f, B_f, Y_f, 𝔰_*^f[𝔜]
and [[eq:tl5-hff-closing]] in place of those with index c, with two changes.

*The zeroth order.* By [[lem:tl5-hff-zero]], the zeroth-order step of the lemma in use gives its bounds of h(p), of
Ψ_B(p) with 1 ≤ |B| ≤ N − 2 and of the families of words of one length with C_S^h and C_(0,0)^h for h and with C_S^f and
C_(0,0) for the others. With [[lem:tl5-hfc-h]], μ |H(p)| ≤ 𝔤₁ μ |h(p)|, so 𝔰_P⁰(p) ≤ C_P⁰(p) ℰ_g(p)^(1/2) + C_(P,0)⁰(p)
η₀(p). The bounds at a point that the proof of [[thm:tl5-hfc]] uses take the zeroth-order step only through these
bounds: through the quantities of 𝔰_P⁰, in the entries of [[lem:tl5-hfc-h]] and in 𝔎 and 𝔎₀, which Step 3 of the proof
of [[prop:tl5-hfs-bootstrap]] forms from the bound of 𝔰_P⁰; through μ |h(p)| in [[lem:tl5-hfp-rec]]; and through the
families of the words of each length in [[lem:tl5-hfp-low]]. Each is formed from the bounds of the step in the same way
for all values of their constants, so they hold with the constants with index f.

*The parts with ϱ.* With route (𝔰) the proof of [[thm:tl5-hfc]] bounds them as written, with ε^c = ε^f. With route (𝔯),
after Step 1, 𝔰 ≤ 𝔰₁^v on D^κ_s, so [[lem:tl5-hff-rho]] applies at every point of D^κ_s, with ϱ(p) ≤ ϱ. In Step 2 the
terms with ϱ of the family of level j are bounded as in the proof of [[thm:tl5-hfe]], through Step 2 of the proof of
[[prop:tl5-hft-bootstrap]] with 𝔠^ϱ and the replacements, now with μ⁻¹ 𝔰_P⁰ in place of 𝔰 by [[lem:tl5-hff-rho]]. With
the weights μ^|I| they contribute to the bulk at most 2Ω̂² μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z 𝔰_P⁰ ϱ (√e_o + √c √e_i) at
each point, where that proof has 𝔰₁^v in place of μ⁻¹ 𝔰_P⁰. As ℰ_g(p) ≤ e^(φ(p)) Y_s² at every point p of D^κ_s, the
bound of 𝔰_P⁰ gives 𝔰_P⁰ ≤ C_P⁰ e^(φ/2) Y_s + C_(P,0)⁰ η₀ there. So this part together with the forcing term is at most
2Ω̂² s (√e_o + √c √e_i), with s := s_N[2R̂ic] + s₀ + Y_s s₁, s₀ := μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_(P,0)⁰ η₀ ϱ and s₁
:= μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰ e^(φ/2) ϱ. As in the proof of [[prop:tl5-hf-linear]], its integral with the
weight e^(−φ) over Q(a′, b′) is at most Y_s 𝒮[s]; and 𝒮 is subadditive and positively homogeneous, so Y_s 𝒮[s] ≤ Y_s
ε^f + 𝔯_ϱ^f Y_s². The inequality of Step 3 then holds with ε^f in place of ε^c and with 𝔯^f in place of 𝔯^c, and gives
(H1) with A_f and B_f.

The rest of the proof of [[thm:tl5-hfc]], with A_f, B_f, Y_f and 𝔰_*^f[𝔜], holds as written. For the last claim, let
𝔶₀^h = 𝔶₀ and take route (𝔰). By [[lem:tl5-hff-zero]], C_S^h ≤ C_S^l, C_S^f ≤ C_S^l and C_(0,0)^h = C_(0,0), so C_P⁰ ≤
𝔤₁ C_S^l and C_(P,0)⁰ = 𝔤₁ C_(0,0), as 𝔤₁ ≥ 1; every constant with index c is nondecreasing in these numbers, so each
constant with index f is at most the one it replaces; and 𝔯_ϱ^f = 0 and ε^f = ε^c. Then η_f ≥ η_c, A_f ≤ A_c, B_f ≤ B_c
and 4A_f B_f ≤ 4A_c B_c. The smaller root 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, so Y_f ≤ Y_c, and
𝔰_*^f ≤ 𝔰_*^f[Y_c] ≤ 𝔰_*^c[Y_c] = 𝔰_*^c, as 𝔰_*^c[𝔜] is nondecreasing in 𝔜 and in the constants. ∎

**Remark {#rem:tl5-hff-what}** (What changes.) In the products with a factor at a point, the part with ϱ of a monomial
is the residual of the recovery of its factor D̂²Ψ_C times its factor Φ₁, which is H, h or a Ψ_B. The bound |Φ₁| ≤ 𝔰 ≤
𝔰₁^v makes it a forcing term with the factor 𝔰₁^v ϱ, which enters ε, and so A, the closing condition and the term of 𝔰_*
with A, which carries μ^(−N/2). In route (𝔯), Φ₁ is bounded as a quantity of 𝔰_P⁰, at the cost of a factor μ⁻¹, the
weights leaving μ^(−3/2) μ^(b/2) in place of μ^(−1/2) μ^(b/2), and 𝔰_P⁰ by its bound at the point, which comes from the
energies and from η₀ alone. The factor e^(φ/2) of that bound is taken up by the weight e^(−φ) of 𝒮, as e^(φ/2) is in
S_F, so the part gives the term 𝔯_ϱ^f Y_s², which enters 𝔯, and a part of ε with ϱ η₀: in the coefficient of ϱ in ε, μ⁻¹
C_(P,0)⁰ η₀ takes the place of 𝔰₁^v, and 𝔯_ϱ^f carries μ⁻¹ C_P⁰ where ε^l carries 𝔰₁^v. The two routes put the part in
different places, ε against 𝔯, so the theorem takes either; it takes route (𝔯) only for N ≥ 6 with option (b), where the
bounds of the second derivatives carry the weight μ^(−(|C|+1)/2) on their parts with ϱ. In the zeroth-order step, the
part |Ψ_(JB)|² of the density of a word JB is bounded through the energy of JB itself, with the weight 𝔶_(|J|)
μ^(|B|+2), which is μ^(|JB|) at the largest weights 𝔶_k = μ^(k−2), so its coefficient 1/(2Ω̂² z̲) has no factor μ.
Through the shorter word C with JB = ZC the weight leaves the factor μ, and the coefficient becomes 6μ 𝔷² 𝔨₂, or at most
7μ 𝔷² 𝔨₂ for the words B′ that the first letters of a family share; the part with |D̂_(∂_γ)Ψ_(JB)|² stays with its own
word. At each point the smaller bound is taken, so C_S^f ≤ C_S^l for all weights. The word h has no shorter word, and
its own part keeps the coefficient 1/(2Ω̂² z̲) with the factor 𝔶₀^h μ²; a weight 𝔶₀^h < 𝔶₀ lowers it, at the cost of
C_(E,0)(𝔶^h) ≥ C_(E,0)(𝔶), whose square has the term 1/(2π² 𝔶₀^h) with j₁ = j₂ = 0. The entry C_P⁰ that bounds μ |H| and
the Ψ_B is the larger of 𝔤₁ C_S^h and C_S^f, so it falls only if both do, which is why the step for h takes its own
weight. The counts, the recovery constants, the first-order constants, the weights 𝔲₀, 𝔲₁, 𝔲_M, the thresholds 𝔰₀ and
𝔰₁^v and the rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hff]] are
established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD bea115c4, where sec:tl5-hfc is merged (Section 57.29,
merge 203efd5e). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hff) through the last line of
[[rem:tl5-hff-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfc-what]] (line 7643,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfc-what]] (lines 7641–7642).* Old:

rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfc]] are established in
this paper for no background at 10 l5.

New (one line added, of 117 characters; the two old lines are unchanged):

rates are unchanged. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfc]] are established in
this paper for no background at 10 l5.
[[sec:tl5-hff]] moves the parts with ϱ into 𝔯 and takes the zeroth order through the shorter words ([[thm:tl5-hff]]).

*3. Nothing else changes.* No earlier text is edited: the sites listed in the Comparison keep their texts, and the new
constants are defined in def:tl5-hff-constants by reference to them.

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hff acts at every level, on thm:tl5-hfc; its route (𝔯) acts only at N ≥ 6 with option (b).

**Containment.** For 𝔶₀^h = 𝔶₀ and route (𝔰) every new factor is at most the old one, for all admissible weights and
choices, so thm:tl5-hff contains thm:tl5-hfc, and through it every earlier theorem in the range where thm:tl5-hfc
contains it. Exactly where:
- the last claim of thm:tl5-hff and the last paragraph of its proof;
- C_S^f ≤ C_S^l holds for all weights, through the first entry of the minimum in eq:tl5-hff-cs (lem:tl5-hff-zero);
- C_S^h ≤ C_S^l and C_(0,0)^h = C_(0,0) need 𝔶₀^h = 𝔶₀; then C_P⁰ ≤ 𝔤₁C_S^l and C_(P,0)⁰ = 𝔤₁C_(0,0), as 𝔤₁ ≥ 1;
- ε^f = ε^c and 𝔯_ϱ^f = 0 need route (𝔰);
- Y_f ≤ Y_c, as the smaller root 2A/(1 + (1 − 4AB)^½) is nondecreasing in A and in B; 𝔰_*^f ≤ 𝔰_*^c, as 𝔰_*^c[𝔜] is
  nondecreasing in 𝔜 and in the constants.
The present closing conditions stay valid beside the new one: no earlier theorem is changed, and thm:tl5-hfc is the case
just named.

**Both constraints.** Every change enters both 𝔰_*^f and the closing condition: C_P⁰ through C_P^v and C_∞ in 𝔰_*, and
through 𝔎, 𝔎₀ (so 𝔎^D, 𝔎^D₀) in S_F and 𝔯; C_S^h through 𝔨_rec^p in C_P^v and 𝔎; C_S^h and C_S^f through 𝔐_p^(m) in
C_(∞,μ)^(m), so in 𝔰_* and in S_F at N ≥ 6; route (𝔯) through ε^f in A_f, and through 𝔯_ϱ^f in η_f, both of which
enter A_f and B_f, hence 𝔰_*^f and 4A_fB_f.

Unchanged: all counts (𝔠^♮, 𝔠^D, 𝔠^(D,7), 𝔠^ϱ, 𝔠^Mq), the recovery constants (𝔨_♯, K_rec, k₁^D, k₂^z, 𝔷₁′, 𝔷₂′),
the first-order constants (C₁^l(𝔚), C₁^l, C₁^(Γ,l), C_(1,ϱ)^l, C_(1,0)), C_(0,0) for the words other than h, the
weights 𝔲₀, 𝔲₁, 𝔲_M, 𝔶₀, 𝔶₁, θ, ϑ₁, ϑ₂, the functions 𝔨₁, 𝔨₂, 𝔷, 𝔵^z, the thresholds 𝔰₀ and 𝔰₁^v with the cap, the
factor 𝔤₁, the rule of the threshold (Y_f has the form of Y_c), S_M, ε_M, and the rates.

1. Lever 4, the parts with ϱ into 𝔯 (lem:tl5-hff-rho; route (𝔯) of eq:tl5-hff-routes).
   - The check of 𝒮, made first. In eq:tl5-hf-source, ‖f‖²_(1,t) = ∫_(Σ₁(t,b)) e^(−φ) f² dμ dτ₂/(1 − κκ′), and ‖f‖_(2,t)
     likewise, so a factor e^(φ/2) of the source cancels the weight: 𝒮[e^(φ/2) f] is 𝒮₀[f], 𝒮₀ being 𝒮 with φ
     replaced by 0, as in prop:tl5-hf-linear. 𝒮 is subadditive and positively homogeneous (rem:tl5-hfw-what) and
     monotone on s ≥ 0, which is all the proof uses. The factor e^(φ/2) is the one S_F carries; so
         𝔯_ϱ^f = ϱ 𝒮₀[μ⁻¹ (1 − 𝔵^z)⁻¹ 𝔤^l_(ϱ,t) k₂^z C_P⁰].
   - The factor Φ₁ that the route bounds differently: when Φ₂ = D̂²Ψ_C, Φ₁ is H, h or Ψ_B (proof of
     lem:tl5-hfs-products), a quantity of 𝔰_P⁰, whose bound at a point has no part with ϱ. So there is no ϱ² term: the
     route gives a Y_s² term in 𝔯 and a ϱη₀ term in ε only.
   - The sites, at HEAD bea115c4, old → new in route (𝔯):
     - 87:5607 (lem:tl5-hfs-products, "With |Φ₁| ≤ 𝔰 in the term with ϱ(p)"), 87:5898–5899 (lem:tl5-hft-products, "is
       then at most ν 𝔰^(q−1) μ^((n − ℓ_E(Φ₂))/2) 2k₂ ϱ(p)") and 87:5902 ("μ^((n−|J|−1)/2) 𝔰 2k₂ ϱ(p)")
         → the two terms of eq:tl5-hff-rho, μ^(−1) 𝔰_P⁰ in place of 𝔰; the lemmas themselves are kept;
     - 87:6287 (thm:tl5-hfw, "we use 2k₂ 𝔰 ϱ ≤ 2𝔰₁^v k₂ ϱ, by Step 1"), 87:6385 (thm:tl5-hfy, "k₂ 𝔰 ϱ/(1 − 𝔵) ≤ 𝔰₁^v
       k₂ ϱ/(1 − 𝔵)") and 87:7471 (proof of thm:tl5-hfe, "With the bound 𝔰 ≤ 𝔰₁^v of Step 1")
         → 𝔰_P⁰ ≤ C_P⁰ e^(φ/2) Y_s + C_(P,0)⁰ η₀ at each point, with μ⁻¹;
     - 87:7426 (def:tl5-hfe-constants, "ε^l := 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^l k₂^z ϱ]")
         → ε^f, the factor 𝔰₁^v of the coefficient of ϱ replaced by μ⁻¹ C_(P,0)⁰ η₀; and 𝔯^f := 𝔯^c + 𝔯_ϱ^f.
   - Not offered at N = 4 or with option (a), where the products carry 𝔠^ϱ at other arguments (ν; 1 with the level
     weights μ^(n/2)); their forms with 𝔰_P⁰ are not proved here.
   - An option, not a minimum: route (𝔰) puts the part into ε, route (𝔯) into 𝔯 (and ϱη₀ into ε). Each theorem holds
     with its route's ε^f and 𝔯^f; neither set of constants is at most the other.
2. Lever 3a, the zeroth order through the shorter words (lem:tl5-hff-zero).
   - Old: C_S^l(p)² := C_(E,0)(𝔶)² 𝔴₀(p)⁴ sup 𝔳₀⁴ R⁻³ (𝔲₀^♯/(2Ω̂² z̲) + 2𝔲₀⁻¹ 𝔨₁) (87:7399), one constant for
     every word B of the step (lem:tl5-hfp-abs (c), 87:6713–6723).
   - New: C_S^f for 1 ≤ |B| ≤ N − 2 and for its families, with the coefficient 1/(2Ω̂² z̲) replaced, at each point where
     this is smaller, by 6μ𝔷²𝔨₂ (and the words B′ shared by the first letters of a family carrying 7μ𝔷²𝔨₂ alone);
     C_S^h for h, with its own leaf weight 𝔶₀^h.
   - The word h: of the note's two options, the first is taken, the step for h with its own leaf weight 𝔶₀^h ≤ μ⁻².
     The reason: h carries the entry 𝔤₁C_S^h of μ|H| in C_P⁰ = max(𝔤₁C_S^h, C_S^f). With the second option, h's own
     part kept and the gain taken only for |B| ≥ 1, C_P⁰ = 𝔤₁C_S^l and the entry does not move. The second option is
     the case 𝔶₀^h = 𝔶₀ of the first, so nothing is lost by taking the first.
   - The bookkeeping (proof of lem:tl5-hff-zero): the classes of words JB with |J| = 2, JB with |J| ≤ 1, and B′, of
     lengths |B| + 2, |B| + 1 or |B|, and |B| − 1; preimages 6 (the rotations as first letter of J) and, for B′, 1 for a
     single word and at most 7 for a family (Z ∈ Γ). The weights: 𝔶_(|J|) μ^(|B|+2) ≤ μ μ^(|C|) in every case, from
     𝔶_k ≤ μ^(k−2), 𝔶₂ = 1. The part 8𝔲₀⁻¹|D̂∂_γ|²|Ψ_(JB)|² of the Y bracket takes the same route, inside 𝔲₀^♯.
   - The sites, at HEAD bea115c4, old → new: the entries 𝔤₁C_S^l and 𝔤₁C_(0,0) of μ|H| and the Ψ_B (the sites of
     lem:tl5-hfc-h, among them eq:tl5-hfs-linfty, eq:tl5-hfg-cinf and its forms, C_P^v and C_(P,0)^v, and 𝔎, 𝔎₀ of
     def:tl5-hfs-constants, 87:5655) → C_P⁰, C_(P,0)⁰; 87:6675 and 87:6677 (𝔨_rec^p, "𝔷₂′ μ C_S^p) + (1 − 𝔰₁^v)⁻¹ μ
     𝔯_♯ C_S^p", and 𝔨_rec^(0,p)) → C_S^h, C_(0,0)^h; 87:6672 (𝔐_p^(m)) → C_S^h at b = 0, C_S^f at b ≥ 1.
3. The closing condition eq:tl5-hff-closing is eq:tl5-hfc-closing with the constants with index f; it also defines
   Y_f, through 4A_fB_f < 1.

What they give, deduced, not evaluated; upper figures. Assumptions:
- every supremum at one point: each fall below is that of the leading entry at its supremum; with the new constants the
  supremum, or the leading entry, may move, so the figures are upper figures;
- the figures taken from G0g and G0j were measured at the suprema of other constants (S_F, C₁^x) and in earlier rounds;
  they stand in for the values at the supremum of C_S;
- G0q (P-GRD14 evaluated) has not reached me; the figures of G0p are before P-GRD14.
Lever 4, at level 6 (G0p §G0p.4).
- G0p's optima: f / ϱ = −31.96 / −32.01, −28.82 / −28.75, −40.52 / −40.54, −34.82 / −34.80; share of ε given to f
  0.03 / 0.5 / 0.1 / 0.4; 𝔰_* sets ε, 4.94 / 3.74 / 6.11 / 4.98 decades below the closing.
- At those parameters, fixed: route (𝔯) leaves ϱ in ε only with μ⁻¹C_(P,0)⁰η₀ in place of 𝔰₁^v. If that part and
  𝔯_ϱ^f are negligible, f may take all of ε, a rise of log₁₀(1/share) = 1.52 / 0.30 / 1.00 / 0.40, and min(f, ϱ) rises
  by at most that plus the margin of f over the minimum: +1.57 / +0.30 / +1.02 / +0.40. ϱ is then bounded only by 𝔯
  and by the term of 𝔰_* with ϱ; neither is evaluated.
- Re-optimised: G0p's computed price of ε's coefficient of ϱ × 0.1 is +0.90 / +0.61 / +0.81 / +0.40. Wherever
  μ⁻¹C_(P,0)⁰η₀ ≤ 0.1 𝔰₁^v at the supremum, the point that attains that price has under route (𝔯) an ε no larger, and
  an η smaller by 𝔯_ϱ^f; so route (𝔯) attains the price less a loss of order 𝔯_ϱ^f/ln 10 decades. At seed 2 D_A the
  price exceeds the fixed-parameter figure, so the re-optimisation pays there.
- The two factors this needs are not reported at level 6: η₀/𝔰₁^v (at level 4, G0p §G0p.0 has η₀ = 10^−18.6 /
  10^−18.0 / 10^−20.1 / 10^−19.3 and 𝔰₁^v = 5.0 × 10⁻⁵ / 2.0 × 10⁻⁵ / 4.5 × 10⁻⁵ / 1.4 × 10⁻⁵), and 𝔯_ϱ^f (at level 4,
  G0p §G0p.1 puts ϱ's 𝔯 budget 2.2–4.4 decades away).
Lever 3a.
- At the supremum of C_S, the second entry of the minimum taken, the first entry of its maximum the larger, and 𝔲₀
  chosen pointwise for each bracket: with X := 1/(2Ω̂² z̲), Y := 8|D̂∂_γ|² X + 2𝔨₁, X′ := 6μ𝔷²𝔨₂ and Y′ := 8|D̂∂_γ|²
  X′ + 2𝔨₁, the least values are 2(XY)^½ and 2(X′Y′)^½, so C_S^f/C_S^l = (X′Y′/(XY))^¼. For X′ ≤ X, Y′ ≤ Y, and
  the fall of C_S lies between ¼ and ½ of log₁₀(X/X′).
- X/X′ = (X/𝔨₂)/(6μ𝔷²). With X/𝔨₂ the share of 1/z̲ in 𝔨₂'s numerator, 0.75 / 0.73 / 0.81 / 0.81 (G0j §G0j.1),
  𝔷 = 10^0.75 / 10^0.68 / 10^0.67 / 10^0.59 (G0g §G0g.3, as 𝔨_B = max(𝔷, 2)), and G0p's level-4 μ = 10⁻⁵ / 3 × 10⁻⁵ /
  10⁻⁶ / 3 × 10⁻⁶ (§G0p.0): log₁₀(X/X′) = 2.60 / 2.25 / 3.79 / 3.47, so C_S^f falls by 0.65–1.30 / 0.56–1.12 /
  0.95–1.90 / 0.87–1.74 decades. At G0p's level-6 μ = 10⁻⁵ / 10⁻⁴ / 3 × 10⁻⁶ / 10⁻⁵ (§G0p.4): log₁₀(X/X′) = 2.60 /
  1.73 / 3.31 / 2.95, falls of 0.65–1.30 / 0.43–0.86 / 0.83–1.66 / 0.74–1.48 decades.
- C_S^h falls as much where 𝔶₀^h μ² (𝔲₀^♯X + 2𝔲₀⁻¹𝔨₁) ≤ 2𝔲₀⁻¹𝔨₁, which near the new optimal 𝔲₀ asks for 𝔶₀^h μ² of
  about X′/X or less, at the cost C_(E,0)(𝔶^h)/C_(E,0)(𝔶), not evaluated (1 at 𝔶₀^h = 𝔶₀).
- Level 4. After P-GRD14's factor 𝔤₁ (−0.30 on the entry of μ|H|), G0p's margins (§G0p.1: log₁₀ sup 𝔨_rec^p / sup 2C_S
  = −0.195 / +0.109 / −0.108 / +0.223) put 𝔨_rec^p above the entry 𝔤₁C_S at all four, by +0.106 / +0.410 / +0.193 /
  +0.524. So C_P^v does not move with C_P⁰: about 0 through 𝔰_*. Through S_F (𝔎 = max(C_P⁰𝔨_A, C_P𝔨_B)) where the
  closing binds (seed 2 D_A): not evaluated. This is the note's expectation: 𝔨_rec^p is the next constant at level 4.
- Level 6. G0p's price of C_S ÷ 2 is +0.22 / +0.06 / +0.18 / +0.02 (§G0p.4, before P-GRD14); C_S acts there through
  𝔐_p^(2), which carries C_S without the factor of H, and through S_F. Where both C_S^f and C_S^h fall by 0.30 or more
  at the points that matter, the point attaining that price stays admissible, so lever 3a pays at least it; the falls
  above at the level-6 μ exceed 0.30 in every case. Beyond 0.30 it is capped where the C₁ part of 𝔐_p^(2) leads;
  G0p gives 𝔐_p^(2)/C₁ = 0.92–1.29 decades, but not the split of 𝔐_p^(2) between its parts.
The two levers act on different factors (the coefficient of ϱ in ε; C_S in 𝔐_p, C_P⁰ and 𝔎), so at level 6 their gains
add at most; they are not evaluated together.

Not done (P-GRD16 if G0q leaves room).
- The C₁ term of 𝔨_rec^p, a weighted family version of lem:tl5-hfp-c1 for the seven fields. Scoped, not drafted:
  - the recovery's leading term is 𝔨_♯ times the norm of (v_Z) ↦ (|T|⁻¹ v_T, (Σ c^ab_j v_(K_ab))_j) at p, so a
    weighted bound would apply the Sobolev inequality to |T(p)|⁻¹ D̂Ψ_T and to the six fields Σ c^ab_j(p) D̂Ψ_(K_ab),
    with constant coefficients;
  - in the proof of lem:tl5-hfp-c1 the parts that come from words ending in the letter B (the leading terms D̂Ψ_(JB),
    the recovery k₁^D 𝒟_g through the words ZJB, the terms 𝔷_Z and 𝔯_♯|Ψ_C|, the remainders R′ with Ψ_(σB)) can be
    bounded through the face energies of the words ending in T and in a rotation, whose sum is at most ℰ_g; the terms
    with 𝔄 and the nonlinear terms, bounded through the full 𝒥_g and 𝔐, do not split;
  - so the parts that split give at most max(|T|⁻², λ_M⁻¹) times their present coefficient squared, that is K_rec² times
    it: no gain in the worst case; only the parts that do not split gain, their count (43n)^½ becoming (43|T|⁻² +
    258λ_M⁻¹)^½ against 301^½ K_rec, and 𝔞_𝔄 likewise;
  - on those parts the factor is between (258/301)^½ = 0.93 (λ_M^(−½) ≥ |T|⁻¹) and (43/301)^½ = 0.38 (|T|⁻¹ ≫
    λ_M^(−½)); in 𝔩_D(Γ) they are the part 301^½ 𝔵^z/(1 − 𝔵^z) of 1 + 301^½ 𝔵^z/(1 − 𝔵^z), 1.27 of 2.27 at
    𝔵^z = 0.068 (G0p §G0p.0, seed 1 D_A);
  - the bound is plausible but not proved: it needs the face energies split by the last letter of the words, which no
    lemma of the chapter gives, and whether it gains turns on |T|⁻¹ against λ_M^(−½) at the supremum, which G0q is
    measuring.
- Lever 4 at N = 4 and with option (a).
- The weighted Cauchy–Schwarz inequality for 𝔨₁ and |H| ≤ |h|/(1 − |h|) in place of 𝔤₁ (P-GRD14's list).

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hff	paper/reader/proofs/P-GRD15.md@PENDING:1	P-GRD15, section	new; at the end of ch:ten-l5, after rem:tl5-hfc-what; the parts with rho of the products through the bound of s_P^0 at a point, into r (route (r), N >= 6, option (b)); the zeroth-order step through the energies of the shorter words, and a leaf weight y_0^h for the word h
    lem:tl5-hff-rho	paper/reader/proofs/P-GRD15.md@PENDING:21	P-GRD15, Lemma	N >= 6, option (b): the terms with rho(p) of lem:tl5-hft-products hold with mu^(-1) s_P^0 in place of s
    eq:tl5-hff-rho	paper/reader/proofs/P-GRD15.md@PENDING:29	P-GRD15, display	new
    lem:tl5-hff-zero	paper/reader/proofs/P-GRD15.md@PENDING:52	P-GRD15, Lemma	the zeroth-order step with C_S^f for |B| >= 1 and its families (|Psi_(ZC)|^2 through the energy of C: coefficient 6 mu z^2 k_2, 7 for the words shared in a family, the smaller bound at each point) and with C_S^h, C_(0,0)^h for h, with its own leaf weight y_0^h; C_S^f <= C_S^l
    eq:tl5-hff-cs	paper/reader/proofs/P-GRD15.md@PENDING:60	P-GRD15, display	new
    def:tl5-hff-constants	paper/reader/proofs/P-GRD15.md@PENDING:106	P-GRD15, Definition	constants with index f: C_P^0 = max(g_1 C_S^h, C_S^f), C_(P,0)^0 = max(g_1 C_(0,0)^h, C_(0,0)) in place of g_1 C_S^l, g_1 C_(0,0); C_S^h in k_rec^p; C_S^h, C_S^f in M_p^(m); routes (s), (r) for the parts with rho; eta_f, A_f, B_f, Y_f, s_*^f
    eq:tl5-hff-routes	paper/reader/proofs/P-GRD15.md@PENDING:116	P-GRD15, display	route (s): eps^f = eps^l, r_rho^f = 0; route (r): eps^f = S[s_N + mu^(-1)(1 - x^z)^(-1) g^l_(rho,t) k_2^z C_(P,0)^0 eta_0 rho], r_rho^f = rho S[mu^(-1)(1 - x^z)^(-1) g^l_(rho,t) k_2^z C_P^0 e^(phi/2)]
    eq:tl5-hff-constants	paper/reader/proofs/P-GRD15.md@PENDING:125	P-GRD15, display	new
    thm:tl5-hff	paper/reader/proofs/P-GRD15.md@PENDING:127	P-GRD15, Theorem	thm:tl5-hfc with the constants with index f and either route; Y_sigma <= Y_f; for y_0^h = y_0 and route (s) its hypotheses are implied by those of thm:tl5-hfc
    eq:tl5-hff-closing	paper/reader/proofs/P-GRD15.md@PENDING:132	P-GRD15, display	closing condition: 4 eta_f^(-3/2)(delta_w + eta_f^(-1/2)(eps^f + eps_M^f))(S_F^f + S_M^f) < 1
    rem:tl5-hff-what	paper/reader/proofs/P-GRD15.md@PENDING:171	P-GRD15, Remark	what changes
