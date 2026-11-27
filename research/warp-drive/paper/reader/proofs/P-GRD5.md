### The constants sharpened a fifth time {#sec:tl5-hfv}

This section sharpens the constants of [[sec:tl5-hft]] (level N ≥ 6) and of [[sec:tl5-hfq]] (level four) in four ways
and proves [[thm:tl5-hf]] and [[thm:tl5-hf4]] with them. First, the number ϑ of the quasilinear term is replaced by two
numbers ϑ₁, ϑ₂ ∈ (0, 1), one for each family of faces, and the bootstrap is closed with η := 1 − max(ϑ₁, ϑ₂) − 𝔯 in place
of the bounds ϑ ≤ 1/4 and 𝔯 ≤ 1/4; this frees the cap 𝔰_θ of the smallness condition and the factor 8√2 of the closing
condition ([[lem:tl5-hfv-close]]). Second, the conversion of the high factor into the densities is made separately for
the two families of faces ([[lem:tl5-hfv-conv]]). Third, |H| ≤ 𝔤₁ |h| replaces |H| ≤ 2|h| in the constant 𝔨_B. Fourth, at
level four the recovery of D̂²h at a point is bounded term by term ([[lem:tl5-hfv-rec]]). The closing conditions are
[[eq:tl5-hfv-closing]]; the earlier ones remain valid. Throughout, the notation is that of [[sec:tl5-hfs]],
[[sec:tl5-hft]] and [[sec:tl5-hfq]].

**Lemma {#lem:tl5-hfv-close}** (Two numbers for the quasilinear term.) Let ϑ₁, ϑ₂ ∈ (0, 1), and put

    θ_H^(1) := (√2 + 1/2) |H| (c + κ′)/min(c, κ′),      θ_H^(2) := (√2 + 1/2) |H| (1 + κc)/(κc),
    𝔰_(θ,v) := min(ϑ₁ (√2 + 1/2)⁻¹ inf_(D^κ) min(c, κ′)/(c + κ′),
                   ϑ₂ (√2 + 1/2)⁻¹ inf_(D^κ) κc/(1 + κc)).                                              {#eq:tl5-hfv-cap}

If |H| ≤ 𝔰_(θ,v) at a point, then θ_H^(1) ≤ ϑ₁ and θ_H^(2) ≤ ϑ₂ there; the face densities of J̃ := J[Ψ] − 𝔟[Ψ] on the
faces Σ₁ and Σ₂ are at least (1 − ϑ₁) ε₁[Ψ] and (1 − ϑ₂) ε₂[Ψ]; and for rates a_o, a_i and φ as in
[[prop:tl5-hf-linear]],

    2Ω̂² |dφ(𝔟[Ψ])| ≤ ϑ₁ a_o (e_o + κ′ e_i) + ϑ₂ a_i (e_i + κ e_o).                                    {#eq:tl5-hfv-dphi}

So if the rates â_o := (1 − ϑ₁) a_o and â_i := (1 − ϑ₂) a_i are admissible for (𝔅_N, E_o^N, E_i^N), then the linear
bulk ñᵀ 𝔅_N ñ − 2Ω̂² dφ(J̃) of the proof of [[prop:tl5-hf-bootstrap]] is at most 0. Finally, if Y ≥ 0 satisfies η Y² ≤
δ² + Y ε + S Y³ with η > 0 and δ, ε, S ≥ 0, then Y ≤ A + B Y² with A := η^(−1/2) δ + η⁻¹ ε and B := η⁻¹ S.

*Proof.* The proof of [[lem:tl5-hf-quasilinear]] (b) gives 2Ω̂² |dτ₁(𝔟)| ≤ θ_H^(1) (e_o + κ′ e_i) and 2Ω̂² |dτ₂(𝔟)| ≤
θ_H^(2) (e_i + κ e_o) separately, and the definition of 𝔰_(θ,v) gives the first claim. The face densities are those of
the proof of [[prop:tl5-hf-bootstrap]], Step 2, with θ_H^(1) and θ_H^(2) in place of θ_H. As dφ = a_o dτ₁ + a_i dτ₂,
[[eq:tl5-hfv-dphi]] follows; and 2Ω̂² dφ(J) = (a_o + κ a_i) e_o + (a_i + κ′ a_o) e_i, so 2Ω̂² dφ(J̃) ≥ (â_o + κ â_i)
e_o + (â_i + κ′ â_o) e_i, which dominates ñᵀ 𝔅_N ñ by the admissibility of â_o, â_i. For the last claim, if Y ≥ η^(−1/2)
δ, then Y ≤ η⁻¹ δ²/Y + η⁻¹ ε + η⁻¹ S Y² ≤ A + B Y², and otherwise Y < A. ∎

**Lemma {#lem:tl5-hfv-conv}** (The conversion into the densities, by families.) Let A := 1/z̲ + 1/c and

    𝔣₂^o := √2 Ω̂ (A (1 + cA))^(1/2),      𝔣₂^i := √2 Ω̂ (1/A + c)^(1/2).

Then for every family of fields as in [[prop:tl5-hf-linear-n]], with 𝒥_g and the weighted sums e_o, e_i of it,
2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂^o e_o + 𝔣₂^i e_i.

*Proof.* By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ A e_o + e_i, and by the Cauchy–Schwarz inequality √e_o + √c √e_i ≤ (1/A +
c)^(1/2) (A e_o + e_i)^(1/2); so 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ √2 Ω̂ (1/A + c)^(1/2) (A e_o + e_i), which is the claim. ∎

**Lemma {#lem:tl5-hfv-rec}** (The recovery of D̂²h at a point, term by term.) Let N = 4 and put 𝔷₁ := 3 max_Z |D̂Z| and
𝔷₂ := 2 max_Z |D̂²Z|, and, with the constants of [[lem:tl5-hfs-linfty]] (C₁ := C₁^♮, C_(1,0) := C_(1,0)^♮),

    𝔨_rec := (6/5) ((√3 + 8/3) K_rec √7 (C₁ + 𝔷₁ μ^(1/2) C₁ + 𝔷₂ μ C_S) + μ 𝔯₀ C_S),
    𝔨_rec^ϱ := (6/5) (√3 + 8/3) K_rec √7 (1 + 𝔷₁ μ^(1/2)) C_(1,ϱ),
    𝔨_rec^0 := (6/5) ((√3 + 8/3) K_rec √7 ((1 + 𝔷₁ μ^(1/2)) C_(1,0) + 𝔷₂ μ C_(0,0)) + μ 𝔯₀ C_(0,0)),
    C_P^v := 2 max(2C_S, C₁, 𝔨_rec),   C_(P,ϱ)^v := 2 max(C_(1,ϱ), 𝔨_rec^ϱ + k₂),
    C_(P,0)^v := 2 max(2C_(0,0), C_(1,0), 𝔨_rec^0).

In the setting of [[lem:tl5-hfs-linfty]] or of [[lem:tl5-hft-small]] (b), the bound of 𝔰_P = 𝔰_g^(0) of
[[eq:tl5-hfs-linfty]] holds with C_P^v, C_(P,ϱ)^v and C_(P,0)^v in place of C_P^♮, C_(P,ϱ)^♮ and C_(P,0)^♮.

*Proof.* In the step on second derivatives at low levels of the proof of [[lem:tl5-hfs-linfty]] with B = ∅, the bound of
[[lem:tl5-hf-recovery]] for h, as used in the proof of [[lem:tl5-hf-linfty]], is (6/5) times (√3 + 8/3) K_rec
((Σ_Z |D̂Ψ_Z|²)^(1/2) + (Σ_Z 𝔷_Z²)^(1/2)) + (4/3)|𝔣| + 𝔯₀ |h|, with (Σ_Z 𝔷_Z²)^(1/2) ≤ √7 (𝔷₁ |D̂h| + 𝔷₂ |h|), and 𝔣 has
no part 𝔄 at level zero. Multiply by μ² and bound each jet by its weighted bound at p: μ² |D̂Ψ_Z| ≤ C₁ ℰ_g^(1/2) +
C_(1,ϱ) ϱ(p) + C_(1,0) η₀(p) for the seven fields Z, μ² |D̂h| ≤ μ^(1/2) times that bound, and μ² |h| ≤ μ (C_S ℰ_g^(1/2) +
C_(0,0) η₀(p)), in place of the bound of L_g by (2𝔐^(0))^(1/2) times the largest of them; the residual and the nonlinear
terms are as there. Taking the largest of the four bounds and absorbing 𝔰_g^(0)/2 as there gives the claim. ∎

**Definition {#def:tl5-hfv-constants}** (The constants sharpened a fifth time.) Let N ≥ 6 and the constants be those of
[[def:tl5-hft-constants]] with either option, or N = 4 and those of [[def:tl5-hfq-constants]] for some θ ∈ [0, 1]. Fix
ϑ₁, ϑ₂ ∈ (0, 1). Form the same constants with the following replacements, and call them the constants with index v:
𝔰_θ by 𝔰_(θ,v) in 𝔰₁ (that is in 𝔰₁^t or 𝔰₁^q); in 𝔞_(o,s) and 𝔟_(o,s) the factor 𝔣₂ by 𝔣₂^o, and in 𝔞_(i,s) and
𝔟_(i,s) by 𝔣₂^i; 𝔨_B by max(𝔷, 𝔤₁) in 𝔎, 𝔎_ϱ and 𝔎₀; and, for N = 4, C_P^♮, C_(P,ϱ)^♮ and C_(P,0)^♮ by C_P^v,
C_(P,ϱ)^v and C_(P,0)^v of [[lem:tl5-hfv-rec]]. With the resulting S_F^v := S_(F,s), S_M^v := S_(M,q) (0 for N ≥ 6),
ε^v := ε_(w,t) or ε_(w,q), ε_M^v := ε_(M,q) (0 for N ≥ 6), 𝔯^v := 𝔯_t or 𝔯_q, 𝔰₁^v and 𝔰_*^v (with A_v in place of A_t or
A_q), put

    η := 1 − max(ϑ₁, ϑ₂) − 𝔯^v,      A_v := η^(−1/2) δ_w + η⁻¹ (ε^v + ε_M^v),
    B_v := η⁻¹ (S_F^v + S_M^v).                                                                   {#eq:tl5-hfv-constants}

**Theorem {#thm:tl5-hfv}** (Existence close to an explicit background, with the constants sharpened a fifth time.) In
the setting of [[thm:tl5-hft]] (N ≥ 6) or of [[thm:tl5-hf4q]] (N = 4), with ϑ₁, ϑ₂ ∈ (0, 1) in place of ϑ and the
constants with index v of [[def:tl5-hfv-constants]], suppose: (a) η₀ < 𝔰₁^v; (b) the rates (1 − ϑ₁) a_o, (1 − ϑ₂) a_i
are admissible for (𝔅_N, E_o^N, E_i^N); (c) η > 0, 𝔰_*^v < 𝔰₁^v and the closing condition

    4 A_v B_v = 4 η^(−3/2) (δ_w + η^(−1/2) (ε^v + ε_M^v)) (S_F^v + S_M^v) < 1.                      {#eq:tl5-hfv-closing}

Then the conclusions of [[thm:tl5-hf]] (N ≥ 6) or [[thm:tl5-hf4]] (N = 4) hold with A_v and 𝔰_*^v in place of A_w (or
A_(w,4)) and 𝔰_*.

*Proof.* The proofs of [[prop:tl5-hft-bootstrap]] and [[prop:tl5-hfq-bootstrap]] apply with the following changes.
Step 1 uses only 𝔰_*^v < 𝔰₁^v, and gives |H| ≤ 𝔰 < 𝔰_(θ,v) on D^κ_s, so θ_H^(1) ≤ ϑ₁ and θ_H^(2) ≤ ϑ₂ by
[[lem:tl5-hfv-close]]. In Step 2 the face densities of J̃ are at least (1 − ϑ₁) ε₁ and (1 − ϑ₂) ε₂, and the linear bulk
with the weight is at most 0 by [[lem:tl5-hfv-close]] and (b); the conversion of the terms with 𝒥_g uses
[[lem:tl5-hfv-conv]], so 𝔣₂^o multiplies the densities e_o and 𝔣₂^i the densities e_i; in the bound of a factor H by the
energies, |H| ≤ 𝔤₁ |h|, as H = −g⁻¹ h ĝ⁻¹ and a factor g⁻¹ raising an index costs at most 1 + |H| ≤ 𝔤₁; and for N = 4,
[[lem:tl5-hfv-rec]] bounds 𝔰_P. Step 3 then gives (1 − max(ϑ₁, ϑ₂)) Σ_I μ^|I| ℰ_I(a′, b′) ≤ δ_w² + Y_s (ε^v + ε_M^v) +
𝔯^v Y_s² + (S_F^v + S_M^v) Y_s³, and taking the supremum, η Y_s² ≤ δ_w² + Y_s (ε^v + ε_M^v) + (S_F^v + S_M^v) Y_s³; the
last claim of [[lem:tl5-hfv-close]] gives Y_s ≤ A_v + B_v Y_s². The rest is the proof of [[thm:tl5-hft]] or
[[thm:tl5-hf4q]] with A_v, B_v and [[eq:tl5-hfv-closing]]; the proofs of persistence use only |H| ≤ 1/8 and θ_H ≤ ϑ on
each family of faces, and their choice of rates holds with (1 − ϑ₁) a_o, (1 − ϑ₂) a_i in place of (1 − ϑ) a_o, (1 − ϑ)
a_i. ∎

**Remark {#rem:tl5-hfv-what}** (What the fifth sharpening changes.) With ϑ₁ = ϑ₂ = 1/4 and 𝔯^v = 1/4, η = 1/2 and
[[eq:tl5-hfv-closing]] is the form 8(√2 δ_w + 2(ε^v + ε_M^v))(S_F^v + S_M^v) < 1 of the earlier theorems; smaller ϑ₁,
ϑ₂ and 𝔯^v let η approach 1 and remove the factor 8√2 up to 4, and larger ϑ₁, ϑ₂ raise the cap 𝔰_(θ,v) at the cost of η
and of larger rates a_o = â_o/(1 − ϑ₁), a_i = â_i/(1 − ϑ₂). The cap on the faces Σ₂ carries κc/(1 + κc), as the density
e_i + κ e_o of these faces controls the derivative along ê₄ only through κ e_o; the numbers κ, κ′ of
[[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
[[thm:tl5-hfv]] are established in this paper for no background at 10 l5.
