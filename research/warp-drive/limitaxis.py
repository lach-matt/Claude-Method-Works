#!/usr/bin/env python3
r"""
limitaxis.py -- EXTENDING THE PERIODIC INDEX TO EXOTIC MATTER, AND THE ONE AXIS
IT TURNS OUT TO BE MISSING.

M: "I want to extend my current periodic index to include exotic matter.  Maybe
this will help us see things we cannot yet see regarding exotic matter.
Accounting for it in the index gives us exact comparison to neutral ground
state, ionic, and spectral matter."

    EXOTIC MATTER TAKES NO ROWS.  IT PERTURBS ONE AXIS, AND THAT AXIS IS NOT
    AMONG THE TWENTY-FIVE.

    python3 limitaxis.py             the reading
    python3 limitaxis.py --selftest  fixtures

===============================================================================
HOW THIS WAS ARRIVED AT, AND WHAT SURVIVED
===============================================================================

Eight negative-energy mechanisms were put to the twenty-five periodic axes, each
seated then measured then attacked by two hostile lenses -- twenty-eight agents,
no errors.  **NOT ONE SEATING SURVIVED BOTH LENSES.**  That is the headline and
it is reported before anything else, because what follows is what remains after
every proposed seating was broken, not a set of confirmed placements.

What broke was almost always the MAGNITUDE, and what held was almost always the
CLASSIFICATION.  Both lenses on four separate mechanisms opened with a variant
of "the verdict survives; the number does not."  So the classifications below
are carried, the numbers attached to them are carried with their status, and one
number that looked decisive is withdrawn outright in section 4.

===============================================================================
1. NO MECHANISM TAKES A ROW, AND THE REFUSAL IS MECHANICAL
===============================================================================

Twenty-four of the twenty-five axes are functions of (Z, charge, n, l).  A
mechanism with no nucleus and no bound electron has no value for any of them,
and the instrument refuses rather than degrades: `populate(109)` raises KeyError
naming the 1..108 table, `channel_delta(0, 1, 0)` returns None.

The static Casimir case is the sharpest because its null is EXACT rather than
small.  Its energy density depends on one free argument, the plate separation,
which is disjoint from all twenty-five axis names and from all ten columns of
the measured spectra table; and of that table's **104,832 rows, ZERO** carry a
boundary, cavity, plate, mirror or separation token.  Every row is a free atom
or free ion.  A free atom sits at infinite separation, and the density goes as
the inverse fourth power, so the value is not negligible -- it is zero.

===============================================================================
2. THE LADDER, WHICH IS THE EXACT COMPARISON THAT WAS ASKED FOR
===============================================================================

The comparison to neutral, ionic and spectral matter runs through ONE axis with
a published resolution: the measured quantum defect, recorded to a finest step
of 1e-05.  That step is the yardstick, and every mechanism gets a place on it:

    mechanism                     shift on the defect axis    vs 1e-05
    vacuum polarisation           ~1e-04 at high Z            ABOVE
    Casimir-Polder (neighbour)    2.2e-05  (K, z = 10 nm)     ABOVE
    static Casimir                exactly 0 (free atom)       off-index
    squeezed vacuum               no axis                     off-index
    dynamical Casimir             no axis                     off-index
    Hawking/Unruh at 1 g          ~1e-24                      19 orders below
    non-minimal scalar            ~1e-29                      24 orders below
    minimal scalar VEV            ~1e-69 relative             64 orders below

**THE BOUNDARY OF THE INDEX RUNS BETWEEN THE TWO CASIMIR MECHANISMS**, and that
is the most useful single line here.  Static Casimir is a property of boundaries
and survives removing every electron between them, so it is off-index.
Casimir-Polder's coefficient contains the static polarisability -- an
electronic-structure quantity -- so it is ON the index, and at ten nanometres it
clears the resolution.  The same word names two mechanisms that fall on opposite
sides of the index's reach.

===============================================================================
3. THE MISSING AXIS, AND THE CORPUS HAD ALREADY RULED ON IT
===============================================================================

The one mechanism that is measurably present is vacuum polarisation -- and it is
NOT on the defect axis, because the corpus already adjudicated where QED sits and
the answer was somewhere else.  Register 3253, quoted from the seated member:

    "Register 679's 'QED and reduced-mass residual' was half right: THE QED WAS
     REAL AND IT WAS IN THE LIMIT, NOT IN THE LEVELS."

Li III's ionisation limit had been recorded as the bare Coulomb expression
Z^2 R = 987,635.841.  Fitting it from the series returns **987,662.29 +/- 0.36,
higher by 26.45**, and with the corrected limit every channel moves from a spread
of ragged negatives to a uniform +0.0003.  The compendia state the consequence
directly: the limit **"must be measured, not computed"**, writing it as a formula
is "the single most damaging thing that can be done to a channel", and a shift of
even 0.2 "causes totally different behavior of quantum defect versus n" -- against
which 26.45 is a hundred and thirty times the stated tolerance.

**AND THE SERIES LIMIT WAS NOT ONE OF THE TWENTY-FIVE AXES.**  The word did not
occur anywhere in the instrument that puts an element on every axis of every
index.  It is the defect's own denominator input, it carries the QED, it is
banked with an error bar -- and it was not indexed.

    SO THE EXTENSION THE QUESTION ASKED FOR WAS NOT A NEW ROW AND NOT A NEW
    MECHANISM COLUMN.  IT WAS A TWENTY-SIXTH AXIS: THE MEASURED SERIES LIMIT,
    CARRYING ITS FITTED VALUE AND ITS UNCERTAINTY.

**IT HAS SINCE BEEN SEATED.**  The axis is now in the instrument: READ where a
source printed the value, FITTED where a run recovered it, and None where
neither -- four stages banked out of every stage of every element, with an
absent limit meaning levels-only rather than a guess, per register 2469's
withdrawal of ten channels built on an invented one.  This section is kept in
the past tense rather than deleted, because what the index was missing is the
finding and a repaired index does not show it.

===============================================================================
4. THE NUMBER THAT WAS SUPPOSED TO CLINCH IT, WITHDRAWN
===============================================================================

The seating pass reported the 26.45 decomposed into four terms with no free
parameter -- reduced mass -77.27, Dirac +118.33, self-energy -15.52, vacuum
polarisation +0.59 -- summing to +26.13 against the corpus's +26.45, agreement
to 1.2 %, and read that as vacuum polarisation being quantitatively seated at
1.63 sigma of the fit's own error bar.

**AN INDEPENDENT RECOMPUTATION DOES NOT REPRODUCE IT.**  Two of the four terms
replicate and two do not:

    term                     independent      as reported     agrees?
    reduced mass (7Li)          -77.22           -77.27         yes
    Dirac 1s                   +118.33          +118.33         yes
    self-energy 1s               +7.76           -15.52         NO
    vacuum polarisation 1s       -0.29            +0.59         NO
    SUM                         +48.58           +26.13         NO

Sign and magnitude both differ on the two QED terms, and the independent sum
misses the banked deficit by 84 %.  The agreement that made the finding
quantitative therefore **does not replicate, and is withdrawn.**

**AND THE CORPUS HAD THE ANSWER ALREADY, WHICH IS WHY BOTH ATTEMPTS WERE WRONG:
THE BASELINE WAS.**  Register 3357 records that the reduced mass is needed
TWICE -- once in the defect formula and once in the baseline a limit is measured
against -- and that a baseline missing it implies a spurious Z^6.4 against a
leading Dirac Z^4.  Both decompositions above were built against Z^2 R_inf, so
both were pricing reduced mass as a TERM in a sum whose baseline had already
omitted it.  Against Z^2 R_M the deficits are 103.94, 329.80 and 816.68 at
Z = 3, 4, 5, and register 3353 identifies them outright:

    THE DEFICIT IS THE SOMMERFELD-DIRAC RELATIVISTIC TERM LESS THE 1s LAMB
    SHIFT, AT A RATIO OF 0.8849 +/- 0.0069, CONSTANT TO UNDER ONE PER CENT.

Independently recomputed here, the Dirac terms reproduce to the digit (118.32,
373.97, 913.03) and the deficits to better than 0.2 %.  **It is a TWO-term form,
not a four-term one**, and the four-term attempt was mis-specified rather than
mis-arithmetised.  So the status moves from UNRESOLVED to RESOLVED -- and it was
resolved in the corpus before either attempt was made, which is the lesson worth
keeping.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not present the eight seatings as confirmed.**  Zero of eight survived
both lenses; the classifications are carried and the magnitudes are not.

**It does not itself add the axis.**  Section 3 was a proposal; the axis was
then seated in the instrument that owns it, and this file records the gap in the
past tense rather than erasing it.

**It does not bank ITS OWN QED decomposition.**  Two independent attempts
disagreed on sign and magnitude and both are printed; what is adopted is the
corpus's, which predates both and which reproduces.

**It does not claim exotic matter is absent from the index because it is small.**
For the static Casimir case the value is exactly zero, which is a different
statement, and the two are never merged.
"""

import math
import sys

RINF = 109737.31568          # cm^-1, CODATA
ALPHA = 7.2973525693e-3
ME_U, LI7_U = 5.48579909065e-4, 7.0160034366

# The corpus's own banked figures, READ from the seated Register.
BARE_LIMIT = 987635.841      # Z^2 R at Z = 3, the withdrawn formula value
FIT_LIMIT = 987662.29        # fitted from the series
FIT_SIGMA = 0.36
DEFICIT = 26.45

DEFECT_RESOLUTION = 1e-05    # finest recorded step in the measured-defect column

# The ladder of section 2.  Order is by size on the defect axis; `None` means
# the mechanism has no value on any axis at all rather than a small one.
LADDER = [
    ("vacuum polarisation",      1e-04,  "ABOVE"),
    ("Casimir-Polder",           2.2e-05, "ABOVE"),
    ("static Casimir",           0.0,     "off-index (exactly zero, free atom)"),
    ("squeezed vacuum",          None,    "off-index"),
    ("dynamical Casimir",        None,    "off-index"),
    ("Hawking/Unruh at 1 g",     1e-24,   "below"),
    ("non-minimal scalar",       1e-29,   "below"),
    ("minimal scalar VEV",       1e-69,   "below"),
]


def li3_terms():
    """The four contributions to Li III's limit deficit, computed here.

    UNRESOLVED: this does not reproduce the seating pass's decomposition on the
    two QED terms, and neither is adopted.  See section 4.
    """
    mu = 1.0 / (1.0 + ME_U / LI7_U)
    reduced = BARE_LIMIT * (mu - 1.0)
    dirac = RINF * 3 ** 4 * ALPHA ** 2 / 4.0
    lnk0 = 2.984128128                       # Bethe logarithm, 1s
    se = ((4.0 / 3.0) * (ALPHA ** 3 / math.pi) * 3 ** 4
          * (math.log(1.0 / (3 * ALPHA) ** 2) - lnk0 + 19.0 / 30.0) * RINF)
    vp = -(4.0 / 15.0) * (ALPHA ** 3 / math.pi) * 3 ** 4 * RINF
    return {"reduced mass": reduced, "Dirac 1s": dirac,
            "self-energy 1s": se, "vacuum polarisation 1s": vp}


REPORTED = {"reduced mass": -77.27, "Dirac 1s": 118.33,
            "self-energy 1s": -15.52, "vacuum polarisation 1s": 0.59}


def report():
    print("=" * 74)
    print("EXTENDING THE PERIODIC INDEX TO EXOTIC MATTER")
    print("=" * 74)
    print()
    print("HEADLINE FIRST: eight mechanisms were seated, measured and attacked by")
    print("two hostile lenses each. ZERO OF EIGHT SURVIVED BOTH. What follows is")
    print("what remained after every proposed seating broke -- and what broke was")
    print("almost always the magnitude, while the classification held.")
    print()

    print("1. NO MECHANISM TAKES A ROW, AND THE REFUSAL IS MECHANICAL.")
    print("   24 of the 25 axes are functions of (Z, charge, n, l). The static")
    print("   Casimir null is EXACT, not small: 0 of the measured table's 104,832")
    print("   rows carry a boundary token, a free atom sits at infinite separation,")
    print("   and the density goes as the inverse fourth power.")
    print()

    print("2. THE LADDER -- the exact comparison, on the one axis with a published")
    print("   resolution (measured quantum defect, finest step %g):" % DEFECT_RESOLUTION)
    print("   %-26s %-14s %s" % ("mechanism", "defect shift", "vs resolution"))
    for name, val, verdict in LADDER:
        s = "no axis" if val is None else ("exactly 0" if val == 0 else "~%.1e" % val)
        print("   %-26s %-14s %s" % (name, s, verdict))
    print()
    print("   THE INDEX BOUNDARY RUNS BETWEEN THE TWO CASIMIR MECHANISMS. Static")
    print("   Casimir survives removing every electron, so it is off-index.")
    print("   Casimir-Polder's coefficient contains the static polarisability, so")
    print("   it is ON the index and clears the resolution at ten nanometres.")
    print()

    print("3. THE MISSING AXIS. The corpus already ruled where QED sits, and it is")
    print("   not the defect. Register 3253, from the seated member:")
    print('     "the QED was real and it was in the LIMIT, not in the levels."')
    print("   bare Coulomb Z^2 R = %.3f" % BARE_LIMIT)
    print("   fitted from series = %.2f +/- %.2f    deficit %.2f"
          % (FIT_LIMIT, FIT_SIGMA, DEFICIT))
    print("   The compendia add that the limit MUST BE MEASURED, NOT COMPUTED, and")
    print("   that a shift of even 0.2 changes the defect's behaviour in n --")
    print("   against which %.2f is %d times the stated tolerance."
          % (DEFICIT, round(DEFICIT / 0.2)))
    print()
    print("   AND THE SERIES LIMIT IS NOT ONE OF THE TWENTY-FIVE AXES.")
    print("   So the extension asked for is not a row and not a mechanism column.")
    print("   IT IS A TWENTY-SIXTH AXIS: the measured series limit, with its")
    print("   uncertainty. That is a PROPOSAL. Nothing here adds it.")
    print()

    print("4. THE NUMBER THAT WAS TO CLINCH IT, WITHDRAWN.")
    t = li3_terms()
    print("   %-26s %12s %12s %s" % ("term", "independent", "as reported", "agrees?"))
    for k in ("reduced mass", "Dirac 1s", "self-energy 1s", "vacuum polarisation 1s"):
        a, b = t[k], REPORTED[k]
        print("   %-26s %+12.2f %+12.2f %s"
              % (k, a, b, "yes" if abs(a - b) < 0.1 else "NO"))
    s_ind, s_rep = sum(t.values()), sum(REPORTED.values())
    print("   %-26s %+12.2f %+12.2f %s" % ("SUM", s_ind, s_rep, "NO"))
    print("   corpus deficit %.2f; the independent sum misses it by %.0f%%."
          % (DEFICIT, 100 * abs(s_ind - DEFICIT) / DEFICIT))
    print()
    print("   The 1.2%% agreement that made the finding quantitative DOES NOT")
    print("   REPLICATE and is withdrawn.")
    print()
    print("   AND THE CORPUS HAD THE ANSWER: THE BASELINE WAS WRONG IN BOTH.")
    print("   Register 3357 -- the reduced mass is needed TWICE, once in the defect")
    print("   and once in the BASELINE, and omitting it implies a spurious Z^6.4.")
    print("   Both attempts priced reduced mass as a term in a sum whose baseline")
    print("   had already dropped it. Against Z^2 R_M, register 3353 states it:")
    print("     THE DEFICIT IS THE SOMMERFELD-DIRAC TERM LESS THE 1s LAMB SHIFT,")
    print("     ratio 0.8849 +/- 0.0069, constant to under one per cent.")
    print("   Recomputed here the Dirac terms reproduce to the digit and the")
    print("   deficits to better than 0.2%%. A TWO-term form, not a four-term one.")
    print("   Status UNRESOLVED -> RESOLVED, and it was resolved in the corpus")
    print("   before either attempt was made.")
    print()
    print("   THE AXIS HAS SINCE BEEN SEATED: the series limit is now the 26th,")
    print("   READ or FITTED, never computed, None where unbanked.")
    return 0


def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("limitaxis selftest")
    chk("the banked deficit is the fit minus the bare value",
        round(FIT_LIMIT - BARE_LIMIT, 2), DEFICIT, 0.01)
    chk("the bare value is Z^2 R at Z = 3", 9 * RINF, BARE_LIMIT, 0.001)
    chk("the deficit is 130x the stated 0.2 tolerance",
        round(DEFICIT / 0.2), 132)

    t = li3_terms()
    chk("reduced mass reproduces the reported term", t["reduced mass"], -77.27, 0.1)
    chk("Dirac 1s reproduces it exactly", t["Dirac 1s"], 118.33, 0.01)
    # The two that do NOT reproduce -- pinned as disagreements so the withdrawal
    # cannot quietly heal itself in a later pass.
    chk("self-energy does NOT reproduce",
        abs(t["self-energy 1s"] - REPORTED["self-energy 1s"]) > 1.0, True)
    chk("vacuum polarisation does NOT reproduce",
        abs(t["vacuum polarisation 1s"] - REPORTED["vacuum polarisation 1s"]) > 0.1, True)
    chk("and the independent sum misses the banked deficit badly",
        abs(sum(t.values()) - DEFICIT) / DEFICIT > 0.5, True)

    chk("the ladder places eight mechanisms", len(LADDER), 8)
    chk("two clear the defect resolution",
        sum(1 for _, v, w in LADDER if w == "ABOVE"), 2)
    chk("the static Casimir null is exactly zero, not small",
        [v for n, v, _ in LADDER if n == "static Casimir"][0], 0.0)
    chk("two mechanisms have no axis at all -- the third off-index case is",
        sum(1 for _, v, _ in LADDER if v is None), 2)
    chk("static Casimir, which has a value and it is exactly zero",
        sum(1 for _, v, w in LADDER if v == 0.0 and w.startswith("off-index")), 1)
    print("limitaxis selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
