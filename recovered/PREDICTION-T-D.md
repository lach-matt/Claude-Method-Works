# PREDICTION — T-D. THE NODE-COUNT NULL, DERIVED FROM THE MEASURED NODE SPECTRUM.
# FILED SESSION 66 BEFORE `pack66/nodespec.py` EXISTED AND BEFORE ANY SPECTRUM WAS
# COMPUTED AT ANY ATOM. R 1449 / §2.13. Scored only after this file's sha is verified
# against pack66/PREDICTION-T-D.sha256; the scorer halts without it.
# M's rulings this session: (1) T-D runs. (2) Z<=108 is the derivation; anything above
# 108 is strictly theoretical, run as OUTPUT to fill unwitnessed spectroscopic values,
# NEVER scored and NEVER in a denominator. (3) CLASS A IS TO BE DERIVED, NOT FORCED.

## RULING 3 IS THE DESIGN, AND IT KILLED THE GATE I PROPOSED
`PROPOSED-T-D-REPLACEMENT.md` §3 gate [2] asked to force CLASS A by requesting a node
count the field cannot carry. **WITHDRAWN.** That manufactures the outcome under test —
Standing 7's defect one level up, and F65.1's. The classification is instead READ OFF A
MEASURED QUANTITY: for each failing channel the instrument reports the node spectrum
nd(e) across the bound range, and the class is a consequence of that spectrum.

    CLASS A   the spectrum NEVER attains tgt anywhere in e<0.
              The self-consistent field carries no state with the node count the label
              (n,l) demands. Reading (1) of the s65 bridge. Challenge-level.
    CLASS B   the spectrum attains tgt, and log(nrm) has NO zero in that window.
              The s42 mechanism: the state exists and the SCF update destroys it.
    CLASS C   the spectrum attains tgt and log(nrm) HAS a zero there.
              The state is present AND findable; the parent's bracket walked out.
              Reading (2) of the s65 bridge.

## STANDING 7b — HOW THIS TEST IS PROVEN ABLE TO FAIL, WITHOUT FORCING ANYTHING
Not by construction, but from the sealed archive, which already contains both a
non-trivial outcome and the inert one:
  * **CLASS B is demonstrably reachable.** `pack42/FINDING-REPAIR-4D.md` §1(i) records
    NodeGated raising, at Z=21 4d, `nd==1 window exists but log(nrm) has no zero in
    it ... minlog=+0.9083`. That is a CLASS B measurement, already published.
  * **Inertness is demonstrably reachable.** s42 D1: identical to the parent on healthy
    channels, to 3e-6 against the banked Z=21 3d D = -0.26664.
  * **A and C are distinct branches of the SPECTRUM, not of a raise.** They are
    separated by whether tgt appears in nd(e) and, if it does, by the sign pattern of
    log(nrm) within that window. Both are measurable outcomes of the same scan and
    neither is constructed.
Therefore T-D has live falsifiers in three directions and is admissible.

## WHAT IS IN HAND BEFORE THIS FILE, AND DECLARED (no result is)
A survey of the SEALED chain's own `fail` dictionaries — counts and sets only,
Standing 5, no solves. It corrects the s65 bridge's framing and is NOT a prediction:

    node-count failures in the sealed chain      383
    of which l=2 (d)                             162   across 83 distinct Z
    d shortfall (tgt-got) takes ONLY two values  1 (135 cells)   2 (27 cells)
    a d channel is NEVER returned with too many nodes
    4d fails Z=21..33 | 5d Z=20..51 | 6d Z=39..83 | 7d Z=57..116 | 8d Z=89..119

**The s65 bridge's "eleven instances" is a sample of a population of 162.** The
shortfall is an integer taking exactly two values across a hundred protons. That
regularity is what T-D is aimed at, and it is sealed data, not a result of this test.

## THE SCORED SET — TEN CELLS, ALL Z<=108, FIXED HERE AND NOT CHANGEABLE AFTER
Read off the sealed rows before this file was written:

    Z= 21   4d tgt1 got0 short1        Z= 49   5d tgt2 got1 short1
    Z= 21   5d tgt2 got0 short2        Z= 49   6d tgt3 got1 short2
    Z= 39   5d tgt2 got1 short1        Z= 57   6d tgt3 got2 short1
    Z= 39   6d tgt3 got2 short1        Z= 57   7d tgt4 got3 short1
                                       Z= 89   7d tgt4 got3 short1
                                       Z= 89   8d tgt5 got4 short1

## THE PREDICTIONS

**PD-0 · INERTNESS.** NodeSpec on the healthy Z=21 3d channel does NOT raise, and the
chain D reproduces the banked -0.26664 to |d| <= 3e-6 (s42's own tolerance after
F42.2). If it raises or drifts, T-D DOES NOT RUN and nothing below is scored.

**PD-1 · DETERMINISM ON THE FAILURE SIDE.** Z=21 4d returns **CLASS B**, with the
tgt=1 window present and **minlog = +0.9083 +/- 0.01** on the 160-point grid,
reproducing s42's NodeGated value. A ninth determinism receipt, and a receipt against
a DIFFERENT SESSION's instrument rather than against this chain's own cache.

**PD-2 · THE HEADLINE, AND IT IS THE DISCRIMINATOR:**
> **THE SHORTFALL INTEGER IS THE CLASSIFIER. short1 -> CLASS B. short2 -> CLASS A.**
Reason stated in advance: a shortfall of one is one destroyed root, which is exactly
what s42 measured. **A shortfall of two cannot be one destroyed root** — it requires
that the label's node count is absent from the field altogether.

    PREDICTED, CELL BY CELL:
      CLASS B (8):  21 4d | 39 5d | 39 6d | 49 5d | 57 6d | 57 7d | 89 7d | 89 8d
      CLASS A (2):  21 5d | 49 6d

**PD-3 · THE CEILING.** In every CLASS A cell, the MAXIMUM nd attained anywhere in
e<0 equals `got`, the node count the sealed chain reported. The solver returns the
highest bound d state the field actually carries, and the label asks for one above it.

**PD-4 · CLASS C IS DEAD. PREDICTED 0 OF 10.** Reading (2) of the s65 bridge — the
solver bracket, state present and findable — is predicted to occur at NO cell. s42
refuted it at Z=21 by showing the seed sits INSIDE the window with nd=1. If any cell
returns CLASS C, reading (2) is alive at that atom and PD-4 is false.

**PD-5 · WHAT IS NOT PREDICTED.** The eigenvalues. The minlog values other than
Z=21 4d. The iteration at which each raise occurs. Any D. Any margin, entrant,
ordering or rung. Whether the same law holds for f or g channels — 149 f and 63 g
failures exist in the sealed chain and NONE is in this test.

## HOW THE OUTCOMES READ, FIXED IN ADVANCE
  * **PD-2 holds 10/10.** The shortfall integer is a measured classifier, and CLASS A
    is DERIVED at two atoms: the self-consistent field carries no state with the node
    count the Madelung label presupposes. **That is the Challenge-level statement in
    its exact form** — the rule is stated in a labelling the field does not carry —
    and it is reached by measurement, not by reading.
  * **All ten CLASS B.** Reading (1) dies everywhere. The null is uniformly an
    instrument property and item 1 closes NEGATIVELY. Honest, cheap, and it retires a
    standing ambiguity.
  * **Any CLASS C.** Reading (2) is alive and the sealed chain is dropping channels it
    could have found. That would be a fault against the chain and is reported FIRST,
    before any interpretation, as F66.2.
  * **A/B split that is NOT the shortfall.** PD-2 is false in its detail; report the
    split and DO NOT substitute a new classifier in the same session (F65.1's rule).

## BUDGET, DECLARED (§2.20), ZENO-SEGMENTED
The raise occurs during SCF, not at convergence, so each cell costs a few iterations
plus a 160-point scan — cheap, unlike a converged solve.
    SEG 3   Z = 21, 39, 49   (six cells)      budget 900 s
    SEG 4   Z = 57, 89       (four cells)     budget 900 s
    SEG 4b  Z > 108, OUTPUT ONLY, unscored, ruling (2). Run only if SEG 3+4 complete.
If a segment overruns it is reported OVERRUN and the test is scored over the cells
actually covered, stated as such, and NOT against ten.

## WHAT T-D CANNOT DO
It is not a derivation of the Madelung rule and it touches no sealed file, no margin,
no entrant, no ordering clause, and no Deliverable. A CLASS A result establishes that
a quantity the Madelung statement presupposes is ABSENT from the field at that atom.
That is a precondition for asking the question in another language. It is not the
answer.
