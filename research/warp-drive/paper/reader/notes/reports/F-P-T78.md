# F-P-T78: fix round for proofs/P-T78.md

The file is `research/warp-drive/paper/reader/proofs/P-T78.md`, 673 lines, md5
**78bfabb87c33125cbc0d627317535495** (it was b2bff29e…). No chapter or crosswalk was edited and nothing was committed.
The scratch builder, the merge script and the merge copy are in
`/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/pt78/`.

## Findings applied

| # | Change |
|---|---|
| 1 | Overview, last sentence: the reader's text ("In [[ch:s15]], [[lem:tf-lin-reduction]] … with e_Υ > 0"), reflowed. |
| 2 | Overview, first sentence: the reader's text, adding γ_Υ > 0, 0 ≤ e_Υ < 1 and 4e_Υγ_Υ² ≤ ½. |
| 3 | Item 8 is a complete replacement of the current rem:ec-point-outside, using the reader's 21-line combined text. One correction: the remark sits at chapter 71 lines **52–68**, not 49–68. Lines 49–50 belong to def:ec-point. The old text is lines 52–68 exactly. A note after the item says what this version changes against the current text (i: one clause deleted; ii: one sentence added; iii: the γ_(Υ,H) sentence recast), so that P-T49 or P-ADM can be re-based on it. The reader's crosswalk note is added to the "Notes for existing rows". |
| 4 | New item 9: rem:ec-lb-conditions, chapter 71 lines 1779–1780. The second line uses the reader's replacement ("bounds of rows u3 and u4 on e_Υ and γ_Υ"). Its crosswalk note is added. |
| 5 | Line numbers: rem:ec-not-evaluated is at 4961–4963 (item 10), and sec:scope-constants at 83–84 (item 11). |
| 6 | Row u4 ends "Threshold: ε_1 on u2; ½s_C on c1–c2." |
| 7 | Notation, see below. |
| 8 | Proof of lem:iii-d-7-1: the reader's three lines, so (a) at γ_Υ = 0 is stated. Item 2's note on unchanged lines still holds. |
| 9 | New item 12 drops "or by (0, γ_Υ)" at chapter 34 line 561. New item 13 changes chapter 35 line 54 to "γ_Υ is as in [[prop:iii-f1-3-3]]." Item 14 ("Unchanged") no longer lists chapter 35, and it records that the γ_1 in the proof of prop:iii-d1-4-1 is a local constant. |

The items are renumbered 1–14. The crosswalk "text N" references follow the new numbering.

**Notation (finding 7):**
- Line 87 now reads "written in x".
- Δ is renamed Δ_e, as in prop:np-10-20.
- The Notation paragraph says that r := |x| = r̂, and that from there on x̂ denotes the direction.
- The S̄ sentence names the endomorphism and the threshold separately.
- In lem:tf-lin-reduction, N_1 and N_2 are renamed N_ω and N_h.
- r̂ is kept in the overview, which comes before the Notation paragraph and uses the tf variable, and in the sc-b weight
  statements, where r = r̂ is stated. rem:tf-sign uses r.

## Checks

- **Old texts.** All ten were re-copied from the current chapters: items 2, 5, 6, 7, 8, 9, 10, 11, 12 and 13. Each
  occurs exactly once, both in its own file and in all chapters together.
- **Scratch merge.** The merge applies every item to a copy of `chapters/`, including the two insertions:
  - `lint.py --chapters`: 0 hits;
  - `assemble.py --check`: 0 problems;
  - after real label resolution of the whole merged paper, no line exceeds 121 characters.
- **Thresholds.** In the merged chapters, ε_L no longer occurs. γ_1 occurs only as the local constant in chapter 32.
- **P-T78 itself.** It lints with only the expected hits: file paths in the crosswalk rows, labels defined in both an
  old and a new text, and references that are undefined in the isolated file. Lines are ≤ 121 characters, there are no
  wrapped-line markers, and labels are lowercase.
- **Mathematics.** No change to the mathematics.
