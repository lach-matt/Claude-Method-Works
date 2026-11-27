# F-P-T49: fix round for proofs/P-T49.md after R-P-T49

**File:** `research/warp-drive/paper/reader/proofs/P-T49.md`

- Before: md5 81f3f0edc4d7918bfe12c8c1fafe5c6b, 664 lines.
- **After: md5 d2cad2883b4f7aeeb56571bd92615400, 659 lines.**
- No chapter was edited and nothing was committed.
- The pre-fix copy is kept at `/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pt49/P-T49.before-fix.md`.

Every point of the review was applied in the reader's words.

## Majors

- **M1. Text 6.** I took the reader's five lines verbatim. The sentence now reads "real part in [2, 51]"; the pole
  statement rests on prop:is-mult's own argument, not on thm:t49-point; and the text writes 𝖹_exc. The heading reads
  "(lines 3123–3126)" and "New, the five lines".
- **M2. rem:t49-count.**
  - The remark is deleted.
  - rem:t49-scope now states "whether 𝖹 ∩ I is finite is not decided here".
  - The remark is gone from text 1's label list, and text 1's last sentence is dropped.
  - Its crosswalk row is gone.
  - Nothing cited it. The section no longer carries a pending marker.

## Minors

- **m1. Text 4** is rebased on chapter 33, lines 3538–3540 at HEAD, using the reader's four lines.
- **m2. Text 7** is rebased on the merged remark at 7854b15c: lines 69–71 are replaced by the reader's five lines, and
  the fallback paragraph is deleted. A note says that P-ADM's item 31 replaces text 7 if the two files merge together.
  - I kept the remark's clause "the exclusion z_Υ ∉ 𝖹_exc of row u5 is a separate condition" (line 63) unchanged. It
    stays true, and P-ADM's combined text expects only the inserted sentence.
- **m3. Chapter 71.** New texts 9 (rem:is-summary, line 3462) and 10 (rem:sp-scope, lines 4073–4079), in the reader's
  words. Text 8 is revised, and crosswalk notes are added for both remarks.
- **m4.** rem:t49-sets (a): "two distinct roots …, that are not complex conjugates of each other".
- **m5.** The introduction and rem:t49-sets now say "contained in a union of zero sets"; 𝖹₁ and 𝖹₂ are such unions.
- **m6.** "4.56 at s = 7/5".
- **m7.** The bounds on R₃ᵉ and R₃⁰ now come from the factored form (< 42.1 and < 38).
- **m8.** rem:t49-scope is replaced by the reader's text, which includes M2 (b).

## Nits

- **n1.** cor:t49-right uses Ω = [κ₀, ∞) × {10⁻⁶}, and cites "whose proof counts the roots for every real κ ≥ 3".
- **n2.** prop:t49-pairs: (C4) also uses that the roots of C and of p_(v) are real.
- **n3.** Text 1 is anchored on the last line as text 4 leaves it.
- **n4.** Every placement heading carries its line numbers at 7854b15c.
- **n5.** Crosswalk sources read `paper/reader/proofs/P-T49.md@PENDING:N`, or `:N-M` from the label to the end of the
  item. All 22 rows were renumbered.
- **n6.** eq:t49-disc reads "(−1)^15 times the resultant … divided by the leading coefficient π₆".
- **n7.** The shift coefficients are renamed q₀, …, q₃, as the reader suggested. No q₀–q₃ occurs in chapter 33; the
  only overlap is the letter of q(d, ν) in eq:s14-q.
- **n8.** The chapter 71 texts write 𝖹_exc.
- **n9.** The 𝔖 table now prints the leading digits of 𝔖(k, l_k(l_k + 2)) and 𝔖(k, (l_k + 1)(l_k + 3)). All 49 rows
  were re-verified exactly.

## Checks against HEAD 7854b15c, after the P-T78 merge

- **Old texts.** I re-copied every old text from `git show 7854b15c:…`, and each occurs exactly once:
  - text 3: chapter 33, line 114;
  - text 4: chapter 33, lines 3538–3540;
  - text 5: chapter 34, line 490;
  - text 6: chapter 71, lines 3123–3126;
  - text 7: chapter 71, lines 69–71;
  - text 9: chapter 71, line 3462;
  - text 10: chapter 71, lines 4073–4079.
  The text 2 anchors (chapter 96, lines 258 and 260) are unique. The chapters in the working tree equal HEAD.
- **Scratch merge.** I applied texts 1–7, 9 and 10 to an export of HEAD.
  - `lint.py --chapters`: 0 hits.
  - `assemble.py --check`: 0 problems.
  - Assembled text: 98,503 lines, none longer than 121 characters after label resolution, and 0 hits from lint's
    assembled-mode scan.
- **P-T49.md itself.**
  - Linting it together with the chapters gives only the file names in its crosswalk rows, as in merged proof files.
  - Lines are ≤ 121 characters, no wrapped line starts with a marker, keys are lowercase, and there are no backslashes.
