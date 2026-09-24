# SOURCES.md — provenance map for 02-lambda (not published)

Paper: `PAPER.md`, "The Lattice of Subshell Transitions" — **retitled in the 2026-09-24 repair pass from "The
Lattice of One-Electron Transitions"**, the title the draft and the audit carried (audit finding R-15: 481 of the
976 cells move two or three electrons, so "one-electron" was false of the cells; the old title is kept here for the
author, and the retitle is his to settle). Drafted 2026-09-21 in a run cut off by
a service limit (PAPER.md, check.py, figures.py, FIGURES.tsv and eight figures present, SOURCES.md
absent); resumed and finished 2026-09-24. The inherited `check.py` was read in full and run before
anything was changed: it was already green — 59 rows, 0 failures; with `--selftest` 65 rows, the six
negative controls all refuted, the sum-bound witness already pinned deterministically (the step the
earlier run recorded as in progress was complete). After the repair pass it discharges **77 rows, 0 failures** in
about 66 s (5 GUARD, 5 MACHINE-CHECKED, 54 EXHAUSTIVE, 4 SAMPLED, 9 CITED); `--selftest` adds six
negative controls, all refuted (83 rows). Every number in the paper is produced by that run or is a
bibliographic figure in the reference list. Z3 is the solver (`z3-solver`, Python 3.12 via
`method/bin`).

All line ranges below are in `method/members/`. `M` is `The_Method_1_6-2.md`, `C` is
`The_Method_1_6___Mathematical_Compendium-2.md`, `I` is `The_Method_1_6___The_Index_of_Indices-2.md`.

## What the finishing pass changed

**In `check.py`** (no existing check was weakened or altered in what it tests):

1. Every row label was renamed to the paper's own numbering. The inherited labels numbered the
   results differently from PAPER.md (its "Theorem 2, rank is modular" is the paper's Theorem 4,
   its "Lemma 6" the paper's Theorem 13, and so on throughout); the verification record must quote
   the check's labels exactly, so the labels now carry the paper's numbers.
2. Numbers the paper printed that no row produced were given rows: the 13,468 signature covers;
   370 cells in some minimum cover, the median 59 (0.24 %), the second-most-common 14,492 (58.9 %);
   the smallest witness set (4 cells); 976/7 = 139.4; the density 14.12 %; the skew −0.4334;
   log 2 = 0.6931 and log(11/10) = 0.0953; which bound has the lowest and highest containment rate.
3. New obligations, each behind a new or strengthened statement in the paper: E = 0 and the
   closed-form generator count at five further cap settings (Theorem 2, Theorem 6); the two
   certificates for order dimension 7, written out (Corollary 2); 1,113,045,672 maximal chains
   (Corollary 3); the orientation of the constraint graph has no directed cycle (Lemma 3, used by
   the corrected proof of Theorem 4); the 319-cell spin projection, k + 1 spins over each, defect 0
   (Lemma 4); 31,604 of 115,162 comparable intervals are boxes (Proposition 1); the Möbius function
   in coordinates and against the arithmetic Möbius function (Corollary 6); a three-element local
   account of the cell common to all minimum seeds (Theorem 18); what every minimum seed contains
   (Corollary 7); all 976 single-cell deletions closing back to Λ (Corollary 8).
4. Two CITED rows added (Fulkerson 1956; Stanley 2012). The word "seated" was removed from row
   details, since the record quotes them and the guard forbids it.

**In `PAPER.md`:**

- **Two proofs were incomplete and are rewritten.** Theorem 4's grading step said "any coordinate in
  which they differ can be lowered one step"; that is false for sublattices of a box in general
  (the chain {(0,0), (1,1)} is a sublattice in which a cover has rank distance 2) and needs the
  shape of the bounds: the proof now lowers a differing coordinate that bounds no other differing
  coordinate, which exists because the oriented constraint graph has no directed cycle (Lemma 3,
  moved into §1 and given that clause). Theorem 6's converse argued "contradicting minimality" in a
  circle; it now proves j = min{x : x_c ≥ j_c} through the unique lower cover, and proves m_c = v
  and the injectivity of (c, v) ↦ j(c, v), both of which the closed count needs.
- §0 named the machine-checked and exhaustive results by numbers that did not match the paper's
  own (a leftover of the check's old numbering); corrected. §0 called the seed "a measured
  minimum"; it is exact by exhaustive branch and bound, and now says so. §8 claimed "defect zero at
  four cap settings" with no check behind it; the settings are now recovered, checked and named.
- The Chvátal (1979) citation was misattached: it was cited for the rule "a set that uniquely covers
  an element is in every minimum cover", which is not what that paper is. It is now cited, with
  Johnson (1974), for the greedy heuristic, which certifies an upper bound only.
- Corollaries 3–8 are new (see item 3 above). The former Corollaries 3 and 4 are now 4 and 5.
- References: Carathéodory (1911) removed (nothing in the paper uses it — the Carathéodory bound
  is the companion paper's subject and is refuted there); Fulkerson (1956) and Monjardet (1981)
  added; Birkhoff (1940), Edelman–Jamison (1985), Johnson (1974), Lauritzen (1996), Moore (1910),
  Sperner (1928), Stanley (2012) and de Moura–Bjørner (2008) were listed but uncited and are now
  cited where used.

## What the repair pass changed (2026-09-24, against AUDIT.md)

The dispositions are in `AUDIT.md` Part C and its repair record; this section records what moved and
where each new number comes from.

**In `check.py`** (no check weakened; every change adds an assertion or a printed value):

1. **Covers from the order alone** (A-1). `covers_of()` no longer tests y − eᵢ ∈ Λ; it computes, for
   every pair, x < y with no cell strictly between, by bitset, and the row "Theorem 4, Λ is graded" now
   asserts 3,749 covers, every one a unit step and every one raising rank by 1. The rows for Theorem 6
   and Corollary 3 inherit the order-derived cover sets. At the five further cap settings the
   join-irreducible count still takes lower covers as unit steps, which Theorem 4 (proved for every cap)
   licenses; the row says so.
2. **Three new rows for the physics** (R-15, R-16, R-17): "D1, electrons moved" (q = 0/1/2/3: 165, 330,
   345, 136; 481 move two or three); "D1, the model of a cell" (g = q in 461, g < q in 515, g = 0 in 485,
   source = target in 200); "Table 1, the spin envelope" (503 cells whose 2S no k-electron configuration
   carries: 413 parity, 180 particle–hole, 90 both; 473 physical = 48.5 %, which is the main volume's own
   "48.5 % density" for the envelope at M §7 1751). The spin rule used is 2S ≡ k (mod 2) and
   2S ≤ min(k, 4ℓ + 2 − k), the particle–hole conjugation M §12.11.2 3368–3398 names.
3. **Six rows that printed and asserted nothing now pin their values** (A-3): Table 3's ranks and
   weights, the twenty implications as a set, the bit accounting, the log chain, the void-free fraction
   with its rates, product and lift, and the covers-by-cell median 59 and second 14,492. Table 2's row
   pins all eight marginals.
4. **Numbers the paper printed with no row now have one** (A-4): the extended box for the floor, the
   87.7 % / 1.6 % shares of the heaviest and lightest letter, and the SAMPLED family 976³ = 929,714,176
   ordered triples. **The draft's 8,064 for the box extended to k = 0 did not reproduce: the box has
   9,216 points** (3·2·4·4·3·2·4·4); the paper now prints 9,216 and the row asserts it. 8,064 was the
   inherited draft's figure, and no source passage states either number — it was arithmetic the draft
   got wrong and nothing pinned.
5. The Theorem 17 SAMPLED row prints how many of its 80 subsets are covers (0), so the paper can say
   which direction it tests (A-5); Corollary 7's row carries q = k = 1, 2, 3 as three properties and pins
   s → s at 17,403 of 24,585 (A-6); the Theorem 1 label reads 21 variables (A-2); CITED rows carry name
   and year, Karp's reads NP-hard with the decision version NP-complete (R-27), and two are added —
   Birkhoff 1940 / Davey–Priestley 2002 for "a sublattice of a distributive lattice is distributive" and
   the rank-modularity characterisation of modular lattices (R-1), and Stanley 1989 for log-concave ⟹
   unimodal (R-13).

**In `PAPER.md`:**

- Title, thesis and abstract: "subshell transitions"; the thesis attaches "every such set" to the seeds
  (R-26); the abstract states the cell model, that six bounds are exact and the seventh an envelope, and
  that no selection rule or spectral datum enters (R-21).
- §0: the "nothing chosen for convenience" sentence is replaced by the exact/envelope statement with the
  503 count; a paragraph says which headline results are inherited from "sublattice of a product of
  chains" and which are new (R-23); the counts by q are stated (R-15); the cap-free list is corrected
  (R-3); "Counted" replaces "Measured" (A-14); NP-hard (R-27).
- §1: the physics paragraph is rewritten (R-16 to R-21): Schrödinger 1926 for ℓ ≤ n − 1 with Bohr kept
  for n; spin addition rather than Hund (Hund 1925 dropped from the references, now uncited); "spin
  label 2S (multiplicity 2S + 1)"; the exact spin rule and why it is not imposed; g as the number
  placed with the target taken to begin empty — which is the mathematical compendium's own statement
  at C 1294 ("g ≤ q reads g as electrons placed by this transition; g ≤ 2(2f+1) reads it as electrons
  present … they coincide exactly when the target subshell begins empty") and the main volume's
  "removed but not placed" at M 2893. D1 states the model and what g < q, q = 0 and source = target
  cells are. Table 1 gains a "kind" column and moves to follow D2. D3 states the general alphabets
  (R-8). D7 cites the companion paper by title and Baker–Pixley / Bergman (R-22, R-24).
- §2: R-1 corrected (rank modularity is modularity's signature; M₃); Sperner defined in D8 and the
  product-of-chains remark added (R-13, R-24); Theorem 6's injectivity line supplied (R-4); "density"
  for the bit fraction (R-28); Trotter cited (R-24).
- §3: "interval metric / measure" throughout (R-28); "d as defined in D10 equals (2)" (R-12); D11's
  quantity is the size, the number of points (A-11).
- §4: Theorem 12 is stated as the nested formula with its two closed leaves, and the g-first aside is
  replaced by the sentence that the single-argument property belongs to a leaf order (R-2, R-10); the
  Chebyshev sentence is replaced by a reading marked heuristic (R-9).
- §5: the Theorem 14 display is a display block with Unicode superscripts throughout, the one
  superscript Unicode lacks (q) set as an HTML superscript, one sum per line (A-8); Theorem 15 says "at
  the caps of D3"; Corollary 5 (R-7).
- §6: 𝒪(Q) for down-sets (R-5); the crosscut corollary cited precisely and the closed form noted as
  textbook (R-14); fifteen comparisons (R-6).
- §7: Theorem 17 stated for any setting with E = 0 and its SAMPLED clause names both directions
  (R-3, A-5); "NP-hard" (R-27); "the disjoint-witness bound certifies 5" (R-11); Corollary 7's status
  names q = k at each k (A-6).
- §8 and References: Lach 2026, *The Closure Law of a Finite Index*, this collection (R-22); nine
  references added (R-24), Garey–Johnson and Hardy–Littlewood–Pólya declined as optional.
- §9: rebuilt from the 77-row run; the families paragraph adds 9,216 and 929,714,176; the
  not-machine-checked paragraph says how the grading is tested at the base caps and licensed at the
  further ones.
- Typography: figures stay in PAPER-SPEC.md §9's form (empty alt text, caption paragraph beginning
  **Figure n.** under the image) and table headings as bold paragraphs; page-foot splits were removed
  by placement — Table 1 follows D2, Figure 1 precedes Lemma 3, Figure 4 precedes Theorem 11 (A-12).
  An interim pandoc-figure/alt-text form was reverted on the coordinator's ruling. The file names in
  `figures/` match the figure numbers (A-13).

**Figures.** `fig5-caterpillar.png`, the archival plate `restore-point-2-13/figures/fig07.png`, is
replaced by a computed `fig7-caterpillar.png` drawn by `figures.py` from `check.py`'s CONSTRAINTS: the
plate's arrows ran n→ℓ→k→q→g→f→e, which is neither the nesting order of Theorem 14 nor the direction of
bounding, and its leaf label misprinted a subscript (A-9). The four remaining archival plates are
unchanged in bytes; the files are renamed so that `figN` is Figure N (A-13), and Figure 4's caption
notes that the plate's own title says "occupancy measure" for the d the paper now calls the interval
measure (A-11, R-28).

## Where each section draws from

| paper section | source passages |
|---|---|
| Thesis, Abstract, §0 | M §7 1729–1800 (the eight coordinates, the seven constraints and four origins, "every constraint is of one form", the closure proof §7.3, the cap convention §7.4); M §8 1801–1816 (the standing caps (3,3,1,3,1)); I §I 11–38 (the constraint table with k ≥ 1 as definitional, the one coupling, 976 → 1,000 and the 24 lost) |
| §1 physics paragraph, D1–D4, Table 1 | M §7.1 1755–1768 (constraint → origin table); M §7 1745–1753 ("vector coupling yields an envelope: 2S ≤ k contains every physical multiplicity and admits values no k electrons can carry, at 48.5 % density"); M §12.11.2–12.11.3 3368–3413 (the exact coupling bound needs a congruence or two parents; particle–hole conjugation; "counting coordinates close exactly, coupling coordinates close as envelopes"); C §IV.L 1092–1170 (each bound's prior art: Bohr 1913 and Schrödinger 1926 for ℓ ≤ n − 1, Stoner 1924, Pauli 1925, Hund 1925 for the spin bound — the paper cites spin addition and Condon–Shortley instead, R-20; q ≤ k and g ≤ q definitional; k ≥ 1 the occupancy floor, M §10.2 2043–2050 and register 301); C §IV.L 1294 (g as electrons placed, the target taken to begin empty, no coordinate for prior occupancy); M §12.11.0.8 2885–2895 ("something not removed and something removed but not placed"); C §IV.L 1462–1470 ("The definition of Λ") |
| §1 D5–D7, Theorem 1, Lemma 1 | M §7.3 1781–1793 (the closure proof, "meets are symmetric"); C §IV.L 1432–1440 ("Sublattice of a product", both branches of both operations written out); M §7.2 1769–1779 (a sum could not appear; Chapter 17) — the paper's negative control replaces the source's 89,864 sampled join failures with a solver witness |
| §1 Lemma 2 | M §14.1 3687–3715 (X closed ⟺ X = ℛ(X); Bergman / Baker–Pixley named); `research/warp-drive/prover.py` (the subset-quantified harness, imported by path); the direction proved here is fixed point ⟹ sublattice, the converse being the companion paper's Theorem 2 |
| §1 Theorem 2 | M §7.3 1791–1792 ("E(Λ) = 0, verified by direct computation at four cap settings — 216, 976, 1,636 and 2,394 cells"); C §IV.L 990–998 ("The closure theorem", verified at four settings); I 1355–1362 ("976 rows. F(1) = 976, F(−1) = 2, E = 0, density 0.1412 of a box of 6,912"); I 377–1360, the Λ₈ table, read by `check.py` and compared in both directions with the rebuilt set |
| §1 Table 2, Corollary 1 | C §IV.L 1181–1202 ("The most active constraint is the coupling itself": 673, 575, 564, 308, 300, 200, 25, 24); M §11.5 2236–2247 (remove the coupling and 976 becomes 1,000; the 24 have f = 0, g = 3); M §10.2 2043–2050 (k ≥ 1; the 25 cells at k = 0) |
| §1 Lemma 3, Figure 1 | M §8.5 1906–1918 (the tree, treewidth 1); M §11.4 2231–2235 (a caterpillar); C §IV.L 1642–1650 ("The constraint tree"); M Figure 7.1 1776–1779 |
| §2 Theorem 3 | M §8.1 1818–1823 (4,000 sampled triples); C §IV.L 1482–1490 ("Birkhoff / product of chains": the chain identity checked by the three orderings, "the forcing is the embedding, not a census") |
| §2 Theorem 4 | M §8.2 1824–1851 (rank conserved, 475,800 pairs, modular with equality, the cheaper test); C §IV.L 1522–1530 ("Modularity (equality, not submodularity)"); the grading itself is asserted nowhere in the source and is proved here |
| §2 Theorem 5, Figure 2 | M §8.4 1878–1905 (Sperner by Dilworth and bipartite matching, 122 at rank 11, log-concave, skew −0.43, not rank-symmetric); C §IV.L 1602–1610 ("The Sperner property": the rank sequence in full, the 122-chain Dilworth partition, Stanley 1980 on Peck posets); C §IV.L 1592–1600 (the skew) |
| §2 Theorem 6, Table 3 | M §8.3 1852–1877 (17 join-irreducibles, 20 covers); M Appendix A.19 and A.19.0 10140–10180 (the seventeen written out by rank; "every generator is the least cell with one coordinate at one value", Σᵢ(\|Aᵢ\| − 1) = 17, the letter/rank/weight/forces table); C §IV.L 1032–1040 ("The join-irreducible count"); the claim that every join-irreducible has that form is stated in the source without proof and is proved here |
| §2 Theorem 7, Theorem 8, Figure 3 | M §11.1.1 2099–2178 (binary: 976 of 131,072 words, join OR, meet AND, 17 bits, 9.93, 7.07 surplus, 0.7446 %; the twenty implications cut the space exactly); M A.19.0 10170–10180 (nine within, eleven between, listed); C §IV.L 1062–1080 ("The Birkhoff representation", "The Boolean representation"), 1422–1430 ("The implication circuit") |
| §2 Corollary 2 | M §8.6 1919–1940 (order dimension 7, corrected from 8 — register 409; width of J(Λ), the two certificates, g rides on q); C §IV.L 1472–1480 (the antichain of seven written out) |
| §2 Corollary 3 | C §IV.L 1222–1243 ("Every other shape the lattice contains": e(P) = 1,113,045,672 maximal chains; boxes 31,604 of 115,162; the two seventeens are one) |
| §2 Theorem 9 | M §8.4 1892–1899 (8 of 976 survive x ↦ max − x; the competing 112 under a different map); M A.19.1 10182–10192 (the eight written out, q = k, g = q, 2S = q); M §11.8.1 2287–2307 (no fixed point, the eight all of even rank) |
| §3 D9, D10, Theorems 10 and 11, Figure 4 | M §9 1941–1962 (the prime encoding, rank = Ω(N)); M §9.2 1963–2016 (d = τ(lcm/gcd), d(x,x) = 1, the five forms, the multiplicative triangle, log d an ℓ¹ metric, hyperbolic balls, first step log 2, tenth log(11/10)); C §IV.L 1502–1510 ("The lattice metric", Monjardet 1981), 1532–1540 ("The interval measure" — the name the paper now uses for d, R-28) |
| §4 D11, Theorem 12, Theorem 13, Proposition 1, Figure 5 | M §10 2026–2079 (the void; 10.3 containment in seven comparisons; 10.4 the count with no sieve, the two leaves in closed form); M Appendix A.10 10021–10035 (the tree factorisation proved); C §IV.L 1082–1104 ("The box factorises": the elimination argument, Freuder for width 1 ⟺ forest, the witness on a closed triangle); C §IV.L 1662–1671 ("The void-free fraction": rates 69.95–98.06 %, product 20.13 %, joint 28.35 %, lift 1.4081 at the base caps; Chebyshev's sum inequality for the sign of the dependence) |
| §5 D12, Theorem 14, Corollary 4, Lemma 4, Theorem 15, Corollary 5, Figures 6 and 7 | M §11.1 2084–2098 and §11.3 2216–2230 (the single expression; F(1) = 976, F′(1)/F(1) = 11.0666, F(−1) = 2); M §11.6 2248–2255 (the detachable factor; 319 cells with 2S removed, E = 0, every seven-cell carries k + 1 spins); M §11.7 2256–2279 (why a closed expression exists: monotone, two-variable, acyclic); M §11.8 2280–2286 and §11.8.1 2287–2307 (not palindromic, 5 against 4; F(−1) = 2 has a cause); C §IV.L 1000–1030, 1552–1560, 1572–1580, 1612–1620 |
| §6 D13, Theorem 16, Corollary 6 | M §9.3 2017–2025 (μ in closed form; the transfer condition to μ_arith); M Appendix A.9 10009–10020 (the proof via Birkhoff and Rota's crosscut theorem); C §IV.L 1512–1520 ("Möbius function of a distributive lattice", the transfer condition and "decidable in seven comparisons") |
| §7 D14, Theorems 17 and 18, Corollaries 7 and 8, Figure 8 | M §14.5.1 3768–3802 (no cell removable; "Λ is the closure of SEVEN of its cells — 139 to 1"; greedy 12, 11, 12 superseded); M §14.5.9 3922–3963 (the set-cover reading; seed(Λ₈) = 7 exact by branch and bound, LB 5, five heuristics 12/7/7/7/40); M §14.5.10–§14.5.14 3964–4080 (the four-cell "core" of 140 greedy and 219 randomised covers, the six channel conditions, the fifth position, the binary reading — all superseded by the exact enumeration, see below); C §IV.S 598–606 (the generation criterion), 660–668 (the envelope-step law; s → s in 71 % of the 24,585 exact covers), 670–678 (the forced set, corrected: 24,585 covers, one common cell (2,1,3,3,2,1,3,0)), 680–688 (the seed is a set cover), 722–730 (Λ's seed — seven cells), 782–790 ("A seed"), 804–822 (the unit template corrected; non-uniqueness as a Krein–Milman failure, Edelman–Jamison) |
| §8 | M §11.7 2256–2279 (the three shape facts); M §7.1 1765–1768 ("attributed to indexing rather than to physics") |
| not used | M D.4.2–D.4.4 10414–10495 (the recovered bound system of 56 envelopes, the pointwise minimum, the tie at every cell, the one-way map from presentations to Λ) — read; it concerns the operator's normal form, which is the companion paper's §4, and nothing here depends on it |

## Interpretations chosen, and why

1. **Own-box regime.** ℛ(X) is computed inside the box X itself realises (D7), as the source does
   (M §6.1) and as the companion paper's §1 states. `tools/cypher.py`'s `op_order` rebuilds the
   alphabets from the cells, so the operator under test is in that regime by construction.
2. **The caps are part of every count.** The source's convention (M §8, "a cap-dependent figure
   without a stated cap is at these caps") is made explicit in D3, and §0 says which statements are
   cap-free (the machine-checked and proved ones) and which are counts.
3. **The seed's minimality is exact, not measured.** The source reports seven both as "exact by
   branch and bound" and, in older passages, as a heuristic figure; the paper's Theorem 18 proves
   the search complete (branching on an uncovered element, pruning by a disjoint-witness bound) and
   runs every limit 1–7. The inherited §0 called it "a measured minimum"; corrected.
4. **Theorem 17 is stated for Λ and proved from Theorem 2**, not imported from the companion paper's
   Theorems 12–13; the two agree in content and the proofs are independent.
5. **"Four cap settings" recovered.** The source names the four cell counts and not the caps. A
   sweep over caps finds 1,636 and 2,394 at exactly one setting each — (3,3,1,4,1) and (4,3,1,4,1) —
   and 216 at 142 settings, of which (2,2,1,2,1), every cap lowered by one, is the natural reading
   and is the one used. Two further settings from C §IV.L 1077 ((4,4,2,4,1) and (4,4,2,6,2)) were
   added for the generator count.
6. **Subscripts.** The source's leaf formulas use 0-based subscripts (hi₇ for 2S, hi₆ for g); the
   paper indexes coordinates 1–8, so they read hi₈ and hi₇.

## Reproduction — what reproduces, what does not, and what was not printed

**Reproduced exactly** (source figure = measured): 976 cells, 6,912 box, 14.12 %; E = 0 and
idempotence; 475,800 pairs modular; 122 at rank 11 and the full rank sequence; 11.0666 and skew
−0.43; 17 join-irreducibles, 20 covers, 9 within and 11 between, the seventeen cells, their ranks,
weights and implications (M A.19.0 table, cell for cell); 976 of 131,072 words, 9.93 bits, 7.07
surplus, 0.7446 %; order dimension 7 with the source's antichain; e(P) = 1,113,045,672; 31,604 of
115,162 comparable intervals are boxes (27.4 %); the eight reflection survivors and no fixed point;
the five forms of d, d(x,x) = 1; 673/575/564/308/300/200/25/24 marginal exclusions; 1,000 and the 24
lost at f = 0, g = 3; the leaf formulas; F(1) = 976, F(−1) = 2, the split by k (0, +2, 0), F_box(−1)
= 0; 319 seven-cells at E = 0 with k + 1 spins; μ ∈ {−1, 0, +1} in closed form; seed 7, LB 5, 102
elements (25 slots + 77 steps), 24,585 minimum covers, one common cell (2,1,3,3,2,1,3,0), no element
uniquely covered; every cell implied by the other 975; s → s in 71 % of covers (17,403/24,585 =
70.8 %); void-free 28.35 %, rates 69.95–98.06 %, product 20.13 %, lift 1.4081 (C §IV.L 1662 at the
base caps).

**Source claims that do NOT reproduce, or reproduce differently** (the paper prints the measured
value; none of these was repaired in the source):

1. *Generator counts across cap settings.* M §8.3 1867 says the count grows "17, 23, 31, 32"
   across settings; C §IV.L 1077 says "17, 24, 33, 35" at (3,3,1,3,1), (4,4,2,4,1), (4,4,2,6,2),
   (5,5,2,6,2). Measured at the first three: **17, 24, 33** — the compendium's figures, not the
   main volume's. The fourth setting was not run (19,109 cells at the third already; the closure
   there is the slow step). The paper prints the measured three.
2. *Why F(−1) ≠ 0.* M §11.8.1 and C §IV.L 1022 attribute F_box(−1) = 0 to "ℓ and f each have
   exactly two [values]", listing four factors. Measured: **five** of the eight alphabets have even
   size (ℓ, f, and q, g, 2S with four values each). The conclusion F_box(−1) = 0 is unaffected — one
   vanishing factor suffices — but the paper's Theorem 15 states the five.
3. *The Möbius transfer condition.* M §9.3 and C §IV.L 1512 state "μ_Λ = μ_arith iff the interval
   is a void-free unit hypercube", tested on 60 + 56 pairs. Measured over all 116,138 comparable
   pairs: the two functions **agree on 99,034 and differ on 17,104**, and every disagreement is a
   unit hypercube with a void — so the biconditional is correct among unit hypercubes and false as
   stated, since on a non-unit interval both functions vanish and agree. Corollary 6 states the
   precise form: μ ≠ 0 exactly on the 19,079 void-free unit hypercubes.
4. *"18 join-irreducibles and 18 meet-irreducibles"* (C §IV.L 1562, "Join-prime and meet-prime").
   Measured 17 and 17 (Theorem 6). Not printed; the entry's "step(Λ₈) = 4" and the interval-removal
   criterion were not examined.
5. *"forced by Chvátal's reduction"* (C §IV.S 670). The reduction in question fires when an
   element is covered by exactly one set; the same entry records zero such elements, and the
   measurement confirms it (smallest witness set: 4). The cell is in every minimum cover, but not by
   that rule. The paper says so and gives the three-element local account instead.
6. *The void-free fraction over "776 million pairs", 27.7–30.1 %, joint 30.13 % against product
   20.19 %, factor 1.49* (M §10.2). Those are at a cap family the source does not name (C §IV.L 1662
   says the same) and are not reproduced; the base-cap figures 0.2835 / 0.2013 / 1.4081 are, and
   are what the paper prints. C §IV.L 1662's factorisation of the lift as a product of six edge
   lifts (1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022) was **not attempted** and is not
   printed; Proposition 1 measures the lift and does not decompose it.
7. *The sampled verifications* — distributivity on 4,000 triples, the five forms on 500 and 2,000
   pairs, the triangle on 4,000, μ on 47 pairs, containment on 3,168 pairs, the factorisation on
   eight random intervals, Sperner at five cap settings — are replaced by exhaustive families (289
   coordinate triples plus a 200,000-triple sampled transcription check; 475,800 pairs; 116,138
   pairs; 1,944,000 boxes). Sperner is measured at the base caps only.
8. *The 140-greedy / 219-randomised "stable core of four"* (M §14.5.10–§14.5.14) and everything
   built on it — the four corners, the six channel conditions as a sample statement, the fifth
   position (3,0,1,1,*,0,1,1), the binary complement pairing — is superseded by the exact
   enumeration inside the source itself (C §IV.S 618, 670, 804: corner 4 in 14 %, the unit template
   in 10 % of the 24,585). The paper prints only what the exact enumeration gives; the 14 % and
   10 % figures were not re-measured and are not printed. What survives of the six channel
   conditions is proved as Corollary 7 (five forced by the covering criterion, s → s not).
9. *The competing reflection count 112* under x ↦ max + min − x (M §8.4): a different map; noted,
   not measured, not printed.
10. *M §14.5.1's greedy-removal figures 12, 11, 12 and "at most ten"* are heuristics the source
    itself retracts at §14.5.9; not printed.
11. *"a depth of five"* for the implication circuit (M §11.1.1) and the three depth readings
    (C §IV.L 1422) — not printed.
12. *"976 = 8 × 122"* and "fifty-seven-fold compression" (976/17) — arithmetic coincidences, not
    printed.

**Corrections already in the record that the paper carries.** Order dimension 7, not 8 (M §8.6,
register 409). seed(Λ) = 7, not 10–13 (M §14.5.9, registers 503–506). The four-corner universality
withdrawn (C §IV.S 670). The Freuder mis-citation (M §14.1, register 400): the paper cites Freuder
1982 only for "a constraint graph has width 1 iff it is a forest", which that paper does state, and
never for global consistency.

**Consistency with the companion closure-law paper** (*The Closure Law of a Finite Index*, Lach 2026, now in the References as R-22 required). seed(Λ) = 7 exact — agreed. The general box
seed law d + c − 2 is refuted there from d = 5; this paper never states it and says nothing about
seeds of boxes. Definitions D7 and D14 here agree with that paper's D5 and D8, and its Theorems 12
and 13 with this paper's Theorem 17.

## Figures

Four plates are archival copies from the mirror's extracted figure archives, copied byte-for-byte by
`figures.py` with md5 recorded in `FIGURES.tsv` (fig1 and fig2 from
`extracted/archives/the-method-1-6-figures-build8/`, fig4 and fig6 from
`extracted/archives/restore-point-2-13/`); each was read against its caption and against the check's
numbers (fig1 labels the bounds as 2(2ℓ+1) and 2(2f+1), the paper's 4ℓ+2 and 4f+2 — the same
bounds, and the caption now says so). Four are computed by `figures.py` from `check.py`'s own
functions: fig3 (the generating poset), fig5 (the void), fig7 (the caterpillar in Theorem 14's nesting
order, replacing the archival fig07 plate — see the repair section above) and fig8 (the seed). File
numbers match figure numbers. `method/PROOF-FIGURES.tsv` was consulted by the earlier
run; the archival plates are the ones it matched.

## What the check does not cover

The Sperner property, the Möbius function, the seed and every count are at the base caps only,
except where Theorem 2 names further settings. The completeness of the branch-and-bound is argued in
Theorem 18's proof and not certified by an external tool. Theorem 16's cited steps (Birkhoff, Rota)
are not machine-checked. Distributivity on cell triples and the multiplicative triangle on cell
triples are SAMPLED transcription checks of proved statements.
