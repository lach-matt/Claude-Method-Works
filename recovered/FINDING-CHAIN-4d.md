# FINDING-CHAIN-4d (s44, item 2) — THE ROW GOES 10/10 ON THE FIELD AND 4/10 ON THE RECORD, AND THE SCOREBOARD SAYS 7/10

## 0 · THE ROW

    Z   ent  rec    ok      D_ent    margin   vs   nfail
    39   4d   4d   True   -0.19561  0.04367   5p     2
    40   4d   4d   True   -0.24150  0.08243   5p     2
    41   4d   4d   True   -0.28612  0.12139   5p     2
    42   4d   4d   True   -0.33040  0.16098   5p     2
    43   4d   5s  False   -0.37474  0.20135   5p     2
    44   4d   4d   True   -0.41936  0.24256   5p     2
    45   4d   4d   True   -0.46440  0.28464   5p     2
    46   4d   4d   True   -0.50993  0.32758   5p     3
    47   4d   5s  False   -0.55601  0.37140   5p     3
    48   4d   5s  False   -0.60266  0.41607   5p     3

**Chain 37 -> 47 steps. Chained score 35/37 -> 42/47. FIRST DIVERGENCE unchanged at 25.**
Margins are quoted with the channel they are margins against, per F44.2's remedy. **The runner-up
is 5p at every one of the ten steps** — the identity does not change once, which is exactly the
stability the 4p row lacked and s43 did not notice it lacked.

## 1 · SCORING — 10 HELD, 1 CONSISTENT-BY-FLAG, 0 FAILED

**PC4D-0 HELD EXACTLY.** `rec_ent` is non-null at all ten and reads 4d at 39,40,41,42,44,45,46 and
5s at 43,47,48 — the predicted pattern with no exception. **And every one of the ten record
configurations in §2 of the prediction, quoted from recall, matches `ground.py` character for
character.** The recall was under prediction and it holds; that is worth one line because R 1639
and R 1645 are the reason it was put under prediction at all.

**PC4D-1 HELD.** 4d is the entrant at all ten steps. **The n+l = 6 tie-break (clause 2, smaller n
first) now holds on a THIRD distinct pair**: 4s/3d 10/10, 4p/5s 6/6, and now 4d/5p 10/10. Three
unrelated pairs, 26 steps, no exception. The clause is not a property of any pair it was found on.

**PC4D-2 HELD, WITH ONE WORD OF THE CLAIM WITHDRAWN.** 4d entered Z=39 in THIRD place at Z=38
(-0.09658, behind 5s -0.17457 and 5p -0.11818) and won. Measured: across 38 -> 39, **4d deepened by
0.09903 while 5p deepened by 0.03376** — a factor of 2.9 in one proton. That is the discontinuous
promotion F44.2 said the row would demand, and it is not a drift.
*Withdrawn: the claim said 4d "overtakes both 5p and 5s". **5s is not overtaken; it is not a
candidate.** It is full at Sr and `candidates()` excludes it. The overtaking is of 5p alone, and
the vacancy of the n+l = 5 group is the reason the promotion is discontinuous rather than gradual.
Stated rather than quietly dropped.*
*CONSISTENT, not HELD, at Z=39's magnitude (timing flag §0): D = -0.19561 against s42's filed
-0.195614. The re-derivation returns the probed value exactly. Per R 1645 that does not
retroactively convert the flag into a prediction.*

**PC4D-3 HELD, AND MORE STRONGLY THAN FILED.** The runner-up at Z=39 is 5p as predicted. Unfiled
and measured: it is 5p at all ten steps, so the row's margin column is for once a comparison
between the same two channels throughout, and the monotone widening 0.04367 -> 0.41607 means
something. **In the 4p row it did not, which is F44.2.**

**PC4D-4 HELD — AND THE HALF-SHELL IS THERE, THREE ORDERS BELOW THE BOUND.**
Per-proton steps: -0.04589, -0.04462, -0.04428, -0.04434, -0.04462, -0.04504, -0.04553, -0.04608,
-0.04665. Monotone deepening throughout, no reversal, **maximum excursion about trend ~0.0012
against a bound of 0.05** — the field is smooth across the whole d subshell.
Second differences: +0.00127, +0.00034, **-0.00006**, -0.00028, -0.00042, -0.00049, -0.00055,
-0.00057. **THE SECOND DIFFERENCE CHANGES SIGN BETWEEN 41->42 AND 42->43, AND THE PER-PROTON STEP
HAS ITS MINIMUM AT Z=42.** The chain's configuration at Z=43 is `[Kr]4d5 5s2` — the half shell.
The prediction filed the possibility in advance and named where it would sit; it sits there, as an
inflection of magnitude 6e-5, not as a swing. **The correct reading is the conservative one: the
field carries half-shell structure at the 1e-4 level and NOTHING at the 1e-2 level where the
record's anomalies live.** Exchange stabilisation at 4d5 cannot be what moves Nb, Mo, Ru, Rh, Pd
and Ag, because in this field it is four orders too small to move anything.

**PC4D-5 HELD EXACTLY, EVERY TERM.** `ok` True at 39,40,41,42,44,45,46 and False at 43,47,48 —
7/10 at precisely the predicted Z. Chained 35/37 -> **42/47**. **FIRST DIVERGENCE unchanged at 25**,
as predicted, because the definition takes the first False and 25 < 43.

**PC4D-6 HELD EXACTLY, AND IT IS THE ROW'S REAL RESULT.** Chain configuration against record:

    Z   chain config       record config      cfg match   ok      agree?
    39  [Kr]4d1 5s2        [Kr]4d1 5s2          YES      True     yes
    40  [Kr]4d2 5s2        [Kr]4d2 5s2          YES      True     yes
    41  [Kr]4d3 5s2        [Kr]4d4 5s1          no       True     **NO**
    42  [Kr]4d4 5s2        [Kr]4d5 5s1          no       True     **NO**
    43  [Kr]4d5 5s2        [Kr]4d5 5s2          YES      False    **NO**
    44  [Kr]4d6 5s2        [Kr]4d7 5s1          no       True     **NO**
    45  [Kr]4d7 5s2        [Kr]4d8 5s1          no       True     **NO**
    46  [Kr]4d8 5s2        [Kr]4d10             no       True     **NO**
    47  [Kr]4d9 5s2        [Kr]4d10 5s1         no       False    yes
    48  [Kr]4d10 5s2       [Kr]4d10 5s2         YES      False    **NO**

**CONFIGURATION 4/10. `ok` 7/10. THEY DISAGREE AT SEVEN OF TEN STEPS — 41, 42, 43, 44, 45, 46, 48 —
the exact set filed in advance.** In the 3d row the disagreement was 4 of 10; here it is nearly
total, and it runs in BOTH directions: `ok` True on a wrong configuration at five steps, `ok` False
on a right one at two.

**PC4D-7 TRIGGERED. THE nlchain CONFIGURATION COLUMN IS NOW BLOCKING.** PC4P-7 filed the trigger
explicitly and PC4D-6 has met it seven times over. **The chained score 42/47 is not a statement
about configurations and must not be quoted as one again until the column exists.** s42 §4(3) is
upgraded from OWED to BLOCKING and is the first item of the next session.

**PC4D-8 HELD.** At Tc(43) and Cd(48) the chain's configuration equals the record's character for
character, and `ok` is False at both. **The walk re-converges onto the record having passed through
configurations the record does not hold**, and the scoreboard marks the two places it is right as
wrong. `rectag` reads the record's STEP; the walk produces a STATE; where the record's previous
element is anomalous the two objects are not comparable, and nothing in the flag says so.

**PC4D-9 HELD, AGAINST A STANDING EXPECTATION.** `PD-6: entrant != argmax|Delta| at Z=[]`. The
exception set is still **EMPTY** with ten new steps in. **PC3D-10's expected first break of Delta
at Z=39..41 DID NOT ARRIVE**, and the prediction filed against it holds. The stated reason holds
too: the crossover at Z=39 is Pauli-forced — the n+l = 5 group closes at Sr — and a forced switch
tests bookkeeping, not the field. PD-5's 4f trace extends across Z=39..48 at |Delta| <= 1.2e-4,
still HELD.

**PC4D-10 HELD, FILED AS ITS OWN NEGATIVE.** `PD-6: entrant != argmin n at Z=[19, 20, 37, 38]` —
**unchanged across the entire row.** As filed: 4d carries n=4 and beats 5p (n=5) and 6s (n=6), and
no candidate with smaller n is open, so n and n+l agree at all ten steps. **THIS ROW DOES NOT
DISCRIMINATE THE ORDERING VARIABLE, AND SAYING SO BEFORE THE RUN IS WHAT STOPS A NULL BEING READ AS
SUPPORT.** The evidence for n+l over n still rests on four elements — K, Ca, Rb, Sr — from two rows.

## 2 · UNPREDICTED AND REPORTABLE — THE d-CHANNEL FAILURES ARE SYSTEMATIC

`nfail` was explicitly not predicted (§4 of the prediction). Measured:

    Z=39..45   5d, 6d fail          (nfail 2)
    Z=46..48   5d, 5g, 6d fail      (nfail 3)

**5d and 6d fail to converge at every one of the ten steps, and 5g joins them at exactly Z=46.**
This is the F39.2 class — the node-count failure that s42 diagnosed as a bound solution destroyed
by the first SCF update, not as an unbound channel. It does not touch any claim above: the failed
channels are far above the winner and `nfail` never reached the winning channel.

**But it is now diagnosable rather than merely countable.** Gate 80's `t7g_exc.HFCN` raises a
NAMED exception carrying (Z, n, l, e, nd, target) at precisely this condition, and it is inert
against the parent to bit-identity. **Running the row's failures through HFCN would name every one
of the 23 failures by channel, eigenvalue and node target for the cost of no new physics.** Filed
as the natural next use of the s43 instrument; not opened here, because this file scores a
prediction and does not open a new object.

The onset of 5g at Z=46 is stated as a measured fact and NOT explained. It coincides with the
chain's 4d8 configuration and with nothing else this file has measured.

## 3 · WHAT THE ROW ESTABLISHES

**The field walks the 4d row perfectly and the record does not.** Ten steps, one channel, no
convergence failure in the winner, a margin that widens monotonically over a runner-up that never
changes identity, and a subshell whose only internal structure is an inflection four orders below
the anomalies it would have to explain.

**The six anomalies of the 4d row are therefore NOT in the entrant channel.** The field is asked
which channel takes the next electron and answers 4d correctly at all ten; the record's departures
— Nb, Mo, Ru, Rh, Pd, Ag — are all s->d PROMOTIONS OF ALREADY-PLACED ELECTRONS, which a
one-electron-at-a-time walk cannot express and does not attempt. **The n+l rule is not what fails
at Nb; the walk's format is.** That is a statement about the solution format, and it is the
sharpest thing this row produces.

## 4 · NOT DONE HERE

Z=49..108. The configuration column (now BLOCKING). Naming the 23 channel failures through HFCN.
PV-3. Anything about WHY the record promotes at Nb, Mo, Ru, Rh, Pd and Ag — this file establishes
that the entrant walk cannot address it, and does not address it.
