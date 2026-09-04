# PREDICTION-4f-COLLAPSE (s46, item 1 — BINDING per s45 bridge §5(1))

Filed BEFORE nlchain is pointed at Z=55. R 1449. Nothing below is read from a run past Z=54.
All baseline figures are DERIVED at this session's open from sealed `nlchain.jsonl`
(53 rows, md5 e00cf4e50c35), not recalled from the s45 bridge.

## 0 · THE BASELINE, DERIVED — AND ONE CORRECTION TO s45

    Z   D_4f      Zeff      Zeff-1        Z   D_4f      Zeff      Zeff-1
    39  -0.03137  1.001918  +0.001918     47  -0.03128  1.000480  +0.000480
    40  -0.03135  1.001599  +0.001599     48  -0.03128  1.000480  +0.000480
    41  -0.03133  1.001279  +0.001279     49  -0.03127  1.000320  +0.000320
    42  -0.03132  1.001119  +0.001119     50  -0.03129  1.000640  +0.000640
    43  -0.03130  1.000800  +0.000800     51  -0.03129  1.000640  +0.000640
    44  -0.03130  1.000800  +0.000800     52  -0.03128  1.000480  +0.000480
    45  -0.03129  1.000640  +0.000640     53  -0.03128  1.000480  +0.000480
    46  -0.03128  1.000480  +0.000480     54  -0.03128  1.000480  +0.000480

Zeff = sqrt(-32 D). Hydrogenic 4f at unit charge is exactly -1/32 = -0.03125.

**CORRECTION TO s45 §2(9).** That finding states the deviation "shrinks MONOTONICALLY
toward 1 as Z rises." **The sealed data does not support this across the full range.** It
shrinks monotonically Z=39..49 (0.001918 -> 0.000320), then RISES at Z=50 to 0.000640 and
settles at 0.000480 for Z=52..54.

**AND THE REASON MATTERS MORE THAN THE CORRECTION.** `D` is stored to five decimals, so
dD = 1e-5 maps to dZeff ~ 1.6e-4. **Every value in the table above is an integer multiple of
1.6e-4**, and the Z=50 excursion is exactly ONE such unit. The fine trend is at or below
storage resolution and monotonicity cannot be read from it in either direction.
**WHAT SURVIVES IS THE FLATNESS, WHICH IS FAR ABOVE RESOLUTION**: sixteen elements, sixteen
added protons, total spread 1.4e-3 in Zeff and 9e-5 in D. That is the baseline the collapse
must be measured against, and it is stated at the precision it actually has.
The largest single-step change anywhere in the baseline is **3.2e-4** (Z=39->40).

## 1 · THE MECHANISM, STATED SO IT CAN FAIL

The l=3 effective potential carries a centrifugal term 6/r^2 dividing an INNER well near the
nucleus from an OUTER hydrogenic well. An uncollapsed 4f electron sits in the outer well,
outside the whole core, and sees unit charge however large Z becomes — which is why D_4f is
inert to sixteen added protons. Collapse is **transfer of the wavefunction between wells**,
not continuous contraction of one well.

**Consequence, and it is the whole prediction: the departure from Zeff = 1 is DISCONTINUOUS
in Z, not gradual.** Sourced: Goeppert-Mayer, Phys. Rev. 60 (1941) 184-187;
Griffin, Andrew & Cowan, Phys. Rev. 177 (1969) 62-71. Already in the chain
(PARTS-OF-THE-LAW §3), not imported for this.

## 2 · THE CLAIMS

**PC4F-1 — 4f DOES NOT COLLAPSE AT Cs(55) OR Ba(56).** Zeff stays inside [1.000, 1.002] and
D_4f inside [-0.0314, -0.0312] at both. The entrants at 55 and 56 are 6s electrons, which lie
OUTSIDE nothing 4f is inside; they cannot open the inner well.

**PC4F-2 — 4f DOES NOT COLLAPSE AT La(57) EITHER, AND THIS IS THE LOAD-BEARING CLAUSE.**
Zeff(57) stays inside [1.000, 1.010]. **Basis: 5d is ALREADY twice as deep as 4f and is
deepening while 4f is flat** — 5d runs -0.06111, -0.06233, -0.06350 at Z=52,53,54
(~0.0012/proton) against 4f's -0.03128 unmoved. For 4f to take the step at 57 it must cross
a threshold that is receding from it.

**PC4F-3 — THE FIELD SELECTS 5d AT Z=57, SO THE STEP COLUMN PASSES AT La.** Record:
La(57) = [Xe]5d1 6s2. Predicted ent = 5d, ok(57) = True. Predicted D_5d(57) in
**[-0.085, -0.060]** — a band, widened below the naive extrapolation because two 6s electrons
enter at 55 and 56 and screen 5d.

**PC4F-4 — AND THE n+l RULE SELECTS 4f AT Z=57, SO THE RULE AND THE FIELD DIVERGE.**
4f and 5d both carry n+l = 7; clause 2 (smaller n first) names 4f. **The rule is therefore
predicted WRONG at La while the field is RIGHT.** This is PART 3 arriving exactly where
PARTS-OF-THE-LAW §1 said it would, and it is the first step in 56 where the two disagree.
**The tie-break clause's unbroken run — 32 steps, four pairs — is predicted to BREAK HERE,
on its fifth pair, and to break for a stated reason rather than by exception.**

**PC4F-5 — COLLAPSE ARRIVES AT Ce(58), IN ONE STEP.** Record Ce(58) = [Xe]4f1 5d1 6s2, so the
record's step raises 4f. For the walk to agree, D_4f must fall BELOW D_5d between 57 and 58:
a drop of **at least 0.03 Ha in a single proton**, against a sixteen-element baseline whose
largest step is 9e-5 in D. Predicted Zeff(58) > **1.4** (from |D| > 0.06), i.e. the deviation
from 1 grows by **more than three orders of magnitude in one step**.
**Falsified by any gradual approach**: if Zeff passes through 1.05-1.25 at some Z and stays,
the double-well account is wrong and collapse is contraction after all.

**PC4F-6 — THE FIRST Z WITH Zeff - 1 > 0.01 IS IN {58, 59}, SHARPEST SINGLE VALUE 58.**
Falsified by any Z <= 57 showing it — and note that PC4F-2, PC4F-3 and PC4F-6 fail TOGETHER
if collapse comes early, because an early collapse takes the step at La and breaks the record.

## 3 · WHAT WOULD FALSIFY THE ITEM ENTIRELY

Any of: Zeff leaving [1.000, 1.002] at Z=55 or 56; collapse at or before 57; no collapse by
Z=60; a collapse spread smoothly over three or more Z; or 4f taking the entrant step at any
Z <= 57. **Each is decidable in one chain step and none requires a new instrument.**

## 4 · THE FLAG THAT MUST CLEAR FIRST (F46.1)

`6p` is stored at **-0.07617 (52), -0.07922 (53), +0.11105 (54)** — a bound channel unbinding
by 0.19 Ha as one proton is added. **6p carries n+l = 7 and is therefore a live candidate at
exactly the step PC4F-3 and PC4F-4 are about.** If that value is an artefact it may displace
5d in the ordering at 57 and the openings test reports on a corrupted ladder.
**RESOLVED BEFORE Z=57 IS SCORED, NOT AFTER.** Nothing in §2 is scored until it clears.

## 5 · UNPREDICTED, DECLARED AS UNPREDICTED

The collapse's exact D_4f at 58 (only that it is below D_5d). Whether 5g and 6g continue to
fail to converge. `nfail`, iteration counts, the `sec` field. Whether cfg_ok holds at 57 and
58 — the record carries 5d1 at both, and a walk with no promotion operator may or may not
reproduce it; that is part 2's business, not this file's.
