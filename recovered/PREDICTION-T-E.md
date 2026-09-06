# PREDICTION — T-E. IS THE minlog DESCENT A STEP OR A SLOPE?
# FILED SESSION 67 BEFORE `pack67/nodespec67.py` EXISTED AND BEFORE ANY CELL AT ANY Z
# IN THE SCORED SET WAS COMPUTED. R 1449 / §2.13. Scored only after this file's sha is
# verified against pack67/PREDICTION-T-E.sha256; the driver halts without it.
# M's rulings this session: (1) F67.1 confirmed. (2) the separating test runs.
# s66 ruling (2) STANDS AND IS INHERITED: Z<=108 is the derivation. Every scored cell
# here is Z<=70. Nothing above 108 is touched.

## THE QUESTION, STATED SO IT CAN ONLY GO ONE OF TWO WAYS
F67.1 withdrew "minlog falls systematically with Z" — false on its own rows, since
Z=49 exceeds Z=39 in both channels. What the ten s66 rows DO show is two disjoint
clusters with an empty gap:

    GROUP L   Z = 21, 39, 49   six cells    +0.4368 .. +1.2644
    GROUP H   Z = 57, 89       four cells   +0.0401 .. +0.0937
    nothing between +0.0937 and +0.4368     (factor 4.66, empty)

Two readings, and NOTHING IN THE TEN CELLS PICKS BETWEEN THEM, because Z, n, tgt,
nd_max and f-presence all move together across that sample:

  (S) SLOPE.     minlog is a continuous function of Z (or of something that moves with
                 Z) and the "gap" is only the sampling — no atom was measured between
                 49 and 57. The descent continues below Z=57 and may reach zero.
  (T) THRESHOLD. minlog takes one value in the absence of a collapsed f shell and a
                 much smaller one in its presence, switching at the 4f collapse.
                 There is no descent to continue and nothing to extrapolate.

**The archive fixes the threshold's location independently and BEFORE this test.**
`DELIVERABLE-3-COLLAPSE-CONDITION.md` §3, sealed: 4f sits on a flat plateau at
n* = 3.998 across Z = 53..56, is in transit at Z = 57 (n* 3.9930 -> 2.1764, dn*/dZ =
-1.8166), and is collapsed by Z = 58 (n* = 1.1672). **Reading (T) therefore predicts the
step between Z=56 and Z=58 and nowhere else, and it made that prediction before this
file, from a different instrument, for a different purpose.**

## WHAT IS IN HAND BEFORE THIS FILE, AND DECLARED (no minlog is)
A survey of the sealed chain's own `fail` dictionaries, Standing 5, counts and sets
only, no solves:

    d-channel node-count failures, Z = 50..56 :  Z=50 5d,6d | Z=51 5d | Z=52..56 NONE
    d-channel node-count failures, Z = 58..70 :  6d and 7d at EVERY atom, 26 cells
    s66 per-cell cost                         :  1 to 3 s, ten cells in 21 s total

**The pre-side is thin and is declared thin.** Z=52..56 carry no d node-count failure,
so this test CANNOT pin the step to one proton. It can only bound it to 51 < Z < 58.
That is stated here, in advance, as a limit of the test and not discovered afterwards.
**The load-bearing clause is therefore PS-2, on the post-side, where thirteen
consecutive atoms are available and the two readings differ sharply.**

## THE SCORED SET — TWENTY-NINE CELLS, ALL Z <= 70, FIXED HERE AND NOT CHANGEABLE
    Z=50  5d (tgt2 short1)   Z=50  6d (tgt3 short1)   Z=51  5d (tgt2 short1)
    Z=58..70  6d (tgt3 short1) and 7d (tgt4 short1) — 26 cells, every atom, no gaps
If a cell errors or returns NO-RAISE it is reported as such and the clause is scored
over the cells actually returned, stated as such, and NOT against 29.

## PS-0 · DETERMINISM GATE, WITH THE REFERENCE'S PRECISION STATED (Standing 12, F66.2)
The s67 driver is a copy of the sealed `pack66/nodespec.py` differing ONLY in the three
path constants CACHE, PRED, PSHA. Scan geometry, bound range, grid and shoot are
untouched. Before any scored cell runs, the driver recomputes **Z=39, both channels**,
which s66 measured and cached:

    (i)   Z=39 5d returns CLASS B with minlog == 0.4649
    (ii)  Z=39 6d returns CLASS B with minlog == 0.4368

**Precision, stated rather than assumed:** `nodespec.py` itself stores
`round(min(...), 4)`. The reference therefore carries exactly four decimals and the new
value is produced by the identical rounding, so **exact equality of the 4-dp values is
the correct specification and is satisfiable.** This is the defect of F66.2 repaired at
the point where it was made, not after the number is read. If either clause fails, the
copy is not the parent, T-E DOES NOT RUN, and nothing below is scored.
Z=39 is NOT in the scored set and its minlog is already published, so PS-0 carries no
information about the outcome — it is an instrument check only.

## THE PREDICTIONS

**PS-1 · THE STEP IS LARGE AND IT IS WHERE THE COLLAPSE IS.** Same channel, across the
unmeasurable gap: **minlog(Z=50, 6d) / minlog(Z=58, 6d) >= 4.0.**

**PS-2 · THE HEADLINE, AND IT IS THE DISCRIMINATOR:**
> **ONCE 4f HAS COLLAPSED, minlog IS FLAT. Across Z = 58..70, taken per channel,
> max/min <= 3.0 for 6d AND max/min <= 3.0 for 7d, AND neither channel is monotone
> decreasing across all thirteen atoms.**
Reason stated in advance: under reading (T) the quantity switches at a threshold and
has no Z-dependence to continue; thirteen added protons past the switch should move it
little. Under reading (S) thirteen protons is MORE than the eight that carried Z=49's
+0.77 down to Z=57's +0.073 — a factor of ten — so (S) requires a large, ordered,
continuing descent across exactly this range. **The two readings cannot both survive
PS-2.**

**PS-3 · THE PRE-SIDE STAYS HIGH.** All three pre-collapse cells — Z=50 5d, Z=50 6d,
Z=51 5d — return **minlog > 0.20**, the divider being the geometric mean of the two
observed band edges (+0.4368 and +0.0937), fixed here at 0.20 before any is measured.

**PS-4 · CLASS C IS STILL DEAD, AND CLASS A WITH IT. PREDICTED 29 OF 29 CLASS B.**
This is the direct test of the s66 §6 worry. §6 said that if minlog crosses zero the
cell becomes CLASS C. Thirteen atoms lie past the point §6 expected further decline.
**If minlog ever crosses zero in this range, a CLASS C appears here.** Predicted: none
does, at any of the 29.

**PS-5 · WHAT IS NOT PREDICTED.** Any eigenvalue. Any nd_max. Any win_pts. Any
sign_changes count. Any iteration count. Any D. Any margin, entrant, ordering, rung or
bound. The step's location within 51 < Z < 58 beyond that bound. Whether 7d behaves as
6d does at the pre-side (7d does not fail at Z=50 or 51 and is not in those cells).
Anything about f or g channels — 149 f and 63 g node-count failures exist in the sealed
chain and NONE is in this test. Anything about Δδ or α: T-E measures a norm condition,
not a defect, and no bridge between them is claimed here.

## STANDING 7b — HOW THIS TEST IS PROVEN ABLE TO FAIL, FROM THE ARCHIVE
Not by construction:
  * **minlog demonstrably varies by a factor of 31** across s66's ten sealed cells
    (+0.0401 to +1.2644), and non-monotonically in Z. A flatness clause over thirteen
    atoms is therefore a real constraint on a quantity already known to move.
  * **PS-3's divider lies strictly inside the observed empty gap**, with measured values
    on both sides of it. Either side is attainable.
  * **CLASS A and CLASS C are live branches of the same scan**, separated by whether tgt
    appears in nd(e) and by the sign pattern of log(nrm) within the window. s42
    demonstrated CLASS B and inertness reachable; neither A nor C is excluded by the
    instrument, only by this prediction.
  * **PS-1 and PS-2 can fail independently.** A large step with a continuing post-side
    descent falsifies PS-2 alone; a smooth slope with no step falsifies both.

## HOW THE OUTCOMES READ, FIXED IN ADVANCE
  * **PS-1, PS-2, PS-3 all hold.** The descent is a STEP, bounded to 51 < Z < 58, and it
    coincides with a 4f collapse that a different sealed instrument located at Z=57
    before this test existed. Reading (S) dies; §6's extrapolation in Z has nothing to
    extrapolate along, and F67.1's withdrawal is completed rather than merely asserted.
    **What minlog then measures is the presence of a collapsed f shell in the core** —
    a property of the same core/tail crossover region that
    `FINDING-ALPHA-THE-WHY.md` §7 names as what must set Δδ. That is a connection, and
    it is filed as a connection and NOT as a result.
  * **PS-2 fails with an ordered descent through 58..70.** Reading (S) is alive, minlog
    does track a continuous variable, and §6's zero-crossing worry is real and must be
    carried. Report it, and per F65.1 propose NO replacement mechanism in the session
    that establishes it.
  * **PS-3 fails.** The step lies below Z=50 and the collapse-at-57 location is refuted.
    Report the bound and do not re-site the step in this session.
  * **Any CLASS C.** Reading (2) of the s65 bridge is alive at that atom, the sealed
    chain is dropping a channel it could have found, and it is reported FIRST, before
    any other clause, as a fault against the chain.

## BUDGET, DECLARED (§2.20), ZENO-SEGMENTED
    SEG A   PS-0 gate, Z=39 both channels                        budget 300 s
    SEG B   Z = 50, 51 — the three pre-side cells                budget 300 s
    SEG C   Z = 58..64 — fourteen cells                          budget 900 s
    SEG D   Z = 65..70 — twelve cells                            budget 900 s
Segments run in order and a later one does not start until the earlier one has closed.
If a segment overruns it is reported OVERRUN and the affected clause is scored over the
cells actually covered, stated as such.

## WHAT T-E CANNOT DO
It is not a derivation of anything. It touches no sealed file, no margin, no entrant,
no ordering, no rung and no Deliverable. It does not measure Δδ, α, or any defect. A
step at the collapse would establish that the d-channel norm condition is governed by
the presence of a collapsed f shell rather than by Z. That is a fact about the field,
and it is a precondition for asking whether the same region sets Δδ. **It is not that
answer and does not bear on it without further work that is not proposed here.**
