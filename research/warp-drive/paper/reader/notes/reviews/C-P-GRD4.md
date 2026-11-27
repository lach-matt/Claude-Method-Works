# C-P-GRD4: confirming read of proofs/P-GRD4.md (the constants at level four sharpened a fourth time, sec:tl5-hfq)

**File read:** proofs/P-GRD4.md at a08ce8c0, md5 8f464d0b5a7702cab0486aad721dbf15, 273 lines:
- chapter text 1–161 (sec:tl5-hfq, 14 labels);
- Placement 163–189;
- Comparison 191–251;
- crosswalk rows 253–273.

**Review being confirmed:** notes/reviews/R-P-GRD4.md (on 82aa2785, md5 fa9f162d…): NOT CONFIRMED, 0 Major, 1 minor (m1), 4 nits (n1–n4).

**Also read:**
- in chapter 87 at a08ce8c0 (md5 6fb0d2cf…, 5977 lines):
  - lem:tl5-hf-linfty (87:4306–4345: C_S, C_(0,0), C₁ and C_(1,0));
  - def:tl5-hf-constants (87:4431–4452: 𝔰_θ);
  - lem:tl5-hfg-linfty (87:5132–5170: eq:tl5-hfg-cinf);
  - the notation of sec:tl5-hfs (87:5455–5478: Λ₂^μ, 𝔠^♮_n(ν), k₁^(j,μ));
  - lem:tl5-hfs-linfty (87:5545–5590);
  - lem:tl5-hft-small (87:5850–5890).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd4/.

## Verdict in brief

All five changes resolve their findings correctly and completely. None introduces a new error, and nothing outside the findings changed.

**m1:**
- The factor 2 of |H| ≤ 2|h| is absorbed by the entries 2C_S and 2C_(0,0) in the maxima that define C_(∞,μ) and C_((∞,0),ν).
- The new η₀ argument is right: both inequalities hold for ν ∈ (0, 1], and the second is exactly the definition of Λ₂^ν. It is the ν-analogue of the step the merged chapter already uses at 87:5578–5583.

**Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5207 old labels changes. The 14 crosswalk rows point at their labels.

No replacement is needed.

## What changed between 82aa2785 and a08ce8c0

`git diff 82aa2785 a08ce8c0 -- proofs/P-GRD4.md` has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in a08ce8c0 | Finding |
|---|---|---|
| R1, first part | 65–67 | m1 |
| R1, second part | 72–75 | m1 |
| R2 | 81–83 | n1 |
| R4 | 103–104 | n4 |
| R3 | 109–110 | n2 |
| R5 | 173 | n3 |
| crosswalk rows from lem:tl5-hfq-mixed on | 263–270 | renumbered by +4, +5, +6 |

**Nothing else changed.** The Comparison is byte-identical to the draft's. The same commit also adds notes/reviews/R-P-GRD4.md and an entry in notes/DECISIONS.md; neither is merged text.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive a08ce8c0 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd4/tree. Chapter 87 and its crosswalk are byte-identical at 8e7dd529 (the Placement's HEAD) and a08ce8c0, so the quotations are current.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:5976–5977. After the replacement, rem:tl5-hft-what ends at line **5978**.
- Item 1: chapter-text lines 1–161 were appended there after one blank line.
- Crosswalk: the 14 rows were appended with `@PENDING:` → `@a08ce8c0:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5221 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5221, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5207 old labels changes its printed number.**
- The new labels are numbered as follows:
  - sec:tl5-hfq is Section 57.19;
  - lem:tl5-hfq-m, lem:tl5-hfq-theta and lem:tl5-hfq-mixed are Lemmas 57.186–57.188;
  - def:tl5-hfq-constants is Definition 57.189;
  - prop:tl5-hfq-bootstrap is Proposition 57.190;
  - thm:tl5-hf4q is Theorem 57.191;
  - rem:tl5-hfq-what is Remark 57.192.

**Crosswalk:**
- Each of the 14 rows' line holds its `{#label}`: lines 1, 15, 19, 38, 43, 48, 87, 106, 120, 122, 127, 140, 144 and 153.
- Appended, the file has a header and 377 rows, equal in order to the 377 labels of chapter 87.

**Paper rules on the changed chapter lines** (65–67, 72–75, 81–83, 103–104, 109–110):
- Lengths, in characters: 115, 100, 61, 120, 116, 116, 89, 117, 109, 24, 114, 35, 103 and 48. The longest chapter-text line in the file is 121 (line 144, unchanged).
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Line 75 starts with "Φ = D̂²Ψ_B", line 83 with "μ^(n/2)" and line 109 with "𝔰_θ)".
- All 14 labels are lowercase.
- There are no file or program names and no code in the chapter text.
- Lines 67, 83, 104 and 110 are now short source lines. That is cosmetic; the lint accepts them and the assembled check passes.

## m1 — the proof of eq:tl5-hfq-small (lines 65–78): RESOLVED

### (i) The factor 2 for H

**The new text:** "(for H the factor 2 of |H| ≤ 2|h| is taken up by 2C_S and 2C_(0,0) in the constants)".

**Where the 2C_S and 2C_(0,0) come from:**
- eq:tl5-hfg-cinf (87:5139–5141) defines C_∞^(m) := 2 max(2C_S, C₁^g, …) and C_(∞,0)^(m) := 2 max(2C_(0,0), C_(1,0)^g, …).
- lem:tl5-hfs-linfty (87:5548–5550) forms C_(∞,μ)^(m) and C_((∞,0),μ)^(m) from these by changing only k₁^(m), C₁^g and C_(1,0)^g. So the entries 2C_S and 2C_(0,0) stay.
- eq:tl5-hfq-small takes "the constants of eq:tl5-hfs-linfty for μ and for ν", so C_((∞,0),ν)^(N−4) = 2 max(2C_(0,0), C_(1,0)^♮(ν), …). Comparison line 213 says the same.
- With either Sobolev choice of sec:tl5-hft only the values of C_S and C_(0,0) change, not this structure (87:5843–5848).

**The bound.** With 2𝔈 := C_(∞,μ)^(N−4) ℰ_g^(1/2) and 2ℜ := C_((∞,ϱ),ν)^(N−4) ϱ + C_((∞,0),ν)^(N−4) η₀, as defined at lines 68–69:
- 𝔈 ≥ 2C_S ℰ_g^(1/2) and ℜ ≥ 2C_(0,0) η₀.
- Hence |H| ≤ 2|h| ≤ 2μ^(−1) C_S ℰ_g^(1/2) + 2C_(0,0) η₀ ≤ a_H 𝔈 + r_H ℜ, with a_H = μ^(−1) (order 0), r_H = ν^(−1) ≥ 1 and h = Ψ_∅.

So no factor 2 enters a_H. The bound is the same as eq:tl5-hfs-linfty's own 𝔰_P⁰ ≤ 2C_S ℰ_g^(1/2) + 2C_(0,0) η₀ (87:5557). Now max_Φ a_Φ = max μ^(−(o+2)/2) ≤ μ^(−N/2) holds, since o ≤ N − 2 for every low quantity, H included. The counterexample the review gave (μ > 1/2 at N = 4) no longer applies.

### (ii) The η₀ part of D̂Ψ_B on S_a

**The new text:** "a coefficient of the remainder of ℒ^J D̂Ψ_B carrying a ≤ 2 letters is at most Λ_a ≤ ν^(−(|B|+3)/2) ν^((1+a)/2) Λ_a ≤ ν^(−(|B|+3)/2) Λ₂^ν, which gives r_Φ times the constant C_(1,0) formed with ν".

**First inequality.**
- ν^(−(|B|+3)/2) ν^((1+a)/2) = ν^((a − |B| − 2)/2).
- The exponent is ≤ 0, since a ≤ 2 and |B| ≥ 0.
- With ν = μ^θ ∈ (0, 1], so that μ ∈ (0, 1] and θ ∈ [0, 1], a power with exponent ≤ 0 is ≥ 1. The sign is right; at θ = 0 it is an equality.

**Second inequality.**
- Λ₂^μ := max(μ Λ₁, μ^(3/2) Λ₂) (87:5470), taken at ν, gives ν^((1+a)/2) Λ_a ≤ Λ₂^ν for a = 1 (ν Λ₁) and a = 2 (ν^(3/2) Λ₂). This is exactly the definition.
- a = 0 does not occur: a remainder factor is ℒ^B Γ′[π^Z] (lem:tl5-hfs-quadratic (a), 87:5483–5484), which carries |B| + 1 ≥ 1 letters.
- The text's "a ≤ 2" is the chapter's own wording at 87:5579, where the same inequality μ^((1+a)/2) Λ_a ≤ Λ₂^μ is used.

**What it gives.**
- On S_a, |D̂Ψ_(JB)|, |Ψ_C| and |D̂Ψ_C| (|C| = |J| + |B| − a ≤ N − 1) are at most η₀ ≤ ν^(−(|B|+3)/2) η₀.
- Termwise, (1 + 6Λ₂) η₀ ≤ ν^(−(|B|+3)/2) (1 + 6Λ₂^ν) η₀.
- C_(1,0)² = 516π² C_(S³)² 𝔭₃ 𝔴(p)⁶ sup_(S_a) 𝔳⁶ (1 + 6Λ)² (87:4344) has no k₁ in it, so the result is r_Φ C_(1,0)^♮(ν) η₀, with r_Φ = ν^(−(o+2)/2) and o = |B| + 1.
- This is the constant that C_((∞,0),ν)^(N−4) in eq:tl5-hfq-small carries. It matches Comparison line 214 ("C_(1,0) with Λ₂^ν = max(νΛ₁, ν^(3/2)Λ₂)").
- The argument is the ν-analogue of 87:5580–5581 ("on S_a it is at most μ^((1+a)/2) Λ_a η₀(p)"), and it agrees with the D̂²Ψ_B step, which already gives the η₀ parts of the jets the weight ν.

The leading term |D̂Ψ_(JB)| ≤ η₀ ≤ r_Φ η₀ is left to the reader, which is acceptable. The second gap the review named is closed.

### (iii) The rest of the proof

It reads correctly with both changes. Each low quantity satisfies |Φ| ≤ a_Φ 𝔈 + r_Φ ℜ + 𝔫_Φ. The fixed-point step gives t ≤ 2, and with max a_Φ ≤ μ^(−N/2) and max r_Φ ≤ ν^(−N/2) this yields eq:tl5-hfq-small. No new error.

## n1 — the clash with ν := μ^θ (lines 80–85): RESOLVED

"at most its background norm times 𝔰^(q−1) μ^(n/2) ν^(−ℓ_E(Φ₂)/2) 2k₂ ϱ(p)" no longer uses ν for the background norm. The rest checks:
- μ^(n/2) = μ^((1−θ)n/2) ν^(n/2), and ν^((n − ℓ_E)/2) ≤ ν^((b−1)/2), since n − ℓ_E ≥ b − 1 (b ≥ 1) or ≥ 0 (b = 0) and ν ≤ 1. So the term is at most μ^((1−θ)n/2) ν^(−1/2) ν^(b/2).
- eq:tl5-hfs-sum with ν′ = ν (Σ background norm · ν^(b/2) 𝔰^(q−2) ≤ 𝔠^♮_n(ν)) then gives the first replacement of the lemma's statement.

## n2 — 𝔰_θ (lines 108–110): RESOLVED

𝔰_θ is defined in def:tl5-hf-constants (87:4451), formed with ϑ ∈ (0, 1/4], and does not involve θ. The added clause says this, and the citation is right.

## n3 — the Placement's line reference (line 173): RESOLVED

"(line 5978 once item 2 is applied)": after item 2 the last line of rem:tl5-hft-what is 87:5978. I checked this on the scratch merge.

## n4 — the bound of ‖M_g‖_Σ (lines 103–104): RESOLVED

"its bound of ‖M_g‖_Σ holding by [[lem:tl5-hfq-theta]]". That lemma's statement includes "the statements of lem:tl5-hft-small (b) and of lem:tl5-hft-products hold". lem:tl5-hft-products gives lem:tl5-hfs-mixed with ‖M_g‖_Σ ≤ λ_t^μ 𝔍_g + ς_t ϱ, from the bound of M_g^(3) in lem:tl5-hft-small (b). This applies under 𝔰 ≤ 𝔰₀^q, since k₃^♮(μ) ≤ k₃^♮(ν). The citation is right.

## The Comparison against the chapter text (spot check)

The Comparison did not change. After the change it still agrees with the chapter text:

**Constants:**
- 𝔠^Mq₁ and 𝔠^Mq₂ (eq:tl5-hfq-m);
- 𝔤₁ = 1 + 2𝔰_♭ (87:5447) and 𝔤₀ = √5 + 1/4 (87:4246);
- k₃^♮(ν) (lem:tl5-hft-small (b) at N = 4);
- 𝔰₀^q and 𝔰₁^q, with 𝔰_θ (def:tl5-hfq-constants);
- 𝔰_(*,q) (eq:tl5-hfq-constants).

**The C_(∞,·) constants:**
- C_(∞,μ)^(0), C_((∞,ϱ),ν)^(0) and C_((∞,0),ν)^(0) are eq:tl5-hfg-cinf with (2𝔐^(0))^(1/2) = √16 = 4, since 𝔐^(0) = 1 + 7.
- C_(1,0)^♮(ν) with Λ₂^ν, now matching the m1 text.

**The rest:**
- k₁^(j,ν) and α_𝔄^(j,ν) (87:5468–5470 at ν);
- 𝔤_(ϱ,q) and ε_(w,q);
- λ_t^(μ,2), 𝔛^q_(1,t), 𝔛^q_(2,t) and 𝔜^q_(1,t) (lem:tl5-hfq-mixed);
- S_(M,q), 𝔯_(M,q), ε_(M,q), A_q, B_q and 𝔯_q.

**Numbers recomputed:**
- At 𝔰_♭ = 1/8: 𝔠^Mq₁ = 550.83204 and 𝔠^Mq₂ = 5.34765625.
- At 𝔰_♭ = 10⁻¹⁰: 480.0000000453 and 4.0000000008.
- 96𝔤₁(𝔤₀ + √5)𝔰_♭ = 70.832 ≤ 71.

All agree with Comparison lines 207 and 234.

## New findings

None.

The only remarks are cosmetic: the short source lines 67, 83, 104 and 110 left by the line breaks of the replacements. The paper's rules allow them, and they need no change.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd4/:
- tree/: the merged copy at a08ce8c0;
- orig/: the unmerged archive, for the numbering comparison;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- 87.md: chapter 87 at a08ce8c0;
- grd4.diff: the diff.

Verdict: CONFIRMED
