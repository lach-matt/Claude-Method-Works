# M-CIVP3: merge of proofs/P-CIVP3.md (Tier 3, cone data through the axes) into chapters 83, 81, 03 and 90

Input: proofs/P-CIVP3.md, CONFIRMED by notes/reviews/R-P-CIVP3.md ("Final confirmation").
- md5 dfa0b5519b02565e8586e46db00d12a4, 1,109 lines. The section is lines 1–823, line 824 is blank, Placement runs
  825–1063, and the crosswalk rows run 1064–1109.
- `git show 31936331:./proofs/P-CIVP3.md` is byte-identical to the working file. No commit after 31936331 touches the
  file, and its md5 is the same after the merge.
- I did not edit, delete or commit any file in proofs/.

Base: 50d0899b, the head when I started. No commit between 0c8952c0 (the scratch merge) and 50d0899b touches
chapters/ or crosswalk/.

**About commits.** I made no commit. Snapshot commits by another agent took in my edits:
- 52609127 took the four chapter files.
- 3aff0fa6 took the four crosswalk files.
- Both commits also carry proof files that are not mine (P-HF, P-UB2, P-CIVP5).

I rebuilt the merge with the same four scripts from a `git archive` of 50d0899b. The rebuilt chapters/ and crosswalk/
are identical to the working tree (`diff -rq` is empty), and the working tree equals HEAD (51d38d8a) for both
directories. The only commits since 50d0899b that touch chapters/ or crosswalk/ are 52609127 and 3aff0fa6. The others
(326f4363, f967dca2, 099e8d51, e8453e08, 03ea039e, e72ef24e, 51d38d8a) touch other files.

The diff is `git diff 50d0899b HEAD -- chapters crosswalk`: 8 files, 926 insertions, 49 deletions, 19 hunks. It is
saved as /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/reports/M-CIVP3.diff
(md5 e9b4248a5a6d6b679e8366d9c2557031). A plain `git diff` of chapters/ and crosswalk/ is now empty, because everything
is committed.

## 1. Placement items

**Checks before the edits.**
- Each old text occurred exactly once, as whole lines, in its own chapter and in all 62 chapters, at the line the file
  gives.
- For item 1, the heading "### Null shells along the leaves {#sec:loc-shells}" occurred once (83:2409). The line before
  it was blank, and the line before that was the last line of rem:civp-large-beyond ("not explicit and no estimate of
  the solution is given.", 83:2407).
- None of the 30 labels was defined in chapters/ before the merge.
- No item stopped.

**Copying.** Every new text was copied byte for byte from the file's lines, and so was the section, lines 1–823.

**Checks after the edits.**
- Each new text occurs exactly once in chapters/.
- Every old text is gone.
- The section occurs once.

| Item | Site | Old (50d0899b) | New (now) |
|---|---|---|---|
| 1 | the section, sec:loc-axis … rem:loc-axis-scope, after rem:civp-large-beyond and before sec:loc-shells, one blank line before and one after | before 83:2409 | 83:2424–3246, with blank lines at 2423 and 3247. rem:civp-large-beyond now ends at 2422, and the sec:loc-shells heading is at 3248. |
| 2 | ch:localised-data, the opening paragraph (2 → 4 lines) | 83:13–14 | 83:13–16 |
| 3 | the paragraph after rem:loc-cone-scope, its lines 707–708 (2 → 8 lines) | 83:707–708 | 83:713–720 |
| 3 cont. | the same paragraph, its last five lines (5 → 5 lines) | 83:717–721 | 83:729–733 |
| 4 | rem:loc-cone-scope (ii), its last two sentences (5 → 7 lines) | 83:684–688 | 83:686–692 |
| 5 | rem:loc-cone-scope (iv) (3 → 5 lines) | 83:698–700 | 83:702–706 |
| 6 | rem:loc-cone-local-scope, its last sentence (3 → 5 lines) | 83:1644–1646 | 83:1656–1660 |
| 7 | rem:civp-large-domain, its last sentence (5 → 6 lines) | 83:2385–2389 | 83:2399–2404 |
| 8 | ch:class-system, lem:class-leaf-differences, the definition of the leaves (4 → 8 lines) | 81:1326–1329 | 81:1326–1333 |
| 9 | ch:theorems, the bullet "More families" (6 → 8 lines) | 03:376–381 | 03:376–383 |
| 10 | ch:scope, the paragraph on localised data, its last seven lines (7 → 9 lines) | 90:217–223 | 90:217–225 |
| 11 | no change | — | — |
| 12 | Appendix A and the references: no change | — | — |
| 13 | proof of prop:bg-slice, the paragraph *The packet*, rewrap only (5 → 5 lines) | 83:4707–4711 | 83:5546–5550 |

**Positions the coordinator asked for.**
- The paragraph after rem:loc-cone-scope was 83:702–721 and is now **83:708–733** (26 lines).
- lem:class-leaf-differences keeps its label line, **81:1324**. The lemma runs 81:1324–1357, with its proof at
  1344–1357; it ran 1324–1353 before. The definition of the leaves is now **81:1326–1333**.

**File lengths.**
- Chapter 83: 5,381 → 6,220 lines (+839 = 823 + 1 + 2 + 6 + 0 + 2 + 2 + 2 + 1 + 0).
- Chapter 81: 1,671 → 1,675 lines.
- Chapter 03: 398 → 400 lines.
- Chapter 90: 257 → 259 lines.

**Assembled numbering.**
- sec:loc-axis is Section 53.6, with subsections 53.6.1–53.6.4: sec:loc-axis-data, sec:loc-axis-leaves,
  sec:loc-axis-reduced and sec:loc-axis-example.
- Every later section of the chapter moves by one. sec:loc-shells moves from 53.6 to 53.7, sec:loc-kid is 53.8, and
  sec:margins is 53.15.
- Results:
  - Theorem 53.41 (thm:loc-axis) and Definition 53.42 (def:loc-axis-data).
  - Lemmas 53.43–53.55: lem:loc-axis-constraints, lem:loc-axis-jets, lem:loc-axis-leaf, lem:loc-axis-shear,
    lem:loc-axis-system, lem:loc-axis-energy, lem:loc-axis-cauchy, lem:loc-axis-past, lem:loc-axis-propagation,
    lem:loc-axis-gauge, lem:loc-axis-dependence, lem:loc-axis-unique and lem:loc-axis-angle.
  - Corollary 53.56 (cor:loc-axis-cones).
  - Remarks 53.57 and 53.58 (rem:loc-axis-constants, rem:loc-axis-scope).
- Equations (53.34)–(53.40): eq:loc-axis-cone, eq:loc-axis-principal, eq:loc-axis-hl, eq:loc-axis-shear,
  eq:loc-axis-time, eq:loc-axis-region and eq:loc-axis-closure.
- Later labels move as expected:
  - def:loc-shell-solution: 53.41 → 53.59, and rem:loc-shell-scope: 53.52 → 53.70.
  - eq:loc-shell-einstein: (53.34) → (53.41).
  - prop:bg-rays is Proposition 53.102 and prop:bg-slice is Proposition 53.104.
  - lem:class-leaf-differences stays Lemma 51.28.

## 2. Crosswalk

**New rows (30).**
- They are the file's rows 1072–1101, copied verbatim with their tabs. The only change is "@PENDING:" → "@31936331:".
- A script checked each N against `git show 31936331:./proofs/P-CIVP3.md`: N is the one line carrying `{#label}`, and
  there are 0 mismatches. The row labels are the section's labels in order.
- The rows sit at crosswalk/83-localised-data.tsv lines 90–119, from sec:loc-axis (:1) to rem:loc-axis-scope (:812).
  They come directly after rem:civp-large-beyond (89) and before sec:loc-shells (now 120).
- Rows: 248 → 278.

**Changed cells on existing rows (9 rows).** Each cell is appended after "; " and ends with a tag
"(P-CIVP3 text N)", N the item number. The tag for items 4 and 5 is "(P-CIVP3 texts 4–5)", as in "(P-K texts 4–5)".

The four rows the file names use the file's own texts, with the tag added:

| Crosswalk:line | Label | Change |
|---|---|---|
| 81:62 | lem:class-leaf-differences | source + "; paper/reader/proofs/P-CIVP3.md@31936331:965-987" (the lines of item 8 at that commit); source_name + "; proof P-CIVP3, Placement 8"; note + "; H_L[Θ_A] read with p_A(n) and the γ3-orthogonal complement of the spatial part of p_A, a plane fixed by p_A (eq:loc-axis-hl) (P-CIVP3 text 8)" |
| 83:26 | rem:loc-cone-scope | note + "; (ii) and (iv) amended by proof P-CIVP3, Placement 4 and 5 (P-CIVP3 texts 4–5)" |
| 83:57 | rem:loc-cone-local-scope | note + "; last sentence amended by proof P-CIVP3, Placement 6 (P-CIVP3 text 6)" |
| 83:88 | rem:civp-large-domain | note + "; a sentence on thm:loc-axis appended by proof P-CIVP3, Placement 7 (P-CIVP3 text 7)" |

The file gives no crosswalk text for five other sites it changes. Following M-SHELL and M-CIVP12, I wrote these notes
from each item's new text. Each is a note only, and no source was changed.

| Crosswalk:line | Label | Note appended |
|---|---|---|
| 83:2 | ch:localised-data | the opening paragraph adds, before the sentence on Σ_τ0, the sentence on data near the background's that are not localised away from the axes, developed on the whole rectangle spanned by the two cones (thm:loc-axis, cor:loc-axis-cones), text of proof P-CIVP3 (P-CIVP3 text 2) |
| 83:21 | prop:loc-cones | the closing paragraph adds the development near the background's of cone data not restricted to a band, on every rectangle [0, 7.2] × [0, v_1] (thm:loc-axis, cor:loc-axis-cones), names the data of thm:civp-large as those localised in a band, and narrows the data not developed to those that differ from the background's near an axis and are not near the background's (rem:loc-axis-scope), text of proof P-CIVP3 (P-CIVP3 text 3) |
| 83:245 | prop:bg-slice | the paragraph The packet of its proof rewrapped so that every line fits 121 characters after assembly; no word changed (P-CIVP3 text 13) |
| 03:22 | sec:further-results | the More families bullet lists separately the data localised in a band (thm:civp-large, thm:loc-cone-development) and the data near the background's, localised in angle or not, developed on the whole rectangle of the two cones (thm:loc-axis, cor:loc-axis-cones), text of proof P-CIVP3 (P-CIVP3 text 9) |
| 90:7 | sec:scope-families | the paragraph on localised data adds the development of cone data near the background's on the whole rectangle of the two cones (thm:loc-axis, cor:loc-axis-cones) and narrows the developments not established to data that are not near the background's (rem:loc-cone-scope, rem:loc-axis-scope), text of proof P-CIVP3 (P-CIVP3 text 10) |

Text 3, which is the closing paragraph after rem:loc-cone-scope, goes on prop:loc-cones. That row already traces the
paragraph ("(P-CIVP text 4)", "(P-SHELL text 8)").

The prop:bg-slice note follows the wording of the rewrap rows in crosswalk/71 and crosswalk/33.

Items 1, 11 and 12 need no note on an existing row.

**Checks on the crosswalk.**
- No crosswalk file contains "PENDING".
- Every row of the changed files has exactly 4 fields.
- In every chapter, the crosswalk's label column equals the chapter's sequence of `{#…}` labels, in order.

## 3. Label counts

| | Before (50d0899b) | After |
|---|---|---|
| labels defined in chapters | 4,803 | 4,833 (+30, all in chapter 83) |
| crosswalk rows, all files | 4,803 | 4,833 (+30) |
| chapter 83 labels / crosswalk 83 rows | 248 / 248 | 278 / 278 |

## 4. Checks (on the final state)

- `python3 lint.py --chapters`: 62 files, 4,833 labels, 0 hits.
- `python3 assemble.py --check`: labels 4,833, computations cited 0, problems 0.
- The in-memory check prints `[] 0`.
- Line lengths, counted in characters:
  - No line of any chapter is longer than 121 characters.
  - The assembled text has 104,102 lines, the longest 121 characters long, and none longer.
- Line starts:
  - Of the added chapter lines, only the five headings start with "#": the section heading at 83:2424 and its four
    "####" subsection headings.
  - The only indented added line that starts with "|" is a displayed formula inside an indented block (83:2806).
  - I compared the assembled text before and after: the set of lines that start with "+ ", "- ", "* ", "> ", "#", "=" or
    "|" changes only by the new headings and the renumbered section headings.
- I never ran assemble.py without --check.

The scripts are in /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/merge-civp3/:
items.py, check_old.py, apply.py, check_new.py, xw_rows.py, xw_apply.py and consistency.py. The rebuild from 50d0899b
is in rebuild/.
