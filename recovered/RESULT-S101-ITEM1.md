# RESULT S101 ITEM 1 (G5b) -- P1 SCORED AGAINST PREDICTION 56c319fc: FALSIFIED. G5b remains OPEN.
## SEVERITY LINE: one prediction fault (F101.4, the scored miss), one instrument fault (F101.3, caught and
##   fixed in-run before any scoring read). No sealed number affected. The measurement side is REPRODUCED.
## RUNGS AT 58-B (pack101/d101.py, receipt d101-58.json; 5 foreground SCF solves; prediction hash gate PASS):
##   R1 direct  = +9.014e-5  -- REPRODUCES the sealed s93 measurement (+8.0e-5, sign + band). Object real.
##   R2 chain   = +1.059e-4  -- d/dq Efun[Q; P(q); I(P(q))] at fixed Q. IDENTITY R2 = R1 holds to FD class
##                (gap 1.6e-5, h=0.1 orbital path vs Richardson). THE DEFECT IS EXACTLY THE NON-STATIONARITY
##                OF Efun ALONG THE SHOOTING PATH -- derived in form and verified numerically.
##   R3 proj    = -3.191e-4  -- the T1-only (sqrt(M) exchange-weight) projection. OUTSIDE window
##                [5.6e-5, 10.4e-5], SIGN WRONG. P1 FALSIFIED.
## F101.3 SEVERITY instrument (caught in-run): R2 as first coded held I_a fixed while moving orbitals,
##   dropping the kinetic path term dI/dq; exposed by magnitude (-7.2 Ha); fixed (Ione per endpoint);
##   re-run before any scoring read.
## F101.4 SEVERITY prediction: the G5b mechanism attribution AS STATED -- "defect = projection of the G1
##   T1 content <dP/dq|(A_shoot - A_Efun)|P>" -- is FALSIFIED. MECHANISM FROM THE DECOMPOSITION (R2parts
##   vs R3parts, per shell): the true per-shell chain contributions are +3e-5-class for n>=3 shells and
##   NEGATIVE for the 1s/2s/2p core, netting +1.07e-4; the T1-only projection is outer-shell-negative and
##   misses this structure entirely. TWO named reasons: (i) T2-class per-shell operator-content terms
##   (Vloc-slot/ceff conventions) are 1e-7 in the EIGENVALUE expectation <P|dF|P> (s100) but carry NO
##   smallness in the PATH projection <dP/dq|dF|P> -- the s100 G1 closure bounds the wrong projection for
##   this object; (ii) the hfc2 field is per-shell (own-ceff differs by shell), so same-l shells are NOT
##   mutually orthogonal eigenfunctions of one operator -- measured <dP_a/dq, P_b>: 5s-6s = -1.2e-2,
##   4d-5d = -3.8e-4, 4s-5s = -2.5e-4 -- and the dropped constraint-class cross terms are first-order.
## WHAT STANDS DERIVED (new, receipt-backed): defect(q) = <grad_P Efun, dP/dq> EXACTLY (R2 = R1); the
##   defect is a property of the construction (Efun's operator content vs the shooting field), per-shell
##   decomposed at 58-B. The +8.0e-5 is not one term's projection; it is the full non-stationarity sum.
## NOT RUN (order conditional): 90-A, 91-A scoring (P2, P3 conditional on P1); cf-Z control (window lever
##   moot after falsification -- the falsification itself is the non-vacuous demonstration).
## STATE: G5b OPEN. Residue count: ONE. Next-route candidates FOR M'S RULING (not executed):
##   (a) exact-operator projection: apply the s100 term-matched F_Efun build per shell to <dP/dq|.|P> +
##       constraint terms -- tests whether the FULL operator-content difference (T1+T2+cross) closes R2
##       analytically (the T1-only clause falsified; the full-content clause is the surviving candidate);
##   (b) rule the derived identity R2 = R1 (defect == Efun non-stationarity on the shoot path, per-shell
##       decomposed) as the closure statement itself -- the residue named, derived, and located, with the
##       d-selectivity and 90/91 sign flip to be exhibited by the same decomposition at those rows.