# SCORING — PREDICTION-5fCLOSE-97-108, closed at s50

Filed s49 before any of Z=97..108 ran. Scored s50 after the walk reached 108. Six of the twelve
steps (97..102) were run and scored in s49; 103..108 ran this session. **6 held, 3 failed.**

| clause | verdict | what the field did |
|---|---|---|
| PG-1 5f entrant at 97..102 | **HELD** | all six |
| PG-2 ok passes 97..102 | **HELD** | all six |
| PG-3 cfg fails at every Z in 97..103 | **HELD** | 97,98,99,100,101,102,103 all fail — recovers nowhere inside |
| PG-4 Lr(103): record says 7p, walk says 5f, ok False | **HELD** | entrant 5f, D −0.76321, margin **0.55649** over 6d; record 7p |
| PG-5 6d entrant at 104..108, ok passes all five | **FAILED at 104** | entrant 5f, ok False. 105..108 held |
| PG-6 cfg recovers nowhere in 104..108 | **FAILED at 104..108** | cfg passes at ALL FIVE |
| PG-7 no ordering failure in 97..108; FIRST STEP DIVERGENCE stays 25 | **HELD** | 0 ordering failures; ok_first = 25 |
| PG-8 ok_score (97,107), cfg_score (68,107) | **FAILED, both integers** | actual **(96,107)** and **(73,107)** |
| PG-9 no constant introduced | **HELD** | c = 137.035999 only |

## The single error behind all three failures

PG-5, PG-6 and PG-8 fail from ONE miscount, stated in PG-4's reasoning: *"the walk, one 5f behind,
reaches 5f14 only at 103."* It reaches 5f14 at **104**. The walk held 5f12 after Z=102, not 5f13.
Every consequence follows from that one off-by-one:

- 104 is a fifth actinide `ok` failure, not the first of five passes → ok_score 96, not 97
- and the walk's fourteenth 5f lands on a configuration that ALREADY carries 6d2 7s2, giving
  **5f14 6d2 7s2 — exactly the record's Rf(104)** → cfg_score 73, not 68

**PG-6 failed in the direction that favours the walk, and that is the finding.** The walk entered
the actinides with two offsets — one 5f behind, one 6d ahead — which s49 correctly said "cannot
cancel" one at a time. They cancelled *simultaneously* at 104. The record's 7p1 at Lr does not
persist into Rf, so the walk's inability to open 7p costs it exactly one element. From 105 the walk
and the record run in lockstep in 6d and the cfg column holds to the end of the derivation.

**The walk rejoined the record for the final five elements without a promotion operator.** This is
the Ce(58) structure recurring at the top of the table: where the offsets happen to cancel, the
one-electron walk reproduces the observed configuration outright.

## What was NOT predicted and is now measured

The margin does **not** widen monotonically with Z. s49 read 0.19 at Os → 0.52 at No(102) as a
trend in Z. It is not. It tracks the depth of the open f channel: 0.55649 at 103, 0.59191 at 104 —
the widest in the chain — then **collapses to 0.05440 at 105** the moment 5f closes, recovering
only to 0.08254, 0.11126, 0.14058 at 106, 107, 108. The widening was 5f being deep, not the
ordering becoming less ambiguous down the table. **The s49 bridge sentence is corrected here.**
