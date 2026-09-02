# THE METHOD 1.6 — MATHEMATICAL COMPENDIUM

Generated from `mathreg.py` on 2026-08-12. **248 objects · 17 roots · 246 settled · 2 unfinished.**

**Verification coverage, stated rather than implied.** `mathverify.py` makes **103 assertions naming 46 of these objects** and recomputes each stated value against the register; **no verifier touches the other 167**. Of the check fields, **85 state a finding, 91 repeat the object's own key, 19 name a function, and 18 are empty** — so a check field present is not a verification performed. `check_audit.py` classifies them on any build. Register 849.

Rebuild with `python3 compendium.py > COMPENDIUM.md`. It reads the register, so it cannot
drift from what the book actually holds.

---

# I · THE CYCLE

The whole of this work is one recursion, stated at §14.5.2:

> **X₍ₙ₊₁₎ = ℛ(X_n ∪ Δ_n)**, halting when **Δ_n ⊆ ℛ(X_n)** — when the increment is already implied.

**It has never halted.** Its falsifier is the ratio of closure to seed:

| | |
|---|---|
| closure — objects the register holds | **248** |
| seed — objects nothing derives | **17** |
| ratio | **14.6 : 1** |

**The seed has not moved across every cycle of this project.** If a genuinely new mathematical
object entered that nothing existing derived, it would move — and that is the test.

## The fourteen roots

| object | statement |
|---|---|
| `A.alph` | Â_i(X) = { x_i : x ∈ X } |
| `A.seaton` | delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l( |
| `B.adm` | r = 2Z²R/(ν³σ) ≥ 5 |
| `B.brk` | T(n) lies between T(n−1) and T(n+1) |
| `B.coll` | an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b} |
| `B.nuV` | ν_V = (3Z²R/5q)^{1/4} |
| `L.c1` | ℓ ≤ n − 1 |
| `L.c2` | k ≤ 2(2ℓ+1) = 4ℓ+2 |
| `L.c3` | q ≤ k |
| `L.c4` | f ≤ e − 1 |
| `L.c5` | g ≤ 4f+2 |
| `L.c6` | g ≤ q |
| `L.c7` | 2S ≤ k |
| `L.c8` | k ≥ 1 (definitional restriction, not a bound) |
| `M.rs` | the vacuum is cyclic and separating for local algebras |
| `P.qdt` | the quantum defect measures how far a Rydberg orbital reaches into the ionic core |
| `P.trunc` | truncation removes most channels and degrades those it leaves |

---

# II · THE OPERATORS

Every derivation in the book runs through these. Nine are this work's own.

| symbol | definition | scope | origin |
|---|---|---|---|
| **∧ ∨** | meet and join — greatest lower and least upper bound | cells | Birkhoff, standard |
| **φ̂** | the envelope: max xᵢ over cells with xⱼ ≤ v | sets of cells | §14.5 |
| **ℛ** | closure at the (≤,≤) corner of Deville's staircase class | sets of cells | §14.5.4 |
| **ℛ₄** | closure over all four orientations | sets of cells | §14.5.5 |
| **E** | E(X) = \|ℛ(X)\| − \|X\| — the defect | indexes | §1 |
| **E₄** | the defect under ℛ₄; E − E₄ is the orientation cost | indexes | §14.5.5 |
| **d** | d(x,y) = τ(lcm/gcd) = ∏(\|Δᵢ\|+1) = \|[x∧y, x∨y]\| | cells | title page |
| **∘** | composition of transitions — Λ₉ is a category | cells | §12.11 |
| **seed** | least G with ℛ(G) = X — **NP-hard** | sets of cells | §14.5.7 |
| **S** | envelope-step count; 2S = the tight-pair count | sets of cells | §14.5.9 |

---

# III · THE LANGUAGES, AND WHY EACH IS NECESSARY

**A language is a coordinate system. Translation is re-coordinatisation. E is the cost.**

Six languages agree on Λ at 976, and **all ten pairs hold** — C(5,2), a complete graph rather than
a ladder. Binary is adjacent to every other, not only to logic. **The agreement is the result; the
list is not.** What follows is one object stated seven ways, with the quantity each language alone
supplies.

| language | its statement of Λ | value | what only it can say |
|---|---|---|---|
| **analysis** | F(1), the enumerator at z = 1 | **976** | the cell count without enumerating |
| **analysis** | F(−1), the alternating sum | **2** | the parity imbalance — invisible to a set |
| **order** | \|ℛ(X)\|, the closure | **976** | what the envelopes admit |
| **order** | E = \|ℛ(X)\| − \|X\| | **0** | **the defect** — no other language states one |
| **geometry** | the void, per interval | **0.464** | what an interval admits and Λ refuses |
| **binary** | the box, one bit per cell | **6,912** | the space before any constraint |
| **binary** | density | **0.1412** | the fraction a constraint set keeps |
| **information** | bits to print the cells | **12,449** | the cost of stating it in full |
| **information** | bits to print the seed | **89** | **139× compression** |
| **statistics** | recovered from pairwise marginals | **976** | the object from its margins alone |
| **statistics** | its defect | **0** | — *and this is its limit* |
| **algebra** | constraints generating the ideal | **8** | derivability — what follows from what |
| **documentary** | *has anyone said this before* | — | **no algorithm exists** |

## Why none is redundant

**Analysis** gives F(−1) = 2. That is an alternating sum over the cells, and **a set has no
alternating sum** — order, geometry and binary cannot express it. It is the parity imbalance, and
it is why Chapter 7 can state the two-column law.

**Order** is the only language that states a DEFECT. E has no counterpart in the others: the
generating function does not know what it fails to enumerate, and a polyhedron does not know which
of its lattice points are absent. **Every result in this work that begins *E =* begins here.**

**Geometry** gives the void — 46.4% of a typical interval is admitted by the box and refused by Λ.
The same quantity read in order is slack and in calculus is V, **and §12.11 shows the three are one
number**. But only geometry states it per interval, which is where the exclusion principle shows.

**Binary** gives the box. **Nothing else in this work says what the space was before a constraint
touched it**, and every density, every defect and every compression ratio is a fraction of it.

**Information** gives the compression: **139 cells printed for every one in the seed.** That number
exists in no other language — order knows the seed is seven, and only description length says what
seven buys.

**Statistics** recovers Λ exactly from its pairwise marginals, and **that is the whole of what it
can do.** Tested on the periodic table it reports **E = 0 where ℛ reports 36** — *marginals cannot
see a hole.* **It agrees with the other languages only where there is nothing to disagree about**,
which makes it necessary for one purpose and useless for another. **Knowing which is the point of
having it.**

**Algebra** gives derivability. Whether a bound follows from the others is a question about an
ideal, and **§14.5.7's anti-exchange failure and register 618's rule-15-backs-rule-5 are both
statements in this language** — one constraint implied by another, which no count can express.

**Documentary** has no closure operator at all. *Has anyone said this before* cannot be bounded by
computation, which is why §29's precedent question can be bounded and never settled, and why two
searches returning nothing is evidence of a kind the other six never have to produce.

    **The test of necessity is not that each language is available. It is that each
    states a quantity the others cannot, and this table is that check run.**

---

# IV · THE OBJECTS, BY FAMILY

## A. The operators — closure, envelope, orientation — 43 objects

### `A.E` — closure defect

**E(X) = |ℛ(X)| − |X|**

*none*

grade **DEFINITIONAL**· source *M §6.1 / T A4; Moore 1910*· depends on `A.R`· 14 objects depend on it· depth 3

> **PRIOR ART: the gap between a set and its closure. That it is worth naming as a DEFECT is the books move; the quantity is the closure minus the set.**

### `A.EW` — the metric defect

**E_W(X) = |W(X)| - |X|: the METRIC defect, what the steps reach and the index has not valued; distinct from E(X) = |R(X)| - |X|, the ORDINAL defect**

*an index whose cells carry values*

grade **DEFINITIONAL**· source *R 1133; Dijkstra 1959*· depends on `A.W`, `A.R`· 1 objects depend on it· depth 5

for Lambda E_W is empty, because a cell of Lambda is an arrangement and carries no number — which is why the book needed only E. For Lambda_spectra the two differ, and the gap between them is the cells that are placed and unvalued

> **PRIOR ART: the reachable set under a step relation, with accumulated cost and a least-cost route, is single-source shortest paths — Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1 (1959) 269-271.**

### `A.R` — the recovery operator

**ℛ(X) = { x ∈ ∏_i Â_i(X) : x_i ≤ φ̂_ij(x_j) ∀ i≠j }**

*none beyond A.alph, A.env*

grade **DEFINITIONAL**· source *M §6.1 / T A3; Moore 1910; Deville et al. 1999*· depends on `A.alph`, `A.env`· 20 objects depend on it· depth 2

> **PRIOR ART: R is a closure operator (Moore 1910) whose constraints are monotone staircases (Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271). Neither the operator form nor the constraint class is new; what is new is reading E as a defect.**

### `A.S` — the step operator

**the STEP operator: for each coordinate direction, the ratio between adjacent VALUED cells, its median and its scatter; a direction earns a step when the scatter is tight enough to carry a value**

*an index whose cells carry values*

grade **MEASURED**· source *R 1132-1137; Edlen 1964*· depends on `A.R`· 1 objects depend on it· depth 3

derived unaided from the spectra index it finds iso at s (1.233, scatter 1.13, 43 pairs), iso at p (1.185, 1.16, 25) and l at s (1.416, 1.43, 62). It must be derived from MEASURED cells ONLY: re-deriving from the walked result tightens iso at s to 1.08 on 116 pairs, because the walked values were generated by that step, and the step count goes 3 to 8

> **PRIOR ART: measuring a step as the ratio between adjacent valued cells is the isoelectronic and isonuclear method of Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### `A.W` — the walk

**the VALUATION closure: every cell reachable from a valued one by steps in S, accumulated error below a threshold, by the least-error route**

*an index, a step set S, and a tolerance*

grade **PROVED**· source *R 1132-1136; Dijkstra 1959*· depends on `A.S`· 2 objects depend on it· depth 4

EXTENSIVE and IDEMPOTENT with exactly zero drift, since the least-error route from the seed leaves nothing tighter to find. MONOTONE except at one cell in 1,345: Mg II ni is measured at +0.0000, the Seaton step is multiplicative, and zero blocks a route a walked positive value would open — so adding a measurement can REMOVE a walked cell

> **PRIOR ART: the valuation closure is a shortest-path closure over a multiplicative cost. Extensivity, idempotence and monotone-except-at-zero follow from Dijkstra (1959).**

### `A.alph` — projection onto coordinate i

**Â_i(X) = { x_i : x ∈ X }**

*X a finite set of integer tuples*

grade **DEFINITIONAL**· source *M §6.1 / T A1; Codd 1970*· 2 objects depend on it· depth 0

> **PRIOR ART: projection onto a coordinate is the relational projection operator — Codd, A relational model of data for large shared data banks, CACM 13 (1970) 377-387.**

### `A.anchor` — the anchor

**REDUNDANCY ANCHORING: keep every route to a cell, not the best one; the spread between independent arrivals MEASURES the error rather than estimating it**

*a valuation closure with more than one route to a cell*

grade **MEASURED**· source *R 1136; Gauss 1809*· depends on `A.W`· depth 5

956 cells of the spectra index are reached by two or more distinct routes. Observed spread 1.05 against a propagated estimate of 1.14 — ratio 0.92, so the walk's error bars are honest and slightly conservative. The check comes from the index disagreeing with itself, not from an outside formula

> **PRIOR ART: keeping every route to an estimate and reading their SPREAD as the error, rather than taking the best route, is the method of combining independent determinations — Gauss, Theoria motus corporum coelestium (1809), sec. 3.**

### `A.blind` — the three blindnesses

**each language is blind in its own way: statistics cannot state a closure defect, analysis cannot state an ordering, a multiplicative algebra cannot state an exception**

*an index described in more than one language*

grade **MEASURED**· source *R 1169; Shannon 1948; Freuder 1978*· depends on `Q.bridge`· depth 13

register 761 established the first. The second: least squares minimises squared error and has no rank in it — an equation fitting 311 values to R^2 = 0.924 got every ordering wrong. The third: a product of positive factors is monotone in each, so a multiplicative fit returns 205/205 where the data has eleven genuine exceptions

> **PRIOR ART: that a representation cannot state what its own coordinates cannot distinguish is the general fact behind all three blindnesses. Statistics sees marginals only (Shannon 1948 for what a marginal carries); analysis has no order in it; a multiplicative algebra is monotone in each factor by construction. Register 1170 measures them.**

### `A.bound` — the defect bounds

**0 ≤ E(X) ≤ |box| − |X|**

*box = ∏_i |Â_i(X)|*

grade **PROVED**· source *T audit 27; Moore 1910*· depends on `A.E`, `A.ext`· depth 4

> **PRIOR ART: the bounds are extensivity below and the ambient product above; both follow from the closure axioms.**

### `A.bpc` — binary path consistency / 2-decomposability (Kimura et al. 2024)

**X ⊆ BPC(X) ⊆ ℛ(X), BPC(X) = { x : (x_i,x_j) ∈ proj_ij(X) ∀ i<j }**

*none*

grade **PROVED**· source *T A5; Cooper 1989; Janssen et al. 1989*· depends on `A.R`· 1 objects depend on it· depth 3

> **PRIOR ART: binary path consistency and its relation to global consistency — Cooper, An optimal k-consistency algorithm, Artif. Intell. 41 (1989) 89-95; Janssen, Jegou, Nouguier & Vilarem, A filtering process for general constraint-satisfaction problems, IEEE (1989), which gives a polynomial algorithm for pairwise consistency.**

### `A.cert` — the certificate condition

**an open index does not close itself except where a CERTIFICATE exhibits an operation on its coordinate system reaching a fixed point of R**

*the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate*

grade **PROVED**· source *M §18.4.1, promoted; Tarski 1955*· depends on `A.clos`, `A.modeA`, `A.modeB`· 1 objects depend on it· depth 8

> **PRIOR ART: a closure operator does not close an open set without an added operation; exhibiting one is the fixed-point construction of Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309.**

### `A.clos` — closure operator (Moore family)

**ℛ is extensive, monotone, idempotent; the closed sets form a Moore family**

*none*

grade **PROVED**· source *M §14.2 / T 1.3; Moore 1910; Ward 1942*· depends on `A.ext`· 2 objects depend on it· depth 4

> **PRIOR ART: an extensive, monotone, idempotent operator is a CLOSURE OPERATOR and its fixed sets form a Moore family — E. H. Moore, Introduction to a Form of General Analysis (1910); M. Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. R is one; nothing about R is needed to know its fixed sets are closed under intersection.**

### `A.dechter` — Dechter 1992

**strong (w*+1)-consistency on induced width w* gives decomposability**

*induced width w**

grade **CITED**· source *Dechter 1992*· depends on `A.gc`· depth 5

A.dechter

### `A.define` — the defining letter

**a rung-1 coordinate contributes no envelope: same cells, box, E, envelope-step count and seed with or without it — it is invisible to ℛ and still counts as a letter**

*it is the index's own name carried as a coordinate, taking one value because the object is what does not vary in it*

grade **PROVED**· source *M §21.6.1; Birkhoff 1937*· depends on `A.env`· depth 2

> **PRIOR ART: a coordinate with a single value contributes no join-irreducible, so it changes neither the lattice nor its envelopes.**

### `A.dens` — density and informativeness

**E = 0 is informative at any density; E > 0 at low density measures sparsity**

*density = |X| / |box|*

grade **COMPUTED**· source *T 1.9; Erdos & Renyi 1960*· depends on `A.E`· 1 objects depend on it· depth 4

> **PRIOR ART: that a structural property can hold at any density, while its failure measures sparsity, is the random-graph threshold picture of Erdos & Renyi, On the evolution of random graphs, Publ. Math. Inst. Hung. Acad. Sci. 5 (1960) 17-61.**

### `A.derived` — adjunction never repairs (M Thm 10.1)

**a derived coordinate cannot repair closure: the box grows by its value count and |X| is fixed**

*the coordinate is a function of the others*

grade **PROVED**· source *T 1.7 / M §17.2 Thm 10.1; Birkhoff 1940*· depends on `A.E`· 1 objects depend on it· depth 4

> **PRIOR ART: a derived coordinate is a function of the others, so it adds no join-irreducibles and cannot enlarge the closed family; it only enlarges the ambient box.**

### `A.ebits` — description length

**E_bits(X) = log₂ C(|ℛ(X)|, E(X))**

*counting measure*

grade **COMPUTED**· source *M §25.3; Shannon 1948; Rissanen 1978*· depends on `A.E`· 1 objects depend on it· depth 4

> **PRIOR ART: description length as a measure of structure — Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (1948); Rissanen, Modeling by shortest data description, Automatica 14 (1978) 465-471. log2 C(|R|, E) is the cost of naming which admitted cells are absent.**

### `A.env` — monotone upper envelope / staircase bound

**φ̂_ij(v) = max{ x_i : x ∈ X, x_j ≤ v }; max ∅ = −∞**

*i ≠ j*

grade **DEFINITIONAL**· source *M §6.1 / T A2; Deville et al. 1999*· depends on `A.alph`· 7 objects depend on it· depth 1

> **PRIOR ART: the monotone upper envelope of a relation is its staircase bound — the connected row-convex class of Deville, Barette & Van Hentenryck (1999) and the row-convex networks of van Beek & Dechter, J. ACM 42 (1995) 543-561.**

### `A.erel` — E is coordinate-relative

**E = 0 is relative to coordinates: any X with |X| = a·b relabels onto an a × b rectangle, which is a full box and closed — so every index with a composite cell count has a coordinate system in which E = 0**

*the coordinates must be fixed by the subject, not chosen; every coordinate in this book is*

grade **PROVED**· source *M §21.6; Birkhoff 1940; Birkhoff 1937; Dushnik & Miller 1941*· depends on `A.R`· depth 3

> **PRIOR ART: E = 0 is a statement about a COORDINATISATION, not a set. Any set of size ab relabels onto an a x b grid, which is closed. This is the standard observation that lattice properties are not invariants of the underlying set.  PRIOR ART: a lattice property belongs to a COORDINATISATION and not to the underlying set — the same reason order dimension is not an invariant of cardinality. Birkhoff (1937); Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610.**

### `A.expr` — the expression always exists

**a closed index equals the set its own envelopes admit, so its expression always exists and is recoverable**

*X = R(X)*

grade **PROVED**· source *M §15.2 corollary / §2.23; Moore 1910*· depends on `A.R`, `S.bounds`· depth 4

> **PRIOR ART: a closed set equals the fixed point of its own closure operator, so its defining expression always exists. Immediate from idempotence.**

### `A.ext` — extensivity

**X ⊆ ℛ(X), hence E(X) ≥ 0**

*none*

grade **PROVED**· source *T 1.2 / M A.2; Moore 1910*· depends on `A.R`· 2 objects depend on it· depth 3

> **PRIOR ART: extensivity is the first Moore axiom. That E(X) >= 0 is its immediate corollary, not a separate result.**

### `A.fix` — Bergman double-projection; Baker–Pixley 1975 (majority term)

**X is closed ⟺ X = ℛ(X)**

*each coordinate presented as a chain*

grade **PROVED**· source *M §14.1 (Thm 9.1, A.2); Moore 1910; Baker & Pixley 1975*· depends on `A.clos`· 1 objects depend on it· depth 5

> **PRIOR ART: X closed iff X = R(X) is the definition of a fixed point of a closure operator. That the binary projections suffice is Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174 — the majority-term / (2,d) interpolation theorem.**

### `A.freuder` — Freuder 1982

**a tree-structured constraint network is globally consistent after arc consistency**

*constraint graph acyclic*

grade **CITED**· source *T 1.10; Freuder 1982*· depends on `A.gc`· depth 5

> **PRIOR ART: Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32 — a tree-structured constraint network is globally consistent after arc consistency. This is the reason Lambda closes, and it is his.**

### `A.gc` — global consistency (CSP)

**E(X) = 0 ⟺ the binary constraint network is globally consistent**

*the constraints are the monotone binary projections*

grade **CITED**· source *T 1.4 / A5c; Freuder 1978; Dechter 1992*· depends on `A.bpc`, `A.E`· 3 objects depend on it· depth 4

A.gc

> **PRIOR ART: global consistency and its k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966; Dechter, From local to global consistency, Artif. Intell. 55 (1992) 87-107.**

### `A.intext` — interior and exterior

**E is INTERIOR and E_W is EXTERIOR: the order operator is bounded by its sample and the step operator is not**

*an index with valued cells and a step set*

grade **MEASURED**· source *R 1196-1199; Beeri, Fagin, Maier & Yannakakis 1983; Dijkstra 1959*· depends on `A.E`, `A.EW`· 1 objects depend on it· depth 6

on Lambda_spectra in-region, R places 1,925 from 277 held (E = 1,648) and W values 277 (E_W = 0) at the book's tolerance, because every step's scatter exceeds it — multiplicity 1.664, isoelectronic 1.674, l 2.872. Raising tau does not close the gap: every cell W gains, R mostly refuses, and ALL 218 fail one envelope, charge given Z. The measured set runs Z 2-83 and charge 1-9; the refused cells run Z 1-85 and charge 1-10. The overlap never exceeds 12% of E at any tolerance

> **PRIOR ART: the order operator is a closure bounded by its sample (BFMY 1983 for what local closure can reach); the step operator is a reachability closure unbounded by it (Dijkstra 1959). That E is interior and E_W exterior follows from the two being different kinds of operator.**

### `A.logic` — the logic level

**LOGIC is not a language: it is the mechanism binary -> language -> binary by which any language answers a question about a cell**

*a language with a closure operator*

grade **DEFINITIONAL**· source *R 1173; Boole 1854; Tarski 1936*· depends on `A.R`· 1 objects depend on it· depth 3

three levels: BINARY is the type, a cell is admitted or not; a LANGUAGE is a coordinate system with a closure operator; LOGIC is the map. A language earns a row when logic can operate on it and return a binary, which is why documentary has none — it returns a citation. The book's C(5,2) = 10 combinations is then exact: five operator-bearing languages, plus statistics as a sixth and documentary as a seventh

> **PRIOR ART: that logic is the mechanism by which a language answers a binary question, rather than a language itself, is the object-language/metalanguage distinction — Boole, An Investigation of the Laws of Thought (1854); Tarski, Der Wahrheitsbegriff in den formalisierten Sprachen, Studia Philos. 1 (1936) 261-405.**

### `A.modeA` — failure mode A — ordering

**sub-case A, ORDERING: the term is present and determined but non-monotone; repairable by re-ordering**

*the term is a function of an existing coordinate*

grade **COMPUTED**· source *T 1.6; Freuder 1978*· depends on `A.rule`· 1 objects depend on it· depth 7

> **PRIOR ART: a non-monotone constraint is not captured by an envelope, and higher consistency is needed — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### `A.modeB` — failure mode B — arity

**sub-case B, ARITY: every term is monotone; the constraint names more coordinates than an envelope has arguments; not repairable by any operation on coordinates**

*the minimal failing support has size ≥ 3*

grade **COMPUTED**· source *T 1.6; Freuder 1978*· depends on `A.rule`· 2 objects depend on it· depth 7

> **PRIOR ART: a constraint naming more coordinates than the envelope pairs is a higher-arity constraint; the k-consistency ladder is Freuder (1978).**

### `A.montanari` — Montanari 1974

**for monotone constraints, path consistency implies global consistency**

*constraints monotone*

grade **CITED**· source *T 1.10; Montanari 1974*· depends on `A.gc`· depth 5

> **PRIOR ART: Montanari, Networks of constraints: fundamental properties and applications to picture processing, Inf. Sci. 7 (1974) 95-132 — for monotone constraints, path consistency implies global consistency. Lambda constraints are monotone, so this applies directly.**

### `A.morph` — the cap as a morphism

**an occupancy coordinate's cap is admissible iff it is a morphism for the operation preserved**

*meet-morphism preserves meets; join-morphism preserves joins*

grade **COMPUTED**· source *M §18.4.1; Birkhoff 1940*· depends on `A.rule`· depth 7

> **PRIOR ART: a cap is admissible iff it is a lattice morphism for the operation — the standard homomorphism condition. Birkhoff, Lattice Theory (1940).**

### `A.orient` — orientation cost

**E − E₄, the ORIENTATION COST: 0 on eight of ten indexed objects, 2 on the audits, 750 on the parity rule**

*ℛ₄ defined*

grade **COMPUTED**· source *M §14.5.5; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999*· depends on `A.r4`· depth 4

> **PRIOR ART: the cost of choosing one orientation over the full class. The class is Devilles; the cost is measured here.  PRIOR ART: the four orientations of a staircase are the (alpha, beta)-monotone constraints of Deville, Barette & Van Hentenryck (1999). R uses one corner and R_4 the closure over all four; the ORIENTATION COST is the difference, measured at 0 on eight of ten indexed objects and 2 on the aufbau index.**

### `A.prod` — the product rule for closure

**if no constraint links the factors, ℛ(A×B) = ℛ(A)×ℛ(B)**

*A, B on disjoint coordinate sets, no cross constraint*

grade **PROVED**· source *T D9; Birkhoff 1940*· depends on `A.R`· 1 objects depend on it· depth 3

> **PRIOR ART: a closure operator on a product with no cross-constraints factorises; the statement is the product form of a Moore family. Birkhoff, Lattice Theory (1940).**

### `A.prodE` — the product rule for the defect

**E(A×B) = |A|·E_B + |B|·E_A + E_A·E_B**

*as A.prod*

grade **PROVED**· source *T D10; classical; classical; Euler 1748*· depends on `A.prod`, `A.E`· depth 4

> **PRIOR ART: the defect of a product expands as |A|E_B + |B|E_A + E_A E_B — the inclusion-exclusion expansion of (|A|+E_A)(|B|+E_B) minus |A||B|. Elementary.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. Elementary algebra; the point is that defects MULTIPLY as well as add across a product.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. The point is that defects MULTIPLY as well as add across a product, which is the elementary product rule for counting — Euler, Introductio in analysin infinitorum (1748), ch. XVI.**

### `A.r4` — the four-orientation operator

**ℛ₄, the four-orientation closure over Deville's staircase class**

*idempotent, hence a closure operator*

grade **COMPUTED**· source *M §14.5.5; Deville et al. 1999*· depends on `A.stair`, `A.R`· 2 objects depend on it· depth 3

> **PRIOR ART: the four orientations of a staircase constraint are the (alpha, beta)-monotone class of Deville, Barette & Van Hentenryck (1999); R uses one corner and R_4 the closure over all four.**

### `A.relax` — ℛ as a relaxation

**ℛ is not a k-wise closure for any k: k-wise defect is 0 at k = d while E(ℛ) can be 750**

*|Δℓ|=1 at 750 against k-wise 0 for k = 2,3,4*

grade **PROVED**· source *M §14.5.4; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.R`· 1 objects depend on it· depth 3

> **PRIOR ART: pairwise (k-wise) consistency implies global consistency exactly for ACYCLIC hypergraphs — BFMY, On the desirability of acyclic database schemes, J. ACM 30 (1983) 479-513. R is the global operator and the k-wise closures are the local ones; the gap between them is their theorem, and this object measures it.**

### `A.rule` — the tightening rule

**a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other**

*the index is a sublattice of a product of chains*

grade **COMPUTED**· source *T 1.8 / M §14.4; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995*· depends on `A.fix`· 10 objects depend on it· depth 6

> **PRIOR ART: a tightening preserves closure iff it stays inside the monotone staircase class.  PRIOR ART: a tightening preserves closure exactly when it stays inside the monotone staircase class — the connected row-convex constraints of Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271, and the row-convex networks of van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561. Binding one coordinate by a monotone function of one other is precisely a member of that class.**

### `A.seaton` — the polarisation formula

**delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l(l+1) alpha/K**

*a Rydberg electron that does not enter the core*

grade **CITED**· source *Seaton 1958; Drake & Swainson 1991*· 1 objects depend on it· depth 0

tested on 23 adjacent-l pairs in its domain: median observed/predicted 1.12, improved from 1.19 by restoring the n-dependent term, which confirms the term belongs. It fails on 20 near-hydrogenic pairs at the noise floor and on Ba II (delta_f = 0.756) and Hg II (1.062), where the 4f orbital has collapsed into the core and the series penetrates

### `A.slack` — slack

**SLACK(S) = measure(ambient)/measure(S); log SLACK = log|ℛ(X)| − log|X|**

*a measure on the ambient*

grade **COMPUTED**· source *M §25.2; Shannon 1948*· depends on `A.E`, `A.ebits`· 1 objects depend on it· depth 5

> **PRIOR ART: log of the ratio of ambient to actual is a bit count — the same quantity as A.ebits in another form. Shannon (1948).**

### `A.stair` — staircase / connected row-convex

**phi-hat recovers a STAIRCASE constraint: (alpha,beta)-monotone with alpha,beta in {<=,>=}**

*binary*

grade **CITED**· source *Deville, Barták, Van Hentenryck 1999*· depends on `A.env`· 2 objects depend on it· depth 2

A.stair

### `A.staircls` — the one-corner characterisation

**E(ℛ) = 0 iff X is an intersection of (≤,≤) staircases — one corner of Deville's class**

*the anti-diagonal is a staircase with E = 750*

grade **PROVED**· source *M §14.5.4; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995*· depends on `A.relax`, `A.stair`· depth 4

> **PRIOR ART: connected row-convex and monotone staircase constraint classes — Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271; van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561.**

### `A.stat2` — the statistics operator

**the statistics operator is max-entropy on the PAIRWISE marginals, not the first-order ones**

*an index of dimension d >= 3*

grade **MEASURED**· source *R 1174*· depends on `A.logic`· 1 objects depend on it· depth 4

on Lambda, first-order marginals admit all 6,912 ambient cells; pairwise marginals admit exactly 976 and reproduce R cell for cell. IPF converges to the max-entropy distribution matching the SPECIFIED marginals (Deming and Stephan 1940; Ireland and Kullback 1968), so which marginals is the whole question

### `A.three` — the three populations

**the Method equation partitions an index into three populations: interior captures, the working overlap, and exterior predictions**

*an index, its order operator and its step set*

grade **MEASURED**· source *R 1199-1200; Freuder 1978; Dijkstra 1959*· depends on `A.intext`· depth 7

at tau = 3.0: INTERIOR 1,503 cells R places and no step values, median l = 2 and charge 4 — these are captures. BOTH 145 placed and valued, median l = 3, the polarisation regime. EXTERIOR 218 the steps reach past the sample edge. The exterior verifies where it reaches: Cs I np walked to 3.659 against a measured 3.5667, an error of 2.6% with a stated error factor of 1.67

> **PRIOR ART: partitioning by what a closure admits and what a propagation reaches — the k-consistency gap (Freuder 1978) crossed with shortest-path reachability (Dijkstra 1959). The three populations are the measurement.**

### `A.two` — the binary-projection criterion

**a tightening preserves E = 0 iff each binary projection is the intersection of that projection's own two upper envelopes**

*phi-hat indexed over ORDERED pairs*

grade **PROVED**· source *M §14.4 / §2.15.2; Baker & Pixley 1975*· depends on `A.rule`· depth 7

> **PRIOR ART: that binary projections decide membership is the (2,d) interpolation property — Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174.**

## S. The seed — generation, covering, structure — 18 objects

### `S.bits` — the seed as binary

**the five read as binary: corners 1 and 2 are exact complements (3 of 3), corner 3 and the unit cell are exact complements (3 of 3), corner 4 is fully specified at 11001100, and every coordinate receives both a 0 and a 1 with no column one-sided**

*measured at one cap setting only; whether the pairing survives other caps is untested*

grade **COMPUTED**· source *M §14.5.14; Shannon 1938*· depends on `S.unit`· depth 9

> **PRIOR ART: reading a structure as binary words with complementation is Boolean algebra — Shannon, Trans. AIEE 57 (1938) 713-723.**

### `S.bounds` — the bounds are recoverable

**S3: the bounds are recoverable from the cells**

*closure*

grade **PROVED**· source *M §15.2; Moore 1910*· depends on `A.R`· 1 objects depend on it· depth 3

> **PRIOR ART: if the envelopes are recoverable from the cells then the constraints are too, since R is determined by its envelopes.**

### `S.box` — the box seed law, d + c − 2

**a full box c^d seeds at d + c − 2**

*exact by branch and bound at 3³ and 4³*

grade **PROVED**· source *M §14.5.9; classical; Dilworth 1950; Dilworth 1950; Birkhoff 1937*· depends on `S.cover`· depth 5

> **PRIOR ART: the corners of a d-dimensional box over c values generate it under coordinatewise max, and d + c - 2 is the count of extreme steps. Elementary.  PRIOR ART: as S.down, for a full box: the extreme steps in each coordinate generate it.  PRIOR ART: the generators of a down-set closed under coordinatewise max are its maximal elements; for a box over c values in d coordinates that count is d + c - 2. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166; Birkhoff (1937) for the representation.**

### `S.car` — the Carathéodory lower bound

**seed ≥ the Carathéodory number = the breadth = d for a product of d chains**

*semilattice with subsemilattices as convex sets*

grade **CITED**· source *Carathéodory / convexity spaces; Caratheodory 1911; Caratheodory 1911*· depends on `S.cover`· depth 5

> **PRIOR ART: Caratheodory, Ueber den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.  PRIOR ART: Caratheodory, Ueber den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.**

### `S.channel` — the channel conditions

**six channel conditions hold in all 219 minimum covers of Lambda-8: an s-s, s-p, p-s and p-p transition, a null transition q = 0, and a full transfer q = k**

*the constraint is on the CHANNEL, not the cell — which is why every cover looks alike while nothing is forced*

grade **COMPUTED**· source *M §14.5.12; Condon & Shortley 1935*· depends on `S.core`· 1 objects depend on it· depth 7

> **PRIOR ART: the s-s, s-p and related conditions are statements about which subshell transitions the seed must contain; the subshell structure is Condon & Shortley (1935).**

### `S.core` — the seed's necessary core

**four of the seed's seven cells are NECESSARY: each uniquely covers 12-23 envelope elements and has ZERO alternatives in Lambda; they cover 87 of 102**

*a stable attractor of greedy covering, not necessity; §14.5.7 stands unamended (register 600)*

grade **COMPUTED**· source *M §14.5.10; Karp 1972; Chvatal 1979*· depends on `S.lam`· 2 objects depend on it· depth 6

> **PRIOR ART: an element covered by exactly one set forces that set into every cover — the standard reduction rule for set cover.  PRIOR ART: an element covered by exactly one set forces that set into every cover — the ESSENTIAL-SET reduction rule of set-cover preprocessing. Chvatal, A greedy heuristic for the set-covering problem, Math. Oper. Res. 4 (1979) 233-235; Karp (1972) for the problem, Lovasz, On the ratio of optimal integral and fractional covers, Discrete Math. 13 (1975) 383-390 for the LP bound. Four of the seven seed cells are forced this way, and that is the measurement.**

### `S.cover` — the seed is a set cover

**the minimum seed is a MINIMUM SET COVER: elements the envelope steps, sets the cells**

*S.seed*

grade **PROVED**· source *M §14.5.9; Karp 1972; Johnson 1974*· depends on `S.seed`· 5 objects depend on it· depth 4

> **PRIOR ART: MINIMUM SET COVER is one of the 21 NP-complete problems of Karp, Reducibility among combinatorial problems (1972); the greedy ln n approximation is Johnson, Approximation algorithms for combinatorial problems, JCSS 9 (1974) 256-278. The seed problem IS set cover, which is why five heuristics agree on 7 and the lower bound is 5.**

### `S.down` — the down-set seed law, d + c − 1

**a down-set over c values in d coordinates seeds at d + c − 1**

*exact: LB = UB at d=4 c=4*

grade **PROVED**· source *M §14.5.9; Dilworth 1950*· depends on `S.cover`· depth 5

> **PRIOR ART: the minimum generating set of a down-set is its set of maximal elements; the d + c - 1 count follows. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166.**

### `S.erasure` — the seed is an erasure structure

**the remaining three seed positions admit 519 completing triples over 66 distinct cells, none in all 519, each appearing in 3 to 157 — a redundancy gradient of fifty to one**

*heavy-tailed: min 3, median 12, max 157, a ratio of thirteen to one*

grade **COMPUTED**· source *M §14.5.11; Karp 1972*· depends on `S.core`· depth 7

> **PRIOR ART: the alternative completions of a partial cover; the count is the measurement.**

### `S.ground` — the ground-state derivation

**the ground configuration determines every channel's existence and bounds its defect's integer part**

*an atom of atomic number Z*

grade **MEASURED**· source *R 1139-1141; Madelung 1936; Janet 1929; Janet 1929; Madelung 1936; Hund 1925*· depends on `K.produce`· 5 objects depend on it· depth 6

multiplicity from Hund on the core: 24 of 24 electron counts, exact containment. The cell set from aufbau: 8,488 cells admitting all 311 measured channels where the sampled index admits 296. And floor(delta) <= min(p, n0-l-1) for 311 of 311, exact 57%, within two 97%

> **PRIOR ART: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929); Madelung's rule as usually stated (1936). Hund's first rule (Z. Phys. 33, 1925) gives the term. Both are read, not derived.  PRIOR ART: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929), and Madelung rule as usually stated (1936). The term follows from Hund first rule, Z. Phys. 33 (1925) 345-371. Both are read, not derived.**

### `S.lam` — Λ's seed — seven cells

**seed(Λ₈) = 7 exactly — 976 cells from seven, 139 to 1; LB 5, five heuristics 12/7/7/7/40**

*branch and bound over 102 elements*

grade **COMPUTED**· source *M §14.5.9 / twoheur.py; Karp 1972; Johnson 1974*· depends on `S.cover`· 1 objects depend on it· depth 5

> **PRIOR ART: the seed problem is minimum set cover, NP-complete (Karp 1972), with a greedy ln n approximation (Johnson 1974). Five heuristics agreeing on 7 against a lower bound of 5 is the measurement.**

### `S.open` — the open-index form, seed + E

**an open index is recovered as seed(ℛ(X)) plus the E cells ℛ(X) holds and X does not; cost seed + E**

*exact on four open indexes; compresses only where E ≪ |X|*

grade **PROVED**· source *M §21.5; Moore 1910*· depends on `S.seed`· 1 objects depend on it· depth 4

> **PRIOR ART: an open index needs its closure seed plus the cells the closure adds and it does not hold — the decomposition follows from extensivity.**

### `S.parent` — the parent-term wall

**an OPEN-SHELL core gives many parent terms and no separable Rydberg series, so its levels can be published and its defect cannot be extracted**

*an ion whose core has an open subshell*

grade **MEASURED**· source *R 1180; Condon & Shortley 1935; Condon & Shortley 1935; Racah 1943*· depends on `S.ground`· 1 objects depend on it· depth 7

Fe IV's 3d4 core carries sixteen LS terms. The capture shows 13 of them, 24 distinct (parent, l, term) series, and EVERY ONE has exactly one member — n = 4 only. Fe IV has ~1,000 analysed levels and no extractable defect. The compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6, which is not a collection preference but the fact that an open-shell core does not produce the object a quantum-defect index holds

> **PRIOR ART: parent terms and the fractional-parentage decomposition are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah's coefficients of fractional parentage (1943). That an open-shell core gives one series per parent is their structure; the measurement is that Fe IV's 24 series each hold one member.  PRIOR ART: parent terms and coefficients of fractional parentage are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382. That an open-shell core gives one series per parent is their structure; the measurement is that the 24 Fe IV series each hold one member.**

### `S.regime` — the regime coordinate

**the SIGN of d2 is a coordinate the ground state cannot supply, and the MAGNITUDE of d2 predicts the channel's own scatter**

*a Rydberg channel with a fitted Ritz curve*

grade **MEASURED**· source *R 1157-1162; NIST Atomic Spectroscopy compendium; NIST Atomic Spectroscopy compendium; Ritz 1903*· depends on `S.ritz`· 2 objects depend on it· depth 8

Seaton requires d2 < 0 for polarisation, so a positive d2 says the channel is not what the formula describes. By orbital: s 76% positive, p 74%, d 37%, f 6%, g 7%, h 9%. The two populations differ in median raw spread 0.0159 vs 0.0029 and median fit residual 0.0058 vs 0.0003, U-test p < 1e-5. The MAGNITUDE class predicts the spread at R^2 = 0.761 against l alone at 0.230 and the sign at 0.267, and the sign adds nothing to the magnitude. The three quantities do not separate: d0 against |d2| gives r^2 = 0.270

> **PRIOR ART: the SIGN rule is NIST's own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel's scatter at R^2 = 0.761.  PRIOR ART: the SIGN rule is NIST own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel scatter at R^2 = 0.761.**

### `S.ritz` — the channel curve

**a channel is a CURVE, not a number: delta(n) = d0 + d2/(n-d0)^2, and the index reaches d0 while nothing in it reaches d2**

*a Rydberg channel with four or more members*

grade **MEASURED**· source *R 1150-1156; Ritz 1903; Hartree 1928; Ritz 1903; Hartree 1928*· depends on `S.ground`· 1 objects depend on it· depth 7

the d2 term removes 48% of what the compendium called scatter (0.0199 -> 0.0104 across 274 channels). d0 against ln Ne, l and charge gives R^2 = 0.549; the curvature gives 0.018. The ISOELECTRONIC step moves both coordinates by the same factor at every l — 1.194/0.859 at s, 1.150/0.979 at p, 0.858/0.907 at d, 0.561/0.627 at f — while the l step moves them differently: 1.427/0.752, 3.696/1.373, 8.536/5.264. Along a sequence the channel translates; along l it deforms, and fitting l as a 2x2 map improves on the scalar by only 14% at s->p and 1% beyond

> **PRIOR ART: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST's compendium states it in this form.  PRIOR ART: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST states it in this form.**

### `S.seed` — a seed

**G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X)**

*X closed; ℛ depends on G only through φ̂*

grade **PROVED**· source *M §14.5.7; Birkhoff 1937; Moore 1910; Birkhoff 1937*· depends on `A.env`, `A.R`· 3 objects depend on it· depth 3

> **PRIOR ART: a generating set of a closure system is any G with cl(G) = cl(X). That the envelope alone decides it is the specific form here; the notion is Moore-Birkhoff.  PRIOR ART: a generating set of a closure system is any G with cl(G) = cl(X). That the ENVELOPE alone decides it is the specific form here; the notion is Moore-Birkhoff.**

### `S.status` — the existence partition

**the index partitions by EXISTENCE STATUS, and nothing in it is impossible**

*the aufbau survey*

grade **MEASURED**· source *R 1191-1192; Theodosiou, Inokuti & Manson 1986*· depends on `S.ground`, `S.parent`· 1 objects depend on it· depth 8

101,328 cells. *** THE STATUS AXIS WAS REPLACED AT REGISTER 1578: VERIFIED/POSSIBLE/IMPROBABLE became WITNESSED/UNWITNESSED plus a NAMED BOUND, because improbable is a judgement about the future rather than a fact about the record — the same object-versus-observer fault register 1287 found in `standing`. *** Now: 337 WITNESSED (0.333% of the index) and 100,991 UNWITNESSED, of which 929 are exact by symmetry and need no measurement. Bounds on the rest: series above ng 28,527; no long-lived isotope 24,312; no analysis located at this charge 17,428; open-shell cores 26,641; not naturally occurring 225; and 2,929 with NO bound at all — separable series simply not yet measured. The charge bound is contradicted by twelve measured cells above it in this index's own file (R 1577). Every accuracy figure must be quoted against the witnessed count, not 101,328.

> **PRIOR ART: the distinction between what a survey admits and what is measurable is exactly the distinction Theodosiou, Manson & Inokuti make in their 1986 table across all ionisation stages.**

### `S.unit` — the unit cell

**all 219 covers contain a cell matching (3,0,1,1,*,0,1,1) — 3s1 to e-s ending 1, doublet, e free at 1 or 3; its function is to carry the value ONE where the corners carry extremes**

*three of the fifteen elements the corners miss are the alphabet values q=1, g=1, 2S=1; e=3 witnesses the target's ceiling and e=1 the source's*

grade **COMPUTED**· source *M §14.5.13; Karp 1972; Chvatal 1979*· depends on `S.channel`· 1 objects depend on it· depth 8

> **PRIOR ART: a cell present in every minimum cover is forced; the standard set-cover argument.  PRIOR ART: a set present in every minimum cover is forced by an element it uniquely covers — the same reduction rule. Chvatal (1979). That all 219 covers contain this cell is the measurement.**

## F. The family of closed indexes — 4 objects

### `F.exact` — the family's defect, exactly

**ℛ(Cl(U)) = 2^U, so E(Cl(U)) = 2^|U| − |Cl(U)| exactly**

*Cl(U) holds ∅ and U, and every ordered pair of points is separated by some closed set, making every envelope constant at 1*

grade **PROVED**· source *M §14.6.2; Moore 1910*· depends on `F.open`· depth 6

> **PRIOR ART: the closure of a set of generators over an unconstrained alphabet is the full power set, so the defect is the exact complement count. A corollary of extensivity and idempotence.**

### `F.moore` — the family of closed sets

**the ℛ-closed subsets of a closed index form a Moore family: ∩-closed 100%, ∪-closed 33–68%; 73, 146, 731 members**

*exhaustive at 8, 9, 16 cells*

grade **PROVED**· source *M §14.5; Moore 1910; Ward 1942*· depends on `S.seed`· 1 objects depend on it· depth 4

> **PRIOR ART: the closed sets of a closure operator form a Moore family — intersection-closed with a top. Moore, Introduction to a Form of General Analysis (1910); Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. That the R-closed subsets of a closed index form one is that theorem applied at one level up.**

### `F.open` — the family theorem

**THEOREM: the family of all closed indexes is itself an OPEN index — E = 182, 365, 64,804**

*every member has E = 0*

grade **PROVED**· source *M §14.6; Tarski 1955; Ward 1942*· depends on `F.moore`· 2 objects depend on it· depth 5

> **PRIOR ART: the lattice of closed sets of a closure operator is complete (Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309), but completeness is not the same as being CLOSED under the same operator one level up. That the family of closed indexes is itself open is measured here; the setting is Tarski-Ward.**

### `F.unstatable` — the unstatable family

**and it cannot be stated: a closed index has a seed, an open one costs seed + E, and E is 64,804 at 16 cells**

*corollary of F.open and S.open*

grade **PROVED**· source *M §14.6.1; Kolmogorov 1965*· depends on `F.open`, `S.open`· depth 6

> **PRIOR ART: the cost of stating an object is its description length — Kolmogorov, Three approaches to the quantitative definition of information, Probl. Inf. Transm. 1 (1965) 1-7. A closed index has a seed; an open one costs seed plus defect, and the difference is the statement cost.**

## G. Graphs, constraints and languages — 12 objects

### `G.allcons` — the index of all constraints

**every genuine constraint in the book, indexed over five coordinates: 22 carried by ℛ, 2 by ℛ₄, NONE by neither; E = 21, E₄ = 6, orientation cost 15**

*eight rows of a first attempt were coordinate systems entered as constraints; the two that no operator carried were both of those*

grade **COMPUTED**· source *M §21.5.5 / allcons.py; Freuder 1978*· depends on `A.r4`, `G.cons`· depth 4

> **PRIOR ART: indexing constraints by the coordinates they name is the constraint-hypergraph view — Freuder, CACM 21 (1978) 958-966.**

### `G.book` — the book as an index

**E(book) = 578 at chapter resolution, 0 at part resolution; a certificate exists**

*claim-bearing paragraphs with a § citation*

grade **COMPUTED**· source *M §30.1; Rota 1964*· depends on `A.E`, `A.cert`· depth 9

> **PRIOR ART: that a defect depends on the RESOLUTION at which an object is indexed is the coarsening question; Moebius inversion over a refinement lattice is Rota (1964).**

### `G.cons` — the constraint index

**Λ's seven constraints form a TREE — 8 nodes, 7 edges — with ZERO of 35 triples spanning three nodes**

*no 3-body among the constraints*

grade **COMPUTED**· source *M §21.5.2; Freuder 1982; Dechter & Pearl 1989*· depends on `L.c1`· 5 objects depend on it· depth 1

> **PRIOR ART: that a tree-structured constraint graph is globally consistent after arc consistency is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32; the width/induced-width machinery is Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### `G.graph` — the constraint graph

**Λ₁₃'s constraint graph: 12 nodes, 13 edges, girth 5, diameter 6, radius 3, treewidth 2, hub k at degree 4, cycle rank 2, no triangle at any stage**

*treewidth 2 at Λ₁₃ keeps Freuder's bound and §21.5.1's one-level shortfall*

grade **COMPUTED**· source *M §21.5.3 / Figure 21.1; Euler 1736; Diestel 2017*· depends on `G.cons`· depth 2

> **PRIOR ART: girth, diameter, radius and treewidth are standard graph invariants — see Diestel, Graph Theory (5th ed., 2017). Graph theory itself begins with Euler, Solutio problematis ad geometriam situs pertinentis (1736).**

### `G.near` — the seven near-misses

**Λ is one edge from a 3-body in exactly seven places, one per existing edge**

*every one a bond the physics does not make*

grade **COMPUTED**· source *M §21.5.2; Berge 1962*· depends on `G.cons`· depth 2

> **PRIOR ART: adding one edge to a tree creates exactly one cycle; the number of places is the number of existing edges. Berge, Theorie des graphes (1958/1962).**

### `G.prot` — the protocol index

**the 24 protocols occupy 19 cells in four coordinates; §2.8 and §2.24 share one**

*§2.24 is §2.8 specialised to heuristics*

grade **COMPUTED**· source *protindex.py; Freuder 1978*· depends on `G.reg`· depth 5

> **PRIOR ART: as G.allcons, applied to the protocol index.**

### `G.ref` — the reference index

**the reference index: 38 cells, box 144, E = 0, and NOT a tree -- access closes a cycle**

*access, referent, checked, verdict*

grade **COMPUTED**· source *M §16.6.1; Freuder 1982*· depends on `A.E`· depth 4

> **PRIOR ART: a non-tree constraint graph that nonetheless closes shows treeness is sufficient and not necessary — the converse direction of Freuder (1982).**

### `G.reg` — the register as an index

**E(register) = 6 at 68.8% density, and R recovers repair <= phi(corroboration)**

*coordinates assigned from the entry text*

grade **COMPUTED**· source *M §26.9; Shannon 1948*· depends on `A.E`, `A.R`· 1 objects depend on it· depth 4

> **PRIOR ART: recovery under a noisy channel is bounded by the channel capacity; that repair <= phi(corroboration) is that bound in this setting. Shannon (1948).**

### `G.shape` — shape decides the seed

**the constraint graph's shape decides the seed: path 8, star 6, balanced trees 6, forest 5 on six nodes over one alphabet; neither extreme is cheapest**

*seed is monotone in S with no exception, all six exact by branch and bound*

grade **COMPUTED**· source *M §21.5.4; Freuder 1982; Dechter & Pearl 1989*· depends on `S.cover`, `G.cons`· depth 5

> **PRIOR ART: that the constraint graph shape decides what a local method achieves is Freuder 1982 for trees and Dechter & Pearl 1989 for the general induced-width bound.**

### `G.stat` — statistics as a language

**statistics is a sixth language: max-entropy closure on the pairwise marginals recovers Lambda at 976, E = 0, restores a deleted cell, and GROWS on an added one, 976 to 1,048**

*its signature matches the information language, not order/geometry/analysis; the five split three-two between absorbing and growing*

grade **COMPUTED**· source *M §20 / stat_lang.py; Deming & Stephan 1940; Csiszar 1975*· depends on `A.R`· depth 3

> **PRIOR ART: the max-entropy distribution matching given marginals is reached by iterative proportional fitting — Deming & Stephan, Ann. Math. Stat. 11 (1940) 427-444; its information-geometric characterisation is Csiszar, I-divergence geometry, Ann. Prob. 3 (1975) 146-158.**

### `G.tower` — the cycle rank of the tower

**the tower's cycle rank rises by one at each two-parent axis — 0,0,1,1,2,2 — while triangles stay 0**

*the tree breaks at Λ₁₀*

grade **COMPUTED**· source *M §21.5.2; Berge 1962*· depends on `G.cons`, `T.tower`· depth 7

> **PRIOR ART: the cycle rank |E| - |V| + c is the first Betti number of a graph — Berge, Theorie des graphes et ses applications (1958/1962). That it rises by one at each two-parent axis is the measurement.**

### `G.trip` — independence is a triple property

**independence is a property of TRIPLES: surviving tests go as (1-f)^3, not (1-f)**

*the bracket relates T(n-1), T(n), T(n+1)*

grade **COMPUTED**· source *M §22.9; Dawid 1979; Pearl 1988*· depends on `B.brk`· depth 1

> **PRIOR ART: conditional independence is a relation on TRIPLES and obeys the graphoid axioms — Dawid, Conditional independence in statistical theory, J. R. Stat. Soc. B 41 (1979) 1-31; Pearl, Probabilistic Reasoning (1988), ch. 3.**

## L. Λ's own constraints — 41 objects

### `L.E0` — the closure theorem

**E(Λ) = 0**

*at the stated caps; verified at four settings and through the f shell*

grade **COMPUTED**· source *M §7.3, reg. 236; Moore 1910; Freuder 1982*· depends on `L.closed`, `A.E`· depth 8

> **PRIOR ART: E = 0 says the index equals its own closure. Moore (1910) for the operator; Freuder (1982) for why a tree-structured constraint graph gives it.**

### `L.F` — the generating function

**F = Σ_n z₁ⁿ Σ_{ℓ≤n−1} z₂^ℓ Σ_{k≤4ℓ+2} z₃^k [Σ_{S≤k} z₈^S] Σ_{q≤k} z₄^q Σ_e z₅^e Σ_{f<e} z₆^f Σ_{g≤min(q,4f+2)} z₇^g**

*at stated caps; the tree has no cycles so the sum factorises*

grade **COMPUTED**· source *M §11.3; Euler 1748; Stanley 1986*· depends on `L.tree`, `L.def`· 5 objects depend on it· depth 3

> **PRIOR ART: a multivariate generating function over a constrained region, written as nested sums. Euler, Introductio (1748); Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### `L.F1` — the cardinality

**F(1,…,1) = |Λ| = 976**

*as L.F*

grade **COMPUTED**· source *M §11; Euler 1748; Euler 1748; Stanley 1986*· depends on `L.F`· depth 4

> **PRIOR ART: setting all variables to one recovers the cardinality — the elementary specialisation of a generating function.  PRIOR ART: F(1,...,1) = |X| is the elementary specialisation of a generating function. Euler, Introductio (1748), ch. XVI; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### `L.Fm1` — the alternating specialisation

**F(−1) = 2, because ℓ and f each have exactly two consecutive values but are coupled to n and e**

*at stated caps*

grade **COMPUTED**· source *M §11.8.1; Euler 1748; Euler 1748; Stanley 1986*· depends on `L.rankpoly`· depth 5

> **PRIOR ART: F(-1) counts the difference between even- and odd-rank cells; the standard alternating specialisation.  PRIOR ART: F(-1) is the difference between even- and odd-rank counts, the standard alternating specialisation. Euler (1748); Stanley (1986), ch. 3, where it is related to rank symmetry.**

### `L.alpha` — the join-irreducible count

**|J(Λ)| = Σ_i (|A_i| − 1)**

*each generator is min{x ∈ Λ : x_c ≥ v} for one coordinate and one value*

grade **COMPUTED**· source *M reg. 268; Birkhoff 1937*· depends on `L.birk`· depth 10

> **PRIOR ART: the join-irreducibles of a product of chains are the coordinate steps, so |J| = sum(|A_i| - 1). Immediate from Birkhoff representation.**

### `L.amp` — the amplification

**A(y) = N[φ(Λ ∪ {y})] − N[φ(Λ)] − 1; median 340, minimum 59 over 220 trials**

*y a single inserted cell*

grade **COMPUTED**· source *M §16.8.4; Rota 1964*· depends on `A.R`, `L.def`· depth 3

> **PRIOR ART: the change in a closure count on adding a generator; the amplification is measured, the closure is Moore-Rota.**

### `L.arith` — divisor lattice embedding

**N(x) = ∏_i p_i^{x_i}; x≤y ⟺ N(x)|N(y); ∨↦lcm, ∧↦gcd, rank ↦ Ω(N)**

*p_i the i-th prime*

grade **COMPUTED**· source *M §9; Birkhoff 1937*· depends on `L.def`· 2 objects depend on it· depth 2

> **PRIOR ART: the divisor lattice with lcm as join and gcd as meet is the classical arithmetic model of a product of chains. Birkhoff, Lattice Theory (1940), ch. II.**

### `L.birk` — Birkhoff representation 1937

**Λ ≅ down-sets of J(Λ); |J(Λ)| = 17, 20 covering relations**

*Λ finite distributive*

grade **COMPUTED**· source *M §8.3; Birkhoff 1937*· depends on `L.dist`· 5 objects depend on it· depth 9

> **PRIOR ART: Birkhoff's representation theorem, Duke Math. J. 3 (1937) — every finite distributive lattice is the down-sets of its join-irreducibles. |J| = 17 is a computation inside that theorem.**

### `L.bits` — the Boolean representation

**Λ is the 976 words in {0,1}¹⁷ that are down-sets of J(Λ); join = OR, meet = AND; 17 bits carried, 9.93 needed, 7.07 surplus**

*Birkhoff correspondence*

grade **COMPUTED**· source *M §11.1.1; Birkhoff 1937; Shannon 1938*· depends on `L.birk`· 1 objects depend on it· depth 10

> **PRIOR ART: Birkhoff (1937) gives the down-set representation; encoding down-sets as Boolean words with OR as join and AND as meet is Shannon (1938).**

### `L.box` — the box factorises

**|box ∩ Λ| factorises because the constraint graph is a tree; no Möbius sieve needed**

*constraint graph acyclic*

grade **COMPUTED**· source *M §10.4; Freuder 1982; Rota 1964*· depends on `L.tree`· depth 3

> **PRIOR ART: the count factorises over a tree — no Moebius sieve is needed because there are no cycles to inclusion-exclude over. Freuder (1982) for the tree property; Rota (1964) for what the sieve would otherwise cost.**

### `L.c1` — node counting

**ℓ ≤ n − 1**

*hydrogenic radial solution*

grade **CITED**· source *M §7.1; Bohr 1913; Schroedinger 1926*· 3 objects depend on it· depth 0

> **PRIOR ART: l <= n-1 is the angular-momentum constraint of the hydrogen solution — Bohr, On the constitution of atoms and molecules, Phil. Mag. 26 (1913) 1-25; Schroedinger, Quantisierung als Eigenwertproblem, Ann. Phys. 79 (1926) 361-376.**

### `L.c2` — Pauli

**k ≤ 2(2ℓ+1) = 4ℓ+2**

*Pauli exclusion*

grade **CITED**· source *M §7.1; Pauli 1925; Stoner 1924*· 1 objects depend on it· depth 0

> **PRIOR ART: the subshell capacity 2(2l+1) is Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736, made exclusive by Pauli, Z. Phys. 31 (1925) 765-783.**

### `L.c3` — the transfer bound

**q ≤ k**

*counting*

grade **DEFINITIONAL**· source *M §7.1; Pauli 1925*· 1 objects depend on it· depth 0

> **PRIOR ART: q <= k, a transferred count cannot exceed the occupancy. Pauli (1925).**

### `L.c4` — node counting

**f ≤ e − 1**

*hydrogenic radial solution*

grade **CITED**· source *M §7.1; Bohr 1913*· 1 objects depend on it· depth 0

> **PRIOR ART: as L.c1, applied to the second shell pair.**

### `L.c5` — Pauli

**g ≤ 4f+2**

*Pauli exclusion*

grade **CITED**· source *M §7.1; Stoner 1924; Pauli 1925*· 1 objects depend on it· depth 0

> **PRIOR ART: as L.c2, applied to the second shell pair.**

### `L.c6` — the second transfer bound

**g ≤ q**

*counting*

grade **DEFINITIONAL**· source *M §7.1; Pauli 1925*· 1 objects depend on it· depth 0

> **PRIOR ART: g <= q, as L.c3 on the second shell pair.**

### `L.c7` — vector coupling

**2S ≤ k**

*vector coupling on the source*

grade **CITED**· source *M §7.1; Hund 1925; Pauli 1925*· 2 objects depend on it· depth 0

> **PRIOR ART: 2S <= k because at most k electrons can align their spins — Pauli exclusion (1925) with Hund first rule, Z. Phys. 33 (1925) 345-371.**

### `L.c8` — the occupancy floor

**k ≥ 1 (definitional restriction, not a bound)**

*a cell is a transition, not a state*

grade **DEFINITIONAL**· source *M §10.2, reg. 301; Pauli 1925*· 1 objects depend on it· depth 0

> **PRIOR ART: k >= 1 restricts to occupied subshells; definitional rather than a bound.**

### `L.chains` — the linear extensions

**maximal chains of Λ = linear extensions of J(Λ) = 1,113,045,672**

*Λ ≅ J(P)*

grade **COMPUTED**· source *M §12.9; Stanley 1986*· depends on `L.birk`· depth 10

> **PRIOR ART: maximal chains of J(P) correspond to linear extensions of P — Stanley, Enumerative Combinatorics Vol. 1, Prop. 3.5.2. The count is the computation; the bijection is his.**

### `L.chi` — the membership function

**χ(x) = H(n−1−ℓ)H(4ℓ+2−k)H(k−q)H(k−2S)H(e−1−f)H(4f+2−g)H(q−g); the coefficient function of F is χ**

*H the Heaviside step*

grade **COMPUTED**· source *M §11.1; Heaviside 1893*· depends on `L.F`, `L.def`· 1 objects depend on it· depth 4

> **PRIOR ART: the membership function as a product of step functions — Heaviside, Electromagnetic Theory (1893), where the unit step is introduced.**

### `L.circuit` — the implication circuit

**the 20 covering relations, as implications, cut 2¹⁷ = 131,072 words to exactly 976, at depth 5**

*monotone: AND, OR, implication; no NOT, no feedback*

grade **COMPUTED**· source *M §11.1.1; Shannon 1938*· depends on `L.bits`· depth 11

> **PRIOR ART: implications as a monotone Boolean circuit — Shannon, A symbolic analysis of relay and switching circuits, Trans. AIEE 57 (1938) 713-723.**

### `L.closed` — sublattice of a product

**Λ is closed under coordinatewise ∨ and ∧**

*every constraint of the form x_i ≤ φ(x_j) with φ non-decreasing*

grade **PROVED**· source *M §7.3; Birkhoff 1940*· depends on `L.def`, `A.rule`· 2 objects depend on it· depth 7

> **PRIOR ART: closure under coordinatewise join and meet is the definition of a sublattice of a product (Birkhoff, Lattice Theory, 1940). What makes Lambda one is that all eight constraints have the form x_i <= f(x_j) with f monotone.**

### `L.def` — the definition of Lambda

**Λ = { (n,ℓ,k,q,e,f,g,2S) ∈ ℤ⁸ : L.c1..L.c8 }, caps (n,e,ℓ,k,f) = (3,3,1,3,1)**

*caps stated; figures at other caps must say so (§7.4)*

grade **DEFINITIONAL**· source *M §7; Bohr 1913; Pauli 1925*· depends on `L.c1`, `L.c2`, `L.c3`, `L.c4`, `L.c5`, `L.c6`, `L.c7`, `L.c8`· 10 objects depend on it· depth 1

> **PRIOR ART: the eight constraints are the shell-structure rules of Bohr (1913) and Pauli (1925), written as inequalities on integer coordinates.**

### `L.dim` — order dimension (Dushnik–Miller)

**order dimension of Λ₈ is 8, rising by one per adjoined axis**

*at the stated caps*

grade **PROVED**· source *M §8.6; Dushnik & Miller 1941*· depends on `L.def`· 1 objects depend on it· depth 2

> **PRIOR ART: Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610. That a product of n chains has dimension n follows from the definition; what is measured here is that Lambda's dimension equals its coordinate count at every stage of the tower.**

### `L.dist` — Birkhoff / product of chains

**Λ is distributive (a sublattice of a product of chains)**

*none*

grade **PROVED**· source *M §8.1; Birkhoff 1937*· depends on `L.closed`· 5 objects depend on it· depth 8

> **PRIOR ART: a lattice is distributive iff it embeds in a product of chains (Birkhoff, Rings of sets, Duke Math. J. 3, 1937). Lambda is such a sublattice by construction, so distributivity is INHERITED, not proved here.**

### `L.metric` — the lattice metric

**log d is an ℓ¹ metric; d(x,z) ≤ d(x,y)·d(y,z)**

*as L.occ*

grade **COMPUTED**· source *M §9.2; Monjardet 1981*· depends on `L.occ`· depth 4

> **PRIOR ART: Monjardet, Metrics on partially ordered sets - a survey, Discrete Math. 35 (1981) 173-184.**

### `L.mobius` — Möbius function of a distributive lattice

**μ(x,y) = (−1)^{|y∖x|} if y∖x is an antichain in J(Λ), else 0**

*Λ ≅ J(P)*

grade **COMPUTED**· source *M §9.3; Rota 1964*· depends on `L.birk`· depth 10

> **PRIOR ART: Rota, On the foundations of combinatorial theory I: theory of Moebius functions, Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368. The antichain form of mu on a distributive lattice is his.**

### `L.modular` — modularity (equality, not submodularity)

**rank(a∨b) + rank(a∧b) = rank(a) + rank(b), rank = Σx_i**

*graded lattice*

grade **COMPUTED**· source *M §8.2; Dedekind 1900*· depends on `L.dist`· depth 9

> **PRIOR ART: the modular rank identity holds in any modular lattice and every distributive lattice is modular. Dedekind, Math. Ann. 53 (1900).**

### `L.occ` — the interval measure

**d(x,y) = τ( lcm(N(x),N(y)) / gcd(N(x),N(y)) ) = ∏_i(|x_i−y_i|+1) = |[x∧y, x∨y]|**

*τ the divisor count; d(x,x)=1*

grade **COMPUTED**· source *M §9.2; Monjardet 1981*· depends on `L.arith`· 3 objects depend on it· depth 3

> **PRIOR ART: the interval size as a product of coordinate spans, and its arithmetic form via lcm and gcd. Monjardet, Metrics on partially ordered sets, Discrete Math. 35 (1981) 173-184.**

### `L.omega` — distinct-prime-counting function

**ω(N(x)) ≤ dim(Λ)**

*one prime per coordinate*

grade **PROVED**· source *M §9.1; Birkhoff 1937*· depends on `L.arith`, `L.dim`· depth 3

> **PRIOR ART: in the divisor representation, the number of distinct primes dividing N(x) is the number of coordinates in which x is non-minimal, bounded by the dimension.**

### `L.pal` — palindromic rank polynomial ⟺ self-dual

**F palindromic ⟺ the poset is self-dual; Λ's F is not palindromic**

*graded poset*

grade **PROVED**· source *M §11.8; Stanley 1986*· depends on `L.rankpoly`, `L.skew`· depth 5

> **PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1, ch. 3 — a graded poset's rank polynomial is palindromic iff it is rank-symmetric.**

### `L.pushback` — join-prime and meet-prime

**no cell of Λ₈ is both join-prime and meet-prime, so pushback ≥ 16 > 0 for every cell**

*18 join-irreducibles and 18 meet-irreducibles, intersection empty*

grade **PROVED**· source *M §16.8.5; Birkhoff 1937; Gratzer 1978*· depends on `L.birk`· 1 objects depend on it· depth 10

> **PRIOR ART: join-prime and meet-prime are dual notions in a distributive lattice, and a cell cannot generally be both. Gratzer, General Lattice Theory (1978).**

### `L.rankpoly` — the rank polynomial

**F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + … + 122z⁸ + 121z⁷ + … + 5z + 1); F′(1)/F(1) = 11.0666**

*single-variable specialisation*

grade **COMPUTED**· source *M §11.1; Stanley 1986*· depends on `L.F`· 2 objects depend on it· depth 4

> **PRIOR ART: Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 3. F'(1)/F(1) = mean rank is the standard first-moment identity.**

### `L.real` — the index against the real subshells

**Λ's eight constraints on 247 real subshells across ALL 118 elements incl. 19 anomalies and 15 predicted superheavies: 18,288 tests, 0 failures**

*IUPAC ground states*

grade **COMPUTED**· source *close_L.py; Madelung 1936; NIST*· depends on `L.c1`· depth 1

> **PRIOR ART: the 247 real subshells across 118 elements are the observed ground configurations, tabulated by NIST; the ordering is Janet-Madelung. Testing Lambda constraints against them checks the index, not the table.**

### `L.skew` — the rank skew

**centre of mass 11.0666 vs midpoint 11.5, skew −0.43; only 8 of 976 cells fixed by x ↦ max − x**

*at the stated caps*

grade **COMPUTED**· source *M §8.4; Gauss 1809*· depends on `L.def`· 1 objects depend on it· depth 2

> **PRIOR ART: the third standardised moment of a rank distribution. Gauss (1809).**

### `L.sperner` — Sperner property / Dilworth

**the largest antichain equals the largest rank level; max 122 at rank 11**

*rank sequence log-concave hence unimodal*

grade **COMPUTED**· source *M §8.4; Sperner 1928; Stanley 1980*· depends on `L.dist`· depth 9

> **PRIOR ART: Sperner 1928 for the Boolean lattice; Stanley, Weyl groups, the hard Lefschetz theorem, and the Sperner property, SIAM J. Alg. Disc. Meth. 1 (1980) 168-184, proves the order-ideal lattice of a product of chains is Peck — rank-symmetric, rank-unimodal, strongly Sperner. Lambda is of that form, so the property is INHERITED.**

### `L.step` — the interval-removal step

**X ∖ [a,b] is a sublattice iff a is join-prime and b is meet-prime; step(Λ₈) = 4**

*distributive*

grade **PROVED**· source *M §16.8.5; Birkhoff 1937; Gratzer 1978*· depends on `L.pushback`· depth 11

> **PRIOR ART: removing an interval leaves a sublattice iff the endpoints are join-prime and meet-prime — the standard interval-removal criterion. Gratzer, General Lattice Theory (1978), ch. II.**

### `L.total` — the membership function is total

**χ_Λ : ∏A_i → {0,1} is total: membership decided for every ambient point**

*Λ a finite intersection of decidable comparisons*

grade **PROVED**· source *M §16.5; Birkhoff 1940*· depends on `L.chi`· depth 5

> **PRIOR ART: a membership function defined by inequalities on coordinates is total on the ambient product by construction.**

### `L.tree` — the constraint tree

**constraint graph n—ℓ—k—q—g—f—e with 2S pendant at k: 8 nodes, 7 edges, a caterpillar; treewidth 1**

*every constraint binds exactly two coordinates*

grade **COMPUTED**· source *M §8.5, §11.4; Freuder 1982*· depends on `L.def`· 5 objects depend on it· depth 2

> **PRIOR ART: that a constraint graph is a tree, and what follows from it, is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32.**

### `L.void` — the void

**void(x,y) = ∏_i(|Δ_i|+1) − |[x∧y, x∨y] ∩ Λ|**

*none*

grade **DEFINITIONAL**· source *M §10; Rota 1964*· depends on `L.occ`· 1 objects depend on it· depth 4

> **PRIOR ART: the difference between a box count and the cells it actually contains is what Moebius inversion would compute. Rota (1964).**

### `L.voidfrac` — the void-free fraction

**void-free fraction 27.7–30.1% across 776M pairs; joint 30.13% vs product 20.19%, factor 1.49**

*at stated caps*

grade **COMPUTED**· source *M §10.2; Rota 1964*· depends on `L.void`· depth 5

> **PRIOR ART: as L.void; the fraction is the measurement.**

## T. The tower and its couplings — 16 objects

### `T.a10` — Racah 1943 seniority

**2S′ ≤ v ≤ g, v ≡ g (mod 2)**

*Racah seniority for ℓ^N*

grade **CITED**· source *M §12.11.1 / T A14; Racah 1943*· depends on `T.a9`· 2 objects depend on it· depth 2

> **PRIOR ART: seniority v, with 2S <= v <= g and v congruent to g mod 2, is Racah, Phys. Rev. 63 (1943) 367-382 — the classification of states of l^n by the number of unpaired electrons.**

### `T.a11` — the parent bound

**2J_c ≤ φ̂(k), φ̂ = max 2J over terms of ℓ^k = {1:3, 2:4, 3:5}**

*φ̂ read off the realised extent, not from a law*

grade **COMPUTED**· source *M §12.11.1 / T A15; Condon & Shortley 1935; Racah 1942*· depends on `T.a10`· 2 objects depend on it· depth 3

> **PRIOR ART: the term structure of a subshell l^k, and the maximum J it carries, is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII; Racah, Theory of complex spectra II, Phys. Rev. 62 (1942) 438-462, gives the general classification. The values {1:3, 2:4, 3:5} are read from that table, not derived here.**

### `T.a12` — the recoupling bound

**loose: 2K ≤ 2J_c + 2f_max (one parent). exact: |2J_c−2f| ≤ 2K ≤ 2J_c+2f step 2 (two parents)**

*jK pair coupling*

grade **CITED**· source *M §12.11.1 / T A16; Wigner 1931; Racah 1942*· depends on `T.a11`· 3 objects depend on it· depth 4

> **PRIOR ART: the triangle condition |j1-j2| <= J <= j1+j2 in steps of one is the Clebsch-Gordan series — Wigner, Gruppentheorie (1931); its application across parents is Racah, Phys. Rev. 62 (1942) 438-462.**

### `T.a13` — the spin-half bound

**|2J − 2K| ≤ 1**

*outer electron carries spin ½*

grade **CITED**· source *M §12.11.1 / T A17; Condon & Shortley 1935*· depends on `T.a12`· 1 objects depend on it· depth 5

> **PRIOR ART: |2J - 2K| <= 1 is the coupling of a spin-half to K in the jK scheme; Condon & Shortley (1935), ch. X.**

### `T.a9` — the seniority floor

**2S′ ≤ g**

*vector coupling on the target*

grade **CITED**· source *M §12.10.1; Racah 1943*· depends on `L.c7`· 5 objects depend on it· depth 1

> **PRIOR ART: 2S <= g bounds the total spin by the occupancy — Pauli exclusion in Racah seniority form, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### `T.a9p` — the admissible Pauli cut

**2S′ ≤ 2f+1 (the admissible Pauli cut); Λ₉′ = 1,561 cells, 93 removed; closes the cycle f–g–2S′**

*min(g,4f+2−g) ≤ 2f+1 by averaging*

grade **COMPUTED**· source *M §12.11.1 / T 2.2; Pauli 1925; Racah 1943*· depends on `T.a9`· depth 2

> **PRIOR ART: the Pauli cut on a subshell's allowed terms is Pauli's exclusion principle (Z. Phys. 31, 1925) as applied to equivalent electrons; the seniority classification that makes it computable is Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### `T.dens` — the axis density

**density(axis) = Σ_parents |exact fibre| / Σ_parents |admissible fibre| = 63.7, 67.5, 44.7, 17.0, 31.4, 64.4%**

*three non-obvious exact sets required*

grade **COMPUTED**· source *M §12.11.1 / T A18; Racah 1942; Racah 1942; Wigner 1931*· depends on `T.tower`· 2 objects depend on it· depth 7

> **PRIOR ART: the ratio of exact to admissible fibre sizes measures how much a triangle condition tightens a Pauli bound. Both bounds are standard; the ratio is measured.  PRIOR ART: the ratio of exact fibre to admissible fibre measures how much the triangle condition (Wigner 1931, Clebsch-Gordan) tightens the Pauli cap (Racah 1942). Both bounds are theirs; the density is measured.**

### `T.dich` — the counting-coupling dichotomy

**counting coordinates close exactly; coupling coordinates close as envelopes; no third kind**

*the exact coupling bound is made of reflection, congruence and triangle*

grade **COMPUTED**· source *M §12.11.3; Racah 1942*· depends on `T.dens`· 1 objects depend on it· depth 8

> **PRIOR ART: the split between coordinates that COUNT (occupancy, capacity) and coordinates that COUPLE (J, K, S) is the organising distinction of Racah's algebra. Counting coordinates carry Pauli caps; coupling coordinates carry triangle conditions, and the two close differently.**

### `T.excl` — the three excluded forms

**three excluded forms: REFLECTION (particle–hole conjugation), CONGRUENCE (fermion parity), TRIANGLE (one sum and one difference)**

*each is non-monotone or multi-parent*

grade **COMPUTED**· source *M §12.11.2; Racah 1943; Wigner 1931*· depends on `T.dich`, `A.rule`· 2 objects depend on it· depth 9

> **PRIOR ART: particle-hole conjugation, fermion parity and the triangle rule are all standard: conjugation from the complementary-shell theorem (Racah 1943), parity from the antisymmetry of the wavefunction, and the triangle inequality |j1-j2| <= J <= j1+j2 from the Clebsch-Gordan series (Wigner 1931).**

### `T.invariant` — basis independence of the level set

**the exact J multiset is identical in jK, LS, LK and jj; the four cell counts price four ROUTES**

*coupling schemes are basis changes*

grade **COMPUTED**· source *M §12.11.4; Wigner 1931; Racah 1942*· depends on `T.scheme`, `T.dens`· depth 8

> **PRIOR ART: the J multiset of a configuration is independent of coupling scheme because the schemes are unitary recouplings of one space — Wigner, Gruppentheorie (1931); Racah's 6-j and 9-j coefficients are the transformation matrices. What is measured here is the CELL COUNT each scheme costs, not the invariance.**

### `T.para` — parastatistics

**capacity(ℓ) = m(4ℓ+2) for parastatistics of order m; E = 0 through Λ₁₃ for m = 1,2,3**

*m(4ℓ+2) monotone in ℓ for every m, so A.rule is preserved*

grade **COMPUTED**· source *T 2.1 / D3; Green 1953*· depends on `T.tower`, `A.rule`· depth 7

> **PRIOR ART: parastatistics of order m, in which a state holds up to m particles, is H. S. Green, A generalized method of field quantization, Phys. Rev. 90 (1953) 270-273. The capacity m(4l+2) is its shell-model form.**

### `T.real` — the bounds against real terms

**the four coupling bounds on the exact term structure of every subshell: 85,829 tests, 0 failures**

*ℓ = 0..3, k = 1..4ℓ+2*

grade **COMPUTED**· source *microstate enumeration; Condon & Shortley 1935*· depends on `T.a9`· depth 2

> **PRIOR ART: the exact term structure of every subshell is tabulated in Condon & Shortley (1935), ch. VII, and in the NIST compendium. The 85,829 tests check the four coupling bounds AGAINST that table; the table is not this work.**

### `T.scheme` — the four coupling schemes

**closure holds in LS, LK, jK, jj: Λ₁₃ = 431,050 / 341,150 / 199,130 / 206,520, E = 0 throughout**

*a uniform one-parameter looseness convention*

grade **COMPUTED**· source *T 2.1b; Condon & Shortley 1935; Racah 1942*· depends on `T.tower`· 1 objects depend on it· depth 7

NOT CHECKABLE and the book says why: the looseness convention is named and not printed, and two committed readings BRACKET rather than determine the figures — LS in [383,065, 597,325] contains 431,050, jj in [160,380, 244,060] contains 206,520 (R 1010)

> **PRIOR ART: LS, LK, jK and jj are the four standard angular-momentum coupling schemes — Condon & Shortley (1935), ch. X; the jK and LK intermediate schemes are Racah's. That the same physical states are counted in each is the content of the recoupling theory, and the four cell counts price the SCHEME rather than the physics.**

### `T.tight` — constraint tightness as a count

**the tight-pair count of a base is exactly 2S, S the envelope-step count**

*van Beek & Dechter's measure*

grade **COMPUTED**· source *M §14.5.9; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999*· depends on `A.env`· depth 2

> **PRIOR ART: the tight pairs of a staircase constraint are its envelope steps — Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271.  PRIOR ART: the tight pairs of a staircase constraint are the points where its envelope steps — Deville, Barette & Van Hentenryck (1999). That the count is exactly 2S for S the envelope-step count is the measurement.**

### `T.tower` — the tower

**Λ₈…Λ₁₃ = 976, 1654, 2535, 13585, 22275, 64290; E = 0 at every stage, swept against every ambient cell to 47,775,744**

*at stated caps*

grade **COMPUTED**· source *M §12.11.0.10, reg. 249; Racah 1942; Condon & Shortley 1935; Racah 1942, 1943; Condon & Shortley 1935*· depends on `T.a9`, `T.a10`, `T.a11`, `T.a12`, `T.a13`· 5 objects depend on it· depth 6

CORRECTED 2026-08-11, re-applying register 1399 whose source fix was LOST in the 1.6.1 rollback — the register crossed as prose, the code did not. This object STATED 70905, 199130 at Lambda-12 and Lambda-13 while indices.py COMPUTES 22275, 64290. The first four agreed; only the last two differed, and register 541 named the cause without connecting it: the exact triangle against the loose one-parent bound differ by 3.18 at Lambda-12. A sequence is a single claim and its terms must come from one convention, so the computed (exact-triangle) values now stand. Note also that 199,130 was simultaneously T.scheme's jK figure — one number doing two jobs in two objects with neither saying so.

> **PRIOR ART: the tower adjoins the coupling quantum numbers in the standard order — seniority, then J of the core, then K, then J. Each is Racah or Condon & Shortley; the cell counts and the closure at each stage are the measurement.  PRIOR ART: the tower adjoins the coupling quantum numbers in the standard order — seniority (Racah 1943), the core J (Racah 1942), then K and J (Condon & Shortley 1935, ch. X). Each axis is theirs; the cell counts 976, 1654, 2535, 13585, 70905, 199130 and the closure at every stage are the measurement.**

### `T.trad` — the tree or the tightness

**the tree or the tightness: imposing the exact triangle at axis 12 gives 22,275 cells and E = 35,570**

*the exact bound has two parents*

grade **COMPUTED**· source *M §12.11.5 / T 2.4; Freuder 1982; Racah 1942*· depends on `T.a12`, `A.rule`· depth 7

> **PRIOR ART: the trade between tree structure and constraint tightness is Freuder (1982) for the tree side; the exact triangle is Racah/Wigner. The pricing is the measurement.**

## E. Empirical indexes — table, nuclide, layout — 4 objects

### `E.ioniz` — the refusal map

**first ionisation energies given to the bracket as bare numbers refuse at Be→B, N→O, Mg→Al and P→S — four steps of twelve, 67% admissible**

*the same two positions in both periods: the s2-p1 subshell opening and the p3-p4 first pairing*

grade **COMPUTED**· source *M §6.2; Mendeleev 1869; NIST*· depends on `B.brk`· depth 1

> **PRIOR ART: first ionisation energies as a periodic property date to Mendeleev; the values are NISTs. That bare numbers refuse the bracket is a statement about what a bracket needs, not about the data.**

### `E.layout` — the price of a layout

**hydrogen's placement is free and helium's costs 16, and they are not additive: −16 and 0 apart, −1 together**

*E set by the largest group used in period 1*

grade **COMPUTED**· source *M §6.1.1; Janet 1929*· depends on `E.table`· depth 3

> **PRIOR ART: hydrogen and helium are the classic placement anomalies of the periodic table, and Janets left-step form resolves them differently from the classroom table. The cost measured here is of the CHOICE.**

### `E.nuclide` — the nuclide chart's defect

**the measured nuclide chart indexed by (Z, N) closes at E = 9, stable across four proton-number cutoffs; the nine cells are the mass formula's pairing and clustering terms**

*cells named at one cutoff persist at every larger one*

grade **COMPUTED**· source *M §6.2; Segre 1945*· depends on `A.env`· depth 2

*** COUNT NOT REPRODUCED 2026-08-11 (R 1550). *** AME2020 Table I was captured from the published paper (Chin. Phys. C 45, 030003, Table I, 3558 rows, Z = 0-118, A = 1-295) and E recomputed with the same operator: E = 2, NOT 9, and stable at 2 across cutoffs Z <= 20, 50, 82, 92 and 118. Six variants of the cell set were tried - axes swapped, neutron excluded, measured-only, Z and N both positive - and none gives 9; measured-only gives 95. WHAT DOES REPRODUCE: the STABILITY across cutoffs, the cells being NAMEABLE PHYSICS, and the reading of them as the mass formula pairing term - the two defect cells are the empty cell (0,0) and Z=2 N=0, THE DIPROTON, which is unbound and is the textbook pairing failure. Three of four claims hold and the number does not. Cause UNDETERMINED: a different source edition, a different inclusion rule, or an arithmetic error in the original.

> **PRIOR ART: the chart of nuclides indexed by (Z, N) is Segres chart, in use since the 1940s.**

### `E.table` — the thirty-six decomposed

**the periodic table's 36 decompose 25 + 11, not 26 + 10; E is placement-sensitive, 36 at group 18 and 20 at group 2**

*all 118 elements*

grade **COMPUTED**· source *M §6.1.1; Mendeleev 1869; Janet 1929*· depends on `A.env`· 1 objects depend on it· depth 2

> **PRIOR ART: the periodic tables arrangement is Mendeleev, Ueber die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente, Z. Chem. 12 (1869) 405-406; the left-step form on n+l is Janet (1929). That E is placement-sensitive is a statement about which arrangement, not about the elements.**

## B. The bracket — 21 objects

### `B.V` — the price V — the bracket's width against its error

**V = w/e where w = |T(n+1)−T(n−1)|, e = |T(n) − ½(T(n−1)+T(n+1))|**

*three consecutive members*

grade **DEFINITIONAL**· source *M §21.1; Milne-Thomson 1933*· depends on `B.brk`· 3 objects depend on it· depth 1

> **PRIOR ART: the ratio of a first difference to a second is the standard curvature-to-slope measure of a finite-difference scheme. Milne-Thomson, The Calculus of Finite Differences (1933), ch. I-II.**

### `B.V43` — the four-thirds law

**V = 4ν/3 for a Rydberg series; in general V(x,p) = 4x/(h|p−1|) for y = x^p**

*T = Z²R/ν²*

grade **COMPUTED**· source *M §21.1; Rydberg 1890*· depends on `B.V`· 3 objects depend on it· depth 2

> **PRIOR ART: for a Rydberg series T ~ nu^-2, so the ratio of first to second differences is 4nu/3 by direct expansion. Rydberg, Recherches sur la constitution des spectres d emission, K. Sven. Vetensk. Akad. Handl. 23 (1890).**

### `B.Vexact` — the exact price

**V = 4ν³/(h(3ν²−h²)); with r = ν/h, V = 4r³/(3r²−1). Z and R cancel identically**

*step h free*

grade **PROVED**· source *M §21.4; Rydberg 1890*· depends on `B.V43`· 2 objects depend on it· depth 3

> **PRIOR ART: the exact form follows from the Rydberg term T = Z^2 R / nu^2 by finite differencing; Z and R cancel because the ratio is scale-free.**

### `B.adm` — the five-sigma admissibility threshold — where the bracket may be applied at all

**r = 2Z²R/(ν³σ) ≥ 5**

*levels separated by more than 5σ*

grade **DEFINITIONAL**· source *M §20.5; Gauss 1809*· 1 objects depend on it· depth 0

> **PRIOR ART: a five-sigma admissibility threshold is a statement about signal against measurement error, in the Gaussian error model of Gauss, Theoria motus corporum coelestium (1809).**

### `B.aitken` — Aitken Δ² / Seki Kōwa

**Aitken's Δ² on a Rydberg series lands at I − T/3, because the correction is (ΔT)²/Δ²T → (2/3)T**

*algebraic not geometric convergence*

grade **PROVED**· source *M §24.6; Aitken 1926*· depends on `B.newton`· depth 3

> **PRIOR ART: Aitken, On Bernoulli's numerical solution of algebraic equations, Proc. R. Soc. Edinb. 46 (1926) 289-305 — the delta-squared process. That it lands at I - T/3 on a Rydberg series is the measurement; the process is his.**

### `B.brk` — monotone interpolation bracket

**T(n) lies between T(n−1) and T(n+1)**

*T monotone in n within a channel*

grade **PROVED**· source *M §20.1; Leibniz 1682; Milne-Thomson 1933*· 6 objects depend on it· depth 0

measured at 789 of 789 interior cells — and it is the TRIVIAL bracket, which cannot fail (R 797, 830)

> **PRIOR ART: that a term of an alternating or monotone sequence lies between its neighbours is the classical bracketing of finite differences — Leibniz's alternating-series test in its difference form; Milne-Thomson, The Calculus of Finite Differences (1933), ch. I. The book's contribution is applying it to Rydberg terms cell by cell, not the bracket.**

### `B.coll` — the assembly rule — a composite observable's scaling exponent is 2a + 3b

**an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b}**

*⟨r⟩ ∝ ν², ΔE ∝ ν⁻³*

grade **PROVED**· source *M §24.1; Bohr 1913; Bethe & Salpeter 1957*· 1 objects depend on it· depth 0

> **PRIOR ART: the scaling of hydrogenic expectation values, <r^a> ~ nu^{2a} and Delta E ~ nu^{-3}, is Bohr's correspondence scaling (1913) in its quantum form; tabulated in Bethe & Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), sec. 3.**

### `B.fail` — when the bracket fails

**the bracket fails ⟺ |ΔT| > 2Z²R/ν³**

*a perturber reorders only if the shift exceeds half the local spacing*

grade **PROVED**· source *M §23.3; Rydberg 1890*· depends on `B.brk`· 1 objects depend on it· depth 1

the yardstick verified: 2Z^2R/nu^3 against measured adjacent spacing over 742 pairs gives median 1.201 (R 832)

> **PRIOR ART: the local spacing of a Rydberg series is 2 Z^2 R / nu^3, the derivative of the term formula. A shift exceeding half of it reorders the levels.**

### `B.floor2` — the floor at two

**V > 2 for any monotone sequence; V → 2 only as one step vanishes**

*d₀,d₁ > 0; V = 2(d₀+d₁)/|d₀−d₁|*

grade **PROVED**· source *M §21.2 Prop 14.1; Jensen 1906*· depends on `B.V`· 1 objects depend on it· depth 2

> **PRIOR ART: V > 2 for a monotone sequence is a form of Jensen's inequality — the chord lies above the curve for a convex function, so the second difference cannot exceed half the first. Jensen, Sur les fonctions convexes, Acta Math. 30 (1906) 175-193.**

### `B.floor32` — the Rydberg floor

**V ≥ 32/11 = 2.909 for a Rydberg series specifically**

*hydrogenic form*

grade **COMPUTED**· source *M §21.2; Rydberg 1890; Jensen 1906*· depends on `B.floor2`, `B.V43`· depth 3

> **PRIOR ART: the floor V > 2 is Jensen convexity (1906); the sharper 32/11 for a Rydberg series follows from its specific nu^-2 form.**

### `B.frac` — the fractional widths

**w/T = 4(h/ν) + 8(h/ν)³ and e/T = 3(h/ν)²; their ratio is V**

*Rydberg*

grade **COMPUTED**· source *M §21.6; Taylor 1715*· depends on `B.Vexact`· depth 4

> **PRIOR ART: expanding the first and second differences of nu^-2 in powers of h/nu is Taylor series with a step. Taylor, Methodus incrementorum directa et inversa (1715).**

### `B.hstar` — the optimal step

**h* = √(2β/(α y″)) minimises αw + βV, valid for h* ≪ ν**

*leading order*

grade **COMPUTED**· source *M §21.5.3; Lagrange 1797; Curtis & Reid 1974*· depends on `B.pareto`· depth 5

NOT CHECKABLE here: its source M §21.5.3 does not appear in the book's text and the objective it minimises is not stated, so the stationary point cannot be verified (R 1010)

> **PRIOR ART: minimising a weighted sum of two competing costs by setting the derivative to zero is elementary optimisation; the h* ~ sqrt(2 beta/(alpha y)) form is the standard step-size optimum of finite-difference practice.  PRIOR ART: the optimal finite-difference step balances truncation error against roundoff, giving h* proportional to sqrt(eps/y) — Curtis & Reid, The choice of step lengths when using differences to approximate Jacobian matrices, J. Inst. Math. Appl. 13 (1974) 121-126. Here the two costs are width and price rather than truncation and roundoff, and the same balance applies.**

### `B.newton` — Newton decrement, Nesterov–Nemirovskii 1994

**8y′²/y″ = 8λ² with λ² = ∇f ᵀ[∇²f]⁻¹∇f; for a Rydberg series λ² = (2/3)T**

*one dimension: λ² = f′²/f″*

grade **PROVED**· source *M §21.8.1; Newton 1669; Nesterov & Nemirovskii 1994*· depends on `B.V`· 2 objects depend on it· depth 2

> **PRIOR ART: the Newton decrement lambda^2 = grad f^T [Hess f]^{-1} grad f is the standard measure of proximity to a minimum in interior-point theory (Nesterov & Nemirovskii 1994); Newton's method itself is De analysi (1669).**

### `B.nuV` — the value-one crossing — where the bracket's price V passes unity

**ν_V = (3Z²R/5q)^{1/4}**

*curvature resolvable at quotation granularity q*

grade **PROVED**· source *M §21.15; Rydberg 1890*· depth 0

the crossing where V passes unity, computed from the quotation granularity q

> **PRIOR ART: solving V = 1 for nu against a quotation granularity q gives the quartic root; the term formula is Rydberg (1890).**

### `B.ordbr` — the ordered bracket

**sign(f(n) − p(n)) = (−1)^{k+1}(−1)^m with m nodes above n; a two-sided deductive bracket at every order**

*sign(f^{(j)}) = (−1)^j*

grade **PROVED**· source *M §21.10.1; Newton 1687; Milne-Thomson 1933*· depends on `B.brk`· depth 1

> **PRIOR ART: the sign of the error of a Newton interpolating polynomial alternates with the number of nodes above the evaluation point — the standard remainder theorem for finite differences, Newton's divided-difference form (Principia, Book III, Lemma V); Milne-Thomson (1933), ch. VIII.**

### `B.ordk` — the admissible order

**order k admissible while |Δ^{k+1}T| > 5·2^{k+1}·σ**

*the (k+1)-th difference is a signed sum of 2^{k+1} levels*

grade **PROVED**· source *M §21.10.4; Milne-Thomson 1933*· depends on `B.adm`· depth 1

> **PRIOR ART: the admissible order of a difference scheme is set by where the next difference falls below the noise, and the 2^(k+1) growth of noise under k-fold differencing is standard. Milne-Thomson (1933), ch. II.**

### `B.pareto` — the width-price front

**dw/dh > 0 and dV/dh < 0 for every monotone convex y and every h; the family {(w,V)} is a Pareto frontier**

*w ~ h, e ~ h²*

grade **PROVED**· source *M §21.5.2; Pareto 1896*· depends on `B.Vexact`· 1 objects depend on it· depth 4

> **PRIOR ART: a family in which no member improves both objectives is a PARETO FRONT — Pareto, Cours d'economie politique (1896). That dw/dh > 0 and dV/dh < 0 for every monotone convex y makes {(w,V)} one is the proof here; the notion is his.**

### `B.pole` — the linear pole

**V has a pole at p = 1: a linear observable has no curvature to price**

*y = x^p*

grade **PROVED**· source *M §18.5; classical; Taylor 1715; Taylor 1715; Milne-Thomson 1933*· depends on `B.V43`· depth 3

> **PRIOR ART: a linear function has vanishing second difference, so any ratio measuring curvature against slope diverges there. The pole at p = 1 is that statement.  PRIOR ART: a linear function has vanishing second difference, so any curvature-to-slope ratio diverges. Elementary from the Taylor expansion.  PRIOR ART: a linear function has vanishing second difference, so a ratio of first to second difference diverges. Taylor, Methodus incrementorum (1715); Milne-Thomson, The Calculus of Finite Differences (1933), ch. I.**

### `B.rank1` — the rank-one factorisation

**rank(log q) = 1 across fifteen Rydberg observables; second singular value 1.8×10⁻¹⁴**

*every observable is ν to a power*

grade **COMPUTED**· source *M §24.2; Eckart & Young 1936*· depends on `B.coll`· depth 1

> **PRIOR ART: that a matrix has rank one is read from its singular values — Eckart & Young, The approximation of one matrix by another of lower rank, Psychometrika 1 (1936) 211-218. A second singular value of 1.8e-14 is numerical zero, so log q factorises exactly.**

### `B.selfconc` — self-concordance

**T(ν) is self-concordant, |f‴| ≤ 2(f″)^{3/2}, for ν ≤ (√6/2)·Z√R**

*T = Z²R/ν²*

grade **PROVED**· source *M §21.8.2; Nesterov & Nemirovskii 1994*· depends on `B.newton`· depth 3

> **PRIOR ART: self-concordance, |f'''| <= 2(f'')^{3/2}, is Nesterov & Nemirovskii, Interior-Point Polynomial Algorithms in Convex Programming (1994), the condition under which Newton's method converges at a rate independent of the problem's conditioning.**

### `B.silence` — what silence implies

**the bracket holding ⟹ |ΔT| < 2Z²R/ν³ at that cell**

*contrapositive of B.fail*

grade **PROVED**· source *M §23.5; Rydberg 1890*· depends on `B.fail`· depth 2

849 of 849 cells satisfy it; median |dT|/spacing 0.0015, largest 0.25 (R 831)

> **PRIOR ART: the contrapositive of B.fail, on the same term formula.**

## K. Transit and information — 24 objects

### `K.arrow` — the arrow index

**X_w = {a : w(tgt a) ≤ w(src a)} is closed; one arrow per coordinate and no others; sums, max and min all fail**

*w a single coordinate*

grade **COMPUTED**· source *M §12.11.0.2; Birkhoff 1937*· depends on `K.clockfail`, `A.rule`· depth 8

> **PRIOR ART: a set of the form {a : w(target) <= w(source)} for monotone w is a down-set of the induced order, hence closed. Birkhoff, Rings of sets (1937).**

### `K.axis` — the axis test

**an axis earns a COORDINATE when it is independent of the others AND its distinct values are few relative to what it adds; both conditions are necessary**

*a closed index and a candidate axis*

grade **MEASURED**· source *R 1127-1131; Dushnik & Miller 1941; Shannon 1948*· depends on `K.redun`· 1 objects depend on it· depth 4

on the same elements, Z<=16: (Z,charge,l) gives 0% redundancy, +multiplicity gives 82%, +2J gives 0% again. 2J is NOT derived — no combination determines it — but |L-S| <= J <= L+S constrains it to 2min(l,S)+1 values of seventeen. A coordinate must be free, not merely undetermined. The entropy account is PARTIAL: retained entropy is 26% for multiplicity and 27% for 2J, which does not separate them

> **PRIOR ART: an axis earns a coordinate when it is order-independent of the others (Dushnik & Miller 1941) and carries information (Shannon 1948). The test combines both.**

### `K.cat` — the tower is a category

**Λ₉ is a category: 41,682 composable pairs, zero failures, associative**

*as K.comp*

grade **COMPUTED**· source *M §12.11.0; Mac Lane 1971*· depends on `K.comp`· 2 objects depend on it· depth 3

> **PRIOR ART: associativity of composition and the existence of identities are the category axioms — Mac Lane, Categories for the Working Mathematician (1971). Verifying them on 41,682 composable pairs checks that Lambda_9 IS a category; the axioms are not this work.**

### `K.clock` — the composition clock

**occupancy never rises along composition: 0 of 739 steps; the tick is k − g = (k−q) + (q−g)**

*destinations begin empty -- an assumption, not a constraint*

grade **COMPUTED**· source *M §12.11.0.1; classical; Floyd 1967*· depends on `K.comp`· 1 objects depend on it· depth 3

> **PRIOR ART: a quantity that never increases along composition is a MONOVARIANT, the standard tool for proving termination. That occupancy is one here is the measurement; the technique is old.  PRIOR ART: a quantity that never increases along composition is a variant function, the standard termination argument — Floyd, Assigning meanings to programs, Proc. Symp. Appl. Math. 19 (1967) 19-32.**

### `K.clockfail` — the clock that does not tick

**index (g,G) with g ≤ G ≤ 4f+2 and g ≤ q: 13,775 cells, closed, and 31.6% of composable pairs raise occupancy**

*prior occupancy carried as a coordinate*

grade **COMPUTED**· source *M §12.11.0.2; Floyd 1967*· depends on `K.clock`, `A.rule`· 1 objects depend on it· depth 7

> **PRIOR ART: a candidate variant that is closed but does not decrease is a failed termination measure. Floyd (1967).**

### `K.comp` — composition

**b∘a defined when tgt(a) = src(b); the composite transfers min(q_a, q_b)**

*Λ₉'s target (e,f,g,2S′) has the source's constraint forms*

grade **COMPUTED**· source *M §12.11.0; Mac Lane 1971*· depends on `T.a9`· 6 objects depend on it· depth 2

> **PRIOR ART: composition defined when target meets source is the category axiom; what is measured is that the composite transfers min(q_a, q_b), which is a property of this index and not of categories.**

### `K.corner` — corners and faces

**the whole-object defect decomposes into FACES and CORNERS, and the corners are an artefact of loose coordinatisation**

*an index of dimension d and its d-1 axis slices*

grade **MEASURED**· source *R 1177; Freuder 1978*· depends on `K.langclose`· depth 7

of the 6,195 cells R admits and Lambda_spectra does not hold, 3,993 are admitted by some three-axis slice and 2,202 by none. Statistics admits ONE of the 2,202 and geometry 28%, against 20% and 70% of the faces. And every available fifth coordinate makes the corners worse — by 70% to 652% — because all four candidates are DERIVED (register 1122)

> **PRIOR ART: cells admitted by the full closure and by no lower-arity projection are exactly the k-consistency gap — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### `K.coupling` — the refuted conjecture

**coordinate COUPLING does not predict redundancy**

*a closed index*

grade **MEASURED**· source *R 1120; Dechter & Pearl 1989*· depends on `K.redun`· depth 4

across six indices — Lambda, Lambda_spectra, the periodic table, Janet, the calendar, a box ordering — redundancy against coupling gives r^2 = 0.002, p = 0.94. Janet and the box ordering both have 50% coupling and 0% redundancy; Lambda_spectra has 17% coupling and 20% redundancy

> **PRIOR ART: that coupling alone does not predict what a local method achieves — the induced width, not the edge count, is the parameter. Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### `K.deadend` — the dead ends, defined

**the non-composable cells are defined exhaustively: at Lambda-10 all 485 have g = 0 and every g = 0 cell is non-composable; at Lambda-13, 11,188 at g = 0, 5,116 with 2J in {6,7,8} which no 2J_c can start, and 8,214 failing only in combination**

*L.c8 is k >= 1, so a target ending empty can never be a source; and 2J inherits 2K's range while 2J_c is bounded by phi(k) alone*

grade **COMPUTED**· source *M §12.11.1.5; Mac Lane 1971*· depends on `K.peak`· depth 6

> **PRIOR ART: cells that compose with nothing are those whose target is no other cell source — the non-composable part of a quiver.**

### `K.decay` — data-processing inequality + Pinsker

**for a tree-structured index, I(u;v) is non-increasing in tree distance d, and |P(A_u∩A_v) − P(A_u)P(A_v)| ≤ √(I(u;v)·ln2 / 2)**

*Markov random field on a tree; data processing; Pinsker*

grade **PROVED**· source *M §12.11.0.7; Lauritzen 1996; Pearl 1988*· depends on `K.markov`· depth 5

> **PRIOR ART: mutual information is non-increasing in tree distance because every path is separated — the data-processing inequality on a Markov tree. Cover & Thomas, Elements of Information Theory (1991), Thm 2.8.1; Lauritzen, Graphical Models (1996), ch. 3.**

### `K.girth` — the girth is four

**the girth of the unit-step graph on Λ₉ is exactly 4**

*unit-step adjacency = covering relation, 6,658 edges*

grade **PROVED**· source *T 4.3; classical graph theory; Berge 1962*· depends on `L.dist`· depth 9

> **PRIOR ART: girth is the length of the shortest cycle, standard since Euler. That a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves.  PRIOR ART: girth is the length of the shortest cycle; that a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves. Berge, Theorie des graphes (1958/1962).**

### `K.helly` — Helly number

**molecular transit is an intersection question; the Helly number is ≥ 5 and ≤ 144**

*a molecule moves as one fibre; a circuit is a square; ground set C(9,2)·4 = 144*

grade **COMPUTED**· source *T 4.4; Helly 1923*· depends on `K.comp`· depth 3

> **PRIOR ART: the Helly number of a family is the least h such that every h-wise intersecting subfamily intersects — Helly, Ueber Mengen konvexer Koerper mit gemeinschaftlichen Punkten, Jahresber. DMV 32 (1923) 175-176.**

### `K.jump` — the categorial jump

**the axis that makes the tower a category is worth twenty points: Lambda-8 is 50.3% composable and Lambda-9, adding 2S' <= g, is 70.7%**

*the companion's index sits between them at 59.5% — three transition indexes, three fractions, so this is not a norm*

grade **COMPUTED**· source *M §12.11.1.3; Mac Lane 1971*· depends on `K.twocol`· depth 5

> **PRIOR ART: the axis that closes composition is the one that supplies identities and associativity — the category axioms. What is priced is the cell cost of adding it.**

### `K.langclose` — closure as agreement

**E(X) = 0 if and only if the languages agree**

*an index of dimension >= 3 and two or more operators*

grade **MEASURED**· source *R 1176; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `K.three`· 1 objects depend on it· depth 6

six indexes, three operators — order, statistics, geometry. Lambda and a box ordering: E = 0 and every pair agrees, 0 cells differing. The periodic table, Janet, the calendar and Lambda_spectra: E > 0 and every pair differs. No exception. Closure is therefore a language-theoretic property as well as an order-theoretic one, and the language test is cheaper: R enumerates the ambient product, pairwise consistency needs only the marginals

> **PRIOR ART: global and local closures coincide exactly on acyclic structures — BFMY, J. ACM 30 (1983) 479-513. That E = 0 iff the languages agree is that theorem read as an equivalence.**

### `K.markov` — the Markov property

**the future is conditionally independent of the past given the transfer: every past gives the same future set at each q**

*the constraint graph is a tree, q the cut vertex*

grade **COMPUTED**· source *M §12.11.0.8; Lauritzen 1996; Pearl 1988*· depends on `C.cut`, `L.tree`· 1 objects depend on it· depth 4

> **PRIOR ART: the future being conditionally independent of the past given the present is the MARKOV PROPERTY. Its graphical form — separation in the graph implies conditional independence — is Lauritzen, Graphical Models (1996), ch. 3, and Pearl, Probabilistic Reasoning in Intelligent Systems (1988).**

### `K.peak` — the composability peak

**composability peaks at Lambda-10 and falls after: 0.0000, 0.7068, 0.8087, 0.6956, 0.6394, 0.6186 across Lambda-8 to Lambda-13**

*counting axes raise the fraction and coupling axes lower it, with no exception — §12.11.3's dichotomy predicts the sign as well as the price*

grade **COMPUTED**· source *M §12.11.1.4; Berge 1962*· depends on `K.twocol`· 1 objects depend on it· depth 5

> **PRIOR ART: the composability fraction is the arc density of the composition quiver; its rise and fall with the tower is the measurement.**

### `K.produce` — the production rule

**an axis PRODUCED by another gives a dimension exactly when its production is NOT MONOTONE**

*a closed index and an axis derived from its coordinates*

grade **MEASURED**· source *R 1143; Birkhoff 1937*· depends on `K.axis`· 2 objects depend on it· depth 5

multiplicity is produced by Ne and cycles 2,{1,3},2,{1,3},{2,4} — NOT monotone — and adding it takes redundancy from 20% to 82%. Ne is produced by (Z,charge) and monotone: 0%. n0 is produced by (Z,charge,l) and monotone: 0%. R's envelopes are cumulative maxima, so a monotonically-produced axis is already inside them; a non-monotone one is invisible to them. This resolves the apparent contradiction between R 1122 and R 1123

> **PRIOR ART: a monotone function of existing coordinates adds no join-irreducibles and so no dimension; a non-monotone one does. Birkhoff (1937).**

### `K.quiver` — the composition quiver

**composable cells are the arcs of a quiver Q on 33 objects; the composition graph is the line digraph L(Q), |E| = Σ_v in(v)·out(v) = 27,027**

*a loop at every vertex*

grade **COMPUTED**· source *T 4.2; Gabriel 1972*· depends on `K.cat`· depth 4

> **PRIOR ART: a quiver is a directed graph whose paths generate an algebra — Gabriel, Unzerlegbare Darstellungen I, Manuscripta Math. 6 (1972) 71-103. The composable cells form the arcs of one.**

### `K.redun` — the projection ladder

**redundancy under R rises with the number of INDEPENDENT coordinates; a DERIVED coordinate lowers it**

*a closed index X of dimension d*

grade **MEASURED**· source *R 1119-1122; Shannon 1948*· depends on `A.R`· 2 objects depend on it· depth 3

Lambda PROJECTED onto its own first d coordinates, same constraints: d=8 gives 61% removable with exact recovery, d=7,6,5 give 30%, d=4 gives 5%, d=3 gives 0%. And adding the electron count Ne = Z-c+1 to the spectra index — a FUNCTION of two coordinates it already has — drops redundancy from 20% to 0% while doubling the envelopes and raising coupling 17% to 33%

> **PRIOR ART: redundancy is the excess of a representation over its entropy. That it rises with the number of INDEPENDENT coordinates is the measurement; the notion is Shannon (1948).**

### `K.three` — the three-coordinate rule

**an index needs THREE coordinates before its languages can disagree**

*an index and two languages*

grade **PROVED**· source *R 1175; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.stat2`· 1 objects depend on it· depth 5

at d = 2 there is one coordinate pair, so pairwise consistency and the cell coincide and every language returns the same answer. The periodic table, Janet and the calendar were all tested at two and all reported agreement; rebuilt at three — with block, l and weekday, each non-monotone in the second coordinate — the periodic table gives order E = 100 against statistics 0, reproducing the book's recorded caveat. All three match the book at 2-D first: 36, 0 and 7

> **PRIOR ART: pairwise consistency is a statement about PAIRS, so an object with one pair cannot make it. BFMY (1983) for the general local-to-global framework.**

### `K.transit` — the transit profile

**the transit profile MI/H = 0.51, 0.93, 0.08, 0.13, 0.77 at Λ₉–Λ₁₃: reduced at 10, a label through 11 and 12, re-attaching at 13**

*Λ₁₂ built with the loose bound*

grade **COMPUTED**· source *M §12.11; Shannon 1948*· depends on `T.tower`· depth 7

> **PRIOR ART: MI/H is the normalised mutual information, standard since Shannon (1948).**

### `K.twocol` — space is what an index holds, time is what it composes

**an index has a time column exactly when its cells are moves: Lambda-8 976/0, Lambda-9 1,654/1,169, the companion's index 2,370/1,410, while the periodic table and the calendar have no second column and cannot have one**

*a transition cell has two ends so composability is askable; a state cell has one position and the question does not arise*

grade **COMPUTED**· source *M §12.11.1.3; Mac Lane 1971*· depends on `K.cat`· 3 objects depend on it· depth 4

> **PRIOR ART: an index has a composition structure exactly when its cells are morphisms rather than objects — the distinction is the category axioms. Mac Lane (1971). CORRECTED 2026-08-11: this statement printed Lambda-8 as 976/491. It is 976/0. The generated table in INDICES.md gives 0 with fraction 0.0000, indices.py says 'Lambda-8 composes not at all — four source coordinates against three target', and K.window states the reason as a dependency: 'Lambda-8 target has 3 coordinates against 4', so tgt(a) = src(b) is not even askable at Lambda-8 and Lambda-9 is the FIRST composable level. The 491 was a hand-authored figure in an object graded COMPUTED, contradicting the computation it depends on.**

### `K.window` — the composable window

**Λ₉ is the first composable level and the last tree level**

*Λ₈ target has 3 coordinates against 4; Λ₁₀ has 10 nodes and 10 edges*

grade **COMPUTED**· source *T 4.1; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `K.comp`, `L.tree`· depth 3

> **PRIOR ART: that treeness and composability are different properties, and that an index can be the last of one and the first of the other, is the acyclicity/local-consistency distinction of BFMY, J. ACM 30 (1983) 479-513.**

### `K.zcross` — the periodic table as a coordinate

**composability is 22.71% within one element and 85.23% across the 118, while E is 28,503 without Z and 972,862 with it**

*composability wants the whole table and closure wants one atom; Lambda closes because it has no Z*

grade **COMPUTED**· source *M §12.11.1.6; Edlen 1964*· depends on `K.twocol`· 1 objects depend on it· depth 5

> **PRIOR ART: that composability is far higher across elements than within one is the isoelectronic structure — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964).**

## M. The modular chain — 9 objects

### `M.C1` — the presymplectic potential

**the presymplectic potential θ = δφ £_ℓφ η carries no transverse derivative, so Ω is block diagonal in y and {φ(u,y),φ(u′,y′)} = (1/4√q(y))sgn(u−u′)δ^{d−2}(y−y′)**

*u-independent transverse metric, i.e. Θ = 0; non-derivative interactions only*

grade **COMPUTED**· source *T 10.4c, F1, F2; Wald & Zoupas 2000*· depends on `M.hsmi`· 2 objects depend on it· depth 3

> **PRIOR ART: the presymplectic potential and its ambiguities are Wald & Zoupas, General definition of conserved quantities in general relativity, Phys. Rev. D 61 (2000) 084027.**

### `M.C2` — the open object — half-sided modular inclusion on a non-expanding horizon · **GRADED OPEN**

**Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂) for t ≤ 0, u₁ < u₂, WITH Ω cyclic and separating for BOTH M(u₁) and M(u₂)**

*N a non-expanding horizon with no Killing field, ω Hadamard*

grade **OPEN**· source *T 10.4d, F6*· depends on `M.C1`, `M.hsmi`· 1 objects depend on it· depth 4

REGRADED CONDITIONAL 2026-08-11 (R 1507). This object is NOT open. It is PROVED on one existence hypothesis, in nine steps NONE of which uses a Killing field: P_lambda >= 0 from the ANEC on ACHRONAL generators (R 1471); U(s) unitary by Stone; U(s) B U(s)-dagger inside B because the cut translates into itself, which is CAUSAL structure (R 1506); U(s)Omega = Omega from the hypothesis; C_lambda = U(1) B U(1)-dagger, the source own equation; Omega cyclic for C_lambda since C_lambda Omega = U(B Omega) with U unitary and B Omega dense (R 1501); separating since C_lambda is inside B; hence the four Borchers conditions, hence HSMI by Borchers 1992 and Wiesbrock 1993. THE HYPOTHESIS: there exists a state annihilated by every smeared ANE operator and cyclic and separating for the exterior algebra. A Killing horizon supplies it (Hartle-Hawking); a non-expanding horizon is not known to. So the isometry supplies a WITNESS, not a step. The open question is a CONTAINMENT between two classes of spacetimes, not a parameter. STATEMENT COMPLETED 2026-08-11 (R 1481): the standardness clause was missing. A half-sided modular inclusion is N inside M with a vector Omega CYCLIC AND SEPARATING FOR BOTH, and sigma_t(N) inside N for t <= 0 — Lechner-Scotford Def 2.1, equivalent to the Borchers triple by Borchers 1992 and Wiesbrock 1993. This object stated only the inclusion clause. The omitted clause is exactly the one Faulkner and Speranza ASSUME rather than derive — arXiv 2405.00847 sec 3.1 says, of the smaller algebra, assuming Omega is cyclic for it — and Reeh-Schlieder does not supply it, because their Omega is a vacuum for the average null energy operators and, in their own words, may not coincide with a global minimal energy state. Araki and Zsido, Rev. Math. Phys. 17 (2005) 491-543, extend Wiesbrock to weights and fill a gap in the 1993 proof. OPEN on the GEOMETRIC route only. M.sorce closes it by construction — a geometric modular flow needs a conformal Killing vector and a non-expanding horizon has none; Chandrasekaran & Flanagan (arXiv:2601.07915) have the Killing case. The ALGEBRAIC route is not blocked: M.hsmi characterises HSMI by a one-parameter unitary group with positive generator and mentions no Killing field, and M.C1's commutator is already an algebraic object. That route was ATTEMPTED (R 1018-1022): its free half goes through — M.C1's commutator gives a positive generator per null generator, negative/positive spectral weight 5e-5, so a standard pair exists per generator and block diagonality keeps them unmixed. The obstruction is in the CORNER EDGE MODES, where Chandrasekaran & Flanagan show the null translation generator is necessarily two-sided. A proposal that Theta = 0 supplies the missing relative boost was tested and FAILS: theta_ab -> a(y) theta_ab under l -> a(y)l, so theta = 0 is invariant under the rescaling and cannot fix its parameter. The paper's OWN route (Sec 7.3) supplies the boost from SMOOTHNESS instead — local Rindler frames give chi = kappa(u d_u - v d_v) with grad_(mu chi_nu) = O(u,v), and footnote 44 says a local boost Killing field is all that is needed. It establishes the modular flow's geometric action TO FIRST ORDER at any cut and states explicitly that these CANNOT be patched together. M.C2 needs finite u1 < u2. The reduction bottoms out at POSITIVITY of the null translation generator, and that is NOT implied by Hadamard: Hadamard is microlocal (a wavefront-set condition) while positivity is a global spectral one, and a smooth deformation of the vacuum raises negative/positive spectral weight from 4.8e-05 to 2.6e-03 while changing the UV tail by 0.0000%. Thermal states are Hadamard and carry both signs. Positivity is a SELECTION CRITERION assumed by everyone who needs it — Chandrasekaran-Flanagan Sec 8 and Dappiaggi-Moretti-Pinamonti both — and Kay-Wald 1991 get uniqueness only for states INVARIANT UNDER THE KILLING FLOW, the hypothesis M.C2 drops. CORRECTION (R 1038-1042): the hypothesis is NOT purely geometric — the standard NEH definition's third condition is 'Einstein field equations hold on Delta and -T^a_b l^b is future causal', an energy condition on the state, which via Raychaudhuri forces T_ab l^a l^b = 0 and sigma_ab = 0, hence L_l q_ab = 0 — which is M.C1's hypothesis, so M.C1 assumes a consequence of the definition. The shortfall is ORDER: the condition fixes the background, while half-sidedness is spectral on the perturbations

### `M.hsmi` — Borchers 1992 / Wiesbrock 1993

**half-sided modular inclusion is CHARACTERISED by a one-parameter unitary group with positive generator**

*common cyclic separating vector; extended to weights by Araki–Zsidó 2004*

grade **CITED**· source *T E2, E3; Borchers 1992; Wiesbrock 1993*· depends on `M.tt`· 2 objects depend on it· depth 2

> **PRIOR ART: half-sided modular inclusion and its characterisation by a one-parameter group with positive generator — Borchers, The CPT theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Lett. Math. Phys. 28 (1993) 107-114.**

### `M.ledger` — the modular ledger

**d − 1 = 1 + (d − 2) ON THE FREE ALGEBRA: one HSMI per generator supplies the affine line; the transverse direct integral is C1 and no HSMI supplies it. INCOMPLETE ON THE DRESSED ALGEBRA, which carries doubled corner modes besides**

*a null hypersurface in d dimensions — THIS IS A MANIFOLD COUNT, NOT AN ALGEBRA COUNT (R 1484)*

grade **COMPUTED**· source *T 10.4e, F7; Borchers 1992; Wiesbrock 1993*· depends on `M.C1`, `M.C2`· depth 5

COMPLETED 2026-08-11 (R 1484): the sum is TWO accountings. LEVEL ONE, the manifold, is what this object counts and it is correct. LEVEL TWO, the algebra, carries the corner content, and register 1020 writes it exactly: the residual freedom is l -> a(y) l, acting on the affine parameter as u -> u/a(y) + b(y). Those are two arbitrary FUNCTIONS ON THE CUT, not DIMENSIONS OF A MANIFOLD, so no arithmetic sum can hold them and none should be attempted. R 1022 named what would close M.C2 — a canonical scaling of the affine parameter — which is a(y). QUALIFIED 2026-08-11 (R 1483): the sum is the FREE count and was stated without the qualifier. Register 1019, which M.C2 own check already cites, records that half-sidedness fails on the DRESSED algebra and not the free one, and that Chandrasekaran and Flanagan recover it by EXTENDING THE PHASE SPACE WITH DOUBLED CORNER MODES — relative boosts AND null translations of the respective corners. Those modes belong to the affine family and the transverse family at once, so they are not a summand but an OVERLAP, and 1 + (d-2) does not count them. This object mentioned neither corner nor edge mode nor two-sided nor either author. dimensional_ledger — and the ledger IS the kinematic/stateful decomposition (R 1035): the STATEFUL object (HSMI, hence M.C2) supplies exactly ONE dimension, the affine line; the KINEMATIC one (M.C1, Theta = 0) supplies the other d-2. Read as a counting argument until then

> **PRIOR ART: one half-sided modular inclusion per generator supplies the affine line — the Borchers-Wiesbrock theorem, Borchers, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Lett. Math. Phys. 28 (1993) 107-114.**

### `M.rs` — Reeh–Schlieder

**the vacuum is cyclic and separating for local algebras**

*Hadamard state; region with nonempty causal complement*

grade **CITED**· source *T E0; Reeh & Schlieder 1961*· 1 objects depend on it· depth 0

> **PRIOR ART: the vacuum is cyclic and separating for local algebras — Reeh & Schlieder, Bemerkungen zur Unitaeraequivalenz von Lorentzinvarianten Feldern, Nuovo Cim. 22 (1961) 1051-1068.**

### `M.semi` — semifinite carries a trace

**a semifinite factor carries a trace, hence an entropy; type III carries none**

*von Neumann classification*

grade **CITED**· source *T E5; Murray & von Neumann 1936*· depends on `M.takesaki`· depth 3

> **PRIOR ART: the type classification of factors, and that only semifinite ones carry a trace, is Murray & von Neumann, On rings of operators, Ann. Math. 37 (1936) 116-229, and its sequels.**

### `M.sorce` — Sorce 2024

**any geometric modular flow must be generated by a conformal Killing field**

*general*

grade **CITED**· source *T 10.4; Sorce 2024*· depends on `M.tt`· depth 2

> **PRIOR ART: that a geometric modular flow must be generated by a conformal Killing field — Sorce, Analyticity and unitarity for cosmological correlators (2024) and related work on geometric modular flow.**

### `M.takesaki` — Takesaki duality 1973

**N = M ⋊_{σ^φ} ℝ is type II_∞ with trace τ, τ∘θ_s = e^{−s}τ, and M = N ⋊_θ ℝ uniquely**

*M type III, φ a faithful semifinite normal weight; STATED FOR ℝ*

grade **CITED**· source *T E4; Takesaki 1973*· depends on `M.tt`· 1 objects depend on it· depth 2

> **PRIOR ART: the structure theorem for type III factors as crossed products — Takesaki, Duality for crossed products and the structure of von Neumann algebras of type III, Acta Math. 131 (1973) 249-310.**

### `M.tt` — Tomita–Takesaki

**for (M,Ω) there exist Δ, J with Δ^{it} M Δ^{−it} = M**

*M a von Neumann algebra, Ω cyclic and separating*

grade **CITED**· source *T E1; Tomita 1967; Takesaki 1970*· depends on `M.rs`· 3 objects depend on it· depth 1

> **PRIOR ART: Tomita-Takesaki modular theory — Tomita, Quasi-standard von Neumann algebras (1967, unpublished); Takesaki, Tomita Theory of Modular Hilbert Algebras and its Applications, Springer LNM 128 (1970).**

## W. The violation index — 9 objects

### `W.core15` — the core at fifteen letters

**at fifteen letters: 18,072 cells, E = 816 = 1 × 816, core (X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)**

*the split alphabet of T §6.5*

grade **COMPUTED**· source *T 7.1; Chinneck & Dravnieks 1991*· depends on `W.core9`· 1 objects depend on it· depth 5

> **PRIOR ART: as W.core9 at a finer alphabet. That the core is unchanged while the multiplicity grows is the measurement; the notion of an irreducible infeasible subsystem is theirs.**

### `W.core9` — the core at nine letters

**at nine letters: 2,370 cells, E = 30 = 1 × 30, core (X=0, U=0, NEC=3)**

*the coordinate set of T §5.1*

grade **COMPUTED**· source *T 5.3; Chinneck & Dravnieks 1991*· depends on `A.E`· 3 objects depend on it· depth 4

cell count RECOMPUTED: the 17 rules of vi_best.json applied to the 4·3·3·3·5·2·2·3·3 box give exactly 2,370. E=30 is the arity-4 CONSTRAINT-LANGUAGE defect (NEC>=3 -> IC v U v X), not the envelope defect of the cell set, which is 3,040 (R 1009)

> **PRIOR ART: a minimal set of conditions whose joint failure is irreducible is a MINIMAL UNSATISFIABLE SUBSET — Chinneck & Dravnieks, Locating minimal infeasible constraint sets in linear programs, ORSA J. Comput. 3 (1991) 157-168; in SAT the same object is the MUS. The conditions themselves are physics: the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950) and the equations of motion.**

### `W.face` — the null surface is a face

**the companion's local null surface is a FACE of the 6-cube, not a parity class: 32 of 64 with every rung 2, and a parity class gives E = 32 where the printed E is 0**

*deducible from three printed numbers with no access to any cell; THETA = 0 at 16 and STAT = 0 at 8 nest Killing horizons inside non-expanding ones*

grade **COMPUTED**· source *T §10.1, §10.4; Coxeter 1948*· depends on `A.R`· depth 3

> **PRIOR ART: a face of the n-cube is the set fixing some coordinates and freeing the rest — Coxeter, Regular Polytopes (1948), ch. VII. A parity class is not a face, which is what distinguishes them here.**

### `W.frontier` — the frontier metric — distance and status on the fifteen-letter alphabet

**d(c) = X_exp + U_ghost + |NEC_pt−3| + EOM + d_P; s(c) = 1{·}+1{·}+1{·}+1{·} + s_P**

*the fifteen-letter alphabet; d_P the L1 distance on the eleven free letters*

grade **DEFINITIONAL**· source *T D7, D8; classical; Hamming 1950*· depends on `W.core15`· depth 6

> **PRIOR ART: a defect built as a sum of independent violation counts, with a support counted separately, is the standard form of a penalty function.  PRIOR ART: a defect built as an L1 distance on free letters plus a count of violated conditions is a Hamming-type distance with weights — Hamming, Error detecting and error correcting codes, Bell Syst. Tech. J. 29 (1950) 147-160.**

### `W.jur` — jurisdiction does not change the defect

**a jurisdicted forcing and an unjurisdicted disjunction give identical defects; arity ≥ 3 makes a defect possible, jurisdiction narrowness makes it small**

*the scope condition is a coordinate*

grade **COMPUTED**· source *T 8.2; Freuder 1978*· depends on `W.supp`· depth 9

> **PRIOR ART: that a constraint of arity 3 or more is not captured by binary projections is the k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966. Whether a scope condition is jurisdicted or disjunctive does not change the arity, hence not the defect.**

### `W.onehot` — the one-hot partition

**status is one bit per vocabulary and the partition forces one-hot: 35 of 40 terms weight 1, 2 weight 0, 3 weight 2**

*weight 2 = relation or unsplit conflation; weight 0 = ungrounded or constructible*

grade **COMPUTED**· source *T 10.5; classical; Shannon 1938; classical*· depends on `W.rel`· depth 4

partition RECOMPUTED: 35 + 2 + 3 = 40 terms, total weight 41 (R 1009)

> **PRIOR ART: a partition of a set forces exactly one indicator to be set — the one-hot encoding. Elementary, and the measurement is that 35 of 41 statuses satisfy it.  PRIOR ART: a partition forces exactly one indicator — the one-hot encoding of Boolean algebra, Shannon, Trans. AIEE 57 (1938) 713-723. Weight 2 signals a relation or a conflation; weight 0 an ungrounded term.**

### `W.rel` — Brunetti–Fredenhagen–Verch 2003

**a term that is a relation between two vocabularies cannot be a coordinate of either**

*the BFV partition A : Loc → Alg has four parts*

grade **COMPUTED**· source *T 8.4; Brunetti, Fredenhagen & Verch 2003*· depends on `A.R`· 1 objects depend on it· depth 3

> **PRIOR ART: a term that is a relation between two vocabularies is a morphism, not an object — the locally covariant framework of Brunetti, Fredenhagen & Verch, The generally covariant locality principle, Commun. Math. Phys. 237 (2003) 31-68, makes the distinction precise.**

### `W.scale` — the defect does not scale

**the defect does not scale: core = 1 at 4, 5, 7 and 9 coordinates; only the multiplicity moves (3,5,10,30)**

*projections of one index*

grade **COMPUTED**· source *T 5.7; Chinneck & Dravnieks 1991*· depends on `W.core9`· depth 5

> **PRIOR ART: that the core of an infeasible system is invariant under refining the encoding is the well-definedness of the MUS; only the multiplicity of witnesses changes.**

### `W.supp` — the core is minimal

**of 414 coordinate subsets excluding {X,U,NEC}, 0 fail: the triple is the unique minimal failing subset, arity exactly 3. THE COUNT RECONCILES — subsets of size 2..6 at d = 9 number exactly 414 — but the convention is unprinted and the failure count needs the cells. Arity 3**

*as W.core9*

grade **COMPUTED**· source *T 5.4; Chinneck & Dravnieks 1991*· depends on `W.core9`, `A.modeB`· 1 objects depend on it· depth 8

combinatorics RECOMPUTED: subsets of size 2..6 from 9 coordinates number 456; those containing all of {X,U,NEC} number 42; 456-42 = 414 exactly as stated (R 1009)

> **PRIOR ART: testing all 414 subsets and finding none fails without the triple establishes MINIMALITY in their sense — no proper subset is infeasible.**

## EM. The electromagnetic quotient — 7 objects

### `EM.cross` — the selection-rule crossing

**EM-allowed cells compose at 11.6% within one element against the forbidden 40.7%, and the order reverses across the table at 89.7% against 77.9%**

*the rule that forbids composition inside an atom is the rule that enables it between atoms; parity repeats it at 38.4% against 20.1%*

grade **COMPUTED**· source *M §12.11.1.7; Laporte 1924*· depends on `K.zcross`· depth 6

> **PRIOR ART: the composability contrast between allowed and forbidden cells is a consequence of the parity rule; the measurement is the fraction.**

### `EM.image` — the complete rectangle

**Λ₉'s image on (multipole, ΔS) is the COMPLETE rectangle at every cap; E = 0 vacuously**

*as EM.map*

grade **COMPUTED**· source *M §12.11.8; Wigner 1927*· depends on `EM.map`, `A.dens`· depth 5

> **PRIOR ART: that the selection rules cut a complete rectangle in (multipole, Delta S) is the product structure of the space-spin decomposition. Wigner, Z. Phys. 43 (1927) 624.**

### `EM.map` — electric/magnetic multipole selection rules

**the multipole is determined by |Δl| and parity alone: 0->M1, 1->E1, 2->E2, 3->E3**

*one-electron jump; no source J exists in Λ*

grade **COMPUTED**· source *M §12.11.8; Laporte 1924; Condon & Shortley 1935*· depends on `L.def`· 5 objects depend on it· depth 2

> **PRIOR ART: the multipole order of a transition is fixed by |Delta l| and parity — Laporte, Z. Phys. 23 (1924) 135; the full multipole classification is Condon & Shortley (1935), ch. IV.**

### `EM.notcomp` — selection and composition are unrelated

**composability and the EM condition share 0.0004 bits of a possible 0.633**

*on Λ₉'s cells*

grade **COMPUTED**· source *M §12.11.8; Shannon 1948*· depends on `EM.map`, `K.comp`· depth 3

> **PRIOR ART: shared information between two binary properties, in bits. Shannon (1948).**

### `EM.parity` — the parity hole

**|Δl| = 1 is delta^-1({-1,+1}), a hole at zero, not convex; E = 750**

*as EM.spin*

grade **COMPUTED**· source *M §12.11.8; Laporte 1924; Wigner 1927*· depends on `EM.map`, `I.convex`, `T.excl`· depth 11

> **PRIOR ART: the parity selection rule |Delta l| = 1 for electric dipole radiation is Laporte, Z. Phys. 23 (1924) 135, and its group-theoretic ground is Wigner, Z. Phys. 43 (1927) 624.**

### `EM.quotient` — the electromagnetic quotient

**the EM index is a QUOTIENT of Λ, not an extension: adjoining its coordinates gives E = 3,900**

*every EM coordinate is a function of Λ's own*

grade **COMPUTED**· source *M §12.11.8; Noether 1918*· depends on `EM.map`, `A.derived`· depth 5

> **PRIOR ART: a selection rule is a quotient by a symmetry, not an extension of the state space. Noether, Invariante Variationsprobleme, Nachr. Ges. Wiss. Goettingen (1918) 235-257, is the general statement of the correspondence between symmetry and conserved structure.**

### `EM.spin` — the spin diagonal

**ΔS = 0 is a diagonal, hence two monotone one-parent bounds; imposing it preserves E = 0 at four cap settings**

*LS coupling*

grade **COMPUTED**· source *M §12.11.8; Russell & Saunders 1925; Wigner 1931*· depends on `EM.map`, `I.convex`· depth 11

> **PRIOR ART: Delta S = 0 for electric dipole transitions in LS coupling is the spin selection rule — Russell & Saunders, Astrophys. J. 61 (1925) 38; Wigner, Gruppentheorie (1931), for the representation-theoretic statement.**

## C. Protocol and audit objects — 9 objects

### `C.Aq` — the first factor

**A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k (1−z^{min(k,3)+1})/(1−z)**

*caps as stated; q held fixed*

grade **COMPUTED**· source *M §12.7 / T C2eq; Euler 1748; Stanley 1986*· depends on `L.F`· 1 objects depend on it· depth 4

> **PRIOR ART: a nested sum over a constrained region, written as a polynomial in z, is the standard rank-generating construction. Euler (1748) for the method; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1, for the modern treatment.**

### `C.Bq` — the second factor

**B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f (1−z^{min(q,4f+2)+1})/(1−z)**

*as C.Aq*

grade **COMPUTED**· source *M §12.7 / T C3eq; Euler 1748; Stanley 1986*· depends on `L.F`· 1 objects depend on it· depth 4

> **PRIOR ART: as C.Aq — the second factor of the fibred count, built the same way.**

### `C.box` — the box generating function

**Box(a,b)(z) = ∏_i z^{a_i}(1−z^{b_i−a_i+1})/(1−z)**

*every fibre bottoms out in a product of chains*

grade **DEFINITIONAL**· source *M §12.7.2 / T C4eq; Euler 1748*· depends on `C.Aq`, `C.Bq`· depth 5

> **PRIOR ART: the generating function of a box is a product of finite geometric series — Euler, Introductio in analysin infinitorum (1748), ch. XVI, where partition generating functions are introduced.**

### `C.compare` — the comparison audit

**the COMPARISON AUDIT: index, math and language cypher checked against one another, not each against itself**

*any two indexes and the cypher*

grade **MEASURED**· source *R 1169-1172; Tarski 1936; Beeri, Fagin, Maier & Yannakakis 1983*· depends on `A.R`, `K.produce`· depth 6

three checks. COVERAGE: every index coordinate has a math object and every family an index part — 0 and 0. LANGUAGE: five index/language pairs never run — Lambda_spectra in geometry, algebra, information and statistics, Lambda_alpha in analysis. CONTRADICTION: three standing, all on Lambda_spectra between ORDER and ANALYSIS — delta falls with l (194/205 vs 102/205), triplet exceeds singlet (55/66 vs 33/66), delta falls along a sequence (89/143 vs 135/143). The audit names the pair and does NOT adjudicate

> **PRIOR ART: comparing two formal readings of one object and requiring agreement is the metalanguage move (Tarski 1936); that global and local readings agree exactly on acyclic structures is BFMY (1983).**

### `C.cut` — every cut closes

**every two-sided cut of the tree gives defect zero, not only q**

*the tree is doing the work, not the transfer*

grade **COMPUTED**· source *M §12.11.0.8; Freuder 1982*· depends on `C.fib`, `L.tree`· 1 objects depend on it· depth 3

> **PRIOR ART: every two-sided cut of a tree separates it, so the defect vanishes at each — Freuder, J. ACM 29 (1982) 24-32.**

### `C.fib` — the fibred count

**|Λ| = Σ_q |A(q)|·|B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 976**

*conditioned on the transfer q*

grade **COMPUTED**· source *M §12.6.1 / T C1eq; Fubini 1907*· depends on `L.def`· 4 objects depend on it· depth 2

> **PRIOR ART: summing a product over a fibration of the index set is the discrete Fubini theorem. That the fibres here are independent is what makes |Lambda| factor as a sum of products.**

### `C.local` — local closure is not implied

**E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q; the second does not follow from the first**

*cross-sections with induced coordinates*

grade **COMPUTED**· source *M §12.8.5 / T C5eq; Rota 1964*· depends on `C.fib`, `A.E`· depth 4

> **PRIOR ART: that a global count factorises over a decomposition does not imply each part is separately closed — the failure of naive Moebius inversion over non-independent parts. Rota (1964).**

### `C.pareto` — the fibre trade

**|A(q)| falls 33,33,23,8 while |B(q)| rises 5,10,15,17; no q improves both**

*at stated caps*

grade **COMPUTED**· source *M §12.8.1; Pareto 1896*· depends on `C.fib`· depth 3

> **PRIOR ART: no q improves both factors — a Pareto front in the two counts. Pareto, Cours d economie politique (1896).**

### `C.qmean` — the transfer distribution

**⟨q⟩ = 1.4631, sd 0.930; peak at q = 2 with 345 cells (35.3%)**

*at stated caps*

grade **COMPUTED**· source *M §12.8.2; classical; Gauss 1809*· depends on `C.fib`· depth 3

> **PRIOR ART: the first and second moments of a distribution over a coordinate; elementary.  PRIOR ART: first and second moments of a distribution over a coordinate. Gauss, Theoria motus (1809).**

## I. The intake — interval maps and convexity — 3 objects

### `I.convex` — the convexity criterion

**delta^-1(T) is a sublattice iff T intersect range(delta) is convex in range(delta)**

*as I.interval*

grade **PROVED**· source *M §17.3; Birkhoff 1937*· depends on `I.interval`, `T.excl`· 2 objects depend on it· depth 10

> **PRIOR ART: the preimage of a set under a lattice homomorphism is a sublattice iff the set is convex in the image — the standard sublattice criterion. Birkhoff, Lattice Theory (1940), ch. II.**

### `I.interval` — the interval map

**delta = f - l is an INTERVAL MAP: min(da,db) <= delta(a v b), delta(a ^ b) <= max(da,db)**

*a sublattice of a product of chains*

grade **PROVED**· source *M §17.3; Birkhoff 1940*· depends on `L.dist`· 1 objects depend on it· depth 9

> **PRIOR ART: a difference of two coordinates is an INTERVAL MAP on a distributive lattice — it need not be a homomorphism but it is bounded above and below by the coordinatewise extremes. Standard; Birkhoff, Lattice Theory (1940).**

### `I.shape` — the shape of an interval

**between any two points there is an interval and the method returns its measure; three objects, one shape**

*cells, states under composition, measurements*

grade **COMPUTED**· source *M §9.2; Birkhoff 1940; Birkhoff 1940; Monjardet 1981*· depends on `L.occ`, `K.comp`, `B.brk`, `A.slack`· depth 6

> **PRIOR ART: between any two points of a lattice lies the interval [a and b, a or b]; the method returns its measure. Elementary lattice geometry.  PRIOR ART: between any two lattice points lies the interval [a and b, a or b]; its measure on a product of chains is the product of coordinate spans. Birkhoff, Lattice Theory (1940), ch. II; Monjardet, Discrete Math. 35 (1981) 173-184.**

## P. The spectral mechanisms — what moves a defect and by how much — 17 objects

### `P.buildlimit` — constructed limit

**a limit can be built from two spectra and tested by convergence**

*a series converging on a state above its own ionisation threshold*

grade **MEASURED**· source *R 711, 712; Edlen 1964*· depends on `P.converge`, `P.lcollapse`· depth 2

Ne I 2s.2p6.np on 173,929.75 + 217,047.598 gives +0.8408 +/- 0.0191 over ten

> **PRIOR ART: constructing a limit by summing the ionisation energies of successive stages is standard spectroscopic practice. Edlen, Handbuch der Physik XXVII (1964).**

### `P.charge` — the same-element ladder

**at s and p the quantum defect falls with charge at FIXED ELEMENT**

*a fixed element with two or more charge states*

grade **MEASURED**· source *R 963; Edlen 1964*· depends on `P.qdt`· depth 1

37 of 37 monotone at l<=1, no exceptions; all nine failures are at l>=2 where P.dcollapse governs

> **PRIOR ART: the fall of the defect with ionisation stage along an isonuclear sequence is standard spectroscopy — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### `P.converge` — self-determined limit

**a Rydberg series measures its own ionisation limit**

*enough members that the fit is determined*

grade **MEASURED**· source *R 684, 685, 686, 698, 699; Rydberg 1890; Ritz 1903*· depends on `P.qdt`· 1 objects depend on it· depth 1

38 of 58 put the published limit within 3x the fit own error; only 15 of 58 within the PUBLISHED error (R 812-813)

> **PRIOR ART: extrapolating a Rydberg series to its limit is the classical method of determining an ionisation energy — Rydberg (1890), Ritz (1903).**

### `P.coreblind` — parent-term independence

**delta depends on l and the core's charge, not on the core's STATE**

*two parent terms of one species*

grade **MEASURED**· source *R 709, 710, 743; Seaton 1958*· depends on `P.qdt`· depth 1

TWO instances; and CONTRADICTED IN PRINCIPLE by MQDT, which defines the defect as mu_(l,lambda,alpha+) depending on the core state (R 947)

> **PRIOR ART: single-channel quantum defect theory treats the core as a fixed phase shift, so delta depends on l and the core charge only. Its failure for multi-channel cases is Seaton MQDT (Rep. Prog. Phys. 46, 1983).**

### `P.dcollapse` — orbital collapse

**an orbital collapses at the onset of its shell and leaves the Rydberg series**

*3d across the transition row, 4f across the lanthanides*

grade **MEASURED**· source *R 719, 734, 735, 736; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969*· depends on `P.iso`· depth 2

all ten P.iso exceptions are d and small; Ba III 4f gives 1.0 against neon's 0.006

> **PRIOR ART: orbital collapse at the onset of a shell — Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187; Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71.**

### `P.iso` — the isoelectronic ladder

**for one element and l, delta falls as the core charge rises**

*defect large enough to exceed its own scatter*

grade **MEASURED**· source *R 708, 716, 717, 718*· depends on `P.qdt`· 1 objects depend on it· depth 1

8 of 9 s/p ladders exact; and a form delta = a + b*ln(c+1)/c fits the Mg-like ns ladders to 2% of range and predicts out-of-sample, but FAILS on nd, nf and all He-like ladders (47-65%); the method is Edlen 1964 (R 942-945)

### `P.jj` — the coupling-scheme marker

**J-inconsistency within one series marks where LS coupling has failed**

*same series, different J*

grade **MEASURED**· source *R 703; Condon & Shortley 1935*· depends on `P.qdt`· depth 1

114 of 129 consistent on raw levels, interval 82-93%; heavy elements fail at 23% against light at 8% (R 818-819)

> **PRIOR ART: the transition from LS to jj coupling as the spin-orbit interaction grows with Z is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. X.**

### `P.jsplit` — the j-splitting

**delta splits by the outer electron's own j when there is something to couple to**

*an OPEN-SHELL core, or Z large enough for the electron's spin-orbit*

grade **MEASURED**· source *R 754, 756, 757, 758, 759; Sommerfeld 1916*· depends on `P.qdt`· depth 1

median 0.0454 over 19 open/heavy pairs against 0.0002 over 10 closed/light — 227x

> **PRIOR ART: fine-structure splitting of a term by J is Sommerfeld, Zur Quantentheorie der Spektrallinien, Ann. Phys. 51 (1916) 1-94, in its relativistic form; Dirac (1928) supplies the exact theory.**

### `P.lcollapse` — the l-collapse

**delta falls monotonically with l and reaches zero by f**

*unperturbed series*

grade **MEASURED**· source *R 693, 702, 713, 724; Hartree 1928; Seaton 1958*· depends on `P.qdt`· 2 objects depend on it· depth 1

229 of 230 adjacent-l pairs correct, judged against EACH PAIR'S OWN 2 sigma rather than a fixed tolerance. The test carried an unstated slack of 0.02 until R 1072; at a fixed 0.02 it reads 251/251, strictly 242/251. The one failure is He I p->d, whose p defect is NEGATIVE — the Appendix B omission of R 871, which could not be recomputed when the reduced-mass Rydberg was corrected (R 1072-1074)

> **PRIOR ART: the defect falls with l because the centrifugal barrier keeps the electron out of the core — the standard penetration argument, Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89, and Seaton (1958).**

### `P.lens` — the precision lens

**near the limit delta is measured through a lens worsening as n^3**

*delta depends on (limit - E), which shrinks as n^2 while level error does not*

grade **MEASURED**· source *R 749, 750, 751, 752; Rydberg 1890*· depends on `P.qdt`· depth 1

WEAK at scale: only 44 of 79 channels show a wider high half (56%), and the n^3 prediction of 4.2x is observed at 1.3x (R 827)

> **PRIOR ART: near the limit dT/dnu ~ nu^-3, so a fixed energy uncertainty maps to a defect uncertainty growing as nu^3. Direct from the term formula.**

### `P.mono` — the monotonicity of the defect

**the defect approaches delta_0 monotonically: PENETRATION series fall, POLARISATION series rise**

*steps resolvable against their own uncertainty*

grade **MEASURED**· source *R 806, 821-824; NIST Atomic Spectroscopy compendium; Ritz 1903*· depends on `P.qdt`· depth 1

penetration (|d|>=0.1) falls 146 of 163 = 92%; polarisation (|d|<0.01) RISES 52 of 52 = 100%; combined 94% against 66% as a single claim (R 985-987)

> **PRIOR ART: the extended Ritz formula has a positive second coefficient for penetration and a negative one for polarisation, so the approach to delta_0 is monotone from above or below. Stated in NIST compendium.**

### `P.perturb` — series perturbation

**a large spread measures a perturber, not bad data**

*a state of the same symmetry crossing the series*

grade **MEASURED**· source *R 696, 704, 741, 742; Fano 1961; Lu & Fano 1970*· depends on `P.qdt`· depth 1

Si I nd spreads 0.15-0.21 where ASD's own leading-percentage column names 3s3p3 at 14%

> **PRIOR ART: a perturbed Rydberg series is a series crossed by a level of another channel — Fano, Effects of configuration interaction on intensities and phase shifts, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Graphic analysis of perturbed Rydberg series, Phys. Rev. A 2 (1970) 81-86.**

### `P.polar` — core polarisation

**beyond l=3 the defect follows core POLARISABILITY in direction, not in magnitude**

*l >= 4, where the orbital does not reach the core*

grade **MEASURED**· source *R 731-733, 788, 792-795; Born & Heisenberg 1924; Seaton 1958*· depends on `P.lcollapse`· depth 2

grows with Z at +0.0005/unit over seven elements; a quantitative alpha_d fit was attempted and did NOT work, cause undiagnosed (R 794)

> **PRIOR ART: core polarisation as the source of the high-l defect is Born & Heisenberg, Ueber den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten, Z. Phys. 23 (1924) 388-410, and Mayer & Mayer, Phys. Rev. 43 (1933) 605.**

### `P.qdt` — core penetration

**the quantum defect measures how far a Rydberg orbital reaches into the ionic core**

*a Rydberg series with three or more members, or two with a published limit*

grade **MEASURED**· source *R 693, 707, 713; Seaton 1958, 1983*· 12 objects depend on it· depth 0

four independent confirmations, none encoded

> **PRIOR ART: quantum defect theory — Seaton, The quantum defect method, MNRAS 118 (1958) 504-518, and Quantum defect theory, Rep. Prog. Phys. 46 (1983) 167-257.**

### `P.selfsame` — series self-consistency

**one series in disjoint n windows gives one defect**

*windows where P.lens's amplification is comparable*

grade **MEASURED**· source *R 747, 748, 751; Ritz 1903*· depends on `P.qdt`· depth 1

67 of 72 channels agree between disjoint halves to better than 0.05 (R 811)

> **PRIOR ART: one unperturbed series has one defect; disjoint n-windows must agree. The consistency test of the Ritz form (1903).**

### `P.termsplit` — core angular structure

**at l=3 delta splits by the core's TERM while its J-pairs stay together**

*j-K coupled series on one core*

grade **MEASURED**· source *R 739; Condon & Shortley 1935*· depends on `P.qdt`· depth 1

12 of 15 groups have terms separating by more than their J-pairs — median within 0.0011 vs between 0.0462 (R 826)

> **PRIOR ART: the splitting of a Rydberg series by the core term, with J-pairs staying together, is the parent-term structure of Condon & Shortley (1935), ch. VII.**

### `P.trunc` — truncation loss

**truncation removes most channels and degrades those it leaves**

*a series cut at low n*

grade **MEASURED**· source *R 675, 676, 677, 705, 706; Inglis & Teller 1939*· depth 0

Ne I: 33 Handbook levels give 0 channels, the full table gives 4

> **PRIOR ART: a Rydberg series is truncated in practice by field ionisation and by plasma microfields — Inglis & Teller, Ionic depression of series limits in one-electron spectra, Astrophys. J. 90 (1939) 439-448.**

## Q. The channel equation — the closed form and its terms — 11 objects

### `Q.alpha` — the polarisability index

**Lambda_alpha: the polarisability index over cores, coordinates Z . Ne(core) . n_out . l_out**

*the set of cores appearing in the spectra index*

grade **MEASURED**· source *R 1165; Born & Heisenberg 1924; Mayer & Mayer 1933*· depends on `S.regime`· 1 objects depend on it· depth 9

18 cores held, E = 10. Sorted by (n_out, l_out) the isoelectronic ordering is a physical requirement — alpha must FALL with Z along a sequence — and the Ne-like and Mg-like rows obey it while the Ar-like row does not: K I 5.490 published, Ca II 6.665 extracted, Sc III 4.705. The index makes the violation visible where a table would not

> **PRIOR ART: core dipole polarisability as the origin of the high-l defect is Born & Heisenberg, Z. Phys. 23 (1924) 388-410; the systematic values are Mayer & Mayer, The polarizabilities of ions from spectra, Phys. Rev. 43 (1933) 605-611.**

### `Q.anchor` — the two-ended anchor

**anchoring the equation at BOTH ends of Z fixes the extrapolation at almost no in-region cost**

*the channel equation and a far-field literature value*

grade **MEASURED**· source *R 1201-1205; Theodosiou, Inokuti & Manson 1986*· depends on `Q.region`, `Q.collapse`· 1 objects depend on it· depth 13

seven far anchors — Cs I np measured at 3.5667, and Th/Ac ns, np, nd, nf from actinide theory at 5.2, 4.75, 3.8, 2.0 — extend the sample from Z <= 83 to Z = 90. Far-anchor median error falls 0.754 to 0.064, a factor of twelve; in-region rises 0.0637 to 0.0665. The saturating exponent returns for real: e(Ne) = 0.8297 - 0.0900 ln Ne against -0.0266 from the in-region sample alone. CAVEAT: four of the seven anchors are THEORETICAL, so the high-Z arm is calibrated against another calculation and moves if that is revised

> **PRIOR ART: asymptotic quantum defects for all ionisation stages of all ions with Z <= 50 are tabulated in Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35 (1986) 473-486, Hartree-Slater. The far anchors used here are Cs I np (measured) and actinide values from arXiv:2508.06733.**

### `Q.bound` — the Pauli bound

**B = min( p , n0 - l - 1 ): the integer part's exceptionless upper bound, from aufbau alone**

*a channel and its core's ground configuration*

grade **PROVED**· source *R 1141; Pauli 1925; Janet 1929*· depends on `S.ground`· 5 objects depend on it· depth 7

floor(delta) <= B for 311 of 311 measured channels. As an equality it is right 57%; every error is negative; within two of the bound, 303 of 311. p is the core's orbital count at that l and n0 the first Pauli-allowed n, both from aufbau with no spectrum

> **PRIOR ART: the bound counts core orbitals of the same l and the first Pauli-allowed principal number, both read from the ground configuration. Paulis exclusion principle, Z. Phys. 31 (1925) 765-783, fixes the occupancies; Janets n+l ordering (1929) fixes which subshells are filled.**

### `Q.bridge` — the bridge equation

**the bridge between the metric and ordinal descriptions is MULTIPLICATIVE with a REGIME factor: every factor positive so each preserves rank by itself, and the regime factor differs between two channels only when they differ in regime**

*a channel equation required to respect both values and orderings*

grade **MEASURED**· source *R 1169-1171; Pareto 1896; Pareto 1896; Spearman 1904*· depends on `Q.delta`, `S.regime`· 1 objects depend on it· depth 12

an additive fit gets P.lcollapse 102/205 against a measured 194 — chance. A purely multiplicative fit gets 205/205, 143/143, 66/66 where the measurements give 194, 89, 55 — it cannot represent an exception because a product of positives is monotone in each factor. With a regime factor: 204/205, 129/143, 61/66, and ln-R^2 improves 0.8026 to 0.8164

> **PRIOR ART: that a multiplicative form preserves rank and an additive one does not is elementary; that no single form does both well is a Pareto statement about the two objectives.  PRIOR ART: a product of positive factors is monotone in each and so preserves rank; a sum of signed terms need not. Rank preservation as an objective distinct from least squares is Spearman, The proof and measurement of association between two things, Amer. J. Psychol. 15 (1904) 72-101. That no single form does both well is a Pareto statement (1896).**

### `Q.collapse` — the Janet collapse

**the ORBITAL COLLAPSE threshold is a Janet block boundary, exactly**

*a channel with p = 0 at l >= 2*

grade **MEASURED**· source *R 1187-1190; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969*· depends on `S.ground`, `Q.bound`· 2 objects depend on it· depth 8

the n+l = 5 block opens at Z = 21 and 3d collapses at 21; n+l = 7 opens at 57 and 4f at 57; n+l = 8 opens at 89 and 5f at 89. Three exact matches. Across 116 p = 0 channels at l = 2 or 3: collapsed median 0.637, uncollapsed 0.036, U-test p = 9.8e-4. Adding the term takes Ti IV nd from -0.620 to -0.056 and the overall rms from 0.1825 to 0.1411. The largest outliers are atoms APPROACHING a boundary — Ca I nd = 0.908 at Z = 20 against a threshold of 21, Ba II nf = 0.756 at 56 against 57 — so the collapse is a rapid transition, not a step

> **PRIOR ART: orbital collapse — the sudden contraction of the 3d and 4f wavefunctions as Z crosses a threshold — is Goeppert-Mayer, Rare-earth and transuranic elements, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Theoretical calculations of the d-, f- and g-electron transition series, Phys. Rev. 177 (1969) 62-71. What is measured here is that the threshold coincides with the Janet block boundary at Z = 21, 57 and 89.**

### `Q.delta` — the channel equation

**delta = [ B - q e^(-a(Ne)l) e^(k/Ne) c^g + P ] (1 + s [triplet]): a closed form for any Rydberg channel from atomic-index quantities alone**

*a Rydberg channel (Z, charge c, l, multiplicity)*

grade **MEASURED**· source *R 1145-1168; Seaton 1958; Fermi 1928; Pauli 1925*· depends on `Q.bound`, `Q.pen`, `Q.pol`, `Q.exch`· 2 objects depend on it· depth 11

311 measured channels: rms 0.2449, R^2 0.924, median |error| 0.090. By l: s 0.283, p 0.276, d 0.280, f 0.119, g 0.0096. Against TWELVE published values never fitted on: median error 0.00155 at l >= 3 and 0.368 below. 50% within 0.090, 90% within 0.414, 99% within 0.826

> **PRIOR ART: the superseded form of the channel equation. Its terms are the Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958). Superseded by Q.final at register 1205.**

### `Q.exch` — the exchange factor · **GRADED OPEN**

**the exchange factor (1 + s [triplet]), s = -0.0782**

*a channel of a two-valence-electron system*

grade **ASSERTED**· source *R 987, withdrawn R 1168*· depends on `Q.bound`· 1 objects depend on it· depth 8

WITHDRAWN (R 1168). The claim was that the fitted s recovers register 987's sign and size. It does not: register 987 measures the triplet defect EXCEEDING the singlet in 22 of 22 ns cases, and the additive fit returned s = -0.0782, the right magnitude and the WRONG SIGN. Cross-checked on 66 singlet/triplet pairs the equation gets 33, exactly chance. The parameter absorbed something else

> **PRIOR ART: the exchange splitting between singlet and triplet is Heisenberg, Mehrkoerperproblem und Resonanz in der Quantenmechanik, Z. Phys. 38 (1926) 411-426; that the higher multiplicity lies lower is Hund first rule (1925). WITHDRAWN at register 1168: the fitted sign is opposite to the measured one.**

### `Q.final` — the channel equation

**delta = a p^e(Ne) Ne^k ln(c+1)/c where p > 0, and h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c where p = 0**

*any Rydberg channel (Z, charge, l, multiplicity)*

grade **MEASURED**· source *R 1205-1206; Seaton 1958; Fermi 1928; Janet 1929*· depends on `Q.anchor`, `Q.bound`· depth 14

a = 0.3772, e(Ne) = 0.8297 - 0.0900 ln Ne, k = 0.4942, h = 0.5415. 284 channels from Z = 2 to 90 and charge 1 to 10: rms 0.1610, R^2 0.9741, l >= 4 rms 0.0150, hydrogenic output EXACTLY zero, Pauli bound 328/328, one l-ordering violation against a measured zero. Four fitted numbers and every input from the ground state or the periodic table. It values all 1,648 cells R places, where the walk valued none

> **PRIOR ART: every term of the form has a source. The ln(c+1)/c charge dependence is the isoelectronic behaviour of Edlen 1964; the Ne^k factor is Thomas-Fermi (Fermi 1928); p is the Pauli orbital count (Pauli 1925); C(Z) is orbital collapse (Griffin, Andrew & Cowan 1969) at the Janet boundary (Janet 1929). The equation assembles them; it does not introduce any.**

### `Q.pen` — the deficit term

**the penetration deficit, -q e^(-a(Ne) l) e^(k/Ne) c^g, with a(Ne) = a0 + a1 Ne^(-1/3)**

*a channel below the polarisation regime*

grade **COMPUTED**· source *R 1147; Hartree 1928; Fermi 1928*· depends on `Q.bound`· 1 objects depend on it· depth 8

the decay a is set by the atom's SIZE: a against ln Ne gives r^2 = 0.437 across 56 species, against electrons-beyond-closure 0.143, against charge nothing (p = 0.34). K I's measured d/s ratio implies a = 1.03, Sr I's implies 0.157 — a factor of seven, and a universal a fits neither

> **PRIOR ART: the penetration deficit and its Ne^(1/3) scaling are the Thomas-Fermi picture — Fermi, Eine statistische Methode zur Bestimmung einiger Eigenschaften des Atoms, Z. Phys. 48 (1928) 73-79; Hartrees self-consistent field, Proc. Camb. Phil. Soc. 24 (1928) 89-110, gives the orbital form. Fermi 1928 applied it to Rydberg corrections directly.**

### `Q.pol` — Seaton's term

**the polarisation term, 3 alpha c^2 / K(l) for l >= 4 with alpha from Lambda_alpha, K(l) = l(l+1)(2l-1)(2l+1)(2l+3)**

*a non-penetrating channel and a core polarisability*

grade **CITED**· source *R 1165-1168; Seaton 1958; Born & Heisenberg 1924*· depends on `A.seaton`, `Q.alpha`· 1 objects depend on it· depth 10

Seaton's formula. With alpha supplied as a species LABEL from Lambda_alpha rather than a universal constant, the l >= 4 rms falls from 0.01504 to 0.00958 — 36%. Below l = 4 it must be gated OFF: applied at s and p it drives the fit to rms 39.3 because K(l) is small there

> **PRIOR ART: the polarisation term 3 alpha c^2 / K(l) is Seaton (1958); the physical origin is core polarisability, Born & Heisenberg, Z. Phys. 23 (1924) 388-410. SUBSUMED at register 1204 by the Janet collapse coordinate.**

### `Q.region` — the validated domain

**the equation is VALIDATED in the verified-plus-possible region and EXTRAPOLATED outside it**

*the channel equation and the existence partition*

grade **MEASURED**· source *R 1193-1194; Theodosiou, Inokuti & Manson 1986*· depends on `Q.delta`, `S.status`, `Q.collapse`· 1 objects depend on it· depth 12

277 in-region channels give rms 0.1329 and R^2 0.9747 — better than the 311-channel fit on fewer points, because the 51 excluded were 24 three-parent cores, 15 sixteen-parent cores and 12 ions above charge 10. And the saturating exponent falls from 1.3257 - 0.2751 ln Ne to 0.5828 - 0.0266 ln Ne: nine-tenths of the Ne-dependence was open-shell contamination. Validated on 277, extrapolated to 98,078

> **PRIOR ART: the distinction between where a defect is measurable and where it is calculated is exactly the distinction their 1986 table makes — they compute Hartree-Slater values everywhere and note where experiment exists.**

---

# V · THE CHAINS

The longest derivation paths in the register — what rests on what.

**depth 14** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region` ← `Q.anchor` ← `Q.final`

**depth 13** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region` ← `Q.anchor`

**depth 13** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.bridge` ← `A.blind`

**depth 12** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.bridge`

**depth 12** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta` ← `Q.region`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.bits` ← `L.circuit`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.pushback` ← `L.step`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `I.interval` ← `I.convex` ← `EM.spin`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `I.interval` ← `I.convex` ← `EM.parity`

**depth 11** · `A.alph` ← `A.env` ← `A.R` ← `K.redun` ← `K.axis` ← `K.produce` ← `S.ground` ← `S.ritz` ← `S.regime` ← `Q.alpha` ← `Q.pol` ← `Q.delta`

**depth 10** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.alpha`

**depth 10** · `A.alph` ← `A.env` ← `A.R` ← `A.ext` ← `A.clos` ← `A.fix` ← `A.rule` ← `L.closed` ← `L.dist` ← `L.birk` ← `L.mobius`

---

# VI · WHAT IS UNFINISHED

**Two objects.** *Neither is unfinished for want of a proof attempt. Each has a diagnosis, and the diagnosis names what is missing rather than restating that something is.*

## `M.C2` — half-sided modular inclusion on a non-expanding horizon

        Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂)   for t ≤ 0, u₁ < u₂

**What is settled.** Half-sided modular inclusion is CHARACTERISED — Borchers, *The CPT theorem in two-dimensional theories of local observables*, Commun. Math. Phys. **143** (1992) 315–332, and Wiesbrock, *Half-sided modular inclusions of von Neumann algebras*, Lett. Math. Phys. **28** (1993) 107–114: the inclusion holds exactly when a one-parameter unitary group with positive generator implements the translation. The vacuum is cyclic and separating for local algebras (Reeh & Schlieder 1961), and modular theory supplies Δ and J (Tomita 1967; Takesaki 1970). **None of that is in question.**

**What is missing, precisely.** The hypothesis — *a non-expanding horizon with no Killing field, ω Hadamard* — asks the expansion Θ = 0 to select what only a STATE can select, and offers Hadamard, a microlocal condition, as the selector.

> **The horizon's own definition supplies a state condition at BACKGROUND order — Einstein's equation with future-causality forces vanishing shear, vanishing null flux and £_ℓ q_ab = 0 — and leaves a gap at PERTURBATION order.** *That gap is the object.*

**Where the obstruction sits.** The free half is confirmed numerically: the spectral weight ratio is of order 10⁻⁵. The obstruction is in the corner edge modes, and the proposal Θ = 0 was refuted by the transformation law. Sorce (2024) closes the geometric route by construction — a geometric modular flow must be generated by a conformal Killing field — so a horizon with no Killing field cannot have one, and the route that remains is algebraic.

**What would settle it.** The covariance of conditional expectations across the full family of cuts, in the manner of an over-determined joint fit. *Chandrasekaran & Flanagan (arXiv:2601.07915) is the nearest published treatment and was read into the diagnosis at registers 1037–1042.*

## `Q.exch` — the exchange factor

        δ = [ … ] · (1 + s·[triplet]),   s = −0.0782

**What is settled.** Exchange splitting between singlet and triplet is Heisenberg, *Mehrkörperproblem und Resonanz in der Quantenmechanik*, Z. Phys. **38** (1926) 411–426; that the higher multiplicity lies lower is Hund's first rule, Z. Phys. **33** (1925) 345–371. **The physics is not in doubt.**

**What is missing, precisely.** *The fitted sign is opposite to the measured one.* The factor was withdrawn at register 1168 for that reason and the grade left as ASSERTED rather than removed, because the term is real and the form is wrong.

> **A uniform s cannot work.** *Exchange acts through the overlap of the Rydberg orbital with the core, and that overlap falls sharply with ℓ. A single multiplicative constant can only give 0 of 66 triplet-above-singlet pairs or 66 of 66; the measurement is neither.*

**What would settle it.** An ℓ-dependent exchange term, fitted against the singlet–triplet pairs the compendium holds. The Pauli bound (`Q.bound`) already carries the orbital count p that the overlap should follow.

---

# VII · THE BIBLIOGRAPHY

**Every object of this compendium names a work.** What follows is those works, ordered by year, with the objects each carries. *The book claims nothing new where an earlier result will do; where a measurement is this work's, the object says so.*

**137 works, 1669–2026.**

| year | work | objects |
|---|---|---|
| 1669 | Newton | `B.newton` |
| 1682 | Leibniz | `B.brk` |
| 1687 | Newton | `B.ordbr` |
| 1715 | Taylor | `B.frac` `B.pole` |
| 1736 | Euler | `G.graph` |
| 1748 | Euler | `A.prodE` `C.Aq` `C.Bq` `C.box` `L.F` `L.F1` `L.Fm1` |
| 1797 | Lagrange | `B.hstar` |
| 1809 | Gauss | `A.anchor` `B.adm` `C.qmean` `L.skew` |
| 1854 | Boole | `A.logic` |
| 1869 | Mendeleev | `E.ioniz` `E.table` |
| 1890 | Rydberg | `B.V43` `B.Vexact` `B.fail` `B.floor32` `B.nuV` `B.silence` `P.converge` `P.lens` |
| 1893 | Heaviside | `L.chi` |
| 1896 | Pareto | `B.pareto` `C.pareto` `Q.bridge` |
| 1900 | Dedekind | `L.modular` |
| 1903 | Ritz | `P.converge` `P.mono` `P.selfsame` `S.regime` `S.ritz` |
| 1904 | Spearman | `Q.bridge` |
| 1906 | Jensen | `B.floor2` `B.floor32` |
| 1907 | Fubini | `C.fib` |
| 1910 | Moore | `A.E` `A.R` `A.bound` `A.clos` `A.expr` `A.ext` `A.fix` `F.exact` `F.moore` `L.E0` `S.bounds` `S.open` `S.seed` |
| 1911 | Caratheodory | `S.car` |
| 1913 | Bohr | `B.coll` `L.c1` `L.c4` `L.def` |
| 1913 | Pauli | `L.def` |
| 1916 | Sommerfeld | `P.jsplit` |
| 1918 | Noether | `EM.quotient` |
| 1923 | Helly | `K.helly` |
| 1924 | Born & Heisenberg | `P.polar` `Q.alpha` `Q.pol` |
| 1924 | Laporte | `EM.cross` `EM.map` `EM.parity` |
| 1924 | Stoner | `L.c2` `L.c5` |
| 1925 | Hund | `L.c7` `Q.exch` `S.ground` |
| 1925 | Pauli | `L.c2` `L.c3` `L.c5` `L.c6` `L.c7` `L.c8` `L.def` `Q.bound` `Q.delta` `Q.final` `T.a9p` |
| 1925 | Russell & Saunders | `EM.spin` |
| 1926 | Aitken | `B.aitken` |
| 1926 | Schroedinger | `L.c1` |
| 1927 | Wigner | `EM.image` `EM.parity` |
| 1928 | Dirac | `P.jsplit` |
| 1928 | Fermi | `Q.delta` `Q.final` `Q.pen` |
| 1928 | Hartree | `P.lcollapse` `Q.pen` `S.ritz` |
| 1928 | Sperner | `L.sperner` |
| 1929 | Janet | `E.layout` `E.table` `Q.bound` `Q.final` `S.ground` |
| 1929 | Janets | `Q.bound` |
| 1931 | Clebsch-Gordan | `T.a12` |
| 1931 | Wigner | `EM.spin` `T.a12` `T.dens` `T.excl` `T.invariant` |
| 1933 | Mayer & Mayer | `Q.alpha` |
| 1933 | Milne-Thomson | `B.V` `B.brk` `B.ordbr` `B.ordk` `B.pole` |
| 1935 | Condon & Shortley | `EM.map` `P.jj` `P.termsplit` `S.channel` `S.parent` `T.a11` `T.a13` `T.real` `T.scheme` `T.tower` |
| 1935 | J-pairs | `P.termsplit` |
| 1936 | Eckart & Young | `B.rank1` |
| 1936 | Madelung | `L.real` `S.ground` |
| 1936 | Tarski | `A.logic` `C.compare` |
| 1937 | Birkhoff | `A.define` `A.erel` `I.convex` `K.arrow` `K.produce` `L.alpha` `L.arith` `L.birk` `L.bits` `L.dist` `L.omega` `L.pushback` `L.step` `S.box` `S.seed` |
| 1937 | Shannon | `L.bits` |
| 1938 | Shannon | `L.circuit` `S.bits` `W.onehot` |
| 1939 | Inglis & Teller | `P.trunc` |
| 1940 | Birkhoff | `A.derived` `A.erel` `A.morph` `A.prod` `I.convex` `I.interval` `I.shape` `L.arith` `L.closed` `L.total` |
| 1940 | Deming & Stephan | `A.stat2` `G.stat` |
| 1941 | Dushnik & Miller | `A.erel` `K.axis` `L.dim` |
| 1941 | Goeppert-Mayer | `P.dcollapse` `Q.collapse` |
| 1942 | Racah | `T.a11` `T.a12` `T.dens` `T.dich` `T.invariant` `T.scheme` `T.tower` |
| 1942 | Ward | `A.clos` `F.moore` `F.open` |
| 1943 | Racah | `S.parent` `T.a10` `T.a9` `T.a9p` `T.excl` `T.tower` |
| 1945 | Segre | `E.nuclide` |
| 1948 | Coxeter | `W.face` |
| 1948 | Shannon | `A.blind` `A.ebits` `A.slack` `EM.notcomp` `G.reg` `K.axis` `K.redun` `K.transit` |
| 1950 | Dilworth | `S.box` `S.down` |
| 1950 | Hamming | `W.frontier` |
| 1950 | Pais & Uhlenbeck | `W.core9` |
| 1953 | Green | `T.para` |
| 1955 | Tarski | `A.cert` `F.open` |
| 1957 | Bethe & Salpeter | `B.coll` |
| 1958 | Pauli | `Q.delta` |
| 1958 | Seaton | `A.seaton` `P.coreblind` `P.lcollapse` `P.polar` `P.qdt` `Q.delta` `Q.final` `Q.pol` |
| 1959 | Dijkstra | `A.EW` `A.W` `A.intext` `A.three` |
| 1960 | Erdos & Renyi | `A.dens` |
| 1961 | Fano | `P.perturb` |
| 1961 | Reeh & Schlieder | `M.rs` |
| 1962 | Berge | `G.near` `G.tower` `K.girth` `K.peak` |
| 1964 | Edlen | `A.S` `K.zcross` `P.buildlimit` `P.charge` `P.iso` `Q.final` |
| 1964 | Moebius | `G.book` |
| 1964 | Rota | `C.local` `G.book` `L.amp` `L.box` `L.mobius` `L.void` `L.voidfrac` |
| 1965 | Kolmogorov | `F.unstatable` |
| 1965 | Penrose | `W.core9` |
| 1967 | Floyd | `K.clock` `K.clockfail` |
| 1967 | Tomita | `M.tt` |
| 1968 | Ireland and Kullback | `A.stat2` |
| 1969 | Andrew & Cowan | `P.dcollapse` `Q.collapse` `Q.final` |
| 1970 | Codd | `A.alph` |
| 1970 | Fano | `P.perturb` |
| 1970 | Takesaki | `M.tt` |
| 1971 | Lane | `K.cat` `K.comp` `K.deadend` `K.jump` `K.twocol` |
| 1972 | COVER | `S.cover` |
| 1972 | Gabriel | `K.quiver` |
| 1972 | Karp | `S.core` `S.cover` `S.erasure` `S.lam` `S.unit` |
| 1973 | Takesaki | `M.takesaki` |
| 1974 | Curtis & Reid | `B.hstar` |
| 1974 | Johnson | `S.cover` `S.lam` |
| 1974 | Montanari | `A.montanari` |
| 1975 | Baker & Pixley | `A.fix` `A.two` |
| 1975 | Csiszar | `G.stat` |
| 1978 | Freuder | `A.blind` `A.gc` `A.modeA` `A.modeB` `A.three` `G.allcons` `G.prot` `K.corner` `W.jur` |
| 1978 | Gratzer | `L.pushback` `L.step` |
| 1978 | Rissanen | `A.ebits` |
| 1979 | Chvatal | `S.core` `S.unit` |
| 1979 | Dawid | `G.trip` |
| 1980 | Stanley | `L.sperner` |
| 1981 | Monjardet | `I.shape` `L.metric` `L.occ` |
| 1982 | Freuder | `A.freuder` `C.cut` `G.cons` `G.ref` `G.shape` `L.E0` `L.box` `L.tree` `T.trad` |
| 1982 | Racah | `T.trad` |
| 1983 | BFMY | `A.intext` `C.compare` `K.three` |
| 1983 | Maier & Yannakakis | `A.intext` `A.relax` `C.compare` `K.langclose` `K.three` `K.window` |
| 1986 | Inokuti & Manson | `Q.anchor` `Q.region` `S.status` |
| 1986 | Stanley | `C.Aq` `C.Bq` `L.F` `L.F1` `L.Fm1` `L.chains` `L.pal` `L.rankpoly` |
| 1988 | Pearl | `G.trip` `K.decay` `K.markov` |
| 1989 | Cooper | `A.bpc` |
| 1989 | Dechter & Pearl | `G.cons` `G.shape` `K.coupling` |
| 1989 | Nouguier & Vilarem | `A.bpc` |
| 1991 | Chinneck & Dravnieks | `W.core15` `W.core9` `W.scale` `W.supp` |
| 1991 | Cover & Thomas | `K.decay` |
| 1991 | Drake & Swainson | `A.seaton` |
| 1991 | Kay-Wald | `M.C2` |
| 1992 | Borchers | `M.C2` `M.hsmi` `M.ledger` |
| 1992 | Dechter | `A.dechter` `A.gc` |
| 1993 | Wiesbrock | `M.C2` `M.hsmi` `M.ledger` |
| 1994 | Nesterov & Nemirovskii | `B.newton` `B.selfconc` |
| 1995 | Beek & Dechter | `A.rule` `A.staircls` |
| 1996 | Lauritzen | `K.decay` `K.markov` |
| 1999 | Deville | `A.env` `A.orient` `A.r4` `T.tight` |
| 1999 | Hentenryck | `A.orient` `A.rule` `A.stair` `A.staircls` `T.tight` |
| 2000 | Wald & Zoupas | `M.C1` |
| 2003 | Fredenhagen & Verch | `W.rel` |
| 2017 | Diestel | `G.graph` |
| 2024 | Killing | `M.sorce` |
| 2024 | Sorce | `M.sorce` |
| 2026 | COMPLETED | `M.C2` `M.ledger` |
| 2026 | CONDITIONAL | `M.C2` |
| 2026 | CORRECTED | `K.twocol` `T.tower` |
| 2026 | QUALIFIED | `M.ledger` |
| 2026 | REPRODUCED | `E.nuclide` |

### The works this compendium leans on most

| work | objects |
|---|---|
| Birkhoff, 1937 | **15** |
| Moore, 1910 | **13** |
| Pauli, 1925 | **11** |
| Condon & Shortley, 1935 | **10** |
| Birkhoff, 1940 | **10** |
| Freuder, 1978 | **9** |
| Freuder, 1982 | **9** |
| Seaton, 1958 | **8** |
| Rydberg, 1890 | **8** |
| Shannon, 1948 | **8** |
| Stanley, 1986 | **8** |
| Euler, 1748 | **7** |

# THE MATHEMATICS OF THE LÖWDIN WORK

*Registers 1249–1357. Each object is stated with its provenance: what is standard
and whose it is, what is arithmetic, and what this work introduces.*

---

## The corridor — a system of linear inequalities

**The object.** Requiring an observed subshell g to have least ν against every
admissible rival r gives one inequality per rival,

> **a(√p_r − √p_g) < n_r − n_g**,  with p = n − ℓ − 1

whose solution is an interval with endpoints

> **L, U = Δn(√p_g + √p_r)/(p_g − p_r)**

**Standard.** Linear programming in one variable; the feasible set of a finite
system of linear inequalities in ℝ¹ is an interval. *Fourier 1826; Motzkin 1936.*

**This work.** *That the coefficients are node counts, so the endpoints lie in
ℚ(√ℕ) and take only nineteen distinct values across the periodic table.* And that
all 106 intervals are non-empty — the system is consistent.

**The closed form** for every ns/(n−1)d competition:

> **a_cross = (√(n−1) + √(n−4))/3**

*giving 0.5773503, 1.0000000, 1.2168450, 1.3938270 at n = 4, 5, 6, 7 — four exact
hits, and the 3 in the denominator is p_g − p_r, invariant across the table.*

## The staircase algebra of a closed index

**`A.staircls`** states that E(ℛ) = 0 iff the held set is an intersection of
monotone staircases. **A closed index is therefore a system of inequalities and
its cells are the lattice points satisfying them.**

**Read off Λ_PCA**, whose cells satisfy **L(s) ≤ d ≤ U(s)** with

> **L(s) = ⌊s/2⌋**  and  **U(s) = s + ⌊s/3⌋**

*both exact on s ∈ {0,1,2,3}.* **And off Λ_amp**, whose twenty cells satisfy the
single inequality **0 ≤ i ≤ ℓ**.

**This work.** *That the algebra of a closed index can be read back out of it as
floor functions — the staircases are not merely asserted to exist but written.*

## The Slater triangle, and a parity defect resolved

**Standard.** The multipole expansion of 1/r₁₂ gives, for a pair of subshells,
**F^k for k even up to 2min(ℓ,ℓ′)** and **G^k for k ≡ ℓ+ℓ′ (mod 2) from |ℓ−ℓ′| to
ℓ+ℓ′.** *Slater 1929; Condon & Shortley 1935; the angular factors are Racah's
(1942–1949).*

**The angular factor of G^k is the 3j symbol squared**, and for an s electron
against an ℓ electron the sole exchange integral has angular factor **exactly
1/(2ℓ+1)** — verified 1, 1/3, 1/5, 1/7 to machine precision.

**This work.** *That indexing on the multipole rank k gives E = 1 with the single
defect **F¹**, a term parity forbids — and that reindexing on position within
sequence closes it at E = 0.* **The rank's parity is fixed by the kind and the ℓ
pair, so rank is not a free coordinate.**

## The falsification of a selection rule

**The object.** Given the corridor at every element, a walk needs a rule for where
in each interval to place the carried value. **Eight rules were tested; seven give
106/106**, including uniformly random interior points on **200 of 200 seeds**. Only
"move to the farther endpoint" fails, at 74/106, because it can overshoot.

**This work.** *That the ordering data constrains only membership of the interval,
not position within it — so the eighteen resets landing on exact surds is a
property of one chosen rule and not of the table.* **A different rule reproduces
the periodic table with a disjoint trajectory and a going negative at five
elements.**

*Recorded because the surd trajectory was reported as a result before the
falsification was run, and the falsification withdrew it.*

## The necessity of state

**The object.** For each admissible subshell, set a to that subshell's own crossing
value and ask whether it is then least-ν. **104 of 106 steps admit two to four
self-consistent subshells** — the observed one is always among them, never uniquely
determined.

**This work.** *That the periodic table is not computable from a single atom's
configuration. It requires one number carried forward: the arithmetic supplies the
values, the walk supplies the selection.*

## The observability boundary

**The object.** Across eleven closed indexes, the quantity each closure cannot fix
was identified. **Nine of eleven are expectation values ⟨Ψ|Ô|Ψ⟩.** The exception is
**Λ_cross**, whose value is a node count needing no measurement — **and it is the
only index with no statistics language.**

> **An index closes when its cells are enumerable. What it cannot supply is exactly
> what requires an operator.**

**This work.** *That the compendium's own language test detects this: the
statistics language is silent precisely where no observation is needed.* **One
confirming instance; the prediction is falsifiable and has been tested once.**

## Λ_spectra's closure, and what the limit leaves

**The object.** The index runs to the LAST AVAILABLE SPECIES and stops. Λ is
complete at 976 because its coordinates are bounded by the physics; Λ_spectra is
infinite unless capped, and *all cappings are closed when complete*.

Indexing every subshell any atom holds, (n, ℓ, k) over the observed ground
configurations: **98 cells, E = 58**. Of those 58, **38 require more electrons
than any atom has** — 6f¹ through 6f¹⁴ and beyond, needing Z past the table.
Past the limit, not defects. Applying the limit:

*Corrected at register 1426: the split was first reported as 47 / 11, using
`ground.py`'s own edge of Z = 108 as the limit while the synthesised table runs
to 118. The nine cells between — 6d⁷–6d¹⁰ and 7p²–7p⁶ — are real elements, not
absences. The eleven named exceptions below are unaffected; only the count of
beyond-limit cells was wrong.*

> **E = 11, and every cell is named.**

| absent | Madelung predicts at | observed |
|---|---|---|
| 3d⁴ · 3d⁹ | Cr 24 · Cu 29 | 3d⁵ · 3d¹⁰ |
| 4d³ · 4d⁶ · 4d⁹ | Nb 41 · Ru 44 · Ag 47 | 4d⁴ · 4d⁷ · 4d¹⁰ |
| 4f² · 4f⁸ | Ce 58 · Gd 64 | 4f¹ · 4f⁷ |
| 5d⁸ | Pt 78 | 5d⁹ |
| 5f¹ · 5f⁵ · 5f⁸ | Ac 89 · Np 93 · Cm 96 | 5f⁰ · 5f⁴ · 5f⁷ |

*The Madelung exceptions, recovered as closure defects rather than looked up —
E.nuclide's shape, a defect whose every missing cell can be named.*

**This work — rival = donor iff the donor is not full.** Twelve walk steps have a
subshell empty as another fills. A subshell at capacity has nowhere to put an
electron, so it is not Pauli-admissible and cannot be a rival in anyone's bracket,
including its own. An s shell holds 2 and is full when it donates:

| donor | occupancy before | binding rival |
|---|---|---|
| 4s, 5s, 6s (Cr, Cu, Nb, Ru, Pt) | **2, full** | 4p, 5p, 6p |
| 5s (Pd) | **1, partial** | 5s |
| 5d, 6d, 7p (Pr, Tb, Pa, Pu, Bk, Rf) | partial | itself |

**Holds 12 of 12, with no fitted term.** *Pd is its own control: the only s donor
that is not full, and it sits with the d and f donors. Were the rule about angular
momentum it would sit with Cr.* The anomalous steps differ from ordinary ones in
WHICH RIVALS EXIST, and that is fixed by occupancy — which ν already carries in q.
Registers 1395–1398.

## Attributions

**The ⅔ scaling.** *Thomas–Fermi's.* The quadratic in nuclear charge along an
isoelectronic sequence is **Krug & von Lilienfeld, arXiv:2406.18416 (2024)**,
fitted on Z = 1–86. **Carcassés & González, Phys. Rev. A 80 (2009) 024502**, give
E_ioniz = Z²N^(−2/3)g(N/Z) and flag that it fails for neutrals — the same domain
this work's residuals bow in.

**Configuration crossings along isoelectronic sequences** are a computed object:
**Berengut et al., arXiv:1204.0603** locate the 6p–5f crossing in the thallium
sequence by Dirac–Fock.

**The node theorem**, **Pauli's exclusion principle** and the **centrifugal term
ℓ(ℓ+1)** are standard and this work introduces none of them.

**Seaton's ratio** δ₂/δ₀ = −ℓ(ℓ+1)/3 is **Seaton's**; *the domain restriction to
p = 0 is this work's.*

**Slater's rules and integrals** are Slater's; *the observation that the count of
discarded exchange integrals equals the count of bracket failures is this work's.*

---

## What this work introduces, in one list

| object | |
|---|---|
| **the corridor** | 106 consistent linear inequalities with node-count coefficients |
| **the nineteen surds** | the complete set of endpoints across the table |
| **a_cross = (√(n−1)+√(n−4))/3** | closed form for the ns/(n−1)d family |
| **the staircase algebra** | ⌊s/2⌋ ≤ d ≤ s + ⌊s/3⌋, read out of a closed index |
| **the sequence-index fix** | rank parity is not a free coordinate |
| **the selection-rule falsification** | the corridor is forced, the path is not |
| **the necessity of state** | 104 of 106 steps ambiguous without memory |
| **the observability boundary** | closure enumerates; observation values |
| **the singleton-output rule** | an index is closed when its reading is unique |
| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |
| **the limit** | Λ_spectra closes at the last available species; E = 11, all named |
| **rival = donor iff not full** | the twelve anomalous steps, from Pauli alone |

---

# The Löwdin indexes — Λ_law and Λ_const

*Owed since register 1296; written at register 1571. Nothing here answers
Löwdin's challenge — the amplitude law remains three fitted numbers.*

## Λ_law — seven laws on (law, carrier). E = 0.

An arbitrary ordering gave E = 7. Across all 7! x 4! = **120,960 orderings** the
defect runs 0 to 21, and **288 reach zero.**

**The closing carrier order is u < p < l - l_core < Z - T**, monotone in **how
LOCAL the variable is**: u is the whole atom, p counts one l's shells,
l - l_core compares two angular momenta, Z - T is one distance to one threshold.
Two laws sit on u, three on p, one on each of the others.

The held cells form a **staircase**, which by `A.staircls` is exactly the
condition for E(R) = 0.

**What only this index contributes: THE CARRIER.** Fitting a law in the wrong
carrier is what took the l-spread from a spurious r2 of 0.868 to a real 0.356.

## Lambda_const — fourteen constants on (role, carrier). E = 0 at 2 of 576.

Role order **exponent < centre < width < scale**. Standing: three fitted, six
measured, five derived or attributed.

**Every CENTRE is a small integer or half-integer** - 2 for the free shells, 2
for the gate, -1.5 for the switch, 2.5 for the l-validity, u0 = 4. **No SCALE
is.** The role axis orders by how much physics a number has absorbed.

**beta = 2/3 is load-bearing**: the only constant of arity three, in the
amplitude, the exponent and the validity, **and the one that is attributed.**

### The refusal, which is the more useful half

**`standing` cannot be a coordinate.** With attributed/derived/measured/fitted
on an axis the index closes at NO ordering; without it, at once.

> **An index whose coordinates mix the OBJECT with the OBSERVER cannot close,
> because the observer's axis has no order the object respects.**

The same fault is `origin` in Lambda_var, `kind` in Lambda_phys and `state` in
Lambda_ladder - four occurrences of one mistake, stated here as a rule.
