# F-P-TR: fix round for proofs/P-TR.md

- Old: md5 fa60e463d8da76fe646853f4315db859, 706 lines.
- New: md5 **e8d94b368ba272fae34afde252394de1**, 838 lines.
- A snapshot commit by someone else (814c4c06) has already picked up this version; I committed nothing.
- I edited no chapter.
- Rebased on HEAD d65c494c. Its chapters are identical to fb87f2fc.

## Review findings applied (R-P-TR)

All of M1, m1–m10 and nits 1–15 are applied, in the reader's words except where listed below.

- **M1.** The reader's text is used as given: the b ≥ 56 disc lies in {Re ι > −1/(2h)}, by [[prop:s14-scalar-every-h]].
- **m1.** 4.751175·10⁻¹¹ (both places) and 9.98011…·10⁻⁷.
- **m2, m4–m7, nits 1–4 and 6–8, 10–13.** As given.
- **m3.**
  - The body texts are as given.
  - In placement texts 2, 4, 6 and 7, "such a root" has no antecedent in the chapters where those texts land. I wrote instead:
    - in chapter 71: "the real part of an indicial root ι of □^C_b with |ι − 1| ≤ 50 crosses an integer";
    - in chapter 90: "near some points of 𝖩".
- **m8.** h₁ → h_m throughout.
- **m9.** The coordinator asked for no 𝖧 in hypotheses, and that overrides the reader's replacements of the form "𝖧 of [[eq:iv4-0-1]]". No text now uses 𝖧, h_* or an undefined ε_Υ. Text 7 keeps the chapter's own "h ∈ 𝖧".
- **m10.** I took "the upper bounds for d and N_NM".
- **Nit 5.** Reworded so that it absorbs the new multiple-root clause (below).
- **Nit 9.** Placed after the table, not after "≥ 0.3885", because the 1/100 disc is introduced only there.
- **Nits 14 and 15.** Done. The new note for row 2 also names the multiple-root clause.

## Hypotheses stated directly (coordinator, and P-ADM's note on P-TR)

**Admissibility.** The *Setting* defines "the parameter point (h, 1/100, 1/100) is admissible": for some γ_(Υ,H) > 0 the point meets the conditions of [[thm:vi-c-2-1]]. Form B (item 1b) replaces this with [[def:vi-c-admissible]].

**Where the direct hypotheses now appear.**
- [[thm:tr-transfer]]: h_m ≤ h < 10⁻⁶, h ∉ 𝖩, admissible.
- [[prop:tr-inputs]]: h_m ≤ h < 10⁻⁶, h ∉ 𝖩.
- [[prop:tr-fail]]: 0 < h < 10⁻⁶, admissible.
- The lower-bound sentence: every admissible h ∈ (0, 10⁻⁶).

**The opening and [[rem:tr-scope]].**
- The opening now says the computational point "is not shown to lie in" the proved set.
- [[rem:tr-scope]] cites the open conditions without rows. Form B gives P-ADM's wording, without naming condition numbers, since P-ADM renamed them (P → AP) during this round.
- Answer to P-ADM's question: **the proof uses no property of h beyond h_m ≤ h < 10⁻⁶ and h ∉ 𝖩.** It does not use h ∈ 𝖧.

**New multiple-root clause.** The old proof used h ∉ 𝖹₁ for simplicity, and admissibility no longer gives that.
- 𝖩 now also contains the h at which P_l has a multiple root, for some 123 ≤ l ≤ 142. P-T49's prop:t49-six shows that such h exist in the range.
- prop:tr-inputs (b) now proves simplicity from the location lemmas.
- prop:tr-measure shows that part is finite: the discriminant is a polynomial in h, the leading coefficient is −h³, and it is not zero at 10⁻⁶ ([[prop:t49-simple]]).
- 𝖩 is now "finitely many intervals and points". Its length bound is unchanged.

**New placement item 8.** [[rem:uc-data-order-limits]] says d "is bounded only from below". This adds "except at the points of [[thm:tr-transfer]] if there are any".

## Placement and checks

**Two forms.**
- Items 2, 3, 5, 6 and 8 come in two forms:
  - form A is against HEAD;
  - form B is against HEAD after P-ADM (its items 32, 33, 43, 50, 52).
- Items 1, 4 and 7 have one form. Item 4's old text is the two lines after P-ADM's item 41, which P-ADM leaves unchanged.

**Old texts.** Every old text occurs exactly once:
- in each form A, at HEAD;
- in each form B, in a simulation of all of P-ADM's items 31–44 and 49–53, using P-ADM at its current md5 bb8171d26e255d564043bda5ae5a75c5 (it was still moving during this round).

**Scratch merge.** Both forms were simulated in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/ptr/merge/.
- Form A:
  - `lint.py --chapters`: 0 hits;
  - `assemble.py --check`: 0 problems;
  - sec:tr is Section 49.15, and thm:tr-transfer is Theorem 49.123.
- Form B: 12 hits, all of them references to P-ADM's own labels (vi-c-adm…). Their definitions are in its chapter-46 part, which I did not simulate.
- Both forms: the longest line of new text after label resolution is 121 characters.

**The file itself.**
- At most 121 characters per line, also after worst-case label expansion.
- No bad wrap starts, no backslash, lowercase labels.
- The style lint flags only the crosswalk file locations, which follow the convention.

**Crosswalk.** Sources are "paper/reader/proofs/P-TR.md@PENDING:N".

## If V-I11 is confirmed (1 + 𝒵 in Λ)

### Results that fall with the upper bound of thm:uc-integer

- [[thm:tr-transfer]] (ii): C_*, D_acc, d_R, d_NM, N_NM, d_Ψ, d_FM and c(β).
- Placement texts 2–6 and 8.
- "3R > 1.2498·10²⁴ at the choice of [[def:uc-choice]]" becomes a statement at a choice that is no longer admissible.

The transfer would not merely inherit the failure; its mechanism also breaks.
- The proof of (ii) rests on Λ ∩ {Re < 3 + ε_+} being independent of h, through [[prop:is-lambda]] and [[prop:is-count]].
- With 1 + 𝒵 in Λ, that set contains ι(h) + W for every root ι(h) of C or P_l with 2 < Re ι ≤ 3 + ε_+. Here W is the h-independent semigroup of increments (𝔡₀, 𝔡₁, …).
- So h becomes a fifth input. N_Λ, the admissible ε_K and everything after them depend on h.
- Even a re-established bound at h = 10⁻⁶ would not transfer "with the same numbers".

### Results that stand on their own

- The root enclosures, uniform in h ∈ (0, 10⁻⁶]: lem:tr-split, tr-c-v, tr-small, tr-large and tr-slopes.
- def:tr-exceptional, prop:tr-measure and prop:tr-eps.
- prop:tr-inputs. It concerns ℰ^ι_ind, the multiplicities and the poles, not Λ.
- thm:tr-transfer (i).
- The lower bounds 1.2497·10²⁴ and 2.624·10²⁵. They rest on [[cor:uc-two-offsets]] and [[prop:ec-rounds]], which V-I11 lists as unaffected.
- prop:tr-fail. It uses the lower-bound route of lem:ec-lb-rounds. "d_acc > D_acc" is a comparison with the number 1.57157·10⁵⁰, and its conclusion holds a fortiori.
- Placement text 7, which concerns ε_ind only.

### What the root analysis says about the new points near 3

1. **Which roots can enter.** Only roots with 2 < Re ι ≤ 3 + ε can give a point ι + w in (3, 3 + ε].
   - **Vector type: never.** For l ≥ 2 and h ≥ h_m, ι_v − 3 ≥ 4.99h > ε_+.
   - **Scalar type, h ∈ [h_m, 10⁻⁶]:**
     - ι₁ ∈ (2 + 7·10⁻⁵, 5/2);
     - for l ≤ 122, three real roots in (2, 3);
     - for 123 ≤ l ≤ 142, ι_B ∈ (2 + x/2, 2.031) and two roots with real part in (2.1, 2.92);
     - for l ≥ 143, ι_B is in the strip only if x < 1.01, and ι_P, ῑ_P only if x ≲ 0.733.
   - **Open case.** For x > 70 the enclosures exclude only |ι − 1| ≤ 50. Roots with real part in (2, 3) and |Im ι| > 49 are not excluded at general h; cor:t49-right excludes them only at h = 10⁻⁶.

2. **How many points (rigorous, counted as sums).**
   - Take the ι_B with 0.02 ≤ x ≤ 0.49. They have Re < 2.735.
   - Each gives more than 7.8·10¹⁰ sums ι_B + p𝔡₀ + q𝔡₁ below 3: the lattice points of a triangle number at least its area, 0.265²/(2𝔡₀𝔡₁), using 𝔡₀ < 1.3334·10⁻⁶ and 𝔡₁ < 3.3334·10⁻⁷.
   - There are 559 such degrees at h = 10⁻⁶ (l = 141–699) and 80,961 at h_m (l = 20498–101458).
   - So there are more than 4.3·10¹³ such sums at h = 10⁻⁶ and more than 6.3·10¹⁵ at h_m, against N_Λ < 1.67472·10¹³. The count grows like h^(−1/2).

3. **How they move with h.**
   - P-TR proves rates only near real part 3: ∂_hι_B ≥ 0.98κ for 0.98 ≤ x ≤ 49.02, and ∂_h Re ι_P ≥ 2κ/5 for x ≥ 1/2.
   - Where a rate holds, a fixed sum stays in a window of length ε for an h-interval of length at most ε/(cκ).
   - For roots deep in (2, 3), no rate is proved.
   - Off 𝖩, (H_ε) keeps the w = 0 points out of (3, 3 + ε_Υ). Nothing controls the points with w > 0.

4. **Whether (G) holds at a given h.**
   - After the repair this is a Diophantine question: how close 3 − Re ι(h) comes to W, at scale ε_K ≈ 10⁻¹⁴, for 10³–10⁵ roots.
   - The enclosures here have widths 10⁻⁵–10⁻². They cannot decide it at any h.
   - Heuristic, not proved:
     - The density of W near t is about t/(𝔡₀𝔡₁).
     - So the expected number of points in (3, 3 + 1.6416·10⁻¹⁴] is about 0.037·Σ(3 − Re ι): about 40 at h = 10⁻⁶ and about 6·10³ at h_m, using the centres of the enclosures.
     - The failure at the choice in [[def:uc-choice]] is therefore expected at essentially every h in the range, with the admissible ε_K(h) shrinking as h decreases.
     - The equidistribution behind this is itself only heuristic: W clusters, since 𝔡₀ − 4𝔡₁ ≈ 5.6·10⁻¹³ > ε_K.
