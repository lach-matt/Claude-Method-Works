# PREDICTION — THE 13 EXPOSED ROWS AT A GENUINE c = 1e6
# Session 59. Filed BEFORE any row is computed with the corrected patch. R 1449.
# Instrument: pack59/cinf2.py, can-failed 2026-08-20 (PATCH OK sites=4,
# HFSR.self.c=1000000.0, Z=79 1s shift 314.08 Ha). Sealed nlchain.py, restart mode.
#
# SCOPE, AND WHY IT IS 13 AND NOT 107: F55.2's immunity theorem is COMBINATORIAL --
# a reversal between two channels of EQUAL n+l is a within-shell event and cannot reach
# the ordering clause. 94 of 107 rows have entrant and runner-up sharing n+l. That
# holds whatever c does and is untouched by F59.3. The exposed set is exactly:
#   Z = 2, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88   (all s-closing rows)
#
# BASELINE (sealed chained walk, c=137.035999) ent/runner-up, margin in Ha:
#   2  1s/2s 0.69553   3  2s/2p 0.06767   4  2s/2p 0.09634   11 3s/3d 0.12650
#   12 3s/3p 0.09346   19 4s/4p 0.05411   20 4s/4p 0.06058   37 5s/4d 0.07991
#   38 5s/5p 0.05639   55 6s/5d 0.06306   56 6s/5d 0.03914   87 7s/6d 0.06841
#   88 7s/7p 0.05816
#
# EX-1  DECISIVE. At all 13 rows the entrant at c=1e6 is the SAME as at c=137.035999.
#       READING: the ordering clause is not a relativistic effect anywhere it could be
#       one, and CLAUSE 3 CLOSES.
#       FALSIFIER: any row whose entrant CHANGES is a genuine c-effect on the ordering
#       clause. Clause 3 does NOT close, and that row is reported as the counterexample.
#       No rewording. A clause reworded to pass is FALSIFIED.
#
# EX-2  Margins WILL move, and unlike NR1-3 this is now testable: the instrument is
#       can-failed. Predicted |delta margin| RISES with Z, largest at Z=87/88, smallest
#       at Z=2,3,4. If |delta margin| is 0.00000 anywhere above Z=20, the instrument is
#       suspect AGAIN and the run HALTS -- F59.3's signature.
#
# EX-3  Z=56 (6s/5d, margin 0.03914) is the tightest row in the exposed set and is the
#       most likely single flip. Z=55 and Z=87 (both s/d) are next by the same logic.
#       If exactly one row flips, EX-3 predicts it is Z=56.
#
# EX-4  The four s/d rows (37, 55, 56, 87) shift MORE than the s/p rows of comparable Z,
#       d channels being more sensitive to the core contraction that c controls.
#
# SCORING: EX-1 decides Clause 3. EX-2 is the instrument's own live can-fail and must
# be read BEFORE EX-1 is scored.