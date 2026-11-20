# F-DINT-b: fixes to chapter 71 after R-DINT-b

Files: chapters/71-explicit-constants.md (82+/72−, now 4,382 lines) and crosswalk/71-explicit-constants.tsv (13 notes).
No label added, removed or renamed. The crosswalk's 203 labels equal the chapter's sequence. Diff:
scratch/f_dint_b/f_dint_b.diff. Line numbers are in the new file.

## Items

1. **Minor 1** (381–388): the reviewer's text.
   **Minor 2** (1558–1571): the reviewer's text, with one departure: "At h + h_rem(q) + …" became
   "At h̃ = h + h_rem(q) + …", because h̃ is otherwise undefined in that paragraph.
   - With (d_F + 3; d_F + 3, d_F + 3), "c, b ≤ a" holds, so lem:ec-split-loss (d) applies as before.
   - lem:cs-elem (e) still charges 20,183, and prop:ec-upper's parenthetical is unaffected. Nothing downstream moves.
2. **Nits.**
   - Nit 3 (1252, 1298): the reviewer's headings. Nothing moved, so every [[sec:…]] reference still fits.
   - Nits 4 (381–383), 5 (510–515), 6 (1478–1479) and 7 (4368–4370): the reviewer's texts.
   - Nit 8 (crosswalk rem:ec-other-losses): the reviewer's replacements, with one departure. The phrase "'the next
     section' written [[sec:ec-floor]]" would be stale after minor 1, so the note records minor 1's citation.
3. **R-DINT-a.**
   - O1 (1487–1492): chapter 46 as it stands still defines s_P in lem:iii-k-2-2 (d) and its proof. The parenthesis
     now gives ω_(2d+3) and s_(2d+3) to prop:iii-k-1-2 (3), and s_P to lem:iii-k-2-2 (d).
   - Also applied: O1's second half (1488, 1500). The proof of thm:iii-k-3-2 asks ‖P_5(Ψ(0))‖ < ε_NM, which is
     strict, and ω_k is non-decreasing. So the choice now reads C_(2d)ω̃(ε) < ε_NM, and the proof reads
     "< ε_NM/C_(2d)". The conclusions are unchanged.
   - O2 (28–30): "No result of this chapter is used in the proof of any theorem of this paper outside it. Other
     chapters state explicit values that rest on it, the indices of prop:ii-a1-2-4 and lem:ii-a-8-5, which
     prop:fwd-calculus proves, and the value N′ = 13 of ch:s06, which rests on lem:fwd-orders; these values are used
     only in this chapter."
     - Outside chapter 71, its labels are cited only for those values, in remarks (chapters 33, 62) and in
       chapters 01, 03, 90.
     - 200Θ and N′ = 13 occur nowhere else.
     - Chapter 25 now cites lem:fwd-orders.
   - O3: the opening (20–21) reads "at one admissible choice of the weights and of the free orders and inner products
     (def:uc-choice, def:cs-choices)". thm:uc-integer (2450–2452) names "the admissible choice of the weights of
     def:uc-choice and the free orders and inner products of def:cs-choices".
4. **R2-DB-b nit 2** (3853–3856, 3875–3877, 3938): the reviewer's texts.
   - def:cs-choices has item (h), and (g) now ends with ";".
   - (h)'s justification is appended to "These choices are allowed". I checked it against sec:iii-h2-0: B_1 is chosen
     by (B1)–(B4), and (B4) concerns the order built for 2L_(b₀).
   - lem:cs-elem (e) cites "(def:cs-choices (h))".
5. **Old line 3164** (3168–3169): "taken" moved to the next line, with no word changed.

## Line lengths

- Every changed paragraph was rewrapped with assembly's numbering. Each line is ≤ 121 characters in the source and
  after resolution.
- No line breaks beside an operator.
- No new line starts with a forbidden prefix, apart from the two headings.

## Checks

- `python3 lint.py --chapters`: 62 files, 4,573 labels, **0 hits**.
- `python3 assemble.py --check`: **problems 0**.
- The file ends in one newline and has no trailing blanks.
