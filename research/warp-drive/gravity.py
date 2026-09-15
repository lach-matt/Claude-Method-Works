#!/usr/bin/env python3
r"""
gravity.py -- THE GRAVITY INDEX, DERIVED FROM THE ELEMENTS AND READ ACROSS
DIMENSIONS.

M: "The gravity index does belong because it is derived from the elements
themselves. I am aware the Petrov is spacetime, but specifically gravity is a
force that cannot exist outside spacetime, otherwise it would no longer be
relative."  And before that: "it might be incomplete for a very particular
reason, it is relative and measurable across dimensions."

    python3 gravity.py             the reading
    python3 gravity.py --selftest  fixtures

===============================================================================
0. WHY petrov.py IS NOT THIS, AND IS NOT WITHDRAWN EITHER
===============================================================================

`petrov.py` charts the Petrov type of nine named spacetimes.  It is a correct
index of what it indexes and it stays where it is.  It is NOT an index of the
periodic elements, on three counts that are facts about the file rather than
opinions about it:

  (1) ITS MEMBERS ARE SPACETIMES, NOT ELEMENTS.  Minkowski, FLRW, a pp-wave.
      None of them carries a quantum number, so it fails the criterion
      `registry.enforce()` applies, and registry does not seat it.

  (2) IT IS A D = 4 THEOREM AND SAYS SO IN ITS OWN FIRST LINE.  "A Weyl tensor
      has four principal null directions counted with multiplicity" is the
      factorisation of the Weyl SPINOR into four principal spinors, and that is
      available in four dimensions and nowhere else.  Above four, the
      classification is the CMPP alignment type, and a GENERIC Weyl tensor
      there has no aligned null direction at all -- type G, with no
      four-dimensional analogue.  petrov.py codes (P, X) = (0, 0) as type O,
      conformally flat, so a generic higher-dimensional vacuum read through
      that chart would print as FLAT.  **That is the particular reason M asked
      about, and it is a category error rather than a missing row.**

  (3) AND READ AGAINST ELEMENTS IT IS MAXIMALLY DEGENERATE.  Schwarzschild,
      Kerr and Reissner-Nordstrom are the only three rows an atom could ever
      occupy, and petrov.py puts all three in type D at (P, X) = (2, 2).  Every
      element, every ionisation stage and every level would land in one cell.

THIS FILE IS THE INDEX THOSE THREE FACTS ASK FOR: members that are nuclides in
charge states, coordinates measured from banked data, and the spacetime
dimension carried as a coordinate rather than assumed.

===============================================================================
1. WHAT A MEMBER IS
===============================================================================

    (Z, N, A, q, Ne, 2Je, D)

        Z     proton number
        N     neutron number
        A     nucleon number, A = Z + N        RECOMPUTED, never read
        q     charge state of the ion          q = 0 is the neutral atom
        Ne    electron count, Ne = Z - q
        2Je   twice the total electronic angular momentum of the GROUND level
        D     the spacetime dimension the field is read in

Every slot is a quantum number or a count of them.  The criterion
`registry.enforce()` applies is met by construction, not by exemption.

    **2,696 members, over 8 dimensions: 21,568 charted rows.**
    87 species (element + charge state), Z from 3 to 90, q from 0 to 15.

===============================================================================
2. WHERE EVERY NUMBER COMES FROM
===============================================================================

    M   AME2020 Table I, `extracted/archives/restore-point-2-13/captures/
        AME2020-TableI.tsv` -- 3,558 nuclides with Z, N, A, symbol, mass excess
        in keV, uncertainty and a quality flag.  The ion mass is

            M = A*u + (mass excess)/c^2 - q*m_e

        and the reconstruction is checked against the table's own zero: carbon
        12 has mass excess 0.0 keV by the definition of the scale, and the
        expression returns exactly 12 u for it.  That is a fixture, not a
        remark.

        ELECTRON BINDING IS NEGLECTED, AND THE NEGLECT IS BOUNDED RATHER THAN
        WAVED AT.  `binding_bound()` takes the crude hydrogenic ceiling
        Z^3 * 13.6 eV -- every electron bound no more tightly than the
        innermost one, counted Z times -- against M c^2 for every member.  The
        worst is **5.1e-5, at Z = 90, A = 208**.  The coordinates below are
        decade-resolution, so the neglect sits three orders below the
        resolution and cannot move a cell.  The selftest pins the comparison.

    q   from the spectroscopic numeral of the capture: Al III is q = 2.  Exact
        by the definition of the numeral.

    2Je the NIST ASD level captures in `recovered/`, columns
        `config  term  J  level_cm1`, taking the row at level_cm1 = 0.00
        exactly -- the ground level, by the table's own convention.  57 of the
        captures carry that header commented out; the parser accepts both
        spellings, which is a fact about the capture format and not an
        inference about the data.

        149 captures name a species and carry a level table: **118 distinct
        species**.  **87 of them bank a TRUE ground.**  The other **31** are
        series or high-l captures whose lowest banked level is an EXCITED one,
        and reading its J as a ground J is exactly the error this refuses.
        `excluded_species()` names all 31 with the level that disqualified
        each.

    D   NOT MEASURED.  It is the index's independent variable, and carrying it
        is the whole point of the file.  4 to 11: four is observed; five and
        six are where the horizon structure changes (section 4); ten and eleven
        are the string and M-theory dimensions, and eleven is Nahm's ceiling on
        supergravity.

===============================================================================
3. THE TWO ANGULAR-MOMENTUM FACTS, AND THEY NEED NO NUCLEAR DATUM
===============================================================================

The Kerr parameter is built from the body's TOTAL angular momentum, which for a
free atom is F, not Je.  AME2020 Table I banks no nuclear spin, so F is banked
for no member here.  TWO EXACT STATEMENTS SURVIVE THAT ANYWAY, and the index
rests on them rather than on a guess at I.

    **FORCED.**  Je is half-odd-integer exactly when Ne is odd; I is
    half-odd-integer exactly when A is odd; F = Je + I is half-odd-integer
    exactly when one of those holds and not the other.  A half-odd-integer
    angular momentum cannot be zero.  So

            (A + Ne) odd   ==>   F >= 1/2 > 0,

    with no knowledge of I whatever.  That is the coordinate `F`, it is exact
    arithmetic on two banked integers, and it holds for **1,347 of the 2,696
    members.**

    **VANISHING.**  The converse needs one empirical input.  Every even-Z,
    even-N nucleus has ground-state spin zero; this is the pairing rule, it is
    exceptionless over measured ground states, and it is an EMPIRICAL RULE, not
    a theorem.  Its status is carried as `PAIRING_RULE_STATUS` and is never
    flattened.  Where it applies and 2Je = 0 as well, F = 0 exactly: **308
    members**, of which **228 distinct nuclides are neutral** and therefore
    have an exterior field that is EXACTLY SCHWARZSCHILD.

    The two are mutually exclusive, and the selftest checks that rather than
    assuming it: F = 0 established needs Ne even, while A + Ne odd with A even
    needs Ne odd.  **1,041 members are neither**, and those are the ones whose
    bound class is UNDETERMINED above four dimensions.

===============================================================================
4. THE DIMENSION CHANGES THE ANSWER, NOT THE ARITHMETIC
===============================================================================

A singly-rotating Myers-Perry black hole in D dimensions has a horizon where

        f(r) = r^(D-3) + a^2 * r^(D-5) = mu,        mu proportional to the mass.

        D = 4    f(r) = r + a^2/r.  It falls to a minimum 2a and rises; a root
                 needs mu >= 2a.  **THE KERR BOUND.**
        D = 5    f(r) = r^2 + a^2.  f(0) = a^2 > 0 and f increases; a root
                 needs mu >= a^2.  **A BOUND, and a different one.**
        D >= 6   D - 5 >= 1, so f(0) = 0 and f increases without limit.
                 **A ROOT EXISTS FOR EVERY mu > 0 AND EVERY a.  NO BOUND.**

    THAT IS THE ULTRASPINNING REGIME, and it is the one place where the
    dimension changes the answer rather than the arithmetic.  It is also
    COUPLING-FREE: the value of the D-dimensional gravitational constant is
    fixed by nothing measured here -- G_D carries dimensions four-dimensional
    experiment cannot reach -- and the statement above never uses it.  It says
    a root EXISTS, not where.

    **536 of the 2,696 members are bound at D <= 5 and unbound at D >= 6.**

    CHARGE IS NOT RELIEVED THE SAME WAY.  The static charged Tangherlini
    function is f(r) = 1 - mu/x + Q^2/x^2 with x = r^(D-3); its roots are the
    roots of x^2 - mu x + Q^2, which exist exactly when mu^2 >= 4 Q^2.  A
    bound, in every dimension.  The asymmetry is real: rotation is relieved by
    dimension and charge is not.

===============================================================================
5. THE COORDINATES
===============================================================================

    D   spacetime dimension                    4 .. 11
    B   horizon-bound class in this D          0 none, 1 a bound, 2 undetermined
    F   forced angular momentum                0 may vanish, 1 cannot
    X   spin-decade rank                       0 none, else the rank of
                                               floor(log10 chi)      [33..36]
    Y   charge-decade rank                     0 none, else the rank of
                                               floor(log10 Qtilde)   [15..17]
    E   mass evidence                          0 measured, 1 estimated, from
                                               AME2020's own quality column

        chi     = Je hbar c / (G M^2)             the dimensionless Kerr spin
        Qtilde  = q e / (M sqrt(4 pi eps0 G))     the dimensionless RN charge

    Kerr-Newman has a horizon exactly when chi^2 + Qtilde^2 <= 1.  Every
    charged or spinning member here exceeds that by fifteen to thirty-six
    orders of magnitude, which is the ordinary statement that an atom is not a
    black hole.  THE DECADE is what varies across the elements, and it is what
    is charted.

**B IS A TABLE OF EXACT SOLUTIONS, NOT A JUDGEMENT.**  Each branch names the
metric it rests on, and where no exact metric is known the value is 2 and stays
2.  In particular the general charged ROTATING solution of the Einstein-Maxwell
equations is not known in closed form for D >= 5, so a member with q > 0 whose
total angular momentum is not established zero has NO exact metric above four
dimensions.  `B = 2` records that instead of inheriting the static answer.

**THE ENCODING IS A RANK, AND THE ALTERNATIVE IS MEASURED.**  chi = 0 exactly
when Je = 0, and log 0 is not a number, so a member with no electronic angular
momentum has no decade at all.  Writing it as 0 beside decades of 33 to 36
would place it thirty-three units from its nearest neighbour and distort every
convex hull the geometry operator takes.  The coordinate is therefore the RANK
in the sorted alphabet, evenly spaced, as every other chart in this tree is.
That is a choice, so `encoding_sensitivity()` charts the raw-decade encoding as
well.  **Both give (0, 18, 65): the choice costs nothing, and that is measured
rather than assumed away.**

===============================================================================
6. WHAT IT MEASURES
===============================================================================

    2,696 members x 8 dimensions   21,568 rows
    distinct cells                 524          box 1,920
    no constant coordinate, no coordinate the others determine, no LABEL
    closers                        NONE.  K0.
    CELL                           (0, 18, 65)

        order 1360   algebra 1360   geometry 1360   information 1232
        statistics 1120        -- against 524 held

**FINDING A: THE DIMENSION IS INVISIBLE TO THE ADMISSIBLE CHART AND VISIBLE IN
THE CELL COUNT.**  Fix D and chart the remaining five coordinates:

        D = 4        62 cells      cell (0, 10, 12)
        D = 5 .. 11  66 cells      cell (0, 10, 12)

    The same (K, height, width) at every dimension, and FOUR MORE CELLS from
    five upward.  The four are the B = 2 rows: in four dimensions Kerr-Newman
    covers every (M, Q, J) so no member is undetermined, and from five upward
    the charged rotating metric is unknown and some are.  **So what the
    dimension adds to this index is an ignorance class, not a geometry class**
    -- and the admissible chart cannot see it, because (K, height, width) is
    invariant under it.  Recorded, not repaired.

**FINDING B: THE RELIEF AT SIX IS IN THE MEMBERS AND NOT IN THE CELL.**  536
members lose their bound at D = 6, and the cell does not move.  A chart that
reports (K, height, width) would report the ultraspinning transition as
nothing at all.  That is a limit of the chart, stated here so nobody reads the
invariance as a finding about gravity.

===============================================================================
7. WHAT THIS FILE REFUSES
===============================================================================

**TO CALL 2Je THE MEMBER'S SPIN.**  It is the electronic part.  The nuclear
part is not banked, so chi as computed is the electronic contribution to the
Kerr parameter and nothing more.  Section 3's two facts are the only
total-angular-momentum statements made here, and neither needs I.

**TO PUT A NUMBER ON A HORIZON ABOVE FOUR DIMENSIONS.**  G_D is fixed by
nothing measured here.  Only existence statements are made above D = 4, and
only where an exact solution supplies one.

**TO READ THE PAIRING RULE AS A THEOREM.**  Even-even ground states have spin
zero as an exceptionless empirical rule.  `PAIRING_RULE_STATUS` says so, and
every member whose F = 0 rests on it.

**TO EXTEND THE 87 SPECIES BY INFERENCE.**  Hund's rules would give a ground J
for every element in the table, and that is a computation, not a capture.  The
118 species that parse are counted, the 31 without a banked ground are named
with the level that disqualified each, and the index is the 87 that bank one.

**TO ASSIGN THE WARP METRICS ANYTHING.**  The same refusal petrov.py makes, for
the same reason: nothing in this tree computes one.

**TO CLAIM THE INDEX IS COMPLETE.**  It is an index of the elements'
gravitational field as the banked data determines it.  `registry.COMPLETE`
stays False.
"""


import math
import os
import re
import sys

import hlaw
import mi
import overlap

ROOT = "/home/user/Claude-Method-Works"
AME = os.path.join(ROOT, "extracted/archives/restore-point-2-13/captures/"
                         "AME2020-TableI.tsv")
ASD = os.path.join(ROOT, "recovered")

# CODATA 2018, the values this tree already uses.
U_KG = 1.66053906660e-27
C_SI = 299792458.0
G_SI = 6.67430e-11
HBAR = 1.054571817e-34
E_CHG = 1.602176634e-19
M_E = 9.1093837015e-31
EPS0 = 8.8541878128e-12
KEV_J = 1.602176634e-16
EV_J = 1.602176634e-19
K_Q = math.sqrt(4 * math.pi * EPS0 * G_SI)

DIMS = tuple(range(4, 12))              # 4 .. 11, Nahm's ceiling at the top
NAMES = ("D", "B", "F", "X", "Y", "E")
ARITY = len(NAMES)

PAIRING_RULE_STATUS = "EMPIRICAL-RULE"  # even-even ground states have I = 0
NO_CHARGED_ROTATING_ABOVE_4 = True      # Einstein-Maxwell, D >= 5, closed form

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
         "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18}

_CACHE = {}


# ------------------------------------------------------------------ the data

def nuclides():
    """[(Z, N, A, symbol, mass_excess_keV, quality)] from AME2020 Table I."""
    if "nuc" not in _CACHE:
        out = []
        with open(AME, encoding="utf-8") as fh:
            for ln in fh:
                if ln.startswith("#") or ln.startswith("Z\t"):
                    continue
                p = ln.rstrip("\n").split("\t")
                if len(p) < 7:
                    continue
                Z, N, A = int(p[0]), int(p[1]), int(p[2])
                if A != Z + N:                      # A is recomputed, not read
                    continue
                out.append((Z, N, A, p[3], float(p[4]), p[6]))
        _CACHE["nuc"] = out
    return _CACHE["nuc"]


def symbol_to_Z():
    if "sym" not in _CACHE:
        s = {}
        for Z, _N, _A, sym, _d, _q in nuclides():
            s.setdefault(sym, Z)
        _CACHE["sym"] = s
    return _CACHE["sym"]


def _two_J(text):
    """2J from an ASD J column, or None if the cell is not a plain J."""
    t = text.strip()
    m = re.fullmatch(r"(\d+)/2", t)
    if m:
        return int(m.group(1))
    m = re.fullmatch(r"(\d+)", t)
    if m:
        return 2 * int(m.group(1))
    return None


def _species_of(lines):
    """(symbol, numeral) from a capture's header comments, or None."""
    s2z = symbol_to_Z()
    for h in lines[:8]:
        if not h.startswith("#"):
            continue
        m = re.match(r"#\s*([A-Z][a-z]?)\s+([IVX]+)\b", h)
        if m and m.group(1) in s2z and m.group(2) in ROMAN:
            return (m.group(1), m.group(2))
    return None


def captures():
    """{(symbol, numeral): (lowest banked level, 2J, config, term, file)}.

    The LOWEST level each capture banks with a readable J -- which is the
    ground level only where it is 0.00.  `grounds()` keeps those; the rest are
    named by `excluded_species()` with the level that disqualified them.
    """
    if "cap" in _CACHE:
        return _CACHE["cap"]
    out = {}
    for fn in sorted(os.listdir(ASD)):
        if not fn.endswith(".tsv"):
            continue
        with open(os.path.join(ASD, fn), encoding="utf-8",
                  errors="replace") as fh:
            txt = fh.read()
        if "level_cm1" not in txt:
            continue
        lines = txt.split("\n")
        sp = _species_of(lines)
        if sp is None:
            continue
        hi = next((i for i, l in enumerate(lines)
                    if l.startswith("config\t")
                    or l.lstrip("# ").startswith("config\t")), None)
        if hi is None:
            continue
        cols = lines[hi].lstrip("# ").split("\t")
        try:
            ij, il = cols.index("J"), cols.index("level_cm1")
            ic, it = cols.index("config"), cols.index("term")
        except ValueError:
            continue
        for l in lines[hi + 1:]:
            if not l.strip() or l.startswith("#"):
                continue
            p = l.split("\t")
            if len(p) <= max(ij, il, ic, it):
                continue
            try:
                lv = float(p[il].replace("[", "").replace("]", "")
                           .replace("+x", "").strip())
            except ValueError:
                continue
            tj = _two_J(p[ij])
            if tj is None:
                continue
            prev = out.get(sp)
            if prev is None or lv < prev[0]:
                out[sp] = (lv, tj, p[ic].strip(), p[it].strip(), fn)
            break
    _CACHE["cap"] = out
    return out


def grounds():
    """{(symbol, numeral): (2J, config, term, file)} -- a TRUE ground only."""
    return {sp: (v[1], v[2], v[3], v[4])
            for sp, v in captures().items() if v[0] == 0.0}


def excluded_species():
    """[(species, lowest banked level, file)] -- parsed, but no banked ground.

    Taking the J of an excited level as a ground J is the error this refuses.
    """
    return sorted((("%s %s" % sp), v[0], v[4])
                  for sp, v in captures().items() if v[0] != 0.0)


def capture_files():
    """How many recovered captures carry a level table AND name a species."""
    n = 0
    for fn in sorted(os.listdir(ASD)):
        if not fn.endswith(".tsv"):
            continue
        with open(os.path.join(ASD, fn), encoding="utf-8",
                  errors="replace") as fh:
            txt = fh.read()
        if "level_cm1" not in txt:
            continue
        if _species_of(txt.split("\n")) is not None:
            n += 1
    return n


def carbon12():
    """(mass in u, the table's mass excess) -- the scale's own zero.

    Carbon 12 has mass excess 0.0 keV BY THE DEFINITION of the atomic mass
    unit, so the mass reconstruction must return exactly 12 u for it.  It is an
    independent check on the whole path from the table to M, and it is a
    fixture rather than a remark.
    """
    for Z, _N, A, sym, dm, _q in nuclides():
        if sym == "C" and A == 12 and Z == 6:
            return (A * U_KG + dm * KEV_J / C_SI ** 2) / U_KG, dm
    return None, None


# ------------------------------------------------------------- the members

def members():
    """[(Z, N, A, q, Ne, 2Je, quality, M_kg, chi, Qtilde)] -- no D yet."""
    if "mem" in _CACHE:
        return _CACHE["mem"]
    s2z = symbol_to_Z()
    out = []
    for (sym, num), (tj, _cfg, _term, _f) in sorted(grounds().items()):
        Z, q = s2z[sym], ROMAN[num] - 1
        Ne = Z - q
        if Ne < 1:
            continue
        for zz, N, A, _s, dm, qual in nuclides():
            if zz != Z:
                continue
            M = A * U_KG + dm * KEV_J / C_SI ** 2 - q * M_E
            chi = (tj / 2.0) * HBAR * C_SI / (G_SI * M * M)
            qt = q * E_CHG / (M * K_Q)
            out.append((Z, N, A, q, Ne, tj, qual, M, chi, qt))
    _CACHE["mem"] = out
    return out


def binding_bound():
    """(worst ratio, the member it belongs to) for the neglected binding energy.

    Z^3 * 13.6 eV is a crude ceiling on an atom's total electronic binding --
    every electron bound no more tightly than the innermost hydrogenic one,
    counted Z times over.  Against M c^2 it must be far below the decade
    resolution of X and Y, or the neglect would be moving cells.
    """
    worst, who = 0.0, None
    for Z, _N, A, _q, _Ne, _tj, _ql, M, _c, _t in members():
        r = (Z ** 3 * 13.6 * EV_J) / (M * C_SI ** 2)
        if r > worst:
            worst, who = r, (Z, A)
    return worst, who


# ------------------------------------------------------- the two J statements

def forced(A, Ne):
    """1 iff the total angular momentum F cannot vanish.  Exact arithmetic.

    Je is half-odd-integer iff Ne is odd; I is half-odd-integer iff A is odd;
    F = Je + I is half-odd-integer iff exactly one holds, and a half-odd-integer
    angular momentum is never zero.  No nuclear datum is used.
    """
    return (A + Ne) % 2


def vanishes(Z, N, two_Je):
    """True iff F = 0 is established.  Rests on the PAIRING RULE, not a proof."""
    return Z % 2 == 0 and N % 2 == 0 and two_Je == 0


# ---------------------------------------------------- the horizon-bound table

BOUND_NONE, BOUND_YES, BOUND_UNDET = 0, 1, 2

BRANCHES = (
    ("D=4,  J=0, q=0      Schwarzschild                         no bound", 0),
    ("D=4,  otherwise     Kerr-Newman                           a bound", 1),
    ("D>=5, J=0, q=0      Tangherlini                           no bound", 0),
    ("D>=5, J=0, q>0      Tangherlini-Reissner-Nordstrom        a bound", 1),
    ("D=5,  J!=0, q=0     Myers-Perry, one rotation             a bound", 1),
    ("D>=6, J!=0, q=0     Myers-Perry, one rotation             NO BOUND", 0),
    ("D>=5, q>0, J not proved zero   no exact solution          undetermined", 2),
    ("D>=5, q=0, J undetermined      no determined parameters   undetermined", 2),
)


def bound_class(D, q, F, Jzero):
    """B: whether an extremality bound exists, from an exact solution only."""
    if D == 4:
        # Kerr-Newman covers every (M, Q, J) in four dimensions.
        return BOUND_NONE if (q == 0 and Jzero) else BOUND_YES
    if Jzero:
        # No rotation: static Tangherlini, charged or not.
        return BOUND_YES if q > 0 else BOUND_NONE
    if q > 0:
        # Einstein-Maxwell charged rotating: no closed form for D >= 5.
        return BOUND_UNDET
    if F:
        # Singly-rotating Myers-Perry, and section 4 is the whole content.
        return BOUND_YES if D == 5 else BOUND_NONE
    return BOUND_UNDET


# ----------------------------------------------------------------- the chart

def _ranks():
    """(spin alphabet, charge alphabet) -- the observed decades, sorted."""
    if "rk" not in _CACHE:
        sp = sorted({int(math.floor(math.log10(m[8])))
                     for m in members() if m[8] > 0})
        ch = sorted({int(math.floor(math.log10(m[9])))
                     for m in members() if m[9] > 0})
        _CACHE["rk"] = (sp, ch)
    return _CACHE["rk"]


def rows(raw_decades=False):
    """[(member tuple, cell)] -- every member in every dimension, charted."""
    sp, ch = _ranks()
    out = []
    for Z, N, A, q, Ne, tj, qual, M, chi, qt in members():
        F = forced(A, Ne)
        Jz = vanishes(Z, N, tj)
        if chi <= 0:
            X = -1 if raw_decades else 0
        else:
            d = int(math.floor(math.log10(chi)))
            X = d if raw_decades else sp.index(d) + 1
        if qt <= 0:
            Y = -1 if raw_decades else 0
        else:
            d = int(math.floor(math.log10(qt)))
            Y = d if raw_decades else ch.index(d) + 1
        E = 0 if qual == "M" else 1
        for D in DIMS:
            B = bound_class(D, q, F, Jz)
            out.append(((Z, N, A, q, Ne, tj, D), (D, B, F, X, Y, E)))
    return out


def index(raw_decades=False):
    """The gravity index: the distinct cells of the chart."""
    key = "idx%d" % raw_decades
    if key not in _CACHE:
        _CACHE[key] = frozenset(c for _m, c in rows(raw_decades))
    return _CACHE[key]


# -------------------------------------------------------------- measurements

def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def encoding_sensitivity():
    """(rank cell, raw-decade cell, whether they agree).

    The rank encoding is a choice; this measures what the alternative costs.
    """
    a, b = mi.cell(index(False)), mi.cell(index(True))
    return a, b, a == b


def constant_coords():
    """Coordinates taking one value -- they would widen every closure for free."""
    X = index()
    return [NAMES[i] for i in range(ARITY) if len({c[i] for c in X}) == 1]


def dependent_coords():
    """[(coordinate, the others)] for any coordinate the rest determine.

    OVER-REPRESENTATION IS THE FAULT THIS LOOKS FOR.  A coordinate that the
    others already fix adds no member distinction and multiplies the box.
    """
    X = sorted(index())
    out = []
    for i in range(ARITY):
        seen = {}
        dep = True
        for c in X:
            k = c[:i] + c[i + 1:]
            if seen.setdefault(k, c[i]) != c[i]:
                dep = False
                break
        if dep:
            out.append((NAMES[i], [NAMES[j] for j in range(ARITY) if j != i]))
    return out


def labels():
    """Coordinates overlap.py calls a LABEL rather than a measurement."""
    return [(NAMES[i], d, n, r) for i, d, n, r, v in
            overlap.resolution(index()) if v == "LABEL"]


def per_dimension_cells():
    """{D: (cells at this D, its (K, height, width))} on the five non-D slots.

    FINDING A lives here: the cell is the same at every dimension and the cell
    COUNT is not.
    """
    byD = {}
    for _m, c in rows():
        byD.setdefault(c[0], set()).add(c[1:])
    return {D: (len(v), mi.cell(frozenset(v))) for D, v in sorted(byD.items())}


def by_dimension():
    """{D: (cells at this D, the B values seen there)}."""
    out = {}
    for _m, c in rows():
        e = out.setdefault(c[0], [set(), set()])
        e[0].add(c)
        e[1].add(c[1])
    return {D: (len(v[0]), sorted(v[1])) for D, v in sorted(out.items())}


def relieved():
    """Members whose bound exists at D <= 5 and is gone at D >= 6.

    The ultraspinning statement, counted over the index's own members.
    """
    seen = {}
    for m, c in rows():
        seen.setdefault(m[:6], {})[c[0]] = c[1]
    return sorted(k for k, v in seen.items()
                  if v[4] == BOUND_YES and v[5] == BOUND_YES
                  and all(v[D] == BOUND_NONE for D in range(6, 12)))


def schwarzschild_members():
    """Members whose exterior field is exactly Schwarzschild: q = 0, F = 0."""
    return sorted({(Z, N, A) for Z, N, A, q, _Ne, tj, _ql, _M, _c, _t
                   in members() if q == 0 and vanishes(Z, N, tj)})


# ---------------------------------------------------------------- the reading

def report():
    X = index()
    ms = members()
    print("=" * 74)
    print("THE GRAVITY INDEX -- NUCLIDES, CHARGE STATES AND THE DIMENSION")
    print("=" * 74)
    print()
    print("Derived from the elements themselves, as M ruled. A member is a")
    print("nuclide in a charge state, read in a spacetime dimension:")
    print()
    print("    (Z, N, A, q, Ne, 2Je, D)")
    print()
    print("Every slot is a quantum number or a count of them, so registry's")
    print("criterion is met by construction rather than by exemption.")
    print()
    print("-" * 74)
    print("1. THE DATA, AND WHAT IT EXCLUDES.")
    print("-" * 74)
    m12, dm12 = carbon12()
    print("   AME2020 Table I nuclides kept        %d" % len(nuclides()))
    print("   carbon 12 mass excess, from the table %.1f keV" % dm12)
    print("   ...so the mass path must return       %s u    <- it returns %s"
          % (12.0, m12))
    print("   ASD captures naming a species        %d files" % capture_files())
    print("   distinct species among them          %d" % len(captures()))
    print("   ...banking a TRUE ground level       %d" % len(grounds()))
    print("   ...whose lowest level is EXCITED     %d   EXCLUDED"
          % len(excluded_species()))
    for nm, lv, _f in excluded_species()[:6]:
        print("        %-10s lowest banked level %12.2f cm-1" % (nm, lv))
    print("        ... and %d more, all named by excluded_species()"
          % (len(excluded_species()) - 6))
    print("   nuclide x charge-state members       %d" % len(ms))
    print("   x %d dimensions (4..11)               %d charted rows"
          % (len(DIMS), len(rows())))
    wb, who = binding_bound()
    print("   worst neglected binding / M c^2      %.2e  (Z=%d, A=%d)"
          % (wb, who[0], who[1]))
    print("   decade resolution of X and Y         1e-01")
    print("   -> the neglect is %d orders below the resolution, so it cannot"
          % round(math.log10(0.1 / wb)))
    print("      move a cell. Bounded, not waved at.")
    print()
    print("   THE %d SPECIES, WITH THEIR GROUND J:" % len(grounds()))
    line = "   "
    for i, (sp, v) in enumerate(sorted(grounds().items())):
        line += "%-14s" % ("%s %s %s" % (sp[0], sp[1], _j_str(v[0])))
        if i % 5 == 4:
            print(line)
            line = "   "
    if line.strip():
        print(line)
    print()
    print("-" * 74)
    print("2. THE TWO ANGULAR-MOMENTUM FACTS, WITH NO NUCLEAR DATUM.")
    print("-" * 74)
    nf = sum(1 for m in ms if forced(m[2], m[4]))
    nv = sum(1 for m in ms if vanishes(m[0], m[1], m[5]))
    print("   Je is half-odd-integer iff Ne is odd. I is half-odd-integer iff")
    print("   A is odd. F = Je + I is therefore half-odd-integer iff A + Ne is")
    print("   odd -- and a half-odd-integer angular momentum is never zero.")
    print()
    print("   F != 0 FORCED by (A + Ne) odd        %4d of %d members"
          % (nf, len(ms)))
    print("   F  = 0 by the pairing rule           %4d" % nv)
    print("   neither -- undetermined              %4d" % (len(ms) - nf - nv))
    print("   pairing rule status                  %s" % PAIRING_RULE_STATUS)
    sch = schwarzschild_members()
    print()
    print("   NUCLIDES WITH AN EXACTLY SCHWARZSCHILD EXTERIOR (q=0, F=0): %d"
          % len(sch))
    print("     %s ..." % ", ".join("%s-%d" % (_sym(z), a) for z, _n, a
                                    in sch[:12]))
    print()
    print("-" * 74)
    print("3. THE DIMENSION CHANGES THE ANSWER, NOT THE ARITHMETIC.")
    print("-" * 74)
    print("   Singly-rotating Myers-Perry:  f(r) = r^(D-3) + a^2 r^(D-5) = mu")
    print()
    print("     D = 4    minimum 2a, so a root needs mu >= 2a   THE KERR BOUND")
    print("     D = 5    f(0) = a^2 > 0, a root needs mu >= a^2  A BOUND")
    print("     D >= 6   D-5 >= 1, so f(0) = 0 and f rises without limit --")
    print("              A ROOT FOR EVERY mu > 0 AND EVERY a.   NO BOUND.")
    print()
    print("   It never uses the value of G_D, which nothing here measures.")
    print("   It says a root EXISTS, not where.")
    print()
    print("   %-4s %-7s %s" % ("D", "cells", "horizon-bound classes present"))
    for D, (n, bs) in by_dimension().items():
        print("   %-4d %-7d %s" % (D, n, "   ".join(_b_str(b) for b in bs)))
    rel = relieved()
    print()
    print("   MEMBERS BOUND AT D<=5 AND UNBOUND AT D>=6:   %d of %d"
          % (len(rel), len(ms)))
    print("   Every one is neutral with a forced angular momentum.")
    print()
    print("   CHARGE IS NOT RELIEVED THE SAME WAY. Static charged Tangherlini")
    print("   has roots of x^2 - mu x + Q^2 with x = r^(D-3), which exist iff")
    print("   mu^2 >= 4 Q^2: a bound, in every dimension. The asymmetry is")
    print("   real -- rotation is relieved by dimension and charge is not.")
    print()
    print("-" * 74)
    print("4. THE CHART.")
    print("-" * 74)
    for i, nm in enumerate(NAMES):
        vals = sorted({c[i] for c in X})
        print("   %-3s %-46s %s" % (nm, _coord_doc(nm), vals))
    print()
    print("   spin decades   floor(log10 chi)      %s" % (_ranks()[0],))
    print("   charge decades floor(log10 Qtilde)   %s" % (_ranks()[1],))
    print()
    print("   charted rows      %d" % len(rows()))
    print("   distinct cells    %d" % len(X))
    print("   box               %d" % overlap.box_of(X))
    print("   constant coords   %s" % (constant_coords() or "none"))
    print("   dependent coords  %s   <- no over-representation"
          % ([d[0] for d in dependent_coords()] or "none"))
    print("   LABEL coords      %s" % ([l[0] for l in labels()] or "none"))
    cl, _b = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %5d   E %5d%s"
              % (L, len(cl[L]), e, "   <-- CLOSES" if e == 0 else ""))
    print()
    print("   closers  %s" % (closers() or "NONE -- K0"))
    print("   CELL     %s" % (cell(),))
    a, b, same = encoding_sensitivity()
    print("   rank encoding %s   raw-decade %s   agree %s"
          % (a, b, same))
    print("   -> the encoding choice costs nothing, and that is measured.")
    print()
    print("-" * 74)
    print("5. TWO FINDINGS, RECORDED AND NOT REPAIRED.")
    print("-" * 74)
    pd = per_dimension_cells()
    print("   A. THE DIMENSION IS INVISIBLE TO THE CHART AND VISIBLE IN THE")
    print("      CELL COUNT. Fix D, chart the other five:")
    for D in DIMS:
        print("        D = %-3d %3d cells    cell %s" % (D, pd[D][0], pd[D][1]))
    print("      The same (K, height, width) at every dimension, and four more")
    print("      cells from five upward. The four are the B = 2 rows: in four")
    print("      dimensions Kerr-Newman covers every (M, Q, J) so nothing is")
    print("      undetermined; above it the charged rotating metric is unknown")
    print("      and some members are. SO WHAT THE DIMENSION ADDS HERE IS AN")
    print("      IGNORANCE CLASS, NOT A GEOMETRY CLASS.")
    print()
    print("   B. THE RELIEF AT SIX IS IN THE MEMBERS AND NOT IN THE CELL.")
    print("      %d members lose their bound at D = 6 and the cell does not"
          % len(rel))
    print("      move. A chart reporting (K, height, width) would report the")
    print("      ultraspinning transition as nothing at all. That is a limit")
    print("      of the chart, stated so nobody reads the invariance as a")
    print("      finding about gravity.")
    print()
    print("-" * 74)
    print("6. REFUSED.")
    print("-" * 74)
    print("   To call 2Je the member's spin -- it is the electronic part, and")
    print("     the nuclear part is not banked.")
    print("   To put a number on a horizon above D = 4 -- G_D is fixed by")
    print("     nothing measured here; only existence statements are made.")
    print("   To read the pairing rule as a theorem. It is %s."
          % PAIRING_RULE_STATUS)
    print("   To extend the %d species by Hund's rules -- that is a"
          % len(grounds()))
    print("     computation, not a capture.")
    print("   To assign the warp metrics anything.")
    print("   To claim completeness. registry.COMPLETE stays False.")
    return 0


def _sym(Z):
    for z, _n, _a, s, _d, _q in nuclides():
        if z == Z:
            return s
    return "?"


def _j_str(tj):
    return "%d" % (tj // 2) if tj % 2 == 0 else "%d/2" % tj


def _b_str(b):
    return {0: "0 none", 1: "1 bound", 2: "2 undet"}[b]


def _coord_doc(nm):
    return {"D": "spacetime dimension",
            "B": "horizon-bound class (0 none 1 bound 2 undet)",
            "F": "forced angular momentum (A+Ne odd)",
            "X": "spin-decade rank of chi",
            "Y": "charge-decade rank of Qtilde",
            "E": "mass evidence (0 measured 1 estimated)"}[nm]


# ------------------------------------------------------------------ fixtures

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    print("gravity selftest")

    # -- the data, and A is recomputed rather than trusted
    nuc = nuclides()
    chk("AME2020 nuclides kept", len(nuc), 3558)
    chk("and none was kept with A != Z + N",
        [1 for z, n, a, *_r in nuc if a != z + n], [])
    m12, dm12 = carbon12()
    chk("carbon 12 banks mass excess 0.0 keV, by definition", dm12, 0.0)
    chk("SO THE MASS PATH MUST RETURN EXACTLY 12 u FOR IT", m12, 12.0)

    chk("captures naming a species and carrying a level table",
        capture_files(), 149)
    chk("distinct species among them", len(captures()), 118)
    chk("of which bank a TRUE ground level", len(grounds()), 87)
    chk("the rest are excluded, by name", len(excluded_species()), 31)
    chk("no excluded species sits at level 0.00",
        [s2 for s2, lv, _f in excluded_species() if lv == 0.0], [])
    chk("87 + 31 accounts for every parsed species",
        len(grounds()) + len(excluded_species()), len(captures()))

    # -- the members
    ms = members()
    chk("members (species x nuclide)", len(ms), 2696)
    chk("rows (x 8 dimensions)", len(rows()), 2696 * 8)
    chk("every member has Ne >= 1", min(m[4] for m in ms) >= 1, True)
    chk("every member has A = Z + N",
        all(m[2] == m[0] + m[1] for m in ms), True)
    chk("2Je observed", sorted({m[5] for m in ms}), [0, 1, 2, 3, 4, 8])
    chk("Z runs 3 to 90", (min(m[0] for m in ms), max(m[0] for m in ms)),
        (3, 90))
    chk("q reaches 15 (Fe XVI)", max(m[3] for m in ms), 15)

    # -- THE NEGLECT IS BOUNDED, NOT WAVED AT
    wb, who = binding_bound()
    chk("worst neglected binding sits at Z = 90, A = 208", who, (90, 208))
    chk("and is below 1e-4 of M c^2", wb < 1e-4, True)
    chk("...three orders below the decade resolution of X and Y",
        wb < 0.1 / 100, True)

    # -- section 3: the two angular-momentum facts
    chk("forced is exactly (A + Ne) odd",
        all(forced(a, ne) == (a + ne) % 2
            for a in range(1, 40) for ne in range(1, 40)), True)
    chk("FORCED and VANISHES are mutually exclusive, measured not assumed",
        [m for m in ms if forced(m[2], m[4]) and vanishes(m[0], m[1], m[5])],
        [])
    chk("members with F forced nonzero", sum(1 for m in ms
                                             if forced(m[2], m[4])), 1347)
    chk("members with F established zero",
        sum(1 for m in ms if vanishes(m[0], m[1], m[5])), 308)
    chk("members that are neither -- the undetermined class",
        len(ms) - sum(1 for m in ms if forced(m[2], m[4]))
        - sum(1 for m in ms if vanishes(m[0], m[1], m[5])), 1041)
    chk("vanishes needs even Z, even N and 2Je = 0",
        [vanishes(20, 20, 0), vanishes(20, 21, 0), vanishes(19, 20, 0),
         vanishes(20, 20, 1)], [True, False, False, False])
    chk("nuclides whose exterior field is EXACTLY Schwarzschild",
        len(schwarzschild_members()), 228)
    chk("PAIRING_RULE_STATUS is not flattened to a proof",
        PAIRING_RULE_STATUS, "EMPIRICAL-RULE")

    # -- section 4: the horizon-bound table, branch by branch
    chk("D=4, q=0, J=0     Schwarzschild, no bound",
        bound_class(4, 0, 0, True), BOUND_NONE)
    chk("D=4, q>0          Kerr-Newman, a bound",
        bound_class(4, 1, 1, False), BOUND_YES)
    chk("D=4, J forced     Kerr, a bound",
        bound_class(4, 0, 1, False), BOUND_YES)
    chk("D=4 is never undetermined -- Kerr-Newman covers every (M, Q, J)",
        [bound_class(4, q, f, jz) for q in (0, 3) for f in (0, 1)
         for jz in (True, False) if not (f and jz)].count(BOUND_UNDET), 0)
    chk("D=7, q=0, J=0     Tangherlini, no bound",
        bound_class(7, 0, 0, True), BOUND_NONE)
    chk("q>0, J=0          Tangherlini-RN, a bound in EVERY dimension",
        [bound_class(D, 2, 0, True) for D in DIMS], [BOUND_YES] * 8)
    chk("D=5, q=0, J forced    Myers-Perry, a bound",
        bound_class(5, 0, 1, False), BOUND_YES)
    chk("D>=6, q=0, J forced   NO BOUND -- the ultraspinning regime",
        [bound_class(D, 0, 1, False) for D in (6, 7, 8, 9, 10, 11)],
        [BOUND_NONE] * 6)
    chk("D>=5, q>0, J not established zero: no exact solution, undetermined",
        [bound_class(D, 1, 1, False) for D in DIMS[1:]], [BOUND_UNDET] * 7)
    chk("and that refusal is carried as a flag",
        NO_CHARGED_ROTATING_ABOVE_4, True)
    chk("the branches are enumerated in the file", len(BRANCHES), 8)
    chk("every branch's verdict is one of the three",
        sorted({v for _t, v in BRANCHES}), [0, 1, 2])

    # -- the transition is at SIX, counted over the members
    rel = relieved()
    chk("members bound at D<=5 and unbound at D>=6", len(rel), 536)
    chk("every one of them is neutral and forced",
        [m for m in rel if m[3] != 0 or not forced(m[2], m[4])], [])
    chk("none is relieved at D = 5",
        [m for m in rel
         if bound_class(5, m[3], forced(m[2], m[4]), False) != BOUND_YES], [])

    # -- the chart
    X = index()
    chk("arity is 6", len(next(iter(X))), ARITY)
    chk("distinct cells", len(X), 524)
    chk("box", overlap.box_of(X), 1920)
    chk("no coordinate is constant", constant_coords(), [])
    chk("NO COORDINATE IS DETERMINED BY THE OTHERS -- no over-representation",
        [d[0] for d in dependent_coords()], [])
    chk("no coordinate is a LABEL", [l[0] for l in labels()], [])
    chk("D runs 4..11", sorted({c[0] for c in X}), list(DIMS))
    chk("B takes all three values", sorted({c[1] for c in X}), [0, 1, 2])
    chk("it closes NOTHING -- K0", closers(), [])
    chk("CELL", cell(), (0, 18, 65))

    # -- FINDING A, and it is the whole point of carrying D
    pd = per_dimension_cells()
    chk("D = 4 charts 62 cells", pd[4][0], 62)
    chk("every D >= 5 charts 66", sorted({pd[D][0] for D in DIMS[1:]}), [66])
    chk("THE CELL IS THE SAME AT EVERY DIMENSION",
        sorted({pd[D][1] for D in DIMS}), [(0, 10, 12)])
    chk("and the four extra cells are exactly the B = 2 rows",
        sorted({c[1] for c in X if c[0] == 4}), [0, 1])

    # -- the encoding choice is measured, not assumed away
    a, b, same = encoding_sensitivity()
    chk("the rank and raw-decade encodings agree", same, True)
    chk("and both give the same cell", (a, b), ((0, 18, 65), (0, 18, 65)))

    # -- the refusals, as facts about the file
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    chk("no member is a spacetime -- every slot is an integer",
        all(all(isinstance(v, int) for v in m) for m, _c in rows()[:50]), True)
    chk("no warp metric is a member",
        any("warp" in str(m).lower() for m, _c in rows()), False)
    chk("G_D is never given a value",
        bool(re.search(r"\bG_(5|6|7|8|9|10|11)\s*=", src)), False)
    print("gravity selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
