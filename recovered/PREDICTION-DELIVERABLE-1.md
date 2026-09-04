# PREDICTION — DELIVERABLE 1 (THE ORDERING CLAUSE AS A STANDING DOCUMENT)
# Filed $TS, BEFORE nlchain.jsonl or the cfg mismatch set is read this session.
# R 1449. Scored after the fact. Corrections go to the expectation, never the data.

CARRIED, NOT PREDICTED (already read this session, from bridge 51 and gate 83):
  ordering clause 0 failures in 119 steps; cfg 73/107; ok 96/107; cfg_first 24;
  ok_first 25; tie-break failures {57, 89, 90}.

D1-1  THE CFG MISMATCH SET IS 34 STEPS AND ITS FIRST MEMBER IS Z=24 (Cr).
      gate 83 reports cfg_first 24. Predicted: 107 - 73 = 34 mismatched steps.

D1-2  EVERY CFG MISMATCH IS A PROMOTION, NEVER AN ORDERING VIOLATION.
      The intersection of the cfg mismatch set with the ordering-failure set is EMPTY.
      Strong form: the ordering-failure set is empty outright, so this holds trivially;
      the testable content is that no mismatched step carries a wrong n+l ENTRANT.

D1-3  THE ok-FAILURE SET (11 STEPS) IS A SUBSET OF THE CFG MISMATCH SET (34).
      A step cannot fail the walk score while its configuration agrees.

D1-4  THE CFG MISMATCH SET PERSISTS WITHIN A BLOCK ONCE OPENED.
      34 exceeds the count of NIST-anomalous elements (~20). Predicted cause: after a
      promotion the walk's running configuration stays offset from the observed one for
      subsequent steps in the same block until the block closes. Mismatches therefore
      arrive in RUNS, not as isolated singletons. Predicted: >= 4 runs of length >= 2.

D1-5  THE 3d AND 4d BLOCKS EACH CONTRIBUTE A RUN; THE 4f AND 5f BLOCKS CONTRIBUTE THE
      LARGEST RUNS. Predicted: the single longest run lies in the 5f block (Z 89-103).

D1-6  cfg_first (24) < ok_first (25).
      The configuration column fails one step EARLIER than the walk score. If true, the
      two columns demonstrably measure different objects, which is the clause-2 finding.

SCORING RULE: a clause HOLDS only if the sealed chain shows it without reinterpretation.
A clause that must be reworded to pass is FALSIFIED and recorded as such.