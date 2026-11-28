### The leaf constant, the weights of the words and the seven fields {#sec:tl5-hfp}

This section sharpens the constants of [[sec:tl5-hfz]] in five ways, with the intrinsic Sobolev constants of
[[lem:tl5-hft-face]]. First, the sum over the 43 words in [[eq:tl5-hft-leaf]] is diagonal on the representations of
SO(4), so that inequality holds with its own constant C_(E,r)^♯ ≤ (2/9)^(1/2) (6C_(E,r)²)^(1/2), and also with weights
𝔶₀, 𝔶₁ on the words of lengths zero and one ([[lem:tl5-hfp-leaf]]). Second, in the bounds of Ψ_B(p) and of D̂Ψ_B(p) the
words J of length k ≤ 2 carry weights 𝔶_k ≤ μ^(k−2), which their energies allow, in place of the weight of the longest
words. Third, the first-order bound is proved for a family of words B of one length at once, which counts the seven
fields of the bound of D̂²h at level four together, and at the levels N ≥ 6 the words of each length in the second
derivatives at low levels ([[lem:tl5-hfp-words]], [[lem:tl5-hfp-c1]], [[lem:tl5-hfp-rec]], [[lem:tl5-hfp-low]]). Fourth,
the leading term of the recovery is bounded through the energy of the first derivatives alone, whose density carries 𝔨₂
without its part 1/(2Ω̂²z̲). Fifth, the fields enter the terms 𝔷_Z through (Σ_Z |D̂Z|²)^(1/2) and (Σ_Z |D̂²Z|²)^(1/2).
The closing condition is [[eq:tl5-hfp-closing]]; with 𝔶₀ = 𝔶₁ = 1 every new constant is at most the one it replaces, and
the earlier closing conditions remain valid. The notation is that of [[sec:tl5-hfz]].

**Lemma {#lem:tl5-hfp-leaf}** (The Sobolev inequality on the leaves, with its own constant and with weights.) In the
setting of [[lem:tl5-hft-leaf]] let 𝔶₀, 𝔶₁ > 0, put 𝔶₂ := 1, c_(j₁j₂) := 2j₁(j₁ + 1) + 2j₂(j₂ + 1) and

    C_(E,r)(𝔶)² := (1/(2π²)) Σ_(j₁,j₂) (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r) / (𝔶₀ + 𝔶₁ c_(j₁j₂) + c_(j₁j₂)²).

Then for every C² covariant tensor field A of rank r on S_(u,v) and every ω ∈ S³, with the sum over the words J of
length at most two in the six rotations,

    |A(ω)|₀² ≤ C_(E,r)(𝔶)² Σ_(|J|≤2) 𝔶_(|J|) ∫_(S³) |ℒ^J A|₀² dω.                                     {#eq:tl5-hfp-leaf}

C_(E,r)(𝔶) is nonincreasing in 𝔶₀ and in 𝔶₁, and C_(E,r)^♯ := C_(E,r)(1, 1) satisfies C_(E,r)^♯² ≤ (4/3) C_(E,r)² =
(2/9) · 6C_(E,r)². For r = 0, [[eq:tl5-hf-sphere]] holds with C_(E,0)^♯² in place of 6C_(S³)² = 1/2.

*Proof.* In the proof of [[lem:tl5-hft-leaf]], the orthogonal projection of L²(S³, E) onto V_π commutes with the action
of SO(4), hence with each ℒ_(K_ab), and Ω = c_π on V_π. As ℒ_(K_ab) is skew-adjoint, Σ_(a<b) ‖ℒ_(K_ab) B‖² = ⟨ΩB, B⟩ for
B ∈ V_π; with B = A_π and with B = ℒ_(K_cd) A_π ∈ V_π this gives Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A_π‖² = (𝔶₀ + 𝔶₁ c_π + c_π²)
‖A_π‖², the 36 words of length two being the ordered pairs of rotations. Summed over π, as the V_π are orthogonal, the
left side is Σ_(|J|≤2) 𝔶_(|J|) ‖ℒ^J A‖². With |A_π(ω)|₀² ≤ (dim V_π/(2π²)) ‖A_π‖² as there, the Cauchy–Schwarz
inequality over π gives

    |A(ω)|₀ ≤ Σ_π |A_π(ω)|₀ ≤ C_(E,r)(𝔶) (Σ_π (𝔶₀ + 𝔶₁ c_π + c_π²) ‖A_π‖²)^(1/2),

which is [[eq:tl5-hfp-leaf]]. The series converges, as 𝔶₀ + 𝔶₁ c + c² ≥ min(𝔶₀, 𝔶₁, 1)(1 + c)²/2 bounds its terms by
2/min(𝔶₀, 𝔶₁, 1) times those of C_(E,r)²; and its terms do not increase with 𝔶₀ and 𝔶₁. Since (4/3)(1 + c + c²) − (1 +
c)² = (1 − c)²/3 ≥ 0, C_(E,r)^♯² ≤ (4/3) C_(E,r)². For r = 0, E is the trivial bundle, |·|₀ is the absolute value and
ℒ_K f = K f, so with 𝔶₀ = 𝔶₁ = 1 the right side of [[eq:tl5-hfp-leaf]] is C_(E,0)^♯² times the integral of
[[eq:tl5-hf-sphere]]. ∎

**Definition {#def:tl5-hfp-constants}** (The constants with index p.) In the setting of [[def:tl5-hfz-constants]], with
the intrinsic Sobolev constants, fix 𝔶₀ ∈ (0, μ⁻²] and 𝔶₁ ∈ (0, μ⁻¹], put 𝔶₂ := 1, let C_(E,r)(𝔶) and C_(E,r)^♯ be as in
[[lem:tl5-hfp-leaf]], and put, for 0 ≤ j ≤ N − 1 and ν′ ∈ (0, 1],

    𝔷₁′ := 3 (Σ_(Z∈Γ) |D̂Z|²)^(1/2),   𝔷₂′ := 2 (Σ_(Z∈Γ) |D̂²Z|²)^(1/2),   𝔷′ := (𝔷₁′² + 𝔷₂′²)^(1/2),
    k₁^(j,ν′,p) := 𝔨_♯ K_rec (1 + ν′^(1/2) 𝔷′) + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),   k₁^p := k₁^(N−1,μ,p),
    k₁^D := 𝔨_♯ K_rec,   𝔨₂′ := max(1/c, 1/κ′)/(2Ω̂²),   𝒟_g := (Σ_(|C|≤N) μ^|C| |D̂Ψ_C|²)^(1/2).

For a family 𝔚 of n distinct words of one length b ≤ N − 3 let 𝔞_𝔄(𝔚) be, at each point, the operator norm of the map

    (ξ_K)_(|K|≤b+2) ↦ (Σ_K (𝔶_(|J|) μ^(b+3−|K|))^(1/2) 𝔄_(JB,K) ξ_K)_((J,B)),

the pairs (J, B) running over the words J of rotations with |J| ≤ 2 and the B ∈ 𝔚, 𝔄_(JB,K) := 0 for |K| > |JB|, normed
as in [[def:tl5-hfz-constants]], and put

    𝔩_D(𝔚) := k₁^D (1 + (43n)^(1/2) 𝔵^z/(1 − 𝔵^z)),
    𝔩_J(𝔚) := μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔚) + (43n)^(1/2) 𝔵^z (k₁^p − k₁^D + 2)/(1 − 𝔵^z),
    C₁^U(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(μ^(1/2) + ϖ′^(1/2))²
                + 2|∂_γ|² (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁^D(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂′ (μ (1 + 18|D̂∂_γ|²) + 2|∂_γ|² 𝔩_D(𝔚)²),
    C₁^J(𝔚)² := C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup_(Σ₁(a,b)) 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²) ϖ′ + 2|∂_γ|² (𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
    C₁(𝔚) := min(C₁^U(𝔚), C₁^D(𝔚) + C₁^J(𝔚)),                                                           {#eq:tl5-hfp-c1}

with ϖ′ as in [[lem:tl5-hfx-c1]]. Let C₁^p be the largest of the C₁({B}), |B| ≤ N − 3, and for N = 4 put C₁^Γ := C₁(Γ),
the seven fields being words of length one. Put 𝔗(𝔶)² := (𝔶₀ + 6𝔶₁ + 36)/43 for the steps of [[lem:tl5-hfs-linfty]] and
[[lem:tl5-hft-small]] (a), 𝔗(𝔶)² := (μ²𝔶₀ + 6μ𝔶₁ + 36)/43 for those of [[lem:tl5-hft-small]] (b) and 𝔗(𝔶)² := (ν²𝔶₀ +
6ν𝔶₁ + 36)/43 for those of [[lem:tl5-hfq-theta]]. Let C_S^p be C_S^E of [[eq:tl5-hft-cs]] with C_(E,2)(𝔶)² in place of
6C_(E,2)², and C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p the constants C_(1,ϱ)^z, C_(1,0) and C_(0,0) of the lemma in use
formed with C_(E,r)(𝔶)² 𝔗(𝔶)² in place of 6C_(E,r)² (r = 3, 3 and 2). For 0 ≤ m ≤ N − 4 put 𝔐_p^(m) := (Σ_(b≤m+1)
(C_S^p² + C₁(𝔚_b)²))^(1/2), 𝔚_b being the family of the 7^b words of length b, and for N = 4 put

    𝔨_rec^p := 𝔨_♯ K_rec (C₁^Γ + 𝔷₁′ μ^(1/2) C₁^p + 𝔷₂′ μ C_S^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^p,
    𝔨_rec^(ϱ,p) := 𝔨_♯ K_rec (√7 + 𝔷₁′ μ^(1/2)) C_(1,ϱ)^p,
    𝔨_rec^(0,p) := 𝔨_♯ K_rec ((√7 + 𝔷₁′ μ^(1/2)) C_(1,0)^p + 𝔷₂′ μ C_(0,0)^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_(0,0)^p.

The constants with index p are the constants with index z of [[thm:tl5-hfz]] formed with k₁^(j,·,p), C₁^p, C_S^p,
C_(1,ϱ)^p, C_(1,0)^p, C_(0,0)^p and the 𝔨_rec^(·,p) in place of k₁^(j,·,z), C₁^z, C_S^E, C_(1,ϱ)^z, C_(1,0), C_(0,0) and
the 𝔨_rec^(·,z), with 𝔐_p^(m) in place of (2𝔐^(m))^(1/2) max(C_S, C₁) in C_(∞,μ)^(m) and its forms, and with C_(E,r)^♯²
in place of 6C_(E,r)² in every other constant formed with a Sobolev inequality on a face.

**Lemma {#lem:tl5-hfp-abs}** (The bounds with index p.) (a) [[lem:tl5-hft-face]] holds with C_(E,r)^♯² in place of
6C_(E,r)², and its parts (a) and (b) hold also with every sum over the words J weighted by 𝔶_(|J|) and with C_(E,r)(𝔶)²
in place of 6C_(E,r)², for all 𝔶₀, 𝔶₁ > 0.

(b) In the setting of [[lem:tl5-hfz-abs]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), the lemmas named there hold with k₁^(j,·,p) in
place of k₁^(j,·,z); and the bounds [[eq:tl5-hfs-m2]], [[eq:tl5-hfq-m2]] and those of M_g^(j), in the lemmas that state
them, hold with k₁^D 𝒟_g + (k₁^(j,μ,p) − k₁^D + 2𝔵^z) 𝒥_g in place of (k₁^(j,μ,z) + 2𝔵^z) 𝒥_g.

(c) In that setting, the zeroth-order step of the lemma in use gives its bound of Ψ_B(p), |B| ≤ N − 2, with C_S^p and
C_(0,0)^p in place of C_S^E and C_(0,0); and for a family 𝔚 of n distinct words of one length b ≤ N − 2 it gives the
same bound of (Σ_(B∈𝔚) |Ψ_B(p)|²)^(1/2), with n^(1/2) times its part with η₀.

Moreover k₁^(j,ν′,p) ≤ k₁^(j,ν′,z), and for 𝔶₀ = 𝔶₁ = 1, 𝔗(𝔶) ≤ 1, C_S^p ≤ C_S^E and C_(0,0)^p ≤ C_(0,0).

*Proof.* (a) The proof of [[lem:tl5-hft-face]] uses [[eq:tl5-hft-leaf]] only through its form, applied on the leaves
through γ_ω(v) to A and to ℒ_(∂_γ)A; [[lem:tl5-hfp-leaf]] gives that form with C_(E,r)^♯² in place of 6C_(E,r)², and
with the weights 𝔶_(|J|) and C_(E,r)(𝔶)². The weights pass through the proofs of (a) and (b) there, since (d/dv)|ℒ^J
A|₀² ≤ |ℒ^J A|₀² + |ℒ_(∂_γ) ℒ^J A|₀² holds for each J and is multiplied by 𝔶_(|J|) > 0 before the sum over J, and every
later step bounds the terms of each J separately.

(b) By Minkowski's inequality over Z and the Cauchy–Schwarz inequality, (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷₁′ |D̂Ψ| + 𝔷₂′ |Ψ| ≤ 𝔷′
(|D̂Ψ|² + |Ψ|²)^(1/2), and 𝔷′ ≤ 𝔷₁′ + 𝔷₂′ ≤ √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|); in the proofs of these lemmas the jets
of the terms 𝔷_Z are bounded through (|D̂Ψ_C|² + |Ψ_C|²)^(1/2), so k₁^(j,·,p) may replace k₁^(j,·,z). In the bound of
the second derivatives the leading term of [[eq:tl5-hfz-rec]] for Ψ_C is 𝔨_♯ K_rec (Σ_Z |D̂Ψ_(ZC)|²)^(1/2) ≤ k₁^D
μ^(−(|C|+1)/2) 𝒟_g, the words ZC having length |C| + 1. As 𝒟_g ≤ 𝒥_g, the inductions of the proofs of
[[lem:tl5-hfy-abs]] and [[lem:tl5-hfz-abs]] then close with the stated coefficients: with X_𝒟 ≤ X the weighted 𝒟_g and
𝒥_g of a word and ϱ′ its part with ϱ, R := (k₁^D X_𝒟 + (k₁ − k₁^D + 2𝔵^z) X + k₂^z ϱ′)/(1 − 𝔵^z) satisfies k₁^D X_𝒟 +
(k₁ − k₁^D) X + k₂^z ϱ′ + 𝔵^z (2X + R) = R.

(c) The step applies [[lem:tl5-hf-sobolev]], in the form of [[lem:tl5-hft-face]] (b), to A := Ψ_B; by (a) it holds with
the weights 𝔶_(|J|) and C_(E,2)(𝔶)². As ℒ^J Ψ_B = Ψ_(JB), the words JB are distinct and 𝔶_(|J|) μ^(|B|+2) ≤ μ^(|JB|),
the face term is at most μ^(−(|B|+2)) C_S^p² ℰ_g(p). On S_a, |Ψ_(JB)| ≤ η₀(p) for every J, and for |J| = k this bound,
divided by the weight of the step, is at most 𝔢_k times the one the step uses for every J, with 𝔢_k := 1 in
[[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a); 𝔢_k := μ^((2−k)/2) in [[lem:tl5-hft-small]] (b), where the step
multiplies by μ^((|B|+2)/2) and uses μ^((|B|+2)/2) η₀(p) ≤ η₀(p), while η₀(p) ≤ μ^((2−k)/2) μ^(−(|B|+2)/2) η₀(p); and
𝔢_k := ν^((2−k)/2) in [[lem:tl5-hfq-theta]], where the step uses r_Φ η₀(p) with r_Φ = ν^(−(|B|+2)/2), while η₀(p) ≤
ν^((2−k)/2) r_Φ η₀(p). As 𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36 = 43 𝔗(𝔶)², the sum over J of the squares, with the weights 𝔶_(|J|), is at
most 43 𝔗(𝔶)² times the square of that bound, which gives C_(0,0)^p. For a family, sum the inequality over B ∈ 𝔚: the
words JB are distinct for distinct pairs (J, B), as the B have one length, so the face terms still add up to at most
μ^(−(b+2)) C_S^p² ℰ_g(p), and the terms on S_a to n times those of one word.

Finally (b) gives k₁^(j,ν′,p) ≤ k₁^(j,ν′,z); for 𝔶₀ = 𝔶₁ = 1, 𝔗(𝔶)² ≤ 1 as μ, ν ≤ 1, C_(E,2)(𝔶) = C_(E,2)^♯ and
C_(E,2)^♯² ≤ 6C_(E,2)² by [[lem:tl5-hfp-leaf]]. ∎

**Lemma {#lem:tl5-hfp-words}** (The second derivatives over a family of words, with weights.) In the setting of
[[lem:tl5-hfz-abs]] and [[def:tl5-hfp-constants]], with 𝔰 ≤ 𝔰₁^v on Q(a, b), let 𝔚 be a family of n distinct words of
one length b ≤ N − 3, and let P_ϱ be as in [[lem:tl5-hfz-words]] (b). Then at the points of Σ₁(a, b), the sum being over
the words J of rotations with |J| ≤ 2 and the B ∈ 𝔚,

    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂²Ψ_(JB)|²)^(1/2)
        ≤ 𝔩_D(𝔚) 𝒟_g + 𝔩_J(𝔚) 𝒥_g + (43n)^(1/2) 𝔗(𝔶) μ^((b+3)/2) P_ϱ.                                {#eq:tl5-hfp-words}

Moreover 𝔞_𝔄(𝔚) ≤ (43n/2)^(1/2) α_𝔄^(N−1,μ) and 𝔞_𝔄(𝔚) ≤ (Σ_(B∈𝔚) 𝔞_𝔄({B})²)^(1/2).

*Proof.* By [[lem:tl5-hfp-abs]] (b) and the proof of [[lem:tl5-hfz-words]] (b), the step bounds |D̂²Ψ_C| at the points
of the face, for every word C with |C| = b + k ≤ b + 2, by μ^(−(|C|+1)/2) (k₁^D 𝒟_g + (k₁^p − k₁^D + 2𝔵^z) 𝒥_g)/(1 −
𝔵^z) + P_C, with P_C := 𝔢_k P_ϱ ≥ k₂^z ϱ(p)/(1 − 𝔵^z), where 𝔢_k is as in the proof of [[lem:tl5-hfp-abs]] (c): the
bound of the part with ϱ is uniform in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a), and carries
μ^(−(|C|+1)/2) = μ^((2−k)/2) μ^(−(b+3)/2) in [[lem:tl5-hft-small]] (b) and ν^(−(|C|+1)/2) in [[lem:tl5-hfq-theta]]. So
𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36 = 43 𝔗(𝔶)², the numbers of the words J of lengths 0, 1 and 2 being 1, 6 and 36. Let q be a point of
Σ₁(a, b), (J, B) a pair and C := JB, and put 𝔬_J := (𝔶_(|J|) μ^(b+3))^(1/2), so that 𝔬_J ≤ μ^((|C|+1)/2), as 𝔶_k ≤
μ^(k−2). Apply [[lem:tl5-hfz-rec]] with 𝔥 = 𝔰₁^v to Ψ_C at q, as there, with (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷′
(|D̂Ψ_C|² + |Ψ_C|²)^(1/2); multiply by 𝔬_J, take the Euclidean norm over the 43n pairs and apply Minkowski's inequality
to each kind of term. The words ZJB are distinct for distinct (Z, J, B), as the B have one length, and 𝔬_J² ≤ μ^(|ZJB|);
so the leading term contributes at most k₁^D 𝒟_g. The words JB are distinct and 𝔬_J² ≤ μ μ^(|JB|), so the terms with 𝔷_Z
and with 𝔯_♯ |Ψ_C| contribute at most μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) 𝒥_g, and the terms with 𝔄 at most (1 −
𝔰₁^v)⁻¹ 𝔞_𝔄(𝔚) 𝒥_g, by the definition of 𝔞_𝔄(𝔚) and Σ_K μ^|K| (|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g². For each pair, (1 −
𝔰₁^v)⁻¹ |Σ_K 𝔔_CK ℒ^K(2R̂ic)| ≤ k₂^z ϱ(p) ≤ (1 − 𝔵^z) P_C, and, as in the proof of the bound of |D̂²Ψ_C|, (1 −
𝔰₁^v)⁻¹ |𝔑′_C| ≤ 𝔵^z (2μ^(−(|C|+1)/2) 𝒥_g + 𝔐), where 𝔐 is the bound above for the words of length |C|, which bounds the
second derivatives of the words of length at most |C|. So 𝔬_J times these two terms is at most 𝔵^z (k₁^D 𝒟_g + (k₁^p −
k₁^D + 2) 𝒥_g)/(1 − 𝔵^z) + 𝔬_J P_C. The Euclidean norm over the pairs of the first part is (43n)^(1/2) times it, and
that of the second is (n (𝔶₀𝔢₀² + 6𝔶₁𝔢₁² + 36) μ^(b+3))^(1/2) P_ϱ. Adding the parts gives [[eq:tl5-hfp-words]]. The row
of (J, B) of the map defining 𝔞_𝔄(𝔚) has the sum Σ_K (𝔶_(|J|) μ^(b+3−|K|))^(1/2) ‖𝔄_(JB,K)‖ ≤ Σ_K μ^((|JB|+1−|K|)/2)
‖𝔄_(JB,K)‖ ≤ 2^(−1/2) α_𝔄^(N−1,μ), and the argument of [[lem:tl5-hfz-words]] (a) with 43n rows gives the first bound;
the map is the family over B ∈ 𝔚 of the maps for {B}, which gives the second. ∎

**Lemma {#lem:tl5-hfp-c1}** (The first-order bound over a family of words.) In the setting of [[lem:tl5-hfp-words]], at
p

    (Σ_(B∈𝔚) |D̂Ψ_B(p)|²)^(1/2)
        ≤ μ^(−(b+3)/2) C₁(𝔚) ℰ_g(p)^(1/2) + n^(1/2) (w C_(1,ϱ)^p ϱ(p) + E₀),                        {#eq:tl5-hfp-family}

w being the weight of P_ϱ in [[lem:tl5-hfz-words]] (b) and E₀ the part with η₀ of the bound of |D̂Ψ_B(p)| that the
first-order step of the lemma in use gives, divided by its weight where the step bounds a weighted quantity, formed with
C_(E,3)(𝔶)² 𝔗(𝔶)² in place of 6C_(E,3)². In particular that step gives its bound of D̂Ψ_B(p), |B| ≤ N − 3, with C₁^p,
C_(1,ϱ)^p and C_(1,0)^p in place of C₁^z, C_(1,ϱ)^z and C_(1,0). Moreover C₁(𝔚) ≤ C₁^U(𝔚) ≤ n^(1/2) max_(B∈𝔚) C₁^U({B}),
and for 𝔶₀ = 𝔶₁ = 1, C₁^U({B}) ≤ C₁^z.

*Proof.* For B ∈ 𝔚 let A_B := D̂Ψ_B. By [[lem:tl5-hfp-abs]] (a), [[eq:tl5-hf-cs-r]] with r = 3, in its intrinsic form,
holds with the weights 𝔶_(|J|) and C_(E,3)(𝔶)². Sum it over B ∈ 𝔚 and multiply by μ^(b+3). Let ∫ denote the integral
over Σ₁(a, b) with dμ dτ₂/(1 − κκ′), f := 𝔳₀⁶ R⁻³ (1 + 18|D̂∂_γ|²) and W := 2|∂_γ|² 𝔳₀⁶ R⁻³. At the points of the face
ℒ^J A_B = D̂Ψ_(JB) + R′_(J,B), as in the proof of [[lem:tl5-hfx-c1]]. The words JB are distinct and 𝔶_(|J|) μ^(b+3) ≤ μ
μ^(|JB|), so (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂Ψ_(JB)|²)^(1/2) ≤ μ^(1/2) 𝒟_g. Each monomial of R′_(J,B) is a coefficient
carrying a ≥ 1 letters of J, of norm at most Λ_a, contracted with Ψ_(σB), σ the subword of J left; B ↦ σB is injective,
and 𝔶_(|J|) μ^(b+3) ≤ μ^(1+a) μ^(|σB|) for |J| ≥ 1; so Minkowski's inequality over the monomials and over the words
gives (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |R′_(J,B)|²)^(1/2) ≤ ϖ′^(1/2) 𝒥_g, as in the proof of [[lem:tl5-hfq-mixed]], and likewise
(2ϖ′)^(1/2) 𝒥_g for the D̂R′_(J,B). With [[eq:tl5-hfp-words]], at each point of the face

    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |ℒ^J A_B|²)^(1/2) ≤ μ^(1/2) 𝒟_g + ϖ′^(1/2) 𝒥_g,
    (Σ_(J,B) 𝔶_(|J|) μ^(b+3) |D̂ℒ^J A_B|²)^(1/2) ≤ 𝔩_D(𝔚) 𝒟_g + (𝔩_J(𝔚) + (2ϖ′)^(1/2)) 𝒥_g + y,

with y := (43n)^(1/2) 𝔗(𝔶) μ^((b+3)/2) P_ϱ. Put F_D² := ∫ f μ 𝒟_g², F_J² := ∫ f ϖ′ 𝒥_g², P_D² := ∫ W 𝔩_D(𝔚)² 𝒟_g², P_J²
:= ∫ W (𝔩_J(𝔚) + (2ϖ′)^(1/2))² 𝒥_g², V² := ∫ W y² and S the sum over B of the terms on S_a, times μ^(b+3). By
Minkowski's inequality in L² of the face and then in ℝ³, the square root of the right side is at most

    C_(E,3)(𝔶) 𝔴₀(p)³ ((F_D² + P_D²)^(1/2) + (F_J² + P_J²)^(1/2) + V + S^(1/2)),

and, as 𝒟_g ≤ 𝒥_g, also at most C_(E,3)(𝔶) 𝔴₀(p)³ ((F² + P²)^(1/2) + V + S^(1/2)), where F² := ∫ f (μ^(1/2) + ϖ′^(1/2))²
𝒥_g² and P² := ∫ W (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))² 𝒥_g². By [[eq:tl5-hf-coercive]], on the face |D̂Ψ_C|² ≤ 𝔨₂′
(e_o[Ψ_C] + κ′ e_i[Ψ_C]), and |Ψ_C|² + |D̂Ψ_C|² ≤ 𝔨₂ (e_o[Ψ_C] + κ′ e_i[Ψ_C]) as in the proof of [[lem:tl5-hf-linfty]];
so ∫ g 𝒟_g² ≤ sup (g 𝔨₂′) ℰ_g(p) and ∫ g 𝒥_g² ≤ sup (g 𝔨₂) ℰ_g(p) for every function g ≥ 0, and C_(E,3)(𝔶)² 𝔴₀(p)⁶ times
F_D² + P_D², F_J² + P_J² and F² + P² is at most C₁^D(𝔚)², C₁^J(𝔚)² and C₁^U(𝔚)² times ℰ_g(p). As P_ϱ = w k₂^z ϱ(p)/(1 −
𝔵^z), C_(E,3)(𝔶)² 𝔴₀(p)⁶ V² ≤ n μ^(b+3) w² C_(1,ϱ)^p² ϱ(p)². On S_a, for |J| = k, the bound of ℒ^J A_B that the step
uses for every J, divided by its weight, may be replaced by 𝔢_k times it, 𝔢_k as in the proof of [[lem:tl5-hfp-abs]]
(c): in [[lem:tl5-hft-small]] (b) the weight is μ^((b+3)/2) = μ^((2−k)/2) μ^((|JB|+1)/2), and μ^((|JB|+1)/2) |D̂Ψ_(JB)|
≤ η₀(p) and μ^((|JB|+1)/2) Λ_a ≤ μ^((1+a)/2) Λ_a for the coefficients of R′_(J,B), as |JB| ≥ a; in [[lem:tl5-hfq-theta]]
likewise with ν and the factor ν^(−(b+3)/2) of the step. So the terms on S_a, with the weights 𝔶_(|J|), give n^(1/2)
μ^((b+3)/2) E₀, and dividing by μ^((b+3)/2) gives [[eq:tl5-hfp-family]]. For n = 1 the bound of the step follows, with
C₁({B}) ≤ C₁^p.

For the last claims, (43n)^(1/2) = n^(1/2) 43^(1/2) gives 𝔩_D(𝔚) ≤ n^(1/2) 𝔩_D({B}), and [[lem:tl5-hfp-words]] gives
𝔞_𝔄(𝔚) ≤ n^(1/2) max_B 𝔞_𝔄({B}), so 𝔩_J(𝔚) ≤ n^(1/2) max_B 𝔩_J({B}); as 𝔩_D({B}) does not depend on B, the integrand of
C₁^U(𝔚)² is at most n times the largest of those of the C₁^U({B})², and the supremum over the face of that largest one
is the largest of the suprema. For 𝔶₀ = 𝔶₁ = 1, C_(E,3)(𝔶) = C_(E,3)^♯ and C_(E,3)^♯² ≤ 6C_(E,3)², μ^(1/2) ≤ 1, and
𝔩_D({B}) + 𝔩_J({B}) is 𝔩 of [[eq:tl5-hfz-c1]] with 𝔷′, k₁^p and 𝔞_𝔄({B}) ≤ 𝔞_𝔄 in place of √7 (3 max_Z |D̂Z| + 2
max_Z |D̂²Z|), k₁^z and 𝔞_𝔄, each at most the one it replaces by [[lem:tl5-hfp-abs]] (b); so C₁^U({B}) ≤ C₁^z. ∎

**Lemma {#lem:tl5-hfp-rec}** (The recovery of D̂²h with the seven fields together.) Let N = 4 and, in the setting of
[[lem:tl5-hfz-abs]], 𝔰 ≤ 𝔰₁^v on Q(a, b). Then [[lem:tl5-hfv-rec]], with the constants with index z, holds with 𝔨_rec^p,
𝔨_rec^(ϱ,p) and 𝔨_rec^(0,p) in place of 𝔨_rec^z, 𝔨_rec^(ϱ,z) and 𝔨_rec^(0,z), and with C_S^p, C₁^p, C_(1,ϱ)^p, C_(1,0)^p
and C_(0,0)^p in place of C_S^E, C₁^z, C_(1,ϱ)^z, C_(1,0) and C_(0,0) in C_P^v, C_(P,ϱ)^v and C_(P,0)^v.

*Proof.* In the proof of [[lem:tl5-hfv-rec]], use [[lem:tl5-hfz-rec]] for h at p with 𝔥 = 𝔰₁^v, and bound (Σ_Z
𝔷_Z²)^(1/2) by 𝔷₁′ |D̂h| + 𝔷₂′ |h|, by Minkowski's inequality over Z. Bound μ² (Σ_Z |D̂Ψ_Z|²)^(1/2) by
[[eq:tl5-hfp-family]] with 𝔚 = Γ, b = 1 and n = 7, that is by C₁^Γ ℰ_g^(1/2) + √7 (C_(1,ϱ)^p ϱ(p) + C_(1,0)^p η₀(p))
with the weights of the step, in place of √7 times the bound of one field; bound μ^(3/2) |D̂h| by [[lem:tl5-hfp-c1]]
with B = ∅ and μ |h| by [[lem:tl5-hfp-abs]] (c). The rest is the proof of [[lem:tl5-hfv-rec]]. ∎

**Lemma {#lem:tl5-hfp-low}** (The second derivatives at low levels, with the words of each length together.) In the
setting of [[lem:tl5-hfp-abs]] (c), let 0 ≤ m ≤ N − 4. Then the step on second derivatives at low levels of the lemma in
use holds with 𝔐_p^(m) in place of (2𝔐^(m))^(1/2) max(C_S, C₁) in its part with ℰ_g, its parts with ϱ and η₀ being
formed with C_(1,ϱ)^p, C_(1,0)^p and C_(0,0)^p; and for 𝔶₀ = 𝔶₁ = 1, 𝔐_p^(m) ≤ (2𝔐^(m))^(1/2) max(C_S^E, C₁^z).

*Proof.* In that step, L_g² is the sum over b ≤ m + 1 of Σ_(|C|=b) (μ^(b+2) |Ψ_C|² + μ^(b+3) |D̂Ψ_C|²), with the weights
of the step, and there are 7^b words of length b. By [[lem:tl5-hfp-abs]] (c) and [[eq:tl5-hfp-family]] with 𝔚 = 𝔚_b and
n = 7^b, the two sums over |C| = b are at most the squares of C_S^p ℰ_g(p)^(1/2) + 7^(b/2) e_b and of C₁(𝔚_b)
ℰ_g(p)^(1/2) + 7^(b/2) e′_b, where e_b and e′_b are the parts with ϱ and η₀ of the bounds of one word. Minkowski's
inequality in the Euclidean norm over b and the two kinds gives L_g ≤ 𝔐_p^(m) ℰ_g(p)^(1/2) + (Σ_b 7^b (e_b² +
e′_b²))^(1/2), and Σ_(b≤m+1) 2 · 7^b = 2𝔐^(m), so the second term is at most (2𝔐^(m))^(1/2) times the largest of these
parts, as there. For 𝔶₀ = 𝔶₁ = 1, C₁(𝔚_b) ≤ 7^(b/2) C₁^z by [[lem:tl5-hfp-c1]], and C_S^p ≤ C_S^E; so 𝔐_p^(m)² ≤ Σ_b 7^b
(C_S^E² + C₁^z²) ≤ 2𝔐^(m) max(C_S^E, C₁^z)². ∎

**Theorem {#thm:tl5-hfp}** (Existence with the leaf constant, the weights of the words and the seven fields.) In the
setting of [[thm:tl5-hfz]], with the intrinsic Sobolev constants of [[lem:tl5-hft-face]], let 𝔶₀ ∈ (0, μ⁻²] and 𝔶₁ ∈ (0,
μ⁻¹], let S_F^p, S_M^p, ε_M^p and 𝔯^p be S_F^z, S_M^z, ε_M^z and 𝔯^z formed with the constants with index p of
[[def:tl5-hfp-constants]], and put

    η_p := 1 − max(ϑ₁, ϑ₂) − 𝔯^p,      A_p := η_p^(−1/2) δ_w + η_p⁻¹ (ε^z + ε_M^p),      B_p := η_p⁻¹ (S_F^p + S_M^p),

and let 𝔰_*^p be 𝔰_*^z formed with the constants with index p and with A_p in place of A_z. Suppose: (a) η₀ < 𝔰₁^v; (b)
the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N); (c) η_p > 0, 𝔰_*^p < 𝔰₁^v and the closing
condition

    4 A_p B_p = 4 η_p^(−3/2) (δ_w + η_p^(−1/2) (ε^z + ε_M^p)) (S_F^p + S_M^p) < 1.                 {#eq:tl5-hfp-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_p and 𝔰_*^p in place of A_w (or
A_(w,4)) and 𝔰_*. For 𝔶₀ = 𝔶₁ = 1 each constant with index p, and each of A_p, B_p and 𝔰_*^p, is at most the one of
[[thm:tl5-hfz]] it replaces, and η_p ≥ η_z; so the hypotheses of [[thm:tl5-hfz]], with the intrinsic Sobolev constants,
imply these.

*Proof.* The proof of [[thm:tl5-hfz]] applies with [[lem:tl5-hfp-abs]], [[lem:tl5-hfp-c1]], [[lem:tl5-hfp-low]] and, for
N = 4, [[lem:tl5-hfp-rec]] in place of [[lem:tl5-hfz-abs]], [[lem:tl5-hfz-c1]], the step at low levels and
[[lem:tl5-hfv-rec]]. Step 1 is the same and gives 𝔰(p) ≤ 𝔰_*^p < 𝔰₁^v. The bounds at p and on the faces that Steps 2 and
3 use hold with the constants with index p, by these lemmas and, for the constants of the products of level four with no
factor at a point, by [[lem:tl5-hfp-abs]] (a); ε^z is unchanged, as its coefficient of ϱ contains no Sobolev constant.
The rest is the proof of [[thm:tl5-hfv]] with A_p, B_p and [[eq:tl5-hfp-closing]]. For 𝔶₀ = 𝔶₁ = 1, [[lem:tl5-hfp-leaf]]
gives C_(E,r)^♯² ≤ 6C_(E,r)², and [[lem:tl5-hfp-abs]] gives 𝔗(𝔶) ≤ 1, k₁^(j,·,p) ≤ k₁^(j,·,z) and C_S^p ≤ C_S^E; so
C_(1,ϱ)^p ≤ C_(1,ϱ)^z, C_(1,0)^p ≤ C_(1,0) and C_(0,0)^p ≤ C_(0,0). By [[lem:tl5-hfp-c1]], C₁^p ≤ C₁^z and, at level
four, C₁^Γ ≤ √7 max_Z C₁^U({Z}) ≤ √7 C₁^z; with 𝔷₁′ ≤ √7 𝔷₁, 𝔷₂′ ≤ √7 𝔷₂ and C_S^p ≤ C_S^E this gives 𝔨_rec^(·,p) ≤
𝔨_rec^(·,z), and [[lem:tl5-hfp-low]] gives 𝔐_p^(m) ≤ (2𝔐^(m))^(1/2) max(C_S^E, C₁^z). Every constant of [[thm:tl5-hfz]]
is nondecreasing in these numbers, which gives the last claim as there. ∎

**Remark {#rem:tl5-hfp-what}** (What changes.) The constant of [[eq:tl5-hft-leaf]] comes from ‖(1 + Ω)A‖² ≤ 6 Σ_(|J|≤2)
‖ℒ^J A‖², while on each V_π the sum over the 43 words is exactly (1 + c_π + c_π²) ‖A_π‖²; so C_(E,r)^♯ is at most
(2/9)^(1/2) < 0.48 times (6C_(E,r)²)^(1/2), in every constant formed with a Sobolev inequality on a face. In the bounds
at a point the words J of length k < 2 take the weights 𝔶_k ≤ μ^(k−2), which the energies of the words JB and ZJB allow,
against the weight 1 of the words of length two; the terms of C_(E,r)(𝔶)² are divided by 𝔶₀ + 𝔶₁ c_π + c_π² in place of
1 + c_π + c_π², so the representations with small c_π are bounded through the words of lengths zero and one. The parts
with ϱ and η₀ carry 𝔗(𝔶), which is at most 1 for all admissible weights in [[lem:tl5-hft-small]] (b) and equals ((ν²𝔶₀ +
6ν𝔶₁ + 36)/43)^(1/2) at level four; in [[lem:tl5-hfs-linfty]] and [[lem:tl5-hft-small]] (a) it grows with the weights,
which then trade the part with ℰ_g against those with ϱ and η₀. In 𝔨_rec the seven fields are counted together: where √7
C₁^z counts the leading term of the recovery √7 times, C₁^Γ counts it once over the 301 words JZ, the nonlinear part
keeping the count 301^(1/2) = (7 · 43)^(1/2) and the parts with ϱ and η₀ the factor √7; at the levels N ≥ 6, 𝔐_p^(m)
counts the words of each length in the same way, in place of (2𝔐^(m))^(1/2) times the bound of one word. The leading
term of the recovery is the one term bounded through 𝒟_g, whose density carries 𝔨₂′ = 𝔨₂ − 1/(2Ω̂²z̲); the minimum in
[[eq:tl5-hfp-c1]] keeps C₁(𝔚) ≤ C₁^U(𝔚). The number K_rec = max(|T|⁻¹, λ_M^(−1/2)) is the operator norm of the map
(v_Z)_Z ↦ (|T|⁻¹ v_T, (Σ_(a<b) c^ab_j v_(K_ab))_j) of the proof of [[lem:tl5-hf-recovery]], by [[lem:tl5-hf-fields]]
(a), so it is the best constant of that step for vectors v_Z of any size; a smaller one would need bounds that separate
the words beginning with T from those beginning with a rotation, which 𝒥_g and 𝒟_g do not give. As for [[thm:tl5-hf]]
and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfp]] are established in this paper for no background at 10 l5.

### Placement

This part, the comparison and the crosswalk rows below are instructions and notes for merging; they are not chapter text.
Old texts are quoted exactly from chapters/87-ten-l5.md at HEAD 3a6a1ee0, where sec:tl5-hfz is merged (Section 57.24,
merge 626bca77). Line numbers serve only to find the place.

*1. Where the section goes.* The section above, from its heading (label sec:tl5-hfp) through the last line of
[[rem:tl5-hfp-what]], is inserted at the end of [[ch:ten-l5]], after the last line of [[rem:tl5-hfz-what]] (line 6599, as
changed by item 2), with one blank line before it, as a sibling "###" section. No number already printed changes.

*2. The last sentence of [[rem:tl5-hfz-what]] (lines 6598–6599).* Old:

is needed. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfz]] are established in this paper
for no background at 10 l5.

New:

is needed. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of [[thm:tl5-hfz]] are established in this paper
for no background at 10 l5. [[sec:tl5-hfp]] sharpens the Sobolev constants and the bound of D̂²h ([[thm:tl5-hfp]]).

*3. Nothing else changes.*

### Comparison and the factors for the evaluation

Not chapter text. thm:tl5-hfp is stated with the intrinsic choice of def:tl5-hft-constants (6C_(E,r)² in place of
6C_(S³)² 𝔭_r, the same choice throughout); the other choice is not sharpened here. Every factor below replaces one of
thm:tl5-hfz, and at 𝔶₀ = 𝔶₁ = 1 each is at most it, so thm:tl5-hfp contains thm:tl5-hfz with that choice (its last
sentence). Unchanged: 𝔰₀, 𝔰₁^v and the cap 𝔰_(θ,v); 𝔨_♯, K_rec, 𝔯_♯, k₂^z, k₃^z, 𝔵^z and ε^z (its coefficient of ϱ has
no Sobolev constant); 𝔨₂ and z̲, so the rates; the word counts of the products and 𝔠^♮.

1. The leaf constant (lem:tl5-hfp-leaf, lem:tl5-hfp-abs (a)). With c := 2j₁(j₁ + 1) + 2j₂(j₂ + 1) and
   d := (2j₁ + 1)(2j₂ + 1) m_(j₁j₂)(r),
       C_(E,r)^♯² = (1/(2π²)) Σ d/(1 + c + c²)   replaces   6C_(E,r)² = (6/(2π²)) Σ d/(1 + c)²
   in every constant formed with lem:tl5-hft-face: C_S^E (r = 2), C₁ (r = 3, so 258 C_(E,3)² becomes 43 C_(E,3)^♯²),
   C_(1,ϱ), C_(1,0) (516π² C_(E,3)² becomes 86π² C_(E,3)^♯²), C_(0,0), the bounds of lem:tl5-hf4-face (b) used by the
   products at level four (𝔭_r/2 = 6C_(E,r)² there, so 𝔭_r = 12 C_(E,r)² becomes 2 C_(E,r)^♯²), and 6C_(S³)² = 1/2 in
   eq:tl5-hf-sphere (C_(E,0)^♯²). Proved: C_(E,r)^♯ ≤ (2/9)^(1/2) (6C_(E,r)²)^(1/2), (2/9)^(1/2) = 0.4714, −0.327
   decades, from (4/3)(1 + c + c²) − (1 + c)² = (1 − c)²/3. Summed (j₁ ≤ 4000, the tail extrapolated in 1/j₁):
       r                 0        1        2        3        4
       6C_(E,r)²         0.5000   1.4775   5.3650   21.825   94.259
       C_(E,r)^♯²        0.0873   0.2618   0.9551   3.8832   16.727
       ratio of the constants (C_(E,r)^♯²/(6C_(E,r)²))^(1/2)   0.4177   0.4209   0.4219   0.4218   0.4213
   so −0.375 decades on every such constant, for every rank, at no cost.
2. The weights (lem:tl5-hfp-leaf, lem:tl5-hfp-abs (a), (c), lem:tl5-hfp-c1). For 𝔶₀ ∈ (0, μ⁻²], 𝔶₁ ∈ (0, μ⁻¹],
       C_(E,r)(𝔶)² = (1/(2π²)) Σ d/(𝔶₀ + 𝔶₁ c + c²)
   in place of C_(E,r)^♯² in the parts with ℰ_g of C_S^p (r = 2) and of C₁(𝔚) (r = 3), and C_(E,r)(𝔶)² 𝔗(𝔶)² in the
   parts with ϱ and η₀ (C_(1,ϱ)^p, C_(1,0)^p, C_(0,0)^p; so 516π² C_(E,3)² in C_(1,0) becomes 86π² 𝔗(𝔶)² C_(E,3)(𝔶)²),
   with
       𝔗(𝔶)² = (𝔶₀ + 6𝔶₁ + 36)/43           under lem:tl5-hfs-linfty and lem:tl5-hft-small (a),
       𝔗(𝔶)² = (μ²𝔶₀ + 6μ𝔶₁ + 36)/43        under lem:tl5-hft-small (b)  (≤ 1 for all admissible weights),
       𝔗(𝔶)² = (ν²𝔶₀ + 6ν𝔶₁ + 36)/43        under lem:tl5-hfq-theta, ν = μ^θ.
   Summed ratios q_r := C_(E,r)(𝔶)/C_(E,r)^♯, rank 3 (rank 2 in brackets):
       𝔶 = (μ⁻², μ⁻¹):       μ = 10⁻⁴: 0.1211 (0.1092);   10⁻⁵: 0.0674 (0.0608);   3 × 10⁻⁶: 0.0493 (0.0444)
       𝔶 = (μ⁻¹, μ^(−1/2)):  μ = 10⁻⁴: 0.3820 (0.3454);   10⁻⁵: 0.2876 (0.2596);   3 × 10⁻⁶: 0.2476 (0.2233)
   The parts with ℰ_g fall by q_r, those with ϱ and η₀ by q_r 𝔗(𝔶). At G0l's level-4 optima (μ = 10⁻⁵, 10⁻⁴,
   3 × 10⁻⁶, 10⁻⁵; θ = 0.6875, 0.8125, 0.75, 0.875) under lem:tl5-hfq-theta, rank 3: q₃ 𝔗 = 0.41, 0.186, 0.207, 0.0914
   at 𝔶 = (μ⁻², μ⁻¹), and 0.266, 0.351, 0.227, 0.263 at 𝔶 = (μ⁻¹, μ^(−1/2)). Under lem:tl5-hft-small (b) (G0l's level-6
   option) at 𝔶 = (μ⁻², μ⁻¹), 𝔗 = 1 and every part falls by q_r. Under lem:tl5-hfs-linfty and lem:tl5-hft-small (a)
   𝔗 grows, q₃ 𝔗 = 185–2500 at (μ⁻², μ⁻¹) and 6–22 at (μ⁻¹, μ^(−1/2)) for these μ: there the weights trade the part
   with ℰ_g against those with ϱ and η₀, and 𝔶 = 1 remains available.
3. The fields in k₁ (lem:tl5-hfp-abs (b)).
       k₁^(j,ν′,p) = 𝔨_♯ K_rec (1 + ν′^(1/2) 𝔷′) + (1 − 𝔰₁^v)⁻¹ (ν′^(1/2) 𝔯_♯ + α_𝔄^(j,ν′)),
       𝔷′ = ((3 (Σ_Z |D̂Z|²)^(1/2))² + (2 (Σ_Z |D̂²Z|²)^(1/2))²)^(1/2),
   against k₁^(j,ν′,z) with √7 (3 max_Z |D̂Z| + 2 max_Z |D̂²Z|) in place of 𝔷′; the ratio of the two factors lies in
   [1/√14, 1]. In 𝔨_rec, 𝔷₁′ = 3 (Σ_Z |D̂Z|²)^(1/2) and 𝔷₂′ = 2 (Σ_Z |D̂²Z|²)^(1/2) replace √7 𝔷₁ and √7 𝔷₂. It acts
   only through the parts with ν′^(1/2), which G0l finds visible at μ = 10⁻⁴ alone (k₁^z = 3.05 against 2.3).
   The refined per-word bound k₁^D 𝒟_g + (k₁^(j,μ,p) − k₁^D + 2𝔵^z) 𝒥_g, k₁^D = 𝔨_♯ K_rec, is used here only inside
   eq:tl5-hfp-words; the constants of S_F keep the form (k₁^(j,μ,p) + 2𝔵^z) 𝒥_g.
4. The first-order constant over a family (eq:tl5-hfp-c1, lem:tl5-hfp-words). For a family 𝔚 of n words of one length,
       𝔩_D(𝔚) = k₁^D (1 + (43n)^(1/2) 𝔵^z/(1 − 𝔵^z)),
       𝔩_J(𝔚) = μ^(1/2) (k₁^D 𝔷′ + (1 − 𝔰₁^v)⁻¹ 𝔯_♯) + (1 − 𝔰₁^v)⁻¹ 𝔞_𝔄(𝔚)
                + (43n)^(1/2) 𝔵^z (k₁^p − k₁^D + 2)/(1 − 𝔵^z),
       C₁^U(𝔚)² = C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(μ^(1/2) + ϖ′^(1/2))²
                  + 2|∂_γ|² (𝔩_D(𝔚) + 𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
       C₁^D(𝔚)² = C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂′ (μ (1 + 18|D̂∂_γ|²) + 2|∂_γ|² 𝔩_D(𝔚)²),
       C₁^J(𝔚)² = C_(E,3)(𝔶)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²) ϖ′ + 2|∂_γ|² (𝔩_J(𝔚) + (2ϖ′)^(1/2))²),
       C₁(𝔚) = min(C₁^U(𝔚), C₁^D(𝔚) + C₁^J(𝔚)),   𝔨₂′ = 𝔨₂ − 1/(2Ω̂² z̲) = max(1/c, 1/κ′)/(2Ω̂²),
       𝔞_𝔄(𝔚) ≤ (43n/2)^(1/2) α_𝔄^(N−1,μ),   𝔞_𝔄(𝔚) ≤ (Σ_(B∈𝔚) 𝔞_𝔄({B})²)^(1/2),
   against C₁^z² = 6C_(E,3)² 𝔴₀(p)⁶ sup 𝔳₀⁶ R⁻³ 𝔨₂ ((1 + 18|D̂∂_γ|²)(1 + ϖ′^(1/2))² + 2|∂_γ|² (𝔩 + (2ϖ′)^(1/2))²),
   𝔩 = 𝔩₀ + √43 𝔵^z (k₁^z + 2)/(1 − 𝔵^z). For one word (n = 1) at 𝔶 = 1 the changes are: C_(E,3)^♯² for 6C_(E,3)²;
   (μ^(1/2) + ϖ′^(1/2))² for (1 + ϖ′^(1/2))² (free; G0l: at most 0.02 decades); 𝔷′ for the √7 form; the split, in which
   only the leading term 𝔨_♯ K_rec 𝒟_g carries 𝔨₂′. The weight z̲ itself is not changed, so the rates are not.
   C₁^p = max_(|B|≤N−3) C₁({B}) replaces C₁^z wherever it enters (C_P^v, 𝔎, S_F, 𝔰_*), and C_S^p replaces C_S^E.
5. The seven fields in 𝔨_rec (lem:tl5-hfp-rec), N = 4.
       𝔨_rec^p     = 𝔨_♯ K_rec (C₁^Γ + 𝔷₁′ μ^(1/2) C₁^p + 𝔷₂′ μ C_S^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^p,
       𝔨_rec^(ϱ,p) = 𝔨_♯ K_rec (√7 + 𝔷₁′ μ^(1/2)) C_(1,ϱ)^p,
       𝔨_rec^(0,p) = 𝔨_♯ K_rec ((√7 + 𝔷₁′ μ^(1/2)) C_(1,0)^p + 𝔷₂′ μ C_(0,0)^p) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_(0,0)^p,
   against 𝔨_rec^z = 𝔨_♯ K_rec √7 (C₁^z + 𝔷₁ μ^(1/2) C₁^z + 𝔷₂ μ C_S^E) + (1 − 𝔰₁^v)⁻¹ μ 𝔯_♯ C_S^E and the forms with ϱ
   and η₀ likewise with √7 (1 + 𝔷₁ μ^(1/2)). C₁^Γ = C₁(Γ), n = 7: the leading term counts once over the 301 words JZ in
   place of √7 times, the nonlinear part keeps √301 = √7 √43, the parts with μ^(1/2) count once, and the couplings
   count through 𝔞_𝔄(Γ) ≤ (301/2)^(1/2) α_𝔄^(N−1,μ) or ≤ √7 max_Z 𝔞_𝔄({Z}). This is G0l's √301 lever, with two
   departures from its pricing (C₁^(301), 𝔞_𝔄 without √7): the μ^(1/2) parts lose their √7 (better), the couplings keep
   it (worse; at α_𝔄 = 0.06 and the trivial bound, 0.74 in place of 0.28 in a k-term of 4.4–10.7). By lem:tl5-hfp-c1,
   C₁^Γ ≤ √7 max_Z C₁^U({Z}) ≤ √7 C₁^z at 𝔶 = 1.
6. The low levels (lem:tl5-hfp-low).
       𝔐_p^(m) = (Σ_(b≤m+1) (C_S^p² + C₁(𝔚_b)²))^(1/2)   replaces   (2𝔐^(m))^(1/2) max(C_S^E, C₁^z),
       𝔐^(m) = Σ_(b≤m+1) 7^b,
   in the part with ℰ_g of C_(∞,μ)^(m) (k₁^(m,μ) (2𝔐^(m))^(1/2) max(C_S, C₁) becomes k₁^(m,μ,p) 𝔐_p^(m)) and its forms;
   the parts with ϱ and η₀ keep (2𝔐^(m))^(1/2), formed with C_(1,ϱ)^p, C_(1,0)^p, C_(0,0)^p. 𝔚_b is the family of the
   7^b words of length b; C_S^p counts once per length, and C₁(𝔚_b) counts the leading term once over the 7^b words. At
   N = 4 this is C_(∞,μ)^(0) of 𝔰_(*,q) in eq:tl5-hfq-constants (m = 0: 𝔐_p^(0) = (2C_S^p² + C₁({∅})² + C₁(Γ)²)^(1/2)
   against 4 max(C_S^E, C₁^z)); at N ≥ 6 it is C_P = C_(∞,μ)^(m_P) (C_(∞,μ)^(1) at level 6) and C_(∞,μ)^(N−4) of 𝔰_*.
7. The closing condition eq:tl5-hfp-closing has the form of eq:tl5-hfz-closing with η_p, ε^z, ε_M^p, S_F^p, S_M^p:
   4 η_p^(−3/2) (δ_w + η_p^(−1/2) (ε^z + ε_M^p)) (S_F^p + S_M^p) < 1, with 𝔰_*^p < 𝔰₁^v and η₀ < 𝔰₁^v.

What it gives, deduced, not evaluated. Assumptions: G0l's optima (its tables G0l.0, G0l.1, G0l.4: μ, 𝔵^z, θ, k₁^z);
the bracket of C₁ its k-term (93–95.5 % at the supremum, G0l.2); k₁^D = 𝔨_♯ K_rec = 2.30; α_𝔄 = 0.06; 𝔨₂′ = 𝔨₂/4, which
is G0l's price of 1/z̲ out of 𝔨₂ (C₁ ÷ 2) read back; all suprema at one point.

Level 4 (lem:tl5-hfq-theta), at 𝔶 = (μ⁻², μ⁻¹), for seed 1 D_A, seed 2 D_A, seed 1 D*, seed 2 D*:
- every constant formed with a Sobolev inequality on a face: −0.375 (item 1);
- the parts with ℰ_g of C_S, C₁ and 𝔨_rec: further −1.17, −0.92, −1.31, −1.17 (q₃); the parts with ϱ and η₀: further
  −0.39, −0.73, −0.68, −1.04 (q₃ 𝔗);
- C₁ by the split alone: further −0.23, −0.18, −0.19, −0.19;
- the leading term of 𝔨_rec by the family Γ: further −0.27, −0.30, −0.15, −0.13 (trivial bound of 𝔞_𝔄(Γ); −0.33, −0.36,
  −0.17, −0.16 with 𝔞_𝔄(Γ) = √7 α_𝔄), and with the split −0.45, −0.45, −0.30, −0.28;
- so C_P^v falls by about 2.0, 1.75, 2.0, 1.8 decades and is still led by 𝔨_rec (its lead over C₁, 0.82–1.02, falls by
  about 0.1–0.27; over 2C_S, 1.86–2.20, by about 0.25–0.4, as C_S takes q₂ < q₃);
- 𝔰_(*,q): where its term with A carries C_(∞,μ)^(0) as in eq:tl5-hfq-constants, that term takes items 1 and 2 and
  𝔐_p^(0), further −0.36, −0.38, −0.27, −0.26 (−0.56, −0.54, −0.44, −0.42 with the split); where the evaluation carries
  C_P^v there (G0l.1), it falls with C_P^v; its terms with ϱ and η₀ take −0.76 to −1.41 in all;
- at the 1:1 rate of G0l.1 this is up to about 1.75–2.0 decades on min(f, ϱ). Caps that need the evaluation: S_M,
  2.0–2.4 decades below S_F at the optimum, takes only the factor of item 1 where its constants are formed with
  lem:tl5-hf4-face alone, so the gap would close to about 0.4–1.0 decades and S_M cost up to about 0.15; the parts with
  ϱ and η₀ fall less than C_P^v, and ϱ sits 0.02–0.12 above f; and the 𝔰_* slack, which items 1, 2 and 6 move as well.
Level 6 (lem:tl5-hft-small (b), G0l.4), at 𝔶 = (μ⁻², μ⁻¹), 𝔗 = 1:
- every Sobolev-formed constant, the parts with ϱ and η₀ included: −0.375 and further −1.17, −0.92, −1.31, −1.17;
- the leading terms of C_(∞,μ)^(1) (= C_P at level 6) and C_(∞,μ)^(2) (in 𝔰_*) by 𝔐_p: further −0.57 to −0.73 and
  −0.69 to −1.01 (𝔵^z = 0.002–0.011, 𝔞_𝔄({B}) between 0 and its trivial bound; 𝔐_p^(1)/C₁ = 1.98–2.90 against
  √114 = 10.7, 𝔐_p^(2)/C₁ = 2.76–5.73 against √800 = 28.3), and about −0.2 by the split;
- ϱ binds there and ϱ ∝ 1/(sup C_(∞,μ) k₂^z) (G0l.4), so ϱ could move by up to about 2.2–2.9 decades; f sits 0.21–0.48
  above ϱ and moves with C_P. This needs the evaluation.

Choices for the evaluation. 𝔶 = (μ⁻², μ⁻¹) under lem:tl5-hfq-theta and lem:tl5-hft-small (b); a scan 𝔶₀ = 𝔶₁²,
𝔶₁ ∈ [μ^(−1/2), μ⁻¹] shows the trade with the parts with ϱ and η₀ (at seed 1 D_A the part with ϱ prefers μ^(−1/2):
0.266 against 0.41). 𝔶 = 1 under lem:tl5-hfs-linfty and lem:tl5-hft-small (a), unless ϱ and η₀ have room. The minimum
in eq:tl5-hfp-c1 face by face; 𝔞_𝔄(Γ) by its second bound with a Schur bound per word.

Target 2, "is K_rec ≈ 1 itself sharp?" Yes, for this step. K_rec = max(|T|⁻¹, λ_M^(−1/2)) is the operator norm of the
block-diagonal map (v_Z)_Z ↦ (|T|⁻¹ v_T, (Σ_(a<b) c^ab_j v_(K_ab))_j) of the proof of lem:tl5-hf-recovery: on the block
of the rotations C Cᵀ = M⁻¹ by lem:tl5-hf-fields (a), whose norm is λ_M^(−1/2), so equality holds for some vector
(v_Z) of any size. At G0k's points K_rec ≈ 1.00 and k₁^D = 𝔨_♯ K_rec ≈ 2.30, with 𝔨_♯ → √5 the best of P-GRD9's
argument. A smaller k₁ needs bounds that separate the words beginning with T from those beginning with a rotation, which
𝒥_g and 𝒟_g do not give; the lever proved instead is the split, which lowers the density in front of k₁^D (𝔨₂′).

Not done.
- Target 4 (the word count 7² in 𝔤_(𝒥,s) and 𝔠^♮₄(μ) against 9·2⁴): not attempted; nothing in these arguments produces
  them, and G0l prices them as capped by 𝔰_*.
- The other choice of def:tl5-hft-constants (6C_(S³)² 𝔭_r) and its weights: not done.
- The absorption of the nonlinear part over the words (G0l: +0.02–0.13): not done; it keeps (43n)^(1/2) 𝔵^z.
- The 1/κ′ part of 𝔨₂ (G0k: ≤ 0.1) and z̲ in the rates: not touched.
- The refined per-word bound of item 3 in the constants of S_F: not used.

### Crosswalk rows

Rows for the crosswalk of [[ch:ten-l5]], in its four columns, separated by tabs, in chapter order; the line numbers
are those of this file:
    sec:tl5-hfp	paper/reader/proofs/P-GRD10.md@PENDING:1	P-GRD10, section	new; at the end of ch:ten-l5, after rem:tl5-hfz-what; sharp leaf Sobolev constant, weights of the words, the seven fields together
    lem:tl5-hfp-leaf	paper/reader/proofs/P-GRD10.md@PENDING:16	P-GRD10, Lemma	Sobolev inequality on the leaves with its own constant C#^2 = (1/2pi^2) sum d/(1 + c + c^2) <= (4/3) C^2 = (2/9) 6C^2, and with weights y0, y1 on the words of lengths 0, 1
    eq:tl5-hfp-leaf	paper/reader/proofs/P-GRD10.md@PENDING:24	P-GRD10, display	new
    def:tl5-hfp-constants	paper/reader/proofs/P-GRD10.md@PENDING:44	P-GRD10, Definition	constants with index p: weights y0 <= mu^-2, y1 <= mu^-1, z', k1^(j,nu,p), k1^D, k2', D_g, a_A(W), l_D, l_J, C1(W) = min(C1^U, C1^D + C1^J), C1^p, C1^Gamma, T(y), C_S^p, M_p^(m), krec^p
    eq:tl5-hfp-c1	paper/reader/proofs/P-GRD10.md@PENDING:65	P-GRD10, display	new
    lem:tl5-hfp-abs	paper/reader/proofs/P-GRD10.md@PENDING:84	P-GRD10, Lemma	the face lemma with C#^2 and with weights; k1 with z'; refined per-word bound with D_g; zeroth-order bound with C_S^p, also over a family of words
    lem:tl5-hfp-words	paper/reader/proofs/P-GRD10.md@PENDING:128	P-GRD10, Lemma	second derivatives over a family of n words, with weights: leading term once through D_g, nonlinear part with (43n)^(1/2), couplings through a_A(W)
    eq:tl5-hfp-words	paper/reader/proofs/P-GRD10.md@PENDING:134	P-GRD10, display	new
    lem:tl5-hfp-c1	paper/reader/proofs/P-GRD10.md@PENDING:160	P-GRD10, Lemma	first-order bound over a family with C1(W); C1(W) <= n^(1/2) max C1^U({B}); C1^U({B}) <= C1^z at y0 = y1 = 1
    eq:tl5-hfp-family	paper/reader/proofs/P-GRD10.md@PENDING:164	P-GRD10, display	new
    lem:tl5-hfp-rec	paper/reader/proofs/P-GRD10.md@PENDING:211	P-GRD10, Lemma	lem:tl5-hfv-rec with krec^p: the seven fields as one family, C1^Gamma in place of sqrt7 C1^z
    lem:tl5-hfp-low	paper/reader/proofs/P-GRD10.md@PENDING:222	P-GRD10, Lemma	second derivatives at low levels with M_p^(m) in place of (2M^(m))^(1/2) max(C_S, C1)
    thm:tl5-hfp	paper/reader/proofs/P-GRD10.md@PENDING:236	P-GRD10, Theorem	thm:tl5-hfz with the constants with index p and the intrinsic Sobolev constants; contains it at y0 = y1 = 1
    eq:tl5-hfp-closing	paper/reader/proofs/P-GRD10.md@PENDING:247	P-GRD10, display	closing condition: 4 eta_p^(-3/2)(delta_w + eta_p^(-1/2)(eps^z + eps_M^p))(S_F^p + S_M^p) < 1
    rem:tl5-hfp-what	paper/reader/proofs/P-GRD10.md@PENDING:266	P-GRD10, Remark	what changes; K_rec is the operator norm of its step

Note to change in the existing row of the crosswalk of [[ch:ten-l5]]: rem:tl5-hfz-what, add "; points to sec:tl5-hfp
(P-GRD10 item 2)".
