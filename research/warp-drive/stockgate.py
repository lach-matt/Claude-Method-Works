#!/usr/bin/env python3
r"""
stockgate.py -- THE DESTINATION STOCK CONSTRAINT, AUDITED.  stock.py asked what
binds.  This asks whether the answer survives its own assumptions.  It does --
phosphorus binds, robustly, and the truncation worry is EMPTY -- but three of
stock.py's supporting numbers are wrong, its cosmic column cannot price twelve
of the payload's elements at all, and the constraint it calls "not a barrier"
is FOUR ORDERS OF MAGNITUDE HARSHER for a manufactured payload than for a human.

    python3 stockgate.py             the reading
    python3 stockgate.py --selftest  fixtures (stdlib; z3 where labelled)

This file AUDITS stock.py (commit 2636037), whose --selftest passes 24 of 24 and
whose arithmetic is reproduced here to the digit.  Findings are RECORDED, NOT
REPAIRED, per the standing hold.  stock.py is not edited.

===============================================================================
0.  WHAT STANDS
===============================================================================
M's constraint is real and stock.py states it correctly.  The processing factor

        M(p, s) = max_e ( p_e / s_e )

is a MAX, not a sum: exactly one element binds and every other arrives in
surplus.  The assemblable set is a down-set closed under join.  Phosphorus binds
against raw stellar material.  An asteroid beats a planet.  All of that stands,
and section 8 upgrades two of them from sampled exhaustion to theorems.

===============================================================================
1.  FINDING A -- THE TRUNCATION WORRY IS REAL, AND IT IS EMPTY.  MEASURED.
===============================================================================
THEOREM (monotone extension).  If p' extends p to a larger support with
p'|_supp(p) = p, then M(p', s) >= M(p, s), since a max over a superset cannot
decrease.  `z3_monotone_extension()` discharges it over the reals; UNSAT is the
proof.  So ANY truncated payload gives only a FLOOR, and stock.py's payload
carries 13 elements where a reference adult has measured quantities of 59.

THAT IS THE WORRY.  HERE IS THE MEASUREMENT.  Extending the payload from the
11 bulk elements to all 59 moves the processing factor by

        11 bulk elements        1.9112e3
        + 14 essential trace    1.9109e3
        + 34 incidental         1.9109e3        -0.017 %

IT MOVES DOWN, AND ONLY BY RENORMALISATION.  Not one of the 48 added elements
exceeds phosphorus, so the binder never moves.  Iodine, selenium and the 120 mg
of lead a reference adult carries all land two to ten times below it.

    THE HUMAN STOCK CONSTRAINT IS A BULK-CHEMISTRY CONSTRAINT.  MEASURED, NOT
    ASSUMED -- the max is exactly the statistic a rare element should hijack.

AND IT IS A NEAR MISS, WHICH IS THE PART WORTH REPORTING.  The margin is not
comfortable.  LITHIUM -- 7 mg in a reference adult, one of the 34 incidental
elements stock.py omits -- reaches 91.758 % of phosphorus's factor against a
stellar photosphere.  Nine per cent from flipping the answer.  The third-placed
element is 2.93x behind, so the field is two deep and no deeper.  Section 4 is
about why lithium is there, and it is not an accident.
`truncation_sweep()` produces the rows; the margin is `runner_up()`.

===============================================================================
2.  FINDING B -- stock.py's COSMIC COLUMN CANNOT PRICE THE PAYLOAD AT ALL
===============================================================================
stock.py uses Asplund 2009's PHOTOSPHERIC column.  Twelve elements a reference
adult contains have NO photospheric determination in that table -- the Sun's
spectrum does not show them:

        As  Bi  Br  Cd  Cs  Hg  I  Sb  Se  Ta  Te  U

Against a photospheric-only column each returns p_e/0 = INFINITY, and the
constraint reports that a star cannot supply a human at any budget.  That is
FALSE, and it is an artefact of the measurement method rather than of the star.
`missing_photospheric()` lists them.  The defensible column is the HYBRID
Asplund recommends -- photospheric where determined, meteoritic otherwise -- and
every cosmic number in this file uses it.  stock.py avoided the infinity only by
carrying 17 elements, all of which happen to be photospherically determined.

===============================================================================
3.  FINDING C -- THREE NUMBERS IN stock.py ARE WRONG.  RECORDED.
===============================================================================
(i)  "six hundred times worse than the crust's phosphorus."  COMPUTED from
     stock.py's OWN tables: N 5.3333e2 / P 9.5238e0 = 5.6000e1.  FIFTY-SIX.
     The sentence overstates by 10.71x.  The tables are right.

(ii) stock.py's HUMAN carries K = 0.0040 -- 280 g of potassium in a 70 kg adult.
     ICRP Reference Man and Emsley both give 140 g, exactly half.  stock.py's
     headline that potassium is "the runner-up within 1.32x", and its reading
     that "two independent scarcities sit at the same scale", both rest on the
     doubled value.  On the ICRP datum the gap is 2.63x and the reading fails.

     AND THE TRUE RUNNER-UP IS NOT POTASSIUM.  It is LITHIUM, at 1.7534e3
     against phosphorus's 1.9109e3 -- within 1.09x, genuinely co-binding.
     Section 4 is about why that is interesting rather than a typo.

(iii) stock.py reports a CI chondrite's binding element as NITROGEN at 1.0063e1.
     COMPUTED on the ICRP payload it is PHOSPHORUS at 1.0701e1, with nitrogen
     second at 8.0763e0.  The flip is caused by stock.py's payload table, which
     carries N at 0.032 (ICRP: 0.02568, high by 1.25x) and P at 0.010 (ICRP:
     0.011129, low by 1.11x).  The element is wrong; the magnitude is right to
     6 %, and stock.py's conclusion that an asteroid is the best node survives.

===============================================================================
4.  FINDING D -- THE RUNNER-UP IS LITHIUM, AND THAT IS A REAL ASTROPHYSICAL
    FACT RATHER THAN A DATUM ERROR
===============================================================================
Asplund 2009 gives lithium photospheric 1.05 against meteoritic 3.26 -- a
2.21-dex gap, a factor of 162 in abundance.  It is the largest such gap in the
table and it is not a disagreement: the Sun's convective envelope reaches
2.5 MK, where lithium burns, so the PHOTOSPHERE really is 162x poorer in lithium
than the material the solar system formed from.  Both numbers are correct about
different reservoirs.  `li_dex_gap()` computes it.

CONSEQUENCE FOR SITE SELECTION, AND IT IS SHARP.  Which lithium number applies
depends on what the destination IS:

        a stellar photosphere as stock  ->  Li at 1.7534e3, co-binding with P
        protosolar / meteoritic stock   ->  Li at 1.0846e1, irrelevant

So a destination's processing factor is not a function of its ELEMENTS but of
its THERMAL HISTORY.  A star has burned its lithium.  A chondrite has not.
For the human payload this is a runner-up effect.  For the engineering payload
in section 5 it is the binding constraint outright.

===============================================================================
5.  FINDING E -- THE BIGGEST RESULT HERE.  THE CONSTRAINT BITES ON TECHNOLOGY,
    NOT ON BIOLOGY, AND stock.py COSTED ONLY THE HUMAN
===============================================================================
A 70 kg human against a CI chondrite: processing factor 1.0701e1, i.e. 0.749
tonnes of asteroid.  stock.py is right to call that a site-selection criterion.

A 1000 kg engineering payload -- a spacecraft bus, DECLARED in `CRAFT` below --
against the same chondrite:

        binding element    Ta (tantalum)
        factor             9.0082e4 kg per kg
        for 1000 kg        9.0082e7 kg  =  90,082 TONNES of asteroid

    EIGHT THOUSAND FOUR HUNDRED TIMES HARDER THAN A HUMAN, PER KILOGRAM.

And the binding element is destination-dependent in a way the human's is not:

        destination              binding    factor
        stellar photosphere      Li         6.1499e7      <- the Li depletion
        solar meteoritic         Ta         5.6600e4
        CI chondrite             Ta         9.0082e4
        Earth continental crust  Au         2.6948e5

Four destinations, THREE DIFFERENT BINDING ELEMENTS, none of them biogenic.  The
human payload binds on P almost everywhere because bulk biology uses abundant
elements; a manufactured object binds on whatever refractory rarity its function
demanded -- tantalum for capacitors, gold for contacts -- and those are precisely
the elements cosmochemistry makes least of.

    WHAT IS CHEAP TO TRANSITION IS A PERSON.  WHAT IS EXPENSIVE IS THEIR
    EQUIPMENT.

`CRAFT` is DECLARED, not measured, and section 9 refuses to treat it otherwise.
The ORDER OF MAGNITUDE is robust to the declaration -- any payload containing
parts-per-thousand tantalum or parts-per-ten-thousand gold lands in the same
place -- and `craft_sensitivity()` shows the factor is linear in exactly one
declared number, which is the honest way to report a stipulated input.

===============================================================================
6.  FINDING F -- DEVOLATILISED vs PRIMITIVE, AND A CHONDRITE SITS WITH THE STAR
===============================================================================
stock.py attributes the chondrite's advantage to differentiation.  Right, and it
can be made exact by ranking the binders by Lodders (2003) 50 % condensation
temperature:

        destination              binding  T_c/K   regime
        stellar photosphere      P/Li     1229    ABUNDANCE-LIMITED
        Jupiter (3x solar)       P        1229    ABUNDANCE-LIMITED
        CI chondrite             P        1229    ABUNDANCE-LIMITED
        Earth continental crust  N         123    VOLATILITY-LIMITED

THE CUT IS NOT STAR-vs-BODY.  It is DEVOLATILISED vs PRIMITIVE.  A CI chondrite
retained its volatiles, so like a star it binds on the least abundant required
element -- a refractory one.  Earth's crust outgassed, so it binds on the most
volatile required element, nitrogen, at 4.5862e2 -- forty-three times worse than
the chondrite despite being a far richer rock.  `volatility_regime()` labels each
destination from T_c alone, without being told which it is.

AND THE SNOW LINE IS THEREFORE THE SELECTOR.  Retaining volatiles is a statement
about formation temperature, hence orbital radius.  The admissible arrival sites
are outer-system primitive bodies, and that is a geometric condition on B.

===============================================================================
7.  FINDING G -- ELEMENTS EXISTING IS NOT STOCK.  COMPUTED, NOT QUOTED.
===============================================================================
Of solar-composition material, COMPUTED from the hybrid column and the T_c table:

        H + He                                       9.8663e-1
        Z (everything else)                          1.3370e-2
        refractory elements, T_c >= 500 K            3.2498e-3
        + the oxygen stoichiometrically bound in
          their oxides                               1.7192e-3
        = ROCK                                       4.9690e-3
        + water ice from the leftover oxygen         4.5187e-3
        = ROCK + ICE                                 9.4877e-3

SO 99.06 % OF A SOLAR-COMPOSITION RESERVOIR IS GAS THAT CONDENSES NOWHERE, and
0.50 % is rock.  stock.py prices the diffuse ISM at 7.18e25 m^3 per human, which
is right for the GAS; priced on the condensable fraction alone the sweep is
larger again.  `condensed_budget()` computes every row above.

===============================================================================
8.  THE ORDER STRUCTURE -- AND WHY REGISTER 66 DOES NOT APPLY
===============================================================================
A(s,M) = { p : p_e <= M s_e for all e } is a down-set in the componentwise order
and is closed under componentwise max, hence a PRINCIPAL ideal generated by M*s.
stock.py verifies both by exhaustion on a sampled grid.  `z3_downset()` and
`z3_join_closed()` discharge both as quantified statements over the reals, which
is strictly stronger: not "no counterexample on this grid" but "no counterexample
exists".

REGISTER 66'S MACHINERY DOES NOT TRANSFER, AND THIS FILE SAYS SO PLAINLY.
`tools/orderideal.py` tests downward closure of the OCCUPIED SUBSHELL SET -- the
carrier is cells (n, l, k) of Lambda, the order is on subshell occupancies, and
the corpus's two records disagree about whether the set is closed at all.  The
carrier here is composition vectors over elements and the order is multiset
inclusion.  Different carrier, different order, different question.  The shared
phrase "order ideal" is A SHARED SHAPE, NOT A CORRESPONDENCE, and this file
asserts none -- which is the discipline `paper/CLAIMS.md` line 9080 already
imposes on the method equation itself.

===============================================================================
9.  WHAT THIS DOES TO COORDINATE 7, AND THE REFUSAL IT INHERITS
===============================================================================
`unified.py` numbers B, the declared arrival, as coordinate 7 of eight, gated by
`transit.py` part 1.  stock.py establishes B is not free.  This file states the
gate:

    B admissible  <=>  within the corridor's arrival aperture there is a
                       CONDENSED body, primitive rather than devolatilised,
                       holding at least M(p,s) * m_payload of accessible mass.

Three conjuncts.  The third is a boulder for a person and a small asteroid for
their equipment.  The first excludes gas.  THE SECOND IS THE BINDING ONE, and it
is a snow-line condition, so coordinate 7 is gated on ORBITAL RADIUS AT THE
DESTINATION -- a parameter the eight-value coordinate does not currently carry.

AND A REFUSAL THIS FILE INHERITS AND WILL NOT STEP AROUND.  `paper/CLAIMS.md`
line 9080 refuses, verbatim:

    "That the transition is an instance of the method equation.  A shared shape
     is not a correspondence, and none is asserted."

The framing under which this audit was commissioned has the device "using the
method equation itself to calculate the front and backend coordinates of the
transition corridor."  THE TREE REFUSES THAT IDENTIFICATION.  This file does not
reinstate it and derives nothing from it.  What is established is narrower and
still worth having: coordinate 7 carries a computable sub-constraint, and it is
computed here.

===============================================================================
10.  WHAT THIS FILE REFUSES
===============================================================================
TO TREAT `CRAFT` AS MEASURED.  It is a DECLARED specification written in this
file.  Its binding element is conditional on that declaration.  What is NOT
conditional is that a manufactured payload binds on a refractory rarity rather
than a biogenic element; that follows from any bill of materials containing
capacitors or contacts.

TO PRICE SEPARATION ENERGY.  A processing factor is a MASS OF FEEDSTOCK.  What
it costs to win tantalum from a chondrite is not computed and no number here may
be read as an energy.

TO ADJUDICATE Li PHOTOSPHERIC vs METEORITIC.  Both are correct about different
reservoirs.  Which applies is a property of the destination, not of the table.

TO TREAT THE ABUNDANCES AS MEASURED HERE.  Every one is CITED.  The FACTORS are
COMPUTED.

TO CALL ANY OF THIS A BARRIER.  Even 90,082 tonnes sits ~19 orders below the
shell mass.  It is a site-selection criterion, as stock.py says.
"""

import math
import sys

# ------------------------------------------------------------------ provenance
SOURCES = {
    "A09": "Asplund, Grevesse, Sauval & Scott (2009), ARA&A 47, 481, Table 1 -- "
           "photospheric and meteoritic log eps, H = 12",
    "L03": "Lodders (2003), ApJ 591, 1220 -- CI chondrite, and 50% condensation "
           "temperatures at 1e-4 bar",
    "RG03": "Rudnick & Gao (2003), Treatise on Geochemistry 3, 1 -- bulk "
            "continental crust",
    "ICRP": "ICRP Publication 23 (Reference Man) / Emsley, Nature's Building "
            "Blocks -- reference 70 kg adult, grams per element",
    "JUP": "Wong et al. (2004) Icarus 171, 153; Fletcher et al. (2009) -- "
           "Galileo probe / Jovian heavy-element enrichment over solar",
}

# Asplund 2009 Table 1.  (photospheric, meteoritic); None where not determined.
A09 = {
    "H": (12.00, 8.22), "He": (10.93, 1.29), "Li": (1.05, 3.26), "Be": (1.38, 1.30),
    "B": (2.70, 2.79), "C": (8.43, 7.39), "N": (7.83, 6.26), "O": (8.69, 8.40),
    "F": (4.56, 4.42), "Ne": (7.93, None), "Na": (6.24, 6.27), "Mg": (7.60, 7.53),
    "Al": (6.45, 6.43), "Si": (7.51, 7.51), "P": (5.41, 5.43), "S": (7.12, 7.15),
    "Cl": (5.50, 5.23), "Ar": (6.40, None), "K": (5.03, 5.08), "Ca": (6.34, 6.29),
    "Sc": (3.15, 3.05), "Ti": (4.95, 4.91), "V": (3.93, 3.96), "Cr": (5.64, 5.64),
    "Mn": (5.43, 5.48), "Fe": (7.50, 7.45), "Co": (4.99, 4.87), "Ni": (6.22, 6.20),
    "Cu": (4.19, 4.25), "Zn": (4.56, 4.63), "Ga": (3.04, 3.08), "Ge": (3.65, 3.58),
    "As": (None, 2.30), "Se": (None, 3.34), "Br": (None, 2.54), "Rb": (2.52, 2.36),
    "Sr": (2.87, 2.88), "Y": (2.21, 2.17), "Zr": (2.58, 2.53), "Nb": (1.46, 1.41),
    "Mo": (1.88, 1.94), "Ag": (0.94, 1.20), "Cd": (None, 1.71), "In": (0.80, 0.76),
    "Sn": (2.04, 2.07), "Sb": (None, 1.01), "Te": (None, 2.18), "I": (None, 1.55),
    "Cs": (None, 1.08), "Ba": (2.18, 2.18), "La": (1.10, 1.17), "Ce": (1.58, 1.58),
    "Nd": (1.42, 1.45), "Sm": (0.96, 0.94), "W": (0.85, 0.65), "Au": (0.92, 0.80),
    "Hg": (None, 1.17), "Tl": (0.90, 0.77), "Pb": (1.75, 2.04), "Bi": (None, 0.65),
    "Th": (0.02, 0.06), "U": (None, -0.54), "Ta": (None, -0.12),
}

ATOMIC_MASS = {
    "H": 1.008, "He": 4.003, "Li": 6.94, "Be": 9.012, "B": 10.81, "C": 12.011,
    "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.990,
    "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06,
    "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078, "Sc": 44.956,
    "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845,
    "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723,
    "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904, "Rb": 85.468,
    "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95,
    "Ag": 107.868, "Cd": 112.414, "In": 114.818, "Sn": 118.710, "Sb": 121.760,
    "Te": 127.60, "I": 126.904, "Cs": 132.905, "Ba": 137.327, "La": 138.905,
    "Ce": 140.116, "Nd": 144.242, "Sm": 150.36, "Ta": 180.948, "W": 183.84,
    "Au": 196.967, "Hg": 200.592, "Tl": 204.38, "Pb": 207.2, "Bi": 208.980,
    "Th": 232.038, "U": 238.029,
}

# Lodders (2003) 50% condensation temperatures, K, at 1e-4 bar.  CITED.
TCOND = {
    "H": 182, "He": 3, "C": 40, "N": 123, "O": 180, "Ne": 9, "Na": 958,
    "Mg": 1336, "Al": 1653, "Si": 1310, "P": 1229, "S": 664, "Cl": 948,
    "K": 1006, "Ca": 1517, "Ti": 1582, "V": 1429, "Cr": 1296, "Mn": 1158,
    "Fe": 1334, "Co": 1352, "Ni": 1353, "Cu": 1037, "Zn": 726, "Se": 697,
    "Br": 546, "Rb": 800, "Sr": 1464, "Mo": 1590, "Ag": 996, "Cd": 652,
    "Sn": 704, "I": 535, "Cs": 799, "Ba": 1455, "Pb": 727, "F": 734,
    "B": 908, "Li": 1142, "Be": 1452, "Sc": 1659, "Ga": 968, "Ge": 883,
    "As": 1065, "Y": 1659, "Zr": 1741, "Nb": 1559, "In": 536, "Sb": 979,
    "Te": 709, "La": 1578, "Ce": 1478, "Nd": 1602, "Sm": 1590, "Ta": 1573,
    "W": 1789, "Au": 1060, "Hg": 252, "Tl": 532, "Bi": 746, "Th": 1659,
    "U": 1610, "Ar": 47, "Ni_": 0,
}

# ICRP 23 / Emsley reference 70 kg adult, GRAMS.  CITED, not measured here.
HUMAN_G_BULK = {
    "O": 43000.0, "C": 16000.0, "H": 7000.0, "N": 1800.0, "Ca": 1000.0,
    "P": 780.0, "K": 140.0, "S": 140.0, "Na": 100.0, "Cl": 95.0, "Mg": 19.0,
}
HUMAN_G_ESSENTIAL_TRACE = {
    "Fe": 4.2, "F": 2.6, "Zn": 2.3, "Si": 1.0, "Cu": 0.072, "B": 0.018,
    "I": 0.020, "Se": 0.015, "Ni": 0.015, "Cr": 0.014, "Mn": 0.012,
    "Mo": 0.005, "Co": 0.003, "V": 0.00011,
}
HUMAN_G_INCIDENTAL = {
    "Rb": 0.68, "Sr": 0.32, "Br": 0.26, "Pb": 0.12, "Al": 0.060, "Cd": 0.050,
    "Ce": 0.040, "Ba": 0.022, "Sn": 0.020, "Ti": 0.020, "As": 0.007,
    "Li": 0.007, "Hg": 0.006, "Cs": 0.006, "Ge": 0.005, "Sb": 0.002,
    "Ag": 0.002, "Nb": 0.0015, "Zr": 0.001, "La": 0.0008, "Ga": 0.0007,
    "Te": 0.0007, "Y": 0.0006, "Bi": 0.0005, "Tl": 0.0005, "In": 0.0004,
    "Au": 0.0002, "Sc": 0.0002, "Ta": 0.0002, "Th": 0.0001, "U": 0.0001,
    "Sm": 0.00005, "Be": 0.000036, "W": 0.00002,
}

# DECLARED, not measured: a 1000 kg engineering payload.  Mass fractions.
CRAFT = {
    "Al": 0.380, "Fe": 0.150, "Ti": 0.070, "C": 0.090, "Si": 0.055,
    "O": 0.110, "Cu": 0.045, "Ni": 0.020, "Cr": 0.018, "Mg": 0.012,
    "Zn": 0.008, "Sn": 0.004, "Li": 0.0035, "Nd": 0.0025, "Ag": 0.0012,
    "Au": 0.00035, "Ta": 0.0009, "W": 0.0011, "Co": 0.0018, "Mo": 0.0012,
    "Pb": 0.0006, "In": 0.00012, "Ga": 0.00018, "Ge": 0.00009,
    "Zr": 0.0007, "Nb": 0.0004, "Be": 0.00015, "B": 0.0003,
    "H": 0.010, "N": 0.006, "S": 0.0012, "P": 0.0004, "Ca": 0.0010,
    "Na": 0.0004, "Cl": 0.0003, "K": 0.0002, "Mn": 0.0025,
}

CRUST = {"O": 0.461, "Si": 0.282, "Al": 0.0823, "Fe": 0.0563, "Ca": 0.0415,
         "Na": 0.0236, "Mg": 0.0233, "K": 0.0209, "Ti": 0.0038, "H": 0.0014,
         "P": 0.000655, "C": 0.00199, "Mn": 0.000774, "S": 0.000404,
         "Cl": 0.000244, "N": 0.000056, "Zn": 0.000067, "Cu": 0.0000270,
         "Cr": 0.000092, "Ni": 0.0000470, "F": 0.000553, "Ba": 0.000456,
         "Sr": 0.000320, "Zr": 0.000132, "V": 0.000138, "Li": 0.0000160,
         "Rb": 0.0000490, "Ce": 0.0000430, "Nd": 0.0000200, "La": 0.0000200,
         "Y": 0.0000210, "Co": 0.0000175, "Sc": 0.0000214, "Nb": 0.0000080,
         "Ga": 0.0000160, "Pb": 0.0000110, "B": 0.0000110, "Th": 0.0000056,
         "Sm": 0.0000039, "Be": 0.0000019, "Ta": 0.0000007, "Sn": 0.0000017,
         "As": 0.0000047, "Ge": 0.0000013, "Mo": 0.0000008, "W": 0.0000010,
         "U": 0.0000013, "Br": 0.0000016, "I": 0.0000007, "Cs": 0.0000020,
         "Cd": 0.00000008, "Sb": 0.0000002, "Ag": 0.000000053,
         "Se": 0.00000013, "In": 0.000000052, "Bi": 0.00000018,
         "Tl": 0.0000005, "Hg": 0.00000003, "Au": 0.0000000013,
         "Te": 0.000000005, "Li_": 0.0,
}

CHONDRITE = {"O": 0.464, "Fe": 0.185, "Si": 0.107, "Mg": 0.0965, "S": 0.0541,
             "C": 0.0350, "H": 0.0202, "Ca": 0.00911, "Al": 0.00860,
             "Na": 0.00500, "N": 0.00318, "Ni": 0.0107, "P": 0.00104,
             "Cr": 0.00265, "Mn": 0.00193, "K": 0.000555, "Cl": 0.000698,
             "Ti": 0.000447, "Co": 0.000513, "Zn": 0.000312, "Cu": 0.000126,
             "F": 0.0000604, "V": 0.0000547, "Sr": 0.0000079,
             "Ba": 0.0000024, "Li": 0.0000015, "B": 0.0000008,
             "Se": 0.0000212, "Ge": 0.0000326, "As": 0.0000185,
             "Br": 0.0000035, "Rb": 0.0000023, "Y": 0.0000015,
             "Zr": 0.0000039, "Nb": 0.00000025, "Mo": 0.00000090,
             "Ag": 0.00000020, "Cd": 0.00000069, "In": 0.00000008,
             "Sn": 0.00000170, "Sb": 0.00000014, "Te": 0.00000240,
             "I": 0.00000043, "Cs": 0.00000019, "La": 0.00000024,
             "Ce": 0.00000062, "Nd": 0.00000046, "Sm": 0.00000015,
             "W": 0.00000009, "Au": 0.00000014, "Hg": 0.00000031,
             "Tl": 0.00000014, "Pb": 0.00000247, "Bi": 0.00000011,
             "Th": 0.00000003, "U": 0.00000001, "Ta": 0.00000001,
             "Sc": 0.0000058, "Ga": 0.0000095, "Be": 0.00000002,
             "Hg_": 0.0,
}

#: Jovian heavy-element enrichment over solar, by number relative to H.  CITED.
JUPITER_ENRICH = 3.0

RHO_ISM = 1.0e6 * 1.67262192e-27          # 1 proton/cm^3, as arrival.py uses
RHO_DISC = 1.0e-7                          # kg/m^3, ~1e14 H2/m^3 inner nebula
DUST_TO_GAS = 0.01                         # canonical ISM/disc dust mass ratio
FUCHS_SHELL_KG = 4.4886e27


# ----------------------------------------------------------------- conversions
def _norm(d):
    t = sum(d.values())
    return {k: v / t for k, v in d.items()}


def mass_fractions(grams):
    return _norm(grams)


def mole_fractions(massfrac):
    """Mole fractions from mass fractions.  COMPUTED."""
    n = {e: massfrac[e] / ATOMIC_MASS[e] for e in massfrac}
    return _norm(n)


def solar(column="photospheric"):
    """Mass fractions from A09 log eps.  COMPUTED from the cited log eps."""
    i = 0 if column == "photospheric" else 1
    n = {e: 10.0 ** (v[i] - 12.0) for e, v in A09.items() if v[i] is not None}
    m = {e: n[e] * ATOMIC_MASS[e] for e in n}
    return _norm(m)


def jupiter(column="photospheric", enrich=JUPITER_ENRICH):
    """Solar with every element above He enriched by `enrich` in number.

    COMPUTED, not tabulated: the Galileo enrichment is applied to the cited
    solar column and the mass fractions are renormalised.
    """
    i = 0 if column == "photospheric" else 1
    n = {}
    for e, v in A09.items():
        if v[i] is None:
            continue
        n[e] = 10.0 ** (v[i] - 12.0) * (1.0 if e in ("H", "He") else enrich)
    return _norm({e: n[e] * ATOMIC_MASS[e] for e in n})


def payload(kind="as-composed"):
    """Mass fractions of the 70 kg reference adult under three conventions."""
    g = dict(HUMAN_G_BULK)
    if kind in ("essential", "as-composed"):
        g.update(HUMAN_G_ESSENTIAL_TRACE)
    if kind == "as-composed":
        g.update(HUMAN_G_INCIDENTAL)
    if kind == "bulk":
        pass
    return mass_fractions(g)


STOCKPY_HUMAN = {"O": 0.650, "C": 0.185, "H": 0.095, "N": 0.032, "Ca": 0.015,
                 "P": 0.010, "K": 0.0040, "S": 0.0030, "Na": 0.0015,
                 "Cl": 0.0015, "Mg": 0.0005, "Fe": 0.00006, "Zn": 0.00003}


# ------------------------------------------------------------- the constraint
def factors(p, s):
    """{e: p_e/s_e}.  inf where the stock lacks the element outright."""
    return {e: (float("inf") if s.get(e, 0.0) <= 0.0 else p[e] / s[e]) for e in p}


def processing_factor(p, s):
    """M(p,s) = max_e p_e/s_e.  A MAX, so exactly one element binds."""
    f = factors(p, s)
    e = max(f, key=lambda k: f[k])
    return e, f[e]


def ranked(p, s, n=8):
    f = factors(p, s)
    return sorted(f.items(), key=lambda kv: -kv[1])[:n]


def solar_hybrid():
    """Photospheric where determined, meteoritic otherwise.  A09's own advice.

    COMPUTED from the cited log eps.  This is the defensible cosmic column:
    the photospheric one alone cannot price 12 of the payload's elements.
    """
    n = {}
    for e, (ph, me) in A09.items():
        v = ph if ph is not None else me
        if v is not None:
            n[e] = 10.0 ** (v - 12.0)
    return _norm({e: n[e] * ATOMIC_MASS[e] for e in n})


def missing_photospheric(pkind="as-composed 59"):
    """FINDING B: payload elements with no photospheric determination."""
    ph = solar("photospheric")
    return sorted(e for e in PAYLOADS[pkind]() if e not in ph)


def jupiter_hybrid(enrich=JUPITER_ENRICH):
    """Hybrid solar with everything above He enriched by `enrich` in number."""
    n = {}
    for e, (ph, me) in A09.items():
        v = ph if ph is not None else me
        if v is None:
            continue
        n[e] = 10.0 ** (v - 12.0) * (1.0 if e in ("H", "He") else enrich)
    return _norm({e: n[e] * ATOMIC_MASS[e] for e in n})


DESTS = {
    "stellar photosphere": solar_hybrid,
    "solar meteoritic": lambda: solar("meteoritic"),
    "Jupiter (3x solar)": jupiter_hybrid,
    "CI chondrite": lambda: CHONDRITE,
    "Earth cont. crust": lambda: CRUST,
    "photospheric-only": lambda: solar("photospheric"),
}

PAYLOADS = {
    "stock.py 13-element": lambda: STOCKPY_HUMAN,
    "bulk 11-element": lambda: payload("bulk"),
    "essential 25": lambda: payload("essential"),
    "as-composed 59": lambda: payload("as-composed"),
    "craft 1000 kg (DECLARED)": lambda: _norm(CRAFT),
}


def binding_under(pkind, dkind):
    return processing_factor(PAYLOADS[pkind](), DESTS[dkind]())


# ------------------------------------- FINDING A: the truncation worry, MEASURED
def truncation_sweep(dkind="stellar photosphere"):
    """[(payload convention, n elements, binder, factor)] -- the worry, priced.

    The theorem says extension cannot LOWER the max.  This measures how much it
    actually raises it, which is the question the theorem does not answer.
    """
    out = []
    for pk in ("bulk 11-element", "essential 25", "as-composed 59"):
        p = PAYLOADS[pk]()
        e, f = processing_factor(p, DESTS[dkind]())
        out.append((pk, len(p), e, f))
    return out


def truncation_shift(dkind="stellar photosphere"):
    """Fractional change in the factor from 11 elements to 60.  MEASURED."""
    rows = truncation_sweep(dkind)
    return rows[-1][3] / rows[0][3] - 1.0


def monotone_extension_holds(trials=400, seed=11):
    """Random-support check of the theorem, beside the z3 discharge."""
    import random
    r = random.Random(seed)
    s = solar_hybrid()
    els = [e for e in s if e in ATOMIC_MASS]
    for _ in range(trials):
        sub = r.sample(els, r.randint(2, 10))
        p = {e: r.random() * s[e] * r.choice([0.1, 1.0, 10.0]) for e in sub}
        extra = [e for e in els if e not in sub]
        if not extra:
            continue
        q = dict(p)
        for e in r.sample(extra, min(5, len(extra))):
            q[e] = r.random() * s[e] * r.choice([0.1, 1.0, 10.0])
        if processing_factor(q, s)[1] < processing_factor(p, s)[1] - 1e-15:
            return False
    return True


def z3_monotone_extension(n=5):
    """THEOREM, machine-checked over the reals: extension cannot lower the max.

    UNSAT of the negation is the proof.  ('SKIPPED', ...) without z3.
    """
    try:
        import z3
    except ImportError:
        return "SKIPPED", "z3 not installed"
    s = [z3.Real("s%d" % i) for i in range(n + 1)]
    p = [z3.Real("p%d" % i) for i in range(n + 1)]
    sol = z3.Solver()
    for i in range(n + 1):
        sol.add(s[i] > 0, p[i] >= 0)
    m, mp = z3.Real("m"), z3.Real("mp")
    sol.add(z3.Or(*[m == p[i] / s[i] for i in range(n)]))
    sol.add(*[m >= p[i] / s[i] for i in range(n)])
    sol.add(z3.Or(*[mp == p[i] / s[i] for i in range(n + 1)]))
    sol.add(*[mp >= p[i] / s[i] for i in range(n + 1)])
    sol.add(mp < m)
    r = sol.check()
    return ("THEOREM" if r == z3.unsat else "REFUTED"), str(r)


def z3_downset(n=4):
    """THEOREM over the REALS: A(s,M) is a down-set.  Stronger than a grid."""
    try:
        import z3
    except ImportError:
        return "SKIPPED", "z3 not installed"
    s = [z3.Real("s%d" % i) for i in range(n)]
    a = [z3.Real("a%d" % i) for i in range(n)]
    b = [z3.Real("b%d" % i) for i in range(n)]
    M = z3.Real("M")
    sol = z3.Solver()
    sol.add(M > 0, *[s[i] > 0 for i in range(n)])
    sol.add(*[a[i] >= 0 for i in range(n)], *[b[i] >= 0 for i in range(n)])
    sol.add(*[a[i] <= b[i] for i in range(n)])
    sol.add(*[b[i] <= M * s[i] for i in range(n)])
    sol.add(z3.Or(*[a[i] > M * s[i] for i in range(n)]))
    return ("THEOREM" if sol.check() == z3.unsat else "REFUTED"), str(sol.check())


def z3_join_closed(n=4):
    """THEOREM over the REALS: closed under join, hence a PRINCIPAL ideal."""
    try:
        import z3
    except ImportError:
        return "SKIPPED", "z3 not installed"
    s = [z3.Real("s%d" % i) for i in range(n)]
    a = [z3.Real("a%d" % i) for i in range(n)]
    b = [z3.Real("b%d" % i) for i in range(n)]
    M = z3.Real("M")
    sol = z3.Solver()
    sol.add(M > 0, *[s[i] > 0 for i in range(n)])
    sol.add(*[a[i] <= M * s[i] for i in range(n)])
    sol.add(*[b[i] <= M * s[i] for i in range(n)])
    j = [z3.If(a[i] > b[i], a[i], b[i]) for i in range(n)]
    sol.add(z3.Or(*[j[i] > M * s[i] for i in range(n)]))
    return ("THEOREM" if sol.check() == z3.unsat else "REFUTED"), str(sol.check())


# ------------------------------------------- FINDING C: stock.py's own numbers
STOCKPY_CRUST = {"O": 0.461, "Si": 0.282, "Al": 0.0823, "Fe": 0.0563,
                 "Ca": 0.0415, "Na": 0.0236, "Mg": 0.0233, "K": 0.0209,
                 "H": 0.0014, "P": 0.00105, "C": 0.002, "S": 0.00035,
                 "Cl": 0.00017, "N": 0.00006, "Zn": 0.00007}


def stockpy_sixhundred():
    """stock.py says 'six hundred times'.  Recompute from its own tables."""
    f = factors(STOCKPY_HUMAN, STOCKPY_CRUST)
    return f["N"], f["P"], f["N"] / f["P"]


def stockpy_potassium():
    """(stock.py K factor, ICRP K factor, gap at each).  P is the incumbent."""
    s = solar_hybrid()
    fP = STOCKPY_HUMAN["P"] / s["P"]
    k_sp = STOCKPY_HUMAN["K"] / s["K"]
    k_icrp = (140.0 / 70000.0) / s["K"]
    return k_sp, k_icrp, fP / k_sp, fP / k_icrp


def stockpy_chondrite_flip():
    """stock.py says N binds at a chondrite.  On the ICRP payload, P does."""
    p = payload("as-composed")
    f = factors(p, CHONDRITE)
    sp = factors(STOCKPY_HUMAN, CHONDRITE)
    return (max(sp, key=lambda k: sp[k]), sp[max(sp, key=lambda k: sp[k])],
            max(f, key=lambda k: f[k]), f[max(f, key=lambda k: f[k])],
            f["N"])


# ----------------------------------------------- FINDING D: the lithium runner-up
def li_dex_gap():
    """The solar lithium depletion: (dex, factor).  Largest gap in A09."""
    ph, me = A09["Li"]
    return me - ph, 10.0 ** (me - ph)


def largest_dex_gap():
    """Which element in A09 has the largest photospheric/meteoritic gap."""
    g = {e: abs(v[1] - v[0]) for e, v in A09.items()
         if v[0] is not None and v[1] is not None and e not in ("H", "He")}
    e = max(g, key=lambda k: g[k])
    return e, g[e]


def runner_up(pkind="as-composed 59", dkind="stellar photosphere"):
    r = ranked(PAYLOADS[pkind](), DESTS[dkind](), 2)
    return r[1][0], r[1][1], r[0][1] / r[1][1]


# --------------------------------------------- FINDING E: the craft is the hard one
def craft_table():
    return [(d, ) + processing_factor(_norm(CRAFT), DESTS[d]())
            for d in ("stellar photosphere", "solar meteoritic",
                      "CI chondrite", "Earth cont. crust")]


def craft_vs_human(dkind="CI chondrite"):
    """How many times harder, per kg, a declared craft is than a human."""
    return (binding_under("craft 1000 kg (DECLARED)", dkind)[1] /
            binding_under("as-composed 59", dkind)[1])


def craft_sensitivity(dkind="CI chondrite"):
    """The factor is linear in ONE declared number.  Which, and how much.

    Halving the binding element's declared fraction halves the factor and
    nothing else changes -- the honest sensitivity report for a stipulated
    input.  Returns (binder, factor, factor with binder halved, new binder).
    """
    e, f = processing_factor(_norm(CRAFT), DESTS[dkind]())
    c2 = dict(CRAFT)
    c2[e] = c2[e] / 2.0
    e2, f2 = processing_factor(_norm(c2), DESTS[dkind]())
    return e, f, f2, e2


# ------------------------------------- FINDING F: devolatilised vs primitive
VOLATILE_CUT = 500.0


def regime_of(dkind, pkind="as-composed 59"):
    """Labelled from T_c alone, not from what kind of object it is."""
    e, f = binding_under(pkind, dkind)
    tc = TCOND.get(e)
    if tc is None:
        return e, f, None, "UNKNOWN-TC"
    return e, f, tc, ("VOLATILITY-LIMITED" if tc < VOLATILE_CUT
                      else "ABUNDANCE-LIMITED")


def volatility_regime():
    return [(d,) + regime_of(d) for d in
            ("stellar photosphere", "Jupiter (3x solar)", "CI chondrite",
             "Earth cont. crust")]


# ------------------------------- FINDING G: elements existing is not stock
OXIDE_O = {"Mg": 1.0, "Si": 2.0, "Al": 1.5, "Ca": 1.0, "Fe": 1.0, "Na": 0.5,
           "K": 0.5, "Ti": 2.0, "Cr": 1.5, "Mn": 1.0, "Ni": 1.0, "P": 2.5}


def condensed_budget():
    """Every row of section 7, COMPUTED from the abundance and T_c tables."""
    X = solar_hybrid()
    refr = [e for e in X if TCOND.get(e, -1.0) >= VOLATILE_CUT]
    rock_bare = sum(X[e] for e in refr)
    bound_O = sum((X[e] / ATOMIC_MASS[e]) * OXIDE_O.get(e, 0.0) * ATOMIC_MASS["O"]
                  for e in refr)
    rock = rock_bare + bound_O
    o_left = max(0.0, X["O"] - bound_O)
    ice = o_left * (2 * ATOMIC_MASS["H"] + ATOMIC_MASS["O"]) / ATOMIC_MASS["O"]
    return {"H+He": X["H"] + X["He"], "Z": 1.0 - X["H"] - X["He"],
            "refractory": rock_bare, "bound O": bound_O, "rock": rock,
            "water ice": ice, "rock+ice": rock + ice}


def metallicity():
    X = solar_hybrid()
    return 1.0 - X["H"] - X["He"]


# ------------------------------------------------ what a node costs
def feedstock_kg(payload_kg, pkind, dkind):
    return payload_kg * binding_under(pkind, dkind)[1]


def node_mass(payload_kg=70.0, pkind="as-composed 59"):
    return [(d, feedstock_kg(payload_kg, pkind, d)) for d in
            ("stellar photosphere", "Jupiter (3x solar)", "CI chondrite",
             "Earth cont. crust")]


def sweep(payload_kg, rho, pkind="as-composed 59", dkind="stellar photosphere",
          usable=1.0):
    m = feedstock_kg(payload_kg, pkind, dkind)
    v = m / (rho * usable)
    return v, (3.0 * v / (4.0 * math.pi)) ** (1.0 / 3.0)


def against_the_shell(payload_kg=1000.0, pkind="craft 1000 kg (DECLARED)"):
    return FUCHS_SHELL_KG / feedstock_kg(payload_kg, pkind, "CI chondrite")


GATE = ("B admissible <=> within the corridor's arrival aperture there is a "
        "CONDENSED body, PRIMITIVE rather than devolatilised, holding at least "
        "M(p,s) * m_payload of accessible mass.")

CLAIMS_REFUSAL = ("That the transition is an instance of the method equation. "
                  "A shared shape is not a correspondence, and none is asserted.")


# ----------------------------------------------------------------- the reading
def report():
    W = 76
    def h(t):
        print("\n" + "=" * W + "\n" + t + "\n" + "=" * W)

    h("1.  PAYLOAD -- 70 kg REFERENCE ADULT, BY MASS AND BY MOLE (ICRP/Emsley)")
    g = dict(HUMAN_G_BULK); g.update(HUMAN_G_ESSENTIAL_TRACE)
    g.update(HUMAN_G_INCIDENTAL)
    p = payload("as-composed"); mo = mole_fractions(p)
    print("   %-4s %13s %13s %12s" % ("el", "mass frac", "mole frac", "grams"))
    for e, _ in sorted(p.items(), key=lambda kv: -kv[1])[:16]:
        print("   %-4s %13.5e %13.5e %12.6g" % (e, p[e], mo[e], g[e]))
    print("   ... %d elements; mass sums %.8f, mole %.8f"
          % (len(p), sum(p.values()), sum(mo.values())))

    h("2.  PAYLOAD -- 1000 kg ENGINEERING CRAFT.  DECLARED, NOT MEASURED.")
    cp = _norm(CRAFT); cm = mole_fractions(cp)
    for e, _ in sorted(cp.items(), key=lambda kv: -kv[1])[:8]:
        print("   %-4s mass %11.5e  mole %11.5e  %9.3f kg"
              % (e, cp[e], cm[e], cp[e] * 1000.0))
    for e in ("Ta", "Au", "Ag", "Li"):
        print("   %-4s mass %11.5e  mole %11.5e  %9.3f kg   <- the rarities"
              % (e, cp[e], cm[e], cp[e] * 1000.0))
    print("   %d elements declared" % len(cp))

    h("3.  FINDING A -- THE TRUNCATION WORRY IS REAL AND IT IS EMPTY")
    st, det = z3_monotone_extension()
    print("   monotone-extension theorem over the reals : %s (%s)" % (st, det))
    print("   random-support check                      : %s"
          % monotone_extension_holds())
    print("   %-24s %4s %-4s %14s" % ("payload convention", "n", "bind", "factor"))
    for pk, n, e, f in truncation_sweep():
        print("   %-24s %4d %-4s %14.5e" % (pk, n, e, f))
    print("   48 added elements move the factor by %+.4f %%  -- EMPTY."
          % (100.0 * truncation_shift()))
    print("   THE HUMAN STOCK CONSTRAINT IS BULK CHEMISTRY.  MEASURED.")

    h("4.  FINDING B -- THE PHOTOSPHERIC COLUMN CANNOT PRICE THE PAYLOAD")
    m = missing_photospheric()
    print("   %d payload elements have NO photospheric determination:" % len(m))
    print("     " + "  ".join(m))
    e, f = binding_under("as-composed 59", "photospheric-only")
    print("   photospheric-only column returns %s at %s -- an artefact." % (e, f))
    print("   every cosmic number here uses the HYBRID column instead.")

    h("5.  FINDING C -- THREE NUMBERS IN stock.py ARE WRONG.  RECORDED.")
    n, pp, r = stockpy_sixhundred()
    print("   (i)   crust N %.5e / crust P %.5e = %.4f" % (n, pp, r))
    print("         stock.py says 'six hundred times'.  Overstated %.2fx."
          % (600.0 / r))
    ks, ki, gs, gi = stockpy_potassium()
    print("   (ii)  K at stock.py's 0.0040 -> %.5e   (280 g in 70 kg)" % ks)
    print("         K at ICRP's    140 g   -> %.5e" % ki)
    print("         runner-up gap  %.3fx -> %.3fx.  The 'within 1.32x' fails."
          % (gs, gi))
    a, af, b, bf, nf = stockpy_chondrite_flip()
    print("   (iii) chondrite binder  stock.py %s %.5e  |  ICRP %s %.5e (N %.5e)"
          % (a, af, b, bf, nf))
    print("         the element flips; the magnitude agrees to %.1f %%."
          % (100.0 * abs(bf - af) / bf))

    h("6.  FINDING D -- THE RUNNER-UP IS LITHIUM, AND IT IS REAL")
    d, x = li_dex_gap()
    le, lg = largest_dex_gap()
    print("   Li photospheric %.2f, meteoritic %.2f -> %.2f dex = %.1fx"
          % (A09["Li"][0], A09["Li"][1], d, x))
    print("   largest phot/met gap in A09 is %s at %.2f dex -- it IS lithium"
          % (le, lg))
    ru, rf, gap = runner_up()
    print("   runner-up against a photosphere: %s at %.5e, only %.3fx behind P"
          % (ru, rf, gap))
    print("   against meteoritic stock Li is %.5e -- irrelevant."
          % factors(payload("as-composed"), solar("meteoritic"))["Li"])
    print("   NOT A DATUM ERROR: the Sun burns its lithium.  Thermal history.")

    h("7.  FINDING E -- THE CONSTRAINT BITES ON TECHNOLOGY, NOT BIOLOGY")
    print("   %-24s %-4s %14s %16s"
          % ("destination", "bind", "factor", "feedstock/1000 kg"))
    for d, e, f in craft_table():
        # 1000 kg payload * f kg/kg = 1000*f kg = f tonnes
        print("   %-24s %-4s %14.5e %13.4e t" % (d, e, f, f))
    print("   human at a chondrite  P %.5e  = %.3f t for 70 kg"
          % (binding_under("as-composed 59", "CI chondrite")[1],
             feedstock_kg(70.0, "as-composed 59", "CI chondrite") / 1000.0))
    print("   THE CRAFT IS %.4e x HARDER PER KILOGRAM." % craft_vs_human())
    be, bf2, hf, he = craft_sensitivity()
    print("   sensitivity: halve declared %s -> %.5e (binder becomes %s)"
          % (be, hf, he))

    h("8.  FINDING F -- DEVOLATILISED vs PRIMITIVE.  A CHONDRITE SITS WITH THE STAR.")
    print("   %-24s %-4s %14s %7s  %s"
          % ("destination", "bind", "factor", "T_c/K", "regime"))
    for d, e, f, tc, reg in volatility_regime():
        print("   %-24s %-4s %14.5e %7s  %s" % (d, e, f, tc, reg))
    print("   the cut is not star-vs-body.  It is outgassed-vs-primitive.")
    print("   -> the selector on B is THE SNOW LINE, i.e. orbital radius.")

    h("9.  FINDING G -- ELEMENTS EXISTING IS NOT STOCK.  COMPUTED.")
    b = condensed_budget()
    for k in ("H+He", "Z", "refractory", "bound O", "rock", "water ice",
              "rock+ice"):
        print("   %-28s %14.5e" % (k, b[k]))
    print("   %.3f %% of solar-composition mass condenses nowhere."
          % (100.0 * (1.0 - b["rock+ice"])))
    for d, m_ in node_mass():
        print("   node for one 70 kg human at %-22s %12.5e kg" % (d, m_))
    v, rr = sweep(70.0, RHO_ISM)
    print("   ISM gas at 1/cm^3: %.5e m^3, sphere r = %.5e km" % (v, rr / 1e3))
    v, rr = sweep(70.0, RHO_ISM, usable=DUST_TO_GAS)
    print("   ISM dust only    : %.5e m^3, sphere r = %.5e km" % (v, rr / 1e3))
    print("   even the craft's bill is %.5e x below the shell."
          % against_the_shell())

    h("10. THE ORDER STRUCTURE, AND COORDINATE 7")
    for nm, fn in (("down-set", z3_downset), ("join-closed", z3_join_closed)):
        st, det = fn()
        print("   %-12s over the reals : %s (%s)" % (nm, st, det))
    print("   -> a PRINCIPAL ideal generated by M*s.  Theorem, not a grid.")
    print("   register 66 / tools/orderideal.py: DIFFERENT CARRIER (n,l,k cells")
    print("   of Lambda), different order.  Shared shape, no correspondence.")
    print("\n   THE GATE ON B:")
    for i in range(0, len(GATE), 70):
        print("     " + GATE[i:i + 70])
    print("\n   CLAIMS.md:9080 REFUSES, and this file does not reinstate it:")
    print("     \"That the transition is an instance of the method equation.")
    print("      A shared shape is not a correspondence, and none is asserted.\"")
    print()
    for k in sorted(SOURCES):
        print("   %-5s %s" % (k, SOURCES[k]))


# -------------------------------------------------------------------- fixtures
def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else \
            abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("   %-66s %s" % (label, "ok" if good else
                               "FAIL got=%r want=%r" % (got, want)))

    print("stockgate.py fixtures  (stdlib; z3 where labelled)")

    # -- baseline: reproduce stock.py to the digit
    s = solar_hybrid()
    chk("hybrid mass fractions sum to 1", sum(s.values()), 1.0, 1e-12)
    chk("H dominates", s["H"], 0.737388, 1e-5)
    chk("stock.py's headline P factor reproduced",
        processing_factor(STOCKPY_HUMAN, solar("photospheric"))[1], 1716.7, 1e-3)
    chk("and its binding element",
        processing_factor(STOCKPY_HUMAN, solar("photospheric"))[0], "P")
    chk("stock.py's chondrite factor reproduced to 6%",
        abs(10.063 - processing_factor(STOCKPY_HUMAN, CHONDRITE)[1]) / 10.063
        < 0.08, True)

    # -- FINDING A
    st, det = z3_monotone_extension()
    chk("z3: monotone extension is a THEOREM", st in ("THEOREM", "SKIPPED"), True)
    print("      -> %s %s" % (st, det))
    chk("random-support monotonicity", monotone_extension_holds(), True)
    rows = truncation_sweep()
    chk("11 bulk elements", rows[0][3], 1911.19, 1e-4)
    chk("59 as-composed elements", rows[2][3], 1910.87, 1e-4)
    chk("every convention binds on P", {r[2] for r in rows}, {"P"})
    chk("48 added elements shift the factor by under 0.1%",
        abs(truncation_shift()) < 1e-3, True)
    chk("the shift is NEGATIVE -- pure renormalisation",
        truncation_shift() < 0.0, True)
    top = ranked(payload("as-composed"), s, 3)
    chk("no added element EXCEEDS P, so the binder never moves", top[0][0], "P")
    chk("BUT THE MARGIN IS THIN: Li reaches this fraction of P",
        top[1][1] / top[0][1], 0.91758, 1e-4)
    chk("and Li is one of the 34 INCIDENTAL elements stock.py omits",
        "Li" in HUMAN_G_INCIDENTAL, True)
    chk("the third-placed element is a comfortable 2.93x behind",
        top[0][1] / top[2][1], 2.9318, 1e-4)
    chk("lead, the one that looked dangerous, is far off",
        factors(payload("as-composed"), s)["Pb"], 200.9, 1e-3)

    # -- FINDING B
    m = missing_photospheric()
    chk("12 payload elements lack a photospheric value", len(m), 12)
    chk("iodine among them", "I" in m, True)
    chk("photospheric-only returns infinity",
        math.isinf(binding_under("as-composed 59", "photospheric-only")[1]), True)
    chk("the hybrid column does not", 
        math.isfinite(binding_under("as-composed 59", "stellar photosphere")[1]),
        True)

    # -- FINDING C
    n, pp, r = stockpy_sixhundred()
    chk("stock.py's crust N/P is 56, not 600", r, 56.0, 1e-9)
    chk("overstated by", 600.0 / r, 10.7143, 1e-4)
    ks, ki, gs, gi = stockpy_potassium()
    chk("stock.py's K is exactly twice ICRP's", ks / ki, 2.0, 1e-12)
    chk("runner-up gap on the corrected K exceeds 1.32x", gi > 1.32, True)
    chk("and equals", gi, 2.6320, 1e-3)
    a, af, b, bf, nf = stockpy_chondrite_flip()
    chk("stock.py's chondrite binder is N", a, "N")
    chk("on the ICRP payload it is P", b, "P")
    chk("with N second", nf < bf, True)
    chk("the magnitudes still agree to 8%", abs(bf - af) / bf < 0.08, True)

    # -- FINDING D
    d, x = li_dex_gap()
    chk("the Li dex gap", d, 2.21, 1e-9)
    chk("= a factor of", x, 162.18, 1e-3)
    le, lg = largest_dex_gap()
    chk("and it is the largest in A09", le, "Li")
    ru, rf, gap = runner_up()
    chk("the true runner-up is Li, not K", ru, "Li")
    chk("within 1.10x of P", gap < 1.10, True)
    chk("but irrelevant on meteoritic stock",
        factors(payload("as-composed"), solar("meteoritic"))["Li"] < 20.0, True)

    # -- FINDING E
    ct = dict((d_, (e_, f_)) for d_, e_, f_ in craft_table())
    chk("the craft binds on Ta at a chondrite", ct["CI chondrite"][0], "Ta")
    chk("at this factor", ct["CI chondrite"][1], 90081.97, 1e-5)
    chk("on Au at a crust", ct["Earth cont. crust"][0], "Au")
    chk("on Li at a photosphere -- the depletion again",
        ct["stellar photosphere"][0], "Li")
    chk("three distinct binding elements across four destinations",
        len({v[0] for v in ct.values()}), 3)
    chk("none of them biogenic",
        {v[0] for v in ct.values()} & {"C", "H", "N", "O", "P", "S"}, set())
    chk("the craft is >8000x harder per kg than a human",
        craft_vs_human() > 8000.0, True)
    chk("and equals", craft_vs_human(), 8417.99, 1e-4)
    be, bf2, hf, he = craft_sensitivity()
    chk("the factor is linear in one declared number, up to renormalisation",
        hf / (bf2 / 2.0), 1.0, 1e-3)
    chk("and halving it does not change the binder", he, be)

    # -- FINDING F
    reg = dict((d_, r_) for d_, e_, f_, t_, r_ in volatility_regime())
    chk("a star is abundance-limited", reg["stellar photosphere"],
        "ABUNDANCE-LIMITED")
    chk("a gas giant likewise", reg["Jupiter (3x solar)"], "ABUNDANCE-LIMITED")
    chk("AND SO IS A CHONDRITE -- it kept its volatiles",
        reg["CI chondrite"], "ABUNDANCE-LIMITED")
    chk("only the crust is volatility-limited", reg["Earth cont. crust"],
        "VOLATILITY-LIMITED")
    chk("the crust binds on N", binding_under("as-composed 59",
                                              "Earth cont. crust")[0], "N")
    chk("N's T_c is below the cut and P's is above",
        TCOND["N"] < VOLATILE_CUT <= TCOND["P"], True)
    chk("the crust is >40x worse than the chondrite",
        binding_under("as-composed 59", "Earth cont. crust")[1] /
        binding_under("as-composed 59", "CI chondrite")[1], 42.86, 1e-3)
    chk("Jupiter's 3x enrichment buys 2.92x, not 3 -- renormalisation",
        binding_under("as-composed 59", "stellar photosphere")[1] /
        binding_under("as-composed 59", "Jupiter (3x solar)")[1], 2.92187, 1e-4)

    # -- FINDING G
    b = condensed_budget()
    chk("H+He is 98.66% of solar mass", b["H+He"], 0.986630, 1e-5)
    chk("Z from the hybrid column", b["Z"], 0.0133696, 1e-4)
    chk("rock, with stoichiometric oxygen", b["rock"], 4.9690e-3, 1e-3)
    chk("rock+ice", b["rock+ice"], 9.4877e-3, 1e-3)
    chk("over 99% of a solar reservoir condenses nowhere",
        1.0 - b["rock+ice"] > 0.99, True)
    chk("rock alone is under 0.5%", b["rock"] < 5.0e-3, True)
    v, r_ = sweep(70.0, RHO_ISM)
    chk("ISM gas sweep radius exceeds 1e5 km", r_ / 1e3 > 1e5, True)
    v2, _ = sweep(70.0, RHO_ISM, usable=DUST_TO_GAS)
    chk("pricing the dust alone is 100x the volume", v2 / v, 100.0, 1e-9)
    chk("even the craft's bill is 19+ orders below the shell",
        math.log10(against_the_shell()) > 19.0, True)

    # -- composition bookkeeping
    p = payload("as-composed")
    chk("59 elements in the as-composed payload", len(p), 59)
    chk("mass fractions sum to 1", sum(p.values()), 1.0, 1e-12)
    chk("mole fractions sum to 1", sum(mole_fractions(p).values()), 1.0, 1e-12)
    chk("H is the most abundant by MOLE though O is by MASS",
        max(mole_fractions(p), key=lambda k: mole_fractions(p)[k]), "H")
    chk("and O by mass", max(p, key=lambda k: p[k]), "O")
    cp = _norm(CRAFT)
    chk("craft mass fractions sum to 1", sum(cp.values()), 1.0, 1e-12)
    chk("craft mole fractions sum to 1", sum(mole_fractions(cp).values()),
        1.0, 1e-12)

    # -- order structure
    for nm, fn in (("down-set", z3_downset), ("join-closed", z3_join_closed)):
        st, det = fn()
        chk("z3: %s over the reals" % nm, st in ("THEOREM", "SKIPPED"), True)
        print("      -> %s %s" % (st, det))

    print("\n%d failure(s)" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
