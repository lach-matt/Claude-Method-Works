# READ-ch7 — Phase R2, main volume Chapter 7 "The construction of Λ" (chat 70)

Member The_Method_1_6-2.md (BUILD90 main, md5 4aef772b…), L1724–L1795 (72 lines), read in full against (i) each cited section, (ii) the rebuilt tower (tower-2.py, c0bce27a…), (iii) the chapter instrument r2-ch7.py (beside tower-2.py) and the clerical checker r2-tools.py. Rulings applied: A vocabulary; an unreferenced prior-art attribution is a defect; a co-located stale figure counts against its census row. The chapter has **no census rows** (r2-tools.py census 1724 1795 → 0); CENSUS-CLOSURES-ch7.tsv is the header alone.

## A. Deviations (both texts)

**7-01 · L1790 (§7.4), with L1800, L1849, L1875, L1883 (Ch. 8) and L3065 (§12.11.5).** PRINTED L1790: `every count in this book is stated at explicit caps on n, e, ℓ and k` — four coordinates. PRINTED L1800: `(n_max, e_max, ℓ_max, k_max, f_max) = (3, 3, 1, 3, 1)` — five. PRINTED L1849, L1875, L1883: `At caps (3,3,1,3), k ≥ 1` — four. PRINTED L3065: `f_max — the cap on f under §7.4` — attributes to §7.4 a cap §7.4 does not name. MEASURED (r2-ch7.py): the seven constraints of §7.1 at (n, e, ℓ, k) ≤ (3, 3, 1, 3), k ≥ 1 give **1,176** cells with f bounded only by f ≤ e−1, and **976** only with f ≤ 1 added; k ≥ 0 instead of k ≥ 1 gives 1,001. READING: the object's defining count cannot be rebuilt from §7.1 and §7.4 as printed; the fifth cap is stated once (L1800) and cited back to a section that omits it. Defect (definition under-specified at its home; four-tuple and five-tuple cap statements coexist). Correction site: §7.4's list (add f, or "the two subshell coordinates ℓ and f"), and the three four-tuples in Chapter 8 to match L1800. For R3.

**7-02 · L1786 (§7.3).** PRINTED: `verified by direct computation at four cap settings — 216, 976, 1,636 and 2,394 cells`. SOURCE: 2,394 has no second site in any volume (r2-tools.py figures); 216 and 1,636 recur at L3975 and Register L2225 as the ends of a range for a different test (seed necessity), not as E-sites. MEASURED (r2-ch7.py): the settings are (n, e, ℓ, f, k) = (2,2,1,0,3) [216, one of 60 settings giving that count], (3,3,1,1,3) [976], (3,3,1,1,4) [1,636], (4,3,1,1,4) [2,394]; **E = 0 at all four, first pass +0, second pass +0** — the claim reproduces. READING: not a false claim; the settings are not printed beside the figures although Chapter 8 L1798–1800 promises "where a figure is recomputed under variation the settings are printed beside it". Not a defect on the ruled classes; incidental gap for the prose pass (print the four settings).

**7-03 · L1773–1774 (Figure 7.1 caption) and L5150.** PRINTED L1774: `Three results in this book follow from that fact alone.` — the three are not named at the site or anywhere the phrase is cited. PRINTED L5150 (Ch. 18): `Λ's own shape, which §7.1 says three central results follow from` — the caption sits under §7.2 (L1764), not §7.1. MEASURED (grep `treewidth`, 8 sites): candidates are exact closure at treewidth 1 (§18.4.1, L2863), the tree factorisation of the void count (A.10, L?), and arc-consistency sufficiency at treewidth 1 (L5693). INFERRED: the enumeration is owed. Named-statement without its list; pointer §7.1 → §7.2 wrong by one subsection. Not subject-matter; for the prose pass.

**7-04 · L1792 (§7.4).** PRINTED: `identical across a twenty-eight-fold range in cell count`. SOURCE Ch. 8 L1928: `six settings from 976 to 27,873 cells`. MEASURED: 27,873 / 976 = 28.56. READING: "twenty-eight-fold" is a floor of 28.6; the top setting 27,873 was not reached by any (n, e ≤ 5; ℓ, f ≤ 3; k ≤ 8) setting of the §7.1 constraints (r2-ch7.py grid) — Chapter 8's settings to be read in its own segment. Carried to Ch. 8.

**7-05 · L1728, L1782 (layout).** Four-space-indented display lines `(n, ℓ, k, q, e, f, g, 2S)` and the join inequality render as code blocks; L1753–1760 is a space-aligned column dump (the constraint table). MEASURED (r2-tools.py layout). Production; same class as READ-ch3 3-31.

## B. Verified (claim and source agree; instrument where one exists)

- L1751–1760 the seven constraints: identical to tower-2.py's L8() (MEASURED, set equality of 976 cells rebuilt from the printed text).
- L1762 "seven constraints, four origins": 7 rows; origins hydrogenic ×2, Pauli ×2, counting ×2, vector coupling ×1 = 4 (MEASURED).
- L1741–1743 five further coordinates 2S′, v, 2J_c, K, 2J in that order; coupling order J_c, K, J: matches tower-2.py's stage order (2S′, v, 2J_c, 2K, 2J) and §12.11.1's table L2941–2942 (axis named K, bound 2K ≤ 2J_c + 2f_max) (MEASURED).
- L1745–1748 three exact origins and one envelope: §12.11.3 L3394 "Counting coordinates close exactly. Coupling coordinates close as envelopes" (MEASURED text); §12.11.2 as the proof — record-carried to Ch. 12.
- L1747 "48.5 % density": cells whose 2S a k-electron subshell of capacity 4ℓ+2 can carry (2S ≡ k mod 2, 2S ≤ min(k, 4ℓ+2−k)) = 473 of 976 = 48.46 % (MEASURED; definition INFERRED from physics, match exact to rounding); 503 cells carry a 2S no k electrons can — "admits values no k electrons can carry" (MEASURED).
- L1765 every constraint xᵢ ≤ φ(xⱼ), φ non-decreasing, none a sum or difference: by inspection of the seven (MEASURED); sums fail closure 0 of 28 pairs (minmax.py, chat 66 instrument; MEASURED); Chapter 17 L4870–4880 carries the worked sum case g₁ + g₂ ≤ q and §17.2's "sums, products and differences do not" (MEASURED text).
- L1769, L1773 the constraint graph is a tree: 8 nodes, 7 edges, connected (MEASURED, r2-ch7.py); treewidth 1 follows (INFERRED, standard).
- L1780–1784 the closure proof: correct for joins as printed; for meets, (x∧y)ᵢ = min(xᵢ, yᵢ) ≤ φ(min(xⱼ, yⱼ)) holds by the same monotonicity with the roles exchanged — "Meets are symmetric" is right (INFERRED, checked).
- L1786 E(Λ) = 0 at four settings: see 7-02, reproduced.
- L1790–1791 counts change with caps, shape does not: Ch. 8 L1928 states the invariance under six settings — record-carried to Ch. 8.
- L1794 "checked at no fewer than four settings": consistent with L1786 (four) and Ch. 8 (six).
- Pointers: §12.11 → L2524, §7.4 → L1789, §12.11.3 → L3394, §12.11.2 → L3363, Ch. 17 → L4789, Ch. 8 → L1796, Figure 7.1 placed at L1771 — all resolve to headings carrying the cited matter (MEASURED, r2-tools.py pointers).

## C. Incidental

- Figure 7.1's file `figures/figure-7.1.png` is not a bundle member; existence at press is a production check (the constraint-graph figure exists in the project files as fig5_constraint_graphs.png).
- The global constants check (r2-tools.py constants, all six volumes): 976 at 175 sites, 1,654 at 42, 2,535 at 15, 13,585 at 12, 70,905 at 15, 199,130 at 30, 475,800 at 19; no off-by-one variant of any tower value anywhere; '975' at Register L1729, L3627 and IoI L1355 and '977' at Register L3635, L3885 are to be read in place in those volumes' segments.
