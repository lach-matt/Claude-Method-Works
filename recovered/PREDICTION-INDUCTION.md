# PREDICTION — THE INDUCTION TEST FOR CLAUSE 3
# Filed BEFORE any chained-reference c=1e6 row is computed or read. R 1449.
#
# WHY THIS INSTRUMENT EXISTS. NR-1 is stated over the whole chain and gate 87 could not
# test it, because cinf.py walks in RESTART mode against a CHAINED sealed walk and the
# reference configurations differ at 34 of 107 steps. The obvious remedy -- a full
# chained c=1e6 re-walk -- costs ~2.8 hours. It is also more than the claim needs.
#
# THE ARGUMENT. The walk is deterministic in its reference: config(Z) = config(Z-1) plus
# the entrant, and the entrant is a function of (Z, config(Z-1), c). So if at EVERY Z the
# chained reference cfg_from_chain(Z-1) yields the SAME entrant at c=1e6 as it does at
# c=137.035999, then by induction on Z the chained c=1e6 walk reproduces the sealed chain
# ROW FOR ROW -- identical entrants, identical candidate sets, identical ordering score.
# NR-1 then follows rigorously rather than by re-measurement.
#
# At the 73 steps where cfg_from_chain(Z-1) == OBSERVED(Z-1), cinf.py has ALREADY supplied
# the c=1e6 side and it agreed at 73 of 73. Only the 34 confounded steps are untested:
#   25 30 42 43 45 46 47 48 60 61 62 63 64 66 67 68 69 70 71 79 80
#   92 93 94 95 96 97 98 99 100 101 102 103 104
# This test computes those 34 at c=1e6 ON THE CHAINED REFERENCE. Sealed files untouched;
# c is rebound as a default argument exactly as pack52/cinf.py does (F44.1 precedent).

IN-1  DECISIVE. At all 34 steps the chained-reference c=1e6 entrant equals the SEALED
      entrant. With the 73 already agreeing, the induction closes over all 107 steps and
      the chained c=1e6 walk is proved identical to the sealed chain without running it.
      If ANY step disagrees, the induction FAILS at that step, the full chained re-walk
      becomes mandatory from that Z onward, and that is what will be reported.

IN-2  The ordering clause holds at every one of the 34 rows in its own right: no
      admissible channel of lower n+l is left unchosen. Unlike the restart walk, the
      chained reference has no s-hole, so the 5s/6s artefacts of Z=42,43,45,46,79 must
      NOT appear here. Their absence is the direct confirmation of CT-2.

IN-3  The tie-break failures within this set are exactly those the sealed chain carries:
      none of 25..104 outside {89, 90} -- and 89, 90 are not in this set, so the
      predicted count of tie-break failures among these 34 rows is ZERO.

IN-4  Margins shift but never invert. |margin(c=1e6) - margin(sealed)| stays below the
      sealed margin at every one of the 34 steps, which is what "no inversion" means
      quantitatively. Largest shifts at Z >= 92.

IN-5  Every row converges at rung 0, as both prior walks did at all 118 rows computed.

SCORING: IN-1 decides whether clause 3 closes this session. A clause reworded to pass is
FALSIFIED and recorded as such. If IN-1 holds, what closes is NR-1 as originally stated;
the post-hoc clean-subset partition of gate 87 remains post-hoc and is not promoted.
