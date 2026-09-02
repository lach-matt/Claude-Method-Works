# READ-ch8 — Phase R2, main volume Chapter 8 "What Λ is — distributive, modular, Sperner" (chat 70)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L1796–L1935 (140 lines), read in full against (i) each cited section and Register entry, (ii) the rebuilt tower (tower-2.py, c0bce27a…), (iii) the chapter instrument r2-ch8.py (beside tower-2.py; `settings` mode for the cap ladder) and r2-tools.py. Rulings applied as in READ-ch7. Census rows in range: 1048, 1049 (closed in CENSUS-CLOSURES-ch8.tsv).

## A. Deviations (both texts)

**8-01 · L1863 (§8.3) against L1799–1802 (the chapter's own convention).** PRINTED: `Across six settings from 976 to 27,873 cells the generator count grows — 17, 23, 31, 32 — while the *patterns* hold at fifteen, with zero new and zero lost.` SOURCE: 27,873 has no other site in any volume; no site prints the six settings; four counts are listed for six settings; "patterns" is not defined at the site or elsewhere by grep. MEASURED (r2-ch8.py settings; ji_fast): 27,873 cells is the setting (n, e, ℓ, f, k) = (6,5,2,2,5), unique in n,e ≤ 6, ℓ,f ≤ 2, k ≤ 8; join-irreducible counts **17 at 976 (3,3,1,1,3), 23 at 3,363 (4,4,1,1,4), 31 at 21,775 (5,5,2,2,5), 32 at 27,873 (6,5,2,2,5)** — all four printed values reproduce at natural settings (settings INFERRED as the book's; values MEASURED). READING: the values are true; the settings are not printed beside the figure although L1801 says they are, two of the six settings and their counts are absent, and "fifteen patterns" is unverifiable as printed. Not a false claim; a stated-convention breach at the site that states the convention. For the prose pass: print the six settings and their six counts, define "pattern".

**8-02 · L1837–1838 (§8.2.2).** PRINTED: `on a graded lattice with this rank function it [modularity of rank] is equivalent [to distributivity]`. INFERRED (standard): rank-modularity is equivalent to lattice modularity, not to distributivity — M₃ is graded, its rank satisfies r(a∨b) + r(a∧b) = r(a) + r(b) on every pair, and it is not distributive. The direction the section uses (L1845 "a failure of modularity is a failure of distributivity") is correct; "equivalent" overstates it. For a sublattice of a product of chains with rank Σxᵢ both properties hold outright (MEASURED here), so nothing computed is affected. Wording overclaim in a mathematical statement; correction: "necessary" (or "equivalent to modularity"). For R3, low.

**8-03 · L1874–1875 (§8.4).** PRINTED: `verified exactly at five cap settings by Dilworth's theorem and bipartite matching`. SOURCE: the five settings are not named. MEASURED (r2-ch8.py, Hopcroft–Karp on the comparability graph): width = largest rank level at (2,2,1,0,3) 29 = 29, (3,3,1,1,3) 122 = 122, (3,3,1,1,4) 160 = 160; log-concave at all three. Reproduced where tested; the other two settings unnamed. Same class as 8-01; for the prose pass.

**8-04 · L1849, L1875, L1883.** `At caps (3,3,1,3), k ≥ 1` — four-tuples against the five-tuple convention stated at L1800 in the same chapter. Already recorded as READ-ch7 7-01 (defect); no separate closure.

**8-05 · L1804–1806, L1822, L1851, L1882–1883, L1904 (layout).** Four-space-indented display lines render as code blocks; L1863 table and L1857–1861 fine. MEASURED (r2-tools.py layout). Production.

## B. Verified (claim and source agree; instrument where one exists — all MEASURED unless marked)

- L1800 the caps (3,3,1,3,1) rebuild Λ₈ to 976 (READ-ch7).
- L1808–1809 "84 paragraphs … 69 name no cap … 82 %": 69/84 = 82.1 %; Register 395 (R L1467) records exactly these figures — record-carried.
- L1814 distributive: sublattice of a product of chains (INFERRED, standard); 20,000 random triples, 0 failures.
- L1822–1824 rank modularity on all 475,800 = C(976,2) pairs: 0 violations.
- L1836 O(n³) vs O(n²), L1842–1843 timings 0.0375 s / 0.0188 s "half the work": 0.0188/0.0375 = 0.50 (arithmetic); timings themselves not reproducible.
- L1851–1853 976 cells ← 17 join-irreducibles, 20 covering relations; all 976 down-sets of the 17-element poset are the 976 cells; 976/17 = 57.4 "fifty-seven-fold": all reproduced (down-sets counted by enumeration of the 2¹⁷ subsets).
- L1857–1861 the four printed covers e=2 ⋖ e=2,f=1; k=2 ⋖ k=2,q=2; n=2 ⋖ n=2,ℓ=1 ⋖ n=2,ℓ=1,k=3: each pair both join-irreducible and a cover in J(Λ₈).
- L1876 maximum 122 at rank 11: rank sequence [1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1] over ranks 3–20; L1878 log-concave hence unimodal: true.
- L1880 not rank-symmetric: true; no symmetric chain decomposition follows (INFERRED, standard).
- L1882 centre of mass 11.07, midpoint 11.5, skew −0.43: 11.07 / 11.5 / −0.43 exactly.
- L1885 floors n, k, e ≥ 1 and caps: min (1,0,1,0,1,0,0,0), max (3,1,3,3,3,1,3,3) — the three floors and the listed caps are the binding ones.
- L1887–1890 8 of 976 cells survive x ↦ max − x; 112 have their image in Λ under x ↦ max + min − x and none is fixed: 8 / 112 / 0.
- L1892 particle–hole conjugation terms(ℓᵏ) = terms(ℓ^(4ℓ+2−k)): standard (INFERRED). §12.11.2 as one of three machines — record-carried to Ch. 12.
- L1902–1904 tree e — f — g — q — k — ℓ — n with 2S on k: the seven edges of READ-ch7 (MEASURED).
- L1908 Ch. 10 closed-form void count; L1910 Ch. 15 order recovery 20 of 20; L1912 Ch. 16 two-route protection — record-carried to their chapters.
- L1915 order dimension 7, seven linear orders and no six: width(J(Λ₈)) = 7 by Dilworth (matching), maximum antichain of seven exhibited — one generator per coordinate except g: (3,0,1,0,1,0,0,0) n, (2,1,1,0,1,0,0,0) ℓ, (1,0,2,0,1,0,0,0) k, (1,0,1,1,1,0,0,0) q, (1,0,1,0,3,0,0,0) e, (1,0,1,0,2,1,0,0) f, (1,0,1,0,1,0,0,1) 2S. Dimension = width of J for a finite distributive lattice: standard (INFERRED); confirmed by HANDOFF-20's carried width 7.
- L1923–1926 the g-atom (1,0,1,1,1,0,1,0) is join-irreducible and lies above the q-atom (1,0,1,1,1,0,0,0): true.
- L1928 Λ₉ measures width 7: |Λ₉| = 1,654, 20 join-irreducibles, width(J(Λ₉)) = 7.
- L1918–1919, L1932 Register 409 (R L1523) "dim(Λ₈) = 8 was asserted and is Dilworth's, being the width of J(Λ)": as cited. L1930 Register 36 (R L215) exhibits S₃ within Λ — the "exhibit the antichain" method: as cited.
- L1934 976 of 6,912 = 14.1 %: box = 3·2·3·4·3·2·4·4 = 6,912; 14.12 %.
- Pointers §6.2.1, §12.11.1.1, §12.11.1.2, §22.1.1.1, §32.4.2, §8.1, §8.3, §7.1, §12.11.2, Ch. 10/12/15/16, Figures 8.1 and 8.2 (placed L1867, L1896): all resolve to headings carrying the cited matter (r2-tools.py pointers).

## C. Incidental

- Census 1048 ("had never been written down"): Register 395 states it in the same words — not a defect. Census 1049 ("the eighth is never spent"): dim = 7 < 8 measured — not a defect.
- The generator-count ladder (MEASURED, ji_fast): 976→17, 1,636→21, 1,968→19, 2,394→22, 2,680→25, 3,363→23, 4,428→24, 6,739→25, 9,520→29, 12,451→27, 15,885→28, 21,775→31, 27,873→32, 57,645→37 — banked for whoever prints the six settings.
