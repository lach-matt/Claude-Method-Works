# PREDICTION — SESSION 82, ITEM 5. R81.7: PROPAGATE F81.1.
# FILED BEFORE THE SCANNER IS WRITTEN AND BEFORE ANY FULL-TREE RESULT IS READ.
# The question: which instruments assume the restart-to-stationarity ladder DESCENDS?

## TIMING FLAG, DECLARED UP FRONT
At s82 open, BEFORE this file existed, a scoping grep was run over `pack75..pack81`
and `rt/` only, to inform M's ruling on sequence. Its output was reported to M. What
that grep established, and what is therefore NOT predicted here:
  * within pack75..81 + rt, sense-3 ladders appear in perturb80.py, perturb81.py,
    fixed81.py and nowhere else;
  * all three stationarity break tests read `abs(E2 - E) < ESTAT`;
  * no external consumer of `drop_mHa` exists within that subtree.
**pack5..pack74 IS UNSCANNED. Every clause below is scored on the FULL tree.**

## THE THREE SENSES, AS CLASSIFIED BEFORE THE SCAN
  S1  nlguard.LADDER — the convergence RUNG ladder (beta, maxit). NOT F81.1's object.
  S2  nlchain 'restart' mode — reference = OBSERVED cfg(Z-1). NOT F81.1's object.
  S3  restart-to-stationarity — repeated run2 seeded from its own P, collecting a list
      of total energies. **THIS IS F81.1's OBJECT AND THE ONLY ONE IN SCOPE.**

## CLAUSES

X1 · **THE ENUMERATION IS EXACTLY THREE FILES, TREE-WIDE.** A full scan of every .py
   under pack5..pack82 and rt/ finds S3 ladders in perturb80.py, perturb81.py and
   fixed81.py, and in NO file from pack5..pack74.
   Rationale: restart-to-stationarity was invented at s80 as F80.2's measurement; before
   s80 the project had no reason to re-seed a converged solve from its own orbitals.
   **RISK, STATED: eigen_fix.py, rung597.py and the early hfc2 work all re-seed solves,
   and any of them could carry the pattern under a different name.** If X1 falls it falls
   here, and a pre-s80 site would be the more serious finding, because it would sit
   UNDER sealed rows rather than beside them.

X2 · **ZERO ONE-SIDED TERMINATION TESTS, TREE-WIDE.** No S3 ladder anywhere breaks on a
   signed comparison (`d < eps`, `E2 - E < eps`, `E2 > E`); every one uses a magnitude.
   A one-sided break is the fault WITH TEETH: on a RISING ladder it either never fires
   or fires at pass 1, and 7p rises. Predicted absent, and this is the clause whose
   falsification would disturb a number rather than a word.

X3 · **THE NAIVE REGEX OVER-MATCHES BY AT LEAST FIVE FILES.** Scanning for the bare
   token `ladder` returns >= 8 files, of which at most 3 are S3. The gap between the
   naive match set and the true set is the measurement of how far the word travelled
   past the thing.

X4 · **ZERO EXTERNAL CONSUMERS OF THE SIGNED QUANTITY.** No file outside the three reads
   `drop_mHa`, so no downstream number was computed from a mis-signed input. This is the
   clause that decides whether F81.1 is a naming fault or a numerical one.
   **PREDICTED: NAMING ONLY.**

X5 · **AT LEAST FOUR NAMING SITES SURVIVE IN THE THREE FILES.** Sites where a signed
   quantity that is measured POSITIVE at 7p is called `drop`, `TOTAL DROP`, `descending`
   or `basin floor`. Predicted 4 to 12.

X6 · **A FOURTH SENSE EXISTS IN pack5..pack74.** At least one pre-s80 file uses
   `restart` or `ladder` for an object that is neither S1, S2 nor S3.
   Filed as the clause I expect to lose: three senses in one project is already
   unusual and I may be pattern-matching on the shape of the last two findings.

X7 · **THE LINT GATE FAILS AGAINST pack81 AS SEALED AND PASSES AGAINST THE CORRECTED
   COPY.** Both directions demonstrated before any verdict is accepted (can-fail law).
   If the gate cannot fail on the sealed source it is not measuring anything.

## WHAT IS *NOT* CLAIMED
This item repairs a VOCABULARY and installs a GATE. **It derives nothing, it disturbs no
sealed row, and it does not close O-C1, F54.1 or clause 1.** If X4 holds, F81.1 leaves no
number wrong anywhere in the project and its whole cost was a word — which is exactly
what the seven-fault species has cost every time and is not a reason to discount it.

## SEALED-FILE RULE
**NO SEALED FILE IS EDITED.** pack80 and pack81 are sealed. The correction is written as
(i) this audit, (ii) a corrected vocabulary carried forward, (iii) a lint gate in pack82
that halts any FUTURE instrument committing the fault. Sealed sites are recorded as
findings, not patched.
