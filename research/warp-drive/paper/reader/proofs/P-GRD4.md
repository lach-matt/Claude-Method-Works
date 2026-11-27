### The constants at level four sharpened a fourth time {#sec:tl5-hfq}

This section sharpens the constants of [[sec:tl5-hft]] at level four and proves [[thm:tl5-hf4]] with them. Three changes
are made. First, the products of level four with no factor at a point are counted exactly, monomial by monomial, also in
the terms of higher order of N(h), which removes the constant 𝔠^(3♮)₄ and the count 49 from them ([[lem:tl5-hfq-m]]).
Second, the absorption of the nonlinear terms in the recovery of second derivatives is weighted separately for the parts
with the energies and for those with ϱ and η₀, by μ and by μ^θ for a number θ ∈ [0, 1]; for θ = 0 and θ = 1 this gives
the two options of [[lem:tl5-hft-small]], and between them a family of thresholds and of requirements on ϱ and η₀
([[lem:tl5-hfq-theta]]). Third, three constants of the products with no factor at a point lose a count of words or take
the recovery constant of the level where it is used ([[lem:tl5-hfq-mixed]]). The closing condition is
[[eq:tl5-hf4q-closing]]; those of the earlier theorems remain valid. Throughout, N = 4 unless stated otherwise, μ ∈ (0,
1], the notation is that of [[sec:tl5-hfs]] and [[sec:tl5-hft]], with either choice of Sobolev constants made in
[[sec:tl5-hft]], and the second expansion of [[def:tl5-hfg-graded]] is used.

**Lemma {#lem:tl5-hfq-m}** (The products with no factor at a point, counted exactly.) Let h be as in
[[def:tl5-hfg-graded]] with N = 4, p a point with 𝔰(p) ≤ 𝔰_♭, and P₁, P₂ as in [[lem:tl5-hfs-quadratic]] (c). Then at p

    (Σ_(|I|=4) |𝔑^M_I|²)^(1/2) ≤ 𝔠^Mq₁ P₁ + 𝔠^Mq₂ P₂,
    𝔠^Mq₁ := 480 + 96 𝔤₁ (𝔤₀ + √5) 𝔰_♭,      𝔠^Mq₂ := 4 + 4 𝔤₁ 𝔰_♭ (2 + 𝔤₁ 𝔰_♭).                          {#eq:tl5-hfq-m}

*Proof.* By the proof of [[lem:tl5-hfs-quadratic]] (c), the monomials of 𝔑^M_I have b = 0, two high factors carrying all
four letters, which are D̂Ψ_(I_S) and D̂Ψ_(I_(S^c)) with |S| = 2 or Ψ_(I_S) and D̂²Ψ_(I_(S^c)) with |S| = 3, and other
factors carrying no letter; those of Q contribute at most 480 P₁ + 4 P₂. In the terms of R₃ a factor carrying letters is,
in a monomial of 𝔑^M_I, one of the two high factors, since b = 0. So the factors ĝ⁻¹ carry no letter, and a factor g⁻¹
carrying letters contributes one block Ψ_B with r = 1, that is −g⁻¹ Ψ_B g⁻¹, B of length 3, the expansion of
[[lem:tl5-hfs-quadratic]] (a) giving no other monomial of this kind. A factor g⁻¹ = ĝ⁻¹ + H that joins two factors or
raises an index costs at most 𝔤₁, one that may close a trace at most 𝔤₀, and a factor ĝ⁻¹ that carries no letter costs 1
or, in 𝒯_m, √5; and |h| ≤ 𝔰 ≤ 𝔰_♭. In H₂^(λσ) D̂_λD̂_σ h, H₂ = g⁻¹ h ĝ⁻¹ h ĝ⁻¹, the factor D̂²Ψ_(I_(S^c)), |S^c| = 1,
comes from D̂²h, and Ψ_(I_S) from the first h, from the second, or from the factor g⁻¹ as the block −g⁻¹ Ψ_(I_S) g⁻¹; the
three monomials are at most 𝔤₁ 𝔰, 𝔤₁ 𝔰 and 𝔤₁² 𝔰² times |Ψ_(I_S)| |D̂²Ψ_(I_(S^c))|. The terms 2𝔠(H₂)h contain no
derivative D̂, and two high factors Ψ_B would need six letters. In 2𝔮 − 2𝔮̂ = Σ_m c_m (𝒯_m(H, g⁻¹, D̂h, D̂h) + 𝒯_m(ĝ⁻¹,
H, D̂h, D̂h)), H = −g⁻¹ h ĝ⁻¹, the high pair is D̂Ψ_(I_S), D̂Ψ_(I_(S^c)) from the two factors D̂h, as a factor Ψ_B of
length 3 would be paired with D̂Ψ of length one, which is low; with |H| ≤ 𝔤₁ |h| and Σ |c_m| = 16 these monomials are at
most 16 𝔤₁ 𝔰 (𝔤₀ + √5) |D̂Ψ_(I_S)| |D̂Ψ_(I_(S^c))|. For fixed S the map I ↦ (I_S, I_(S^c)) is a bijection from the words
of length 4 onto the pairs of words of lengths |S| and 4 − |S|; so Minkowski's inequality over the six sets S with |S| =
2 and the four with |S| = 3 gives [[eq:tl5-hfq-m]]. ∎

**Lemma {#lem:tl5-hfq-theta}** (The absorption weighted in two parts.) Let N ≥ 4, θ ∈ [0, 1] and ν := μ^θ, let g, h,
p, a, b, ϱ(p) and η₀(p) be as in [[lem:tl5-hfs-linfty]], k₃^♮(·) as in [[lem:tl5-hft-small]] (b), and suppose that 𝔰 ≤
𝔰₀^q := min(𝔰_♭, 1/(2 sup_(Q(a,b)) k₃^♮(ν))) on Q(a, b). Then at every point of Q(a, b), for every word C with |C| ≤ j ≤
N − 1,

    |D̂²Ψ_C| ≤ 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ν^(−(|C|+1)/2) ϱ(p);                             {#eq:tl5-hfq-m2}

at p, with the constants of [[eq:tl5-hfs-linfty]] for μ and for ν,

    𝔰(p) ≤ μ^(−N/2) C_(∞,μ)^(N−4)(p) ℰ_g(p)^(1/2)
           + ν^(−N/2) (C_((∞,ϱ),ν)^(N−4)(p) ϱ(p) + C_((∞,0),ν)^(N−4)(p) η₀(p));                       {#eq:tl5-hfq-small}

the statements of [[lem:tl5-hft-small]] (b) and of [[lem:tl5-hft-products]] hold; and the terms with ϱ(p) of
[[eq:tl5-hfs-products]] hold with μ^((1−θ)n/2) ν^(−1/2) 𝔠^♮_n(ν) in place of μ^(n/2) 𝔠^♮_n and with μ^((n−|J|)/2)
μ^((1−θ)|J|/2) ν^(−1/2) (𝔠^♮_(|J|)(ν) + 1) in place of μ^(n/2) (𝔠^♮_(|J|) + 1).

*Proof.* As k₃^♮(·) is nondecreasing and μ ≤ ν, 𝔰 ≤ 1/(2 sup k₃^♮(μ)); so [[lem:tl5-hft-small]] (b) and
[[lem:tl5-hft-products]] apply. We prove [[eq:tl5-hfq-m2]] by induction on |C|, as [[eq:tl5-hfs-m2]] is proved in
[[lem:tl5-hfs-linfty]], with R_C := 2(k₁^(j,μ) + 1) μ^(−(|C|+1)/2) 𝒥_g + 2k₂ ν^(−(|C|+1)/2) ϱ(p). The linear part is at
most k₁^(j,μ) μ^(−(|C|+1)/2) 𝒥_g + k₂ ϱ(p), and k₂ ϱ(p) ≤ k₂ ν^(−(|C|+1)/2) ϱ(p). In a nonlinear monomial whose
background factors carry b letters, the factor Φ bounded there by 𝔧 is H, Ψ_(C′) or D̂Ψ_(C′) with |C′| ≤ |C| − b, at
most 2μ^(b/2) μ^(−(|C|+1)/2) 𝒥_g, or D̂²Ψ_(C′) with |C′| ≤ |C| − b and |C′| < |C|, at most μ^(b/2) times the part of
R_C with 𝒥_g plus ν^(b/2) times its part with ϱ(p), by the induction hypothesis; the terms H^(αβ) D̂_αD̂_βΨ_J, |J| < |C|,
are of the same kind with b = 0, and the couplings 𝔔_CJ carry μ^((|C|−|J|)/2) ≤ ν^((|C|−|J|)/2). By
[[eq:tl5-hfs-sum]] with ν′ = μ and ν′ = ν, the nonlinear part is at most 𝔰 k₃^♮(μ) (2μ^(−(|C|+1)/2) 𝒥_g + the part of
R_C with 𝒥_g) + 𝔰 k₃^♮(ν) (the part of R_C with ϱ(p)), and 𝔰 k₃^♮(ν) ≤ 1/2 closes the induction.

For [[eq:tl5-hfq-small]] let a_Φ := μ^(−(o+2)/2) and r_Φ := ν^(−(o+2)/2) for a low quantity Φ of order o (with a factor 2
for H, as |H| ≤ 2|h|). The steps of the proof of [[lem:tl5-hft-small]] (a), with [[eq:tl5-hfq-m2]] in place of
[[eq:tl5-hfs-m2]], give for each Φ a bound |Φ(p)| ≤ a_Φ 𝔈 + r_Φ ℜ + 𝔫_Φ, where 2𝔈 := μ^(N/2)·(the part of the right side
of [[eq:tl5-hfq-small]] with ℰ_g) and 2ℜ := ν^(N/2)·(its part with ϱ and η₀) are formed from the linear terms of those
steps: for D̂Ψ_B the part with ϱ of D̂²Ψ_(JB) on the face is at most 2k₂ ν^(−(|B|+3)/2) ϱ(p); for D̂²Ψ_B the jets of the
recovery carry the weights of [[lem:tl5-hfs-linfty]] with μ in their parts with ℰ_g and with ν in their parts with ϱ(p)
and η₀(p), which gives k₁^(N−4,μ) and k₁^(N−4,ν); the parts with η₀(p) of Ψ_B and D̂Ψ_B are bounded unweighted, and 1 ≤
r_Φ. Here 𝔫_Φ = 0 unless Φ = D̂²Ψ_B, and then 𝔫_Φ is the nonlinear part, whose factor Φ′ of largest order is a low
quantity with a_(Φ′) ≤ μ^(b/2) a_Φ and r_(Φ′) ≤ ν^(b/2) r_Φ, b the letters on the background factors. With t :=
max_Φ |Φ(p)|/(a_Φ 𝔈 + r_Φ ℜ), [[eq:tl5-hfs-sum]] gives 𝔫_Φ ≤ t 𝔰 (k₃^♮(μ) a_Φ 𝔈 + k₃^♮(ν) r_Φ ℜ) ≤ (t/2)(a_Φ 𝔈 + r_Φ ℜ);
so t ≤ 1 + t/2, t ≤ 2, and max_Φ a_Φ ≤ μ^(−N/2), max_Φ r_Φ ≤ ν^(−N/2) give [[eq:tl5-hfq-small]].

In the proof of [[lem:tl5-hfs-products]] a factor Φ₂ = D̂²Ψ_C has, by [[eq:tl5-hfq-m2]], its part with ϱ(p) at most
2k₂ ν^(−ℓ_E(Φ₂)/2) ϱ(p); so the term with ϱ(p) of a monomial with b background letters is at most ν 𝔰^(q−1) μ^(n/2)
ν^(−ℓ_E(Φ₂)/2) 2k₂ ϱ(p), and ℓ_E(Φ₂) ≤ n − b + 1 for b ≥ 1, ℓ_E(Φ₂) ≤ n for b = 0, give μ^(n/2) ν^(−ℓ_E(Φ₂)/2) ≤
μ^((1−θ)n/2) ν^(−1/2) ν^(b/2); [[eq:tl5-hfs-sum]] with ν′ = ν gives the first replacement, and the term H^(αβ)
D̂_αD̂_βΨ_J, |J| < n, the second. ∎

**Lemma {#lem:tl5-hfq-mixed}** (Three constants of level four.) In the setting of [[lem:tl5-hfs-mixed]], with 𝔰 ≤
𝔰₀^q on Q(t, b), put λ_t^(μ,2) := 2([k₁^(2,μ)]_t + 1) and

    𝔛^q_(1,t) := (𝔭₃ 𝔵₃(t) (1 + [ϖ₁]_t))^(1/2),
    𝔛^q_(2,t) := (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (2 [ϖ₂]_t)^(1/2)),      𝔜^q_(1,t) := 𝔱₃(t)^(1/2) (1 + 7λ_t^(μ,2)),

𝔭_r standing for 12 C_(E,r)² with the intrinsic Sobolev constants. Then [[eq:tl5-hfs-mixed]] holds with 𝔛^q_(1,t),
𝔛^q_(2,t) and 𝔜^q_(1,t) in place of 𝔛_(1,t), 𝔛_(2,t) and 𝔜_(1,t).

*Proof.* In the proof of [[lem:tl5-hfs-mixed]], for a rotation word J and a monomial of the remainder R′ of ℒ^J D̂Ψ_B,
the solution factor is Ψ_(σB), σ the subword of J left by the coefficient, and B ↦ σB is injective; so, by Minkowski's
inequality over the monomials and the weights as there, μ² (Σ_(|B|=2) |R′|²)^(1/2) ≤ ρ′_(|J|) 𝒥_g, and summing over J,
μ⁴ Σ_B Σ_J |ℒ^J D̂Ψ_B|² ≤ 2𝒥_g² + 2ϖ₁ 𝒥_g², without the count 49 of the words B. Likewise Z ↦ σZ is injective in the
remainders R of ℒ^J D̂²Ψ_Z, whose solution factors are D̂Ψ_(σZ) or Ψ_(σZ), which removes the count 7 of the fields Z from
their part: μ⁴ Σ_Z Σ_J |ℒ^J D̂²Ψ_Z|² ≤ 602 M_g² + 2ϖ₂ 𝒥_g². In the bound of Y₁ only D̂²Ψ_B with |B| = 2 occurs, and
μ^(3/2) |D̂²Ψ_B| ≤ M_g^(2) ≤ 2(k₁^(2,μ) + 1) 𝒥_g + 2k₂ ϱ by [[lem:tl5-hft-small]] (b); so ‖M_g^(2)‖_Σ ≤ λ_t^(μ,2) 𝔍_g +
ς_t ϱ takes the place of the bound of ‖M_g‖_Σ there. The rest of that proof holds as written. ∎

**Definition {#def:tl5-hfq-constants}** (The constants at level four sharpened a fourth time.) Let N = 4 and the
setting be that of [[def:tl5-hfs-constants]], with its constants formed with the chosen Sobolev constants; fix θ ∈
[0, 1] and put ν := μ^θ, 𝔰₀^q as in [[lem:tl5-hfq-theta]] with the supremum over D^κ, 𝔰₁^q := min(𝔰₀^q/2, c_* κ_m/2,
𝔰_θ), and, with the notation of [[lem:tl5-hfs-mixed]] and [[lem:tl5-hfq-mixed]],

    𝔤_(ϱ,q) := ν^(−1/2) (Σ_(j≤4) (Σ_(j′≤j) μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(ν) + 1))²)^(1/2),
    ε_(w,q) := 𝒮[s₄[2R̂ic] + (1/4) min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) k₂ ϱ],
    S_(M,q) := μ^(−3/2) ∫_(−10)^(u*) w_t (𝔠^Mq₁ 𝔛^q_(1,t) 𝔜^q_(1,t) + 𝔠^Mq₂ 𝔛^q_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_(M,q) := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) (𝔠^Mq₁ 𝔛^q_(1,t) (𝔜′_(1,t) ϱ + 𝔜″_(1,t) η₀)
               + 𝔠^Mq₂ (𝔛^q_(2,t) 𝔜″_(2,t) η₀ + 𝔛′_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_(M,q) := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t 𝔠^Mq₂ 𝔛′_(2,t) 𝔜″_(2,t) dt,
    A_q := √2 δ_w + 2ε_(w,q) + 2ε_(M,q),      B_q := 2 (S_(F,s) + S_(M,q)),      𝔯_q := 𝔯_(w,s) + 𝔯_(M,q),
    𝔰_(*,q) := sup_(p∈D^κ) (2 C_(∞,μ)^(0)(p) μ^(−2) e^(φ(p)/2) A_q
               + ν^(−2) (C_((∞,ϱ),ν)^(0)(p) ϱ(p) + C_((∞,0),ν)^(0)(p) η₀)).                       {#eq:tl5-hfq-constants}

**Proposition {#prop:tl5-hfq-bootstrap}** (The a priori estimate at level four, sharpened a fourth time.) In the
setting of [[def:tl5-hfq-constants]], suppose that the rates a_o, a_i are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴) and
that 𝔯_q ≤ 1/4, η₀ < 𝔰₁^q and 𝔰_(*,q) < 𝔰₁^q. Let g be a solution of the reduced problem on D^κ_s with Y_σ(g) ≤ 2A_q for
every σ ∈ [1/2, s]. Then 𝔰 ≤ 𝔰_(*,q) on D^κ_s; in particular |h|_k̂ < κ_m/2 there, and

    Y_s(g) ≤ A_q + B_q Y_s(g)².                                                                          {#eq:tl5-hfq-h1}

*Proof.* Step 1 is that of the proof of [[prop:tl5-hft-bootstrap]] with 𝔰₀^q, 𝔰₁^q, A_q, 𝔰_(*,q) and [[eq:tl5-hfq-small]]
in place of the quantities of option (b), as 𝔰₁^q ≤ 𝔰₀^q/2: it gives 𝔰 ≤ 𝔰_(*,q) < 𝔰₁^q on D^κ_s, |h|_k̂ < κ_m/2 and θ_H
≤ ϑ. Steps 2 and 3 are those of option (b) there, by [[lem:tl5-hfq-theta]], with two changes. The terms with ϱ of the
family of level j are bounded either as there or by [[lem:tl5-hfq-theta]], which gives μ^(−j/2) ν^(−1/2) Σ_(j′≤j)
μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(ν) + 1) 2k₂ 𝔰 ϱ and, with the weights μ^|I|, the contribution 2Ω̂² (1/4) 𝔤_(ϱ,q)
k₂ ϱ (√e_o + √c √e_i); either bound may be used, which gives ε_(w,q). The terms 𝔑^M_I are bounded as in the proof of
[[prop:tl5-hfs-bootstrap]] with [[eq:tl5-hfq-m]] and [[lem:tl5-hfq-mixed]] in place of [[eq:tl5-hfs-m]] and of the
constants 𝔛_(1,t), 𝔛_(2,t), 𝔜_(1,t) of [[lem:tl5-hfs-mixed]], which gives S_(M,q) Y_s³ + 𝔯_(M,q) Y_s² + ε_(M,q) Y_s. So
(1 − ϑ) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε_(w,q) + ε_(M,q)) + 𝔯_q Y_s² + (S_(F,s) + S_(M,q)) Y_s³, and the conclusion
follows as there. ∎

**Theorem {#thm:tl5-hf4q}** (Level four, with the constants sharpened a fourth time.) In the setting of
[[thm:tl5-hf4t]], with θ and the choices of [[def:tl5-hfq-constants]], suppose: (a) η₀ < 𝔰₁^q; (b) the rates a_o, a_i
are admissible for ((1 − ϑ)⁻¹ 𝔅₄, E_o⁴, E_i⁴); (c) 𝔯_(w,s) + 𝔯_(M,q) ≤ 1/4, 𝔰_(*,q) < 𝔰₁^q and the closing condition

    4 A_q B_q = 8 (√2 δ_w + 2ε_(w,q) + 2ε_(M,q)) (S_(F,s) + S_(M,q)) < 1.                          {#eq:tl5-hf4q-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_q and 𝔰_(*,q) in place of A_(w,4) and 𝔰_*.

*Proof.* The proof of [[thm:tl5-hf4t]] in option (b) applies with A_q, B_q, 𝔰_(*,q), 𝔰₁^q, [[prop:tl5-hfq-bootstrap]],
[[eq:tl5-hfq-h1]] and [[eq:tl5-hf4q-closing]] in place of A_t, B_t, 𝔰_(*,t), 𝔰₁^t, [[prop:tl5-hft-bootstrap]],
[[eq:tl5-hft-h1]] and [[eq:tl5-hf4t-closing]]: it uses 𝔰 ≤ 𝔰_(*,q) < 𝔰₁^q ≤ min(1/16, 𝔰_θ), the bound Y_σ ≤ 2A_q and the
bound of M_g^(3) of [[lem:tl5-hft-small]] (b), which holds as 𝔰 ≤ 1/(2 sup k₃^♮(μ)). ∎

**Remark {#rem:tl5-hfq-what}** (What the fourth sharpening changes.) The products of level four with no factor at a
point carry 𝔠^Mq₁ = 480 + 96 𝔤₁ (𝔤₀ + √5) 𝔰_♭ and 𝔠^Mq₂ = 4 + 4 𝔤₁ 𝔰_♭ (2 + 𝔤₁ 𝔰_♭), in place of 49 𝔰_♭ [𝔠^(3♮)₄]_t
added to 480 and 4. The number θ moves the threshold and the requirements on ϱ and η₀ together: 𝔰₁^q is formed with
k₃^♮(μ^θ), and the terms with ϱ and η₀ of 𝔰_(*,q) carry μ^(−2θ); θ = 0 gives the threshold of option (a) of
[[def:tl5-hft-constants]] with μ⁰ on these terms, and θ = 1 option (b). The factor μ^(−2) of the term with A_q
remains for the reason given in [[rem:tl5-hft-what]]. In 𝔜^q_(1,t) the recovery constant is that of level two, and
𝔛^q_(1,t), 𝔛^q_(2,t) carry no count of the words B and of the fields Z in their parts with ϖ₁ and ϖ₂. As for
[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hf4q]] are established in this paper for no
background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
The sections sec:tl5-hf, sec:tl5-hf4, sec:tl5-hfg, sec:tl5-hfs and sec:tl5-hft stay as they are, and all their closing
conditions remain valid; this section is added beside them. Old texts are quoted exactly from chapters/87-ten-l5.md at
HEAD 8e7dd529, where sec:tl5-hft is merged (87:5760–5977, merge 1b8a7d43). Line numbers serve only to find the place.
Each new text replaces its old text as a whole, with the line breaks shown.

*1. Where the section goes.* The section above, from its heading ("The constants at level four sharpened a fourth time",
label sec:tl5-hfq) through the last line of [[rem:tl5-hfq-what]], is inserted at the end of [[ch:ten-l5]], after the
last line of [[rem:tl5-hft-what]] (line 5977, as changed by item 2), with one blank line before it, as a sibling "###"
section after sec:tl5-hft. It cites results of the earlier sections as they stand and the proofs of
prop:tl5-hft-bootstrap, prop:tl5-hfs-bootstrap and thm:tl5-hf4t with the replacements it states. It defines the
labels listed in the crosswalk rows, none defined elsewhere. No number already printed changes.

*2. The last sentence of [[rem:tl5-hft-what]] (lines 5976–5977).* Old:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hft]] and [[thm:tl5-hf4t]] are established in this
paper for no background at 10 l5.

New:

[[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hft]] and [[thm:tl5-hf4t]] are established in this
paper for no background at 10 l5. [[sec:tl5-hfq]] sharpens the constants at level four a fourth time
([[thm:tl5-hf4q]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. "Proved" refers to the section above; "deduced" marks statements about the method that no proof here
establishes; "computed" marks numbers I evaluated (floating point).

*Closing condition and smallness at level four (proved), for each θ ∈ [0, 1]:*

    8 (√2 δ_w + 2ε_(w,q) + 2ε_(M,q)) (S_(F,s) + S_(M,q)) < 1,   𝔯_(w,s) + 𝔯_(M,q) ≤ 1/4,
    η₀ < 𝔰₁^q,   𝔰_(*,q) < 𝔰₁^q                                                              (thm:tl5-hf4q)

S_(F,s) and 𝔯_(w,s) are those of def:tl5-hfs-constants with the chosen Sobolev constants, as in option (b) of
def:tl5-hft-constants (valid under the weighted absorption, lem:tl5-hft-products). The earlier conditions stay valid.

*Every new factor, as a formula (N = 4, ν := μ^θ).*

    𝔠^Mq₁ = 480 + 96 𝔤₁ (𝔤₀ + √5) 𝔰_♭,   𝔠^Mq₂ = 4 + 4 𝔤₁ 𝔰_♭ (2 + 𝔤₁ 𝔰_♭),   𝔤₁ = 1 + 2𝔰_♭,   𝔤₀ = √5 + 1/4
        (computed: at 𝔰_♭ = 10⁻¹⁰ these are 480 and 4 to nine digits; at 𝔰_♭ = 1/8, 550.8 and 5.35);
    k₃^♮(ν) = (8/5) max_(|C|≤3) (𝔠^♮_(|C|)(ν) + Σ_(J≠C) ν^((|C|−|J|)/2) ‖𝔔_CJ‖ (𝔠^♮_(|J|)(ν) + 1));
    𝔰₀^q = min(𝔰_♭, 1/(2 sup_(D^κ) k₃^♮(ν))),   𝔰₁^q = min(𝔰₀^q/2, c_* κ_m/2, 𝔰_θ);
    𝔰_(*,q) = sup_p (2 C_(∞,μ)^(0) μ^(−2) e^(φ/2) A_q + ν^(−2) (C_((∞,ϱ),ν)^(0) ϱ + C_((∞,0),ν)^(0) η₀)),
        C_(∞,μ)^(0) = 2 max(2C_S, C₁^♮(μ), 4 k₁^(0,μ) max(C_S, C₁^♮(μ))),
        C_((∞,ϱ),ν)^(0) = 2 max(C_(1,ϱ), 4 k₁^(0,ν) C_(1,ϱ) + k₂),
        C_((∞,0),ν)^(0) = 2 max(2C_(0,0), C_(1,0)^♮(ν), 4 k₁^(0,ν) max(C_(0,0), C_(1,0)^♮(ν))),
        (2𝔐^(0))^(1/2) = 4; C₁^♮(ν), C_(1,0)^♮(ν): C₁, C_(1,0) with Λ₂^ν = max(νΛ₁, ν^(3/2)Λ₂) and k₁^(3,ν);
        k₁^(j,ν) = (6/5)((√3 + 8/3) K_rec (1 + ν^(1/2) √7 (3 max|D̂Z| + 2 max|D̂²Z|)) + ν^(1/2) 𝔯₀ + (4/3) α_𝔄^(j,ν)),
        α_𝔄^(j,ν) = √2 max_(|C|≤j) Σ_J ν^((|C|+1−|J|)/2) ‖𝔄_CJ‖; k₁^(0,ν) has α_𝔄^(0,ν) = 0;
    𝔤_(ϱ,q) = ν^(−1/2) (Σ_(j≤4) (Σ_(j′≤j) μ^((j−θj′)/2) 𝔮_(jj′) 7^(j′/2) (𝔠^♮_(j′)(ν) + 1))²)^(1/2);
    ε_(w,q) = 𝒮[s₄[2R̂ic] + (1/4) min(𝔤_(ϱ,q), μ^(−1/2) 𝔤_(𝒥,s)) k₂ ϱ];
    λ_t^(μ,2) = 2([k₁^(2,μ)]_t + 1);  𝔛^q_(1,t) = (𝔭₃ 𝔵₃(t)(1 + [ϖ₁]_t))^(1/2);
    𝔛^q_(2,t) = (𝔭₄ 𝔵₄(t)/2)^(1/2) (√602 λ_t^μ + (2[ϖ₂]_t)^(1/2));  𝔜^q_(1,t) = 𝔱₃(t)^(1/2)(1 + 7λ_t^(μ,2));
        (𝔭_r → 12 C_(E,r)², 𝔳 → 𝔳₀, 𝔴 → 𝔴₀ with the intrinsic Sobolev constants; ϖ₁, ϖ₂, 𝔛′_(2,t), 𝔜′_(1,t),
        𝔜″_(1,t), 𝔜_(2,t), 𝔜″_(2,t), w_t, ς_t as in sec:tl5-hfs);
    S_(M,q) = μ^(−3/2) ∫ w_t (𝔠^Mq₁ 𝔛^q₁ 𝔜^q₁ + 𝔠^Mq₂ 𝔛^q₂ 𝔜₂) [𝔨₂]_t dt;
    𝔯_(M,q) = μ^(−3/2) ∫ w_t [𝔨₂]_t^(1/2) (𝔠^Mq₁ 𝔛^q₁ (𝔜′₁ϱ + 𝔜″₁η₀) + 𝔠^Mq₂ (𝔛^q₂ 𝔜″₂ η₀ + 𝔛′₂ 𝔜₂ ϱ)) dt;
    ε_(M,q) = μ^(−3/2) ϱ η₀ ∫ w_t 𝔠^Mq₂ 𝔛′₂ 𝔜″₂ dt;
    A_q = √2 δ_w + 2ε_(w,q) + 2ε_(M,q),  B_q = 2(S_(F,s) + S_(M,q)),  𝔯_q = 𝔯_(w,s) + 𝔯_(M,q).

*The briefed items.*

1. 𝔠^M (proved, beyond the weighting asked for). The terms of R₃ in 𝔑^M_I are enumerated: b = 0 there, so a weighting
   of the background letters cannot act on them (deduced: G0f's hypothetical (iii) weights a constant whose b > 0
   monomials are not in 𝔑^M at all), but most monomials of 𝔠^(3♮)₄ are not in 𝔑^M; those that are carry the factor 𝔰
   (two h's or H) and admit the exact count over the words. So 49 𝔰_♭ [𝔠^(3♮)₄]_t (10^5.0–8.0 at G0f's optimum) becomes
   96 𝔤₁ (𝔤₀ + √5) 𝔰_♭ ≤ 71, and 𝔠^Mq₁ ≤ 551 for every 𝔰_♭ ≤ 1/8 (computed); 𝔰_♭ no longer needs to be small for 𝔠^M.
2. The ϱ requirement (proved: a one-parameter family). lem:tl5-hfq-theta weights the parts with ℰ_g by μ and those with
   ϱ, η₀ by ν = μ^θ, absorbing each with its own constant k₃^♮(μ), k₃^♮(ν); the binding threshold is k₃^♮(ν). θ = 0 is
   option (a) (threshold k₃^♮(1), μ⁰ on ϱ and η₀), θ = 1 option (b) (threshold k₃^♮(μ), μ^(−2) on ϱ and η₀). The ϱ part
   of D̂²Ψ_C now carries ν^(−(|C|+1)/2), which is the power it carries through the background letters of the
   nonlinear terms: that is what lets k₃^♮(ν) absorb it. A hybrid with (b)'s threshold and (a)'s requirement is not
   given by this proof (deduced): the ϱ part of a factor D̂²Ψ_(C′) in a nonlinear term of level |C| enters with the
   background letters' norm Λ_b and gains ν^(b/2) only through the power ν^(−(|C′|+1)/2) it carries, so a threshold
   formed with weight μ forces ν = μ on it. What θ buys: the threshold k₃^♮(μ^θ) against μ^(−2θ) on ϱ and η₀ (and
   ν^(−1/2) μ^((j−θj′)/2) in 𝔤_(ϱ,q)); the evaluation can optimize θ per case.
3. The rest of S_M (proved where stated). 𝔜₁: the recovery constant of level two, λ_t^(μ,2), in place of the top-level
   λ_t^μ (G0f's 2.1 decades sit in 1 + 7λ_t^μ; how much of k₁^μ is the level-three coupling is for the evaluation). 𝔛₁:
   1 + ϖ₁ in place of 1 + 49ϖ₁ (up to 0.85 decades). 𝔛₂: 2ϖ₂ in place of 14ϖ₂ in its second part. Not done: [𝔨₂]_t,
   𝔪(t) and [2Ω̂²(1 + c/κ′)^(1/2)]_t are face suprema taken out of integrals over the face; keeping them inside needs a
   weighted form of the Hölder inequality of lem:tl5-hf4-face (c) with the weights in the integrand, and was not
   carried out. The 602 = 2 · 7 · 43 in 𝔛₂ stays: it counts second derivatives bounded by their maximum M_g, and an
   ℓ² count needs an ℓ² recovery.
4. 𝔰₁ at level 4: changes only through θ.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfq	paper/reader/proofs/P-GRD4.md@PENDING:1	P-GRD4, section	new; at the end of ch:ten-l5, after rem:tl5-hft-what (author: keep tightening by hand); fourth sharpening at level 4
    lem:tl5-hfq-m	paper/reader/proofs/P-GRD4.md@PENDING:15	P-GRD4, Lemma	products with no point factor at level 4 counted exactly also in R3: coefficients 480 + 96 g1 (g0 + sqrt5) s_flat and 4 + 4 g1 s_flat (2 + g1 s_flat)
    eq:tl5-hfq-m	paper/reader/proofs/P-GRD4.md@PENDING:19	P-GRD4, display	new
    lem:tl5-hfq-theta	paper/reader/proofs/P-GRD4.md@PENDING:38	P-GRD4, Lemma	absorption weighted in two parts (mu for the energies, mu^theta for rho and eta0); family between options (a) and (b)
    eq:tl5-hfq-m2	paper/reader/proofs/P-GRD4.md@PENDING:43	P-GRD4, display	new
    eq:tl5-hfq-small	paper/reader/proofs/P-GRD4.md@PENDING:48	P-GRD4, display	new
    lem:tl5-hfq-mixed	paper/reader/proofs/P-GRD4.md@PENDING:83	P-GRD4, Lemma	X1 without the count 49, X2 without the count 7 in its remainder part, Y1 with the level-2 recovery constant
    def:tl5-hfq-constants	paper/reader/proofs/P-GRD4.md@PENDING:101	P-GRD4, Definition	fourth sharpened constants at level 4: s0^q, s1^q, g_(rho,q), eps_(w,q), S_(M,q), r_(M,q), eps_(M,q), A_q, B_q, s_(*,q)
    eq:tl5-hfq-constants	paper/reader/proofs/P-GRD4.md@PENDING:114	P-GRD4, display	new
    prop:tl5-hfq-bootstrap	paper/reader/proofs/P-GRD4.md@PENDING:116	P-GRD4, Proposition	(H1) at level 4 with the fourth sharpened constants
    eq:tl5-hfq-h1	paper/reader/proofs/P-GRD4.md@PENDING:121	P-GRD4, display	new
    thm:tl5-hf4q	paper/reader/proofs/P-GRD4.md@PENDING:134	P-GRD4, Theorem	thm:tl5-hf4 with the fourth sharpened constants; theta in [0,1]
    eq:tl5-hf4q-closing	paper/reader/proofs/P-GRD4.md@PENDING:138	P-GRD4, display	closing condition at level 4: 8 (sqrt2 delta_w + 2 eps_(w,q) + 2 eps_(M,q)) (S_(F,s) + S_(M,q)) < 1
    rem:tl5-hfq-what	paper/reader/proofs/P-GRD4.md@PENDING:147	P-GRD4, Remark	what the fourth sharpening changes

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hft-what, add "; points to sec:tl5-hfq
(P-GRD4 item 2)".
