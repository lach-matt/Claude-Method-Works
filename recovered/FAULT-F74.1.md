# F74.1 — THE AUDIT INSTRUMENT'S CAN-FAIL GATE COULD NOT FAIL. Session 74.
**SEVERITY: INSTRUMENT. TOUCHES NO SCORED ROW.** No result from goaudit.py v1 or v2 was
reported, carried, or entered anywhere. The fault was caught before any row was used.

**WHAT HAPPENED.** goaudit.py (v1) classified ground_occ call sites by keyword. Its selftest
passed on four cases I wrote FROM MY OWN REGEXES, so the gate could not fail for the reason it
names. Tested against a site established INDEPENDENTLY by F73.3 — ci2b.py L38,
`A = {(n,l):q for n,l,q in ground_occ(Z)}`, known CONSTRUCT — v1 returned SCORE.
**IT WAS WRONG IN THE DANGEROUS DIRECTION: it under-reported construct-side exposure.**
Cause: the regex read the comprehension's `for ... in` as a comparison operator.

**THIS IS R 1671's FAULT COMMITTED AGAIN.** An instrument that narrows its own input reports
on what it admitted, not on what it was asked about. R 1671 recorded it for C6 of the handoff
certificate; it recurred here one session later in a different instrument.

**v2 FAILED DIFFERENTLY AND THE FAILURE WAS INFORMATIVE.** v2 asked "does the value reach a
SOLVER". In ci2b.py the observed configuration A feeds SLATER-CONDON INTEGRALS and never an
SCF, so v2 also missed it. **REACHING A SOLVER IS THE WRONG CRITERION FOR CIRCULARITY.**

**THE REPAIR (goaudit3.py).** The semantic question is replaced by a decidable one: is the
returned value used for anything OTHER than a direct comparison? Wrapped, bound, iterated or
indexed -> CONSTRUCT; compared only -> SCORE. **THE BIAS IS DELIBERATE AND DECLARED: this rule
OVER-reports CONSTRUCT and can never under-report it.** The count is a CEILING on construct-side
exposure, not a measurement of it. The battery is built from F73.3's two established sites plus
a negative control proving SCORE is reachable, so CONSTRUCT is not vacuous.

**STANDING, PROPOSED TO M:** a can-fail battery whose cases are written from the instrument's
own patterns is not a can-fail battery. Ground truth must come from OUTSIDE the instrument.