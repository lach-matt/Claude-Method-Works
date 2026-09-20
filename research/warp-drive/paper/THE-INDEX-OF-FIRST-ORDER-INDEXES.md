# The Index of First-Order Indexes

### An admissible chart for indexes of the periodic elements, its eight lawful channels, and what four refusals establish

**Matthew Lach** - Independent Researcher, with a computing collaborator, under the protocols of The Method v1.6

---

**Abstract.** A first-order index is a finite set of cells obtained by charting a body of atomic, nuclear or particle data on a fixed list of coordinates, subject to one gate: every member must carry quantum numbers of its own. Five closure operators act on such a set, and which of them close it is a property of the set. We prove that only 8 of the 32 subsets of the five can occur, characterise them as the down-sets of a seven-relation law, and use the resulting triple (channel, height, width) as an admissible chart. Charting every index this project seats gives a second-order object of 24 vertices on 24 distinct cells, and ALL EIGHT CHANNELS ARE OCCUPIED BY CHARTS OF REAL DATA, so the bound is tight from nature and not only by construction. We prove that 2-determinacy is vacuous at arity 2 and derive that an arity-2 chart cannot occupy the two lowest channels, which accounts for the difficulty of the channel that was last reached. Its occupant is arity 3, where 2-determinacy is not vacuous and statistics must be EARNED; that is a measured fact about the occupant and not a consequence of the corollary, which does not reach that channel. We then take the register's own DEMAND -- the cells its join-closure requires and no member occupies, 4,759 of them -- and adjudicate it. Three theorems decide most of that adjudication before any physics is brought: the demand invents no coordinate value; a bound monotone in the coordinates can never forbid a demanded cell; and the quark model forbids no cell of the meson chart. One bound in the register is non-monotone, and it empties 894 of the 1012 demanded baryon cells. The remainder splits 36 UNPLACED, 2,503 OPEN and 98 UNDECIDED by a source-completeness rule, and the three bins are not interchangeable: they separate what nature forbids from what a source failed to record from what is genuinely predicted. THE CLASSIFICATION, THE INVARIANT AND THE TWO VACUITY THEOREMS ARE THE CONTRIBUTION AND THE REGISTER IS AN EXHIBIT OF THEM. In particular: whether a physical constraint can rule anything out of a table is decidable FROM THE SHAPE OF THE CONSTRAINT ALONE, before any data is gathered, and for most constraints the answer is no. Every figure here is read from a runnable instrument at build time and no figure is typed.

---

## 0. The two questions

This paper is written to answer two questions about the object it describes, and it is organised so that a reader can check either one without reading the other.

> **Q1 - HOW IS IT TRUE?** What is proved, what is measured, what is assumed, and what would falsify each. Sections 1 to 9 answer this. Every claim is either a theorem with its proof in place, a measurement with the instrument that produced it named, or a refusal with the ground it was refused on.

> **Q2 - WHY IS IT NECESSARY IN THE FIELDS OF STUDY?** What can be asked with this object that cannot be asked without it. Section 10 answers this, and it answers it with the things the object has already found rather than with what it might find.

> **Note.** A third question is not answered and is not asked: whether the register is COMPLETE. The registry carries a completeness flag and it is false. This is the set of first-order indexes found and survived their tests, and section 14 keeps that distinction explicit.

## 1. Notation and definitions

Fix a finite list of coordinates. Each coordinate ranges over a finite totally ordered alphabet, and the BOX is the product of the alphabets that actually occur. A CELL is a point of the box; an INDEX is a finite set of cells.

```
Box(X)  =  A_1 x ... x A_d        A_i = { x_i : x in X }   the OBSERVED alphabet
x <= y  <=>  x_i <= y_i for every i          the containment order
x v y   =  lambda i . max(x_i, y_i)          the JOIN, componentwise
x ^ y   =  lambda i . min(x_i, y_i)          the MEET, componentwise
```

> **Note.** THE BOX IS OBSERVED AND NEVER DECLARED. It is the product of the alphabets the index's own members exhibit, not a range chosen in advance. Section 9's Lemma N1 shows this is not a convention: on a declared ambient box the order operator over-generates, and the hierarchy-law companion paper makes the same point from the other side.

The five closure operators, each a map from subsets of the box to subsets:

```
order       R      =  lambda X . the sublattice hull of X under ^ and v
algebra     G      =  lambda X . the sublattice hull, generated
geometry    H      =  lambda X . hull-completion on every coordinate PAIR
information J      =  lambda X . closure under v alone
statistics  S_k    =  lambda X . { b in Box(X) : every k-coordinate
                                   projection of b occurs in X },  k = 2
```

A language L CLOSES an index X when L(X) = X. The CHANNEL of X is the set of languages that close it, and by Theorem 1 it is one of eight, indexed K0 to K7.

```
K(X)      =  { L : L(X) = X }                the channel
height(X) =  the longest chain in (X, <=)     MIRSKY
width(X)  =  the largest antichain in (X, <=) DILWORTH
cell(X)   =  ( K(X), height(X), width(X) )    THE ADMISSIBLE CHART
J(X)      =  the least v-closed superset of X
D(X)      =  J(X) \ X                         the DEMAND
E(X)      =  | D(X) |                         its size
```

And one predicate, which is the gate on membership rather than a measurement of it:

```
chi(m)    =  TRUE iff the member m carries quantum numbers OF ITS OWN
```

## 2. The criterion, and why it is a function rather than a paragraph

> **C.** A member of a first-order index must carry quantum numbers of its own. Not its host's, not its container's, and not a label that happens to be numeric.

An electron, a subshell, an ionisation transition, a spectroscopic term, a nuclide-charge state, a meson, a baryon, a fractional-quantum-Hall quasiparticle and a nuclear excited state all satisfy chi. A file, a build snapshot, a conversation and a document do not. Neither does a chemical bond, a binding energy or a scattering channel, and those three were each tested against chi and refused on their own measured ground rather than by assertion - section 13.

> **Note.** THE CRITERION IS ENFORCED IN CODE AND THE REASON IS HISTORICAL. While it was a paragraph, thirteen filing-system indexes were seated as vertices - mirrored files, conversations, archives, handoff documents - beside indexes whose members are electrons. Every one of the disruptive vertices was repository metadata and not one was a physical object. The explosion in demand that followed was reported as a finding; it was contamination, and it is withdrawn. `registry.enforce()` now returns the violations and returns the empty list.

> **Lemma 2.1 (the host trap).** If a candidate member's quantum numbers are properties of a containing object rather than of the member, the chart measures the container and reports it as the member. The test is whether two members of the same container can differ in the coordinate.

PROOF. Suppose coordinate c is constant on every container. Then the fibre of the chart over c is a union of whole containers, so |{cells}| counts containers and not members, and height and width are measured on the container order. The converse is the test: if some container holds two members differing in c, c is not the container's. []

> **Note.** THIS IS NOT HYPOTHETICAL. It is why the molecular orbital's sigma/pi is refused - the symmetry label is the MOLECULE's - and why Z and N are refused as coordinates of the deformed nuclear band index, being the host nuclide's and not the level's. The second refusal was paid back immediately: a later audit found 35 of 234 entries carrying the wrong nuclide, and because Z and N were not coordinates the defect could not reach the chart. A refusal that costs nothing is not evidence; one that catches a real defect is.

## 3. Theorem 1 - the lawful channels are the down-sets of the law

The companion paper derives eight clauses relating the five operators. This paper needs only the containments, which are these:

| contained | in | source |
|---|---|---|
| order | algebra | Clause B |
| algebra | order | Clause B |
| information | algebra | Clause C |
| information | order | Clause C |
| statistics | algebra | 6d, three-line proof |
| statistics | order | 6d, three-line proof |
| statistics | geometry | Clause G.3 |

> **Theorem 1.** The set of languages closing an index is a DOWN-SET of the containment law, and every down-set occurs. There are exactly 8, of the 32 subsets of five.

PROOF. Write cl[L] for the closure of X under L. Every operator is EXTENSIVE: X subset-of cl[L](X) for all L. Suppose (a, b) is one of the seven containments, so cl[a] subset-of cl[b], and suppose b closes X, i.e. cl[b](X) = X. Then cl[a](X) subset-of cl[b](X) = X, and by extensivity X subset-of cl[a](X); hence cl[a](X) = X and a closes X. So the closing set is closed downward. Enumerating the down-sets of the seven relations over five languages gives exactly 8. []

| channel | languages that close |
|---|---|
| K0 | (none) |
| K1 | information |
| K2 | statistics |
| K3 | geometry+statistics |
| K4 | information+statistics |
| K5 | geometry+information+statistics |
| K6 | algebra+information+order+statistics |
| K7 | algebra+geometry+information+order+statistics |

> **Note.** The law leaves exactly two languages free to close alone: information and statistics. Nothing forces either from anything else. That asymmetry is what makes K1 and K2 reachable at all, and section 6 shows the freedom is exercised very differently by the two.

### 3.1 The converse, and how its status changed

The converse half of Theorem 1 - that every down-set OCCURS - was originally proved by EXHIBITION: for each down-set, a set of cells was constructed that closes exactly under it. That is a proof, and it is the weaker of the two available.

> **Theorem 1a (tightness from nature).** Every one of the eight lawful channels is occupied by a seated first-order index - a chart of real atomic, nuclear or particle data whose members carry quantum numbers.

| channel | closes | seated indexes there |
|---|---|---|
| K0 | (none) | baryons, channels, fqh, gravity, ions, laws, mesons, observed, readrezayi, terms |
| K1 | information | gravity_bound |
| K2 | statistics | deformedbands, fundamental, inversion, madrule, nucbands, probability |
| K3 | geometry+statistics | fibred, nucshell |
| K4 | information+statistics | spin4 |
| K5 | geometry+information+statistics | baryon_isomultiplet |
| K6 | algebra+information+order+statistics | madelung_slot |
| K7 | algebra+geometry+information+order+statistics | bosonqp, madelung |

PROOF. By exhibition, and the exhibits are in section 5. []

> **What 'from nature' admits.** A chart counts as real data here when its members are MATHEMATICALLY ESTABLISHED BEYOND DOUBT, whether or not they have been observed. Absence of observation is not falsification. The criterion is stated because one of the eight channels turns on it.

THAT CHANNEL IS K1, and it has a single occupant. gravity_bound is charted on the horizon-bound class of a singly-rotating Myers-Perry black hole, and its channel DEPENDS ON THE SPACETIME DIMENSIONS ADMITTED: D<=5 gives K7, D<=6 gives K1, D<=7 gives K1, D<=8 gives K1, D<=9 gives K1, D<=10 gives K1, D<=11 gives K1. Restricted to five and below it is K7 and K1 empties. The bound class is not speculative physics: it is whether r^(D-3) + a^2 r^(D-5) = mu has a root, which is exact in every D, with a bound on rotation at five and none above it (Myers and Perry, 1986). By the criterion above the chart is admitted - and the dependence is stated here rather than left for a reader to discover, because the paper's own instrument has always pinned this sweep and the paper had never said it.

> **Note.** THE DIFFERENCE MATTERS AND IS NOT RHETORICAL. A bound proved tight by construction says the combinatorics admits eight. A bound proved tight by nature says the physical world supplies all eight, so no further clause can be added to the law without contradicting a measurement. TWO OF THE EIGHT WERE EMPTY WHEN THIS PAPER WAS FIRST DRAFTED and the statement above could not have been made then; that is a fact about this project's history rather than a measurement of anything, and it is stated in words for that reason.

## 4. The admissible chart

An index is charted by the triple (K, h, w). Mirsky's theorem gives height as the minimum number of antichains covering the order; Dilworth's gives width as the minimum number of chains. Both are exact and neither is an estimate.

> **Lemma 4.1 (the box is ragged).** |X| <= height(X) x width(X), so the three coordinates are not independent and the product box overstates the space.

PROOF. By Dilworth, X is covered by width(X) chains; each chain has at most height(X) elements. []  Checked on every seated index: 0 violations.

### 4.2 Why these three coordinates and not the earlier five

> **Criterion (order admissibility).** An ORDER invariant is admissible iff it survives appending a MONOTONE REDUNDANT coordinate to the index, since such an append preserves the containment order exactly and therefore must not move any measurement OF THAT ORDER.

Measured over the 9 superseded charts of the earlier inventory - which is the population the sweep actually runs on, and is named here because an earlier draft said 'the seated indexes' and meant these - ARITY moves on every one and so does DENSITY, both being facts about the box and not about the order. height, width, cells, comparable pairs and join-irreducibles do not move at all. C, Sc and Oc of the earlier five-coordinate chart are all functions of K, so the five collapse to three with no loss and one gain: K separates channels that (C, Sc, Oc) merged.

### 4.2a K is not an order invariant, and that is a theorem about it

An audit applied the criterion above to K and K FAILED IT. The append g(c) = sum(c) is redundant, monotone, and an order isomorphism onto its image, so the criterion as first written admits it - and it moves K on 12 of the 19 seated indexes small enough to test. The criterion is sound; applying it to K was a category error, and the error was in the paper's favour. Height and width are invariants of the poset (X, <=). K IS NOT, AND WAS NEVER AN INVARIANT OF IT.

> **Lemma 4.2 (what K is an invariant of).** K is an invariant of X AS A RELATION ON A PRODUCT OF CHAINS, not of the abstract order (X, <=). It is preserved by the automorphisms of that ambient structure - permutation of the coordinates and strictly monotone relabelling of each coordinate's alphabet - and by appending any coordinate whose map is a LATTICE HOMOMORPHISM. It is not preserved by an arbitrary order-isomorphic append.

PROOF of the negative half, which is the half that bites. Each of the five operators is defined by the componentwise max and min of the ambient product, not by the order alone. An append c |-> (c, g(c)) with g monotone is an order isomorphism onto its image for any monotone g, but it carries the join only when g(a v b) = max(g(a), g(b)); for g = sum, a = (1,0) and b = (0,1) give g(a v b) = 2 against max(g(a), g(b)) = 1, so the image is not join-closed and every language above information falls with it. The positive half is immediate: a lattice homomorphism carries both operations, so every closure is computed on an isomorphic structure. []

| append or transformation | is it a lattice homomorphism | K moves on |
|---|---|---|
| append a coordinate projection, c[0] | yes | 0 of 19 |
| append the last coordinate, c[-1] | yes | 0 of 19 |
| append 2*c[0] + 1, monotone f o projection | yes | 0 of 19 |
| append sum(c) | no | 12 of 19 |
| append max(c) -- join only | no | 6 of 19 |
| append min(c) -- meet only | no | 7 of 19 |

The two halves come apart exactly as the proof predicts: max carries the join and not the meet, min the meet and not the join, and each moves K on part of the register while the coordinate projections - the lattice homomorphisms - move it on none.

### 4.2b What K is, in the language of another field

K is not a bespoke invention, and a reader should not have to take it as one. A closure operator fixes X exactly when the operation generating it is a POLYMORPHISM of X read as a relation - an operation under which the relation is closed. So:

| this paper's operator | closes X if and only if |
|---|---|
| information | binary max is a polymorphism of X |
| order / algebra | max AND min are both polymorphisms -- X is a sublattice |
| statistics | X is 2-DECOMPOSABLE: X is the join of its binary projections |
| geometry | X is closed under the pairwise 2-D hull |

That places K inside the Pol-Inv Galois connection of universal algebra (Geiger; Bodnarchuk, Kaluznin, Kotov and Romov, 1968-9), where the set of polymorphisms of a relation is its clone and determines what can be said about it. Closure under a semilattice operation such as max, and decomposability into binary projections, are the two classical tractability conditions of constraint satisfaction (Jeavons, Cohen and Gyssens; Feder and Vardi). K IS A FRAGMENT OF THE POLYMORPHISM CLONE, and Lemma 4.2 is then unsurprising: a clone is an invariant of the relational structure, which is exactly the structure an order isomorphism is free to discard.

> **Note.** AND IT HAS A READING IN THE PHYSICS. statistics closing says every selection rule coupling the quantum numbers is PAIRWISE - there is no irreducibly three-body rule among them. information closing says the realised set is closed under taking the componentwise maximum of any two realised states. order closing says it is a sublattice. So K states THE ARITY AT WHICH THE SELECTION RULES ACT, which is a physical property of the index and not a bookkeeping one.

### 4.3 The chart applied to itself

Applying the chart to the object it produces is a test that object can fail. A coordinate whose distinct values number 90 per cent or more of its members separates everything and therefore groups nothing: it is a row identifier wearing a measurement's clothes.

| axis | distinct | of | ratio | verdict |
|---|---|---|---|---|
| K | 8 | 24 | 0.3333 | measurement |
| height | 17 | 24 | 0.7083 | measurement |
| width | 17 | 24 | 0.7083 | measurement |

No axis is a row label. At eleven vertices two of the three were row labels - height at 0.909 and width perfectly injective at 1.000 - and the reading filed with that finding was that each index brings its own height and width, so the two approach injectivity by construction as the object grows. THAT READING IS REFUTED by the table above: the object grew and the labels became measurements. The prediction failed because a COARSENING of a seated index does not bring a new height and width; it lands in the part of the poset its parent already occupies.

The second-order object has 24 vertices on 24 distinct cells - no two seated indexes share a cell - it closes in nothing, its demand E is 512, and its own cell is (0, 5, 11), which no member occupies.

## 5. The register - every seated index

24 indexes satisfy the criterion and are seated. Each row names what one member IS, which quantum numbers it carries, how many distinct cells the chart has, the cell, and the channel. The METHOD column records how the index was built: TABLE reads a source, FIBRATION addresses a member by its position in a construction, RESIDUAL charts the departure of a measurement from a rule.

| index | method | one member is | quantum numbers | cells | cell | arity |
|---|---|---|---|---|---|---|
| fibred | FIBRATION | 170 electrons, MADELUNG-PREDICTED | n, l, k | 170 | (3, 26, 17) | 3 |
| madelung | FIBRATION | the same 170 electrons, MADELUNG-PREDICTED | n+l, l, k | 170 | (7, 30, 12) | 3 |
| ions | TABLE | 98 Lambda-8 transitions | charge, electron count | 98 | (0, 18, 16) | 7 |
| channels | TABLE | 209 spectroscopic channel shapes | l, Pauli bound, multiplicity | 209 | (0, 16, 24) | 3 |
| laws | RESIDUAL | 584 series against Rydberg-Ritz | n range, l, quantum defect | 54 | (0, 25, 7) | 3 |
| probability | TABLE | 25 subshells | n, l | 25 | (2, 8, 9) | 3 |
| inversion | TABLE | 20 fill-order/shell-order inversions | pairs of (n, l) | 17 | (2, 6, 5) | 3 |
| gravity | TABLE | 3,394 nuclide-charge states x 8 dimensions | Z, N, A, q, Ne, 2J, level status | 914 | (0, 19, 112) | 7 |
| nucshell | TABLE | 22 nuclear single-particle subshells | nr, l, j (nuclear) | 22 | (3, 7, 6) | 3 |
| madrule | RESIDUAL | 20 Madelung exceptions, by their transfer | n+l of the acceptor, l of the donor, occupancy | 13 | (2, 6, 4) | 3 |
| terms | TABLE | 5,132 Russell-Saunders terms over 122 spectra | 2S+1, L, parity, the banked J set | 112 | (0, 13, 18) | 4 |
| observed | FIBRATION | 108 observed differentiating electrons, register 1306 | n, l, k (observed) | 98 | (0, 20, 13) | 3 |
| gravity_bound | TABLE | the same 3,394 nuclide-charge states, on the bound structure alone | horizon-bound class, forced angular momentum, spin-decade rank | 26 | (1, 8, 5) | 3 |
| madelung_slot | FIBRATION | the same 170 electrons, subshell-blind | n+l, k | 82 | (6, 26, 6) | 2 |
| fundamental | TABLE | 30 Standard Model particles -- 12 quarks, 12 leptons, 6 gauge/Higgs | 2J, Q3, colour dimension, generation | 26 | (2, 7, 7) | 4 |
| mesons | TABLE | 242 mesons of the PDG table, 8 set aside for want of a printed parity | 2J, P, 2I, Q3 | 66 | (0, 10, 14) | 4 |
| baryons | TABLE | 278 baryons of the PDG table, 14 set aside for want of a printed parity | 2J, P, 2I, Q3, strangeness, charm, beauty | 184 | (0, 10, 40) | 7 |
| baryon_isomultiplet | TABLE | the same 278 baryons, isospin against charge with flavour dropped | 2I, Q3 | 16 | (5, 7, 4) | 2 |
| fqh | TABLE | 168 quasiparticles of twelve Laughlin states, three of them observed | statistics class, order of the exchange phase, order of the charge, inverse filling fraction | 30 | (0, 15, 4) | 4 |
| bosonqp | TABLE | 15 bosonic excitations -- composites, Goldstone modes and hybrids, every number derived | 2J, Q3 | 5 | (7, 4, 2) | 2 |
| readrezayi | TABLE | 363 parafermion primaries of eleven Read-Rezayi states, two observed | statistics class, order of the twist, order of the charge, level | 78 | (0, 19, 11) | 4 |
| spin4 | TABLE | 10 spin-4 mesons, two of them without a printed mass | P, 2I, Q3 | 9 | (4, 5, 3) | 3 |
| nucbands | TABLE | 2,145 nuclear excited states in magnetic and antimagnetic rotational bands; 27 bands and 93 levels refused for carrying no quantum number | 2I, parity | 121 | (2, 63, 2) | 2 |
| deformedbands | TABLE | 1,907 excited states in two-quasiparticle rotational bands of deformed odd-odd nuclei, Z 67-71 and A 156-174 -- the source's TITLE says 156 <= A <= 168 and its table does not, 132 levels sitting above 168; 56 levels refused for carrying a spin and no parity | 2I, parity | 96 | (2, 49, 2) | 2 |

### 5.1 Provenance - what each index reads, hashed

Declared as SOURCE beside the code that reads it, resolved against the repository root and hashed, so the provenance travels in the tree rather than in prose. AN EMPTY PATH LIST IS NOT A GAP: it means the index is COMPUTED from a rule and reads no table, which is a source and is recorded as one.

| index | reads | files |
|---|---|---|
| baryons | "Review of Particle Physics", Particle Data Group, Int. J. Mod. Phys. A 41, 2630011 (2026), via ... | 1 |
| bosonqp | COMPUTED by three rules and nothing else.  COMPOSITION: charge adds and spin combines by angular... | COMPUTED |
| channels | INLINE in this file: spectroscopic channel shapes transcribed from NIST ASD captures, each row c... | COMPUTED |
| deformedbands | Charted from deformed.entries(), which segments captures/arxiv-2508.05447.txt -- Pinky, Kumar, S... | 3 |
| fibred | COMPUTED from the Madelung rule through shells.py; no table is read.  The reach Z <= 108 is LW1-... | COMPUTED |
| fqh | COMPUTED from the Laughlin wavefunction's closed form -- R. B. Laughlin, Phys. Rev. Lett. 50, 13... | COMPUTED |
| fundamental | "Review of Particle Physics", Particle Data Group, Int. J. Mod. Phys. A 41, 2630011 (2026), via ... | 1 |
| gravity | AME2020 Table I for the nuclides, and the NIST ASD level captures in recovered/ for the charge s... | 2 |
| inversion | COMPUTED from fibred.py's Madelung construction; no table is read. | COMPUTED |
| ions | COMPUTED from the Madelung construction through charts3.py; the reach Z <= 108 is LW1-ground.py'... | COMPUTED |
| laws | Rydberg-Ritz series read from the corpus's own spectra table. | 1 |
| madelung | COMPUTED from the Madelung rule, the same construction fibred.py projects; no table is read. | COMPUTED |
| madrule | Register 1306's banked observed ground configurations, against the Madelung prediction. | 1 |
| mesons | "Review of Particle Physics", Particle Data Group, Int. J. Mod. Phys. A 41, 2630011 (2026), via ... | 1 |
| nucbands | Read from captures/NUCBANDS-levels.tsv, written by nbcapture.py from captures/arxiv-2303.13849.t... | 3 |
| nucshell | A seated member of The Method, imported by path and never copied. | 1 |
| observed | Register 1306's banked observed ground configurations, a seated member loaded by path. | 1 |
| baryon_isomultiplet | Inherited: every row here is a coarsening of a parent index and reads exactly what that parent r... | COMPUTED |
| gravity_bound | Inherited: every row here is a coarsening of a parent index and reads exactly what that parent r... | COMPUTED |
| madelung_slot | Inherited: every row here is a coarsening of a parent index and reads exactly what that parent r... | COMPUTED |
| probability | COMPUTED from fibred.py's Madelung construction; no table is read. | COMPUTED |
| readrezayi | COMPUTED from the Z_k parafermion closed form -- Zamolodchikov and Fateev (1985); Moore and Read... | COMPUTED |
| spin4 | Read from `mesons.rows()`, the seated meson index, which reads captures/PDG-2026.tsv.  The PDG s... | 1 |
| terms | The NIST ASD level tables held in recovered/, read as a directory; four files are refused by nam... | 1 |

### 5.2 What is excused, and on which ground

9 modules in the tree look like indexes and are not, and each carries its ground. The grounds are of three kinds and they are not interchangeable: failing the criterion, failing box invariance, and - one case - having had an incomplete capture, which was retired when the capture closed.

| module | the ground it is excused on |
|---|---|
| axes | members are measurement axes |
| bonds | chemical, atomic and particle bonds -- REFUSED three times over: the molecular orbital's +/- is provably the MOLECULE's and its g/u the HOST's, leavin... |
| deformed | the CAPTURE of the deformed two-quasiparticle bands, not an index -- the levels it segments are seated as `deformedbands`.  TWO refusals were RETRACTE... |
| entropy | members are the seated indexes |
| figure | the index of first-order indexes: its members ARE the seated indexes, so they carry no quantum numbers |
| mi | members are the seated indexes -- and NINE OF THEM ARE NOT REGISTERED ONES; figure.superseded_mi() measures it |
| necindex | members are energy conditions |
| quasiparticle | members ARE quantum objects and the criterion passes -- the chart is refused by BOX INVARIANCE instead, the channel being K2 at every box, so it is a ... |
| rindex | members are refusals |

## 6. Theorem 2 - 2-determinacy, and why one channel was the last to fall

> **Theorem 2.** statistics closes EVERY arity-2 index, vacuously, and this is a property of the definition rather than of any implementation.

PROOF. S_k(X) is the set of box points all of whose k-coordinate projections occur among X's. At arity 2 there is exactly one 2-subset of the coordinates - the whole of them - so the projection is the identity and the reconstruction returns X itself. Hence S_2(X) = X for every X whatever. []

Measured over every coordinate subset of every seated index the sweep reaches - 21 of the 24, the 3 coarsenings being excluded because their sub-charts are sub-charts of their parents and are counted there - 458 sub-charts in all. THE POPULATION IS STATED BECAUSE IT WAS ONCE WRONG: the sweep skipped a missing coordinate list silently and covered 15 of 24 while the prose implied all of them, dropping the very index this section closes on.

| arity | statistics closes | does not |
|---|---|---|
| 2 | 126 | 0 |
| 3 | 64 | 71 |
| 4 | 12 | 98 |
| 5 | 1 | 62 |
| 6 | 0 | 21 |
| 7 | 0 | 3 |

> **Corollary 6.1.** An arity-2 chart cannot occupy K0 or K1.

PROOF. Its channel contains statistics by Theorem 2, and neither K0 nor K1 does. [] Measured over the same sub-charts, the arity-2 channels observed are K2 (38), K3 (27), K4 (4), K5 (4), K6 (3), K7 (50) - K0 and K1 occur zero times, as the corollary requires.

> **Note.** THIS IS WHAT MADE K4 THE HARD CHANNEL, and the difficulty was structural. The law protects K5 and K6 from the free pass, because geometry closing forces statistics and so does the order/algebra block; at those channels the statistics bit is earned by law whatever the arity. K4 = {information, statistics} has neither protection - nothing forces statistics from information - so it is the only channel above K1 whose extra content is exactly the bit an arity-2 chart is given for free. For a long stretch the only charts reaching K4 were arity 2, and a census over 232 modules found no chart of any arity reaching it.

IT IS NOW OCCUPIED, AND AT ARITY 3. The seated index at K4 is spin4, charted on 3 coordinates - an arity at which 2-determinacy is not vacuous and statistics has to be EARNED. The channel the theorem predicted would be hardest is reached, and reached in the way that makes it a measurement rather than a gift. The explanation survives as an account of the difficulty; it is no longer an account of an absence.

## 7. The overlap ruling - when two charts of one subject may both be seated

> They can be seated with overlaps so long as it is not an overlap of same information. An overlap of values in two different languages should tell us two parts of definition contained in that overlapped position. Information is information. But its relative position in this index is information about an object.

A COARSENING - the same members charted on fewer coordinates - overlaps its parent totally. Four readings of the ruling were charted against all 437 proper sub-charts of the 21 non-coarsening seated indexes: 'channel differs from its parent' admits 173, 'cell differs from its parent' 416, 'cell no seated vertex holds' 403, and 'CHANNEL no seated vertex holds' admits 10. The third admits 116 coarsenings of baryons alone; the fourth is bounded, and it is what the ruling says, since the ruling names LANGUAGES and the channel is the set of languages that close a chart. Text and arithmetic select the same reading.

> **Note.** THESE FIVE FIGURES WERE TYPED AND ALL FIVE HAD GONE STALE. They were measured when the register held eleven indexes and never moved as it grew to 24; the instrument that produced four of them could not even be run, raising on the first seated index missing from its coordinate table, and the fifth was computed by no function at all. They are read from the instrument now, and the reading the ruling selects is unchanged - R4 is still far the most bounded.

Four grounds are tested and a candidate must clear all four:

- **NOVEL CHANNEL** - the chart reaches a channel no seated index reaches.
- **NOT A RELABELLING** - it has strictly fewer cells than its parent; a chart that separates exactly as much is the parent renamed.
- **REACH STABLE** - the channel does not depend on where the construction stopped: no late arrival, no oscillation, and a majority of reaches.
- **COORDINATE FORCED** - the channel survives a faithful re-coordinatisation. Two addresses inducing the identical partition of the identical members are one chart written twice.

Of 7 candidates, 3 seat and 4 are refused.

| chart | channel | cells | verdict / ground failed |
|---|---|---|---|
| gravity (B, F, X, E) | K1 | 52 | SEATED |
| madelung (n+l, k) | K6 | 82 | SEATED |
| baryons (2I, Q3) | K5 | 16 | SEATED |
| gravity (B, F, X) |  |  | refused: maximal |
| ions (sl, tl) |  |  | refused: novel channel, reach stable |
| madrule (S_a, l_d) |  |  | refused: novel channel, reach stable |
| nucshell (l, sigma) |  |  | refused: coordinate forced |

> **Lemma 7.1 (the ruling has a subject).** The four grounds test a COARSENING. Two indexes sharing no member are not overlapping charts, and the ruling does not apply to them however many coordinate NAMES they share.

PROOF. A coarsening is a chart of the SAME member set on a subset of the coordinates, so 'strictly fewer cells than its parent' presupposes a parent. Where the member sets are disjoint there is no parent, the second ground is undefined, and the first is not a test of overlap but of novelty. [] This is not academic: the nuclear rotational-band index and the deformed two-quasiparticle index carry the SAME two coordinate names, (2I, parity), and share ZERO nuclides. Sharing a coordinate's name is not sharing information, any more than two nuclides sharing a Z would be.

> **Note.** AND THE FIRST GROUND GIVEN FOR THAT ZERO WAS FALSE. It was stated that the two mass ranges are disjoint. They are not - one index spans A 58-205 and CONTAINS the other's 156-174 entirely. The zero is a measured fact about which nuclides each source happens to tabulate, not a consequence of where they sit. An audit caught it and the weaker, true ground replaces the stronger, false one.

## 8. The demand, and what an empty cell means

E(X) = |J(X) \ X| is the number of cells an index's own join-closure requires and no member occupies. Measured over every seated index small enough to close - , at 914 cells, is not, and is NAMED HERE rather than dropped, so the 18 rows below and the 6 complete indexes and it account for all 24 seated - the register demands 4,759 cells it does not hold.

| index | E |
|---|---|
| gravity | 1550 |
| baryons | 1012 |
| readrezayi | 678 |
| channels | 367 |
| ions | 296 |
| laws | 254 |
| fibred | 140 |
| probability | 112 |
| terms | 98 |
| fqh | 71 |
| observed | 56 |
| fundamental | 46 |
| inversion | 24 |
| madrule | 18 |
| mesons | 15 |
| nucshell | 14 |
| nucbands | 5 |
| deformedbands | 3 |

> **Note.** The partition is exact - every E = 0 index closes under information and every E > 0 index does not - and it is close to definitional, since E is the join deficit and the information closer IS the join closer. It is said so that it is not mistaken for a result. The result is the numbers.

An unadjudicated E is a count of QUESTIONS and not of objects. A demanded cell is one of three things, and only the third is a prediction:

- **FORBIDDEN** - a bound rules the combination out; emptiness is a theorem
- **UNPLACED** - the object exists and the source gives it no coordinates
- **OPEN** - physical, placeable, and nothing there -- a real prediction

### 8.1 Theorem 3 - the demand invents no coordinate value

> **Theorem 3.** pi_i(J(X)) = pi_i(X) for every coordinate i.

PROOF. X subset-of J(X) gives one inclusion. For the other, J(X) is generated from X by repeated componentwise max, and max(a, b) is either a or b, so every coordinate of every generated cell is a coordinate value already present in X. Induct on the generation. []

> **Corollary 3.1.** No bound constraining a SINGLE coordinate can forbid a demanded cell.

> **Note.** Measured on the largest prediction set in the register: of 1012 demanded baryon cells, ZERO carry an even doubled spin - although 2J even is exactly what the spin-statistics of a three-quark state rules out. The strongest single-coordinate fact available about baryons adjudicates nothing, and Corollary 3.1 says why.

### 8.2 Theorem 4 - a monotone bound forbids nothing

> **Theorem 4.** Let B be a set of cells with X subset-of B and B closed under componentwise max. Then J(X) subset-of B, so B forbids no demanded cell. In particular a bound x_i <= g(x_j, ...) with g non-decreasing in each argument is max-closed.

PROOF. J(X) is the LEAST max-closed set containing X, so it is contained in any max-closed superset of X. For the particular case, let a, b lie in B and c = a v b. Then c_i = max(a_i, b_i) is one of them, say a_i, and a_i <= g(a_j) <= g(c_j) because a_j <= c_j for every j and g is non-decreasing; so c lies in B. []

8 bounds were derived for the seated indexes, each from a stated physical law, each checked against every member of its index before being applied to the demand, and NONE fitted to the demand. 6 of the 8 are monotone.

| index | bound | derived from | monotone | forbidden |
|---|---|---|---|---|
| baryons | three-quark flavour content: (2I, Q3, S, C, B) is realisable by qqq or by anti-qqq, with |n_u - n_d| <= 2I <= n_ud and 2I = n_ud (mod 2) | the quark model, on the capture's own quark strings | NO | 894 |
| fibred | l <= n-1; k <= 2(2l+1) - 1 | radial node count; Pauli exclusion | yes | 0 |
| gravity | the horizon bound B = bound_class(D, q, F, Jzero) with Jzero bounded by X and F; and the decade bound from chi/Qtilde^2 = Je/(q^2 alpha) | exact solutions of the D-dimensional field equations; and the two standard couplings, alpha_G cancelling | NO | 1228 |
| ions | l <= n-1 at both ends; Pauli on k and g; q <= k | radial node count; Pauli exclusion | yes | 0 |
| madrule | occ <= 2(2 floor((S_a-1)/2) + 1) | Pauli exclusion through the hidden l_a | yes | 0 |
| nucshell | l = 0 => sigma = +1 | j = l +- 1/2 and j >= 0 | yes | 0 |
| observed | l <= n-1; k <= 2(2l+1) - 1 | radial node count; Pauli exclusion | yes | 0 |
| terms | mult = 1 => the term is not SHORT | Russell-Saunders: a singlet has one level | yes | 0 |

> **Note.** THE ZEROS ARE NOT A FAILED SEARCH. l <= n-1 is the radial node count n - l - 1 being non-negative; the Pauli caps count the spin-orbitals of a subshell; q <= k says one cannot ionise more electrons than are present; l = 0 forcing the upper spin-orbit branch is j = l +- 1/2 with j >= 0; and a Russell-Saunders singlet has one level, so it cannot fall short of its own multiplet. All are theorems, all hold on every seated member without exception, and by Theorem 4 NONE OF THEM CAN forbid a demanded cell. The hypothesis is verified rather than read off the algebra: each bound's admissible set is enumerated over its index's own product box and closed under join by exhaustion.

### 8.3 Theorem 5 - the quark model forbids no cell of the meson chart

> **Theorem 5.** For a quark-antiquark state P = (-1)^(L+1), C = (-1)^(L+S), S in {0,1} and |L - S| <= J <= L + S. Every (J, P) with J a non-negative integer and P = +-1 is realised.

PROOF, four cases. P = -1 requires L even: for J even take (L, S) = (J, 0); for J odd take (J-1, 1), which is even and non-negative and has L + S = J; J = 0 forces L = S, and L = S = 0 gives 0-. P = +1 requires L odd: for J odd take (J, 0); for J even and at least two take (J-1, 1); J = 0 forces L = S, and L = S = 1 gives 0+. [] Checked by exhaustion to J = 12 with no unreached pair.

The exotic quantum numbers - 0--, 0+-, 1-+, 2+- - are forbidden in J^PC, and C IS NOT A COORDINATE of this chart. It was refused for TOTALITY: 168 of the 250 mesons in the source carry no C at all, and a chart carries only coordinates all its members have. THE REFUSAL WAS CORRECT AND THE TRADE RUNS THE OTHER WAY, which an audit established against an earlier draft of this very paragraph. That draft said a coordinate refused for totality is adjudication power given up. It is not, here: 2 of the C-carrying mesons in the capture are pi(1)(1400)0 and pi(1)(1600)0, whose J^PC is 1-+ -- one of the four exotics just named -- and both carry the source's own quark string 'Maybe non-qQ'. Charting C would not make the exotic cells FORBIDDEN cells of the demand. It would make them OCCUPIED cells of the index, and the q-qbar bound would then FAIL this paper's own gate, which requires a bound to hold on every member before it may touch the demand. The meson index has 15 demanded cells and the quark model empties none of them - but the reason is not a price paid for totality. It is that THIS MEMBER SET IS NOT A q-qbar SET, and refusing C concealed the fact rather than costing anything.

### 8.4 The one bound that forbids

By Theorem 4 only a bound that is antitone somewhere, or carries a congruence, can forbid. One qualifies in the register and it qualifies twice over. Gell-Mann-Nishijima gives the isospin projection 2 I3 = 2Q - Y with Y = B + S + C + B' + T, and I3 must be a weight of the isospin-I representation: |2 I3| <= 2I, an absolute value, and 2I congruent to 2 I3 modulo two, a congruence. Both break max-closure. The baryon chart carries Q, S, C, B and I as coordinates, so the bound is EXPRESSIBLE on it, and it forbids 894 of the 1012 demanded cells - 88.3 per cent of the largest prediction set in the register, emptied by theorem rather than by observation.

The relation is not imported. Writing n_a for quarks minus antiquarks of flavour a, Q = (2/3)(n_u + n_c + n_t) - (1/3)(n_d + n_s + n_b), I3 = (n_u - n_d)/2, S = -n_s, C = n_c, B' = -n_b, T = n_t and B = (sum n_a)/3, whence Q - I3 = n_u/6 + n_d/6 + (2/3)(n_c + n_t) - (1/3)(n_s + n_b) = Y/2 identically. All three legs - the charge built from the quark charges, the isospin projection, and the identity - are re-derived from the source's own quark strings: 292 baryon rows, 292 parse, and 292, 292 and 292 clean without exception.

> **Note.** THE SAME CHECK FOUND A FAULT IN THE SOURCE. 191 of 250 meson rows parse - the rest are flavour mixtures, which is why S, C and B are not coordinates of the meson chart and therefore why the bound is inexpressible there - and of those the charge and the identity are clean at 191 and 191 while the isospin projection fails at 189. The two failures are one state and its antiparticle, B(s2)*(5840)0 and B(s2)*(5840)~0, carrying a strange-beauty content with doubled isospin one, while two other states of the identical content carry zero in the same file. Such a pair holds no up or down quark, so I3 = 0 and I = 1/2 has no weight to sit on. IT IS RECORDED AND NOT REPAIRED, and the cost is measured: with the isospin set to zero on both rows the meson index has 66 cells, E = 15 and chart position (0, 10, 14) - identical before and after, because both affected cells are already occupied by other members.

### 8.5 E is a deficit against an operator, and so is forbidding

Every E above is a JOIN deficit. The same cells measured against the ORDER closure give a different deficit and a different verdict. On the 90 drawn positions of the period-by-group periodic layout the join deficit is 0 and the order deficit is 36, and the hydrogenic bound l <= n-1 - read through the layout's own rule for which subshell sits at which group - forbids 25 of the order ghosts and 0 of the join ghosts. By Theorem 4 it could not have been otherwise: expressed on (n, l, k) that bound is monotone; expressed on (period, group) it is not.

> **Law 7 (forbidding power is a property of the chart).** One bound forbids 25 cells on one coordinatisation of the elements and none on two others. The physics did not change.

> **Note.** AND THE CAUTION IS SHARPER THAN THE LAW. The layout on which the bound has teeth is the one this project WITHDREW as over-representation. A chart that can forbid is not thereby a better chart, and the inference is unsound in both directions. Anyone who builds a table is choosing, with the coordinates, what they will be able to rule out.

### 8.6 UNPLACED separated from OPEN

> **The separator.** A demanded cell is UNPLACED if and only if the index's own source holds a row the chart declined to place which supplies ALL BUT ONE of the coordinates and agrees with the cell on every one of them.

The strength condition is the whole rule. A source row missing one coordinate names a LINE of cells and pins each of them; a row missing two names a PLANE and pins nothing. Without it, four thousand unparsed spectroscopic labels would explain every empty cell in one of these charts. Rows below the strength are counted apart and never used. For 11 of the indexes the source has no gap at all, and that is measured rather than assumed: source rows are counted against rows charted and equality is required.

| index | E | forbidden | unplaced | open | undecided |
|---|---|---|---|---|---|
| gravity | 1550 | 1228 | 0 | 322 | 0 |
| baryons | 1012 | 894 | 8 | 110 | 0 |
| readrezayi | 678 | 0 | 0 | 678 | 0 |
| channels | 367 | 0 | 23 | 344 | 0 |
| ions | 296 | 0 | 0 | 296 | 0 |
| laws | 254 | 0 | 0 | 254 | 0 |
| fibred | 140 | 0 | 0 | 140 | 0 |
| probability | 112 | 0 | 0 | 112 | 0 |
| terms | 98 | 0 | 0 | 0 | 98 |
| fqh | 71 | 0 | 0 | 71 | 0 |
| observed | 56 | 0 | 0 | 56 | 0 |
| fundamental | 46 | 0 | 0 | 46 | 0 |
| inversion | 24 | 0 | 0 | 24 | 0 |
| madrule | 18 | 0 | 0 | 18 | 0 |
| mesons | 15 | 0 | 3 | 12 | 0 |
| nucshell | 14 | 0 | 0 | 14 | 0 |
| nucbands | 5 | 0 | 2 | 3 | 0 |
| deformedbands | 3 | 0 | 0 | 3 | 0 |
| TOTAL | 4759 | 2122 | 36 | 2503 | 98 |

2,122 cells are FORBIDDEN and every one is a baryon cell. 36 are UNPLACED, in four charts, and the count of CELLS is deliberately kept apart from the count of OBJECTS: in one chart 3 cells are pinned by 2 objects, because a state lacking only its parity pins both parities and will fill exactly one. 2,503 are OPEN. 98 are UNDECIDED, and the reason is exact rather than a shrug - the loader of that chart discards a refused row without banking its term key, so the tree cannot ask whether any term lost ALL of its levels, and such a term would pin a cell at precisely the required strength. Banking those keys would settle it.

> **Note.** WHAT THE OPEN COLUMN IS AND IS NOT. For the 8 indexes carrying a derived bound it is FINAL AGAINST EVERY MONOTONE BOUND, by Theorem 4 - a proof and not a survey. For the 9 carrying none it is open against nothing at all, and a bound found tomorrow may empty any of them. The two situations are different and are not summed into one adjective. NEITHER IS A COUNT OF UNDISCOVERED OBJECTS.

## 9. Necessity - each hypothesis dropped until it breaks

A claim is only as strong as what fails without it. Each hypothesis this paper relies on is removed here and the consequence measured.

> **N1 - the observed box.** Drop it: chart on a DECLARED ambient box B containing Box(X). Then R_B(X) intersect Box(X) = <X>, but R_B(X) itself is larger, so the order operator OVER-GENERATES and the channel is a property of the declared range rather than of the data. Necessary and sufficient: R_B(X) = <X> iff R_B(X) subset-of Box(X).

> **N2 - the criterion chi.** Drop it: thirteen filing-system indexes were once seated and the demand exploded. Every disruptive vertex was repository metadata. The finding reported at the time was an artefact of the dropped hypothesis and is withdrawn.

> **N3 - arity in Theorem 2.** Drop the arity-2 restriction: statistics no longer closes for free, and the table in section 6 shows where the freedom ends - at arity 3 it closes 64 of 135 sub-charts and not all.

> **N4 - max-closure in Theorem 4.** Drop it and the theorem is false, which is the point: Gell-Mann-Nishijima is not max-closed and it forbids 894 cells. The theorem's hypothesis is exactly the line between the bounds that adjudicate and the bounds that cannot.

> **N5 - the strength condition in the separator.** Drop it and four thousand unparsed spectroscopic labels, each supplying neither of two coordinates, would mark every empty cell in that chart UNPLACED. The rule would then never report a prediction at all.

> **N6 - totality of a coordinate.** Drop it and C could be charted for the mesons; the chart would then place only the 82 of 250 members that carry one, and the exotics would become forbidden cells of a chart that had silently changed its member set. The refusal in section 8.3 is this hypothesis being paid for.

## 10. Why this is necessary in the fields of study

The first question was how the object is true. This one is why anyone outside this project should want it, and the answer is not the register. THE REGISTER IS AN EXHIBIT; THE THEOREMS ARE THE CONTRIBUTION. What follows is what each result licenses for someone who has never seen this corpus and only has a table of their own.

### 10.1 A classification theorem where a field had only examples

Before Theorem 1 the question 'which closure properties does this table have?' has 32 possible answers and no structure among them. After it there are 8, they are the down-sets of a seven-relation law, and they are ORDERED. A classification is not a convenience: it converts an open-ended question into a finite one, and it makes 'unclassified' a reportable state rather than an absence of effort.

Theorem 1a then does what a classification theorem usually cannot: it exhibits every class IN NATURE. All 8 channels are occupied by charts of real atomic, nuclear or particle data. No class is a formal possibility awaiting an example, so no clause can be added to the law without contradicting a measurement. That is the strongest form the tightness of this bound can take.

### 10.2 A computable invariant that is commensurable across subjects

(K, height, width) is exact rather than estimated - height is Mirsky's minimum antichain cover and width is Dilworth's minimum chain cover, both attained - it is cheap to compute, and IT MEANS THE SAME THING for an electron, a meson and a nuclear excited state. Chemistry, atomic spectroscopy, nuclear structure, particle physics and the quasiparticle hierarchies have never been placed on a common axis, not because no one wished to but because there was no invariant to place them on. 24 indexes across those subjects now sit on one chart and no two share a cell.

Lemma 4.1 bounds the space that chart lives in: |X| <= height x width, so the three coordinates are not independent and the product box overstates. An invariant with a known raggedness is more useful than one without, because the overstatement is quantified rather than ignored.

### 10.3 A no-go result that is applicable BEFORE any data is gathered

This is the most transferable thing in the paper and it costs nothing to use. Two theorems together answer, from the SHAPE of a constraint alone, whether that constraint can ever rule anything out of a table.

> **The a priori test.** Let your table's closure demand a set of cells. (i) By Corollary 3.1, a constraint on a single coordinate will forbid none of them. (ii) By Theorem 4, a constraint of the form x_i <= g(x_j, ...) with g non-decreasing will forbid none of them either. A constraint can adjudicate only if it is antitone somewhere, or carries a congruence.

Neither branch requires the data. A physicist holding a bound and a coordinate list can decide in an afternoon whether the bound has any power over the gaps in their table, and the answer is usually NO. Measured here: 8 bounds derived, every one a genuine theorem of quantum mechanics holding on every member without exception, and 6 of them forbid NOTHING - not because the search failed but because Theorem 4 says it must. The one that bites, Gell-Mann-Nishijima, carries an absolute value and a mod-2 congruence and empties 894 of the 1012 cells the BARYON chart demands - not 894 of the register's whole demand, which no single bound touches.

> **Note.** THE NEGATIVE RESULT IS THE USEFUL ONE. A field that has been hoping its conservation laws constrain the gaps in its tables can now check, cheaply, that most of them cannot. That redirects effort rather than consuming it.

### 10.4 A theory of what an empty cell is

E(X) = |J(X) \ X| is a computable functional on indexes, and the adjudication partitions it into three classes that are provably not interchangeable. FORBIDDEN is a theorem about nature. UNPLACED is a statement about a compilation. OPEN is a prediction. No field currently marks which of the three a gap in its tables is, and the three have entirely different consequences: a forbidden cell closes a question, an unplaced cell is work for the compiler of the source, and only an open cell is a place to look.

The separator is a rule with a proof obligation rather than an editorial judgement - a source row must supply all but one coordinate to pin a cell, because a row missing one names a line and a row missing two names a plane. The register's 4,759 demanded cells adjudicate 2,122 FORBIDDEN, 36 UNPLACED, 2,503 OPEN and 98 UNDECIDED, and the UNDECIDED are undecided for a stated reason with a stated remedy.

THE CONSEQUENCE FOR A DATA COMPILATION IS THAT IT ACQUIRES A BOUNDED PREDICTION COUNT. Not a heuristic estimate of how much is missing, but a number its own closure computes, with the part that is forbidden subtracted by theorem and the part that is the compilation's own fault separated out. A table that can say how many of its gaps are genuinely open is a different kind of object from one that cannot.

### 10.5 Representation dependence, made precise and quantified

Law 7 is a theorem about representation rather than about physics, and it has a number attached. The hydrogenic bound l <= n-1 forbids 25 cells on the period-by-group layout of the elements and 0 on two other coordinatisations of the SAME elements. The physics did not move; the chart did. On (n, l, k) the bound is monotone and Theorem 4 empties it; on (period, group) it is not.

> **Note.** SO CHOOSING COORDINATES IS CHOOSING WHAT YOU CAN RULE OUT, and that choice is usually made for legibility. The layout on which the bound has teeth is the one THIS PROJECT WITHDREW as over-representation, so the inference runs in neither direction: forbidding power is not evidence a chart is right, and a right chart is not obliged to forbid. Any field that has more than one standard way to lay out its objects - and most do - has been making this choice without knowing it was one.

### 10.6 Two indexes adjudicated to the floor, and what that buys

The strongest thing this object does is not catch errors. It is to take a table's own demand and drive it down to a residue that cannot be reduced further BY A STATED ARGUMENT rather than by exhaustion of ideas. Two indexes are carried to that point here, and both were chosen because they were the register's worst cases.

> **GRAVITY: 1,550 demanded, 1,228 FORBIDDEN, 0 UNPLACED, 322 OPEN.** Every nuclide-charge state read as a would-be black hole, on (D, B, F, X, Y, L, E).

It began with NO derived bound at all, so the whole demand sat OPEN against nothing - the largest prediction set in the register held by the index the machinery had least to say about. Two bounds are derivable, and both from the chart's own coordinates.

THE HORIZON BOUND. B is not free: it is a total function of the dimension, the charge, the forced angular momentum and whether the angular momentum vanishes. Two of those are coordinates already - the charge decade rank is zero exactly when the charge is, and F is charted outright. The third is HIDDEN, and this is where Law 5 earns its place: a hidden variable free to range forbids nothing, but the coordinates BOUND this one, since a non-zero spin decade forces the angular momentum non-zero and so does F = 1. The function is ANTITONE IN D - there is an extremality bound on a single rotation at five dimensions and none above it - so Theorem 4 permits it to forbid, and it does.

THE DECADE BOUND, WHICH IS THE ONE WORTH READING. The dimensionless spin and the dimensionless charge are not independent quantities:

```
chi      = Je / alpha_G            alpha_G = G M^2 / (hbar c)
Qtilde^2 = q^2 alpha / alpha_G     alpha   = e^2 / (4 pi eps0 hbar c)

    =>   chi / Qtilde^2  =  Je / (q^2 alpha)
```

THE GRAVITATIONAL COUPLING CANCELS AND THE RATIO IS MASS-FREE. Verified on every member row of the source at zero failures. NONE OF THIS IS NEW PHYSICS and none of it is claimed as such - alpha_G is the standard gravitational coupling and alpha/alpha_G is Dirac's large number - but the join operator does not know it. The join pairs a spin decade with a charge decade freely, and the identity says most of those pairings are unphysical. That is the whole content: a sixty-year-old relation, applied to a question nobody had asked of it, empties cells.

> **Note.** AND A FITTED VERSION OF THE SAME BOUND IS REFUSED. Reading the OBSERVED band of the decade difference off the members, instead of deriving the interval from the hidden ranges, forbids 64 cells more. A band measured on the members and then used to forbid demanded cells is fitting, which section 8.2's gate exists to prevent. The smaller, derived figure is the one reported, and the refusal is recorded in the instrument.

> **BARYONS: 1,012 demanded, 894 FORBIDDEN, 8 UNPLACED, 110 OPEN** - and 110 is a FLOOR with a reason, not a stopping point.

Every open cell carries an ODD doubled spin, as three spin-half quarks require, and every spin-parity pair it uses occurs in a seated member: the residue is not junk the bound failed to reach. What would reduce it further is the SU(6) argument that couples isospin to spin through the symmetry of the three-quark wavefunction - and that binds GROUND states only. This index holds orbitally excited baryons, where the orbital angular momentum is hidden and free, so by Law 5 it forbids nothing here. THE FLOOR IS STATED, NOT REACHED BY GIVING UP.

> **Note.** WHY THIS IS THE ARGUMENT FOR THE OBJECT. A table with a bounded, adjudicated demand can say which of its gaps are closed questions and which are places to look - and can say WHY it cannot say more. Neither of these two residues was reduced by finding better physics; both were reduced by asking, of physics already sixty years old, a question the closure operator had forced into view. That is transferable to any table whose members carry quantum numbers, and it is the whole of what is on offer.

### 10.6a The theorems have also caught errors in published sources

A lesser claim, kept separate because it is evidence that the mathematics bites rather than the argument for it. Each came out of a theorem being applied, not out of proofreading.

- The consistency leg of the Gell-Mann-Nishijima derivation found TWO ROWS of the 2026 Review of Particle Physics whose stated isospin contradicts their own quark content, while two other rows of identical content disagree with them in the same file. The cost to this register was then measured and is zero, and both halves are reported.
- A capture's totality argument found that a published nuclear data table's TITLE understates its own contents: 132 of the levels it tabulates lie above the mass range the title claims, reaching A = 174 against a claimed ceiling of 168.
- The UNPLACED rule found a demanded meson cell whose occupant EXISTS and is absent only because the CAPTURE assigns it no parity - and an audit then showed the capture to be wrong, which is a better demonstration than the one first claimed. The Review of Particle Physics does establish these states; the '?' enters through the intermediate file the capture reads. It refutes itself two lines away: for D(0)*(2300) and D(1)(2420) the NEUTRAL member of the isospin doublet carries a parity while the CHARGED member carries '?', at the same spin and the same isospin, and parity is constant across an isospin multiplet by construction. So the rule did separate a fact about a compilation from a fact about nature - the compilation being the intermediate file rather than the RPP. The original claim, that the source assigns no spin-parity, is WITHDRAWN: section 8.4 flags this exact shape as a fault in the source, and this paragraph had accepted the same shape at face value in the opposite direction.

### 10.7 What the object can carry that it does not carry yet

Stated as capacity rather than as promise, because none of it is done. The machinery is indifferent to subject: anything whose members carry quantum numbers of their own can be seated, measured on the same three coordinates, and adjudicated by the same rule. The gate is chi and nothing else. Three consequences follow immediately for a new table: it acquires a channel and a cell, and can be compared with every index already seated; it acquires an E and therefore a bounded count of what it does not hold; and every bound its field wishes to bring can be tested for adjudicating power by section 10.3 before it is applied. THE REGISTER IS NOT THE OBJECT. The register is 24 exhibits; the object is the classification, the invariant, the two vacuity theorems and the separator, and those do not depend on which tables happen to have been charted here.

### 10.8 What it does not give anyone

It gives no new particle, no new element and no new nuclear level. The OPEN column is not a discovery list - section 8.6 says so in terms and section 14 repeats it. It predicts no measurement, and it replaces no model: a shell model and a quark model do work this object cannot begin to do. What is offered is a way of asking, of a table, questions that at present have nowhere to be asked, and a proof of which of those questions have answers.

## 11. The census - coverage, measured rather than inferred

Every chart-shaped accessor in the research tree was charted, with each module's attempt logged so that coverage is measured. 232 of 232 modules were attempted; 4 could not be imported and each is named with the reason. 44 charts were found over 31 modules, of which 24 are neither seated nor excused - and not one of those is a new first-order index. They are members that are not physical objects, alternate charts of already-seated member sets (all landing in occupied channels), or withdrawn and duplicate charts.

> **Note.** THIS SECTION IS A DATED SNAPSHOT, AND IS THE ONLY ONE IN THE PAPER. The sweep ran at commit 0571a2e on 2026-09-18, when the tree held 232 modules; it holds 255 now. NOTHING IN THE TREE RE-RUNS IT, and that is the defect rather than an aside: a stale number inside an instrument-returned dictionary counts as instrument-produced, so this paper's own substitution guard cannot see these figures go out of date. They are a historical measurement, not a claim about the tree as it stands - and the census's K4 finding has been WITHDRAWN for precisely that reason.

Charts per channel, as of that snapshot: K0 15, K1 1, K2 10, K3 7, K4 0, K5 1, K6 2, K7 8.

> **Note.** AND THE CENSUS'S K4 FINDING IS WITHDRAWN. It recorded that no chart in the tree reached K4. True when it ran, FALSE NOW, and refuted without re-running anything: spin4 is SEATED at K4 and section 3.1's table says so two pages earlier. It is withdrawn in the open rather than quietly corrected, because the failure is the instructive part - a present-tense claim carried forward out of a snapshot, contradicting the paper's own register for as long as it stood.

> **Note.** Two artefacts of the census are recorded rather than allowed to read as findings: one chart appears unseated because the census keys on (module, accessor) and the seated row reaches it under a second accessor name, and one is a helper written during this work that reproduces an existing index's members.

## 12. What was refused, and what that establishes

Five adjudications are reported. Four are refusals and one is a retraction. They are set out because a method that only ever accepts has not been tested.

- A candidate reproducing a published four-figure result of this corpus exactly - 0 join counterexamples and meet counts 2862, 12489, 40887, 110229 at caps 6, 8, 10, 12 - was REFUSED. Its channel is the same at nine of ten boxes we could hand it, so the channel is a property of the defining predicate and not of any data; it would sit where it sits in a universe with no atoms in it.
- A channel was shown reachable at arity 3, where statistics must be earned, by three charts of an index's own measured quantities. All three were REFUSED: they were found by SEARCHING for that channel, which is fitting, and a chart selected because it lands somewhere cannot be evidence that it lands there. (The size of that search was quoted here as a figure; no instrument records it, so it is withdrawn rather than repeated. The ground does not depend on it.)
- Two further coarsenings were REFUSED on the reach ground - one oscillating between channels as the element reach grew, one reaching its channel only at the terminal reach, which is the failure mode that withdrew an earlier chart of this project.
- One coarsening was SEATED and then RETRACTED. The same members under an equally faithful address - and the alternative is the primitive the source actually banks - land in an occupied channel, so the chart had no novel channel and was never a candidate. Its apparent result was a fact about which name had been written down. The ground that caught it became the fourth test in section 7.
- Three readings of 'a bond' were REFUSED on three DIFFERENT grounds, and the molecular hole in this register is real, so the candidate was measured rather than waved off.

11 statements this project had asserted were measured to be false in the course of the same work and are listed with their corrections in the accompanying state file. Among them: a parent index described as a complete rectangle closing everything for free, which has density 0.2099 - 170 cells in a box of 810 - and is not a down-set; an attribution of a closure property to one coordinate when a second restores it equally; and an instrument that DECLARED an index exempt from its own strongest test rather than measuring whether it was. Run properly, that test confirmed the seating and located the physics in a constraint of the hydrogenic spectrum.

## 13. Verification record

Every figure in this paper is read from an instrument at build time and substituted into the prose. A figure that disagreed with its instrument would be impossible rather than unlikely. The generator's own selftest enforces this: no numeral of three digits or more may survive in the prose unless some instrument in the facts dictionary actually produced it, collected recursively from integers AND from numerals inside strings the instruments returned.

- Each instrument is stdlib-only except where sympy or z3 is named, and each carries a selftest whose fixtures are this corpus's own recorded numbers. The selftest is the first thing to run and no report is to be trusted before it passes.
- The ledger guards tie the demand table to the registry in both directions: every seated index is adjudicated, complete, or named too large, and the table invents no index the registry does not seat. An earlier version had neither, so a newly seated index could have gone missing from the demand silently.
- Bounds are verified rather than read off the algebra: each bound's admissible set is enumerated over its index's own product box and closed under join by EXHAUSTION.
- One result in the wider tree is machine-checked with z3 rather than only symbolically, and the check returned unsat on both of its identities - a proof over the reals rather than a sample. What a solver verifies is the algebra and not the physics, and that distinction is kept.

> **Note.** ADVERSARIAL AUDITS OF THIS WORK FOUND REAL DEFECTS AND THEY ARE LISTED BECAUSE THEY WERE FOUND, not because they are flattering. In the captures: a capture attached the wrong nuclide to 35 of 234 entries; a table header was parsed as a nuclear level; and a printed parity that shared a line with the next row's isotope number was dropped at three sites, which moved a seated index's member count and its refusal count, both of which this paper prints. In the checks: two fixtures were tautologies, one passing with three quarters of its capture deleted, and one test read a key its subject does not carry and so was vacuously true. In the prose: a quoted decimal was wrong in its fourth significant digit, and a stated ground for a true claim was false. Every one is fixed and each has a regression fixture. THE TOLERANCE IS THE INSTRUCTIVE ONE: it was a decade too loose to catch that decimal, and tightening it then rejected three CORRECT roundings, so it was wrong in both directions. A TOLERANCE IS ITSELF A COEFFICIENT, and it was replaced by a comparison of significant digits with no free parameter at all.

## 14. What is not claimed

- COMPLETENESS. The registry's completeness flag is false and stays false. This is the set of first-order indexes found and survived their tests, not a claim to have found them all.
- That occupying all eight channels closes the subject. It makes the bound of Theorem 1 tight and nothing more. It does not say the eight are the right coordinates, that no further index exists, or that any channel is held by the best chart of it - and 4 of the eight are held by a SINGLE index each (K1 gravity_bound, K4 spin4, K5 baryon_isomultiplet, K6 madelung_slot), so each of those occupancies rests on one seating.
- That the demand E measures progress. It is reported because it is measured. No index here was built to land on a cell the demand wanted, and one that was would be fitted.
- That the OPEN column is a discovery list. It is the count of demanded cells that no bound derivable here forbids and no source row explains. For the indexes with a derived bound that is final against every MONOTONE bound and nothing else; for the rest it is open against nothing at all.
- That the second-order object is itself a first-order index. Its members are indexes and carry no quantum numbers; it fails chi and is excused by name rather than by silence.
- That any capture is beyond audit. Section 13 lists what an audit of this work found.

## 15. Questions a reader should press, and where they are answered

| question | where |
|---|---|
| Is the box observed or declared, and does it matter? | sections 1 and 9, Lemma N1 |
| Could the criterion be gamed by renaming a label a quantum number? | section 2, Lemma 2.1 - the test is whether two members of one container differ |
| Is Theorem 1's converse proved, or just asserted? | section 3.1 - by exhibition, and now by nature |
| Why three coordinates and not the original five? | section 4.2 - the monotone-redundant-coordinate criterion |
| Is K4's occupancy an artefact of the free statistics bit? | section 6 - its occupant is arity 3, where statistics is earned |
| Does the overlap ruling let a chart in twice under two names? | section 7, the four grounds, one seating retracted by the fourth |
| Is E a prediction count? | sections 8 and 8.6 - it is an upper bound, and the adjudication is the paper |
| Why does almost no bound forbid anything? | section 8.2, Theorem 4 - monotone bounds cannot, and nearly all are monotone |
| Is the 8-channel result sensitive to the choice of five languages? | the companion paper, Clauses A to H; this paper takes the containments as given |
| Has anyone checked this work adversarially? | section 13 - yes, more than once, and what they found is listed there rather than summarised |

## Appendix. Reproduction

Every figure above is read from an instrument at build time. Each is stdlib-only unless sympy or z3 is named, and each carries a selftest whose fixtures are this corpus's own recorded numbers. Every command below is run from `research/warp-drive/`, and the generator is run from that directory too.

- python3 registry.py --selftest -- the criterion, enforced on every row
- python3 figure.py --selftest -- the second-order object and its chart
- python3 overlaprule.py --selftest -- the ruling, the four grounds, the refusals
- python3 overlaprule.py --census -- re-derives the 7 candidates
- python3 boxinvariance.py --selftest -- the refused theorem, and the test run properly
- python3 observed.py --selftest -- the observed fibration against the predicted
- python3 subpop.py --selftest -- the sub-population sweep and the containment structure
- python3 predict.py --selftest -- the demand per seated index
- python3 ghosts.py --selftest -- the seven laws, the bounds, the adjudication
- python3 exact.py --selftest -- the closed forms, with no tolerance
- python3 propagator.py --selftest -- the one z3-checked result
- python3 state.py --check -- the state file against every instrument
- python3 paper/mipaper.py --selftest -- that no figure in this paper is typed

