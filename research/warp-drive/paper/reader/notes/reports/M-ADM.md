# M-ADM: merge of proofs/P-ADM.md

Input: proofs/P-ADM.md, md5 bb8171d26e255d564043bda5ae5a75c5 (1,253 lines). It was CONFIRMED by
notes/reviews/R-P-ADM.md, sections "Final (round 2)" and "Final (round 3)". At the start the HEAD was bcece9fb. Its
chapters were identical to those at 6f066bb5, which the reader used in round 3, and chapters/ and crosswalk/ were clean
in the working tree.

I made no commit, did not change P-ADM.md (its md5 is unchanged), and did not delete it. I touched only the 14 chapters
and 13 crosswalks that the placement names. I did not run the plain assemble.py.

While I worked, the coordinator's snapshot commits picked up my edits:
- 54350a5d "Snapshot: work in progress (P-ADM merge, proof files)" holds the chapter edits;
- f8d6d287 holds the crosswalk edits.

At the end, chapters/ is byte-identical to my scratch merge, and `git diff bcece9fb HEAD -- crosswalk` shows only my
rows and notes. Other agents' files changed in the working tree during the run: proofs/P-CIVP3.md, P-CIVP4.md,
P-G24b.md and notes/reviews/R-P-CIVP.md. I did not touch any of them. The full diff of chapters and crosswalk against
bcece9fb is in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/reports/M-ADM.diff`.

## 1. How the items were applied

A script (scratchpad `reader/madm/items.py` and `merge.py`) read the Placement section:
- For each item, the header's "Old, the N lines" count gave the old text, and "New, the M lines" gave the new text.
- The blocks were taken from Parts A–C: A1 (lines 20–81), A2 (85–89), A3 (93–102), A4 (106–169), B1 (179–183),
  B2 (187–190) and B3 (194–207). Part C is the remark alone (214–243); the introductory note at 211–212 is not
  chapter text.
- The three compound directives were built as stated:
  - item 21: Block A1, a blank line, then row c1's two lines, checked to equal the first two old lines;
  - item 30: the old line, a blank line, then Block A4, the line checked to equal the old line;
  - item 33: Part C.

The items were applied in item order, 1 to 58. Before each replacement the script checked two things against the
current state:
- the old text occurs exactly once as contiguous whole lines in its chapter;
- it occurs exactly once as a substring across all chapters.

All 58 passed. In the untouched chapters, each old text began at exactly the line its header gives. Item 59 says
"Unchanged", so there was nothing to apply.

I first ran the merge on a scratch copy and checked it, then ran it on the real chapters. The two results are
identical.

| Item | Chapter, place | Old at (bcece9fb) | Now at |
|---|---|---|---|
| 1 | ch:s15, sec:iii-f-1, parameters (2 → 4) | 34:76–77 | chapters/34-s15-linearised.md:76–79 |
| 2 | ch:s15, sec:iii-f1-1, (C4) → Block B1 (1 → 5) | 34:295 | 34-s15-linearised.md:297–301 |
| 3 | prop:iii-f1-2-3 (f), hypothesis (C4′) (1 → 1) | 34:443 | 34-s15-linearised.md:449 |
| 4 | prop:iii-f1-2-3, part (g), Block B2 (1 → 4) | 34:454 | 34-s15-linearised.md:460–463 |
| 5 | proof of prop:iii-f1-2-3, end of (f) and (g), Block B3 (2 → 14) | 34:498–499 | 34-s15-linearised.md:507–520 |
| 6 | ch:s16, opening, last sentence (2 → 2) | 35:53–54 | chapters/35-s16-iota-plus.md:53–54 |
| 7 | sec:iii-g2-1, standing hypotheses (4 → 4) | 35:1423–1426 | 35-s16-iota-plus.md:1423–1426 |
| 8 | sec:iii-g2-1, after (C5) (2 → 3) | 35:1435–1436 | 35-s16-iota-plus.md:1435–1437 |
| 9 | proof of lem:iii-g2-1-2 (2 → 3) | 35:1493–1494 | 35-s16-iota-plus.md:1494–1496 |
| 10 | proof of thm:iii-g2-3-1, the lowest term (2 → 3) | 35:1636–1637 | 35-s16-iota-plus.md:1638–1640 |
| 11 | sec:iii-g4-1, the operator (1 → 2) | 36:1138 | chapters/36-s17-null-infinity.md:1138–1139 |
| 12 | lem:iii-g4-1-1 (2), statement (2 → 3) | 36:1154–1155 | 36-s17-null-infinity.md:1155–1157 |
| 13 | proof of lem:iii-g4-1-1 (2) (3 → 4) | 36:1162–1164 | 36-s17-null-infinity.md:1164–1167 |
| 14 | proof of lem:iii-g4-3-4 (2 → 3) | 36:1359–1360 | 36-s17-null-infinity.md:1362–1364 |
| 15 | end of the proof of thm:iii-g4-3-1 (1 → 1) | 36:1423 | 36-s17-null-infinity.md:1427 |
| 16 | sec:iii-i10-1, after (H4) (1 → 1) | 41:124 | chapters/41-s22-kerr-face.md:124 |
| 17 | proof of lem:iii-i12-2-3, the reduction (3 → 4) | 41:1204–1206 | 41-s22-kerr-face.md:1204–1207 |
| 18 | ch:s23, the setting (2 → 3) | 42:559–560 | chapters/42-s23-augmentation.md:559–561 |
| 19 | sec:iii-k-0, Parameters (5 → 9) | 46:89–93 | chapters/46-s27-nonlinear.md:89–97 |
| 20 | sec:vi-c-1, opening (6 → 6) | 46:1706–1711 | 46-s27-nonlinear.md:1710–1715 |
| 21 | rows c1–c4 → Block A1, blank, c1 (12 → 65) | 46:1713–1724 | 46-s27-nonlinear.md:1717–1781 |
| 22 | rows u2–u5 → Block A2, row a1 (12 → 5) | 46:1730–1741 | 46-s27-nonlinear.md:1787–1791 |
| 23 | row b2 (4 → 4) | 46:1745–1748 | 46-s27-nonlinear.md:1795–1798 |
| 24 | row b3, threshold (1 → 1) | 46:1751 | 46-s27-nonlinear.md:1801 |
| 25 | row w1, threshold (1 → 1) | 46:1767 | 46-s27-nonlinear.md:1817 |
| 26 | row d1, threshold (1 → 1) | 46:1774 | 46-s27-nonlinear.md:1824 |
| 27 | row d2, threshold (1 → 1) | 46:1780 | 46-s27-nonlinear.md:1830 |
| 28 | thm:vi-c-2-1, steps (1)–(2) → Block A3 (11 → 10) | 46:1791–1801 | 46-s27-nonlinear.md:1841–1850 |
| 29 | proof of thm:vi-c-2-1 (4 → 5) | 46:1825–1828 | 46-s27-nonlinear.md:1874–1878 |
| 30 | sec:vi-c-2, the line, blank, Block A4 (1 → 66) | 46:1834 | 46-s27-nonlinear.md:1884–1949 |
| 31 | ch:explicit-constants, opening, lower bound (4 → 5) | 71:18–21 | chapters/71-explicit-constants.md:18–22 |
| 32 | opening, the computational point (3 → 3) | 71:26–28 | 71-explicit-constants.md:27–29 |
| 33 | rem:ec-point-outside → Part C (23 → 30) | 71:55–77 | 71-explicit-constants.md:56–85 |
| 34 | the paragraph after thm:loss-d (2 → 2) | 71:1484–1485 | 71-explicit-constants.md:1492–1493 |
| 35 | prop:ec-delta-cap, after the display (2 → 3) | 71:1535–1536 | 71-explicit-constants.md:1543–1545 |
| 36 | sec:ec-lb-proved, opening (8 → 8) | 71:1555–1562 | 71-explicit-constants.md:1564–1571 |
| 37 | thm:ec-lb-proved, title and first sentence (3 → 4) | 71:1716–1718 | 71-explicit-constants.md:1725–1728 |
| 38 | proof of thm:ec-lb-proved, the gaps (4 → 4) | 71:1736–1739 | 71-explicit-constants.md:1746–1749 |
| 39 | rem:ec-lb-conditions, opening and bullets (9 → 8) | 71:1774–1782 | 71-explicit-constants.md:1784–1791 |
| 40 | rem:ec-lb-conditions, after the bullets (5 → 6) | 71:1788–1792 | 71-explicit-constants.md:1797–1802 |
| 41 | rem:ec-lb-unbounded (9 → 9) | 71:1796–1804 | 71-explicit-constants.md:1806–1814 |
| 42 | sec:uc-data-order, end of the opening (3 → 3) | 71:4925–4927 | 71-explicit-constants.md:4935–4937 |
| 43 | rem:uc-data-order-limits (3 → 4) | 71:5225–5227 | 71-explicit-constants.md:5235–5238 |
| 44 | rem:ec-not-evaluated (9 → 10) | 71:5286–5294 | 71-explicit-constants.md:5297–5306 |
| 45 | ch:resolvent-bounds, sec:rb-scalar-blocks (3 → 4) | 70:1695–1697 | chapters/70-resolvent-bounds.md:1695–1698 |
| 46 | ch:own-data, after thm:own-data (2 → 2) | 63:70–71 | chapters/63-own-data.md:70–71 |
| 47 | the front matter, the abstract (4 → 5) | 00:33–36 | chapters/00-front.md:33–37 |
| 48 | ch:introduction, sec:introduction-scope (5 → 5) | 01:152–156 | chapters/01-introduction.md:152–156 |
| 49 | ch:theorems, sec:settling-statement, the order K (3 → 4) | 03:314–316 | chapters/03-theorems.md:314–317 |
| 50 | ch:theorems, sec:further-results, constants item (7 → 7) | 03:359–365 | 03-theorems.md:360–366 |
| 51 | ch:scope, sec:scope-constants, lower bound (5 → 6) | 90:66–70 | chapters/90-scope.md:66–71 |
| 52 | sec:scope-constants, the computational point (3 → 3) | 90:79–81 | 90-scope.md:80–82 |
| 53 | sec:scope-constants, explicit values (4 → 5) | 90:85–88 | 90-scope.md:86–90 |
| 54 | ch:s14, sec:iv4-0, after the 1-form c_C (1 → 3) | 33:126 | chapters/33-s14-constraint-damping.md:126–128 |
| 55 | sec:s14-pa, opening (1 → 1) | 33:3130 | 33-s14-constraint-damping.md:3132 |
| 56 | rem:s14-eps-ind-scope, first sentence (3 → 5) | 33:3532–3534 | 33-s14-constraint-damping.md:3534–3538 |
| 57 | rem:t49-sets (d) (1 → 1) | 33:3582 | 33-s14-constraint-damping.md:3586 |
| 58 | rem:t49-scope, first lines (7 → 7) | 33:3866–3872 | 33-s14-constraint-damping.md:3870–3876 |

After the merge, each new text occurs exactly once in its chapter. No old text survives as whole lines, with two
exceptions, both intended:
- item 2: Block B1 keeps the (C4) line and adds (C4′) after it;
- item 30: the line is kept as it stands.

New labels, each defined once:
- 46:1717, def:vi-c-admissible (Definition 38.24);
- 46:1761, prop:vi-c-adm-exist (Proposition 38.25);
- 46:1886, thm:vi-c-adm-holds (Theorem 38.27, after thm:vi-c-2-1, which is Theorem 38.26).

rem:ec-point-outside stays Remark 49.2, at 71:56. The label count goes from 4649 to 4652. In the merged chapter 46 the
rows of sec:vi-c-1 read: the definition, the proposition, then c1, u1, a1, b1–b4, w1–w2, d1–d2 and n1.
`git diff bcece9fb HEAD -- chapters` has 47 hunks, all from these items.

## 2. Crosswalk

**Pin.** `git show 6f066bb5:research/warp-drive/paper/reader/proofs/P-ADM.md` has md5
bb8171d26e255d564043bda5ae5a75c5, the same as the working file. In the three new rows,
"paper/reader/proofs/P-ADM.md@PENDING:" became "paper/reader/proofs/P-ADM.md@6f066bb5:". I checked that lines 20, 64
and 106 of P-ADM.md carry the three `{#label}`s.

**New rows.** These are the file's rows with the four-space indent removed and the pin replaced. Each has 4
tab-separated fields.
- crosswalk/46-s27-nonlinear.tsv:53, def:vi-c-admissible, and :54, prop:vi-c-adm-exist. Both go directly after
  sec:vi-c-1 (:52).
- crosswalk/46-s27-nonlinear.tsv:57, thm:vi-c-adm-holds, directly after thm:vi-c-2-1 (:56).

This is chapter order: sec:vi-c-1, def, prop, sec:vi-c-2, thm:vi-c-2-1, thm:vi-c-adm-holds.

**Notes on existing rows.** Each note is appended after "; ". Where the note column was empty, the note became the
column, with no "; " in front. These were sec:iii-f-1, lem:iii-g2-1-2, thm:iii-g2-3-1, sec:iii-g4-1, thm:iii-g4-3-1 and
sec:iii-i10-1.

- 46-s27-nonlinear.tsv:
  - :4, sec:iii-k-0, "parameters: an admissible point (P-ADM text 19)";
  - :52, sec:vi-c-1, "rows c2–c4 and u2–u5 replaced by def:vi-c-admissible, prop:vi-c-adm-exist and row a1; thresholds
    of b2, b3, w1, d1, d2 re-keyed (P-ADM texts 20–27)";
  - :56, thm:vi-c-2-1, "steps (1)–(2): an admissible point and the numbers it fixes; proof sentence on steps (1)–(2);
    thm:vi-c-adm-holds after it (P-ADM texts 28–30)".
- 34-s15-linearised.tsv:
  - :3, sec:iii-f-1, "results hold at admissible points (P-ADM text 1)";
  - :18, sec:iii-f1-1, "(C4′) added (P-ADM text 2)";
  - :23, prop:iii-f1-2-3, "(f) under (C4′); (g) simplicity on [−101, 0] for every z ∈ (0, ½] (P-ADM texts 3–5)".
- 35-s16-iota-plus.tsv:
  - :2, ch:s16, "(C1) at admissible points from (AP0) (P-ADM text 6)";
  - :96, sec:iii-g2-1, "simplicity from prop:iii-f1-2-3 (g); (C5) at admissible points (P-ADM texts 7, 8)";
  - :99, lem:iii-g2-1-2, "simplicity from (g) (P-ADM text 9)";
  - :118, thm:iii-g2-3-1, "simplicity from (g) (P-ADM text 10)".
- 36-s17-null-infinity.tsv, each with "simplicity only on [−101, 0], from (g)" and its own tag:
  - :84, sec:iii-g4-1 (text 11);
  - :88, lem:iii-g4-1-1 (texts 12, 13);
  - :101, thm:iii-g4-3-1 (text 15);
  - :107, lem:iii-g4-3-4 (text 14).
- 41-s22-kerr-face.tsv:
  - :4, sec:iii-i10-1, "s_C > 100 cited to sec:iii-f-1, not to (C1) (P-ADM text 16)";
  - :50, lem:iii-i12-2-3, "simplicity from (g) (P-ADM text 17)".
- 42-s23-augmentation.tsv:25, sec:iii-j-1, "s_C > 100 cited to sec:iii-f-1 (P-ADM text 18)". sec:iii-j-1 is the
  section whose setting paragraph ("Everything of [[sec:iii-i14-1]] is kept") item 18 edits.
- 71-explicit-constants.tsv: the file's note, "admissible points; the lower bound on the proved set at h ≤ 10⁻⁶; the
  computational point not shown to lie in the proved set", goes on each of its eleven rows:
  - :2, ch:explicit-constants (texts 31, 32);
  - :5, rem:ec-point-outside (text 33);
  - :66, thm:loss-d (34);
  - :68, prop:ec-delta-cap (35);
  - :69, sec:ec-lb-proved (36);
  - :79, thm:ec-lb-proved (texts 37, 38);
  - :83, rem:ec-lb-conditions (texts 39, 40);
  - :84, rem:ec-lb-unbounded (41);
  - :224, sec:uc-data-order (42);
  - :229, rem:uc-data-order-limits (43);
  - :235, rem:ec-not-evaluated (44).
- 70-resolvent-bounds.tsv:100, sec:rb-scalar-blocks, "point not shown to lie in the proved set (P-ADM text 45)".
- 63-own-data.tsv:3, thm:own-data, "point not shown to lie in the proved set (P-ADM text 46)".
- 01-introduction.tsv:9, sec:introduction-scope; 03-theorems.tsv:20, sec:settling-statement, and :22,
  sec:further-results; 90-scope.tsv:4, sec:scope-constants. See §3 (c).
- 33-s14-constraint-damping.tsv:
  - :7, sec:iv4-0, :159, sec:s14-pa, and :182, rem:s14-eps-ind-scope, "the theorems at admissible points; 𝖧 is where
    thm:iii-e-1-1 is stated", tagged text 54, 55 and 56;
  - :184, rem:t49-sets, "no rows named; the exclusions met at the point although not asked (P-ADM text 57)";
  - :201, rem:t49-scope, the same note (text 58). It *replaces* the old note "rows c2, c3, u5", as the file says, so
    that column now holds only the new note.

No "PENDING" is left in any crosswalk file.

## 3. Adjusted, and why

The chapter texts needed no adjustment. Every old text was found exactly once at its stated line, and every new text
and block was applied byte for byte. The adjustments are all in the crosswalk notes:

(a) **Tag form.** The file writes its tags "(P-ADM item N)". You asked for "(P-ADM text N)" "as earlier merges did",
and every existing tag in crosswalk/ has that form (P-K, P-LB, P-T49, P-T78). So I wrote "text" for one item and
"texts" for several, as P-K's "(P-K texts 4–5)" does. N is always the file's item number.

(b) **Per-row tags in grouped notes.** Some of the file's notes name several rows with one collective tag:
- "items 31–44" for the eleven rows of chapter 71;
- "items 54–56" and "items 57, 58" in chapter 33;
- "items 9, 10" and "items 11–15" in chapters 35 and 36.

I kept the note text verbatim, but tagged each row with the items that edit that row, so that each tag points to its
own edit.

(c) **Notes the file does not give.** For four rows the file names only the item, with no note text:
- sec:introduction-scope (item 48);
- sec:settling-statement and sec:further-results (items 49, 50);
- sec:scope-constants (items 51–53).

I wrote short notes from what those items do:
- for 48, 49 and 50: "the lower bound on the proved set at γ_C ≥ 10⁶; the point not shown to lie in the proved set";
- for 51–53: the same, plus "; the parameters fixed only at admissible points".

These notes are mine. Please check or reword them.

(d) **The abstract (item 47).** crosswalk/00-front.tsv holds only its header, because the front matter has no labels.
So there is no row for the note, and I added none.

(e) **Which row owns a site.** For items 4, 5, 8, 10, 11, 14, 15, 19, 38, 49 and 54, the nearest `{#label}` above the
edited lines is an equation label (or, for item 49, thm:settling). The file names the enclosing result or section
instead, for example prop:iii-f1-2-3 for items 4–5, sec:iv4-0 for item 54 and sec:settling-statement for item 49. I
followed the file. For item 49, P-K's note on the same paragraph sits on sec:settling-statement too.

## 4. Checks

- `python3 lint.py --chapters`: "chapters: 62 file(s), 4652 label(s) defined, 0 hit(s)".
- `python3 assemble.py --check`: "labels 4652, computations cited 0, problems 0".
- The in-memory check prints `[] 0`:
  `python3 -c "import sys; sys.path.insert(0,'.'); import assemble as a, lint; n,l,p1=a.number(a.load());
  f,c,o,p2=a.resolve(n,l); print(p1+p2, lint.report('PAPER.md', lint.scan_text('PAPER.md','\n'.join(f),assembled=True)))"`.
- **Crosswalks.** In each of the 13 touched crosswalks:
  - the rows match the chapter's `{#label}`s one for one and in chapter order;
  - every row has 4 fields;
  - no label repeats.

  | crosswalk | labels | rows |
  |---|---|---|
  | 01 | 9 | 9 |
  | 03 | 21 | 21 |
  | 33 | 200 | 200 |
  | 34 | 97 | 97 |
  | 35 | 131 | 131 |
  | 36 | 140 | 140 |
  | 41 | 73 | 73 |
  | 42 | 52 | 52 |
  | 46 | 65 | 65 |
  | 63 | 124 | 124 |
  | 70 | 113 | 113 |
  | 71 | 234 | 234 |
  | 90 | 8 | 8 |
- **Line length.**
  - Every new or changed chapter line is at most 121 characters.
  - The longest raw line in each of the 14 touched chapters is 120 or 121 characters.
  - The assembled, label-resolved paper has 98,669 lines; the longest is 121 characters, and none is longer.
- **Markers.** I checked every inserted or changed line that follows a non-blank line. None starts with "+ ", "- ",
  "* ", "> ", "#", "=" or "|", except the four bullets of item 39, at 71:1788–1791. Each of those follows another
  bullet, as intended.
- P-ADM.md is in place, with md5 bb8171d26e255d564043bda5ae5a75c5.

## 5. Left for the coordinator (not changed)

- **The file's side finding 4.** It concerns lem:iii-i11-2-1 (41:575–590): the list of roots behind E′ omits the roots
  ι^C_(·,+) − 1 that come from □^C, some of which lie below real part 3. The file reports this for the coordinator; it is
  not part of the placement and is not repaired.
- **Old marks in the notes.** Several earlier crosswalk notes still describe rows that this merge removes. For example,
  "rows u3 and u4 without epsilon_L and gamma_1 (P-T78 text 6)" on sec:vi-c-1, and "the bounds of rows u3-u4" on
  rem:ec-lb-conditions. They stay, because a note records history. The file asks to replace only the note on
  rem:t49-scope.
- **P-TR.** The file says P-TR's form B was written against this merged state. I did not check P-TR, as it is outside
  this placement.
