# SESSION 74 — COMBINED HANDOFF
# Open Session 75 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-74 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · FIRST ACTION IN SESSION 75
**THE FIRST ACTION IS THE OPEN, NOT THE WORK.** `bash pack58/open58.sh`.
A ruling taken before the STATE CARD is read has no standing (§H.0). Only after
seal / runtime / canary report CLEAN does work begin.
**THE SECOND ACTION IS §5. THERE IS ONE ITEM IN IT. IT IS CLAUSE 1.**

## §1 · M'S CLOSING RULING AT s74 — THE ONE THAT SETS THE NEXT SESSION
**"EVERYTHING ELSE IS CLOSED BEFORE FORMALIZATION OF THE SOLUTION."**
s74 closed R-D, R-E and R-F. **CLAUSE 1 IS THE ONLY OPEN DELIVERABLE.** Session 75 is a
clause-1 session. Nothing else is to be opened in it. After clause 1 closes, the next thing
is FORMALIZATION (T4, R 1701-1966), which is LAST.

## §2 · M'S RULINGS, TAKEN AND FILED (pack74/RULINGS-S74.md)
**R-D** ground_occ audit: RUN. Executed. Then, on the result: **PROVENANCE TRACE ORDERED FOR
CERTAINTY** — the name match was not accepted as sufficient. **M WAS RIGHT AND THE TRACE
CAUGHT A REAL FAULT (F74.2).**
**R-E** CI-8: run ONLY if the Challenge criteria require it. **ASSESSED: NOT REQUIRED. NOT RUN.**
**R-F** Scope: SCOPE LAST. Deferred to the previous chat's standing position (s52 §3).
**R 1968** STANDING LAW, agreed: *a can-fail battery whose cases are written from the
instrument's own patterns is not a can-fail battery. Ground truth must come from OUTSIDE it.*

## §3 · THE RESULT WORTH THE SESSION
**THE DERIVATION IS NOT CIRCULAR, AND THIS IS NOW MEASURED RATHER THAN ARGUED.**
nlchain.py's step() builds the field from `cfg_prev` — the chain's own prior configuration —
and picks the entrant by `win = min(ok, key=D)`, purely from computed energies. The observed
NIST table (`ground.py`, "READ, not computed") enters at lines 86-89, **AFTER `win` is already
fixed**, solely to compute `rec_ent` and `ok = (rectag == win)`. **IT GRADES; IT DOES NOT BUILD.**
**THE BLIND WALK IS THE EVIDENCE.** With `ground.expand` poisoned so the table is unreachable,
the chain still solves and still chooses:
    Z=3..8 agree 6/6 · Z=9..14 agree 6/6 · Z=19..22 agree 4/4 (spans 4s/3d) · prov never OBSERVED
**16/16, INCLUDING ACROSS THE 4s/3d CROSSOVER.** rt/nlchain.jsonl md5 identical before and
after (4f2b22d4...69ad) — the test wrote nothing.
**LIMIT, STATED: 16 of 107 rows. The f-block and the tie-break rows are UNTESTED by the blind
walk.** Extending to all 107 is bounded and mechanical. It is NOT a clause-1 prerequisite.

## §4 · FAULTS RAISED AT s74
**F74.1 SEVERITY: INSTRUMENT. TOUCHES NO SCORED ROW.** The first audit classifier was wrong in
the dangerous direction — it called ci2b.py L38 SCORE where F73.3 had established CONSTRUCT —
and its can-fail selftest passed because I wrote the cases from my own regexes. **R 1671's
fault repeated.** Repaired by a decidable rule, deliberately biased to OVER-report CONSTRUCT,
with the battery drawn from outside the instrument. Dead versions retained, not deleted.
**F74.2 SEVERITY: SCOPE. TOUCHES NO SCORED ROW.** R-D was posed as an audit of `ground_occ`.
**THE CHAIN DOES NOT CALL `ground_occ`. IT CALLS `ground.expand`, WHICH ground_occ WRAPS.**
So "nlchain.py: ZERO SITES" was true of the NAME and false of the THING. **THIS IS F54.2
EXACTLY — the name audited was not the lever used — twenty sessions later.** Caught by the
poison test, not by reading; source-tracing had said clean twice.
**PROPOSED STANDING RULE, for M at s75 (one line, then move to clause 1):**
*AN AUDIT BY NAME IS NOT AN AUDIT. THE LEVER MUST BE POISONED AND THE CONSUMER MUST DIE.*

## §5 · THE ONLY OPEN ITEM — CLAUSE 1
**THE REVERSE CHAIN FROM THE EXACT MANY-ELECTRON SCHRODINGER EQUATION TO THE FIELD ACTUALLY
SOLVED.** This is Challenge criterion 3 ("start from first principles") joined to criterion 1
("bridge Dirac's gap"). It is DERIVATION work: no network, no new kernel, no walk.
**WHAT MUST BE EXHIBITED, AND EACH STEP NAMED AS DERIVED / APPROXIMATED / CHOSEN:**
  1. H_exact = sum_i(-1/2 nabla_i^2 - Z/r_i) + sum_{i<j} 1/r_ij       — the stated starting point
  2. -> the mean-field (Hartree-Fock) reduction: what is DROPPED is correlation, and it must be
     named as dropped, with the s73 Cu reading (differential d-d correlation) cited as the
     known place it bites
  3. -> the CENTRAL-FIELD / spherical-average step: this is where l becomes a good quantum
     number AT ALL, hence where n+l becomes SAYABLE. **CI-2 (s73) already scored the spectator
     spherical average as machine-zero, worst 1.7e-15 mHa — that is a clause-1 asset, use it.**
  4. -> the scalar-relativistic term: clause 3 established this is NOT optional (Z=90 Th
     reverses by 253 mHa). It must appear in the chain as REQUIRED, not as a refinement.
  5. -> the radial equation the C kernel actually integrates (libshoot_sr.so)
**THE HONEST DIFFICULTY, STATED SO s75 DOES NOT REDISCOVER IT AS A SURPRISE:** step 2 is a
genuine approximation, not an identity. Clause 1 cannot claim the field IS the Schrodinger
equation. **What it can claim is a chain in which every departure is named, bounded where a
bound exists, and shown not to touch an ordering the walk gets right.** Under the standing law
(a mechanism earns a place only if it changes an ordering the walk gets wrong), correlation
has NOT earned one. That is the argument's spine.

## §6 · CARRIED FORWARD, UNCHANGED
**pack67 and pack68 still do not exist**; F67.1-F67.6 remain UNVERIFIABLE and must not be
scored either way. F71.1, F72.1/F72.2, F73.1-F73.4 stand as recorded.
**PREDICTION-CI2x2 IS FULLY SCORED** (CI-1,3,4,5 s71; CI-2,6,7 s73). CI-8 assessed at s74 as
NOT REQUIRED by any criterion and NOT RUN — reopens only on M's ruling.
**THE ALPHA THREAD REMAINS CLOSED** (s70 §5). **Z=111 REMAINS WITHHELD** by RG-1's own
blocking clause; no bulk or conductivity claim was made or may be made.
Deliverable 1 unchanged. Gates unchanged. STATE CARD unchanged: 107 rows, Z=2..108.
**T4 (R 1701-1966) IS LAST**, and only after clause 1 closes.
