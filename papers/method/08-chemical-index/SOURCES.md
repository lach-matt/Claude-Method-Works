# SOURCES.md — provenance map for 08-chemical-index (not published)

Paper: `PAPER.md`, "Closing the chemical properties: a routing index for the elements".
Drafted 2026-09-21 (resumed run; `check.py` and `figures.py` were already in the directory and were
built on, not rewritten). Every number in the paper is produced by `check.py` (75 obligations,
all discharged; `--selftest` adds three negative controls, all refuted) or is CITED.

`check.py` run: `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH; python3 check.py`
→ `summary: EXHAUSTIVE 52, MACHINE-CHECKED 8, SAMPLED 2, CITED 2, GUARD 11 / all obligations discharged`,
exit 0. `--selftest` → `GUARD 14`, exit 0. Both logs in the scratchpad
(`08-run.log`, `08-selftest.log`); the plain run is line-for-line identical to the earlier
`checks/08-chemical-index.log` except for wall-clock timings.

## Where each section draws on

| paper section | source passages (under `method/members/` unless stated) |
|---|---|
| Thesis, §0, Abstract | Physics Compendium 692–784 (Λ_chem: "Forty-two chemical properties of a species, indexed on what each one IS and on which of physics, charge or amplitude it supplies"; the three coordinates; the fifth seat; "E = 0 on fourteen cells"; the boundary table; the last cell; the routing table); Physics Compendium 784–841 (Λ_PCA: "Merged on that axis alone: E = 0 on nine cells"; the 4 × 6 multiplicity table; the per-atom calibration; Λ_amp); Index of Indices 1671–1751 (Λ_phys rebuilt, Λ_amp, Λ_PCA, Λ_chem — the same four statements in summary form) |
| §1 D1–D6 (index, box, ℛ, defect, ordering, staircase) | `tools/cypher.py` `op_order` (imported by path; `R(X) = {x in box : x_i <= phi_ij(x_j) for all i != j}`, `phi_ij(a) = max{y_i : y in X, y_j <= a}`) and `Index` (the own box is the product of the REALISED alphabets, `Index.box`); Mathematical Compendium 3580–3600 ("The staircase algebra of a closed index": `E(ℛ) = 0` iff the held set is an intersection of monotone staircases; "a closed index is therefore a system of inequalities and its cells are the lattice points satisfying them"); companion paper `papers/method/01-closure-law` (the closure law itself — cited in the paper as a companion, not restated) |
| §1 D7–D11 (kind, seat, fifth seat, dependency, Λ_chem) | `extracted/archives/restore-point-2-13/chem4.py` (`KIND`, `SEAT`, `PCA`, and the 42-row table `C` of (name, kind, seat, dependency) — read as a literal by `ast`, never executed); Physics Compendium 711–730 (the three coordinates in prose; "Twelve of the forty-two are properties of MATTER IN BULK") |
| §1 D12 (residual, routing) | `extracted/archives/restore-point-2-13/chem_index.py` (the docstring "Repeatedly in the Loewdin work a residual has been left unexplained because I looked for a universal account of it"; the `R` table of four residuals; the closing paragraph "before calling a residual unexplained, look up which chemical property supplies it and which class it holds on"); Physics Compendium 768–784 |
| §1 D13, §9 (Slater integrals) | `extracted/archives/restore-point-2-13/amp_index.py` (`integrals(l1,l2)`, `PAIRS`); Physics Compendium 815–841; Mathematical Compendium 3604–3620 ("The Slater triangle, and a parity defect resolved") |
| §2 (Lemmas 1–4, the closed families) | `research/warp-drive/prover.py` (`in_R`, `observed`, `contains`, `prove`, `non_vacuous`, `encoding_matches` — imported by path); Ganter's next-closure implemented fresh in `check.py`; the brute-force count over every subset of a box in `check.py` (numpy, bit-parallel) |
| §3 Table 1 | `chem4.py` `C` for kind/seat/dependency; `chem3.py` `C` for the breadth coordinate (checked A6 to name the same 42 with the same kind and seat); the "what it is" column is written here as standard physical chemistry and is not taken from any table; the source column is discussed below |
| §4, §5, §6 | `chem4.py` (the closure and the min-E sweep); Physics Compendium 733–767 (the boundary table and "The last cell, and what filled it": "All 1,440 orderings of the three axes give minimum E = 1"; the ground-term table at Nₑ = 20, 38, 56, 88) |
| §7 | `chem_index.py` `R` (the four residuals with property, class and reason) and `CHEM` (property → supplies → class → measured); Physics Compendium 768–784; main volume 9726–9730 ("Λ_chem dissolved two residuals") |
| §8 | `phys_close.py` `P` (the 22 rows, source/domain/arity/real?); `charge_index.py` `CH` (the nine occurrences); `dom_reg.py` `PH`, `CH`, `D` (the merge on `domain ≡ regime`); `recovered/merge.py` `PH`, `CH` (the earlier merge on identified axis names); Mathematical Compendium 3592–3600 (`L(s) = ⌊s/2⌋`, `U(s) = s + ⌊s/3⌋`); Index of Indices 1671–1682, 1697–1716 |
| §9 | `amp_index.py`; the 3-j symbol implemented fresh in `check.py` by Racah's formula in exact `Fraction` arithmetic |
| §10, §11 | the check's own output; no source passage |

All instruments named above are read **by path**, as literals via `ast.literal_eval`, or imported by
path. Nothing is copied into `check.py`; the one fresh implementation is `ref_R`, the independent
witness-form staircase written for the encoding guard, which is the point of a guard.

## What did not reproduce, and how the paper handles it

### 1. The printed boundary table mixes two property tables (obligations E1, E2, E3)

The source prints, as one table,

| seats included | cells | E |
|---|---|---|
| subvalence + valence | 14 | 0 |
| + the core | 15 | 3 |
| + the nucleus | 20 | 8 |
| + the aggregate | 21 | 11 |
| all five | 26 | 19 |

Recomputed, that sequence is **not** one table. With the term symbol on a charge role (the
assignment the closure needs, §6 of the paper) the five rows are **14/0, 16/2, 21/7, 22/10, 27/18**.
With the term symbol on a physics parameter (the assignment before the fill) they are
**13/1, 15/3, 20/8, 21/11, 26/19**. The printed table is the *first* row of the filled table above
the *last four* rows of the unfilled one — obligation E1 asserts exactly that and passes.

**Disposition: a claim of the source that does not reproduce as printed.** The check is not at
fault; the two tables are each reproduced exactly. The paper prints **both** tables in §5 and in
Figure 3, says which is which, and never prints the mixed sequence. The qualitative statement the
source draws from the table — that the defect climbs monotonically as foreign seats are added —
reproduces in both tables and is what §5 claims.

### 2. The single defect cell of the amplitude index on the raw rank (obligations I4, I4b)

The source states: "Indexed on the raw rank the single defect is **F¹**, a term parity forbids."
Recomputed on the cell set `amp_index.py` builds — the diagonal pairs plus the eleven listed
occupied/rival pairs, indexed on (raw rank k, kind, ℓ of the rival), 21 cells — the minimum defect
over all 5,760 orderings is 1, as stated, but at both minimising orderings the single added cell is
**G¹ at ℓ = 0 (an s rival)**, not F¹. Both are ranks the parity rule forbids where they appear
(for ℓ = ℓ′ = 0 the exchange ranks run from 0 to 0, and 1 is odd; F ranks are always even), so the
*reading* the source takes from the defect survives, but the cell does not.

**Disposition: a claim of the source that does not reproduce.** The paper prints the reproduced
cell, `G¹ at ℓ = 0`, in Theorem 6, with the parity argument for that cell. F¹ is not printed.
The check was not altered; `I4b` pins the reproduced cell so that a future change would fail rather
than pass silently.

### 3. "All 1,440 orderings" (obligations B2, B2b, F1)

The source says 1,440 orderings of the three axes. The realised values at the two closed seats are
four kinds (the kind *rate* is unrealised there), two seats and three dependencies, so there are
4! · 2! · 3! = **288** orderings, not 1,440. The figure 1,440 counts 5! on the kind axis, i.e. it
permutes the unrealised fifth kind as well; 1,440 = 288 × 5. A value no cell realises cannot change
ℛ, so the two counts give the same minimum. **Disposition: not a discrepancy but an ambiguity in
what is being counted.** The paper states 288 as the family, and says in Theorem 1 that the 1,440
are the same 288 counted five times.

### 4. One parameter's domain differs between the two tables that feed the merge (obligation H7)

`phys_close.py` gives `C′ = 1` the domain *all elements*; `dom_reg.py`, which supplies the merge,
gives it the merged domain *low*. Sources agree on all 21 parameters; domains on 20 of 21.
**Disposition: recorded, not repaired.** The paper states the disagreement in §8 and shows it does
not move any cell: (this work, all elements) is occupied by two other items and (this work, low) by
four others, so the nine cells and E = 0 are the same under either assignment. That argument is read
off `RESULTS["pca_names"]`, which `check.py` dumps, and off Table 4, which the paper prints.

### 5. Claims of the source that `check.py` does not reproduce and the paper therefore omits

- **The dissolution of the 1.029 residual.** The source states that the 1.029 factor "was
  arithmetic: the excess above U is 0.028 of the spread at p and 0.785 at d, a ratio of 27.7, and
  the apparent 2.9% agreement came from comparing a ratio at p, where t ≈ 1, with a ratio at d,
  where t ≈ 1.78." None of 0.028, 0.785, 27.7, 2.9%, 1.78 is computed by `check.py`; the corridor
  machinery they rest on is outside this paper. **Not printed.** §7 states only that what happens to
  a residual after routing is not decided by the index.
- **The dissolution of the f-corridor residual** ("p = 0 is the node floor, so no rival lies below
  and L = −∞"). This is a statement about the corridor, an object this paper does not define.
  **Not printed**, for the same reason.
- **"5 of 5 s-block brackets threaded, 0 of 1 f."** A measurement over the bracket test, not
  reproduced here. §9 prints only the integral counts that `check.py` computes (`s/s`: one F and one
  G; `f/f`: four and four) and the consequence that an exchange-dropping rule discards none and four
  respectively. The bracket counts are **not printed**.
- **"a per-core constant reproducible within a species to two decimals", "1.25 times"** and the rest
  of the three measured failure modes of the parameter index (Physics Compendium 680–692). Outside
  this paper's scope; treated in the companion paper on the polarisation ratio. **Not printed.**
- **The dependency counts "objects rest on it"** (66, 72, 18, …, Physics Compendium 371–400). The
  paper's Theorem 4b says only that adding an arity axis costs a minimum defect of 7, which is
  reproduced; the individual dependency counts are **not printed**.

## Interpretations chosen, and why

1. **The own box, not a fixed box, is the ambient grid for E.** `cypher.py`'s `Index` builds its
   alphabets from the realised values, so `ℛ` and hence `E` are computed over the own box. The
   paper makes this explicit (D2, D3) because the distinction changes the numbers: over the 4 × 6
   box 9,115 subsets are closed as subsets of that fixed box and 27,477 are closed over their own
   box. Both counts are printed in §2.
2. **"Minimum over every ordering" is the claim, and the closing orderings are enumerated.** The
   source states E = 0 at a declared order. The paper states it as a minimum over an exhaustively
   visited family and then prints *which* orderings close (§4), because that is where the content
   is: closure forces three of six binary order choices and leaves the other three free.
3. **The 42 properties' "public data source".** No source is named for any of the 42 in the tables
   the index is built from. The paper therefore names a source only where one is independently
   established: the observed ground configuration and the three counts read off it (node count p,
   valence electron count, closed f shell n_f), the ionisation energy, and the ground term — six
   properties, all NIST ASD, the last of which `check.py` marks CITED at obligations F4/F5. The
   other thirty-six carry a dash and the paper states in §0 and §3 that no source is named for them
   and that it takes no numerical value from them. **Nothing was invented.**
4. **The term-symbol fill is presented as non-unique.** The source presents the fill as *the* answer.
   Obligation F2c shows a second single change that also closes the index at fourteen cells. The
   paper states both (Theorem 3, clause 4) and says the evidence for the change made is Table 2 and
   nothing else.
5. **Table 2's ground terms are CITED, not recomputed.** The twelve term symbols are public values.
   `check.py` verifies only the two decidable relations among them (the Nₑ = 20 and Nₑ = 38 rows are
   identical; no sequence is constant). The paper marks the table CITED and says what is verified.
6. **Λ_charge's box.** `check.py` reports box 96 = 4 × 4 × 2 × 3 for the nine occurrences, which is
   the realised box (every value of every one of the four coordinates is realised). The paper prints
   96 and the nine cells.
7. **The merged index's box is 20, not 24.** *One species* is unrealised, so the own box is 4 × 5.
   The band `L(s) ≤ d ≤ U(s)` is a statement about the full 4 × 6 grid and is verified there
   (H11, 24 cells). The paper keeps the two statements apart.
8. **"The last four" of the verification record's D-group labels collide with the paper's definition
   numbers D1–D13.** `check.py`'s obligation tags are kept verbatim, as the brief requires, and §11
   says in one line that the labels are the verification's own and independent of §1's definitions.
   `check.py` was not edited to rename them.

## Figures

All four are computed by `figures.py` from `figures/check-results.json`, which `check.py` writes on
every run. Each was read back as an image and checked cell by cell against the JSON before the
captions were written.

- `fig1-chem-grid.png` — verified: all fourteen occupied cells match `RESULTS["grid"]` under
  `ORD_K = [size, count, energy, symmetry]`, `ORD_P = [A, C, P]`, `ORD_S = [subvalence, valence]`;
  the dashed cell is (symmetry, valence, C). No change needed.
- `fig2-routing.png` — **regenerated.** The existing plate was broken: `fig2()` placed a property
  box at the mean y of the rows routing to it, which put "subshell radius" (mean of rows 0 and 2)
  and "centrifugal barrier" (row 1) at the same y, so the two boxes and their label text were drawn
  on top of one another and neither was legible. `figures.py`'s `fig2()` was rewritten to give each
  property its own non-overlapping slot. The data it draws are unchanged (`RESULTS["ROUTE"]`).
- `fig3-boundary.png` — verified against `got_filled` and `got_held`. No change needed.
- `fig4-pca-grid.png` — verified against `pca_table` and against `L`/`U` at s = 0..3. No change
  needed.

`FIGURES.tsv` carries one row per figure with the md5 of the regenerated file.

## Lint and render

`python3 papers/method/lint.py papers/method/08-chemical-index` → 0 hits.
`python3 papers/method/render.py papers/method/08-chemical-index` → PDF, page count in the report.
