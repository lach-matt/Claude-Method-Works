# F66.2 — PD-0 WAS SPECIFIED AGAINST A ROUNDED REFERENCE AND CANNOT PASS
# Raised 2026-08-20, SESSION 66, immediately on reading PD-0's number and BEFORE any
# cell of T-D was run. The prediction is sha-sealed and IS NOT EDITED.
# The fault is mine, in the writing of the prediction, not in the instrument.

## WHAT WAS FILED
`PREDICTION-T-D.md` PD-0: "the chain D reproduces the banked -0.26664 to
|d| <= 3e-6 (s42's own tolerance after F42.2). If it raises or drifts, T-D DOES NOT
RUN and nothing below is scored."

## WHAT WAS MEASURED

    nodespec D          -0.266643170        it=[30,35], 8 s, no raise (inert)
    banked (5 dp)       -0.26664            |d| = 3.170e-06   -> FAILS the filed gate
    s42 printed (6 dp)  -0.266643           |d| = 1.699e-07
    round(D, 5)         -0.26664            EXACT match to the banked value

## THE DEFECT
The banked number is stored at five decimal places and is therefore quantised at
1e-5. **Storage rounding alone admits |d| up to 5e-6.** A tolerance of 3e-6 against a
5-dp reference is unsatisfiable by any correct instrument roughly forty per cent of
the time, whatever it computes. The 3e-6 figure was lifted from
`FINDING-REPAIR-4D.md` §0, where s42 reported the SAME discrepancy as "|d| = 3e-6" —
s42 rounded 3.17e-6 down to one significant figure and called it a PASS. **I used
s42's rounded statement of the discrepancy as a BOUND on the discrepancy.** That is
circular and self-defeating: the gate was set at the value it was meant to admit.

## WHAT THE MEASUREMENT ACTUALLY SHOWS
The instrument is inert. It reproduces s42's own six-decimal value to 1.7e-7, and it
reproduces the banked value exactly once quantised to the precision the bank stores.
`NodeSpec` did not raise on the healthy 3d channel, which is the substance of PD-0.
**The physics gate passed; the arithmetic gate as written could not.**

## WHAT IS NOT DONE
`PREDICTION-T-D.md` is NOT edited — it is hashed and filed (sha 774d9d5f…, 22:55:53Z)
and a sealed prediction is not rewritten after its first number is read. No cell of
T-D has been run. `nodespec.jsonl` holds no cell rows. R 1449 intact.

## STATUS — M'S RULING OWED
  (a) LITERAL. PD-0 is scored FAILED-AS-WRITTEN and T-D does not run this session.
      The prediction said so and the prediction governs.
  (b) SUPERSEDE. PD-0 is scored FAILED-AS-WRITTEN and entered as such in the record,
      AND a correctly-specified inertness gate is filed as an AMENDMENT with its own
      sha before any cell runs:
          PD-0' : NodeSpec does not raise on Z=21 3d, AND round(D,5) equals the
                  banked -0.26664 exactly, AND |D - s42's -0.266643| <= 1e-6.
      This is not a loosening applied after the fact — the failure stands in the
      record, and the replacement is filed, hashed and can-failed like any other.
  **RECOMMENDED: (b).** Under (a) the session ends having proved only that a badly
  written tolerance is badly written. But it is M's call, and the failure is entered
  either way.
