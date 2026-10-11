#!/usr/bin/env python3
"""unit_cell.py -- item 246: the unit cell completed, and the bulk index as the infinite index it is.  M: "add the other
six to complete the unit cell" -- and, of the board's "The bulk index now holds eighteen universes": "no, it contains
infinite universes".  Worked in the conversation (computed, exact where marked; deduced where marked; not verified by a
separate session; not seated); 2026-10-11.

The other six are bulk5_index.UNIT_REST: two thirds of a 2P step (G x 2^(2/3), tension x 2^(-4/3)) and 2b with a third
of one (G x 2^(4/3), tension x 2^(-2/3)), under each law.  bulk5_index.UNIT_CELL holds the twenty-four: i in {0, 1}, j
in {0, 1/3, 2/3, 1}, three laws.  They are the bulk index's unit cell, not the index.

  U0 (read) M's item-246 words, verbatim in the rulings file.
  U1 (computed, exact) The other six, built as the rest were.  Their 5D side agrees with p2_planck.sector to 1e-12;
     every constant with a form holds on them (closed_bounds' evaluator, 1e-12); each one's own index is closed under
     its own conditions (cell_closure's test, both regime readings).  They add no 5D geometry: 2P x 2/3 is in ours'
     geometry, 2b + 2P/3 in 2b's, each with coupling x 4.  The cell then holds eight 5D bulks, and each geometry carries
     four couplings in doublings -- ours' x 1, x 2, x 4, x 8; 2b's x 2, x 4, x 8, x 16 -- sharing three.  Four of the
     cell lie on 2P's ray (tension in their own Planck units ours): ours, 2P/3, 2P x 2/3 and 2P, a third apart.
  U2 (computed) Plausibility and weight: the windows agree with p2_planck.window on both floors; weights, relative /
     absolute: 2P x 2/3 (W - 2/3)/W and (W - 4/3)/W; 2b + 2P/3 (W - 2)/W and (W - 8/3)/W.
  U3 (computed; the cypher, roster 1173, audited, each axis ordered away from ours) The cell: closed in both bases in
     every language (E = 0); no key, no one-hot code.  Leave one out (order): in 201's basis every member is predicted
     by the other twenty-three; in the 5D basis all but the two far corners, 2a-mirror and 2b+2P.
  U4 (computed, exact; the cypher) The infinite index.  The bulk index is the lattice of (law, i, j), i whole, j in
     thirds, each law -- every one of its universes is a cell member moved by whole steps of 2b and 2P, so it holds
     infinitely many universes.  The cypher takes finite indexes, so it is asked of the cell's translates and of windows
     of cells, in both bases.  Every translate tried -- toward stronger gravity and weaker, along 2b, 2P and both -- is
     closed in every language, each axis ordered away from the translate's own base.  Windows of 2 x 2, 3 x 3 and
     4 x 2 cells reaching out from ours are closed.  A window of 2 x 2 cells around ours is closed in 201's basis under
     every order, and in the 5D basis under exactly two (the geometry axis and the coupling axis running opposite ways),
     open under the other two -- closure under some order, as §15.3 asks.  No window admits a universe between the
     thirds: the cypher's completion stops at the cell's step.  The plausible part, on the thirds: i <= 98 and j <=
     196 2/3 (relative floor), reaching the scanned box's lower edge -- infinite, as item 233's K3 found on the coarser
     lattice.
  U5 (deduced) What item 246 corrects.  The members the instruments compute -- twelve (item 233), eighteen (item 245),
     twenty-four (here) -- are cells of the bulk index, not the index.  The index is infinite on the lattice alone, and
     item 233's unseen axes (the offset's ratio; the matter law between and beyond the three computed) are continuous
     besides; this item does not cut them.

What this does not show.
  - Closure of the whole: M ruled (item 247) that the infinite index is not closed and never can be -- whatever can be
    imagined is plausible, and each imagined universe reopens it (open_index.py).  The windows here are closed; the
    whole is not.
  - The unit cell's matter is the three computed laws; the law between them is unseen (item 233 K7).

Imports bulk5_index.py (and through it p2_planck.py, p2_gravity.py), closed_bounds.py, cell_closure.py, tools/cypher.py
and index_audit.py by path.  Stdlib.  python3 unit_cell.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M246 = ("add the other six to complete the unit cell The bulk index now holds eighteen universes - no, it contains "
        "infinite universes")
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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "uc_b5")
PP, PG = B5.PP, B5.PG
REST = list(B5.UNIT_REST)


def cell_members():
    m = dict(B5.UNIT_CELL)
    if MUT.get("wrong_rest"):
        law, g, s = m["2b+2P/3"]
        m["2b+2P/3"] = (law, g, F(-4, 3))
    if MUT.get("cell_missing"):
        m.pop("2c+2P/3-mirror")
    return m


# ================================================================================ the two bases
def cell5(law, i, j):
    """(matter, 3 ell/l5, kappa5^4) = (law, -2i, i + 3j)"""
    return (B5.LAW_ORDER.index(law) if isinstance(law, str) else law, int(-2 * i), int(i + 3 * j))


def cell201(law, i, j):
    """(matter, 3 sigma_SI, sigma/sigma_P) = (law, -6j, 2i)"""
    return (B5.LAW_ORDER.index(law) if isinstance(law, str) else law, int(-6 * j), int(2 * i))


BASES = {"5D": (cell5, ["matter", "ell_l5_x3", "kappa5_4"]), "201": (cell201, ["matter", "sigma_SI_x3", "sigma_planck"])}


def run_index(cy, held, coords, base=None, orient=None):
    vals = [[0, 1, 2]]
    for x in (1, 2):
        vs = sorted({c[x] for c in held})
        if orient is not None:
            vals.append(sorted(vs, reverse=orient[x - 1]))
        else:
            b = base[x] if base is not None else 0
            vals.append(sorted(vs, key=lambda v: (abs(v - b), v)))
    ix = cy.Index("bulk_cell", coords, [list(c) for c in held], value_order={coords[x]: vals[x] for x in range(3)})
    r = cy.run(ix, "1173", dict(OPTS))
    return {v["language"]: v["E"] for v in r["verdicts"]}, ix


def window(irange, j3range, basis):
    f = BASES[basis][0]
    return sorted({f(law, F(i), F(j3, 3)) for law in range(3) for i in irange for j3 in j3range})


# ================================================================================ U1, U2 the other six
def build(members):
    fd = B5.five_d_bulk(members)
    cb = _load(os.path.join(HERE, "closed_bounds.py"), "uc_cb")
    ev = {n: cb.evaluate_sector(PP.sector(fd[n]["gf"], fd[n]["sf"])) for n in REST if n in fd}
    by_bulk, by_geom = {}, {}
    for n, v in fd.items():
        by_bulk.setdefault((v["e"]["k4"], v["e"]["ell2"]), []).append(n)
        by_geom.setdefault(v["e"]["ell_l5"], []).append(n)
    couplings = {gm: sorted({fd[n]["e"]["k4"] for n in ns}) for gm, ns in by_geom.items()}
    ray = sorted(n for n, v in fd.items() if v["e"]["sigma_planck"] == 0 and v["law"] == "ours")
    return fd, ev, by_bulk, by_geom, couplings, ray


def own_closure(fd):
    """cell_closure's own-index test at the other six's (i, j), both regime readings"""
    cc = _load(os.path.join(HERE, "cell_closure.py"), "uc_cc")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "uc_cy2")
    c = {k: F(v) for k, v in cc.CB.BD.constants().items()}
    out = {}
    for n in REST:
        if n not in fd:
            continue
        i, j = fd[n]["i"], fd[n]["j"]
        for rd in ("regime as a regime", "regime as a bound"):
            key = (i, j, rd)
            if key not in out:
                out[key] = cc.closing_orders(cy, cc.region(i, j, cc.READINGS[rd], cc.default(), c))
    return out


def windows_w(fd, k):
    out = {}
    for n in REST:
        if n not in fd:
            continue
        v = fd[n]
        wn = PP.window(v["gf"], v["sf"])
        row = {}
        for floor, need in (("rel", wn["need_rel"]), ("abs", wn["need_abs"])):
            lo, hi = max(k["S0"], need), min(k["S1"], wn["need_top"])
            iv = B5.w_interval(v["i"], v["j"], k, floor)
            agree = (lo > hi) if iv is None else (abs(math.log2(lo / k["S0"]) - iv[0]) < 1e-9
                                                    and abs(math.log2(hi / k["S0"]) - iv[1]) < 1e-9)
            row[floor] = dict(weight=B5.weight(v["i"], v["j"], k, floor), agree=agree)
        out[n] = row
    return out


# ================================================================================ U3 the cell; U4 the infinite index
def cell_cypher(cy, ia, fd):
    out = {}
    for basis, (f, coords) in BASES.items():
        cells = {n: f(v["law"], v["i"], v["j"]) for n, v in fd.items()}
        held = sorted(set(cells.values()))
        E, ix = run_index(cy, held, coords)
        loo = {}
        for n in fd:
            rest = sorted({c for m, c in cells.items() if m != n})
            if cells[n] in rest:
                loo[n] = True
                continue
            _, ixr = run_index(cy, rest, coords)
            a, _ = cy.ADMISSION["order"][0](ixr, dict(OPTS))
            loo[n] = cells[n] in {tuple(ixr.decode[x][c[x]] for x in range(3)) for c in a}
        out[basis] = dict(n=len(held), E=E, audit=ia.audit_index(coords, held), loo=loo)
    return out


TRANSLATES = ((0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (2, 3), (-3, -2))
WINDOWS = ((2, 2), (3, 3), (4, 2))


def infinite(cy):
    out = dict(translates={}, windows={}, straddle={})
    for basis, (f, coords) in BASES.items():
        for a, b in TRANSLATES:
            held = window(range(a, a + 2), range(3 * b, 3 * b + 4), basis)
            E, _ = run_index(cy, held, coords, base=f(0, F(a), F(b)))
            out["translates"][(basis, a, b)] = (len(held), E)
        for m, n in WINDOWS:
            held = window(range(0, m + 1), range(0, 3 * n + 1), basis)
            E, _ = run_index(cy, held, coords, base=f(0, F(0), F(0)))
            out["windows"][(basis, m, n)] = (len(held), E)
        held = window(range(-1, 2), range(-3, 4), basis)
        orients = list(itertools.product((False, True), repeat=2)) if not MUT.get("no_orient") else [None]
        res = {}
        for o in orients:
            E, _ = run_index(cy, held, coords, base=f(0, F(0), F(0)) if o is None else None, orient=o)
            res[o] = E
        out["straddle"][basis] = (len(held), res)
    # anything between the thirds?  every window's admitted cells decode to j in thirds (E = 0 means nothing admitted)
    return out


def plausible_thirds(k, span=120):
    pts = [(i, F(j3, 3)) for i in range(-span, span + 1) for j3 in range(-3 * span, 6 * span + 1)
           if B5.w_interval(i, F(j3, 3), k, "rel")]
    return dict(imax=max(i for i, _ in pts), jmax=max(j for _, j in pts),
                reaches_edge=any(i == -span or j == -span for i, j in pts), n=len(pts))


def translate_exact(fd):
    """every lattice universe is a member of the cell's half-open part moved by whole 2b, 2P steps (checked on a box)"""
    half = {(law, F(0), F(j3, 3)) for law in B5.LAW_ORDER for j3 in range(3)}
    ok = True
    for law in B5.LAW_ORDER:
        for i in range(-4, 5):
            for j3 in range(-12, 13):
                j = F(j3, 3)
                a, b = i, math.floor(j)
                ok &= (law, F(i - a), j - b) in half and B5.lattice_member(law, i, j) == (law, i + j, -2 * j)
    return ok


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "uc_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "uc_ia")
    k = B5.constants()
    fd, ev, by_bulk, by_geom, cpl, ray = build(cell_members())
    return dict(fd=fd, ev=ev, by_bulk=by_bulk, by_geom=by_geom, cpl=cpl, ray=ray, own=own_closure(fd),
                win=windows_w(fd, k), k=k, cell=cell_cypher(cy, ia, fd), inf=infinite(cy), pl=plausible_thirds(k),
                tr=translate_exact(fd))


def report(o):
    print("unit_cell.py -- the unit cell completed; the bulk index as the infinite index it is (item 246)\n")
    print("U1 the other six:")
    for n in REST:
        if n not in o["fd"]:
            continue
        v = o["fd"][n]
        e = v["e"]
        print("  %-17s law %-6s (i, j) (%s, %s) | kappa5^4 %s ell^2 %s ell/l5 %s sigma/sigma_P %s E1 %s  %s; constants %s" % (
            n, v["law"], v["i"], v["j"], e["k4"], e["ell2"], e["ell_l5"], e["sigma_planck"], e["E1"],
            "agrees" if v["agree"] else "DISAGREES",
            "hold" if all(abs(x - 1) < 1e-12 for vs in o["ev"][n].values() for x in vs) else "FAIL"))
    print("  own index closed: %s" % {"%s,%s %s" % kk: bool(v) for kk, v in o["own"].items()})
    print("  the cell: %d 5D bulks; geometries %s; couplings per geometry %s; on 2P's ray: %s" % (
        len(o["by_bulk"]), {str(kk): len(vv) for kk, vv in o["by_geom"].items()},
        {str(kk): [str(x) for x in vv] for kk, vv in o["cpl"].items()}, o["ray"]))
    print("\nU2 weights (relative, absolute): %s" % {n: ("%.6f" % r["rel"]["weight"], "%.6f" % r["abs"]["weight"],
                                                          r["rel"]["agree"] and r["abs"]["agree"]) for n, r in o["win"].items()})
    print("\nU3 the cell through the cypher:")
    for b, r in o["cell"].items():
        print("  %s: %d cells, E %s, audit %s" % (b, r["n"], r["E"], r["audit"]))
        print("     predicted by the rest (order): %s" % sorted(n for n, x in r["loo"].items() if x))
    inf = o["inf"]
    print("\nU4 the infinite index -- every lattice universe a cell member moved by whole steps: %s" % o["tr"])
    for (b, a, bb), (n, E) in inf["translates"].items():
        print("  %-3s cell moved by (%2d 2b, %2d 2P): %d cells, E %s" % (b, a, bb, n, {k: v for k, v in E.items() if v is not None}))
    for (b, m, n), (c, E) in inf["windows"].items():
        print("  %-3s window of %d x %d cells from ours: %d cells, E %s" % (b, m, n, c, {k: v for k, v in E.items() if v is not None}))
    for b, (c, res) in inf["straddle"].items():
        print("  %-3s 2 x 2 cells around ours: %d cells; worst E by order (reverse geometry/SI, reverse coupling/Planck): %s" % (
            b, c, {str(o_): max(v for v in E.values() if v is not None) for o_, E in res.items()}))
    pl = o["pl"]
    print("  plausible on the thirds (relative floor): i <= %d, j <= %s; reaches the box's lower edge: %s (%d in the box)" % (
        pl["imax"], pl["jmax"], pl["reaches_edge"], pl["n"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("U0 M's item-246 words verbatim in the rulings file", M246 in rul)
    fd = o["fd"]
    ok = len(fd) == 24 and all(v["agree"] for v in fd.values())
    e1, e2 = fd["2P*2/3"]["e"], fd["2b+2P/3"]["e"]
    ok &= (e1["k4"], e1["ell_l5"], e1["sigma_planck"]) == (2, 0, 0) and (e2["k4"], e2["ell_l5"], e2["sigma_planck"]) == (
        2, F(-2, 3), 2)
    ok &= all(abs(x - 1) < 1e-12 for n in o["ev"] for vs in o["ev"][n].values() for x in vs) and len(o["ev"]) == 6
    ok &= all(o["own"].values()) and len(o["own"]) == 4
    ok &= len(o["by_bulk"]) == 8 and sorted(o["by_geom"]) == [F(-2, 3), F(0)]
    ok &= o["cpl"][F(0)] == [0, 1, 2, 3] and o["cpl"][F(-2, 3)] == [1, 2, 3, 4]
    ok &= o["ray"] == sorted(["ours", "2P/3", "2P*2/3", "2P"])
    add("U1 the other six exact (1e-12), every constant holds on them, each own index closed; eight 5D bulks, still two "
        "geometries, each with four couplings in doublings (x1-x8, x2-x16); ours, 2P/3, 2P x 2/3 and 2P on 2P's ray", ok)
    W = o["k"]["W"]
    w = o["win"]
    ok = len(w) == 6 and all(r["agree"] for row in w.values() for r in row.values())
    ok &= abs(w["2P*2/3"]["rel"]["weight"] - (W - 2 / 3) / W) < 1e-12 and abs(w["2P*2/3"]["abs"]["weight"] - (W - 4 / 3) / W) < 1e-12
    ok &= abs(w["2b+2P/3"]["rel"]["weight"] - (W - 2) / W) < 1e-12 and abs(w["2b+2P/3"]["abs"]["weight"] - (W - 8 / 3) / W) < 1e-12
    add("U2 the other six's windows agree with p2_planck.window; weights 2P x 2/3 (W-2/3)/W, (W-4/3)/W; 2b + 2P/3 (W-2)/W, "
        "(W-8/3)/W", ok)
    ce = o["cell"]
    ok = all(ce[b]["n"] == 24 and all(ce[b]["E"][lg] == 0 for lg in LANGS) for b in BASES)
    ok &= all(not ce[b]["audit"]["keys"] and not ce[b]["audit"]["onehot"] for b in BASES)
    ok &= all(ce["201"]["loo"].values()) and sorted(n for n, x in ce["5D"]["loo"].items() if not x) == ["2a-mirror", "2b+2P"]
    add("U3 the unit cell (24) is closed in both bases in every language (E = 0), no key, no one-hot; left out, every "
        "member is predicted by the rest in 201's basis, all but 2a-mirror and 2b+2P in the 5D basis", ok)
    inf = o["inf"]
    ok = o["tr"]
    ok &= all(n == 24 and all(E[lg] == 0 for lg in LANGS) for n, E in inf["translates"].values())
    ok &= all(all(E[lg] == 0 for lg in LANGS) for n, E in inf["windows"].values())
    s201 = inf["straddle"]["201"][1]
    s5 = inf["straddle"]["5D"][1]
    ok &= all(all(E[lg] == 0 for lg in LANGS) for E in s201.values()) and len(s201) == 4
    closing5 = sorted(o_ for o_, E in s5.items() if o_ is not None and all(E[lg] == 0 for lg in LANGS))
    ok &= closing5 == [(False, True), (True, False)]
    pl = o["pl"]
    ok &= pl["imax"] == 98 and pl["jmax"] == F(590, 3) and pl["reaches_edge"]
    add("U4 every lattice universe is a cell member moved by whole steps; every translate tried and every window from ours "
        "closed in both bases; 2 x 2 cells around ours closed in 201's basis under every order and in the 5D basis under "
        "exactly the two opposite orders; nothing admitted between the thirds; the plausible part infinite (i <= 98, "
        "j <= 196 2/3, reaching the box's edge)", ok)
    return res


MUTANTS = {"wrong_rest": "2b + 2P/3 given the tension x 2^(-4/3)",
           "cell_missing": "one of the other six left out",
           "no_orient": "the straddling window tried only in the order away from ours"}


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
        print("  mutant %-13s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
