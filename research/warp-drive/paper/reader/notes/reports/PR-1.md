# PR-1: unused entries removed from Appendix A and the bibliography

Edited: chapters/95-standard-results.md (−63 lines), chapters/98-references.md (−77), crosswalk/95-standard-results.tsv
(−6 rows). The diff only deletes lines.

## Appendix A: the 14 entries with no outside label reference

Tests: (1) a [[label]] reference to the entry or an equation in it from another chapter; (2) a reference from a
used Appendix A entry; (3) a literature citation of the result it states in another chapter.

| Entry | Verdict | Evidence |
|---|---|---|
| thm:std-bgp-riesz | removed | none ([BGP] is cited elsewhere, but never Def. 1.2.1, Lemma 1.2.2 or Prop. 1.2.4; [Rie49] is cited nowhere) |
| thm:std-cbcm-reduced | kept | 02-setting.md:293 "([CBCM10] (2.7)–(2.9), p. 8)" quotes the result |
| thm:std-cbcl-harmonicity | removed | none ([CBCL06] occurs only in this entry) |
| thm:std-lr-propagation | removed | none ([LR05] occurs only in this entry) |
| thm:std-hin26a-cform | kept | 33-s14-constraint-damping.md:554, 1096, 1100, 1310, 1313 [Hin26a, Proposition 5.1] |
| rem:std-racz | removed | none: (3.3) and (4.7) are never cited. The bare [Rac16] at 07-data.md:196 and 83-localised-data.md:10 is for notation and the hyperbolic split, which kept entries cover |
| thm:std-wu-characteristic | removed | none ([Wu26] occurs only in this entry) |
| thm:std-bh-extension | removed | none ([BH17] is cited only for Theorems 7.26, 7.27 and the chart comparison, never 7.21) |
| thm:std-moser-taylor | kept | its eq:std-moser is referenced at 81-class-system.md:387, 388, 516 |
| thm:std-hjs-calculus | kept | 20-s01-spectral-bounded.md:193 [HJS, (2.1), p. 9], and :198–227 |
| thm:std-zero-calculus | kept | 27-s08-iota-normal.md:23 [Hin23e, Theorem 3.4]. Also :1312 (Def. 1.2), :1400 (Cor. 3.3) and :1404 (Cor. 3.6) |
| thm:std-relative-index | kept | 33-s14-constraint-damping.md:2114 [Mel93, Theorem 6.5] |
| thm:std-dlmf-modified | kept | 27-s08-iota-normal.md:1343 [DLMF, (10.25.1)]. Also :1345 (10.28.2), :1347 (10.40.1)–(10.40.2) and :1348 (10.30.2) |
| thm:std-chebyshev | kept | 87-ten-l5.md:359 [Tre19, (15.2)–(15.4), p. 108], :362 Theorem 15.2, :363 Theorem 8.2 |

No entry references any of the six removed ones. Each of the other 48 entries has an outside label reference.

No section is removed: every section that lost an entry still has others. No sentence of the appendix text refers
to a removed entry. The [BH17] convention sentence still applies to the three [BH17] entries that remain.
**Sentences changed: none.**

## Bibliography: 41 entries removed

Order of the rest is kept. Before Appendix A was cut, 37 entries were already unused:
0C (alias), An12, CB69, CBF06, CCRT07, Chr11, CTWG23 (alias), DHRT21, Hin16, Hin22a, Hin25c, HL17 (alias), HL18e,
Hua15, Hun15, HV26, HW13, KI03b, KK25, KS17, Li25, LR17, LX24, Mel94, Min19, MM10, Mos17, MP11, Olv97, RT12,
SBG (alias), Sbi13 (alias), Sch13, Tat13, Tay11, Vas21b, Zwo12.

Removing the entries made 4 more unused: **CBCL06, LR05, Rie49, Wu26**.

Re-running the test finds 0 of 90 unused, so it has stopped. No removed key occurs anywhere outside chapter 98 in
any form, including inside multi-key brackets. Exact-key matching keeps Tay11a. The alias targets Hin23e, CTG23,
Sbi15 and Hin26d are cited directly.

## Crosswalk

The six removed labels' rows are deleted. The crosswalk now matches the chapter's label sequence exactly (62 = 62).

## Checks

- `python3 lint.py --chapters`: 62 files, 4567 labels, **0 hits**.
- `python3 assemble.py --check`: 4567 labels, **0 problems**.
- Longest lines: 121 characters (chapter 95) and 120 (chapter 98). Chapter 46 not touched.

Diff: /tmp/claude-0/-home-user-Claude-Method-Works/36602a96-aefb-52fa-89f4-29a4ab038dc7/scratchpad/reader/scratch/pr1/pr1.diff
