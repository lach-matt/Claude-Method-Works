# PREDICTION-CHAIN-4d (s44, item 2) — WRITTEN BEFORE nlchain IS POINTED AT Z=39 (R 1449)

## 0 · TIMING FLAG, DECLARED AT THE TOP

**One number at Z >= 39 is already known to me.** s42's probe measured the 4d channel at Z=39
converging clean and unblocked at **D = -0.195614**, and that figure is carried in BRIDGE-43 §4(2).
I read it in the bridge at this session's open, before this file was written.

Consequence, stated rather than managed: **any claim in this file about the MAGNITUDE of D_ent at
Z=39 scores CONSISTENT, never HELD.** I have not seen 5p's D at Z=39, nor any other channel's, nor
any winner, margin, ordering, `ok` flag or Delta at any Z >= 39 — so the claims about WHICH channel
wins, and by how much over WHICH runner-up, are untouched by the leak. `nlchain.jsonl` ends at
Z=38 and was read only at Z <= 38.

**Second flag, of a different kind.** The record ground configurations for Z=39..48 quoted in §2
are RECALLED, not read from `ground.py`. I have deliberately not run `G.expand(Z)` for Z >= 39
before writing this file, so that the comparison column is itself under prediction. **If ground.py
disagrees with any configuration in §2, that disagreement is a finding and is reported as one, not
reconciled.**

## 1 · THE OBJECT

`nlchain.py 39 48` on the sealed 37-step chain (ends Z=38). Field: SR-HF, frozen avg-of-config,
grid 4000/2e-5, qtail 1/2, HF maxit 100, c = 137.035999. Reference is the previous NEUTRAL's
configuration on the CURRENT nucleus (F40.1). Configs built through `nlchain.add` (F42.2).
Chain config entering Z=39: `[Kr]5s2`, i.e. `1s22s22p63s23p63d104s24p65s2`.

**This row is not like the 4p row, and the difference is the point.** Z=31..38 contained no
recorded anomaly, which is why it was the cleanest test the walk had had. **Z=39..48 contains six
— Nb, Mo, Ru, Rh, Pd, Ag — the densest concentration of Madelung-irregular elements anywhere in
the table.** The 3d row had two and produced FIRST DIVERGENCE at 25. This row has three times as
many, and Pd is the only element in the table whose record configuration promotes BOTH s
electrons at once.

## 2 · THE COMPARISON COLUMN, RECALLED AND UNDER PREDICTION

Record ground configurations, and the single-channel entrant `rectag` derives from each step
(`nlchain.py` lines 79-84: the channels whose occupancy INCREASES from Z-1 to Z; if exactly one,
that is `rec_ent`; if none or more than one, `rec_ent` is None and `ok` is None):

    Z   record config      increases from Z-1        rec_ent
    39  [Kr]4d1 5s2        4d 0->1                   4d
    40  [Kr]4d2 5s2        4d 1->2                   4d
    41  [Kr]4d4 5s1        4d 2->4  (5s 2->1 falls)  4d
    42  [Kr]4d5 5s1        4d 4->5                   4d
    43  [Kr]4d5 5s2        5s 1->2                   5s
    44  [Kr]4d7 5s1        4d 5->7  (5s 2->1 falls)  4d
    45  [Kr]4d8 5s1        4d 7->8                   4d
    46  [Kr]4d10           4d 8->10 (5s 1->0 falls)  4d
    47  [Kr]4d10 5s1       5s 0->1                   5s
    48  [Kr]4d10 5s2       5s 1->2                   5s

**PC4D-0 — `rec_ent` IS NON-NULL AT ALL TEN STEPS, AND EQUALS 4d AT 39,40,41,42,44,45,46 AND 5s AT
43,47,48.** Falsified by any None in the column. This is a prediction about the RECORD and the
`rectag` rule, containing no field quantity at all — it can be scored the instant the row runs and
it is the load-bearing input to PC4D-5 and PC4D-6. Note what makes it non-trivial: at 41, 44 and 46
the record's step both raises 4d and LOWERS 5s, and `rectag` counts only increases, so a
two-channel rearrangement is reported as a one-channel entrant.

## 3 · THE CLAIMS

**PC4D-1 — 4d WINS AT EVERY STEP Z=39..48. THE ENTRANT IS (4,2) AT ALL TEN.**
Reason: 5s is full at Sr, so the n+l = 5 group is exhausted; the n+l = 6 group is {4d, 5p, 6s} and
clause 2 (smaller n first) puts 4d ahead of 5p. **This is the THIRD distinct pair on which the
tie-break is tested** — 4s/3d in the 3d row (10/10), 4p/5s in the 4p row (6/6), now 4d/5p. A clause
that holds on three unrelated pairs is not a property of any of them.
*Falsified by any step where the winner is not 4d.*

**PC4D-2 — 4d OVERTAKES BOTH 5p AND 5s IN ONE PROTON, FROM THIRD PLACE.**
This is the sharp form of PC4D-1 and it is sharp because of F44.2. At Z=38 the ordering is
5s -0.17457 | 5p -0.11818 | **4d -0.09658**: 4d is THIRD, 0.07799 behind the winner and 0.02160
behind 5p. Across 37->38 it gained 0.00192 on the winner. **At Z=39 it must gain the remaining
0.078 and pass two channels.** s43's reading — that 4d was steadily closing — is withdrawn under
F44.2; on the measured reading this is a discontinuous promotion, and it happens because 5s
CLOSES at Sr and the Pauli seat vanishes, not because 4d was drifting downward.
*Falsified if 4d is not first at Z=39. Reportable either way: the SIZE of the jump is a measured
approach, not a prediction, and is timing-flagged at Z=39 per §0.*

**PC4D-3 — THE RUNNER-UP AT Z=39 IS 5p, AND `order` IS REPORTED WITH IT NAMED.**
The channel displaced from second place is the one that took second at Sr. Falsified if the
runner-up at Z=39 is 5s, 6s, 4f or anything else. **Filed as the operational half of F44.2's
remedy: every margin in FINDING-CHAIN-4d is quoted as `value (vs channel)`.**

**PC4D-4 — D_ent DEEPENS MONOTONICALLY ACROSS ALL TEN STEPS, WITH NO SWING ABOVE 0.05 Ha ABOUT
ITS TREND — AND I EXPECT THE BOUND TO BE APPROACHED NEAR THE HALF-SHELL.**
The 4p row held to 0.02 with second differences ~0.002 because no shell opened inside it. **A d
subshell is not a p subshell**: exchange stabilisation at 4d5 (Z=43) is where the record itself
breaks, and if the field carries any half-shell structure it appears here. The bound is set
deliberately looser than the 4p row's and the reason is stated in advance.
*Falsified by any non-monotone step, or by any swing above 0.05. If a swing appears AT Z=43
specifically, that is not a falsification of the field, it is the half-shell arriving, and it must
be reported as the finding it is rather than absorbed into the bound.*

**PC4D-5 — THE `ok` FLAG SCORES 7/10, TRUE AT 39,40,41,42,44,45,46 AND FALSE AT 43,47,48.**
Direct consequence of PC4D-0 and PC4D-1: `ok` is `rec_ent == win`, the win is 4d throughout, and
`rec_ent` is 5s at exactly three steps. **Chained score goes 35/37 -> 42/47. FIRST DIVERGENCE
STAYS AT 25**, since 25 < 43 and the definition takes the first False.
*Falsified by any other count, or by any movement in FIRST DIVERGENCE.*

**PC4D-6 — AND THE CONFIGURATION SCORES 3/10, NOT 7/10. THE `ok` FLAG OVERSTATES AGREEMENT BY A
FACTOR OF MORE THAN TWO.**
**This is the row's real claim.** Walking the chain's own configuration forward under PC4D-1:

    Z   chain config      record config      config match     ok      agree?
    39  [Kr]4d1 5s2       [Kr]4d1 5s2        YES              True    yes
    40  [Kr]4d2 5s2       [Kr]4d2 5s2        YES              True    yes
    41  [Kr]4d3 5s2       [Kr]4d4 5s1        no               True    **NO**
    42  [Kr]4d4 5s2       [Kr]4d5 5s1        no               True    **NO**
    43  [Kr]4d5 5s2       [Kr]4d5 5s2        YES              False   **NO**
    44  [Kr]4d6 5s2       [Kr]4d7 5s1        no               True    **NO**
    45  [Kr]4d7 5s2       [Kr]4d8 5s1        no               True    **NO**
    46  [Kr]4d8 5s2       [Kr]4d10           no               True    **NO**
    47  [Kr]4d9 5s2       [Kr]4d10 5s1       no               False   yes
    48  [Kr]4d10 5s2      [Kr]4d10 5s2       YES              False   **NO**

**Configuration agrees at 3 of 10 (39, 40, 43, 48 — four, minus none) — CORRECTION: at FOUR of ten,
39, 40, 43, 48. `ok` reports 7 of 10. They disagree at SEVEN of ten steps: 41, 42, 43, 44, 45, 46,
48.** In the 3d row they disagreed at 4 of 10; here the disagreement is nearly total, and in both
directions — `ok` True on a wrong configuration at 41,42,44,45,46, and `ok` False on a RIGHT one at
43 and 48.
*Falsified if the disagreement count is not 7, or if its sign pattern differs.*

**PC4D-7 — s42 §4(3), THE nlchain CONFIGURATION COLUMN, GOES FROM OWED TO BLOCKING.**
PC4P-7 filed the trigger explicitly: if `ok` and the configuration disagree anywhere in a row, the
column is mandatory. **PC4D-6 predicts seven disagreements, and predicts that the chained score
42/47 is not a statement about configurations at all.** If PC4D-6 holds, the chained score must not
be quoted as a configuration score again until the column exists.
*Falsified together with PC4D-6.*

**PC4D-8 — Z=43 AND Z=48 ARE THE TWO PLACES THE WALK IS RIGHT AND THE SCOREBOARD SAYS WRONG.**
At Tc and Cd the chain's configuration equals the record's exactly, and `ok` is False because the
record's PREVIOUS element is anomalous and `rectag` reads the record's step rather than the
record's state. **The walk re-converges onto the record at both, having passed through
configurations the record does not hold.** This is the strongest evidence the row can produce that
`ok` measures the wrong object, and it is predicted here in advance of the run.
*Falsified if the chain's configuration at 43 or 48 differs from the record's.*

**PC4D-9 — PD-6's EXCEPTION SET (argmax|Delta| vs argmin D) STAYS EMPTY THROUGH Z=48; PC3D-10's
EXPECTED FIRST BREAK AT Z=39..41 DOES NOT ARRIVE.**
PC3D-10 expected Delta's first break at the 4d/5s crossover. **I predict against it.** The
crossover at Z=39 is Pauli-forced — 5s closes at Sr and the seat is gone — and PC4P-4 showed a
Pauli-forced switch tests bookkeeping, not the field. Delta breaks where a channel is genuinely
contested, and nothing here is.
*Falsified by any non-empty exception set in Z=39..48. This is a prediction AGAINST a standing
expectation of an earlier session, and a break would be the more interesting result.*

**PC4D-10 — argmin n IS WRONG AT Z=39 AND Z=40, ADDING TWO MORE ELEMENTS TO THE SET {19,20,37,38}.**
At Y and Zr the field picks 4d, and the smallest available n among the candidates is 4 — which 4d
carries. **So argmin n is RIGHT at 39 and 40, and this claim is FILED AS FALSE ON PURPOSE**: it
states the negative so the run can score it, because the set {19,20,37,38} grows only where the
winner's n exceeds some available candidate's n. 4d has n=4 and beats 5p (n=5) and 6s (n=6); there
is no candidate with n<4 that is not full. **Predicted: PD-6's argmin-n exception set is UNCHANGED
at {19,20,37,38} across this entire row.**
*Falsified by any addition. Note this is a genuine asymmetry worth naming: n+l picks right at all
ten, and n also picks right at all ten, so THIS ROW DOES NOT DISCRIMINATE THE TWO. The 4d row is
the wrong place to look for ordering-variable evidence, and saying so before the run prevents a
null result being read as support.*

## 4 · WHAT IS NOT PREDICTED

Absolute D_ent magnitudes at Z=40..48 (no number is asserted; Z=39's is timing-flagged and
excluded from scoring). The size of 4d's promotion at Z=39. Iteration counts, `sec`, wall time.
Whether any channel fails to converge — `nfail` is unpredicted, and given F39.2's history at 4d
a non-zero `nfail` anywhere in this row is reportable but not a falsification of any claim above.
Anything at Z >= 49: the 5p row is not opened by this file.

## 5 · SCORING

Each claim is HELD or FAILED on the run, and a failure is logged with its mechanism, not explained
away. A timing-flagged claim that agrees is written CONSISTENT, not HELD. **PC4D-10 is filed
stating its own negative and is scored the same way — if the exception set grows, it FAILED, and
the growth is the finding.**

**Runtime note.** Ten steps, each solving a reference plus every open candidate at ~10 s per SCF,
with 12+ candidates per step. This will not complete in one tool call. Per the Zeno directive the
row is walked in segments — 39..41, 42..44, 45..46, 47..48 — and `nlchain` appends each row to
`nlchain.jsonl` as it goes, so a segment boundary is a resumption point and not a restart.
