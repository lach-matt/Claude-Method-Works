# The Index of First-Order Indexes

### An admissible chart for indexes of the periodic elements, its eight lawful channels, and what four refusals establish

**Matthew Lach** - Independent Researcher, with a computing collaborator, under the protocols of The Method v1.6

---

**Abstract.** An index of the periodic elements is a finite set of cells whose members carry quantum numbers. Five closure operators -- order, algebra, geometry, information and statistics -- act on such a set, and which of them close it is a property of the set rather than of the operators. We show that only 8 of the 32 subsets of the five can occur, characterise them as the down-sets of a seven-relation law, and use the resulting triple (channel, height, width) as an admissible chart. Charting every index this project seats gives a second-order object of 14 vertices on 14 distinct cells. We prove that 2-determinacy is vacuous at arity 2 and derive from it that an arity-2 chart can never occupy the two lowest channels, which settles why one channel has proved unreachable. We give a ruling admitting overlapping charts when they carry different information, four grounds on which it is tested, and a census over 232 modules establishing that no unseated index exists in the tree. Of five adjudications reported here, four are refusals and one is a retraction of a seating this paper's own method had previously accepted.

---

## 1. The object, and the criterion that bounds it

A first-order index here is a finite set of tuples -- cells -- obtained by charting some body of atomic or nuclear data on a fixed list of coordinates. The subject is the periodic elements, and the criterion is narrow and enforced in code rather than in prose: a member of such an index must carry quantum numbers. An electron, a subshell, a transition, a spectroscopic term, a nuclide-charge state all qualify; a file, a build snapshot or a document does not.

> **Note.** The criterion is a function and not a paragraph, and the reason is historical. When it was a paragraph, thirteen filing-system indexes were seated as vertices -- mirrored files, conversations, archives, handoff documents -- beside indexes whose members are electrons. Every one of the disruptive vertices was repository metadata and not one was an element. The explosion in demand that followed was reported as a finding; it was contamination, and it is withdrawn.

14 indexes satisfy the criterion and are seated.

| index | method | one member is | quantum numbers | cells | cell |
|---|---|---|---|---|---|
| fibred | FIBRATION | 170 electrons, MADELUNG-PREDICTED | n, l, k | 170 | (3, 26, 17) |
| madelung | FIBRATION | the same 170 electrons, MADELUNG-PREDICTED | n+l, l, k | 170 | (7, 30, 12) |
| ions | TABLE | 98 Lambda-8 transitions | charge, electron count | 98 | (0, 18, 16) |
| channels | TABLE | 209 spectroscopic channel shapes | l, Pauli bound, multiplicity | 209 | (0, 16, 24) |
| laws | RESIDUAL | 584 series against Rydberg-Ritz | n range, l, quantum defect | 54 | (0, 25, 7) |
| probability | TABLE | 25 subshells | n, l | 25 | (2, 8, 9) |
| inversion | TABLE | 20 fill-order/shell-order inversions | pairs of (n, l) | 17 | (2, 6, 5) |
| gravity | TABLE | 3,394 nuclide-charge states x 8 dimensions | Z, N, A, q, Ne, 2J, level status | 914 | (0, 19, 112) |
| nucshell | TABLE | 22 nuclear single-particle subshells | nr, l, j (nuclear) | 22 | (3, 7, 6) |
| madrule | RESIDUAL | 20 Madelung exceptions, by their transfer | n+l of the acceptor, l of the donor, occupancy | 13 | (2, 6, 4) |
| terms | TABLE | 5,132 Russell-Saunders terms over 122 spectra | 2S+1, L, parity, the banked J set | 112 | (0, 13, 18) |
| observed | FIBRATION | 108 observed differentiating electrons, register 1306 | n, l, k (observed) | 98 | (0, 20, 13) |
| gravity_bound | TABLE | the same 3,394 nuclide-charge states, on the bound structure alone | horizon-bound class, forced angular momentum, spin-decade rank | 26 | (1, 8, 5) |
| madelung_slot | FIBRATION | the same 170 electrons, subshell-blind | n+l, k | 82 | (6, 26, 6) |

## 2. Five languages and a law

Each of five closure operators takes a finite set of cells to a superset of it. Order and algebra are the sublattice hull under coordinatewise min and max; geometry is hull-completion on coordinate pairs; information is closure under coordinatewise join alone; statistics is 2-determinacy -- the set equals every box point whose two-coordinate projections all occur in it. A language CLOSES an index when applying it returns the index unchanged. The companion paper derives eight clauses relating them; this paper needs only the containments.

| contained | in | source |
|---|---|---|
| order | algebra | Clause B |
| algebra | order | Clause B |
| information | algebra | Clause C |
| information | order | Clause C |
| statistics | algebra | 6d, three-line proof |
| statistics | order | 6d, three-line proof |
| statistics | geometry | Clause G.3 |

### Theorem 1. The lawful channels are the down-sets of that law.

Write cl[L] for the closure of an index X under language L. Every operator is extensive: X is a subset of cl[L] for all L. Suppose (a, b) is one of the seven, so cl[a] is a subset of cl[b], and suppose b closes X, meaning cl[b] = X. Then cl[a] is a subset of X, and by extensivity X is a subset of cl[a]; hence cl[a] = X and a closes X. So the set of languages closing any index is closed downward under the law. Conversely each down-set is realised, by exhibition. Enumerating the down-sets of the seven relations over five languages gives exactly 8 of the 32 subsets.

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

> **Note.** The law leaves exactly two languages free to close alone: information and statistics. Nothing forces either from anything else. That asymmetry is not decoration -- it is what makes K1 and K2 reachable at all, and section 6 shows that the freedom is exercised very differently by the two.

## 3. The admissible chart

An index is charted by the triple (K, h, w): its channel, the length of the longest chain in its cell poset (Mirsky), and the size of the largest antichain (Dilworth). The box is the product of the observed coordinate alphabets, never a declared range. Dilworth's theorem gives |X| <= h * w, so the three are not independent and the product box overstates the space; that inequality was checked on every seated index and holds on all of them (0 violations).

## 4. The index of first-order indexes

Charting each seated index and taking its cell as a member gives a second-order object. It has 14 vertices on 14 distinct cells -- no two seated indexes share a cell -- it closes in nothing, its demand E is 84, and its own cell is (0, 5, 6), which no member occupies.

Applying the chart to itself is a test the object can fail. A coordinate whose distinct values number 90 percent or more of its members separates everything and therefore groups nothing: it is a row identifier wearing a measurement's clothes.

| axis | distinct | of | ratio | verdict |
|---|---|---|---|---|
| K | 6 | 14 | 0.4286 | measurement |
| height | 11 | 14 | 0.7857 | measurement |
| width | 12 | 14 | 0.8571 | measurement |

No axis is a row label. At eleven vertices two of the three were row labels -- height at 0.909 and width perfectly injective at 1.000 -- and the reading filed with that finding was that each index brings its own height and width, so the two approach injectivity by construction as the object grows. That reading is refuted by the table above: the object grew and the labels became measurements. The prediction failed because a COARSENING of a seated index does not bring a new height and width; it lands in the part of the poset its parent already occupies. What the argument really showed is that the defect tracks how the vertex set is built, not how large it is.

## 5. Channel occupancy

The 14 vertices occupy K0, K1, K2, K3, K6, K7. K4, K5 are empty.

## 6. Theorem 2, and why one channel stays empty

Statistics is 2-determinacy: X is the set of box points all of whose 2-coordinate projections occur among X's. At arity 2 there is exactly one 2-subset of the coordinates -- the whole of them -- so the projection is the identity and the reconstruction returns X itself. 2-determinacy therefore holds VACUOUSLY at arity 2, for every set whatever, and statistics closes every arity-2 chart. This is a property of the definition and not of any implementation.

Measured over every sub-chart of every seated index:

| arity | statistics closes | does not |
|---|---|---|
| 2 | 72 | 0 |
| 3 | 41 | 41 |
| 4 | 11 | 60 |
| 5 | 1 | 41 |
| 6 | 0 | 14 |
| 7 | 0 | 2 |

### Corollary. An arity-2 chart cannot occupy K0 or K1.

Its channel contains statistics, and neither K0 nor K1 does. Measured over the same sub-charts, the arity-2 channels observed are K2 (21), K3 (14), K4 (2), K5 (1), K6 (1), K7 (33) -- K0 and K1 occur zero times, as the corollary requires.

> **Note.** This is what makes K4 the hard channel. The law protects K5 and K6 from the free pass, because geometry closing forces statistics and so does the order/algebra block; at those channels the statistics bit is earned by law whatever the arity. K4 = {information, statistics} has neither protection -- nothing forces statistics from information -- so it is the only channel above K1 whose extra content is exactly the bit an arity-2 chart is given. Both charts that have ever reached K4 in this project are arity 2, and a census over 232 modules (section 9) finds no chart of any arity reaching it. That is a sharper statement than a failed search: the only charts that reached it did so at the one arity where half the channel is free.

## 7. Seating an overlapping chart

> They can be seated with overlaps so long as it is not an overlap of same information. An overlap of values in two different languages should tell us two parts of definition contained in that overlapped position. Information is information. But its relative position in this index is information about an object.

A coarsening -- the same members charted on fewer coordinates -- overlaps its parent totally. The ruling above admits it when it is not the same information. Six readings of that phrase were charted against all proper sub-charts of the seated indexes: 'channel differs from its parent' admits 109, 'cell differs from its parent' 254, 'cell no seated vertex holds' 252, and 'CHANNEL no seated vertex holds' admits 6. The third admits 117 coarsenings of a single index; the fourth is bounded, and it is what the ruling says, since the ruling names languages and the channel is the set of languages that close a chart. Text and arithmetic select the same reading.

Four grounds are tested, and a candidate must clear all four:

- NOVEL CHANNEL -- the chart reaches a channel no seated index reaches.
- NOT A RELABELLING -- it has strictly fewer cells than its parent; a chart that separates exactly as much is the parent renamed.
- REACH STABLE -- the channel does not depend on where the construction stopped: no late arrival, no oscillation, and a majority of reaches.
- COORDINATE FORCED -- the channel survives a faithful re-coordinatisation. Two addresses inducing the identical partition of the identical members are one chart written twice.

Of six candidates, 2 seat and 4 are refused.

| chart | channel | cells | verdict / ground failed |
|---|---|---|---|
| gravity (B, F, X) | K1 | 26 | SEATED |
| madelung (n+l, k) | K6 | 82 | SEATED |
| gravity (B, F, X, E) |  |  | refused: reach stable |
| ions (sl, tl) |  |  | refused: reach stable |
| madrule (S_a, l_d) |  |  | refused: reach stable |
| nucshell (l, sigma) |  |  | refused: coordinate forced |

## 8. Two measurements that are about physics

### 8.1 A horizon threshold visible in the closure algebra

One seated coarsening charts nuclide-charge states on (horizon-bound class, forced angular momentum, spin-decade rank), dropping the spacetime dimension. Its bound class comes from the singly-rotating Myers-Perry horizon condition, which has the Kerr bound in four dimensions, a bound in five, and no bound at all from six upward, where the ultraspinning branch opens. Sweeping the dimension ceiling:

| dimensions admitted | channel |
|---|---|
| D <= 5 | K7 |
| D <= 6 | K1 |
| D <= 7 | K1 |
| D <= 8 | K1 |
| D <= 9 | K1 |
| D <= 10 | K1 |
| D <= 11 | K1 |

Read in four and five dimensions the bound structure closes in all five languages. Admit the sixth and four of the five break at once, leaving information alone, and it never moves again. The closure operators are told nothing about dimension; the threshold appears at the dimension the theorem names. The chart is a join-semilattice that is not a lattice -- 0 join counterexamples against 32 meet, in 325 unordered pairs. We record the coincidence and offer no mechanism for why losing a bound should cost four languages rather than three.

### 8.2 What the periodic table predicts against what it does

Two indexes chart the shell fibration: one on the configuration the Madelung rule predicts, one on the configurations a register of this corpus banks as observed. They are seated together by ruling. The predicted chart has 108 cells at the matched reach and closes statistics; the observed has 98 cells at (0, 20, 13) and closes nothing. 25 of the 108 addresses differ and 20 of the configurations do -- and those 20 are exactly the Madelung exceptions this project indexes separately, so the divergence is not an unknown quantity.

The sharpest difference is one neither chart shows alone. 12 elements -- Cr, Cu, Nb, Ru, Pd, Pr, Tb, Pt, Pa, Pu, Bk, Rf -- LOSE occupancy in a subshell as Z increases by one: a filled subshell gives an electron up. The Madelung prediction is monotone in Z by construction and can never do this, verified at every step of the reach. Neither chart supersedes the other.

## 9. The census

Every chart-shaped accessor in the research tree was charted, with each module's attempt logged so that coverage is measured and not inferred. 232 of 232 modules were attempted; 4 could not be imported and each is named with the reason. 44 charts were found over 31 modules, of which 24 are neither seated nor excused -- and not one of those is a new first-order index. They are members that are not elements, alternate charts of already-seated member sets (all landing in occupied channels), or withdrawn and duplicate charts.

Charts per channel: K0 15, K1 1, K2 10, K3 7, K4 0, K5 1, K6 2, K7 8. Nothing in the tree -- 0 of 44 charts over 231 modules.

> **Note.** Two artifacts of the census are recorded rather than allowed to read as findings: one chart appears unseated because the census keys on (module, accessor) and the seated row reaches it under a second accessor name, and one is a helper written during this work that reproduces an existing index's members.

## 10. What was refused, and what that establishes

Five adjudications are reported. Four are refusals and one is a retraction. We set them out because a method that only ever accepts has not been tested.

- A candidate reproducing a published four-figure result of this corpus exactly -- 0 join counterexamples and meet counts 2862, 12489, 40887, 110229 at caps 6, 8, 10, 12 -- was REFUSED. Its channel is the same at nine of ten boxes we could hand it, so the channel is a property of the defining predicate and not of any data; it would sit where it sits in a universe with no atoms in it.
- A channel was shown reachable at arity 3, where statistics must be earned, by three charts of an index's own measured quantities. All three were REFUSED: they were found by searching 120 charts for that channel, which is fitting, and a chart selected because it lands somewhere cannot be evidence that it lands there.
- Two further coarsenings were REFUSED on the reach ground -- one oscillating between channels as the element reach grew, one reaching its channel only at the terminal reach, which is the failure mode that withdrew an earlier chart of this project.
- One coarsening was SEATED and then RETRACTED. The same members under an equally faithful address -- and the alternative is the primitive the source actually banks -- land in an occupied channel, so the chart had no novel channel and was never a candidate. Its apparent result was a fact about which name had been written down. The ground that caught it became the fourth test in section 7.

11 statements this project had asserted were measured to be false in the course of the same work and are listed with their corrections in the accompanying state file. Among them: a parent index described as a complete rectangle closing everything for free, which has density 0.2099 -- 170 cells in a box of 810 -- and is not a down-set; an attribution of a closure property to one coordinate when a second restores it equally; and an instrument that DECLARED an index exempt from its own strongest test rather than measuring whether it was. Run properly, that test confirmed the seating and located the physics in a constraint of the hydrogenic spectrum.

## 11. What is not claimed

- Completeness. The registry's completeness flag is false and stays false. This is the set of first-order indexes found and survived their tests, not a claim to have found them all.
- That an empty channel is impossible. K4, K5 empty. No theorem forbids an index there; for one of them a seating was made and retracted, and for the other the census shows only that nothing in this tree reaches it.
- That the demand E measures progress. It is reported because it is measured. No index here was built to land on a cell the demand wanted, and one that was would be fitted.
- That the second-order object is itself a first-order index. Its members are indexes and carry no quantum numbers; it fails the criterion of section 1 and is excused by name rather than by silence.

## Appendix. Reproduction

Every figure above is read from an instrument at build time. Each instrument is stdlib-only and carries a selftest whose fixtures are this corpus's own recorded numbers; the selftest is the first thing to run and the reports are not to be trusted before it passes.

- python3 registry.py --selftest -- the criterion, enforced on every row
- python3 figure.py --selftest -- the second-order object and its chart
- python3 overlaprule.py --selftest -- the ruling, the four grounds, the refusals
- python3 overlaprule.py --census -- re-derives the six candidates
- python3 boxinvariance.py --selftest -- the refused theorem, and the test run properly
- python3 observed.py --selftest -- the observed fibration against the predicted
- python3 state.py --check -- the state file against every instrument
- python3 paper/mipaper.py --selftest -- that no figure in this paper is typed

