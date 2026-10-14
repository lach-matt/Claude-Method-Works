# AUDIT — 10-beyond-the-atom, "Closure beyond the atom: the defect of other indexes, redundancy, and the electromagnetic quotient"

Audited 2026-09-24 against `PAPER.md` (567 lines, dated 21 September 2026), `check.py` (958 lines),
`SOURCES.md`, `FIGURES.tsv`, the four figures, and the rendered `out/10-beyond-the-atom.pdf`
(21 pages) and `.html`. The audit does not edit `PAPER.md` or `check.py`; it records, the drafter
repairs.

**What was run.** `python3 check.py` (PATH = `method/bin` first, Python 3.12.3, Z3 5.1.0), detached to
a log: **102 obligations, 0 failed** — MACHINE-CHECKED 8, EXHAUSTIVE 78, SAMPLED 9, REFUTATION 2,
GUARD 5, `CLEAN`, about ten minutes. `python3 check.py --selftest`: **106 obligations, 0 failed**,
the four negative controls N1–N4 each reported refuted (N3: 18 of 1,112 cells disagree), `CLEAN`.
`python3 papers/method/lint.py papers/method/10-beyond-the-atom`: **0 hits**. The PDF was rasterised
page by page (PyMuPDF, 1.4×) and all 21 pages read; the HTML was screenshotted with headless Chromium
per the brief. The md5 of every file in `figures/` matches `FIGURES.tsv`; `figure-1-periodic-table.png`
is byte-identical to the audited plate (`PROOF-FIGURES.tsv` row 34, `figure-6.2.png`, md5
`b383daa6…`). Every source passage `SOURCES.md` names was opened and read in full; `tools/cypher.py`,
`docs/CYPHER.md`, `research/warp-drive/prover.py` and the hierarchy-law paper's §0, §4, §6 and §9 were
read. Five probes were run beside the check (a general-partition counterexample to the abstract's
fibration claim, the d = 3 redundancy rung's trial log, the particle-bound nuclide list completed from
NUBASE2020, the closure of the survey's witnessed cells, and the crossing restricted to physical
one-electron moves); their commands and results are quoted where they are used.

**Headline.** Every printed number matches a line of the check's output, the proofs of Lemmas 1–3,
Theorems 1, 2, 5, 6 and Corollaries 1, 3, 4 are complete and correct, the Z3 encodings are the operators
the paper defines, and the nine source claims `SOURCES.md` says do not reproduce are handled honestly
(the paper prints the recomputed figure in every case). The paper is not ready for the author, for
three reasons above the rest. **(1)** The abstract's crossing — the paper's one physical headline —
is computed on a population of 4,325 "moves" of which **2,923 place electrons into a subshell that is
already full** and 2,819 move more than one electron; restricted to the 134 moves that are physical
one-electron transfers, the crossing does not occur (forbidden moves are followable more often than
allowed ones in both scopes). **(2)** The abstract and §0 state that "fibring an index cannot raise its
total defect", with a fibration defined in D5 as any partition; that is false (a three-cell
counterexample is given below), and only the by-a-coordinate case is proved. **(3)** The rendered PDF
sets all of its mathematics in monospace code font, with 113 literal underscores and carets on the
page, and three theorem statements whose (a)/(b)/(c) labels render as "1.", "2.". Beside those:
Proposition 1's general identity is cited to an unlocatable reference when it is prior art with a
six-line proof; §6's discriminating index has a categorical coordinate, which the paper's own
Corollary forbids; the redundancy row "0% at d = 3" ran no trial; the particle-bound nuclide list is
uncited and incomplete at Z = 9, 10, and its stability claim fails when it is completed; the survey
grid and the Kreuzer–Skarke slice are closed and open respectively by construction, and the paper
presents both as measurements on their subjects.

---

## Part A — content audit

### A.1 Definitions and results against the sources

M = `The_Method_1_6-2.md`, I = `…The_Index_of_Indices-2.md`, C = `…Mathematical_Compendium-2.md`,
all under `method/members/`. Row by row:

| paper | source | relation | proof complete? |
|---|---|---|---|
| D1–D4 (index, box, envelope, closure, defect) | M 1546–1556; `docs/CYPHER.md` operator table; `tools/cypher.py` `op_order` | the source's, with the own-box regime explicit and `max ∅` avoided by Lemma 1 | — |
| D5 (fibration) | M 10363–10375, 10696–10735 | **stronger than the source and stronger than what is proved**: the source fibres by categorical axes (a coordinate); D5 admits any partition (A-1) | — |
| D6 (coupling) | I 310–340 ("whose envelope actually constrains", no test) | reconstruction; the test φ_ij(a) < max A_i is stated (SOURCES.md §5.2) | — |
| D7 (redundancy) | I 310–340 (no trial count, threshold or seed) | reconstruction; ladder, 8/10 rule and seed are the paper's, presented as the definition (A-20, R-20) | — |
| D8 (extension, quotient) | I 1467–1475; C 2630–2640 | the paper's formalisation of the source's "quotient, not extension" | — |
| D9 (composability) | I 181–190; M 3343–3400 | reconstruction chosen to reproduce 0 / 1,169 / 2,050 (SOURCES.md §5.3); matches electrons delivered against electrons held (R-7) | — |
| D10 (bit cost) | none | the paper's own | — |
| D11 (five operators) | `docs/CYPHER.md`; `tools/cypher.py` | the instrument's; `information` under-specified (A-23) | — |
| Lemma 1, Theorem 1, Lemma 2, Corollary 1 | M 1650–1656 ("ℛ is idempotent — §32.4.1 proves it"); written out here | the paper's proofs, complete | yes |
| Proposition 1 | `docs/CYPHER.md` (order and algebra both E = 100) | measured on 766 subsets + 3 indexes; general identity **CITED to Lach 2026**, which itself records it as prior art (A-3) | the cited direction has a six-line proof (A-3) |
| Theorem 2 | — | the paper's | yes |
| Theorem 3 | M 1700–1712 (calendar relabelling) | (a) trivial and proved; (b) the source's, computed | yes |
| "Corollary (ordered coordinates only)" | M 10363–10375 | the source's D.1 sentence, unproved remark (A-18) | no proof, none possible — it is a remark |
| Theorem 4, Corollary 2 | M 10696–10735 (E 4/3/2/0 under refinement; "E = 0 … relative to a stated fibration") | Theorem 4 is the paper's and correct as stated; Corollary 2's refinement step is a gap (A-2); the abstract's general claim is false (A-1) | Theorem 4 yes; Corollary 2 no |
| Theorems 5, 6, Refutations 1, 2, Corollary 3 | I 1467–1475; C 2630–2640 ("a derived coordinate cannot improve closure") | the paper's lattice statement of the source's assertion; correct | yes |
| §3.1 Λ, Λ₉, Λ₁₀ | M §7.1; I 1414–1440; `tower-2.py` | exact: 976/6,912, 1,654/27,648, 2,535/110,592; C1b confirms the tower member equals the cypher fixture cell for cell | — |
| §3.1 composability 0 / 1,169 / 2,050 | I 181–190 | exact under the reconstructed match | — |
| §3.2 periodic table 90/126/36, the 36 named, He at 2 → 20 | M 1516–1600; I 1360–1380 | exact | — |
| §3.2 Janet 118/944/0 | I 1382–1392, 1442–1456 | exact | — |
| §3.3 calendar 365/372/7, seven cells, relabelled 0; box ordering 35/125/0; chessboard 64/64/0 | M 1700–1712; I 1398–1410, 1458–1466 | exact (the 56-cell box ordering of M §6.2 is not printed — SOURCES.md §4.7) | — |
| §3.4 particle-bound 27/33/6, 40/48/8, 52/61/9, the nine named | M 1660–1699; I 236–244 | exact at Z ≤ 7; the source's 80/89 at Z ≤ 9 does not reproduce (75/84 printed, SOURCES.md §4.2); the fixture is uncited and incomplete at Z = 9, 10 (A-10) | — |
| §3.4 AME2020 3,558 / 2,550 / 1,008, E = 2, cells (0,0) and (2,0) | C 1860–1872 (the re-measurement) | exact; two populations correctly kept apart | — |
| §3.5 Kreuzer–Skarke 208 / 12,544 / 540, 498 + 498 of 21,528, 112, χ ∈ {0, ±2, ±4}, 26–262, bounds | M 8730–8795; I 246–256 | exact; the defect is by construction (A-7) | — |
| §3.6 d(1), d(2), d(3), d(14); three oscillators E = 0 | M 8700–8706; I 258–266 | exact; the row is a 4³ box (A-27) | — |
| §3.7 survey grid 1,744 / 2,240 / 285, E = 0 | I 286, 340–372 | source's 1,664 / 313 not reproduced, recomputed printed (SOURCES.md §4.4); the grid is closed by construction and the witnessed set is not (A-8) | — |
| §3.9 bit costs 22.6, 34.0, 47.4, 105.1, 633.0 | none | recomputed by hand: 22.59, 34.01, 47.39, 105.08, 632.96 | — |
| §4.2 Table 2, r² = 28227/16524095, p = 0.94 | I 310–340 | six rows exact to rounding (29% → 28.6%, 17% → 16.7%); Janet row only on the 724-cell down-set (SOURCES.md §4.8) | — |
| §4.3 projection ladder 61/30/30/30/5/0 | I 326–332 | exact, but the d = 3 rung ran no trial (A-9) | — |
| §4.4 Nₑ adjoined: 12 envelopes, 33.3%, 0%, E = 20,808; join witness | I 334–340 | exact; E = 20,808 has no source figure | — |
| §5.1 814 / 840; Lemma 3; Corollary 4 | C 2596–2612; M 3548–3600 | the source asserts "convex → closes"; the paper proves it | yes |
| §5.2 526 at E = 0; §5.3 840 at E = 750, witness | M 3583–3590; C 2620–2626 | exact; witness verified (Q5c/Q5d, Q6d) | — |
| §5.4 rectangle 2 × 4, E = 9,278 (source: 3 and 3,900), 1,654, 3,812, H = 0.633, I = 0.0004 | M 3572–3598; I 1471; C 2632–2640 | 9,278 reproduces neither source figure; printed as measured with SOURCES.md §4.3 recording both | — |
| §5.5 Table 3, 4,325 moves, the four percentages, parity 38.4/20.1/89.8/84.5 | M 3343–3360; I 165–180; C 2570–2576 | exact; population size 4,325 has no source figure; the population is unphysical (R-6) | — |
| §6 five languages, 10/10, 10/10, 100/100/83/24/0, 1/10, degeneracy | `docs/CYPHER.md`; I 268–284; M 9405–9500 | exact; "six" not printed (SOURCES.md §4.5) | — |

**The nine non-reproducing source claims (SOURCES.md §4.1–4.9)** are each fairly represented: the
paper prints the recomputed figure and never the stated one; both nuclide populations are kept as two
rows with the difference explained (§3.4); 9,278 is printed with 1,654 and 3,812 beside it and the
qualitative claim rests on Corollary 3 rather than on a number; 1,744 / 2,240 / 285 replace 1,664 / 313
and the "E = 1,351" misreading is corrected by the source's own later sentence; "six" languages is
not printed; 28.6% and 16.7% replace the rounded 29% and 17%; the 35-cell box ordering is used
consistently; the Janet redundancy row names the object it is measured on (with the caveat R-20);
and the parity split is printed in full with the statement that it does not cross. No check was
altered to make a discrepancy vanish (the Q5c fixture change of SOURCES.md §1 was read: it compares
an unordered pair and adds assertions; the search is untouched).

### A.2 Findings — content

**A-1 (BLOCKING) — abstract l.11, §0 l.24, Theorem 4's title l.131, Corollary 2 l.137.** "Fibring an
index cannot raise its total defect" and "Fibring never raises the total defect" are stated for a
fibration, which D5 (l.72) defines as *any* partition of X into non-empty parts. That is false.
Witness: X = {(0,0), (0,1), (1,0)} has ℛ(X) the full 2 × 2 box, E(X) = 1; the partition
{(0,1), (1,0)} ∪ {(0,0)} has fibred defect E({(0,1),(1,0)}) + E({(0,0)}) = 2 + 0 = 2 > 1
(recomputed with the seated operator: `E(X) = 1`, sum `2`). Theorem 4's *statement* is correct because
it restricts to fibring by coordinate 1, and that restriction is what makes the closures disjoint.
Resolve: define a fibration in D5 as the partition by the values of one coordinate (and, iterated, by
several); reword the abstract, §0 item 2 and the theorem's title to "fibring by a coordinate"; or keep
D5 general and add the counterexample as a remark after Theorem 4 stating that the inequality is
special to coordinate fibrations.

**A-2 (MAJOR) — Corollary 2, l.137.** "Refining a fibration by coordinate 1 therefore drives the total
defect to zero by refinement alone." Fibring by coordinate 1 alone leaves every fibre with d − 1 free
coordinates, and Theorem 4 says nothing about those fibres' defects. Reaching singletons needs
Theorem 4 applied to coordinate 1, then to coordinate 2 inside each fibre, and so on to d — legitimate
because ℛ is symmetric in the coordinates, but not said. Resolve: state Theorem 4 for fibring by any
coordinate i (the proof is unchanged), then in Corollary 2 iterate over i = 1, …, d and note that the
finest coordinate fibration is the singleton partition.

**A-3 (MAJOR) — Proposition 1, l.112–114; §5.2 l.379; §7 l.510.** The identity ℛ(X) = ⟨X⟩ on a finite
product of chains is "established in *The Hierarchy Law of Mathematical Languages* (Lach 2026) and is
CITED". That paper's own provenance ledger (§9) records the identity as **PRIOR ART, READ**:
Queyranne and Tardella (2008), Theorem 11, with Topkis (1976) and Veinott (1989) behind it, and its
lift to d ≥ 3 is cited there, not proved. The citation therefore misattributes, and the reference
carries no locator (R-21). The direction is also short enough to prove here: let x ∈ ℛ(X); for each
ordered pair i ≠ j pick z⁽ⁱʲ⁾ ∈ X attaining φ_ij(x_j) (so z_j ≤ x_j, z_i ≥ x_i), and pick w⁽ⁱ⁾ ∈ X with
w_i = x_i (D1); set u⁽ⁱ⁾ := w⁽ⁱ⁾ ∧ ⋀_{j≠i} z⁽ⁱʲ⁾. Then u⁽ⁱ⁾ ≤ x coordinatewise and u⁽ⁱ⁾_i = x_i, so
x = ⋁_i u⁽ⁱ⁾ ∈ ⟨X⟩. With Lemma 2 this is the equality, and Proposition 1 becomes a theorem (PROVED),
§5.2's "that direction is cited rather than proved here" and §7's "the general identity CITED" go, and
Corollary 1 becomes an equivalence. Resolve: add the proof, attribute the result to Queyranne and
Tardella (2008) (and Topkis 1976, Veinott 1989), and cite the hierarchy-law paper only where §6 uses
its containment clauses.

**A-4 (MAJOR) — §0 item 1, l.23.** "These are proved and machine-checked over every subset of three
named boxes" covers Theorem 1, Lemma 2 and Theorem 2. Only Theorem 1 is machine-checked (T1a–c);
Lemma 2 has no obligation at all; Theorem 2 is EXHAUSTIVE on 84 boxes. Statuses merged, in the
paragraph that says statuses are never merged. Resolve: "Theorem 1 is proved and machine-checked over
every subset of three named boxes; Lemma 2 is proved; Theorem 2 is proved and exhausted on 84 boxes."

**A-5 (MAJOR) — l.129 against §6 l.479–485.** "Every index in this paper has all coordinates ordered:
they are counts, dates, ranks and quantum numbers." The discriminating case of §6 is the periodic
table with the **block** adjoined — a categorical coordinate (s, p, d), coded by the instrument as
0, 1, 2 (`_periodic(True)`: s for g ≤ 2, p for g ≥ 13, d otherwise), an order that is neither the
group order (s < d < p) nor anything the paper states. By the paper's own Corollary at l.129, the
E = 100 / 100 / 83 / 24 / 0 row "reports a property of an arbitrary ranking and is not a measurement of
the index". Resolve: either replace block by an ordered quantity with a stated order (for example the
ℓ of the differentiating subshell, 0/1/2, with the coding printed), and re-run L3–L5; or keep the
table and say explicitly that the coordinate is categorical, that the order is the coding, and delete
or qualify the sentence at l.129.

**A-6 (MAJOR) — §6 l.475, l.485.** "There are C(5,2) = 10 pairs, and all ten agree" and "One of the
ten pairs agrees, order with algebra … Agreement among the languages is thus not automatic." The
order–algebra pair agrees on every finite index by the identity the paper itself cites at l.114 (and
measures in Proposition 1); the one agreeing pair in the discriminating case is exactly the pair that
cannot disagree. Resolve: report the pair counts over the four distinct operators (C(4,2) = 6: 6 of 6
on Λ, 0 of 6 on the three-coordinate table), or keep ten and state that one pair agrees by theorem.

**A-7 (MAJOR) — §3.5 l.220–226, thesis l.3, §0 l.25.** The χ = ±6 slice is the set
{(h¹¹, h²¹) : h¹¹ − h²¹ ∈ {−3, +3}} — a difference of two coordinates with value set {−3, +3}, a hole at
0. That is precisely the mechanism of §5.3: by Lemma 3 the join of a cell on one line with a cell on the
other lands on the diagonal, so E > 0 is forced by the slicing, exactly as E = 750 is forced by
|Δℓ| = 1. The paper says "the geometry is elementary" but does not connect it to its own Corollary 4,
and the thesis sentence presents the slice as one of fourteen indexes on which E "separates the closed
from the open". Resolve: state in §3.5 that the slice is open by construction (Lemma 3, value set
{−3, +3}), that the 540 are the cells Lemma 3 predicts, and remove the Kreuzer–Skarke slice from the
thesis sentence's separating claim; see also R-12.

**A-8 (MAJOR) — §3.7 l.236, Table 1 l.250, Table 2 l.292, §4.4.** The "spectroscopic survey grid" is
the product of the survey's element, core-charge and ℓ alphabets cut by c < Z. That cut is a monotone
bound, so the grid is a fixed point of ℛ by construction, and its 20% redundancy is a property of the
construction. The survey's own data — the **285 witnessed cells** — were closed here with the seated
operator: **E = 975 in a box of 1,960**. The paper's row therefore says nothing about the survey, and
the sentence "reading the unwitnessed count as E would say the index is open when it is closed" hides
that the witnessed index *is* open. Resolve: name the row "a product grid over the survey's alphabets";
either add the witnessed set's row (285 / 1,960 / 975) or drop "spectroscopic" from the row and from
the abstract's "atomic spectroscopy"; and say that Table 2's 20% and §4.4's 20% → 0% are measured on
the product grid.

**A-9 (MAJOR) — §4.3 l.317, l.283, Figure 3 caption.** The d = 3 row prints redundancy **0%** as a
SAMPLED figure with "ten trials per rung". No trial was run: the projection has 12 cells, ⌊0.05 × 12⌋ = 0,
and `redundancy()` breaks out at `k < 1` with an empty log (verified: `proj d=3 cells=12 redundancy=0
log=[]`). The number is a protocol stop, not a sample. The same stop would fire on any index under 20
cells. Resolve: print "below the ladder's resolution" for that row (or define D7 with ⌈t|X|⌉ and
re-run), and state the small-|X| rule in D7.

**A-10 (MAJOR) — §3.4 l.204–214, Table 1 l.255.** The particle-bound list carries no citation; it is
the instrument's hand-typed fixture. It is complete through Z = 8 but at Z = 9, 10 it omits nuclides
that NUBASE2020 records as particle-bound: F-29, F-31, Ne-17, Ne-29, Ne-31, Ne-32 and Ne-34. Closing
the completed set with the seated operator: Z ≤ 7 unchanged (52 / 61 / 9); Z ≤ 9 becomes 77 / 86 / 9;
**Z ≤ 10 becomes 94 / 106 / 12**, the three new admitted-and-absent cells being F-16, F-28 and F-30 —
all genuinely unbound, so the reading survives, but "none is added after Z ≤ 7: the defect is a
property of the measurement, not of the window" (l.214) and C7b/C7c fail on the completed data. The
headline E = 9 at Z ≤ 7 stands. Resolve: source the list from NUBASE2020 (Kondev, Wang, Huang, Naimi
and Audi 2021), cite it, recompute the five rows, and replace the stability sentence by what the
completed data show.

**A-11 (MINOR) — Table 1 note, l.240.** The two nuclide boxes are withheld as "not a meaningful
comparator" because they are "set by the largest Z and N present"; every box in the table is set the
same way (the Kreuzer–Skarke box 12,544 = 112² most of all). The boxes are 119 (Z ≤ 7: 7 × 17) and
21,182 (AME2020: 119 × 178). Resolve: print them and delete the note.

**A-12 (MINOR) — Proposition 1, l.112.** "the periodic table (126 cells), the Kreuzer–Skarke slice
(748) and the parity set of §5.3 (1,590)" — those are the closures' sizes; the indexes have 90, 208 and
840 cells. Resolve: "(90 cells, closure 126)" and likewise.

**A-13 (MINOR) — l.186.** "φ(group | period ≤ 1)" is not D3's notation. Resolve: φ_group,period(1).

**A-14 (MINOR) — §0 item 3, l.25.** "Fourteen indexes" followed by a list of thirteen: the dipole
image (Table 1 row 8) is missing. Resolve: add it, or say "fourteen, of which three are full boxes".

**A-15 (MINOR) — Theorems 5 and 6 l.143–149, D8 l.78, Corollary 3 l.159.** D8 and Corollary 3 take
h : X → C; Theorems 5 and 6 take h : B → C on the whole box. Corollary 3 applies Theorem 6 to a map
defined only on X. Harmless (extend h arbitrarily off X; the proofs use h only on S), but unsaid.
Resolve: one sentence in Corollary 3's proof.

**A-16 (MINOR) — Corollary 3, l.159.** "fail to preserve the meet or the join at some pair of cells of X
whose meet or join is in X" — with X closed every meet and join is in X (Corollary 1), so the qualifier
is vacuous. Resolve: delete the clause.

**A-17 (MINOR) — Refutation 1, l.155.** "Z3 independently reports the converse satisfiable over every
S and h on that box" — satisfiability is existential. Resolve: "Z3 finds an S and an h on that box
satisfying the converse's negation".

**A-18 (MINOR) — "Corollary (ordered coordinates only)", l.129.** Unnumbered, unproved, no ∎; it is a
remark, and its first sentence is the source's D.1 sentence verbatim in substance. Resolve: "Remark 1".

**A-19 (MINOR) — Theorem 3(a), l.124.** A bijection of any |X| = ab cells onto a full a × b box has
defect 0 by Theorem 2; this is a remark on Theorem 2, not a theorem. (The relabelling instances C16a/b
are checks of Theorem 2.) Resolve: fold (a) into a remark and let Theorem 3 be the calendar witness.

**A-20 (MAJOR) — D7 l.76, Table 2 l.291, §4.3, abstract.** "61%", "20%", "30%", "5%" are the largest
rungs passed on a ladder of 5, 10, 20, 30, 41, 50, 61, 70, 82, 90 per cent, at an acceptance of 8 of 10.
The check's log shows how close the passes are: Λ passes 61% at **8/10** and fails 70% at 6/10; the
survey grid passes 20% at 8/10 and fails 30% at 5/10; the box ordering fails 5% at 7/10. The ladder's
rungs 41, 61 and 82 are unexplained, and the paper prints "61%" as if it were a measurement to the
percent. The T = 5 branch of D7 is never exercised (the largest census index is 976 cells). Resolve:
say in D7 that the ladder is a convention, print each figure as "passes 61%, fails 70%" (the per-rung
counts D7 promises are in the check's log but not in the paper), and drop the unused branch.

**A-21 (MINOR) — §4.3, l.319.** "falls by a factor of twelve between eight coordinates and four" is
61/5, the ratio of two ladder rungs. Resolve: delete.

**A-22 (MINOR) — §3.1 l.173, §5.4 l.425.** "A cell is a one-electron transfer: q electrons are taken …
and g of them are placed" — q runs to 3; the q − g electrons that are taken and not placed are not
accounted for; and cells with (n, ℓ) = (e, f) or with q = g = 0 are cells of Λ (the |ΔS| witness at
l.425 is 1s → 1s with q = 0). Resolve: say what a cell is — a transfer type of up to three electrons,
including the null transfer — or restrict the wording to what the coordinates say.

**A-23 (MINOR) — D11, l.464–465.** "information: the join-irreducible elements of X, closed under ∨"
is undefined for an X that is not a lattice. The instrument's reading: x ∈ X is a generator when x is not
the coordinatewise join of the cells of X strictly below it (the bottom included). "statistics: … the
support of the maximum-entropy distribution on the order-2 marginals, which iterative proportional
fitting sends to zero exactly when a pairwise projection is unobserved" — the set formula is the
operator; the sentence about the fit is only true when the fit exists (a 2 × 2 × 2 table with zeros at
(1,1,1) and (2,2,2) has positive two-way margins and no maximum-likelihood fit — Haberman 1974).
Resolve: define the generator set as the instrument does; state statistics as the set formula and drop
or qualify the IPF clause.

**A-24 (MINOR) — Table 3 l.442 against §5.4 l.429.** "dipole-allowed" is |Δℓ| = 1 in Table 3 and
|Δℓ| = 1 and ΔS = 0 (264 cells) in §5.4. Resolve: one meaning; call Table 3's class "|Δℓ| = 1".

**A-25 (MINOR) — §5.3 l.381–383, Table 3.** |Δℓ| = 1 is called "the parity rule"; Table 3 calls
"parity-conserving/-changing" the parity of Δℓ. On Λ₉ (ℓ, f ≤ 1) the two coincide; on the §5.5
population (Δℓ up to 3) they do not, and the paper itself contrasts them there. Resolve: call |Δℓ| = 1
the orbital (E1) rule throughout; see R-15.

**A-26 (MINOR) — §3.6, l.228–232, Table 1 l.252.** The section's object — occupation vectors over
infinitely many modes — is never built; what is computed is a 4³ box (Table 1 says so honestly:
"three capped oscillators"), closed by Theorem 2 like the chessboard. The d(N) computation (C10,
C10b) is correct and connected to no closure claim. Resolve: reduce §3.6 to the one sentence Theorem 2
needs, or say plainly that the row is a full box and the d(N) are decoration.

**A-27 (MINOR) — §3.4, l.216.** "(0, 0), which is empty" — the cell is the bottom of the box, admitted
by the closure of any set that contains (0, 1) (the neutron) and (1, 0) (H-1); it is an artefact of
indexing the neutron, not a nuclide. Resolve: say so, and count the diproton as the one admitted-and-absent nuclide.

**A-28 (MINOR) — References, l.553.** Janet's 1928 publication is *La classification hélicoïdale des
éléments chimiques* (Beauvais, Imprimerie Départementale de l'Oise); the 1929 title printed should be
verified against a catalogue. Resolve: cite the 1928 work for the table.

### A.3 Findings — the checks (`check.py`) and the verification record

Every printed number was matched to a line of the check's output (the row map is in A.1; the crossing's
five rows are Q8.; the join witnesses are Q6d.; the per-rung logs are R1.). The eight Z3 obligations
were read: T1a (extensive), T1b (monotone, own box), T1c (idempotent, own box), T4 (fibre closure ⊆
whole closure), T5a/b (graph closed ⇒ S closed), T6a/b (graph closed ⇔ h preserves ∧, ∨ on S). Each
encodes the operator the paper defines: `in_Rown` is D4 in witness form over the observed box;
`closedSp` is closure of the graph under coordinatewise ∧, ∨ with h(a ∨ b) = max(h(a), h(b)); the
converse witnesses are the paper's. Boxes named in the paper match the code (3 × 3, 2 × 2 × 2, 3 × 3 × 3;
h into a 3-chain and a 2-chain).

**A-29 (MAJOR) — T5a, T5b, T6a, T6b (check.py l.390–456); §7 l.534.** The paper's MACHINE-CHECKED
requires "both guards passed", and §7 says "The two guards on every machine check". The only
encoding-fidelity guard (T0a) evaluates the ℛ-membership formula against the seated operator; the four
adjunction obligations do not use that formula. Their encodings (`closedS`, `closedSp`, `hom`) are
never evaluated against a concrete implementation; the one enumerated witness (T5ac/T5bc) corroborates
`closedSp` at a single instance. Resolve: add a guard that evaluates `closedS` and `closedSp` on random
(S, h) over the two boxes against an enumerative test, report it before T5/T6, and make §7's sentence
true; or downgrade the four to "Z3-checked, fidelity guard not run" — the contract has no such status,
so the guard is the repair.

**A-30 (MINOR) — T0c; T1a, T1c; T6.** The non-vacuity guard for Theorem 1(b) runs on 3 × 3 only, while
the obligations run on three boxes; T1a and T1c have no non-trivial hypothesis (a non-empty X), which
should be said; T6a/b have no guard line of their own and rely on T5ag/T5bg (the same hypothesis
shape), which §7 does not say. Resolve: run T0c per box; state which obligations have a hypothesis to
guard.

**A-31 (MINOR) — T5ag/T5bg (check.py l.409–411).** "h non-constant" is demanded on the whole box, not
on S, so the guard admits a graph on which h is constant. Resolve: `z3.Or([And(S[a], S[b], h[a] != h[b]) …])`.

**A-32 (MINOR) — §7 table, l.513.** "Theorem 4 … ✓ 3 obligations, same three boxes" — T4 is one
obligation over three boxes (the count of eight is right only if it is one). Resolve: "1 obligation,
three boxes".

**A-33 (MINOR) — §7 table, l.526.** "Tables 2 and 3, redundancy" — Table 3 is the crossing. The
redundancy data are Table 2 and the untitled tables of §4.3 and §4.4. Resolve: number those tables and
name them here.

**A-34 (MINOR) — check.py labels.** Q3 (l.826) says "Lemma 2 (interval property)" — the paper's
Lemma 3; C16a/b (l.694) say "Corollary 1" — the paper's Theorem 3(a). Resolve: relabel.

**A-35 (MINOR) — Theorem 4's status line, l.135.** T4 encodes only the inclusion ℛ(X_v) ⊆ ℛ(X)
(which is Theorem 1(b) for X_v ⊆ X); disjointness and the inequality are not encoded. §7 says "(the
inclusion)"; the theorem's own status line says "MACHINE-CHECKED (the inclusion ℛ(X_v) ⊆ ℛ(X))" —
adequate, but a reader of the bold word alone will take the theorem as checked. Resolve: "the inclusion
only; the rest is proved".

**A-36 (MINOR) — R3 (check.py l.778), D7 l.76.** D7 promises "the seed and the per-rung trial counts
are printed with every figure"; R3 prints the rung reached and no counts, and the paper prints none of
the R1. counts either (see A-20). Resolve: print the logs.

**A-37 (MINOR) — status choice, §0 l.31–40, §3.4, §5.5.** The AME2020 defect (C8, C8b) and the
crossing (Q8) are numbers computed from cited data by a stated procedure — the contract's MEASURED —
and are labelled EXHAUSTIVE; the paper's status table omits MEASURED and then uses "measured"
informally in Proposition 1's title and throughout §5. Resolve: adopt MEASURED for those rows, or keep
EXHAUSTIVE and stop using "measured" as a quasi-status.

### A.4 Findings — figures

Figure 1 is the audited plate, md5 as recorded; its caption's 90 / 36 / 126 and the three runs are C2
and C2b. Figure 2's eleven bars and their labels are C1, C2, C3, C4, C5, C6, C7, C8b, C9, C12a, Q1b,
and its caption's numbers are all in the check. Figure 3's left panel is R3 and its right panel R1/R2
(the coincident points are labelled together, as the caption says). Figure 4's ten bars are the Q8.
rows to the printed decimal. `figures.py` reads `check.compute_all()` and refuses to draw on a failure.

**A-38 (MINOR) — Figure 1, p.8.** The plate's internal title "36 cells the structure admits and the
table denies" is set across the first row of cells and collides with them; the plate has no legend
(the caption supplies blue/red). Resolve: re-plot from C2/C2b in `figures.py` with the title above the
axes, or crop the title.

**A-39 (MINOR) — Figure 2 caption, l.259.** "eleven of the indexes of Table 1" — the three omitted
(Λ₁₀, the survey grid, the capped oscillators) are not named. Resolve: name them.

### A.5 Findings — lint and the rendered PDF

Lint: 0 hits. Rendering: pandoc + WeasyPrint, 21 pages, every figure present with its caption beneath
it, every table inside its column, no cell clipped, `⟨X⟩` and `∣` glyphs present (checked at 3×).

**A-40 (MAJOR) — every page.** All mathematics is set in monospace code font: 535 code spans, from the
abstract's `d` and `E(X) = |ℛ(X)| − |X|` on p.1 to D11 on p.17 and the Refutation witnesses on p.15.
PAPER-SPEC §9: "A backtick code span is for code and never for mathematics." Resolve: convert every
code span to plain Unicode text; put the displayed definitions in indented blocks.

**A-41 (MAJOR) — pp.4–5 (l.98, l.100–104, l.124–125).** Theorem 1's statement "(a) … (b) … (c)"
renders as an ordered list — "1. X ⊆ ℛ(X); (b) …; (c) …"; its proof's parts (b) and (c) render as
"1." and "2." while the text refers to (a), (b), (c); Theorem 3's "(a)", "(b)" render as "1.", "2."
while its proof refers to (a) and (b). Cause: a line beginning "(a)" is a pandoc fancy-list marker.
Resolve: keep the three clauses on one line, or escape the marker ("(a)\ " or "\(a)").

**A-42 (MINOR) — pp.2–3, pp.18–19, p.10.** "Status words. Six are used and never merged." ends p.2
with its table on p.3; "By object." ends p.18 with its table on p.19; p.10 is half blank below Table 1
because Figure 2 could not fit. Resolve: a keep-with-next rule for a paragraph before a table in the
template, or move the lead-ins.

**A-43.1–A-43.45 (MINOR each) — 45 lines, 113 instances of `_`, `^` or `^{}` inside a code span,
rendering literally on the page** (φ_ij, A_i(X), x_i, X_v, Σ_v, φ^X_ij, φ^{ℛ(X)}_ij, S^h, X^h, N_e,
q^N, ∏_{n≥1}, Σ_{k=1}^{N}, π_ij, s_m, t_n, …). Per the brief each instance is a finding; one row per
line, the count of instances on that line in brackets:

| finding | line | instances | what renders literally |
|---|---|---|---|
| A-43.1 | 50 | 1 | `A_i(X) := { x_i : x ∈ X }` |
| A-43.2 | 52 | 1 | `Box(X) := A_1(X) × ⋯ × A_d(X)` |
| A-43.3 | 54 | 2 | `(x ∧ y)_i = min(x_i, y_i)`, `(x ∨ y)_i = …` |
| A-43.4 | 56 | 1 | `∣Box(X)∣ = ∏_i ∣A_i(X)∣` |
| A-43.5 | 58 | 1 | `a ∈ A_j(X)` |
| A-43.6 | 60 | 1 | `φ_ij(a) := max { y_i : y ∈ X, y_j ≤ a }` |
| A-43.7 | 62 | 1 | `φ_ij` |
| A-43.8 | 66 | 1 | `ℛ(X) := { x ∈ Box(X) : x_i ≤ φ_ij(x_j) … }` |
| A-43.9 | 72 | 4 | `X_v := …`, `v ∈ A_1(X)`, `{X_v}`, `Σ_v E(X_v)` |
| A-43.10 | 74 | 4 | `M_i := max A_i(X)`, `φ_ij`, `φ_ij(a) < M_i`, `a ∈ A_j(X)` |
| A-43.11 | 78 | 2 | `C = C_1 × ⋯ × C_m`, `X^h := …` |
| A-43.12 | 92 | 3 | `a ∈ A_j(X)`, `φ_ij(a)`, `φ_ij(a) ≤ φ_ij(a')` |
| A-43.13 | 94 | 3 | `y_j = a`, `{ y ∈ X : y_j ≤ a }`, `… ⊆ { y ∈ X : y_j ≤ a' }` |
| A-43.14 | 100 | 3 | `x_i ∈ A_i(X)`, `{ y ∈ X : y_j ≤ x_j }`, `φ_ij(x_j) ≥ x_i` |
| A-43.15 | 102 | 7 | `A_i(X) ⊆ A_i(S)`, `x_j ∈ A_j(X) ⊆ A_j(S)`, `φ^S_ij(x_j)`, … |
| A-43.16 | 104 | 6 | `A_i(ℛ(X)) = A_i(X)`, `φ^{ℛ(X)}_ij ≥ φ^X_ij`, `y_j ≤ a`, … |
| A-43.17 | 108 | 6 | `(x ∨ y)_i = max(x_i, y_i)`, `x_i ≤ φ_ij(x_j) ≤ …`, … |
| A-43.18 | 118 | 4 | `y_i = max A_i(X)`, `y_j = x_j`, `y_j ≤ x_j`, `φ_ij(x_j) = max A_i(X) ≥ x_i` |
| A-43.19 | 129 | 1 | `φ_ij` |
| A-43.20 | 131 | 3 | `{X_v}_{v ∈ A_1(X)}`, `ℛ(X_v)`, `⋃_v ℛ(X_v) ⊆ ℛ(X)` |
| A-43.21 | 133 | 1 | `Σ_v E(X_v) ≤ E(X)` |
| A-43.22 | 135 | 10 | `X_v ⊆ X`, `ℛ(X_v) ⊆ ℛ(X)`, `Box(X_v)`, `A_1(X_v) = {v}`, `Σ_v ∣ℛ(X_v)∣ = …`, … |
| A-43.23 | 143 | 2 | `S^h := { (x, h(x)) : x ∈ S } ⊆ B × C`, `S^h` |
| A-43.24 | 145 | 3 | `S^h` ×3 |
| A-43.25 | 147 | 1 | `S^h` |
| A-43.26 | 149 | 3 | `S^h` ×3 |
| A-43.27 | 151 | 1 | `S^h` |
| A-43.28 | 155 | 2 | `S^h = { ((0,0), 1), ((1,1), 0) }`, `S^h` |
| A-43.29 | 157 | 1 | `((1,1,1), 1) ∉ S^h` |
| A-43.30 | 159 | 1 | `E(X^h) > 0` |
| A-43.31 | 161 | 2 | `X^h`, `E(X^h) > 0` |
| A-43.32 | 230 | 3 | `q^N`, `∏_{n≥1} (1 − q^n)^{−24}`, `d(N) = (24/N) Σ_{k=1}^{N} σ(k) d(N−k)` |
| A-43.33 | 283 | 2 | `φ_ij`, `max A_i(X)` |
| A-43.34 | 325 | 1 | `N_e = Z − c + 1` |
| A-43.35 | 337 | 4 | `N_e`, `N_e = 3`, `N_e = 2` ×2 |
| A-43.36 | 353 | 1 | `g(x) = x_i − x_j` |
| A-43.37 | 355 | 4 | `s₁ = a_i`, `s₂ = b_i`, `t₁ = a_j`, `t₂ = b_j` |
| A-43.38 | 357 | 3 | `s_m = max(s₁, s₂)`, `t_n = max(t₁, t₂)`, `t_n ≥ t_m` |
| A-43.39 | 359 | 1 | `g(a ∨ b) = s_m − t_n ≤ s_m − t_m = g_m` |
| A-43.40 | 361 | 1 | `s_m ≥ s_n` |
| A-43.41 | 363 | 1 | `g(a ∨ b) = s_m − t_n ≥ s_n − t_n = g_n` |
| A-43.42 | 365 | 1 | `g_n ≤ g(a ∨ b) ≤ g_m` |
| A-43.43 | 367 | 6 | `s_m = min(s₁, s₂)`, `t_n = min(t₁, t₂)`, `t_n ≤ t_m`, … |
| A-43.44 | 463 | 2 | `{ x ∈ Box(X) : (x_i, x_j) ∈ conv(π_ij X) … }`, `π_ij` |
| A-43.45 | 465 | 1 | `{ x ∈ Box(X) : π_ij(x) ∈ π_ij(X) … }` |

Resolve (all): write φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, qᴺ, πᵢⱼ, sₘ, tₙ in Unicode; put φ^X_ij,
φ^{ℛ(X)}_ij, ∏_{n≥1}(1 − qⁿ)⁻²⁴ and Σ_{k=1}^{N} in display blocks or rephrase (φˣᵢⱼ against φˢᵢⱼ, or
"the envelope of X" and "of S").

**A-44.1–A-44.7 (MINOR each) — `\|` in table cells at lines 251, 265, 410, 412, 413, 442, 443.**
Pandoc renders each as a plain bar and the tables hold, but PAPER-SPEC §9 forbids the form. Resolve:
∣ (U+2223) in every table cell — (∣Δℓ∣, ∣ΔS∣), ∣ℛ(X)∣, ∣ΔS∣ = 0, ∣Δℓ∣ = 1, ∣Δℓ∣ = 0, ∣Δℓ∣ ≠ 1.

---

## Part B — reader audits

### B.1 A mathematician (closure systems, constraint networks), who has not seen this material

I read the definitions first and they are, with two exceptions, adequate: D1–D4 define the operator
completely, and Lemma 1 disposes of the empty-maximum question that usually trips such definitions.
The proofs of Theorem 1, Lemma 2, Theorem 2, Theorems 5 and 6, Lemma 3 and Corollaries 1, 3, 4 are
correct and complete; I checked each step. What is missing is the one sentence that would make the
paper a paper rather than a catalogue.

**R-1 (MAJOR) — §2.1, l.106–118.** The object the paper studies is well known under other names. ℛ is
the bounds-consistency (2-consistency with monotone bounds) closure of constraint-network theory
(Montanari 1974; Mackworth 1977; Freuder 1978), and its fixed points on a product of chains are
*exactly the sublattices of the box* — Queyranne and Tardella's Theorem 11 (2008), resting on Topkis
(1976) and Veinott (1989): a subset of a product of chains is a sublattice iff it is determined by its
pairwise projections, each of which is an order-convex "staircase". Once this is stated as Theorem 0
(the proof is the six lines in A-3), Corollary 1 becomes an equivalence, Proposition 1 stops being a
measurement, Corollary 4 is the statement that an interval condition on a lattice homomorphism to ℤ
cuts a sublattice, and the Kreuzer–Skarke defect, the parity defect and the calendar are three
instances of one fact: a value set with a hole is not a sublattice. Resolve: add Theorem 0 with its
attribution, and let §3 and §5 cite it where they now say "the geometry is elementary".

**R-2 (MAJOR) — §6, l.467, l.487.** "Each returns a superset of X" is asserted for the information
operator without the generator definition that makes it true (A-23); and "the five languages agree
exactly when all five defects are zero" has one trivial direction (all E = 0 ⇒ every operator returns X
⇒ agreement) and a converse that is false in general (five operators can agree on a common proper
superset of X) — the paper calls the pair "one instance of a general law" and cites the hierarchy-law
paper, whose clauses are containments between operators, not this equivalence. Resolve: prove the
trivial direction in one line, say the converse is measured on four indexes and is not a law, and
remove "one instance of a general law".

**R-3 (MINOR) — D6, l.74.** "φ_ij binds when φ_ij(a) < M_i for at least one a" is "φ_ij is not the
constant M_i", i.e. the envelope is non-constant; say so, since "binds" suggests a cell is excluded,
which a non-constant envelope need not do when X is a full box on those two coordinates.

**R-4 (MINOR) — throughout.** S is a superset of X in Theorem 1(b), a subset of B in Theorems 5–6, and
a spin in 2S, 2S′. Resolve: Y for the superset.

**R-5 (MINOR) — D10, l.82.** log₂ C(∣ℛ(X)∣, E) is a description length under a uniform code over
E-subsets, not an entropy and not additive over fibres; "bit cost" is fine if the sentence says which
code. Resolve: one clause.

Beyond these I concur with A-1, A-2 (a fibration must be a coordinate fibration for Theorem 4, and
Corollary 2 needs iteration), A-3, A-5 (a categorical coordinate in §6's only discriminating example),
A-6, A-15, A-16, A-18 and A-19. Nothing here would be rejected by a referee in *Order* for being wrong;
Theorem 3(a), the unnumbered Corollary and Proposition 1 as "measured" would be rejected as padding
around a result that is prior art and should be cited as such.

### B.2 A physicist (nuclide chart, string compactification, atomic spectra)

**R-6 (BLOCKING) — §5.5 l.433–449, Table 3, Figure 4, abstract l.11, §0 l.27, thesis l.3.** The
crossing is computed on 4,325 "moves" (Z, n, ℓ, k, q, e, f, g) with 1 ≤ g ≤ min(q, 4f + 2). The bound
4f + 2 is the target subshell's capacity, not its room: the population never asks how many electrons
(e, f) already holds. I counted with the paper's own population builder: **2,923 of the 4,325 moves
place g electrons into a subshell that is already full** (every move into 1s² of every element beyond
helium, for a start), and 2,819 move more than one electron, to which the electric-dipole rule does not
apply. Restricting to physical one-electron moves — q = g = 1 with the target's occupancy below
4f + 2 — leaves 134 moves, and on them: within one element, |Δℓ| = 1 followable 7 of 59 (11.9%)
against forbidden 14 of 75 (18.7%); across the 118, 24 of 59 (40.7%) against 48 of 75 (64.0%). The
forbidden class leads in both scopes: **there is no crossing**. The abstract's sentence "within one
element a dipole-allowed transition is followable 11.6% of the time against 40.7% for a forbidden one,
while across the 118 elements the order reverses" is a fact about a population that is two-thirds
Pauli-forbidden. Resolve: restrict the population to physical one-electron moves with room in the
target, define followability on the resulting configuration (R-7), recompute Table 3 and Figure 4, and
if the crossing does not survive, remove it from the thesis, the abstract and §0 and keep Table 3 as
bookkeeping with the population stated.

**R-7 (MAJOR) — D9 l.80, §3.1 l.180, §5.5 l.435.** "Followable when its target — the subshell (e, f) at
the occupancy g it delivers — is itself the source subshell, at that occupancy, of some move": this
matches the number of electrons *delivered* (g) against the number a source subshell *holds* (k). A
move that delivers one electron to 3d of an element whose 3d holds nine is "followable" by any move
that removes electrons from a 3d holding one. That is not succession of states; it is a coincidence of
two integers. SOURCES.md §5.3 says the reading was chosen because it reproduces 0 / 1,169 / 2,050.
Resolve: define followability on configurations (after the move the target holds k_e + g; a move
follows when some move's source is (e, f) at occupancy k_e + g in the same element), or say plainly
that the match is formal and carries no physical reading.

**R-8 (MAJOR) — §5.1 l.351, §5.4 table l.410–413.** The 814 cells with Δℓ = 0 are labelled **M1**.
A magnetic-dipole transition connects levels of the same configuration (Δn = 0 in the single-
configuration picture; the M1 operator has no radial part); a jump between different subshells with
Δℓ = 0 is parity-conserving and is E2 or higher, or forbidden. Cells with (n, ℓ) = (e, f) — which Λ
contains — are the only ones the label fits. Resolve: name the two classes "Δℓ = 0 (parity conserved)"
and "|Δℓ| = 1 (E1)", and drop M1, or restrict M1 to n = e.

**R-9 (MAJOR) — §3.4, l.216.** "(2, 0), the diproton, which is unbound and is the textbook failure of
the pairing term." The semi-empirical pairing term favours even–even nuclei and would make ²He *more*
bound, not less; the diproton is unbound because the spin-singlet nucleon–nucleon interaction is just
too weak to bind (the deuteron binds only in the triplet channel) and Coulomb repulsion adds to that.
It is a failure of the mass formula at A = 2 altogether, not of its pairing term. Resolve: rewrite the
clause; the reading of §3.4's nine as pairing and clustering is separately marked as interpretation
and can stay.

**R-10 (MAJOR) — §3.4, l.204–214 (with A-10).** The particle-bound list needs its source, and the
source is NUBASE2020: Kondev, F. G., Wang, M., Huang, W. J., Naimi, S. and Audi, G. (2021), *Chinese
Physics C* **45**, 030001. Against it the fixture misses F-29, F-31, Ne-17, Ne-29, Ne-31, Ne-32 and
Ne-34, and with them E at Z ≤ 10 is 12, admitting F-16, F-28 and F-30 — each a real unbound nuclide,
so the chart's story improves (three more named cells) while the paper's stability sentence fails.
Resolve: as A-10.

**R-11 (MINOR) — §3.5, l.220, Table 1 l.257.** h¹¹ and h²¹ read as eleventh and twenty-first powers.
Resolve: h¹˒¹ and h²˒¹, or h(1,1) and h(2,1) in the text with the standard form in a display.

**R-12 (MAJOR) — §3.5, l.220–226, §0 l.29.** The χ = ±6 slice is a physically arbitrary subset of
the Hodge plot (the interest of χ = ±6 in Candelas et al. is three generations, which the paper does not
mention), and the 540 "predictions consistent with the published bounds" are cells of the region the
same authors describe as "essentially every site occupied" — the plot is known to be dense there. The
"four consistency tests" test nothing the published plot does not already show, and the paper's own
Lemma 3 says the slice must be open (A-7). An index whose cells are Hodge pairs is a sensible object
(30,108 distinct pairs); a slice of it by a non-monotone function is not an index of anything.
Resolve: either close the full Hodge-pair set (the file is public: the Kreuzer–Skarke list at
hep.itp.tuwien.ac.at/~kreuzer/CY) and report that, or state that the slice's E = 540 is Lemma 3 and drop
"predictions".

**R-13 (MINOR) — §3.6.** The transverse light-cone oscillators of the bosonic string are free, so
their occupation vectors form a product and Theorem 2 applies — one sentence. The section's d(N)
computation is correct (24-coloured partitions; the recurrence N d(N) = 24 Σ σ(k) d(N − k)) and
irrelevant to closure; the Table 1 row is a 4³ toy. Resolve: as A-26.

**R-14 (MINOR) — §5.4, l.408–415.** The "electromagnetic quotient" is the image of Λ₉ under
c ↦ (|Δℓ|, |ΔS|); that the image is the full 2 × 4 box says one physical thing — Δℓ and ΔS are
independent on Λ₉, every combination occurring — and the paper should say that instead of "vacuous".
Taking |ΔS| discards the sign of 2S′ − 2S with no reason given. Resolve: two sentences.

**R-15 (MINOR) — §5, l.343.** "Δℓ = ±1 (Laporte 1924)": Laporte's rule is the parity rule (even terms
combine only with odd); Δℓ = ±1 for a one-electron jump is the orbital selection rule that follows from
the rank of the dipole operator (Condon and Shortley 1935, ch. IV). Resolve: attribute each rule to its
statement.

**R-16 (MINOR) — §5.5, l.433.** The ground configurations are read from a local table attributed to
NIST ASD 5.12. I spot-checked Cr (3d⁵4s¹), Cu (3d¹⁰4s¹), Pd (4d¹⁰), La (5d¹6s²), Gd (4f⁷5d¹6s²), Th
(6d²7s²), Pa (5f²6d¹7s²), U (5f³6d¹7s²) and Lr (5f¹⁴7s²7p¹) and all agree with NIST; the other 109
were not checked. No change needed beyond saying the configurations are "as NIST tabulates them,
including its assignments for the ambiguous heavy elements".

**R-17 (MINOR) — §3.7 (with A-8).** "Core charge" is the charge of the parent ion, ionisation stage
plus one; the grid's only physics is c < Z. The witnessed 285 channels are the survey; their closure
is E = 975. An atomic physicist would want that number, not the grid's zero.

### B.3 A journal referee

**Does cataloguing the defects of unrelated objects support the thesis?** Only in part. The thesis
has three limbs. (i) *E is a property of the coordinatisation* — supported, by the calendar witness
and by Theorem 3, though Theorem 3(a) is the observation that any set is a box after relabelling and
Theorem 3(b) is one computation. (ii) *Across fourteen indexes E separates the closed from the open* —
of the fourteen rows, three are full boxes closed by Theorem 2 with no content (the chessboard, the
oscillators, the dipole image), three are one object and its two extensions (Λ, Λ₉, Λ₁₀), the survey
grid is closed by construction (A-8), and the Kreuzer–Skarke slice is open by construction (A-7). The
rows that carry information are Λ, Janet and the box ordering (closed with slack) against the periodic
table, the calendar and the two nuclide populations (open with every absent cell named) — seven, not
fourteen, and the paper's own D2 remark ("E = 0 carries information only when the box exceeds the
cells") says as much. (iii) *A selection rule acts as a quotient* — supported, by Theorems 5–6 and the
three extensions, and this is the paper's genuine contribution together with Lemma 3 / Corollary 4,
which explain in one line why one rule closes and the other does not.

**R-18 (MAJOR) — thesis l.3, abstract, Table 1, §3.** Restate the catalogue as what it is: three
full boxes (closed by theorem), one product grid (closed by construction), one non-interval slice (open
by Lemma 3), and seven informative rows; and restate the thesis over the seven. Resolve: split Table 1
into those groups and rewrite the thesis sentence.

**R-19 (MAJOR) — D7 l.76, §4.2 l.298, D9 l.80 (with A-20, R-7).** Three objects are presented as
definitions and were chosen because they reproduce numbers printed elsewhere: the redundancy ladder and
its 8-of-10 rule, the 724-cell Janet down-set ("so that the sampling has something to remove" is a
rationale written after the fact), and the g-against-k composability match. SOURCES.md §5.1, §5.3 and
§4.8 say so; the paper does not. A referee who learns this from the check rather than the text will
distrust every other definition. Resolve: motivate each independently in the paper, or state in D7, D9
and §4.2 that the protocol is a convention and give the rung interval and the trial counts.

**R-20 (MAJOR) — l.114, l.487, l.556.** *The Hierarchy Law of Mathematical Languages* (Lach 2026) is
cited twice: for ℛ(X) = ⟨X⟩, which that paper itself attributes to Queyranne and Tardella (2008) — the
paper is cited for what it proves only if "what it proves" includes what it imports — and for "the law
relating the containments among these five operators", which is a fair description of its Clauses A–H.
The reference has no venue, URL, DOI or status. Resolve: cite Queyranne and Tardella (2008), Topkis
(1976) and Veinott (1989) for the identity; keep the hierarchy-law citation for §6 only, with a locator
or "manuscript, 2026".

**R-21 (MAJOR) — §4.2, l.300–304.** A least-squares r² and a Student-t p-value are reported for six
points whose ordinate is quantised to a ten-rung ladder and is 0 at four of them. No assumption of the
test holds; the paper then says "the rows themselves make the point without the arithmetic". Resolve:
delete p (and the quadrature sentence); keep r² only as a descriptive number, or delete it too and let
the two sentences that follow carry the point.

**R-22 (MAJOR) — References.** Missing standard references, with full author lists:
- Queyranne, M. and Tardella, F. (2008). Bimonotone linear inequalities and sublattices of ℝⁿ.
  *Discrete Mathematics* **308**, 1508–1523. — the identity of Proposition 1.
- Topkis, D. M. (1976). The structure of sublattices of the product of n lattices. *Pacific Journal of
  Mathematics* **65**, 525–532.
- Veinott, A. F., Jr. (1989). Representation of general and polyhedral subsemilattices and sublattices
  of product spaces. *Linear Algebra and its Applications* **114/115**, 681–704.
- Baker, K. A. and Pixley, A. F. (1975). Polynomial interpolation and the Chinese remainder theorem for
  algebraic systems. *Mathematische Zeitschrift* **143**, 165–174. — the lift to d ≥ 3.
- Montanari, U. (1974). Networks of constraints: fundamental properties and applications to picture
  processing. *Information Sciences* **7**, 95–132; Mackworth, A. K. (1977). Consistency in networks of
  relations. *Artificial Intelligence* **8**, 99–118; Freuder, E. C. (1978). Synthesizing constraint
  expressions. *Communications of the ACM* **21**, 958–966. — ℛ as a consistency closure.
- Deville, Y., Barette, O. and Van Hentenryck, P. (1999). Constraint satisfaction over connected row
  convex constraints. *Artificial Intelligence* **109**, 243–271. — cited by the instrument's own
  documentation for the operator, dropped by the paper.
- Caspard, N. and Monjardet, B. (2003). The lattices of closure systems, closure operators, and
  implicational systems on a finite set: a survey. *Discrete Applied Mathematics* **127**, 241–269.
- Beeri, C., Fagin, R., Maier, D. and Yannakakis, M. (1983). On the desirability of acyclic database
  schemes. *Journal of the ACM* **30**, 479–513. — the agreement-iff-closure reading of §6.
- Ireland, C. T. and Kullback, S. (1968). Contingency tables with given marginals. *Biometrika* **55**,
  179–188; Haberman, S. J. (1974). *The Analysis of Frequency Data*. University of Chicago Press. — the
  statistics operator and the existence caveat (A-23).
- Kondev, F. G., Wang, M., Huang, W. J., Naimi, S. and Audi, G. (2021). The NUBASE2020 evaluation of
  nuclear physics properties. *Chinese Physics C* **45**, 030001; Huang, W. J., Wang, M., Kondev, F. G.,
  Audi, G. and Naimi, S. (2021). The AME 2020 atomic mass evaluation (I). *Chinese Physics C* **45**,
  030002. — particle-boundness and the evaluation's first part.
- von Weizsäcker, C. F. (1935). Zur Theorie der Kernmassen. *Zeitschrift für Physik* **96**, 431–458. —
  the mass formula the paper names.
- Madelung, E. (1936). *Die mathematischen Hilfsmittel des Physikers*, 3rd ed., Springer; Löwdin, P.-O.
  (1969). Some comments on the periodic system of the elements. *International Journal of Quantum
  Chemistry* **3S**, 331–334; Allen, L. C. and Knight, E. T. (2002). The Löwdin challenge: origin of the
  n + l, n (Madelung) rule for filling the orbital configurations of the periodic table. *International
  Journal of Quantum Chemistry* **90**, 80–88. — the (n + ℓ) rule §0 says it does not derive.
- Cowan, R. D. (1981). *The Theory of Atomic Structure and Spectra*. University of California Press. —
  multipole selection rules and coupling schemes (R-8, R-15).

**R-23 (MINOR) — abstract, l.11.** One paragraph of 430 words carrying some forty numbers, then a §0
that repeats most of them. Resolve: halve the abstract; leave the numbers to §0 and the tables.

**R-24 (MINOR) — §7, l.493.** "102 obligations" counts six R1. rows (one table), four L5. rows and
three Q6d. rows that are printouts of one obligation each, and five Q8. rows likewise. The count is of
printed lines. Resolve: "102 rows" or count obligations.

**R-25 (MINOR) — abstract and §0 against the body.** The abstract promises indexes "drawn from …
string compactification, atomic spectroscopy" and delivers a slice open by construction and a product
grid closed by construction (A-7, A-8); §0's "Five things" claims "the catalogue separates" over
fourteen where seven separate (R-18). Otherwise the abstract and §0 promise what the body delivers,
and the verification record is honest about what is sampled and what is cited, subject to A-4, A-29
and A-32–A-33.

---

## Part C — the record

| finding | line(s) | severity | disposition |
|---|---|---|---|
| A-1 fibring claim false for general partitions (abstract, §0, Theorem 4 title, Corollary 2) | 11, 24, 131, 137 | BLOCKING |  **FIXED.** D5 now defines a fibration by a coordinate (iterated for several); Theorem 4 is stated for any coordinate i and its title says so; abstract and §0 item 2 say 'fibring by a coordinate'; Remark 3 prints the audit's three-cell witness (E(X) = 1, fibred defect 2 + 0 = 2) as a REFUTATION (check.py T4b); T4 is machine-checked fibred over every coordinate of each box, 8 instances. |
| A-2 Corollary 2's refinement step needs iteration over all coordinates | 137 | MAJOR |  **FIXED.** Corollary 2 iterates Theorem 4 over i = 1, …, d inside each part and notes the last term is the singleton partition; check.py T4c verifies the chain is non-increasing and ends at 0 on all 766 subsets of 3×3 and 2×2×2. |
| A-3 Proposition 1's identity misattributed to Lach 2026; prior art; six-line proof available | 112–114, 379, 510 | MAJOR |  **FIXED.** Theorem 0 states ℛ(X) = ⟨X⟩ with the six-line proof (z⁽ⁱʲ⁾, w⁽ⁱ⁾, u⁽ⁱ⁾, x = ⋁ u⁽ⁱ⁾), attributed to Queyranne and Tardella 2008 (Thm 11) on Topkis 1976 and Veinott 1989, Baker–Pixley 1975 for the abstract form; Corollary 1 is an equivalence; Proposition 1 is folded into Theorem 0's EXHAUSTIVE corroboration (T3, T3b); the hierarchy-law manuscript is cited only in §6, marked Manuscript. |
| A-4 §0 merges statuses of Theorem 1, Lemma 2, Theorem 2 | 23 | MAJOR |  **FIXED.** §0 item 1 states each status separately: Theorem 1 proved and machine-checked, Lemma 2 proved, Theorem 0 prior art with proof and corroboration, Theorem 2 proved and exhausted on 84 boxes. |
| A-5 §6's block coordinate is categorical, against l.129 and the paper's own Corollary | 129, 479–485 | MAJOR |  **FIXED.** The third coordinate is stated as the ℓ of the column's block with the coding printed (0 for columns 1–2, 2 for 3–12, 1 for 13–18, helium carrying its column's value) and declared a choice of order (Remark 1 names it); check.py L3c verifies the instrument's coding is exactly that function of the group. The numbers are unchanged because the instrument's coding is the ℓ coding. |
| A-6 pair counts include the order–algebra pair that agrees by theorem | 475, 485 | MAJOR |  **FIXED.** §6 discounts the order–algebra pair (agrees by Theorem 0) and reports the six pairs among the four distinct operators: 6/6 on Λ, 6/6 on the box ordering, 0/6 on the three-coordinate table, 6/6 on Λ₉ (check.py L7); the ten-pair figures are kept beside them with the one-by-theorem stated. |
| A-7 Kreuzer–Skarke slice is open by construction (hole in a difference); thesis over-reads | 3, 25, 220–226 | MAJOR |  **FIXED.** §3.5 states the slice is open by construction: the value set of h(1,1) − h(2,1) is {−3, +3}, Corollary 4 does not apply, and the pair (13,16) ∨ (16,13) = (16,16) with difference 0 witnesses Corollary 1 (check.py C9d); the slice is in Table 1's 'open by construction' group and is out of the thesis's separating claim, which no longer exists. |
| A-8 survey grid closed by construction; the witnessed 285 cells have E = 975 | 236, 250, 292, 325–337 | MAJOR |  **FIXED.** The row is 'the product grid', closed by Proposition 2 (its cut Z − c ≥ 1 is bimonotone; T7d); the witnessed channels are a row of their own — 285 cells, box 1,960, |ℛ| = 1,260, E = 975 (C15b) — in §3.7, Table 1 and Figure 2; §4 says the 20% and 20% → 0% are figures of the grid; 'spectroscopic survey grid' is gone from the abstract. |
| A-9 d = 3 redundancy "0%" ran no trial | 283, 317, 321 | MAJOR |  **FIXED.** D7 states the small-|X| rule (no trial when ⌊0.05·|X|⌋ = 0, below 20 cells) and the d = 3 row prints 'below resolution, no trial: ⌊0.05 × 12⌋ = 0'; check.py R3. prints every rung log and R3c records the stop. |
| A-10 particle-bound list uncited and incomplete at Z = 9, 10; stability claim fails when completed | 204–214, 255 | MAJOR |  **FIXED.** The list is derived from NUBASE2020 (Kondev, Wang, Huang, Naimi and Audi 2021), cited: the evaluation's file was fetched from two independent public copies (byte-identical, md5 91e92411…), its Z ≤ 10 ground-state lines are kept verbatim as nubase2020-Z0-10.txt (md5 checked, C7), and the criterion is stated in §3.4. Six cutoffs printed — 27/33/6, 40/48/8, 52/61/9, 64/73/9, 77/86/9, 94/106/12 (C7a) — with F-16, F-28, F-30 named (C7b), every absent cell an unbound ground state (C7d), and the reason they appear only with neon (C7e). The stability sentence is replaced by 'the count is not stable; the reading is'. C7f records the fixture's seven omissions. |
| A-11 nuclide boxes withheld | 240 | MINOR |  **FIXED.** The boxes are printed for both nuclide rows and the Z ≤ 10 row (C7g, C8c: products of the observed alphabets) and the note is deleted. |
| A-12 closure sizes printed as cell counts in Proposition 1 | 112 | MINOR |  **FIXED.** Theorem 0's status line gives cells and closures: 90 → 126, 208 → 748, 840 → 1,590. |
| A-13 φ(group ∣ period ≤ 1) notation | 186 | MINOR |  **FIXED.** φ_group,period(1), named as the largest group reached at period 1. |
| A-14 thirteen indexes listed for fourteen | 25 | MINOR |  **FIXED.** §0 item 3 no longer enumerates; §3 says sixteen rows, fifteen indexes with the nuclides at two cutoffs, and Table 1 lists all sixteen with their group. |
| A-15 h's domain differs between D8/Corollary 3 and Theorems 5–6 | 78, 143–149, 159 | MINOR |  **FIXED.** Corollary 3's proof says h is extended from X to Box(X) arbitrarily, since Theorems 5 and 6 use h only on S = X. |
| A-16 vacuous clause in Corollary 3's hypothesis | 159 | MINOR |  **FIXED.** The clause is deleted; Corollary 3's hypothesis is 'fail to preserve the meet or the join at some pair of cells of X'. |
| A-17 "satisfiable over every S and h" | 155 | MINOR |  **FIXED.** Refutation 1 says Z3 finds an S and an h satisfying the negation of the converse; §7 likewise. |
| A-18 unnumbered, unproved "Corollary" is a remark | 129 | MINOR |  **FIXED.** It is Remark 1, unnumbered as a result and without ∎. |
| A-19 Theorem 3(a) is a remark on Theorem 2 | 124 | MINOR |  **FIXED.** Theorem 3(a) is Remark 2 (an instance of Theorem 2, with the two rectangles); Theorem 3 is the calendar witness alone; check.py C16a/b relabelled 'Remark 2'. |
| A-20 redundancy figures are ladder rungs; rungs unexplained; 8/10 passes marginal; unused branch | 76, 283, 291, 312–317 | MAJOR |  **FIXED.** D7 calls the ladder, the ten trials and the 8-in-10 acceptance conventions whose only justification is that they reproduce the previously reported rungs; Table 2 and §4.3 print the rung passed, the rung failed and the trial counts from the R1. and R3. logs; the redundancy column reads '61%' as a rung and 'below 5%' where the first rung fails; the T = 5 branch is removed (ten trials always). |
| A-21 "factor of twelve" is a ratio of rungs | 319 | MINOR |  **FIXED.** Deleted. |
| A-22 "one-electron transfer" with q ≤ 3; null and same-subshell cells | 173, 425 | MINOR |  **FIXED.** §3.1 says a cell is a transfer type of up to three electrons, the q − g not placed untracked, and that q = g = 0 and (n, ℓ) = (e, f) are cells. |
| A-23 information operator undefined for non-lattice X; IPF clause needs the existence caveat | 464–465 | MINOR |  **FIXED.** D11 defines the information operator via generators as the instrument computes it (with the induction that makes it extensive, Lemma 4) and states statistics as the set formula, with Ireland–Kullback 1968 for the fit and Haberman 1974 for its possible non-existence. |
| A-24 "dipole-allowed" has two meanings | 429, 442 | MINOR |  **FIXED.** One meaning: the mutual-information paragraph that used 'dipole-allowed' for |Δℓ| = 1 and ΔS = 0 is dropped (its rows Q7/Q7b remain in check.py, unprinted); Table 3's class is '|Δℓ| = 1 (allowed)'. |
| A-25 "parity rule" for ∣Δℓ∣ = 1 against Table 3's parity split | 381–383, 444–445 | MINOR |  **FIXED.** 'The orbital rule' throughout; Table 3's parity rows are 'Δℓ even' and 'Δℓ odd'; §5's opening attributes the parity rule to Laporte and the one-electron rule to Condon–Shortley. |
| A-26 §3.6's object is not built; the row is a 4³ box; d(N) decorative | 228–232, 252 | MINOR |  **FIXED.** §3.6 is Theorem 2's sentence and the 4³ instance; d(N) is not printed (C10/C10b remain in check.py). |
| A-27 (0, 0) is the box's bottom, an artefact of indexing the neutron | 216 | MINOR |  **FIXED.** §3.4 calls (0, 0) the bottom of the box, an artefact of indexing the neutron, and the diproton the one admitted-and-absent nuclide. |
| A-28 Janet reference: the 1928 work | 553 | MINOR |  **FIXED.** Janet, C. (1928). La classification hélicoïdale des éléments chimiques. Beauvais. |
| A-29 T5a/b, T6a/b lack the encoding-fidelity guard; §7's "two guards on every machine check" | check.py 390–456; 534 | MAJOR |  **FIXED.** check.py T0d evaluates the three Z3 predicates ('S closed', 'graph(h) closed', 'h preserves ∧, ∨ on S') under 240 random assignments of (S, h) over 3×3 and 2×2×2 against an enumerative decision (graph_truths) and T5/T6 are refused if it fails; §7's guard paragraph now describes it, so 'two guards on every machine check' is true. |
| A-30 non-vacuity guard on one box only; trivial hypotheses unstated; T6 has no guard line | check.py 508–511, 564–567; 534 | MINOR |  **FIXED.** T0c runs on each of the three boxes (three rows), a further T0c row states that Theorem 1(a), 1(c) and Theorem 4 hypothesise only a non-empty X, and T6a/T6b carry their own guard rows T6ag/T6bg; §7 says which obligations have a hypothesis to guard. |
| A-31 T5g's non-constancy is on the box, not on S | check.py 409–411 | MINOR |  **FIXED.** The non-constancy demand is z3.Or(And(S[a], S[b], h[a] != h[b])) — on S. |
| A-32 "Theorem 4 … 3 obligations" is one obligation | 513 | MINOR |  **FIXED.** '1 obligation, the inclusion only, 8 instances over three boxes and every coordinate'. |
| A-33 "Tables 2 and 3, redundancy" — Table 3 is the crossing | 526 | MINOR |  **FIXED.** The row reads 'Table 2, §4.3, §4.4, redundancy'. |
| A-34 check.py labels Q3 "Lemma 2", C16 "Corollary 1" | check.py 694, 826 | MINOR |  **FIXED.** Q3 says Lemma 3; C16a/b say Remark 2. |
| A-35 Theorem 4's MACHINE-CHECKED covers the inclusion only | 135 | MINOR |  **FIXED.** Theorem 4's status line: 'MACHINE-CHECKED — the inclusion ℛ(Xᵥ) ⊆ ℛ(X) only, the rest being the counting above'. |
| A-36 per-rung counts promised, not printed (R3 logs none) | 76, 283; check.py 778 | MINOR |  **FIXED.** The per-rung counts are printed in Table 2 and §4.3 (from R1. and R3. rows, which now print every log). |
| A-37 MEASURED absent from the status table while "measured" is used informally | 31–40, 112, 216, 433 | MINOR |  **FIXED.** MEASURED is the seventh status word in §0; check.py labels the NUBASE, AME2020, survey and followability rows MEASURED; 'measured' is no longer used as a quasi-status in a theorem title. |
| A-38 Figure 1 plate title collides with row 1; no legend | Figure 1, p.8 | MINOR |  **FIXED.** Figure 1 is regenerated by figures.py from C2/C2b with the title above the axes and a legend; FIGURES.tsv records the new md5 and the replaced plate. |
| A-39 Figure 2 caption does not name the three omitted rows | 259 | MINOR |  **FIXED.** Figure 2 shows all sixteen rows of Table 1, grouped, so nothing is omitted. |
| A-40 all mathematics in code font (535 spans) | every page | MAJOR |  **FIXED.** Every code span is gone: mathematics is plain Unicode text throughout, displayed formulas in indented blocks; the rendered PDF's text has no underscore, caret or backslash (pypdf extraction, repair record). |
| A-41 (a)/(b)/(c) of Theorem 1 (statement and proof) and Theorem 3 render as "1.", "2." | 98, 102, 104, 124–125; pp.4–5 | MAJOR |  **FIXED.** Theorem 1's clauses are on one line after the heading; its proof is headed 'Proof of (a)/(b)/(c)'; Theorem 3 has one clause. |
| A-42 orphaned lead-ins before two tables; half-blank p.10 | pp.2–3, 10, 18–19 | MINOR | **DECLINED.** The page template (`paper.html`) is shared by every paper and lies outside this paper's directory, which the drafter may not edit; the rewrite moved every break the audit named (the status-word lead-in and its table now share p.3, the §7 lead-in and its table share p.21), and every figure sits on one page with its caption under it, which the contract asks for. No heading is orphaned at a page foot in the 25-page render. |
| A-43.1 code-span mathematics, 1 instance | 50 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.2 code-span mathematics, 1 instance | 52 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.3 code-span mathematics, 2 instances | 54 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.4 code-span mathematics, 1 instance | 56 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.5 code-span mathematics, 1 instance | 58 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.6 code-span mathematics, 1 instance | 60 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.7 code-span mathematics, 1 instance | 62 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.8 code-span mathematics, 1 instance | 66 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.9 code-span mathematics, 4 instances | 72 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.10 code-span mathematics, 4 instances | 74 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.11 code-span mathematics, 2 instances | 78 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.12 code-span mathematics, 3 instances | 92 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.13 code-span mathematics, 3 instances | 94 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.14 code-span mathematics, 3 instances | 100 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.15 code-span mathematics, 7 instances | 102 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.16 code-span mathematics, 6 instances | 104 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.17 code-span mathematics, 6 instances | 108 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.18 code-span mathematics, 4 instances | 118 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.19 code-span mathematics, 1 instance | 129 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.20 code-span mathematics, 3 instances | 131 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.21 code-span mathematics, 1 instance | 133 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.22 code-span mathematics, 10 instances | 135 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.23 code-span mathematics, 2 instances | 143 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.24 code-span mathematics, 3 instances | 145 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.25 code-span mathematics, 1 instance | 147 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.26 code-span mathematics, 3 instances | 149 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.27 code-span mathematics, 1 instance | 151 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.28 code-span mathematics, 2 instances | 155 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.29 code-span mathematics, 1 instance | 157 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.30 code-span mathematics, 1 instance | 159 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.31 code-span mathematics, 2 instances | 161 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.32 code-span mathematics, 3 instances | 230 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.33 code-span mathematics, 2 instances | 283 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.34 code-span mathematics, 1 instance | 325 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.35 code-span mathematics, 4 instances | 337 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.36 code-span mathematics, 1 instance | 353 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.37 code-span mathematics, 4 instances | 355 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.38 code-span mathematics, 3 instances | 357 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.39 code-span mathematics, 1 instance | 359 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.40 code-span mathematics, 1 instance | 361 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.41 code-span mathematics, 1 instance | 363 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.42 code-span mathematics, 1 instance | 365 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.43 code-span mathematics, 6 instances | 367 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.44 code-span mathematics, 2 instances | 463 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-43.45 code-span mathematics, 1 instance | 465 | MINOR |  **FIXED.** Rewritten in Unicode (φᵢⱼ, Aᵢ(X), xᵢ, Xᵥ, Σᵥ, Sʰ, Xʰ, Nₑ, πᵢⱼ; the envelope of a named index as φᵢⱼ[X]; the old Lemma 3 proof replaced by Lemma 3's two-line argument in xᵢ, yⱼ); the line no longer carries a code span. |
| A-44.1 `\|` in a table cell | 251 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.2 `\|` in a table cell | 265 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.3 `\|` in a table cell | 410 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.4 `\|` in a table cell | 412 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.5 `\|` in a table cell | 413 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.6 `\|` in a table cell | 442 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| A-44.7 `\|` in a table cell | 443 | MINOR |  **FIXED.** ∣ (U+2223) in every table cell. |
| R-1 the operator is the bounds-consistency closure; fixed points are the sublattices (Queyranne–Tardella); state as Theorem 0 | 106–118 | MAJOR |  **FIXED.** Theorem 0 (Queyranne–Tardella) with proof and attribution; the Remark after it names ℛ as a pairwise-consistency closure of a connected-row-convex network (Montanari 1974; Mackworth 1977; Freuder 1978; Deville–Barette–Van Hentenryck 1999) and cites Caspard–Monjardet 2003; §3.5 and §5.3 cite Corollary 1 and Corollary 4 where they said 'the geometry is elementary'; Lemma 3 (bimonotone cut) makes Λ's, the grid's and the box ordering's zeros theorems (Proposition 2). |
| R-2 "each returns a superset" unproved for information; "agree iff all E = 0" has a trivial direction and a false converse | 467, 487 | MAJOR |  **FIXED.** Lemma 4 proves each operator returns a superset (information via the generator induction); §6 states the trivial direction in one line, calls the converse unproved and false in general, reports four indexes as four indexes, and 'one instance of a general law' is gone; check.py L6 verifies no operator is marked NOT EXTENSIVE. |
| R-3 "binds" means non-constant | 74 | MINOR |  **FIXED.** D6 says 'binds when it is not the constant Mᵢ' and that a non-constant envelope need not exclude a cell. |
| R-4 S overloaded (superset, subset, spin) | 98, 143, 173 | MINOR |  **FIXED.** Y is the superset in Theorem 1; S the subset in Theorems 5–6; Notation says 2S, 2S′ are never sets. |
| R-5 bit cost is a description length under a stated code | 82 | MINOR |  **FIXED.** D10 says it is the length of a uniform code over the E-subsets, not an entropy, and not additive over fibres. |
| R-6 crossing population is two-thirds Pauli-forbidden; on physical one-electron moves there is no crossing | 3, 11, 27, 433–451 | BLOCKING |  **FIXED.** check.py Q8a adds the Pauli filter as an obligation (2,923 moves without room for the g delivered, 2,203 into a full subshell, 2,819 multi-electron, 134 physical) and Q9./Q9b/Q9c print the four percentages on the physical population beside the unfiltered ones (Q8./Q8b/Q8c): allowed 11.9% against forbidden 18.7% within, 40.7% against 64.0% across — no crossing (Q9c asserts the order does not reverse). §5.5, Table 3 and Figure 4 carry both populations; the crossing left the abstract and §0 (the title never carried it) and the paper claims none; SOURCES.md §1.2/§4.10 record that the source's figures reproduce on a population two-thirds Pauli-forbidden. |
| R-7 followability matches electrons delivered against electrons held | 80, 180, 435 | MAJOR |  **FIXED.** D9 says the match is formal — electrons delivered against electrons held, a coincidence of two integers with no physical reading — and §5.5 repeats it; a configurational match (target at k + g after the move) is computed (Q10, Q10., Q10b): zero within one element on both populations by construction, 5.1% against 26.7% across on the physical one, no crossing; the §3.1 composability paragraph and the §5.4 mutual-information paragraph are dropped (C14, Q7 rows remain in check.py, unprinted). |
| R-8 Δℓ = 0 cells labelled M1 | 351, 410–413 | MAJOR |  **FIXED.** M1 is gone; the classes are 'Δℓ = 0 (parity conserved)' and '|Δℓ| = 1 (E1)', with the sentence that a jump between different subshells with the same ℓ is not a magnetic-dipole transition. |
| R-9 diproton as "failure of the pairing term" is backwards | 216 | MAJOR |  **FIXED.** Rewritten: the diproton is unbound because the singlet nucleon–nucleon channel is too weak to bind (the deuteron binds only in the triplet) and the Coulomb repulsion adds to it — a failure of any smooth mass formula at A = 2, not of one term. |
| R-10 particle-bound list needs NUBASE2020 and is incomplete (with A-10) | 204–214 | MAJOR |  **FIXED.** As A-10: NUBASE2020 cited with the file's provenance, the list derived, the seven omissions recorded (C7f), E = 12 at Z ≤ 10 printed with F-16, F-28, F-30 named. |
| R-11 h¹¹, h²¹ read as powers | 220, 257 | MINOR |  **FIXED.** h(1,1) and h(2,1) in text and table, introduced as the Hodge numbers usually written with superscripts. |
| R-12 the χ = ±6 slice is not an index of anything; the 540 are cells of a region known to be dense | 29, 220–226 | MAJOR |  **FIXED.** 'Predictions' and the 'four consistency tests' are gone; §3.5 states the defect is forced by the slicing (Corollary 1 with the printed pair), mentions that the region is one the published plot shows as dense and draws nothing from it, and names the three-generation reason for χ = ±6. The full Hodge-pair list is not closed here: it was not read, and the paper says so (this half of the resolving change is not taken). |
| R-13 §3.6 reduces to Theorem 2; d(N) irrelevant | 228–232 | MINOR |  **FIXED.** As A-26. |
| R-14 the quotient's content is the independence of Δℓ and ΔS; ∣ΔS∣ unmotivated | 408–415 | MINOR |  **FIXED.** §5.4 says the full rectangle means Δℓ and ΔS are independent on Λ₉, every combination occurring, and gives the reason |ΔS| is taken (the rules are stated on magnitudes; the sign is carried by ΔS in §5.2). |
| R-15 Laporte's rule is parity, not Δℓ = ±1 | 343 | MINOR |  **FIXED.** §5 attributes Laporte 1924 to the parity rule and Δℓ = ±1 to the rank of the dipole operator (Condon and Shortley 1935, ch. IV; Cowan 1981). |
| R-16 ground configurations spot-checked; say NIST's assignments are used as tabulated | 433 | MINOR |  **FIXED.** §5.5 says the configurations are as NIST tabulates them, including its assignments for the ambiguous heavy elements. |
| R-17 survey's witnessed set is the object of interest, E = 975 | 236 | MINOR |  **FIXED.** The witnessed channels are a row: 285 / 1,960 / 975 (C15b), §3.7, Table 1, Figure 2. |
| R-18 the catalogue: seven informative rows of fourteen; thesis restated over them | 3, 25, 242–257 | MAJOR |  **FIXED.** Table 1 is grouped (closed by theorem, Proposition 2; full box, Theorem 2; open with cells named; open by construction) and the thesis is restated: every zero is a theorem about the rule's shape, every non-zero is forced or named, and 'the catalogue separates' is withdrawn in §0 item 3 and 'what is not claimed'. Going further than the audit asked: Lemma 3 shows the box ordering, Λ and the grid close by theorem too, so no zero in the catalogue is a measurement. |
| R-19 three reconstructions chosen to reproduce printed numbers, presented as definitions | 76, 80, 298 | MAJOR |  **FIXED.** D7 calls the protocol a convention chosen once and states why; §4.2 calls the 724-cell down-set a convention of the same standing; D9 calls the followability match formal. |
| R-20 hierarchy-law citation: misattribution for the identity, no locator | 114, 487, 556 | MAJOR |  **FIXED.** Queyranne–Tardella 2008 (and 2006 for the bimonotone class), Topkis 1976, Veinott 1989, Baker–Pixley 1975 cited for the identity; the hierarchy-law manuscript cited in §6 only, as 'Manuscript', for the containment law and for nothing in the proofs. |
| R-21 r² and p on six ladder-quantised points | 300–304 | MAJOR |  **FIXED.** r² and p are deleted from §4.2 and Figure 3; the rows carry the point in two sentences (check.py R2 still computes them, unprinted). |
| R-22 missing standard references (list given) | References | MAJOR |  **FIXED.** All added with the details given, verified against the sibling papers' checked entries where they overlap (Queyranne–Tardella 2008 title corrected to 'Sublattices of product spaces: hulls, representations and counting'): Queyranne–Tardella 2006 and 2008, Topkis, Veinott, Baker–Pixley, Montanari, Mackworth, Freuder 1978, Deville–Barette–Van Hentenryck, Caspard–Monjardet, Beeri–Fagin–Maier–Yannakakis, Ireland–Kullback, Haberman, Kondev et al. 2021, Huang et al. 2021, von Weizsäcker, Madelung, Löwdin, Allen–Knight, Cowan, Birkhoff 1937. |
| R-23 abstract length and number load | 11 | MINOR |  **FIXED.** The abstract is about 380 words and carries the headline numbers only; §0 carries the rest. |
| R-24 "102 obligations" counts printed rows | 493 | MINOR |  **FIXED.** §7 says 'one row per obligation' and reports the program's own summary counts as rows by status. |
| R-25 abstract's "string compactification, atomic spectroscopy" against what is delivered | 11, 25 | MINOR |  **FIXED.** The abstract names no field it does not deliver; §0 item 3 says the catalogue does not separate by measurement and what decides each row. |

**Totals.** BLOCKING 2 (A-1, R-6). MAJOR 29 (A-2 to A-10, A-20, A-29, A-40, A-41; R-1, R-2, R-7 to
R-10, R-12, R-18 to R-22). MINOR 101 (A-11 to A-19, A-21 to A-28, A-30 to A-39, A-42, A-43.1–45,
A-44.1–7; R-3 to R-5, R-11, R-13 to R-17, R-23 to R-25). 132 findings in all.


---

## Repair record — 2026-09-24

Repaired by the drafter against every finding above; nothing above was deleted or rewritten.
**Dispositions: 118 FIXED, 1 DECLINED** (BLOCKING 2/2 FIXED; MAJOR 29/29 FIXED; MINOR 99 FIXED, 1 DECLINED — A-42).
The half of R-12 that asked for the full Hodge-pair list to be closed is declined inside R-12's FIXED note: the list
was not read here and the paper says so.

**A-1.** The general-partition counterexample was verified with the seated operator (E(X) = 1, fibred defect 2) and is
printed as Remark 3 / check row T4b. Fibrations are by a coordinate (D5); Theorem 4 holds for any coordinate and is
machine-checked fibred over every coordinate of the three boxes (8 instances); Corollary 2 iterates (T4c).

**R-6.** The Pauli filter is check row Q8a: 2,923 of the 4,325 moves deliver more electrons than the target can still
hold (2,203 into a full subshell), 2,819 move more than one electron; 134 are physical. The source's four percentages
reproduce on the unfiltered population (Q8b) and do not cross on the physical one (Q9b: 11.9 / 18.7 within, 40.7 / 64.0
across; Q9c asserts no reversal). A configurational match is computed beside it (Q10). The paper prints both populations
(Table 3, Figure 4) and claims no crossing; SOURCES.md §1.2 / §4.10 record the source's figures as reproduced on a
population two-thirds Pauli-forbidden.

**What changed.** `PAPER.md` rewritten in full: new title ("…the defect of an index, its zeros by theorem, and the
electromagnetic quotient"), abstract halved, thesis restated (every zero of the catalogue is a theorem — Theorem 0 with
Lemma 3's bimonotone cut, Proposition 2 — and every non-zero forced or named); Theorem 0 (Queyranne–Tardella) with the
six-line proof; Remark 1–3; Lemma 3 / Corollary 4 / Proposition 2; Lemma 4; the survey's witnessed channels as a row;
the nuclide list derived from NUBASE2020 (`nubase2020-Z0-10.txt`, verbatim, md5-checked; the full file fetched from two
independent public copies, byte-identical); MEASURED adopted as a status word; every code span gone; ∣ in table cells;
(a)/(b)/(c) inline. `check.py` never weakened: 46 new rows (T0c.×3, T0c, T0d, T4 over every coordinate, T4b, T4c,
T6ag/T6bg, T7a–e, C7 CITED, C7a–g, C8c, C9d, C15b, L3c, L6, L7, R3.×6, R3c, Q8a, Q9.×5, Q9b, Q9c, Q10, Q10.×5, Q10b),
21 rows relabelled MEASURED, the unused T = 5 branch removed, labels corrected (A-34). `figures.py`: Figure 1 computed
from C2/C2b (replacing the plate), Figure 2 sixteen grouped rows, Figure 3 without r², Figure 4 both populations.
`FIGURES.tsv` rewritten with the four new md5s. `SOURCES.md` rewritten (§1.1–1.9 corrections, §4.10–4.11).

**Re-verification.** `python3 check.py` (PATH = `method/bin`, Python 3.12, detached): **148 obligations, 0 failed** —
MACHINE-CHECKED 8, EXHAUSTIVE 74, MEASURED 35, SAMPLED 16, REFUTATION 3, CITED 1, GUARD 11, `CLEAN`.
`python3 check.py --selftest`: **152 obligations, 0 failed**, N1–N4 each refuted (N3: 18 of 1,112 cells disagree),
`CLEAN`. `lint.py`: 0 hits. `render.py`: **25 pages**. pypdf text extraction of the PDF: 0 underscores, 0 carets,
0 backslashes, 0 asterisks, 0 backticks. The HTML screenshotted with headless Chromium per BRIEF-AUDIT step 6 and every
PDF page rasterised (PyMuPDF, 1.3×) and read: Unicode subscripts throughout, every table inside its column, every
figure with its caption; the three figure legends that overlapped bars on the first re-render were moved outside the
plotting area and the figures regenerated (md5s in `FIGURES.tsv` are those of the final run).
