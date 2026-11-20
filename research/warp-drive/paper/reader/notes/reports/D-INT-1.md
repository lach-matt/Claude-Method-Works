# D-INT-1: chapter changes for the integration of the bound on d

**Baseline and diff.** The baseline is b1b87ba8, HEAD when I started. The snapshot commits d1509feb and 04e80763 picked
up my edits, so I took the diff against b1b87ba8: scratch/d_int_1/d_int_1.diff (444 lines, 111+/80−). It touches only my
eight files, and chapters/ and crosswalk/ differ from b1b87ba8 nowhere else. Texts 7, 8 and 12 are unchanged at HEAD.

## 1. CH-43

- 43:303–327 is R-DB-2's lem:iii-j2-2-4, statement and proof, verbatim.
- Uses checked in place: lem:iii-j2-2-1 (b) (43:186–189), prop:iii-j2-4-3 (proof, 43:~462), cor:iii-j3-6-6 (43:~1077)
  and 44:671. Each absorbs the loss (d free or fixed; ‖β‖_(d_0) small covers δ_Θ), so none changed.
- Checked against lem:ii-g-4-1 (2)–(3): d = 3 > 5/2 and > 4/2, and the factor at k + 3.

## 2. CH-46

- (a) 46:1247–1249: (d) now says "there is s_P > 0 such that … ≤ C_kω_(k+3)(…H^(k+3+k′_(k+3))) when … ≤ min(s_(k+3), s_P)".
- (b) 46:1288–1295: the proof, with s_P ∈ (0, s_3].
- (c) 46:1469–1471: the Smallness paragraph, with ω_(2d+3) and min(s_(2d+3), s_P).
- These are R-DB-2's texts, rewrapped. They match the s̃ of prop:ec-delta-cap and the monotonicity in prop:iii-k-1-2 (3).
  48:240 stays true.

## 3. Texts 7, 8, 12

- Text 7: 23:1466–1471, appended to prop:ii-a1-2-4's first paragraph.
- Text 12: 23:1071–1072, a paragraph after (b) of lem:ii-a-8-5.
- Text 8: 25:29–30, the notation paragraph, "N′ is a fixed integer with N′ ≥ −inf 𝗌_0 … (N′ = 13 …)".
- All three are verbatim. The numbers M = 200Θ + 98 and d_0 = 200Θ + 100 agree with prop:fwd-calculus (M + 2 = 200T +
  100).

## 4. CH-3

- 03:351–356: the constants bullet is R-DB-2's text, verbatim.
- I-1's μ̇ item needs nothing. Chapter 3 already writes ṁ (03:344–348), for the same quantity as 64:69–70 ("ṁ its mass
  change"). No μ̇ remains in chapter 3, and crosswalk/03 already has rem:envelope-regularity.

## 5. CH-90

- (a) 90:56: "λ1 < δ ≤ 2^(−(32d+9))".
- (b) 90:60–70: R-DB-2's paragraph, which replaces the marker. It says what is bounded (d = d_NM, and N_NM), by which
  integer bounds (below 1.57157 × 10⁵⁰ and 3.30029 × 10⁵¹), with which key ([[thm:uc-integer]]) and at which weights (one
  admissible choice), against the lower bounds.
- **Departure.** R-DB-2's "d > 1.2497 × 10²⁴ for the index sets as the proofs construct them" is now "d > 1.2497 × 10²⁴
  and N_NM > 2.624 × 10²⁵ at every admissible choice of the weights, for the index sets as the proofs construct them".
  This is exactly cor:uc-two-offsets (a)+(b). It makes the every/one contrast explicit and adds the N_NM bound that
  W-90 lists.

## 6. Abstract and chapter 1

- 00:32–34: "…an upper bound for λ0 at a numerical point and, at a parameter point outside the set on which settling is
  proved, for one choice of the weights, 1.2497 × 10²⁴ < d < 1.57157 × 10⁵⁰ for the loss d with which the settling proof
  applies the Nash–Moser theorem;". The abstract goes from 508 to 533 words.
- 01:149–155, the Scope paragraph: chapter 71 also "bounds the loss d … at a point of the gauge and damping parameters
  outside the set on which that theorem is proved: there d > 1.2497 × 10²⁴ at every admissible choice of the weights,
  and d < 1.57157 × 10⁵⁰ at one ([[thm:uc-integer]])".
- Left as they are: 01:68 and 01:182–183 are true as general statements, and 01:116 concerns another loss.

## 7. I-2

- Chapter 25: all 48 sites of 𝓗 (U+1D4D7) are now ℋ (U+210B), and nothing else changed. Every site is the horizon: 𝓗⁺,
  ∂R_(𝓗⁺), ϑ_𝓗 of eq:i-a-1-5, R_𝓗 (chapter 24's R_ℋ := ∂R_(ℋ⁺)), V_𝓗 and 𝒳_𝓗. None is a Hilbert space, and chapter 25
  had no ℋ before.
- 23:361: "compact interval" is now "compact set". The source (arXiv:2606.28008v1, p. 49) reads "Given I ⋐ ℝ", after
  "fixed compact subset I ⊂ ℝ".

## Keys that resolve after the merge

- thm:uc-integer (01:153, 03:354, 90:68).
- cor:uc-two-offsets (90:65).
- prop:fwd-calculus (23:1072, 23:1470).

All three are in proofs/.

**Until the merge, chapters 3 and 90 disagree with chapter 71.** They now state the proofs/ forms of thm:loss-d and
prop:ec-delta-cap: 1.403 × 10²⁰, δ ≤ 2^(−(32d+9)) and log₁₀ δ < −1.351 × 10²¹. Chapter 71 still prints 7.959 × 10¹⁵
(71:487), and at 71:521–531 a prop:ec-delta-cap with ω_(2d) and s_(2d). That proposition no longer matches the new (d)
of chapter 46, and CH-71 (a) removes it.

## Checks

- `lint.py --chapters`: the 90:66 marker is gone, with no style, length or prefix hits. **6 hits remain**, all
  "undefined label" on the three merge keys. They clear at the merge, not before, so "0 hits" is not reached yet.
- `assemble.py --check`: 4406 labels. The 6 problems are the same references.
- Every line is at most 121 characters, and no wrapped line starts with a listed prefix.
- No label changed, so no crosswalk was touched.
