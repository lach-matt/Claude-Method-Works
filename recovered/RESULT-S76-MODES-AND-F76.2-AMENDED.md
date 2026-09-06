# RESULT S76c — WHAT THE SCF MAP FORGETS, AND F76.2 AMENDED BY IT.
# Prediction sha256 40b7f4c03a2003adeb90480337eccadbdd788bfaace2d22899e3c4831a334c90, filed first.

## THE DECOMPOSITION
Per record, per candidate: d_i = E_seed(i) - E_sealed(i), over candidates PRESENT IN
BOTH. COMMON = mean(d_i). DIFFERENTIAL = d_i - COMMON.
  **max |DIFFERENTIAL| over all 9 records: 1.560 mHa. At 8 of 9 records: <= 0.062 mHa.**
  Headroom (margin - 2*maxDIFF): **positive at every record, minimum 50.99 mHa.**

## F76.2 IS AMENDED. THE 35.58 mHa WAS AN ARTEFACT AND I FOUND IT ONE STEP LATER.
The records disagree in CANDIDATE-SET SIZE (3, 4, 5 or 9 channels in common). **A
margin is the gap to the runner-up, and where the candidate set differs the runner-up
is a DIFFERENT CHANNEL. F76.2 compared margins measured to different opponents.**
**THE 35.58 mHa IS A CANDIDATE-TRUNCATION ARTEFACT, NOT A DISAGREEMENT ABOUT ENERGY.**
On a common candidate set the seeds agree to **1.560 mHa worst case**.
**F76.2's SEVERITY IS REDUCED FROM STRUCTURAL TO RECORD.** Its surviving content:
ORDER_MATCH 3/9 is real, and the cause is now named -- the ranking changes because the
LIST CHANGES, not because the physics moved. **The obligation it raised STANDS: Z=89
is still unseeded.** And its withdrawal of the 0.005 mHa lean STANDS -- that figure is
still an energy agreement being quoted for a margin.

## THE ANSWER TO THE QUESTION
**WHAT THE MAP FORGETS:** the seed, essentially completely. Initial fields differing by
of order 52 Ha collapse to a **common rigid shift of the whole candidate ladder plus at
most 1.56 mHa of differential structure.** The common mode is the forgotten part and it
is forgotten because the argmin cannot see it -- adding a constant to every candidate
leaves the argmin exactly invariant. **The forgetting is not a defect of the algorithm.
It is the argmin's own gauge freedom.**
**WHAT IS RETAINED:** the DIFFERENTIAL ladder -- the relative spacing of the channels.
**DOES THE RETAINED PART DECIDE THE ANSWER: YES, AND THE CRITERION IS WRITEABLE.**

> **INVARIANCE CRITERION (measured, not proved).** Let D(Z) = max over candidates of
> |differential| between any two reachable fixed points, and m(Z) the argmin margin.
> **If 2*D(Z) < m(Z), the entrant is independent of which fixed point is selected.**
> Measured: D <= 1.560 mHa against a margin FLOOR of 32.330 mHa -- **a factor of 20.7,
> and above 500 at eight of the nine records.** The criterion holds with room.

**THIS IS THE NARROWING.** Griesemer-Hantsch's gap -- infinitely many critical points,
no knowledge of which one an algorithm reaches -- **does not propagate to the physical
decision, because the decision is an argmin and the argmin is blind to the common
mode.** The non-uniqueness is real and is confined to the mode that cannot vote.

## PREDICTION SCORED — 2 OF 4
  M1 COMMON larger than DIFFERENTIAL everywhere . . **WRONG** (differential is larger
     at Z=19 seedA, 1.560 against -0.390, and at Z=20 seedC)
  M2 max|DIFF| below the row's margin everywhere . . **CORRECT**, by 20x to 900x
  M3 the 35.58 mHa is mostly differential . . . . . **WRONG** — it is a candidate-set
     artefact, which is a better answer than the one predicted
  M4 winner's differential not systematically least  **CORRECT**

## LIMITS
Three Z values (19, 20, 39), nine records, three seed modes. **Z=89 IS NOT AMONG THEM
AND IT IS THE ROW THE CRITERION IS TIGHTEST AT.** D(Z) is measured over REACHED fixed
points, not over all critical points; Lions' infinitely many are not sampled and cannot
be by this instrument. **The criterion is MEASURED AT 3 ROWS, NOT PROVED ANYWHERE.**