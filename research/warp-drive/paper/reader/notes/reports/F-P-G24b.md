# F-P-G24b: fix round on proofs/P-G24b.md

**File:** `paper/reader/proofs/P-G24b.md`, md5 **a44f9f97a98e435754cf15153bedef33**, 1,645 lines. Not committed.
No chapter or crosswalk was edited.

**Base:** chapter 33 at HEAD (3b715dd5). The chapter last changed at the P-ADM merge (54350a5d), md5
147ca1624e75c280f86908a0aa499824.

- The round started on the P-T49 version of the chapter (9571426c…). The P-ADM merge then changed lines 126, 3130,
  3532–3534, 3582 and 3866–3872.
- None of those lines is a site of T1–T45. All 45 old texts still occur exactly once.
- The citation table was renumbered from a line map: +2 from line 127, and +4 after the old line 3534. The [Hin26, (8.13)]
  row (class b) is now line 3584.
- Citation counts are unchanged: 248 in all ([Hin26a] 208, [Hin26] 29, [Hin26c] 4, [Hin26d] 3, [Hin23d] 2, [Shu92] 1,
  [Mel93] 1).

## Review items (notes/reviews/R-P-G24b.md)

- **m1.** "Positive" is added to T4's cut-off definition. T8 takes it up in its note.
- **m2.** The strong-sense claims of eq:iv6-1-3 and eq:iv6-1-4 are in.
- **m3.** The reader's replacements for T33 and T35 are used, and so is the new text at the old line ~2494. That text is
  T44: it adds the hypothesis that 𝔛 = δ_r⁻¹ is as large as the cone-face symbols need.
- **m4.** §3.2 is now the reader's checked counterexample, in five steps.
- **n1–n12.** All twelve are applied in the reader's words, with one deviation. The n7 line, as the reader wrote it,
  resolves to 122 characters ("Definition 24.27"). It is rewrapped before "near K⁺", and the wording is unchanged.
- **T45.** It is a new text for prop:iv5-7-1.
- **M1.** The relative-index step is unchanged and still open. The marker stays in §6.1, which points to proofs/P-RI.md.

## Crosswalk

The 16 new rows carry `paper/reader/proofs/P-G24b.md@PENDING:N`, where N is the line of the proof file that holds the
label. Every N was checked against the file.

## P-G1 (§8, rewritten for nit F3 of R-P-G1)

§8 now describes P-G1 as it stands: md5 b2d824fb…, which merges first.

- **C33-11 and T41.** Variant A of T41 applies. Its old text is the last two lines of the new C33-11, and it occurs
  there once. The fallback, if T41 were merged first instead, quotes C33-11's current last paragraph.
- **C33-12 and T7.** They share "[[lem:iv5-0-5]] (6) on supp ψ′.", and C33-12 is the whole of line 1536. Either order
  works. The merged line is 106 characters, measured.
- **C33-20 and T34.** As before: C33-20's paragraph goes before T34's new text.
- **Adjacent texts.** T42 and C33-9 are adjacent, and so are T5 and C33-10. The line numbers are given at HEAD. §8 notes
  that P-G1's line numbers are 2 lower than these.
- **Simulation.** I applied P-G1's 20 chapter-33 sites to the chapter at HEAD, then T1–T45 with variant A.
  - All 45 old texts occur exactly once, and no two overlap.
  - C33-20 lands immediately before T34's new text.
  - No line is over 121 characters, and there is no backslash.
  - This agrees with the P-G1 reader's own merge.

## Scratch merge

The scratch copy is `scratchpad/pg24b/`, re-copied from the working tree at HEAD.

| check | before | after |
|---|---|---|
| `lint.py --chapters` | 4652 labels, 0 hits | 4668 labels, 0 hits |
| `assemble.py --check` | 0 problems | 0 problems |
| `lint.py --paper` | — | 0 hits |
| PAPER.md maximum line length | — | 121 |

- **Conservative test.** Every new label was resolved as "Proposition 49.999" and every old label to its actual number.
  Chapter 33's maximum line is then 121.
- **Crosswalk 33.** 216 rows for 216 labels, in chapter order. The 200 old rows keep their order.
- **Reproduction.** Applying the 45 blocks of the proof file to the chapter at HEAD reproduces the checked scratch chapter
  exactly.
- **Withdrawn claim.** The withdrawn "G2 finding" appears nowhere.
