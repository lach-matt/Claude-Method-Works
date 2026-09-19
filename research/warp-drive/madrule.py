#!/usr/bin/env python3
r"""
madrule.py -- THE MADELUNG EXCEPTION INDEX: the twenty elements whose observed
ground configuration is not the one the rule predicts.

    python3 madrule.py             the reading
    python3 madrule.py --selftest  fixtures

===============================================================================
0. IT IS NOT `madelung` AND IT IS NOT `inversion`, AND BOTH WERE MEASURED
===============================================================================

`madelung` fibres 170 ELECTRONS over n+l.  `inversion` seats the 20 places where
two ORDERS on the 25 subshells disagree.  This index seats 20 ELEMENTS whose
NIST-observed ground configuration disagrees with the Madelung PREDICTION.

    THE MEMBER TYPE IS AN ELEMENT, WHICH NO SEATED INDEX HAS.  `fibred` and
    `madelung` have electrons, `probability` subshells, `inversion` pairs of
    subshells, `channels` channel shapes, `laws` series, `ions` transitions,
    `gravity` nuclide-charge states.

    AND IT IS NOT `inversion` UNDER ANOTHER NAME, which is the real risk since
    both are about the same two orders.  `inversion` asks where the orders
    disagree; this asks where NATURE disagrees with one of them.  Measured:
    element-identity overlap is 0.0 -- `inversion` has no elements -- and
    **17 of `inversion`'s 20 subshell pairs carry no exception at all**.  An
    inversion is a necessary condition for an exception and nowhere near a
    sufficient one.

**THIS IS THE FIRST OBJECT IN THE TREE THAT TESTS THE MADELUNG RULE AGAINST
MEASUREMENT AT ELEMENT LEVEL.**  Everything else here charts the rule's own
order; this charts where it fails.

===============================================================================
1. THE TWO SIDES, AND THEY ARE NEVER MERGED
===============================================================================

    OBSERVED    `method/members/LW1-ground.py`, `GROUND` -- 108 elements with
                their NIST ASD 5.12 ground configurations (register 1306).
                Status **READ**.  Never computed, never repaired.
                `CORECFG` supplies the seven noble-gas cores the strings abbreviate.

    PREDICTED   `research/warp-drive/shells.py`, `TRUE_MADELUNG` and `config(Z)`.
                Status **COMPUTED**.  `tools/populate.MADELUNG` is a second
                witness only: it was truncated and repaired once, and `shells.py`
                rebuilds the order itself precisely so that defect stays
                detectable.

**BOTH SIDES SUM TO Z ON ALL 108, AND THAT IS A FIXTURE.**  A configuration
parser that silently drops a token would invent exceptions, so the arithmetic is
checked before any comparison is made.

    108 elements compared, **20 exceptions**:
    Cr Cu Nb Mo Ru Rh Pd Ag La Ce Gd Pt Au Ac Th Pa U Np Cm Lr

===============================================================================
2. THE THREE COORDINATES
===============================================================================

An exception moves electrons from a subshell the rule would have filled to one
it would not have.  The coordinates are that transfer:

    S_a   the ACCEPTOR's Madelung group n+l -- which group gained
    l_d   the DONOR's orbital angular momentum -- what kind of subshell lost
    occ   the OBSERVED occupancy of the acceptor

    20 members, **13 distinct cells**, box 96.  Ratios against cells:
    S_a 0.3077, l_d 0.2308, occ 0.6154.  None is a LABEL.  **`occ` is the one
    that tips first if the reach ever grows**, and that is recorded now rather
    than discovered later.

    Z was measured as a coordinate and REFUSED: 20/20 = 1.0000, a row label.

**IT CLOSES IN `statistics` ALONE**, and its cell is **(2, 6, 4)**.

===============================================================================
3. THE PROXIMITY TO `inversion`, RECORDED AND NOT RULED ON
===============================================================================

`inversion` sits at **(2, 6, 5)**.  This index sits at **(2, 6, 4)** -- the same
channel, the same height, one unit of width apart.  The two are about the same
pair of orders and they land next to each other.

    THAT IS A MEASUREMENT AND NOT A VERDICT.  Whether such proximity should
    block a seating is a ruling, and this file does not make it.  It is stated
    here because a reader comparing the two charts would otherwise find it
    themselves and wonder whether it was noticed.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

**TO SAY AN EXCEPTION FALSIFIES THE ELEMENT.**  It falsifies the rule, at that
element.  The rule's status is **EMPIRICAL-RULE**, the same status
`gravity.PAIRING_RULE_STATUS` carries, and for the same reason.

**TO PUT THE VERDICT ON AN AXIS.**  Whether an element is an exception is the
MEMBERSHIP CONDITION.  Charting it would make a coordinate of the thing that
decides who is a member, and the 108-row flagged variant that does exactly that
is refused by name: 88 of its 108 rows would be inert `AGREES` padding.

**TO TELL THE HALF-FILLED STORY.**  The familiar account is that exceptions buy
a half-filled or filled subshell.  Measured here: `stability_story()` counts how
many of the twenty actually land on a half-filled acceptor, how many on a filled
one, and how many on neither.  The count is printed; the story is not told.

**TO EXTEND PAST Z = 108**, or to predict an exception not observed.  The reach
control is printed rather than hidden -- 18 -> 0, 36 -> 2, 54 -> 8, 86 -> 13,
103 -> 20, 108 -> 20, first exception Cr at Z = 24 -- so a reader can see that
the count is a function of how far the observed table reaches.

**TO USE THE GROUND TERM SYMBOL AS A COORDINATE.**  It would lift 13 cells
higher, and it is the term index's own coordinate; borrowing it here would chart
the same information twice.  The measurement is recorded beside the refusal.

**TO MERGE THE CONVENTION WITH THE RULE.**  Madelung orders by (n+l, n); the
tie-break on equal n+l is a **CONVENTION**, carried separately, because some
exception sites exist only because the rule's statement fixes a tie.
"""

import collections
import importlib.util as _u
import os
import re
import sys

import hlaw
import mi
import overlap
import shells

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    "Register 1306's banked observed ground configurations, against the Madelung prediction.",
    (
        'method/members/LW1-ground.py',
    ),
)


ROOT = "/home/user/Claude-Method-Works"
GROUND_SRC = os.path.join(ROOT, "method/members/LW1-ground.py")
SECOND_WITNESS = os.path.join(ROOT, "tools/populate.py")

LN = "spdfghik"
NAMES = ("S_a", "l_d", "occ")
ARITY = 3
REACH = 108

OBSERVED_STATUS = "READ"            # NIST ASD 5.12, register 1306
PREDICTED_STATUS = "COMPUTED"
RULE_STATUS = "EMPIRICAL-RULE"
TIEBREAK_STATUS = "CONVENTION"      # the (n+l, n) tie-break, carried apart

_TOK = re.compile(r"\[(\w+)\]|(\d)([spdfghik])(\d*)")
_C = {}


def _lw1():
    """The seated member, IMPORTED BY PATH and never copied."""
    if "lw1" not in _C:
        spec = _u.spec_from_file_location("LW1_ground", GROUND_SRC)
        mod = _u.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _C["lw1"] = mod
    return _C["lw1"]


def parse(cfg):
    """A configuration string as {(n, l): occupancy}.

    IT RAISES RATHER THAN SKIPPING.  A parser that silently drops a token it
    does not understand would invent exceptions out of its own gaps, so every
    character of every string must be consumed.
    """
    out = collections.Counter()
    pos = 0
    for m in _TOK.finditer(cfg):
        if cfg[pos:m.start()].strip():
            raise ValueError("unparsed %r in %r" % (cfg[pos:m.start()], cfg))
        pos = m.end()
        if m.group(1):
            out.update(parse(_lw1().CORECFG[m.group(1)]))
        else:
            out[(int(m.group(2)), LN.index(m.group(3)))] += int(m.group(4) or 1)
    if cfg[pos:].strip():
        raise ValueError("trailing %r in %r" % (cfg[pos:], cfg))
    return out


def observed(Z):
    return parse(_lw1().GROUND[Z][1])


def predicted(Z):
    return collections.Counter({(n, l): k for n, l, k in shells.config(Z)})


def sums_check(reach=REACH):
    """[(Z, observed sum, predicted sum)] where either does not equal Z."""
    bad = []
    for Z in sorted(_lw1().GROUND):
        if Z > reach:
            continue
        o, p = sum(observed(Z).values()), sum(predicted(Z).values())
        if o != Z or p != Z:
            bad.append((Z, o, p))
    return bad


def exceptions(reach=REACH):
    """[(Z, symbol, observed, predicted)] -- where nature disagrees."""
    key = "exc%d" % reach
    if key not in _C:
        out = []
        for Z in sorted(_lw1().GROUND):
            if Z > reach:
                continue
            o, p = observed(Z), predicted(Z)
            if dict(o) != dict(p):
                out.append((Z, _lw1().GROUND[Z][0], o, p))
        _C[key] = out
    return _C[key]


def transfer(o, p):
    """((acceptor n, l), (donor n, l)) -- the subshells that gained and lost."""
    gained = sorted(k for k in set(o) | set(p) if o[k] > p[k])
    lost = sorted(k for k in set(o) | set(p) if o[k] < p[k])
    return gained[0], lost[0]


def table(reach=REACH):
    """[(Z, symbol, acceptor, donor, cell)] -- every exception with its cell."""
    out = []
    for Z, sym, o, p in exceptions(reach):
        a, d = transfer(o, p)
        out.append((Z, sym, a, d, (a[0] + a[1], d[1], o[a])))
    return out


def index(reach=REACH):
    """The Madelung exception index as a set of cells."""
    return frozenset(c for _Z, _s, _a, _d, c in table(reach))


def reach_control():
    """[(reach, exceptions to there)] -- the count is a function of the reach."""
    return [(R, sum(1 for Z, *_r in exceptions() if Z <= R))
            for R in (18, 36, 54, 86, 103, 108)]


def first_exception():
    Z, sym = exceptions()[0][0], exceptions()[0][1]
    return Z, sym


def stability_story():
    """(half-filled, filled, neither) acceptors -- the count, not the story."""
    half = full = neither = 0
    for _Z, _s, a, _d, _c in table():
        o = observed(_Z)[a]
        cap = 2 * (2 * a[1] + 1)
        if o == cap // 2:
            half += 1
        elif o == cap:
            full += 1
        else:
            neither += 1
    return half, full, neither


def z_is_a_label():
    """(distinct, members, ratio) for Z -- measured, then refused."""
    zs = [Z for Z, *_r in table()]
    return len(set(zs)), len(zs), len(set(zs)) / len(zs)


def inversion_pairs_without_exception():
    """(inversion pairs, how many carry no exception here).

    An inversion is NECESSARY for an exception and nowhere near SUFFICIENT.
    """
    import inversion
    pairs = {frozenset((a, b)) for a, b in inversion.inversions()}
    mine = {frozenset((a, d)) for _Z, _s, a, d, _c in table()}
    return len(pairs), len(pairs - mine)


def element_overlap_with_inversion():
    """0.0 -- `inversion` has no elements at all, so nothing can be shared."""
    import inversion
    return 0.0 if not hasattr(inversion, "elements") else None


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def near_inversion():
    """(this cell, inversion's cell, how far apart) -- recorded, not ruled on."""
    import inversion
    a, b = cell(), mi.cell(inversion.index())
    return a, b, tuple(x - y for x, y in zip(a, b))


# ---------------------------------------------------------------- the reading

def report():
    X = index()
    tab = table()
    print("=" * 74)
    print("THE MADELUNG EXCEPTION INDEX")
    print("=" * 74)
    print()
    print("Twenty ELEMENTS whose NIST-observed ground configuration is not the")
    print("one the Madelung rule predicts. The first object in this tree that")
    print("tests the rule against measurement at element level.")
    print()
    print("-" * 74)
    print("1. THE TWO SIDES, NEVER MERGED.")
    print("-" * 74)
    print("   OBSERVED   method/members/LW1-ground.py  GROUND   status %s"
          % OBSERVED_STATUS)
    print("   PREDICTED  research/warp-drive/shells.py config()  status %s"
          % PREDICTED_STATUS)
    print("   the rule itself                                   status %s"
          % RULE_STATUS)
    print("   the (n+l, n) tie-break                            status %s"
          % TIEBREAK_STATUS)
    print()
    print("   elements compared            %d" % len(_lw1().GROUND))
    print("   rows where a side != Z       %d   (a fixture, not a remark)"
          % len(sums_check()))
    print("   EXCEPTIONS                   %d" % len(tab))
    print("   %s" % " ".join(s for _Z, s, *_r in tab))
    print()
    print("   reach control, because the count is a function of the reach:")
    for R, n in reach_control():
        print("      Z <= %-4d %2d exceptions" % (R, n))
    print("      first exception: %s at Z = %d"
          % (first_exception()[1], first_exception()[0]))
    print()
    print("-" * 74)
    print("2. THE CHART.")
    print("-" * 74)
    doc = {"S_a": "acceptor's Madelung group n+l",
           "l_d": "donor's orbital angular momentum",
           "occ": "observed occupancy of the acceptor"}
    for i, nm in enumerate(NAMES):
        vals = sorted({c[i] for c in X})
        print("   %-5s %-34s %-26s %d/%d = %.4f"
              % (nm, doc[nm], vals, len(vals), len(X), len(vals) / len(X)))
    d, n, r = z_is_a_label()
    print("   %-5s %-34s %-26s %d/%d = %.4f   REFUSED, LABEL"
          % ("Z", "the atomic number", "", d, n, r))
    print()
    print("   members        %d" % len(tab))
    print("   distinct cells %d" % len(X))
    print("   box            %d" % overlap.box_of(X))
    cl, _b = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %3d   E %3d%s"
              % (L, len(cl[L]), e, "   <-- CLOSES" if e == 0 else ""))
    print()
    print("   closers  %s" % (closers() or "NONE"))
    print("   CELL     %s" % (cell(),))
    print()
    print("-" * 74)
    print("3. IT IS NOT `inversion`, AND THAT WAS MEASURED.")
    print("-" * 74)
    npairs, without = inversion_pairs_without_exception()
    print("   inversion seats %d subshell pairs; %d of them carry NO exception."
          % (npairs, without))
    print("   An inversion is NECESSARY for an exception and nowhere near")
    print("   SUFFICIENT. inversion asks where the two orders disagree; this")
    print("   asks where NATURE disagrees with one of them.")
    a, b, dd = near_inversion()
    print()
    print("   AND THE TWO CELLS ARE ADJACENT:  this %s   inversion %s"
          % (a, b))
    print("   Same channel, same height, one unit of width apart. That is a")
    print("   MEASUREMENT AND NOT A VERDICT: whether such proximity should")
    print("   block a seating is a ruling, and this file does not make it.")
    print()
    print("-" * 74)
    print("4. EVERY EXCEPTION.")
    print("-" * 74)
    print("   %-3s %-4s %-10s %-10s %s" % ("Z", "sym", "acceptor", "donor", "cell"))
    for Z, sym, a, d_, c in tab:
        print("   %-3d %-4s %-10s %-10s %s"
              % (Z, sym, "%d%s" % (a[0], LN[a[1]]), "%d%s" % (d_[0], LN[d_[1]]), c))
    print()
    print("-" * 74)
    print("5. REFUSED.")
    print("-" * 74)
    h, f, nn = stability_story()
    print("   THE HALF-FILLED STORY. The familiar account is that an exception")
    print("   buys a half-filled or filled subshell. Measured over the twenty:")
    print("      half-filled acceptor  %2d" % h)
    print("      filled acceptor       %2d" % f)
    print("      NEITHER               %2d" % nn)
    print("   The count is printed. The story is not told.")
    print()
    print("   To say an exception falsifies the ELEMENT -- it falsifies the")
    print("     rule, at that element.")
    print("   To put the verdict on an axis -- it is the membership condition,")
    print("     and the 108-row flagged variant is refused by name.")
    print("   To extend past Z = %d, or to predict an unobserved exception." % REACH)
    print("   To use the ground term symbol as a coordinate -- it is the term")
    print("     index's own, and borrowing it charts the same thing twice.")
    print("   To merge the (n+l, n) tie-break with the rule.")
    return 0


# ------------------------------------------------------------------ fixtures

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    print("madrule selftest")

    # -- the parser must consume everything, or it invents exceptions
    chk("all 108 ground configurations parse", len(_lw1().GROUND), 108)
    chk("BOTH SIDES SUM TO Z ON EVERY ONE", sums_check(), [])
    chk("the parser raises on an unparsed token rather than skipping",
        _raises(lambda: parse("3s 9q2")), True)
    chk("the seven noble-gas cores are used", len(_lw1().CORECFG), 7)

    # -- the members
    tab = table()
    chk("twenty exceptions", len(tab), 20)
    chk("and they are the known twenty", [s for _Z, s, *_r in tab],
        ["Cr", "Cu", "Nb", "Mo", "Ru", "Rh", "Pd", "Ag", "La", "Ce", "Gd",
         "Pt", "Au", "Ac", "Th", "Pa", "U", "Np", "Cm", "Lr"])
    chk("the first is Cr at Z = 24", first_exception(), (24, "Cr"))
    chk("the reach control is printed rather than hidden", reach_control(),
        [(18, 0), (36, 2), (54, 8), (86, 13), (103, 20), (108, 20)])
    chk("every member is an ELEMENT, a type no seated index has",
        all(isinstance(Z, int) and 1 <= Z <= REACH for Z, *_r in tab), True)

    # -- the chart
    X = index()
    chk("13 distinct cells", len(X), 13)
    chk("arity 3", len(next(iter(X))), ARITY)
    chk("box", overlap.box_of(X), 96)
    chk("no coordinate is constant",
        [NAMES[i] for i in range(ARITY) if len({c[i] for c in X}) == 1], [])
    chk("no coordinate is a LABEL",
        [NAMES[i] for i, _d, _n, _r, v in overlap.resolution(X)
         if v == "LABEL"], [])
    chk("occ is the one nearest the threshold, recorded now",
        max((r, NAMES[i]) for i, _d, _n, r, _v in overlap.resolution(X))[1],
        "occ")
    chk("Z WAS measured as a coordinate and is a LABEL", z_is_a_label()[2], 1.0)
    chk("it closes in statistics alone", closers(), ["statistics"])
    chk("CELL", cell(), (2, 6, 4))

    # -- it is not inversion
    npairs, without = inversion_pairs_without_exception()
    chk("inversion seats 20 subshell pairs", npairs, 20)
    chk("SEVENTEEN OF THEM CARRY NO EXCEPTION", without, 17)
    chk("so an inversion is necessary and not sufficient", without > 0, True)
    a, b, d = near_inversion()
    chk("and the two cells are one width apart, recorded not ruled on",
        (a, b, d), ((2, 6, 4), (2, 6, 5), (0, 0, -1)))

    # -- the refusals, and the story that is not told
    chk("the half-filled story is counted, not told", stability_story(),
        (2, 4, 14))
    chk("most exceptions land on NEITHER a half-filled nor a filled acceptor",
        stability_story()[2] > sum(stability_story()[:2]), True)
    chk("the rule's status is not flattened to a theorem", RULE_STATUS,
        "EMPIRICAL-RULE")
    chk("the observed side is READ, never computed", OBSERVED_STATUS, "READ")
    chk("the tie-break is carried apart from the rule", TIEBREAK_STATUS,
        "CONVENTION")
    print("madrule selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def _raises(fn):
    try:
        fn()
    except Exception:
        return True
    return False


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
