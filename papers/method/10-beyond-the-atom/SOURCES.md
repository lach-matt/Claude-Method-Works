# SOURCES.md — provenance map for 10-beyond-the-atom (not published)

Paper: `PAPER.md`, "Closure beyond the atom: the defect of other indexes, redundancy, and the
electromagnetic quotient". Drafted 2026-09-21 (resumed run). Every number in the paper is produced
by `check.py` — 95 obligations in the plain run, 99 with `--selftest`, all passing — or is CITED.

Run: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH; python3 check.py --selftest`
→ `99 obligations, 0 failed` (MACHINE-CHECKED 8, EXHAUSTIVE 71, SAMPLED 9, REFUTATION 6, GUARD 5).
The plain run is 95 (REFUTATION 2).

Instruments imported by path, never copied: `research/warp-drive/prover.py` (the Z3 harness and its
`cells_of` / `meet` / `join` / `in_R` / `subset_vars` / `contains` / `prove` / `non_vacuous`);
`tools/cypher.py` (`op_order` — the closure operator under test — and the four other language
operators, plus its index builders `_lambda`, `_periodic`, `_nuclide`, `_kreuzer_skarke`,
`_box_ordering`, `_tower` and `_ELEMENT`); `method/members/tower-2.py` (Λ₈…Λ₁₀);
`extracted/archives/restore-point-2-13/close_L118.py` (the 118 observed ground configurations, used
only for the crossing population). Data read, not copied:
`extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv` and
`extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv`.

Reference implementations written fresh here, as the independent side of the encoding guard:
`R_ref` (the staircase written from D3/D4 alone), `hull` (the sublattice hull), `envelopes` and
`coupling`. The object under test is always the seated operator.

---

## 1. The obligation that failed on the previous run, and its disposition

```
[FAIL] Q5c EXHAUSTIVE  a witness pair in the parity set whose join leaves it: dl of the pair and of
                       the join: (1, -1, 0, False) != expected (-1, 1, 0, False)
```

**Disposition: a bug in the check's fixture, fixed in the fixture. The measurement was not touched.**

The witness the run produced *is* a witness, and this was checked rather than assumed before the
fixture was changed. The pair the exhaustive search reaches first is

    a = (1, 0, 1, 0, 2, 1, 0, 0, 0)   Δℓ = f − ℓ = 1 − 0 = +1
    b = (2, 1, 1, 0, 1, 0, 0, 0, 0)   Δℓ = 0 − 1 = −1

both with |Δℓ| = 1, so both lie in the parity set; their coordinatewise join is
`(2, 1, 1, 0, 2, 1, 0, 0, 0)` with Δℓ = 1 − 1 = 0, which fails |Δℓ| = 1 and so leaves the set. All
four properties that make it a witness hold: both members in the set, the join equal to the
componentwise maximum, Δℓ of the join equal to 0, the join outside the set. The fixture had written
the two members' Δℓ values in the order (−1, +1) while `itertools.combinations` over the parity set
reaches (+1, −1) first — an ordering of two components of the *same* witness, and nothing else. Which
member the enumeration reaches first is not part of the claim.

The fixture now compares the two Δℓ values as an **unordered pair** (`sorted(...) == [-1, 1]`) and
additionally asserts that both members lie in the set and that the join does not; a new row `Q5d`
prints the two cells and their join and re-verifies that the join is the componentwise maximum and
is outside the set. Nothing about how the witness is found was altered, and no tolerance was widened.
This is Refutation 3 of the paper, and the paper prints the witness cells.

---

## 2. Where each section draws from

| paper section | source passages (all under `method/members/`) |
|---|---|
| Thesis, §0 | Index of Indices 61–88 (the five drawn-beside indexes with coordinates / cells / box / E, and "E = 0 carries information only when the ambient box exceeds the cells"); 158–372 (the EM quotient, the time index, the nucleon index, the Kreuzer–Skarke frontier, the string partition function, the languages, redundancy); The_Method_1_6-2.md §6 1516–1729 and §31 8614–8795 |
| §1 D1–D4 (index, box, envelope, closure, defect) | The_Method_1_6-2.md 1546–1556 ("The reconstruction is mechanical … Âᵢ(X), φ̂ᵢⱼ(v) = max{xᵢ : x ∈ X, xⱼ ≤ v}, ℛ(X) = {x ∈ ∏Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j}, E(X) = |ℛ(X)| − |X|"); `docs/CYPHER.md` operator table (order, `PINNED`, §32.4.1; matches the seated `rclose.py`); `tools/cypher.py` `op_order` |
| §1 D5, §2.2 Corollary, §2.2 Theorem 4 / Corollary 2 | The_Method_1_6-2.md Appendix D.1 10363–10375 ("ℛ recovers MONOTONE bounds. It applies to ORDERED coordinates only… The repair is the shape Λ already has: fibre over the categorical axes"); D.5.5 10696–10735 (the fibration table 16/7/6/1 fibres against E 0/2/3/4; "E falls as the fibration is refined, and reaches zero by refinement alone… E = 0 is not a claim about a set; it is a claim about a set relative to a stated fibration, and the coarser the fibration the stronger the claim") |
| §1 D6, D7, §4 | Index of Indices 310–340 ("Remove cells at random and ask whether ℛ puts them back"; the six-row table Λ 8/56/29%/61%, Λ_spectra^obs 3/6/17%/20%, box ordering 3/6/50%/0%, Janet 2/2/50%/0%, periodic table and calendar 2/2/0%/0%; "r² = 0.002, p = 0.94"; the projection ladder 61/30/30/30/5/0; "only INDEPENDENT coordinates count"; Nₑ = Z − c + 1 taking 20% → 0% while doubling the envelopes and raising coupling 17% → 33%) |
| §2.1 Theorem 1, Lemma 2, Theorem 2 | The_Method_1_6-2.md §6.2 1650–1656 ("ℛ is idempotent — §32.4.1 proves it — so ℛ(X) satisfies ℛℛ(X) = ℛ(X) for any X whatever. A band's closure is a theorem, not a finding"); `docs/CYPHER.md` (Moore 1910). The proofs in §2 are written out here from D3/D4 and are not taken from a source |
| §2.3 Theorems 5, 6, Corollary 3, Refutations 1–2 | Index of Indices 1467–1475 ("That a selection rule is a QUOTIENT and not an extension… It is the only index here that demonstrates the difference between adding a coordinate and dividing by one"); Mathematical Compendium §IV.EM 2630–2640 ("the EM index is a QUOTIENT of Λ, not an extension"). The lattice statement, its criterion and the two counterexamples are this paper's |
| §3.1 Λ and the tower | The_Method_1_6-2.md §7.1 (the eight inequalities); Index of Indices 1414–1430 ("Eight integer coordinates (n, ℓ, k, q, e, f, g, 2S) under eight inequalities, 976 cells, E = 0"; "Λ assembles them; it introduces none" — Bohr 1913, Schrödinger 1926, Stoner 1924, Pauli 1925, Hund 1925) and 1432–1440 (the tower, cell counts 976, 1654, 2535, E = 0 at every stage); `method/members/tower-2.py` |
| §3.2 the two tables | The_Method_1_6-2.md §6 1516–1545 (90 / 126 / 36 and the 36 named); §6.1.1 1560–1600 (helium at 18 → 36, at 2 → 20; "the entire first row of gaps exists only under the standard placement"); Index of Indices 1360–1380 and 1442–1456 (Janet 118 / 944 / 0; Janet 1928/1929; the Löwdin challenge left open) |
| §3.3 calendar, box, chessboard | The_Method_1_6-2.md §6.3 1700–1712 (the seven named; the relabel-by-length repair; "E(X) = 7 is the price of keeping January first"); Index of Indices 1398–1410, 1458–1466 ("the floor and the ceiling") |
| §3.4 the nuclide chart | The_Method_1_6-2.md §6.2 1660–1676 and §6.2.1 1678–1699 (E = 9, the nine named, four cutoffs, "the drawn chart is the closure of the real one"); Index of Indices 236–244; Mathematical Compendium §IV.E 1860–1872, which carries the AME2020 re-measurement (E = 2, the two cells (0,0) and the diproton) |
| §3.5 Kreuzer–Skarke | The_Method_1_6-2.md §31.3 8730–8795 (the χ = ±6 slice, 208 cells, E = 540, 498 + 498 of 21,528, the five χ values, 112 diagonal, 26–262, the four falsification tests, "the index proposes; it is not thereby right"); Index of Indices 246–256 |
| §3.6 the string partition function | The_Method_1_6-2.md §31.2.3 8700–8706; Index of Indices 258–266 (∏(1 − qⁿ)⁻²⁴, d(1) = 24, d(2) = 324, d(3) = 3,200, d(14) = 156,883,829,400; "a product closes trivially: ℛ adds nothing, so E = 0… the degenerate case of the three closure conditions where independence stands in for the tree") |
| §3.7 the survey grid | Index of Indices 340–372 (Λ_spectra^obs, coordinates Z · core charge · ℓ; "All three grids are closed — each is a fixed point of ℛ… The number beside each is what has not been measured under that cap… it is never a closure defect"); `extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv` |
| §3.9 bit cost | this paper's own construction; no source figure |
| §5 the electromagnetic quotient | Index of Indices 165–180 (the quotient, "Its E = 0 is VACUOUS… It closes because it is a box, not because the selection rules constrain it"; the crossing 11.6 / 40.7 / 89.7 / 77.9); Mathematical Compendium §IV.EM 2570–2672 (the complete rectangle; the multipole map Δℓ → M1/E1/E2/E3 with 814 and 840 on the base build; "composability and the EM condition share 0.0004 bits of a possible 0.633"; "|Δℓ| = 1 is δ⁻¹({−1,+1}), a hole at zero, not convex; E = 750"; "ΔS = 0 is a diagonal… imposing it preserves E = 0"; the 576 intercombination lines and the jK-versus-LS reading); Laporte 1924, Russell & Saunders 1925, Wigner 1927 as the compendium's prior art |
| §6 the languages | The_Method_1_6-2.md §33 9405–9500 (the six languages and the question each asks; "a language that falls silent is the finding"); Index of Indices 268–284 (the operator table; "Six agree on Λ at 976 and all ten pairs hold — C(5,2), a complete graph, not a ladder"; "marginals cannot see a hole"); `docs/CYPHER.md` in full (the three refusals, the operator definitions and their statuses, the measured-five result, the d = 2 degeneracy, the roster docket); `tools/cypher.py` docstring |
| §6, the law itself | cited to *The Hierarchy Law of Mathematical Languages*, per the brief; not proved here |

---

## 3. What reproduces exactly

Every figure below was recomputed by `check.py` and agrees with the source to the digit printed.

- Λ 976 cells in a box of 6,912, E = 0 (C1); the tower member's Λ₈ equals the cypher fixture cell
  for cell (C1b); Λ₉ 1,654 in 27,648 and Λ₁₀ 2,535 in 110,592, both E = 0 (C12a, C12b).
- The periodic table 90 / 126 / 36, and the 36 are exactly period 1 groups 2–17 and periods 2 and 3
  groups 3–12 (C2, C2b); helium at group 2 gives E = 20 (C2c).
- Janet 118 / 944 / 0 (C3). The calendar 365 / 372 / 7 with the seven cells named (C4, C4b) and the
  relabel-by-length repair at E = 0 (C4c). Box ordering 35 / 125 / 0 (C5). Chessboard 64 / 64 / 0 (C6).
- The particle-bound nuclides at Z ≤ 5, 6, 7 — (27, 33, 6), (40, 48, 8), (52, 61, 9) — with the nine
  named, unchanged at larger cutoffs, and every cell persisting (C7, C7b, C7c).
- Kreuzer–Skarke 208 / 12,544 / 540, from 498 join and 498 meet failures of 21,528 pairs; 112 on the
  diagonal; χ ∈ {0, ±2, ±4}; h¹¹ + h²¹ from 26 to 262; all 540 satisfy h¹¹ ≥ 1, h²¹ ≥ 1 and
  h¹¹ + h²¹ ≤ 502 (C9, C9b, C9c).
- d(1) = 24, d(2) = 324, d(3) = 3,200, d(14) = 156,883,829,400, by product expansion and by the
  Euler recurrence independently, for N ≤ 16 (C10, C10b).
- Composable cells: Λ₈ 0, Λ₉ 1,169, Λ₁₀ 2,050 (C14).
- Redundancy and coupling: Λ 56 envelopes / 61%, the survey grid 6 / 20%, box ordering 6 / 0%,
  Janet 2 / 0%, periodic table 2 / 0%, calendar 2 / 0% (R1); r² = 0.002 and p = 0.94 (R2); the
  projection ladder 61 / 30 / 30 / 30 / 5 / 0 (R3); Nₑ adjoined takes 20% → 0% with the envelopes
  doubled to 12 and coupling 16.7% → 33.3% (R4).
- The EM quotient: the image is the complete 2 × 4 rectangle at E = 0 (Q1b); M1 814 and E1 840
  (Q1a); 576 intercombination cells (Q2); the spin rule 526 cells at E = 0 (Q4); the parity rule
  840 cells at E = 750 (Q5); H = 0.633 bits and I = 0.0004 bits (Q7b).
- The crossing: 11.6% against 40.7% within one element and 89.7% against 77.9% across the 118
  (Q8, Q8b, Q8c); the parity pair 38.4% against 20.1% within one element (Q8 rows).
- The languages: all five speak on Λ at E = 0, ten pairs, ten agreeing (L1, L1b); documentary
  silent, analysis not run (L1c); the box ordering 10 of 10 (L2); the three-coordinate periodic
  table at order 100, algebra 100, geometry 83, information 24, statistics 0 with 1 of 10 pairs
  agreeing (L3, L3b); the degeneracy guard fires at d = 2 and not at d = 3 (L4).

---

## 4. What does NOT reproduce, and what the paper does about it

**A finding is recorded, never repaired.** In every case below the paper prints the recomputed
figure, or omits the claim; no check was altered to make a discrepancy vanish.

### 4.1 The nuclide defect at the AME2020 evaluation: 9 stated, 2 measured

Index of Indices 236 and The_Method_1_6-2.md §6.2 state **E = 9** on the measured nuclide chart,
stable across cutoffs. Recomputed on AME2020 Table I as captured (3,558 rows, Z = 0–118, of which
2,550 carry a measured mass and 1,008 an extrapolated one), the defect is **E = 2** at every cutoff
Z ≤ 20, 50, 82, 92 and 118, and the two admitted-and-absent cells are (0, 0) and (2, 0), the diproton
(C8, C8b).

Mathematical Compendium §IV.E 1866 already carries this as a re-measurement and states it plainly,
so the later reading governs. The cause is not a disagreement about the operator: it is **two
different populations**. The 9 is measured on the *particle-bound* light nuclides; the 2 is measured
on the whole AME2020 set, which includes unbound and extrapolated species that fill most of the
region the smaller chart leaves open. `check.py` computes both (C7 and C8b), and the paper carries
both as two rows of Table 1 with the difference stated explicitly in §3.4. Neither number is
presented as a correction of the other.

### 4.2 The nuclide cell counts at Z ≤ 9: 80 / 89 stated, 75 / 84 measured

§6.2.1's table gives 80 nuclides and 89 admitted at Z ≤ 9. The seated particle-bound table gives
**75 and 84**, with E = 9 either way (C7). Only the defect, the nine named cells and their stability
are carried into the paper; the cutoff-by-cutoff cell counts printed in §3.4 are the recomputed ones
(27/33, 40/48, 52/61, 75/84, 87/96). The stated 80/89 is not printed anywhere.

### 4.3 The EM extension's defect: 3 stated in one place, 3,900 in another, 9,278 measured

Index of Indices 1471 states "*Adjoining the multipole and ΔS as coordinates gives E = 3*".
Mathematical Compendium §IV.EM 2636 states "*adjoining its coordinates gives E = 3,900*". The two
disagree with each other. Recomputed on Λ₉ with (|Δℓ|, |ΔS|) adjoined as two further coordinates:
**E = 9,278** (Q6). Neither source figure reproduces, and no variant tried reproduces either —
adjoining |Δℓ| alone gives E = 1,654 and |ΔS| alone gives E = 3,812 (Q6b, Q6c), both measured here
for the first time with no source figure to compare.

The paper prints **9,278**, and 1,654 and 3,812 beside it, and states the qualitative claim the two
source figures agree on — that the extension is open where the quotient is closed — as the result.
The cause of the two stated figures is undetermined: a different cap setting, a different set of
adjoined quantities (the multipole *label* rather than |Δℓ|), or an arithmetic error. The paper's
§2.3 supplies what the figures were evidence for — Corollary 3, which says a closed index extended
by a map that fails to preserve the join cannot be closed — so the qualitative claim now rests on a
proof rather than on a number that does not reproduce.

### 4.4 The channel survey grid: 1,664 cells and 313 held stated, 1,744 and 285 measured

Index of Indices 286 and 350 give the as-measured grid at **1,664** cells with **313** held (596
channels across them) and 1,351 unwitnessed. Rebuilt from the survey data as (Z, core charge, ℓ)
over the 28 elements, the ten charges [1, 2, 3, 4, 5, 6, 9, 11, 15, 16] and the eight ℓ values s…k,
restricted to charge < Z: **1,744 cells in a box of 2,240, with 285 of them witnessed** (C15). E = 0
either way. The paper prints 1,744, 2,240 and 285. The difference is in the cap, not the operator:
the reconstruction's element and charge alphabets are read off the survey file, and the source's own
text says every cap is a decision.

One reading is corrected rather than reproduced. The Index of Indices table at line 286 lists the
survey under a column headed **E** with the value 1,351 — the unwitnessed count. The same volume at
line 350 states outright that this number "*is never a closure defect*" and that all three grids are
fixed points of ℛ. The later statement governs, `check.py` measures E = 0, and the paper says so.

### 4.5 "Six agree on Λ at 976 and all ten pairs hold"

Index of Indices 280 says **six** languages agree and quotes C(5,2) = 10 for the pair count. The two
do not fit: six languages give fifteen pairs. Measured rather than asserted, the operator-bearing set
on Λ is **five** — order, algebra, geometry, information, statistics — with C(5,2) = 10 pairs, all
ten agreeing (L1b). The count survives; the membership is not the one the roster names: `statistics`
returns a cell decision and is in, `analysis` returns a magnitude and is out, joining `documentary`
as a second special row for a different reason.

Which languages exist at all is an open question in the sources (two rosters are printed and they
share two names), and the tool's third refusal is that it will not pick one. The paper therefore
does not assert a roster: §6 states that it counts a language as operator-bearing **on the index in
front of it** and computes the pair count from that, and it names the measured five. The word "six"
is not printed.

### 4.6 Λ's coupling: 29% stated, 28.6% measured

16 of 56 envelopes bind, which is 28.57%. The source rounds to 29%; the paper prints 28.6% (R1). The
survey grid's 1/6 is printed as 16.7% where the source rounds to 17%. No other redundancy figure
differs at the precision either states.

### 4.7 A box ordering at 56 cells and at 35 cells

The_Method_1_6-2.md §6.2's table gives a box ordering l ≥ w ≥ h at **56** cells, E = 0; Index of
Indices 66 and 1398 give **35** in a box of 125. These are the same construction over six values and
over five. The paper uses the five-value form, 35 in 125, which is the one the redundancy census and
the language-agreement fixture both use; the 56-cell form is not printed.

### 4.8 The Janet redundancy row

The six-row redundancy table's Janet entry (d = 2, 2 envelopes, 50% coupling, 0% redundancy)
reproduces only on the **724-cell down-set** of the 118-element filling along n + ℓ, not on the
118-cell (n + ℓ, Z) index of the catalogue, whose coupling is 100% (R1, R1b, R1c). Both are closed.
The paper prints the 724-cell form in Table 2 and says in the same paragraph which object it is and
what the 118-cell form gives, so the two rows of the paper that both say "Janet" are not confused.

### 4.9 The parity half of the crossing

Mathematical Compendium §IV.EM 2576 says "*parity repeats it at 38.4% against 20.1%*". Both numbers
reproduce exactly — but they are the **within-element** pair only. Measured across the 118 elements,
the parity split does **not** reverse: parity-conserving 89.8% against parity-changing 84.5%, the
same order as within (Q8 rows). The source quotes only the within-element figures, so nothing it
states is contradicted; but "repeats it" is an overstatement of what the parity split does, since
"it" is a crossing and the parity split does not cross.

The paper prints all four parity figures and says explicitly that the crossing proper belongs to the
|Δℓ| = 1 split and that the parity split is a companion to its within-element half only.

---

## 5. Interpretations chosen, and why

1. **Redundancy's protocol (D7).** The sources define redundancy as "*the largest fraction removable
   with exact recovery*" and print six values, but state no trial count, no acceptance threshold and
   no seed. The reconstruction here — a fixed ladder of ten fractions climbed in increasing order,
   ten independent trials per rung (five above 3,000 cells), acceptance at 8 of 10, stop at the first
   failure, seed 20260809 — reproduces **all six** published values and the whole six-rung projection
   ladder. That agreement is the evidence for the protocol. The paper states the protocol in full in
   D7 and marks every figure SAMPLED with its seed and per-rung counts, which the sources do not.

2. **Coupling's "binds" (D6).** The sources say "*the fraction of coordinate pairs whose envelope
   actually constrains*" without a test. The test used is: φ_ij binds when φ_ij(a) < max A_i(X) for
   at least one a. It reproduces 56 / 6 / 6 / 2 / 2 / 2 envelopes and 29% / 17% / 50% / 50% / 0% / 0%
   on the six rows, to rounding. The paper states the test in D6.

3. **Composability (D9), and the crossing population.** The sources say an index has a time column
   when its cells are moves, and print 976/0, 1,654/1,169, 2,535/2,050 without defining the match.
   The reading that reproduces all three is: a move's target end is (e, f, 2S′) or (e, f, g) and its
   source end (n, ℓ, 2S) or (n, ℓ, k), and a cell is followable when its target end equals the source
   end of some cell. Λ₈ gives 0 because its source end carries four components and its target end
   three, so no match is possible — which is why the source prints 0 there. The crossing population
   (4,325 moves over the 118 observed ground configurations) is built here from the ground
   configurations directly; the sources print the four percentages but not the population size, so
   **4,325** is measured here and has no source figure to agree with. The four percentages it yields
   agree with the source exactly, which is the corroboration.

4. **"E = 0 is VACUOUS".** The source asserts it. The paper proves it: the image is the complete
   2 × 4 rectangle (Q1b), and a full box closes by Theorem 2. The paper therefore states the
   vacuity as a consequence rather than as an assertion, and says in §5.4 what follows — that a
   claim of closure for the electromagnetic index carries no information about the rules.

5. **The convexity of the value set.** The source states "*ΔS = 0 is a diagonal, hence two monotone
   one-parent bounds*" and "*|Δℓ| = 1 is δ⁻¹({−1,+1}), a hole at zero, not convex*". Neither is
   proved there. The paper proves the interval property for a difference of two coordinates (Lemma
   3, and exhaustively on all 1,367,031 pairs of Λ₉) and derives the convexity criterion from it
   (Corollary 4), and exhibits the explicit witness for the non-convex case (Refutation 3). The
   sources' assertions become theorems with one witness.

6. **The nine nuclide cells as pairing and clustering.** The sources read the nine as "*the pairing
   and clustering terms of the mass formula, counted*". That is an interpretation of computed cells
   and no computation here establishes it. The paper names the nine, states which are unbound for
   which reason, and marks the mass-formula reading as an interpretation in both §0 and §3.4.

7. **The 540 Kreuzer–Skarke cells as predictions.** The catalogue file was not read, here or in the
   sources. The paper states the 540, the three published bounds all 540 satisfy, and that none falls
   in the sparsely populated tip — and says in §0 and §3.5 that this is weaker than a lookup.

8. **Bit cost (D10).** This paper's own construction, to put defects of different sizes on one scale.
   No source figure; every value is computed (C13, C13b).

9. **The fibration caveat.** Appendix D.5.5's own finding — that E falls as a fibration is refined
   and reaches zero by refinement alone — is stated in the sources as a measurement on one
   thirty-two-element index. The paper proves it: Theorem 4 (fibring by a coordinate never raises the
   total defect) and Corollary 2 (the finest fibration gives zero, because a singleton is a full box).
   The paper then states that every defect it reports is taken at the single fibre.

---

## 6. What the sources state that the paper deliberately omits

- **The book's own indexes** (the audits at E = 16, the register at 6, the protocols at 105, the
  constraints, the mathematics at 0, the numbers at 40). These index the working record, which the
  published text may not mention at all, and the brief did not ask for them.
- **The first-ionisation refusal map** (four steps of twelve, 67% admissible) — it belongs to another
  paper in this set and adds nothing to this one's thesis.
- **The 25 + 11 decomposition of the periodic table's 36**, which is computed on the drawn
  118-element layout rather than on the 90-cell index this paper closes. The two cell sets are
  different objects and mixing them would misstate what the 36 are.
- **Λ₃, Λ_phys, the violation index and the indexes named-and-not-built.** Outside the brief's scope.
- **The three-body, celestial-mechanics and Hagedorn material** of the same chapter as the
  Kreuzer–Skarke and string sections. Bracket results, not closure results.
- **The 32-column layout at E = 106 and the left-step at 120 cells / E = 0.** Both are further
  layouts of the same elements; the paper makes the coordinate-relativity point with the two it
  computes in full and does not multiply instances.

---

## 7. Refusals of the imported instrument that bind the paper

`tools/cypher.py`'s docstring and `docs/CYPHER.md` state three refusals, and each constrains what
§6 may say. They are carried into the paper as an explicit paragraph, not silently honoured.

1. **A language that was never run is not silent.** `NOT-RUN` is a distinct state from `SILENT`. The
   paper reports `analysis` as not run (it declares no witness) and `documentary` as silent by
   construction, and never merges the two.
2. **Agreement at two coordinates is not evidence.** At d = 2 there is one coordinate pair, so
   pairwise consistency and cell membership coincide and every pairwise operator agrees for no
   reason; such a run is marked degenerate and its agreement withheld. Every agreement figure in the
   paper is at d ≥ 3, and the paper says why.
3. **The roster is not chosen for you.** Which languages there are is open. The paper counts
   operator-bearing languages **as measured on the index in front of it** and computes C(5,2) from
   that, and does not assert a roster. This is also why §4.5 above is a correction of a membership
   and not of a count.

A fourth refusal binds the same way: a resource cap reports as `REFUSED` and never as `SILENT`,
because a compute limit is not a finding. No run in `check.py` hit a cap.

Finally, the law relating the five operators to one another is cited, not proved: the paper states
that on four indexes with d ≥ 3 the five agree exactly when all five defects are zero, calls that a
measurement on four indexes, and attributes the general law to *The Hierarchy Law of Mathematical
Languages*. The sources' own hedge — that the "without exception" of the agreement claim is an
overgeneralisation on a base of six indexes and three operators — is the reason the paper does not
state it as a theorem.
