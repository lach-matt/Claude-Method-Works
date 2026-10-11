#!/usr/bin/env python3
"""three_body_index.py -- item 217 ("pairs alone over-reach: - we are missing a piece of the puzzle. Position 2. It could
be the method equation itself that connects position 1 to position 2. It could be that the everything bulk contributes
something we cannot see making this a 3 body problem."), with M's paper "The Three Body Problem for Unknown Masses"
(drive mirror, read-only) and its Law 3.  Computed by tools/cypher.py on bulk_index.py's index (M's account of the
transfer); worked in the conversation; seated under 206; 2026-10-11.

M's paper, Law 3 (READ, verbatim): "Every coupling coordinate's exact physical bound requires either two parents or a
congruence, and a tree carries only one (§12.11.2). Three bodies form K₃, treewidth 2, requiring strong 3-consistency
(Freuder 1982) where the closure operator ℛ delivers 2 (§21.5.1)."  Its fingerprint: pairs over-reach, the two-body chain
closes.

  B1 (computed) the bulk index's pairwise constraints form a TREE, a path: horizon_1 -- held_1 -- held_2 -- horizon_2 (the
     only unseen value pairs: the object held nowhere; a horizon at a position that does not hold it).  Yet order 2
     over-reaches by three cells, and each is refused at order 3 by a three-way constraint: (held_1, held_2, horizon_1),
     (held_1, held_2, horizon_2), (held_1, horizon_1, horizon_2), (held_2, horizon_1, horizon_2).  The binding bound --
     both horizons stand exactly when both positions hold the object -- has two parents, which a tree carries only one
     of: Law 3's mechanism, here
  B2 (computed) no hidden two-valued coordinate over the five stages closes order 2 (all 30 non-constant patterns)
  B3 (computed) exactly ONE hidden three-valued coordinate does, up to relabelling, with no key and no redundant group:
     'belongs' -- one value at before and opening, a second at the realized stage alone, a third at closing and after.
     Where the object belongs: position 1; both at once; position 2.  It is M's three holds (106 (b)): "horizon
     position 1 only as the corridor opens", "held on both horizons simultaneously", "held only at the horizon of
     position 2".  The middle value -- the object held across both, while "the corridor builds position 2 with the bits
     in mind" -- is the piece the four coordinates left implicit
  B4 (computed) with 'belongs' in, statistics closes at orders 2 and 3 (E = 0): pairs suffice once the third value is a
     coordinate.  The four lattice languages do not close under any of the 96 codings (order and algebra E >= 3,
     geometry >= 3, information >= 1): the exact region is not a lattice, and the ordinal closure gives its envelope --
     Law 3 again
  B5 (deduced from B4 and the corpus) the method equation has two halves (register 1133: E(X) = |R(X)| - |X| ordinal,
     E_W(X) = |W(X)| - |X| metric; register 1206: the metric half closes by a closed form on the index's own
     coordinates).  The ordinal half cannot connect position 1 to position 2 exactly here (B4).  If the method equation
     connects them, it is through its metric half: a closed form giving position 2's values from the index's
     coordinates -- which needs values this index does not carry (the energy E at each position: 203, 110, 111)
So, on M's two guesses: H-BULK-THIRD-BODY is supported in the cypher's sense -- the transfer's binding constraint is
three-way (position 1, position 2, and the corridor's horizons that stand only when both hold), and the one coordinate
that closes it pairwise has a third value, 'both', the corridor holding the object across.  H-METHOD-EQUATION-CONNECTS
is open: the ordinal half gives only the envelope, and the metric half needs the positions' values.  M-MISSING-PIECE
(position 2): what the index lacked was that middle value, and position 2's own values.
What this does not show: the index is M's account, five cells; 'belongs' is the unique closing coordinate within ternary
patterns over those stages, not a computed geometry; the metric half is not computed.
Imports bulk_index.py, index_audit.py and tools/cypher.py by path; reads the paper's mirror copy (read-only).  Stdlib.
python3 three_body_index.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
PAPER = os.path.join(ROOT, "drive", "The Method Materials", "CORPUS", "The_Three_Body_Problem_for_Unknown_Masses_Lach-2.md")
MUT = {}
M217 = ("we are missing a piece of the puzzle. Position 2. It could be the method equation itself that connects position 1 "
        "to position 2. It could be that the everything bulk contributes something we cannot see making this a 3 body problem.")
LAW3 = ["requires either two parents or a congruence, and a tree carries only one",
        "Three bodies form K₃, treewidth 2, requiring strong 3-consistency"]
LANGS = ("order", "algebra", "geometry", "information")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def compute():
    bi = _load(os.path.join(HERE, "bulk_index.py"), "tb_bulk_index")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "tb_cypher")
    ia = _load(os.path.join(HERE, "index_audit.py"), "tb_index_audit")
    C, ST = list(bi.C), dict(bi.STAGES)
    names = list(ST)
    cells = [ST[n] for n in names]

    def stat(coords, cl, k):
        cl = sorted(set(cl), key=str)
        ix = cy.Index("tb", coords, [list(c) for c in cl])
        inv = [{v: kk for kk, v in ix.code[i].items()} for i in range(len(coords))]
        a, _ = cy.op_statistics(ix, {"statistics_order": k})
        return {tuple(inv[i][c[i]] for i in range(len(coords))) for c in a}
    # B1 the pairwise constraint graph and the three-way blocks
    edges = set()
    for i, j in itertools.combinations(range(len(C)), 2):
        seen = {(c[i], c[j]) for c in cells}
        if any((a, b) not in seen for a in (0, 1) for b in (0, 1)):
            edges.add((C[i], C[j]))
    tri = [t for t in itertools.combinations(C, 3) if all(p in edges or p[::-1] in edges for p in itertools.combinations(t, 2))]
    over = sorted(stat(C, cells, 2) - set(cells))
    triples = set()
    for t in over:
        for s in itertools.combinations(range(len(C)), 3):
            if tuple(t[i] for i in s) not in {tuple(c[i] for i in s) for c in cells}:
                triples.add(tuple(C[i] for i in s))
    # B2, B3 hidden coordinates
    binary = [p for p in itertools.product([0, 1], repeat=5) if len(set(p)) > 1
              and len(stat(C + ["b"], [ST[n] + (p[k],) for k, n in enumerate(names)], 2)) == 5]
    ternary = []
    for p in itertools.product([0, 1, 2], repeat=5):
        if len(set(p)) != 3:
            continue
        c5 = [ST[n] + (p[k],) for k, n in enumerate(names)]
        if len(stat(C + ["b"], c5, 2)) == 5:
            m = {}
            ternary.append(tuple(m.setdefault(v, len(m)) for v in p))
    canon = sorted(set(ternary))
    # B4 with 'belongs'
    bel = (0, 0, 1, 2, 2) if not MUT.get("belongs_binary") else (0, 0, 1, 1, 1)
    C5 = C + ["belongs"]
    c5 = [ST[n] + (bel[k],) for k, n in enumerate(names)]
    lat = {l: [] for l in LANGS}
    vals = [[0, 1]] * 4 + [sorted(set(bel))]
    for orders in itertools.product(*[list(itertools.permutations(v)) for v in vals]):
        ix = cy.Index("tb5", C5, [list(c) for c in c5], value_order={C5[i]: list(orders[i]) for i in range(5)})
        for l in LANGS:
            a, _ = cy.ADMISSION[l][0](ix, {})
            lat[l].append(len(a) - 5)
    return {"edges": sorted(edges), "tri": tri, "over": over, "triples": sorted(triples), "binary": binary,
            "canon": canon, "audit_belongs": ia.audit_index(C5, c5),
            "stat_belongs": (len(stat(C5, c5, 2)) - 5, len(stat(C5, c5, 3)) - 5),
            "lattice": {l: (min(v), max(v), len(v)) for l, v in lat.items()}}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rulings = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read().replace("\n    ", " ")
    paper = open(PAPER, encoding="utf-8").read()
    add("B0 M's 217 verbatim in the rulings file; Law 3 verbatim in M's paper", M217 in rulings and all(q in paper for q in LAW3))
    add("B1 the pairwise constraints form a tree (no triangle); order 2 over-reaches by 3 cells, each refused at order 3 by "
        "a three-way constraint (four triples)", not d["tri"] and len(d["edges"]) == 3 and len(d["over"]) == 3
        and len(d["triples"]) == 4)
    add("B2 no hidden two-valued coordinate closes order 2 (30 patterns)", not d["binary"])
    add("B3 exactly one hidden three-valued coordinate does, up to relabelling: position 1 (before, opening), both "
        "(realized), position 2 (closing, after) -- M's three holds; no key, no redundant group",
        d["canon"] == [(0, 0, 1, 2, 2)] and not d["audit_belongs"]["keys"] and not d["audit_belongs"]["onehot"])
    lat = d["lattice"]
    add("B4 with it statistics closes at orders 2 and 3; the four lattice languages close under none of the 96 codings "
        "(the exact region is not a lattice: Law 3)", d["stat_belongs"] == (0, 0) and lat["order"][2] == 96
        and all(v[0] >= 1 for v in lat.values()))
    return res


MUTANTS = {"belongs_binary": "the hidden coordinate entered with two values (position 1 / not)"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-15s %-62s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("three_body_index.py -- the bulk index as a three-body problem (item 217)\n")
    print("B1 pairwise constraint edges:", d["edges"], " triangles:", d["tri"] or "none")
    print("   over-reach at order 2:", d["over"], " refused at order 3 by:", d["triples"])
    print("B2 binary hidden coordinates closing order 2:", d["binary"] or "none")
    print("B3 ternary (up to relabelling):", d["canon"], " audit:", d["audit_belongs"])
    print("B4 statistics with 'belongs' (orders 2, 3):", d["stat_belongs"], " lattice languages (min E, max E, codings):", d["lattice"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
