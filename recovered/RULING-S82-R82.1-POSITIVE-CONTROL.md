# RULING-S82 — R82.1. ISSUED BY M AT s82, ON THE F82.1 PROPOSAL. **BINDING.**

## R82.1 · THE POSITIVE CONTROL. A CAN-FAIL SUITE MAY NOT BE DRAWN ENTIRELY FROM THE
## INSTRUMENT'S OWN ASSUMPTIONS.

**ANY DETECTOR THAT SCANS THE CORPUS MUST INCLUDE, AMONG ITS CAN-FAILS, AT LEAST ONE
REAL FILE DRAWN FROM THE CORPUS WHOSE VERDICT IS ESTABLISHED BY INSPECTION BEFORE THE
DETECTOR IS RUN.**

**THE BASIS, MEASURED AND NOT ARGUED.** F82.1's third draft missed a third of its targets
and mislabelled the missing file as external to itself. **All five synthetic can-fails
passed.** They passed because they were written by the same hand, from the same picture,
that made the detector blind. A synthetic can-fail tests whether the instrument does what
its author intended; it cannot test whether the author's intention covered the corpus.

**WHAT COUNTS AS A POSITIVE CONTROL.**
  1. It is a **REAL FILE** already in the tree — not written for the test.
  2. Its verdict is **ESTABLISHED BY INSPECTION AND WRITTEN DOWN BEFORE the detector
     runs against it.** A verdict formed after seeing the detector's output is not a
     control; it is a rationalisation.
  3. **BOTH DIRECTIONS ARE REQUIRED**: at least one real file that MUST be flagged, and
     at least one real file that MUST NOT be — the second drawn from the near-miss set,
     the files that a naive version of the detector would wrongly catch.
  4. It **GATES**. A failing positive control halts the run, exactly as a synthetic
     can-fail does.

**THIS EXTENDS THE CAN-FAIL LAW; IT DOES NOT REPLACE IT.** Synthetic can-fails still run
and still gate — they are the only way to exhibit a fault the corpus does not happen to
contain. R82.1 adds the direction the synthetics cannot cover.

**SCOPE.** Every corpus-scanning detector from s82 onward. **f811.py is retrofitted
immediately**, and its scored result is re-verified under the retrofit before ITEM 5 is
allowed to stand as closed.

**THE STANDING LINE, EXTENDED.** Read the units · read which one it picked · read whether
the instrument can see what it claims · read whether a direction was measured or assumed ·
read what the patch actually replaced · **and read whether the test that proves the
instrument can see was drawn from the same picture that made it blind.**
