# C-P-GRD7: confirming read of proofs/P-GRD7.md (the first-order constant, counted over the words, sec:tl5-hfx)

**File read:** proofs/P-GRD7.md at 12ca1ed3, md5 31812b4ddaf9be2fc261e43014801aa3, 96 lines:
- chapter text 1–46 (sec:tl5-hfx, 5 labels);
- Placement 48–68;
- Comparison 70–83;
- crosswalk rows 85–96.

**Review being confirmed:** notes/reviews/R-P-GRD7.md (on 3d367b13, md5 3f06af92…): NOT CONFIRMED, 0 Major, 2 minor (m1, m2), 2 nits (n1, n2).

**Also read**, in chapter 87 at 12ca1ed3 (md5 c41fdded…, 6297 lines):
- lem:tl5-hf-linfty, its first-order step (87:4306–4356, C₁, C_(1,ϱ), C_(1,0));
- m_P (87:5053);
- eq:tl5-hfg-cinf (87:5139–5141);
- Λ₂^μ (87:5470);
- lem:tl5-hfs-linfty (87:5545–5590);
- lem:tl5-hft-small (87:5850–5890);
- def:tl5-hfs-constants (87:5646–5675);
- lem:tl5-hfv-rec;
- notes/reports/G0e.md (lines 125–127).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd7/.

## Verdict in brief

**Resolved correctly:** m1, m2 and n1.
- The minimum C₁^x = min(C₁^♮, the new number) is valid at every use.
- The remark's cross term and the sufficient condition 8Λ₂^μ ≤ k₁^μ + 1 are right.
- The level-6 entries are right.

**n2: not quite.** The split is right and needed, but the clause it adds, "the part with ϱ being half of it" (line 31), is wrong.
- The single split halves the **square** of the ϱ part.
- So the part with ϱ is 2^(−1/2) times that of the old proof, not half.
- Read literally, the clause would give C_(1,ϱ)/2, which is not an upper bound.

One word-level replacement fixes it (R1′ below; tested). Everything else is confirmed.

**Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5245 old labels changes. The 5 crosswalk rows point at their labels.

## What changed between 3d367b13 and 12ca1ed3

`git diff 3d367b13 12ca1ed3 -- research/warp-drive/paper/reader/proofs/P-GRD7.md` has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in 12ca1ed3 | Finding |
|---|---|---|
| lem:tl5-hfx-c1 statement and display | 10–14 | m1 |
| the proof's last sentence | 28–31 | m1, n2 |
| thm:tl5-hfx statement | 34–35 | n1 |
| rem:tl5-hfx-what | 40–46 | m1 |
| Comparison opening | 72–79 | m1 |
| Comparison "Level 6" | 82–83 | m2 |
| crosswalk rows of thm:tl5-hfx and rem:tl5-hfx-what | 92–93 | renumbered by +1 |

**Nothing else changed.** The introduction, the proof up to "In the", the theorem's proof and the Placement are byte-identical to the draft's. The same commit also adds notes/reviews/R-P-GRD7.md and files under rule/, which are not merged text.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive 12ca1ed3 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd7/tree. Chapter 87 and its crosswalk are byte-identical at a3d0c091 (the Placement's HEAD) and 12ca1ed3.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:6296–6297. It replaces two lines by two, so rem:tl5-hfw-what still ends at **6297**, as item 1 says.
- Item 1: chapter-text lines 1–46 were appended there after one blank line.
- Crosswalk: the 5 rows were appended with `@PENDING:` → `@12ca1ed3:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5250 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5250, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5245 old labels changes its printed number.**
- The new labels are numbered as follows:
  - sec:tl5-hfx is Section 57.22;
  - lem:tl5-hfx-c1 is Lemma 57.202;
  - eq:tl5-hfx-c1 is (57.146);
  - thm:tl5-hfx is Theorem 57.203;
  - rem:tl5-hfx-what is Remark 57.204.

**Crosswalk:**
- Each of the 5 rows' line holds its `{#label}`: lines 1, 9, 14, 33 and 40.
- Appended, the file has a header and 399 rows, equal in order to the 399 labels of chapter 87.

**Paper rules on the changed chapter lines** (10–14, 28–31, 34–35, 40–46):
- All are at most 120 characters, and so is every chapter-text line of the file.
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Lines 11 and 35 start with "(", lines 43 and 44 with "4|∂_γ|²" and "8Λ₂^μ".
- All 5 labels are lowercase.
- There are no file or program names and no code in the chapter text.

## m1 — C₁^x := min(C₁^♮, the new number): RESOLVED

### Validity of the minimum

C₁^♮ is a number attached to the point p. It is C₁ of lem:tl5-hf-linfty with Λ₂^μ and k₁^μ (87:5547–5548): 𝔴(p)⁶ times a supremum over the face Σ₁(a, b), a = τ₁(p), b = τ₂(p). The new number has the same form, with ϖ′ and k₁^μ inside the same supremum. Both are therefore numbers at p, and eq:tl5-hfx-c1 takes the minimum of the two numbers, not inside the supremum. That is legitimate.

**Both bounds hold with the same ϱ and η₀ parts.** At p:
- μ^((|B|+3)/2) |D̂Ψ_B(p)| ≤ C₁^♮ ℰ_g^(1/2) + C_(1,ϱ) ϱ + C_(1,0)^♮ η₀ (eq:tl5-hfs-linfty's first-order bound);
- by the new count, the same holds with the second entry, a smaller ϱ part (see n2) and an η₀ part at most C_(1,0)^♮ η₀. On S_a the 43 is kept, since η₀ is a supremum.

So both hold with the old parts C_(1,ϱ)ϱ and C_(1,0)^♮η₀, and hence so does the minimum. The same holds unweighted in lem:tl5-hft-small (a) (87:5869–5872) and with ν in lem:tl5-hfq-theta. This is the device of R-P-GRD5's m1, a choice made at each point between two valid bounds.

**Where C₁ is used.** Every use comes from this first-order bound at a point, and every use is nondecreasing in C₁:
- **C_(∞,μ)^(m)(p)** = 2 max(2C_S, C₁, k₁^(m,μ)(2𝔐^(m))^(1/2) max(C_S, C₁)) at p (eq:tl5-hfg-cinf with the substitutions of 87:5548–5550). Then 𝔰_* takes the supremum over p of 2C_(∞,μ)^(N−4)(p)…, after the minimum at each p.
- **C_P^v** at p: at N = 4 it is 2 max(2C_S, C₁, 𝔨_rec), where 𝔨_rec uses μ²|D̂Ψ_Z| ≤ C₁ℰ_g^(1/2) + …, the first-order bound with B = Z. At N ≥ 5 it is C_(∞,μ)^(m_P) with m_P = 1 (87:5053).
- **𝔎 = max(2C_S𝔨_A, C_P𝔨_B)** at p, and 𝔞_(·,s) ∋ 𝔣₀C_P + 𝔣₂𝔤𝔎. S_F^v takes face suprema of 𝔞e^(φ/2) after the minimum at each point.
- **The low-level second-order step** uses max(C_S, C₁) for jets at the same point p.

C₁ does not enter C_(1,ϱ), C_(1,0)^♮, 𝔎_ϱ, 𝔎₀, 𝔯^v, 𝔰₁^v or the level-four mixed constants. So the minimum is valid wherever C₁ is used, and C₁^x ≤ C₁^♮ makes every constant with index x at most its old value. The proof's last sentence states this, and thm:tl5-hfx's proof (unchanged) routes every use through the three lemmas.

### The cross term and the sufficient condition (remark lines 40–46; Comparison 72–79)

Put x = k₁^μ + 1 and Λ = Λ₂^μ = max(μΛ₁, μ^(3/2)Λ₂). I checked this exactly and on a 300,000-point sample (calc/c1.py).

- **ϖ′.** ρ′₁ = 2μΛ₁ ≤ 2Λ and ρ′₂ = 4μΛ₁ + 2μ^(3/2)Λ₂ ≤ 6Λ, so ϖ′ = 6ρ′₁² + 36ρ′₂² ≤ (24 + 1296)Λ² = 1320Λ². The sample has no violation.
- **The terms.** Expanding (2·43^(1/2)x + (2ϖ′)^(1/2))² = 4·43x² + 4·43^(1/2)x(2ϖ′)^(1/2) + 2ϖ′ gives:
  - the coefficient 4·43·4 of x² against 4·43·8 in C₁^♮;
  - 2ϖ′ against 43·72Λ²;
  - (1 + ϖ′^(1/2))² against 43(1 + 6Λ)²;
  - the cross term 4|∂_γ|²·4·43^(1/2)(k₁^μ + 1)(2ϖ′)^(1/2), with no counterpart in C₁^♮.

  These are the remark's exact terms.
- **The sufficient condition.** The (1 + ϖ′^(1/2))² term is always the smaller: 1 + 36.33Λ ≤ 43^(1/2)(1 + 6Λ). For the ∂_γ part, (2ϖ′)^(1/2) ≤ 51.38Λ reduces the comparison to 456t² − 1347.7t + 172 ≥ 0 with t = Λ/x, which holds for t ≤ 0.1337 or t ≥ 2.822. 8Λ ≤ x means t ≤ 0.125, which is inside, so it is a sufficient condition.
  - It is needed pointwise on Σ₁(a, b), since then the integrands are ordered at every point of the face and so are the suprema. The remark says "on Σ₁(a, b)".
  - Sample: the maximum of C₁^new/C₁^♮ with 8Λ ≤ x is 0.966, with no violation; the overall maximum is 1.157.
- **The example.** At μ = 1, Λ₁ = Λ₂ = 2, k₁^μ + 1 = 8, |∂_γ| = 1, D̂∂_γ = 0: ϖ′ = 5280 and C₁^new/C₁^♮ = 1.108, as the Comparison says ("11 % above").
- **G0e** (G0e.md lines 125–127) gives k₁^μ = 7–16 and Λ₂^μ ≤ 4 × 10⁻³, so 8Λ₂^μ ≤ 0.032 ≪ k₁^μ + 1, as the Comparison says.
- **Decades.** "0.15 decades" is log₁₀√2 = 0.151, and "up to 1.6 decades" is log₁₀43 = 1.63.

## m2 — level 6 (Comparison 82–83): RESOLVED

At N ≥ 5, m_P = min(1, N − 4) = 1 (87:5053), so C_P^v = C_P^♮ = C_(∞,μ)^(1). 𝔰_*^w carries C_(∞,μ)^(N−4), which is C_(∞,μ)^(2) at N = 6. Both contain C₁ (eq:tl5-hfg-cinf). "Level 6: C₁^x enters there as well (C_P^v = C_(∞,μ)^(1), and C_(∞,μ)^(2) in 𝔰_*^w); its effect there is not evaluated here" is right, and agrees with the Comparison's opening ("at level four and at N ≥ 6 alike").

## n1 — the theorem's list (lines 34–35): RESOLVED

"in C_P^v (directly, and at level four also through 𝔨_rec), hence in 𝔎 and S_F^v, and in C_(∞,μ)^(N−4) of 𝔰_*^w":
- At N = 4, C_P^v = 2 max(2C_S, C₁, 𝔨_rec) (lem:tl5-hfv-rec) contains C₁ directly and through 𝔨_rec.
- At N ≥ 6, C_P^v = C_(∞,μ)^(1) contains it directly.
- C_P enters 𝔎 and 𝔞, hence S_F^v.

The vague "the constants of level four" is gone.

## n2 — the split of the 𝒥_g and ϱ parts (lines 28–31): the split is RESOLVED; its added clause is WRONG

**The split is right and is the one that is needed.** The bound is (Σ_J μ^(|B|+3)|D̂ℒ^J A|²)^(1/2) ≤ X 𝒥_g + 43^(1/2)·2k₂ϱ, with X = 2·43^(1/2)(k₁^μ + 1) + (2ϖ′)^(1/2) (the ϱ part with ν or μ-weights as in the respective lemma). Squaring once with (x + y)² ≤ 2x² + 2y² and multiplying by 2|∂_γ|² in eq:tl5-hf-cs-r gives:
- 4|∂_γ|² X² 𝒥_g², the display's second line;
- the part with ϱ, 2|∂_γ|²·2·43·4k₂²ϱ² = 16·43 |∂_γ|²k₂²ϱ².

**The old proof** (87:4347–4353) splits twice: |D̂ℒ^J A|² ≤ 2M₂² + 2·72Λ²𝒥², then M₂² ≤ 8(k₁ + 1)²𝒥² + 8k₂²ϱ². That reproduces C₁'s 4·8 and 4·72, and C_(1,ϱ)'s 32. So per word the ϱ part is 2|∂_γ|²·16k₂²ϱ² = 32|∂_γ|²k₂²ϱ², and over the 43 words it is 43·32 |∂_γ|²k₂²ϱ², which is C_(1,ϱ)²'s 258·32/6.

**The ratio.** New against old is 16·43/(32·43) = 1/2 **in the square**. Under the Sobolev root the part with ϱ of the bound is C_(1,ϱ)ϱ/√2, not C_(1,ϱ)ϱ/2.

The clause "and parts with ϱ and η₀ at most those of that proof, the part with ϱ being half of it" speaks of the parts of the bound, as the preceding "the part with ℰ_g of the bound" shows. So "half" is a factor √2 too small. Anyone forming the reduced ϱ constant from it would get a number that is not an upper bound. The conclusion actually used, "at most those of that proof", is unaffected.

**Fix:** R1′.

## Replacement text

### R1′ (n2), line 31 of P-GRD7.md

Old:

    being half of it. The bound with C₁^♮ holds as well, with the same parts with ϱ and η₀; so it holds with C₁^x. ∎

New:

    being 2^(−1/2) times it. The bound with C₁^♮ holds as well, with the same parts with ϱ and η₀; so it holds with C₁^x. ∎

**Tested:**
- The old text occurs exactly once.
- The new line has 119 characters. No line count changes, so the crosswalk rows stand.
- Variant: scratchpad/reader/cpgrd7/P-GRD7.variant.md, md5 9235942f87a87ae47c67fc80774748ce, 96 lines.
- Merged into a fresh archive of 12ca1ed3 with the same Placement (tree2/): lint.py --chapters 0 hits (5250 labels), assemble.py --check 0 problems, in-memory `[] 0`, and all 5 crosswalk rows at their labels.

An equivalent alternative is "…, the square of the part with ϱ being half of that there."

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd7/:
- tree/: the merged copy at 12ca1ed3;
- tree2/: the same with R1′ applied;
- orig/: the unmerged archive;
- tools/merge.py and tools/merge2.py: apply the Placement and append the crosswalk rows;
- calc/c1.py: ϖ′, the sufficient condition, the example and the ϱ factor;
- grd7.diff: the diff.

Verdict: NOT CONFIRMED
