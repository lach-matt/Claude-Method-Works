# SESSION 83 — COMBINED HANDOFF
# Open Session 84 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-83 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108.

## §0 · OPEN
`bash pack58/open58.sh` passed: s82 seal **1375/1375 root MATCH**, STATE CARD CLEAN,
canary CLEAN. M ruled at open: **adopt the g-ladder as clause 1's object, run (a) and
(b) for the comparison, bind doubt82, and hand Item 2 forward.**
**ITEM 1 WORKED ALL SESSION. ITEM 3 DISCHARGED. ITEM 2 SET UP AND HALTED.**

## §1 · ITEM 1 — CLAUSE 1. **NOT CLOSED. THE TARGET IS NARROWED FOR THE FIRST TIME.**
pack83/RESULT-S83-ITEM1-THE-g-LADDER.md. Predictions 86da5c2b...4c5b7b7e and
8f9aa8d8...be843c81, each filed and hashed before its run. Instruments gtest83.py and
front83.py, both f811 lint rc=0, all can-fails passed and gated.

**THE DERIVED EQUIVALENCE.** s82's q_eff = −rV = 1.000000 licenses an exact defect
representation. With σ = n+ℓ: **ν = σ − g(ℓ), g(ℓ) := ℓ + δ(n,ℓ)**. Madelung is
EXACTLY equivalent to (G-within) g increasing in ℓ inside a σ-class — the tie-break —
and (G-across) max g(σ+1) − min g(σ) < 1 — the n+ℓ ordering. **A change of
coordinates, not a result**; its value is that the threshold is the pure number 1 and
carries no units, where CLOSE-S78 §3 showed the eigenvalue form cannot be assumed.

**THE FRONTIER RESULT.** On the w lowest-ν channels per row:
| w | 2 | 3 | 4 | 5 | 6+ |
|---|---|---|---|---|---|
| rows failing (of 107) | **1** | 6 | 28 | 42 | 43 |
**NO CLEAN WIDTH EXISTS.** But at w=2 the relaxed field is Madelung-ordered at
**106 of 107, sole exception Z=90 — thorium**, the same element clause 3 carries.
w=3 failures are 19, 20, 38, 57, 88, 90 — every one a block-opening crossing. **At La
the field ranks 5d above 4f and OBSERVATION AGREES WITH THE FIELD.** Four of the six
are places where the derived field is right and the rule being derived is wrong.
**DECLARED LIMITATION:** the window is a ν-window, so a disagreement is invisible
until the Madelung-favoured channel rises into the top w (5f is ν-rank 5 at Ac). The
F82.2 shape, declared in advance this time.

**ROUTE (b), AND IT IS ALIVE AGAIN.** At Z=90 the relaxation is 89.901 mHa against a
79.244 mHa gap — **113%**, which killed the fixed-field target. The same term in
g-units is **+0.42226 against a decision unit of exactly 1 — 42%.** Both ladders give
the same verdict. **ONE ROW. It must not travel until Z=91 is run** — the identical
flag s79's 10.1 mHa carried and s81 discharged against it.
**ROUTE (a) IS A PRESENTATION OF (c), NOT AN ALTERNATIVE** (P8, held).

**CLAUSE 1 NOW ASKS FOR:** *derive a property of F_core forcing g(rank 1) > g(rank 2)
at the width-2 frontier, and account for Z=90.* **The global statement is measurably
FALSE — 43 of 107 — and the derivation never needed it.** That narrowing is the
session's one durable deliverable.

## §2 · ITEM 3 — R82.2 DISCHARGED. **THE CONTROL FAILED, AND THAT IS THE COMPLIANCE.**
doubt82's first binding to a physical instrument. Trusted: penetrating channels ℓ≤3 —
**PASSED** (6d at Z=90, g = 6.381784 against 6.382 filed). **DOUBTED: the ℓ=4
channels, whose banked D sit at the hydrogenic −1/(2n²) — FAILED**, max spread over Z
1.00e−05, max |D + 1/(2n²)| 5.92e−06. Every claim in §1 is restricted to ℓ ≤ 3 and
says so. **The threshold was 1e−5 and the measurement landed ON it — my number, and
the ℓ=4 variation sits exactly at F47.3's mixed-rung resolution limit.**

## §3 · ITEM 2 — SET UP, EXERCISED ON REAL ROWS, **AND HALTED ON ITS OWN FAULT**
Prediction **631d5861...a49ed538** filed and hashed. Driver pack83/stat84.py: second
chain to statchain.jsonl, no sealed row edited, scored on ORDERING, resumable ledger
(F53.3), both floors written per row, lint rc=0, can-fails passed.
**COST MEASURED: sealed chain 10,887 s / 107 rows. Stationary ≈ 8–12× ⇒ 24–36 hours.
IT DOES NOT FIT ONE SESSION AND MUST NOT BE ATTEMPTED IN ONE.**

**F83.2 — THE RESTART LEVER IS DEAD.** The real-row exercise at Z=2,3,4 PASSED its
filed verdict (entrants 1s/2s/2s, |dD| = 0.005/0.002/0.003 mHa, C10 correct) **and
the pass is what exposed the fault**: every row came back `passes=1, offset
+0.000000`. `stationary()` calls run_guarded twice with **no re-seed of P0/EPS0**, so
the second call repeats the same deterministic SCF and the offset is zero **BY
CONSTRUCTION, NOT BY PHYSICS.** conf82 re-seeds; this does not.
**THE STANDING METHODOLOGICAL LAW IS EXACTLY THIS LAW, AND I BROKE IT:** an
instrument that varies a parameter must demonstrate the parameter moves the output
before any row. **ELEVENTH APPEARANCE OF THE SPECIES IN SIX SESSIONS.**
**Zero rows survive.** statchain.jsonl DELETED — otherwise resume would have silently
skipped three non-stationary rows into the stationary chain at s84. Driver stamped
`LEVER_DEAD = True`; `run` halts rc=4 and the halt is verified.
**AND THE LOW-Z SITING IS THE SECOND HALF OF THE LESSON:** offset = 0 is also the
correct physical answer at Z=2,3,4, so the exercise was sited where a dead lever and
a live one look identical. **F82.2 again, in a new instrument, one session later.**

## §4 · FAULTS REGISTERED THIS SESSION
* **F83.1** gtest83 scored the FULL candidate ladder; Clause 2 had already ruled that
  population out of scope. The 43 rows are NOT derivation failures; **Deliverable 1 is
  untouched.** P2/P4 met their bands and are declared UNINFORMATIVE.
* **F83.2** the restart lever is dead in stat84 (§3). OPEN, blocking Item 2.

## §5 · SCORING — **I LOST HEAVILY AND IT IS RECORDED AS SUCH**
Prediction 1: P1 correct (machinery) · P2 correct/uninformative · **P3 SPLIT**, the
"concentrates at f-openings" clause FALSE, 43 rows spanning Z=12..90 · P4
correct/uninformative · **P5 correct and near-vacuous** · P6 correct in verdict, on
the boundary · P7 correct (+0.42226, band 0.20–0.60) · P8 correct.
Prediction 2: **Q1 FALSIFIED** (no W at any width) · **Q2 VOID** · **Q3 FALSIFIED**
(filed Z=57/89/90 at w=2; only Z=90) · **Q4 FALSIFIED** (filed 2–8, measured 1) ·
Q5 correct (machinery). **FOUR OF FIVE LOST.**
**Q3's ESCAPE CLAUSE IS WITHDRAWN WITH ITS REASON** — it declared the construction
void if Z=57/89 did not fail at w=2; that inference was itself wrong (window
semantics, §1), and CF2 shows the instrument catches Z=90's sealed tie-break exactly.
The withdrawal is entered rather than the clause quietly dropped.
Item 2: **C10 correct** — and see §3 for what the correct verdict concealed.

## §6 · UNCHANGED
Deliverable 1, the gates, the STATE CARD, the chain and every sealed row are
untouched. **NO PROPERTY OF F_core HAS BEEN DERIVED. CLAUSE 1 REMAINS THE LAST OPEN
DELIVERABLE.** T4 unblocked, last by practice. ALPHA THREAD CLOSED. Z=111 WITHHELD.
F54.1, F67.1–F67.6 UNVERIFIABLE, O-C1 open, Rung B not built, F82.2 open and bounded.
