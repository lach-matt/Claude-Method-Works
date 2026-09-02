# READ-ch16j — chat 119 — main L8700–L8789 (§31.3 – §31.3.4), chapter 31 closed

Unit cut by own heading scan: §31.3 L8700, §31.3.1 L8702, §31.3.2 L8714, §31.3.3 L8720,
§31.3.4 L8728, chapter 32 head L8790 — so chapter 31 ends at L8789. 90 lines, the
movement-closing cut. Instruments: `r2-ch16h` (computable, golden 6063a7c1), `r2-ch16i`
(prose, golden aa1177df). Prints & Proofs offset over the whole unit is a uniform **−88**,
measured on eight independent anchors.

## A — Deviations

**16j-01 — an ordinal count contradicted by the book's own restatement of the same set.**
L8783 prints *The 24 excluded values — 102, 103, 115, 117 and the run 119–126*. The sentence
names **twelve** values. Twenty-four is the count of excluded **cells** (2 per value, and
232 − 208 = 24 confirms it). The main volume gets it right elsewhere: **L11070 prints
"208 cells from 13 ≤ h ≤ 128 less twelve exclusions"** for the same slice. One volume, two
sites, one set of exclusions, two counts. Repair: *twelve* at L8783, or *24 excluded cells*.
Docket 21, and docket 14's shape internalised to a single volume.

**16j-02 — a criterion cited and then departed from, with its conclusion kept.**
L8716–L8717: *By §16.7.1's test the absence is removable — not by re-coordinatising but by
re-constructing — so it is a defect of the index.* §16.7.1 read in full (L4578–L4617): the
printed discriminator is re-coordinatisation. L4593 *Order the blocks f, d, p, s and define
the period by n + ℓ, and the defect vanishes. So the 36 belong to the drawing.* L4614–L4615
*A defect of the index vanishes under some re-coordinatisation. A feature of the world
survives every one.* Under the test as printed, an absence that survives every
re-coordinatisation is a feature of the world — the opposite of the conclusion drawn.
Either §31.3.2's inference or §16.7.1's criterion has to give. Docket 12 (a consequence
asserted of hypotheses that do not entail it), docket 9(b).

**16j-03 — a pointer whose target carries no part of the claim.**
L8785: *…moves the set toward its own normal form, which is what §10 says a void should do
when it is structural rather than accidental.* §10 swept in full over its whole span
L2021–L2074, all four subsections: **zero sites** for *structural*, **zero** for
*accidental*, **zero** for *normal form*. §10 defines the void (L2024), attributes it to
Pauli and the hydrogenic bound (L2027), sizes it at 27.7–30.1 % (L2033) and factorises its
count (L2061–L2071). It makes no structural/accidental distinction and states no normal-form
behaviour. Not a token probe: the whole span was read. Docket 9(b).

**16j-04 — one work, two irreconcilable author lists.**
Text L8732: *Candelas, de la Ossa, He & Szendroi (Triadophilia, ATMP 12 (2008) 429)*.
Bibliography L11804: ***Candelas, P., de la Ossa, X. & Rodriguez-Villegas, F.** (2007).
*Triadophilia* (arXiv:0706.3134).* He and Szendroi appear only in the text;
Rodriguez-Villegas only in the bibliography. The 2008/2007 split is defensible (journal
against preprint); the author lists are not — one entry is for a different paper. This is
also why the attribution sweep scored **Szendroi** unbibliographed. Docket 16, docket 36.

**16j-05 — an unanchored ordinal.**
L8755: *24.3.4.2 The fourth falsification test, run.* Every *falsification test* site in the
main volume: L5198, L8755, L9205, L9226, L9360, L10280, L11072. §32.6 L9207 prints *The
three conditions are tested here*; L10280 prints *the three falsification tests of §32.6*;
L11072 and register 387 both print *all three falsification tests hold at 540 of 540*, of
the three rows inside this very section. No printed enumeration contains a fourth. Two
readings survive and neither is printed: fourth after §32.6's three (a forward reference,
and to tests of a different object — the book, not the catalogue), or the test belonging to
lettered item D, the fourth item. Recorded with both readings rather than asserted false.
Docket 21, docket 33.

**16j-06 — stale sub-numbering, three sites, and it is authoring.**
L8738, L8755, L8777 print **24.3.4.1, 24.3.4.2, 24.3.4.3** inside §31.3.4. `heading_line`
resolves **24.3.4 to None** — no such section exists; §24.3 is at L6668. `enclosing` puts
all three in §31.3.4. They are **not markdown headings** (no `#`), so they carry none of the
document structure their siblings carry. MEASURED: these are the **only three lines in the
main volume** whose N.N.N.N number disagrees with its own enclosing chapter, and the only
24.3.4.x sites in six volumes. Present in Prints & Proofs at P8650 — **authoring, not
production**, settled without escalation. Repair: 31.3.4.1–3, as `####` headings.
Docket 31, docket 28, docket 32.

**16j-07 — Ruling 45, three sites in ninety lines.**
L8729 *a gzipped file this session could not read*; L8757 *The file is missing*; L8788 *What
remains of item D is the lookup. 540 named cells, a file, and an afternoon.* The same
register recurs at L11076 (*a gzipped catalogue this session could not reach*). Docket 5.

**16j-08 — an attribution with no bibliography entry.**
**Klemm** (L8715, *Klemm–Kreuzer toric CICYs*), one main-volume site, absent from
`## References` at its BODY occurrence L11503 and from R.7 L11806, and absent from the other
five volumes. Kreuzer and Skarke both resolve at L11797. Docket 36.

## B — Verified findings

The mathematics of this unit reproduces essentially exactly.

- **Inclusion–exclusion, L8707–L8708.** 248,305 + 248,305 − 495,515 = **1,095**. EXACT. The
  equality of the two counts is itself a check on the mirror symmetry claimed at L8704, and
  it holds.
- **The Pareto arithmetic, L8721–L8723.** 1,095/495,515 = **0.221 %** (3 dp, ROUND_HALF_EVEN);
  1,095/473,800,776 = **0.0002 %** (4 dp); the factor **956** EXACT — and correctly computed
  on the unrounded values, since the printed rounded pair would give 1,105. The convention is
  right and is recorded as a docket-34 **pass**, not a charge.
- **The slice as a cell set, L8732–L8734.** 13…128 less the twelve named exclusions gives 104
  values and **208 cells**; without exclusions **232**; C(208,2) = **21,528** unordered
  (ordered would be 43,056 — the printed figure names the unordered convention).
- **E(X) = 540, L8736.** EXACT under closure to a **fixed point**. The one-step closure over
  pairs of X alone gives 534; the second round adds the 6 cells the gaps in H put out of
  one-step reach. The **498 join and 498 meet failures are EXACT one-step counts** over the
  21,528 pairs. The printed line therefore carries two conventions and prints neither — see C.
- **589 and 49.** The unexcluded 232-cell set closes at **589** (there one step and the fixed
  point coincide, which is precisely why the gapped set separates them), and 589 − 540 = **49**.
- **The predictions table, L8746–L8750.** 540 cells; **5** distinct χ values, exactly
  {0, ±2, ±4}; **112** on the diagonal, first (13,13), last (131,131); h¹¹ + h²¹ from **26 to
  262**. Every row EXACT. L8744's *the join of (h, h+3) and (h+3, h) is (h+3, h+3)* holds for
  104 of 104.
- **The falsification rows, L8760–L8768.** 540/540 positive on both indices; 540/540 under the
  published maximum 502; 540/540 mirror partners present; 0/540 in the thin tip; zero
  falsified. Both named cells present: **X₁₉,₁₉** and **X₂₀,₂₀**.
- **§31.3.1's Λ column, L8711–L8712.** |Λ₈| = **976**. *self-dual cells 8 of 976*: the section
  prints no definition, and four candidate involutions were measured — coordinate reversal 0,
  complement fixed points 0, reversal-image-in-Λ 0, and **complement-image-in-Λ = 8**, which
  is exactly the semantics the KS column needs (*all*, because the list is closed under the
  involution). The figure is reproducible and the definition is uniquely determined by the
  table's own other column. *rank polynomial palindromic false*: the rank sequence read out of
  chat 118's banked golden (sum 976, consistent) is not a palindrome. EXACT.
- **L8717–L8718's two comparisons.** *the periodic table's 36* — L4589 and L4606 print 36
  admitted of 36. *the belt's six* — L4605 prints *0 of 6 admitted*, and L4614's polarity is
  the one the sentence uses. Both figures and both polarities correct.
- **§12.8.1's pointer, L8725.** *|A_q| falls as |B_q| rises* — L2424 prints *|A_q| falls 33,
  33, 23, 8 while |B_q| rises 5, 10, 15, 17*. EXACT.
- **Register 387 is exact and on point.** Cited by L11070 for this slice, its headline
  reproduces 208, E(X) = 540, 498 and 498 of 21,528, five χ values, 112 on the diagonal and
  26–262. A negative witness for the register-citation class, recorded so the class is not
  made to look worse than the book is.
- **§30.4.2's charge does not survive contact with its target.** L8604's omission column says
  *§31.3's statistic — stated against the wrong denominator*. §31.3.3 states it against
  495,515, the right denominator, and names 473.8 million only to reject it as *true and
  uninformative*. Chat 118's 16g-04 is now measured at the target: the row is not merely a
  member of the wrong class, its charge is false.
- **Zero Ruling 46 sites. Zero first-person pronouns. Zero duplicated long lines** over 47
  swept — the thirteenth consecutive clean unit for DEF-105 item 1. **Zero census rows** in
  L8700–L8789 across classes `main` and `all`.

## C — Incidentals

1. **Two conventions in one printed line (L8736).** 498 + 498 are one-step failures over the
   pairs of X; 540 is the fixed-point closure. Both exact, neither convention printed. A
   reader recomputing one step would get 534 and think the book wrong. Worth a clause.
2. **The thin-tip row is unfalsifiable by construction (L8765–L8766).** The slice's minimum
   sum is 26, so no closure of it could ever land below 22; *where a prediction would be
   refuted* names an empty possibility. The row is true; it is not a test.
3. **§31.3 has zero body lines** — the only parent section in chapters 30–31 with none
   (§30.4 has 5, §31.1 has 2, §31.2 has 1). Its children carry the content, so this is a
   consistency point, not a gap.
4. **The section that does the work carries no register citation.** Register 387 is cited at
   L11070 in the appendix; §31.3.4 cites nothing.
5. **Reverse-direction bibliography claim.** L11801's Huang & Taylor entry says its counts are
   *used in §31.3.1*; §31.3.1 attributes them to no one, printing only *three published counts*.
6. **The 30,108-pair file.** L11798–L11799 records it as published and unread, with a pointer
   to §32.2 — consistent with L8729 and L8757, and the honest reading is that the class is
   Ruling 45's form rather than a false claim.
