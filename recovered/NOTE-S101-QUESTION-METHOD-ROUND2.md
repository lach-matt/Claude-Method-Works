# NOTE S101 -- QUESTION-METHOD ROUND 2 (M's method: residue -> question -> outward query)
## SEVERITY LINE: no faults this round. One PRIMARY HIT term-matched; one null; one internal.
## Q3 (fractional-q physics): "Is dE/dq = eps for fractional occupation in HF, and what breaks it?"
##   HIT: Baerends, arXiv:1911.05651 (2019), "A critique of Janak's theorem". PRIMARY READ (pp.1-3,8,14-16).
##   TERM-BY-TERM MATCH (R-A rule):
##   (i) Slater relation dE^{HF1}/dn_p = eps_p is EXACT for the HF energy written with LINEAR occupation
##       dependence (E_HF1, his Eq.41-42) -- chain rule only. <-> our path functional class.
##   (ii) THE KEY CLAUSE (his Eq.46-47): the derivative is CONVENTION-DEPENDENT off the integer domain.
##       E_HF2 (quadratic n-dependence) gives dE/dn = 2n*eps -- identical physics at integers, different
##       derivative on the fractional path. "The derivative with respect to occupation number depends on
##       the way occupation numbers are introduced."
##   (iii) Slater TS fractional occupation is "a mathematical device" -- matches our fractional-q path's
##       instrumental status (no physical claim; T4 language guarded already).
##   MAPPING TO G5b: dE/dq - eps = 0 REQUIRES the eigenvalue operator and the differentiated functional to
##       be the SAME variational object (the functional's own Euler-Lagrange operator). Where A_shoot is not
##       the EL operator of Efun, the Slater relation acquires a first-order defect -- precisely the
##       non-stationarity projection <dP/dq|(A_shoot - A_Efun)|P> of Item 1. MECHANISM CLASS CORROBORATED.
##   NOT COVERED by the hit: the sign law, the magnitude, the d-vs-s selectivity -- Item 1's formula
##       remains ORIGINAL content; the citation carries the class, not the number.
##   LEDGER CANDIDATE (M rules on naming): Slater dE/dn = eps (Slater 1969/Quantum Theory of Molecules and
##       Solids v4; Janak 1978 PRB 18:7165 for the DFT form; Baerends 1911.05651 for the convention-dependence
##       clause). Cite at T4 where the fractional-q instrument is introduced.
## Q4 (numerical sign law for non-self-adjoint discretization defect): NULL. Nearest: spectral-symbol
##   analyses of discretized self-adjoint operators (2004.10058, 1908.05788) -- class-adjacent, no defect-sign
##   theorem. The one-sidedness of our defect must come out of Item 1's projection itself.
## Q5 (d-selectivity): INTERNAL. Expected answer is the projection's own radial weight (d states sample the
##   region where the omitted sqrt(M) varies fastest); scored by the P1-P3 run, not by literature.
## METHOD ASSESSMENT (for M): 2 rounds, 5 questions -> Item 2 discharged (stale-premise fault caught),
##   1 mechanism-class corroboration gained, 2 nulls that certify originality of the remaining derivation.
##   The remaining residue (G5b) is not further reducible by query: it requires the one specified run.