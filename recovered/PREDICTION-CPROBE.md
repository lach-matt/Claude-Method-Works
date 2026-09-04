# PREDICTION — THE c-SENSITIVITY PROBE (F54.2 REMEDY, PRECONDITION FOR ALL CLAUSE-3 WORK)
# Filed BEFORE any probe row is computed or read. R 1449.
#
# WHY THIS INSTRUMENT EXISTS.  F54.2: every session-53 clause-3 chain -- cinf.jsonl,
# ctrl137.jsonl, induct.jsonl -- was computed at c = 137.035999.  The rebinding in
# pack52/cinf.py and pack53/induct.py patched __defaults__ on t7c_kernel.eigen_sr,
# numerov_wf_sr and scf_occ_sr.  None of the three is on the walk's path:
#   nlguard.py:64   H.HFC(Z, cfg, c=C0)          <- c passed EXPLICITLY, from nlguard's
#                                                   own `from t7c_kernel import C0`
#   t7c_hfsr.py:8   HFSR.__init__(..., c=C0)     -> self.c
#   t7c_hfsr.py:39  eigen_sr(Vf, l, n, 1.0, self.Z, c, ...)   <- POSITIONAL; the default
#                                                                is unreachable
# So the patched defaults were doubly dead.  The single live lever for the walk is the
# module-level name `nlguard.C0`.
#
# THE RULING THIS ENFORCES.  An instrument that varies a parameter must FIRST demonstrate
# that the parameter moves the number.  A null instrument passes every agreement test
# perfectly -- that is its signature, and s53's 21/21 then 34/34 with zero margin drift
# was that signature, not a confirmation.  No clause-3 row may be computed until CP-1
# holds.  This gate is a PRECONDITION, not a result.
#
# METHOD.  One SCF reference solve, through the SAME entry the walk uses
# (nlguard.run_guarded), on the SAME chained reference configuration, at two values of
# nlguard.C0.  No sealed file is modified; C0 is rebound in memory (F44.1 precedent).
# Test atoms: Z=10 (small scalar-relativistic correction) and Z=80 (large).

CP-1  DECISIVE.  |E(c=1e6) - E(c=137.035999)| at Z=80 EXCEEDS 1 mHa (0.001 Ha).
      Reading: the lever is connected and c genuinely moves the object.
      If it does NOT exceed 1 mHa, the lever is STILL not connected, F54.2 is not
      remedied, and NO clause-3 walk may be run.  Reported as such, not reworded.

CP-2  The same difference at Z=10 is STRICTLY SMALLER than at Z=80.  Scalar-relativistic
      corrections scale steeply with nuclear charge; a probe that moved both equally
      would indicate an artefact rather than physics.

CP-3  THE s53 LEVER REPRODUCED AS A NULL.  Patching ONLY the three t7c_kernel defaults
      (eigen_sr, numerov_wf_sr, scf_occ_sr) with nlguard.C0 left at 137.035999 changes
      the Z=80 energy by EXACTLY 0.0.  This confirms F54.2's root cause by direct
      experiment rather than by source reading alone.
      If instead it moves the energy, the root cause is misdiagnosed and F54.2 must be
      re-opened and re-stated.

CP-4  Every solve in this probe converges, at rung 0.

CP-5  The correction is attractive-side consistent: the c=1e6 (non-relativistic) total
      energy is HIGHER (less negative) than the c=137.035999 one at Z=80, since scalar
      relativity contracts and stabilises the s and p core.  Stated as a sign clause and
      scored; a wrong sign is reported as a wrong sign, not explained away.

SCORING: CP-1 alone decides whether clause-3 work may resume.  CP-3 decides whether
F54.2 stands as diagnosed.  A clause reworded to pass is FALSIFIED and recorded as such.
This probe measures NOTHING about the Madelung ordering and must not be reported as if
it did.
