#!/usr/bin/env python3
r"""
observed.py -- THE SHELL FIBRATION AS NATURE FILLS IT, beside the one Madelung
predicts.  DOCKET 26, and M ruled BOTH.

    python3 observed.py             the reading
    python3 observed.py --selftest  fixtures

===============================================================================
0. THE DOCKET, AND WHAT THE OBJECTION TURNED OUT TO BE
===============================================================================

DOCKET 26 opened on a verification finding: `fibred.address` calls
`tools/populate.aufbau_config`, and that function's own docstring says

    "The configuration Madelung order predicts.  Register 1306 WITHDREW this
     table as the store's ground configurations -- 'that table was wrong at
     Pd ... and at Lr' -- but COORDINATES-2.13 was built on it, so reproducing
     the index as it stands requires it.  IT IS NEVER THE DEFAULT."

    READ CAREFULLY, THAT IS NOT A FAULT IN `fibred`.  The table was withdrawn
    as a source of OBSERVED ground configurations.  It remains exactly what it
    says it is -- what Madelung predicts -- and building the Madelung fibration
    out of it is the one correct use of it.  `fibred` and `madelung` are
    honestly labelled and they stay.

    WHAT WAS MISSING WAS THE OTHER OBJECT.  Nothing here charted the
    configurations nature actually shows.  M: "both".

===============================================================================
1. THE MEMBERS, AND WHERE THEY COME FROM
===============================================================================

One member is the (n, l, k) address of an element's DIFFERENTIATING ELECTRON,
read from register 1306's banked observed ground configurations --
`method/members/LW1-ground.py`, a SEATED MEMBER, loaded by path and never
copied.  k is the prior occupancy of the subshell, the 0-based slot the
electron takes; the same convention `fibred.address` uses, so the two charts
are comparable by construction.

    108 elements, 108 addresses, 98 DISTINCT CELLS.
    Reach Z <= 108, which is every element register 1306 banks.

    THE REACH IS WHERE OBSERVATION STOPS, NOT A COMPLETE UNIT, and that is
    said plainly.  `mi.py` section 3 has each chart reach "the last complete
    unit its own construction defines" -- a shell for Janet, a period for the
    periodic layout.  This construction's unit is an element someone has made
    and measured, so its reach is the banked table and M's ruling that the
    upper bound is open applies to it with full force.  `ions` is seated on
    the same footing.

===============================================================================
2. WHAT IT IS, AND HOW IT DIFFERS FROM THE PREDICTION
===============================================================================

                        cells   cell            channel
    observed  (n,l,k)      98   (0, 20, 13)     K0   closes NOTHING
    predicted (n,l,k)     108   (2, 21, 12)     K2   closes statistics
                                                     (at the matched reach
                                                      Z <= 108)
    predicted at its own reach of 170 electrons: 170 cells, (3, 26, 17), K3

    25 OF THE 108 ADDRESSES DIFFER.  Note that 20 of 108 CONFIGURATIONS
    differ -- the two counts are both right and they count different things:
    a configuration can differ while its differentiating electron does not,
    and one departure shifts the addresses of the elements after it.  The 20
    are exactly `madrule`'s twenty Madelung exceptions, an object this tree
    already seats, so the divergence is not an unknown quantity: it is the
    thing `madrule` indexes, seen from the other side.

    THE OBSERVED CHART HOLDS ONE CELL THE PREDICTION DOES NOT: (7, 1, 0).
    The prediction holds ELEVEN the observation does not, every one of them a
    d or f slot -- (3,2,4), (3,2,9), (4,2,3), (4,2,6), (4,2,9), (4,3,2),
    (4,3,8), (5,2,8), (5,3,1), (5,3,5), (5,3,8).  Those are slots the
    Madelung order fills in sequence and nature skips, which is why the
    observed chart has 98 cells against 108 addresses: ten addresses repeat.

    AND TWELVE ELEMENTS LOSE OCCUPANCY IN A SUBSHELL -- Cr, Cu, Nb, Ru, Pd,
    Pr, Tb, Pt, Pa, Pu, Bk, Rf.  Going from Z-1 to Z, a subshell that was
    occupied gives an electron up.  THE MADELUNG PREDICTION NEVER DOES THIS:
    its occupancies are monotone in Z by construction.  This is the sharpest
    physical difference between the two objects and it is invisible to either
    chart alone.

===============================================================================
3. THE REACH SWEEP, BY PERIOD
===============================================================================

    Z <=  10    10 cells   K7        Z <=  54    49 cells   K0
    Z <=  18    18 cells   K7        Z <=  86    78 cells   K0
    Z <=  36    34 cells   K2        Z <= 108    98 cells   K0

    THE CHANNEL SETTLES AT K0 FROM Z <= 54 AND NEVER MOVES AGAIN.  The two
    early K7s are degenerate -- at ten and eighteen cells the chart is a
    complete rectangle and closes everything for free, and the PREDICTED
    chart gives K7 at exactly the same two reaches, so that is a fact about
    small reaches rather than about either object.

    THE PREDICTION'S OWN SWEEP GOES K7, K7, K3, K3, K3, K2 -- it does not
    settle.  So the two charts disagree about their own stability as well as
    about their cells, and the observed one is the steadier of the two.

===============================================================================
4. WHY BOTH ARE SEATED, WHICH IS A RULING AND NOT A MEASUREMENT
===============================================================================

M, on DOCKET 26: "both".

    THE OVERLAP RULING'S FOUR GROUNDS GOVERN COARSENINGS, and this is not one:
    it is a DIFFERENT MEMBER SET at the same arity, 25 of 108 addresses apart
    from the prediction's, so `novel channel` does not apply to it any more
    than it applies to `terms` sharing K0 with `laws`.  What applies is the
    ordinary criterion -- its members are electrons and they carry (n, l, k) --
    and M's prohibition on seating the same information twice.

    IT IS NOT THE SAME INFORMATION, and the file measures that rather than
    asserting it: a different member set, a different cell, a different
    channel, and a difference set that is exactly `madrule`'s twenty
    exceptions plus the twelve occupancy losses the prediction cannot produce.

    WHAT THIS FILE REFUSES TO CONCLUDE: that the observed chart SUPERSEDES the
    predicted one.  It does not, and M's ruling is the reason -- both.  The
    prediction is what the Madelung rule says and it is right to chart it; the
    observation is what nature does; the twenty-five places they part are the
    finding neither holds alone.
"""

import importlib.util
import os
import sys

import hlaw
import mi

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    "Register 1306's banked observed ground configurations, a seated member loaded by path.",
    (
        'method/members/LW1-ground.py',
    ),
)


LW1 = "/home/user/Claude-Method-Works/method/members/LW1-ground.py"
REACH = 108
NAMES = ("n", "l", "k")
ARITY = len(NAMES)
_C = {}


def _lw1():
    """Register 1306's ground configurations.  IMPORTED BY PATH, never copied."""
    if "m" not in _C:
        spec = importlib.util.spec_from_file_location("lw1_ground", LW1)
        m = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(m)
        except SystemExit:          # the member prints and exits when run
            pass
        _C["m"] = m
    return _C["m"]


def config(Z):
    """{(n, l): occupancy} as register 1306 banks it."""
    return {(n, l): o for n, l, o in _lw1().expand(Z)}


def elements():
    """{Z: symbol} over the banked reach."""
    return {Z: v[0] for Z, v in sorted(_lw1().GROUND.items())}


def address(Z):
    """(n, l, k) of Z's OBSERVED differentiating electron, or None.

    Same convention as `fibred.address`: k is the prior occupancy of the
    subshell that gained.  Where more than one gains, the highest (n, l) is
    taken -- measured to happen ZERO times, which the selftest pins.
    """
    now, prev = config(Z), (config(Z - 1) if Z > 1 else {})
    g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
    if not g:
        return None
    n, l = g[-1]
    return (n, l, prev.get((n, l), 0))


def addresses(reach=REACH):
    return {Z: a for Z in sorted(_lw1().GROUND) if Z <= reach
            and (a := address(Z))}


def index(reach=REACH):
    """The observed shell fibration as a set of cells."""
    return frozenset(addresses(reach).values())


def losses(reach=REACH):
    """[(Z, symbol, [(n,l) that lost an electron])] -- the prediction never has any."""
    el, out = elements(), []
    for Z in sorted(_lw1().GROUND):
        if Z > reach or Z < 2:
            continue
        now, prev = config(Z), config(Z - 1)
        d = sorted((n, l) for (n, l), o in prev.items() if o > now.get((n, l), 0))
        if d:
            out.append((Z, el[Z], d))
    return out


def multi_gain(reach=REACH):
    """[(Z, the subshells that gained)] where MORE than one did.  Must be []."""
    out = []
    for Z in sorted(_lw1().GROUND):
        if Z > reach:
            continue
        now, prev = config(Z), (config(Z - 1) if Z > 1 else {})
        g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
        if len(g) > 1:
            out.append((Z, g))
    return out


def _predicted(reach=REACH):
    import fibred
    return fibred.addresses(reach)


def differing_addresses(reach=REACH):
    """[(Z, symbol, observed, predicted)] where the two charts disagree."""
    el, P, O = elements(), _predicted(reach), addresses(reach)
    return [(Z, el[Z], O[Z], P[Z]) for Z in sorted(O)
            if Z in P and O[Z] != P[Z]]


def differing_configs(reach=REACH):
    """[(Z, symbol)] where the CONFIGURATION disagrees -- madrule's exceptions."""
    sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
    import populate as pop
    el, out = elements(), []
    for Z in sorted(_lw1().GROUND):
        if Z > reach:
            continue
        if config(Z) != {(n, l): o for n, l, o in pop.aufbau_config(Z)}:
            out.append((Z, el[Z]))
    return out


def only_observed(reach=REACH):
    return sorted(index(reach) - frozenset(_predicted(reach).values()))


def only_predicted(reach=REACH):
    return sorted(frozenset(_predicted(reach).values()) - index(reach))


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


PERIODS = (10, 18, 36, 54, 86, 108)


def reach_sweep():
    """[(reach, cells, K)] by PERIOD -- section 3."""
    return [(r, len(index(r)), mi.K(index(r))) for r in PERIODS]


def predicted_sweep():
    """The same sweep on the prediction, for contrast."""
    import fibred
    return [(r, len(frozenset(fibred.addresses(r).values())),
             mi.K(frozenset(fibred.addresses(r).values()))) for r in PERIODS]


# ---------------------------------------------------------------------------

def report():
    X = index()
    print("=" * 74)
    print("THE OBSERVED SHELL FIBRATION -- what nature fills, not what "
          "Madelung predicts")
    print("=" * 74)
    print()
    print("DOCKET 26.  M: \"both\".")
    print()
    print("1. THE OBJECT.")
    print("   members      %d elements, register 1306's banked ground configs"
          % len(addresses()))
    print("   cells        %d" % len(X))
    print("   cell         %s" % (cell(),))
    print("   closes       %s" % (", ".join(closers()) or "NOTHING"))
    print("   source       %s" % LW1)
    print()
    print("2. AGAINST THE PREDICTION, AT THE MATCHED REACH Z <= 108.")
    P = frozenset(_predicted().values())
    print("   observed     %3d cells  K%d" % (len(X), mi.K(X)))
    print("   predicted    %3d cells  K%d" % (len(P), mi.K(P)))
    print("   addresses that differ       %d" % len(differing_addresses()))
    print("   configurations that differ  %d   (madrule's exceptions)"
          % len(differing_configs()))
    print("   cells only observed   %s" % (only_observed(),))
    print("   cells only predicted  %s" % (only_predicted(),))
    print()
    print("3. WHAT THE PREDICTION CANNOT DO: %d elements lose occupancy."
          % len(losses()))
    for Z, sym, d in losses():
        print("      %3d %-3s loses %s" % (Z, sym, d))
    print()
    print("4. THE REACH SWEEP, BY PERIOD.")
    print("   %-10s %18s   %18s" % ("reach", "observed", "predicted"))
    for (r, n, k), (_r2, n2, k2) in zip(reach_sweep(), predicted_sweep()):
        print("   Z <= %-5d %10d cells K%-2d %12d cells K%-2d"
              % (r, n, k, n2, k2))
    print()
    print("5. BOTH ARE SEATED.  That is M's ruling and not a measurement.")
    print("   This file does not conclude that the observation supersedes the")
    print("   prediction.  The twenty-five places they part are the finding")
    print("   neither chart holds alone.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("register 1306 banks 108 elements", len(_lw1().GROUND), 108)
    chk("every one yields a differentiating address", len(addresses()), 108)
    chk("NO element has two subshells gaining at once -- so the rule that "
        "takes the highest never fires", multi_gain(), [])
    chk("98 distinct cells", len(index()), 98)
    chk("arity 3", len(next(iter(index()))), 3)
    chk("it closes NOTHING", closers(), [])
    chk("cell", cell(), (0, 20, 13))

    # against the prediction
    P = frozenset(_predicted().values())
    chk("the prediction has 108 cells at the matched reach", len(P), 108)
    chk("the prediction closes statistics there", mi.K(P), 2)
    chk("25 ADDRESSES differ", len(differing_addresses()), 25)
    chk("20 CONFIGURATIONS differ -- a different count of a different thing",
        len(differing_configs()), 20)
    chk("and those 20 are exactly madrule's exceptions",
        [z for z, _s in differing_configs()],
        sorted(z for z, *_r in __import__("madrule").exceptions()))
    chk("one cell is observed and not predicted", only_observed(), [(7, 1, 0)])
    chk("eleven are predicted and not observed", len(only_predicted()), 11)
    chk("and every one of those eleven is a d or f slot",
        sorted({l for _n, l, _k in only_predicted()}), [2, 3])

    # the physical difference the prediction cannot produce
    L = losses()
    chk("twelve elements lose occupancy in a subshell", len(L), 12)
    chk("and they are these", [s for _z, s, _d in L],
        ["Cr", "Cu", "Nb", "Ru", "Pd", "Pr", "Tb", "Pt", "Pa", "Pu", "Bk",
         "Rf"])
    sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
    import populate as pop
    mono = []
    for Z in range(2, 109):
        now = {(n, l): o for n, l, o in pop.aufbau_config(Z)}
        prev = {(n, l): o for n, l, o in pop.aufbau_config(Z - 1)}
        if any(o > now.get(k, 0) for k, o in prev.items()):
            mono.append(Z)
    chk("THE PREDICTION LOSES OCCUPANCY NOWHERE -- monotone by construction",
        mono, [])

    # the sweep
    sw = reach_sweep()
    chk("six period reaches", len(sw), 6)
    chk("the channel settles at K0 from Z <= 54 and never moves",
        [k for r, _n, k in sw if r >= 54], [0, 0, 0])
    chk("the two early K7s are degenerate -- the PREDICTION gives K7 at the "
        "same two reaches",
        [k for r, _n, k in predicted_sweep() if r <= 18], [7, 7])

    # the ruling
    chk("it does NOT claim to supersede the prediction -- both are seated",
        "does not conclude that the observation supersedes" in
        open(__file__, encoding="utf-8").read(), True)
    print("observed selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
