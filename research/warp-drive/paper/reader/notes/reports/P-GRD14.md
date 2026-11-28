# P-GRD14: writer's report (sec:tl5-hfc; levers 1 and 2 of the round-14 plan)

**File:** research/warp-drive/paper/reader/proofs/P-GRD14.md, md5 2c26c0de5e598d4b5ec464c815836c86, 266 lines.
Not committed. Base: HEAD 0563d28a, chapter 87 md5 53dfe295 (7504 lines). Drafted under scratchpad/reader/pgrd14/.

Layout: chapter text 1–136 (9 labels), Placement 138–160, Comparison 162–253, Crosswalk 255–266.
Assembled: Section 57.29; Lemma 57.240 (lem:tl5-hfc-cont), Lemma 57.241 (lem:tl5-hfc-h), Definition 57.242,
Theorem 57.243, Remark 57.244; displays (57.167)–(57.169). Index letter c.

## Proved

1. **lem:tl5-hfc-cont.** lem:tl5-continuation with any threshold 𝔜 ∈ (Y₋, Y₊), the roots of q(y) = By² − y + A, in
   place of 2A. The solution satisfies y_σ ≤ Y₋ = 2A/(1 + (1 − 4AB)^½). Also proved: A ≤ Y₋ < 2A < 1/(2B) ≤ Y₊. For
   𝔜 = 2A the hypotheses are the old ones. Non-emptiness, openness and closedness are each written out.
2. **lem:tl5-hfc-h.** |H| ≤ 𝔤₁|h| wherever 𝔰 ≤ 𝔰_♭. This comes from lem:tl5-wg-norms (a), H = −g⁻¹hĝ⁻¹, and the cost
   1 + |H| of g⁻¹ raising an index, as in lem:tl5-hfs-quadratic (a) and thm:tl5-hfv. Consequently 2C_S and 2C_(0,0)
   become 𝔤₁C_S and 𝔤₁C_(0,0) in the bounds at a point. 𝔰 ≤ 𝔰_♭ is available at every site: each hypothesis 𝔰 ≤ 𝔰₀^⋆, 𝔰₀^♮,
   𝔰₀^μ, 𝔰₀^q or 𝔰₁^v is at most 𝔰_♭.
3. **thm:tl5-hfc.**
   - The constants with index c are those with index l with 𝔤₁ in place of the factor 2.
   - Y_c = 2A_c/(1 + (1 − 4A_cB_c)^½), and 𝔰_*^c = 𝔰_*^l formed with Y_c in place of 2A_l.
   - Closing condition: 4A_cB_c < 1 with η_c > 0, 𝔰_*^c < 𝔰₁^v, η₀ < 𝔰₁^v and admissible rates.
   - Conclusions: a solution with Y_σ ≤ Y_c, plus the rest with 𝔰_*^c.
   - The continuity step is explicit: fix 𝔜 ∈ (Y_c, 2A_c] with 𝔜𝔰_*^c < Y_c𝔰₁^v. Since 𝔰_*^c[𝔜] ≤ (𝔜/Y_c)𝔰_*^c, this
     gives 𝔰_*^c[𝔜] < 𝔰₁^v.
   - The a priori bound is read at three places: (i) Step 1 of every a priori estimate, (ii) the two persistence lemmas
     (the smallness and P(N)), (iii) the continuation. Each takes 𝔜. Steps 2 and 3 do not read the bound.
   - After the solution is built, (i) with Y_c gives 𝔰 ≤ 𝔰_*^c.
   - No site keeps 2A. The Comparison lists every site by line, with its old text and disposition.
   - **Containment:** 𝔤₁ ≤ 5/4 < 2 and Y_c ≤ 2A_c ≤ 2A_l, so every constant is at most its index-l version. The
     hypotheses of thm:tl5-hfe therefore imply these.

## Deduced gains (Comparison; upper figures, every supremum at one point)

- **Lever 1:** A/A₀ = 2 − x₀ with x₀ = 10^(−spare). Level 4: +0.07 / +0.15 / +0.18 where 𝔰_* binds (G0p margins
  0.09 / 0.24 / 0.30, read as closing spare), 0 at seed 2 D_A. Level 6: +0.30 on the ε budget, for f and ϱ.
- **Lever 2:** the μ|H| entry of C_P^v falls by 0.30. Level 4: up to +0.30, capped by the unreported margin of the next
  entry, max(C₁^l, 𝔨_rec^l). This is G0p's "C_S ÷ 2" price up to μ-small entries. Level 6: about 0.
- **Together at level 4:** about +0.37 to +0.48 where 𝔰_* binds.

## Not done (P-GRD15 if the prices leave room)

- Lever 3a: the zeroth-order step via the shorter words, with its own leaf weight.
- Lever 4: the ϱ parts of the products moved into 𝔯.
- The 𝔨₁ Cauchy–Schwarz sharpening and |H| ≤ |h|/(1 − |h|), both small.

## Checks (scratch tree from git archive 0563d28a, Placement applied)

- Item 2's two old lines found once at 87:7503–7504; pointer line 118 characters.
- lint --chapters: 0 hits (5320 labels); assemble --check: 0 problems; in-memory: `[] 0`. Re-run on the repository copy:
  same results.
- 0 of 5311 existing numbers change; 9 added.
- Crosswalk: 9 rows at their labels (lines 1, 15, 18, 39, 60, 72, 74, 78, 121), ASCII; merged 469 = 469, same order.
- Chapter text ≤ 120 characters per line, no forbidden line starts; notes ≤ 121.
