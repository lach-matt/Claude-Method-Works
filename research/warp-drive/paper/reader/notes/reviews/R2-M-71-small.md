# R2-M-71-small: confirming reading of the coordinator's application of R-M-71-small

## Scope

**Tree read.** HEAD 06ff986d, "Reader's edition: R-M-71-small (merge exact, chapter 62 remark true; 0M 1m 2n) applied
in the reviewer's words; …". Its parent is ff80798d. The commit touches four files: `chapters/62-interior.md`,
`chapters/71-explicit-constants.md`, `crosswalk/71-explicit-constants.tsv`, and the new `notes/reviews/R-M-71-small.md`.
The working tree is clean.

**Sources compared.**
- Each changed file at HEAD and at HEAD~1, compared word by word and field by field.
- R-M-71-small's replacement texts, compared string for string.
- `git show 4c08cac1:research/warp-drive/paper/reader/proofs/P-U71-small.md`: 438 lines, md5
  2e4c1bcc85f09ad5bfe3837eab493cd7.
- The cited targets in chapters 46, 63 and 71.

**Edits.** I edited no repository file. I tried the proposed fix below on a scratch copy of the crosswalk. I ran
`assemble.py` only with `--check`. Its `load`, `number` and `resolve` were imported in memory to measure resolved lines,
and nothing was written.

## Verdict

**CONFIRMED.** Major 0, minor 0, nit 1.

All five edits are resolved. Each new text is true where it stands, and every label it cites was checked against its
target. Word sequences against the parent change only where intended: nothing was lost or duplicated at any join. The
crosswalk has one row per label of chapter 71, in order, with 4 fields each. The contract holds, and lint and the
assembler report 0.

The single nit is bookkeeping. Three crosswalk notes still describe the d_NM definitions with the wording that the
observation edit replaced.

## One row per edit

| Edit | Where (HEAD) | Resolved | True where it stands | Joins (word sequence against ff80798d) |
|---|---|---|---|---|
| m1 | 71:1500–1502, prop:ec-delta-cap | Yes. The two lines equal R-M-71-small's replacement string for string. d_R is now named at its first occurrence in the chapter (1501); the next occurrence is 2242. The crosswalk note of prop:ec-delta-cap is a pure append of "; d_R named at its first use", and no other field changed. | Yes. [[lem:uc-dr]] (Lemma 49.58, 71:2451) defines d_R as "the number that [[def:ec-accounted-loss]] assigns to" the construction of ℛ(U) in the proof of [[lem:iii-k-2-3]], and its title is "The accounted loss of the right inverse for Ψ". [[lem:iii-k-2-3]] (Lemma 38.17, 46:1312) is the lemma that gives ℛ(U). d ≥ d_R ≥ d_acc is eq:uc-d-small together with d_R ≥ d_acc of [[thm:loss-d]] (Theorem 49.32), as the citations say. ℛ(U) is already named earlier, at 71:1473, as that of [[lem:iii-k-2-3]]. | One insertion only: "d_R the accounted loss of the right inverse ℛ(U) of [[lem:iii-k-2-3]] ([[lem:uc-dr]]);" between "d_acc," and "[[thm:loss-d]],". The join "Nash–Moser / threshold" (1502/1503) is unchanged. |
| n1 | 62:580–581, end of rem:half-class-changes | Yes. Line 581 equals the review's replacement string for string. | Yes. [[rem:own-half-changes]] (Remark 44.10, 63:282) (b): R has one factor per exponent of ℰ_0 up to the weight reached (3 or 4 against 2), so "d_1 changes by a finite amount, and ε with it". Its ε is the threshold of [[thm:iii-k-4-3]] (63:270, "with ε and d_1 chosen in step (6)"), which chapter 62 writes ε_n. The remark lies inside [[sec:own-half-class]] (63:189), so the gapped "shows" reads correctly. The new text does not claim that d changes, which agrees with R-M-71-small 5b. | One replacement only: "rise." became "rise, and [[rem:own-half-changes]] that d_1 and ε_n change through the exponents of ℰ_0^½.". The next paragraph, "So the continuation of", is unchanged. Crosswalk row 62:21 carries only a citation note, so it is not stale. |
| n2 | crosswalk/71:199–207 | Yes. In all 9 rows, fields 2 and 3 equal the review's table cell for cell. Fields 1 and 4 are unchanged. | Yes. Each line number is that label's own `{#…}` line in the file at 4c08cac1: 1 sec:cs-small, 29 lem:cs-sharp, 33 eq:cs-sharp, 69 lem:uc-small-orders, 92 eq:uc-small, 101 eq:uc-small-diff, 221 rem:uc-small-reading, 241 prop:uc-d-small, 251 eq:uc-d-small. The path resolves at 4c08cac1 (44b114b5~1) and is retired at HEAD. The form `paper/reader/proofs/<file>@<commit>:<line>` and the source_name "d-bound proof small, …" match the family (for example `P-U71-assembly.md@d1509feb`, which resolves). | No other row of the crosswalk changed. |
| obs. a | 71:163–167, paragraph after def:ec-accounted-loss | Yes. It reads "as their proofs fix them ([[prop:uc-d-small]] at the computational point)", the review's suggested wording verbatim. | Yes. See §2 below. | One replacement only: "as [[prop:uc-d-small]] fixes them." became "as their proofs fix them ([[prop:uc-d-small]] at the computational point).". The rewrap now leaves a 25-character line, 167 ("at which its proof asks U"), before "small; for …". That line is not counted; see the observations. |
| obs. b | 71:1434–1440, thm:loss-d | Yes. It reads "that their proofs fix ([[prop:uc-d-small]] at the computational point)", the suggested wording in the relative form. | Yes. See §2 below. | One replacement only: "that [[prop:uc-d-small]] fixes," became "that their proofs fix ([[prop:uc-d-small]] at the computational point),". Rewrapped, it ends "… N_NM =" / "21d_NM + 6, d_NM ≥ d_acc, and:". 507 chapter lines end in " =", so that break is house practice. |

## Checks

### 1. n2 line numbers

`git show 4c08cac1:…/proofs/P-U71-small.md` has 438 lines, md5 2e4c1bcc85f09ad5bfe3837eab493cd7, the merged source. Each
of the 9 line numbers prints the line that carries the label's own `{#kind:key}`. The file's only other label,
`{#eq:uc-integer}` at 402, belongs to the Placement section and has no row here. That is correct, because eq:uc-integer
keeps its own row from P-U71-close.

### 2. The d_NM definitions away from the computational point, and at it

**Away from the point.** sec:ec-accounted (163–170) and thm:loss-d (1434–1440) now define d_NM through what the three
proofs fix, not through a result stated at the computational point.

That definition stands without the parenthesis:
- The proof of [[lem:iii-k-2-3]] fixes its d under *The constants*. It must be at least d_R, d′_0, d_BG and m + 5, as the
  proof of prop:uc-d-small (a) records.
- The other two fix theirs from d_Φ and [[lem:ii-g-4-1]]. This is the wording of lem:uc-phi-loss (2240–2242): "as their
  proofs fix them from d_Φ".

The rest of each sentence ("at least the loss of its estimate … and the orders at which its proof asks U small") is
general. It agrees with:
- the opening of sec:cs-small (4338–4340);
- the proof of thm:loss-d at 1474 ("d_NM, the largest of the d's of the three results");
- prop:ec-delta-cap, which in the general proof of [[thm:settling]] now names d_R from [[lem:uc-dr]], a general
  definition (sec:uc-close).

**At the point.** prop:uc-d-small (a) computes exactly the d's that those proofs fix: max(d_R, d_* + d_F + d_Φ) for
[[lem:iii-k-2-3]], and d_Φ + 8 for the other two. "So the proof of [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] with d_NM =
max(…)" is therefore the general d_NM evaluated there.

thm:uc-integer is stated at the computational point. Its proof takes d_NM < D_acc from prop:uc-d-small (d) (2501), and
eq:uc-integer's d_NM ≤ D_NM := D_acc is that same d_NM. The other sites that cite prop:uc-d-small (23, 1467, 1949, 2485,
2534, 4345) each speak at the computational point or of bounding the orders, and each still reads correctly.

The phrase "as their proofs fix them" now occurs twice in consecutive sentences of the 163 paragraph, once for the d's
and once for the losses of the other two estimates. The referents differ and both are right.

### 3. Crosswalk shape

- There is a header `label	source	source_name	note`, then 212 rows for the 212 labels of chapter 71.
- The labels are unique and in the chapter's order.
- Every row has exactly 3 tabs. No field is empty, and none has leading or trailing whitespace.
- The file ends in a newline.

### 4. Contract

| Check | Result |
|---|---|
| Line width, source | PASS. The longest line in all chapters is 121. Changed lines: 71:163–167 are 114, 121, 120, 120, 25; 71:1434–1440 are 98, 117, 115, 108, 110, 115, 30; 71:1501–1502 are 112, 111; 62:581 is 116. |
| Line width, resolved | PASS. Resolved in memory, the paper has 96,454 lines, the longest 121. That is R-M-71-small's 96,452 plus one line from each of the two rewraps. The same changed lines resolve to 106, 105, 114, 110, 25; 90, 103, 96, 107, 94, 99, 30; 104, 101; and 104. |
| Wrapped-line starts | PASS. No changed line, and no continuation line in the changed paragraphs, starts with "+ ", "- ", "* ", "> ", "#", "=" or "\|", in source or resolved. Elsewhere in chapters 62 and 71 the only such lines are deliberate list items and table rows (62:329–333; 71:108–121, 368–384, 1271–1274, 1351–1369, 1985–1997, 2988–3017), all untouched. |
| Backslash | PASS. There is none in any chapter. |
| File, program, code or AI language | PASS. The changed lines contain no file, program, code, script, merge, placement, `.md`/`.py`, `proofs/` or proof-file name, and no AI language. Provenance appears only in the crosswalk, where it belongs. |
| `python3 lint.py --chapters` | `chapters: 62 file(s), 4579 label(s) defined, 0 hit(s)` |
| `python3 assemble.py --check` | `labels 4579, computations cited 0, problems 0` |

## Finding

### n1 (nit). crosswalk/71-explicit-constants.tsv:10, 11, 66 — three notes still quote the replaced wording

**The problem.** After the observation edit, text 1 (71:164) reads "as their proofs fix them ([[prop:uc-d-small]] at the
computational point)". Text 2 (71:1436–1437) reads "that their proofs fix ([[prop:uc-d-small]] at the computational
point)".

The notes of three rows still describe both definitions as "as prop:uc-d-small fixes them":
- row 10, sec:ec-accounted: "the paragraph after def:ec-accounted-loss rewritten: d_NM is … as prop:uc-d-small fixes
  them (text 1)";
- row 11, def:ec-accounted-loss: "the paragraph after it now defines d_NM as … as prop:uc-d-small fixes them (text 1)";
- row 66, thm:loss-d: "d_NM is the largest of the three results' d's (smallness orders included), as prop:uc-d-small
  fixes them".

Row 11 says "now defines", so it misdescribes the current text. In this commit, m1's text change received a note on
prop:ec-delta-cap, and the chapter's other review-driven changes carry notes too (F-DINT-b). The observation's two
changes received none.

**Replacement.** Append the same text to field 4 (note) of rows 10, 11 and 66, keeping fields 1–3 unchanged:

```
; the d's are those their proofs fix, prop:uc-d-small at the computational point
```

Tried on a scratch copy: the result still has 212 rows, 4 fields each, labels in the chapter's order.

## Observations (not counted, no change asked)

**71:167 is a 25-character line inside the paragraph.** The line is "at which its proof asks U", left by the rewrap of text
1, before "small; for …". The contract allows it, and the chapters already hold about 270 short lines inside paragraphs.
For a tidier source, replace lines 167–170 by these four lines (118, 120, 112 and 17 characters; the word sequence is
unchanged, and no line starts with a forbidden prefix):

```
at which its proof asks U small; for [[lem:iii-k-2-3]] these include the order d′_0 ≥ d_* + D + d_Φ of its proof, with
d_* of [[lem:iii-j2-2-3]], D the d of [[thm:iii-j2-4-1]] and d_Φ the loss of U ↦ Φ(U). As (iii) of [[thm:ii-g-2-1]] asks
[[eq:ii-g-2-4]] of the right inverse of [[lem:iii-k-2-3]], whose loss is that of [[eq:iii-j2-4-2]], d_NM ≥ d_acc
([[thm:loss-d]]).
```

**n2's notes on the equation rows.** These notes still begin "display: …", and their source_name now ends in
"display". This is redundant but harmless; R-M-71-small asked for the notes to be kept.
