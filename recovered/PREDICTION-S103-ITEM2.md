# PREDICTION S103 ITEM 2 (amended per RULING-M-S102-POST-SEAL) -- hashed BEFORE any arithmetic.
# Object: defect(q) = dE_SCF/dq - g(q)  [d101.py line 3 convention; g = frozen-functional gradient,
# ts93 g_of == d101 g_frozen, confirmed from source]. ONE function; sealed exposures at ts93 5pt nodes.
## OBS-S103-1 (frame, filed before run; F-candidate vs S102 RESULT framing, NOT vs the ruling's
## operative demand): T1 = quad - D = Gauss5(g) - D = -Gauss5(defect) + O(<1e-7) [Gauss error bounded
## empirically: quad3-quad5 < 1e-7 all rows/systems]. The sealed NEGATIVE integrated column is the
## integral of MINUS defect. In the one-function frame both exposures are predicted POSITIVE:
## integrated exposure -T1 = +5.9e-5 (90-A), +4.1e-5 (91-A), +9.5e-5 (58-B);
## midpoint exposure (d101 fresh) = +3.329e-5, +5.774e-5, +9.01e-5. The premise "sign change of
## defect(q) across the interval" is predicted to be a sign-convention artifact of the T1 column.
## The node derivation decides (comparison decides).
## RULE B LINES (inequality, direction, exactness -- per row, systems 90-A, 91-A, 58-B):
## P1 SUM (sign-exact + value-window): Gauss5-weighted sum of node defects > 0 AND within
##    [-T1 - 3e-5, -T1 + 3e-5]. Targets: +5.9e-5 / +4.1e-5 / +9.5e-5. THIS IS THE CAN-FAIL:
##    ~21 fresh SCF solves per row must combine through derivative stencils to reproduce a sealed
##    number they never saw. Non-vacuous: a wrong stencil or drifted solve breaks the sum.
## P2 MIDPOINT (value-exact, tol 2e-5): defect(0.5) = +3.329e-5 / +5.774e-5 / +9.01e-5 (d101 R1).
## P3 CROSSING (sign-exact, scores the ruling premise): defect(q_i) > 0 at ALL five nodes, all three
##    rows -- NO interior crossing. Falsifier: any node < -2e-5 (below FD noise floor) at 90/91
##    establishes a REAL crossing; P3 then entered FALSIFIED with the node located and OBS-S103-1
##    withdrawn in part.
## P4 SHAPE (direction-only, from integral-vs-midpoint asymmetry): 90-A (sum > midpoint) -> at least
##    one edge node (q=.047/.953) defect ABOVE midpoint defect; 91-A (sum < midpoint) -> at least one
##    edge node BELOW midpoint defect.
## INSTRUMENT w103.py: g(q_i) read from SEALED ts93-*-5pt receipts (the exposure object; own g_frozen
##    printed at midpoint as cross-check only). dE/dq stencils: interior nodes + upper edge (.953):
##    d101 Richardson central h=0.2/0.1 (q+0.2 <= 1.153 = 6d occ 1.15, capacity 10, legal in setq);
##    lower edge (.047): 5-point one-sided forward O(h^4), h=0.1. Zeno: one row per call, foreground,
##    per-solve receipts printed. Sealed files untouched; all output pack103/.