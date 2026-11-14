# XW-1: crosswalk sweep

## Counting rule

Every `{#kind:key}` in the chapter file is one row, of every kind (part, ch, sec, app, eq, def, lem, prop, thm, cor,
rem), in file order. The 42 crosswalks that already matched carry rows for part:, ch:, sec: and eq: labels, and 95 had
one for app:. Rows that are not labels ("(proof)", "(abstract)", "(recalled, unlabelled here)") do not count.

## Changes (existing rows' text unchanged)

- 00: removed "(abstract)". The chapter has no labels, so only the header is left.
- 04: removed "eq:waves (recalled, unlabelled here)".
- 06: +4 sec rows (ue-theorem, ue-linearisation, ue-decomposition, ue-every-order); sec:ue-bootstrap moved before
  eq:ue-energy.
- 07: +4 sec rows (data-theorem, -identities, -approximant, -evolution); rem:data-rates moved before sec:data-proof.
- 08: removed the three "prop:… (proof)" rows (those props are labelled in 03); rem:boundary-first-order and
  eq:theta-two-scale reordered.
- 09: removed "thm:past-construction (proof)".
- 10, 30, 39, 45, 64: reordered only.
- 27: +eq:ii-f-lp-prime.
- 33: +16 (eq:s14-lh, rem:s14-u6, eq:s14-s-ang, eq:s14-s-rad, rem:s14-e0, rem:s14-r0, eq:s14-theta-in, eq:iv5-fib,
  eq:iv5-fib-adj, rem:s14-other-routes, rem:s14-counting, rem:s14-polyhom, rem:s14-dim3, eq:s14-theta,
  rem:s14-delta50, rem:s14-eps-point). Removed eq:iv4-0-2: the same display is now keyed eq:s14-lh, and no chapter
  cites the old key.
- 40: +def:s21-eps-g; eq:s21-rows-at-b reordered.
- 62: +lem:interior-chart.
- 95: +42 rows (every std- entry, section and display from the Appendix A rounds); thm:std-bgp-development reordered.
- Format: 176 rows that had three columns got an empty fourth (note) column, in 04, 05, 48, 62, 63, 64, 65, 80,
  84 and 95.

The removed rows are kept in commit 55b7401 and in
/tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/xw1/removed-rows.tsv.
The 00 abstract row and the four proof rows held provenance that may want a new home.

## Sources

**Source not located** (best site given):
- thm:std-bgp-riesz: GAUGEDECAY5.md:3322-3327. The record reads neither [BGP] §1.2 nor [Rie49].
- thm:std-bh17-embedding: P:2093-2094 and NP:7231-7256. The record reads only [BH17] 7.21, 7.26 and 9.14.

**Written in the edition, with no display in the record** (the record site they rest on is given):
- eq:std-slab, cor:std-moser-product, thm:std-gn-moser, eq:std-gn-moser, cor:std-zero-sobolev;
- eq:s14-s-ang, eq:s14-s-rad, eq:s14-theta, def:s21-eps-g, lem:interior-chart.

**Literature the record does not read:**
- [BW15] (thm:std-hormander-cauchy) and [Usu26] (thm:std-mazzeo-melrose);
- [DS23] Thm 2.5 (thm:std-ds-stability);
- [Tre19] (thm:std-chebyshev, sourced to proof D1).

Proof A is unmerged, so rem:s14-delta50 and rem:s14-eps-point also cite paper/reader/proofs/P-A-indicial.md.

## Chapters 82, 83 and 03 (not touched)

- 82: matches, 81 rows.
- 83: matches, 177 rows.
- 03: one row is missing, rem:envelope-regularity (chapter line 49). It belongs between thm:main and
  prop:boundary-spacelike. Nothing else differs.

## P-C-lambda0: retired (`git rm`)

Staged, not committed by me; others' commits took it in (b571483) and the crosswalks in (777e1e6).

- (a) STATUS.md:58 records chapter 86 "written (confirmed proof C carried byte for byte …) … CONFIRMED". STATUS.md:76
  records proof C itself as CONFIRMED.
- (b) All 16 labels of the file are defined in chapters/86-lambda0.md. The chapters hold 49 [[…]] references to them
  (in 03, 84, 85, 86 and 87), and all of them resolve. No label from its one earlier version (1dfd704) is missing,
  and no chapter names the file.
- Note: crosswalk/86 cites the file in 16 source cells. This follows the precedent of crosswalk/83, which cites the
  deleted P-K83a/b/c.

## Other proof files (by labels)

- **Merged:** P-B-morawetz, P-B2-band, P-D1-cone, P-D234-residuals, P-E-background, P-E-margins, P-F-edge,
  P-H-l24, T-B2, T-D1, T-D234, T-E-background, T-E-margins.
- **Not merged:**
  - P-A-indicial: 2 of 26 labels in chapters (prop:gap-sums and rem:gap-sums, in 71).
  - P-A3-every-h: 0 of 15.
  - P-K82: 2 of 15.
  - P-U71-IS: 0 of 32.
  - P-U71-SP: 0 of 26.
  - P-U71-assembly: 3 of 20.
  - P-U71-close: 0 of 20.
  - P-U71-forward: 0 of 35.
  - T-A: 0 of 7.
  - T-B: 6 of 7; sec:tb-morawetz-mM is missing.

## Other observations

- 98-references has no labels and no crosswalk. I did not create one.
- Unresolved references outside proof A/A3: app:tables (33) and ch:scope (01, 03).
- The undefined s14 keys are cor:s14-eps-ind-point, lem:s14-delta50, prop:s14-scalar-every-h and rem:s14-eps-ind-scope.

## Final check

A script compares each chapter's labels with its crosswalk's label column. All 57 crosswalks I own now match
exactly, in order, with no missing, extra or duplicate rows. Every row has four columns.
82 and 83 match too; 03 differs only as stated above. No chapter file was changed.
