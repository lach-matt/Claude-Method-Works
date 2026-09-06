### 24.4 The genome — three indices, one lemma, and a zero outside physics

 Serving §24, THE METHOD OUTSIDE SPECTROSCOPY. A fourth domain, entered under the same protocols
 as the three above it, and returning a different verdict from all of them.

 **The genome is the hardest available test of this book's claim, and it is hard in the one way the
 other three domains are not.** Celestial mechanics, the nucleus, string theory and the Calabi–Yau
 catalogue all supply objects whose bounds are physical. The genome supplies an object whose content
 is *contingent* — a particular string, one of 4^N, selected by history rather than forbidden by a
 law. If the claim of Part II is a claim about indexing and not about physics, it must say something
 here, and what it says must not be flattering by construction.

 It says four things. Three are negative. The fourth is the first non-trivial E = 0 this book has
 found outside a physical constraint, and it is not where it was expected.

#### 24.4.1 The coordinate index, and its cost

 The genomic address is (chromosome, position), with 1 ≤ p ≤ L(c). It is the coordinate system of
 every sequence database in use. Computed at GRCh38:

  quantity                                         value
  \|X\|                                            3,088,269,832
  \|ℛ(X)\|                                         5,974,954,128
  **E(X)**                                         **2,886,684,296**
  E/\|X\|                                          0.9347
  join-closure violations, of 576 ordered pairs    512

 **Chromosome 1 is both first in the labelling and longest in the assembly**, so the running maximum
 of §23.3's characterisation is constant, and ℛ(X) is the entire ambient box. Every chromosome length
 must be supplied from outside. This is Chapter 1's thirty-six cells at eighty million times the
 scale, and it is the same defect exactly: **you have to be told where chromosome 21 stops; the
 coordinate system cannot tell you.**

 **The repair is a relabelling, and it is exact.** Sorting chromosomes by length makes L
 non-decreasing, φ monotone, and §2.3's proof goes through unchanged: 0 violations, E = 0. The
 conventional labelling carries twenty inversions, three of them among the autosomes — (10,11),
 (19,20), (21,22).

 **The three is not a structural quantity and was nearly reported as one.** Perturbing the lengths by
 ±10% leaves the index non-closed in 2,000 of 2,000 trials, so *non-closure* is structural. But
 perturbing by ±3% reproduces the specific inversion set in only 269 of 2,000, with the count ranging
 from two to nine. The first stability test measured the wrong claim and the second caught it.
 Register 302.

#### 24.4.2 And ℛ does not repair here — it fabricates

 §P21 records thirty deletions from Λ and thirty repairs: ℛ restores what is removed, exactly, to a
 fixed point at 976. **That property does not transfer, and the reason is precise.**

 Λ's facets *are* two-variable monotone bounds, so ℛ is the identity on them. The genome's bounds are
 empirical and non-monotone, so ℛ replaces each with a running maximum. Computed on a four-element
 toy:

    declared bounds   [10,  7, 13,  4]
    after ℛ           [10, 10, 13, 13]        E = 12

 **The closure returned a closed object describing a different genome, and certified it with E = 0.**
 This is P22's forgery arriving without a forger: nothing was concealed, and the falsehood is in
 plain sight in the bounds — but the operator that produced it is the one this book recommends.

    ℛ repairs an index whose bounds are already monotone and rewrites one whose bounds are not.
    A zero must state the orientation of its axes or it states nothing.

 That is register 275 extended. A zero is worth the size of the box it was computed in **and the
 orientation of the labels it was computed under.**

#### 24.4.3 The lemma

 Three failures in three spaces turned out to be one failure, and it admits a two-line proof.

    **Lemma.** For a function graph X = {(i, vᵢ)}, E(X) = 0 if and only if v is non-decreasing.

 *Proof.* (⇐) If v is non-decreasing, both coordinates rise together, so X is a chain in the product
 order, and a chain is closed. (⇒) If vᵢ > vⱼ for some i < j, then (i,vᵢ) ∨ (j,vⱼ) = (j, vᵢ); X holds
 exactly one cell at coordinate j, namely (j,vⱼ) ≠ (j,vᵢ). So E ≥ 1. ∎

 Checked on 4,000 random vectors: zero monotone cases with E ≠ 0, zero non-monotone cases with E = 0.

 **It is the converse of §2.3, restricted to function graphs, and the book effectively held it
 already.** It was derived before it was recognised. Register 303, and B.2.19.1 — the model was the
 suspect and the model was wrong.

#### 24.4.4 Three failures, triangulated

 B.2.18: three measurements of one object locate a fourth.

  the measurement                          the space           what it found
  chromosome length vs. chromosome number  the assembly        non-monotone; E = 2,886,684,296
  base vs. position                        the sequence        non-monotone; E = 3N
  snarl allele count vs. level             the pangenome       antitone; E > 0, reversible

 Each is a function graph on a conventionally labelled axis. The lemma says E = 0 requires the label
 to be ordered by the value. The fourth point, invisible in any one of them and forced by the three
 together:

    **Genomic labels are assigned by discovery order, by physical position, or by construction
    order. None is assigned by capacity. Closure requires labelling by capacity. Therefore no
    genomic index in use is closed, and every one is closable by a relabelling that destroys the
    label's meaning.**

 This is §13.1 with a measurement attached. An index carries what its coordinates carry; a genomic
 coordinate carries *where to look*, and the closed relabelling carries *how much is there*. The
 fullest closed definition of the genomic index exists, is unique, and is the one nothing can be
 looked up in.

#### 24.4.5 Three prediction budgets, and only one of them closed

 §13.6 says E(X) is the prediction budget. **The genome shows the budget is not fungible**, and
 partitions into three kinds that behave differently:

  budget                    count            per base   the admitted cell is
  coordinate  E(chr,pos)    2,886,684,296    0.935      admitted, **forbidden** — a position past an end
  ignorance   E(N-runs)     150,630,700      0.049      admitted, **unknown** — a coordinate with no base
  contingent  E(pos,base)   9,264,809,496    3.000      admitted, **realisable** — an alternate allele

 The coordinate budget is spent entirely on falsehoods and buys nothing. The contingent budget cannot
 close: E = 0 there requires every human to carry the same genome. **Only the ignorance budget was
 ever a prediction in the usable sense, and it is 1.2% of the total.**

 **It cashed.** The N-runs were cells with coordinates and no content — §11.5's D3, totality catching
 a missing value — and they were settled by measurement rather than by the index. T2T-CHM13 (2022)
 returned a gapless 3.055 Gbp assembly for every chromosome but Y, adding ~200 Mbp and 1,956 gene
 predictions; T2T-Y followed in 2023. E_ignorance → 0. That is Chapter 14's retrieval executed at 150
 million cells, and it is the only prediction a genomic index has made and had confirmed.

 **The contingent budget, measured.** E(pos,base) = 3N, verified numerically at N = 50, 200, 800 with
 E/N = 2.960, 2.965, 2.999, and the only sequences with E = 0 are the monotone ones — which are
 precisely the sequences carrying no information. Against it, gnomAD v4 observes 786,500,648 SNVs:
 **8.49% occupancy**. The description length is N·log₂(E/N + 1) = 6,176,539,664 bits = 772 MB.

    **The genome's information content is its closure defect.** E = N(\|Σ\| − 1) is not a
    measure of what the index is missing. It is a measure of what the index is for.

 And the trade of §13.6.4 inverts. The book says an index may be complete or predictive, not both.
 The genome sits at the far predictive end and pays a price the book does not name: **maximal E is
 maximal prediction budget and minimal predictive power.** An index admitting all four bases at every
 site predicts nothing about any site. Every advance in variant effect prediction works by shrinking
 ℛ — conservation, trinucleotide context, selection coefficients — not by spending E.

#### 24.4.6 The snarl tower, and a non-trivial zero

 The pangenome graph escapes §24.4.1's defect by construction: the snarl decomposition defines
 genetic sites without any single reference coordinate system. It was entered expecting the
 counting bounds of §11.4 form. **Five of six committed predictions were refuted and the sixth
 carried the result.**

 The bound that survives is forced rather than assigned: **two haplotypes differing inside a child
 snarl differ inside its parent**, so A(child) ≤ A(parent). Read by *height* rather than by level,
 A is non-decreasing, and the index closes.

  quantity                                    value
  levels                                      0–28
  occupied cells                              626
  ambient box                                 2,726
  **density**                                 **0.2296**
  **E (height orientation)**                  **0**
  E (level orientation, as labelled)          2,100

 **Density 0.23, not 1.0** — this is not a full product, so register 275's test passes: the zero is
 strong in proportion to a box 4.4 times its size. It is the first non-trivial zero this book has
 found outside a physical constraint.

 **And it does not rest on the numbers.** For any A non-decreasing in height, joins give (max u, max
 a) with max a < A(max u) by monotonicity and meets are symmetric, so the staircase is closed at
 density Σ A(u) / ((D+1)·A_max) < 1 whenever the tower has depth structure at all. The A vector used
 above is synthetic and marked so; the result is **orientation-dependent and data-independent.**

#### 24.4.7 Two defects recorded and not repaired

 **The nesting is not a tree.** Snarls, bibubbles and flubbles in a bidirected graph can overlap
 without strict nesting. Treewidth 1 fails, so the three results §2.2 draws from it do not transfer,
 and the constraint-graph claim is withdrawn. Register 301.

 **The cells are not distinct.** The same genetic difference can reappear at multiple levels of the
 hierarchy. Modelled at 5, 10 and 20% duplication, E is then computed on the wrong set entirely —
 626 reported against 595, 564 and 501 distinct. **This is why audit 9, DISTINCTNESS, must run before
 audit 1, LATTICE**, and in §B.2.17.14's hierarchy it does. The ordering was fixed before this case
 arrived to test it, which is the only reason it holds here.

#### 24.4.8 What this establishes, and what it does not

 **Establishes.** That the law of Part II applies to an object with no physical bounds, and returns a
 verdict rather than a compliment. That E partitions by the modality of the admitted cell, which is a
 distinction §13.6 does not draw. That closure is a property of label orientation, provable in two
 lines and confirmed on 4,000 cases. That a non-trivial zero exists outside physics, on the one
 genomic axis whose bound is forced by argument rather than assigned by convention.

 **Does not establish.** That the snarl index closes on real data — the A vector is synthetic, the
 monotonicity is proved but the density is not measured. That the pangenome E is computable at scale;
 no graph was fetched, and §24.4.6's caps are levels alone. That the three-inversion count means
 anything; it does not. That any of this predicts. **It does not: the genome's one closable index is
 complete, and by §13.6 a complete index predicts nothing.**

 **And the domain statement.** The method enters genomics and returns four measurements, three of
 them negative, one zero, and no prediction. That is the correct outcome for an index whose content
 is contingent, and it is the strongest available evidence that E measures indexing rather than
 physics — because if E were measuring physics it would have had nothing to say here at all.

---

### Register — entries 298 to 303

 **298.** §26 proposed as the slot for this work, and the proposal made without enumerating what
 occupies the sequence. §24 already carries three domains and §25 turns the law on the book. The
 correct slot is §24.4. B.2.19.2 — read the structure at the point of insertion.

 **299.** *Withdrawn:* the conservation law Σ_a c(L,a) = H obstructs closure of the pangenome allele
 index, because §2.2 forbids sums. *Replaced by:* E is invariant under the sum. Computed at 12, 40
 and 400 with the order pattern held fixed: E = 12, 12, 12. §2.2 forbids a sum **as a constraint
 form**, not a set whose members sum to a constant. A reading in B.2.20's sense — a stated criterion
 applied to a case it does not settle.

 **300.** *Withdrawn:* adjoining H as a coordinate repairs the obstruction and yields a weak zero.
 *Replaced by:* a constant axis is inert. E = 12 before and after. With 299 refuted there was nothing
 to repair, and the weak zero never arises.

 **301.** *Withdrawn:* the snarl nesting is a tree, so treewidth 1 holds as in §2.2. *Replaced by:*
 snarls can overlap without strict nesting. Found in the literature, not by computation — which is
 the second time in this work that reading preceded deriving and should have preceded it earlier.

 **302.** A stability test perturbed chromosome lengths at ±10%, found non-closure in 2,000 of 2,000,
 and the three-inversion count was then stated as though that test had covered it. It had not. Re-run
 at ±3%: the inversion set reproduces 269 times in 2,000, count ranging two to nine. Non-closure is
 structural; the count of three is a fact about exact GRCh38 values. B.2.19.6 — the test must be shown
 capable of failing *for the claim it is offered against.*

 **303.** The lemma of §24.4.3 was derived from three instances and only afterwards recognised as the
 converse of §2.3 restricted to function graphs. Search-before-deriving, failing inward against this
 book rather than outward against the literature. B.2.19.1.

### Search before deriving — the ledger for this section

  component                                    precedent                        status
  genetic code as a Boolean lattice B(X)³      Sánchez et al. 2004              derived, then found
  E = 3N as the space of possible variants     arXiv 2509.20702; 8,892,915,237  derived, then found
  snarl / ultrabubble nested decomposition     Paten et al. 2018 (cacti)        found before deriving
  the monotonicity lemma                       §2.3 of this book, converse      derived, then found

 **Three of four were already in print or already in this book.** The protocol was followed on one of
 them. §F.5 is the standing ledger and this is its continuation.

### Provenance

 GRCh38 chromosome lengths are **recalled, not retrieved**; the fetch of Piovesan et al. 2019 Table 2
 returned the article body without the table. This is a stated gap in the B.2.10 sense, with ρ = 1,
 and every structural claim in §24.4.1 was tested for dependence on the exact values. The N-base count
 150,630,700 is from that paper's text, retrieved. gnomAD v4 counts and the T2T assembly figures are
 retrieved. The snarl level bound 0–28 is retrieved; the A vector at §24.4.6 is synthetic and marked.
 No genome, graph or sequence file was fetched or read: the objects are too large for the channel and
 nothing was inferred as though one had been.
