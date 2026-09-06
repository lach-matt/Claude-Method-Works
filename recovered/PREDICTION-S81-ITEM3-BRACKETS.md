# PREDICTION — SESSION 81, ITEM 3. THE TWO REMAINING Z=89 BRACKETS, 7d AND 8d.
# FILED BEFORE ANY RUN OF de81.py. R 1449.
# Instrument: pack81/de81.py, importing pack80/de80.py unmodified. Currency: dE.

## WHAT IS KNOWN BEFORE THE RUN
Sealed Z=89 ranks, in dE: 6d **−157.620 mHa** (rank 1) · 7p **−125.288** (rank 2) ·
8s −70.65 · 8p −49.17 · 5f −31.46 · 5g −20.00. m(89) = **32.332 mHa**.
s80 closed three of the five CLASS B channels with de80's fallback: 6f **−20.486**,
7f **−14.282**, 8f **−10.528** mHa, all converged at rung 0 with **one** fallback firing
and zero edge flags, on the LEAST-BOUND branch; the most-bound branch supported no
self-consistent field at any of the three.
7d and 8d were untouched by s80. refine79 found no target-node zero for them.

## THE CLAUSES

**U1 · BOTH 7d AND 8d CONVERGE ON THE LEAST-BOUND BRANCH.** de80's fallback reaches a
target-node zero for each and the SCF closes at rung 0.
*Rationale: refine79's failure was under F80.1's undeclared orientation and a bound of
its own choosing; de80's window is adaptive ([0.20, 8.0] × |e|) and its scan returns the
whole zero set. The three f channels all closed once the orientation was declared.
**If they do NOT converge, the Z=89 row keeps two holes and the honest statement is that
five channels were CLASS B and three were recovered, not five.***

**U2 · THE ENTRANT IS UNCHANGED AND RANKS 1 AND 2 ARE UNTOUCHED.** Both channels lie
ABOVE 7p, and by more than 2 × m(89) = 64.7 mHa.
*Rationale: every recovered channel so far has landed far above rank 2 — 6f at 3.241 m,
7f at 3.433 m, 8f at 3.549 m. d channels above 6d should behave the same way. **This is
the clause the row depends on; if it fails, Z=89's entrant is in question and that is a
result, not a nuisance.***

**U3 · 7d IS MORE BOUND THAN 8d, AND BOTH LIE BETWEEN 8s (−70.65) AND 5f (−31.46) mHa.**
*Rationale: within one l block min-max orders by node count, so 7d (4 nodes) must lie
above 6d (3 nodes) and 8d (5 nodes) above 7d. The magnitude bracket is an extrapolation
from the f channels' spacing and is the weakest clause here.*

**U4 · AT LEAST ONE FIRING RETURNS n_zeros ≥ 2, AND THE MOST-BOUND BRANCH FAILS TO CLOSE
ON AT LEAST ONE CHANNEL.** F80.1's structure repeats in the d block.
*Rationale: the two-member zero set appeared at all three f channels. **But the Z=90 5f
probe in item 1 never fired the fallback at all, so a two-member set is not universal.
I expect it here because 7d/8d are high-lying and weakly bound, which is the regime where
it appeared.***

**U5 · THE FALLBACK FIRES ONCE PER CHANNEL, NOT EVERY ITERATION.**
*Rationale: s80's X5 was falsified badly in exactly this way — n_fb = 1 on all three f
channels, because state misidentification is a START-UP ARTEFACT and the field stays on
the correct state unaided. **This clause is the corrected version of a prediction I lost
last session, and I am filing the correction rather than repeating the error.***

**U6 · THE K4 CAN-FAIL RETURNS THE SEALED 6d ENERGY EXACTLY, WITH ZERO FALLBACK FIRINGS.**
*Rationale: de80's C1 established this in s80. Here it is re-run through a different
driver, so it also gates that the driver's import path has not disturbed the sealed code.*

## FILED IN ADVANCE, AGAINST THIS RESULT
1. **THIS IS A RANKING RESULT, NOT A DERIVATION.** It closes holes in a table. **It
   derives no property of F_core and must never be quoted as doing so.**
2. **A CONVERGED CHANNEL IS NOT A PROOF THAT THE FIELD HAS NO OTHER SOLUTION** for that
   channel. That is O-C1's territory and O-C1 is open.
3. **ONE SEED, SEED A's CHAIN, ONE RUNG.** Nothing here re-seeds.
4. If a zero is found within EDGEFRAC of a scan edge it is a **FLAG, NOT A RESULT**, and
   must be reported as such (de80's G2).
