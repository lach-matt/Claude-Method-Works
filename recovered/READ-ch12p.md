# READ-ch12p — Phase R2, main volume §12.11.0.12 "How an index enters a larger index, and what it looks like from there" (chat 75)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L2999–L3031 (33 lines, none over 400 characters; §12.11.1 opens at L3032), read in full against §12.11.0.9 (L2898, READ-ch12m), §22.1 (L5943–5951, the bracket rule), the Register (334 at R L1239–1241), the MC mirror (MC L1364–1370, whose figure sites the census lists), the banked r2-ch12e/f (Λ₉'s 41,682 composable pairs, ranks 3…23) and r2-ch12n (Λ₁₃'s length 43), the rebuilt tower (tower-2.py, c0bce27a…) and the segment instrument r2-ch12p.py (r2lib by path; all 199,130 cells of Λ₁₃, all 1,654 of Λ₉ and all 41,682 composable ordered pairs). Pointers: §12.11.0.9, §22.1 and Register 334 resolve to headings and claims. Census rows in range: none (CENSUS-CLOSURES-ch12p.tsv is a header).

## A. Deviations (both texts)

None of substance.

**12p-01 · layout.** L3021 four-space paragraph renders as code. Production.

## B. Verified (all MEASURED unless marked; r2-ch12p.py)

- L3004–3007 Λ₁₃ as a chain: rank = coordinate sum takes 44 contiguous values (3 … 46), one more than the lattice length 43 (r2-ch12n; max sum − min sum = 43, every step of the greedy cover chain raising the sum by one); log₂ 199,130 = 17.60 bits collapse to log₂ 44 = 5.46; compression 199,130 / 44 = 4,526 to 1; 12.14 bits per cell lost; 5.46 / 17.60 = 31.0 % survives. L3008–3009: dimension 1 of Λ (n) is a chain of 3 values.
- L3011–3013 Λ₉'s rank chain has 21 values (3 … 23) and the fibres beneath them run from 1 cell (ranks 3 and 23) to 185 (rank 12); the whole profile 1, 5, 15, 35, 63, 98, 131, 159, 177, 185, 181, 165, 139, 108, 77, 51, 32, 18, 9, 4, 1.
- L3015–3019: Λ₉ composes — 41,682 composable ordered pairs, all 41,682 composites inside Λ₉ (associativity: r2-ch12e on all composable triples); reduced to rank there are 264 distinct (rank a, rank b) inputs, 46 of which determine a single output rank = 17.4 % ("17 %" — the DEFERRED item "17 % of 264": the denominator is the 264 rank inputs, as the sentence says; by composable pairs the share would be 179 of 41,682 = 0.4 %); the worst spread is 12 output ranks, at the single input (13, 9); composite ranks lie in [3, 23], the full rank range of Λ₉.
- L3021–3025 §22.1 (L5943) resolves; L5947–5949 the bracket `T(n) lies between T(n−1) and T(n+1) … returns an interval rather than a value` — what L3021 says composition becomes one coordinate up.
- L3027–3029: the 185 cells are cells of Λ₉ (the rank-12 fibre of Λ₉ itself); every composite is a cell of Λ₉ (41,682 of 41,682), so every branch terminates in a cell of Λ₉. Register 334 (R L1241) carries the three answers (44 rank values, 12.14 bits lost, 31 %; branching to 185; composition a bracket).
- MC L1364–1370 carries 17.60, 5.46, 4,526, 12.14 (figure census); each reproduces.

## C. Incidental

- L3005 `the only chain-valued function ℛ accepts on it is its rank` is a statement about ℛ, not a computation; the rank used here (coordinate sum) is the grading r2-ch12f verified for Λ₉ and r2-ch12n's chain length is consistent with for Λ₁₃; whether other chain-valued gradings exist is not tested.
- Spread distribution over the 264 inputs: 46 · 1, 38 · 2, 33 · 3, 23 · 4, 24 · 5, 18 · 6, 19 · 7, 19 · 8, 20 · 9, 18 · 10, 5 · 11, 1 · 12; 124 of the 264 output sets are full intervals of ranks — "an interval" at L3021 is the bracket [min, max], not always every rank between.
- The §12.11.0 block (§12.11.0.1 … §12.11.0.12) is now read in full (chats 73–75); the L2779 "fourth" before L2838 "third" ordering matter (DEFERRED) is the block's only open cross-item, for the Chapter 12 close.
