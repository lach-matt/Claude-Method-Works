# NOTE S101 -- Q6 ANSWERED: THE RESIDUE OBJECT HAS AN ESTABLISHED NAME AND LAW
## SEVERITY LINE: no faults. Attribution round; term-matched against primaries.
## ANSWER: the G5b defect is a PULAY TERM (Pulay 1969, Mol. Phys. 17:197) of the occupation parameter q.
## TERM-BY-TERM (R-A rule):
##   (i) Pulay's object: dE/dlam for a wavefunction not variationally stationary for the evaluated
##       functional = Hellmann-Feynman part + wavefunction-response ("Pulay") terms of the form
##       <dphi/dlam|H|phi> + h.c. (standard force expression; verified against 1969 abstract + the
##       standard formulation F = -Tr[Gamma dH] + Tr[Gamma^E dS] class). Pulay 1969: HF-force-only
##       methods are unreliable BECAUSE these terms are dropped.
##   (ii) Our object: defect(q) = dE_SCF/dq - dEfun/dq|_frozen = <grad_P Efun, dP/dq> -- verified
##       numerically at 58-B (R2 = R1, d101 receipt). Same structure, lam = q; the non-variational
##       character = shooting orbitals are not stationary points of Efun (per-shell slots + M-weighted
##       exchange, s100 G1; per-shell ceff => equal-l non-orthogonality, d101 xterms).
##   (iii) The s93 name for the measured object was already "Hellmann-Feynman-in-q defect" -- the sealed
##       record's own vocabulary matches: the defect is the correction Pulay showed must accompany a
##       Hellmann-Feynman derivative for non-variational states.
##   (iv) Machinery class for exact evaluation: Lagrangian / Z-vector method (Handy-Schaefer 1984 JCP
##       81:5031; Helgaker-Jorgensen) -- the standard route that makes response terms computable; ours
##       is directly computable since dP/dq is measured on the path.
## LEDGER: Law-candidate (M rules naming): "The HF-in-q defect of the sealed field is the Pulay response
##   term of the occupation parameter." Cite: Pulay 1969 (class), d101-58 receipt (our identity R2=R1).
## WHAT THIS CLOSES: the defect's EXISTENCE and FORM are now attributed + derived (not anomalous, not
##   unexplained in kind). WHAT REMAINS FOR ZERO RESIDUE: the per-shell VALUE derivation (route (a)) --
##   +8.0e-5 at 58-B and the 90/91 signs from named operator content, matching R2parts shell by shell.