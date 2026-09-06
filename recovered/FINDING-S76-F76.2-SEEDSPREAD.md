# F76.2 — THE SEED SPREAD IS THE SAME SIZE AS THE ARGMIN MARGIN.
# SEVERITY: STRUCTURAL. TOUCHES NO SCORED ENTRANT. RAISED BY ME, AT MEASUREMENT.
# Prediction sha256 6fa522e14d84e809e3718e5523e364831ff7eb0bcc54bde61ccec34bac6b505d filed first.

## MEASURED (seedO.jsonl: modes seedA/B/C, Z = 19, 20, 39, 9 records)
  ENT_MATCH   9/9   — the entrant never moved.
  ORDER_MATCH 3/9   — the RANKING BELOW THE WINNER moved in two thirds of records.
  |d margin| vs sealed:  min 0.0000 · median 1.9500 · **max 35.5800 mHa**
  records above 1 mHa: 5 of 9.   **records above 32.33 mHa: 2 of 9.**

## PREDICTION SCORED — 3 OF 4
  Q1 ENT_MATCH 100% . . . . . . . . . . . . . . **CORRECT**
  Q2 ORDER_MATCH lower than ENT_MATCH . . . . . **CORRECT** (3/9 against 9/9)
  Q3 spread exceeds 0.005 mHa, max above 1 mHa . **CORRECT** (median 1.95, max 35.58)
  Q4 max |d margin| stays below 32.33 mHa . . . . **WRONG — it is 35.58**

## WHAT THIS DOES TO THE SELECTION RULE DRAFTED THIS SESSION
POSITION-S76-SELECTION-RULE.md §4 leaned on the seed study — "0.005 mHa from 52 Ha
away" — as evidence that which critical point the algorithm lands on does not matter.
**THAT EVIDENCE DOES NOT SUPPORT THAT CONCLUSION AND I WITHDRAW THE LEAN.**
  * **0.005 mHa is an ENERGY agreement. 35.58 mHa is a MARGIN disagreement. They are
    different quantities and the first must never again be quoted for the second.**
  * The natural robustness lemma — *if the spread of reachable critical points is
    below half the margin, the argmin is independent of which one is selected* — is
    **FALSIFIED ON OUR OWN DATA AT THE SCALE THAT MATTERS.** The spread reaches
    35.58 mHa; the tightest chain margin is 32.330 mHa. The lemma's hypothesis fails.
  * **THE ENTRANT NEVERTHELESS NEVER MOVED, 9 of 9.** The decision is more stable than
    the bound that would have explained why it is stable. **That gap between what is
    observed and what can be argued is now the honest statement of Step 0(ii).**

## LIMITS OF THIS FINDING, STATED SO IT IS NOT OVERSOLD
Three Z values, nine records, three seed modes. **This is not a survey of the 107
rows and must not be reported as one.** None of the three rows measured is the
tightest row; Z=89 was NOT re-seeded. **The one measurement that would decide the
question — re-seeding Z=89, margin 32.330 — HAS NOT BEEN RUN.**

## THE OBLIGATION THIS CREATES
Re-seed the tight rows: Z = 89, 56, 39, 72, 90, 19. If the entrant survives every
seed at Z=89 the observation stands and the explanation is still missing. **If it
flips at any seed, the selection rule is not a formality — it is load-bearing on the
result itself, and Deliverable 1 inherits a dependency it does not currently declare.**