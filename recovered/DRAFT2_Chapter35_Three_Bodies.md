# DRAFT 2 — Proposed Chapter 35: Three Bodies, and What a Complete Index Is Allowed to Say

*For review. Placement: Part VII — The Challenges, after §34 The Löwdin Challenge. Not written into the book.*

Serving PART III — THE LAW and PART VI — THE REACH. The chapter runs the method on the one object §12.11 named as the maximal case of what Chapter 18 forbids, and reports that the method's negative is the problem's solution.

### 35.1 The challenge

§31.1.1 tested celestial mechanics on families and found "nothing here touches Poincaré." §12.11.2 went further: three bodies carry all three excluded forms at once — a sum in the superposition, a difference in the relative position, a symmetric function in the mutual interaction — so the book's prediction was envelope precision only. §21.5.1 counted the deficit: K₃ has treewidth 2, needs strong 3-consistency, and ℛ reaches 2; the shortfall is exactly one level. The challenge was to take those three negatives and ask whether, together, they *are* the solution. Register [new].

### 35.2 The number before the interpretation

Thirteen mass order-types, six checks each, 78 of 78. Triangle form at cap 8: 344 cells, 0 join failures, 8,385 meet failures; caps 3–12 give meet failures 12 · 111 · 477 · 1,488 · 3,780 · 8,385 · 16,812 · 31,227 · 54,555 · 90,705 with join failures at 0 throughout. Two-body chain: 0 of either kind at every cap. Eight attribution questions, eight closed. One inherited polynomial wrong, replaced.

### 35.3 What the book contributed, section by section

**§25.6 supplied the definition of solution.** A complete index has E = 0 and makes no predictions. Applied to ℳ_{E,L} decomposed into invariant tori, periodic orbits, hyperbolic sets, the ergodic region and the collision set, the decomposition is an index, and it closes: exhaustive because every motion has an asymptotic class, disjoint because the collision set is of measure zero for all masses (Saari 1971, 1973) and there are no non-collision singularities at n = 3 (Painlevé). E = 0. Hence the index is complete and predicts nothing — which is exactly Brudno's theorem on the chaotic stratum, that an orbit's complexity grows at its entropy rate. The two statements "the problem is completely solvable as a stratification" and "no trajectory formula exists" are one statement, and §25.6 is where that was already written.

**§18.4.1 supplied the certificate.** The reduction to the shape sphere is a sequence of dropped coordinates — translation, rotation, scale — and the law of realised closure says an open index closes only where such a certificate is exhibited. Montgomery's shape map is that certificate: onto, exactly identifying oriented-congruent triangles, sending only triple collision to zero. The law was confirmed on a fourth open object outside the book's own five.

**§12.11.2 supplied the shape of the answer.** The three excluded forms are read directly off the potential: U = Σ c_ij/d_ij is a sum; the Jacobi vectors are differences; the potential's minimal polynomial is symmetric in the three terms. The book had said three bodies carry all three; the derivation confirms it term by term, and §12.11.3's dichotomy — counting coordinates close exactly, coupling coordinates close as envelopes — makes the strata envelopes by construction. The cap-8 computation reproduces §12.11.2's "join-closed and meet-broken" on a grid the book never ran.

**§12.11.1.3 and §12.11.0.2 supplied the licence to remove time.** An index has a time column exactly when its cells are moves; the shape cells are configurations; so time is removed and the flow becomes the geodesic flow of the Jacobi–Maupertuis metric. Time returns as a quadrature carrying the transcendental part. §12.11.4's "precision is path-dependent; physics is not" is the geodesic equation with rational Christoffel symbols.

**§21.5.1 supplied the deficit and its size.** One level. The book's only genuinely ternary object is the bracket T(n−1), T(n), T(n+1); the three-body problem is the ternary object of celestial mechanics; its solution is therefore a bracket, and §31.1.1 had already named the brackets: zero-velocity surfaces, Hill regions, KAM tori.

**§14.5's seed supplied the five points.** Euler's three collinear roots and Lagrange's two equilateral points exist for every mass triple and are the least set from which the families are generated.

**§31.1.1 supplied the silence.** L4/L5 stability at μ < 0.0385209 is a threshold; the method is silent on thresholds; the chapter does not pretend otherwise.

**§2.14 supplied the correction.** The first audit run failed 13 of 13 on one check. Uniform failure was the signal: the fault was in the audit, a factor of the hyper-radius carried in from an inherited convention. Stating the number before the interpretation is what located it. Register [new].

**§E.5 and audit 7 supplied the ledger.** Eight residues were formed into questions and put to the literature before anything was derived. Seven belonged to others; the eighth — a degree-8 form of the potential — turned out to be classical (the norm over (ℤ/2)³, Lagrange's resolvent) and the version in circulation turned out to be wrong in two coefficients. The second route caught it, which is register 784's mechanism on a new object.

### 35.4 The law this chapter adds

**Mass-uniformity.** *Every mass-dependent quantity in the three-body index enters through c_ij = (m_i m_j)^{3/2}/√(m_i+m_j) and the three collision rays b_ij; the manifold, the metric, the norm polynomial and the constraint graph are mass-free. A change of masses moves the five fixed points and rescales three rays; it cannot create a sixth point, close a meet, or open a join.* The symmetry group of the index has order 6, 2 or 1 according to how many masses coincide, and that is the only thing the order-type of the masses decides. This is the Index of Indices' one-line claim — coordinates come from the subject or from nowhere — with the subject's contribution isolated to six numbers.

### 35.5 What the chapter does not claim

No trajectory. No prediction. No extension to n ≥ 4 of the measure-zero clause (Xia 1992 shows non-collision singularities exist at n = 5). No statement about the contents of ℳ_per beyond the equal-mass figure-eight, which is Moore's and Chenciner–Montgomery's. Nothing that touches Poincaré.

### 35.6 The one-line summary

*The three-body problem is solved to exactly the precision a closed index permits, and the book had already computed that precision before the problem was posed to it.*

---

**Cross-references to insert:** §12.11.2 (forward reference to 35.3); §21.5.1 (forward reference to 35.3); §25.6 (add: "Chapter 35 runs this on three bodies"); §31.1.1 (add: "completed in Chapter 35"); Part VII contents; Index; References (add the bibliography of Draft 1, minus the book's own entries).
