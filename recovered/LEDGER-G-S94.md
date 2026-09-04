# ATTRIBUTION LEDGER ADDENDUM -- SECTION G: LAW A, THE LARGE-Z THEOREMS (s94). Fetched this session, not recalled.
## G · NON-RELATIVISTIC LARGE-Z ASYMPTOTICS OF THE TOTAL ENERGY
G1  Frank, R.L., Merz, K., Siedentop, H. (2022). "The Scott conjecture for large Coulomb systems: a review." arXiv:2204.10081.
    PRIMARY (full text read via alphaXiv, pp. 4-7, 20-21, 26, 29, 44). Carries the statements of G2-G5 with theorem numbers; used as the
    fetched authority for their content. Relativistic section (Thm 4.6) also read.
G2  Lieb, E.H., Simon, B. (1977). "The Thomas-Fermi theory of atoms, molecules and solids." Adv. Math. 23:22-116. Abstract read PRIMARY
    (Caltech copy, math.caltech.edu/SimonPapers/53.pdf); theorem content via G1 Thm 3.1 [Thms III.1, III.3 of G2]:
    E_S(N,Z)/Z^{7/3} -> E^TF(alpha,1), alpha=N/Z fixed; rescaled ground-state density -> TF density (weak L^1, Coulomb norm).
    Error: o(Z^{7/3}). A statement about the TOTAL ground-state energy and the TOTAL one-particle density.
G3  Scott correction. Hughes (1986/1990, lower bound); Siedentop-Weikard (1987-89, both bounds); Bach (1991/93, ions). Via G1 Thm 3.4:
    E_S(N,Z) = E^TF(alpha,1) Z^{7/3} + (q/4) Z^2 + O(Z^{47/24}).  [SECONDARY as to the originals; statement PRIMARY via G1]
G4  Fefferman, C., Seco, L.A. (1990-1996, seven papers). Via G1 eq. (1.15): E_S(Z) = E^TF Z^{7/3} + (q/4) Z^2 - C_DS Z^{5/3} + o(Z^{5/3}).
    Dirac-Schwinger term rigorous. [SECONDARY as to originals; statement PRIMARY via G1]. G1 remarks the Z^{5/3} term is exchange PLUS the
    semiclassical eigenvalue-sum asymptotics of -(1/2)Delta - Phi^TF with semiclassical parameter Z^{-1/3}.
G5  Bach, V. (1992). "Error bound for the Hartree-Fock energy of atoms and molecules." Commun. Math. Phys. 147:527-548. PRIMARY (abstract
    read, projecteuclid): |E_S - E_HF| = O(Z^{5/3-delta}) for any delta < 2/21. I.e. HF is exact through order Z^{5/3} inclusive; the
    correlation energy of the whole atom is o(Z^{5/3}). Bach (1993) CMP 155:295 extends to the TF mean-field with Dirac exchange. [abstract]
G6  Relativistic leading order. Via G1 Thm 4.6 (Sorensen 2005 Chandrasekhar; Cassanas-Siedentop / Frank-Siedentop-Warzel Brown-Ravenhall;
    Handrek-Siedentop 2015 Furry): (E_rel - E^TF)/Z^{7/3} -> 0 at fixed Z/c below the critical coupling. Relativistic Scott term differs
    (Frank-Siedentop-Warzel 2008). Leading order is non-relativistic; the correction enters at Z^2. [SECONDARY as to originals]
G7  NOTED, NOT FETCHED: Seco-Sigal-Solovej, "Bounds on the ionization energy of large atoms" (CMP 1990), and Solovej, "The ionization
    conjecture in Hartree-Fock theory" (Ann. Math. 2003): bounds on an energy DIFFERENCE (ionization energy) but of the form C Z^{20/21}
    / uniform-in-Z constants for the HF excess charge. Seen by title in G1 and the Bach reference lists only. [SECONDARY, title only]
## Term-by-term match to our objects (attribution standard, R-A extended)
##   H1 Schroedinger Hamiltonian H_{N,Z}, non-rel   <->  G2-G5 exactly this operator (q=2). Our FIELD is scalar-relativistic (H5): the
##       non-rel theorems do not apply to the field AS RUN; G6 says their leading order survives relativity, nothing finer.
##   E_HF (our sealed totals, ~9e3..3.8e4 Ha)       <->  G5's E_HF (unrestricted HF over all determinants). Ours is RESTRICTED (H3/H4, RHF,
##       average of configuration): E_RHF >= E_HF; G5 bounds E_HF, not E_RHF. The restricted-vs-unrestricted gap is NOT in any theorem here.
##   D(c;Z,core) = E[core+c] - E[core]                <->  NO theorem object. It is a difference of two totals of DIFFERENT electron numbers
##       (N and N+1) at the same Z; G5 controls each total to O(Z^{5/3-delta}) with an unstated constant; the difference inherits the SUM of
##       the two bounds, not a cancellation. G7 controls ionization-type differences only to powers of Z.
##   m(Z) = D(c1) - D(c2), tightest 0.03233 Ha (Z=89) <->  a difference of two D's: a second difference of totals. No theorem here has a
##       second-difference statement. Numerically at Z=89: Z^{5/3-2/21} = 1.15e3; Z^{5/3} = 1.78e3; Z^{47/24} = 6.5e3. The margin is
##       2.8e-5 of the smallest of these, before the unknown constant.
## What Law A gives the chain
##   (a) H3/H4 are asymptotically JUSTIFIED as to totals: the independent-particle description is exact through Z^{5/3} (G5). This is the
##       strongest available first-principles warrant that a single-determinant field is the right object at large Z. It is a statement about
##       the FUNCTIONAL, not about any row.
##   (b) It does NOT bound |D_exact(c;Z) - D_HF(c;Z)| for either channel, NOR the differential error between two channels against m(Z).
##       The required statement -- correlation shifts a two-channel ordering margin by less than 32 mHa at Z=89 -- is a second-difference,
##       row-specific, restricted-functional claim; none of G2-G7 is of that form, and their error terms are 10^4-10^5 times m(Z) before constants.
##   (c) G1 Remark 3.12 / Heilmann-Lieb: "shell structure is not a prominent property" of the large-Z limit density -- Law A lives on scales
##       (Z^{-1/3}, Z^{-1}) where the filling order is invisible. The n+l ordering is a sub-asymptotic (oscillatory, Z^{3/2}-scale at most,
##       Cordoba et al.) object. Law A cannot see the thing the chain decides.
## VERDICT FOR ITEM 2: Law A cannot bound the differential D(c;Z) error. Filed honestly. Criterion 3 sufficiency stays OPEN; routes (i)/(iii).