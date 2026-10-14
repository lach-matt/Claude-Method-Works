# SOURCES.md — provenance map for 10-beyond-the-atom (not published)

Paper: `PAPER.md`, "Closure beyond the Atom: the Defect of an Index, Its Zeros by Theorem, and the
Electromagnetic Quotient" — the title settled 2026-09-24 at the author's direction; it had been carried as a
working title in sentence case since the repair, and the settlement re-cases it to match the shelf and changes no word. Drafted 2026-09-21; repaired 2026-09-24 against `AUDIT.md` (132 findings).
Every number in the paper is produced by `check.py` or is CITED. Run of 2026-09-24: `python3 check.py`
→ **148 obligations, 0 failed** (MACHINE-CHECKED 8, EXHAUSTIVE 74, MEASURED 35, SAMPLED 16, REFUTATION 3,
CITED 1, GUARD 11), `CLEAN`; `python3 check.py --selftest` → **152 obligations, 0 failed**, the four negative
controls N1–N4 each refuted (N3: 18 of 1,112 cells disagree), `CLEAN`.

Run: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH; python3 check.py --selftest`.

Instruments imported by path, never copied: `research/warp-drive/prover.py` (the Z3 harness and its
`cells_of` / `meet` / `join` / `in_R` / `subset_vars` / `contains` / `prove` / `non_vacuous`);
`tools/cypher.py` (`op_order` — the closure operator under test — and the four other language
operators, plus its index builders `_lambda`, `_periodic`, `_kreuzer_skarke`, `_box_ordering`,
`_tower`, `_ELEMENT`, and `_nuclide`, which is now used only to be compared with the derived list);
`method/members/tower-2.py` (Λ₈…Λ₁₀); `extracted/archives/restore-point-2-13/close_L118.py` (the 118
observed ground configurations, used only for the followability population). Data read, not copied:
`extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv`,
`extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv`, and — new on 2026-09-24 —
`nubase2020-Z0-10.txt` beside the check (§1.3 below).

Reference implementations written fresh here, as the independent side of the encoding guards:
`R_ref` (the staircase written from D3/D4 alone), `hull` (the sublattice hull), `graph_truths` (the
enumerative decision of the three predicates of Theorems 5 and 6), `envelopes` and `coupling`. The
object under test is always the seated operator.

---

## 1. Corrections made on 2026-09-24, and where they came from

### 1.1 The fibration claim (AUDIT A-1, A-2)

The first draft defined a fibration as any partition and claimed "fibring never raises the total
defect". That is false for a general partition — X = {(0,0),(0,1),(1,0)} has E = 1 and the partition
{(0,1),(1,0)} ∪ {(0,0)} has fibred defect 2 — and the check now prints the counterexample (T4b,
REFUTATION). The source passage (The_Method_1_6-2.md D.5.5 10696–10735) only ever fibres by
categorical axes, i.e. by a coordinate, so the source's statement was correct and the draft's
generalisation was the error. D5 now defines a fibration by a coordinate; Theorem 4 holds for any
coordinate i (the proof is unchanged; T4 is machine-checked over every coordinate of each of the three
boxes, 8 instances); Corollary 2 iterates over i = 1..d and T4c checks the chain on 766 subsets.

### 1.2 The crossing (AUDIT R-6, R-7)

The source (Index of Indices 165–180; Mathematical Compendium §IV.EM 2570–2576) states four
percentages — allowed followable 11.6% within one element against forbidden 40.7%, and 89.7% against
77.9% across the 118 — and calls their reversal a crossing. All four reproduce exactly on the
population the draft built from the ground configurations (4,325 moves, Q8., Q8b, Q8c). **That
population is two-thirds unphysical**: its rule bounds the electrons delivered by the target's capacity
4f + 2 and never by its room, so 2,923 of the 4,325 moves deliver more electrons than the target
subshell can still hold (2,203 into a subshell already full), and 2,819 move more than one electron
(Q8a). Restricted to physical one-electron moves into a subshell with room — 134 moves — the order
does not reverse: forbidden leads within (18.7% against 11.9%) and across (64.0% against 40.7%)
(Q9., Q9b, Q9c). **The source's crossing figures are therefore reproduced on a population that is
two-thirds Pauli-forbidden, and the paper claims no crossing.** The followability match itself is
formal (electrons delivered against electrons held); a configurational match (target at the occupancy
it holds after the move) gives zero within one element on both populations, necessarily, and 5.1%
against 26.7% across the table on the physical population (Q10, Q10., Q10b). The paper prints both
populations and both matches (§5.5, Table 3, Figure 4) and says what each is. The "crossing" left the
abstract and §0; the title never carried it.

### 1.3 The particle-bound nuclide list (AUDIT A-10, R-10)

The draft used the instrument's hand-typed fixture (`tools/cypher.py` `_NUCLIDES`), uncited. The
list is now **derived** from NUBASE2020 (Kondev, Wang, Huang, Naimi and Audi 2021, Chinese Physics C
45, 030001). The evaluation's file `nubase_4.mas20.txt` was fetched from two independent public
copies — `raw.githubusercontent.com/awsteiner/o2scl/main/data/o2scl/nucmass/ame20/nubase_4.mas20.txt`
and `raw.githubusercontent.com/pynucastro/pynucastro/main/pynucastro/nucdata/AtomicMassEvaluation/nubase_4.mas20.txt`
(the AMDC host itself was not reachable from this session) — and the two copies are byte-identical,
md5 `91e92411c7c609aa73b28136da61317f`. The verbatim ground-state lines with Z ≤ 10 (144 lines) plus
the file's own header are kept beside the check as `nubase2020-Z0-10.txt`, md5
`56728dd35af7bd1906681ba56a9facf6`, checked by C7. The criterion, stated in the paper: a ground state
with Z ≥ 1 is particle-bound unless the half-life field reads `p-unst` or the first listed decay mode
is n, 2n, 3n, p, 2p, 3p or A (α). Under it the derived list agrees with the fixture through Z ≤ 8 and
differs at Z = 9, 10 exactly as the audit said: the fixture omits F-29, F-31, Ne-17, Ne-29, Ne-31,
Ne-32 and Ne-34 (C7f). Ne-33 (`n ?`, no half-life) and F-30 (`n ?`) are unbound under the criterion.

Consequences: the six cutoffs are 27/33/6, 40/48/8, 52/61/9, 64/73/9, 77/86/9, **94/106/12** (C7a);
the three cells added at Z ≤ 10 are F-16, F-28, F-30 (C7b), every one a ground state the evaluation
lists as unbound (C7d); they appear only when neon enters because N = 7, 19, 21 are first realised by
Ne-17, Ne-29, Ne-31 (C7e). **The draft's sentence "none is added after Z ≤ 7: the defect is a property
of the measurement, not of the window" was false and is gone**; the paper now says the count is not
stable and the reading is. The source's own figures — E = 9 stable across four cutoffs, 80/89 at
Z ≤ 9 (The_Method_1_6-2.md §6.2.1 1678–1699) — are not reproduced at Z ≤ 9 (77/86) or Z ≤ 10 (94/106/12);
the source's fixture was incomplete, and the paper prints the derived figures.

### 1.4 Theorem 0 and the attribution (AUDIT A-3, R-1, R-20)

The draft cited ℛ(X) = ⟨X⟩ to the hierarchy-law manuscript, whose own provenance ledger records it as
prior art (Queyranne and Tardella 2008, Theorem 11; Topkis 1976; Veinott 1989; Baker and Pixley 1975).
The paper now states it as Theorem 0 with that attribution and the six-line proof (z⁽ⁱʲ⁾, w⁽ⁱ⁾,
u⁽ⁱ⁾ = w⁽ⁱ⁾ ∧ ⋀ z⁽ⁱʲ⁾, x = ⋁ u⁽ⁱ⁾), Corollary 1 is an equivalence, and the former Proposition 1
survives as the exhaustive corroboration T3/T3b. The hierarchy-law manuscript is cited once, in §6,
for the containment law it proves, and nothing in this paper's proofs rests on it.

### 1.5 Zeros by theorem (AUDIT R-18, A-7, A-8)

The audit found that of the fourteen rows only seven carried information. Working out why, the closed
rows turn out to be closed **by theorem**: Lemma 3 (a bimonotone cut a·xᵢ − b·xⱼ ≥ c of a sublattice
is a sublattice — the finite-chain case of Queyranne and Tardella 2006) with Theorem 0 gives E = 0 for
Λ (eight bimonotone inequalities over the caps box; T7a checks Λ is exactly that cut, 976 cells equal
to the tower's), Λ₉, Λ₁₀ (T7b), the box ordering (T7c), the product grid (T7d) and Janet's staircase
(T7e). This is a stronger and more honest statement than the draft's "E separates the closed from the
open": no zero in the catalogue is a measurement. The thesis and title were restated accordingly.
The survey's own data — the 285 witnessed channels — are added as a row: 285 cells, box 1,960,
|ℛ| = 1,260, E = 975 (C15b). The Kreuzer–Skarke slice is stated as open by construction (value set
{−3, +3} of h(1,1) − h(2,1); witness (13,16) ∨ (16,13) = (16,16), C9d) and the word "predictions"
is gone; C9c is kept as bookkeeping and the paper says it tests nothing about the list.

### 1.6 The redundancy protocol (AUDIT A-9, A-20, R-19, R-21)

D7 now says the ladder, the ten trials and the 8-in-10 acceptance are conventions, chosen because
they reproduce the previously reported figures and for no other reason; every figure is printed with
the rung passed, the rung failed and the counts (Table 2, §4.3, from R1. and R3. logs). The d = 3
projection has 12 cells, ⌊0.05 × 12⌋ = 0, no trial ran (R3c); the paper prints "below resolution".
The unused T = 5 branch is removed (ten trials always). r² and p are no longer printed (R2 still
computes them; nothing in the paper cites the row).

### 1.7 The languages (AUDIT A-5, A-6, A-23, R-2)

The third coordinate of the discriminating index is the instrument's block coding 0/2/1 for columns
1–2 / 3–12 / 13–18, helium carrying its column's value (L3c). The paper states it as the ℓ of the
column's block, an ordered quantity, and says the order is a choice. The order–algebra pair agrees by
Theorem 0 and is discounted: pair counts over the four distinct operators are 6/6, 6/6, 0/6, 6/6 (L7).
Lemma 4 proves each operator returns a superset (the information operator defined via generators, as
the instrument computes it; statistics as the set formula, with Haberman 1974 for the existence
caveat), and L6 checks that no operator is marked NOT EXTENSIVE. The "agree iff all E = 0" sentence
now states the trivial direction, calls the converse unproved and false in general, and reports four
indexes as four indexes.

### 1.8 The guards (AUDIT A-29, A-30, A-31)

T0d evaluates the three Z3 predicates of Theorems 5 and 6 under 240 random assignments of (S, h)
over the two boxes against `graph_truths`, and T5/T6 are refused if it fails. T0c runs per box
(three rows) and a further row records that Theorem 1(a), 1(c) and Theorem 4 hypothesise only a
non-empty X. The non-constancy demand of the T5 guard is on S, not on the box; T6 has its own guard
line.

### 1.9 What was dropped from the paper (retained in the check, unprinted)

The §3.1 composability paragraph (Λ₈ 0 / Λ₉ 1,169 / Λ₁₀ 2,050: C14, C14b), the mutual-information
paragraph of §5.4 (H = 0.633, I = 0.0004: Q7, Q7b), the string degeneracies d(1), d(2), d(3), d(14)
(C10, C10b), and r² = 0.002 / p = 0.94 (R2). Each rested on the formal followability match or on
material the audit found decorative (A-26, R-13, R-21, R-7). The rows remain in `check.py` so that
nothing was weakened; the paper simply no longer prints them.

---

## 2. Where each section draws from

| paper section | source passages (all under `method/members/`) |
|---|---|
| Thesis, §0 | Index of Indices 61–88 (the five drawn-beside indexes; "E = 0 carries information only when the ambient box exceeds the cells"); 158–372; The_Method_1_6-2.md §6 1516–1729 and §31 8614–8795 |
| §1 D1–D4 | The_Method_1_6-2.md 1546–1556 (Âᵢ(X), φ̂ᵢⱼ(v), ℛ(X), E(X)); `docs/CYPHER.md` operator table; `tools/cypher.py` `op_order` |
| §1 D5, Remark 1, Theorem 4, Remark 3, Corollary 2 | The_Method_1_6-2.md D.1 10363–10375 ("ℛ recovers MONOTONE bounds… fibre over the categorical axes"); D.5.5 10696–10735 (E 4/3/2/0 under refinement, "relative to a stated fibration"). The source fibres by categorical axes only; the general-partition counterexample is this paper's |
| §1 D6, D7, §4 | Index of Indices 310–340 (the six-row table; the projection ladder 61/30/30/30/5/0; Nₑ = Z − c + 1) |
| §2.1 Theorem 1, Lemma 2, Theorem 2 | The_Method_1_6-2.md §6.2 1650–1656 ("ℛ is idempotent — §32.4.1 proves it"); `docs/CYPHER.md`. The proofs are written here from D3/D4 |
| §2.1 Theorem 0 | Queyranne and Tardella 2008 (Thm 11), Topkis 1976, Veinott 1989, Baker and Pixley 1975, as recorded in `research/warp-drive/paper/THE-HIERARCHY-LAW.md` §4.3 and §9; the proof is written here |
| §2.3 Theorems 5, 6, Corollary 3, Refutations 1–2 | Index of Indices 1467–1475 ("a selection rule is a QUOTIENT and not an extension"); Mathematical Compendium §IV.EM 2630–2640. The lattice statement and the counterexamples are this paper's |
| §2.4 Lemma 3, Corollary 4, Proposition 2 | Mathematical Compendium §IV.EM 2620–2626 ("ΔS = 0 is a diagonal…"; "|Δℓ| = 1 is δ⁻¹({−1,+1}), a hole at zero, not convex") — the source asserts convexity; the lemma and the proposition are this paper's, with Queyranne and Tardella 2006 for the inequality class |
| §3.1 Λ and the tower | The_Method_1_6-2.md §7.1 (the eight inequalities); Index of Indices 1414–1440; `method/members/tower-2.py` |
| §3.2 the two tables | The_Method_1_6-2.md §6 1516–1545 (90 / 126 / 36); §6.1.1 1560–1600 (helium at 2 → 20); Index of Indices 1360–1380, 1442–1456 (Janet 118 / 944 / 0) |
| §3.3 calendar, box, chessboard | The_Method_1_6-2.md §6.3 1700–1712; Index of Indices 1398–1410, 1458–1466 |
| §3.4 the nuclide chart | The_Method_1_6-2.md §6.2 1660–1676, §6.2.1 1678–1699 (E = 9, four cutoffs — see §1.3 above); Index of Indices 236–244; Mathematical Compendium §IV.E 1860–1872 (the AME2020 re-measurement, E = 2); NUBASE2020 as §1.3 |
| §3.5 Kreuzer–Skarke | The_Method_1_6-2.md §31.3 8730–8795 (208 cells, E = 540, 498 + 498, 112 diagonal, five χ values, 26–262); Index of Indices 246–256. The source's "the index proposes" reading is not carried (A-7, R-12) |
| §3.6 oscillators | The_Method_1_6-2.md §31.2.3 8700–8706; Index of Indices 258–266 — reduced to Theorem 2's sentence; d(N) not printed |
| §3.7 the survey | Index of Indices 340–372 (the grid; "never a closure defect"); `extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv`. The witnessed-channel row is this paper's |
| §3.9 bit cost | this paper's own construction |
| §5 the electromagnetic quotient | Index of Indices 165–180; Mathematical Compendium §IV.EM 2570–2672 (the rectangle; 814 and 840; E = 750; 526 at E = 0); Laporte 1924, Russell & Saunders 1925, Wigner 1927; Condon & Shortley 1935 and Cowan 1981 for the one-electron rule (R-15) |
| §5.5 followability | Index of Indices 165–180 and Mathematical Compendium 2570–2576 (the four percentages and the parity pair) — see §1.2 above |
| §6 the languages | The_Method_1_6-2.md §33 9405–9500; Index of Indices 268–284; `docs/CYPHER.md`; `tools/cypher.py` |
| §6, the containment law | cited to *The Hierarchy Law of Mathematical Languages* (manuscript); not used |

---

## 3. What reproduces exactly

- Λ 976 / 6,912 / 0 (C1); the tower member equals the cypher fixture (C1b); Λ₉ 1,654 / 27,648 / 0 and Λ₁₀ 2,535 / 110,592 / 0 (C12a, C12b); Λ is exactly the caps box cut by the eight inequalities (T7a).
- The periodic table 90 / 126 / 36, the 36 named (C2, C2b); helium at group 2 gives E = 20 (C2c).
- Janet 118 / 944 / 0 (C3), a staircase (T7e). The calendar 365 / 372 / 7 with the seven cells named (C4, C4b) and the relabel-by-length repair at E = 0 (C4c). Box ordering 35 / 125 / 0 (C5). Chessboard 64 / 64 / 0 (C6).
- The particle-bound nuclides at Z ≤ 5, 6, 7 — (27, 33, 6), (40, 48, 8), (52, 61, 9) — with the nine named (C7a, C7b); at Z ≤ 8, 9 the nine persist; see §1.3 for Z ≤ 10.
- AME2020 3,558 rows, 2,550 measured, 1,008 extrapolated, E = 2 at five cutoffs, the two cells (0,0) and (2,0) (C8, C8b).
- Kreuzer–Skarke 208 / 12,544 / 540, 498 + 498 of 21,528, 112 diagonal, χ ∈ {0, ±2, ±4}, 26–262 (C9, C9b).
- The redundancy rungs: Λ 61%, the grid 20%, box ordering / Janet down-set / periodic table / calendar below 5% (R1); the projection ladder 61 / 30 / 30 / 30 / 5 / — (R3, with the d = 3 stop R3c); Nₑ adjoined 12 envelopes, 33.3%, below 5%, E = 20,808 (R4, R4b).
- The quotient: the complete 2 × 4 rectangle at E = 0 (Q1b); 814 and 840 (Q1a); the spin rule 526 at E = 0 (Q4); the orbital rule 840 at E = 750 (Q5); the witness (Q5c, Q5d); the extensions 9,278 / 1,654 / 3,812 (Q6, Q6b, Q6c) with a join-failure witness each (Q6d).
- The four followability percentages on the unfiltered population (Q8b) and the parity pair 38.4% / 20.1% (Q8. rows).
- The languages: five speak on Λ at E = 0 (L1), ten pairs agreeing (L1b), the three-coordinate table 100 / 100 / 83 / 24 / 0 with one pair agreeing (L3, L3b), degeneracy at d = 2 (L4).

---

## 4. What does NOT reproduce, and what the paper does about it

**A finding is recorded, never repaired.** The paper prints the recomputed figure or omits the claim.

### 4.1 The nuclide defect at the AME2020 evaluation: 9 stated, 2 measured
Two populations (see the draft's account, unchanged): the 9 is the particle-bound light nuclides, the 2 the whole AME2020 set; the paper carries both as two rows (C7a, C8b).

### 4.2 The nuclide counts at Z ≤ 9 and Z ≤ 10
The source states 80 / 89 at Z ≤ 9 and E = 9 stable across cutoffs. Derived from NUBASE2020: 77 / 86 / 9 at Z ≤ 9 and 94 / 106 / 12 at Z ≤ 10 (C7a). See §1.3. The stated 80 / 89 and the stability claim are not printed.

### 4.3 The EM extension's defect: 3 stated in one place, 3,900 in another, 9,278 measured
Unchanged from the draft: neither source figure reproduces; the paper prints 9,278 with 1,654 and 3,812 beside it and rests the qualitative claim on Corollary 3 (Q6, Q6b, Q6c, Q6d).

### 4.4 The survey grid: 1,664 cells and 313 held stated, 1,744 and 285 measured
Unchanged from the draft (C15); the "E = 1,351" reading is corrected by the source's own later sentence. New: the paper now also prints the witnessed set's own closure, 285 / 1,960 / 975 (C15b), which no source states.

### 4.5 "Six agree on Λ"
Unchanged: five operator-bearing languages measured (L1b); the paper does not print "six".

### 4.6 Λ's coupling 29% → 28.6%; the grid's 17% → 16.7%
Rounding; the paper prints the exact fractions (R1).

### 4.7 A box ordering at 56 and at 35 cells
The five-value form, 35 in 125, is used; the 56-cell form is not printed.

### 4.8 The Janet redundancy row
Reproduces only on the 724-cell down-set (R1b, R1c); the paper says so in §4.2 and calls the choice a convention (R-19).

### 4.9 The parity half of the crossing
Both within-element parity figures reproduce (38.4 / 20.1); across the table the parity split does not reverse (89.8 / 84.5). The paper prints all four on both populations and says the parity split crosses on neither.

### 4.10 The crossing itself
See §1.2: reproduced exactly on the source's population, which is two-thirds Pauli-forbidden; absent on the physical population. The paper claims no crossing.

### 4.11 "E = 9 is a property of the measurement, not of the window"
Not reproduced on the completed data (C7a, C7b); the paper says the count moves and the reading does not.

---

## 5. Interpretations chosen, and why

1. **Redundancy's protocol (D7)** — a convention (ladder, ten trials, 8 of 10, seed 20260809), stated as such; its justification is that it reproduces the previously reported rungs, and the paper says that is its only justification.
2. **Coupling's "binds" (D6)** — φᵢⱼ is not the constant Mᵢ; stated with the caveat that a non-constant envelope need not exclude a cell (R-3).
3. **Followability (D9)** — the formal match that reproduces 0 / 1,169 / 2,050 and the four crossing percentages; labelled formal; the configurational match computed beside it (§1.2).
4. **"E = 0 is VACUOUS"** — proved as Theorem 2 on the full 2 × 4 image (Q1b), and restated as the independence of Δℓ and ΔS on Λ₉ (R-14).
5. **Convexity** — Lemma 3 (bimonotone cut) and Corollary 4, with Refutation 3's witness; the interval property exhaustive on 1,367,031 pairs (Q3).
6. **The nuclide cells as pairing and clustering** — an interpretation, marked; the diproton sentence rewritten to the singlet-channel explanation (R-9); (0,0) called the bottom of the box (A-27).
7. **The Kreuzer–Skarke 540** — the closure of a slice that is open by construction; not predictions (A-7, R-12). The full Hodge-pair list was not read here, and the paper says so.
8. **Bit cost (D10)** — a description length under a uniform code over E-subsets (R-5).
9. **The fibration caveat** — Theorem 4 for a coordinate, Remark 3 for the general case, Corollary 2 iterated.
10. **The block coordinate** — the instrument's coding read as the ℓ of the column's block; a declared choice of order (A-5).

---

## 6. What the sources state that the paper deliberately omits

Unchanged from the draft: the book's own indexes; the first-ionisation refusal map; the 25 + 11 decomposition of the 36; Λ₃, Λ_phys, the violation index; the three-body and Hagedorn material; the 32-column layout and the 120-cell left-step. Added: the string degeneracies d(N) (computed, unprinted); the composability counts 1,169 / 2,050 (computed, unprinted); r² and p (computed, unprinted); the crossing as a claim.

---

## 7. Refusals of the imported instrument that bind the paper

Unchanged: NOT-RUN is not SILENT; agreement at d = 2 is withheld; the roster is measured on the index in front of it and not asserted; a resource cap is REFUSED, never SILENT (no run hit a cap). The containment law is cited, not proved, and the paper no longer calls its four-index observation "one instance of a general law".

---

## 8. Figures

`figures/figure-1-periodic-table.png` is now computed by `figures.py` from C2 / C2b (the audited plate it replaces had its title across the first row of cells and no legend, AUDIT A-38); Figures 2–4 are computed from `check.py`'s VALUES. `FIGURES.tsv` carries the md5 of each after the final run.


**The redundancy protocol — closed 2026-09-24 as a reconstruction.** The store was searched for an instrument stating the trial count, threshold or seed behind the source's redundancy figures; none exists in the seated members, the recovered tree or the extracted archives (the word occurs only in audit scripts about other things). D7 stays the paper's own stated convention, marked SAMPLED, which is what the tree supports.
