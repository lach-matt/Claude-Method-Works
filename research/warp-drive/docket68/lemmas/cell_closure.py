#!/usr/bin/env python3
"""cell_closure.py -- item 244: closure per cell, not of the whole bulk index.  M, on the board's report of item 243:
"I also found the twelve-member bulk index isn't closed (order E = 6) - what if the constants of the bulk index only
need to guarantee closure of each cell under its own conditions, not closure of the entire bulk index?"  Carried as M's
hypothesis H-CELL-CLOSURE and put to the cypher (196).  Worked in the conversation (computed, exact where marked; READ
where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-11.

A cell of the bulk index is a universe, and item 8 (H-CLOSED-INDEX) makes each universe a closed index.  The Method
(READ) makes a closed index's closure a question of order: §15.3, "X is closed under some order iff" may-precede is a
total order (at d = 2; necessary above it); §15.4, "If the constraint graph is a tree, each axis is constrained only by
its parent" -- and the orders are recovered; §15.5, "For an index whose graph has cycles, S2 is open".

  E0 (read) M's item-244 words and item 8's sentence, verbatim in the rulings file; the Method's sentences above,
     verbatim in The_Method_1_6-2.md.
  E1 (computed) The constants cannot close the bulk index.  Entered as coordinates they take one value in every cell,
     and a one-value coordinate multiplies the index's box by one: every language's E is unchanged (closed_bounds C2,
     re-run here on the twelve members).  The bulk's closure was never a thing they could give.
  E2 (computed, exact) What the bulk index lacks.  The cells the cypher adds to the twelve members (order 6, algebra 6,
     geometry 6, information 3) are decoded from the 5D basis back to (G, tension) steps: every one is off the
     positions' lattice -- a third of a 2P step (G x 2^(1/3), tension x 2^(-2/3)) and 2b plus two thirds of one (G x
     2^(5/3), tension x 2^(-4/3)), each under the three matter laws.  In 5D terms: ours' geometry (ell / l5) with 2b's
     coupling, and 2b's geometry with 2P's.  Those six universes hold every constant with a form (their sectors computed,
     1e-12), and with them the bulk index is closed in every language (E = 0, eighteen cells).  The bulk's non-closure
     is universes it does not yet hold, between the members -- item 233's "every plausible and possible" bulk -- not a
     constant's failure.
  E3 (computed; the cypher, roster 1173) Each cell's own index is closed.  A cell's own conditions (item 244 (a)): its
     window (the top, and the table-top floor read at its own G -- or, as the alternative reading, the absolute floor),
     its plane's positivity and its README capacity, with the throat's matter regime read as a regime and, separately,
     as a bound.  Its own index is the admissible set over its own coordinates (its tension's place w, the offset's
     ratio z, the README's size n) on a grid.  All eighteen cells -- the twelve members and the six E2 adds -- are closed
     in every language (E = 0) under every reading, under exactly two orders: w and z rising with the README's size
     falling, and its reverse.  A cell's matter law enters none of its own conditions (it enters the matter exceptions,
     a fixed fact, and chemistry, the object's), so cells differing only in law share one own index.
  E4 (computed; deduced where marked) What guarantees each cell's closure.  Each two-coordinate own condition ties
     a pair -- positivity ties w and z, capacity z and n, the regime (as a bound) n and w; the top and the floors are
     single-coordinate, the box.  Only a condition that binds -- excludes a point every other own condition admits --
     enters the graph.  Under the stated forms the binding graph is a path, a tree (§15.4), in every reading: with the
     regime as a regime, positivity and capacity; with the regime as a bound, positivity and the regime, the capacity
     never binding -- positivity and the regime imply it with log2(4/3) to spare (bounds.py B2's identity, the bit
     area's 4/3).  So each cell is closed by the shape of its own conditions, and stays closed under every constant
     lifted (closed_bounds' lifts) and every power of the curvature swept.  A cycle (w - z - n - w) appears only when a
     lift makes the capacity bind beside the regime, and a cycle closes only when the signs around it agree (deduced:
     the edges need opposite-signed coefficients after orienting, so the product of -sign(a_u a_v) around it must be
     +1).  Sweeping the offset's power in the capacity (pc, N_max ~ dsigma^-pc) and the README's power in the throat's
     area (qN, 4 pi r0^2 = N^qN A_bit) over -1, 0, 1, 2: the cell opens in every order exactly when pc < 0 and qN > 0 --
     a capacity that grows with the offset, beside a throat that grows with the README -- and is closed everywhere else
     (with qN <= 0 the regime never binds inside the window, its constant 199.07 exceeding W = 196.89).  The cypher's
     verdict and the binding sign-parity rule agree at every swept point.  The stated forms have (1, 1): with the regime
     read as a bound, the capacity's form (its offset power's sign) and the throat's bit area (its README power's sign)
     are what keep each cell closed; with the regime read as a regime, nothing has to.
  E5 (computed, exact; the board's translation of P2) Each cell defends itself: at each of the eighteen cells, the map
     from (G, tension, offset's ratio, README) to the quantities the constants fix has dim q 10, rank 4, ⅅ = 6; freed of
     every constant, ⅅ = 0.  The self-defence is the constants', cell by cell.

What this does not show.
  - Whether the regime is a bound or a regime is the record's (236 R4 calls it a regime); both are reported.
  - The grid is a scan: w by 25 over the window, z by 50 over [-450, 450], n by 50 over [0, 400] doublings.  Each own
    condition is monotone in each coordinate, so the closing orders do not depend on the step; the range does matter,
    because a condition that binds only outside the scan is invisible to it -- an earlier scan with z from -50 hid the
    capacity's binding at z < -406 under pc = -1 and read four open cells as closed.  The range is set so that every
    swept condition binds inside it.
  - The six off-lattice universes are the cypher's completion of the 5D basis, not members any position builds.
  - Relativity bounds and the one-coupling relation are relations to the object and to other cells, left out of a
    cell's own conditions by reading (a).

Imports closed_bounds.py (and through it bounds.py, bulk5_index.py, p2_planck.py, p2_gravity.py) and tools/cypher.py by
path.  Stdlib.  python3 cell_closure.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
METHOD = os.path.join(ROOT, "method", "members", "The_Method_1_6-2.md")
MUT = {}
M244 = ("I also found the twelve-member bulk index isn't closed (order E = 6) - what if the constants of the bulk index "
        "only need to guarantee closure of each cell under its own conditions, not closure of the entire bulk index?")
M8 = "Each universe/spacetime is a repository/closed index."
READS = ["X is closed under some order iff", "If the constraint graph is a tree, each axis is constrained only by its parent.",
         "For an index whose graph has cycles, S2 is open"]
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
LANGS = ("order", "algebra", "geometry", "information", "statistics")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


CB = _load(os.path.join(HERE, "closed_bounds.py"), "cc_cb")
B5M, PP = CB.B5M, CB.PP
OWN_COORDS = ("w", "z", "n")
WS = [F(x) for x in range(0, 200, 25)]
ZS = [F(x) for x in range(-450, 451, 50)]
NS = [F(x) for x in range(0, 401, 50)]
READINGS = {
    "regime as a regime": ["top (corridor inside the curvature)", "table-top floor (relative)", "plane positivity",
                           "README capacity"],
    "regime as a bound": ["top (corridor inside the curvature)", "table-top floor (relative)", "plane positivity",
                          "README capacity", "throat matter regime"],
    "absolute floor": ["top (corridor inside the curvature)", "table-top floor (absolute)", "plane positivity",
                       "README capacity"],
}


def default():
    P = dict(CB.DEFAULT)
    if MUT.get("regime_sign"):
        P["qN"] = F(-1)
    return P


# ================================================================================ E1, E2 the bulk index
def bulk_cells():
    fd = B5M.five_d()
    return {n: (B5M.LAW_ORDER.index(fd[n]["law"]), int(3 * fd[n]["e"]["ell_l5"]), int(fd[n]["e"]["k4"])) for n in PP.MEMBERS}


def bulk_ix(cy, held):
    coords = ["matter", "ell_l5_x3", "kappa5_4"]
    vals = [sorted({c[x] for c in held}, key=lambda t: (abs(t), t)) for x in range(3)]
    return cy.Index("bulk5_cells", coords, [list(c) for c in held], value_order={coords[x]: vals[x] for x in range(3)})


def decode(cell):
    """a 5D-basis cell (law, 3 ell/l5, kappa5^4 exponent) back to (law, g, s): kappa5^4 = g - s, 3 ell/l5 = -(2g + s);
    on the positions' lattice when g is an integer and s an even one; (i, j) = (g + s/2, -s/2)"""
    x, kap = cell[1], cell[2]
    g = F(kap - x, 3)
    s = g - kap
    on = g.denominator == 1 and s.denominator == 1 and s.numerator % 2 == 0
    return dict(law=B5M.LAW_ORDER[cell[0]], g=g, s=s, i=g + s / 2, j=-s / 2, on=on)


def bulk_closure(cy):
    held = sorted(set(bulk_cells().values()))
    ix = bulk_ix(cy, held)
    added = {}
    for lg in ("order", "algebra", "geometry", "information"):
        a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
        added[lg] = sorted({tuple(ix.decode[x][c[x]] for x in range(3)) for c in a} - set(held))
    six = sorted(set().union(*added.values()))
    if MUT.get("drop_offlattice"):
        six = six[:3]
    full = sorted(set(held) | set(six))
    r = cy.run(bulk_ix(cy, full), "1173", dict(OPTS))
    ev = {}
    for c in six:
        d = decode(c)
        ev[c] = CB.evaluate_sector(PP.sector(2.0 ** float(d["g"]), 2.0 ** float(d["s"])))
    return dict(held=held, added=added, six=six, decoded={c: decode(c) for c in six}, E_full={v["language"]: v["E"] for v in
                                                                                             r["verdicts"]}, n_full=len(full),
                ev=ev)


# ================================================================================ E3 each cell's own index
def region(i, j, names, P, c):
    out = []
    for w in WS:
        for z in ZS:
            for n in NS:
                s = CB.slacks(dict(i=i, j=j, w=w, z=z, n=n, law=0, mu=0, field=0), P, c)
                if all(s[k] >= 0 for k in names):
                    out.append((w, z, n))
    return out


def own_ix(cy, cells, orient):
    vals = [sorted({x[k] for x in cells}, reverse=orient[k]) for k in range(3)]
    return cy.Index("cell", list(OWN_COORDS), [list(x) for x in cells],
                    value_order={OWN_COORDS[k]: vals[k] for k in range(3)})


ORIENTS = list(itertools.product((False, True), repeat=3))       # reverse w, z, n


def closing_orders(cy, cells):
    """the orientations under which order and algebra add nothing (E = 0)"""
    out = []
    for o in (ORIENTS if not MUT.get("numeric_order") else ORIENTS[:1]):
        ix = own_ix(cy, cells, o)
        if all(len(cy.ADMISSION[lg][0](ix, dict(OPTS))[0]) == len(cells) for lg in ("order", "algebra")):
            out.append(o)
    return out


def cell_list(bc):
    """the eighteen cells: the twelve members and the six E2 adds, as (name, law, i, j)"""
    out = [(n, law, F(i), F(j)) for n, (law, i, j) in B5M.member_steps().items()]
    for c, d in bc["decoded"].items():
        out.append(("off-lattice %s g=%s s=%s" % (d["law"], d["g"], d["s"]), d["law"], d["i"], d["j"]))
    return out


def own_closure(cy, cells, c):
    P = default()
    by_ij = {}
    for name, law, i, j in cells:
        for rd, names in READINGS.items():
            key = (i, j, rd)
            if key not in by_ij:
                reg = region(i, j, names, P, c)
                orders = closing_orders(cy, reg)
                E = None
                if orders:
                    r = cy.run(own_ix(cy, reg, orders[0]), "1173", dict(OPTS))
                    E = {v["language"]: v["E"] for v in r["verdicts"]}
                by_ij[key] = dict(size=len(reg), orders=orders, E=E)
    return {(name, rd): by_ij[(i, j, rd)] for name, law, i, j in cells for rd in READINGS}, len({(i, j) for _, _, i, j in cells})


# ================================================================================ E4 what guarantees it
def graph(names, P, c, i=0, j=0):
    """the own coordinates each own condition ties (non-zero coefficients, from the forms' rows), kept only where the
    condition binds -- excludes some point of the scan that every other own condition admits"""
    rows, _ = CB.rows(P, c)
    box = [(w, z, n) for w in WS for z in ZS for n in NS]
    sl = {pt: CB.slacks(dict(i=i, j=j, w=pt[0], z=pt[1], n=pt[2], law=0, mu=0, field=0), P, c) for pt in box}
    edges = []
    for nm in names:
        tied = tuple(v for v in OWN_COORDS if rows[nm].get(v, 0) != 0)
        binds = any(sl[pt][nm] < 0 and all(sl[pt][o] >= 0 for o in names if o != nm) for pt in box)
        if len(tied) == 2 and binds:
            edges.append((nm, tied, tuple(rows[nm][v] for v in tied)))
    nodes = {v for _, t, _ in edges for v in t}
    tree = len(edges) == len(nodes) - 1 if nodes else True
    return edges, tree


def parity_closes(edges):
    """deduced: an edge a_u u + a_v v + ... >= 0 needs the two axes oriented so that their coefficients take opposite
    signs (o_u sign a_u = -o_v sign a_v); a forest always admits that, a cycle only when the product of -sign(a_u a_v)
    around it is +1 (one cycle here: w - z - n - w)"""
    if MUT.get("parity_flip"):
        prod = 1
        for _, t, (au, av) in edges:
            prod *= -((au > 0) - (au < 0)) * ((av > 0) - (av < 0))
        return prod == -1 or len(edges) < 3
    if len(edges) < 3:
        return True
    prod = 1
    for _, t, (au, av) in edges:
        prod *= -((au > 0) - (au < 0)) * ((av > 0) - (av < 0))
    return prod == 1


def guarantee(cy, c):
    P0 = default()
    out = dict(graph={rd: graph(names, P0, c) for rd, names in READINGS.items()}, lifts={}, sweeps={})
    for name, src, whose, hooks in CB.CONSTANTS:
        for hk in hooks:
            P = dict(P0)
            P[hk] = CB.LIFT[hk]
            for rd in ("regime as a regime", "regime as a bound"):
                out["lifts"][(name, hk, rd)] = bool(closing_orders(cy, region(0, 0, READINGS[rd], P, c)))
    for pc, qn in itertools.product((F(-1), F(0), F(1), F(2)), repeat=2):
        P = dict(P0)
        P["pc"], P["qN"] = pc, qn
        for rd in ("regime as a regime", "regime as a bound"):
            names = READINGS[rd]
            edges, tree = graph(names, P, c)
            out["sweeps"][(pc, qn, rd)] = dict(closed=bool(closing_orders(cy, region(0, 0, names, P, c))),
                                               predicted=parity_closes(edges), tree=tree)
    for beta in (F(-1), F(0), F(2)):
        P = dict(P0)
        P["beta"] = beta
        out["sweeps"][("beta", beta, "regime as a bound")] = dict(
            closed=bool(closing_orders(cy, region(0, 0, READINGS["regime as a bound"], P, c))), predicted=True, tree=False)
    return out


# ================================================================================ E5 each cell defends itself
def cell_defence(cells):
    """the Jacobian of the constants' quantities in (g, s, z, n) at each cell, from the forms (closed_bounds.ex)"""
    P = CB.DEFAULT
    out = {}
    for name, law, i, j in cells:
        def q(g, s, z, n):
            # (i, j) for G x 2^g, tension x 2^s: j = -s/2, i = g - j
            jj = j - F(s, 2) if not isinstance(s, F) else j - s / 2
            ii = i + g - (jj - j)
            e = CB.ex(ii, jj, 0, z, n, P)
            return {"hbar2": P["h"], "c2": P["cc"], "k4": e["k4"], "A": e["A"], "n2": e["n2"], "Eb": e["E"] + P["e"],
                    "ell2": e["ell2"], "L4": e["L4"], "E1": e["E1"], "Nmax": e["Nmax"]}
        f0 = q(0, 0, 0, 0)
        J = []
        for k in f0:
            J.append([q(*[1 if x == p else 0 for x in range(4)])[k] - f0[k] for p in range(4)])
        rk = CB.rank(J)
        out[name] = dict(dim_q=len(J), rank=rk, D=len(J) - rk)
    return out


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cc_cy")
    c = {k: F(v) for k, v in CB.BD.constants().items()}
    ev = CB.evaluate_members()
    b12 = CB.bulk_index(cy, ev, list(PP.MEMBERS))
    bc = bulk_closure(cy)
    cells = cell_list(bc)
    own, distinct = own_closure(cy, cells, c)
    return dict(b12=b12, bc=bc, cells=cells, own=own, distinct=distinct, g=guarantee(cy, c), D=cell_defence(cells),
                D_free=CB.defence(tuple(n for n, s, w, h in CB.CONSTANTS)))


def fmt_o(o):
    return "(" + ", ".join("%s %s" % (v, "falling" if r else "rising") for v, r in zip(OWN_COORDS, o)) + ")"


def report(o):
    print("cell_closure.py -- closure per cell, not of the whole bulk index (item 244)\n")
    b = o["b12"]
    print("E1 the twelve-member bulk index: E without the constants %s; with them as coordinates %s" % (b["E0"], b["E1"]))
    bc = o["bc"]
    print("\nE2 the cells the cypher adds: %s" % {lg: len(v) for lg, v in bc["added"].items()})
    for c, d in bc["decoded"].items():
        print("  %s -> law %-6s G x 2^(%s), tension x 2^(%s): (i, j) = (%s, %s), %s; constants %s" % (
            c, d["law"], d["g"], d["s"], d["i"], d["j"], "on the lattice" if d["on"] else "off the positions' lattice",
            "hold" if all(abs(x - 1) < 1e-12 for vs in bc["ev"][c].values() for x in vs) else "FAIL"))
    print("  with them: %d cells, E %s" % (bc["n_full"], bc["E_full"]))
    print("\nE3 each cell's own index (w, z, n; %d distinct own indexes over %d cells):" % (o["distinct"], len(o["cells"])))
    for name, law, i, j in o["cells"]:
        row = []
        for rd in READINGS:
            r = o["own"][(name, rd)]
            row.append("%s: %d cells, %s" % (rd, r["size"], "closed under %s" % " / ".join(fmt_o(x) for x in r["orders"])
                                                if r["orders"] else "OPEN in every order"))
        print("  %-34s %s" % (name, "; ".join(row)))
    first = o["own"][(o["cells"][0][0], "regime as a bound")]
    print("  every language's E under the closing order (ours, regime as a bound): %s" % first["E"])
    g = o["g"]
    print("\nE4 the own conditions' graph:")
    for rd, (edges, tree) in g["graph"].items():
        print("  %-20s %s -> %s" % (rd, [(n, t) for n, t, a in edges], "a tree" if tree else "a cycle"))
    print("  every constant lifted at a cell -- closed under some order: %s" % (
        "all" if all(g["lifts"].values()) else [k for k, v in g["lifts"].items() if not v]))
    print("  sweeps of the offset's power in the capacity (pc) and the README's power in the throat's area (qN):")
    for (a, b_, rd), r in g["sweeps"].items():
        if a == "beta":
            print("    curvature's power of sigma %s, %s: closed %s" % (b_, rd, r["closed"]))
            continue
        print("    pc %2s qN %2s  %-20s closed %-5s  the sign-parity rule says %-5s %s" % (
            a, b_, rd, r["closed"], r["predicted"], "" if r["closed"] == r["predicted"] else "DISAGREES"))
    print("\nE5 each cell's self-defence: %s; with every constant freed ⅅ = %d" % (
        sorted({(d["dim_q"], d["rank"], d["D"]) for d in o["D"].values()}), o["D_free"]["D"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    met = " ".join(open(METHOD, encoding="utf-8").read().split())
    add("E0 M's item-244 words and item 8's sentence verbatim in the rulings file; §15.3-§15.5's sentences verbatim in "
        "The_Method_1_6-2.md", M244 in rul and M8 in rul and all(q in met for q in READS))
    b = o["b12"]
    add("E1 the constants as coordinates leave the twelve-member bulk index's E unchanged in every language (order 6)",
        b["E0"] == b["E1"] and b["E0"]["order"] == 6)
    bc = o["bc"]
    ok = {lg: len(v) for lg, v in bc["added"].items()} == {"order": 6, "algebra": 6, "geometry": 6, "information": 3}
    ok &= len(bc["six"]) == 6 and not any(d["on"] for d in bc["decoded"].values())
    ok &= sorted({(d["g"], d["s"]) for d in bc["decoded"].values()}) == [(F(1, 3), F(-2, 3)), (F(5, 3), F(-4, 3))]
    ok &= all(abs(x - 1) < 1e-12 for c in bc["ev"] for vs in bc["ev"][c].values() for x in vs)
    ok &= bc["n_full"] == 18 and all(bc["E_full"][lg] == 0 for lg in LANGS)
    add("E2 the six cells the cypher adds are all off the positions' lattice (G x 2^(1/3), tension x 2^(-2/3); G x 2^(5/3), "
        "tension x 2^(-4/3); three laws each), each holds every constant with a form, and with them the bulk index is "
        "closed in every language (18 cells, E = 0)", ok)
    want = [(False, False, True), (True, True, False)]
    ok = len(o["cells"]) == 18 and o["distinct"] == 6
    ok &= all(o["own"][(n, rd)]["orders"] == want and o["own"][(n, rd)]["size"] > 0 for n, law, i, j in o["cells"]
              for rd in READINGS)
    ok &= all(r["E"] is not None and all(r["E"][lg] == 0 for lg in LANGS) for r in o["own"].values())
    add("E3 all eighteen cells' own indexes are closed in every language under every reading, under exactly two orders "
        "(w and z rising, the README falling, and the reverse); a cell's matter law enters none of its own conditions", ok)
    g = o["g"]
    ok = all(tree for edges, tree in g["graph"].values())
    ok &= [n for n, t, a in g["graph"]["regime as a bound"][0]] == ["plane positivity", "throat matter regime"]
    ok &= all(g["lifts"].values())
    sw = g["sweeps"]
    ok &= all(r["closed"] == r["predicted"] for r in sw.values())
    ok &= all(sw[(pc, qn, rd)]["closed"] for pc, qn, rd in sw if pc != "beta" and rd == "regime as a regime")
    ok &= all(sw[(pc, qn, rd)]["closed"] == (not (pc < 0 and qn > 0)) for pc, qn, rd in sw
              if pc != "beta" and rd == "regime as a bound")
    ok &= all(r["closed"] for (a, b_, rd), r in sw.items() if a == "beta")
    add("E4 under the stated forms the binding own conditions form a tree in every reading (as a bound, the regime makes "
        "the capacity redundant); every lift keeps every cell closed; with the regime as a bound the cell opens exactly "
        "when the capacity's offset power is negative and the throat area's README power positive; the cypher agrees "
        "with the binding sign-parity rule at every point", ok)
    D = o["D"]
    add("E5 every cell defends itself: dim q 10, rank 4, ⅅ = 6 at all eighteen; 0 with every constant freed",
        len(D) == 18 and all((d["dim_q"], d["rank"], d["D"]) == (10, 4, 6) for d in D.values()) and o["D_free"]["D"] == 0)
    return res


MUTANTS = {"regime_sign": "the README's power in the throat's area taken as -1",
           "numeric_order": "only the numeric order tried",
           "drop_offlattice": "three of the six added cells left out",
           "parity_flip": "the sign-parity rule inverted"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
