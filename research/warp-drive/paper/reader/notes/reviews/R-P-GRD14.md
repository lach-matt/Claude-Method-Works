# R-P-GRD14: an independent review of proofs/P-GRD14.md (sec:tl5-hfc)

**File reviewed.** research/warp-drive/paper/reader/proofs/P-GRD14.md at fb41e869, md5 2c26c0de5e598d4b5ec464c815836c86,
266 lines. Its parts are:
- the chapter text, P:1–136 (9 labels);
- the Placement, P:138–160;
- the Comparison, P:162–252;
- the crosswalk rows, P:254–266.

The writer's report is notes/reports/P-GRD14.md.

**Base.** chapters/87-ten-l5.md, md5 53dfe2952fe5fd45f3637cbd3cd77a88, 7504 lines and 5,311 labels; this is the 0563d28a
text. Citations below are P:n for the proof file and 87:n for the chapter.

**Verdict: CONFIRMED.** 0 Major, 0 minor, 3 nits, all three in the Comparison.
- Both claims hold, the theorem holds, and the containment of thm:tl5-hfe holds.
- A tested fixed copy repairs the three nits. P:1–226 is byte-identical to the original, so no label moves.

## 1. Mechanics

The scratch tree is `git archive HEAD` with the writer's placement applied.

- **Placement.** Item 2's two old lines occur once, at 87:7503–7504. The new line is 118 characters, as stated. The
  phrase "line 7505, as changed by item 2" is right. The chapter becomes 7642 lines.
- **Checks.**
  - lint.py --chapters: 0 hits, 5320 labels (5311 + 9).
  - assemble.py --check: 0 problems.
  - In-memory check: `[] 0`. I did not run plain `python3 assemble.py`.
- **Crosswalk.**
  - 9 of 9 rows give the line of their label (1, 15, 18, 39, 60, 72, 74, 78, 121).
  - The merged crosswalk has 469 rows for 469 labels, and the new labels are lowercase.
  - None of the 5,311 existing printed numbers changes.
  - The row descriptions match their labels.
- **Format.**
  - The longest chapter-text line is 120 characters.
  - No wrapped chapter-text line starts with a forbidden marker. The START flags occur only on Comparison bullets, from
    P:225 on.
  - The chapter text names no file or program and contains no code or AI language.
- **Numbering.** sec:tl5-hfc is Section 57.29. It contains Lemma 57.240 (lem:tl5-hfc-cont), Lemma 57.241
  (lem:tl5-hfc-h), Definition 57.242, Theorem 57.243 and Remark 57.244, with displays (57.167)–(57.169). The writer's
  report agrees.

## 2. lem:tl5-hfc-cont (P:15–37) holds

I checked it against lem:tl5-continuation (87:3494–3552).

**The roots.**
- With x = 4AB ∈ (0, 1), the roots of By² − y + A are (1 ∓ (1 − x)^(1/2))/(2B).
- The smaller root is x/(2B(1 + (1 − x)^(1/2))) = 2A/(1 + (1 − x)^(1/2)) = Y₋.

**The chain A ≤ Y₋ < 2A < 1/(2B) ≤ Y₊.**
- 1 < 1 + (1 − x)^(1/2) ≤ 2 gives A ≤ Y₋ < 2A.
- x < 1 gives 2A < 1/(2B).
- (1 − x)^(1/2) ≥ 0 gives 1/(2B) ≤ Y₊.
- q is convex with q(0) = A > 0, so q ≥ 0 on [0, Y₋] and q < 0 exactly on (Y₋, Y₊).
- 10⁵ random (A, x) pairs gave 0 failures. The Remark's table Y₋/A = 1 / 1.111 / 1.172 / 1.225 / 1.382 / 2 and the
  series A + A²B + 2A³B² + ⋯ (the Catalan series of the smaller root) both reproduce.

**The key step.** If y ≥ 0, y ≤ A + By² and y ≤ 𝔜 < Y₊, then q(y) ≥ 0 rules out (Y₋, Y₊). So y ≤ Y₋ < 𝔜, and the bound
is strict, which is what openness needs. ✓

**Openness and closedness with 𝔜.**
- **Not empty.** (F1_W), y_(1/2) ≤ A ≤ Y₋ < 𝔜, and continuity in σ.
- **Open.** (H1) on each restriction with y ≤ 𝔜 gives y_σ ≤ Y₋ < 𝔜, in particular y_s < 𝔜. Then (H4) with (F3_W)
  extends the solution, and continuity keeps y ≤ 𝔜 on some [1/2, s″].
- **Closed.** The limit argument of the original with (H2), (F2_W) and the closedness of the tilt goes through. The
  bound y_σ ≤ 𝔜 passes to the limit as y_σ ≤ 2A does: for σ < s̄ by restriction, and at s̄ by continuity.
- **Conclusion.** y_σ ≤ Y₋ follows by (H1) on each restriction. For 𝔜 = 2A ∈ (Y₋, Y₊) the hypotheses are those of
  lem:tl5-continuation. ✓

## 3. thm:tl5-hfc, the threshold (P:74–119) holds

### Circularity: none

- B_c = η_c⁻¹(S_F^c + S_M^c) and A_c = η_c^(−1/2)δ_w + η_c⁻¹(ε^c + ε_M^c), with η_c = 1 − max(ϑ) − 𝔯^c. They are formed
  from the constants with index c, δ_w, ϑ₁, ϑ₂, ϱ and η₀.
- ε^c = ε^l carries 𝔰₁^v, as do 𝔵^z, k₂^z and 𝔨_♯(𝔰₁^v). But 𝔰₁^v = min(𝔰₀/2, c_*κ_m/2, 𝔰_(θ,v)) is a number fixed by
  the setting, not by A, by 𝔰_* or by 𝔜.
- The use of the bootstrap smallness in ε is "2k₂𝔰ϱ ≤ 2𝔰₁^v k₂ϱ" (thm:tl5-hfw, 87:6287) and
  "k₂^z𝔰ϱ/(1 − 𝔵^z) ≤ 𝔰₁^v …" (thm:tl5-hfz). Both go through 𝔰₁^v, never through 𝔰_*.
- S_F, S_M, 𝔯 and ε_M contain no A.
- So Y_c is an explicit function of A_c and B_c, and 𝔰_*^c = 𝔰_*^c[Y_c] is defined after it. Nothing is circular. ✓

### The continuity step

- Every 𝔰_* of the chain has the form sup_p(2C(p)·w(p)·A + b(p)) with C, w, b ≥ 0. The listed forms are:
  - 87:4453, 4824, 5298, 5676, 5910 and 5914 (with μ^(−N/2) outside), and 6098 (with ν^(−2) on the ϱ and η₀ terms);
  - 𝔰_*^v through 𝔰_*^l, each "formed with … and with A_x in place of".
- A occurs once, in the term with C_∞ (or C_P^v at level four).
- 𝔰_*^c[𝔜] = sup(a(p)𝔜 + b(p)). For 𝔜 ≥ Y_c, a𝔜 + b ≤ (𝔜/Y_c)(aY_c + b), so 𝔰_*^c[𝔜] ≤ (𝔜/Y_c)𝔰_*^c. The ϱ and η₀ parts
  b(p) ≥ 0 only help. ✓
- **The choice of 𝔜.** The interval (Y_c, min(2A_c, Y_c𝔰₁^v/𝔰_*^c)) is not empty, because Y_c < 2A_c and 𝔰_*^c < 𝔰₁^v.
  Also 𝔜 ≤ 2A_c < 1/(2B_c) ≤ Y₊. ✓
- **The case A_c = 0.** If A_c = 0, ĝ is the solution, as in thm:tl5-hf. Otherwise B_c > 0 because S_F^c > 0. ✓
- **The final re-run.** With Y_σ(g) ≤ Y_c on [1/2, v*] and 𝔰_*^c[Y_c] = 𝔰_*^c < 𝔰₁^v, Step 1, run with Y_c as its bound
  (the Σ_* argument of thm:tl5-hfy, which needs the strict inequality), gives 𝔰 ≤ 𝔰_*^c on D^κ, |h|_k̂ < κ_m/2 and the
  θ_H bounds. The bound for ε then follows from eq:tl5-hf-eps. ✓

### Every site that reads Y_σ ≤ 2A

I searched chapter 87 for every 2A, 2A_x, 4A², 4A_x², Y_σ and y_σ outside the continuation lemma. The hits are listed
below.

- **Step 1 of each a priori estimate.** The bound is used only for ℰ(p) ≤ e^(φ(p))Y_σ² ≤ 4e^(φ(p))A². The sites are:
  - 87:4460 and 4470–4471 (prop:tl5-hf-bootstrap);
  - 87:4835 (N = 4, Step 1 "as written");
  - 87:5306 and 5313 (hfg);
  - 87:5685 (hfs);
  - 87:5920–5921 and 5927 (hft);
  - 87:6103 (hfq);
  - Step 1 of hfv through hfe, through "Step 1 uses only 𝔰_* < 𝔰₁^v" and the Σ_* argument of thm:tl5-hfy.
- **Steps 2 and 3 do not read the bound.** I checked this in the base proof, 87:4480–4510.
  - Step 2 uses |H| ≤ 𝔰 and 𝔧 ≤ (2k₁ + 4)𝒥₁ + 2k₂ϱ.
  - Step 3 uses 𝔰 ≤ C_∞μ^(−N/2)e^(φ/2)Y_s + …, that is Y_s itself.
  - The level-four S_M expansion uses 𝔍_g ≤ [𝔨₂]_t^(1/2)Y_s.
  - The ϱ terms use 𝔰₁^v. ✓
- **Both persistence lemmas.** The sites are 87:4518 and 4526 (lem:tl5-hf-persistence: "P(N) holds: ℰ⁰ ≤ μ^(−N)
  e^(Φ_o(u*)+Φ_i(v*)) 4A_w² and 𝔰 ≤ 𝔰_*") and 87:4878 and 4892 (lem:tl5-hf4-persistence, μ^(−4)… 4A_(w,4)²).
  - They use the bound through 𝔰 ≤ 𝔰_* (giving |H| ≤ 1/8 and θ_H) and through P(N). At level four the |D̂²Ψ_B| bound is
    an L² bound on faces, through ∫𝒥₁² ≤ [𝔨₂]_t times the face energy (87:4892–4894, and thm:tl5-hf4t, 87:5961–5964).
  - Their later uses are 87:5371–5372, 5393–5394, 5731, 5950 and 6129, and the "proofs of persistence use only |H| ≤ 1/8
    and θ_H ≤ ϑ" of thm:tl5-hfv (87:6244).
  - With Y_σ ≤ 𝔜, P(N) takes 𝔜² in place of 4A², and the smallness is 𝔰_*^c[𝔜] < 𝔰₁^v. ✓
- **The continuation.** The sites are 87:3500–3552, and the conclusions 87:4571, 4580, 4582 and 4979. These become
  lem:tl5-hfc-cont with 𝔜, and the conclusion Y_σ ≤ Y_c ≤ 2A_c.
- **Elsewhere.** 87:2493 (rem:tl5-wg-continuation) only says that the a priori bound must imply the strict tilt, which
  y ≤ 𝔜 does. No other site in chapter 87 reads the value 2A. I found no missed site. ✓

## 4. lem:tl5-hfc-h (P:39–58) holds

**The proof.**
- In the frame where ĝ = η, lem:tl5-wg-norms (a) (87:2071–2080) gives |H| ≤ 2|h| for |h| ≤ 1/2. Since |h| ≤ 𝔰 ≤ 𝔰_♭ ≤
  1/8, this gives |H| ≤ 2𝔰_♭.
- H = −g⁻¹hĝ⁻¹ follows from g⁻¹ − ĝ⁻¹ = −g⁻¹hĝ⁻¹.
- Raising an index with ĝ⁻¹ preserves the Frobenius norm, and H is submultiplicative. So |H| ≤ (1 + |H|)|h| ≤ (1 + 2𝔰_♭)
  |h| = 𝔤₁|h|.
- The same cost 1 + |H| ≤ 𝔤₁ is used at 87:5518 (lem:tl5-hfs-quadratic (a)) and 87:6240 (thm:tl5-hfv). ✓

**Each replaced site.** At every site the "2" is the factor of μ|H(p)| ≤ 2μ|h(p)| in the zeroth-order step, and
𝔰 ≤ 𝔰_♭ holds at p.

| Site | Where | Why the 2 is the H factor | Smallness at p |
|---|---|---|---|
| 87:5139, 5141, 5174 | lem:tl5-hfg-linfty | The entry 2C_S of C_∞^(m) bounds μ\|H\| via μ\|h\| ≤ C_Sℰ^(1/2) + C_(0,0)η₀ (87:5172–5174). The outer 2 is the absorption. | 𝔰 ≤ 𝔰₀^⋆ = min(𝔰_♭, …) on Q(a, b) ∋ p |
| 87:5557, 5576 | lem:tl5-hfs-linfty | 𝔰_P⁰ := max(μ\|H\|, μ^(..)\|Ψ_B\|), so 2C_S covers H, and C_S ≤ 𝔤₁C_S covers Ψ_B. | 𝔰 ≤ 𝔰₀^♮ ≤ 𝔰_♭ |
| 87:5655, 5712 | def:tl5-hfs-constants and Step 3 | 𝔎 and 𝔎₀ come from 𝔓 = max(𝔨_A𝔰_P⁰, 𝔨_B𝔰_P) and the Step-3 bound of 𝔰_P⁰. | After Step 1, 𝔰 ≤ 𝔰_* < 𝔰₁^♮ ≤ 𝔰_♭ on D^κ_s |
| 87:5868 | lem:tl5-hft-small (a) | "and \|H(p)\| ≤ 2\|h(p)\|" | 𝔰 ≤ 𝔰₀^♮ (part (b): 𝔰₀^μ) |
| 87:6044–6045 | lem:tl5-hfq-theta | "the factor 2 of \|H\| ≤ 2\|h\| is taken up by 2C_S and 2C_(0,0)" | 𝔰 ≤ 𝔰₀^q ≤ 𝔰_♭ |
| 87:6199–6200 | lem:tl5-hfv-rec | C_P^v = 2max(2C_S, C₁, 𝔨_rec): the entries are μ\|H\| (2C_S), Ψ_B (C_S), D̂Ψ_B (C₁) and D̂²h (𝔨_rec) of 𝔰_g^(0). | The setting of hfs-linfty or hft-small (b) |

From sec:tl5-hfy on, 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 ≤ 𝔰_♭/2 (87:6368). ✓

**The kept sites, all of them valid to keep.**
- 87:4323–4325 and their proof at 87:4345 (lem:tl5-hf-linfty) are proved under 𝔰 ≤ 𝔰₀ ≤ 1/8, with no 𝔰_♭.
- The 2 of 2𝒥_g in the absorption, at 87:5166–5169, 5885–5887 and 4338, comes from |H| ≤ 2|h| for Φ = H. It enters
  only through k₃𝔰, and through 𝔵 from sec:tl5-hfy on.
- 87:5211 is (∗) of lem:tl5-hfg-products. Its 𝔨_B is max(𝔷, 𝔤₁) at index v.
- 87:4491 is in the base Step 2.

**Missed sites.** I searched every "2|h", "|H| ≤ 2", "2C_S", "2C_(0,0)", "2𝒥" and "2μ|h". The remaining hits (87:4787,
5256, 5638 and 6078) are Minkowski factors 2𝒥_g², unrelated to H. Nothing that the index-l chain uses with |H| ≤ 2|h|
was missed, except the deliberately kept 2𝒥_g. ✓

## 5. The rest of the theorem, the definition and the Remark

- **The definition.** It replaces exactly these entries, in 𝔎, 𝔎₀ and everything formed from them. ε^c = ε^l, since ε
  carries no C_S.
- **The containment.**
  - 𝔤₁ ≤ 5/4 < 2, and the constants are nondecreasing in their entries.
  - Hence η_c ≥ η_l, A_c ≤ A_l, B_c ≤ B_l and 4A_cB_c ≤ 4A_lB_l < 1.
  - Y_c ≤ 2A_c, and 𝔰_*^c ≤ 𝔰_*^c[2A_c] ≤ 𝔰_*^l < 𝔰₁^v.
  - So the hypotheses of thm:tl5-hfe imply those of thm:tl5-hfc. ✓
- **The Remark.** Its statements are right. The sentence "at every point where a bound at a point is formed, 𝔰 ≤ 𝔰_♭
  holds" is meant within the chain from sec:tl5-hfg on. The base lemma lem:tl5-hf-linfty has no 𝔰_♭ and is kept, so
  the context makes this clear.

## 6. The Comparison

- **The site lists of items 1 and 2.** Every cited line number and quoted text matches 87 at 0563d28a.
- **Lever 1: A/A₀ = 2 − x₀ follows** from the stated assumptions:
  - the term of 𝔰_* with A binds before and after;
  - B is fixed;
  - A scales with the size that f and ϱ share;
  - the closing spare is read as x₀ = 4A₀B₀ = 10^(−spare), which follows from the same scaling, since the closing
    binds at A₀/x₀.
- **The derivation.**
  - From 2A/(1 + s) = 2A₀ with s = (1 − 4AB)^(1/2) and B fixed: A = A₀(1 + s) and 4AB = x₀(1 + s) = 1 − s².
  - So s = 1 − x₀, 4AB = 2x₀ − x₀², and A/A₀ = 2 − x₀.
  - The closing after the change sits at 2x₀ − x₀² < 1, so it does not bind. The text's "both bind after" is wrong
    (n2).
- **The numbers.**
  - Spares 0.09 / 0.24 / 0.30 give x₀ = 0.813 / 0.575 / 0.501 and +0.075 / +0.154 / +0.176 ✓.
  - At level 6, x₀ → 0 gives +0.30 ✓.
  - Lever 2 is log₁₀(2/𝔤₁) = 0.301 at 𝔰_♭ = 10⁻⁴ ✓.
  - The sum of the two levers is +0.37 / +0.45 / +0.48 ✓. As upper figures they add only if lever 2's rise in A is
    matched by a fall of S_F, so that the closing spare is not used up first. The Comparison's "upper figures" covers
    this.
- **The G0p figures.**
  - The interim optima −22.01 / −20.70 / −29.14 / −26.02 (level 4) and −32.01 / −28.82 / −40.54 / −34.82 (level 6) match
    G0p's interim logs (scratchpad/g0p/p_s*_N*_main.log).
  - G0p is interim, and its head report is not in the repository. Its margins 0.09 / 0.24 / 0.30, "83–100 % of the
    points" and the pending price "C_S ÷ 2" appear neither in G0p's head report nor in its logs, so I could not check
    them. The arithmetic built on them checks.
- **The level-6 sentence** "ϱ binds there and f is 0.02–0.5 above" does not match those logs.
  - At seed 1, ϱ binds, with f 0.05 above in D_A and 0.02 above in D*.
  - At seed 2, f binds, with ϱ 0.07 above in D_A and 0.02 above in D*.
  - 0.5 is G0o's figure (f 0.12–0.51 above ϱ, G0o.3).
  - The conclusion, about +0.30 for both, is unaffected (n3).
- **The assumption** "(its ϱ and η₀ terms 9.5–13 decades away, G0l)" is only half supported. G0l line 152 gives
  9.5–13 for the term of 𝔰_* with ϱ only (n1).

## 7. Findings (all nits)

**n1 (nit), Comparison P:227–228.**
- Text: "(its ϱ and η₀ terms 9.5–13 decades away, G0l)".
- Why: G0l reports the ϱ term only.
- Replacement (tested): "(its term with ϱ 9.5–13 decades away, G0l; its term with η₀ not reported)".

**n2 (nit), Comparison P:231–232.**
- Text: "If 𝔰_* binds before and both bind after".
- Why: the derivation itself puts the closing at 4AB = 2x₀ − x₀² < 1 after the change, so only 𝔰_* binds after.
- Replacement (tested): "If 𝔰_* binds before and after, … so 1 − (1 − x)^½ = x₀, x = 2x₀ − x₀² < 1 (the closing does
  not bind after) and A/A₀ = 2 − x₀."

**n3 (nit), Comparison P:235.**
- Text: "ϱ binds there and f is 0.02–0.5 above".
- Why: see §6.
- Replacement (tested): "at G0p's interim optima they lie within 0.02–0.07 of each other (ϱ binds at seed 1, f at
  seed 2), so both move by about +0.30."

## 8. The fixed copy

/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd14/P-GRD14.fixed.md

- md5 a5622bfa58e74fc9c6792db2be32680f, 267 lines.
- Made by /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/rpgrd14/tools/fix.py.
  Each old text occurs exactly once.
- P:1–226 is byte-identical to the original: the chapter text, the placement and the crosswalk rows are unchanged.
- Re-merged in a fresh tree, it passes every check:
  - item 2 found at 7503;
  - lint: 0 hits, 5320 labels;
  - check: 0 problems;
  - `[] 0`;
  - crosswalk: 9 of 9 rows at their labels, 469 = 469;
  - 0 existing numbers changed;
  - the notes have no line over 121 characters.

## Verdict

**CONFIRMED.** 0 Major, 0 minor, 3 nits, all in the Comparison.
- lem:tl5-hfc-cont is correct.
- The definition of Y_c is not circular.
- The continuity step and the choice of 𝔜 are valid.
- Every reader of the a priori bound takes 𝔜, and none was missed.
- lem:tl5-hfc-h holds at each of its sites.
- thm:tl5-hfc contains thm:tl5-hfe.
