# RESULT S81 — ITEM 3. THE TWO REMAINING Z=89 BRACKETS. **U1 IS FALSIFIED, AND THE
# FALSIFICATION IS A STRONGER STATEMENT THAN THE PREDICTION WAS.**
# 7d AND 8d ARE NOT UNREACHED. NO BOUND STATE CARRYING THEIR NODE COUNT WAS FOUND ANYWHERE
# IN A WINDOW EIGHTY TIMES WIDER THAN THE ONE refine79 SEARCHED.
# Prediction sha256 63eb8489992ecd943896ac43d475818cfab566600615d79014db43f21b91d7bc, filed first.
# Instrument pack81/de81.py, IMPORTING pack80/de80.py unmodified. No sealed file edited.

## THE CAN-FAIL, RUN FIRST AND RUN AGAIN BEFORE EVERY QUESTION ROW
**K4:** 6d through this driver, fallback inert, returns **E = −25694.541630577907, the
sealed pack77 value to every digit, with fb = 0.** PASS. It ran seven times in this
session and passed every time — see F81.4 for why it ran more often than intended.

## THE RESULT — FOUR RUNS, TWO CHANNELS, BOTH BRANCHES, ALL FOUR REFUSE
| ch | branch | window searched (Ha) | target nodes | standard bracket gave | outcome |
|---|---|---|---|---|---|
| 7d | least-bound | [−1.99e−4, −0.635] | 4 | 3 | **NO TARGET-NODE ZERO** |
| 7d | most-bound | [−1.99e−4, −0.635] | 4 | 3 | **NO TARGET-NODE ZERO** |
| 8d | least-bound | [−1.06e−4, −0.340] | 5 | 4 | **NO TARGET-NODE ZERO** |
| 8d | most-bound | [−1.06e−4, −0.340] | 5 | 4 | **NO TARGET-NODE ZERO** |
The first pass used de80's f-channel window, shallow end −0.0159 Ha, and returned the same
refusal. **That bound was widened to −2e-4 Ha — the SAME shallow bound the project adopted
at s79 as fixed79's E5 amendment — and 900 scan points, and BOTH BRANCHES WERE RE-RUN.**
K5 declares the widening and the timing flag: **it followed a numerical result.** The
prediction file was not touched and its sha gate held across the amendment.

## WHAT THIS IS, AND WHAT IT IS NOT
**IT IS NOT "THE INSTRUMENT COULD NOT REACH THEM".** de80's fallback recovered 6f, 7f and
8f at Z=89 in one firing each, and this driver reproduces the sealed 6d energy exactly.
The same machinery, pointed at 7d and 8d over three decades of energy, finds **no energy
at all whose solution carries the target node count.**
**THE STATEMENT SUPPORTED IS: in the Z=89 field, over [−2e−4, −0.64] Ha, the l=2 channel
has no bound state with 4 nodes and none with 5.** The d ladder in this field appears to
terminate at 6d.
**THE STATEMENT NOT SUPPORTED, AND IT MUST NOT BE MADE: "7d does not exist".** Three
caveats, all filed:
1. **THE SCAN SEES THE FIELD AT THE ITERATION WHERE THE FALLBACK FIRES**, not the
   converged field. de80's G2 exists because the field moves every iteration.
2. **THE WINDOW IS FINITE.** Nothing is claimed shallower than −1e−4 Ha. A state within
   0.1 mHa of threshold is outside this search by construction.
3. **ONE Z, ONE SEED, ONE RUNG.**

## WHAT IT SETTLES FOR THE Z=89 ROW
s79 left five CLASS B channels. s80 recovered three. **This session shows the remaining
two are of a different kind: not unreached, but carrying no bound target-node state in the
searched window. A channel with no bound state cannot be the entrant.**
**THE Z=89 ROW IS THEREFORE COMPLETE IN A STRONGER SENSE THAN "THREE OF FIVE HOLES
CLOSED": three recovered and placed 137–147 mHa above rank 1, two shown absent from the
spectrum over three decades. RANK 1 AND RANK 2 ARE UNTOUCHED. THE ENTRANT AT Z=89 IS 6d.**

## PREDICTION SCORED — U2 CARRIED VACUOUSLY, U5 AND U6 CORRECT, **U1 U3 U4 FALSIFIED**
  U1 both converge on the least-bound branch . . **FALSIFIED, AND IT IS THE RESULT.**
     Neither converges, on either branch, under a bound 80x wider than refine79's. The
     filed rationale — that refine79's failure was an orientation-and-bound artefact —
     **is wrong for these two channels.** It was right for the three f channels; I
     generalised it and it did not travel. **The prediction filed the losing branch's
     honest statement in advance and that statement is now the result.**
  U2 entrant unchanged, both above 7p by >2 m(89) . . **THE FIRST CLAUSE HOLDS AND THE
     SECOND IS VACUOUS.** No dE exists to compare. Scored as carried, not as correct: a
     clause that cannot be evaluated is not evidence.
  U3 7d more bound than 8d, both between −70.65 and −31.46 mHa . . **FALSIFIED**, and it
     was filed as the weakest clause. No values exist.
  U4 n_zeros ≥ 2 somewhere, most-bound fails on at least one channel . . **FALSIFIED.**
     n_zeros = 0 everywhere; the zero SET IS EMPTY, not two-membered. F80.1's structure
     does not repeat in the d block. **The most-bound branch does fail — but so does the
     least-bound, which is not what the clause claimed.**
  U5 the fallback fires once per channel, not every iteration . . **CORRECT**, and it is
     the corrected form of s80's badly-falsified X5. **The correction travelled.**
  U6 K4 returns the sealed 6d energy with zero firings . . **CORRECT**, seven times.

## F81.4 — A str_replace PATCH DELETED A FUNCTION HEADER AND ONE FUNCTION SWALLOWED
## ANOTHER. RAISED AGAINST MY OWN INSTRUMENT.
**WHAT HAPPENED.** The K5 widening was inserted immediately above `def canfail():` by
replacing that header line. **The header was consumed; `canfail`'s body became part of
`widen()`.** Every `wide` invocation therefore ran the 6d can-fail before its question
run, and the name `widen` described half of what the function did.
**HOW IT SURFACED.** The receipts. `de81.jsonl` carried a K4 row before every
question-wide row, which the CLI dispatch could not explain. **It was chased rather than
waved through, because unexplained instrument behaviour is exactly what this project
registers.**
**SEVERITY: BENIGN IN EFFECT, AND THAT IS NOT A DEFENCE.** The gate ran MORE often, not
less, and passed every time; no result is disturbed and the four refusals reproduce
identically after the repair. **But a function carrying a name that describes half its
behaviour is the same species as every other fault in this run.** Repaired; the header is
restored and both paths re-verified.
**THE SPECIES, SEVENTH APPEARANCE IN FOUR SESSIONS.** F78.1 · F79.1 · F79.2 · F80.1 ·
F80.3 · F81.1 · **F81.4: read what the patch actually replaced.**
