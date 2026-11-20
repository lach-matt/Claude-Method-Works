# M-71-small: merge of P-U71-small into chapter 71

**Source.** proofs/P-U71-small.md, md5 2e4c1bcc85f09ad5bfe3837eab493cd7. This is the version with R2-P-U71-small's nit N1
applied (lines 165–167), the same as HEAD 4c08cac1. It was confirmed by R-P-U71-small, F-P-U71-small and R2-P-U71-small.
A copy is kept beside this report as P-U71-small.merged-source.md.

**Files touched.**
- chapters/71-explicit-constants.md: 347 insertions, 32 deletions.
- crosswalk/71-explicit-constants.tsv: 9 rows added, 14 rows amended.
- proofs/P-U71-small.md: removed with `git rm -f`. The `-f` was needed because, when the merge started, the file carried
  the N1 change uncommitted. HEAD 4c08cac1 has since committed it, and its md5 equals the merged source's.
- Nothing was committed.

**Scripts** (scratchpad/reader/):
- merge71small.py: locates each old text with whitespace-insensitive matching, checks it, applies it, and inserts part one.
- bytecheck71small.py: the byte-identity check.
- xw71small.py: the crosswalk rows.

## Where the subsection went

Part one is proof lines 1–301: from "#### The smallness orders and the loss of the Nash–Moser step {#sec:cs-small}" through
the paragraph after prop:uc-d-small, ending "under both.". It is now **chapter 71 lines 4334–4634**:
- line 4332 is the last line of rem:cs-sharpness (as amended by text 12);
- line 4333 is blank;
- the subsection is lines 4334–4634;
- line 4635 is blank;
- line 4636 is "### The first constants of the linear theory {#sec:ec-linear}".

The Placement section was not inserted.

Assembled, the new labels number as follows:
- sec:cs-small = Section 49.12.7;
- lem:cs-sharp = Lemma 49.107, lem:uc-small-orders = Lemma 49.108;
- rem:uc-small-reading = Remark 49.109, prop:uc-d-small = Proposition 49.110;
- eq:cs-sharp, eq:uc-small, eq:uc-small-diff and eq:uc-d-small = (49.51)–(49.54).

This agrees with R2's in-memory merge.

## The 14 texts

Every old text was located by its quoted start and end phrases, or its whole line, with whitespace-insensitive matching.
For each one:
- the start phrase occurs once;
- the whole old range occurs once;
- the range spans the stated number of lines.

The end phrase of 8 ("21d_NM + 6 is the regularity of") occurs twice in the chapter. The end was taken as its first
occurrence after the unique start, and the 3-line count confirms it.

Every range text began and ended on a line boundary, including text 4 ("([[eq:ii-g-2-5]])." opens line 1465 and "By" ends
line 1467). So no line outside a quoted range had to be split. Texts 8a, 9, 10a and 10b are in-line replacements; each
old string occurs once and the rest of its line is kept.

After the merge, each new text occurs verbatim in chapter 71 exactly once (checked by script). All joins were read with 3
lines on either side, and each paragraph reads continuously.

| Text | Where | Old lines (before) | New lines (after) |
|---|---|---|---|
| 1 | sec:ec-accounted, paragraph defining d_NM | 162–166 | 163–169 |
| 2 | thm:loss-d, statement | 1431–1434 | 1434–1438 |
| 3 | paragraph after (iii) of thm:loss-d | 1460–1461 | 1464–1466 |
| 4 | proof of thm:loss-d | 1465–1467 | 1470–1473 |
| 5 | prop:ec-delta-cap | 1493 | 1499–1500 |
| 6 | (4) of rem:ec-upper-open | 1938–1940 | 1945–1948 |
| 7a | opening of sec:uc-close, line | 1953 | 1961 |
| 7b | opening of sec:uc-close, two lines | 1960–1961 | 1968–1970 |
| 8a | lem:uc-phi-loss, title (in line) | 2222 | 2231 |
| 8b | lem:uc-phi-loss, statement line | 2231 | 2240 |
| 8c | proof of lem:uc-phi-loss | 2243–2245 | 2252–2254 |
| 9 | (ii) of thm:uc-reduction (in line) | 2255 | 2264 |
| 10a | lem:uc-dr, statement (in line) | 2444 | 2453 (121 characters, as the text says) |
| 10b | proof of lem:uc-dr, last sentence (in line) | 2457 | 2466 |
| 11a | thm:uc-integer, display eq:uc-integer | 2466 | 2475 |
| 11b | thm:uc-integer, "The losses of …" | 2473 | 2482–2483 |
| 11c | proof of thm:uc-integer | 2489–2491 | 2499–2501 |
| 12 | rem:cs-sharpness, last three lines | 4317–4319 | 4330–4332 |
| 13 | opening of the chapter | 22–23 | 22–24 |
| 14 | rem:uc-missing, last line | 2519 | 2529–2532 |

None of the old phrases remains: no "d_NM = max(d_R, …", "two other components of d_NM", "then d_NM = d_R", "so that
d_NM equals it" or "whose largest is d_NM". The only "d_NM = max" left is the new display eq:uc-d-small. No other chapter
carries those phrases.

## Crosswalk

**Added**, after rem:cs-sharpness and before sec:ec-linear, in order of definition. Each has source "proofs/P-U71-small.md
(merged)" and source_name "P-U71-small", with the result's title where there is one:

| Label | Note (short form) |
|---|---|
| sec:cs-small | merged verbatim at the end of sec:cs; the d of thm:iii-k-3-2 is the largest of the three results' d's, including the smallness orders; introduces K̄, R_base and the base charge |
| lem:cs-sharp | K ≤ K̄; d_acc, d_R ≤ D_♭ < 2.6193·10⁴⁹ |
| eq:cs-sharp | display: d_acc, d_R ≤ D_♭ and the integer D_♭ |
| lem:uc-small-orders | the orders (a)–(d); d_* ≤ D_* = T_12 + 14 < 2.14559·10³⁵; m + 14 ≤ d_* |
| eq:uc-small | display: D_* := T_12 + 14 |
| eq:uc-small-diff | display (F1) |
| rem:uc-small-reading | the remainder-bounding reading: d_* ≤ D′_* < 2.6193·10⁴⁹ |
| prop:uc-d-small | d_NM = max(d_R, d_* + d_F + d_Φ) ≥ d_R ≥ d_acc; < 2.6193·10⁴⁹ or < 5.2386·10⁴⁹, below D_acc; lower bounds carry over; paragraph after it |
| eq:uc-d-small | display: d_NM = max(d_R, d_* + d_F + d_Φ), d_F ≤ d_R, d_acc ≤ d_R ≤ d_NM |

**Amended.** Each row had "; P-U71-small: …" appended to its note, naming the text number:
- ch:explicit-constants (13);
- sec:ec-accounted (1);
- def:ec-accounted-loss (1);
- thm:loss-d (2–4);
- prop:ec-delta-cap (5);
- rem:ec-upper-open (6);
- sec:uc-close (7);
- lem:uc-phi-loss (8);
- thm:uc-reduction (9);
- lem:uc-dr (10);
- thm:uc-integer (11);
- rem:cs-sharpness (12);
- rem:uc-missing (14).

Three of these rows go beyond the list in the task:
- **def:ec-accounted-loss.** Its existing note says that "the paragraph after it defines d_NM (largest of the losses
  …)". Text 1 rewrites exactly that paragraph.
- **ch:explicit-constants.** It owns the chapter's opening, which text 13 changes.
- **sec:uc-close.** It owns the section's opening, which text 7 changes.

lem:uc-phi-loss's source_name keeps the old title, since it names the source as it was; the note records the new title.

**Check (script).** The chapter's {#kind:key} labels, in order, match the crosswalk's label column exactly:
- 212 labels and 212 rows, all unique;
- the two sequences are identical;
- every row has 4 fields.

## Byte identity

This was checked by bytecheck71small.py before the `git rm`:
- Chapter lines 4334–4634 are identical to proof lines 1–301. md5 7df6965f248e39f518afeae13f581fe6 on both sides.
- The part has 47 blank-line-separated blocks. All 47 are byte-identical in place, and each occurs once in the chapter.
- The line before the part is blank, the line after it is blank, and the next line is the sec:ec-linear heading.
- The 16 multi-line new texts and the 4 in-line ones each occur verbatim exactly once.

## Check outputs

- `python3 lint.py --chapters`: `chapters: 62 file(s), 4579 label(s) defined, 0 hit(s)`. Before the merge it was 4570.
- `python3 assemble.py --check`: `labels 4579, computations cited 0, problems 0`.
- The number/resolve/lint snippet prints `[] 0`.
- No line in the assembled paper is longer than 121 characters, and the longest source line of chapter 71 is 121.
- `python3 assemble.py` was not run without --check.

The diff of chapter 71 and the crosswalk is M-71-small.diff (612 lines), in this directory.
