
# THE METHOD 1.6 — MATHEMATICAL COMPENDIUM

Generated from `mathreg.py` on 2026-08-12; the counts below were recounted from this file on 2026-08-29. **299 objects · 18 roots · 297 settled · 2 unfinished.**

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
| closure — objects the register holds | **265** |
| seed — objects nothing derives | **17** |
| ratio | **15.6 : 1** |

**The seed has not moved across every cycle of this project.** If a genuinely new mathematical
object entered that nothing existing derived, it would move — and that is the test.

## The eighteen roots

| object | statement |
|---|---|
| shape space and the shape sphere | ℝ³ = ℂ³ / (translations × rotations); S² = that / scale — shape space (Montgomery 2014; Hopf 1931) |
| projection onto coordinate i (§6.1) | Â_i(X) = { x_i : x ∈ X } |
| the polarisation formula | delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l( |
| the five-sigma admissibility threshold — where the bracket may be applied at all (§22.5) | r = 2Z²R/(ν³σ) ≥ 5 |
| monotone interpolation bracket (§20.1) | T(n) lies between T(n−1) and T(n+1) |
| the assembly rule — a composite observable's scaling exponent is 2a + 3b (§24.1) | an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b} |
| the value-one crossing — where the bracket's price V passes unity (§23.15) | ν_V = (3Z²R/5q)^{1/4} |
| node counting, ℓ ≤ n − 1 (§7.1) | ℓ ≤ n − 1 |
| Pauli, k ≤ 4ℓ + 2 (§7.1) | k ≤ 2(2ℓ+1) = 4ℓ+2 |
| the transfer bound (§7.1) | q ≤ k |
| node counting, f ≤ e − 1 (§7.1) | f ≤ e − 1 |
| Pauli, g ≤ 4f + 2 (§7.1) | g ≤ 4f+2 |
| the second transfer bound (§7.1) | g ≤ q |
| vector coupling (§7.1) | 2S ≤ k |
| the occupancy floor (§10.2) | k ≥ 1 (definitional restriction, not a bound) |
| Reeh–Schlieder | the vacuum is cyclic and separating for local algebras |
| core penetration (register 693) | the quantum defect measures how far a Rydberg orbital reaches into the ionic core |
| truncation loss (register 675) | truncation removes most channels and degrades those it leaves |

---

# II · THE OPERATORS

Every derivation in the book runs through these. Ten are this work's own; two (π, N₈) are cited and used as found.

| symbol | definition | scope | origin |
|---|---|---|---|
| **∧ ∨** | meet and join — greatest lower and least upper bound | cells | Birkhoff, standard |
| **φ̂** | the envelope: max xᵢ over cells with xⱼ ≤ v | sets of cells | §14.5 |
| **ℛ** | closure at the (≤,≤) corner of Deville's staircase class | sets of cells | §14.5.4 |
| **ℛ₄** | closure over all four orientations | sets of cells | §14.5.5 |
| **E** | E(X) = \|ℛ(X)\| − \|X\| — the defect | indexes | §6.1 |
| **E₄** | the defect under ℛ₄; E − E₄ is the orientation cost | indexes | §14.5.5 |
| **d** | d(x,y) = τ(lcm/gcd) = ∏(\|Δᵢ\|+1) = \|[x∧y, x∨y]\| | cells | title page |
| **∘** | composition of transitions — Λ₉ is a category | cells | §12.11 |
| **seed** | least G with ℛ(G) = X — **NP-hard** | sets of cells | §14.5.7 |
| **S** | envelope-step count; 2S = the tight-pair count | sets of cells | §14.5.9 |
| **ent** | the entrant operator: argmax over frontier (n,ℓ) of \|D(n,ℓ)\| in the ion's self-consistent field | subshells | §35; register 1701 |
| **π** | the shape map ℂ³ → ℝ³, w = (½(\|Z₁\|²−\|Z₂\|²), Re Z₁Z̄₂, Im Z₁Z̄₂) | configurations | Montgomery 2014; Hopf 1931 |
| **N₈** | the norm ∏_{ε∈{±1}³}(U − ε·u) — the minimal polynomial of a sum of three square roots | potentials | Lagrange 1770 |

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
it is why §12.1 can state its two-column law — ascending and descending quantities, exchanged under ν ↦ ν⁻³, a bipartite sign structure that admits no odd number of orientation reversals.

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

### Closure defect

**E(X) = |ℛ(X)| − |X|**

*none*

Definitional — M §6.1 / T A4; Moore 1910.

> **Prior art: the gap between a set and its closure. Naming the gap as a defect is this book's step; the quantity is the closure minus the set.**

### The metric defect

**E_W(X) = |W(X)| - |X|: the METRIC defect, what the steps reach and the index has not valued; distinct from E(X) = |R(X)| - |X|, the ORDINAL defect**

*an index whose cells carry values*

Definitional — R 1133; Dijkstra 1959.

for Λ E_W is empty, because a cell of Λ is an arrangement and carries no number — which is why the book needed only E. For Λ_spectra the two differ, and the gap between them is the cells that are placed and unvalued

> **Prior art: the reachable set under a step relation, with accumulated cost and a least-cost route, is single-source shortest paths — Dijkstra, A note on two problems in connexion with graphs, Numer. Math. 1 (1959) 269-271.**

### The recovery operator

**ℛ(X) = { x ∈ ∏_i Â_i(X) : x_i ≤ φ̂_ij(x_j) ∀ i≠j }**

*none beyond projection onto coordinate i (§6.1), monotone upper envelope / staircase bound (§6.1)*

Definitional — M §6.1 / T A3; Moore 1910; Deville et al. 1999.

> **Prior art: R is a closure operator (Moore 1910) whose constraints are monotone staircases (Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271). Neither the operator form nor the constraint class is new; what is new is reading E as a defect.**

### The step operator

**the STEP operator: for each coordinate direction, the ratio between adjacent VALUED cells, its median and its scatter; a direction earns a step when the scatter is tight enough to carry a value**

*an index whose cells carry values*

Measured — R 1132-1137; Edlen 1964.

derived unaided from the spectra index it finds iso at s (1.233, scatter 1.13, 43 pairs), iso at p (1.185, 1.16, 25) and l at s (1.416, 1.43, 62). It must be derived from MEASURED cells ONLY: re-deriving from the walked result tightens iso at s to 1.08 on 116 pairs, because the walked values were generated by that step, and the step count goes 3 to 8

> **Prior art: measuring a step as the ratio between adjacent valued cells is the isoelectronic and isonuclear method of Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### The walk

**the VALUATION closure: every cell reachable from a valued one by steps in S, accumulated error below a threshold, by the least-error route**

*an index, a step set S, and a tolerance*

Proved — R 1132-1136; Dijkstra 1959.

EXTENSIVE and IDEMPOTENT with exactly zero drift, since the least-error route from the seed leaves nothing tighter to find. MONOTONE except at one cell in 1,345: Mg II ni is measured at +0.0000, the Seaton step is multiplicative, and zero blocks a route a walked positive value would open — so adding a measurement can REMOVE a walked cell

> **Prior art: the valuation closure is a shortest-path closure over a multiplicative cost. Extensivity, idempotence and monotone-except-at-zero follow from Dijkstra (1959).**

### Projection onto coordinate i

**Â_i(X) = { x_i : x ∈ X }**

*X a finite set of integer tuples*

Definitional — M §6.1 / T A1; Codd 1970.

> **Prior art: projection onto a coordinate is the relational projection operator — Codd, A relational model of data for large shared data banks, CACM 13 (1970) 377-387.**

### The anchor

**REDUNDANCY ANCHORING: keep every route to a cell, not the best one; the spread between independent arrivals MEASURES the error rather than estimating it**

*a valuation closure with more than one route to a cell*

Measured — R 1136; Gauss 1809.

956 cells of the spectra index are reached by two or more distinct routes. Observed spread 1.05 against a propagated estimate of 1.14 — ratio 0.92, so the walk's error bars are honest and slightly conservative. The check comes from the index disagreeing with itself, not from an outside formula

> **Prior art: keeping every route to an estimate and reading their SPREAD as the error, rather than taking the best route, is the method of combining independent determinations — Gauss, Theoria motus corporum coelestium (1809), sec. 3.**

### The three blindnesses

**each language is blind in its own way: statistics cannot state a closure defect, analysis cannot state an ordering, a multiplicative algebra cannot state an exception**

*an index described in more than one language*

Measured — R 1169; Shannon 1948; Freuder 1978.

register 761 established the first. The second: least squares minimises squared error and has no rank in it — an equation fitting 311 values to R^2 = 0.924 got every ordering wrong. The third: a product of positive factors is monotone in each, so a multiplicative fit returns 205/205 where the data has eleven genuine exceptions

> **Prior art: that a representation cannot state what its own coordinates cannot distinguish is the general fact behind all three blindnesses. Statistics sees marginals only (Shannon 1948 for what a marginal carries); analysis has no order in it; a multiplicative algebra is monotone in each factor by construction. Register 1170 measures them.**

### The defect bounds

**0 ≤ E(X) ≤ |box| − |X|**

*box = ∏_i |Â_i(X)|*

Proved — T audit 27; Moore 1910.

> **Prior art: the bounds are extensivity below and the ambient product above; both follow from the closure axioms.**

### Binary path consistency / 2-decomposability (Kimura et al. 2024)

**X ⊆ BPC(X) ⊆ ℛ(X), BPC(X) = { x : (x_i,x_j) ∈ proj_ij(X) ∀ i<j }**

*none*

Proved — T A5; Cooper 1989; Janssen et al. 1989.

> **Prior art: binary path consistency and its relation to global consistency — Cooper, An optimal k-consistency algorithm, Artif. Intell. 41 (1989) 89-95; Janssen, Jegou, Nouguier & Vilarem, A filtering process for general constraint-satisfaction problems, IEEE (1989), which gives a polynomial algorithm for pairwise consistency.**

### The certificate condition

**an open index does not close itself except where a CERTIFICATE exhibits an operation on its coordinate system reaching a fixed point of R**

*the admitted operations: relabel, re-coordinatise, refine a fibration, drop a coordinate*

Proved — M §18.4.1, promoted; Tarski 1955.

> **Prior art: a closure operator does not close an open set without an added operation; exhibiting one is the fixed-point construction of Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309.**

### Closure operator (Moore family)

**ℛ is extensive, monotone, idempotent; the closed sets form a Moore family**

*none*

Proved — M §14.2 / T 1.3 (App. G); Moore 1910; Ward 1942.

> **Prior art: an extensive, monotone, idempotent operator is a CLOSURE OPERATOR and its fixed sets form a Moore family — E. H. Moore, Introduction to a Form of General Analysis (1910); M. Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. R is one; nothing about R is needed to know its fixed sets are closed under intersection.**

### Dechter 1992

**strong (w*+1)-consistency on induced width w* gives decomposability**

*induced width w**

Cited — Dechter 1992.

### The defining letter

**a rung-1 coordinate contributes no envelope: same cells, box, E, envelope-step count and seed with or without it — it is invisible to ℛ and still counts as a letter**

*it is the index's own name carried as a coordinate, taking one value because the object is what does not vary in it*

Proved — M §21.6.1; Birkhoff 1937.

> **Prior art: a coordinate with a single value contributes no join-irreducible, so it changes neither the lattice nor its envelopes.**

### Density and informativeness

**E = 0 is informative at any density; E > 0 at low density measures sparsity**

*density = |X| / |box|*

Computed — T 1.9 (App. G); Erdos & Renyi 1960.

> **Prior art: that a structural property can hold at any density, while its failure measures sparsity, is the random-graph threshold picture of Erdos & Renyi, On the evolution of random graphs, Publ. Math. Inst. Hung. Acad. Sci. 5 (1960) 17-61.**

### Adjunction never repairs (M Thm 10.1)

**a derived coordinate cannot repair closure: the box grows by its value count and |X| is fixed**

*the coordinate is a function of the others*

Proved — T 1.7 (App. G) / M §17.2 Thm 10.1; Birkhoff 1940.

> **Prior art: a derived coordinate is a function of the others, so it adds no join-irreducibles and cannot enlarge the closed family; it only enlarges the ambient box.**

### Description length

**E_bits(X) = log₂ C(|ℛ(X)|, E(X))**

*counting measure*

Computed — M §25.3; Shannon 1948; Rissanen 1978.

> **Prior art: description length as a measure of structure — Shannon, A mathematical theory of communication, Bell Syst. Tech. J. 27 (1948); Rissanen, Modeling by shortest data description, Automatica 14 (1978) 465-471. log2 C(|R|, E) is the cost of naming which admitted cells are absent.**

### Monotone upper envelope / staircase bound

**φ̂_ij(v) = max{ x_i : x ∈ X, x_j ≤ v }; max ∅ = −∞**

*i ≠ j*

Definitional — M §6.1 / T A2; Deville et al. 1999.

> **Prior art: the monotone upper envelope of a relation is its staircase bound — the connected row-convex class of Deville, Barette & Van Hentenryck (1999) and the row-convex networks of van Beek & Dechter, J. ACM 42 (1995) 543-561.**

### E is coordinate-relative

**E = 0 is relative to coordinates: any X with |X| = a·b relabels onto an a × b rectangle, which is a full box and closed — so every index with a composite cell count has a coordinate system in which E = 0**

*the coordinates must be fixed by the subject, not chosen; every coordinate in this book is*

Proved — M §21.6; Birkhoff 1940; Birkhoff 1937; Dushnik & Miller 1941.

> **Prior art: E = 0 is a statement about a COORDINATISATION, not a set. Any set of size ab relabels onto an a x b grid, which is closed. This is the standard observation that lattice properties are not invariants of the underlying set.**

> **Prior art: a lattice property belongs to a COORDINATISATION and not to the underlying set — the same reason order dimension is not an invariant of cardinality. Birkhoff (1937); Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610.**

### The expression always exists

**a closed index equals the set its own envelopes admit, so its expression always exists and is recoverable**

*X = R(X)*

Proved — M §15.2 corollary / §2.23; Moore 1910.

> **Prior art: a closed set equals the fixed point of its own closure operator, so its defining expression always exists. Immediate from idempotence.**

### Extensivity

**X ⊆ ℛ(X), hence E(X) ≥ 0**

*none*

Proved — T 1.2 (App. G) / M A.2; Moore 1910.

> **Prior art: extensivity is the first Moore axiom. That E(X) ≥ 0 is its immediate corollary, not a separate result.**

### Bergman double-projection; Baker–Pixley 1975 (majority term)

**X is closed ⟺ X = ℛ(X)**

*each coordinate presented as a chain*

Proved — M §14.1 (Thm 9.1, A.2); Moore 1910; Baker & Pixley 1975.

> **Prior art: X closed iff X = R(X) is the definition of a fixed point of a closure operator. That the binary projections suffice is Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174 — the majority-term / (2,d) interpolation theorem.**

### Freuder 1982

**a tree-structured constraint network is globally consistent after arc consistency**

*constraint graph acyclic*

Cited — T 1.10 (App. G); Freuder 1982.

> **Prior art: Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32 — a tree-structured constraint network is globally consistent after arc consistency. This is the reason Λ closes, and it is his.**

### Global consistency (CSP)

**E(X) = 0 ⟺ the binary constraint network is globally consistent**

*the constraints are the monotone binary projections*

Cited — T 1.4 (App. G) / A5c; Freuder 1978; Dechter 1992.

> **Prior art: global consistency and its k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966; Dechter, From local to global consistency, Artif. Intell. 55 (1992) 87-107.**

### Interior and exterior

**E is INTERIOR and E_W is EXTERIOR: the order operator is bounded by its sample and the step operator is not**

*an index with valued cells and a step set*

Measured — R 1196-1199; Beeri, Fagin, Maier & Yannakakis 1983; Dijkstra 1959.

on Λ_spectra in-region, R places 1,925 from 277 held (E = 1,648) and W values 277 (E_W = 0) at the book's tolerance, because every step's scatter exceeds it — multiplicity 1.664, isoelectronic 1.674, l 2.872. Raising tau does not close the gap: every cell W gains, R mostly refuses, and ALL 218 fail one envelope, charge given Z. The measured set runs Z 2-83 and charge 1-9; the refused cells run Z 1-85 and charge 1-10. The overlap never exceeds 12% of E at any tolerance

> **Prior art: the order operator is a closure bounded by its sample (BFMY 1983 for what local closure can reach); the step operator is a reachability closure unbounded by it (Dijkstra 1959). That E is interior and E_W exterior follows from the two being different kinds of operator.**

### The logic level

**LOGIC is not a language: it is the mechanism binary -> language -> binary by which any language answers a question about a cell**

*a language with a closure operator*

Definitional — R 1173; Boole 1854; Tarski 1936.

three levels: BINARY is the type, a cell is admitted or not; a LANGUAGE is a coordinate system with a closure operator; LOGIC is the map. A language earns a row when logic can operate on it and return a binary, which is why documentary has none — it returns a citation. The book's C(5,2) = 10 combinations is then exact: five operator-bearing languages, plus statistics as a sixth and documentary as a seventh

> **Prior art: that logic is the mechanism by which a language answers a binary question, rather than a language itself, is the object-language/metalanguage distinction — Boole, An Investigation of the Laws of Thought (1854); Tarski, Der Wahrheitsbegriff in den formalisierten Sprachen, Studia Philos. 1 (1936) 261-405.**

### Failure mode A — ordering

**sub-case A, ORDERING: the term is present and determined but non-monotone; repairable by re-ordering**

*the term is a function of an existing coordinate*

Computed — T 1.6 (App. G); Freuder 1978.

> **Prior art: a non-monotone constraint is not captured by an envelope, and higher consistency is needed — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### Failure mode B — arity

**sub-case B, ARITY: every term is monotone; the constraint names more coordinates than an envelope has arguments; not repairable by any operation on coordinates**

*the minimal failing support has size ≥ 3*

Computed — T 1.6 (App. G); Freuder 1978.

> **Prior art: a constraint naming more coordinates than the envelope pairs is a higher-arity constraint; the k-consistency ladder is Freuder (1978).**

### Montanari 1974

**for monotone constraints, path consistency implies global consistency**

*constraints monotone*

Cited — T 1.10 (App. G); Montanari 1974.

> **Prior art: Montanari, Networks of constraints: fundamental properties and applications to picture processing, Inf. Sci. 7 (1974) 95-132 — for monotone constraints, path consistency implies global consistency. Λ constraints are monotone, so this applies directly.**

### The cap as a morphism

**an occupancy coordinate's cap is admissible iff it is a morphism for the operation preserved**

*meet-morphism preserves meets; join-morphism preserves joins*

Computed — M §18.4.1; Birkhoff 1940.

> **Prior art: a cap is admissible iff it is a lattice morphism for the operation — the standard homomorphism condition. Birkhoff, Lattice Theory (1940).**

### Orientation cost

**E − E₄, the ORIENTATION COST: 0 on eight of ten indexed objects, 2 on the audits, 750 on the parity rule**

*ℛ₄ defined*

Computed — M §14.5.5; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999.

> **Prior art: the cost of choosing one orientation over the full class. The class is Devilles; the cost is measured here.**

> **Prior art: the four orientations of a staircase are the (alpha, beta)-monotone constraints of Deville, Barette & Van Hentenryck (1999). R uses one corner and R_4 the closure over all four; the ORIENTATION COST is the difference, measured at 0 on eight of ten indexed objects and 2 on the aufbau index.**

### The product rule for closure

**if no constraint links the factors, ℛ(A×B) = ℛ(A)×ℛ(B)**

*A, B on disjoint coordinate sets, no cross constraint*

Proved — T D9; Birkhoff 1940.

> **Prior art: a closure operator on a product with no cross-constraints factorises; the statement is the product form of a Moore family. Birkhoff, Lattice Theory (1940).**

### The product rule for the defect

**E(A×B) = |A|·E_B + |B|·E_A + E_A·E_B**

*as the product rule for closure*

Proved — T D10; classical; Euler 1748.

> **Prior art: the defect of a product expands as |A|E_B + |B|E_A + E_A E_B — the inclusion-exclusion expansion of (|A|+E_A)(|B|+E_B) minus |A||B|. Elementary.**

> **Prior art: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. Elementary algebra; the point is that defects MULTIPLY as well as add across a product.  PRIOR ART: expanding (|A| + E_A)(|B| + E_B) - |A||B| gives the three terms. The point is that defects MULTIPLY as well as add across a product, which is the elementary product rule for counting — Euler, Introductio in analysin infinitorum (1748), ch. XVI.**

### The four-orientation operator

**ℛ₄, the four-orientation closure over Deville's staircase class**

*idempotent, hence a closure operator*

Computed — M §14.5.5; Deville et al. 1999.

> **Prior art: the four orientations of a staircase constraint are the (alpha, beta)-monotone class of Deville, Barette & Van Hentenryck (1999); R uses one corner and R_4 the closure over all four.**

### ℛ as a relaxation

**ℛ is not a k-wise closure for any k: k-wise defect is 0 at k = d while E(ℛ) can be 750**

*|Δℓ|=1 at 750 against k-wise 0 for k = 2,3,4*

Proved — M §14.5.4; Beeri, Fagin, Maier & Yannakakis 1983.

> **Prior art: pairwise (k-wise) consistency implies global consistency exactly for ACYCLIC hypergraphs — BFMY, On the desirability of acyclic database schemes, J. ACM 30 (1983) 479-513. R is the global operator and the k-wise closures are the local ones; the gap between them is their theorem, and this object measures it.**

### The tightening rule

**a tightening preserves E = 0 iff it binds one coordinate by a monotone function of one other** — *one-sided as stated; the operator is two-sided (main §2.15.2; register 402).*

*the index is a sublattice of a product of chains*

Computed — T 1.8 (App. G) / M §14.4; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995.

> **Prior art: a tightening preserves closure iff it stays inside the monotone staircase class.**

> **Prior art: a tightening preserves closure exactly when it stays inside the monotone staircase class — the connected row-convex constraints of Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271, and the row-convex networks of van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561. Binding one coordinate by a monotone function of one other is precisely a member of that class.**

### The polarisation formula

**delta(n) = (alpha/K(l))(3 - l(l+1)/n^2) for a non-penetrating series, so delta_0 = 3 alpha/K and delta_2 = -l(l+1) alpha/K**

*a Rydberg electron that does not enter the core*

Cited — Seaton 1958; Drake & Swainson 1991.

tested on 23 adjacent-l pairs in its domain: median observed/predicted 1.12, improved from 1.19 by restoring the n-dependent term, which confirms the term belongs. It fails on 20 near-hydrogenic pairs at the noise floor and on Ba II (delta_f = 0.756) and Hg II (1.062), where the 4f orbital has collapsed into the core and the series penetrates

### Slack

**SLACK(S) = measure(ambient)/measure(S); log SLACK = log|ℛ(X)| − log|X|**

*a measure on the ambient*

Computed — M §25.2; Shannon 1948.

> **Prior art: log of the ratio of ambient to actual is a bit count — the same quantity as description length (§25.3) in another form. Shannon (1948).**

### Staircase / connected row-convex

**phi-hat recovers a STAIRCASE constraint: (alpha,beta)-monotone with alpha,beta in {≤,≥}**

*binary*

Cited — Deville, Barták, Van Hentenryck 1999.

### The one-corner characterisation

**E(ℛ) = 0 iff X is an intersection of (≤,≤) staircases — one corner of Deville's class**

*the anti-diagonal is a staircase with E = 750*

Proved — M §14.5.4; Deville, Barette & Van Hentenryck 1999; van Beek & Dechter 1995.

> **Prior art: connected row-convex and monotone staircase constraint classes — Deville, Barette & Van Hentenryck, Constraint satisfaction over connected row-convex constraints, Artif. Intell. 109 (1999) 243-271; van Beek & Dechter, On the minimality and global consistency of row-convex constraint networks, J. ACM 42 (1995) 543-561.**

### The statistics operator

**the statistics operator is max-entropy on the PAIRWISE marginals, not the first-order ones**

*an index of dimension d ≥ 3*

Measured — R 1174.

on Λ, first-order marginals admit all 6,912 ambient cells; pairwise marginals admit exactly 976 and reproduce R cell for cell. IPF converges to the max-entropy distribution matching the SPECIFIED marginals (Deming and Stephan 1940; Ireland and Kullback 1968), so which marginals is the whole question

### The three populations

**the Method equation partitions an index into three populations: interior captures, the working overlap, and exterior predictions**

*an index, its order operator and its step set*

Measured — R 1199-1200; Freuder 1978; Dijkstra 1959.

at tau = 3.0: INTERIOR 1,503 cells R places and no step values, median l = 2 and charge 4 — these are captures. BOTH 145 placed and valued, median l = 3, the polarisation regime. EXTERIOR 218 the steps reach past the sample edge. The exterior verifies where it reaches: Cs I np walked to 3.659 against a measured 3.5667, an error of 2.6% with a stated error factor of 1.67

> **Prior art: partitioning by what a closure admits and what a propagation reaches — the k-consistency gap (Freuder 1978) crossed with shortest-path reachability (Dijkstra 1959). The three populations are the measurement.**

### The binary-projection criterion

**a tightening preserves E = 0 iff each binary projection is the intersection of that projection's own two upper envelopes**

*phi-hat indexed over ORDERED pairs*

Proved — M §14.4 / §2.15.2; Baker & Pixley 1975.

> **Prior art: that binary projections decide membership is the (2,d) interpolation property — Baker & Pixley, Polynomial interpolation and the Chinese remainder theorem for algebraic systems, Math. Z. 143 (1975) 165-174.**

## S. The seed — generation, covering, structure — 21 objects

### The generation criterion

**X₀ ⊆ Λ generates Λ iff (a) X₀'s alphabet equals Λ's in every coordinate and (b) X₀'s pairwise envelopes equal Λ's at every alphabet value — exact, two-route validated at 200/200 covers closing to 976 under the sealed ℛ; it is the licence for the set-cover formulation: elements the alphabet slots and envelope steps, a cell covering what it witnesses**

*forward: Λ = ℛ(X₀) sits inside X₀'s box, so alphabets agree, and each envelope maximum is achieved by a cell of Λ that X₀'s closure must admit; back: same box, same constraints, same closure — using E(Λ) = 0*

Proved — M §14.5.9; EXPANSION-MC54 T1, L1.

> **Prior art: Baker & Pixley, Math. Z. 143 (1975) 165-174 — binary determination: pairwise envelopes decide membership. Deville, Barták & Van Hentenryck (1999) — the staircase constraint class ℛ lives in.**

### The alphabet law

**every generating set witnesses every alphabet value of every coordinate — every letter, both ways: for each coordinate some seed cell sits at its minimum and some at its maximum — CAP-INDEPENDENT, the proof using no cap; corollaries: every seed contains a null transition q = 0 and a full transfer q = k, both measured element-forced at all four cap settings tested**

*immediate from the generation criterion (§14.5.9): a generating set must reproduce the alphabet exactly, since the closure is carved from the generating set's own box*

Proved — M §14.5.12; EXPANSION-MC54 T2, C2.1.

> **Prior art: none claimed for the law itself; the application to an index's minimum seeds and the cap-sweep are the contribution.**

### The seed as binary, corrected

**writing 1 for a coordinate at its maximum and 0 at its minimum, every column receives both a 0 and a 1 across ANY seed, at ANY cap — a corollary of the alphabet law (§14.5.12), cap-independent because its proof uses no cap; the complement pairings once described here are REFUTED at Λ₈ itself — corner 4 (11001100) appears in 14% of the 24,585 exact minimum covers, the unit template in 10%**

*the earlier statement was a property of a 219-cover biased sample; what survives as law is the both-symbols-per-column reading, and only that*

Proved — M §14.5.14; EXPANSION-MC54 T2; Shannon 1938.

> **Prior art: reading a structure as binary words is Shannon, Trans. AIEE 57 (1938) 713-723 — retained for the encoding; the complementation claims are corrected, not carried.**

### The bounds are recoverable

**S3: the bounds are recoverable from the cells**

*closure*

Proved — M §15.2; Moore 1910.

> **Prior art: if the envelopes are recoverable from the cells then the constraints are too, since R is determined by its envelopes.**

### The box seed law, d + c − 2

**a full box c^d seeds at d + c − 2**

*exact by branch and bound at 3³ and 4³*

Proved — M §14.5.9; classical; Dilworth 1950; Birkhoff 1937.

> **Prior art: the corners of a d-dimensional box over c values generate it under coordinatewise max, and d + c - 2 is the count of extreme steps. Elementary.**

> **Prior art: as the down-set seed law, d + c − 1 (§14.5.9), for a full box: the extreme steps in each coordinate generate it.  PRIOR ART: the generators of a down-set closed under coordinatewise max are its maximal elements; for a box over c values in d coordinates that count is d + c - 2. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166; Birkhoff (1937) for the representation.**

### The Carathéodory lower bound

**seed ≥ the Carathéodory number = the breadth = d for a product of d chains**

*semilattice with subsemilattices as convex sets*

Cited — Carathéodory / convexity spaces; Caratheodory 1911.

> **Prior art: Caratheodory, Über den Variabilitaetsbereich der Fourierschen Konstanten, Rend. Circ. Mat. Palermo 32 (1911) 193-217 — every point of a convex hull in R^d is a combination of at most d+1 points. Its lattice analogue is the breadth, and it bounds the seed below.**

### The envelope-step law

**call (i, j, t) a STEP of Λ if t is minimal in coordinate j's alphabet with the envelope φ̂_ij at its value; then every generating set contains, for each step, a cell with c_j ≤ t and c_i = φ̂_ij(t) exactly — and covering all steps with all alphabet slots SUFFICES, because the running max is constant between steps**

*the six recorded channel conditions are the ℓ ≤ 1 face of this law — s→p, p→s, p→p, the null q = 0 and the full q = k are steps; s→s is NOT a step and was never forced, holding in 71% of the 24,585 exact covers; s→d and d→s become element-forced at the d-shell cap*

Proved — M §14.5.12; EXPANSION-MC54 T3; Condon & Shortley 1935.

> **Prior art: the subshell channel structure is Condon & Shortley (1935); determination of a monotone function by its breakpoints is elementary. The law supersedes the six-condition sample statement, which it contains as one face.**

### The seed's forced set, corrected

**exact enumeration gives 24,585 minimum covers at the Λ₈ cap, and exactly ONE cell is common to all of them — corner 3, (2,1,3,3,2,1,3,0), forced by Chvátal's reduction — and that forcing is CAP-SPECIFIC, falling at the d-shell cap; the four-corner universality of the 219-cover sample is refuted**

*nothing else is necessary: 0 uniquely-covered envelope elements at every other position; the seed's invariant content is alphabet slots and envelope steps (the alphabet law (§14.5.12), the envelope-step law (§14.5.12)), not cell identities*

Computed — M §14.5.10; SEED-CAP-FINDING; Karp 1972; Chvatal 1979.

> **Prior art: a set present in every minimum cover is forced by an element it uniquely covers — Chvátal (1979); the exact count and the cap-dependence are the measurement.**

### The seed is a set cover

**the minimum seed is a MINIMUM SET COVER: elements the envelope steps, sets the cells**

*a seed (§14.5.7)*

Proved — M §14.5.9; Karp 1972; Johnson 1974.

> **Prior art: MINIMUM SET COVER is one of the 21 NP-complete problems of Karp, Reducibility among combinatorial problems (1972); the greedy ln n approximation is Johnson, Approximation algorithms for combinatorial problems, JCSS 9 (1974) 256-278. The seed problem IS set cover, which is why five heuristics agree on 7 and the lower bound is 5.**

### The down-set seed law, d + c − 1

**a down-set over c values in d coordinates seeds at d + c − 1**

*exact: LB = UB at d=4 c=4*

Proved — M §14.5.9; Dilworth 1950.

> **Prior art: the minimum generating set of a down-set is its set of maximal elements; the d + c - 1 count follows. Dilworth, A decomposition theorem for partially ordered sets, Ann. Math. 51 (1950) 161-166.**

### The seed is an erasure structure

**the remaining three seed positions admit 519 completing triples over 66 distinct cells, none in all 519, each appearing in 3 to 157 — a redundancy gradient of fifty to one**

*heavy-tailed: min 3, median 12, max 157, a ratio of thirteen to one*

Computed — M §14.5.11; Karp 1972.

> **Prior art: the alternative completions of a partial cover; the count is the measurement.**

### The ground-state derivation

**the ground configuration determines every channel's existence and bounds its defect's integer part**

*an atom of atomic number Z*

Measured — R 1139-1141; Madelung 1936; Janet 1929; Hund 1925.

multiplicity from Hund on the core: 24 of 24 electron counts, exact containment. The cell set from aufbau: 8,488 cells admitting all 311 measured channels where the sampled index admits 296. And floor(delta) ≤ min(p, n0-l-1) for 311 of 311, exact 57%, within two 97%

> **Prior art: the ground configuration follows the n+l ordering — Janet, La classification helicoidale des elements chimiques (1929); Madelung's rule as usually stated (1936). Hund's first rule (Z. Phys. 33, 1925) gives the term. Both are read, not derived.**

### Λ's seed — seven cells

**seed(Λ₈) = 7 exactly — 976 cells from seven, 139 to 1; LB 5, five heuristics 12/7/7/7/40**

*branch and bound over 102 elements*

Computed — M §14.5.9 / twoheur.py; Karp 1972; Johnson 1974.

> **Prior art: the seed problem is minimum set cover, NP-complete (Karp 1972), with a greedy ln n approximation (Johnson 1974). Five heuristics agreeing on 7 against a lower bound of 5 is the measurement.**

### The open-index form, seed + E

**an open index is recovered as seed(ℛ(X)) plus the E cells ℛ(X) holds and X does not; cost seed + E**

*exact on four open indexes; compresses only where E ≪ |X|*

Proved — M §21.5; Moore 1910.

> **Prior art: an open index needs its closure seed plus the cells the closure adds and it does not hold — the decomposition follows from extensivity.**

### The parent-term wall

**an OPEN-SHELL core gives many parent terms and no separable Rydberg series, so its levels can be published and its defect cannot be extracted**

*an ion whose core has an open subshell*

Measured — R 1180; Condon & Shortley 1935; Racah 1943.

Fe IV's 3d4 core carries sixteen LS terms. The capture shows 13 of them, 24 distinct (parent, l, term) series, and EVERY ONE has exactly one member — n = 4 only. Fe IV has ~1,000 analysed levels and no extractable defect. The compendium holds Ne-like and Na-like ions at charge 15 and 16 and no open-shell ion above charge 6, which is not a collection preference but the fact that an open-shell core does not produce the object a quantum-defect index holds

> **Prior art: parent terms and the fractional-parentage decomposition are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah's coefficients of fractional parentage (1943). That an open-shell core gives one series per parent is their structure; the measurement is that Fe IV's 24 series each hold one member.**

> **Prior art: parent terms and coefficients of fractional parentage are Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII, and Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382. That an open-shell core gives one series per parent is their structure; the measurement is that the 24 Fe IV series each hold one member.**

### The regime coordinate

**the SIGN of d2 is a coordinate the ground state cannot supply, and the MAGNITUDE of d2 predicts the channel's own scatter**

*a Rydberg channel with a fitted Ritz curve*

Measured — R 1157-1162; NIST Atomic Spectroscopy compendium; Ritz 1903.

Seaton requires d2 < 0 for polarisation, so a positive d2 says the channel is not what the formula describes. By orbital: s 76% positive, p 74%, d 37%, f 6%, g 7%, h 9%. The two populations differ in median raw spread 0.0159 vs 0.0029 and median fit residual 0.0058 vs 0.0003, U-test p < 1e-5. The MAGNITUDE class predicts the spread at R^2 = 0.761 against l alone at 0.230 and the sign at 0.267, and the sign adds nothing to the magnitude. The three quantities do not separate: d0 against |d2| gives r^2 = 0.270

> **Prior art: the SIGN rule is NIST's own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel's scatter at R^2 = 0.761.**

> **Prior art: the SIGN rule is NIST own — its compendium states that the Ritz coefficient a is usually positive for core-penetration series and negative for core-polarization series. What is measured here is the distribution across 274 channels and that |d2| predicts a channel scatter at R^2 = 0.761.**

### The channel curve

**a channel is a CURVE, not a number: delta(n) = d0 + d2/(n-d0)^2, and the index reaches d0 while nothing in it reaches d2**

*a Rydberg channel with four or more members*

Measured — R 1150-1156; Ritz 1903; Hartree 1928.

the d2 term removes 48% of what the compendium called scatter (0.0199 -> 0.0104 across 274 channels). d0 against ln Ne, l and charge gives R^2 = 0.549; the curvature gives 0.018. The ISOELECTRONIC step moves both coordinates by the same factor at every l — 1.194/0.859 at s, 1.150/0.979 at p, 0.858/0.907 at d, 0.561/0.627 at f — while the l step moves them differently: 1.427/0.752, 3.696/1.373, 8.536/5.264. Along a sequence the channel translates; along l it deforms, and fitting l as a 2x2 map improves on the scalar by only 14% at s->p and 1% beyond

> **Prior art: the extended Ritz formula delta = delta_0 + a/(n-delta_0)^2 + b/(n-delta_0)^4 is Ritz, Zur Theorie der Serienspektren, Ann. Phys. 12 (1903) 264-310, with Hargreaves and Hartree (Proc. Camb. Phil. Soc. 24, 1928) supplying the foundation. NIST's compendium states it in this form.**

### A seed

**G ⊆ X is a seed of X under ℛ iff φ̂(G) = φ̂(X)**

*X closed; ℛ depends on G only through φ̂*

Proved — M §14.5.7; Birkhoff 1937; Moore 1910.

> **Prior art: a generating set of a closure system is any G with cl(G) = cl(X). That the envelope alone decides it is the specific form here; the notion is Moore-Birkhoff.**

### The existence partition

**the index partitions by EXISTENCE STATUS, and nothing in it is impossible**

*the aufbau survey*

Measured — R 1191-1192; Theodosiou, Inokuti & Manson 1986.

101,328 cells. *** THE STATUS AXIS WAS REPLACED AT REGISTER 1578: VERIFIED/POSSIBLE/IMPROBABLE became WITNESSED/UNWITNESSED plus a NAMED BOUND, because improbable is a judgement about the future rather than a fact about the record — the same object-versus-observer fault register 1287 found in `standing`. *** Now: 337 WITNESSED (0.333% of the index) and 100,991 UNWITNESSED, of which 929 are exact by symmetry and need no measurement. Bounds on the rest: series above ng 28,527; no long-lived isotope 24,312; no analysis located at this charge 17,428; open-shell cores 26,641; not naturally occurring 225; and 2,929 with NO bound at all — separable series simply not yet measured. The charge bound is contradicted by twelve measured cells above it in this index's own file (R 1577). Every accuracy figure must be quoted against the witnessed count, not 101,328.

> **Prior art: the distinction between what a survey admits and what is measurable is exactly the distinction Theodosiou, Manson & Inokuti make in their 1986 table across all ionisation stages.**

### The unit template, corrected

**the unit template (3,0,1,1,*,0,1,1) is NOT forced: it appears in 10% of the 24,585 exact minimum covers; its premise — five universal cells, corners as extreme points — fails, because Λ₈ has NO extreme points (non-uniqueness as a Krein–Milman failure (§14.5.11))**

*mid-alphabet values such as q = 1, g = 1, 2S = 1 are alphabet slots owed by the alphabet law and may be carried by many different cells — which is exactly why no single carrier is forced*

Computed — M §14.5.13; SEED-CAP-FINDING; Chvatal 1979.

> **Prior art: Chvátal (1979) — the forcing rule whose hypothesis this cell fails. That 10% of exact covers contain it is the measurement.**

### Non-uniqueness as a Krein–Milman failure

**a cell x is EXTREME when x ∉ ℛ(Λ∖{x}); on record ℛ(Λ∖{x}) = Λ for all 976 cells — Λ₈ has NO extreme points, yet seed = 7: a MAXIMAL failure of the combinatorial Krein–Milman property, and exactly what permits 24,585 minimum generating sets to coexist**

*a closure space where every closed set is the hull of its extreme points is precisely a convex geometry (anti-exchange); ℛ on Λ₈ is as far from one as possible, so no unique minimum seed can exist — the seed's invariant content is the alphabet law (§14.5.12) + the envelope-step law (§14.5.12), never cell identities*

Proved — M §14.5.11; EXPANSION-MC54 P4; Edelman 1980; Edelman & Jamison 1985.

> **Prior art: Edelman, Alg. Univ. 10 (1980) 290-299; Edelman & Jamison, Geom. Dedicata 19 (1985) 247-270 — anti-exchange closures / convex geometries and the combinatorial Krein–Milman theorem. Dilworth (1940) — uniqueness under conditions Λ₈ does not meet; Krein & Milman (1940) — the classical antecedent.**

## F. The family of closed indexes — 4 objects

### The family's defect, exactly

**ℛ(Cl(U)) = 2^U, so E(Cl(U)) = 2^|U| − |Cl(U)| exactly**

*Cl(U) holds ∅ and U, and every ordered pair of points is separated by some closed set, making every envelope constant at 1*

Proved — M §14.6.2; Moore 1910.

> **Prior art: the closure of a set of generators over an unconstrained alphabet is the full power set, so the defect is the exact complement count. A corollary of extensivity and idempotence.**

### The family of closed sets

**the ℛ-closed subsets of a closed index form a Moore family: ∩-closed 100%, ∪-closed 33–69%; 74, 147, 732 members, ∅ counted**

*exhaustive at 8, 9, 16 cells*

Proved — M §14.5, §14.6; register 1789; Moore 1910; Ward 1942.

> **Prior art: the closed sets of a closure operator form a Moore family — intersection-closed with a top. Moore, Introduction to a Form of General Analysis (1910); Ward, The closure operators of a lattice, Ann. Math. 43 (1942) 191-196. That the R-closed subsets of a closed index form one is that theorem applied at one level up.**

### The family theorem

**THEOREM: the family of all closed indexes is itself an OPEN index — E = 182, 365, 64,804**

*every member has E = 0*

Proved — M §14.6; Tarski 1955; Ward 1942.

> **Prior art: the lattice of closed sets of a closure operator is complete (Tarski, A lattice-theoretical fixpoint theorem, Pacific J. Math. 5 (1955) 285-309), but completeness is not the same as being CLOSED under the same operator one level up. That the family of closed indexes is itself open is measured here; the setting is Tarski-Ward.**

### The unstatable family

**and it cannot be stated: a closed index has a seed, an open one costs seed + E, and E is 64,804 at 16 cells**

*corollary of the family theorem (§14.6) and the open-index form, seed + E (§21.5)*

Proved — M §14.6.1; Kolmogorov 1965.

> **Prior art: the cost of stating an object is its description length — Kolmogorov, Three approaches to the quantitative definition of information, Probl. Inf. Transm. 1 (1965) 1-7. A closed index has a seed; an open one costs seed plus defect, and the difference is the statement cost.**

## G. Graphs, constraints and languages — 12 objects

### The index of all constraints

**every genuine constraint in the book, indexed over five coordinates: 22 carried by ℛ, 2 by ℛ₄, NONE by neither; E = 21, E₄ = 6, orientation cost 15**

*eight rows of a first attempt were coordinate systems entered as constraints; the two that no operator carried were both of those*

Computed — M §21.5.5 / allcons.py; Freuder 1978.

> **Prior art: indexing constraints by the coordinates they name is the constraint-hypergraph view — Freuder, CACM 21 (1978) 958-966.**

### The book as an index

**E(book) = 578 at chapter resolution, 0 at part resolution; a certificate exists**

*claim-bearing paragraphs with a § citation*

Computed — M §30.1; Rota 1964.

> **Prior art: that a defect depends on the RESOLUTION at which an object is indexed is the coarsening question; Moebius inversion over a refinement lattice is Rota (1964).**

### The constraint index

**Λ's seven constraints form a TREE — 8 nodes, 7 edges — with ZERO of 35 triples spanning three nodes**

*no 3-body among the constraints*

Computed — M §21.5.2; Freuder 1982; Dechter & Pearl 1989.

> **Prior art: that a tree-structured constraint graph is globally consistent after arc consistency is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32; the width/induced-width machinery is Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### The constraint graph

**Λ₁₃'s constraint graph: 13 nodes, 14 edges, girth 3, diameter 6, radius 4, treewidth 2, hub k at degree 4, cycle rank 2, one triangle — 2S′, g, v — from Λ₁₀ onward**

*treewidth 2 at Λ₁₃ keeps Freuder's bound and §21.5.1's one-level shortfall; the triangle is that K₃, inside the tower*

Computed — M §12.11.1, §21.5.3; register 1790; Euler 1736; Diestel 2017.

> **Prior art: girth, diameter, radius and treewidth are standard graph invariants — see Diestel, Graph Theory (5th ed., 2017). Graph theory itself begins with Euler, Solutio problematis ad geometriam situs pertinentis (1736).**

### The seven near-misses

**Λ is one edge from a 3-body in exactly seven places, one per existing edge**

*every one a bond the physics does not make*

Computed — M §21.5.2; Berge 1962.

> **Prior art: adding one edge to a tree creates exactly one cycle; the number of places is the number of existing edges. Berge, Theorie des graphes (1958/1962).**

### The protocol index

**the 24 protocols occupy 19 cells in four coordinates; §2.8 and §2.24 share one**

*§2.24 is §2.8 specialised to heuristics*

Computed — protindex.py; Freuder 1978.

> **Prior art: as the index of all constraints (§21.5.5), applied to the protocol index.**

### The reference index

**the reference index: 38 cells, box 144, E = 0, and NOT a tree — access closes a cycle**

*access, referent, checked, verdict*

Computed — M §16.6.1; Freuder 1982.

> **Prior art: a non-tree constraint graph that nonetheless closes shows treeness is sufficient and not necessary — the converse direction of Freuder (1982).**

### The register as an index

**E(register) = 6 at 68.8% density, and R recovers repair ≤ φ(corroboration)**

*coordinates assigned from the entry text*

Computed — M §28.9; Shannon 1948.

> **Prior art: recovery under a noisy channel is bounded by the channel capacity; that repair ≤ φ(corroboration) is that bound in this setting. Shannon (1948).**

### Shape decides the seed

**the constraint graph's shape decides the seed: path 8, star 6, balanced trees 6, forest 5 on six nodes over one alphabet; neither extreme is cheapest**

*seed is monotone in S with no exception, all six exact by branch and bound*

Computed — M §21.5.4; Freuder 1982; Dechter & Pearl 1989.

> **Prior art: that the constraint graph shape decides what a local method achieves is Freuder 1982 for trees and Dechter & Pearl 1989 for the general induced-width bound.**

### Statistics as a language

**statistics is a sixth language: max-entropy closure on the pairwise marginals recovers Λ at 976, E = 0, restores a deleted cell, and GROWS on an added one, 976 to 1,048**

*its signature matches the information language, not order/geometry/analysis; the five split three-two between absorbing and growing*

Computed — M §20 / stat_lang.py; Deming & Stephan 1940; Csiszar 1975.

> **Prior art: the max-entropy distribution matching given marginals is reached by iterative proportional fitting — Deming & Stephan, Ann. Math. Stat. 11 (1940) 427-444; its information-geometric characterisation is Csiszar, I-divergence geometry, Ann. Prob. 3 (1975) 146-158.**

### The cycle rank of the tower

**the tower's cycle rank rises by one at each two-parent axis — 0,0,1,1,2,2 — and the first of the two cycles is a triangle: triangles 0,0,1,1,1,1**

*the tree breaks at Λ₁₀, where v takes 2S′ and g as parents and 2S′ ≤ g already holds*

Computed — M §12.11.1, §21.5.2; register 1790; Berge 1962.

> **Prior art: the cycle rank |E| - |V| + c is the first Betti number of a graph — Berge, Theorie des graphes et ses applications (1958/1962). That it rises by one at each two-parent axis is the measurement.**

### Independence is a triple property

**independence is a property of TRIPLES: surviving tests go as (1-f)^3, not (1-f)**

*the bracket relates T(n-1), T(n), T(n+1)*

Computed — M §24.9; Dawid 1979; Pearl 1988.

> **Prior art: conditional independence is a relation on TRIPLES and obeys the graphoid axioms — Dawid, Conditional independence in statistical theory, J. R. Stat. Soc. B 41 (1979) 1-31; Pearl, Probabilistic Reasoning (1988), ch. 3.**

## L. Λ's own constraints — 68 objects

### The closure theorem

**E(Λ) = 0**

*at the stated caps; verified at four settings and through the f shell*

Computed — M §7.3, reg. 236; Moore 1910; Freuder 1982.

> **Prior art: E = 0 says the index equals its own closure. Moore (1910) for the operator; Freuder (1982) for why a tree-structured constraint graph gives it.**

### The generating function

**F = Σ_n z₁ⁿ Σ_{ℓ≤n−1} z₂^ℓ Σ_{k≤4ℓ+2} z₃^k [Σ_{S≤k} z₈^S] Σ_{q≤k} z₄^q Σ_e z₅^e Σ_{f<e} z₆^f Σ_{g≤min(q,4f+2)} z₇^g**

*at stated caps; the tree has no cycles so the sum factorises*

Computed — M §11.3; Euler 1748; Stanley 1986.

> **Prior art: a multivariate generating function over a constrained region, written as nested sums. Euler, Introductio (1748); Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### The cardinality

**F(1,…,1) = |Λ| = 976**

*as L.F*

Computed — M §11; Euler 1748; Stanley 1986.

> **Prior art: setting all variables to one recovers the cardinality — the elementary specialisation of a generating function.**

> **Prior art: F(1,...,1) = |X| is the elementary specialisation of a generating function. Euler, Introductio (1748), ch. XVI; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1.**

### The alternating specialisation

**F(−1) = 2, and the number has a cause — proved at the stated caps. F(−1) counts even-rank cells against odd, and two escapes had to be closed before the 2 meant anything. A pairing argument cannot cancel it: the duality map σ(x) = top − x sends rank to 20 − rank, and 20 is even, so σ preserves rank parity and can pair like only with like; the eight cells that survive x → top − x (§8.3) all have even rank — 6, 8, 8, 10, 10, 12, 12, 14 — and contribute +8, not 0, while σ fixes nothing, the top's odd entries making 2x = top impossible. And the source is the tree: a coordinate summed freely over an even number of consecutive values kills an alternating sum, and ℓ and f each have exactly two — Σ(−1)ⁿ = −1 for n = 1…3, Σ(−1)^ℓ = 0 for ℓ = 0…1, Σ(−1)^e = −1 for e = 1…3, Σ(−1)^f = 0 for f = 0…1 — so the free box has F_box(−1) = 0 exactly, and if the coordinates were free the alternating sum would vanish. The constraints couple ℓ to n and f to e, and every potentially vanishing range is clipped by its parent — ℓ runs to n−1, f to e−1, k to 4ℓ+2, q to k, g to q and 4f+2, 2S to k — so no zero factor ever appears free, and the elimination along the tree at z = −1 leaves a residue of exactly 2, confirmed against the rank polynomial (§11.1) directly and through the detachable leaf's factorisation (§11.6), whose spin sum at −1 is 1 for k even and 0 for k odd, localising the whole residue on the k = 2 cells. So F(−1) = 2 measures the same thing the skew of §8.3 and the eight survivors measure — the tree's asymmetry — by a third route: three routes, one fact**

*at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); σ(x) = top − x with top = (3, 1, 3, 3, 3, 1, 3, 3), rank 20*

Proved — M §11.8.1; Euler 1748; Stanley 1986.

> **Prior art: F(−1) is the difference between even- and odd-rank counts, the standard alternating specialisation — Euler (1748); Stanley, *Enumerative Combinatorics I* (1986), ch. 3, where it is related to rank symmetry. That the free box vanishes while the tree's couplings leave a residue of 2, and that the residue, the skew and the eight survivors are one fact, are this book's.**

### The join-irreducible count

**|J(Λ)| = Σ_i (|A_i| − 1)**

*each generator is min{x ∈ Λ : x_c ≥ v} for one coordinate and one value*

Computed — M reg. 268; Birkhoff 1937.

> **Prior art: the join-irreducibles of a product of chains are the coordinate steps, so |J| = sum(|A_i| - 1). Immediate from Birkhoff representation.**

### The amplification

**A(y) = |ℛ(Λ ∪ {y})| − |Λ| − 1; over every insertable cell of Λ₈'s alphabet box — 5,936 — min 15, median 309, max 1,795, no exception**

*y a single inserted cell; population the 6,912-cell alphabet box less Λ₈; exhaustive at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1)*

Proved — M §16.8.4; register 1791; Rota 1964.

> **Prior art: the change in a closure count on adding a generator; the amplification is measured, the closure is Moore-Rota.**

### Divisor lattice embedding

**N(x) = ∏_i p_i^{x_i}; x≤y ⟺ N(x)|N(y); ∨↦lcm, ∧↦gcd, rank ↦ Ω(N)**

*p_i the i-th prime. The rank correspondence is an identity, not a convention: Ω(N(x)), the number of prime factors of N(x) counted with multiplicity, sums the exponents, Σ_i x_i, which is the lattice rank of modularity (equality, not submodularity) (§8.2); so rank(x) = Ω(N(x)) on every cell, while the distinct-prime count ω(N(x)) of distinct-prime-counting function (§9.1) drops the multiplicities and reads instead the number of occupied coordinates. The two prime-counting functions read the two invariants — Ω the rank, ω the coordinate support — off the one number N(x)*

Computed — M §9; Birkhoff 1937.

> **Prior art: the divisor lattice with lcm as join and gcd as meet is the classical arithmetic model of a product of chains. Birkhoff, Lattice Theory (1940), ch. II.**

### The Birkhoff representation

**Λ ≅ down-sets of J(Λ) under x ↦ {j ∈ J : j ≤ x}; |J(Λ)| = 17, 20 covering relations — proved by exhaustion: all 2¹⁷ = 131,072 subsets of J(Λ) tested, exactly 976 are down-sets, matching |Λ| cell for cell; the seventeen fall into fifteen coordinate-support patterns — a generator's pattern being the set of coordinates on which it exceeds the bottom cell (1,0,1,0,1,0,0,0) — and the patterns are cap-independent: at caps (3,3,1,3,1), (4,4,2,4,1), (4,4,2,6,2), (5,5,2,6,2) the generator count grows 17, 24, 33, 35 while the fifteen hold with zero new and zero lost, only multiplicities changing**

*Λ finite distributive; join-irreducible = covers exactly one cell, computed on the rank grading modularity (equality, not submodularity) (§8.2) licenses*

Proved — M §8.3; Birkhoff 1937.

> **Prior art: Birkhoff's representation theorem, Duke Math. J. 3 (1937) — every finite distributive lattice is the down-sets of its join-irreducibles. |J| = 17 is a computation inside that theorem; the cap-sweep of the fifteen patterns is the measurement.**

### The Boolean representation

**Λ is the 976 words in {0,1}¹⁷ that are down-sets of J(Λ); join = OR, meet = AND; 17 bits carried, 9.93 needed, 7.07 surplus — proved. The map cell ↦ {generators beneath it}, written as a bit-string, is injective on the 976 cells and so a bijection onto its image; it carries the lattice operations to the bitwise ones exactly, with zero failures for join and zero for meet over all 475,800 unordered pairs, which is Birkhoff's correspondence restated in positions rather than sets. The seventeen bits are not free of one another: the twenty cover-implications of the implication circuit (§11.1.1) cut the ambient 131,072 words to exactly these 976, so the surplus is not spare capacity and no bit is removable, every generator being join-irreducible by construction — the redundancy lives in the implications, where in a closed index it always lives. The accounting: 17 bits carried per cell, log₂976 = 9.93 needed to index the cells, 7.07 surplus, and Λ occupies 0.7446 % of the space it is written in**

*Birkhoff correspondence*

Proved — M §11.1.1; Birkhoff 1937; Shannon 1938.

> **Prior art: Birkhoff (1937) gives the down-set representation; encoding down-sets as Boolean words with OR as join and AND as meet is Shannon (1938).**

### The box factorises

**|box ∩ Λ| is in closed form because the constraint graph is a tree, and the closed form exists exactly when it is — proved. For a box [lo, hi] in the ambient product of chains, |box ∩ Λ| = Σ_z ∏_{(i,j)} [zᵢ ≤ φ(zⱼ)], the sum over the box's points of the product of the seven edge indicators. Eliminate the coordinates one at a time, always a vertex with at most one live neighbour: each step sums one coordinate out of the factors that mention it and leaves a message that is a function of that single neighbour, so no intermediate table ever has two arguments and no term is ever subtracted. Peeling the two pendant vertices of the caterpillar n—ℓ—k—q—g—f—e with 2S at k (the constraint tree (§8.5)) gives the two leaves in closed form — #{2S} = max(0, min(hi₇, k) − lo₇ + 1) and #{g} = max(0, min(hi₆, q, 2(2f+1)) − lo₆ + 1), a leaf under a monotone bound being the length of its interval clipped by the bound — and what remains is the main volume's formula, |box ∩ Λ| = Σ over n, ℓ, k, q, e, f in the box of [ℓ ≤ n−1][1 ≤ k ≤ 2(2ℓ+1)][q ≤ k][f ≤ e−1] · #{2S ≤ k} · #{g ≤ min(q, 2(2f+1))}; the void is then the void (§10)'s difference ∏ᵢ(hiᵢ − loᵢ + 1) − |box ∩ Λ|. Verified: the eight random intervals of §10.4 reproduced, then exhaustively — every box [x∧y, x∨y] over all 475,800 unordered pairs and the 976 singletons, 116,138 distinct boxes, zero discrepancies against direct enumeration; the full peel, one coordinate per step, measures message arity 1 at every step and agrees with enumeration on 100 random boxes at each of 976, 8,847 and 25,748 cells, the argument using no cap. Conversely the closed form is the tree's and nothing weaker: a constraint graph has width 1 if and only if it is a forest (Freuder), so once it carries a cycle every elimination order produces a message in two coordinates, and the route back to one-coordinate counts is the Rota sieve over the cycle's constraints, alternating in sign — a cycle forces an inclusion–exclusion term. Witnessed on Λ: closing the triangle k—q—2S with the constraint 2S ≤ q+1, which cuts 976 cells to 911 and so is not redundant, raises the elimination width to 2; the tree-style count that ignores the closing constraint is wrong on 9 of 40 random boxes, and the eight-term sieve over the triangle is right on all 40 — on the box lo = (2,1,2,0,2,0,0,0), hi = (3,1,3,2,3,1,1,3) the tree count is 280, the true count 240, and the 40 removed are exactly the box's points of Λ violating 2S ≤ q+1. The chain rule that factorises the void-free fraction (§10.2)'s joint law along the tree and the elimination that gives this count are one machinery**

*box [lo, hi] in the ambient product of chains; coordinates in the order (n, ℓ, k, q, e, f, g, 2S), the leaf subscripts 6 and 7 counted from zero in that order as in §10.4; exhaustion at the base caps (n,e,ℓ,k,f) = (3,3,1,3,1); cap-independence sampled at (4,4,2,5,1) and (5,5,2,6,1); the converse holds for any set cut by binary constraints on a product of chains, not only Λ*

Proved — M §10.4; Freuder 1982; Rota 1964; Lauritzen 1996.

> **Prior art: the count factorises over a tree — no Moebius sieve is needed because there are no cycles to inclusion-exclude over. Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982): width 1 if and only if the constraint graph is a tree, in both directions. Rota (1964) for what the sieve costs once a cycle is present. Elimination along a tree as the chain rule: Lauritzen, Graphical Models (1996). That Λ's two leaves are interval lengths clipped by a monotone bound, and the witness on the closed triangle, are this book's.**

### Node counting, ℓ ≤ n − 1

**ℓ ≤ n − 1**

*hydrogenic radial solution*

Cited — M §7.1; Bohr 1913; Schroedinger 1926.

> **Prior art: l ≤ n-1 is the angular-momentum constraint of the hydrogen solution — Bohr, On the constitution of atoms and molecules, Phil. Mag. 26 (1913) 1-25; Schroedinger, Quantisierung als Eigenwertproblem, Ann. Phys. 79 (1926) 361-376.**

### Pauli, k ≤ 4ℓ + 2

**k ≤ 2(2ℓ+1) = 4ℓ+2**

*Pauli exclusion*

Cited — M §7.1; Pauli 1925; Stoner 1924.

> **Prior art: the subshell capacity 2(2l+1) is Stoner, The distribution of electrons among atomic levels, Phil. Mag. 48 (1924) 719-736, made exclusive by Pauli, Z. Phys. 31 (1925) 765-783.**

### The transfer bound

**q ≤ k**

*counting*

Definitional — M §7.1; Pauli 1925.

> **Prior art: q ≤ k, a transferred count cannot exceed the occupancy. Pauli (1925).**

### Node counting, f ≤ e − 1

**f ≤ e − 1**

*hydrogenic radial solution*

Cited — M §7.1; Bohr 1913.

> **Prior art: as node counting, ℓ ≤ n − 1 (§7.1), applied to the second shell pair.**

### Pauli, g ≤ 4f + 2

**g ≤ 4f+2**

*Pauli exclusion*

Cited — M §7.1; Stoner 1924; Pauli 1925.

> **Prior art: as Pauli, k ≤ 4ℓ + 2 (§7.1), applied to the second shell pair.**

### The second transfer bound

**g ≤ q**

*counting*

Definitional — M §7.1; Pauli 1925.

> **Prior art: g ≤ q, as the transfer bound (§7.1) on the second shell pair.**

### Vector coupling

**2S ≤ k**

*vector coupling on the source*

Cited — M §7.1; Hund 1925; Pauli 1925.

> **Prior art: 2S ≤ k because at most k electrons can align their spins — Pauli exclusion (1925) with Hund first rule, Z. Phys. 33 (1925) 345-371.**

### The occupancy floor

**k ≥ 1 (definitional restriction, not a bound)**

*a cell is a transition, not a state*

Definitional — M §10.2, reg. 301; Pauli 1925.

> **Prior art: k ≥ 1 restricts to occupied subshells; definitional rather than a bound.**

### The surface is a cylinder

**Λ's derived quantities split into two classes — *e*, ν, *V* rising up a series and *T*, *r*, δ, spacing, *w* falling — exchanged under the map ν ↦ ν⁻³, so the sign structure is bipartite; and a bipartite sign structure can reverse orientation only an even number of times along any closed traverse, which makes the surface orientable, a cylinder and not a Möbius band. The finding is a reason, not an absence of one: verified exhaustively, zero orientation-reversing loops among all cycles of length 3 through 5, and both alternative routes to a twist close by construction — a non-monotone quantity contributes an *undefined* edge rather than a reversing one, and a quantity independent of ν contributes *no* edge, leaving no third way to build a reversal. The structural guarantee is underwritten by the shape of the constraint graph itself: it is a tree — eight vertices and seven edges, connected and acyclic, measured in every other shape the lattice contains (§12.9) — so §12.1's orientability follows from the construction and not from a search that merely failed to find a counterexample. The cylinder is a cylinder over the transfer coordinate *q*, the base of the fibration whose fibres the two-body separation (§12.6.1) computes.**

*the two derived-quantity classes of §12.1 under ν ↦ ν⁻³; orientability certified exhaustively over cycles of length 3–5 and structurally from the tree constraint graph; at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.1; König 1936; Harary 1953; Listing 1861; Möbius 1865; Freuder 1982.

> **Prior art: a graph is bipartite exactly when it carries no odd cycle — König, *Theorie der endlichen und unendlichen Graphen* (1936); a sign structure whose classes exchange is balanced, every cycle carrying an even number of reversals — Harary, *Michigan Math. J.* 2 (1953); the one-sided band the finding excludes is Listing (1861) and Möbius (1865); a constraint graph of width one is a forest, so carries no cycle to twist — Freuder, *J. ACM* 29 (1982). That Λ's ascending and descending quantities form exactly such a bipartite sign structure under ν ↦ ν⁻³, and that its constraint graph is the tree which forces orientability by construction rather than by search, is this book's.**
### The most active constraint is the coupling itself

**Of the seven bounds that cut Λ from its box, g ≤ q removes the most. Ranked by marginal exclusion — the cells that satisfy all six other bounds and fail only this one — g ≤ q leads at 673, then q ≤ k at 575, k ≤ 4ℓ+2 at 564, ℓ ≤ n−1 at 308, 2S ≤ k at 300, f ≤ e−1 at 200, and the two that barely bind, k ≥ 1 at 25 and g ≤ 4f+2 at 24. And the bound that binds hardest is the only one relating a target coordinate to a source coordinate: g ≤ q reads placed ≤ removed, the electrons arriving cannot outnumber those the source gave up. Remove it and the two ends of the tree separate into an index of source configurations beside an index of target configurations — a product of states; keep it and each cell is a move that conserves what it transfers. The most active constraint and the coupling are one bound, and it is the bound that makes Λ a cylinder over the transfer rather than a rectangle of states.**

*the seven constraints ranked by marginal exclusion over the value box of Λ₈ — g ≤ q first at 673, then q ≤ k 575, k ≤ 4ℓ+2 564, ℓ ≤ n−1 308, 2S ≤ k 300, f ≤ e−1 200, k ≥ 1 25, g ≤ 4f+2 24 — measured on the rebuilt Λ₈ at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); that g ≤ q alone binds a target to a source is read from the constraint graph.*

Proved — M §13.3; Birkhoff 1940.

> **Prior art: the count of cells an inequality removes from a product of chains is a direct enumeration, and that a graded lattice is a cylinder over a base exactly when one relation binds its two ends is Birkhoff (1940). That g ≤ q is the most active of Λ's seven constraints — 673 otherwise-admissible cells, more than any other — and is the coupling, the sole target-to-source bound whose removal collapses the index of transitions into a product of states, is this book's.**


### The two-body separation

**The lattice does not factorise, and then it does. As a bare product of its two ends it fails — |A| × |B| × |q| = 33 × 17 × 4 = 2,244 against 976 — because the ends are coupled twice over, q ≤ k tying the transfer to the parent and g ≤ q tying the target's occupancy to the transfer. Conditioned on the coupling they separate exactly: |Λ| = Σ_q |A(q)| × |B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 165 + 330 + 345 + 136 = 976, exactly. One end is the parent configuration (n, ℓ, k) with its spin 2S, the other the target (e, f) with its occupancy g, and they meet at q, the number transferred — the shape of a two-body problem, two objects and a coupling, separating as a two-body problem separates, into centre-of-mass and relative motion with q in the role of the conserved coupling. The exactness is the tree's doing: q is a cut vertex of the constraint tree (§8.5), so fixing it severs every path between the two sides, and the count of a severed pair is a product — the same separator property that makes the box factorisation (§10.4) close in one pass. The four section counts 165, 330, 345, 136 are the cylinder's profile, computed rather than drawn: the base is q — the axis along which the surface is a cylinder (§12.1) — and the fibre at each q is A(q) × B(q).**

*the two ends A = (n, ℓ, k; 2S) and B = (e, f; g) of the constraint tree, coupled through q by q ≤ k and g ≤ q; separation verified by exhaustive enumeration at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.6.1; Newton 1687; Lauritzen 1996.

> **Prior art: that a two-body problem separates into centre-of-mass and relative motion about a conserved coupling is Newton's reduction (*Principia*, 1687); that conditioning on a separating vertex of a tree renders the two sides independent — the property that turns a coupled count into a sum of products — is Lauritzen, *Graphical Models* (1996). That Λ's eight coordinates are two such bodies, parent and target meeting at the transfer, with the bare product 2,244 failing and the conditioned sum returning 976 exactly — the cylinder's profile 165, 330, 345, 136 — is this book's.**

### The fibres, in closed form

**Each side of the cylinder has its own closed expression, and they are different shapes. A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k · (1 − z^{min(k,3)+1})/(1 − z) and B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f · (1 − z^{min(q,4f+2)+1})/(1 − z), each trailing factor a finite geometric sum counting the pendant coordinate — 2S ≤ k on the A side, g ≤ min(q, 4f+2) on the B side. Both verified against enumeration at every q as full polynomial identities, coefficient by coefficient, not merely at the evaluations; the evaluations A_q(1) = 33, 33, 23, 8 and B_q(1) = 5, 10, 15, 17 recover the profile of the two-body separation (§12.6.1). And the two sides are not the same tree: A_q is a caterpillar — the path n—ℓ—k with 2S pendant at k — while B_q is a path, e—f—g, capped by the base, so the whole lattice is a caterpillar because it is these two glued at q, and the pendant sits on the A side only. The fibration iterates: Λ fibres over q with fibre A_q × B_q; A_q fibres over k with fibre an (n, ℓ)-set times the 2S-chain; B_q fibres over f with fibre an e-set times the g-chain — three levels, each verified an exact product at every value of its base, and at the bottom every fibre is a product of chains, a box, with the closed form Box(a, b)(z) = ∏ᵢ z^{aᵢ}(1 − z^{bᵢ−aᵢ+1})/(1 − z). Each level closes for the reason the two-body separation is exact: fixing the base variable severs the fibre into independent factors — the elimination of the box factorisation (§10.4), run level by level to a floor of boxes.**

*the two fibre polynomials at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); identities verified per q by exhaustive coefficient comparison; all three fibration levels verified as exact products.*

Proved — M §12.7; Euclid c. 300 BCE; Euler 1748; Steenrod 1951; Harary & Schwenk 1973; Stanley 1986; Lauritzen 1996.

> **Prior art: the finite geometric sum is Euclid, *Elements* IX.35; counting by generating function is Euler, *Introductio in analysin infinitorum* (1748); the rank generating function of a graded poset is Stanley, *Enumerative Combinatorics I* (1986); the caterpillar is named in Harary & Schwenk (1973); the fibration language is Steenrod, *The Topology of Fibre Bundles* (1951); elimination along a tree, one vertex at a time, is Lauritzen, *Graphical Models* (1996). That the cylinder's two sides carry different trees — caterpillar against path, the pendant on one side only — with closed forms exact at every q, and that the fibration iterates in three levels to a floor of boxes, is this book's.**

### Four numbers, five facts

**The counts 165, 330, 345, 136 carry more than their sum — five facts read off the table, every one verified exhaustively. First, a Pareto frontier inside the lattice: |A_q| falls 33, 33, 23, 8 while |B_q| rises 5, 10, 15, 17, so raising the transfer costs the parent and pays the target, monotonically, and no q improves both — the shape of §23.5's dw/dh > 0 with dV/dh < 0, which the book presents as a fact about brackets and is here a fact about the index itself. Second, a most-probable transfer: the fibre peaks at q = 2 with 345 cells, 35.3% of Λ, the sequence is log-concave hence unimodal, and the mean transfer ⟨q⟩ = 1428/976 = 1.4631, sd 0.930, is S′(1)/S(1) in the base variable — the number of electrons moved, averaged over every admissible configuration. Third, an 8-to-3 compression that loses no count: Λ's generating function has eight variables, the shape has three, and S(1,1,1) = 976 — not a projection that forgets cells but one that forgets which coordinate inside each side and keeps how many, a general fact about caterpillars, a path with one pendant reducing to (base, left, right) whatever its length. Fourth, every cross-section is itself a closed, modular lattice: all eight slices — A_q and B_q at each of the four q — are closed under coordinatewise join and meet with E = 0, and the modular law x ∨ (a ∧ b) = (x ∨ a) ∧ b for x ≤ b holds on all 31,519 conditioned triples across the eight slices with zero failures; each slice is in fact distributive, all 93,966 triples passing, as a sublattice of a product of chains must be — the sublattice closure (§7.3) restricting to each fibre. The shape is not a cylinder over an arbitrary set; it is a cylinder whose every cross-section satisfies this book's own law. Fifth, E(X) gains a local form: E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q, and the second does not follow from the first — a closed index could in principle carry defective slices, and here none do, a new invariant.**

*the fibre table of the two-body separation (§12.6.1); all five facts at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); closure, the modular law and the distributive law checked on every triple of every slice; the mean exact as 1428/976.*

Proved — M §12.8; Pareto 1896; Laplace 1812; Dedekind 1900; Birkhoff 1937; Harary & Schwenk 1973; Stanley 1989.

> **Prior art: the frontier on which no move improves both objectives is Pareto, *Cours d'économie politique* (1896); the mean as G′(1)/G(1) of a generating function is Laplace, *Théorie analytique des probabilités* (1812); that a positive log-concave sequence is unimodal is elementary, surveyed in Stanley (1989); the modular law is Dedekind (1900); that a sublattice of a product of chains is distributive, hence modular, is Birkhoff (1937); the caterpillar reduction to (base, left, right) rests on Harary & Schwenk (1973). That the fibre table carries all five at once — a Pareto frontier inside an index, a most-probable transfer, a count-preserving compression, cross-sections every one closed and modular, and a local form of E — is this book's.**

### Every other shape the lattice contains

**Intervals, antichains, chains — and one shape absent. An interval [x, y] is a box exactly when no constraint binds across it: I_{x,y} = Box(x, y) ⟺ for every constraint u ≤ φ(v), y_u ≤ φ(x_v) — the record tested sixty of sixty, and the criterion is here proved by exhaustion, agreeing with direct enumeration on all 115,162 comparable intervals without exception. Boxes are 31,604 of 115,162 — 27.4%, the record's sampled 27% now the exact population figure — and the other 72.6% are where the physics is active: some constraint binds. The binding rates rank the constraints — the record's sample reads g ≤ q at 35.6%, q ≤ k at 33.0%, g ≤ 4f + 2 at 4.9% (§12.9), and over the full population of meet-join intervals [x∧y, x∨y] of all 475,800 unordered pairs, exhaustively, the rates are 30.0%, 28.0% and 1.9% — the same order on both bases. The most active constraint is the coupling; the least is the Pauli bound — which §16.8 finds the cheapest to violate; two independent measures, one answer. The eighteen rank levels partition Λ into eighteen antichains while every maximal chain carries exactly eighteen cells, so the minimum antichain partition and the maximum chain meet at eighteen — Mirsky's dual of Dilworth, exactly attained; the largest level, 122 at rank 11, is the largest antichain outright, certified by the Dilworth chain partition of the Sperner property (§8.4), and Λ is exactly eight times its widest level, 976 = 8 × 122. Λ is the lattice of down-sets of its seventeen join-irreducibles — the Birkhoff representation (§8.3) — so its maximal chains are the linear extensions of that seventeen-element poset: e(P) = 1,113,045,672, recomputed independently this build on the rank grading and exact, where counting linear extensions is #P-complete in general. And the two seventeens are one: every cover adds exactly one join-irreducible, so a maximal chain of seventeen steps enumerates the seventeen generators of §8.3 one at a time — the book reports both numbers without connecting them, and the connection is that they are the same count. One shape is absent: the constraint graph is eight vertices and seven edges, connected and acyclic — measured, a tree — so there is no Möbius band, no cycle, no non-planar minor, nothing to twist and nothing to close; the orientability of the surface — the surface is a cylinder (§12.1) — follows by construction, not by search.**

*the interval census exhaustive over all 115,162 comparable intervals at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); binding rates on two bases, the record's sample and the exhaustive meet-join population, each named; e(P) by independent chain-counting on the rank grading.*

Proved — M §12.9; Birkhoff 1937; Stanley 1986; Brightwell & Winkler 1991; Sperner 1928; Dilworth 1950; Mirsky 1971; Listing 1861; Möbius 1865; Kuratowski 1930; Wagner 1937; Freuder 1982.

> **Prior art: a finite distributive lattice is the down-sets of its join-irreducibles — Birkhoff (1937); its maximal chains correspond to the linear extensions of that poset — Stanley, *Enumerative Combinatorics I* (1986), Prop. 3.5.2, carried from the entry this one absorbs; counting linear extensions is #P-complete in general — Brightwell & Winkler (1991); the largest antichain at a rank level is the Sperner property (Sperner 1928), certified by chain partition after Dilworth (1950); the dual — minimum antichain partition equals maximum chain — is Mirsky (1971); the one-sided band the census excludes is Listing (1861) and Möbius (1865); the minor characterisation of planarity is Kuratowski (1930) and Wagner (1937); a width-one constraint graph is a forest — Freuder (1982). That the box criterion is exact on the whole population, that the binding rates rank coupling first and Pauli last on two independent bases, that the eighteens meet with Mirsky attained, that the seventeens are one — a maximal chain enumerating the seventeen generators one cover at a time — and that Λ is eight times its widest antichain, is this book's.**

### Transitions compose

**Λ₈ cannot be iterated: its source (n, ℓ, k, 2S) is four coordinates and its target (e, f, g) is three, so a transition's output is not a legal input and no second step exists — the asymmetry is a missing spin. The ninth axis supplies it. Giving the target its own multiplicity 2S′ ≤ g under exactly the source's constraint forms — f ≤ e−1 against ℓ ≤ n−1, g ≤ 4f+2 against k ≤ 4ℓ+2, 2S′ ≤ g against 2S ≤ k — makes all 1,654 targets of Λ₉ legal sources. Define the composite b ∘ a whenever a's target equals b's source: it runs a's source to b's target and transfers min(q_a, q_b), no more than was taken and no more than arrives. Λ₉ is closed under this composition exhaustively — 41,682 composable pairs, zero failures — and associative, verified on all 842,206 composable triples with none failing, sharpening the record's 8,434-triple sample to the whole population. Λ₉ is therefore not merely a lattice of transitions but a category of them, and composition is time: not a stamp on a cell but an order between cells. And Λ₉ is the only stage of the tower that composes — composition needs the target's coordinate set matched by a source set of the same shape, and every axis above the ninth attaches to one end or to the joint object, so the shapes part company: Λ₈ three against four, Λ₁₀ has no source seniority, Λ₁₁'s 2J_c is the source's alone, and Λ₁₂ and Λ₁₃ bind joint coordinates that are not end coordinates. So the tower carries three gradings, not two. The dichotomy of the six axes (§12.11.3) sorts them into counting and coupling, exact and envelope; composability sorts them more strictly, and is lost at axis 10 — one step before exactness — because v is a counting coordinate that closes exactly and still has no source counterpart. An axis can be exact and not composable; none is composable and not exact. And what fails to compose is nameable: at the tenth axis, where the composable fraction peaks at 2,050 of 2,535, the 485 cells that do not compose are exactly the 485 with g = 0 — every g = 0 cell and no other — a transition that empties its target subshell, which is k ≥ 1 seen from the other end.**

*the composition b ∘ a defined by target-source matching with transfer min(q_a, q_b); closure verified by exhaustive enumeration of all 41,682 composable pairs and associativity over all 842,206 composable triples at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.11.0; Eilenberg & Mac Lane 1945; Mac Lane 1971.

> **Prior art: a class of objects with composable, associative arrows carrying identities is a category — Eilenberg & Mac Lane, *Trans. Amer. Math. Soc.* 58 (1945), the standard reference being Mac Lane, *Categories for the Working Mathematician* (1971). That Λ₈'s four-against-three asymmetry blocks iteration, that adjoining the target multiplicity 2S′ ≤ g repairs it so all 1,654 targets are legal sources, that Λ₉ is then closed under composition on all 41,682 pairs and associative on all 842,206 triples with zero failures, and that composability is a strictly finer grading than exactness — lost at the tenth axis, one step before the eleventh — is this book's.**

### The six axes of the tower

**Five coordinates carry Λ₈'s object of transitions up to Λ₁₃, and each is a physical degree of freedom no function of the coordinates below it expresses — the door Theorem 17.1 (§17.1) requires every legitimate axis to enter by. The ninth adds the target's multiplicity 2S′ ≤ g; the tenth its seniority 2S′ ≤ v ≤ g, Racah's pairing depth; the eleventh the core's fine structure 2J_c ≤ φ̂(k); the twelfth the core–orbit orientation 2K ≤ 2J_c + 2f_max; the thirteenth the outer electron's spin bit |2J − 2K| ≤ 1. Every stage is closed — E = 0 at all six, verified not by pair-testing but by the characterisation that X is closed iff ℛ(X) = X (the closure characterisation, §14.1), a sweep of the ambient box rather than of the pairs, so the top stage's 47,775,744 ambient cells are each decided and no stage admits a cell it does not contain: 976, 1,654, 2,535, 13,585, 70,905 and 199,130 cells against boxes 6,912, 27,648, 110,592, 663,552, 5,308,416 and 47,775,744. Each stage projects exactly onto the one below. The densities — the values the coupling realises over the values the bound admits — are 63.7, 67.5, 44.7, 17.0, 31.4 and 64.4 % at the caps of §7.4, and three of the six exact sets are not the obvious ones: seniority at the tenth means the terms new at occupancy v, terms(f^v) less terms(f^{v−2}) as multisets; the core's J at the eleventh is restricted to terms carrying the cell's own multiplicity, not all terms of ℓᵏ; the target spin at the ninth is the spin set of f^g by microstate enumeration. Under those definitions all six reproduce exactly, and are cap-dependent as always. Nor is Λ₉ the tightest admissible object: 2S′ ≤ 2f+1 is admissible and provably containing — min(g, 4f+2−g) ≤ 2f+1 by averaging — and closes at 1,561 cells against 1,654, cutting exactly the 93 cells (f = 0, g = 2, 2S′ = 2), an s² target carrying triplet spin. The price is structural: the constraint graph gains its first cycle, f–g–2S′, so the tree-propagation guarantee lapses and must be retested. The tree or the tightness — the language offers both only up to 1,561 against 1,654.**

*the five adjoined coordinates with their bounds; closure by the ℛ(X) = X sweep of every ambient cell at all six stages; densities and cardinalities at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1), cap-dependent; Λ₉′ the alternative 2S′ ≤ 2f+1 closing at 1,561.*

Computed — M §12.11.1; Racah 1943; Slater 1929; Condon & Shortley 1935; Birkhoff 1940; Freuder 1982.

> **Prior art: seniority as a classification of the states of ℓⁿ is Racah, *Phys. Rev.* 63 (1943); the LS terms of a configuration by microstate enumeration is Slater, *Phys. Rev.* 34 (1929) and Condon & Shortley, *The Theory of Atomic Spectra* (1935); that a sublattice of a product of chains is fixed by its pairwise projections — the basis of the ℛ(X) = X closure test — rests on Birkhoff (1940); that a width-one constraint graph is a forest whose propagation is exact, lost when a cycle enters, is Freuder, *J. ACM* 29 (1982). That these five coordinates carry Λ up six stages with every stage closed and exactly projecting, the density column reproduced only under the three non-obvious exact sets, and the tree-or-tightness alternative located precisely at the 93 cells whose exclusion buys 2S′ ≤ 2f+1 at the cost of the first cycle, is this book's.**

### Three excluded forms

**Two constraint forms were already excluded — sums and differences (§17.2) — and the tower requires a third: symmetric bounds. Every coupling axis's exact ceiling is symmetric under particle-hole conjugation, terms(ℓᵏ) = terms(ℓ^{4ℓ+2−k}), verified exactly for every k on the p and d shells, and a symmetric non-constant function is not monotone, so the admissibility condition (§14.4) cannot carry it: min(g, 4f+2−g) for spin, the conjugation ceiling for seniority, and max2J(ℓ, k) — unimodal, peaking at half filling, 25 at f⁷ and zero at closure — for the core's J. One reflection, three appearances. The envelope gap decomposes into three distinct parts, and at the caps of §7.4 the ninth axis's gap is parity 5, fold 1, both 1 while the eleventh's is ceiling 16, parity 24, triangle 17 — three machines, the reflection (conjugation), the congruence (fermion parity), and the triangle (coupling additivity, one sum and one difference, precisely §17.2's two exclusions wearing physics), and no coupling axis escapes all three. Behind them is one law, three instances deep before the triangle made it four: every coupling coordinate's exact physical bound requires either two parents or a congruence, and the tree carries only one — spin needing min(g, 4f+2−g), seniority the conjugation ceiling, the core's J a non-monotone envelope. Each admissible extension is the monotone envelope of its physics. One half of the triangle survives the four-cap check: the region {|2L−2S| ≤ 2J ≤ 2L+2S} is join-closed — zero failures at caps 6, 8, 10 and 12 — and meet-broken at every one, by 2,862, 12,489, 40,887 and 110,229 failing meets, so certainty survives upward and dies downward, which is the reflection asymmetry (§8.4) stated as an inequality. And the check sharpens the statement: impose the parity congruence as well and the join closure dies too — 1,848 failures at cap 6 — so the surviving half belongs to the parity-free triangle and to nothing larger. Three bodies carry all three excluded forms at once; §36.3 runs the method on that case and finds the maximal forbidden case is the solved one.**

*the three symmetric ceilings under particle-hole conjugation, verified for every k on the p and d shells; the join-closure and meet-failure counts of the surviving half-triangle {|2L−2S| ≤ 2J ≤ 2L+2S} over unordered pairs at box caps 6, 8, 10, 12; the parity-congruence collapse measured at cap 6.*

Proved — M §12.11.2; Pauli 1925; Racah 1942; Wigner 1927; Dilworth 1940.

> **Prior art: the equivalence of a shell's terms under particle-hole conjugation is the complementarity of Pauli (1925) developed by Racah, *Phys. Rev.* 61 (1942); the triangle condition |L−S| ≤ J ≤ L+S on vector coupling is Wigner, *Gruppentheorie* (1927); that a set closed under one lattice operation need not be closed under the other — join without meet — is elementary lattice theory after Dilworth (1940). That these three symmetric forms are exactly what excludes the coupling ceilings from a monotone presentation, that the envelope gap decomposes into reflection, congruence and triangle with no coupling axis escaping all three, and that the surviving half-triangle is join-closed and meet-broken by 2,862, 12,489, 40,887 and 110,229 — dying at the join too once parity is imposed, at 1,848 — is this book's.**

### Law versus extent, and what E measures

**Counting coordinates close exactly; coupling coordinates close as envelopes; there is no third kind in this object. The origins table (§7.1) has four rows — Pauli, the hydrogenic solution and counting give single-coordinate exact bounds, which is why E(Λ) = 0 was available at all, while vector coupling gives envelopes provably and permanently, because its exact form is made of the three excluded shapes (§12.11.2). The sharper statement is about where each axis's bound is taken from, the same distinction between a deduction and a fit that §22 draws for brackets. Reading the thirteen bounds by provenance gives three values, not two: the first ten are taken from a law that exists independently of Λ — the hydrogenic radial solution, Pauli, counting, vector coupling on each end, Racah's seniority — while the eleventh, 2J_c ≤ φ̂(k), is taken from the extent of Λ itself. For φ̂ is not derived but observed: computed at the caps of §7.4 it is {1: 3, 2: 4, 3: 5}, and the largest 2J_c the set actually realises at each occupancy is {1: 3, 2: 4, 3: 5} — the same numbers, because φ̂ is the envelope of the set's own extent. A bound taken from the law closes exactly; a bound taken from the extent closes only to an envelope. That is why exactness is lost at the eleventh axis and not before it. The twelfth is a third kind again, and the one the book chose: the law for K is 2K ≤ 2J_c + 2f with the cell's own f, which has two parents and breaks the tree — the two-body separation (§12.6.1) is a cylinder because every coupling axis hangs off one side, and the tight two-parent K is the first bridge between the ends other than q, breaking the factorisation by 15,150 cells at Λ₁₂ and 45,450 at Λ₁₃, 21.4 % and 22.8 % of the product. The book substitutes f_max, the cap, giving one parent and a surviving factorisation — the law weakened, not abandoned, and 39,375 of Λ₁₂'s 70,905 cells sit at an f below the cap, so for those the bound admits more than the law does. And this says what E(X) measures: ℛ builds its envelopes from X's own projections, so E(X) = |ℛ(X)| − |X| is the price of describing a set by its extent rather than by its law — the count of what the pattern admits and the law does not — and E(X) = 0 says the two coincide, the extent is the law for that set, self-reference stated as arithmetic.**

*the thirteen bounds by provenance — law, extent, law-weakened; φ̂ computed at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1), and shown equal to the realised 2J_c maxima; the two-parent factorisation breakage 15,150 at Λ₁₂ and 45,450 at Λ₁₃; the 39,375 cells below the f cap.*

Proved — M §12.11.3, §12.11.3.1, §12.11.5; Racah 1943; Slater 1929; Moore 1910.

> **Prior art: seniority as the bound weakened at the twelfth axis is Racah, *Phys. Rev.* 63 (1943); the realised maxima that φ̂ envelopes are the term maxima of Slater (1929); that a closure operator's defect measures the gap between a set and the closure its own relations generate is the closure-operator framework of Moore, *Introduction to a Form of General Analysis* (1910). That Λ's provenance column has three values not two — a bound from the law closing exactly, a bound from the extent closing only to an envelope, a bound weakened from two parents to one at a measured cost of 15,150 and 45,450 cells — and that this identifies E(X) as the price of extent over law, zero exactly when the extent is the law, is this book's.**

### An index whose one prediction is false

**The electric-dipole selection rule on (2J, 2J′), |Δ2J| ≤ 2, is a closed index by the mutual-bound lemma (§17.4): a region cut by a symmetric bound between two coordinates closes under join and meet. Remove from it the one transition nature forbids — J = 0 ↛ 0, the cell (0, 0) in doubled units — and closure fails by exactly four meets at every cap tested, and all four failing meets are that same forbidden cell: (0, 1) ∧ (1, 0) = (0, 0) among them, the four running (0, 1), (0, 2) against (1, 0), (2, 0). The defect is E = 1, cap-independent — four meets and one restored cell at box caps 4, 6 and 8 alike — and the single cell ℛ restores is precisely the one the atom vetoes: the photon's unit of angular momentum, with the parity half of the rule a congruence that breaks joins, the photon's odd parity. So here is the calibration the reader is owed (§31.3.4): E(X) counts proposals, not guarantees. This is an index whose single proposal is known false, vetoed by structure the index does not carry — J = 0 → 0 is excluded by the transversality of a real photon, a fact about the electromagnetic field and not about the coordinate region, so the region cannot see it and ℛ dutifully restores the cell the region's own extent implies. The 540 cells of the Kreuzer–Skarke slice are proposals of exactly this kind, and are stated as such. An index is honest about what it proposes; it is not thereby right, and the one place this index makes a checkable physical claim on its own, the claim is false — which is why the falseness is a result and not a failure. The photon reading is interpretation; the E = 1, the four meets and the parity congruence are computed.**

*the region {|Δ2J| ≤ 2} with the cell (0, 0) removed; the four failing meets and the unit closure defect E = 1 verified at box caps 4, 6 and 8, cap-independent; the parity half a join-breaking congruence.*

Proved — M §12.11.6; Wigner 1927; Dirac 1927; Moore 1910.

> **Prior art: that electric-dipole radiation changes J by at most one and forbids J = 0 → 0 is the selection rule of Wigner (1927) and Dirac's quantum theory of radiation, *Proc. R. Soc. A* 114 (1927), the exclusion resting on the photon carrying one unit of angular momentum; that a closure operator restores exactly the elements a set's own relations imply is Moore (1910). That the dipole rule read as a coordinate region is a closed index, that removing its one physically forbidden cell leaves a unit defect restored by ℛ at that very cell, and that this calibrates E(X) as a count of proposals rather than guarantees — an index honest about a claim that is nonetheless false — is this book's.**

### The occupancy clock, and definability is not reachability

**Composition on Λ₉ (§12.11.0) has a direction, and what breaks the symmetry is a coordinate already in the index. Take the source signature (n, ℓ, k, 2S) and target (e, f, g, 2S′) as objects and each cell as a morphism: there are 33 objects, 739 of the 1,089 ordered pairs joined by a step, and not one step raises k. The object graph falls into three strongly connected components, each pure in occupancy — eight objects at k = 3, fifteen at k = 2, ten at k = 1 — with full circulation inside each and no return between, so the quotient is a chain of three, and the stratification survives at four cap settings, not one. The clock is occupancy and the tick is k − g: cycles inside an era cost nothing, and the downward edges, where the clock advances, do not reverse. The eight objects at maximal occupancy have a property the others lack, every morphism into them conservative, forced by k_max = g ≤ q ≤ k ≤ k_max — so time in this index is a counting phenomenon, not a coupling one. And definability is not reachability. A cell is its own down-set, a seventeen-bit word, and in that sense contains its own description; it does not contain a path to every other. Over the 2,735,716 ordered cell pairs of Λ₉, 311,180 are comparable in the lattice order (11.4 %), 675,606 joined by a composition path (24.7 %), and only 9,720 in both (0.4 %): neither order contains the other and they share a four-hundredth of what either carries. The lattice says what a cell is; composition says what it can become, and running them together is the error this census forecloses — a cell can be fully defined and unreachable, and most pairs are exactly that. On the reading that time is nine-dimensional: as a dimension it is false, the composition preorder quotienting to a chain of order dimension one; as a location it is exact, since Λ₈ cannot iterate and Λ₁₀ loses composition, so nine is not the dimension of time but the unique dimension at which time exists.**

*the object graph of Λ₉'s composition, its strongly connected components by Tarjan, and a step counted as rising when target occupancy exceeds source; the pair census over all 2,735,716 = 1,654² ordered cell pairs at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); stratification confirmed under four cap settings.*

Computed — M §12.11.0.1; Tarjan 1972; Birkhoff 1937; Eilenberg & Mac Lane 1945.

> **Prior art: the strongly connected components of a directed graph by depth-first search are Tarjan, *SIAM J. Comput.* 1 (1972); a finite distributive lattice's element as the down-set of the join-irreducibles beneath it is Birkhoff (1937); objects with composable arrows are a category, Eilenberg & Mac Lane (1945). That Λ₉'s composition is a clock ticking in occupancy k − g down a chain of three eras, never rising, and that its lattice order and its composition reachability share only 0.4 % of pairs — a cell fully defined yet unreachable — so that nine is the unique dimension at which time exists rather than the dimension of time, is this book's.**

### The arrow is a property of the assumption

**The clock of §12.11.0.1 is real, and its hypothesis is narrower than it looks: one coordinate carries two readings the constraint set does not distinguish. The bound g ≤ q reads g as electrons placed by this transition; g ≤ 2(2f+1), Pauli, reads it as electrons present in the target subshell. They coincide exactly when the target subshell begins empty, and Λ carries no coordinate for what was already there — so composition's matching condition, that b's source occupancy equal a's target occupancy, silently identifies placed with present, an assumption about destinations rather than a constraint of counting. The repair is to index the sum rather than bound it (§17.4): carry (g, G) with g the number placed and G the total after arrival, under g ≤ G ≤ 2(2f+1), g ≤ q and 2S′ ≤ G, all single-parent monotone bounds, prior occupancy G − g recovered as a derived quantity — 13,775 cells, closed. And the clock does not survive it: of 2,620,090 composable pairs, 826,950 — 31.6 % — raise occupancy. A closed index of transitions has a one-way clock exactly when its destinations begin empty; the arrow is a property of the assumption, not of the object. What survives is more than what fell. The occupancy law as mathematics is untouched — it holds of any index of its stated form, and the extended index simply is not of that form — and a temporal structure survives as a restriction: the maximal sub-index on which a chosen weight never rises, X_w = {a : w(tgt a) ≤ w(src a)}, is closed, and there is one such arrow per coordinate and no others. The four single-coordinate weights each give a closed arrow — shell 9,407 cells, subshell 9,845, occupancy 5,165, spin 7,160, every one E = 0 — while a sum breaks both sides, a maximum breaks meets and a minimum breaks joins, none closing. An index does not have a clock; it has one per coordinate, and occupancy, the one this book built on, is the most restrictive of the four.**

*the two readings of g separated by indexing the sum as (g, G); the extended index and the four weight-arrows verified closed by the ℛ(X) = X sweep at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); the 31.6 % over all 2,620,090 composable pairs.*

Computed — M §12.11.0.2; Pauli 1925; Birkhoff 1940; Freuder 1982.

> **Prior art: that a subshell's occupancy is bounded by 2(2ℓ+1) is Pauli exclusion (1925); that a bound on a sum of coordinates cannot be imposed while the sum can be carried as an indexed coordinate is the sum-indexing move of §17.4, resting on the monotone-bound admissibility of Birkhoff (1940); that each such never-rising restriction is a sublattice, closed, follows from the same width-one property Freuder (1982) gives. That Λ's one-way clock is an artefact of identifying electrons placed with electrons present, dissolved by the (g, G) index into 13,775 cells where 31.6 % of transitions raise occupancy, leaving one closed arrow per coordinate and no others — occupancy the most restrictive — is this book's.**

### The arrows decay with distance

**The four temporal arrows — one per coordinate (§12.11.0.2) — are not independent, and how much any two agree is governed by their distance in the constraint tree. Measured as overlap against independence, P(A_u ∩ A_v) / P(A_u)P(A_v), the six pairs order strictly by tree distance on the source chain n — ℓ — k — 2S with no overlap between distance classes: at distance one, occupancy ∩ spin 1.466, subshell ∩ occupancy 1.222, shell ∩ subshell 1.107; at distance two, subshell ∩ spin 1.080, shell ∩ occupancy 1.070; at distance three, shell ∩ spin 1.025. And a theorem stands behind it, on the separation hypothesis (§12.11.0.4). Let X be an index whose constraint graph is a tree, and A_u, A_v the arrows of coordinates u and v at tree distance d. Then the coordinates form a Markov random field on the tree — the indicator of X is a product of one factor per edge, so conditioning on a separating vertex gives exact conditional independence; hence by the data-processing inequality the mutual information I(u; v) is non-increasing in d; hence by Pinsker's inequality |P(A_u ∩ A_v) − P(A_u)P(A_v)| ≤ √(I(u; v) · ln2 / 2). The overlap of two arrows is bounded by a quantity that decays with their distance in the constraint tree. The mutual informations themselves fall strictly, 0.353, 0.227 and 0.199 bits at distance one, 0.094 and 0.070 at distance two, 0.020 at distance three, as the theorem requires. What the theorem proves is that agreement must fall away with distance; the strict ordering measured here is not implied by it, the Pinsker bound being loose, so the decay is claimed as a theorem and the strictness reported as measurement. And the falsifier fires: the hypothesis is separation, so the test is an index whose graph carries a cycle, and the tower supplies exactly one — the tighter Λ₉′ of 1,561 cells, where 2S′ ≤ 2f+1 couples 2S′ to both f and g and closes the f–g–2S′ triangle. There the Markov property fails, six violations of sixteen where the tree has none, the data-processing step has no chain to run along, and the Pinsker bridge has nothing to bound. Λ₉′ is the third independent result to break at that stage, with the cut law and the two-parent count, which is why the tree or the tightness (§12.11.1) is not a choice between presentations but a single boundary.**

*the four arrow indicators on the (g, G) extended index of §12.11.0.2; overlaps and mutual informations at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); the falsifier the conditional-independence test 2S′ ⊥ f | g over its sixteen cells, six failing on Λ₉′ and none on the tree.*

Proved — M §12.11.0.7; Markov 1906; Pinsker 1964; Cover & Thomas 1991; Lauritzen 1996; Freuder 1982.

> **Prior art: a system of random variables whose dependence factorises along the edges of a graph is a Markov random field, the tree case giving exact conditional independence on a separating vertex — Lauritzen, *Graphical Models* (1996), after Markov (1906); that a function of the data cannot increase mutual information is the data-processing inequality of Cover & Thomas, *Elements of Information Theory* (1991); that total-variation distance is bounded by the root of relative entropy is Pinsker (1964); a width-one constraint graph is a tree — Freuder, *J. ACM* 29 (1982). That Λ's four temporal arrows are exactly such a field on the tree, so their agreement is bounded by a mutual information decaying with tree distance — strictly at 1.466 down to 1.025, and falsified precisely where the constraint graph gains its first cycle — is this book's.**

### Past, present and future

**Reading the constraint tree as past — change — future (§10.2) has an arithmetic, and it is not the arithmetic of three free things. Treated as independent the three parts overcount by 130 %: |A| × |Q| × |B| = 33 × 4 × 17 = 2,244 against |Λ| = 976, a defect of 1,268. Conditioned on the transfer they separate exactly, defect zero — but the balance is not special to the transfer. Every two-sided cut of the tree gives it: ℓ, q, f and g, all defect zero, so the two-body separation (§12.6.1) presents the factorisation as though the transfer did the work when the tree does it, and q is distinguished only by which two things it separates. And the reason it is exactly four is the tree: deleting a coordinate splits the constraint graph into two components precisely when that coordinate is an internal vertex of degree two, and n, e and 2S are leaves while k has degree three, so ℓ, q, f and g are the caterpillar's four internal degree-two vertices and the only two-sided cuts that exist. The future is never a value: of 97 (past, present) pairs none determines a single future — futures per pair run 5, median 10, maximum 17 — and for each value of the present every past gives the same future set. At present 0 there are 33 distinct pasts and one future set of 5; at present 1, 33 pasts and one set of 10; at present 2, 23 pasts and one set of 15; at present 3, 8 pasts and one set of 17. The future is conditionally independent of the past given the present, a Markov property exact at every value: the past constrains only which presents are reachable, and having spent that it has spent everything. The dependence is monotone and opposed, the future set nesting increasing 5 ⊂ 10 ⊂ 15 ⊂ 17 while the past set nests decreasing 33 ⊇ 33 ⊇ 23 ⊇ 8, and the bracket is saturated — at every present the admissible future is the full interval between its own extremes, E(X) = 0 read on the target end. The tick decomposes: over the 1,169 composable cells the clock k − g ticks 0, 1 or 2 across 389, 540 and 240 cells, and k − g = (k − q) + (q − g) has two sources, something not removed and something removed but not placed, 350 against 350 pure with 80 in both, the split table its own transpose — (0,1) = 270 against (1,0) = 270, (0,2) = 80 against (2,0) = 80. Irreversibility has two independent sources contributing identically: one a choice not taken, the other a capacity that could not receive, and the index weights them the same. And Pauli is a minority partner — g's ceiling is fixed by counting in 60.2 % of composable cells, tied in 29.5 % and by shell capacity in only 10.3 % — so the arrow of time in this object is overwhelmingly a counting phenomenon. That the shape is a path and not a triangle is the exactness ⇒ not-a-triangle theorem (§12.11.0.8), proved separately.**

*the three parts A = (n, ℓ, k; 2S), Q = q, B = (e, f, g) of the constraint tree; the two-sided-cut census and the Markov table at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); the tick decomposition over the 1,169 composable cells.*

Proved — M §12.11.0.8; Markov 1906; Lauritzen 1996; Harary & Schwenk 1973.

> **Prior art: that a variable is conditionally independent of the rest given its graph neighbours is the Markov property, the tree case exact — Markov (1906), Lauritzen, *Graphical Models* (1996); that an internal degree-two vertex of a caterpillar is a separator is elementary tree theory, the caterpillar named in Harary & Schwenk (1973). That past, present and future read off Λ's tree are a Markov chain with the future conditionally independent of the past given the present — the future set nesting up 5 to 17 as the past nests down 33 to 8, the tick split into two equal irreversibility sources of 350 each, and Pauli a 10.3 % minority in the arrow — is this book's.**

### Exactness proves the three parts are not a triangle

**The claim is that Λ's exact closure is itself a proof that past, present and future form a path and not a triangle — that there is no direct past–future constraint — and the proof is three steps. First, treewidth one is equivalent to exact closure under ℛ, and treewidth two yields only an envelope. ℛ rebuilds a set from its pairwise projections, so it enforces exactly pairwise consistency; by the theory of consistency and width, a constraint network whose graph has treewidth one — a tree — is made globally consistent by pairwise consistency alone, so ℛ reaches its fixed point with no cells added and E = 0, while a network of treewidth two requires strong 3-consistency, one level above what a pairwise operator supplies, and the shortfall shows as an envelope, E > 0 (§18.4). The distinction is exhibited concretely: the path region {F ≤ Q ≤ P} closes with E = 0, and the coupling triangle {|P − Q| ≤ F ≤ P + Q}, a K₃, closes only to an envelope with E strictly positive. Second, a direct constraint among all three of past, present and future would make their constraint graph a triangle — the complete graph K₃ on three vertices — which has treewidth two. Third, Λ closes exactly: E(Λ) = 0, verified at every one of its cells. By the first step exact closure forces treewidth one; by the second a past–future edge would force treewidth two; the two are incompatible, so there is no past–future edge and the three parts are a path, past ↔ present ↔ future, with the future reaching the past only through the present. The converse frames the result: the one place this book carries a genuine ternary object is the bracket, whose three parts do form a triangle, and there — the three-body case (§36.3, register 316) — ℛ is exactly one consistency level short, which is why its surviving fraction falls as (1 − f)³ and why ℛ was never the right operator for it. Λ is a path because it is exact; the three-body problem is a triangle because it is not. Exactness and shape are the same fact read two ways.**

*the equivalence treewidth 1 ⟺ exact closure under ℛ and treewidth 2 ⟹ envelope, exhibited on the path {F ≤ Q ≤ P} at E = 0 and the triangle {|P − Q| ≤ F ≤ P + Q} at E > 0; E(Λ) = 0 verified over all 976 cells at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); the triangle case tied to the three-body shape.*

Proved — M §12.11.0.8, §18.4; Freuder 1982; Dechter & Pearl 1989; Robertson & Seymour 1986.

> **Prior art: that a constraint network of width one is made globally consistent by arc and path consistency, so a tree closes exactly, is Freuder, *J. ACM* 29 (1982); that achieving global consistency on a graph requires consistency of order one more than its induced width — treewidth two needing strong 3-consistency — is Dechter & Pearl, *Artificial Intelligence* 38 (1989); treewidth itself is Robertson & Seymour, *J. Algorithms* 7 (1986); the complete graph K₃ has treewidth two. That E(Λ) = 0 therefore proves Λ's past–present–future graph is a tree — carrying no past–future edge, a path — while the genuinely ternary bracket is the triangle one consistency level beyond ℛ's reach, is this book's.**

### Two indices, and the one that does not exist

**If composition has a direction, the other direction is a fair question, and it is not a sign change — extending k, q and g below zero leaves the object closed and the clock intact, a negative occupancy being a lower one and not a reversed one. The reversal is a different object: exchange the two ends of Λ₉, (n, ℓ, k, 2S) ↔ (e, f, g, 2S′) with the transfer unchanged, and the reversed index rev(Λ₉) is a lawful closed index of the same 1,654 cells, E = 0, and it is not Λ₉. That is the failure of self-duality (§11.8) read temporally: both are lawful and simply not the same object. Their intersection is where time has no direction. Every one of its 389 cells satisfies g = q = k — total transfer, nothing retained and nothing lost — which is exactly the set of morphisms carrying a reverse; it closes at E = 0, factorises over its own transfer, and is a groupoid, every one of its 33 objects carrying an identity and every morphism a two-sided inverse. The cycles of the occupancy clock (§12.11.0.1) were confined to level sets of occupancy with every step conservative, conservative being g = q and the level-set condition k = g, so the intersection is that condition stated as an object rather than as a property of paths — 23.5 % of Λ₉. And the union does not exist: Λ₉ ∪ rev(Λ₉) has 2,919 cells but 360,000 failing joins and 470,625 failing meets, and closing it would require admitting 2,857 further cells — the amplification of §16.8.4, priced. Three of the four positions exist and the fourth does not: a present is definable from the past and the future, and the thing containing both is not. A structure holding both directions of time is not available at any price this index recognises; what is available is a structure holding their agreement.**

*the reversal exchanging Λ₉'s two ends with the transfer fixed; intersection and union verified by enumeration, E of each by the sublattice closure of ℛ — iterated join and meet to a fixed point, not a single projection — at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.11.0.9; Brandt 1927; Birkhoff 1940; Dedekind 1900.

> **Prior art: a category in which every morphism is invertible is a groupoid — Brandt, *Math. Ann.* 96 (1927); that the join-and-meet closure of a subset of a product of chains is its smallest containing sublattice is Birkhoff (1940); the lattice operations themselves Dedekind (1900). That reversing Λ₉'s two ends gives a second lawful closed index distinct from the first, that their intersection is the g = q = k groupoid where time has no direction, and that their union is not a lattice — costing 2,857 cells to close, so a structure holding both directions of time does not exist at this index's price — is this book's.**

### Every stage of the tower in one table

**The tower is reported in six places under six aspects; gathered in one pass it is seven stages, each with its dimension, cell count, closure defect, ambient box, fill, new coordinate and its bound, and its two gradings. Λ₈: dimension 8, 976 cells, E = 0, box 6,912, fill 14.12 %, exact and does not compose. Λ₉: 9, 1,654, E = 0, box 27,648, fill 5.98 %, adjoining 2S′ ≤ g, exact and the one stage that composes. Λ₉′: 9, 1,561, E = 0, box 27,648, fill 5.65 %, the tighter 2S′ ≤ 2f+1, exact and composing. Λ₁₀: 10, 2,535, E = 0, box 110,592, fill 2.29 %, adjoining v under 2S′ ≤ v ≤ g, exact and does not compose. Λ₁₁: 11, 13,585, E = 0, box 663,552, fill 2.05 %, adjoining 2J_c ≤ φ̂(k), an envelope and does not compose. Λ₁₂: 12, 70,905, E = 0, box 5,308,416, fill 1.34 %, adjoining 2K ≤ 2J_c + 2f_max, envelope. Λ₁₃: 13, 199,130, E = 0, box 47,775,744, fill 0.42 %, adjoining |2J − 2K| ≤ 1, envelope. Every stage closes — E = 0 at all seven, tested against every cell of the ambient box and not by pairs, forty-seven million cells at Λ₁₃ — and closure is the one property the tower never spends. Everything else falls monotonically: fill runs 14.12 % down to 0.42 %, each coordinate multiplying the box faster than it multiplies the object, so the surplus that §11.1.1 measures at seven bits per cell in Λ₈ grows at every step. The tower is not a refinement that sharpens but one that admits more room and fills less of it. And the two gradings part company at different heights: composition is lost at Λ₁₀ and exactness at Λ₁₁, so there is a stage — Λ₁₀ — that is exact and does not compose, and no stage that composes without being exact.**

*the seven stages of the tower gathered in one census; cardinalities, ambient boxes and fills computed at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); closure by the ℛ(X) = X sweep of every ambient cell, the fill each stage's cells over its box.*

Computed — M §12.11.0.10; Birkhoff 1940; Shannon 1948.

> **Prior art: the ℛ(X) = X test that certifies each stage closed rests on the sublattice characterisation of Birkhoff (1940); reading the fill deficit as a surplus in bits is the information measure of Shannon, *Bell Syst. Tech. J.* 27 (1948). That the whole tower Λ₈ through Λ₁₃ closes at E = 0 while its fill falls monotonically from 14.12 % to 0.42 % — the surplus growing at every coordinate — and that its two gradings part at different heights, leaving one stage exact but non-composing and none composing without being exact, is this book's.**

### The fourteenth axis, and the tower's last stage

**The tower stops at thirteen because the physics stopped being supplied, not because the construction failed, and what lies beyond can be settled without being built. Read the surplus first: the bits the ambient box could carry, log₂ of the box, against the bits the object needs, log₂ of the cells, give 12.75 against 9.93 at Λ₈ and 25.51 against 17.60 at Λ₁₃, a surplus rising 2.82, 4.06, 5.45, 5.61, 6.23, 7.91 while fill falls 14.12 % to 0.42 %. A constrained coordinate has mean multiplicity strictly below its own value count — if it did not it would be free and carry no constraint — so each axis multiplies the box by more than it multiplies the object, and fill is monotone decreasing and bounded below by zero, hence converges to a limit L in [0, fill(Λ₁₃)] = [0, 0.416801 %]. From inside the construction that is the whole of what can be said: the admissibility criterion — a new coordinate is admissible when its bounds are lattice morphisms of the stage below, which is what keeps the enlarged index closed — permits continuations of Λ₁₃, all built from the tower's own kinds of axis, reaching L = 0, L = 0.031146 %, and L arbitrarily close to fill(Λ₁₃) from below, so the value is undecidable from admissibility alone and the bracket is only tight and right-open. The reason inside cannot decide it is exact and worth stating: a relabel — a coordinate that is a function of those already present — is admissible, since it closes, and it lowers fill, since it inflates the box while leaving the cell count fixed; a measurement, an independent new label, also lowers fill. Fill falling does not distinguish the two, and closure sees nothing but fill and order, so closure cannot tell a measurement from a relabel — which is why every route to L = 0 is a disguised repetition and why no finite number of built stages fixes the limit. What distinguishes them is the door (§17.1): an axis must be an independent degree of freedom, and a relabel, being dependent, fails it. So a fill-lowering relabel is barred not at closure but at the door — and every genuine axis of the tower is therefore a measurement. That is the step inside lacks and outside supplies, and it decides L. A bound atomic transition under the caps of §7.4 carries finitely many independent labels — two multiplets, one nucleus, one projection each, a finite complete set (Condon & Shortley 1935; Cowan 1981) — so there are finitely many measurements, finitely many axes, and the sum of fill deficits is finite: the tower has no limit to take but a last stage D_last, with L = fill(D_last) > 0. L = 0, admissible from inside, is excluded from outside. The value follows once the remaining rungs are named, and the record names most of them: they are one-parent envelopes (§12.11.5 declined the two-parent tightening; the selection-rule bridge of §12.11.6 is two-parent and so is not a tower axis), the core's J already carries the source shell's J-range through φ̂(k), and the record's world is field-free. The physics after the outer electron's spin bit is the hyperfine coupling F = J ⊗ I (Casimir 1936) then its projection, adjoined in the one-parent envelope style as a window on 2J and on 2J_c under a declared cap on the nuclear spin — a declaration about the world, of the kind Z = 120 is. Over the joint (k, 2J_c, 2J) census of Λ₁₃, 91 classes, every combination of that cap and the open rulings lands L in [0.047 %, 0.333 %], so on the sole premise that the remaining physics is among these named rungs the bracket of the fourteenth axis tightens from [0, 0.416801 %) to a fifth of its width, off zero by two orders of magnitude at the bottom. The record-consistent reading — the largest primordial ground-state spin, I = 7, the core's J read as the source J, field-free — gives L = 0.283507 % at a last stage of fifteen, and L = 0.302400 % if the primordial isomer's I = 9 is admitted; the two differ only in value, not in the ladder. And a null sits nowhere on this bracket: the empty index satisfies every criterion in this book — ℛ(∅) = ∅ so E(∅) = 0, Q(∅) = ∅ so it is complete, zero join-irreducibles, zero bits — so E(X) = 0 is necessary for completeness and not sufficient for content, and what distinguishes Λ from nothing at all is not closure but its seventeen join-irreducibles and its bits of surplus. The existence of the limit is the law's; its value is the world's; and the world, asked the one question answerable without a further ruling — is the ladder finite — has answered yes.**

*the bits and fills at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); the inside undecidability by three admissible continuations of Λ₁₃ reaching 0, 0.031146 % and the supremum, all closed at E = 0; the last-stage result on the premise that a bound transition carries finitely many independent labels, the fill-lowering relabel barred at the door and not at closure; the value over the joint (k, 2J_c, 2J) census, 91 classes, with the hyperfine rungs of §12.11.5's one-parent style and the nuclear-spin cap declared; the empty index by definition and |J(Λ)| = 17 measured.*

Proved — M §12.11.0.11, §17.1, §18.4.1; Weierstrass 1860s; Birkhoff 1937; Baker & Pixley 1975; Condon & Shortley 1935; Casimir 1936; Shannon 1948.

> **Prior art: that a monotone bounded sequence converges is the monotone convergence theorem, Weierstrass's foundational analysis, and an infinite product of factors below one vanishes exactly when the sum of their deficits diverges is the standard product criterion; that a bound preserving meets and joins keeps the enlarged relation a sublattice — the admissibility criterion — is Birkhoff (1940), its closure test resting on Baker & Pixley (1975); that a bound atomic transition carries a finite complete set of labels is Condon & Shortley, *The Theory of Atomic Spectra* (1935) and Cowan (1981), the hyperfine coupling F = J ⊗ I being Casimir (1936); a finite distributive lattice is fixed by its join-irreducibles, of which the empty lattice has none, Birkhoff (1937); bits as logarithms of counts, Shannon (1948). That the tower's fill is undecidable from the construction's admissibility criterion yet has a last stage once the door bars the fill-lowering relabel and the physics bounds the labels — so the limit exists by law and equals fill(D_last) > 0, tightening to [0.047 %, 0.333 %] and to a record-consistent 0.283507 % — is this book's.**

### How Λ enters a larger index

**Beyond the direction of the fourteenth axis is the other question: what happens to Λ when it becomes a coordinate of something bigger. All three answers are computed, and none needs the larger index built. It enters as a chain, and it enters small. A coordinate must be totally ordered and Λ₁₃ is a lattice, so the only chain-valued function ℛ accepts on it is its rank: 199,130 cells become 44 rank values, 17.60 bits collapsing to 5.46, a compression of 4,526 to 1 with 12.14 bits per cell lost. Thirty-one per cent of the object survives the promotion and the rest is not representable as a coordinate at all — structurally the same kind of thing as the first dimension of Λ, which is a chain of three, so an index can be an axis of another at that price. A coarse coordinate is a branching node: at Λ₉ the rank chain has 21 values and the fibres beneath them run from 1 cell to 185, so one point above stands for as many as a hundred and eighty-five below and nothing in the coordinate distinguishes them. And composition, seen from above, stops being a map and becomes a bracket. Λ₉ composes — 41,682 pairs, closed and associative — but reduced to rank there are 264 distinct pairs of input ranks, and only 17 % of them determine a single output rank; the worst spread is twelve possible output ranks from one input pair, the composite's rank lying in [3, 23], narrowed by the inputs and not fixed by them. From one coordinate up, a transition is not a function of its inputs but an interval. That is the bracket of §22.1 arriving unbidden one dimension higher, and it is the clearest statement in this book of what coarsening costs: not error but resolution — the deduction stays valid and stops being sharp. What this does not show is any escape from the index. The branching is inside it: those 185 cells are cells of Λ₉, states of the same object, and what the collapse loses is resolution, not access to anything else. Ignorance about this index is not evidence of another, and every branch terminates in a cell of Λ₉.**

*Λ's rank as its only admissible chain-valued coordinate, 199,130 cells to 44 values; the Λ₉ fibres and the rank-reduced composition — 264 input-rank pairs, the share fixing a single output and the worst interval — measured at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1), the composite rank on the raw coordinate scale.*

Computed — M §12.11.0.12; Dilworth 1950; Birkhoff 1937; Shannon 1948.

> **Prior art: that the longest-chain height gives a lattice its rank is Birkhoff (1937), and that a lattice's width and its chain decomposition are dual is Dilworth (1950); the collapse of a distribution to a coarser one measured in bits is Shannon (1948). That Λ₁₃ enters a larger index only as its rank — 44 values, 4,526 cells to one, thirty-one per cent surviving — so that its composition seen from one coordinate up is not a map but an interval of up to twelve output ranks, the bracket of coarsening arriving one dimension higher with every branch still terminating in a cell of Λ, is this book's.**

### Which selection rules a closed index will accept

**A cell of Λ is an electromagnetic transition, and the rules that decide whether a photon connects two configurations — multipole, parity, the change in spin — are not coordinates of Λ but functions of the coordinates it already carries. The index therefore imposes no electromagnetic constraint of its own; the question is only which of those rules it will hold once they are handed to it. A selection rule presented as a set of admissible cells may be imposed on Λ₉ with closure surviving exactly when that set is convex in the range of the quantity defining it, which is §17.3's criterion arriving where it can be measured. The spin rule ΔS = 0 is the diagonal of a difference, σ⁻¹({0}), and a diagonal is two monotone one-parent bounds at once; it is convex in range, and imposing it keeps 526 of Λ₉'s 1,654 cells at defect zero, holding not at one cap but at four settings of §7.4 — 1,654, 2,664, 44,153 and 60,164 cells, E = 0 at each. The parity rule |Δℓ| = 1 is δ⁻¹({−1, +1}), and here the set has a hole: it admits Δℓ = −1 and Δℓ = +1 and refuses the Δℓ = 0 between them, so it is not convex in range, and imposing it keeps 840 cells at a defect of 750 — the closure of the punctured set fills the hole straight back in. The two rules divide on exactly the property the criterion names, and the criterion says which in advance rather than after the count. The parity rule is a further instance of the congruence form of Three excluded forms (§12.11.2) — a bound with a fixed parity between admissible values — and it is the first for which the criterion also names the repair that would work: any reparametrisation that moves the hole to an endpoint of the range makes the set convex and closes it, at the cost of no longer being the parity rule. So one of the two electromagnetic rules can be carried by the index at E = 0 and the other cannot, and the line between them is not physical but order-theoretic: a rule is admissible when its image is an interval, and refused when its image is an interval with a point removed.**

*the spin rule σ⁻¹({0}) imposed on Λ₉, 526 cells at E = 0 and stable across the four caps 1,654 / 2,664 / 44,153 / 60,164 (the four-cap sizes carried from the record); the parity rule δ⁻¹({−1, +1}) imposed on Λ₉, 840 cells at E = 750, both E by the sublattice closure of ℛ — iterated join and meet to a fixed point, not a single projection — at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); convexity-in-range read on Δℓ = f − ℓ and ΔS = 2S′ − 2S.*

Proved — M §12.11.8, §17.3; Russell & Saunders 1925; Laporte 1924; Wigner 1927; register 1792.

> **Prior art: that the electric-dipole spin rule is ΔS = 0 in LS coupling is Russell & Saunders, Astrophys. J. 61 (1925) 38, and that the parity rule is |Δℓ| = 1 is Laporte, Z. Phys. 23 (1924) 135, its group-theoretic ground Wigner, Z. Phys. 43 (1927) 624; that the closed subsets of a closure operator are those fixed by it, so that admissibility is an interval condition on the defining quantity, is the standard order theory. That whether a selection rule can be imposed on Λ₉ with E = 0 is decided by whether its set is convex in the range of its defining quantity — the spin diagonal convex and holding at four caps, the parity rule punctured at zero and closing to E = 750, the repair being to move the hole to an endpoint — is this book's.**
### The electromagnetic index is a quotient, not an extension

**Every electromagnetic quantity a transition carries — the change in orbital ℓ, the change in spin, the multipole that follows from them — is a function of coordinates Λ already holds, and that single fact settles what adjoining them can and cannot do. Adjoin the electromagnetic coordinates to Λ₉ as new axes and the closed index of defect zero becomes an index of defect 3,900: the ambient box grows by the value count of each new coordinate while the cell count does not move, because a derived coordinate adds no cell that was not already determined, so it adds no join-irreducible and cannot enlarge the closed family — it can only enlarge the space that family is measured against. This is Theorem 17.1 in the direction that matters, that a coordinate which is a function of the others cannot improve closure and here strictly worsens it, and it names the electromagnetic content of Λ correctly: not an extension that adds structure but a quotient that reads structure already present. The image says the same from the other side — Λ's map onto (multipole, change in spin) is the complete rectangle at every cap, E = 0 for the empty reason that a full box always closes — so the electromagnetic law is nowhere added and everywhere derived. And the derived predicate is not the composition predicate the book has been calling a transition. The transit condition that decides whether one cell is a legal source for another and the electromagnetic condition that decides whether a photon connects them are near-independent on the same cells, sharing 0.0004 of a possible 0.633 bits: one is about state succession and the other about radiation, and the index carries both without their being the same question. A selection rule is a quotient by a symmetry, and Λ was already carrying its quotient before the electromagnetic coordinates were named.**

*E = 3,900 for the adjunction of the electromagnetic coordinates to Λ₉, and the 0.0004-of-0.633-bit near-independence of the electromagnetic and composition predicates; the complete-rectangle image E = 0 measured on Λ₉ at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §12.11.8, §17.1; Noether 1918; Wigner 1927; Shannon 1948.

> **Prior art: that a selection rule is a quotient by a symmetry rather than an extension of the state space is the symmetry–conservation correspondence, Noether, Nachr. Ges. Wiss. Göttingen (1918) 235; that a derived coordinate adds no join-irreducible and so cannot enlarge a closed distributive family follows from Birkhoff's representation, and the shared information between two binary predicates in bits is Shannon (1948). That adjoining Λ's electromagnetic coordinates gives E = 3,900 while its image on (multipole, ΔS) is the complete rectangle at E = 0 — so the electromagnetic law is a quotient of Λ and not an extension of it, and is near-independent of the composition predicate at 0.0004 of 0.633 bits — is this book's.**

### Four coupling schemes price four routes to one object

**A coupling scheme is a basis change, and the atom does not move under it, so the four standard schemes for a two-electron configuration must agree on the physics and may disagree only on the bookkeeping — and measured against Λ₁₃ they do exactly that. The tower as built uses jK, and its cell count is 199,130; rebuilding LK from its recoupling chain reproduces its stated figure from the chain alone at 341,150. LS and jj depend on a looseness convention that the physics names but does not fix a value for, and two committed readings of it bracket rather than determine their counts: LS falls in [383,065, 597,325] and contains 431,050, jj in [160,380, 244,060] and contains 206,520. The four counts span a factor of 2.17, and that spread is the whole point: it prices four routes to one object, not four objects. Where the counts differ the exact J multiset does not, and this is the proof: a coupling scheme is a unitary change of basis on the same space, so the multiset of total J it yields is invariant under recoupling — the same whether J is reached through K or directly. The fifteen configurations computed through the jK, LS and jj chains independently are the witness, identical in every one, and §12.11.4 states the same at the channel level, 12 of 12 (J_c, f) pairs, while the envelopes differ, 64.4 per cent through K against 39.4 direct. The envelope does not commute with recoupling though the multiset does; the index remembers the route and the atom does not. One route is then privileged, and here for a structural reason rather than a proved one: because the outer electron's spin is a half, the final triangle degenerates to the mutual bound |2J − 2K| ≤ 1, which is admissible on both sides and closes, losing only the parity point 2J = 2K — the smallest quantum of angular momentum being the largest the constraint language can hold exactly, and the scheme that reaches it is jK, which the atoms of the later chapters realise at high n because the weak coupling goes last. [The jK privilege is interpretation; the multiset invariance and the four counts are proved and measured.]**

*jK = 199,130 as |Λ₁₃| measured on the rebuilt tower at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1); LK = 341,150, the LS bracket [383,065, 597,325] ∋ 431,050 and the jj bracket [160,380, 244,060] ∋ 206,520, and the 15-of-15 identity of the J multiset across schemes, from the record; the 2.17-fold spread and the 64.4-against-39.4 envelope contrast as §12.11.4.*

Proved — M §12.11.8, §12.11.4; Racah 1942; Cowan & Andrew 1965.

> **Prior art: that jK, LK, LS and jj are the four types of pure coupling for a two-electron configuration is Cowan & Andrew, J. Opt. Soc. Am. 55 (1965) 502 — a precedent for the set and not only for its members — and the recoupling algebra by which a scheme is a change of basis is Racah, Phys. Rev. 62 (1942) 438. That the four schemes reproduce or bracket the Λ₁₃ counts — jK 199,130, LK 341,150, LS ∋ 431,050, jj ∋ 206,520, a 2.17-fold spread — while the exact J multiset is identical across all four in fifteen of fifteen configurations, so that the cell-count spread prices four routes to one object and jK is privileged by the outer electron's half-spin degenerating the final triangle to |2J − 2K| ≤ 1, is this book's.**

### Adjunction never repairs a closed index

**A non-closed index cannot be mended by adding a coordinate that is a function of the ones it already has, and the proof is one line. Adjoin to a set S a coordinate h computed from each cell, forming the graph S′ = {(x, h(x))}; then the join of (x, h(x)) and (y, h(y)) is (x ∨ y, h(x) ∨ h(y)), and if S′ is closed that pair lies in S′, so x ∨ y lies in S — and meets likewise. So S′ closed forces S closed: the graph of a derived coordinate can be closed only if its base already was. The contrapositive is the working statement — a set that is not closed stays not closed under the adjunction of any function of its coordinates — and it fixes what adjunction can be for. The companion criterion says which coordinates close at all: Λ × h is closed exactly when h is a lattice homomorphism, and that was measured across four hundred and twenty-four tests at a hundred per cent — projections, minima and constants qualify, sums, products and differences do not. A difference fails for the reason the join exposes: over x ∨ y the two terms take their maxima independently, so e(x∨y) − ℓ(x∨y) need not equal the larger of the two differences, and the graph breaks. This is why the electromagnetic coordinates cannot improve Λ: every one of them is a function of coordinates Λ already carries, and adjoining them gives not repair but E = 3,900, the worked instance of the theorem in the direction that a derived coordinate strictly worsens closure rather than improving it. Only three routes to repair remain, and the theorem is what leaves exactly three: enlarge the index by adding cells, restrict it by removing them, or reorder it and change neither — adjoining a derived axis is none of these, and is ruled out at the source.**

*the theorem proved by the join/meet identity on the graph {(x, h(x))}; the homomorphism criterion Λ × h closed ⟺ h a lattice homomorphism measured at 100 % over 424 tests, projections/minima/constants qualifying and sums/products/differences not, confirmed on the rebuilt Λ₈ for the projection, minimum, constant and difference cases; the E = 3,900 electromagnetic adjunction as the worked instance, at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §17.2; Birkhoff 1940.

> **Prior art: that a sublattice of a product of lattices is exactly a subset closed under the componentwise meet and join, so that the graph of a function is a sublattice only when the function preserves both — a lattice homomorphism — is Birkhoff, Lattice Theory (1940). That a non-closed index therefore cannot be repaired by adjoining any function of its own coordinates, leaving only enlarge, restrict and reorder as repairs, and that the electromagnetic coordinates are the worked instance at E = 3,900, is this book's.**


### The membership function

**χ(x) = H(n−1−ℓ)H(4ℓ+2−k)H(k−q)H(k−2S)H(e−1−f)H(4f+2−g)H(q−g); the coefficient function of F is χ**

*H the Heaviside step*

Computed — M §11.1; Heaviside 1893.

> **Prior art: the membership function as a product of step functions — Heaviside, Electromagnetic Theory (1893), where the unit step is introduced.**

### The implication circuit

**The 20 covering relations of J(Λ), read as implications between bit positions, cut 2¹⁷ = 131,072 words to exactly 976 — the cut is exact and nothing else is imposed, proved by exhaustion. Order the seventeen generators; bit i of a word says generator i lies beneath the cell. If generator j covers generator i then bit j set forces bit i set, and a word satisfies all twenty such implications if and only if its set of bits is a down-set of J(Λ), which by the Birkhoff representation (§8.3) is a cell. Verified by enumerating the whole ambient space: of the 131,072 seventeen-bit words exactly 976 satisfy the twenty implications, and the accepted set is equal as a set to the image of Λ under cell ↦ word, not merely equal in count. The circuit is monotone — AND, OR and implication only, no NOT, no feedback — so it decides membership and computes no function of successive inputs. Its depth depends on which circuit is meant, and all three readings are recorded: with unbounded fan-in, one level of implications under one AND, depth 2; with two-input gates, the twenty implications evaluate in parallel and a balanced AND tree over them adds ⌈log₂20⌉ = 5, giving 5 above the implication level and 6 in total; the forcing circuit that closes a set of bits downward instead of testing it has depth equal to the longest chain in J(Λ), 5 generators and so 4 covering steps. The book's stated depth of five is the AND-tree reading. Fan-in and fan-out are bounded: no bit is forced by more than 3 others and no bit forces more than 3**

*monotone: AND, OR, implication; no NOT, no feedback; the 17 generators as input lines and the 20 covers as gates; depth stated for the two-input accept circuit, with the unbounded-fan-in and forcing readings recorded beside it*

Proved — M §11.1.1; Birkhoff 1937; Shannon 1938.

> **Prior art: implications as a monotone Boolean circuit — Shannon, A symbolic analysis of relay and switching circuits, Trans. AIEE 57 (1938) 713-723. That the words satisfying the cover-implications are exactly the down-sets is Birkhoff (1937); the exhaustion over 2¹⁷ and the three depth readings are this book's.**

### Sublattice of a product

**Λ is closed under coordinatewise ∨ and ∧ — worked case by case: for z = x∨y and any constraint xᵢ ≤ φ(xⱼ) with φ non-decreasing, the slot zᵢ comes from x or from y; from x, zᵢ = xᵢ ≤ φ(xⱼ) ≤ φ(max(xⱼ,yⱼ)) = φ(zⱼ), the bound riding monotonicity upward; from y symmetrically; for z = x∧y the binding slot is on the j side — with zⱼ = xⱼ, zᵢ ≤ xᵢ ≤ φ(xⱼ) = φ(zⱼ), the bound riding selection downward; the seven edges instantiate φ as ℓ ≤ n−1, k ≤ 4ℓ+2, q ≤ k, f ≤ e−1, g ≤ 4f+2, g ≤ q, 2S ≤ k, and the floors n, e, k ≥ 1 are constants, preserved by max and min alike; verified over all 475,800 unordered pairs at the stated caps, zero failures on either operation**

*every constraint of the form x_i ≤ φ(x_j) with φ non-decreasing; both branches of both operations written out, neither appealing to the other*

Proved — M §7.3; Birkhoff 1940.

> **Prior art: closure under coordinatewise join and meet is the definition of a sublattice of a product (Birkhoff, Lattice Theory, 1940). What makes Λ one is that all eight constraints have the form x_i ≤ f(x_j) with f monotone.**

### The language combinations

**The six languages of §11.1 — order, algebra, analysis, geometry, information, logic — combine pairwise, and P21 demands that a combination name one shared object of Λ rather than an analogy between two descriptions; ten pairs were put to that test and ten hold, each verified at the caps of §7.4. Order and algebra: coordinatewise meet and join are gcd and lcm under N(x) = ∏ pᵢ^{xᵢ}, with zero failures on either operation over all 475,800 unordered pairs — the sublattice closure (§7.3) with the divisor-lattice embedding (§9). Order and analysis: F′(1)/F(1) is the mean rank, 11.0666 — the rank polynomial (§11.1). Order and geometry: the bounding box minus the lattice is the void, 6,912 − 976 = 5,936 (§10). Geometry and analysis: F is not palindromic if and only if the poset is not self-dual, and one witness settles both — the rank sizes are not symmetric, 5 cells at rank 4 against 4 at rank 19 and the peak 122 at rank 11 against 121 at rank 10, so F is no palindrome and Λ admits no rank-reversing automorphism (§11.8). Order and information: ℛ(Λ) = Λ, so the closure defect is zero and no bit is wasted against the polytope. Algebra and information: the whole index is seven rows of two non-zero entries, the matrix A and nothing more, from which all 976 cells regenerate — the membership function (§11.1). Logic and algebra: that same membership function χ, a product of seven Heaviside steps, selects exactly 976 of the box's 6,912 points. Logic and analysis — the eighth, and the one that makes "single expression" literal: the coefficient function of F is χ, the coefficient of z₁^{n}···z₈^{2S} being 1 when the cell exists and 0 when it does not, so F and χ are one function written twice; F(1) = 976 and F(−1) = 2. Analysis and information: log₂ F(1) = log₂ 976 = 9.93 bits to name one cell — the Boolean representation (§11.1.1). Algebra and geometry: the integer points of the polytope A x ≤ b are the lattice exactly, no point of the box satisfying the bounds falling outside Λ. Ten combinations, ten shared objects — each a quantity one language produces and another confirms on the same 976 cells**

*the six languages of §11.1; a combination is an unordered pair, of which C(6,2) = 15 exist; ten were put to P21 and all ten name a shared object, listed here with the quantity each pair agrees on; every count at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Computed — M §11.2; Birkhoff 1937; Stanley 1986; Heaviside 1893; Shannon 1938.

> **Prior art: each single-language fact is standard — the divisor-lattice meet and join are Birkhoff (1937); the rank generating function and the palindromic ⟺ self-dual equivalence are Stanley, *Enumerative Combinatorics I* (1986); the step-function product is Heaviside, *Electromagnetic Theory* (1893); the bit count is Shannon (1938). That the six languages' pairwise combinations each name one shared object of Λ — ten put to the admission test and ten holding on the same 976 cells — is this book's.**
### The languages are one statement, and E is what translation costs

**Five results in this book have one shape and were never set beside one another until the languages were gathered, and put in a row they stop being separate facts and become a single one. Each is one object under two namings, and the defect changes between them: the 118 elements are E = 36 as period against group and E = 0 as Janet's n + ℓ against position; Λ₉'s parity rule is E = 750 as the congruence |Δℓ| = 1 and E = 0 as the convex band |Δℓ| ≤ 1; the same J multiset is jK 199,130, LK 341,150, LS 431,050 and jj 206,520, four routes to one atom; slack is E in order, the void in geometry and V in calculus, one quantity three ways; and Λ at 976 is where six languages agree and ten of their combinations hold. What they share is that a language is a coordinate system, a translation between two is a re-coordinatisation of one object, and E is what that translation costs — zero when a closed naming exists and positive by exactly the number of cells the drawing misplaces when it does not. This is the law of realised closure read in the vocabulary of language: a thing is sayable without loss exactly when a translation into a closed language exists, and the certificate is that translation, which is why it must be exhibited rather than searched for. Every number here is proved elsewhere in the book and none is new; what is new is that they are one statement, and the mechanism that makes these languages speak to one another is ℛ — its fixed points are the sayable-without-loss and its defect is the price of saying a thing otherwise. It is the justification of the subtitle: the transitions speak the languages, and E is the cost of translation between them.**

*the namings each proved where they arise — the periodic table and Janet at E = 36 / 0 (§6.2), the parity rule at E = 750 / 0 (§12.11.8, verified here), the four-scheme J multiset with jK = 199,130 (verified here as |Λ₁₃|), slack as the one quantity of order, geometry and calculus, and Λ at 976 agreed by six languages (|Λ₈| = 976, verified here) and ten combinations (§11.2); the collapse to one statement is §21.1, at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §21.1, §18.4.1; Birkhoff 1940.

> **Prior art: that a change of coordinates on one object is a translation and that the objects agreeing across coordinate systems is the content of a representation theorem is Birkhoff's programme (1940); each of the numbers is proved at its own place in this book with its own prior art. That they are one statement — a language is a coordinate system, translation is re-coordinatisation, and E, the closure defect of ℛ, is what the translation costs, zero exactly when a closed naming exists — so that ℛ is the mechanism by which the book's languages speak to one another, is this book's, and is the justification of its subtitle.**


### The definition of Λ

**Λ = { (n,ℓ,k,q,e,f,g,2S) ∈ ℤ⁸ : node counting ℓ ≤ n − 1, Pauli k ≤ 4ℓ + 2, the transfer bound q ≤ k, node counting f ≤ e − 1, Pauli g ≤ 4f + 2, the second transfer bound g ≤ q, vector coupling 2S ≤ k, the occupancy floor k ≥ 1 (§7.1, §10.2) }, caps (n,e,ℓ,k,f) = (3,3,1,3,1)**

*caps stated; figures at other caps must say so (§7.4)*

Definitional — M §7; Bohr 1913; Pauli 1925.

> **Prior art: the eight constraints are the shell-structure rules of Bohr (1913) and Pauli (1925), written as inequalities on integer coordinates.**

### Order dimension (Dushnik–Miller)

**order dimension of Λ₈ is 7 = width of J(Λ), certified both ways: J(Λ) partitions into seven chains, and seven generators are pairwise incomparable — one per coordinate except g, whose every generator sits above the q-atom (1,0,1,1,1,0,0,0) because g ≤ q, so g contributes no independent antichain member and the order pays seven dimensions for eight axes; the earlier figure 8 was asserted, never derived (register 409), and is corrected; Λ₉ also measures width 7, so the dimension does not rise by one per adjoined axis**

*Dilworth: the dimension of a finite distributive lattice is the width of its join-irreducible poset; lower certificate the antichain (1,0,1,0,1,0,0,1), (1,0,1,0,2,1,0,0), (1,0,1,0,3,0,0,0), (1,0,1,1,1,0,0,0), (1,0,2,0,1,0,0,0), (2,1,1,0,1,0,0,0), (3,0,1,0,1,0,0,0); upper certificate the seven-chain partition; at the stated caps*

Proved — M §8.6; Dushnik & Miller 1941; Dilworth 1950.

> **Prior art: Dushnik & Miller, Partially ordered sets, Amer. J. Math. 63 (1941) 600-610; Dilworth, Ann. Math. 51 (1950) 161-166 for dimension = width of the join-irreducibles. A product of n chains has dimension at most n; equality fails for Λ because the coupling g ≤ q welds g's generators above q's — kin to the production rule (register 1143): a monotone bound, like a monotone production, adds no independent join-irreducibles.**

### Birkhoff / product of chains

**Λ is distributive, and exactly: x∧(y∨z) = (x∧y)∨(x∧z) holds coordinatewise in ℤ — min(a, max(b,c)) = max(min(a,b), min(a,c)) is an identity of integers, checked by the three orderings of a, b, c — and sublattice of a product (§7.3) makes Λ's ∨ and ∧ the ambient coordinatewise operations, so the identity restricts to Λ with nothing left at the boundary; the forcing is the embedding, not a census**

*4,000 sampled triples at the stated caps return zero failures — a check on the instrument, the theorem needing none*

Proved — M §8.1; Birkhoff 1937.

> **Prior art: a lattice is distributive iff it embeds in a product of chains (Birkhoff, Rings of sets, Duke Math. J. 3, 1937). Λ is such a sublattice by construction; the expansion writes the inheritance out.**

### Why a closed expression exists

**A closed product form for |box ∩ Λ| exists exactly when the constraint graph is a tree of monotone binary bounds, and that condition decomposes into three facts, each separately necessary — proved. Every constraint being a monotone bound of the form xᵢ ≤ φ(xⱼ) makes the admissible region a polytope and keeps it closed under join and meet — the sublattice closure (§7.3); every bound coupling exactly two variables makes the constraint graph a tree — the constraint tree (§8.5, §11.4); the tree having no cycles lets the counting sum factorise, one coordinate eliminated at a time with no term ever subtracted — the box factorisation (§10.4). Remove any one and no closed expression survives. Drop monotone and impose a sum bound — conservation g₁ + g₂ ≤ q, a ceiling on a sum rather than on a single coordinate — and join-closure is lost: the book records 89,864 join failures in 979,300 sampled composition pairs with meets unaffected, and the counterexample is two lines, a = (g₁=1, g₂=0, q=1) and b = (g₁=0, g₂=1, q=1), each conserving while their join (g₁=1, g₂=1, q=1) transfers two units having removed one — the failure is join-only and meet-preserved on every cap tested, because a maximum can breach a sum ceiling and a minimum cannot. Drop two-variable and impose a three-variable constraint and the graph is no longer a tree — the triangle form on K₃ (§36), {|a−b| ≤ c ≤ a+b}, is join-closed but meet-broken and so not a sublattice, and Λ carries no such triple, zero of its thirty-five closing on three variables — the three-coordinate rule (Register 1175), the signature of a tree. Drop acyclic and close a cycle and the Rota sieve returns — closing the triangle k—q—2S raises the elimination width to two and forces an eight-term inclusion–exclusion, the tree-style count wrong by 40 cells on the box factorisation's witness box. The three together are why Λ closes in one pass where full arithmetic never closes, and place it at the last graph structure on which the pairwise operator ℛ is complete — the Helly number (Appendix G, Theorem 4.4)**

*the closed form of the box factorisation; three necessary conditions — monotone bounds, two-variable couplings, acyclicity — each exhibited with its own counterexample; the sum-bound figure sampled over composition pairs, the cycle witness exact at the caps of §7.4.*

Proved — M §11.7; Freuder 1982; Rota 1964; Lauritzen 1996.

> **Prior art: a count factorises over a constraint graph exactly when the graph has width one, that is, is a tree — Freuder, J. ACM 29 (1982); the coordinate elimination is Lauritzen, *Graphical Models* (1996); the sieve a cycle forces is Rota (1964). That these three conditions on Λ are each necessary, each with an exhibited counterexample — the conservation sum bound for monotonicity, the triangle form for two-variableness, the closed k—q—2S triangle for acyclicity — is this book's.**

### The lattice metric

**log d is an ℓ¹ metric and d satisfies the multiplicative triangle inequality d(x,z) ≤ d(x,y)·d(y,z) — both proved coordinatewise. Taking logs, log d(x,y) = Σ_i log(|x_i−y_i|+1) by the interval measure (§9.2), a sum of per-axis terms each of the form log(|Δ_i|+1); since |·| is a metric on ℤ, each term obeys the ordinary triangle inequality and their sum is an ℓ¹ metric, so log d is a metric and d is its exponential. The multiplicative form is the same fact before taking logs: it suffices that (|a−c|+1) ≤ (|a−b|+1)(|b−c|+1) for integers a,b,c, which holds because with s = |a−b|, t = |b−c| the right side is st+s+t+1 ≥ s+t+1 ≥ |a−c|+1, the last step the integer triangle inequality; taking the product over the eight coordinates gives d(x,z) ≤ d(x,y)·d(y,z). Equality holds on an axis iff st = 0, i.e. y lies between x and z there, so global equality iff y ∈ [x∧z, x∨z] — y on a geodesic; 4,000 of 4,000 sampled triples satisfy the inequality. d is symmetric and d ≥ 1 with equality iff x = y. The balls are hyperbolic: on a two-axis slice the level set d = D is the lattice hyperbola (1+|Δ_1|)(1+|Δ_2|) = D, and each axis is a log-distorted chain whose first step is log 2 and tenth step log(11/10), the distortion log((m+1)/m) shrinking with m**

*as the interval measure; the metric structure is the coordinatewise integer metric carried through log, not a separate construction — the sampling checks the instrument, the coordinate reduction is the proof*

Proved — M §9.2; Monjardet 1981.

> **Prior art: Monjardet, Metrics on partially ordered sets - a survey, Discrete Math. 35 (1981) 173-184.**

### Möbius function of a distributive lattice

**μ(x,y) = (−1)^{|y∖x|} if y∖x is an antichain in J(Λ), else 0 — the closed form, read off the 17-element poset J(Λ) with no recursion. Since Λ ≅ J(P) (the Birkhoff representation (§8.3)) with |P| = 17, the interval [x,y] in Λ corresponds to the interval [D_x, D_y] of down-sets, and by Rota's theorem for a distributive lattice the Möbius value is (−1)^{|y∖x|} when the generators added, y∖x, form an antichain in P and 0 when they do not; values lie in {−1,0,+1}, confirmed against the recursive definition on 47 comparable pairs. A transfer condition ties this to the arithmetic Möbius μ_arith of the divisor lattice embedding (§9): μ_Λ(x,y) = μ_arith(N(x),N(y)) if and only if the interval [x,y] is a void-free unit hypercube — every |x_i − y_i| ≤ 1 (so the ratio N(y)/N(x) is squarefree and μ_arith = (−1)^{Σ(y_i−x_i)} ≠ 0) AND the whole coordinate box ∏_i[x_i,y_i] lies inside Λ. The reason: on a void-free unit hypercube the Λ-interval is the full Boolean cube on the differing coordinates, whose order Möbius is the product (−1)^{Σ Δ_i}, matching μ_arith; a void — a box cell excluded by Λ's constraints — prunes the cube, and the Möbius of the pruned interval no longer equals the product. So among unit hypercubes, void-free ⟺ agreement and void-bearing ⟺ disagreement, with no mixed case: verified exact, void-free pairs all agreeing and void-bearing pairs all disagreeing (the book's tested split 60 agree / 56 disagree). The condition is decidable in seven comparisons — no cell of Λ admits an independent +1 step in more than seven coordinates at once (the maximum local up-degree is 7, attained at six cells; the couplings pin at least one coordinate from every cell), so a unit-hypercube interval spans at most seven coordinates and only those spans need testing**

*Λ ≅ J(P); the antichain closed form is Rota's, applied; the transfer biconditional is the new content — μ_arith is nonzero only on unit hypercubes, and there it agrees with μ_Λ exactly when Λ removes nothing from the box*

Proved — M §9.3; Rota 1964.

> **Prior art: Rota, On the foundations of combinatorial theory I: theory of Moebius functions, Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368. The antichain form of mu on a distributive lattice is his.**

### Modularity (equality, not submodularity)

**rank(a∨b) + rank(a∧b) = rank(a) + rank(b) with rank = Σxᵢ, for every pair — derived: per coordinate max(aᵢ,bᵢ) + min(aᵢ,bᵢ) = aᵢ + bᵢ as integers, and summing over the eight coordinates gives the identity because sublattice of a product (§7.3) makes ∨ and ∧ coordinatewise; equality rather than the submodular ≤ is the graded signature of distributivity — a graded lattice whose rank meets the equality is modular, and Λ, distributive, could not do otherwise; verified over all 475,800 unordered pairs, zero failures**

*the equality is pointwise arithmetic plus sublattice of a product; the equivalence with modularity on a graded lattice is the rank criterion*

Proved — M §8.2; Dedekind 1900; Birkhoff 1940.

> **Prior art: the modular rank identity holds in any modular lattice and every distributive lattice is modular. Dedekind, Math. Ann. 53 (1900); the rank criterion, Birkhoff, Lattice Theory (1940).**

### The interval measure

**d(x,y) has five equivalent forms, all equal to ∏_i(|x_i−y_i|+1): (1) the interval count |[x∧y, x∨y]|, the number of cells z with x∧y ≤ z ≤ x∨y; (2) the coordinate form ∏_i(|x_i−y_i|+1); (3) the two-integer form τ(N(x)N(y)/gcd(N(x),N(y))²); (4) the one-rational form τ(a·b) where N(x)/N(y) = a/b in lowest terms; (5) the p-adic form ∏_p(|v_p(ρ)|+1) with ρ = N(x)/N(y). The five collapse to one because the divisor embedding divisor lattice embedding (§9) puts one prime on each coordinate: the exponent of p_i in ρ = N(x)/N(y) is exactly x_i − y_i, so |v_{p_i}(ρ)| = |x_i − y_i| and forms (2) and (5) are the same product; τ counts divisors multiplicatively over the primes, giving forms (3) and (4) the same product of (|x_i−y_i|+1); and the interval [x∧y, x∨y] is, in a product of chains, the box ∏_i [min(x_i,y_i), max(x_i,y_i)], whose cell count is ∏_i(|x_i−y_i|+1) — form (1). All five verified equal on 2,000 random pairs with zero mismatch, the p-adic form checked by an independent factorisation of numerator and denominator. d(x,x) = 1 because every |Δ_i| = 0: a point counts itself**

*τ the divisor count; the equivalence is forced by the one-prime-per-coordinate embedding, not sampled — the sampling checks the instrument. arithmetic (τ of a ratio), geometric (a box of cells), and order-theoretic (an interval) write the one quantity three ways, and the p-adic and two-integer forms are its arithmetic re-expressions*

Proved — M §9.2; Monjardet 1981.

> **Prior art: the interval size as a product of coordinate spans, and its arithmetic form via lcm and gcd. Monjardet, Metrics on partially ordered sets, Discrete Math. 35 (1981) 173-184.**

### Distinct-prime-counting function

**ω(N(x)) ≤ 8, the coordinate count — proved and tight. In the divisor embedding divisor lattice embedding (§9) each coordinate carries its own prime, N(x) = ∏ᵢ pᵢ^{xᵢ}, so a prime pᵢ divides N(x) exactly when its exponent xᵢ is positive; ω(N(x)), the count of distinct prime divisors, is therefore |{ i : xᵢ > 0 }|, one prime admitted per occupied coordinate and never more than the eight coordinates that exist — the bound is the coordinate count by construction, with no appeal to the order of Λ. It is tight: the cell (2,1,3,3,2,1,3,3) has all eight exponents positive, so N of it is divisible by all eight primes and ω = 8, verified by direct factorisation; one hundred cells attain it. The floors n, k, e ≥ 1 force those three exponents positive on every cell, so ω ≥ 3 everywhere, the minimum realised at the bottom cell (1,0,1,0,1,0,0,0) where the other five coordinates rest at zero. The bound is NOT the order dimension, which is 7 (order dimension (Dushnik–Miller) (§8.6)): at the tight cell ω = 8 exceeds dim, so the two quantities are distinct and the coordinate count is the correct ceiling**

*ω is |{ i : xᵢ > 0 }| directly, not the count of non-minimal coordinates — the floors put three primes on every cell; the earlier bound quoted dim(Λ) when 8 was believed to be the dimension, but the one-prime-per-coordinate proof always proved the coordinate count, and dim = 7 leaves it the only defensible ceiling*

Proved — M §9.1; Birkhoff 1937.

> **Prior art: in the divisor representation (Birkhoff, Lattice Theory, 1940), the number of distinct primes dividing N(x) is the number of coordinates on which the exponent is positive, bounded by the coordinate count. The counting function ω itself is classical number theory; what is measured here is that on Λ it reaches its ceiling of eight and that this ceiling is the coordinate count and not the order dimension.**

### Palindromic rank polynomial ⟺ self-dual

**F palindromic ⟺ the poset is self-dual, and Λ fails both by a single witness — proved. Read the rank sizes from both ends: forwards 1, 5, 15, 34, 59, 87 · backwards 1, 4, 10, 21, 37, 57 — they part company one step in, 5 against 4, so F is no palindrome and Λ admits no rank-reversing automorphism. §8.3 reports as separate numerical facts that only 8 of 976 cells survive x → top − x and that the rank sequence is asymmetric; they are the same statement — the failed reflection and the failed palindrome are one asymmetry read in two languages**

*graded poset; Λ at the caps of §7.4*

Proved — M §11.8; Stanley 1986.

> **Prior art: Stanley, *Enumerative Combinatorics I* (1986), ch. 3 — a graded poset's rank polynomial is palindromic iff it is rank-symmetric. The one-witness reading on Λ — 5 against 4 one step in — and the identity of the failed reflection with the failed palindrome are this book's.**

### Join-prime and meet-prime

**no cell of Λ₈ is both join-prime and meet-prime, so pushback ≥ 16 > 0 for every cell**

*18 join-irreducibles and 18 meet-irreducibles, intersection empty*

Proved — M §16.8.5; Birkhoff 1937; Gratzer 1978.

> **Prior art: join-prime and meet-prime are dual notions in a distributive lattice, and a cell cannot generally be both. Gratzer, General Lattice Theory (1978).**

### The rank polynomial

**F(z) = z³(z¹⁷ + 4z¹⁶ + 10z¹⁵ + … + 122z⁸ + 121z⁷ + … + 5z + 1); F′(1)/F(1) = 11.0666**

*single-variable specialisation*

Computed — M §11.1; Stanley 1986.

> **Prior art: Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 3. F'(1)/F(1) = mean rank is the standard first-moment identity.**

### The index against the real subshells

**Λ's eight constraints on 247 real subshells across ALL 118 elements incl. 19 anomalies and 15 predicted superheavies: 18,288 tests, 0 failures**

*IUPAC ground states*

Computed — close_L.py; Madelung 1936; NIST.

> **Prior art: the 247 real subshells across 118 elements are the observed ground configurations, tabulated by NIST; the ordering is Janet-Madelung. Testing Λ constraints against them checks the index, not the table.**

### The rank skew

**centre of mass 11.0666 vs midpoint 11.5, skew −0.43; only 8 of 976 cells fixed by x ↦ max − x**

*at the stated caps*

Computed — M §8.4; Gauss 1809.

> **Prior art: the third standardised moment of a rank distribution. Gauss (1809).**

### The Sperner property

**the largest antichain equals the largest rank level: 122 at rank 11, certified by a Dilworth partition of all 976 cells into 122 chains — no antichain exceeds a chain cover, and level 11 achieves it; the rank sequence 1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1 over ranks 3–20 is log-concave at every interior rank, hence unimodal; Λ is NOT rank-symmetric — centre of mass 11.07 against midpoint 11.5, skew −0.43, the sequence and its reverse first parting at rank 4, five against four — and NOT self-dual: 8 of 976 cells survive x ↦ max − x against the box maxima (3,1,3,3,3,1,3,3), none fixed; restricted to one occupancy coordinate the reflection is particle-hole conjugation, terms(pᵏ) = 1, 1, 3, 3, 3, 1, 1 for k = 0..6, exactly symmetric**

*Dilworth partition computed by bipartite matching on the full comparability relation; log-concavity is rᵢ² ≥ rᵢ₋₁rᵢ₊₁ at every interior rank*

Proved — M §8.4; Sperner 1928; Dilworth 1950; Stanley 1980.

> **Prior art: Sperner 1928 for the Boolean lattice; Dilworth 1950 for antichain = chain cover; Stanley, SIAM J. Alg. Disc. Meth. 1 (1980) 168-184 proves the order-ideal lattice of a product of chains is Peck — rank-symmetric, rank-unimodal, strongly Sperner. Λ is measurably NOT rank-symmetric, so the Peck property does not transfer whole: Sperner survives, symmetry does not, and the certificate above is direct rather than inherited.**

### The detachable leaf

**2S is a leaf of the constraint tree (§8.5, §11.4) — it appears in exactly one bound, 2S ≤ k — so it detaches cleanly: its sum over the cells closes as a geometric series, [Σ_{S=0}^{k} z₈^S] = (1 − z₈^{k+1})/(1 − z₈), and it multiplies the rank polynomial (§11.1) by that factor and nothing else. Spin multiplicity is algebraically inert — it scales every seven-coordinate cell's count by (k+1) and changes no structure, which is why deleting it leaves the closure defect at zero, proved and verified at the caps of §7.4. Removing 2S projects Λ onto the seven-coordinate lattice on (n, ℓ, k, q, e, f, g); that projection has 319 cells and is itself closed, its polytope's integer points equal to its cells exactly, so E = 0 both before the leaf is removed and after; every one of the 319 seven-coordinate cells carries exactly k+1 spin values, and Σ (k+1) = 976 recovers the full count. The factorisation is exact — the full rank polynomial F(z) equals Σ over the 319 seven-cells of z^{n+ℓ+k+q+e+f+g} · (1 − z^{k+1})/(1 − z), checked against direct enumeration at z = 2, 3, ½ and −1, where it also reproduces F(−1) = 2. Spin is the one coordinate the index can shed without cost**

*2S the eighth coordinate, its only bound 2S ≤ k, hence a leaf of the constraint tree; the seven-coordinate projection onto (n, ℓ, k, q, e, f, g); counts at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Proved — M §11.6; Euler 1748; Lauritzen 1996.

> **Prior art: the geometric-series closed form is Euler; a leaf coordinate summing out of a tree factorisation is Lauritzen, *Graphical Models* (1996), the same elimination the box factorisation (§10.4) performs. That 2S is that leaf, that spin multiplicity is therefore algebraically inert, and that its removal leaves E = 0 on a 319-cell closed index, are this book's.**

### The interval-removal step

**X ∖ [a,b] is a sublattice iff a is join-prime and b is meet-prime; step(Λ₈) = 4**

*distributive*

Proved — M §16.8.5; Birkhoff 1937; Gratzer 1978.

> **Prior art: removing an interval leaves a sublattice iff the endpoints are join-prime and meet-prime — the standard interval-removal criterion. Gratzer, General Lattice Theory (1978), ch. II.**

### The membership function is total

**χ_Λ : ∏A_i → {0,1} is total: membership decided for every ambient point**

*Λ a finite intersection of decidable comparisons*

Proved — M §16.5; Birkhoff 1940.

> **Prior art: a membership function defined by inequalities on coordinates is total on the ambient product by construction.**

### The constraint tree

**constraint graph n—ℓ—k—q—g—f—e with 2S pendant at k: 8 nodes, 7 edges, a caterpillar; treewidth 1**

*every constraint binds exactly two coordinates*

Computed — M §8.5, §11.4; Freuder 1982.

> **Prior art: that a constraint graph is a tree, and what follows from it, is Freuder, A sufficient condition for backtrack-free search, J. ACM 29 (1982) 24-32.**

### The void

**void(x,y) = ∏_i(|Δ_i|+1) − |[x∧y, x∨y] ∩ Λ|**

*none*

Definitional — M §10; Rota 1964.

> **Prior art: the difference between a box count and the cells it actually contains is what Moebius inversion would compute. Rota (1964).**

### The void-free fraction

**The seven constraints are positively dependent over pairs of cells, and the dependence runs only along the constraint tree — proved, with the factor derived. For a pair (x,y) of Λ-cells the box [x∧y, x∨y] lies inside Λ iff each constraint xᵢ ≤ φ(xⱼ) holds throughout it, which by monotonicity of φ is the single comparison hiᵢ ≤ φ(loⱼ) (`M §10.3`). Each comparison is a NARROWNESS condition on the coordinates it touches: at zero width in the shared coordinate it holds with probability 1, and its probability falls monotonically with that width (q ≤ k: 1.000, 0.599, 0.319 at widths 0, 1, 2). Two constraints that share a coordinate are therefore two decreasing functions of one width variable, and Chebyshev's sum inequality gives P(both) ≥ P(one)·P(other) — the dependence is positive, and it is positive for this reason and no other. Conditioned on the shared coordinate's interval (lo, hi) the two are independent: the lift P(both | interval)/(P(one | interval)·P(other | interval)) is 1.0000 in every stratum for all five shared-coordinate pairs, so all dependence flows through shared coordinates and nowhere else; constraint pairs sharing no coordinate measure lifts 0.9999–1.0101. Because the constraint graph is a tree (the constraint tree (§8.5)), the joint probability factorises along it by the chain rule, and the factor above independence is exactly the product of the six edge lifts in tree order: at caps (3,3,1,3,1), exhaustively over all 475,800 unordered pairs, individual rates 69.95–98.06%, product 20.13%, joint 28.35%, and 1.0838 × 1.0854 × 1.1212 × 1.0522 × 1.0125 × 1.0022 = 1.4081 = joint/product to four decimals. The factor is cap-dependent (1.33–1.66 across six settings from 976 to 234,340 cells) because the edge lifts are; the recorded 27.7–30.1% void-free fraction across 776M pairs, and its joint 30.13% against product 20.19% giving 1.49, are the measurement at the original larger population, consistent with this law and not reproduced here**

*pairs (x,y) of Λ-cells; box [x∧y, x∨y] in the ambient product of chains; containment tested as hiᵢ ≤ φ(loⱼ) per constraint; base-cap instance exhaustive at (n,e,ℓ,k,f) = (3,3,1,3,1); the 776M-pair figures at their original cap family, which the record does not name*

Proved — M §10.2, §10.3; Rota 1964; Lauritzen 1996.

> **Prior art: as the void (§10) for the fraction. Positive association of two decreasing functions of one variable is Chebyshev's sum inequality; factorisation of a joint law along a tree by conditional independence is the Markov property, Lauritzen, Graphical Models (1996). The derivation of the factor as a product of edge lifts is this book's.**

## T. The tower and its couplings — 16 objects

### Racah 1943 seniority

**2S′ ≤ v ≤ g, v ≡ g (mod 2)**

*Racah seniority for ℓ^N*

Cited — M §12.11.1 / T A14; Racah 1943.

> **Prior art: seniority v, with 2S ≤ v ≤ g and v congruent to g mod 2, is Racah, Phys. Rev. 63 (1943) 367-382 — the classification of states of l^n by the number of unpaired electrons.**

### The parent bound

**2J_c ≤ φ̂(k), φ̂ = max 2J over terms of ℓ^k = {1:3, 2:4, 3:5}**

*φ̂ read off the realised extent, not from a law*

Computed — M §12.11.1 / T A15; Condon & Shortley 1935; Racah 1942.

> **Prior art: the term structure of a subshell l^k, and the maximum J it carries, is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. VII; Racah, Theory of complex spectra II, Phys. Rev. 62 (1942) 438-462, gives the general classification. The values {1:3, 2:4, 3:5} are read from that table, not derived here.**

### The recoupling bound

**loose: 2K ≤ 2J_c + 2f_max (one parent). exact: |2J_c−2f| ≤ 2K ≤ 2J_c+2f step 2 (two parents)**

*jK pair coupling*

Cited — M §12.11.1 / T A16; Wigner 1931; Racah 1942.

> **Prior art: the triangle condition |j1-j2| ≤ J ≤ j1+j2 in steps of one is the Clebsch-Gordan series — Wigner, Gruppentheorie (1931); its application across parents is Racah, Phys. Rev. 62 (1942) 438-462.**

### The spin-half bound

**|2J − 2K| ≤ 1**

*outer electron carries spin ½*

Cited — M §12.11.1 / T A17; Condon & Shortley 1935.

> **Prior art: |2J - 2K| ≤ 1 is the coupling of a spin-half to K in the jK scheme; Condon & Shortley (1935), ch. X.**

### The seniority floor

**2S′ ≤ g**

*vector coupling on the target*

Cited — M §12.10.1; Racah 1943.

> **Prior art: 2S ≤ g bounds the total spin by the occupancy — Pauli exclusion in Racah seniority form, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### The admissible Pauli cut

**2S′ ≤ 2f+1 (the admissible Pauli cut); Λ₉′ = 1,561 cells, 93 removed; closes the cycle f–g–2S′**

*min(g,4f+2−g) ≤ 2f+1 by averaging*

Computed — M §12.11.1 / T 2.2 (App. G); Pauli 1925; Racah 1943.

> **Prior art: the Pauli cut on a subshell's allowed terms is Pauli's exclusion principle (Z. Phys. 31, 1925) as applied to equivalent electrons; the seniority classification that makes it computable is Racah, Theory of complex spectra III, Phys. Rev. 63 (1943) 367-382.**

### The axis density

**density(axis) = Σ_parents |exact fibre| / Σ_parents |admissible fibre| = 63.7, 67.5, 44.7, 17.0, 31.4, 64.4%**

*three non-obvious exact sets required*

Computed — M §12.11.1 / T A18; Racah 1942; Wigner 1931.

> **Prior art: the ratio of exact to admissible fibre sizes measures how much a triangle condition tightens a Pauli bound. Both bounds are standard; the ratio is measured.**

> **Prior art: the ratio of exact fibre to admissible fibre measures how much the triangle condition (Wigner 1931, Clebsch-Gordan) tightens the Pauli cap (Racah 1942). Both bounds are theirs; the density is measured.**

### The counting-coupling dichotomy

**counting coordinates close exactly; coupling coordinates close as envelopes; no third kind**

*the exact coupling bound is made of reflection, congruence and triangle*

Computed — M §12.11.3; Racah 1942.

> **Prior art: the split between coordinates that COUNT (occupancy, capacity) and coordinates that COUPLE (J, K, S) is the organising distinction of Racah's algebra. Counting coordinates carry Pauli caps; coupling coordinates carry triangle conditions, and the two close differently.**

### The three excluded forms

**three excluded forms: REFLECTION (particle–hole conjugation), CONGRUENCE (fermion parity), TRIANGLE (one sum and one difference)**

*each is non-monotone or multi-parent*

Computed — M §12.11.2; Racah 1943; Wigner 1931.

> **Prior art: particle-hole conjugation, fermion parity and the triangle rule are all standard: conjugation from the complementary-shell theorem (Racah 1943), parity from the antisymmetry of the wavefunction, and the triangle inequality |j1-j2| ≤ J ≤ j1+j2 from the Clebsch-Gordan series (Wigner 1931).**

### Basis independence of the level set

**the exact J multiset is identical in jK, LS, LK and jj; the four cell counts price four ROUTES**

*coupling schemes are basis changes*

Computed — M §12.11.4; Wigner 1931; Racah 1942.

> **Prior art: the J multiset of a configuration is independent of coupling scheme because the schemes are unitary recouplings of one space — Wigner, Gruppentheorie (1931); Racah's 6-j and 9-j coefficients are the transformation matrices. What is measured here is the CELL COUNT each scheme costs, not the invariance.**

### Parastatistics

**capacity(ℓ) = m(4ℓ+2) for parastatistics of order m; E = 0 through Λ₁₃ for m = 1,2,3**

*m(4ℓ+2) monotone in ℓ for every m, so the tightening rule (§14.4) is preserved*

Computed — T 2.1 (App. G) / D3; Green 1953.

> **Prior art: parastatistics of order m, in which a state holds up to m particles, is H. S. Green, A generalized method of field quantization, Phys. Rev. 90 (1953) 270-273. The capacity m(4l+2) is its shell-model form.**

### The bounds against real terms

**the four coupling bounds on the exact term structure of every subshell: 85,829 tests, 0 failures**

*ℓ = 0..3, k = 1..4ℓ+2*

Computed — microstate enumeration; Condon & Shortley 1935.

> **Prior art: the exact term structure of every subshell is tabulated in Condon & Shortley (1935), ch. VII, and in the NIST compendium. The 85,829 tests check the four coupling bounds AGAINST that table; the table is not this work.**

### The four coupling schemes

**closure holds in LS, LK, jK, jj: Λ₁₃ = 431,050 / 341,150 / 199,130 / 206,520, E = 0 throughout**

*a uniform one-parameter looseness convention*

Computed — T 2.1b (App. G); Condon & Shortley 1935; Racah 1942.

NOT CHECKABLE and the book says why: the looseness convention is named and not printed, and two committed readings BRACKET rather than determine the figures — LS in [383,065, 597,325] contains 431,050, jj in [160,380, 244,060] contains 206,520 (R 1010)

> **Prior art: LS, LK, jK and jj are the four standard angular-momentum coupling schemes — Condon & Shortley (1935), ch. X; the jK and LK intermediate schemes are Racah's. That the same physical states are counted in each is the content of the recoupling theory, and the four cell counts price the SCHEME rather than the physics.**

### Constraint tightness as a count

**the tight-pair count of a base is exactly 2S, S the envelope-step count**

*van Beek & Dechter's measure*

Computed — M §14.5.9; Deville et al. 1999; Deville, Barette & Van Hentenryck 1999.

> **Prior art: the tight pairs of a staircase constraint are its envelope steps — Deville, Barette & Van Hentenryck, Artif. Intell. 109 (1999) 243-271.**

### The tower

**Λ₈…Λ₁₃ = 976, 1654, 2535, 13585, 70905, 199130; E = 0 at every stage under the closure-preserving bounds, swept against every ambient cell to 47,775,744**

*at stated caps*

Computed — M §12.11.0.10, reg. 249; Racah 1942; Condon & Shortley 1935; Racah 1942, 1943.

Measured on the rebuilt tower at the caps of §7.4. Under the exact coupling triangle at axis 12 the count is 22,275 and E = 35,570 (register 541; the tree or the tightness (§12.11.5)); the closure-preserving bound is the tower's convention, and a sequence is a single claim, so its terms come from one convention (register 1399). 199,130 is also the jK figure of the four coupling schemes: one number in two objects. Recorded at register 1788.

> **Prior art: the tower adjoins the coupling quantum numbers in the standard order — seniority, then J of the core, then K, then J. Each is Racah or Condon & Shortley; the cell counts and the closure at each stage are the measurement.**

### The tree or the tightness

**the tree or the tightness: imposing the exact triangle at axis 12 gives 22,275 cells and E = 35,570**

*the exact bound has two parents*

Computed — M §12.11.5 / T 2.4 (App. G); Freuder 1982; Racah 1942.

> **Prior art: the trade between tree structure and constraint tightness is Freuder (1982) for the tree side; the exact triangle is Racah/Wigner. The pricing is the measurement.**

## E. Empirical indexes — table, nuclide, layout — 4 objects

### The refusal map

**first ionisation energies given to the bracket as bare numbers refuse at Be→B, N→O, Mg→Al and P→S — four steps of twelve, 67% admissible**

*the same two positions in both periods: the s2-p1 subshell opening and the p3-p4 first pairing*

Computed — M §6.2; Mendeleev 1869; NIST.

> **Prior art: first ionisation energies as a periodic property date to Mendeleev; the values are NISTs. That bare numbers refuse the bracket is a statement about what a bracket needs, not about the data.**

### The price of a layout

**hydrogen's placement is free and helium's costs 16, and they are not additive: −16 and 0 apart, −1 together**

*E set by the largest group used in period 1*

Computed — M §6.1.1; Janet 1929.

> **Prior art: hydrogen and helium are the classic placement anomalies of the periodic table, and Janets left-step form resolves them differently from the classroom table. The cost measured here is of the CHOICE.**

### The nuclide chart's defect

**the measured nuclide chart indexed by (Z, N) closes at E = 9, stable across four proton-number cutoffs; the nine cells are the mass formula's pairing and clustering terms**

*cells named at one cutoff persist at every larger one*

Computed — M §6.2; Segre 1945.

*** COUNT NOT REPRODUCED 2026-08-11 (R 1550). *** AME2020 Table I was captured from the published paper (Chin. Phys. C 45, 030003, Table I, 3558 rows, Z = 0-118, A = 1-295) and E recomputed with the same operator: E = 2, NOT 9, and stable at 2 across cutoffs Z ≤ 20, 50, 82, 92 and 118. Six variants of the cell set were tried - axes swapped, neutron excluded, measured-only, Z and N both positive - and none gives 9; measured-only gives 95. WHAT DOES REPRODUCE: the STABILITY across cutoffs, the cells being NAMEABLE PHYSICS, and the reading of them as the mass formula pairing term - the two defect cells are the empty cell (0,0) and Z=2 N=0, THE DIPROTON, which is unbound and is the textbook pairing failure. Three of four claims hold and the number does not. Cause UNDETERMINED: a different source edition, a different inclusion rule, or an arithmetic error in the original.

> **Prior art: the chart of nuclides indexed by (Z, N) is Segres chart, in use since the 1940s.**

### The thirty-six decomposed

**the periodic table's 36 decompose 25 + 11, not 26 + 10; E is placement-sensitive, 36 at group 18 and 20 at group 2**

*all 118 elements*

Computed — M §6.1.1; Mendeleev 1869; Janet 1929.

> **Prior art: the periodic tables arrangement is Mendeleev, Über die Beziehungen der Eigenschaften zu den Atomgewichten der Elemente, Z. Chem. 12 (1869) 405-406; the left-step form on n+l is Janet (1929). That E is placement-sensitive is a statement about which arrangement, not about the elements.**

## B. The bracket — 21 objects

### The price V — the bracket's width against its error

**V = w/e where w = |T(n+1)−T(n−1)|, e = |T(n) − ½(T(n−1)+T(n+1))|**

*three consecutive members*

Definitional — M §21.1; Milne-Thomson 1933.

> **Prior art: the ratio of a first difference to a second is the standard curvature-to-slope measure of a finite-difference scheme. Milne-Thomson, The Calculus of Finite Differences (1933), ch. I-II.**

### The four-thirds law

**V = 4ν/3 for a Rydberg series; in general V(x,p) = 4x/(h|p−1|) for y = x^p**

*T = Z²R/ν²*

Computed — M §21.1; Rydberg 1890.

> **Prior art: for a Rydberg series T ~ nu^-2, so the ratio of first to second differences is 4nu/3 by direct expansion. Rydberg, Recherches sur la constitution des spectres d emission, K. Sven. Vetensk. Akad. Handl. 23 (1890).**

### The exact price

**V = 4ν³/(h(3ν²−h²)); with r = ν/h, V = 4r³/(3r²−1). Z and R cancel identically**

*step h free*

Proved — M §21.4; Rydberg 1890.

> **Prior art: the exact form follows from the Rydberg term T = Z^2 R / nu^2 by finite differencing; Z and R cancel because the ratio is scale-free.**

### The five-sigma admissibility threshold — where the bracket may be applied at all

**r = 2Z²R/(ν³σ) ≥ 5**

*levels separated by more than 5σ*

Definitional — M §22.5; Gauss 1809.

> **Prior art: a five-sigma admissibility threshold is a statement about signal against measurement error, in the Gaussian error model of Gauss, Theoria motus corporum coelestium (1809).**

### Aitken Δ² / Seki Kōwa

**Aitken's Δ² on a Rydberg series lands at I − T/3, because the correction is (ΔT)²/Δ²T → (2/3)T**

*algebraic not geometric convergence*

Proved — M §24.6; Aitken 1926.

> **Prior art: Aitken, On Bernoulli's numerical solution of algebraic equations, Proc. R. Soc. Edinb. 46 (1926) 289-305 — the delta-squared process. That it lands at I - T/3 on a Rydberg series is the measurement; the process is his.**

### Monotone interpolation bracket

**T(n) lies between T(n−1) and T(n+1)**

*T monotone in n within a channel*

Proved — M §20.1; Leibniz 1682; Milne-Thomson 1933.

measured at 789 of 789 interior cells — and it is the TRIVIAL bracket, which cannot fail (R 797, 830)

> **Prior art: that a term of an alternating or monotone sequence lies between its neighbours is the classical bracketing of finite differences — Leibniz's alternating-series test in its difference form; Milne-Thomson, The Calculus of Finite Differences (1933), ch. I. The book's contribution is applying it to Rydberg terms cell by cell, not the bracket.**

### The assembly rule — a composite observable's scaling exponent is 2a + 3b

**an observable ⟨r⟩^a/(ΔE)^b scales as ν^{2a+3b}**

*⟨r⟩ ∝ ν², ΔE ∝ ν⁻³*

Proved — M §24.1; Bohr 1913; Bethe & Salpeter 1957.

> **Prior art: the scaling of hydrogenic expectation values, <r^a> ~ nu^{2a} and Delta E ~ nu^{-3}, is Bohr's correspondence scaling (1913) in its quantum form; tabulated in Bethe & Salpeter, Quantum Mechanics of One- and Two-Electron Atoms (1957), sec. 3.**

### When the bracket fails

**the bracket fails ⟺ |ΔT| > 2Z²R/ν³**

*a perturber reorders only if the shift exceeds half the local spacing*

Proved — M §23.3; Rydberg 1890.

the yardstick verified: 2Z^2R/nu^3 against measured adjacent spacing over 742 pairs gives median 1.201 (R 832)

> **Prior art: the local spacing of a Rydberg series is 2 Z^2 R / nu^3, the derivative of the term formula. A shift exceeding half of it reorders the levels.**

### The floor at two

**V > 2 for any monotone sequence; V → 2 only as one step vanishes**

*d₀,d₁ > 0; V = 2(d₀+d₁)/|d₀−d₁|*

Proved — M §21.2 Prop 14.1; Jensen 1906.

> **Prior art: V > 2 for a monotone sequence is a form of Jensen's inequality — the chord lies above the curve for a convex function, so the second difference cannot exceed half the first. Jensen, Sur les fonctions convexes, Acta Math. 30 (1906) 175-193.**

### The Rydberg floor

**V ≥ 32/11 = 2.909 for a Rydberg series specifically**

*hydrogenic form*

Computed — M §21.2; Rydberg 1890; Jensen 1906.

> **Prior art: the floor V > 2 is Jensen convexity (1906); the sharper 32/11 for a Rydberg series follows from its specific nu^-2 form.**

### The fractional widths

**w/T = 4(h/ν) + 8(h/ν)³ and e/T = 3(h/ν)²; their ratio is V**

*Rydberg*

Computed — M §21.6; Taylor 1715.

> **Prior art: expanding the first and second differences of nu^-2 in powers of h/nu is Taylor series with a step. Taylor, Methodus incrementorum directa et inversa (1715).**

### The optimal step

**h* = √(2β/(α y″)) minimises αw + βV, valid for h* ≪ ν**

*leading order*

Computed — M §21.5.3; Lagrange 1797; Curtis & Reid 1974.

NOT CHECKABLE here: its source M §21.5.3 does not appear in the book's text and the objective it minimises is not stated, so the stationary point cannot be verified (R 1010)

> **Prior art: minimising a weighted sum of two competing costs by setting the derivative to zero is elementary optimisation; the h* ~ √(2 beta/(alpha y)) form is the standard step-size optimum of finite-difference practice.**

> **Prior art: the optimal finite-difference step balances truncation error against roundoff, giving h* proportional to √(eps/y) — Curtis & Reid, The choice of step lengths when using differences to approximate Jacobian matrices, J. Inst. Math. Appl. 13 (1974) 121-126. Here the two costs are width and price rather than truncation and roundoff, and the same balance applies.**

### Newton decrement, Nesterov–Nemirovskii 1994

**8y′²/y″ = 8λ² with λ² = ∇f ᵀ[∇²f]⁻¹∇f; for a Rydberg series λ² = (2/3)T**

*one dimension: λ² = f′²/f″*

Proved — M §23.8.1; Newton 1669; Nesterov & Nemirovskii 1994.

> **Prior art: the Newton decrement lambda^2 = grad f^T [Hess f]^{-1} grad f is the standard measure of proximity to a minimum in interior-point theory (Nesterov & Nemirovskii 1994); Newton's method itself is De analysi (1669).**

### The value-one crossing — where the bracket's price V passes unity

**ν_V = (3Z²R/5q)^{1/4}**

*curvature resolvable at quotation granularity q*

Proved — M §23.15; Rydberg 1890.

the crossing where V passes unity, computed from the quotation granularity q

> **Prior art: solving V = 1 for nu against a quotation granularity q gives the quartic root; the term formula is Rydberg (1890).**

### The ordered bracket

**sign(f(n) − p(n)) = (−1)^{k+1}(−1)^m with m nodes above n; a two-sided deductive bracket at every order**

*sign(f^{(j)}) = (−1)^j*

Proved — M §23.10.1; Newton 1687; Milne-Thomson 1933.

> **Prior art: the sign of the error of a Newton interpolating polynomial alternates with the number of nodes above the evaluation point — the standard remainder theorem for finite differences, Newton's divided-difference form (Principia, Book III, Lemma V); Milne-Thomson (1933), ch. VIII.**

### The admissible order

**order k admissible while |Δ^{k+1}T| > 5·2^{k+1}·σ**

*the (k+1)-th difference is a signed sum of 2^{k+1} levels*

Proved — M §23.10.4; Milne-Thomson 1933.

> **Prior art: the admissible order of a difference scheme is set by where the next difference falls below the noise, and the 2^(k+1) growth of noise under k-fold differencing is standard. Milne-Thomson (1933), ch. II.**

### The width-price front

**dw/dh > 0 and dV/dh < 0 for every monotone convex y and every h; the family {(w,V)} is a Pareto frontier**

*w ~ h, e ~ h²*

Proved — M §21.5.2; Pareto 1896.

> **Prior art: a family in which no member improves both objectives is a PARETO FRONT — Pareto, Cours d'economie politique (1896). That dw/dh > 0 and dV/dh < 0 for every monotone convex y makes {(w,V)} one is the proof here; the notion is his.**

### The linear pole

**V has a pole at p = 1: a linear observable has no curvature to price**

*y = x^p*

Proved — M §18.5; classical; Taylor 1715; Milne-Thomson 1933.

> **Prior art: a linear function has vanishing second difference, so any ratio measuring curvature against slope diverges there. The pole at p = 1 is that statement.**

### The rank-one factorisation

**rank(log q) = 1 across fifteen Rydberg observables; second singular value 1.8×10⁻¹⁴**

*every observable is ν to a power*

Computed — M §24.2; Eckart & Young 1936.

> **Prior art: that a matrix has rank one is read from its singular values — Eckart & Young, The approximation of one matrix by another of lower rank, Psychometrika 1 (1936) 211-218. A second singular value of 1.8e-14 is numerical zero, so log q factorises exactly.**

### Self-concordance

**T(ν) is self-concordant, |f‴| ≤ 2(f″)^{3/2}, for ν ≤ (√6/2)·Z√R**

*T = Z²R/ν²*

Proved — M §23.8.2; Nesterov & Nemirovskii 1994.

> **Prior art: self-concordance, |f'''| ≤ 2(f'')^{3/2}, is Nesterov & Nemirovskii, Interior-Point Polynomial Algorithms in Convex Programming (1994), the condition under which Newton's method converges at a rate independent of the problem's conditioning.**

### What silence implies

**the bracket holding ⟹ |ΔT| < 2Z²R/ν³ at that cell**

*contrapositive of when the bracket fails (§23.3)*

Proved — M §23.5; Rydberg 1890.

849 of 849 cells satisfy it; median |dT|/spacing 0.0015, largest 0.25 (R 831)

> **Prior art: the contrapositive of when the bracket fails, on the same term formula.**

## K. Transit and information — 25 objects

### The arrow index

**X_w = {a : w(tgt a) ≤ w(src a)} is closed; one arrow per coordinate and no others; sums, max and min all fail**

*w a single coordinate*

Computed — M §12.11.0.2; Birkhoff 1937.

> **Prior art: a set of the form {a : w(target) ≤ w(source)} for monotone w is a down-set of the induced order, hence closed. Birkhoff, Rings of sets (1937).**

### The axis test

**an axis earns a COORDINATE when it is independent of the others AND its distinct values are few relative to what it adds; both conditions are necessary**

*a closed index and a candidate axis*

Measured — R 1127-1131; Dushnik & Miller 1941; Shannon 1948.

on the same elements, Z≤16: (Z,charge,l) gives 0% redundancy, +multiplicity gives 82%, +2J gives 0% again. 2J is NOT derived — no combination determines it — but |L-S| ≤ J ≤ L+S constrains it to 2min(l,S)+1 values of seventeen. A coordinate must be free, not merely undetermined. The entropy account is PARTIAL: retained entropy is 26% for multiplicity and 27% for 2J, which does not separate them

> **Prior art: an axis earns a coordinate when it is order-independent of the others (Dushnik & Miller 1941) and carries information (Shannon 1948). The test combines both.**

### The tower's two ends joined

**at every consecutive stage Λ_{D+1} → Λ_D the correspondence from a rank above to the ranks below is a GAP-FREE INTERVAL with both endpoints monotone — no exception across all 199,130 cells — so the tower's chains form ONE directed system of monotone brackets χ(Λ₁₃) → … → χ(Λ₈), composition of the five stage-brackets containing the direct bracket with slack ≤ 2 rank units; the projection from Λ₁₃ covers ALL of χ(Λ₈), ranks 3 through 20 without gap, two routes agreeing — the 1D chain is the system's TERMINAL OBJECT, entirely inside the image from the top, and the 14D direction is the same system's LIMIT; the strict MAP form is REFUTED, branching 4, 4, 6, 8, 9 growing with height**

*register 334's sentence — a bracket, not a map — proved stage-by-stage down the whole tower; the proof carries at full resolution with no bit-encoding, the connection's native language the bracket, the house currency; provenance: the build reproduced seven of seven Λ₈ fingerprints and every printed tower count before anything was measured on it*

Proved — M §12.11.0.11; 03-1D-lands-inside-14D; tower.py, tower3.py, factor.py.

> **Prior art: §22's outward rule — composition pays a bounded, priced slack — appearing inside the tower; no external attribution claimed, the exhaustive stage census is the measurement.**

### The tower is a category

**Λ₉ is a category: 41,682 composable pairs, zero failures, associative**

*as composition (§12.11.0)*

Computed — M §12.11.0; Mac Lane 1971.

> **Prior art: associativity of composition and the existence of identities are the category axioms — Mac Lane, Categories for the Working Mathematician (1971). Verifying them on 41,682 composable pairs checks that Λ₉ IS a category; the axioms are not this work.**

### The composition clock

**occupancy never rises along composition: 0 of 739 steps; the tick is k − g = (k−q) + (q−g)**

*destinations begin empty — an assumption, not a constraint*

Computed — M §12.11.0.1; classical; Floyd 1967.

> **Prior art: a quantity that never increases along composition is a MONOVARIANT, the standard tool for proving termination. That occupancy is one here is the measurement; the technique is old.**

### The clock that does not tick

**index (g,G) with g ≤ G ≤ 4f+2 and g ≤ q: 13,775 cells, closed, and 31.6% of composable pairs raise occupancy**

*prior occupancy carried as a coordinate*

Computed — M §12.11.0.2; Floyd 1967.

> **Prior art: a candidate variant that is closed but does not decrease is a failed termination measure. Floyd (1967).**

### Composition

**b∘a defined when tgt(a) = src(b); the composite transfers min(q_a, q_b)**

*Λ₉'s target (e,f,g,2S′) has the source's constraint forms*

Computed — M §12.11.0; Mac Lane 1971.

> **Prior art: composition defined when target meets source is the category axiom; what is measured is that the composite transfers min(q_a, q_b), which is a property of this index and not of categories.**

### Corners and faces

**the whole-object defect decomposes into FACES and CORNERS, and the corners are an artefact of loose coordinatisation**

*an index of dimension d and its d-1 axis slices*

Measured — R 1177; Freuder 1978.

of the 6,195 cells R admits and Λ_spectra does not hold, 3,993 are admitted by some three-axis slice and 2,202 by none. Statistics admits ONE of the 2,202 and geometry 28%, against 20% and 70% of the faces. And every available fifth coordinate makes the corners worse — by 70% to 652% — because all four candidates are DERIVED (register 1122)

> **Prior art: cells admitted by the full closure and by no lower-arity projection are exactly the k-consistency gap — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966.**

### The refuted conjecture

**coordinate COUPLING does not predict redundancy**

*a closed index*

Measured — R 1120; Dechter & Pearl 1989.

across six indices — Λ, Λ_spectra, the periodic table, Janet, the calendar, a box ordering — redundancy against coupling gives r^2 = 0.002, p = 0.94. Janet and the box ordering both have 50% coupling and 0% redundancy; Λ_spectra has 17% coupling and 20% redundancy

> **Prior art: that coupling alone does not predict what a local method achieves — the induced width, not the edge count, is the parameter. Dechter & Pearl, Tree clustering for constraint networks, Artif. Intell. 38 (1989) 353-366.**

### The dead ends, defined

**the non-composable cells are defined exhaustively: at Λ₁₀ all 485 have g = 0 and every g = 0 cell is non-composable; at Λ₁₃, 35,630 at g = 0, 13,750 with 2J in {6,7,8} which no 2J_c can start, and 22,680 failing only in combination**

*the occupancy floor (§10.2) is k ≥ 1, so a target ending empty can never be a source; and 2J inherits 2K's range while 2J_c is bounded by φ(k) alone*

Computed — M §12.11.1.5; Mac Lane 1971.

> **Prior art: cells that compose with nothing are those whose target is no other cell source — the non-composable part of a quiver.**

### Data-processing inequality + Pinsker

**for a tree-structured index, I(u;v) is non-increasing in tree distance d, and |P(A_u∩A_v) − P(A_u)P(A_v)| ≤ √(I(u;v)·ln2 / 2)**

*Markov random field on a tree; data processing; Pinsker*

Proved — M §12.11.0.7; Lauritzen 1996; Pearl 1988.

> **Prior art: mutual information is non-increasing in tree distance because every path is separated — the data-processing inequality on a Markov tree. Cover & Thomas, Elements of Information Theory (1991), Thm 2.8.1; Lauritzen, Graphical Models (1996), ch. 3.**

### The girth is four

**the girth of the unit-step graph on Λ₉ is exactly 4**

*unit-step adjacency = covering relation, 6,658 edges*

Proved — T 4.3 (App. G); classical graph theory; Berge 1962.

> **Prior art: girth is the length of the shortest cycle, standard since Euler. That a unit-step graph on a product of chains has girth 4 follows from the commuting square of any two coordinate moves.**

### Helly number

**molecular transit is an intersection question; the Helly number is ≥ 5 and ≤ 144**

*a molecule moves as one fibre; a circuit is a square; ground set C(9,2)·4 = 144*

Computed — T 4.4 (App. G); Helly 1923.

> **Prior art: the Helly number of a family is the least h such that every h-wise intersecting subfamily intersects — Helly, Über Mengen konvexer Körper mit gemeinschaftlichen Punkten, Jahresber. DMV 32 (1923) 175-176.**

### The categorial jump

**the axis that makes the tower a category is worth twenty points: Λ₈ is 50.3% composable and Λ₉, adding 2S' ≤ g, is 70.7%**

*the companion's index sits between them at 59.5% — three transition indexes, three fractions, so this is not a norm*

Computed — M §12.11.1.3; Mac Lane 1971.

> **Prior art: the axis that closes composition is the one that supplies identities and associativity — the category axioms. What is priced is the cell cost of adding it.**

### Closure as agreement

**E(X) = 0 if and only if the languages agree**

*an index of dimension ≥ 3 and two or more operators*

Measured — R 1176; Beeri, Fagin, Maier & Yannakakis 1983.

six indexes, three operators — order, statistics, geometry. Λ and a box ordering: E = 0 and every pair agrees, 0 cells differing. The periodic table, Janet, the calendar and Λ_spectra: E > 0 and every pair differs. No exception. Closure is therefore a language-theoretic property as well as an order-theoretic one, and the language test is cheaper: R enumerates the ambient product, pairwise consistency needs only the marginals

> **Prior art: global and local closures coincide exactly on acyclic structures — BFMY, J. ACM 30 (1983) 479-513. That E = 0 iff the languages agree is that theorem read as an equivalence.**

### The Markov property

**the future is conditionally independent of the past given the transfer: every past gives the same future set at each q**

*the constraint graph is a tree, q the cut vertex*

Computed — M §12.11.0.8; Lauritzen 1996; Pearl 1988.

> **Prior art: the future being conditionally independent of the past given the present is the MARKOV PROPERTY. Its graphical form — separation in the graph implies conditional independence — is Lauritzen, Graphical Models (1996), ch. 3, and Pearl, Probabilistic Reasoning in Intelligent Systems (1988).**

### The composability peak

**composability peaks at Λ₁₀ and falls after: 0.0000, 0.7068, 0.8087, 0.6956, 0.6592, 0.6381 across Λ₈ to Λ₁₃**

*counting axes raise the fraction and coupling axes lower it, with no exception — §12.11.3's dichotomy predicts the sign as well as the price*

Computed — M §12.11.1.4; Berge 1962.

> **Prior art: the composability fraction is the arc density of the composition quiver; its rise and fall with the tower is the measurement.**

### The production rule

**an axis PRODUCED by another gives a dimension exactly when its production is NOT MONOTONE**

*a closed index and an axis derived from its coordinates*

Measured — R 1143; Birkhoff 1937.

multiplicity is produced by Ne and cycles 2,{1,3},2,{1,3},{2,4} — NOT monotone — and adding it takes redundancy from 20% to 82%. Ne is produced by (Z,charge) and monotone: 0%. n0 is produced by (Z,charge,l) and monotone: 0%. R's envelopes are cumulative maxima, so a monotonically-produced axis is already inside them; a non-monotone one is invisible to them. This resolves the apparent contradiction between R 1122 and R 1123

> **Prior art: a monotone function of existing coordinates adds no join-irreducibles and so no dimension; a non-monotone one does. Birkhoff (1937).**

### The composition quiver

**composable cells are the arcs of a quiver Q on 33 objects; the composition graph is the line digraph L(Q), |E| = Σ_v in(v)·out(v) = 27,027**

*a loop at every vertex*

Computed — T 4.2 (App. G); Gabriel 1972.

> **Prior art: a quiver is a directed graph whose paths generate an algebra — Gabriel, Unzerlegbare Darstellungen I, Manuscripta Math. 6 (1972) 71-103. The composable cells form the arcs of one.**

### The projection ladder

**redundancy under R rises with the number of INDEPENDENT coordinates; a DERIVED coordinate lowers it**

*a closed index X of dimension d*

Measured — R 1119-1122; Shannon 1948.

Λ PROJECTED onto its own first d coordinates, same constraints: d=8 gives 61% removable with exact recovery, d=7,6,5 give 30%, d=4 gives 5%, d=3 gives 0%. And adding the electron count Ne = Z-c+1 to the spectra index — a FUNCTION of two coordinates it already has — drops redundancy from 20% to 0% while doubling the envelopes and raising coupling 17% to 33%

> **Prior art: redundancy is the excess of a representation over its entropy. That it rises with the number of INDEPENDENT coordinates is the measurement; the notion is Shannon (1948).**

### The three-coordinate rule

**an index needs THREE coordinates before its languages can disagree**

*an index and two languages*

Proved — R 1175; Beeri, Fagin, Maier & Yannakakis 1983.

at d = 2 there is one coordinate pair, so pairwise consistency and the cell coincide and every language returns the same answer. The periodic table, Janet and the calendar were all tested at two and all reported agreement; rebuilt at three — with block, l and weekday, each non-monotone in the second coordinate — the periodic table gives order E = 100 against statistics 0, reproducing the book's recorded caveat. All three match the book at 2-D first: 36, 0 and 7

> **Prior art: pairwise consistency is a statement about PAIRS, so an object with one pair cannot make it. BFMY (1983) for the general local-to-global framework.**

### The transit profile

**the transit profile MI/H = 0.51, 0.93, 0.08, 0.13, 0.77 at Λ₉–Λ₁₃: reduced at 10, a label through 11 and 12, re-attaching at 13**

*Λ₁₂ built with the loose bound*

Computed — M §12.11; Shannon 1948.

> **Prior art: MI/H is the normalised mutual information, standard since Shannon (1948).**

### Space is what an index holds, time is what it composes

**an index has a time column exactly when its cells are moves: Λ₈ 976/0, Λ₉ 1,654/1,169, the companion's index 2,370/1,410, while the periodic table and the calendar have no second column and cannot have one**

*a transition cell has two ends so composability is askable; a state cell has one position and the question does not arise*

Computed — M §12.11.1.3; Mac Lane 1971.

> **Prior art: an index has a composition structure exactly when its cells are morphisms rather than objects — the distinction is the category axioms. Mac Lane (1971). CORRECTED 2026-08-11: this statement printed Λ₈ as 976/491. It is 976/0. The generated table in INDICES.md gives 0 with fraction 0.0000, indices.py says 'Λ₈ composes not at all — four source coordinates against three target', and the composable window states the reason as a dependency: 'Λ₈ target has 3 coordinates against 4', so tgt(a) = src(b) is not even askable at Λ₈ and Λ₉ is the FIRST composable level. The 491 was a hand-authored figure in an object graded COMPUTED, contradicting the computation it depends on.**

### The composable window

**Λ₉ is the first composable level and the last tree level**

*Λ₈ target has 3 coordinates against 4; Λ₁₀ has 10 nodes and 10 edges*

Computed — T 4.1 (App. G); Beeri, Fagin, Maier & Yannakakis 1983.

> **Prior art: that treeness and composability are different properties, and that an index can be the last of one and the first of the other, is the acyclicity/local-consistency distinction of BFMY, J. ACM 30 (1983) 479-513.**

### The periodic table as a coordinate

**composability is 22.71% within one element and 85.23% across the 118, while E is 28,503 without Z and 972,862 with it**

*composability wants the whole table and closure wants one atom; Λ closes because it has no Z*

Computed — M §12.11.1.6; Edlen 1964.

> **Prior art: that composability is far higher across elements than within one is the isoelectronic structure — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964).**

## M. The modular chain — 9 objects

### The presymplectic potential

**the presymplectic potential θ = δφ £_ℓφ η carries no transverse derivative, so Ω is block diagonal in y and {φ(u,y),φ(u′,y′)} = (1/4√q(y))sgn(u−u′)δ^{d−2}(y−y′)**

*u-independent transverse metric, i.e. Θ = 0; non-derivative interactions only*

Computed — T 10.4c (App. G), F1, F2; Wald & Zoupas 2000.

> **Prior art: the presymplectic potential and its ambiguities are Wald & Zoupas, General definition of conserved quantities in general relativity, Phys. Rev. D 61 (2000) 084027.**

### Half-sided modular inclusion on a non-expanding horizon

**Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂) for t ≤ 0, u₁ < u₂, WITH Ω cyclic and separating for BOTH M(u₁) and M(u₂)**

*N a non-expanding horizon with no Killing field, ω Hadamard*

Conditional — proved on one existence hypothesis, register 1507; what remains is a containment of classes. T 10.4d (App. G), F6.

The object is conditional (register 1507): it is proved on one existence hypothesis, in nine steps none of which uses a Killing field — P_λ ≥ 0 from the ANEC on achronal generators (register 1471); U(s) unitary by Stone; U(s) B U(s)† ⊆ B because the cut translates into itself, which is causal structure (register 1506); U(s)Ω = Ω from the hypothesis; C_λ = U(1) B U(1)†, the source's own equation; Ω cyclic for C_λ since C_λΩ = U(BΩ) with U unitary and BΩ dense (register 1501); separating since C_λ ⊆ B; hence the four Borchers conditions, hence half-sided modular inclusion by Borchers 1992 and Wiesbrock 1993. The hypothesis: a state annihilated by every smeared ANE operator and cyclic and separating for the exterior algebra. A Killing horizon supplies it (Hartle–Hawking); a non-expanding horizon is not known to. The isometry supplies a witness, not a step, and what remains open is a containment between two classes of spacetimes, not a parameter. The statement carries the standardness clause (register 1481): a half-sided modular inclusion is N ⊆ M with a vector Ω cyclic and separating for both, and σ_t(N) ⊆ N for t ≤ 0 (Lechner–Scotford, Def. 2.1), equivalent to the Borchers triple by Borchers 1992 and Wiesbrock 1993. The earlier statement gave only the inclusion clause. The omitted clause is the one Faulkner and Speranza assume rather than derive — arXiv:2405.00847 §3.1 assumes Ω cyclic for the smaller algebra — and Reeh–Schlieder does not supply it, since their Ω is a vacuum for the averaged null energy operators and, in their words, may not coincide with a global minimal-energy state. Araki and Zsidó, Rev. Math. Phys. 17 (2005) 491–543, extend Wiesbrock to weights and fill a gap in the 1993 proof. The geometric route is closed: Sorce 2024 shows a geometric modular flow needs a conformal Killing vector, and a non-expanding horizon has none; Chandrasekaran and Flanagan (arXiv:2601.07915) have the Killing case. The algebraic route is not blocked: the Borchers–Wiesbrock characterisation is by a one-parameter unitary group with positive generator and mentions no Killing field, and the commutator of the presymplectic potential is already an algebraic object. That route was attempted (registers 1018–1022). Its free half goes through — the commutator gives a positive generator per null generator, negative-to-positive spectral weight 5 × 10⁻⁵, so a standard pair exists per generator and block diagonality keeps them unmixed. The obstruction is in the corner edge modes, where Chandrasekaran and Flanagan show the null translation generator is necessarily two-sided. The proposal that Θ = 0 supplies the missing relative boost fails: θ_ab → a(y) θ_ab under ℓ → a(y) ℓ, so Θ = 0 is invariant under the rescaling and cannot fix its parameter. The paper's own route (§7.3) takes the boost from smoothness — local Rindler frames give χ = κ(u ∂_u − v ∂_v) with ∇_(μ χ_ν) = O(u, v), and its footnote 44 needs only a local boost Killing field — establishing the modular flow's geometric action to first order at any cut, and states that these cannot be patched together; this object needs finite u₁ < u₂. The reduction bottoms out at positivity of the null translation generator, which Hadamard does not imply: Hadamard is microlocal, a wavefront-set condition, while positivity is a global spectral one; a smooth deformation of the vacuum raises the negative-to-positive spectral weight from 4.8 × 10⁻⁵ to 2.6 × 10⁻³ while leaving the UV tail unchanged, and thermal states are Hadamard and carry both signs. Positivity is a selection criterion assumed by everyone who needs it — Chandrasekaran–Flanagan §8 and Dappiaggi–Moretti–Pinamonti both — and Kay–Wald 1991 obtain uniqueness only for states invariant under the Killing flow, the hypothesis this object drops. The hypothesis is not purely geometric (registers 1038–1042): the standard non-expanding-horizon definition's third condition — the Einstein equations hold on Δ and −T^a_b ℓ^b is future causal — is an energy condition on the state, which by Raychaudhuri forces T_ab ℓ^a ℓ^b = 0 and σ_ab = 0, hence £_ℓ q_ab = 0, the hypothesis of the presymplectic potential; so that object assumes a consequence of the definition. The shortfall is one of order: the condition fixes the background, while half-sidedness is spectral on the perturbations.

### Borchers 1992 / Wiesbrock 1993

**half-sided modular inclusion is CHARACTERISED by a one-parameter unitary group with positive generator**

*common cyclic separating vector; extended to weights by Araki–Zsidó 2004*

Cited — T E2, E3; Borchers 1992; Wiesbrock 1993.

> **Prior art: half-sided modular inclusion and its characterisation by a one-parameter group with positive generator — Borchers, The CPT theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Lett. Math. Phys. 28 (1993) 107-114.**

### The modular ledger

**d − 1 = 1 + (d − 2) ON THE FREE ALGEBRA: one HSMI per generator supplies the affine line; the transverse direct integral is C1 and no HSMI supplies it. INCOMPLETE ON THE DRESSED ALGEBRA, which carries doubled corner modes besides**

*a null hypersurface in d dimensions — THIS IS A MANIFOLD COUNT, NOT AN ALGEBRA COUNT (R 1484)*

Computed — T 10.4e (App. G), F7; Borchers 1992; Wiesbrock 1993.

COMPLETED 2026-08-11 (R 1484): the sum is TWO accountings. LEVEL ONE, the manifold, is what this object counts and it is correct. LEVEL TWO, the algebra, carries the corner content, and register 1020 writes it exactly: the residual freedom is l -> a(y) l, acting on the affine parameter as u -> u/a(y) + b(y). Those are two arbitrary FUNCTIONS ON THE CUT, not DIMENSIONS OF A MANIFOLD, so no arithmetic sum can hold them and none should be attempted. R 1022 named what would close M.C2 — a canonical scaling of the affine parameter — which is a(y). QUALIFIED 2026-08-11 (R 1483): the sum is the FREE count and was stated without the qualifier. Register 1019, which M.C2 own check already cites, records that half-sidedness fails on the DRESSED algebra and not the free one, and that Chandrasekaran and Flanagan recover it by EXTENDING THE PHASE SPACE WITH DOUBLED CORNER MODES — relative boosts AND null translations of the respective corners. Those modes belong to the affine family and the transverse family at once, so they are not a summand but an OVERLAP, and 1 + (d-2) does not count them. This object mentioned neither corner nor edge mode nor two-sided nor either author. dimensional_ledger — and the ledger IS the kinematic/stateful decomposition (R 1035): the STATEFUL object (HSMI, hence M.C2) supplies exactly ONE dimension, the affine line; the KINEMATIC one (M.C1, Theta = 0) supplies the other d-2. Read as a counting argument until then

> **Prior art: one half-sided modular inclusion per generator supplies the affine line — the Borchers-Wiesbrock theorem, Borchers, Commun. Math. Phys. 143 (1992) 315-332; Wiesbrock, Lett. Math. Phys. 28 (1993) 107-114.**

### Reeh–Schlieder

**the vacuum is cyclic and separating for local algebras**

*Hadamard state; region with nonempty causal complement*

Cited — T E0; Reeh & Schlieder 1961.

> **Prior art: the vacuum is cyclic and separating for local algebras — Reeh & Schlieder, Bemerkungen zur Unitaeraequivalenz von Lorentzinvarianten Feldern, Nuovo Cim. 22 (1961) 1051-1068.**

### Semifinite carries a trace

**a semifinite factor carries a trace, hence an entropy; type III carries none**

*von Neumann classification*

Cited — T E5; Murray & von Neumann 1936.

> **Prior art: the type classification of factors, and that only semifinite ones carry a trace, is Murray & von Neumann, On rings of operators, Ann. Math. 37 (1936) 116-229, and its sequels.**

### Sorce 2024

**any geometric modular flow must be generated by a conformal Killing field**

*general*

Cited — T 10.4 (App. G); Sorce 2024.

> **Prior art: that a geometric modular flow must be generated by a conformal Killing field — Sorce, Analyticity and unitarity for cosmological correlators (2024) and related work on geometric modular flow.**

### Takesaki duality 1973

**N = M ⋊_{σ^φ} ℝ is type II_∞ with trace τ, τ∘θ_s = e^{−s}τ, and M = N ⋊_θ ℝ uniquely**

*M type III, φ a faithful semifinite normal weight; STATED FOR ℝ*

Cited — T E4; Takesaki 1973.

> **Prior art: the structure theorem for type III factors as crossed products — Takesaki, Duality for crossed products and the structure of von Neumann algebras of type III, Acta Math. 131 (1973) 249-310.**

### Tomita–Takesaki

**for (M,Ω) there exist Δ, J with Δ^{it} M Δ^{−it} = M**

*M a von Neumann algebra, Ω cyclic and separating*

Cited — T E1; Tomita 1967; Takesaki 1970.

> **Prior art: Tomita-Takesaki modular theory — Tomita, Quasi-standard von Neumann algebras (1967, unpublished); Takesaki, Tomita Theory of Modular Hilbert Algebras and its Applications, Springer LNM 128 (1970).**

## W. The violation index — 9 objects

### The core at fifteen letters

**at fifteen letters: 18,072 cells, E = 816 = 1 × 816, core (X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)**

*the split alphabet of T §6.5 (App. G)*

Computed — T 7.1 (App. G); Chinneck & Dravnieks 1991.

> **Prior art: as the core at nine letters at a finer alphabet. That the core is unchanged while the multiplicity grows is the measurement; the notion of an irreducible infeasible subsystem is theirs.**

### The core at nine letters

**at nine letters: 2,370 cells, E = 30 = 1 × 30, core (X=0, U=0, NEC=3)**

*the coordinate set of T §5.1 (App. G)*

Computed — T 5.3 (App. G); Chinneck & Dravnieks 1991.

cell count RECOMPUTED: the 17 rules of vi_best.json applied to the 4·3·3·3·5·2·2·3·3 box give exactly 2,370. E=30 is the arity-4 CONSTRAINT-LANGUAGE defect (NEC≥3 -> IC v U v X), not the envelope defect of the cell set, which is 3,040 (R 1009)

> **Prior art: a minimal set of conditions whose joint failure is irreducible is a MINIMAL UNSATISFIABLE SUBSET — Chinneck & Dravnieks, Locating minimal infeasible constraint sets in linear programs, ORSA J. Comput. 3 (1991) 157-168; in SAT the same object is the MUS. The conditions themselves are physics: the null energy condition (Penrose 1965), ghost states (Pais & Uhlenbeck 1950) and the equations of motion.**

### The null surface is a face

**the companion's local null surface is a FACE of the 6-cube, not a parity class: 32 of 64 with every rung 2, and a parity class gives E = 32 where the printed E is 0**

*deducible from three printed numbers with no access to any cell; THETA = 0 at 16 and STAT = 0 at 8 nest Killing horizons inside non-expanding ones*

Computed — T §10.1 (App. G), §10.4; Coxeter 1948.

> **Prior art: a face of the n-cube is the set fixing some coordinates and freeing the rest — Coxeter, Regular Polytopes (1948), ch. VII. A parity class is not a face, which is what distinguishes them here.**

### The frontier metric — distance and status on the fifteen-letter alphabet

**d(c) = X_exp + U_ghost + |NEC_pt−3| + EOM + d_P; s(c) = 1{·}+1{·}+1{·}+1{·} + s_P**

*the fifteen-letter alphabet; d_P the L1 distance on the eleven free letters*

Definitional — T D7, D8; classical; Hamming 1950.

> **Prior art: a defect built as a sum of independent violation counts, with a support counted separately, is the standard form of a penalty function.**

> **Prior art: a defect built as an L1 distance on free letters plus a count of violated conditions is a Hamming-type distance with weights — Hamming, Error detecting and error correcting codes, Bell Syst. Tech. J. 29 (1950) 147-160.**

### Jurisdiction does not change the defect

**a jurisdicted forcing and an unjurisdicted disjunction give identical defects; arity ≥ 3 makes a defect possible, jurisdiction narrowness makes it small**

*the scope condition is a coordinate*

Computed — T 8.2 (App. G); Freuder 1978.

> **Prior art: that a constraint of arity 3 or more is not captured by binary projections is the k-consistency ladder — Freuder, Synthesizing constraint expressions, CACM 21 (1978) 958-966. Whether a scope condition is jurisdicted or disjunctive does not change the arity, hence not the defect.**

### The one-hot partition

**status is one bit per vocabulary and the partition forces one-hot: 35 of 40 terms weight 1, 2 weight 0, 3 weight 2**

*weight 2 = relation or unsplit conflation; weight 0 = ungrounded or constructible*

Computed — T 10.5 (App. G); classical; Shannon 1938.

partition RECOMPUTED: 35 + 2 + 3 = 40 terms, total weight 41 (R 1009)

> **Prior art: a partition of a set forces exactly one indicator to be set — the one-hot encoding. Elementary, and the measurement is that 35 of 41 statuses satisfy it.**

> **Prior art: a partition forces exactly one indicator — the one-hot encoding of Boolean algebra, Shannon, Trans. AIEE 57 (1938) 713-723. Weight 2 signals a relation or a conflation; weight 0 an ungrounded term.**

### Brunetti–Fredenhagen–Verch 2003

**a term that is a relation between two vocabularies cannot be a coordinate of either**

*the BFV partition A : Loc → Alg has four parts*

Computed — T 8.4 (App. G); Brunetti, Fredenhagen & Verch 2003.

> **Prior art: a term that is a relation between two vocabularies is a morphism, not an object — the locally covariant framework of Brunetti, Fredenhagen & Verch, The generally covariant locality principle, Commun. Math. Phys. 237 (2003) 31-68, makes the distinction precise.**

### The defect does not scale

**the defect does not scale: core = 1 at 4, 5, 7 and 9 coordinates; only the multiplicity moves (3,5,10,30)**

*projections of one index*

Computed — T 5.7 (App. G); Chinneck & Dravnieks 1991.

> **Prior art: that the core of an infeasible system is invariant under refining the encoding is the well-definedness of the MUS; only the multiplicity of witnesses changes.**

### The core is minimal

**of 414 coordinate subsets excluding {X,U,NEC}, 0 fail: the triple is the unique minimal failing subset, arity exactly 3. THE COUNT RECONCILES — subsets of size 2..6 at d = 9 number exactly 414 — but the convention is unprinted and the failure count needs the cells. Arity 3**

*as the core at nine letters*

Computed — T 5.4 (App. G); Chinneck & Dravnieks 1991.

combinatorics RECOMPUTED: subsets of size 2..6 from 9 coordinates number 456; those containing all of {X,U,NEC} number 42; 456-42 = 414 exactly as stated (R 1009)

> **Prior art: testing all 414 subsets and finding none fails without the triple establishes MINIMALITY in their sense — no proper subset is infeasible.**

## EM. The electromagnetic quotient — 10 objects

### The selection-rule crossing

**EM-allowed cells compose at 11.6% within one element against the forbidden 40.7%, and the order reverses across the table at 89.7% against 77.9%**

*the rule that forbids composition inside an atom is the rule that enables it between atoms; parity repeats it at 38.4% against 20.1%*

Computed — M §12.11.1.7; Laporte 1924.

> **Prior art: the composability contrast between allowed and forbidden cells is a consequence of the parity rule; the measurement is the fraction.**

### The complete rectangle

**Λ₉'s image on (multipole, ΔS) is the COMPLETE rectangle at every cap; E = 0 vacuously**

*as electric/magnetic multipole selection rules (§12.11.8)*

Computed — M §12.11.8; Wigner 1927.

> **Prior art: that the selection rules cut a complete rectangle in (multipole, Delta S) is the product structure of the space-spin decomposition. Wigner, Z. Phys. 43 (1927) 624.**

### Electric/magnetic multipole selection rules

**the multipole is determined by |Δl| and parity alone: 0->M1, 1->E1, 2->E2, 3->E3**

*one-electron jump; no source J exists in Λ*

Computed — M §12.11.8; Laporte 1924; Condon & Shortley 1935.

> **Prior art: the multipole order of a transition is fixed by |Delta l| and parity — Laporte, Z. Phys. 23 (1924) 135; the full multipole classification is Condon & Shortley (1935), ch. IV.**

### Selection and composition are unrelated

**composability and the EM condition share 0.0004 bits of a possible 0.633**

*on Λ₉'s cells*

Computed — M §12.11.8; Shannon 1948.

> **Prior art: shared information between two binary properties, in bits. Shannon (1948).**

### The parity hole

**|Δl| = 1 is delta^-1({-1,+1}), a hole at zero, not convex; E = 750**

*as the spin diagonal (§12.11.8)*

Computed — M §12.11.8; Laporte 1924; Wigner 1927.

> **Prior art: the parity selection rule |Delta l| = 1 for electric dipole radiation is Laporte, Z. Phys. 23 (1924) 135, and its group-theoretic ground is Wigner, Z. Phys. 43 (1927) 624.**

### The electromagnetic quotient

**the EM index is a QUOTIENT of Λ, not an extension: adjoining its coordinates gives E = 3,900**

*every EM coordinate is a function of Λ's own*

Computed — M §12.11.8; Noether 1918.

> **Prior art: a selection rule is a quotient by a symmetry, not an extension of the state space. Noether, Invariante Variationsprobleme, Nachr. Ges. Wiss. Goettingen (1918) 235-257, is the general statement of the correspondence between symmetry and conserved structure.**

### The spin diagonal

**ΔS = 0 is a diagonal, hence two monotone one-parent bounds; imposing it preserves E = 0 at four cap settings**

*LS coupling*

Computed — M §12.11.8; Russell & Saunders 1925; Wigner 1931.

> **Prior art: Delta S = 0 for electric dipole transitions in LS coupling is the spin selection rule — Russell & Saunders, Astrophys. J. 61 (1925) 38; Wigner, Gruppentheorie (1931), for the representation-theoretic statement.**
### The multipole is fixed by the orbital jump and the parity

**The multipole of a transition is fixed by two quantities Λ carries — the change in orbital angular momentum and the parity of the jump. The rule assigns the lowest multipole whose parity matches: Δℓ = 0 gives M1, Δℓ = 1 gives E1, Δℓ = 2 gives E2, Δℓ = 3 gives E3. It is a one-electron jump read off the source and target subshells, and it assigns no multipole when |Δℓ| exceeds 3. The change in total J is not available: Λ builds J on the target side only and carries no source J, so the |ΔJ| ≤ multipole-order part of the electric-dipole rule, which needs both endpoints' J, cannot be expressed. The map states the part the coordinates support. It was validated against nine textbook classifications and shown able to refuse. On the base index only M1 and E1 occur, 814 and 840 cells, because the caps hold |Δℓ| ≤ 1; E2, E3 and the refusal appear at wider caps.**

*the multipole assignment Δℓ → {0: M1, 1: E1, 2: E2, 3: E3}, lowest matching parity, read from Δℓ = f − ℓ on Λ₉; on the base build only M1 (814) and E1 (840) occur, E2/E3 and the |Δℓ| > 3 refusal exercised at wider caps; the nine-classification validation carried from the record, at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Computed — M §12.11.8, §4.6; Laporte 1924; Condon & Shortley 1935.

> **Prior art: the multipole order of a radiative transition is fixed by the change in orbital angular momentum and the parity — Laporte, Z. Phys. 23 (1924) 135; the full classification is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. IV. That Λ fixes the multipole from Δℓ and parity alone, |ΔJ| being inexpressible for want of a source J, is this book's reading of the rule.**

### Intercombination lines: the index admits what LS coupling forbids

**576 of Λ₉'s cells are E1 transitions with ΔS ≠ 0. In LS coupling these are forbidden: when spin and orbital angular momentum couple separately, the spin state is conserved in an electric-dipole transition, so ΔS = 0 is a strict rule and a line changing the total spin — an intercombination line — cannot occur. The rule is not exact in nature. Spin-orbit interaction mixes states of different S, and the mixing grows with nuclear charge, so intercombination lines appear and strengthen down a group; in heavy atoms they are ordinary. The index admits all 576 because it is built in jK coupling, not LS. A jK-built index couples each electron's orbital and spin before combining, so S is not a good quantum number of the scheme and ΔS = 0 is not one of its rules; the spin rule is available only where LS coupling holds, and imposing it on Λ₉ keeps 526 cells at E = 0 (the spin diagonal). Whether the 576 lines are forbidden or allowed is therefore a property of the coupling scheme, not of the atom: LS forbids them, jK does not, and the same transitions are present or absent according to which scheme names them.**

*576 cells of Λ₉ are E1 (|Δℓ| = 1) with ΔS = 2S′ − 2S ≠ 0, verified on the rebuilt Λ₉; the spin rule ΔS = 0 keeps 526 cells at E = 0 (verified); the LS spin-selection rule and its spin-orbit breakdown, and the jK-vs-LS distinction, from the record, at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Computed — M §12.11.8; Russell & Saunders 1925; Condon & Shortley 1935.

> **Prior art: the spin selection rule ΔS = 0 for electric-dipole transitions in LS coupling is Russell & Saunders, Astrophys. J. 61 (1925) 38, and its breakdown by spin-orbit mixing, growing with nuclear charge, is standard — Condon & Shortley, The Theory of Atomic Spectra (1935). That Λ₉ admits 576 intercombination lines because it is built in jK coupling, where ΔS = 0 is not a rule, so that the same transitions are forbidden or allowed according to the scheme, is this book's reading.**

### The four coupling schemes as physical recoupling chains

**A coupling scheme is an order in which the four angular momenta of a two-electron configuration — the two orbital momenta and the two spins — are added. Four orders are standard. In jK the inner electron's orbital and spin couple first to j₁, then the outer orbital joins to give K, then the outer spin gives J: ℓ₁ + s₁ = j₁, j₁ + ℓ₂ = K, K + s₂ = J. In LK the two orbital momenta couple to L, then the core spin joins to give K, then the outer spin gives J. In LS the two orbital momenta couple to L and the two spins to S, and L and S give J. In jj each electron's orbital and spin couple to a j, and the two j's give J. The schemes are physical, not notational: each applies where its couplings are the strong ones. LS holds when the electrostatic term dominates and spin-orbit is weak; jj when spin-orbit dominates; jK when the outer electron is loosely bound and its own spin-orbit coupling is the weakest interaction present, coupled last. That is why jK is the scheme high Rydberg states realise — the weak coupling goes last, and for a distant outer electron the weakest coupling is its spin to the rest. jK carries a further advantage in this index: because the outer electron's spin is ½, the final triangle K + s₂ = J degenerates to |2J − 2K| ≤ 1, a mutual bound that closes, so jK reaches an exact bound where the others do not. Cowan and Andrew treat exactly these four as the pure coupling types for two-electron configurations. All four are changes of basis among the same states: because the atomic Hamiltonian is rotationally invariant, total angular momentum is conserved and the coupled states are eigenstates of J² and J_z, their energy independent of the orientation quantum number M. By the Wigner-Eckart theorem every transition matrix element between such states factors into a geometric part fixed by rotational symmetry and a reduced part carrying the physics, the reduced part independent of orientation — the algebra the schemes already use.**

*the four recoupling chains — jK (ℓ₁+s₁=j₁, j₁+ℓ₂=K, K+s₂=J), LK, LS, jj — with the physical regime each applies in and the ½-spin degeneracy giving jK its exact final bound |2J − 2K| ≤ 1; the chain definitions from NIST and the four-scheme precedent from the record; rotational invariance of the Hamiltonian giving conservation of J, the M-independence of energy, and the Wigner-Eckart factorisation are standard results cited below; at the caps of §7.4, (n, e, ℓ, k, f) = (3, 3, 1, 3, 1).*

Computed — M §12.11.8; Eckart 1930; Wigner 1931; Racah 1942; Cowan & Andrew 1965.

> **Prior art: the recoupling algebra by which a coupling scheme is a change of basis is Racah, Phys. Rev. 62 (1942) 438, and the four schemes jK, LK, LS, jj are the pure coupling types for a two-electron configuration — Cowan & Andrew, J. Opt. Soc. Am. 55 (1965) 502. That jK is the scheme high Rydberg states realise, the weak coupling going last, and that its outer ½-spin degenerates the final triangle to |2J − 2K| ≤ 1, an exact bound, is this book's reading. That a coupling scheme is a change of basis among eigenstates of a rotationally invariant Hamiltonian, with transition matrix elements factoring by rotational symmetry into an orientation-independent reduced part and a geometric part, is the Wigner-Eckart theorem — Eckart, Rev. Mod. Phys. 2 (1930) 305, and Wigner, Gruppentheorie (1931); standard textbook treatment in Sakurai, Modern Quantum Mechanics.**


## C. Protocol and audit objects — 9 objects

### The first factor

**A_q(z) = Σ_{n=1}^{3} zⁿ Σ_{ℓ=0}^{min(n−1,1)} z^ℓ Σ_{k=max(q,1)}^{min(4ℓ+2,3)} z^k (1−z^{min(k,3)+1})/(1−z)**

*caps as stated; q held fixed*

Computed — M §12.7 / T C2eq; Euler 1748; Stanley 1986.

> **Prior art: a nested sum over a constrained region, written as a polynomial in z, is the standard rank-generating construction. Euler (1748) for the method; Stanley, Enumerative Combinatorics Vol. 1 (1986), ch. 1, for the modern treatment.**

### The second factor

**B_q(z) = Σ_{e=1}^{3} z^e Σ_{f=0}^{min(e−1,1)} z^f (1−z^{min(q,4f+2)+1})/(1−z)**

*as C.Aq*

Computed — M §12.7 / T C3eq; Euler 1748; Stanley 1986.

> **Prior art: as C.Aq — the second factor of the fibred count, built the same way.**

### The box generating function

**Box(a,b)(z) = ∏_i z^{a_i}(1−z^{b_i−a_i+1})/(1−z)**

*every fibre bottoms out in a product of chains*

Definitional — M §12.7.2 / T C4eq; Euler 1748.

> **Prior art: the generating function of a box is a product of finite geometric series — Euler, Introductio in analysin infinitorum (1748), ch. XVI, where partition generating functions are introduced.**

### The comparison audit

**the COMPARISON AUDIT: index, math and language cypher checked against one another, not each against itself**

*any two indexes and the cypher*

Measured — R 1169-1172; Tarski 1936; Beeri, Fagin, Maier & Yannakakis 1983.

three checks. COVERAGE: every index coordinate has a math object and every family an index part — 0 and 0. LANGUAGE: five index/language pairs never run — Λ_spectra in geometry, algebra, information and statistics, Λ_alpha in analysis. CONTRADICTION: three standing, all on Λ_spectra between ORDER and ANALYSIS — delta falls with l (194/205 vs 102/205), triplet exceeds singlet (55/66 vs 33/66), delta falls along a sequence (89/143 vs 135/143). The audit names the pair and does NOT adjudicate

> **Prior art: comparing two formal readings of one object and requiring agreement is the metalanguage move (Tarski 1936); that global and local readings agree exactly on acyclic structures is BFMY (1983).**

### Every cut closes

**every two-sided cut of the tree gives defect zero, not only q**

*the tree is doing the work, not the transfer*

Computed — M §12.11.0.8; Freuder 1982.

> **Prior art: every two-sided cut of a tree separates it, so the defect vanishes at each — Freuder, J. ACM 29 (1982) 24-32.**

### The fibred count

**|Λ| = Σ_q |A(q)|·|B(q)| = 33·5 + 33·10 + 23·15 + 8·17 = 976**

*conditioned on the transfer q*

Computed — M §12.6.1 / T C1eq; Fubini 1907.

> **Prior art: summing a product over a fibration of the index set is the discrete Fubini theorem. That the fibres here are independent is what makes |Λ| factor as a sum of products.**

### Local closure is not implied

**E(Λ) = 0 and E(A_q) = E(B_q) = 0 for every q; the second does not follow from the first**

*cross-sections with induced coordinates*

Computed — M §12.8.5 / T C5eq; Rota 1964.

> **Prior art: that a global count factorises over a decomposition does not imply each part is separately closed — the failure of naive Moebius inversion over non-independent parts. Rota (1964).**

### The fibre trade

**|A(q)| falls 33,33,23,8 while |B(q)| rises 5,10,15,17; no q improves both**

*at stated caps*

Computed — M §12.8.1; Pareto 1896.

> **Prior art: no q improves both factors — a Pareto front in the two counts. Pareto, Cours d economie politique (1896).**

### The transfer distribution

**⟨q⟩ = 1.4631, sd 0.930; peak at q = 2 with 345 cells (35.3%)**

*at stated caps*

Computed — M §12.8.2; classical; Gauss 1809.

> **Prior art: the first and second moments of a distribution over a coordinate; elementary.**

> **Prior art: first and second moments of a distribution over a coordinate. Gauss, Theoria motus (1809).**

## I. The intake — interval maps and convexity — 3 objects

### The convexity criterion

**delta^-1(T) is a sublattice iff T intersect range(delta) is convex in range(delta)**

*as the interval map (§17.3)*

Proved — M §17.3; Birkhoff 1937.

> **Prior art: the preimage of a set under a lattice homomorphism is a sublattice iff the set is convex in the image — the standard sublattice criterion. Birkhoff, Lattice Theory (1940), ch. II.**

### The interval map

**delta = f - l is an INTERVAL MAP: min(da,db) ≤ delta(a v b), delta(a ^ b) ≤ max(da,db)**

*a sublattice of a product of chains*

Proved — M §17.3; Birkhoff 1940.

> **Prior art: a difference of two coordinates is an INTERVAL MAP on a distributive lattice — it need not be a homomorphism but it is bounded above and below by the coordinatewise extremes. Standard; Birkhoff, Lattice Theory (1940).**

### The shape of an interval

**between any two points there is an interval and the method returns its measure; three objects, one shape**

*cells, states under composition, measurements*

Computed — M §9.2; Birkhoff 1940; Monjardet 1981.

> **Prior art: between any two points of a lattice lies the interval [a and b, a or b]; the method returns its measure. Elementary lattice geometry.**

> **Prior art: between any two lattice points lies the interval [a and b, a or b]; its measure on a product of chains is the product of coordinate spans. Birkhoff, Lattice Theory (1940), ch. II; Monjardet, Discrete Math. 35 (1981) 173-184.**

## P. The spectral mechanisms — what moves a defect and by how much — 17 objects

### Constructed limit

**a limit can be built from two spectra and tested by convergence**

*a series converging on a state above its own ionisation threshold*

Measured — R 711, 712; Edlen 1964.

Ne I 2s.2p6.np on 173,929.75 + 217,047.598 gives +0.8408 +/- 0.0191 over ten

> **Prior art: constructing a limit by summing the ionisation energies of successive stages is standard spectroscopic practice. Edlen, Handbuch der Physik XXVII (1964).**

### The same-element ladder

**at s and p the quantum defect falls with charge at FIXED ELEMENT**

*a fixed element with two or more charge states*

Measured — R 963; Edlen 1964.

37 of 37 monotone at l≤1, no exceptions; all nine failures are at l≥2 where orbital collapse (register 719) governs

> **Prior art: the fall of the defect with ionisation stage along an isonuclear sequence is standard spectroscopy — Edlen, Atomic spectra, Handbuch der Physik XXVII (1964) 80-220.**

### Self-determined limit

**a Rydberg series measures its own ionisation limit**

*enough members that the fit is determined*

Measured — R 684, 685, 686, 698, 699; Rydberg 1890; Ritz 1903.

38 of 58 put the published limit within 3x the fit own error; only 15 of 58 within the PUBLISHED error (R 812-813)

> **Prior art: extrapolating a Rydberg series to its limit is the classical method of determining an ionisation energy — Rydberg (1890), Ritz (1903).**

### Parent-term independence

**delta depends on l and the core's charge, not on the core's STATE**

*two parent terms of one species*

Measured — R 709, 710, 743; Seaton 1958.

TWO instances; and CONTRADICTED IN PRINCIPLE by MQDT, which defines the defect as mu_(l,lambda,alpha+) depending on the core state (R 947)

> **Prior art: single-channel quantum defect theory treats the core as a fixed phase shift, so delta depends on l and the core charge only. Its failure for multi-channel cases is Seaton MQDT (Rep. Prog. Phys. 46, 1983).**

### Orbital collapse

**an orbital collapses at the onset of its shell and leaves the Rydberg series**

*3d across the transition row, 4f across the lanthanides*

Measured — R 719, 734, 735, 736; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969.

all ten exceptions to the isoelectronic ladder (register 708) are d and small; Ba III 4f gives 1.0 against neon's 0.006

> **Prior art: orbital collapse at the onset of a shell — Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187; Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71.**

### The isoelectronic ladder

**for one element and l, delta falls as the core charge rises**

*defect large enough to exceed its own scatter*

Measured — R 708, 716, 717, 718.

8 of 9 s/p ladders exact; and a form delta = a + b*ln(c+1)/c fits the Mg-like ns ladders to 2% of range and predicts out-of-sample, but FAILS on nd, nf and all He-like ladders (47-65%); the method is Edlen 1964 (R 942-945)

### The coupling-scheme marker

**J-inconsistency within one series marks where LS coupling has failed**

*same series, different J*

Measured — R 703; Condon & Shortley 1935.

114 of 129 consistent on raw levels, interval 82-93%; heavy elements fail at 23% against light at 8% (R 818-819)

> **Prior art: the transition from LS to jj coupling as the spin-orbit interaction grows with Z is Condon & Shortley, The Theory of Atomic Spectra (1935), ch. X.**

### The j-splitting

**delta splits by the outer electron's own j when there is something to couple to**

*an OPEN-SHELL core, or Z large enough for the electron's spin-orbit*

Measured — R 754, 756, 757, 758, 759; Sommerfeld 1916.

median 0.0454 over 19 open/heavy pairs against 0.0002 over 10 closed/light — 227x

> **Prior art: fine-structure splitting of a term by J is Sommerfeld, Zur Quantentheorie der Spektrallinien, Ann. Phys. 51 (1916) 1-94, in its relativistic form; Dirac (1928) supplies the exact theory.**

### The l-collapse

**delta falls monotonically with l and reaches zero by f**

*unperturbed series*

Measured — R 693, 702, 713, 724; Hartree 1928; Seaton 1958.

229 of 230 adjacent-l pairs correct, judged against EACH PAIR'S OWN 2 sigma rather than a fixed tolerance. The test carried an unstated slack of 0.02 until R 1072; at a fixed 0.02 it reads 251/251, strictly 242/251. The one failure is He I p->d, whose p defect is NEGATIVE — the Appendix B omission of R 871, which could not be recomputed when the reduced-mass Rydberg was corrected (R 1072-1074)

> **Prior art: the defect falls with l because the centrifugal barrier keeps the electron out of the core — the standard penetration argument, Hartree, Proc. Camb. Phil. Soc. 24 (1928) 89, and Seaton (1958).**

### The precision lens

**near the limit delta is measured through a lens worsening as n^3**

*delta depends on (limit - E), which shrinks as n^2 while level error does not*

Measured — R 749, 750, 751, 752; Rydberg 1890.

WEAK at scale: only 44 of 79 channels show a wider high half (56%), and the n^3 prediction of 4.2x is observed at 1.3x (R 827)

> **Prior art: near the limit dT/dnu ~ nu^-3, so a fixed energy uncertainty maps to a defect uncertainty growing as nu^3. Direct from the term formula.**

### The monotonicity of the defect

**the defect approaches delta_0 monotonically: PENETRATION series fall, POLARISATION series rise**

*steps resolvable against their own uncertainty*

Measured — R 806, 821-824; NIST Atomic Spectroscopy compendium; Ritz 1903.

penetration (|d|≥0.1) falls 146 of 163 = 90%; polarisation (|d|<0.01) RISES 52 of 52 = 100%; combined 94% against 66% as a single claim (R 985-987)

> **Prior art: the extended Ritz formula has a positive second coefficient for penetration and a negative one for polarisation, so the approach to delta_0 is monotone from above or below. Stated in NIST compendium.**

### Series perturbation

**a large spread measures a perturber, not bad data**

*a state of the same symmetry crossing the series*

Measured — R 696, 704, 741, 742; Fano 1961; Lu & Fano 1970.

Si I nd spreads 0.15-0.21 where ASD's own leading-percentage column names 3s3p3 at 14%

> **Prior art: a perturbed Rydberg series is a series crossed by a level of another channel — Fano, Effects of configuration interaction on intensities and phase shifts, Phys. Rev. 124 (1961) 1866-1878; Lu & Fano, Graphic analysis of perturbed Rydberg series, Phys. Rev. A 2 (1970) 81-86.**

### Core polarisation

**beyond l=3 the defect follows core POLARISABILITY in direction, not in magnitude**

*l ≥ 4, where the orbital does not reach the core*

Measured — R 731-733, 788, 792-795; Born & Heisenberg 1924; Seaton 1958.

grows with Z at +0.0005/unit over seven elements; a quantitative alpha_d fit was attempted and did NOT work, cause undiagnosed (R 794)

> **Prior art: core polarisation as the source of the high-l defect is Born & Heisenberg, Über den Einfluss der Deformierbarkeit der Ionen auf optische und chemische Konstanten, Z. Phys. 23 (1924) 388-410, and Mayer & Mayer, Phys. Rev. 43 (1933) 605.**

### Core penetration

**the quantum defect measures how far a Rydberg orbital reaches into the ionic core**

*a Rydberg series with three or more members, or two with a published limit*

Measured — R 693, 707, 713; Seaton 1958, 1983.

four independent confirmations, none encoded

> **Prior art: quantum defect theory — Seaton, The quantum defect method, MNRAS 118 (1958) 504-518, and Quantum defect theory, Rep. Prog. Phys. 46 (1983) 167-257.**

### Series self-consistency

**one series in disjoint n windows gives one defect**

*windows where the amplification of the precision lens (register 749) is comparable*

Measured — R 747, 748, 751; Ritz 1903.

67 of 72 channels agree between disjoint halves to better than 0.05 (R 811)

> **Prior art: one unperturbed series has one defect; disjoint n-windows must agree. The consistency test of the Ritz form (1903).**

### Core angular structure

**at l=3 delta splits by the core's TERM while its J-pairs stay together**

*j-K coupled series on one core*

Measured — R 739; Condon & Shortley 1935.

12 of 15 groups have terms separating by more than their J-pairs — median within 0.0011 vs between 0.0462 (R 826)

> **Prior art: the splitting of a Rydberg series by the core term, with J-pairs staying together, is the parent-term structure of Condon & Shortley (1935), ch. VII.**

### Truncation loss

**truncation removes most channels and degrades those it leaves**

*a series cut at low n*

Measured — R 675, 676, 677, 705, 706; Inglis & Teller 1939.

Ne I: 33 Handbook levels give 0 channels, the full table gives 4

> **Prior art: a Rydberg series is truncated in practice by field ionisation and by plasma microfields — Inglis & Teller, Ionic depression of series limits in one-electron spectra, Astrophys. J. 90 (1939) 439-448.**

## Q. The channel equation — the closed form and its terms — 11 objects

### The polarisability index

**Λ_alpha: the polarisability index over cores, coordinates Z . Ne(core) . n_out . l_out**

*the set of cores appearing in the spectra index*

Measured — R 1165; Born & Heisenberg 1924; Mayer & Mayer 1933.

18 cores held, E = 10. Sorted by (n_out, l_out) the isoelectronic ordering is a physical requirement — alpha must FALL with Z along a sequence — and the Ne-like and Mg-like rows obey it while the Ar-like row does not: K I 5.490 published, Ca II 6.665 extracted, Sc III 4.705. The index makes the violation visible where a table would not

> **Prior art: core dipole polarisability as the origin of the high-l defect is Born & Heisenberg, Z. Phys. 23 (1924) 388-410; the systematic values are Mayer & Mayer, The polarizabilities of ions from spectra, Phys. Rev. 43 (1933) 605-611.**

### The two-ended anchor

**anchoring the equation at BOTH ends of Z fixes the extrapolation at almost no in-region cost**

*the channel equation and a far-field literature value*

Measured — R 1201-1205; Theodosiou, Inokuti & Manson 1986.

seven far anchors — Cs I np measured at 3.5667, and Th/Ac ns, np, nd, nf from actinide theory at 5.2, 4.75, 3.8, 2.0 — extend the sample from Z ≤ 83 to Z = 90. Far-anchor median error falls 0.754 to 0.064, a factor of twelve; in-region rises 0.0637 to 0.0665. The saturating exponent returns for real: e(Ne) = 0.8297 - 0.0900 ln Ne against -0.0266 from the in-region sample alone. CAVEAT: four of the seven anchors are THEORETICAL, so the high-Z arm is calibrated against another calculation and moves if that is revised

> **Prior art: asymptotic quantum defects for all ionisation stages of all ions with Z ≤ 50 are tabulated in Theodosiou, Inokuti & Manson, At. Data Nucl. Data Tables 35 (1986) 473-486, Hartree-Slater. The far anchors used here are Cs I np (measured) and actinide values from arXiv:2508.06733.**

### The Pauli bound

**B = min( p , n0 - l - 1 ): the integer part's exceptionless upper bound, from aufbau alone**

*a channel and its core's ground configuration*

Proved — R 1141; Pauli 1925; Janet 1929.

floor(delta) ≤ B for 311 of 311 measured channels. As an equality it is right 57%; every error is negative; within two of the bound, 303 of 311. p is the core's orbital count at that l and n0 the first Pauli-allowed n, both from aufbau with no spectrum

> **Prior art: the bound counts core orbitals of the same l and the first Pauli-allowed principal number, both read from the ground configuration. Paulis exclusion principle, Z. Phys. 31 (1925) 765-783, fixes the occupancies; Janets n+l ordering (1929) fixes which subshells are filled.**

### The bridge equation

**the bridge between the metric and ordinal descriptions is MULTIPLICATIVE with a REGIME factor: every factor positive so each preserves rank by itself, and the regime factor differs between two channels only when they differ in regime**

*a channel equation required to respect both values and orderings*

Measured — R 1169-1171; Pareto 1896; Spearman 1904.

*Stated on the channel equation then current, the channel equation, first form (register 1145), which the channel equation, final form (register 1205) superseded at register 1205; the claim was re-tested there on the standing form and holds (one ℓ-ordering violation in 328 channels). The dependence line keeps the channel equation, first form because the channel equation, final form descends from this object, and the graph records the order of establishment, not present support (register 1750).*

an additive fit gets the l-collapse (register 693) 102/205 against a measured 194 — chance. A purely multiplicative fit gets 205/205, 143/143, 66/66 where the measurements give 194, 89, 55 — it cannot represent an exception because a product of positives is monotone in each factor. With a regime factor: 204/205, 129/143, 61/66, and ln-R^2 improves 0.8026 to 0.8164

> **Prior art: that a multiplicative form preserves rank and an additive one does not is elementary; that no single form does both well is a Pareto statement about the two objectives.**

> **Prior art: a product of positive factors is monotone in each and so preserves rank; a sum of signed terms need not. Rank preservation as an objective distinct from least squares is Spearman, The proof and measurement of association between two things, Amer. J. Psychol. 15 (1904) 72-101. That no single form does both well is a Pareto statement (1896).**

### The Janet collapse

**the ORBITAL COLLAPSE threshold is a Janet block boundary, exactly**

*a channel with p = 0 at l ≥ 2*

Measured — R 1187-1190; Goeppert-Mayer 1941; Griffin, Andrew & Cowan 1969.

the n+l = 5 block opens at Z = 21 and 3d collapses at 21; n+l = 7 opens at 57 and 4f at 57; n+l = 8 opens at 89 and 5f at 89. Three exact matches. Across 116 p = 0 channels at l = 2 or 3: collapsed median 0.637, uncollapsed 0.036, U-test p = 9.8e-4. Adding the term takes Ti IV nd from -0.620 to -0.056 and the overall rms from 0.1825 to 0.1411. The largest outliers are atoms APPROACHING a boundary — Ca I nd = 0.908 at Z = 20 against a threshold of 21, Ba II nf = 0.756 at 56 against 57 — so the collapse is a rapid transition, not a step

> **Prior art: orbital collapse — the sudden contraction of the 3d and 4f wavefunctions as Z crosses a threshold — is Goeppert-Mayer, Rare-earth and transuranic elements, Phys. Rev. 60 (1941) 184-187, and Griffin, Andrew & Cowan, Theoretical calculations of the d-, f- and g-electron transition series, Phys. Rev. 177 (1969) 62-71. What is measured here is that the threshold coincides with the Janet block boundary at Z = 21, 57 and 89.**

### The channel equation, first form

**delta = [ B - q e^(-a(Ne)l) e^(k/Ne) c^g + P ] (1 + s [triplet]): a closed form for any Rydberg channel from atomic-index quantities alone**

*a Rydberg channel (Z, charge c, l, multiplicity)*

Measured — R 1145-1168; Seaton 1958; Fermi 1928; Pauli 1925.

311 measured channels: rms 0.2449, R^2 0.924, median |error| 0.090. By l: s 0.283, p 0.276, d 0.280, f 0.119, g 0.0096. Against TWELVE published values never fitted on: median error 0.00155 at l ≥ 3 and 0.368 below. 50% within 0.090, 90% within 0.414, 99% within 0.826

> **Prior art: the superseded form of the channel equation. Its terms are the Pauli bound (Pauli 1925), the Thomas-Fermi deficit (Fermi 1928) and Seaton polarisation (1958). Superseded by the channel equation, final form (register 1205) at register 1205.**

### The exchange factor

**the exchange factor (1 + s [triplet]), s = -0.0782**

*a channel of a two-valence-electron system*

Asserted — R 987, withdrawn R 1168.

WITHDRAWN (R 1168). The claim was that the fitted s recovers register 987's sign and size. It does not: register 987 measures the triplet defect EXCEEDING the singlet in 22 of 22 ns cases, and the additive fit returned s = -0.0782, the right magnitude and the WRONG SIGN. Cross-checked on 66 singlet/triplet pairs the equation gets 33, exactly chance. The parameter absorbed something else

> **Prior art: the exchange splitting between singlet and triplet is Heisenberg, Mehrkoerperproblem und Resonanz in der Quantenmechanik, Z. Phys. 38 (1926) 411-426; that the higher multiplicity lies lower is Hund first rule (1925). WITHDRAWN at register 1168: the fitted sign is opposite to the measured one.**

### The channel equation, final form

**delta = a p^e(Ne) Ne^k ln(c+1)/c where p > 0, and h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c where p = 0**

*any Rydberg channel (Z, charge, l, multiplicity)*

Measured — R 1205-1206; Seaton 1958; Fermi 1928; Janet 1929.

a = 0.3772, e(Ne) = 0.8297 - 0.0900 ln Ne, k = 0.4942, h = 0.5415. 284 channels from Z = 2 to 90 and charge 1 to 10: rms 0.1610, R^2 0.9741, l ≥ 4 rms 0.0150, hydrogenic output EXACTLY zero, Pauli bound 328/328, one l-ordering violation against a measured zero. Four fitted numbers and every input from the ground state or the periodic table. It values all 1,648 cells R places, where the walk valued none

> **Prior art: every term of the form has a source. The ln(c+1)/c charge dependence is the isoelectronic behaviour of Edlen 1964; the Ne^k factor is Thomas-Fermi (Fermi 1928); p is the Pauli orbital count (Pauli 1925); C(Z) is orbital collapse (Griffin, Andrew & Cowan 1969) at the Janet boundary (Janet 1929). The equation assembles them; it does not introduce any.**

### The deficit term

**the penetration deficit, -q e^(-a(Ne) l) e^(k/Ne) c^g, with a(Ne) = a0 + a1 Ne^(-1/3)**

*a channel below the polarisation regime*

Computed — R 1147; Hartree 1928; Fermi 1928.

the decay a is set by the atom's SIZE: a against ln Ne gives r^2 = 0.437 across 56 species, against electrons-beyond-closure 0.143, against charge nothing (p = 0.34). K I's measured d/s ratio implies a = 1.03, Sr I's implies 0.157 — a factor of seven, and a universal a fits neither

> **Prior art: the penetration deficit and its Ne^(1/3) scaling are the Thomas-Fermi picture — Fermi, Eine statistische Methode zur Bestimmung einiger Eigenschaften des Atoms, Z. Phys. 48 (1928) 73-79; Hartrees self-consistent field, Proc. Camb. Phil. Soc. 24 (1928) 89-110, gives the orbital form. Fermi 1928 applied it to Rydberg corrections directly.**

### Seaton's term

**the polarisation term, 3 alpha c^2 / K(l) for l ≥ 4 with alpha from Λ_alpha, K(l) = l(l+1)(2l-1)(2l+1)(2l+3)**

*a non-penetrating channel and a core polarisability*

Cited — R 1165-1168; Seaton 1958; Born & Heisenberg 1924.

Seaton's formula. With alpha supplied as a species LABEL from Λ_alpha rather than a universal constant, the l ≥ 4 rms falls from 0.01504 to 0.00958 — 36%. Below l = 4 it must be gated OFF: applied at s and p it drives the fit to rms 39.3 because K(l) is small there

> **Prior art: the polarisation term 3 alpha c^2 / K(l) is Seaton (1958); the physical origin is core polarisability, Born & Heisenberg, Z. Phys. 23 (1924) 388-410. SUBSUMED at register 1204 by the Janet collapse coordinate.**

### The validated domain

**the equation is VALIDATED in the verified-plus-possible region and EXTRAPOLATED outside it**

*the channel equation and the existence partition*

Measured — R 1193-1194; Theodosiou, Inokuti & Manson 1986.

*Stated on the channel equation then current, the channel equation, first form (register 1145), which the channel equation, final form (register 1205) superseded at register 1205; the claim was re-tested there on the standing form and holds (in-region error 0.147, far-anchor 0.064). The dependence line keeps the channel equation, first form because the channel equation, final form descends from this object, and the graph records the order of establishment, not present support (register 1750).*

277 in-region channels give rms 0.1329 and R^2 0.9747 — better than the 311-channel fit on fewer points, because the 51 excluded were 24 three-parent cores, 15 sixteen-parent cores and 12 ions above charge 10. And the saturating exponent falls from 1.3257 - 0.2751 ln Ne to 0.5828 - 0.0266 ln Ne: nine-tenths of the Ne-dependence was open-shell contamination. Validated on 277, extrapolated to 98,078

> **Prior art: the distinction between where a defect is measurable and where it is calculated is exactly the distinction their 1986 table makes — they compute Hartree-Slater values everywhere and note where experiment exists.**

---

## LS. The Löwdin solution — the order derived from the equation — 8 objects

*Chapter 35 and its companion paper; register 1701–1712. These objects are verified by the solution's own sealed instruments and receipts, not yet by `mathverify.py`; wiring them into the book's verifier is a build task, and until it is done this page states the verification that exists rather than implying one that does not. The mathematics of the challenge (Chapter 34, registers 1249–1357) is stated separately below under THE MATHEMATICS OF THE LÖWDIN WORK.*

### The entrant operator

**ent(Z) = argmax over frontier (n,ℓ) of |D(n,ℓ)|, D the converged one-channel depth in the self-consistent field of the ion (Z, cfg(Z−1)); scalar-relativistic Koelling–Harmon; c = 137.035999 the only entered number. Chained, cfg(Z) = cfg(Z−1) + ent(Z): 107 of 107 against the measured ground configurations, Z = 2–108**

*the operator Chapter 27 said a non-closing index requires; sign-exact by construction, and the margin |D(ent)| − |D(runner-up)| is its own error bar, recorded at every step*

Computed — M §35; register 1701, 1702.

### The ordering law, five clauses

**Clause 1 (ordering): smaller n+ℓ opens first — 107/107. Clause 2 (tie-break): equal n+ℓ, smaller n first — exceptions exactly {La, Ac, Th}, derived by the collapse condition (§35). Clause 3 (correlation): at the five contested rows the second-order differential is positive — every competition widens. Domain clause: Z ≤ 112; spin-orbit worst case 0.083 Ha under every margin. Relativistic clause: the c → ∞ twin disagrees at eleven elements**

*statement and proof form in the companion paper*

Proved — M §35; register 1701–1706.

### The collapse condition

**The double-well criterion, stated from the field, for which f channel is collapsed at which Z: decides exactly the Clause-2 exception set and occupies exactly the domain where Chapter 34's corridor is silent (L = −∞ at f openings)**

*adjacent to the transition the mean-field equations admit two stationary solutions of one configuration with distinct converged operators; a sign at SCF tolerance there is branch content, not noise*

Computed — M §35; register 1703; Griffin–Andrew–Cowan 1969, 1971.

> **Prior art: the orbital-collapse double well is Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62; the placement of it against the corridor's silence is this work's.**

### The pinned-channel theorem (no g block)

**Every g channel offered by the walk sits at −1/(2n²) to storage precision: 5g over 65 elements, 6g over 70, 7g over 57, 8g over 28. dn*/dZ = 0 across a hundred protons**

*the absence of collapse, not its slow approach; a relation the data cannot violate is defending something — here, the nonexistence of a g period below Z = 121*

Measured — M §35; register 1704.

### The state-dependent multiplier identity

**For u, v eigenstates of different self-consistent operators, the two eigen-relation evaluations of ⟨u|T|v⟩ differ by exactly asym(u,v) = (ε_v − ε_u)⟨u|v⟩ − ⟨u|(V_v − V_u)|v⟩ + [⟨u|X_v⟩ − ⟨v|X_u⟩]; verified to machine precision, four of four elements, worst 2.6·10⁻¹⁵, independent of SCF tolerance**

*a residual of large cancelling terms, not a convergence artefact; it reclassified a registered instrument fault as derived content*

Proved — M §35; register 1708, 1709; Löwdin 1950.

> **Prior art: an instance of the non-orthogonality problem, Löwdin, J. Chem. Phys. 18 (1950) 365.**

### The exact-quartic decomposition

**The energy functional with one shell's orbital varying along a fixed direction is exactly quartic in the path parameter (one-body quadratic; two-body quartic); five evaluations at t ∈ {0, ±½, ±1} determine every Taylor coefficient with zero truncation error**

*the floating-point floor at |E| ~ 10⁴ Ha (~10⁻¹²) is the only limit, and it is stated, not implied; protocol*

Proved — M §35;.

### The defect closed: chord = rot + perp

**The walk's one systematic internal discrepancy — the Hellmann–Feynman-in-q defect — is a Pulay term of the occupation parameter. In the one-shell-frozen gauge it splits exactly: rot = linear gradient law + (q·s/dq2)·⟨asym⟩ + endpoint-Hessian term; perp = the first-order perturbed-HF response on the orthogonal complement. Balance: zero unexplained residue**

*the signed trace verified at ratios 0.999992 and 1.000103; the endpoint-Hessian term (+1.7·10⁻⁷, +6.1·10⁻⁹) is twenty to five hundred times too small for the residual it was hypothesised to explain — a hypothesis falsified by the clause that scored HIT, and kept*

Proved — M §35; register 1707, 1709, 1711; Pulay 1969; Gerratt–Mills 1968.

> **Prior art: the occupation-parameter term is Pulay, Mol. Phys. 17 (1969) 197; the orthogonal-complement response is Gerratt & Mills, J. Chem. Phys. 49 (1968) 1719.**

### The twin operator, c → ∞

**The identical entrant operator with the constant removed disagrees with the c = 137.035999 operator at eleven elements — Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, Rf — every disagreement an error against nature, since the relativistic operator scores 107/107**

*the relativistic clause of the ordering law, five clauses (§35), measured rather than asserted*

Measured — M §35; register 1706.

## 3B. Three bodies — the index of families — 9 objects

*Chapter 36 and its companion paper; register 1713–1724. One new root, shape space and the shape sphere — shape space, standard mathematics cited as found (Montgomery 2014; Hopf 1931; register 1739) — and otherwise the family derives from node counting, ℓ ≤ n − 1 (§7.1)–the occupancy floor (§10.2), monotone interpolation bracket (§20.1) and the operators, and the seed did not move — the cycle's falsifier passing on a new subject.*

### Shape space and the shape sphere

**ℝ³ = ℂ³ / (translations × rotations); S² = that / scale. Onto; identifies exactly the oriented-congruent triangles; only triple collision maps to 0; w₃ = signed area up to a mass constant; ‖w‖ = I/2**

*the coordinates in which three bodies become one point*

Proved — Montgomery 2014, Thm 1; Hopf 1931.

### The shape metric

**ds² = |dw|²/(2√‖w‖); every plane through 0 totally geodesic; cone metric dr² + ¼r²dθ²**

*as shape space and the shape sphere*

Proved — Montgomery 2014, Thm 3.

### The Jacobi–Maupertuis metric

**g_E = (E+U)·ds²; trajectories at energy E are its geodesics; dt = ds_E/√(2(E+U))**

*licence in the index: §12.11.1.3, §12.11.0.2*

Proved — Maupertuis 1744; Jacobi 1837.

### The potential on shape space

**U(w) = Σ c_ij/d_ij, c_ij = (m_i m_j)^{3/2}/√(m_i+m_j), d_ij² = ‖w‖ − w·b_ij; identity r_ij² = d_ij²/μ_ij. No hyper-radius factor**

*650 triangles, 13 mass cases, error < 10⁻¹⁰; the first audit's uniform 13/13 failure was a hyper-radius divisor inherited from working material — register 1718, protocol 1722*

Proved — Montgomery 2014 §11; register 1718; main §D.5.9.

### The algebraic variety

**With u_ij = c_ij/d_ij, p = Σu², q = Σu_i²u_j², r = ∏u²: U⁸ − 4pU⁶ + (6p²−8q)U⁴ − 4(p³−4pq+16r)U² + (p²−4q)² = 0; constant term ∏(u₁±u₂±u₃)²**

*proved symbolically (sympy) and measured at 13 mass cases; an inherited form with U⁴ coefficient "6S₂²−4S₄+8S₁₁" = 2p²+16q was wrong and is withdrawn — register 1719*

Proved — Lagrange 1770; register 1719, 1720.

> **Prior art: N₈ is the norm over (ℤ/2)³ — Lagrange's resolvent method, 1770. Not new mathematics.**

### The five fixed points

**Three Euler roots (one positive root of the quintic per ordering) and two Lagrange points, for every mass triple — 13/13**

*seed of the family index in §14.5's sense*

Proved — Euler 1767; Lagrange 1772; register 1717; main §D.5.9.

### The triangle form on K₃

**{|a−b| ≤ c ≤ a+b}: join-closed, meet-broken. Cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 meet failures 12·111·477·1,488·3,780·8,385·16,812·31,227·54,555·90,705; two-body chain 0 throughout**

*confirms §12.11.2 on a grid the book never ran*

![Closure defect against cap](figures/fig2_closure_defect.png)

*meet and join failures against cap; the two-body chain at zero throughout*

Measured — M §36; register 1716.

### The deficit

**K₃ has treewidth 2; strong 3-consistency is required; ℛ reaches 2 (§32.3). Shortfall exactly one level**

*the separation hypothesis of §7.1 broken by the smallest graph that can break it*

![K₂ against K₃](figures/fig5_constraint_graphs.png)

*K₂ against K₃, and the consistency level each requires*

Proved — M §21.5.1; Freuder 1982.

### The index Λ₃

**Λ₃ = {KAM, per, chaos, erg, coll} on ℳ_{E,L}. E(Λ₃) = 0: exhaustive (Chazy classes), disjoint up to measure zero (Saari 1971/73; Painlevé, n = 3). By §25.6, predictions = 0 — Brudno's theorem on the chaotic stratum**

*cited theorems assembled; the assembly is this work's. The maximal forbidden case of Chapter 18 is the solved case, because what is forbidden is exactly what Poincaré excludes — register 1724*

Proved — M §36; register 1713, 1714, 1724; Chazy 1922; Saari 1971; Brudno 1983.

# V · THE CHAINS

The longest derivation paths in the register — what rests on what.

**depth 14** · projection onto coordinate i (§6.1) ← monotone upper envelope / staircase bound (§6.1) ← the recovery operator (§6.1) ← the projection ladder (register 1119) ← the axis test (register 1127) ← the production rule (register 1143) ← the ground-state derivation (register 1139) ← the channel curve (register 1150) ← the regime coordinate (register 1157) ← the polarisability index (register 1165) ← Seaton's term (register 1165) ← the channel equation, first form (register 1145) ← the validated domain (register 1193) ← the two-ended anchor (register 1201) ← the channel equation, final form (register 1205)

**depth 13** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form ← the validated domain ← the two-ended anchor

**depth 13** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form ← the bridge equation (register 1169) ← the three blindnesses (register 1169)

**depth 12** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form ← the bridge equation

**depth 12** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form ← the validated domain

**depth 11** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) (§14.2) ← Bergman double-projection; Baker–Pixley 1975 (majority term) (§14.1) ← the tightening rule (§14.4) ← sublattice of a product (§7.3) ← Birkhoff / product of chains (§8.1) ← the Birkhoff representation (§8.3) ← the Boolean representation (§11.1.1) ← the implication circuit (§11.1.1)

**depth 11** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) ← Bergman double-projection; Baker–Pixley 1975 (majority term) ← the tightening rule ← sublattice of a product ← Birkhoff / product of chains ← the Birkhoff representation ← join-prime and meet-prime (§16.8.5) ← the interval-removal step (§16.8.5)

**depth 11** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) ← Bergman double-projection; Baker–Pixley 1975 (majority term) ← the tightening rule ← sublattice of a product ← Birkhoff / product of chains ← the interval map (§17.3) ← the convexity criterion (§17.3) ← the spin diagonal (§12.11.8)

**depth 11** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) ← Bergman double-projection; Baker–Pixley 1975 (majority term) ← the tightening rule ← sublattice of a product ← Birkhoff / product of chains ← the interval map ← the convexity criterion ← the parity hole (§12.11.8)

**depth 11** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form

**depth 10** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) ← Bergman double-projection; Baker–Pixley 1975 (majority term) ← the tightening rule ← sublattice of a product ← Birkhoff / product of chains ← the Birkhoff representation ← the join-irreducible count

**depth 10** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← extensivity ← closure operator (Moore family) ← Bergman double-projection; Baker–Pixley 1975 (majority term) ← the tightening rule ← sublattice of a product ← Birkhoff / product of chains ← the Birkhoff representation ← Möbius function of a distributive lattice (§9.3)

**depth 17** · projection onto coordinate i ← monotone upper envelope / staircase bound ← the recovery operator ← the projection ladder ← the axis test ← the production rule ← the ground-state derivation ← the channel curve ← the regime coordinate ← the polarisability index ← Seaton's term ← the channel equation, first form ← the validated domain ← the two-ended anchor ← the channel equation, final form ← the entrant operator (§35) ← the state-dependent multiplier identity (§35) ← the defect closed: chord = rot + perp (§35) · *the Löwdin solution's longest path, through the channel equation; the walk's one defect closed at zero residue*

**depth 4** · node counting, ℓ ≤ n − 1 (§7.1) ← the constraint index (§21.5.2) ← the constraint graph (§21.5.3) ← the deficit (§21.5.1) ← the index Λ₃ (§36) · *the three-body index; the family's own links rest on node counting, ℓ ≤ n − 1–the occupancy floor (§10.2), the constraint graph and the constraint tree (§8.5), roots already in the register — closes to §25.6 and the Brudno rate*

---

# VI · WHAT IS UNFINISHED

*Neither the Löwdin solution nor the three-body work adds an open object; the two below are untouched by both.*

**Two objects.** *Neither is unfinished for want of a proof attempt. Each has a diagnosis, and the diagnosis names what is missing rather than restating that something is.*

## Half-sided modular inclusion on a non-expanding horizon

        Δ_{M(u₁)}^{it} M(u₂) Δ_{M(u₁)}^{−it} ⊆ M(u₂)   for t ≤ 0, u₁ < u₂

**What is settled.** Half-sided modular inclusion is CHARACTERISED — Borchers, *The CPT theorem in two-dimensional theories of local observables*, Commun. Math. Phys. **143** (1992) 315–332, and Wiesbrock, *Half-sided modular inclusions of von Neumann algebras*, Lett. Math. Phys. **28** (1993) 107–114: the inclusion holds exactly when a one-parameter unitary group with positive generator implements the translation. The vacuum is cyclic and separating for local algebras (Reeh & Schlieder 1961), and modular theory supplies Δ and J (Tomita 1967; Takesaki 1970). **None of that is in question.**

**What is missing, precisely.** The hypothesis — *a non-expanding horizon with no Killing field, ω Hadamard* — asks the expansion Θ = 0 to select what only a STATE can select, and offers Hadamard, a microlocal condition, as the selector.

> **The horizon's own definition supplies a state condition at BACKGROUND order — Einstein's equation with future-causality forces vanishing shear, vanishing null flux and £_ℓ q_ab = 0 — and leaves a gap at PERTURBATION order.** *That gap is the object.*

**Where the obstruction sits.** The free half is confirmed numerically: the spectral weight ratio is of order 10⁻⁵. The obstruction is in the corner edge modes, and the proposal Θ = 0 was refuted by the transformation law. Sorce (2024) closes the geometric route by construction — a geometric modular flow must be generated by a conformal Killing field — so a horizon with no Killing field cannot have one, and the route that remains is algebraic.

**What would settle it.** The covariance of conditional expectations across the full family of cuts, in the manner of an over-determined joint fit. *Chandrasekaran & Flanagan (arXiv:2601.07915) is the nearest published treatment and was read into the diagnosis at registers 1037–1042.*

## The exchange factor

        δ = [ … ] · (1 + s·[triplet]),   s = −0.0782

**What is settled.** Exchange splitting between singlet and triplet is Heisenberg, *Mehrkörperproblem und Resonanz in der Quantenmechanik*, Z. Phys. **38** (1926) 411–426; that the higher multiplicity lies lower is Hund's first rule, Z. Phys. **33** (1925) 345–371. **The physics is not in doubt.**

**What is missing, precisely.** *The fitted sign is opposite to the measured one.* The factor was withdrawn at register 1168 for that reason and the grade left as ASSERTED rather than removed, because the term is real and the form is wrong.

> **A uniform s cannot work.** *Exchange acts through the overlap of the Rydberg orbital with the core, and that overlap falls sharply with ℓ. A single multiplicative constant can only give 0 of 66 triplet-above-singlet pairs or 66 of 66; the measurement is neither.*

**What would settle it.** An ℓ-dependent exchange term, fitted against the singlet–triplet pairs the compendium holds. The Pauli bound (register 1141) already carries the orbital count p that the overlap should follow.

---

# VII · THE BIBLIOGRAPHY

**Every object of this compendium names a work.** What follows is those works, ordered by year, with the objects each carries. *The book claims nothing new where an earlier result will do; where a measurement is this work's, the object says so.*

**162 works, 1669–2026.** *Ten rows the generator had read out of callout text — status words, a possessive, a method name — were removed on 2026-08-24 (register 1736); the count was 172.*

| year | work | objects |
|---|---|---|
| 1669 | Newton | `B.newton` |
| 1682 | Leibniz | `B.brk` |
| 1687 | Newton | `B.ordbr` |
| 1715 | Taylor | `B.frac` `B.pole` |
| 1736 | Euler | `G.graph` |
| 1744 | Maupertuis | `3B.JM` |
| 1748 | Euler | `A.prodE` `C.Aq` `C.Bq` `C.box` `L.F` `L.F1` `L.Fm1` |
| 1767 | Euler | `3B.five` |
| 1770 | Lagrange | `3B.norm` |
| 1772 | Lagrange | `3B.five` |
| 1797 | Lagrange | `B.hstar` |
| 1809 | Gauss | `A.anchor` `B.adm` `C.qmean` `L.skew` |
| 1837 | Jacobi | `3B.JM` |
| 1842 | Jacobi | `3B.JM` |
| 1854 | Boole | `A.logic` |
| 1869 | Mendeleev | `E.ioniz` `E.table` |
| 1878 | Hill | `3B.index` |
| 1890 | Rydberg | `B.V43` `B.Vexact` `B.fail` `B.floor32` `B.nuV` `B.silence` `P.converge` `P.lens` |
| 1890 | Poincaré | `3B.index` |
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
| 1922 | Chazy | `3B.index` |
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
| 1931 | Wigner | `EM.spin` `T.a12` `T.dens` `T.excl` `T.invariant` |
| 1931 | Hopf | `3B.shape` |
| 1933 | Mayer & Mayer | `Q.alpha` |
| 1933 | Milne-Thomson | `B.V` `B.brk` `B.ordbr` `B.ordk` `B.pole` |
| 1935 | Condon & Shortley | `EM.map` `P.jj` `P.termsplit` `S.channel` `S.parent` `T.a11` `T.a13` `T.real` `T.scheme` `T.tower` |
| 1936 | Eckart & Young | `B.rank1` |
| 1936 | Madelung | `L.real` `S.ground` |
| 1936 | Tarski | `A.logic` `C.compare` |
| 1936 | Murray & von Neumann | `M.semi` |
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
| 1950 | Löwdin | `LS.asym` |
| 1953 | Green | `T.para` |
| 1954 | Kolmogorov | `3B.index` |
| 1955 | Tarski | `A.cert` `F.open` |
| 1957 | Bethe & Salpeter | `B.coll` |
| 1958 | Pauli | `Q.delta` |
| 1958 | Seaton | `A.seaton` `P.coreblind` `P.lcollapse` `P.polar` `P.qdt` `Q.delta` `Q.final` `Q.pol` |
| 1959 | Dijkstra | `A.EW` `A.W` `A.intext` `A.three` |
| 1960 | Erdos & Renyi | `A.dens` |
| 1961 | Fano | `P.perturb` |
| 1961 | Reeh & Schlieder | `M.rs` |
| 1962 | Berge | `G.near` `G.tower` `K.girth` `K.peak` |
| 1963 | Arnold | `3B.index` |
| 1964 | Edlen | `A.S` `K.zcross` `P.buildlimit` `P.charge` `P.iso` `Q.final` |
| 1964 | Moebius | `G.book` |
| 1964 | Rota | `C.local` `G.book` `L.amp` `L.box` `L.mobius` `L.void` `L.voidfrac` |
| 1965 | Kolmogorov | `F.unstatable` |
| 1965 | Penrose | `W.core9` |
| 1967 | Floyd | `K.clock` `K.clockfail` |
| 1967 | Tomita | `M.tt` |
| 1968 | Ireland and Kullback | `A.stat2` |
| 1968 | Alekseev | `3B.index` |
| 1968 | Gerratt & Mills | `LS.chord` |
| 1969 | Andrew & Cowan | `P.dcollapse` `Q.collapse` `Q.final` |
| 1969 | Griffin, Andrew & Cowan | `LS.coll` |
| 1969 | Pulay | `LS.chord` |
| 1970 | Codd | `A.alph` |
| 1970 | Fano | `P.perturb` |
| 1970 | Takesaki | `M.tt` |
| 1971 | Lane | `K.cat` `K.comp` `K.deadend` `K.jump` `K.twocol` |
| 1971 | Griffin, Andrew & Cowan | `LS.coll` |
| 1971 | Saari | `3B.index` |
| 1972 | Gabriel | `K.quiver` |
| 1972 | Karp | `S.core` `S.cover` `S.erasure` `S.lam` `S.unit` |
| 1973 | Takesaki | `M.takesaki` |
| 1973 | Saari | `3B.index` |
| 1974 | Curtis & Reid | `B.hstar` |
| 1974 | Johnson | `S.cover` `S.lam` |
| 1974 | Montanari | `A.montanari` |
| 1974 | McGehee | `3B.index` |
| 1975 | Baker & Pixley | `A.fix` `A.two` |
| 1975 | Csiszar | `G.stat` |
| 1975 | Marchal & Saari | `3B.index` |
| 1976 | Monaghan | `3B.index` |
| 1978 | Freuder | `A.blind` `A.gc` `A.modeA` `A.modeB` `A.three` `G.allcons` `G.prot` `K.corner` `W.jur` |
| 1978 | Gratzer | `L.pushback` `L.step` |
| 1978 | Rissanen | `A.ebits` |
| 1979 | Chvatal | `S.core` `S.unit` |
| 1979 | Dawid | `G.trip` |
| 1980 | Stanley | `L.sperner` |
| 1981 | Monjardet | `I.shape` `L.metric` `L.occ` |
| 1982 | Freuder | `A.freuder` `C.cut` `G.cons` `G.ref` `G.shape` `L.E0` `L.box` `L.tree` `T.trad` `3B.def` |
| 1982 | Racah | `T.trad` |
| 1982 | Marchal & Bozis | `3B.index` |
| 1983 | Beeri, Fagin, Maier & Yannakakis | `A.intext` `C.compare` `K.three` |
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
| 1996 | Lauritzen | `K.decay` `K.markov` `L.box` `L.voidfrac` |
| 1998 | Montgomery | `3B.shape` |
| 1999 | Deville | `A.env` `A.orient` `A.r4` `T.tight` |
| 1999 | Hentenryck | `A.orient` `A.rule` `A.stair` `A.staircls` `T.tight` |
| 2000 | Wald & Zoupas | `M.C1` |
| 2000 | Chenciner & Montgomery | `3B.five` |
| 2002 | Montgomery | `3B.metric` |
| 2003 | Fredenhagen & Verch | `W.rel` |
| 2006 | Hsiang & Straume | `3B.shape` |
| 2014 | Montgomery | `3B.shape` `3B.metric` `3B.pot` |
| 2017 | Diestel | `G.graph` |
| 2019 | Fleischer & Knauf | `3B.index` |
| 2021 | Kol | `3B.index` |
| 2023 | Kol | `3B.index` |
| 2024 | Sorce | `M.sorce` |
| 2026 | Lach, *The Löwdin Solution* | `LS.ent` `LS.law` `LS.coll` `LS.pin` `LS.asym` `LS.quart` `LS.chord` `LS.twin` |
| 2026 | Lach, *The Three-Body Problem for Unknown Masses* | `3B.tri` `3B.def` `3B.index` |

## The works this compendium leans on most

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

*The twelve objects the closing list names are entered in the main volume's Appendix D at §D.5.10 (register 1734), where they close at E = 0 with the corridor's precedent read as this work's.*

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

**The object.** For each admissible subshell, ask whether some value of `a` makes it
least-ν against its Pauli-admissible rivals. **Every step admits more than one — two to
six across the table, and one never** — the observed one always among them, never
uniquely determined.

**The theorem.** *In the plane where each admissible subshell is the point (√r, n),
ν = n − a√r takes whichever point a line of slope `a` reaches first, so only vertices of
the lower convex hull are ever taken. A point set carrying two distinct node counts has
at least two such vertices, and the unfilled set carries two below 124 electrons — every
neutral atom there is. Proved, and it needs no observation: the ambiguity is a fact about
point sets, not about atoms.*

**This work.** *One number is carried so the form stays exact. No single `a` lies in all
106 corridors and the running intersection empties eleven times; three values suffice for
the whole table and three are forced, boron, lanthanum and lawrencium having pairwise
disjoint corridors (register 1580). What is not geometry is that the observed subshell is
among the admissible ones at all 106 steps — that is the corridor, and it is what survives
the form's demotion (registers 1445, 1460, 1463).*

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
| **the necessity of state** | no step admits fewer than two; the theorem is geometry, the corridor is the physics |
| **the observability boundary** | closure enumerates; observation values |
| **the singleton-output rule** | an index is closed when its reading is unique |
| **the domain prohibition** | no parameter of this work is universal, so no pooled fit across regions is admissible |
| **the limit** | Λ_spectra closes at the last available species; E = 11, all named |
| **rival = donor iff not full** | the twelve anomalous steps, from Pauli alone |

---

# The Löwdin indexes — Λ_law and Λ_const

*Owed since register 1296; written. Nothing here answers
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

## Λ_const — fourteen constants on (role, carrier). E = 0 at 2 of 576.

Role order **exponent < centre < width < scale**. Standing: three fitted, six
measured, five derived or attributed.

**Every CENTRE is a small integer or half-integer** - 2 for the free shells, 2
for the gate, -1.5 for the switch, 2.5 for the l-validity, u0 = 4. **No SCALE
is.** The role axis orders by how much physics a number has absorbed.

**beta = 2/3 is load-bearing**: the only constant of arity three, in the
amplitude, the exponent and the validity, **and the one that is attributed.**

## The refusal, which is the more useful half

**`standing` cannot be a coordinate.** With attributed/derived/measured/fitted
on an axis the index closes at NO ordering; without it, at once.

> **An index whose coordinates mix the OBJECT with the OBSERVER cannot close,
> because the observer's axis has no order the object respects.**

The same fault is `origin` in Λ_var, `kind` in Λ_phys and `state` in
Λ_ladder - four occurrences of one mistake, stated here as a rule.
