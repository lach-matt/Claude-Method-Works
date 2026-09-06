# RESULT S80 — ITEM 1. F79.2 IS CLOSED. THE Z=89 TABLE IS NOW IN ONE CURRENCY.
# THE ENTRANT IS UNCHANGED AND THE MARGINS ARE LARGER, NOT SMALLER, THAN THE WITHDRAWN ONES.
# Prediction sha256 560ce4ad3c2be891fd4bac5ce72fddbc10810100e986547d10a94a443839a641, filed first.
# Instrument pack80/de80.py — SEVEN declared lines from sealed hfc2.py / nlguard.py.

## THE THREE CAN-FAILS, RUN FIRST, ALL PASSED, AND ONE OF THEM IS NEW TO THIS PROJECT
C3 SCORER — 6d against baseline 7p returns **ENTRANT CHANGES**; 5f against baseline 6d
   returns **ROW HOLDS**. M's order required an instrument whose verdict space is not
   one-sided. Both verdicts reachable on the identical path.
C1 MACHINERY — 6d with the fallback INERT returns **E = -25694.541630577907, the sealed
   pack77 value to every digit**, 44 iterations, and **fb = 0**: the fallback does not
   touch the ruling path on a healthy channel.
C2 FALLBACK PATH — 6d with the fallback **FORCED** on the 6d channel fires on all 44
   iterations, returns **e_fb = e_std = -0.176897462, identical to nine digits**, and
   lands on **-25694.541630579646, the sealed energy to 1.7e-9.**
   **THIS IS THE CONTROL s79 DID NOT HAVE.** refine79 could show a state existed; it
   could not show that RETURNING that state reproduces what the ruling path returns.

## THE MEASUREMENT — dE = E(cfg88 + ch) - E(ref), E(ref) = -25694.38401018016
| ch | E | dE (mHa) | above 6d | above 7p | x m(89) | verdict |
|---|---|---|---|---|---|---|
| **6f** | -25694.404496178428 | **-20.486** | 137.134 | **104.802** | **3.241** | ROW HOLDS |
| **7f** | -25694.398292407324 | **-14.282** | 143.338 | **111.006** | **3.433** | ROW HOLDS |
| **8f** | -25694.394538374345 | **-10.528** | 147.092 | **114.760** | **3.549** | ROW HOLDS |
Baselines, sealed: 6d dE = **-157.620** (rank 1), 7p dE = **-125.288** (rank 2),
m(89) = **32.332 mHa**. All three converged at rung 0, 83-86 iterations, **zero edge flags**.
**THE ENTRANT AT Z=89 IS 6d. NEITHER RANK 1 NOR RANK 2 IS TOUCHED, AND THE MULTIPLES OF
THE MARGIN ARE NOW RATIOS OF LIKE QUANTITIES AND MAY BE STATED.**

## F79.2 IS CLOSED
The withdrawn multiples are superseded, not restored: **2.898 m -> 3.241 m, 3.248 m ->
3.433 m, 3.440 m -> 3.549 m.** The repair moved every f channel FURTHER from rank 2, by
11.1, 6.0 and 3.6 mHa. **The Z=89 hole is no longer three eigenvalues and two brackets.
It is three converged rows in the table that decides the row.** Two brackets — 7d and
8d — remain, and are untouched by this session.

## THE CURRENCY OFFSET, NOW MEASURED AT FOUR CHANNELS INSTEAD OF ONE
| ch | dE | eps (converged) | dE - eps |
|---|---|---|---|
| 6d | -0.157620 | -0.176898 | **+19.277 mHa** |
| 6f | -0.020486 | -0.020354 | **-0.132 mHa** |
| 7f | -0.014282 | -0.014151 | **-0.132 mHa** |
| 8f | -0.010528 | -0.010393 | **-0.135 mHa** |
**THE OFFSET IS 146 TIMES SMALLER AT THE f CHANNELS THAN AT 6d, AND IT IS OF THE
OPPOSITE SIGN.** F79.2 warned that the one-channel 6d offset was *"an estimate from one
channel's offset, NOT a bound on the offset in the others."* That warning was correct and
is now discharged by measurement: the offset does not transfer between channels.
**This is why the repair had to be run rather than argued.**

## PREDICTION SCORED — X2 X3 X6 X7 CORRECT, X1 SPLIT, X4 AND X5 FALSIFIED
  X1 all three converge . . . . **SPLIT.** True on the surviving branch; FALSE on the
     other, and the prediction did not know a branch choice existed. See F80.1.
  X2 entrant unchanged, all above 6d AND above 7p . . **CORRECT**, 137-147 mHa above 6d.
  X3 dE ordering matches eigenvalue ordering . . **CORRECT** — and this was filed as
     *"the clause most likely to fail... I expect it to be the one that costs me."*
     It did not. **The clause I trusted least held; two I did not flag broke.**
  X4 offset positive and under 19.277 mHa . . **FALSIFIED ON SIGN.** It is NEGATIVE,
     -0.13 mHa. The magnitude clause was right and the reasoning behind it — a diffuse f
     orbital perturbs the [Rn] core less — survives; **the sign was asserted from one
     channel's example and was wrong.**
  X5 the fallback fires on every iteration, n_fb == it . . **FALSIFIED, AND BADLY.**
     **n_fb = 1 on all three.** The fallback fires ONCE, on iteration 1, and every channel
     is healthy for the remaining 82-85 iterations. **The filed rationale — that state
     misidentification is structural because eigen_sr's guess carries no knowledge of the
     node count — is WRONG. It is a START-UP ARTEFACT.** Once the SCF is placed on the
     correct state it stays there of its own accord. This is a fact about the field, it
     was not predicted, and it is the most interesting thing in the run.
  X6 no scan-bound edge flag . . **CORRECT** — zero flags on any converged channel.
  X7 margins larger than the withdrawn ones by under 20 mHa . **CORRECT** — +11.1, +6.0,
     +3.6 mHa. Recorded: the withdrawn figures were computed from the branch F80.1
     rejects, so this clause is scored against superseded numbers.

## RECORDED AGAINST THIS RESULT, NOT BURIED
1. **F80.1 IS RAISED AGAINST THIS SESSION'S OWN FIRST RUN**, and the instrument was
   amended after a numerical result. Timing flag declared in F80.1.
2. **ONE SEED, SEED A's CHAIN.** The reference and the two baselines are sealed seed-A
   values. Nothing here re-seeds.
3. **THE FALLBACK IS NOT A PROOF THAT THE FIELD HAS NO OTHER SOLUTION.** It shows the
   more-bound branch does not self-consistently close and the less-bound branch does.
   That is a statement about what the program reaches, which is O-C1's territory.
4. **THIS IS A RANKING RESULT, NOT A DERIVATION.** It closes a fault against a written
   result. It derives no property of F_core and must never be quoted as doing so.
