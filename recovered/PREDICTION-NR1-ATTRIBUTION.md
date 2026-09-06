# PREDICTION — NR-1 ATTRIBUTION: THE FIVE ORDERING FLAGS AT c = 137.035999
# Session 59. Filed BEFORE any control row at Z = 42,43,45,46,79 is computed or read. R 1449.
#
# INSTRUMENT: the SEALED rt/nlchain.py in 'restart' mode, unpatched, c at its default
# 137.035999 -- the identical invocation pack53/ctrl137.sh used for the 11 NR-4 steps
# ('python3 nlchain.py restart <Z>').  Reference configuration = OBSERVED config(Z-1),
# the same reference cinf.py used, so the ONLY difference from the c=1e6 walk is c.
#
# WHY THIS IS A SOLVE AND NOT A READ (F59.1): the s58 bridge item 2 stated the control
# "is pack53/ctrl137.jsonl, ALREADY SEALED. Cost: a read, not a solve."  ctrl137.jsonl
# holds 11 rows, Z = 25 30 47 48 60 61 62 71 80 103 104 -- the NR-4 steps ONLY.  A
# content search of all 232 sealed .jsonl files returns ZERO restart-mode rows at
# Z = 42,43,45,46,79.  The gap is real and was declared only after the search.
#
# BASELINE BEING TESTED AGAINST (sealed, pack53/cinf.jsonl, clight=1e6, mode cinf):
#   Z=42 ent 4d / runner-up 5s      Z=43 4d / 5s      Z=45 4d / 5s
#   Z=46 4d / 5s                    Z=79 5d / 6s
#
# ---------------------------------------------------------------------------
# NR1-1  DECISIVE.  At all five Z the c=137.035999 restart control returns the SAME
#        entrant AND the SAME runner-up channel identity as the c=1e6 restart walk.
#        READING: the NR-1 ordering flag is carried by the REFERENCE CONFIGURATION,
#        not by c.  The count of c-attributed ordering failures over Z=2..108 is ZERO,
#        and CLAUSE 3 CLOSES.
#        FALSIFIER, STATED IN ADVANCE: if at ANY of the five the entrant or the
#        runner-up identity DIFFERS from the c=1e6 row, that row IS a c-effect, NR-1
#        becomes a live ordering failure there, and Clause 3 does NOT close.  The
#        clause will NOT be reworded to survive.  A reworded clause is FALSIFIED.
#
# NR1-2  At each of the five the runner-up is the LOWER n+l s channel -- 5s (n+l=5)
#        against entrant 4d (n+l=6) at Z=42,43,45,46; 6s (n+l=6) against 5d (n+l=7)
#        at Z=79.  This is what makes the row cross-n+l and therefore EXPOSED in the
#        restart walk while it is IMMUNE in the sealed chained walk.
#
# NR1-3  The MARGINS will differ numerically between c=137.035999 and c=1e6 -- scalar-
#        relativistic contraction is a real effect and is not predicted to vanish.
#        The ORDER is predicted unchanged despite it.  |delta margin| is predicted to
#        be LARGEST at Z=79 and smallest among the 4d four, being a Z-scaling effect.
#        If the order flips anywhere, NR1-1's falsifier has fired and NR1-3 is moot.
#
# NR1-4  All five converge; each returns at rung 0, as all 11 control rows did.
#
# NR1-5  CROSS-CHECK, decides the ATTRIBUTION rather than the reproduction.  In the
#        sealed CHAINED walk (rt/nlchain.jsonl, mode 'chain') the same five Z carry
#        entrant/runner-up of EQUAL n+l -- 4d/5p at 42,43,45,46 and 5d/6p at 79.
#        Same c, same code, DIFFERENT reference => different flag.  Different c, same
#        reference => same flag.  Those two together, and only those two together,
#        attribute the flag to the reference configuration.  NR1-1 alone does not.
#
# SCORING: NR1-1 decides Clause 3.  NR1-5 is what converts "reproduces" into
# "attributed".  Any clause failing is recorded FALSIFIED with its measured values.