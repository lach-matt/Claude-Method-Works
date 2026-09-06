# PREDICTION — RUNG 0 ASSEMBLY: THE CHECKABLE CLAUSES
# FILED SESSION 63, BEFORE ANY CHAIN ROW WAS READ AND BEFORE ANY CODE OF THIS
# SESSION'S TESTS WAS WRITTEN OR RUN. R 1449.
# Scope: the assembly is a WRITING task, but it makes CLAIMS about what the sealed
# chain shows. Those claims are predicted here so they cannot be fitted afterwards.
# Scored only after the sha of this file is verified against the pre-run record.

## WHY THIS FILE EXISTS AT ALL FOR A WRITING TASK
Rung 0 is the written reverse chain. A document cannot be falsified by a run. But
the document will assert that the sealed walk EXHIBITS certain structures — the
period lengths, the n+l ordering, the tie-break — and those are readings of data
this session has not yet looked at. **If they are read first and asserted second,
the assembly is a description of what was found, not a derivation that predicted
it.** The Challenge asks for a derivation. So the structures are predicted here,
from the chain's construction alone, and read afterwards.

The chain's construction is fixed and sealed: cfg(Z) = cfg(Z-1) + argmin_c D(c),
D(c) = E_HF(cfg(Z-1)+c ; nuclear charge Z) - E_HF(cfg(Z-1) ; nuclear charge Z),
on the scalar-relativistic average-of-configuration Hartree-Fock field, CORR=False,
c = 137.035999 the only number ever entered. Nothing below is tuned to make it come out.

## A0 — THE CHAIN IS COMPLETE AND CONTIGUOUS
`nlchain.jsonl` carries a row for every Z in 2..120 with no gap and no duplicate:
**119 rows, min Z = 2, max Z = 120, len(set) = 119.**
FALSIFIER: any gap, any duplicate key, or any row whose `ent` is absent.
If this fails, every clause below is void and the assembly cannot be written from
this artefact.

## A1 — THE PERIOD LENGTHS. **THIS IS CHALLENGE CRITERION 2 (period sequence) AND
## IT HAS NOT PREVIOUSLY BEEN EXTRACTED FROM THE WALK.**
Define, using ONLY the chain's own entrant column and nothing from `ground.py`:
a NEW PERIOD begins at each Z whose entrant is an `ns` channel (l=0) with n
strictly greater than every n previously entered as an s channel. Period length is
the difference between consecutive period-start values of Z.

PREDICTED period starts:   Z = 1, 3, 11, 19, 37, 55, 87, 119
PREDICTED period lengths:  **2, 8, 8, 18, 18, 32, 32**  and period 8 open at Z=119
                           with 2 rows of it walked (Z=119, 120).

This is the exact sequence the 1969 Challenge names. It is predicted to fall out of
the entrant column with no shell-capacity rule imposed and no period boundary
defined in the code — `nlchain.py` contains no notion of a period anywhere.
FALSIFIER: any length differing from 2,8,8,18,18,32,32, or a period start at a Z
not in the list above. A single wrong length falsifies the period-sequence claim
and it must be reported as a failure of the derivation, not smoothed over.

## A2 — THE ORDERING CLAUSE OF MADELUNG
Order the channels by the Z at which each is FIRST entered by the chain. Along that
sequence, **n+l is non-decreasing.**
PREDICTED: zero inversions in n+l over the whole first-entry sequence.
FALSIFIER: any channel first entered after a channel of strictly larger n+l.
This is the primary object of the Challenge and a single inversion is a failure.

## A3 — THE TIE-BREAK CLAUSE OF MADELUNG
Within each block of equal n+l, first entries are ordered by **increasing n**.
PREDICTED: zero violations, over every n+l block the chain reaches.
Prior sessions established this over 26 steps and three distinct pairs (4s/3d,
4p/5s, 4d/5p). PREDICTED HERE over the WHOLE chain, which is the stronger claim
and the one the assembly needs.
FALSIFIER: any equal-(n+l) block whose first entries run high-n before low-n.

## A4 — THE MADELUNG SEQUENCE ITSELF, AS A STRING
The first-entry order predicted, in full, is
    1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p 8s
possibly continuing 5g at or before Z=120 if the field places it there.
FALSIFIER: any departure from this string in the region the chain covers.
**DECLARED IN ADVANCE, BECAUSE IT IS THE HONEST RISK:** the walk is known to
disagree with the OBSERVED configuration at some rows (the `ok=False` rows, the
Cr/Cu-type anomalies). A2/A3/A4 are claims about the CHAIN'S OWN first-entry
order, which is what the derivation produces. They are NOT claims that the chain
reproduces every observed ground state, and must not be read as such. Criterion 7
is answered by A5, separately and on its own terms.

## A5 — THE EXCEPTIONS ARE A FORMAT LIMITATION, AND THE COUNT IS PREDICTED
The `ok` column compares the chain's entrant to the observed differentiating
electron where `ground.py` has a measured configuration.
PREDICTED: the rows scoring `ok=False` are a MINORITY, they cluster in the d and f
blocks, and **every one of them is an element whose observed ground state differs
from the aufbau configuration by the PROMOTION OF AN ALREADY-PLACED ELECTRON**
(s->d or s->f), not by the placement of the differentiating electron in a channel
of different n+l. A one-electron walk cannot express a promotion of an electron it
placed at an earlier Z; the format has no move for it.
PREDICTED count of `ok=False` rows: **fewer than 25 of the scored rows.**
FALSIFIER, and it is the one that would matter: an `ok=False` row where the
observed differentiating electron enters a channel of DIFFERENT n+l from the
chain's entrant AND no promotion of an already-placed electron accounts for the
difference. That would be a genuine counterexample to the rule rather than to the
format, and it must be reported as such, first, before anything else.

## A6 — THE SEED cfg(1) = 1s IS DERIVED, NOT CHOSEN
`nlchain.py:35` seeds the walk with `d = {(1,0): 1}` and SPEC §3 labels this
CHOSEN. **It is predicted to be DERIVABLE on the walk's own field**, which would
remove the last declared choice from the chain's inputs and is worth the three
solves it costs.
Solving Z=1 with the ruling path (`nlguard.run_guarded`, CORR=False, c=C0) for the
single-electron configurations 1s, 2s and 2p:
    PREDICTED  E(1s) < E(2s) < E(2p),  1s the argmin, by a wide margin
    PREDICTED  E(1s) = -0.5000 Ha to within 1 mHa of exact non-relativistic
               hydrogen, the residual being the scalar-relativistic correction
               (s62 Rung 5 already measured -0.500008079; this must reproduce it)
    PREDICTED  E(2s) and E(2p) near -0.125 Ha, the hydrogenic n=2 value
FALSIFIER: 1s not the argmin at Z=1 -> the seed IS a choice and must stay labelled
CHOSEN in the assembly's ledger. Report it as such; do not quietly keep the label.
FALSIFIER: E(1s) not reproducing s62's -0.500008079 -> a determinism failure, which
outranks this test and is reported first.

## A7 — THE CONSTANT LEDGER IS EMPTY BUT FOR c
Every numerical quantity on the live path from `nlchain.step` down to the C kernel
is DERIVED, PHYSICALLY FIXED, or NUMERICAL (mesh, tolerance, damping). PREDICTED:
the only physical constant is c = 137.035999, and the only quantities that are
neither derived nor physical are the numerical controls whose effect on the answer
has been bounded by Rungs 3, 4 and 7 at <= 0.05 mHa against margins of 32 mHa and up.
FALSIFIER: any coefficient on the live path that is neither derived from the HF
formalism nor a bounded numerical control. That would breach criterion 4 and is the
worst outcome available to this session.

## WHAT THIS FILE DOES NOT PREDICT, STATED SO IT CANNOT BE OVERCLAIMED
It does not predict that Rung 2 (the single-configuration bound) will close. Rung 2
is owed and is to be finished inside the assembly; whatever it returns is returned.
It does not predict that the deferred items — the F61.1 55-row re-walk, the Z=59
residue, the coupled 4f2.5d SO check, the s56 2.88 mHa residue, the promotion
operator — will be resolved. They are named as open by M's ruling and stay named.
It does not predict anything about rows above Z=108, which carry PREDICTED labels
and have no measured configuration to score against.