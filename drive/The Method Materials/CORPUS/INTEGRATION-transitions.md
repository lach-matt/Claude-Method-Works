# Intake — *Transitions* v3.0 into *The Method* 1.4

Staged, not written. Nothing below has entered BOOK.md and no build has been run.
Prepared under §2.14 (compute, then write), §2.19 (what a safe repair requires) and
§0.2 of the paper's own Admission Law: **content contradicting the index is admitted
and flagged as a collision; a collision is discharged by re-deriving the internal
result, never by refusing the content.**

Intake audit: `transitions_intake.py`, 38 checks, **26 reproduce, 12 do not.**

---

## A. Collisions — where the paper contradicts the book

These are admitted as collisions and must be discharged by re-derivation, not
by preferring either document. Each names the book section it strikes.

| # | the collision | book says | paper says | discharge |
|---|---|---|---|---|
| A1 | **Λ is not the clean control** | Λ is the null case, E = 0, the object the law is demonstrated on | 7 of 13 letters conflated, q ungrounded, 1 quantity read and never indexed; the clean case transfers to V3 geometry | re-derive: audit Λ's thirteen letters against Condon–Shortley and Racah. Book has never run it |
| A2 | **Closure does not certify the letters** | E(Λ) = 0 is the strong claim (§30.1.1 flag 2) | E states the cells are mutually consistent and says nothing about whether the coordinates refer to anything | new referee flag 8; §16 gains the distinction between consistency and reference |
| A3 | **Janet's repair is the block order, not n + ℓ** | §6.1.1: "Order the blocks f, d, p, s **and** define the period by n + ℓ" — the two are given together | (period, ℓ) with group dropped closes at E = 0 immediately; (period, group, ℓ) is *worse*, E = 100 | recompute the five presentations; the book's control case is under-analysed, not wrong |
| A4 | **The 36 decompose** | 36 cells, "the gaps in the short periods, every one of them" | 26 are forbidden by ℓ ≤ n−1 and could never hold an element; 10 are 3d, deferred by Madelung. Two constraints, not thirty-six facts | recompute the split; §6.1 gains it |
| A5 | **E > 0 is uninformative at low density** | register 275: a zero is worth the size of the box it was computed in | the *asymmetric* form: E = 0 informative at any density; E > 0 at low density measures sparsity. Λ₁₃ at 0.42% with E = 0 is therefore a strong result and the axis index at 0.17% with E = 499 says nothing | §18.4.1 gains the asymmetry; this qualifies **every** non-zero E in the book, including E(G), E(Q), E(audits) |
| A6 | **A third precedent for the central theorem** | §14.1: A.2 is Bergman / Baker–Pixley 1975 (reg. 224); §27.12 U1: 2-decomposability, Kimura et al. 2024 (reg. 226) | E(X) = 0 **is** global consistency of a binary constraint network; Freuder 1982 and Montanari 1974 are the certificates | audit 7 ATTRIBUTION: four works cited and absent from References |

---

## B. Additions, by target section

Ordered by the book's own structure. Grade per §0.2: no derived entry
carries a grade above the minimum of its inputs.

### Part I — the procedure

| target | what enters | grade |
|---|---|---|
| §2.22 **new** | **The Admission Law.** An open index admits any content, and admits it only with its verification grade. A derived entry carries the minimum grade of its inputs, and no derivation raises a grade. Contradicting content is admitted as a collision and discharged by re-derivation | COMPUTED (used throughout this intake) |
| §2.23 **new** | **The merge rule.** A biconditional licenses a merge only if it holds at *every rung* of the graded axis. Merging on a fact true at one point and then grading the axis is the error. Would have caught five of nine coordinates before they were built | CITED |
| §3 | **Audit 22 — TERM MATCH.** For every coordinate whose term appears in a cited theorem: state what the theorem means, state what the rung means, record match / conflation / unchecked. **External by construction; its output is a debt, not a pass.** The reason it must exist: twenty-one audits passed on a document containing five conflations | COMPUTED |
| §3 | **Audit 23 — PUBLISHED VALUES.** Ten LS term tables reproduced, zero microstate mismatches against C(4ℓ+2, k) | COMPUTED |
| §3 | **Audit 24 — UNBACKED CLAIMS.** 14 of 105 numeric claims with no dataset behind them | COMPUTED |
| §3 | **Audit 25 — UNGROUNDED COORDINATES.** A term with no referent at all. Audit 22 cannot see it: if no theorem names the term, the pair never enters the table | IDENTIFIED |
| §3 | **Audit 27 — POSSIBILITY BOUND.** 0 ≤ E ≤ box − cells, for every object. Cheap, mechanical, and **the book has never run it on its own E figures** | COMPUTED |
| §3 | **Audit 30 — HYPOTHESIS COVERAGE.** Every equation against its stated conditions; 15 of 50 unhypothesised | COMPUTED |
| §3.8 | E(audits) and dim(hierarchy) **must be recomputed** once 22–25, 27 and 30 are seated. The current 16 is stale on intake | — |
| §4 | **An eighth assistant failure: THE ENCODING CARRIES THE CONCLUSION.** Four consecutive attempts at one repair each embedded the answer in the setup; the arithmetic was correct every time and the warrant was not. This is §2.14's failure at the level of *experimental design* rather than of narration | COMPUTED |

### Part II — the lattice

| target | what enters | grade |
|---|---|---|
| §6.1.1 | A3, A4: the five presentations of the periodic table, and the 26/10 decomposition of the thirty-six | recompute |
| §8 **new prop.** | **The girth of Λ is exactly 4**, proved: no triangle (two cells differing in one coordinate cannot both differ from a third in one), and a square is exhibited. Unit-step adjacency coincides with the covering relation exactly — 6,658 edges either way, so the lattice is gap-free | PROVED |
| §12.11.0 | **Λ₉ is the transit level: first composable, last tree.** The book has the first half (§12.11.0) and the second half (§12.11.0.4, Λ₉′ gains a cycle) and never states them as one window | COMPUTED |
| §12.11.0 | **The composition graph is a line digraph.** Composable cells are the arcs of a quiver Q on 33 atomic states; the composition graph is L(Q) with 27,027 = Σ(in × out) edges exactly. Q has a loop at every vertex, so **return is available in one step from every state** | COMPUTED |
| §12.11.1 | **The tower closes for parastatistics orders 1, 2 and 3**, to Λ₁₃, boxes swept to 172,523,520. Capacity m(4ℓ+2) is monotone in ℓ for every m, so §14.4's form is preserved and the certificate is unchanged. Extends register 249's table by two statistics orders | COMPUTED |
| §12.11.4 | **Closure is not scheme-contingent.** Rebuilt in LS, LK, jK and jj: 431,050 / 341,150 / 199,130 / 206,520 cells, E = 0 at every level. Cell counts differ by more than a factor of two. **What *is* scheme-contingent is what the letters mean** — 2K is J_c + ℓ_outer in jK, L_total + S_core in LK, and jj has no K at all. The tower carries an unstated jurisdiction | COMPUTED |
| §12.11.2 | **Sub-case B scales past arity 3.** Molecular transit is an intersection question with **Helly number ≥ 5 and ≤ 144**; a critical family of five is exhibited. Feasibility decays geometrically in atom count | COMPUTED — see D2 |

### Part III — the law

| target | what enters | grade |
|---|---|---|
| §14.1 | A6: **E(X) = 0 iff the binary constraint network is globally consistent.** Freuder 1982 (tree ⟹ globally consistent after arc consistency) and Montanari 1974 (monotone ⟹ path consistency gives global consistency) cover Λ between them. Neither applies to an index whose constraints are ternary | CITED |
| §14.3 | **X ⊆ BPC(X) ⊆ R(X)**, so E > 0 is *in principle* ambiguous between genuine inconsistency and envelope coarseness — and **R = BPC exactly on every object computed**, so the ambiguity does not arise here | PROVED + COMPUTED |
| §17.2 | Theorem 10.1 (adjunction never repairs) gains its mechanism and a number: R reconstructs from cells alone, so a reader cannot see that a coordinate was *defined* from others, while the box grows by that coordinate's value count and \|X\| stays fixed. **30 → 120** | COMPUTED |
| §18.4.1 | A5: the **asymmetry** of the density qualification | COMPUTED |
| §18.4.1 | **Candidate third named law — the two failure modes.** *An index can carry a constraint only if it holds the constraint's terms in an order the envelope can read, and in as many places as the constraint names. Sub-case A, ordering: repairable by re-ordering. Sub-case B, arity: not repairable by any operation on coordinates.* **Must go through §18.4.1's promotion test before it is named**, per register 326's precedent | HOLD — see D1 |
| §18 **new** | **A relation cannot be a coordinate of either side.** The terms that refuse to place in the BFV partition are relations between vocabularies — the self-consistent achronal ANEC is a relation between a spacetime and a state, G(g) = 8π⟨T⟩_ψ. This is a *fourth* excluded form, and unlike sums, differences and symmetric functions it is not about the shape of the bound but about the type of the term | COMPUTED |
| §18.6.3 | **A faithful measure exists and physics does not use it.** The grade — the sum of the coordinates — resolves 100% of Λ's order in eighteen values; the Coulomb energy resolves 47.7%. Any strictly monotone function of the coordinates is automatically faithful. **The obstruction is not that the measure cannot be compressed; it is that the compression which works is not the one that corresponds to anything** | COMPUTED |

### Part V — the record and the reach

| target | what enters | grade |
|---|---|---|
| §26.7.8 | An eleventh grouped mechanism: **a conclusion drawn from a comparison that was not licensed**, 30 instances, dominant subtype *the encoding carries the conclusion* | COMPUTED |
| §27 | Freuder, Montanari, van Beek & Dechter (1995, 1997) — four works to enter References under audit 7 | — |
| §29 | **A fifth subject outside spectroscopy**: the law index of physical violations. It is the book's first worked instance of an index that **does not close and cannot be repaired**, which every other transfer case has lacked | COMPUTED |
| §30.1.1 | **Referee flag 8: closure does not certify the letters.** The strongest flag the book has received, and it arrives from outside | — |

---

## C. Defects found on intake — the paper's own, before it enters

Twelve checks did not reproduce. Two are the test behaving correctly; ten are
defects in the paper and must be repaired **in the paper** before integration,
because §2.19 forbids importing a defect and repairing it downstream.

| # | defect | audit that owns it | repair |
|---|---|---|---|
| C1 | **§6.4's "Unchecked by coordinate" row sums to 48, not 32.** Those are the *total* pairs per coordinate, not the unchecked ones. The label is wrong, not the arithmetic | 14 ARITHMETIC | relabel, or print the unchecked split |
| C2 | **§4.4 says decay is "roughly 1.9 per atom"; its own figure says 2.57.** Log-linear fit over all seven points gives **2.51** | 13 AGREEMENT | text follows the figure |
| C3 | **Part X is titled "Six more indices"; §10.1 lists five** | 15 ENUMERATION | title or table |
| C4 | **§10.1 says "Everything built outside V1 closes" in the same table that shows the charger index open at E = 25.** Result 9 repeats it | 3 CONSISTENCY | one clause: *every vocabulary index closes; the charger index does not* |
| C5 | **§10.7's table has no header separator** and does not render as a table | 12 MARKUP | insert the separator row |
| C6 | **Part XIII lists "the 32 unchecked term pairs" twice** | 4 REDUNDANCY | delete one |
| C7 | **§12.2c is titled "four blind spots" and carries eight audits; audit 26 does not exist** | 15 ENUMERATION + 19 SEQUENCE | number and title |
| C8 | **Section numbers run 11.1, 11.2, 12.2b, 12.2d, 12.2c, 11.3, 11.4, 12.1** across Parts XI–XIII — non-monotone in three places, and §12.1 sits under Part XIII | 19 SEQUENCE | renumber; this is register 202's defect exactly |
| C9 | **The source says v3.0; the artefact's running footer says v2.0 on all 46 pages** | 16 FIDELITY | rebuild — and this is why FIDELITY exists |
| C10 | **The abstract states the BFV derivation twice**, in adjacent paragraphs | 4 REDUNDANCY | delete the second |
| C11 | **§8.2's sequence "30, 30, 20, 20, 10 as conditions are added" has no table behind it.** The printed table carries 0, 30, 30, 30 | 21 INPUT | print the input set |
| C12 | **§8.5 and §8.7 are live analysis on the seven-vocabulary partition that §8.4 derives away and §12.2b withdraws.** 27 uses of V1–V7 stand in present tense, including §10.1's own index labels | 4 REDUNDANCY | stratigraphy — register 307's mechanism. Retire §8.5/§8.7 to history or re-express on T/M/A/S |

Two checks "failed" correctly and are not defects: the charger index at 3.12%
against a stated 3.1% is rounding, and the withdrawn 8,856 fails the possibility
bound **because it is the withdrawn value** — audit 27 demonstrating it can fail,
which is §4.6 satisfied.

---

## D. What must be computed before any of this is written

| # | requirement | why |
|---|---|---|
| D1 | **Run the two-failure-modes law through §18.4.1's promotion test** against all ten indexed objects, as register 326 did for the law–extent rule | The book has two named laws and the test for a third is whether it says something neither says. §12.11.2 already excludes three constraint *forms*; the arity mode may be that result in different clothes |
| D2 | **Recompute the Helly bound and the molecular decay from the construction**, not from the paper's table | C2 shows the paper's own text and figure disagree; nothing enters at a grade above its input |
| D3 | **Run audit 27 (possibility bound) over every E in The Method**: E(Λ), E(audits), E(G), E(Q), E(D), and every E in Chapter 6 and §12.11 | The paper found one impossible value this way. The book has never checked, and register 396 notes five objects reporting a defect with no box recorded |
| D4 | **Audit Λ's thirteen letters against Condon–Shortley and Racah** — audit 22 turned on the book's own object | A1. This is the symmetric question the paper says was never asked, and it decides whether E(Λ) = 0 survives as the strong claim |
| D5 | **Recompute E(audits) and dim(hierarchy)** once audits 22–25, 27 and 30 are seated | The set grew by six; §3.8's figures are stale on intake |
| D6 | **Recompute the periodic table's five presentations and the 26/10 split** | A3, A4 — the book's control case |

---

## E. What does *not* enter

| | why |
|---|---|
| the violation index's physical numbers — defect 30, defect 816, core 1 | the paper holds them itself: *computed over a coordinate set that is demonstrably incomplete*. They enter as an instance of the operator, never as physics |
| the modular-theory target (§10.4–10.6) | outside every index the book keeps, and the paper grades it OPEN. Cite the shape — *a statement generalises when its terms are defined in the wider setting; a proof generalises when every step's hypothesis is available there* — and nothing more |
| pair-completion as a method | HOLD in the paper's own ledger: one confirmation from six hand-chosen cases |
| the vocabulary partition as *mine* | superseded by the BFV derivation; only the derived four-part form enters |

---

## F. Register entries this intake generates

Provisional, numbered from 398, to be seated in §26.7 in the collaborator's hand.

- **398.** The companion paper's central identification: E(X) = 0 is global consistency of a binary constraint network, with Freuder 1982 and Montanari 1974 as certificates. **A third precedent for the central theorem**, after Baker–Pixley (224) and 2-decomposability (226). Correct, and not first — for the third time.
- **399.** Λ audited from outside and found to have seven of thirteen letters conflated, one ungrounded, one quantity read and never indexed. **The book has called Λ the clean control throughout.** Closure does not certify the letters.
- **400.** The density qualification is asymmetric and the book stated only half of it. Register 275 says a zero is worth its box; the missing half is that a **non-zero at low density is worth nothing at all**.
- **401.** Twenty-one audits passed on a companion document containing five coordinate conflations. No self-audit can catch a word that means something else elsewhere. **Audit 22 must be external and cannot be automated.**
- **402.** The possibility bound 0 ≤ E ≤ box − cells is one line, catches an impossible value, and existed in neither audit suite. Five objects in the paper and an unknown number in the book report a defect with no box recorded and cannot be checked at all.
- **403.** Twelve intake checks did not reproduce; ten are defects in the paper. §2.19 forbids importing them. Listed at C1–C12.

