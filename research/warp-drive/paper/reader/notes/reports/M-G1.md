# M-G1: merge of proofs/P-G1.md into the reader's edition

Source: `proofs/P-G1.md`, md5 b2d824fb9e0990378a7f16c0d1a726b7, 1,224 lines. The working copy is byte-identical to
`git show 3b715dd5:…/proofs/P-G1.md`, and that blob has the same md5. Base: HEAD 92c08494 at the start of the merge.
The chapter files at 92c08494 match the backups taken before the merge.

Chapter 33 at the base is not the md5 the file names (9571426c…). It is 147ca162…, because the P-ADM merge (07c2aaff)
added two lines near line 123. That is why every chapter-33 site sits 2 lines below the line number the file gives. Every
old text was still found exactly once. Chapters 23, 95 and 98 match the md5s the file names.

The coordinator's automatic "Snapshot: work in progress (P-G1 merge, proof files)" commits (86df0ccb, e504c91d, …) picked
up the edited chapters and crosswalk while I worked. I made no commit myself. Plain `git diff` is therefore empty, so
M-G1.diff is `git diff 92c08494 -- chapters crosswalk`. It touches exactly four files: chapters 33, 95 and 98, and
crosswalk 33.

## Items applied (old = line at base 92c08494, new = line after the merge)

Before each replacement, the script checked that the old text occurs exactly once, as whole lines, both in its chapter and
in all of chapters/. All 24 required sites passed.

| Item | Old file:line | New file:line |
|---|---|---|
| C33-1 | 33:1277–1279 | 33:1277–1280 |
| C33-2 | 33:1283–1286 | 33:1284–1287 |
| C33-3 | 33:1288–1295, plus blank line 1296 | deleted; one blank line is left before lem:iv5-0-2 (33:1289); the label moves to 33:1757 |
| C33-4 | inserted before 33:1398 (heading of sec:iv5-1) | 33:1390–1964 = P-G1 lines 1–575 byte for byte, then a blank line; sec:iv5-1 is now at 33:1966 |
| C33-5 | 33:1421–1423 | 33:1989–1993 |
| C33-6 | 33:1440–1441 | 33:2010–2019 |
| C33-7 | 33:1447 | 33:2025–2026 |
| C33-8 | 33:1454 | 33:2033–2034 |
| C33-9 | 33:1466 | 33:2046–2047 |
| C33-10 | 33:1508 | 33:2089–2090 |
| C33-11 | 33:1527–1531 | 33:2109–2138 |
| C33-12 | 33:1536 | 33:2143–2145 |
| C33-13 | 33:1574–1575 | 33:2183–2188 |
| C33-14 | 33:1612–1613 | 33:2225–2226 |
| C33-15 | 33:1710 | 33:2323–2324 |
| C33-16 | 33:2040 | 33:2654–2656 |
| C33-17 | 33:2109 | 33:2725–2726 |
| C33-18 | 33:2160–2162 | 33:2777–2783 |
| C33-19 | 33:2433–2434 | 33:3054–3056 |
| C33-20 | inserted before 33:2488 ("This gives [Hin26a, (B.39)] …"); T34 of P-G24b was not applied, so this is the original line | 33:3110–3112, then a blank line; the anchor is now at 33:3114 |
| C23-1 (optional) | 23:367–369 | **not applied**; the chapter is unchanged |
| C95-1 | 95:851–853 | 95:851–854 |
| C95-2 | 95:893 | 95:894–927 |
| C95-3 | inserted after 95:995 (last line of (S15)) | 95:1031–1079 ((S16), 49 lines); the anchor is at 95:1029, with one blank line before the block and one after it, before rem:std-sbg-sobolev |
| C98-1 | 98:76–77 | 98:76–77 |

**C23-1 was not applied.** The file says (lines 998–1003) that "C23-1 is to be applied only together with a check of
27:460 and 37:824". That check is not part of P-G1, so C23-1 does not apply when P-G1 is merged alone. Chapter 23 is
unchanged, and no item touches chapter 27 ("No change").

Nothing from P-G24b was applied.

**Cross-check.** I also ran the reader's own scratch-merge script (scratchpad/reader/pg1tools/merge.py, mode g1) on a
fresh copy of the base. Its chapters 23, 33, 95 and 98 are byte-identical to the merged chapters.

## Crosswalk (crosswalk/33-s14-constraint-damping.tsv)

**Removed (1 row):**

- `prop:np-10-65-a	docket68/n1star/N1STAR-PROOF.md:8189	NP 10.65 (a)	statement of [Hin23d] and [Hin26d]` (after
  def:iv5-0-1).

**Added (14 rows):** rows 69–82, after lem:iv5-0-5 (row 68) and before sec:iv5-1 (row 83). They are the file's rows with
@PIN replaced by @3b715dd5, in the file's order:

- sec:iv5-calc 1-575
- def:iv5-calc-cells 14-48
- lem:iv5-calc-structure 50-143
- def:iv5-calc-micro 145-158
- lem:iv5-calc-disjoint 160-233
- lem:iv5-calc-d 235-279
- lem:iv5-calc-dual 281-333
- lem:iv5-calc-reg 335-366
- prop:np-10-65-a 368-512
- eq:iv5-calc-ell 400
- lem:iv5-calc-garding 514-541
- eq:iv5-calc-garding 518
- lem:iv5-calc-q0 546-571
- eq:iv5-calc-q0 551

Every row is `paper/reader/proofs/P-G1.md@3b715dd5:N`. For each row, N is the line in P-G1 that carries the label: a
single line for a display, or a range from the label line to the end of the item. I kept the ranges the file gives
because the reader checked them and because the earlier merges used the same convention (P-T49, for example). For all
14, the script checked that the first line of the range carries `{#label}`.

**Changed (12 rows): the file's notes, appended.** Each note is appended after "; ", or becomes the note where the field
was empty (def:iv5-0-1, prop:iv5-1-2, 2-1, 3-1, 4-1, 5-2, 7-1, thm:iv5-7-3, sec:iv6-2). Three rows already had F-G24
notes: prop:iv5-1-3, lem:iv5-8-1 and thm:iv6-2-1.

The words are the file's. Only the closing tag is rewritten, to the coordinator's form: "(C33-5)" becomes "(P-G1 text
C33-5)", and a tag that names several items becomes "(P-G1 texts C33-1, C33-2)", "(P-G1 texts C33-6 to C33-9)" or
"(P-G1 texts C33-10 to C33-12)", following "(P-ADM texts 12, 13)". The file's leading "G1:" is kept.

The notes go to these rows, with these tags:

| Row | Tag |
|---|---|
| def:iv5-0-1 | C33-1, C33-2 |
| prop:iv5-1-2 | C33-5 |
| prop:iv5-1-3 | C33-6 to C33-9 |
| prop:iv5-2-1 | C33-10 to C33-12 |
| prop:iv5-3-1 | C33-13 |
| prop:iv5-4-1 | C33-14 |
| prop:iv5-5-2 | C33-15 |
| prop:iv5-7-1 | C33-16 |
| thm:iv5-7-3 | C33-17 |
| lem:iv5-8-1 | C33-18 |
| sec:iv6-2 | C33-19 |
| thm:iv6-2-1 | C33-20 |

No row says PENDING. Every row has exactly 4 tab-separated fields, and the header is unchanged.

The file names no crosswalk notes for chapters 95 and 98, and no labels change there, so their crosswalks are untouched.

## Label counts

- Whole edition: 4,652 before, 4,665 after (+13). The section adds 14 labels and prop:np-10-65-a moves into it.
- Chapter 33 crosswalk: 200 rows before, 213 after, for 213 labels in chapter order.

## Checks (after the merge)

- `python3 lint.py --chapters`: 62 files, 4,665 labels, **0 hits**.
- `python3 assemble.py --check`: labels 4,665, computations cited 0, **problems 0**.
- In-memory assembled check: prints **`[] 0`**.
- **Crosswalks:** every crosswalk file has one row per label of its chapter, in chapter order, with 4 fields. 0 files
  mismatch.
- **Line lengths:** no line over 121 characters (counted as characters) in any chapter. None in the assembled text with
  labels resolved either (99,379 lines, maximum 121).
- **Line starts:** the only added lines that begin with a forbidden prefix are intended ones:
  - the new heading "#### The semiclassical 3b- and eb-calculi {#sec:iv5-calc}";
  - the three "- " list items in lem:iv5-calc-dual;
  - the "- [Hin23d]" bibliography item.
- **Whitespace:** no triple newline and no new trailing whitespace in the changed files.
- **Citations:** [Hin23d] is now cited only in chapter 27, as the file states. [Shu92] is still cited, in chapters 30 and
  95.
- **Untouched files:** PAPER.md was not written, and proofs/P-G1.md is unchanged (md5 b2d824fb…).
