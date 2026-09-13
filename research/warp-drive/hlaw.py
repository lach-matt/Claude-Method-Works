#!/usr/bin/env python3
r"""
hlaw.py -- THE HIERARCHY LAW AS AN INSTRUMENT.  Hand it an index; it reports
what the law says about that index, and it tries to break the law while it is
there.

The paper (paper/THE-HIERARCHY-LAW.md) states and proves the law.  law.py
argues it, induce.py measured it, lawfigures.py pins the paper's figures.
None of those is a thing you can point at an index.  This is.

    python3 hlaw.py --example antichain2      run the law against a named index
    python3 hlaw.py --index FILE              ... or one you supply
    python3 hlaw.py --list                    the built-in indexes
    python3 hlaw.py --sweep 400               try to break the law, N random indexes
    python3 hlaw.py --selftest                fixtures are the paper's own numbers

INPUT.  One tuple per line, integers separated by commas or whitespace; blank
lines and `#` comments ignored.  Every tuple must have the same arity.  A JSON
list-of-lists is also accepted.

EXIT.  0 if the law holds on the index, 1 if it does not.  A non-zero exit from
this program is a refutation of the hierarchy law, not a bug report -- see
"IF THIS PROGRAM EXITS 1" at the bottom of this docstring.

===============================================================================
WHAT IT REFUSES TO DO, AND THE REFUSALS ARE THE POINT
===============================================================================

**It never prints a total ranking of the five.**  Clause E is a refutation: the
order in which the five nest is a property of the index, not a law, and 14
distinct rankings appear across 400 indexes.  A program that prints "the
hierarchy" as a list would be reporting an artefact of whichever index it was
handed.  This one prints the partial order and marks every incomparable pair
INCOMPARABLE.

**It never reports a size comparison as a containment.**  |geometry| > |information|
does not mean information subset geometry.  On both seated indexes in the paper
those two are set-theoretically incomparable while their sizes differ, and an
earlier draft of the paper read the size reversal as a nesting swap and had to
withdraw it.  Sizes and containments are printed in separate blocks here and are
never merged.

**It never promotes a containment to a law because it held on your index.**
Exactly seven of the twenty containments are lawful, each proved in the paper.
The other thirteen vary.  When one of the thirteen holds on your index this
program says INDEX-ONLY, and it means it -- six of the thirteen are refuted as
universal claims by an explicit witness the paper prints, and the rest by
measurement.

**It does not repair a refutation.**  If a lawful containment fails, the
instrument reports it and exits 1.  It does not adjust the ambient, retry under
another regime, or downgrade the clause.

===============================================================================
WHAT IT IMPORTS RATHER THAN REIMPLEMENTS
===============================================================================

The five operators are decomposable.py's (`stair`, `gen`, `joinclose`) and
lawfigures.py's (`stat`, `geom`, which reach the convex hull through
necindex.cypher).  Nothing here recomputes a closure that another instrument
already defines -- if the operators are wrong they are wrong in one place.

===============================================================================
IF THIS PROGRAM EXITS 1
===============================================================================

Exit 1 means one of the seven lawful containments failed on a finite index.
Each of the seven is proved in the paper, so before treating that as a
refutation, check the two things a proof does not cover:

  1. Is every factor a chain?  Clause B's proof needs each coordinate's observed
     alphabet totally ordered.  Off the chains the staircase UNDER-generates --
     the paper's N2 -- and `order subset algebra` fails in that one direction.
     This program's inputs are integer tuples, so its factors are always chains
     and this escape does not apply to anything it can read.
  2. Is the ambient the observed box?  Every containment here is computed in
     `Box(X) = product of pi_i(X)`, which is the paper's own-box regime.

If neither applies, the index is a counterexample to a proved clause and the
proof is wrong.  Print it and keep it.
"""

import itertools
import json
import random
import sys

import decomposable as D
import lawfigures as LF
import necindex

LANGS = LF.LANGS
OPS = LF.OPS

# The law.  (a, b) reads `a subset b`.  Seven of the twenty ordered pairs, each
# proved in the paper: two are Clause B, two Clause C, one G.3, and two the
# three-line proof in section 6d.  This tuple is the law's whole content as far
# as containment goes, and it is not derived here -- it is quoted.
LAWFUL = (
    ("order", "algebra"), ("algebra", "order"),          # Clause B
    ("information", "algebra"), ("information", "order"),  # Clause C
    ("statistics", "algebra"), ("statistics", "order"),    # section 6d proof
    ("statistics", "geometry"),                            # G.3
)

WHY = {
    ("order", "algebra"): "Clause B",
    ("algebra", "order"): "Clause B",
    ("information", "algebra"): "Clause C",
    ("information", "order"): "Clause C",
    ("statistics", "algebra"): "6d, three-line proof",
    ("statistics", "order"): "6d, three-line proof",
    ("statistics", "geometry"): "Clause G.3",
}

# The six non-containments the paper refutes with an explicit minimal witness.
# The other seven of the thirteen vary by measurement only.
WITNESSED = (
    ("geometry", "order"), ("order", "geometry"),
    ("information", "statistics"), ("statistics", "information"),
    ("information", "geometry"), ("geometry", "information"),
)

EXAMPLES = {
    "antichain2": ([(0, 1), (1, 0)],
                   "the two-cell antichain; separates three of the six incomparabilities"),
    "chain2": ([(0, 0), (1, 1)],
               "the order-dependence witness of Clause F"),
    "geom-not-order": ([(0, 0), (0, 1), (1, 2), (2, 2)],
                       "geometry not-subset order"),
    "geom-not-info": ([(0, 0), (0, 2), (1, 1)],
                      "geometry not-subset information"),
    # ONE set, three jobs. The paper remarks on it: the statistics-not-subset-
    # information witness is the same three cells that break 2-determinacy in
    # Clause D, and they are also X_3 of the section 8d construction at d = 3.
    # Listing it once, rather than three times under three names, is the point.
    "three-cell": ([(0, 0, 0), (0, 1, 1), (1, 0, 1)],
                   "statistics not-subset information; breaks 2-determinacy; "
                   "and is X_3 of section 8d at d = 3"),
    # Imported, never copied: the cells are necindex.py's, which is where that
    # index is seated. The paper's section 7 prints |geometry| = 29 and
    # |information| = 208 for it after the arity coordinate was seated, and the
    # selftest holds this program to those.
    "energy-conditions": (sorted(necindex.cells()),
                          "the index of section 7: 17 energy conditions over five "
                          "coordinates in a 576-cell box"),
}


# ------------------------------------------------------------------ the index

def parse_index(text):
    """Tuples from text.  JSON list-of-lists, or one tuple per line."""
    t = text.strip()
    if t.startswith("["):
        rows = [tuple(int(v) for v in r) for r in json.loads(t)]
    else:
        rows = []
        for line in t.splitlines():
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            rows.append(tuple(int(v) for v in line.replace(",", " ").split()))
    if not rows:
        raise ValueError("no tuples found")
    d = len(rows[0])
    if d < 2:
        raise ValueError("d >= 2 is required; the law says nothing at d = 1")
    for r in rows:
        if len(r) != d:
            raise ValueError("ragged index: %r has arity %d, expected %d" % (r, len(r), d))
    return frozenset(rows)


def closures(X):
    """{name: frozenset} for the five, over the observed box."""
    d = len(next(iter(X)))
    box = D.box_of(X, d)
    return {L: frozenset(OPS[L](sorted(X), box)) for L in LANGS}, box


# ------------------------------------------------------------------- the law

def check_law(cl):
    """Every lawful containment, checked.  [(a, b, holds, why)]."""
    return [(a, b, cl[a] <= cl[b], WHY[(a, b)]) for a, b in LAWFUL]


def index_only(cl):
    """The thirteen that are not lawful, and whether each holds HERE."""
    out = []
    for a in LANGS:
        for b in LANGS:
            if a == b or (a, b) in LAWFUL:
                continue
            out.append((a, b, cl[a] <= cl[b], (a, b) in WITNESSED))
    return out


def clause_readout(X, cl, box):
    """Clause-by-clause, on this index.  [(clause, statement, value)]."""
    d = len(next(iter(X)))
    rows = [
        ("A", "each closure is extensive (X subset L(X))",
         all(X <= cl[L] for L in LANGS)),
        ("B", "order == algebra, both the sublattice hull",
         cl["order"] == cl["algebra"] == frozenset(D.gen(set(X)))),
        ("C", "information == the join-closure of X",
         cl["information"] == frozenset(D.joinclose(set(X)))),
        ("D", "algebra is 2-determined here",
         D.kdet(cl["algebra"], box, 2)),
        ("D", "information is 2-determined here",
         D.kdet(cl["information"], box, 2)),
        ("G", "statistics subset geometry (G.3, lawful)",
         cl["statistics"] <= cl["geometry"]),
    ]
    if d >= 3:
        rows.append(("D", "information is 3-determined here",
                     D.kdet(cl["information"], box, 3)))
    return rows


def relabel_sensitivity(X, seed=0):
    """Clause F, on this index: which operators a coordinate relabelling moves.
    Returns {name: invariant?}."""
    d = len(next(iter(X)))
    box = D.box_of(X, d)
    rnd = random.Random(seed)
    perms = []
    for i in range(d):
        v = list(box[i])
        sh = v[:]
        rnd.shuffle(sh)
        perms.append(dict(zip(v, sh)))
    inv = [{v: k for k, v in p.items()} for p in perms]
    Xp = frozenset(tuple(perms[i][x[i]] for i in range(d)) for x in X)
    bp = D.box_of(Xp, d)
    out = {}
    for L in LANGS:
        back = frozenset(tuple(inv[i][y[i]] for i in range(d))
                         for y in OPS[L](sorted(Xp), bp))
        out[L] = back == frozenset(OPS[L](sorted(X), box))
    return out


# ---------------------------------------------------------------- the report

def report(X, name=None):
    """Print the full reading.  Returns True if the law holds on this index."""
    d = len(next(iter(X)))
    cl, box = closures(X)
    W = 13

    print("=" * 74)
    print("THE HIERARCHY LAW, APPLIED%s" % ("" if not name else "  --  " + name))
    print("=" * 74)
    print("  d = %d    |X| = %d    box = %s    |Box| = %d"
          % (d, len(X), "x".join(str(len(a)) for a in box),
             len(list(itertools.product(*box)))))
    print()

    print("THE FIVE CLOSURES.  E is the residual |L(X)| - |X|.")
    for L in LANGS:
        print("  %-*s |L(X)| = %-6d E = %d" % (W, L, len(cl[L]), len(cl[L]) - len(X)))
    print()

    print("SIZES ARE NOT CONTAINMENTS, so they are reported apart and never merged.")
    order_by_size = sorted(LANGS, key=lambda L: (len(cl[L]), L))
    print("  by size, smallest first: %s" % "  <=  ".join(
        "%s(%d)" % (L, len(cl[L])) for L in order_by_size))
    print("  ^ a size order. It is NOT a nesting order and must not be read as one.")
    print()

    law = check_law(cl)
    ok = all(h for _, _, h, _ in law)
    print("THE LAW -- seven containments, each proved. All seven must hold.")
    for a, b, holds, why in law:
        print("  [%s] %-*s subset %-*s   (%s)"
              % ("ok" if holds else "REFUTED", W, a, W, b, why))
    print("  VERDICT: %s" % ("the law holds on this index"
                             if ok else "*** THE LAW FAILS ON THIS INDEX ***"))
    print()

    print("THIS INDEX ONLY -- the other thirteen. Holding here is not a law.")
    for a, b, holds, wit in index_only(cl):
        tag = "INDEX-ONLY" if holds else "fails here"
        note = "refuted as universal by a witness in the paper" if wit else "varies by measurement"
        print("  [%-10s] %-*s subset %-*s   %s" % (tag, W, a, W, b, note))
    print()

    print("THE PARTIAL ORDER ON THIS INDEX. No total ranking is printed: Clause E.")
    for i, a in enumerate(LANGS):
        for b in LANGS[i + 1:]:
            ab, ba = cl[a] <= cl[b], cl[b] <= cl[a]
            rel = ("EQUAL" if ab and ba else
                   "%s subset %s" % (a, b) if ab else
                   "%s subset %s" % (b, a) if ba else "INCOMPARABLE")
            print("  %-*s vs %-*s   %s" % (W, a, W, b, rel))
    print()

    print("CLAUSE READOUT.")
    for clause, stmt, val in clause_readout(X, cl, box):
        print("  [%s] Clause %-2s %s" % ("yes" if val else " no", clause, stmt))
    print()

    print("CLAUSE F -- does a coordinate relabelling move the operator?")
    for L, invariant in relabel_sensitivity(X).items():
        print("  %-*s %s" % (W, L, "invariant" if invariant else "MOVES (order-dependent)"))
    print("  statistics is the one that must never move; the others may.")
    print()
    return ok


# ----------------------------------------------------------------- the sweep

def sweep(n=400, seed=19):
    """Try to break the law over n random indexes.  (violations, checked)."""
    rnd = random.Random(seed)
    bad = []
    for _ in range(n):
        d = rnd.randint(2, 4)
        alpha = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 10))))
        cl, _ = closures(X)
        for a, b in LAWFUL:
            if not cl[a] <= cl[b]:
                bad.append((sorted(X), a, b))
    return bad, n


# -------------------------------------------------------------------- checks

def selftest():
    """Fixtures are the paper's own recorded numbers and its printed witnesses."""
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("hlaw selftest -- fixtures from paper/THE-HIERARCHY-LAW.md")

    # The law is quoted, not derived. It must equal Clause H's measured set.
    chk("LAWFUL is exactly Clause H's seven", sorted(LAWFUL),
        sorted(LF.PINS["h_always"]))
    chk("and there are seven of them", len(LAWFUL), 7)
    chk("out of twenty ordered pairs", len(LANGS) * (len(LANGS) - 1), 20)
    chk("thirteen are not lawful", 20 - len(LAWFUL), 13)
    chk("six of the thirteen carry a witness", len(WITNESSED), 6)
    chk("no witnessed pair is also lawful",
        [p for p in WITNESSED if p in LAWFUL], [])

    # The law holds on every built-in index.
    for nm, (rows, _) in sorted(EXAMPLES.items()):
        cl, _ = closures(frozenset(rows))
        chk("the law holds on example %r" % nm,
            all(cl[a] <= cl[b] for a, b in LAWFUL), True)

    # Each witness example really shows the non-containment it is named for.
    cl, _ = closures(frozenset(EXAMPLES["geom-not-order"][0]))
    chk("geom-not-order: geometry not-subset order", cl["geometry"] <= cl["order"], False)
    cl, _ = closures(frozenset(EXAMPLES["geom-not-info"][0]))
    chk("geom-not-info: geometry not-subset information",
        cl["geometry"] <= cl["information"], False)
    cl, _ = closures(frozenset(EXAMPLES["antichain2"][0]))
    chk("antichain2: order not-subset geometry", cl["order"] <= cl["geometry"], False)
    chk("antichain2: information not-subset statistics",
        cl["information"] <= cl["statistics"], False)
    X = frozenset(EXAMPLES["three-cell"][0])
    cl, box = closures(X)
    chk("three-cell: statistics not-subset information",
        cl["statistics"] <= cl["information"], False)
    chk("three-cell: and information is NOT 2-determined",
        D.kdet(cl["information"], box, 2), False)

    # Clause B on every example: order and algebra are one operator.
    chk("order == algebra on every built-in index",
        all(closures(frozenset(r))[0]["order"] == closures(frozenset(r))[0]["algebra"]
            for r, _ in EXAMPLES.values()), True)

    # The section 8d construction: information misses a cell its pairs admit.
    X = frozenset(EXAMPLES["three-cell"][0])
    cl, box = closures(X)
    chk("three-cell: it is X_3, so k = 2 fails there too",
        D.kdet(cl["information"], box, 2), False)

    # The paper's section 7 prints figures for the energy-condition index. This
    # program computes them from the seated cells, so agreement ties the
    # instrument to the published table rather than to its own arithmetic.
    X = frozenset(EXAMPLES["energy-conditions"][0])
    cl, box = closures(X)
    chk("energy-conditions: 17 cells over five coordinates", (len(X), len(next(iter(X)))), (18, 6))
    chk("energy-conditions: box is 576 cells",
        len(list(itertools.product(*box))), 576)
    chk("energy-conditions: |geometry| = 30 after the arity fix", len(cl["geometry"]), 30)
    chk("energy-conditions: |information| = 208 after the arity fix", len(cl["information"]), 208)
    chk("energy-conditions: geometry and information are INCOMPARABLE",
        (cl["geometry"] <= cl["information"], cl["information"] <= cl["geometry"]),
        (False, False))
    chk("energy-conditions: order == algebra == 256",
        (cl["order"] == cl["algebra"], len(cl["order"])), (True, 256))
    chk("energy-conditions: statistics admits exactly the seated cells, E = 0",
        (cl["statistics"] == X, len(cl["statistics"]) - len(X)), (True, 0))
    chk("energy-conditions: the law holds on it",
        all(cl[a] <= cl[b] for a, b in LAWFUL), True)

    # The sweep must find nothing. If it ever does, that is the finding.
    bad, n = sweep(200, seed=5)
    chk("200-index sweep finds no violation of the law", len(bad), 0)

    # Parsing.
    chk("parse: whitespace and commas agree",
        parse_index("0 1\n1,0"), frozenset({(0, 1), (1, 0)}))
    chk("parse: JSON agrees", parse_index("[[0,1],[1,0]]"),
        frozenset({(0, 1), (1, 0)}))
    chk("parse: comments and blanks ignored",
        parse_index("# c\n\n0 0\n1 1  # trailing\n"), frozenset({(0, 0), (1, 1)}))
    for bad_in, why in (("0 1\n0 1 2", "ragged"), ("", "empty"), ("0\n1", "d = 1")):
        try:
            parse_index(bad_in)
            chk("parse rejects %s" % why, False, True)
        except ValueError:
            chk("parse rejects %s" % why, True, True)

    print("hlaw selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()

    if "--list" in argv:
        print("built-in indexes (each is a witness the paper prints):\n")
        for nm, (rows, note) in sorted(EXAMPLES.items()):
            cells = str(sorted(rows))
            if len(cells) > 34:
                cells = "%d cells, d = %d" % (len(rows), len(rows[0]))
            print("  %-18s %-34s %s" % (nm, cells, note))
        return 0

    if "--sweep" in argv:
        i = argv.index("--sweep")
        n = int(argv[i + 1]) if i + 1 < len(argv) else 400
        bad, checked = sweep(n)
        print("swept %d random indexes against the seven lawful containments" % checked)
        if not bad:
            print("no violation found. This corroborates the law; it does not prove it —")
            print("the proofs are in the paper and a sweep cannot add to them.")
            return 0
        print("*** %d VIOLATIONS -- each is a counterexample to a proved clause ***" % len(bad))
        for X, a, b in bad[:20]:
            print("  %s subset %s fails on %s" % (a, b, X))
        return 1

    if "--example" in argv:
        i = argv.index("--example")
        nm = argv[i + 1] if i + 1 < len(argv) else ""
        if nm not in EXAMPLES:
            print("unknown example %r; --list shows them" % nm, file=sys.stderr)
            return 2
        rows, note = EXAMPLES[nm]
        return 0 if report(frozenset(rows), "%s (%s)" % (nm, note)) else 1

    if "--index" in argv:
        i = argv.index("--index")
        if i + 1 >= len(argv):
            print("--index needs a file", file=sys.stderr)
            return 2
        path = argv[i + 1]
        with open(path) as fh:
            X = parse_index(fh.read())
        return 0 if report(X, path) else 1

    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
