# SOURCES.md — provenance map for 06-order-recovery (not published)

Paper: `PAPER.md`, "Order Recovery and the Reorderability Law". Drafted 2026-09-21 on a `check.py`
left by an earlier run; that run was cut off by a service limit while `check.py` was mid-flight, and
the paper was finished 2026-09-24 by a resumed run (see "The resumed run" below). Every number in
the paper is produced by `check.py` — **90 obligations: 52 EXHAUSTIVE, 29 MACHINE-CHECKED,
6 REFUTATION, 3 SAMPLED, all discharged, exit 0, 232.6 s; `--selftest` adds four negative controls,
all refuted** — or is CITED.

## Where each section draws from

All volume paths are under `/home/user/Claude-Method-Works/method/members/`.
`MAIN` = `The_Method_1_6-2.md`; `MATH` = `The_Method_1_6___Mathematical_Compendium-2.md`.

| paper section | source passages |
|---|---|
| Thesis, §0 | MAIN §30 8321–8614 ("Order recovery, and the reorderability law": the law, the procedure, the residue); MAIN §15.3–15.5 4295–4337 (S2, "the necessary condition is provable and dimension-free"; "at d = 2 the converse also holds"; "Λ contains its own order") |
| §1 D1–D4 (index, ordering, closure, ℛ, E) | MATH §IV.A 144–175 ("Closure defect E(X) = \|ℛ(X)\| − \|X\|", "The recovery operator", "Projection onto coordinate i", Moore 1910, Deville–Barette–Van Hentenryck 1999); MATH §IV.A "Closure operator (Moore family)", "Extensivity", "Monotone upper envelope / staircase bound", "The one-corner characterisation"; MAIN §15.2 4279–4292 (S3, "the envelope set determines the index completely", "for Λ₈ that is 56 functions") |
| §1 D5–D7 (fibre, may precede, recovered order) | MAIN §15.3 4295–4306 (the definition of "may precede" and the necessity lemma, given there in full) |
| §1 D8 (constraint graph, tree-structured) | MAIN §7.2 1769–1780 (every constraint is `xᵢ ≤ φ(xⱼ)`; the graph is a tree); MATH §IV.G 890–900 ("The constraint index": 8 nodes, 7 edges, zero of 35 triples); MATH §IV.A 376–384 (Freuder 1982) |
| §1 D9–D11 (orientation variables, bijunctive, growth step) | MAIN §30.3.2 8404–8428 (the constraint system on orientations, complement invariance, the arity table, THE LAW); MAIN §30.3.4 8480–8496 (the step law and the three-quarters figure) |
| §2.1 Theorem 1 | MAIN §30.3.1 8396–8402 ("ℛ-closure and closure under join and meet are the SAME CONDITION"); MATH §IV.A "Bergman double-projection; Baker–Pixley 1975 (majority term)" and "Global consistency (CSP)"; MAIN §7.3 1781–1793 (Λ is closed, with the monotonicity proof) |
| §2.1 Corollary 1 | MAIN §16.5 4460–4476 (D3 — totality: "χ_Λ is total … a finite conjunction of decidable comparisons", with the proof); MAIN §15.2 (S3) |
| §2.2–2.3 Lemmas 1–4, Theorem 2 | MAIN §15.3 4295–4306; MAIN Appendix A "The total-order criterion at d = 2" 9995–10007 (both directions, written out) |
| §3.1 Theorem 3, §3.2 Lemma 5 | MAIN §30.3.3 8445–8468 (the d = 2 characterisation; the fourth lemma with its proof; 2,354 interval sets; "strictly is load-bearing" and the 1,098) |
| §3.3 DECIDE₂ | MAIN §30.3.2 8428–8432 ("at d = 2 every constraint has arity 2 … 2-colouring plus transitivity decides exactly"); the algorithm verified here is root enumeration plus Theorem 2, not the 2-colouring |
| §4.1 | MAIN §15.3 4306–4310 ("above d = 2 the converse fails … the axes' requirements can be mutually incompatible"); MAIN §30.3.7 8535–8545 (projection-based criteria ruled out; "closure is a d-dimensional condition"); MAIN Appendix A.3 remark ("the converse fails, and §18.4 exhibits a counterexample" — §18.4 is outside the passages named for this paper and was not drawn on). The three-unit-vector witness, its proof, and the census over 193 / 3,271 / 63,775 subsets are the paper's own |
| §4.2–4.3 Theorems 4–5 | MAIN §15.4 4311–4326 (propagation along the tree; "root anywhere, fix the root by brute force, and extend with backtracking"; "cost Σ\|Aᵢ\|!, never the product"); MATH §IV.A 376–384 (Freuder 1982), §IV.G 890–900 |
| §4.4 Theorem 6, the diagnostic loop | MAIN §16.7.1 4610–4640 (E removable or not; the periodic table against Janet; the asteroid-belt counter-case); MATH §IV.A "Failure mode A — ordering" and "Failure mode B — arity" (Freuder 1978); MATH §IV.A "The certificate condition" (the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate) |
| §5 Λ | MAIN §7 1729–1810 (the eight coordinates, the seven bounds and their four origins, the caps convention (3,3,1,3,1)); MAIN §8.3 via Appendix A "The seventeen generators, written out" 10122–10160 (17 join-irreducibles, `Σ(\|Aᵢ\|−1) = 17`, the closed form of a generator); MAIN §16.8.6 4784–4794 (16 binding pairs, transitive reduction returns the seven edges); MAIN §15.4 4318–4322 (20 of 20 at two cap settings) |
| §6 the law | MAIN §30.3.2, §30.3.4, §30.3.5, §30.3.8 8404–8560 |
| §7.1 | MAIN §16.5 4460–4485 |
| (none) | MAIN §19 5386–5554 ("Retrieval as a lattice problem") was named among this paper's sources and was read in full. It is not drawn on. Its subject is retrieval redundancy ρ — a count of routes to a document — and its one lattice claim, that a six-cell retrieval index fibred by route closes with E = 0 (§19.5.3), names neither the cells nor the coordinates' values, so nothing in it can be recomputed. Its self-refutation (§19.5.1: "ρ is a property of the query, not of the literature") is about search, not about closure, and the paper makes no claim about it |
| §7.2 Lemma 8 | MAIN §16.1 4348–4360 (ⅅ = dim q − rank ∂Φ/∂p ≥ dim q − dim p, with the one-line proof); MAIN §16.4.1 4426–4436 (the 1960 precedent, quoted from Edlén's Handbuch footnote) |
| §7.3 | MAIN §16.8.4 4666–4700 (A(y), the amplification, "minimum 59 across 220 trials"; the figure's "median 352, minimum 15"); MAIN §16.8.2 4655–4662 (replacement is not a question put to an index) |
| §7.4 Lemma 9 | MAIN §16.8.5 4702–4724 (pushback; the removal lemma with its proof; step(Λ₈) = 4 and the named interval); MAIN §30.3.4 8489–8496 (Rival's bound) |

## The honesty rule the brief names, applied

Where a source states a result as proved and checks it only by sampling, the paper states PROVED for
the proof and states the sample separately, or omits the sample. Four places:

1. **Totality of χ.** MAIN §16.5 proves it and records that "an earlier pass drew 30,000 uniform
   samples from a box of 6,912", superseded there by an exhaustive test. The paper prints the proof
   (Corollary 1, PROVED) and the exhaustive figure (6,912 of 6,912). The 30,000 is not printed.
2. **The d = 2 criterion.** MAIN §15.3 and Appendix A both add "Verified on 120 sets; 274 of 274
   constructed total orders give closed sets". The paper proves the criterion (Theorem 2, both
   directions) and machine-checks it over *every* subset of four boxes and every total order on the
   named coordinate. The 120 and the 274 are not printed.
3. **The counting bound.** MAIN §16.1 proves `ⅅ ≥ dim q − dim p` in one line and adds "verified on
   seven dimension pairs and 420 random nonlinear maps". The paper prints the proof (Lemma 8) and its
   own sample — 60 maps, seed 3, exact rational rank — marked SAMPLED with size and seed, and says
   the sample corroborates the implementation and not the lemma. The 420 was not reproduced.
4. **Λ's recovery.** MAIN §15.4 states "20 of 20, at two cap settings". The paper prints that as
   SAMPLED with the seed, and adds the exhaustive measurement that qualifies it: Λ is closed under
   exactly **16** ordering systems, so "recovered" means "returned an admissible ordering", and the
   built ordering or its reverse came back in only 3 of 20 and 0 of 20. The source does not state the
   16; it is measured here, and without it "20 of 20" would read as a stronger claim than it is.

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
- The eighteen-column periodic layout: 90 cells, `E = 36`. The left-step arrangement: `E = 0`.
- The nesting lemma over all 2,354 interval families, and the 1,098 refutations of the weak reading.
- The growth step `2^(d−2)`: 1, 2, 4.
- The largest reorderable proper subset of the Boolean box: 3, 6, 12, 24 — three quarters.
- `Σ|A_i|! = 94` against `∏|A_i|! = 11,943,936`.
- Λ recovered from a scrambled bag, 20 of 20 at each of the two cap settings.
- Every pair constraint complement-closed: 1,967,872 of them here (the source checked 3,781).
- Every constraint of arity ≤ 3 bijunctive; not every constraint of arity 4.
- The minimum of `A(y)`: **15**, which is the figure the source's own plate prints.

Proved here where the source measured:

- `E(X) = 0 ⟺ X` a sublattice. MAIN §30.3.1 states it as a measurement — "1,487 instances, zero
  disagreements, and confirmed on all 475,800 pairs of Λ". Theorem 1 proves it for every `d` and
  every alphabet, and `check.py` verifies it on every subset of five boxes, 70,598 in all.
- Transitivity of "may precede". The source states the necessity lemma and the `d = 2` criterion but
  never states that ⊑ is transitive unconditionally. Lemma 3 proves it (two applications of
  absorption), and it is what makes the criterion of Theorem 2(c) a criterion.
- The three-quarters bound. MAIN §30.3.4 verifies it "by construction at `d = 2, 3, 4 and 5". Theorem 9
  proves it for every `d ≥ 2` — from Theorem 1's Baker–Pixley step — and Z3 confirms it to `d = 6`.
- The factorisation over a tree, and the completeness of the propagation. MAIN §15.4 describes the
  algorithm and reports its success rate; Theorems 4 and 5 prove that it returns *every* solution,
  and `check.py` compares the solution **sets** — not merely the yes/no — against brute force on
  7,486 tree-structured subsets.

## Reproduction — what does NOT reproduce, and what the paper did about it

**1. The arity census of the source's plate for figure 30.1 (2/2, 14/14, 114/141, 121/129).** Not
reproducible under the parametrisation the paper states, and the source's parametrisation could not
be recovered. Under D9 and Lemma 7 — a constraint on the `k` orientation variables of a pair, closed
under global complement, hence a subset of `{0,1}^{k−1}`, and always containing the origin because
`x` and `y` are themselves cells — the counts are 2, 8, 128 and 32,768 at arities 2, 3, 4 and 5, with
2, 8, 73 and 1,442 bijunctive. The source's 14 at arity 3 equals `2^{2^2} − 2`, the number of
non-empty proper complement-closed subsets of `{0,1}^3` *without* requiring the origin; but the
all-ones assignment always lies in `C(x,y)`, so that cannot be the count of constraints that arise.
Worse, the source's 141 at arity 4 exceeds the 128 that the origin-containing parametrisation allows
at all, so the two censuses count different objects. **The paper prints its own figures and the plate
is not used**; Figure 4 is computed instead. The qualitative claim the plate carries — entirely
bijunctive at arity ≤ 3, not at arity 4, boundary exact — reproduces. **Marked for M: what the 141
counts.**

**2. `check.py`'s own arity witness was wrong and was corrected.** The block asserted that the
six-cell set `{0000, 1111, 1100, 0011, 1010, 0101}` realises the relation `{000, 110, 101}` at the
pair `(0000, 1111)`. It realises `{000, 011, 101}` — the same relation with two difference variables
exchanged — and the run FAILED on that line. This is a bug in the check, not a claim of the source
that fails to reproduce: the source claims only that the language "contains exactly-one-of-three",
and the realised relation is exactly-one-of-three up to an exclusive-or translation and a
coordinatewise complement, which `check.py` now verifies rather than asserts. The fix reads the
relation off the witness and checks (a) that it has three elements, (b) that its majority is not in
it, and (c) that translating by `110` gives exactly-two-of-three. Nothing else was changed to make
the line pass.

**3. `check.py` crashed before the first run finished, and the crash was a bug in the check.** In the
tree-propagation routine, partial solutions keyed by integer coordinate indices were merged with
`dict(p, **s)`, which requires string keys. Replaced by `{**p, **s}`. No obligation's content
changed. Section I has since run to completion (2026-09-24): on every tree-structured subset using
every value — 175 of 2×2×3 (path), 6,625 of 2×3×3 (path), 343 and 343 of 2×2×2×2 (path and star) —
the solution set the propagation returns equals the brute-force set, and every one of the 362,144
relabellings of a reorderable one is recovered. Λ: 20 of 20 at both cap settings, 16 admissible
ordering systems at both.

**4. "twelve boxes" for the growth step.** MAIN §30.3.4 reports the step measured "exhaustively
across twelve boxes — eight, all 2-D; three at `d = 3`; one at `d = 4`". The census here uses **ten**:
six 2-D, three 3-D, one 4-D. The two further 2-D boxes are not named in the source, and the step is 1
at every 2-D box tested, so nothing turns on the difference. The paper says ten and names all ten.

**5. "The language is NP-complete" (MAIN §30.3.8).** Not printed. The same passage records that the
realisability is blocked — "three reduction attempts, all over-constraining in the same direction" —
and a constraint language lying outside Schaefer's classes is not a hardness result for the decision
problem unless arbitrary instances of that language can be realised as pairs of cells of an index.
No such reduction exists here. §6.5 of the paper states the gap in three numbered points and calls the
complexity open. **This is the one place where the paper declines a headline the source states.**

**6. "18,736 = 18,736" at the box 2×3×3 (MAIN §30.3.5).** Not reconciled. The census here gives
**20,068** reorderable subsets of the 262,144, and **13,051** reorderable among the 34,588 subsets
that use every value of every alphabet. Neither is 18,736, and the source does not define which set
its growth procedure enumerates. Not printed. **Marked for M.**

**7. `A(y)`'s median and minimum (MAIN §16.8.4 and its plate).** The prose says "a median of 340 more
— minimum 59 across 220 trials"; the plate says "over 140 random insertions … median 352, minimum
15". The exhaustive census over **all 5,936** ambient non-cells gives minimum **15**, median **309**,
mean 380.9, maximum 1,795, none zero. So: the plate's minimum of 15 is the true minimum and the
prose's 59 is a sample minimum above it; 340 and 352 are sample medians and the population median is
309. The paper prints 15, 309, 380.9, 1,795 and marks them EXHAUSTIVE; the plate is not used, because
its printed median disagrees with the population median. Figure 5 is computed instead.

**8. "The same 118 elements" (MAIN §16.7.1).** The two coordinatisations do not have the same cells:
the eighteen-column layout has **90** occupied cells in a box of 126, and the left-step arrangement
has **22** in a box of 40. The claim is about the subject, not a bijection of cells, and the paper
says so explicitly in §4.4 and uses the pair as an instance of the diagnostic loop rather than as a
re-labelling.

**9. Not reproduced and not printed, because no instrument or instance family was located.**
MAIN §30.1's "384 of 384 reorderable instances complete under a targeted attack" and the
backtrack-count table; §30.2 and its successor's correlation tables (0.31, 0.438, 0.375, 0.606,
−0.628); §30.2.2's log–log slope of 2.29 on five points; §30.3.6's signature census (30, 210, 4,168
classes); §30.3.7's three ruled-out method classes with their measurements (17 criteria, 1.66–2.19
components, 89.8 %, 96.7 %); §15.4's two failed earlier methods (0 of 12; 42 % and 25 %); §16.8.6's
two-closure-operator table; §16.8.4's regression `A ≈ fibre × (0.972 − 0.154·descendants)`. The paper
makes no claim about any of them. They are measurements of search behaviour on instance families the
source does not specify, and a paper that printed them would be printing numbers it cannot recompute.

**10a. "Linear" at arity ≤ 3, and the source's "at d = 3".** MAIN §30.3.2 states that at arity 2 the
decision is "signed-graph 2-colouring — LINEAR", at arity 3 "2-SAT … LINEAR", and reports
"2-colouring plus transitivity decides exactly — 300/300 at |A| = 3, 300/300 at |A| = 4. At d = 3 with
binary axes, 396 of 396". None of this is printed. Bijunctivity of the *pair constraints* is proved and
enumerated (Theorem 8), but the orientation variables must also satisfy transitivity on each
coordinate, which is a three-literal clause, so bijunctivity of the pairs does not by itself make the
decision a two-satisfiability instance — the paper says so at §6.5 point 2 — and the source does not
specify how its 2-colouring handles transitivity, so the 300/300 and 396/396 sweeps could not be
reproduced. The paper's `d = 2` decision is DECIDE₂ (root enumeration plus Theorem 2), which is proved
correct and checked exhaustively; the `d = 2` *cost* the source claims is not asserted. The source also
places the boundary "at d = 3"; the paper says the first non-bijunctive constraint is possible at
`d = 4` and not before — the same fact, stated as the first dimension where it appears rather than the
last where it cannot. **Recorded as an interpretation, not a discrepancy.**

**10. Λ's 16 admissible ordering systems is new here.** The source does not state it. It was measured
by running the propagation with every solution returned rather than the first, at both cap settings,
and it is what makes "20 of 20" a precise claim rather than an ambiguous one. It rests on Theorem 5
(the propagation returns every solution), which is proved and exhaustively checked on the small
families, and on Λ being tree-structured, which is checked.

## The resumed run (2026-09-24)

- The first run's log ended in the `dict(p, **s)` traceback (item 3 above). The fix was already in
  `check.py`; `python3 check.py` was run to completion (232.6 s, exit 0) and then `--selftest`.
- `check.py` section H2 — "every pair projection reorderable does not make X reorderable", three
  EXHAUSTIVE lines — had been added to the check after the paper's §4.1 and §8 were written: the paper
  said "87 obligations: 49 EXHAUSTIVE" and stated the projection gap without its measurement. §4.1 now
  carries the three-cell witness with a written proof, the census (193 / 3,271 / 63,775 subsets; 98 /
  2,460 / 61,462 not reorderable; smallest witnesses printed by the check), and the honest qualifier
  that in those three boxes the pair criterion excludes nothing at all, since every subset of a 2×2 or
  a 2×3 box is reorderable (Table 2). §8 carries the row and the totals read 90 / 52.
- `check.py`'s section and obligation labels were renumbered to the paper's numbering — "Theorem 1"
  became "Theorem 2" for the one-axis criterion, "Theorem 2" became "Theorem 3" for the fibre
  characterisation, "Lemma 4" became "Lemma 5", "Theorem 3" became "Theorem 5", "Lemma 5" became
  "Lemma 9", "Lemma 6" became "Lemma 8", and the obligations "1(a)…1(c)" became "2(a)…2(c)". Labels
  only; no encoding, family, box, seed or verdict changed. A `fraction_reorderable` field was added to
  each census row so that the four fractions Figure 4's caption prints (1.000, 0.723, 0.077, 0.050) are
  produced by `check.py` rather than by the figure script.
- §0 named "Theorem 6" for propagation and "Theorem 4" for the diagnostic; both were the body's
  numbering shifted by one and are now "Theorems 4 and 5" and "Theorem 6". §2.1 pointed at guard (c)
  for the cell-for-cell envelope check, which is guard (d). Figure 1's caption now says that the
  recovered ordering is the reverse of the built one.
- Eleven entries in References were never cited in the body. Booth–Lueker and Tucker are now cited at
  Lemma 5, Dechter (1992), Dechter–Pearl (1989) and Montanari (1974) at Theorem 4, van Beek–Dechter
  (1995) at D4, Davey–Priestley (2002) at D2, Scerri (2007) at the periodic-table instance; Dilworth
  (1950) had no use in the paper and was removed. The Edlén sentence cited "1960" against a 1964
  reference (the source quotes the chapter as "manuscript 1960"); the paper now cites Edlén (1964).
- Nothing in the figures changed in content; `figures.py` was re-run from the resumed run's
  `results.json` and `FIGURES.tsv` carries the md5 of each file as it now stands.

## Interpretations chosen

- **"Step" means two different things in the source and the paper separates them.** MAIN §30.3.4's
  step is the growth step of the reorderable family, `f(d) = 2^(d−2)`; MAIN §16.8.5's `step(Λ₈) = 4`
  is the size of the smallest removable interval. The paper calls the first the **growth step** (D11)
  and the second **the smallest removable interval** (§7.4), and never uses one word for both.
- **The alphabet convention.** The source works at explicit caps and does not state the convention
  `A_i = { x_i : x ∈ X }`. The paper states it as part of D1 and shows in §2.4 and §3.1 where it is
  load-bearing: Lemma 3 picks an element of a fibre, and the interval half of Theorem 3 needs the
  middle value to occur somewhere. An explicit counterexample is given in §3.1.
- **"May precede" as a preorder, not an order.** MAIN §15.3 and Appendix A say "the may-precede
  relation is a total order". It is not, in general: the full box makes every pair related both ways.
  What is true, and what the paper proves and machine-checks, is that it is a total *preorder*, that
  its linear extensions are exactly the admissible orders, and that the ties count the ambiguity
  (Lemma 4). The source's own phrase is recovered as the tie-free case. This is a correction to a
  statement of the source, and `check.py` carries it as a REFUTATION with a Z3 witness in each of four
  boxes.
- **The diagnostic loop.** The source states the two failure modes (ordering, arity) as a
  classification without a decision procedure. The paper derives them as Theorem 6, with a witness on
  each side — a pair projection that is not closed, or a triple whose median is missing — and proves
  that one of the two must be present whenever `E > 0`. The exhaustive check confirms "neither" never
  occurs, on 70,598 subsets.
- **What "reorderable" quantifies over.** The census counts *every* subset of the box, not only those
  using every value; a subset that does not use a value is reorderable exactly when it is reorderable
  as an index over its own alphabets, because permuting an unused value changes nothing. The
  algorithm comparisons in §3.3 and §4.3 are run over the subsets that use every value, which is
  where the criteria are stated, and the counts are given separately.
- **The example of Figure 1 returns the reverse ordering.** The recovery returned one of the four
  admissible ordering systems, and it happens to be the reverse of the one the example was built
  with. That is left as it is rather than re-seeded: it is the paper's point about reversal made
  visible, and the caption says the four are two ties times two reversals.

## Sources outside the volumes

Baker and Pixley (1975) is used in the proof of Theorem 1 Step 4 and of Theorem 9, and is named in the
source's own prior-art note in MATH §IV.A ("Bergman double-projection; Baker–Pixley 1975 (majority
term)"). Freuder (1978, 1982), Montanari (1974), Dechter (1992), Dechter and Pearl (1989), Deville
et al. (1999), van Beek and Dechter (1995), Moore (1910), Ward (1942), Schaefer (1978), Booth and
Lueker (1976), Tucker (1972), Rival (1973), Birkhoff (1967) and Janet (1929) are all named in the
source's prior-art notes at MATH §IV.A and §IV.G and MAIN §30.3. Jeavons, Cohen and Gyssens (1997),
Davey and Priestley (2002), Scerri (2007) and de Moura and Bjørner (2008) are added here. Every entry
in References is cited at least once in the body.

**Citation forms not independently verified** (no access to the literature through the proxy): the
volume and page numbers of Rival (1973) — the source names the bound and the year but not the
pagination, and the form printed is from memory; the pagination of Baker and Pixley (1975); Janet
(1929)'s imprint. **Marked for M** to confirm all three. Nothing in the paper's results depends on
them: Rival's bound is quoted only to say that the Boolean case proved here is tighter, and
Baker–Pixley's theorem is used in the form "an algebra with a majority term has every subalgebra of a
finite product determined by its binary projections", which is standard and is also in Bergman's
textbook treatment.
