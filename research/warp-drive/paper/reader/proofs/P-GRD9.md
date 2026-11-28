### The recovery sharpened and counted over the words {#sec:tl5-hfz}

In the recovery of second derivatives of [[lem:tl5-hf-recovery]] the coefficients (√3 + 8/3) K_rec, 4/3 and 𝔯₀ are
divided by 1 − (4/3)|H| ≥ 5/6, which gives the factor (6/5)(√3 + 8/3) of K_rec in every recovery constant, the factor
8/5 in k₂, in k₃ and in front of α_𝔄, and (6/5)𝔯₀. After Step 1 of the bootstrap |H| ≤ 𝔰 ≤ 𝔰₁^v; this section bounds the
second derivatives with that smallness and with the entry (1, 1) kept apart ([[lem:tl5-hfz-rec]]), which replaces these
factors by 𝔨_♯(𝔰₁^v) < 2.45, (1 − 𝔰₁^v)⁻¹ and (1 − 𝔰₁^v)⁻¹ 𝔯_♯. It then bounds the second derivatives of the words JB of
the first-order step in the Euclidean norm over the 43 words J ([[lem:tl5-hfz-words]]): the leading term of the recovery
counts once, the couplings 𝔄 count through the operator norm of their family over the words, and the count 43 remains
only with the nonlinear part. Finally the parts with 𝒥_g and with ϱ of the first-order step are separated by the
triangle inequality on the face, in place of (x + y)² ≤ 2x² + 2y² ([[lem:tl5-hfz-c1]]). The closing condition is
[[eq:tl5-hfz-closing]]; every new constant is at most the one it replaces, and the earlier closing conditions remain
valid. The notation is that of [[sec:tl5-hfy]].

**Lemma {#lem:tl5-hfz-rec}** (The recovery with the entry (1, 1) apart.) Let p, H, Ψ, 𝔣, K_rec, 𝔷_Z, ‖𝓡̂‖ and ‖𝒞_(·1)‖
be as in [[lem:tl5-hf-recovery]], except that |H| ≤ 𝔥 at p for a number 𝔥 ∈ [0, 1) in place of |H| ≤ 1/4, and put

    𝔨_♯(𝔥) := (1 + (2 + √2 𝔥)²/(1 − 𝔥)²)^(1/2),      𝔯_♯ := 2‖𝓡̂‖ + ‖𝒞_(·1)‖.

Then at p

    |D̂²Ψ| ≤ 𝔨_♯(𝔥) K_rec ((Σ_(Z∈Γ) |D̂ ℒ_ZΨ|²)^(1/2) + (Σ_(Z∈Γ) 𝔷_Z²)^(1/2))
             + (1 − 𝔥)⁻¹ (|𝔣| + 𝔯_♯ |Ψ|).                                                         {#eq:tl5-hfz-rec}

The function 𝔨_♯ is increasing, 𝔨_♯(0) = √5 and 𝔨_♯(1/4) < 3.3; for 𝔥 ≤ 1/4 each coefficient of [[eq:tl5-hfz-rec]] is at
most the corresponding one of [[eq:tl5-hf-recovery]] divided by 1 − (4/3)𝔥.

*Proof.* Let X be as in the proof of [[lem:tl5-hf-recovery]], X₀ the sum of its terms |D̂²Ψ(A, B)|² with A ≠ 1, and
X₁ := X − X₀, the sum of the |D̂²Ψ(1, B)|², B ≠ 1; that proof gives X^(1/2) ≤ K_rec ((Σ_Z |D̂ℒ_ZΨ|²)^(1/2) + (Σ_Z
𝔷_Z²)^(1/2)) without using H. Let R² := |D̂²Ψ|² − |D̂²Ψ(1, 1)|², the sum of X and of the |D̂²Ψ(A, 1)|², A ≠ 1. As
D̂²Ψ(A, 1) = D̂²Ψ(1, A) + 𝒞_(A1)Ψ, Minkowski's inequality gives (Σ_(A≠1) |D̂²Ψ(A, 1)|²)^(1/2) ≤ X₁^(1/2) + ‖𝒞_(·1)‖ |Ψ|,
and so R ≤ (X₀ + 2X₁)^(1/2) + ‖𝒞_(·1)‖ |Ψ|. In the identity for (1 + H^11) D̂²Ψ(1, 1) of that proof the squared norms of
the four diagonal terms D̂²Ψ(0, 0) and D̂²Ψ(j, j) are terms of X₀, so the sum of their norms is at most 2X₀^(1/2); by
the Cauchy–Schwarz inequality |Σ_((M,N)≠(1,1)) H^MN D̂²Ψ(M, N)| ≤ |H| R; and |H^11| ≤ |H| ≤ 𝔥. With R ≤ (2X)^(1/2) +
‖𝒞_(·1)‖ |Ψ| in the last term this gives

    (1 − 𝔥) |D̂²Ψ(1, 1)| ≤ 2X₀^(1/2) + √2 𝔥 X^(1/2) + |𝔣| + (2‖𝓡̂‖ + 𝔥 ‖𝒞_(·1)‖) |Ψ|.

Write X₀ = s² X with s ∈ [0, 1], so that X₀ + 2X₁ = (2 − s²) X. As |D̂²Ψ| = (R² + |D̂²Ψ(1, 1)|²)^(1/2), Minkowski's
inequality in the plane gives |D̂²Ψ| ≤ g(s)^(1/2) X^(1/2) + ‖𝒞_(·1)‖ |Ψ| + (1 − 𝔥)⁻¹ (|𝔣| + (2‖𝓡̂‖ + 𝔥 ‖𝒞_(·1)‖) |Ψ|),
with g(s) := 2 − s² + (2s + √2 𝔥)²/(1 − 𝔥)²; and ‖𝒞_(·1)‖ + 𝔥 ‖𝒞_(·1)‖/(1 − 𝔥) = ‖𝒞_(·1)‖/(1 − 𝔥). As 4/(1 − 𝔥)² > 1, g
is convex, so its largest value on [0, 1] is g(1) = 𝔨_♯(𝔥)² or g(0) = 2 + 2𝔥²/(1 − 𝔥)², and g(1) ≥ g(0) since
(2 + √2 𝔥)² − 2𝔥² − (1 − 𝔥)² = 3 + (4√2 + 2)𝔥 − 𝔥² > 0. With the bound of X this is [[eq:tl5-hfz-rec]]. For the last
claim, 𝔨_♯(𝔥) ≤ 𝔨_♯(1/4) < √3 + 8/3, (4/3)(1 − 𝔥) ≥ 1 − (4/3)𝔥, (8/3)(1 − 𝔥) ≥ 2(1 − (4/3)𝔥) and √2 (1 − 𝔥) ≥ 1 − (4/3)𝔥
for 𝔥 ≤ 1/4. ∎

**Definition {#def:tl5-hfz-constants}** (The constants with index z.) In the setting of [[lem:tl5-hfy-abs]], with k₃,
𝔰₁^v and 𝔵 as there, let 𝔨_♯ := 𝔨_♯(𝔰₁^v) and 𝔯_♯ be as in [[lem:tl5-hfz-rec]], q₁ as in [[lem:tl5-hf-linfty]], and
α_𝔄^(j,ν′) and k₁^(j,ν′) the numbers α_𝔄^(j,μ) and k₁^(j,μ) of [[def:tl5-hfs-bounds]] with ν′ in place of μ. For 0 ≤ j ≤
N − 1 and ν′ ∈ (0, 1] put

    k₁^(j,ν′,z) := 𝔨_♯ K_rec (1 + ν′^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|))
                   + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),
    k₁^z := k₁^(N−1,μ,z),   k₂^z := (1 − 𝔰₁^v)⁻¹ q₁,   k₃^z := (5/8)(1 − 𝔰₁^v)⁻¹ k₃,   𝔵^z := 𝔰₁^v sup_(D^κ) k₃^z,

and let 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z) be 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0 of [[lem:tl5-hfv-rec]] with 𝔨_♯ in place of
(6/5)(√3 + 8/3) and (1 − 𝔰₁^v)⁻¹ 𝔯_♯ in place of (6/5)𝔯₀. For a word B with |B| ≤ N − 3 let 𝔞_𝔄(B) be, at each point,
the operator norm of the map

    (ξ_K)_(|K|≤|B|+2) ↦ (Σ_K μ^((|B|+3−|K|)/2) 𝔄_(JB,K) ξ_K)_J,

J running over the 43 words of rotations with |J| ≤ 2 and 𝔄_(JB,K) := 0 for |K| > |JB|, from the families (ξ_K) of jets
at the point, with the Euclidean norm of the family formed with the norm (|D̂Ψ|² + |Ψ|²)^(1/2) on the jets, to the
families of tensors indexed by J, with their Euclidean norm. Let 𝔞_𝔄 be the largest of the 𝔞_𝔄(B), and put

    𝔩₀ := 𝔨_♯ K_rec (1 + μ^(1/2) √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)) + (1 − 𝔰₁^v)⁻¹ (μ^(1/2) 𝔯_♯ + 𝔞_𝔄),
    𝔩 := 𝔩₀ + 43^(1/2) 𝔵^z (k₁^z + 2)/(1 − 𝔵^z),
    C₁^z² := 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) 𝔳⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 2|∂_γ|² (𝔩 + (2ϖ′)^(1/2))²),
    C_(1,ϱ)^z² := 43 · 6 C² 𝔴(p)⁶ sup_(Σ₁(a,b)) (𝔳⁶ R⁻³ 2|∂_γ|² (k₂^z)²/(1 − 𝔵^z)²)
                  · ∫_(Σ₁(a,b)) dμ dτ₂/(1 − κκ′),                                                  {#eq:tl5-hfz-c1}

with ϖ′ and 6C²𝔴⁶𝔳⁶ as in [[lem:tl5-hfx-c1]]; so C_(1,ϱ)^z is C_(1,ϱ) with 2(k₂^z)²/(1 − 𝔵^z)² in place of 32k₂². The
constants with index z are the constants of [[thm:tl5-hfy]] formed with k₁^(j,·,z), k₂^z, 𝔵^z, 𝔨_rec^z, 𝔨_rec^(ϱ,z),
𝔨_rec^(0,z), C₁^z and C_(1,ϱ)^z in place of k₁^(j,·), k₂, 𝔵, 𝔨_rec, 𝔨_rec^ϱ, 𝔨_rec^0, C₁^x and C_(1,ϱ); the thresholds
𝔰₀ and 𝔰₁^v keep k₃.

**Lemma {#lem:tl5-hfz-abs}** (The bounds with index z.) In the setting of [[lem:tl5-hfy-abs]], if 𝔰 ≤ 𝔰₁^v on Q(a, b),
then the lemmas named there hold with its replacements and with k₁^(j,·,z), k₂^z, 𝔵^z, 𝔨_rec^z, 𝔨_rec^(ϱ,z) and
𝔨_rec^(0,z) in place of k₁^(j,·), k₂, 𝔵, 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0. In particular the bounds [[eq:tl5-hfs-m2]],
[[eq:tl5-hfq-m2]] and those of M_g^(j), in the lemmas that state them, hold at every point of Q(a, b) with (k₁^(j,μ,z) +
2𝔵^z)/(1 − 𝔵^z) and k₂^z/(1 − 𝔵^z) in place of 2(k₁^(j,μ) + 1) and 2k₂. Moreover k₁^(j,ν′,z) ≤ k₁^(j,ν′), k₂^z ≤ k₂, 𝔵^z
≤ 2𝔵/3 ≤ 1/6, and 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z) are at most 𝔨_rec, 𝔨_rec^ϱ and 𝔨_rec^0 formed with the same
constants of first order.

*Proof.* In each of these lemmas the second derivatives are recovered only through [[eq:tl5-hf-recovery]], at points of
Q(a, b) (at p in [[lem:tl5-hfv-rec]]), for the tensor H of the solution, and divided by 1 − (4/3)|H| ≥ 5/6: this gives
the factor (6/5)(√3 + 8/3) of K_rec, the factor (6/5)𝔯₀ with its weight, and the factor 8/5 of |𝔣|, which stands in
front of the couplings 𝔄 in k₁^(j,·), of the residual in k₂ = (8/5)q₁ and of the nonlinear terms in every constant of
absorption. At these points |H| ≤ 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 ≤ 1/16, so [[lem:tl5-hfz-rec]] with 𝔥 := 𝔰₁^v gives the same bound
with 𝔨_♯, (1 − 𝔰₁^v)⁻¹ 𝔯_♯ and (1 − 𝔰₁^v)⁻¹ in place of these three factors. The constants named are formed from these
factors as before; so the linear parts of the bounds hold with k₁^(j,·,z), k₂^z and the 𝔨_rec^(·,z), and the nonlinear
parts with every constant of absorption multiplied by (5/8)(1 − 𝔰₁^v)⁻¹. With 𝔰 ≤ 𝔰₁^v each of these products with 𝔰 is
at most 𝔵^z on Q(a, b), at level four as k₃^♮(μ) ≤ k₃^♮(ν); so the proof of [[lem:tl5-hfy-abs]] holds with 𝔵^z in place
of 𝔵. Finally 𝔨_♯ ≤ 𝔨_♯(1/16) < 2.45 < (6/5)(√3 + 8/3), (1 − 𝔰₁^v)⁻¹ ≤ 16/15 < 8/5, 2(1 − 𝔰₁^v)⁻¹ ≤ (6/5)(8/3) and
(1 − 𝔰₁^v)⁻¹ ≤ (6/5)√2, which give the inequalities, with 𝔵^z = (5/8)(1 − 𝔰₁^v)⁻¹ 𝔵 ≤ (2/3)𝔵 and 𝔵 ≤ 1/4. ∎

**Lemma {#lem:tl5-hfz-words}** (The second derivatives counted over the words.) In the setting of [[lem:tl5-hfz-abs]],
with 𝔰 ≤ 𝔰₁^v on Q(a, b), let |B| ≤ N − 3.

(a) Let r_B and c_B be the largest of the sums of μ^((|B|+3−|K|)/2) ‖𝔄_(JB,K)‖ over K for fixed J and over J for fixed
K, at a point. Then 𝔞_𝔄(B) ≤ (r_B c_B)^(1/2) ≤ 43^(1/2) r_B ≤ (43/2)^(1/2) α_𝔄^(N−1,μ) there; so 𝔩₀ ≤ 43^(1/2) k₁^z and
𝔩 ≤ 43^(1/2) (k₁^z + 2𝔵^z)/(1 − 𝔵^z).

(b) By [[lem:tl5-hfz-abs]], the first-order step of the lemma in use bounds |D̂²Ψ_(JB)| at the points of Σ₁(a, b), for
every word J of rotations with |J| ≤ 2, by μ^(−(|B|+3)/2) 𝒥_g (k₁^z + 2𝔵^z)/(1 − 𝔵^z) + P_ϱ, where P_ϱ := w k₂^z
ϱ(p)/(1 − 𝔵^z) with w = 1 in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a), w = μ^(−(|B|+3)/2) in
[[lem:tl5-hft-small]] (b) and w = ν^(−(|B|+3)/2) in [[lem:tl5-hfq-theta]]. Then at those points, the sum being over the
43 words J,

    (Σ_J |D̂²Ψ_(JB)|²)^(1/2) ≤ μ^(−(|B|+3)/2) 𝔩 𝒥_g + 43^(1/2) P_ϱ.                                  {#eq:tl5-hfz-words}

*Proof.* (a) Write a_JK := μ^((|B|+3−|K|)/2) 𝔄_(JB,K). For a family (ξ_K), the Cauchy–Schwarz inequality gives |Σ_K a_JK
ξ_K|² ≤ (Σ_K ‖a_JK‖)(Σ_K ‖a_JK‖ |ξ_K|²) ≤ r_B Σ_K ‖a_JK‖ |ξ_K|², and summing over J gives Schur's bound (r_B c_B)^(1/2).
Each term of a sum over J is at most r_B, so c_B ≤ 43 r_B. As |B| + 3 ≥ |JB| + 1, the sum over K for fixed J is at most
Σ_K μ^((|JB|+1−|K|)/2) ‖𝔄_(JB,K)‖ ≤ 2^(−1/2) α_𝔄^(N−1,μ). Then 𝔩₀ = k₁^z + (1 − 𝔰₁^v)⁻¹ (𝔞_𝔄 − α_𝔄^(N−1,μ)) ≤ k₁^z +
(43^(1/2) − 1)(1 − 𝔰₁^v)⁻¹ α_𝔄^(N−1,μ) ≤ 43^(1/2) k₁^z, and 43^(1/2) (k₁^z + 2𝔵^z) − (1 − 𝔵^z) 𝔩 = (1 −
𝔵^z)(43^(1/2) k₁^z − 𝔩₀) ≥ 0.

(b) Let q be a point of Σ₁(a, b) and C := JB. As |H(q)| ≤ 𝔰(q) ≤ 𝔰₁^v, [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v applies to Ψ_C,
with 𝔣 = Σ_K 𝔄_CK(D̂Ψ_K, Ψ_K) + Σ_K 𝔔_CK ℒ^K(2R̂ic) − 𝔑_C, 𝔑_C the nonlinear terms of the proof of
[[lem:tl5-hf-linfty]]. Take the Euclidean norm over J and apply Minkowski's inequality to each kind of term. The words
ZJB are distinct for distinct (Z, J) and have length at most |B| + 3 ≤ N, so (Σ_J Σ_Z |D̂Ψ_(ZJB)|²)^(1/2) ≤
μ^(−(|B|+3)/2) 𝒥_g. The words JB are distinct and have length at most |B| + 2, and (Σ_Z 𝔷_Z²)^(1/2) ≤ √7
(3 max_Z |D̂Z| + 2 max_Z |D̂²Z|)(|D̂Ψ_C|² + |Ψ_C|²)^(1/2); so the terms with 𝔷_Z and with 𝔯_♯ |Ψ_C| contribute at most
μ^(1/2) μ^(−(|B|+3)/2) 𝒥_g times their coefficients. As Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², the definition of 𝔞_𝔄(B)
bounds the terms with 𝔄 by (1 − 𝔰₁^v)⁻¹ μ^(−(|B|+3)/2) 𝔞_𝔄(B) 𝒥_g. Together these contribute at most μ^(−(|B|+3)/2) 𝔩₀
𝒥_g. For each J, (1 − 𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) ≤ (1 − 𝔵^z) P_ϱ, as w ≥ 1; and, as in the proof of the
bound of |D̂²Ψ_C| that the step uses, (1 − 𝔰₁^v)⁻¹ |𝔑_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐), 𝔐 that bound for the second
derivatives of the words of length at most |C|, whose weights are at most μ^(−(|B|+3)/2) and w as |C| + 1 ≤ |B| + 3; so
𝔐 ≤ μ^(−(|B|+3)/2) 𝒥_g (k₁^z + 2𝔵^z)/(1 − 𝔵^z) + P_ϱ. For each J these two terms are thus at most P_ϱ + μ^(−(|B|+3)/2)
𝒥_g 𝔵^z (k₁^z + 2)/(1 − 𝔵^z), which does not depend on J, so their Euclidean norm over the 43 words J is at most
43^(1/2) times it. Adding the parts gives [[eq:tl5-hfz-words]]. ∎

**Lemma {#lem:tl5-hfz-c1}** (The first-order constant with index z.) In the setting of [[lem:tl5-hfz-abs]], with 𝔰 ≤
𝔰₁^v on Q(a, b), the first-order step of the lemma in use, [[lem:tl5-hfs-linfty]], [[lem:tl5-hft-small]] or
[[lem:tl5-hfq-theta]], gives its bound of D̂Ψ_B(p), |B| ≤ N − 3, with C₁^z and C_(1,ϱ)^z of [[eq:tl5-hfz-c1]] in place
of C₁^x and C_(1,ϱ), with the weights of that step and its part with η₀. Moreover C₁^z ≤ C₁^x and C_(1,ϱ)^z ≤ C_(1,ϱ),
these being formed as in [[thm:tl5-hfy]].

*Proof.* Let A := D̂Ψ_B. By Minkowski's inequality over the words and the bounds of R′_J and D̂R′_J in the proof of
[[lem:tl5-hfx-c1]], at the points of Σ₁(a, b), (Σ_J |ℒ^J A|²)^(1/2) ≤ μ^(−(|B|+3)/2) (1 + ϖ′^(1/2)) 𝒥_g and (Σ_J |D̂ℒ^J
A|²)^(1/2) ≤ (Σ_J |D̂²Ψ_(JB)|²)^(1/2) + μ^(−(|B|+3)/2) (2ϖ′)^(1/2) 𝒥_g; by [[eq:tl5-hfz-words]] the latter is at most
μ^(−(|B|+3)/2) (𝔩 + (2ϖ′)^(1/2)) 𝒥_g + 43^(1/2) P_ϱ. Let ∫ denote the integral over Σ₁(a, b) with dμ dτ₂/(1 − κκ′), and
put W := 2|∂_γ|² 𝔳⁶ R⁻³, F := ∫ 𝔳⁶ R⁻³ (1 + 18|D̂∂_γ|²) Σ_J |ℒ^J A|², P² := μ^(−(|B|+3)) ∫ W (𝔩 + (2ϖ′)^(1/2))² 𝒥_g² and
V² := 43 ∫ W P_ϱ². By Minkowski's inequality in L² of the face, ∫ W Σ_J |D̂ℒ^J A|² ≤ (P + V)²; so the right side of
[[eq:tl5-hf-cs-r]] with r = 3, or of its form in [[lem:tl5-hft-face]] (a), is at most 6C² 𝔴(p)⁶ (F + (P + V)² + S), S
its term on S_a, and

    (F + (P + V)² + S)^(1/2) ≤ (F + P²)^(1/2) + V + S^(1/2).

As in the proof of [[lem:tl5-hf-linfty]], |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) on the face, so ∫ f 𝒥_g² ≤
sup (f 𝔨₂) ℰ_g(p) for every function f ≥ 0, and 6C² 𝔴(p)⁶ (F + P²) ≤ μ^(−(|B|+3)) C₁^z² ℰ_g(p). Next 6C² 𝔴(p)⁶ V² ≤
w² C_(1,ϱ)^z² ϱ(p)², as P_ϱ = w k₂^z ϱ(p)/(1 − 𝔵^z) with w and ϱ(p) numbers; and S is bounded as in the proof of
[[lem:tl5-hfx-c1]]. This is the bound of the step with C₁^z and C_(1,ϱ)^z.

For the comparison let 𝔨 := (k₁^z + 2𝔵^z)/(1 − 𝔵^z) and Λ := Λ₂^μ, so that ϖ′ ≤ 1320 Λ² as in [[rem:tl5-hfx-what]], 𝔩 ≤
43^(1/2) 𝔨 by [[lem:tl5-hfz-words]] (a), and 𝔨 ≤ (k₁^μ + 2𝔵)/(1 − 𝔵) ≤ 2(k₁^μ + 1) by [[lem:tl5-hfz-abs]], as (k, x) ↦
(k + 2x)/(1 − x) is increasing in each argument and 𝔵 ≤ 1/4. At each point of the face 2(𝔩 + (2ϖ′)^(1/2))² ≤
4(43^(1/2) 𝔨 + (2ϖ′)^(1/2))², which compares C₁^z with the second entry of C₁^x. Also 2(𝔩 + (2ϖ′)^(1/2))² ≤ 4𝔩² + 8ϖ′ ≤
43 · 4 (72Λ² + 2𝔨²) and (1 + ϖ′^(1/2))² ≤ (1 + 37Λ)² ≤ 43 (1 + 6Λ)², which compare it with C₁^♮, whose term with k₁^μ is
4|∂_γ|² · 2(2(k₁^μ + 1))², or 4|∂_γ|² · 2((k₁^μ + 2𝔵)/(1 − 𝔵))² with the replacements of [[lem:tl5-hfy-abs]], both at
least 4|∂_γ|² · 2𝔨². Finally 2(k₂^z)²/(1 − 𝔵^z)² ≤ 8k₂²/(1 − 𝔵)². ∎

**Theorem {#thm:tl5-hfz}** (Existence with the recovery sharpened and counted over the words.) In the setting of
[[thm:tl5-hfy]] let S_F^z, S_M^z, ε_M^z and 𝔯^z be S_F^v, S_M^v, ε_M^v and 𝔯^v formed with the constants with index z of
[[def:tl5-hfz-constants]], and put

    ε^z := 𝒮[s_N[2R̂ic] + 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^v k₂^z ϱ],      η_z := 1 − max(ϑ₁, ϑ₂) − 𝔯^z,
    A_z := η_z^(−1/2) δ_w + η_z⁻¹ (ε^z + ε_M^z),      B_z := η_z⁻¹ (S_F^z + S_M^z),

and let 𝔰_*^z be 𝔰_*^w formed with the constants with index z and with A_z in place of A_w^v. Suppose: (a) η₀ < 𝔰₁^v;
(b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_z > 0, 𝔰_*^z < 𝔰₁^v and the
closing condition

    4 A_z B_z = 4 η_z^(−3/2) (δ_w + η_z^(−1/2) (ε^z + ε_M^z)) (S_F^z + S_M^z) < 1.                 {#eq:tl5-hfz-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_z and 𝔰_*^z in place of A_w (or
A_(w,4)) and 𝔰_*. Each constant with index z, and each of ε^z, A_z, B_z and 𝔰_*^z, is at most the one of [[thm:tl5-hfy]]
it replaces, and η_z is at least η; so the hypotheses of [[thm:tl5-hfy]] imply these.

*Proof.* The proof of [[thm:tl5-hfy]] applies with [[lem:tl5-hfz-abs]] and [[lem:tl5-hfz-c1]] in place of
[[lem:tl5-hfy-abs]] and [[lem:tl5-hfx-c1]]. In Step 1, Σ_* is the set of σ with 𝔰 ≤ 𝔰₁^v on D^κ_σ, as there; for σ ∈ Σ_*
and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ, so the two lemmas apply at p and give 𝔰(p) ≤ 𝔰_*^z < 𝔰₁^v, and Σ_* = [1/2, s] as
there. Steps 2 and 3 use their bounds in place of those they replace; in the terms with ϱ of Step 2, k₂^z 𝔰 ϱ/(1 − 𝔵^z)
≤ 𝔰₁^v k₂^z ϱ/(1 − 𝔵^z) gives ε^z. The rest is the proof of [[thm:tl5-hfv]] with A_z, B_z and [[eq:tl5-hfz-closing]].
For the last claim, k₁^(j,·,z), k₂^z, 𝔵^z, the 𝔨_rec^(·,z), C₁^z and C_(1,ϱ)^z are at most the numbers they replace, by
[[lem:tl5-hfz-abs]] and [[lem:tl5-hfz-c1]]; every constant of [[thm:tl5-hfy]], ε^w and 𝔯^v are nondecreasing in these
numbers, so η_z ≥ η, and A_w^v, B_v and 𝔰_*^w are nonincreasing in η and nondecreasing in the constants. ∎

**Remark {#rem:tl5-hfz-what}** (What changes.) The recovery constant loses the factor 6/5 of 1 − (4/3)|H| ≥ 5/6, and its
coefficient √3 + 8/3 of K_rec becomes 𝔨_♯, which lies between √5 and 𝔨_♯(1/16) < 2.45; so the factor (6/5)(√3 +
8/3) > 5.27 becomes about √5 < 2.24 when 𝔰₁^v is small, in k₁^(j,·), in 𝔨_rec, and through the bounds of the second
derivatives in 𝔨_A, λ_t^μ, λ_t^(μ,2) and C₁^z. The factor 8/5 in front of the residual and of the nonlinear terms
becomes (1 − 𝔰₁^v)⁻¹ ≤ 16/15, which lowers k₂ and k₃, and with k₃ the number 𝔵, by the factor (5/8)(1 − 𝔰₁^v)⁻¹ ≤ 2/3.
In the part of C₁^z with 𝒥_g the count 43 of the words remains only in the nonlinear part 43^(1/2) 𝔵^z (k₁^z + 2)/(1 −
𝔵^z), against 43^(1/2) (k₁^μ + 2𝔵)/(1 − 𝔵) in [[eq:tl5-hfx-c1]] with the replacements of [[lem:tl5-hfy-abs]]: the
nonlinear terms are bounded through the largest second derivative and are not absorbed over the words, so no condition
on 43^(1/2) 𝔵^z is needed. The couplings 𝔄 enter through the norm 𝔞_𝔄 of their family over the words, which any bound of
it may replace, Schur's (r_B c_B)^(1/2) among them, and which is at most (43/2)^(1/2) α_𝔄^(N−1,μ). The triangle
inequality on the face halves the term with |∂_γ|² of the square of C₁^z against the split (x + y)² ≤ 2x² + 2y² of
[[eq:tl5-hfx-c1]], and quarters the square of C_(1,ϱ)^z against the two splits of C_(1,ϱ); it is at least as good as
(x + y)² ≤ (1 + δ)x² + (1 + 1/δ)y² for every δ > 0, which would move a factor between the two parts, so no such number
is needed. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfz]] are established in this paper
for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD fa3fa0f0, where sec:tl5-hfy is merged (Section 57.23,
merge 7b592452). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfz) through the last line of
[[rem:tl5-hfz-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfy-what]] (line 6392, as
changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfy-what]] (lines 6391–6392).* Old:

replaces. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper
for no background at 10 l5.

New:

replaces. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfy]] are established in this paper
for no background at 10 l5. [[sec:tl5-hfz]] sharpens the recovery and counts it over the words ([[thm:tl5-hfz]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. Every factor below replaces one of thm:tl5-hfy and is at most it, so thm:tl5-hfz contains
thm:tl5-hfy (its last sentence). The thresholds 𝔰₀, 𝔰₁^v (and the cap 𝔰_(θ,v)) are unchanged and still formed with k₃.

1. The recovery coefficient of K_rec. 𝔨_♯ := (1 + (2 + √2 𝔰₁^v)²/(1 − 𝔰₁^v)²)^(1/2) replaces (6/5)(√3 + 8/3) =
   5.27846 in every k₁^(j,ν′) (every level j, weights μ, ν, 1) and in 𝔨_rec, 𝔨_rec^ϱ, 𝔨_rec^0. 𝔨_♯ = √5 + 3.05 𝔰₁^v +
   O((𝔰₁^v)²); √5 = 2.23607; 𝔨_♯(1/16) = 2.44178. At 𝔰₁^v ≤ 10⁻⁴ the ratio is 0.4236, −0.373 decades.
2. The coefficient of |𝔣|. (1 − 𝔰₁^v)⁻¹ replaces 8/5: in front of α_𝔄^(j,ν′) in k₁^(j,ν′); in k₂, so k₂^z = q₁/(1 −
   𝔰₁^v) = (5/8)(1 − 𝔰₁^v)⁻¹ k₂ wherever k₂ enters (C_(1,ϱ), C_(∞,ϱ), C_(P,ϱ)^v through "𝔨_rec^ϱ + k₂", ς_t and so
   𝔯_M and ε_M, the products' terms with ϱ, ε); and in the absorption, so 𝔵^z = (5/8)(1 − 𝔰₁^v)⁻¹ 𝔵 ≤ 2𝔵/3 replaces
   𝔵 in every replacement of lem:tl5-hfy-abs: 1/(1 − 𝔵^z), (k₁^z + 2𝔵^z)/(1 − 𝔵^z), k₂^z/(1 − 𝔵^z).
3. The coefficient of |Ψ|. 𝔯_♯/(1 − 𝔰₁^v), 𝔯_♯ = 2‖𝓡̂‖ + ‖𝒞_(·1)‖, replaces (6/5)𝔯₀ = (6/5)((8/3)‖𝓡̂‖ +
   √2‖𝒞_(·1)‖), with the same weights (μ^(1/2) in k₁^(j,μ), μ in 𝔨_rec, 𝔨_rec^0).
   So k₁^(j,ν′,z) = 𝔨_♯ K_rec (1 + ν′^(1/2) √7 (3 max|D̂Z| + 2 max|D̂²Z|)) + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),
   against k₁^(j,ν′) = (6/5)((√3 + 8/3) K_rec (1 + ν′^(1/2) √7 (…)) + ν′^(1/2) 𝔯₀ + (4/3) α_𝔄^(j,ν′)).
4. The first-order constant. C₁^z of eq:tl5-hfz-c1 replaces C₁^x = min(C₁^♮, second entry) everywhere (C_P^v directly
   and, at level four, through 𝔨_rec^z; 𝔎, S_F; C_(∞,μ)^(N−4) in 𝔰_*). No minimum is needed: lem:tl5-hfz-c1 proves
   C₁^z ≤ both entries pointwise in the integrand.
   C₁^z² = 6C²𝔴(p)⁶ sup 𝔳⁶R⁻³𝔨₂((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 2|∂_γ|²(𝔩 + (2ϖ′)^(1/2))²),
   against the second entry 6C²𝔴(p)⁶ sup 𝔳⁶R⁻³𝔨₂((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 4|∂_γ|²(√43 (k₁^μ + 2𝔵)/(1 − 𝔵) +
   (2ϖ′)^(1/2))²), where
   𝔩 = 𝔩₀ + √43 𝔵^z (k₁^z + 2)/(1 − 𝔵^z), 𝔩₀ = k₁^z with 𝔞_𝔄 in place of α_𝔄^(N−1,μ), k₁^z = k₁^(N−1,μ,z).
   So the k-term of the bracket goes from √43 (k₁^μ + 2𝔵)/(1 − 𝔵) to 𝔩, and its factor 4|∂_γ|² to 2|∂_γ|².
5. The coupling norm over the words. 𝔞_𝔄 = max_B 𝔞_𝔄(B), 𝔞_𝔄(B) the operator norm of the block matrix
   (μ^((|B|+3−|K|)/2) 𝔄_(JB,K))_(J,K), J over the 43 rotation words, K over the words with |K| ≤ |B| + 2. Any upper bound
   may be used: Schur's (r_B c_B)^(1/2) (largest row sum times largest column sum of the block norms, under the root), or
   the trivial (43/2)^(1/2) α_𝔄^(N−1,μ), which already gives 𝔩₀ ≤ √43 k₁^z. At G0k's points every coupling carries a weight
   μ^(1/2) or smaller (μ = 10⁻⁶ … 10⁻⁴), so 𝔞_𝔄 is negligible against 𝔨_♯ K_rec whichever bound is used, and the
   Schur bound only matters at larger μ.
6. C_(1,ϱ)^z: 2(k₂^z)²/(1 − 𝔵^z)² in place of 8k₂²/(1 − 𝔵)² of thm:tl5-hfy (32k₂² in lem:tl5-hf-linfty); with k₂^z this
   is C_(1,ϱ) × (1/2)(5/8)(1 − 𝔰₁^v)⁻¹ (1 − 𝔵)/(1 − 𝔵^z) ≈ × 0.30 (−0.52 decades). It enters C_(∞,ϱ), 𝔨_rec^(ϱ,z),
   C_(P,ϱ)^v, 𝔎_ϱ, 𝔯, and the terms with ϱ of 𝔰_*.
7. ε^z: coefficient of ϱ 𝔰₁^v (1 − 𝔵^z)⁻¹ 𝔤_ϱ^v k₂^z in place of 𝔰₁^v (1 − 𝔵)⁻¹ 𝔤_ϱ^v k₂, ratio (5/8)(1 − 𝔰₁^v)⁻¹(1 −
   𝔵)/(1 − 𝔵^z) ≈ 0.63 (−0.20 decades).
8. The closing condition eq:tl5-hfz-closing has the form of eq:tl5-hfw-closing with η_z, ε^z, ε_M^z, S_F^z, S_M^z.

The optimised split (target 3). Not needed as a parameter: the triangle inequality in L² of the face gives the factors
(1, 1) on the parts with 𝒥_g and with ϱ, against (2, 2) for the single split and (1 + δ, 1 + 1/δ) for every δ > 0.
Against thm:tl5-hfy this is C₁ ÷ √2 on the k-term (G0k's δ = 0.01 price) with C_(1,ϱ) ÷ 2 instead of × 7.1.

What it gives, deduced, not evaluated. Assumptions: k₁^μ ≈ 5.3 at the supremum, as G0k reports, carried by its first
term, so K_rec ≈ 1.00; the 𝔄, 𝔯 and 𝔷 terms negligible (weights μ^(1/2)); the k-term the whole bracket of C₁. At G0k's
level-4 optima (𝔵 = 0.073, 0.099, 0.086, 0.147; 𝔰₁^v ≤ 2 × 10⁻⁵):
- k₁^z ≈ 2.245, 𝔵^z ≈ 0.046, 0.062, 0.054, 0.092; per-word (k₁ + 2𝔵)/(1 − 𝔵) ≈ 5.9–6.6 → 2.45–2.68;
- the k-term √43 (k₁^μ + 2𝔵)/(1 − 𝔵) ≈ 38.5, 40.0, 39.3, 43.0 → 𝔩 ≈ 3.58, 4.08, 3.83, 5.06; with 4 → 2 under the root,
  C₁ falls by about 1.18, 1.14, 1.16, 1.08 decades;
- 𝔨_rec carries 𝔨_♯ as well: where 𝔨_rec is the largest entry of C_P^v (𝔨_rec ≈ 5.3 √7 C₁ against C₁ and 2C_S), C_P^v
  falls by about 1.57, 1.53, 1.55, 1.48 decades (with the outer 1/(1 − 𝔵^z), 0.01–0.03);
- if f keeps moving 1:1 with C_P (G0k), f could gain up to that much at level 4, until the 𝔰_* slack, ϱ (C_(1,ϱ) ×
  0.30, k₂ × 0.63 help it) or the part of C₁'s bracket without k₁ binds. This needs the evaluation.
Level 6 (𝔵 = 0.003–0.07, ϱ binds): the ε coefficient of ϱ falls by about 0.20 decades (k₂^z), and C_(1,ϱ) by 0.52;
C₁^z and 𝔨_♯ enter C_P^v = C_(∞,μ)^(1) and 𝔰_*, where f is not binding.

Not done.
- Target 4 (the word count 7² in 𝔤_(𝒥,s) and 𝔠^♮₄(μ) against 9·2⁴): not attempted.
- A further lever found, not taken: in 𝔨_rec the seven fields Z enter as √7 max_Z |D̂Ψ_Z(p)|. The argument of
  lem:tl5-hfz-words and lem:tl5-hfz-c1 applies to the family (D̂Ψ_Z)_Z at once (the words JZ and Z′JZ are distinct, and
  Z ↦ σZ is injective in the remainders, as in lem:tl5-hfq-mixed), giving C₁ with √301 𝔵^z in place of √43 𝔵^z in 𝔩
  and √7 only on the parts with ϱ and η₀, in place of √7 C₁. Deduced worth at G0k's 𝔵: 0.14–0.22 decades on 𝔨_rec.
- The nonlinear part keeps its count √43 per word: it is bounded through the maximum of the second derivatives, whose
  words are not of the form J′B, so an ℓ² absorption over J is not available without a new bound of the nonlinear
  terms over the words. The theorem needs no condition on √43 𝔵^z; at G0k's 𝔵^z it is 1.3–2.8 of 𝔩.
- 𝔨_♯ → √5 is the best this argument gives: its inequalities are equalities when X lies on the diagonal with
  D̂²Ψ(0, 0) = −D̂²Ψ(j, j) and 𝔣 = Ψ = 0, H = 0. A smaller k₁ needs more structure of the frame components.
- 1/z̲ in 𝔨₂, the rank-3 Sobolev constant and the 1/κ′ part: not attempted.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfz	paper/reader/proofs/P-GRD9.md@PENDING:1	P-GRD9, section	new; at the end of ch:ten-l5, after rem:tl5-hfy-what; recovery sharpened and counted over the words
    lem:tl5-hfz-rec	paper/reader/proofs/P-GRD9.md@PENDING:15	P-GRD9, Lemma	recovery with |H| <= h and the entry (1,1) apart: k#(h) = (1 + (2 + sqrt2 h)^2/(1 - h)^2)^(1/2) for (6/5)(sqrt3 + 8/3), 1/(1 - h) for 8/5, (2|R| + |C|)/(1 - h) for (6/5)r0
    eq:tl5-hfz-rec	paper/reader/proofs/P-GRD9.md@PENDING:23	P-GRD9, display	new
    def:tl5-hfz-constants	paper/reader/proofs/P-GRD9.md@PENDING:47	P-GRD9, Definition	constants with index z: k1^(j,nu,z), k2^z, k3^z, x^z = (5/8)(1 - s1^v)^-1 x, krec^z, coupling norm a_A(B) over the words, l0, l, C1^z, C1rho^z
    eq:tl5-hfz-c1	paper/reader/proofs/P-GRD9.md@PENDING:70	P-GRD9, display	new
    lem:tl5-hfz-abs	paper/reader/proofs/P-GRD9.md@PENDING:77	P-GRD9, Lemma	the lemmas of lem:tl5-hfy-abs with the recovery constants of index z; each at most the old one
    lem:tl5-hfz-words	paper/reader/proofs/P-GRD9.md@PENDING:97	P-GRD9, Lemma	second derivatives of the words JB in l2 over the 43 words: leading term once, couplings through a_A (Schur bound), nonlinear part with sqrt43
    eq:tl5-hfz-words	paper/reader/proofs/P-GRD9.md@PENDING:110	P-GRD9, display	new
    lem:tl5-hfz-c1	paper/reader/proofs/P-GRD9.md@PENDING:134	P-GRD9, Lemma	first-order bound with C1^z, C1rho^z by the triangle inequality in L2 of the face; C1^z <= C1^x, C1rho^z <= C1rho
    thm:tl5-hfz	paper/reader/proofs/P-GRD9.md@PENDING:164	P-GRD9, Theorem	thm:tl5-hfy with the constants with index z; contains it
    eq:tl5-hfz-closing	paper/reader/proofs/P-GRD9.md@PENDING:175	P-GRD9, display	closing condition: 4 eta_z^(-3/2)(delta_w + eta_z^(-1/2)(eps^z + eps_M^z))(S_F^z + S_M^z) < 1
    rem:tl5-hfz-what	paper/reader/proofs/P-GRD9.md@PENDING:190	P-GRD9, Remark	what changes

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfy-what, add "; points to sec:tl5-hfz
(P-GRD9 item 2)".
