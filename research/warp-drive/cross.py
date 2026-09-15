#!/usr/bin/env python3
r"""
cross.py -- THE INTERSECTION INDEX: every pair of axes, measured against each
other, and the pairs where information sits that neither axis carries alone.

M: "Indexes can also be found by comparing measurements of axis to the axis it
intersects. Not just from the chats and previous works. You can identify more by
what is in front of you... This is a hunt for unidentified data contained
within."

    python3 cross.py             the reading
    python3 cross.py --selftest  fixtures

===============================================================================
0. THE MEMBER IS A PAIR OF AXES, WHICH IS A KIND NOTHING HERE HAS CHARTED
===============================================================================

`axes.py` charts the twenty-six axes as members -- the ways we know things.  This
charts their INTERSECTIONS: for every unordered pair (a, b), what the two of them
say together over the elements where both are defined.

    THAT IS A DIFFERENT MEMBER SET, NOT A RE-CHART.  `charts3.py` proved that
    rearranging the element address reaches no new channel; the way past it is a
    new kind of member.  An axis pair is one: 190 members from 20 axes, and none
    of them is an element, a measurement, or an index.

===============================================================================
1. THE THREE COORDINATES, AND THE THIRD IS THE HUNT
===============================================================================

Over the elements where both axes are defined:

        support   how many elements carry both
        pair      how many distinct (a, b) values occur
        gain      pair - max(distinct a, distinct b)

    GAIN IS THE MEASUREMENT M ASKED FOR.  It is how much the intersection
    separates elements BEYOND what either axis separates alone.

        gain = 0   one axis determines the other on this support, or they are
                   redundant.  The intersection carries nothing new.
        gain > 0   the pair distinguishes elements that NEITHER axis
                   distinguishes.  That is information held at the
                   intersection and nowhere else.

    `gain` is non-negative by construction -- the pair refines both projections
    -- and `gain_is_nonnegative()` checks that over every pair rather than
    asserting it.

===============================================================================
2. WHAT IS COMPARED, AND WHAT IS REFUSED
===============================================================================

`populate()` returns twenty keys per element.  Five of them are STRUCTURED --
lists and dicts of per-subshell or per-transition rows -- and comparing a dict to
an integer is not a measurement of anything.  Those five are compared by their
canonical JSON form, which is exact and order-stable, and `structured()` names
them so the reader knows which comparisons are on a serialisation.

    TWO AXES ARE ALWAYS None IN THIS SPREAD -- `limit_deficit` and
    `series_limit` are not populated for a neutral atom at this reach.  An axis
    that is None everywhere has one distinct value and a support of zero with
    anything; `dead_axes()` names them and they are kept, because an axis that
    says nothing is a fact about the corpus and not a row to hide.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

To call a high gain a discovery.  It is a place to look: the pair separates
elements neither axis does, and WHY is a question for whoever reads the rows.
`top_gains()` prints the pairs and nothing else.

To read gain as correlation.  It counts distinct values, not agreement, and two
axes can have a large gain while being unrelated -- that is what a large gain
usually means.  Nothing here is a statistical claim.

To extend past the seated reach.  The spread is the elements `populate` answers
for, and `REACH` names it.
"""

import itertools
import json
import sys

sys.path.insert(0, "/home/user/Claude-Method-Works/tools")

import hlaw
import mi
import populate as _pop

REACH = 118
_CACHE = {}


def rows(reach=REACH):
    """{Z: {axis: value}} over the spread, computed once."""
    if reach not in _CACHE:
        sp = _pop.Spectra(_pop.DEFAULT_SPECTRA)
        out = {}
        for Z in range(1, reach + 1):
            try:
                out[Z] = _pop.populate(Z, sp, charge=1)
            except Exception:                      # an element populate declines
                continue
        _CACHE[reach] = out
    return _CACHE[reach]


def axes(reach=REACH):
    """The axis names populate actually returns, sorted."""
    r = rows(reach)
    return sorted(next(iter(r.values())))


def _key(v):
    """A hashable, order-stable form.  Structured values go through JSON."""
    if isinstance(v, (int, float, str, bool, type(None))):
        return v
    return json.dumps(v, sort_keys=True, default=str)


def structured(reach=REACH):
    """The axes whose values are lists or dicts, named rather than hidden."""
    r = rows(reach)
    one = next(iter(r.values()))
    return sorted(k for k, v in one.items() if isinstance(v, (list, dict)))


def dead_axes(reach=REACH):
    """Axes that are None for every element in the spread."""
    r = rows(reach)
    return sorted(a for a in axes(reach)
                  if all(d.get(a) is None for d in r.values()))


def support(a, b, reach=REACH):
    """Elements where both axes are defined."""
    r = rows(reach)
    return [Z for Z, d in r.items()
            if d.get(a) is not None and d.get(b) is not None]


def measure(a, b, reach=REACH):
    """(support, distinct pairs, gain) for one intersection."""
    r = rows(reach)
    zs = support(a, b, reach)
    va = {_key(r[Z][a]) for Z in zs}
    vb = {_key(r[Z][b]) for Z in zs}
    vp = {(_key(r[Z][a]), _key(r[Z][b])) for Z in zs}
    return len(zs), len(vp), len(vp) - max(len(va), len(vb), 0)


def table(reach=REACH):
    """[(a, b, support, pair, gain)] over every unordered pair."""
    return [(a, b) + measure(a, b, reach)
            for a, b in itertools.combinations(axes(reach), 2)]


def index(reach=REACH):
    """The intersection index as a set of cells."""
    return frozenset((s, p, g) for _a, _b, s, p, g in table(reach))


def gain_is_nonnegative(reach=REACH):
    """[(a, b, gain)] for any pair with gain < 0.  Must be empty.

    The pair refines both projections, so it cannot separate LESS than either.
    Checked over every pair rather than argued.
    """
    return [(a, b, g) for a, b, _s, _p, g in
            [(x, y, s, p, g) for x, y, s, p, g in table(reach)] if g < 0]


def determines(reach=REACH):
    """[(a, b)] where gain is zero on a non-empty support -- one fixes the other."""
    return [(a, b) for a, b, s, _p, g in table(reach) if g == 0 and s > 0]


def top_gains(n=12, reach=REACH):
    """The pairs holding the most information neither axis holds alone."""
    return sorted(table(reach), key=lambda t: (-t[4], t[0], t[1]))[:n]


def criterion(reach=REACH):
    X = index(reach)
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def closers(reach=REACH):
    X = index(reach)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(reach=REACH):
    return mi.cell(index(reach))


# ---------------------------------------------------------------------------

def report():
    t = table()
    print("=" * 74)
    print("THE INTERSECTION INDEX -- every pair of axes, measured against")
    print("each other")
    print("=" * 74)
    print()
    print("1. THE MEMBERS.")
    print("   elements in the spread   %d" % len(rows()))
    print("   axes populate returns    %d" % len(axes()))
    print("   PAIRS                    %d" % len(t))
    print("   distinct cells           %d" % len(index()))
    print("   structured axes (compared by canonical JSON): %s"
          % ", ".join(structured()))
    print("   axes that are None throughout: %s"
          % (", ".join(dead_axes()) or "none"))
    print()
    print("2. GAIN IS NON-NEGATIVE, CHECKED NOT ARGUED.")
    bad = gain_is_nonnegative()
    print("   pairs with gain < 0: %d   %s" % (len(bad), bad[:3] if bad else ""))
    if bad:
        print("   THE MEASUREMENT IS WRONG. Everything below is void.")
        return 1
    print()
    print("3. WHERE THE INFORMATION IS -- the pairs that separate elements")
    print("   NEITHER axis separates.")
    print("   %-22s %-22s %-8s %-7s %s"
          % ("axis", "intersects", "support", "pairs", "GAIN"))
    for a, b, s, p, g in top_gains():
        print("   %-22s %-22s %-8d %-7d %d" % (a, b, s, p, g))
    print()
    det = determines()
    print("4. AND WHERE THERE IS NONE: %d pairs have gain 0 on a non-empty"
          % len(det))
    print("   support -- one axis fixes the other, or they are redundant.")
    for a, b in det[:6]:
        print("   %-22s determines or is determined by %s" % (a, b))
    print()
    print("5. THE CHART CRITERION (DOCKET 3) AND WHERE IT LANDS.")
    crit = criterion()
    for nm in sorted(crit):
        print("   %-8s moves on %d" % (nm, crit[nm]))
    if any(crit.values()):
        print("   A COORDINATE MOVED. The reading below is void.")
        return 1
    print("   closes   %s" % (", ".join(closers()) or "nothing"))
    print("   CELL     %s" % (cell(),))
    print()
    print("6. REFUSED: to call a high gain a discovery -- it is a place to")
    print("   look, and WHY is a question for whoever reads the rows. To read")
    print("   gain as correlation: it counts distinct values, not agreement,")
    print("   and two unrelated axes usually have a LARGE gain. To extend past")
    print("   the seated reach.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    r = rows()
    chk("the spread is populated", len(r) > 100, True)
    A = axes()
    chk("populate returns twenty axes", len(A), 20)
    chk("Z is one of them", "Z" in A, True)
    chk("and so is the Janet cell", "janet_cell" in A, True)
    t = table()
    chk("every unordered pair is measured", len(t), len(A) * (len(A) - 1) // 2)
    chk("GAIN IS NEVER NEGATIVE", gain_is_nonnegative(), [])
    chk("some pair has positive gain", any(g > 0 for *_x, g in t), True)
    chk("some pair has zero gain", any(g == 0 for *_x, g in t), True)
    # Z is injective, so it determines everything on its support
    zg = [(b, g) for a, b, _s, _p, g in t if a == "Z"]
    chk("Z determines every axis it meets -- gain 0 throughout",
        [b for b, g in zg if g != 0], [])
    chk("and it meets most of them", len(zg) > 10, True)
    # a dead axis has empty support with everything
    dead = dead_axes()
    chk("two axes are None throughout this spread", len(dead), 2)
    chk("limit_deficit is one", "limit_deficit" in dead, True)
    chk("a dead axis has zero support with everything",
        {s for a, b, s, _p, _g in t if a in dead or b in dead}, {0})
    chk("structured axes are named", len(structured()) >= 4, True)
    chk("the key of a dict is order-stable",
        _key({"b": 1, "a": 2}), _key({"a": 2, "b": 1}))
    chk("the key of a scalar is itself", _key(7), 7)
    crit = criterion()
    chk("K admissible", crit["K"], 0)
    chk("height admissible", crit["height"], 0)
    chk("width admissible", crit["width"], 0)
    c = cell()
    chk("the cell is a 3-tuple", len(c), 3)
    chk("height and width bound the size",
        max(c[1], c[2]) <= len(index()) <= c[1] * c[2], True)
    print("cross selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
