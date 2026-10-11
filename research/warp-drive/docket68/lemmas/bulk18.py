#!/usr/bin/env python3
"""bulk18.py -- item 245: the bulk index with the six in-between universes added.  M: "add the six in-between universes
to the bulk index".  The six are bulk5_index.IN_BETWEEN (G x 2^(1/3) with the tension x 2^(-2/3), a third of a 2P step;
G x 2^(5/3) with x 2^(-4/3), 2b and two thirds of one; each under the three matter laws), and bulk5_index.BULK holds the
eighteen.  Item 233's twelve-member results stay as recorded in bulk5_index K1-K7.  Worked in the conversation
(computed, exact where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-11.

  X0 (read) M's item-245 words, verbatim in the rulings file.
  X1 (computed, exact) The six's 5D side, built as the twelve were: kappa5^4, ell^2, Lambda5, G5, l5, ell/l5,
     sigma/sigma_P, N_max, E1 and m1 as exact powers of 2 (thirds), each agreeing with p2_planck.sector to 1e-12, and
     (ell/l5)^3 x sigma/sigma_P = ours on all eighteen.  Each of the six sits in a 5D bulk of its own -- (kappa5^4 x 2,
     ell^2 x 2^(1/3)) and (x 8, x 2^(-1/3)) -- six bulks in all.  They add no 5D geometry: the eighteen sit in the two
     the positions had.  2P/3 is in ours' geometry with 2b's coupling, and its tension in its own Planck units is ours,
     as 2P's is -- it lies a third of the way along 2P's ray; 2b + 2/3 2P is in 2b's geometry with 2P's coupling.  Each
     geometry now carries three couplings: ours' x 1, x 2, x 8; 2b's x 2, x 8, x 16.
  X2 (computed, exact) The lattice.  Every one of the eighteen is a whole-number combination of 2b and a third of 2P;
     the positions' lattice (2b and 2P) is a sublattice of index 3 in it.  As (law, i, j): the twelve at i, j in {0, 1},
     the six at (0, 1/3) and (1, 2/3).  In 201's basis the six carry tensions in SI no position carries (x 2^(-2/3),
     x 2^(-4/3)).
  X3 (computed) Plausibility and weight, as item 233 computed them: each window agrees with p2_planck.window to 1e-9
     on both floors; weights, relative / absolute: 2P/3 (W - 1/3)/W and (W - 2/3)/W; 2b + 2/3 2P (W - 2)/W and
     (W - 10/3)/W.  All six are plausible.
  X4 (computed; the cypher, roster 1173, audited, each axis ordered away from ours) The eighteen as an index.
     - 5D basis (matter, 3 ell/l5, kappa5^4): closed in every language (E = 0); no key, no one-hot code.
     - 201's basis (matter, 3 sigma_SI, sigma/sigma_P): not closed -- order, algebra and geometry admit six more
       (information three): two thirds of a 2P step (G x 2^(2/3), tension x 2^(-4/3); (i, j) = (0, 2/3)) and 2b with a
       third of one (G x 2^(4/3), tension x 2^(-2/3); (1, 1/3)), under each law.  They are the rest of the finer
       lattice's unit cell (i in {0, 1}, j in {0, 1/3, 2/3, 1}); with them -- twenty-four -- the index is closed in
       both bases.  Recorded, not added: item 245 names six.  Whether the bulk index's closure is read in the bulk's own
       5D basis (eighteen suffice) or in 201's (twenty-four) is a basis question this item does not settle.
     - Leave one out (5D basis): which members the other seventeen predict, per language.  Each of the six is predicted
       under order and algebra; 2a-mirror and 2b+2P, the box's far corners, by no language.
  X5 (computed; deduced where marked) What moves in the instruments that read the members, re-run against the
     eighteen.  weight_cypher V6 (G from the bulk and the plane): holds on the six, numerically and exactly.  copy_p2
     C1 (the README-matched corridor on position 2's side): size x 2^(1/6) and mass-energy x 2^(-1/6) at 2P/3, x 2^(5/6)
     and x 2^(-5/6) at 2b + 2/3 2P.  copy_p2's bodies: a 1e22 kg body's surface gravity at the six's G under each law.
     copy_p2 C5 (the variances as an index: law, G, Lambda4): reported over the eighteen beside the twelve.
     weight_cypher V2 (the positions' maximum-entropy weights in 201's box): the six fall outside the box (their SI
     tensions are values the positions never carry), so it gives them no weight; what V2 measures is unchanged.
     closed_bounds C2 and cell_closure E2-E3 already hold the six (every constant holds; each own index closed).
     relgrav reads ours and 2a alone: unchanged.  Deduced: the instruments that scan the integer lattice (bounds B3,
     wbound, weight_address) report half-planes and directions; a region cut by linear bounds is finite on a lattice
     exactly when its polyhedron is bounded, whatever the step, so the finer lattice moves none of their findings, only
     their point counts.  Not re-run.

What this does not show.
  - The six are the cypher's completion of the 5D basis; no position builds them.  Their matter is the three computed
    laws, unchanged.
  - Item 233's "possible" was what the positions generate; the eighteen generate a finer lattice, reported (X2), and
    which of the two is "possible" is a reading this item does not settle.

Imports bulk5_index.py (and through it p2_planck.py, p2_gravity.py), p2_matter.py, tools/cypher.py and index_audit.py
by path.  Stdlib.  python3 bulk18.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M245 = "add the six in-between universes to the bulk index"
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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "b18_b5")
PP, PG = B5.PP, B5.PG
SIX = list(B5.IN_BETWEEN)


def bulk():
    members = dict(B5.BULK)
    if MUT.get("wrong_third"):
        law, g, s = members["2P/3"]
        members["2P/3"] = (law, g, F(-1, 3))
    if MUT.get("drop_six"):
        members = {n: v for n, v in members.items() if n not in SIX[:3]}
    return members


# ================================================================================ X1 the 5D side; X2 the lattice
def bulks_geoms(fd):
    by_bulk, by_geom = {}, {}
    for n, v in fd.items():
        by_bulk.setdefault((v["e"]["k4"], v["e"]["ell2"]), []).append(n)
        by_geom.setdefault(v["e"]["ell_l5"], []).append(n)
    couplings = {gm: sorted({fd[n]["e"]["k4"] for n in ns}) for gm, ns in by_geom.items()}
    return by_bulk, by_geom, couplings


def lattice_coords(g, s):
    return (g + s / 2, -3 * s / 2)


def lattice(fd):
    """each member as a 2b + b (2P/3): g = a + b/3, s = -2b/3, so b = -3s/2, a = g + s/2"""
    out = {}
    for n, v in fd.items():
        b = -3 * v["s"] / 2
        a = v["g"] + v["s"] / 2
        out[n] = (a, b, a.denominator == 1 and b.denominator == 1)
    # the positions' generators in the (2b, 2P/3) basis: 2b = (1, 0), 2P = (0, 3): index |det| = 3
    gens = [out_ for out_ in (lattice_coords(F(1), F(0)), lattice_coords(F(1), F(-2)))]
    index = abs(gens[0][0] * gens[1][1] - gens[0][1] * gens[1][0])
    return out, index


# ================================================================================ X3 plausibility and weight
def windows(fd, k):
    out = {}
    for n in SIX:
        v = fd[n]
        i, j = v["i"], v["j"]
        wn = PP.window(v["gf"], v["sf"])
        row = {}
        for floor, need in (("rel", wn["need_rel"]), ("abs", wn["need_abs"])):
            lo = max(k["S0"], need)
            hi = min(k["S1"], wn["need_top"])
            iv = B5.w_interval(i, j, k, floor)
            agree = (lo > hi) if iv is None else (abs(math.log2(lo / k["S0"]) - iv[0]) < 1e-9
                                                    and abs(math.log2(hi / k["S0"]) - iv[1]) < 1e-9)
            row[floor] = dict(iv=iv, weight=B5.weight(i, j, k, floor), agree=agree)
        out[n] = row
    return out


# ================================================================================ X4 the cypher
def cell5(v):
    return (B5.LAW_ORDER.index(v["law"]), int(3 * v["e"]["ell_l5"]), int(v["e"]["k4"]) if not MUT.get("integer_cast")
            else int(v["e"]["k4"]))


def cell201(v):
    s3 = 3 * v["e"]["sigma"]
    return (B5.LAW_ORDER.index(v["law"]), int(s3) if not MUT.get("integer_cast") else int(v["e"]["sigma"]),
            int(v["e"]["sigma_planck"]))


def index(cy, held, coords, name):
    vals = [sorted({c[x] for c in held}, key=lambda t: (abs(t), t)) for x in range(len(coords))]
    return cy.Index(name, coords, [list(c) for c in held], value_order={coords[x]: vals[x] for x in range(len(coords))})


def admitted(cy, ix, lg):
    a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
    return None if a is None else {tuple(ix.decode[x][c[x]] for x in range(len(ix.coords))) for c in a}


def cypher18(cy, ia, fd):
    out = {}
    for basis, f, coords in (("5D", cell5, ["matter", "ell_l5_x3", "kappa5_4"]),
                             ("201", cell201, ["matter", "sigma_SI_x3", "sigma_planck"])):
        cells = {n: f(v) for n, v in fd.items()}
        held = sorted(set(cells.values()))
        ix = index(cy, held, coords, "bulk18_" + basis)
        run = cy.run(ix, "1173", dict(OPTS))
        out[basis] = dict(n=len(held), E={v["language"]: v["E"] for v in run["verdicts"]}, run=run,
                          audit=ia.audit_index(coords, held), cells=cells)
    # leave one out, 5D basis: does the index of the other members admit the one left out?
    cells = out["5D"]["cells"]
    loo = {}
    for n in fd:
        rest = sorted({c for m, c in cells.items() if m != n})
        if cells[n] in rest:
            loo[n] = {lg: True for lg in ("order", "algebra", "geometry", "information")}
            continue
        ix = index(cy, rest, ["matter", "ell_l5_x3", "kappa5_4"], "bulk18_loo")
        row = {}
        for lg in ("order", "algebra", "geometry", "information"):
            try:
                adm = admitted(cy, ix, lg)
            except Exception:
                adm = None
            row[lg] = None if adm is None else cells[n] in adm
        loo[n] = row
    out["loo"] = loo
    # 201's basis: what it admits beyond the eighteen, decoded (s = sigma_SI_x3 / 3, p = 2g + s), and the finer lattice's
    # unit cell (twenty-four) in both bases
    cells = out["201"]["cells"]
    held = sorted(set(cells.values()))
    ix = index(cy, held, ["matter", "sigma_SI_x3", "sigma_planck"], "bulk18_201")
    extra = {}
    for lg in ("order", "algebra", "geometry", "information"):
        add = sorted(admitted(cy, ix, lg) - set(held))
        extra[lg] = sorted({(B5.LAW_ORDER[c[0]], (c[2] - F(c[1], 3)) / 2, F(c[1], 3)) for c in add})
    unit = dict(fd)
    for i in (0, 1):
        for j in (F(1, 3), F(2, 3)):
            for law in B5.LAW_ORDER:
                g, s_ = i + j, -2 * j
                if not any((v["law"], v["g"], v["s"]) == (law, g, s_) for v in fd.values()):
                    unit["cell(%s,%s)-%s" % (i, j, law)] = None
    members = {n: (v["law"], v["g"], v["s"]) for n, v in fd.items()}
    for n in unit:
        if n not in fd:
            i, j, law = n[5:].split("-")[0].strip("()").split(",") + [n.split("-")[-1]]
            jj = F(j)
            members[n] = (law, int(i) + jj, -2 * jj)
    fd24 = B5.five_d_bulk(members)
    E24 = {}
    for basis, f, coords in (("5D", cell5, ["matter", "ell_l5_x3", "kappa5_4"]),
                             ("201", cell201, ["matter", "sigma_SI_x3", "sigma_planck"])):
        h = sorted({f(v) for v in fd24.values()})
        r = cy.run(index(cy, h, coords, "bulk24_" + basis), "1173", dict(OPTS))
        E24[basis] = dict(n=len(h), E={v["language"]: v["E"] for v in r["verdicts"]})
    out["extra201"] = extra
    out["unit24"] = E24
    return out


# ================================================================================ X5 what moves downstream
def downstream(cy, ia, fd):
    c4 = PG.C ** 4
    v6 = {}
    for n in SIX:
        v = fd[n]
        sec = PP.sector(v["gf"], v["sf"])
        sms = sec["k4"] * sec["sigma"] * c4 / (48 * math.pi)
        curv = 3 * c4 / (4 * math.pi * sec["ell"] ** 2 * (sec["sigma"] - 2 * sec["offset"]))
        v6[n] = dict(sms=abs(sms / sec["G"] - 1), curv=abs(curv / sec["G"] - 1),
                     exact=v["e"]["G"] == v["e"]["k4"] + v["e"]["sigma"])
    c1 = {n: dict(size=fd[n]["g"] / 2, energy=-fd[n]["g"] / 2) for n in SIX}
    pm = _load(os.path.join(HERE, "p2_matter.py"), "b18_pm")
    o = pm.compute()
    bodies = {}
    for n in SIX:
        v = fd[n]
        row = {}
        for el in ("Cu", "Ag", "Au"):
            s0 = o["sol"][(el, "ours")]
            g0 = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], PG.G)["g"]
            s = o["sol"][(el, v["law"])]
            row[el] = PG.body(1e22, s["rho"], s["B0"] * 1e9, s["Bp"], PG.G * v["gf"])["g"] / g0
        bodies[n] = row
    # copy_p2 C5's variance index (law, log2 G, log2 Lambda4), in thirds, over the twelve and the eighteen
    def c5(members):
        cells = sorted({(B5.LAW_ORDER.index(fd[n]["law"]), int(3 * fd[n]["e"]["G"]),
                         int(3 * (fd[n]["e"]["G"] + fd[n]["e"]["sigma"]))) for n in members})
        coords = ["matter_law", "log2_G_x3", "log2_Lambda4_x3"]
        ix = index(cy, cells, coords, "copy_variances18")
        rows, keys = cy.coordinate_report(ix)
        run = cy.run(ix, "1173", dict(OPTS))
        return dict(n=len(cells), E={v["language"]: v["E"] for v in run["verdicts"]},
                    adds_nothing=[r["coordinate"] for r in rows if r["adds_nothing"]], audit=ia.audit_index(coords, cells))
    twelve = [n for n in fd if n not in SIX]
    # weight_cypher V2's box in 201's basis: the positions' values (sigma_SI exponent 0 or -2, sigma/sigma_P 0 or 2)
    v2_box = {(a, s, p) for a in range(3) for s in (0, -2) for p in (0, 2)}
    v2_out = {n: (B5.LAW_ORDER.index(fd[n]["law"]), fd[n]["e"]["sigma"], fd[n]["e"]["sigma_planck"]) not in v2_box
              for n in SIX}
    return dict(v6=v6, c1=c1, bodies=bodies, c5_12=c5(twelve), c5_18=c5(list(fd)), v2_out=v2_out)


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "b18_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "b18_ia")
    fd = B5.five_d_bulk(bulk())
    k = B5.constants()
    lat, idx = lattice(fd)
    return dict(fd=fd, bg=bulks_geoms(fd), lat=lat, idx=idx, k=k, win=windows(fd, k) if "2P/3" in fd else {},
                cy=cypher18(cy, ia, fd), ds=downstream(cy, ia, fd) if all(n in fd for n in SIX) else None)


def report(o):
    print("bulk18.py -- the bulk index with the six in-between universes (item 245)\n")
    print("X1 the six's 5D side (exponents of 2 against ours):")
    for n in SIX:
        if n not in o["fd"]:
            continue
        v = o["fd"][n]
        e = v["e"]
        print("  %-17s law %-6s (i, j) (%s, %s) | kappa5^4 %s ell^2 %s Lambda5 %s G5 %s l5 %s ell/l5 %s | sigma/sigma_P %s "
              "N_max %s E1 %s m1 %s  %s" % (n, v["law"], v["i"], v["j"], e["k4"], e["ell2"], e["L5"], e["G5"], e["l5"],
                                            e["ell_l5"], e["sigma_planck"], e["N_max"], e["E1"], e["m1"],
                                            "agrees" if v["agree"] else "DISAGREES"))
    by_bulk, by_geom, cpl = o["bg"]
    print("  5D bulks (kappa5^4, ell^2): %d -- %s" % (len(by_bulk), {"(%s, %s)" % kk: len(vv) for kk, vv in by_bulk.items()}))
    print("  5D geometries (ell/l5): %s; couplings in each: %s" % (
        {str(kk): len(vv) for kk, vv in by_geom.items()}, {str(kk): [str(x) for x in vv] for kk, vv in cpl.items()}))
    print("\nX2 each member as a 2b + b (2P/3): %s; the positions' lattice is index %d in it" % (
        {n: "(%s, %s)" % (a, b) for n, (a, b, ok) in o["lat"].items()}, o["idx"]))
    print("\nX3 the six's windows (w interval; weight) -- relative, absolute:")
    for n, row in o["win"].items():
        print("  %-17s %s" % (n, "; ".join("%s [%s, %s] %.6f%s" % (f, "%.4f" % r["iv"][0], "%.4f" % r["iv"][1], r["weight"],
                                                                     "" if r["agree"] else " DISAGREES p2_planck")
                                         for f, r in row.items())))
    y = o["cy"]
    print("\nX4 the cypher over the eighteen:")
    for b in ("5D", "201"):
        print("  basis %s: %d cells; E %s; audit %s" % (b, y[b]["n"], y[b]["E"], y[b]["audit"]))
    print("  201's basis admits beyond the eighteen, as (law, g, s): %s" % {
        lg: [(a, str(g), str(s_)) for a, g, s_ in v] for lg, v in y["extra201"].items()})
    print("  the finer lattice's unit cell (twenty-four) -- 5D basis: %d cells E %s; 201's: %d cells E %s" % (
        y["unit24"]["5D"]["n"], y["unit24"]["5D"]["E"], y["unit24"]["201"]["n"], y["unit24"]["201"]["E"]))
    print("  leave one out (5D basis), predicted by the other seventeen:")
    for n, row in y["loo"].items():
        print("    %-17s %s" % (n, row))
    d = o["ds"]
    if d:
        print("\nX5 what moves downstream:")
        print("  V6 G from the bulk and the plane on the six: %s" % {n: (("%.1e" % r["sms"]), ("%.1e" % r["curv"]), r["exact"])
                                                                   for n, r in d["v6"].items()})
        print("  C1 README-matched corridor at position 2 (size, mass-energy exponents): %s" % {
            n: (str(r["size"]), str(r["energy"])) for n, r in d["c1"].items()})
        print("  bodies, 1e22 kg, surface gravity against ours: %s" % {
            n: {el: "%.4f" % x for el, x in r.items()} for n, r in d["bodies"].items()})
        print("  C5 variance index (law, G, Lambda4): twelve %s cells E %s adds nothing %s; eighteen %s cells E %s adds "
              "nothing %s" % (d["c5_12"]["n"], d["c5_12"]["E"], d["c5_12"]["adds_nothing"], d["c5_18"]["n"], d["c5_18"]["E"],
                              d["c5_18"]["adds_nothing"]))
        print("  V2 the six outside the positions' 201 box: %s" % d["v2_out"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("X0 M's item-245 words verbatim in the rulings file", M245 in rul)
    fd = o["fd"]
    by_bulk, by_geom, cpl = o["bg"]
    ok = len(fd) == 18 and all(v["agree"] for v in fd.values())
    ok &= all(v["e"]["ell_l5"] * 3 == -v["e"]["sigma_planck"] for v in fd.values())
    e3, e5 = fd["2P/3"]["e"], fd["2b+2P*2/3"]["e"]
    ok &= (e3["k4"], e3["ell2"], e3["ell_l5"], e3["sigma_planck"]) == (1, F(1, 3), 0, 0)
    ok &= (e5["k4"], e5["ell2"], e5["ell_l5"], e5["sigma_planck"]) == (3, F(-1, 3), F(-2, 3), 2)
    ok &= len(by_bulk) == 6 and sorted(by_geom) == [F(-2, 3), F(0)]
    ok &= cpl[F(0)] == [0, 1, 3] and cpl[F(-2, 3)] == [1, 3, 4]
    add("X1 the six's 5D side exact and agreeing with p2_planck.sector (1e-12); six 5D bulks; still two geometries -- 2P/3 "
        "in ours' (Planck-unit tension ours, as 2P), 2b + 2/3 2P in 2b's; couplings ours' x1, x2, x8 and 2b's x2, x8, x16", ok)
    lat = o["lat"]
    ok = all(okk for a, b, okk in lat.values()) and o["idx"] == 3
    ok &= lat["2P/3"][:2] == (0, 1) and lat["2b+2P*2/3"][:2] == (1, 2) and lat["2P"][:2] == (0, 3)
    ok &= (fd["2P/3"]["i"], fd["2P/3"]["j"]) == (0, F(1, 3)) and (fd["2b+2P*2/3"]["i"], fd["2b+2P*2/3"]["j"]) == (1, F(2, 3))
    add("X2 all eighteen are whole-number combinations of 2b and 2P/3; the positions' lattice has index 3 in it; the six at "
        "(i, j) = (0, 1/3) and (1, 2/3)", ok)
    W = o["k"]["W"]
    win = o["win"]
    ok = len(win) == 6 and all(r["agree"] for row in win.values() for r in row.values())
    ok &= abs(win["2P/3"]["rel"]["weight"] - (W - 1 / 3) / W) < 1e-12 and abs(win["2P/3"]["abs"]["weight"] - (W - 2 / 3) / W) < 1e-12
    ok &= abs(win["2b+2P*2/3"]["rel"]["weight"] - (W - 2) / W) < 1e-12
    ok &= abs(win["2b+2P*2/3"]["abs"]["weight"] - (W - 10 / 3) / W) < 1e-12
    add("X3 the six's windows agree with p2_planck.window (1e-9); weights 2P/3 (W-1/3)/W, (W-2/3)/W; 2b + 2/3 2P (W-2)/W, "
        "(W-10/3)/W; all plausible", ok)
    y = o["cy"]
    ok = y["5D"]["n"] == 18 and all(y["5D"]["E"][lg] == 0 for lg in LANGS)
    ok &= not y["5D"]["audit"]["keys"] and not y["5D"]["audit"]["onehot"] and y["201"]["n"] == 18
    ok &= all(y["loo"][n]["order"] and y["loo"][n]["algebra"] for n in SIX)
    ok &= not any(y["loo"][n][lg] for n in ("2a-mirror", "2b+2P") for lg in ("order", "algebra", "geometry", "information"))
    ok &= y["201"]["E"]["order"] == 6 and y["201"]["E"]["algebra"] == 6 and y["201"]["E"]["information"] == 3
    ok &= sorted({(g, s_) for v in y["extra201"].values() for law, g, s_ in v}) == [(F(2, 3), F(-4, 3)), (F(4, 3), F(-2, 3))]
    ok &= all(y["unit24"][b]["n"] == 24 and all(y["unit24"][b]["E"][lg] == 0 for lg in LANGS) for b in ("5D", "201"))
    add("X4 the eighteen in the 5D basis are closed in every language (E = 0), no key, no one-hot; each of the six is "
        "predicted by the other seventeen under order and algebra, 2a-mirror and 2b+2P by none; in 201's basis six more "
        "are admitted (G x 2^(2/3) and 2^(4/3)), and the twenty-four of the finer unit cell are closed in both bases", ok)
    d = o["ds"]
    ok = d is not None
    if ok:
        ok &= all(r["sms"] < 1e-12 and r["curv"] < 1e-12 and r["exact"] for r in d["v6"].values())
        ok &= d["c1"]["2P/3"] == dict(size=F(1, 6), energy=F(-1, 6)) and d["c1"]["2b+2P*2/3"] == dict(size=F(5, 6),
                                                                                                     energy=F(-5, 6))
        ok &= all(d["v2_out"].values()) and d["c5_12"]["n"] == 12 and d["c5_18"]["n"] == 18
        ok &= all(x > 0 for r in d["bodies"].values() for x in r.values())
    add("X5 downstream: V6 holds on the six; C1's corridor at 2P/3 x 2^(1/6) in size, x 2^(-1/6) in mass-energy, at 2b + 2/3 "
        "2P x 2^(5/6), x 2^(-5/6); V2's box excludes the six; C5's variance index re-run over the eighteen", ok)
    return res


MUTANTS = {"wrong_third": "2P/3 given the tension x 2^(-1/3)",
           "drop_six": "three of the six left out",
           "integer_cast": "fractional exponents truncated to integers in the cypher's cells"}


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
        print("  mutant %-13s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
