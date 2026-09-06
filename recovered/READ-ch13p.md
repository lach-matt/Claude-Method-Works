# READ-ch13p.md — Phase R2, chat 85 — main §16.6 through §16.8 (L4482–L4788, 307 lines)

Section read under the chat-81 cadence: the whole section read first, its claims censused into
two kinds, then exactly two instrument batches — `r2-ch13p` (computable, 9,543 B · md5 30e7afea ·
148 lines · 93 s) and `r2-ch13q` (prose, 16,442 B · md5 1e1479f4 · 225 lines · 1 s). Both banked.

**Boundaries, MEASURED by heading scan before reading:** §16.6 opens **L4482**; Chapter 17 opens
**L4789**. HANDOFF-37's figures are correct — the third handoff in a row was checked and this one
holds. Sixteen subsections: §16.6 (L4482), §16.6.1 (L4520), §16.6.2 (L4555), §16.7 (L4574),
§16.7.1–§16.7.4 (L4578, L4618, L4636, L4644), §16.8 (L4659), §16.8.1–§16.8.6 (L4663, L4669, L4683,
L4691, L4733, L4772).

## The claim census

**Computable (re-measurable on the tower) — 20 claims, all instrumented in r2-ch13p.**

| # | site | claim |
|---|---|---|
| K1 | L4665 | φ(2S \| k) = 1 at k = 1 |
| K2 | L4623–4627, L4670–4672 | Λ 976 → fabrication 1,051; closed; E = 0; fixed point |
| K3 | L4634, L4671 | the fabrication contains 75 impossible configurations |
| K4 | L4692–4693 | median 340, minimum 59 across 220 trials, zero exceptions |
| K5 | L4703 | "insert one — amplifies, always — minimum 59" |
| K6 | L4714–4715 | Figure 16.2: 140 insertions, median 352, minimum 15 |
| K7 | L4695 | A(y) = N[φ(Λ ∪ {y})] − N[φ(Λ)] − 1, exact on all cells tested |
| K8 | L4698 | deletions always repaired; C(Λ − x + y) = C(Λ + y) |
| K9 | L4710 | g ≤ 4f+2 the only constraint sharing its variable; an order of magnitude cheaper; 397 % jump |
| K10 | L4721–4722 | A ≈ fibre × (0.972 − 0.154·d); corr = −0.942; median error 7 %, worst 24 % |
| K11 | L4724–4729 | the descendants table, and the A/fibre bands |
| K12 | L4731 | leaves exact; the root off by a factor of 2.5 |
| K13 | L4737–4744 | 475,800 pairs; pushback min 16, median 504, mean 739, max 5,091; 0 removable |
| K14 | L4749–4751 | eighteen join-primes, eighteen meet-primes, intersection empty |
| K15 | L4755–4761 | X ∖ [a, b] is a sublattice iff a is join-prime and b is meet-prime |
| K16 | L4763–4766 | step(Λ₈) = 4; the interval; free in n and e; 972 cells; 471,906 pairs |
| K17 | L4773–4774 | ℛ recovers 16 binding pairs; transitive reduction returns the seven edges |
| K18 | L4778–4782 | A full vs A tree-only: 119/307, 269/563, 74/74 |
| K19 | L4537 | the reference index: 38 cells, box 144, density 26.4 %, E = 0, width 2, not a tree |
| K20 | L4543–4546 | 28 terms, 13 of 38 occupied, E = 11, the five-way breakdown, 68 % checked |

**Prose (pointers, restated figures, attributions, self-description) — 14 claims, all in r2-ch13q.**

| # | site | claim |
|---|---|---|
| P1 | L4482, L4488, L4500 | "there are six", against the two tables and the following sentence |
| P2 | L4502–4503 | twenty-one structural audits on a companion document carrying five |
| P3 | L4512–4514 | ⅅ_gro has no instance anywhere until now; q is the instance |
| P4 | L4115–4116 (cite) | §14.6.1: "§16.6 grades *multiverse dimension* ⅅ_gro" — the DEFERRED item |
| P5 | L4523 | the back-matter Index carries fifty-one terms, none saying what a term points at |
| P6 | L4525 | "constraints of §16.4 form" — 13o-01's eighth site |
| P7 | L4534 | §17.2's Theorem 17.1 forbids a repair coordinate |
| P8 | L4550–4551 | §19.5 says a blocked ρ = 1 cell is a stated gap |
| P9 | L4562–4569 | §29.1 proves ⅅ(novelty) = 0; verdict is the *first* coordinate below the floor |
| P10 | L4589–4593 | 36 / 106 / 0 for the three conventions, "the same 118 elements" |
| P11 | L4605–4612 | E irreducible; 0 of 6; 36 of 36; thirteen of thirteen above the cut |
| P12 | L4615 | §6.2's Janet table is that test |
| P13 | L4645, L4653 | §16.3's *five* recorded failures; a quantum defect of 4.9, a term value below zero |
| P14 | L4784–4787 | "the two that agree bound leaves"; "they agree on Λ and nowhere else" |
| P15 | L4621, L4665 | "one electron with spin multiplicity 2, which no atom has" |

Every §-pointer in range (21, per `r2-tools.py pointers`) was resolved to the **claim**, not the
heading. Thirteen of fourteen tested resolve; one does not (13p-06).

---

## A. Deviations

**13p-01 — the amplification floor of 59 is a class minimum printed as a global one, and the figure
on the same page contradicts it.** §16.8.4 L4692–4693 prints *"a median of 340 more — minimum 59
across 220 trials, zero exceptions"*, and the table at L4703 prints *"insert one — **amplifies,
always** — minimum 59"*. Figure 16.2's caption at L4714–4715, eleven lines later, prints
*"over 140 random insertions … median 352, minimum 15"*. MEASURED over the **population** — every
one of the 5,936 cells of the ambient box outside Λ₈, closure computed for each:

    A: minimum 15, median 309, mean 380.9, maximum 1,795, zero-cost insertions 0
    cells with A < 59: 86      cells with A < 15: 0
    quantiles: 5 % 89 · 25 % 191 · 50 % 309 · 75 % 497 · 95 % 898

The **15** is exact and is the true floor; the caption is right and the body is wrong. The **59** is
exactly the minimum over the *2S ≤ k* violators alone (measured: min 59 for that class), the class
of the worked fabrication — a class minimum carried into a sentence that quantifies over every
insertion. Neither printed median reproduces: 309 against 340 and against 352. What does hold is
*"zero exceptions"* and *"none is free"*: no insertion anywhere in the population has A = 0.
Seeded samples of the two printed sizes give min 15 / median 269 (n = 140) and min 15 / median 317
(n = 220), so the sample size does not explain the gap. **Two sites must move together** (L4693 and
L4703), and the figure caption must not.

**13p-02 — φ(2S | k) = 1 at k = 1 is false; the refusal it justifies is true.** §16.8.1 L4665:
*"Λ answers from its own content: φ(2S | k) = 1 at k = 1, the cell asks for 2, refused."* MEASURED
on Λ₈: at k = 1 the admissible 2S values are **{0, 1}**, so φ = **2** (at k = 2, φ = 3; at k = 3,
φ = 4). The cell asking 2S = 2 is refused, because 2 ∉ {0, 1} — the conclusion is sound and the
mechanism is real. Only the fibre size is wrong. The 13g-01 / 13h-04 / 13j-01 / 13l-01 / 13n-01
class: a claim true while the statement printed for it is not.

**13p-03 — §16.6's headline count is six; its own table lists seven, and its own next sentence
counts seven.** The heading at L4482 reads *"The defences are disjoint, and there are six."*
MEASURED: the first table (L4483–4486) carries **3** mechanism rows; the second (L4491–4498)
carries **7** — ℛ(Λ) = Λ, ⅅ ≥ 1, χ_Λ total, §28.8's index, ⅅ_ref, ⅅ_dict, ⅅ_gro. L4488 explains the
six as *"Three was the count … There are six, and the other three"* — 3 + 3, which omits §28.8's
index, a row the table prints as runnable. L4500 then reads *"Why the first four cannot reach the
last three"* — 4 + 3 = **7**. Three counts of one object in nineteen lines: 6, 7 and 7. L4572's
*"this work supplied an instance of each"* inherits whichever count governs. The 13j-11 class,
now in Chapter 16.

**13p-04 — "fifty-one terms" is stale by exactly the six terms Chapters 35–36 added.** §16.6.1
L4522–4523: *"its back-matter Index carries fifty-one terms."* MEASURED against the Index's own
statement of extent at main **L11419**: *"**Verified:** 57 terms, 311 entries, 44 specialisation
relations, 0 violations — E(index) = 0."* The same line gives the cause: *"Six terms and four
relations entered with Chapters 35–36."* 57 − 6 = 51. The figure was right before the Löwdin and
three-body material was absorbed and was not restated afterwards. **A second site carries it**:
main **L5192**, *"This book's own back-matter Index carries fifty-one author-chosen …"*. Both must
move; "57 terms" occurs at main L11419 and at ioi L1524.

**13p-05 — §14.6.1 attributes to §16.6 a grading §16.6 does not perform (the DEFERRED item, closed).**
Carried since chat 74 and re-listed by chats 83 and 84. §14.6.1 L4115–4116: *"§16.6 grades
*multiverse dimension* ⅅ_gro — a term with no referent established anywhere — and §29.2.2 records it
as not posable."* MEASURED: *multiverse* occurs **zero** times in §16.6 (L4482–L4519) and three
times in the whole main volume (L4116, L7347, L9303) — never inside Chapter 16. What §16.6 actually
grades with ⅅ_gro is ***q*, this book's transfer coordinate** (L4512–4514), and it says so in terms
that exclude a second instance: *"ⅅ_gro is the one with no instance anywhere until now."* If
*multiverse dimension* were also graded, that sentence is false; if it is not graded, L4115–4116 is.
The §29.2.2 half of the citation is sound — L7348's *"not posable"* is in that section. **Disposition
for R3:** either §16.6 gains the second instance and L4512 weakens, or L4115–4116 re-points to
§29.2.2 alone. Two sites, one of which must move.

**13p-06 — the Janet table is attributed to §6.2 and sits in §6.1.1.** §16.7.1 L4614–4616:
*"§6.2's Janet table is that test — run once, on one example, and never named as one."* MEASURED:
the table is at main **L1581–1585** and its reading at L1587, both inside **§6.1.1 "And a known
layout costs nothing"** (opens L1552); **§6.2 opens at L1594** and contains *"Janet"* zero times.
The 13d-01 / 13h-01 / 13l-03 / 13o-01 class — a table attributed to a neighbour that does not
contain it — and the pointer is off by one subsection, not by a chapter.

**13p-07 — "the same 118 elements" is one of three cell counts the book prints for those three
conventions.** §16.7.1 L4593: *"**The same 118 elements.** Order the blocks f, d, p, s and define
the period by *n* + ℓ, and the defect vanishes."* MEASURED at main L1581–1585, the book's own table
of the same three conventions: 18-column **90** cells, 32-column **118**, Janet left-step **120**.
The E column agrees exactly with §16.7.1's 36 / 106 / 0, so the defect figures are sound and only
the cell count is restated wrongly: 118 is the 32-column figure alone. The argument needs the three
conventions to index the same 118 elements, and the earlier table says they hold 90, 118 and 120
cells — which is a different claim about the *drawing*, not about the elements, but the two sites
now print incompatible numbers with no reconciliation at either.

**13p-08 — "the first coordinate anywhere in this book below the ⅅ ≥ 1 floor" is the third such
site, and one of the other two is cited two lines above it.** §16.6.2 L4568–4569. MEASURED: the
pattern ⅅ(x) = 0 occurs at main L4562, L4565 and **L7865**, and ⅅ = 0 at main **L1589**, L4442,
L4558, L7884 and L11622. L4562 — inside this very subsection — cites §29.1 as *already proving*
ⅅ(novelty) = 0 (L7865, *"necessarily and permanently. Not undefended: undefendable"*), and L4565
derives verdict's ⅅ = 0 **from** ⅅ(bibliography) = 0. A derived instance cannot be the first.
L1589 is earlier still: *"E(periodic table) = 36 has ⅅ = 0."* The substance — verdict is
undefendable and caps all twenty-eight terms — is untouched; only the primacy claim fails.

**13p-09 — §16.7.4 counts five recorded failures in a section that records one, and tabulates
three.** L4645: *"§16.3's five recorded failures are all of the second kind. Not one is a missing
cell."* MEASURED: §16.3 (L4359–L4378) and §16.3.1 (L4379–L4406) together record **one** worked case
— Al II and K II computed with Z_eff = 1 (L4360). §16.7.4's own table at L4647–4651 lists **three**
failure kinds (a wrong nuclear charge, a wrong ionisation limit, a mislabelled parent). Three counts
again: one, three, five. Related: L4653 names two catching quantities, *"a quantum defect of 4.9, a
term value below zero"*; the 4.9 is at §16.3 L4366 ✓, but *"term value below zero"* occurs at
**L4653 only** in the whole main volume — §16.3 records no such quantity.

**13p-10 — §16.8.6 states the two operators agree on Λ and nowhere else, and prints a row where
they agree elsewhere.** L4786–4787: *"§11's nested sum counts the tree system; they agree on Λ and
nowhere else."* The table three lines above (L4782) prints 2S ≤ k at **74 / 74** — an agreement on
Λ ∪ {y}. MEASURED over single-constraint violators (30 per class, 24 for g ≤ 4f+2): the full
pairwise operator and the tree-only operator agree on **30/30** of the 2S ≤ k insertions, **30/30**
of the g ≤ q insertions, 10/30 of q ≤ k and 8/24 of g ≤ 4f+2, and on **0/30** of ℓ ≤ n−1, k ≤ 4ℓ+2
and f ≤ e−1. So "nowhere else" is false at 108 measured sites, one of which the section itself
prints. The neighbouring sentence is *correct* and is the fix: L4784's *"the two that agree bound
leaves"* names exactly the two constraints that agree everywhere — 2S ≤ k and g ≤ q, both bounding
a variable with no descendants.

**13p-11 — the A/fibre model does not reproduce, and "fibre" is defined nowhere in the section.**
L4721–4722: *"A ≈ fibre × (0.972 − 0.154 · descendants of the bounded variable), corr(descendants,
A/fibre) = −0.942, median error 7 %, worst 24 %."* Two readings of *fibre* were swept, because the
section never states one:

- *fibre = the alphabet size of the bounded variable* — A/fibre lands at 3.75 to 104.5, three orders
  from the printed band; corr = **+0.819**.
- *fibre = the number of ambient-box cells breaking exactly that constraint* — corr = **+0.284**,
  and the per-row ratios are 0.397 / 0.244 / 0.625 (descendants 0), 0.955 / 0.311 (descendants 1),
  0.477 (3), 0.679 (4).

Under the second reading, and using the A figures **the book itself prints at L4780–4782**, two of
the three rows reproduce to two decimals — ℓ ≤ n−1: 119/308 = **0.386** against a printed **0.39**;
k ≤ 4ℓ+2: 269/564 = **0.477** against a printed **0.48** — and f ≤ e−1's 0.955 lands at the top of
the printed 0.66–0.95 band. The three descendants-0 rows do not: measured 0.397, 0.244 and 0.625
against a printed 0.96–0.99. The printed correlation of −0.942 reproduces under neither reading.
Recorded, not identified: the model is partly reconstructible but the section does not supply the
definition its own figures were computed against. The 13j-07 / 13l-09 / 13n-02 class.

**13p-12 — the 397 % jump does not reproduce, though the fact it illustrates does.** L4710:
*"which is why *g* ≤ 4*f*+2 … is an order of magnitude cheaper to violate than any other. **Remove
the rival and it jumps 397 % into the normal band.**"* MEASURED: g ≤ 4f+2's violators have median
A = **15** against a band median of **179** over all single-constraint violators — an order of
magnitude, confirmed. Rebuilding the index with the rival g ≤ q dropped (1,649 cells) and
re-measuring the same class gives median A = **193** over 291 cells: a jump of **+1,187 %**, and it
does land in the normal band. A 397 % jump would take 15 to 74.6; the population gives 193.
Reading-dependent in the same way as 13p-11 and recorded with it.

**13p-13 — the reference index's four figures are consistent under 156 readings of constraints the
section does not state, and its "cycle" does not follow from the two it does state.** §16.6.1 L4537:
*"**38 cells, ambient box 144, density 26.4 %, E = 0**"*, and L4538–4539: *"**And it is not a
tree**: access bounds *referent at its top value* and bounds *checked* directly, closing the cycle
access–referent–checked. Width 2."* MEASURED: the box is 4 · 3 · 3 · 4 = **144** ✓ and 38/144 =
26.39 % ✓. Sweeping every monotone reading of the three named bounds (9,000 combinations),
**156** give exactly 38 cells with E = 0 — the figures are consistent but do not pin the index down.
And the two constraints the text names are **two edges on three nodes**: access→referent and
access→checked form a path, not a cycle; closing access–referent–checked needs a third edge between
referent and checked, which the section never states. The 13n-02 class, with an added structural
claim that does not follow from its own stated premises.

## B. Verified

**B1 — the fabrication, exactly.** Inserting the cell (n, ℓ, k, q, e, f, g, 2S) = **(1, 0, 1, 0, 1,
0, 0, 2)** — one electron asking 2S = 2 — and closing under join and meet gives **1,051** cells,
A(y) = **74**, **75** new cells, every one of them breaking **2S ≤ k** and nothing else. The
fabrication is closed under join and meet (0 leaks each way), has **E = 0**, and is a fixed point of
ℛ; so is Λ₈. Every figure at L4624, L4634, L4670–4672 and L4782 reproduces, and 976 + 1 + 74 = 1,051
is internally consistent across four sites.

**B2 — pushback.** Λ₈ has **475,800** unordered pairs of distinct cells ✓ (976 · 975 / 2). Counting,
for each cell, the pairs of *other* cells joining to it or meeting at it: **minimum 16** ✓,
**mean 739.0** ✓, **maximum 5,091** ✓, **cells removable with no failing pair: 0** ✓. The median
measures **503** against a printed **504** — one off, recorded in C4. The least-pushed cell is
**(2, 1, 3, 3, 2, 1, 3, 0)**, at 16, which is the lower endpoint of the step interval of B4.

**B3 — eighteen of each, and the intersection is empty.** MEASURED: **18** cells of Λ₈ are the join
of no pair of others and **18** are the meet of no pair of others; the intersection is **0**. So
L4749–4751 holds exactly, and with it the reason the floor is *derived rather than measured*.

**B4 — step(Λ₈) = 4, and the interval is the one printed.** Searching every interval [a, b] with a
join-irreducible and b meet-irreducible (267 tested) for the smallest whose complement is still
closed under join and meet: **step = 4**, a = **(2, 1, 3, 3, 2, 1, 3, 0)**, b = **(3, 1, 3, 3, 3, 1,
3, 0)**, leaving **972** cells and **471,906** surviving pairs — every figure of L4763–4766 ✓ — free
in exactly the coordinates **n and e** ✓, the two ends of the caterpillar. Λ₈ is closed under join
and meet (0 leaks) and distributive on 20,000 seeded triples, which is what the L4755 theorem's
proof assumes.

**B5 — sixteen binding pairs, and the transitive reduction returns the seven edges.** MEASURED from
the cells: **16** ordered binding pairs, and they are **exactly** the transitive closure of the
seven defining edges (set equality, not just cardinality). Their transitive reduction is the seven:
n→ℓ, ℓ→k, k→2S, k→q, q→g, f→g, e→f. The undirected graph is a tree on 8 nodes with 7 edges. Both
ℛ_full(Λ₈) and ℛ_tree(Λ₈) return Λ₈. L4773–4774 holds in full.

**B6 — the descendants table, every row.** L4724–4729 gives 0 for 2S ≤ k, g ≤ q and g ≤ 4f+2; 1 for
q ≤ k and f ≤ e−1; 3 for k ≤ 4ℓ+2; 4 for ℓ ≤ n−1. MEASURED on the directed dependency graph
(bounding → bounded): **0, 0, 0, 1, 1, 3, 4** — all seven exact. Note this is the *directed* graph,
in which g has two parents; the undirected version is the tree of B5. Read from the undirected tree
the counts would be 6, 5, 3, 0, 2, 1 and wrong — the standing warning of chat 84's B6 applies.

**B7 — g is the only variable bounded twice.** MEASURED: ℓ, k, 2S, q and f are each bounded by one
constraint; **g** by two (g ≤ q and g ≤ 4f+2). L4710's *"the only constraint sharing its variable
with a stricter one"* is exact, and the cheapness it explains is real (median A 15 against a band
median of 179 — an order of magnitude). Only the 397 % is not reproducible (13p-12).

**B8 — A(y) is exact, and deletion is always repaired.** A(y) = N[φ(Λ ∪ {y})] − N[φ(Λ)] − 1 agrees
with the direct cell count on every one of the 5,936 insertions. L4698's *"deletions are always
repaired"* follows from B2 with nothing left to test: every cell of Λ₈ has pushback ≥ 16, so no
deletion survives closure, and C(Λ − x + y) = C(Λ + y) identically.

**B9 — six pointers resolve to the claim.** §17.2 → L4806 carries *adjunction never repairs*
verbatim, as a theorem with proof ✓ (so L4534's use of it to exclude *repair* as a coordinate is
sound). §2.13 → L649 *Commit before you look* ✓. §29.1 → L7859 carries ⅅ(novelty) = 0 ✓. §16.1 →
L4335 the counting argument ✓. §12.11.0.4 → L2725 the separation hypothesis ✓. §16.4 → L4407 is
13o-01's known defect and is not re-derived here; L4525's *"constraints of §16.4 form"* resolves to
the claim at **L1765**, as chat 84 established, and is its eighth site.

**B10 — §19.5 says what §16.6.1 quotes it as saying.** L4550–4551 attributes to §19.5 *"a blocked
ρ = 1 cell is a stated gap, not an unexplained absence"*, and names four documents — Edlén 1964,
Ritz 1908, Paschen & Götze 1922, Dunz 1911. MEASURED: §19.5 L5433–5434 names those four documents
in that order ✓ at ρ ≤ 2, and the phrases *stated gap* and *unexplained absence* occur together at
main L628, L4551 and L5545. The quoted proposition is the book's, sourced, and the four names match.

## C. Incidental

**C1 — the median pushback is 503, printed 504.** One off, on a figure whose four companions
(16 / 739 / 5,091 / 0) are all exact. Λ₈ has an even number of cells, so a "median" over 976 values
is a convention rather than a datum; 503 is the lower of the two central values and 504 the mean of
them would be 503.5. Not a defect of substance; recorded because R3 must choose a convention.

**C2 — "spin multiplicity 2, which no atom has" uses the book's 2S where a reader will read 2S + 1.**
L4621 and L4665. In the book's coordinates the cell is 2S = 2, i.e. S = 1, which one electron indeed
cannot have — the physics is right and the measurement in B1 confirms the refusal. But *spin
multiplicity* in spectroscopic usage is 2S + 1, and multiplicity 2 is a doublet, which is exactly
what one electron does have. The phrase occurs at main L477, L4621, L4665 and mc L1620, and the
main volume states the 2S + 1 convention at none of them. A reader checking the sentence against
standard usage finds it false; a reader using the book's coordinates finds it true.

**C3 — "E is irreducible" is printed over a table in which E falls from 2 to 1.** §16.7.1 L4605
against the belt table at L4601–4603: (p, q) gives E = 2, and both re-coordinatisations give E = 1.
The intended sense — E cannot be driven to **zero**, which is the test of §16.7.1 — is what the rest
of the paragraph argues and what *"0 of 6 admitted"* supports. The word as printed is stronger than
the table beneath it.

**C4 — "thirteen of thirteen above the cut, zero of six below" inverts its own cut.** L4608–4610
says every resonance of order **≤ 7** is occupied and every one of order **≥ 8** is empty, then
calls the occupied ones *above the cut* and the empty ones *below*. The orders that are occupied are
the numerically lower ones. The counts are internally consistent — six absences, matching *"0 of 6
admitted"* at L4605 — only the direction words are reversed.

**C5 — the resonance-strength law carries no source.** L4611's *"Resonance strength enters at
e^|p−q|"* is a standard result of celestial mechanics and is the physical warrant for the whole
asteroid-belt case. MEASURED: the only named sources in the section's 307 lines are Racah (L4510),
and Edlén / Ritz / Paschen & Götze / Dunz (all at L4550, as unretrieved documents rather than as
authorities); *asteroid* occurs at main L4597, L5325 and L5336, *mean-motion* at L4595 and L8632,
and no author is named at any of them. The 13o-02 class — a published result used as a worked case
with no attribution. With 13h-05, 13h-06, 13j-13, 13l-04 and 13o-02.

**C6 — the leaf rule of L4784 is sound one way and not the other.** The two constraints on which the
operators agree everywhere both bound leaves (B5, 13p-10). The converse fails: g ≤ 4f+2 also bounds
a leaf (g has no descendants) and the operators disagree on 16 of its 24 violators, because the full
pairwise operator carries transitively implied bounds (e→g, k→g, ℓ→g, n→g) that the tree operator
does not. "No descendants, no transitive propagation" is true of the bounded variable and false of
the operator.

**C7 — Figure 16.2's registered line is 33 lines off its placement, in a new direction.** MEASURED:
FIGURE_ASSETS.md L24 and FIGURE_MAP.md L21 both register Figure 16.2 at **4679**; it is placed at
main **L4712**. Offset **+33**, outside 13l-07's measured −11 to +29 band and opposite in sign to
13o-05's −31 for Figure 16.1. Both members are process files, so this is production, not
reader-facing; it confirms 13l-07's disposition that the column is unusable for placement.

**C8 — the main-volume Index carries a build remark and a script name.** Discovered while measuring
13p-04. Main **L11419**, inside the reader-facing `## Index`: *"Regenerated from the text on
2026-08-24 (`index_gen.py`) … The previous index (57 terms, 139 entries, 44 relations) carried
locators on the numbering the book had before Part I and Part IV were inserted."* That is an
editorial-process remark and a script name in a reader-facing volume — **Ruling 45** and
**Ruling 46**. The paragraph is also the evidence for 13p-04, so R3 must extract the extent figures
before removing the remark.

**C9 — no heading in the section is truncated, and §16.3 L4366 is not either.** All fifteen `###`
headings in range render whole; §16.7.3's heading is followed by an indented block, which is a
legitimate display line of the kind chat 84 measured at L574, L579, L4277 and five others. A
suspected truncation at §16.3 L4366 was **re-measured from the file and is not one** — the line ends
*"…by a **median of 50 %**, where Na I gives 0.2 %."* and the sentence is complete. Recorded so the
suspicion is not carried.

**C10 — the section cites four Register entries by name and none by count.** Registers 403 (reg
L1499), 404 (L1503), 405 (L1507) and 349 (L1279) all exist and are cited as *"Register N"*, the
naming form; the counted form *"Registers N"* occurs zero times in range, so `register_cites.py`
counts none of them (G0i). L4502's *"Twenty-one structural audits passed on a companion document
carrying five of them"* has one other site — reg L1501, inside Register 404's neighbourhood — and
the "five" has no stated population at either site.

## What was not done

The periodic-table E figures (36 / 106 / 0), the asteroid-belt E figures (2 / 1 / 1), the 0 of 6 and
36 of 36 admission counts, and §16.6.1's *"thirteen cells occupied of thirty-eight, E = 11"* were
**not re-measured on their own data** — those catalogues are not in r2lib and are not reconstructible
from the tower. Their arithmetic and their agreement with other sites were checked (the 36 / 106 / 0
triple reproduces main L1583–1585 exactly; the 28-term breakdown sums to 28 and 19/28 = 67.86 %
rounds to the printed 68 %). Adding the periodic table and the belt to r2lib is owed before Chapter 6
or Chapter 19 is read.
