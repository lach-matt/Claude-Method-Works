# PREDICTION-CHAIN-4p (s43, item 1) — WRITTEN BEFORE nlchain IS POINTED AT Z=31 (R 1449)
Standing ruling s40 (3): the walk moves; nothing else opens until it does. Segment: Z = 31..38, 3 steps per call.

## 0 · THE ENTRY PREMISE, VERIFIED BY READING NOT BY ASSUMING (no run)
Row 30 banked: `ref_cfg = 1s2 2s2 2p6 3s2 3p6 3d9 4s2`, entrant 3d, `rec_cfg = ...3d10 4s2`.
**Therefore the chain's configuration at Z=30 is 3d10 4s2 — IDENTICAL to the record's Zn.**
The two 3d-row divergences (Z=25, Z=30) are ENTRANT-CHANNEL divergences that leave the ACCUMULATED
CONFIGURATION in agreement: the chain reaches Mn and Zn by a different route and arrives at the same place.
**The 4p row therefore opens on the record configuration, and no divergence is inherited into it.**
This is s41 finding 5 (the `ok` flag and the configuration disagree) seen from the other side, and it is the
reason a 27/29 `ok` score does not mean the chain is two elements off course.

## 1 · WHAT THE INSTRUMENT WILL DO (from source, nlchain.step)
Candidates at Z=31 from cfg_prev = [Ar]3d10 4s2: n in 1..5, l <= min(n-1,4), any shell below CAP.
Available: **4p, 4d, 4f, 5s, 5p, 5d, 5f, 5g** (8 offered). D = E(Z, cfg_prev + c) - E(Z, cfg_prev) at fixed
nucleus Z (F40.1). Winner = min D. `ok` compares the winner to the record's entrant channel only.
Banked order at Z=30 for reference: 3d -0.53981 | 4p -0.19856 | 5s -0.09845 | 5p -0.06525 | 4f -0.03126 |
5f -0.02001. **4d, 5d, 5g did not converge at Z=30 and are absent from that list.**

## 2 · PREDICTIONS, WITH REASONS, SO A FAILURE IS SCORED AND NOT EXPLAINED AFTERWARDS
    PC4P-1  Z=31..36 entrant is **4p at every step**; ok=True on all six.        PREDICT: TRUE
            Reason: 3d is full, so within n+l = 5 the only competitor is 5s, and 4p carries the lower n.
            The field already ranks 4p above 5s by 0.100 Ha at Z=30 with 4p EMPTY; adding nuclear charge
            widens it, because 4p penetrates the 3d10 core and 5s sees it screened.
    PC4P-2  The runner-up is **5s at every one of Z=31..36**.                     PREDICT: TRUE
            Reason: the Z=30 order already has 5s second among convergent channels once 3d closes.
    PC4P-3  |D_ent| increases monotonically across Z=31..36.                      PREDICT: TRUE
            Reason: same-shell filling under rising Z; the 2p (Z=5..10) and 3p (Z=13..18) rows both do it.
    PC4P-4  The 4p-over-5s margin increases monotonically across Z=31..36.        PREDICT: TRUE
    PC4P-5  **Z=37 entrant is 5s, ok=True; Z=38 entrant is 5s, ok=True.**         PREDICT: TRUE
            Reason: 4p closes at Kr, and 5s is the last n+l = 5 channel. The competitor is 4d at n+l = 6.
    PC4P-6  **The margin at Z=37 is the SMALLEST of the eight steps**, and smaller than at Z=36.
                                                                                  PREDICT: TRUE
            Reason: 37 is a shell-boundary step and 5s/4d is the near-degenerate pair the whole 4d/5s
            crossover is made of. If the field is going to break in this segment, it breaks here.
    PC4P-7  D_ent JUMPS UP (less bound) from Z=36 to Z=37 — the shell-closure step.PREDICT: TRUE
            Reason: the 18->19 signature, -0.54225 -> -0.14774, repeated one shell out.
    PC4P-8  **nfail > 0 on at least one step of Z=31..36, and 4d is among the non-convergent channels.**
                                                                                  PREDICT: TRUE
            Reason: s42 measured that a diffuse d channel on a closed-core field has no normalisable
            node-correct solution; 4d, 5d, 5g were already absent at Z=30.
    PC4P-9  **Every drop stays SAFE: gate 77 reports UNSAFE = 0 after the segment.** PREDICT: TRUE
            Reason: a dropped channel is only UNSAFE if it could have won; 4d cannot win below Z=39.
    PC4P-10 **PD-6's exception set stays EMPTY through Z=38** — entrant = argmax|Delta| on every new row.
                                                                                  PREDICT: TRUE
            Reason: PC3D-10 is expected to make its first break at the 4d/5s crossover Z=39..41, which is
            OUTSIDE this segment. This prediction is what makes that expectation falsifiable HERE.
    PC4P-11 Chained score after the segment is **35/37** — the two 3d-row divergences stay the only ones.
                                                                                  PREDICT: TRUE
    PC4P-12 The accumulated configuration at Z=36 equals the record's Kr, and at Z=38 the record's Sr.
                                                                                  PREDICT: TRUE
            Scored SEPARATELY from the `ok` flag, per s41 finding 5 / next-chat item (3).

## 3 · THE FOURTH-OUTCOME CLAUSE, REGISTERED IN ADVANCE SO A NULL IS NOT MISREAD
If **PC4P-5 fails and 4d wins at Z=37**, that is not a numerics fault and must not be repaired into
agreement. It would mean the SR-HF field places the 4d minimum below 5s one element early, and the object
to report is the crossover's LOCATION, not a broken step. The diagnostic that separates a real early
crossover from a convergence artefact: read whether 4d's D at Z=37 sits on the smooth trend of 4d's D
across Z=31..36, or arrives discontinuously from a channel that had been dropping.
If **any of Z=31..36 fails to give 4p**, the first thing to check is nfail, not the physics: a step whose
4p channel dropped will hand the row to whatever converged, and that is an instrument failure wearing the
appearance of a finding.

## 4 · HELD
No record value entered as an input. Record configurations are RECALLED for the comparison column only.
c = 137.035999 only. Grid, seed, qtail, maxit, frozen avg-of-config, candidate rule: UNCHANGED from s42.
No parent file edited. Configurations are built by `nlchain.add` only (F42.2 — shell order is load-bearing).
Gate log is written fresh, never appended to (F42.1).
