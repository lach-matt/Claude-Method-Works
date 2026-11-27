# F2-P-G24b: second fix round on proofs/P-G24b.md

The file was a44f9f97a98e435754cf15153bedef33 (1,645 lines). It is now **01ed4e5b9a768c1b93bfa12a2695b075, 1,673 lines**.
I edited only proofs/P-G24b.md. Nothing is committed. proofs/P-RI.md was not touched. PAPER.md in the real directory was not
rebuilt.

## Findings of R2-P-G24b

| item | outcome |
|---|---|
| r1 | Applied as written. T35 now reads "{τ ≥ (0.75/10)T}" (line 1405), and so does the thm:iv6-2-1 crosswalk note. I checked it first: χ_(τ,0) is 0 for τ ≤ T/40 and 1 for τ ≥ (0.75/10)T (sec:iv5-1, chapter line 1975). |
| n-a | Applied as written. |
| n-b | Applied with a change. The review's header text named the old base (147ca162, P-ADM). The header now names the chapter at HEAD (P-G1 merge dff79ca7, md5 d2184d75…) and adds "as whole lines". Line 1622 was rewrapped as written. Other lines also broke the 121-character limit, so I fixed them too: the 27 rows of the §2.2 table (up to 305 characters) are now a wrapped list; the T41 heading was 128 characters; the prop:iv5-2-1 crosswalk note was 122. The proof file now has no line over 121 except the tab-separated crosswalk rows. |
| n-c | Applied as written. The T22 header now says "New (12 lines)". |
| n-d | Applied with a change. The wording is the review's. The T45 old text now runs to the end of its chapter line (see "Whole lines" below), so the new text keeps that line's tail, " [[prop:iv5-1-3]] needs only". I rewrapped the three lines to 95, 109 and 86 characters to avoid a short last line. |
| n-e | Applied as written. The T4 header now says "New (37 lines)". |
| n-f | Applied as written, at both sites (T34 and T37). |
| n-g | Applied as written. |
| n-h | Applied, with the line numbers moved to HEAD. The index-0 part is lines 3017–3049 (it was 2396–2428), and §6.1's steps (i) and (iii) are lines 3029–3045 (they were 2408–2424). The new line is 116 characters. |
| n-i | Applied, with a change of line number. The row now reads @PENDING:515, which is variant A's label line in the new file. The review's 479 was that label's line in the old file. The note is as the review wrote it. |

## Line numbers, md5 and whole lines

- **Line ranges and md5.** Every T header range was recomputed from the chapter at HEAD (md5 d2184d75…) by locating its old
  text. All 45 agree with the review's table. Ranges that end on a blank line include it: T4 is 2066–2068 and T18 is
  2516–2517.
- **Whole lines.** Five old texts were not whole lines:
  - T15 and T16 were fragments of a line.
  - T29 and T45 ended partway through a line, already at 147ca162.
  - T7 became a partial line once C33-12 was merged.

  Each now consists of whole chapter lines, and its new text carries the same tail:
  - T7's last line is C33-12's line.
  - T29 takes in the paragraph's last line (3009), so the tail joins one 114-character line.
  - T15 and T16 are their full lines.

  All 45 old texts (T41 as variant A) occur exactly once as whole lines, and none overlaps another. T29 still ends
  before "So [[eq:iv6-1-1]] is Fredholm", and P-RI-2 starts at "*Index 0.*" (line 3017), so neither of P-RI's old texts
  is touched.
- **§2 rebased.**
  - Chapter 33 now has 277 citations: [Hin26a] 203, [Hin26] 29, [Hin26c] 4, [Hin26d] 40 and [Mel93] 1.
  - Class (a-G1) is now empty.
  - New entry: sec:iv5-calc, lines 1390–1964, with [Hin26d] ×40, class (c). Every [Hin26d] item cited there appears in
    Appendix A's thm:std-sbg-calculus, (S1)–(S16).
  - The other entries were mapped by a diff from 147ca162 to d2184d75. P-G1's changed sites were reclassified by hand.
  - A closing paragraph says where each old (a-G1) site went, and why the counts changed: [Hin26a] 208 → 203, [Hin23d]
    2 → 0, [Shu92] 1 → 0 and [Hin26d] 3 → 40.
  - Coverage was checked by script. All 253 citation lines lie in an entry, and every single line an entry lists
    carries a citation.
- **§8 rewritten.** It says that P-G1 is merged and its proof file retired (rows pinned @3b715dd5), and that the
  overlapping texts already reflect it:
  - C33-11/T41: use variant A, at lines 2137–2138.
  - C33-12/T7: the old text runs to the end of line 2143.
  - C33-20/T34: the paragraph is at lines 3110–3112, before T34's old text.
  - T42/C33-9 and T5/C33-10 are adjacent. A script found no other contact with any P-G1 site.
- **Other sections updated.** The T34 note, the T41 intro and §6.2 now describe P-G1 as merged. The §5 intro states the
  whole-lines convention, and §7 carries the new checks.
- **T41's first variant is kept.** Its old text no longer occurs in the chapter. It is marked "kept for comparison only",
  and variant A is marked as the one to apply. The coordinator may drop it.

## Scratch merge

The scratch copy is in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/f2pg24b/reader/.
It is the `git archive` of HEAD a5fe9baa, with chapter 33 md5 d2184d75…. I applied T1–T45 (T41 as variant A) as
whole-line replacements, read from the final proofs/P-G24b.md. I then inserted the 16 crosswalk rows after their anchors
and appended the 19 notes.

| check | before | after |
|---|---|---|
| lint.py --chapters | 4665 labels, 0 hits | 4681 labels, 0 hits |
| assemble.py --check | 4665 labels, 0 problems | 4681 labels, 0 problems |
| assemble.py, then lint.py --paper | — | PAPER.md: 0 hits |
| longest line (characters): chapter 33 raw / resolved / PAPER.md | — | 121 / 121 / 121 |
| conservative test (new labels as "Proposition 49.999" / "(49.999)") | — | chapter 33 longest 121 |
| backslashes in chapter 33 | — | 0 |
| wrapped lines starting "+ ", "- ", "* ", "> ", "#", "=", "\|" | 0 | 0 (chapter 33 and its part of PAPER.md) |
| proof file lines over 121 (tab rows excepted) | 27+3 | 0 |
| crosswalk 33 | 213 rows | 229 rows for 229 labels, one per label, in chapter order |

- The merged chapter 33 has md5 f27c5f5e55aeb178d977b79de96741ee.
- The review's scratch chapter with the nits applied (r2pg24b-nits, 4c496d0d…) differs from mine in two places only, both
  rewraps with the same wording: T45 (n-d) and T29's tail.
