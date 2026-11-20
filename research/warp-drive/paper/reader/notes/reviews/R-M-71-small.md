# R-M-71-small: confirming reading of the merge of P-U71-small into chapter 71, and of rem:half-class-changes

## Scope

**Tree read.** HEAD 44b114b5, which is the merge. Its parent is 4c08cac1.

**Sources compared.**
- The merged source: `git show 44b114b5~1:…/proofs/P-U71-small.md`, 438 lines, md5 2e4c1bcc85f09ad5bfe3837eab493cd7. This
  equals the file at 4c08cac1.
- Chapter 71 before the merge: `git show 44b114b5~1:…/chapters/71-explicit-constants.md`, 4390 lines.
- Chapter 71 at HEAD: 4705 lines.
- The crosswalk before the merge and at HEAD.
- Chapter 62 as reworded in bf5a96c4.

**Edits.** Nothing in the repository was edited. I tried the proposed replacements below on a copy of `chapters/`,
`crosswalk/`, `assemble.py` and `lint.py` in the scratchpad. This file is the only one written outside the scratchpad.

## Verdict

**CONFIRMED** — Major 0, minor 1, nit 2.

**The merge is exact.** I rebuilt chapter 71 from scratch: the old chapter, with the 20 old texts of the 14 Placement
items replaced by their new texts verbatim, and part one inserted. The rebuild equals HEAD's chapter 71 byte for byte. The
inserted subsection is byte-identical to source lines 1–301. The crosswalk matches the chapter's labels exactly.

**The chapter 62 rewording is true.** It agrees with chapter 63 and with how chapter 71 counts the index sets in d.
Nothing cites the remark for "d is the same".

**The findings.** The one minor is a symbol, d_R, that text 5 uses about 950 lines before it is defined. The two nits
are a crosswalk source format and an optional pointer in chapter 62. None of them touches a number or a proof.

## Checks

| # | Check | Result |
|---|---|---|
| 1a | Chapter 71 lines 4334–4634 equal source lines 1–301 | PASS. `cmp` finds them identical. md5 ab0baea432f7327e814419e20966ea95 with the final newline. Without it the md5 is 7df6965f248e39f518afeae13f581fe6, the merger's figure. |
| 1b | Blank lines and placement | PASS. Line 4333 is blank and line 4635 is blank. Line 4332 is the last line of rem:cs-sharpness, in sec:cs-bound, the last #### of sec:cs. Line 4636 is the heading of sec:ec-linear. The Placement section (source 303–438) is not in any chapter. |
| 2a | Each old text located and replaced in full, verbatim | PASS. My rebuild matches HEAD byte for byte. Each start phrase occurs once. Each range begins and ends at a line boundary. Line counts: text 1 = 5 (the paragraph), 2 = 4, 3 = 2, 4 = 3, 5 = 1, 6 = 3, 7a = 1, 7b = 2, 8b = 1, 8c = 3, 11a = 1, 11b = 1, 11c = 3, 12 = 3, 13 = 2, 14 = 1. These agree with the texts' own counts. |
| 2b | Kept parts of the in-line texts 8a, 9, 10a, 10b | PASS. Each old string occurs once, within a single line, and the rest of its line is unchanged: lines 2231, 2264, 2453 (121 characters) and 2466. |
| 2c | The text 8 end phrase | PASS. "21d_NM + 6 is the regularity of" was at old lines 1464 (proof of thm:loss-d) and 2245. The range starts at 2243, so the first occurrence after it is 2245, which is correct. The 1464 sentence is intact at line 1469. |
| 2d | Joins read continuously | PASS. Each was read with context: lines 18–27, 158–172, 1428–1476, 1494–1504, 1940–1974, 2229–2268, 2446–2536 and 4323–4334. The short lines "and let the Nash–Moser" (1500), "[[eq:iii-j2-4-2]] for it. By" (1473) and "d_FM, d_Ψ ≤ 62N_Λ + 10. ∎" (2466) are ordinary wraps. |
| 2e | No old phrase remains | PASS. I took every 6-word window of each old hunk that is not in its new hunk and searched all chapters for it. Every hit is either inside a new text ("d_acc and d_NM are at most an integer"; "the losses of … [[prop:iii-j2-4-3]], that of", text 8c; "d_NM is the largest of the", text 1) or in an unrelated rule of def:ec-accounted-loss (153, 1479). "d_NM ≥ d_acc ≥ 3R > 1.2497·10²⁴" stands correctly in cor:uc-two-offsets and eq:uc-lower. None of these remains anywhere: "two other components", "d_NM = d_R", "d_NM = max(d_R, d_FM", "so that d_NM equals it", "whose largest is d_NM". |
| 3a | The stale phrasings, in chapters 71, 00, 01, 03, 46 and 90 | PASS. "max(d_R" occurs only as "d_NM ≥ max(d_R, d_FM, d_Ψ)" (2240, 2264), "d_R = max(d_R, …)" (2453) and inside sec:cs-small (4581–4612). "two other components" and "d_NM = d_R" occur nowhere. |
| 3b | Every d_NM sentence against the new definition | PASS. Chapter 71 has 43 lines with d_NM. The untouched ones are 390, 396, 1469–1492, 2080–2091 and 2487. Elsewhere: 00:34, 01:151–154, 03:351–354, 46:1251 and 1550, 90:58–72. Each speaks of "the loss d with which the Nash–Moser theorem is applied", which is the d of thm:iii-k-3-2 (46:1550, the largest of the three d's), or gives lower bounds through d_NM ≥ d_acc. All hold for the new d_NM by prop:uc-d-small (d). One readability issue: **m1**. |
| 3c | thm:uc-integer covers the new d_NM | PASS. eq:uc-integer reads "d_acc ≤ d_R ≤ D_acc, d_NM ≤ D_NM := D_acc". The finer bounds cite lem:cs-sharp and prop:uc-d-small. The proof takes d_NM < D_acc from prop:uc-d-small (d), which covers both readings of the fixed seminorms. The citation is a forward one but not circular: prop:uc-d-small uses only the defined constants D_e, C_* and D_acc, and the lower bounds. |
| 4a | Crosswalk shape | PASS. There is a header and 212 rows for 212 labels, all unique, in the chapter's order, with 4 fields each. No field is empty and none has stray whitespace. |
| 4b | The 9 new rows and 13 amended notes | PASS on content. The new rows sit between rem:cs-sharpness and sec:ec-linear, in order of definition. Their notes agree with the text. All 13 amendments are pure appends ("; P-U71-small: … (text n)"), and no source or source_name field changed. The source format differs from the file's convention: **n2**. |
| 5a | rem:half-class-changes is true where it stands | PASS. At this point the logarithmic orders of ℰ^C_I at the half-integers are not determined. They enter l_*, which by def:iii-i10-1-1 bounds the logarithmic orders of ℰ^C_I, and so they enter k̄(λ) = k̄_0 + (J_* + 1)(l_* + 1)(n(λ) + 1). Through k̄(λ) they enter the counts in d (thm:loss-d (iii)). So "d … may change" is right. d_1 = max(d_0, N_NM + k″) (46:1603) moves with d, and ε_n, λ1 and δ with them. |
| 5b | Consistency with chapter 63, def:iii-i10-1-1 and chapter 71's counts | PASS. prop:own-same-index-sets gives the same ℰ_I^C, logarithmic orders included, so the orders do not rise, as the remark says. rem:own-half-changes (b) has d_1 and ε change through the extra factors of R, which "may change" covers. Chapter 71 counts pairs (λ, k) with k ≤ k̄(λ): lem:uc-n-iota (2391–2414), lem:uc-fourier-count (2215, 2225) and rem:cs-sharpness (4323–4332). That is "through k̄(λ)" exactly. The construction of thm:iii-c1-3-1 is not in chapter 71's inventory, so the change in d_1 does not reach d. An optional pointer: **n1**. |
| 5c | Is the remark cited for "d is the same"? | No. Its only citation is 63:194, "settles the question left open in [[rem:half-class-changes]]", which matches the new text. No other chapter says d is the same in the half-integer class. Crosswalk row 62:21 is unchanged, which is in line with the other coordinator edits (a3877611). |
| 6a | Line widths | PASS. The longest line of chapter 71 is 121 characters, and of chapter 62 also 121 (line 577). The assembled paper has 96,452 lines, the longest 121. |
| 6b | Wrapped-line starts, backslashes, language | PASS. No changed line, and no line of rem:half-class-changes, starts with "+ ", "- ", "* ", "> ", "#", "=" or "\|", except the #### heading of sec:cs-small. There are no backslashes. There is no file, program, code or AI language: "P-U71", "proofs/", "merge", "placement", "script" and "file" do not occur in the changed text. |
| 6c | `python3 lint.py --chapters` | `chapters: 62 file(s), 4579 label(s) defined, 0 hit(s)` |
| 6d | `python3 assemble.py --check` | `labels 4579, computations cited 0, problems 0` |
| 6e | number/resolve/lint snippet | `[] 0` |
| 6f | The proposed fixes, tried in the scratch copy | m1 and n1 applied: lint 0 hits, assemble 0 problems, snippet `[] 0`. The new lines are 112, 111 and 116 characters, shorter after resolution. |

## Findings

### m1 (minor). chapters/71-explicit-constants.md:1499–1500 — d_R is used before it is defined

**The problem.** Text 5 puts "d ≥ d_R ≥ d_acc" into the statement of prop:ec-delta-cap. That is now the first occurrence
of d_R in the chapter. It is defined only in lem:uc-dr (2451–2453), about 950 lines later. Before the merge, d_R first
appeared in lem:uc-phi-loss (now 2240), which names it in place: "with d_R ≥ d_acc the accounted loss of
[[lem:iii-k-2-3]]".

The inequality is true (R2 checked it), and the proof of prop:ec-delta-cap uses only d ≥ d_acc. The problem is only that
a reader meets a symbol with no definition.

**Replacement.** Replace lines 1499–1500:

```
d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] (d ≥ d_R ≥ d_acc, [[thm:loss-d]], [[prop:uc-d-small]]),
and let the Nash–Moser
```

by:

```
d_NM with which [[thm:iii-k-3-2]] applies [[thm:ii-g-2-1]] (d ≥ d_R ≥ d_acc, d_R the accounted loss of the right
inverse ℛ(U) of [[lem:iii-k-2-3]] ([[lem:uc-dr]]); [[thm:loss-d]], [[prop:uc-d-small]]), and let the Nash–Moser
```

Line 1501, "threshold be ε_NM = θ_0^(−(8d+2)), …", follows unchanged. ℛ(U) is named in the proof of thm:loss-d
(1471) as that of lem:iii-k-2-3, and "accounted loss" is the wording of lem:uc-phi-loss and lem:uc-dr.

If this is applied, append to the note of crosswalk row prop:ec-delta-cap: "; d_R named at its first use".

### n1 (nit). chapters/62-interior.md:581 — optional pointer to what chapter 63 says changes

**The problem.** "So d, ε_n and d_1, and with them λ1 and δ, may change; [[sec:own-half-class]] shows that the logarithmic
orders do not rise." This is true. But the "So" follows the sentence on the logarithmic orders, and the remark then says
only that the orders do not rise. A reader may conclude that nothing changes. In fact rem:own-half-changes (b) has d_1,
and ε with it, change through the extra exponents of ℰ_0^½, whatever the logarithmic orders do. The first sentence of the
remark already lists ε_n and d_1 as separate entry points, so this is optional.

**Replacement.** Replace line 581:

```
logarithmic orders do not rise.
```

by:

```
logarithmic orders do not rise, and [[rem:own-half-changes]] that d_1 and ε_n change through the exponents of ℰ_0^½.
```

### n2 (nit). crosswalk/71-explicit-constants.tsv:199–207 — the source format of the 9 new rows

**The problem.** Every other proof-sourced row in this file and in the other crosswalks gives `paper/reader/proofs/<file>`
with a line, and the d-bound family adds a commit (`…@d1509feb:<line>`). The neighbouring rows 195–198 are an example.
The new rows give `proofs/P-U71-small.md (merged)`, with no line and no commit, for a file that no longer exists at HEAD.
Their source_name also departs from the family's "d-bound proof <part>, …".

**Replacement.** Replace fields 2 and 3 of rows 199–207 as below, and keep the notes. Commit 4c08cac1 holds the merged
source, md5 2e4c1bcc…; the line numbers are its label lines.

| Row | label | source | source_name |
|---|---|---|---|
| 199 | sec:cs-small | paper/reader/proofs/P-U71-small.md@4c08cac1:1 | d-bound proof small, subsection: The smallness orders and the loss of the Nash–Moser step |
| 200 | lem:cs-sharp | paper/reader/proofs/P-U71-small.md@4c08cac1:29 | d-bound proof small, Lemma (The single-step losses summed level by level.) |
| 201 | eq:cs-sharp | paper/reader/proofs/P-U71-small.md@4c08cac1:33 | d-bound proof small, display |
| 202 | lem:uc-small-orders | paper/reader/proofs/P-U71-small.md@4c08cac1:69 | d-bound proof small, Lemma (The orders of the smallness conditions.) |
| 203 | eq:uc-small | paper/reader/proofs/P-U71-small.md@4c08cac1:92 | d-bound proof small, display |
| 204 | eq:uc-small-diff | paper/reader/proofs/P-U71-small.md@4c08cac1:101 | d-bound proof small, display |
| 205 | rem:uc-small-reading | paper/reader/proofs/P-U71-small.md@4c08cac1:221 | d-bound proof small, Remark (Fixed seminorms that also bound the remainders.) |
| 206 | prop:uc-d-small | paper/reader/proofs/P-U71-small.md@4c08cac1:241 | d-bound proof small, Proposition (The loss with which the Nash–Moser theorem is applied.) |
| 207 | eq:uc-d-small | paper/reader/proofs/P-U71-small.md@4c08cac1:251 | d-bound proof small, display |

## Observations (not counted, no change asked)

- **Texts 1 and 2 define d_NM through a result stated at the computational point.** The paragraph after
  def:ec-accounted-loss (164) and thm:loss-d (1435–1436) are general, and they define d_NM as the d's "as
  [[prop:uc-d-small]] fixes them" and "that [[prop:uc-d-small]] fixes". prop:uc-d-small is stated at the computational
  point. The rest of each sentence carries the general meaning: each d is at least the loss of its estimate and the
  orders at which its proof asks U small, and 46:1550 agrees. Both earlier readings accepted these texts, so I leave them.
  If the coordinator wants them strictly general, "as their proofs fix them ([[prop:uc-d-small]] at the computational
  point)" would do it, with a reflow of both paragraphs.
- **Report M-71-small.** Its "Files touched" says "14 rows amended", but its own list, and the crosswalk, have 13.
  Its md5 7df6965f… for the part is the md5 without the final newline; with it, the md5 is ab0baea4…. Both sides agree in
  either form.
