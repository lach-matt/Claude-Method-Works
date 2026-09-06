#!/usr/bin/env python3
"""lambda8.py -- Lambda-8 rebuilt from the seven constraints the book prints, and the
claims made about their graph, checked.

Candidate E-072 of CANDIDATES-R4-subject-matter.tsv asks whether Lambda has SEVEN
constraints, as section 21.5.2 and tower-2.py have it, or EIGHT, as one Register
entry prints.  Everything else here is the surrounding claim, checked in the same run
because it is one object.

WHAT THE BOOK PRINTS (main, section 21.5.2)

    "Lambda's seven constraints are seven pairs, each with a multiplier and an offset:
       l <= n-1 . k <= 4l+2 . q <= k . f <= e-1 . g <= 4f+2 . g <= q . 2S <= k
     Each constraint is pairwise, so three constraints closing on three variables is a
     3-body.  Counted over every triple: 3 nodes 0, 4 nodes 7, 5 nodes 20, 6 nodes 8.
     Lambda has no 3-body among its constraints -- zero of thirty-five.  Its constraint
     graph is eight nodes and seven edges: a tree.  And it is one edge away in exactly
     seven places."

WHAT THIS PROGRAM DOES

  1. Rebuilds Lambda-8 from those seven constraints and the section 7.4 caps ALONE,
     as a filter over the ambient box, and checks it against the seated tower-2.py
     cell for cell.  If the seven generate the object, the object has seven.
  2. Counts the constraints as pairwise relations and builds their graph.
  3. Checks the triple census 0 / 7 / 20 / 8 over all C(7,3) = 35 triples.
  4. Checks that the graph is a tree, and finds every place one added edge would
     make a 3-body.

The point of (1) is that the count is not settled by counting a printed list.  A
constraint set is right when it generates the object and no proper subset does.

INPUT
  method/members/tower-2.py -- the seated member, imported by path, never copied.

REFUSALS
  The section 7.4 caps (n <= 3, l <= 1, k <= 3, e <= 3, f <= 1) are BOUNDS ON THE BOX,
  not constraints between coordinates, and are not counted as such.  That is the
  book's own distinction and this program keeps it; a reader who counted a cap as a
  constraint would get more than seven and would be counting a different thing.
  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, itertools, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")

NAMES = ["n", "l", "k", "q", "e", "f", "g", "2S"]
IX = {s: i for i, s in enumerate(NAMES)}

# The seven constraints, exactly as section 21.5.2 prints them.  Each is (name, the
# pair of coordinates it relates, the test).
CONSTRAINTS = [
    ("l <= n-1",  ("n", "l"),  lambda c: c[IX["l"]]  <= c[IX["n"]] - 1),
    ("k <= 4l+2", ("l", "k"),  lambda c: c[IX["k"]]  <= 4 * c[IX["l"]] + 2),
    ("q <= k",    ("k", "q"),  lambda c: c[IX["q"]]  <= c[IX["k"]]),
    ("f <= e-1",  ("e", "f"),  lambda c: c[IX["f"]]  <= c[IX["e"]] - 1),
    ("g <= 4f+2", ("f", "g"),  lambda c: c[IX["g"]]  <= 4 * c[IX["f"]] + 2),
    ("g <= q",    ("q", "g"),  lambda c: c[IX["g"]]  <= c[IX["q"]]),
    ("2S <= k",   ("k", "2S"), lambda c: c[IX["2S"]] <= c[IX["k"]]),
]

# The section 7.4 caps: bounds on the box, not relations between coordinates.
CAPS = dict(n=(1, 3), l=(0, 1), k=(1, 3), q=(0, 3), e=(1, 3), f=(0, 1), g=(0, 3))


def load_tower(members):
    path = os.path.join(members, "tower-2.py")
    spec = importlib.util.spec_from_file_location("tower2", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def box():
    """The ambient box the caps allow, before any constraint.  2S's own range is
    bounded by k's cap, which is the only place a cap and a constraint meet."""
    for n in range(CAPS["n"][0], CAPS["n"][1] + 1):
        for l in range(CAPS["l"][0], CAPS["l"][1] + 1):
            for k in range(CAPS["k"][0], CAPS["k"][1] + 1):
                for q in range(CAPS["q"][0], CAPS["q"][1] + 1):
                    for e in range(CAPS["e"][0], CAPS["e"][1] + 1):
                        for f in range(CAPS["f"][0], CAPS["f"][1] + 1):
                            for g in range(CAPS["g"][0], CAPS["g"][1] + 1):
                                for S2 in range(0, CAPS["k"][1] + 1):
                                    yield (n, l, k, q, e, f, g, S2)


def rebuild(subset=None):
    use = CONSTRAINTS if subset is None else [CONSTRAINTS[i] for i in subset]
    return {c for c in box() if all(t(c) for _, _, t in use)}


def graph():
    return [tuple(sorted(pair)) for _, pair, _ in CONSTRAINTS]


def is_tree(nodes, edges):
    par = {v: v for v in nodes}

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False, "has a cycle"
        par[ra] = rb
    roots = {find(v) for v in nodes}
    return (len(roots) == 1 and len(edges) == len(nodes) - 1,
            f"{len(roots)} component(s), {len(edges)} edges over {len(nodes)} nodes")


def measure(members):
    tw = load_tower(members)
    seated = {tuple(c) for c in tw.L8()}
    built = rebuild()
    # Is any constraint redundant?  Drop each in turn and see whether the object grows.
    redundant = []
    for i, (name, _, _) in enumerate(CONSTRAINTS):
        without = rebuild([j for j in range(len(CONSTRAINTS)) if j != i])
        if without == built:
            redundant.append(name)
    E = graph()
    tree, why = is_tree(NAMES, E)
    # The triple census: for each triple of constraints, how many distinct nodes
    triples = {}
    for t in itertools.combinations(range(len(CONSTRAINTS)), 3):
        span = len({v for i in t for v in CONSTRAINTS[i][1]})
        triples[span] = triples.get(span, 0) + 1
    # One edge away from a 3-body: a non-edge whose endpoints are at distance 2
    adj = {v: set() for v in NAMES}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    near = []
    for v in NAMES:
        for a, b in itertools.combinations(sorted(adj[v]), 2):
            if b not in adj[a]:
                near.append((a, b, tuple(sorted((a, v, b)))))
    return dict(seated=len(seated), built=len(built), same=(seated == built),
                redundant=redundant, edges=E, tree=tree, why=why,
                triples=triples, near=sorted(near), constraints=CONSTRAINTS)


def report(o):
    print("  LAMBDA-8 REBUILT FROM THE SEVEN CONSTRAINTS THE BOOK PRINTS")
    print()
    print("  1. DO THE SEVEN GENERATE THE OBJECT?")
    for name, pair, _ in o["constraints"]:
        print(f"       {name:<10}  relates {pair[0]} and {pair[1]}")
    print(f"     seated tower-2.py L8()   {o['seated']} cells")
    print(f"     rebuilt from the seven   {o['built']} cells")
    print(f"     identical cell for cell  {o['same']}")
    print(f"     redundant constraints    {o['redundant'] or 'none -- every one is needed'}")
    print("     So the constraint set is exactly seven: seven generate it, and no six do.")
    print()
    print("  2. THE CONSTRAINT GRAPH")
    print(f"     {len(NAMES)} nodes, {len(o['edges'])} edges: "
          + " · ".join(f"{a}-{b}" for a, b in o["edges"]))
    print(f"     a tree? {o['tree']}   ({o['why']})")
    print()
    print("  3. THE TRIPLE CENSUS, over all C(7,3) = 35 triples of constraints")
    for span in sorted(o["triples"]):
        tag = "  <== a true 3-body" if span == 3 else ""
        print(f"     triples spanning {span} nodes: {o['triples'][span]}{tag}")
    print(f"     total {sum(o['triples'].values())};  3-bodies {o['triples'].get(3, 0)}")
    print()
    print("  4. ONE EDGE FROM A 3-BODY")
    for a, b, tri in o["near"]:
        print(f"     add {a} - {b:<3} -> a 3-body on {{{', '.join(tri)}}}")
    print(f"     {len(o['near'])} places, one per existing edge, which is what adding an edge")
    print("     to a tree gives.")
    print()
    print("  VERDICT ON CANDIDATE E-072")
    print("     SEVEN. The seven printed constraints generate Lambda-8 exactly and none is")
    print("     redundant. Every claim section 21.5.2 makes about their graph reproduces.")
    print("     The Register entry printing 'Lambda's eight constraints' is the outlier.")
    print("     Nothing is repaired here.")


FIXTURES = """the corpus's own recorded numbers:
  |Lambda-8| = 976                                   -- everywhere, and tower-2.out
  seven constraints, eight nodes, seven edges, a tree -- main section 21.5.2
  triples 0 / 7 / 20 / 8 over thirty-five             -- main section 21.5.2
  one edge from a 3-body in exactly seven places      -- main section 21.5.2, and the
                                                         Mathematical Compendium's
                                                         'The seven near-misses'"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("seated |L8|", o["seated"], 976)
    eq("rebuilt from the seven", o["built"], 976)
    eq("identical to the seated object", o["same"], True)
    eq("no constraint is redundant", o["redundant"], [])
    eq("nodes", len(NAMES), 8)
    eq("edges", len(o["edges"]), 7)
    eq("the graph is a tree", o["tree"], True)
    eq("triples spanning 3 nodes", o["triples"].get(3, 0), 0)
    eq("triples spanning 4 nodes", o["triples"].get(4, 0), 7)
    eq("triples spanning 5 nodes", o["triples"].get(5, 0), 20)
    eq("triples spanning 6 nodes", o["triples"].get(6, 0), 8)
    eq("triples in all", sum(o["triples"].values()), 35)
    eq("one edge from a 3-body", len(o["near"]), 7)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<12} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--members", default=MEMBERS)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.members)
    report(measure(a.members))
    return 0


if __name__ == "__main__":
    sys.exit(main())
