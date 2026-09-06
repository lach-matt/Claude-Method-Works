# BRIDGE — LOWDIN SESSION 57 · THE WALK WAS ALREADY IN THE ARCHIVE

Open Session 58 with **`bash pack57/open57.sh`** and nothing else.
The only number ever entered into this chain remains **c = 137.035999**.

---

## §1 · WHAT SESSION 57 DID

Opened clean, byte-for-byte. verify56 **ok=1127 bad=0 extra=0**, both halves.
Full replay of gates 1..71 diffs to pack55/GATES-55-OPEN.log in **ZERO LINES**.

Executed M's ruling RULING-56-LET-THE-MATH-DECIDE: both blocking questions were
withdrawn as rulings and re-issued as instruments. **The math answered them, and it
answered a question that had not been asked.**

    ORDERING CLAUSE     0 failures in 119 steps        unchanged (sealed chain)
    DERIVATION          107 rows, Z=2..108             unchanged
    INSTRUMENT B        N_exp = 13, EXACTLY as predicted, row set exact
    CLAUSE 3            the 107-row c=1e6 walk EXISTS, sealed since s53
    NEW                 Deliverable 5, gate 97

**NOTHING IN THE SEALED CHAIN MOVED.** No sealed file was modified.

## §2 · THE RESULT, IN ONE STATEMENT

> **94 of the 107 derivation rows cannot reach the ordering clause at any value of c**,
> because entrant and runner-up share n+l and a within-shell reversal is tie-break only.
> The 13 that can are exactly the s-closing rows of each n+l group. All 13 have already
> been walked at c=1e6. **La and Ac — Madelung's own two counterexamples — are among
> the 94 immune.**

## §3 · THE FIND (F57.4) — CLAUSE 3'S WALK WAS NEVER OWED

s56 §7 item 2b asked M to rule whether a full 107-row c=1e6 walk was owed, costing it
at "~107 x 150 s, several sessions."

**`pack53/cinf.jsonl` is that walk.** 107 rows, Z=2..108, `clight = 1000000.0`,
mode `cinf`, sealed session 53, scored by gates 87 and 88, in every manifest since.
The ruling M was asked for was a ruling on whether to redo completed work.

## §4 · F57.2 — F56.3's STATED GROUND IS FALSE

s56 recorded F56.3 as "s55 §6 was supported at one end only — Z=57 at c=1e6 had never
been run." **`pack54/c3.jsonl` contains Z=57 at c=1e6, sealed in s54.** pack56 re-ran it
and reproduced it **bit-for-bit in every physics field**; only wall-clock `sec` differs.

s56's physics conclusion is untouched and is now independently reproduced across two
sessions and two builds — an unplanned determinism check that passed. **But s55 was
two-ended all along, and F56.3 was a search failure, not an evidence gap.**

## §5 · FAULTS THIS SESSION

    F57.1  PREDICTION-B's Z^4 envelope normalised at Z=91 does not contain the
           Z=57 point. Falsifier FIRED as filed.        REFUSED, not re-normalised
    F57.2  F56.3's stated ground is false; pack54/c3.jsonl held Z=57 at c=1e6
                                                        REGISTERED (physics unaffected)
    F57.3  gate97 v1 ASSERTED the walked set from memory instead of reading it.
           Found by reading the archive, not by the gate    REMEDIED (read from jsonl)
    F57.4  the exhaustive c=1e6 walk existed and was costed as unbuilt   REGISTERED
    F57.5  gates 87, 88 and 96 read /tmp and do not survive a fresh extract.
           Third instance of one relocation fault class     REMEDY OWED (see §6 item 2)

No fault carried open into s58 except F57.5's remedy, which is named below.

## §6 · ORDERED WORK LIST FOR SESSION 58

1. **`bash pack57/open57.sh`.** Expect verify clean; full replay diff ZERO LINES.
2. **F57.5 REMEDY, FIRST AND MECHANICAL.** Make gates 87, 88, 96 relocation-safe the
   way gate 96 v2 was, and put 87 and 88 into the smoke list. An unenforced gate is
   not a gate (s51 precedent), and these two were silently absent for four sessions.
3. **ATTRIBUTE THE FIVE NR-1 FLAGS — THE ONLY THING CLAUSE 3 STILL OWES.**
   gate 87 flags ordering failures at **Z = 42, 43, 45, 46, 79** in the c=1e6 walk.
   All five are s->d promotion anomalies (Mo, Tc, Rh, Pd, Au) where the RESTART-mode
   reference leaves the lower s channel open, so the runner-up is 5s/6s (lower n+l)
   instead of the sealed chain's 5p/6p (equal n+l).
   **PREDICTION TO FILE BEFORE RUNNING: all five reproduce identically at
   c = 137.035999 in restart mode, proving them a format artefact and not a c-effect.**
   The control is **`pack53/ctrl137.jsonl`, already sealed.** Cost: a read, not a solve.
   If they reproduce, Clause 3 CLOSES.
4. **NR-4's 11 CONFOUNDED STEPS** — [25, 30, 47, 48, 60, 61, 62, 71, 80, 103, 104].
   gate 87 has correctly HELD these unscored since s53. Same control resolves them.
5. **M'S RULING OWED — ONE, AND IT REPLACES THE s56 WIDTH RULING:**
   > Before any claim that evidence is MISSING, and before any cost estimate for
   > producing it, the sealed archive must be searched for it BY CONTENT. A declared
   > gap that the archive already fills is a fault against the declarer.
   Adopt or reject. Instrument A is suspended, not withdrawn; its prediction file
   is filed, unscored, and its ONE-ENDED-UNCHECKED by-product is still owed.
6. **CLAUSE 1 — the reverse chain to the many-electron Schrodinger equation.** Reading
   DONE (s53 §8 item 5). **This is now the largest owed item in the whole solution**,
   and after item 3 nothing upstream of it is open.
7. Deferred: -8.021 mHa residue at Z=59; coupled 4f2.5d SO check; promotion operator
   as an object; the 2.88 mHa residue of s56 §5.
8. **T4 (R 1701 onward) — LAST. Not opened in any working session.**

Bank restore-point-2_13 (R 1700) untouched throughout s57.

## §7 · GATES AND PREDICTIONS

    gate 97  PREDICTION-B-EXPOSED    6/7   B-3b FALSIFIED   can-failed 3 ways, all bite
    gate 87  re-pointed, run          NR-1 5 flags, NR-4 HELD  (sealed s53, unenforced)
    gates 1..71                       all rc=0, diff to reference = ZERO LINES

    PREDICTION-A-WIDTH.md      f1e2b484bc1f4e96   15:38:25Z   before any read  UNSCORED
    PREDICTION-B-EXPOSED.md    512ae671d2fa0a8f   15:38:25Z   before any read  SCORED 6/7

R 1449 held at two of two.

## §8 · INSTRUMENTS ADDED

    pack57/gate97.py                          Instrument B, can-fail in three directions
    pack57/PREDICTION-A-WIDTH.md              filed, suspended, unscored
    pack57/PREDICTION-B-EXPOSED.md            filed, scored 6/7
    pack57/RULING-56-LET-THE-MATH-DECIDE.md   the loose s56 deliverable, now folded and hashed
    pack57/DELIVERABLE-5-CLAUSE-3-COVERAGE.md
    pack57/open57.sh                          s58 open
