# M-K: merge of proofs/P-K.md

Input: proofs/P-K.md, md5 5258f67d066990c6de53d35be8fcfbd6 (466 lines), CONFIRMED by notes/reviews/R-P-K.md and
notes/reviews/R2-P-K.md (Final). P-K.md was not changed and not deleted; the coordinator retires it.

Pin: `git show 6de81a35:research/warp-drive/paper/reader/proofs/P-K.md | md5sum` gives 5258f67d066990c6de53d35be8fcfbd6,
so the crosswalk source column cites `paper/reader/proofs/P-K.md@6de81a35:N`.

I made no commit. While I worked, the coordinator's automatic snapshot f3e7d724 ("Snapshot: work in progress
(explicit-K merge, proof files)") committed my edits to the five chapters and five crosswalks. `git diff 155f39c6 HEAD
-- chapters crosswalk` contains exactly the hunks listed below and nothing else, and the working tree equals HEAD for
chapters/ and crosswalk/. The same snapshot also carries other agents' edits to proofs/P-F123.md and proofs/P-T78.md,
which are not mine.

## 1. Placement items applied

Before each replacement I checked that the old text occurs exactly once in the current chapter, as whole lines (with a
newline on each side). All eight did, at the lines the headers give, so no item needed adjusting. Each new text was
copied byte for byte from P-K.md. After the merge each new text occurs exactly once and no old text remains. Text 3 is
the exception to the second check by design: its new text begins with the old line.

| Item | Where | Old text found at | New text now at |
|---|---|---|---|
| 1 | section sec:uc-data-order (P-K lines 1–316, byte-identical) | after "under both." (71:4906), before sec:ec-linear | chapters/71-explicit-constants.md:4911–5226; one blank line before, one after; sec:ec-linear now at 5228 |
| 2 | ch. 71, opening paragraph | 71:29–30 (2 lines) | chapters/71-explicit-constants.md:29–33 |
| 3 | ch. 03, paragraph after thm:settling | 03:311 (1 line) | chapters/03-theorems.md:311–318 (the same line and seven more) |
| 4 | ch. 46 (ch:s27), prop:iii-k-1-2 (3) | 46:248 (1 line) | chapters/46-s27-nonlinear.md:248–249 |
| 5 | ch. 46, *Smallness* in the proof of thm:iii-k-3-2 | 46:1603 (1 line; 1604 after item 4) | chapters/46-s27-nonlinear.md:1604–1606 |
| 6 | ch. 63, paragraph after thm:own-data | 63:67 (1 line) | chapters/63-own-data.md:67–71; the three lines that follow stay, at 72–74, not refilled |
| 7 | ch. 63, rem:own-half-changes (b) | 63:291–293 (3 lines; 295–297 after item 6) | chapters/63-own-data.md:295–299 |
| 8 | ch. 90, sec:scope-constants | 90:76–77 (2 lines) | chapters/90-scope.md:76–79 |
| 9 | ch. 90, sec:scope-after | 90:134–135 (2 lines; 136–137 after item 8) | chapters/90-scope.md:136–138 |
| 10 | unchanged texts | — | nothing to apply (merge instruction only) |

The six labels are defined once each, all in chapter 71: sec:uc-data-order 4911, lem:uc-data-losses 4950,
prop:uc-data-order 5086, eq:uc-data-order 5094, eq:uc-kstar-own 5102, rem:uc-data-order-limits 5217. In the assembled
paper they are Section 49.14, Lemma 49.119, Proposition 49.120, (49.62), (49.63) and Remark 49.121, and sec:ec-linear is
now Section 49.15.

Item 6 permits refilling the paragraph. I did not refill it, because every line is already within the limit and
refilling would only add to the diff.

Chapters 33 and 83 were not touched, and P-K does not name them.

## 2. Crosswalk

- **crosswalk/71-explicit-constants.tsv:224–229.** The six new rows, sec:uc-data-order through
  rem:uc-data-order-limits, go between eq:uc-d-small (223) and sec:ec-linear (now 230). That is chapter order, since no
  label is defined between eq:uc-d-small and sec:ec-linear. Each row is P-K's "Row N." text, with its wrapped lines
  joined by single spaces and split into four fields at the first three "; ". Row 3's note keeps its own "; " ("…
  K*(a, M, k1) of thm:own-data; at the computational point K ≤ …") inside the fourth column. The source column reads
  `paper/reader/proofs/P-K.md@6de81a35:N` (N = 1, 40, 176, 184, 192, 307).
- **Adjustment: trailing full stop.** Each "Row N." item in P-K ends with a full stop that closes the listing's
  sentence. Of the 4,609 notes in all the crosswalks, 4,608 end without a full stop, so I dropped it from the six notes.
  No other character of the rows was changed.
- **Notes on existing rows.** Each note is appended after "; ", or written alone where the note column was empty
  (sec:settling-statement, rem:own-half-changes). Each note carries a "(P-K text N)" tag, after the "(P-LB text N)" tag
  that M-LB used, because ch:explicit-constants and sec:scope-constants already end with a P-LB note:
  - crosswalk/71-explicit-constants.tsv:2 ch:explicit-constants: "opening states d_1 and K (P-K text 2)", after the
    P-LB note;
  - crosswalk/03-theorems.tsv:20 sec:settling-statement: "the paragraph after thm:settling states K explicit in d (P-K
    text 3)";
  - crosswalk/46-s27-nonlinear.tsv:11 prop:iii-k-1-2 and :46 thm:iii-k-3-2: "k′_k and d_1 counted in
    prop:uc-data-order (P-K texts 4–5)";
  - crosswalk/63-own-data.tsv:3 thm:own-data and :21 rem:own-half-changes: "d_1, k1 and K* explicit in d (P-K texts
    6–7)";
  - crosswalk/90-scope.tsv:4 sec:scope-constants, after the P-LB note, and :5 sec:scope-after: "K and d_1 explicit in d
    (P-K texts 8–9)".
- **Adjustment: shared notes.** P-K gives one parenthetical for each pair of rows (texts 4–5, 6–7, 8–9). I wrote it
  unchanged on both rows of the pair rather than splitting it by text. Strictly, text 4 sits in prop:iii-k-1-2 and text 5
  in thm:iii-k-3-2, text 6 in thm:own-data and text 7 in rem:own-half-changes, text 8 in sec:scope-constants and text 9
  in sec:scope-after. If the coordinator prefers one text number per row, only the tag changes.

## 3. Checks (on the merged tree; HEAD 28a7a38a, working tree equal for chapters/ and crosswalk/)

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4615 label(s) defined, 0 hit(s)". That is 4609 + 6, the number
  R2-P-K's scratch merge predicted.
- `python3 assemble.py --check`: "labels 4615, computations cited 0, problems 0".
- The in-memory check prints `[] 0`.
- **Crosswalk order.** Each crosswalk I touched has exactly one row per label in chapter order, with 4 tab-separated
  fields on every row and the 4-field header:
  - 71: 234 labels, 234 rows;
  - 03: 21 and 21;
  - 46: 62 and 62;
  - 63: 124 and 124;
  - 90: 8 and 8.
- **Line lengths.**
  - Source lines: the five touched chapters have maximum line lengths of 120 (03) and 121 (46, 63, 71, 90), and none is
    over 121.
  - Assembled paper: 97,750 lines, the longest 121, and none over.
  - Changed lines: I assembled the tree with HEAD-before-merge copies of the five chapters and diffed the two
    assemblies. That gives 360 changed or new assembled lines, the count R2-P-K reports, and the longest is 120.
- **Wrapped lines.** Among the changed lines, the only ones that start with "+ ", "- ", "* ", "> ", "#", "=" or "|" are
  the two section headings (49.14, and 49.15 renumbered), each after a blank line. No new or changed source line starts
  a wrapped line with any of them.
