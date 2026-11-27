# M-LB: merge of proofs/P-LB.md

Input: proofs/P-LB.md, md5 b769e8df079712aba31e21bf8c401639 (508 lines), CONFIRMED by notes/reviews/R2-P-LB.md.
Output: proofs/P-LB.md, md5 52191107b952d2c76346b9f08e817b8c (509 lines), merged into chapters 71, 00, 01, 03, 90 and
33 and crosswalks 71, 01, 03, 90 and 33. P-LB.md is kept for the coordinator to retire.

I made no commit. While I worked, the coordinator's automatic snapshots committed my edits: 2690f667 holds
P-LB.md with the nits (the same md5 as the working file), and 281f5587 holds the merged chapters and crosswalks.
After 281f5587 the working tree has no change in any file I touched.

## 1. Nits applied to proofs/P-LB.md (R2-P-LB's exact texts)

- **N1** (text 4, lines 348–350): "where z = 4e_Υγ_Υ² is that point's gauge parameter, not 4·10⁻⁶, and g is …" is now
  "where R is the number of rounds at that point, z = 4e_Υγ_Υ² its gauge parameter (not the value 4·10⁻⁶ fixed in this
  section) and g the function of [[eq:ec-lb-g]]". Still three lines, so text 4 is still "the six lines".
- **N2** (text 3, last sentence, lines 332–334): now "At every point of the proved set a lower bound for d holds as an
  explicit function of z = 4e_Υγ_Υ² and h, with no threshold evaluated, through bounds for ε_Υ and ε_ind(h) that hold at
  every such point ([[lem:ec-lb-gauge]], [[lem:ec-lb-ind]], [[thm:ec-lb-proved]])." Still three lines, so text 3 is
  still "the seventeen lines".
- **N4** (item 11, merge instructions only, lines 451–454): "stays true and, by [[rem:ec-lb-conditions]], follows from
  the proof of [[thm:ec-lb-proved]] at z = 4·10⁻⁶)". Item 11 grows from three lines to four, so every line after 453
  moves down by one: item 12's old text is now lines 460–461 and its new text 465–467. The section (lines 1–254) and the
  crosswalk line numbers in it do not move.
- **N3** (optional, applied): every B_g is now Θ_g and every B_η is now Θ_η. That is 53 + 27 = 80 occurrences, on lines
  124–202 and 226 and in the crosswalk rows (now lines 486, 487, 489). Before renaming I grepped chapters/ and crosswalk/
  for Θ_g and Θ_η: no hits. Θ_ occurs in none of chapters 40, 41 or 71. Θ is one code point, so no line length changes;
  P-LB.md's longest line is still 121 characters.

## 2. Placement items applied

Before each replacement I checked that the old text occurs exactly once in the current chapter, as whole lines. All ten
did, so no item needed adjusting. Final positions in the current tree:

| Item | Where | Old text found at | New text now at |
|---|---|---|---|
| 1 | section sec:ec-lb-proved (P-LB lines 1–254, byte-identical) | after "stop." (now 1542), before sec:ec-upper | chapters/71-explicit-constants.md:1544–1797; one blank line before, one after; sec:ec-upper now at 1799 |
| 2 | ch. 71, opening | 71:16 (10 lines) | chapters/71-explicit-constants.md:16–28 |
| 3 | ch. 71, rem:ec-point-outside | 71:49 (9 lines) | chapters/71-explicit-constants.md:52–68 |
| 4 | ch. 71, paragraph after thm:loss-d | 71:1462 (3 lines) | chapters/71-explicit-constants.md:1473–1478 |
| 5 | ch. 71, prop:ec-delta-cap | 71:1512 (1 line) | chapters/71-explicit-constants.md:1526–1527 |
| 6 | ch. 71, rem:ec-not-evaluated | 71:4693 (3 lines) | chapters/71-explicit-constants.md:4963–4968 |
| 7 | front matter, abstract | 00:32 (6 lines) | chapters/00-front.md:32–38 |
| 8 | ch. 01, sec:introduction-scope | 01:150 (5 lines) | chapters/01-introduction.md:150–156 |
| 9 | ch. 03, sec:further-results item | 03:351 (7 lines) | chapters/03-theorems.md:351–358 |
| 10 | ch. 90, sec:scope-constants | 90:66 (2 lines) | chapters/90-scope.md:66–71 |
| 11 | unchanged texts | — | nothing to apply (merge instruction only) |
| 12 | ch. 33, rem:s14-eps-ind-scope | 33:3537 (2 lines) | chapters/33-s14-constraint-damping.md:3537–3539 |

The "old text found at" lines for items 3–6 are where each old text stood when it was replaced, that is after the
earlier items in chapter 71 had already been applied. In the untouched chapter they were at 49, 1462, 1512 and 4693, as
P-LB says.

After the merge every new text occurs exactly once and no old text remains.

Things that needed checking (no adjustment was needed):

- **Chapter 33.** It changed after R2's tree (HEAD 99cdddb7), so item 12's old text now sits at lines 3537–3538, not
  3534–3535. The remark itself is unchanged and still occurs exactly once, followed by "defined.", so the text was
  applied verbatim.
- **Concurrent edits.** During the merge someone else edited chapter 33 (lines 1362–1363 and 1948) and its crosswalk
  (rows lem:iv5-6-tform and lem:iv6-0-flow). Those edits and mine are both in 281f5587, and none overlaps another.
- **Chapters 20, 22, 63, 95 and 98.** P-LB does not touch them.

## 3. Crosswalk

- **crosswalk/71-explicit-constants.tsv:69–84.** The 16 new rows, sec:ec-lb-proved through rem:ec-lb-unbounded, were
  inserted between prop:ec-delta-cap (68) and sec:ec-upper (85). They are copied from P-LB.md, so they carry Θ_g and
  Θ_η. The source column is "paper/reader/proofs/P-LB.md:N" as P-LB gives it, with no commit pin. If the coordinator
  wants a pin like the P-U71 rows have, 2690f667 holds this exact P-LB.md.
- **Notes appended after "; "**, as P-LB gives them:
  - 71:2 ch:explicit-constants (text 2);
  - 71:5 rem:ec-point-outside (text 3);
  - 71:66 thm:loss-d (text 4);
  - 71:68 prop:ec-delta-cap (text 5);
  - 71:229 rem:ec-not-evaluated (text 6);
  - crosswalk/01-introduction.tsv:9 sec:introduction-scope (text 8);
  - crosswalk/03-theorems.tsv:22 sec:further-results (text 9);
  - crosswalk/90-scope.tsv:4 sec:scope-constants (text 10);
  - crosswalk/33-s14-constraint-damping.tsv:182 rem:s14-eps-ind-scope (text 12).
- **The front matter crosswalk** has no rows, and text 7 needs none.
- **P-K.md and P-T78.md.** Each P-LB note is the last item of its row's note column. P-K's notes for
  ch:explicit-constants and sec:scope-constants, and P-T78's for sec:scope-constants, can be appended after "; ".

## 4. Checks

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4609 label(s) defined, 0 hit(s)". Before the merge it was 4593;
  the 16 new labels make 4609.
- `python3 assemble.py --check`: "labels 4609, computations cited 0, problems 0".
- The in-memory assembled line check prints `[] 0`.
- **Crosswalk order.** Each crosswalk I touched, and the front matter's, has exactly one row per label in chapter order,
  with 4 tab-separated fields on every row:
  - 71: 228 labels, 228 rows;
  - 00: 0 and 0;
  - 01: 9 and 9;
  - 03: 21 and 21;
  - 90: 8 and 8;
  - 33: 181 and 181.
- **Line lengths.** No merged source line is over 121 characters (the longest is 121). The assembled paper has 97,411
  lines; its longest is 121 and none is over. The new section assembles as §49.8 (Lemmas 49.34, 49.35, 49.37,
  Theorem 49.38, Corollary 49.39, Remarks 49.36, 49.40, 49.41), and its longest assembled line is 120.
- **Wrapped lines.** The only merged lines that start with "+ ", "- ", "* ", "> ", "#", "=" or "|" are the intended
  ones: the section heading, the eight list items of rem:ec-lb-conditions (after a blank line), and the first line of
  text 9's list item, which is unchanged.
- **P-LB.md itself.** No line is over 121 characters, and lint finds no wrap hit in it.
