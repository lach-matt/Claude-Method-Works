# PREDICTION — CLAUSE 3 RESUMED AT A GENUINE c = 1e6 (FAIL-FAST SEGMENT)
# Filed BEFORE any row of this walk is computed or read. R 1449.
#
# PRECONDITION MET.  cprobe.py scored PREDICTION-CPROBE.md (db654c3d23fba6eb...) and
# returned PASS on all five clauses: |dE| = 1206.45 Ha at Z=80, 0.1457 Ha at Z=10, ratio
# 8282, correct sign, rung 0.  The lever is nlguard.C0.  s53's lever moved the Z=80
# energy by EXACTLY 0.0 and is dead (F54.2, confirmed by experiment).
#
# WHAT IS BEING TESTED.  Whether the ORDERING CLAUSE -- the entrant chosen at each step --
# survives c -> infinity.  If it does, the ordering clause is derived from the
# NON-RELATIVISTIC field and Deliverable 1 §6.1 may be struck.  If it does not, §6.1
# stands and the derivation remains scalar-relativistic.  Nothing about the tie-break
# clause is claimed here.
#
# WHY A SUBSET, AND WHY THIS SUBSET.  A full chained c=1e6 re-walk costs ~2.8 hours.
# Falsification is cheap and confirmation is expensive, so the steps most likely to
# invert are run FIRST.  The selection rule is fixed here, before any row:
#
#     the eight steps with the SMALLEST SEALED MARGIN among Z >= 55.
#
# Margin is the gap between the winning channel's depth and the runner-up's.  A step with
# a small margin is one a perturbation of any size can invert; a step with a large margin
# is not.  Restricting to Z >= 55 selects where the scalar-relativistic correction is
# large.  The rule is mechanical and was applied to the SEALED chain, not to any c=1e6
# result.  It yields:
#
#     Z = 55 (6s, 0.06306)  56 (6s, 0.03914)  57 (5d, 0.06756)  72 (5d, 0.04507)
#         88 (7s, 0.05816)  89 (6d, 0.03233)  90 (6d, 0.05405)  105 (6d, 0.05440)
#
# These include every 6s/5d and 6d/7s competition in the chain -- exactly the pairs where
# relativistic s-contraction and d-expansion act in OPPOSITE directions and are therefore
# most able to reorder.  If c -> infinity is going to break the ordering anywhere, the
# prior expectation is that it breaks here.
#
# METHOD.  nlchain.step on the CHAINED reference cfg_from_chain(Z-1), with nlguard.C0
# rebound to 1e6 in memory.  Identical in every other respect to the sealed walk.  No
# sealed file is modified.

C3-1  DECISIVE.  At all eight steps the c=1e6 entrant EQUALS the sealed entrant.
      Reading: the ordering clause survives c -> infinity at the steps most able to
      break it, and the full 107-row confirmation walk is worth its 2.8 hours.
      If ANY step returns a different entrant, clause 3 is answered NEGATIVELY at that
      step, Deliverable 1 §6.1 STANDS, no further rows are needed for that verdict, and
      the disagreeing Z is reported as the counterexample it is.

C3-2  Margins MOVE, and by amounts far larger than the zero of s53's null instrument.
      At least one of the eight steps shows |margin(c=1e6) - margin(sealed)| > 1 mHa.
      This is the clause that would have caught F54.2 and is stated so that it can.

C3-3  The 6s and 7s steps (55, 56, 88) show their margins WIDEN or their entrant depths
      shift LESS negative on removing relativity, since scalar relativity stabilises s
      channels; the 5d and 6d steps (57, 72, 89, 90, 105) shift in the opposite sense.
      A sign clause, scored per step and reported as measured.

C3-4  Every solve converges at rung 0.

C3-5  No candidate SET differs from the sealed step's candidate set.  The reference is
      chained and identical by construction, so a difference here would indicate an
      instrument fault, not physics (F53.2's confound, which this design excludes).

SCORING: C3-1 decides whether the full walk is run.  A clause reworded to pass is
FALSIFIED and recorded as such.  Eight steps holding does NOT close clause 3 -- it
licenses the remaining 99.  This will not be reported as closure.
