# BRIDGE — LOWDIN SESSION 53 · CLAUSE 3 FIRED, NR-1 FALSIFIED AS STATED, INDUCTION 21/34

Open Session 54 with **`bash pack53/open53.sh`** and nothing else. It is open52.sh with
one change: **gate 86 is routed through `pack53/runsealed.py`**, without which the open
HALTS (F53.1). The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 53 DID

Fired clause 3, scored it, found the instrument confounded, built the control and the
induction that resolve it, and left the induction 13 rows short.

    ORDERING CLAUSE   0 failures in 119 steps    unchanged (sealed chain)
    DERIVATION        107 rows, Z=2..108         unchanged
    CLAUSE 3          NR-1 FALSIFIED AS STATED; induction 21/34, NOT CLOSED
    CT-1              HELD 11/11
    c=1e6 walk        107 rows complete, 167 minutes

---

## §2 · NR-1 IS FALSIFIED AND THE FALSIFICATION IS NOT ABOUT c

`cinf.jsonl`, 107 rows, Z=2..108, rc=0, no gaps, clight=1e6 on every row, every entrant
at rung 0. Scored by **gate 87** (written and can-failed BEFORE any row was read, its
ordering and tie-break tests lifted VERBATIM from sealed gate85):

    NR-1  ordering failures  [42,43,45,46,79]           FALSIFIED
    NR-2  tiebreak           [57,60,61,62,89,90,103]    FALSIFIED
    NR-3  |dD| < 1 mHa for Z<30 (measured 1.95 mHa)     FALSIFIED
    NR-4  HELD -- 11 confounded steps lacked a control
    NR-5  g channels unmoved                            HELD
    NR-6  ok 101/107 against 96/107                     FALSIFIED

**NOT ONE CLAUSE WAS REWORDED.** The instrument is the wrong one, and F53.2 -- registered
before the result was read -- is why that is provable rather than arguable.

At all five ordering failures the c=1e6 walk chose **the same entrant as the sealed
chain**. What differs is the candidate list:

    Z=42,43,45,46   offending channel 5s   occ=1 in OBSERVED(Z-1)   occ=2 FULL in CHAIN(Z-1)
    Z=79            offending channel 6s   occ=1 in OBSERVED(Z-1)   occ=2 FULL in CHAIN(Z-1)

The observed atom carries the s-hole the one-electron walk never made -- Deliverable 1
§5(a)'s promotion structure, reappearing in the candidate SET. A half-empty channel is
admissible; a full one is not present at all. Same for the extra tie-break failures: 4f
carries one MORE electron in the observed reference at 60-62, 6d two FEWER at 103. These
are statements about configurations and hold independently of c.

**POST-HOC, AND LABELLED SO.** On the 73 steps where both walks share a reference:
entrant differences NONE (73/73), ordering failures [], tie-break [57, 89, 90] exactly as
sealed, g channels shifted by 0.00e+00. **NR-2's falsifying branch did NOT fire** -- La,
Ac and Th survive c -> infinity, so Deliverable 3's collapse condition is NOT entangled
with the relativistic layer and Deliverable 1 §3 does NOT reopen. This partition was not
in the filed prediction and does not carry a pre-filed clause's weight.

---

## §3 · CT-1 HELD, 11 OF 11

`PREDICTION-CTRL137.md` (26f54de3ab...) filed 02:55:58 before the first control row.
The control is the SEALED, UNPATCHED nlchain.py in restart mode at c=137.035999 -- same
observed reference as cinf.py, so c is the only difference.

    Z    ctrl(c=137,restart)  cinf(c=1e6,restart)   sealed(c=137,chain)
    25/30      4s                   4s                    3d
    47/48      5s                   5s                    4d
    60/61/62   5d                   5d                    4f
    71         5d                   5d                    4f
    80         6s                   6s                    5d
    103        7p                   7p                    5f
    104        6d                   6d                    5f

Every disagreement is borne by the REFERENCE CONFIGURATION. **c-attributed entrant
changes over Z=2..108: ZERO.** CT-4 held: rung 0 throughout.

---

## §4 · THE INDUCTION — THE ARGUMENT THAT REPLACES A 2.8-HOUR RE-WALK

The entrant is a function of (Z, config(Z-1), c). If at EVERY Z the CHAINED reference
yields the same entrant at c=1e6 as at c=137.035999, then by induction on Z the chained
c=1e6 walk reproduces the sealed chain ROW FOR ROW and NR-1 follows rigorously rather
than by re-measurement. At the 73 clean steps cinf.py already supplied the c=1e6 side and
it agreed 73/73. Only the 34 confounded steps needed computing.

`PREDICTION-INDUCTION.md` (8a9aef3f95...) filed 03:39:21 before the first row.
`pack53/induct.py` rebinds c exactly as cinf.py does; no sealed file is touched.

**21 of 34 rows landed. Entrant agrees with the sealed chain at 21 of 21**, including the
whole 4f run through Z=71. **IN-1 IS NOT CLOSED AND IS NOT REPORTED AS CLOSED.**

    REMAINING: 92 93 94 95 96 97 98 99 100 101 102 103 104   -- the 5f block

`pack53/gate88.py` is written and in place to score CT-1 and IN-1..IN-5 the moment the
last row lands. It has NOT been can-failed yet -- do that before believing it.

---

## §5 · FAULTS

**F53.1 — A SEALED GATE THAT CANNOT RUN FROM A FRESH EXTRACT.** open52.sh HALTED at step
4. `pack52/gate86.py` and `pack52/cinf.py` both hard-code s52's absolute path
`/home/claude/s52/LOWDIN-HANDOFF-51/rt` in a sys.path.insert and an os.chdir. One of the
two was the clause-3 instrument. **Remedy `pack53/runsealed.py`** (F44.1 precedent): reads
the sealed source, rebinds the ONE path literal, execs in memory, proves the substitution
touched nothing else, prints the sealed sha256, refuses a tree with no nlchain.py.
Can-failed both directions (wrong tree -> rc=3; flipped expectation -> 18/19 FAIL rc=1).
Sealed hashes still match MANIFEST-52. Gate 86 then PASSES 19/19.

**F53.2 — THE CLAUSE-3 INSTRUMENT IS CONFOUNDED, AND ITS SCOPE IS WIDER THAN FIRST
REGISTERED.** cinf.py walks RESTART mode against a CHAINED sealed walk; references differ
at 34 of 107 steps. Registered BEFORE the result was read, which is the only reason the
falsification could be read correctly. **Scope extension found on scoring: the confound
reaches the CANDIDATE SET, not merely the entrant.** That is what falsified NR-1. Gate 87
partitions entrant disagreements; a successor should partition candidate sets too.

**F53.3 — A DETACHED JOB MAY BE REAPED AT A TURN BOUNDARY.** Bridge 52 §5 ruled that only
a chat handoff kills a detached run and the F49.2 remedy was written to that assumption.
Observed across s53: five turn crossings, **four reaps**, one survival -- pid 857 (Z=43),
975 (Z=61), 487 twice (Z=27 of the induction, then Z=104). Not memory: 3.8 GB free each
time. **The ruling is MAY, not DOES**, because the negative instance was observed.
Operational rule: poll inside a single turn, mirror per segment, resume from the last
flushed Z. Cost is one row per crossing.

**A CORRECTION TO A SEALED ESTIMATE.** Bridge 52 §8 projected ~45 s/row and ~80 minutes
from a single Z=24 row. Measured: 40 s/row to Z=33, 85 s/row by Z=43, 120-200 s/row above
Z=60; **167 minutes for 107 rows.** Counts from the instrument, not from the estimate.

---

## §6 · GATES

Gates 1..71 replayed from a fresh extract at open: **283 lines, 71 rc=0, diff to the
pack52 reference confined to gate 6's `sec` field** (8 -> 16, CPU contention), which is
the documented exclusion. Eight smoke gates PASS. verify52.sh at open: **ok=1054 bad=0
extra=0**. Gate 86 PASS 19/19 via the F53.1 remedy. **Gate 87 NEW** -- reconciled against
sealed gate85 (fed nlchain.jsonl it returns [], [57,89,90], 94, 96/107 exactly) and
can-failed on NR-1. **Gate 88 NEW, NOT YET RUN, NOT YET CAN-FAILED.**

---

## §7 · WHERE THE TIME GOES — MEASURED, FOR THE SPEEDUP RULING

    Z= 30   9 channels   41 s   SCF iterations per channel  30/31/32
    Z= 60  13 channels  106 s                               33/33/37
    Z= 90  14 channels  169 s                               38/38/43
    Z=108  13 channels  151 s                               38/38/38

**Every candidate re-converges from the same cold TFD start, taking the same ~38
iterations, though it differs from the already-converged reference by ONE electron.**
Second multiplier: eigen_sr finds each eigenvalue by 200 bisection halvings, each a full
Numerov shoot, on a bracket the node count already established. `nproc` = 1, so the
independent per-channel solves are serialised.

**The warm start does double duty.** Family B was rejected because the potential was
GUESSED; our TFD start is a guess too, and the defence -- that it is iterated away and
does not survive convergence -- has never been demonstrated, only assumed. Starting from a
different potential and recovering the same depths IS that demonstration. Gate it by
re-deriving the sealed 107 rows and requiring the identical entrant at every step.
REFUSED: perturbative screening as a REPLACEMENT for the ΔSCF (it degrades the object to
an eigenvalue ordering), and pruning any channel by expectation.

---

## §8 · ORDERED WORK LIST FOR SESSION 54

1. **`bash pack53/open53.sh`.** Expect verify53 clean, gates 1..71 diff to gate-6-`sec`
   only, gate 83 (73,107)/(96,107), gates 85 and 86 PASS.
2. **RESUME THE INDUCTION, FIRST THING.** 13 rows, ~35 minutes:
       cd rt && bash run.sh IND 'python3 ../pack53/induct.py /tmp/induct.jsonl 92 93 94 95 96 97 98 99 100 101 102 103 104'
   First `cp pack53/induct.jsonl /tmp/induct.jsonl` -- the 21 completed rows are in the
   pack and must NEVER be recomputed. Poll inside ONE turn (F53.3).
3. **Can-fail `pack53/gate88.py`, then run it.** It scores CT-1 and IN-1..IN-5 against
   both pre-filed predictions and reports CLAUSE 3 INDUCTION CLOSES / does not.
4. **If IN-1 holds at all 34: clause 3 CLOSES and Deliverable 1 §6.1 is STRUCK** -- the
   ordering clause is then derived from the non-relativistic field, not merely from a
   scalar-relativistic one. Rewrite §6.1 and §0 accordingly. If any row disagrees, the
   full chained c=1e6 re-walk is mandatory from that Z onward. Report either way.
5. **Then clause 1** -- the reverse chain from the many-electron Schrödinger equation to
   the field actually solved. The reading is DONE: the ruling field is hfc2/HFSR with
   CORR=False; the entrant is a **ΔSCF total-energy difference, not an eigenvalue**;
   exchange is Gaspar-Kohn-Sham (Vx = -(3rho/pi)^(1/3), alpha=2/3 DERIVED, not fitted,
   with Ex = (3/4)∫rho·Vx giving the -1/4 term exactly); the Latter tail enforces the
   asymptotic -q/r; TFD enters ONLY as an SCF starting guess. Each of these is an
   approximation to be NAMED and its effect on the ordering BOUNDED. The warm-start test
   of §7 supplies the TFD one.
6. Deferred: the transit width; the -8.021 mHa residue at Z=59; the coupled 4f2.5d SO
   check; the promotion operator as an object.
7. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s53.
