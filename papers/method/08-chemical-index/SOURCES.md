# SOURCES.md — provenance map for 08-chemical-index (not published)

Paper: `PAPER.md`, "Closing the Chemical Properties: a Classification Index for the Elements" — the title settled 2026-09-24 at the author's direction; it had been carried as a working title in sentence case since the repair, and the settlement re-cases it to match the shelf and changes no word.
Drafted 2026-09-21 as "… a routing index for the elements"; audited 2026-09-24 (`AUDIT.md`, 58 findings);
repaired 2026-09-24 against that audit. The repair kept every result the audit did not refute and
replaced what it did; the title changed because the routing claim was withdrawn (R-C14). Every number
the paper prints is produced by `check.py` (**96 obligations**, all discharged; `--selftest` adds three
negative controls, all refuted) or is CITED.

`check.py` run: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH; python3 check.py`
→ `summary: EXHAUSTIVE 68, MACHINE-CHECKED 12, SAMPLED 2, CITED 3, GUARD 11 / all obligations
discharged`, exit 0, ~40 s. `--selftest` → the same plus N1, N2, N3 `ok`, `GUARD 14`, exit 0. Logs in
the scratchpad (`p08-check.out`, `p08-selftest.out`). The pre-repair run was 75 obligations
(52/8/2/2/11); the 21 added are named under "The repair" below.

## Where each section draws on

| paper section | source passages (under `method/members/` unless stated) |
|---|---|
| Thesis, §0, Abstract | Physics Compendium 692–784 (Λ_chem: the three coordinates; the fifth seat; "E = 0 on fourteen cells"; the boundary table; the last cell; the routing table — the last two of which the paper now declines to read as the source does); Physics Compendium 784–841 (Λ_PCA: "Merged on that axis alone: E = 0 on nine cells"; the 4 × 6 multiplicity table; Λ_amp); Index of Indices 1671–1751 |
| §1 D1–D6 (index, box, ℛ, defect, ordering, staircase) | `tools/cypher.py` `op_order` (imported by path) and `Index` (the own box is the product of the REALISED alphabets); Mathematical Compendium 3580–3600 ("The staircase algebra of a closed index"); companion paper `papers/method/01-closure-law` (cited as a companion; the part used is Lemma 3, proved in §2) |
| §1 D7–D11 (kind, seat, fifth seat, dependency, Λ₁₄) | `extracted/archives/restore-point-2-13/chem4.py` (`KIND`, `SEAT`, `PCA`, the 42-row table `C` read as a literal by `ast`, never executed); Physics Compendium 711–730. **The second clause of D7** (a quantity fixed by a symmetry label alone) and **the "nominal" reading of D10 at the outer seats** are the paper's own, made in answer to R-C2 and R-C3; the source states neither |
| §1 D12 (Slater integrals) | `extracted/archives/restore-point-2-13/amp_index.py` (`integrals(l1,l2)`, `PAIRS`); Physics Compendium 815–841; Mathematical Compendium 3604–3620; the definitions of Rᵏ, Fᵏ = Rᵏ(ab, ab), Gᵏ = Rᵏ(ab, ba) verified against a public text (see "What did not reproduce" 5) |
| §2 (Lemmas 1–4, Lemma 2′, "Where ℛ sits", the closed families, the base rate) | `research/warp-drive/prover.py` (`in_R`, `observed`, `contains`, `prove`, `non_vacuous`, `encoding_matches`, `join`, `meet` — imported by path); Ganter's next-closure and the brute-force subset count implemented fresh in `check.py`; the orbit-union count of C3c (fourteen-cell subsets closed under SOME ordering) written for the repair in answer to R-M4 |
| §3 Table 1 | `chem4.py` `C` for kind/seat/dependency; `chem3.py` `C` for the breadth coordinate (A6, A6b); the "what it is" column is written here as standard physical chemistry. **The source column of the first draft is dropped** (R-C7): no source is named for any of the 42 in the instruments, and the paper says so in prose. **Restored and filled 2026-09-24 at the author's direction**: a fifth column names, for every one of the 42, the public tabulation in which a reader finds it — eleven the NIST ASD, thirty-one the twenty-one compilations added to the References, each verified by web search (the publishers' pages are behind the proxy) as to authors, title, journal or publisher, volume and pages, and as to carrying the property named; the paper still takes no number from any of them. The CRC Handbook is cited in its current edition (106th, 2025). The instruments still name no source; the column is the paper's |
| §4 (Theorem 1, Propositions 3–5, the closing orders) | `chem4.py` (the closure and the min-E sweep); Physics Compendium 733–767. Propositions 3, 4, 5 and the centrifugal-barrier alternative (B6–B9, C3c) are the paper's own measurements, made in answer to R-M3, R-M4, R-C2, R-C4 |
| §5, §6 | Physics Compendium 736–767 (the boundary table; "The last cell, and what filled it"; the ground-term table at Nₑ = 20, 38, 56, 88) |
| §7 | `phys_close.py` `P` (22 rows); `charge_index.py` `CH` (nine occurrences); `dom_reg.py` `PH`, `CH` (the merge on `domain ≡ regime`); `recovered/merge.py` `PH`, `CH` (the earlier merge on identified axis names); Mathematical Compendium 3592–3600 (`L(s) = ⌊s/2⌋`, `U(s) = s + ⌊s/3⌋`); Index of Indices 1671–1682, 1697–1716; Physics Compendium 784–813 |
| §8 | `amp_index.py`; the 3-j symbol by Racah's formula and Slater's Rᵏ on hydrogenic functions, both implemented fresh in `check.py` in exact `Fraction` arithmetic |
| §9, §10 | the check's own output; no source passage |

All instruments named above are read **by path**, as literals via `ast.literal_eval`, or imported by
path. Nothing is copied into `check.py`; the fresh implementations are `ref_R` (the independent
witness-form staircase for the encoding guard), next-closure, the brute-force count, the 3-j symbol
and the hydrogenic Rᵏ.

## What did not reproduce, and how the paper handles it

### 1. The printed boundary table mixes two property tables (obligations E1, E2, E3)

The source prints, as one table, 14/0, 15/3, 20/8, 21/11, 26/19. Recomputed, that sequence is
**not** one table. With the ground term on a charge role the five rows are **14/0, 16/2, 21/7,
22/10, 27/18**; with it on a physics parameter they are **13/1, 15/3, 20/8, 21/11, 26/19**. The printed
table is the first row of the filled table above the last four rows of the unfilled one — E1 asserts
exactly that. **Disposition:** the paper prints both tables (Theorem 2, Figure 2), never the mixed
sequence; the record's E1 row describes the splice without printing it (A-1).

**The source reads the table as a boundary of the classification. The paper no longer does** (R-C3,
R-R11): eighteen of the twenty outer-seat properties carry a dependency label that D10's own
criterion does not license, so Theorem 2 measures the labels, and §5 says so. The monotone climb is
still reproduced and still printed; the reading is withdrawn.

### 2. The single defect cell of the amplitude index on the raw rank (obligations I4, I4b)

The source states the single defect is **F¹**. Recomputed on the cell set `amp_index.py` builds, the
minimum defect over all 5,760 orderings is 1, but at both minimising orderings the single added cell
is **G¹ at ℓ = 0 (an s rival)**. **Disposition:** the paper prints the reproduced cell, with the parity
argument written for that cell and for the s/s pair specifically (A-19). F¹ is not printed.

### 3. "All 1,440 orderings" (obligations B2, B2b, F1)

The realised values at the two closed seats are four kinds, two seats and three dependencies, so
there are 4! · 2! · 3! = **288** orderings; 1,440 = 288 × 5 permutes the unrealised fifth kind, which
cannot change ℛ (D2). **Disposition:** the paper states 288 and says the 1,440 are the same 288
counted five times.

### 4. One parameter's domain differs between the two tables that feed the merge (obligation H7)

`phys_close.py` gives `C′ = 1` the domain *all elements*; `dom_reg.py` gives it *low*. Sources agree
on 21/21, domains on 20/21. **Disposition:** recorded, not repaired; §7 shows the discrepancy moves no
cell (both cells stay occupied by other items — read off `RESULTS["pca_names"]` and Table 3).

### 5. The Slater result at s/s and f/f (the audit's BLOCKING finding A-8; obligations I5b, I8, I8b, I8c)

The source states: "At s/s the exchange G⁰ IS the direct F⁰, so dropping exchange costs nothing; at
f/f it discards four independent quantities." The first draft printed the conclusion ("discards no
independent radial quantity at s/s and four at f/f") without the reason, and the audit showed no single
reading makes both clauses true: the reason (G⁰ = F⁰) holds for *equivalent* electrons — the same
radial function twice — and for equivalent electrons it holds at every rank, so f/f discards nothing
independent either; for *non-equivalent* pairs (nℓ, n′ℓ) it fails already at s/s, which discards one.

**How the identity was verified.** The tree holds no copy of Condon and Shortley (1935) or Cowan
(1981); `drive/MANIFEST.tsv` has no such title, and the volumes cite the rank rules only. The
definitions were therefore taken from a public text that restates them from those sources: Pain,
J.-C. (2023), *Inequalities for exchange Slater integrals*, arXiv:2309.00503, eqs. (2), (5), (7) —
Rᵏ(ij, tu) = ∫∫ (r<ᵏ / r>ᵏ⁺¹) Pᵢ(r₁)Pⱼ(r₂)Pₜ(r₁)Pᵤ(r₂) dr₁dr₂, Fᵏ(ij) = Rᵏ(ij, ij), Gᵏ(ij) = Rᵏ(ij, ji),
citing Slater 1929, Condon and Shortley 1935, Cowan 1981 (read through the alphaXiv connector; the
proxy blocks arxiv.org, Wikipedia and DLMF directly). With i = j the two are the same integral —
Lemma 6 is that observation and nothing more. A second public text, Moore and van der Laan,
arXiv:0807.0416 (eqs. 27–28 and the sentence following, eq. 41), gives the same integrands and
states that for equivalent electrons no exchange integral appears in the energy of ℓⁿ, which is the
sentence Lemma 6 adds as CITED. The 3-j closed form (j j 0; m −m 0) = (−1)ʲ⁻ᵐ/√(2j+1), the
column-permutation sign (−1)ʲ¹⁺ʲ²⁺ʲ³ and the all-zero parity rule used in Lemma 5 (A-7) were confirmed
against public statements (Edmonds 1957 as cited there) and are computed exactly in I6, I6b, I7.
Beyond the citations, the identity is checked in exact rational arithmetic on hydrogenic functions
(I8b: Gᵏ(nℓ, nℓ) = Fᵏ(nℓ, nℓ), twenty equalities, 1s to 4f) after the Rᵏ implementation reproduces
five tabulated Condon–Shortley values exactly (I8), and the non-equivalent case is shown to differ at
every rank (I8c: eleven inequalities, F⁰(1s,2s) = 17/81 against G⁰(1s,2s) = 16/729).

**Disposition: a claim of the source that does not hold as printed.** The paper prints the split
(Corollary 1): an equivalent pair discards no independent quantity at any ℓ; a non-equivalent pair
discards ℓ + 1. "None at s/s and four at f/f" is not printed, and §8 says why. The source's
consequence — "the count of lost integrals is the count of failures: 5 of 5 s-block brackets, 0 of 1
f" — was never printed and is not now.

### 6. Claims of the source the paper omits or declines to read

- **Routing** — the four residuals (the 1.029 factor, the f corridor, the occupancy slope, the crossing
  charge) sent to a closed-seat property with a class (`chem_index.py` `R`, `CHEM`; Physics Compendium
  768–784; main volume 9726–9730). The first draft printed them as Table 3 and titled itself a
  "routing index". The audit (A-14, A-15, R-C14): the residuals are undefined in the paper, the
  numbers are uncomputed, the class record is outside the paper, and nothing measured any variation.
  **Withdrawn entirely**: no residual, no routing table, no routing figure; §9 says the index routes
  nothing. Obligation G7 stays in `check.py` (a check is never weakened) and the record says no
  sentence rests on it.
- **"c = 2 is the most particular domain"** read from *low* before *neutral* in the closing order
  (Physics Compendium 813). The audit (R-M8): the axis runs from the broadest domain upward, so the
  reading contradicts the direction. **Not printed**; §7 states the order and draws nothing from it.
- **The dissolution arithmetic** of the 1.029 residual, the f-corridor argument, "5 of 5 s-block
  brackets / 0 of 1 f", the three measured failure modes of the parameter index, and the per-parameter
  dependency counts — all outside `check.py`'s reach. **Not printed**, as before.
- **"A closed list"** of chemical properties (the source: "every chemical property demanded of a
  species was entered"). The audit (R-C1): standard tabulations carry properties the list omits.
  **Withdrawn**: §3 calls it the list as compiled.

## Interpretations chosen, and why

1. **The own box is the ambient grid for E.** As before (D2, D3); both fixed-box and own-box counts
   are printed in §2.
2. **"Minimum over every ordering" is the claim, and its base rate is the family closed under SOME
   ordering.** The first draft printed 5,824 of 2²⁴ (closed at one fixed ordering) as if it were the
   base rate; the audit (R-M4) named the right family. C3c enumerates it: 6,432 of C(24, 14) =
   1,961,256 fourteen-cell subsets of the 4 × 2 × 3 box, by taking every closed set of the box under
   all 288 relabellings. The paper reads Theorem 1 against that (Proposition 4) and keeps 5,824 only as
   the enumeration figure it is.
3. **What the closure consists of.** The valence seat is a full 4 × 3 block (B6), so E = 0 reduces to
   the two subvalence cells (Proposition 3, proved and measured: 30 of 66 pairs, exactly those sharing
   a coordinate, B8). The paper says this in the thesis, the abstract and §0, as R-M3 and R-R2 asked.
4. **What the closure rests on.** Seven sole-occupant cells; emptying three of them breaks closure
   (B7, B7b). The paper names the three and defends each in a sentence (Proposition 5); the
   coordination-number assignment is stated to be the least defended.
5. **The centrifugal barrier.** R-C2: not a symmetry label. Rather than reassign silently, D7 gains a
   second clause (a quantity fixed by a symmetry label alone) that licenses the entry, and the
   alternative reading is measured: as an energy, thirteen cells, no ordering closes (B9). Both are
   printed.
6. **The outer-seat labels are nominal.** R-C3: no Slater integral supplies a melting point. D10 now
   says the dependency is defined at the closed seats and nominal elsewhere; Theorem 2 is kept as a
   computation and its "boundary" reading dropped; Table 1's caption says the outer-seat kinds and
   dependencies are labels as compiled.
7. **The charge index on (role, regime).** R-M5: carrier is a bijective function of role and sign a
   function of role in the compiled table (H5b), so the four coordinates carry two; Theorem 4c is
   stated on the 4 × 3 box and the over-specification sentence is deleted.
8. **Theorem 7 demoted to a remark.** A-10: no map from an amplitude cell to (source, domain) is
   defined. H12 stays; the paper calls it a reading.
9. **The term-symbol fill is presented as non-unique** (F2c), as before.
10. **Table 2's ground terms are CITED, the species named, two cells marked "not consulted"**
    (R-C11); the paper takes no value from NIST ASD beyond the twelve terms.
11. **Sweeps are halved by Lemma 4 and the paper says so** (A-6): D5 counts reversal pairs twice, §2
    states the halving, Theorem 2's table prints the visited count (E4), and §10 names the four sweeps
    run in full (B3b, F2b, H10, J2).
12. **The idempotence obligation carries no hypothesis** (A-4): `observed(X)` was dropped from D2's
    idempotent claim, which holds over every subset with max ∅ = −∞; Lemma 2 says so.
13. **Every printed count is asserted, not merely printed** (A-2, A-3): B5, C1–C4, B2's sixteen, F1's
    twenty, F2b's 16/4, F2c, H3, H10, I3, I4b, B3c's forced/free structure, G3's 4,135, G4's 492, H4's
    864, H13's 17,280 and 13,824 all carry equalities.
14. **The verification record's D-labels** are `check.py`'s own and independent of §1's definition
    numbers; §10 says so in one line.
15. **Typography** (A-21 to A-27): no code spans remain in `PAPER.md`; every subscript and superscript
    is Unicode; the fixed-box operator is written ℛ(X; B) because Unicode has no subscript B, and the
    number of coordinates is n because it has no subscript d; the property the instrument labels
    "closed f shell n_f" is written "closed f-shell count" in prose and in `figures.py`; the sub-table
    headings are `###` headings so the template keeps them with their tables; the φ display block has a
    blank quoted line between its two lines; figure alt texts are empty so pandoc emits no second
    "Figure n" label; the term symbol is described in words (multiplicity, L and J).

## The repair (2026-09-24), in one place

`check.py` went from 75 to 96 obligations. Added: A6b (breadth as an axis, min E = 2), B3c (the
forced/free structure of the eight closing orders), B6 (full valence block), B7/B7b (sole occupants
and removal sweeps), B8 (the base rate beside a full block), B9 (the barrier as an energy), C3c (the
some-ordering base rate), D3 ×4 (ℛ(X) a sublattice, Lemma 2′), K1 (where ℛ sits), E4 (visited counts),
H5b (role/carrier bijection; the 4 × 3 charge box), H7b (region → low), I5b (rank lists), I6b (the
3-j closed form and column orders), I8 (CITED hydrogenic controls), I8b (equivalent electrons),
I8c (non-equivalent). Strengthened: B5 (asserts 1,482 and the size sequence), D2 (no hypothesis on
idempotence), J1 (the set identity, not sizes), G3/G4/H4/H13 (counts pinned), and every printed count
named in item 13 above. Nothing was weakened; G7 is retained. `figures.py`: the routing figure removed,
the defect figure and the merged-grid figure renumbered 2 and 3, the underscore label replaced.

## Figures

All three are computed by `figures.py` from `figures/check-results.json`, which `check.py` writes on
every run. Each was read back as an image and checked against the JSON and the captions.

- `fig1-chem-grid.png` — all fourteen occupied cells match `RESULTS["grid"]` under
  `ORD_K = [size, count, energy, symmetry]`, `ORD_P = [A, C, P]`; the dashed cell is (symmetry,
  valence, C); the subvalence label reads "closed f-shell count".
- `fig2-defect.png` — matches `got_filled` and `got_held`; the first blue value is 0 and draws no bar.
- `fig3-pca-grid.png` — matches `pca_table` and `L`/`U` at s = 0..3, at the universal-first closing
  ordering with neutral before hydrogenic; the caption says the other closing ordering swaps those
  two columns.

`FIGURES.tsv` carries one row per figure with the md5 of the file on disk.

## Lint and render

`python3 papers/method/lint.py papers/method/08-chemical-index` → 0 hits.
`python3 papers/method/render.py papers/method/08-chemical-index` → 26 pages. A pypdf text extraction
of the PDF finds 0 underscores, 0 carets, 0 backslashes and 0 asterisks; the pages were rasterised
and read (see `AUDIT.md`, "Repair record").
