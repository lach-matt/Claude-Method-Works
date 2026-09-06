# PROVENANCE TRACE — ordered by M at s74 ("provenance trace for certainty").
Supersedes the name-match cross-reference in AUDIT-GROUND-OCC-S74.md, which was WRONG. See F74.2.

## 1 · THE NAME MATCH WAS AN ARTEFACT
The s74 audit reported ZERO construct-side files named by Deliverable 1 or any gate. That
collector matched `gate\d+`, which catches gate7980.py and **NOT `gates_run55.sh`**. Measured
properly: **gates_run55.sh invokes 65 instruments, and 47 OF THEM ARE CONSTRUCT-SIDE.**
An instrument that narrows its own input reports on what it admitted (R 1671). Twice in one session.

## 2 · IMPORT CLOSURE OF THE DELIVERABLE-1 CHAIN
Transitive import closure of gate86.py / nlchain.py / nlcfg.py: 19-21 modules each, of which
three are construct-side — hfc2.py, t5_scf.py, t7c_hfsr.py. **ALL FOUR OF THEIR ground_occ
SITES SIT INSIDE `if __name__ == "__main__"` GUARDS** and are unreachable on import.
**THAT READING WAS TRUE AND STILL MISSED THE POINT (F74.2): the chain reaches the table by a
different name entirely.**

## 3 · THE POISON TEST — DIRECT EXPERIMENTAL VERIFICATION (F54.2's standing requirement)
Both levers poisoned, can-fail verified in both directions before any row was read.
**RESULT: the chain DIED AT Z=3 on `ground.expand`. The derivation DOES consume the observed table.**

## 4 · WHERE, AND WHAT KIND OF USE — nlchain.py step()
    the field       NG.run_guarded(Z, cfg_prev, 'ref') and add(cfg_prev, c)   <- CHAIN, no table
    the choice      win = min(ok, key=D)                                       <- ENERGIES, no table
    the table       G.expand(Z), lines 86-89, AFTER win is already fixed       <- SCORE only
                    -> rec, rec_ent, and ok = (rectag == win)
**THE OBSERVED TABLE ENTERS EXACTLY ONCE, AFTER THE DERIVATION HAS COMMITTED, TO GRADE IT.
THAT IS SCORING, NOT CONSTRUCTION. THE DERIVATION IS NOT CIRCULAR.**
The poison run shows it directly: at Z=3 both channels were SOLVED (2s -0.19629, 2p -0.12862,
rung 0) and only THEN did the poison bite.

## 5 · THE BLIND WALK — THE CERTAINTY M ASKED FOR
Poisoned with KeyError, which step() already handles, so the walk runs blind and records
prov=SYNTHESISED-UNMEASURED. Its choice is compared against the sealed row. Zeno segments:
    Z=3..8    agree 6  disagree 0
    Z=9..14   agree 6  disagree 0
    Z=19..22  agree 4  disagree 0     <- spans the 4s/3d boundary
    TOTAL     agree 16 disagree 0, prov never OBSERVED
**WITH THE OBSERVED TABLE UNREACHABLE, THE FIELD SELECTS THE SAME ENTRANT AT ALL SIXTEEN ROWS
TESTED, INCLUDING ACROSS THE 4s/3d CROSSOVER.** rt/nlchain.jsonl md5 identical before and
after (4f2b22d4...69ad): the test wrote nothing.

## 6 · LIMITS, STATED
16 of 107 rows tested, chosen for cheapness and for the one boundary they span. NOT the whole
walk. The f-block and the tie-break rows are UNTESTED by the blind walk. The claim earned is:
**the derivation's SELECTION is table-independent where measured, and the table's only role in
step() is to grade.** Extending to all 107 is bounded, mechanical, and not yet done.