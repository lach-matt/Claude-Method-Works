# F61.1 — THE SEALED CHAIN IS HETEROGENEOUS IN CONSTRUCTION AT Z<=56
# Raised 2026-08-20T17:26Z by the seed test's OWN identity control, before any seed
# variant was read. Registered before scoring. Standing 8 (s60) is what caught it.

## WHAT HAPPENED
`pack61/seedtest.py O 19 A` re-runs the Z=19 chain step with the BASELINE seed — the
sealed construction, nothing varied. It should reproduce the sealed row exactly. It did
not reproduce the margin:

    channel   sealed        harness A     delta
    4s       -0.14774      -0.14774       0.00000   BIT-IDENTICAL   (entrant)
    3d       -0.05807      -0.05807       0.00000   BIT-IDENTICAL
    4d       -0.03282      -0.03282       0.00000   BIT-IDENTICAL
    4f       -0.03125      -0.03125       0.00000   BIT-IDENTICAL
    4p       -0.09363      -0.09558      -0.00195   DIFFERS, 1.95 mHa

    entrant 4s = 4s. Order 4s,4p,3d,4d,4f = identical. margin 0.05411 -> 0.05609.

## CAUSE — NOT THE SEED, AND NOT A DEFECT IN THE HARNESS
4p is the ONE channel at this row that the guard has to rescue: the harness reports it
converging at **rung 1** of nlguard.LADDER, every other channel at rung 0. The sealed
Z=19 row carries **`rung_ref: None`** — it has no rung fields at all, because it was
walked BEFORE nlguard was wired into nlchain at s48 (F47.2's repair).

Pre-guard, a channel that cycled to maxit had its last iterate taken as a value.
Post-guard, `run_guarded` re-runs it with different (beta, maxit) and returns a converged
number, or refuses. **The 1.95 mHa is the size of F47.2's repair at this channel.** The
guarded number is the better one; the sealed one was never converged.

## SCOPE — SURVEYED, NOT ASSUMED (counts and sets, Standing 5)
    rows total                        119
    PRE-GUARD, no rung_ref             55   Z = 2..56, contiguous, no gaps
    GUARDED                            64   Z = 57..120, contiguous
    pre-guard rows scoring ok=True     50
    pre-guard rows scoring ok=False     5
The split is clean at Z=57, exactly where the walk resumed after s48.

## WHAT THIS DOES AND DOES NOT TOUCH
DOES NOT touch the entrant at Z=19: 4s wins by 54-56 mHa either way, and the four
channels that did not need the guard are bit-identical to the last digit — which is also
a determinism result, a second independent one this session after F60.2's receipt B.
DOES mean **any MARGIN quoted from a row in Z=2..56 may carry a milli-Hartree-scale
artifact in any channel that needed the guard**, and the margin is the runner-up minus
the winner, so a rescued RUNNER-UP moves it directly. Margins in that range are 39 mHa
and up; the artifact seen here is 2 mHa, a factor of 20 below. That is an argument that
entrants are safe, NOT a measurement that they are, and it is not offered as one.
DOES bear on EX-4's failure at Z=19 (s60 §1), which sits at 0.6-2.5 mHa — the same scale
as this artifact, at the same Z. **NOT CLAIMED AS THE EXPLANATION.** The s61 prediction
file bars the word "numerical" as an excuse until the Rung 7 floor is measured, and that
bar stands against this session's own convenient finding.

## REMEDY
1. **The seed test does not compare to the sealed row.** Its baseline is the harness's
   own seed-A row, same construction, seed varied and nothing else (Standing 8). Done.
2. Re-walking Z=2..56 under the guard is a real repair and a real cost. NOT undertaken
   in s61 and NOT smuggled in. Entered on the owed list for a future session, where it
   should be run as a re-derivation with the entrant compared at all 55 rows.
3. No sealed file is edited (F44.1 route).
