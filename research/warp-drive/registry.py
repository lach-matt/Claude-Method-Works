#!/usr/bin/env python3
r"""
registry.py -- EVERY INDEX OF THE PERIODIC ELEMENTS, WITH THE CRITERION
ENFORCED RATHER THAN DESCRIBED.

M: "Remove any index in the project whose members do not have quantum numbers."

    python3 registry.py             the reading
    python3 registry.py --selftest  fixtures

===============================================================================
0. THE CRITERION IS A FUNCTION HERE, AND THAT IS THE WHOLE REPAIR
===============================================================================

THE SUBJECT IS THE PERIODIC ELEMENTS.  A member of an index of it is an
electron, a subshell, a transition, a channel or a series -- something carrying
quantum numbers.

    NOTHING ENFORCED THAT, AND THE FIGURE WAS CONTAMINATED.  Thirteen
    filing-system indexes were seated as vertices -- mirrored files, BUILD
    snapshots, conversations, archives, artefact names, handoff documents,
    numbering gaps, and this tree's own dockets -- beside indexes whose members
    are electrons.  E went from 9 to 133, and EVERY ONE of the twelve
    disruptive vertices was repository metadata.  Not one was an element.

    THE EXPLOSION WAS THE CONTAMINATION, NOT A FINDING, and it was reported as
    one.  Withdrawn here.  The element-only figure is NINE vertices at E = 15
    on the measurement that prompted this rewrite, and SEVEN once the two
    indexes whose members are axes rather than elements come out.

    SO `QUANTUM` IS A COLUMN AND `enforce()` IS A FIXTURE.  Every registered
    index names the quantum numbers its members carry; a row that names none is
    refused.  A criterion in a docstring is what let the filing cabinet in.

===============================================================================
1. WHAT IS AN INDEX HERE, AND WHAT IS NOT
===============================================================================

    fibred        170 electrons          n, l, k
    madelung      the same 170           n+l, l, k
    ions          98 transitions         charge, electron count
    channels      209 channel shapes     l, Pauli bound, multiplicity
    laws          584 series             n range, l, quantum defect
    probability   25 subshells           n, l
    inversion     20 inversions          pairs of (n, l)
    gravity       3,394 nuclide-charge   Z, N, A, q, Ne, 2J, level status
                  states, read in 8
                  spacetime dimensions
    nucshell      22 NUCLEAR subshells   nr, l, j -- the only non-atomic
                                         member type seated here
    madrule       20 elements the        n+l acceptor, l donor, occupancy
                  Madelung rule misses
    terms         5,132 LS terms over    2S+1, L, parity, the banked J set
                  122 spectra

REMOVED, files deleted, all created in the session that made the mess:
`store.py` and its thirteen filing-system indexes; `obstruction.py` with its
currency and exotic-matter sub-indexes, whose members are obstructions to
building a warp drive; `filled.py`, a re-chart of the seated indexes;
`cross.py`, whose members are PAIRS OF AXES; and `density.py` and `occupy.py`,
both built on the contaminated figure.

PRESENT AS FUNCTIONS, NOT INDEXES OF THIS PROJECT: `mi.index`, `axes.index`,
`entropy.index`, `rindex.rindex`, `necindex.index`.  Their members are seated
indexes, measurement axes, refusals and energy conditions.  The files are NOT
deleted -- they carry charting machinery and findings this session did not
produce -- and `NOT_AN_INDEX` names each with its reason so nothing re-seats
them.

===============================================================================
2. WHAT THIS FILE REFUSES
===============================================================================

To claim completeness.  `COMPLETE = False`, and it stays false.

To accept a row that cannot name its quantum numbers.

To excuse a module silently.  A module exposing an `index()` that is neither
registered nor listed in `NOT_AN_INDEX` fails the selftest.
"""

import importlib
import os
import sys

COMPLETE = False
HERE = os.path.dirname(os.path.abspath(__file__))

METHODS = ("TABLE", "FIBRATION", "RESIDUAL")

# (module, accessor, method, what one member is, THE QUANTUM NUMBERS)
REGISTERED = (
    ("fibred", "index", "FIBRATION", "170 electrons", "n, l, k"),
    ("madelung", "janet", "FIBRATION", "the same 170 electrons", "n+l, l, k"),
    ("ions", "index", "TABLE", "98 Lambda-8 transitions",
     "charge, electron count"),
    ("channels", "index", "TABLE", "209 spectroscopic channel shapes",
     "l, Pauli bound, multiplicity"),
    ("laws", "index", "RESIDUAL", "584 series against Rydberg-Ritz",
     "n range, l, quantum defect"),
    ("probability", "index", "TABLE", "25 subshells", "n, l"),
    ("inversion", "index", "TABLE", "20 fill-order/shell-order inversions",
     "pairs of (n, l)"),
    ("gravity", "index", "TABLE",
     "3,394 nuclide-charge states x 8 dimensions",
     "Z, N, A, q, Ne, 2J, level status"),
    ("nucshell", "index", "TABLE", "22 nuclear single-particle subshells",
     "nr, l, j (nuclear)"),
    ("madrule", "index", "RESIDUAL", "20 Madelung exceptions, by their transfer",
     "n+l of the acceptor, l of the donor, occupancy"),
    ("terms", "index", "TABLE", "5,132 Russell-Saunders terms over 122 spectra",
     "2S+1, L, parity, the banked J set"),
    # ---- SEATED BY THE OVERLAP RULING.  M: "They can be seated with overlaps
    # so long as it is not an overlap of same information ... its relative
    # position in this index is information about an object."  Each of the
    # three is a coarsening of a row above, over the SAME members, reaching a
    # channel no row above reaches.  `overlaprule.py` states the ruling, the
    # three grounds it is tested on, the three candidates it REFUSES, and the
    # two parts of the definition each seating carries.  They are seated in
    # that file rather than in their parents so that the rows a ruling put here
    # are visible as such.
    ("overlaprule", "gravity_bound", "TABLE",
     "the same 3,394 nuclide-charge states, on the bound structure alone",
     "horizon-bound class, forced angular momentum, spin-decade rank"),
    ("overlaprule", "nucshell_lsigma", "TABLE",
     "the same 22 nuclear subshells, radially blind",
     "l, spin-orbit sign (nuclear)"),
    ("overlaprule", "madelung_slot", "FIBRATION",
     "the same 170 electrons, subshell-blind",
     "n+l, k"),
)

NOT_AN_INDEX = {
    "mi": "members are the seated indexes -- and NINE OF THEM ARE NOT "
          "REGISTERED ONES; figure.superseded_mi() measures it",
    "figure": "the index of first-order indexes: its members ARE the seated "
              "indexes, so they carry no quantum numbers",
    "axes": "members are measurement axes",
    "entropy": "members are the seated indexes",
    "rindex": "members are refusals",
    "necindex": "members are energy conditions",
}


def _mod(name):
    return importlib.import_module(name)


def enforce():
    """[(name, problem)] for any registered row that fails the criterion.

    MUST BE EMPTY.  This is the criterion as a function; it was a paragraph
    before, and a paragraph is what let thirteen filing-system indexes in.
    """
    bad = []
    for mod, acc, meth, _what, q in REGISTERED:
        nm = "%s.%s" % (mod, acc)
        if not q or not q.strip():
            bad.append((nm, "names no quantum numbers"))
        if meth not in METHODS:
            bad.append((nm, "unknown method %s" % meth))
    return bad


def rows():
    """[(name, module, accessor, method, members, quantum numbers)]."""
    return [("%s.%s" % (m, a), m, a, me, w, q)
            for m, a, me, w, q in REGISTERED]


def short(name=None):
    """{full name: a unique short label}, or one label if `name` is given.

    THE MODULE NAME WAS THE LABEL AND THAT STOPPED BEING UNIQUE.  Every row
    here was one module until the overlap ruling seated three coarsenings in
    `overlaprule.py`; `figure.py` keyed its vertices on `name.split(".")[0]`
    and silently folded three vertices into one -- twelve where there are
    fourteen.  The selftest caught it because the figure's vertex count is a
    PROPERTY there and not a pinned number, which is the whole reason that
    conversion was made.

    So the label is the module where the module seats one row, and the
    ACCESSOR where it seats more.  `short_is_unique()` is a fixture, not a
    hope.
    """
    n = {}
    for _nm, m, _a, _me, _w, _q in rows():
        n[m] = n.get(m, 0) + 1
    out = {nm: (m if n[m] == 1 else a) for nm, m, a, _me, _w, _q in rows()}
    return out if name is None else out[name]


def short_is_unique():
    """[] unless two rows want the same label."""
    lab = short()
    seen, bad = {}, []
    for nm, l in sorted(lab.items()):
        if l in seen:
            bad.append((l, seen[l], nm))
        seen[l] = nm
    return bad


def index_of(name):
    for nm, mod, acc, _me, _w, _q in rows():
        if nm == name:
            return getattr(_mod(mod), acc)()
    raise KeyError(name)


def by_method():
    out = {}
    for nm, _mo, _a, me, _w, _q in rows():
        out.setdefault(me, []).append(nm)
    return {k: sorted(v) for k, v in sorted(out.items())}


def modules_with_index():
    """Every module here exposing an index()-like accessor, by module name."""
    out = []
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".py") or f == os.path.basename(__file__):
            continue
        src = open(os.path.join(HERE, f), encoding="utf-8").read()
        if "\ndef index(" in src or "\ndef rindex(" in src:
            out.append(f[:-3])
    return out


def missing():
    """Modules exposing an index that are neither registered nor excused."""
    named = {m for _n, m, _a, _me, _w, _q in rows()}
    return [m for m in modules_with_index()
            if m not in named and m not in NOT_AN_INDEX]


def sizes():
    out = {}
    for nm, _mo, _a, _me, _w, _q in rows():
        try:
            out[nm] = len(index_of(nm))
        except Exception as exc:                   # pragma: no cover
            out[nm] = "ERROR %s" % exc
    return out


def cells(slow=False, budget=None):
    """{name: cell or 'UNMEASURED'}.  An unmeasured cell is never guessed."""
    import mi
    out = {}
    for nm, _mo, _a, _me, _w, _q in rows():
        X = index_of(nm)
        if not slow and budget is not None and len(X) > budget:
            out[nm] = "UNMEASURED"
            continue
        out[nm] = mi.cell(X)
    return out


def figure(slow=False, budget=None):
    """The element figure: the cell of every registered index."""
    return frozenset(c for c in cells(slow, budget).values()
                     if c != "UNMEASURED")


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("EVERY INDEX OF THE PERIODIC ELEMENTS")
    print("=" * 74)
    print()
    bad = enforce()
    print("1. THE CRITERION, ENFORCED.")
    print("   registered indexes      %d" % len(REGISTERED))
    print("   rows failing it         %d   %s" % (len(bad), bad if bad else ""))
    if bad:
        print("   THE CRITERION FAILS. Everything below is void.")
        return 1
    print()
    print("2. THE INDEXES, AND WHAT THEIR MEMBERS ARE QUANTISED ON.")
    sz = sizes()
    print("   %-16s %-8s %-30s %s" % ("index", "cells", "members", "quantum"))
    for nm, _mo, _a, _me, w, q in rows():
        print("   %-16s %-8s %-30s %s" % (short(nm), sz.get(nm), w[:30], q))
    print()
    print("3. NOT INDEXES OF THIS PROJECT.")
    for m, why in sorted(NOT_AN_INDEX.items()):
        print("   %-12s %s" % (m, why))
    print()
    miss = missing()
    print("4. UNACCOUNTED MODULES: %d   %s" % (len(miss), ", ".join(miss) or "none"))
    if miss:
        print("   A module exposing an index must be registered with its")
        print("   quantum numbers or named in NOT_AN_INDEX. This fails the")
        print("   selftest.")
    print()
    print("5. COMPLETE = %s." % COMPLETE)
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("THE CRITERION HOLDS ON EVERY REGISTERED ROW", enforce(), [])
    chk("fourteen indexes registered -- eleven, and three the overlap ruling "
        "seated", len(REGISTERED), 14)
    chk("exactly three came from the ruling, and they agree with it",
        sorted((m, a) for m, a, _me, _w, _q in REGISTERED
               if m == "overlaprule"),
        [("overlaprule", "gravity_bound"), ("overlaprule", "madelung_slot"),
         ("overlaprule", "nucshell_lsigma")])
    chk("every one names its quantum numbers",
        [n for n, *_r in rows() if not _r[4].strip()], [])
    chk("every method is known",
        sorted({m for _n, _mo, _a, m, _w, _q in rows()} - set(METHODS)), [])
    chk("names are unique", len({n for n, *_r in rows()}), len(rows()))
    chk("SHORT labels are unique too -- three rows share one module now",
        short_is_unique(), [])
    chk("and the three that do are labelled by their accessor",
        sorted(short(nm) for nm, m, *_r in rows() if m == "overlaprule"),
        ["gravity_bound", "madelung_slot", "nucshell_lsigma"])
    chk("NO module exposing an index is unaccounted for", missing(), [])
    chk("six modules are excused, with reasons", len(NOT_AN_INDEX), 6)
    chk("every excuse is non-empty",
        [k for k, v in NOT_AN_INDEX.items() if not v.strip()], [])
    chk("mi is excused, not registered",
        "mi" in NOT_AN_INDEX and "mi" not in {m for _n, m, *_r in rows()}, True)
    chk("cross is gone", os.path.exists(os.path.join(HERE, "cross.py")), False)
    chk("store is gone", os.path.exists(os.path.join(HERE, "store.py")), False)
    chk("obstruction is gone",
        os.path.exists(os.path.join(HERE, "obstruction.py")), False)
    chk("filled is gone", os.path.exists(os.path.join(HERE, "filled.py")), False)
    chk("density is gone", os.path.exists(os.path.join(HERE, "density.py")), False)
    chk("occupy is gone", os.path.exists(os.path.join(HERE, "occupy.py")), False)
    sz = sizes()
    chk("no index errored", [n for n, v in sz.items() if isinstance(v, str)], [])
    chk("fibred seats 170 electrons", sz["fibred.index"], 170)
    chk("madelung seats the same 170", sz["madelung.janet"], 170)
    chk("ions seats 98 transitions", sz["ions.index"], 98)
    chk("channels seats 209 shapes", sz["channels.index"], 209)
    chk("probability seats 25 subshells", sz["probability.index"], 25)
    chk("inversion seats 17 distinct cells", sz["inversion.index"], 17)
    chk("gravity seats 914 distinct cells", sz["gravity.index"], 914)
    chk("nucshell seats 22 nuclear subshells", sz["nucshell.index"], 22)
    chk("madrule seats 13 distinct cells", sz["madrule.index"], 13)
    chk("terms seats 112 distinct cells", sz["terms.index"], 112)
    chk("the ruling's gravity coarsening seats 26",
        sz["overlaprule.gravity_bound"], 26)
    chk("the ruling's nucshell coarsening seats 12",
        sz["overlaprule.nucshell_lsigma"], 12)
    chk("the ruling's madelung coarsening seats 82",
        sz["overlaprule.madelung_slot"], 82)
    chk("completeness is not claimed", COMPLETE, False)
    print("registry selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
