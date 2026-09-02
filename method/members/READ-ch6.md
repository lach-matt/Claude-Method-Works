# READ-ch6 — Phase R2, main volume Chapter 6 "The periodic table is not a closed index" (chat 69)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L1511–L1723 (213 lines), read in full against (i) each cited section, (ii) the cited Register entries (298, 308, 348, 388, 390, 448), (iii) the chapter's own definition of ℛ (§6.1, L1535–1540) re-implemented and run on every index the chapter prints (r2-ch6.py, banked beside tower-2.py; the two-sided operator of r2-ch1.py run beside it for comparison). Labels as READ-ch3. Form follows SWEEP-B-C-chat67.md. Nothing in any volume was changed.

## A. Deviations (both texts)

**6-01 · L1687–L1688 (INPUT, the chapter's own standard).** PRINTED: `The input set is the chart itself, printed at §6.2 for Z ≤ 9`. SOURCE: §6.2 (L1594–1680) prints the nine absent cells (L1625) and no nuclide list; the chapter prints no (Z, N) set anywhere. MEASURED (read; grep). READING: the measurement §6.2.1 says is stated "to F.3's highest standard" has its input unprinted — §3.7.1's INPUT audit fails on this section by the book's own definition. r2-ch6.py reconstructs the particle-bound set from standard nuclear data (INFERRED input): Z ≤ 5 gives 27 / 33 / 6 with the six named cells, Z ≤ 6 gives 40 / 48 / 8, Z ≤ 7 gives 52 / 61 / 9 with the nine — each exactly the printed row; Z ≤ 9 gives 77 nuclides / 86 admitted / E = 9 against the printed 80 / 89 / 9. The three nuclides that separate 77 from 80 cannot be identified because the input is not printed.

**6-02 · L1719 against L1607.** PRINTED L1719: `Λ is the same 118 elements on different coordinates, with E = 0`. SOURCE: the §6.2 table row L1607 `Λ · 976 · 0 · yes`; Chapter 7 names 976 (L1786) and never 118; the 118-cell Λ is Register 35's Λ ⊆ ℕ³ (Register L211–213). MEASURED (grep). READING: the closing sentence describes the element index of an earlier build, not the Λ8 the table and Chapter 7 build — INFERRED as to which object.

**6-03 · L1585–L1587 (the Janet row's coordinate).** PRINTED: `left-step (Janet) · 120 · 0`; `Order the blocks f, d, p, s and define the period by n + ℓ`. MEASURED (r2-ch6.py): with the column counted from the s end (s = 1–2, p = 3–8, d = 9–18, f = 19–32) ℛ admits 120 and E = 0; with the column counted from the f end, as the prose orders the blocks, ℛ admits 256 and E = 136 — under both operators. READING: the result holds under one orientation of the column coordinate and the prose names the other; the coordinate that makes the row true is not stated (INPUT).

**6-04 · L1576–L1578 (attribution).** PRINTED: `IUPAC places it at 18; the left-step form and a quantum-chemical case place it at 2`. SOURCE: `Janet` occurs at 12 sites in the volume, none in the References (L11594 onward); the quantum-chemical case is unnamed. MEASURED (grep). READING: R-ATTR — Janet's table and the helium-at-2 argument are cited without a listed source.

**6-05 · L1535–L1536 (the definition).** PRINTED: `the value sets Âᵢ(X) = { xᵢ : x ∈ X } — which values occur the bounds φ̂ᵢⱼ(v) = max{ xᵢ : x ∈ X, xⱼ ≤ v }` — two definitions run together on one line inside a four-space-indented block. MEASURED. READING: a line break lost between `occur` and `the bounds`.

**6-06 · L1553 against L1581–L1585.** PRINTED: `Computed on four conventions over the same elements:` — followed by a digression (L1555–1579) and a table of three conventions. SOURCE: the fourth is the helium-at-2 variant printed separately at L1570–1572. MEASURED (read). READING: the sentence's table is three rows; the four are found only by adding the earlier table — INFERRED.

**6-07 · L1556.** PRINTED: `Recomputed on the drawn eighteen-column layout with all 118 elements` over a decomposition of the 36 cells of the 90-cell table. MEASURED (L1519). READING: the layout has 90 cells; the sentence's 118 is the element count, not the cell count.

**6-08 · L1597–L1613 (the §6.2 table).** PRINTED: the table split in two with its header printed twice (L1597, L1605) and the cardinality column escaped as `\       X\` at both. MEASURED. READING: one table; the second header is a break, not a new table (same escaped-bar class as READ-ch2's items).

**6-09 · Single-site figures.** `three eras` (L1665) — second site §12.11.0.1 (three occurrences of `era` in L2577–2640); `ninth subject` (L1658) — Register 348 (L1277) `TIME ENTERED AS THE NINTH SUBJECT … The other eight are things indexed`; the eight are not enumerated in either. MEASURED (grep). READING: resolves to the Register; the enumeration is record-carried.

**6-10 · L1498-class pointers.** Register 308 (L1656) sits only in the grouped heading `### 288, 308` (Register L1331); its individual content is not recoverable from the group. MEASURED (grep `^### `).

**6-11 · Layout.** Column dumps L1558–1561, L1570–1572, L1643–1644, L1690–1694; four-space-indented paragraphs L1535–1536, L1540, L1625, L1669–1670, L1696–1697, L1714; the markdown tables at L1517–1521 and L1581–1585 render as tables (the only ones in Chapters 1–6 so far). MEASURED.

## B. Verified (r2-ch6.py unless stated)

- 18-column table, f-block detached, helium at 18: 90 cells, ℛ admits 126, E = 36; the thirty-six are exactly (p1, g2–g17), (p2, g3–g12), (p3, g3–g12) (L1515–1523, L1583). Helium at group 2: E = 20 (L1572); the difference sixteen (L1578–1579). 32-column: 118 cells, admits 224, E = 106 (L1584). Both operators agree on all three.
- §6.1.1 decomposition: 1d 10 + 1p 5 + 2d 10 = 25 forbidden; 3d 10 + period-1 group 2 = 11 deferred; 25 + 11 = 36; 1p contributes five because helium occupies group 18 (L1559–1566); Register 448 (L1665) states the same. MEASURED arithmetic.
- Helium's triad He(2), Ne(10), Ar(18): 10 = (2 + 18)/2. MEASURED.
- §6.2: box ordering l ≥ w ≥ h with sides 1..6: 56 cells, E = 0; chessboard 64, E = 0; Λ8 976, E = 0 under §6.1's ℛ and under the two-sided operator; calendar (month, day) 365, E = 7, the seven = (2,29), (2,30), (2,31), (4,31), (6,31), (9,31), (11,31) (L1611, L1677); §6.3 relabelling by length (February, April, June, September, November, January, March, …) gives E = 0 (L1706–1708); February first alone gives E = 4 (not printed; noted).
- Figure 6.1 caption `seven indices, four self-defining` (L1529): the §6.2 rows are box, nuclide band, chessboard, Λ (yes) and subnet, calendar, periodic table (no) — 7 and 4. MEASURED (count).
- The audit index (§2.21 table) under §6.1's one-sided ℛ gives 11, 0, 19, 18, 17, 16, 16 — identical to the two-sided run of r2-ch3.py, so Chapter 3's E(audits) follows Chapter 6's definition.
- Ionization energies L1643–1644 match NIST first ionization energies to three decimals (Li 5.392 … Ar 15.760); the four refused steps fall at positions 2 and 5 of both periods (Be→B, N→O, Mg→Al, P→S); interior cells 2 × 6 = 12, 8 admissible = 67% (L1646–1649). NIST is listed in Appendix B (L10179). MEASURED.
- L1617 `ℛ is idempotent — §32.4.1 proves it`: §32.4.1 (L9085) at L9105 `ℛ(ℛ(X)) is cut by the same inequalities and equals ℛ(X) ∎`; also §14.2 (L3711) `ℛ is a closure operator`. L1591 §7.1 = L1750 `The constraints, and where each comes from`. L1659 §F.4.3 = L11343 `Time, which this work has and does not read`. L1660 §12.11.0 = L2535, L1672 §12.11.0.1 = L2577. L1682 §F.3 = L11278. MEASURED (grep).
- L1663–1666 `zero of 739 steps`, `904 of 1,654 cells`, L1673–1674 `seventeen-bit`, `24.7%`, `0.4%`: second sites L2581–2582, L2607, L2611, L2617–2618 (§12.11.0.1); 1,654 = |Λ9| (tower-2.py). MEASURED.
- Register headlines: 298 (L1117, the nuclide row conflated a band with a measurement; ℛ idempotent), 348 (L1277), 388 (L1441), 390 (L1449, §6.2.1's recomputation), 448 (L1665). MEASURED (`^### N`).
- L1616 a band between two monotone drip lines has E = 0 necessarily: a monotone lower bound on N given Z is an upper bound on Z given N, so §6.1's one-sided ℛ recovers both edges — INFERRED reasoning consistent with the operator; Register 298 states it as a theorem.

## C. Incidental

- L1719's 118 (6-02) is the same object as Register 35's `dim = 3` (READ-ch3 3-20): two survivals of the three-coordinate element index in a book whose Λ is Λ8. Whether Chapter 6 should say 976 or say "the elements' index" is M's.
- The subnet-with-a-hole row (L1609: 248 cells, E = 8) has no printed input; not reproduced.
