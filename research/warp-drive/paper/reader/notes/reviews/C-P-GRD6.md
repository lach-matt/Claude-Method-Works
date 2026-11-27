# C-P-GRD6: confirming read of proofs/P-GRD6.md (the terms with ϱ, sharpened, sec:tl5-hfw)

**File read:** proofs/P-GRD6.md at 30025949 (branch ccr-af9edcf6-9a60sz), md5 4a08f9e37e0e33b4d15dd1b6b781963a, 103 lines:
- chapter text 1–41 (sec:tl5-hfw, 6 labels);
- Placement 43–68;
- Comparison 70–89;
- crosswalk rows 91–103.

**Review being confirmed:** notes/reviews/R-P-GRD6.md (on b8d033b5, md5 6f10eb9c…): NOT CONFIRMED, 0 Major, 3 minor (m1–m3), 2 nits (n1, n2).

**Also read:**
- in chapter 87 at 30025949 (md5 78dd5c4b…, 6254 lines):
  - eq:tl5-hf-source and prop:tl5-hf-linear (87:3863–3882);
  - def:tl5-hf-constants (87:4431–4452: ϱ, η₀ and ε_w);
  - prop:tl5-hf-bootstrap, Steps 1–3 (87:4455–4510);
  - def:tl5-hf4-constants and the M-term step of prop:tl5-hf4-bootstrap (87:4812–4875);
  - ε_(M,g) (87:5292) and def:tl5-hfs-constants (87:5646–5675);
- notes/reports/G0g.md (G0g.0) and notes/reports/G0h.md (G0h.0 and the addendum G0h.rule).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd6/.

## Verdict in brief

All five changes (m1–m3, n1, n2) resolve their findings correctly and completely. None introduces a new error, and nothing outside the findings changed.

- **m2:** the terms 𝔑^M_I are now correctly excluded. The forcing term and the ϱ part are bounded together into Y_s ε^w, as the merged Step 3 does, and 𝔰_*^w stands where Step 1 gives it.
- **m3:** the remark now names every place the residual enters. 𝒮 as defined at eq:tl5-hf-source is subadditive and positively homogeneous.
- **m1:** every figure in the new size paragraph agrees with G0g and G0h.
- **The central step:** 𝔰 ≤ 𝔰_*^w < 𝔰₁^v holds on all of D^κ_s before Step 2 uses it, and it comes from the hypothesis alone.
- **Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5239 old labels changes. The 6 crosswalk rows point at their labels.

No replacement is needed.

## What changed between b8d033b5 and 30025949

`git diff b8d033b5 30025949 -- research/warp-drive/paper/reader/proofs/P-GRD6.md` has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in 30025949 | Finding |
|---|---|---|
| introduction | 3–8 | m2 |
| proof of thm:tl5-hfw, from "in Step 2." | 26–33 | m2 |
| rem:tl5-hfw-what | 35–41 | m3 |
| Placement item 1 | 53 | n1 |
| Comparison, closing condition | 74–75 | n2 |
| Comparison, the size paragraph | 79–84 | m1 |
| Comparison, the briefed items' last sentence | 88–89 | m3 |
| crosswalk rows from def:tl5-hfw-constants on | 96–100 | renumbered by +1, +2 |

**Nothing else changed.** The definition, the theorem's statement and the Placement's item 2 are byte-identical to the draft's. The same commit also adds notes/reviews/R-P-GRD6.md and files under rule/, which are not merged text.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive 30025949 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd6/tree. Chapter 87 and its crosswalk are byte-identical at cb200e34 (the Placement's HEAD) and 30025949, so the quotations are current.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:6253–6254. After the replacement, rem:tl5-hfv-what ends at line **6255**.
- Item 1: chapter-text lines 1–41 were appended there after one blank line.
- Crosswalk: the 6 rows were appended with `@PENDING:` → `@30025949:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5245 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5245, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5239 old labels changes its printed number.**
- The new labels are numbered as follows:
  - sec:tl5-hfw is Section 57.21;
  - def:tl5-hfw-constants is Definition 57.199;
  - thm:tl5-hfw is Theorem 57.200;
  - rem:tl5-hfw-what is Remark 57.201;
  - the displays are (57.144) and (57.145).

**Crosswalk:**
- Each of the 6 rows' line holds its `{#label}`: lines 1, 10, 14, 18, 21 and 35.
- Appended, the file has a header and 394 rows, equal in order to the 394 labels of chapter 87.

**Paper rules on the changed chapter lines** (3–8, 27–33, 35–41):
- All are at most 120 characters. The longest chapter-text line in the file is 121 (line 21, unchanged).
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Line 28 starts with "√e_i):" and line 33 with "Y_s".
- All 6 labels are lowercase.
- There are no file or program names and no code in the chapter text.
- Lines 33 and 41 are short source lines, which is cosmetic.

## The central step, checked independently: 𝔰 < 𝔰₁^v on all of D^κ_s when Step 2 uses it

**How the theorem runs.** thm:tl5-hfw runs the proof of thm:tl5-hfv, which applies the a priori estimate to a solution on D^κ_s with Y_σ ≤ 2A_w^v for every σ ∈ [1/2, s]. The estimate is prop:tl5-hft-bootstrap or prop:tl5-hfq-bootstrap, built on prop:tl5-hf-bootstrap.

**Step 1** (87:4467–4476, reused at every level).
- Σ_* = {σ : 𝔰 ≤ 𝔰₀ on D^κ_σ} contains 1/2, since 𝔰 ≤ η₀ < 𝔰₁ on N₀, and it is closed.
- It is open: at p ∈ D^κ_σ the low-quantity bound with ℰ ≤ e^(φ(p)) Y_σ² ≤ 4e^(φ(p)) A² gives 𝔰(p) ≤ 𝔰_* < 𝔰₁ ≤ 𝔰₀/2.
- So Σ_* = [1/2, s], and **𝔰 ≤ 𝔰_* on D^κ_s**.
- In thm:tl5-hfw, A is A_w^v and 𝔰_* is 𝔰_*^w, "𝔰_*^v with A_w^v in place of A_v" (line 16). So Step 1 gives 𝔰 ≤ 𝔰_*^w < 𝔰₁^v at every point of D^κ_s, using only the assumed bound on Y and hypothesis (c).

**Step 2** applies the energy identity on Q(a′, b′) with a′ ≤ u* and b′ ≤ s, so Q(a′, b′) ⊂ D^κ_s (87:4479, 4505). The products lemmas are used at points of D^κ_s with ϱ(p) ≤ ϱ. So the bound 2k₂𝔰ϱ ≤ 2𝔰₁^v k₂ϱ is available at every point where Step 2 uses it.

**No circularity.**
- 𝔰₁^v = min(𝔰₀/2, c_*κ_m/2, 𝔰_(θ,v)), with 𝔰₀ = 𝔰₀^♮, 𝔰₀^μ or 𝔰₀^q, depends on background quantities and ϑ₁, ϑ₂ only.
- ϱ and η₀ are numbers: the sups of lem:tl5-hf-linfty at τ₁ = u*, τ₂ = v* (87:4433).
- So ε^w, then A_w^v, then 𝔰_*^w are defined in that order, and 𝔰_*^w < 𝔰₁^v is a condition, not a fixed point.

**Step 3** closes as before: the strict improvement Y_s ≤ A + BY_s² gives Y_s < 2A for the continuation.

## m2 — the terms 𝔑^M_I, the forcing term, 𝔰_*^w (lines 3–8, 26–33, chapter text): RESOLVED

**The exclusion of 𝔑^M_I.** At level four the terms 𝔑^M_I are bounded separately in every form of the bootstrap: by S_M Y_s³ + 𝔯_M Y_s² + ε_M Y_s. Their ϱ enters only 𝔯_M and ε_M; S_M has none. I checked each form:

| Form | Where | ϱ in 𝔯_M | ϱ in ε_M |
|---|---|---|---|
| unsharpened | 87:4817–4818, 4866–4867 | (2ϱ + η₀) | μ²ϱ(ϱ + η₀) |
| sharpened | 87:5292 | — | ε_(M,g) |
| second sharpening | 87:5669–5671 | ϱ terms | ϱη₀ |
| fourth sharpening | 𝔯_(M,q), ε_(M,q) | as in the second | as in the second |

So the parenthesis "(at level four, of those other than the terms 𝔑^M_I, whose parts with ϱ go into 𝔯_M and ε_M)" is exact in every form. "the nonlinear terms of level j other than 𝔑^M_I" and "the terms 𝔑^M_I are bounded as there" match the merged proofs ("other than 𝔑^M_I", 87:5321, 5698). ε_M^v keeps its old coefficient in A_w^v, as the definition says. At N ≥ 6 the M terms are 0.

**The ϱ part of the remaining terms.** It always carries a factor bounded by 𝔰. In the products lemmas the ϱ term of a monomial with q ≥ 2 solution factors is (background norm)·𝔰^(q−1)·(weights)·2k₂ϱ, with 𝔰^(q−2) absorbed by eq:tl5-hfs-sum. In H^(αβ)D̂_αD̂_βΨ_J it is |H|·2k₂ϱ with |H| ≤ 𝔰. Every Step 2 writes 2k₂𝔰ϱ and then uses 𝔰 ≤ 1/8:
- B_j at 87:5698–5703;
- option (b) of prop:tl5-hft-bootstrap;
- both routes of the minimum in prop:tl5-hfq-bootstrap.

Replacing 𝔰 by 𝔰₁^v therefore preserves the minimum 𝔤_ϱ^v = min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s)).

**The forcing term together with the ϱ part.** In Step 2 the bulk is ∫ e^(−φ)(2Ω̂²(s_N[2R̂ic] + (1/4)𝔤k₂ϱ)(√e_o + √c√e_i) + …) (87:4502). Step 3 bounds that first term "as in prop:tl5-hf-linear by Y_s ε_w" (87:4506): it is a single source s in eq:tl5-hf-hyp, so Y ≤ Y_d + 𝒮[s].

The new sentence, "this part together with the forcing term 2Ω̂² s_N[2R̂ic] (√e_o + √c √e_i) is bounded by Y_s ε^w", is exactly that, with s = s_N[2R̂ic] + 2𝔰₁^v𝔤_ϱ^v k₂ϱ and 𝒮[s] = ε^w. The draft bounded the two parts separately, which gives only 𝒮[s_N] + 𝒮[ϱ part] ≥ ε^w. The slip the review noted is closed.

**𝔰_*^w.** The introduction now says "After Step 1 of the proof of [[thm:tl5-hfw]], 𝔰 is at most 𝔰_*^w < 𝔰₁^v". That is the quantity this section's Step 1 bounds (see the central step), and it agrees with the proof (line 26). "a solution factor bounded by 𝔰" replaces the looser "a factor 𝔰 of the solution".

## m3 — the remark and the Comparison's "only the sum" (lines 35–41, 88–89): RESOLVED

**Where the residual enters**, which is the remark's first sentence:
- ε^w carries s_N[2R̂ic] and ϱ.
- ε_M^v carries ϱ, through ϱη₀ or ϱ(ϱ + η₀).
- 𝔯^v carries ϱ, through the C_(P,ϱ)ϱ and 𝔎_ϱϱ of 𝔟_(o,s) and 𝔟_(i,s) (87:5657–5658) and the ϱ terms of 𝔯_(M,q). So η = 1 − max(ϑ₁, ϑ₂) − 𝔯^v carries it too.
- 𝔰_*^w carries ϱ through C_(∞,ϱ)ϱ or ν^(−2)C_((∞,ϱ),ν)ϱ, and through A_w^v.
- (a), (b), δ_w, B_v and S_F^v, S_M^v contain no residual.

So "through ε^w and ε_M^v, and through ϱ also in 𝔯^v, and so in η, and in 𝔰_*^w" is complete and correct.

**𝒮 is subadditive and positively homogeneous.**
- eq:tl5-hf-source (87:3876) defines 𝒮 := ∫_(−10)^a ‖2Ω̂² s‖_(1,t) dt + ∫_(1/2)^b ‖2√c Ω̂² s‖_(2,t) dt, with ‖f‖²_(1,t) := ∫_(Σ₁(t,b)) e^(−φ) f² dμ dτ₂/(1 − κκ′) and the like for ‖·‖_(2,t). These are weighted L² norms on the faces.
- For bounded measurable s₁, s₂ ≥ 0 and a constant λ ≥ 0, Minkowski's inequality on each face gives ‖s₁ + s₂‖ ≤ ‖s₁‖ + ‖s₂‖, and ‖λs‖ = λ‖s‖. The outer integrals are linear and monotone. Hence 𝒮[s₁ + s₂] ≤ 𝒮[s₁] + 𝒮[s₂] and 𝒮[λs] = λ𝒮[s]; 𝒮 is also monotone.

**The bound.** ϱ and 𝔰₁^v are numbers, so ε^w = 𝒮[s_N[2R̂ic] + 2𝔰₁^v𝔤_ϱ^v k₂ϱ] ≤ 𝒮[s_N[2R̂ic]] + 2𝔰₁^vϱ 𝒮[𝔤_ϱ^v k₂], as stated.

**Monotonicity.** A_w^v increases with ε^w, so do 𝔰_*^w and the left side of eq:tl5-hfw-closing, and no other hypothesis involves ε^w. So "the hypotheses hold whenever they hold with ε^w replaced by this sum" is right, and so is the conclusion that the theorem fixes no ratio.

**The coefficient.** On the same bound the coefficient of ϱ for ε^v is (1/4)𝒮[𝔤_ϱ^v k₂], so the ratio is 2𝔰₁^v/(1/4) = 8𝔰₁^v. Also 𝔰₁^v ≤ 𝔰₀/2 ≤ 𝔰_♭/2 ≤ 1/16, since 𝔰_♭ ∈ (0, 1/8].

**Comparison 88–89.** "in ε^w the theorem needs only the sum, but ϱ also enters 𝔯^v (so η), 𝔰_*^w and ε_M^v, which this section leaves as they are" now agrees with the remark.

## m1 — the size estimate (Comparison 79–84): RESOLVED

**Figures checked against the reports:**
- **G0h.0, level 4** (G0h.md line 60): 𝔰₁^v = 2.0 × 10⁻⁵, 5.9 × 10⁻⁶, 1.4 × 10⁻⁵ and 4.5 × 10⁻⁶, each "(the cap)", in the column order seed 1 D_A, seed 2 D_A, seed 1 D*, seed 2 D*.
- **G0g.0** (G0g.md line 48, same order): 𝔰₁^q = 8.3 × 10⁻⁶, 1.3 × 10⁻⁶, 4.5 × 10⁻⁶ and 1.8 × 10⁻⁶.
- **−log₁₀(8𝔰₁):**
  - at G0h's values: 3.80, 4.33, 3.95 and 4.44, that is 3.8, 4.3, 4.0 and 4.4;
  - at G0g's values: 4.18, 4.98, 4.44 and 4.84, that is 4.2, 5.0, 4.4 and 4.8.
- **The room:** G0h's addendum (G0h.md line 270, "room: best f − max-min") gives 1.9, 2.2, 2.6 and 3.3. Each decade of the ϱ coefficient raises min(f, ϱ) by about one until f binds (G0h.md lines 272–275).

**The conclusion.** Since 3.8 > 1.9, 4.3 > 2.2, 4.0 > 2.6 and 4.4 > 3.3, "so that there f binds again" follows. The closing caveat is accurate: G0h.0's points are f-optimal, and the addendum's max-min points have other θ and μ, with 𝔰₁ not listed.

The draft's "10⁻¹⁵…10⁻¹⁸ … 14–17 decades" is gone.

## n1 — the Placement's line reference (line 53): RESOLVED

"(line 6255 once item 2 is applied)": after item 2 the last line of rem:tl5-hfv-what is 87:6255. I checked this on the scratch merge.

## n2 — η > 0 in the Comparison (lines 74–75): RESOLVED

The Comparison's list now has "η > 0", as in hypothesis (c) of thm:tl5-hfw (line 19).

## Observations (no change required)

- The definition is unchanged, and its three choices of 𝔤_ϱ^v are the factors of (1/4)k₂ϱ in ε_(w,s), in ε_(w,t) option (b) and in ε_(w,q). eq:tl5-hfw-closing is 4A_w^vB_v.
- thm:tl5-hfw contains thm:tl5-hfv: 2𝔰₁^v ≤ 1/8 < 1/4 gives ε^w ≤ ε^v, A_w^v ≤ A_v and 𝔰_*^w ≤ 𝔰_*^v.
- The short source lines 33 and 41 are cosmetic.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd6/:
- tree/: the merged copy at 30025949;
- orig/: the unmerged archive;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- 87.md: chapter 87 at 30025949;
- grd6.diff: the diff.

Verdict: CONFIRMED
