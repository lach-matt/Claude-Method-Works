# R-P-GRD11: an independent review of proofs/P-GRD11.md (sec:tl5-hfu)

Reviewed: research/warp-drive/paper/reader/proofs/P-GRD11.md at b9d0f611. md5 975cc2072424a0863437a708a61d2e84,
322 lines. The chapter text is P:1–192, with 11 labels. The placement is P:194–215, the Comparison P:217–306 and the
crosswalk rows P:308–322. The writer's report is notes/reports/P-GRD11.md.

Base: chapters/87-ten-l5.md at HEAD, unchanged since 89765a14. It has 6883 lines and 5,281 labels, and sec:tl5-hfp is
Section 57.25. The citations below are P:n for the proof file and 87:n for the chapter.

Verdict: **CONFIRMED**. There is no Major and no minor finding. One nit is in the Comparison, which is not chapter
text: a range is understated at the 10⁻⁶ point. A tested fixed copy is provided, and its chapter text is
byte-identical to the original.

## 1. Mechanics (scratch tree from `git archive HEAD`, the writer's placement)

- **Item 2.** The old two lines were found exactly at 87:6882–6883. The new third line is the pointer sentence, 102
  characters long, as the placement says. Because item 2 adds one line, "line 6884, as changed by item 2" in item 1 is
  right. The section is inserted after it with one blank line, as a sibling "###" section, and the chapter grows to
  7077 lines.
- **lint.py --chapters:** 62 files, 5292 labels defined (5281 + 11), 0 hits.
- **assemble.py --check:** labels 5292, computations cited 0, problems 0.
- **In-memory check:** `[] 0`. Plain `python3 assemble.py` was not run.
- **Crosswalk:** all 11 rows give the line of their own label. Chapter labels 441 = crosswalk rows + new labels 441.
  All new labels are lowercase. Of the 5281 existing printed numbers, none changes.
- **Format:** the longest chapter-text line is 120 characters. No wrapped chapter-text line starts with a forbidden
  marker. The only START flags are the Comparison's bullet lines P:301–305, which are notes and not wrapped
  chapter-text lines. There are no file names, no program names, no code and no AI language in P:1–192.
- **Crosswalk descriptions:** each row's description matches its label (P:312–322). No amendment note is needed,
  and none is given.

## 2. The claims

### lem:tl5-hfu-face (P:18, eq:tl5-hfu-face P:28)

- **The first inequality (the weights).** The points γ_ω(v) fill one leaf, and eq:tl5-hfp-leaf is applied on that
  leaf with 𝔶₂ := 1.
  - The pointwise comparison |ℒ^J A|₀ ≤ 𝔳₀^r|ℒ^J A| is used, and e^(−φ) is constant on the leaf.
  - With dω dv = R⁻³ dμ dτ₂/(1 − κκ′), the supremum of 𝔳₀^(2r)R⁻³ over Σ ⊂ Σ₁(t, v*) is at most 𝔵_r(t).
  - This is the step of lem:tl5-hf4-face (b), in the form of lem:tl5-hft-face (c), with C_(E,r)(𝔶) of
    lem:tl5-hfp-leaf in place of the unweighted constant. The weights act only through that leaf inequality. ✓
- **The second inequality (the coefficients kept apart).** |ℒ_(∂_γ)A| ≤ |∂_γ||D̂A| + r|D̂∂_γ||A|. Squaring with
  (x + y)² ≤ 2x² + 2y² gives |A|₀² + |ℒ_(∂_γ)A|₀² ≤ 𝔳₀^(2r)((1 + 2r²|D̂∂_γ|²)|A|² + 2|∂_γ|²|D̂A|²).
  - Each coefficient, multiplied by 𝔳₀^(2r)R⁻³, is bounded by its own supremum: 𝔱_(r,0) and 𝔱_(r,1).
  - Both are at most 𝔱_r, which is the larger of the two, so the old bound (a) follows.
  - At r = 3 the coefficients are 1 + 18|D̂∂_γ|² and 2|∂_γ|², as the Comparison states at P:235. ✓

### lem:tl5-hfu-fam (P:40, eq:tl5-hfu-fam P:55), for all N ≥ 4

Checked step by step against the proof at P:63–76.

- **Hypothesis.** Each C ∈ 𝔙 carries a number with 𝔬_C² ≤ μ^(|C|+1). That is what makes every weight below
  admissible.
- **Leading term, counted once.** lem:tl5-hfz-rec with 𝔥 = 𝔰₁^v applies at each point, since |H| ≤ 𝔰 ≤ 𝔰₁^v. Its
  leading term runs over the words ZC, Z ∈ Γ. These are distinct over Z and C, because a word determines its first
  letter and the word of its remaining letters. Also 𝔬_C² ≤ μ^(|ZC|). So Minkowski's inequality and the definition
  of 𝒥_g give k₁^D 𝒥_g, with no factor of n. ✓
- **The terms with 𝔷_Z and 𝔯_♯.** The C are distinct and 𝔬_C² ≤ μ·μ^(|C|), so these terms give
  μ^(1/2)(k₁^D𝔷′ + (1 − 𝔰₁^v)⁻¹𝔯_♯)𝒥_g ✓. The bound (Σ_Z 𝔷_Z²)^(1/2) ≤ 𝔷′(…)^(1/2) is the one from
  lem:tl5-hfp-abs (b).
- **The couplings.** These are bounded by (1 − 𝔰₁^v)⁻¹𝔞_𝔄(𝔙)𝒥_g, using the operator norm and
  Σ_K μ^|K|(|D̂Ψ_K|² + |Ψ_K|²) ≤ 𝒥_g² ✓.
- **The nonlinear part, per word.** (1 − 𝔰₁^v)⁻¹|𝔑′_C| ≤ 𝔵^z(2μ^(−(|C|+1)/2)𝒥_g + 𝔐_C), and
  𝔐_C ≤ μ^(−(|C|+1)/2)(k₁ + 2𝔵)𝒥_g/(1 − 𝔵) + w_C k₂ ϱ/(1 − 𝔵). The second inequality holds because the weights of
  lem:tl5-hfp-abs (b) do not decrease with length and 𝒟_g ≤ 𝒥_g.
  - Multiplying by 𝔬_C, with 𝔬_Cμ^(−(|C|+1)/2) ≤ 1, gives 𝔵(2(1 − 𝔵) + k₁ + 2𝔵)/(1 − 𝔵) = 𝔵(k₁ + 2)/(1 − 𝔵) ✓.
  - The Euclidean norm of this constant over n words is n^(1/2) times it ✓. This is the only place n enters
    besides 𝔞_𝔄.
- **The parts with ϱ.** The parts 𝔬_C k₂ϱ and 𝔬_C𝔵w_C k₂ϱ/(1 − 𝔵) add to at most 𝔬_C w_C k₂ϱ/(1 − 𝔵), since
  w_C ≥ 1. That gives the second term of eq:tl5-hfu-fam ✓.
- **The bound 𝔞_𝔄(𝔙) ≤ (n/2)^(1/2)α_𝔄.** Each row sum is Σ_K 𝔬_Cμ^(−|K|/2)‖𝔄_CK‖ ≤ Σ_K μ^((|C|+1−|K|)/2)‖𝔄_CK‖
  ≤ 2^(−1/2)α_𝔄. Each of the n components is therefore at most that times the norm of the family ✓.
- **The bound on 𝔩(𝔙).** With k₁^(j,μ,p) = k₁^D + μ^(1/2)(…) + (1 − 𝔰₁^v)⁻¹α_𝔄 and n ≥ 1,
  𝔩(𝔙) ≤ n^(1/2)(k₁ + 𝔵(k₁ + 2)/(1 − 𝔵)) = n^(1/2)(k₁ + 2𝔵)/(1 − 𝔵) ✓.
- **Level.** No step uses the level, so the lemma holds for all N ≥ 4.

### Distinctness behind each family

- **The words JB of X₁** (43 J × 49 B). These are distinct because the B have one length, |B| = 2. The map B ↦ σB
  is injective, as in lem:tl5-hfq-mixed (87:6076).
- **𝔙₂.** These are the 49 words of length two, distinct by definition, with 𝔬² = μ³ = μ^(|C|+1).
- **𝔙_Γ.** These are the 301 = 43 × 7 words JZ, with Z ∈ Γ a single letter. They are distinct because Z has one
  length, so JZ determines J and Z. The weight is 𝔬² = 𝔶_(|J|)μ⁴ ≤ μ^(|J|+2) = μ^(|JZ|+1), using 𝔶_k ≤ μ^(k−2).
  The map Z ↦ σZ is injective in the remainders R, as in lem:tl5-hfq-mixed (87:6078).
- **The words ZC of the leading term.** These are distinct, as in the lemma's proof.
- **The 49 and 343 words of the 𝔜″ terms.** These are the words of lengths two and three, each counted once. ✓

### Weights allowed in each mixed-term use (lem:tl5-hfu-mixed, P:100)

Every use was checked against the step's weight.

- **X₁:** 𝔶μ⁴ ≤ μ^(|JB|). For the remainder R′, 𝔶^(1/2)μ² ≤ μ^(a/2)μ^(|σB|/2).
- **X₂:** 𝔶μ⁴ ≤ μ^(|JZ|+1). For R, 𝔶^(1/2)μ² ≤ μ^(1/2)μ^(a/2)μ^(|σZ|/2).
- **Y₁:** μ³ = μ·μ^(|B|). In 𝔙₂ the weight 𝔬² = μ³ ≤ μ^(|C|+1).
- **Y₂:** μ³ = μ^(|B|), so no gain is available there. P:304 says so.

All the weights are allowed. The sums follow:

- Σ_(J,Z) 𝔶μ⁴ν^(−(|J|+2)) = 301(μ/ν)⁴𝔗² ✓, with 𝔗² = (ν²𝔶₀ + 6ν𝔶₁ + 36)/43.
- Σ 𝔬²w² = 49(μ/ν)³ ✓, which gives the factor 7(μ/ν)^(3/2) of 𝔜′₁.
- 98π² = 49·2π² and 686π² = 343·2π² ✓. These give μ^(3/2)π(98[𝔳₀⁶]_t)^(1/2) and μ^(3/2)π(686[𝔳₀⁴]_t)^(1/2).

### def:tl5-hfu-constants (P:78–98) and thm:tl5-hfu (P:146, eq:tl5-hfu-closing P:157)

- **The constants.** S_M^u, 𝔯_M^u and ε_M^u are S_(M,q), 𝔯_(M,q) and ε_(M,q) of eq:tl5-hfq-constants
  (87:6093–6096), formed with items 1–6. The pairing is the same, term by term:
  - 𝔛₁𝔜₁ and 𝔛₂𝔜₂ in S;
  - 𝔛₁𝔜′₁ϱ, 𝔛₁𝔜″₁η₀, 𝔛₂𝔜″₂η₀ and 𝔛′₂𝔜₂ϱ in 𝔯;
  - 𝔛′₂𝔜″₂ in ε.
- **The closing condition.** 4η_u^(−3/2)(δ_w + η_u^(−1/2)(ε^z + ε_M^u))(S_F^p + S_M^u) < 1, with
  𝔯^u = 𝔯^p − 𝔯_M^p + 𝔯_M^u, is eq:tl5-hfp-closing with exactly these replacements. The condition 𝔰_*^u < 𝔰₁^v is
  𝔰_*^p with A_u. ✓

### Containment of thm:tl5-hfp at N = 4 for 𝔶₀, 𝔶₁ ≥ 1, and the earlier closings

- **Each new factor is at most the old one.**
  - 𝔛₁: the factor is q₃ times (1 + ϖ^(1/2))/(2(1 + ϖ))^(1/2), which is at most 1.
  - 𝔜₁: 𝔩(𝔙₂) ≤ 7λ^(μ,2), and the old factor is 1 + 7λ^(μ,2).
  - 𝔛₂: 𝔩(𝔙_Γ) ≤ √301λ^μ ≤ √602λ^μ, and μ^(1/2)ϖ^(1/2) ≤ (2ϖ)^(1/2).
  - 𝔛′₂: √301 𝔗(μ/ν)² ≤ √301 ≤ √602, since (μ/ν)⁴𝔗² ≤ 1.
  - 𝔜′₁: (μ/ν)^(3/2) ≤ 1, and 𝔱_(3,1) ≤ 𝔱₃.
  - 𝔜″: μ^(3/2) ≤ 1.
  - The weighted leaf constant C_(E,r)(𝔶) ≤ C_(E,r)^♯ holds when 𝔶₀, 𝔶₁ ≥ 1 (lem:tl5-hfp-leaf).
  - For 𝔛₁ this uses (1 + x)² ≤ 2(1 + x²).
  - For 𝔜₁ the old bound follows from 𝔜₁ ≤ 𝔱₃^(1/2)(μ + 𝔩(𝔙₂)²)^(1/2) ≤ 𝔱₃^(1/2)(1 + 7λ^(μ,2)).
- **Consequences.** Hence S_M^u ≤ S_M^p, 𝔯_M^u ≤ 𝔯_M^p and ε_M^u ≤ ε_M^p. That gives η_u ≥ η_p, A_u ≤ A_p and
  B_u ≤ B_p. Then 𝔰_*^u ≤ 𝔰_*^p, so the hypotheses of thm:tl5-hfp imply those of thm:tl5-hfu. ✓
- **Earlier closings.** N ≥ 6 is untouched, since S_M = 𝔯_M = ε_M = 0 there. At N = 4 every earlier theorem is
  unchanged. The new section adds a theorem and edits none, so every earlier closing condition stays valid. ✓

## 3. The Comparison section

- **Items 1–8 (P:227–254).** These match the definition and the old constants of lem:tl5-hfq-mixed and
  def:tl5-hfq-constants (87:6070, 87:6093–6096).
- **The q table (P:259–262)** reproduces exactly at 𝔶 = (μ⁻², μ⁻¹). It was computed independently with numpy, with
  j₁ ≤ 40000 and the tail extrapolated in 1/j₁, using the same series as for R-P-GRD10.

  | μ  | 10⁻⁴   | 3×10⁻⁵ | 10⁻⁵   | 3×10⁻⁶ | 10⁻⁶   |
  |----|--------|--------|--------|--------|--------|
  | q₂ | 0.1097 | 0.0812 | 0.0617 | 0.0456 | 0.0347 |
  | q₃ | 0.1216 | 0.0900 | 0.0684 | 0.0506 | 0.0385 |
  | q₄ | 0.1310 | 0.0970 | 0.0737 | 0.0545 | 0.0414 |

  Ranks 2 and 3 agree with G0m line 10.

- **The deduced figures (P:264–282)** were recomputed from the stated assumptions: k₁^D = 2.30, α_𝔄 = 0.06, the
  μ^(1/2) parts 0.01, 0.32, 0, 0, 𝔱_(3,1) = 𝔱₃, and G0m's optima.
  - **𝔜₁.** Recovering k₁^(2,μ,p) from 1 + 7λ^(μ,2) = 17.8, 20.3, 18.0, 19.3 gives 𝔩(𝔙₂) = 2.85, 3.48, 3.09, 4.34 ✓,
    so the decades are −0.80, −0.77, −0.77, −0.65 ✓.
  - **𝔛₂.** From √602λ^μ = 59, 68, 60, 64, 𝔩(𝔙_Γ) = 3.66, 4.76, 4.27, 7.35 ✓, so the decades are −2.3, −2.2, −2.5,
    −2.1 ✓.
  - **𝔛₁.** q₃ in decades is −1.17, −1.05, −1.41, −1.17 ✓, and the triangle factor is 0 to −0.15 ✓.
  - **S_M.** The term with 𝔠^Mq₁ falls by 2.0–2.1, 1.8–2.0, 2.2–2.3 and 1.8–2.0 decades ✓. The term with 𝔠^Mq₂
    falls at least as far ✓. From G0m's 0.22, 0.25, 0.85, 0.48 above S_F (G0m line 163), S_M ends 1.3–1.9 below ✓.
  - **G0m's figures.** The gains +0.31, +0.26, +0.34, +0.14 and "within 0.06" match G0m lines 171 and 194 ✓. The
    lower-bound argument "every term at most the corresponding term of G0m's lever" holds, because the lever's terms
    are the old ones × q, and items 2–6 only lower them further.
  - **𝔯_M η₀ terms.** The extra factor μ^(3/2) is −7.5, −6.8, −9.0, −7.5 decades ✓.
  - **𝔯_M ϱ terms.** One range is understated; see finding N1.
- **"Choices for the evaluation" (P:284–286)** is consistent with the definition. 𝔞_𝔄(𝔙_Γ) is 𝔞_𝔄(Γ) of
  def:tl5-hfp-constants, with the same rows and weights, so 𝔩(𝔙_Γ) is G0m's C₁^Γ k-term ✓.

## 4. The statement "9·2⁴ is G0's comparison count, not a proved one" (P:297–300): correct

- **The bound.** From eq:tl5-hfs-cn, 𝔠^(2♮)_n contains the term with no background letters from H₁^(λσ)D̂_λD̂_σh,
  which is 2⁴ at n = 4. The term 16Σ⁴_n λ̂λ̂β₁β₁, at b = 0 with λ̂^♮₀ := √5, gives 16·5·2⁴ = 1280. Every other term
  is non-negative. So 𝔠^♮₄(μ) + 1 ≥ 16 + 1280 = 1296 = 16·81 = 9·144, for every μ. This is against G0's comparison
  value 9·2⁴ = 144.
- **What reaching 144 would need.** It needs 16 + 16x ≤ 144, that is a bound x ≈ 8 of the bilinear form 2𝔮̂ in place
  of 16λ̂₀² = 80. The chapter does not state such a bound. The writer's account is right.

**Recommended note for the evaluation reports.** G0g (line 136 and item 5 at line 151), G0h (item 3 at line 164),
G0l (line 174) and G0m (line 196) price "𝔠^♮₄(μ) → 9·2⁴" as an available lever.

- Without a new bound of 2𝔮̂, the most reachable is the excess above 1296. Since log₁₀ 9 = 0.954, G0g's 0.98, 1.22,
  1.15, 1.38 decades shrink to at most about 0.03, 0.27, 0.20, 0.43.
- G0l's +0.47, +0.37, +0.02, +0.05 and G0m's +0.19, +0.17, +0.05, +0.06 are therefore upper figures for a target the
  text does not reach. Each should carry "needs a bound of 2𝔮̂ of about 8 in place of 80".
- Proposed note: "9·2⁴ is a comparison count, not a proved target; the terms with b = 0 give 𝔠^♮₄(μ) + 1 ≥ 1296 = 9²·2⁴,
  and below that the lever needs a bound of the form 2𝔮̂ that the chapter does not state."

These are report files, so I made no edit to them.

## 5. Findings

**N1 (nit), Comparison P:275.** "its terms with ϱ fall by about q₃ (μ/ν)^(3/2) (−2.6 to −3.6) and q₄ 2^(−1/2) (μ/ν)²
𝔗 (−2.9 to −3.6)".

- **The values.** At G0m's four optima (μ, θ) = (10⁻⁵, 3/4), (3×10⁻⁵, 11/16), (10⁻⁶, 3/4), (10⁻⁵, 13/16), with μ/ν =
  μ^(1−θ) and (μ/ν)²𝔗 = ((μ/ν)² + 6(μ/ν)³ + 36(μ/ν)⁴)^(1/2)/√43, the two factors are:
  - q₃(μ/ν)^(3/2): −3.04, −3.17, −3.66, −2.57;
  - q₄2^(−1/2)(μ/ν)²𝔗: −3.27, −3.34, −3.81, −2.87.
- **Why it is a nit.** Both upper ends are understated at the 10⁻⁶ point (−3.66 and −3.81 against −3.6). The error is
  conservative: the gain is larger than stated, and nothing in the evaluation's choices depends on it. Listing the
  values per point matches the neighbouring bullets.
- **Replacement**, tested; the second line is a continuation inside the bullet:

      - 𝔯_M: its terms with ϱ fall by about q₃ (μ/ν)^(3/2) (−3.04, −3.17, −3.66, −2.57) and q₄ 2^(−1/2) (μ/ν)² 𝔗 (−3.27,
        −3.34, −3.81, −2.87);

**Fixed copy:** /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd11/P-GRD11.fixed.md

- md5 ea6da21cb9f616f767c7037be7c85219, 323 lines.
- P:1–192 is byte-identical to the original, so the crosswalk line numbers are unchanged.
- Re-merged in a fresh tree (tree2): lint 0 hits with 5292 labels, check 0 problems, `[] 0`, crosswalk 11 of 11 and
  441 = 441, 0 existing numbers changed. Counted in characters, the two new lines are 114 and 23 long. The only lines
  over 121 in either copy are the tab-separated crosswalk rows. P:275 is notes, not chapter text.

## Verdict

**CONFIRMED.** No Major or minor finding is open. One nit (N1) is in the Comparison, and a fixed copy is offered. The
note on 9·2⁴ for the evaluation reports is recommended.
