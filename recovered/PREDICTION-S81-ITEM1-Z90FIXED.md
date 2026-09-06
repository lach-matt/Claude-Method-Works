# PREDICTION — SESSION 81, ITEM 1. THE FIXED-FIELD CROSS-CHANNEL COMPARISON AT Z=90.
# FILED BEFORE ANY RUN OF fixed81.py, INCLUDING THE REFERENCE BUILD. R 1449.
# Instrument: pack81/fixed81.py. Object: eps_2^{l=3}(F_core[Phi_d*]) vs eps_4^{l=2}(F_core[Phi_d*]).

## WHAT IS KNOWN BEFORE THE RUN, AND WHERE IT COMES FROM
Sealed chain row Z=90: entrant 6d, D_ent = -0.19094 Ha, rank 2 = **5f** at -0.13689 Ha,
m(90) = **54.05 mHa**. Sealed row Z=91: the entrant FLIPS to 5f. **Z=90 is the last row
6d wins, and its rank 2 is the f channel itself** — so unlike Z=89, where rank 2 was 7p
and the f channels were CLASS B holes, this fixed-field comparison is the row's own
decision.
At Z=89 the same instrument returned a fixed-field gap of **+155.369 mHa** on the pair
(6f, 6d), against a dE-currency separation of 137.134 mHa, with a relaxation term of
**10.072 mHa acting to CLOSE the gap**.
The node counts: **5f has ONE node (2nd in l=3); 6d has THREE (4th in l=2).**

## THE CLAUSES

**V1 · THE ORDERING HOLDS AT FIXED FIELD.** eps(5f) > eps(6d) at Z=90, gap POSITIVE and
above the FLOOR of 0.035 mHa.
*Rationale: the sealed row puts 5f 54.05 mHa above 6d in dE, and at Z=89 the fixed-field
gap exceeded the dE gap. I expect the same sign here. If V1 fails, clause 1's fixed-field
special case is FALSE at Z=90 and the derivation has a counterexample at the row adjacent
to the flip. This is the clause with real content.*

**V2 · THE GAP IS SMALLER THAN Z=89's 155.4 mHa, AND LIES BETWEEN 40 AND 110 mHa.**
*Rationale: the dE separation is 54.05 mHa here against 137.13 mHa at Z=89, and at Z=89
the fixed-field gap sat 18.2 mHa above the dE separation. Scaling that offset gives ~72
mHa. I bracket it wide because the offset is one measurement at one Z and the pair is a
different pair. **A gap below 10.1 mHa would mean the Z=89 relaxation term is large enough
to erase it, and the fixed-field argument would carry nothing at Z=90.** That is the
outcome I am filing against.*

**V3 · THE RELAXATION TERM AT Z=90 IS SMALLER THAN THE GAP AND ACTS TO CLOSE IT.**
Not computed by this instrument; recorded as a clause for the follow-on run if reached.
*Rationale: at Z=89 it was 10.072 mHa and closed the gap, because denying the f channel
its own core relaxation costs it exactly that. The mechanism is not Z-specific.*

**V4 · THE l=3 PROBE DOES NOT NEED THE FINE SCAN. fine_used = 0 FOR 5f.**
*Rationale: 5f is a CONVERGED sealed channel at Z=90 (dE = -0.13689), unlike 6f/7f/8f at
Z=89 which were CLASS B and needed the scan every time. The standard bracket should find
a 1-node l=3 state without help. **This is the clause I most expect to lose**, because the
frozen field is not the field 5f converged in, and s79's W4 says the standard bracket
misidentified the state in the frozen field even for a healthy channel.*

**V5 · THE TWO SELECTION BRANCHES AGREE, BECAUSE THE ZERO SET HAS ONE MEMBER.**
n_zeros = 1 on every firing at Z=90, so most-bound and least-bound return the SAME eps to
all digits, and the spread is 0.0.
*Rationale: F80.1's two-member zero set appeared at 6f/7f/8f at Z=89 — high-lying, weakly
bound channels scanned over a wide window. 5f at Z=90 is bound at -0.137 Ha and well
separated from 4f below it. If V5 fails, the branch that supports no self-consistent
probe is to be reported and the surviving branch carries the result — F80.1's rule.*

**V6 · THE E9 RESTART LADDER DROPS THE Z=90 ENERGY BY BETWEEN 0.01 AND 0.10 mHa,
MONOTONE, AND TERMINATES IN UNDER 12 PASSES.**
*Rationale: F80.2 measured 0.034493 mHa at Z=89, monotone and geometric with ratio ~0.3,
and diagnosed it as a property of the STOPPING TEST, not of any Z. If the drop at Z=90
falls far outside that band, F80.2's "it applies equally to every row" is wrong and the
fault is larger than it was stated to be.*

**V7 · THE MACHINERY CAN-FAIL RETURNS THE SCF's OWN eps(6d) TO BETTER THAN 1 mHa.**
*Rationale: E6+E7 build the field run2 builds for shell a with _ceff(a,Q) = Q[a]-1 = 1,
which is exactly the reduced core occupancy. At Z=89 the analogous check agreed to 1e-6
Ha. **At Z=90 it is a harder test, because the probe's own shell is now PRESENT in the
core and the same-shell exchange correction is exercised for the first time.** If this
misses by more than 1 mHa, E7 is wrong and no gap from this instrument may be quoted.*

**V8 · THE CONTROL RETURNS ORDERING FAILS, WITH 4f MORE BOUND THAN 6d BY MORE THAN 5 Ha.**
*Rationale: 4f is inside the [Rn] core. At Z=89 the control returned -12489 mHa. The
verdict space must not be one-sided.*

## WHAT WOULD MAKE THIS RESULT WORTHLESS, FILED IN ADVANCE
1. **This is ONE Z, ONE PAIR, ONE FIELD, ONE RUNG.** It is a MEASUREMENT of clause 1's
   fixed-field special case, NOT a derivation of it, and must never be quoted as one.
2. **The same-shell asymmetry of E7 is real**: the l=2 probe has a partner in its own
   shell and the l=3 probe does not. That is the scheme's convention, and if the gap is
   small the asymmetry is a candidate explanation for it, not a nuisance.
3. **Vc = 0 (E2) moves both channels**, and the 19.3 mHa offset s79 measured between
   eps(6d) and the sealed dE at Z=89 lives there. **No figure from this instrument is to
   be compared against a sealed dE without that offset being named.**
4. **Nothing here derives a property of F_core.** Clause 1 is untouched by a measurement.
