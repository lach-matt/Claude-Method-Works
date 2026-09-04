# READ-ch9 — Phase R2, main volume Chapter 9 "The arithmetic encoding" (chat 70)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L1936–L2020 (85 lines), read in full against (i) each cited section and Register entry, (ii) the rebuilt tower (tower-2.py, c0bce27a…), (iii) the chapter instrument r2-ch9.py (beside tower-2.py) and r2-tools.py. Rulings applied as in READ-ch7. Census rows in range: none; CENSUS-CLOSURES-ch9.tsv is the header alone.

## A. Deviations (both texts)

**9-01 · L2019 (§9.3) — a stated biconditional that is false in general.** PRINTED: `μ_Λ = μ_arith **iff** the interval is a void-free unit hypercube. Exact — 60 void-free pairs all agree, 56 void-bearing pairs all disagree, no mixed case.` MEASURED (r2-ch9.py, all 115,162 comparable pairs of Λ₈; μ_Λ by the closed form of L2015, itself verified against the recursive definition on 300 of 300 sampled pairs; μ_arith = the number-theoretic Möbius function of N(y)/N(x)): void-free unit hypercubes 18,103 — all agree; void-bearing unit hypercubes 17,104 — all disagree; **non-unit intervals (some Δᵢ ≥ 2) 79,955 — all agree, both functions being 0** (13,501 void-free, 66,454 void-bearing). Agreement therefore holds on 98,058 of 115,162 comparable pairs, not only on void-free unit hypercubes. READING: the 116 tested pairs were evidently all unit hypercubes, and the biconditional was stated for the whole lattice. True statement: *restricted to unit-hypercube intervals*, μ_Λ = μ_arith iff the interval is void-free; on every non-unit interval both vanish. Defect, subject-matter (an "Exact" theorem overgeneralised from its sample). For R3: restate with the restriction; a Register correction entry (both states kept).

**9-02 · L1996–2002 (§9.2 "Five equivalent forms") with L1994 and the Figure 9.1 caption L2009.** PRINTED: form 1 `|[x∧y, x∨y]| — interval count`; L1994 `The measure counts *cells*, and a cell is occupied`; L2009 `d(x,y) counts cells in the interval between two points`; `verified 500/500 and 2,000/2,000`. MEASURED (r2-ch9.py, 2,000 random pairs): forms 2, 3, 4, 5 agree 2,000/2,000; form 1 read as the number of **cells of Λ** in [x∧y, x∨y] agrees with form 2 on 580 of 2,000; over all 475,800 pairs the box [x∧y, x∨y] contains a non-cell for **340,929 (71.7 %)** and is void-free for 134,871 (28.3 %). READING: the five forms are equivalent only when the interval is taken in the divisor lattice (the box, every point of which is a divisor of lcm/gcd) — which is the encoding's own lattice (L1949) — and not in Λ, where the interval usually has voids (as §9.3 itself says at L2019). "Counts cells" is false under the natural reading for 71.7 % of pairs. Defect, subject-matter (definition stated loosely at its home). For R3: say "counts the points of the box [x∧y, x∨y] — the divisors of lcm/gcd — of which Λ's cells are a subset".

**9-03 · L1965 and L1982–1983.** PRINTED: `the orders are partial and share 0.3%`; `the 0.3% overlap`. SOURCE: 0.3 % has 7 other sites (3 in main); its definition is not given in this chapter. MEASURED here: comparable pairs are 24.2 % of all pairs (115,162 of 475,800), so 0.3 % is not comparability. Record-carried to the site that defines it (Ch. 18/27 region — to be read in its chapter); not closed here.

**9-04 · L1943–1947, L1970–1974, L1998–2002 (layout).** Space-aligned column dumps and four-space display lines (L1939, L1949, L1959, L1963, L2015) render as code blocks. MEASURED (r2-tools.py layout). Production.

## B. Verified (all MEASURED unless marked)

- L1939–1947 N(x) = ∏pᵢ^{xᵢ}: x ≤ y ⇔ N(x) | N(y), join = lcm, meet = gcd, rank Σxᵢ = Ω(N): 0 violations on all 976 cells and all 475,800 pairs.
- L1949 Λ is a sublattice of the divisor lattice of one integer (N(top)): INFERRED, immediate.
- L1952 rank = Ω(N) on all 976 cells: true.
- L1954 ω(N(x)) ≤ 8, tight at (2,1,3,3,2,1,3,3): that cell is in Λ, ω = 8 there (and at 99 other cells); ω can exceed dim = 7: true (8 > 7).
- L1959, L1971 d = ∏(|Δᵢ|+1) = τ(lcm/gcd): forms 2–5 agree on 2,000/2,000 (see 9-02 for form 1).
- L1992 d(x,x) = 1: true.
- L2003–2004 symmetric; d ≥ 1 with equality iff x = y; multiplicative triangle inequality 4,000 of 4,000: 0 violations on 4,000 fresh triples. log d = Σ log(|Δᵢ|+1) is a metric (sum of per-axis concave metrics) — INFERRED; "ordinary ℓ¹" is loose (ℓ¹ sum of log-distorted axes, as L2005 itself says); balls hyperbolic with boundary (1+Δ₁)(1+Δ₂) = D, steps log 2 and log(11/10): INFERRED, immediate.
- L2015 Möbius closed form (Rota, Λ ≅ J(P), |P| = 17): = recursive definition on 300 of 300 sampled comparable pairs; values in {−1, 0, +1} on all 115,162.
- L2019 "60 void-free pairs all agree, 56 void-bearing pairs all disagree": consistent with the measured behaviour on unit hypercubes (see 9-01 for the general statement). "Decidable in seven comparisons": the box [x∧y, x∨y] lies in Λ iff each of the seven constraints holds at its worst corner (bounded coordinate at the top, bounding coordinate at the bottom) — agrees with brute force on 3,000 pairs.
- L1972–1974 middle and third rows (17 % of 264 inputs single-valued, worst spread 12, range [3, 23]; w priced at V = 4ν/3): §12.11.0.12 (L2999) and §22.1 (L5943) — record-carried to Chapters 12 and 22. L1977 §27 "proves the three measures are one quantity" — record-carried to Ch. 27.
- L1980–1982 Theorem 18.2 (4 other main sites, L5344 …), §18.6 (L5303), §25.6.3 (L7039), §14.3 (L3719), §18.4.1 (L4999), Register 438 (R L1627): all resolve; claims record-carried to their chapters.
- Figure 9.1 placed at L2007.

## C. Incidental

- Void-free boxes are 28.3 % of all pairs and 27.3 % of comparable pairs (31,604 of 115,162); the figure may be useful to whoever restates 9-01 and 9-02.
