# READ-ch12n — Phase R2, main volume §12.11.0.10 "Every Λ in one table" (chat 75)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L2932–L2956 (25 lines, none over 400 characters; §12.11.0.11 opens at L2957), read in full against §11.1.1 (L2094–2127, the surplus table at L2113–2115), the Register (315 at R L1171–1173; the lowercase `register 249` at L2945, missed by r2-tools' case-sensitive regex, resolved by hand to R L983–985), the MC mirror (MC L1342–1344), the banked r2-ch12c (17 join-irreducibles of Λ₈), r2-ch12e (the tower axes, composition), r2-ch12f (Λ₉'s length 20) and r2-ch12i (Λ₉, Λ₉′ closure), the rebuilt tower (tower-2.py, c0bce27a…) and the segment instrument r2-ch12n.py (r2lib by path; every row of the table on every cell of its stage). Census rows in range: 1066 (C9), closed in CENSUS-CLOSURES-ch12n.tsv.

## A. Deviations (both texts)

None of substance.

**12n-01 · layout.** L2935–2942 column-dump table (5–7 gaps per row). Production.

## B. Verified (all MEASURED unless marked; r2-ch12n.py)

- L2936–2942 cells: 976 / 1,654 / 1,561 / 2,535 / 13,585 / 70,905 / 199,130 — tower-2.py by path; the Λ₉′ row is r2lib.lam9p (Λ₉ ∩ {2S′ ≤ 2f+1}).
- L2936–2942 ambient box = Π(max − min + 1) over the realised coordinate ranges: 6,912 / 27,648 / 27,648 / 110,592 / 663,552 / 5,308,416 / 47,775,744; fill 14.12 / 5.98 / 5.65 / 2.29 / 2.05 / 1.34 / 0.42 % to the printed two decimals.
- L2936–2942 E = 0 at all seven: pairwise, on every ordered pair, for Λ₈ (952,576 pairs), Λ₉ (2,735,716), Λ₉′ (2,436,721), Λ₁₀ (6,426,225) and Λ₁₁ (184,552,225) — 0 failing joins, 0 failing meets each; for Λ₁₂ and Λ₁₃, whose 5.0 · 10⁹ and 4.0 · 10¹⁰ pairs exceed this container, the exact fibre-interval criterion: every one of the 13,585 prefixes of Λ₁₂ carries exactly the fibre 2K ∈ [0, 2J_c + 2·f_max] and every one of the 70,905 prefixes of Λ₁₃ exactly 2J ∈ [max(0, 2K − 1), 2K + 1] (verified cell by cell), and on all 36, resp. 64, realised value pairs of the bound coordinate the four interval inclusions hold with 0 violations — so, Λ₁₁ being closed pairwise, Λ₁₂ and then Λ₁₃ are closed (the criterion is an equivalence: the fibres are full intervals, so their pairwise maxima and minima range over exactly the intervals tested). Register 249 (R L985) records the box-exhaustive test to 47,775,744 cells; this chat reproduces E = 0 by the two routes above, not by that one (C).
- L2936–2942 the "new coordinate / bounded by" column is tower-2.py's stage definitions (r2-ch12e.out's axes line): 2S′ ≤ g; Λ₉′ adds 2S′ ≤ 2f+1; 2S′ ≤ v ≤ g; 2J_c ≤ φ̂(k) with φ̂ = {1: 3, 2: 4, 3: 5}; 2K ≤ 2J_c + 2f_max with f_max = 1; |2J − 2K| ≤ 1 (with the spin floor 2J ≥ 0 that tower-2.py applies at 2K = 0).
- L2936–2942 the composition half of the grading column: Λ₈ and Λ₁₀–Λ₁₃ do not compose (target tuple 3, 5, 6, 7, 8 coordinates against a 4-coordinate source — no target is a source); Λ₉ composes (1,169 composable cells, all 41,682 composable ordered pairs compose inside Λ₉) and so does Λ₉′ (1,076 composable cells; all 35,532 composites inside Λ₉′). L2953–2954 `Composition is lost at Λ₁₀ … Λ₁₀ … exact and does not compose, and no stage that composes without being exact` agrees with the table's two columns (the exact/envelope half is the book's classification — C).
- L2944–2946: E = 0 at all seven (above); `forty-seven million cells at Λ₁₃` = 47,775,744 (the box); `per register 249` resolves (R L985); census 1066's `never spends` is exact over the seven stages.
- L2948: fill falls monotonically along the main tower, 14.12 → 5.98 → 2.29 → 2.05 → 1.34 → 0.42 %; at every step the box grows faster than the object (box ×4.00, ×4.00, ×6.00, ×8.00, ×9.00 against cells ×1.695, ×1.533, ×5.359, ×5.219, ×2.808).
- L2949–2950 §11.1.1 (L2094) resolves; its surplus at L2113–2115 is bits carried 17 − bits needed 9.93 = 7.07 per cell for Λ₈. Recomputed as |J(Λ_d)| (the lattice length, by a greedy maximal chain; = 17 for Λ₈ and 20 for Λ₉, r2-ch12c's and r2-ch12f's figures) minus log₂ cells: 7.07 → 9.31 → 11.69 → 14.27 → 18.89 → 25.40 bits per cell at Λ₈ … Λ₁₃ — it grows at every step, as printed (Λ₉′: 9.39).
- L2955 Register 315 (R L1173) carries the section: E = 0 at every stage, fill falling monotonically 14.12 % to 0.42 %.
- MC L1344 mirrors the table's figures (5.98, 5.65, 2.29, 2.05, 1.34 %, from the figure census); every figure reproduces.

## C. Incidental

- L2949's "so": the fill's decrease is the *box* surplus log₂(box/cells) (2.82 → 4.06 → 5.45 → 5.61 → 6.23 → 7.91 bits), while "seven bits per cell" is §11.1.1's *generator* surplus (|J| − log₂ cells). Both grow at every step, so the sentence is true, but it names one quantity and argues from the other.
- Register 249's box-exhaustive closure (every box cell, 47.7 M at Λ₁₃) is not reproduced in this container; E = 0 is reproduced pairwise to Λ₁₁ and by the exact fibre criterion above it. No disagreement with the record.
- The exact/envelope half of the grading column (exactness "lost at Λ₁₁") is a provenance classification with no computation behind it here; §12.11.3.1 (L3409–3461) carries it with 12j-01's "three values, not two" (DEFERRED) — the two-valued column here may be the site that line was written against.
- L2933 `reported in six places under six aspects` is not testable from the sentence (the six are not named); the tower's cell counts appear at many more than six sites (r2-tools: 199,130 at 13 main sites).
- L2942's `|2J − 2K| ≤ 1` reads as symmetric; tower-2.py floors 2J at 0, which only bites at 2K = 0 (2J ∈ {0, 1}); the box count 47,775,744 = 9 · 5,308,416 is on the realised range 0…8 either way.
- r2-ch12n.py's `length()` (greedy cover chain, exact on any finite lattice with a bottom) and `fibre_check`/`criterion` are reusable for §12.11.1's per-axis sections and for any closure claim above Λ₁₁; the instrument runs in about 60 s, the Λ₁₁ pairwise closure being 40 s of it.
