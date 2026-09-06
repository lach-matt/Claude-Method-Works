# SCORE — T-E. IS THE minlog DESCENT A STEP OR A SLOPE?
# SESSION 67. Prediction pack67/PREDICTION-T-E.md
# sha 218396913cf53cf5d36620e70607296e63fa1b9303db5443ede332bf273432a5,
# filed 2026-08-20T23:28:43Z before pack67/nodespec67.py existed and before any cell of
# the scored set was computed. Verified at every invocation; the driver halts without it.
# Instrument pack67/nodespec67.py — the sealed pack66 parent with three path constants
# changed and NOTHING else (diff proved: 3 lines). Cache pack67/nodespec67.jsonl.
# THE CLASS C AT Z=51 IS REPORTED FIRST, IN pack67/FAULT-F67.2, AS THE PREDICTION
# REQUIRED. THIS FILE IS THE SCORE AND IS SECOND.

## THE HEADLINE

    BOTH FILED READINGS ARE DEAD. minlog IS NEITHER A SLOPE IN Z NOR A TWO-VALUED
    STEP AT THE 4f COLLAPSE. AND ONE CELL IS CLASS C.

## THE ROWS — 29 SCORED CELLS, PLUS THE 2 GATE CELLS AT Z=39

    GATE (not scored)              PRE-COLLAPSE (scored)
    Z=39 5d  B  0.4649             Z=50 5d  B   1.4105
    Z=39 6d  B  0.4368             Z=50 6d  B   0.4287
                                   Z=51 5d  C  -0.2904   <-- F67.2

    POST-COLLAPSE (scored)   6d                 7d
    Z=58   B  0.2760              B   0.2842
    Z=59   B  0.2932              B   0.2893
    Z=60   B  0.3390              B   0.3315
    Z=61   B  0.4155              B   0.4108
    Z=62   B  0.5131              B   0.5279
    Z=63   B  0.4841              B   0.6841
    Z=64   B  0.4837              B   0.0021   <-- 7d breaks away here
    Z=65   B  0.5115              B   0.0613
    Z=66   B  0.5678              B   0.1497
    Z=67   B  0.6530              B   0.1147
    Z=68   B  0.6217              B   0.0608
    Z=69   B  0.5908              B   0.0325
    Z=70   B  0.5826              B   0.0292

## SCORING, AGAINST THE FILED FILE

    PS-0  **HELD EXACTLY.** Z=39 returned CLASS B with minlog 0.4649 (5d) and 0.4368
          (6d), reproducing s66 digit for digit at the four decimals the instrument
          stores. nd_max=14 both, as s66. **TENTH DETERMINISM RECEIPT**, and the second
          against another session's cached values from a driver that did not exist when
          they were made. The precision was stated in advance (Standing 12, proposed at
          s66 after F66.2) and the gate was satisfiable. **F66.2's defect did not recur.**

    PS-1  **FAILED.** Predicted minlog(50,6d)/minlog(58,6d) >= 4.0.
          Measured 0.4287 / 0.2760 = **1.553**. There is no large step across the
          unmeasurable gap. The pre-collapse and post-collapse 6d values are the same
          size.

    PS-2  **FAILED, and it is the discriminator.** Scored 1 of 2 channels.
            6d across Z=58..70:  max/min = 0.6530/0.2760 = **2.37 <= 3.0**, and not
                                 monotone decreasing. **HOLDS.**
            7d across Z=58..70:  max/min = 0.6841/0.0021 = **326**. **FAILS, by two
                                 orders of magnitude.**
          The clause required both. It is scored FAILED.

    PS-3  **FAILED as written.** Scored 2 of 3.
          Z=50 5d = 1.4105 > 0.20 held. Z=50 6d = 0.4287 > 0.20 held.
          Z=51 5d = **-0.2904**, which is not merely below the divider but below ZERO,
          and is the CLASS C cell.

    PS-4  **FAILED. 28 CLASS B, 1 CLASS C, 0 CLASS A, of 29.** Reported first, F67.2.

    PS-5  Held. No eigenvalue, nd_max, win_pts, sign-change count, iteration, D, margin,
          entrant, ordering, rung or bound was predicted and none is claimed. Nothing
          about f or g channels. Nothing about Delta-delta or alpha.

    NET: PS-0 held. PS-1, PS-2, PS-3, PS-4 all failed. PS-5 held.
    **A four-clause failure on a prediction whose two readings were exhaustive means the
    exhaustion was false, not that the measurement went badly.** That is the result.

## WHAT IS ESTABLISHED, STATED NEGATIVELY AND ONLY NEGATIVELY

  1. **Reading (S), the slope, is dead.** minlog does not fall with Z. Past the 4f
     collapse the 6d value RISES, 0.276 at Z=58 to 0.653 at Z=67 — the opposite
     direction to the s66 §6 sentence F67.1 withdrew. F67.1's withdrawal is now
     completed by measurement rather than by arithmetic on ten rows.
  2. **Reading (T), the two-valued step at the collapse, is dead.** Z=50 6d (before the
     collapse) and Z=58 6d (after it) differ by a factor of 1.55. There is no step at
     the 4f collapse in the 6d channel, and Deliverable 3's Z=57 transit — correct as a
     statement about n* — does not govern this quantity.
  3. **The s66 §6 zero-crossing worry was RIGHT THAT IT CROSSES, AND WRONG ABOUT WHERE.**
     §6 supposed minlog might reach zero at some high Z by continued descent. It reaches
     zero at **Z=51**, below every atom §6 was looking at, and by no descent at all.
  4. **6d and 7d are not the same quantity.** They track each other to within 0.03
     across Z=58..62, and from Z=64 they diverge by a factor of 20 and stay diverged.
     **Whatever governs minlog separates two channels of the same l at the same atom**,
     which no reading in the filed prediction allows for.

## WHAT IS **NOT** PROPOSED HERE, AND WHY
F65.1's rule is observed without exception: **no replacement reading, classifier or
mechanism is proposed in the session that falsified this one.** Two things are recorded
as SHAPE OF THE DATA, unscored, not interpreted, and flagged for Standing 6 before any
future session treats either as new:

  * the 7d break at Z=64, and the low-minlog cells generally — Z=51 5d (-0.29),
    Z=57 6d/7d (+0.073/+0.094), Z=64..70 7d (0.0021..0.1497), Z=89 7d/8d (+0.090/+0.040);
  * the smooth 6d rise across the 4f row, 0.276 to 0.653, which is monotone to within
    two small reversals at Z=63 and Z=68..70.

**No account of either is offered.** F67.1 exists precisely because the last session to
describe this quantity in a sentence described it wrongly, and the sentence was the
cheap part.

## COST, AND WHAT WAS TOUCHED
31 cells, 82 s of compute, four Zeno segments, none overrun. No sealed file edited. No
margin, entrant, ordering, rung, bound, gate or Deliverable touched. The Löwdin
deliverable is unaffected in either direction. **The chain's `fail` set is affected in
its meaning, and that is F67.2.**

## MINOR DEFECT, REGISTERED — F67.3 (COSMETIC)
Every row written by `pack67/nodespec67.py` carries `"driver": "pack66/nodespec.py"`,
because that string is a hardcoded literal in the parent and the copy changed only the
three path constants. The rows in `pack67/nodespec67.jsonl` are therefore mislabelled as
to provenance. **They are NOT edited** — data rows are not rewritten after the fact. The
correction lives here and in the fault log.
