# F44.2 — s43 ATTRIBUTED THE MARGIN NARROWING TO 4d. THE SAME SEALED ROWS SAY THE RUNNER-UP IS 5p.

Registered s44, at the read step, BEFORE PREDICTION-CHAIN-4d was written and before nlchain
was pointed at Z=39. Same class as F43.2: a cause asserted without reading the column that
carries it. Mine, one session earlier.

## 0 · THE CLAIM AS FILED

`FINDING-CHAIN-4p.md` §4, and carried up into BRIDGE-43 §2(6) as a numbered finding:

    The margin NARROWS from 0.07991 (Z=37) to 0.05639 (Z=38) -- the only place in this row
    where the margin moves against the trend. ... **That is the 4d competition tightening as
    Z=39 approaches.**

The two margins are correct. The attribution is not.

## 1 · WHAT THE `order` COLUMN ACTUALLY HOLDS

`margin` is defined at `nlchain.py` line 76 as `D[runner-up] - D[winner]` over the sorted
candidate list. It says how far the winner leads **whatever is second**, and it does not name
what that is. The `order` field does. Read off the sealed rows:

    Z=36  4p -0.48627 | 5s -0.13437 | 5p -0.08713 | 4d -0.05966     margin 0.35190
    Z=37  5s -0.13964 | 4d -0.05973 | 5d -0.03373 | 4f -0.03126     margin 0.07991
    Z=38  5s -0.17457 | 5p -0.11818 | 4d -0.09658 | 6s -0.06892     margin 0.05639

**THE RUNNER-UP CHANGES IDENTITY BETWEEN Rb AND Sr.** At Z=37 it is 4d. At Z=38 it is 5p,
and 4d has been pushed to third. The margin that narrowed is `5s - 5p` at Z=38 and `5s - 4d`
at Z=37: **the two numbers compared in the finding are gaps between different pairs of
channels.**

## 2 · THE 5s-4d GAP, WHICH IS THE QUANTITY THE FINDING MEANT, IS FLAT

    Z=37   5s - 4d  =  -0.13964 - (-0.05973)  =  0.07991
    Z=38   5s - 4d  =  -0.17457 - (-0.09658)  =  0.07799

**A narrowing of 0.00192 across one proton, against the 0.02352 the finding reported.** The 4d
competition is not tightening in any measured sense; it is holding station. 4d deepens by
0.03685 and the winning 5s deepens by 0.03493 — 4d is tracking the winner, not closing on it.

**What actually happened between Rb and Sr is that 5p arrived**, moving from outside the top
four at Z=37 to second place at Z=38. That is the unexplained event in the row, and s43 did not
see it because it read `margin` and never read `order`.

## 3 · WHY THIS MATTERS MORE THAN AN ARITHMETIC SLIP

The finding was filed as a MEASURED APPROACH — explicitly not a prediction, precisely so that it
could be leaned on without R 1449 scoring. It then became bridge §2(6) and bridge §4(2)'s reason
for calling the 4d row "the most informative row yet reached". **A misattributed measurement
that is exempt from prediction-scoring propagates further than a failed prediction does,
because nothing is set up to catch it.**

And it inverts the shape of the coming test. On s43's reading, 4d is closing on 5s and Z=39 is
the natural crossover. On the measured reading, **4d must at Z=39 overtake BOTH 5p and 5s from
third place, gaining 0.078 on the winner in one proton after gaining 0.002 in the last one.**
That is a far stronger demand on the field, and it is what PREDICTION-CHAIN-4d must be written
against.

## 4 · SCOPE — WHAT IS AND IS NOT TOUCHED

Touched: `FINDING-CHAIN-4p.md` §4 and BRIDGE-43 §2(6), interpretation only.
**Not touched: every number in the 4p row.** The eight chain rows, the eight scored claims, the
per-proton steps, PD-6's exception set and the argmin-n finding are unaffected — none of them
depends on the identity of the runner-up. §2(4), the row's stated real result, stands.

Per H.4 the sealed files are NOT rewritten. This entry is the correction, and BRIDGE-44 §2 will
carry the corrected reading beside a pointer here.

## 5 · REMEDY

`order[1]` is already in every row; nothing needs computing. **The remedy is that `margin` must
never again be quoted without the channel it is a margin against.** Proposed for the nlchain
show table and for every future finding file: report `margin` as `0.05639 (vs 5p)`, so that a
change of runner-up is visible in the same glance as a change of gap. This is the configuration
column's argument (s41 finding 5) applied to the ordering: **a scalar that summarises a ranked
list hides the rank.**
