### The products with no factor at a point, with the weights and the families of words {#sec:tl5-hfu}

This section carries the leaf constant, the weights of the words and the counting over families of words of
[[sec:tl5-hfp]] into the products of level four with no factor at a point, that is into the numbers S_M, 𝔯_M and ε_M of
[[def:tl5-hfq-constants]]. Four changes are made. First, the Sobolev inequality on the leaves in [[lem:tl5-hf4-face]]
(b) takes the weights 𝔶 and the constant C_(E,r)(𝔶) of [[lem:tl5-hfp-leaf]], and the inequality along the curves γ_ω in
(a) keeps the coefficients of |A|² and of |D̂A|² apart ([[lem:tl5-hfu-face]]). Second, the second derivatives of a
family of words are bounded in the Euclidean norm over the family, the leading term of the recovery counting once
([[lem:tl5-hfu-fam]]); this replaces the count 7 of the 49 words of length two in 𝔜_(1,t) and the count √602 of the
second derivatives in 𝔛_(2,t). Third, the remainders are added to the leading terms by the triangle inequality over the
words in place of (x + y)² ≤ 2x² + 2y², and those of the second derivatives gain a factor μ^(1/2) from the weights of
the energies. Fourth, the terms with η₀ keep the factor μ^(3/2) of the step, and those with ϱ the weights of
[[lem:tl5-hfq-theta]] ([[lem:tl5-hfu-mixed]]). The closing condition is [[eq:tl5-hfu-closing]]; for 𝔶₀, 𝔶₁ ≥ 1 every new
constant is at most the one it replaces, and the earlier closing conditions remain valid. [[lem:tl5-hfu-fam]] holds for
every N ≥ 4; the rest of the section is at level four, with the intrinsic Sobolev constants of [[lem:tl5-hft-face]], and
the notation is that of [[sec:tl5-hfp]].

**Lemma {#lem:tl5-hfu-face}** (The inequalities on a face, with weights and with the coefficients apart.) Let t, b, Σ,
γ_ω, S_t and the norms be as in [[lem:tl5-hf4-face]], in the form of [[lem:tl5-hft-face]] (c), let 𝔶₀, 𝔶₁ > 0, 𝔶₂ := 1
and C_(E,r)(𝔶) be as in [[lem:tl5-hfp-leaf]], and put

    𝔱_(r,0)(t) := [𝔳₀^(2r) R⁻³ (1 + 2r² |D̂∂_γ|²)]_t,      𝔱_(r,1)(t) := [2 𝔳₀^(2r) R⁻³ |∂_γ|²]_t,

both at most 𝔱_r(t). Then for every smooth covariant tensor field A of rank r with 1 ≤ r ≤ 4 on Q(t, b), the sum being
over the words J of length at most two in the six rotations,

    ⟦A⟧_(2,∞)² ≤ C_(E,r)(𝔶)² 𝔵_r(t) Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖_Σ²,
    ⟦A⟧_(∞,2)² ≤ [𝔳₀^(2r)]_t ∫_(S_t) |A|² dω + 𝔱_(r,0)(t) ‖A‖_Σ² + 𝔱_(r,1)(t) ‖D̂A‖_Σ².               {#eq:tl5-hfu-face}

*Proof.* For the first inequality fix v, as in the proof of [[lem:tl5-hf4-face]] (b) in the form of [[lem:tl5-hft-face]]
(c). The points γ_ω(v), ω ∈ S³, fill one leaf, and [[eq:tl5-hfp-leaf]] applied to A on it gives sup_ω |A|₀²(γ_ω(v)) ≤
C_(E,r)(𝔶)² Σ_J 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀²(γ_ω(v)) dω. With |ℒ^J A|₀ ≤ 𝔳₀^r |ℒ^J A|, multiply by e^(−φ), which is constant
on the leaf, integrate over v and use dω dv = R⁻³ dμ dτ₂/(1 − κκ′); the supremum of 𝔳₀^(2r) R⁻³ over Σ ⊂ Σ₁(t, v*) is at
most 𝔵_r(t). For the second, the proof of [[lem:tl5-hf4-face]] (a) in that form bounds e^(−φ(v)) ∫_(S³) |A|₀²(γ_ω(v)) dω
by ∫_(S_t) |A|₀² dω plus the integral over the part of Σ with v′ ≤ v, with e^(−φ) dω dv′, of |A|₀² + |ℒ_(∂_γ)A|₀² ≤
𝔳₀^(2r) ((1 + 2r²|D̂∂_γ|²) |A|² + 2|∂_γ|² |D̂A|²). With dω dv′ = R⁻³ dμ dτ₂/(1 − κκ′), bounding the two coefficients
times 𝔳₀^(2r) R⁻³ by their own suprema, in place of their largest, and |A|₀² by 𝔳₀^(2r) |A|² on S_t gives the second
inequality. ∎

**Lemma {#lem:tl5-hfu-fam}** (The second derivatives over a weighted family of words.) In the setting of
[[lem:tl5-hfz-abs]] and [[def:tl5-hfp-constants]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), let 𝔙 be a family of n distinct words C
with |C| ≤ j ≤ N − 1, each with a number 𝔬_C > 0 such that 𝔬_C² ≤ μ^(|C|+1). Let 𝔞_𝔄(𝔙) be, at each point, the operator
norm of the map

    (ξ_K)_(|K|≤N) ↦ (Σ_K 𝔬_C μ^(−|K|/2) 𝔄_CK ξ_K)_(C∈𝔙),

𝔄_CK := 0 for |K| > |C|, normed as in [[def:tl5-hfz-constants]], and put

    𝔩(𝔙) := k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙) + n^(1/2) 𝔵^z (k₁^(j,μ,p) + 2)/(1 − 𝔵^z).

Let w_C be the weight of the part with ϱ(p) of the bound of |D̂²Ψ_C| in the lemma in use: 1 in [[lem:tl5-hfs-linfty]]
and [[lem:tl5-hft-small]] (a), μ^(−(|C|+1)/2) in [[lem:tl5-hft-small]] (b) and ν^(−(|C|+1)/2) in [[lem:tl5-hfq-theta]].
Then at every point of Q(a, b)

    (Σ_(C∈𝔙) 𝔬_C² |D̂²Ψ_C|²)^(1/2) ≤ 𝔩(𝔙) 𝒥_g + (Σ_(C∈𝔙) 𝔬_C² w_C²)^(1/2) k₂^z ϱ(p)/(1 − 𝔵^z).         {#eq:tl5-hfu-fam}

Moreover 𝔞_𝔄(𝔙) ≤ (n/2)^(1/2) α_𝔄^(j,μ) and 𝔩(𝔙) ≤ n^(1/2) (k₁^(j,μ,p) + 2𝔵^z)/(1 − 𝔵^z).

*Proof.* Let q be a point of Q(a, b) and C ∈ 𝔙. As |H(q)| ≤ 𝔰(q) ≤ 𝔰₁^v, [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v applies to
Ψ_C at q, with 𝔣 and 𝔑′_C as in the proof of [[lem:tl5-hfz-words]] (b), and (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷′
(|D̂Ψ_C|² + |Ψ_C|²)^(1/2) as in the proof of [[lem:tl5-hfp-abs]] (b). Multiply by 𝔬_C, take the Euclidean norm over 𝔙
and apply Minkowski's inequality to each kind of term. A word determines its first letter and the word of its other
letters, so the words ZC, Z ∈ Γ, C ∈ 𝔙, are distinct, and 𝔬_C² ≤ μ^(|ZC|); the leading term therefore contributes at
most k₁^D 𝒥_g. The words C are distinct and 𝔬_C² ≤ μ μ^(|C|), so the terms with 𝔷_Z and with 𝔯_♯ |Ψ_C| contribute at
most μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) 𝒥_g, and, as Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g², the terms with 𝔄 at most
(1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙) 𝒥_g. For each C, (1 − 𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) and, as in the proof of
[[lem:tl5-hfz-words]] (b), (1 − 𝔰₁^v)⁻¹ |𝔑′_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐_C), where 𝔐_C is the bound of the second
derivatives of the words of length at most |C| that [[lem:tl5-hfp-abs]] (b) gives. The weights of that bound do not
decrease with the length and 𝒟_g ≤ 𝒥_g, so 𝔐_C ≤ μ^(−(|C|+1)/2) (k₁^(j,μ,p) + 2𝔵^z) 𝒥_g/(1 − 𝔵^z) + w_C k₂^z
ϱ(p)/(1 − 𝔵^z). As 𝔬_C μ^(−(|C|+1)/2) ≤ 1, w_C ≥ 1 and 2(1 − 𝔵^z) + k₁^(j,μ,p) + 2𝔵^z = k₁^(j,μ,p) + 2, 𝔬_C times these
two terms is at most 𝔵^z (k₁^(j,μ,p) + 2) 𝒥_g/(1 − 𝔵^z) + 𝔬_C w_C k₂^z ϱ(p)/(1 − 𝔵^z), and the Euclidean norm over 𝔙 of
the first part is n^(1/2) times it. Adding the parts gives [[eq:tl5-hfu-fam]]. For the last claims, the row of C of the
map defining 𝔞_𝔄(𝔙) has the sum Σ_K 𝔬_C μ^(−|K|/2) ‖𝔄_CK‖ ≤ Σ_K μ^((|C|+1−|K|)/2) ‖𝔄_CK‖ ≤ 2^(−1/2) α_𝔄^(j,μ), so each
of the n components of the image is at most 2^(−1/2) α_𝔄^(j,μ) times the norm of the family, which gives the first
bound. With it, and with k₁^(j,μ,p) = k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ α_𝔄^(j,μ), 𝔩(𝔙) ≤
n^(1/2) (k₁^(j,μ,p) + 𝔵^z (k₁^(j,μ,p) + 2)/(1 − 𝔵^z)) = n^(1/2) (k₁^(j,μ,p) + 2𝔵^z)/(1 − 𝔵^z). ∎

**Definition {#def:tl5-hfu-constants}** (The constants with index u.) Let N = 4 and the setting be that of
[[thm:tl5-hfp]], at level four with θ, ν = μ^θ and the weights 𝔶₀, 𝔶₁ of [[def:tl5-hfp-constants]], and let 𝔗(𝔶)² :=
(ν²𝔶₀ + 6ν𝔶₁ + 36)/43 be its number for [[lem:tl5-hfq-theta]]. Let 𝔙₂ be the family of the 49 words of length two, each
with the number μ^(3/2), and 𝔙_Γ the family of the 301 words JZ, J a word of rotations with |J| ≤ 2 and Z ∈ Γ, the word
JZ with the number (𝔶_(|J|) μ⁴)^(1/2); as 𝔶_k ≤ μ^(k−2), both satisfy the hypothesis of [[lem:tl5-hfu-fam]], with j = 2
and j = 3. With the notation of [[lem:tl5-hfs-mixed]], [[lem:tl5-hfq-mixed]] and [[lem:tl5-hfu-face]], 𝔵_r(t), 𝔱_r(t),
𝔪(t) and [𝔳₀^(2r)]_t formed as in [[lem:tl5-hft-face]] (c), and ς_t := [k₂^z]_t (1 − 𝔵^z)⁻¹ (∫_(Σ₁(t,v*)) dμ
dτ₂/(1 − κκ′))^(1/2), put

    𝔛^u_(1,t) := C_(E,3)(𝔶) 𝔵₃(t)^(1/2) (1 + [ϖ₁]_t^(1/2)),
    𝔛^u_(2,t) := C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ([𝔩(𝔙_Γ)]_t + μ^(1/2) [ϖ₂]_t^(1/2)),
    𝔛′^u_(2,t) := 301^(1/2) 𝔗(𝔶) (μ/ν)² C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ς_t,
    𝔜^u_(1,t) := (μ 𝔱_(3,0)(t) + 𝔱_(3,1)(t) [𝔩(𝔙₂)]_t²)^(1/2),      𝔜′^u_(1,t) := 7 (μ/ν)^(3/2) 𝔱_(3,1)(t)^(1/2) ς_t,
    𝔜″^u_(1,t) := μ^(3/2) π (98 [𝔳₀⁶]_t)^(1/2),      𝔜″^u_(2,t) := μ^(3/2) π (686 [𝔳₀⁴]_t)^(1/2),

and, with w_t as in [[def:tl5-hfs-constants]], 𝔠^Mq₁, 𝔠^Mq₂ as in [[eq:tl5-hfq-m]] and 𝔜_(2,t) = 𝔱₂(t)^(1/2),

    S_M^u := μ^(−3/2) ∫_(−10)^(u*) w_t (𝔠^Mq₁ 𝔛^u_(1,t) 𝔜^u_(1,t) + 𝔠^Mq₂ 𝔛^u_(2,t) 𝔜_(2,t)) [𝔨₂]_t dt,
    𝔯_M^u := μ^(−3/2) ∫_(−10)^(u*) w_t [𝔨₂]_t^(1/2) (𝔠^Mq₁ 𝔛^u_(1,t) (𝔜′^u_(1,t) ϱ + 𝔜″^u_(1,t) η₀)
             + 𝔠^Mq₂ (𝔛^u_(2,t) 𝔜″^u_(2,t) η₀ + 𝔛′^u_(2,t) 𝔜_(2,t) ϱ)) dt,
    ε_M^u := μ^(−3/2) ϱ η₀ ∫_(−10)^(u*) w_t 𝔠^Mq₂ 𝔛′^u_(2,t) 𝔜″^u_(2,t) dt.                      {#eq:tl5-hfu-constants}

**Lemma {#lem:tl5-hfu-mixed}** (The products with no factor at a point, with index u.) In the setting of
[[lem:tl5-hfq-mixed]] and [[def:tl5-hfu-constants]], with 𝔰 ≤ 𝔰₁^v on Q(t, b) and the constants with index p,
[[eq:tl5-hfs-mixed]] holds with 𝔛^u_(1,t), 𝔛^u_(2,t), 𝔛′^u_(2,t), 𝔜^u_(1,t), 𝔜′^u_(1,t), 𝔜″^u_(1,t) and 𝔜″^u_(2,t) in
place of 𝔛^q_(1,t), 𝔛^q_(2,t), 𝔛′_(2,t), 𝔜^q_(1,t), 𝔜′_(1,t), 𝔜″_(1,t) and 𝔜″_(2,t). For 𝔶₀, 𝔶₁ ≥ 1 each of these is at
most the one it replaces, formed with the constants with index p.

*Proof.* The first line of [[eq:tl5-hfs-mixed]] is unchanged. In the steps below [[lem:tl5-hfu-fam]] is applied on
Q(t, b), with ϱ in place of ϱ(p) as in the proof of [[lem:tl5-hfg-mixed]], and the bound of the lemma in use is that of
[[lem:tl5-hfq-theta]], so w_C = ν^(−(|C|+1)/2).

*μ² X₁.* By [[eq:tl5-hfu-face]] with r = 3, μ⁴ X₁² ≤ C_(E,3)(𝔶)² 𝔵₃(t) ‖(Σ_(J,B) 𝔶_(|J|) μ⁴ |ℒ^J D̂Ψ_B|²)^(1/2)‖_Σ², the
sum being over the 43 words J and the 49 words B of length two. At each point ℒ^J D̂Ψ_B = D̂Ψ_(JB) + R′_(J,B), as in the
proof of [[lem:tl5-hfs-mixed]]. The words JB are distinct, as the B have one length, and 𝔶_(|J|) μ⁴ ≤ μ^(|JB|), so
(Σ_(J,B) 𝔶_(|J|) μ⁴ |D̂Ψ_(JB)|²)^(1/2) ≤ 𝒥_g. A monomial of R′_(J,B) whose coefficient carries a letters of J is at most
Λ_a |Ψ_(σB)|, σ the subword of J left and |σB| = |JB| − a, and 𝔶_(|J|)^(1/2) μ² ≤ μ^(|JB|/2) = μ^(a/2) μ^(|σB|/2); as B
↦ σB is injective, Minkowski's inequality over the monomials gives (Σ_B 𝔶_(|J|) μ⁴ |R′_(J,B)|²)^(1/2) ≤ ρ′_(|J|) 𝒥_g
with ρ′_(|J|) as in the proof of [[lem:tl5-hfs-mixed]], and Σ_J ρ′_(|J|)² = ϖ₁. By Minkowski's inequality over the pairs
(J, B), (Σ_(J,B) 𝔶_(|J|) μ⁴ |ℒ^J D̂Ψ_B|²)^(1/2) ≤ (1 + ϖ₁^(1/2)) 𝒥_g, and so μ² X₁ ≤ 𝔛^u_(1,t) 𝔍_g.

*μ² X₂.* By [[eq:tl5-hfu-face]] with r = 4, μ⁴ X₂² ≤ C_(E,4)(𝔶)² 𝔵₄(t) ‖(Σ_(J,Z) 𝔶_(|J|) μ⁴ |ℒ^J D̂²Ψ_Z|²)^(1/2)‖_Σ²,
the sum being over the 43 words J and the Z ∈ Γ. At each point ℒ^J D̂²Ψ_Z = D̂²Ψ_(JZ) + R_(J,Z), as in the proof of
[[lem:tl5-hfs-mixed]]. By [[eq:tl5-hfu-fam]] for 𝔙_Γ the part with the D̂²Ψ_(JZ) is at most 𝔩(𝔙_Γ) 𝒥_g + 301^(1/2) 𝔗(𝔶)
(μ/ν)² k₂^z ϱ/(1 − 𝔵^z), as Σ_(J,Z) 𝔶_(|J|) μ⁴ ν^(−(|J|+2)) = 7 (μ/ν)⁴ (ν²𝔶₀ + 6ν𝔶₁ + 36) = 301 (μ/ν)⁴ 𝔗(𝔶)². A monomial
of R_(J,Z) whose coefficient carries a letters is contracted with Ψ_(σZ) or D̂Ψ_(σZ), |σZ| = |JZ| − a, and 𝔶_(|J|)^(1/2)
μ² ≤ μ^((|JZ|+1)/2) = μ^(1/2) μ^(a/2) μ^(|σZ|/2); with the background norms of that proof and the injectivity of Z ↦ σZ,
(Σ_(J,Z) 𝔶_(|J|) μ⁴ |R_(J,Z)|²)^(1/2) ≤ μ^(1/2) ϖ₂^(1/2) 𝒥_g. Minkowski's inequality over the pairs and in L² of the
face, with e^(−φ) ≤ 1 and Σ ⊂ Σ₁(t, v*) in the part with ϱ, gives μ² X₂ ≤ 𝔛^u_(2,t) 𝔍_g + 𝔛′^u_(2,t) ϱ.

*μ^(3/2) Y₁ and μ^(3/2) Y₂.* By [[eq:tl5-hfu-face]] with r = 3 for A := D̂Ψ_B, summed over the 49 words B of length two,
μ³ Y₁² is at most μ³ [𝔳₀⁶]_t Σ_B ∫_(S_t) |D̂Ψ_B|² dω + 𝔱_(3,0)(t) ‖(μ³ Σ_B |D̂Ψ_B|²)^(1/2)‖_Σ² + 𝔱_(3,1)(t)
‖(μ³ Σ_B |D̂²Ψ_B|²)^(1/2)‖_Σ². On S_t, |D̂Ψ_B| ≤ η₀ and ∫_(S_t) dω = 2π², so the first term is at most (𝔜″^u_(1,t) η₀)²;
as μ³ = μ μ^(|B|), the second norm is at most μ^(1/2) 𝔍_g; and by [[eq:tl5-hfu-fam]] for 𝔙₂, whose sum of the 𝔬_C² w_C²
is 49 (μ/ν)³, the third norm is at most [𝔩(𝔙₂)]_t 𝔍_g + 7 (μ/ν)^(3/2) ς_t ϱ. With (x + y + z)^(1/2) ≤ x^(1/2) +
(y + z)^(1/2) and Minkowski's inequality in the plane this gives μ^(3/2) Y₁ ≤ 𝔜^u_(1,t) 𝔍_g + 𝔜′^u_(1,t) ϱ + 𝔜″^u_(1,t)
η₀. Likewise for A := Ψ_B, summed over the 343 words B of length three, with r = 2, |Ψ_B| ≤ η₀ on S_t and μ³ Σ_B
(|Ψ_B|² + |D̂Ψ_B|²) ≤ 𝒥_g², as 𝔱_(2,0)(t) and 𝔱_(2,1)(t) are at most 𝔱₂(t): μ^(3/2) Y₂ ≤ 𝔜_(2,t) 𝔍_g + 𝔜″^u_(2,t) η₀.

*The comparison.* Let 𝔶₀, 𝔶₁ ≥ 1, so that C_(E,r)(𝔶) ≤ C_(E,r)^♯ by [[lem:tl5-hfp-leaf]]. With the constants with index
p, 𝔭_r/2 is C_(E,r)^♯² in [[lem:tl5-hfq-mixed]] and [[lem:tl5-hfs-mixed]], and λ_t^μ and λ_t^(μ,2) are ([k₁^(3,μ,p)]_t +
2𝔵^z)/(1 − 𝔵^z) and ([k₁^(2,μ,p)]_t + 2𝔵^z)/(1 − 𝔵^z), by [[lem:tl5-hfz-abs]] and [[lem:tl5-hfp-abs]] (b). Then
𝔛^u_(1,t) ≤ 𝔛^q_(1,t), as (1 + x)² ≤ 2(1 + x²). By [[lem:tl5-hfu-fam]], [𝔩(𝔙_Γ)]_t ≤ 301^(1/2) λ_t^μ and [𝔩(𝔙₂)]_t ≤ 7
λ_t^(μ,2); with μ^(1/2) ≤ 2^(1/2) this gives 𝔛^u_(2,t) ≤ 𝔛^q_(2,t), and 𝔜^u_(1,t) ≤ 𝔱₃(t)^(1/2) (μ + [𝔩(𝔙₂)]_t²)^(1/2) ≤
𝔱₃(t)^(1/2) (1 + 7 λ_t^(μ,2)) = 𝔜^q_(1,t). As μ ≤ ν ≤ 1, 𝔶₀ ≤ μ⁻² and 𝔶₁ ≤ μ⁻¹, (μ/ν)⁴ 𝔗(𝔶)² ≤ ((μ/ν)² + 6(μ/ν)³ +
36(μ/ν)⁴)/43 ≤ 1, so 𝔛′^u_(2,t) ≤ 𝔛′_(2,t); and (μ/ν)^(3/2) ≤ 1, 𝔱_(3,1)(t) ≤ 𝔱₃(t) and μ^(3/2) ≤ 1 give the other
three. ∎

**Theorem {#thm:tl5-hfu}** (Level four, with the weights and the families of words in the products with no factor at a
point.) In the setting of [[thm:tl5-hfp]] with N = 4, let S_M^p, 𝔯_M^p and ε_M^p be S_(M,q), 𝔯_(M,q) and ε_(M,q) of
[[eq:tl5-hfq-constants]] formed with the constants with index p, so that S_M^p and ε_M^p are those of [[thm:tl5-hfp]]
and 𝔯_M^p is the part of 𝔯^p with the products with no factor at a point, let S_M^u, 𝔯_M^u and ε_M^u be as in
[[def:tl5-hfu-constants]], 𝔯^u := 𝔯^p − 𝔯_M^p + 𝔯_M^u, and put

    η_u := 1 − max(ϑ₁, ϑ₂) − 𝔯^u,      A_u := η_u^(−1/2) δ_w + η_u⁻¹ (ε^z + ε_M^u),      B_u := η_u⁻¹ (S_F^p + S_M^u),

and let 𝔰_*^u be 𝔰_*^p with A_u in place of A_p. Suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are
admissible for (𝔅₄, E_o⁴, E_i⁴); (c) η_u > 0, 𝔰_*^u < 𝔰₁^v and the closing condition

    4 A_u B_u = 4 η_u^(−3/2) (δ_w + η_u^(−1/2) (ε^z + ε_M^u)) (S_F^p + S_M^u) < 1.                 {#eq:tl5-hfu-closing}

Then the conclusions of [[thm:tl5-hf4]] hold with A_u and 𝔰_*^u in place of A_(w,4) and 𝔰_*. For 𝔶₀, 𝔶₁ ≥ 1, S_M^u ≤
S_M^p, 𝔯_M^u ≤ 𝔯_M^p and ε_M^u ≤ ε_M^p, so η_u ≥ η_p, A_u ≤ A_p, B_u ≤ B_p and 𝔰_*^u ≤ 𝔰_*^p, and the hypotheses of
[[thm:tl5-hfp]] with N = 4 imply these.

*Proof.* The proof of [[thm:tl5-hfp]] applies with N = 4 and with A_u, 𝔰_*^u, 𝔯^u and η_u in place of A_p, 𝔰_*^p, 𝔯^p
and η_p. Step 1 is unchanged and gives 𝔰 ≤ 𝔰_*^u < 𝔰₁^v on D^κ_s. In Step 2 the terms 𝔑^M_I are bounded, as in the proof
of [[prop:tl5-hfq-bootstrap]], by the argument of the proof of [[prop:tl5-hfs-bootstrap]] with [[eq:tl5-hfq-m]] and the
bounds of μ² X₁, μ^(3/2) Y₁, μ² X₂ and μ^(3/2) Y₂ on the faces Σ₁(t, b′). By [[lem:tl5-hfu-mixed]], which applies there
as 𝔰 ≤ 𝔰₁^v on D^κ_s, these bounds hold with the constants of [[def:tl5-hfu-constants]], and expanding with 𝔍_g ≤
[𝔨₂]_t^(1/2) Y_s as there gives S_M^u Y_s³ + 𝔯_M^u Y_s² + ε_M^u Y_s in place of S_M^p Y_s³ + 𝔯_M^p Y_s² + ε_M^p Y_s. No
other step uses S_M^p, 𝔯_M^p or ε_M^p, and the rest is the proof of [[thm:tl5-hfv]] with A_u, B_u and
[[eq:tl5-hfu-closing]]. For the last claim, each constant of [[def:tl5-hfu-constants]] is at most the one it replaces,
by [[lem:tl5-hfu-mixed]], and S_M, 𝔯_M and ε_M are nondecreasing in these constants; so 𝔯^u ≤ 𝔯^p and η_u ≥ η_p, and
A_u, B_u and 𝔰_*^u, which are nonincreasing in η_u and nondecreasing in ε_M^u and S_M^u, are at most A_p, B_p and 𝔰_*^p.
∎

**Remark {#rem:tl5-hfu-what}** (What changes.) The products with no factor at a point are bounded through the Hölder
inequality [[eq:tl5-hf4-holder]], one factor in ⟦·⟧_(2,∞), which the Sobolev inequality on the leaves bounds, and the
other in ⟦·⟧_(∞,2), which the inequality along the curves γ_ω bounds. The first now carries C_(E,r)(𝔶) of
[[sec:tl5-hfp]], at most (2/9)^(1/2) (6C_(E,r)²)^(1/2) for 𝔶₀, 𝔶₁ ≥ 1 and smaller for the weights 𝔶_k ≤ μ^(k−2), which
the energies of the words JB and JZ allow, and the triangle inequality over the words: the factor (2(1 + ϖ₁))^(1/2) of
𝔛_(1,t) becomes 1 + ϖ₁^(1/2). In 𝔛_(2,t) the second derivatives of the 301 words JZ are counted together, so that √602
λ_t^μ becomes 𝔩(𝔙_Γ), in which the leading term of the recovery counts once and 301^(1/2) remains with the nonlinear
part and in the bound of 𝔞_𝔄(𝔙_Γ); and the remainders of ℒ^J D̂²Ψ_Z, whose solution factors Ψ_C and D̂Ψ_C
have |C| = |JZ| − a while the weight (𝔶_(|J|) μ⁴)^(1/2) of the step is at most μ^((|JZ|+1)/2), gain the factor μ^(1/2)
in place of the factor 2 of their square. In 𝔜_(1,t) the second derivatives of the 49 words of length two are counted
together, so that 7 λ_t^(μ,2) becomes 𝔩(𝔙₂), whose leading term counts once and whose nonlinear part carries 7 𝔵^z; the
first derivatives D̂Ψ_B, |B| = 2, have the weight μ² of their own length against the weight μ³ of the step, which gives
μ in place of 1 beside 𝔩(𝔙₂)², and the two coefficients of [[lem:tl5-hf4-face]] (a) are kept apart. The terms with η₀
keep the factor μ^(3/2) of the step, and those with ϱ the weights of [[lem:tl5-hfq-theta]], which give (μ/ν)^(3/2) in
𝔜′^u_(1,t) and (μ/ν)² 𝔗(𝔶) ≤ 1 in 𝔛′^u_(2,t). The coefficients 𝔠^Mq₁ and 𝔠^Mq₂, the factors w_t and [𝔨₂]_t and the
factor 𝔜_(2,t) are unchanged: in 𝔜_(2,t) the words B of length three have the weight μ³ of the step, so neither a count
nor a power is gained there. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfu]] are
established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 89765a14, where sec:tl5-hfp is merged (Section 57.25,
merge b08d91c5). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfu) through the last line of
[[rem:tl5-hfu-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfp-what]] (line 6884,
as changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfp-what]] (lines 6882–6883).* Old:

the words beginning with T from those beginning with a rotation, which 𝒥_g and 𝒟_g do not give. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfp]] are established in this paper for no background at 10 l5.

New (one line added, of 102 characters; the two old lines are unchanged):

the words beginning with T from those beginning with a rotation, which 𝒥_g and 𝒟_g do not give. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfp]] are established in this paper for no background at 10 l5.
[[sec:tl5-hfu]] carries the weights and the families of words into S_M, 𝔯_M and ε_M ([[thm:tl5-hfu]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. Level four only: for N ≥ 6, S_M = 𝔯_M = ε_M = 0 and thm:tl5-hfp stands as it is. At level four
thm:tl5-hfu changes S_M^p, 𝔯_M^p and ε_M^p and nothing else: S_F^p, the part 𝔯_(w,s) of 𝔯^p, ε^z, 𝔰₁^v, the cap
𝔰_(θ,v) and every constant with index p are those of thm:tl5-hfp. "Old" below means the constant of lem:tl5-hfq-mixed
and lem:tl5-hfs-mixed formed with the constants with index p and the intrinsic Sobolev constants, so 𝔭_r/2 = C_(E,r)^♯²,
λ_t^μ = ([k₁^(3,μ,p)]_t + 2𝔵^z)/(1 − 𝔵^z), λ_t^(μ,2) = ([k₁^(2,μ,p)]_t + 2𝔵^z)/(1 − 𝔵^z) and ς_t = [k₂^z]_t (1 −
𝔵^z)⁻¹ (∫_(Σ₁(t,v*)) dμ dτ₂/(1 − κκ′))^(1/2). The weights 𝔶 are those of def:tl5-hfp-constants; for 𝔶₀, 𝔶₁ ≥ 1 every
new factor is at most the old one (lem:tl5-hfu-mixed), so thm:tl5-hfu contains thm:tl5-hfp at N = 4.

1. 𝔛_(1,t) (the factor at a point of P₁, rank 3).
       new  C_(E,3)(𝔶) 𝔵₃(t)^(1/2) (1 + [ϖ₁]_t^(1/2)),      old  (2 C_(E,3)^♯² 𝔵₃(t) (1 + [ϖ₁]_t))^(1/2),
   ϖ₁ = 6(2μ^(1/2)Λ₁)² + 36(4μ^(1/2)Λ₁ + 2μΛ₂)² unchanged. Factor q₃ · (1 + ϖ₁^(1/2))/(2(1 + ϖ₁))^(1/2); the second
   factor lies in [2^(−1/2), 1], equal to 1 at ϖ₁ = 1 and to 2^(−1/2) as ϖ₁ → 0.
2. 𝔜_(1,t) (the other factor of P₁, along the curves).
       new  (μ 𝔱_(3,0)(t) + 𝔱_(3,1)(t) [𝔩(𝔙₂)]_t²)^(1/2),      old  𝔱₃(t)^(1/2) (1 + 7 λ_t^(μ,2)),
       𝔩(𝔙₂) = k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙₂) + 7 𝔵^z (k₁^(2,μ,p) + 2)/(1 − 𝔵^z),
   𝔞_𝔄(𝔙₂) ≤ (49/2)^(1/2) α_𝔄^(2,μ) (the rows are the 49 words of length two with the weight μ^(3/2)); 𝔱_(3,0) and
   𝔱_(3,1) are the sups of 𝔳₀⁶R⁻³(1 + 18|D̂∂_γ|²) and 2𝔳₀⁶R⁻³|∂_γ|² whose larger one is 𝔱₃. Proved: 𝔩(𝔙₂) ≤
   7 (k₁^(2,μ,p) + 2𝔵^z)/(1 − 𝔵^z).
3. 𝔛_(2,t) (the factor at a point of P₂, rank 4).
       new  C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ([𝔩(𝔙_Γ)]_t + μ^(1/2) [ϖ₂]_t^(1/2)),
       old  C_(E,4)^♯ 𝔵₄(t)^(1/2) (√602 λ_t^μ + (2[ϖ₂]_t)^(1/2)),
       𝔩(𝔙_Γ) = k₁^D + μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔙_Γ)
                + √301 𝔵^z (k₁^(3,μ,p) + 2)/(1 − 𝔵^z),
   𝔞_𝔄(𝔙_Γ) ≤ (301/2)^(1/2) α_𝔄^(3,μ). 𝔞_𝔄(𝔙_Γ) is 𝔞_𝔄(Γ) of def:tl5-hfp-constants (the same rows and weights), so
   𝔩(𝔙_Γ) = 𝔩_D(Γ) + 𝔩_J(Γ), the k-term of C₁^Γ that G0m already forms. Proved: 𝔩(𝔙_Γ) ≤ √301 λ^μ.
4. 𝔛′_(2,t) (the part with ϱ of P₂'s factor at a point).
       new  √301 𝔗(𝔶) (μ/ν)² C_(E,4)(𝔶) 𝔵₄(t)^(1/2) ς_t,      old  √602 C_(E,4)^♯ 𝔵₄(t)^(1/2) ς_t,
   𝔗(𝔶)² = (ν²𝔶₀ + 6ν𝔶₁ + 36)/43 (lem:tl5-hfq-theta's). (μ/ν)⁴𝔗² ≤ ((μ/ν)² + 6(μ/ν)³ + 36(μ/ν)⁴)/43 ≤ 1 for every
   admissible 𝔶, with equality at 𝔶 = (μ⁻², μ⁻¹), where (μ/ν)²𝔗 ≈ (μ/ν)/√43 with μ/ν = μ^(1−θ).
5. 𝔜′_(1,t): new 7 (μ/ν)^(3/2) 𝔱_(3,1)(t)^(1/2) ς_t, old 7 𝔱₃(t)^(1/2) ς_t.
6. 𝔜″_(1,t), 𝔜″_(2,t): new μ^(3/2) π (98[𝔳₀⁶]_t)^(1/2) and μ^(3/2) π (686[𝔳₀⁴]_t)^(1/2), old the same without μ^(3/2).
7. Unchanged: 𝔜_(2,t) = 𝔱₂(t)^(1/2), 𝔠^Mq₁ = 480 + 96𝔤₁(𝔤₀ + √5)𝔰_♭, 𝔠^Mq₂ = 4 + 4𝔤₁𝔰_♭(2 + 𝔤₁𝔰_♭), w_t, [𝔨₂]_t,
   𝔪(t) = [max(1, 𝔴₀)⁶R^(3/2)]_t.
8. S_M^u, 𝔯_M^u, ε_M^u are S_(M,q), 𝔯_(M,q), ε_(M,q) of eq:tl5-hfq-constants with items 1–6. The closing condition
   eq:tl5-hfu-closing is eq:tl5-hfp-closing with 𝔯^u = 𝔯^p − 𝔯_M^p + 𝔯_M^u in η, ε_M^u in A and S_M^u in B; 𝔰_*^u is
   𝔰_*^p with A_u.

The weighted leaf ratios q_r := C_(E,r)(𝔶)/C_(E,r)^♯ at 𝔶 = (μ⁻², μ⁻¹), summed to j₁ ≤ 40000 with the tail
extrapolated in 1/j₁ (ranks 2 and 3 agree with G0m's):

       μ        10⁻⁴      3 × 10⁻⁵   10⁻⁵      3 × 10⁻⁶   10⁻⁶
       q₂       0.1097    0.0812     0.0617    0.0456     0.0347
       q₃       0.1216    0.0900     0.0684    0.0506     0.0385
       q₄       0.1310    0.0970     0.0737    0.0545     0.0414

What it gives, deduced, not evaluated. At G0m's level-4 optima (G0m.0: μ = 10⁻⁵, 3 × 10⁻⁵, 10⁻⁶, 10⁻⁵; 𝔵^z = 0.008,
0.017, 0.016, 0.054; θ = 3/4, 11/16, 3/4, 13/16), for seed 1 D_A, seed 2 D_A, seed 1 D*, seed 2 D*. Assumptions:
k₁^D = 2.30; α_𝔄 = 0.06 with the trivial bounds of 𝔞_𝔄; the μ^(1/2) part of k₁ 0.01, 0.32, 0, 0 (G0l's k₁^z, scaled by
μ^(1/2) and by G0m's 𝔷′ ratio at seed 2 D_A); 𝔱_(3,1) = 𝔱₃ (no gain from keeping the coefficients apart); every
supremum at one point.
- 𝔜_(1,t): 1 + 7λ^(μ,2) = 17.8, 20.3, 18.0, 19.3 against 𝔩(𝔙₂) ≈ 2.85, 3.48, 3.09, 4.34: −0.80, −0.77, −0.77, −0.65.
- 𝔛_(1,t): q₃ = 10^(−1.17), 10^(−1.05), 10^(−1.41), 10^(−1.17), and the triangle inequality 0 to −0.15.
- So the term 𝔠^Mq₁ 𝔛_(1,t) 𝔜_(1,t) of S_M falls by about 2.0–2.1, 1.8–2.0, 2.2–2.3, 1.8–2.0 decades.
- 𝔛_(2,t): q₄ and 𝔩(𝔙_Γ) ≈ 3.7, 4.8, 4.3, 7.4 against √602 λ^μ ≈ 59, 68, 60, 64: −2.3, −2.2, −2.5, −2.1, so the term
  with 𝔠^Mq₂ falls at least as far as the term with 𝔠^Mq₁.
- S_M therefore falls by about 1.8–2.3 decades, from 0.22, 0.25, 0.85, 0.48 above S_F (G0m.2) to about 1.3–1.9 below.
- 𝔯_M: its terms with ϱ fall by about q₃ (μ/ν)^(3/2) (−2.6 to −3.6) and q₄ 2^(−1/2) (μ/ν)² 𝔗 (−2.9 to −3.6);
  its terms with η₀ and ε_M by μ^(3/2) more (−7.5, −6.8, −9.0, −7.5 decades).
- min(f, ϱ): every term of S_M^u is at most the corresponding term of G0m's hypothetical lever "S_M with the weighted
  constants as well" (its ℰ_g part × q), and 𝔯_M^u, ε_M^u are at most the unchanged ones of that lever. So the gain is
  at least G0m's computed +0.31, +0.26, +0.34, +0.14, and, as G0m reports that 𝔰_* then binds again or comes within
  0.06, at most about 0.1 more.
- After this, 𝔰_* binds at level four. Its term with A carries C_P^v, led by 𝔨_rec^p, so the C_P^v levers return to
  G0l's 1:1 rate (G0m.3), and lowering S_F alone gains only up to 𝔰_*.

Choices for the evaluation. 𝔶 = (μ⁻², μ⁻¹), as at G0m's optima. [𝔩(𝔙_Γ)]_t is G0m's C₁^Γ k-term taken as a supremum
over Σ₁(t, v*); [𝔩(𝔙₂)]_t is the same formula with n = 49, no words J, and k₁^(2,μ,p); 𝔱_(3,0) and 𝔱_(3,1) come from
the integrand of 𝔱₃ before its maximum. q₃ multiplies 𝔛_(1,t) and q₄ multiplies 𝔛_(2,t) and 𝔛′_(2,t).

Not done.
- Target 2, the word count 7² in S_F and 𝔠^♮₄(μ) → 9·2⁴: not done.
  - It is capped. After this section 𝔰_* binds or comes within about 0.06 (G0m.2–3), and both levers act on S_F alone.
  - The word count would need the products lemma eq:tl5-hfs-products summed over the words of each length before the
    Cauchy–Schwarz inequality of Step 2. In each monomial the letters on the factor in the energies need no count, as
    𝒥_g already sums over all words. The factor at a point would be counted through the family bounds of
    lem:tl5-hfp-abs (c) and eq:tl5-hfp-family. That replaces 7^(j′/2)(𝔠^♮_(j′)(μ) + 1) by a sum over the monomials of
    7^((j′ − k_E)/2) times their norms, k_E the letters on the factor in the energies, which means restating
    eq:tl5-hfs-cn monomial by monomial.
  - 9·2⁴ is G0's comparison count, not a proved one. From eq:tl5-hfs-cn, the terms with b = 0 alone give 𝔠^♮₄(μ) + 1 ≥
    2⁴ (from H₁^(λσ)D̂_λD̂_σh) + 16 λ̂₀² 2⁴ (from 2𝔮̂) = 16 · 81 = 1296 for every μ, against 144. Reaching 9·2⁴ needs a
    bound of the bilinear form 2𝔮̂ of about 8 in place of 16 λ̂₀² = 80, that is the form itself, which the chapter does
    not state.
- 𝔠^Mq₁: the count 6 of the sets S is not lowered. Minkowski's inequality over the six S is an equality when D̂Ψ_B
  vanishes but for one word of two equal letters. The factor 80 = 16 λ̂₀² is, as above, a bound of 2𝔮̂.
- The split with 𝒟_g and 𝔨₂′ in S_M: not done; G0m found the split worth nothing at the supremum in C₁.
- 𝔜_(2,t): no gain is available by these arguments, since the words of length three carry the step's weight μ³ = μ^|B|.
- 𝔪(t): both pairs of [[eq:tl5-hf4-holder]] have r_X + r_Y = 6, so max(1, 𝔴₀)⁶ could be 𝔴₀⁶. That changes nothing
  where 𝔴₀ ≥ 1 (G0g), and is not taken.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfu	paper/reader/proofs/P-GRD11.md@PENDING:1	P-GRD11, section	new; at the end of ch:ten-l5, after rem:tl5-hfp-what; the weights, the leaf constant and the families of words in S_M, r_M and eps_M at level four
    lem:tl5-hfu-face	paper/reader/proofs/P-GRD11.md@PENDING:18	P-GRD11, Lemma	lem:tl5-hf4-face (b) with the weights y and C_(E,r)(y)^2 (intrinsic form), and (a) with the coefficients of |A|^2 and |DA|^2 apart: t_(r,0), t_(r,1)
    eq:tl5-hfu-face	paper/reader/proofs/P-GRD11.md@PENDING:28	P-GRD11, display	new
    lem:tl5-hfu-fam	paper/reader/proofs/P-GRD11.md@PENDING:40	P-GRD11, Lemma	second derivatives over a weighted family of n distinct words: leading term once, couplings through a_A(V), nonlinear part with n^(1/2); l(V) <= n^(1/2)(k1 + 2x)/(1 - x)
    eq:tl5-hfu-fam	paper/reader/proofs/P-GRD11.md@PENDING:55	P-GRD11, display	new
    def:tl5-hfu-constants	paper/reader/proofs/P-GRD11.md@PENDING:78	P-GRD11, Definition	constants with index u: families V_2 (49 words of length two) and V_Gamma (301 words JZ); X^u_(1,t), X^u_(2,t), X'^u_(2,t), Y^u_(1,t), Y'^u_(1,t), Y''^u_(1,t), Y''^u_(2,t); S_M^u, r_M^u, eps_M^u
    eq:tl5-hfu-constants	paper/reader/proofs/P-GRD11.md@PENDING:98	P-GRD11, display	new
    lem:tl5-hfu-mixed	paper/reader/proofs/P-GRD11.md@PENDING:100	P-GRD11, Lemma	eq:tl5-hfs-mixed with the constants with index u; each at most the old one for y0, y1 >= 1
    thm:tl5-hfu	paper/reader/proofs/P-GRD11.md@PENDING:146	P-GRD11, Theorem	thm:tl5-hfp at N = 4 with S_M^u, r_M^u, eps_M^u; contains it for y0, y1 >= 1
    eq:tl5-hfu-closing	paper/reader/proofs/P-GRD11.md@PENDING:157	P-GRD11, display	closing condition: 4 eta_u^(-3/2)(delta_w + eta_u^(-1/2)(eps^z + eps_M^u))(S_F^p + S_M^u) < 1
    rem:tl5-hfu-what	paper/reader/proofs/P-GRD11.md@PENDING:175	P-GRD11, Remark	what changes
