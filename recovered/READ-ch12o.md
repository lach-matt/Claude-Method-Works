# READ-ch12o — Phase R2, main volume §12.11.0.11 "The fourteenth axis, and what can be said about it from inside" (chat 75)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L2957–L2998 (42 lines, none over 400 characters; §12.11.0.12 opens at L2999), read in full against §11.1.1 (L2094–2127; the surplus at L2113–2115), §22.1.2 (L6006–6033; the rule at L6022 and L6027), §32.1.4 (L8963–8992; the boundary at L8989–8990), P19 (L373–383), the Register (333 at R L1235–1237), the MC mirror (MC L1354, whose figure sites the census lists), the rebuilt tower (tower-2.py, c0bce27a…) and the segment instrument r2-ch12o.py (r2lib by path; every stage on every cell). Pointers: §22.1.2, §32.1.4 and Register 333 resolve to headings and claims. Census rows in range: 1067 (C9), closed in CENSUS-CLOSURES-ch12o.tsv.

## A. Deviations (both texts)

**12o-01 · L2962–2968 against L2997 (with L2949 of §12.11.0.10 and §11.1.1 L2113–2115) — "surplus" names two different quantities, and the section gives Λ₈ both values.** PRINTED L2962–2963: `D    cells      ambient box     fill     bits carried   needed   surplus` / `8      976           6,912   14.12%            12.75     9.93      2.82` — surplus = log₂ box − log₂ cells, 2.82 bits at Λ₈. PRINTED L2996–2997: `What distinguishes Λ from the empty index is not closure but |J(Λ)| = 17 and its seven bits of surplus.` — §11.1.1's surplus, L2113–2115: `bits carried per cell 17 / bits needed to index 976 cells 9.93 / surplus 7.07 bits per cell`. And §12.11.0.10 L2949–2950 argues from the fill ("so **the surplus §11.1.1 measures at seven bits per cell in Λ₈ grows at every step**") for the generator quantity. MEASURED (r2-ch12o; r2-ch12n): both quantities exist and both rise at every step — box surplus 2.82 → 4.06 → 5.45 → 5.61 → 6.23 → 7.91 bits; generator surplus |J(Λ_d)| − log₂ cells = 7.07 → 9.31 → 11.69 → 14.27 → 18.89 → 25.40 bits — and they differ at Λ₈ by 4.25 bits (17 generators against log₂ 6,912 = 12.75 box bits). No printed figure is wrong; the one word "surplus", and the one "bits carried" (17 in §11.1.1, 12.75 here), name different measures across §11.1.1, §12.11.0.10 and this table, and a reader of this section alone reads Λ₈'s surplus as 2.82 in the table and "seven bits" at its last line. Definitional; for R3 (name the two: box surplus / generator surplus, or carry both columns).

**12o-02 · layout.** L2962–2968 column-dump table (6 gaps per row); L2976–2977 four-space paragraph renders as code. Production.

## B. Verified (all MEASURED unless marked; r2-ch12o.py)

- L2962–2968 the table: cells, ambient box and fill as READ-ch12n B; bits carried = log₂ box 12.75 / 14.75 / 16.75 / 19.34 / 22.34 / 25.51; needed = log₂ cells 9.93 / 10.69 / 11.31 / 13.73 / 16.11 / 17.60; surplus 2.82 / 4.06 / 5.45 / 5.61 / 6.23 / 7.91 — all to the printed two decimals.
- L2970: fill falls at every step and surplus rises at every step (both True along D = 8 … 13).
- L2971–2973 the law: at every new axis the mean multiplicity (cells ratio) is strictly below the new coordinate's value count (box multiplier) — 1.695 < 4, 1.533 < 4, 5.359 < 6, 5.219 < 8, 2.808 < 9 — and no axis is free (at every stage some fibre is smaller than the full value set: fibre sizes {1,2,3,4}, {1,2,3,4}, {4,5,6}, {3,…,8}, {2,3}); the "if it did not, it would be free" step is exact (mean multiplicity equals the value count only when every fibre is the full set). Fill is therefore monotone decreasing and bounded below by 0 — a deduction, as L2979 says.
- L2976, L2981: the limit exists (monotone, bounded) and lies in [0, 0.42 %] — fill at D = 13 is 0.4168 %, within the printed bracket; that the limit is 0 does not follow from the construction (nothing computed here bears on it).
- L2979–2980 ratios stage to stage 0.424, 0.383, 0.893, 0.652, 0.312 — reproduce to three decimals and are not monotone. §22.1.2 (L6006) resolves; its rule is L6022 `take the next width from the law, not from the pattern` and L6027 `Presume the next bracket from the law … never from the pattern` — the existence/value distinction L2981–2983 draws.
- L2986 §32.1.4 (L8963) resolves; L8989–8990 `E names cells; it never names a coordinate. Every one of the fifty-five is a combination of values the index already carries` — the claim restated (census 1067).
- L2992–2994 the empty index: E(∅) = 0 (no pair to fail), Q(∅) = ∅, and P19 is `COMPLETE ⟺ Q = ∅` (L381), `strictly stronger than closure` (L383); zero join-irreducibles, zero bits — definitional, consistent.
- L2997 |J(Λ₈)| = 17 (greedy maximal chain; r2-ch12c's figure) and 17 − 9.93 = 7.07 bits (§11.1.1's "seven bits"). Register 333 (R L1237) carries the section's four claims verbatim in substance.
- MC L1354 carries the table's bits figures (12.75, 2.82, 4.06, 5.45, 5.61, 6.23, 25.51, 17.60, 7.91 per the figure census); every one reproduces.

## C. Incidental

- L2986 attributes to §32.1.4 "ℛ never produces a coordinate"; §32.1.4 says it of E (the named cells). Same boundary, different subject word.
- The bracket [0, 0.42 %] is stated with the rounded fill; the measured upper bound is 0.4168 %.
- The fill ratios equal (cells ratio)/(value count) at each step, so L2979's five numbers are the law's five inequalities read as fractions — 0.424 = 1.695/4 and so on; the table and the ratios are one measurement.
- r2-ch12o.py reuses r2-ch12n's `length()`; the two surpluses should be lifted into r2lib as named functions when the MC segment reads MC L1074 (9.93), L1354 and L1364.
