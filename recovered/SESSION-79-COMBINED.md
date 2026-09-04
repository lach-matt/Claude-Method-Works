# SESSION 79 — COMBINED HANDOFF
# Open Session 80 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-79 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · OPEN
`bash pack58/open58.sh` passed at s79 open: s78 seal **1275/1275 root MATCH**, canary
CLEAN (float, kernel, numpy, physics), STATE CARD CLEAN. M ruled both items at open:
scope = item 2 then item 1; Step 0(ii) = ADOPT with the obligation registered to Route C.

## §1 · STEP 0(ii) ADOPTED — pack79/RULING-S79-STEP0ii-ADOPTED.md
The field is DEFINED as a global minimiser of E^RHF at the candidate's fixed shell
occupancies over Hantsch's relaxed set; existence by his Theorem 2.1.
**(beta, maxit) LEAVES THE DEFINITION.** The convergence ladder is now a numerical scheme
for approaching an independently defined object, and F47.3's ~1e-5 limit is a statement
about the SCHEME, not the field. The rule is stated on the ENERGY, never the spectrum;
Lions' simplicity assertion is NOT imported and must not enter later by stealth.
**OBLIGATION O-C1, OWNER ROUTE C, LOAD-BEARING: the program must be shown to reach the
GLOBAL minimiser.** Four seeds agreeing to 0.005 mHa from 52 Ha away, and seed D holding
at Z=89 from 517 Ha away, is a FOUR-START BASIN TEST AND IS NEVER TO BE QUOTED AS A PROOF.
The falsifier is cheap and still not run: perturb a CONVERGED solution and re-converge.

## §2 · ITEM 2 — CLOSED. THREE OF THE FIVE Z=89 HOLES ARE NOW FOUND STATES.
pack79/RESULT-S79-ITEM2-Z89-FOUND-STATES.md. Prediction sha a2a5e4c8...162671 filed first.
Instrument `refine79.py`, four declared lines from sealed pack77/nodespec77.py, NFINE=3000
against s77's 160. **CAN-FAIL RAN FIRST AND GATED**: the control (tgt := the node count the
sealed solver returned) returned CLASS C and bisected e = -0.020286239, log(nrm) = 0.0,
**reproducing the sealed runtime's own e_returned = -0.020286, res = 0.0.** Direction B
demonstrated by 7d and 8d on the identical code path.
| ch | s77 | **s79** | win pts | zero |
|---|---|---|---|---|
| 6f | B | **C** | 3 -> 353 | **-0.031600440** |
| 7f | B | **C** | 4 -> 460 | **-0.020275522** |
| 8f | B | **C** | 2 -> 463 | **-0.014084998** |
| 7d | B | B | 5 -> 646 | none |
| 8d | B | B | 3 -> 551 | none |
**F78.2 IS REFUTED AT Z=89**, on sealed data before anything new ran: all five failures are
RuntimeError node-count raises, **ZERO TypeErrors**, and res_returned = 0.0/1e-9 throughout.
**The bracket expansion did not fail — it succeeded, converged to a TRUE zero, and the zero
belonged to a different state. The mechanism is STATE MISIDENTIFICATION.** F78.2 stands as
raised at Z=19 under perturbation and is closed at Z=89.
Prediction: Q1 Q2 Q3 Q5 correct, **Q3 correct on BOTH halves and on the filed rationale**;
Q4 split — verdict right, containment clause wrong (8f fell 1.416 mHa outside its bracket).
Undiagnosed and recorded: sign_changes = 2 on all three f channels (two zeros at one node
count; the instrument bisects the MORE BOUND, so the conclusion is the conservative one).

## §3 · ITEM 1 — THE FIXED-FIELD OBJECT IS COMPUTED. THE ORDERING HOLDS BY 155.4 mHa.
pack79/RESULT-S79-ITEM1-FIXED-FIELD.md. Prediction sha 34068ce5...15fb505 filed first.
Instrument `fixed79.py`, five declared lines from sealed rt/hfc2.py run2.
**CAN-FAIL RAN FIRST: the 4f control returned gap = -12489.147 mHa, ORDERING FAILS.**
**CROSS-CHECK: Phi_d* converged to E = -25694.541630577907, the sealed s77 6d row TO EVERY
DIGIT**, and the independently built frozen probe re-solved 6d at -0.176897146.
  **eps_4^{l=2}(F_core[Phi_d*]) = -0.176897 Ha  (6d, 3 nodes)**
  **eps_3^{l=3}(F_core[Phi_d*]) = -0.021528 Ha  (6f, 2 nodes)**
  **GAP, ONE FIELD = +155.369 mHa. CLOSE-S78 §3's RESIDUAL CLAIM HOLDS AT Z=89.**
**AND THE RELAXATION TERM — s78's one genuinely open, genuinely separate object — IS
MEASURED: 145.297 mHa across two fields vs 155.369 mHa in one, so RELAXATION = 10.072 mHa,
AND IT CLOSES THE GAP RATHER THAN OPENING IT. 15.4 times smaller than the gap it would
have to erase.** First number ever put on that object.
W1 W2 W4 W5 correct; **W2 correct on both clauses and on the filed rationale.** W3's check
passed to 1e-6 but named the wrong comparand — see F79.2.
**RECORDED: the instrument's FIRST run returned "no zero at target node count" and that was
an artefact of its own scan bound (-0.0265, when W2 had already placed the state above
-0.0316). F79.1's shape, in code written this session, caught ONLY because W2 was filed
first.** Also: 0.451 mHa beta-dependence — no precision better than ~0.5 mHa is claimed.
**THIS IS A MEASUREMENT OF THE CLAUSE-1 INEQUALITY AT ITS TIGHTEST INSTANCE. IT IS NOT A
DERIVATION OF IT AND MUST NEVER BE QUOTED AS ONE. NO PROPERTY OF F_core HAS BEEN DERIVED.**

## §4 · FAULTS
**F79.1 RAISED AND CLOSED — s77 QUOTED THE WRONG END OF ITS OWN RANGE, TWICE.** `minlog` is
the MINIMUM; where log(nrm) is negative throughout, that is the point FARTHEST from zero.
s77's "f channels within e^-6 of a findable zero" cited the far end; the refined window runs
-7 to +7.9 and CROSSES. **And the d channels are the inverse — minlog +0.04 IS their closest
approach, while s77 called them "not marginal". Both readings inverted.** The verdict
f-near-C survives; its evidence never supported it. Repaired: maxlog is now recorded (D2).
**F79.2 RAISED, NOT CLOSED — CURRENCY MISMATCH.** `-0.15762` is a TOTAL-ENERGY DIFFERENCE
(E(6d) - E(ref) = -0.157621, measured from pack77/o89_89_A.jsonl); every nodespec window
and every found zero is a ONE-ELECTRON EIGENVALUE. **At 6d the two differ by 19.277 mHa,
comparable to the 32.330 mHa margin itself.** s77's "103.8 mHa above 6d" and **this
session's own item-2 margin table** compare unlike quantities. **REGISTERED AGAINST MY OWN
RESULT IN THE SAME SESSION.** Item 1 is UNAFFECTED — it compares eps against eps in one
field. The qualitative Z=89 verdict survives provisionally; **every stated MULTIPLE OF THE
MARGIN is withdrawn as stated.**
**THE SPECIES.** F78.1 read the raise, not the sentence. F79.1 read the instrument, not the
label on its column. F79.2 READ THE UNITS. Three faults, two sessions, one species: a
number carried forward under a name that did not describe it.

## §5 · OWED, IN ORDER
1. **F79.2's REPAIR — CONVERT THE THREE FOUND f STATES INTO dE.** Run the Z=89 SCF at
   cfg+6f, cfg+7f, cfg+8f with refine79's node-targeted scan as the solver's fallback;
   take E - (-25694.384010). **REACHABLE ONLY SINCE ITEM 2.** Until run, the Z=89 hole is
   three eigenvalues and two brackets, NOT three entries in the table that decides the row.
2. **CLAUSE 1 — derive a cross-channel property of F_core forcing eps_3^{l=3} >
   eps_4^{l=2}.** Structure UNCHANGED by s79. **What is new is a TARGET: any property
   proving the fixed-field inequality with more than 10.1 mHa to spare carries the full
   claim at this Z.** There was no number to aim at before.
3. **O-C1's falsifier** — perturb a converged solution and re-converge. Cheap, never run,
   and it is now load-bearing because Step 0(ii) is adopted.
4. **The fixed-field comparison at the other tight rows** — 56, 39, 72, 90, 19. One Z is
   one Z.
5. Rung B — permission earned at s78 §2, still NOT built.
6. F77.2's admissibility sweep across other rows. Four seeds, four firings, never once a
   top-two rank. Still not a proof.
7. Re-seed the remaining tight rows with seed D.
8. sign_changes = 2 at the f channels — undiagnosed.

## §6 · INSTRUMENTS ADDED (all in pack79, no sealed file edited)
`refine79.py` refined node spectrum, D1-D4, maxlog recorded, tgt as argument = the can-fail.
`fixed79.py` frozen-core probe, E1-E5, 4f control = the can-fail. E5 is the scan-bound
amendment forced by §3's recorded artefact.
`refine79.jsonl`, `fixed79_run.json`, `fixed79_control.json` — receipts.

## §7 · UNCHANGED
All seven criteria read MET. T4 unblocked, last by practice. Route order 0 -> B -> A -> C.
F67.1-F67.6 remain UNVERIFIABLE. THE ALPHA THREAD REMAINS CLOSED. Z=111 WITHHELD.
Deliverable 1, the gates and the STATE CARD are untouched by this session.