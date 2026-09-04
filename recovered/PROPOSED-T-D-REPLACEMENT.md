# PROPOSED — T-D. THE REPLACEMENT FOR THE RULED NODE-COUNT NULL. FOR M'S RULING.
# SESSION 66. Follows F66.1. NOTHING IS FILED AND NOTHING IS RUN.
# Standing 7b: a TEST must be proven able to fail before it is filed. §3 below is
# how that proof is to be produced, and it is to be produced BEFORE the prediction.

## WHAT THE ARCHIVE LEAVES OPEN AFTER F66.1
s42 answered ONE atom and ONE channel: Z=21, 4d. Its answer was that the labelled
state exists in the initial field, is destroyed by the SCF update, and is absent from
the self-consistent field — the raise being the field answering correctly through the
wrong exception. **Whether that is what happens at the other ten instances is not
measured anywhere.** The s65 observation that the shortfall is exactly ONE node in
eleven instances spanning a hundred protons — and TWO at 7d@81 — is unexplained, and
a shortfall that is constant across a hundred protons is not a coincidence of a
solver.

## §1 · THE INSTRUMENT ALREADY EXISTS AND DISCRIMINATES
`rt/t7f_rep.py::NodeGated` raises two DIFFERENT exceptions, and the difference is
exactly the two readings of the s65 bridge:

    CLASS A   "no nd==tgt window exists"               the field carries no such
                                                       state at any e<0. Reading (1).
    CLASS B   "window exists, log(nrm) has no zero"    the state exists and the SCF
                                                       update destroys it. The s42
                                                       mechanism.

It was NOT adopted into the chain at s43 (its bracket was rejected; only HFCN's
exception-naming was adopted). It is used here EXACTLY as s42 used it: as a
read-only diagnostic, beside `nlchain`, editing nothing. D1-inertness on healthy
channels was measured at s42 to bit-identity and is re-measured here as gate [0].

## §2 · T-D, THE TEST
For each of the eleven node-count failures, run the failing channel through NodeGated
at the same Z and the same configuration the sealed chain used, and record the class.

    Z=21 4d   Z=31 4d   Z=39 5d   Z=49 5d   Z=49 6d   Z=57 6d
    Z=81 6d   Z=81 7d(short two)  Z=89 7d   Z=113 …   (exact list to be read off the
    sealed `fail` dictionaries, not from memory, before the prediction is written)

**WHAT EACH OUTCOME MEANS, FIXED IN ADVANCE:**

  * **ALL CLASS B.** The null is uniformly the SCF self-destruction of a diffuse
    weakly-bound channel. Reading (1) dies everywhere and not merely at Z=21. The
    Madelung labelling is NOT being contradicted by the field; the instrument cannot
    resolve an excited channel whose own exchange source defeats it. **This closes
    the item negatively and it does NOT reach the Challenge.** It is still worth
    knowing, because it retires a standing "two readings" and unblocks nothing.

  * **ANY CLASS A.** At that atom the self-consistent field carries no state with the
    node count the label (n,ℓ) demands. **That is the Challenge-level statement**, and
    it is M's standing point in its exact form: the null is a gap, and the gap is that
    the Madelung rule is stated in a labelling — hydrogenic node counts — that the
    many-electron field does not carry at precisely the atoms where its d tie-break is
    tested. It would then be a measurement, not a reading.

  * **MIXED.** The class is a function of Z or of ℓ, and which is the next question.
    Report the split before interpreting it.

  * **7d@81 IS THE SHARPEST SINGLE CELL** and is predicted separately, because a
    shortfall of TWO cannot be one destroyed root.

## §3 · CAN-FAIL, TO BE DEMONSTRATED BEFORE THE PREDICTION IS FILED (Standing 7b)
The test is only admissible if BOTH classes are reachable. To be shown, in this order,
before any prediction file exists:

    [0]  INERTNESS. NodeGated on a healthy channel (Z=21 3d) reproduces the sealed
         D to the s42 tolerance and does not raise. If it raises, the instrument is
         wrong and T-D does not run.
    [1]  CLASS B REACHABLE. Z=21 4d must return CLASS B, reproducing s42's
         minlog=+0.9083. This is a determinism receipt on the failure side.
    [2]  CLASS A REACHABLE. Force it — ask for a node count the field demonstrably
         cannot carry (a high n at a low Z). If CLASS A cannot be produced ON DEMAND,
         **T-D has no falsifier and MUST NOT BE FILED.** That is F65.1's rule.

Only if [0], [1] and [2] all pass does the prediction get written and hashed.

## §4 · BUDGET, DECLARED (§2.20) AND ZENO-SEGMENTED
Solves ARE required — this is not a sealed-data test. Segments, each closed and
receipted before the next opens:

    SEG 1   can-fail [0][1][2] and read the exact failure list off the sealed rows.
    SEG 2   prediction written, hashed, filed. NOTHING RUN IN THIS SEGMENT.
    SEG 3   the light atoms: Z = 21, 31, 39, 49.
    SEG 4   the heavy atoms: Z = 57, 81, 89, 113. Z=113 last and separately —
            it is beyond the 107-row derivation boundary (Z=2..108) and its result
            is OUTPUT, not derivation. It is NOT scored into the denominator.
    SEG 5   score against the filed sha; write up; seal.

If SEG 3 overruns, SEG 4 is deferred and the test is scored over the atoms it
actually covers, reported as such, and NOT compared against eleven.

## §5 · WHAT T-D CANNOT DO
It is not a derivation and it does not touch the sealed chain, any margin, any
entrant, the ordering clause, or Deliverables 1, 3, 4 or 5. A CLASS A result would
not by itself derive anything; it would establish that a quantity the Madelung
statement presupposes is absent from the field, which is the precondition for asking
the question in a different language — not the answer.

## §6 · WHAT IS NOT PROPOSED
No edit to `nlchain.py`, `hfc2.py`, `t7c_hfsr.py`, `t7f_rep.py` or `t7g_exc.py`
(F44.1 route: a new driver in pack66 beside them). No adoption of NodeGated's
bracket — s42 tested it and it FAILED D2. No re-run of the s42 Z=21 probe beyond the
one determinism receipt in [1].
