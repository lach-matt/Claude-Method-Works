# FINDING R4-07 — a recorded figure defect that does not survive the precision of its own inputs, and three that do. NOT REPAIRED.

Measured 6 September 2026. `method/proofs/precision.py` holds the test; its selftest asserts the
arithmetic of every case and each is checkable by hand.

## The question this asks, and why it is not the question `arith.py` asks

A derived figure that disagrees with a recomputation is not therefore wrong. **If its inputs are
printed rounded, the recomputation inherits their slack.** A number printed as *25.96* is not
25.960000; it stands for the interval [25.955, 25.965). Divide two such numbers and the quotient is
an interval, not a value.

`arith.py` scores a stated equality under rounding conventions. **This asks a different question:
does the printed figure lie inside the interval its printed inputs allow?** Three verdicts:

| | |
|---|---|
| **INSIDE** | the figure is consistent with its inputs at their printed precision. **Not a defect.** |
| **OUTSIDE** | no precision defence exists; the disagreement is real. |
| **EXACT-INPUT** | the inputs are counts, so there is no interval and no defence. |

## D-61 does not survive as a defect, and it should be withdrawn

**Printed, at main §23.10.4 and Appendix E.2:** *"Do the perturbation bounds tighten at higher
order? Yes, **1,585-fold** — median 25.96 cm⁻¹ at order 1, 0.0164 at order 6."*

**Raised as** (docket 12, and candidate D-61): *"1,585-fold against the table's own
25.96 / 0.0164 = 1582.9268."*

**Measured.** The two medians are printed to four and three significant figures. The interval they
allow for the ratio is **[1577.81, 1588.07)**, and **1,585 lies inside it.**

**So there is no defect here.** The naive quotient 1582.93 is what you get by treating two rounded
medians as exact; the book's 1,585 is what you get from the unrounded ones, which it does not print.
The record itself half-saw this — *"the unrounded medians are not printed"* — and stopped short of
the conclusion. **The conclusion is that the figure is consistent with its own inputs and the
finding does not stand.**

**This is the class the test exists for**, and it is worth saying plainly: a figure computed from
rounded inputs cannot be checked by recomputing from those inputs. Any other recorded finding of the
same shape is owed the same test before it is called a defect.

## Three that do survive, and each is small

**E-035 · main §14.5, twice.** *"Λ is the closure of SEVEN of its cells — a compression of 139 to 1,
**exactly**."* Both inputs are exact counts: 976 cells and a seed of 7. **976 / 7 = 139.428571**, and
976 = 7 · 139 + 3. There is no interval and no defence. **The figure 139 is a fair rounding; the word
*exactly* is what is false**, and under M's test that makes it a prose error over a true object —
the object *seed(Λ₈) = 7, |Λ₈| = 976* is true and is proved elsewhere in this pass by
`method/proofs/lambda8.py`.

**F-033 · main L8206.** *"The test grew by a factor of **five and a half**."* From ten checkable
designations to fifty-four. Both are exact counts. **54 / 10 = 5.4**, not 5.5. No defence.

**E-110 · main §26.6, the Aitken table, row n = 20.** The *T*/3 column prints **91.4477** where
274.3433 / 3 = **91.447767**. The table's other three rows agree at the printed precision exactly:
1097.3730/3 = 365.7910, 68.5858/3 = 22.8619, 17.1465/3 = 5.7155. **So this is one row and one place,
a truncation inside a rounded table**, which is what the record calls it (15b-04). It is real and it
is the smallest kind of real.

## What is owed

1. **D-61 is withdrawn as a finding.** Docket 12 should carry the withdrawal, and the record's own
   note about the unrounded medians is the reason.
2. **E-035, F-033 and E-110 stand as recorded** and go to M with the rest of the figure class at the
   prose pass. E-035's repair is one word.
3. **The test should be run over the rest of the recorded figure class before any of it is called a
   defect.** One case in four did not survive it here. `precision.py` takes a case as data: its
   printed claim, its printed inputs, and the record entry that raised it.

**Nothing is repaired here.**
