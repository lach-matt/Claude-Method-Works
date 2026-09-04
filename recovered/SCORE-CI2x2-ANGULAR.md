# SCORE — PREDICTION-CI2x2, THE ANGULAR HALF. Session 71, route C-b.
# Prediction sha256 bb04e6c201c1650acba0cae3636af1605298ee3ab57c8b330fb70814c5fb1429
# FILED BEFORE ci2a.py EXISTED. Instrument: pack71/ci2a.py. Rows: pack71/ci2a.json.
# Reference configurations are the CHAIN's own (mode=chain, nlchain.jsonl ref_cfg).
# No SCF run. No radial integral. No constant. c untouched.

## CAN-FAIL, PASSED BEFORE ANY ROW WAS READ
The new all-zero 3j reproduces the SEALED `t7b_hf._c3j0sq` on 225 diagonal cases to 1e-12,
and returns NONZERO on (0,2,2) and (2,2,2) and ZERO on (0,1,2). **Both directions
demonstrated.** A routine that returned zero everywhere would have failed gate B.

## THE ROWS
    Z  el  a->b     l_a+l_b  open spectators  kappa    V
    24 Cr  4s->3d      2     3d3              [2]      NONZERO
    29 Cu  4s->3d      2     3d8              [2]      NONZERO
    58 Ce  5d->4f      5     5d1              -        ZERO
    90 Th  6d->5f      5     6d1              -        ZERO
    21 Sc  4s->3d      2     (none open)      -        ZERO
    57 La  6s->5d      2     (none open)      -        ZERO
    89 Ac  7s->6d      2     (none open)      -        ZERO

## SCORING
    CI-1  HELD.  One-body coupling nonzero nowhere: l_a =/= l_b at every row.
    CI-2  NOT TESTED. Needs the numerically averaged spectator set. Carried open.
    CI-3  HELD.  Direct two-body contribution nonzero nowhere. Exchange carries it alone.
    CI-4  HELD.  NONZERO exactly where l_A + l_B is even and ZERO where it is odd.
    CI-5  HELD.  Zero at all three first-entry rows.
    CI-6  NOT TESTED. Needs radial integrals. **This is what remains of the object.**
    CI-7  NOT TESTED. Needs the diagonaliser.

## THE ONE RESULT WORTH THE SESSION, AND WHY Ce AND Th ARE THE SHARP CASES
At Ce and Th the spectator shell **is open** — 5d1 and 6d1 — and the coupling is still
exactly zero. **That is the parity rule biting, not an occupancy accident.** Had the rows
come back zero only where nothing was open, the test would have shown nothing.
    l_a + l_b even is REQUIRED, and d<->f is odd.

**CONSEQUENCE, STATED AT ITS PROPER STRENGTH AND NO FURTHER.**
Relaxing L3 to a two-configuration superposition CANNOT displace the entrant at any row
that opens a channel, and CANNOT reach a tie-break row at all. The ORDERING clause, the
period lengths and the tie-break are immune to the single-determinant restriction **by
derivation from angular momentum and parity — not by a bound, and not by a survey of
rows.** Rung 2 previously reached the same conclusion by MEASUREMENT (the anomaly rows and
the first-entry rows have empty intersection, s60). Two independent routes, one empirical
and one derived, now give the same partition.

**WHAT IS NOT CLOSED.** V is NONZERO at Cr and Cu with kappa = 2. The configuration column
at the s<->d promotion rows is exactly where the object is alive, and its MAGNITUDE is
unmeasured. CI-6 decides whether the 2x2 repairs those rows or is too small to matter.
Either answer is a result. **Neither may be asserted before it is measured.**