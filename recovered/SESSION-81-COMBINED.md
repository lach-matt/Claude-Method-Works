# SESSION 81 — COMBINED HANDOFF
# Open Session 82 with `bash pack58/open58.sh` using the LOWDIN-HANDOFF-81 tar.
# NO SEALED FILE WAS EDITED. c = 137.035999 remains the only number ever entered.
# THE DERIVATION IS 107 ROWS, Z=2..108. Any claim of 119 is a boundary violation.

## §0 · OPEN
`bash pack58/open58.sh` passed: s80 seal **1310/1310 root MATCH**, canary CLEAN, STATE
CARD CLEAN. M ruled at open: **items 1, 2, 3 all worked; item 4 (clause 1) not started.**
All three closed. **M issued SEVEN RULINGS at close — RULING-S81, binding.**

## §1 · ITEM 1 — THE FIXED-FIELD COMPARISON AT Z=90. THE RELAXATION TERM EXCEEDS THE GAP.
pack81/RESULT-S81-ITEM1-Z90-FIXED-FIELD.md. Prediction sha ce8baedb...0b1d811a filed first.
`fixed81.py`: fixed79 patched, NOT reused — E6 reduces the entrant's occupancy by one
instead of deleting the shell (deleting it would have run a 90-electron atom with 89),
E7 builds run2's own field for shell a, E8 carries F80.1, E9 carries F80.2.
**THREE CAN-FAILS PASSED FIRST**, one exactly: the frozen l=2 probe returned the SCF's own
**eps(6d) = -0.217248225 to nine digits, diff 0.0 mHa.**
| currency | value | ordering |
|---|---|---|
| TOTAL ENERGY (the row's own) | **+54.009 mHa** | 6d WINS |
| ONE FIELD (clause 1's object) | **+79.244 mHa** | HOLDS |
| TWO FIELDS (each relaxed) | **-10.657 mHa** | **REVERSED** |
Reproduces sealed m(90) = 54.05 mHa to 0.04 mHa. **THE ENTRANT AT Z=90 IS 6d, UNTOUCHED.**
**THE FINDING: the relaxation term is 89.901 mHa — LARGER than the 79.244 mHa gap it
would have to erase.** At Z=89 it was 10.072 on 155.369 (6.5%); at Z=90, 113%.
**s79's 10.1 mHa target is a Z=89 figure and does not travel.** s79 flagged it as "a
measurement at one Z, not a bound"; that flag was load-bearing and is now discharged.
Scored: V1 V2 V4 V5 V7 V8 correct, V6 split, **V3 FALSIFIED** — and V3 was the clause with
the content. Filed rationale "the mechanism is not Z-specific" is wrong.

## §2 · ITEM 2 — F80.3 CLOSED. AND J2 IS THE REPAIR F80.3 SHOULD HAVE SPECIFIED.
pack81/RESULT-S81-ITEM2-TOL-AND-7P.md. Prediction sha 933aad7a...6c42975d filed first.
**All eight converged s80 rows re-label to SAME BASIN at the measured 0.034493 mHa floor.
All three "O-C1 FALSIFIED" labels collapse. F80.3 IS CLOSED.** Deepest row clears by 2% of
the floor — filed in advance as nearly a coin-toss.
**SECOND CONFIGURATION, cfg88+7p (rank 2):** six perturbations, two kinds, both can-fails
passed. **O-C1 NOT FALSIFIED THERE EITHER. NOT ESTABLISHED.**
**J2 — RESTART BOTH SIDES, NOT ONE — SHRINKS THE SCATTER 17x:** landing range 0.023487 mHa
-> stationary range **0.001414 mHa**, and every run lands ABOVE the reference, none below.
**The null's floor falls from ~0.035 to ~0.0015 mHa — 0.005% of m(89).** **R81.2 MAKES
THIS STANDING LAW.** Scored: W1 W3 W6 correct, W4 split, W2 mostly falsified, W5 unresolved.
A free determinism receipt: the grid ran twice by operator error and returned identical dE
to all six decimals, landing and stationary alike. Kept as a gate nobody designed.

## §3 · ITEM 3 — 7d AND 8d REFUSE ON BOTH BRANCHES. **U1 FALSIFIED.**
pack81/RESULT-S81-ITEM3-BRACKETS.md. Prediction sha 63eb8489...1b91d7bc filed first.
`de81.py` IMPORTS de80 unmodified; nothing written into pack80. K4 (6d, fallback inert ->
sealed energy exactly) gated every run and passed seven times.
| ch | window (Ha) | target nodes | outcome |
|---|---|---|---|
| 7d | [-1.99e-4, -0.635] | 4 | **NO TARGET-NODE ZERO**, both branches |
| 8d | [-1.06e-4, -0.340] | 5 | **NO TARGET-NODE ZERO**, both branches |
First pass used de80's f-channel bound and refused; **widened to the -2e-4 Ha the project
adopted at s79 (K5, timing flag declared) and both branches re-run.** Same refusal.
**NOT an instrument limitation** — the same machinery recovered 6f/7f/8f in one firing
each. **But M RULED (R81.6) THAT THEY STAY CLASS B until confirmed at the CONVERGED field
rather than at the fallback iteration. That confirmation is now OWED.**
Scored: U5 U6 correct, U2 vacuous, **U1 U3 U4 falsified.** s80's f-channel diagnosis was
generalised to the d block and did not travel.

## §4 · FAULTS — FOUR, ALL AGAINST THIS SESSION'S OWN WORK, THREE CAUGHT BY GATES
**F81.1 RESTART LADDER IS NOT A DESCENT.** At 7p it RISES 0.022195 mHa. F80.2's number and
mechanism survive; its words do not — "basin floor" is the wrong name and the direction
was assumed from one configuration. Four measurements: three down, one up, 2.7x spread.
**R81.7: NOT DISCHARGED. Its repair is PROPAGATION.**
**F81.2 TOL A THOUSAND TIMES TOO SMALL — THE UNITS.** Would have reinstated F80.3 inside
its own repair. Caught by a can-fail that passed BY LUCK, which is not a pass. REPAIRED.
**F81.3 THE LEVER READ OFF THE WRONG OBJECT.** J3 halted the grid at rc=4, `LEVER DEAD`.
The lever was live; the instrument's ability to SEE it was not. REPAIRED.
**F81.4 A str_replace PATCH DELETED A FUNCTION HEADER**; `widen()` swallowed `canfail()`.
Benign in effect — the gate ran MORE often — **and that is not a defence.** REPAIRED.
**THE SPECIES, SEVENTH APPEARANCE IN FOUR SESSIONS.**

## §5 · M's SEVEN RULINGS — RULING-S81-SEVEN-RULINGS.md, BINDING
R81.1 **F80.2: RE-RUN the chain to stationarity** (second chain, no sealed row edited,
scored on ORDERING not energy) · R81.2 **J2 IS STANDING LAW** · R81.3 TOL both ways,
comparison decides, M expects per-configuration · R81.4 clause 1: **(c) preferred, (a) and
(b) run as the comparison** · R81.5 priority follows from R81.4; Z=91 only if needed ·
R81.6 **7d/8d CLASS B, confirmation NECESSARY** · R81.7 repair the faults; F81.1 by
propagation. **M RULED THE Z=90 FIGURES OUT OF DELIVERABLE 1 — structure only.**

## §6 · UNCHANGED
Deliverable 1, the gates, the STATE CARD, the chain and every sealed row are untouched.
**NO PROPERTY OF F_core HAS BEEN DERIVED. CLAUSE 1 IS THE LAST OPEN DELIVERABLE AND s81
MADE ITS TARGET HARDER, NOT EASIER.** T4 unblocked, last by practice. THE ALPHA THREAD
REMAINS CLOSED. Z=111 WITHHELD. F67.1-F67.6 remain UNVERIFIABLE.