# RESULT S77 — Z=89 RE-SEEDED. THE OBLIGATION FROM F76.2 IS PARTLY DISCHARGED.
# Prediction sha256 e8640c51f8c48dfd2b8cdec7fb4f2e028b261c4728e6d54cb6f75d39bd722a81, filed first.
# Lever verified first: A->B 2.070841 Ha, A->C 51.948837 Ha at the valence. PHASE A PASS.

## HOW IT WAS RUN
Detached jobs do not survive a tool-call boundary in this container (observed, s77), so
phase O was ZENO-SEGMENTED: one guarded solve per invocation, receipts appended, resume
from the receipt file. **The ruling path is untouched** — candidates, reference and every
solve go through nlchain's own helpers and NG.run_guarded. **The driver is validated by
its own output: seed A reproduces the sealed row exactly, so the segmentation is
equivalent to nlchain.step, not merely intended to be.**

## THE THREE SEEDS AT Z=89
| seed | ent | margin mHa | candidates | ENT_MATCH | ORDER_MATCH |
|---|---|---|---|---|---|
| sealed | 6d | 32.330 | 9 | — | — |
| A | 6d | 32.330 | 9 | **TRUE** | **TRUE** (identical to 5 dp, all 9) |
| B | 6d | 32.390 | 5 | **TRUE** | FALSE |
| C | — | — | 0 | **NO DATA** | **NO DATA** |
**SEED C PRODUCED NO DATA AND THIS IS NOT A RESULT ABOUT THE FIELD.** All 15 items,
reference included, failed identically: `RuntimeError: Z=89 50 nodes 3` — the bare-Coulomb
Numerov start finds 3 nodes in 5s where 4 are required. **The failure is in the SEED
CONSTRUCTOR, before any SCF.** Seed C is inapplicable at Z=89.

## THE COMMON-SET MEASUREMENT — WHAT s76 SAID WOULD DECIDE THE QUESTION
Seed B against sealed, over the 5 channels common to both:
  **COMMON mode +0.008000 mHa · max|DIFFERENTIAL| 0.052000 mHa**
  **2*D = 0.104 mHa against m(89) = 32.330 mHa — the criterion HOLDS, headroom
  +32.226 mHa, a factor of 311.** Well inside s76's measured bound of 1.560 mHa.

## PREDICTION SCORED — 4 CORRECT, 1 WRONG, 1 NO-DATA
  P1 seed A reproduces the sealed row exactly . . . . **CORRECT** (all 9 D, margin, nfail)
  P2 ENT_MATCH true at all three seeds . . . . . . . . **CORRECT WHERE TESTABLE**, 2 of 2.
     **The third seed returned no data, so P2 was not put at its full risk.**
  P3 ORDER_MATCH false at B or C . . . . . . . . . . . **CORRECT** (B: 6d 7p 5f 5g 7g)
  P4 candidate set moves . . . . . . . . . . . . . . . **CORRECT, AND AT THE WRONG SEED**
     — predicted at C, occurred at B (9 fails, up from 5). The stated mechanism — node
     count decided by shooting on the seeded functions — is exactly what fired.
  P5 2*D(89) < m(89) on a common set . . . . . . . . . **CORRECT**, by a factor of 311
  P6 the F76.2 raw-margin artefact reappears . . . . . **WRONG — 0.06 mHa raw**, and the
     reason is worth more than the prediction was:

## THE SHARPENING OF F76.2
Seed B truncates the ballot from 9 candidates to 5, yet the raw margin moves by 0.06 mHa.
**Truncation alone does not produce the artefact. The truncation at s76 removed the
RUNNER-UP; this one removed ranks 3 and 4 (8s, 8p) and left ranks 1 and 2 intact.**
**A margin is a two-body quantity. Only a change that touches rank 1 or rank 2 can move
it.** F76.2's 35.58 mHa was therefore not a candidate-set artefact in general — it was a
RUNNER-UP-SUBSTITUTION artefact, which is a narrower and checkable condition.

## F77.2 RAISED — CANDIDATE ADMISSIBILITY IS SEED-DEPENDENT. SEVERITY: STRUCTURAL.
Seed A admits 9 channels at Z=89; seed B admits 5, rejecting 8s, 8p, 6g, 8g on node count
where seed A converged them. **The argmin is taken over a set the seed can change.** At
Z=89 neither the winner nor the runner-up was touched and the entrant is unaffected.
**Nothing in the instrument guarantees that, and no row has been checked for it.** This is
a channel of seed-dependence distinct from the energy spread s76 measured, and s76 did not
see it because it scored ENT_MATCH and ORDER_MATCH, not ADMISSIBILITY.
  *Bounding observation, not a proof: a seed can only change the entrant by deleting the
  winner, and a deleted channel is one whose node count the shooting could not satisfy —
  a failure to FIND the state, not a statement that it lies higher.*

## WHAT IS NOW TRUE, AND WHAT IS NOT
**TRUE: the entrant at the tightest of all 107 rows survives every seed that produced a
field, and the differential spread there is 622 times smaller than the margin.**
**NOT TRUE: that Z=89 has been tested at full strength.** The 52 Ha probe is unavailable
at Z=89. The falsifier applied here is the 2 Ha one. **The obligation from F76.2 is PARTLY
discharged: Z=89 is re-seeded, but not by the strongest instrument, and Z = 56, 39, 72,
90, 19 remain.** Nothing is proved. One row survived one weakened falsifier.