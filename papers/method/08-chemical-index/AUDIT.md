# AUDIT — 08-chemical-index

Paper: `PAPER.md`, "Closing the chemical properties: a routing index for the elements" (610 lines).
Audited 2026-09-24 against `SOURCES.md`, the source passages it names, `check.py` (plain and
`--selftest`), the four figures, `lint.py`, and the rendered HTML/PDF (`out/08-chemical-index.pdf`,
23 pages). Not published. Nothing in `PAPER.md` or `check.py` was edited.

Runs (PATH with `method/bin` first, Python 3.12):

- `python3 check.py` → `summary: EXHAUSTIVE 52, MACHINE-CHECKED 8, SAMPLED 2, CITED 2, GUARD 11 /
  all obligations discharged`, exit 0, 42 s wall.
- `python3 check.py --selftest` → the same plus N1, N2, N3 all `ok`; `GUARD 14`, exit 0.
- `python3 papers/method/lint.py papers/method/08-chemical-index` → 0 hits.
- Figure md5s in `FIGURES.tsv` match the files on disk (all four).
- An independent enumeration written for this audit (witness-form ℛ, all 288 relabellings)
  reproduces the sixteen closing orderings of the fourteen cells and the four closing orderings of
  the alternative fill, and reproduces the §4 description of the eight sub < val closing orders
  exactly.

Note on the scratchpad: the shared scratchpad already held `check.out` from another paper's audit;
this audit's logs are `p08-check-6775.out` and `p08-selftest-6775.out`.

---

## Part A — content audit

### A.1 Definitions, results and numbers against the sources and the check

Source abbreviations: PC = Physics Compendium volume, II = Index of Indices volume, MC =
Mathematical Compendium volume, MAIN = main volume; instruments under
`extracted/archives/restore-point-2-13/` and `recovered/merge.py` as `SOURCES.md` names them.

| paper item (line) | source | paper vs source | check | verdict |
|---|---|---|---|---|
| D1–D4 index, box, ℛ, defect (60–72) | `tools/cypher.py` `op_order`, `Index.box`; MC 3580–3590 | same operator (own box, max-form); paper adds the own-box/fixed-box distinction the source leaves implicit | G1, G2, G3 | agrees |
| D5 orderings, `∏|A_i(X)|!` (74) | — (paper's own) | — | B2 counts 288 | agrees |
| D6 staircase system (76–78) | MC 3580–3586 "intersection of monotone staircases" | equivalent, made precise (f_ij with −∞) | D1 | agrees |
| D7 kind, D8 seat, D9 fifth seat, D10 dependency (80–98) | PC 711–730; `chem4.py` `KIND`, `SEAT`, `PCA` | names identical; the one-line glosses of each kind are the paper's own | A2, A3, A5 | agrees; see R-C2 |
| D12 residual, routing (102) | `chem_index.py` docstring and closing paragraph; PC 768–784 | paper's definition is stronger (species-indexed, reproducible; "admissible" is the paper's word) | G7 | admissibility relies on a record not in the paper — A-14 |
| D13 Slater integrals (104) | `amp_index.py` `integrals`; PC 815–820; MC 3604–3612 | same enumeration; CITED Slater 1929, Condon & Shortley 1935 | I5 | agrees |
| Lemma 1 witness form (112–116) | `cypher.py` (max form); `prover.py` `in_R` (witness form) | proof complete | G1, G2 | PROVED; complete |
| Lemma 2 closure operator (118–124) | — | proof complete | D2 ×4 | PROVED; MACHINE-CHECKED claim overstated for (iii) — A-4 |
| Lemma 3 staircase law (126–128) | MC 3580–3586 (stated, not proved there) | proof complete both directions | D1 ×4 (⇐ only) | PROVED |
| Lemma 4 reversal (132–136) | — | proof complete | J1 (sizes only), J2 | PROVED; A-5 |
| closed-family table (140–148) | — | — | C1, C1b, C2, C3, C3b, C4, B5 | values printed by the check; only agreement is asserted — A-2, A-3 |
| Prop. 1 census 9/8/8/11/6, 6/2/2/20/12, (16,10,16)/(15,11,16) (225) | `chem4.py` `C` | recomputed row by row here: agrees | A1–A4 | agrees |
| Prop. 2 the twelve bulk properties (227) | PC 722–726 (lists eleven names, "electrical and thermal conductivity" as one item) | agrees; the source's "eleven hand-picked" refers to an earlier list | A5 | agrees; tautology — R-M6 |
| breadth coordinate (231) | `chem3.py` `C` | A6 verifies same 42 with same kind and seat | A6 | "constrained by the other coordinates" not measured — A-9 |
| Table 1, 42 rows (156–223) | `chem4.py` `C` | every (name, kind, seat, dep) checked against the literal here: 42/42 agree, term symbol at C as the fill | A1–A5 | agrees |
| "six carry a named public source" (43, 156) | no source named in `chem4.py`/`chem3.py` for any row | paper names NIST ASD for six; true that the instruments name none | — | agrees; see R-C6, R-C7 |
| Theorem 1 (237–244): 14 cells, box 24, 288 orderings, E = 0, sixteen close | PC 733–735 "E = 0 on fourteen cells"; PC 757 "1,440 orderings" | paper's 288 is the realised-value family; 1,440 = 5!·2!·3! permutes the unrealised kind | B1, B1b, B2, B2b, B3, B3b | agrees; A-16 |
| staircase written out (248–257) | `check.py` phi tables | φ tables `kind<-seat [1,3]`, `pca<-seat [0,2]`, others constant: agrees with the paper's two functions | B4 | agrees |
| the eight closing orders (259–265) | — | reproduced independently here | B3b (count only) | structure printed, not asserted — A-3 |
| E = 0 over a named family, 5,824 / 8,590 (271) | — | — | C3, C3b | A-3 |
| Theorem 2 table (279–289) | PC 736–746 prints 14/0, 15/3, 20/8, 21/11, 26/19 | **source does not reproduce**: it is the filled first row over the unfilled last four (E1). Paper prints both real tables — correct handling | E2, E3, printed rows | agrees with the check; A-1, A-6 |
| "differ in every row" (293) | — | 14/16/21/22/27 vs 13/15/20/21/26: true | E2, E3 | agrees |
| Theorem 3 (305–312): 13 cells, minE 1, 20 minimise, 16/4, alt fill closes in 4 | PC 757–759 "All 1,440 orderings … minimum E = 1 … the cell is symmetry × valence × charge" | paper is stronger and more honest: the source names one cell, the check finds two; the paper prints both | F1, F2, F2b, F2c, N1 | agrees; nc_alt = 4, 16/4, 20 printed not pinned — A-3 |
| four symmetry properties on P or A (316) | `chem4.py` rows | agrees | F3 | agrees |
| Table 2 ground terms (320–329) | PC 762–767 (identical table) | identical; CITED NIST ASD | F4, F5 | agrees; see R-P4 |
| Table 3 routing (341–348), Prop. 3 | `chem_index.py` `R`, `CHEM`; PC 770–777 | identical rows; class column from `CHEM` | G7 | agrees; A-14, A-15 |
| §8.1: 22 listed, one excluded, 21 (368) | `phys_close.py` `P` (`5σ threshold` real? = False) | agrees | H1 | agrees |
| Theorem 4a: 7 cells, box 12, E = 0, 4 of 144 (372) | `phys_close.py` (E2 = 0 without arity) | recounted here from `P`: 7 cells, box 4×3 | H2, H3 | 4 of 144 printed not pinned — A-3 |
| Theorem 4b arity: 12 cells, minE 7 over 864 (374) | `phys_close.py` (source, domain, arity) | agrees | H4 | agrees |
| Theorem 4c: nine occurrences, nine cells, box 96, 2/3/4 (380) | `charge_index.py` `CH` | recounted here: agrees | H5, H6 | agrees; content trivial — R-R7 |
| Theorem 4 merge: 9 cells, box 20, 4 of 2,880, low before neutral (388) | `dom_reg.py` `PH`, `CH`; PC 784–800 "E = 0 on nine cells" | agrees; the two universal-first closing orders differ only in neutral/hydrogenic order | H8, H10, H10b | agrees; ncm = 4 printed not pinned — A-3; interpretation — R-R8 |
| Table 4 multiplicities (392–397) | PC 790–796 (identical table) | recounted here from `PH` + `CH`: 5 / 3,1 / 7,1 / 2,5,2,4 = 30 | H9 | agrees |
| Theorem 4d band L, U (405–411) | MC 3592–3600 | identical | H11, N3 | agrees; proof complete |
| name-merge 13/E=6, 18/E=11 (419) | `recovered/merge.py`; II 1712–1716 | agrees | H13 | agrees |
| one domain differs, C′ = 1 (421) | `phys_close.py` (3,1) vs `dom_reg.py` (3,3) | agrees; the "does not move a cell" argument checked against Table 4 here: (this work, all elements) = {a amplitude, β}, (this work, low) = {h₀, C′, three charge occurrences} | H7 | agrees |
| Theorem 5: 20 cells, box 32, triangle, 4 of 1,152 (429–433) | PC 822–826; MC 3596; `amp_index.py` | agrees | I1, I2, I3 | 4 of 1,152 printed not pinned — A-3 |
| Theorem 6: 21 cells, minE 1 over 5,760, defect **G¹ at ℓ = 0** (435) | PC 826 and II 1690 and MC 3616 all print **F¹** | **source does not reproduce**: the check finds G¹ at an s rival at both minimising orderings; paper prints the reproduced cell | I4, I4b | correct handling; A-19 |
| Lemma 5: (ℓ 0 ℓ; 0 0 0)² = 1/(2ℓ+1) (439–443) | PC 833–838; MC 3613–3615 ("1, 1/3, 1/5, 1/7 to machine precision") | paper's exact-rational version is stronger; **the cited closed form in the proof is malformed** | I6, I7 | A-7 |
| Corollary 1: s/s {F⁰},{G⁰}; f/f four each; "discards no … at s/s and four at f/f" (447) | PC 828–830 "at s/s the exchange G⁰ IS the direct F⁰ … at f/f it discards four independent quantities" | paper drops the source's reason (G⁰ = F⁰) and keeps the conclusion | I5 (counts only) | the physics is wrong as stated — A-8 (BLOCKING) |
| Theorem 7: amplitude contributes (mathematics, universal), (mathematics, all elements) (449) | `check.py` comment "three_merge.py's reading"; not in `SOURCES.md`'s table for §9 | no source passage; the map from an amplitude cell to (source, domain) is not defined in the paper | H12 (two named cells ∈ merge) | A-10 |
| §11 counts 52/8/2/2/11 = 75; three controls (471) | check output | recounted from the record's tables: 6+8+2+6+2+8+8+3+7+1+14+8+2 = 75 | summary line | agrees |
| G3 4,135 cells, G4 492, Z3 5.1.0 (510–528) | check output | agrees | G3, G4 | agrees |

Claims of the source that the paper omits (SOURCES.md §5): the 1.029 dissolution arithmetic, the
f-corridor argument, "5 of 5 s-block brackets / 0 of 1 f", the three measured failure modes, the
dependency counts. Confirmed absent from `PAPER.md`. Correct.

### A.2 The Z3 obligations and their guards (`check.py` lines 497–587)

Eight obligations, D1 ×4 and D2 ×4, over the boxes 4×2×3, 4×5, 4×6, 2×4×4 — the four boxes the
paper names (§2 Lemma 2, Lemma 3, §11 D-table). Each is reported only after G3, G4, G5 ×4, G6 ×4
have run; `report()` records a failed guard as a failure and the summary exits 1, so a guard
failure cannot be silent.

- **D1** (`staircase_closed`): hypothesis = monotone `f_ij` into `{−1, …, |A_i|−1}` (−1 encodes
  −∞), `X = X(f)` cell by cell, and `observed(X)`; conclusion `in_R(X, x) == X[x]` for every cell.
  This is Lemma 3 (⇐) restricted to value-realising X, which is exactly what line 128 states.
  Encoding: `in_R` is the witness form of Lemma 1, not the max form of D3; the equivalence is
  Lemma 1 (PROVED) and G3 tests it concretely. Box named. Correct.
- **D2** (`extensive_monotone` and `idempotent`): extensivity and monotonicity carry no
  hypothesis; **idempotence carries `observed(X)`**. Lemma 2 (line 118–122) is stated for all
  `X ⊆ B` and the MACHINE-CHECKED sentence says "the set variable ranging over all 2²⁴ … subsets".
  For (iii) the effective range is the value-realising subsets. See A-4.
- **G5/G6** (non-vacuity): a staircase system strictly inside the box, and an observed X strictly
  inside the box, each shown satisfiable per box. Adequate for D1 and for the idempotence half
  of D2; the extensive/monotone half has no hypothesis to be vacuous.
- **G3/G4** (encoding fidelity): `prover.encoding_matches` compares `in_R` evaluated concretely
  against `ref_R_fixed` on 300 random instances over the four boxes (4,135 cells), and G4 shows a
  reference with one pair direction dropped is caught (492). Note `encoding_matches` evaluates the
  *Python* witness predicate, not the z3 term; the z3 term `in_R` is the same expression built
  symbolically, so fidelity is by construction plus this concrete test. Acceptable; the record
  should say so (A-4 resolving text covers it).
- **N2** (selftest): "every observed subset is closed" refuted on 3×3 by counterexample. The
  negative control exercises the same `prove` path. Correct.

No MACHINE-CHECKED claim in the paper names a box the check does not cover.

### A.3 Figures against captions and text

- **Figure 1** (fig1-chem-grid.png, read): two 4×3 panels; kinds size < count < energy < symmetry
  upward, dependencies amplitude < charge < physics rightward; subvalence panel holds "closed f
  shell n_f" at (count, A) and "lanthanide contraction" at (size, A); valence panel holds every
  cell with the correct property names (checked against `RESULTS["grid"]` and Table 1); dashed
  orange cell at (symmetry, valence, charge role). Matches caption and §4. Defects: "n_f" with a
  literal underscore in the figure; the "lanthanide contraction" label overflows its cell slightly
  at print size (legible).
- **Figure 2** (fig2-routing.png, read): four residuals, three property boxes with cell labels,
  three classes; two arrows into "subshell radius". Matches Table 3. Defects: "t(l)" in the figure
  against "t(ℓ)" in Table 3; "0.021-0.243" (hyphen) and "2,3,5" against Table 3's "0.021–0.243"
  and "2, 3, 5"; "n_f" underscore.
- **Figure 3** (fig3-boundary.png, read): five groups, blue 0/2/7/10/18 with (14/16/21/22/27
  cells), orange 1/3/8/11/19 with (13/15/20/21/26 cells). Matches caption, Theorem 2 and E2/E3.
  Labels legible; the "(14 cells)" label sits over the zero-height blue bar as the caption warns.
- **Figure 4** (fig4-pca-grid.png, read): 4×6 grid, multiplicities 5 / 3,1 / 7,1 / 2,5,2,4 in the
  nine cells, L(s) path on the left edge and U(s) on the right edge of the occupied band, column
  "one species" empty. Matches Table 4 and Theorem 4d. Neutral drawn before hydrogenic — one of
  the two universal-first closing orders (H10 output); the caption does not say the other closing
  order swaps them (minor).

`FIGURES.tsv` rows and md5s agree with the files.

### A.4 Lint

0 hits.

### A.5 Typography in the rendered PDF and HTML

Rendered pages read as images (23 PDF pages via PyMuPDF at 96 dpi; HTML via headless Chromium at
1000×16000 sliced to 1000×1400). Defects visible on the page:

- **Literal backslashes** in the §11 J-table, row J1: the claim cell renders as
  `\|ℛ(X)\| = \|ℛ(σX)\|` (PDF p.22, HTML). Source line 579 escapes the pipes inside a code span;
  inside backticks pandoc keeps the backslash. (A-21)
- **Carets and braces as superscripts**: `^{2S+1}L_J` is printed verbatim in code font in Table 1
  (term symbol row, p.8) and in §6 line 318 (p.12/13). `F^k`, `G^k`, `F^0, F^2, F^4` in D13 and
  §9 render as carets. (A-22)
- **Underscore subscripts throughout the definitions and proofs**: `x_i`, `y_j`, `φ_ij`, `f_ij`,
  `A_i(X)`, `Λ_chem`, `E_(X)`, `minE(Λ₁₃)`; the property name "closed f shell n_f" carries a bare
  underscore in prose (Table 1, Table 3, both figures). `Λ₁₃` in monospace renders with a visible
  gap ("Λ₁ ₃", p.12). PAPER-SPEC §9 allows backticks for subscripts; the brief's criterion is the
  page, and on the page these are underscores. (A-23)
- **Orphaned headings at page feet**: "(a) the nucleus — six properties" ends p.6 with the table
  on p.7 and half of p.6 blank; "(d) the valence shell — twenty properties" ends p.7 likewise;
  "D · the solver obligations (…)" ends p.19; "J · the reversal symmetry" ends p.21. These are
  bold paragraphs, not headings, so the template's `page-break-after: avoid` does not reach them.
  (A-24)
- **Displayed block run together**: the two φ lines of the staircase (lines 250–251) are two `>`
  lines with no blank line between them and render as one wrapped line:
  "φ_{kind ← seat} : subvalence ↦ count, valence ↦ symmetry φ_{dep ← seat} : subvalence ↦ A,
  valence ↦ P" (p.10). (A-25)
- **Duplicate figure labels**: every figure shows a small "Figure n" line (pandoc's implicit
  figure caption from the alt text) immediately above the bold "Figure n." caption paragraph
  (pp.11, 12, 14, 16). (A-26)
- "the functionsφ_ij of D3" — the space before the code span collapses on p.10 (kerning of the
  serif/mono boundary); minor, same fix as A-23.
- Tables fit their columns; no cell is clipped; all four figures appear at legible size with their
  captions on the same page; no page of the record's tables splits a row.

### A.6 Findings from Part A

| id | line(s) | severity | finding | resolving change |
|---|---|---|---|---|
| A-1 | 536 | MINOR | Obligation E1's row prints the sequence "14/0, 15/3, 20/8, 21/11, 26/19", which is the source's spliced table and appears nowhere else in the paper; a reader cannot tell what it is or why it is checked. | Either drop E1 from the record or word the row as "a splice of the filled first row over the unfilled last four rows is not either table" without printing the spliced numbers. |
| A-2 | 148, 495 | MAJOR | B5 is reported with `ok=True` unconditionally (`check.py` line 332–333). The figure 1,482 and the size sequence 1, 14, 70, 176, 270, 288, 242, 175, 114, 66, 37, 17, 8, 3, 1 (line 148) are computed but never asserted; the sequence is not even printed to the log (JSON only). A drift would pass green. | Assert `n_closed_sub == 1482` and `closed_sizes == {…}` in B5 and print the sequence in the detail. |
| A-3 | 27, 40, 148, 241, 259–265, 271, 310, 372, 388, 429, 459, 503–508, 553–568 | MAJOR | Printed, not pinned: 5,824 / 8,590 / 9,115 / 27,477 / 3,449 / 7,887 / 33 / 38 / 29,067 (C1–C4 assert only agreement between two methods or `> 0`), "sixteen close" (B2 asserts minE and 288 only; sixteen follows from B3b + Lemma 4), "20 minimise" (F1), 16 / 4 (F2b asserts `nA > 0 and nB > 0`), "four of 288" (F2c), "four of 144" (H3), "four of 2,880" (H10 asserts `mEm == 0`), "four of 1,152" (I3), "2 minimising" (I4b detail), and the structural description of the eight closing orders (261–263, asserted nowhere; B3b pins the count 8 and prints the orders). Every one is on an output line, so the paper's numbers match the log today, but the check does not fail when they move. | Pin each printed count as an equality in its obligation; add an obligation asserting the three forced/free properties of the eight closing orders. |
| A-4 | 122, 518–521 | MINOR | Lemma 2 says MACHINE-CHECKED "with the set variable ranging over all 2²⁴ … subsets"; the idempotence obligation (`idempotent`, line 540–543) carries the hypothesis `observed(X)`, so (iii) is discharged only for value-realising X. (i) and (ii) carry no hypothesis. | State in Lemma 2 and in the D2 rows: "(i), (ii) over every subset; (iii) over every value-realising subset", or drop `observed` from `idempotent` (the fixed-box operator with max ∅ = −∞ is idempotent without it). |
| A-5 | 134, 579 | MINOR | Lemma 4 asserts `ℛ(σX) = σ(ℛ(X))`; J1 samples only `|ℛ(X)| = |ℛ(σX)|`. The record's J1 row is honest about this; the sentence at line 134 ("corroborated SAMPLED") is not. | Either test the set identity in J1 or say at line 134 that the sampled corroboration is of the size equality. |
| A-6 | 289, 537–538 | MAJOR | "EXHAUSTIVE at every row: every ordering of the realised values is visited, the count in the fifth column." The sweep (`sweep`, `use_symmetry=True`) visits half the orderings of the last axis and doubles the counts by Lemma 4 (line 156–157). For 864, 17,280 and 86,400 the visited count is half; J2 verifies the halving only on the 288 case. Lemma 4 is PROVED so the inference is sound, but the sentence is false as written, and the same wording is used at lines 241–244 and 307. | Say "visited up to the reversal symmetry of Lemma 4 (half the orderings of one axis are visited and each stands for its reversal)" at Theorem 1, 2 and 3, and print the visited count beside the family size. |
| A-7 | 443 | MAJOR | Lemma 5's proof cites "(j 0 j; m −m 0) = (−1)^{j−m}/√(2j+1)". With j₂ = 0 the middle projection must be 0, so the symbol as printed is not a valid 3-j symbol. The correct closed form is (j j 0; m −m 0) = (−1)^{j−m}/√(2j+1) (Edmonds 1957 eq. 3.7.7), or equivalently (j 0 j; m 0 −m) = (−1)^{j−m}/√(2j+1) up to the column-permutation sign. The check (I6) computes (ℓ 0 ℓ; 0 0 0)² correctly; the printed formula does not. | Replace the cited form with (j j 0; m −m 0) = (−1)^{j−m}/√(2j+1) and note that (ℓ 0 ℓ; 0 0 0) is a column permutation of (0 ℓ ℓ; 0 0 0), the symbol that actually carries the s–ℓ exchange (rank k = ℓ). |
| A-8 | 447 | BLOCKING | Corollary 1 states that a rule which drops exchange "discards no independent radial quantity at s/s and four at f/f", and says the count "is read off D13 with no fitting". D13 enumerates {F⁰} and {G⁰} at s/s, so from D13 alone dropping G⁰ discards one quantity. The source's reason — G⁰(ns, ns) = F⁰(ns, ns) — holds for *equivalent* electrons (same n and ℓ), and for equivalent electrons it holds at every rank: G^k(nℓ, nℓ) = F^k(nℓ, nℓ) for all k (Slater 1929; Condon and Shortley 1935; Cowan 1981 §6-4). So under the equivalent-electron reading f/f discards nothing independent, and under the non-equivalent reading (nℓ, n′ℓ) s/s discards one. Either way one clause is false, and the conclusion is printed as a physical result under EXHAUSTIVE. | Restate D13's diagonal pair as (nℓ, nℓ) or (nℓ, n′ℓ) explicitly; if equivalent, the corollary becomes "the exchange list duplicates the direct list at every ℓ, so a closed shell's exchange costs no independent quantity at any ℓ" and the f/f clause is withdrawn; if non-equivalent, the s/s clause becomes "one". Add the identity as a CITED statement with Cowan (1981). Re-audit §9's closing sentence of Theorem 6's paragraph accordingly. |
| A-9 | 231 | MINOR | "its values are constrained by the other coordinates rather than free of them" is asserted for breadth and not measured; only the amplitude analogue (§9) is measured. `chem3.py`'s min-E sweep over (kind, seat, breadth) would measure it in seconds. | Either add the breadth sweep as an obligation and print its minimum defect, or soften to "was not adopted; the analogous coordinate of §9 is measured". |
| A-10 | 449, 564 | MAJOR | Theorem 7 assigns the amplitude index two (source, domain) cells and calls the result EXHAUSTIVE, but the paper defines no map from a cell (kind, ℓ, i) of the amplitude index to a (source, domain) pair; the two cells are a declaration inside `check.py` (comment: "three_merge.py's reading"), and `SOURCES.md` names no source passage for it. H12 checks only that two named cells lie in the merge. | Either define the map (e.g. "every Slater integral is an exact consequence of the formalism, source *mathematics*; F⁰ is asserted for every species, higher ranks for elements with ℓ ≥ 1, hence *universal* and *all elements*") and check it row by row, or demote Theorem 7 to a remark and remove EXHAUSTIVE. |
| A-11 | 27 | MINOR | "the two innermost open seats — the subvalence shell and the valence shell". They are the two outermost shells, and by D8 the subvalence shell is part of the closed core, so neither "innermost" nor "open" is right. | "the two outermost shells" or "the two shells nearest the valence electrons". |
| A-12 | 33 | MINOR | "the alternative that was not tested" — the alternative was tested (F2c, Theorem 3 clause 4) and not adopted. | "the alternative that was not adopted". |
| A-13 | 86–92 | MINOR | D8 says every property has exactly one seat, but the seats as defined nest: the subvalence shell is "the outermost shell of the core", so a subvalence property is also a core property. Table 1 resolves this by convention, not by the definition. | Define "the core" as the closed shells *below* the subvalence shell, so the five seats partition the species. |
| A-14 | 102, 350 | MAJOR | D12's admissibility requires that "every class it names is one that property is recorded to hold on", and Proposition 3 checks it EXHAUSTIVE — against `chem_index.py`'s `CHEM` list, which is not in the paper. A reader cannot verify the class column; the paper contains no (property, class) record. | Print the (property, class) record for the three routed properties (subshell radius — one subshell; centrifugal barrier — d and f only; closed f shell — period 6, 7) as a small table or as a column of Table 1, and state what "recorded" means. |
| A-15 | 341–348 | MAJOR | Table 3's four residuals — "the 1.029 factor on t(ℓ)", "no f corridor", "occupancy slope 0.021–0.243", "crossing charge 2, 3, 5" — name objects (t(ℓ), corridor, occupancy slope, crossing charge) the paper never defines, and print four numbers (1.029, 0.021, 0.243, 2/3/5) that no obligation computes and no CITED mark covers. | Give each residual one defining sentence (what form was fitted, on what class, what departed) or replace the residual names with neutral labels R1–R4 and describe them in prose; mark the numbers as labels carried from the fits, not results. |
| A-16 | 244 | MINOR | "since a value no cell realises cannot change ℛ" is asserted; it is immediate from D2 (ℛ is computed over the own box, which does not contain the unrealised value), and B2b checks only 288 × 5 = 1,440. | Add "(D2)" after the clause. |
| A-17 | 138 | MINOR | "enumerated twice by independent means: once by Ganter's next-closure … and once by visiting every subset." For the own-box column the first route is `ownbox_count`, a sum over sub-boxes of spanning closed subsets weighted by binomials, not next-closure over the box. | Say "by next-closure over the fixed box and, for the own-box count, by next-closure over every sub-box weighted by the number of ways to choose it". |
| A-18 | 380–382 | MINOR | Theorem 4c is EXHAUSTIVE over "one ordering" (H5); a computation at one ordering is not a decision procedure over a family. Same for H2, H8, I1, B3. | Name the family as "the 96 cells of the box under the declared ordering" or use a plain "computed" status for single-ordering checks. |
| A-19 | 435 | MINOR | "a rank the parity rule of D13 forbids there, since for ℓ = ℓ′ = 0 …": the cell's third coordinate is "ℓ of the rival" only; the partner's ℓ is not a coordinate, and the parity argument needs ℓ′ = 0 too. The only ℓ = 0 cells come from the s/s diagonal pair, which makes it true, but the sentence should say so. | "the only pair in the index with an s rival is s/s, for which …". |
| A-20 | 586 | MINOR | "Theorems 1, 2, 3, 4, 5, 6 and 7 … there is no quantifier to discharge" — Theorems 1–3 and 4 quantify over all orderings (a finite family, exhausted), which is a quantifier; the sentence means "no quantifier over subsets of a box". | Say that. |
| A-21 | 579 | MINOR | Literal backslashes on the page in the J1 row (typography). | Write the cell without a code span, e.g. |ℛ(X)| = |ℛ(σX)| with the bars escaped as `\|` outside backticks, or word it "the sizes of ℛ(X) and ℛ(σX) agree". |
| A-22 | 104, 204, 318, 447 | MINOR | `^{2S+1}L_J`, `F^k`, `G^k`, `F^0, F^2, F^4` print as carets and braces (typography). | Use Unicode: ²ˢ⁺¹L_J is not expressible in Unicode superscripts for the letters; write "the ^{2S+1}L_J label" as "the term label (multiplicity, L, J)" in prose and "Fᵏ, Gᵏ, F⁰, F², F⁴" with Unicode superscripts. |
| A-23 | throughout §1–§2, Tables 1 and 3, figures | MINOR | Underscore subscripts in code spans (x_i, φ_ij, f_ij, A_i(X), Λ_chem) and the bare "n_f" in prose and in both figures; "Λ₁₃" gapped in monospace (typography). | Prefer Unicode subscripts where they exist (xᵢ, yⱼ, Aᵢ, Λ_chem → Λchem or "the chemical index"); for n_f, which has no Unicode subscript f, write n(f) or "the closed-f count" in prose and in `figures.py`. |
| A-24 | PDF pp.6, 7, 19, 21 | MINOR | Four orphaned bold run-in headings at page feet with the following table on the next page; pp.6 and 7 are half blank (typography). | Make the sub-table headings `###` headings (the template keeps a heading with its successor) or add `page-break-inside: avoid` to the table + heading pair in `paper.html`. |
| A-25 | 250–251 | MINOR | The two φ lines of the displayed staircase merge into one paragraph on the page (typography). | Put a blank `>` line between them, or use a fenced block. |
| A-26 | 267, 295, 352, 401 | MINOR | Each figure shows a small "Figure n" (alt text) above the bold caption — a duplicated label (typography). | Use an empty alt text `![](figures/…)` or make the alt text the caption sentence; `render.py` uses `implicit_figures`. |
| A-27 | Fig. 2 | MINOR | "t(l)", "0.021-0.243", "2,3,5" in the figure against "t(ℓ)", "0.021–0.243", "2, 3, 5" in Table 3. | Normalise the residual strings in `figures.py` (or in `chem_index.py`'s `R` labels as read) to the table's forms. |

---

## Part B — reader audits

### B.1 A mathematician (order, lattices, combinatorics), writing in the first person

I have not seen this material before. The formal core is small and I can follow it: an index is a
finite subset of a product of finite chains; ℛ is defined by pairwise maxima; closure is E = 0;
Lemma 3 identifies closed sets with sets cut out by one monotone map per ordered pair of
coordinates. Lemmas 1–4 are proved correctly and completely. My difficulties are with what is
built on them.

- **R-M1** (line 126, Lemma 3) — MINOR. `X = X(f) ∩ Box(X)` with f over Box(X): the intersection
  is redundant since X(f) ⊆ Box(X) by D6. Also, D1 requires an index to be non-empty and Lemma 3
  (⇒) uses it (Box(X) of the empty set is undefined); say "non-empty" in the lemma or note that
  it is inherited from D1. *Change:* drop "∩ Box(X)"; add "(X non-empty by D1)".
- **R-M2** (line 122) — MINOR. See A-4: the idempotence obligation is over value-realising X; the
  sentence claims all subsets.
- **R-M3** (lines 237–271, Theorem 1 and its reading) — MAJOR. Closure here is nearly forced by
  the shape of the data, and the paper does not say so. The valence seat is a full 4 × 3 block
  (every one of twelve cells occupied — Figure 1, line 257 "at the valence seat every cell of the
  grid is occupied"); a full block is closed under every ordering. The subvalence seat holds two
  cells, (size, A) and (count, A), which share a dependency. The only content of E = 0 is
  therefore that these two cells form a product set {size, count} × {A} that can be placed at the
  bottom corner of the sub-box by choosing an ordering — and any two cells with the same
  dependency and distinct kinds would do. The "three forced binary choices" of lines 261–265
  (sub < val, A least, {count, size} below the others) are a restatement of where those two cells
  sit. I would not accept "closes as an index" as a *result* in this setting without the sentence
  "the valence block is full, so Theorem 1 reduces to the position of the two subvalence cells".
  *Change:* add that sentence to §4 and to §0 point 2; move the weight of the paper to Theorem 2
  (the monotone climb) and Theorem 3 (the structural vacancy), which do carry content.
- **R-M4** (lines 40, 459) — MAJOR. The denominators printed (5,824 of 2²⁴ fixed-ordering closed
  sets; 16 of 288 orderings) are the wrong denominators for the claim made, which is a *minimum
  over orderings*. The relevant base rate is: among 14-subsets of the 4 × 2 × 3 box (or among
  configurations with a full 12-cell block plus two cells), how many are closed under *some*
  ordering. That is a different and much larger family, and it is computable (C(24,14) =
  1,961,256 subsets × 144 orderings up to reversal is within budget, or restrict to the shape).
  *Change:* compute and print "closed under some ordering" counts for the 4 × 2 × 3 box at size
  14, and read Theorem 1 against that.
- **R-M5** (lines 379–382, Theorem 4c) — MAJOR. The nine cells lie in a 4 × 4 × 2 × 3 box, but
  in the data (`CH`) role and carrier are in bijection (screening ↔ u, decay base ↔ c itself,
  decay rate ↔ Nₑ, ordering ↔ the configuration) and sign is a function of role. So the box is
  effectively 4 × 3 and the nine cells are (role, regime) pairs; "nine occurrences give nine
  distinct cells" says only that no occurrence is listed twice at the same regime. The sentence
  "no two of the roles collapse onto one another, so the charge is not over-specified" (line 382)
  does not follow from anything computed. *Change:* state the bijection, present the charge index
  on (role, regime) with box 12, and delete the over-specification sentence or prove it.
- **R-M6** (lines 227–229, Proposition 2) — MAJOR as stated, MINOR if reworded. D9 *defines* the
  aggregate seat as the seat of a bulk property; Table 1 assigns it by that definition; Proposition
  2 then verifies that the twelve rows assigned the aggregate seat are the twelve bulk properties.
  That is a consistency check of a definition, not a result, and "Proposition 2 is the fifth
  seat's whole justification" makes a definition its own justification. *Change:* reword
  Proposition 2 as "Table 1 is consistent with D9" and drop "whole justification"; the honest
  justification is line 229's second sentence (twelve entries had no seat inside a free atom).
- **R-M7** (line 449, Theorem 7) — MAJOR. No map from the amplitude index to (source, domain) is
  defined (A-10). A theorem cannot be about an undefined map.
- **R-M8** (lines 417, 388) — MAJOR. "Read through the calibration, c = 2 is the narrower domain —
  the more particular one — than c = 1." The domain axis in both universal-first closing orders
  runs universal < all elements < low < neutral < …, i.e. from the broadest domain upward; *low
  before neutral* on that axis places low on the broader side of neutral, which is the opposite of
  "narrower". Nothing in the order supports either reading — the order of low and neutral is
  fixed by the multiplicity pattern of Table 4, and the other two closing orders (the reversals)
  put neutral first. *Change:* delete the interpretive sentence, or state exactly what the order
  says: "in the closing orders oriented with universal first, low precedes neutral; the paper draws
  no conclusion about breadth from this".
- **R-M9** (line 386) — MINOR. "a region refines into neutral, low and hydrogenic": the two
  parameters at *a region* in the parameter index (Seaton δ₂/δ₀, h₀ collapse) are both placed at
  *low* in the merge with no stated rule; the refinement is a choice per parameter. *Change:* say
  which regime each region-domain parameter was assigned and why.
- **R-M10** (line 138) — MINOR. See A-17: the own-box counts are not obtained by next-closure over
  the box.
- **R-M11** (line 74, D5) — MINOR. An "ordering" is defined as a bijection to {0, …, m − 1}; the
  sweep in fact permutes value *codes* and Lemma 4 reverses codes. Fine, but say that E depends on
  the ordering only through the induced total orders, so ∏ |A_i(X)|! is the number of distinct
  orderings, and that the reversal pairs of Lemma 4 are distinct orderings (so "sixteen" counts
  each reversal pair as two).
- **R-M12** (lines 318, 331) — MINOR. "which is the definition of a charge role (D10)": D10
  defines a charge role as "one of the roles the core charge c plays, the cells of the charge index
  of §8"; "varies with c at fixed Nₑ" is a criterion, not the definition. *Change:* "which is what
  D10 asks of a charge role" and add that criterion to D10.

What a referee for *Order* or *Algebra Universalis* would reject: the closure results as results
(R-M3, R-M4); Theorem 4c's content sentence (R-M5); Theorem 7 (R-M7). What is unmotivated: why
pairwise staircases rather than the down-set closure in the product order — the choice is inherited
from the companion paper and is not motivated here beyond Lemma 3; one sentence would do.

### B.2 A chemist / atomic physicist who works with periodic-property data, writing in the first person

I work with NIST ASD, with the standard radius, electronegativity and affinity tabulations, and
with Slater–Condon theory. The paper takes almost no numerical value from any tabulation, which is
honest, and Table 2's twelve ground terms are correct as I read NIST ASD (Ca I ¹S₀, Sc II 3d4s ³D₁,
Ti III 3d² ³F₂, V IV 3d² ³F₂; Sr I, Y II 4d5s ³D₁, Zr III 4d² ³F₂, Nb IV 4d² ³F₂; Ba I, La II 5d²
³F₂, Ce III 4f² ³H₄; Ra I, Ac II 7s² ¹S₀, Th III 5f6d ³H₄°). My findings are about definitions.

- **R-C1** (line 154, "the list is closed in the sense that every chemical property demanded of a
  species was entered, rather than a selection being made") — MAJOR. It is a selection. Standard
  element-property tabulations (CRC Handbook; Emsley's *The Elements*) carry, among others,
  polarisability, standard electrode potential, work function, magnetic susceptibility, enthalpies
  of fusion, vaporisation and atomisation, specific heat, atomic volume, allotropy, crustal
  abundance, thermal expansion, bulk modulus, refractive index — none is in Table 1, while "smell"
  and "taste" are. The paper's own "fifth seat" argument (line 229: it appeared "because the list
  was not selected") rests on this claim. *Change:* replace "closed" with "the list as compiled";
  state that it was assembled from an informal enumeration; remove "rather than a selection being
  made" and the dependent clause at line 229.
- **R-C2** (Table 1, kind column against D7) — MAJOR for the one entry inside the closed index,
  MINOR for the rest. D7 says a *symmetry* is "a label of a state's transformation behaviour". The
  centrifugal barrier ℓ(ℓ+1)/2r² is a potential-energy term; it is not a symmetry label (ℓ is; the
  barrier is not). It is the sole occupant of the cell (symmetry, valence, P) — move it to *energy*
  and that cell empties, the valence block is no longer full, and Theorem 1 as stated fails. Outside
  the closed seats: density is mass per volume, not "a length or a cross-section"; hardness (Mohs,
  Vickers) is an ordinal or a pressure, not an energy; a half-life is a time, not "a quantity per
  unit time"; metallic character is not a transformation label; reactivity is not a rate without a
  named reaction. *Change:* for the centrifugal barrier, either defend the "symmetry" assignment in
  one sentence (e.g. "recorded by its ℓ label") or reassign and recompute; for the others, either
  widen D7 or reassign and recompute Theorem 2.
- **R-C3** (Table 1, dependency column outside the two closed seats; D10) — MAJOR. D10 says the
  dependency is "which of three families of quantities *supplies its value*": a parameter of the
  one-electron problem, a role of the core charge, or a Slater integral. No Slater integral supplies
  the value of a melting point, a smell, a taste, hardness or crystal structure (all A); no
  one-electron parameter supplies atomic mass, isotope abundance, nuclear spin, half-life or a
  neutron cross-section (all P); electrical conductivity is not a role of the core charge (C). For
  eighteen of the twenty outer-seat properties the coordinate is undefined in the paper's own
  terms. Theorem 2's "monotone climb" is then measuring the incoherence of those eighteen labels,
  not a property of a classification. The paper says the assignments are declarations (§0 point 1),
  but a declaration that contradicts the coordinate's definition is not a declaration, it is a
  category error. *Change:* either give D10 a fourth value ("none of the three") and recompute
  Theorem 2 with it, or state that the outer-seat dependencies are nominal placeholders and that
  Theorem 2 measures what happens when placeholders are admitted — and weaken §5's reading
  accordingly.
- **R-C4** (Table 1, dependency column inside the closed seats) — MAJOR. Five cells of the closed
  index have a single occupant: coordination number (count, A), oxidation states (count, C), ionic
  radius (size, C), term symbol (symmetry, C), centrifugal barrier (symmetry, P). Closure depends
  on those five assignments and on no other. Of them, "a Slater integral supplies the coordination
  number" and "a role of the core charge supplies the ionic radius" are not defensible as stated:
  coordination number is a property of a compound's structure, and Shannon's ionic radii are
  fitted to crystal data at stated charge and coordination. The paper should say which five
  assignments the closure rests on and defend each in a sentence. *Change:* add a short paragraph
  after Theorem 1 naming the five sole-occupant cells and the assignment behind each.
- **R-C5** (line 167, "nuclear charge Z … C") — MINOR. Z is not a role of the *core charge* c as the
  paper defines c (line 106: 1 for a neutral atom, 2 for a singly charged ion). *Change:* P, or
  state the identification.
- **R-C6** (lines 181, 188, 190 — "NIST ASD" for the closed f shell count, node count p and valence
  electron count) — MINOR. NIST ASD tabulates ground configurations and levels; n_f, p = n − ℓ − 1
  and the valence count are read off the configuration by the reader. *Change:* "derived from the
  NIST ASD ground configuration".
- **R-C7** (lines 43, 156 — thirty-six dashes, "no public data source is named") — MINOR. True of
  the paper, but a chemist reads the column as "no source exists". Standard tabulations exist for
  nearly all thirty-six (see the referee's reference list, R-R4). *Change:* either cite them (the
  paper still takes no value) or drop the column and keep the sentence at line 156.
- **R-C8** (line 197, "colour of the ion … set by term splittings") — MINOR. The colour of a
  transition-metal ion in solution or in a solid is a ligand-field (d–d) or charge-transfer
  property of a complex, not of the free species (Z, c); a free ion's term splittings are not what
  is seen. *Change:* "the visible absorption of the ion in its common complexes" and note it is not
  a free-species property, or move it to the aggregate.
- **R-C9** (lines 191, 220–221, 223) — MINOR. Coordination number, smell, taste and reactivity are
  not properties of an element as a species (Z, c) as usually understood; the first is a property
  of a compound, the middle two are physiological responses to a substance, the last is undefined
  without a named reaction and conditions. *Change:* say so in a footnote to Table 1 or remove
  them (which changes the census and Theorem 2).
- **R-C10** (line 106, "c is the core charge of a species — 1 for a neutral atom") — MINOR. In
  atomic physics "core charge" means the charge seen outside the core, Z − N_core; what the paper
  calls c is the spectroscopic stage (NIST's "I, II, III …") or net charge + 1. *Change:* "the
  spectroscopic charge stage c (NIST's Roman numeral)".
- **R-C11** (Table 2) — MINOR. The species are not named, so a reader cannot look the terms up:
  Nₑ = 20 is Ca I, Sc II, Ti III, V IV; 38 is Sr I, Y II, Zr III, Nb IV; 56 is Ba I, La II, Ce III;
  88 is Ra I, Ac II, Th III. The "—" at c = 4 for Nₑ = 56 and 88 reads as "not in the database", but
  Pr IV (4f² ³H₄) and Pa IV (5f² ³H₄) are in NIST ASD. *Change:* name the species in the table and
  either fill the two cells or say "not consulted".
- **R-C12** (line 447, Corollary 1) — BLOCKING, see A-8. For equivalent electrons G^k = F^k at every
  k; for a closed f shell the "four independent quantities" are not independent.
- **R-C13** (lines 439–445, Lemma 5) — MINOR beyond A-7. "The angular factor of the sole exchange
  integral … is the square of the 3-j symbol" is true up to the convention: in the configuration
  average the exchange coefficient is −½ (ℓ₁ k ℓ₂; 0 0 0)² (Cowan 1981 eq. 6.38), and in a specific
  LS term it is a different combination. The lemma should say which coefficient it means. *Change:*
  "the rank-ℓ exchange coefficient of the configuration average is −½(0 ℓ ℓ; 0 0 0)² = −1/(2(2ℓ+1))
  (Cowan 1981); the 3-j square is 1/(2ℓ+1)".
- **R-C14** (Table 3 and §7 — does "routing" claim more than an index on categorical coordinates
  can support?) — MAJOR. Yes. Routing as defined (D12) names the property a residual "varies with";
  nothing in the paper measures any variation. The index verifies only that the named property has
  a cell in the closed seats and a class in an unpublished record (A-14). The choice of property
  for each residual is a judgement recorded in the source instrument's "why" strings, which the
  paper does not print. So "Four residuals are routed" (line 35) is "four routings were declared and
  found admissible". The title's "a routing index" and the thesis's "saying which properties the
  index can route" claim more than that. *Change:* reword §0 and §7 to "declared and admissible";
  print the one-line reason for each routing; consider "a classification index" in the title.
- **R-C15** (line 180, "lanthanide contraction … caused by a filled f shell screening poorly", dep.
  A) — MINOR. The standard account is incomplete shielding by 4f (a screening statement, i.e. C or P
  in the paper's vocabulary) with a relativistic contribution of roughly 10–30 % (Pyykkö 1988); "a
  Slater integral supplies it" is not the usual reading. *Change:* defend A in one clause or
  reassign.

### B.3 A journal referee, writing in the first person

**Summary judgement.** The mathematics is correct and small; the verification machinery is
unusually careful; the physical and chemical content is thin and in one place wrong. The paper is
candid about its limits (§0 "What is not established", §10), and that candour is its strength. But
the abstract, thesis and title promise closure and routing as results, and the body delivers a
full 12-cell block plus two cells (R-M3), a routing table that is declared rather than derived
(R-C14), and a boundary theorem over labels that the paper's own definition does not license
(R-C3). Can an index whose two categorical axes are freely reordered and whose ordered axis has two
values carry "closure" as a result? Not as written. With 288 relabellings available, closure of a
14-cell set in a 24-cell box is a weak constraint; the paper knows this (line 459) but prints the
wrong denominator (R-M4).

- **R-R1** (line 3, thesis; line 23) — MAJOR. "each closure declares a boundary, saying which
  properties the index can route and which it cannot". Only the chemical index's boundary is
  measured (Theorem 2). The merged index has no boundary theorem; the amplitude index has none.
  *Change:* "the chemical index's closure declares a boundary …".
- **R-R2** (abstract line 13; §0 line 27) — MAJOR. "those fourteen close: E = 0, exhaustively over
  all 288 orderings" reads as a strong result; see R-M3. The abstract should carry the sentence
  that the valence block is full. *Change:* add "(the valence seat occupies every cell of its 4 × 3
  block; closure is carried by the two subvalence cells)".
- **R-R3** (§11, verification record honesty) — MAJOR in aggregate. (a) B5 always true (A-2);
  (b) most printed counts are printed, not asserted (A-3); (c) "every ordering visited" where half
  are (A-6); (d) EXHAUSTIVE for single-ordering computations (A-18); (e) idempotence hypothesis
  (A-4). None is a wrong number today; all are places where the record claims more than the check
  enforces. *Change:* as in A-2, A-3, A-4, A-6, A-18.
- **R-R4** (References) — MINOR. Missing standard references the paper's content calls for:
  - Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California
    Press, Berkeley — the standard source for F^k, G^k, the equivalent-electron identity and the
    configuration-average exchange coefficient (needed for A-8, R-C13).
  - Davey, B. A. and Priestley, H. A. (2002). *Introduction to Lattices and Order*, 2nd edn.
    Cambridge University Press — closure operators and closure systems (Lemma 2).
  - Birkhoff, G. (1967). *Lattice Theory*, 3rd edn. American Mathematical Society, Providence.
  - Caspard, N., Leclerc, B. and Monjardet, B. (2012). *Finite Ordered Sets: Concepts, Results and
    Uses*. Cambridge University Press.
  - For the properties the paper says have no named source: Shannon, R. D. (1976). Revised effective
    ionic radii and systematic studies of interatomic distances in halides and chalcogenides. *Acta
    Crystallographica* **A32**, 751–767. — Cordero, B., Gómez, V., Platero-Prats, A. E., Revés, M.,
    Echeverría, J., Cremades, E., Barragán, F. and Alvarez, S. (2008). Covalent radii revisited.
    *Dalton Transactions*, 2832–2838. — Pauling, L. (1932). The nature of the chemical bond. IV.
    The energy of single bonds and the relative electronegativity of atoms. *Journal of the
    American Chemical Society* **54**, 3570–3582. — Mulliken, R. S. (1934). A new electroaffinity
    scale; together with data on valence states and on valence ionization potentials and electron
    affinities. *Journal of Chemical Physics* **2**, 782–793. — Allred, A. L. and Rochow, E. G.
    (1958). A scale of electronegativity based on electrostatic force. *Journal of Inorganic and
    Nuclear Chemistry* **5**, 264–268. — Rienstra-Kiracofe, J. C., Tschumper, G. S., Schaefer,
    H. F., Nandi, S. and Ellison, G. B. (2002). Atomic and molecular electron affinities:
    photoelectron experiments and theoretical computations. *Chemical Reviews* **102**, 231–282. —
    Andersen, T., Haugen, H. K. and Hotop, H. (1999). Binding energies in atomic negative ions: III.
    *Journal of Physical and Chemical Reference Data* **28**, 1511–1533. — Clementi, E. and
    Raimondi, D. L. (1963). Atomic screening constants from SCF functions. *Journal of Chemical
    Physics* **38**, 2686–2689. — Slater, J. C. (1964). Atomic radii in crystals. *Journal of
    Chemical Physics* **41**, 3199–3204. — Desclaux, J. P. (1973). Relativistic Dirac–Fock
    expectation values for atoms with Z = 1 to Z = 120. *Atomic Data and Nuclear Data Tables* **12**,
    311–406 (subshell radii; relativistic 7s). — Pyykkö, P. (1988). Relativistic effects in
    structural chemistry. *Chemical Reviews* **88**, 563–594 (relativistic contraction; lanthanide
    contraction). — Meija, J., Coplen, T. B., Berglund, M., Brand, W. A., De Bièvre, P., Gröning, M.,
    Holden, N. E., Irrgeher, J., Loss, R. D., Walczyk, T. and Prohaska, T. (2016). Atomic weights of
    the elements 2013 (IUPAC Technical Report). *Pure and Applied Chemistry* **88**, 265–291. —
    Kondev, F. G., Wang, M., Huang, W. J., Naimi, S. and Audi, G. (2021). The NUBASE2020 evaluation
    of nuclear physics properties. *Chinese Physics C* **45**, 030001 (half-lives, spins, abundances).
    — Stone, N. J. (2005). Table of nuclear magnetic dipole and electric quadrupole moments. *Atomic
    Data and Nuclear Data Tables* **90**, 75–176. — Mughabghab, S. F. (2018). *Atlas of Neutron
    Resonances*, 6th edn. Elsevier, Amsterdam. — Haynes, W. M. (ed.) (2016). *CRC Handbook of
    Chemistry and Physics*, 97th edn. CRC Press, Boca Raton.
  *Change:* add Cowan and one order-theory text at least; the data references only if the source
  column is kept.
- **R-R5** (References, lines 592–610) — MINOR. Eleven entries are never cited in the text: Fermi
  1928, Thomas 1927, Madelung 1936, Janet 1929, Pauli 1925, Stoner 1924, Hund 1925, Goeppert-Mayer
  1941, Griffin–Andrew–Cowan 1969, Seaton 1958, Ganter 2010; de Moura and Bjørner 2008 is listed
  but Z3 is never cited by author. *Change:* cite each where it belongs (Z3 at line 51 or 510) or
  remove it.
- **R-R6** (line 603, "Lach, M. (2026) … Companion paper, in preparation") — MINOR. The closure law
  is cited to an unavailable paper; the part used is re-proved here (Lemma 3), which is enough.
  *Change:* say in D4 "the part used is proved in §2; nothing else from the companion is used".
- **R-R7** (line 382) — MAJOR. See R-M5; "the content" is a tautology.
- **R-R8** (line 417) — MAJOR. See R-M8; the interpretation contradicts the axis direction.
- **R-R9** (line 35 and §7 title) — MAJOR. See R-C14; routing is declared, not derived.
- **R-R10** (line 154) — MAJOR. See R-C1; the "closed list" claim is false and load-bearing.
- **R-R11** (lines 279–299, Theorem 2's reading) — MAJOR. See R-C3; the climb is over labels the
  paper's own definition does not license, so "the classification does not apply there" is
  circular: the labels are meaningless there by construction.
- **R-R12** (abstract line 15) — MINOR. "for any (Z, c) the index states which parameters apply"
  — this is an interpretation (line 415), not a checked map; no obligation evaluates it for a
  single (Z, c). *Change:* "can be read as stating".
- **R-R13** (line 447) — BLOCKING. See A-8.
- **R-R14** (line 443) — MAJOR. See A-7.
- **R-R15** (novelty) — MINOR. The staircase characterisation of closed sets under pairwise monotone
  bounds is a special case of closure systems in products of chains; the paper does not situate it
  (Davey–Priestley; Ganter–Wille's formal concept analysis is cited for the algorithm only). One
  paragraph in §2 placing ℛ among closure operators on a product of chains would answer the
  novelty question the paper otherwise leaves open. *Change:* add it.

Does the abstract promise what the body delivers? Numerically yes — every number in the abstract
is in the check's output. Substantively no — see R-R1, R-R2, R-R9. Is the verification record
honest? Honest in its statuses, over-generous in what it implies is enforced (R-R3).

---

## Part C — the record

| id | line(s) | severity | finding (short) | disposition |
|---|---|---|---|---|
| A-1 | 536 | MINOR | E1 row prints the source's spliced sequence unexplained | |
| A-2 | 148, 495 | MAJOR | B5 asserts nothing; 1,482 and the size sequence unpinned | |
| A-3 | many | MAJOR | printed counts not asserted (closed-family counts, 16, 20, 16/4, 4 ×4, closing-order structure) | |
| A-4 | 122, 518–521 | MINOR | D2 idempotence carries `observed(X)`; Lemma 2 says all subsets | |
| A-5 | 134, 579 | MINOR | J1 samples sizes; Lemma 4 claims set identity | |
| A-6 | 241, 289, 307 | MAJOR | "every ordering visited" where the sweep halves one axis | |
| A-7 | 443 | MAJOR | malformed 3-j closed form in Lemma 5's proof | |
| A-8 | 447 | BLOCKING | Corollary 1 wrong: G^k = F^k for equivalent electrons at every k | |
| A-9 | 231 | MINOR | breadth "constrained" asserted, not measured | |
| A-10 | 449, 564 | MAJOR | Theorem 7's map undefined; two cells are a declaration | |
| A-11 | 27 | MINOR | "two innermost open seats" wrong | |
| A-12 | 33 | MINOR | "not tested" → "not adopted" | |
| A-13 | 86–92 | MINOR | seats nest under D8 | |
| A-14 | 102, 350 | MAJOR | admissibility checked against a (property, class) record not in the paper | |
| A-15 | 341–348 | MAJOR | residuals undefined; four uncomputed numbers | |
| A-16 | 244 | MINOR | "cannot change ℛ" — cite D2 | |
| A-17 | 138 | MINOR | own-box counts are not by next-closure over the box | |
| A-18 | 380, 553–566 | MINOR | EXHAUSTIVE used for single-ordering computations | |
| A-19 | 435 | MINOR | parity argument assumes ℓ′ = 0 | |
| A-20 | 586 | MINOR | "no quantifier to discharge" imprecise | |
| A-21 | 579 | MINOR | literal backslashes on the page (J1 row) | |
| A-22 | 104, 204, 318, 447 | MINOR | carets/braces as superscripts on the page | |
| A-23 | §1–§2, tables, figures | MINOR | underscore subscripts on the page; n_f in prose and figures; Λ₁₃ gapped | |
| A-24 | PDF pp.6, 7, 19, 21 | MINOR | four orphaned run-in headings at page feet | |
| A-25 | 250–251 | MINOR | φ display block merges into one line | |
| A-26 | 267, 295, 352, 401 | MINOR | duplicated "Figure n" labels | |
| A-27 | Fig. 2 | MINOR | t(l), hyphen, "2,3,5" against Table 3 | |
| R-M1 | 126 | MINOR | redundant ∩ Box(X); non-emptiness | |
| R-M2 | 122 | MINOR | = A-4 | |
| R-M3 | 237–271 | MAJOR | valence block full; closure reduces to two subvalence cells; say so | |
| R-M4 | 40, 459 | MAJOR | wrong denominator for a min-over-orderings claim | |
| R-M5 | 379–382 | MAJOR | charge index: role ↔ carrier bijective; "content" sentence unsupported | |
| R-M6 | 227–229 | MAJOR | Proposition 2 verifies a definition; "whole justification" circular | |
| R-M7 | 449 | MAJOR | = A-10 | |
| R-M8 | 417 | MAJOR | "narrower domain" contradicts the axis direction | |
| R-M9 | 386 | MINOR | region → low assignment unstated | |
| R-M10 | 138 | MINOR | = A-17 | |
| R-M11 | 74 | MINOR | orderings vs induced orders; reversal pairs counted twice | |
| R-M12 | 318, 331 | MINOR | "definition of a charge role" is a criterion | |
| R-C1 | 154, 229 | MAJOR | "closed list" claim false and load-bearing | |
| R-C2 | Table 1 kind column | MAJOR | centrifugal barrier is not a symmetry; sole occupant of a closed cell; other kinds violate D7 | |
| R-C3 | Table 1 dep. column, outer seats | MAJOR | dependency undefined for eighteen outer-seat properties; Theorem 2 reads labels | |
| R-C4 | Table 1 dep. column, closed seats | MAJOR | closure rests on five sole-occupant assignments; name and defend them | |
| R-C5 | 167 | MINOR | Z is not a role of c | |
| R-C6 | 181, 188, 190 | MINOR | NIST ASD "source" for derived counts | |
| R-C7 | 43, 156 | MINOR | dashes read as "no source exists" | |
| R-C8 | 197 | MINOR | colour of the ion is a complex property | |
| R-C9 | 191, 220–223 | MINOR | coordination number, smell, taste, reactivity not species properties | |
| R-C10 | 106 | MINOR | "core charge" misnamed | |
| R-C11 | 320–327 | MINOR | species unnamed; two "—" cells are in NIST ASD | |
| R-C12 | 447 | BLOCKING | = A-8 | |
| R-C13 | 439–445 | MINOR | which exchange coefficient; convention | |
| R-C14 | 35, 337–358, title | MAJOR | routing is declared and checked admissible, not derived | |
| R-C15 | 180 | MINOR | lanthanide contraction on A | |
| R-R1 | 3, 23 | MAJOR | thesis: "each closure declares a boundary" — only one does | |
| R-R2 | 13, 27 | MAJOR | abstract should say the valence block is full | |
| R-R3 | §11 | MAJOR | record implies more enforcement than the check does (A-2, A-3, A-4, A-6, A-18) | |
| R-R4 | References | MINOR | missing Cowan 1981, an order-theory text, data tabulations | |
| R-R5 | 592–610 | MINOR | eleven uncited references; Z3 uncited | |
| R-R6 | 603 | MINOR | companion paper in preparation | |
| R-R7 | 382 | MAJOR | = R-M5 | |
| R-R8 | 417 | MAJOR | = R-M8 | |
| R-R9 | 35, §7 | MAJOR | = R-C14 | |
| R-R10 | 154 | MAJOR | = R-C1 | |
| R-R11 | 279–299 | MAJOR | = R-C3 | |
| R-R12 | 15 | MINOR | per-(Z, c) reading is an interpretation | |
| R-R13 | 447 | BLOCKING | = A-8 | |
| R-R14 | 443 | MAJOR | = A-7 | |
| R-R15 | §2 | MINOR | situate ℛ among closure operators on products of chains | |

Counts (distinct findings, cross-references to the same defect counted once):
**BLOCKING 1** (A-8 = R-C12 = R-R13); **MAJOR 20** (A-2, A-3, A-6, A-7, A-10, A-14, A-15, R-M3,
R-M4, R-M5, R-M6, R-M8, R-C1, R-C2, R-C3, R-C4, R-C14, R-R1, R-R2, R-R3; R-M7, R-R7–R-R11 and
R-R14 are cross-references); **MINOR 37** (A-1, A-4, A-5, A-9, A-11 to A-13, A-16 to A-27, R-M1,
R-M9, R-M11, R-M12, R-C5 to R-C11, R-C13, R-C15, R-R4 to R-R6, R-R12, R-R15).
