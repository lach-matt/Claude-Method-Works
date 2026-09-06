# ATTRIBUTION LEDGER ADDENDUM -- SECTION I: LAW C FETCHED (s94, V4). Bach, Lieb, Loss, Solovej, "There are no unfilled shells in
# Hartree-Fock theory", PRL 72:2981 (1994); arXiv:cond-mat/9307066. PRIMARY: full text read (5 pp.) via alphaXiv.
## I1 STATEMENT (theorem, p.3): H = sum_i(-(1/2)Delta_i + U) + (1/2) sum_{i!=j} V, V positive definite as a two-body operator (Coulomb is).
##    Phi_HF a minimiser over ALL Slater determinants of N orthonormal space-spin orbitals (unrestricted; no symmetry constraint). If phi is an
##    eigenfunction of the HF operator h_Phi orthogonal to the N occupied orbitals, with eigenvalue eps, then eps > eps_k for all occupied k.
##    Corollaries (p.4): (1) the occupied orbitals are the N LOWEST levels of h_Phi -- "no proof of this assertion without V >= 0";
##    (2) Phi_HF leaves no degenerate level partially filled; there is a GAP, at least V_{N,N+1} (exchange-type integral of the HOMO/LUMO
##    pair, p.5), "usually not a tiny quantity", so "even an approximate degeneracy is unlikely".
##    Proof (pp.4-5): swap phi_N for phi_{N+1}; E(tilde Phi) - E(Phi_HF) = eps_{N+1} - eps_N - V_{N,N+1}; minimality + eps_{N+1} <= eps_N
##    gives 0 <= -V_{N,N+1} < 0. Three lines. Existence of the minimiser for N <= Z: Lieb-Simon 1977 CMP 53:185 (archive Step-0 authority
##    for general HF; Hantsch 1206.4932 for RHF).
## I2 SCOPE: unrestricted HF over the full determinant space. The theorem says NOTHING about restricted/symmetry-adapted or
##    average-of-configuration functionals, and NOTHING about fractional occupation (its determinants carry integer occupations).
## I3 TERM-BY-TERM MATCH TO OUR OBJECTS
##    H3 (single determinant)            <-> the theorem's object class exactly (when unrestricted).
##    H4 (average of configuration,      <-> NOT covered. Worse: the theorem PROVES that an open (n,l) shell with k < 2(2l+1) electrons
##        spherical open shells)              spread as a degenerate level is NEVER an unrestricted-HF minimiser. The unrestricted minimiser
##                                            of an open-shell atom breaks spherical symmetry (the "symmetry dilemma"); the object "subshell
##                                            (n,l), partially filled" exists ONLY under the restriction H4. So the Lowdin question ("which
##                                            subshell does the Zth electron enter") is well posed in RHF/average-of-configuration and is
##                                            NOT well posed in the HF that Law A (Bach 1992) bounds. H4 is therefore not a convenience but
##                                            the CONDITION under which the Challenge's own vocabulary exists. Criterion 2 (which electron)
##                                            inherits this: the differentiating electron is an H4 object.
##    Koopmans exact in the field (s93)  <-> the corollary "occupied = N lowest levels of h_Phi" is the unrestricted analogue; in our RHF
##                                            field it is NOT guaranteed by this theorem. The chain never uses eigenvalue ORDER to decide a
##                                            row (it uses argmin of total-energy differences D); L5 uses eigenvalue DIFFERENCES on the sealed
##                                            object, not orderings of occupied vs unoccupied. No clause of L1-L6 rests on corollary (1).
##    F93.6 (fractional-q d-shell          <-> NOT named by Law C (fractional q is outside the theorem). The s94 candidate claim in ledger H
##        non-stationarity)                  ("Law C is the law behind F93.6") was WRONG as stated: F94.4.
##    Gap >= V_{N,N+1}                   <-> a lower bound on the HOMO-LUMO gap of the UNRESTRICTED h_Phi. Not our margin m(Z) (which is a
##                                            total-energy second difference in the restricted field). Not usable for criterion 3.
## I4 WHAT LAW C GIVES THE CHAIN: the statement, provable in three lines from H1 + repulsive V, that the (n,l)-subshell picture is a
##    restricted-field object. Together with Law A (unrestricted HF exact through Z^{5/3} for TOTALS) this says: the exact theory and its
##    best single-determinant approximation both LACK the object the periodic table is written in; the object appears when spherical
##    symmetry is imposed (H4). This is the sharpest available statement of why Lowdin's Challenge cannot be answered "from H1 directly" and
##    must be conditional -- and it is a theorem, not an opinion. T4 should cite it at the FDS's statement of H4.
## I5 FAULT F94.4 SEVERITY: hygiene (candidate-law hygiene; nothing filed on it). Ledger H named Law C as the law behind F93.6 from its TITLE
##    before fetching. Fetched: it addresses H4, not fractional occupation. Species: citation by name (attribution standard, R-A extended).
##    F93.6 stays OPEN and un-attributed.