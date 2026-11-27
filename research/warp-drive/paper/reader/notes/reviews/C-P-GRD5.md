# C-P-GRD5: confirming read of proofs/P-GRD5.md (the constants sharpened a fifth time, sec:tl5-hfv)

**File read:** proofs/P-GRD5.md at c3506861, md5 6ed9c26203ccdc2b2c46ec7eed4fc172, 210 lines:
- chapter text 1–112 (sec:tl5-hfv, 11 labels);
- Placement 114–140;
- Comparison 142–191;
- crosswalk rows 193–210.

**Review being confirmed:** notes/reviews/R-P-GRD5.md (on f49900d7, md5 d8c646ea…): NOT CONFIRMED, 0 Major, 1 minor (m1), 6 nits (n1–n6).

**Also read**, in chapter 87 at c3506861 (md5 7d66a4e7…, 6140 lines):
- def:tl5-hf-frame (87:3625–3627, 0 < c < 1/2);
- def:tl5-hf-current and lem:tl5-hf-densities (87:3696–3716, eq:tl5-hf-coercive);
- Step 2 of prop:tl5-hfg-bootstrap (87:5319–5345, the old conversion at 87:5329–5330);
- def:tl5-hfs-bounds (87:5446, 𝔰_♭ ∈ (0, 1/8]);
- k₁^(j,μ) (87:5468–5470);
- 𝔨_B (87:5594);
- def:tl5-hfs-constants and prop:tl5-hfs-bootstrap (87:5646–5720);
- eq:tl5-hfg-cinf (87:5139–5141);
- notes/reports/G0g.md, for n4.

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd5/.

## Verdict in brief

All seven changes (m1, n1–n6) resolve their findings correctly and completely. None introduces a new error, and nothing outside the findings changed.

**m1:**
- The identity holds, and 𝔣₂^i < 𝔣₂ always.
- The pointwise choice of the pair is a valid bound in the energy estimate, because the conversion is a pointwise inequality, multiplied by a nonnegative factor before it is integrated.
- With the fix, every constant with index v is at most its old counterpart, so at ϑ₁ = ϑ₂ = ϑ the earlier theorems' hypotheses imply those of thm:tl5-hfv.
- The reviewer's counterexample to lowering 𝔣₂^o alone is arithmetically right.

**n5 and n6** agree with thm:tl5-hfv and eq:tl5-hfv-constants.

**Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5221 old labels changes. The 11 crosswalk rows point at their labels.

No replacement is needed.

## What changed between f49900d7 and c3506861

`git diff f49900d7 c3506861 -- proofs/P-GRD5.md` (138 lines with context) has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in c3506861 | Finding |
|---|---|---|
| introduction, rewrapped | 5–11 | n6 |
| lem:tl5-hfv-conv, statement and proof | 36–49 | m1 |
| rem:tl5-hfv-what, rewrapped | 106–112 | n5 |
| Placement item 1 | 124 | n1 |
| Comparison, the 𝔣₂ formula | 154–156 | m1 |
| Comparison item 1 | 172–177 | n2, n3 |
| Comparison item 4 | 188–189 | n4 |
| Comparison item 5 | 190–191 | m1 |
| crosswalk rows from lem:tl5-hfv-rec on | 202–207 | renumbered by +5 |

**The two rewrapped chapter paragraphs**, compared with whitespace normalised:
- The introduction differs from the draft only by "η := 1 − max(ϑ₁, ϑ₂) − 𝔯 in" → "η = 1 − max(ϑ₁, ϑ₂) − 𝔯^v in".
- The remark differs only by "remove the factor 8√2 up to 4" → "lower the factors 8√2 of δ_w and 16 of ε^v + ε_M^v towards 4".

**Nothing else changed.** The same commit adds only notes/reviews/R-P-GRD5.md.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive c3506861 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd5/tree. Chapter 87 and its crosswalk are byte-identical at 87e4d2c5 (the Placement's HEAD) and c3506861, so the quotations are current.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:6139–6140. After the replacement, rem:tl5-hfq-what ends at line **6141**.
- Item 1: chapter-text lines 1–112 were appended there after one blank line.
- Crosswalk: the 11 rows were appended with `@PENDING:` → `@c3506861:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5232 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5232, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5221 old labels changes its printed number.**
- The new labels are numbered as follows:
  - sec:tl5-hfv is Section 57.20;
  - lem:tl5-hfv-close, lem:tl5-hfv-conv and lem:tl5-hfv-rec are Lemmas 57.193–57.195;
  - def:tl5-hfv-constants is Definition 57.196;
  - thm:tl5-hfv is Theorem 57.197;
  - rem:tl5-hfv-what is Remark 57.198;
  - the displays are (57.140)–(57.143).

**Crosswalk:**
- Each of the 11 rows' line holds its `{#label}`: lines 1, 13, 17, 23, 36, 51, 71, 81, 83, 88 and 106.
- Appended, the file has a header and 388 rows, equal in order to the 388 labels of chapter 87.

**Paper rules on the changed chapter lines** (5–11, 36–43, 46–49, 108–112):
- All are at most 120 characters. The longest chapter-text line in the file is 121 (line 88, unchanged).
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Line 9 starts with "𝔨_B.", line 43 with "𝔣₂^i".
- All 11 labels are lowercase.
- There are no file or program names and no code in the chapter text.
- Line 43 ("𝔣₂^i e_i.", 9 characters) is a short source line. That is cosmetic.

## m1 — 𝔣₂ by families (lem:tl5-hfv-conv, lines 36–49; Comparison 154–156 and item 5): RESOLVED

I checked symbolically with sympy and numerically (calc/f2.py).

**The identity.** With A = 1/z̲ + 1/c, (𝔣₂^o)² = 2Ω̂²A(1 + cA) and 𝔣₂² = 4Ω̂²(1 + A) (87:5650). Then:
- cA = 1 + c/z̲, so A(cA − 1) = (1/z̲ + 1/c)(c/z̲) = c/z̲² + 1/z̲;
- hence (𝔣₂^o)² − 𝔣₂² = 2Ω̂²(A(1 + cA) − 2(1 + A)) = 2Ω̂²(A(cA − 1) − 2) = 2Ω̂²(c/z̲² + 1/z̲ − 2).

sympy reduces all three steps to 0. The proof's chain at line 47 is exactly this.

**𝔣₂^i < 𝔣₂ always.**
- 1/A < c, since A > 1/c, and c < 1/2 (87:3627). So 1/A + c < 2c < 1, which gives (𝔣₂^i)² = 2Ω̂²(1/A + c) < 2Ω̂² < 4Ω̂²(1 + A) = 𝔣₂².
- The text states the first two steps; the last is immediate.
- Among 200,000 random points (c ∈ (0, 1/2), z̲ ∈ [10⁻³, 10³]), there is no violation. 𝔣₂^o > 𝔣₂ holds at 47 % of them and never inside the split region.

**The lemma's bound.**
- Cauchy–Schwarz gives √e_o + √c√e_i ≤ (1/A + c)^(1/2)(Ae_o + e_i)^(1/2).
- With 2Ω̂²𝒥_g² ≤ Ae_o + e_i (eq:tl5-hf-coercive), this gives 2Ω̂²𝒥_g(√e_o + √c√e_i) ≤ √2Ω̂(1/A + c)^(1/2)(Ae_o + e_i).
- The two coefficients are √2Ω̂(A(1 + cA))^(1/2) and √2Ω̂(1/A + c)^(1/2), so the split pair is valid at every point.
- The old pair (𝔣₂, 𝔣₂) is valid at every point by 87:5329–5330. The citation, "Step 2 of the proof of prop:tl5-hfg-bootstrap", is right.
- I checked the pointwise choice against the coercive bound at equality for 600,000 random (point, e_o, e_i) triples: no violation.

**The pointwise choice in the energy estimate: valid.**
- The conversion is a pointwise inequality between functions of the point. e_o and e_i are the weighted sums Σ_I μ^|I| e_o[Ψ_I] at that point, with constant weights μ^|I|, and 𝒥_g is formed with the same weights (87:5326–5330).
- In Step 2 it is multiplied by the nonnegative factor μ^(−3/2) 𝔤_(𝒥,s) 𝔓 e^(−φ) and only then integrated (87:5342, 5702–5704).
- Step 3 then uses only 𝔞_(o,·)(x) ≤ sup over the face Σ₁ through x, and likewise 𝔞_(i,·) on Σ₂, in S_(F,s) and 𝔯_(w,s).
- So a choice that changes from point to point keeps the integrated inequality, whatever the weights. It is the same mechanism by which 𝔣₀ and 𝔣₁, both functions of the point, enter already.

**Every constant with index v is at most its old counterpart.**
- **𝔣₂:** 𝔣₂^o ≤ 𝔣₂ and 𝔣₂^i ≤ 𝔣₂ everywhere. In the split region the first holds by the identity and the second always; elsewhere both equal 𝔣₂. All terms of 𝔞 and 𝔟 are nonnegative, so 𝔞_(o/i,v) ≤ 𝔞_(o/i,s) and 𝔟_(o/i,v) ≤ 𝔟_(o/i,s), hence S_F^v ≤ S_(F,s) and 𝔯^v ≤ 𝔯.
- **𝔨_B:** max(𝔷, 𝔤₁) ≤ max(𝔷, 2), since 𝔤₁ = 1 + 2𝔰_♭ ≤ 5/4 (87:5446). So 𝔎, 𝔎_ϱ and 𝔎₀ do not grow.
- **The cap:** with ϑ₁ = ϑ₂ = ϑ, 𝔰_(θ,v) = ϑ(√2 + 1/2)⁻¹ min(inf 1/R₁, inf 1/R₂) = 𝔰_θ (87:4451). So 𝔰₁^v = 𝔰₁.
- **The level-4 constants:** 𝔨_rec ≤ 4k₁^(0,μ) max(C_S, C₁), since √7 ≤ 4, μ ≤ μ^(1/2) and μ𝔯₀ ≤ 4μ^(1/2)𝔯₀, against k₁^(0,μ) of 87:5469. Likewise 𝔨_rec^ϱ ≤ 4k₁^(0,μ) C_(1,ϱ) and 𝔨_rec^0 ≤ 4k₁^(0,μ) max(C_(0,0), C_(1,0)). So C_P^v ≤ C_P^♮, and the same holds for the ϱ and 0 constants.
- **ε:** ε_(w,t) and ε_(w,q) contain no 𝔣₂, 𝔨_B or C_P, so ε^v and ε_M^v are unchanged.

**Containment of the earlier theorems.** Take the old hypotheses (ϑ ≤ 1/4, 𝔯 ≤ 1/4) and set ϑ₁ = ϑ₂ = ϑ.
- η = 1 − ϑ − 𝔯^v ≥ 1/2.
- So A_v ≤ √2δ_w + 2(ε + ε_M), B_v ≤ 2(S_F + S_M) and 4A_vB_v ≤ 4AB < 1.
- 𝔰_*^v ≤ 𝔰_*, 𝔰₁^v = 𝔰₁, and (1 − ϑ)a_o, (1 − ϑ)a_i are admissible for 𝔅_N.
- So the hypotheses of thm:tl5-hfv hold. Before the fix this failed exactly where c/z̲² + 1/z̲ > 2.

**The reviewer's counterexample** to lowering only the o-coefficient: c = 0.4, z̲ = 0.1, e_o = 1, e_i = 9, with equality in the coercive bound.
- A = 12.5 and c/z̲² + 1/z̲ = 50.
- 2Ω̂²𝒥_g(√e_o + √c√e_i) = 19.00Ω̂, against 𝔣₂e_o + 𝔣₂^i e_i = 7.348Ω̂ + 9·0.9798Ω̂ = 16.17Ω̂.
- 𝔣₂^o = 12.247Ω̂ against 𝔣₂ = 7.348Ω̂, which is 0.222 decades.

The arithmetic is right. The counterexample shows that the inference from the coercive bound fails, which is the relevant sense, since the coercive bound is not itself sharp. That remark is in the review, not in the file.

**Comparison 154–156 and item 5:**
- "both ≤ 𝔣₂" is right.
- "𝔣₂^i ≤ (c/(1 + A))^(1/2) 𝔣₂ where split" is right: (𝔣₂^i/𝔣₂)² − c/(1 + A) reduces to −c³z̲/(2(c + z̲)(cz̲ + c + z̲)) < 0.
- "𝔣₂^o < 𝔣₂ only where c/z̲² + 1/z̲ < 2" is right.
- "(z̲ ≥ 1 suffices)" is right: c/z̲² + 1/z̲ ≤ c + 1 < 3/2.
- "never above 𝔣₂" is right.

The definition (lines 74–75) and the theorem's proof (lines 96–97) use 𝔣₂^o and 𝔣₂^i as the lemma now defines them, so they are consistent.

## n1 — the Placement's line reference (line 124): RESOLVED

"(line 6141 once item 2 is applied)": after item 2 the last line of rem:tl5-hfq-what is 87:6141. I checked this on the scratch merge.

## n2, n3 — Comparison item 1 (lines 172–177): RESOLVED

**The rise of the cap.**
- 𝔰_(θ,v) = min(ϑ₁X₁, ϑ₂X₂) ≤ max(ϑ₁, ϑ₂) min(X₁, X₂), with equality at ϑ₁ = ϑ₂. Against 𝔰_θ = ϑ min(X₁, X₂), the rise is at most max(ϑ₁, ϑ₂)/ϑ = (1 − η − 𝔯^v)/ϑ, and that is below 100 at ϑ = 10⁻² because η > 0.
- At a given η and 𝔯^v, max(ϑ₁, ϑ₂) is fixed. So "the split itself adds nothing to the cap at a given η and serves the rates" is exact.

**n3.** "a separate bound of the component H(dv, dv), on which the bootstrap gives nothing better than |H|" replaces the inaccurate "not small in general". It is marked deduced.

## n4 — Comparison item 4 (lines 188–189): RESOLVED

G0g (notes/reports/G0g.md lines 149–150) gives exactly "0.7, 1.3, 0.0 and 0.3" as the upper bound by dropping the 7², and "0.6, 0.6, 0.0 and 0.3" by the moved-√7 model of G0f.

## n5 — the remark's factors (lines 106–112, chapter text): RESOLVED

eq:tl5-hfv-closing is 4A_vB_v = 4η^(−3/2)(δ_w + η^(−1/2)(ε^v + ε_M^v))(S_F^v + S_M^v). So:
- the coefficient of δ_w(S_F^v + S_M^v) is 4η^(−3/2);
- the coefficient of (ε^v + ε_M^v)(S_F^v + S_M^v) is 4η^(−2).

At η = 1/2 these are 4·2^(3/2) = 8√2 and 4·4 = 16, the two coefficients of the old form 8(√2δ_w + 2ε)S. Both decrease as η rises towards 1 and tend to 4. So "lower the factors 8√2 of δ_w and 16 of ε^v + ε_M^v towards 4" is exact, and the first sentence of the remark (η = 1/2 at ϑ₁ = ϑ₂ = 𝔯^v = 1/4) is consistent with it.

## n6 — η defined once (lines 5–11, chapter text): RESOLVED

The introduction now writes "η = 1 − max(ϑ₁, ϑ₂) − 𝔯^v" with "=". This matches the one definition, η := 1 − max(ϑ₁, ϑ₂) − 𝔯^v in eq:tl5-hfv-constants (line 80), and the use η > 0 in thm:tl5-hfv (c).

lem:tl5-hfv-close keeps η as a generic positive number in its last claim, which is how the theorem's proof applies it. The introduction now names 𝔯^v before its definition in def:tl5-hfv-constants; that is acceptable in an overview paragraph.

## Observations (no change required)

- **O1.** 𝔣₂^o is continuous across the curve c/z̲² + 1/z̲ = 2, since it equals 𝔣₂ there; in effect 𝔣₂^o = min(√2Ω̂(A(1 + cA))^(1/2), 𝔣₂). 𝔣₂^i, however, jumps from its split value to 𝔣₂ on leaving the closed set {c/z̲² + 1/z̲ ≤ 2}, so it is lower semicontinuous.
  - The suprema over the faces in S_F^v and 𝔯^v stay finite, since 𝔣₂^i ≤ 𝔣₂, and t ↦ sup is measurable.
  - The estimate uses only the bound by the supremum. So "the functions of p being evaluated at the point of the supremum" (87:5664) is read for 𝔞_(i,v) and 𝔟_(i,v) as the supremum, which need not be attained.
  - Any convex combination of the two valid pairs is also valid, if a continuous choice is ever wanted.
- **O2.** The short source line 43 is cosmetic.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd5/:
- tree/: the merged copy at c3506861;
- orig/: the unmerged archive;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- calc/f2.py: the identity, the bounds, the pointwise choice and the counterexample;
- 87.md: chapter 87 at c3506861;
- grd5.diff: the diff.

Verdict: CONFIRMED
