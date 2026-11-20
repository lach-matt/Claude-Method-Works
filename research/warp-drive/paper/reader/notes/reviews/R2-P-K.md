# R2-P-K: confirming reading of proofs/P-K.md (md5 e38d85b60ed9a392d9f143d944a8ed06, 466 lines)

**Verdict: NOT CONFIRMED.** All 18 findings of R-P-K are resolved. Every new text reads correctly in context. Every
printed integer and decimal bound recomputes exactly. The choice made for finding 2 is sound. One new minor issue
remains, in text 3: the upper bound for d is stated without the admissible choice it holds at. I also found five nits.
There is no Major issue.

Line numbers are those of proofs/P-K.md unless a chapter is named. The tree moved while I read: proofs/P-LB.md was
merged (commit a722cb42, "M-LB") and the proof file was retired. I checked the placement against both trees:
- **before the merge**: the chapters at 2690f667;
- **after the merge**: the chapters at the current HEAD c4214cb8, identical to the working tree.

## The 18 findings

| # | Status | Where (P-K lines) |
|---|---|---|
| 1 minor, lowering hypothesis | resolved | 34–38, 40–42, 86–91, 176–178; remark 312–314 |
| 2 minor, k = 0 and the ranges of n | resolved | 51, 57, 63, 93, 122–125, 166, 180, 219–222, 236–241; text 4 at 363–364; row 3 at 450 |
| 3 minor, a → L_F | resolved | 15, 46–47, 215, 227–229, 233, 236–237; no stale "a" for 132 is left |
| 4 minor, "fixed by ℓ0 and ℓ_I" | resolved | text 2 at 339–340, text 3 at 351–352, text 8 at 411–412 |
| 5 minor, the two data classes | resolved | text 4 at 363–364, text 5 at 372–374 |
| 6 minor, the additive terms | resolved | 308 |
| N1 | resolved | 76 |
| N2 | resolved | 149 |
| N3 | resolved | 315–316 |
| N4 | resolved | 376, 380–381, 389; ch63 lines 67, 68–70 and 291–293 match |
| N5 | resolved | 6–7 |
| N6 | resolved | 102 |
| N7 | resolved | 238 |
| N8 | resolved | 214 |
| N9 | resolved | 267–269 |
| N10 | resolved | 428 |
| N11 | nothing to do | P-K has no "Section [[sec:…]]" |
| N12 | resolved | in F-P-K |

### Finding 2: the choice and its consistency

**The choice is right.** The alternative takes k′_k = 282 + L_P for k ≥ 1 and k′_0 = 283 + L_P, which makes
k′_0 > k′_1. Chapter 46 line 248 says "We take k′_k non-decreasing in k", and chapter 46 relies on that monotonicity at
lines 1309 and 1605. Keeping the alternative would therefore mean editing a hypothesis of chapter 46, as R-P-K's
version of text 4 did, or showing that those two uses need only k + k′_k to be non-decreasing.

The writer's choice leaves that sentence true as written. It keeps "for every k" and "a constant serves". Its cost is
one derivative in d_1, K, N and k1. These are upper counts already, and the remark says so ("smaller orders may
serve"). The parenthesis at lines 240–241 records that 282 + L_P would serve at the orders the proofs use.

The proof works with m := k + 3:
- m ≥ 3, as (iv) asks;
- n = m + L_P ≥ 10, which covers (vi) at n and at n + 6, and covers n + 13 ≥ 21 and n + 6 + L_0 ≥ 21;
- the left side of (3) at the order k + 2 < m is controlled by ℬ^m;
- n + 16 + 2L_F = k + 3 + L_P + 280 = k + (283 + L_P).

**Consistency.** I grepped every occurrence of k′_k, k″, d_1, K, N, k1, M and K*. All use 283 + L_P and the derived
values: lines 180, 184, 187, 190, 201–205, 237, 241, 243, 251, 253, 260, 262, 287, 289, 298–302, 308, texts 2–9, and
rows 3–5. Their other forms are consistent too:
- M = 2k1 + 17 and 2M + 1 = 4k1 + 35;
- eq:uc-kstar-own has the same form at lines 192, 385 and 457;
- k′ is constant, so the monotonicity that chapter 46 asks for holds;
- d_1 = max(309, 21d + 6 + d + 3 + 283 + L_P) = 22d + 292 + L_P, because 22 + 292 + 7 > 309.

No stale 282 (except the deliberate one), 291, 305, 330, 335, 339, 344, 347 or 348 remains.

## Recomputation (exact integers and fractions, python3)

Inputs:
- D_acc = 157,156,403,040·10³⁹ + 1,258,700·10¹⁸, from thm:uc-integer;
- D_b and D_c, from prop:uc-d-small (b) and (c), as printed at lines 293–294;
- d ≥ d_acc > 1.2497·10²⁴, from eq:uc-lower.

Results, all of which hold:
- **K at the computational point.** 22·157,156,403,040 = 3,457,440,866,880 and 22·1,258,700 = 27,691,400.
  22D_acc + 345 equals the printed 52-digit integer, ending …345, with leading digits 3.4574408; it is
  < 3.45745·10⁵¹.
- **d_1 and N there.** 22D_acc + 331 and 22D_acc + 348.
- **The two seminorm readings.** 22D_b + 345 equals the printed integer ending …513, and it is < 5.7624·10⁵⁰.
  22D_c + 345 equals the printed integer ending …591, and it is < 1.15248·10⁵¹.
- **The lower bound for K.** 22·1.2497·10²⁴ = 2.74934·10²⁵ exactly, so K > 22d > 2.74934·10²⁵ > 2.7493·10²⁵.
- **J at the computational point.** ℓ^♭_I = 60099/40000, and 4(7/2 − ℓ^♭_I) + 1 = 89901/10000 < 9, so J ≤ 8. In
  general the bound is < 11, so J ≤ 10.
- **L_P and K in general.** L_P ≤ 23 + 20 = 43 and 28 + 20 = 48, so K ≤ 22d + 349. At the computational point
  L_P ≤ 39 and 44, so K ≤ 22d + 345, d_1 ≤ 22d + 331 and N ≤ 22d + 348.
- **The half-integer class.** d_1 ≤ 22d + 336, and k1 ≤ 22D_acc + 340 = k̄.
- **The upper bound for K\*.** k̄ + 4 + (4k̄ + 35)(k̄ + 3) = 4k̄² + 48k̄ + 109 = 4.78155893918…·10¹⁰³ < 4.78156·10¹⁰³.
  The intermediate steps hold: k̄ > 10⁵¹, 48k̄ + 109 < 10⁻⁴⁹k̄², k̄ < 3.4574408669·10⁵¹,
  k̄² = 1.1953897347…·10¹⁰³ < 11.95389735·10¹⁰², and (4 + 10⁻⁴⁹)·11.95389735·10¹⁰² < 4.78156·10¹⁰³.
- **The lower bound for K\*.** K* > (4/3)k1², with k1 > 2.74934·10²⁵ and k1² > 7.5588704·10⁵⁰ > 7.5588·10⁵⁰. So
  (4/3)·7.5588·10⁵⁰ = 1.00784·10⁵¹ > 1.0078·10⁵¹.
- **Text 3's bound for d.** D_acc < 1.57157·10⁵⁰.

## Labels, re-reading, placement and merge

**Labels.** All 77 existing labels that P-K cites resolve, and the 6 new ones are defined nowhere else. I re-checked
what the fix round newly cites or depends on:
- row d1 of sec:vi-c-1: jℰ_0 ⊂ ℰ_0;
- lem:own-e-flux: θ_k = (k − 4)/5, s_R and eq:own-kstar;
- lem:viii-2-1: takes k′_k as in lem:iii-k-2-2 (d);
- rem:ec-not-evaluated: λ1 and δ are not evaluated;
- the paragraph after thm:own-data: λ_2 is not evaluated;
- Step 1 of thm:iii-c1-3-1: it lowers α₀ "if needed so that α₁ ∉ Re π₁ℰ₀";
- Step 2 of thm:iii-c1-3-1: "ν > ¼ … J ≤ 4(ℓ_I − ℓ^♭_I) + 1";
- def:uc-choice: ℓ_I < 3.5.

**Re-reading.** I read the file end to end. The section holds together: the definitions, the lemma's ranges, the count
in the proof of (a), and (b)–(d) with the remark.

**Old texts.** Each of the eight old texts occurs exactly once in the chapters, before and after the P-LB merge, and so
does the insertion anchor ("under both." followed by the heading of sec:ec-linear).

| Item | Before the merge | After the merge |
|---|---|---|
| 2 | ch71:26–27 | ch71:29–30 |
| 3 | ch03:311 | ch03:311 |
| 4 | ch46:248 | ch46:248 |
| 5 | ch46:1603 | ch46:1603 |
| 6 | ch63:67 | ch63:67 |
| 7 | ch63:291–293 | ch63:291–293 |
| 8 | ch90:72–73 | ch90:76–77 |
| 9 | ch90:130–131 | ch90:134–135 |

**Overlap with P-LB.** On the pre-merge chapters I applied P-K then P-LB, and P-LB then P-K, with P-LB's own placement
section (P-LB md5 52191107…). Every old text of either file occurred exactly once in both orders, and the two results
are byte-identical, so no P-K old text overlaps a P-LB old text. Applying P-K to the current HEAD gives the same result
in chapters 03, 46, 63, 71 and 90.

**The merge on the current HEAD**, in the scratch copy …/scratchpad/r2pk/ (chapters, crosswalk, assemble.py, lint.py,
OUTLINE.md):
- `lint.py --chapters`: 62 files, 4615 labels (4609 + 6), 0 hits;
- `assemble.py --check`: labels 4615, problems 0;
- plain `assemble.py` in the scratch copy, then `lint.py --paper`: 0 hits;
- the longest line of the assembled paper is 121 characters, and none is over;
- the 359 changed or new assembled lines are at most 120 characters, and none starts a wrapped line with "+ ", "- ",
  "* ", "> ", "#", "=" or "|". The section assembles as §49.14.

On the pre-merge tree the same run gave 4599 labels and 0 problems, with a maximum line length of 121.

**Typography of P-K.md.** Every line is at most 121 characters, no wrapped line has a forbidden start, all labels and
references are lowercase, and there is no backslash.

## New findings

### m1. minor — text 3 states the upper bound for d without the choice it holds at (lines 347, 353–355)

thm:uc-integer bounds d at the computational point only at the admissible choice of def:uc-choice and def:cs-choices.
For other admissible choices d may be larger. Every other place in the paper that states 1.57157 × 10⁵⁰ carries the
choice, and the ch71 crosswalk records this repair (F-DINT-b). The places are:
- the opening of ch71;
- sec:introduction-scope;
- the further-results item of ch03;
- sec:scope-constants;
- the abstract.

Text 3, in ch03 right after thm:settling, drops it and does not cite thm:uc-integer. Text 2 and text 8 do not need the
change, because the sentence just before each of them states the choice.

Old (line 347):

    New (the same line, followed by six lines that continue its paragraph):

New:

    New (the same line, followed by seven lines that continue its paragraph):

Old (lines 353–355):

    below by explicit functions of the gauge and damping parameters ([[ch:explicit-constants]]). At the computational
    point of [[def:ec-point]], which lies outside that set ([[rem:ec-point-outside]]), d is at most an integer below
    1.57157 × 10⁵⁰, and K at most one below 3.45745 × 10⁵¹.

New:

    below by explicit functions of the gauge and damping parameters ([[ch:explicit-constants]]). At the computational
    point of [[def:ec-point]], which lies outside that set ([[rem:ec-point-outside]]), and at one admissible choice of the
    weights, orders and inner products, d is at most an integer below 1.57157 × 10⁵⁰ ([[thm:uc-integer]]), and K at most
    one below 3.45745 × 10⁵¹.

I tested the replacement in a scratch copy:
- the source lines are 113, 118, 116 and 25 characters;
- resolved, the longest is 111;
- lint finds 0 hits, and assemble finds 0 problems.

### Nits

- **n1. Crosswalk row locations (lines 444, 449, 454, 456, 459).** The intro grew by one line, so rows 2–6 point one
  line early. Replace "P-K.md:39" by "P-K.md:40", ":175" by ":176", ":183" by ":184", ":191" by ":192" and ":306" by
  ":307". Row 1 (":1") is right.
- **n2. Line 11.** "use the upper bound for d at the computational point" is incomplete, because part (d) also uses the
  lower bound eq:uc-lower (K > 2.7493·10²⁵ and K* > 1.0078·10⁵¹).
  - Old: `follow from it use the upper bound for d at the computational point, which lies outside the set on which`
  - New: `follow from it use the bounds for d at the computational point, which lies outside the set on which`
- **n3. Lines 240–241.** "k + 3 of [[lem:iii-k-2-2]] (d), where m := k + 2 would serve" uses k for the lemma's index
  and then for the index of (3).
  - Old:

        k, as (3) asks. (The proofs use (3) only at the orders j + 3 of [[eq:s27-theta]] and k + 3 of [[lem:iii-k-2-2]] (d),
        where m := k + 2 would serve and give 282 + L_P; the one more order makes the count hold at k = 0 as well.)

  - New (110 and 101 characters):

        k, as (3) asks. (The proofs use (3) only at orders k ≥ 3, by [[eq:s27-theta]] and [[lem:iii-k-2-2]] (d), where
        m := k + 2 would serve and give 282 + L_P; the one more order makes the count hold at k = 0 as well.)

- **n4. Text 3 and the remark can now name the lower bound.** Their claim that d is bounded below on the proved set is
  true only with P-LB merged, and P-LB is now merged. thm:ec-lb-proved is defined in ch71, before the place where the
  section goes.
  - Line 353, old: `below by explicit functions of the gauge and damping parameters ([[ch:explicit-constants]]). At the computational`
  - Line 353, new: `below by explicit functions of the gauge and damping parameters ([[thm:ec-lb-proved]]). At the computational`
    (apply this after m1 too).
  - Line 311, old: `bounded only from below, by the lower bounds of this chapter on that set; the numbers of its part (d) are those of the`
  - Line 311, new: `bounded only from below ([[thm:ec-lb-proved]]); the numbers of its part (d) are those of the` (refill).
  - Both were tested: lint 0, assemble 0 problems, resolved lines of 101 and 85 characters.
- **n5. Line numbers in the item headers after the P-LB merge.**
  - Line 330: "(lines 26–27)" → "(lines 29–30)".
  - Line 403: "(lines 72–73)" → "(lines 76–77)".
  - Line 415: "(lines 130–131)" → "(lines 134–135)".
- **n6. Item 10 (lines 430–434)** still describes P-LB as an unmerged proposal, with its pre-merge line numbers.
  - Old:

        statements, as d_1 and K are now explicit in d while d is bounded above only at the computational point; the proposal
        for the lower bounds of d on the proved set rewrites three of its lines (lines 4693–4695), which no text here touches.
        That proposal also rewrites lines 16–25 of the opening of [[ch:explicit-constants]], lines 351–357 of [[ch:theorems]]
        and lines 66–67 of [[ch:scope]]; none of these overlaps texts 2, 3, 8 or 9. [[ch:introduction]] states no value of K or
        d_1.

  - New (117, 114, 116 and 28 characters):

        statements, as d_1 and K are now explicit in d while d is bounded above only at the computational point. The proposal
        for the lower bounds of d on the proved set is merged, three lines of that remark among its texts, and none of its
        texts in [[ch:explicit-constants]], [[ch:theorems]] or [[ch:scope]] overlaps texts 2, 3, 8 or 9. [[ch:introduction]]
        states no value of K or d_1.

  M-LB §3 already records that P-K's notes for ch:explicit-constants and sec:scope-constants are appended after the P-LB
  notes, separated by "; ". Row 3's note itself contains "; " ("… of thm:own-data; at the computational point …").
  That does no harm, because the rows are given as four named fields, but whoever merges should keep it in the note
  column.
