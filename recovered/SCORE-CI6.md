# SCORE — CI-6, THE MAGNITUDE OF V. Session 73, R-C(a). R 1969.
# Prediction: pack71/PREDICTION-CI2x2.md, sha256 bb04e6c201c1650acba0cae3636af1605298ee3ab57c8b330fb70814c5fb1429,
# filed and hashed at s71 BEFORE ci2.py existed. Determinant choice fixed by
# pack73/DERIVATION-CI6-SECTOR.md, filed BEFORE any radial integral was evaluated.
# Instrument pack73/ci2.py · rows pack73/ci2.json · scalar-relativistic HF, c = 137.035999.
# No constant beyond c. No CG recoupling: this is R-C(a), not (b).

## CAN-FAIL, PASSED BEFORE ANY SCORED ROW — AND IT CAUGHT A REAL ERROR
    A1 allowed   d->s angular only        +0.063888     NONZERO required   PASS
    A2 forbidden p->s angular only         0.000000     ZERO required      PASS
    B  opposite-spin replacement           0.000000     ZERO required      PASS
    C  closed 3p6 spectator, full radial  -5.42e-20 Ha  ZERO required      PASS
    D  lever: 1 open d -> 2 open d        shift 4.07e-03 Ha  MUST MOVE     PASS
**C FAILED ON FIRST RUN at -9.99 mHa and the failure was diagnostic.** The exchange angular
factor had been written c^kap(lk mk; lb mb); Condon-Shortley requires c^kap(lb mb; lk mk).
The two differ by (-1)^(mk-mb) and that phase is exactly what cancels the closed-shell sum.
**Fixed before any row was read.** Recorded, not suppressed.

## THE ROWS
    Z  el  replacement          (M_L,M_S)   field   |V| mHa    vs 0.05 mHa floor
    24 Cr  3d(0,dn) -> 4s(0,dn)  (2, 2)      A       4.0711     CLEARS  x81
    24 Cr  3d(0,dn) -> 4s(0,dn)  (2, 2)      B       2.7582     CLEARS  x55
    29 Cu  3d(0,dn) -> 4s(0,dn)  (0, 1/2)    A       0.0000     BELOW  (4.3e-19 Ha)
    29 Cu  3d(0,dn) -> 4s(0,dn)  (0, 1/2)    B       0.0000     BELOW  (8.7e-19 Ha)
field A = HFSR average-of-configuration orbitals of 3d5 4s1 (Cr) / 3d10 4s1 (Cu);
field B = the competing configuration's orbitals. Orbital-set sensitivity at Cr: 32%.
Both fields clear the floor at Cr; both give machine zero at Cu.

## SCORING — CI-6 IS A CONJUNCTIVE CLAUSE AND IT IS FAILED AS FILED
CI-6 reads: "V at Cr 24 AND Cu 29 clears the 0.05 mHa working floor."
    Cr 24  CLEARS by a factor of 55-81.  
    Cu 29  DOES NOT CLEAR.
**CI-6 FAILED AS FILED.** The clause is not rewritten to fit the outcome. What follows is
what the failure MEANS, and it is not what the clause's falsifier anticipated.

## THE Cu ZERO IS NOT A SMALL NUMBER. IT IS AN EXACT SELECTION RULE, PREDICTED FIRST.
DERIVATION-CI6-SECTOR §3a, filed before any radial integral: Cu's A determinant is closed
3d10 + 4s(up), which is PURE 2S; the B determinant at M_L=0 is a 3d9 hole at m=0 with 4s2,
and 3d9 carries only 2D, so B is PURE 2D. H is a scalar; <2S|H|2D> = 0 exactly.
**The instrument was never told this and reproduced it to 4e-19 Ha on both fields.**
That is an independent validation of the instrument on a known answer, and it converts the
Cu entry from "below floor" to "forbidden".

## WHAT MOVED, AND WHAT DID NOT
1. **The parity rule is NECESSARY, NOT SUFFICIENT.** s71 scored Cu NONZERO at SHELL
   resolution (kappa=2, open 3d8 spectator). At DETERMINANT resolution Cu is exactly zero.
   No contradiction — a shell-level flag is an upper bound on support — but the s71 table's
   Cu entry is SUPERSEDED. Registered as F73.1. CI-4's falsifier ("zero at BOTH Cr and Cu")
   is NOT triggered: Cr is nonzero. **CI-4 STANDS.**
2. **CI-1, CI-3, CI-5 UNTOUCHED.** CI-2 and CI-7 still NOT TESTED.
3. **THE ORDERING CLAUSE IS UNTOUCHED.** Nothing here reaches a first-entry or tie-break
   row. Deliverable 1 is not amended by this session.

## WHAT CI-6 DECIDES ABOUT THE CONFIGURATION COLUMN — STATED AT ITS PROPER STRENGTH
At **Cu 29** configuration mixing between 3d10 4s1 and 3d9 4s2 is **rigorously forbidden**.
The Cu anomaly is not "too small to repair by the 2x2"; it is **unreachable by the 2x2**.
That is a closure by derivation, not by bound.
At **Cr 24** V is real and clears the floor by ~2 orders. But per DERIVATION §3b/§4 the
element connects 3d4 4s2 (5D, its ground term) to an EXCITED 5D of 3d5 4s1 — NOT to Cr's
7S ground term, which has no partner of the same (L,S) in the other configuration.
**The 2x2 therefore cannot lower Cr's observed ground state at either row.**
Whether it moves the A-vs-B comparison at all is CI-7, which needs E_A, E_B and the
diagonaliser and is NOT run under this ruling.

## TIMING
Prediction hashed at s71. Determinant sector derived and hashed at s73 before any radial
integral. Can-fail passed before any scored row. The Condon-Shortley fix was made before
any scored row was read. No design decision in this score followed a scored number.