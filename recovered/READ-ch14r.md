# READ-ch14r — chat 99 — main L6623–L6740, §24 through §24.7 (Chapter 24, first of three reads)

Boundaries re-scanned on `The_Method_1_6-2.md` before reading: Chapter 24 opens **L6623**, §25 opens
**L6884**, chapter extent **261 lines, fourteen headings**. Unit **L6623–L6740, 118 lines, eight
headings**, closing before §24.8 at L6741. Instruments: `r2-ch14r` (computable, 232 lines,
`1693fbf1`) and `r2-ch14s` (prose, 126 lines, `692a7ecb`). No corrections made; no Register entry
written; chat-67 hold in force.

**The basis, stated first because every count below depends on it.** The Spectra Compendium's
Section II states its own totals at spectra-member L900: **596 channel rows across 28 elements ·
2,269 interior cells**. `r2-ch14r` reproduces that line exactly, so the parse is the compendium's own
basis. Of those 596 rows, **477 carry three or more levels and 119 are two-member channels** —
477 + 119 = 596. **HANDOFF-51's carried "477 rows" is therefore not stale; it names the ≥3-level
subset.** My first framing of it as stale was an instrument-side error, self-caught and corrected
here: when a carried figure disagrees with a fresh count, the finding is about the count's basis.

---

## A. Deviations

**14r-01 — Chapter 24's headline collection figures agree with the Register and disagree with the
data volume.** L6626 prints *546 of 789 interior cells — 69.2%*, failing on *243 cells across 62
channels*. Measured over every compendium row carrying an `m/k` bracket: **1,577 of 1,738, 161
failures over 98 channels, 90.7%**. Register 673 registers *869 to 930 interior cells* and Register
797 registers the 789; so chapter and Register agree with each other. **The class is not a wrong
figure but a stale one**: the compendium grew past both. Sweep stated in full — five row-filters
(all `m/k`; duplicates removed; two-member species excluded; neutrals only; undivided channels only),
sixteen ionisation-stage thresholds and two ℓ caps. **None returns 789, 546, 930, 869, 1,105 or
1,442.** Repair is a recomputation at the current basis, not a corrected digit.

**14r-02 — two of §24.2's seven contributors match nothing in the compendium.** Ne I printed
**16 channels / 131 cells** against measured **7 / 39**; K I printed **4 / 105** against **4 / 39**.
No species in the table has an interior sum of 131 or 105. Four rows are exact (He I 9/189, Al I
4/94, Na I 6/80, Ga I 5/61) and **Li I 3/55 resolves on undivided channels only** (39+8+8), which
confirms chat 98's 14p-17 reading of that column. So the table's basis is *undivided channels*, and
under that basis Ne I and K I — whose rows are all J-resolved — should read 0/0, not 16/131 and 4/105.

**14r-03 — §24.1 overstates three of its four spans.** ℓ measured **0 through 7** (four `nk` rows:
B V, Be IV, Li III ×2) against the printed *0 through 6*; Z measured **2 through 83** against the
printed *1 through 83*; ionisation stages measured **1, 2, 3, 4, 5, 6, 9** (the stage column reaches
16) against the printed *Z_eff 1 through 3*.

**14r-04 — the cores list contradicts its own count twice.** L6639 prints *core types 23, all
characterised*; L6644 lists **25 items**, one of them **3d⁹ ²D (declined)**. Both the count and the
"all characterised" fail on the same line pair.

**14r-05 — hydrogen has no channel row.** §24.7 calls H I *one row of the collection* and gives it
*5 cells* with a *median error of 0.006 cm⁻¹*. Swept across all six volumes: **zero H I channel
rows**; hydrogen appears only as an ionisation energy in the Löwdin supply (spectra L1119,
109678.77174307 cm⁻¹, which does corroborate §24.7's R_H). The 5 cells and the 0.006 are
unsourced — the thirteenth member of the unprinted-input class, and of the *inputs absent* half.

**14r-06 — §24.7 and §24.9 give hydrogen two different cell counts.** L6729 *H I gives 5 cells*;
L6781, in the same chapter, *Computed on H I … only 13 of 64 interior cells — 20%*. 13/64 = 20.3%,
so L6781 is internally sound; 5 and 64 cannot both be H I's interior count. **Flagged for chat 100**,
whose unit contains L6781.

**14r-07 — §24.3's monotone claim is false as stated, and the list that supports it is short two
channels.** L6669: *the defect falls monotonically with ℓ*. The nine He I rows in ℓ order run
+0.2965, +0.1392, −0.0133, +0.0014, +0.0007, −0.0010, −0.0014, −0.0015, −0.0016: signed monotonicity
breaks at p→d, and **|δ| rises at four consecutive steps from ¹D onward**. L6671 prints **seven means
for nine channels**, silently omitting **1snd ¹D (+0.0007)** and **1snh ¹H° (−0.0015)** — the omitted
h is precisely the step that would expose the reversal. Figure 24.1's caption at L6648 scopes the
same claim correctly (*wherever the defect is the core's*, *the three places it rises are marked*);
§24.3's sentence does not.

**14r-08 — "members" takes two meanings in one sentence.** L6672: *twenty members for ni and
twenty-three for the two ns channels*. He I ni carries **levels 20, interior 18**; each ns carries
**levels 25, interior 23**. So *members* = levels for ni and = interior for ns. Either reading makes
one of the two figures wrong.

**14r-09 — §24.4's "six orders of magnitude" belongs to a different claim.** L6690 calls the seven
He II values *monotone across six orders of magnitude*. They span **×47.9 = 1.68 orders**. The
six-orders figure is Figure 24.1's, over the whole collection (4.9 in Bi I to 1.6 × 10⁻⁶ in He II =
**6.49 orders**), and that one is exact. All seven He II values match compendium rows at the
compendium's precision, and are monotone decreasing — only the span is wrong.

**14r-10 — Li II's printed progression does not reproduce; Be II's does.** L6720 prints Li II
*0.182 → 0.054 → 0.002 → 0.0002*. Measured: s matches ³S (+0.1814) and p matches ³P° (+0.0543), but
**d and f match nothing** — ¹D +0.0011 and ³D +0.0027 bracket the printed 0.002 without equalling it,
¹F +0.0000 and ³F +0.0006 bracket 0.0002. Be II's four (**0.262 / 0.049 / 0.002 / 0.0001**) are exact
against its four rows. **The singlet/triplet selection is the unprinted convention** — fourteenth
member of the class, *conventions unstated* half.

**14r-11 — §24.6's ℓ = 5 claim fails on both species.** L6723: *Li II and Be II both give ℓ = 5
defects near −0.0003 — three members each*. Measured: Li II ¹H° **−0.0000, levels 4, interior 2**;
Be II ²H° **−0.0002, levels 5, interior 3**. Neither δ is −0.0003 and neither species has three
members under either reading of *members*.

**14r-12 — the witness offered for the pairing claim is not a pair.** L6718: *the δ progression has
the same shape in both members of every pair, scaled*, evidenced by **Li II** (helium-like) and
**Be II** (lithium-like) — one member each of two *different* pairs. The claim is about within-pair
shape; the evidence is across pairs.

**14r-13 — "neon II fail[ed] entirely" against 37 Ne II rows.** L6704/L6708 rest the dilution rule on
Ne II failing. Ne II carries **37 channel rows and 69 interior cells** in the compendium. The weaker
reading holds exactly — **none of its 37 rows is bracket-tested** — so the repair is to say which
failure is meant.

**14r-14 — the dilution formula is unverifiable as printed.** L6706: *cells per channel ≈ (measured
shells / D) − 2*. With D the number of parent J levels, the three witnesses give 2/5 − 2, 3/5 − 2 and
5/5 − 2, all negative, where measured cells per channel are 1–3. The relation the table actually
satisfies is **interior = levels − 2, exact on all 477 rows with three or more levels**. Either
*measured shells* is not the n-span or *D* is not the J count; neither is defined in the section.

**14r-15 — 0.006 × 54 ≠ 0.34.** L6735 says substituting R_∞ *inflates the median error 54-fold to
0.34 cm⁻¹*. 0.006 × 54 = **0.324**; 0.34 / 0.006 = **56.7-fold**. The two printed numbers are
mutually inconsistent at their own precision unless the unrounded median is carried, which is not
printed.

**14r-16 — "10⁻⁵ relative" is an order out at the light end.** L6737. Measured m_e/M across the 28
elements carrying rows: **He 1.37 × 10⁻⁴ down to Bi 2.63 × 10⁻⁶**. The claim holds from about Na
onward and fails for He, Li and Be — which are four of the seven species this very chapter features.

**14r-17 — Ruling 45, two sites in 118 lines.** L6628 *An earlier version of this chapter read …
the implementation behind Appendix B is not in hand*; L6632 *An earlier version of this chapter read
… reconciling needs the twenty rows, which are owed*. Both are editorial-process remarks in
reader-facing prose. Joins chat 97's L6453 and the L6483 caption.

**14r-18 — Ruling 46, a build number in reader-facing prose.** L6693 *the uncorrected series the
Spectra Compendium carried until **Build 9***. Volume-wide sweep: **main 2 sites (L6693, L7659),
Register 5 (L20, L31, L65, L68 …)** — seven in the reader-facing volumes.

**14r-19 — six channels are tabulated twice.** Ar II carries L326–L328 and L331 again at L367–L369
and L366 under a second configuration notation, and Si I carries L811/L812/L836 again at
L839/L841/L837 — same species, same normalised series, same n range, same levels, same limit; one
copy bracket-tested, the other `untested`, and two of the Si I pairs differ in δ in the fourth place
(+0.0126 vs +0.0129, +0.0570 vs +0.0573). **68 interior cells are counted more than once** in the
compendium's own totals. This is a *compendium* defect and it bears directly on 14r-01.

**14r-20 — the Edlén Handbuch chapter carries two dates.** L6676 *the 1960 manuscript*; L4550, L5433,
L5453, L8015, L8034 all **1964**; L11621 **1960**. Curtis's own title (L7964, *26 Years Later*,
1987) implies 1961. Consequently **L6683's *sixty-five years old*** is 66 against 1960 and 62 against
1964 in a 2026 text — right only against 1960 in 2025.

**14r-21 — a pointer that resolves to the heading but not the claim.** L6686: *they are ab initio QED
calculations, not Ritz series formulas. That distinction matters and §24.7 develops it.* §24.7
(L6725–L6740) carries **Ritz zero times**; it develops the reduced-mass identity instead. Swept:
*Ritz* has 31 main-volume sites, first L4550. **Ninth member of the pointer-off-by-one class.**

**14r-22 — a second pointer failing at the claim.** L6666: *the census of §24.12 excludes them
structurally.* §24.12 (L6844–L6856) carries **exclude / excludes / excluded zero times**; the whole
main volume has one site, L10881. Either §24.12 must say it or the caption must not claim it.
**Tenth member of the class.**

**14r-23 — two cases for Register citations inside 118 lines.** *Register 797* (L6628) and
*Register 783* (L6632) against *register 673* (L6632, same line) and *register 1758* (L6691).
All four resolve and none is a bare SUPERSEDED forward.

**14r-24 — "KI" set without its space, twice.** L6657 and L6716, both inside tables, against five
correct *K I* sites in the main volume and 37 in the Register. **14r-25 — the stage spelled in
words.** L6704 *neon II*, the only such site in the main volume (one more at Register L5994).

---

## B. Verified findings

1. **The unit's boundaries.** §24 at L6623, §24.8 at L6741, §25 at L6884; `section_span(24)` =
   (6623, 6884). Exact-token resolver, never prefix, never heading rank.
2. **The compendium's own totals line reproduces** — 596 rows, 2,269 interior cells, 28 elements.
3. **interior = levels − 2 on every one of the 477 rows with three or more levels**, zero exceptions;
   the 119 two-member rows print interior 1 by the compendium's stated convention, which is not a
   defect.
4. **He I: nine channels, ℓ 0 through 6, n to 35** — all three exact. All seven printed means equal a
   compendium δ at four places.
5. **He II: all seven values exact** at the compendium's precision, monotone decreasing, seven values
   against seven rows; **ng carries six members** exactly as L6697 says.
6. **The He II limit recovery is exact**: 438,908.885 − 438,908.871 = **0.014**, and 0.014/438,908.885
   = **3.19 parts in 10⁸** — *three parts in 10⁸* as printed.
7. **Figure 24.1's span is exact**: largest |δ| **4.9036** (Bi I ns), smallest non-zero **1.6 × 10⁻⁶**
   (He II ni), **6.49 orders**.
8. **Bi I, four for four**: δ̄ = **4.90** on the ns channel (HALF_UP, 2 dp, from +4.9036); **five
   members**; **the largest defect in the work** — Bi I holds the table maximum; **³P₀ reaches
   n = 11**.
9. **Ne I's "two limits" holds at its own scope** — the ²P°-core rows carry exactly two
   (173,929.750 and 174,710.090); the third Ne I limit belongs to the ¹P° row at L716 and is outside
   the claim. *Read the scope, not the species.*
10. **§B.3 confirms the Figure 24.1 caption**: Al I 3s²nd ²D and Al II 3snf ³F° are both flagged
    there as perturbed.
11. **Be II's four printed defects are exact**, and both Li II's and Be II's cited rows fall in the
    stated *five to ten members*.
12. **58.5 cm⁻¹** = 109,737.3 − 109,678.7717 = 58.5283, as printed.
13. **§32.5 does carry the 1,061 bound** L6683 sends the reader to — resolved to the claim, not the
    heading. Chat 97's 14n-A7 asked where 1,061 comes from; it is at least *stated* there.
14. **All four Register citations resolve** to live entries (673 at Register L2439, 783 at L2863,
    797 at L2919, 1758 at L6493), none a bare SUPERSEDED forward.
15. **Both figures are complete** — image directive plus caption for 24.1 and 24.2.
16. **L6634 is not the 14q-06 defect.** It is the §24.1 heading followed by a table header, exactly as
    DEFERRED's chat-98 block predicted. That site closes.
17. **The Curtis review is properly carried** in the bibliography at L7964–L7965 (Physica Scripta 35,
    805–810, 1987), outside the unit.

---

## C. Incidental

1. The compendium's He II rows carry the **derived** limit 438,908.871, not the tabulated
   438,908.885 — so the row rests on a limit this work computed, which §B.1's *constructed* caveat
   already contemplates. The tabulated value lives at main L6697 and Register 1758 only. Not a
   deviation; a provenance note that R3 should carry when it repairs 14r-01.
2. The channel table's tenth column is headed **fits** but takes the values 1, 2, 3, 4, 5, 6, 9, 11,
   15, 16 and tracks the ionisation stage. Header/content mismatch in the data volume.
3. Register 673 states the channel table ran **133 to 175 channels, 869 to 930 interior cells**; the
   compendium now stands at 596 and 2,269. The Register records the growth; nothing records the
   arrival at today's figures.
4. **Fourteen universal or near-universal sentences in 118 lines** — the highest density of the
   phase so far. Six are load-bearing for §24's argument.
5. L6624 promises *two collections*; the chapter names the bracket-tested one and Appendix B's, and
   *collection* occurs twelve times in the chapter without the second being defined in this unit.
6. **Single-witness figures in this unit: five of twenty-one distinctive figures** — the H I 5 cells,
   the 0.006 median, the 0.34, the 54-fold, and the 23 core types. Continues the R4 class.
7. §24.3's quotation of Curtis at L6678–L6680 is a block quotation of published text; its length
   should be checked against the permissions pass in production, not here.

---

## Instrument faults, self-caught and rewritten, none trimmed — thirteen

1. `q()` passed a `Fraction` to `Decimal(str(…))` → `ConversionSyntax`. 2. Assumed a 477-row table
from the handoff instead of measuring; the table is 596 and 477 is its ≥3-level subset. 3. Duplicate
detector keyed on species + n range, grouping *different* channels that merely share an n range —
120 false positives; re-keyed on a normalised series and returned six real ones. 4. The
interior = levels − 2 test counted the compendium's own two-member convention as 119 defects; scoped
to levels ≥ 3 and it is exact. 5. The Ne I limits test was mis-scoped past the core its sentence
names. 6. `ell()` used in the C1 sweep above its own definition. 7. The He II δ match demanded 5e-8
against a compendium that prints two significant figures. 8. The bibliography test for Curtis matched
the citing line itself. 9. The *five to ten members* test drew on every row of the species instead of
the rows the printed figures come from. 10. The 10⁻⁵-relative claim was first tested against
hydrogen's own ratio rather than the heavier species the sentence is about. 11. The ℓ = 7 and
stage-column results were asserted before the offending rows were printed as evidence. 12. The
tabulated He II limit was nearly recorded absent before the six-volume sweep was run. 13. My opening
report called HANDOFF-51's 477 "stale" — a verdict about a carried figure delivered before the basis
that produces it had been measured.

**The one worth carrying to chat 100:** *a carried figure that disagrees with a fresh count is not
wrong until the two bases are compared.* Chat 98 measured 477; I measured 596; both are right, on
different bases, and the difference is exactly the 119 two-member channels.
