# AMENDMENT — PD-0′. A CORRECTLY SPECIFIED INERTNESS GATE FOR T-D.
# FILED SESSION 66 on M's ruling (b) to F66.2. Own sha, verified by the driver.
# `PREDICTION-T-D.md` (sha 774d9d5f…, 22:55:53Z) IS NOT EDITED AND IS NOT SUPERSEDED
# IN ANY OTHER RESPECT. PD-1..PD-5 stand exactly as filed and are untouched.

## TIMING FLAG, DECLARED FIRST (R 1449)
**THIS GATE IS WRITTEN AFTER ITS NUMBER WAS READ.** D = -0.266643170 was measured and
reported before this file existed. PD-0′ is therefore NOT a prediction and is NOT
scored as one. It is a re-specification of a gate whose measurement is already in the
record, and it is admissible only because:
  * the FAILURE of PD-0 as written stands in the record permanently (F66.2) and is
    not amended away;
  * the quantity being gated — inertness of `NodeSpec` on a healthy channel — is a
    property of the INSTRUMENT, not an outcome of T-D. No cell of T-D has been run,
    and nothing in PD-0′ can move any cell's class;
  * the defect being repaired is arithmetic and was diagnosable without the number:
    a 3e-6 bound against a reference stored at 1e-5 is unsatisfiable by construction.

If any of those three ceased to be true this amendment would be a loosening applied
after the fact, and would be inadmissible.

## PD-0′ — THE GATE
T-D runs if and only if ALL THREE hold at Z=21 on the healthy 3d channel:

    (i)   `NodeSpec` DOES NOT RAISE.                      [the substance of PD-0]
    (ii)  round(D, 5) == -0.26664 exactly.                [the banked value, at the
                                                           precision the bank stores]
    (iii) |D - (-0.266643)| <= 1e-6.                      [s42's six-decimal value in
                                                           FINDING-REPAIR-4D §0]

Clause (iii) is the real gate: it compares like with like, at a precision the
reference actually carries. Clause (ii) is the bank check with the quantisation
stated rather than ignored. Clause (i) is what PD-0 was for.

## WHAT THIS DOES NOT DO
It does not touch PD-1 (the Z=21 4d determinism receipt, minlog = +0.9083 ± 0.01),
PD-2 (the shortfall integer as classifier), PD-3, PD-4 or PD-5. It does not change
the ten scored cells, which remain fixed as filed and all at Z ≤ 108 under M's
ruling (2). It does not change the class definitions, which are read off the measured
node spectrum under M's ruling (3) and are not forced.

## RECORD
    PD-0   FAILED AS WRITTEN.  |d| = 3.170e-06 against a filed bound of 3e-6.
           Entered permanently. F66.2.
    PD-0′  SUPERSEDING GATE. Timing-flagged. Not scored as a prediction.
