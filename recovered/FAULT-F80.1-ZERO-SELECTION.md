# F80.1 — WHEN THE TARGET-NODE ZERO SET HAS TWO MEMBERS, BOTH s79's INSTRUMENT AND THIS
# ONE SELECTED SILENTLY, BY THE ORDER OF THEIR OWN geomspace ARGUMENTS. THEY SELECTED
# OPPOSITE MEMBERS. SEVERITY: THE SELECTED STATE DECIDES THE ANSWER.
# RAISED AND CLOSED IN THIS SESSION, ON THE SELF-CONSISTENCY CRITERION.

## THE UNDIAGNOSED FACT s79 LEFT ON THE TABLE
pack79/RESULT-S79-ITEM2 recorded `sign_changes = 2` on all three f channels and filed it
as *"undiagnosed"*: two energies carrying the target node count with nrm = 1. It then
stated that refine79 *"bisects the FIRST, which is the more bound"*, and reasoned that
taking the more bound made the conclusion conservative.

## WHAT WAS NOT SEEN: "FIRST" IS NOT A PROPERTY OF THE FIELD
refine79 builds `es = -geomspace(abs(lo_e), abs(hi_e))` with `lo_e = win[0]*PAD` — the
MORE bound end — so its scan runs most-bound to least-bound and its first crossing is the
MORE bound zero. de80's first draft built the same expression with the arguments in the
opposite order, so its first crossing was the LESS bound zero. **Neither instrument
declared an orientation. The two differ at 6f by 11.6 mHa, and the choice was made by
argument order, not by any stated rule.**

## THE REPAIR, DECLARED AS G6 AND G7
G6: every crossing is bisected, not the first; the scan returns the WHOLE zero set,
sorted most-bound first, and `n_zeros` and `spread` are recorded on every firing.
G7: selection is an explicit argument, `most-bound` or `least-bound`, and **BOTH WERE
RUN.** Method §2.24: a single heuristic cannot tell you whether you are in the case where
it works — run two and report the SPREAD.

## THE SPREAD, AND IT IS NOT A SPREAD — IT IS A DISQUALIFICATION
| ch | most-bound | least-bound |
|---|---|---|
| 6f | **NO SCF.** RuntimeError node count, fb=7 on the wide window | conv, 83 it, dE = **-0.020486** |
| 7f | **NO SCF.** RuntimeError node count, fb=3 | conv, 86 it, dE = **-0.014282** |
| 8f | **NO SCF.** the target-node zero set becomes EMPTY as the field drifts | conv, 85 it, dE = **-0.010528** |
**The more-bound branch does not support a self-consistent field at any of the three
channels. The less-bound branch converges at all three, in one fallback firing.**
The most-bound failure was re-run with the G3 warm start DISABLED and fails identically,
so it is not an artefact of the narrow window. **The instrument REFUSES rather than
coerces (§2.9): it returns a state whose node count is not the target and run2 raises.**

## AND s79's OWN FLAGGED ANOMALY IS THE SYMPTOM, NOW RESOLVED
s79 recorded, not buried: *"6f AT -0.031600 IS 0.140 mHa MORE BOUND THAN SEALED 5f AT
-0.03146. Within one fixed field min-max forbids that ordering."* It was excused because
the two are different SCF fields. **On the surviving branch the anomaly does not arise:
6f dE = -0.020486 is 10.98 mHa LESS bound than 5f dE = -0.031463, which is the ordering
min-max wants.** The flag was pointing at the selection, and it was right.

## WHAT IS WITHDRAWN
**pack79's three f eigenvalues — -0.031600440, -0.020275522, -0.014084998 — are the
MORE-BOUND branch and are withdrawn as descriptions of the 6f/7f/8f states of the
self-consistent field.** They remain correct as what they were measured to be: zeros of
log(nrm) at the target node count in the iteration-1 field. **They are not the states the
field converges on.** Every margin s79 computed from them is superseded by §the result.
s79's item-2 verdict — entrant unchanged, ranks 1 and 2 untouched — SURVIVES, and is
now carried by dE rather than by eigenvalues.

## THE SPECIES, AND IT IS THE SAME ONE AGAIN
F78.1: read the raise, not the sentence. F79.1: read the instrument, not the label on its
output column. F79.2: read the units. **F80.1: READ WHICH ONE IT PICKED, AND WHY.** Four
faults in three sessions, one species — a number carried forward under a name that did not
describe it. **Here the name was "the" target-node zero, and there were two.**

## TIMING FLAG, DECLARED
**G6 and G7 were written AFTER the first 6f run returned a zero that disagreed with
refine79's.** The design decision followed a numerical result and is flagged as such. The
prediction file was NOT edited; its sha gate held across the amendment, and C2 was
re-run against the amended code path and passed before any question run was scored.
