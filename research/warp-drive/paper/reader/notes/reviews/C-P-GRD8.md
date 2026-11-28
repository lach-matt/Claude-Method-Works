# C-P-GRD8: confirming read of proofs/P-GRD8.md (the absorption with the bootstrap's smallness, sec:tl5-hfy)

**File read:** proofs/P-GRD8.md at bcf07954, md5 742cd674ea21447e282a24978464ea07, 96 lines:
- chapter text 1–47 (sec:tl5-hfy, 4 labels);
- Placement 49–69;
- Comparison 71–84;
- crosswalk rows 86–96.

**Review being confirmed:** notes/reviews/R-P-GRD8.md (on c0543b1e, md5 80431453…): NOT CONFIRMED, 0 Major, 3 minor (m1–m3), 1 nit (n1).

**Also read**, in chapter 87 at bcf07954 (md5 fda8b8aa…, 6344 lines):
- lem:tl5-hf-linfty (87:4306–4356);
- lem:tl5-hf4-mixed (λ_t and ς_t, 87:4762);
- prop:tl5-hf-bootstrap, Step 1 (87:4467–4476);
- lem:tl5-hfs-linfty (87:5545–5590);
- lem:tl5-hfs-products and lem:tl5-hfs-mixed (87:5592–5645);
- def:tl5-hfs-constants (87:5646–5675);
- lem:tl5-hft-small and lem:tl5-hft-products (87:5850–5905);
- lem:tl5-hfq-theta and lem:tl5-hfq-mixed (87:6030–6070);
- notes/reports/G0h.md (G0h.0, level 6).

I edited no repository file and committed nothing. All scratch work is under scratchpad/reader/cpgrd8/.

## Verdict in brief

All four changes (m1, m2, m3, n1) resolve their findings correctly and completely. None introduces a new error, and nothing outside the findings changed.

**m1:**
- The per-option list is right: lem:tl5-hfs-linfty is assigned to option (a) only, and option (b) and level four use lem:tl5-hft-small (b), lem:tl5-hft-products and lem:tl5-hfq-theta.
- Every listed replacement is valid in its own lemma: λ_t^(μ,2); ς_t, hence 𝔯_M and ε_M; C_(1,ϱ) with 32k₂² = 8(2k₂)²; the products' terms with ϱ; and so the coefficient of ε^w, 2𝔰₁^v → 𝔰₁^v/(1 − 𝔵).

**m2:** the list of what the smallness is used for is complete.

**m3:** every replaced factor gains at least log₁₀(2(1 − 𝔵)).

**n1:** the inclusion Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ is now stated.

**The continuity argument**, checked independently, is sound.

**Mechanical checks:** the merge gives lint 0, problems 0 and `[] 0`. No printed number of the 5250 old labels changes. The 4 crosswalk rows point at their labels.

No replacement is needed.

## What changed between c0543b1e and bcf07954

`git diff c0543b1e bcf07954 -- research/warp-drive/paper/reader/proofs/P-GRD8.md` has exactly these hunks, each the review's replacement text word for word:

| Hunk | Lines in bcf07954 | Finding |
|---|---|---|
| lemma statement, from "Q(a, b), then" | 13–21 | m1 |
| lemma proof | 23–30 | m2 |
| theorem statement, second line | 33–34 | m1 |
| theorem proof | 37–41 | m1, n1 |
| remark | 43–47 | m1, m3 |
| Comparison paragraph | 74–84 | m3 |
| crosswalk rows of thm:tl5-hfy and rem:tl5-hfy-what | 92–93 | renumbered |

**Nothing else changed.** The introduction, the lemma's first three lines and the Placement are byte-identical to the draft's.

## Mechanical checks (scratch merge)

**Scratch tree:** `git archive bcf07954 research/warp-drive/paper/reader`, extracted under scratchpad/reader/cpgrd8/tree. Chapter 87 and its crosswalk are byte-identical at 11a31701 (the Placement's HEAD) and bcf07954.

**Applying the Placement:**
- Item 2: its old text occurs exactly once, at 87:6343–6344. It replaces two lines by two, so rem:tl5-hfx-what still ends at **6344**, as item 1 says.
- Item 1: chapter-text lines 1–47 were appended there after one blank line.
- Crosswalk: the 4 rows were appended with `@PENDING:` → `@bcf07954:` (tools/merge.py).

**Results:**
- `python3 lint.py --chapters`: 62 files, 5254 labels, **0 hits**.
- `python3 assemble.py --check`: labels 5254, **problems 0**. PAPER.md was not rewritten; its md5 is unchanged.
- In-memory assembled check: prints **`[] 0`**.

**Numbering:** I compared assemble.number on the unmerged and merged trees.
- **None of the 5250 old labels changes its printed number.**
- sec:tl5-hfy is Section 57.23, lem:tl5-hfy-abs is Lemma 57.205, thm:tl5-hfy is Theorem 57.206 and rem:tl5-hfy-what is Remark 57.207.

**Crosswalk:**
- Each of the 4 rows' line holds its `{#label}`: lines 1, 10, 32 and 43.
- Appended, the file has a header and 403 rows, equal in order to the 403 labels of chapter 87.

**Paper rules on the changed chapter lines** (13–21, 23–30, 33–34, 37–41, 43–47):
- All are at most 120 characters, and so is every chapter-text line of the file.
- No line starts with "+ ", "- ", "* ", "> ", "#", "=" or "|". Line 23 starts with "*Proof.*", line 39 with "[1/2, s]".
- All 4 labels are lowercase.
- There are no file or program names and no code in the chapter text.

## The continuity argument, checked independently

Σ_* := {σ ∈ [1/2, s] : 𝔰 ≤ 𝔰₁^v on D^κ_σ}.
- **Start.** D^κ_(1/2) = S ⊂ N₀, and 𝔰 ≤ η₀ < 𝔰₁^v on N₀ ∩ D^κ_s by hypothesis (a), so 1/2 ∈ Σ_*.
- **Closed.** 𝔰 is continuous and the compact sets D^κ_σ increase with σ, as in the old Step 1 (87:4469–4470).
- **Open.** For σ ∈ Σ_* and p ∈ D^κ_σ, Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ (87:4470), so 𝔰 ≤ 𝔰₁^v on it and lem:tl5-hfy-abs gives the bounds at p with k₃𝔰 ≤ 𝔵. With ℰ_g(p) ≤ e^(φ(p))Y_σ² ≤ 4e^(φ(p))A² they give 𝔰(p) ≤ 𝔰_*. Hypothesis (c), 𝔰_* < 𝔰₁^v, is a strict gap uniform on D^κ_σ, and the uniform continuity of 𝔰 on D^κ_s extends 𝔰 < 𝔰₁^v to some D^κ_(σ′), σ′ > σ.

So Σ_* = [1/2, s] and 𝔰 ≤ 𝔰_* < 𝔰₁^v on D^κ_s. That is every point where Steps 2 and 3 use the lemma.

**What the old argument needed.** It needed only a strict gap between its bound and its hypothesis; the factor 1/2 between 𝔰₁ and 𝔰₀ was never used for openness.

**No circularity.**
- 𝔰₁^v = min(𝔰₀/2, c_*κ_m/2, 𝔰_(θ,v)) and k₃ are background numbers, so 𝔵 = 𝔰₁^v sup k₃ is one too.
- The replaced constants, ε^w (with 𝔰₁^v/(1 − 𝔵)), A and 𝔰_* follow in that order.
- After Step 1, |h| ≤ 𝔰 < c_*κ_m/2 and |H| ≤ 𝔰 < 𝔰_(θ,v) still give |h|_k̂ < κ_m/2 and θ_H ≤ ϑ, as before.

## m1 — the scope and the list of replacements (lines 13–21, 33–34, 37–41): RESOLVED

### Which lemmas hold, per option

**𝔵 ≤ 1/4 in every option.** k₃ and 𝔰₀ are formed with the same constant: k₃^♮ and 𝔰₀^♮ (87:5652), k₃^♮(μ) and 𝔰₀^μ (87:5912), k₃^♮(ν) and 𝔰₀^q (87:6087). Each 𝔰₀ is ≤ 1/(2 sup_(D^κ) k₃), so 𝔰₁^v ≤ 𝔰₀/2 gives 𝔵 ≤ 1/4.

**Option (a)** (N ≥ 6, k₃ = k₃^♮). 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀^♮/2 satisfies the hypothesis 𝔰 ≤ 𝔰₀^♮ of lem:tl5-hfs-linfty, of lem:tl5-hft-small (a) and of lem:tl5-hfs-products. These are the lemmas that Steps 1–3 of option (a) use (87:5690–5694, 5927).

**Option (b)** (k₃ = k₃^♮(μ)). 𝔰₁^v ≤ 𝔰₀^μ/2, but it need not be ≤ 𝔰₀^♮, since k₃^♮(μ) ≤ k₃^♮. So lem:tl5-hfs-linfty, whose absorptions use k₃^♮, is not available. The chapter uses lem:tl5-hft-small (b) and lem:tl5-hft-products in its place (87:5933), and the list now says exactly that.

**Level four** (k₃ = k₃^♮(ν)).
- "these" after the semicolon refers to the lemmas of option (b), which agrees with thm:tl5-hf4q's proof ("The proof of [[thm:tl5-hf4t]] in option (b) applies").
- The other lemmas there are lem:tl5-hfq-theta, lem:tl5-hfs-mixed (as given by lem:tl5-hft-products) and lem:tl5-hfq-mixed.
- lem:tl5-hfq-theta needs 𝔰 ≤ 𝔰₀^q, which holds, and it applies lem:tl5-hft-small (b), since k₃^♮(μ) ≤ k₃^♮(ν).

**lem:tl5-hfv-rec** (level four) and **lem:tl5-hfx-c1** hold in each setting.

The theorem uses only the lemmas of the chosen set, so the list is the right scope.

### Each replacement, checked in its own lemma

- **eq:tl5-hfs-m2 and M_g^(j).** M ≤ k₁𝒥 + k₂ϱ + k₃𝔰(2𝒥 + M) (87:4336–4339), with k₃(q)𝔰(q) ≤ 𝔵 at every point of Q(a, b). This gives M(1 − 𝔵) ≤ (k₁ + 2𝔵)𝒥 + k₂ϱ.
  - In the induction (87:5563–5573), R_C := ((k₁^(j,μ) + 2𝔵)X + k₂ϱ)/(1 − 𝔵) with X = μ^(−(|C|+1)/2)𝒥_g satisfies k₁X + k₂ϱ + 𝔵(2X + R_C) = R_C exactly.
  - The 2 in 2𝒥 comes from 𝔧 ≤ 2𝒥 + M, that is from |H| ≤ 2|h|, and is rightly kept.
- **eq:tl5-hfq-m2** (87:6034–6043). The part with 𝒥_g absorbs with k₃^♮(μ)𝔰 ≤ 𝔵 and the part with ϱ with k₃^♮(ν)𝔰 ≤ 𝔵. They close separately as (k₁^(j,μ) + 2𝔵)X/(1 − 𝔵) and k₂ν^(−(|C|+1)/2)ϱ/(1 − 𝔵).
- **𝔨_A := 2k₁^μ + 2** (87:5594) enters through |Φ₂| ≤ 𝔨_Aμ^(−ℓ_E/2)𝒥_g + 2k₂ϱ by eq:tl5-hfs-m2, and so does the products' ϱ term. Both are replaced, giving the ϱ term (k₂/(1 − 𝔵))𝔰ϱ.
- **λ_t^μ := 2([k₁^μ]_t + 1)** (87:5616) and **λ_t^(μ,2) := 2([k₁^(2,μ)]_t + 1)** (87:6067) come from ‖M_g^(3)‖_Σ and from M_g^(2) (lem:tl5-hft-small (b), j = 2). The supremum commutes with the increasing affine map, giving ([k₁^·]_t + 2𝔵)/(1 − 𝔵).
- **ς_t := 2[k₂]_t(∫ dμ dτ₂/(1 − κκ′))^(1/2)** (87:4762) is the face norm of the 2k₂ϱ part of M_g, so it becomes [k₂]_t/(1 − 𝔵)(…)^(1/2). It enters 𝔛′_(2,t) and 𝔜′_(1,t) (87:5621–5622), hence 𝔯_M and ε_M.
- **C_(1,ϱ).** In the first-order step, |D̂ℒ^J A|² ≤ 2M₂² + 2·72Λ²𝒥² and M₂² ≤ 2(2(k₁ + 1)𝒥)² + 2(2k₂ϱ)², and the Sobolev form contributes the factor 2|∂_γ|². So C_(1,ϱ)²'s 32|∂_γ|²k₂² is 2|∂_γ|²·2·2·(2k₂)², that is 32k₂² = 8(2k₂)². With 2k₂ → k₂/(1 − 𝔵) it becomes 8k₂²/(1 − 𝔵)². This holds in each first-order step that forms C_(1,ϱ): lem:tl5-hf-linfty, lem:tl5-hfs-linfty, lem:tl5-hft-small (a) and (b), and lem:tl5-hfq-theta with ν.
- **C₁^x.** In the second entry, 2·43^(1/2)(k₁^μ + 1) comes from the maximum bound of D̂²Ψ_(JB), and it becomes 43^(1/2)(k₁^μ + 2𝔵)/(1 − 𝔵).
- **ε^w.** The products' ϱ term is now (k₂/(1 − 𝔵))𝔰ϱ, and P-GRD6's step 2k₂𝔰ϱ ≤ 2𝔰₁^v k₂ϱ becomes k₂𝔰ϱ/(1 − 𝔵) ≤ 𝔰₁^v k₂ϱ/(1 − 𝔵), using 𝔰 < 𝔰₁^v after Step 1. So ε^w = 𝒮[s_N[2R̂ic] + (𝔰₁^v/(1 − 𝔵))𝔤_ϱ^v k₂ϱ]. At level four both routes of 𝔤_ϱ^v = min(𝔤_(ϱ,q), μ^(−1/2)𝔤_(𝒥,s)) carry the same 2k₂𝔰ϱ, so the minimum survives. The theorem's statement and proof (lines 33–34, 40) say this.
- **The outer factor 2 of the maxima.** C_∞^(m), C_(∞,ϱ)^(m) and C_(∞,0)^(m) (87:5139–5141), their weighted forms, and C_P^v, C_(P,ϱ)^v and C_(P,0)^v (lem:tl5-hfv-rec): from 𝔰 ≤ m + 𝔵𝔰, 𝔰 ≤ m/(1 − 𝔵). The t-argument gives t ≤ 1/(1 − 𝔵).
- **Not replaced, rightly:**
  - the inner 2C_S and 2C_(0,0), which come from |H| ≤ 2|h|;
  - (2𝔐)^(1/2);
  - the k₂ of C_(∞,ϱ) and of 𝔨_rec^ϱ + k₂, the recovery's own residual term;
  - the 4|∂_γ|² of C₁^x.

**Containment.** Each new factor is at most the old one, since 𝔵 ≤ 1/4: for example, (k₁ + 2𝔵)/(1 − 𝔵) ≤ 2(k₁ + 1) is k₁(1 − 2𝔵) + 2 − 4𝔵 ≥ 0. So thm:tl5-hfy contains thm:tl5-hfx.

## m2 — what the smallness is used for (lines 23–30): RESOLVED

**The three uses.** 𝔰 ≤ 𝔰₁^v ≤ 𝔰₀/2 ≤ 𝔰_♭/2 ≤ 1/16 keeps:
- 𝔰 ≤ 𝔰_♭, in the expansions with 𝔠^♮ (eq:tl5-hfs-sum);
- |H| ≤ 1/8, as |H| ≤ 𝔰, which gives the factor 6/5 of the recovery (87:4336);
- 𝔰 ≤ 1, in the powers 𝔰^(q−2).

**The absorptions.** They carry the k₃ of the chosen set; at level four the part with 𝒥_g carries k₃^♮(μ) ≤ k₃^♮(ν). The sentence "the bounds that use them (of the products, of ‖M_g‖_Σ and of the first-order step) follow with the replaced coefficients" covers the m1 list.

The old claim "used only through k₃𝔰 ≤ 1/2" is gone.

## m3 — the gain and 𝔵 (lines 43–47; Comparison 74–84): RESOLVED

**The gain.** For each replaced factor the ratio old/new is at least 2(1 − 𝔵):
- 2(k₁ + 1)(1 − 𝔵)/(k₁ + 2𝔵) ≥ 2(1 − 𝔵), since 2𝔵 ≤ 1;
- the ratio is exactly 2(1 − 𝔵) for 2k₂, for the outer 2, for ς_t, for C_(1,ϱ) (whose square falls by 4(1 − 𝔵)²) and for the coefficient of ε^w.

So "each new factor is at least 2(1 − 𝔵) times smaller" is right, and log₁₀(2(1 − 𝔵)) is 0.176 at 𝔵 = 1/4 ("0.18 decades") and tends to log₁₀2 = 0.301 as 𝔵 → 0. At 𝔵 = 1/4 the replacements are (k₁ + 1/2)/(3/4) = (4/3)(k₁ + 1/2), (4/3)k₂ and 4/3.

**The values of 𝔵.** G0h.0 at level 6 gives 𝔰₁^v = 4.0 × 10⁻⁵, 1.7 × 10⁻⁵ and 1.9 × 10⁻⁶ "(1/(4k₃^♮(μ)))", where 𝔵 = 1/4 exactly. At the fourth point the cap, 1.4 × 10⁻⁵ against 1/(4k₃) = 1.8 × 10⁻⁵, gives 𝔵 = 1.4/(4·1.8) = 0.19. So "𝔵 ≪ 1" is gone, rightly.

The new list "Replaced everywhere" matches the lemma.

## n1 — Q(τ₁(p), τ₂(p)) ⊂ D^κ_σ (line 37): RESOLVED

This is now stated, as in the old Step 1 (87:4470), and it is what makes the lemma's hypothesis "𝔰 ≤ 𝔰₁^v on Q(a, b)" hold at p.

## Observations (no change required)

- **C₁^♮.** It is the first entry of C₁^x and contains the bound of D̂²Ψ through 4|∂_γ|²·8(k₁^μ + 1)² = 4|∂_γ|²·2(2(k₁^μ + 1))². The general clause ("wherever these bounds enter") lets it become 4|∂_γ|²·2((k₁^μ + 2𝔵)/(1 − 𝔵))², and the Comparison's "(In C₁: the "factors 2·2" item loses one 2…)" reads it so. The lemma's explicit list names only the second entry. Both readings give valid bounds, and the minimum of C₁^x makes the difference immaterial at the evaluation's values.
- **Notation.** The new 𝔵 shares its letter with the Sobolev quantities 𝔵_r(t) of lem:tl5-hf4-face. At level four both now occur in 𝔛^q_(2,t), through λ_t^μ. The subscript and argument distinguish them, so a rename is optional.
- **"could be summed."** The Comparison's "Not done" sentence is speculative. An ℓ² absorption over the 43 words would need more than 𝔵 ≤ 1/4, since √43/4 > 1. The R-P-GRD8 reviewer noted this too.

## Scratch artefacts

All paths are under /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/cpgrd8/:
- tree/: the merged copy at bcf07954;
- orig/: the unmerged archive;
- tools/merge.py: applies the Placement and appends the crosswalk rows;
- 87.md: chapter 87 at bcf07954;
- grd8.diff: the diff.

Verdict: CONFIRMED
