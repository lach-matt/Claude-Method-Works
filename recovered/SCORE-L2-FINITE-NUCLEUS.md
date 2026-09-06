# SCORE — L2, THE FINITE NUCLEUS
# SESSION 64. Prediction pack64/PREDICTION-L2-FINITE-NUCLEUS.md
# sha 5765c6d00d2d4325c210c3fb5f330806c5db6a3ffab74a1d216da3b3035ee0e5, filed
# 20:53:46Z BEFORE any solve of this test and before the Z=120 chain row was read.
# Instrument pack64/l2fin.py. Rows: Z = 3, 89, 120 (see prediction §"three atoms").

## THE FALSIFICATION, FIRST, BECAUSE THE PREDICTION SAID TO REPORT IT FIRST

**S2 IS FALSIFIED. L2 IS NOT BELOW THE WORKING FLOOR AND NEVER WAS.**
Predicted |dD| < 0.05 mHa at every row. Measured **0.27480 mHa at Z=89** and
**11.61091 mHa at Z=120** — 232x the floor. The project has quoted every margin in
every document against a 0.05 mHa floor; **that floor covers numerics and does not
cover the nucleus.**

**S1 ALSO FAILED ON MAGNITUDE.** Predicted dE of order 1 Ha at Z=89 (range 0.3-3).
Measured **16.95 Ha**. The scalar-relativistic density at the origin is ~6x the
non-relativistic hydrogenic estimate the prediction was built on. The method guard
inside S1 PASSED (dE >> 0.01 Ha; 1569 mesh points lie inside R_nuc at Z=89), so the
measurement stands and it is the prediction that was wrong.

## THE MEASUREMENT

    Z      dE(ref)      dD(entrant)    margin      margin after L2   margin/|shift|
     3    9.76e-08 Ha    0.00000 mHa   67.67 mHa      67.67 mHa        5.8e7
    89    16.95 Ha      -0.27480 mHa   32.33 mHa      32.48 mHa          212
   120    1158 Ha      +11.61091 mHa   98.28 mHa      84.86 mHa          7.3

margin shift is dD(runner-up) − dD(entrant); at Z=89 also dD(5f) − dD(6d) = +0.27273
mHa on the 126.16 mHa tie-break gap.

## WHAT PASSED, AND IT IS WHAT L2 NEEDED
    S1 sub-clause   every l>0 orbital contributes <= 1e-12 Ha. The shift is 1s and 2s
                    and nothing else.                                          PASS
    S2 cancellation |dD|/dE = 1.6e-5 at Z=89, 1.0e-5 at Z=120. Five orders.    PASS
    S2 entrant      unchanged at all three rows.                               PASS
    worse falsifier |dD| never approaches the row's margin.                NOT FIRED

**The finite nucleus costs the ENERGIES enormously and the ANSWER very little.** That
is the structure the assembly claims for every approximation in the chain, and L2 now
has a number instead of a blank.

## THE NUMBER SPLITS THE WALK IN TWO, AND THIS IS THE USEFUL PART
    Z <= 108 (the CLAIMED region)   worst case Z=89: 0.15 mHa on the tightest margin
                                    in the whole chain. Factor 212. Safe, stated.
    Z >  108                        factor 7.3. At Z=120 the finite nucleus eats 14%
                                    of the margin.
Rows above Z=108 already carry PREDICTED labels for want of a measured configuration.
**This is a second, independent reason not to claim them, reached from a different
direction.** The scope limit Z <= 108 is now supported twice.

## TWO LIMITS ON THE MEASUREMENT ITSELF, DECLARED
1. It is FIRST-ORDER perturbation theory on point-nucleus orbitals. At Z=120 the
   perturbation is ~2% of the total energy and first-order PT is at its limit: that
   number is an ORDER OF MAGNITUDE, not a precise value. Tightening it means solving
   self-consistently with a finite nucleus, which edits the sealed potential.
2. **M1's predicted numerical check is WITHDRAWN AS UNEXECUTABLE.** There is no mass
   parameter in this field to rescale, so the normal mass shift stands on the exact
   scaling argument alone (uniform scale mu/m on every channel; margins scale
   identically; argmin invariant identically). M2's specific-mass-shift bound,
   |dD_SMS| <~ (m/M)|D| = 0.016 mHa at Z=3, remains an ORDER-OF-MAGNITUDE BOUND and is
   declared as one. Given that finite SIZE came in 200x above prediction, that bound
   should be treated with corresponding suspicion and is not to be quoted as measured.

## LEDGER CONSEQUENCE
L2 moves from **APPROXIMATION, UNBOUNDED** to **BOUNDED, WITH THE BOUND STATED**, at
0.15 mHa on margins for Z <= 108. Every one of the twelve links of ASSEMBLY-RUNG-0 now
carries a number **except correlation**, which is a declared restriction of the model
rather than a hole in the ledger — see BRIDGE §3.
