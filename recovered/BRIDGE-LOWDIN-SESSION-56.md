# BRIDGE — LOWDIN SESSION 56 · THE TRANSIT WIDTH IS DERIVED

Open Session 57 with **`bash pack56/open56.sh`** and nothing else.
The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 56 DID

Opened clean, byte-for-byte. Answered §7 item 2 — the first proton of transit — and in doing
so found and closed a one-ended claim in s55's own §6.

    ORDERING CLAUSE   0 failures in 119 steps            unchanged (sealed chain)
    DERIVATION        107 rows, Z=2..108                 unchanged
    TRANSIT WIDTH     DERIVED, not identified.  Deliverable 3 §6's owed item DISCHARGED.
    4f FIRST PROTON   survives c=1e6 at BOTH ends -- s55 §6 was supported at one end only
    NEW               Deliverable 4, gates 94/95/96

**NOTHING IN THE SEALED CHAIN MOVED.** No sealed file was modified. Full replay 1..71 diffs
to pack55/GATES-55-OPEN.log in **ZERO LINES**, gate-6 `sec` included.

## §2 · THE RESULT, IN ONE STATEMENT

> At the atom where an f shell opens, the f channel is behind the d channel of its own shell
> by a **positive** amount that is **less than half of what one proton of collapse delivers**.
> A lag of zero is therefore impossible and a second transit proton is unnecessary.
> **THE WIDTH IS ONE.**

    swing(4f) = 0.22144 Ha = 2.21 x shortfall(57) = 0.10029
    swing(5f) = 0.13600 Ha = 2.52 x shortfall(90) = 0.05405

The width decomposes into two kinds of proton with different causes:

    width = (plateau protons, dn*/dZ ~ 0, gap cannot shrink) + (transit protons, gap not yet crossed)
    4f  rel & non-rel : 0 + 1 = 1
    5f  relativistic  : 1 + 1 = 2       5f  c=1e6 : 1 + 0 = 1
    ONLY THE TRANSIT PROTON IS TOUCHED BY RELATIVITY.

## §3 · TWO CLAUSES FALSIFIED, AND THEY ARE THE FINDING (gate 94, 8/10)

FP-2b predicted 4f second in its own shell at La. It is **third** — behind 6p as well as 5d.
FP-3c predicted the shortfall below 0.05. It is **0.10029**.
**The first proton is not a near-miss.** At both openings the f channel is behind *every*
penetrating channel of its own shell. It is not narrowly beaten; it is not competing.

## §4 · F56.3 — s55 §6 WAS SUPPORTED AT ONE END ONLY (gate 96, 6/6)

s55 concluded "the 4f transit is one proton in BOTH fields" from **Z=58 alone**, which shows
only that 4f *wins* at the upper end. Z=57 at c=1e6 had never been run. Run this session:

    SELFCHECK Z=80 |dE| = 1206.454498 Ha exact.   ent(57, c=1e6) = 5d.  4f STILL LOSES.
    shortfall 0.10029 -> 0.00288    4f/5d differential 0.09741 (vs 0.18300 at Z=90)

**s55's (1,1) survives and is now two-ended.** This is F55.2's pattern a third time: a real
number, correctly computed, made to carry more than it was measured across.

**RULING PROPOSED FOR M: A WIDTH IS NEVER ESTABLISHED FROM ONE END. Any claim of the form
"N protons" must exhibit the loss at the lower end and the win at the upper end, in the same
field. F44.2, F55.2 and F56.3 are one fault recurring in three costumes.**

## §5 · THE NAMED RESIDUE

The non-relativistic 4f first proton stands on **2.88 mHa**. The chain is deterministic and
reproduces bit-for-bit, so *"in this field, 4f loses at La even at c=1e6"* is secure. The
stronger reading *"the first proton is not relativistic"* rests on a margin **35x narrower**
than its sealed counterpart and is stated with that number attached. Residue is not closure.

## §6 · FAULTS THIS SESSION

    F56.1  PREDICTION-FIRSTPROTON's own formula line was mis-signed against its
           stated meaning; gate94 v1 implemented it literally and four clauses
           failed on SIGN, not physics                          REMEDIED (gate94 carries the
                                                                stated sign; filed file untouched)
    F56.2  gate95's OV-3/OV-4 ratio clause is VACUOUS at shortfall=0 and passed a
           deliberate corruption. A clause any positive number passes is not a
           clause. Found by can-fail, not by reading            REMEDIED (shortfall>0 required)
    F56.3  s55 §6 established the 4f width from its upper end only              REMEDIED (gate 96)
    F56.4  gate96 v1 read the self-check from the jsonl record, which never
           carried it, and reported a physics FAIL that was an input gap.
           It failed CLOSED, the correct direction                REMEDIED (reads the sealed log)

No fault carried open into s57.

## §7 · ORDERED WORK LIST FOR SESSION 57

1. **`bash pack56/open56.sh`.** Expect verify56 clean; full replay diff ZERO LINES.
2. **M'S RULING OWED, TWICE, AND BOTH BLOCK:**
   a. **§4's width ruling** above — adopt or reject.
   b. **IS CLAUSE 3 CLOSED?** Carried unanswered from s55 §7 item 3. It is answered on 12
      adversarially chosen rows (11 from s55 + Z=57 here) plus a screen; it is NOT answered
      exhaustively. Is the adversarial sample sufficient, or is a full 107-row c=1e6 walk
      owed? Cost of the full walk: ~107 x 150 s, several sessions.
3. **CLAUSE 1 — the reverse chain to the many-electron Schrodinger equation.** Reading is DONE
   (s53 §8 item 5). This is now the largest owed item in the whole solution and nothing
   upstream of it is open.
4. Deferred: −8.021 mHa residue at Z=59; coupled 4f2.5d SO check; promotion operator as an
   object; the 2.88 mHa residue of §5.
5. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s56.

## §8 · GATES AND PREDICTIONS

    gate 94  PREDICTION-FIRSTPROTON   8/10  two clauses FALSIFIED   can-failed 3 ways
    gate 95  PREDICTION-OVERSHOOT      6/6  PASS                    can-failed 2 ways
    gate 96  PREDICTION-Z57C           6/6  PASS                    can-failed 2 ways
                                            (canfail 2 is ordering-preserving by construction
                                             and correctly does not bite -- noted, not a defect)
    gates 1..71                        all rc=0, diff to reference = ZERO LINES

    PREDICTION-FIRSTPROTON.md  ecd3cc64479abfc5  15:15:35Z   before any read
    PREDICTION-OVERSHOOT.md    561239ae02c5de53  15:18:24Z   before any read
    PREDICTION-Z57C.md         cbcc3d249ab02f34  15:19:53Z   before the walk launched

R 1449 held at three of three.

## §9 · INSTRUMENTS ADDED

    pack56/fp56.py       side-by-side shell reader, n+l carried for every channel
    pack56/gate94.py     scores PREDICTION-FIRSTPROTON
    pack56/gate95.py     scores PREDICTION-OVERSHOOT
    pack56/gate96.py     scores PREDICTION-Z57C, relocation-safe input
    pack56/c3z57.jsonl   Z=57 at c=1e6, the missing end
    pack56/Z57C-selfcheck.log        the lever's own proof, sealed
    pack56/DELIVERABLE-4-THE-TRANSIT-WIDTH.md
    pack56/open56.sh     s57 open