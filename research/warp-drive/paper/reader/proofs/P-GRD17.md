### The second derivatives at low levels word by word, through the map of the recovery {#sec:tl5-hfn}

This section makes one change, at the levels N ≥ 6. In the step on second derivatives at low levels
([[lem:tl5-hfp-low]]) the bound of D̂²Ψ_B(p), |B| ≤ m, is the recovery of Ψ_B at p. Its linear part consists of the
leading term, through the first derivatives of the seven words ZB, Z ∈ Γ; the terms with 𝔷_Z and with 𝔯_♯, through D̂Ψ_B
and Ψ_B; and the couplings 𝔄_BJ, through the jets of words J of length at most |B| that the substitutions of
[[def:tl5-hf-coupling]] bring in. The step bounds all these jets together by the norm L_g of the jets of all the words
of length at most m + 1, so that its constant k₁^(m,μ,p) 𝔐_p^(m) counts the families of all 7^b words of each length b ≤
m + 1. But 𝔰_g^(m) is the largest of its quantities, and the bound of each D̂²Ψ_B needs only the jets of its own
recovery. So we bound, for each word B, the leading term through the family of the seven words ZB alone, by the
first-order bound of [[lem:tl5-hfp-c1]] for that family and through the image under the map 𝒳_p of [[lem:tl5-hfk-rec]],
as [[lem:tl5-hfk-fam]] does at level four for the seven fields ([[lem:tl5-hfn-fam]]); the terms with 𝔷_Z, with the
weights of their fields as in [[eq:tl5-hfk-rec]], and with 𝔯_♯ through the bounds of D̂Ψ_B and Ψ_B of the one word B;
and only the couplings through L_g ([[lem:tl5-hfn-low]]). The constant 𝔐_n^(m) so formed takes the place of k₁^(m,μ,p)
𝔐_p^(m) in the part with ℰ_g of the bounds at a point, the parts with ϱ and η₀ being kept, and so enters C_P^♮, through
it the closing condition, and the term of 𝔰_* with A ([[def:tl5-hfn-constants]], [[thm:tl5-hfn]]). The closing condition
is [[eq:tl5-hfn-closing]]; every new constant is at most the one it replaces, and the earlier closing conditions remain
valid. The notation is that of [[sec:tl5-hfk]].

**Lemma {#lem:tl5-hfn-fam}** (The seven words ZB through the map of the recovery.) Let N ≥ 6, let the setting be that of
[[lem:tl5-hfp-low]], with 𝔰 ≤ 𝔰₁^v on Q(a, b) and the constants with index l, and let 𝒳_p, |·|_Γ and 𝔨_Γ be as in
[[lem:tl5-hfk-rec]], formed with the numbers |T(p)|, λ_M(p) and c^ab_j(p) of the point p. For a word B with |B| ≤ N − 4
let ΓB be the family of the seven words ZB, Z ∈ Γ, which are distinct and have the length |B| + 1 ≤ N − 3. At each point
of Σ₁(a, b) let 𝔞_𝔄^k(ΓB) be the operator norm of the map that defines 𝔞_𝔄(ΓB) in [[def:tl5-hfp-constants]], its
components of the pairs (J, TB) multiplied by |T(p)|⁻¹ and those of the pairs (J, K_ab B) by λ_M(p)^(−1/2). Let
C₁^k(ΓB)(p) be K_rec(p) times the constant C₁^l(ΓB)(p) of [[eq:tl5-hfe-constants]] formed with 43^(1/2) 𝔨_Γ/K_rec(p) in
place of 301^(1/2), the count (43 · 7)^(1/2) of the family, and with 𝔞_𝔄^k(ΓB)/K_rec(p) in place of 𝔞_𝔄(ΓB), in 𝔩_D(ΓB)
and 𝔩_J(ΓB) at every point of the face. Then

    |𝒳_p (D̂Ψ_(ZB)(p))_(Z∈Γ)| ≤ μ^(−(|B|+4)/2) C₁^k(ΓB) ℰ_g(p)^(1/2) + 𝔨_Γ (w C_(1,ϱ)^l ϱ(p) + E₀),    {#eq:tl5-hfn-fam}

with w and the part E₀ with η₀ as in [[lem:tl5-hfp-c1]] for 𝔚 = ΓB. Moreover 𝔞_𝔄^k(ΓB) ≤ K_rec(p) 𝔞_𝔄(ΓB) and C₁^k(ΓB) ≤
K_rec(p) C₁^l(ΓB).

*Proof.* Let A_Z := D̂Ψ_(ZB) for Z ∈ Γ. The proof of [[lem:tl5-hfk-fam]] applies with these A_Z, with the family ΓB in
place of Γ in [[lem:tl5-hfp-c1]] and [[lem:tl5-hfp-words]], with the pairs (J, ZB) and the words JZB, Z′JZB and σZB in
place of the pairs (J, Z) and the words JZ, Z′JZ and σZ, σ being the subword of J that a monomial of a remainder leaves,
and with the factors μ^(|B|+4) and μ^(−(|B|+4)/2) in place of μ⁴ and μ^(−2). That proof uses of the family Γ and of N =
4 only the following, which hold here at every level N ≥ 6. The fields Ã₀ := |T(p)|⁻¹ A_T and Ã_j := Σ_(a<b) c^ab_j(p)
A_(K_ab), j = 2, 3, 4, are combinations of the A_Z with constant coefficients, so Σ_i |Ã_i(p)|² = |𝒳_p (A_Z(p))_Z|², and
by [[lem:tl5-hf-fields]] (a) at p, applied to the tensors at each point, Σ_i |ℒ^J Ã_i|² ≤ |(|ℒ^J A_Z|)_Z|_Γ² and
Σ_i |D̂ℒ^J Ã_i|² ≤ |(|D̂ℒ^J A_Z|)_Z|_Γ² at every point of the face and of S_a, for every word J. [[lem:tl5-hfp-c1]]
holds for the family ΓB, in the form that the proof of [[thm:tl5-hfe]] gives it, as its words are distinct and have one
length at most N − 3. The bounds of its proof for each pair are of the three kinds of the proof of [[lem:tl5-hfk-fam]].
(i) The bounds of the leading terms D̂Ψ_(JZB), of the remainders R′_(J,ZB) and D̂R′_(J,ZB), and, in the bound of
D̂²Ψ_(JZB) by [[lem:tl5-hfz-rec]] at the point of the face, of its leading term through the words Z′JZB and of its terms
with 𝔷_(Z′) and with 𝔯_♯ |Ψ_(JZB)|: they form over the pairs a family whose Euclidean norm the proof bounds through 𝒟_g
or 𝒥_g, as the words JZB, the words Z′JZB and, for each σ, the words σZB are distinct for distinct indices; by
[[lem:tl5-hfk-rec]] (a) each of these parts is at most K_rec(p) times its bound there. (ii) The bounds u_J that do not
depend on Z: those of the nonlinear part and of the part with ϱ of the bound of D̂²Ψ_(JZB), which by the proof of
[[lem:tl5-hfp-words]] depend only on J and on the length of JZB, and on S_a the bound of ℒ^J A_Z that the step uses for
every J; for a family y of numbers over the pairs with y_(J,Z) = u_J, the weighted norm |y|_Γ :=
(Σ_J |(y_(J,Z))_Z|_Γ²)^(1/2) of that proof is 𝔨_Γ (Σ_J u_J²)^(1/2), where the Euclidean norm is √7 (Σ_J u_J²)^(1/2).
(iii) The terms with 𝔄, whose family over the pairs, multiplied by 𝔬_J and weighted, has the norm |·|_Γ at most (1 −
𝔰₁^v)⁻¹ 𝔞_𝔄^k(ΓB) 𝒥_g, by the definition of 𝔞_𝔄^k(ΓB) and Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g². So the rest of the proof
of [[lem:tl5-hfk-fam]] gives [[eq:tl5-hfn-fam]], with C₁^k(ΓB) in its part with ℰ_g and with 𝔨_Γ in place of the factor
√7 of the parts with ϱ(p) and η₀ of [[eq:tl5-hfp-family]]. The last claims follow as there: the map that defines
𝔞_𝔄^k(ΓB) is that defining 𝔞_𝔄(ΓB) followed by the multiplication of its components by numbers at most K_rec(p), so
𝔞_𝔄^k(ΓB) ≤ K_rec(p) 𝔞_𝔄(ΓB); 43^(1/2) 𝔨_Γ/K_rec(p) ≤ 301^(1/2) by [[lem:tl5-hfk-rec]] (a); and the functions in
C₁^(U,l)(ΓB), C₁^(D,l)(ΓB) and C₁^(J,l)(ΓB) are nondecreasing in that count and in 𝔞_𝔄(ΓB), as k₁^p ≥ k₁^D, so
C₁^k(ΓB) ≤ K_rec(p) C₁^l(ΓB). ∎

**Lemma {#lem:tl5-hfn-low}** (The step at low levels, word by word.) Let N ≥ 6, let the setting be that of
[[lem:tl5-hfp-low]], with 𝔰 ≤ 𝔰₁^v on Q(a, b) and the constants with index f, and let 0 ≤ m ≤ N − 4. For a word B
with |B| ≤ m put, at p, with 𝔷₁^k and 𝔷₂^k as in [[lem:tl5-hfk-rec]], C₁^k(ΓB) as in [[lem:tl5-hfn-fam]], C₁^l({B}) as
in [[eq:tl5-hfe-constants]], C_S^f as in [[lem:tl5-hff-zero]] and α_𝔄^(m,μ) as in [[def:tl5-hfs-bounds]],

    𝔨_rec^n(B) := 𝔨_♯ (C₁^k(ΓB) + 𝔷₁^k μ^(1/2) C₁^l({B}) + 𝔷₂^k μ C_S^f) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^f,
    𝔐_n^(m) := max_(|B|≤m) 𝔨_rec^n(B) + (1 − 𝔰₁^v)⁻¹ α_𝔄^(m,μ) 𝔐_p^(m),                                {#eq:tl5-hfn-low}

for B = ∅ with C_S^h of [[lem:tl5-hff-zero]] in place of C_S^f, and with 𝔐_p^(m) in its form with index f. Then the step
on second derivatives at low levels of the lemma in use holds with 𝔐_n^(m) in place of k₁^(m,μ,p) 𝔐_p^(m) in its part
with ℰ_g, its parts with ϱ and η₀ being as they are. Moreover 𝔐_n^(m) ≤ k₁^(m,μ,p) 𝔐_p^(m), and C₁^l(𝔚′) ≤ C₁^l(𝔚) for
families 𝔚′ ⊂ 𝔚 of words of one length.

*Proof.* Let |B| ≤ m. In the step, the bound of D̂²Ψ_B(p) is the recovery of Ψ_B at p with 𝔥 = 𝔰₁^v, as |H(p)| ≤ 𝔰(p) ≤
𝔰₁^v, with 𝔣 = Σ_J 𝔄_BJ(D̂Ψ_J, Ψ_J) + Σ_J 𝔔_BJ ℒ^J(2R̂ic) − 𝔑′_B as in the proof of [[lem:tl5-hfz-words]] (b). Use
[[lem:tl5-hfk-rec]] (b) for it in place of [[lem:tl5-hfz-rec]]. Its linear part consists of the leading term 𝔨_♯ |𝒳_p
(D̂Ψ_(ZB)(p))_Z|, as ℒ_ZΨ_B = Ψ_(ZB); the terms 𝔨_♯ (𝔷₁^k |D̂Ψ_B| + 𝔷₂^k |Ψ_B|) and (1 − 𝔰₁^v)⁻¹ 𝔯_♯ |Ψ_B|, which
involve only the word B; and the couplings (1 − 𝔰₁^v)⁻¹ |Σ_J 𝔄_BJ(D̂Ψ_J, Ψ_J)|, |J| ≤ |B|. The residual and the
nonlinear part are bounded as in the step, by k₂^z ϱ(p) and through the absorption. The step multiplies the bound by
μ^((|B|+4)/2), bounds the jets of the linear part by L_g with the coefficients of k₁^(m,μ,p), and L_g by
[[lem:tl5-hfp-low]]. Let ē_ϱ and ē₀ be the largest of the parts with ϱ(p) and with η₀(p) of the bounds of one jet that
the zeroth- and first-order steps give, with the weights of the step in these parts, and let ν′ := μ, or ν′ := 1 in
[[lem:tl5-hft-small]] (a), whose jets are not weighted in these parts. As in the proof of [[lem:tl5-hfp-low]], the step
bounds the parts with ϱ(p) and η₀(p) of its linear part by k₁^(m,ν′,p) (2𝔐^(m))^(1/2) ē_ϱ and k₁^(m,ν′,p) (2𝔐^(m))^(1/2)
ē₀, and these are its parts with ϱ(p) and η₀(p).

Here we bound the four terms apart, with the weight μ^((|B|+4)/2). By [[eq:tl5-hfn-fam]], μ^((|B|+4)/2) |𝒳_p
(D̂Ψ_(ZB)(p))_Z| is at most C₁^k(ΓB) ℰ_g(p)^(1/2) plus parts with ϱ(p) and η₀(p) at most 𝔨_Γ ē_ϱ and 𝔨_Γ ē₀, as w
C_(1,ϱ)^l ϱ(p) + E₀ is the part with ϱ(p) and η₀(p) of the bound of |D̂Ψ_(ZB)(p)| that the first-order step gives for
the one word ZB, whose weight in the step is μ^((|B|+4)/2). As μ^((|B|+4)/2) = μ^(1/2) μ^((|B|+3)/2) = μ μ^((|B|+2)/2),
the first-order step, by [[lem:tl5-hfp-c1]] with 𝔚 = {B}, and the zeroth-order step, by [[lem:tl5-hff-zero]], bound
μ^((|B|+4)/2) |D̂Ψ_B| by μ^(1/2) C₁^l({B}) ℰ_g(p)^(1/2) and μ^((|B|+4)/2) |Ψ_B| by μ C_S^f ℰ_g(p)^(1/2), with C_S^h for
B = ∅, plus parts with ϱ(p) and η₀(p) at most ν′^(1/2) ē_ϱ and ν′^(1/2) ē₀, and ν′ ē₀. The couplings are bounded as in
the step: their part with ℰ_g by (1 − 𝔰₁^v)⁻¹ α_𝔄^(m,μ) 𝔐_p^(m) ℰ_g(p)^(1/2), through L_g and [[lem:tl5-hfp-low]], and
their parts with ϱ(p) and η₀(p) by (1 − 𝔰₁^v)⁻¹ α_𝔄^(m,ν′) (2𝔐^(m))^(1/2) times ē_ϱ and ē₀. So the part with ℰ_g of the
linear part is at most (𝔨_rec^n(B) + (1 − 𝔰₁^v)⁻¹ α_𝔄^(m,μ) 𝔐_p^(m)) ℰ_g(p)^(1/2) ≤ 𝔐_n^(m) ℰ_g(p)^(1/2), and its parts
with ϱ(p) and η₀(p) are at most

    (𝔨_♯ 𝔨_Γ + 𝔨_♯ ν′^(1/2) 𝔷₁^k + (1 − 𝔰₁^v)⁻¹ α_𝔄^(m,ν′) (2𝔐^(m))^(1/2)) ē_ϱ,
    (𝔨_♯ 𝔨_Γ + 𝔨_♯ (ν′^(1/2) 𝔷₁^k + ν′ 𝔷₂^k) + (1 − 𝔰₁^v)⁻¹ (ν′ 𝔯_♯ + α_𝔄^(m,ν′) (2𝔐^(m))^(1/2))) ē₀.

As 𝔐^(m) ≥ 1 + 7, (2𝔐^(m))^(1/2) ≥ 4; by [[lem:tl5-hfk-rec]] (a), 𝔨_Γ ≤ √7 K_rec and 𝔷₁^k + 𝔷₂^k ≤ K_rec (𝔷₁′ + 𝔷₂′) ≤
√2 K_rec 𝔷′; and ν′ ≤ ν′^(1/2) ≤ 1. So both coefficients are at most k₁^(m,ν′,p) (2𝔐^(m))^(1/2), and these parts are at
most those of the step. In [[lem:tl5-hft-small]] (a), where the step bounds |D̂²Ψ_B(p)| without the weight, the same
bounds, not multiplied by μ^((|B|+4)/2), give the part with ℰ_g with the factor μ^(−(|B|+4)/2) and the parts with ϱ(p)
and η₀(p) with ν′ = 1. As 𝔰_g^(m) is the largest of its quantities, and 𝔐_n^(m) bounds the part with ℰ_g for every B
with |B| ≤ m, this gives the claim.

For the last claims, let 𝔚′ ⊂ 𝔚 be families of words of one length. The map that defines 𝔞_𝔄(𝔚′) is that defining 𝔞_𝔄(𝔚)
followed by the restriction to the components of the pairs (J, C) with C ∈ 𝔚′, of norm at most 1, so 𝔞_𝔄(𝔚′) ≤ 𝔞_𝔄(𝔚);
the functions in C₁^(U,l), C₁^(D,l) and C₁^(J,l) are nondecreasing in the number of the words of the family, through the
counts of the nonlinear parts of 𝔩_D and 𝔩_J, and in 𝔞_𝔄, as k₁^p ≥ k₁^D; so C₁^l(𝔚′) ≤ C₁^l(𝔚). With 𝔚_b as in
[[def:tl5-hfp-constants]], [[lem:tl5-hfn-fam]] and ΓB ⊂ 𝔚_(|B|+1) give C₁^k(ΓB) ≤ K_rec C₁^l(ΓB) ≤ K_rec C₁^l(𝔚_(|B|+1))
≤ K_rec 𝔐_p^(m), as |B| + 1 ≤ m + 1. As {B} ⊂ 𝔚_(|B|), the Cauchy–Schwarz inequality, 𝔷₁^k² + 𝔷₂^k² ≤ K_rec² 𝔷′² by
[[lem:tl5-hfk-rec]] (a), and μ ≤ μ^(1/2) give 𝔷₁^k μ^(1/2) C₁^l({B}) + 𝔷₂^k μ C_S^f ≤ μ^(1/2) K_rec 𝔷′ (C₁^l(𝔚_(|B|))² +
C_S^f²)^(1/2) ≤ μ^(1/2) K_rec 𝔷′ 𝔐_p^(m), the two numbers in the root being terms of 𝔐_p^(m) with b = |B| (with C_S^h
for B = ∅); and μ 𝔯_♯ C_S^f ≤ μ^(1/2) 𝔯_♯ 𝔐_p^(m). So 𝔨_rec^n(B) ≤ (𝔨_♯ K_rec (1 + μ^(1/2) 𝔷′) + (1 − 𝔰₁^v)⁻¹ μ^(1/2)
𝔯_♯) 𝔐_p^(m) for every B, and 𝔐_n^(m) ≤ k₁^(m,μ,p) 𝔐_p^(m). ∎

**Definition {#def:tl5-hfn-constants}** (The constants with index n.) Let N ≥ 6, let the setting be that of
[[def:tl5-hff-constants]], with either route of [[eq:tl5-hff-routes]], and let 𝔐_n^(m), 0 ≤ m ≤ N − 4, be as in
[[eq:tl5-hfn-low]], at each point p. The constants with index n are the constants with index f formed with 𝔐_n^(m) in
place of the entry k₁^(m,μ,p) 𝔐_p^(m) of C_(∞,μ)^(m), in its form with index f, for 0 ≤ m ≤ N − 4, and in every constant
formed from these, among them C_P^♮ = C_(∞,μ)^(m_P) and 𝔎 of [[def:tl5-hfs-constants]], 𝔎^D of
[[def:tl5-hfd-constants]], S_F and 𝔰_*. Let S_F^n and 𝔯^n be S_F^f and 𝔯^f formed with them, ε^n := ε^f, and

    η_n := 1 − max(ϑ₁, ϑ₂) − 𝔯^n,      A_n := η_n^(−1/2) δ_w + η_n⁻¹ ε^n,      B_n := η_n⁻¹ S_F^n.

For a number 𝔜 ≥ 0 let 𝔰_*^n[𝔜] be 𝔰_*^f[𝔜] formed with the constants with index n, and, when 4A_n B_n < 1, put

    Y_n := 2A_n/(1 + (1 − 4A_n B_n)^(1/2)),      𝔰_*^n := 𝔰_*^n[Y_n].                            {#eq:tl5-hfn-constants}

**Theorem {#thm:tl5-hfn}** (Existence with the second derivatives at low levels word by word.) Let N ≥ 6. In the setting
of [[thm:tl5-hff]], with either route of [[eq:tl5-hff-routes]] and the constants with index n of
[[def:tl5-hfn-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N,
E_o^N, E_i^N); (c) η_n > 0, the closing condition

    4 A_n B_n = 4 η_n^(−3/2) (δ_w + η_n^(−1/2) ε^n) S_F^n < 1,                                     {#eq:tl5-hfn-closing}

and 𝔰_*^n < 𝔰₁^v. Then there is a solution g of the reduced problem on D^κ with Y_σ(g) ≤ Y_n for every σ ∈ [1/2, v*],
and the other conclusions of [[thm:tl5-hf]] hold with 𝔰_*^n in place of 𝔰_*. Each constant with index n is at most the
one with index f it replaces, ε^n = ε^f, η_n ≥ η_f, A_n ≤ A_f, B_n ≤ B_f, Y_n ≤ Y_f and 𝔰_*^n ≤ 𝔰_*^f; so the hypotheses
of [[thm:tl5-hff]] at N ≥ 6 imply these.

*Proof.* The proof of [[thm:tl5-hff]] with the chosen route applies with the constants with index n, ε^n, 𝔯^n, η_n, A_n,
B_n, Y_n, 𝔰_*^n[𝔜] and [[eq:tl5-hfn-closing]] in place of those with index f, S_M and ε_M being 0 at N ≥ 6, with one
change: the bounds at a point of 𝔰_g^(m), 0 ≤ m ≤ N − 4, and of 𝔰 that it uses hold with C_(∞,μ)^(m) formed with 𝔐_n^(m)
in place of k₁^(m,μ,p) 𝔐_p^(m).

To see this, let p be a point at which such a bound is formed. Then 𝔰 ≤ 𝔰₁^v on Q(a, b): in Step 1, for the σ of the set
Σ_* of the proof of [[thm:tl5-hfy]] and p ∈ D^κ_σ, as Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, and in Steps 2 and 3, as 𝔰 ≤ 𝔰₁^v on
D^κ_s. So [[lem:tl5-hfn-low]] applies at p: the step on second derivatives at low levels of the lemma in use holds with
𝔐_n^(m) in place of k₁^(m,μ,p) 𝔐_p^(m) in its part with ℰ_g, and with its parts with ϱ(p) and η₀(p) as they are. The
bounds at p of 𝔰_g^(m) and of 𝔰 are formed from the steps of zeroth, first and second order, the absorption and the
largest of the bounds, in the same way for all values of their constants, as in the proof of [[thm:tl5-hfe]]; so they
hold with C_(∞,μ)^(m) so formed, and with the constants of their parts with ϱ(p) and η₀(p) unchanged. The proofs on
which that of [[thm:tl5-hff]] rests use the entry k₁^(m,μ,p) 𝔐_p^(m) only through these bounds: in Step 1 through the
bound of 𝔰, in 𝔰_*, and in Step 3 through the bound of 𝔰_P = 𝔰_g^(m_P), in C_P^♮, from which 𝔎, 𝔎^D and S_F are formed
in the same way for all values of these numbers. So they hold with the constants with index n.

For the last claim, 𝔐_n^(m) ≤ k₁^(m,μ,p) 𝔐_p^(m) by [[lem:tl5-hfn-low]], and every constant with index f is
nondecreasing in this entry, through maxima, sums, products and suprema with nonnegative coefficients; so each constant
with index n is at most the one it replaces, and ε^n = ε^f. Then η_n ≥ η_f, A_n ≤ A_f, B_n ≤ B_f and 4A_n B_n ≤ 4A_f
B_f, as in the proof of [[thm:tl5-hff]]; the smaller root 2A/(1 + (1 − 4AB)^(1/2)) is nondecreasing in A and in B, so
Y_n ≤ Y_f, and 𝔰_*^n ≤ 𝔰_*^n[Y_f] ≤ 𝔰_*^f[Y_f] = 𝔰_*^f, 𝔰_*^n[𝔜] being nondecreasing in 𝔜 and in the constants. ∎

**Remark {#rem:tl5-hfn-what}** (What changes.) The quantity 𝔰_g^(m) is the largest of its weighted quantities, so the
step on second derivatives at low levels may bound each D̂²Ψ_B, |B| ≤ m, through its own recovery at p. Its leading term
involves the first derivatives of the seven words ZB only, the terms with 𝔷_Z and 𝔯_♯ the jets of B only, and only the
couplings 𝔄_BJ the jets of the words of length at most |B| that the substitutions bring in. The step bounded all of
these by the one number L_g, and so by 𝔐_p^(m), the Euclidean norm over the lengths b ≤ m + 1 of C_S and of the
constants C₁(𝔚_b) of the families of all 7^b words of length b, whose nonlinear parts carry the count (43 · 7^b)^(1/2),
with the coefficient k₁^(m,μ,p) in front of all of it. In 𝔐_n^(m) the leading term carries the family of the seven words
ZB at every length, through the map 𝒳_p, its nonlinear parts carrying 43^(1/2) 𝔨_Γ where those of the family of length b
carried K_rec(p) (43 · 7^b)^(1/2), and the terms with 𝔷_Z and 𝔯_♯ carry the constants C₁^l({B}) and C_S^f, or C_S^h, of
the one word B, with the weights of the fields in 𝔷₁^k and 𝔷₂^k; only the couplings keep 𝔐_p^(m), with the coefficient
(1 − 𝔰₁^v)⁻¹ α_𝔄^(m,μ). The parts with ϱ(p) and η₀(p) that the new bound gives are at most those of the step, by
(2𝔐^(m))^(1/2) ≥ 4 and the bounds of [[lem:tl5-hfk-rec]] (a), so those of the step are kept. In C₁^k(ΓB), as in
[[rem:tl5-hfk-what]], the terms bounded through 𝒟_g and 𝒥_g over the pairs keep the factor K_rec(p), the terms with one
bound for the seven words take 𝔨_Γ, and the couplings the norm 𝔞_𝔄^k(ΓB) of their weighted map. For B = ∅, 𝔨_rec^n(∅)
has the form of 𝔨_rec^k of [[def:tl5-hfk-constants]], the constant of the same step for h at level four, with C₁^l({∅})
in place of C₁^l. The entry 𝔐_n^(m) enters C_(∞,μ)^(m), so C_P^♮ for m = m_P, and through it 𝔎, 𝔎^D and S_F, and the
term of 𝔰_* with A for m = N − 4. The counts of the products, the Sobolev and leaf constants, the constants of one word,
the parts with ϱ and η₀ of the bounds at a point, the weights 𝔲₀, 𝔲₁, 𝔶₀, 𝔶₁ and 𝔶₀^h, the routes, the thresholds 𝔰₀ and
𝔰₁^v and the rates are unchanged, and at level four nothing changes. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfn]] are established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD f76dfef5, where sec:tl5-hfk is merged (Section 57.31,
merge 3fe8a9a7). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfn) through the last line of
[[rem:tl5-hfn-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfk-what]] (line 8039,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfk-what]] (lines 8037–8038).* Old:

the rates are unchanged, and at the levels N ≥ 6 nothing changes. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfk]] are established in this paper for no background at 10 l5.

New (one line added, of 112 characters; the two old lines are unchanged):

the rates are unchanged, and at the levels N ≥ 6 nothing changes. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
hypotheses of [[thm:tl5-hfk]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfn]] bounds the second derivatives at low levels word by word, at the levels N ≥ 6 ([[thm:tl5-hfn]]).

*3. Nothing else changes.* No earlier text is edited: the sites listed in the Comparison keep their texts, and the new
constants are defined in def:tl5-hfn-constants by reference to them.

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfn acts at the levels N ≥ 6 only, on thm:tl5-hff with either route of eq:tl5-hff-routes and
either option of def:tl5-hft-constants. At level four nothing changes: thm:tl5-hfk, the last theorem, is at N = 4 only,
and at N ≥ 6 the last theorem is thm:tl5-hff, which thm:tl5-hfn contains.

**Containment.** There is no new choice: for all admissible weights, routes and options the new entry is at most the old
one, so thm:tl5-hfn contains thm:tl5-hff at N ≥ 6, and through it every earlier theorem at these levels in the range
where thm:tl5-hff contains it. Exactly where:
- the last claim of thm:tl5-hfn and the last paragraph of its proof;
- 𝔐_n^(m) ≤ k₁^(m,μ,p) 𝔐_p^(m) for 0 ≤ m ≤ N − 4: the last paragraph of the proof of lem:tl5-hfn-low, term by term:
  - C₁^k(ΓB) ≤ K_rec C₁^l(ΓB): lem:tl5-hfn-fam (a multiplication of the components by numbers at most K_rec, and
    43^½𝔨_Γ/K_rec ≤ 301^½ by lem:tl5-hfk-rec (a));
  - C₁^l(ΓB) ≤ C₁^l(𝔚_(|B|+1)) and C₁^l({B}) ≤ C₁^l(𝔚_(|B|)): the restriction of the map of 𝔞_𝔄 to a subfamily has
    norm at most 1, and the integrands are nondecreasing in the count (43n)^½ and in 𝔞_𝔄, as k₁^p ≥ k₁^D;
  - the terms with 𝔷: Cauchy–Schwarz with (𝔷₁^k² + 𝔷₂^k²)^½ ≤ K_rec𝔷′, and μ ≤ μ^½; the term with 𝔯_♯: μ ≤ μ^½;
  - C₁^l(𝔚_b) and C_S^(b) (C_S^h for b = 0, C_S^f for b ≥ 1) are terms of 𝔐_p^(m) for b ≤ m + 1;
- the parts with ϱ(p) and η₀(p) of the step are kept, so C_((∞,ϱ),μ)^(m) and C_((∞,0),μ)^(m) are unchanged; the new
  parts are at most these, by (2𝔐^(m))^½ ≥ 4 ≥ √7, 𝔷₁^k + 𝔷₂^k ≤ √2K_rec𝔷′ and ν′ ≤ ν′^½ (lem:tl5-hfn-low);
- every constant with index f is nondecreasing in the entry; ε^n = ε^f; Y_n ≤ Y_f, the smaller root being
  nondecreasing in A and in B; 𝔰_*^n ≤ 𝔰_*^f.
The present closing conditions stay valid beside the new one: no earlier theorem is changed, and the hypotheses of
thm:tl5-hff at N ≥ 6 imply those of thm:tl5-hfn.

**Both constraints.** The change enters the entry k₁^(m,μ,p)𝔐_p^(m) of C_(∞,μ)^(m) for every m ≤ N − 4. Through
C_P^♮ = C_(∞,μ)^(m_P), m_P = 1, it enters 𝔎 = max(C_P⁰𝔨_A, C_P^♮𝔨_B), 𝔎^D (𝔠^(D,7)C_P + 7^(j′/2)(…)𝔎), 𝔞_(o,s) and
𝔞_(i,s) (𝔣₀C_P, 𝔣₁C_P), so S_F, B_n, the closing condition and Y_n; through C_(∞,μ)^(N−4) it enters the term of 𝔰_* with
A. It does not enter 𝔯 (whose entries are 𝔣₀ and 𝔣₁ times C_(P,ϱ) and C_(P,0), 𝔎_ϱ, 𝔎₀, 𝔎^D_ϱ, 𝔎^D₀ and, on route
(𝔯), 𝔯_ϱ^f with C_P⁰) nor ε, so 𝔯^n = 𝔯^f, η_n = η_f and A_n = A_f (deduced from the definitions; the theorem states
only the inequalities, which suffice).

Unchanged: all counts of the products (𝔠^♮, 𝔠^D, 𝔠^(D,7), 𝔠^ϱ), the Sobolev and leaf constants, the recovery constants
at the points of the face (𝔨_♯, K_rec, k₁^D, k₁, k₂^z, 𝔷′, 𝔵^z), the first-order constants of the families
(C₁^l(𝔚), C₁^l, C_(1,ϱ)^l, C_(1,0)^p), C_S^f, C_S^h, C_(0,0)^h, C_P⁰, C_(P,0)⁰, the parts with ϱ and η₀ of every bound at
a point (C_(P,ϱ)^♮, C_(P,0)^♮, C_((∞,ϱ),μ)^(m), C_((∞,0),μ)^(m)), the weights 𝔲₀, 𝔲₁, 𝔶₀, 𝔶₁, 𝔶₀^h, θ, ϑ₁, ϑ₂, the
functions 𝔨₁, 𝔨₂, 𝔷, 𝔤₁, the thresholds 𝔰₀ and 𝔰₁^v with the cap, the routes, the rule of the threshold (Y_n has the
form of Y_f), ε and the rates. Level four is untouched.

1. Lever A, scoped first as mathematics (sites at HEAD f76dfef5).
   - What 𝔰_g^(m) is. def:tl5-hfg-graded (87:5051–5052): the maximum of μ|H|, μ^((|B|+2)/2)|Ψ_B| (|B| ≤ N − 2),
     μ^((|B|+3)/2)|D̂Ψ_B| (|B| ≤ N − 3) and μ^((|B|+4)/2)|D̂²Ψ_B| (|B| ≤ m), over the words B. So the step on second
     derivatives at low levels bounds a supremum over the words, each D̂²Ψ_B(p) through its own recovery at p, and the
     bounds at a point take the largest of the four steps; nothing is summed over B.
   - The step: lem:tl5-hf-linfty (87:4355–4360), lem:tl5-hfg-linfty (87:5185–5193), lem:tl5-hfs-linfty
     (87:5585–5590), lem:tl5-hft-small (a) (87:5873–5879) and (b) (87:5887–5889), lem:tl5-hfp-low (87:6822–6834). Its
     bound of D̂²Ψ_B(p) is the recovery at p (lem:tl5-hf-recovery, 87:4040–4076, in the form of lem:tl5-hfz-rec,
     87:6408–6438, with 𝔥 = 𝔰₁^v by lem:tl5-hfz-abs, 87:6482–6483), with 𝔣 from the commuted equation (87:4332–4333).
   - What that recovery needs: (a) D̂ℒ_ZΨ_B = D̂Ψ_(ZB), the seven words ZB of length |B| + 1, in the leading term;
     (b) D̂Ψ_B and Ψ_B, in 𝔷_Z = 3|D̂Z||D̂Ψ_B| + 2|D̂²Z||Ψ_B| and in 𝔯_♯|Ψ_B|; (c) 𝔣 = Σ_J 𝔄_BJ(D̂Ψ_J, Ψ_J) +
     Σ_J 𝔔_BJ ℒ^J(2R̂ic) − 𝔑′_B. Only the couplings of (c) bring in other words. By def:tl5-hf-coupling (87:4077–4098)
     every D̂²Ψ_J, |J| < |B|, of the commutator terms (𝔏_(Z_S)𝒦[π^(Z_k)])Ψ_(J(k,S)) of eq:tl5-hf-system (87:4028) is
     replaced by ℛ_p, recursively over the shorter words, with D̂ℒ_ZΨ_J = D̂Ψ_(ZJ) and L̂Ψ_J again by the system; so
     𝔄_BJ acts on the jets of words J with |J| ≤ |B|, not of the form ZB (the same-level ones come from the recovery of
     the D̂²Ψ_(I′), |I′| = |B| − 1, 87:4096–4097), and 𝔄_∅J = 0, as L̂Ψ_∅ = 𝔤. The residual is k₂^zϱ(p) and the
     nonlinear terms are absorbed (87:5190–5192; 87:5888).
   - The step bounds (a), (b) and the jets of (c) by one number, L_g (87:5187–5188; 87:5585–5588: "the terms with
     D̂Ψ_(ZB) are bounded by L_g as there"), the norm of the jets of all words of length at most m + 1, and
     lem:tl5-hfp-low bounds L_g by 𝔐_p^(m)ℰ_g^½ plus its parts with ϱ and η₀ (87:6827–6832). That is the entry
     k₁^(m,μ,p)𝔐_p^(m), whose 𝔐_p^(m) counts the families 𝔚_b of all 7^b words of each length b ≤ m + 1.
   - The route, word by word (lem:tl5-hfn-low): (a) through eq:tl5-hfp-family for 𝔚 = ΓB (seven distinct words of
     length |B| + 1 ≤ N − 3), with the map 𝒳_p (lem:tl5-hfn-fam); (b) through the one-word steps, C₁^l({B}) and C_S^f or
     C_S^h; (c) through α_𝔄^(m,μ)L_g, as before. It holds for every m ≤ N − 4, both options and both routes, so both
     𝔐_p^(1) (in C_P^♮) and 𝔐_p^(2) (in 𝔰_* at N = 6) are replaced.
   - The weighted image of round 16 (lem:tl5-hfk-rec, lem:tl5-hfk-fam) applies to this step at every N ≥ 6: the proof of
     lem:tl5-hfk-fam uses of Γ and of N = 4 only that the family is seven distinct words of one length at most N − 3,
     one for each field, and the three kinds are the same with the words JZB, Z′JZB and σZB (lem:tl5-hfn-fam). So the
     second kind (the nonlinear part of C₁(ΓB), and the part with ϱ and the terms on S_a, which lie in the parts with
     ϱ(p) and η₀ of eq:tl5-hfn-fam) takes 𝔨_Γ in place of √7K_rec, the factor ω = 𝔨_Γ/(√7K_rec) of G0r §G0r.4, the third
     kind 𝔞_𝔄^k(ΓB) ≤ K_rec𝔞_𝔄(ΓB), and the terms 𝔷_Z at p take 𝔷₁^k and 𝔷₂^k. The first kind keeps K_rec(p), as at
     level four.
   - The parts with ϱ and η₀ of the new bound are at most those of the step (lem:tl5-hfn-low), so they are kept and no
     constant with ϱ or η₀ is redefined; P-GRD16's scoping had proposed new ones there too, which is not needed.
2. Lever B (level 4, kind 1 of C₁^(Γ,l)): no honest route; the obstruction, exactly. Nothing drafted.
   - Kind 1 (68.8 / 69.6 / 71.2 / 70.9 % of C₁^(Γ,l) at the point holding sup 𝔨_rec^p, G0r §G0r.4 item 1) is the
     leading family terms (μ^½ + ϖ′^½) through D̂Ψ_(JZ) and the remainders, the (2ϖ′)^½ of D̂R′, the face recovery's
     k₁^D through Z′JZ and its terms with 𝔷′ and 𝔯_♯. Each is bounded through 𝒟_g or 𝒥_g over the pairs (J, Z), and the
     map 𝒳_p weights them by Z, the last letter of JZ (87:7914–7918): what they need is |T(p)|⁻²E_T + λ_M(p)⁻¹E_R,
     E_T and E_R the weighted face energies of the words ending in T and in a rotation.
   - The energies. Every bound of the chapter enters the face energies only through ℰ_g(p) (87:6794, 87:7720), and
     ℰ_g(p) ≤ e^(φ(p))Y_s² (87:7604–7605, 87:7802). Given only E_T + E_R ≤ ℰ_g(p), the supremum of the weighted sum is
     K_rec(p)²ℰ_g(p). What would be needed: E_T ≤ θ_Tℰ_g(p) at the supremum with θ_T < 1, which would give kind 1 the
     factor (θ_T|T|⁻² + (1 − θ_T)λ_M⁻¹)^½ where |T|⁻¹ > λ_M^(−½) (the T part leads K_rec at every level-4 face point,
     G0r §G0r.3 item 1). Nothing in the chapter gives θ_T, and no report measures the split.
   - The bootstrap quantity. Y_s is one number for all the words (87:6241–6243). What would be needed: a bootstrap for
     the energies split by last letter, Σ_I w_(ℓ(I)) μ^|I| ℰ_I with constant weights, carried through
     prop:tl5-hf-linear-n (87:4099–4122): the couplings ℭ_(jj′ϰ) of 𝔅_N split by last letter (the commutator terms
     with k = j of eq:tl5-hf-system carry π^(Z_j) and change the last letter; π^(K₁₂) = π^(K₃₄) = 0, 87:3940, but
     π^T ≠ 0 in general), and s_N, δ_w and the products weighted. With constant weights the recovery at p gains
     max(|T(p)|⁻²/w_T, λ_M(p)⁻¹/w_R) in place of K_rec(p)², while every other use of ℰ_g pays 1/min(w); where the
     forcing sits on the words ending in T, A grows by the factor by which B falls (P-GRD16's sketch). A gain needs
     the split of the energies and of the forcing by last letter, which no report measures.
   - The transport split by letter. The face transport (eq:tl5-hfe-face) acts on the four fields Ã_i, and the weights
     act on the last letter Z; a split by the first letter of JZ does not separate the components the weights act on.
     For the face recovery's leading term, lem:tl5-hfk-rec at the face point q weights the first letter Z′ of Z′JZ,
     but then the family over (J, Z) carries two weights, on the first and the last letter, and needs the energies
     split by both: the same obstruction.
   - So kind 1 keeps K_rec, and G0r's ÷ 2 price of 𝔨_rec^p's C₁ term (+0.285 / +0.254 / +0.295 / +0.293,
     §G0r.3 item 2) is not reached by any proved route; round 16's +0.035 to +0.077 stands at level 4.
3. Lever C (k₃ in 𝔰₀ at level 6 in D_A): scoped only, not drafted.
   - In D_A, 𝔰₁^v = 𝔰₀/2 = 1/(4 sup k₃) (G0r §G0r.1), k₃ = k₃^♮(μ) with its factor 8/5 = (6/5)(4/3), that of
     1 − (4/3)|H| ≥ 5/6 in front of |𝔣|. Since sec:tl5-hfz the absorptions use k₃^z = (5/8)(1 − 𝔰₁^v)⁻¹k₃ and
     𝔵^z = 𝔰₁^v sup k₃^z, but the thresholds keep k₃ (def:tl5-hfz-constants, 87:6467–6468).
   - A threshold with k₃^z (circular in 𝔰₁^v, closable with a fixed 𝔥 ≥ 𝔰₁^v and k₃^𝔥 := (5/8)(1 − 𝔥)⁻¹k₃) would let
     𝔰₁^v rise by up to (8/5)(1 − 𝔥). It is not a smaller k₃ in G0r's sense: 𝔵^z = 𝔰₁^v sup k₃^z rises with 𝔰₁^v,
     from about 5/32 to 1/4, and with it the nonlinear parts (43n)^½𝔵^z(…)/(1 − 𝔵^z) of every C₁(𝔚) (kind 2, 28–30 %
     of C₁^(Γ,l) at level 4, G0r §G0r.4 item 1), the factors (1 − 𝔵^z)⁻¹ of every C_∞ and C_P and the
     (k₁ + 2𝔵^z)/(1 − 𝔵^z) of the bounds of the second derivatives. Every lemma of sec:tl5-hfs to sec:tl5-hfy that uses
     𝔰 ≤ 𝔰₀ or 𝔵 ≤ 1/4 would need restating.
   - A smaller k₃ that keeps 𝔵^z, worth log₁₀ q in D_A for a factor q, as f ∝ 𝔰₁^v = 1/(4 sup k₃) there (G0r §G0r.1;
     deduced), needs smaller counts 𝔠^♮ or sums of the ‖𝔔_CJ‖ in the absorption; no section has them. (A sketch, not
     checked: the second-derivative factors of the nonlinear terms have shorter words, lem:tl5-hfg-quadratic, so an
     induction over the length could replace the absorption of M_g and of the step at low levels; it trades the
     threshold for a factor polynomial in 𝔵^z.)
   - Either way the rise of 𝔰₁^v in D_A is capped by ϑ's cap, 1.48 and 1.14 times higher (G0r §G0r.1), and at seed 1 by
     𝔰₀ ≤ 𝔰_♭ = 10⁻⁴, 1.25 times 𝔰₀ = 2 × 4.0 × 10⁻⁵ there (deduced from the 𝔰₁^v of G0r §G0r.0), unless 𝔰_♭ is raised.
     So lever C is worth at most +0.10 (+0.17 with 𝔰_♭ raised) / +0.06 at the present ϑ₂ in D_A, before the cost
     through 𝔵^z, and 0 in D*, where 𝔰₁^v is at the cap of ϑ₂; a larger ϑ₂ costs η and the admissibility of the rates.
4. The sites, at HEAD f76dfef5, old → new:
   - the entry k₁^(m,μ,p)𝔐_p^(m) of C_(∞,μ)^(m) (eq:tl5-hfg-cinf at 87:5139 with the replacements of 87:6681,
     87:7413–7414, 87:7570 and 87:7755–7756) → 𝔐_n^(m) of eq:tl5-hfn-low, for 0 ≤ m ≤ N − 4;
   - the proof of lem:tl5-hfp-low (87:6827–6834) and the step it modifies (87:5585–5590, 87:5873–5879) →
     lem:tl5-hfn-low, with lem:tl5-hfn-fam for the leading term;
   - the constants formed from C_(∞,μ)^(m): C_P^♮ (87:5648), 𝔎 (87:5655), 𝔎^D (87:7197–7198), S_F (87:5659–5660),
     𝔰_* (87:5910–5915 in its forms) → index n.
5. The closing condition eq:tl5-hfn-closing is eq:tl5-hff-closing at N ≥ 6 (S_M = ε_M = 0) with the constants with
   index n; it also defines Y_n, through 4A_nB_n < 1.

What it gives, deduced, not evaluated. Assumptions:
- every supremum at one point: each fall below is that of the leading entry at the point where G0r measured it, on the
  P-GRD15 optimum; with the new entry the supremum, or the leading entry, may move, so the falls are upper figures for
  the falls of the suprema, and the gains through the theorem are upper figures at the parameters of that optimum (a
  re-optimisation of μ, x or ϑ may add to them, as round 15's did, G0r §G0r.0);
- the G0r figures are on P-GRD15 (sec:tl5-hff) with route (𝔯) at level 6; sec:tl5-hfk acts at N = 4 only.
Level 6, through the term of 𝔰_* with A (G0r §G0r.1: f binds alone there, f ∝ 𝔰₁^v/sup(C_(∞,μ)^(2)μ^(−3)e^(φ/2)); ϱ
is 4.0–7.9 decades above f and the closing 2.9–5.2 decades away, so f keeps binding under a rise of less than 2.9).
- The entry, seed 1 D_A / seed 2 D_A / seed 1 D* / seed 2 D*, at the point where G0r §G0r.4 item 2 measures it, the one
  holding sup C_P^v, where k₁𝔐_p^(1) leads: log₁₀ C₁^l({ZB})/𝔐_p^(2) = −0.62 / −0.61 / −0.61 / −0.59 at x = 𝔵_D and
  −0.70 / −0.70 / −0.66 / −0.68 at the optimum's x (−0.62 / −0.60 / −0.62 / −0.59 and −0.70 / −0.69 / −0.67 / −0.68 with
  the suprema taken apart), C₁^l({ZB}) being C₁^l(ΓB); C₁^l({ZB}) is 0.08 / 0.08 / 0.08 / 0.08 and 0.11 / 0.11 / 0.09 /
  0.10 above the one-word C₁; α_𝔄 is 0.1 / 0.2 / 0.1 / 0.1 % of k₁ there and 0.3 / 0.3 / 0.2 / 0.3 % at the point
  holding sup k₁𝔐_p^(2), where 𝔰_*'s supremum sits. The figures below take r at G0r's point and the larger α, as if the
  two points were one (the first assumption); the larger α gives the smaller lower figures.
- With r := C₁^l({ZB})/𝔐_p^(2): the leading term 𝔨_♯C₁^k(ΓB) is at most r times its counterpart 𝔨_♯K_rec𝔐_p^(2); the
  terms with 𝔷 are at most (C₁^l² + μC_S²)^½/𝔐_p^(2) ≤ r times theirs, as C₁^l({B}) ≤ C₁^l is below C₁^l({ZB}); the term
  with 𝔯_♯ is at most μ^½C_S/𝔐_p^(2) times its; the couplings keep their size. So
  𝔐_n^(2)/(k₁𝔐_p^(2)) ≤ r + (1 − r) × (α_𝔄's share), and at that point, at fixed parameters, the entry falls by at least
  about 0.61 / 0.60 / 0.60 / 0.58 at x = 𝔵_D and 0.69 / 0.69 / 0.65 / 0.67 at the optimum's x, to the rounding of G0r's
  two-place figures (−log₁₀(r + (1 − r)α) = 0.616 / 0.606 / 0.607 / 0.586 and 0.695 / 0.695 / 0.657 / 0.675 with the
  printed r and the larger α; with the suprema apart, 0.616 / 0.596 / 0.617 / 0.586 and 0.695 / 0.685 / 0.667 / 0.675).
  These are lower figures for the fall at that point, not upper ones.
- Upper figures. (i) The entry is at least its leading term, so it falls by at most −log₁₀ r + log₁₀ s + w, with
  s := k₁/(𝔨_♯K_rec) at that point and w the fall of C₁^k(ΓB) below K_rec C₁^l(ΓB) through the map; neither is
  reported at level 6 (G0r gives k₁ ≈ 𝔨_♯K_rec(1 + μ^½𝔷′) + μ^½𝔯_♯/(1 − 𝔰₁^v) to 99.7 %, without the split; at
  level 4 on Γ, w = 0.071 / 0.062 / 0.045 / 0.045, from C₁^k/(K_rec C₁^(Γ,l)) = 0.850 / 0.866 / 0.901 / 0.902,
  §G0r.4 item 1). (ii) The other entries of C_(∞,μ)^(2) do not move, so its supremum cannot fall below that of
  (1 − 𝔵^z)⁻¹C₁^l, 1.1–1.3 decades below sup k₁𝔐_p^(2) (§G0r.4 item 2), nor below that of C_P⁰ (not reported for
  m = 2; for m = 1, sup C_P^v/sup C_P⁰ = +1.02 / +1.17 / +1.20 / +1.43, §G0r.3 item 3).
- So at fixed parameters the gain of the level-6 target is at most the smaller of 1.1–1.3 and the fall, and the fall at
  the optimum's x lies between about 0.69 / 0.69 / 0.65 / 0.67 and 0.70 / 0.70 / 0.66 / 0.68 + log₁₀ s + w. G0r's ÷ 2
  price of 𝔐_p's C₁ part, +0.286 / +0.295 / +0.276 / +0.295 (§G0r.3 item 3), shows the target answering nearly one to
  one to a fall of the entry there.
- Through the closing condition: C_P^♮'s entry falls by about the ratio C₁^l({ZB})/𝔐_p^(1), 0.32–0.37 decades
  (§G0r.4 item 2, at the point holding sup C_P^v, before the factor k₁ and the terms with 𝔷 and 𝔯_♯); at level 6 the
  closing is 2.9–5.2 decades away, so this gives nothing there.
- The parts with ϱ and η₀: unchanged. Level 4: nothing.

Not done.
- Lever B: kind 1 needs the face energies split by last letter, or a bootstrap weighted by it (item 2).
- Lever C: a threshold with k₃^z, or an absorption-free induction, capped by ϑ's cap and 𝔰_♭ (item 3).
- The couplings of the step keep 𝔐_p^(m); they could take the norm of the words of length at most |B| only (𝔐_p^(m−1)
  for m ≥ 1, and 0 for B = ∅, as 𝔄_∅J = 0). Their share of k₁ is 0.2–0.3 % at level 6, so at most about 0.003 of the
  entry; not drafted.
- For G0s to measure: 𝔐_n^(2) and 𝔐_n^(1) at the level-6 optima, the ratio s = k₁/(𝔨_♯K_rec), and C₁^k(ΓB)
  against K_rec C₁^l(ΓB) at level 6.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfn	paper/reader/proofs/P-GRD17.md@PENDING:1	P-GRD17, section	new; at the end of ch:ten-l5, after rem:tl5-hfk-what; N >= 6: the step on second derivatives at low levels bounded word by word, each D^2 Psi_B(p) through its own recovery: the leading term through the family of the seven words ZB and the map X_p, the terms with z_Z and r_sharp through the one word B, only the couplings through L_g; M_n^(m) in place of k_1^(m,mu,p) M_p^(m) in C_(inf,mu)^(m)
    lem:tl5-hfn-fam	paper/reader/proofs/P-GRD17.md@PENDING:20	P-GRD17, Lemma	N >= 6, |B| <= N - 4, GammaB = (ZB)_Z: |X_p (D Psi_(ZB)(p))_Z| <= mu^(-(|B|+4)/2) C_1^k(GammaB) E_g(p)^(1/2) + k_Gamma (w C_(1,rho)^l rho(p) + E_0); C_1^k(GammaB) = K_rec(p) C_1^l(GammaB) with 43^(1/2) k_Gamma/K_rec for 301^(1/2) and a_A^k(GammaB)/K_rec for a_A(GammaB); the proof of lem:tl5-hfk-fam for the family GammaB
    eq:tl5-hfn-fam	paper/reader/proofs/P-GRD17.md@PENDING:30	P-GRD17, display	new
    lem:tl5-hfn-low	paper/reader/proofs/P-GRD17.md@PENDING:63	P-GRD17, Lemma	N >= 6, 0 <= m <= N - 4: the step on second derivatives at low levels with M_n^(m) in place of k_1^(m,mu,p) M_p^(m) in its part with E_g, its parts with rho and eta_0 as they are; M_n^(m) <= k_1^(m,mu,p) M_p^(m); C_1^l(W') <= C_1^l(W) for subfamilies
    eq:tl5-hfn-low	paper/reader/proofs/P-GRD17.md@PENDING:69	P-GRD17, display	k_rec^n(B) = k_sharp (C_1^k(GammaB) + z_1^k mu^(1/2) C_1^l({B}) + z_2^k mu C_S^f) + (1 - s_1^v)^(-1) mu r_sharp C_S^f (C_S^h for B empty); M_n^(m) = max_(|B|<=m) k_rec^n(B) + (1 - s_1^v)^(-1) alpha_A^(m,mu) M_p^(m)
    def:tl5-hfn-constants	paper/reader/proofs/P-GRD17.md@PENDING:122	P-GRD17, Definition	constants with index n (N >= 6, either route): M_n^(m) in place of the entry k_1^(m,mu,p) M_p^(m) of C_(inf,mu)^(m), 0 <= m <= N - 4, in its form with index f, and in every constant formed from these (C_P^natural, K, K^D, S_F, s_*); eps^n = eps^f; eta_n, A_n, B_n, Y_n, s_*^n
    eq:tl5-hfn-constants	paper/reader/proofs/P-GRD17.md@PENDING:133	P-GRD17, display	new
    thm:tl5-hfn	paper/reader/proofs/P-GRD17.md@PENDING:135	P-GRD17, Theorem	N >= 6: thm:tl5-hff (either route) with the constants with index n; Y_sigma <= Y_n; its hypotheses are implied by those of thm:tl5-hff at N >= 6
    eq:tl5-hfn-closing	paper/reader/proofs/P-GRD17.md@PENDING:140	P-GRD17, display	closing condition: 4 eta_n^(-3/2)(delta_w + eta_n^(-1/2) eps^n) S_F^n < 1
    rem:tl5-hfn-what	paper/reader/proofs/P-GRD17.md@PENDING:169	P-GRD17, Remark	what changes
