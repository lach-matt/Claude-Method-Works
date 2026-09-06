# SESSION 77 — COMBINED HANDOFF
# Open Session 78 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-77 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · FIRST ACTION IN SESSION 78
`bash pack58/open58.sh`. **IT WILL PASS — s77 IS SEALED.** Then pack77/ORDER-FOR-S78.md.
**M'S STANDING INSTRUCTION: ITEMS 2 AND 3 OPEN s78, AND THE LOWER-BOUND QUESTION IS TO BE
RETURNED TO AND FINISHED. IT IS NOT PARKED.**

## §1 · WHAT s77 SETTLED
**ITEM 1 CLOSED — THE Z=89 ROW HAS NO SILENT HOLE.** All five never-converging channels
are CLASS B: the target node count IS attained in the field; the shooting fails to find
it. Windows: 7d [-0.0538,-0.0327], 6f [-0.0371,-0.0199], 8d [-0.0289,-0.0225],
7f [-0.0289,-0.0137], 8f [-0.0176,-0.0155] Ha. **The most bound edge of the most bound
missing channel is 71.45 mHa above the RUNNER-UP and 103.78 mHa above the winner — 2.2x
and 3.2x the 32.330 mHa margin. Neither rank 1 nor rank 2 is reachable by any of them.**
  * 7d and 8d were ALREADY in pack66/nodespec.jsonl from s66 and had not been read.
    s66 scoped itself `l != 2`, so no f channel had been scanned at any Z.
  * **STRUCTURAL POINT, pack77/POSITION-S77-WHERE-THE-LOWER-BOUND-LIVES.md: "6f" is a
    NODE-COUNT CONSTRAINT IMPOSED BY THE SHOOTING, NOT BY THE FUNCTIONAL.** Free
    minimisation with an added f electron at Z=89 gives 5f — cfg_prev carries 4f14 and
    orthogonality forces one node. Two nodes needs orthogonality to an UNOCCUPIED state.
**Z=89 RE-SEEDED (F76.2's obligation, PARTLY discharged).** ENT_MATCH TRUE at every seed
that produced a field. Common-set differential 0.052 mHa; **2D = 0.104 mHa vs m = 32.330
mHa, criterion HOLDS by a factor of 311** at the tightest of all 107 rows.
**RUNG A CAVEAT SETTLED FROM SOURCE — RUNG A STANDS.** nlchain.step calls
NG.run_guarded(Z, cfg_prev + c) per candidate and nlguard calls HFC(...).run2: **every
candidate is a fresh full SCF at its own Z-electron occupancy. Nothing is frozen.**
D = E(cfg+c) - E(cfg) is a difference of two converged TOTALS; Eref is one common constant
per Z, so argmin over D IS argmin over E. **s76 §3's D(Z) is NOT narrower than stated.**

## §2 · FAULTS
**F77.1 UNSEALED HANDOFF — CLOSED BY RULING S77.1 (M RULES B).** s76 was tarred without
`condense.py 76 --seal`. Integrity established instead by subset verification: the 1215
paths sealed at s75 recompute to root ff11fa8d...bd62e, MATCH, s76 adding 13 / changing 0
/ removing 0. **NO s76 LINEAGE ROW WAS WRITTEN. `condense.py 76 --check` FAILS FOREVER AND
THAT IS INTENDED** — it is the fault made visible from the tooling. s76's files are sealed
inside the s77 root. **STANDING: a session is not closed until the seal has run. Tarring
is not sealing.**
**F77.2 RAISED — CANDIDATE ADMISSIBILITY IS SEED-DEPENDENT. SEVERITY: STRUCTURAL.**
Seed A admits 9 channels at Z=89; seed B admits 5, rejecting 8s, 8p, 6g, 8g on node count
where A converged them. **The argmin is taken over a set the seed can change.** At Z=89
neither winner nor runner-up was touched. **No other row has been checked. s76 could not
see this because it scored ENT_MATCH and ORDER_MATCH, never ADMISSIBILITY.**
**F77.3 SEQUENCING ERROR, MINE, RECORD.** The item-1 can-fail (N1) was run AFTER the scan,
not before: `cells()` iterates the sealed `fail` map so 5f was never offered to it. It
PASSED — 5f and 5g return NO-RAISE through the widened l=3 path — but a can-fail that
follows its results is not a gate. **Check that a can-fail is REACHABLE by the driver.**

## §3 · THE SHARPENING OF F76.2
Seed B truncated the ballot 9 -> 5 and the raw margin moved 0.06 mHa. **Truncation alone
does not produce the artefact. s76's truncation removed the RUNNER-UP; this one removed
ranks 3 and 4 and left ranks 1 and 2 intact. A margin is a two-body quantity.** F76.2's
35.58 mHa was a RUNNER-UP-SUBSTITUTION artefact — narrower, and checkable.

## §4 · THE LOWER BOUND — M'S QUESTION, ANSWERED AND OWED
**IT IS NEITHER ITEM 2 NOR ITEM 3. Both are SAMPLING, and a sample never bounds its set.**
For the LINEAR radial Fock operator at a FIXED field, Courant-Fischer gives eps_1 < eps_2
< ... exactly and higher levels carry lower bounds free. **THE ENTIRE GAP IS THE
NONLINEARITY.** What must be bounded is how far self-consistent relaxation can move a
level — a spectral-gap statement, i.e. RUNG C, open here and open in the literature
(Hantsch Remark (b); BLLS PRL 72 (1994) 2981 does not transfer to RHF).
**THE NARROWING, AND IT IS THE SESSION'S BEST LEAD: we do not need a bound over all
critical points, only over relaxation between two NAMED sectors at one Z.** Rung B remains
a prerequisite IN PRACTICE (it produces the eps_k Rung C must control) and is not a route
IN PRINCIPLE. **M HAS INSTRUCTED THAT THIS QUESTION BE RETURNED TO AND FINISHED.**

## §5 · OWED, IN ORDER
1. **ITEM 2 — seed D.** Seed C is INAPPLICABLE at Z=89: all 15 items including the
   reference die at `RuntimeError: Z=89 50 nodes 3`, in the SEED CONSTRUCTOR, before any
   SCF. **The 52 Ha probe has never been applied at the tightest row; the falsifier that
   ran there was the 2 Ha one.** Seed D must be constructible at high Z, comparably
   displaced, and physically unlike A — candidates: screened hydrogenic at an effective
   charge far from Z, or seeding from a converged neighbour. **PHASE-A CAN-FAIL FIRST.**
2. **ITEM 3 — lever-test the eigenindex k, then build Rung B.** Note the lead from item 1:
   the three f channels return minlog -6.53/-6.01/-5.45 against the d channels' +0.09/
   +0.04. **The f failures are near-CLASS-C — within e^-6 of a findable state — which is
   exactly where an eigenindex selector would bite.** Not evidence about ordering.
3. **THE LOWER BOUND (§4). RETURN TO IT AND FINISH IT.**
4. F77.2's admissibility sweep across other rows — NOT started, larger question.
5. Re-seed the remaining tight rows: Z = 56, 39, 72, 90, 19.
6. Step 0(ii) selection rule: **STILL DRAFTED, NOT ADOPTED. AWAITING M's RULING.**

## §6 · INSTRUMENTS ADDED THIS SESSION (all in pack77, no sealed file edited)
`o89seg.py` — ZENO-SEGMENTED phase O, one guarded solve per invocation, resume from
receipts. **Detached jobs do not survive a tool-call boundary in this container; segment
instead.** Validated by its own output: seed A reproduces the sealed row exactly.
`o89score.py` — assembles a segmented run; scores raw AND common-candidate-set margins.
`seedtest77.py` — 3-line delta from pack61 (output paths only).
`nodespec77.py` — 4-line delta from pack66 (cache path, gate repointed, `l not in (2,3)`).

## §7 · UNCHANGED
All seven criteria read MET. T4 unblocked, last by practice. Route order 0 -> B -> A -> C.
F67.1-F67.6 remain UNVERIFIABLE. THE ALPHA THREAD REMAINS CLOSED. Z=111 WITHHELD.
Deliverable 1, the gates and the STATE CARD are untouched by this session.