# C-P-GRD3: confirming read of proofs/P-GRD3.md (the constants sharpened a third time, sec:tl5-hft)

**File read:** proofs/P-GRD3.md at 3748e932, md5 88c8d48fa7ae99695c536c90a17ad66c, 345 lines:
- chapter text 1–217 (the brief says 1–216; line 217 is the last line of rem:tl5-hft-what, "paper for no background at 10 l5.");
- Placement 219–245;
- Comparison 247–318;
- crosswalk rows 320–345.

**Review being confirmed:** notes/reviews/R-P-GRD3.md (on 46fc10fc, md5 fce4240d…): NOT CONFIRMED, 0 Major, 2 minor (m1, m2), 4 nits (n1–n4).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd3/.

## Verdict in brief

Five of the six findings are resolved correctly and completely (m1, n1, n2, n3, n4). m2 is resolved where it matters: the three upper bounds are rigorous and dominate partial sum plus tail.

But the m2 change brings in a new false statement. "(the values are 0.89416, 3.63744, 15.7096)" gives the sums truncated at 2j₁ < 2·10⁵, not the values. The values are 0.894166, 3.637471 and 15.70976, and to the digits printed they are 0.89417, 3.63747 and 15.7098. Two of the three printed "values" lie below the true values by more than rounding: the same defect m2 was raised against.

The same sentence also leaves out the step that makes the tail bound work: m_(j₁j₂)(r) = 0 unless |j₁ − j₂| ≤ r, so that 2j₂ + 1 ≥ 2j₁ + 1 − 2r. One replacement (C1′) fixes both. It is in the Comparison, not the chapter text, so the chapter text itself is confirmed.

## What changed between 46fc10fc and 3748e932

`git diff 46fc10fc 3748e932 -- proofs/P-GRD3.md` has exactly seven hunks:
- R1: lines 37–43, m1.
- R3: lines 59–60, n2.
- R2: lines 213–215, n1.
- R4: line 229, n3.
- C1: lines 277–280, m2.
- C2: line 293, n4.
- The 15 crosswalk rows from lem:tl5-hft-face on, renumbered by +3.

Each hunk is the review's replacement text verbatim. **Nothing else changed.** The same commit adds notes/reviews/R-P-GRD3.md, which is not merged text.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive 3748e932 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd3/tree. Chapter 87 and its crosswalk are byte-identical at f754985f and 3748e932, so the Placement's quotations are current.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:5757–5758. After the replacement, rem:tl5-hfs-what ends at line **5759**.
- Item 1: chapter-text lines 1–217 were appended there after one blank line.
- Crosswalk: the 19 rows were appended to crosswalk/87-ten-l5.tsv with `@PENDING:` → `@3748e932:`. Each row's line holds its `{#label}` (19/19).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5207 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5207, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** none of the 5188 old labels changes its printed number. The section is Section 57.18; thm:tl5-hft is Theorem 57.183, thm:tl5-hf4t is Theorem 57.184 and rem:tl5-hft-what is Remark 57.185.

**Crosswalk:** a header row, then 363 rows equal, in order, to the 363 labels of chapter 87.

**Paper rules on the changed chapter lines** (37–43, 59–60, 213–215):
- Lengths, in characters: 112, 106, 115, 112, 115, 112, 35, 117, 104, 119, 117, 30. The longest chapter-text line in the file is 121 (line 196, unchanged).
- No wrapped line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Line 39 starts with "[J₁^±", line 41 with "Σ_i" and line 216 with "[[thm".
- All 19 labels are lowercase.
- There are no file or program names and no code in the chapter text.

## m1 — the Casimir value (lines 37–43): RESOLVED

**Convention:** 87:3923 gives K_ab := X_a ∂_(X_b) − X_b ∂_(X_a). As a linear field X ↦ BX this is B = E_ba − E_ab, and the bracket of linear vector fields is [V_A, V_B] = V_(BA−AB). Script: scratchpad/reader/cpgrd3/calc/casimir.py; sympy, exact.

**The brackets.** With L₁ = K₂₃, L₂ = −K₁₃, L₃ = K₁₂, M_i = K_(i4) and J_i^± = (L_i ± M_i)/2:
- As vector fields, [J₁^±, J₂^±] = −J₃^±, [J₂^±, J₃^±] = −J₁^± and [J₃^±, J₁^±] = −J₂^±, for both signs.
- [J_i⁺, J_l⁻] = 0 for all nine pairs (i, l).
- I checked independently with the K_ab as differential operators on a generic function f(X₁, …, X₄) (sympy): the same seven relations hold exactly. The operator bracket on functions is the vector-field bracket, and ℒ_[X,Y] = [ℒ_X, ℒ_Y] on tensors, so the relations hold for the ℒ_(J^±) on V_π.
- As 4×4 matrices acting on vectors the commutator has the opposite sign, [J₁⁺, J₂⁺] = +J₃⁺. The text says "the fields … satisfy", which is the right reading, and the sign does not enter the Casimir.

**The sum.** Σ_(a<b) K_ab² = Σ_i (L_i² + M_i²) holds term by term, since L₂² = K₁₃². Then (x + y)² + (x − y)² = 2x² + 2y² holds for non-commuting x and y, so Σ_i (L_i² + M_i²) = 2 Σ_i ((J_i⁺)² + (J_i⁻)²). Both equalities were checked exactly as operators on f and as 4×4 matrices.

**The signs.** The J_i^± are real and skew. With S := −iJ, [J₁, J₂] = −J₃ gives [S₁, S₂] = iS₃, the standard relations, and −ΣJ_i² = ΣS_i² = j(j + 1) on spin j. The bracket relations fix the normalisation, since scaling J by λ scales the bracket by λ² and the right side by λ. Checks:
- on ℝ⁴, −Σ(J_i⁺)² = −Σ(J_i⁻)² = 3/4 = (1/2)(3/2);
- on harmonic polynomials of degree n = 1, …, 5, both are (n/2)(n/2 + 1).

**The parenthetical checks.**
- Each K_ab² is minus the projection onto the (a, b) plane, so on ℝ⁴ the sum is −3 = 2(−3/4 − 3/4).
- On degree-n harmonics, Σ K_ab² = −n(n + 2) for n = 1, …, 5 (two harmonics each), equal to 2·(−2(n/2)(n/2 + 1)).

**Both coefficients.** On (ℝ⁴)^(⊗2) I diagonalised −Σ(J⁺)², −Σ(J⁻)² and Ω together. The joint eigenvalues are:
- (0, 0) with Ω = 0, once;
- (0, 2) with Ω = 4, three times;
- (2, 0) with Ω = 4, three times;
- (2, 2) with Ω = 8, nine times.

So Ω = 2j₁(j₁ + 1) + 2j₂(j₂ + 1) holds on (1, 0) and (0, 1), where j₁ ≠ j₂. The argument is now an identity, Ω = 2(−Σ(J⁺)²) + 2(−Σ(J⁻)²). It fixes each coefficient separately, independently of the j₁ = j₂ checks, which now serve only as sanity checks. The gap m1 named is closed.

**Wording:**
- Since the labelling (j₁, j₂) is a convention and c_π and m_(j₁j₂) are symmetric, "of spins j₁ and j₂ on π" is right.
- "Σ_(a<b) K_ab²" for Σ ℒ_(K_ab)² is the abuse of notation the earlier text already used.
- No new error.

## m2 — C_(E,r)² as rigorous upper bounds (Comparison, lines 277–280): BOUNDS RESOLVED; NEW ERROR IN THE SAME SENTENCE

**The multiplicities.** I iterated ⊗(2[0] ⊕ [1]), with dimension checks 25, 125, 625:
- e(2) = (5, 5, 1);
- e(3) = (15, 21, 8, 1);
- e(4) = (51, 86, 46, 11, 1).

An independent SO(3) character integral gives the same. All agree with line 274.

**The partial sums over 2j₁ < 3000.** Exact rational terms, summed at 30 digits (calc/ce.py):

| r | partial sum | file says | tail bound 5^r/(2π²(3000 − 2r)) | partial + tail | stated bound |
|---|---|---|---|---|---|
| 0 | 0.0833164 | — | 1.69·10⁻⁵ | 0.0833333 | 1/12 |
| 2 | 0.8937443 | 0.89374 ✓ | 4.2274·10⁻⁴ | 0.8941671 | ≤ 0.8942 ✓ |
| 3 | 3.6353605 | 3.63536 ✓ | 2.1151·10⁻³ | 3.6374756 | ≤ 3.6375 ✓ |
| 4 | 15.6992049 | 15.6992 ✓ | 1.0583·10⁻² | 15.7097874 | ≤ 15.710 ✓ |

The partial sums agree with 0.89374, 3.63536 and 15.6992 to the digits shown. Each stated bound dominates partial sum plus tail, the closest margin being 2.4·10⁻⁵ at r = 3.

**The per-term bound: proved.** Put a = 2j₁ + 1 and b = 2j₂ + 1. Then 1 + 2j₁(j₁ + 1) + 2j₂(j₂ + 1) = (a² + b²)/2, so a term of the sum is 4abm/(a² + b²)². Since a² + b² ≥ 2ab, the term is at most m/(ab). The script asserts this exactly for every term with 2j₁ < 3000.

**Σ_(j₂) m_(j₁j₂)(r) ≤ 5^r: proved.**
- Σ_(j₂) m_(j₁j₂) = Σ_j e_j · #{j₂ : |j₁ − j| ≤ j₂ ≤ j₁ + j, j₂ ≡ j₁ mod 1}.
- That count is 2 min(j₁, j) + 1 ≤ 2j + 1.
- So the sum is at most Σ_j (2j + 1) e_j = dim E_o = 5^r, with equality once j₁ ≥ r.
- The script asserts this for every 2j₁ < 3000.

**The tail: proved, and it does need the extra step.** The tail is the sum over 2j₁ =: n ≥ 3000, n running over every integer, which takes the half-integer steps of j₁. The steps:
- e_j(r) = 0 for j > r, so m_(j₁j₂)(r) = 0 unless |j₁ − j₂| ≤ r. On every nonzero term, therefore, b ≥ a − 2r = n + 1 − 2r > 0.
- So the j₂-sum at fixed n is at most 5^r/((n + 1)(n + 1 − 2r)).
- That is at most 5^r(1/(n − 2r) − 1/(n + 1 − 2r)), which telescopes to 5^r/(3000 − 2r).
- With the factor 1/(2π²) this is the stated bound.

Without the lower bound on 2j₂ + 1, the two facts the Comparison cites give nothing: a j₂-sum of m/(ab) bounded only through Σ m ≤ 5^r and b ≥ 1 would diverge over n. The vanishing for |j₁ − j₂| > r is stated in the chapter text (line 52), but the Comparison's "as …" clause omits it and the telescoping. That is an incomplete justification, not a wrong one.

**The new error: "(the values are 0.89416, 3.63744, 15.7096)".** I computed rigorous enclosures (calc/truev.py):
- lower end: the partial sum to 2j₁ < N;
- upper end: the partial sum plus the tail bound;
- additional lower bound: the tail is at least 5^r(1 − 2r²/(N + 1 − 2r)²)²/(2π²(N + 1 + 2r)), from 4ab/(a² + b²)² = (1/(ab))(1 − (a − b)²/(a² + b²))² and Σ_(j₂) m = 5^r for n ≥ 2r.

| r | partial, 2j₁ < 2·10⁵ | enclosure from N = 3000 | enclosure from N = 2·10⁶ | value | file says |
|---|---|---|---|---|---|
| 2 | 0.8941601 | [0.8941658, 0.8941671] | 0.894166448 (width < 10⁻⁹) | **0.894166** | 0.89416 |
| 3 | 3.6374393 | [3.6374664, 3.6374756] | 3.637470994 | **3.637471** | 3.63744 |
| 4 | 15.7095991 | [15.7097276, 15.7097874] | 15.709757453 | **15.70976** | 15.7096 |

The printed "values" are the partial sums to 2j₁ < 2·10⁵, copied from R-P-GRD3's m2, where they are also called "the true values". The tail beyond 2·10⁵ is about 5^r/(2π²·2·10⁵), for example 1.6·10⁻⁴ at r = 4, and the tail bound is asymptotically sharp, so it cannot be neglected.

All three printed values lie below the true ones:
- at r = 3 by 3·10⁻⁵;
- at r = 4 by 1.6·10⁻⁴;
- at r = 2 the value rounds to 0.89417.

So the parenthetical repeats, in a smaller way, the defect m2 was raised against: numbers presented as the constants that are not upper bounds. The stated bounds 0.8942, 3.6375 and 15.710 still dominate the true values and are the numbers to use.

**The factors** 219, 270 and 197 stand. They are 196.083/0.8942, 981.083/3.6375 and 3088.083/15.710, with C_(S³)²𝔭_r = 2353/12, 11773/12 and 37057/12.

**Fix:** C1′ below. It corrects the values and adds the missing step. A minimal alternative is to change only "0.89416, 3.63744, 15.7096" to "0.89417, 3.63747, 15.7098".

## n1 — what 𝔛, 𝔜 and 𝔪 carry (remark, lines 212–215): RESOLVED

The new text reads: "every constant formed from the Sobolev inequality on a face, at level four also 𝔛, carries 6C_(E,r)² in place of 6C_(S³)² 𝔭_r, and these constants, 𝔜 and 𝔪 carry the operator norms 𝔳₀, 𝔴₀". I checked each part against 87:4762–4765 and lem:tl5-hft-face (c):
- 𝔛_t carries 𝔭_r 𝔵_r(t), and (c) replaces 𝔭_r/2 = 6C_(S³)²𝔭_r by 6C_(E,r)² and 𝔳 by 𝔳₀ in 𝔵_r.
- 𝔜_t is built from 𝔱₃, 𝔱₂, [𝔳⁶]_t, [𝔳⁴]_t, λ_t and ς_t, all from lem:tl5-hf4-face (a) and the recovery constants, with no Sobolev constant on S³. So it carries 𝔳₀ only.
- 𝔪 carries max(1, 𝔴₀)⁶.

The sentence is now exact, and the paragraph still reads correctly. Line 215 is now a short source line, "are free for each face. As for" (30 characters); that is cosmetic and the lint accepts it. See N3 for the clause it carries.

## n2 — h₀ the same for all faces with one t in (c) (lines 59–60): RESOLVED, consistent with level four

**The new hypothesis:** "with numbers α, β, ρ fixed for each face Σ₁(a, b), in (c) the same for all the faces Σ₁(t, b) with one t".

**Why (c) needs it.**
- lem:tl5-hf4-face (87:4684–4698) fixes t and b with Σ = Σ₁(t, b), but its brackets [f]_t are suprema over Σ₁(t, v*) ⊇ Σ₁(t, b).
- Its (a) starts from the leaf S_t, which lies in every Σ₁(t, b).
- With 𝔳₀ and 𝔴₀ in place of 𝔳 and 𝔴, the numbers 𝔵_r(t), 𝔱_r(t), 𝔪(t) and [𝔳₀^(2r)]_t are functions of t alone only if h₀ does not depend on b.

**How level four uses it.**
- lem:tl5-hf4-mixed and lem:tl5-hfg-mixed apply (c) on Σ₁(t, b) for every b ∈ [1/2, s] and produce 𝔛_t, 𝔜_t and 𝔪(t).
- m_t (87:4816, 5289) is integrated over t alone in S_M and 𝔯_M, and the proofs of thm:tl5-hf4s and thm:tl5-hf4t pass through these.
- So a choice of h₀ per t is exactly what the level-four constants need, and it agrees with the Comparison's level-4 entries ([·]_t with 𝔳₀ and 𝔴₀, lines 295–298).

**Other uses.** (a) and (b) of lem:tl5-hft-face (C_S^E, C₁^E and the others, with sup over Σ₁(a, b)) keep a choice per face. They are separate inequalities with their own auxiliary metric, so no conflict arises.

**The proof** still holds under the new hypothesis: h₀ has constant coefficients on each face, so ℒ_(∂_γ)h₀ = 0.

The remark (line 215) and the Comparison (line 281) still say "free for each face" and "chosen per face". See N3; this is recommended, not required.

## n3 — the Placement's line reference (line 229): RESOLVED

"(line 5759 once item 2 is applied)": after item 2 the last line of rem:tl5-hfs-what is 87:5759. I checked this on the scratch merge.

## n4 — C_(1,0)^♮ in option (b) (line 293): RESOLVED

"(with Λ₂^μ for C_(1,0)^♮, option (b))" matches 87:5547–5550. There C_(1,0)^♮ is C_(1,0) with Λ₂^μ in place of Λ, and C_((∞,0),μ) is formed with C_(1,0)^♮. Option (b)'s 𝔰_(*,t) (lines 154–155, 270) uses C_((∞,0),μ).

## New findings

- **N1 (required; Comparison, lines 279–280).** "(the values are 0.89416, 3.63744, 15.7096)" are truncated sums, not the values, which are 0.894166, 3.637471 and 15.70976. The change brought this in. Fix: C1′.
- **N2 (with N1; Comparison, lines 278–279).** The tail bound's justification omits that m_(j₁j₂)(r) = 0 unless |j₁ − j₂| ≤ r, which gives 2j₂ + 1 ≥ 2j₁ + 1 − 2r, and the telescoping sum. Fix: C1′.
- **N3 (recommended, not required; line 215 and Comparison line 281).** After n2 the lemma ties α, β, ρ across the faces Σ₁(t, b) with one t in (c). The remark's "free for each face" and the Comparison's "chosen per face" overstate the freedom at level four. Fix: R2′ and C3′. They are optional; with them the merged copy passes all three checks again (scratch: P-GRD3.variant.md, md5 650c18c6…).

## Replacement texts

Each old text occurs exactly once in the file at 3748e932. The crosswalk line numbers are unaffected: C1′ adds two lines after the chapter text, and R2′ and C3′ change no line count.

### C1′ (N1, N2; required), Comparison lines 277–280

Old:

                     C_(E,2)² ≤ 0.8942, C_(E,3)² ≤ 3.6375, C_(E,4)² ≤ 15.710, C_(E,0)² = 1/12: the sums over 2j₁ < 3000
                     are 0.89374, 3.63536, 15.6992 (computed), and the tail is at most 5^r/(2π²(3000 − 2r)), as each term
                     is at most m_(j₁j₂)(r)/((2j₁ + 1)(2j₂ + 1)) and Σ_(j₂) m_(j₁j₂)(r) ≤ 5^r (the values are 0.89416,
                     3.63744, 15.7096); against C_(S³)² 𝔭_r = 196.1, 981.1, 3088.1: factors 219, 270, 197 in the squares;

New:

                     C_(E,2)² ≤ 0.8942, C_(E,3)² ≤ 3.6375, C_(E,4)² ≤ 15.710, C_(E,0)² = 1/12: the sums over 2j₁ < 3000
                     are 0.89374, 3.63536, 15.6992 (computed), and the tail is at most 5^r/(2π²(3000 − 2r)), as each term
                     is at most m_(j₁j₂)(r)/((2j₁ + 1)(2j₂ + 1)), Σ_(j₂) m_(j₁j₂)(r) ≤ 5^r, m_(j₁j₂)(r) = 0 unless
                     |j₁ − j₂| ≤ r, so that 2j₂ + 1 ≥ 2j₁ + 1 − 2r, and Σ_(n≥3000) 1/((n + 1)(n + 1 − 2r)) ≤ 1/(3000 − 2r)
                     (the values are 0.894166, 3.637471, 15.70976, computed); against C_(S³)² 𝔭_r = 196.1, 981.1, 3088.1:
                     factors 219, 270, 197 in the squares;

(Lines: 115, 117, 110, 118, 117 and 54 characters. The minimal alternative changes only "0.89416, 3.63744, 15.7096" to "0.89417, 3.63747, 15.7098".)

### R2′ (N3; recommended), chapter text line 215

Old: `are free for each face. As for`

New: `are free for each face, in (c) for each t. As for`

### C3′ (N3; recommended), Comparison line 281

Old:

                     h₀ = α² du² + β² dv² + ρ² γ₀ with constants α, β, ρ chosen per face;

New:

                     h₀ = α² du² + β² dv² + ρ² γ₀ with constants α, β, ρ chosen per face (per t at level four in (c));

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd3/:
- tree/: the merged copy at 3748e932;
- tree2/: the merged copy with C1′, R2′ and C3′ applied;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- calc/casimir.py, calc/harm.py: m1;
- calc/ce.py, calc/truev.py: m2.

Verdict: NOT CONFIRMED
