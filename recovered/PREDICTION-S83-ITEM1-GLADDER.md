# PREDICTION — S83 ITEM 1 · CLAUSE 1 · THE g-LADDER
# FILED BEFORE ANY ROW IS READ. R1449.
# Instrument: pack83/gtest83.py. Object adopted by M's ruling at s83 open.

## THE OBJECT

F_core's tail is exactly Coulombic with net charge 1 (MEASURED s82: q_eff = -rV =
1.000000 over 20-298 a0).  Every bound candidate therefore admits an EXACT defect
representation, by definition and not by approximation:

    D(n,l) = -1 / (2 nu^2),      nu := n - delta(n,l),      delta := n - (-2D)^(-1/2)

With sigma := n + l this is the identity

    **nu = sigma - g(l),        g(l) := l + delta(n,l)**

and since energy order IS nu order, Madelung (order by sigma, ties by least n) is
EXACTLY equivalent to two statements about g:

    (G-within)  g increasing in l inside each sigma-class      <=> the tie-break
    (G-across)  max g at sigma+1  -  min g at sigma  <  1      <=> the n+l ordering

D is the project's own sealed total-energy currency, relaxed on both sides.  This is
route (c): the property evaluated at the RELAXED field directly.  Routes (a) and (b)
are run for the comparison M ordered.

## TIMING FLAG — DECLARED, NOT BURIED

**Z=90 WAS HAND-COMPUTED BEFORE THIS FILE WAS WRITTEN.** g(7p)=6.054, g(6d)=6.382,
g(5f)=6.089 at sigma=8; g is NOT increasing in l; the walk's order 6d < 5f < 7p is
reproduced.  **Z=90 IS EXCLUDED FROM EVERY SCORED BAND BELOW** and appears only as a
worked example.  Z=89 was NOT computed.  No aggregate was computed.

## CLAUSES

P1 · MACHINERY.  nu-ordering reproduces the sealed D-ordering at 107/107 rows.
     nu is a strictly monotone function of D, so this is a CHECK, NOT A FINDING, and
     it is filed as the positive direction of the can-fail.  Any row that disagrees
     is an arithmetic fault in gtest83, not physics.

P2 · G-WITHIN, GROSS.  Among penetrating channels (l <= 3) the ladder g(0) < g(1) <
     g(2) < g(3) is violated at SOME Z.  I expect violations to be COMMON, not rare:
     **more than 20 of the 107 rows carry at least one within-sigma inversion.**

P3 · WHERE.  The within-sigma inversions CONCENTRATE at f-channel openings.  Z=57
     (La) and Z=89 (Ac) both carry one.  Filed as the clause I most expect to lose,
     because the sealed walk's tie-break failures are already known to sit there and
     I may simply be re-reading a known result in new coordinates.

P4 · G-ACROSS, THE BAND.  The number of rows where (G-across) FAILS is **between 3
     and 25 of 107.**

P5 · COINCIDENCE.  The g-condition's failure set and the sealed walk's own
     ordering/tie-break failure set overlap on **at least half of the smaller set.**
     If the overlap is near zero the reformulation is measuring something else and
     that must be said.

P6 · THE DOUBT-SITED CONTROL (R82.2).  Trusted region: penetrating channels, l <= 3,
     where delta is a measured property of F_core.  **DOUBTED region: the g channels
     (l=4), whose banked D values are -0.02, -0.01389, -0.01021, -0.00781 — equal to
     the hydrogenic -1/(2n^2) to five decimals.**
     EXPECTATION FILED: these are a FLOOR, not a measurement.  |D + 1/(2n^2)| < 1e-5
     at EVERY Z, with ZERO variation in Z at fixed n.  **I THEREFORE EXPECT THE
     DOUBT-SITED CONTROL TO FAIL** — the instrument cannot measure delta where delta
     is not being computed.  Under R82.2 clause 5 that RESTRICTS the claim to l <= 3
     and does not void it.  If instead the values DO vary with Z, the control passes,
     l=4 enters the trusted region, and P2/P4's bands are void because they were
     filed over l <= 3.

P7 · ROUTE (b), THE RELAXATION IN g-UNITS.  Using s81's frozen-field eigenvalues at
     Z=90 — eps(6d in Phi_d*) = -0.217248225, eps(5f in Phi_d*) = -0.138004359,
     eps(5f in Phi_f*) = -0.227905042 — the 89.901 mHa relaxation term converts to a
     shift in g for the 5f channel of **between 0.20 and 0.60**, and the fixed-field
     g-ladder and the relaxed g-ladder give the SAME verdict at Z=90 (both fail
     G-within).  If the verdicts differ, route (b) is dead for the same reason the
     fixed-field target died.

P8 · ROUTE (a) vs (c).  Route (a) — the statement proved Z by Z — yields NO
     additional information over (c) beyond the per-row verdict list, because (c)
     already evaluates at every Z.  **(a) IS A PRESENTATION OF (c), NOT AN
     ALTERNATIVE TO IT**, and the comparison will say so.

## WHAT THIS CANNOT DO, STATED FIRST

**THIS DERIVES THE EQUIVALENCE, NOT THE BOUND.**  It converts Madelung into a
condition on one scalar function of l built from F_core.  It does NOT show that
F_core must satisfy that condition.  **NO PROPERTY OF F_core IS DERIVED BY THIS
INSTRUMENT.**  Any claim that clause 1 is closed by this file is false.
