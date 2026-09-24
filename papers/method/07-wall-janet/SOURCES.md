# SOURCES.md — provenance map for 07-wall-janet (not published)

Paper: `PAPER.md`, **"The Parent-Term Wall and the Cost of a Drawn Coordinate"** — a working title
adopted in the 2026-09-24 repair. **The title the paper carried from 2026-09-21 to 2026-09-24 was
"The Parent-Term Wall and the Janet Collapse"**, and it is recorded here for the author, who may
restore it: it was changed because the audit (R-2 / R-17) showed the paper's first half is not a
result about Janet's ordering but about which coordinate is drawn, and the collapse statistic of §5
is now one measurement among several rather than the headline. The directory name `07-wall-janet`
is unchanged.

Drafted 2026-09-21, resuming a `check.py` left complete at 90 obligations by an earlier run;
repaired 2026-09-24 against `AUDIT.md` (49 rows, 40 distinct findings). Every number in the paper is
produced by `check.py` — **145 of 145 obligations pass** (EXHAUSTIVE 117, GUARD 15, MACHINE-CHECKED
13); `python3 check.py --selftest` adds six negative controls, all refuted, for 151 — or is CITED.
(The audited draft ran 101 / 105 with GUARD 3 and four controls.)

Run it with `export PATH=/home/user/Claude-Method-Works/method/bin:$PATH` first; it takes about
six minutes, most of it the 7×18 Z3 obligation and the exact permutation distribution over
C(128, 7) assignments.

## What the 2026-09-24 repair changed, and why

The audit's three BLOCKING findings each turned on a claim stated more strongly than the record
supports. None was resolved by weakening a check; every one was resolved by adding obligations and
printing what they return.

**1. The framing (R-2 / R-17).** The source's headline contrast — E = 36 on (period, group) against
E = 0 on (n+ℓ, Z), "the periodic table and Janet index THE SAME 118 elements and give E = 36 and
E = 0" (Index of Indices 1454) — compares two presentations whose *second* coordinates differ, and
Theorem 1 (the paper's own) makes the second result automatic: any partition of Z into contiguous
rows laid out in order is a chain on (row, Z), and a chain is closed. `check.py` now computes both
tables both ways. **(period, Z): 118 cells, box 826, E = 0.** The left-step table **on its own drawn
(row, column) coordinates: 118 cells, box 256, E = 138** (136 with Z = 119, 120 admitted), because
it holds the corners (1, 32) and (8, 1) and Lemma 3 fills the box — exactly as the eighteen-column
table (E = 36) and the thirty-two-column table (E = 106) do. Corollary 1 was also run on all 117
two-row contiguous partitions of Z = 1 … 118: every one is closed. The paper's thesis, abstract and
§0 now claim exactly that: **what closes is Z as a coordinate, under any contiguous row partition;
what does not close is any drawn table on its drawn coordinates, with E = box − cells.** This is
recorded as **a finding about the source**: the source's contrast is an artefact of the coordinate
choice, not a property that separates Janet's ordering from Mendeleev's. The source's own sentence
"E is coordinate-relative, demonstrated on one subject" (Index of Indices 1454) is, read literally,
the paper's conclusion; the sentences around it ("Janet closes at E = 0 and the classroom table
does not", line 81) are the ones the paper does not repeat. Nothing in the source was altered.

**2. The measurable-cells chain (A-1, A-2).** See "Stated by a source and NOT reproduced", item 5.

**3. Proposition 3 (A-3 / R-1).** The audited draft stated "a channel label is ambiguous if and
only if the species prints two limits and the row names no parent" and proved only the
sufficiency of one limit; the other direction is false in general (a K or J label that couples to
one core J only is admissible on one parent alone). The paper now states the implication that is
proved — one printed limit determines the channel — and gives Ba III's `nd 2[3/2]* J=2` at both
its limits its own status, a REFUTATION of "the outer label determines the parent". The thesis,
abstract and §0 say "can fail … and does fail once", not "exactly when".

**The MAJORs, in the order of the audit.** A-2: the single-term cut and the obstacle identification
are now computed under both configuration rules (Madelung order, as the index was built; the
tabulated ground configuration, as D8 defines) and both are printed — 1,755 / 1,925 and 26,641 /
21,271. A-4: the highest-weight step of Theorem 6's proof is written out, the peel's non-negativity
is an obligation (17,476 decrements, 0 below zero), an independent count by second differences is
a second obligation, and the fⁿ row is cited to Nielson and Koster (1963), not Condon and Shortley.
A-5: the fidelity guard now evaluates *three* implementations — the Z3 term itself under
`z3.simplify`, the seated `op_order`, and the fresh `R_ref` from D3–D4 — on the same 300 draws and
prints the three pairwise disagreement counts (all 0), and the paper describes exactly that. A-6:
the non-vacuity guard runs once per (hypothesis, box) pair, thirteen in all, the 7×18 box
included. A-8: the exact permutation distribution of the rank sum over all C(128, 7) assignments
(midranks for the 12 ties) is computed — two-sided p = 3.4 × 10⁻⁵, one-sided 1.7 × 10⁻⁵ — and the
direction (773 of 847 cross pairs) is printed; the normal approximation is named as such and kept
for comparison. A-9: "four conventions, and a fifth class that writes none". A-10: the status
vocabulary is PAPER-SPEC §5's, which since 2026-09-24 admits MEASURED as a declared status word;
the guard is SAMPLED (300, seed 7). A-14: every subscript and superscript is Unicode; the extracted
text of all 22 rendered pages holds zero underscores, carets and backslashes. A-15: Figure 1 is
computed by `figures.py` from `periodic_cells` and `E_of` (see below). R-9: series are per parent
*level*, several per (level, ℓ) in Racah's pair coupling — Racah (1942) cited in D7 and §6, and the
compilation's own Ba III rows (20 series at one limit) shown as the instance. R-10: the sentence
"differ in nothing else the index records" is deleted; the charge distribution of both classes is
printed (all seven collapsed cells are ions at spectrum numbers 3–16; 63 of the 121 below are at
spectrum number ≤ 2), the confound is stated in §0, §5 and §10, and the one isoelectronic sequence
crossing an opening (K I, Ca II, Sc III) is given. R-11: "exactly the fine-structure interval" is
replaced by "to the precision at which the limits are printed", and the equality is stated as the
construction, not a test. R-12: the compilation's own source list is read by `check.py` (25 species
attributed by compilation — Kaufman & Martin 2, Kramida & Martin 1, Sansonetti 2, NIST ASD 20 — and
Sugar & Corliss 1985 / Sugar & Musgrove 1990, 1995 named as additional sources; 45 species with no
species-level attribution), and the paper prints that. R-18: Proposition 4 is restated as the
compilation's labelling convention verified on all 596 rows. R-19: Janet 1928 (*La classification
hélicoïdale …*) and 1929 (*Considérations …*) with the titles the search confirms; Stewart 2010
cited in §4; the left-step table described in one sentence; the closed object called "the (n+ℓ, Z)
presentation". R-20 / R-21: every reference is cited where it belongs (a script over the reference
list finds each author-year in the body); Hund 1925 was dropped; Racah 1942, Cowan 1981, Nielson &
Koster 1963, Sugar & Corliss 1985, Fermi 1928, Connerade 1978, Klechkovskii 1962, Mann & Whitney
1947 and Martin & Wiese 1996 were added with details verified by search or from the compilation's
own source list.

## What the 2026-09-21 run changed in the inherited `check.py`

The inherited file ran clean on `python3 check.py` (90/90) but **`--selftest` failed one negative
control**, and that failure is a bug in the check, not a claim of the source that does not
reproduce. The control built `janet_cells(JANET_ROWS_118) + [(3, 13)]` and asserted E > 0; E is 0.
Reading the construction: appending (3, 13) to the (n+ℓ, Z) index leaves it a **chain** — (3, 13)
is above every cell of rows 1–3 and below (4, 13) — and Theorem 1 says a chain is closed, so the
perturbed set was no perturbation at all. The control now *moves* a cell instead: it deletes
(5, 30) and inserts (2, 30), which breaks the chain and gives E = 54, and is refuted as a control
must be. The fact the broken control accidentally established is kept as a positive obligation in
section C ("appending (3, 13) leaves a chain of 119 cells and E stays 0"), and the paper prints it
in §4 as *closure follows the shape, not the count*. Nothing was weakened to make a discrepancy
vanish: the assertion the control makes is strictly stronger than before.

Obligations added on 2026-09-21 (ten) and 2026-09-24 (forty-four), by what the paper needed:

| added obligation | why |
|---|---|
| the table holds both extreme corners (1, 18) and (7, 1) | the hypothesis of Lemma 3, on its own object |
| appending (3, 13) keeps the chain and E = 0 / moving (5, 30) to row 2 gives E = 54 | §4's shape-not-count paragraph |
| the five label conventions: 80 / 9 / 20 / 30 / 457 | the conventions a parent may be written in; `label_form` had lumped jj pairs with run-on configurations |
| the dotted-pattern census reports 80 of 139, undercounting by 59 | the narrow-pattern point, stated as a number |
| the four two-limit species carry 99 rows, split per limit — and (2026-09-24) which limit carries which count | Figure 5 and Table 4 (A-12) |
| exactly two outer labels are printed at two limits, one of them a parent case | the REFUTATION witness — Ba III `nd 2[3/2]* J=2` at both limits |
| the highest spectrum number with a multi-level core is IV (Al IV), once | §7's ceiling paragraph (see discrepancy 2 below) |
| no core in the table has more than one open subshell; the six open shapes are s¹, p¹, p², p⁴, p⁵, d¹ | `core_terms` multiplies per-subshell term counts, which is the configuration's count only when at most one subshell is open |
| each Si I identical-key pair differs in exactly two of eleven columns | §8's third kind of repeat |
| **(period, Z): 118 cells, box 826, E = 0; the periods open at 1, 3, 11, 19, 37, 55, 87** | the framing (R-2) |
| **all 117 two-row contiguous partitions of Z = 1 … 118 are closed, both implementations** | Corollary 1 as a family |
| **the left-step table on (row, column): 118 cells, box 256, corners (1, 32) and (8, 1), E = 138; 136 at 120 cells; helium above beryllium** | the framing (R-2); Lemma 3 on the third drawing |
| the largest n occupied equals the period on 107 of 108 (palladium) | §4's "what does separate the two row coordinates" |
| non-vacuity for each of the thirteen (hypothesis, box) pairs; the fidelity guard as three pairwise counts | A-5, A-6 |
| the full fⁿ row; the peel never negative over 17,476 decrements; the second-difference count agrees; particle–hole symmetry | A-4, A-13 |
| U₁ = 773 of 847, no tied cross pair; the exact permutation p over C(128, 7); 12 ties; the charge distribution of both classes; the argon-core nd sequence; the factor 10.0 | A-8, A-13, R-10 |
| the measurable chain under the cuts that produce it, with a D8 core (1,925) and a Madelung core (1,755, the 170 differing cells with cores Pd, Ce, Pt); the chain under the source's stated cuts (61,152 / 12,720 / 7,950 / 3,550) | A-1, A-2 |
| the obstacle identification under the tabulated configurations: 21,271 of 26,641 | A-2 |
| the source list: 25 species attributed by compilation, the 2 / 1 / 2 / 20 split, 45 not; the 25 NIST and 5 Theodosiou provenance cells are measured cells | R-12 |
| C II (5) and Ga II (2) are the seven single-level rows naming a parent; Ar II's 30 + 14 rows print one limit; the labelling convention on all 596 rows | A-24, R-15, R-18 |
| section I's arithmetic re-labelled: 118 − 118 = 0 on both closed indices, 110 − 90 = 20, 256 − 118 = 138; E = box − cells on the three drawn tables | A-11 |

## Where each section draws from

All paths below are under `/home/user/Claude-Method-Works/`.

| paper section | source passages |
|---|---|
| §0, §1 D1–D4, Lemma 1, Lemma 2 | `method/members/The_Method_1_6-2.md` 1516–1560 (§6 and §6.1: the 90 / 126 / 36 table; the definition of Âᵢ, φ̂ᵢⱼ and ℛ(X); "E(X) = |ℛ(X)| − |X| is the gap"; "no outside knowledge enters"); 1607–1620 (idempotence of ℛ, and that a drawn band's closure is a theorem rather than a finding); `tools/cypher.py` `op_order` (imported by path — the staircase as the instrument computes it) |
| §2 Theorem 1, Corollary 1, Theorem 2, the Remark, Lemma 3 | no source passage: the paper's own, proved in full and machine-checked |
| §3 Theorem 3, Theorem 4, Proposition 1 | main volume 1522 (the 36 named as period 1 groups 2–17 and periods 2/3 groups 3–12), 1551–1566 (§6.1.1: the decomposition 25 forbidden + 11 deferred; "1p contributes five and not six, because helium occupies group 18 itself"; helium at group 18 → E = 36, at group 2 → E = 20; "the difference is sixteen cells"), 1570–1572 (the three-convention table: 18-column 90/36, 32-column 118/106, left-step 120/0); `method/members/The_Method_1_6___The_Index_of_Indices-2.md` 1361–1372 (all 90 cells listed period by period), 1440–1444 (the periodic table as the control index) |
| §4 Theorem 5, the periods against Z, the left-step drawing | Index of Indices 1374–1388 (the eight rows with their atomic-number ranges and lengths 2, 2, 8, 8, 18, 18, 32, 30; "118 cells, E = 0"), 1446–1456 (118 cells in a box of 944, E = 0; the Janet citation; the shell-length sequence by the Klechkovski–Hakala formulas; the Löwdin challenge as an open problem and "this work uses the ordering and does not explain it"; "E is coordinate-relative, demonstrated on one subject"); **the (period, Z) and (row, column) indices have no source passage and are the paper's own** (see the framing finding above); `method/members/LW1-ground.py` (imported — the tabulated ground configurations, Z = 1…108); `tools/populate.py` `janet_cell` (imported — the differentiating-electron reading, which fails at six elements); `tools/cypher.py` `_janet` (the (n+ℓ, ℓ) subshell fixture: 22 cells, box 40, E = 0) |
| §5 | `method/members/The_Method_1_6___Spectra_Compendium-2.md` 268–283 ("The Janet collapse": the 3d/4f/5f table at Z = 21, 57, 89; Ti IV nd 0.6202 against Sr II nf 0.0618; "the collapse coordinate is read from the periodic table, not fitted"; Ca I nd 0.908 at Z = 20 and Ba II nf 0.756 at 56); `method/members/The_Method_1_6___Mathematical_Compendium-2.md` 3060–3070 ("The Janet collapse" entry, with Goeppert-Mayer 1941 and Griffin, Andrew & Cowan 1969 as prior art); `method/members/The_Method_1_6___The_Physics_Compendium-2.md` 478–486 ("Janet block boundary — Z = 21, 57, 89, an exact integer", and "Where it fails: as a SHARP threshold"); Spectra Compendium 40–60 (the bound column, including the three parent-count obstacles at 9,756 / 11,605 / 5,280 cells); `drive/The Method Materials/COORDINATES-2_13.csv` (the 104,832-cell index itself) |
| §6 Theorem 6, Corollaries 2–3, Proposition 3, the REFUTATION | Mathematical Compendium 742–754 ("The parent-term wall": "an OPEN-SHELL core gives many parent terms and no separable Rydberg series"; Condon & Shortley 1935 ch. VII and Racah 1943 as prior art); Spectra Compendium 250–258 ("The parent-term wall": "A closed-shell core has one parent term and gives one Rydberg series per ℓ. An open-shell core gives one series per parent, all interleaved, converging on different limits" — **see discrepancy 6**); Mathematical Compendium 2980–2992 ("Core angular structure": at ℓ = 3 δ splits by the core's term while its J-pairs stay together) |
| §7, §8 | Spectra Compendium 293–935 (the channel table, 596 rows) and 973–1027 (§IV: the B.1 source list; the count paragraph — 596 rows, 477 series of three or more members, 119 two-member channels, 28 elements, 70 species, 3,342 levels, 2,269 interior cells, bracket 1,577 of 1,738 on 392 rows, 78 no-triple, 126 untested); `method/proofs/compendia4.py` and `compendia3.py` (read for the conventions and imported by path for the table reader — see below) |
| §9 | Spectra Compendium 297 (the bracket column's definition and its three values); main volume 1633–1646 (an index may bracket a quantity only along an axis the quantity is monotone on; the first-ionisation-energy illustration); the companion paper `03-bracket/PAPER.md` in this series, cited in §9 by description only |

## The parsers: imported, never copied

`check.py` imports five instruments by path and copies none of them:

- `tools/cypher.py` — `Index` and `op_order`, the staircase closure. The fresh reference
  implementation `R_ref` in `check.py` is written from D3–D4 and is *not* a copy; the two agree on
  every object the paper computes, and the encoding guard compares the Z3 term, `op_order` and
  `R_ref` pairwise on 300 random draws (3,578 cell decisions, 0 disagreements).
- `method/members/LW1-ground.py` — `expand`, `GROUND`, `CORE`: the tabulated ground configurations.
- `tools/populate.py` — `core_p`, `janet_cell`, `aufbau_config`, `pauli_bound`, `collapse_C`.
- `method/proofs/compendia4.py` (which itself imports `compendia3.py` and `compendia2.py`) — its
  `rows()` is run as an independent reader of the channel table and its row indices are compared
  against `check.py`'s own parse, row for row. `check.py` also borrows `compendia4.PREFIX` for
  label normalisation rather than re-typing the regular expression.
- `research/warp-drive/prover.py` — `cells_of`, `subset_vars`, `observed`, `in_R`, `prove`,
  `non_vacuous`.

**Where the conventions came from.** `compendia3.py`'s `PARENT` pattern is `^\S*\.\(.*?\)\.`, a
dotted configuration followed by a parenthesised group; `compendia4.py` records that this pattern
"does not see `(3P)ns 4P J=5/2` or `2s22p5(2P*3/2)nd ...`, so it UNDERCOUNTS", and prints 139
against 80. This paper's §7 takes that finding, splits the 39 rows that are parenthesised but not
dotted into 30 jj pairs and 9 run-on configurations by reading the labels, and states the four
conventions that write a parent, with counts, beside the 457 rows that write none. The 59-row
margin between the narrowest and the widest reading is the paper's own arithmetic on those counts.
The label forms themselves are NIST ASD's (Martin & Wiese 1996).

## Reproduction — what reproduces, what does not, and what was chosen

### Reproduced exactly

E = 36 on (period, group) with the 36 cells named; the decomposition 25 forbidden (1d 10, 1p 5,
2d 10) + 11 deferred (3d 10, 1s 1); E = 20 with helium at group 2 and the 16-cell difference;
E = 106 on the 32-column layout; E = 100 with a block coordinate adjoined; E = 0 on (n+ℓ, Z) at
118 and at 120 cells, with rows 2, 2, 8, 8, 18, 18, 32, 30 and openings 1, 3, 5, 13, 21, 39, 57, 89;
E = 0 on the (n+ℓ, ℓ) subshell index at 22 cells in a box of 40; the 596-row channel table with
70 species, 28 elements, 119 starred rows, 3,342 levels, 2,269 interior cells and the bracket
column at 1,577/1,738 on 392 rows with 78 no-triple and 126 untested; the coordinate index at
104,832 cells, 13,104 keys, 7,260 pairs, grades 929/358/103,545, the 22 bound strings and their
counts; the four numbers of the measurable chain (61,152 → 11,416 → 4,395 → 1,755) **as numbers,
but not under the cuts the source states — see item 5**; d⁴ = 16 LS terms, and the full
p^k, d^k, f^k term tables; the four two-limit species and the three sub-wavenumber pairs; the four
Ar II notation duplicates and the two Ba III n-window pairs (against `compendia4.py`'s own
selftest fixtures); the source list's 25 attributed species.

### Stated by a source and NOT reproduced — the paper prints the reproduced figure

**1. The Janet-collapse sample and statistics.** Both the Spectra Compendium (line 279) and the
Mathematical Compendium (line 3068) state: *"Across 116 cells with p = 0 at ℓ = 2 or 3: collapsed
median 0.637, uncollapsed 0.036, U-test p = 9.8×10⁻⁴."* Recomputed from the coordinate index with
`populate.core_p`, the figures are:

| quantity | stated | measured here |
|---|---|---|
| cells with p = 0 at ℓ = 2 or 3 | 116 | **128** (of 148 measured d and f cells) |
| collapsed median | 0.637 | **0.6202** |
| uncollapsed median | 0.036 | **0.0335** |
| two-sided p | 9.8 × 10⁻⁴ | **3.4 × 10⁻⁵ exact** (permutation distribution over C(128, 7)); the tie-corrected normal approximation gives 2.5 × 10⁻⁴ (U = 74, z = −3.66) |
| split sizes | not stated | **7 at or past, 121 below** |
| direction | not stated | collapsed larger in 773 of 847 cross pairs |

The paper prints the measured figures and never the stated ones. The gap of twelve cells is the
likeliest source of the rest — a guess, labelled as one: the stated run predates the index's
extension to Z ≤ 120 and its last measured-cell additions, and `check.py` recomputes p from the
*tabulated* ground configuration at each core rather than from whatever list the earlier run used.
The source's p is presumably a normal approximation of some kind; which kind it does not say.
This is recorded, not repaired; `check.py` was not adjusted in either direction. **The audit's
R-10 adds a caution the source does not carry**: the seven collapsed cells are all ions at spectrum
numbers 3–16 and 63 of the 121 below are at spectrum number ≤ 2, so the split is confounded with
ionisation stage, and the paper says so wherever it prints the statistic.

**2. The open-shell charge ceiling.** The Spectra Compendium (line 256) and the Mathematical
Compendium (line 750) both say the compilation holds *"no open-shell ion above charge 6"*. The
measurement is tighter and the statement is therefore true but not sharp: the highest spectrum
number at which a core carries **more than one level** is IV, reached once, by Al IV (core 2p⁵ ²P°).
Reading "open-shell" as "at least one unfilled subshell" rather than "more than one core level"
puts Fe XV in the class — its core is 3s ²S₁/₂, one open subshell and one level — and the ceiling
would then be XV, not 6 either. Neither reading gives 6. The paper prints the measured statement
in the form the classification supports ("no core with more than one level above spectrum number
IV") and states the two Fe species explicitly so the reader can see which reading is in force. The
audited draft's "which is what Corollary 2 predicts" is gone (A-23): the ceiling is a fact about
which series were captured.

**3. The Fe IV series census is not reproduced, and is not printed.** Both compendia state that
Fe IV's 3d⁴ core carries sixteen LS terms, that the capture shows 13 of them across 24 distinct
(parent, ℓ, term) series, that every one of those 24 has exactly one member, and that Fe IV has
about a thousand analysed levels and no extractable defect. **The channel table holds no Fe IV
rows at all** (the only Fe species present are Fe XV and Fe XVI), and the level data behind the
claim is not in this tree, so `check.py` can reproduce only the term count: d⁴ = 16, exhaustively,
over all 210 Slater determinants of that configuration. The paper therefore states the term count
and the general corollary and omits the Fe IV measurement entirely. It is replaced, as evidence of
the same point, by two things `check.py` *can* verify: the compilation's own ceiling at spectrum
number IV, and the coordinate index's three parent-count obstacles (3 / 16 / 119 parents on
9,756 / 11,605 / 5,280 cells), each shown to equal the maximum term count of the p, d and f block
respectively — under the Madelung-order configuration the index was built with. Under the
tabulated configurations (D8) the identification holds on 21,271 of the 26,641, and the paper
prints both (A-2).

**4. The framing: "Janet closes and the classroom table does not."** The Index of Indices (lines
66–83, 1448–1454) presents E = 36 against E = 0 as a contrast between two tables of the same 118
elements and reads it as a fact about Janet's ordering ("Janet's 1928 ordering, chosen for shell
structure, is the coordinate system where E = 0"). `check.py` shows the contrast is an artefact
of the coordinate choice: (period, Z) also has E = 0 (118 cells, box 826); the left-step table on
its drawn (row, column) coordinates has E = 138 (box 256), a larger defect than the eighteen-column
table's; and every one of the 117 two-row contiguous partitions of Z closes. The one sentence of
the source that survives unchanged is its own "E is coordinate-relative" (1454). **A finding about
the source, recorded, not repaired**: the source's numbers all reproduce; its reading of them does
not. The paper's title was changed for this reason (see the head of this file).

**5. The measurable-cells chain and its cuts (A-1, A-2).** The Spectra Compendium (258–261) prints
61,152 → 11,416 → 4,395 → 1,755 with the cuts *Z ≤ 92; core charge ≤ 10; ℓ ≤ 4; a single-term
core*. `check.py` reproduces the four numbers, but only with **Z ≤ 83 and spectrum number ≤ 10**
for the second, **Z ≤ 83, spectrum number ≤ 6, ℓ ≤ 4** for the third, and the core taken **in
Madelung order** (as the index was built) for the fourth. The cuts as the source states them give
**61,152, 12,720, 7,950 and 3,550** (with a tabulated one-term core); the hybrid Z ≤ 83, spectrum
number ≤ 10, ℓ ≤ 4 gives 7,135. Under D8's tabulated ground configuration the last cut gives
**1,925**, not 1,755; the 170 cells between the two counts have cores Pd, Ce and Pt, closed or
one-term as tabulated and open in Madelung order. The paper prints the chain with the cuts that
produce it, states both configuration rules and both last counts, and prints the stated-cut chain
beside it. The audited draft had listed this chain under "Reproduced exactly", and SOURCES.md was
wrong to do so: the numbers reproduce, the procedure does not.

**6. "One series per parent term."** The Spectra Compendium (256) states the rule as *"an
open-shell core gives one series per parent, all interleaved, converging on different limits"*,
and the audited draft repeated it as "one series per parent term, each converging on its own
limit". That is not the literature's statement and not the paper's own D6: series are built on
parent *levels*, each level is a limit, and within one parent level and one ℓ there are several
series, one per (K, J) in Racah's pair coupling (Racah 1942) — which is exactly the `2[3/2]°`
notation the compilation's own labels use, and the compilation shows it: 20 Ba III rows converge on
the single ²P°₃/₂ limit. The paper states the rule per level and cites Racah 1942, and marks the
structure CITED (Condon & Shortley 1935; Racah 1942, 1943; Cowan 1981); only the term counts are
measured here. A finding about the source's wording, recorded.

**7. The Janet citation.** The tree is inconsistent about Janet: the Index of Indices (1452)
cites *Considérations sur la structure du noyau de l'atome*, Beauvais (1929), "with the table
first published in 1928"; the Register (291) and the Mathematical Compendium (720) cite *La
classification hélicoïdale des éléments chimiques* as 1929. The search confirms *La classification
hélicoïdale* is the 1928 pamphlet (Imprimerie Départementale de l'Oise, Beauvais) and
*Considérations* the 1929 one, and Stewart 2010 (*Foundations of Chemistry* 12, 5–15) is the
account the paper cites for the table's history. The paper cites both with the dates the search
gives.

### Superseding, where a later passage governs

`compendia3.py` pins Ba III `nd 2[3/2]* J=2` as a label printed at two limits and the short-key
duplicate count at nine; `compendia4.py` supersedes both, after a relabelling that gave every row
of the four two-limit species an explicit parent. This paper measures the **current** table and so
agrees with `compendia4.py`: 139 rows naming a parent, 4 notation duplicates, 2 window pairs, 2
identical-key Si I pairs — and the stripped-label test recovers `compendia3.py`'s Ba III
observation in the form that survives the relabel, since stripping the parent prefix is exactly
what makes the two rows collide again. That is the paper's §6 REFUTATION witness and §8's caution.

## Interpretations chosen, and why

1. **Proposition 3 states one direction only.** The audited draft called a channel label
   "ambiguous exactly when the species carries two limits and the row names no parent", which is
   the criterion `compendia4.py` records M as having ruled on for the *relabelling*; as a theorem
   it is only half true. The paper proves that one printed limit determines the channel and says
   outright that two limits do not by themselves leave it undetermined (a K or J that couples to
   one core level only fixes the parent). Ba III's label at two limits is a REFUTATION of the
   opposite universal claim, with its own status. The weaker reading of "ambiguous" ("the core has
   two levels and the row names no parent") gives 93 rows; the paper reports that number as what
   it is — rows whose parent is determined by Proposition 3 because their species prints one limit.
2. **Proposition 4 is the compilation's labelling convention, verified.** That every row of a
   two-limit species names a parent is how the compilation was labelled (`compendia4.py`), so the
   proposition confirms a rule applied without exception, not a property of the thirteen spectra;
   §0, §7 and §10 say so. A species may have a multi-level core whose second limit was never
   captured, and Ar II (core 3p⁴, 3 terms, 5 levels, one printed limit on all 44 rows) is named as
   the concrete case.
3. **The three sub-wavenumber limit pairs are excluded on their magnitude, not on a judgement.**
   Ca II 0.010, Li I 0.036, Zn I 0.020 cm⁻¹: the cut is "a wavenumber or more apart", stated in the
   paper, applied by `check.py`, and it is the same cut `compendia4.py` uses.
4. **The slot rule of Theorem 4 is stated in the paper before it is used.** Reading a
   (period, group) cell as a subshell requires a convention — groups 1–2 the s slot, 3–12 the d slot,
   13–18 the p slot, n = period, f-block set aside. The source states the decomposition and its
   result; the paper states the rule that produces it, so a reader can check the 36 cases.
5. **The collapse section is a measured separation with its confound printed, not a derivation.**
   The source is careful ("a measurement against Janet's boundaries, not a derivation of them",
   Index of Indices 1452); the paper adds the charge confound the audit found and the caution that
   no same-charge comparison across an opening exists in the sample.
6. **The left-step table's drawn coordinates are numbered as the drawing is read.** Columns 1 … 32
   with the f-block at 1–14, d at 15–24, p at 25–30 and s at 31–32, so hydrogen is (1, 31), helium
   (1, 32), and actinium opens row 8 at column 1. Any other numbering that keeps the s-block at the
   right and the f-block at the left holds the same two corners and gives the same E by Lemma 3.
7. **Figures 1–5 are all computed.** Figure 1 was the audited plate
   `extracted/archives/the-method-1-6-figures-build8/figures/figure-6.2.png` (md5
   b383daa6351d7fb140a7055651649f1f) until the audit (A-15) found its red title drawn across the
   first row of cells; it is now drawn by `figures.py` from `periodic_cells` and `E_of` with the
   same 90 / 36 / 126 content and the title above the grid. Figure 4's caption says "cells", not
   "channels" (A-17), and Figure 5 prints the four spans to the three decimals of the limits, as
   `check.py`'s `span_labels` obligation pins them (A-13). `figures.py` re-run on 2026-09-24
   reproduces every md5 in `FIGURES.tsv`.

## Public provenance

The measured levels behind the channel table and the coordinate index are NIST ASD retrievals and
the published compilations named in the paper's §7 and References (Kaufman & Martin 1991; Kramida
& Martin 1997; Sansonetti 2008a, 2008b; Sugar & Corliss 1985; Sugar & Musgrove 1990, 1995;
Theodosiou, Inokuti & Manson 1986). The ground configurations are the NIST tabulation. Nothing in
the published text points at anything else.
