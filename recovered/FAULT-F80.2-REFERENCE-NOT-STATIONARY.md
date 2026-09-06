# F80.2 — THE SEALED ENERGIES ARE NOT STATIONARY UNDER RESTART. run2 STOPS ON EIGENVALUE
# DRIFT; STEP 0(ii) IS STATED ON THE ENERGY. MEASURED: 0.034493 mHa AT Z=89 6d.
# RAISED AND MEASURED IN THIS SESSION. NOT A THREAT TO ANY VERDICT. NOT CLOSED.

## HOW IT WAS FOUND — BY A CAN-FAIL, WHICH IS WHAT THEY ARE FOR
perturb80's C1 control applies a ZERO perturbation and must return SAME BASIN. It did not.
Restarting the SCF from its own converged solution, with nothing changed, returned
**E lower by 0.021054 mHa in 4 iterations.**

## THE MECHANISM
`hfc2.run2` stops when `dmax < tol` with `dmax = max |e_new - e_old|` over shells — a test
on the EIGENVALUE DRIFT. **The adopted Step 0(ii) rule defines the field as a global
minimiser of E^RHF — a statement ON THE ENERGY.** The stopping test and the definition
are about different quantities, so the scheme halts at a point that is stationary enough
in eigenvalues and still descending in energy.

## THE MEASUREMENT — THE RESTART LADDER, Z=89 6d, RUNG 0
| pass | E | from first pass |
|---|---|---|
| 0 | -25694.541630577907 | 0.000000 mHa   **<- THE SEALED VALUE** |
| 1 | -25694.541651632084 | -0.021054 |
| 3 | -25694.541663092048 | -0.032514 |
| 6 | -25694.541664970395 | -0.034392 |
| 9 | -25694.541665072324 | -0.034494 |
| 12 | -25694.541665070870 | **-0.034493  STATIONARY** |
Monotone, geometric, ratio ~0.3. **THE SEALED VALUE SITS 0.034493 mHa ABOVE ITS OWN
BASIN FLOOR.**

## WHAT IT DOES NOT THREATEN, STATED PLAINLY
m(89) = 32.332 mHa. **The drop is 0.11% of the margin it would have to erase.** The s79
relaxation term is 10.072 mHa and the s79 beta-dependence is 0.451 mHa — both LARGER than
this. **No ordering, no entrant, no margin in this project is touched.** It applies
equally to every row, being a property of the stopping test, not of any Z.

## WHAT IT DOES MEAN
1. **It is an independent confirmation of F47.3's ~1e-5 figure**, arrived at by a different
   route: not mixed rungs, but the stopping test itself. 3.4e-5 Ha.
2. **It is a statement about the SCHEME, which is exactly where s79's ruling put such
   statements.** RULING-S79 §2: "(beta, maxit) LEAVES THE DEFINITION... F47.3's limit is a
   statement about the SCHEME, not about the field." **This is a second one, and the
   ruling's framing absorbs it without amendment.**
3. **Any future instrument that compares two ENERGIES at a precision finer than ~0.035 mHa
   must restart to stationarity first.** perturb80 does (H5). Nothing sealed does.

## NOT PROPOSED: RE-RUNNING THE CHAIN
107 rows at ~12 restarts each buys 0.034 mHa on quantities separated by tens of mHa.
**It is recorded as a known offset, not repaired, and the decision is M's.**