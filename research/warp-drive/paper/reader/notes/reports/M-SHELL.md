# M-SHELL: merge of proofs/P-SHELL.md (null shells along the leaves) into chapters 83, 90 and 98

Input: proofs/P-SHELL.md, CONFIRMED by notes/reviews/R-P-SHELL.md ("Second confirmation").
- md5 0dbc56e0d7f13174376f7e7180142946, 971 lines: section 1–820, Placement 822–944, Crosswalk 945–971.
- `git show 1af64a9e:…` is byte-identical to the working file.
- The md5 is the same after the merge. I did not edit, delete or commit any file in proofs/.

Base: HEAD ab1283b7, the P-F123 merge. Every old text was located by content in that state.

**About commits.** I made no commit. Another agent's commit, b1b958c4 ("P-UB2 final: …"), took in my three chapter
files. The two crosswalk files are still uncommitted in the working tree.

To confirm that the committed content is exactly this merge, I rebuilt it with the same two scripts from a `git archive`
of ab1283b7. The rebuilt chapters/ and crosswalk/ directories are identical to the working tree (`diff -rq` is empty).
The three chapter files are also identical to HEAD. Between ab1283b7 and HEAD, no other commit touches chapters/ or
crosswalk/.

The diff is `git diff ab1283b7 -- chapters crosswalk`: 5 files, 877 insertions, 10 deletions, 11 hunks. It is saved
as /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/reports/M-SHELL.diff
(md5 b186b75029d0371e0bd75fd2137b5ad9). A plain `git diff` now shows only the two crosswalk files, because the chapter
edits are committed.

## 1. Placement items

**Checks before the edits.** A script checked each old text before replacing it. Each one occurred exactly once, as
whole lines, in its own chapter and in all 62 chapters, at the line the file gives. No item stopped. The heading of
sec:loc-kid occurred once, still at 83:2391, and rem:civp-large-beyond came directly before it. So no other section
stood between the Tier 2 section and that heading.

**Copying.** Every new text and the inserted section were copied byte for byte from the file's lines.

**Checks after the edits.**
- Each new text occurs exactly once in chapters/.
- The old texts of items 2, 3, 5 and 8 are gone.
- The old texts of items 4 and 6 still occur once each. In both cases the new text is the old text with lines inserted
  before it, so the old lines are the end of the new text.

| Item | What | Old (ab1283b7) | New (now) |
|---|---|---|---|
| 1 | section P-SHELL 1–820, sec:loc-shells … rem:loc-shell-scope, after rem:civp-large-beyond and before sec:loc-kid, one blank line before and one after | before 83:2391 | 83:2409–3228 (blank lines 2408 and 3229); sec:loc-kid heading now 83:3230 |
| 2 | rem:loc-cone-scope (iii), its second line (1 → 6 lines) | 83:681 | 83:689–694 |
| 3 | rem:civp-large-domain, its last sentence (3 → 5 lines) | 83:2369–2371 | 83:2385–2389 |
| 4 | the chapter opening: a new paragraph before the last paragraph (2 → 10 lines) | 83:26–27 | 83:26–35 (new paragraph 26–32, blank 33, the old paragraph 34–35) |
| 5 | ch:scope, the end of the localised-data paragraph (2 → 7 lines) | 90:217–218 | 90:217–223 |
| 6 | references: [Poi02] after [MP86] and before [Rac16] (2 → 4 lines) | 98:157–158 | 98:157–160 ([Poi02] 157–158, [Rac16] 159–160) |
| 7 | Appendix A: no new entry | — | nothing to apply |
| 8 | the paragraph after lem:loc-cone-in and rem:loc-cone-scope, the last two lines of its last sentence (2 → 5 lines) | 83:704–705 | 83:717–721 (the paragraph is now 83:702–721) |
| 9 | "No other change" | — | — |

File lengths:
- Chapter 83: 4,542 → 5,381 lines (+839 = 821 + 5 + 2 + 8 + 3).
- Chapter 90: 252 → 257 lines.
- Chapter 98: 193 → 195 lines.

**New labels: 21, each defined once,** all in chapter 83. They run from sec:loc-shells at 2409 to rem:loc-shell-scope
at 3207. None was defined, or cited, anywhere in chapters/ before the merge.

**Assembled numbering.**
- sec:loc-shells is Section 53.6. sec:loc-kid moves from 53.6 to 53.7, and each later section of the chapter moves by
  one: sec:bg-below is now 53.13 and sec:margins 53.14.
- Results:
  - Definition 53.41 (def:loc-shell-solution).
  - Lemmas 53.42 and 53.43 (lem:loc-shell-ricci, lem:loc-shell-identities).
  - Proposition 53.44 (prop:loc-shell-junction).
  - Remark 53.45 (rem:loc-shell-poisson).
  - Definition 53.46 (def:loc-shell-data).
  - Proposition 53.47 (prop:loc-shell-cones).
  - Lemma 53.48 (lem:loc-shell-corner-large) and Lemma 53.49 (lem:loc-shell-corner-small).
  - Theorem 53.50 (thm:loc-shells).
  - Proposition 53.51 (prop:loc-shell-crossing).
  - Remark 53.52 (rem:loc-shell-scope).
- Equations: (53.34)–(53.41), from eq:loc-shell-einstein to eq:loc-shell-crossing-rule.
- Every number resolves from a label. No chapter source hard-codes a result number of ours.

## 2. Crosswalk

**Pin.** Each source is paper/reader/proofs/P-SHELL.md@1af64a9e:N. N is the one line that carries `{#label}` in
`git show 1af64a9e:…` (checked by script). All 21 of the file's line numbers equal those lines. No crosswalk file
contains "PENDING". Every row of the two changed files has exactly 4 fields.

**New rows (21).**
- They are the file's rows 951–971 verbatim, tabs as given, with "P-SHELL.md:" replaced by "P-SHELL.md@1af64a9e:".
- They sit at crosswalk/83-localised-data.tsv lines 90–110, from sec:loc-shells (:1) to rem:loc-shell-scope (:799), in
  chapter order. They come after rem:civp-large-beyond (89) and before sec:loc-kid (now 111).
- Rows: 227 → 248.
- The notes of two rows contain the lower-case words "pending statement T1/T2" as the file gives them. They are not
  pins.

**Notes on existing rows (5 rows, fourth field only; sources unchanged).**
- The file gives no texts for existing rows, so I wrote each note from its item's new text.
- Each is appended after "; " to a non-empty field and ends with its tag.

| Crosswalk:line | Label | Note appended |
|---|---|---|
| 83:2 | ch:localised-data | the paragraph on cone data with null shells along leaves of the two cones, before the last paragraph of the opening (thm:loc-shells, prop:loc-shell-junction, prop:loc-shell-crossing), text of proof P-SHELL (P-SHELL text 4) |
| 83:21 | prop:loc-cones | the last sentence of the closing paragraph excepts finitely many null shells along leaves of the two cones and data smooth except across such leaves, developed slab by slab by thm:loc-shells, and its last clause is narrowed to the other chapters (P-SHELL text 8) |
| 83:26 | rem:loc-cone-scope | (iii): measure-valued densities in general are not covered; finitely many null shells along leaves, and data smooth except across finitely many leaves, are covered by thm:loc-shells (P-SHELL text 2) |
| 83:88 | rem:civp-large-domain | the last sentence excepts finitely many null shells along leaves of the two cones and data smooth except across finitely many leaves, developed slab by slab with thm:civp-large in thm:loc-shells (P-SHELL text 3) |
| 90:7 | sec:scope-families | the paragraph on localised data ends with cone data with finitely many null shells along leaves of the two cones (thm:loc-shells, prop:loc-shell-crossing, rem:loc-shell-scope), text of proof P-SHELL (P-SHELL text 5) |

Text 8 goes on prop:loc-cones because that row already traces this closing paragraph ("(P-CIVP text 4)"), as M-CIVP12
recorded it.

**Not traced.**
- Text 1 needs no note on an existing row. The new section is its own section, with its own rows.
- Text 6 (the bibliography) has nowhere to go, because chapter 98 has no crosswalk file. M-CIVP12 and M-F123 handled it
  the same way.
- Text 7 changes nothing.

## 3. Label counts

| | Before (ab1283b7) | After |
|---|---|---|
| labels defined in chapters | 4,782 | 4,803 (+21, all in chapter 83) |
| crosswalk rows, all files | 4,782 | 4,803 (+21) |
| chapter 83 labels / crosswalk 83 rows | 227 / 227 | 248 / 248 |

A script compared every chapter with its crosswalk. Each crosswalk's label column equals its chapter's sequence of
`{#…}` labels, in order, with 4 fields per row and no PENDING.

## 4. Checks (on the final state)

- `python3 lint.py --chapters`: 62 files, 4,803 labels, 0 hits.
- `python3 assemble.py --check`: labels 4,803, computations cited 0, problems 0.
- The in-memory check prints `[] 0`.
- Line lengths, counted in characters:
  - No line of any chapter is longer than 121 characters.
  - The assembled text has 103,255 lines, the longest 121 characters long, and none longer.
- Line starts:
  - The only new lines that start with "- " or "#" are intended: the section heading 83:2409; the list items at
    83:2800–2803, 2811–2815, 2876–2883 and 2897–2899 (each after a blank line or another item, with indented
    continuation lines); and the two reference entries 98:157 and 98:159.
  - The assembled text of Section 53.6 shows the same items and no other such line.
- No assemble.py run without --check.

## 5. Note for the next merge (P-CIVP3, Tier 3)

proofs/P-CIVP3.md (Tier 3, data through the axes) is confirmed in notes/reviews/R-P-CIVP3.md. Its Placement already
anticipates this merge. For each site that this merge rewrote, it gives a second new text: its item 3 continued
(P-SHELL item 8), item 7 (P-SHELL item 3) and item 10 (P-SHELL item 5).

As a check, I ran each of its old texts against the chapters as they are now. Seven old texts occur once each. The three
that this merge replaced no longer occur, as expected.

Its line numbers refer to the pre-merge state. For example, its "704–705" is now 83:717–721 and its "2369–2371" is now
83:2385–2389. A merger should find each site by content.
