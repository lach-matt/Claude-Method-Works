# C-P-GRD12: confirming read of proofs/P-GRD12.md (one leaf constant for every rank, and the products over the words, sec:tl5-hfd)

**File read:** proofs/P-GRD12.md at bb003245 (branch ccr-af9edcf6-9a60sz), md5 e3418723eb11471d2dc20e27267c96b2, 325 lines:
- chapter text 1–186 (sec:tl5-hfd, 9 labels);
- Placement 188–209;
- Comparison 211–311;
- crosswalk rows 313–325.

**Review being confirmed:** notes/reviews/R-P-GRD12.md (on 59f30503, md5 eec80894…): NOT CONFIRMED as submitted, 0 Major, 1 minor (m1), 6 nits (n1–n6).

**Also read:**
- thm:tl5-hfu in chapter 87 at bb003245 (87:7031–7047; md5 3fdd3474…, 7077 lines);
- the weight conditions of sec:tl5-hfp (87:6613–6833).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd12/.

## Verdict in brief

All seven changes (m1, n1–n6) resolve their findings correctly and completely. None introduces a new error, and nothing outside the findings changed.

**m1.** The opening paragraph and the Remark now put the sum over π before the largest eigenvalue, max_j Σ_π. That matches the proof of lem:tl5-hfd-leaf, whose central step I re-derived.

**n1.** The containment is right: thm:tl5-hfp (N ≥ 6) and thm:tl5-hfu (N = 4) are contained for all weights, and thm:tl5-hfp at N = 4 only for 𝔶₀, 𝔶₁ ≥ 1, through thm:tl5-hfu.

**n2–n6.** The square roots, 0.0895, 0.0089, "2^n − 1 + 𝔰_♭𝔠^(3♮)_n", −1.0 to −1.65 and the pointer line are all right.

**Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5292 old labels changes. The 9 crosswalk rows point at their labels.

No replacement is needed.

## What changed between 59f30503 and bb003245

`git diff 59f30503 bb003245 -- research/warp-drive/paper/reader/proofs/P-GRD12.md` has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in bb003245 | Finding |
|---|---|---|
| opening paragraph, rewrapped | 7–17 | m1, n2 |
| thm:tl5-hfd, last sentence | 142–143 | n1 |
| rem:tl5-hfd-what | 167–169 | m1 |
| Placement item 2 heading and pointer line | 203, 207 | n6 |
| Comparison table | 233 | n3, 0.0895 |
| Comparison 𝔖_j list | 236 | n3, 0.0089 |
| Comparison "the rest" | 252–253 | n4 |
| Comparison j′ = 4 | 275–280 | n5 |
| crosswalk rows from lem:tl5-hfd-leaf on | 318–325 | renumbered by +1 or +2 |

I compared the rewrapped opening paragraph with the draft's, whitespace normalised. It differs only by:
- the m1 clause ("; summed over π with the weights, these multiples give one number for each spin, the largest being that of spin zero, the constant of the functions");
- the n2 clause ("the square root of the number of its own words, in place of 7^(j′/2), that of all the words of the level").

The rest of the Remark is unchanged. **Nothing else changed.** The same commit adds only notes/reviews/R-P-GRD12.md.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive bb003245 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd12/tree. Chapter 87 and its crosswalk are byte-identical at b6df4c77 (the Placement's HEAD) and bb003245.

**Applying the Placement:**
- Item 2: its two old lines occur exactly once, at 87:7076–7077. The new pointer line, 120 characters, is added after them, so rem:tl5-hfu-what ends at **7078**, as item 1 says.
- Item 1: chapter-text lines 1–186 were appended there after one blank line.
- Crosswalk: the 9 rows were appended with `@PENDING:` → `@bb003245:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5301 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5301, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5292 old labels changes its printed number.**
- sec:tl5-hfd is **Section 57.27**, with lem:tl5-hfd-leaf as Lemma 57.230, lem:tl5-hfd-words as Lemma 57.231, def:tl5-hfd-constants as Definition 57.232, thm:tl5-hfd as Theorem 57.233, rem:tl5-hfd-what as Remark 57.234 and the displays (57.160)–(57.162).

**Crosswalk:**
- Each of the 9 rows' line holds its `{#label}`: lines 1, 19, 28, 61, 74, 109, 133, 137 and 165.
- Appended, the file has a header and 450 rows, equal in order to the 450 labels of chapter 87.

**Paper rules on the changed chapter lines** (7–17, 142–143, 167–169):
- All are at most 119 characters. The longest chapter-text line in the file is 120 (line 180, unchanged).
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Lines 15, 17, 142 and 143 start with "(" or "[[".
- All 9 labels are lowercase.
- There are no file or program names and no code in the chapter text.

## The central step of lem:tl5-hfd-leaf, re-derived

**One Cauchy–Schwarz over π and the basis together.** Expand A = Σ_π A_π with each A_π in an orthonormal basis (s_(πUk)) made of bases of the V_π^U. For a unit u in the fibre at ω,

    ⟨A(ω), u⟩₀ = Σ_(π,U,k) a_(πUk) ⟨s_(πUk)(ω), u⟩₀,

and one Cauchy–Schwarz inequality with the weights w_π gives

    |⟨A(ω), u⟩₀|² ≤ (Σ_π w_π ‖A_π‖²) · Σ_π w_π⁻¹ Σ_(U,k) |⟨s_(πUk)(ω), u⟩₀|² = (Σ_π w_π ‖A_π‖²) · ⟨(Σ_π w_π⁻¹ K_π(ω)) u, u⟩₀,

since ⟨K_π^U(ω)u, u⟩₀ = Σ_k |⟨u, s_k(ω)⟩₀|².

**The operator at o.**
- K_π(g·ω) = g K_π(ω) g⁻¹, so the norm of Σ_π w_π⁻¹K_π(ω) does not depend on ω.
- At o, by Schur's lemma and the trace, K_π^U(o) = dim π P_U/(2π²(2j_U + 1)) if j_U ∈ CG(π), and 0 otherwise.
- So Σ_π w_π⁻¹K_π(o) = Σ_U 𝔖_(j_U)(𝔶)P_U, where 𝔖_j = (1/(2π²(2j + 1))) Σ_(π: j∈CG(π)) dim π/w_π. This is the lemma's definition, since j ∈ CG(j₁, j₂) ⟺ |j₁ − j₂| ≤ j ≤ j₁ + j₂ and j₁ + j₂ − j ∈ ℕ.
- The P_U are orthogonal projections that sum to the identity, so the norm is **max_j 𝔖_j** over the spins of the fibre.
- The supremum over u then gives |A(ω)|₀² ≤ (max_j 𝔖_j)·Σ_(|J|≤2)𝔶_(|J|)‖ℒ^J A‖².

**𝔖_j ≤ 𝔖_0.**
- j ∈ ℕ and j₁ + j₂ − j ∈ ℕ make d := j₁ − j₂ an integer with |d| ≤ j.
- For fixed d, κ = (j₁ + j₂)/2 determines (j₁, j₂) = (κ + d/2, κ − d/2).
- (2j₁ + 1)(2j₂ + 1) = (2κ + 1)² − d² ≤ (2κ + 1)², and c_(j₁j₂) = m² + 2m + d² ≥ m(m + 2) = c_(κκ), with m = 2κ.
- w is increasing in c ≥ 0.
- So each of the 2j + 1 rows is at most 2π²𝔖_0, which gives 𝔖_j ≤ 𝔖_0.
- The fibre always contains spin 0 (e_0(r) ≥ 1), so max_j 𝔖_j = 𝔖_0 = C_(E,0)(𝔶)².

The proof's text (lines 46–56) is exactly this.

**Numbers recomputed** (calc/leaf.py, sums to m = 2·10⁶ with the tail 1/M):

| 𝔶 | C_(E,0)² | 𝔖_j for j = 0–4 | C_(E,0)/C_(E,r) for r = 2, 3, 4 |
|---|---|---|---|
| 1 | 0.0872507 | 0.0872507, 0.0290836, 0.0165243, 0.0115952, **0.00894971** | 0.302241, 0.149897, 0.072222 |
| (μ⁻², μ⁻¹), μ = 10⁻⁴ | 4.59464 × 10⁻⁴ | — | 0.200012, **0.089451**, 0.040005 |

In both cases 𝔖_j is decreasing in j and max_j 𝔖_j = 𝔖_0.

**The wrong order, for contrast.** Σ_π w_π⁻¹ max_j c_(π,j) is 1.19, 1.25, 1.28 and 1.29 times C_(E,0)² for r = 1–4 at 𝔶 = 1, truncated at 2j < 400, consistent with the review's 1.194–1.296. So the order matters, as m1 says.

## m1 — the order of the sum and the largest eigenvalue (lines 7–8, 167–170): RESOLVED

**Opening paragraph.** "on each isotypic component of the fibre it is a multiple of the identity; summed over π with the weights, these multiples give one number for each spin, the largest being that of spin zero, the constant of the functions". The sum over π comes first and gives one number per spin, the 𝔖_j; the largest is then 𝔖_0. That is max_j Σ_π, as proved.

**Remark.** "the pointwise bound needs only the largest eigenvalue of the kernels summed over π with the weights, the Cauchy–Schwarz inequality being taken over π and the basis together for one direction in the fibre; each kernel is a multiple of the identity on each isotypic component of the fibre for the isotropy group, so that sum is 𝔖_j(𝔶) on the component of spin j, and 𝔖_j(𝔶) ≤ 𝔖_0(𝔶)".
- "that sum" refers to the weighted sum of the kernels, an operator equal to 𝔖_j on the spin-j component. That fixes the reading as the largest eigenvalue of Σ_π w_π⁻¹K_π.
- This is the proof's mechanism, including the single Cauchy–Schwarz for one direction u.
- On a whole isotypic component of spin j each K_π is the same multiple dim π/(2π²(2j + 1)) of the identity, so "each kernel is a multiple of the identity on each isotypic component" is exact.

## n1 — the containment (lines 140–143): RESOLVED

The new sentence is "so the hypotheses of [[thm:tl5-hfp]] (N ≥ 6) and of [[thm:tl5-hfu]] (N = 4) imply these, and for N = 4 and 𝔶₀, 𝔶₁ ≥ 1 so do those of [[thm:tl5-hfp]]".
- The pairing matches the parentheses "(or η_u)" and "(or A_u, B_u and 𝔰_*^u)".
- The N = 4 clause is the chain thm:tl5-hfp ⇒ thm:tl5-hfu, which the chapter states only "For 𝔶₀, 𝔶₁ ≥ 1" (87:7044–7046), followed by thm:tl5-hfu ⇒ thm:tl5-hfd for all weights.
- The sentence claims no converse, so it is exact.
- The Comparison's "so it contains both theorems" (lines 213–214) and the crosswalk note "contains both for all weights" read "both" as thm:tl5-hfp at N ≥ 6 and thm:tl5-hfu at N = 4, consistent with this.

## n2 — the counts as square roots (lines 12–14): RESOLVED

"the factor at a point by the square root of the number of its own words, in place of 7^(j′/2), that of all the words of the level". In the proof the factor at a point carries (Σ_(I_P) μ^(k_P+3)|Φ₁|²)^(1/2) ≤ 7^(k_P/2)𝔰_P, the square root of the number 7^(k_P) of its words. 7^(j′/2) is the square root of 7^(j′).

## n3 — the two roundings (Comparison 233, 236): RESOLVED

0.089451 → **0.0895**, and 𝔖_4(1) = 0.00894971 → **0.0089**, both recomputed above. The other entries of the table and of the 𝔖_j list agree with my values to the digits shown.

## n4 — "the rest" (Comparison 252–253): RESOLVED

At Λ = 0, 𝔠^(2♮)_n = 81·2^n − 1: the first sum gives 2^n − 1 and the 2𝔮̂ sum gives 16·5·2^n. 𝔠^D_n = 80·2^n. So 𝔠^♮_n − 𝔠^D_n = 2^n − 1 + 𝔰_♭𝔠^(3♮)_n, that is 15 + 𝔰_♭𝔠^(3♮)₄ at n = 4, as written.

## n5 — the j′ = 4 term (Comparison 275–280): RESOLVED

With 𝔠^♮₄ = 1337–1401, the floor 1303 and 𝔨_B = 10^0.6–0.75:

**Old:** 49(𝔠^♮₄ + 1) gives 6.56–6.87 × 10⁴.

**x = 0** (the part above the floor all in the rest, which then runs from 57 to 121):
- 1853/𝔨_B + 49·(58 to 122) gives 3.17–6.44 × 10³.
- The falls are −1.03 to −1.32, stated as −1.0 to −1.3.

**All of type D** (x = 34–98, the rest at the floor 23, so 49·24 = 1176):
- (1853 + (7^(1/2) to 49)x)/𝔨_B + 1176 gives 1.52–2.85 × 10³.
- The falls are −1.38 to −1.65, stated as −1.4 to −1.65.

So the overall range is −1.0 to −1.65, and the bracket 𝔠^(D,7)₄(μ) ∈ [1853 + 7^(1/2)x, 1853 + 49x] follows from the definition, the type-D excess carrying between 7^(1/2) and 49 per unit.

## n6 — the pointer line (Placement 203, 207): RESOLVED

"[[sec:tl5-hfd]] gives the leaves one Sobolev constant for every rank and sums products over the words ([[thm:tl5-hfd]])." names both changes. It is 120 characters, as item 2's heading now says, and it passed the lint and the assembled line check.

## Observations (no change required)

- Comparison line 281 still says "S_F falls about 1.0–1.7 decades" after the j′ = 4 range became −1.0 to −1.65. "about" and the rounding cover it.
- Remark lines 180–181: "the factor at a point by the 7^(k_P) words of its own length" means counted over those words, which gives the factor 7^(k_P/2). It is not wrong, and the opening paragraph now states the square root explicitly.
- In the Remark, "the largest eigenvalue of the sum over π of the kernels, with the weights" would make the order explicit without the following clause. The present wording is fixed by "so that sum is 𝔖_j(𝔶)", so a change is optional.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd12/:
- tree/: the merged copy at bb003245;
- orig/: the unmerged archive;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- calc/leaf.py: 𝔖_j, the ratios and the wrong-order sum;
- 87.md: chapter 87 at bb003245;
- grd12.diff: the diff.

Verdict: CONFIRMED
