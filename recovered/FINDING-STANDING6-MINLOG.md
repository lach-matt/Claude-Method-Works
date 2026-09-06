# FINDING — STANDING 6 ON THE s66 §6 MINLOG TREND
# SESSION 67, ITEM 1, RUN BEFORE ANYTHING ELSE TOUCHED IT, as the s66 bridge required.
# Archive search by content + arithmetic on SEALED rows only. Standing 5 observed:
# counts, sets and reads. NO solve was run. NO prediction was needed and none is filed.
# No sealed file is edited. R 1449 intact.

## WHAT WAS TO BE CHECKED
`BRIDGE-LOWDIN-SESSION-66.md` §6, filed as diagnostic and NOT scored:

> "**minlog falls systematically with Z** — +0.91/+1.13 at Z=21 down to +0.090/+0.040
> at Z=89 ... If it crosses zero at some Z the cell becomes CLASS C. **Nothing measured
> says it does.** Standing 6 applies before any session treats this as new."

## PART 1 — IS THE MEASUREMENT IN THE ARCHIVE?  NO. IT IS NEW.
Literal `minlog` occurs in four sealed places only: `rt/t7f_rep.py`, `pack42/t7f_rep.py`,
`pack42/BRIDGE-LOWDIN-SESSION-42.md`, `pack42/FINDING-REPAIR-4D.md`. All four carry the
SINGLE value +0.9083 at Z=21 4d. A minlog at any other atom exists nowhere before s66.
**The ten-cell spectrum is a genuinely new measurement. Standing 6 does not retire it.**

## PART 2 — IS THE INFERENCE FORM IN THE ARCHIVE?  YES, TWICE, AND BOTH TIMES IT FAILED.
The inference "quantity q falls with Z across my sample, therefore Z governs q" has been
made twice in this chain and corrected twice, in both cases by widening the sample:

  * **s49 → s50.** `pack49/BRIDGE-LOWDIN-SESSION-49.md` §2 read the margin as widening
    monotonically with Z, 0.19 at Os to 0.52 at No(102). `pack50/SCORING-5fCLOSE-97-108.md`:
    *"The margin does not widen monotonically with Z ... It tracks the depth of the open f
    channel ... collapses to 0.05440 at 105 the moment 5f closes."*
    **The governing variable was f-channel depth, not Z.**
  * **s45 → s46.** `pack46/PREDICTION-4f-COLLAPSE.md` corrects s45 §2(9)'s "shrinks
    monotonically toward 1 as Z rises": non-monotone at Z=50, AND the whole fine trend
    sits at or below storage resolution, so monotonicity was unreadable in either direction.

**Both corrections have the same two edges: a hidden channel variable, and resolution.**

## PART 3 — AND THE CLAIM IS FALSE ON ITS OWN TEN SEALED ROWS.
Read off `pack66/nodespec.jsonl`, no recomputation:

    Z   ch   tgt   minlog          Z   ch   tgt   minlog
    21  4d    1    +0.9083         49  5d    2    +0.7741
    21  5d    2    +1.1314         49  6d    3    +1.2644
    39  5d    2    +0.4649         57  6d    3    +0.0726
    39  6d    3    +0.4368         57  7d    4    +0.0937
                                   89  7d    4    +0.0897
                                   89  8d    5    +0.0401

**minlog RISES from Z=39 to Z=49 in BOTH channels** — 5d +0.4649 → +0.7741, and
6d +0.4368 → +1.2644, the largest single value in the set. The sequence over the three
low atoms is DOWN then UP. **"Falls systematically with Z" is contradicted by the data
the sentence was written from.** Registered as **F67.1**; the s66 bridge is sealed and
is NOT edited.

## PART 4 — WHAT THE TEN ROWS DO SHOW: A TWO-GROUP SPLIT, NOT A TREND.

    GROUP L   Z = 21, 39, 49   six cells    min +0.4368   max +1.2644
    GROUP H   Z = 57, 89       four cells   min +0.0401   max +0.0937

The groups do not overlap and **nothing lies between +0.0937 and +0.4368 — a factor of
4.66 with no cell inside it.** Ten points falling into two tight clusters with an empty
gap between them is not a trend in a continuous variable. It is a step, and a step has a
threshold.

**AND THE STEP LIES EXACTLY AT THE f-BLOCK OPENINGS.** Group H is Z=57 (La) and Z=89
(Ac) and nothing else. Those are precisely the two atoms Deliverable 1 §6 already names
as the tie-break failures attributable to orbital collapse, and precisely the two the
observed opening sequence puts at 5d-before-4f and 6d-before-5f. Group L is Z=21, 39, 49
— every one of them with no f channel open.

**This is s50's correction in the same shape: a quantity that looked like a trend in Z,
and the archive's own reading is that it tracks the f channel.** The confound is total in
this sample — Z, n, tgt, nd_max and f-presence all move together across the ten cells,
and every cell of Group H is an f-opening atom.

## PART 5 — VERDICT ON ITEM 1
  1. The measurement stands and is new. Standing 6 does not retire it.
  2. The s66 §6 sentence is **withdrawn as stated** (F67.1). It is not a trend in Z.
  3. The onward inference — "if it crosses zero at some Z the cell becomes CLASS C" —
     **has no support at all**, because there is no established trend in Z to extrapolate
     along. Extrapolating a step across its own empty gap is the error s49 made.
  4. **A discriminating test exists and is cheap**, and it is named here WITHOUT being
     run: the sealed survey gives 6d failures across Z=39..83 and 5d across Z=20..51.
     A minlog row at 6d for Z in 50..56 (no f open) and Z in 58..70 (4f filling) separates
     the two hypotheses, because Z rises smoothly across that range while f-presence
     switches at exactly one atom. **Step at Z=57 → f-onset governs. Smooth descent
     through 50..56 → Z governs.** Filed as a candidate, not opened. It requires M's
     ruling, a filed and hashed prediction, and a can-fail demonstration first.

## WHAT THIS COST AND WHAT IT TOUCHED
No solve. No margin, entrant, ordering, rung, bound, gate or Deliverable is touched.
No sealed file edited. Cost: one archive search and one read of ten sealed rows.
