# AMENDMENT — THE STALE LINES. SESSION 70, ON M'S INSTRUCTION.
# NO SEALED FILE IS EDITED. Standing 4, F44.1 route. This file carries exact
# replacement text and its receipts, and nothing else.
# Every receipt below is a file opened in session 70. Nothing rests on s69's scoring,
# which was made without DELIVERABLE-5, pack59 or pack60 open.
# The only number ever entered into the chain remains c = 137.035999.

---

## A1 · ASSEMBLY-RUNG-0 §5 — L2 IS BOUNDED. MOVE THE LINE.

REMOVE from **OPEN, NAMED, NOT WORKED**:

    * L2: finite nuclear size and mass are not modelled and not bounded here.

ADD to **BOUNDED, WITH THE BOUND STATED**:

    * L2 finite nuclear size: measured s64, first-order PT on point-nucleus orbitals.
      |dD| = 0.27480 mHa at Z=89 and 11.61091 mHa at Z=120; entrant unchanged at all
      three rows tested (Z = 3, 89, 120). Margin-to-shift 212 at Z=89, and 0.15 mHa
      on the tightest margin in the chain. **The 0.05 mHa working floor covers
      numerics and does not cover the nucleus** — S2 was FALSIFIED at 232x the floor
      and the falsification stands in the record.
      Nuclear MASS: exact scaling argument only (uniform mu/m on every channel,
      margins scale identically, argmin invariant). The SMS bound 0.016 mHa at Z=3 is
      declared ORDER-OF-MAGNITUDE and is not to be quoted as measured.

RECEIPT: `pack64/SCORE-L2-FINITE-NUCLEUS.md`, "LEDGER CONSEQUENCE" — *L2 moves from
APPROXIMATION, UNBOUNDED to BOUNDED, WITH THE BOUND STATED, at 0.15 mHa on margins
for Z <= 108.* Prediction sha 5765c6d0…, filed 20:53:46Z before any solve.

**AND IT SPLITS THE WALK.** Z<=108 carries factor 212; Z=120 carries factor 7.3, the
finite nucleus eating 14% of the margin. **A second and independent reason not to
claim rows above Z=108**, reached from a different direction than the missing
measured configuration. The scope limit is now supported twice.

---

## A2 · ASSEMBLY-REVISION-S64 R3 IS SUPERSEDED BY ITS OWN SESSION'S SCORE.

R3 reads, of the L2 line: *"STAYS, and is now the only link in the twelve-link chain
carrying no number."* **That is false as of the same session.** `SCORE-L2-FINITE-
NUCLEUS.md` gives L2 a number and moves it out of the open list. R3's FIRST half —
the single-configuration line sharpened with the four measured first-entry rows —
stands unaffected and is not withdrawn.

Registered as **F70.3**, against s64's draft, not against its measurement. Neither
file is edited. The correct closing sentence of the ledger is the score's own:
**every one of the twelve links now carries a number except correlation**, which is a
declared restriction of the model rather than a hole — and which must never be
reported as a proof that correlation cannot change the ordering.

---

## A3 · DELIVERABLE 1 §6 — ITEMS 1 AND 2 ARE DISCHARGED. REPLACE BOTH.

**§6.1** was written at s52 and its owed clause reads: *"eleven rows are not 107. The
sample is adversarial... the remaining rows are SCREENED... not WALKED. A screened row
is not a walked row and is never counted as one."*

REPLACE THE OWED CLAUSE WITH:

    DISCHARGED, s57 + s59 + s60. Coverage is 107/107 and no row is screened.
      94 rows IMMUNE combinatorially — entrant and runner-up share n+l, so no value
      of c can reach the ordering clause. Depends on no walk (D5 §1).
      13 rows EXPOSED, all s-closing, max Z=88 — and ALL THIRTEEN WALKED at c=1e6.
      EX-1 HOLDS 13 of 13: every entrant at c=1e6 is the entrant at c=137.035999.
      The instrument was proven live before the rows were read (EX-2: shift rises
      monotonically to 49 mHa), and the reference construction was verified
      IDENTICAL at 13/13 before the comparison was believed (F60.3), so the two
      sides differ in c and in nothing else.
    **The ordering clause is not a relativistic effect anywhere it could be one.**

RECEIPTS: `DELIVERABLE-5-CLAUSE-3-COVERAGE.md` §1 · `pack59/BRIDGE-LOWDIN-SESSION-59.md`
§3 (the 13 rows named with margins) · `pack60/SCORE-EXPOSED-13.md` (prediction sha
6a04409318b8881c verified before any row read) · `pack60/BRIDGE-LOWDIN-SESSION-60.md`
§1, *"94 + 13 = 107/107."*

**§6.2** reads: *"THE REVERSE DERIVATION — the explicit chain from the many-electron
Schrödinger equation to the field actually solved... Owed since s47 item (10)."*

REPLACE WITH:

    DISCHARGED, s63. `pack63/ASSEMBLY-RUNG-0.md`: twelve links L1..L12 in reverse
    from the exact many-electron Schrodinger equation to `nlchain.step`, each with a
    file:line receipt into the sealed runtime and each classified DERIVED, BOUNDED,
    APPROXIMATION, NUMERICAL CONTROL or SEED-ONLY.

---

## A4 · ONE FURTHER STALE ITEM, FOUND WHILE FIXING THESE

`pack60/SCORE-EXPOSED-13.md` EX-4 fails at Z=19 and states what is owed: *"a floor for
the restart walk, or a targeted re-run of Z=19."* It appears in no later work list and
in no residue list, including s69 §3. **It does not touch EX-1** — the Z=19 entrant is
4s in both fields — and EX-4 was RETIRED by M's ruling at s59 as an ordering not
required by any Challenge clause. Recorded here so it is carried knowingly rather than
lost silently.

---

## WHAT THIS AMENDMENT DOES NOT DO

It adopts nothing. R1, R2 and R3-first-half of `ASSEMBLY-REVISION-S64.md` remain
**deferred by M's ruling to formalisation time** (s65 §6) and are untouched here.
It edits no sealed byte, moves no margin, changes no entrant, no ordering, no rung, no
gate and no prediction sha. It corrects three statements of STATUS that the archive's
own later files already contradict.
