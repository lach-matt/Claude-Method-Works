# R-P-GRD5: review of proofs/P-GRD5.md (sec:tl5-hfv, "The constants sharpened a fifth time")

File reviewed: research/warp-drive/paper/reader/proofs/P-GRD5.md, md5 d8c646ead5b1ee58789f8bba0f43d317, 200 lines,
at f49900d7. Chapter: chapters/87-ten-l5.md at HEAD (6140 lines; identical to 87e4d2c5 and e047e7e0 for this chapter,
last changed by 40140118, as the Placement says). Line references "87:n" are to that chapter, "P:n" to the file.

Fixed copy: scratchpad/reader/rpgrd5/P-GRD5.fixed.md, md5 6ed9c26203ccdc2b2c46ec7eed4fc172, 210 lines, made by
scratchpad/reader/rpgrd5/tools/fix.py (8 replacements, each found exactly once; crosswalk @PENDING numbers recomputed
from the label lines).

## 1. Mechanics (both the file as submitted and the fixed copy)

Scratch merge into a fresh `git archive HEAD` tree with the writer's placement (item 2 applied as whole lines, found
once at 87:6139-6140; the section appended after the new last line with one blank line):

| check | P-GRD5.md | P-GRD5.fixed.md |
|---|---|---|
| lint.py --chapters | 62 files, 5232 labels (5221 + 11), 0 hits | 62 files, 5232 labels, 0 hits |
| assemble.py --check | 0 problems | 0 problems |
| in-memory check | `[] 0` | `[] 0` |
| lines over 121 characters | none outside the crosswalk rows | none outside the crosswalk rows |
| wrapped line starting with a forbidden mark | none | none |
| crosswalk rows: label at the stated line | 11 of 11 | 11 of 11 (lines 1, 13, 17, 23, 36, 51, 71, 81, 83, 88, 106) |
| chapter labels = crosswalk + new rows | 388 = 388 | 388 = 388 |

No printed number changes: the section is 57.20, thm:tl5-hfv is Theorem 57.197, rem:tl5-hfv-what Remark 57.198. All 11
labels are lowercase and new. The chapter text contains no file or program names, code or AI language.

## 2. The checks asked for

### 2.1 The cap 𝔰_θ

- **𝔰_(θ,v) (P:13-19).** The old cap (87:4451) is ϑ X with X = ((√2 + 1/2) sup max(R₁, R₂))⁻¹, R₁ = (c + κ′)/min(c, κ′),
  R₂ = (1 + κc)/(κc). Since sup max(R₁, R₂) = max(sup R₁, sup R₂), X = min(X₁, X₂) with X₁, X₂ exactly the two
  infima of [[eq:tl5-hfv-cap]]. |H| ≤ 𝔰_(θ,v) gives θ_H^(1) ≤ ϑ₁ and θ_H^(2) ≤ ϑ₂ at once. The proof of
  lem:tl5-hf-quasilinear (b) (87, the display with (√2 + 1/2)(c + κ′)|H| |D̂Ψ|² and the two density bounds
  2 min(c, κ′)Ω̂²|D̂Ψ|² and 2κcΩ̂²|D̂Ψ|²) indeed bounds dτ₁(𝔟) and dτ₂(𝔟) separately, so the split is legitimate.
  Correct.
- **[[eq:tl5-hfv-dphi]] and the linear bulk (P:23-33).** dφ = a_o dτ₁ + a_i dτ₂, so 2Ω̂²|dφ(𝔟)| ≤ ϑ₁ a_o(e_o + κ′e_i) +
  ϑ₂ a_i(e_i + κe_o); with 2Ω̂² dφ(J) = (a_o + κa_i)e_o + (a_i + κ′a_o)e_i this leaves (â_o + κâ_i)e_o + (â_i + κ′â_o)e_i,
  which dominates ñᵀ𝔅_N ñ when (â_o, â_i) is admissible. At ϑ₁ = ϑ₂ = ϑ hypothesis (b) is the old "(1 − ϑ)⁻¹𝔅_N"
  hypothesis, admissibility being linear in the rates. Correct.
- **The closing with η (P:26-27, P:94-96).** If Y ≥ η^(−1/2)δ, then η^(−1)δ²/Y ≤ η^(−1/2)δ, so Y ≤ A + BY²; otherwise
  Y < η^(−1/2)δ ≤ A. Step 3: the face densities are at least (1 − ϑ₁)ε₁ and (1 − ϑ₂)ε₂, hence at least
  (1 − max(ϑ₁, ϑ₂)) times the sum; moving 𝔯^v Y_s² to the left gives η Y_s² ≤ δ_w² + Y_s(ε^v + ε_M^v) + (S_F^v + S_M^v)Y_s³.
  Correct. 𝔯^v is 𝔯_t (= 𝔯_s, whose M part is 0 for N ≥ 5, 87:5674) or 𝔯_q = 𝔯_(w,s) + 𝔯_(M,q) (87:6097), so η carries the
  M part at level four as the old "𝔯_(w,s) + 𝔯_(M,q) ≤ 1/4" did.
- **Every old use of ϑ ≤ 1/4 or 𝔯 ≤ 1/4.** 87:4478 "(1 − ϑ) ≥ 3/4" (face densities, positivity only); 87:4509, 4873,
  5352, 5717, 5936 (Step 3: ϑ ≤ 1/4 and 𝔯 ≤ 1/4 give the factor 2; replaced by η); the smallness lists 87:4458, 4833,
  5304, 5683, 5920, 6103 and the theorem hypotheses 87:4567, 4975, 5362, 5382, 5722, 5736, 5941, 5954, 6121 (replaced by
  η > 0); the persistence lemmas 87:4516-4548 and 87:4876-4950 use (1 − ϑ)⁻¹ rates and (1 − ϑ)Ã > 0, which need only
  ϑ < 1, and |H| ≤ 1/8 (87:4521, 4881), which 𝔰 < 𝔰₁^v ≤ 𝔰₀/2 ≤ 1/16 keeps. With two numbers the rates of (iii) of
  87:4932 become A/(1 − ϑ₁) + Ã and A′/(1 − ϑ₂), the remainder (1 − ϑ₁)Ã(e_o + κ′e_i); this is what P:97-99 says.
  No use is missed.
- **The claim that the cap cannot be removed in this proof (Comparison item 1, deduced).** Correct as a limit of this
  proof. In a null frame the |D̂_(ê₄)Ψ|² part of dτ₂(𝔟) has coefficient (1/2)(1 − κc)H(dv, dv) + κH(du, dv) (dτ₂ =
  dv + κ du, up to the normalisation of dv), while e_i + κe_o contains |w₊|² only through κe_o ≥ κcΩ̂²|w₊|²
  ([[lem:tl5-hf-densities]], 87:3703-3716). The κH(du, dv) part is harmless; the H(dv, dv) part forces |H(dv, dv)| ≲ ϑ₂κ
  in these units, i.e. the cap ∝ κc. The last clause "which is not small in general" is imprecise (H(dv, dv) is as small
  as |H|; what is missing is a bound better than |H|): nit n3.
- **κ, κ′ (Comparison item 1).** def:tl5-wg-domains (87:2056) fixes κ, κ′ ∈ (0, 1/4] with κ′(v* − 1/2) < u* + 10 and
  κ(u* + 10) < v* − 1/2: quoted exactly. The list of what carries them checks: κ_m in c_*κ_m/2 of 𝔰₁ (87:4452, 5652,
  5912, 6087); 𝔨₂ (87:4318); 𝔨₁ and ∂_γ = ∂_v − κ′∂_u (87:4176); 𝔱_r (87:4698); (1 + c/κ′)^(1/2) in w_t (87:5666);
  lem:tl5-wg-domains (d) (87:2096); 1 − κκ′ (87:3690, 3741). "ϑ ∈ (0, 1/4] in each theorem" (87:4449, 4560, 4967).
- **The rise of the cap (Comparison item 1).** min(ϑ₁X₁, ϑ₂X₂) ≤ max(ϑ₁, ϑ₂) min(X₁, X₂), with equality at ϑ₁ = ϑ₂.
  So the rise is the factor max(ϑ₁, ϑ₂)/ϑ = (1 − η − 𝔯^v)/ϑ at most, strictly below 1/ϑ = 100 at the evaluation's
  ϑ = 10⁻² (G0g line 23: κ = κ′ = ϑ = 10⁻²). "(1 − η)/ϑ = up to 100" is a bound but not the factor, and hides that the
  split itself adds nothing to the cap at a given η (its use is the rates): nit n2.

### 2.2 thm:tl5-hfv

4A_vB_v = 4(η^(−1/2)δ_w + η⁻¹(ε^v + ε_M^v))η⁻¹(S_F^v + S_M^v) = 4η^(−3/2)(δ_w + η^(−1/2)(ε^v + ε_M^v))(S_F^v + S_M^v):
the powers are right. At η = 1/2: 4 · 2√2 (δ_w + √2 ε)S = 8(√2 δ_w + 2ε)S, the old condition. N ≥ 6: ε_M^v = S_M^v = 0
(87:5674), the form 4η^(−3/2)(δ_w + η^(−1/2)ε_(w,t))S_(F,s) < 1. N = 4: 4η^(−3/2)(δ_w + η^(−1/2)(ε_(w,q) + ε_(M,q)))
(S_(F,s) + S_(M,q)) < 1, matching B_q = 2(S_(F,s) + S_(M,q)) and A_q (87:6097) at η = 1/2. Step 1 uses only
𝔰_*^v < 𝔰₁^v with A_v in 𝔰_*^v; the continuity argument from Y ≤ A_v + B_vY² and 4A_vB_v < 1 is the old one. Correct.

### 2.3 𝔣₂ by families (lem:tl5-hfv-conv)

The lemma is correct as a bound: 2Ω̂²𝒥_g² ≤ Ae_o + e_i ([[eq:tl5-hf-coercive]]), (√e_o + √c√e_i)² ≤ (1/A + c)(Ae_o + e_i),
and (1/A + c)^(1/2)A = (A(1 + cA))^(1/2). 200,000 random points (c ∈ (0, 1/2), z̲ ∈ [10⁻², 10^1.5]) gave no violation.
But it is **not** a sharpening everywhere: (𝔣₂^o)² − 𝔣₂² = 2Ω̂²(cA² − A − 2) = 2Ω̂²(c/z̲² + 1/z̲ − 2), using cA = 1 + c/z̲.
So 𝔣₂^o > 𝔣₂ wherever c/z̲² + 1/z̲ > 2, for instance c = 0.4, z̲ = 0.1: 𝔣₂^o = 12.25Ω̂ against 𝔣₂ = 7.35Ω̂ (0.22 decades
worse); in the random sample half the points. 𝔣₂^i < 𝔣₂ always (1/A + c ≤ 2c < 1 as c < 1/2, 87:3627). Finding m1.

### 2.4 𝔨_B = max(𝔷, 𝔤₁)

|H| ≤ |g⁻¹||h||ĝ⁻¹| with |g⁻¹| ≤ 1 + |H| and |H| ≤ 𝔰 ≤ 𝔰_♭/2, so 1 + |H| ≤ 1 + 2𝔰_♭ = 𝔤₁ (87:5447) ≤ 5/4 < 2. Correct, and
𝔨_B never grows.

### 2.5 The level-4 recovery 𝔨_rec (lem:tl5-hfv-rec)

The √7 counts the seven fields once ((Σ_Z 𝔷_Z²)^(1/2) ≤ √7(𝔷₁|D̂h| + 𝔷₂|h|), and (Σ_Z |D̂Ψ_Z|²)^(1/2) ≤ √7 times the
largest), against (2𝔐^(0))^(1/2) = 4 with 𝔐^(0) = 1 + 7 (87, eq:tl5-hfg-cinf). μ² |D̂h| ≤ μ^(1/2) times the bound of
μ²|D̂Ψ_Z| and μ²|h| ≤ μ(C_Sℰ^(1/2) + C_(0,0)η₀) put μ^(1/2) and μ on the lower jets; |h| has no ϱ part, so 𝔨_rec^ϱ has no
𝔷₂ term. With M = max(C_S, C₁) and μ ≤ 1, 𝔨_rec ≤ (6/5)((√3 + 8/3)K_rec√7 M(1 + μ^(1/2)(𝔷₁ + 𝔷₂)) + μ𝔯₀M) ≤
4k₁^(0,μ)M (k₁^(j,μ) at 87:5469), and likewise 𝔨_rec^ϱ ≤ 4k₁^(0,μ)C_(1,ϱ), 𝔨_rec^0 ≤ 4k₁^(0,μ)max(C_(0,0), C_(1,0)); so
C_P^v ≤ C_P^♮, C_(P,ϱ)^v ≤ C_(P,ϱ)^♮, C_(P,0)^v ≤ C_(P,0)^♮ (87:5648, eq:tl5-hfg-cinf). The Comparison formula of the old
4k₁^(0,μ) is right. Correct.

### 2.6 Every earlier closing condition stays valid

Yes: nothing earlier is edited except the appended sentence of rem:tl5-hfq-what. But the section is meant to contain the
earlier theorems: with ϑ₁ = ϑ₂ = ϑ, the old hypotheses should imply those of thm:tl5-hfv (𝔰_(θ,v) ≥ 𝔰_θ, η ≥ 1/2,
A_v ≤ √2δ + 2ε, and every constant with index v at most the old one). That holds for 𝔰_(θ,v), 𝔨_B, C_P^v, C_(P,ϱ)^v,
C_(P,0)^v and 𝔣₂^i, but fails for 𝔣₂^o where c/z̲² + 1/z̲ > 2. With m1's fix every constant with index v is at most the
old one, and thm:tl5-hfv contains the earlier theorems.

## 3. Findings

### Major

None.

### minor

**m1. lem:tl5-hfv-conv: 𝔣₂^o exceeds the old 𝔣₂ where c/z̲² + 1/z̲ > 2 (P:36-44, Comparison P:149-150 and item 5,
P:181).** Why: (𝔣₂^o)² − 𝔣₂² = 2Ω̂²(c/z̲² + 1/z̲ − 2) (§2.3). There the "sharpened" constants 𝔞_(o,s), 𝔟_(o,s) are larger,
so S_F^v, ε^v and 𝔯^v may be larger than the old ones; the section's claim to sharpen, Comparison item 5 ("proved") and
the inclusion of the earlier theorems (§2.6) fail there. z, z̲ are free positive functions (87:3696), so this is not
excluded by the setting. Fix: take the split pair only where it is not worse, and the old pair elsewhere (both bounds
are proved, the old one at 87:5330); then 𝔣₂^o, 𝔣₂^i ≤ 𝔣₂ everywhere. A min of the o-coefficients alone is not a valid
bound (c = 0.4, z̲ = 0.1, e_o = 1, e_i = 9, 2Ω̂²𝒥_g² = Ae_o + e_i: 19.0Ω̂ against 𝔣₂ + 9𝔣₂^i = 16.2Ω̂), so the choice is of
the pair, pointwise. Replacements:

Old (P:36-44):

    **Lemma {#lem:tl5-hfv-conv}** (The conversion into the densities, by families.) Let A := 1/z̲ + 1/c and

        𝔣₂^o := √2 Ω̂ (A (1 + cA))^(1/2),      𝔣₂^i := √2 Ω̂ (1/A + c)^(1/2).

    Then for every family of fields as in [[prop:tl5-hf-linear-n]], with 𝒥_g and the weighted sums e_o, e_i of it,
    2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂^o e_o + 𝔣₂^i e_i.

    *Proof.* By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ A e_o + e_i, and by the Cauchy–Schwarz inequality √e_o + √c √e_i ≤ (1/A +
    c)^(1/2) (A e_o + e_i)^(1/2); so 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ √2 Ω̂ (1/A + c)^(1/2) (A e_o + e_i), which is the claim. ∎

New:

    **Lemma {#lem:tl5-hfv-conv}** (The conversion into the densities, by families.) Let A := 1/z̲ + 1/c and 𝔣₂ be as in
    [[def:tl5-hfs-constants]]; at the points where c/z̲² + 1/z̲ ≤ 2 put

        𝔣₂^o := √2 Ω̂ (A (1 + cA))^(1/2),      𝔣₂^i := √2 Ω̂ (1/A + c)^(1/2),

    and at the other points 𝔣₂^o := 𝔣₂^i := 𝔣₂. Then 𝔣₂^o ≤ 𝔣₂ and 𝔣₂^i ≤ 𝔣₂ everywhere, and for every family of fields as
    in [[prop:tl5-hf-linear-n]], with 𝒥_g and the weighted sums e_o, e_i of it, 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂^o e_o +
    𝔣₂^i e_i.

    *Proof.* By [[eq:tl5-hf-coercive]], 2Ω̂² 𝒥_g² ≤ A e_o + e_i, and by the Cauchy–Schwarz inequality √e_o + √c √e_i ≤ (1/A +
    c)^(1/2) (A e_o + e_i)^(1/2); so 2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ √2 Ω̂ (1/A + c)^(1/2) (A e_o + e_i), which is the claim at
    the points where c/z̲² + 1/z̲ ≤ 2. There A(1 + cA) − 2(1 + A) = A(cA − 1) − 2 = c/z̲² + 1/z̲ − 2 ≤ 0, as cA = 1 + c/z̲,
    so 𝔣₂^o ≤ 𝔣₂; and 1/A + c ≤ 2c < 1, as 1/A < c < 1/2, so 𝔣₂^i < 𝔣₂. At the other points the claim is the bound
    2Ω̂² 𝒥_g (√e_o + √c √e_i) ≤ 𝔣₂ (e_o + e_i) of Step 2 of the proof of [[prop:tl5-hfg-bootstrap]]. ∎

Old (Comparison, P:149-150):

        A = 1/z̲ + 1/c,  𝔣₂^o = √2 Ω̂ (A(1 + cA))^(1/2) (in 𝔞_o, 𝔟_o),  𝔣₂^i = √2 Ω̂ (1/A + c)^(1/2) (in 𝔞_i, 𝔟_i),
            against 𝔣₂ = 2Ω̂ (1 + A)^(1/2) in both;

New:

        A = 1/z̲ + 1/c,  𝔣₂^o = √2 Ω̂ (A(1 + cA))^(1/2) (in 𝔞_o, 𝔟_o),  𝔣₂^i = √2 Ω̂ (1/A + c)^(1/2) (in 𝔞_i, 𝔟_i)
            where c/z̲² + 1/z̲ ≤ 2, and 𝔣₂^o = 𝔣₂^i = 𝔣₂ elsewhere, against 𝔣₂ = 2Ω̂ (1 + A)^(1/2) in both; both ≤ 𝔣₂,
            𝔣₂^i ≤ (c/(1 + A))^(1/2) 𝔣₂ where split, and 𝔣₂^o < 𝔣₂ only where c/z̲² + 1/z̲ < 2 (z̲ ≥ 1 suffices);

Old (Comparison item 5, P:181):

    5. 𝔣₂ (proved: 𝔣₂^o, 𝔣₂^i), 𝔨_B (proved: 𝔤₁ in place of 2), the factor 8√2 (proved: η); 𝔠^♮₄(μ) against 9·2⁴ not done.

New:

    5. 𝔣₂ (proved: 𝔣₂^o, 𝔣₂^i, never above 𝔣₂; the gain on the faces Σ₁ needs c/z̲² + 1/z̲ < 2), 𝔨_B (proved: 𝔤₁ in place
       of 2), the factor 8√2 (proved: η); 𝔠^♮₄(μ) against 9·2⁴ not done.

(𝔣₂^i/𝔣₂ = ((1/A + c)/(2(1 + A)))^(1/2) ≤ (c/(1 + A))^(1/2); z̲ ≥ 1 gives c/z̲² + 1/z̲ ≤ c + 1 < 3/2.) The theorem's proof
(P:91-92) and the definition (P:69-70) need no change: they use 𝔣₂^o and 𝔣₂^i as the lemma defines them. The lemma
grows by five lines; the crosswalk numbers of the later labels move accordingly (fixed copy).

### nits

**n1. Placement item 1 (P:119).** After item 2 replaces two lines by three, the last line of rem:tl5-hfq-what is 6141.
Old: "(line 6140, as changed by item 2)". New: "(line 6141 once item 2 is applied)".

**n2. Comparison item 1, the rise of the cap (P:166-167).** See §2.1. Replacement under n3 (same lines).

**n3. Comparison item 1, H(dv, dv) (P:168-169).** "which is not small in general" says the wrong thing (it is as small
as |H|). Old (P:166-169):

       and ϑ₂ (faces Σ₂, cap ∝ κc/(1 + κc)), each free in (0, 1), and the closing is written with η, so the cap rises by up
       to (1 − η)/ϑ = up to 100 against ϑ = 10⁻² at the price of η and of the rates. Not removable in this proof (deduced):
       on Σ₂ the 𝔟-flux contains |D̂_(ê₄)Ψ|² with a coefficient of size |H|, and the face density e_i + κe_o controls it only
       with the weight κc; a sharper cap would need the component H(dv, dv), which is not small in general. What carries κ,

New:

       and ϑ₂ (faces Σ₂, cap ∝ κc/(1 + κc)), each free in (0, 1), and the closing is written with η, so the cap rises by
       the factor max(ϑ₁, ϑ₂)/ϑ at most, that is (1 − η − 𝔯^v)/ϑ, below 100 against ϑ = 10⁻², at the price of η and of the
       rates; the factor is attained at ϑ₁ = ϑ₂, so the split itself adds nothing to the cap at a given η and serves the
       rates. Not removable in this proof (deduced): on Σ₂ the 𝔟-flux contains |D̂_(ê₄)Ψ|² with a coefficient of size |H|,
       and the face density e_i + κe_o controls it only with the weight κc; a sharper cap would need a separate bound of the
       component H(dv, dv), on which the bootstrap gives nothing better than |H|. What carries κ,

**n4. Comparison item 4 (P:180).** G0g (its levers list, item 4) gives 0.7, 1.3, 0.0 and 0.3 decades in f as an upper
bound by dropping the 7², and 0.6, 0.6, 0.0 and 0.3 by the moved-√7 model of G0f; "≤ 0.6 by G0g's model" reports only
the second. Old: "4. The word count 7² in S_F (not done; worth ≤ 0.6 decades in f by G0g's model)." New:

    4. The word count 7² in S_F (not done; worth at most 0.7, 1.3, 0.0 and 0.3 decades in f as an upper bound by dropping
       it, and 0.6, 0.6, 0.0 and 0.3 by the moved-√7 model, both in G0g).

**n5. rem:tl5-hfv-what (P:103), chapter text.** "remove the factor 8√2 up to 4" is unclear; as η → 1 the closing
tends to 4(δ_w + ε^v + ε_M^v)(S_F^v + S_M^v), so the coefficients 8√2 of δ_w and 16 of ε^v + ε_M^v both fall towards 4.
Old (P:102-107, from "[[eq:tl5-hfv-closing]] is the form"):

    [[eq:tl5-hfv-closing]] is the form 8(√2 δ_w + 2(ε^v + ε_M^v))(S_F^v + S_M^v) < 1 of the earlier theorems; smaller ϑ₁,
    ϑ₂ and 𝔯^v let η approach 1 and remove the factor 8√2 up to 4, and larger ϑ₁, ϑ₂ raise the cap 𝔰_(θ,v) at the cost of η
    and of larger rates a_o = â_o/(1 − ϑ₁), a_i = â_i/(1 − ϑ₂). The cap on the faces Σ₂ carries κc/(1 + κc), as the density
    e_i + κ e_o of these faces controls the derivative along ê₄ only through κ e_o; the numbers κ, κ′ of
    [[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the hypotheses of
    [[thm:tl5-hfv]] are established in this paper for no background at 10 l5.

New:

    [[eq:tl5-hfv-closing]] is the form 8(√2 δ_w + 2(ε^v + ε_M^v))(S_F^v + S_M^v) < 1 of the earlier theorems; smaller ϑ₁,
    ϑ₂ and 𝔯^v let η approach 1 and lower the factors 8√2 of δ_w and 16 of ε^v + ε_M^v towards 4, and larger ϑ₁, ϑ₂ raise
    the cap 𝔰_(θ,v) at the cost of η and of larger rates a_o = â_o/(1 − ϑ₁), a_i = â_i/(1 − ϑ₂). The cap on the faces Σ₂
    carries κc/(1 + κc), as the density e_i + κ e_o of these faces controls the derivative along ê₄ only through κ e_o; the
    numbers κ, κ′ of [[def:tl5-wg-domains]] are those of the setting. As for [[thm:tl5-hf]] and [[thm:tl5-hf4]], the
    hypotheses of [[thm:tl5-hfv]] are established in this paper for no background at 10 l5.

**n6. Introduction (P:5), chapter text.** η is defined twice, here as "η := 1 − max(ϑ₁, ϑ₂) − 𝔯" and in
[[eq:tl5-hfv-constants]] with 𝔯^v. Write "=" and 𝔯^v here; the paragraph is rewrapped in the same nine lines. Old (P:5-11):

    numbers ϑ₁, ϑ₂ ∈ (0, 1), one for each family of faces, and the bootstrap is closed with η := 1 − max(ϑ₁, ϑ₂) − 𝔯 in place
    of the bounds ϑ ≤ 1/4 and 𝔯 ≤ 1/4; this frees the cap 𝔰_θ of the smallness condition and the factor 8√2 of the closing
    condition ([[lem:tl5-hfv-close]]). Second, the conversion of the high factor into the densities is made separately for
    the two families of faces ([[lem:tl5-hfv-conv]]). Third, |H| ≤ 𝔤₁ |h| replaces |H| ≤ 2|h| in the constant 𝔨_B. Fourth, at
    level four the recovery of D̂²h at a point is bounded term by term ([[lem:tl5-hfv-rec]]). The closing conditions are
    [[eq:tl5-hfv-closing]]; the earlier ones remain valid. Throughout, the notation is that of [[sec:tl5-hfs]],
    [[sec:tl5-hft]] and [[sec:tl5-hfq]].

New:

    numbers ϑ₁, ϑ₂ ∈ (0, 1), one for each family of faces, and the bootstrap is closed with η = 1 − max(ϑ₁, ϑ₂) − 𝔯^v in
    place of the bounds ϑ ≤ 1/4 and 𝔯 ≤ 1/4; this frees the cap 𝔰_θ of the smallness condition and the factor 8√2 of the
    closing condition ([[lem:tl5-hfv-close]]). Second, the conversion of the high factor into the densities is made
    separately for the two families of faces ([[lem:tl5-hfv-conv]]). Third, |H| ≤ 𝔤₁ |h| replaces |H| ≤ 2|h| in the constant
    𝔨_B. Fourth, at level four the recovery of D̂²h at a point is bounded term by term ([[lem:tl5-hfv-rec]]). The closing
    conditions are [[eq:tl5-hfv-closing]]; the earlier ones remain valid. Throughout, the notation is that of
    [[sec:tl5-hfs]], [[sec:tl5-hft]] and [[sec:tl5-hfq]].

Crosswalk rows in the fixed copy (only the line numbers change): lem:tl5-hfv-rec 51, def:tl5-hfv-constants 71,
eq:tl5-hfv-constants 81, thm:tl5-hfv 83, eq:tl5-hfv-closing 88, rem:tl5-hfv-what 106; the first five rows are unchanged.

## 4. Checked and correct, no change

lem:tl5-hfv-close in full; [[eq:tl5-hfv-dphi]]; the theorem's proof, including the persistence clause; the definition's
list of replacements (𝔰_θ only enters 𝔰₁, 𝔣₂ only 𝔞_(·,s), 𝔟_(·,s), 𝔨_B only 𝔎, 𝔎_ϱ, 𝔎₀); 𝔨_B; lem:tl5-hfv-rec and its
three constants; the closing condition at η = 1/2 and in both level forms; the Placement quotation of 87:6139-6140 and
its commit statements; Comparison lines 141-159 other than the 𝔣₂ line, items 2 and 3.

## 5. Verdict

One minor finding (m1) is open in the file as submitted; with the eight replacements above, all tested in the fixed copy
(lint 0 hits, assemble --check 0 problems, in-memory `[] 0`, crosswalk 388 = 388), nothing else is open.

Verdict: NOT CONFIRMED
