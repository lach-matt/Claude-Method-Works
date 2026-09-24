# SOURCES.md — provenance map for 06-order-recovery (not published)

Paper: `PAPER.md`, "Order Recovery and the Reorderability Law". Drafted 2026-09-21 on a `check.py`
left by an earlier run; finished 2026-09-24 by a resumed run; audited 2026-09-24 (`AUDIT.md`, one
BLOCKING finding) and **repaired 2026-09-24** against every finding (see "The repair" below). Every
number in the paper is produced by `check.py` — **111 obligations: 72 EXHAUSTIVE, 28 MACHINE-CHECKED,
8 REFUTATION, 3 SAMPLED, all discharged, exit 0; `--selftest` adds five negative controls, all
refuted** — or is CITED.

## Where each section draws from

All volume paths are under `/home/user/Claude-Method-Works/method/members/`.
`MAIN` = `The_Method_1_6-2.md`; `MATH` = `The_Method_1_6___Mathematical_Compendium-2.md`.

| paper section | source passages |
|---|---|
| Thesis, §0 | MAIN §30 8321–8614 ("Order recovery, and the reorderability law": the law, the procedure, the residue); MAIN §15.3–15.5 4295–4337 (S2, "the necessary condition is provable and dimension-free"; "at d = 2 the converse also holds"; "Λ contains its own order") |
| §1 D1–D4 (index, ordering, closure, ℛ, E) | MATH §IV.A 144–175 ("Closure defect E(X) = \|ℛ(X)\| − \|X\|", "The recovery operator", "Projection onto coordinate i", Moore 1910, Deville–Barette–Van Hentenryck 1999); MATH §IV.A "Closure operator (Moore family)", "Extensivity", "Monotone upper envelope / staircase bound", "The one-corner characterisation"; MAIN §15.2 4279–4292 (S3, "the envelope set determines the index completely", "for Λ₈ that is 56 functions") |
| §1 D5–D7 (fibre, may precede, recovered order) | MAIN §15.3 4295–4306 (the definition of "may precede" and the necessity lemma, given there in full) |
| §1 D8 (constraint graph, G-/T-structured) | MAIN §7.2 1769–1780 (every constraint is `xᵢ ≤ φ(xⱼ)`; the graph is a tree); MATH §IV.G 890–900 ("The constraint index": 8 nodes, 7 edges, zero of 35 triples); MATH §IV.A 376–384 (Freuder 1982) |
| §1 D9–D11 (orientation variables, pair constraint, bijunctive, growth step) | MAIN §30.3.2 8404–8428 (the constraint system on orientations, complement invariance, the arity table, THE LAW); MAIN §30.3.4 8480–8496 (the step law and the three-quarters figure). "Pair constraint" and "partition constraint" are the paper's own terms |
| §2.1 Theorem 1 | MAIN §30.3.1 8396–8402 ("ℛ-closure and closure under join and meet are the SAME CONDITION"); MATH §IV.A "Bergman double-projection; Baker–Pixley 1975 (majority term)" and "Global consistency (CSP)"; MAIN §7.3 1781–1793 (Λ is closed, with the monotonicity proof) |
| §2.1 Corollary 1 | MAIN §16.5 4460–4476 (D3 — totality: "χ_Λ is total … a finite conjunction of decidable comparisons", with the proof); MAIN §15.2 (S3) |
| §2.2–2.3 Lemmas 1–4, Theorem 2 | MAIN §15.3 4295–4306; MAIN Appendix A "The total-order criterion at d = 2" 9995–10007 (both directions, written out) |
| §3.1 Theorem 3, §3.2 Lemma 5 | MAIN §30.3.3 8445–8468 (the d = 2 characterisation; the fourth lemma with its proof; 2,354 interval sets; "strictly is load-bearing" and the 1,098) |
| §3.3 DECIDE₂ | MAIN §30.3.2 8428–8432 ("at d = 2 every constraint has arity 2 … 2-colouring plus transitivity decides exactly"); the algorithm verified here is root enumeration plus Theorem 2, not the 2-colouring |
| §4.1 | MAIN §15.3 4306–4310 ("above d = 2 the converse fails … the axes' requirements can be mutually incompatible"); MAIN §30.3.7 8535–8545 (projection-based criteria ruled out; "closure is a d-dimensional condition"); MAIN Appendix A.3 remark ("the converse fails, and §18.4 exhibits a counterexample" — §18.4 is outside the passages named for this paper and was not drawn on). The three-unit-vector witness, its proof, and the census over 193 / 3,271 / 63,775 subsets are the paper's own |
| §4.2–4.3 Theorems 4–5 | MAIN §15.4 4311–4326 (propagation along the tree; "root anywhere, fix the root by brute force, and extend with backtracking"; "cost Σ\|Aᵢ\|!, never the product"); MATH §IV.A 376–384 (Freuder 1982), §IV.G 890–900. The memoised form and the cost proof are the paper's own; the source's Σ\|Aᵢ\|! is recovered as the bound on the number of evaluations |
| §4.4 Theorem 6, the diagnostic loop | MAIN §16.7.1 4610–4640 (E removable or not; the periodic table against Janet; the asteroid-belt counter-case); MATH §IV.A "Failure mode A — ordering" and "Failure mode B — arity" (Freuder 1978); MATH §IV.A "The certificate condition" (the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate) |
| §5 Λ | MAIN §7 1729–1810 (the eight coordinates, the seven bounds and their four origins, the caps convention (3,3,1,3,1)); MAIN §8.3 via Appendix A "The seventeen generators, written out" 10122–10160 (17 join-irreducibles, `Σ(\|Aᵢ\|−1) = 17`, the closed form of a generator); MAIN §16.8.6 4784–4794 (16 binding pairs, transitive reduction returns the seven edges); MAIN §15.4 4318–4322 (20 of 20 at two cap settings). The parity over-admission (413 cells) and the structure of the 16 admissible systems are measured here and are not in the source |
| §6 the law | MAIN §30.3.2, §30.3.4, §30.3.5, §30.3.8 8404–8560 |
| §7.1 | MAIN §16.5 4460–4485 |
| (none) | MAIN §19 5386–5554 ("Retrieval as a lattice problem") was named among this paper's sources and was read in full. It is not drawn on. Its subject is retrieval redundancy ρ — a count of routes to a document — and its one lattice claim, that a six-cell retrieval index fibred by route closes with E = 0 (§19.5.3), names neither the cells nor the coordinates' values, so nothing in it can be recomputed. Its self-refutation (§19.5.1: "ρ is a property of the query, not of the literature") is about search, not about closure, and the paper makes no claim about it |
| §7.2 Lemma 8 | MAIN §16.1 4348–4360 (ⅅ = dim q − rank ∂Φ/∂p ≥ dim q − dim p, with the one-line proof); MAIN §16.4.1 4426–4436 (the 1960 precedent, quoted from Edlén's Handbuch footnote — the Handbuch itself was not consulted, and the paper says the remark is quoted at second hand) |
| §7.3 | MAIN §16.8.4 4666–4700 (A(y), the amplification, "minimum 59 across 220 trials"; the figure's "median 352, minimum 15"); MAIN §16.8.2 4655–4662 (replacement is not a question put to an index) |
| §7.4 Lemma 9 | MAIN §16.8.5 4702–4724 (pushback; the removal lemma with its proof; step(Λ₈) = 4 and the named interval); MAIN §30.3.4 8489–8496 and 8502–8505 (Rival's bound, printed there as `\|K\| ≤ (3/2)\|L\|` — see "Rival" below) |

## The honesty rule the brief names, applied

Where a source states a result as proved and checks it only by sampling, the paper states PROVED for
the proof and states the sample separately, or omits the sample. Four places:

1. **Totality of χ.** MAIN §16.5 proves it and records that "an earlier pass drew 30,000 uniform
   samples from a box of 6,912", superseded there by an exhaustive test. The paper prints the proof
   (Corollary 1, PROVED) and the exhaustive figure (6,912 of 6,912, for both the seven bounds and
   the 56-comparison envelope conjunction). The 30,000 is not printed.
2. **The d = 2 criterion.** MAIN §15.3 and Appendix A both add "Verified on 120 sets; 274 of 274
   constructed total orders give closed sets". The paper proves the criterion (Theorem 2, both
   directions) and machine-checks it over *every* subset of four boxes that uses every value and
   every total order on the named coordinate. The 120 and the 274 are not printed.
3. **The counting bound.** MAIN §16.1 proves `ⅅ ≥ dim q − dim p` in one line and adds "verified on
   seven dimension pairs and 420 random nonlinear maps". The paper prints the proof (Lemma 8) and its
   own sample — 60 maps, seed 3, exact rational rank — marked SAMPLED with size and seed, and says
   the sample corroborates the implementation and not the lemma. The 420 was not reproduced.
4. **Λ's recovery.** MAIN §15.4 states "20 of 20, at two cap settings". The paper prints that as
   SAMPLED with the seed, and adds the exhaustive measurement that qualifies it: Λ is closed under
   exactly **16** ordering systems at each setting — and says which sixteen (ties × one reversal at
   976; one tie × three independent component reversals at 216, both verified against the DP's own
   list) — so "recovered" means "returned an admissible ordering", and the built ordering or its
   reverse came back in only 3 of 20 and 0 of 20. The source does not state the 16.

## Reproduction — what reproduces

Exactly, against the source's stated figures:

- Λ: 976 cells, box 6,912, `E = 0`; 216 cells at the smaller caps; the seven bounds rebuild both.
- Membership decided at all 6,912 ambient points and agreeing with the cell list at every one.
- 17 join-irreducibles above the bottom, `Σ(|A_i|−1) = 17`; 18 join-prime and 18 meet-prime cells
  with empty intersection; 16 binding coordinate pairs; the seven-edge tree, and Λ equal to the
  intersection of its seven edge cylinders.
- Pushback over all 475,800 pairs: minimum **16**, maximum **5,091**, mean **739.0**, none zero. The
  source's median is 504 and the computed median is **503.5** — the exact median of an even-length
  list, which the source rounded. Recorded, nothing turns on it.
- The smallest removable interval: 4 cells, `(2,1,3,3,2,1,3,0)` to `(3,1,3,3,3,1,3,0)`, leaving 972
  cells with zero failures over all 471,906 surviving pairs.
- The eighteen-column periodic layout: 90 cells in a box of 126, `E = 36`. The left-step arrangement:
  `E = 0` — on the 19 subshells occupied through Z = 118 and on the 20 with 8s (see "What does not
  reproduce", item 8, for the fixture's 22).
- The nesting lemma over all 2,354 interval families (and 5,084 multisets), and the 1,098 refutations
  of the weak reading.
- The growth step `2^(d−2)`: 1, 2, 4, attained at the full box in every one of the ten boxes.
- The largest reorderable proper subset of the Boolean box: 3, 6, 12, 24 — three quarters; and every
  maximal proper sublattice of 2^d, d ≤ 4, has exactly that size (2, 6, 12 of them).
- `Σ|A_i|! = 94` against `∏|A_i|! = 11,943,936` — the source's "cost Σ|Aᵢ|!, never the product",
  recovered here as the bound on the number of memoised evaluations (Theorem 5).
- Λ recovered from a scrambled bag, 20 of 20 at each of the two cap settings.
- Every pair constraint complement-closed: 1,967,872 of them here (the source checked 3,781).
- The minimum of `A(y)`: **15**, which is the figure the source's own plate prints; attained at 32
  ambient non-cells, the first `(2,1,3,2,2,1,3,0)`.

Proved here where the source measured:

- `E(X) = 0 ⟺ X` a sublattice. MAIN §30.3.1 states it as a measurement — "1,487 instances, zero
  disagreements, and confirmed on all 475,800 pairs of Λ". Theorem 1 proves it for every `d` and
  every alphabet, and `check.py` verifies it on every subset of five boxes, 70,598 in all.
- Transitivity of "may precede". The source states the necessity lemma and the `d = 2` criterion but
  never states that ⊑ is transitive unconditionally. Lemma 3 proves it (two applications of
  absorption), and it is what makes the criterion of Theorem 2(c) a criterion.
- The three-quarters bound. MAIN §30.3.4 verifies it "by construction at `d = 2, 3, 4 and 5". Theorem 9
  proves it for every `d ≥ 2` — from Theorem 1's Baker–Pixley step — and Z3 confirms it to `d = 6`;
  Corollary 2 identifies every maximal sublattice, from Rival 1973.
- The factorisation over a graph, and the completeness and cost of the propagation. MAIN §15.4
  describes the algorithm and reports its success rate; Theorems 4 and 5 prove that it returns
  *every* solution and bound its memoised cost, and `check.py` compares the solution **sets** — not
  merely the yes/no — against brute force on 7,486 tree-structured subsets.
- Every pair constraint arises (Theorem 7): stated in the source as a census; proved here by the
  construction X = C at the pair (0ᵏ, 1ᵏ), and the construction run for all 138 constraints at k ≤ 4.

## Reproduction — what does NOT reproduce, and what the paper did about it

**1. The arity census of the source's plate for figure 30.1 (2/2, 14/14, 114/141, 121/129), and
the law's boundary.** Not reproducible under any parametrisation tried, and the source's own
parametrisation could not be recovered. Under D9 — a constraint on the `k` orientation variables of
a pair, closed under global complement and containing both constant assignments — the counts are 2,
8, 128 and 32,768 at arities 2, 3, 4 and 5, with **2, 5, 15 and 52 bijunctive** (the Bell numbers;
Theorem 8). Counted on the difference relation `T` instead the bijunctive counts are 2, 8, 73 and
1,442. The source's 14 at arity 3 equals `2^{2^2} − 2`, the number of non-empty proper
complement-closed subsets of `{0,1}^3` *without* the origin requirement; **measured on that
parametrisation, 10 of the 14 are majority-closed, not 14 of 14** (`check.py` prints it, not as an
obligation) — so the plate's arity-3 claim fails on its own count as well as on the paper's. The 141
at arity 4 exceeds the 128 relations available and remains unexplained. **The paper prints its own
figures and the plate is not used**; Figure 4 is computed. The source's law says "entirely bijunctive
at arity ≤ 3 … boundary at arity 3, and since arity is bounded by d and reaches it, at d = 3"; that
sentence is true of `T` and false of the constraint `C` at arity 3 (5 of 8), and the paper's own
first draft carried the same conflation ("the first non-bijunctive constraint appears at d = 4"),
which the audit's finding A-1 caught. The repaired paper states the law on `C`, with the boundary at
d = 3 for the right reason. **Marked for M: what the 141 counts.**

**1a. The superseded statement, for the author.** The drafted paper's Theorem 8 read: "every
constraint arising at arity at most 3 is bijunctive and 55 of the 128 arising at arity 4 are not …
the first non-bijunctive constraint is possible at d = 4 and not before", counted on `T`. The
repaired Theorem 8 reads: a pair constraint is bijunctive iff it is a partition constraint, B(k) of
them, first non-bijunctive at d = 3. The title "Order Recovery and the Reorderability Law" is kept —
the paper still states one law, and a sharper one — and the audit's mathematician preferred this
resolution "because it is what the title promises". No retitle.

**2. `check.py`'s first arity-4 witness was wrong and was corrected (drafting run).** The block
asserted that the six-cell set `{0000, 1111, 1100, 0011, 1010, 0101}` realises the relation
`{000, 110, 101}` at the pair `(0000, 1111)`. It realises `{000, 011, 101}` — the same relation with
two difference variables exchanged — and the run FAILED on that line. A bug in the check, not a claim
of the source that fails to reproduce; the fix reads the relation off the witness. Nothing else was
changed to make the line pass. The repaired check reads both witnesses (arity 3 and arity 4) off the
sets.

**3. `check.py` crashed before the first run finished (drafting run).** `dict(p, **s)` with integer
keys in the tree-propagation routine; replaced by `{**p, **s}`. No obligation's content changed.

**4. "twelve boxes" for the growth step.** MAIN §30.3.4 reports the step measured "exhaustively
across twelve boxes — eight, all 2-D; three at `d = 3`; one at `d = 4`". The census here uses **ten**:
six 2-D, three 3-D, one 4-D. The two further 2-D boxes are not named in the source, and the step is 1
at every 2-D box tested, so nothing turns on the difference. The paper says ten and names all ten.

**5. "The language is NP-complete" (MAIN §30.3.8).** Not printed as a result about reorderability.
The source's own sentence — the language contains exactly-one-of-three and no Schaefer class covers
it — is about `T` at arity 4; the paper's §6.5 makes the correct statement about `C`: the pair
constraints alone are 0-valid and 1-valid (every one contains both constant assignments, so the
source's "no Schaefer class covers the language" is false of the pair constraints on their own —
audit A-2), and only with antisymmetry does the language {C₃, ≠} leave all six classes, at arity 3.
The realisability gap is stated in three points, and "open" is now situated against Green and Cohen
(2008) and Jeavons and Cooper (1995). **This is the one place where the paper declines a headline the
source states.**

**6. "18,736 = 18,736" at the box 2×3×3 (MAIN §30.3.5).** Not reconciled. The census here gives
**20,068** reorderable subsets of the 262,144, and **13,051** reorderable among the 34,588 subsets
that use every value of every alphabet. Neither is 18,736, and the source does not define which set
its growth procedure enumerates. Not printed. **Marked for M.**

**7. `A(y)`'s median and minimum (MAIN §16.8.4 and its plate).** The prose says "a median of 340 more
— minimum 59 across 220 trials"; the plate says "over 140 random insertions … median 352, minimum
15". The exhaustive census over **all 5,936** ambient non-cells gives minimum **15**, median **309**,
mean 380.9, maximum 1,795, none zero. The paper prints 15, 309, 380.9, 1,795 and marks them
EXHAUSTIVE; the plate is not used. Figure 5 is computed instead.

**8. "The same 118 elements" and the left-step count (MAIN §16.7.1).** The two coordinatisations do
not have the same cells: the eighteen-column layout has **90** occupied cells (elements) in a box of
126. The seated left-step fixture has **22** cells, but they are the hydrogenic rule under caps —
`(n+ℓ, ℓ)` for `1 ≤ n ≤ 7, ℓ ≤ min(n−1, 3)` — and include 6f, 7d and 7f, which no element through
Z = 118 occupies (audit A-9). The paper prints the **19** subshells occupied through oganesson (box
32, `E = 0`) and the **20** with 8s (`E = 0`), from two check lines built independently of the
fixture; the fixture's own line (22 cells, `E = 0`) stays in the check and is not printed.

**9. Not reproduced and not printed, because no instrument or instance family was located.**
MAIN §30.1's "384 of 384 reorderable instances complete under a targeted attack" and the
backtrack-count table; §30.2 and its successor's correlation tables (0.31, 0.438, 0.375, 0.606,
−0.628); §30.2.2's log–log slope of 2.29 on five points; §30.3.6's signature census (30, 210, 4,168
classes); §30.3.7's three ruled-out method classes with their measurements (17 criteria, 1.66–2.19
components, 89.8 %, 96.7 %); §15.4's two failed earlier methods (0 of 12; 42 % and 25 %); §16.8.6's
two-closure-operator table; §16.8.4's regression `A ≈ fibre × (0.972 − 0.154·descendants)`. The paper
makes no claim about any of them.

**10. "Linear" at arity ≤ 3 (MAIN §30.3.2).** The source states that at arity 2 the decision is
"signed-graph 2-colouring — LINEAR", at arity 3 "2-SAT … LINEAR", with "300/300 at |A| = 3, 300/300
at |A| = 4. At d = 3 with binary axes, 396 of 396". None of this is printed. At arity 3 the pair
constraints are not all bijunctive (5 of 8), so "2-SAT at arity 3" is not available on `C` at all;
even where they are, transitivity is a three-literal clause (§6.5 point 2). The paper's `d = 2`
decision is DECIDE₂, proved correct and checked exhaustively.

**11. Λ's 16 admissible ordering systems, and their structure, are new here.** Measured by running
the propagation with every solution returned; the structure (ties at 976; component reversals at
216) was proposed by the audit (A-21), generated independently in the check and compared with the
DP's list — equal at both settings.

## The repair (2026-09-24)

Against `AUDIT.md`: 1 BLOCKING, 12 MAJOR, 26 MINOR distinct findings, every one dispositioned there.
What changed in the record:

- **The law recounted on `C`** (A-1): the check enumerates every pair constraint at arity 2–5,
  decides bijunctivity by the two-clause closure at every arity and by majority-closure at arity ≤ 4
  (0 disagreements), verifies each bijunctive one is a partition constraint, counts the Bell numbers,
  checks `C` bijunctive ⇒ `T` bijunctive (0 failures), prints the arity-3 witness with its
  constraint read off, and keeps the `T` census with pins. Figure 4 regenerated (bars on `C`, hollow
  markers on `T`, the boundary between arity 2 and 3).
- **Guards** (A-12): non-vacuity on every Z3 box (14 lines); fidelity for every encoding — `s*`,
  Theorem 3's four, Lemma 9's three, the harness's `closed` — against references written fresh from
  the definitions. The `results.json` field `guards` carries every count.
- **Pins** (A-16): every number the check prints is now asserted by its line.
- **New obligations**: the envelope conjunction at all 6,912 points (A-14); the parity count and the
  singlet cell (R-16); the 19/20 left-step instances (A-9); the 5,084 multisets (R-9); the D1
  exhibit (A-6); the structure of the 16 (A-21); Theorem 7's construction (A-5); the maximal
  sublattices of 2², 2³, 2⁴ and the three-element chain (A-3); the Schaefer-class tests on the
  witness (A-2); the doubly-irreducible counts and box − largest = step (A-7); the argmin of A(y)
  (R-20). The step line was folded into the five Z3 lines (A-13): 28 MACHINE-CHECKED.
- **Figures**: `fig4-arity.png` and `fig1-example.png` regenerated (FIGURES.tsv carries the new
  md5s); `fig2`, `fig3` (copied plates) and `fig5` unchanged in content, `fig5` re-drawn from the
  same data.
- **Text**: every mathematics code span rewritten in Unicode (A-10); Figure 4's caption, Table 2's
  caption, §6.5 rewritten; Theorem 7 proved; Theorem 8 restated and proved; Corollary 2 added;
  Theorem 5 given its cost clause; RECOVER in a fenced block; Janet 1928; Green–Cohen and
  Jeavons–Cooper added.

## Interpretations chosen

- **"Step" means two different things in the source and the paper separates three.** MAIN §30.3.4's
  step is the growth step of the reorderable family, `f(d) = 2^(d−2)`; MAIN §16.8.5's `step(Λ₈) = 4`
  is the size of the smallest removable interval. The paper calls the first the **growth step**
  (D11), the second **the smallest removable interval** (§7.4), and — after audit A-23 — uses
  **drop** for the quantity Theorem 9 actually proves at the full Boolean box, which is a lower bound
  on the growth step there.
- **The alphabet convention.** The source works at explicit caps and does not state the convention
  `A_i = { x_i : x ∈ X }`. The paper states it as part of D1 and shows in §2.4 and §3.1 where it is
  load-bearing, with the four-cell declared-alphabet REFUTATION in §3.1 (the drafted paper's
  five-cell example did not exhibit it — audit A-6).
- **"May precede" as a preorder, not an order.** MAIN §15.3 and Appendix A say "the may-precede
  relation is a total order". It is not, in general: the full box makes every pair related both ways.
  What is true, and what the paper proves and machine-checks, is that it is a total *preorder*, that
  its linear extensions are exactly the admissible orders, and that the ties count the ambiguity
  (Lemma 4). The source's own phrase is recovered as the tie-free case. This is a correction to a
  statement of the source, and `check.py` carries it as a REFUTATION with a Z3 witness in each of four
  boxes.
- **The diagnostic loop.** The source states the two failure modes (ordering, arity) as a
  classification without a decision procedure. The paper derives them as Theorem 6, with a witness on
  each side, and proves that one of the two must be present whenever `E > 0`.
- **What "reorderable" quantifies over.** The census counts *every* subset of the box, ∅ and
  singletons included (each trivially closed), and Table 2's caption now says so; the step ranges over
  `|Y| ≥ 2` as D11 says. The algorithm comparisons in §3.3 and §4.3 run over the subsets that use
  every value, which is where the criteria are stated.
- **The example of Figure 1 returns the reverse ordering.** Left as it is: the paper's point about
  reversal made visible.
- **Rival's bound is quoted only in its verified role.** The paper cites Rival (1973) for the interval
  theorem (verified) and Corollary 2 rests on that; the cardinality bound is stated in the direction
  the audit gives, `|L| ≤ (3/2)|K|`, as a lower bound on a maximal sublattice, and is not used in any
  proof.
- **"Open" in §6.5 means open relative to Green–Cohen 2008.** Their NP-hardness is for max-closure
  alone of arbitrary constraint sets over a common domain; their Boolean tractability is for a common
  Boolean domain. Neither is reorderability, and the paper says why in both directions.

## Sources outside the volumes

Baker and Pixley (1975) is used in the proof of Theorem 1 Step 4 and of Theorem 9, and is named in the
source's own prior-art note in MATH §IV.A. Freuder (1978, 1982), Montanari (1974), Dechter (1992),
Dechter and Pearl (1989), Deville et al. (1999), van Beek and Dechter (1995), Moore (1910), Ward
(1942), Schaefer (1978), Booth and Lueker (1976), Tucker (1972), Rival (1973), Birkhoff (1967) and
Janet are all named in the source's prior-art notes at MATH §IV.A and §IV.G and MAIN §30.3. Jeavons,
Cohen and Gyssens (1997), Davey and Priestley (2002), Scerri (2007), de Moura and Bjørner (2008),
Green and Cohen (2008) and Jeavons and Cooper (1995) are added here. Every entry in References is
cited at least once in the body.

**Verified through the proxy (2026-09-24 repair).** Publisher sites (ScienceDirect, Springer,
Cambridge, AMS, Semantic Scholar, arXiv direct, CORE) are all egress-blocked; two arXiv papers were
readable through the alphaXiv connector and serve as restatements:

- **Rival (1973)**: Adaricheva, Mata, Silberger and Zamojska-Dzienio, *Conjecture on maximal
  sublattices of finite semidistributive lattices and beyond*, arXiv:2507.22682 (v2, 2026), §1 and
  §3, state Rival's Theorem 3 — "the complements of maximal sublattices of distributive lattices are
  always intervals [a, b] with a a unique join-irreducible element and b a unique meet-irreducible
  one" — and give the entry "I. Rival, Maximal Sublattices of Finite Distributive Lattices,
  Proc. Amer. Math. Soc. 37 (1973), 417–420". Title, volume and pages confirmed. **The cardinality
  bound's wording is not confirmed**: the source volume prints `|K| ≤ (3/2)|L|` (vacuous), the audit
  gives `|L| ≤ (3/2)|K|`, and the paper prints the audit's direction. **Marked for M** to confirm
  against the paper itself. Nothing in the paper's proofs depends on it.
- **Green and Cohen (2008)**: Takhanov, *On the induced problem for fixed-template CSPs*,
  arXiv:1708.08292 (v3), §1 ("Motivation") and §3.1, restate the problem (permutations of each
  variable's domain making the permuted relations max-closed), that "to find such permutations is
  computationally difficult in general", that the reduction "is always tractable for Boolean domains
  [13]", that the version with total orders "is NP-hard in general (see Proposition 38 from [13])",
  and the entry "Artificial Intelligence 172(8), 1094–1118 (2008)". The audit's further detail
  ("NP-complete for domain size three even for binary instances") could not be verified and is not
  printed.
- **Jeavons and Cooper (1995)**: bibliographic details (Artificial Intelligence 79(2), 327–339)
  confirmed from search listings; the max-closed tractability theorem is stated in the paper as
  Takhanov and the CSP literature restate it. The abstract itself was not reachable.
- **Janet**: the French imprint *La classification hélicoïdale des éléments chimiques* (Beauvais,
  Imprimerie Départementale de l'Oise) is 1928, per the audit (A-24); the paper cites 1928. Not
  independently verified through the proxy. **Marked for M.**

**Citation forms not independently verified**: the pagination of Baker and Pixley (1975). Nothing in
the paper's results depends on it.

## Figures

Figure 4's caption fractions are 1.000, **0.724** (47,416/65,536 = 0.72351), 0.077, 0.050, as
`check.py`'s `fraction_reorderable` prints them (audit A-28 — this file previously said 0.723).
