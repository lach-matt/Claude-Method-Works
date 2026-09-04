# F66.1 — THE RULED FIRST TASK OF SESSION 66 IS ALREADY ANSWERED IN THE ARCHIVE
# Raised 2026-08-20, SESSION 66, AT THE OPEN, BEFORE ANY PREDICTION WAS FILED AND
# BEFORE ANY SOLVE WAS RUN. Standing 6 — SEARCH THE ARCHIVE BY CONTENT BEFORE
# DECLARING A GAP — was run this time, and it fired.
# No sealed file is edited. No prediction is filed. R 1449 intact.
# Same class as F65.2, caught one stage earlier: at ruling time, not at write-up time.

## WHAT WAS RULED
`BRIDGE-LOWDIN-SESSION-65.md` §3, and item 1 of the s66 work list, ruled FIRST and
ahead of everything: THE NODE-COUNT NULL. It states two readings of the eleven
node-count failures (Z = 21, 31, 39, 49, 57, 81, 89, 113 across 4d/5d/6d/7d, each
returning exactly one node short of the hydrogenic label, 7d@81 short two):

  (1) the field supports one fewer bound d state than the labelling assumes — a
      Challenge-level statement, and M's standing point that a null is a gap
      needing a different mathematical language;
  (2) the shooting solver's search bracket, the state being present but unfound.

And it states: **"NOTHING IN HAND PICKS BETWEEN THEM."** It then rules the test —
"count the d eigenvalues the field actually supports at Z=21 by widening the search."

## THAT SENTENCE IS FALSE. THE ARCHIVE PICKS BETWEEN THEM AT Z=21, TWICE OVER.

**`pack42/FINDING-PROBE-4D.md` (s42, item 0) ran exactly the ruled test and more.**
It is titled *F39.2 IS NEITHER (a) NOR (b)*, where (a) and (b) are, verbatim in
substance, readings (1) and (2) above:

  * **Reading (2) — bracket — REFUTED by measurement.** §1(b): the it2 seed sits at
    eh = −0.040180 with **nd = 1 AT THE SEED**. The bracket STARTS ON THE CORRECT
    STATE. It is not outside anything.
  * **Reading (1) as stated — "unbound in the field" — REFUTED by measurement.**
    §1(a): the tail is exactly Coulombic, V·r = −1.000000 at r = 30, 60, 100, 200,
    298; `_ceff = 0` for the q=1 shell; the ℓ=2 well supports nd = 1, 2, 3 and 5
    states at e < 0. The channel is bound and the well is deep enough.
  * **The mechanism was found and named.** §2–§3: the 4d solution EXISTS at it1
    (e = −0.047224, nd = 1) and is GONE at it2. A 421-point fine scan across the
    whole nd = 1 window at it2 finds **ZERO sign changes of log(nrm)**; closest
    approach min log(nrm) = +0.892, the norm 2.44× too large — structural, not a
    near-miss. The diffuse Rydberg orbital re-drives its own exchange source and
    destroys its own root. §4: the bracket then walks DOWN and OUT past the window
    and bisects a two-root bracket, returning the nd = 0 state.

**AND `pack42/FINDING-REPAIR-4D.md` §2 then settles the physics, which is the part
the s65 bridge needed and did not have:**

> "The self-consistent field of [Ar]4s²4d¹ at Z=21 has NO normalisable 1-node
> solution. Not at the start, not on the path, not at the fixed point... AND IT IS
> NOT A NUMERICS FAULT: IT IS THE FIELD ANSWERING CORRECTLY. Neutral scandium has
> no self-consistent 4d channel — the d electron collapses to 3d... **The raise is
> the correct answer delivered through the wrong exception.**"

All three candidate repairs FAILED D2 (NodeGated loudly and correctly; mixing
damping at β = 0.20, 0.10, 0.05, 0.02 — so it is not a step-size problem; ChannelHold
spuriously, caught by a cross-check written before the run).

## WHAT THIS COSTS THE RULED ITEM
The ruled test — widen the search at Z=21 and count the d eigenvalues the field
supports — **has been run twice at s42, on a finer instrument than the one proposed
(per-iteration trace plus a 421-point scan, at it2 AND at the fixed point).** Running
it again would consume the session's first and highest-priority slot to re-derive a
closed item. That is F65.2's failure exactly, one stage earlier in the pipeline.

## WHAT IS *NOT* IN THE ARCHIVE — AND IT IS THE BETTER ITEM
s42 established this **at one atom and one channel: Z=21, 4d.** The s65 bridge's
observation that the shortfall is **exactly one node in eleven instances spanning a
hundred protons** is not answered anywhere. Nor is 7d@81, which is short TWO.

`pack44/FINDING-CHAIN-4d.md` §2 names the un-run work in terms of an instrument that
already exists and is sealed:

> "Running the row's failures through HFCN would name every one of the 23 failures by
> channel, eigenvalue and node target for the cost of no new physics. **Filed as the
> natural next use of the s43 instrument; not opened here.**"

That was filed at s44 and has not been opened in twenty-two sessions.

TWO SEALED INSTRUMENTS ARE IN HAND, BOTH VERIFIED D1-INERT ON HEALTHY CHANNELS:
  * `rt/t7g_exc.py` — `HFCN`, ADOPTED at s43 on M's ruling (2), exception-naming only.
    Carries (Z, n, ℓ, e, nd, tgt). Says WHICH state was returned instead.
  * `rt/t7f_rep.py` — `NodeGated`, NOT adopted (bracket rejected), but present, sealed
    and read-only usable as s42 used it. It is the one that DISCRIMINATES, because it
    raises two DIFFERENT exceptions:
        "no nd==tgt window exists"                  -> the field carries no such state
        "window exists but log(nrm) has no zero"    -> the s42 self-destruction
    **That distinction is the whole question, and it is per-channel and per-atom.**

## STATUS
OPEN pending M's ruling. No prediction filed, no run made, nothing edited. The
replacement item is set out in `pack66/PROPOSED-T-D-REPLACEMENT.md`.
